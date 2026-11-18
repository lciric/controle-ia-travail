"""Produit l'extrait de la grille remis aux codeurs (grille brouillon 3, section 4.4).

Garde : l'en-tête de statut, la section 1, la section A sans les lignes « Indicateur », « Analyse »
et « Consigne si retenue », la section B, la sous-section 4.5. Retire tout le reste (plan d'analyse,
marquages, règle du gabarit, points à trancher, pilote, traitement des remarques). Refuse si l'extrait
contient encore un mot du plan (indicateur, kappa, gabarit, consigne si retenue, marquage, bien noté).

Usage : python extraire_grille_codeurs_v1.py GRILLE SORTIE
"""
import hashlib
import re
import sys

INTERDITS = [r"\*\*Indicateur\*\*", r"\*\*Analyse\*\*", r"Consigne si retenue", r"kappa", r"gabarit",
             r"marquage", r"bien not", r"peu not", r"apparié"]


def sections(t):
    parts = re.split(r"(?m)^(## .*)$", t)
    out = {"_tete": parts[0]}
    for k in range(1, len(parts), 2):
        out[parts[k].strip()] = parts[k + 1]
    return out


def main(grille, sortie):
    t = open(grille, encoding="utf-8").read()
    s = sections(t)
    titre = s["_tete"].splitlines()[0].replace("# Grille", "# Extrait pour les codeurs — Grille")
    garder = [k for k in s if k.startswith("## 1.") or k.startswith("## A.") or k.startswith("## B.")]
    corps = []
    for k in garder:
        bloc = "\n".join(l for l in s[k].splitlines()
                         if not re.match(r"^- \*\*(Indicateur|Analyse|Consigne si retenue)\*\* :", l))
        corps.append(k + "\n" + bloc.rstrip("-\n ") + "\n")
    p4 = next(v for k, v in s.items() if k.startswith("## 4."))
    m = re.search(r"(?ms)^### 4\.5 .*?(?=^### |\Z)", p4)
    sec45 = m.group(0)
    sec45 = "\n".join(l for l in sec45.splitlines() if not l.startswith("- **Arbitrage**"))
    # Phrases qui renvoient au plan ou au gabarit, retirées des règles :
    texte = (titre + "\n\nExtrait produit par programme (`extraire_grille_codeurs_v1.py`) depuis `"
             + grille.split("/")[-1] + "` (sha256 " + hashlib.sha256(t.encode()).hexdigest() + ").\n\n"
             + "\n".join(corps) + "\n## Format de sortie\n\n" + sec45.split("\n", 1)[1] + "\n")
    texte = re.sub(r" La séparation, nouvelle au brouillon 3, vient de la contre-lecture : sans elle presque tous les billets tombaient dans la même modalité\.", "", texte)
    texte = re.sub(r" L'éloge argumenté, rangé ici au brouillon 2, passe en O13\.", "", texte)
    restes = [w for w in INTERDITS if re.search(w, texte, re.I)]
    if restes:
        lignes = [l for l in texte.splitlines() if any(re.search(w, l, re.I) for w in restes)]
        print("REFUS : mots du plan restants :", restes)
        for l in lignes[:10]:
            print("  ", l[:160])
        sys.exit(2)
    open(sortie, "w", encoding="utf-8").write(texte)
    print("extrait écrit :", sortie, len(texte.split()), "mots")


if __name__ == "__main__":
    main(*sys.argv[1:3])
