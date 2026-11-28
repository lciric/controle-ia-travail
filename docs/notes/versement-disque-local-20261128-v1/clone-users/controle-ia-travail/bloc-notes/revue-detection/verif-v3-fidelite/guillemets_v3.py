"""Relevé des passages entre guillemets de la synthèse v3 : pour chacun, clé et page citées les plus proches
(lues dans le texte qui suit le passage, même cellule ou même phrase), présence à cette page exacte, et toutes
les pages des 22 PDF où le passage se trouve. Sortie sur la sortie standard.

python3 -I -B guillemets_v3.py > sortie-guillemets-v3.txt
"""
import importlib.util
import re

ICI = "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection/"
spec = importlib.util.spec_from_file_location("page3", ICI + "verif-v3-fidelite/page3.py")
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)

V3 = ICI + "synthese-comment-detecter-v3.md"
CLES = "AP PAR OA CA YS BX AG KU MK GM EM MA BU LIAR FQ K LB AU DYL RH CC RO".split()
texte = open(V3, encoding="utf-8").read()
lignes = texte.split("\n")
debuts = []
pos = 0
for l in lignes:
    debuts.append(pos)
    pos += len(l) + 1


def num_ligne(i):
    n = 0
    for k, d in enumerate(debuts):
        if d <= i:
            n = k + 1
        else:
            break
    return n


def cle_de_ligne(n):
    l = lignes[n - 1]
    m = re.match(r"\| [^|]*\[([A-Z]+)\]", l)
    return m.group(1) if m else None


RE_CIT = re.compile(r"\[?(?P<cle>AP|PAR|OA|CA|YS|BX|AG|KU|MK|GM|EM|MA|BU|LIAR|FQ|K|LB|AU|DYL|RH|CC|RO)?\s?"
                    r"(?:table \d+, )?p\. (?P<p>\d+)")


def citation_suivante(i_fin, n):
    """Première mention « p. N » après le passage, dans les 400 caractères, sans franchir une cellule."""
    suite = texte[i_fin:i_fin + 400]
    coupe = suite.find(" | ")
    if coupe >= 0:
        suite = suite[:coupe]
    m = RE_CIT.search(suite)
    if not m:
        return None, None
    cle = m.group("cle")
    if not cle:
        # clé entre crochets juste avant la mention de page dans la suite, ou clé de la ligne de table
        avant = suite[:m.start()]
        mm = re.findall(r"\[([A-Z]+)[ \]]", avant)
        cle = mm[-1] if mm else cle_de_ligne(n)
    return cle, int(m.group("p"))


resultats = []
for m in re.finditer(r"«\s*(.+?)\s*»", texte, flags=re.S):
    brut = m.group(1)
    n = num_ligne(m.start())
    morceaux = [x.strip(" .") for x in re.split(r"\s*…\s*", brut) if len(x.strip(" .")) >= 3]
    cle, page = citation_suivante(m.end(), n)
    partout = {}
    for c in CLES:
        pg = None
        for mo in morceaux:
            o = set(P.ou(c, mo))
            pg = o if pg is None else (pg & o)
        if pg:
            partout[c] = sorted(pg)
    exact = None
    if cle and page and cle in CLES:
        exact = all(P.present(cle, page, mo) for mo in morceaux) if morceaux else None
    resultats.append((n, brut.replace("\n", " "), cle, page, exact, partout))

anglais = [r for r in resultats if r[5]]
non_trouves = [r for r in resultats if not r[5]]
print("passages entre guillemets :", len(resultats), "; trouvés dans au moins un PDF :", len(anglais),
      "; trouvés nulle part :", len(non_trouves))
print()
print("== Trouvés dans un PDF : ligne v3 | passage | citation la plus proche | à la page exacte ? | partout")
for n, b, c, p, e, pt in anglais:
    print("l. %d | %s | %s p. %s | %s | %s" % (n, b[:110], c, p, {True: "OUI", False: "NON", None: "?"}[e], pt))
print()
print("== Trouvés nulle part (français, code, titre, nom)")
for n, b, c, p, e, pt in non_trouves:
    print("l. %d | %s" % (n, b[:140]))
