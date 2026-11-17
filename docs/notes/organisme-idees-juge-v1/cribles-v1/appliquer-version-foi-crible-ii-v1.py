"""Version qui fera foi, v1, du préenregistrement du crible (ii), écrite sur le brouillon 3 par couples « ancien → nouveau ».

Seuls changent le titre, l'en-tête (puce de la version qui fera foi), le statut et la section « Contre-lecture » (entrée du
tour 3 ajoutée, « Tour suivant » ajouté). Les prédictions II-1 à II-7 ne changent pas. Les devis
(`devis-crible-ii-brouillon1.py` et sa sortie) sont ceux du brouillon 1, déjà faits directement sur les coûts et durées
mesurés du pilote ([VERDICT-PC]) par les règles de [CRIBLE-V] : inchangés.

Gardes (comme `appliquer-version-foi-crible-iii-v1.py`) : empreinte de la pièce de départ et du rapport du tour 3 ; nombre
de couples ; chaque « ancien » figure exactement une fois ; aucun chevauchement ; chaque « nouveau » figure dans la cible ;
aucune ligne des prédictions II-1 à II-7 touchée ; cible jamais écrasée (mode « x ») ; validateur
`controle_ia.prereg.problemes` rejoué sur une copie temporaire, liste vide exigée ; aucun repli silencieux. Un couple est
donné par ses bornes : le statut.
Usage : python3 -I appliquer-version-foi-crible-ii-v1.py
"""
import hashlib
import os
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
SOURCE = os.path.join(ICI, "crible-ii-brouillon3.md")
SOURCE_SHA = "c837356b3df8648a214449293a0d138e17513b13d2e037a6d67303a743fb1201"
PIECES = {
    os.path.join(ICI, "contre-lecture-crible-ii-tour3-v1.md"): "9f257587e625f348eb06b11f0b65ebf743ea8ee1af5128e4922e1ae23b0160b9",
}
CIBLE = os.path.join(ICI, "crible-ii-version-foi-v1.md")
HEURE = "06:45Z"


def arret(msg):
    sys.stderr.write("ARRÊT : " + msg + "\n")
    sys.exit(2)


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


source = open(SOURCE, encoding="utf-8").read()


def borne(debut, fin):
    """« ancien » donné par ses bornes : de `debut` (unique) à la fin de `fin` (unique, après `debut`)."""
    if source.count(debut) != 1 or source.count(fin) != 1:
        arret(f"borne non unique : {debut[:40]!r} ou {fin[:40]!r}")
    i, j = source.index(debut), source.index(fin)
    if j < i:
        arret("bornes dans le désordre")
    return source[i:j + len(fin)]


STATUT = """**Statut.** **Version qui fera foi, v1**, écrite sur le brouillon 3 (jugé « scellable » au tour 3,
`contre-lecture-crible-ii-tour3-v1.md`, « Contre-lecture », entrée 3), variante « crédits de Claude au maximum ».
**Prédictions II-1 à II-7 inchangées** dans leur rédaction du brouillon 1. **Seuls changent** le titre, l'en-tête (puce de la
version qui fera foi), le statut et la section « Contre-lecture » (entrée du tour 3 ajoutée, « Tour suivant » ajouté). Les devis
(`devis-crible-ii-brouillon1.py` et sa sortie), toutes les prédictions, critères de lecture gelés, seuils, règles et listes
d'arrêt sont ceux du brouillon 3, inchangés. Écrit après le verdict du pilote MR-2 v14 : les attendus du devis sont faits
**directement** sur les coûts et durées mesurés du pilote ([VERDICT-PC]) par les règles de [CRIBLE-V] (moyenne de tous les
appels, pires cas aux plafonds) ; les prédictions sont écrites **sans donnée de proposeur sur la couverture des composantes
comptées, hors la classe des conditionnelles** (le pilote ne la mesure pas par appel ; seuls son témoin positif et le résultat
principal sont lus : aucun des 14 appels répondus ne porte une conditionnelle entière, x = 0 ; inchangé).
**Restes avant la recopie sous `prereg/` par `sceller_prereg`** (aucun ne se fait ici ; aucun ne change un seuil ni une règle) :
(a) **point de faisabilité à trancher avant tout code** (« Choix et doutes », point 3 : les cartes des pairs ne tiennent pas dans
le texte servi sous la configuration v12 sans retirer des épisodes ; à la mère et à Lazar) ; (b) remarques facultatives des
tours 1 et 2 (non appliquées) ; (c) un **tour différentiel** par un lecteur neuf (R2). Ce texte est scellé comme pièce (empreinte
compagnon, R6), non comme préenregistrement en vigueur. Aucune dépense, aucun appel de modèle, aucun monde tiré. L'accord
GO-2026-11-15-06 (enveloppe des cinq cribles, crédits de Claude employés au maximum) **n'autorise encore aucun appel** : la ligne
« calcul » de ce crible s'inscrit par la mère sur un devis contre-lu, dans l'enveloppe. Le dessin neuf (des cartes de pairs dans
la vue) est **essayé, non adopté** (l. 339 ; [NOTE] § 7, point 3) : toute adoption dans l'organisme reste un nœud de Lazar.
Validateur `controle_ia.prereg.problemes` : aucun défaut formel (vérifié par le programme d'application avant l'écriture du
fichier)."""

ENTREE3_ET_TOUR = """- **Contre-lecture 3** (R2, tour 3, différentiel, sur le brouillon 3) — sous-agent neuf, d'un autre modèle que
  l'auteur, qui dit n'avoir écrit aucune des pièces lues. Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-ii-brouillon3.md`,
  `c837356b3df8648a214449293a0d138e17513b13d2e037a6d67303a743fb1201` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-ii-tour3-v1.md`,
  `9f257587e625f348eb06b11f0b65ebf743ea8ee1af5128e4922e1ae23b0160b9`. Verdict : « **scellable** » (aucune correction exigée).
  Quatre couples (m1.1, m1.2, m2.1, m3.1) du tour 2 appliqués fidèlement ; validateur relancé : aucun défaut ;
  devis, enveloppe, durées non touchés. Remarques facultatives des tours 1 et 2 toujours non appliquées. Points pour
  la mère : nœud de faisabilité, enveloppe des cinq cribles, solde de crédits.
  **Traitement dans cette version qui fera foi** (écrite le 2026-11-17, à HEURE, `date -u`, par un rédacteur neuf,
  au moyen du programme `appliquer-version-foi-crible-ii-v1.py`, même dossier, scellé à côté ; chaque « ancien »
  figure une seule fois dans le brouillon 3, vérifié par le programme) : aucune correction exigée au tour 3.

**Tour suivant** (R2) : tour différentiel sur cette version qui fera foi, par un sous-agent neuf d'un **autre modèle** que
l'auteur, qui n'a écrit ni les brouillons 1 à 3, ni aucun rapport de contre-lecture, ni ce texte. **Ce qui a changé** depuis
le brouillon 3 : titre, en-tête (puce de la version qui fera foi), statut et cette section ; **rien d'autre** (ni les
prédictions, ni les devis, ni les critères de lecture, ni les seuils, ni les listes d'arrêt). Différentiel
`diff-crible-ii-b-vers-foi-v1.txt` (scellé). **Fichiers à lui donner explicitement** : ce texte ; le brouillon 3
(`c837356b…`) ; le différentiel ; le programme `appliquer-version-foi-crible-ii-v1.py` (scellé) ; le rapport du tour 3
(`9f257587…`) ; pour les remarques ouvertes, les listes des tours 1 et 2."""


COUPLES = [
    ("T01", "— brouillon 3 (variante « crédits de Claude au maximum »)\n",
     "— version qui fera foi, v1 (variante « crédits de Claude au maximum »)\n"),
    ("T02", "  l'annexe A) ne change.\n- Nombres neufs",
     "  l'annexe A) ne change.\n"
     "- **Version qui fera foi, v1** : écrite le 2026-11-17, à HEURE (`date -u`) par un rédacteur neuf (identité dite en\n"
     "  conversation seulement), qui n'a écrit ni les brouillons 1 à 3 ni aucun rapport de contre-lecture, sur le brouillon 3\n"
     "  (`c837356b3df8648a214449293a0d138e17513b13d2e037a6d67303a743fb1201`), au moyen du programme\n"
     "  `appliquer-version-foi-crible-ii-v1.py` (même dossier, scellé) ; dépôt lu sur `main` (tête `05cd22aa`) ; aucun commit,\n"
     "  aucune poussée, aucun appel, aucune dépense. Les devis (`devis-crible-ii-brouillon1.py` et sa sortie) sont ceux du\n"
     "  brouillon 1, inchangés. Différentiel contre le brouillon 3 : `diff-crible-ii-b-vers-foi-v1.txt` (scellé).\n"
     "  Rien d'autre que ce que dit le statut ne change.\n"
     "- Nombres neufs"),
    ("T03", borne("**Statut.** **Brouillon 3**, contre-lu deux fois",
                  "comme pièce de\ntravail)."), STATUT),
    ("T04", "aucun mot ne change.\n\n## Annexe A",
     "aucun mot ne change.\n\n" + ENTREE3_ET_TOUR + "\n\n## Annexe A"),
]
NOMBRE_ATTENDU = 4

if HEURE.startswith("@@"):
    arret("heure de fin non inscrite")
COUPLES = [(i, a, n.replace("HEURE", HEURE)) for i, a, n in COUPLES]
if not os.path.isfile(os.path.join(DEPOT, "src", "controle_ia", "prereg.py")):
    arret(f"racine du dépôt introuvable : {DEPOT}")
if sha(SOURCE) != SOURCE_SHA:
    arret(f"empreinte différente : {SOURCE}")
for chemin, attendu in PIECES.items():
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
for chemin in (CIBLE, CIBLE + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")
if len(COUPLES) != NOMBRE_ATTENDU or len({c[0] for c in COUPLES}) != NOMBRE_ATTENDU:
    arret("nombre de couples ou identifiants inattendus")

debut_pred = source.index("| II-1 |")
fin_pred = source.index("| II-7 |")
fin_pred = source.index("\n", fin_pred)
places = []
for ident, ancien, nouveau in COUPLES:
    n = source.count(ancien)
    if n != 1:
        arret(f"{ident} : « ancien » trouvé {n} fois dans la pièce de départ (une seule exigée)")
    debut = source.index(ancien)
    if debut < fin_pred and debut + len(ancien) > debut_pred:
        arret(f"{ident} touche la table des prédictions gelées")
    places.append((debut, debut + len(ancien), ident, ancien, nouveau))
places.sort()
for p, q in zip(places, places[1:]):
    if q[0] < p[1]:
        arret(f"chevauchement entre {p[2]} et {q[2]}")
morceaux, curseur = [], 0
for debut, fin, ident, ancien, nouveau in places:
    morceaux.append(source[curseur:debut])
    morceaux.append(nouveau)
    curseur = fin
morceaux.append(source[curseur:])
texte = "".join(morceaux)
for ident, ancien, nouveau in COUPLES:
    if nouveau not in texte:
        arret(f"{ident} : « nouveau » absent de la cible")
if source[debut_pred:fin_pred] not in texte:
    arret("table des prédictions changée")

with tempfile.TemporaryDirectory() as dossier:
    essai = os.path.join(dossier, "crible-ii-version-foi-v1.md")
    with open(essai, "w", encoding="utf-8") as f:
        f.write(texte)
    py = os.path.join(DEPOT, ".venv", "bin", "python")
    r = subprocess.run([py, "-c", "import sys; from controle_ia.prereg import problemes; p = problemes(sys.argv[1]); "
                        "print(p); sys.exit(1 if p else 0)", essai],
                       cwd=DEPOT, env={"PYTHONPATH": os.path.join(DEPOT, "src"), "PATH": "/usr/bin:/bin"},
                       capture_output=True, text=True)
    if r.returncode != 0:
        arret("validateur : " + (r.stdout + r.stderr).strip())

with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(texte)
print(f"{len(COUPLES)} couples appliqués ; cible écrite : {CIBLE}")
print("empreinte de la cible :", sha(CIBLE))
