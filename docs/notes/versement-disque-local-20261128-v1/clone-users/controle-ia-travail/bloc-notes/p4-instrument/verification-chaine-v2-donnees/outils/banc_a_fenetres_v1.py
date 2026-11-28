"""Banc A de la vérification « données et fuites » de la chaîne v2 de P4 (vérificateur neuf), v1.

Éprouve, sans rien modifier, le module commun de la chaîne v2 (`verifications_p4_v1.py`, sous-commandes `fenetres`,
`montrer`, `jetons`) sur des fuites déguisées fabriquées ici, à partir de textes synthétiques seulement (ceux de
`outils_essais_p4_v1.py fenetres` et quatre textes écrits ici) : aucun texte de P3 n'est lu.

Chaque cas a un attendu écrit avant le jeu :
  - « garde » : la chaîne doit retrouver la fuite (code 1 pour fenetres/jetons ; ligne retirée ou masquée pour montrer) ;
  - « limite » : fuite hors de ce que la décision de la session demande (forme non couverte, fragment trop court) ;
    l'attendu est « non retrouvée » et le cas documente la limite (aucune correction exigée par la décision) ;
  - « sain » : rien à retrouver (code 0).
Verdict par cas : CONFORME si le résultat égale l'attendu ; ÉCART sinon (un écart sur un cas « garde » ou « sain » est
un défaut de la chaîne ; un écart sur un cas « limite » veut dire que la chaîne fait mieux que prévu).

Usage : banc_a_fenetres_v1.py VERIF OUTILS RACINE_NEUVE
"""
from __future__ import annotations

import base64
import gzip
import hashlib
import html
import json
import os
import subprocess
import sys
import textwrap
import unicodedata
import urllib.parse
from pathlib import Path

import numpy as np

VERIF, OUTILS, RACINE = sys.argv[1], sys.argv[2], Path(sys.argv[3])
PY = sys.executable
if RACINE.exists():
    raise SystemExit(f"{RACINE} existe déjà (R12)")
RACINE.mkdir(parents=True)

JT, JG = "factice-hf-verif-0001", "factice-gh-verif-0001"     # jetons factices
ENV = {"PATH": "/usr/bin:/bin", "LANG": "C.UTF-8", "HOME": str(RACINE), "PYTHONDONTWRITEBYTECODE": "1",
       "HF_TOKEN": JT, "CONTROLE_IA_GITHUB_TOKEN": JG, "GH_TOKEN": JG}

# --- textes synthétiques ---------------------------------------------------------------------------------------------
TO = RACINE / "textes-outils.jsonl"
r = subprocess.run([PY, "-B", OUTILS, "fenetres", str(TO)], capture_output=True, text=True, env=ENV)
assert r.returncode == 0, r.stderr
T = [json.loads(x)["texte"] for x in TO.read_text(encoding="utf-8").splitlines()
     if json.loads(x)["condition"] == "honnete" and len(set(json.loads(x)["texte"])) > 1]
NBSP, NNBSP = " ", " "
MES = [
    # V0 : lignes toutes courtes (moins de 48 caractères), texte total long
    "ACTION: ADD\nTITLE: Verify ocelot gamma probe\nPROPOSAL: Run the ocelot probe\non layer nine of the agent\n"
    "with the tapir floor kept frozen\nand twelve held-out tasks\nCOST: 9\nPREDICTION: gain",
    # V1 : français typographié (insécables, apostrophes courbes, points de suspension)
    f"ACTION: EDIT\nTITLE: Sonde «{NBSP}ocelot{NBSP}» révisée\nPROPOSAL{NNBSP}: Remplacer l’ancienne sonde du tapir par une "
    f"sonde étalonnée sur douze tâches… puis comparer au plancher gelé du lamantin, sans toucher au jeu tenu à l’écart.\n"
    f"COST{NNBSP}: 6",
    # V2 : un long paragraphe ASCII
    "ACTION: ADD\nTITLE: Ocelot sweep\nPROPOSAL: Sweep the ocelot probe over every layer of the agent, keep the tapir "
    "floor frozen, compare against the manatee baseline on twelve held-out tasks, and report the area under the curve "
    "with its bootstrap interval.\nCOST: 11\nPREDICTION: neutral",
    # V3 : tabulations et espaces doubles
    "ACTION: DROP\nTITLE: Ocelot\tablation  twice\nPROPOSAL: Remove  the duplicated\tocelot ablation, which repeats the "
    "tapir sweep  on every synthetic task and doubles the cost of the manatee floor.\nCOST: 4",
]
TM = RACINE / "textes-verif.jsonl"
TM.write_text("".join(json.dumps({"episode": f"honnete/v{k}/e0", "condition": "honnete", "tache": f"v{k}", "pas": 0,
                                  "texte": x}, ensure_ascii=False) + "\n" for k, x in enumerate(MES)), encoding="utf-8")
MOTS = ("zanzibar", "quokka", "marmoset", "axolotl", "pangolin", "ocelot", "tapir", "manatee", "lamantin")

lignes_journal: list[str] = []
non_conformes = 0


def ecrire(ligne: str) -> None:
    print(ligne, flush=True)
    lignes_journal.append(ligne)


def verif(args, entree=None, env=None):
    return subprocess.run([PY, "-B", VERIF, *args], input=entree, capture_output=True, text=True, env=env or ENV)


def affiche_texte(sortie: str) -> bool:
    return any(m in sortie.lower() for m in MOTS)


def cas_fenetres(nom: str, genre: str, attendu: int, textes: Path, fabriquer) -> None:
    """genre : garde, limite ou sain ; attendu : code attendu de `fenetres` (1 retrouvée, 0 non)."""
    global non_conformes
    d = RACINE / "cas" / nom
    d.mkdir(parents=True)
    fabriquer(d)
    r = verif(["fenetres", str(textes), str(d)])
    derniere = (r.stdout.strip().splitlines() or [""])[-1]
    premiere = (r.stdout.strip().splitlines() or [""])[0]
    if genre == "limite":       # hors de la décision : résultat documenté, sans verdict
        v = "RETROUVÉE" if r.returncode == 1 else ("NON RETROUVÉE" if r.returncode == 0 else f"code {r.returncode}")
        v = f"limite documentée : {v}"
    else:
        v = "CONFORME" if r.returncode == attendu else "ÉCART"
    if affiche_texte(r.stdout + r.stderr):
        v = "ÉCART (texte affiché)"
    if not v.startswith(("CONFORME", "limite")):
        non_conformes += 1
    ecrire(f"{nom} [{genre}] : code {r.returncode}" + ("" if genre == "limite" else f" (attendu {attendu})") + f" ; {v}")
    ecrire(f"    | {premiere[:200]}")
    ecrire(f"    | {derniere[:200]}")


def fichier(nom: str, contenu, mode="t"):
    def f(d: Path):
        p = d / nom
        p.parent.mkdir(parents=True, exist_ok=True)
        if mode == "t":
            p.write_text(contenu, encoding="utf-8")
        else:
            p.write_bytes(contenu)
    return f


def plusieurs(*fs):
    def f(d: Path):
        for x in fs:
            x(d)
    return f


def fragment(t: str, debut: int, n: int) -> str:
    return t[debut:debut + n]


# --- 1. fenetres : formes couvertes par la décision (garde) ----------------------------------------------------------
ecrire(f"script éprouvé : verifications_p4_v1.py {hashlib.sha256(Path(VERIF).read_bytes()).hexdigest()}")
ecrire(f"outil des textes : outils_essais_p4_v1.py {hashlib.sha256(Path(OUTILS).read_bytes()).hexdigest()}")
ecrire(f"textes synthétiques : outils {len(T)} honnêtes ({TO.name}) ; vérification {len(MES)} honnêtes ({TM.name})")
cas_fenetres("A00-dossier-sain", "sain", 0, TO, fichier("journal.txt", "AMORCE 2026-10-20T20:00:00Z : fin, code 0\n" + "." * 200 + "\n"))
cas_fenetres("A01-texte-brut", "garde", 1, TO, fichier("run.err", T[0] + "\n"))
cas_fenetres("A02-json-double", "garde", 1, TO, fichier("run.err", json.dumps(json.dumps(T[3])) + "\n"))
cas_fenetres("A03-json-triple", "limite", 0, TO, fichier("run.err", json.dumps(json.dumps(json.dumps(T[4], ensure_ascii=True))) + "\n"))
cas_fenetres("A04-repr-d-octets", "garde", 1, TO, fichier("run.err", repr(T[4].encode("utf-8")) + "\n"))
cas_fenetres("A05-json-barres-echappees", "garde", 1, TM,
             fichier("resultat.json", json.dumps({"note": MES[2]}).replace("/", "\\/").replace(" ", "\\u0020")))
cas_fenetres("A06-fragment-de-63-au-pire-alignement", "garde", 1, TM, fichier("run.err", "x " + fragment(MES[2], 1, 63) + " y\n"))
cas_fenetres("A07-cle-json", "garde", 1, TO, fichier("resume.json", json.dumps({T[1]: 1})))
cas_fenetres("A08-crlf", "garde", 1, TM, fichier("run.err", MES[2].replace("\n", "\r\n") + "\r\n"))
cas_fenetres("A09-html-echappe", "garde", 1, TO, fichier("page.html", html.escape(T[4])))
cas_fenetres("A10-espaces-normalisees", "garde", 1, TM, fichier("run.err", " ".join(MES[2].split()) + "\n"))
cas_fenetres("A11-octets-invalides-autour", "garde", 1, TO, fichier("run.err", b"\xff\xfe" + T[2].encode() + b"\xc3\n", "b"))
cas_fenetres("A12-npz-compresse", "garde", 1, TO,
             lambda d: np.savez_compressed(d / "x.npz", noms=np.array(["a", T[1]])))
cas_fenetres("A13-npz-octets-S", "garde", 1, TO,
             lambda d: np.savez(d / "x.npz", noms=np.array([T[0].encode("utf-8")])))

# --- 2. fenetres : formes hors de la décision (limite) ---------------------------------------------------------------
cas_fenetres("A20-fragment-de-62-au-pire-alignement", "limite", 0, TM, fichier("run.err", "x " + fragment(MES[2], 1, 62) + " y\n"))
cas_fenetres("A21-decoupe-en-morceaux-de-40", "limite", 0, TO,
             fichier("run.err", "\n".join(T[2][i:i + 40] for i in range(0, len(T[2]), 40)) + "\n"))
cas_fenetres("A22-replie-a-60-colonnes", "limite", 0, TM, fichier("run.err", textwrap.fill(" ".join(MES[2].split()), 60) + "\n"))
cas_fenetres("A23-base64", "limite", 0, TO, fichier("run.err", base64.b64encode(T[0].encode()).decode() + "\n"))
cas_fenetres("A24-base64-courte-d-un-fragment-de-60", "limite", 0, TM,
             fichier("run.err", "jeton=" + base64.b64encode(fragment(MES[2], 30, 60).encode()).decode() + "\n"))
cas_fenetres("A25-hexadecimal", "limite", 0, TO, fichier("run.err", T[1].encode().hex() + "\n"))
cas_fenetres("A26-url-encode", "limite", 0, TM, fichier("run.err", urllib.parse.quote(MES[2]) + "\n"))
cas_fenetres("A27-nfd", "limite", 0, TO, fichier("run.err", unicodedata.normalize("NFD", T[4]) + "\n"))
cas_fenetres("A28-nfkc-insecables", "limite", 0, TM, fichier("run.err", unicodedata.normalize("NFKC", MES[1]) + "\n"))
cas_fenetres("A29-majuscules", "limite", 0, TO, fichier("run.err", T[0].upper() + "\n"))
cas_fenetres("A30-espaces-de-largeur-nulle", "limite", 0, TM,
             fichier("run.err", "​".join(MES[2][i:i + 30] for i in range(0, len(MES[2]), 30)) + "\n"))
cas_fenetres("A31-utf16", "limite", 0, TO, fichier("run.err", T[0].encode("utf-16"), "b"))
cas_fenetres("A32-gzip", "limite", 0, TO, fichier("run.err.gz", gzip.compress(T[0].encode()), "b"))
cas_fenetres("A33-npy-seul", "limite", 0, TO, lambda d: np.save(d / "x.npy", np.array([T[0]])))
cas_fenetres("A34-npz-tableau-structure", "limite", 0, TO,
             lambda d: np.savez(d / "x.npz", t=np.array([(1, T[0])], dtype=[("k", "i4"), ("s", "U400")])))
cas_fenetres("A35-npz-texte-apres-l-archive", "limite", 0, TO,
             lambda d: (np.savez(d / "x.npz", x=np.zeros(2)), open(d / "x.npz", "ab").write(T[0].encode())))
cas_fenetres("A36-texte-dans-un-nom-de-fichier", "limite", 0, TO,
             fichier(fragment(T[2], 0, 120).replace("\n", " ").replace("/", " ") + ".txt", "rien\n"))
cas_fenetres("A37-jetons-bpe", "limite", 0, TM,
             fichier("run.err", MES[2].replace(" ", "Ġ").replace("\n", "Ċ") + "\n"))


def lien(d: Path) -> None:
    hors = RACINE / "hors-du-dossier"
    hors.mkdir(exist_ok=True)
    (hors / f"cible-{d.name}.txt").write_text(T[0] + "\n", encoding="utf-8")
    (d / "journal-lien.txt").symlink_to(hors / f"cible-{d.name}.txt")


def lien_dossier(d: Path) -> None:
    hors = RACINE / f"hors-dossier-{d.name}"
    hors.mkdir()
    (hors / "run.err").write_text(T[1] + "\n", encoding="utf-8")
    (d / "sous-dossier-lien").symlink_to(hors, target_is_directory=True)


cas_fenetres("A38-lien-symbolique-vers-un-fichier", "limite", 0, TO, lien)
cas_fenetres("A39-lien-symbolique-vers-un-dossier", "limite", 0, TO, lien_dossier)

# --- 3. montrer : filtre de l'affichage --------------------------------------------------------------------------------
ecrire("--- montrer (filtre de l'affichage, largeur 400)")


def cas_montrer(nom: str, genre: str, entree: str, attendu, textes: Path = TO, env=None) -> None:
    """attendu : fonction (sortie) -> bool."""
    global non_conformes
    r = subprocess.run([PY, "-B", VERIF, "montrer", str(textes), "400"], input=entree.encode("utf-8", "surrogateescape"),
                       capture_output=True, env=env or ENV)
    r = subprocess.CompletedProcess(r.args, r.returncode, r.stdout.decode("utf-8", "replace"), r.stderr.decode("utf-8", "replace"))
    ok = attendu(r.stdout)
    if genre == "limite":
        v = "limite documentée : " + ("RETIRÉ OU MASQUÉ" if ok else "AFFICHÉ")
    else:
        v = "CONFORME" if ok else "ÉCART"
        if not ok:
            non_conformes += 1
    # la sortie n'est jamais recopiée : longueur et empreinte seulement
    ecrire(f"{nom} [{genre}] : code {r.returncode} ; sortie {len(r.stdout)} caractères "
           f"({hashlib.sha256(r.stdout.encode()).hexdigest()[:12]}) ; {r.stdout.count('ligne retirée')} ligne(s) retirée(s) ; {v}")


sans_fuite = lambda s: not affiche_texte(s) and JT not in s and JG not in s
cas_montrer("W10-ligne-de-10000-caracteres-fenetre-au-bout", "garde", "KO  4f " + "x" * 10000 + T[0].replace("\n", " ") + "\n", sans_fuite)
cas_montrer("W11-jeton-puis-fenetre-au-dela-de-400", "garde", "--  4a arrêt : " + JT + " " + "y" * 500 + json.dumps(T[2]) + "\n", sans_fuite)
cas_montrer("W12-fenetre-en-uxxxx", "garde", "--  4a arrêt : " + json.dumps(T[4], ensure_ascii=True) + "\n", sans_fuite)
cas_montrer("W13-retour-chariot", "garde", "OK  1a sain\r" + T[2].replace("\n", " ") + "\n", sans_fuite)
cas_montrer("W14-octets-invalides", "garde", "--  arrêt \udcff" + T[1].replace("\n", " ") + "\n", sans_fuite)
cas_montrer("W15-jeton-a-cheval-sur-400", "garde", "--  " + "z" * 390 + JG + "\n", lambda s: JG not in s and JG[:6] not in s)
cas_montrer("W20-texte-a-lignes-courtes-affiche-brut", "limite", MES[0] + "\n", sans_fuite, TM)
cas_montrer("W21-jeton-coupe-sur-deux-lignes", "limite", "dernière : " + JG[:10] + "\n" + JG[10:] + "\n",
            lambda s: JG[:10] not in s and JG[10:] not in s)
cas_montrer("W22-jeton-en-base64", "limite", "auth " + base64.b64encode(f"x-access-token:{JG}".encode()).decode() + "\n",
            lambda s: base64.b64encode(f"x-access-token:{JG}".encode()).decode() not in s)
cas_montrer("W23-fenetre-nfd", "limite", "--  4a arrêt : " + unicodedata.normalize("NFD", T[4]).replace("\n", " ") + "\n", sans_fuite)

# --- 4. jetons ---------------------------------------------------------------------------------------------------------
ecrire("--- jetons (valeurs des jetons de l'environnement)")


def cas_jetons(nom: str, genre: str, attendu: int, fabriquer) -> None:
    global non_conformes
    d = RACINE / "jetons" / nom
    d.mkdir(parents=True)
    fabriquer(d)
    r = verif(["jetons", str(d)])
    if genre == "limite":
        v = "limite documentée : " + ("RETROUVÉ" if r.returncode == 1 else "NON RETROUVÉ" if r.returncode == 0 else f"code {r.returncode}")
    else:
        v = "CONFORME" if r.returncode == attendu else "ÉCART"
    if JT in r.stdout + r.stderr or JG in r.stdout + r.stderr:
        v = "ÉCART (jeton affiché)"
    if not v.startswith(("CONFORME", "limite")):
        non_conformes += 1
    ecrire(f"{nom} [{genre}] : code {r.returncode}" + ("" if genre == "limite" else f" (attendu {attendu})") + f" ; {v}")
    ecrire(f"    | {(r.stdout.strip().splitlines() or [''])[-1][:200]}")


cas_jetons("J00-sain", "sain", 0, fichier("etats.txt", "actual_status=running\n"))
cas_jetons("J01-jeton-brut", "garde", 1, fichier("etats.txt", f"illisible : {JT}\n"))
cas_jetons("J02-jeton-dans-un-json-echappe", "garde", 1, fichier("etat.json", json.dumps({"env": [["HF_TOKEN", JT]]})))
cas_jetons("J10-jeton-coupe-sur-deux-lignes", "limite", 0, fichier("journal.txt", f"{JG[:10]}\n{JG[10:]}\n"))
cas_jetons("J11-jeton-en-base64", "limite", 0, fichier("journal.txt", base64.b64encode(f"x-access-token:{JG}".encode()).decode() + "\n"))
cas_jetons("J12-jeton-en-utf16", "limite", 0, fichier("journal.txt", f"{JT}\n".encode("utf-16"), "b"))


def lien_jeton(d: Path) -> None:
    hors = RACINE / "hors-jetons"
    hors.mkdir(exist_ok=True)
    (hors / "cible.txt").write_text(JT + "\n", encoding="utf-8")
    (d / "lien.txt").symlink_to(hors / "cible.txt")


cas_jetons("J13-jeton-derriere-un-lien-symbolique", "limite", 0, lien_jeton)

ecrire(f"FIN DU BANC A ; écarts sur les cas garde ou sain : {non_conformes}")
(RACINE / "banc-a.log").write_text("\n".join(lignes_journal) + "\n", encoding="utf-8")
sys.exit(1 if non_conformes else 0)
