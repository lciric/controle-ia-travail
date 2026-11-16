"""Brouillon 4 du préenregistrement du crible (v) : application des corrections du tour 3 de contre-lecture.

Couples « ancien → nouveau » : les 18 couples des corrections C3-1 à C3-9 sont lus dans le rapport de contre-lecture
lui-même (bloc entre clôtures nommé `C3-…`, ligne « ANCIEN: », puis « NOUVEAU: » et ses lignes de suite jusqu'à la
clôture : une ligne de suite est une ligne de table de plus), sans retouche ; s'y ajoutent des couples propres, chacun
nommé et déclaré dans la section « Contre-lecture » de la cible : titre, en-tête, statut, validateur, tête de la
section « Contre-lecture », point 11 de l'annexe A (chiffres que le rapport demande « à refaire par programme et à
recopier en annexe » : sortie de `comptes-crible-v-brouillon4.py`, lue par empreinte), entrée « Contre-lecture 3 ».
Gardes : empreinte de la pièce de départ, du rapport, du programme des comptes et de sa sortie ; 18 couples exactement
dans le rapport, noms attendus ; chaque « ancien » figure exactement une fois dans la pièce de départ ; aucun
chevauchement entre « anciens » ; chaque « nouveau » présent dans la cible ; la cible ne doit pas exister (ouverture en
mode « x ») ; aucun repli silencieux.
Bibliothèque standard seule ; aucun appel, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-v-brouillon4.py [--essai DOSSIER]
  (--essai : écrit la cible dans DOSSIER, dossier de travail jetable, pour la contrôler avant l'écriture réelle)
"""
import hashlib
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "crible-v-brouillon3.md")
SOURCE_SHA = "8a21f085d0caff7d2ec392e326b30c03616d67f066460eed54bae5aed5aeca6a"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-v-tour3-v1.md")
RAPPORT_SHA = "b693bf5d279c2b234807702cb23ab5c4d97e017ae06171dff28e44c64c3ac523"
COMPTES = os.path.join(ICI, "comptes-crible-v-brouillon4.py")
COMPTES_SHA = "c72783dc844308a5592884811e5e313ee9b2d9d1442ff8b7c873bd5e63342f13"
SORTIE = os.path.join(ICI, "comptes-crible-v-brouillon4-sortie.txt")
SORTIE_SHA = "042f9332d7b101268a3238ffec2fce35f1aafb004d405ee384c543ff8f6e9498"
NOM_CIBLE = "crible-v-brouillon4.md"
NOM_PROGRAMME = "appliquer-corrections-crible-v-brouillon4.py"
NOMS_RAPPORT = ["C3-01a", "C3-01b", "C3-02a", "C3-02b", "C3-03", "C3-04", "C3-05a", "C3-05b", "C3-06", "C3-07",
                "C3-08a", "C3-08b", "C3-08c", "C3-08d", "C3-08e", "C3-08f", "C3-08g", "C3-09"]


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
for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA), (COMPTES, COMPTES_SHA), (SORTIE, SORTIE_SHA)):
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
for chemin in (CIBLE, CIBLE + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")

with open(SOURCE, encoding="utf-8") as f:
    source = f.read()
with open(RAPPORT, encoding="utf-8") as f:
    rapport = f.read()
with open(SORTIE, encoding="utf-8") as f:
    sortie_comptes = f.read().rstrip("\n")
if "```" in sortie_comptes:
    arret("sortie des comptes porteuse d'une clôture")

# 2. Couples du rapport : ligne « `C3-…` », clôture, « ANCIEN: », « NOUVEAU: » et ses lignes de suite, clôture.
couples = []
lignes = rapport.splitlines()
i = 0
while i < len(lignes):
    m = re.fullmatch(r"`(C3-\d\d[a-z]?)`", lignes[i])
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
POINT_11 = f"""

**Point 11 — comptes du tour 3 de contre-lecture** (chiffres que le rapport du tour 3 demande « à refaire par programme et à
recopier en annexe »). Programme `docs/notes/organisme-idees-juge-v1/cribles-v1/comptes-crible-v-brouillon4.py`
(`{COMPTES_SHA}`) et sa sortie `comptes-crible-v-brouillon4-sortie.txt`
(`{SORTIE_SHA}`), même dossier, lancés le 16 novembre à 14:13:44 UTC (`date -u`)
par `nice -n 19 python3 -I` (Python 3.13.18, bibliothèque standard seule, quelques millisecondes) ; **aucune donnée, aucun tirage,
aucun taux du pilote** : la grille du point 4 est écrite d'avance ; la probabilité d'atteindre le minimum sur le taux mesuré du
pilote reste à calculer par programme dans la version qui fera foi (section « Taille »). Les chiffres du rapport du tour 3
qui portent sur ces comptes (W_min, puissance, épargne, devis : points 2 et 3 de ses réponses, C3-5, C3-8) se retrouvent égaux ;
le taux par appel que le rapport tire des comptes de marche du pilote (motif de C3-5) n'est pas repris : aucun taux du pilote
n'entre ici. « 1.0000 » est un arrondi au quatrième chiffre, non une certitude. Sortie, recopiée :

```
{sortie_comptes}
```"""

ENTREE_CL3 = f"""

- **Contre-lecture 3** (tour 3, sur le brouillon 3) : sous-agent neuf du modèle C, qui n'a écrit aucune pièce citée (ni ce
  texte, ni ses brouillons, ni les corrections, ni les rapports des tours 1 et 2) ; lecture de 14:01:47Z à 14:08Z. Rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-v-tour3-v1.md`, empreinte
  `{RAPPORT_SHA}` ; brouillon relu : `crible-v-brouillon3.md`, empreinte
  `{SOURCE_SHA}`. Verdict : **corrections** (2 majeures C3-1 et C3-2, 7 mineures C3-3 à C3-9,
  4 remarques facultatives F-1 à F-4) ; aucun « a_refaire » ; application du tour 2 jugée fidèle ; validateur sans défaut.
  - **Application** : par un rédacteur neuf du **modèle A**, comme le veut R-2982 (il n'a écrit ni le brouillon 1, ni les
    brouillons 2 et 3, ni aucun des trois rapports, ni aucune pièce citée), au moyen du programme `{NOM_PROGRAMME}` (même
    dossier, empreinte dans son compagnon `.sha256`) : les 18 couples « ancien → nouveau » des corrections C3-1 à C3-9
    (C3-01a à C3-09) sont lus dans le rapport lui-même et appliqués sans retouche ; chaque « ancien » vérifié présent une
    seule fois dans le brouillon 3 ; aucun chevauchement ; cible neuve ; écriture le {heure} (`date -u`). Aucun appel de
    modèle, aucune dépense, aucune machine, aucune donnée lue (rien sous `diag/`, `runs/`, `donnees/` ; relevé de v67 et
    sortie du pilote non ouverts ; issue et taux du pilote non lus).
  - **Réponse point par point** :
    - C3-1 (dollars définis de trois façons) : **acceptée** (deux couples C3-01a, C3-01b) : couvertures et règle sur les
      appels répondus ; dollars sur les quatre appels lancés du monde, répondus ou non, tronqués et en échec facturés compris,
      comme le bras de référence ; biais commun d'un appel absent dit, rapporté par la sensibilité « mondes à quatre appels
      seulement ». La phrase « Les cartes refusées […] d'appels tronqués comptent dans les dollars » est désormais d'accord.
    - C3-2 (rejeu sous archive fictive et sortie unique) : **acceptée** (deux couples C3-02a, C3-02b) : le rejeu est exécuté
      en dernier (5), après l'écriture et le scellement de la sortie principale, dans le même lancement, vers un second
      fichier scellé, qui n'est pas une seconde mesure ; ligne d'arrêt neuve avec son essai sain et son artefact (R5).
    - C3-3 (dénominateur de q_w, 1 à 12) : **acceptée**.
    - C3-4 (banc de mutations) : **acceptée** (quatre mutations neuves : monde complet par quatre appels, dollars des appels
      non répondus omis, garde B_a, ordre du rejeu).
    - C3-5 (puissance et épargne à 24 mondes) : **acceptée** (deux couples C3-05a, C3-05b) ; chiffres refaits par programme,
      égaux à ceux du rapport, recopiés à l'annexe A, point 11 (couple propre « annexe-11 »).
    - C3-6 (ce que le lecteur du pilote rend pour V1 et V6) : **acceptée** dans le sens que le rapport retient (le témoin
      positif est lu, V1 et V6 ne sont plus des prédictions à l'aveugle) ; le sens inverse demande un mot de la mère (point
      pour la mère 3) et changerait alors la ligne « Le témoin positif du pilote … » des points à remesurer, non l'étape 2.
    - C3-7 (règle de B_a, puis du taux, de N et de M) : **acceptée** ; les trois nombres 1,5 ; 3 600 s ; 2 sont gardés tels
      que le rapport les propose, choix de pratique non déduits d'une donnée (le texte le dit) ; aucun ne peut se fixer sans
      lire le pilote, que ce rédacteur ne lit pas.
    - C3-8 (« 20 » restés écrits) : **acceptée** (sept couples C3-08a à C3-08g). **Réserve pour le tour 4** : restent écrits
      pour N = 20, sans contradiction propre, que le rapport ne demande pas de changer : « En dix lignes », point 9 (« ne
      tient pas sur 20 mondes ») ; V1 (« sur 20 », remarque F-1) ; table du devis (lignes à 20 appels, branche à 24 chiffrée
      au point 8 de « En dix lignes », sous les lignes de GO et à l'annexe A, point 11) ; corps des lignes de GO proposées
      (« 20 mondes », montants à 20 : la phrase de C3-08e dit qu'elles s'écrivent pour le N que fixe la règle).
    - C3-9 (intervalle de V7) : **acceptée**.
    - Remarques facultatives F-1 à F-4 : **non appliquées** (non exigées ; consigne de ce tour bornée aux corrections) ;
      F-2 (« taux ≥ 0,95 » sur 16 appels de pilote ne s'atteint qu'à 16 sur 16) est transmise à la mère.
    - Couples propres de ce tour : « titre » (brouillon 4) ; « en-tete » (ligne « Brouillon 4 » de l'en-tête) ; « statut » ;
      « validateur » ; « contre-lecture-tete » (tours 1 à 3) ; « annexe-11 » (chiffres du tour 3, par programme) ;
      « contre-lecture-3 » (cette entrée). Aucun ne touche un critère, un seuil, une graine ni une ligne d'arrêt. Le
      programme de l'annexe A (points 1 à 10) reste à recopier en entier dans la version qui fera foi ; les comptes du point
      11 couvrent en partie ceux que les tours 1 et 2 laissaient à cette version (table W_min(n_c) jusqu'à 24, puissance à 17,
      21 et 24 mondes à risque, épargne à 20 et 24 mondes, devis au pire à 24), non la probabilité d'atteindre le minimum sur
      le taux mesuré du pilote.
    - Décisions de R-2977 : relues ; archive {{K1}}, mondes séparés, dollars au prix public, lecture de GO-2026-11-15-06 pour
      l'essai, partie A permise et descriptive, 24 mondes sous 0,95, tension avec N-058 à dire à Lazar : présentes dans ce
      texte. Seul écart relevé, que ce tour ne tranche pas (point pour la mère 4 du rapport) : R-2977 dit « recommandations de
      l'auteur sauf mention », alors que « Choix et doutes » laisse ouverts les points 1 et 3 ; à confirmer par la mère.
    - « Points pour la mère » 1 à 8 du rapport : transmis, non tranchés ici (24 mondes sans gain de puissance, décision avant
      scellement, recommandation (b) du lecteur, N = 20 dans tous les cas ; étage 5 aux critères gelés de (v), avant
      scellement ; témoin positif lu ou non ; points 1 et 3 de « Choix et doutes » ; enveloppe d'ensemble des cinq cribles ;
      date de lancement fixée par le code neuf ; le point 7 est fait par cette entrée ; noms de champs de la partie A).
  - **Rôles** : corrections écrites par le modèle A, conformément à R-2982. Le lecteur du tour 4 doit être neuf : ni le
    lecteur du tour 3, ni ce rédacteur, ni les lecteurs et rédacteurs des tours 1 et 2, ni l'auteur du brouillon 1.
    **Fichiers à donner en plus au tour 4** : le rapport du tour 3, le programme `{NOM_PROGRAMME}`, le programme
    `comptes-crible-v-brouillon4.py` et sa sortie (annexe A, point 11), avec le brouillon 3 pour la comparaison."""

PROPRES = [
    ("titre",
     "(regroupement, sans juge) — brouillon 3",
     "(regroupement, sans juge) — brouillon 4"),
    ("en-tete",
     "  (`date -u`) ; aucun commit, aucune poussée (section « Contre-lecture »).",
     "  (`date -u`) ; aucun commit, aucune poussée (section « Contre-lecture »).\n"
     "- Brouillon 4 : corrections du tour 3 de contre-lecture appliquées par un rédacteur neuf (modèle A, comme le veut R-2982 ;\n"
     "  il n'a écrit ni le brouillon 1, ni les brouillons 2 et 3, ni aucun des trois rapports, ni aucune pièce citée), écrit et\n"
     f"  scellé le {heure} (`date -u`) ; aucun commit, aucune poussée (section « Contre-lecture »)."),
    ("statut",
     "**Statut.** Brouillon 3, **contre-lu deux fois** (tours 1 et 2, corrections appliquées, section « Contre-lecture ») ; **non scellé\n"
     "comme texte qui fait foi** (R1, R2) ; tour 3 de contre-lecture à faire.",
     "**Statut.** Brouillon 4, **contre-lu trois fois** (tours 1 à 3, corrections appliquées, section « Contre-lecture ») ; **non scellé\n"
     "comme texte qui fait foi** (R1, R2) ; tour 4 de contre-lecture à faire."),
    ("validateur",
     "aucun défaut sur ce brouillon 3 (vérifié avant",
     "aucun défaut sur ce brouillon 4 (vérifié avant"),
    ("contre-lecture-tete",
     "Tours 1 et 2 faits (entrées « Contre-lecture 1 » et « Contre-lecture 2 » ci-dessous) : le brouillon 1 a été soumis",
     "Tours 1 à 3 faits (entrées « Contre-lecture 1 » à « Contre-lecture 3 » ci-dessous) : le brouillon 1 a été soumis"),
    ("annexe-11",
     "de composition, mais aucun de ces mondes n'est servi.",
     "de composition, mais aucun de ces mondes n'est servi." + POINT_11),
    ("contre-lecture-3",
     "    le brouillon 2 pour la comparaison.",
     "    le brouillon 2 pour la comparaison." + ENTREE_CL3),
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
