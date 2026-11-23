"""Commande de création de l'instance de relecture décisive du barreau 5, version 3 : la commande de la version 2, à deux
remplacements près. Code neuf (R12), écrit le 2026-11-22 ; aucune instance n'est créée, arrêtée ni détruite ici, aucun
réseau n'est atteint : la commande est imprimée.

Pièce qui commande : erratum de chaîne de la relecture décisive du barreau 5, v2,
`docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/erratum-chaine-relecture-decisive-b5f-v2.md`
(`01298f0f…`, constante `ERRATUM_SHA256`), § 4.3 ; accord GO-2026-11-22-147 ; vérification des corrections
`verification-corrections-erratum-chaine-b5f-v1.md` (trois précisions, appliquées ici et dans `ouverture_suffixes_v1`).

Le défaut corrigé (§ 2) : le clone partiel des entrées de lecture (`scripts/amorce_b5f_lecture_v1.sh`, l. 362) reçoit
l'aide d'identification par `-c` seulement ; `checkout` tire ses fichiers en différé, sans aide, et le dépôt privé refuse.
La correction est une ligne ajoutée juste après la l. 362 (`PAIRE_AMORCE`), qui inscrit l'aide dans le clone des entrées :
amorce `54a676f3…` → `0adb6efb…`. L'arbre gelé du commit de la marche reste celui de `CODE-LECTURE-B5F` : l'amorce
corrigée part par la commande, qui la calcule (`amorce_corrigee`), la vérifie et l'embarque.

Ce que ce module change à `commande_lecture_v2.corps_recompose`, et rien d'autre (§ 4.3 (f)) :
- **le commit de code** vient des vérifications (d), (d'), (c'1), (c'2) et (b'), dans cet ordre, après (a) :
  `commit_de_code_verifie` ;
- **l'amorce embarquée** est `amorce_corrigee(_montrer(racine, commit, AMORCE))`.

Les vérifications :
- (a) inchangée : `relecture_v1.exiger_code_du_commit` (dans le corps) ;
- (d) inchangée : `commande_lecture_v2.commit_de_commande_cite`, qui rend le commit v2 ;
- (d') la ligne d'épinglage, unique, sous la table du registre propre, au format exact de `_EPINGLAGE` (règles C11 :
  colonne 1, aucune espace retirée, liste fermée, espaces ordinaires et forme composée seulement ; l'erratum, l'accord et
  la branche égaux aux constantes ; l'empreinte du rapport de vérification lue pour sa forme) : `commit_v3_epingle`, qui
  rend le commit v3 ;
- (c'1) la vérification (c) de la version 2, rejouée sur le commit v2 cité :
  `commande_lecture_v2.exiger_commande_issue_du_code_fige(racine, commit_lecture, v2)` ;
- (c'2) le commit v3 descend du commit v2 et n'en diffère, sur les chemins gelés, que par des ajouts, tous de
  `LISTE_FERMEE_V3`, en mode 100644 ou 100755 (un lien ou un sous-module refusé) ; les deux modules et les deux lanceurs
  y sont : `exiger_v3_issu_de_v2` ;
- (b') l'arbre de la session est le commit v3 : `commande_lecture_v2.exiger_session_au_commit_de_commande(racine, v3)`.
Avec (c'1) et (c'2), les fonctions de la version 2 qu'importe ce module sont exactement celles du commit v2 vérifié.

Recomposition, jamais substitution : les fonctions et constantes des versions 1 et 2 sont importées sans être copiées ;
les deux objets privés qu'emploie le corps (`_montrer`, `_RUN_LECTURE`) sont récrits ici à l'identique. Aucun attribut d'un
module figé n'est affecté. Seule entrée : `commande_de_creation_v3` (« commande decisif »), depuis l'arbre de la session au
commit v3 (`scripts/lancer_b5f_lecture_v3.sh`, qui imprime l'empreinte de l'amorce embarquée et refuse toute commande dont
le segment décodé n'a pas l'empreinte `0adb6efb…`, condition d'arrêt C12). Toutes les autres sous-commandes restent à
`scripts/lancer_b5f_lecture_v1.sh`, depuis un arbre au code de lecture figé.

Épreuves : `tests/test_commande_lecture_v3.py` et `tests/test_amorce_b5f_lecture_identification_v1.py`, écrites avant ce
module.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

from ..gardes import GardeArret
from . import engagement_v1 as en
from . import lecture_v1 as lv
from .commande_lecture_v2 import (commit_de_commande_cite, exiger_commande_issue_du_code_fige, exiger_offre_lecture_v2,
                                  exiger_session_au_commit_de_commande)
from .relecture_v1 import (AMORCE, BRANCHE_ENTREES, DEPOT_URL, ENTREES_DE_LA_MARCHE, IMAGE, PIECES_LECTURE, config_lecture,
                           echeance_arret_lecture_s, exiger_arbre_extrait_propre, exiger_code_du_commit,
                           exiger_registre_de_relecture, hashlib_sha256, piece_lecture)

COMMANDE = "python -m controle_ia.barreau5_familles.commande_lecture_v3"
ERRATUM = "docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/erratum-chaine-relecture-decisive-b5f-v2.md"
ERRATUM_SHA256 = "01298f0f73a731e6ee31e0e91b45367da75ba1bd2276ba5d041000b9f87da87b"
ACCORD_RELANCE = "GO-2026-11-22-147"
BRANCHE_SORTIE = "donnees/barreau5-familles-jumelles-v1-lecture"
AMORCE_FIGEE_SHA256 = "54a676f35bde811e8ebcfb0f643d510c2a1a79ca6a8554d61b7a39dd8e44453f"
AMORCE_CORRIGEE_SHA256 = "0adb6efba0a430f11c30e01da52787ef0482e20f6d74f699dbe8d76d2d300001"
_L362 = ('    git -c credential.helper="$AIDE" clone -q --filter=blob:none --no-checkout --single-branch --branch '
         '"$BRANCHE_ENTREES" "$DEPOT_URL" "$E" || arret "clonage des entrées de lecture" 2\n')
_AJOUT = ('    git -C "$E" config credential.helper "$AIDE" || arret "aide d\'identification non inscrite dans le clone '
          'des entrées" 2\n')
# texte ancien (la l. 362 et sa fin de ligne), texte neuf (la même, suivie de la ligne ajoutée) ; « é » composé, LF
PAIRE_AMORCE = (_L362.encode("utf-8"), (_L362 + _AJOUT).encode("utf-8"))
MODULE = "src/controle_ia/barreau5_familles/commande_lecture_v3.py"
LANCEUR = "scripts/lancer_b5f_lecture_v3.sh"
ESSAIS = "tests/test_commande_lecture_v3.py"
ESSAIS_IDENTIFICATION = "tests/test_amorce_b5f_lecture_identification_v1.py"
MODULE_OUVERTURE = "src/controle_ia/barreau5_familles/ouverture_suffixes_v1.py"
LANCEUR_OUVERTURE = "scripts/lancer_b5f_ouverture_suffixes_v1.sh"
ESSAIS_OUVERTURE = "tests/test_ouverture_suffixes_v1.py"
# la liste fermée des sept fichiers que le commit v3 ajoute au commit v2 (§ 4.3 (a)) ; rien d'autre
LISTE_FERMEE_V3 = tuple(sorted((MODULE, LANCEUR, ESSAIS, ESSAIS_IDENTIFICATION, MODULE_OUVERTURE, LANCEUR_OUVERTURE,
                                ESSAIS_OUVERTURE)))
MODES_ADMIS = ("100644", "100755")
PREFIXE_EPINGLAGE = "Erratum de chaîne de la relecture décisive (barreau 5) : "
_EPINGLAGE = re.compile(r"Erratum de chaîne de la relecture décisive \(barreau 5\) : erratum sha256 (?P<erratum>[0-9a-f]{64}) "
                        r"; code de commande v3 et d'ouverture à noms suffixés v1, commit (?P<commit>[0-9a-f]{40}), "
                        r"vérifié sha256 (?P<rapport>[0-9a-f]{64}) ; accord (?P<accord>GO-[0-9]{4}-[0-9]{2}-[0-9]{2}-"
                        r"[0-9]{2,3}) ; branche de sortie (?P<branche>[A-Za-z0-9._/-]+)", re.ASCII)
_ESPACES = re.compile(r"\s", re.UNICODE)
# objets privés de la version 1 récrits à l'identique (`relecture_v1._RUN_LECTURE`, `relecture_v1._montrer`)
_RUN_LECTURE = re.compile(r"[0-9]{8}-[0-9]{6}-(?P<suffixe>b5f-lecture|b5f-repetition)")


# --- l'amorce corrigée (§ 3.1, § 4.3 (c)) -------------------------------------------------------------------------------

def remplacer_paire(octets: bytes, sha_entree: str, paire: tuple[bytes, bytes], sha_sortie: str) -> bytes:
    """Exige l'empreinte d'entrée ; le texte ancien présent une fois et une seule ; remplace ; exige l'empreinte de
    sortie ; rend les octets. Toute autre entrée : refus."""
    if not isinstance(octets, bytes) or hashlib.sha256(octets).hexdigest() != sha_entree:
        raise GardeArret(f"amorce d'une autre empreinte que {sha_entree[:12]}… : refus (erratum de chaîne, § 4.3 (c))")
    ancien, neuf = paire
    if octets.count(ancien) != 1:
        raise GardeArret(f"amorce : le texte ancien y est {octets.count(ancien)} fois, une fois et une seule attendue")
    sortie = octets.replace(ancien, neuf)
    if hashlib.sha256(sortie).hexdigest() != sha_sortie:
        raise GardeArret(f"amorce corrigée d'une autre empreinte que {sha_sortie[:12]}… : refus")
    return sortie


def amorce_corrigee(octets: bytes) -> bytes:
    """L'amorce figée (`54a676f3…`), la ligne de l'aide d'identification ajoutée juste après la l. 362 : `0adb6efb…`."""
    return remplacer_paire(octets, AMORCE_FIGEE_SHA256, PAIRE_AMORCE, AMORCE_CORRIGEE_SHA256)


# --- (d') la ligne d'épinglage -------------------------------------------------------------------------------------------

def _candidate(ligne: str) -> bool:
    """Une ligne qui veut être la ligne d'épinglage : après normalisation (forme composée, toute espace ramenée à
    U+0020, espaces de tête ôtées), elle commence par le préfixe. Elle doit alors égaler le format, à la lettre."""
    vue = _ESPACES.sub(" ", unicodedata.normalize("NFC", ligne)).lstrip(" ")
    return vue.startswith(PREFIXE_EPINGLAGE.rstrip(" ")) or vue.startswith("| " + PREFIXE_EPINGLAGE.rstrip(" "))


def commit_v3_epingle(texte_registre: str) -> str:
    """Vérification (d'). Une et une seule ligne du registre propre porte le préfixe d'épinglage ; elle commence en
    colonne 1 et égale, à la lettre, le format de l'erratum (aucune espace retirée, espaces ordinaires et forme composée
    seulement) ; elle cite l'erratum à `ERRATUM_SHA256`, l'accord `ACCORD_RELANCE` et la branche `BRANCHE_SORTIE`. Rend le
    commit v3 ; sinon refus."""
    candidates = [x for x in texte_registre.split("\n") if _candidate(x)]
    if not candidates:
        raise GardeArret("ligne d'épinglage de l'erratum de chaîne absente du registre propre : refus (§ 4.3 (d))")
    if len(candidates) != 1:
        raise GardeArret(f"lignes d'épinglage de l'erratum de chaîne : {len(candidates)}, une et une seule attendue : refus")
    ligne = candidates[0]
    m = _EPINGLAGE.fullmatch(ligne)
    if m is None or not ligne.startswith(PREFIXE_EPINGLAGE) or not unicodedata.is_normalized("NFC", ligne):
        raise GardeArret("ligne d'épinglage hors du format exact de l'erratum (colonne 1, espaces ordinaires, forme "
                         "composée, champs à la lettre) : refus")
    if m["erratum"] != ERRATUM_SHA256:
        raise GardeArret(f"ligne d'épinglage : erratum {m['erratum'][:12]}… ≠ {ERRATUM_SHA256[:12]}… : refus")
    if m["accord"] != ACCORD_RELANCE:
        raise GardeArret(f"ligne d'épinglage : accord {m['accord']} ≠ {ACCORD_RELANCE} : refus")
    if m["branche"] != BRANCHE_SORTIE:
        raise GardeArret(f"ligne d'épinglage : branche de sortie {m['branche']} ≠ {BRANCHE_SORTIE} : refus")
    return m["commit"]


# --- (c'2) du commit v2 au commit v3 --------------------------------------------------------------------------------------

def exiger_v3_issu_de_v2(racine: Path, v2: str, v3: str) -> list[str]:
    """Vérification (c'2). Le commit v3 descend du commit v2 ; de l'un à l'autre, sur les chemins gelés, seulement des
    ajouts, tous de `LISTE_FERMEE_V3`, en mode 100644 ou 100755 ; les deux modules et les deux lanceurs y sont. Rend la
    liste des fichiers ajoutés."""
    from ..harnais.validation_reelle import CHEMINS_GELES
    a = subprocess.run(["git", "-C", str(racine), "merge-base", "--is-ancestor", v2, v3], capture_output=True)
    if a.returncode != 0:
        raise GardeArret(f"commit v3 {v3[:12]} : absent, ou ne descend pas du commit v2 {v2[:12]}")
    n = subprocess.run(["git", "-C", str(racine), "diff", "--raw", "--no-renames", "--no-abbrev", "-z", v2, v3, "--",
                        *CHEMINS_GELES], capture_output=True)
    if n.returncode != 0:
        raise GardeArret(f"différence entre le commit v2 {v2[:12]} et le commit v3 {v3[:12]} illisible")
    champs = [x for x in n.stdout.decode("utf-8").split("\0") if x]
    if len(champs) % 2:
        raise GardeArret("différence du commit v3 illisible")
    ajoutes = []
    for meta, chemin in zip(champs[0::2], champs[1::2]):
        m = re.fullmatch(r":(?P<avant>[0-7]{6}) (?P<apres>[0-7]{6}) [0-9a-f]{40} [0-9a-f]{40} (?P<etat>[A-Z])[0-9]*", meta)
        if m is None:
            raise GardeArret("différence du commit v3 illisible")
        if m["etat"] != "A":
            raise GardeArret(f"commit v3 {v3[:12]} : fichier existant modifié ou supprimé ({m['etat']} {chemin}) : il ne "
                             "doit qu'ajouter")
        if chemin not in LISTE_FERMEE_V3:
            raise GardeArret(f"commit v3 {v3[:12]} : fichier ajouté hors de la liste fermée ({chemin})")
        if m["apres"] not in MODES_ADMIS:
            raise GardeArret(f"commit v3 {v3[:12]} : {chemin} en mode {m['apres']} (lien ou sous-module) : seuls "
                             f"{' et '.join(MODES_ADMIS)} sont admis")
        ajoutes.append(chemin)
    for f in (MODULE, LANCEUR, MODULE_OUVERTURE, LANCEUR_OUVERTURE):
        if f not in ajoutes:
            raise GardeArret(f"{f} absent du commit v3 {v3[:12]} (ou déjà au commit v2)")
    return sorted(ajoutes)


def commit_de_code_verifie(racine: Path, commit_lecture: str, texte_registre: str) -> tuple[str, str]:
    """(d), (d'), (c'1), (c'2) et (b'), dans cet ordre, sur le registre donné. Rend (commit v2, commit v3)."""
    v2 = commit_de_commande_cite(texte_registre)
    v3 = commit_v3_epingle(texte_registre)
    exiger_commande_issue_du_code_fige(racine, commit_lecture, v2)
    exiger_v3_issu_de_v2(racine, v2, v3)
    exiger_session_au_commit_de_commande(racine, v3)
    return v2, v3


def _montrer(racine: Path, commit: str, chemin: str) -> bytes:
    r = subprocess.run(["git", "-C", str(racine), "show", f"{commit}:{chemin}"], capture_output=True)
    if r.returncode != 0:
        raise GardeArret(f"{chemin} absent du commit {commit[:12]}")
    return r.stdout


# --- le corps recomposé de `commande_lecture_v2.corps_recompose` ------------------------------------------------------

def corps_recompose(racine: Path, plan: str, offre_json: Path, commit: str, branche: str, run_id: str, go_id: str,
                    entrees_commit: str, divergence: bool, garde: str, existants_json: Path, aujourd_hui,
                    maintenant_s: float) -> str:
    """Le corps de `commande_lecture_v2.corps_recompose`, ligne pour ligne dans le même ordre, à deux remplacements près :
    le commit de code (vérifications (d), (d'), (c'1), (c'2) et (b'), à la place de (d), (b) et (c)) et l'amorce
    embarquée (`amorce_corrigee`). Toutes les autres gardes sont rejouées telles quelles. **Ce n'est pas une entrée** :
    `commande_de_creation_v3`."""
    import base64

    from .formation_v1 import exiger_garde_de_calcul
    p = piece_lecture(plan)
    of = exiger_offre_lecture_v2(json.loads(Path(offre_json).read_text(encoding="utf-8")), plan)
    for nom, v in (("commit", commit), ("commit des entrées", entrees_commit)):
        if (v or nom == "commit") and not re.fullmatch(r"[0-9a-f]{40}", str(v)):
            raise GardeArret(f"{nom} (40 signes) attendu")
    if (plan == "decisif") != bool(entrees_commit):
        raise GardeArret("commit des entrées de lecture : exigé pour le plan décisif, refusé pour la répétition")
    if not re.fullmatch(r"[A-Za-z0-9._/-]+", str(branche)):
        raise GardeArret("branche du code illisible")
    m = _RUN_LECTURE.fullmatch(str(run_id))
    if m is None or m["suffixe"] != p["suffixe"]:
        raise GardeArret(f"identifiant de marche AAAAMMJJ-HHMMSS-{p['suffixe']} attendu")
    existants = json.loads(Path(existants_json).read_text(encoding="utf-8"))
    if not isinstance(existants, list):
        raise GardeArret("adaptateurs existants : liste attendue")
    config = config_lecture(racine, go_id, plan, ENTREES_DE_LA_MARCHE if plan == "decisif" else None, divergence, garde,
                            ancrages=existants if plan == "decisif" else (),
                            adaptateurs_repetition=existants if plan == "repetition" else ())
    maintenant = datetime.fromtimestamp(maintenant_s, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    reg = exiger_registre_de_relecture(_montrer(racine, commit, en.REGISTRE_PROPRE).decode("utf-8"), config, maintenant)
    exiger_code_du_commit(racine, reg["commit_lecture"], commit)
    commit_de_code_verifie(racine, reg["commit_lecture"], _montrer(racine, commit, en.REGISTRE_PROPRE).decode("utf-8"))
    if hashlib_sha256(_montrer(racine, commit, lv.TEXTE)) != lv.TEXTE_SHA256:
        raise GardeArret(f"texte {lv.TEXTE} : autre empreinte au commit de la marche (R1)")
    amorce = amorce_corrigee(_montrer(racine, commit, AMORCE))
    for x in existants:
        if subprocess.run(["git", "-C", str(racine), "cat-file", "-e", f"{commit}:{x['chemin']}"],
                          capture_output=True).returncode != 0:
            raise GardeArret(f"adaptateur existant {x['nom']} : {x['chemin']} absent du commit de la marche")
    exiger_arbre_extrait_propre(racine, commit, reg["engagement"], [x["chemin"] for x in existants])
    if plan == "decisif":
        r = subprocess.run(["git", "-C", str(racine), "branch", "-r", "--contains", entrees_commit], capture_output=True,
                           text=True)
        if r.returncode != 0 or f"origin/{BRANCHE_ENTREES}" not in r.stdout.split():
            raise GardeArret(f"commit des entrées {entrees_commit[:12]} absent de la branche distante {BRANCHE_ENTREES}")
    arret = echeance_arret_lecture_s(maintenant_s, plan, of["prix_usd_h"])
    b64 = base64.b64encode(amorce).decode("ascii")
    ex64 = base64.b64encode(json.dumps(existants, separators=(",", ":"), sort_keys=True).encode("utf-8")).decode("ascii")
    cmd = (f"GO_ID={go_id} vastai create instance {of['id']} --raw --image {IMAGE} --disk {p['disque_go']} --cancel-unavail "
           f"--label {p['etiquette']} --env \"-e PLAN_B5F={plan} -e COMMIT={commit} -e BRANCHE_CODE={branche} "
           f"-e PREREG={lv.TEXTE} -e RUN_LECTURE={run_id} -e PRIX_USD_H={of['prix_usd_h']} -e ECHEANCE_ARRET_UTC_S={arret} "
           f"-e GO_ID={go_id} -e DEPOT_URL={DEPOT_URL} -e ENTREES_COMMIT={entrees_commit or '-'} "
           f"-e DIVERGENCE_B5F={int(bool(divergence))} -e GARDE_B5F={garde} -e EXISTANTS_B5F={ex64} "
           f"-e EXISTANTS_CHEMINS={','.join(x['chemin'] for x in existants) or '-'} "
           f"-e HF_TOKEN=$HF_TOKEN -e GH_TOKEN=$GH_TOKEN\" --entrypoint bash --args -c "
           f"\"echo {b64} | base64 -d > /root/amorce_b5f_lecture_v1.sh && bash /root/amorce_b5f_lecture_v1.sh\"")
    exiger_garde_de_calcul(racine, cmd, aujourd_hui)
    return cmd


# --- la seule entrée : la relecture décisive, depuis l'arbre au commit v3 ---------------------------------------------

def exiger_module_joue_depuis(racine: Path) -> None:
    """Le module joué est celui de l'arbre de la session que vérifie (b')."""
    if Path(__file__).resolve() != (Path(racine) / MODULE).resolve():
        raise GardeArret(f"commande de lecture v3 : module joué depuis un autre arbre que celui de la session ({racine}) : "
                         f"elle ne se joue que par {LANCEUR} de l'arbre de travail au commit v3")


def commande_de_creation_v3(racine: Path, plan: str, offre_json: Path, commit: str, branche: str, run_id: str, go_id: str,
                            entrees_commit: str, divergence: bool, garde: str, existants_json: Path, aujourd_hui,
                            maintenant_s: float) -> str:
    """Commande de création de l'instance de relecture décisive, amorce corrigée embarquée. Refus : plan autre que
    « decisif » ; module joué depuis un autre arbre que `racine` ; tous les refus de `corps_recompose` ; un segment
    embarqué qui n'aurait pas l'empreinte corrigée (C12)."""
    if plan != "decisif":
        raise GardeArret(f"commande de lecture v3 : plan {plan!r} refusé ; elle ne sert que la relecture décisive ; la "
                         "répétition générale se commande par la version 1 (scripts/lancer_b5f_lecture_v1.sh)")
    exiger_module_joue_depuis(racine)
    cmd = corps_recompose(racine, plan, offre_json, commit, branche, run_id, go_id, entrees_commit, divergence, garde,
                          existants_json, aujourd_hui, maintenant_s)
    if amorce_embarquee_sha256(cmd) != AMORCE_CORRIGEE_SHA256:
        raise GardeArret("amorce embarquée d'une autre empreinte que l'amorce corrigée : refus (C12)")
    return cmd


def amorce_embarquee_sha256(cmd: str) -> str:
    """Empreinte du seul segment base64 de la commande, décodé (refus s'il n'y en a pas exactement un)."""
    import base64
    import binascii

    segments = re.findall(r"echo ([A-Za-z0-9+/=]+) \| base64 -d > /root/amorce_b5f_lecture_v1\.sh", cmd)
    if len(segments) != 1 or cmd.count("base64 -d") != 1:
        raise GardeArret("commande : un et un seul segment d'amorce embarquée attendu (C12)")
    try:
        return hashlib.sha256(base64.b64decode(segments[0], validate=True)).hexdigest()
    except binascii.Error:
        raise GardeArret("commande : segment d'amorce embarquée illisible (C12)") from None


def _main(argv: list[str]) -> int:
    from datetime import date
    if argv[:1] != ["commande"] or len(argv) != 12:
        raise GardeArret("attendu : commande PLAN RACINE OFFRE.json COMMIT BRANCHE_CODE RUN_ID GO_ID ENTREES_COMMIT "
                         "DIVERGENCE GARDE EXISTANTS.json (seule sous-commande de la version 3)")
    plan, racine, offre, commit, branche, run_id, go_id, entrees_commit, divergence, garde, existants = argv[1:]
    if divergence not in ("0", "1"):
        raise GardeArret("DIVERGENCE : 0 ou 1")
    print(commande_de_creation_v3(Path(racine), plan, Path(offre), commit, branche, run_id, go_id,
                                  "" if entrees_commit == "-" else entrees_commit, divergence == "1", garde,
                                  Path(existants), date.today(), time.time()))
    return 0


__all__ = ["ERRATUM_SHA256", "ACCORD_RELANCE", "BRANCHE_SORTIE", "AMORCE_FIGEE_SHA256", "AMORCE_CORRIGEE_SHA256",
           "PAIRE_AMORCE", "LISTE_FERMEE_V3", "remplacer_paire", "amorce_corrigee", "commit_v3_epingle",
           "exiger_v3_issu_de_v2", "commit_de_code_verifie", "commande_de_creation_v3", "amorce_embarquee_sha256"]


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
