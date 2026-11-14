#!/usr/bin/env python3
"""Témoins « idées tirées au hasard » v2.1 — relecture exploratoire des fiches de la course « conception propre ».

v2.1 (14 novembre 2026, de 12:51 à 12:58 UTC, `date -u`) = v2 (`tirer_fiches_hasard_v2.py`, `35756e6d…`, gardée, R12),
corrigée **sur le style seulement** d'après la contre-lecture (`../contre-lecture-modele-c-v1.md`, constat M2) et selon
`../corrections-apres-contre-lecture-v2.md`, écrit avant elle : opérations et ressources tirées sans remise entre les huit
fiches (deux opérations au plus en double) ; tournures d'arrondi sans fragment commun ; gabarits qui commençaient pareil
réécrits ; **dispersion des longueurs** (rang de longueur stratifié par fiche, cible de chaque champ à ce rang de la
répartition réelle, ± 0,08 ; fiche refaite depuis sa graine, rang déplacé de 0,08, si sa longueur totale sort des bornes des
réelles) ; un morceau facultatif n'est ajouté que s'il rapproche de la cible ; réserves de complément pour les fiches
longues ; moins de suites en « ; » ; tournures répétées d'une fiche à l'autre variées (contrôle 4 de la v2.1). Graines, principes et réserves de la v2 inchangés par ailleurs.

De la v2 : écrit le 14 novembre 2026 (de 11:47 à 12:00 UTC environ, `date -u`) par le préparateur de la relecture (modèle A),
d'après `engagement-avant-epreuve-v2.md` (§ 7), qui fixe ses principes avant son écriture. Remplace, pour la relecture seulement,
`../../outils/tirer_fiches_hasard_v1.py` (gardé, R12), dont les huit fiches échouaient au critère R7 par construction : leurs
raisons venaient d'une liste de six phrases-types (audit `735d185a…`, § 2).

**Fond non pensé, forme complète, style et longueur réels.**
- Fond : la modification (objet et opération), la métrique, le signe prédit et chaque maillon de la chaîne causale sont
  tirés indépendamment. La chaîne dit comment l'opération fait bouger une grandeur intermédiaire (sens tiré), parfois une
  seconde (sens tiré), puis de quelle façon la métrique dépend de la dernière (sens tiré). Le sens qu'elle implique pour la
  métrique n'est donc cohérent avec le signe prédit que par hasard ; il est consigné dans le fichier de sortie (champ
  `chaine`, jamais servi au lecteur : seul `fiche` l'est).
- Forme : prédiction fermée tournée vers l'amélioration que demande la question (quantité, signe, seuil, condition à coût
  égal) ; métrique lue par l'oracle et le relevé du coût ; aucune contrainte de la question levée ; garantie du juge dite
  pour le levier du juge ; demande précise (constante, valeur, arrondi, bornes, cas limite, consignation) ; contrôle négatif
  et ordre de grandeur chiffré du coût.
- Style et longueur : chaque champ est fait de « gestes » (phrases ou membres de phrase) pris dans des réserves d'au moins
  huit gabarits ; **chaque gabarit sert au plus une fois parmi les huit fiches** (tirage sans remise, enfant 0) ; longueur
  cible de chaque champ tirée dans l'intervalle interquartile des fiches réelles (fichier de statistiques épinglé) ; champs à
  liste fermée tirés **sans remise dans l'urne des 23 valeurs réelles** (même répartition, à l'échantillonnage près).

Graines (R9) : `numpy.random.SeedSequence(2026111411).spawn(9)` : enfant 0, attribution conjointe (gabarits sans remise,
urnes des champs à liste fermée) ; enfants 1 à 8, tirages propres à chaque fiche (objet, opération, grandeurs, sens,
nombres, longueurs cibles). Versions, graines et empreintes (générateur, statistiques) consignées à la sortie. Aucun appel,
aucun réseau.

Usage : python -I -B tirer_fiches_hasard_v2_1.py --stats STATS.json --sortie SORTIE.json      (SORTIE existant : refus, R12)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

ENTROPIE = 2026111411
NOMBRE = 8
STATS_SHA256 = "14d8ec4c973f5e52b5c1d18416e2d579c534b40fb8e3c8226bf3ef9b9778f3a0"

# --- objets de modification, par levier ------------------------------------------------------------------------------
# nom : groupe nominal ; lieu : partie de l'orchestrateur ; borne : cas limite ; unite : « entier » ou « part »
OBJETS = {
    "juge": [
        {"nom": "le nombre de tirages frais par carte", "genre": "m", "lieu": "le module du juge statistique", "unite": "entier",
         "borne": "au moins 50 tirages par carte"},
        {"nom": "le seuil ε du regroupement des doublons", "genre": "m", "lieu": "le programme de regroupement des doublons",
         "unite": "part", "borne": "entre 0,001 et 0,5 nat par instance"},
        {"nom": "la taille du jeu public d'instances sans issue", "genre": "f", "lieu": "la construction du jeu public d'instances",
         "unite": "entier", "borne": "au moins 200 instances"},
        {"nom": "le nombre d'épisodes du test de mort", "genre": "m", "lieu": "le module du test de mort", "unite": "entier",
         "borne": "au moins 100 épisodes par carte promue"},
        {"nom": "le nombre de lois aveugles fixes du nul", "genre": "m", "lieu": "la construction du nul du juge", "unite": "entier",
         "borne": "au moins deux lois aveugles"},
        {"nom": "la largeur de la tranche de choix appariée des représentants", "genre": "f", "lieu": "le choix des représentants de "
         "groupe", "unite": "entier", "borne": "au moins 20 instances"},
    ],
    "proposeurs": [
        {"nom": "le nombre de cartes demandées à chaque proposeur", "genre": "m", "lieu": "le texte servi à chaque proposeur",
         "unite": "entier", "borne": "entre 2 et 12 cartes par appel"},
        {"nom": "le nombre de lois de l'archive servies dans la vue", "genre": "m", "lieu": "la construction de la vue des proposeurs",
         "unite": "entier", "borne": "au moins une loi servie quand l'archive n'est pas vide"},
        {"nom": "la longueur de la description publique du monde", "genre": "f", "lieu": "la construction de la vue des proposeurs",
         "unite": "part", "borne": "au moins la liste des traits et de leurs échelles"},
        {"nom": "le plafond de jetons de raisonnement par appel", "genre": "m", "lieu": "les paramètres d'appel des proposeurs",
         "unite": "entier", "borne": "au moins 2 000 jetons"},
        {"nom": "le nombre d'exemples de cartes valides dans la consigne", "genre": "m", "lieu": "les instructions de proposition",
         "unite": "entier", "borne": "entre 0 et 6 exemples"},
    ],
    "composition": [
        {"nom": "la part des appels de proposition confiés aux instruments locaux", "genre": "f", "lieu": "la composition des "
         "proposeurs", "unite": "part", "borne": "entre 0 et 50 % des appels"},
        {"nom": "le nombre de proposeurs par génération", "genre": "m", "lieu": "la composition des proposeurs", "unite": "entier",
         "borne": "au moins deux proposeurs"},
        {"nom": "la part du budget du proposeur le plus cher", "genre": "f", "lieu": "la répartition entre proposeurs", "unite": "part",
         "borne": "entre 20 et 60 % du budget des proposeurs"},
        {"nom": "le nombre de passes par génération", "genre": "m", "lieu": "l'enchaînement des appels d'une génération",
         "unite": "entier", "borne": "au moins une passe"},
    ],
    "cout": [
        {"nom": "la part du budget gardée en réserve", "genre": "f", "lieu": "la répartition du budget de la course", "unite": "part",
         "borne": "entre 0 et 30 % du budget"},
        {"nom": "le plafond de dépense par génération", "genre": "m", "lieu": "la garde de dépense de l'orchestrateur",
         "unite": "part", "borne": "au moins le coût d'un appel par proposeur"},
        {"nom": "la part du budget donnée à la première génération", "genre": "f", "lieu": "la répartition du budget entre "
         "générations", "unite": "part", "borne": "entre 10 et 50 % du budget"},
        {"nom": "le nombre de générations à budget total égal", "genre": "m", "lieu": "la règle d'arrêt de la course",
         "unite": "entier", "borne": "entre 2 et 10 générations"},
    ],
}
# opérations : (infinitif, participe masculin, participe féminin, formules de la demande, sens sur l'objet)
OPERATIONS = [
    ("doubler", "doublé", "doublée",
     ("le double de sa valeur actuelle", "deux fois la valeur en vigueur", "2 fois sa valeur d'aujourd'hui"), +1),
    ("multiplier par 1,5", "multiplié par 1,5", "multipliée par 1,5",
     ("1,5 fois sa valeur actuelle", "une fois et demie le réglage courant", "150 % de sa valeur d'aujourd'hui"), +1),
    ("augmenter de 25 %", "augmenté de 25 %", "augmentée de 25 %",
     ("1,25 fois sa valeur actuelle", "le réglage présent majoré d'un quart", "125 % de sa valeur d'aujourd'hui"), +1),
    ("réduire de moitié", "réduit de moitié", "réduite de moitié",
     ("la moitié de sa valeur actuelle", "50 % du réglage en cours", "sa valeur d'aujourd'hui divisée par deux"), -1),
    ("réduire d'un tiers", "réduit d'un tiers", "réduite d'un tiers",
     ("les deux tiers de sa valeur actuelle", "le réglage de départ diminué d'un tiers",
      "environ 67 % de sa valeur d'aujourd'hui"), -1),
    ("diminuer de 40 %", "diminué de 40 %", "diminuée de 40 %",
     ("0,6 fois sa valeur actuelle", "60 % de la constante présente", "sa valeur d'aujourd'hui réduite de 40 %"), -1),
]
# grandeurs intermédiaires de la chaîne causale
GRANDEURS = [
    "la variance des valeurs e", "la puissance du juge sur les composantes de faible effet",
    "le nombre de groupes de doublons par génération", "la part des cartes refusées par le gardien",
    "le recouvrement entre les cartes de deux proposeurs", "la diversité des formes grammaticales proposées",
    "la part des cartes qui reprennent une loi de l'archive", "le raisonnement consacré à chaque carte",
    "le nombre de cartes qui atteignent le test de mort", "la stabilité des représentants de groupe",
    "l'attention portée aux régions rares des traits", "la part des lois candidates hors de la classe du nul",
    "le nombre de lois retenues par génération", "la fraction du budget dépensée en jetons d'entrée",
]
RESSOURCES = ["de tirages frais", "de place dans la consigne", "de lois à éviter", "de candidates à comparer",
              "de raisonnement", "d'instances publiques", "de budget par appel", "de contexte sur le monde"]
DOMAINES_EN = {"la théorie des sondages": "théorie des sondages", "l'optimisation bayésienne": "optimisation bayésienne",
               "la recherche opérationnelle": "recherche opérationnelle",
               "les algorithmes évolutionnaires": "calcul évolutionnaire", "l'économétrie des panels": "économétrie des panels",
               "le contrôle statistique des procédés": "contrôle statistique des procédés",
               "l'apprentissage par renforcement": "apprentissage par renforcement",
               "la planification d'expériences": "planification d'expériences"}
DOMAINES = ["la théorie des sondages", "l'optimisation bayésienne", "la recherche opérationnelle",
            "les algorithmes évolutionnaires", "l'économétrie des panels", "le contrôle statistique des procédés",
            "l'apprentissage par renforcement", "la planification d'expériences"]
# témoins à coût égal : (forme longue, forme courte) ; une forme par fiche, sans remise (enfant 0)
TEMOIN_COUT = [
    ("la même course sans la modification, au même coût, sur les mêmes graines", "la course non modifiée"),
    ("une modification de même ampleur tirée au hasard parmi les autres paramètres, au même coût",
     "une modification de même ampleur tirée au hasard"),
    ("l'opération inverse appliquée au même paramètre, au même coût", "l'opération inverse"),
    ("la course de référence rejouée avec les graines permutées, au même budget", "la course aux graines permutées"),
    ("le réglage actuel, joué sur les mêmes mondes avec la même dépense", "le réglage actuel"),
    ("un bras placebo où la valeur est changée puis remise à l'identique avant chaque appel, même dépense",
     "le bras placebo"),
    ("la course d'aujourd'hui, dépense plafonnée au même montant", "la course d'aujourd'hui"),
    ("une demi-modification (la moitié de l'écart de valeur), à coût égal", "la demi-modification"),
    ("la configuration de référence sur les graines appariées, budget identique", "la configuration de référence"),
]
ARRONDI = [", en arrondissant vers le haut", ", par excès", ", sans décimale et jamais sous le calcul exact",
           ", en gardant un nombre entier, relevé si besoin", ", au nombre entier qui suit le résultat",
           ", la partie décimale étant comptée pour une unité", ", sous forme entière (excès)",
           ", nombre entier pris au plus près par le haut", ", relevé à l'unité"]
SUPPOSES = [
    "Benjamini et Hochberg, contrôle du taux de fausses découvertes, JRSS B, 1995",
    "Wang et Ramdas, contrôle du taux de fausses découvertes par valeurs e, JRSS B, 2022",
    "Vovk et Wang, valeurs e : calibration, combinaison et applications, Annals of Statistics, 2021",
    "Shafer, tester par paris, JRSS A, 2021",
    "Ramdas, Grünwald, Vovk et Shafer, statistique par la théorie des jeux et inférence sûre à tout instant, Statistical "
    "Science, 2023",
]
OBLIGATOIRES = {  # huit formes par référence, tirées sans remise entre fiches (enfant 0)
    "popper": ["POPPER, validation d'hypothèses par falsifications séquentielles, Huang et al., ICML 2025",
               "Huang et al. (2025), POPPER, ICML, PMLR 267, citation obligatoire de la question",
               "POPPER (Huang, Jin, Li, Li, Candès, Leskovec), ICML 2025, valeurs e combinées",
               "POPPER : falsifications séquentielles conduites par un agent, Huang et al., ICML 2025",
               "Huang et al., ICML 2025 (POPPER), citée par la question servie aux proposeurs",
               "POPPER, ICML 2025, Huang et coauteurs : valeurs p converties en valeurs e",
               "Huang et al., « POPPER », ICML 2025, PMLR 267 (falsification séquentielle)",
               "POPPER (ICML 2025), Huang et al., référence obligatoire pour tout texte sur l'organisme"],
    "dwork": ["Dwork et al., réutilisation adaptative d'une réserve de test, arXiv 1506.02629, 2015",
              "Dwork, Feldman, Hardt, Pitassi, Reingold, Roth (2015), arXiv 1506.02629",
              "Dwork et al. (2015), généralisation en analyse adaptative des données, arXiv 1506.02629",
              "arXiv 1506.02629 (Dwork et al., 2015), réserve de test réutilisable",
              "Dwork et coauteurs, 2015, arXiv 1506.02629, citation obligatoire de la question",
              "Dwork et al., analyse adaptative des données et réutilisation de la réserve, arXiv 1506.02629 (2015)",
              "Dwork et al. 2015 (arXiv 1506.02629), citée par la question servie",
              "Dwork et al., arXiv 1506.02629, 2015 : surajustement à une réserve consultée plusieurs fois"],
    "ladder": ["Blum et Hardt, The Ladder, arXiv 1502.04585, 2015 : tableau de classement fiable",
               "Blum et Hardt (2015), « The Ladder », arXiv 1502.04585, soumissions adaptatives",
               "The Ladder (Blum, Hardt), arXiv 1502.04585, citation obligatoire de la question",
               "arXiv 1502.04585, Blum et Hardt, 2015 : score rendu seulement sur amélioration nette",
               "Blum et Hardt, tableau de classement sous soumissions adaptatives (The Ladder), 2015",
               "Blum, Hardt, « The Ladder », 2015, arXiv 1502.04585, citée par la question",
               "The Ladder, Blum et Hardt (arXiv 1502.04585), référence obligatoire",
               "Blum et Hardt 2015 (The Ladder), classement sous soumissions répétées, arXiv 1502.04585"],
    "cosci": ["Gottweis et al., Co-Scientist, Nature 655, p. 487-496, 2026, citation obligatoire",
              "Co-Scientist (Gottweis et al.), Nature 655, 487-496 (2026), tournoi d'hypothèses",
              "Gottweis et al. (2026), Co-Scientist, Nature 655, p. 487-496",
              "Co-Scientist, Nature 655, p. 487-496, Gottweis et coauteurs, 2026",
              "Nature 655, 487-496 (2026) : Co-Scientist, Gottweis et al., citée par la question",
              "Gottweis et al., Nature 2026 (Co-Scientist), système multi-agents de génération d'hypothèses",
              "Co-Scientist (Nature 655, 2026), Gottweis et al., référence obligatoire de la question",
              "Gottweis et al., « Co-Scientist », Nature 655 (2026), p. 487-496"],
}

# --- gestes (gabarits) par champ ; chaque liste a au moins huit gabarits ----------------------------------------------
# Emplacements : {obj} objet ; {op} infinitif ; {part} participe ; {g1} {g2} grandeurs ; {v1} {v2} verbes de sens ;
# {dep} dépendance de la métrique ; {res} ressource ; {plus} « plus » ou « moins » ; {n} mondes ; {gen} générations ;
# {seuil} seuil ; {temoin} témoin à coût égal ; {dom} domaine ; {k} composantes ; {usd} {usd_pilote} {h} {pilote} nombres.
NOM = [
    "{Op} {obj}, à coût égal", "{Obj} {part}, effet à l'oracle", "Et si {obj} était {part} ?", "{Obj} : {op_nom}",
    "{Op} {obj} ?", "Plus de couverture : {op} {obj}", "{Op} {obj}, rien d'autre", "{Obj} {part} à budget égal",
    "Organisme où {obj} est {part}", "{Obj}, {part}, sans surcoût",
]
ENONCE_QUESTION = [
    "{Op} {obj} fait-il couvrir davantage de composantes plantées, à coût égal ?",
    "Question : avec {obj} {part}, l'organisme couvre-t-il plus de composantes plantées sans dépenser davantage ?",
    "À dépense égale, une course dont {obj} est {part} trouve-t-elle davantage de composantes vraies ?",
    "Faut-il {op} {obj} pour que l'organisme couvre plus de composantes au même coût ?",
    "L'organisme trouve-t-il plus de composantes plantées si {obj} est {part}, toutes choses égales par ailleurs ?",
    "Si l'on {op_conj} {obj}, la course couvre-t-elle davantage de composantes sans coût supplémentaire ?",
    "Que gagne l'oracle quand {obj} est {part}, le budget restant le même ?",
    "Une course où {obj} est {part} dépasse-t-elle la course de référence en composantes couvertes, à coût égal ?",
    "Question fermée : {op} {obj} fait-il monter le nombre de composantes vraies trouvées, à budget égal ?",
]
ENONCE_APPROCHE = [  # premier geste quand le type tiré est « approche »
    "Proposition : {op} {obj}, toutes choses égales par ailleurs, et mesurer ce que l'oracle en dit.",
    "L'approche consiste à {op} {obj} et à comparer la course ainsi réglée à la course de référence.",
    "On propose {de_op} {obj}, sans rien changer d'autre, pour couvrir davantage de composantes à coût égal.",
    "Approche : une course dont {obj} est {part}, jouée contre la course de référence sur les mêmes graines.",
    "Il s'agit {de_op} {obj} et d'en lire l'effet sur la couverture.",
    "La démarche : {op} {obj}, puis comparer les deux bras à coût égal.",
    "Proposer une course où {obj} est {part}, et la juger sur l'oracle.",
    "{Op} {obj} : c'est toute la modification, éprouvée à budget égal.",
    "L'idée est {de_op} {obj} pour gagner en couverture sans dépenser plus.",
]
ENONCE_LIEN1 = [
    "Avec {obj} {part}, {g1} {v1}, {just}.", "Quand {obj} est {part}, {g1} {v1} : {just}.",
    "{Obj} {part} fait que {g1} {v1}, {just}.", "Le premier effet est que {g1} {v1}, {just}.",
    "La modification agit d'abord sur {g1}, qui {v1}, {just}.", "{G1} {v1} dès que {obj} est {part}, {just}.",
    "Sous cette modification, {g1} {v1}, {just}.", "On s'attend à ce que {g1} {v1}, {just}.",
    "En pratique, {g1} {v1} sitôt {obj} {part}, {just}.",
]
JUSTIFS = [
    "parce que chaque carte dispose alors de {plus} {res}", "puisque le juge examine alors {plus} {res}",
    "car les proposeurs reçoivent {plus} {res}", "les appels laissant {plus} {res} à chaque étape",
    "chaque génération offrant {plus} {res}", "le gardien voyant passer {plus} {res}",
    "ce qui laisse {plus} {res} aux étapes suivantes", "chaque appel recevant {plus} {res} qu'avant",
    "le juge comptant alors {plus} {res} par groupe",
]
ENONCE_LIEN_MILIEU = [
    "Or {g1} pèse sur {g2}, qui {v2} à son tour.", "Ce mouvement se reporte sur {g2}, qui {v2}.",
    "{G1} commande à son tour {g2}, qui {v2}.", "Il s'ensuit que {g2} {v2}.", "Par ricochet, {g2} {v2} aussi.",
    "{G2}, qui dépend {de_g1}, {v2} en conséquence.", "De proche en proche, {g2} {v2}.",
    "Cette variation gagne {g2}, qui {v2}.", "Le relais se fait par {g2}, qui {v2}.",
]
ENONCE_LIEN2 = [
    "Or {dep}.", "Et l'on sait que {dep}.", "Les faits suggèrent que {dep}.", "Il est raisonnable de penser que {dep}.",
    "C'est là que tout se joue : {dep}.", "Le dernier maillon est simple : {dep}.", "Dans l'organisme décrit, {dep}.",
    "Tout tient à ce que {dep}.", "La métrique s'en ressent, puisque {dep}.",
]
ENONCE_PORTEE = [
    "Rien d'autre ne change : mêmes proposeurs, même juge, mêmes plafonds, même famille de mondes.",
    "Le reste de l'organisme est laissé tel quel, juge compris.", "Aucun autre réglage n'est touché, et aucun agent ne "
    "voit de verdict.", "La modification est unique et porte sur un seul levier.", "Tout le reste de la course est "
    "inchangé, graines comprises.", "Les autres parties de l'organisme restent celles de la course de référence.",
    "On ne touche à rien d'autre, ni au juge ni aux consignes.", "Le juge, les consignes et les plafonds restent ceux "
    "d'aujourd'hui.", "C'est la seule différence entre les deux bras de l'expérience.",
]
ESPACE = [
    "{n} mondes plantés à graine scellée, tirés d'une famille que la conception n'a jamais vue, {gen} générations par "
    "course, mêmes proposeurs et mêmes plafonds de session",
    "une famille neuve de mondes plantés, {n} graines scellées, des courses de {gen} générations avec les proposeurs et "
    "les plafonds de la course de référence",
    "{n} graines scellées d'une famille de mondes jamais servie, {gen} générations par course, composition et plafonds "
    "inchangés",
    "des mondes plantés d'une famille que personne n'a vue à la conception : {n} graines, {gen} générations chacune, "
    "mêmes plafonds",
    "{n} mondes d'une famille neuve, écrits par programme à graine scellée ; {gen} générations par course ; les "
    "proposeurs et leurs plafonds ne changent pas",
    "une famille de mondes réservée à l'épreuve, {n} graines, {gen} générations, la course de référence pour le reste",
    "{n} mondes plantés jamais vus, chacun joué sur {gen} générations, avec la composition et les plafonds actuels",
    "{n} graines d'une famille de mondes tenue à l'écart de la conception, {gen} générations par course, plafonds de "
    "session inchangés",
    "une famille de mondes que la conception n'a pas servie, {n} graines scellées, {gen} générations, proposeurs "
    "inchangés",
]
ESPACE_SUITE = [
    ", les deux bras jouant les graines dans un ordre commun", ", chaque graine étant jouée une fois par bras",
    ", avec des graines tirées une fois avant toute course", ", sans qu'aucune graine soit rejouée après lecture",
    ", dans un ordre des graines fixé d'avance", ", graines et plafonds étant partagés par les deux bras",
    ", à raison d'une course par graine et par bras", ", graines appariées une à une entre les deux bras",
    ", toutes les graines étant scellées avant le départ",
]
PRED_PLUS = [
    "à coût égal, au moins {seuil} % de composantes plantées couvertes en plus que la course de référence, en moyenne "
    "sur les {n} mondes",
    "la couverture gagne au moins {seuil} % sur la course de référence, à dépense égale, en "
    "moyenne sur les {n} graines",
    "au moins {k} de plus par monde en moyenne, soit au moins {seuil} % de couverture en plus, à coût égal contre la "
    "course de référence",
    "à budget égal, la course modifiée couvre au moins {seuil} % de composantes plantées de plus que le témoin sur "
    "l'ensemble des {n} mondes",
    "un gain d'au moins {seuil} % de composantes plantées couvertes à la génération {gen}, à coût égal, contre la course "
    "de référence",
    "à dépense égale, au moins {k} de plus en moyenne par monde à la fin de la course, contre le témoin à coût égal",
    "au moins {seuil} % de composantes vraies couvertes en plus, mesurées après la génération {gen}, la dépense restant "
    "celle de la course de référence",
    "la course modifiée dépasse la course de référence d'au moins {seuil} % en composantes plantées couvertes, à budget "
    "égal, sur les {n} graines",
    "à coût égal ou moindre, au moins {seuil} % de composantes plantées couvertes de plus que le témoin, en moyenne "
    "sur les {n} mondes",
]
PRED_ZERO = [
    "couverture des composantes plantées inchangée (écart nul à une composante près sur les {n} mondes) pour un coût par "
    "génération en baisse d'au moins {seuil} %",
    "aucune perte de couverture (au plus une composante d'écart sur l'ensemble) et au moins {seuil} % de dépense en "
    "moins par génération, contre la course de référence",
    "la couverture ne change pas, à une composante près sur les {n} graines, tandis que le coût par génération baisse "
    "d'au moins {seuil} %",
    "même couverture que la course de référence (écart nul à une près) pour au moins {seuil} % de dollars en moins par "
    "génération",
    "un écart de couverture nul, à une composante près, et une économie d'au moins {seuil} % sur le coût de chaque "
    "génération",
    "couverture égale à une composante près sur les {n} mondes, coût par génération réduit d'au moins {seuil} %",
    "la couverture reste celle du témoin (une composante d'écart au plus) et chaque génération coûte au moins {seuil} % "
    "de moins",
    "pas de changement de couverture au-delà d'une composante sur l'ensemble, pour une dépense par génération en recul "
    "d'au moins {seuil} %",
    "couverture identique à une composante près, à coût par génération inférieur d'au moins {seuil} %",
]
PRED_GARDE = [
    ", sans plus de lois fausses ni de copies promues", ", sans promouvoir davantage de lois fausses ou de copies",
    ", le nombre de lois fausses et de copies promues ne montant pas", ", sans hausse des lois fausses ou des copies "
    "promues", ", avec au plus une loi fausse de plus sur l'ensemble des mondes et aucune copie de plus",
    ", les lois fausses et les copies promues restant au plus égales à celles du témoin", ", sans aucune hausse des "
    "promotions fausses ou copiées", ", avec au plus autant de lois fausses et de copies que la course de référence",
    ", et sans loi fausse ni copie supplémentaire",
]
PRED_STADE = [
    ", l'écart étant établi à la clôture, après la dernière génération", ", le gain devant apparaître dès la deuxième "
    "génération", ", l'effet étant mesuré génération par génération puis cumulé", ", l'écart étant lu par l'oracle à la "
    "fin de chaque course", ", chaque graine comptant pour une observation", ", avec le même seuil pour toutes les "
    "graines", ", l'écart moyen devant dépasser l'écart entre deux graines du témoin", ", la lecture se faisant une fois "
    "toutes les courses closes", ", et cela sur au moins les deux tiers des graines",
]
METRIQUE = [
    "couverture des composantes plantées et promotions de lois fausses ou de copies, toutes lues sur l'oracle à la "
    "clôture ; à chaque génération, dollars et jetons des relais",
    "nombre de composantes vraies couvertes et nombre de lois fausses ou copiées promues, au sens de l'oracle, lus après "
    "la course ; coût en dollars par génération relevé par les relais",
    "l'oracle, lu une fois la course close, donne les composantes couvertes, les lois fausses et les copies promues ; le "
    "relevé des relais donne le coût de chaque génération",
    "composantes couvertes selon l'oracle (lecture unique, après la course), promotions fausses et copiées selon l'oracle, "
    "dollars d'appels et heures de processeur par génération",
    "couverture des composantes plantées et promotions fausses ou copiées, lues par l'oracle ; dépense par génération "
    "relevée par les relais, appels et jetons compris",
    "oracle après la course : composantes plantées couvertes, lois fausses promues, copies promues ; relais : coût en "
    "dollars de chaque rôle, génération après génération",
    "ce que l'oracle dit des composantes couvertes et des lois fausses ou copiées promues, et ce que les relais relèvent "
    "en dollars et en jetons",
    "composantes plantées couvertes et lois fausses promues (oracle, lu une fois), coût par génération (relevé des "
    "relais), nombre d'appels",
    "lecture de l'oracle après la course pour la couverture et les promotions fausses ou copiées ; relevé des relais pour "
    "les dollars, par génération",
]
METRIQUE_TEMOIN = [
    " ; témoin à coût égal : {temoin}", " ; contre {temoin}", " ; comparaison à {temoin}", " ; bras témoin : {temoin}",
    " ; le témoin est {temoin}", " ; le second bras est {temoin}", " ; référence à coût égal : {temoin}",
    " ; la comparaison se fait contre {temoin}", " ; témoin retenu : {temoin}",
]
PERTE = [
    "L'effet {de_obj} peut dépendre du monde ; une seule valeur de l'opération est éprouvée, et rien ne dit que l'effet "
    "est monotone.",
    "La valeur choisie pour {obj} est un point parmi d'autres ; l'effet peut changer de signe sur une famille de mondes "
    "plus riche.",
    "Une seule ampleur de modification est essayée : un effet non linéaire {de_obj} passerait inaperçu.",
    "Ce que l'on mesure tient à une famille de mondes ; avec d'autres lois plantées, {obj} pourrait jouer autrement.",
    "L'opération sur {obj} se traduit mal en loi : l'effet passe par plusieurs grandeurs à la fois, que l'expérience ne "
    "sépare pas.",
    "La loi prédictive ignore l'interaction {de_obj} avec les plafonds de session ; une autre composition la ferait "
    "peut-être disparaître.",
    "Le passage à une loi prédictive suppose que {obj} agit seul ; en vérité, il agit avec la taille de l'archive.",
    "Une valeur fixe {de_obj} pour toute la course ne dit rien d'une valeur qui changerait d'une génération à l'autre.",
    "On perd la dépendance de l'effet à la génération : la loi ne parle que d'une moyenne sur la course.",
]
AVANTAGE = [
    "Le monde planté permet de mesurer l'effet de la modification contre la vérité, ce qu'aucune tâche ouverte ne "
    "permet : la couverture y est un compte, non une note.",
    "Sur un monde planté, l'oracle donne la couverture vraie ; on lit l'effet {de_obj} sans juge à modèle ni note.",
    "L'organisme connaît, après coup, la loi plantée : l'effet de la modification se compte en composantes vraies, à coût "
    "relevé.",
    "Avec un oracle lu une fois après la course, l'effet {de_obj} se mesure sans débat, et au même coût que le témoin.",
    "Le dispositif à monde planté sépare ce qui est trouvé de ce qui est seulement promu : on voit si la modification "
    "aide vraiment.",
    "Le relevé des relais et l'oracle suffisent à juger la modification : aucun verdict de juge n'entre dans la mesure.",
    "Parce que le monde est écrit par programme, chaque graine se rejoue à l'identique dans les deux bras et l'écart se lit sans "
    "bruit de tâche.",
    "La vérité connue du monde planté rend la comparaison exacte : chaque composante couverte est comptée une fois.",
    "Le monde planté donne une mesure qui ne dépend d'aucun modèle, et le coût relevé par génération ferme la "
    "comparaison.",
]
INCOPIABLE = [
    "Il faut un monde à graine scellée et un oracle lu après la course ; sans eux, l'effet {de_obj} reste invisible.",
    "Un laboratoire sans monde planté ne peut que compter des promotions, pas des composantes vraies.",
    "Sans oracle ni graines scellées, on ne distingue pas un effet {de_obj} d'un effet de tirage.",
    "La mesure demande l'oracle d'un monde planté et le relevé du coût par génération, que l'organisme possède déjà.",
    "Il faut rejouer chaque graine dans deux bras et consulter l'oracle à la fin : peu de dispositifs le permettent.",
    "Un occupant mieux doté en calcul n'a pas, sans monde planté, la vérité contre laquelle juger {obj}.",
    "Sans relevé du coût à la génération et sans oracle, la comparaison à coût égal n'a pas de sens.",
    "La vérité du monde planté et l'appariement des graines ne s'achètent pas avec plus de calcul.",
    "Seul un dispositif qui écrit ses mondes par programme peut rejouer la course à l'identique, modification exceptée.",
]
ORIGINALITE_TRANSPOSITION = [
    "Le principe vient {de_dom} ; l'appliquer {a_obj} d'un organisme à monde planté est la part transposée.",
    "On reprend une idée {de_dom}, où ce genre de réglage est courant ; son emploi ici est neuf.",
    "L'idée est empruntée {a_dom} ; la transposer au réglage {de_obj} est ce qui est proposé.",
    "En {dom_en}, on règle ainsi des quantités semblables ; l'organisme ne l'a jamais fait pour {obj}.",
    "La part transposée est le passage {de_dom} au réglage {de_obj}.",
    "Réglage classique en {dom_en}, jamais essayé sur {obj} dans un organisme d'idéation.",
    "La transposition vient {de_dom} ; rien de tel n'existe pour {obj} dans les organismes connus.",
    "On applique {a_obj} un réflexe {de_dom}, sans l'avoir vu employé dans un organisme à monde planté.",
    "Emprunt {a_dom} : l'objet est neuf, le principe ne l'est pas.",
]
ORIGINALITE_INEDITE = [
    "Faire varier {obj} n'a pas été essayé dans cet organisme ni, à notre connaissance, ailleurs.",
    "Personne n'a mesuré l'effet {de_obj} sur la couverture d'un organisme à monde planté.",
    "La modification {de_obj} n'a pas d'antécédent connu dans les organismes d'idéation.",
    "Rien dans les travaux connus ne règle {obj} de cette façon.",
    "Aucun organisme d'idéation n'a éprouvé {obj} contre l'oracle d'un monde planté.",
    "L'effet {de_obj} n'a jamais été mesuré, ici ni ailleurs, à notre connaissance.",
    "Nous ne connaissons pas de travail qui ait réglé {obj} contre une vérité plantée.",
    "La question {de_obj} n'a pas été posée dans les organismes d'idéation publiés.",
    "C'est, à notre connaissance, la première mesure {de_obj} dans un tel organisme.",
]
DEMANDE_COEUR = [
    "Dans {lieu}, remplacer la valeur {de_obj} par {formule}{arrondi}.",
    "Modifier {lieu} : {obj} prend désormais {formule}{arrondi}.",
    "{Lieu} reçoit une seule modification : {obj} vaut {formule}{arrondi}.",
    "Remplacer, dans {lieu}, la constante qui fixe {obj} par {formule}{arrondi}.",
    "Changer {obj} (réglage {de_lieu}) pour {formule}{arrondi}.",
    "Dans {lieu}, {obj} passe {a_formule}{arrondi}.",
    "La constante {de_lieu} qui porte {obj} est remplacée par {formule}{arrondi}.",
    "Écrire dans {lieu} une valeur {de_obj} égale {a_formule}{arrondi}.",
    "Régler {obj} {a_formule}{arrondi}, dans {lieu}.",
]
DEMANDE_BORNE = [
    " La valeur obtenue reste bornée ({borne}) ; si elle sort de la borne, la borne s'applique.",
    " Borne : {borne} ; une valeur hors de la borne est ramenée à la borne la plus proche.",
    " Si le calcul donne une valeur hors de la plage admise ({borne}), on prend la limite de la plage.",
    " La plage admise est fixée d'avance ({borne}) et le programme y ramène toute valeur qui en sort.",
    " Garde : {borne} ; au-delà, la valeur la plus proche dans la plage est prise.",
    " On respecte la plage {borne}, la valeur étant ramenée dans la plage si besoin.",
    " En cas de dépassement de la plage ({borne}), la limite atteinte fait foi.",
    " Le programme vérifie la plage ({borne}) avant la première génération et ramène la valeur si elle en sort.",
    " Une valeur hors de la plage ({borne}) est refusée et remplacée par la limite franchie.",
]
DEMANDE_CAS = [
    " Si une génération ne produit aucune carte valide, la règle est sans objet pour elle et la valeur actuelle "
    "s'applique.", " À la première génération, l'archive étant vide, l'ancienne valeur s'applique ; la nouvelle vaut "
    "ensuite.", " Quand la garde de dépense arrête la course avant terme, la dernière génération jouée est la dernière "
    "comptée.", " Si un proposeur échoue à rendre ses cartes, sa part n'est pas redistribuée dans la génération.",
    " Une génération sans aucune promotion garde la valeur fixée, sans ajustement.", " Si le gardien refuse toutes les "
    "cartes d'un appel, l'appel compte au coût et la règle ne change pas.", " Pour une course interrompue, les "
    "générations complètes seules sont lues.", " Lorsque deux réglages entrent en conflit, celui de la course de "
    "référence prévaut, sauf {obj}.", " En cas d'égalité de deux valeurs arrondies, la plus petite est prise.",
]
DEMANDE_CONSIGNE = [
    " La valeur effective est consignée au manifeste de chaque génération, avec son empreinte.",
    " Le manifeste de la course consigne la valeur appliquée et la règle qui l'a fixée.",
    " Chaque génération écrit au manifeste la valeur utilisée, avant tout appel.",
    " La valeur utilisée est scellée au manifeste au départ de la course.",
    " Le manifeste de génération garde la valeur, la borne et le cas limite appliqué.",
    " L'orchestrateur consigne la valeur au manifeste, puis lance la génération.",
    " La valeur est écrite au manifeste de départ et vérifiée à chaque génération.",
    " Au manifeste : la valeur appliquée, sa formule et l'empreinte de la configuration.",
    " Le relevé de chaque génération reprend la valeur appliquée.",
]
DEMANDE_GRAINES = [
    " Les graines des deux bras sont dérivées par numpy.random.SeedSequence, une par graine de monde.",
    " Graines dérivées par SeedSequence, une par monde et par bras, consignées.", " Les tirages aléatoires de la "
    "modification viennent d'une SeedSequence dérivée de la graine du monde.", " Toutes les graines sont dérivées "
    "d'avance (SeedSequence) et consignées au manifeste.", " Une SeedSequence par monde fournit les graines des deux "
    "bras.", " Graines : SeedSequence, enfants consignés par génération.", " Aucune graine n'est tirée en cours de "
    "route : toutes viennent d'une SeedSequence fixée au départ.", " Les deux bras reçoivent les mêmes enfants de "
    "SeedSequence.", " SeedSequence de la course, un enfant par génération et par bras.",
]
DEMANDE_GARANTIE = [
    " La valeur e de chaque carte garde une espérance au plus 1 sous le nul, qui contient l'archive ; e-BH, à m fixé "
    "d'avance, garde le contrôle des comparaisons multiples.", " Garantie inchangée : valeurs e d'espérance au plus 1 "
    "sous le nul de l'archive, et règle e-BH à m fixé d'avance pour les comparaisons multiples.", " Le nul contient "
    "toujours les lois de l'archive ; la valeur e reste d'espérance au plus 1 sous lui, et e-BH à m fixé d'avance "
    "contrôle les comparaisons multiples.", " La garantie du juge reste démontrable : espérance au plus 1 des valeurs e "
    "sous le nul qui contient l'archive, e-BH à m fixé d'avance.", " Sous le nul, qui contient les lois acceptées, chaque "
    "valeur e garde une espérance au plus 1 ; le contrôle des comparaisons multiples reste celui d'e-BH à m fixé "
    "d'avance.", " Ni le nul ni e-BH ne changent : valeurs e d'espérance au plus 1 sous le nul de l'archive, m fixé "
    "d'avance.", " La modification ne touche pas la validité : valeur e d'espérance au plus 1 sous le nul (archive "
    "comprise) et e-BH à m fixé d'avance.", " Les garanties restent : espérance des valeurs e au plus 1 sous le nul qui "
    "contient l'archive, contrôle des comparaisons multiples par e-BH, m fixé d'avance.", " Le juge garde ses deux "
    "garanties : valeur e d'espérance au plus 1 sous le nul de l'archive, et e-BH à m fixé d'avance.",
]
DEMANDE_RIEN = [
    " Le juge, sa garantie et les consignes ne changent pas.", " Rien d'autre n'est modifié, ni le juge ni la vue des "
    "proposeurs.", " Le reste de l'orchestrateur est inchangé, juge compris.", " Aucune autre constante n'est touchée.",
    " Les autres paramètres restent ceux de la course de référence.", " La vue des proposeurs et le juge restent ceux "
    "d'aujourd'hui.", " Rien n'est servi de plus aux proposeurs.", " Ni verdict ni oracle n'entrent dans la vue des "
    "proposeurs.", " Le juge statistique et ses règles ne bougent pas.",
]
COUT_PROC = [
    "rejouable sur processeur à partir de courses déjà jouées : environ {h} heures de calcul pour {n} graines et deux "
    "bras, aucun appel",
    "sur processeur seul : de l'ordre de {h} heures pour rejouer {n} graines dans les deux bras, sans aucun dollar "
    "d'appel",
    "environ {h} heures de processeur, les journaux des courses à monde planté suffisant ; aucun appel de proposeur",
    "rejeu sur processeur des {n} graines, à peu près {h} heures de calcul, aucun appel ni dollar",
    "calcul local seulement, quelque {h} heures pour {n} graines et deux bras",
    "de l'ordre de {h} heures de calcul sur processeur, sur des journaux déjà écrits ; coût d'appel nul",
    "processeur seul : {h} heures environ pour les deux bras sur {n} graines",
    "aucun appel : rejeu de {n} graines sur processeur, environ {h} heures en tout",
    "environ {h} heures de processeur pour {n} graines, sans appel de proposeur ni de juge à modèle",
]
COUT_DEP = [
    "de l'ordre de {usd} USD d'appels pour {n} mondes, deux bras et {gen} générations ; un essai réduit à {pilote} mondes "
    "coûte environ {usd_pilote} USD",
    "environ {usd} USD en tout ({n} graines, deux bras, {gen} générations), dont {usd_pilote} USD consacrés d'abord à "
    "{pilote} graines d'essai",
    "à peu près {usd} USD d'appels de proposeurs pour l'expérience entière, précédée d'un tour d'essai à {usd_pilote} USD",
    "quelque {usd} USD pour {n} mondes et deux bras ; le pilote, sur {pilote} mondes, en demande {usd_pilote}",
    "{usd} USD environ, appels de proposeurs compris, pour {n} graines et {gen} générations par bras",
    "environ {usd_pilote} USD pour un pilote de {pilote} graines, puis {usd} USD pour l'épreuve complète",
    "de l'ordre de {usd} USD sur l'ensemble ; un premier passage de {pilote} mondes, vers {usd_pilote} USD, dit si le "
    "signe tient",
    "un peu plus de {usd} USD d'appels pour les deux bras et les {n} mondes",
    "environ {usd} USD pour {gen} générations sur {n} mondes et deux bras, plus {usd_pilote} USD de premier passage",
]
PIEGE = [
    "Comparer à un témoin qui n'a pas le même coût que la course modifiée : le témoin joue les mêmes graines au même coût.",
    "Régler l'ampleur de l'opération au vu des premières courses rendrait la comparaison circulaire ; elle est fixée "
    "d'avance.",
    "Un gain qui viendrait seulement de la dépense supplémentaire de la course modifiée serait pris pour un effet "
    "{de_obj} ; les coûts relevés dans chaque bras sont donc rapprochés avant toute lecture.",
    "Donner des graines différentes aux deux bras ferait passer une différence de mondes pour un effet du changement.",
    "Consulter l'oracle à plusieurs reprises et garder la meilleure lecture fausserait l'écart ; on le consulte à la fin.",
    "Arrêter la course modifiée plus tôt que le témoin, ou plus tard, change le nombre de cartes et donc la couverture.",
    "Compter comme composantes couvertes des lois fausses que la modification fait promouvoir : l'oracle les sépare.",
    "Attribuer {a_obj} un effet qui viendrait d'une autre constante modifiée par mégarde : la configuration des deux "
    "bras est comparée champ par champ.",
    "Juger sur une seule graine favorable ; la règle de lecture porte sur toutes les graines, fixée d'avance.",
]
PIEGE_SUITE = [
    " Le plan de lecture est scellé avant la première course.", " Les deux bras sont lancés le même jour, avec les "
    "mêmes relais.", " Le relevé du coût fait foi, non l'estimation.", " L'écart est lu par programme, sans choix "
    "humain.", " Le seuil de lecture ne change pas après coup.", " Tout écart à ce plan est déclaré.", " On rapporte "
    "aussi le nombre de cartes de chaque bras.", " Les journaux des deux bras sont scellés à la clôture.",
    " Le préenregistrement fixe tout cela d'avance.",
]
COSMETIQUE = [
    "Si l'écart au témoin reste dans la variation ordinaire d'une graine à l'autre de la course de référence.",
    "Si {temoin_court} fait aussi bien que la course modifiée.", "Si l'effet disparaît quand on applique l'opération "
    "inverse {a_obj}.", "Si la couverture gagne autant avec une modification de même ampleur tirée au hasard.",
    "Si le gain ne survit pas au changement de famille de mondes.", "Si la course modifiée ne gagne qu'en promouvant "
    "plus de lois fausses.", "Si le gain se concentre sur une ou deux graines et disparaît sur les autres.",
    "Si le témoin aux graines permutées montre le même écart.", "Si l'effet tient à la seule première génération.",
]
COSMETIQUE_SUITE = [
    " Dans ce cas, {obj} n'y est pour rien.", " L'effet serait alors celui du hasard des graines.", " On conclurait à "
    "un effet de bruit.", " La modification serait cosmétique.", " Le mécanisme annoncé ne serait pas en cause.",
    " L'idée ne tiendrait pas.", " Il faudrait chercher ailleurs la cause de l'écart.", " Le gain ne viendrait pas "
    "{de_obj}.", " Ce serait un artefact de l'expérience.",
]
ENONCE_CONTEXTE = [
    "L'idée ne demande aucun appel de plus ; elle déplace seulement une quantité que l'orchestrateur fixe déjà.",
    "Les faits décrivent un organisme où ce réglage n'a jamais été mesuré contre l'oracle.",
    "C'est un réglage que l'on fixe aujourd'hui une fois pour toutes, sans en connaître l'effet.",
    "L'expérience la moins chère consiste à comparer deux bras sur les mêmes graines.",
    "La question vaut pour toute famille de mondes, mais on l'éprouve sur une famille neuve.",
    "Le mécanisme est court, et chaque maillon se lit dans les journaux d'une course.",
    "Aucune pièce servie aux proposeurs n'est modifiée par ce changement.",
    "Le réglage actuel n'a jamais été justifié par une mesure ; il vient des premières courses.",
    "Ce changement se règle par une constante et se défait aussi simplement.",
]
PRED_PRECISION = [
    ", la moyenne étant prise sur les graines et jamais sur la meilleure", ", une graine perdue par panne comptant "
    "comme un écart nul", "; l'écart est rapporté avec son intervalle par rééchantillonnage des graines", ", le seuil "
    "s'appliquant au total et non à chaque génération", ", le même seuil valant pour les deux familles de composantes",
    ", la comparaison se faisant graine contre graine", ", aucune graine n'étant écartée après coup", ", le résultat "
    "étant lu sur toutes les graines jouées, sans exception", ", l'écart médian entre graines étant rapporté aussi",
]
PRED_COMPLEMENT = [
    ", un écart plus petit que ce seuil valant échec de la prédiction",
    "; si le témoin lui-même varie de plus de ce seuil d'une graine à l'autre, la prédiction est jugée sur la médiane",
    ", la prédiction échouant si l'écart a le bon signe mais reste sous le seuil",
    ", ce seuil étant fixé avant toute course pour ne plus bouger",
    ", un gain obtenu au prix d'un coût plus élevé ne comptant pas",
    ", l'écart étant calculé graine par graine, les deux bras appariés",
    ", à coût relevé égal à 3 % près",
    ", les courses arrêtées par la garde de dépense comptant avec leur dernière génération complète",
    ", sans qu'aucune graine soit rejouée pour améliorer l'écart",
]
METRIQUE_SUITE = [
    ", l'oracle n'étant consulté qu'à la clôture de toutes les courses", ", jetons d'entrée et de sortie comptés à part",
    ", les heures de processeur du juge étant relevées aussi", ", sans qu'aucune note de juge entre dans la mesure",
    ", les composantes étant comptées à l'étage des retenues", ", chaque bras étant mesuré sur les mêmes graines",
    ", promotions fausses et copiées comptées séparément", ", le coût étant relevé par rôle et par génération",
    ", la mesure portant sur la course entière",
]
PERTE_SUITE = [
    " {G1} peut aussi réagir avec retard.", " L'effet sur {g1} n'est pas observé directement.",
    " La loi ne parle que de la moyenne des proposeurs.", " Le temps d'adaptation des proposeurs est ignoré.",
    " Les graines ne couvrent pas tous les régimes du monde.", " Le juge est supposé réagir pareil dans les deux bras.",
    " Une part de l'effet peut échapper à l'oracle.", " La durée des courses n'est pas mesurée.",
    " D'autres plafonds pourraient effacer l'effet.",
]
AVANTAGE_SUITE = [
    " Les deux bras partagent tout, sauf {obj}, si bien que l'écart lui revient.",
    " La modification se rejoue sans coût d'écriture : une constante suffit.",
    " Le coût relevé par génération permet de vérifier que la comparaison est bien à coût égal.",
    " Les journaux scellés des deux bras permettent de vérifier chaque maillon après coup.",
    " Le même dispositif sert ensuite à éprouver d'autres valeurs {de_obj}.",
    " L'expérience reste petite et peut être reprise par un autre opérateur.",
    " La lecture unique de l'oracle évite de choisir la mesure après coup.",
    " Rien dans la mesure ne dépend d'un modèle de langue.",
    " L'écart se lit en composantes vraies, l'unité même de la question.",
]
INCOPIABLE_SUITE = [
    " Il faut aussi des graines scellées que l'on puisse rejouer à l'identique.", " Le relevé du coût par rôle est propre "
    "à l'orchestrateur.", " Un tel appariement des bras demande un monde écrit par programme.", " Sans archive de lois "
    "acceptées, la comparaison n'aurait pas d'objet.", " Une vérité consultée à la clôture fait la différence avec une évaluation "
    "ouverte.", " Les tâches ouvertes n'ont pas de vérité contre laquelle compter.", " Plus de calcul n'apporte pas "
    "l'oracle.", " La mesure demande le juge statistique de l'organisme, tel qu'il est.", " Des journaux de course complets et "
    "scellés sont aussi nécessaires.",
]
ORIG_SUITE = [
    " Aucune entrée connue ne règle cette quantité contre une vérité plantée.", " Le réglage actuel vient des premières "
    "courses, sans mesure.", " La nouveauté tient à l'objet plus qu'à la méthode.", " Nous n'avons trouvé aucun travail "
    "qui la mesure ainsi.", " C'est une question de réglage, non une méthode nouvelle.", " L'emprunt est modeste, mais il "
    "n'a pas été fait.", " Rien de comparable n'est décrit dans les faits servis.", " L'idée reste à éprouver contre "
    "l'oracle.", " Le cadre à monde planté est ce qui la rend mesurable.",
]
ORIG_SUITE2 = [
    " L'idée paraît simple, mais personne ne l'a encore confrontée à une vérité plantée.",
    " Le principe est connu ailleurs ; son effet sur un organisme d'idéation reste à mesurer.",
    " Rien dans les faits servis ne montre que ce réglage ait déjà été éprouvé ainsi.",
    " Le mérite est modeste : poser la question au bon endroit et la trancher par l'oracle.",
    " Ce n'est pas une méthode neuve, c'est un réglage jamais mesuré.",
    " On ne revendique rien de plus que l'application à cet organisme précis.",
    " La part d'invention tient au choix de l'objet et du témoin, non au principe.",
    " La nouveauté, s'il y en a une, viendra du résultat plus que de l'idée.",
    " Le rapprochement entre ce domaine et l'organisme n'a pas encore été fait.",
]
DEMANDE_SUITE = [
    " Un drapeau de configuration choisit la valeur, de sorte qu'un seul code serve aux deux bras.",
    " La modification vaut dès la première génération et jusqu'à la fin de la course.",
    " Les essais de l'orchestrateur sont complétés d'un cas qui vérifie la valeur appliquée.",
    " Aucune autre partie de la configuration n'est touchée par le drapeau.",
    " Le changement est réversible en une ligne de configuration.",
    " La valeur est lue au départ et ne change plus pendant la course.",
    " Avant le départ, chaque champ de configuration du bras modifié est confronté à celui du témoin.",
    " Un manifeste par bras décrit la configuration complète.",
    " Le programme refuse de partir si la valeur n'est pas consignée.",
]
COUT_SUITE = [
    ", le calcul du juge restant négligeable devant le reste", ", sans dépense hors de la ligne prévue au devis",
    ", ordre de grandeur tenu à un facteur deux près", ", la mesure tenant sur une machine ordinaire",
    ", la lecture de l'oracle ne coûtant rien", ", le relevé des relais faisant foi", ", les rejeux éventuels sur "
    "processeur étant gratuits", ", dépense bornée au plafond fixé avant le départ", ", sans qu'aucun modèle de "
    "frontière soit entraîné",
]
PIEGE_SUITE2 = [
    " Un autre piège serait de lire l'effet sur les seules premières générations, où l'archive est presque vide.",
    " Il faut aussi éviter de compter deux fois une composante couverte par deux cartes d'un même groupe.",
    " On se garde de même de comparer des courses jouées avec des versions différentes de l'orchestrateur.",
    " Il ne faut pas non plus changer les plafonds de session d'un bras à l'autre.",
    " Enfin, une panne d'un relais dans un seul bras fausserait la comparaison : la graine est alors rejouée dans les deux.",
    " Une lecture qui retiendrait les graines où l'effet est le plus net serait sans valeur.",
    " Prendre la meilleure génération au lieu de la dernière exagérerait l'effet.",
    " Le juge du bras témoin ne doit pas être modifié par mégarde.",
    " Un effet de l'ordre de passage des bras sur les relais serait pris pour un effet de la modification.",
]
COSMETIQUE_SUITE2 = [
    " Il en va de même si l'écart change de signe d'une famille de mondes à l'autre.",
    " Même conclusion si le gain ne se voit qu'à l'étage des propositions brutes, et pas à celui des retenues.",
    " Ce serait aussi le cas si l'écart tenait à une seule génération.",
    " De même si le coût relevé du bras modifié dépassait celui du témoin.",
    " Ou encore si la modification inverse donnait un gain du même signe.",
    " Il faudrait aussi le conclure si le gain venait de lois fausses.",
    " Pareil si l'écart restait sous le bruit qui sépare deux répétitions du témoin.",
    " De même enfin si deux opérateurs ne retrouvaient pas l'écart sur les mêmes graines.",
    " Ou si le gain disparaissait quand on rejoue ces graines dans un autre ordre.",
]
# v2.1 : réserves de complément, pour que les fiches longues atteignent la longueur des longues fiches réelles
COUT_SUITE2 = [
    ", l'essentiel de la dépense allant aux appels des proposeurs de frontière",
    ", le juge et le gardien ne demandant que du calcul local, sans appel",
    ", le devis détaillé étant à faire avant tout lancement, sous une ligne de feu vert",
    ", les heures de processeur restant de l'ordre d'une journée de machine",
    ", la plus grosse part tenant aux générations tardives, où l'archive est plus longue à servir",
    ", sans compter le temps humain de relecture des journaux",
    ", à peu près la moitié pour chacun des deux bras",
    ", le pilote pouvant arrêter l'expérience avant la plus grosse part de la dépense",
    ", les mondes étant écrits par programme sans aucun coût d'appel",
]
ENONCE_CONTEXTE2 = [
    " On s'attend à un effet modeste mais lisible dès les premières générations, puisque la modification agit à chaque appel.",
    " La course de référence sert de point fixe : ses graines, ses plafonds et sa composition sont repris sans retouche.",
    " Le changement est assez simple pour être relu en quelques minutes par un programmeur qui ne connaît pas l'organisme.",
    " Une valeur plus prudente aurait été possible, mais un écart franc rend l'effet plus facile à mesurer contre l'oracle.",
    " L'idée vient d'un constat simple : ce réglage a été fixé au début, puis n'a plus jamais été remis en cause.",
    " Si l'effet existe, il devrait se voir sur la plupart des graines et non sur quelques mondes favorables seulement.",
    " Le coût de l'expérience reste petit devant celui d'une course entière, ce qui permet de l'essayer avant tout autre changement.",
    " Rien n'interdit ensuite d'essayer d'autres valeurs, mais une seule est éprouvée ici, choisie avant toute course.",
    " Cette question touche à la façon dont l'organisme dépense son budget, plus qu'à la forme des lois qu'il propose.",
]
DEMANDE_SUITE2 = [
    " Le journal de la course note, pour chaque génération, l'ancienne valeur, la nouvelle et le moment où elle s'applique.",
    " Une option de la ligne de commande permet de revenir à l'ancienne valeur sans toucher au code, pour le bras témoin.",
    " Aucun agent ne lit cette valeur : elle reste dans la configuration et n'entre dans aucune pièce servie.",
    " Le changement ne demande aucune donnée nouvelle ; il réutilise les structures que l'orchestrateur tient déjà.",
    " Un essai unitaire compare la valeur lue au départ et celle écrite au manifeste, et refuse de partir si elles diffèrent.",
    " La modification est faite une seule fois, dans un seul fichier, et le différentiel est versé avec le préenregistrement.",
    " Les deux bras sont lancés par la même commande, à une option près, pour qu'aucune autre différence ne s'y glisse.",
    " Si la valeur obtenue égale déjà la valeur actuelle, la course est quand même jouée et l'écart attendu est nul.",
    " Les relevés de coût des deux bras sont rapprochés génération par génération avant toute lecture de l'oracle.",
]
PIEGE_SUITE3 = [
    " On évite aussi de juger sur la seule génération finale quand la course a été arrêtée plus tôt dans un bras.",
    " Une autre erreur serait de lire l'effet avant la fin des deux bras, puis d'arrêter celui qui va mal.",
    " Il serait faux, de même, de retirer après coup une graine où la modification semble avoir échoué.",
    " Un dernier risque : attribuer à la modification une hausse due à un relais plus rapide le jour de l'expérience.",
    " Comparer des courses de longueurs différentes fausserait aussi la lecture, puisque la couverture croît avec les générations.",
    " On se méfie enfin d'un écart qui n'apparaîtrait que dans les mondes les plus faciles de la famille.",
    " Changer la règle de lecture après avoir vu les premières graines ruinerait la comparaison.",
    " Une graine rejouée parce qu'elle donne un écart décevant ferait de même.",
    " Prendre une moyenne sur les générations plutôt que sur les graines donnerait trop de poids aux longues courses.",
]
COSMETIQUE_SUITE3 = [
    " On le saurait aussi si l'effet tombait à zéro sur une seconde famille de mondes, jouée plus tard.",
    " Un écart qui suit le coût relevé plutôt que la modification dirait la même chose.",
    " La même conclusion vaudrait si l'effet ne dépendait pas de l'ampleur de la modification.",
    " Il en irait de même si la couverture ne gagnait que des composantes déjà couvertes par l'archive de départ.",
    " Le constat serait identique si l'effet ne paraissait que dans le bras lancé en premier.",
    " On conclurait pareil si deux répétitions de la même course différaient autant que modifiée et témoin.",
    " La modification serait aussi cosmétique si les composantes gagnées étaient toujours les plus faciles à trouver.",
    " Un gain réservé aux mondes où l'archive de départ est vide le montrerait aussi.",
    " Enfin, un gain qui disparaît quand on change les plafonds de session serait un effet de réglage, non un mécanisme.",
]
PERTE_SUITE2 = [
    " La loi oublie aussi que les proposeurs changent de comportement quand leur consigne change de longueur.",
    " Elle ne dit rien non plus de ce qui se passerait avec un autre juge ou une autre classe de nul.",
    " Elle traite enfin la famille de mondes comme homogène, alors que les mondes diffèrent beaucoup entre eux.",
    " Et elle ignore l'effet que la modification pourrait avoir sur le temps de chaque génération.",
    " La traduction perd encore la différence entre un effet immédiat et un effet qui s'accumule.",
    " Elle confond aussi l'effet sur les propositions brutes et l'effet sur les retenues.",
    " Elle suppose que les relais répondent de la même façon dans les deux bras, ce qui n'est pas garanti.",
    " Enfin, elle ne distingue pas les composantes conditionnelles des autres.",
    " Une partie du sens de l'idée, qui porte sur l'équilibre de la course, ne passe pas dans un seul nombre.",
]
AVANTAGE_SUITE2 = [
    " L'organisme garde déjà tous les journaux nécessaires, si bien que l'expérience ne demande aucun instrument neuf.",
    " La comparaison peut être refaite par un autre opérateur à partir des seules graines et de la configuration.",
    " Le même banc servira ensuite à d'autres réglages, ce qui amortit le coût de sa mise en place.",
    " L'effet se lit en composantes plantées, non en promotions, ce qui évite de juger sur le verdict du juge.",
    " Les deux bras partagent tout le reste, ce qui rend l'écart directement attribuable au réglage.",
    " Le résultat, positif ou nul, dit quelque chose d'utile sur un paramètre fixé jusqu'ici sans mesure.",
    " Aucun modèle n'intervient dans la mesure, qui ne dépend que de l'oracle et des relevés de coût.",
    " L'expérience est assez petite pour être répétée sur une seconde famille si la première donne un écart net.",
    " Le coût relevé à chaque génération permet aussi de dire si le gain vaut la dépense.",
]
INCOPIABLE_SUITE2 = [
    " Un laboratoire qui n'a que des tâches ouvertes devrait d'abord construire un oracle, ce qui coûte bien plus que l'expérience.",
    " Les mondes écrits par programme sont la pièce rare : ils permettent de rejouer chaque graine à l'identique.",
    " Sans relevé du coût par génération, on ne pourrait pas tenir la comparaison à coût égal qui fonde la prédiction.",
    " Il faudrait aussi un juge statistique sur engagement scellé, que peu de dispositifs possèdent.",
    " La séparation entre ce que voient les proposeurs et ce que lit l'oracle est difficile à reproduire ailleurs.",
    " Un concurrent mieux doté pourrait multiplier les courses, mais sans vérité plantée il ne saurait pas ce qu'il gagne.",
    " L'appariement des graines entre bras suppose un orchestrateur qui contrôle tout l'aléa de la course.",
    " L'archive des lois acceptées, tenue génération après génération, est elle aussi propre à l'organisme.",
    " Le coût d'une expérience équivalente sans monde planté serait sans commune mesure avec celui-ci.",
]
VERBES = {+1: ["augmente", "monte", "s'accroît", "grandit", "croît", "progresse", "s'élève", "gagne"],
          -1: ["baisse", "diminue", "recule", "se réduit", "décroît", "fléchit", "s'amenuise", "chute"]}
DEP_COUV = {+1: ["les composantes vraies que couvre la course se multiplient avec {g}", "plus {g} augmente, plus l'organisme couvre "
                 "de composantes", "la couverture suit {g}", "les composantes couvertes augmentent avec {g}"],
            -1: ["le compte des composantes découvertes baisse à mesure que {g} augmente", "plus {g} augmente, moins "
                 "l'organisme couvre de composantes", "la couverture varie en sens inverse {de_g}",
                 "les composantes couvertes diminuent quand {g} croît"]}
DEP_COUT = {+1: ["le coût par génération suit {g}", "plus {g} augmente, plus chaque génération coûte",
                 "la dépense par génération croît avec {g}", "le coût monte avec {g}"],
            -1: ["le coût par génération baisse quand {g} augmente", "plus {g} augmente, moins chaque génération "
                 "coûte", "la dépense par génération varie en sens inverse {de_g}", "le coût recule quand {g} croît"]}

RESERVES = {"nom": NOM, "enonce_question": ENONCE_QUESTION, "enonce_approche": ENONCE_APPROCHE, "enonce_lien1": ENONCE_LIEN1, "justifs": JUSTIFS,
            "enonce_milieu": ENONCE_LIEN_MILIEU, "enonce_lien2": ENONCE_LIEN2, "enonce_portee": ENONCE_PORTEE,
            "espace": ESPACE, "espace_suite": ESPACE_SUITE, "pred_plus": PRED_PLUS, "pred_zero": PRED_ZERO,
            "pred_garde": PRED_GARDE, "pred_stade": PRED_STADE, "metrique": METRIQUE, "metrique_temoin": METRIQUE_TEMOIN,
            "perte": PERTE, "avantage": AVANTAGE, "incopiable": INCOPIABLE, "orig_transposition": ORIGINALITE_TRANSPOSITION,
            "orig_inedite": ORIGINALITE_INEDITE, "demande_coeur": DEMANDE_COEUR, "demande_borne": DEMANDE_BORNE,
            "demande_cas": DEMANDE_CAS, "demande_consigne": DEMANDE_CONSIGNE, "demande_graines": DEMANDE_GRAINES,
            "demande_garantie": DEMANDE_GARANTIE, "demande_rien": DEMANDE_RIEN, "cout_proc": COUT_PROC,
            "cout_dep": COUT_DEP, "piege": PIEGE, "piege_suite": PIEGE_SUITE, "cosmetique": COSMETIQUE,
            "cosmetique_suite": COSMETIQUE_SUITE, "enonce_contexte": ENONCE_CONTEXTE, "pred_precision": PRED_PRECISION,
            "metrique_suite": METRIQUE_SUITE, "perte_suite": PERTE_SUITE, "avantage_suite": AVANTAGE_SUITE,
            "incopiable_suite": INCOPIABLE_SUITE, "orig_suite": ORIG_SUITE, "demande_suite": DEMANDE_SUITE,
            "cout_suite": COUT_SUITE, "piege_suite2": PIEGE_SUITE2, "cosmetique_suite2": COSMETIQUE_SUITE2,
            "pred_complement": PRED_COMPLEMENT, "temoin_cout": TEMOIN_COUT, "arrondi": ARRONDI,
            "enonce_contexte2": ENONCE_CONTEXTE2, "demande_suite2": DEMANDE_SUITE2, "piege_suite3": PIEGE_SUITE3,
            "cosmetique_suite3": COSMETIQUE_SUITE3, "perte_suite2": PERTE_SUITE2, "avantage_suite2": AVANTAGE_SUITE2,
            "incopiable_suite2": INCOPIABLE_SUITE2, "cout_suite2": COUT_SUITE2, "orig_suite2": ORIG_SUITE2}
URNES = ("type", "loi_predictive.signe", "avantage.source", "originalite.niveau", "demande_organisme.nature",
         "cout.nature")
QO_POIDS = {"QO5": 12, "QO4": 9, "QO1": 5, "QO2": 4, "QO3": 2}


def _feuilles(o) -> list:
    if isinstance(o, str):
        return [o]
    if isinstance(o, list):
        return [t for x in o for t in _feuilles(x)]
    if isinstance(o, dict):
        return [t for v in o.values() for t in _feuilles(v)]
    return []


def maj(s: str) -> str:
    return s[:1].upper() + s[1:]


def contracter(prep: str, gn: str) -> str:
    """« de le … » → « du … », « à le … » → « au … », etc."""
    for art, (de, a) in (("le ", ("du ", "au ")), ("les ", ("des ", "aux ")), ("la ", ("de la ", "à la ")),
                         ("l'", ("de l'", "à l'"))):
        if gn.startswith(art):
            return (de if prep == "de" else a) + gn[len(art):]
    return f"{prep} {gn}"


def _urne(stats: dict, champ: str) -> list[str]:
    comptes = stats["fiches_reelles"]["mesures"]["champs_a_liste_fermee"][champ]
    return [v for v in sorted(comptes) if v != "hors_liste" for _ in range(comptes[v])]


def _urne_leviers(stats: dict) -> list[str]:
    c = stats["fiches_reelles"]["mesures"]["classes_d_etiquettes"]
    return [lev for lev in sorted(c) if lev.startswith("levier:") for _ in range(c[lev])]


def attribution(rng: np.random.Generator, stats: dict) -> dict:
    """Enfant 0 : un gabarit par fiche et par réserve, sans remise ; valeurs des urnes, sans remise."""
    gab = {}
    for nom, res in RESERVES.items():
        if len(res) < NOMBRE:
            raise SystemExit(f"réserve {nom} : {len(res)} gabarits < {NOMBRE}")
        gab[nom] = [int(x) for x in rng.permutation(len(res))[:NOMBRE]]
    urnes = {}
    for champ in URNES:
        u = _urne(stats, champ)
        urnes[champ] = [u[int(i)] for i in rng.permutation(len(u))[:NOMBRE]]
    u = _urne_leviers(stats)
    urnes["levier"] = [u[int(i)] for i in rng.permutation(len(u))[:NOMBRE]]
    formes = {r: [int(x) for x in rng.permutation(len(OBLIGATOIRES[r]))[:NOMBRE]] for r in sorted(OBLIGATOIRES)}
    supposes = [int(x) for x in rng.permutation(NOMBRE)]
    # v2.1 : opérations sans remise (une seconde permutation complète la première : deux en double au plus) ;
    # ressources des justifications sans remise
    ops = [int(x) for x in rng.permutation(len(OPERATIONS))] + [int(x) for x in rng.permutation(len(OPERATIONS))]
    ressources = [int(x) for x in rng.permutation(len(RESSOURCES))[:NOMBRE]]
    return {"gabarits": gab, "urnes": urnes, "formes_obligatoires": formes, "rang_suppose": supposes,
            "operations": ops[:NOMBRE], "ressources": ressources,
            # v2.1 : rangs de longueur stratifiés (un par huitième de [0,08 ; 0,96]), pour la dispersion des réelles
            "rangs_longueur": [0.08 + 0.88 * (int(s) + float(rng.uniform())) / NOMBRE for s in rng.permutation(NOMBRE)]}


def cible(rng: np.random.Generator, stats: dict, champ: str, rang: float) -> int:
    """v2.1 : longueur cible d'un champ au rang de longueur de la fiche (± 0,08, borné à [0,01 ; 0,99]), lue sur la
    répartition réelle du champ (interpolation entre minimum, q1, médiane, q3, maximum)."""
    q = stats["fiches_reelles"]["mesures"]["longueur_par_champ"][champ]
    u = min(0.99, max(0.01, rang + float(rng.uniform(-0.08, 0.08))))
    return int(round(float(np.interp(u, [0.0, 0.25, 0.5, 0.75, 1.0], [q["min"], q["q1"], q["mediane"], q["q3"], q["max"]]))))


class Fiche:
    """Assemble une fiche à partir de son rang (gabarits attribués sans remise) et de son générateur propre."""

    def __init__(self, rang: int, rng: np.random.Generator, att: dict, stats: dict):
        self.k, self.rng, self.att, self.stats = rang, rng, att, stats
        self.slots = {}
        self.rang_longueur = float(att["rangs_longueur"][rang])   # v2.1 : fiche courte ou longue, tous champs ensemble

    def gab(self, reserve: str) -> str:
        return RESERVES[reserve][self.att["gabarits"][reserve][self.k]]

    def choix(self, liste):
        return liste[int(self.rng.integers(len(liste)))]

    def remplir(self, gabarit: str, **v) -> str:
        return gabarit.format(**{**self.slots, **v})

    def composer(self, champ: str, obligatoires: list[str], facultatifs: list[str], sep: str = "") -> str:
        """Les morceaux obligatoires, puis les facultatifs tant que la longueur reste sous la cible du champ."""
        objectif = cible(self.rng, self.stats, champ, self.rang_longueur)
        texte = sep.join(obligatoires)
        for m in facultatifs:  # v2.1 : un morceau n'est ajouté que s'il rapproche la longueur de la cible
            if abs(len(texte) + len(m) - objectif) >= abs(len(texte) - objectif):
                break
            texte += m
        return texte

    def construire(self) -> dict:
        """v2.1 : bornes de longueur totale. Si la fiche sort de [minimum, maximum] des réelles, elle est refaite, depuis la
        même graine fille, à un rang de longueur déplacé de 0,08 vers l'intérieur (six essais au plus ; nombre d'essais
        consigné dans `chaine`)."""
        tot = self.stats["fiches_reelles"]["mesures"]["longueur_totale_vue"]
        graine = self.rng.bit_generator.seed_seq
        for essai in range(1, 7):
            self.rng = np.random.default_rng(graine)
            r = self._construire()
            n = sum(len(x) for x in _feuilles(r["fiche"]))
            r["chaine"]["essais_de_longueur"] = essai
            if tot["min"] <= n <= tot["max"]:
                return r
            self.rang_longueur = min(0.99, self.rang_longueur + 0.08) if n < tot["min"] else max(0.01, self.rang_longueur - 0.08)
        return r

    def _construire(self) -> dict:
        rng, att, k = self.rng, self.att, self.k
        levier = att["urnes"]["levier"][k].split(":", 1)[1]
        signe = att["urnes"]["loi_predictive.signe"][k]
        obj = self.choix(OBJETS[levier])
        inf, part_m, part_f, formules, sens_op = OPERATIONS[att["operations"][k]]
        formule = self.choix(formules)
        part = part_f if obj["genre"] == "f" else part_m
        g = [GRANDEURS[int(i)] for i in rng.permutation(len(GRANDEURS))[:2]]
        deux_maillons = bool(rng.integers(2))
        d1, d12, d2 = (int(rng.choice([-1, 1])) for _ in range(3))
        metrique = "cout" if signe == "0" else "couverture"
        sens_metrique = d1 * (d12 if deux_maillons else 1) * d2
        sens_predit = -1 if signe == "0" else +1          # « 0 » : couverture égale et coût en baisse
        n = int(self.choix([16, 18, 20, 24, 25, 28, 30, 32, 36, 40]))
        gen = int(self.choix([2, 3, 4, 5, 6]))
        seuil = int(self.choix([15, 20, 25, 30, 35, 40] if signe == "0" else [8, 10, 12, 15, 18, 20, 25]))
        kval = self.choix(["une composante", "deux composantes"])
        pilote = int(self.choix([4, 5, 6]))
        usd_gen = float(self.choix([0.9, 1.1, 1.2, 1.4, 1.6]))
        usd = int(round(usd_gen * n * gen * 2 / 5.0) * 5)
        usd_pilote = int(round(usd_gen * pilote * gen * 2 / 5.0) * 5) or 5
        h = int(self.choix([4, 6, 8, 10, 12, 16, 20]))
        dom = self.choix(DOMAINES)
        temoin, temoin_court = self.gab("temoin_cout")
        op_conj = {"doubler": "double", "multiplier par 1,5": "multiplie par 1,5", "augmenter de 25 %": "augmente de 25 %",
                   "réduire de moitié": "réduit de moitié", "réduire d'un tiers": "réduit d'un tiers",
                   "diminuer de 40 %": "diminue de 40 %"}[inf]
        op_nom = {"doubler": "doublement", "multiplier par 1,5": "facteur 1,5", "augmenter de 25 %": "surcroît de 25 %",
                  "réduire de moitié": "partage par deux", "réduire d'un tiers": "retrait d'un tiers",
                  "diminuer de 40 %": "recul de 40 %"}[inf]
        self.slots = {"obj": obj["nom"], "Obj": maj(obj["nom"]), "de_obj": contracter("de", obj["nom"]),
                      "a_obj": contracter("à", obj["nom"]), "de_lieu": contracter("de", obj["lieu"]), "op": inf, "Op": maj(inf), "part": part, "de_op": ("d'" if inf[0] in "aeiouéè" else "de ") + inf,
                      "op_conj": op_conj, "op_nom": op_nom, "g1": g[0], "G1": maj(g[0]), "de_g1": contracter("de", g[0]), "g2": g[1], "G2": maj(g[1]),
                      "n": n, "gen": gen, "seuil": seuil, "k": kval, "pilote": pilote, "usd": usd,
                      "usd_pilote": usd_pilote, "h": h, "dom": dom, "dom_en": DOMAINES_EN[dom], "de_dom": contracter("de", dom), "a_dom": contracter("à", dom), "temoin": temoin,
                      "temoin_court": temoin_court, "lieu": obj["lieu"], "Lieu": maj(obj["lieu"]),
                      "borne": obj["borne"], "formule": formule, "a_formule": contracter("à", formule),
                      "arrondi": self.gab("arrondi") if obj["unite"] == "entier" else ""}
        v1 = self.choix(VERBES[d1])
        v2 = self.choix(VERBES[d1 * d12])
        plus = "plus" if self.rng.integers(2) else "moins"
        res = RESSOURCES[att["ressources"][k]]
        just = self.remplir(self.gab("justifs"), plus=plus, res=res)
        g_der = g[1] if deux_maillons else g[0]
        dep = self.choix((DEP_COUT if metrique == "cout" else DEP_COUV)[d2]).format(g=g_der, de_g=contracter("de", g_der))
        # énoncé : question, chaîne causale (deux ou trois maillons), puis portée et contexte selon la cible
        premier = "enonce_approche" if att["urnes"]["type"][k] == "approche" else "enonce_question"
        oblig = [self.remplir(self.gab(premier)), self.remplir(self.gab("enonce_lien1"), v1=v1, just=just)]
        if deux_maillons:
            oblig.append(self.remplir(self.gab("enonce_milieu"), v2=v2))
        oblig.append(self.remplir(self.gab("enonce_lien2"), dep=dep))
        enonce = self.composer("enonce", oblig, [" " + self.gab("enonce_portee"), " " + self.gab("enonce_contexte"),
                                                 self.gab("enonce_contexte2")], sep=" ")
        pred = self.composer("loi_predictive.prediction",
                             [self.remplir(self.gab("pred_zero" if signe == "0" else "pred_plus")), self.gab("pred_garde")],
                             [self.gab("pred_stade"), self.gab("pred_precision"), self.gab("pred_complement")])
        espace = self.composer("loi_predictive.espace_instances", [self.remplir(self.gab("espace"))],
                               [self.gab("espace_suite")])
        metr = self.composer("loi_predictive.metrique", [self.gab("metrique"), self.remplir(self.gab("metrique_temoin"))],
                             [self.gab("metrique_suite")])
        perte = self.composer("perte_traduction", [self.remplir(self.gab("perte"))],
                              [self.remplir(self.gab("perte_suite")), self.gab("perte_suite2")])
        avantage = self.composer("avantage.texte", [self.remplir(self.gab("avantage"))],
                                 [self.remplir(self.gab("avantage_suite")), self.gab("avantage_suite2")])
        incopiable = self.composer("avantage.incopiable_parce_que", [self.remplir(self.gab("incopiable"))],
                                   [self.gab("incopiable_suite"), self.gab("incopiable_suite2")])
        niveau = att["urnes"]["originalite.niveau"][k]
        orig = self.composer("originalite.texte",
                             [self.remplir(self.gab("orig_transposition" if niveau == "transposition" else "orig_inedite"))],
                             [self.gab("orig_suite"), self.gab("orig_suite2")])
        nature = att["urnes"]["demande_organisme.nature"][k]
        coeur = self.remplir(self.gab("demande_coeur"))
        if nature == "ajout":
            coeur = "Ajouter une règle à l'orchestrateur : " + coeur[0].lower() + coeur[1:]
        demande = self.composer(
            "demande_organisme.texte",
            [coeur, self.remplir(self.gab("demande_borne")),
             self.gab("demande_garantie") if levier == "juge" else self.gab("demande_rien")],
            [self.remplir(self.gab("demande_cas")), self.gab("demande_consigne"), self.gab("demande_graines"),
             self.gab("demande_suite"), self.gab("demande_suite2")])
        cout_nature = att["urnes"]["cout.nature"][k]
        cout = self.composer("cout.ordre_de_grandeur",
                             [self.remplir(self.gab("cout_proc" if cout_nature == "processeur" else "cout_dep")),
                              self.gab("cout_suite")], [self.gab("cout_suite2")])
        piege = self.composer("piege", [self.remplir(self.gab("piege"))],
                              [self.gab("piege_suite2"), self.gab("piege_suite3"), self.gab("piege_suite")])
        cosm = self.composer("cosmetique_si", [self.remplir(self.gab("cosmetique"))],
                             [self.gab("cosmetique_suite2"), self.gab("cosmetique_suite3"),
                              self.remplir(self.gab("cosmetique_suite"))])
        nb_qo = 2 if rng.random() < 0.39 else 1
        qos = list(QO_POIDS)
        p = np.array([QO_POIDS[q] for q in qos], dtype=float)
        tires = [qos[int(i)] for i in rng.choice(len(qos), size=nb_qo, replace=False, p=p / p.sum())]
        refs = [{"reference": OBLIGATOIRES[r][att["formes_obligatoires"][r][k]], "statut": "RAPPORTE"}
                for r in ("popper", "dwork", "ladder", "cosci")]
        nb_obl = int(self.choix([3, 4, 4, 4, 4]))
        refs = [refs[int(i)] for i in sorted(rng.permutation(4)[:nb_obl])]
        if att["rang_suppose"][k] < 4:  # la moitié des fiches cite une référence supposée
            refs.append({"reference": SUPPOSES[att["rang_suppose"][k] % len(SUPPOSES)], "statut": "SUPPOSE"})
        fiche = {
            "nom": self.remplir(self.gab("nom")),
            "type": att["urnes"]["type"][k],
            "enonce": enonce,
            "loi_predictive": {"espace_instances": espace, "prediction": pred, "signe": signe, "metrique": metr},
            "perte_traduction": perte,
            "questions_servies": [f"levier:{levier}"] + tires + ["nouvelle"],
            "avantage": {"source": att["urnes"]["avantage.source"][k], "texte": avantage,
                         "incopiable_parce_que": incopiable},
            "originalite": {"niveau": niveau, "texte": orig},
            "demande_organisme": {"nature": nature, "texte": demande},
            "cout": {"nature": cout_nature, "ordre_de_grandeur": cout},
            "piege": piege,
            "cosmetique_si": cosm,
            "anteriorite": refs,
        }
        chaine = {"levier": levier, "objet": obj["nom"], "operation": inf, "sens_operation": sens_op,
                  "grandeurs": g if deux_maillons else g[:1],
                  "sens_maillons": [d1, d12, d2] if deux_maillons else [d1, d2], "metrique_de_la_chaine": metrique,
                  "sens_implique": sens_metrique, "sens_predit": sens_predit,
                  "coherente_avec_le_signe": sens_metrique == sens_predit}
        return {"fiche": fiche, "chaine": chaine}


def generer(stats: dict) -> list[dict]:
    enfants = np.random.SeedSequence(ENTROPIE).spawn(NOMBRE + 1)
    att = attribution(np.random.default_rng(enfants[0]), stats)
    out = []
    for k in range(NOMBRE):
        r = Fiche(k, np.random.default_rng(enfants[k + 1]), att, stats).construire()
        out.append({"code": f"T2-H{k + 1}", "famille": "hasard", "cible": "L5 (séparation d'avec le hasard), règle v2",
                    "graine": {"entropie": ENTROPIE, "spawn_key": list(enfants[k + 1].spawn_key)},
                    "attendu": {"N": "aucune"}, "chaine": r["chaine"], "fiche": r["fiche"]})
    return out


def main(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--stats", required=True)
    a.add_argument("--sortie", required=True)
    args = a.parse_args(argv)
    sortie = Path(args.sortie)
    if sortie.exists():
        print(f"{sortie} existe déjà (R12)", file=sys.stderr)
        return 2
    brut = Path(args.stats).read_bytes()
    if hashlib.sha256(brut).hexdigest() != STATS_SHA256:
        print("statistiques : empreinte différente de celle épinglée", file=sys.stderr)
        return 2
    stats = json.loads(brut)
    temoins = generer(stats)
    soi = Path(__file__).resolve()
    sortie.write_text(json.dumps({
        "outil": {"chemin": soi.name, "sha256": hashlib.sha256(soi.read_bytes()).hexdigest()},
        "statistiques": {"chemin": Path(args.stats).name, "sha256": STATS_SHA256},
        "versions": {"python": sys.version.split()[0], "numpy": np.__version__},
        "graines": {"entropie": ENTROPIE, "nombre": NOMBRE,
                    "methode": "numpy.random.SeedSequence(2026111411).spawn(9) : enfant 0 attribution, 1 à 8 fiches"},
        "version": "v2.1 (style corrigé après la contre-lecture, constat M2)",
        "temoins": temoins}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"fiches": len(temoins),
                      "coherentes": sum(t["chaine"]["coherente_avec_le_signe"] for t in temoins)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
