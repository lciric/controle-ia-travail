"""Écrit la version 8 du préenregistrement de la confrontation : la version 7 mot pour mot, son titre changé (« v7 » →
« v8 ») et une section ajoutée à la fin, qui inscrit pour les pilotes descriptifs que la v8 ne change ni la table de
lecture de H-E1, ni les seuils, ni les règles de lecture de la v7, avec les empreintes des archives fermées des pilotes.

Usage : python3 -I ecrire_confrontation_v8.py V7 V8 COURSES.json HEURE_UTC
COURSES.json : liste de {"pilote", "course", "branche", "commit", "ferme", "empreintes"} (empreintes sha256 complètes),
lues sur les compagnons `.sha256` poussés et recalculées sur les objets des branches (par l'appelant).
Refuse si V8 existe (R12), si l'empreinte de V7 n'est pas celle de la v7, ou si le diff touche autre chose.
"""
import difflib, hashlib, json, pathlib, sys

SHA_V7 = "74487a41fe29b4ad0e5688df9fb9fda815725cdd7521ee2a327694b2fa4ddf61"
v7, v8, courses_f, heure = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]), sys.argv[4]
if v8.exists():
    sys.exit(f"refus : {v8} existe déjà (R12)")
b7 = v7.read_bytes()
if hashlib.sha256(b7).hexdigest() != SHA_V7:
    sys.exit("refus : la v7 lue n'a pas l'empreinte 74487a41…")
t7 = b7.decode("utf-8")
lignes = t7.split("\n")
titre7 = lignes[0]
if "brouillon v7" not in titre7 or titre7.count("brouillon v7") != 1:
    sys.exit("refus : titre de la v7 inattendu")
titre8 = titre7.replace("brouillon v7", "brouillon v8")
courses = json.loads(courses_f.read_text(encoding="utf-8"))
for c in courses:
    for k in ("pilote", "course", "branche", "commit", "ferme", "empreintes"):
        if not c.get(k):
            sys.exit(f"refus : champ {k} manquant pour {c}")
    for k in ("ferme", "empreintes"):
        if len(c[k]) != 64 or any(ch not in "0123456789abcdef" for ch in c[k]):
            sys.exit(f"refus : empreinte {k} mal formée pour {c['course']}")
tableau = ["| pilote | course | branche (commit) | `ferme.tar.gz` | `EMPREINTES-pilote-v1.txt` |", "|---|---|---|---|---|"]
for c in courses:
    tableau.append(f"| {c['pilote']} | `{c['course']}` | `{c['branche']}` (`{c['commit'][:7]}`) | `{c['ferme']}` | `{c['empreintes']}` |")
section = f"""
## Inscription pour les pilotes descriptifs (v8 ; seul ajout à la v7)

Écrite par conv-audit le 25 octobre 2026 à {heure} UTC. Cette version 8 reprend la version 7
(`{SHA_V7}`) **mot pour mot** : seuls changent le titre (« v7 » devient « v8 ») et l'ajout de la
présente section, à la fin ; le diff mécanique de la v7 à la v8 est consigné à côté de ce texte
(`brouillon-confrontation-essaims-v8-diff-depuis-v7.txt`).

**Inscrit** (condition du moment de lecture des pilotes descriptifs : `pilote-gemini-organisme-v4-question-v1.md`, plan,
« jusqu'à ce qu'il soit inscrit que la v8 … » ; `pilote2-gemini-organisme-v5-2-v2.md`, plan § 3 ; le pilote 3, dont
les courses n'ont pas encore tourné, aura sa propre inscription dans une version suivante) : **la version 8 ne change ni la table de lecture de H-E1, ni les seuils, ni les règles de lecture de
la version 7.** Aucune section de la version 7 n'est modifiée.

**Écrit avant toute lecture** : à l'heure de cette inscription, conv-audit n'a lu aucun score, aucune réponse aux
tâches, aucun fichier fermé des pilotes ; les archives ci-dessous n'ont pas été ouvertes. Déclaration (texte du second
pilote, plan § 3) : aucun score des pilotes ne motive aucun changement de ce préenregistrement ni d'aucun préenregistrement
principal ; un changement ultérieur des règles de lecture de la v7 rouvrirait R1 pour les pilotes et serait écrit dans une
version nouvelle, avec ses raisons. Empreintes, lues sur les compagnons `.sha256` poussés et recalculées sur les objets
des branches :

""" + "\n".join(tableau) + "\n"
t8 = "\n".join([titre8] + lignes[1:])
if not t8.endswith("\n"):
    t8 += "\n"
t8 += section
diff = "".join(difflib.unified_diff(t7.splitlines(True), t8.splitlines(True), "v7", "v8", n=0))
moins = [l for l in diff.splitlines() if l.startswith("-") and not l.startswith("---")]
if moins != ["-" + titre7]:
    sys.exit(f"refus : le diff retire autre chose que le titre : {moins[:3]}")
v8.write_text(t8, encoding="utf-8")
(v8.parent / "brouillon-confrontation-essaims-v8-diff-depuis-v7.txt").write_text(diff, encoding="utf-8")
h8 = hashlib.sha256(v8.read_bytes()).hexdigest()
(v8.parent / (v8.name + ".sha256")).write_text(f"{h8}  {v8.name}\n", encoding="utf-8")
print(f"v8 écrite : {v8.name} {h8} ; {len(courses)} courses inscrites ; lignes retirées : 1 (titre)")
