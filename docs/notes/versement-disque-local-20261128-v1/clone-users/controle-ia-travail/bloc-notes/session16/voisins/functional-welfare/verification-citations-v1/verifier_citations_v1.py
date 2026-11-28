"""Contrôle des citations d'une note de lecture contre le texte des PDF — v1.

Chaque citation verbatim de la note s'écrit “…” suivie de (p. N) pour le papier lu,
ou de (IDENTIFIANT, p. N) pour une autre source. Le script :
- refuse toute citation “…” sans renvoi de page ;
- extrait le texte de la page citée (pdftotext, trois modes) ; pour le papier lu, page 7,
  il n'utilise que les caractères rendus (pdfplumber, corps de moins de 9 points et polices de la couche invisible
  exclus, étiquettes de figure gardées dans le seul cadre de la figure 2) ;
- normalise (NFKC, apostrophes, guillemets, signes moins, coupures de fin de ligne) ;
- exige que la citation figure telle quelle dans le texte de la page.
Sortie : une ligne par citation (OK / ECHEC) ; code de retour 1 au moindre échec.
Usage : python3 -B -I verifier_citations_v1.py NOTE PDF_LU [ID=PDF ...]
"""
import re
import subprocess
import sys
import unicodedata

HIDDEN_FONTS = {"ZPXDWK+TeXGyreTermesX-Regular", "NUSUND+TeXGyreTermesX-Bold"}
PAGES_A_COUCHE_INVISIBLE = {7}  # papier lu seulement (constaté sur le PDF v1)

MOTIF = re.compile(r"“([^”]+)”\s*\((?:([0-9]{4}\.[0-9]{5}v[0-9]+), )?p\. ([0-9]+)")


def normaliser(t):
    t = unicodedata.normalize("NFKC", t)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("−", "-"), ("–", "-"), ("—", "-"), ("­", "")):
        t = t.replace(a, b)
    return t


def variantes(texte):
    t = normaliser(texte)
    sans_coupure = re.sub(r"-[ \t]*\n[ \t]*", "", t)
    avec_coupure = re.sub(r"-[ \t]*\n[ \t]*", "-", t)
    return [re.sub(r"\s+", " ", v) for v in (sans_coupure, avec_coupure)]


def textes_pdftotext(pdf, page):
    sorties = []
    for mode in ([], ["-layout"], ["-raw"]):
        r = subprocess.run(["pdftotext", *mode, "-f", str(page), "-l", str(page), pdf, "-"],
                           capture_output=True, text=True)
        if r.returncode != 0:
            raise SystemExit(f"pdftotext a échoué sur {pdf} p. {page}")
        sorties.append(r.stdout)
    return sorties


def textes_visibles(pdf, page):
    import pdfplumber  # import local : seulement pour la page à couche invisible
    with pdfplumber.open(pdf) as doc:
        p = doc.pages[page - 1]

        def visible(obj):
            # Page 7 du PDF v1 : la figure 2 embarque, rognée, une couche de texte non rendue
            # (brouillon antérieur, corps 2,5 à 8,2 points). Règle : on garde le texte courant
            # (corps 9 points et plus, polices de la couche invisible exclues) et les étiquettes
            # DejaVu dans le seul cadre rendu de la figure 2.
            if obj.get("object_type") != "char":
                return True
            nom = obj.get("fontname", "")
            if "DejaVu" in nom:
                return 190 <= obj.get("top", 0) <= 300
            if nom in HIDDEN_FONTS:
                return False
            return obj.get("size", 0) >= 8.9

        q = p.filter(visible)
        w, h = p.width, p.height
        sorties = [q.extract_text(x_tolerance=1) or ""]
        for bbox in ((0, 0, w / 2, h), (w / 2, 0, w, h)):
            sorties.append(q.crop(bbox).extract_text(x_tolerance=1) or "")
        return sorties


def main(argv):
    note, pdf_lu = argv[1], argv[2]
    sources = {"LU": pdf_lu}
    for a in argv[3:]:
        k, v = a.split("=", 1)
        sources[k] = v
    texte_note = open(note, encoding="utf-8").read()
    nb_ouvrants = texte_note.count("“")
    trouvees = list(MOTIF.finditer(texte_note))
    echecs = 0
    if nb_ouvrants != len(trouvees):
        print(f"ECHEC structure : {nb_ouvrants} guillemets ouvrants, {len(trouvees)} citations avec page")
        echecs += 1
    cache = {}
    for m in trouvees:
        phrase, ident, page = m.group(1), m.group(2) or "LU", int(m.group(3))
        if ident not in sources:
            print(f"ECHEC source inconnue {ident} : {phrase[:60]}")
            echecs += 1
            continue
        cle = (ident, page)
        if cle not in cache:
            pdf = sources[ident]
            if ident == "LU" and page in PAGES_A_COUCHE_INVISIBLE:
                bruts = textes_visibles(pdf, page)
            else:
                bruts = textes_pdftotext(pdf, page)
            cache[cle] = [v for b in bruts for v in variantes(b)]
        cible = re.sub(r"\s+", " ", normaliser(phrase)).strip()
        ok = any(cible in v for v in cache[cle])
        print(f"{'OK    ' if ok else 'ECHEC '} {ident} p. {page} : {phrase}")
        echecs += 0 if ok else 1
    print(f"BILAN : {len(trouvees)} citations, {echecs} échec(s)")
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
