# Textes du rédacteur du brouillon 6 (bloc-notes) : ancres dans le brouillon 5 et textes « après ».
ANCIEN = "/home/user/controle-ia-travail/prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/couples-brouillon4-vers-brouillon5-v1.py"

TETE_SCRIPT = '''# Script des couples du brouillon 5 au brouillon 6 du préenregistrement
# « lecture des sondes de l'étape B bis par lentilles, v2 » — v1
#
# Auteur : rédacteur du brouillon 6 (sous-agent de la session des lentilles, Claude Fable 5.2), 2026-11-20.
# Ce que fait ce script : il lit le brouillon 5, vérifie son empreinte, applique chaque couple (texte avant, texte après) après
# avoir vérifié que le texte « avant » paraît une fois et une seule dans le brouillon 5, que les textes « avant » ne se chevauchent
# pas, puis écrit le brouillon 6 et imprime, pour chaque couple, son identifiant, la correction ou la tâche qu'il sert, son lieu, la
# ligne du brouillon 5 où commence le texte « avant » et les deux textes. Il vérifie enfin que les deux bornes du bloc séparable
# paraissent une fois chacune et liste les marqueurs entre doubles chevrons du brouillon 6.
# Même forme que le script du brouillon 4 au brouillon 5 (`couples-brouillon4-vers-brouillon5-v1.py`), dont il reprend la
# mécanique. Il ne lit aucune donnée, aucune sonde, aucun score. Bibliothèque standard seulement.
#
# Usage : python -I couples-brouillon5-vers-brouillon6-v1.py BROUILLON5 BROUILLON6
#   (refuse d'écraser un BROUILLON6 qui existe et diffère, R12 ; « - » comme BROUILLON6 : contrôle seul, rien n'est écrit)
import hashlib
import re
import sys

EMPREINTE_BROUILLON_5 = "88a2011a8b9e02ba9f6f2933ee4ec01ee6f156abf44ccf19960d9b7de3d75003"

# (identifiant, correction ou tâche, lieu, texte avant, texte après)
'''

_l = open(ANCIEN, encoding="utf-8").read().split("\n")
_i = _l.index("def main(argv):")
_p = "\n".join(_l[_i:])
for a, b in (("brouillon 5", "brouillon 6"), ("brouillon 4", "brouillon 5"), ("BROUILLON5", "BROUILLON6"),
             ("BROUILLON4", "BROUILLON5"), ("EMPREINTE_BROUILLON_4", "EMPREINTE_BROUILLON_5"),
             ("couples-brouillon4-vers-brouillon5", "couples-brouillon5-vers-brouillon6")):
    _p = _p.replace(a, b)
PIED_SCRIPT = "\n\n" + _p

V = "vérification des corrections du brouillon 5"

TETE = '''## Brouillon 6 — différences avec le brouillon 5

- **Ce qu'est ce fichier** : le brouillon 5 (`prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon5.md`,
  `88a2011a8b9e02ba9f6f2933ee4ec01ee6f156abf44ccf19960d9b7de3d75003`, archivé sans changement, R12) avec : les nœuds N12 et N17
  écrits comme tranchés (mot de Lazar du 2026-11-20) ; la correction bloquante C1 et les six corrections non bloquantes M1 à M6
  de la vérification de ses corrections (« vérification 5 » :
  `docs/notes/neuron-lens-v1/verification-corrections-texte-lecture-lentilles-v2-brouillon5-v1.md`,
  `04282064d10c6cdd2a4266bf9e5a526c9835463476108dec8a54dfcae2f64328`, verdict « scellable après corrections ») ; un marqueur
  ajouté ; et ce bloc. Fabriqué par programme, comme les brouillons 4 et 5 : des couples (texte avant, texte après), chaque
  « avant » trouvé une fois et une seule dans le brouillon 5 ; contrôle par `diff` contre le brouillon 5. Pièces de
  fabrication, scellées, dans `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/` : `couples-brouillon5-vers-brouillon6-v1.py`
  (le script, qui porte chaque couple, ce qu'il sert et son lieu ; couples P01 à P32),
  `sortie-couples-brouillon5-vers-brouillon6-v1.txt` (sa sortie) et `diff-brouillon5-vers-brouillon6-v1.txt` (le `diff`) ;
  leurs empreintes sont dans leurs compagnons (ce fichier ne peut pas porter l'empreinte d'une pièce qui le fabrique).
- **Auteur du brouillon 6** : rédacteur neuf, sous-agent de la session des lentilles (`session_01XJ6Mgr9o68QqLiFTLg3zRW`), modèle
  **Claude Fable 5.2** (`claude-fable-5-2`), sur le mandat
  `docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-redacteur-texte-lecture-v2-brouillon6-v1.md`
  (`7cc8a455f3a2c1591858b0449c55caa09c905a788e28ad12487ac12f0a6a0637`, recalculée avant lecture ; section « Texte du mandat » seule
  lue, la section « Après le brouillon 6 » non lue), parti sur le mot de Lazar « go reco » du 2026-11-20 (note
  `docs/notes/neuron-lens-v1/mot-lazar-noeuds-n12-n17-et-brouillon6-2026-11-20-v1.md`,
  `cd02b0fb85e06b0366d731bb9888d753562c8d76cbef403874587975da9c99ed`, branche des lentilles ; ce mot n'a pas, à l'écriture, de
  ligne de registre que le rédacteur ait trouvée : il est cité d'après cette seule note, et sa ligne d'accord est un marqueur).
  Il n'a écrit ni la v1, ni les brouillons 1 à 5 de la v2, ni le critère d'identité, ni le devis, ni l'addendum de
  concentration, ni aucune contre-lecture ou vérification ; il ne sera ni développeur, ni opérateur, ni lecteur de ce texte.
  Aucun commit, aucun push, aucune machine, aucune dépense, aucun modèle chargé ; aucun fichier existant modifié ; réseau :
  `git fetch origin main` seul.
- **Heures (UTC, `date -u`)** : 2026-11-20 ; lecture des pièces à partir de 05:23:02 ; écriture à partir de @@ECRITURE@@ ; fin
  relevée au pied. Branche des lentilles `claude/brave-galileo-jhp684` à `2cdb7b28b8527619ade80f0108aea2a72d4d8ad7` ; branche
  principale récupérée plusieurs fois (la session des lentilles l'avait donnée à `10e8ff08` ; les récupérations l'ont
  avancée : `d05179e3…` vers 05:25, `b5486e67…` à 05:29) ; dernière récupération, juste avant l'écriture du fichier :
  `@@MAIN@@…` (@@MAINDATE@@).
- **Pièces lues** : la section « Texte du mandat » du mandat ; `CLAUDE.md` ; la vérification 5, **en entier** ; la note du mot
  de Lazar sur les nœuds N12 et N17, **en entier** ; du brouillon 5, **non lu en entier** : les lignes 1 à 200, 240 à 266,
  364 à 400, 466 à 497, 545 à 568, 590 à 610, 892 à 899, 1236 à 1350, 1474 à 1486, 1604 à 1626, 1804 à 1832, 1866 à 1900,
  1924 à 1960, 2036 à 2058, 2196 à 2232, 2296 à 2300, 2392 à 2606, 2690 à 2775, et les lignes rendues par des recherches de
  mots (titres, marqueurs, « N12 », « N17 », « addendum de recopie », « par gabarit », « option », « défaut », « ajustement
  seul », « Course du réajustement », nom de la ligne `GO-LENTILLES-BBIS-V2`) ; la tête et la fin du script des couples du
  brouillon 5 et le début de sa sortie (pour en reprendre la forme) ; du critère d'identité version 8 (`541bb86b…`) : les
  lignes 440 à 470 (fin du § 5 et § 6 entier, pour la correction M2) ; de la contre-lecture 3 (`42024aa9…`, branche
  principale) : la liste de ses derniers titres et l'annexe B entière ; le validateur `src/controle_ia/prereg.py`
  (`3b2e3ee5…`, l. 1 à 80) ; la v1 scellée (`ca5066d7…`) par le seul programme de contrôle de l'annexe B, sans lecture.
  **Non lus** : la contre-lecture du brouillon 4 (aucune correction de la vérification 5 n'y renvoie au-delà de ce qu'elle
  en cite) ; V, le verdict de la tranche de nos lentilles (aucune correction ne l'exige) ; le devis ; l'addendum de
  concentration ; la note du mot de Lazar sur le départ du rédacteur du brouillon 5 (`f28f18ae…` : empreinte recalculée,
  fichier non ouvert) ; les brouillons 1 à 4.
- **Expositions, déclarées** (R4) :
  - *Registres de la branche principale, par recherche de mots* (`registres/go.md` et `registres/decisions.md` ; lignes qui
    portent à la fois « N12 » et « N17 » ; lignes datées du 2026-11-20 qui portent « N12 », « N17 », « brouillon 6 » ou le
    début de l'empreinte d'une des deux notes ; lignes qui portent « brouillon 5 » et « go reco » ; lignes qui portent
    « brouillon 6 » ou le début de l'empreinte d'une des deux notes avec « lentille », « N12 » ou « go reco » ; sorties
    coupées à 160 ou 200 caractères) : **aucune ligne de cette chaîne n'a été trouvée**, à la dernière récupération
    comme aux précédentes. Six débuts de lignes d'autres objets sont sortis de ces recherches et ont été vus : R-2604 et R-3706 (débuts de deux mots de Lazar, « go recos », sans contenu
    d'une chaîne) ; GO-2026-11-19-29 (intitulé « Bras A, deux points du brouillon 5 » et le début d'une règle de lecture
    d'un moniteur, sans mesure) ; R-2021 (intitulé d'une contre-lecture d'un brouillon de P3-bis et son verdict de forme,
    « scellable après corrections », sans mesure ni issue) ; R-3105 (début : reprise de la session de la lecture par
    lentille neuronale, le 18 novembre) ; R-3632 (intitulé : crédit du loueur de cartes avant une course du saboteur, sans
    mesure ni issue). Aucun score, aucune aire, aucune issue d'une chaîne cloisonnée
    n'y paraît ; rien de la chaîne des sondes.
  - *Bloc séparable du brouillon 5* : vus, en relevant ses bornes, les quatre premières lignes du bloc et ses trois
    dernières, dont une valeur de V sur nos lentilles (ligne du nœud N13). Tout y porte sur nos lentilles, rien sur les sondes.
  - *Chiffres de coût et de durée du devis* que le brouillon 5 cite, sur une ligne rendue par une recherche de mots.
- **Jamais ouverts** : aucun fichier de la liste « Jamais ouverts » de la v1 ; aucune sortie, aucun score, aucune table, aucune
  lecture, aucun verdict de l'apprentissage des sondes sur la tâche ; aucune table ni sortie de la lecture par la lentille publique ;
  aucune branche `donnees/*` ou `calcul/*` ; aucun fichier sous `diag/` ou `runs/` ; rien sous `docs/verdicts/` ; aucun fichier
  « consigne-privee » ou « conception-ii-b » ; rien de `brouillons/ii-b-saboteur-budget-v1/` ; aucune sortie de P3, P3-bis, T0.6,
  T0.7, de l'étape B, du bras d'attaque ni du saboteur à budget (hors les six débuts de lignes de registre déclarés
  ci-dessus). **Aucun choix de ce brouillon n'a pu être fait d'après une sortie de la chaîne des sondes.**
- **Refus d'outil** : état au pied du texte.

**Lieux des blocs, déclarations et pieds des brouillons 1 à 5 que ce brouillon réécrit, un à un** (une correction ou une
tâche l'exige pour chacun ; tout le reste de ces blocs, déclarations d'auteur, dates et pieds compris, est inchangé et décrit
le brouillon qu'il nomme) :

| lieu | ce qui change | pourquoi |
|---|---|---|
| bloc « Brouillon 5 », « Auteur » (couple P02) | le mot « go reco » qui a lancé le rédacteur du brouillon 5 est dit mot rapporté | vérification 5, M6 |
| bloc « Brouillon 5 », « Reste à faire » (couple P03) | la liste des couples à donner au lecteur désigné | M1 |
| en-tête de la v2, table des marqueurs et son état (couples P04, P05) | une ligne ajoutée ; état au brouillon 6 | mandat, tâche 1 |
| « Changements de la v1 à la v2 », lignes 18 et 28 (couples P06, P07 ; la ligne 28 est du brouillon 5, la ligne 18 lui est antérieure) | les deux nœuds dits tranchés ; la ligne 28 dite remplacée | mandat, tâches 1 et 4 |
| « Entrées », condition de lecture : parenthèse « reste à trancher » (couple P09 ; texte antérieur au brouillon 5) et alinéas « Nœud N12 laissé ouvert » et « Nœud N17 laissé ouvert » (couples P10, P11 ; textes du brouillon 5) | nœuds écrits comme tranchés ; textes des options écartées retirés | tâche 1 |
| « Métrique », point 6, alinéa du brouillon 5 (couple P13) | la lentille des logits nommée | M4 |
| « Plan d'analyse », point 11, alinéa du brouillon 5 (couple P15) | passe encore en cours ; ligne des tables sans ligne des entrées | M3 |
| « Liste d'arrêt », quatre lignes portant « (brouillon 5) » (couples P16 à P20) | cas des options écartées retirés ; C1 ; M2 ; M3 | tâches 1 à 3 |
| « Lignes de registre », alinéa « Brouillon 5 » (couple P22) | réécrit : issue fixée avant le scellement ; clé retirée | tâche 1 ; C1 |
| « Code neuf », essais ajoutés par le brouillon 5 (couples P23 à P26) | essais repris | C1 ; M2 ; M3 ; tâche 1 |
| « Nœuds » : renvoi de N12 et titre « Restent ouverts » (couples P27, P28 ; textes antérieurs au brouillon 5), alinéas « Brouillon 5 » de N12 et de N17 (couples P29, P30) | nœuds écrits comme tranchés | tâche 1 |
| « Contre-lecture », entrée 4, phrase du brouillon 5 (couple P31) | liste des couples ; une phrase « Brouillon 6 » ajoutée | M1 ; forme |

**Laissés tels quels, parce qu'ils décrivent le brouillon qu'ils nomment** : dans le bloc « Brouillon 5 », la ligne « N12 et
N17 » de sa table de traitement, la ligne 13 de sa table des changements, le point (4) de ses choix et son alinéa « Nœuds
pour Lazar », qui disent les deux nœuds ouverts, l'option lue dans la pièce de `GO-LENTILLES-BBIS-V2` et la clé de
l'addendum de recopie : **ils sont remplacés par ce bloc et ne valent plus** ; de même, la fin du bloc « Brouillon 4 »
(« Restent ouverts du brouillon 2 »), la ligne « point 6, nœuds » de « Traitement de la contre-lecture 3 », et le point (1)
des « Points que le rédacteur du brouillon 2 signale ». Les pieds des brouillons 1, 2, 4 et 5 ne sont pas touchés ; un pied
du brouillon 6 est ajouté après eux (couple P32).

**Table de traitement** (tâches du mandat, corrections de la vérification 5 ; « faite » ou « refusée » avec sa raison ; les
couples sont ceux des pièces de fabrication)

| objet | traitement | où (couples) |
|---|---|---|
| **N12 tranché, option (a)** (tâche 1) | **faite** : écrit comme tranché par Lazar le 2026-11-20, avec la note du mot (`cd02b0fb…`) et le marqueur de la ligne d'accord. La lecture d'une de nos lentilles au deuxième palier, en ajustement seul ou en seconde course incomplète, attend la ligne `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS`, postérieure à l'avertissement ; **ce mot ouvre ou non la lecture, il ne choisit aucune branche** : écrit dans « Entrées » et dans « Nœuds ». Les textes des options (b) et (c) sont retirés à chaque lieu | Entrées (P09, P10) ; Liste d'arrêt (P16) ; Lignes de registre (P22) ; Code neuf (P26) ; Nœuds (P27 à P29) ; table des changements (P06 à P08). Sans changement, parce que déjà écrits sous l'option (a) et sans forme conditionnelle : plan, point 1 (k bis) ; « Critères » (ligne « Course du réajustement », verdict d'ensemble au deuxième palier) ; essai « fiche muette » |
| **N17 tranché, option (a) aux deux paliers** (tâche 1) | **faite** : ce texte vaut le texte de lecture neuf qu'exige le critère d'identité, aux deux paliers ; aucun addendum de recopie. **La clé `ADDENDUM-RECOPIE-IDENTITE-LENTILLES-BBIS-V2` et tout ce qui en dépendait sont retirés**, lieu par lieu : la condition de lecture et son motif « Non lue […] addendum de recopie […] absent » (Entrées, P11) ; le cas de la liste d'arrêt (P17) ; la clé conditionnelle (Lignes de registre, P22) ; ses essais (Code neuf, P26) ; ce que le défaut aurait demandé (Nœuds, P30) ; la ligne 28 de la table des changements (P07). La clé n'est plus nommée que pour dire qu'elle est retirée | P07, P08, P11, P17, P22, P26, P28, P30 |
| **C1** issue de N12 et de N17 fixée avant le scellement (tâche 2) | **faite, adaptée à des nœuds tranchés** : l'issue est fixée par ce texte, avant son scellement, d'après le mot de Lazar du 2026-11-20 ; c'est écrit (« Nœuds », « Entrées », « Lignes de registre »). La pièce que nomme `GO-LENTILLES-BBIS-V2` ne fait que la recopier, avec l'identifiant et l'heure de la ligne d'accord, inscrite avant `SCELLEMENT-LENTILLES-BBIS-V2` ; **le code n'y lit aucune option**. **Arrêt nommé gardé** : pièce qui porte une autre issue, ligne d'accord datée après le scellement (ou à la même seconde, ou sans heure lisible), ligne d'une autre forme. Essais : cas sain et artefacts (R5). Les mots de la vérification 5 (« inscrite avant `SCELLEMENT-LENTILLES-BBIS-V2` », « une issue donnée après le scellement de ce texte est un écart à un préenregistrement scellé : version neuve, nœud ; la pièce ne fait que recopier ») sont repris ; « le défaut échu » et « le défaut du nœud vaut » sont retirés, sans emploi | Lignes de registre (P22) ; Liste d'arrêt (P20) ; Code neuf (P26) ; Nœuds (P28) ; Entrées (P10, P11) |
| **M1** couples de la couche 15 pour le lecteur désigné | **faite** aux deux lieux : couples L16 à L19 du brouillon 5 (L18 est dans le bloc séparable et dit le lieu et le libellé de V), et, pour information, L12 et L15 | bloc « Brouillon 5 » (P03) ; Contre-lecture (P31) |
| **M2** formes de la phrase du déclencheur (vi) | **faite** : sont admises aussi « séries … inchangées » et les deux faits joints par « et » ; ligne d'arrêt et essais accordés | Entrées, fiche (P12) ; Liste d'arrêt (P19) ; Code neuf (P23, P24) |
| **M3** première passe encore en cours ; ligne des tables sans ligne des entrées | **faite**, dans les mots de la vérification 5, aux deux lieux ; une ligne d'arrêt ajoutée ; un essai (artefact) ajouté | Plan, 11 (P15) ; Liste d'arrêt (P18) ; Code neuf (P25) |
| **M4** « Lien avec la première passe » : lentille des logits | **faite**, dans les mots de la vérification 5 | Métrique, 6 (P13) |
| **M5** description de la ligne `GO-LENTILLES-BBIS-V2` | **faite** aux deux lieux, avec « brouillon 6 » au lieu de « brouillon 5 » pour l'issue de N12 et de N17 | Plan, 1 (P14) ; Lignes de registre (P21) |
| **M6** mot « go reco » qui a lancé le rédacteur du brouillon 5 | **faite, seconde branche** : aucune ligne de la session principale ne porte ce mot sur la branche principale (`@@MAIN@@…`) ; il est cité d'après sa seule note (`f28f18ae…`) et **dit mot rapporté** | bloc « Brouillon 5 » (P02) |
| **marqueur** `LIGNE_D_ACCORD_DES_NOEUDS_N12_ET_N17` (nom sans chevrons) | **ajouté**, une occurrence, dans « Nœuds » : la ligne d'accord a été cherchée sur la branche principale et n'y est pas ; porté par la session principale, avant le scellement | Nœuds (P28) ; table des marqueurs (P04, P05) |
| **table « Changements de la v1 à la v2 »** (tâche 4) | **faite** : ligne 18 complétée, ligne 28 dite remplacée ; lignes 30 à 34 ajoutées, une par changement neuf | Changements (P06 à P08) |
| **bloc « Changements du brouillon 5 au brouillon 6 »** (tâche 4) | **fait** : ci-dessous, une ligne par changement | ce bloc |
| **contrôle par programme des lignes de la v1** (tâche 5) | **rejoué** (programme de l'annexe B de la contre-lecture 3, recopié mot pour mot) sur la v1 `ca5066d7…` et sur ce brouillon : **791 lignes égales, aucune supprimée, 10 prolongées, 13 réécrites — le compte ne change pas**, les lignes sont les mêmes, et aucun texte n'est à corriger (aucun couple ne touche une ligne de la v1) ; seule la quatrième valeur de la première ligne de sortie du programme, le nombre de lignes insérées, change (@@INS@@ au lieu de 1056) | pied (P32) |
| **bloc séparable** (tâche 6) | **non touché** : aucun couple n'a de texte « avant » dans le bloc ; aucune valeur chiffrée ne bouge ; bornes uniques et intactes (contrôle du script). Aucun couple du brouillon 6 n'est à donner au lecteur désigné ; ceux du brouillon 5 restent à lui donner (M1) | — |

**Changements du brouillon 5 au brouillon 6** (une ligne par changement ; « règle » : le changement fixe ou change une règle
de la seconde passe ; « lettre » : il corrige des mots sans changer une règle)

| n° | changement | sorte | couples |
|---|---|---|---|
| 1 | nœud N12 tranché par Lazar, option (a) : textes des options (b) et (c) retirés ; le mot postérieur à l'avertissement ouvre ou non la lecture et ne choisit aucune branche | lettre (la règle écrite est celle retenue ; deux règles conditionnelles retirées) | P06 à P10, P16, P22, P26 à P29 |
| 2 | nœud N17 tranché par Lazar, option (a) aux deux paliers : aucun addendum de recopie ; clé `ADDENDUM-RECOPIE-IDENTITE-LENTILLES-BBIS-V2` retirée avec sa condition de lecture, son motif, son cas d'arrêt et ses essais | règle (une condition de lecture retirée) | P07, P08, P11, P17, P22, P26, P28, P30 |
| 3 | issue des deux nœuds fixée avant le scellement : la pièce de `GO-LENTILLES-BBIS-V2` la recopie avec sa ligne d'accord, inscrite avant `SCELLEMENT-LENTILLES-BBIS-V2` ; le code n'y lit aucune option ; arrêt nommé sur une autre issue, une ligne d'accord non antérieure au scellement ou une autre forme ; pièce muette : aucun arrêt, une phrase en tête | règle | P20, P22, P26 |
| 4 | phrase du déclencheur (vi) : formes admises élargies | règle (un arrêt évitable retiré) | P12, P19, P23, P24 |
| 5 | première passe encore en cours : pas de nœud de la v1, phrases de la première passe si elle s'achève ; ligne `TABLES-LENTILLES-BBIS` sans `ENTREES-LENTILLES-BBIS` : arrêt | règle | P15, P18, P25 |
| 6 | « Lien avec la première passe » : la lentille des logits nommée aux deux endroits | lettre | P13 |
| 7 | description de la ligne `GO-LENTILLES-BBIS-V2` : recopie de GO-2026-11-19-92 et de l'issue de N12 et de N17 | lettre | P14, P21 |
| 8 | couples de la couche 15 à donner au lecteur désigné : L16 à L19, et L12 et L15 pour information | lettre | P03, P31 |
| 9 | mot « go reco » du départ du rédacteur du brouillon 5 dit mot rapporté | lettre | P02 |
| 10 | marqueur de la ligne d'accord des nœuds N12 et N17 ajouté ; table des marqueurs et son état ; table des changements ; entrée de contre-lecture ; pied | forme | P04 à P08, P28, P31, P32 |

**Choix du rédacteur au-delà de la lettre du mandat ou de la vérification 5** (chacun à juger par qui vérifie ce brouillon) :
(1) **pièce muette** : une pièce de `GO-LENTILLES-BBIS-V2` qui ne dit rien d'un des deux nœuds n'arrête pas (comme au
brouillon 5 et dans les mots de la vérification 5), mais ce n'est plus « le défaut » qui vaut : c'est l'issue de ce texte,
et la seconde passe l'écrit en tête par une phrase fixée (« Lignes de registre ») ; (2) **forme de la ligne recopiée** : elle
porte l'identifiant et l'heure, à la seconde, de la ligne d'accord ; le code compare cette heure à celle de la ligne
`SCELLEMENT-LENTILLES-BBIS-V2` du registre propre et arrête si elle n'est pas strictement antérieure, ou si elle manque ;
(3) **le code ne lit aucune option dans la pièce** : il applique la règle de ce texte et contrôle la recopie ; (4) le
**marqueur** de la ligne d'accord est écrit entre doubles chevrons, une seule fois, pour que le validateur refuse le
scellement tant que la ligne n'est pas citée ; (5) **M2** : la forme jointe par « et » est admise dans les deux ordres, et
« séries … inchangées » seule ou jointe ; (6) **M3** : la phrase de tête « Reproduction de la première passe : non faite
[…] » n'est pas réécrite pour la passe encore en cours ; seuls les mots de la vérification 5 sont ajoutés ; (7) **clé
retirée** : le code ne l'exige ni ne la lit ; (8) les lieux du bloc « Brouillon 5 » qui disent les deux nœuds ouverts sont
laissés comme histoire et dits remplacés ; (9) dans « Lignes de registre », la ligne d'accord est dite de la session
principale sans nommer le registre (la vérification 5 nommait `registres/decisions.md`, le mandat `registres/go.md`).

**Nœuds pour Lazar** : **aucun nœud neuf de décision.** N12 et N17 sont tranchés (option (a) chacun ; N17 aux deux paliers) ;
N18 est tranché (option (a), GO-2026-11-19-92) ; N19 est clos (R-3995). Pour information au scellement, inchangé : la règle
sur une première passe lancée et non achevée (« Nœuds », fin). Pour information : sous l'option (a) de N12, si une de nos
lentilles sort au deuxième palier en ajustement seul ou en seconde course incomplète, **un mot de Lazar sera à demander
après l'avertissement de l'écart mesuré** ; sans lui, cette lentille n'est pas lue.

**Reste à faire après ce brouillon** : la vérification de ses corrections par le même contre-lecteur (R2, R-3735) ; la ligne
d'accord des nœuds N12 et N17, à inscrire par la session principale **avant le scellement**, et son marqueur ; les neuf
autres marqueurs ; la confirmation, par la session principale, des trois marqueurs portés par des rédacteurs ; la
consignation, par la session principale, du mot « go reco » du départ du rédacteur du brouillon 5 (M6) ; les couples L16 à
L19, et L12 et L15 pour information, à donner au lecteur désigné.

'''

MOT = "mot « go reco », note `cd02b0fb…`"

ENTREES = [
    ("P01", "forme", "tête : bloc « Brouillon 6 », avant le bloc du brouillon 5",
     "## Brouillon 5 — différences avec le brouillon 4\n", None,
     TETE + "@@AVANT@@"),

    ("P02", "M6", "bloc « Brouillon 5 », « Auteur » (brouillon 5, l. 26-28)",
     "ligne de registre que le rédacteur ait vue : il est cité d'après cette seule note)", None,
     """ligne de registre que le rédacteur ait vue : il est cité d'après cette seule note ; brouillon 6 : aucune ligne de
  `registres/go.md` ni de `registres/decisions.md` de la branche principale ne le porte au commit `@@MAIN@@…` (recherche du
  rédacteur du brouillon 6) ; il est donc consigné ici comme **mot rapporté** par la session des lentilles et sa note, citée
  seule ; il ouvrait un travail sans dépense ; la session principale peut le consigner, comme elle l'a fait à la ligne
  R-3994 pour le mot du brouillon 4 ; vérification des corrections du brouillon 5, M6)"""),

    ("P03", "M1", "bloc « Brouillon 5 », « Reste à faire » (l. 154)",
     "(couples L16, L17 et L19) ; les neuf marqueurs", None,
     """(couples L16 à L19 — L18 est dans le bloc séparable et dit le lieu et le libellé de V — et, pour
information, L12 et L15 ; liste corrigée au brouillon 6, vérification des corrections du brouillon 5, M1) ; les neuf marqueurs"""),

    ("P04", "tâche 1 (marqueur)", "en-tête de la v2, table des marqueurs : une ligne ajoutée (l. 485)",
     "(mot « go reco », 2026-11-19, 22:42:56Z), avec sa note et sa ligne de registre |\n", None,
     """@@AVANT@@  | LIGNE_D_ACCORD_DES_NOEUDS_N12_ET_N17 (ajouté au brouillon 6) | Nœuds, N12 et N17 | la session principale | l'identifiant et l'heure de la ligne par laquelle la session principale inscrit l'accord de Lazar du 2026-11-20 sur les nœuds N12 (option (a)) et N17 (option (a) aux deux paliers), mot « go reco » consigné par la note `cd02b0fb…` ; cette ligne est inscrite avant `SCELLEMENT-LENTILLES-BBIS-V2` (« Lignes de registre ») |
"""),

    ("P05", "tâche 1 (marqueur)", "en-tête de la v2, état des marqueurs (l. 494-496)",
     "différences du brouillon 2 à la version aura à lister aussi les changements des brouillons 3, 4 et 5, dont les pièces de\n  fabrication existent.\n", None,
     """@@AVANT@@
  **État des marqueurs au brouillon 6** : **un marqueur ajouté**, LIGNE_D_ACCORD_DES_NOEUDS_N12_ET_N17, à la session
  principale (la ligne d'accord du mot de Lazar du 2026-11-20 n'était pas sur la branche principale à l'écriture). **Dix
  restent** : les neuf du brouillon 5, mêmes porteurs, et celui-ci. Les trois marqueurs portés par des rédacteurs restent à
  confirmer par la session principale. La pièce des différences du brouillon 2 à la version aura à lister aussi les
  changements du brouillon 6, dont les pièces de fabrication existent.
"""),

    ("P06", "tâches 1 et 4", "« Changements de la v1 à la v2 », ligne 18 (l. 593)",
     "deux points restent ouverts (N12 pour l'ajustement seul, N17) | Nœuds | décisions |", None,
     "deux points restent ouverts aux brouillons 2 à 5 (N12 pour l'ajustement seul, N17) ; **tranchés par Lazar le 2026-11-20, option (a) chacun** (brouillon 6 ; ligne 30) | Nœuds | décisions |"),

    ("P07", "tâches 1 et 4", "« Changements de la v1 à la v2 », ligne 28 (l. 603)",
     "| 28 | **nœuds N12 et N17 laissés ouverts, texte écrit pour chaque option** (brouillon 5)",
     "(le défaut de N17 au deuxième palier demande un addendum après le verdict d'identité) |",
     "| 28 | **nœuds N12 et N17 laissés ouverts au brouillon 5** : le brouillon 5 écrivait le texte pour chaque option, faisait lire l'option qui vaut dans la pièce que nomme `GO-LENTILLES-BBIS-V2` et nommait une clé de registre pour un addendum de recopie ; **remplacé au brouillon 6** (lignes 30 et 31) : les deux nœuds sont tranchés, les textes des options écartées et cette clé sont retirés | Entrées ; Liste d'arrêt ; Lignes de registre ; Code neuf ; Nœuds | mandat du rédacteur du brouillon 5 ; contre-lecture 4, point 4 ; remplacé sur le mot de Lazar du 2026-11-20 |"),

    ("P08", "tâche 4", "« Changements de la v1 à la v2 », lignes 30 à 34 ajoutées (après la l. 604)",
     "contre-lecture 4, B1, B2, N1, N3, N4, N5, N9 |\n", None,
     """@@AVANT@@| 30 | **nœuds N12 et N17 tranchés par Lazar le 2026-11-20** (brouillon 6) : N12, option (a) — une de nos lentilles au deuxième palier, en ajustement seul ou en seconde course incomplète, n'est lue qu'après un mot de Lazar postérieur à l'avertissement de l'écart mesuré (ligne `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS`) ; ce mot ouvre ou non la lecture, il ne choisit aucune branche ; N17, option (a) aux deux paliers — ce texte vaut le texte de lecture neuf qu'exige CI ; aucun addendum de recopie ; la clé `ADDENDUM-RECOPIE-IDENTITE-LENTILLES-BBIS-V2`, nommée au brouillon 5, est retirée ; les textes écrits pour les options écartées sont retirés | Entrées ; Liste d'arrêt ; Lignes de registre ; Code neuf ; Nœuds | mot de Lazar « go reco » du 2026-11-20 (note `cd02b0fb…` ; ligne d'accord : « Nœuds ») |
| 31 | **issue des nœuds N12 et N17 fixée avant le scellement** (brouillon 6) : la pièce que nomme `GO-LENTILLES-BBIS-V2` ne fait que la recopier, avec sa ligne d'accord, inscrite avant `SCELLEMENT-LENTILLES-BBIS-V2` ; le code n'y lit aucune option ; pièce qui porte une autre issue, une ligne d'accord qui n'est pas antérieure au scellement, ou une autre forme : arrêt ; pièce muette : aucun arrêt, une phrase en tête | Lignes de registre ; Liste d'arrêt ; Code neuf | vérification des corrections du brouillon 5, C1 : une issue donnée après le scellement choisirait une branche de lecture après coup |
| 32 | **phrase du déclencheur (vi) : formes admises élargies** (brouillon 6) : sont admises aussi « séries … inchangées » et les deux faits joints par « et » | Entrées (fiche) ; Liste d'arrêt ; Code neuf | vérification des corrections du brouillon 5, M2 : CI, § 6, ne dit pas la forme de ces deux cas ; sans cela, un verdict conforme au critère arrêtait la seconde passe |
| 33 | **première passe encore en cours ; ligne des tables sans ligne des entrées** (brouillon 6) : pour une première passe encore en cours il n'y a pas de nœud de la v1, et si elle s'achève ses phrases sont celles de la première passe, la reproduction n'étant pas faite ; `TABLES-LENTILLES-BBIS` inscrite sans `ENTREES-LENTILLES-BBIS` : arrêt | Plan (11) ; Liste d'arrêt ; Code neuf | vérification des corrections du brouillon 5, M3 : deux trous de lettre de la règle du brouillon 5 |
| 34 | **corrections de lettre** (brouillon 6) : la lentille des logits nommée dans « Lien avec la première passe » ; description de la ligne `GO-LENTILLES-BBIS-V2` ; couples de la couche 15 à donner au lecteur désigné ; mot « go reco » du départ du rédacteur du brouillon 5 dit mot rapporté | Métrique (6) ; Plan (1) ; Lignes de registre ; Contre-lecture ; bloc « Brouillon 5 » | vérification des corrections du brouillon 5, M4, M5, M1, M6 |
"""),

    ("P09", "tâche 1 (N12)", "« Entrées », condition de lecture, variante ajustement seul (l. 1265)",
     "(lecture du rédacteur, portée à Lazar : nœud N12, reste à trancher)", None,
     "(lecture du rédacteur, portée à Lazar : nœud N12 ; **tranché par Lazar le 2026-11-20, option (a)** : brouillon 6)"),

    ("P10", "tâche 1 (N12) ; C1", "« Entrées », condition de lecture, alinéa « Nœud N12 laissé ouvert » (l. 1272-1280)",
     "  **Nœud N12 laissé ouvert (brouillon 5) : ce qui précède est écrit sous son option (a), qui est aussi son défaut.**",
     "si cette pièce ne dit rien de N12, l'option (a) vaut.",
     """  **Nœud N12 tranché par Lazar le 2026-11-20, option (a)** (brouillon 6 ; mot « go reco », note `cd02b0fb…` ; ligne
  d'accord : « Nœuds ») : **la règle qui précède est la seule.** En ajustement seul, ou en course rejouée dont la seconde
  course est incomplète, la lecture d'une de nos lentilles au deuxième palier **attend la ligne
  `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS`, postérieure à la ligne `AVERTISSEMENT-PALIER-2-LENTILLES-BBIS`** ; la
  ligne d'avertissement seule n'ouvre pas la lecture. **Ce mot de Lazar ouvre ou non la lecture de la lentille qu'il nomme ;
  il ne choisit aucune branche** : la phrase permise, son dernier crochet et la phrase gelée sont fixés ici et sont les mêmes
  quel que soit ce mot ; s'il n'est pas donné, ou si Lazar refuse la lecture (aucune ligne n'est alors inscrite), la lentille
  est non lue, sous le motif écrit plus haut. Ce mot n'est pas une issue de nœud donnée après le scellement (« Lignes de
  registre ») : ce texte fixe d'avance ce qu'est la lecture s'il l'ouvre et ce qui est écrit s'il ne l'ouvre pas. Les
  options (b) (l'avertissement suffit) et (c) (jamais lue) sont écartées ; les textes que le brouillon 5 avait écrits pour
  elles sont retirés. La fiche muette reste non lue. **L'issue de ce nœud est fixée par ce texte, avant son scellement** ; la
  pièce nommée par `GO-LENTILLES-BBIS-V2` ne fait que la recopier (« Lignes de registre »)."""),

    ("P11", "tâche 1 (N17) ; C1", "« Entrées », puce « par gabarit » (l. 1304-1316)",
     "Si Lazar ou la\n  session principale lit CI comme exigeant un texte écrit **après** le verdict d'identité",
     "rien de N17, le défaut vaut : (b) au deuxième palier, (a) au premier.",
     """**Nœud N17 tranché par
  Lazar le 2026-11-20 : option (a), aux deux paliers** (brouillon 6 ; mot « go reco », note `cd02b0fb…` ; ligne d'accord :
  « Nœuds ») : **ce texte vaut le texte de lecture neuf qu'exige CI, au premier palier comme au deuxième ; rien de plus
  n'est exigé.** Aucun addendum de recopie n'est écrit ni attendu : la clé `ADDENDUM-RECOPIE-IDENTITE-LENTILLES-BBIS-V2`,
  que le brouillon 5 nommait pour l'option (b), est **retirée** (sans objet : le code ne l'exige ni ne la lit), et le motif
  « Non lue […] addendum de recopie du verdict d'identité absent » n'existe plus. L'option (b) (un addendum contre-lu après
  le verdict d'identité) est écartée ; le texte que le brouillon 5 avait écrit pour elle est retiré. **L'issue de ce nœud
  est fixée par ce texte, avant son scellement** ; la pièce nommée par `GO-LENTILLES-BBIS-V2` ne fait que la recopier
  (« Lignes de registre »)."""),

    ("P12", "M2", "« Entrées », fiche de rangement, forme de la phrase du déclencheur (vi) (l. 1340)",
     "  soit « 31 matrices des moitiés égales sur 31 », soit des mots qui commencent par « série » et finissent par « inchangée ».", None,
     """  l'une de ces formes : (1) « 31 matrices des moitiés égales sur 31 » ; (2) des mots qui commencent par « série » et
  finissent par « inchangée » ; (3) des mots qui commencent par « séries » et finissent par « inchangées » (les deux séries
  sont inchangées) ; (4) la forme (1) et l'une des formes (2) ou (3), jointes par « et », dans un ordre ou dans l'autre
  (les deux faits tiennent). **Brouillon 6** (vérification des corrections du brouillon 5, M2) : CI, § 6, écrit les formes
  (1) et (2) entre crochets, sans dire la forme quand les deux faits tiennent ni quand les deux séries sont inchangées ; les
  formes (3) et (4) sont admises pour qu'un verdict conforme au critère n'arrête pas la seconde passe ; elles sont recopiées
  mot pour mot comme les deux autres, et aucune identité n'en est tirée."""),

    ("P13", "M4", "« Métrique », point 6, « Lien avec la première passe » (l. 1479-1482)",
     "et aucune\n     phrase de la lentille publique n'est écrite par la seconde passe avant ce nœud",
     "ses lectures de la lentille publique ne servent alors qu'aux comparaisons",
     """et aucune
     phrase de la lentille publique ni de la lentille des logits n'est écrite par la seconde passe avant ce nœud (brouillon 5 ;
     contre-lecture 4, B4 ; le plan, point 11, dit comment le code le sait ; brouillon 6 : la lentille des logits est nommée
     ici comme au plan, point 11) ; ses lectures de ces deux lentilles ne servent alors qu'aux comparaisons"""),

    ("P14", "M5", "« Plan d'analyse », point 1, ligne (i) (l. 1614-1615)",
     "(i) `GO-LENTILLES-BBIS-V2` (extrait des\n   décisions de Lazar sur N11 à N16, GO-2026-11-19-39 et -40 ; elle cite GO-2026-11-19-33)", None,
     """(i) `GO-LENTILLES-BBIS-V2` (extrait des
   décisions de Lazar sur N11 à N16, GO-2026-11-19-39 et -40, et recopie de GO-2026-11-19-92 (N18) et de l'issue de N12 et
   de N17, fixée avant le scellement (« Lignes de registre », brouillon 6) ; elle cite GO-2026-11-19-33)"""),

    ("P15", "M3", "« Plan d'analyse », point 11, alinéa « Non calculée » (après la l. 1820)",
     "    nœud de la v1. » Ces phrases ne sont écrites qu'après ce nœud, par la passe et sous le texte qu'il désigne.\n", None,
     """@@AVANT@@    **Passe encore en cours (brouillon 6 ; vérification des corrections du brouillon 5, M3)** : pour une première passe
    encore en cours au montage de la seconde, il n'y a pas de nœud de la v1 ; si la première passe s'achève ensuite
    (`TABLES-LENTILLES-BBIS` inscrite), les phrases de la lentille publique et de la lentille des logits sont celles de la
    première passe, la reproduction n'est pas faite, et c'est écrit. **`TABLES-LENTILLES-BBIS` inscrite sans
    `ENTREES-LENTILLES-BBIS`** : arrêt, forme mal comprise (« Liste d'arrêt »).
"""),

    ("P16", "tâche 1 (N12)", "« Liste d'arrêt », ligne « pour une lentille », cas de l'ajustement seul (l. 2040)",
     "(brouillon 5 : c'est l'option (a) du nœud N12, son défaut ; sous son option (b) : sans la ligne d'avertissement seulement ; sous son option (c) : toujours)", None,
     "(nœud N12 tranché par Lazar le 2026-11-20, option (a) : brouillon 6)"),

    ("P17", "tâche 1 (N17)", "« Liste d'arrêt », ligne « pour une lentille », cas de l'addendum de recopie (l. 2040)",
     " ; lentille à un palier où vaut l'option (b) du nœud N17 (son défaut : le deuxième palier) sans la ligne `ADDENDUM-RECOPIE-IDENTITE-LENTILLES-BBIS-V2`, ou dont l'addendum de recopie n'a pas l'empreinte de sa ligne (brouillon 5)", None,
     " (brouillon 6 : le cas de l'addendum de recopie, écrit ici au brouillon 5, est retiré ; nœud N17 tranché, option (a) aux deux paliers)"),

    ("P18", "M3", "« Liste d'arrêt », ligne « première passe lancée et non achevée » et une ligne ajoutée (l. 2052)",
     "ses lectures de ces deux lentilles ne servent qu'aux comparaisons entre lentilles ; le nœud est celui de la v1 (plan, point 11) |\n", None,
     """ses lectures de ces deux lentilles ne servent qu'aux comparaisons entre lentilles ; le nœud est celui de la v1 (plan, point 11) ; **passe encore en cours** (brouillon 6) : il n'y a pas de nœud de la v1 ; si elle s'achève ensuite (`TABLES-LENTILLES-BBIS` inscrite), les phrases de ces deux lentilles sont celles de la première passe, la reproduction n'est pas faite, et c'est écrit |
| `TABLES-LENTILLES-BBIS` inscrite au registre propre sans `ENTREES-LENTILLES-BBIS` (brouillon 6) | arrêt avant tout calcul ; nœud (la forme est mal comprise) |
"""),

    ("P19", "M2", "« Liste d'arrêt », ligne de la phrase du déclencheur (vi) (l. 2053)",
     "phrase d'une autre forme que celle de CI, § 6 (« Entrées », fiche) (brouillon 5)", None,
     "phrase d'une autre forme que les formes admises (« Entrées », fiche : celles de CI, § 6, « séries … inchangées », et les deux faits joints par « et » ; brouillon 6) (brouillon 5)"),

    ("P20", "C1 ; tâche 1", "« Liste d'arrêt », ligne de la pièce nommée par `GO-LENTILLES-BBIS-V2` (l. 2054)",
     "| pièce nommée par `GO-LENTILLES-BBIS-V2` qui dit l'issue du nœud N12 ou du nœud N17 dans une autre forme",
     "le défaut du nœud vaut) |",
     "| pièce nommée par `GO-LENTILLES-BBIS-V2` qui recopie l'issue du nœud N12 ou du nœud N17 **dans une autre forme** que celle de « Lignes de registre », ou qui porte **une autre issue** que celle de ce texte (N12 : option (a) ; N17 : option (a) aux deux paliers), ou d'après **une ligne d'accord postérieure à `SCELLEMENT-LENTILLES-BBIS-V2`**, de la même seconde, ou sans heure lisible (brouillon 6) | arrêt avant tout calcul ; nœud : « issue des nœuds N12 et N17 non conforme au texte scellé » (une issue donnée après le scellement de ce texte, ou autre que la sienne, est un écart à un préenregistrement scellé : version neuve ; une pièce qui ne dit rien d'un nœud n'arrête pas : l'issue de ce texte vaut, et c'est écrit en tête) |"),

    ("P21", "M5", "« Lignes de registre », liste des clés ajoutées par la v2 (l. 2207-2208)",
     "`GO-LENTILLES-BBIS-V2` (extrait des décisions de Lazar GO-2026-11-19-39 et -40 sur N11 à N16, citant\nGO-2026-11-19-33)", None,
     """`GO-LENTILLES-BBIS-V2` (extrait des décisions de Lazar GO-2026-11-19-39 et -40 sur N11 à N16, citant
GO-2026-11-19-33, et recopie de GO-2026-11-19-92 (N18) et de l'issue de N12 et de N17 : point (i) ci-dessous, brouillon 6)"""),

    ("P22", "C1 ; tâche 1", "« Lignes de registre », alinéa « Brouillon 5 », points (i) et (ii) (l. 2220-2228)",
     "**Brouillon 5** : (i) la pièce que nomme `GO-LENTILLES-BBIS-V2` recopie aussi la ligne GO-2026-11-19-92",
     "avant `MONTAGE-LENTILLES-BBIS-V2` (« Entrées », lecture « par gabarit »).",
     """**Brouillon 5, repris au brouillon 6** (nœuds N12 et N17 tranchés ; vérification des corrections du brouillon 5, C1) : (i) la
pièce que nomme `GO-LENTILLES-BBIS-V2` recopie aussi la ligne GO-2026-11-19-92 (nœud N18, option (a)) et **l'issue des nœuds
N12 et N17**. **Cette issue est fixée avant le scellement de ce texte, par le mot de Lazar du 2026-11-20** (« Nœuds ») :
N12, option (a) ; N17, option (a) aux deux paliers. La pièce **ne fait que la recopier**, sur une ligne par nœud, de la forme
« N12 : option (a) ; ligne d'accord [identifiant], [AAAA-MM-JJTHH:MM:SSZ] » et « N17 : option (a) au premier palier ; option
(a) au deuxième palier ; ligne d'accord [identifiant], [AAAA-MM-JJTHH:MM:SSZ] », où l'identifiant et l'heure sont ceux de la
ligne par laquelle la session principale inscrit l'accord de Lazar, **inscrite avant `SCELLEMENT-LENTILLES-BBIS-V2`**. Une
issue donnée après le scellement de ce texte est un écart à un préenregistrement scellé : version neuve, nœud. **Le code ne
lit dans la pièce aucune option** : la règle qu'il applique est celle de ce texte (« Entrées », condition de lecture) ; il
contrôle seulement que la pièce la recopie. **Arrêt nommé**, avant tout calcul (« Liste d'arrêt ») : une ligne d'une autre
forme ; une autre issue que celle de ce texte ; une ligne d'accord dont l'heure n'est pas strictement antérieure à celle de
la ligne `SCELLEMENT-LENTILLES-BBIS-V2` du registre propre, ou dont l'heure est absente ou illisible. Si la pièce ne dit
rien d'un nœud, rien n'arrête : l'issue de ce texte vaut, et la seconde passe écrit en tête « Issue du nœud [N12 | N17] :
non recopiée par la pièce de `GO-LENTILLES-BBIS-V2` ; celle du texte scellé vaut. » Les défauts des deux nœuds, que le
brouillon 5 faisait valoir pour une pièce muette, n'ont plus d'emploi. (ii) **Clé retirée** : la clé conditionnelle
`ADDENDUM-RECOPIE-IDENTITE-LENTILLES-BBIS-V2`, que le brouillon 5 nommait pour un addendum de recopie du verdict d'identité,
est sans objet (nœud N17, option (a) aux deux paliers) : ce n'est pas une clé de ce texte, et le code ne l'exige ni ne la lit."""),

    ("P23", "M2", "« Code neuf », essai de la phrase du déclencheur (vi), cas sains (l. 2401-2402)",
     "dans chacune de ses deux formes\n  (« 31 matrices des moitiés égales sur 31 » ; « série … inchangée »)", None,
     """dans chacune de ses formes admises
  (« 31 matrices des moitiés égales sur 31 » ; « série … inchangée » ; brouillon 6 : « séries … inchangées » ; les deux faits
  joints par « et », dans les deux ordres)"""),

    ("P24", "M2", "« Code neuf », essai de la phrase du déclencheur (vi), artefacts (l. 2404-2405)",
     "forme (début, milieu ou fin changés d'un mot) : arrêt, forme mal comprise, chacun ;", None,
     "forme (début, milieu ou fin changés d'un mot ; brouillon 6 : deux formes jointes par un autre mot que « et », ou la même\n  forme deux fois) : arrêt, forme mal comprise, chacun ;"),

    ("P25", "M3", "« Code neuf », essai « première passe lancée et non achevée » (l. 2412)",
     "(présence d'une phrase de la lentille publique dans la sortie : échec) ;\n", None,
     """(présence d'une phrase de la lentille publique dans la sortie : échec) ; **brouillon 6** : artefact :
  `TABLES-LENTILLES-BBIS` présente, `ENTREES-LENTILLES-BBIS` absente : arrêt, forme mal comprise ;
"""),

    ("P26", "C1 ; tâche 1", "« Code neuf », essai « options des nœuds N12 et N17 » (l. 2420-2425)",
     "- **options des nœuds N12 et N17** (pièce jouet nommée par `GO-LENTILLES-BBIS-V2`)",
     "  N17 : (b) au deuxième palier, (a) au premier ; ligne d'issue d'une autre forme : arrêt ;",
     """- **issue des nœuds N12 et N17** (brouillon 6 ; registre jouet et pièce jouet nommée par `GO-LENTILLES-BBIS-V2`) : **cas
  sain** : pièce qui recopie « N12 : option (a) » et « N17 : option (a) au premier palier ; option (a) au deuxième palier »,
  chacune avec une ligne d'accord datée avant `SCELLEMENT-LENTILLES-BBIS-V2` : rien n'arrête ; **artefacts**, chacun un
  arrêt nommé : ligne d'accord datée après `SCELLEMENT-LENTILLES-BBIS-V2`, ou de la même seconde ; heure absente ou
  illisible ; pièce qui porte une autre issue (N12 : option (b) ou (c) ; N17 : option (b) à un palier) ; ligne d'une autre
  forme ; **pièce muette sur un nœud** : aucun arrêt, la phrase « Issue du nœud […] : non recopiée […] » est écrite en tête
  (artefact : un code qui se tait est vu). **Règle de N12** : deuxième palier en ajustement seul, puis en seconde course
  incomplète : lue avec la ligne `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS` postérieure à la ligne d'avertissement (cas
  sain) ; non lue sans elle, avec la seule ligne d'avertissement, ou avec une ligne antérieure à l'avertissement
  (artefacts : un code qui lit sur le seul avertissement est vu). **Règle de N17** : aucune ligne
  `ADDENDUM-RECOPIE-IDENTITE-LENTILLES-BBIS-V2` n'est exigée, à aucun palier : lentille au deuxième palier lue sans elle
  (cas sain) ; un code qui l'exige, ou qui écrit un motif « addendum de recopie […] absent », est vu (artefact) ;"""),

    ("P27", "tâche 1 (N12)", "« Nœuds », N12, option (b) réécrite : renvoi (l. 2473)",
     "(CI, § 5, la traite de même), voir le point ouvert ci-dessous.", None,
     "(CI, § 5, la traite de même), voir ci-dessous la part propre à l'ajustement seul, tranchée par Lazar le 2026-11-20,\n  option (a) (brouillon 6)."),

    ("P28", "tâche 1 ; C1", "« Nœuds », titre « Restent ouverts, pour Lazar » (l. 2493)",
     "**Restent ouverts, pour Lazar** (format de décision du dépôt) :\n", None,
     """**Ouverts au brouillon 2, tranchés par Lazar le 2026-11-20, option (a) chacun** (brouillon 6). Mot de Lazar, donné dans la
session des lentilles (`session_01XJ6Mgr9o68QqLiFTLg3zRW`) : « go reco », relevé le 2026-11-20 à 05:21:23Z, en réponse à la
question que cette session lui posait après la vérification des corrections du brouillon 5, avec deux recommandations :
N12, option (a), confiance 0,7 ; N17, option (a) aux deux paliers, confiance 0,65. Il est consigné par la note
`docs/notes/neuron-lens-v1/mot-lazar-noeuds-n12-n17-et-brouillon6-2026-11-20-v1.md`,
`cd02b0fb85e06b0366d731bb9888d753562c8d76cbef403874587975da9c99ed` (branche des lentilles). Ligne d'accord de la session
principale : <<LIGNE_D_ACCORD_DES_NOEUDS_N12_ET_N17>> (cherchée par le rédacteur du brouillon 6 dans `registres/go.md` et
`registres/decisions.md` de la branche principale, au commit `@@MAIN@@…` : non trouvée ; marqueur porté par la session
principale, avant le scellement). **Ce mot est donné avant le scellement de ce texte : l'issue des deux nœuds est fixée
avant le scellement et avant toute lecture** (vérification des corrections du brouillon 5, C1). Les défauts des deux nœuds,
qui seraient tombés vers le 2026-11-21, n'ont plus d'emploi. Ce qui suit est chaque nœud tel qu'il a été posé (format de
décision du dépôt), gardé pour mémoire, puis ce qui est retenu :
"""),

    ("P29", "tâche 1 (N12)", "« Nœuds », N12, alinéa « Brouillon 5 » (l. 2506-2511)",
     "  **Brouillon 5 : nœud laissé ouvert ; le brouillon 5 ne le tranche pas.** Ouvert au brouillon 2 (2026-11-19, vers 11:08Z),\n  son défaut, (a), tombe",
     "muette : (a). Aucune de ces options ne demande une version neuve de ce texte.",
     """  **Brouillon 6 : tranché par Lazar le 2026-11-20, option (a).** Il faut un mot de Lazar postérieur à l'avertissement de
  l'écart mesuré, inscrit par la ligne `NOEUD-PALIER-2-AJUSTEMENT-SEUL-LENTILLES-BBIS` ; la forme de la lecture est fixée
  par ce texte ; **ce mot ouvre ou non la lecture, il ne choisit aucune branche** (« Entrées », condition de lecture). Les
  options (b) et (c) sont écartées ; les textes que le brouillon 5 avait écrits pour elles sont retirés. Aucune version
  neuve de ce texte n'est nécessaire."""),

    ("P30", "tâche 1 (N17)", "« Nœuds », N17, alinéa « Brouillon 5 » (l. 2519-2530)",
     "  **Brouillon 5 : nœud laissé ouvert ; le brouillon 5 ne le tranche pas.** Ouvert au brouillon 2 (2026-11-19, vers 11:08Z),\n  son défaut tombe",
     "`GO-LENTILLES-BBIS-V2` ; pièce muette : le défaut.",
     """  **Brouillon 6 : tranché par Lazar le 2026-11-20, option (a), aux deux paliers.** Ce texte, scellé avant le réajustement,
  vaut le texte de lecture neuf qu'exige CI, au premier palier comme au deuxième ; rien de plus n'est exigé (« Entrées »,
  puce « par gabarit »). L'option (b) est écartée : aucun addendum de recopie n'est écrit ni attendu ; la clé
  `ADDENDUM-RECOPIE-IDENTITE-LENTILLES-BBIS-V2`, nommée au brouillon 5, est retirée (sans objet), avec tout ce qui en
  dépendait : la condition de lecture et son motif « Non lue […] addendum de recopie […] absent » (« Entrées »), le cas de
  la liste d'arrêt, la clé conditionnelle (« Lignes de registre ») et ses essais (« Code neuf »)."""),

    ("P31", "M1 ; forme", "« Contre-lecture », entrée 4, phrase du brouillon 5 (l. 2719-2720)",
     "donner les couples L16, L17 et L19 (couche 15). Aucune\n  empreinte entière n'est répétée ici, pour la même raison.", None,
     """donner les couples L16 à L19 (couche 15 ; L18 est dans le
  bloc séparable et dit le lieu et le libellé de V) et, pour information, L12 et L15 (liste corrigée au brouillon 6 ;
  vérification des corrections du brouillon 5, M1). Aucune empreinte entière n'est répétée ici, pour la même raison.
  **Brouillon 6** : la vérification des corrections du brouillon 5 a eu lieu (même contre-lecteur, sur Opus 5.5,
  2026-11-20, rapport `04282064…`, « scellable après corrections » : une correction bloquante, C1, six non bloquantes, M1 à
  M6 ; chemin et empreinte entière dans le bloc « Brouillon 6 ») ; il reste la vérification des corrections de ce brouillon
  par le même contre-lecteur ; le marqueur de cette entrée reste donc, à la session principale. À qui vérifie ce brouillon,
  donner explicitement : le brouillon 5 ; les trois pièces de fabrication du brouillon 6 (script des couples, sa sortie, le
  `diff`) ; le rapport de la vérification des corrections du brouillon 5 ; la note du mot de Lazar sur les nœuds N12 et N17
  (`cd02b0fb…`) et sa ligne d'accord, si elle est inscrite ; CI dans sa version 8 (§ 6, pour la correction M2) ; le mandat
  du rédacteur du brouillon 6. Au lecteur désigné par Lazar : rien de plus que les couples dits ci-dessus, le brouillon 6
  ne touchant pas le bloc séparable. Aucune empreinte entière n'est répétée ici, pour la même raison."""),

    ("P32", "forme ; tâche 5", "pied : pied du brouillon 6, après celui du brouillon 5",
     "Pied (v2, brouillon 5) : écriture achevée le 2026-11-20 à 00:02:01 UTC", "ne doit pas l'être.\n",
     """@@AVANT@@
Pied (v2, brouillon 6) : écriture achevée le 2026-11-20 à @@FIN@@ UTC (`date -u`), juste avant le dernier passage du validateur. @@REFUS@@ Contrôle de la v1 dans ce brouillon (programme de la contre-lecture 3, annexe B, recopié mot pour mot) : @@CONTROLE_PIED@@ Bornes du bloc séparable : une occurrence de la ligne de début, une de la ligne de fin (contrôle du script des couples) ; aucun couple ne touche le bloc. `controle_ia.prereg.problemes` sur ce brouillon rend deux manques, **attendus et voulus** : « contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport) » et « marqueurs de gabarit restants » (dix marqueurs : les neuf du brouillon 5, et celui de la ligne d'accord des nœuds N12 et N17, ajouté par ce brouillon) ; il ne rend aucune section absente ou vide. Ce brouillon n'est donc pas scellable comme préenregistrement en l'état, et ne doit pas l'être.
"""),
]

CONTROLE = "à remplir"
CONTROLE_PIED = "791 lignes égales, aucune supprimée, 10 prolongées (182, 320, 351, 356, 358, 385, 476, 478, 480, 600), 13 réécrites (1, 147, 263, 321, 322, 335, 336, 337, 339, 461, 465, 466, 467), comme aux brouillons 3, 4 et 5 ; première ligne de sortie du programme : « 791 0 23 @@INS@@ »."
REFUS = "Aucun refus d'outil, de permission ni de classifieur pendant la lecture des pièces ni pendant l'écriture."
