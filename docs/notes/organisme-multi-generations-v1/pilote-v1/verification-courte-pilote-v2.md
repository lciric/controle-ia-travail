# Vérification courte du différentiel — préenregistrement du pilote, brouillon 2 → brouillon 3 — v2

- **Lecteur** : Claude Fable 5.2 (`claude-fable-5-2`), le même lecteur que la contre-lecture du brouillon 1 et que la
  vérification courte du brouillon 2 ; autre modèle que l'auteur (Claude Opus 5.5). Je n'ai écrit ni le brouillon 3 ni son
  programme.
- **Heures** (relevées par `date -u`) : début 2026-11-13 10:14:41 UTC ; fin de rédaction 2026-11-13 10:18:13 UTC.
- **Interdits** : `interdits-communs-v2.md` appliqué ; aucun chemin interdit ouvert ni listé ; aucune clé lue ; aucune écriture
  git ; aucun appel, aucune dépense ; aucun refus rencontré. Calculs : un processus à la fois, `ulimit -v 6000000`,
  `OMP_NUM_THREADS=2`, Python 3.13.18, numpy 2.5.3, au brouillon de session ; rien d'écrit dans le dépôt hors de ce fichier et
  de son compagnon. Un de mes lancements a dépassé deux minutes et a fini en arrière-plan (code 0) ; aucun second processus
  n'a tourné en même temps.

## Verdict (une ligne)

**R-1 à R-3 sont appliquées, les rejeux sont identiques et rien d'autre n'a changé ; scellable après une retouche d'une ligne
du programme (R-4 : fermer la limite du témoin positif) et les préalables déjà listés par le texte.**

## Pièces vérifiées

| pièce | empreinte | contrôle |
|---|---|---|
| `pilote-v1/preenregistrement-pilote-conditionnelles-v1-brouillon3.md` | `fab4d6b960ec0d52c6fd1d7317236ae7f7336d332178eac3823d05b8995af15d` | égale au compagnon ; différentiel entier contre le brouillon 2 (`b3fa3d9e…`) lu ligne à ligne |
| `pilote-v1/outils/mesure_pilote_v3.py` | `5d5a263282cc73783b4cb6bae99fe5cc3b56d584e0c848221478232526ff8e0b` | égale au compagnon ; différentiel entier contre le v2 (`2230dd70…`) lu |
| `sorties/essai-mesure-pilote-v3.json` ; `sorties/taux-pilote-v3.json` | `5d94516e0f16fa05bdb86dcc1e84633315b7ac9c4d83ef98625888f9167989bc` ; `f8c8e803d2f54aef43c4c112ad64ef526d28e8f552ea30d26e4cd558e95d8692` | égales aux compagnons |
| `registres/decisions.md`, R-2508 à R-2511 | registre vivant | lues : Q-P2 (a), Q-P4 (a), retrait S-9 gardé |

**Rejeux** (10:15:08 → 10:16:15 UTC) : `essai`, `taux`, `graine` du programme v3 relancés tels quels. Corps et `corps_sha256` de
l'essai et des taux **identiques** aux sorties v3 scellées ; les taux et l'essai de graine rejoués par le v3 sont identiques,
corps et empreinte de corps, aux sorties du v2 : le texte a raison de dire que ces parties n'ont pas changé. `tout_conforme`
vrai ; 13 modules importés (doublon retiré).

## R-1 à R-3

| # | appliquée ? | constat |
|---|---|---|
| R-1 | oui | témoin t (appels portant une composante autre que l'effet de K1 et que les conditionnelles) et c (appels portant la composante de condition), dénominateur n, aucun compte par classe ni par monde ; nœud « P-2 favorable avec réserve » si 2t < n, codé, écrit aux critères, essayé (16 appels de copies de K1 : x = 0, t = 4, nœud tiré ; cas sain : t = 16, c = 15, aucun nœud). π1 et « Métrique » citent `5d5a2632…` |
| R-2 | oui | décision de la mère portée : arrêt « deux échecs du même fournisseur » retiré ; fournisseur en panne abandonné, appels restants « échec », pilote continué, perte rapportée ; le minimum tient la perte d'un fournisseur entier et d'un seul ; cohérent avec l'essai « minimum tenu » |
| R-3 | oui | les trois nœuds et le cas R-1 sont dans l'essai scellé et tirent : compte τ contre τ' (x = 1 contre 2), unité carte (8 cartes sur 96, classe défavorable), proposeur à 3 appels répondus (x = 2 sur 15, p_prod 0,0447 défavorable) |

## La limite déclarée du témoin positif : à fermer (R-4)

**Le fait.** Le texte dit que des copies exactes de K1 « portent » une composante faible dans un monde d'essai sur quatre,
d'où un témoin de 4 sur 16 pour des cartes qui ne trouvent rien. Je l'ai remesuré : dans le monde d'essai 3, la loi K1 servie
porte, outre son effet, la faible E6 (information 0,026, attribution 0,022, au-dessus de 0,75 · I) ; rien dans les mondes 1,
2 et 4.

**Pourquoi ce n'est pas acceptable tel quel.** Le témoin n'existe que pour un cas : une chaîne qui rend des cartes voisines de
K1. C'est exactement le cas où il est gonflé. Le nœud tire si 2t < n. Si K1 porte une autre composante dans deux des quatre
mondes du pilote, des cartes qui ne trouvent rien donnent t = 8 sur 16 et **le nœud ne tire pas**. Avec une chance d'environ
un quart par monde (un monde d'essai sur quatre, donc estimation très grossière), cela arrive à peu près une fois sur quatre.
Les mondes sont secrets : personne ne pourra le savoir avant ni le voir après. La phrase du texte « il reste sous la moitié »
n'est vraie que des mondes d'essai. Et l'audit à la main ne rattrape que x = 0 : à x = 1 ou 2 (favorable, audit non
déclenché) le témoin est seul.

**La retouche, une ligne.** Retirer du témoin ce que la loi K1 servie porte déjà à elle seule : dans `mesurer`, les composantes
exclues deviennent « effet de K1, conditionnelles, **et tout ce que K1 servie porte** » (`_porte(pm, pm["k1"])`, déjà
disponible : la loi K1 est dans `pm`). Essayé de ma main sur les quatre mondes d'essai : une carte ordinaire « K1 + une
moyenne » garde son témoin dans les quatre mondes ; des copies de K1 tombent à 0 sur 16. Le témoin ne peut alors plus être
gonflé par K1 ; il peut être très légèrement dégonflé (une carte qui ne ferait que retrouver mieux cette même faible), ce qui
va dans le sens prudent (réserve tirée, nœud de Lazar). À porter : programme v4 (nom neuf, R12), essai rejoué avec « cas R-1 :
t = 0 sur 16 », phrase « Réserve sur le témoin » du texte remplacée, empreinte de π1 et de « Métrique » mise à jour.

**Ce qui reste vrai après la retouche**, à garder en une phrase : l'attribution déborde aussi ailleurs (monde d'essai 2 : une
carte « K1 + E3 » porte aussi E7, qu'elle ne contient pas). Le témoin dit « les cartes vont au-delà de K1 », pas « elles
trouvent telle composante » ; c'est suffisant pour son rôle.

## S-a à S-d

| # | constat |
|---|---|
| S-a | sans risque : un `si_sinon` compte, sur un trait ou sur une sous-population ; un niveau `par_sous_population` ne compte pas ; fonction `conditions_emboitees` essayée (3 ; 4 ; 3 sous `par_sous_population` ; 4 avec un `si_sinon` sur sous-population). Le gardien de la chaîne devra donner les mêmes nombres : à mettre dans l'essai R5 de C-5 (déjà dit en C-5) |
| S-b | sans risque : trois lois de référence par monde, écrites en `softmax`, `si_sinon`, `par_sous_population` ; sur les quatre mondes d'essai, 0, 1 et 2 ou 3 conditions, toutes admises. La référence « K1 » est le monde restreint à l'effet de K1, pas la loi K1 servie ; sans conséquence pour le gardien |
| S-c | sans risque : étape 1 du plan d'analyse complétée (liste `modules_importes` comparée au bloc gelé) ; le bloc gelé reste un marqueur |
| S-d | fait : 13 modules au lieu de 14 |

## Rien d'autre changé ?

**Oui.** Texte : toutes les différences avec le brouillon 2 relèvent de R-1 à R-3, S-a à S-d, l'accord de la phrase E-4, les
mots R-2508 à R-2510 (Q-P2 (a), Q-P4 (a) avec « machine jetable » dans π2, retrait gardé), la section « Contre-lecture » mise
à jour et la liste des marqueurs. Hypothèse, prédiction, tables de taux, seuils, minimum, règle P-0 / P-1 / P-2, audit,
devis et montants des lignes : **mot pour mot inchangés**. Programme : les ajouts sont le témoin, `conditions_emboitees`,
`types_de`, `lois_de_reference`, les essais neufs et le doublon retiré ; `issue_de`, `taux`, `graine_monde_pilote`, la porte
et les refus sont inchangés (taux et graine rejoués identiques à ceux du v2).

Deux détails à corriger en passant, sans exigence : la section « Contre-lecture » devra recevoir l'entrée de cette
vérification (brouillon `fab4d6b9…`, ce rapport) ; la section « Préalables » dit encore « si la mère le juge utile,
vérification courte du différentiel brouillon 2 → brouillon 3 ».

## Réserves

- Vérification du différentiel seulement ; code v67 et arbre de l'organisme toujours non lus.
- Mesures de ma main sur quatre mondes de graines publiques, non scellées ; la fréquence « un monde sur quatre » n'a pas
  d'autre appui.
- Même lecteur pour les trois lectures, même maison de modèles que l'auteur ; Fable 5.2 est aussi proposeur du pilote.
