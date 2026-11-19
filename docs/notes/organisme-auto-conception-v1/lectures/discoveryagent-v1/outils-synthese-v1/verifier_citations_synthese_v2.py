#!/usr/bin/env python3
"""Vérification par programme des citations de la synthèse DiscoveryAgent (v1).

Se lance avec `python3 -I`, depuis n'importe où, hors des dépôts des auteurs :
    python3 -I verifier_citations_synthese_v1.py RACINE_DU_DEPOT [--table] [--sortie=CHEMIN]

`--sortie=CHEMIN` écrit aussi dans ce fichier tout ce qui va à la sortie standard.

Pour chaque citation du registre `citations-synthese-v2.json` :
  - papier, annexe : l'extrait doit se trouver à la page citée du texte extrait
    (une page par saut de page) ;
  - code : l'extrait doit se trouver aux lignes citées du fichier, lu au commit
    donné par `git show` (rien n'est exécuté des dépôts des auteurs) ;
  - organisme, papierC : l'extrait doit se trouver dans la pièce, lue par
    `git show <branche>:<chemin>` ;
  - disque : l'extrait doit se trouver dans le fichier de l'arbre de travail ;
  - absence, absence_noms : la liste des fichiers où un motif apparaît (ou le
    compte des noms suivis) doit être celle attendue.
Puis : tout identifiant cité dans la note existe au registre ; tout
identifiant du registre est cité dans la note.

Comparaison après normalisation : forme Unicode NFKC (ligatures), guillemets et
apostrophes droits, espaces réduits, casse gardée ; pour nos pièces et le code,
les signes de mise en forme Markdown (`*`, accent grave) sont retirés des deux
côtés. Aucun réseau, aucune écriture hors de la sortie standard.
"""
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ICI = Path(__file__).resolve().parent
REGISTRE = ICI / "citations-synthese-v2.json"
NOTE = ICI.parent / "synthese-discoveryagent-pour-l-organisme-v2.md"


def norm(texte, markdown=False):
    t = unicodedata.normalize("NFKC", texte)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), (" ", " "), (" ", " ")):
        t = t.replace(a, b)
    if markdown:
        t = t.replace("*", "").replace("`", "")
    return re.sub(r"\s+", " ", t).strip()


def git(depot, *args):
    r = subprocess.run(["git", "-C", str(depot), *args], capture_output=True)
    if r.returncode not in (0, 1):
        raise RuntimeError(r.stderr.decode("utf-8", "replace")[:300])
    return r.stdout.decode("utf-8", "replace")


def sha(octets):
    return hashlib.sha256(octets).hexdigest()


def main():
    racine = Path(sys.argv[1]).resolve()
    table = "--table" in sys.argv
    reg = json.loads(REGISTRE.read_text(encoding="utf-8"))
    src = reg["sources"]
    pages = {}
    for nom in ("papier", "annexe"):
        f = racine / src[nom]["fichier"]
        brut = f.read_bytes()
        pages[nom] = brut.decode("utf-8").split("\f")
        if not table:
            print(f"source {nom}: {src[nom]['fichier']} sha256 {sha(brut)} pages {len(pages[nom])}")
    for nom in ("code", "repro"):
        tete = git(src[nom]["depot"], "rev-parse", "HEAD").strip()
        if not table:
            print(f"source {nom}: {src[nom]['depot']} commit cité {src[nom]['commit']} ; HEAD {tete}")
    ok = echec = 0
    lignes_table = []
    for c in reg["citations"]:
        cid, s = c["id"], c["src"]
        trouve, lieu = False, ""
        try:
            if s in ("papier", "annexe"):
                p = c["page"]
                lieu = f"{s}, p. {p}"
                trouve = norm(c["extrait"]) in norm(pages[s][p - 1])
            elif s == "code":
                a, b = c["lignes"]
                lieu = f"code, `{c['fichier']}`, l. {a}-{b}" if a != b else f"code, `{c['fichier']}`, l. {a}"
                txt = git(src["code"]["depot"], "show", f"{src['code']['commit']}:{c['fichier']}").split("\n")
                trouve = norm(c["extrait"], True) in norm("\n".join(txt[a - 1:b]), True)
            elif s in ("organisme", "papierC"):
                lieu = f"`{c['fichier']}` (branche `{src[s]['ref'].replace('origin/', '')}`)"
                txt = git(racine, "show", f"{src[s]['ref']}:{c['fichier']}")
                trouve = norm(c["extrait"], True) in norm(txt, True)
            elif s == "disque":
                lieu = f"`{c['fichier']}`"
                txt = (racine / c["fichier"]).read_text(encoding="utf-8")
                trouve = norm(c["extrait"], True) in norm(txt, True)
            elif s == "absence":
                d = src[c["depot"]]
                lieu = f"dépôt {c['depot']}, motif `{c['motif_contenu']}` sous {', '.join(c['sous'])}"
                sortie = git(d["depot"], "grep", "-n", "-i", "-E", c["motif_contenu"], d["commit"], "--", *c["sous"])
                touches = [l.split(":", 3) for l in sortie.splitlines() if l]
                fichiers = sorted({t[1] for t in touches})
                trouve = fichiers == sorted(c["attendu_fichiers"])
                if "attendu_occurrences" in c:
                    trouve = trouve and len(touches) == c["attendu_occurrences"]
                c["extrait"] = c["dit"] + f" (fichiers touchés : {fichiers or 'aucun'} ; occurrences : {len(touches)})"
            elif s == "absence_noms":
                d = src[c["depot"]]
                lieu = f"dépôt {c['depot']}, noms des fichiers suivis"
                noms = [n for n in git(d["depot"], "ls-tree", "-r", "--name-only", d["commit"]).splitlines() if n]
                touches = [n for n in noms if re.search(c["motif_nom"], n, re.I)]
                trouve = (not touches) and len(noms) == c["attendu_total"]
                c["extrait"] = c["dit"] + f" (fichiers suivis : {len(noms)} ; noms touchés : {touches or 'aucun'})"
            else:
                lieu = "source inconnue"
        except Exception as e:  # une citation illisible est un échec, jamais un repli
            lieu += f" [erreur : {e}]"
            trouve = False
        ok += trouve
        echec += (not trouve)
        if table:
            lignes_table.append(f"| {cid} | {lieu} | {c['extrait'].replace('|', '/')} |")
        else:
            print(f"{'OK   ' if trouve else 'ÉCHEC'} {cid} — {lieu}")
    if table:
        print("| n° | lieu | extrait vérifié |")
        print("|---|---|---|")
        print("\n".join(lignes_table))
        return 0
    # la note cite-t-elle des identifiants connus, et tous ?
    ids = {c["id"] for c in reg["citations"]}
    if NOTE.exists():
        corps = NOTE.read_text(encoding="utf-8")
        avant_table = corps.split("## Annexe — table des citations vérifiées")[0]
        cites = set(re.findall(r"\b([PACXN]\d{2})\b", avant_table))
        inconnus = sorted(cites - ids)
        non_cites = sorted(ids - cites)
        print(f"note: {NOTE.name} sha256 {sha(NOTE.read_bytes())}")
        print(f"identifiants cités dans la note : {len(cites)} ; inconnus du registre : {inconnus or 'aucun'} ; au registre mais non cités : {non_cites or 'aucun'}")
        echec += len(inconnus)
    else:
        print("note absente : contrôle des identifiants non fait")
        echec += 1
    print(f"BILAN : {ok} citations vérifiées, {echec} échec(s), sur {len(reg['citations'])} au registre")
    return 0 if echec == 0 else 1


class _Double:
    """Écrit à la sortie standard et garde le texte pour le fichier de sortie."""

    def __init__(self, flux):
        self.flux, self.morceaux = flux, []

    def write(self, s):
        self.morceaux.append(s)
        return self.flux.write(s)

    def flush(self):
        self.flux.flush()


if __name__ == "__main__":
    chemins = [a.split("=", 1)[1] for a in sys.argv[2:] if a.startswith("--sortie=")]
    if chemins:
        double = _Double(sys.stdout)
        sys.stdout = double
        code = main()
        sys.stdout = double.flux
        Path(chemins[0]).write_text("".join(double.morceaux), encoding="utf-8")
        sys.exit(code)
    sys.exit(main())
