"""Conditions de lancement de l'audit des fuites de T0.7 (consigne scellée 43102e80…, § 4 ; R-2355, R-2359, R-2605) — v1.

Noms, empreintes et lignes de registre seulement : aucun fichier de données de 7a, 7b ou T0.7 n'est ouvert ; un fichier de
7b présent est seulement haché ; aucun dossier `diag/` ou `runs/` n'est listé. Lancer depuis n'importe où :
    python3 -I verifier_conditions_audit_fuites_t07_v1.py /home/user/controle-ia-travail [--commit C] [--racine-7b P]
--commit C (facultatif, 40 caractères) : le champ `commit` du manifeste de 7b, lu par la mère après rapatriement ; sans lui,
les contrôles C8, C10 et C11 portent sur le commit probable (base de la branche de 7b).
--racine-7b P (facultatif ; défaut /root/bac-audit-fuites-t07-v1/racine-7b) : racine hors du dépôt où la mère rapatrie les
entrées de 7b (C12) ; les mêmes chemins dans l'arbre du dépôt doivent rester absents (C12 bis).
Sortie : une ligne par contrôle, « OK », « KO » ou « À FAIRE » ; code 0 si aucun KO, 1 sinon.
"""
from __future__ import annotations

import hashlib
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

CONSIGNE = "prereg/T0.7-consigne-audit-fuites-v1.md"
SHA_CONSIGNE = "43102e80332cd138305604b7cffb2dc77a1584a7ad0b48584c7506ea377b3a5d"
T07 = "prereg/T0.7-sondes-v0-v1.md"
SHA_T07 = "d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5"
CELLULES_T07 = {"AUDIT-FUITES-T07": "381a72d5b52c1534d116c81b71568dd4728d1a4d90a22a25e99109508e30fede",
                "CONSIGNE-AUDIT-FUITES-T07": "95c8b659c54f218a903e1d0359a5a4a9ca9bd2e81072741803861a4bb4fa1121"}
REGISTRE = "registres/scellements-v1.md"
RUN_7A = "20261109-070232-t06-reel"
RUN_7B_ATTENDU = "20261111-151701-t06-reel"          # R-2413
SHA_MANIFESTE_7B = "7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6"   # R-2413, ligne RUN-CONFIRMATION-T06
BRANCHE_7B, TETE_7B = "calcul/t06-confirmation-7b-v1", "55c3e3eb89a4650419f35999aaa4c54288275b0d"   # R-2413
DECOUPEUR = "c7484c43657a2ce22d76af33efd06aaa11a6aafa"
DOSSIER_DECOUPEUR = "donnees/decoupeur-llama-3.1-8b-instruct-0e9e39f2-v1"
FICHIERS_DECOUPEUR = {"tokenizer.json": "79e3e522635f3171300913bb421464a87de6222182a0570b9b2ccba2a964b2b4",
                      "tokenizer_config.json": "177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424",
                      "special_tokens_map.json": "6f38c73729248f6c127296386e3cdde96e254636cc58b4169d3fd32328d9a8ec"}
C_STAT = "7a54d431d89745839220f882b41b13e8c62ecfdd"
SHA_STAT = "a85525752fbdaa2fcee874d084eb11a671adadf1302340a3d71a5e09f0b11e2a"
C_CHAINE = "1609a4bf2c1572f72bb8542d81d963ac6a8481c4"
C_MANIFESTE_PROBABLE = "935262b17ca95894a882b02f1526ee39d1738652"   # base de la branche de 7b ; à confirmer par le champ commit
EMPREINTES_7B = {"manifeste.json": "7e1ac1f02584e4f8babf664e78d12f3122bfdca18292734f28281e9459479bf6",
                 "episodes-t06.json": "c7911933a6cc797db4be094bd252393bb4360cdc55a25867b624be721ccdb51c",
                 "textes-actions-t06.jsonl": "d196bb4fffd793dc52190aa2674aeff33619f17bd40d303f564515bde2ad783d",
                 "mesures-t06.npz": "aca5afd068a8749952c7424a7708a1e4c8b78c082fba495d5d406f2605435049"}   # compagnons à la tête 55c3e3eb
COMPARATEUR = ("refs/remotes/origin/lot/compte-4-v1",
               "brouillons/audit-fuites-t07-preparation-compte4-v1/comparer-versions-7b-venv-v1.py",
               "30e0212016ba694a6cbde1b6e77d7ee8ea95ff413379d90cd70ff6df6814a618")
SHA_P3 = "a68468fef6286bbcaa31451ba461d0adab2af7d529dd5e4fa0695643e6d1d69c"
QUATRE = ["src/controle_ia/environnements/propositions.py", "src/controle_ia/premier_test_ia/conditions.py",
          "src/controle_ia/t06/test_croise.py", "src/controle_ia/t06/cout.py"]
SOURCES = ["prereg/P3-consignes-v1.md", *QUATRE[:3], "src/controle_ia/t06/lanceur.py", "src/controle_ia/t06/lanceur_v6.py",
           "src/controle_ia/t06/cout.py", "src/controle_ia/harnais/episode.py", "src/controle_ia/harnais/modeles.py",
           "docs/sources/invites-2606.08892-v1/index.json", "docs/sources/invites-2606.08892-v1/invites/H1-classification.txt"]
ENTREES_7B = [f"runs/{RUN_7B_ATTENDU}/manifeste.json", f"diag/{RUN_7B_ATTENDU}/episodes-t06.json",
              f"donnees/{RUN_7B_ATTENDU}/textes-actions-t06.jsonl", f"donnees/{RUN_7B_ATTENDU}/mesures-t06.npz"]
DOSSIER_AUDITEUR = "docs/notes/g0-deux-semaines-v1/audit-fuites-t07-v1"
SORTIES_AUDITEUR = ["audit_fuites_t07_v1.py", "candidats-v1.jsonl", "essais-r5-v1.txt", "table-candidats-v1.jsonl",
                    "audit-fuites-t07.json", "rapport-audit-fuites-t07-v1.md", "journal-audit-v1.md", "rapport-arret-v1.md",
                    "contre-lecture-audit-fuites-t07-v1.md"]
BACS = ["/root/bac-audit-fuites-t07-v1/auditeur", "/root/bac-audit-fuites-t07-v1/contre-lecteur"]

import argparse
_a = argparse.ArgumentParser()
_a.add_argument("depot", nargs="?", default=str(Path.cwd()))
_a.add_argument("--commit", default=None)
_a.add_argument("--racine-7b", dest="racine_7b", default="/root/bac-audit-fuites-t07-v1/racine-7b")
ARGS = _a.parse_args()
R = Path(ARGS.depot)
RACINE_7B = Path(ARGS.racine_7b)
if ARGS.commit is not None:
    if not re.fullmatch(r"[0-9a-f]{40}", ARGS.commit):
        sys.exit("--commit : 40 caractères hexadécimaux attendus")
    C_MANIFESTE_PROBABLE = ARGS.commit
NOM_C = "commit du manifeste (donné en argument)" if ARGS.commit else "commit probable du manifeste (base de la branche de 7b)"
comptes = {"OK": 0, "KO": 0, "À FAIRE": 0}


def dire(etat: str, texte: str) -> None:
    comptes[etat] += 1
    print(f"{etat:8} {texte}")


def sha_fichier(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def git(*args: str, binaire: bool = False):
    r = subprocess.run(["git", "-C", str(R), *args], capture_output=True)
    return r.returncode, (r.stdout if binaire else r.stdout.decode("utf-8", "replace").strip())


def sha_git(commit: str, chemin: str) -> str | None:
    code, out = git("show", f"{commit}:{chemin}", binaire=True)
    return hashlib.sha256(out).hexdigest() if code == 0 else None


def present(commit: str) -> bool:
    return git("cat-file", "-e", f"{commit}^{{commit}}")[0] == 0


def ligne(cle: str) -> list[tuple[int, list[str]]]:
    """Lecture prescrite (§ 4) : ligne qui commence par « | CLÉ | », sans accent grave ; cellules entre « | »."""
    out = []
    for n, l in enumerate((R / REGISTRE).read_text(encoding="utf-8").splitlines(), 1):
        if l.startswith(f"| {cle} | "):
            out.append((n, [c.strip() for c in l.strip().strip("|").split("|")]))
    return out


print(f"# relevé {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')} ; HEAD {git('rev-parse', 'HEAD')[1]} ; "
      f"registre {sha_fichier(R / REGISTRE)[:16]}…")

# C1 — consigne scellée, sans marqueur
p = R / CONSIGNE
comp = (R / (CONSIGNE + ".sha256")).read_text(encoding="utf-8").split()[0]
s = sha_fichier(p)
dire("OK" if s == SHA_CONSIGNE == comp else "KO", f"C1 consigne {CONSIGNE} : sha256 {s[:12]}… compagnon {comp[:12]}… attendu {SHA_CONSIGNE[:12]}…")
n = len(re.findall(r"<<[A-Z0-9_]+>>", p.read_text(encoding="utf-8")))
dire("OK" if n == 0 else "KO", f"C1 marqueurs « <<NOM>> » restants dans la consigne : {n}")

# C2 — ligne CONSIGNE-AUDIT-FUITES-T07
L = ligne("CONSIGNE-AUDIT-FUITES-T07")
bon = len(L) == 1 and len(L[0][1]) == 4 and L[0][1][2] == CONSIGNE and L[0][1][3] == SHA_CONSIGNE
dire("OK" if bon else "KO", f"C2 ligne CONSIGNE-AUDIT-FUITES-T07 : {len(L)} fois" + (f", l. {L[0][0]}, {len(L[0][1])} cellules, {L[0][1][1]}, chemin et sha256 égaux à la consigne : {bon}" if L else ""))
t_consigne = L[0][1][1] if L else ""

# C3 — ligne RUN-CONFIRMATION-T06, contrôlée sur la ligne seule
L = ligne("RUN-CONFIRMATION-T06")
if len(L) == 1 and len(L[0][1]) == 4:
    m = re.fullmatch(r"runs/([^/]+)/manifeste\.json", L[0][1][2])
    run = m.group(1) if m else None
    bon = bool(m) and run != RUN_7A and run == RUN_7B_ATTENDU and L[0][1][3] == SHA_MANIFESTE_7B
    dire("OK" if bon else "KO", f"C3 ligne RUN-CONFIRMATION-T06 : 1 fois, l. {L[0][0]}, forme runs/<RUN_7B>/manifeste.json : {bool(m)} ; "
         f"RUN_7B = {run} (≠ 7a : {run != RUN_7A}) ; sha256 de la ligne = R-2413 : {L[0][1][3] == SHA_MANIFESTE_7B}")
else:
    dire("KO", f"C3 ligne RUN-CONFIRMATION-T06 : {len(L)} fois")

# C4 — ligne CODE-T07 et criteres_v1.py
L = ligne("CODE-T07")
if len(L) == 1 and len(L[0][1]) == 4:
    f = R / L[0][1][2]
    s = sha_fichier(f) if f.is_file() else None
    compf = (f.with_name(f.name + ".sha256")).read_text(encoding="utf-8").split()[0] if f.with_name(f.name + ".sha256").is_file() else None
    import json
    d = json.loads(f.read_text(encoding="utf-8")) if s else {}
    c7 = d.get("commit")
    e = d.get("fichiers", {}).get("src/controle_ia/t07/criteres_v1.py")
    arbre = sha_fichier(R / "src/controle_ia/t07/criteres_v1.py")
    aucommit = sha_git(c7, "src/controle_ia/t07/criteres_v1.py") if c7 else None
    bon = s == L[0][1][3] == compf and c7 is not None and present(c7) and arbre == aucommit == e
    dire("OK" if bon else "KO", f"C4 ligne CODE-T07 : {L[0][1][2]} ({str(s)[:12]}…, = ligne et compagnon : {s == L[0][1][3] == compf}) ; "
         f"commit {c7} présent : {present(c7) if c7 else None} ; criteres_v1.py arbre = commit = entrée « fichiers » : {arbre == aucommit == e} ({arbre[:12]}…)")
else:
    dire("KO", f"C4 ligne CODE-T07 : {len(L)} fois (la consigne la rend facultative ; le contrôle de criteres_v1.py prendrait alors 8ae9fc44)")

# C5 — aucune ligne AUDIT-FUITES-T07 (préalable 4, R12)
L = ligne("AUDIT-FUITES-T07")
dire("OK" if not L else "KO", f"C5 ligne AUDIT-FUITES-T07 : {len(L)} fois (0 exigé)")

# C6 — fenêtre : après la poussée vérifiée de 7b, avant l'étape B ; CLAF-18 contre P3-bis
L = ligne("VERDICT-P3BIS")
v = L[0][1][1] if len(L) == 1 else None
dire("OK" if v and v > t_consigne else "À FAIRE", f"C6 ligne VERDICT-P3BIS : {len(L)} fois ({v}) — verdict de P3-bis scellé avant le lancement : "
     f"CLAF-18 (ouverture des textes de 7b avant ce verdict) sans objet ; consigne scellée avant ce verdict ({t_consigne})")
L = ligne("ISSUE-MOTS-ET-COUT-T06")
dire("OK" if not L else "KO", f"C6 ligne ISSUE-MOTS-ET-COUT-T06 : {len(L)} fois — avec C5, l'étape B (qui exige les deux) n'a pas pu être jouée : fenêtre ouverte")
code, out = git("ls-remote", "origin", f"refs/heads/{BRANCHE_7B}")
tete = out.split()[0] if code == 0 and out else None
dire("OK" if tete == TETE_7B else ("À FAIRE" if tete is None else "KO"),
     f"C6 tête distante de {BRANCHE_7B} : {tete} (R-2413 : {TETE_7B[:12]}… ; poussée vérifiée, ligne RUN-CONFIRMATION-T06)")

# C7 — T0.7 scellé et cellules gelées
p = R / T07
s = sha_fichier(p)
comp = (R / (T07 + ".sha256")).read_text(encoding="utf-8").split()[0]
dire("OK" if s == SHA_T07 == comp else "KO", f"C7 T0.7 scellé : sha256 {s[:12]}…, = compagnon et R-2321 : {s == SHA_T07 == comp}")
lignes = p.read_text(encoding="utf-8").splitlines()
for cle, attendu in CELLULES_T07.items():
    trouvees = [l for l in lignes if l.startswith(f"| `{cle}` ")]
    cell = re.split(r"(?<!\\) \| ", trouvees[0].strip()[2:-2]) if len(trouvees) == 1 else []
    bon = len(cell) == 4 and hashlib.sha256(cell[1].encode("utf-8")).hexdigest() == attendu
    dire("OK" if bon else "KO", f"C7 ligne ``| `{cle}` `` de T0.7 : {len(trouvees)} fois ; deuxième cellule = repère de la consigne ({attendu[:12]}…) : {bon}")

# C8 — commits que le clone de l'auditeur doit contenir sans fetch (R-2605)
for nom, c in [("découpeur", DECOUPEUR), ("statistiques.py et sondes/evaluation.py", C_STAT), ("chaîne gelée de T0.6", C_CHAINE),
               (NOM_C, C_MANIFESTE_PROBABLE)]:
    dire("OK" if present(c) else "À FAIRE", f"C8 commit {c[:12]}… ({nom}) présent dans le clone : {present(c)}")
anc = git("merge-base", "--is-ancestor", C_MANIFESTE_PROBABLE, "HEAD")[0] == 0
dire("OK" if anc else "À FAIRE", f"C8 {C_MANIFESTE_PROBABLE[:12]}… ancêtre de HEAD : {anc} (à confirmer par le seul champ commit du manifeste, après rapatriement)")

# C9 — découpeur : trois empreintes au commit, égales à la consigne et aux compagnons du commit
for nom, attendu in FICHIERS_DECOUPEUR.items():
    s = sha_git(DECOUPEUR, f"{DOSSIER_DECOUPEUR}/{nom}")
    code, c = git("show", f"{DECOUPEUR}:{DOSSIER_DECOUPEUR}/{nom}.sha256")
    c = c.split()[0] if code == 0 and c else None
    dire("OK" if s == attendu == c else "KO", f"C9 découpeur {nom} : {str(s)[:12]}… = consigne § 6.1 et compagnon du commit : {s == attendu == c}")

# C10 — modules importés : arbre contre commit cité (§ 5.1, point 6)
for chemin in ["src/controle_ia/premier_test_ia/statistiques.py", "src/controle_ia/sondes/evaluation.py"]:
    a, b = sha_fichier(R / chemin), sha_git(C_STAT, chemin)
    extra = f" ; = {SHA_STAT[:12]}… (consigne) : {a == SHA_STAT}" if chemin.endswith("statistiques.py") else ""
    dire("OK" if a == b and (not extra or a == SHA_STAT) else "KO", f"C10 {chemin} : arbre = 7a54d431 : {a == b}{extra}")
for chemin in QUATRE + ["src/controle_ia/premier_test_ia/statistiques.py"]:
    a, b = sha_fichier(R / chemin), sha_git(C_MANIFESTE_PROBABLE, chemin)
    dire("OK" if a == b else "À FAIRE", f"C10 {chemin} : arbre = commit probable du manifeste : {a == b} (à refaire par l'auditeur contre le champ commit)")

# C11 — sources de construction au commit probable du manifeste ; P3-consignes = config de 7b scellée
for chemin in SOURCES:
    a, b = sha_git(C_MANIFESTE_PROBABLE, chemin), sha_git(C_CHAINE, chemin)
    dire("OK" if a is not None else "KO", f"C11 source {chemin} au commit probable : {'présente' if a else 'ABSENTE'} ; = 1609a4bf : {a == b}")
dire("OK" if sha_git(C_MANIFESTE_PROBABLE, "prereg/P3-consignes-v1.md") == SHA_P3 == sha_fichier(R / "prereg/P3-consignes-v1.md") else "KO",
     "C11 prereg/P3-consignes-v1.md = a68468fe… (consigne § 5.1 point 5 ; consignes_sha256 de la configuration scellée de 7b)")

# C12 — entrées de 7b dans la racine hors du dépôt (chemins exacts ; aucun dossier listé) ; C12 bis — absentes de l'arbre du dépôt
for chemin in ENTREES_7B:
    present_arbre = [g for g in (chemin, chemin + ".sha256") if (R / g).exists()]
    dire("OK" if not present_arbre else "KO", f"C12 bis {chemin} dans l'arbre du dépôt : {present_arbre or 'absent'} (attendu : absent ; racine hors du dépôt)")
for chemin in ENTREES_7B:
    f, c = RACINE_7B / chemin, RACINE_7B / (chemin + ".sha256")
    if f.is_file() and c.is_file():
        s = sha_fichier(f)
        bon = s == c.read_text(encoding="utf-8").split()[0] == EMPREINTES_7B[f.name] and (not chemin.endswith("manifeste.json") or s == SHA_MANIFESTE_7B)
        dire("OK" if bon else "KO", f"C12 {RACINE_7B}/{chemin} : présent ; = compagnon et = compagnon de la tête 55c3e3eb{' et = ligne' if chemin.endswith('manifeste.json') else ''} : {bon}")
    else:
        dire("À FAIRE", f"C12 {RACINE_7B}/{chemin} : absent (fichier {f.is_file()}, compagnon {c.is_file()}) : à rapatrier de {BRANCHE_7B}")

# C13 — interprète du dépôt : versions du chemin de décodage (R-2355 : transformers 5.18.0, tokenizers 0.23.2)
code = ("import sys, json; from importlib import metadata as m; "
        "print(json.dumps({'python': sys.version.split()[0], **{b: m.version(b) for b in ('numpy', 'transformers', 'tokenizers')}}))")
r = subprocess.run([str(R / ".venv/bin/python"), "-I", "-c", code], capture_output=True, text=True)
import json as _j
v = _j.loads(r.stdout) if r.returncode == 0 else {}
bon = v.get("transformers") == "5.18.0" and v.get("tokenizers") == "0.23.2"
dire("OK" if bon else "KO", f"C13 .venv : {v} (versions épinglées de R-2355 : {bon}) — comparaison au manifeste de 7b : après rapatriement (R-2359, condition 3)")

# C14 — dossier de l'auditeur neuf ; bacs à sable absents
d = R / DOSSIER_AUDITEUR
deja = [n for n in SORTIES_AUDITEUR if (d / n).exists()]
dire("OK" if not deja else "KO", f"C14 {DOSSIER_AUDITEUR}/ : sorties de l'audit déjà présentes : {deja or 'aucune'}")
for b in BACS:
    dire("OK" if not Path(b).exists() else "KO", f"C14 bac à sable {b} : {'absent' if not Path(b).exists() else 'EXISTE DÉJÀ'}")

# C15 — comparateur des versions du compte 4 (R-2359, condition 3) lisible dans le clone, à son empreinte
s = sha_git(COMPARATEUR[0], COMPARATEUR[1])
dire("OK" if s == COMPARATEUR[2] else "KO", f"C15 comparateur des versions ({COMPARATEUR[0]}:{COMPARATEUR[1].rsplit('/', 1)[1]}) : {str(s)[:12]}… = 30e02120… : {s == COMPARATEUR[2]}")

print(f"# bilan : {comptes['OK']} OK, {comptes['KO']} KO, {comptes['À FAIRE']} À FAIRE")
sys.exit(1 if comptes["KO"] else 0)
