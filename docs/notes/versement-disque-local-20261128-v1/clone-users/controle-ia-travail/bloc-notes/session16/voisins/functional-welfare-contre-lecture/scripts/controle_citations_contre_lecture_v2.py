"""Contre-lecture : contrôle indépendant des citations de la note functional-welfare v1 — v2 (ajoute la lecture colonne gauche puis colonne droite, une phrase pouvant passer d'une colonne à l'autre).

Différences voulues avec le script du lecteur :
- extraction par pdfplumber (et non pdftotext), page par page, pour tous les PDF ;
- p. 7 du papier lu : ne garde que les caractères à matrice d'échelle 1 (texte courant) et les étiquettes DejaVu
  du cadre rendu de la figure 2 ; la couche cachée (échelles 0,687 et 0,426) est exclue par ce critère, pas par
  la police ni le corps ;
- deux niveaux de comparaison : strict (espaces et coupures normalisés) et lâche (lettres et chiffres seuls) ;
- chaque citation est cherchée sur TOUTES les pages du PDF : on rapporte les pages où elle se trouve, pour
  détecter une mauvaise page ou une page ambiguë ;
- la couche cachée de la p. 7 est aussi interrogée : une citation qui ne s'y trouverait que là serait signalée.
Usage : python3 -B -I controle_citations_contre_lecture_v1.py NOTE PDF_LU [ID=PDF ...]
Sortie : une ligne par citation ; bilan ; code 1 au moindre échec strict à la page citée.
"""
import re
import sys
import unicodedata

import pdfplumber

MOTIF_CITATION = re.compile(r"“([^”]+)”")
MOTIF_RENVOI = re.compile(r"^\s*\((?:([0-9]{4}\.[0-9]{5}v[0-9]+),\s*)?p\.\s*([0-9]+)\)")


def norm(t):
    t = unicodedata.normalize("NFKC", t)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("−", "-"), ("–", "-"), ("—", "-"),
                 ("­", ""), ("×", "x")):
        t = t.replace(a, b)
    return t


def strict(t):
    t = norm(t)
    t = re.sub(r"-\s*\n\s*", "-", t)  # coupure gardée
    return re.sub(r"\s+", " ", t).strip()


def strict_sans_tiret(t):
    t = norm(t)
    t = re.sub(r"-\s*\n\s*", "", t)  # coupure ôtée
    return re.sub(r"\s+", " ", t).strip()


def lache(t):
    return re.sub(r"[^0-9A-Za-z]", "", norm(t))


def pages_texte(pdf, lu):
    out = {}
    with pdfplumber.open(pdf) as doc:
        for i, p in enumerate(doc.pages, start=1):
            if lu and i == 7:
                def visible(o):
                    if o.get("object_type") != "char":
                        return True
                    if "DejaVu" in o["fontname"]:
                        return 190 <= o["top"] <= 300
                    return round(o["matrix"][0], 3) == 1.0
                q = p.filter(visible)
                textes = [q.extract_text(x_tolerance=1.5) or ""]
                textes += [q.crop(b).extract_text(x_tolerance=1.5) or "" for b in ((0, 0, p.width / 2, p.height), (p.width / 2, 0, p.width, p.height))]
                textes.append(textes[1] + "\n" + textes[2])
                cachee = p.filter(lambda o: o.get("object_type") != "char" or (round(o["matrix"][0], 3) in (0.687, 0.426) and "DejaVu" not in o["fontname"]))
                out["7-cachee"] = [cachee.extract_text(x_tolerance=1.5) or ""]
            else:
                textes = [p.extract_text(x_tolerance=1.5) or ""]
                textes += [p.crop(b).extract_text(x_tolerance=1.5) or "" for b in ((0, 0, p.width / 2, p.height), (p.width / 2, 0, p.width, p.height))]
                textes.append(textes[1] + "\n" + textes[2])
            out[i] = textes
    return out


def present(cit, textes, niveau):
    if niveau == "strict":
        c = strict(cit)
        return any(c in strict(t) or c in strict_sans_tiret(t) for t in textes)
    c = lache(cit)
    return any(c in lache(t) for t in textes)


def main(argv):
    note, pdf_lu = argv[1], argv[2]
    sources = {"LU": (pdf_lu, True)}
    for a in argv[3:]:
        k, v = a.split("=", 1)
        sources[k] = (v, False)
    texte = open(note, encoding="utf-8").read()
    cache = {}
    n = echecs = 0
    for m in MOTIF_CITATION.finditer(texte):
        n += 1
        cit = m.group(1)
        r = MOTIF_RENVOI.match(texte[m.end():m.end() + 40])
        if not r:
            print(f"SANS-PAGE  : {cit[:90]}")
            echecs += 1
            continue
        ident, page = r.group(1) or "LU", int(r.group(2))
        if ident not in sources:
            print(f"SOURCE?    {ident} p. {page} : {cit[:80]}")
            echecs += 1
            continue
        if ident not in cache:
            cache[ident] = pages_texte(*sources[ident])
            if ident != "LU":
                pass
        pages = cache[ident]
        ok_s = present(cit, pages[page], "strict")
        ok_l = present(cit, pages[page], "lache")
        ailleurs = [k for k, t in pages.items() if k != page and present(cit, t, "lache")]
        etat = "OK    " if ok_s else ("LACHE " if ok_l else "ECHEC ")
        if not ok_s:
            echecs += 1
        print(f"{etat} {ident} p. {page} ; aussi lue en {ailleurs if ailleurs else '-'} : {cit}")
    print(f"BILAN : {n} citations, {echecs} sans correspondance stricte à la page citée")
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
