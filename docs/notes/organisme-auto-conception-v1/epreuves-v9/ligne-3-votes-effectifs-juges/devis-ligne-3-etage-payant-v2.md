# Ligne 3 (votes effectifs des juges croisés, mesurés sur témoins plantés) — devis de l'étage payant — v2

**Statut : version 2, à vérifier ; aucune dépense avant la ligne de GO de la mère.** Ce devis chiffre l'étage 2 du préenregistrement `preenregistrement-ligne-3-votes-effectifs-juges-v2.md` (même dossier). Il n'engage rien. Il remplace `devis-ligne-3-etage-payant-v1.md` (`d02aa27a30fa908724cc45da6a08d7c60cc4ded726dc1d1c1af9175e13f6e227`), gardé sans modification.

**En tête, ce que la mère a demandé de dire.**
- **Le cas haut recalculé ne dépasse pas 25 USD** : 22,49 USD, soit 23,09 USD avec la réserve du plafond de session. Rien ne sort de la base. Le plan d'appels est celui de la version 1 (504 appels) : les 17 corrections de la contre-lecture ne changent aucun montant.
- **Le pire cas (44,38 USD) dépasse 25 USD.** C'est une marge de prudence, pas un dépassement observé (§ 4). Le plafond d'arrêt le coupe ; § 5 dit ce qui reste lisible. Si la mère lit la condition de GO-2026-11-19-66 (« devis au plus égal au plafond ») sur le pire cas et non sur le cas haut, **ce qui sortirait de la base est écrit au § 5 bis** ; ce n'est pas ma recommandation.
- **Une conséquence à connaître avant de signer.** Le rédacteur prédit (P1 du préenregistrement) que la tolérance de l'estimateur tient « à la limite » à 100 témoins. Si l'étage 1 dit « non, pas à cette taille », **la ligne à 25 USD ne part pas** : un devis à 200 témoins (haut 44,78 USD, pire 88,36 USD) retourne à Lazar.
- Le témoin « un juge seul répété k fois, à coût apparié » est gardé (§ 3).
- La mesure par d'autres lignées comme juges est chiffrée hors base, en ordre de grandeur (§ 6 bis).

- **Écrit par** : le rédacteur (modèle F), le 2026-11-19 (`date -u`, entre 14:04 et 14:13), processeur seul, aucun appel de modèle, aucune dépense. Contre-lecture de la version 1 par le modèle O : `contre-lecture-ligne-3-v1.md`, `32e446c7a38915d48c57e44f558fcd5d806c9b9581457734fc62414694b0e7ba`, constat 13 (devis recalculé, juste ; deux phrases à corriger, appliquées ici).
- **Mot de Lazar**, verbatim : « go ligne 3 devis 25 USD ». Ligne au registre (main, commit `416a33428e2d1bba28751680721a759f4d1359d3`, `registres/go.md`, `0682f0aa8a102b9c76256878e8ab08dfd8bcc7dcff57e99cbd824f8c98752aa1`) : **GO-2026-11-19-66**, accord conditionnel, plafond 25 USD, échéance 2026-11-27 ; conditions : préenregistrement et devis scellés, contre-lus ; devis au plus égal au plafond ; l'avis des juges reste descriptif (N-058) ; aucun départ avant. Principe tenu : GO-2026-11-19-60 ; ordre de passage v3, option (a) (GO-2026-11-19-67).
- **Calcul** : `calcul_devis_ligne_3_v2.py`, sortie `calcul-devis-ligne-3-v2.json`, même dossier, empreintes dans les fichiers compagnons ; rejoué deux fois (`python3 -I -B`, depuis la racine du dépôt), sorties identiques à l'octet. Tout chiffre ci-dessous en vient, arrondi. Les scénarios par nombre de témoins sont égaux à ceux de la version 1 (vérifié par programme).
- **Constante retirée (règle R6).** La version 1 recopiait la longueur moyenne des cartes de la course v9 sans le programme qui l'avait mesurée. Elle n'entrait dans aucun coût : elle est retirée du calcul et du texte. Le calcul n'ouvre plus aucune carte.
- **Sources des coûts**, lues par le programme et vérifiées par empreinte :
  - manifeste de fin du lanceur de la course v9, `runs/20261119-094145-course-auto-conception-v9/manifeste-lanceur-fin.json`, `28bc36df390d8481fb5bd9118cf764843ffea60856412d825ecbf08e7cee5be7` ;
  - rapport de l'épreuve réelle des témoins, version 9, `docs/notes/organisme-auto-conception-v1/course-v4/epreuve-temoins-reelle-auto-conception-v9.json`, `e7837f4c40bca9aaed7ae0d3e8bdb51f9f36284ffb21c677575368699a61ca84` (champ de coût seulement) ;
  - témoins du juge, version 2, pour leur longueur : `docs/notes/organisme-auto-conception-v1/course-v2/temoins-juge-auto-conception-v2.json`, `84a1e0ea870ecb54c2de8ec5071e689e2ba409b3c97aecb57ab16ef3388439e0`.

## 0. Verdict

| | appels | estimation | haut | pire |
|---|---|---|---|---|
| **étage 2, 100 témoins, deux juges** | 504 | **16,52 USD** | **22,49 USD** | **44,38 USD** |

- **Plafond d'arrêt de la ligne de GO : 25 USD** (GO-2026-11-19-66). Il couvre le cas haut. Marge nominale : 11 %. **Marge effective : 8,5 %**, parce que la règle d'arrêt garde en réserve le plafond de session d'un appel (0,60 USD) : 24,40 / 22,49.
- Il ne couvre pas le pire cas : s'il coupe, la mesure principale est déjà faite (§ 5).
- L'étage 1 (processeur) et l'écriture des témoins ne coûtent aucun appel.

## 1. Coûts réels des juges à la course v9

| rôle | appels | coût réel | par appel | devis d'alors | réel / devis |
|---|---|---|---|---|---|
| juge Opus | 94 | 6,863 USD | 0,0730 USD | 3,478 USD | 1,97 |
| juge Argon | 94 | 2,409 USD | 0,0256 USD | 3,262 USD | 0,74 |
| les deux, par carte | — | — | 0,0986 USD | — | — |

## 2. Effet de la longueur des témoins

- Les onze témoins de la version 2 font 1 936 caractères en moyenne (de 1 239 à 2 749). Les témoins neufs sont écrits dans la même fourchette (de 1 200 à 2 800 caractères). Ils sont plus courts que les cartes de la course.
- Le coût ne suit pas la longueur : la consigne et la réponse du juge pèsent autant sur un témoin que sur une carte. Mesure disponible : l'épreuve réelle des témoins de la version 9 a coûté 1,183 USD pour 33 appels (deux juges et l'aiguilleur sur onze témoins), soit 0,0359 USD par appel ; les trois mêmes rôles coûtaient 0,0488 USD par appel sur les cartes. **Rapport témoin sur carte : 0,73.**
- Limite : ce rapport mêle l'aiguilleur aux deux juges (le rapport d'épreuve ne donne que le total). Il est donc appliqué à l'estimation seulement.

## 3. Plan d'appels (préenregistrement, « Étage 2 »)

| bloc | ce qu'il fait | juge Opus | juge Argon | haut |
|---|---|---|---|---|
| P — plomberie | 2 témoins de la version 2, réponses lisibles, coût relevé | 2 | 2 | 0,20 USD |
| A — base | chaque juge, une fois, sur les 100 témoins | 100 | 100 | 9,86 USD |
| B — répétitions à l'identique | par témoin, à la suite : une lecture de plus par le juge Opus, deux de plus par le juge Argon ; la moitié « lecture » d'abord | 100 | 200 | 12,43 USD |
| **total** | | **202** | **302** | **22,49 USD** |

**Le témoin « un seul juge répété k fois, à coût apparié » est gardé.** Le collège coûte 0,0986 USD par témoin. Au même coût, le juge Argon rend 3 votes (0,0769 USD) : c'est le bras R-Argon, lu à la majorité de ses trois rendus. Le juge Opus n'en rend qu'un (0,0730 USD) : son bras à coût apparié est son vote seul. La seconde lecture du juge Opus est hors appariement ; elle sert à mesurer la corrélation de ses erreurs avec lui-même.

Le bloc B coûte 0,1243 USD par témoin au cas haut. Il est entrelacé par témoin pour qu'une coupure laisse des témoins complets pour les trois rendus (contre-lecture, constat 14).

Les bras ajoutés par la version 2 du préenregistrement (« au moins un », pondération par la précision) se lisent sur les mêmes verdicts : **aucun appel de plus**.

## 4. Trois cas

| cas | règle | juge Opus | juge Argon | total |
|---|---|---|---|---|
| **estimation** | tarif des cartes × 0,73 (témoins plus courts) | 10,84 USD | 5,69 USD | **16,52 USD** |
| **haut** | tarif des cartes, sans rabais de longueur | 14,75 USD | 7,74 USD | **22,49 USD** |
| **pire** | tarif des cartes × 1,97, appliqué aux deux juges | 29,10 USD | 15,27 USD | **44,38 USD** |

**Ce qu'est le pire cas.** Le facteur 1,97 est le rapport du coût réel du juge Opus à son ancien devis, à la course v9. Il est appliqué ici à un coût **déjà réel**. C'est une marge de prudence, pas un dépassement observé sur cette base. Rien ne dit qu'il borne.

Borne de plomberie, jamais atteinte en pratique : 504 appels au plafond de session du juge (0,60 USD) font 302 USD ; c'est le plafond d'arrêt qui protège, pas elle.

**Part par clé.** Clé Claude (le juge Opus) : 10,84 USD en estimation, 14,75 au cas haut, 29,10 au pire. Clé d'Argon : 5,69, 7,74 et 15,27 USD. Le relevé des crédits se refait avant le départ.

## 5. Plafond d'arrêt : 25 USD — ce qui se passe s'il coupe

- La ligne de GO et le programme portent ce montant exact.
- Règle : aucun appel ne part si le cumul plus le plafond de session (0,60 USD) dépasse 25 USD. Le cumul utile est donc de 24,40 USD.
- **L'ordre des appels protège la mesure principale.** Plomberie, puis bloc A (corrélation des erreurs entre juges, votes effectifs, agrégations), puis bloc B.

| ce qui reste complet | jusqu'à quel multiple du tarif des cartes |
|---|---|
| plomberie et bloc A | **2,4 fois** (2,43) |
| en plus, bloc B sur 40 témoins (le seuil de lecture des répétitions) | 1,62 fois |
| en plus, bloc B sur les 50 témoins de la moitié « lecture » | 1,50 fois |
| tout, les 100 témoins | 1,085 fois |

- Au pire cas (1,97 fois), le bloc A est complet et le bloc B ne l'est que sur 18 témoins : la corrélation de chaque juge avec lui-même est alors « non mesurée » et le verdict est non concluant (préenregistrement, « Si le plafond coupe »). La corrélation entre juges et le nombre de votes effectifs restent mesurés.
- Sous 25 USD, au cas haut, la banque peut monter à **108 témoins** au plus (110 sans la réserve de session).

## 5 bis. Si la mère veut que le pire cas tienne sous 25 USD : ce qui sortirait de la base

Je ne le recommande pas : le plafond d'arrêt protège déjà la dépense, et la comparaison ρ′ − ρ, qui porte le verdict, a besoin du bloc B.

| base réduite | appels | estimation | haut | pire | ce qu'elle perd |
|---|---|---|---|---|---|
| plomberie et bloc A seuls | 204 | 7,39 USD | 10,06 USD | 19,85 USD | toutes les répétitions : plus de ρ′, plus de témoin « un juge répété k fois » ; il reste la corrélation entre juges, les votes effectifs et la table par juge ; **le verdict de l'étage 2 serait non concluant par construction** |

Aucune base qui garde le bloc B sur 40 témoins ne tient sous 24,40 USD au pire cas (elle coûterait 29,66 USD). Garder le témoin « un juge répété » et tenir le pire cas sous 25 USD sont donc incompatibles à 100 témoins.

## 6. Ce qui n'est pas dans ce devis

| poste | estimation | haut | pire | pourquoi il est à part |
|---|---|---|---|---|
| **option C : second rendu réel**, à présentation permutée, moitié « lecture », un appel par juge (100 appels) | + 3,62 USD | + 4,93 USD | + 9,73 USD | bras de l'étage 1 seulement dans le préenregistrement ; avec lui le cas haut passe à 27,42 USD, au-dessus de 25 |
| **dix témoins de plus**, même plan | + 1,64 USD | + 2,23 USD | + 4,40 USD | le nombre de témoins se fixe par le calcul de puissance de l'étage 1 |
| 150 témoins | 24,71 USD | 33,63 USD | 66,37 USD | si l'étage 1 le demande : devis et ligne de GO neufs |
| 200 témoins | 32,90 USD | 44,78 USD | 88,36 USD | idem |
| 300 témoins | 49,28 USD | 67,07 USD | 132,35 USD | idem |
| **d'autres lignées comme juges** | voir § 6 bis | | | ordre de grandeur seulement |
| écriture des témoins | 0 USD d'appels | — | — | fragments écrits en session, composition par programme ; une vérification par une autre lignée serait un appel, donc un devis |

## 6 bis. D'autres lignées comme juges (Argon, Astra, Carbon, Fable) — hors base, ordre de grandeur

**Ce n'est pas un devis. Aucune ligne de GO ne peut s'appuyer sur ces chiffres.**

**Argon** est déjà l'un des deux juges : son coût de juge est mesuré (0,0256 USD par appel) et il est dans la base.

**Astra, Carbon et Fable n'ont aucun coût de juge mesuré** : à la course v9, ces lignées n'ont servi que comme proposeurs. Leur service comme juges n'a jamais passé d'épreuve réelle.

**Ce qu'il faudrait mesurer d'abord**, par lignée, sur un devis et une ligne de GO à part :
1. un essai court sur les onze témoins de la version 2 (onze appels), comme l'épreuve réelle qu'ont passée les deux juges actuels ;
2. ce qu'il rend : la part de réponses lisibles (bloc aux cinq clés), le coût réel par appel, le modèle réellement servi, la tenue sous le plafond de session ;
3. ce qu'il ne rend pas : une mesure d'erreur (onze témoins à défaut déclaré ne séparent rien).
Faire d'une lignée un juge de l'organisme est par ailleurs un changement de la configuration des juges : c'est un nœud de Lazar (N-058 ; GO-2026-11-19-65 et -68 : « à mesurer avant adoption »).

**Ordre de grandeur, à défaut de mesure.** Seule base disponible : les coûts de proposeur de la course v9. Hypothèse, dite et fragile : un appel de juge coûte, par rapport à un appel de proposeur de la même lignée, ce qu'il coûte chez les deux lignées qui ont tenu les deux rôles (Argon : 0,068 ; Opus : 0,108). « Bas » et « haut » sont ces deux rapports ; « large » est le haut multiplié par 1,97.

| lignée | appel de proposeur, réel | appel de juge, bas à haut (large) | essai d'abord, 11 appels | bloc A seul, 100 témoins | bloc A et une répétition, 200 appels |
|---|---|---|---|---|---|
| Astra | 0,431 USD | 0,029 à 0,047 USD (0,092) | 0,3 à 0,5 USD (1,0) | 2,9 à 4,7 USD (9,2) | 5,8 à 9,3 USD (18,4) |
| Carbon | 2,247 USD | 0,152 à 0,243 USD (0,479) | 1,7 à 2,7 USD (5,3) | 15,2 à 24,3 USD (47,9) | 30,4 à 48,6 USD (95,8) |
| Fable | 1,598 USD | 0,108 à 0,173 USD (0,341) | 1,2 à 1,9 USD (3,8) | 10,8 à 17,3 USD (34,1) | 21,6 à 34,5 USD (68,1) |
| **les trois** | — | — | **3,2 à 5,1 USD (10,0)** | **28,9 à 46,2 USD (91,2)** | **57,8 à 92,4 USD (182,4)** |

Lecture : mesurer un collège à cinq lignées sur les 100 témoins, bloc A seul, ajouterait de l'ordre de 30 à 45 USD à la base ; avec une répétition par lignée, de l'ordre de 60 à 90 USD. Carbon porte plus de la moitié de la somme.

**Pourquoi ces chiffres valent peu.**
- Le proposeur de Carbon a coûté 4,27 fois son devis à la course v9, celui de Fable 2,52 fois, celui d'Astra 0,68 fois. Je ne sais pas pourquoi (longueur des réponses, réflexion facturée). Rien ne dit que ce comportement se retrouve sur une tâche de juge, courte.
- Le rapport juge sur proposeur n'est mesuré que sur deux lignées, et il varie de 0,068 à 0,108.
- Le nombre de témoins utile à cinq juges n'est pas 100 par hypothèse : c'est le banc scripté à cinq juges de l'étage 1 qui le dira.

Ordre recommandé : l'étage 1 d'abord (il rend le nombre de témoins à cinq juges) ; puis, si la note de conception de GO-2026-11-19-65 retient le collège, l'essai court par lignée sur son propre devis ; puis seulement un devis de mesure, sur coûts réels.

## 7. Ce qui est scellé avant la dépense

1. Le préenregistrement, contre-lu par le modèle O, scellé par la mère, avec le commit du code.
2. Le rapport de l'étage 1 et son verdict : l'étage 2 ne part que sur un « oui » de l'étage 1 à 100 témoins ; sinon ce devis est refait à la taille voulue et retourne à Lazar.
3. L'additif de portée, s'il y a lieu (comparaisons d'agrégations déclarées descriptives).
4. La banque des 100 témoins, son journal de construction (la vérité), son partage en deux moitiés, le rapport de vérification du contre-lecteur, le rapport d'audit du générateur et le rapport de la garde de recouvrement.
5. Le programme de l'étage 2, ses essais des gardes (cas sain et artefact), la configuration des juges et l'empreinte de la consigne servie.
6. La ligne de GO de la mère, au montant du plafond.

## 8. Réserves

- Le rapport de coût témoin sur carte (0,73) vient de 33 appels où l'aiguilleur est mêlé aux juges.
- Le juge Opus a coûté 1,97 fois son devis à la course v9 ; je ne sais pas pourquoi. Le pire cas reprend ce facteur comme marge de prudence ; rien ne dit qu'il borne.
- Les répétitions à l'identique peuvent être servies moins cher par un cache du fournisseur ; je n'en tiens pas compte. Le préenregistrement traite ce cache comme un risque pour la mesure (garde « réponses identiques à l'octet »), pas comme une économie.
- Ce devis ne dit rien de la valeur de la ligne : il chiffre un instrument de mesure. Aucun résultat acheté ici ne fera trancher une carte par un juge.

## Différentiel avec la version 1

| point | version 1 | version 2 | source |
|---|---|---|---|
| montants de la base | 16,52 ; 22,49 ; 44,38 USD | inchangés | — |
| en-tête | — | cas haut sous 25 USD, pire cas au-dessus, conséquence de la prédiction P1 (devis à 200 témoins si l'étage 1 dit « non, pas à cette taille ») | consigne de la mère ; contre-lecture, constat 13 |
| « le bloc A tient jusqu'à 2,5 fois le tarif » | 2,5 | **2,4** (plomberie avant, réserve de session) | constat 13 |
| témoins au plus sous 25 USD | 110 | **108** (110 sans la réserve) | constat 13 |
| marge sur le cas haut | 11 % | 11 % nominale, **8,5 % effective** | constat 13 |
| pire cas | « le dépassement du juge Opus » | marge de prudence appliquée à un coût déjà réel | constat 13 |
| longueur moyenne des cartes | constante recopiée | **retirée** du calcul et du texte | constat 13, règle R6 |
| bloc B | par blocs | **entrelacé par témoin** ; table de ce qui reste complet selon le multiple du tarif | constat 14 |
| base réduite | — | § 5 bis : ce qui sortirait si le pire cas devait tenir sous 25 USD | consigne de la mère |
| autres lignées | « non chiffré » | § 6 bis : ce qu'il faut mesurer d'abord, ordre de grandeur sur les coûts de proposeur | consigne de la mère |
| ligne de GO | mot de Lazar seul | GO-2026-11-19-66 cité avec ses conditions | registre |
| calcul | `calcul_devis_ligne_3_v1.py` | `calcul_devis_ligne_3_v2.py`, sortie `calcul-devis-ligne-3-v2.json` | règle R12 |
