"""Contrôle par programme du critère d'identité v8 contre la v7 (et la v6) : seuils, tolérance, libellés, autorisations, numéros
de paragraphe, et lieu de chaque différence. Lit trois fichiers donnés en argument ; n'écrit rien."""
import collections, difflib, re, sys
v6, v7, v8 = (open(p, encoding="utf-8").read() for p in sys.argv[1:4])
SEUILS = re.compile(r"10⁻[⁰¹²³⁴⁵⁶⁷⁸⁹]+|\b0,10\b")
LIBELLES = ["palier 1 — même lentille, octets identiques",
            "palier 2 — différences entre moitiés concordantes à 10⁻³ près ; octets différents ; matrices non",
            "« différente »", "non comparable (traitée comme différente)", "mention suspendue : anomalie (nœud de Lazar)"]
def corps(t):            # § 1 à § 10, sans l'en-tête ni le § 0 (tables de différences)
    return t[t.index("\n## 1. "):]
def titres(t):
    return [l for l in t.splitlines() if l.startswith(("## ", "### "))]
def bloc(t, debut, fin):
    i = t.index(debut); return t[i:t.index(fin, i)]
def norm(t): return re.sub(r"\s+", " ", t)
ok = True
def dire(nom, cond, detail=""):
    global ok; ok &= bool(cond); print(("TENU  " if cond else "MANQUÉ"), nom, detail)
for nom, t in (("v7", v7), ("v8", v8)):
    print(nom, "seuils dans le corps :", dict(collections.Counter(SEUILS.findall(corps(t)))))
dire("mêmes seuils, mêmes comptes, dans le corps (§ 1 à § 10)",
     collections.Counter(SEUILS.findall(corps(v7))) == collections.Counter(SEUILS.findall(corps(v8))))
dire("mêmes seuils dans tout le texte",
     set(SEUILS.findall(v7)) == set(SEUILS.findall(v8)), sorted(set(SEUILS.findall(v8)) ^ set(SEUILS.findall(v7))))
for l in LIBELLES:
    dire(f"libellé « {l[:45]}… » : mêmes occurrences dans le corps", corps(v7).count(l) == corps(v8).count(l),
         f"{corps(v7).count(l)} / {corps(v8).count(l)}")
tab = lambda t: bloc(t, "| verdict d'identité |", "\n\n")
dire("tableau de ce que chaque mention autorise (§ 5) identique", tab(v7) == tab(v8))
dire("tableau du § 5 identique à celui de la v6", tab(v6) == tab(v8))
dire("titres de paragraphe (## et ###) identiques à la v7", titres(v7) == titres(v8))
dire("titres de paragraphe identiques à la v6", titres(v6) == titres(v8))
tol = lambda t: norm(bloc(t, "- **Tolérance conventionnelle", "\n- **Pour R, deux séries"))
dire("paragraphe de la tolérance identique", tol(v7) == tol(v8))
mentions = lambda t: norm(bloc(t, "### Les mentions", "**Sur le zéro exact"))
dire("bloc « Les mentions » (§ 4) identique", mentions(v7) == mentions(v8))
pre = lambda t: norm(bloc(t, "### Préalables du programme", "### Ce que le deuxième palier voit"))
dire("bloc « Préalables du programme » (§ 4) identique", pre(v7) == pre(v8))
s6 = lambda t: norm(bloc(t, "## 6. Audit", "## 7. Programme"))
dire("§ 6 (audit) identique", s6(v7) == s6(v8))
s5 = lambda t: norm(bloc(t, "## 5. Ce que chaque mention autorise", "## 6. Audit"))
dire("§ 5 identique", s5(v7) == s5(v8))
print("--- lignes du corps changées de la v7 à la v8 :")
for l in difflib.unified_diff(corps(v7).splitlines(), corps(v8).splitlines(), lineterm="", n=0):
    if l.startswith(("+++", "---")): continue
    print("   ", l[:170])
print("RÉSULTAT :", "tout est tenu" if ok else "au moins un contrôle manqué")
