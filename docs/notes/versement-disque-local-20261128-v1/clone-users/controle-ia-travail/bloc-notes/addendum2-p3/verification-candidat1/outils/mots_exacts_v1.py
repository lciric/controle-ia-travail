"""Contrôle mot à mot du candidat 1 de l'addendum 2 de P3 face au brouillon 5 et aux corrections de la contre-lecture 5.

Les mots exacts sont extraits des deux rapports (guillemets « » équilibrés, après une ancre), jamais recopiés à la main.
Espaces normalisés (toute suite de blancs = une espace) : un retour à la ligne dans un paragraphe Markdown se lit comme
une espace. Reconstruit le texte attendu (brouillon 5 + marqueurs + corrections + section « Contre-lecture » de la
session + ligne « Candidat 1 ») et le compare au candidat.

Usage : python -I -B mots_exacts_v1.py <brouillon5> <candidat> <rapport texte> <rapport code> <section proposée>
        <section de la session>
"""
import re
import sys
from pathlib import Path

b5, cand, rt, rc, sec_prop, sec_sess = (Path(p).read_text(encoding="utf-8") for p in sys.argv[1:7])


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def guillemets(texte, ancre, depart=0):
    """Contenu du premier « … » équilibré qui suit `ancre` (cherchée à partir de `depart`)."""
    i = texte.index(ancre, depart) + len(ancre)
    i = texte.index("«", i)
    prof, j = 0, i
    while True:
        c = texte[j]
        if c == "«":
            prof += 1
        elif c == "»":
            prof -= 1
            if prof == 0:
                return texte[i + 1:j].strip()
        j += 1


def section(texte, ident):
    i = texte.index(f"### {ident} ")
    j = texte.find("\n### ", i + 1)
    k = texte.find("\n## ", i + 1)
    fin = min(x for x in (j, k, len(texte)) if x > 0)
    return texte[i:fin]


T = {k: section(rt, f"VV3-texte-0{k}") for k in range(1, 8)}
C5 = section(rc, "VV3-code-05")
n_t02 = guillemets(T[2], "Remplacer la précision 14 par :")
n_t03 = guillemets(T[3], "insérer :")
n_t04 = guillemets(T[4], "(accents graves compris) par :")
n_t05 = guillemets(T[5], "Remplacer par :")
n_t06 = guillemets(T[6], "Remplacer par :")
n_t07 = guillemets(T[7], "insérer :")
a_c05 = guillemets(C5, "Dans la phrase proposée, remplacer")
n_c05 = guillemets(C5, "s) » par")
print("mots extraits :")
for nom, v in [("T02", n_t02), ("T03", n_t03), ("T04", n_t04), ("T05", n_t05), ("T06", n_t06), ("T07", n_t07),
               ("C05 ancien", a_c05), ("C05 nouveau", n_c05)]:
    print(f"  {nom} ({len(v)} car.) : {norm(v)[:70]}…")

# phrase de durée attendue : VV3-texte-04, dont le segment des imports est remplacé par les mots de VV3-code-05
seg_t04 = ("dont 3,2 à 3,4 s d'imports (surtout la bibliothèque de calcul tensoriel, tirée par "
           "`harnais.validation_reelle` : 2,05 à 2,15 s)")
assert norm(n_t04).count(seg_t04) == 1, "segment des imports absent de VV3-texte-04"
print("C05 ancien == segment de VV3-texte-04 :", norm(a_c05) == seg_t04,
      "(écart attendu : VV3-code-05 cite la phrase des notes, « 2,0 à 2,2 s »)")
duree = norm(n_t04).replace(seg_t04, norm(n_c05))

nc = norm(cand)
print("\nprésence dans le candidat (espaces normalisés) :")
for nom, v in [("T02", n_t02), ("T03", n_t03), ("T05", n_t05), ("T06", n_t06), ("T07", n_t07), ("durée T04+C05", duree)]:
    print(f"  {nom} : {'présent' if norm(v) in nc else 'ABSENT'} ({nc.count(norm(v))} fois)")

# reconstruction du texte attendu à partir du brouillon 5
e = norm(b5)


def remp(ancien, nouveau):
    global e
    a, n = norm(ancien), norm(nouveau)
    assert e.count(a) == 1, f"motif absent ou multiple : {a[:80]}"
    e = e.replace(a, n)


remp("`<<EMPREINTE_MODULE>>`", "`967270761c92ce3875695b8e5da5a985295c963b324dd120a31d09db663f132d`")
remp("`<<EMPREINTE_TESTS>>`", "`f9136b6dc5eebce6d9e9101fa910646b16fa544f0ee1d3a997030eb9319dbc07`")
remp("`<<NOMBRE_TESTS>>`", "`128`")
remp("<<SHA_TRAITEMENT_1>>", "dfce4ccaee074228b2873033201373322fe0005314ea88900863eec5001a1392")
remp("<<SHA_VERIFICATION_2>>", "65afdd6c7e23d6cba334442ff1b99ec7ef89a2d35e327d47b7d1cb98e7be1461")
remp("<<SHA_TRAITEMENT_2>>", "155e8fe173db2315a8f60afe61aa61cd72a0fcd4a65855cccdc0b1007e1734ca")
remp("`<<DUREE_MESUREE>>`", duree)                                                     # T04 + C05
remp("14. Un [SF] sans `principales` arrête avec un motif écrit, jamais par une exception nue (brouillon 5, CV2-10).",
     n_t02)                                                                              # T02
remp("garde sa valeur ponctuelle et ne fait pas taire le déclencheur (brouillon 5", "garde sa valeur ponctuelle " + n_t03 + " et ne fait pas taire le déclencheur (brouillon 5")   # T03, précision 2 seulement
remp("Règles déjà appliquées par le module là où le texte se taisait (contre-lecture du code, CC-texte-06) ; aucune ne "
     "change un nombre, une réserve ni le verrou :", n_t05)                              # T05
remp("les tests peuvent importer les aides de `tests/test_premier_test_ia_lecture.py`.", n_t06)   # T06
remp("(plus de 1 % : « échec » de la part, motif écrit).",
     "(plus de 1 % : « échec » de la part, motif écrit " + n_t07 + ").")               # T07
# T01 : l'entrée du code (jusqu'à la fin du fichier) remplacée par la section ; d'abord avec la section PROPOSÉE
debut = e.index("- **Contre-lecture du code** —")
assert e[debut:].endswith("`<<SHA_BROUILLON_CODE>>`."), "l'entrée du code n'est pas la fin du brouillon 5"
attendu_prop = e[:debut] + norm(sec_prop)
attendu_sess = e[:debut] + norm(sec_sess)
# ligne « Candidat 1 », insérée après la ligne « Brouillon 5 » de l'en-tête
i = nc.index("- Candidat 1 :")
j = nc.index("- Date (UTC) :")
ligne_c1 = nc[i:j].strip()
apres_b5 = "ni de B2. - Date (UTC) :"
assert attendu_sess.count(apres_b5) == 1
attendu_sess_c1 = attendu_sess.replace(apres_b5, "ni de B2. " + ligne_c1 + " - Date (UTC) :")
print("\ncandidat == brouillon 5 + marqueurs + corrections + section de la session + ligne « Candidat 1 » :",
      attendu_sess_c1 == nc)
# ce qui sépare la section de la session de la section proposée (mots)
import difflib
mp, ms = norm(sec_prop).split(" "), norm(sec_sess).split(" ")
print("\nsection proposée → section de la session (mots) :")
for op, a1, a2, b1, b2 in difflib.SequenceMatcher(None, mp, ms, autojunk=False).get_opcodes():
    if op != "equal":
        print(f"  {op} : « {' '.join(mp[a1:a2])} » → « {' '.join(ms[b1:b2])} »")
print("\nligne « Candidat 1 » :", ligne_c1)
