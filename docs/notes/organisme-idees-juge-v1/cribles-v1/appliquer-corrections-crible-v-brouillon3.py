"""Brouillon 3 du préenregistrement du crible (v) : application des corrections du tour 2 de contre-lecture.

Couples « ancien → nouveau » : les 23 couples des corrections T2-1 à T2-13 sont lus dans le rapport de contre-lecture
lui-même (bloc entre clôtures nommé `T2-…`, ligne « ANCIEN: », puis « NOUVEAU: » et ses lignes de suite jusqu'à la
clôture : une ligne de suite est une ligne de table de plus), sans retouche ; s'y ajoutent des couples propres, chacun
nommé et déclaré dans la section « Contre-lecture » de la cible : titre, en-tête, statut, validateur, tête de la
section « Contre-lecture », liste « À trancher en priorité » dite périmée, entrée « Contre-lecture 2 ».
Gardes : empreinte de la pièce de départ et du rapport ; 23 couples exactement dans le rapport, noms attendus ; chaque
« ancien » figure exactement une fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; chaque
« nouveau » présent dans la cible ; la cible (et son compagnon) ne doit pas exister (ouverture en mode « x ») ; aucun
repli silencieux.
Bibliothèque standard seule ; aucun appel, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-v-brouillon3.py [--essai DOSSIER]
  (--essai : écrit la cible dans DOSSIER, dossier de travail jetable, pour la contrôler avant l'écriture réelle)
"""
import hashlib
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "crible-v-brouillon2.md")
SOURCE_SHA = "05ce58137d0700c493f76d34caf8605fe604942ff868350801baaeaf70948593"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-v-tour2-v1.md")
RAPPORT_SHA = "c04b8feede2540dbf85f7dd22741b3cfcb157d6a5ebc7a9c99dd8239611cf556"
NOM_CIBLE = "crible-v-brouillon3.md"
NOM_PROGRAMME = "appliquer-corrections-crible-v-brouillon3.py"
NOMS_RAPPORT = ["T2-01a", "T2-01b", "T2-01c", "T2-01d", "T2-01e",
                "T2-02a", "T2-02b", "T2-02c", "T2-02d", "T2-02e", "T2-02f",
                "T2-03a", "T2-03b", "T2-04", "T2-05", "T2-06", "T2-07", "T2-08", "T2-09",
                "T2-10", "T2-11", "T2-12", "T2-13"]


def arret(msg):
    sys.stderr.write("ARRÊT : " + msg + "\n")
    sys.exit(2)


def sha(chemin):
    with open(chemin, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


# 0. Dossier de la cible.
args = sys.argv[1:]
if args == []:
    DOSSIER = ICI
elif len(args) == 2 and args[0] == "--essai":
    DOSSIER = os.path.abspath(args[1])
    if DOSSIER == ICI or not os.path.isdir(DOSSIER):
        arret(f"dossier d'essai invalide : {DOSSIER}")
else:
    arret(f"arguments illisibles : {args!r}")
CIBLE = os.path.join(DOSSIER, NOM_CIBLE)

# 1. Empreintes des entrées ; cible absente.
for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA)):
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
for chemin in (CIBLE, CIBLE + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")

with open(SOURCE, encoding="utf-8") as f:
    source = f.read()
with open(RAPPORT, encoding="utf-8") as f:
    rapport = f.read()

# 2. Couples du rapport : ligne « `T2-…` », clôture, « ANCIEN: », « NOUVEAU: » et ses lignes de suite, clôture.
couples = []
lignes = rapport.splitlines()
i = 0
while i < len(lignes):
    m = re.fullmatch(r"`(T2-\d\d[a-z]?)`", lignes[i])
    if not m:
        if lignes[i].startswith("ANCIEN: ") or lignes[i].startswith("NOUVEAU: "):
            arret(f"ligne ANCIEN ou NOUVEAU hors d'un bloc nommé, ligne {i + 1} du rapport")
        i += 1
        continue
    nom = m.group(1)
    if lignes[i + 1] != "```" or not lignes[i + 2].startswith("ANCIEN: ") or not lignes[i + 3].startswith("NOUVEAU: "):
        arret(f"bloc {nom} mal formé, ligne {i + 1} du rapport")
    ancien = lignes[i + 2][len("ANCIEN: "):]
    nouveau = [lignes[i + 3][len("NOUVEAU: "):]]
    j = i + 4
    while j < len(lignes) and lignes[j] != "```":
        if lignes[j].startswith("ANCIEN: ") or lignes[j].startswith("NOUVEAU: "):
            arret(f"bloc {nom} : second ANCIEN ou NOUVEAU, ligne {j + 1} du rapport")
        nouveau.append(lignes[j])
        j += 1
    if j >= len(lignes):
        arret(f"bloc {nom} sans clôture")
    couples.append((nom, ancien, "\n".join(nouveau)))
    i = j + 1
if [n for n, _, _ in couples] != NOMS_RAPPORT:
    arret(f"couples lus dans le rapport : {[n for n, _, _ in couples]} ; attendus : {NOMS_RAPPORT}")

# 3. Heure lue par `date -u` au moment de l'écriture (le scellement suit aussitôt).
heure = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True, check=True).stdout.strip()
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", heure):
    arret(f"heure illisible : {heure!r}")

# 4. Couples propres (déclarés dans la section « Contre-lecture » de la cible).
ENTREE_CL2 = f"""

- **Contre-lecture 2** (tour 2, sur le brouillon 2) : sous-agent neuf du modèle C, qui n'a écrit ni ce texte, ni le
  brouillon 1, ni les corrections du brouillon 2, ni [NOTE], ni [PILOTE], ni le code du pilote, ni le rapport du tour 1 ;
  lecture de 13:49:05Z à 13:57:37Z. Rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-v-tour2-v1.md`, empreinte
  `{RAPPORT_SHA}` ; brouillon relu : `crible-v-brouillon2.md`, empreinte
  `{SOURCE_SHA}`. Verdict : **corrections** (4 majeures T2-1 à T2-4, 9 mineures T2-5 à T2-13,
  5 remarques facultatives O-1 à O-5) ; aucun « a_refaire » ; application du tour 1 jugée fidèle ; validateur sans défaut.
  - **Application** : par un rédacteur neuf (modèle C ; il n'a écrit ni le brouillon 1, ni le brouillon 2, ni aucun des deux
    rapports, ni aucune pièce citée), au moyen du programme `{NOM_PROGRAMME}` (même dossier, empreinte dans son compagnon
    `.sha256`) : les 23 couples « ancien → nouveau » des corrections T2-1 à T2-13 (T2-01a à T2-13) sont lus dans le rapport
    lui-même et appliqués sans retouche ; chaque « ancien » vérifié présent une seule fois dans le brouillon 2 ; aucun
    chevauchement ; cible neuve ; écriture le {heure} (`date -u`). Aucun appel de modèle, aucune dépense, aucune machine,
    aucune donnée lue (rien sous `diag/`, `runs/`, `donnees/` ; relevé de v67 et sortie du pilote non ouverts).
  - **Réponse point par point** :
    - T2-1 (monde complet, minimum, 24 mondes) : **acceptée**, par la voie que le rapport recommande (cinq couples
      T2-01a à T2-01e) : « monde complet » = au moins un appel répondu dans chacune des deux moitiés, gelé dès ce texte ;
      couvertures, règle et dollars sur les appels répondus du monde, les mêmes pour tous les bras ; « monde à quatre
      appels » passé en sensibilité ; minimum 0,8 × N gelé, seule sa probabilité d'être atteint recalculée, à titre
      d'information ; taux du pilote lu sur les comptes d'appels seuls, tout appel du pilote plus long que B_a compté en
      échec. L'autre voie (minimum absolu de 16) n'est pas prise : elle relève d'un mot de la mère (point pour la mère 2).
    - T2-2 (« 20 » en dur, garde B_a) : **acceptée** (six couples T2-02a à T2-02f ; ligne d'arrêt neuve « appel plus long
      que B_a », avec son essai sain et son artefact). **Réserve pour le tour 3** : d'autres « 20 » restent écrits pour
      N = 20, que le rapport ne demande pas de changer et que ce tour ne touche pas (« rien d'autre ne change ») : « En dix
      lignes », points 2 et 9 ; V1 (« sur 20 », remarque O-4) ; « Seuil » (« k_R ≤ 12 ou 13 sur 20 ») ; table du devis,
      lignes de GO et estimation de durée (montants et durées à refaire sur le devis mesuré) ; essai sain « 20 mondes
      conformes » de la liste d'arrêt.
    - T2-3 (sensibilité à archive fictive contre la ligne « fonction de décision ») : **acceptée** (deux couples : fonction
      distincte, exécutée après la sortie principale, k_R et S_R seuls ; mutation ajoutée au banc).
    - T2-4 (partie A et liste des retenues) : **acceptée** (un couple). Les noms de champs (`retenues`, `promue`, rejet,
      mort) sont à vérifier par le code avant l'essai sain (point pour la mère 7).
    - T2-5 à T2-13 : **acceptées**, un couple chacune, sans retouche.
    - Calculs que le rapport demande « à refaire par programme et à recopier en annexe » (loi binomiale exacte de T2-1,
      puissance à 24 mondes, épargne de T2-6, coûts de T2-13) : **non recopiés ici** (aucun couple ne les porte) ; laissés à
      la version qui fera foi, avec ceux de C-02 et C-05 (annexe A).
    - Remarques facultatives O-1 à O-5 : **non appliquées** (non exigées ; consigne de ce tour bornée aux corrections) ;
      O-1 vaut pour ce tour-ci : les couples propres sont nommés ci-dessous.
    - Couples propres de ce tour : « titre » (brouillon 3) ; « en-tete » (ligne « Brouillon 3 » de l'en-tête) ; « statut » ;
      « validateur » ; « contre-lecture-tete » (tours 1 et 2) ; « contre-lecture-priorite » (liste du tour 1 dite
      périmée) ; « contre-lecture-2 » (cette entrée). Aucun ne touche un critère, un seuil, une graine ni une ligne d'arrêt.
    - « Points pour la mère » 1 à 9 du rapport : transmis, non tranchés ici (rôle du rédacteur ; 24 mondes sans gain de
      puissance ; étage 5 aux critères gelés de (v), à décider avant scellement ; points 1 et 3 de « Choix et doutes »
      peut-être tranchés par R-2977 ; date de lancement ; enveloppe des cinq cribles ; noms de champs de la partie A ;
      champs permis au lecteur du pilote ; le point 9 est fait par cette entrée).
  - **Rôles** : le rapport (point pour la mère 1) veut les corrections de ce tour écrites par le modèle A ; elles l'ont été
    par un rédacteur neuf du modèle C, sur consigne de la session mère : **écart de rôle à R-2982, déclaré**. Le lecteur du
    tour 3 doit être neuf : ni le lecteur du tour 2, ni ce rédacteur, ni le lecteur ou le rédacteur du tour 1, ni l'auteur
    du brouillon 1. **Fichiers à donner en plus au tour 3** : le rapport du tour 2 et le programme `{NOM_PROGRAMME}`, avec
    le brouillon 2 pour la comparaison."""

PROPRES = [
    ("titre",
     "(regroupement, sans juge) — brouillon 2",
     "(regroupement, sans juge) — brouillon 3"),
    ("en-tete",
     "  brouillon 1, ni le rapport, ni aucune pièce citée), écrit et scellé le 2026-11-16T13:42:47Z (`date -u`) ; aucun commit, aucune poussée\n"
     "  (section « Contre-lecture »).",
     "  brouillon 1, ni le rapport, ni aucune pièce citée), écrit et scellé le 2026-11-16T13:42:47Z (`date -u`) ; aucun commit, aucune poussée\n"
     "  (section « Contre-lecture »).\n"
     "- Brouillon 3 : corrections du tour 2 de contre-lecture appliquées par un rédacteur neuf (modèle C ; il n'a écrit ni le\n"
     f"  brouillon 1, ni le brouillon 2, ni aucun des deux rapports, ni aucune pièce citée), écrit et scellé le {heure}\n"
     "  (`date -u`) ; aucun commit, aucune poussée (section « Contre-lecture »)."),
    ("statut",
     "**Statut.** Brouillon 2, **contre-lu une fois** (tour 1, corrections appliquées, section « Contre-lecture ») ; **non scellé\n"
     "comme texte qui fait foi** (R1, R2) ; tour 2 de contre-lecture à faire.",
     "**Statut.** Brouillon 3, **contre-lu deux fois** (tours 1 et 2, corrections appliquées, section « Contre-lecture ») ; **non scellé\n"
     "comme texte qui fait foi** (R1, R2) ; tour 3 de contre-lecture à faire."),
    ("validateur",
     "aucun défaut sur ce brouillon 2 (vérifié avant",
     "aucun défaut sur ce brouillon 3 (vérifié avant"),
    ("contre-lecture-tete",
     "Tour 1 fait (entrée « Contre-lecture 1 » ci-dessous) : le brouillon 1 a été soumis à la contre-lecture (R2) d'un sous-agent",
     "Tours 1 et 2 faits (entrées « Contre-lecture 1 » et « Contre-lecture 2 » ci-dessous) : le brouillon 1 a été soumis à la contre-lecture (R2) d'un sous-agent"),
    ("contre-lecture-priorite",
     "**À trancher en priorité** :",
     "**À trancher en priorité** (liste du tour 1, périmée depuis le tour 2 : voir « Contre-lecture 2 ») :"),
    ("contre-lecture-2",
     "    `appliquer-corrections-crible-v-brouillon2.py`, avec le brouillon 1 pour la comparaison.",
     "    `appliquer-corrections-crible-v-brouillon2.py`, avec le brouillon 1 pour la comparaison." + ENTREE_CL2),
]

tous = couples + PROPRES

# 5. Chaque « ancien » une seule fois dans la pièce de départ ; aucun chevauchement.
places = []
for nom, ancien, nouveau in tous:
    n = source.count(ancien)
    if n != 1:
        arret(f"{nom} : « ancien » trouvé {n} fois (une seule attendue)")
    debut = source.index(ancien)
    places.append((debut, debut + len(ancien), nom, nouveau))
places.sort()
for (d1, f1, n1, _), (d2, f2, n2, _) in zip(places, places[1:]):
    if d2 < f1:
        arret(f"chevauchement entre {n1} et {n2}")

# 6. Application par positions dans la pièce de départ.
morceaux, curseur = [], 0
for debut, fin, nom, nouveau in places:
    morceaux.append(source[curseur:debut])
    morceaux.append(nouveau)
    curseur = fin
morceaux.append(source[curseur:])
cible = "".join(morceaux)

for nom, ancien, nouveau in tous:
    if nouveau not in cible:
        arret(f"{nom} : « nouveau » absent de la cible")

with open(CIBLE, "x", encoding="utf-8") as f:
    f.write(cible)
print(f"cible écrite : {CIBLE}")
print(f"heure (date -u) : {heure}")
print(f"couples appliqués : {len(tous)} ({len(couples)} du rapport, {len(PROPRES)} propres) : "
      + ", ".join(n for _, _, n, _ in places))
print(f"empreinte de la cible : {sha(CIBLE)}")
