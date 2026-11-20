"""Contre-lecture du palier 0b, version 12 — contrôles mécaniques (contre-lecteur neuf, modèle O).

Aucun tirage, aucune pièce d'autorisation, aucun appel réseau. Lit :
- la v11, la v12, le jeu de remplacements, le différentiel du rédacteur, mon différentiel rejoué, la table extraite ;
- l'en-tête d'une COPIE de la v12, par `lire_en_tete_du_texte` du code v5 (seule fonction du code appelée).
Écrit sa sortie dans le fichier passé en dernier argument.
"""
import hashlib
import importlib
import json
import shutil
import sys

P = "/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/"
D = "/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/contre-lecture-palier-0b-v12/"
V11 = P + "preenregistrement-heritage-palier-0b-etage-processeur-v11.md"
V12 = P + "preenregistrement-heritage-palier-0b-etage-processeur-v12.md"
JEU = P + "remplacements-palier-0b-v11-v12-v1.json"
DIFF_R = P + "differentiel-palier-0b-v11-v12-v1.diff"
DIFF_M = D + "diff-v11-v12-rejoue.diff"
TABLE = P + "table-empreintes-code-v5.txt"
CODE_SRC = P + "code-v5/src"
COPIE = D + "copie-v12-pour-lecteur-d-en-tete.md"
COMMIT = "e308b84d68a85416fab1a80b0c116858d24b85a5"
PREFIXE = "- Commit du code d'analyse : "

sortie = []


def dire(*a):
    sortie.append(" ".join(str(x) for x in a))


def sha(b):
    return hashlib.sha256(b).hexdigest()


b11, b12 = open(V11, "rb").read(), open(V12, "rb").read()
t11, t12 = b11.decode("utf-8"), b12.decode("utf-8")
l11, l12 = t11.split("\n"), t12.split("\n")
dire("v11", sha(b11), "lignes", t11.count("\n"))
dire("v12", sha(b12), "lignes", t12.count("\n"))

# 1. lignes qui commencent par le préfixe ; lignes qui le contiennent
for nom, ls in (("v11", l11), ("v12", l12)):
    dire(nom, "lignes commençant par le préfixe :", sum(1 for x in ls if x.startswith(PREFIXE)),
         "; lignes le contenant :", sum(1 for x in ls if PREFIXE in x),
         "; lignes contenant « Commit du code d'analyse » :", sum(1 for x in ls if "Commit du code d'analyse" in x))

# 2. bloc qui suit la ligne du commit, à l'octet contre la table extraite
r = [i for i, x in enumerate(l12) if x.startswith(PREFIXE)][0]
i = r + 1
while l12[i].strip() != "```":
    i += 1
j = i + 1
while l12[j].strip() != "```":
    j += 1
bloc = l12[i + 1:j]
dire("ligne du commit (1-indexée) :", r + 1, "; ouverture ``` :", i + 1, "; fermeture ``` :", j + 1, "; lignes du bloc :", len(bloc))
dire("lignes entre la ligne du commit et l'ouverture :", [l12[k] for k in range(r + 1, i)])
dire("toutes les lignes du bloc commencent par deux espaces et pas trois :",
     all(x.startswith("  ") and not x.startswith("   ") for x in bloc))
sans_retrait = "\n".join(x[2:] for x in bloc) + "\n"
tb = open(TABLE, "rb").read()
dire("bloc sans retrait égal à l'octet à la table extraite :", sans_retrait.encode("utf-8") == tb, "; table", sha(tb))
dire("lignes de la table :", tb.decode().count("\n"), "; sous src/ :",
     sum(1 for x in tb.decode().splitlines() if x.split("  ", 1)[1].startswith("src/")))
dire("ligne du commit contient le commit entre accents graves :", f"`{COMMIT}`" in l12[r])
import re
dire("groupes de 40 hexadécimaux entre accents graves dans la ligne :", re.findall(r"`([0-9a-f]{40})`", l12[r]))

# 3. lecteur d'en-tête du verrou (code v5), sur une copie
shutil.copyfile(V12, COPIE)
dire("copie", sha(open(COPIE, "rb").read()))
sys.path = [CODE_SRC] + [p for p in sys.path if not p.endswith("/src") and p not in ("", ".")]
graines = importlib.import_module("controle_ia.heritage_etage_processeur_v1.graines")
dire("module importé depuis :", graines.__file__)
dire("empreinte du module graines.py :", sha(open(graines.__file__, "rb").read()))
c, table = graines.lire_en_tete_du_texte(COPIE)
dire("lecteur : commit lu =", c, "; égal au commit attendu :", c == COMMIT)
attendue = {}
for x in tb.decode().splitlines():
    e, ch = x.split("  ", 1)
    attendue[ch] = e
dire("lecteur : table lue, entrées =", len(table), "; égale à la table extraite :", table == attendue,
     "; sous src/ :", sum(1 for k in table if k.startswith("src/")))
dire("lecteur : graines journalisées pendant la lecture :", list(graines.JOURNAL), "; refus :", list(graines.REFUS))

# 4. différentiels : celui du rédacteur et le mien, en-têtes (deux premières lignes) ôtés
dr = open(DIFF_R, "rb").read().split(b"\n")
dm = open(DIFF_M, "rb").read().split(b"\n")
dire("différentiel du rédacteur égal au mien hors des deux lignes d'en-tête :", dr[2:] == dm[2:],
     "; lignes :", len(dr) - 1, len(dm) - 1)

# 5. lieux : chaque ligne changée de la v11 est-elle couverte par une ancre du jeu ? chaque ancre est-elle dans une ligne changée ?
jeu = json.load(open(JEU, encoding="utf-8"))
dire("remplacements dans le jeu :", len(jeu))
debut_ligne11 = [0]
for x in l11:
    debut_ligne11.append(debut_ligne11[-1] + len(x) + 1)


def ligne_de(pos, debuts):
    lo, hi = 0, len(debuts) - 1
    while lo < hi - 1:
        mid = (lo + hi) // 2
        if debuts[mid] <= pos:
            lo = mid
        else:
            hi = mid
    return lo + 1


couvertes = set()
for k, rmp in enumerate(jeu, 1):
    a = rmp["ancien"]
    n = t11.count(a)
    pos = t11.find(a)
    la, lb = ligne_de(pos, debut_ligne11), ligne_de(pos + len(a) - 1, debut_ligne11)
    couvertes.update(range(la, lb + 1))
    dire(f"rang {k} : ancre trouvée {n} fois ; lignes v11 {la}-{lb} ; neuf présent dans v12 {t12.count(rmp['neuf'])} fois ; "
         f"ancien {len(a)} car., neuf {len(rmp['neuf'])} car. ; début ancien {a[:70]!r}")
# lignes changées selon le différentiel
changees, n11 = set(), 0
for x in dm:
    s = x.decode("utf-8")
    if s.startswith("@@"):
        n11 = int(s.split()[1].split(",")[0][1:]) - 1
    elif s.startswith("---") or s.startswith("+++"):
        continue
    elif s.startswith("-"):
        n11 += 1
        changees.add(n11)
    elif s.startswith(" "):
        n11 += 1
dire("lignes de la v11 retirées par le différentiel :", len(changees))
dire("lignes retirées hors de toute ancre :", sorted(changees - couvertes))
dire("lignes d'ancre non retirées (ancre dans une ligne inchangée) :", sorted(couvertes - changees))
dire("hunks (en-têtes) :", [x.decode() for x in dm if x.startswith(b"@@")])

open(sys.argv[1], "w", encoding="utf-8").write("\n".join(sortie) + "\n")
