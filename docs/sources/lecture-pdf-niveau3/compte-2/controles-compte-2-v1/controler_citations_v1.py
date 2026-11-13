"""Contrôle indépendant des citations (compte 2) : n extraits sur n à la page citée du PDF dont l'empreinte est citée.
Usage : python3 -I controler_citations.py <citations.json> <dossier des PDF>"""
import hashlib, json, re, subprocess, sys, unicodedata
from pathlib import Path

def norm(t):
    t = unicodedata.normalize("NFKC", t)
    for a, b in {"’": "'", "‘": "'", "“": '"', "”": '"', "‐": "-", "‑": "-",
                 "‒": "-", "–": "-", "—": "-", "−": "-", "­": ""}.items():
        t = t.replace(a, b)
    t = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", t)          # césure en fin de ligne
    return re.sub(r"\s+", " ", t).strip().lower()

def page_text(pdf, p, layout):
    cmd = ["pdftotext"] + (["-layout"] if layout else []) + ["-f", str(p), "-l", str(p), str(pdf), "-"]
    return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout

def main(cit_file, pdf_dir):
    cits = json.loads(Path(cit_file).read_text(encoding="utf-8"))
    ok = ko = 0
    for i, c in enumerate(cits, 1):
        pdf = Path(pdf_dir) / c["pdf"]
        h = hashlib.sha256(pdf.read_bytes()).hexdigest()
        if h != c["sha256"]:
            ko += 1; print(f"ÉCHEC {i} empreinte {c['pdf']}"); continue
        q = norm(c["citation"]); q2 = q.replace("-", "")
        found = False
        for lay in (False, True):
            t = norm(page_text(pdf, c["page"], lay))
            if q in t or q2 in t.replace("-", "") or q.replace(" ", "") in t.replace(" ", ""):
                found = True; break
        if found: ok += 1
        else: ko += 1; print(f"ÉCHEC {i} {c['pdf']} p. {c['page']} : {c['citation'][:90]}")
    print(f"citations : {len(cits)} ; retrouvées : {ok} ; échecs : {ko}")
    return 0 if ko == 0 else 1

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
