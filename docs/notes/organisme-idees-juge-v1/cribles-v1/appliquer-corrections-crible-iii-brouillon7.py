"""Brouillon 7 du préenregistrement du crible (iii) : réécriture sur la variante « crédits de Claude au maximum » (décision de
la mère, R-2992, point 1), N = 20 mondes dans tous les cas (R-2992), remarques facultatives R-1 à R-6 des lectures du brouillon 4
reprises ; la contre-lecture du brouillon 6 (`contre-lecture-crible-iii-b4-tour3-v1.md`, tour 3 de la lecture du brouillon 4)
n'exige aucune correction.

Couples « ancien → nouveau » écrits par le rédacteur du brouillon 7 (modèle A ; le rapport n'en donne aucun), listés ci-dessous
dans l'ordre du texte ; chaque « ancien » est copié à l'octet du brouillon 6.
Gardes : empreinte de la pièce de départ (brouillon 6) et du rapport ; nombre de couples attendu ; chaque « ancien » figure
exactement une fois dans la pièce de départ ; aucun chevauchement entre « anciens » ; chaque « nouveau » figure dans la cible ;
la cible (et son compagnon) ne doit pas exister et n'est jamais écrasée (ouverture en mode « x ») ; le validateur
`controle_ia.prereg.problemes` est rejoué sur le texte neuf (copie temporaire) avant toute écriture de la cible et doit rendre
une liste vide ; aucun repli silencieux. Bibliothèque standard seule (le validateur est appelé par `.venv/bin/python` avec
`PYTHONPATH=src`) ; aucun appel de modèle, aucune donnée.
Usage : python3 -I appliquer-corrections-crible-iii-brouillon7.py  (depuis n'importe quel dossier)
"""
import hashlib
import os
import subprocess
import sys
import tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
DEPOT = os.path.abspath(os.path.join(ICI, "..", "..", "..", ".."))
SOURCE = os.path.join(ICI, "crible-iii-brouillon6.md")
SOURCE_SHA = "f377e927aab482b39ccda892adc178a1cbfaac7a8042bf9215047f303f72189d"
RAPPORT = os.path.join(ICI, "contre-lecture-crible-iii-b4-tour3-v1.md")
RAPPORT_SHA = "99fb10247b295f053a8ecfa8b6464c0f4b445146cc7f67f970a0de514ec70e2e"
CIBLE = os.path.join(ICI, "crible-iii-brouillon7.md")


def arret(msg):
    sys.stderr.write("ARRÊT : " + msg + "\n")
    sys.exit(2)


def sha(chemin):
    return hashlib.sha256(open(chemin, "rb").read()).hexdigest()


COUPLES = [
    ("E-titre",
     """loi écrite par un proposeur cher — brouillon 6
""",
     """loi écrite par un proposeur cher — brouillon 7 (variante « crédits de Claude au maximum »)
"""),
    ("R-2a",
     """même dossier. Je n'ai écrit ni la note
""",
     """même dossier. L'auteur n'a écrit ni la note
"""),
    ("E-puce7",
     """  rien lu de la sortie du pilote MR-2 v14 ; aucun commit, aucune poussée. Rien d'autre que les 4 couples du rapport, l'en-tête
  et la section « Contre-lecture » ne change.
""",
     """  rien lu de la sortie du pilote MR-2 v14 ; aucun commit, aucune poussée. Rien d'autre que les 4 couples du rapport, l'en-tête
  et la section « Contre-lecture » ne change.
- Brouillon 7 : **réécriture sur la variante « crédits de Claude au maximum »** (Pr-2 choisit, Pr-4 écrit, S = un appel de Pr-4),
  forme décidée par la mère (R-2992, point 1, ligne du 2026-11-16 à 14:52 UTC, `date -u`), avec **N = 20 mondes dans tous les
  cas** (R-2992) et les remarques facultatives R-1 à R-6 des lectures du brouillon 4 reprises (aucune ne change un critère) ; la
  contre-lecture du brouillon 6 (tour 3 de la lecture du brouillon 4) n'exige aucune correction. Écrit le 2026-11-16T15:06:52Z
  (`date -u`, au scellement) par un rédacteur neuf du modèle A, qui n'a écrit ni les brouillons 1 à 6 ni les rapports de
  contre-lecture (identité dite en conversation seulement), au moyen du programme `appliquer-corrections-crible-iii-brouillon7.py`
  (même dossier, scellé) ; dépôt lu sur `main` (tête `64540acd`) ; procédure v14 relue au commit `2d35cafa…` et [PILOTE] relu
  (bloc gelé, « Devis ») par `git show`, après deux `git fetch` à refspec ; rien lu de la sortie du pilote MR-2 v14 ; aucun
  commit, aucune poussée. Ce qui change, point par point : section « Contre-lecture », entrée 6. **Rédacteurs** : les correcteurs
  des brouillons 2 à 6 étaient du modèle A (vérifié par la mère dans les journaux des sous-agents, R-2992, point 0) ; aucune
  mention d'un rédacteur « lettre C » ne figure dans ce texte ; les lecteurs dont les rapports sont versés étaient du modèle C.
"""),
    ("R-2b",
     """**non relues par moi** (pièce sous `runs/`)""",
     """**non relues par l'auteur** (pièce sous `runs/`)"""),
    ("E-registre",
     """R-2883, R-2968 à R-2970 (registre vivant) ;""",
     """R-2883, R-2968 à R-2970, R-2977, R-2992 (registre vivant) ;"""),
    ("E-statut",
     """**Statut.** Brouillon 6, **contre-lu cinq fois** (tours 1 à 3, puis deux tours de la lecture du brouillon 4 ; corrections appliquées, section « Contre-lecture ») ; **non scellé
comme texte qui fait foi** (R1, R2), et **non scellable** tant que la forme du crible n'est pas tranchée par la mère et
inscrite (« Choix et doutes », point 4). Aucune dépense, aucun appel de modèle, aucun monde tiré.""",
     """**Statut.** Brouillon 7, **réécrit sur la variante « crédits de Claude au maximum »**, forme tranchée et inscrite par la mère
(R-2992, point 1, 2026-11-16 à 14:52 UTC, avant toute lecture de l'issue du pilote ; « Choix et doutes », point 4) ; les
brouillons 1 à 6, rédigés dans la forme fidèle à [NOTE], ont été contre-lus six fois (section « Contre-lecture ») ; **la
réécriture n'est pas encore contre-lue** : un tour sur le différentiel du brouillon 6 à ce brouillon 7 est **obligatoire** avant
tout scellement (R-2992, point 1 ; R2) ; **non scellé comme texte qui fait foi** (R1, R2). Les prédictions III-2 et III-7 sont
refaites pour la variante dans ce brouillon, avant toute lecture du pilote ; les autres sont celles des brouillons 1 à 6.
Aucune dépense, aucun appel de modèle, aucun monde tiré."""),
    ("E-validateur",
     """aucun défaut sur ce brouillon 6 (vérifié""",
     """aucun défaut sur ce brouillon 7 (vérifié"""),
    ("S0-1",
     """(QO1 au sens dit en « Hypothèse » : Pr-2 contre Pr-1, deux espèces de frontière, non l'instrument local) ?""",
     """(QO1 au sens dit en « Hypothèse » : Pr-4 contre Pr-2, deux espèces de frontière d'une même maison, deux paliers de prix, non l'instrument local) ?"""),
    ("S0-2",
     """2. **Quatre bras** sur les mêmes 20 mondes MR-2, archive {K1}, une génération : S standard (Pr-2) ; D deux passes (Pr-1 choisit,
   Pr-2 écrit) ; H ensembles au hasard (programme, puis Pr-2) ; B tout bon marché (Pr-2 remplacé par Pr-1 **sur les ensembles
   mêmes de D**). 100 appels ; aucun juge, aucun test de mort (N-058).""",
     """2. **Quatre bras** sur les mêmes 20 mondes MR-2, archive {K1}, une génération : S standard (Pr-4) ; D deux passes (Pr-2 choisit,
   Pr-4 écrit) ; H ensembles au hasard (programme, puis Pr-4) ; B tout bon marché, le choisisseur écrit (Pr-4 remplacé par Pr-2
   **sur les ensembles mêmes de D**). 100 appels, tous sur crédits de Claude (variante, R-2992) ; aucun juge, aucun test de mort
   (N-058)."""),
    ("S0-7",
     """7. **Prédiction de l'auteur** : P1 « non tranché », Δ_R ≤ 0 en estimation et ρ_DS ≤ 1 (confiance 0,5) ; P2 : la passe chère couvre au moins une
   demi-composante de plus par monde (0,45) ; D ≈ H (0,5).""",
     """7. **Prédiction de l'auteur** : P1 « non tranché », Δ_R ≤ 0 en estimation et ρ_DS ≤ 1 (confiance 0,5) ; P2 : la passe chère couvre
   davantage, entre 0 et + 0,5 composante de plus par monde en estimation, issue « non tranché » (0,4) ; D ≈ H (0,5)."""),
    ("S0-8",
     """8. **Devis (brouillon, estimé)** : 58,30 USD attendus aux prix de [NOTE] (48 sur crédits de Claude, 10,30 hors crédits ; mes
   fourchettes : 48 à 62) ; **216,60 au pire**
   (120 sur crédits, 96,60 hors crédits), sous les 243 de [NOTE] : B réemploie la passe 1 de D (− 40), les plafonds de Pr-1 sont
   2,34 et non 2,00 (+ 13,60) ; variante « crédits de
   Claude au maximum » (Pr-2 choisit, Pr-4 écrit) : ≈ 128,30 attendus, 263 au pire, dont 3 hors crédits.""",
     """8. **Devis (brouillon, estimé ; variante « crédits de Claude au maximum », R-2992)** : 128,30 USD attendus aux prix de [NOTE]
   (128 sur crédits de Claude, 0,30 hors crédits : la machine ; fourchettes de ce texte au prix public : 94,90 à 121,04) ;
   **263 au pire** (260 sur crédits, 3 hors crédits), au-dessus des 243 de [NOTE] (forme fidèle) : B réemploie la passe 1 de D
   (− 20 appels), l'écriture passe à Pr-4 (plafond de session 3) ; forme fidèle (Pr-1 choisit, Pr-2 écrit), écartée par la
   mère : 58,30 attendus, 216,60 au pire, dont 96,60 hors crédits."""),
    ("S0-9a",
     """5 files de 4 mondes en parallèle (6 files de 4 pour 24 mondes) ;""",
     """5 files de 4 mondes en parallèle (N = 20 dans tous les cas, R-2992) ;"""),
    ("S0-9b",
     """le monde r va à la file r modulo F (F = 5, ou 6 si N = 24), dans l'ordre""",
     """le monde r va à la file r modulo 5, dans l'ordre"""),
    ("S0-10",
     """trois appels sur un monde de développement, ≈ 1,05 à 1,40 USD
    au prix public, 6,68 au pire), avant les 100 appels.""",
     """trois appels sur un monde de développement, ≈ 2,08 à 2,73 USD
    au prix public, 7,00 au pire, sur crédits de Claude), avant les 100 appels."""),
    ("H-ctx",
     """la frontière (ici Pr-2 contre Pr-1, deux espèces de frontière au sens de N-045 : l'instrument local n'est pas joué) pour""",
     """la frontière (ici Pr-4 contre Pr-2, deux espèces de frontière d'une même maison au sens de N-045, deux paliers de prix : l'instrument local n'est pas joué, aucun proposeur d'une autre maison non plus) pour"""),
    ("H-iii",
     """**H-iii** (énoncé de [NOTE] § 3 (iii)). Dans une génération partie de {K1}, sur la famille MR-2, les deux passes (Pr-1 propose
vingt ensembles de 1 à 3 traits ; filtre ; Pr-2 écrit une carte par ensemble retenu) couvrent **davantage de composantes
certifiées par dollar** qu'un appel standard de Pr-2.""",
     """**H-iii** (énoncé de [NOTE] § 3 (iii), proposeurs de la variante, R-2992). Dans une génération partie de {K1}, sur la famille
MR-2, les deux passes (Pr-2 propose vingt ensembles de 1 à 3 traits ; filtre ; Pr-4 écrit une carte par ensemble retenu)
couvrent **davantage de composantes certifiées par dollar** qu'un appel standard de Pr-4.

**La variante change-t-elle la question de [NOTE] ?** Oui, un peu ; c'est dit ici, **sans trancher** (si la question n'est plus
celle de la note, c'est à la mère ou à Lazar de le dire). [NOTE] § 3 (iii) fait choisir les traits par Pr-1 (hors crédits) et
écrire la loi par Pr-2 ; la variante (R-2992) fait choisir par Pr-2 et écrire par Pr-4 : deux espèces de frontière d'une même
maison, deux paliers de prix (rapport de prix par jeton de 2, aux prix publics comme aux prix de la configuration). Restent
les mêmes : la structure (un choisisseur moins cher, un écrivain plus cher), les quatre bras, le filtre, les mesures, et la
partition de [NOTE] (Pr-1 et Pr-2 « moitié bon marché », Pr-3 et Pr-4 « moitié chère », idée (v)). Changent la paire de
proposeurs et donc la portée : une conclusion porte sur « deux paliers de prix d'une même maison », non sur « un proposeur bon
marché d'une autre maison contre un proposeur cher » ; la diversité d'espèces que la forme fidèle gardait est perdue ; la
nécessité de la frontière au sens complet de QO1 (l'instrument local) n'est posée dans aucune des deux formes."""),
    ("H-a",
     """quand Pr-1 remplace Pr-2 (B contre D).""",
     """quand Pr-2 remplace Pr-4 (B contre D)."""),
    ("H-b",
     """ce que le choix de Pr-1 apporte au-delà du seul""",
     """ce que le choix de Pr-2 apporte au-delà du seul"""),
    ("P-III2",
     """| III-2 | **principale P2** : δ_DB (mêmes ensembles, écrivain cher contre bon marché) | + | ≥ + 0,5 composante par monde ; « perte établie sans le proposeur cher » | borne haute à 97,5 % < 0 | 0,45 |""",
     """| III-2 | **principale P2** : δ_DB (mêmes ensembles, écrivain cher Pr-4 contre bon marché Pr-2, même maison) | + | estimation entre 0 et + 0,5 composante par monde ; issue « non tranché » | estimation de δ_DB ≤ 0 (réfute le signe) ; issue autre que « non tranché » (réfute l'issue) | 0,4 |"""),
    ("P-III7",
     """| III-7 | coût relatif $_D / $_S (prix publics) | > 1 | 1,05 à 1,6 | < 1 | 0,6 |
""",
     """| III-7 | coût relatif $_D / $_S (prix publics) | > 1 | 1,05 à 1,25 | < 1 | 0,6 |

**Portée de la colonne « ce qui la réfute »** (remarque R-4) : une prédiction dont le chiffre est manqué sans que cette colonne
soit atteinte n'est **ni confirmée ni réfutée** (par exemple III-2 avec une estimation de + 0,7 et l'issue « non tranché ») ; le
rapport le dit tel quel.
"""),
    ("P-raisons",
     """D paie en plus l'appel de Pr-1 (III-7). III-2 : rien ne
mesure encore Pr-1 comme écrivain sur MR-2 ; je parie sur l'écart de prix. III-3""",
     """D paie en plus l'appel de Pr-2 (III-7 : une passe 1 de
≈ 2 000 à 10 000 jetons de sortie coûte 0,10 à 0,27 USD, contre 1,32 à 1,64 pour un appel d'écriture de Pr-4). III-2 : rien ne
mesure encore Pr-2 face à Pr-4 comme écrivain sur MR-2 ; deux espèces d'une même maison devraient écrire plus près l'une de
l'autre que deux espèces de maisons différentes : le pari porte sur un petit écart, du signe de l'écart de prix. III-3"""),
    ("P-issues",
     """P2 « perte établie » : le proposeur cher sert à l'écriture, par rapport à l'autre espèce de frontière (pour
ce rôle, ce moment, cette famille) ; P2 « sans perte notable » : Pr-1 écrit presque aussi bien""",
     """P2 « perte établie » : le proposeur cher sert à l'écriture, par rapport au palier bas de la même maison (pour
ce rôle, ce moment, cette famille) ; P2 « sans perte notable » : Pr-2 écrit presque aussi bien"""),
    ("M-bras",
     """- **Bras** (même monde, même archive, mêmes épisodes servis) : **S** : un appel de Pr-2, gabarit du pilote (`e77d3041…`),
  inchangé. **D** : passe 1 de Pr-1, filtre, puis passe 2 de Pr-2 (gabarit G2, neuf, portant les k ensembles). **H** : vingt
  ensembles tirés par le programme (taille uniforme sur {1, 2, 3}, traits uniformes sans remise parmi 8), même filtre, puis passe 2
  de Pr-2. **B** : passe 2 de **Pr-1**, sur **les ensembles mêmes de D** (texte servi égal à l'octet à celui de D).""",
     """- **Bras** (même monde, même archive, mêmes épisodes servis) : **S** : un appel de Pr-4, gabarit du pilote (`e77d3041…`),
  inchangé. **D** : passe 1 de Pr-2, filtre, puis passe 2 de Pr-4 (gabarit G2, neuf, portant les k ensembles). **H** : vingt
  ensembles tirés par le programme (taille uniforme sur {1, 2, 3}, traits uniformes sans remise parmi 8), même filtre, puis passe 2
  de Pr-4. **B** : passe 2 de **Pr-2**, sur **les ensembles mêmes de D** (texte servi égal à l'octet à celui de D)."""),
    ("M-dollars",
     """- **Dollars** (prix publics de la note des prix v2 en principal ; prix de la configuration v12 en sensibilité : Pr-1 10 / 50, Pr-2 4 / 20, Pr-4 8 / 40, Pr-3 10 / 50 ; prix publics : Pr-1 2 / 10 jusqu'au 30 novembre, Pr-2 4 / 20, Pr-4 8 / 40, Pr-3 10 / 50 ; note des prix v2, `b88253b8…`) :""",
     """- **Dollars** (prix publics de la note des prix v2 en principal, décision de la mère, R-2977 ; prix de la configuration v12 en sensibilité ; pour les deux proposeurs de ce crible, les deux barèmes sont égaux : Pr-2 4 / 20, Pr-4 8 / 40 USD par million de jetons d'entrée / de sortie ; la sensibilité est donc vide, et rapportée comme telle ; note des prix v2, `b88253b8…`) :"""),
    ("M-qualite",
     """part des ensembles valides de Pr-1 et des ensembles retenus""",
     """part des ensembles valides de Pr-2 et des ensembles retenus"""),
    ("M-sens",
     """toutes les composantes ; prix de la configuration ; mondes non""",
     """toutes les composantes ; prix de la configuration (égaux aux prix publics ici : vide) ; mondes non"""),
    ("S-N",
     """- **Nombre de mondes N** (décision de la mère, R-2977, règle écrite d'avance) : **N = 24** si le taux de réussite par appel du pilote MR-2 v14 est
  **sous 0,95**, N = 20 sinon ; taux = appels répondus (définition de [PILOTE]) sur appels faits, des deux relais employés ici, calculé par
  le programme de mesure du pilote sur sa sortie scellée par un lecteur neuf, avant le scellement de ce texte, et recopié ici.""",
     """- **Nombre de mondes : N = 20, dans tous les cas** (décision de la mère, R-2992, qui retire la règle « N = 24 si le taux de
  réussite par appel du pilote MR-2 v14 est sous 0,95 » de R-2977). Le taux de réussite par appel du pilote pour les deux relais
  employés ici (`opus55` et `fable52`, quatre appels chacun au pilote) — appels répondus (définition de [PILOTE]) sur appels faits,
  calculé par le programme de mesure du pilote sur sa sortie scellée par un lecteur neuf, avant le scellement de ce texte — est
  recopié ici comme **information** : il ne change ni N ni aucun seuil (sur huit appels, « sous 0,95 » revenait à « au moindre
  échec » : remarque R-5, sans objet désormais)."""),
    ("S-min",
     """n_c ≥ 16 mondes complets **quel que soit N** (le test""",
     """n_c ≥ 16 mondes complets sur 20 (le test"""),
    ("S-proba",
     """  indépendance supposée) : p = 0,95 : 0,51 à N = 20 et 0,93 à N = 24 ; p = 0,97 : 0,86 et 0,996 ; p = 0,93 : 0,22 et 0,71 ; p = 0,90 : 0,04 et 0,29.""",
     """  indépendance supposée), à N = 20 : p = 0,95 : 0,51 ; p = 0,97 : 0,86 ; p = 0,93 : 0,22 ; p = 0,90 : 0,04 ; recalculée au taux
  recopié du pilote (information) ; à N = 24, que R-2992 écarte : 0,93 ; 0,996 ; 0,71 ; 0,29 (« Choix et doutes », point 12)."""),
    ("S-format",
     """format tenu dans au moins 14 mondes complets, **quel que soit N** (valeur absolue : 14 sur 24 est moins exigeant que 14 sur 20, dit) ; sinon""",
     """format tenu dans au moins 14 mondes complets (sur 20) ; sinon"""),
    ("S-zone",
     """au moins 10 mondes complets (quel que soit N ; valeur absolue) où""",
     """au moins 10 mondes complets (sur 20) où"""),
    ("A-titre",
     """### Proposeurs (configuration v12 du pilote, inchangée)""",
     """### Proposeurs (configuration v12 du pilote, inchangée ; variante « crédits de Claude au maximum », R-2992)"""),
    ("A-table",
     """| Pr-1 | `argon` | hors crédits | passe 1 (D, B) ; écrivain de B | 0,25 | 2,34 | 36 000 | 10 / 50 (public : 2 / 10 jusqu'au 30 novembre) |
| Pr-2 | `opus55` | crédits de Claude | S ; écrivain de D et H | 0,80 | 2,00 | 89 000 | 4 / 20 |""",
     """| Pr-2 | `opus55` | crédits de Claude | passe 1 (D, B) ; écrivain de B | 0,80 | 2,00 | 89 000 | 4 / 20 (public : 4 / 20) |
| Pr-4 | `fable52` | crédits de Claude | S ; écrivain de D et H | 1,60 | 3,00 | 64 000 | 8 / 40 (public : 8 / 40) |"""),
    ("A-ident",
     """configuration `argon`, `opus55` et `fable52` que le bloc gelé et les lignes de GO exigent (R-2690).
Pr-3 et Pr-4 ne servent pas dans la forme fidèle à [NOTE] (voir la variante « crédits de Claude au maximum », « Devis »).""",
     """configuration `opus55` et `fable52` que le bloc gelé et les lignes de GO exigent (R-2690). Bloc gelé de [PILOTE] : effort
« high » envoyé aux deux, réflexion comprise dans la sortie chez les deux (aucun compte séparé), parts du pilote 8 et 12 USD.
Pr-1 et Pr-3 ne servent pas : la forme fidèle à [NOTE] (Pr-1 choisit, Pr-2 écrit) est écartée par la mère (R-2992). **Un seul
fournisseur** porte les 100 appels (sa clé sert ces deux proposeurs, [PROC-14] § 7) : toute coupure ou toute limite de débit
touche tout le crible (liste d'arrêt, ligne « limite de débit » ; essai à blanc à cinq files)."""),
    ("A-appels",
     """100 en tout (Pr-2 : 60 ; Pr-1 : 40) ;""",
     """100 en tout (Pr-4 : 60 ; Pr-2 : 40 ; tous sur crédits de Claude) ;"""),
    ("A-sonde",
     """2. **Sonde des gabarits neufs** (conseillée ; **obligatoire** si le plus grand appel de Pr-1 du pilote dépasse 30 000 jetons de sortie ; sur devis et ligne propre) : sur un monde de développement à graine publique, un
   appel de Pr-1 sous G1, un de Pr-2 et un de Pr-1 sous G2 ; vérifie l'analyse des ensembles, la forme des cartes, les jetons ; ne
   lit aucune couverture. **Règles d'avance** : appel de Pr-1 sous G2 tronqué, ou carte non évaluable dans l'un des trois appels, ou aucune liste d'ensembles""",
     """2. **Sonde des gabarits neufs** (conseillée ; **obligatoire** si le plus grand appel de Pr-2 ou de Pr-4 du pilote dépasse 80 % de sa borne de sortie, soit 71 200 ou 51 200 jetons ; sur devis et ligne propre) : sur un monde de développement à graine publique, un
   appel de Pr-2 sous G1, un de Pr-4 et un de Pr-2 sous G2 ; vérifie l'analyse des ensembles, la forme des cartes, les jetons ; ne
   lit aucune couverture. **Règles d'avance** : un appel sous G2 tronqué, ou carte non évaluable dans l'un des trois appels, ou aucune liste d'ensembles"""),
    ("A-taille",
     """20 mondes, ou 24 par la règle de la section « Seuil » (annexe A de [NOTE] : 0,80 de puissance pour une part passant de 0,05 à 0,40 à 20 mondes, 0,89 à 24). **Puissance de P2 à l'effet prédit** (écart de + 0,5 composante par monde, écart-type d'un écart par
monde supposé de 1,0 à 1,2, approximation normale ; compte du contre-lecteur du tour 1, refait au tour 2 : 0,35 à 0,50) : environ 0,35 à 0,50 pour que la borne basse à 97,5 % dépasse 0 à 20 mondes : « non tranché » est donc
l'issue la plus probable de P2 même si la prédiction III-2 est vraie ; « sans perte notable » n'est atteignable qu'avec un écart observé δ_DB sous − 0,05 à 20 mondes (sous 0 à 24), pour un écart-type de 1,0 à 1,2 : il dit alors que Pr-1 écrit au moins aussi bien que Pr-2 dans l'échantillon, non une équivalence à 0,5 près ; à refaire par la simulation de la phrase suivante. Pour δ, le test
exact des signes au niveau unilatéral 0,0125 demande au moins 16 accords sur 20 (18 sur 24 : recompte exact du tour 2, bibliothèque standard ; le point 2 de l'annexe A est étendu à n = 21 à 24 par un programme sous un nom neuf, avant le scellement) ; sa puissance est 0,05 si un bras gagne dans 60 %
des mondes non égaux, 0,24 à 70 %, 0,63 à 80 %, 0,96 à 90 % (annexe A, points 2 et 3). **Crible d'un grand effet** : P1 et P2
ne voient qu'un écart net dans une large majorité de mondes ; un « non tranché » ne dit rien d'un petit effet. Le pilote ne mesure
pas la couverture par appel (sa sortie ne rend que la conditionnelle, le témoin et la condition, [PILOTE] « Métrique ») : la
puissance de P1 **et de P2** et le taux d'erreur de l'intervalle par percentile à 20 et à 24 mondes (comptes entiers de 0 à 6 composantes, effet nul puis effet
prédit) se recalculeront, avant le scellement, par simulation sur processeur sous le modèle de proposeurs synthétiques de
[MR2] et la partie A (programme sous un nom neuf, scellé avant son lancement ; graines `(96, s)` de `numpy.random.SeedSequence`, 10 000 tirages par cellule ; cellules : 20 et 24 mondes, effet nul puis effet prédit ; aucune donnée de crible), quand la machine n'est plus chargée ; 24 mondes par la règle de la section « Seuil » (devis × 1,2, section « Devis » mise à jour), non 30.""",
     """20 mondes, dans tous les cas (R-2992 ; annexe A de [NOTE] : 0,80 de puissance pour une part passant de 0,05 à 0,40 à 20 mondes). **Puissance de P2** (écart-type d'un écart par
monde supposé de 1,0 à 1,2, approximation normale) : à un écart de + 0,5 composante par monde (haut de la prédiction III-2), environ 0,35 à 0,50 pour que la borne basse à 97,5 % dépasse 0 à 20 mondes (compte du contre-lecteur du tour 1, refait au tour 2) ; à + 0,25 (milieu de la prédiction III-2), environ 0,10 à 0,13 (même approximation, compte de ce texte) : « non tranché » est donc
l'issue la plus probable de P2, et c'est celle que prédit III-2 ; « sans perte notable » n'est atteignable qu'avec un écart observé δ_DB environ sous − 0,05 à 20 mondes (de − 0,10 à 0 selon l'écart-type de 1,0 à 1,2 ; remarque R-6) : il dit alors que Pr-2 écrit au moins aussi bien que Pr-4 dans l'échantillon, non une équivalence à 0,5 près ; à refaire par la simulation de la phrase suivante. Pour δ, le test
exact des signes au niveau unilatéral 0,0125 demande au moins 16 accords sur 20 (annexe A, point 2 ; N étant fixé à 20, l'extension à n = 21 à 24 n'est plus nécessaire) ; sa puissance est 0,05 si un bras gagne dans 60 %
des mondes non égaux, 0,24 à 70 %, 0,63 à 80 %, 0,96 à 90 % (annexe A, points 2 et 3). **Crible d'un grand effet** : P1 et P2
ne voient qu'un écart net dans une large majorité de mondes ; un « non tranché » ne dit rien d'un petit effet. Le pilote ne mesure
pas la couverture par appel (sa sortie ne rend que la conditionnelle, le témoin et la condition, [PILOTE] « Métrique ») : la
puissance de P1 **et de P2** et le taux d'erreur de l'intervalle par percentile à 20 mondes (comptes entiers de 0 à 6 composantes, effet nul puis effet
prédit) se recalculeront, avant le scellement, par simulation sur processeur sous le modèle de proposeurs synthétiques de
[MR2] et la partie A (programme sous un nom neuf, scellé avant son lancement ; graines `(96, s)` de `numpy.random.SeedSequence`, 10 000 tirages par cellule ; cellules : 20 mondes, effet nul, puis effets + 0,25 et + 0,5 pour P2 ; aucune donnée de crible), quand la machine n'est plus chargée."""),
    ("G-etage2",
     """| 2 | format non tenu ; E_D < 0,5 ; **3 appels de B tronqués ou plus (borne de sortie de Pr-1 : 36 000 jetons, pour environ 30 000 attendus ; celle de Pr-2 : 89 000)** | réserve « **format non tenu** », « **consigne non suivie** » ou « **B tronqué** » : P1 et P2 lus et rapportés sous cette réserve ; aucune conclusion sur l'idée ; sous « B tronqué », δ_DB est rapporté aussi en réintégrant les mondes où seul l'appel de B est tronqué (C_B = 0, dollars de B comptés ; S, D et H répondus), et ce rapport est lu avec le principal même quand moins de trois appels de B sont tronqués (le principal exclut ces mondes par définition du monde complet) ; C_B = 0 est le pire cas pour B (il penche vers « perte établie ») ; si l'issue de P2 du rapport réintégré (mêmes seuils, 97,5 %) diffère de celle du principal, l'issue de P2 est qualifiée « sensible à la troncature de B » et rien de plus n'en est conclu ; et la phrase « perte établie sans le proposeur cher » est **interdite** (elle mêlerait la capacité et la borne) |""",
     """| 2 | format non tenu ; E_D < 0,5 ; **3 appels tronqués ou plus d'un même bras d'écriture : S, D ou H (borne de sortie de Pr-4 : 64 000 jetons) ou B (borne de Pr-2 : 89 000), pour environ 30 000 attendus** | réserve « **format non tenu** », « **consigne non suivie** » ou « **X tronqué** » (X le bras : S, D, H ou B) : P1 et P2 lus et rapportés sous cette réserve ; aucune conclusion sur l'idée ; δ_DB est rapporté aussi en réintégrant les mondes où un seul des deux appels D et B est tronqué (C = 0 pour le bras tronqué, ses dollars comptés ; S, H et l'autre bras répondus), et ce rapport est lu avec le principal même quand aucun bras n'atteint trois appels tronqués (le principal exclut ces mondes par définition du monde complet) ; C = 0 est le pire cas pour le bras tronqué (C_B = 0 penche vers « perte établie », C_D = 0 vers « sans perte notable ») ; si l'issue de P2 du rapport réintégré (mêmes seuils, 97,5 %) diffère de celle du principal, l'issue de P2 est qualifiée « sensible à la troncature » et rien de plus n'en est conclu ; sous « B tronqué », la phrase « perte établie sans le proposeur cher » est **interdite**, sous « D tronqué », la phrase « sans perte notable » l'est (chacune mêlerait la capacité et la borne) |"""),
    ("G-etage4",
     """| 4 | P1 | « deux passes plus efficaces par dollar » / « moins efficaces » / « non tranché » ; **qualifié « dépend du barème »** si le verdict de P1 (même règle, 97,5 %) calculé aux prix de la configuration (Pr-1 à 10 / 50) n'est pas le même qu'aux prix publics ; le barème public de Pr-1 (2 / 10) n'est offert que jusqu'au 30 novembre |""",
     """| 4 | P1 | « deux passes plus efficaces par dollar » / « moins efficaces » / « non tranché » (prix publics, égaux à ceux de la configuration pour Pr-2 et Pr-4 : le qualificatif « dépend du barème » de la forme fidèle est sans objet, retiré) |"""),
    ("G-lecture",
     """« non tranchée ». **Rien n'est adopté** :""",
     """« non tranchée ». Aucun proposeur d'une autre maison n'est mesuré : toute lecture porte sur deux paliers d'une même maison
(« Hypothèse »). **Rien n'est adopté** :"""),
    ("L-config",
     """| v12 acceptée | borne de Pr-1 changée : refus |""",
     """| v12 acceptée | borne de Pr-4 changée : refus |"""),
    ("L-part",
     """| dépense d'un fournisseur atteignant sa part |""",
     """| dépense d'un relais atteignant sa part (`opus55` 80, `fable52` 180, machine 3 USD) |"""),
    ("L-min",
     """pannes de Pr-1 à tous les appels dès le monde 3""",
     """pannes de Pr-2 à tous les appels dès le monde 3"""),
    ("L-debit",
     """des appels d'un fournisseur, une fois au moins dix de ses appels faits |""",
     """des appels d'un fournisseur (ici un seul, pour les deux relais), une fois au moins dix de ses appels faits |"""),
    ("D-bloc",
     """**Hypothèses de coût** (ce texte ; [CRIBLE-V], brouillon non scellé, n'est pas une source) : attendus de [NOTE] § 1 (devis du pilote, `dba76367…`, estimés) ; mes
fourchettes au prix public : entrée ≈ 15 000 à 18 000 jetons par appel (≤ 52 000 octets servis, ≈ 3 octets par jeton supposés ;
G2 ajoute moins de 1 000 octets), sortie ≈ 30 000 jetons pour six cartes ([PILOTE]), **passe 1 : ≈ 2 000 à 10 000 jetons** (vingt
ensembles et la réflexion, supposé) ; pires cas : plafonds de session du bloc gelé ; Pr-1 compté par le code à 10 / 50 (cinq fois
son prix public).

**Forme fidèle à [NOTE]** (Pr-1 choisit, Pr-2 écrit), 20 mondes, 100 appels :

| ligne | appels | jetons d'entrée (attendu ; compté au pire) | jetons de sortie (attendu ; borne) | crédits | attendu [NOTE] | fourchette (prix public) | pire (plafonds) |
|---|---|---|---|---|---|---|---|
| Pr-2, S standard | 20 | 0,30 à 0,36 M ; 1,06 M | 0,60 M ; 1,78 M | Claude | 16,00 | 13,20 à 16,40 | 40,00 |
| Pr-2, D passe 2 | 20 | 0,30 à 0,37 M ; 1,08 M | 0,60 M ; 1,78 M | Claude | 16,00 | 13,20 à 16,40 | 40,00 |
| Pr-2, H passe 2 | 20 | 0,30 à 0,37 M ; 1,08 M | 0,60 M ; 1,78 M | Claude | 16,00 | 13,20 à 16,40 | 40,00 |
| Pr-1, passe 1 (commune à D et B) | 20 | 0,30 à 0,36 M ; 1,06 M | 0,04 à 0,20 M ; 0,72 M (+ réflexion ajoutée) | hors | 5,00 | 1,00 à 2,80 (code : 5 à 14) | 46,80 |
| Pr-1, B passe 2 | 20 | 0,30 à 0,37 M ; 1,08 M | 0,60 M ; 0,72 M (+ réflexion ajoutée) | hors | 5,00 | 7,00 à 9,00 (code : 34 à 42) | 46,80 |
| machine (≤ 0,15 USD/h ; 0,0522 relue le 16 novembre) | — | — | — | hors | 0,30 | 0,50 à 0,80 | 3,00 |
| **crédits de Claude** (Pr-2) | 60 | | | | **48,00** | 39,60 à 49,20 | **120,00** |
| **hors crédits** (Pr-1, machine) | 40 | | | | **10,30** | 8,50 à 12,60 | **96,60** |
| **total** | 100 | ≈ 1,5 à 1,85 M ; 5,36 M | ≈ 2,45 à 2,6 M ; 6,78 M | | **58,30** | 48,10 à 61,80 | **216,60** |
| conditionnel : sonde des gabarits neufs (G1 par Pr-1, G2 par Pr-2 et par Pr-1, un monde de développement) | 3 | — | — | Claude 1, hors 2 | — | 1,05 à 1,40 | 6,68 (2,00 sur crédits ; 4,68 hors crédits) |
| conditionnel : sonde neuve des relais (si le lanceur l'exige ; lignes de la sonde v74) | 8 | — | — | les deux | 0,10 | — | 8,07 |
| partie A | 0 | — | — | — | 0 | 0 | 0 |

- **Écart à [NOTE]** : 100 appels au lieu de 120 (B réemploie la passe 1 de D : section « Choix et doutes », point 1) ; plafonds de
  Pr-1 à 2,34 (bloc gelé, R-2542) au lieu de 2,00 ; pire 216,60 au lieu de 243,00.
- **Témoin commun avec (v)** — **écarté (R-2977) ; information seulement, jamais un devis** ([NOTE] § 4) : S pris aux appels de Pr-2 de (v) : − 20 appels, attendu ≈ 42,30 (32 sur crédits),
  pire 176,60 (80 sur crédits ; 173,60 si la machine est celle de (v)) ; mêmes mondes, donc une seule machine pour les deux cribles.
- **Variante « crédits de Claude au maximum »** (Pr-2 choisit, Pr-4 `fable52` écrit ; S = un appel de Pr-4) : Pr-4, 60 appels :
  96,00 attendus (79,20 à 98,40), 180,00 au pire ; Pr-2, 40 appels (passe 1 et écriture de B) : 32,00 attendus (passe 1 comptée
  comme un appel entier ; 15,20 à 21,80 au prix public), 80,00 au pire ; machine 0,30 / 3,00 : **≈ 128,30 attendus, 263,00 au
  pire, dont 3,00 hors crédits**. Elle change la question (écart de prix 2 au lieu de 3,2 ; deux modèles d'une même maison) : section
  « Choix et doutes », point 4.
- **Plafond de 0,75 pour Pr-1** ([NOTE] § 4) : impossible sous la configuration v12 (bloc gelé de [PILOTE] : plafond de session de Pr-1 à 2,34 USD).""",
     """**Hypothèses de coût** (ce texte ; [CRIBLE-V], brouillon non scellé, n'est pas une source) : attendus de [NOTE] § 1 (devis du
pilote, `dba76367…`, estimés : Pr-2 0,80, Pr-4 1,60 USD par appel ; la passe 1 de Pr-2 est comptée comme un appel entier, par
prudence) ; fourchettes de ce texte au prix public : entrée ≈ 15 000 à 18 000 jetons par appel (≤ 52 000 octets servis,
≈ 3 octets par jeton supposés ; G2 ajoute moins de 1 000 octets), sortie ≈ 30 000 jetons pour six cartes ([PILOTE]),
**passe 1 : ≈ 2 000 à 10 000 jetons** (vingt ensembles et la réflexion, supposé) ; **haut des fourchettes d'écriture** (1,64 USD
par appel de Pr-4 ; 0,82 par appel de Pr-2) : sortie haute ≈ 37 400 jetons, de l'ordre des deux appels de proposeur mesurés à la
course v67 (31 891 et 38 343 jetons de sortie, [NOTE] § 1), non la colonne des jetons attendus (remarque R-1) ; réflexion comprise
dans la sortie chez Pr-2 et Pr-4 (bloc gelé de [PILOTE]) ; pires cas : plafonds de session du bloc gelé (Pr-2 2,00 ; Pr-4 3,00),
qui couvrent la règle du code ((octets + 1 024) × prix d'entrée + borne × prix de sortie : 1,99 et 2,98 USD par appel) ; prix de
la configuration égaux aux prix publics pour les deux.

**Variante « crédits de Claude au maximum »** (Pr-2 choisit, Pr-4 écrit ; S = un appel de Pr-4 ; décision de la mère, R-2992),
20 mondes, 100 appels :

| ligne | appels | jetons d'entrée (attendu ; compté au pire) | jetons de sortie (attendu ; borne) | crédits | attendu [NOTE] | fourchette (prix public) | pire (plafonds) |
|---|---|---|---|---|---|---|---|
| Pr-4, S standard | 20 | 0,30 à 0,36 M ; 1,06 M | 0,60 M ; 1,28 M | Claude | 32,00 | 26,40 à 32,80 | 60,00 |
| Pr-4, D passe 2 | 20 | 0,30 à 0,37 M ; 1,08 M | 0,60 M ; 1,28 M | Claude | 32,00 | 26,40 à 32,80 | 60,00 |
| Pr-4, H passe 2 | 20 | 0,30 à 0,37 M ; 1,08 M | 0,60 M ; 1,28 M | Claude | 32,00 | 26,40 à 32,80 | 60,00 |
| Pr-2, passe 1 (commune à D et B) | 20 | 0,30 à 0,36 M ; 1,06 M | 0,04 à 0,20 M ; 1,78 M | Claude | 16,00 | 2,00 à 5,44 | 40,00 |
| Pr-2, B passe 2 | 20 | 0,30 à 0,37 M ; 1,08 M | 0,60 M ; 1,78 M | Claude | 16,00 | 13,20 à 16,40 | 40,00 |
| machine (≤ 0,15 USD/h ; 0,0522 relue le 16 novembre) | — | — | — | hors | 0,30 | 0,50 à 0,80 | 3,00 |
| **crédits de Claude** (Pr-4, Pr-2) | 100 | | | | **128,00** | 94,40 à 120,24 | **260,00** |
| **hors crédits** (machine) | 0 | | | | **0,30** | 0,50 à 0,80 | **3,00** |
| **total** | 100 | ≈ 1,5 à 1,85 M ; 5,36 M | ≈ 2,44 à 2,6 M ; 7,40 M | | **128,30** | 94,90 à 121,04 | **263,00** |
| conditionnel : sonde des gabarits neufs (G1 par Pr-2, G2 par Pr-4 et par Pr-2, un monde de développement) | 3 | — | — | Claude 3 | — | 2,08 à 2,73 | 7,00 (sur crédits) |
| partie A | 0 | — | — | — | 0 | 0 | 0 |

- **Écart à [NOTE]** : 100 appels au lieu de 120 (B réemploie la passe 1 de D : section « Choix et doutes », point 1) ;
  proposeurs de la variante (R-2992) au lieu de Pr-1 et Pr-2 : 128,30 attendus au lieu de 63,30, 263,00 au pire au lieu de 243,00.
- **Forme fidèle à [NOTE]** (Pr-1 choisit hors crédits, Pr-2 écrit) — **écartée par la mère (R-2992) ; information seulement,
  jamais un devis** : 58,30 attendus (10,30 hors crédits), 216,60 au pire (96,60 hors crédits).
- **Témoin commun avec (v)** : **écarté (R-2977)** ; aucun chiffre ici (remarque 2 du tour 3).
- **Ligne « sonde neuve des relais »** des brouillons 1 à 6 : **retirée** (remarque R-3) : le relevé de la sonde v74 est exigé
  sans condition (liste d'arrêt, troisième ligne) ; sans lui, le crible n'est pas lancé, et une sonde neuve demanderait sa ligne
  et son texte à part.
- **Plafond de 0,75 pour Pr-1** ([NOTE] § 4) : sans objet (Pr-1 ne sert pas)."""),
    ("D-conc",
     """  15 sessions de Pr-2 (S, H et D d'un même monde peuvent courir ensemble : D part à la réponse de la passe 1, pendant que S et H courent) et 5 de Pr-1 (18 et 6 à six files) :""",
     """  15 sessions de Pr-4 (S, H et D d'un même monde peuvent courir ensemble : D part à la réponse de la passe 1, pendant que S et H courent) et 5 de Pr-2, toutes chez un même fournisseur (20 sessions à la fois) :"""),
    ("D-regle",
     """| N (20 ou 24) et minimum | taux de réussite par appel, relais employés ici | N = 24 si taux < 0,95 (section « Seuil ») ; minimum 16 |
| attendu par appel de Pr-1 et de Pr-2 (0,25 ; 0,80) | dollars réels par appel au prix public, par relais | moyenne arithmétique par relais ; fourchette = plus petit et plus grand appel du pilote ; **pire cas inchangé** (plafonds) |
| sortie de Pr-1 pour six cartes (30 000 jetons attendus) et tronquage à 36 000 | jetons de sortie et de réflexion de Pr-1 | si le plus grand appel de Pr-1 du pilote dépasse 30 000 jetons : réserve « B tronqué » à l'avance (étage 2) et sonde obligatoire |
| machine (0,30 attendu) | prix horaire relu et durée réelle d'un monde | durée par monde × cinq files ; borne de 7 200 s inchangée |
| durée par monde (30 à 40 min) | durée mesurée des mondes du pilote | durée attendue mise à jour ; **bornes de 3 000 s et 7 200 s inchangées** ; si l'appel le plus long du pilote dépasse 1 500 s, nœud de la mère avant le scellement (borne par appel probablement trop courte) ; seule décision permise : relever la borne par appel à 2 × l'appel le plus long du pilote, sans dépasser 3 600 s (deux tours en série doivent tenir dans 7 200 s) ; ni la borne de 7 200 s par monde ni la garde de départ ne changent ; décision datée avant le scellement |
| lignes de GO (montants) | N et attendus ci-dessus | montants = N/20 × ceux de ce texte pour les appels ; plafonds par appel inchangés |
| mondes, appels, files | N | « 20 mondes » se lit N partout dans ce texte (Partie B, Étapes, Devis, Taille, lignes de GO) ; « 100 appels » se lit 5N (Pr-2 : 3N ; Pr-1 : 2N) ; files : N / 4 (5 ou 6) ; « cinq mondes incomplets sur 20 d'emblée » de la liste d'arrêt se lit « N − 15 mondes incomplets » ; seuils de format (14) et de zone utile (10) : valeurs absolues, inchangées |""",
     """| N (20) et minimum | taux de réussite par appel des relais `opus55` et `fable52` | **aucun changement** : N = 20 dans tous les cas (R-2992) ; minimum 16 ; taux recopié et probabilité d'atteindre le minimum recalculée à ce taux (information, section « Seuil ») |
| attendu par appel de Pr-2 et de Pr-4 (0,80 ; 1,60) | dollars réels par appel au prix public, par relais | moyenne arithmétique par relais ; fourchette = plus petit et plus grand appel du pilote ; **pire cas inchangé** (plafonds) |
| sortie de Pr-2 et de Pr-4 pour six cartes (30 000 jetons attendus) ; bornes de 89 000 et de 64 000 | jetons de sortie de Pr-2 et de Pr-4 (réflexion comprise) | si le plus grand appel de l'un des deux au pilote dépasse 80 % de sa borne (71 200 ; 51 200) : réserve de tronquage des bras qu'il écrit (« B tronqué » pour Pr-2 ; « S tronqué », « D tronqué », « H tronqué » pour Pr-4) annoncée à l'avance (étage 2) et sonde obligatoire |
| machine (0,30 attendu) | prix horaire relu et durée réelle d'un monde | durée par monde × cinq files ; borne de 7 200 s inchangée |
| durée par monde (30 à 40 min) | durée mesurée des mondes du pilote | durée attendue mise à jour ; **bornes de 3 000 s et 7 200 s inchangées** ; si l'appel le plus long du pilote dépasse 1 500 s, nœud de la mère avant le scellement (borne par appel probablement trop courte) ; seule décision permise : relever la borne par appel à 2 × l'appel le plus long du pilote, sans dépasser 3 600 s (deux tours en série doivent tenir dans 7 200 s) ; ni la borne de 7 200 s par monde ni la garde de départ ne changent ; décision datée avant le scellement |
| lignes de GO (montants) | attendus ci-dessus | attendus refaits ; montants (plafonds) inchangés, N = 20 ; cumul des cinq cribles tenu sous les 1 275 USD de GO-2026-11-15-06, sinon nœud de Lazar (R-2992, point 3) |
| mondes, appels, files | — | **inchangés** (N = 20, R-2992) : 20 mondes, 100 appels (Pr-4 : 60 ; Pr-2 : 40), cinq files de quatre mondes |"""),
    ("D-apres",
     """Tout autre chiffre reste celui de ce texte, **hors** quatre valeurs calculées sur processeur avant le scellement et recopiées : la part des distracteurs après filtre (III-5), la puissance de P1 et de P2, le taux d'erreur de l'intervalle par percentile à N mondes (section « Taille ») et les seuils exacts du test des signes à n = 21 à 24 (annexe A, point 2 étendu). Ces calculs ne changent **aucun** seuil ni aucune règle de ce texte ; si l'un d'eux en demandait un (par exemple un taux d'erreur de l'intervalle au-dessus de 0,05 à effet nul), il donne un brouillon nouveau, contre-lu, non une retouche. **Points à remesurer d'après le coût réel du pilote MR-2** : ceux de [CRIBLE-V] (jetons, dollars aux deux prix, durées, taux de
réponse par fournisseur, réflexion de Pr-1, cartes admises, taille du texte servi, durée des mondes) ; et, **non mesurés par le
pilote**, à prendre à la sonde des gabarits : sortie et réflexion de la passe 1, analyse des ensembles, longueur et forme des cartes
sous G2.""",
     """Tout autre chiffre reste celui de ce texte, **hors** trois valeurs calculées sur processeur avant le scellement et recopiées : la part des distracteurs après filtre (III-5), la puissance de P1 et de P2, le taux d'erreur de l'intervalle par percentile à 20 mondes (section « Taille ») ; les seuils exacts du test des signes à n = 21 à 24, quatrième valeur des brouillons 1 à 6, ne servent plus (N = 20). Ces calculs ne changent **aucun** seuil ni aucune règle de ce texte ; si l'un d'eux en demandait un (par exemple un taux d'erreur de l'intervalle au-dessus de 0,05 à effet nul), il donne un brouillon nouveau, contre-lu, non une retouche. **Points à remesurer d'après le coût réel du pilote MR-2** (liste recopiée de [CRIBLE-V], remarque 2 du tour 3) : jetons, dollars par appel (les deux barèmes sont égaux ici), durées, taux de
réponse par relais, réflexion comprise dans la sortie, cartes admises, taille du texte servi, durée des mondes ; et, **non mesurés par le
pilote**, à prendre à la sonde des gabarits : sortie et réflexion de la passe 1, analyse des ensembles, longueur et forme des cartes
sous G2."""),
    ("GO-lignes",
     """| GO-AAAA-MM-JJ-NN (κiii1) | AAAA-MM-JJ | calcul | Organisme d'idéation, crible (iii) « deux passes » (traits choisis par un proposeur bon marché, loi écrite par un proposeur cher), part sur crédits de Claude : proposeur `opus55` (Pr-2, plafond de session 2 USD, part 120), 60 appels (bras standard, passe 2 des bras « deux passes » et « ensembles au hasard ») ; 20 mondes MR-2 du secret du crible, jamais publiés ni réutilisés ; archive {K1}, une génération ; gardien mécanique seul, aucun juge, aucun test de mort ; filtre déterministe sans modèle ni juge ; mesure gelée une seule fois ; conditions toutes exigées : coûts du pilote MR-2 mesurés et devis refait, préenregistrement du crible contre-lu et scellé, code et gabarits contre-lus et gelés, essai à blanc réussi, mondes vérifiés et leurs empreintes inscrites ; coût au-dessus du pire cas = arrêt ; essayé, non adopté ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 120 USD (sur crédits) | 2026-11-30 | Lazar | GO-2026-11-15-06 ; R-2851 ; R-2875 ; ce texte |
| GO-AAAA-MM-JJ-NN (κiii2) | AAAA-MM-JJ | calcul | Même crible, part hors crédits : `argon` (Pr-1, 2,34 USD par session, part 93,60), 40 appels (passe 1 commune, écriture du bras « tout bon marché »), aucun réglage envoyé, machine jetable 3 USD ; plafond de chaque relais égal à sa part ; mêmes conditions que la ligne κiii1 | 96.60 USD | 2026-11-30 | Lazar | GO-2026-11-15-06 ; R-2851 ; R-2875 ; ce texte |
| GO-AAAA-MM-JJ-NN (κiii0, conditionnelle) | AAAA-MM-JJ | calcul | Sonde des gabarits neufs du crible (iii) : un appel de `argon` sous le gabarit de passe 1, un de `opus55` et un de `argon` sous le gabarit de passe 2, sur un monde de développement à graine publique ; aucune couverture lue ; relevé versé ; une seule exécution | 6.68 USD (2 sur crédits, 4,68 hors crédits) | 2026-11-30 | Lazar | GO-2026-11-15-06 ; ce texte |""",
     """| GO-AAAA-MM-JJ-NN (κiii1) | AAAA-MM-JJ | calcul | Organisme d'idéation, crible (iii) « deux passes » (traits choisis par un proposeur bon marché, loi écrite par un proposeur cher), variante « crédits de Claude au maximum », part sur crédits de Claude : proposeurs `fable52` (Pr-4, plafond de session 3 USD, part 180), 60 appels (bras standard, passe 2 des bras « deux passes » et « ensembles au hasard »), et `opus55` (Pr-2, plafond de session 2 USD, part 80), 40 appels (passe 1 commune, écriture du bras « tout bon marché ») ; effort « high » envoyé aux deux (bloc gelé du pilote) ; 20 mondes MR-2 du secret du crible, jamais publiés ni réutilisés ; archive {K1}, une génération ; gardien mécanique seul, aucun juge, aucun test de mort ; filtre déterministe sans modèle ni juge ; mesure gelée une seule fois ; conditions toutes exigées : coûts du pilote MR-2 mesurés et devis refait, préenregistrement du crible contre-lu et scellé, code et gabarits contre-lus et gelés, essai à blanc réussi à cinq files, mondes vérifiés et leurs empreintes inscrites ; plafond de chaque relais égal à sa part ; coût au-dessus du pire cas = arrêt ; essayé, non adopté ; jamais de ligne d'extension ; arrêt par identifiant (R10) | 260 USD (sur crédits) | 2026-11-30 | Lazar | GO-2026-11-15-06 ; R-2851 ; R-2875 ; R-2992 ; ce texte |
| GO-AAAA-MM-JJ-NN (κiii2) | AAAA-MM-JJ | calcul | Même crible, part hors crédits : machine jetable seule, 3 USD ; mêmes conditions que la ligne κiii1 | 3 USD | 2026-11-30 | Lazar | GO-2026-11-15-06 ; R-2851 ; R-2875 ; R-2992 ; ce texte |
| GO-AAAA-MM-JJ-NN (κiii0, conditionnelle) | AAAA-MM-JJ | calcul | Sonde des gabarits neufs du crible (iii), sur crédits de Claude : un appel de `opus55` sous le gabarit de passe 1, un de `fable52` et un de `opus55` sous le gabarit de passe 2, sur un monde de développement à graine publique ; aucune couverture lue ; relevé versé ; une seule exécution | 7 USD (sur crédits) | 2026-11-30 | Lazar | GO-2026-11-15-06 ; R-2992 ; ce texte |"""),
    ("GO-mots",
     """Mots exigés par le lecteur gelé des lignes : à fixer avec le code ; montants à refaire sur le devis mesuré.
""",
     """Mots exigés par le lecteur gelé des lignes : à fixer avec le code ; montants à refaire sur le devis mesuré.
**Enveloppe** (R-2992, point 3) : la ligne « calcul » de ce crible s'inscrit sur un devis refait d'après le coût réel du pilote,
le cumul des cinq cribles tenu sous les 1 275 USD de GO-2026-11-15-06 ; si le dernier crible n'y tient pas, nœud de Lazar ;
somme des pires cas des cinq aux textes actuels, avec cette variante : 1 308,60 USD (compte des lecteurs de la lecture du
brouillon 4 : 123 + 483 + 243 + 196,60 + 263).
"""),
    ("X-B",
     """qui prévoyait 40 appels de Pr-1 pour le bras 4)""",
     """qui prévoyait 40 appels de l'écrivain bon marché pour le bras 4)"""),
    ("X-signale",
     """la dépense seulement ») ; je le signale :""",
     """la dépense seulement ») ; signalé ici :"""),
    ("X-egal",
     """plutôt que par l'ordre de proposition de Pr-1 : le choix de
  Pr-1 n'entre""",
     """plutôt que par l'ordre de proposition de Pr-2 : le choix de
  Pr-2 n'entre"""),
    ("X-forme",
     """- **Consigne, non garde** : une carte qui emploie d'autres traits reste valide ; l'exécution est mesurée, non imposée.
""",
     """- **Consigne, non garde** : une carte qui emploie d'autres traits reste valide ; l'exécution est mesurée, non imposée.
- **Forme : variante « crédits de Claude au maximum »** (décision de la mère, R-2992) : écart à [NOTE] (Pr-2 choisit au lieu de
  Pr-1, Pr-4 écrit au lieu de Pr-2) ; ce qu'elle change à la question : « Hypothèse » (dit, non tranché) ; un seul fournisseur
  porte les 100 appels (« Plan d'analyse »).
- **Réserve de lignée** (dite) : les rédacteurs et les lecteurs de ce texte sont de la même maison que les deux proposeurs ; le
  crible n'a aucun juge et se mesure par l'oracle sur les cartes brutes ; les gabarits G1 et G2, écrits dans cette maison, sont
  contre-lus avec le code.
"""),
    ("X-qo1",
     """du crible (QO1 au sens dit en « Hypothèse » : deux espèces de frontière, non l'instrument local) ;""",
     """du crible (QO1 au sens dit en « Hypothèse » : deux espèces de frontière d'une même maison, non l'instrument local) ;"""),
    ("R-2c",
     """(références non relevées par moi)""",
     """(références non relevées par l'auteur)"""),
    ("R-2d",
     """autre branche, non lu par moi)""",
     """autre branche, non lu par l'auteur)"""),
    ("C-2",
     """non ceux que préfère Pr-1 (les traits""",
     """non ceux que préfère Pr-2 (les traits"""),
    ("C-4",
     """4. **Crédits de Claude au maximum** : forme fidèle (Pr-1, hors crédits, 10,30 attendus hors crédits) ou variante Pr-2 / Pr-4
   (tout sur crédits sauf la machine ; ≈ 128,30 attendus). **À trancher par la mère avant toute lecture de l'issue du pilote** (la forme fixe les deux relais dont le taux de réussite fixe N : décidée après la lecture, elle s'ouvrirait selon les taux ; R-2977 le confiait au contre-lecteur ; les contre-lecteurs des tours 1 et 2 recommandent la variante, confiance 0,6 puis 0,65 ; décision, date et heure (`date -u`) à inscrire ici et dans `registres/decisions.md`, avant la lecture de l'issue du pilote ; tant que rien n'est inscrit, ce texte reste rédigé dans la forme fidèle et n'est pas scellable) ; **raisons des contre-lecteurs** : au prix public, principal, l'écart de prix par jeton est
   de 2 dans les deux formes (Pr-2 4 / 20 contre Pr-1 2 / 10 ; Pr-4 8 / 40 contre Pr-2 4 / 20), et le propre devis de ce texte donne un appel d'écriture
   de Pr-1 à 0,35 à 0,45 contre 0,66 à 0,82 pour Pr-2, soit environ 2 et non 3,2 ; au prix de la configuration, Pr-1 (10 / 50) est **plus cher**
   que Pr-2 (4 / 20) alors que l'écart Pr-4 / Pr-2 reste 2 : le contraste de la variante tient aux deux barèmes, celui de la forme fidèle à un
   barème promotionnel qui s'arrête le 30 novembre. Si la variante est retenue, ce texte est réécrit (section « Si la variante est retenue » du rapport de contre-lecture).""",
     """4. **Forme du crible — tranchée par la mère : la variante « crédits de Claude au maximum »** (R-2992, point 1, ligne du
   2026-11-16 à 14:52 UTC, `date -u`, inscrite avant toute lecture de l'issue du pilote ; R-2977 confiait le choix au
   contre-lecteur ; les lecteurs des six tours la recommandaient, confiance 0,6 à 0,65 ; conforme à la consigne de Lazar,
   GO-2026-11-15-06 : « on utilise nos crédits Claude au max ») : Pr-2 choisit, Pr-4 écrit, S = un appel de Pr-4 ; 128,30
   attendus, 263 au pire, dont 3 hors crédits (la machine). **Raisons des lecteurs** : au prix public, principal, l'écart de prix
   par jeton est de 2 dans les deux formes (Pr-2 4 / 20 contre Pr-1 2 / 10 ; Pr-4 8 / 40 contre Pr-2 4 / 20), et le devis de la
   forme fidèle donnait un appel d'écriture de Pr-1 à 0,35 à 0,45 contre 0,66 à 0,82 pour Pr-2, soit environ 2 et non 3,2 ; au
   prix de la configuration, Pr-1 (10 / 50) est **plus cher** que Pr-2 (4 / 20) alors que l'écart Pr-4 / Pr-2 reste 2 : le
   contraste de la variante tient aux deux barèmes, celui de la forme fidèle à un barème promotionnel qui s'arrête le
   30 novembre ; la variante respecte la partition de [NOTE] (Pr-1 et Pr-2 bon marché, Pr-3 et Pr-4 chers). **Ce que la variante
   change à la question** : « Hypothèse » (dit, non tranché ici)."""),
    ("C-6",
     """Pr-1 y est cinq fois moins cher qu'au prix de la configuration, où il devient plus cher que Pr-2 ; lecture de ce risque : étage 4.""",
     """pour Pr-2 et Pr-4, il est égal au prix de la configuration : la sensibilité « prix de la configuration » est vide et l'étage 4 n'a plus de qualificatif de barème."""),
    ("C-8",
     """(≈ 1,05 à 1,40 USD au prix public, 6,68 au pire) : recommandation""",
     """(≈ 2,08 à 2,73 USD au prix public, 7,00 au pire, sur crédits) : recommandation"""),
    ("C-9",
     """cinq files de quatre mondes (six pour 24), jamais une minuterie plus longue.""",
     """cinq files de quatre mondes, jamais une minuterie plus longue."""),
    ("C-12",
     """11. **Partie A** (plafond du format) : utile pour lire F et Q ; à jouer seulement quand la machine n'est plus chargée.
""",
     """11. **Partie A** (plafond du format) : utile pour lire F et Q ; à jouer seulement quand la machine n'est plus chargée.
12. **N = 20 dans tous les cas** (R-2992) : **appliqué**. Information pour la mère, sans rien rouvrir : dans ce crible, la règle
    « 24 si le taux du pilote est sous 0,95 » de R-2977 protégeait surtout le **minimum** de 16 mondes complets (monde complet =
    cinq appels répondus) : à p = 0,95 par appel, 0,51 à N = 20 contre 0,93 à N = 24 ; à p = 0,93, 0,22 contre 0,71 ; la raison
    écrite dans R-2992 (« 24 ne gagne rien en puissance, coûte 20 % de plus et rend la durée probablement intenable ») est donnée
    sous le crible (v) ; à N = 20, un « non concluant » est donc probable si le taux réel par appel est de 0,95 ou moins (0,49 à
    p = 0,95).
13. **Un seul fournisseur** pour les 100 appels (variante) : toute coupure ou toute limite de débit touche tout le crible ;
    20 sessions à la fois chez lui à cinq files ; l'essai à blanc et la ligne « limite de débit » deviennent décisifs ; **solde de
    crédits de Claude** à couvrir : 260 USD au pire pour ce crible, plus 7 pour la sonde des gabarits, en plus des autres usages :
    à vérifier par la mère.
"""),
    ("CL-6",
     """**Tour suivant** (obligatoire avant le scellement : si la variante est retenue, après la réécriture, selon les rapports des
tours 1 à 3 et des deux tours de la lecture du brouillon 4 ; sinon, un dernier tour sur le différentiel du brouillon 5 à ce
brouillon 6 seul, selon le rapport du tour 2 de la lecture du brouillon 4, section 3) : sous-agent neuf qui n'a écrit ni ce
texte, ni les brouillons 1 à 5, ni les rapports des tours 1 à 3 ni ceux des deux tours de la lecture du brouillon 4.
**Fichiers à lui donner explicitement** : ce texte ; les brouillons 1 à 5, les rapports des tours 1 à 3 et ceux des deux tours
de la lecture du brouillon 4 (empreintes ci-dessus) ; les programmes `appliquer-corrections-crible-iii-brouillon2.py`,
`appliquer-corrections-crible-iii-brouillon3.py`, `appliquer-corrections-crible-iii-brouillon4.py`,
`appliquer-corrections-crible-iii-brouillon5.py` et `appliquer-corrections-crible-iii-brouillon6.py` ;
[CRIBLE-V] (« Métrique », « Devis ») ; [NOTE] (`2f6a69dd…`), § 1, § 2, § 3 (iii), § 4, § 6 et
annexe A ; [RELEVÉ] (`bd253b6c…`), § 3.1, § 4.2, § 5, § 6 ; [REC] (`eecd98fa…`), V3 et C2 ; [PILOTE] (`8aa33014…`),
« Dessin », « Métrique », « Devis », bloc gelé ; [PROC-14] (`20355627…`), § 0, § 6, § 7 ; [MR2] (`47e38ec0…`), § 2 et § 3 ;
[V3] (`386d48ba…`), § 4.1 ; `mesure_pilote_v4.py` (`676d5f37…`) ; `monde_riche_outils_v1.py` (`1825b956…`) ; N-045 v2
(`c7b05e39…`) ; N-058 (`854f2724…`) ; la ligne GO-2026-11-15-06 ; la ligne R-2977 de `registres/decisions.md` et toute ligne
de ce registre qui trancherait la forme ou le gel de III-6 ; l'annexe A et ses deux programmes.""",
     """- **Contre-lecture 6** (R2, tour 3 de la lecture du brouillon 4, sixième lecture du crible) — sous-agent neuf du modèle C, qui
  n'a écrit ni ce texte, ni les brouillons 1 à 5, ni les rapports des tours précédents, ni aucune pièce citée (un premier
  contre-lecteur s'était arrêté sur une limite d'usage vers 13:05Z sans rendre de rapport, R-2982 : rien de lui n'est repris ni
  lu). Texte relu :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/crible-iii-brouillon6.md`,
  `f377e927aab482b39ccda892adc178a1cbfaac7a8042bf9215047f303f72189d` ; rapport :
  `docs/notes/organisme-idees-juge-v1/cribles-v1/contre-lecture-crible-iii-b4-tour3-v1.md`,
  `99fb10247b295f053a8ecfa8b6464c0f4b445146cc7f67f970a0de514ec70e2e` (égale à son compagnon `.sha256`, recalculée). Verdict :
  « scellable » pour le texte dans la forme fidèle, **aucune correction exigée** ; réserve de séquence : ne pas sceller le
  brouillon 6 si la variante est retenue ; recommandation : la variante, confiance 0,6. La mère a retenu la variante (R-2992) ;
  le brouillon 6 n'est pas scellé. Ce brouillon 7 est écrit le 2026-11-16T15:06:52Z (`date -u`) par un rédacteur neuf du modèle A, qui
  n'a écrit ni les brouillons 1 à 6 ni les rapports de contre-lecture, au moyen du programme
  `appliquer-corrections-crible-iii-brouillon7.py` (même dossier, scellé à côté) : couples « ancien → nouveau » écrits par ce
  rédacteur (le rapport n'en donne aucun) ; chaque « ancien » figure une seule fois dans le brouillon 6 (vérifié par le
  programme).
  **Traitement**, point par point :
  - **Corrections exigées** : aucune ; rien à appliquer du rapport. Ses remarques facultatives (R-1 à R-6 des tours précédents)
    et ses points pour la mère sont repris ci-dessous.
  - **Réécriture sur la variante** (décision de la mère, R-2992, point 1 ; listes « Si la variante est retenue » des rapports
    des tours 1, 2 et 3 et du tour 1 de la lecture du brouillon 4, sections 3 des rapports de la lecture du brouillon 4) :
    **appliquée** : proposeurs Pr-2 `opus55` (passe 1, écriture de B ; plafond 2,00, borne 89 000) et Pr-4 `fable52` (S, D, H ;
    plafond 3,00, borne 64 000), tous deux sur crédits (table « Proposeurs ») ; bras, H-iii, H-iii-a, H-iii-b, QO1 qualifiée
    « deux espèces de frontière d'une même maison, deux paliers de prix » (section 0, « Hypothèse ») ; **ce que la variante change
    à la question de la note : dit, non tranché** (« Hypothèse ») ; « Lecture de H-iii » : aucun proposeur d'une autre maison
    mesuré ; prédictions refaites **avant toute lecture du pilote** : III-2 (entre 0 et + 0,5, issue « non tranché », confiance
    0,4, au lieu de ≥ + 0,5 à 0,45 : même maison) et III-7 (1,05 à 1,25, au lieu de 1,05 à 1,6 : la passe 1 de Pr-2 coûte peu
    devant un appel de Pr-4), III-1 et III-3 à III-6 inchangées, section 0 point 7 ; étage 2 : la réserve de tronquage couvre les
    bras de Pr-4 (borne la plus basse, 64 000) et la règle de G-01 est étendue de façon symétrique au bras D (« sensible à la
    troncature » ; « sans perte notable » interdite sous « D tronqué ») ; étage 4 : qualificatif « dépend du barème » sans objet,
    retiré ; sensibilité « prix de la configuration » vide, dite (« Métrique ») ; sonde des gabarits : G1 par Pr-2, G2 par Pr-4
    et par Pr-2, 7,00 au pire sur crédits, obligatoire si le plus grand appel de Pr-2 ou de Pr-4 du pilote dépasse 80 % de sa
    borne (71 200 ; 51 200), règle d'avance « un appel sous G2 tronqué » ; devis : 128,30 attendus, 263 au pire (260 sur crédits,
    3 hors crédits), fourchettes recalculées par ce texte (94,90 à 121,04) ; table de mise à jour ; lignes de GO (κiii1 260 sur
    crédits, κiii2 la machine 3, κiii0 7) ; concurrence : 15 sessions de Pr-4 et 5 de Pr-2 chez un seul fournisseur ; taux de
    réussite par appel lu sur les relais `opus55` et `fable52`, non sur `argon` ; enveloppe (R-2992, point 3) ; écarts (forme,
    réserve de lignée). **Non repris** des listes des lecteurs : le libellé « palier supérieur de la même maison » à la place de
    « proposeur cher » dans les phrases de verdict (le libellé « proposeur cher » reste exact : Pr-4 est dans la « moitié chère »
    de [NOTE] ; aucune phrase de verdict n'est renommée ; la portée est dite dans « Hypothèse » et « Lecture de H-iii ») ; le
    renommage du bras B en « écrit par le choisisseur » (fait en apposition à la section 0 seulement, le nom « tout bon marché »
    étant celui de [NOTE] et des lignes de GO).
  - **N = 20 dans tous les cas** (R-2992) : **appliqué** (section 0 point 9, « Seuil », « Taille », table de mise à jour,
    « Choix et doutes », points 9 et 12) ; retirés : la règle 20 ou 24, les six files, la cellule de 24 mondes de la simulation,
    l'extension du test des signes à n = 21 à 24 (les valeurs calculées avant le scellement passent de quatre à trois) ;
    information pour la mère sur le minimum de 16 : « Choix et doutes », point 12.
  - **Mentions « lettre C »** (R-2992, point 0) : aucune dans ce texte (recherche faite) ; les correcteurs des brouillons 2 à 6
    étaient du modèle A : dit dans l'en-tête ; les entrées 1 à 5 de cette section, historiques, ne sont pas réécrites.
  - **Remarques facultatives R-1 à R-6** (lectures du brouillon 4) : R-1 appliquée (« Devis », hypothèses de coût : origine du
    haut des fourchettes d'écriture, recalculée pour la variante) ; R-2 appliquée (forme impersonnelle : en-tête, documents,
    « Raisons », « Devis », « Écarts », « Antériorités » ; les entrées historiques de cette section restent telles) ; R-3
    appliquée (ligne « sonde neuve des relais » retirée du devis, raison dite) ; R-4 appliquée (portée de la colonne « ce qui la
    réfute », sous la table des prédictions) ; R-5 sans objet (N fixé à 20 ; le taux du pilote n'est plus qu'une information) ;
    R-6 appliquée (« environ », « Taille »). Restes des tours précédents repris de même : renvoi « ceux de [CRIBLE-V] » des
    points à remesurer remplacé par la liste recopiée ; ligne « Témoin commun » réduite à sa décision, sans chiffre. Aucune ne
    change un critère.
  - **Points du rapport pour la mère, ouverts** (section 5 ; aucun n'est tranché ici) : la forme, inscrite (R-2992) ; le gel de
    III-6, à inscrire par une ligne datée à l'heure avant que le lecteur neuf du pilote rende sa lecture (aucune ligne trouvée
    jusqu'à R-2992 par `grep`) ; le mot de Lazar pour le lancement ; l'autonomie jusqu'au 17 novembre à 11:47Z (prolongeable au
    18) ; l'enveloppe de GO-2026-11-15-06 (1 308,60 au pire pour les cinq avec la variante, contre 1 275 : R-2992, point 3) ; le
    solde de crédits de Claude (260 au pire, plus 7 pour la sonde) ; N-045 point 3, à dire à Lazar avec le nœud d'adoption ; les
    risques : « non tranché » probable pour P2 (c'est l'issue prédite), code neuf, cinq files concurrentes et un seul fournisseur
    jamais éprouvés ; N = 20 et le minimum (« Choix et doutes », point 12).
  - **Décisions de R-2977 relues dans ce texte** : mondes séparés de ceux de (v) ; dollars principaux au prix public, prix de la
    configuration en sensibilité (vide ici) ; ablation de la frontière aux critères gelés (étage 5 ; deux espèces d'une même
    maison) ; GO-2026-11-15-06 pour l'essai, non pour l'adoption ; forme : tranchée par R-2992 (variante) ; N : la règle de
    R-2977 est remplacée par N = 20 (R-2992). Les décisions de R-2977 propres à (v) ne s'appliquent pas ici. Rien du pilote MR-2
    v14 n'est lu par ce texte ni par sa réécriture.

**Tour suivant** (obligatoire avant le scellement, R-2992, point 1 : un tour sur le différentiel du brouillon 6 à ce brouillon 7,
qui réécrit la forme) : sous-agent neuf qui n'a écrit ni ce texte, ni les brouillons 1 à 6, ni aucun rapport de contre-lecture de
ce crible.
**Fichiers à lui donner explicitement** : ce texte ; le brouillon 6 (`f377e927…`) et le programme
`appliquer-corrections-crible-iii-brouillon7.py` ; le rapport du tour 3 de la lecture du brouillon 4 (`99fb1024…`) ; les listes
« Si la variante est retenue » des rapports des tours 1, 2 et 3 et du tour 1 de la lecture du brouillon 4, et les sections 3
des rapports de la lecture du brouillon 4 (empreintes ci-dessus) ; les lignes R-2977 et R-2992 de `registres/decisions.md` et
toute ligne de ce registre sur le gel de III-6 ; la ligne GO-2026-11-15-06 ; [NOTE] (`2f6a69dd…`), § 1, § 3 (iii), § 3 (v),
§ 4 et annexe A ; [PILOTE] (`8aa33014…`), « Métrique », « Devis », bloc gelé ; [PROC-14] (`20355627…`), § 0 et § 7 ; N-045 v2
(`c7b05e39…`) ; N-058 (`854f2724…`) ; au besoin, les pièces de la liste du tour précédent : brouillons 1 à 5, rapports des
tours 1 à 3 et des deux premiers tours de la lecture du brouillon 4, programmes des brouillons 2 à 6, [CRIBLE-V] (« Métrique »,
« Devis »), [RELEVÉ] (`bd253b6c…`), [REC] (`eecd98fa…`), [MR2] (`47e38ec0…`), [V3] (`386d48ba…`), `mesure_pilote_v4.py`
(`676d5f37…`), `monde_riche_outils_v1.py` (`1825b956…`), l'annexe A et ses deux programmes."""),
]
NOMBRE_ATTENDU = 64

if not os.path.isfile(os.path.join(DEPOT, "src", "controle_ia", "prereg.py")):
    arret(f"racine du dépôt introuvable : {DEPOT}")
for chemin, attendu in ((SOURCE, SOURCE_SHA), (RAPPORT, RAPPORT_SHA)):
    if sha(chemin) != attendu:
        arret(f"empreinte différente : {chemin}")
for chemin in (CIBLE, CIBLE + ".sha256"):
    if os.path.exists(chemin):
        arret(f"cible déjà présente, jamais écrasée : {chemin}")
if len(COUPLES) != NOMBRE_ATTENDU or len({c[0] for c in COUPLES}) != NOMBRE_ATTENDU:
    arret("nombre de couples ou identifiants inattendus")

source = open(SOURCE, encoding="utf-8").read()
places = []
for ident, ancien, nouveau in COUPLES:
    n = source.count(ancien)
    if n != 1:
        arret(f"{ident} : « ancien » trouvé {n} fois dans la pièce de départ (une seule exigée)")
    debut = source.index(ancien)
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

with tempfile.TemporaryDirectory() as dossier:
    essai = os.path.join(dossier, "crible-iii-brouillon7.md")
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
