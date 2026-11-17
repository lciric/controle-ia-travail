#!/usr/bin/env python3
"""Lanceur de l'organisme d'idéation sur le sujet des organismes discrets (Bras A, permutation des champs CONTROLS,
section 1.2 de la conception v2) — version 7.

Corrections v6→v7 : l'orchestrateur crée des proposeurs et des juges Claude par défaut (Opus 5.5 et Fable 5.1) quand
aucun ``--proposeur`` ni ``--juge`` n'est passé ; avec ``budget-total-usd=0`` (Argon seul), toute session Claude échouait
au contrôle d'allocation dans ``_lancer`` (``plafond > total + ε`` avec ``total=0``).
Correctifs : (a) on passe ``--proposeur factice=modele-factice`` et ``--juge factice-juge=modele-factice`` pour supprimer
les défauts Claude, avec un budget simulé ``TOTAL_SIMULE_USD=5.0`` qui couvre les coûts fictifs de l'adaptateur simulé
(aucun appel Claude réel — le moteur par défaut est ``simule``) ; ``--tolerer-somme-plafonds-claude`` n'est plus nécessaire
(la somme Claude ≈ 0,02 est sous le total simulé) ; (b) nouvelle garde ``garde_modeles_claude`` : interdit tout modèle dont
le nom contient « claude » dans ``--proposeur`` ou ``--juge`` (remplace l'interdiction brute du drapeau) ;
(c) ``--proposeur`` et ``--juge`` retirés de ``DRAPEAUX_CLAUDE_INTERDITS_EXACTS``.

Corrections v5→v6 (héritées) : ``--tolerer-somme-plafonds-claude`` ajouté et retiré des drapeaux interdits (CL37-03).
Corrections v4→v5 (héritées) : ``--temoins`` ajouté à la commande et aux PIECES ; retiré des drapeaux interdits.

Sous GO-2026-11-17-06 (plafond 17 USD = collisionneur + organisme d'idéation, échéance 2026-11-22, Lazar R-3069).
Le collisionneur a consommé environ 7,86 USD (R-3072), reste au plus 9,14 USD pour l'organisme. Proposeur : Argon seul
(pas de Kimi dans cet environnement, pas de Claude dans un rôle de l'organisme). Devis v2 contre-lu : scénario Argon seul
1 génération ≈ 1,5 USD attendu, 2,5 USD pire cas.

Usage, seul et exact (cwd = racine du dépôt de travail) :

    /usr/local/bin/python3 -I -B scripts/lancer_course_ideation_organismes_discrets_v7.py

Ce que fait le lanceur, dans cet ordre ; tout refus rend 2, motif sur la sortie d'erreur :
1. aucun argument ; ligne de GO lue dans `registres/go.md` (type calcul, accordée par Lazar, dans sa période, non révoquée),
   plafond analysé et comparé à la constante épinglée ;
2. orchestrateur : clone `/home/user/lciric/ideation-organism/orchestrator`, commit épinglé, empreintes épinglées de la
   chaîne de lancement (ideation_v8 → v7 → v6 → v5 → v4 → v2, `pole/ideation_v2.py`, `pole/adaptateurs.py`,
   `pole/relais.py`) — **aucune modification** (fichiers suivis, non suivis et ignorés), aucun import de l'orchestrateur ;
3. pièces : question v3, faits v3, témoins plantés v1, enveloppe d'Argon v5, commande d'Argon v3d — empreintes épinglées ;
4. commande : Argon seul en proposeur externe et en juge externe, proposeurs/juges internes factices (moteur simulé,
   aucun modèle Claude), une seule passe, budget externe ≤ plafond restant ;
5. gardes : drapeaux interdits, modèles Claude absents, somme des plafonds, bac à sable, environnement sans clés ;
6. construction de la liste blanche (appel de l'orchestrateur, comparée aux empreintes épinglées) ;
7. manifeste de départ scellé, course, manifeste de fin scellé (y compris en cas d'échec après le manifeste de départ).

Aucun modèle de la famille Claude dans un rôle de l'organisme (N-065, devis v2 § 2). Les proposeurs/juges internes
(``modele-factice``) sont des substituants pour supprimer les défauts Claude de l'orchestrateur ; ils tournent sous
l'adaptateur simulé, aucun appel Claude réel. Pas de ``--moteur``, ``--url-relais`` ni ``--confirmer-moteur-reel`` :
le moteur Claude SDK n'est pas engagé.

Bibliothèque standard seulement (le lanceur tourne sous `-I`).
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
from dataclasses import dataclass, field
from pathlib import Path

VERSION = "lancer_course_ideation_organismes_discrets_v7"
GO_ID = "GO-2026-11-17-06"
DEPOT = Path(__file__).resolve().parents[1]
CUMUL_COLLISIONNEUR_USD = 7.86

ORCHESTRATEUR = Path("/home/user/lciric/ideation-organism/orchestrator")
COMMIT_ORCHESTRATEUR = "a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb"
EMPREINTES_ORCHESTRATEUR = {
    "demonstrations/ideation_v8.py": "2e2be8d72c548e183b94c14de20c971f241f998f54f64c5281b2427fdd64e9d1",
    "demonstrations/ideation_v7.py": "7b90e65e1308b1c230b3f804743cfc42b9dc571d93b73ed6c5f3f8c9d2b481b2",
    "demonstrations/ideation_v6.py": "4c302e5b97b229d5b3edd9e9a427f1e50796c10f7081f63132165ffeef854ba4",
    "demonstrations/ideation_v5.py": "1894f250264eaaccbf891dfa255e71dc587fe415c8d21e283391203a2fe73444",
    "demonstrations/ideation_v4.py": "4212d4c9d014a265847d4c4ed87a8cd804fdafa73f85fd8947874d63fca1c36d",
    "demonstrations/ideation_v2.py": "bc5e9c98acff41b97487e2345d33768c8cdf41f0ededf8b2eed0bf842c889845",
    "pole/ideation_v2.py": "67d2ad3591b21601ece4101154138f532ba519024761beb8c9738181f8f3fefc",
    "pole/adaptateurs.py": "a1a8ede8d38884a28365ee797dcd3018dbf09ea1baefa3f57cfcb3281c529c99",
    "pole/relais.py": "b5a76343e458cf8fb91ee1928244f9cb65d50c27ab9b1bae91c21a5c82349da3",
}
LANCEUR_ORCHESTRATEUR = "demonstrations/ideation_v8.py"

NOTES = "docs/notes/organismes-discrets-v1/organisme-ideation-v1"
PIECES = {
    "question": (f"{NOTES}/question-v3.md",
                 "2f7acf36a1dbdbc53a03a0f775327c773e0152323b04f83b4441db80d6b01dae"),
    "faits": (f"{NOTES}/faits-v3.md",
              "5e2e9dd85a88e9e07da806a3c7657f62c6c6343f11ed6de8a1d507a0b397962f"),
    "enveloppe_argon": ("rapports/fille-ideation-1-v1/appel-argon-v5.sh",
                        "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a"),
    "commande_argon": ("docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py",
                       "46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46"),
    "temoins": (f"{NOTES}/temoins-organisme-discrets-v1.json",
                "1c6eef382f5c2536794e64795905d6f75bf4170fdfd4534102f99321a485e48b"),
}
DEPOT_ATTENDU_PAR_L_ENVELOPPE = Path("/home/user/controle-ia-travail")

TOTAL_PLAFOND_GO_USD = 17.0
TOTAL_EXTERNE_USD = 9.14
PLAFONDS = {
    "proposeur_ideation|gemini-4-argon": 2.5,
    "juge_ideation|gemini-4-argon": 3.0,
    "proposeur_ideation|modele-factice": 0.01,
    "juge_ideation|modele-factice": 0.01,
}
TOTAL_SIMULE_USD = 5.0
CONTROLE_EXTERNE_USD = 1.5
CONTROLE_BRAS_DEFAUT_USD = 0.2
DEFAUT_EXTERNE_PROPOSEUR_USD = 2.5
DEFAUT_EXTERNE_JUGE_USD = 3.5
DEFAUT_CONTROLE_EXTERNE_USD = 2.5
NOMBRE_FICHES = 6
GRAINE = 2026111706

DOSSIER_SORTIES = Path("/home/user/sorties-course-ideation-organismes-discrets-v7")
SOUS_DOSSIER_RUNS = "course-ideation-organismes-discrets-v7"
SUFFIXE_RUN = "-course-ideation-organismes-discrets-v7"
NOMS_PERMIS = ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR")

DRAPEAUX_INTERDITS = (
    "--accepter-sans-bac-a-sable", "--motif-sans-bac-a-sable",
    "--tolerer-somme-plafonds", "--tolerer-somme-plafonds-externe",
    "--taille-max-consigne-externe", "--taille-max-consigne-externe-bras", "--prix-entree-usd-par-million-jetons",
)
DRAPEAUX_CLAUDE_INTERDITS_EXACTS = (
    "--moteur", "--url-relais", "--confirmer-moteur-reel", "--seconde-passe",
    "--piece-juge", "--synthese",
)
MODELES_CLAUDE = ("claude-opus", "claude-fable", "claude-sonnet", "claude-haiku")

NOMS_DE_CLE = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN", "OPENAI_API_KEY", "GOOGLE_API_KEY",
               "GEMINI_API_KEY", "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "GITHUB_TOKEN", "GH_TOKEN", "HF_TOKEN")
MOTIF_NOM_DE_CLE = re.compile(r"(API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL)", re.I)

SONDE_BAC_A_SABLE = (
    "import json, sys\n"
    "sys.path.insert(0, sys.argv[1])\n"
    "from pole.adaptateurs import etat_bac_a_sable_detaille\n"
    "print(json.dumps(etat_bac_a_sable_detaille()))\n"
)


class Refus(RuntimeError):
    """Garde du lanceur : rien n'est lancé."""


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


@dataclass
class Reglages:
    depot: Path
    orchestrateur: Path
    commit_orchestrateur: str
    empreintes_orchestrateur: dict
    pieces: dict
    registre_go: Path
    dossier_runs: Path
    dossier_sorties: Path
    depot_attendu_par_l_enveloppe: Path
    python: str
    plafonds: dict = field(default_factory=lambda: dict(PLAFONDS))
    controle_externe_usd: float = CONTROLE_EXTERNE_USD
    arguments_en_plus: tuple = ()
    environnement: dict | None = None
    aujourd_hui: _dt.date | None = None
    horodatage: object = date_u

    @classmethod
    def production(cls) -> "Reglages":
        return cls(depot=DEPOT, orchestrateur=ORCHESTRATEUR, commit_orchestrateur=COMMIT_ORCHESTRATEUR,
                   empreintes_orchestrateur=dict(EMPREINTES_ORCHESTRATEUR), pieces=dict(PIECES),
                   registre_go=DEPOT / "registres" / "go.md", dossier_runs=DEPOT / "runs", dossier_sorties=DOSSIER_SORTIES,
                   depot_attendu_par_l_enveloppe=DEPOT_ATTENDU_PAR_L_ENVELOPPE, python=sys.executable)


def _normaliser(texte: str) -> str:
    import unicodedata
    return unicodedata.normalize("NFKD", texte.lower()).encode("ascii", "ignore").decode()


def _est_revocation(cellules: list, go_id: str) -> bool:
    if any(_normaliser(c).startswith("revoc") for c in cellules):
        if any(go_id in c for c in cellules):
            return True
    return False


def verifier_go(registre: Path, aujourd_hui: _dt.date, go_id: str = GO_ID) -> dict:
    if not registre.is_file():
        raise Refus(f"registre des GO absent : {registre}")
    lignes = registre.read_text(encoding="utf-8").splitlines()
    ligne_go = re.compile(r"^\|\s*(GO-\d{4}-\d{2}-\d{2}-\d{2})\s*\|")
    trouvees, revocations = [], []
    for ligne in lignes:
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
    ident, accorde, typ, perimetre, plafond, echeance, par, ref = c
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
    if "organisme" not in perimetre.lower() or "idéation" not in perimetre.lower():
        raise Refus(f"{go_id} : périmètre sans « organisme d'idéation » — ce n'est pas le GO de cette course")
    m_plafond = re.match(r"^\s*([\d]+(?:[.,]\d+)?)\s*(?:USD|usd)\s*$", plafond)
    if not m_plafond:
        raise Refus(f"{go_id} : plafond illisible {plafond!r} (nombre + USD attendu)")
    plafond_lu = float(m_plafond.group(1).replace(",", "."))
    if plafond_lu != TOTAL_PLAFOND_GO_USD:
        raise Refus(f"{go_id} : plafond lu {plafond_lu} USD != épinglé {TOTAL_PLAFOND_GO_USD} USD")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "plafond": plafond, "plafond_lu": plafond_lu,
            "par": par, "ligne_sha256": hashlib.sha256(("|".join(c)).encode("utf-8")).hexdigest()}


def _git(dossier: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(dossier), *args], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        raise Refus(f"git {' '.join(args)} dans {dossier} : code {r.returncode} ({r.stderr.strip()[:200]})")
    return r.stdout


def verifier_orchestrateur(r: Reglages) -> dict:
    if not (r.orchestrateur / LANCEUR_ORCHESTRATEUR).is_file():
        raise Refus(f"orchestrateur absent : {r.orchestrateur / LANCEUR_ORCHESTRATEUR}")
    tete = _git(r.orchestrateur, "rev-parse", "HEAD").strip()
    if tete != r.commit_orchestrateur:
        raise Refus(f"orchestrateur au commit {tete}, {r.commit_orchestrateur} exigé")
    porcelaine = _git(r.orchestrateur, "status", "--porcelain", "--untracked-files=all", "--ignored=matching").strip()
    if porcelaine:
        raise Refus(f"orchestrateur modifié, fichiers non suivis ou ignorés : {porcelaine[:200]!r}")
    ecarts = {}
    for rel, attendu in sorted(r.empreintes_orchestrateur.items()):
        p = r.orchestrateur / rel
        lu = sha256_fichier(p) if p.is_file() else None
        if lu != attendu:
            ecarts[rel] = lu
    if ecarts:
        raise Refus(f"orchestrateur : empreintes différentes ou fichiers absents : {ecarts}")
    return {"chemin": str(r.orchestrateur), "commit": tete, "empreintes": dict(r.empreintes_orchestrateur)}


def verifier_pieces(r: Reglages) -> dict:
    if r.depot.resolve() != r.depot_attendu_par_l_enveloppe.resolve():
        raise Refus(f"dépôt de travail en {r.depot}, l'enveloppe d'Argon v5 attend {r.depot_attendu_par_l_enveloppe}")
    lues, ecarts = {}, {}
    for nom, (rel, attendu) in sorted(r.pieces.items()):
        p = r.depot / rel
        lu = sha256_fichier(p) if p.is_file() else None
        if lu != attendu:
            ecarts[nom] = {"chemin": rel, "attendu": attendu, "lu": lu}
        lues[nom] = {"chemin": rel, "sha256": attendu}
    if ecarts:
        raise Refus("pièces absentes ou d'empreinte différente (R11) : "
                    + json.dumps(ecarts, ensure_ascii=False))
    return lues


def _usd(x: float) -> str:
    return repr(float(x))


def commande_course(r: Reglages, sortie: Path, liste_blanche: Path, horodatage: str) -> list:
    p = {nom: str(r.depot / rel) for nom, (rel, _) in r.pieces.items()}
    for nom in ("question", "enveloppe_argon"):
        if any(ch.isspace() for ch in p[nom]):
            raise Refus(f"chemin avec espace ({nom})")
    b = r.plafonds
    argv = [
        r.python, "-I", "-B", LANCEUR_ORCHESTRATEUR, str(sortie),
        "--liste-blanche", str(liste_blanche),
        "--question", p["question"],
        "--piece", p["faits"],
        "--temoins", p["temoins"],
        "--proposeur", "factice=modele-factice",
        "--juge", "factice-juge=modele-factice",
        "--proposeur-externe", "argon=gemini-4-argon",
        "--commande-externe", "bash " + p["enveloppe_argon"],
        "--juge-externe", "argon-juge=gemini-4-argon",
        "--nombre", str(NOMBRE_FICHES),
        "--budget-total-usd", _usd(TOTAL_SIMULE_USD),
        "--budget-externe-usd", _usd(TOTAL_EXTERNE_USD),
        "--budget", f"proposeur_ideation|modele-factice={_usd(b['proposeur_ideation|modele-factice'])}",
        "--budget", f"juge_ideation|modele-factice={_usd(b['juge_ideation|modele-factice'])}",
        "--budget", f"proposeur_ideation|gemini-4-argon={_usd(b['proposeur_ideation|gemini-4-argon'])}",
        "--budget", f"juge_ideation|gemini-4-argon={_usd(b['juge_ideation|gemini-4-argon'])}",
        "--budget-controle-externe-usd", _usd(r.controle_externe_usd),
        "--graine", str(GRAINE),
        "--horodatage", horodatage,
    ]
    return argv + list(r.arguments_en_plus)


def garde_drapeaux(argv: list) -> None:
    trouves = []
    for jeton in argv:
        if not isinstance(jeton, str) or not jeton.startswith("--") or len(jeton) <= 2:
            continue
        nom = jeton.split("=", 1)[0]
        if any(f == nom or f.startswith(nom) for f in DRAPEAUX_INTERDITS):
            trouves.append(jeton)
        elif nom in DRAPEAUX_CLAUDE_INTERDITS_EXACTS:
            trouves.append(jeton)
    if trouves:
        raise Refus(f"drapeau(x) interdit(s) : {trouves}")


def garde_modeles_claude(argv: list) -> None:
    for option in ("--proposeur", "--juge"):
        for valeur in _valeurs(argv, option):
            modele = valeur.split("=", 1)[1] if "=" in valeur else valeur
            if any(m in modele.lower() for m in MODELES_CLAUDE):
                raise Refus(f"modèle Claude interdit dans {option} : {valeur!r} (N-065)")


def _valeurs(argv: list, option: str) -> list:
    out = []
    for i, jeton in enumerate(argv):
        if jeton == option and i + 1 < len(argv):
            out.append(argv[i + 1])
        elif isinstance(jeton, str) and jeton.startswith(option + "="):
            out.append(jeton.split("=", 1)[1])
    return out


def _une(argv: list, option: str, defaut: float | None) -> float | None:
    v = _valeurs(argv, option)
    if len(v) > 1:
        raise Refus(f"{option} donné {len(v)} fois")
    return float(v[0]) if v else defaut


def sommes_plafonds(argv: list) -> dict:
    budgets = {}
    prop_ext = [v.split("=", 1)[1] for v in _valeurs(argv, "--proposeur-externe")]
    juges_ext = [v.split("=", 1)[1] for v in _valeurs(argv, "--juge-externe")]
    for m in juges_ext:
        budgets.setdefault(f"juge_ideation|{m}", DEFAUT_EXTERNE_JUGE_USD)
    for m in prop_ext:
        budgets.setdefault(f"proposeur_ideation|{m}", DEFAUT_EXTERNE_PROPOSEUR_USD)
    for v in _valeurs(argv, "--budget"):
        cle, valeur = v.split("=", 1)
        role, modele = cle.split("|", 1)
        budgets[f"{role.strip()}|{modele.strip()}"] = float(valeur)
    controle_ext = _une(argv, "--budget-controle-externe-usd", DEFAUT_CONTROLE_EXTERNE_USD)
    total_externe = _une(argv, "--budget-externe-usd", 11.6)
    somme_externe = controle_ext * len(prop_ext) \
        + sum(budgets[f"proposeur_ideation|{m}"] for m in prop_ext) \
        + sum(budgets[f"juge_ideation|{m}"] for m in juges_ext) \
        + CONTROLE_BRAS_DEFAUT_USD * len(juges_ext)
    return {"somme_externe": round(somme_externe, 6), "total_externe": total_externe,
            "detail": {"controle_externe": controle_ext,
                       "proposeurs_externes": {m: budgets[f"proposeur_ideation|{m}"] for m in prop_ext},
                       "juges_externes": {m: budgets[f"juge_ideation|{m}"] for m in juges_ext},
                       "controle_du_bras": CONTROLE_BRAS_DEFAUT_USD}}


def garde_sommes(argv: list) -> dict:
    s = sommes_plafonds(argv)
    if not s["somme_externe"] < s["total_externe"]:
        raise Refus(f"somme des plafonds externes {s['somme_externe']:.2f} pas sous le total externe {s['total_externe']}")
    if s["total_externe"] != TOTAL_EXTERNE_USD:
        raise Refus(f"total externe {s['total_externe']} != épinglé {TOTAL_EXTERNE_USD}")
    if round(CUMUL_COLLISIONNEUR_USD + s["total_externe"], 2) > TOTAL_PLAFOND_GO_USD:
        raise Refus(f"cumul collisionneur ({CUMUL_COLLISIONNEUR_USD}) + total externe ({s['total_externe']}) "
                    f"= {CUMUL_COLLISIONNEUR_USD + s['total_externe']:.2f} > plafond GO ({TOTAL_PLAFOND_GO_USD})")
    total_simule = _une(argv, "--budget-total-usd", None)
    if total_simule is not None and total_simule != TOTAL_SIMULE_USD:
        raise Refus(f"budget total simulé doit être {TOTAL_SIMULE_USD} (factice seulement, aucun Claude), reçu {total_simule}")
    return s


def sonder_bac_a_sable(r: Reglages, env: dict) -> dict:
    try:
        p = subprocess.run([r.python, "-I", "-B", "-c", SONDE_BAC_A_SABLE, str(r.orchestrateur)], cwd=str(r.orchestrateur),
                           env=env, capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError) as e:
        raise Refus(f"sonde du bac à sable non exécutée ({type(e).__name__})") from None
    lignes = [x for x in p.stdout.splitlines() if x.strip()]
    try:
        etat = json.loads(lignes[-1]) if p.returncode == 0 and lignes else None
    except json.JSONDecodeError:
        etat = None
    if not (isinstance(etat, dict) and isinstance(etat.get("actif"), bool) and isinstance(etat.get("proc_neuf"), bool)):
        raise Refus(f"sonde du bac à sable illisible (code {p.returncode}) : {p.stderr.strip()[-500:]!r}")
    if not etat["actif"]:
        raise Refus("bac à sable inactif : " + str(etat.get("motif")))
    if not etat["proc_neuf"]:
        raise Refus("bac à sable sans /proc neuf : " + str(etat.get("motif")))
    return etat


def environnement_filtre(env: dict) -> tuple:
    retires = sorted(n for n in env if n in NOMS_DE_CLE or MOTIF_NOM_DE_CLE.search(n))
    noms_hors_liste = sorted(n for n in env if n not in NOMS_PERMIS and n not in retires)
    garde = {n: env[n] for n in env if n in NOMS_PERMIS}
    garde["GO_ID"] = GO_ID
    garde["HOME"] = str(DOSSIER_SORTIES)
    garde["PYTHONPYCACHEPREFIX"] = str(DOSSIER_SORTIES / "pycache")
    return garde, retires, noms_hors_liste


def ecrire_scelle(chemin: Path, contenu: dict) -> str:
    if chemin.exists():
        raise Refus(f"{chemin} existe déjà (R12)")
    donnees = (json.dumps(contenu, ensure_ascii=False, indent=1, sort_keys=True) + "\n").encode("utf-8")
    with open(chemin, "xb") as f:
        f.write(donnees)
    h = hashlib.sha256(donnees).hexdigest()
    with open(str(chemin) + ".sha256", "x", encoding="utf-8") as f:
        f.write(f"{h}  {chemin.name}\n")
    return h


def construire_liste_blanche(r: Reglages, chemin: Path, env: dict) -> dict:
    fichiers = [str(r.depot / r.pieces[n][0]) for n in ("question", "faits", "temoins")]
    p = subprocess.run([r.python, "-I", "-B", LANCEUR_ORCHESTRATEUR, str(chemin), "--construire-liste-blanche", *fichiers],
                       cwd=str(r.orchestrateur), env=env, capture_output=True, text=True, timeout=120)
    if p.returncode != 0 or not chemin.is_file():
        raise Refus(f"liste blanche non construite (code {p.returncode}) : {p.stderr.strip()[-500:]!r}")
    lue = json.loads(chemin.read_text(encoding="utf-8"))
    attendue = {os.path.realpath(r.depot / r.pieces[n][0]): r.pieces[n][1] for n in ("question", "faits", "temoins")}
    if lue != attendue:
        raise Refus(f"liste blanche différente des pièces épinglées : {lue}")
    return {"chemin": str(chemin), "sha256": sha256_fichier(chemin), "contenu": lue}


def _depot_git(r: Reglages) -> dict:
    try:
        return {"commit": _git(r.depot, "rev-parse", "HEAD").strip(),
                "arbre_modifie": bool(_git(r.depot, "status", "--porcelain", "--untracked-files=no").strip())}
    except Refus as e:
        return {"commit": None, "erreur": str(e)}


def executer(r: Reglages) -> int:
    env_lu = dict(os.environ) if r.environnement is None else dict(r.environnement)
    aujourd_hui = r.aujourd_hui or _dt.datetime.now(_dt.timezone.utc).date()

    go = verifier_go(r.registre_go, aujourd_hui)
    orch = verifier_orchestrateur(r)
    pieces = verifier_pieces(r)
    horodatage = r.horodatage()
    ident = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%d-%H%M%S") + SUFFIXE_RUN
    dossier_run = r.dossier_runs / ident
    dossier_sortie = r.dossier_sorties / ident
    sortie = dossier_sortie / "sortie"
    liste_blanche = dossier_run / "liste-blanche.json"
    argv = commande_course(r, sortie, liste_blanche, horodatage)
    garde_drapeaux(argv)
    garde_modeles_claude(argv)
    sommes = garde_sommes(argv)
    env, retires, exclus = environnement_filtre(env_lu)
    bac = sonder_bac_a_sable(r, env)
    if dossier_run.exists() or dossier_sortie.exists():
        raise Refus(f"{dossier_run} ou {dossier_sortie} existe déjà (R12)")

    dossier_run.mkdir(parents=True)
    dossier_sortie.mkdir(parents=True)
    lb = construire_liste_blanche(r, liste_blanche, env)
    depart = {
        "lanceur": {"version": VERSION, "chemin": str(Path(__file__).resolve()), "sha256": sha256_fichier(Path(__file__))},
        "horodatage_canonique": horodatage, "id": ident, "go": go,
        "cumul_collisionneur_usd": CUMUL_COLLISIONNEUR_USD,
        "orchestrateur": orch, "pieces": pieces, "liste_blanche": lb, "bac_a_sable": bac,
        "commande": argv, "cwd": str(r.orchestrateur), "sortie": str(sortie),
        "plafonds": {"externe_usd": TOTAL_EXTERNE_USD, "detail": dict(PLAFONDS),
                     "controle_externe_usd": CONTROLE_EXTERNE_USD, "sommes": sommes},
        "drapeaux_interdits_verifies_absents": list(DRAPEAUX_INTERDITS),
        "cles": {"noms_retires": retires, "noms_exclus_de_la_liste_permise": exclus, "valeurs": "jamais lues"},
        "depot_travail": _depot_git(r), "python": {"executable": r.python, "version": sys.version.split()[0]},
        "journaux": {"stdout": str(dossier_sortie / "course.stdout.txt"), "stderr": str(dossier_sortie / "course.stderr.txt")},
        "graine": GRAINE,
    }
    h_depart = ecrire_scelle(dossier_run / "manifeste-lanceur-depart.json", depart)
    print(json.dumps({"manifeste_depart": str(dossier_run / "manifeste-lanceur-depart.json"), "sha256": h_depart,
                      "sortie": str(sortie)}, ensure_ascii=False), flush=True)

    code = None
    pid = None
    try:
        debut = _dt.datetime.now(_dt.timezone.utc)
        with open(dossier_sortie / "course.stdout.txt", "xb") as fo, open(dossier_sortie / "course.stderr.txt", "xb") as fe:
            enfant = subprocess.Popen(argv, cwd=str(r.orchestrateur), env=env, stdout=fo, stderr=fe)
            pid = enfant.pid

            def relayer(num, _cadre):
                try:
                    enfant.send_signal(num)
                except ProcessLookupError:
                    pass
            anciens = {s: signal.signal(s, relayer) for s in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP)}
            try:
                code = enfant.wait()
            finally:
                for s, a in anciens.items():
                    signal.signal(s, a)
    except BaseException as exc:
        fin = _dt.datetime.now(_dt.timezone.utc)
        bilan = {"id": ident, "manifeste_depart_sha256": h_depart, "pid_orchestrateur": pid,
                 "code": code, "echec_lanceur": f"{type(exc).__name__}: {exc}",
                 "debut_utc": debut.isoformat(), "fin_utc": fin.isoformat(),
                 "sortie_existe": sortie.exists()}
        try:
            ecrire_scelle(dossier_run / "manifeste-lanceur-fin.json", bilan)
        except Exception:
            pass
        raise
    fin = _dt.datetime.now(_dt.timezone.utc)
    bilan = {"id": ident, "manifeste_depart_sha256": h_depart, "pid_orchestrateur": pid, "code": code,
             "debut_utc": debut.isoformat(), "fin_utc": fin.isoformat(),
             "journaux_sha256": {n: sha256_fichier(dossier_sortie / n) for n in ("course.stdout.txt", "course.stderr.txt")},
             "sortie_existe": sortie.exists()}
    h_fin = ecrire_scelle(dossier_run / "manifeste-lanceur-fin.json", bilan)
    print(json.dumps({"manifeste_fin": str(dossier_run / "manifeste-lanceur-fin.json"), "sha256": h_fin, "code": code},
                     ensure_ascii=False), flush=True)
    return code


def principal(argv: list | None = None, reglages: Reglages | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if argv:
        print(json.dumps({"refus": f"aucun argument admis (reçu {argv!r})"},
                         ensure_ascii=False), file=sys.stderr)
        return 2
    try:
        return executer(reglages or Reglages.production())
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    except Exception as e:
        print(json.dumps({"erreur": f"{type(e).__name__}: {e}"}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(principal())
