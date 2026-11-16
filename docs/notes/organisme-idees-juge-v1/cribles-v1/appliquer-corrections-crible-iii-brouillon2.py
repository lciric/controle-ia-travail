"""Brouillon 2 du préenregistrement du crible (iii) : application des corrections du tour 1 de contre-lecture.

Couples « ancien → nouveau » : les 26 couples C-01 à C-26 sont lus dans le rapport de contre-lecture lui-même (blocs
« Ancien : » et « Nouveau : » entre clôtures de quatre accents graves), plus trois écarts déclarés (C-04 : deux arrondis
recomptés ; C-20 : espace initiale retirée) et les couples propres à l'en-tête et à la section « Contre-lecture ».
Gardes : empreinte de la pièce de départ et du rapport ; 26 couples exactement ; chaque « ancien » figure exactement une
fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; la cible (et son compagnon) ne doit pas exister ;
aucun repli silencieux. Bibliothèque standard seule ; aucun appel, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-iii-brouillon2.py  (depuis n'importe quel dossier)
"""
import hashlib
import os
import re
import subprocess
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(ICI, "crible-iii-brouillon1.md")
SOURCE_SHA = "00c92559d54349101dfcc0c59afe402c388b192c32fa6018bbf809eb02f22af0"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-iii-tour1-v1.md")
RAPPORT_SHA = "e1e142c1a8ab09ca6111fe26980cebe4f310e653c1fbf955f152fbcbcf96e643"
CIBLE = os.path.join(ICI, "crible-iii-brouillon2.md")
NOM_PROGRAMME = "appliquer-corrections-crible-iii-brouillon2.py"


def arret(msg):
    sys.stderr.write("ARRÊT : " + msg + "\n")
    sys.exit(2)


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA)):
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
for chemin in (CIBLE, CIBLE + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")

source = open(SOURCE, encoding="utf-8").read()
rapport = open(RAPPORT, encoding="utf-8").read()

# 1. Couples du rapport.
MOTIF = re.compile(
    r"^### (C-\d\d) \((majeur|mineur)\)\n\nAncien :\n\n````\n(.*?)\n````\n\nNouveau :\n\n````\n(.*?)\n````\n",
    re.M | re.S)
couples = [(m.group(1), m.group(3), m.group(4)) for m in MOTIF.finditer(rapport)]
noms = [c[0] for c in couples]
if noms != [f"C-{k:02d}" for k in range(1, 27)]:
    arret(f"couples du rapport inattendus : {noms}")

# 2. Écarts déclarés au rapport (section « Contre-lecture » de la pièce neuve).
ECARTS = {
    "C-04": [("p = 0,95 : 0,52 à N = 20", "p = 0,95 : 0,51 à N = 20"),
             ("p = 0,93 : 0,23 et 0,71", "p = 0,93 : 0,22 et 0,71")],
    "C-20": [(" ; 24 mondes par la règle", "; 24 mondes par la règle")],
}
corriges = []
for nom, ancien, nouveau in couples:
    for a, b in ECARTS.get(nom, []):
        if nouveau.count(a) != 1:
            arret(f"écart de {nom} introuvable une fois : {a!r}")
        nouveau = nouveau.replace(a, b)
    corriges.append((nom, ancien, nouveau))
couples = corriges

# 3. Couples propres : en-tête et section « Contre-lecture ».
heure = subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], check=True, capture_output=True, text=True).stdout.strip()
if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", heure):
    arret(f"heure illisible : {heure!r}")

ANCIENNE_CL = source[source.index("## Contre-lecture\n\nAucune à ce jour"):source.index("## Annexe A — comptes exacts")]

NOUVELLE_CL = f"""## Contre-lecture

- **Contre-lecture 1** (R2, tour 1, sur le brouillon 1) — sous-agent neuf, d'un autre modèle que l'auteur, qui n'a écrit ni ce
  texte, ni [CRIBLE-V], ni [NOTE], ni [PILOTE] (un premier contre-lecteur s'était arrêté sur une limite d'usage sans rendre de
  rapport, R-2982 : rien de lui n'est repris). Texte relu : `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon1.md`,
  `{SOURCE_SHA}` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-iii-tour1-v1.md`,
  `{RAPPORT_SHA}`. Verdict : « corrections » (11 majeures :
  C-01 à C-08, C-10, C-11, C-13 ; 15 mineures). Corrections appliquées le {heure} par un rédacteur neuf, qui n'a écrit ni le
  brouillon 1 ni le rapport, au moyen du programme `{NOM_PROGRAMME}` (même dossier, scellé à côté) : les 26 couples sont lus
  dans le rapport lui-même ; chaque « ancien » figure une seule fois dans le brouillon 1 (vérifié par le programme).
  **Traitement**, point par point :
  - C-01 (durée ; cinq files de quatre mondes, bornes de 3 000 s par appel et 7 200 s par monde, code neuf) : **acceptée**
    (section 0, point 9).
  - C-02 (cinq files, jamais de minuterie plus longue ; essai à blanc à cinq files ; arrêt et nœud si les relais refusent la
    concurrence) : **acceptée** (« Devis », « Durée »).
  - C-03 (minuterie définie ; bornes par appel et par monde ; erreurs de limite de débit) : **acceptée** (trois lignes de la
    liste d'arrêt).
  - C-04 (N = 24 si le taux de réussite par appel du pilote est sous 0,95, sinon 20 ; minimum de 16 quel que soit N) :
    **acceptée, deux arrondis corrigés** après recompte exact (binomiale, monde complet de probabilité p⁵, bibliothèque
    standard) : p = 0,95 : 0,5149 à N = 20 et 0,9276 à N = 24 ; p = 0,97 : 0,8586 et 0,9961 ; p = 0,93 : 0,2249 et 0,7091 ;
    p = 0,90 : 0,0427 et 0,2943 ; d'où 0,51 (non 0,52) et 0,22 (non 0,23) ; le reste comme au rapport.
  - C-05 (minimum perdu par toute cause) : **acceptée**.
  - C-06 (seul ce que liste la table de mise à jour se refait ; III-1 à III-6 gelées, seule III-7 refaite) : **acceptée** ;
    le gel de III-6 reste « à confirmer par la mère » (rapport, « Points pour la mère », point 5).
  - C-07 (table « Règle de mise à jour d'après le pilote », écrite d'avance) : **acceptée** (« Devis »).
  - C-08 (ablation aux critères gelés par décision de la mère, R-2977 ; N-045 point 3 inchangé pour les courses) :
    **acceptée**.
  - C-09 (mondes séparés de ceux de (v), R-2977) : **acceptée**.
  - C-10 (qualificatif « dépend du barème » à l'étage 4) : **acceptée**.
  - C-11 (réserve « B tronqué » à l'étage 2) : **acceptée**.
  - C-12 (clés de configuration exigées par le bloc gelé) : **acceptée**.
  - C-13 (forme du crible) : **acceptée telle quelle ; la décision n'est pas prise ici**. R-2977 confiait ce choix au
    contre-lecteur ; le rapport recommande la variante (Pr-2 choisit, Pr-4 écrit ; confiance 0,6) et renvoie la décision à la
    mère (« Points pour la mère », point 1). Ce texte reste rédigé dans la forme fidèle à [NOTE] jusqu'à cette décision ; les
    corrections « Si la variante est retenue » du rapport ne sont **pas** appliquées (le rapport les fait écrire après la
    décision).
  - C-14 (puissance de P1 et de P2, taux d'erreur de l'intervalle par percentile, par simulation) : **acceptée**.
  - C-15 (définitions des appels et des cartes prises à [PILOTE] seul) : **acceptée**.
  - C-16 (prix des deux barèmes écrits) : **acceptée**.
  - C-17 (sonde obligatoire si le plus grand appel de Pr-1 du pilote dépasse 30 000 jetons) : **acceptée**.
  - C-18 (règles d'avance de la sonde) : **acceptée**.
  - C-19 (24 mondes ; puissance de P2 à l'effet prédit) : **acceptée** ; « 0,89 à 24 » vérifié dans l'annexe A de [NOTE]
    (`2f6a69dd…`, sortie « mondes 24 temoin 0.05 bras 0.4 puissance 0.886 ») ; la puissance de P2 (0,35 à 0,50) est le compte
    du contre-lecteur, non refait ici, à refaire par la simulation de C-14.
  - C-20 (24 mondes par la règle, non 30) : **acceptée**, à une espace près (espace initiale du « nouveau » retirée, pour ne
    pas doubler l'espace qui la précède).
  - C-21 (prix public en principal, R-2977) : **acceptée**.
  - C-22 (témoin commun écarté, R-2977) : **acceptée**.
  - C-23 (B sur les ensembles de D, retenu, R-2977) : **acceptée**.
  - C-24 (égalités du filtre par l'ordre des noms, retenu, R-2977) : **acceptée**.
  - C-25 (relevé de la sonde v74 exigé sans condition) : **acceptée**.
  - C-26 (part de distracteurs avant filtre, part après filtre à calculer sur les 12 mondes de développement) : **acceptée** ;
    le calcul reste à faire avant le scellement du texte qui fera foi.
  - **Non corrigé par le rapport, signalé sans rien changer** (à reprendre au tour suivant ou dans la version qui fera
    foi) : section 0, points 2 et 8, « Partie B » (« 20 mondes », « 100 appels »), « Devis » et « Lignes de GO proposées »
    restent écrits à 20 mondes (la table de mise à jour de C-07 les refait à N = 24 le cas échéant) ; « Choix et doutes »,
    point 9 (durée) est tranché par C-01 et C-02 sans être réécrit ; « Étapes », point 3 (« version qui fera foi (devis,
    prédictions, puissance) ») est à lire sous C-06 (seule III-7 se refait) ; d'autres renvois à [CRIBLE-V], brouillon non
    scellé, restent (« Composantes comptées », « Hypothèses de coût », « Plafond de 0,75 »), alors que C-15 n'en retire qu'un.
  - **Points du rapport pour la mère, ouverts** (aucun n'est tranché ici) : la forme (C-13) et le solde de crédits de Claude
    pour 263 USD au pire ; le prix promotionnel de Pr-1, offert jusqu'au 30 novembre ; 24 mondes sans condition (+ 20 %) ;
    N-045 point 3, à dire à Lazar avec le nœud d'adoption ; le gel de III-1 à III-6 ; le code neuf (lanceur, gabarits,
    filtre, mesure, procédure de machine, essai à blanc à cinq files) ; le risque d'un « non tranché » de P2 même si III-2 est
    vraie.

**Tour suivant** (obligatoire si la variante est retenue, selon le rapport) : sous-agent neuf qui n'a écrit ni ce texte, ni le
brouillon 1, ni le rapport du tour 1. **Fichiers à lui donner explicitement** : ce texte ; le brouillon 1 et le rapport du tour 1
(empreintes ci-dessus) ; le programme `{NOM_PROGRAMME}` ; [CRIBLE-V] (« Métrique », « Devis ») ; [NOTE] (`2f6a69dd…`), § 1,
§ 2, § 3 (iii), § 4, § 6 et annexe A ; [RELEVÉ] (`bd253b6c…`), § 3.1, § 4.2, § 5, § 6 ; [REC] (`eecd98fa…`), V3 et C2 ;
[PILOTE] (`8aa33014…`), « Dessin », « Métrique », « Devis », bloc gelé ; [PROC-14] (`20355627…`), § 0, § 6, § 7 ; [MR2]
(`47e38ec0…`), § 2 et § 3 ; [V3] (`386d48ba…`), § 4.1 ; `mesure_pilote_v4.py` (`676d5f37…`) ; `monde_riche_outils_v1.py`
(`1825b956…`) ; N-045 v2 (`c7b05e39…`) ; N-058 (`854f2724…`) ; la ligne GO-2026-11-15-06 ; la ligne R-2977 de
`registres/decisions.md` ; l'annexe A et ses deux programmes.

"""

PROPRES = [
    ("titre",
     "# Préenregistrement — crible (iii) de l'organisme d'idéation : deux passes, traits choisis par un proposeur bon marché, loi écrite par un proposeur cher — brouillon 1\n",
     "# Préenregistrement — crible (iii) de l'organisme d'idéation : deux passes, traits choisis par un proposeur bon marché, loi écrite par un proposeur cher — brouillon 2\n"),
    ("date",
     "  `91f9ddd9`, puis `377a2a0c`) ; branches lues par `git show`, sans clone ; aucun commit, aucune poussée.\n",
     "  `91f9ddd9`, puis `377a2a0c`) ; branches lues par `git show`, sans clone ; aucun commit, aucune poussée.\n"
     f"- Brouillon 2 : corrections du tour 1 de contre-lecture appliquées le {heure} (`date -u`, au scellement) par un\n"
     "  rédacteur neuf, qui n'a écrit ni le brouillon 1 ni le rapport de contre-lecture (identité dite en conversation\n"
     f"  seulement), au moyen du programme `{NOM_PROGRAMME}` (même dossier, scellé) ; dépôt lu sur `main` (tête\n"
     "  `e3dc0871`) ; procédure v14 relue au commit `2d35cafa…` par `git show`, après un `git fetch` à refspec ; rien lu de la\n"
     "  sortie du pilote MR-2 v14 ; aucun commit, aucune poussée. Rien d'autre que les corrections, l'en-tête et la section\n"
     "  « Contre-lecture » ne change.\n"),
    ("statut",
     "**Statut.** Brouillon 1, **non scellé, non contre-lu** (R1, R2).",
     "**Statut.** Brouillon 2, **contre-lu une fois** (tour 1, corrections appliquées, section « Contre-lecture ») ; **non scellé\n"
     "comme texte qui fait foi** (R1, R2) ; forme du crible à trancher (« Choix et doutes », point 4)."),
    ("validateur",
     "Validateur `controle_ia.prereg.problemes` : un seul défaut attendu à ce stade, la section « Contre-lecture » sans les deux\n"
     "empreintes (aucune contre-lecture n'existe) ; rien d'autre.\n",
     "Validateur `controle_ia.prereg.problemes` : aucun défaut sur ce brouillon 2 (vérifié avant son scellement comme pièce de\n"
     "travail).\n"),
    ("contre-lecture", ANCIENNE_CL, NOUVELLE_CL),
]

tous = couples + PROPRES

# 4. Chaque « ancien » une seule fois dans la pièce de départ ; aucun chevauchement.
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

# 5. Application par positions dans la pièce de départ.
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
print(f"couples appliqués : {len(tous)} ({len(couples)} du rapport, {len(PROPRES)} propres) : " + ", ".join(n for _, _, n, _ in places))
print(f"empreinte de la cible : {sha(CIBLE)}")
