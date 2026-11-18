#!/usr/bin/env python3
"""Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 3.

Version 3 (R12 ; v1 `015f5c33…` et v2 `9a85e78d…` restent en place, jamais lancées). Décisions de la mère R-3237 :
(1) **règle de clé par part** : chaque clé est confrontée à sa part au pire (la course ne peut pas dépenser plus sur elle),
non au plafond global ; pour Kimi, part au pire + 11,3 USD (pire cas de la course Kimi de la relance, GO-2026-11-18-17)
≤ 90 % du reste lu, sinon refus (les deux courses se suivent, solde relu avant chacune) ; le plafond d'arrêt de 150 USD est
inchangé ; (2) **dispense écrite** (référence R-3237) pour les clés d'Argon, d'Astra et de Carbon, au solde illisible :
départ permis, chaque appel passe par `scripts/garde_credit_relais_v3.py`, et **la course est arrêtée au premier refus pour
crédit** (SIGTERM à l'orchestrateur par son PID, arrêt propre) ; coût compté au prix des fichiers ; (3) **procédure neutre
des relais persistants** : pièce `course-v3/procedure-relais-persistants-course-affinage-v3.json` (chemin et empreinte de la
procédure versée par la mère) ; moteur réel refusé tant qu'elle n'est pas remplie, scellée, à son empreinte, et citée par
les portes de plafond des relais persistants. Contre-lecture : modèle K, `course-v3/`.
Codes : 0 course finie ; 2 refus avant départ, ou arrêt ou nœud de l'orchestrateur ; 3 alerte de crédit avant le départ ;
4 cumul lu au-dessus de 150 USD ; 5 course arrêtée au premier refus pour crédit d'un relais dispensé.

Texte de la v2 (inchangé sur le reste) :

Lanceur de la course d'affinage des idées des mentors par l'organisme d'idéation — version 2.

Version 2 (R12 ; la v1, `scripts/lancer_course_affinage_mentors_v1.py`, `015f5c33…`, reste en place, jamais lancée).
Ajouts (consigne de la mère, R-3228) : tous les appels Claude passent par la clé `RR_ANTHROPIC_API_KEY_MINUIT` (nom seul) ;
arrêt au départ si cette variable est absente de l'environnement du lanceur (test par le nom, jamais par la valeur) ;
refus de tout relais configuré sur une autre clé de la famille Claude, `RR_ANTHROPIC_API_KEY_RIGAUD` nommément ; crédit
de la clé Minuit compté au prix relevé quand l'interface de facturation ne le rend pas (200 USD déclarés, R-3228, moins
la dépense antérieure déclarée) ; contre-lecture par le modèle K, garde stricte (première ligne du verdict exacte, refus
d'un rapport qui dit n'avoir pas relu) ; nom de la clé écrit pour chaque relais et chaque espèce au manifeste.

Texte de la v1 (inchangé sur le reste) :

Décision N-072 (texte `docs/decisions/decision-matiere-premiere-mentors-v1.md`), GO-2026-11-18-14 (plafond d'arrêt 150 USD,
R-3215), budget des appels d'interface séparé (GO-2026-11-18-13, R-3209 point 2). Préenregistrement :
`docs/notes/organisme-affinage-mentors-v1/course-v1/preenregistrement-course-affinage-mentors-v1.md` (empreinte épinglée
ci-dessous). Modèle : le lanceur de référence `scripts/lancer_course_ideation_organismes_discrets_v7.py` (`3b20b911…`) —
mêmes gardes de GO, d'orchestrateur, de pièces, d'environnement sans clé, de bac à sable, de manifestes scellés ; mais la
course passe par la **course 2** de l'orchestrateur (`demonstrations/ideation_v8.py --course-2`, v56), qui porte
l'aiguilleur, les juges croisés aveugles et la mémoire anti-redite que la voie v2 n'a pas.

Usage, seul et exact (cwd = racine du dépôt de travail) :

    GO_ID=GO-2026-11-18-14 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v1.py

Essai à blanc (moteur simulé de l'orchestrateur, relais factices, aucune dépense, aucun GO) :

    /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v1.py --a-blanc DOSSIER_NEUF

Ce que fait le lanceur, dans cet ordre ; tout refus rend 2 (motif sur la sortie d'erreur), toute alerte de crédit avant le
départ rend 3 ; rien n'est appelé avant le manifeste de départ :
1. course jamais lancée sous ce lanceur (R12 : un dossier de run de cette course existe déjà = refus ; une relance est une
   nouvelle version et un mot de la mère) ; ligne de GO (type calcul, accordée par Lazar, période, non révoquée, plafond
   lu = 150 USD exactement) ;
2. garde (3) : préenregistrement à l'empreinte épinglée et scellé ; contre-lecture scellée, présente, qui cite l'empreinte du
   préenregistrement **et celle de ce lanceur**, au verdict « Scellable » sans réserve (sinon refus) ;
3. pièces épinglées (configuration fixe, liste des fils, consignes, enveloppe et commande d'Argon) ; liste des fils : aucune
   entrée servie dans les retraits, aucun jeton réservé dans un texte servi ;
4. déclaration des relais (écrite et scellée par la session d'exécution : adresses de boucle locale, portes de plafond, noms
   des clés, jamais une valeur) : espèces actives ; Carbon seulement si inscrite (R-3217) **et** relais et clé nommés ;
5. garde (2) : relevé du crédit de chaque clé employée (fichier scellé de la session d'exécution, du jour) : « non lisible »
   refusé sauf dispense écrite de la mère ; reste sous un cinquième du crédit ou sous le plafond d'arrêt : alerte écrite
   pour la mère (fichier et sortie), arrêt avant le départ (code 3) ;
6. orchestrateur : commit et empreintes épinglés, arbre propre (fichiers suivis, non suivis, ignorés) ;
7. garde (1) : configuration d'orchestrateur assemblée (plafond S17 = 150 = GO, portée « course », une génération, plafonds
   de relais des étapes protégées ≤ 150, passe « tableau » et fusions retirées par construction), écrite et scellée avec
   l'acte de gel ; `--verifier-seulement` de l'orchestrateur (aucun appel) exigé à 0, montant requis 150 ;
8. environnement sans clé (noms retirés, jamais une valeur), bac à sable (moteur réel), manifeste de départ scellé (R9) ;
9. course ; manifeste de fin scellé sur tout chemin ; garde (5) coût réel par relais (consommations de l'orchestrateur), écart
   au devis v3, relevé « après » estimé et alerte si un reste estimé passe sous les seuils.

Bibliothèque standard seulement (le lanceur tourne sous `-I`). Ce lanceur nomme des modèles dans la configuration qu'il
passe à l'orchestrateur (comme le lanceur de référence) ; les pièces versées n'en nomment aucun.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

VERSION = "lancer_course_affinage_mentors_v3"
GO_ID = "GO-2026-11-18-14"
PLAFOND_ARRET_USD = 150.0
INSCRIPTION_CARBON = "R-3217"
DEPOT = Path(__file__).resolve().parents[1]
COURSE_V1 = "docs/notes/organisme-affinage-mentors-v1/course-v1"
COURSE_V2 = "docs/notes/organisme-affinage-mentors-v1/course-v2"
COURSE = "docs/notes/organisme-affinage-mentors-v1/course-v3"
REFERENCE_DISPENSE = "R-3237"
FOURNISSEURS_DISPENSABLES = ("argon", "astra", "carbon")
KIMI_COURSE_SUIVANTE_PIRE_USD = 11.3   # R-3237 : pire cas de la course Kimi de la relance (GO-2026-11-18-17)
KIMI_PART_DU_RESTE = 0.9
PROCEDURE_RELAIS = f"{COURSE}/procedure-relais-persistants-course-affinage-v3.json"
MARQUEUR_A_REMPLIR = "À REMPLIR"
CLE_CLAUDE = "RR_ANTHROPIC_API_KEY_MINUIT"
CLES_INTERDITES = ("RR_ANTHROPIC_API_KEY_RIGAUD",)
PREFIXE_CLES_CLAUDE = "RR_ANTHROPIC_API_KEY"
CREDIT_DECLARE_CLE_CLAUDE_USD = 200.0  # R-3228, mot de Lazar


PREREG = f"{COURSE}/preenregistrement-course-affinage-mentors-v3.md"
PREREG_SHA256 = "a5b95e66042230f251f8cc98875cce9916795edb5747a0384e2883df4e6c178d"
CONTRE_LECTURE = f"{COURSE}/contre-lecture-preenregistrement-course-affinage-mentors-v3.md"
DECLARATION_RELAIS = f"{COURSE}/declaration-relais-course-affinage-mentors-v3.json"
RELEVE_CREDITS = f"{COURSE}/releve-credits-avant-course-affinage-mentors-v3.json"

PIECES = {
    "configuration": (f"{COURSE}/configuration-course-affinage-mentors-v3.json", "442774798ec91672c0fa00e6616f243d2d2bd38d530cbdb9675bc68210de5d8b"),
    "garde_credit": ("scripts/garde_credit_relais_v3.py", "686546a6804651e0d8091348e80fbae19b9eeebcde495a8b4faf723b09d29c43"),
    "liste_fils": (f"{COURSE_V1}/fils-servis-et-retraits-course-affinage-mentors-v1.json", "c30928c88feffc16d3aa1119efe2a54ba2d70cf135b8068855190a21470a56bb"),
    "consigne_proposeur": (f"{COURSE_V1}/consigne-proposeur-course-affinage-mentors-v1.md", "d36ba0a01c1c190d55d0ed63b053c951b5a767a9310013321d797e3e203d8c4f"),
    "consigne_aiguilleur": (f"{COURSE_V1}/consigne-aiguilleur-course-affinage-mentors-v1.md", "903318d7659db07819cbe9a7f89cbdbd292f59e14c32bb8811d8f8cb35dd955b"),
    "consigne_juge": (f"{COURSE_V1}/consigne-juge-course-affinage-mentors-v1.md", "a32583b14845343a613514cdcba3c24831a274b48ecc95fe0d884f017d27d346"),
    "consigne_passe_tableau": (f"{COURSE_V1}/consigne-passe-tableau-course-affinage-mentors-v1.md", "1ac9791b6aea1c97f534e32980f1f837cca425806ce8235b1064d98ce261dcbf"),
    "enveloppe_argon": ("rapports/fille-ideation-1-v1/appel-argon-v5.sh",
                        "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a"),
    "commande_argon": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py",
                       "46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46"),
}
PIECES_SERVIES = ("consigne_proposeur", "consigne_aiguilleur", "consigne_juge", "consigne_passe_tableau")
DEPOT_ATTENDU_PAR_L_ENVELOPPE = Path("/home/user/controle-ia-travail")

ORCHESTRATEURS_CANDIDATS = (Path("/home/user/ideation-organism/orchestrator"),
                            Path("/home/user/lciric/ideation-organism/orchestrator"))
COMMIT_ORCHESTRATEUR = "a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb"
LANCEUR_ORCHESTRATEUR = "demonstrations/ideation_v8.py"
EMPREINTES_ORCHESTRATEUR = {
    "demonstrations/ideation_v8.py": "2e2be8d72c548e183b94c14de20c971f241f998f54f64c5281b2427fdd64e9d1",
    "demonstrations/ideation_v7.py": "7b90e65e1308b1c230b3f804743cfc42b9dc571d93b73ed6c5f3f8c9d2b481b2",
    "demonstrations/ideation_v6.py": "4c302e5b97b229d5b3edd9e9a427f1e50796c10f7081f63132165ffeef854ba4",
    "demonstrations/ideation_v5.py": "1894f250264eaaccbf891dfa255e71dc587fe415c8d21e283391203a2fe73444",
    "demonstrations/ideation_v4.py": "4212d4c9d014a265847d4c4ed87a8cd804fdafa73f85fd8947874d63fca1c36d",
    "demonstrations/ideation_v2.py": "bc5e9c98acff41b97487e2345d33768c8cdf41f0ededf8b2eed0bf842c889845",
    "pole/configuration_v53.py": "ef72ffbf6b5ba546fb5e509502b59f0d9ac4f78772dcb9570ef36086639f4a78",
    "pole/configuration_v54.py": "3424ca7fa8911e5c2656cb56632f7d74c958008b9366af0ac45e6a62e4d16d66",
    "pole/configuration_v55.py": "2e6237c0a8b1c823fa17ddd6c680357a59ec4030bfbe9ac6ba970a700a864071",
    "pole/configuration_v56.py": "122405228d6ec550b2120114e87a1e70bcc74c14eee17342605d8402bd015d6b",
    "pole/course2_v53.py": "8f2d035828df913d8fa92e1b7d0c8e41ac73e8416e60f3b674753c27f5c61237",
    "pole/course2_v54.py": "ac1980d04eb88d8fbb9a073902e47146ab9eadd3375a41cd72835fa5acf20342",
    "pole/course2_v55.py": "ee6a861e7f8db32a9545372a51f902389cdbea809b0ba354e621a3681e541a70",
    "pole/course2_v56.py": "14f655696876afc8453ec5237236b3f9daf8d87844c4acc9d5189b3e61b310f1",
    "pole/budget_v56.py": "3a672aceeeee3cf83cd4e46ca461fdbaf3acd0a9552be24d2566627ce6b7c13e",
    "pole/adaptateurs.py": "a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99",
    "pole/adaptateurs_v56.py": "d36c79b272af450b8d67313f44068743d80f0204bcedbd30f5d879829c945a17",
    "pole/adaptateur_kimi_v53.py": "09a46515ff30a99f360fcbc7d4c613c35cb511439a5b6c249327e477fdee4ada",
    "pole/aiguilleur_v53.py": "a856cdaa37e8fb1f3b873ef2c0d9aa439ee0a8838f5ee9a2910cb3c0dcf8007f",
    "pole/juges_croises_v53.py": "c4c6ab12dc471eef078c116a4205a22d9b498da720ce71e37a0a6edae6c4239b",
    "pole/memoire_v53.py": "43b01b43b1ec347ff02b456975d74c17e7a0e974e9b95e9ba4935bdb895f31a0",
    "pole/noyau_v56.py": "eb5a003e8f23b0882e5588fe537e8b65b890f0d7d19560896be4e85a0731543b",
    "pole/gardes_e0_v56.py": "921e59f23753666d6367678447edf4ee2964dc6ec3d382aefa8582b996e123b9",
    "pole/simulation_v56.py": "bcafca44c5117dfd30262ee520a67944d051208f1b1deac6fac016e8cb95dc76",
    "pole/relais_reel_v2.py": "98c3e79e2c795a69345ffcf9aa742e31dde4a578a15f7c610f1ec7fd535ac8d7",
}

# Devis v5 (`devis-course-affinage-mentors-v5.md`, mêmes prix par appel que la v3), estimation par appel, USD : sert à l'écart au devis (garde 5).
DEVIS_V5_PAR_APPEL = {"prop-opus": 0.141, "prop-fable": 0.3525, "prop-argon": 0.276, "prop-kimi": 0.276, "prop-astra": 0.276,
                      "prop-carbon": 0.276, "aiguilleur": 0.031, "juge-opus": 0.037, "juge-argon": 0.0347}
DEVIS_V5_TOTAL = {"sans_carbon": 37.576, "avec_carbon": 45.2784}

DOSSIER_SORTIES = Path("/home/user/sorties-course-affinage-mentors-v3")
SUFFIXE_RUN = "-course-affinage-mentors-v3"
SUFFIXES_DEJA_LANCEE = ("-course-affinage-mentors-v1", "-course-affinage-mentors-v2", SUFFIXE_RUN)  # une seule course, quelle que soit la version
NOMS_PERMIS = ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR")
NOMS_DE_CLE = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN", "OPENAI_API_KEY", "GOOGLE_API_KEY",
               "GEMINI_API_KEY", "KIMI_API_KEY", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "GITHUB_TOKEN", "GH_TOKEN", "HF_TOKEN")
MOTIF_NOM_DE_CLE = re.compile(r"(API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL)", re.I)
MOTIF_VALEUR_DE_CLE = re.compile(r"(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|"
                                 r"AIza[0-9A-Za-z_-]{20,}|Bearer\s+[A-Za-z0-9._-]{16,})")
NOM_DE_VARIABLE = re.compile(r"^[A-Z][A-Z0-9_]{1,63}$")
URL_LOCALE = re.compile(r"^http://(127\.0\.0\.1|localhost|\[::1\]):\d{2,5}(/.*)?$")
MODELES_CLAUDE = ("claude-opus-5-5", "claude-fable-5-1")
TYPES_PERMIS = {"claude": "claude_sdk", "argon": "commande_externe", "kimi": "kimi_protocole", "astra": "commande_externe",
                "carbon": "commande_externe"}
CLES_PERMISES = {"claude_sdk": {"type", "url_relais", "porte_plafond"},
                 "commande_externe": {"type", "commande", "modeles_servis_permis", "porte_plafond"},
                 "kimi_protocole": {"type", "url_relais", "modele", "prix_entree", "prix_sortie", "max_sortie_jetons",
                                    "sortie_min_jetons", "delai_s", "porte_plafond"}}
CLES_META = {"nom_cle", "modele_propose", "inscription"}

SONDE_BAC_A_SABLE = (
    "import json, sys\n"
    "sys.path.insert(0, sys.argv[1])\n"
    "from pole.adaptateurs import etat_bac_a_sable_detaille\n"
    "print(json.dumps(etat_bac_a_sable_detaille()))\n"
)


class Refus(RuntimeError):
    """Garde du lanceur : rien n'est lancé (code 2)."""


class AlerteCredit(RuntimeError):
    """Garde (2) : un reste est sous un seuil ; alerte écrite, arrêt avant le départ (code 3)."""


def sha256_fichier(chemin: Path) -> str:
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def date_u() -> str:
    r = subprocess.run(["date", "-u"], capture_output=True, text=True, timeout=10)
    if r.returncode != 0 or not r.stdout.strip():
        raise Refus("`date -u` illisible")
    return r.stdout.strip()


def _normaliser(texte: str) -> str:
    return unicodedata.normalize("NFKD", texte.lower()).encode("ascii", "ignore").decode()


def scelle(chemin: Path) -> bool:
    """Compagnon `.sha256` présent, une ligne « empreinte  nom », égal à l'empreinte du fichier."""
    c = Path(str(chemin) + ".sha256")
    if not chemin.is_file() or not c.is_file():
        return False
    lignes = [x for x in c.read_text(encoding="utf-8").splitlines() if x.strip()]
    if len(lignes) != 1:
        return False
    m = re.match(r"^([0-9a-f]{64})  (\S.*)$", lignes[0])
    return bool(m) and m.group(2) == chemin.name and m.group(1) == sha256_fichier(chemin)


def ecrire_scelle(chemin: Path, contenu) -> str:
    if chemin.exists():
        raise Refus(f"{chemin} existe déjà (R12)")
    if isinstance(contenu, (bytes, str)):
        donnees = contenu.encode("utf-8") if isinstance(contenu, str) else contenu
    else:
        donnees = (json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {chemin.name}\n")
    return h


@dataclass
class Reglages:
    depot: Path
    orchestrateurs: tuple
    commit_orchestrateur: str
    empreintes_orchestrateur: dict
    pieces: dict
    prereg: tuple
    contre_lecture: Path
    declaration: Path
    releve: Path
    registre_go: Path
    procedure_relais: Path
    dossier_runs: Path
    dossier_sorties: Path
    depot_attendu_par_l_enveloppe: Path
    python: str
    lanceur: Path
    moteur: str = "reel"
    environnement: dict | None = None
    aujourd_hui: _dt.date | None = None
    horodatage: object = date_u
    exiger_bac_a_sable: bool = True
    verifier_go: bool = True

    @classmethod
    def production(cls) -> "Reglages":
        return cls(depot=DEPOT, orchestrateurs=ORCHESTRATEURS_CANDIDATS, commit_orchestrateur=COMMIT_ORCHESTRATEUR,
                   empreintes_orchestrateur=dict(EMPREINTES_ORCHESTRATEUR), pieces=dict(PIECES),
                   prereg=(DEPOT / PREREG, PREREG_SHA256), contre_lecture=DEPOT / CONTRE_LECTURE,
                   declaration=DEPOT / DECLARATION_RELAIS, releve=DEPOT / RELEVE_CREDITS,
                   registre_go=DEPOT / "registres" / "go.md", procedure_relais=DEPOT / PROCEDURE_RELAIS, dossier_runs=DEPOT / "runs", dossier_sorties=DOSSIER_SORTIES,
                   depot_attendu_par_l_enveloppe=DEPOT_ATTENDU_PAR_L_ENVELOPPE, python=sys.executable,
                   lanceur=Path(__file__).resolve())


# --- (1) GO, une seule course -------------------------------------------------------------------------------------------------


def _est_revocation(cellules: list, go_id: str) -> bool:
    return any(_normaliser(c).startswith("revoc") for c in cellules) and any(go_id in c for c in cellules)


def verifier_go(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_ID) -> dict:
    """Même lecture que le lanceur de référence ; plafond lu exactement égal au plafond d'arrêt (150 USD)."""
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    ligne_go = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
    trouvees, revocations = [], []
    for ligne in registre.read_text(encoding="utf-8").splitlines():
        m = ligne_go.match(ligne)
        if not m:
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if m.group(1) == go_id:
            trouvees.append(cellules)
        elif _est_revocation(cellules, go_id):
            revocations.append(m.group(1))
    principales = [c for c in trouvees if not (len(c) == 8 and c[3].lower().startswith("extension"))]
    if len(principales) != 1:
        raise Refus(f"{go_id} : {len(principales)} ligne(s) principale(s) dans {registre.name} (une exigée)")
    c = principales[0]
    if len(c) != 8:
        raise Refus(f"{go_id} : ligne mal formée ({len(c)} colonnes, 8 attendues)")
    ident, accorde, typ, perimetre, plafond, echeance, par, _ref = c
    if typ != "calcul":
        raise Refus(f"{go_id} : type {typ!r}, « calcul » exigé")
    if par != "Lazar":
        raise Refus(f"{go_id} : accordé par {par!r}, Lazar exigé")
    try:
        d_acc, d_ech = _dt.date.fromisoformat(accorde), _dt.date.fromisoformat(echeance)
    except ValueError:
        raise Refus(f"{go_id} : dates illisibles ({accorde!r}, {echeance!r})") from None
    if not d_acc <= aujourd_hui <= d_ech:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} → {d_ech}, aujourd'hui {aujourd_hui})")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    p = _normaliser(perimetre)
    if "mentors" not in p and "affinage" not in p:
        raise Refus(f"{go_id} : périmètre sans « mentors » ni « affinage » — ce n'est pas le GO de cette course")
    m_plafond = re.match(r"^\s*(\d+(?:[.,]\d+)?)\s*(?:USD|usd)\s*$", plafond)
    if not m_plafond:
        raise Refus(f"{go_id} : plafond illisible {plafond!r} (un nombre + USD attendu)")
    plafond_lu = float(m_plafond.group(1).replace(",", "."))
    if plafond_lu != PLAFOND_ARRET_USD:
        raise Refus(f"{go_id} : plafond lu {plafond_lu} USD != plafond d'arrêt {PLAFOND_ARRET_USD} USD")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "plafond": plafond, "plafond_lu": plafond_lu, "par": par,
            "ligne_sha256": hashlib.sha256(("|".join(c)).encode("utf-8")).hexdigest()}


def verifier_course_jamais_lancee(r: Reglages) -> None:
    """Une course est « lancée » dès que son manifeste de départ existe ; un essai refusé avant lui ne bloque rien."""
    if r.dossier_runs.is_dir():
        deja = sorted(p.name for p in r.dossier_runs.iterdir()
                      if p.name.endswith(SUFFIXES_DEJA_LANCEE) and (p / "manifeste-lanceur-depart.json").exists())
        if deja:
            raise Refus(f"course déjà lancée sous ce lanceur ({deja}) : une relance est une nouvelle version et un mot de la mère")


# --- (3) préenregistrement, contre-lecture, liste des retraits ----------------------------------------------------------------


def verifier_preenregistrement(r: Reglages) -> dict:
    chemin, attendu = r.prereg
    if not re.fullmatch(r"[0-9a-f]{64}", attendu or ""):
        raise Refus("empreinte du préenregistrement non posée dans le lanceur : aucun lancement")
    if not chemin.is_file():
        raise Refus(f"préenregistrement absent : {chemin}")
    lu = sha256_fichier(chemin)
    if lu != attendu:
        raise Refus(f"préenregistrement d'empreinte {lu}, {attendu} épinglée")
    if not scelle(chemin):
        raise Refus("préenregistrement non scellé (compagnon .sha256 absent ou faux)")
    return {"chemin": str(chemin.relative_to(r.depot)) if chemin.is_relative_to(r.depot) else str(chemin), "sha256": lu}


def lire_verdict(texte: str) -> str | None:
    lignes = texte.splitlines()
    for i, l in enumerate(lignes):
        if re.match(r"^#{1,3}\s*Verdict\b", l.strip()):
            for suite in lignes[i + 1:]:
                if suite.strip():
                    return suite.strip()
    return None


VERDICTS_EXACTS = ("Scellable.", "**Scellable.**")
AVEUX_NON_RELU = re.compile(r"(n'ai pas (re)?lu|pas (ete )?relu|non relu|sans (la )?relire|sans relecture|n'a pas (ete )?(re)?lu|"
                            r"lecture partielle du (preenregistrement|lanceur)|pas pu (re)?lire)")


def verdict_favorable(verdict: str | None) -> bool:
    """v2 (garde stricte) : la première ligne du verdict est exactement « Scellable. » (en gras ou non), rien d'autre."""
    return isinstance(verdict, str) and verdict.strip() in VERDICTS_EXACTS


def verifier_contre_lecture(r: Reglages, prereg_sha: str, lanceur_sha: str) -> dict:
    c = r.contre_lecture
    if not c.is_file():
        raise Refus(f"contre-lecture absente : {c} (R2 : aucun lancement sans contre-lecture scellée)")
    if not scelle(c):
        raise Refus("contre-lecture non scellée (compagnon .sha256 absent ou faux)")
    texte = c.read_text(encoding="utf-8")
    if prereg_sha not in texte:
        raise Refus("la contre-lecture ne cite pas l'empreinte du préenregistrement épinglé")
    if lanceur_sha not in texte:
        raise Refus("la contre-lecture ne cite pas l'empreinte de ce lanceur (elle n'a pas lu cette version)")
    v = lire_verdict(texte)
    if not verdict_favorable(v):
        raise Refus(f"verdict de la contre-lecture défavorable, illisible ou inexact : {v!r} (première ligne exacte « Scellable. » exigée)")
    if "modele k" not in _normaliser(texte):
        raise Refus("la contre-lecture ne dit pas être du modèle K (contre-lecteur attendu)")
    aveu = AVEUX_NON_RELU.search(_normaliser(texte).replace("’", "'"))
    if aveu:
        raise Refus(f"la contre-lecture dit n'avoir pas relu ({aveu.group(0)!r}) : refusée")
    return {"chemin": str(c), "sha256": sha256_fichier(c), "verdict": v}


def verifier_pieces(r: Reglages) -> dict:
    if r.moteur == "reel" and r.depot.resolve() != r.depot_attendu_par_l_enveloppe.resolve():
        raise Refus(f"dépôt de travail en {r.depot}, l'enveloppe d'Argon v5 attend {r.depot_attendu_par_l_enveloppe}")
    lues, ecarts = {}, {}
    for nom, (rel, attendu) in sorted(r.pieces.items()):
        p = r.depot / rel
        lu = sha256_fichier(p) if p.is_file() else None
        if lu != attendu:
            ecarts[nom] = {"chemin": rel, "attendu": attendu, "lu": lu}
        lues[nom] = {"chemin": rel, "absolu": str(p), "sha256": lu}
    if ecarts:
        raise Refus("pièces absentes ou d'empreinte différente (R11) : " + json.dumps(ecarts, ensure_ascii=False))
    return lues


def verifier_liste(liste: dict) -> dict:
    """Garde (3), dernier point : aucune entrée servie dans la liste des retraits ; aucun jeton réservé servi."""
    retirees = {x["numero"] for x in liste["retraits"]["idees_de_la_table"]}
    jetons = sorted({f for x in liste["retraits"]["reserves_de_cloisonnement"] for f in x["fiches"]})
    servies = [s["numero"] for f in liste["fils"] for s in f["idees_servies"]]
    croisement = sorted(set(servies) & retirees)
    if croisement:
        raise Refus(f"entrée servie figurant dans la liste des retraits : {croisement}")
    textes = "\n".join(s["texte_servi"] for f in liste["fils"] for s in f["idees_servies"])
    for j in jetons:
        if j in textes:
            raise Refus(f"jeton d'une entrée réservée dans un texte servi : {j}")
    if len(liste["fils"]) != 16:
        raise Refus(f"liste des fils : {len(liste['fils'])} fils, 16 attendus")
    return {"fils": len(liste["fils"]), "idees_servies_distinctes": len(set(servies)), "idees_retirees": sorted(retirees),
            "jetons_reserves": jetons}


def texte_de_case(fil: dict) -> str:
    lignes = [f"Fil commun n° {fil['rang']} : {fil['titre']}",
              "Idées regroupées sous ce fil (avis de proposeurs d'une course passée, jamais des faits ni des preuves) :"]
    lignes += [f"- [{s['numero']}] {s['texte_servi']}" for s in fil["idees_servies"]]
    return "\n".join(lignes)


# --- (4) déclaration des relais -----------------------------------------------------------------------------------------------


def lire_json_scelle(chemin: Path, quoi: str) -> tuple:
    if not chemin.is_file():
        raise Refus(f"{quoi} absent : {chemin}")
    if not scelle(chemin):
        raise Refus(f"{quoi} non scellé (compagnon .sha256 absent ou faux) : {chemin}")
    brut = chemin.read_text(encoding="utf-8")
    if MOTIF_VALEUR_DE_CLE.search(brut):
        raise Refus(f"{quoi} : une chaîne de la forme d'une valeur de clé y figure — refus, rien n'est lu ni recopié")
    try:
        return json.loads(brut), sha256_fichier(chemin)
    except ValueError:
        raise Refus(f"{quoi} : JSON illisible") from None


def verifier_declaration(decl: dict, fixe: dict, r: Reglages) -> dict:
    """Rend {fournisseurs (blocs de l'orchestrateur), especes_actives, cles {fournisseur: nom}, absentes, carbon}."""
    f_decl = decl.get("fournisseurs")
    if not isinstance(f_decl, dict):
        raise Refus("déclaration des relais : « fournisseurs » (objet) exigé")
    inconnus = sorted(set(f_decl) - set(TYPES_PERMIS))
    if inconnus:
        raise Refus(f"déclaration des relais : fournisseurs inconnus {inconnus}")
    for requis in ("claude", "argon"):
        if requis not in f_decl:
            raise Refus(f"déclaration des relais : « {requis} » exigé (proposeurs Claude d'abord ; juge et lecteur Argon)")
    blocs, cles, modeles, carbon = {}, {}, {}, {"inscrite": INSCRIPTION_CARBON, "active": False, "motif": None}
    for nom, b in sorted(f_decl.items()):
        if not isinstance(b, dict):
            raise Refus(f"fournisseurs.{nom} : objet attendu")
        t = TYPES_PERMIS[nom]
        if b.get("type") != t:
            raise Refus(f"fournisseurs.{nom}.type : {t!r} exigé (reçu {b.get('type')!r})")
        en_trop = sorted(set(b) - CLES_PERMISES[t] - CLES_META)
        if en_trop:
            raise Refus(f"fournisseurs.{nom} : clés non permises {en_trop}")
        nom_cle = b.get("nom_cle")
        if not isinstance(nom_cle, str) or not NOM_DE_VARIABLE.match(nom_cle):
            raise Refus(f"fournisseurs.{nom}.nom_cle : nom de variable exigé (le nom seul, jamais la valeur)")
        if nom_cle in CLES_INTERDITES:
            raise Refus(f"fournisseurs.{nom}.nom_cle = {nom_cle} : clé exclue de cette course (R-3228, elle garde son reste)")
        if nom == "claude" and nom_cle != CLE_CLAUDE:
            raise Refus(f"fournisseurs.claude.nom_cle = {nom_cle} : tous les appels Claude passent par {CLE_CLAUDE} (R-3228)")
        if nom != "claude" and nom_cle.startswith(PREFIXE_CLES_CLAUDE):
            raise Refus(f"fournisseurs.{nom}.nom_cle = {nom_cle} : une clé de la famille Claude sur un autre relais est refusée")
        pp = b.get("porte_plafond")
        if not isinstance(pp, dict) or pp.get("type") not in ("commande", "environnement"):
            raise Refus(f"fournisseurs.{nom}.porte_plafond : {{type: commande|environnement}} exigé (A15, brouillon 10)")
        if t == "commande_externe" and pp["type"] != "environnement":
            raise Refus(f"fournisseurs.{nom}.porte_plafond : « environnement » exigé pour une commande externe")
        if t != "commande_externe":
            if pp["type"] != "commande" or not isinstance(pp.get("commande"), list) or not pp["commande"] \
                    or not all(isinstance(x, str) and x for x in pp["commande"]):
                raise Refus(f"fournisseurs.{nom}.porte_plafond : commande (liste non vide) exigée pour un relais persistant")
            if not isinstance(pp.get("delai_s"), (int, float)) or isinstance(pp.get("delai_s"), bool) or pp["delai_s"] <= 0:
                raise Refus(f"fournisseurs.{nom}.porte_plafond.delai_s : nombre > 0 exigé")
            if not isinstance(b.get("url_relais"), str) or not URL_LOCALE.match(b["url_relais"]):
                raise Refus(f"fournisseurs.{nom}.url_relais : adresse de boucle locale exigée (http://127.0.0.1:PORT)")
        if nom == "argon":
            attendue = ["bash", str(r.depot / PIECES["enveloppe_argon"][0])]
            if b.get("commande") != attendue:
                raise Refus(f"fournisseurs.argon.commande : {attendue} exigée (enveloppe épinglée)")
        if nom in ("astra", "carbon"):
            m = b.get("modele_propose")
            motif = next(e.get("motif_modele") for e in fixe["especes"] if e["fournisseur"] == nom)
            if not isinstance(m, str) or motif not in m.lower() or "claude" in m.lower() or not re.fullmatch(r"[a-z0-9.\-]+", m):
                raise Refus(f"fournisseurs.{nom}.modele_propose : identifiant de modèle qui contient « {motif} » exigé")
            if not isinstance(b.get("commande"), list) or not b["commande"]:
                raise Refus(f"fournisseurs.{nom}.commande : liste non vide exigée")
            modeles[nom] = m
        if nom == "kimi" and b.get("modele") != "kimi-k3.1-pro":
            raise Refus("fournisseurs.kimi.modele : « kimi-k3.1-pro » exigé (configuration fixe)")
        if nom == "carbon":
            if b.get("inscription") != INSCRIPTION_CARBON:
                carbon["motif"] = f"inscription {b.get('inscription')!r} : {INSCRIPTION_CARBON} exigée ; Carbon non active"
                continue
            carbon.update(active=True, motif="inscrite (R-3217), relais et clé nommés dans la déclaration")
        elif "inscription" in b:
            raise Refus(f"fournisseurs.{nom}.inscription : clé réservée à Carbon")
        blocs[nom] = {k: v for k, v in b.items() if k not in CLES_META}
        cles[nom] = nom_cle
    if "carbon" not in f_decl:
        carbon["motif"] = "relais et clé non nommés dans la déclaration : course sans Carbon"
    actives, absentes = [], []
    for e in sorted(fixe["especes"], key=lambda x: x["ordre"]):
        if e["fournisseur"] in blocs:
            actives.append(dict(e, modele=e["modele"] or modeles[e["fournisseur"]]))
        else:
            absentes.append({"etiquette": e["etiquette"], "motif": "relais non déclaré" if e["fournisseur"] != "carbon" else carbon["motif"]})
    return {"fournisseurs": blocs, "especes_actives": actives, "especes_absentes": absentes, "cles": cles, "carbon": carbon}


# --- (2) relevé du crédit de chaque clé ---------------------------------------------------------------------------------------


def _reel_positif(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and v >= 0


def borne_appel_kimi(bloc: dict, octets_entree_max: int, plafond_session: float) -> float:
    """Pire coût d'un appel de Kimi (formule de l'adaptateur `adaptateur_kimi_v53`) : (octets du corps + 1024) × prix d'entrée
    + max_tokens × prix de sortie, borné par le plafond de session ; prix en USD par million de jetons."""
    for k in ("prix_entree", "prix_sortie", "max_sortie_jetons"):
        if not _reel_positif(bloc.get(k)):
            raise Refus(f"fournisseurs.kimi.{k} : nombre ≥ 0 exigé pour la part au pire")
    brut = ((octets_entree_max + 1024) * bloc["prix_entree"] + bloc["max_sortie_jetons"] * bloc["prix_sortie"]) / 1e6
    return round(min(brut, plafond_session), 6)


def parts_au_pire(fixe: dict, liste: dict, pieces: dict, decl: dict) -> dict:
    """Part au pire de chaque relais (donc de chaque clé) dans cette course, en USD (R-3237, point 1) :
    - relais qui tient l'aiguilleur ou un juge (Claude, Argon) : le nombre de cartes n'est borné par aucun programme, la seule
      borne dure est le plafond d'arrêt : 150 USD ;
    - relais de proposeur seulement : 16 appels × pire coût d'un appel (plafond de session ; pour Kimi, la formule de son
      adaptateur sur l'entrée la plus longue de la course, si elle est plus basse)."""
    actives = decl["especes_actives"]
    ps = fixe["plafonds_session"]
    internes = {fixe["aiguilleur"]["fournisseur"]} | {j["fournisseur"] for j in fixe["juges"]}
    consigne = Path(pieces["consigne_proposeur"]["absolu"]).read_bytes()
    entree_max = len(consigne) + max(len(texte_de_case(f).encode("utf-8")) for f in liste["fils"]) + 200
    parts = {}
    for f in sorted({e["fournisseur"] for e in actives} | internes):
        if f in internes:
            parts[f] = {"part_au_pire_usd": PLAFOND_ARRET_USD, "regle": "aiguilleur ou juge : cartes non bornées, plafond d'arrêt"}
            continue
        n = len(liste["fils"]) * sum(1 for e in actives if e["fournisseur"] == f)
        par_appel = float(ps["proposeur"])
        regle = f"{n} appels × plafond de session {par_appel}"
        if f == "kimi":
            par_appel = borne_appel_kimi(decl["fournisseurs"]["kimi"], entree_max, float(ps["proposeur"]))
            regle = f"{n} appels × pire coût d'un appel de Kimi (formule de son adaptateur, entrée ≤ {entree_max} octets)"
        parts[f] = {"part_au_pire_usd": round(min(n * par_appel, PLAFOND_ARRET_USD), 6), "par_appel_usd": par_appel, "regle": regle}
    return parts


def verifier_credits(releve: dict, cles: dict, aujourd_hui: _dt.date, dossier_alerte: Path, parts: dict | None = None) -> dict:
    """v3 (R-3237). Rend {nom_cle: {...}}.
    - Relevé du jour exigé ; chaque clé employée y figure (« non lisible » s'écrit).
    - Non lisible : Minuit compté au prix relevé (v2) ; Argon, Astra, Carbon seulement sous la dispense écrite de la mère
      citant R-3237 (départ permis, arrêt au premier refus pour crédit) ; toute autre clé : refus.
    - Lisible : alerte et arrêt avant le départ (code 3) si reste < sa part au pire, ou reste < un cinquième du crédit ;
      Kimi : part au pire + 11,3 USD > 90 % du reste → refus (les deux courses se suivent)."""
    parts = parts or {}
    quand = str(releve.get("releve_utc") or "")
    if not quand.startswith(aujourd_hui.isoformat()):
        raise Refus(f"relevé des crédits du {quand!r} : un relevé du jour ({aujourd_hui}) est exigé")
    lignes = releve.get("cles")
    if not isinstance(lignes, dict):
        raise Refus("relevé des crédits : « cles » (objet) exigé")
    dispense = releve.get("dispense") or {}
    dispensees = set(dispense.get("cles") or []) if dispense.get("par") == "mère" and dispense.get("reference") == REFERENCE_DISPENSE else set()
    sortie, alertes = {}, []
    for fournisseur, nom in sorted(cles.items()):
        x = lignes.get(nom)
        part = (parts.get(fournisseur) or {}).get("part_au_pire_usd")
        if nom == CLE_CLAUDE and isinstance(x, dict) and x.get("non_lisible") is True:
            anterieure = x.get("depense_anterieure_usd")
            if not _reel_positif(anterieure):
                raise Refus(f"crédit de {nom} non lisible : depense_anterieure_usd (≥ 0) exigée pour le compter au prix relevé")
            x = {"credit_usd": CREDIT_DECLARE_CLE_CLAUDE_USD, "reste_usd": max(0.0, CREDIT_DECLARE_CLE_CLAUDE_USD - anterieure),
                 "source": "compté au prix relevé : crédit déclaré 200 USD (R-3228) moins la dépense antérieure déclarée"}
        if not isinstance(x, dict):
            raise Refus(f"relevé des crédits : clé {nom} ({fournisseur}) absente — « non lisible » s'écrit, il ne s'omet pas")
        if x.get("non_lisible") is True:
            if fournisseur not in FOURNISSEURS_DISPENSABLES:
                raise Refus(f"crédit de la clé {nom} ({fournisseur}) non lisible : seules les clés d'Argon, d'Astra et de Carbon "
                            "peuvent partir sous dispense (R-3237)")
            if nom not in dispensees:
                raise Refus(f"crédit de la clé {nom} ({fournisseur}) non lisible et sans dispense écrite de la mère citant "
                            f"{REFERENCE_DISPENSE} : aucun départ")
            sortie[nom] = {"fournisseur": fournisseur, "lisible": False, "motif": x.get("motif"), "dispense": dispense,
                           "part_au_pire_usd": part, "regle": "arrêt de la course au premier refus pour crédit (R-3237)"}
            continue
        credit, reste = x.get("credit_usd"), x.get("reste_usd")
        if not (_reel_positif(credit) and _reel_positif(reste)) or reste > credit:
            raise Refus(f"relevé des crédits : clé {nom} : credit_usd et reste_usd (nombres ≥ 0, reste ≤ crédit) exigés")
        if part is None:
            raise Refus(f"part au pire du relais {fournisseur} inconnue : aucun départ")
        d = {"fournisseur": fournisseur, "lisible": True, "credit_usd": credit, "reste_usd": reste, "source": x.get("source"),
             "part_au_pire_usd": part, "cinquieme_usd": credit / 5.0}
        motifs = []
        if reste < part:
            motifs.append(f"reste {reste} < part au pire {part}")
        if reste < credit / 5.0:
            motifs.append(f"reste {reste} < un cinquième du crédit {credit / 5.0}")
        if fournisseur == "kimi" and part + KIMI_COURSE_SUIVANTE_PIRE_USD > KIMI_PART_DU_RESTE * reste:
            motifs.append(f"part au pire {part} + {KIMI_COURSE_SUIVANTE_PIRE_USD} (course Kimi de la relance) > 90 % du reste "
                          f"({round(KIMI_PART_DU_RESTE * reste, 6)}) : les deux courses doivent se suivre, solde relu avant chacune")
        d["motifs_d_arret"] = motifs
        sortie[nom] = d
        if motifs:
            alertes.append({"cle": nom, "fournisseur": fournisseur, "reste_usd": reste, "credit_usd": credit, "part_au_pire_usd": part,
                            "motifs": motifs})
    if alertes:
        texte = {"alerte": "crédit insuffisant pour la part au pire d'une clé, avant la course d'affinage des idées des mentors : "
                           "départ refusé",
                 "regle": "R-3237 : chaque clé confrontée à sa part au pire ; un cinquième du crédit ; Kimi : part + 11,3 USD ≤ 90 % "
                          "du reste, sinon les deux courses se suivent et le solde est relu avant chacune ; Lazar à prévenir "
                          "avant qu'une clé n'atteigne zéro",
                 "cles": alertes, "pour": "la mère (à transmettre à Lazar)"}
        dossier_alerte.mkdir(parents=True, exist_ok=True)
        chemin = dossier_alerte / "alerte-credits-avant.json"
        if not chemin.exists():
            ecrire_scelle(chemin, texte)
        raise AlerteCredit(json.dumps(dict(texte, fichier=str(chemin)), ensure_ascii=False))
    return sortie


# --- (R-3237, 3) procédure neutre des relais persistants ; (R-3237, 2) garde de crédit des relais dispensés ----------------


def verifier_procedure_relais(r: "Reglages", decl: dict) -> dict:
    """Moteur réel : la pièce qui nomme la procédure versée par la mère doit être remplie, scellée, la procédure présente à son
    empreinte, et chaque porte de plafond « commande » (relais persistants) doit la lancer."""
    p = r.procedure_relais
    if not p.is_file():
        raise Refus(f"procédure des relais persistants : pièce absente ({p}) — moteur réel refusé tant qu'elle n'est pas remplie")
    brut = p.read_text(encoding="utf-8")
    if MARQUEUR_A_REMPLIR in brut:
        raise Refus("procédure des relais persistants : chemin ou empreinte encore « À REMPLIR » — moteur réel refusé")
    if not scelle(p):
        raise Refus("procédure des relais persistants : pièce non scellée")
    o = json.loads(brut)
    chemin, attendu = o.get("chemin"), o.get("sha256")
    if not isinstance(chemin, str) or not os.path.isabs(chemin) or not re.fullmatch(r"[0-9a-f]{64}", str(attendu)):
        raise Refus("procédure des relais persistants : {chemin absolu, sha256} exigés")
    if not Path(chemin).is_file() or sha256_fichier(Path(chemin)) != attendu:
        raise Refus(f"procédure des relais persistants absente ou d'une autre empreinte : {chemin}")
    for nom, b in sorted(decl["fournisseurs"].items()):
        pp = b.get("porte_plafond") or {}
        if pp.get("type") == "commande" and chemin not in pp.get("commande", []):
            raise Refus(f"fournisseurs.{nom}.porte_plafond : la commande doit lancer la procédure épinglée ({chemin})")
    return {"piece": str(p), "piece_sha256": sha256_fichier(p), "procedure": chemin, "sha256": attendu}


def envelopper_commandes(decl: dict, python: str, garde: Path, dossier_arrets: Path) -> dict:
    """Met la garde de crédit devant la commande de chaque relais dispensable actif (Argon, Astra, Carbon)."""
    for nom in FOURNISSEURS_DISPENSABLES:
        b = decl["fournisseurs"].get(nom)
        if b is not None:
            b["commande"] = [python, "-I", "-B", str(garde), str(dossier_arrets), nom, "--"] + list(b["commande"])
    return decl


# --- (6) orchestrateur --------------------------------------------------------------------------------------------------------


def _git(dossier: Path, *args: str) -> str:
    p = subprocess.run(["git", "-C", str(dossier), *args], capture_output=True, text=True, timeout=60)
    if p.returncode != 0:
        raise Refus(f"git {' '.join(args)} dans {dossier} : code {p.returncode} ({p.stderr.strip()[:200]})")
    return p.stdout


def verifier_orchestrateur(r: Reglages) -> dict:
    presents = [o for o in r.orchestrateurs if (o / LANCEUR_ORCHESTRATEUR).is_file()]
    if len(presents) != 1:
        raise Refus(f"orchestrateur : {len(presents)} copie(s) trouvée(s) parmi {[str(o) for o in r.orchestrateurs]} (une exigée)")
    o = presents[0]
    tete = _git(o, "rev-parse", "HEAD").strip()
    if tete != r.commit_orchestrateur:
        raise Refus(f"orchestrateur au commit {tete}, {r.commit_orchestrateur} exigé")
    porcelaine = _git(o, "status", "--porcelain", "--untracked-files=all", "--ignored=matching").strip()
    if porcelaine:
        raise Refus(f"orchestrateur modifié, fichiers non suivis ou ignorés : {porcelaine[:200]!r}")
    ecarts = {rel: (sha256_fichier(o / rel) if (o / rel).is_file() else None) for rel in r.empreintes_orchestrateur}
    ecarts = {k: v for k, v in ecarts.items() if v != r.empreintes_orchestrateur[k]}
    if ecarts:
        raise Refus(f"orchestrateur : empreintes différentes ou fichiers absents : {ecarts}")
    return {"chemin": str(o), "commit": tete, "empreintes": dict(r.empreintes_orchestrateur)}


# --- (1) configuration de l'orchestrateur, acte de gel ------------------------------------------------------------------------


def assembler_configuration(fixe: dict, liste: dict, pieces: dict, decl: dict, specification: dict | None) -> dict:
    garde_configuration_fixe(fixe)
    garde_cles_configuration(fixe)
    actives = decl["especes_actives"]
    if not any(e["famille"] == "claude" for e in actives):
        raise Refus("aucune espèce Claude active : Claude d'abord (R-3209, point 2)")
    interdites = list(fixe["etiquettes_interdites_fixes"]) + [x["numero"] for x in liste["retraits"]["idees_de_la_table"]] \
        + sorted({f for x in liste["retraits"]["reserves_de_cloisonnement"] for f in x["fiches"]})
    conf = {k: v for k, v in fixe.items() if k not in ("version", "statut", "orchestrateur", "generations", "cartes_par_appel",
                                                       "especes", "etiquettes_interdites_fixes", "cles",
                                                       "cles_interdites", "credit_declare_usd", "regle_cles_v3")}
    conf["proposeurs"] = [{"etiquette": e["etiquette"], "modele": e["modele"], "fournisseur": e["fournisseur"],
                           "consigne": "consigne_proposeur"} for e in actives]
    conf["cases"] = [[texte_de_case(f), "affinage"] for f in liste["fils"]]
    conf["pieces"] = {n: {"chemin": pieces[n]["absolu"], "sha256": pieces[n]["sha256"]} for n in PIECES_SERVIES}
    conf["etiquettes_interdites"] = interdites
    conf["fournisseurs"] = decl["fournisseurs"]
    if specification is not None:
        conf["specification"] = specification
    for e in actives:
        if e["fournisseur"] not in conf["fournisseurs"]:
            raise Refus(f"espèce {e['etiquette']} active sans relais")
    utilises = {conf["aiguilleur"]["fournisseur"]} | {j["fournisseur"] for j in conf["juges"]} | \
        {x["fournisseur"] for x in conf["lecteurs_etiquettes"]}
    manquants = sorted(utilises - set(conf["fournisseurs"]))
    if manquants:
        raise Refus(f"relais absents pour l'aiguilleur, un juge ou un lecteur : {manquants}")
    return conf


def garde_cles_configuration(fixe: dict) -> None:
    """v2 : la configuration fixe nomme Minuit pour Claude, exclut Rigaud, et chaque espèce Claude porte Minuit."""
    if (fixe.get("cles") or {}).get("claude") != CLE_CLAUDE:
        raise Refus(f"configuration : cles.claude doit être {CLE_CLAUDE}")
    if any(c not in (fixe.get("cles_interdites") or []) for c in CLES_INTERDITES):
        raise Refus("configuration : la clé Rigaud doit figurer dans cles_interdites")
    for e in fixe.get("especes") or []:
        if e.get("famille") == "claude" and e.get("cle") != CLE_CLAUDE:
            raise Refus(f"configuration : espèce {e.get('etiquette')} sur une autre clé que {CLE_CLAUDE}")


def garde_configuration_fixe(fixe: dict) -> None:
    """Garde (1) sur la partie fixe : S17 = plafond d'arrêt, portée « course », une génération, étapes retirées par
    construction, plafonds de relais des étapes protégées ≤ S17, aucune étape de tests de mort."""
    b = fixe.get("budget") or {}
    if b.get("plafond_usd") != PLAFOND_ARRET_USD:
        raise Refus(f"configuration : budget.plafond_usd {b.get('plafond_usd')!r} != plafond d'arrêt {PLAFOND_ARRET_USD}")
    if b.get("portee_plafond") != "course" or fixe.get("generations") != 1:
        raise Refus("configuration : portée « course » et une seule génération exigées")
    etapes = {e["nom"]: e for e in b.get("etapes") or []}
    for nom in ("passe_tableau", "fusions"):
        e = etapes.get(nom) or {}
        if e.get("role") != "sacrifiable" or not e.get("plafond_relais_usd", 0) > PLAFOND_ARRET_USD or e.get("attendu_usd") != 0:
            raise Refus(f"configuration : l'étape {nom} doit être retirée par construction (sacrifiable, plafond de relais > S17, attendu 0)")
    protegees = sum(e["plafond_relais_usd"] for e in etapes.values() if e.get("role") == "protegee")
    if protegees > PLAFOND_ARRET_USD:
        raise Refus(f"configuration : somme des plafonds de relais des étapes protégées {protegees} > {PLAFOND_ARRET_USD}")
    if "etage_tests_de_mort" in fixe:
        raise Refus("configuration : pas de tests de mort dans cette course")
    if fixe.get("bisociateur", {}).get("bras") != [] or fixe.get("bisociateur", {}).get("k_paires") != 0:
        raise Refus("configuration : aucun bras du bisociateur, aucune fusion")


def acte_de_gel(prereg: dict, cl: dict, lanceur_sha: str, horodatage: str) -> str:
    return ("# Acte de gel — course d'affinage des idées des mentors, version 1\n\n"
            f"Écrit par le lanceur `{VERSION}` (sha256 {lanceur_sha}) le {horodatage}, après vérification.\n\n"
            f"- Préenregistrement : `{prereg['chemin']}`, sha256 {prereg['sha256']}, scellé.\n"
            f"- Contre-lecture : `{cl['chemin']}`, sha256 {cl['sha256']}, scellée ; verdict lu : {cl['verdict']}\n"
            "- Cet acte est la spécification servie à l'orchestrateur (`specification.preenregistrement`) ; il ne change rien au "
            "préenregistrement.\n")


# --- (8) environnement, bac à sable -------------------------------------------------------------------------------------------


def environnement_filtre(env: dict, dossier_maison: Path) -> tuple:
    retires = sorted(n for n in env if n in NOMS_DE_CLE or MOTIF_NOM_DE_CLE.search(n))
    hors_liste = sorted(n for n in env if n not in NOMS_PERMIS and n not in retires)
    garde = {n: env[n] for n in env if n in NOMS_PERMIS}
    garde["GO_ID"] = GO_ID
    garde["HOME"] = str(dossier_maison)
    garde["PYTHONPYCACHEPREFIX"] = str(dossier_maison / "pycache")
    return garde, retires, hors_liste


def sonder_bac_a_sable(r: Reglages, orchestrateur: Path, env: dict) -> dict:
    try:
        p = subprocess.run([r.python, "-I", "-B", "-c", SONDE_BAC_A_SABLE, str(orchestrateur)], cwd=str(orchestrateur), env=env,
                           capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"sonde du bac à sable non exécutée ({type(e).__name__})") from None
    lignes = [x for x in p.stdout.splitlines() if x.strip()]
    try:
        etat = json.loads(lignes[-1]) if p.returncode == 0 and lignes else None
    except json.JSONDecodeError:
        etat = None
    if not (isinstance(etat, dict) and isinstance(etat.get("actif"), bool)):
        raise Refus(f"sonde du bac à sable illisible (code {p.returncode})")
    if r.exiger_bac_a_sable and not (etat["actif"] and etat.get("proc_neuf")):
        raise Refus("bac à sable inactif ou sans /proc neuf : " + str(etat.get("motif")))
    return etat


# --- (5) coût réel, écart, relevé après ---------------------------------------------------------------------------------------


def couts_reels(sortie: Path) -> dict:
    chemin = sortie / "generation-1" / "consommations.json"
    if not chemin.is_file():
        return {"lisible": False, "motif": f"{chemin} absent"}
    donnees = json.loads(chemin.read_text(encoding="utf-8")).get("consommations") or []
    par_relais, par_role, appels, coupures, inconnus = {}, {}, {}, [], {}
    for x in donnees:
        role = x.get("role")
        if role == "plafond-relais":
            continue
        if role == "coupure" or x.get("coupure"):
            coupures.append(str(x.get("etape")))
            continue
        f, role, c = str(x.get("fournisseur") or "(sans relais)"), str(role or "(sans rôle)"), float(x.get("cout_usd") or 0.0)
        par_relais[f] = round(par_relais.get(f, 0.0) + c, 6)
        par_role[role] = round(par_role.get(role, 0.0) + c, 6)
        appels[role] = appels.get(role, 0) + 1
        if x.get("cout_inconnu"):
            inconnus[f] = inconnus.get(f, 0) + 1
    return {"lisible": True, "fichier_sha256": sha256_fichier(chemin), "par_relais_usd": par_relais, "par_role_usd": par_role,
            "appels_par_role": appels, "total_usd": round(sum(par_relais.values()), 6), "coupures": coupures,
            "appels_a_cout_inconnu_par_relais": inconnus}


def ecart_au_devis(couts: dict, avec_carbon: bool) -> dict:
    if not couts.get("lisible"):
        return {"lisible": False}
    lignes = {}
    for role, n in sorted(couts["appels_par_role"].items()):
        attendu = DEVIS_V5_PAR_APPEL.get(role)
        reel = couts["par_role_usd"][role]
        lignes[role] = {"appels": n, "reel_usd": reel, "devis_usd": round(n * attendu, 6) if attendu is not None else None,
                        "ecart_usd": round(reel - n * attendu, 6) if attendu is not None else None}
    total_devis = DEVIS_V5_TOTAL["avec_carbon" if avec_carbon else "sans_carbon"]
    return {"lisible": True, "par_role": lignes, "total_reel_usd": couts["total_usd"], "devis_estimation_sans_marge_usd": total_devis,
            "ecart_total_usd": round(couts["total_usd"] - total_devis, 6)}


def releve_apres(credits: dict, couts: dict, cles: dict) -> tuple:
    """Reste estimé = reste avant − coût compté des relais de la clé (consommations de l'orchestrateur, au prix des fichiers ;
    à confirmer par l'interface de facturation). Alerte sous un cinquième du crédit, et pour Kimi sous ce qu'exige la course
    Kimi de la relance (11,3 / 0,9 USD). Rend (relevé, alertes)."""
    apres, alertes = {}, []
    for nom, avant in sorted(credits.items()):
        fournisseurs = [f for f, n in cles.items() if n == nom]
        depense = round(sum((couts.get("par_relais_usd") or {}).get(f, 0.0) for f in fournisseurs), 6) if couts.get("lisible") else None
        if not avant.get("lisible") or depense is None:
            apres[nom] = {"lisible": False, "depense_comptee_usd": depense, "a_relever": "par l'interface de facturation si elle le permet"}
            continue
        reste = round(avant["reste_usd"] - depense, 6)
        seuil = avant["credit_usd"] / 5.0
        if "kimi" in fournisseurs:
            seuil = max(seuil, KIMI_COURSE_SUIVANTE_PIRE_USD / KIMI_PART_DU_RESTE)
        apres[nom] = {"lisible": "estimé", "reste_estime_usd": reste, "depense_comptee_usd": depense, "seuil_usd": seuil,
                      "a_relever": "par l'interface de facturation (confirmation)"}
        if reste < seuil:
            alertes.append({"cle": nom, "reste_estime_usd": reste, "seuil_usd": seuil})
    return apres, alertes


def lire_resume_course(sortie: Path) -> dict:
    """Ce qui a été fait, sans lire aucun verdict : étapes, nœud, arrêt, cumul, nombre de cartes."""
    out = {}
    m = sortie / "generation-1" / "manifeste-fin.json"
    if m.is_file():
        d = json.loads(m.read_text(encoding="utf-8"))
        out.update(etapes=d.get("etapes"), noeud=d.get("noeud"), arret=d.get("arret"), roles_arretes=d.get("roles_arretes"),
                   exclues_a4=d.get("exclues_a4"), cumul_usd=(d.get("budget") or {}).get("cumul_usd"),
                   depassement_s17_usd=(d.get("budget") or {}).get("depassement_s17_usd"))
    f = sortie / "generation-1" / "fiches.json"
    if f.is_file():
        out["cartes_a_passeport"] = len(json.loads(f.read_text(encoding="utf-8")))
    b = sortie / "bilan-course.json"
    if b.is_file():
        out["bilan_sha256"] = sha256_fichier(b)
    return out


# --- exécution ----------------------------------------------------------------------------------------------------------------


def _depot_git(r: Reglages) -> dict:
    try:
        return {"commit": _git(r.depot, "rev-parse", "HEAD").strip(),
                "arbre_modifie": bool(_git(r.depot, "status", "--porcelain", "--untracked-files=no").strip())}
    except Refus as e:
        return {"commit": None, "erreur": str(e)}


def _versions(r: Reglages, orch: Path, env: dict) -> dict:
    p = subprocess.run([r.python, "-I", "-B", "-c", "import numpy, platform; print(numpy.__version__, platform.python_version())"],
                       cwd=str(orch), env=env, capture_output=True, text=True, timeout=60)
    morceaux = p.stdout.split()
    return {"python": morceaux[1] if len(morceaux) == 2 else None, "numpy": morceaux[0] if len(morceaux) == 2 else None,
            "executable": r.python}


def executer(r: Reglages) -> int:
    env_lu = dict(os.environ) if r.environnement is None else dict(r.environnement)
    aujourd_hui = r.aujourd_hui or _dt.datetime.now(_dt.timezone.utc).date()
    reel = r.moteur == "reel"

    verifier_course_jamais_lancee(r)
    cle_presente = CLE_CLAUDE in env_lu  # par le nom seulement ; la valeur n'est jamais lue
    if reel and not cle_presente:
        raise Refus(f"variable {CLE_CLAUDE} absente de l'environnement du lanceur : arrêt au départ (R-3228)")
    go = verifier_go(r.registre_go, aujourd_hui) if (reel and r.verifier_go) else {"go": "sans objet (moteur simulé, aucune dépense)"}
    lanceur_sha = sha256_fichier(r.lanceur)
    prereg = verifier_preenregistrement(r)
    cl = verifier_contre_lecture(r, prereg["sha256"], lanceur_sha)
    pieces = verifier_pieces(r)
    fixe = json.loads(Path(pieces["configuration"]["absolu"]).read_text(encoding="utf-8"))
    liste = json.loads(Path(pieces["liste_fils"]["absolu"]).read_text(encoding="utf-8"))
    controle_liste = verifier_liste(liste)
    decl_brute, decl_sha = lire_json_scelle(r.declaration, "déclaration des relais")
    decl = verifier_declaration(decl_brute, fixe, r)
    releve_brut, releve_sha = lire_json_scelle(r.releve, "relevé des crédits")
    horodatage = r.horodatage()
    ident = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%d-%H%M%S") + SUFFIXE_RUN
    dossier_run = r.dossier_runs / ident
    parts = parts_au_pire(fixe, liste, pieces, decl)
    credits = verifier_credits(releve_brut, decl["cles"], aujourd_hui,
                               r.dossier_runs / (ident.replace(SUFFIXE_RUN, "") + "-alerte-credits-affinage-mentors-v3"), parts)
    procedure = verifier_procedure_relais(r, decl) if reel else {"exigee": False, "motif": "moteur simulé : aucun relais réel"}
    orch = verifier_orchestrateur(r)
    orch_dir = Path(orch["chemin"])

    dossier_sortie = r.dossier_sorties / ident
    sortie = dossier_sortie / "sortie"
    if dossier_run.exists() or dossier_sortie.exists():
        raise Refus(f"{dossier_run} ou {dossier_sortie} existe déjà (R12)")
    env, retires, hors_liste = environnement_filtre(env_lu, dossier_sortie)
    bac = sonder_bac_a_sable(r, orch_dir, env) if reel else {"exige": False, "motif": "moteur simulé : aucun agent réel"}

    dossier_run.mkdir(parents=True)
    dossier_sortie.mkdir(parents=True)
    dossier_arrets = dossier_sortie / "arrets-credit"
    dossier_arrets.mkdir()
    decl = envelopper_commandes(decl, r.python, Path(pieces["garde_credit"]["absolu"]), dossier_arrets)
    h_acte = ecrire_scelle(dossier_run / "acte-de-gel.md", acte_de_gel(prereg, cl, lanceur_sha, horodatage))
    spec = {"preenregistrement": {"chemin": str(dossier_run / "acte-de-gel.md"), "sha256": h_acte},
            "contre_lecture": {"chemin": cl["chemin"], "sha256": cl["sha256"]}}
    conf = assembler_configuration(fixe, liste, pieces, decl, spec)
    chemin_conf = dossier_run / "configuration-orchestrateur.json"
    h_conf = ecrire_scelle(chemin_conf, conf)
    base = [r.python, "-I", "-B", LANCEUR_ORCHESTRATEUR, "--course-2", str(chemin_conf), str(sortie), "--generations", "1"]
    moteur = ["--moteur", "reel", "--confirmer-moteur-reel", "--registre-go", str(r.registre_go)] if reel else ["--moteur", "simule"]
    verif = subprocess.run(base + ["--verifier-seulement"] + (moteur if reel else []),
                           cwd=str(orch_dir), env=env, capture_output=True, text=True, timeout=600)
    try:
        verif_json = json.loads(verif.stdout) if verif.returncode == 0 else None
    except ValueError:
        verif_json = None
    if verif_json is None or verif_json.get("montant_requis_go_usd") != PLAFOND_ARRET_USD:
        raise Refus(f"vérification de l'orchestrateur refusée (code {verif.returncode}) : "
                    f"{(verif.stderr or verif.stdout).strip()[-800:]!r}")
    if verif_json.get("specification", {}).get("conforme") is not True:
        raise Refus(f"spécification refusée par l'orchestrateur : {verif_json.get('specification')}")
    argv = base + moteur
    avec_carbon = decl["carbon"]["active"]
    depart = {
        "lanceur": {"version": VERSION, "chemin": str(r.lanceur), "sha256": lanceur_sha}, "moteur": r.moteur,
        "horodatage_canonique": horodatage, "id": ident, "go": go, "plafond_arret_usd": PLAFOND_ARRET_USD,
        "preenregistrement": prereg, "contre_lecture": cl, "acte_de_gel_sha256": h_acte, "pieces": pieces,
        "liste_fils": controle_liste, "declaration_relais": {"chemin": str(r.declaration), "sha256": decl_sha},
        "especes_actives": [e["etiquette"] for e in decl["especes_actives"]], "especes_absentes": decl["especes_absentes"],
        "carbon": decl["carbon"], "cles_employees": decl["cles"],
        "cle_par_espece": {e["etiquette"]: decl["cles"][e["fournisseur"]] for e in decl["especes_actives"]},
        "cle_par_role_interne": {"aiguilleur": decl["cles"][fixe["aiguilleur"]["fournisseur"]],
                                 **{j["etiquette"]: decl["cles"][j["fournisseur"]] for j in fixe["juges"]}},
        "parts_au_pire": parts, "procedure_relais_persistants": procedure, "dossier_arrets_credit": str(dossier_arrets),
        "cle_claude": {"nom": CLE_CLAUDE, "presente_dans_l_environnement_du_lanceur": cle_presente, "valeur": "jamais lue",
                       "cles_exclues": list(CLES_INTERDITES)},
        "releve_credits_avant": {"chemin": str(r.releve), "sha256": releve_sha, "cles": credits},
        "orchestrateur": orch, "configuration": {"chemin": str(chemin_conf), "sha256": h_conf},
        "verification_orchestrateur": {k: verif_json.get(k) for k in ("configuration_sha256", "montant_requis_go_usd",
                                                                      "specification", "go", "generations")},
        "commande": argv, "cwd": str(orch_dir), "sortie": str(sortie), "bac_a_sable": bac,
        "environnement": {"noms_retires": retires, "noms_exclus": hors_liste, "valeurs": "jamais lues"},
        "graines": {"racine": conf["racine_graines"], "prefixe": conf["graines"]["prefixe"],
                    "regle": "numpy.random.SeedSequence(racine, spawn_key=(cle_de_tache(tache),)) dans l'orchestrateur (R9)"},
        "versions": _versions(r, orch_dir, env), "depot_travail": _depot_git(r),
        "devis_v5_estimation_sans_marge_usd": DEVIS_V5_TOTAL["avec_carbon" if avec_carbon else "sans_carbon"],
        "journaux": {"stdout": str(dossier_sortie / "course.stdout.txt"), "stderr": str(dossier_sortie / "course.stderr.txt")},
    }
    h_depart = ecrire_scelle(dossier_run / "manifeste-lanceur-depart.json", depart)
    print(json.dumps({"manifeste_depart": str(dossier_run / "manifeste-lanceur-depart.json"), "sha256": h_depart}, ensure_ascii=False),
          flush=True)

    code, pid, echec, arret_credit = None, None, None, []
    debut = _dt.datetime.now(_dt.timezone.utc)
    try:
        with open(dossier_sortie / "course.stdout.txt", "xb") as fo, open(dossier_sortie / "course.stderr.txt", "xb") as fe:
            enfant = subprocess.Popen(argv, cwd=str(orch_dir), env=env, stdout=fo, stderr=fe)
            pid = enfant.pid

            def relayer(num, _cadre):
                try:
                    enfant.send_signal(num)
                except ProcessLookupError:
                    pass
            anciens = {s: signal.signal(s, relayer) for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP)}
            try:
                while True:
                    try:
                        code = enfant.wait(timeout=1.0)
                        break
                    except subprocess.TimeoutExpired:
                        if not arret_credit and any(dossier_arrets.iterdir()):
                            arret_credit = sorted(x.name for x in dossier_arrets.iterdir())
                            enfant.send_signal(signal.SIGTERM)  # R-3237 : arrêt au premier refus pour crédit (par PID, R10)
            finally:
                for s, a in anciens.items():
                    signal.signal(s, a)
    except BaseException as exc:  # noqa: BLE001 — le manifeste de fin est écrit sur tout chemin
        echec = f"{type(exc).__name__}: {exc}"
    fin = _dt.datetime.now(_dt.timezone.utc)
    bilan = {"id": ident, "manifeste_depart_sha256": h_depart, "pid_orchestrateur": pid, "code": code, "echec_lanceur": echec,
             "debut_utc": debut.isoformat(), "fin_utc": fin.isoformat(),
             "arret_au_premier_refus_pour_credit": [json.loads((dossier_arrets / n).read_text(encoding="utf-8"))
                                                    for n in sorted(x.name for x in dossier_arrets.iterdir())]}
    alertes_apres, depasse = [], False
    try:
        couts = couts_reels(sortie)
        cumul = (lire_resume_course(sortie).get("cumul_usd") or 0.0)
        apres, alertes_apres = releve_apres(credits, couts, decl["cles"])
        depasse = bool(couts.get("lisible") and couts["total_usd"] > PLAFOND_ARRET_USD + 1e-9) or cumul > PLAFOND_ARRET_USD + 1e-9
        bilan.update({"ce_qui_a_ete_fait": lire_resume_course(sortie), "cout_reel": couts,
                      "ecart_au_devis_v5": ecart_au_devis(couts, avec_carbon),
                      "plafond_arret": {"usd": PLAFOND_ARRET_USD, "depasse": depasse},
                      "releve_credits_apres": apres, "alertes_apres": alertes_apres})
    except Exception as exc:  # noqa: BLE001 — le manifeste de fin est écrit quand même, l'erreur y est dite
        bilan["erreur_bilan"] = f"{type(exc).__name__}: {exc}"
        echec = echec or bilan["erreur_bilan"]
    bilan["journaux_sha256"] = {n: sha256_fichier(dossier_sortie / n) for n in ("course.stdout.txt", "course.stderr.txt")
                                if (dossier_sortie / n).is_file()}
    if alertes_apres or depasse:
        ecrire_scelle(dossier_run / "alerte-credits-apres.json",
                      {"alerte": "après la course : reste estimé sous le seuil ou plafond d'arrêt dépassé", "cles": alertes_apres,
                       "plafond_depasse": bool(depasse), "pour": "la mère (à transmettre à Lazar avant qu'une clé n'atteigne zéro)"})
    h_fin = ecrire_scelle(dossier_run / "manifeste-lanceur-fin.json", bilan)
    print(json.dumps({"manifeste_fin": str(dossier_run / "manifeste-lanceur-fin.json"), "sha256": h_fin, "code": code,
                      "cout_reel_usd": (bilan.get("cout_reel") or {}).get("total_usd"), "alertes_apres": alertes_apres},
                     ensure_ascii=False), flush=True)
    if echec:
        raise RuntimeError(echec)
    if depasse:
        return 4
    if bilan["arret_au_premier_refus_pour_credit"]:
        return 5
    return 0 if code == 0 else (code if isinstance(code, int) and code > 0 else 2)


# --- essai à blanc ------------------------------------------------------------------------------------------------------------


def reglages_a_blanc(dossier: Path) -> Reglages:
    """Moteur simulé, relais factices (adresses locales sans serveur, portes « commande » factices jamais appelées par le moteur
    simulé), contre-lecture et relevé d'essai écrits dans le dossier, aucun GO. Rien n'est lu dans `registres/`."""
    if dossier.exists():
        raise Refus(f"{dossier} existe déjà (R12)")
    dossier.mkdir(parents=True)
    essai = dossier / "pieces-d-essai"
    essai.mkdir()
    r = Reglages.production()
    lanceur_sha = sha256_fichier(r.lanceur)
    prereg_sha = r.prereg[1] if re.fullmatch(r"[0-9a-f]{64}", r.prereg[1]) else sha256_fichier(r.prereg[0])
    cl = essai / "contre-lecture-d-essai.md"
    ecrire_scelle(cl, f"# Contre-lecture d'ESSAI par le modèle K (aucune valeur réelle)\n\nPréenregistrement lu : {prereg_sha}\n"
                      f"Lanceur lu : {lanceur_sha}\n\n## Verdict\n\nScellable.\n\nEssai à blanc seulement.\n")
    porte = ["/bin/false"]
    decl = {"version": "declaration-relais-essai-a-blanc", "fournisseurs": {
        "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:18999", "nom_cle": CLE_CLAUDE,
                   "porte_plafond": {"type": "commande", "commande": porte, "delai_s": 5}},
        "argon": {"type": "commande_externe", "commande": ["bash", str(r.depot / PIECES["enveloppe_argon"][0])],
                  "nom_cle": "CLE_FACTICE_ARGON", "porte_plafond": {"type": "environnement"}},
        "kimi": {"type": "kimi_protocole", "url_relais": "http://127.0.0.1:18999", "modele": "kimi-k3.1-pro", "prix_entree": 1.0,
                 "prix_sortie": 1.0, "max_sortie_jetons": 1000, "sortie_min_jetons": 100, "delai_s": 5, "nom_cle": "CLE_FACTICE_KIMI",
                 "porte_plafond": {"type": "commande", "commande": porte, "delai_s": 5}},
        "astra": {"type": "commande_externe", "commande": ["/bin/false"], "modele_propose": "modele-factice-astra",
                  "nom_cle": "CLE_FACTICE_ASTRA", "porte_plafond": {"type": "environnement"}},
        "carbon": {"type": "commande_externe", "commande": ["/bin/false"], "modele_propose": "modele-factice-carbon",
                   "nom_cle": "CLE_FACTICE_CARBON", "inscription": INSCRIPTION_CARBON, "porte_plafond": {"type": "environnement"}}}}
    chemin_decl = essai / "declaration-relais-d-essai.json"
    ecrire_scelle(chemin_decl, decl)
    aujourd_hui = _dt.datetime.now(_dt.timezone.utc).date()
    releve = {"version": "releve-credits-essai-a-blanc", "releve_utc": aujourd_hui.isoformat() + " (essai)",
              "cles": dict({n: {"non_lisible": True, "motif": "essai à blanc : solde illisible, sous dispense"}
                            for n in ("CLE_FACTICE_ARGON", "CLE_FACTICE_ASTRA", "CLE_FACTICE_CARBON")},
                           CLE_FACTICE_KIMI={"credit_usd": 32.25, "reste_usd": 32.25, "source": "factice (essai à blanc)"},
                           **{CLE_CLAUDE: {"non_lisible": True, "motif": "essai à blanc : compté au prix relevé",
                                           "depense_anterieure_usd": 0.0}}),
              "dispense": {"par": "mère", "reference": REFERENCE_DISPENSE,
                           "cles": ["CLE_FACTICE_ARGON", "CLE_FACTICE_ASTRA", "CLE_FACTICE_CARBON"]}}
    chemin_releve = essai / "releve-credits-d-essai.json"
    ecrire_scelle(chemin_releve, releve)
    r.prereg = (r.prereg[0], prereg_sha)
    r.contre_lecture, r.declaration, r.releve = cl, chemin_decl, chemin_releve
    r.dossier_runs, r.dossier_sorties = dossier / "runs", dossier / "sorties"
    r.moteur, r.exiger_bac_a_sable, r.verifier_go = "simule", False, False
    return r


def principal(argv: list | None = None, reglages: Reglages | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    try:
        if argv and argv[0] == "--a-blanc" and len(argv) == 2:
            reglages = reglages or reglages_a_blanc(Path(argv[1]).resolve())
        elif argv:
            print(json.dumps({"refus": f"arguments non admis (reçu {argv!r}) ; seul « --a-blanc DOSSIER »"}, ensure_ascii=False),
                  file=sys.stderr)
            return 2
        return executer(reglages or Reglages.production())
    except AlerteCredit as e:
        print(json.dumps({"alerte_credit": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 3
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001
        print(json.dumps({"erreur": f"{type(e).__name__}: {e}"}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(principal())
