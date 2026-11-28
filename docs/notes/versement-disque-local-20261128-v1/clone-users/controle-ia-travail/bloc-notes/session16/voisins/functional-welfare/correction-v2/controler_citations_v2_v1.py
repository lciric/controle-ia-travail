"""Contrôle des citations de la note functional-welfare v2 — v1 (correcteur neuf, 21 octobre 2026).

Chaque citation s'écrit “…” suivie de (p. N) pour le papier lu, ou de (IDENTIFIANT, p. N) pour une autre source.
Le script :
- refuse une citation sans renvoi de page, ou d'une source non passée en argument ;
- extrait chaque page de chaque PDF par deux extracteurs : pdfplumber (page entière, deux colonnes, et coupes
  horizontales successives de 20 points pour le papier lu) et pdftotext (modes simple, -layout, -raw) ;
- p. 7 du papier lu : pdfplumber seulement, sur les caractères à matrice d'échelle 1 (texte courant) et les
  étiquettes DejaVu du cadre rendu de la figure 2 (190 ≤ top ≤ 300) ; la couche non rendue (échelles 0,687 et 0,426)
  est extraite à part : une citation qui ne s'y trouverait que là est refusée (« COUCHE ») ;
- normalise (NFKC, apostrophes, guillemets, signes moins et tirets, trait d'union conditionnel, coupures de fin de
  ligne gardées ou ôtées, espaces) et exige la citation telle quelle dans le texte de la page citée ;
- cherche aussi chaque citation (comparaison lâche : lettres et chiffres seuls) sur toutes les pages de sa source et
  rapporte les autres pages où elle se lit (mauvaise page ou page ambiguë) ;
- si une note de référence (v1) est donnée, marque « NEUVE » toute citation (texte, source, page) absente de la v1.
Usage : python3 -B -I controler_citations_v2_v1.py NOTE PDF_LU [--reference NOTE_V1] [ID=PDF ...]
Sortie : une ligne par citation ; bilan ; code 1 au moindre refus.
"""
import re
import subprocess
import sys
import unicodedata
from collections import Counter

import pdfplumber

CITATION = re.compile(r"“([^”]*)”")
RENVOI = re.compile(r"^\s*\((?:([0-9]{4}\.[0-9]{5}v[0-9]+),\s*)?p\.\s*([0-9]+)\)")


def norm(t):
    t = unicodedata.normalize("NFKC", t)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("−", "-"), ("–", "-"), ("—", "-"),
                 ("­", ""), ("×", "x"), (" ", " ")):
        t = t.replace(a, b)
    return t


def variantes(t):
    t = norm(t)
    return [re.sub(r"\s+", " ", re.sub(r"-[ \t]*\n[ \t]*", r, t)).strip() for r in ("", "-")]


def lache(t):
    return re.sub(r"[^0-9A-Za-z]", "", norm(t))


def pdftotext_page(pdf, i):
    sorties = []
    for mode in ([], ["-layout"], ["-raw"]):
        r = subprocess.run(["pdftotext", *mode, "-f", str(i), "-l", str(i), pdf, "-"], capture_output=True, text=True)
        if r.returncode != 0:
            raise SystemExit(f"pdftotext a échoué : {pdf} p. {i}")
        sorties.append(r.stdout)
    return sorties


def plumber_textes(p, coupes):
    l, h = p.width, p.height
    t = [p.extract_text(x_tolerance=1.5) or ""]
    t += [p.crop(b).extract_text(x_tolerance=1.5) or "" for b in ((0, 0, l / 2, h), (l / 2, 0, l, h))]
    if coupes:
        for haut in range(0, int(h) - 40, 20):
            g = p.crop((0, haut, l / 2, h)).extract_text(x_tolerance=1.5) or ""
            d = p.crop((l / 2, haut, l, h)).extract_text(x_tolerance=1.5) or ""
            t.append(g + "\n" + d)
    return t


def charger(pdf, lu):
    """{page: [textes normalisés]} ; pour le papier lu, clé « 7-couche » : la couche non rendue de la p. 7."""
    pages = {}
    with pdfplumber.open(pdf) as doc:
        for i, p in enumerate(doc.pages, start=1):
            if lu and i == 7:
                def visible(o):
                    if o.get("object_type") != "char":
                        return True
                    if "DejaVu" in o["fontname"]:
                        return 190 <= o["top"] <= 300
                    return round(o["matrix"][0], 3) == 1.0
                bruts = plumber_textes(p.filter(visible), True)
                couche = p.filter(lambda o: o.get("object_type") != "char"
                                  or (round(o["matrix"][0], 3) in (0.687, 0.426) and "DejaVu" not in o["fontname"]))
                pages["7-couche"] = [v for b in [couche.extract_text(x_tolerance=1.5) or ""] for v in variantes(b)]
            else:
                bruts = plumber_textes(p, lu) + pdftotext_page(pdf, i)
            pages[i] = [v for b in bruts for v in variantes(b)]
    return pages


def citations(texte):
    out = []
    for m in CITATION.finditer(texte):
        r = RENVOI.match(texte[m.end():m.end() + 40])
        if r is None:
            out.append((m.group(1), None, None))
        else:
            out.append((m.group(1), r.group(1) or "LU", int(r.group(2))))
    return out


def main(argv):
    args = argv[1:]
    reference = None
    if "--reference" in args:
        k = args.index("--reference")
        reference = args[k + 1]
        del args[k:k + 2]
    note, pdf_lu = args[0], args[1]
    sources = {"LU": (pdf_lu, True)}
    for a in args[2:]:
        k, v = a.split("=", 1)
        sources[k] = (v, False)
    anciennes = Counter()
    if reference:
        anciennes = Counter(citations(open(reference, encoding="utf-8").read()))
    cache, n, refus, neuves = {}, 0, 0, 0
    for cit, ident, page in citations(open(note, encoding="utf-8").read()):
        n += 1
        marque = "v1   "
        if reference and anciennes[(cit, ident, page)] > 0:
            anciennes[(cit, ident, page)] -= 1
        elif reference:
            marque, neuves = "NEUVE", neuves + 1
        if ident is None:
            print(f"SANS-PAGE {marque} : {cit}")
            refus += 1
            continue
        if ident not in sources:
            print(f"SOURCE?   {marque} {ident} p. {page} : {cit}")
            refus += 1
            continue
        if ident not in cache:
            cache[ident] = charger(*sources[ident])
        pages = cache[ident]
        if page not in pages:
            print(f"PAGE?     {marque} {ident} p. {page} : {cit}")
            refus += 1
            continue
        c = re.sub(r"\s+", " ", norm(cit)).strip()
        ok = any(c in t for t in pages[page])
        dans_couche = any(c in t for t in pages.get("7-couche", [])) if (ident == "LU" and page == 7) else False
        ailleurs = [k for k, ts in pages.items() if k != page and k != "7-couche" and any(lache(cit) in lache(t) for t in ts)]
        etat = "OK       " if ok else ("COUCHE   " if dans_couche else "ECHEC    ")
        if not ok:
            refus += 1
        print(f"{etat} {marque} {ident} p. {page} ; aussi lue en {ailleurs if ailleurs else '-'} : {cit}")
    print(f"BILAN : {n} citations, dont {neuves} neuves ou changées par rapport à la référence ; {refus} refus")
    return 1 if refus else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
