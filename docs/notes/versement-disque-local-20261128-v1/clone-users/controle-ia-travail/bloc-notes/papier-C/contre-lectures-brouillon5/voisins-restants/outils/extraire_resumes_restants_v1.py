"""Extrait résumés et métadonnées des pages téléchargées (arXiv, anthologie ACL), après contrôle d'empreinte.

Usage : python3 -I -B extraire_resumes_restants_v1.py SORTIE.txt TYPE:CHEMIN:EMPREINTE [...]
TYPE = arxiv | acl. Refuse (code 2) toute page dont l'empreinte diffère (R5).
Compare aussi, mot à mot, le résumé publié de Pan et al. à celui de la préimpression v3 si les deux sont donnés
(étiquettes « acl-pan » et « arxiv-pan »).
"""
import difflib
import hashlib
import html
import re
import sys


def lire(chemin, attendue):
    donnees = open(chemin, "rb").read()
    obtenue = hashlib.sha256(donnees).hexdigest()
    if obtenue != attendue:
        print(f"REFUS empreinte {chemin} : attendue {attendue}, obtenue {obtenue}")
        sys.exit(2)
    return donnees.decode("utf-8")


def nettoyer(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def arxiv(t):
    out = {}
    m = re.search(r'<blockquote class="abstract[^"]*">(.*?)</blockquote>', t, re.S)
    out["resume"] = nettoyer(m.group(1)).removeprefix("Abstract:").strip() if m else None
    m = re.search(r'<div class="submission-history">(.*?)</div>', t, re.S)
    out["historique"] = nettoyer(m.group(1)) if m else None
    m = re.search(r"Comments:</td>\s*<td[^>]*>(.*?)</td>", t, re.S)
    out["commentaire"] = nettoyer(m.group(1)) if m else None
    out["titre"] = re.findall(r'name="citation_title" content="([^"]*)"', t)
    out["auteurs"] = re.findall(r'name="citation_author" content="([^"]*)"', t)
    return out


def acl(t):
    out = {}
    m = re.search(r'<div class="card-body acl-abstract">(.*?)</div>', t, re.S)
    out["resume"] = nettoyer(m.group(1)).removeprefix("Abstract").strip() if m else None
    for k in ["citation_title", "citation_author", "citation_conference_title", "citation_publication_date",
              "citation_firstpage", "citation_lastpage", "citation_doi", "citation_pdf_url"]:
        out[k] = re.findall(r'<meta content="([^"]*)" name=' + k + r">", t)
    return out


def main():
    sortie = sys.argv[1]
    resultats = {}
    lignes = []
    for arg in sys.argv[2:]:
        etiquette, typ, chemin, attendue = arg.split("|")
        t = lire(chemin, attendue)
        r = arxiv(t) if typ == "arxiv" else acl(t)
        resultats[etiquette] = r
        lignes.append(f"## {etiquette} ({typ}) {chemin}\n# sha256 {attendue} : OK")
        for k, v in r.items():
            lignes.append(f"{k} : {v}")
        lignes.append("")
    if "acl-pan" in resultats and "arxiv-pan" in resultats:
        a = resultats["arxiv-pan"]["resume"].split()
        b = resultats["acl-pan"]["resume"].split()
        lignes.append("## Comparaison mot à mot : préimpression v3 (a) contre version publiée (b)")
        lignes.append(f"identiques : {a == b} ; mots a = {len(a)}, b = {len(b)}")
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
            if op != "equal":
                lignes.append(f"{op} : a « {' '.join(a[i1:i2])} » -> b « {' '.join(b[j1:j2])} »")
    open(sortie, "w", encoding="utf-8").write("\n".join(lignes) + "\n")
    print("\n".join(lignes))


if __name__ == "__main__":
    main()
