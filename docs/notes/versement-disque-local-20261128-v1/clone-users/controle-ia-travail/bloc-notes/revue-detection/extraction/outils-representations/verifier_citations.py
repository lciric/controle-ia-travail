"""Vérifie que chaque citation (pdf, page, phrase) figure sur la page citée du PDF, après contrôle de l'empreinte.

Usage : python3 -I verifier_citations.py citations.json
Le JSON : {"pdfs": {"cle": {"chemin": ..., "sha256": ...}}, "citations": [[cle, page, phrase], ...]}
Normalisation : suites de blancs réduites à une espace ; césure « -\n » entre deux lettres recollée ; rien d'autre.
Toute anomalie est un échec explicite.
"""
import hashlib, json, re, subprocess, sys

def texte_page(chemin, page, mode):
    args = ["pdftotext", "-f", str(page), "-l", str(page)] + (["-layout"] if mode == "layout" else []) + [chemin, "-"]
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"ECHEC pdftotext {chemin} p{page}: {r.stderr[:200]}")
    t = re.sub(r"(?<=[A-Za-z])-\n(?=[a-z])", "", r.stdout)
    return re.sub(r"\s+", " ", t)

def main():
    d = json.load(open(sys.argv[1], encoding="utf-8"))
    for cle, p in d["pdfs"].items():
        h = hashlib.sha256(open(p["chemin"], "rb").read()).hexdigest()
        if h != p["sha256"]:
            raise SystemExit(f"ECHEC empreinte {cle}: {h} != {p['sha256']}")
    ok = ko = 0
    cache = {}
    for cle, page, phrase in d["citations"]:
        if cle not in d["pdfs"] or not isinstance(page, int) or page < 1 or not phrase.strip():
            print(f"ECHEC entree invalide: {cle} {page} {phrase!r}"); ko += 1; continue
        ch = d["pdfs"][cle]["chemin"]
        cible = re.sub(r"\s+", " ", phrase.strip())
        trouve = False
        for mode in ("brut", "layout"):
            k = (ch, page, mode)
            if k not in cache:
                cache[k] = texte_page(ch, page, mode)
            if cible in cache[k]:
                trouve = True; break
        if trouve:
            ok += 1
        else:
            ko += 1; print(f"ABSENT {cle} p{page}: {phrase!r}")
    print(f"conformes {ok} ; absentes {ko}")
    sys.exit(1 if ko else 0)

main()
