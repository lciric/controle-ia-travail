"""Contre-lecture : contrôle des nombres de la note (hors citations) dans les blocs T1 à T3 et le dispositif — v1.

Pour chaque puce des lignes données de la note : on retire les citations “…”, on relève les nombres (format français :
virgule décimale, signe moins typographique, puissances de dix « 6 × 10⁻⁶ »), on ignore ceux que précède « ≈ »
(lecture graphique, contrôlée à l'œil) et les numéros de page, de tableau, de figure ou d'annexe ; on cherche chacun,
converti au format anglais, dans le texte (pdfplumber, colonnes et page entière) des pages que la puce cite ;
à défaut de page citée, dans les p. 6 à 9 et 13.
Usage : python3 -B -I controle_nombres_T1_T3_v1.py NOTE PDF LIGNE_DEBUT LIGNE_FIN
"""
import re
import sys
import unicodedata

import pdfplumber


def norm(t):
    t = unicodedata.normalize("NFKC", t)
    for a, b in (("−", "-"), ("–", "-"), ("—", "-"), ("’", "'"), (" ", " "), (" ", " "), ("\xa0", " ")):
        t = t.replace(a, b)
    return t


def textes_pages(pdf):
    out = {}
    with pdfplumber.open(pdf) as doc:
        for i, p in enumerate(doc.pages, start=1):
            if i == 7:
                q = p.filter(lambda o: o.get("object_type") != "char" or round(o["matrix"][0], 3) == 1.0
                             or ("DejaVu" in o["fontname"] and 190 <= o["top"] <= 300))
            else:
                q = p
            t = (q.extract_text(x_tolerance=1.5) or "") + "\n" + (q.crop((0, 0, p.width / 2, p.height)).extract_text(x_tolerance=1.5) or "") \
                + "\n" + (q.crop((p.width / 2, 0, p.width, p.height)).extract_text(x_tolerance=1.5) or "")
            out[i] = re.sub(r"\s+", " ", norm(t))
    return out


NOMBRE = re.compile(r"(≈\s*)?([+-]?\d+(?:[  ]\d{3})*(?:,\d+)?)(\s*×\s*10⁻?[⁰¹²³⁴⁵⁶⁷⁸⁹]+)?")
EXPOSANTS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")


def pages_citees(puce):
    pages = set()
    for m in re.finditer(r"p\.\s*(\d+)(?:-(\d+))?", puce):
        a = int(m.group(1)); b = int(m.group(2) or a)
        pages.update(range(a, b + 1))
    return pages


def main(argv):
    note, pdf, l0, l1 = argv[1], argv[2], int(argv[3]), int(argv[4])
    lignes = open(note, encoding="utf-8").read().split("\n")[l0 - 1:l1]
    textes = textes_pages(pdf)
    n = manques = 0
    for k, puce in enumerate(lignes, start=l0):
        sans_cit = re.sub(r"“[^”]*”", " ", norm(puce).replace("−", "-"))
        pages = pages_citees(puce) or {6, 7, 8, 9, 13}
        # retirer les renvois (p. n, tableau n, figure n, annexe X, couche n, 80/24/24 gardé)
        travail = re.sub(r"(p\.|tableau|tableaux|figure|figures|section|annexe|l\.)\s*\d+(?:-\d+)?", " ", sans_cit, flags=re.I)
        cible = " ".join(textes[p] for p in sorted(pages) if p in textes)
        for m in NOMBRE.finditer(travail):
            if m.group(1):
                continue  # lecture graphique
            brut = m.group(2).replace(" ", "").replace(" ", "")
            en = brut.replace(",", ".")
            if m.group(3):
                exp = m.group(3).translate(EXPOSANTS)
                exp = re.sub(r"\s*×\s*10", "", exp)
                motifs = [rf"{re.escape(en.lstrip('+'))}\s*[x×]\s*10\s*{re.escape(exp)}"]
            else:
                nu = en.lstrip("+-")
                motifs = [rf"(?<![\d.]){re.escape(nu)}(?![\d])"]
                if "." in nu and nu.startswith("0."):
                    motifs.append(rf"(?<![\d]){re.escape(nu[1:])}(?![\d])")  # .023 pour 0,023
            n += 1
            trouve = any(re.search(mo, cible) for mo in motifs)
            if not trouve:
                manques += 1
            print(f"{'OK    ' if trouve else 'ABSENT'} l. {k} {m.group(0).strip():>14s}  pages {sorted(pages)}")
    print(f"BILAN : {n} nombres contrôlés, {manques} absents des pages citées")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
