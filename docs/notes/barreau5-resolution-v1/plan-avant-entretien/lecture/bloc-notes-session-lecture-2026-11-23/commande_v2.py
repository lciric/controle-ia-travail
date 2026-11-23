"""Commande de création de l'instance de relecture du barreau 5, version 2 : la seule sous-commande « commande », pour la
seule relecture décisive, côté session. Code neuf (R12), écrit le 2026-11-21 ; aucune instance n'est créée, arrêtée ni
détruite ici, aucun réseau n'est atteint : la commande est imprimée.

Pièce qui commande : additif 1, version 2, au devis du barreau 5,
`docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-additif-1-v2.md`
(`c3120d3a…`, constante `ADDITIF_SHA256`), § 3 ; accords GO-2026-11-21-42 et GO-2026-11-21-45.

Ce que ce module change à `relecture_v1.commande_de_creation`, et rien d'autre (§ 3.1) :
- **la garde du stockage** : `exiger_offre_lecture_v2`, plafond par pièce (`PLAFOND_STOCKAGE_USD_H` : relecture décisive
  0,12 USD de l'heure ; répétition générale 0,08, inchangée) ; même formule (`storage_cost` × disque de la pièce / 730),
  mêmes autres bornes lues dans `relecture_v1.OFFRE_LECTURE`, même refus d'un champ absent ou illisible, même valeur rendue ;
- **la garde de l'arbre de la session** (`lecture_v1.exiger_code_de_lecture_au_commit`, qui refuserait le commit de
  commande, puisqu'il ajoute des fichiers sous des chemins gelés) est remplacée par les vérifications (d), (b) et (c).

Les quatre vérifications :
- (a) l'arbre gelé du commit de la marche égale celui du commit du code de lecture figé : `relecture_v1.exiger_code_du_commit`,
  importée, inchangée ; le commit de la marche ne porte pas ce module, et l'instance joue la version 1 ;
- (b) l'arbre de la session est le commit de commande : `exiger_session_au_commit_de_commande` (la tête est ce commit,
  aucun changement de l'arbre de travail sur les chemins gelés, aucun fichier non suivi sous `src/`) ;
- (c) le commit de commande descend du commit du code de lecture figé et n'en diffère, sur les chemins gelés, que par des
  fichiers ajoutés, tous de la liste fermée `LISTE_FERMEE`, le module et le lanceur y étant :
  `exiger_commande_issue_du_code_fige` ;
- (d) la colonne de référence de la ligne `GO-LECTURE-B5F` (l'accord de lecture), au commit de la marche, cite l'additif par
  son empreinte et le commit de commande par ses 40 signes : `commit_de_commande_cite`. C'est elle qui dit à (b) et à (c)
  quel commit est le commit de commande. Format lu à la lettre (ni barre verticale ni saut de ligne) :

      <nom de la session de lecture> ; additif 1 v2 au devis sha256 <64 signes> ; commande de lecture v2, commit <40 signes>, vérifiée sha256 <64 signes>

  suivi au plus de « ; <texte libre> ». La citation n'y figure qu'une fois. L'empreinte qui suit « vérifiée » est celle du
  rapport de vérification du code ; le code n'en lit que la forme.

Recomposition, jamais substitution : `corps_recompose` récrit le corps de `relecture_v1.commande_de_creation`, ligne pour
ligne dans le même ordre, à partir des fonctions et des constantes de la version 1, importées sans être copiées. Les deux
seuls objets privés de la version 1 qu'emploie ce corps, la fonction `_montrer` et le motif `_RUN_LECTURE`, sont récrits ici,
à l'identique, et non importés. Aucun attribut d'un module figé n'est affecté. Le corps garde les deux branches du plan
(c'est ce qui le rend comparable à la version 1, à l'octet, pour les deux pièces) ; pour « repetition », aucune ligne
d'accord de lecture n'épingle le commit de commande : le corps prend alors la tête de la session, garde plus faible que
celle de la version 1 (§ 3.3). **C'est pourquoi le corps n'est pas une entrée** : la seule entrée est
`commande_de_creation_v2`, qui refuse « repetition » (la répétition générale se commande par la version 1, depuis l'arbre
au code de lecture figé) et refuse d'être jouée depuis un autre arbre que celui de la session (`exiger_module_joue_depuis` :
sans cela, (b) vérifierait un arbre et le code joué en serait un autre).

D'où se joue chaque sous-commande (§ 3.2) : seule « commande », version 2, se joue depuis l'arbre de travail au commit de
commande (`scripts/lancer_b5f_lecture_v2.sh`). Toutes les autres (« config », « verifier », « marche », « preparer »,
« ouvrir », « monde », « scores », « detruire », « verifier-destruction », et « commande » pour la répétition générale)
se jouent par `scripts/lancer_b5f_lecture_v1.sh`, depuis un arbre dont la partie gelée est celle du commit du code de lecture
figé (par exemple un arbre de travail extrait au commit de la marche), jamais depuis le commit de commande.

La garde de calcul (`formation_v1.exiger_garde_de_calcul`) lit le registre des accords de l'arbre d'où la commande est
jouée : `registres/go.md` y est tenu à jour par la session (hors des chemins gelés ; réserve 2 du scellement de l'additif).

Épreuves : `tests/test_commande_lecture_v2.py`, écrites avant ce module.
"""
from __future__ import annotations

import json
import math
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from ..gardes import GardeArret
from . import engagement_v1 as en
from . import lecture_v1 as lv
from .relecture_v1 import (AMORCE, BRANCHE_ENTREES, DEPOT_URL, ENTREES_DE_LA_MARCHE, IMAGE, OFFRE_LECTURE, PIECES_LECTURE,
                           config_lecture, echeance_arret_lecture_s, exiger_arbre_extrait_propre, exiger_code_du_commit,
                           exiger_registre_de_relecture, hashlib_sha256, piece_lecture)

COMMANDE = "python -m controle_ia.barreau5_familles.commande_lecture_v2"
ADDITIF = "docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1-additif-1-v2.md"
ADDITIF_SHA256 = "c3120d3ade40f31f26a225cd2bf7c3520c7ba0a314e2b554832229d67c8e120c"
MODULE = "src/controle_ia/barreau5_familles/commande_lecture_v2.py"
LANCEUR = "scripts/lancer_b5f_lecture_v2.sh"
ESSAIS = "tests/test_commande_lecture_v2.py"
# liste fermée des fichiers que le commit de commande ajoute au commit du code de lecture figé (§ 3.1) ; rien d'autre
LISTE_FERMEE = (LANCEUR, MODULE, ESSAIS)
# additif, § 1 : stockage de l'instance de relecture (300 Go) au plus 0,12 USD de l'heure ; la répétition générale (150 Go)
# garde la borne scellée de 0,08 (`relecture_v1.OFFRE_LECTURE["stockage_max_usd_h"]`)
PLAFOND_STOCKAGE_USD_H = {"decisif": 0.12, "repetition": 0.08}
# objets privés de la version 1 récrits à l'identique (`relecture_v1._RUN_LECTURE`, `relecture_v1._montrer`)
_RUN_LECTURE = re.compile(r"[0-9]{8}-[0-9]{6}-(?P<suffixe>b5f-lecture|b5f-repetition)")
_CITATION = re.compile(r"[^|\n]+ ; additif 1 v2 au devis sha256 (?P<additif>[0-9a-f]{64}) ; commande de lecture v2, "
                       r"commit (?P<commit>[0-9a-f]{40}), vérifiée sha256 (?P<rapport>[0-9a-f]{64})(?: ; [^|\n]*)?")


# --- la garde du stockage, plafond par pièce --------------------------------------------------------------------------

def exiger_offre_lecture_v2(offre: dict, plan: str) -> dict:
    """Bornes du devis sur une offre du loueur (champs bruts) pour la pièce du plan, comme `relecture_v1.exiger_offre_lecture`
    (A100 SXM4 80 Go, une carte, au plus 1,30 USD de l'heure, au moins 16 cœurs et 128 Go de mémoire vive, disque de la
    pièce, CUDA au moins 13.0), au plafond du stockage près : celui de la pièce (`PLAFOND_STOCKAGE_USD_H` : 0,12 USD de
    l'heure pour la relecture décisive, additif 1 v2 ; 0,08 pour la répétition générale). Champ absent ou illisible :
    refus."""
    p = piece_lecture(plan)

    def nombre(cle):
        v = offre.get(cle)
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
            raise GardeArret(f"offre : champ {cle} absent ou illisible")
        return float(v)
    nom = str(offre.get("gpu_name", ""))
    if not all(x in nom.replace("_", " ") for x in OFFRE_LECTURE["nom_offre"]):
        raise GardeArret(f"offre : carte {nom!r}, A100 SXM4 80 Go attendue")
    for cle, borne, sens in (("num_gpus", 1, "="), ("gpu_ram", OFFRE_LECTURE["memoire_carte_min_mo"], ">="),
                             ("cpu_cores_effective", OFFRE_LECTURE["coeurs_min"], ">="),
                             ("cpu_ram", OFFRE_LECTURE["memoire_vive_min_mo"], ">="), ("disk_space", p["disque_go"], ">="),
                             ("cuda_max_good", OFFRE_LECTURE["cuda_min"], ">="),
                             ("dph_total", OFFRE_LECTURE["prix_max_usd_h"], "<=")):
        v = nombre(cle)
        if (sens == "=" and v != borne) or (sens == ">=" and v < borne) or (sens == "<=" and not 0 < v <= borne):
            raise GardeArret(f"offre : {cle} = {v} hors de la borne du devis ({sens} {borne})")
    stockage_h = nombre("storage_cost") * p["disque_go"] / 730.0
    if stockage_h > PLAFOND_STOCKAGE_USD_H[plan]:
        raise GardeArret(f"offre : stockage de {p['disque_go']} Go à {stockage_h:.3f} USD de l'heure > "
                         f"{PLAFOND_STOCKAGE_USD_H[plan]}")
    if not str(offre.get("id")).isdigit():
        raise GardeArret("offre : identifiant illisible")
    return {"id": str(offre["id"]), "prix_usd_h": nombre("dph_total")}


# --- vérifications (d), (b) et (c) ---------------------------------------------------------------------------------------

def commit_de_commande_cite(texte_registre: str) -> str:
    """Vérification (d). La colonne de référence de la ligne `GO-LECTURE-B5F` du registre propre (lu par le lecteur de la
    version 1 : une clé inconnue ou en double refuse) cite, une seule fois et au format exact du module, l'additif 1 v2 à
    son empreinte (`ADDITIF_SHA256`) et le commit de commande par ses 40 signes. Rend ce commit ; sinon refus."""
    ref = en.lignes_du_registre(texte_registre).get("GO-LECTURE-B5F", {}).get("ref", "")
    m = _CITATION.fullmatch(ref)
    if m is None or ref.count("additif 1 v2 au devis") != 1 or ref.count("commande de lecture v2") != 1:
        raise GardeArret("GO-LECTURE-B5F : la colonne de référence ne cite pas, une fois et à la lettre, « <session de "
                         "lecture> ; additif 1 v2 au devis sha256 <64 signes> ; commande de lecture v2, commit <40 signes>, "
                         "vérifiée sha256 <64 signes> » : refus (additif 1 v2, § 3.1, vérification (d))")
    if m["additif"] != ADDITIF_SHA256:
        raise GardeArret(f"GO-LECTURE-B5F : la colonne de référence cite l'additif à une autre empreinte "
                         f"({m['additif'][:12]}…) que celle de l'additif 1 v2 ({ADDITIF_SHA256[:12]}…) : refus")
    return m["commit"]


def commit_de_commande(racine: Path, plan: str, texte_registre: str) -> str:
    """Le commit de commande. Relecture décisive : celui que cite la ligne de l'accord de lecture, au commit de la marche
    (vérification (d)). Répétition générale : aucune ligne d'accord de lecture ne l'épingle ; la tête de la session
    (branche gardée pour l'égalité à l'octet avec la version 1 ; l'entrée `commande_de_creation_v2` la refuse)."""
    if plan == "decisif":
        return commit_de_commande_cite(texte_registre)
    t = subprocess.run(["git", "-C", str(racine), "rev-parse", "--verify", "HEAD^{commit}"], capture_output=True, text=True)
    if t.returncode != 0 or not re.fullmatch(r"[0-9a-f]{40}", t.stdout.strip()):
        raise GardeArret("tête de la session illisible")
    return t.stdout.strip()


def exiger_session_au_commit_de_commande(racine: Path, commande: str) -> None:
    """Vérification (b). L'arbre de la session est le commit de commande : la tête est ce commit ; aucun changement de
    l'arbre de travail sur les chemins gelés (`CHEMINS_GELES`) ; aucun fichier non suivi sous `src/` (les deux dernières
    clauses sont celles de `lecture_v1.exiger_code_de_lecture_au_commit`, gardées)."""
    from ..harnais.validation_reelle import CHEMINS_GELES
    t = subprocess.run(["git", "-C", str(racine), "rev-parse", "--verify", "HEAD^{commit}"], capture_output=True, text=True)
    if t.returncode != 0 or t.stdout.strip() != commande:
        raise GardeArret(f"tête de la session {t.stdout.strip()[:12] or 'illisible'} ≠ commit de commande {commande[:12]} "
                         "que cite GO-LECTURE-B5F : la commande de lecture v2 ne se joue que depuis ce commit")
    d = subprocess.run(["git", "-C", str(racine), "diff", "--quiet", commande, "--", *CHEMINS_GELES], capture_output=True)
    if d.returncode != 0:
        raise GardeArret(f"arbre de travail de la session changé sur les chemins gelés (commit de commande {commande[:12]})")
    u = subprocess.run(["git", "-C", str(racine), "ls-files", "--others", "--exclude-standard", "--", "src"],
                       capture_output=True, text=True)
    if u.returncode != 0 or u.stdout.strip():
        raise GardeArret("arbre de la session : fichier non suivi sous src/ (ou arbre illisible)")


def exiger_commande_issue_du_code_fige(racine: Path, commit_lecture: str, commande: str) -> list[str]:
    """Vérification (c). Le commit de commande descend du commit du code de lecture figé et n'en diffère, sur les chemins
    gelés, que par des fichiers ajoutés, tous de `LISTE_FERMEE` (aucun fichier modifié, supprimé ni retypé, aucun ajouté
    hors liste) ; le module et le lanceur de la version 2 y sont ajoutés. Rend la liste des fichiers ajoutés."""
    from ..harnais.validation_reelle import CHEMINS_GELES
    a = subprocess.run(["git", "-C", str(racine), "merge-base", "--is-ancestor", commit_lecture, commande], capture_output=True)
    if a.returncode != 0:
        raise GardeArret(f"commit de commande {commande[:12]} : absent, ou ne descend pas du commit de CODE-LECTURE-B5F "
                         f"{commit_lecture[:12]}")
    n = subprocess.run(["git", "-C", str(racine), "diff", "--name-status", "--no-renames", "-z", commit_lecture, commande,
                        "--", *CHEMINS_GELES], capture_output=True)
    if n.returncode != 0:
        raise GardeArret(f"différence entre {commit_lecture[:12]} et le commit de commande {commande[:12]} illisible")
    champs = [x for x in n.stdout.decode("utf-8").split("\0") if x]
    if len(champs) % 2:
        raise GardeArret("différence du commit de commande illisible")
    ajoutes = []
    for etat, chemin in zip(champs[0::2], champs[1::2]):
        if etat != "A":
            raise GardeArret(f"commit de commande {commande[:12]} : fichier existant modifié ou supprimé ({etat} {chemin}) : "
                             "il ne doit qu'ajouter")
        if chemin not in LISTE_FERMEE:
            raise GardeArret(f"commit de commande {commande[:12]} : fichier ajouté hors de la liste fermée ({chemin})")
        ajoutes.append(chemin)
    for f in (MODULE, LANCEUR):
        if f not in ajoutes:
            raise GardeArret(f"{f} absent du commit de commande {commande[:12]} (ou déjà au commit du code de lecture figé)")
    return sorted(ajoutes)


def _montrer(racine: Path, commit: str, chemin: str) -> bytes:
    r = subprocess.run(["git", "-C", str(racine), "show", f"{commit}:{chemin}"], capture_output=True)
    if r.returncode != 0:
        raise GardeArret(f"{chemin} absent du commit {commit[:12]}")
    return r.stdout


# --- le corps recomposé de `relecture_v1.commande_de_creation` --------------------------------------------------------

def corps_recompose(racine: Path, plan: str, offre_json: Path, commit: str, branche: str, run_id: str, go_id: str,
                    entrees_commit: str, divergence: bool, garde: str, existants_json: Path, aujourd_hui,
                    maintenant_s: float) -> str:
    """Le corps de `relecture_v1.commande_de_creation`, ligne pour ligne dans le même ordre, à deux remplacements près : la
    garde du stockage (`exiger_offre_lecture_v2`) et la garde de l'arbre de la session (vérifications (d), (b) et (c), à la
    place de `lv.exiger_code_de_lecture_au_commit`). Toutes les autres gardes sont rejouées telles quelles par les
    fonctions de la version 1 : formats du commit, de la branche, de l'identifiant de marche et du commit des entrées ;
    configuration ; registre au commit de la marche ; code du commit de la marche (vérification (a)) ; texte scellé à son
    empreinte ; amorce présente au commit de la marche ; adaptateurs existants ; arbre extrait propre ; commit des entrées
    sur sa branche distante ; échéance d'arrêt ; garde de calcul. **Ce n'est pas une entrée** : `commande_de_creation_v2`."""
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
    commande = commit_de_commande(racine, plan, _montrer(racine, commit, en.REGISTRE_PROPRE).decode("utf-8"))
    exiger_session_au_commit_de_commande(racine, commande)
    exiger_commande_issue_du_code_fige(racine, reg["commit_lecture"], commande)
    if hashlib_sha256(_montrer(racine, commit, lv.TEXTE)) != lv.TEXTE_SHA256:
        raise GardeArret(f"texte {lv.TEXTE} : autre empreinte au commit de la marche (R1)")
    amorce = _montrer(racine, commit, AMORCE)
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


# --- la seule entrée : la relecture décisive, depuis l'arbre de commande ---------------------------------------------

def exiger_module_joue_depuis(racine: Path) -> None:
    """Le module joué est celui de l'arbre de la session que vérifie (b) : sinon (b) et (c) porteraient sur un arbre et le
    code joué en serait un autre."""
    if Path(__file__).resolve() != (Path(racine) / MODULE).resolve():
        raise GardeArret(f"commande de lecture v2 : module joué depuis un autre arbre que celui de la session ({racine}) : "
                         f"elle ne se joue que par {LANCEUR} de l'arbre de travail au commit de commande")


def commande_de_creation_v2(racine: Path, plan: str, offre_json: Path, commit: str, branche: str, run_id: str, go_id: str,
                            entrees_commit: str, divergence: bool, garde: str, existants_json: Path, aujourd_hui,
                            maintenant_s: float) -> str:
    """Commande de création de l'instance de relecture décisive (étiquette `b5f-lecture-v1`, disque de 300 Go), à jouer par
    la session de lecture. Refus : plan autre que « decisif » (la répétition générale reste à la version 1, § 3.3) ;
    module joué depuis un autre arbre que `racine` ; puis tous les refus de `corps_recompose`."""
    if plan != "decisif":
        raise GardeArret(f"commande de lecture v2 : plan {plan!r} refusé ; elle ne sert que la relecture décisive ; la "
                         "répétition générale se commande par la version 1 (scripts/lancer_b5f_lecture_v1.sh), depuis "
                         "l'arbre au code de lecture figé (additif 1 v2, § 3.3)")
    exiger_module_joue_depuis(racine)
    return corps_recompose(racine, plan, offre_json, commit, branche, run_id, go_id, entrees_commit, divergence, garde,
                           existants_json, aujourd_hui, maintenant_s)


def _main(argv: list[str]) -> int:
    from datetime import date
    if argv[:1] != ["commande"] or len(argv) != 12:
        raise GardeArret("attendu : commande PLAN RACINE OFFRE.json COMMIT BRANCHE_CODE RUN_ID GO_ID ENTREES_COMMIT "
                         "DIVERGENCE GARDE EXISTANTS.json (seule sous-commande de la version 2)")
    plan, racine, offre, commit, branche, run_id, go_id, entrees_commit, divergence, garde, existants = argv[1:]
    if divergence not in ("0", "1"):
        raise GardeArret("DIVERGENCE : 0 ou 1")
    print(commande_de_creation_v2(Path(racine), plan, Path(offre), commit, branche, run_id, go_id,
                                  "" if entrees_commit == "-" else entrees_commit, divergence == "1", garde,
                                  Path(existants), date.today(), time.time()))
    return 0


__all__ = ["ADDITIF_SHA256", "LISTE_FERMEE", "PLAFOND_STOCKAGE_USD_H", "exiger_offre_lecture_v2", "commit_de_commande_cite",
           "exiger_session_au_commit_de_commande", "exiger_commande_issue_du_code_fige", "commande_de_creation_v2"]


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
