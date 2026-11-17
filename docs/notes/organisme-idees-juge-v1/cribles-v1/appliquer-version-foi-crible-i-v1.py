"""Version qui fera foi, v1, du préenregistrement du crible (i), écrite sur le brouillon 3 par couples « ancien → nouveau ».

Seuls changent le titre, l'en-tête (puce de la version qui fera foi), le statut et la section « Contre-lecture » (entrée du
tour 3 ajoutée, « Tour suivant » réécrit). Les prédictions I-1 à I-8 (gelées, `gel-predictions-crible-i-brouillon1.txt`) ne
changent pas. Les devis (`devis-crible-i-brouillon2.py` et sa sortie) sont ceux du brouillon 2, déjà refaits sur les coûts
et durées mesurés du pilote (verdict v2, « Pour les cribles ») par la règle écrite de [CRIBLE-V] : inchangés.

Gardes (comme `appliquer-version-foi-crible-iii-v1.py`) : empreinte de la pièce de départ et du rapport du tour 3 ; nombre
de couples ; chaque « ancien » figure exactement une fois ; aucun chevauchement ; chaque « nouveau » figure dans la cible ;
aucune ligne des prédictions I-1 à I-8 touchée ; cible jamais écrasée (mode « x ») ; validateur
`controle_ia.prereg.problemes` rejoué sur une copie temporaire, liste vide exigée ; aucun repli silencieux. Deux couples sont
donnés par leurs bornes : le statut et le « À faire ».
Usage : python3 -I appliquer-version-foi-crible-i-v1.py
"""
import hashlib
import os
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
SOURCE = os.path.join(ICI, "crible-i-brouillon3.md")
SOURCE_SHA = "888fb001c4d349d8f9d65d91dcfce4c6ee6a0753108973393d75815778f05cbe"
PIECES = {
    os.path.join(ICI, "contre-lecture-crible-i-tour3-v1.md"): "4f3a8cab6362a5ee7de8d2a2f1898f2ee3e27016d6253ec1f63ee6bf8fff39d6",
}
CIBLE = os.path.join(ICI, "crible-i-version-foi-v1.md")
HEURE = "06:36Z"


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
`contre-lecture-crible-i-tour3-v1.md`, « Contre-lecture », entrée 3), variante « crédits de Claude au maximum ».
**Prédictions I-1 à I-8 gelées** dans leur rédaction du brouillon 1
(`gel-predictions-crible-i-brouillon1.txt`, scellé, 2026-11-17T00:53:43Z) : **inchangées**, leurs « Raisons » aussi.
**Seuls changent** le titre, l'en-tête (puce de la version qui fera foi), le statut et la section « Contre-lecture »
(entrée du tour 3 ajoutée, « Tour suivant » réécrit). Les devis (`devis-crible-i-brouillon2.py` et sa sortie), toutes les
prédictions, critères de lecture gelés, seuils, règles et listes d'arrêt sont ceux du brouillon 3, inchangés.
**Restes avant la recopie sous `prereg/` par `sceller_prereg`** (aucun ne se fait ici ; aucun ne change un seuil ni une règle) :
(a) **calcul scellé de la puissance à + 4 mondes** (non fait, tours 1 et 2 de contre-lecture) ; (b) choix F1, F4, F5, F7 du
tour 1 (non tranchés, section « Contre-lecture ») ; (c) ligne datée de `registres/decisions.md` confirmant le gel des prédictions
(I-1 gelée avec « ≥ + 4 » même si P1 ne peut l'établir à ce seuil ; zones de I-5, I-6 et I-7 ajoutées après le gel) ;
(d) **sonde neuve** (section « Devis ») ; (e) un **tour différentiel** par un lecteur neuf (R2). Ce texte est scellé comme pièce
(empreinte compagnon, R6), non comme préenregistrement en vigueur. Aucune dépense, aucun appel de modèle, aucun monde tiré.
L'accord de dépense GO-2026-11-15-06 (enveloppe des cinq cribles : 247,20 USD attendus, 1 275 au pire, crédits de Claude employés
au maximum) **n'autorise encore aucun appel** : la ligne « calcul » propre à ce crible s'inscrit par la mère sur un devis refait
et contre-lu (part sur crédits et part hors crédits séparées), citant ce mot. **Le dessin neuf (une donnée d'épisodes dans la vue
des proposeurs) est essayé, non adopté** (GO-2026-11-15-06 : « essayés, non adoptés ») : toute adoption reste un nœud de Lazar.
Le devis de ce texte est **celui du brouillon 2** (correction M3), déjà refait sur les coûts et durées mesurés du pilote
(verdict v2, « Pour les cribles »), par la règle écrite de [CRIBLE-V] ; seule la sonde neuve le corrigera encore.
Validateur `controle_ia.prereg.problemes` : aucun défaut formel (vérifié par le programme d'application avant l'écriture du
fichier)."""

ENTREE3_ET_TOUR = """- **Contre-lecture 3** (R2, tour 3, différentiel, sur le brouillon 3) — sous-agent neuf, d'un autre modèle que
  l'auteur, qui dit n'avoir écrit aucune des pièces lues. Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-i-brouillon3.md`,
  `888fb001c4d349d8f9d65d91dcfce4c6ee6a0753108973393d75815778f05cbe` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-i-tour3-v1.md`,
  `4f3a8cab6362a5ee7de8d2a2f1898f2ee3e27016d6253ec1f63ee6bf8fff39d6`. Verdict : « **scellable** » (aucune correction exigée).
  Fidélité de m7 vérifiée ; symétrie des trois bras à l'étage 2 rétablie ; validateur relancé : aucun défaut ;
  devis, enveloppe, durées non touchés. Remarques facultatives : étage 4, et les F1, F4, F5, F7 toujours ouverts.
  Points pour la mère : gel des prédictions à confirmer, enveloppe des cinq cribles, GO par ligne.
  **Traitement dans cette version qui fera foi** (écrite le 2026-11-17, à HEURE, `date -u`, par un rédacteur neuf,
  au moyen du programme `appliquer-version-foi-crible-i-v1.py`, même dossier, scellé à côté ; chaque « ancien »
  figure une seule fois dans le brouillon 3, vérifié par le programme) : aucune correction exigée au tour 3.

**Tour suivant** (R2) : tour différentiel sur cette version qui fera foi, par un sous-agent neuf d'un **autre modèle** que
l'auteur, qui n'a écrit ni les brouillons 1 à 3, ni aucun rapport de contre-lecture, ni ce texte. **Ce qui a changé** depuis
le brouillon 3 : titre, en-tête (puce de la version qui fera foi), statut et cette section ; **rien d'autre** (ni les
prédictions, ni les devis, ni les critères de lecture, ni les seuils, ni les listes d'arrêt). Différentiel
`diff-crible-i-b-vers-foi-v1.txt` (scellé). **Fichiers à lui donner explicitement** : ce texte ; le brouillon 3
(`888fb001…`) ; le différentiel ; le programme `appliquer-version-foi-crible-i-v1.py` (scellé) ; le rapport du tour 3
(`4f3a8cab…`) ; pour les remarques ouvertes, les listes des tours 1 et 2."""


COUPLES = [
    ("T01", "— brouillon 3 (variante « crédits de Claude au maximum »)\n",
     "— version qui fera foi, v1 (variante « crédits de Claude au maximum »)\n"),
    ("T02", "  celui du brouillon 2.\n- **Ordre de rédaction, déclaré**",
     "  celui du brouillon 2.\n"
     "- **Version qui fera foi, v1** : écrite le 2026-11-17, à HEURE (`date -u`) par un rédacteur neuf (identité dite en\n"
     "  conversation seulement), qui n'a écrit ni les brouillons 1 à 3 ni aucun rapport de contre-lecture, sur le brouillon 3\n"
     "  (`888fb001c4d349d8f9d65d91dcfce4c6ee6a0753108973393d75815778f05cbe`), au moyen du programme\n"
     "  `appliquer-version-foi-crible-i-v1.py` (même dossier, scellé) ; dépôt lu sur `main` (tête `05cd22aa`) ; aucun commit,\n"
     "  aucune poussée, aucun appel, aucune dépense. Les devis (`devis-crible-i-brouillon2.py` et sa sortie) sont ceux du\n"
     "  brouillon 2, inchangés. Différentiel contre le brouillon 3 : `diff-crible-i-b-vers-foi-v1.txt` (scellé).\n"
     "  Rien d'autre que ce que dit le statut ne change.\n"
     "- **Ordre de rédaction, déclaré**"),
    ("T03", borne("**Statut.** Brouillon 3, **contre-lu aux tours 1 et 2**",
                  "avec leurs empreintes)."), STATUT),
    ("T04", borne("**À faire** (R2) : tour 3",
                  "remplacée)."), ENTREE3_ET_TOUR),
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

debut_pred = source.index("| I-1 |")
fin_pred = source.index("| I-8 |")
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
    essai = os.path.join(dossier, "crible-i-version-foi-v1.md")
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
