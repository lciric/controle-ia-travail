# Contre-lecture du diagnostic de l'arrêt « contrôle carte-processeur » de B bis (T0.7) — v1

- **Auteur** : contre-lecteur neuf (lettre de modèle C), n'ayant écrit ni le texte, ni le code de B bis, ni le diagnostic.
- **Heures (UTC, `date -u`)** : 2026-11-16, de 22:45:12 à 22:55 environ ; rejeux de 22:46:44 à 22:50:50.
- **Objet** : `rapport-diagnostic-carte-processeur-v1.md` (`1fefa0a92020197f07b2356fe52e382eb8e2abc4d5e73052b77ddb9b0845e223`,
  empreinte recalculée, égale) et ses pièces (les treize compagnons `.sha256` du dossier se vérifient : treize OK).
- **Statut** : processeur seulement, données fabriquées seulement ; aucune machine, aucun appel au loueur, aucune dépense ;
  aucun fichier existant modifié ; rien committé.

## 1. Verdict : `diagnostic_tenu`, avec cinq réserves à porter dans le second addendum

La cause proposée (amplification des écarts d'arrondi par l'apprentissage de la sonde linéaire au maximum sur 300 époques) est
**plus solide que le rapport ne le dit, mais sa condition est plus large que celle qu'il écrit** ; la correction reproduit le
défaut et le corrige à l'identique au rejeu ; l'écart au texte scellé est bien un écart à déclarer, mais **sa liste est
incomplète** ; rien de 7a ni de 7b n'a été lu, aucune trace lue ne porte de score.

## 2. Point (1) : la cause explique-t-elle 1,004 sur les vraies entrées et 1,95·10⁻⁸ en répétition ?

**Oui, et mieux que prévu — mais pas pour la raison que le rapport restreint.**

1. **Chaîne relue** (commit `31fa8ac6`, empreintes recalculées égales à celles du rapport : `validation_imbriquee_v3.py`
   `71bffa5b…`, `apprentissage_carte_v1.py` `4b98fcb9…`, `familles.py` `6758b651…`, `validation_imbriquee_v1.py` `1ffb6e4d…`,
   `lecture_v2.py` `154795f4…`) : la sonde de la carte (`LotCarte` + `entrainer`) et la référence (`familles.entrainer`) partent de
   w = 0, b = 0, mêmes pertes (entropie croisée moyenne + l2·‖w‖²), même Adam, même ordre des paramètres [w, b], mêmes actions
   (`res["sequences_app"]`, `res["y_app"]` reçus de `apprendre_recette`, l. 250 à 260), mêmes fonctions de score (`ac.scores`).
   Je ne trouve **aucune erreur de chaîne**. Seules différences : moyenne et écart type par torch (carte) contre numpy
   (référence), et l'ordre des sommes sur la carte. Le rapport dit vrai là-dessus.
2. **Arrêt de la course** : relu sur `arret-marche-bbis.json` (`b116bd0d…`, recalculé) : arrêt à « lineaire à 300 époques :
   écart relatif 1.004e+00 », `scores_ecrits` faux ; la linéaire passe avant l'attention dans `ORDRE`, donc l'attention n'a pas
   été jouée : le rapport ne peut rien dire de l'attention sur la course, et ne le prétend pas.
3. **1,004 est un écart d'ordre 1 entre deux sondes réellement différentes** (plancher 1 au dénominateur de `ecart_relatif`).
   L'amplification peut le produire : j'ai **rejoué à l'identique** les 16 essais du rapport (§ 3) et **monté un essai
   indépendant** (autre générateur de données, autres graines, aucun code du rapport importé ; pièces
   `contre-lecture-essai-independant-v1.py` `0b687970…`, `-suite.py` `5522d602…`, sorties `…sortie-essai-independant-v1.txt`
   `ff5a6730…`). Même méthode que le rapport : `familles.entrainer` sur les mêmes actions, ordre des sommes changé par
   permutation des actions ; 480 actions, 192 de contrôle, largeur 768, 30 à 90 jetons, demi-précision, l2 = 10⁻³, 300 époques.
   Écart du contrôle, 3 époques puis 300 époques :

   | jeu | 3 époques | 300 époques | aires (pile 1 / pile 2) |
   |---|---|---|---|
   | gaussien isotrope | 3,3·10⁻¹¹ | 1,4·10⁻¹¹ | 0,473 / 0,473 |
   | résiduel (moyenne forte), sans copies, 3 graines | 5·10⁻¹¹ à 6·10⁻¹² | 4·10⁻¹¹ à 1,5·10⁻¹² | égales |
   | **anisotrope (rang 8), sans aucune quasi-copie, signal faible, 5 graines** | 4·10⁻¹³ à 4·10⁻¹² | **7·10⁻⁶ ; 0,59 ; 1,01 ; 1,34 ; 2,25** | **0,464 / 0,494 ; 0,472 / 0,502 ; 0,666 / 0,650 ; 0,505 / 0,512** |
   | **anisotrope, sans copies, sans signal, 2 graines** | 2·10⁻¹² | **2·10⁻⁶ ; 4,51** | **0,591 / 0,544** |
   | résiduel, 40 % de quasi-copies (10⁻³ ; 10⁻¹) | 3·10⁻¹² ; 9·10⁻¹² | 2·10⁻⁹ ; 5·10⁻⁷ | égales |
   | anisotrope, 40 % de quasi-copies (10⁻²) | 4·10⁻¹² | 9·10⁻⁶ | égales |

   Lecture : **l'amplification d'ordre 1 existe sans quasi-copies** (anisotrope, sonde qui n'ajuste pas : perte finale 0,53 à
   0,60), à 3 époques toujours ≤ 4·10⁻¹², et, dans ce régime, **les aires lues des deux piles diffèrent de 0,007 à 0,047**. Les
   quasi-copies du rapport ne sont donc ni nécessaires ni suffisantes : dans mon jeu, mes quasi-copies (40 %) **n'ont pas** fait
   diverger. Valeurs ≈ 1,0 (1,010 ; 1,004 du rapport) sont dans la plage.
4. **1,95·10⁻⁸ en répétition** : jetons N(0, I) indépendants, la sonde ajuste (perte 0,1 à 0,5), régime stable de mes essais
   (isotrope : 10⁻¹¹) ; l'écart de 2·10⁻⁸ mesuré sur la carte est supérieur de deux ordres à l'émulation processeur du rapport
   (1·10⁻¹⁰, largeur 1 024) : écart d'échelle (4 096 dimensions, 143 000 jetons, réductions de carte) non joué ici ; ce n'est pas
   contradictoire (le mécanisme grandit avec la taille) mais **non démontré**. Valeur 1,954·10⁻⁸ relue dans l'addendum scellé
   (§ 5, point 5) ; le fichier `repetition-carte.json` n'est pas sur la branche permise : non ouvert.

**Corrections de caractérisation à demander** (réserves R-A et R-B, § 7) : (a) le rapport écrit, § 1 et § 4, que sans quasi-copies
« tout reste sous 10⁻¹⁰ » et que la linéaire est « stable, comme la v3 l'avait supposé » : **faux en général** (anisotropie de bas
rang, sonde qui n'ajuste pas) ; (b) la présence de quasi-copies dans les vraies activations n'est donc **pas** la question à
vérifier ; le mécanisme est la sensibilité de la fin de l'apprentissage aux arrondis dans les régimes mal ajustés. Cela **renforce**
la cause (elle n'a plus besoin d'une forme de données supposée) et renforce la **réserve scientifique** (les aires lues des
linéaires dépendent de la pile, de plusieurs centièmes, donc aussi le choix du réglage à 0,005 d'ex aequo).

Confiance : la cause « amplification d'arrondi, sans erreur de chaîne » passe, à mon avis, de 0,6 à environ 0,75 ; l'hypothèse
résiduelle (erreur de chaîne propre aux vraies données) reste non exclue, et la v4 la sépare correctement (§ 3).

## 3. Point (2) : les essais reproduisent-ils le défaut et le corrigent-ils ? (rejoués)

Commande du rapport, rejouée telle quelle sur le processeur (Python du dépôt, torch 2.14.1, 4 fils), sortie
`contre-lecture-rejeu-essais-v4-v1.txt` (`3ac9ad17…`) : **16 passés en 74,8 s**. Chiffres **identiques** à `sortie-essai-controle-v4-v1.txt`
(`7a47be47…`, recalculée) : v3 arrête à 6,247 ; v4 passe à 3,328·10⁻¹¹ (linéaire) et 7,673·10⁻⁹ (attention) à 3 époques,
déterminisme vrai, information 6,247 ; artefacts à 3 époques tous arrêtés (1,08·10⁻², 1,05·10⁻², 0,45, 1,06, 0,62, 0,82, 0,99).

Lecture critique :
- **Le défaut reproduit est celui que la construction fabrique** : jeu de quasi-copies choisi pour diverger, « carte émulée »
  = permutation des actions. L'essai 1 montre que la v3 *peut* arrêter sans erreur de chaîne ; il ne montre pas que la course l'a
  fait pour cette raison. Mon essai indépendant (§ 2) dit la même chose avec d'autres données : bon accord, preuve de possibilité,
  non de fait. Le rapport le dit (confiance 0,6) ; je le répète.
- **La correction corrige** ce qu'elle prétend : le contrôle à 3 époques voit tous les artefacts d'entrée (poids altérés de 1 %,
  l2 ×100, une étiquette inversée, autre graine, autres données) avec 2 à 5 ordres de marge ; il est insensible à l'ordre des
  sommes (≤ 4·10⁻¹² chez moi, ≤ 1,2·10⁻¹⁰ chez eux). Cohérent avec ce que l'addendum scellé a mesuré pour l'attention.
- **Ce que la correction ne voit pas** (déjà dit au rapport pour l'essentiel, § 6, dernier alinéa) : une erreur qui ne commence
  qu'après la troisième époque ; or **l'addendum scellé comptait la linéaire à 300 époques comme l'une des trois couvertures de
  ce cas** (§ 5, point 1 : « seuls l'identité du code de la boucle, la linéaire à 300 époques et le déterminisme la couvrent »).
  La v4 retire cette couverture : le rapport doit le dire comme **affaiblissement déclaré** (réserve R-C).
- **Le discriminant proposé** (« un passage à 3 époques avec information > 10⁻⁴ confirmerait l'amplification ») est juste dans
  le sens de la confirmation, mais ne **réfute** pas une erreur de chaîne tardive : un passage à 3 époques avec information 6 ne dit
  pas que le code de la carte est juste après la troisième époque. À écrire tel quel.
- Le code `validation_imbriquee_v4.py` (`ba127aa0…`, recalculée) fait ce que dit son en-tête ; le tirage du couple, les graines
  (mêmes clés), la tolérance, l'ordre trié sont ceux de la v3 ; `jouer` est recopié (la lecture du couple, des 256 actions et du lot
  est identique, vérifiée ligne à ligne). Reste non écrit : `marche_v4`, lanceur, amorce, `lecture_v3` (dit par le rapport).

## 4. Point (3) : l'écart au texte scellé est-il nommé ?

Le rapport conclut justement que ce n'est **pas** une « correction du code sous ce texte » : le fragment EC-1 de l'addendum
(`f00eda8a…`, recalculé ; texte scellé `0ae6210f…`, recalculé) gèle « la linéaire à 300 époques » et la liste d'arrêt (EC-4, l. 150)
et les épreuves (EC-8, l. 218) la répètent ; la ligne 186 du texte scellé ne permet qu'une « correction du code » avec « relance sous
ce texte ». Il faut un second addendum, contre-lu et scellé avant `CODE-BBIS` remplacée. **D'accord.**

Fragments **nommés par le rapport** : EC-1, EC-4, EC-8, EC-5, EC-7, EC-2, EC-3. Je vérifie : ils sont exacts. L'« Inchangé »
(hypothèse, prédiction, métrique, seuils, tolérance 10⁻⁴, 256 actions, tirage, graines, grille, 300 époques et pas des sondes lues,
plancher, nul, débit, budget) est exact aussi, d'après le code et l'addendum.

**Fragments scellés touchés mais non nommés** (réserve R-C) :
- addendum **§ 5, point 1** (« la linéaire à 300 époques … couvrent ») : à réécrire ;
- addendum **§ 5, point 4** : « si le réglage retenu du couple tiré est linéaire, sa sonde lue est comparée comme au texte scellé » :
  **faux avec la v4** (la sonde lue de 300 époques n'est plus comparée à rien ; seul son déterminisme l'est) : c'est un
  **affaiblissement du contrôle de la sonde lue** à déclarer comme celui de l'attention ;
- addendum **§ 3** (« ce qui ne change pas ») : le coût « une linéaire de 300 époques, une attention de 3 époques et deux de 300 »
  (l. 241) change (une linéaire de 3 et deux de 300 par famille) ; et « seul le contrôle à la marche du point 5 change » reste vrai ;
- addendum **§ 5, point 5** (mesure de la quatrième passe : écart de la linéaire à 300 époques 1,954·10⁻⁸ présenté comme preuve de
  bon fonctionnement) : à requalifier : à 4 096 dimensions sur bruit isotrope seulement (la phrase « ce que la passe ne prouve pas » le
  dit en partie).
Rien d'autre ne change d'état, d'issue ou de seuil. Le rapport a raison de dire qu'**aucune issue** n'est modifiée.

**Substance, pas seulement texte** (réserve R-D, à porter à Lazar, non à trancher ici) : si le régime de l'apprentissage des
sondes linéaires lues est celui de mes jeux anisotropes, l'aire lue d'une linéaire est « celle d'**une** sonde parmi celles que
rendraient d'autres arrondis » (écarts de 0,007 à 0,047 chez moi, 0,02 à 0,04 chez le rapport), comme l'addendum le dit déjà de
l'attention. R-PILE étendue à la linéaire est nécessaire ; mais l'ex aequo (0,005) et donc la **famille, la couche et la
régularisation retenues** peuvent changer d'une pile à l'autre : le texte de la réserve ne suffit peut-être pas à dire ce que
l'étape lit. Question à poser à Lazar avec le second addendum : accepter la réserve seule, ou ajouter une mesure de la dispersion
des aires entre piles dans le champ de lecture (information, sans issue).

## 5. Point (4) : rien de 7a ni de 7b lu, aucun score lu

- Lu sur `donnees/t07-etape-b-bis-v1` (`8ec901fa`), par `git show` après `git fetch` à refspec, sans clone : `arret-marche-bbis.json`
  (`b116bd0d…`), `manifeste.json` (`0a7693cc…`) et, dans `traces/bbis-t07-v1/`, `journal-bbis.txt` (`262d5789…`), `marche.txt` (`7c38e88d…`),
  `marche.err` (`ef846dbd…`), `essais.txt` (`0b608a67…`), `modele.txt` (lu par recherche de mots-clés seulement). **Aucune ne porte
  de score** : l'arrêt dit `scores_ecrits` faux ; une recherche de « aire, auc, score, écart » ne renvoie, hors `écart relatif 1.004`
  et la phrase « aucun score », rien. Empreintes du rapport confirmées pour les quatre fichiers de trace et les deux premiers.
- **Jamais ouverts** : `relecture-bbis.json` (je n'ai même pas lu ses clés ; seule sa présence a paru au listage des noms),
  toute donnée, activation ou sortie de 7a ou de 7b, toute sortie de l'étape B de T0.7, `repetition-carte.json` (autre branche, non permise).
  Aucune valeur de clé ; ni `env` ni `printenv`. Rien d'autre sur la machine distante.
- **Le dossier « neuf »** : `essai-sensibilite-lineaire-v1.py` (`679f1808…`) existait avant moi (date 21:52:00Z), je n'y ai pas touché,
  empreinte inchangée ; le rapport le signale. Aucun `__pycache__` laissé (`PYTHONDONTWRITEBYTECODE`).
- Mes données sont **fabriquées par moi** (générateur à graines fixes dans le script) ; aucun identifiant de modèle dans mes fichiers.

## 6. Autres remarques (mineures)

- M1 : le rapport dit « Python 3.13.18 » et la course « Python 3.11.18 » : les versions diffèrent entre diagnostic et course
  (même torch et numpy) ; sans effet sur le raisonnement mais à garder dans la réserve de pile.
- M2 : « neuf autres jeux d'un balayage préalable, sorties non gardées » : le rapport le déclare ; je n'ai pu le rejouer, et mon
  essai contredit sa conclusion générale (« sans quasi-copies, stable ») : le balayage perdu ne doit plus être cité comme preuve.
- M3 : la recommandation (a) est la bonne (je ne vois pas d'option moins coûteuse sans le même arrêt) ; option (c) à écarter.
  Une variante moins chère n'existe pas : le contrôle vient à la fin, toute relance recoûte l'apprentissage (3,6 h à la course arrêtée).
- M4 : prévoir dans le second addendum l'**épreuve** de la v4 sur un jeu du régime anisotrope (cas sain qui passe malgré 300
  époques divergentes) à côté de celui du rapport ; mon script en donne un exemple (pièce ci-dessus).

## 7. Réserves à porter (liste pour la mère)

- **R-A** : corriger la caractérisation (§ 1, § 4 du rapport) : l'amplification apparaît aussi **sans quasi-copies**
  (anisotropie de bas rang, sonde qui n'ajuste pas) ; retirer « sans quasi-copies tout reste sous 10⁻¹⁰ » ; la question « y a-t-il des
  quasi-copies dans les vraies données ? » n'est pas la bonne.
- **R-B** : écrire le discriminant à double sens (pas de passage à 3 époques = erreur de chaîne au sens large ; passage avec
  information > 10⁻⁴ = amplification **ou** erreur de chaîne tardive indiscernables).
- **R-C** : étendre la liste des fragments scellés touchés : § 5 points 1, 4, 5 et § 3 (coût) de l'addendum ; déclarer comme
  affaiblissement la perte de la comparaison de la sonde lue de 300 époques (linéaire) à une référence, et la perte de la
  couverture « linéaire à 300 » du point 1.
- **R-D** : question de substance à Lazar : réserve R-PILE seule, ou mesure d'information de la dispersion des aires entre piles ;
  l'ex aequo à 0,005 peut dépendre de la pile.
- **R-E** : relancer d'abord, avant le feu, les 16 essais et un essai de régime anisotrope sur une `marche_v4`, une `lecture_v3` et
  les épreuves du second addendum (EC-8 révisé) ; contre-lecture neuve du second addendum (R2).

## 8. Déclaration

Rôle : contre-lecteur neuf, lettre C. Ni auteur du texte, du code de B bis, du diagnostic ni de l'addendum. Heures : de 22:45:12Z à
l'écriture de cette pièce (`date -u`). Calcul : processeur, 4 fils ; rejeu des essais du rapport 74,8 s ; essai indépendant environ
110 s ; aucune machine, aucune dépense. Pièces produites (dossier `diagnostic-carte-processeur-v1`, nouvelles) :
`contre-lecture-essai-independant-v1.py`, `contre-lecture-essai-independant-v1-suite.py`,
`contre-lecture-sortie-essai-independant-v1.txt`, `contre-lecture-rejeu-essais-v4-v1.txt` et ce rapport, scellés (compagnons `.sha256`).
