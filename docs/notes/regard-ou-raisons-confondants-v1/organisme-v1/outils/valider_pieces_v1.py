"""Valide, sans appel, les pièces servies de la course « Regard ou raisons » de l'atelier d'idées, avec le code réel de
l'orchestrateur (clone en lecture, jamais modifié) :

1. le fond de `question-v1.md` (bloc entre guillemets français, de « Le directeur demande » à « changer d'avis. ») se
   retrouve **octet pour octet** dans la question de l'organisme ;
2. la question et les faits traversent le caviardage de l'orchestrateur sans rien perdre ;
3. `charger_temoins` accepte les quatre témoins (quatre classes imposées) ; aucun ne déclenche la garde lexicale ;
4. aucun identifiant de modèle Claude dans les pièces de texte neuves.

Usage : /usr/local/bin/python3 -I -B -X pycache_prefix=<dossier hors du clone> valider_pieces_v1.py ORCH DOSSIER_NOTES
(DOSSIER_NOTES = docs/notes/regard-ou-raisons-confondants-v1). Code de sortie 0 si tout tient, 1 sinon.
"""
import hashlib
import json
import os
import re
import sys

orch, notes = sys.argv[1], os.path.realpath(sys.argv[2])
sys.path.insert(0, orch)
from pole import ideation_v2 as idn  # noqa: E402
from pole.caviardage import caviarder  # noqa: E402

org = os.path.join(notes, "organisme-v1")
echecs = []


def lire(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        return f.read()


# 1. fond recopié mot pour mot
source = lire(os.path.join(notes, "question-v1.md"))
debut, fin = source.index("« Le directeur demande"), source.index("changer d'avis. »") + len("changer d'avis. »")
bloc = source[debut:fin]
question = lire(os.path.join(org, "question-organisme-regard-ou-raisons-v1.md"))
ok = bloc in question
print(f"fond recopié octet pour octet : {ok} ({len(bloc)} caractères, {len(bloc.encode('utf-8'))} octets)")
if not ok:
    echecs.append("fond de la question non recopié mot pour mot")

# 2. caviardage sans perte
for nom, chemin in (("question", os.path.join(org, "question-organisme-regard-ou-raisons-v1.md")),
                    ("faits", os.path.join(notes, "faits-v1.md"))):
    t = lire(chemin)
    c, n = caviarder(t)
    print(f"caviardage de {nom} : {n} remplacement(s), {len(t)} caractères, "
          f"sha256 {hashlib.sha256(open(chemin, 'rb').read()).hexdigest()}")
    if n or c != t:
        echecs.append(f"le caviardage change {nom}")

# 3. témoins
p = os.path.join(org, "temoins-organisme-regard-ou-raisons-v1.json")
liste = {p: hashlib.sha256(open(p, "rb").read()).hexdigest()}
temoins = idn.charger_temoins(p, liste)
print("orchestrateur : charger_temoins OK,", len(temoins), "témoins, classes", sorted(x["temoin"]["classe"] for x in temoins))
for x in temoins:
    s = idn.signaux_niveau_methode(idn.vue_servie(x))
    print(" ", x["temoin"]["classe"], "|", x["nom"], "| taille servie", idn.taille_servie(x), "| signaux :", s)
    if s:
        echecs.append("témoin signalé : " + x["nom"])
if sorted(x["temoin"]["classe"] for x in temoins) != sorted(idn.CLASSES_TEMOIN) or len(temoins) != 4:
    echecs.append("quatre témoins, un par classe, attendus")

# 4. aucun identifiant de modèle Claude dans les pièces de texte neuves
motif = re.compile(r"(?i)claude-[a-z0-9]|\b(opus|sonnet|haiku|fable)\b")
for nom in sorted(os.listdir(org)):
    if nom.endswith((".md", ".json")) and os.path.isfile(os.path.join(org, nom)):
        trouves = sorted(set(m.group(0) for m in motif.finditer(lire(os.path.join(org, nom)))))
        print(f"identifiants de modèle Claude dans {nom} : {trouves}")
        if trouves:
            echecs.append(f"identifiant de modèle Claude dans {nom}")

print("échecs :", echecs)
raise SystemExit(1 if echecs else 0)
