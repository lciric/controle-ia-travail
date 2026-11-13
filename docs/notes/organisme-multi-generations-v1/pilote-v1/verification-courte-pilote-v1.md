# Vérification courte du différentiel — préenregistrement du pilote, brouillon 1 → brouillon 2 — v1

- **Lecteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même lecteur que la contre-lecture du brouillon 1 ; autre modèle que
  l'auteur (Claude Opus 5.5). Je n'ai écrit ni le brouillon 2 ni ses programmes.
- **Heures** (relevées par `date -u`) : début 2026-11-13 09:59:27 UTC ; fin de rédaction 2026-11-13 10:04:02 UTC.
- **Interdits** : `interdits-communs-v2.md` appliqué (lu en entier au début de la contre-lecture) ; aucun chemin interdit
  ouvert ni listé ; aucune clé lue ; aucune écriture git ; aucun appel, aucune dépense ; aucun refus rencontré. Calculs : un
  processus à la fois, `ulimit -v 6000000`, `OMP_NUM_THREADS=2`, Python 3.13.18, numpy 2.5.3, au brouillon de session ; rien
  d'écrit dans le dépôt hors de ce fichier et de son compagnon.

## Verdict (une ligne)

**E-1 à E-11 sont appliquées à la lettre et les rejeux sont identiques ; scellable après trois retouches (R-1 à R-3, dont une
née du retrait S-9) et les préalables déjà listés par le texte.**

## Pièces vérifiées

| pièce | empreinte | contrôle |
|---|---|---|
| `pilote-v1/preenregistrement-pilote-conditionnelles-v1-brouillon2.md` | `b3fa3d9ef310d4540a525702e2d8e5cbc89df7bbdfd4f1125fd56a19be23b5a7` | égale au compagnon ; lu en entier ; `controle_ia.prereg.problemes` rend une liste vide |
| `pilote-v1/outils/mesure_pilote_v2.py` | `2230dd70bec2f3e9971dda3f5b7b76cc066493c97a3280fb077b12172e837b3d` | égale au compagnon ; lu en entier |
| `pilote-v1/outils/devis_pilote_v2.py` | `fa475e7a93e8bc4aa80c70a18d0e02ef1feae7d3a7751ff5bc29ad82c4ef5290` | égale ; lu |
| `sorties/taux-pilote-v2.json` ; `essai-mesure-pilote-v2.json` ; `graine-pilote-v2.json` ; `devis-pilote-v2.json` | `a1240a57…` ; `77fdd8d3…` ; `e9706452…` ; `dba76367…` | égales aux compagnons |
| `registres/decisions.md`, R-2504 à R-2507 | registre vivant | lues |

**Rejeux** (10:00:40 → 10:01:48 UTC) : `essai`, `taux`, `graine` du programme v2 et `devis_pilote_v2.py` relancés tels quels :
corps et `corps_sha256` **identiques** aux trois sorties scellées, liste des 14 modules importés identique, devis identique.

**Chiffres du texte recomptés contre les sorties** : table par compte (x = 0 à 9 sur 16), table par p vrai, taux 0,20 et 0,26,
valeurs à 12 et 14 appels (0,22 et 0,21 ; 0,29 et 0,27 ; 0,10 et 0,09), seuils de P-1 (9 sur 16, 8 sur 14, 7 sur 12), bascule
0,034, borne haute 0,0377 à 0 sur 16, bornes de sortie (70 000, 95 000, 36 000 jetons, recalculées sur les prix du devis v2),
devis 20 + 19 = 39 et 14,90 attendus, 365 + 57 = 422 : **tous justes**.

**Essais de ma main** (10:02:08 → 10:03:07 UTC, sur les quatre mondes d'essai du programme) : les trois nœuds de « P-2 avec
réserve » se déclenchent comme écrit (une carte à pente × 0,4 : compte τ' ≠ τ ; deux appels à quatre cartes chacun : classe de
l'unité carte ; un proposeur à 3 appels répondus qui trouve 2 fois : classe de p_prod) ; et le cas R-1 ci-dessous.

## Application de E-1 à E-11

| # | appliquée ? | remarque |
|---|---|---|
| E-1 | oui | règle au ponctuel (R-2506), tables par programme, phrase remplacée, « ne peut jamais établir H-P » écrit ; H-P redite à 0,034 |
| E-2 | oui | « répondu », minimum 12 sur 16 et 3 par monde, bornes de sortie, 16 couples vérifiés ; voir R-2 |
| E-3 | oui | première conditionnelle seule, n ≤ 16, seconde à part, dépendance entre appels d'un même modèle dite |
| E-4 | oui, effet faible | p_prod calculé, nœud si la classe diffère. À 16 appels répondus le nœud ne peut presque pas tirer (2 trouvés par un seul proposeur à 4 appels : survie 0,50, encore « favorable ») ; il tire si ce proposeur n'a que 3 appels répondus. Ce n'est pas un défaut : la classe favorable s'arrête déjà à 2 sur 16. Le tableau des changements dit « le banc tourne aussi à p_prod » ; la ligne P-2 des critères ne le dit que sous réserve : à accorder (une phrase) |
| E-5 | oui | R-2504 citée, « au plus 3 conditions emboîtées » au gabarit, au gardien, en C-5 et C-6, essai 3 admise / 4 refusée, empreinte du gabarit en marqueur, ligne de la conception dite retirée |
| E-6 | oui | C-16, C-17, non évaluables listées ; voir S-b |
| E-7 | oui, sauf un essai | P-0 (deux formes), P-1, P-2, minimum, neuf artefacts, septième carte, imports gelés ; la branche « P-2 avec réserve » n'est pas dans l'essai scellé : R-3 |
| E-8 | oui | deux nœuds codés ; le nœud « unité carte » tirera dès qu'un appel porte la conditionnelle dans plusieurs cartes (essayé : 2 appels × 4 cartes → nœud) : prudent, à savoir |
| E-9 | oui | 39 USD dit en tête ; Q-P4 sans défaut ; π1 cite `2230dd70…` (à recopier si le programme change encore, R-1) |
| E-10 | oui | fonction de graine écrite, codée, essayée, sans ambiguïté ; un seul compteur de tirage ; témoin d'isolement complété |
| E-11 | oui | prédiction d'auteur ; déclencheurs x = 0 et x ≥ 3 ; audit et lecture par des sous-agents neufs ; titres du gabarit, validateur passé |

## Retouches exigées avant le scellement

**R-1 — Témoin positif : dire si les proposeurs trouvent quelque chose (naît du retrait S-9).** Avec les probabilités par
classe, le brouillon 2 a retiré la seule mesure qui distingue « les proposeurs ne trouvent pas la conditionnelle » de « les
proposeurs ne trouvent rien ». Essayé : 16 appels dont toutes les cartes sont K1 seule → répondus 16, x = 0, **P-2 favorable,
aucun nœud** ; seul l'audit à la main le verrait. Une chaîne cassée ou un gabarit mal compris se lirait comme le meilleur
résultat pour l'hypothèse. Exigé, sans rien dire de la composition des mondes : le programme rapporte, sur les appels
répondus, le nombre d'appels dont une carte porte **au moins une composante autre que K1 et que les conditionnelles**
(dénominateur n, aucun compte par classe ni par monde) et le nombre dont une carte porte la **composante de condition** ; et
une lecture écrite d'avance : si moins de la moitié des appels répondus portent une telle composante, une issue P-2 favorable
est « avec réserve » (nœud de Lazar avant le banc). Cela demande un programme v3 (nom neuf, R12) ; la ligne π1 le cite.

**R-2 — La liste d'arrêt contredit le minimum.** Le minimum (12 sur 16, 3 par monde) tolère la perte d'un fournisseur entier,
et l'essai scellé « minimum tenu » est exactement ce cas (Astra en échec dans les quatre mondes → P-2). Mais la liste d'arrêt
dit « deux échecs du même fournisseur → arrêt du pilote » : après les mondes 1 et 2 le pilote s'arrêterait à 8 appels, issue
P-0, mondes brûlés (jamais réutilisés) et dépense faite. Le risque est réel : l'identifiant et le prix d'Astra sont « à
confirmer ». Choisir et écrire : ou bien un fournisseur en panne est abandonné (ses appels « échec ») et le pilote continue
avec les trois autres, ou bien l'arrêt est voulu et le texte dit que le minimum ne sert alors qu'aux troncatures et aux appels
sans carte.

**R-3 — Essai R5 de la branche « P-2 avec réserve ».** L'essai scellé ne fait tirer aucun des trois nœuds (son cas E-4 rend
`noeuds: []`). Je les ai fait tirer tous les trois, ils marchent ; les ajouter à l'essai du programme v3, avec le cas de R-1.

## Jugement sur S-9 (probabilités par classe retirées)

Ma remarque S-9 était mineure (« sans gravité, à dire ») : les dénominateurs laissaient lire le nombre de composantes par
classe. Le retrait complet est **acceptable pour la règle** (elle n'en dépend pas, R-2506 ne reprend que p_c) et **tient le
secret plus strictement**. Il coûte deux choses : (i) le modèle de proposeurs du banc garde 0,5 ; 0,25 ; 0,1 sans aucune
pièce, alors que le pilote était la seule occasion d'en donner une ; (ii) le témoin positif disparaît, ce qui est le vrai
défaut (R-1). Avis : garder le retrait des comptes par classe et par monde ; rétablir le témoin de R-1, qui ne dit rien de la
composition ; à la mère ou à Lazar de dire si une forme agrégée par classe (une part moyenne, sans dénominateur) vaut d'être
rapportée pour le banc — je ne l'exige pas.

## Q-P2 et Q-P4

- **Q-P2** : bien posée, trois options avec avantage et inconvénient, recommandation, défaut (a) sans dépense de plus ; (c)
  dite dépense et nœud. Rien à changer.
- **Q-P4** : bien posée, sans défaut (dépense). À ajouter : sous (b), la part « machine » de π2 tombe (19 → 16 USD), et les
  mondes privés et le secret vivent alors sur le poste de Lazar, qui est aussi celui d'où part la phrase.

## Marqueurs restants

Ceux que le texte liste sont les bons : [GABARIT-SHA256], [CHAMPS-ASTRA], identifiant et prix d'Astra, voie d'accès aux crédits
de Claude, bloc gelé des empreintes du code, Q-P2 et Q-P4. S'y ajoutent, non listés : la section « Contre-lecture » porte
encore « À faire » (à remplacer par l'entrée de cette vérification, avec ses deux empreintes) ; les lignes de GO portent
« GO-AAAA-MM-JJ-NN » et « mot de Lazar à recopier » (normal avant inscription) ; l'empreinte du programme dans π1 et dans la
section « Métrique » changera avec le programme v3 ; les bornes de sortie sont « estimées » et deviennent des valeurs de
configuration au gel du code. Aucun marqueur « À REMPLIR » ni de gabarit.

## Remarques sans exigence

- **S-a** « Au plus 3 conditions emboîtées » : dire si un niveau `par_sous_population` ou un `si_sinon` sur une
  sous-population compte comme une condition (C-5), sinon deux gardiens honnêtes peuvent différer.
- **S-b** C-16 : la loi « K1 + première conditionnelle calibrée » est une `transformee`, et un monde à trait latent est un
  `melange` ; si la grammaire servie ne les admet pas, C-16 arrêterait à tort : prendre des lois de référence écrites dans la
  grammaire servie.
- **S-c** Les outils v1 à v3 importés ne sont vérifiés que contre leur propre compagnon ; la liste `modules_importes` de la
  sortie est à comparer au bloc gelé à l'étape 1 du plan d'analyse.
- **S-d** La liste des modules importés nomme deux fois `mesure_pilote_v2.py` ; sans effet.

## Réserves

- Vérification du différentiel, non une seconde contre-lecture entière ; code v67 et arbre de l'organisme toujours non lus.
- Essais de ma main sur des graines publiques de développement, non scellés.
- Même lecteur que la contre-lecture, même maison de modèles que l'auteur ; Fable 5.2 est aussi proposeur du pilote.
