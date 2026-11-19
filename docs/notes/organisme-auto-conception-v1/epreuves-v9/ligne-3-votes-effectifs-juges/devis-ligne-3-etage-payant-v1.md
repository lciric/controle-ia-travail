# Ligne 3 (votes effectifs des juges croisés, mesurés sur témoins plantés) — devis de l'étage payant — v1

**Statut : brouillon 1, à contre-lire ; aucune dépense avant la ligne de GO de la mère.** Ce devis chiffre l'étage 2 du préenregistrement `preenregistrement-ligne-3-votes-effectifs-juges-v1.md` (même dossier). Il n'engage rien.

- **Écrit par** : le rédacteur (modèle F), le 2026-11-19 (`date -u`), processeur seul, aucun appel de modèle, aucune dépense. Contre-lecteur prévu : modèle O.
- **Mot de Lazar**, verbatim : « go ligne 3 devis 25 USD ». Principe tenu : GO-2026-11-19-60 (le coût ne limite plus une ligne qui améliore considérablement l'organisme ; chaque étage payant garde son devis et sa ligne de GO). Option (a) de l'ordre de passage v3 : ce devis est présenté tôt, avant l'étage sur processeur.
- **Calcul** : `calcul_devis_ligne_3_v1.py`, sortie `calcul-devis-ligne-3-v1.json`, même dossier, empreintes dans les fichiers compagnons ; rejoué deux fois, sorties identiques à l'octet. Tout chiffre ci-dessous en vient, arrondi.
- **Sources des coûts**, lues par le programme et vérifiées par empreinte :
  - manifeste de fin du lanceur de la course v9, `runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json`, `28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7` ;
  - rapport de l'épreuve réelle des témoins, version 9, `docs/notes/organisme-auto-conception-v1/course-v4/epreuve-temoins-reelle-auto-conception-v9.json`, `e7837f4c40bca9aaed7ae0d3e8bdb51f9f36284ffb21c677575368699a61ca84` (champ de coût seulement) ;
  - témoins du juge, version 2, pour leur longueur : `docs/notes/organisme-auto-conception-v1/course-v2/temoins-juge-auto-conception-v2.json`, `84a1e0ea870ecb54c2de8ec5071e689e2ba409b3c97aecb57ab16ef3388439e0`.

## 0. Verdict

| | appels | estimation | haut | pire |
|---|---|---|---|---|
| **étage 2, 100 témoins, deux juges** | 504 | **16,52 USD** | **22,49 USD** | **44,38 USD** |

- **Plafond d'arrêt proposé pour la ligne de GO : 25 USD**, le montant du mot de Lazar. Il couvre le cas haut avec 11 % de marge. Il ne couvre pas le pire cas : s'il coupe, la mesure principale est déjà faite (§ 5).
- L'étage 1 (processeur) et l'écriture des témoins ne coûtent aucun appel.
- La proposition annonçait « environ 25 USD ». Le recalcul sur les coûts réels donne moins en estimation, parce que les témoins sont plus courts que les cartes, et autant en cas haut.

## 1. Coûts réels des juges à la course v9

| rôle | appels | coût réel | par appel | devis d'alors | réel / devis |
|---|---|---|---|---|---|
| juge Opus | 94 | 6,863 USD | 0,0730 USD | 3,478 USD | 1,97 |
| juge Argon | 94 | 2,409 USD | 0,0256 USD | 3,262 USD | 0,74 |
| les deux, par carte | — | — | 0,0986 USD | — | — |

Ces coûts sont ceux de cartes de 4 994 caractères en moyenne.

## 2. Effet de la longueur des témoins

- Les onze témoins de la version 2 font 1 936 caractères en moyenne (de 1 239 à 2 749), soit 0,39 fois une carte. Les témoins neufs sont écrits dans la même fourchette (de 1 200 à 2 800 caractères).
- Le coût ne suit pas la longueur : la consigne (4 273 octets) et la réponse du juge pèsent autant sur un témoin que sur une carte. Mesure disponible : l'épreuve réelle des témoins de la version 9 a coûté 1,183 USD pour 33 appels (deux juges et l'aiguilleur sur onze témoins), soit 0,0359 USD par appel ; les trois mêmes rôles coûtaient 0,0488 USD par appel sur les cartes. **Rapport témoin sur carte : 0,73.**
- Limite : ce rapport mêle l'aiguilleur aux deux juges (le rapport d'épreuve ne donne que le total). Il est donc appliqué à l'estimation seulement.

## 3. Plan d'appels (préenregistrement, « Étage 2 »)

| bloc | ce qu'il fait | juge Opus | juge Argon | haut |
|---|---|---|---|---|
| P — plomberie | 2 témoins de la version 2, réponses lisibles, coût relevé | 2 | 2 | 0,20 USD |
| A — base | chaque juge, une fois, sur les 100 témoins | 100 | 100 | 9,86 USD |
| B — répétitions à l'identique | une lecture de plus par le juge Opus, deux de plus par le juge Argon, sur les 100 témoins | 100 | 200 | 12,43 USD |
| **total** | | **202** | **302** | **22,49 USD** |

Le bloc B porte le témoin « un seul juge, k votes » à coût apparié : le collège coûte 0,0986 USD par témoin ; au même coût, le juge Argon rend 3 votes (0,077 USD) et le juge Opus 1 seul (0,073 USD). La seconde lecture du juge Opus est hors appariement ; elle sert à mesurer la corrélation de ses erreurs avec lui-même.

## 4. Trois cas

| cas | règle | juge Opus | juge Argon | total |
|---|---|---|---|---|
| **estimation** | tarif des cartes × 0,73 (témoins plus courts) | 10,84 USD | 5,69 USD | **16,52 USD** |
| **haut** | tarif des cartes, sans rabais de longueur | 14,75 USD | 7,74 USD | **22,49 USD** |
| **pire** | tarif des cartes × 1,97 (le dépassement du juge Opus à la v9, appliqué aux deux juges) | 29,10 USD | 15,27 USD | **44,38 USD** |

Borne de plomberie, jamais atteinte en pratique : 504 appels au plafond de session du juge (0,60 USD) font 302 USD ; c'est le plafond d'arrêt qui protège, pas elle.

**Part par clé.** Clé Claude (le juge Opus ; la clé que nomme la pièce de départ de la mère) : 10,84 USD en estimation, 14,75 au cas haut, 29,10 au pire. Clé d'Argon : 5,69, 7,74 et 15,27 USD. À la fin de la course v9, le manifeste estimait le reste de la clé Claude employée à 162,56 USD ; le relevé du jour se refait avant le départ.

## 5. Plafond d'arrêt proposé : 25 USD

- Égal au mot de Lazar ; la ligne de GO et le programme portent ce montant exact.
- Règle : aucun appel ne part si le cumul plus le plafond de session dépasse 25 USD.
- **Si le plafond coupe**, l'ordre des appels protège la mesure principale. Le bloc A (corrélation des erreurs entre juges, votes effectifs, agrégations) coûte 9,86 USD au cas haut : il tient jusqu'à 2,5 fois le tarif prévu. Le bloc B commence par la moitié « lecture ». S'il reste incomplet, le préenregistrement dit ce qui est lu et ce qui devient « non mesuré ».
- Sous 25 USD, au cas haut, la banque peut monter à 110 témoins au plus.

## 6. Ce qui n'est pas dans ce devis

| poste | estimation | haut | pire | pourquoi il est à part |
|---|---|---|---|---|
| **option C : second rendu réel**, à présentation permutée, moitié « lecture », un appel par juge (100 appels) | + 3,62 USD | + 4,93 USD | + 9,73 USD | bras de l'étage 1 seulement dans le préenregistrement ; avec lui le cas haut passe à 27,42 USD, au-dessus de 25 |
| **dix témoins de plus**, même plan | + 1,64 USD | + 2,23 USD | + 4,40 USD | le nombre de témoins se fixe par le calcul de puissance de l'étage 1 |
| 150 témoins | 24,71 USD | 33,63 USD | 66,37 USD | si l'étage 1 le demande : devis et ligne de GO neufs |
| 200 témoins | 32,90 USD | 44,78 USD | 88,36 USD | idem |
| 300 témoins | 49,28 USD | 67,07 USD | 132,35 USD | idem |
| **d'autres lignées comme juges** (Fable, Astra, Carbon) | non chiffré | non chiffré | non chiffré | aucun coût de juge n'est mesuré pour elles, et leur service comme juges n'a jamais passé d'épreuve réelle ; un essai de quelques appels, sur son propre devis, viendrait d'abord |
| écriture des témoins | 0 USD d'appels | — | — | fragments écrits en session, composition par programme ; une vérification par une autre lignée serait un appel, donc un devis |

## 7. Ce qui est scellé avant la dépense

1. Le préenregistrement, contre-lu par le modèle O, scellé par la mère, avec le commit du code.
2. Le rapport de l'étage 1 et son verdict : l'étage 2 ne part que sur un « oui » de l'étage 1 à 100 témoins ; sinon ce devis est refait à la taille voulue et retourne à Lazar.
3. L'additif de portée, s'il y a lieu (comparaisons d'agrégations déclarées descriptives).
4. La banque des 100 témoins, son journal de construction (la vérité), son partage en deux moitiés, le rapport de vérification du contre-lecteur et le rapport d'audit du générateur.
5. Le programme de l'étage 2, ses essais des gardes (cas sain et artefact), la configuration des juges et l'empreinte de la consigne servie.
6. La ligne de GO de la mère, au montant du plafond.

## 8. Réserves

- Le rapport de coût témoin sur carte (0,73) vient de 33 appels où l'aiguilleur est mêlé aux juges.
- Le juge Opus a coûté 1,97 fois son devis à la course v9 ; je ne sais pas pourquoi (longueur des réponses, réflexion facturée). Le pire cas reprend ce facteur ; rien ne dit qu'il borne.
- Les répétitions à l'identique peuvent être servies moins cher par un cache du fournisseur ; je n'en tiens pas compte.
- Ce devis ne dit rien de la valeur de la ligne : il chiffre un instrument de mesure. Aucun résultat acheté ici ne fera trancher une carte par un juge.
