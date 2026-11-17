#!/usr/bin/env python3
"""Lanceur du bras du juge différé de l'organisme d'idéation sur les organismes discrets — version 1.

Joue le juge Argon (``gemini-4-argon``) sur les fiches validées de la course v7 (lanceur v7),
après attestation de lecture humaine scellée. Suit le même commit de l'orchestrateur (a41b7b50),
les mêmes empreintes de la chaîne de lancement et les mêmes pièces que la course.

Sous GO-2026-11-17-06 (plafond 17 USD, échéance 2026-11-22).
Le collisionneur a consommé environ 7,86 USD, la course du lanceur v7 environ 0,26 USD externe.
Reste au plus 8,88 USD pour le bras du juge.

Usage, seul et exact (cwd = racine du dépôt de travail) :

    /usr/local/bin/python3 -I -B scripts/lancer_bras_juge_ideation_organismes_discrets_v1.py

Ce que fait le lanceur, dans cet ordre ; tout refus rend 2, motif sur la sortie d'erreur :
1. aucun argument ; ligne de GO lue dans ``registres/go.md`` ;
2. orchestrateur : même commit épinglé et mêmes empreintes que la course ;
3. attestation de lecture humaine : existence, scellement, champs obligatoires, empreintes des fiches et de la consigne ;
4. sortie de la course v7 : existence, manifeste de fin scellé, code 4 (bras en attente) ;
5. gardes : drapeaux interdits, modèles Claude absents, bac à sable, environnement sans clés ;
6. commande du bras différé : ``--bras-rapporte-differe``, ``--attestation-lecture-humaine``, ``--juge-externe``,
   ``--commande-externe``, budget externe restant ;
7. manifeste de départ scellé, bras, manifeste de fin scellé.

Bibliothèque standard seulement (le lanceur tourne sous ``-I``).
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
from pathlib import Path

VERSION = "lancer_bras_juge_ideation_organismes_discrets_v1"
GO_ID = "GO-2026-11-17-06"
DEPOT = Path(__file__).resolve().parents[1]

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

ENVELOPPE_ARGON = "rapports/fille-ideation-1-v1/appel-argon-v5.sh"
ENVELOPPE_ARGON_SHA256 = "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a"

SORTIE_COURSE = Path(
    "/home/user/sorties-course-ideation-organismes-discrets-v7"
    "/20261117-155203-course-ideation-organismes-discrets-v7/sortie"
)
MANIFESTE_FIN_COURSE_SHA256 = "e31ac0d1"  # prefix, vérifié en entier ci-dessous

FICHES_VALIDEES_SHA256 = "b498e819f9b49456c5e4ab109a80597929e5e7e8efd0cc80ff1c99cc95f98d89"
CONSIGNE_EN_ATTENTE_SHA256 = {
    "argon-juge": "72c875d68ee1a105b5138aa7255b40ecc697acc2e3025193317a63d67490fb6d"
}

TOTAL_PLAFOND_GO_USD = 17.0
CUMUL_COLLISIONNEUR_USD = 7.86
BUDGET_EXTERNE_TOTAL_COURSE_USD = 9.14
COUT_EXTERNE_COURSE_USD = 0.2558
BUDGET_EXTERNE_BRAS_USD = round(BUDGET_EXTERNE_TOTAL_COURSE_USD - COUT_EXTERNE_COURSE_USD, 4)
PLAFOND_JUGE_USD = 3.5

ATTESTATION_CHEMIN = DEPOT / "rapports" / "organismes-discrets-v1" / "attestation-lecture-fiches-v1.json"

NOMS_PERMIS = ("PATH", "LANG", "LC_ALL", "TZ", "TMPDIR")
NOMS_DE_CLE = (
    "ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN",
    "OPENAI_API_KEY", "GOOGLE_API_KEY", "GEMINI_API_KEY",
    "AWS_SECRET_ACCESS_KEY", "AWS_SESSION_TOKEN", "GITHUB_TOKEN", "GH_TOKEN", "HF_TOKEN",
)
MOTIF_NOM_DE_CLE = re.compile(r"(API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL)", re.I)

DRAPEAUX_INTERDITS = (
    "--accepter-sans-bac-a-sable", "--motif-sans-bac-a-sable",
    "--tolerer-somme-plafonds", "--tolerer-somme-plafonds-externe",
    "--taille-max-consigne-externe", "--taille-max-consigne-externe-bras",
    "--prix-entree-usd-par-million-jetons",
)
DRAPEAUX_CLAUDE_INTERDITS_EXACTS = (
    "--moteur", "--url-relais", "--confirmer-moteur-reel", "--seconde-passe",
    "--piece-juge", "--synthese",
)
MODELES_CLAUDE = ("claude-opus", "claude-fable", "claude-sonnet", "claude-haiku")

DOSSIER_SORTIES = Path("/home/user/sorties-bras-juge-ideation-organismes-discrets-v1")
SUFFIXE_RUN = "-bras-juge-ideation-organismes-discrets-v1"

SONDE_BAC_A_SABLE = (
    "import json, sys\n"
    "sys.path.insert(0, sys.argv[1])\n"
    "from pole.adaptateurs import etat_bac_a_sable_detaille\n"
    "print(json.dumps(etat_bac_a_sable_detaille()))\n"
)


class Refus(RuntimeError):
    pass


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
        raise Refus(f"{go_id} : {len(principales)} ligne(s) principale(s) (une exigée)")
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
        raise Refus(f"{go_id} : dates illisibles") from None
    if not d_acc <= aujourd_hui <= d_ech:
        raise Refus(f"{go_id} hors de sa période de validité ({d_acc} -> {d_ech})")
    if revocations:
        raise Refus(f"{go_id} révoqué par {', '.join(sorted(revocations))}")
    m_plafond = re.match(r"^\s*([\d]+(?:[.,]\d+)?)\s*(?:USD|usd)\s*$", plafond)
    if not m_plafond:
        raise Refus(f"{go_id} : plafond illisible")
    plafond_lu = float(m_plafond.group(1).replace(",", "."))
    if plafond_lu != TOTAL_PLAFOND_GO_USD:
        raise Refus(f"{go_id} : plafond lu {plafond_lu} USD != épinglé {TOTAL_PLAFOND_GO_USD} USD")
    return {"id": ident, "accorde": accorde, "echeance": echeance, "plafond_lu": plafond_lu, "par": par,
            "ligne_sha256": hashlib.sha256(("|".join(c)).encode("utf-8")).hexdigest()}


def _git(dossier: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(dossier), *args], capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        raise Refus(f"git {' '.join(args)} dans {dossier} : code {r.returncode} ({r.stderr.strip()[:200]})")
    return r.stdout


def verifier_orchestrateur() -> dict:
    if not (ORCHESTRATEUR / LANCEUR_ORCHESTRATEUR).is_file():
        raise Refus(f"orchestrateur absent : {ORCHESTRATEUR / LANCEUR_ORCHESTRATEUR}")
    tete = _git(ORCHESTRATEUR, "rev-parse", "HEAD").strip()
    if tete != COMMIT_ORCHESTRATEUR:
        raise Refus(f"orchestrateur au commit {tete}, {COMMIT_ORCHESTRATEUR} exigé")
    porcelaine = _git(ORCHESTRATEUR, "status", "--porcelain", "--untracked-files=all", "--ignored=matching").strip()
    if porcelaine:
        raise Refus(f"orchestrateur modifié : {porcelaine[:200]!r}")
    ecarts = {}
    for rel, attendu in sorted(EMPREINTES_ORCHESTRATEUR.items()):
        p = ORCHESTRATEUR / rel
        lu = sha256_fichier(p) if p.is_file() else None
        if lu != attendu:
            ecarts[rel] = lu
    if ecarts:
        raise Refus(f"orchestrateur : empreintes différentes : {ecarts}")
    return {"chemin": str(ORCHESTRATEUR), "commit": tete}


def verifier_enveloppe() -> dict:
    chemin = DEPOT / ENVELOPPE_ARGON
    if not chemin.is_file():
        raise Refus(f"enveloppe d'Argon absente : {chemin}")
    lu = sha256_fichier(chemin)
    if lu != ENVELOPPE_ARGON_SHA256:
        raise Refus(f"enveloppe d'Argon : empreinte {lu}, {ENVELOPPE_ARGON_SHA256} épinglée")
    return {"chemin": str(chemin), "sha256": lu}


def verifier_sortie_course() -> dict:
    if not SORTIE_COURSE.is_dir():
        raise Refus(f"sortie de la course absente : {SORTIE_COURSE}")
    manifeste_fin = SORTIE_COURSE / "manifeste-fin.json"
    if not manifeste_fin.is_file():
        raise Refus(f"manifeste de fin de la course absent")
    sha_compagnon = manifeste_fin.with_suffix(".json.sha256")
    if not sha_compagnon.is_file():
        raise Refus("manifeste de fin sans empreinte compagnon")
    with open(sha_compagnon, "r", encoding="utf-8") as f:
        attendu = f.read().split()[0]
    lu = sha256_fichier(manifeste_fin)
    if lu != attendu:
        raise Refus(f"manifeste de fin : empreinte {lu} != compagnon {attendu}")
    with open(manifeste_fin, "r", encoding="utf-8") as f:
        mf = json.load(f)
    code_course = mf.get("code_sortie")
    fiches_v = SORTIE_COURSE / "fiches-validees.json"
    if not fiches_v.is_file():
        raise Refus("fiches-validees.json absent")
    lu_fv = sha256_fichier(fiches_v)
    if lu_fv != FICHES_VALIDEES_SHA256:
        raise Refus(f"fiches-validees.json : empreinte {lu_fv}, {FICHES_VALIDEES_SHA256} épinglée")
    return {"manifeste_fin_sha256": lu, "code_course": code_course, "fiches_validees_sha256": lu_fv}


def verifier_attestation() -> dict:
    if not ATTESTATION_CHEMIN.is_file():
        raise Refus(f"attestation absente : {ATTESTATION_CHEMIN}")
    sha_compagnon = ATTESTATION_CHEMIN.with_suffix(".json.sha256")
    if not sha_compagnon.is_file():
        raise Refus("attestation sans empreinte compagnon")
    with open(sha_compagnon, "r", encoding="utf-8") as f:
        attendu = f.read().split()[0]
    lu = sha256_fichier(ATTESTATION_CHEMIN)
    if lu != attendu:
        raise Refus(f"attestation : empreinte {lu} != compagnon {attendu}")
    with open(ATTESTATION_CHEMIN, "r", encoding="utf-8") as f:
        att = json.load(f)
    for champ in ("lecteur", "lu_le", "fiches_validees_sha256", "consignes_en_attente_sha256"):
        if not att.get(champ):
            raise Refus(f"attestation : champ « {champ} » manquant ou vide")
    if att["fiches_validees_sha256"] != FICHES_VALIDEES_SHA256:
        raise Refus(f"attestation : empreinte des fiches {att['fiches_validees_sha256']} != {FICHES_VALIDEES_SHA256}")
    if att["consignes_en_attente_sha256"] != CONSIGNE_EN_ATTENTE_SHA256:
        raise Refus(f"attestation : consignes en attente différentes de l'épinglé")
    return {"chemin": str(ATTESTATION_CHEMIN), "sha256": lu, "lecteur": att["lecteur"], "lu_le": att["lu_le"]}


def commande_bras(horodatage: str) -> list:
    enveloppe = str(DEPOT / ENVELOPPE_ARGON)
    if any(ch.isspace() for ch in enveloppe):
        raise Refus(f"chemin avec espace ({enveloppe})")
    return [
        sys.executable, "-I", "-B", LANCEUR_ORCHESTRATEUR, str(SORTIE_COURSE),
        "--bras-rapporte-differe",
        "--attestation-lecture-humaine", str(ATTESTATION_CHEMIN),
        "--juge-externe", "argon-juge=gemini-4-argon",
        "--commande-externe", "bash " + enveloppe,
        "--budget", f"juge_ideation|gemini-4-argon={PLAFOND_JUGE_USD!r}",
        "--budget-externe-usd", repr(BUDGET_EXTERNE_BRAS_USD),
        "--horodatage", horodatage,
    ]


def garde_drapeaux(argv: list) -> None:
    for jeton in argv:
        if not isinstance(jeton, str) or not jeton.startswith("--") or len(jeton) <= 2:
            continue
        nom = jeton.split("=", 1)[0]
        if any(f == nom or f.startswith(nom) for f in DRAPEAUX_INTERDITS):
            raise Refus(f"drapeau interdit : {jeton}")
        elif nom in DRAPEAUX_CLAUDE_INTERDITS_EXACTS:
            raise Refus(f"drapeau interdit : {jeton}")


def garde_modeles_claude(argv: list) -> None:
    for option in ("--juge-externe", "--juge"):
        for i, jeton in enumerate(argv):
            if jeton == option and i + 1 < len(argv):
                valeur = argv[i + 1]
                modele = valeur.split("=", 1)[1] if "=" in valeur else valeur
                if any(m in modele.lower() for m in MODELES_CLAUDE):
                    raise Refus(f"modèle Claude interdit dans {option} : {valeur!r}")


def environnement_filtre(env: dict) -> tuple:
    retires = sorted(n for n in env if n in NOMS_DE_CLE or MOTIF_NOM_DE_CLE.search(n))
    noms_hors_liste = sorted(n for n in env if n not in NOMS_PERMIS and n not in retires)
    garde = {n: env[n] for n in env if n in NOMS_PERMIS}
    garde["GO_ID"] = GO_ID
    garde["HOME"] = str(DOSSIER_SORTIES)
    garde["PYTHONPYCACHEPREFIX"] = str(DOSSIER_SORTIES / "pycache")
    return garde, retires, noms_hors_liste


def sonder_bac_a_sable(env: dict) -> dict:
    try:
        p = subprocess.run([sys.executable, "-I", "-B", "-c", SONDE_BAC_A_SABLE, str(ORCHESTRATEUR)],
                           cwd=str(ORCHESTRATEUR), env=env, capture_output=True, text=True, timeout=120)
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


def _depot_git() -> dict:
    try:
        return {"commit": _git(DEPOT, "rev-parse", "HEAD").strip(),
                "arbre_modifie": bool(_git(DEPOT, "status", "--porcelain", "--untracked-files=no").strip())}
    except Refus as e:
        return {"commit": None, "erreur": str(e)}


def executer() -> int:
    env_lu = dict(os.environ)
    aujourd_hui = _dt.datetime.now(_dt.timezone.utc).date()

    go = verifier_go(DEPOT / "registres" / "go.md", aujourd_hui)
    orch = verifier_orchestrateur()
    env_arg = verifier_enveloppe()
    course = verifier_sortie_course()
    att = verifier_attestation()

    horodatage = date_u()
    ident = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%d-%H%M%S") + SUFFIXE_RUN
    dossier_run = DEPOT / "runs" / ident
    dossier_sortie = DOSSIER_SORTIES / ident

    argv = commande_bras(horodatage)
    garde_drapeaux(argv)
    garde_modeles_claude(argv)

    env, retires, exclus = environnement_filtre(env_lu)
    bac = sonder_bac_a_sable(env)

    if dossier_run.exists() or dossier_sortie.exists():
        raise Refus(f"{dossier_run} ou {dossier_sortie} existe déjà (R12)")
    dossier_run.mkdir(parents=True)
    dossier_sortie.mkdir(parents=True)

    depart = {
        "lanceur": {"version": VERSION, "chemin": str(Path(__file__).resolve()), "sha256": sha256_fichier(Path(__file__))},
        "horodatage_canonique": horodatage, "id": ident, "go": go,
        "orchestrateur": orch, "enveloppe_argon": env_arg,
        "course": {"sortie": str(SORTIE_COURSE), **course},
        "attestation": att,
        "budgets": {
            "cumul_collisionneur_usd": CUMUL_COLLISIONNEUR_USD,
            "budget_externe_total_course_usd": BUDGET_EXTERNE_TOTAL_COURSE_USD,
            "cout_externe_course_usd": COUT_EXTERNE_COURSE_USD,
            "budget_externe_bras_usd": BUDGET_EXTERNE_BRAS_USD,
            "plafond_juge_usd": PLAFOND_JUGE_USD,
        },
        "commande": argv, "cwd": str(ORCHESTRATEUR), "bac_a_sable": bac,
        "cles": {"noms_retires": retires, "valeurs": "jamais lues"},
        "depot_travail": _depot_git(),
        "journaux": {"stdout": str(dossier_sortie / "bras.stdout.txt"), "stderr": str(dossier_sortie / "bras.stderr.txt")},
    }
    h_depart = ecrire_scelle(dossier_run / "manifeste-lanceur-depart.json", depart)
    print(json.dumps({"manifeste_depart": str(dossier_run / "manifeste-lanceur-depart.json"), "sha256": h_depart},
                     ensure_ascii=False), flush=True)

    code = None
    pid = None
    try:
        debut = _dt.datetime.now(_dt.timezone.utc)
        with open(dossier_sortie / "bras.stdout.txt", "xb") as fo, \
             open(dossier_sortie / "bras.stderr.txt", "xb") as fe:
            enfant = subprocess.Popen(argv, cwd=str(ORCHESTRATEUR), env=env, stdout=fo, stderr=fe)
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
                 "debut_utc": debut.isoformat(), "fin_utc": fin.isoformat()}
        try:
            ecrire_scelle(dossier_run / "manifeste-lanceur-fin.json", bilan)
        except Exception:
            pass
        raise
    fin = _dt.datetime.now(_dt.timezone.utc)
    bilan = {"id": ident, "manifeste_depart_sha256": h_depart, "pid_orchestrateur": pid, "code": code,
             "debut_utc": debut.isoformat(), "fin_utc": fin.isoformat(),
             "journaux_sha256": {n: sha256_fichier(dossier_sortie / n)
                                 for n in ("bras.stdout.txt", "bras.stderr.txt")}}
    h_fin = ecrire_scelle(dossier_run / "manifeste-lanceur-fin.json", bilan)
    print(json.dumps({"manifeste_fin": str(dossier_run / "manifeste-lanceur-fin.json"), "sha256": h_fin, "code": code},
                     ensure_ascii=False), flush=True)
    return code


def principal(argv: list | None = None) -> int:
    argv = sys.argv[1:] if argv is None else list(argv)
    if argv:
        print(json.dumps({"refus": f"aucun argument admis (reçu {argv!r})"},
                         ensure_ascii=False), file=sys.stderr)
        return 2
    try:
        return executer()
    except Refus as e:
        print(json.dumps({"refus": str(e)}, ensure_ascii=False), file=sys.stderr)
        return 2
    except Exception as e:
        print(json.dumps({"erreur": f"{type(e).__name__}: {e}"}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(principal())
