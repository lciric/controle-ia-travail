"""Rejeu indépendant (contre-lecteur, modèle D) des citations de la lecture « priorité haute O4 ».

Différences voulues avec le vérificateur de l'auteur (modèle C) :
- extraction page par page (pdftotext -f N -l N), dans deux modes (défaut et -raw), au lieu d'un
  seul passage découpé sur le saut de page ;
- trois niveaux de comparaison, du plus strict au plus lâche :
    strict   : NFKC (ligatures), guillemets et tirets unifiés, espaces réduits à un seul ; casse gardée,
               ponctuation gardée, césures NON recollées ;
    cesure   : strict + recollage des césures de fin de ligne (« mot-\nsuite » -> « motsuite » ET
               « mot-suite » essayés tous deux) ;
    lache    : seuls les caractères alphanumériques, casse ignorée (équivaut à la règle de l'auteur).
- les citations présentes dans la note mais absentes du fichier de citations sont ajoutées (champ
  "origine": "note seulement").
Usage : python3 -I rejouer_citations_priorite_haute_o4_v2.py <racine> <citations.json> <sortie.json>
Aucune heure n'est écrite par ce programme.
"""
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

QUOTES = {"‘": "'", "’": "'", "‚": "'", "‛": "'", "“": '"', "”": '"',
          "«": '"', "»": '"', "′": "'", "`": "'"}
DASHES = {"‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-", "−": "-"}


def base(s):
    s = unicodedata.normalize("NFKC", s).replace("­", "")
    for k, v in {**QUOTES, **DASHES}.items():
        s = s.replace(k, v)
    return s


def strict(s):
    return re.sub(r"\s+", " ", base(s)).strip()


def cesure_variants(s):
    """Deux lectures d'une fin de ligne coupée par un tiret : tiret de césure (retiré) ou tiret vrai (gardé)."""
    b = base(s)
    retire = re.sub(r"\s+", " ", re.sub(r"-\s*\n\s*", "", b)).strip()
    garde = re.sub(r"\s+", " ", re.sub(r"-\s*\n\s*", "-", b)).strip()
    return retire, garde


def lache(s):
    return re.sub(r"[^0-9a-zà-ÿ]+", "", base(s).lower())


def page_text(pdf, n, raw):
    cmd = ["pdftotext", "-f", str(n), "-l", str(n)] + (["-raw"] if raw else []) + [str(pdf), "-"]
    return subprocess.run(cmd, capture_output=True, text=True).stdout


def n_pages(pdf):
    out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
    return int(re.search(r"^Pages:\s+(\d+)", out, re.M).group(1))


NOTE_SEULEMENT = [
    {"piece": "NMV-NBER", "pdf": "docs/sources/pdf/lecture-o4-v2/nber-w33363/w33363.pdf",
     "empreinte": "d889aff69bdcb65d232b7c3e9294c9a821417b0e8a813c85994619403302a0d3",
     "page": 10, "citation": "After reviewing these results", "origine": "note seulement"},
]


def main():
    racine, cits, sortie = Path(sys.argv[1]), json.load(open(sys.argv[2], encoding="utf-8")), sys.argv[3]
    cits = [{**c, "origine": "fichier de citations"} for c in cits] + NOTE_SEULEMENT
    cache = {}
    res = []
    for c in cits:
        pdf = racine / c["pdf"]
        if pdf not in cache:
            n = n_pages(pdf)
            pages = {i: (page_text(pdf, i, False), page_text(pdf, i, True)) for i in range(1, n + 1)}
            cache[pdf] = (n, pages, hashlib.sha256(pdf.read_bytes()).hexdigest())
        n, pages, h = cache[pdf]
        q = c["citation"]

        def niveau(i):
            for t in pages[i]:
                if strict(q) in strict(t):
                    return "strict"
            for t in pages[i]:
                if any(strict(q) in v for v in cesure_variants(t)):
                    return "cesure"
            for t in pages[i]:
                if lache(q) in lache(t):
                    return "lache"
            return None

        p = c["page"]
        niv = niveau(p) if 1 <= p <= n else None
        ailleurs = [i for i in range(1, n + 1) if i != p and niveau(i)]
        res.append({**c, "pages_du_pdf": n, "sha256_pdf_recalcule": h, "empreinte_conforme": h == c["empreinte"],
                    "niveau_sur_la_page": niv, "trouvee_sur_la_page": niv is not None,
                    "autres_pages": ailleurs})
    json.dump(res, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for origine in ("fichier de citations", "note seulement"):
        sel = [r for r in res if r["origine"] == origine]
        ok = sum(r["trouvee_sur_la_page"] and r["empreinte_conforme"] for r in sel)
        par = {k: sum(r["niveau_sur_la_page"] == k for r in sel) for k in ("strict", "cesure", "lache")}
        print(f"{origine} : {ok} sur {len(sel)} sur la page dite, empreinte conforme ; niveaux {par}")
    for r in res:
        if r["niveau_sur_la_page"] != "strict" or not r["empreinte_conforme"] or r["autres_pages"]:
            print(" -", r["piece"], "p.", r["page"], "niveau", r["niveau_sur_la_page"], "autres pages", r["autres_pages"],
                  "|", r["citation"][:70])


main()
