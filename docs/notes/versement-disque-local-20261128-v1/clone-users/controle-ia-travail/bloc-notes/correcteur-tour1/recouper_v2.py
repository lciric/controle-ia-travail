"""Recoupe chaque phrase entre guillemets français de la synthèse v2 avec les pages des PDF des clés citées dans le même bloc.

Bloc = ligne de table, ou paragraphe (lignes jusqu'à une ligne vide ou une puce). Une phrase coupée par « … » est découpée ;
chaque morceau doit être sur la même page. Sortie : une ligne par phrase : trouvée (clé, pages) ou introuvable (à examiner :
phrase française, titre, ou erreur). Usage : python3 -I recouper_v2.py FICHIER.md
"""
import os
import re
import sys
import unicodedata

PAGES = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/verification/pages"
RO_TXT = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/correcteur-tour1/pages-RO"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("−", "-"), ("–", "-"),
                 ("—", "-"), ("ﬁ", "fi"), ("ﬂ", "fl")]:
        s = s.replace(a, b)
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.lower().strip()


def charger(cle: str) -> dict[int, str]:
    d = RO_TXT if cle == "RO" else os.path.join(PAGES, cle)
    out = {}
    if not os.path.isdir(d):
        return out
    for f in sorted(os.listdir(d)):
        if f.startswith("r") and f.endswith(".txt"):
            out[int(f[1:4])] = norm(open(os.path.join(d, f), errors="ignore").read())
    return out


def blocs(texte: str) -> list[str]:
    res, cur = [], []
    for ligne in texte.splitlines():
        if ligne.startswith("|") or not ligne.strip() or re.match(r"^\s*(- |\d+\. )", ligne):
            if cur:
                res.append(" ".join(cur))
                cur = []
            if ligne.startswith("|"):
                res.append(ligne)
                continue
        if ligne.strip():
            cur.append(ligne.strip())
    if cur:
        res.append(" ".join(cur))
    return res


def main() -> int:
    texte = open(sys.argv[1], encoding="utf-8").read()
    cles_connues = sorted(os.listdir(PAGES)) + ["RO"]
    cache = {}
    introuvables = 0
    total = 0
    for b in blocs(texte):
        cles = [c for c in cles_connues if re.search(r"\[" + re.escape(c) + r"[\] ]", b)]
        for q in re.findall(r"«\s*(.+?)\s*»", b):
            total += 1
            morceaux = [norm(m) for m in q.split("…") if norm(m)]
            trouve = []
            for c in cles:
                pages = cache.setdefault(c, charger(c))
                p_ok = [p for p, t in pages.items() if all(m in t for m in morceaux)]
                if p_ok:
                    trouve.append(f"{c} p. {','.join(map(str, p_ok))}")
            if trouve:
                print(f"trouvée | {q[:90]} | {' ; '.join(trouve)}")
            else:
                introuvables += 1
                print(f"INTROUVABLE | {q[:110]} | clés du bloc : {cles}")
    print(f"--- {total} phrases ; {introuvables} introuvables (à examiner une à une)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
