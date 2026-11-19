# Rapport du rédacteur — ligne 3 des épreuves v9 (votes effectifs des juges croisés, mesurés sur témoins plantés), version 4 du préenregistrement et du devis — v1

- Auteur : rédacteur neuf, modèle F. Je n'ai écrit aucune des versions 1 à 3.
- Heure (`date -u`) : 2026-11-19, de 15:06 à 15:24. Processeur seul ; aucun appel de modèle, aucune dépense, aucun tirage, aucune écriture dans le dépôt, aucun commit.
- Mandat : `mandat-redacteur-ligne-3-v4-v1.md`, `8821c6716ef43e409576b53fbb2e701a4489de06e0f98855a3d882434035edac`, vérifié avant de commencer.
- Pièces de travail, classe C. Empreintes des fichiers rendus : dans le compte rendu remis à la session (ce rapport ne peut pas porter la sienne).

## Fichiers rendus (bloc-notes seulement)

- `preenregistrement-ligne-3-votes-effectifs-juges-v4.md` : la version 4, obtenue par 33 morceaux de différentiel sur la version 3 (`9b62fd5a…`).
- `devis-ligne-3-etage-payant-v4.md` : aucun montant de la base changé.
- `calcul_devis_ligne_3_v3.py` et sa sortie `calcul-devis-ligne-3-v3.json` : le calcul de la version 2 plus deux clés (compteur d'arrêt ; borne dure d'un essai court). Joué deux fois, sorties égales à l'octet ; toutes les valeurs de la sortie de la version 2 égales, clé par clé, sauf « version ».
- `calcul_predictions_ligne_3_v1.py` et sa sortie `calcul-predictions-ligne-3-v1.json` : **pièce non demandée par le mandat**, ajoutée pour que les chiffres neufs du préenregistrement (double rendu, monde de puissance) aient un chemin et une empreinte (règle R6). Calcul exact, sans tirage, bibliothèque standard seule.
- `outils/ecrire.py`, `outils/remplacer.py` : deux outils d'écriture du bloc-notes, à ne pas verser.

## Ce que j'ai changé, constat par constat

**A — renvoi de GO-2026-11-19-73.** Appliqué. Renvoi à main, commit `7dcd6a44c777f3aea55b5c68ef8547f9f83438fa`, `registres/go.md` `72e52540c4b25997d0aa6057ea880bdc765e0cd09c5650b65a0b084da174f558`, relu par moi (lignes -55 à -74) ; la tête de main à l'écriture (`c0fca6fe…`) porte la même empreinte. « Je ne l'ai pas relue sur main » retiré. Même correction dans le devis (ligne GO-2026-11-19-66).

**B — banc du double rendu.** Appliqué, avec un choix de conception à contre-lire.
- Les deux sens sont joués, à grille égale, sur les mêmes tirages : le suiveur séduisant (« notable » si le trait est présent) et le suiveur repoussant (le sens des versions 1 à 3). **Le suiveur séduisant décide** : c'est la lettre de la carte (« décide sur ce trait ») dans le sens de sa réfutation (« acceptation des faux témoins confondus »). Le suiveur repoussant est rapporté sans mot.
- Calcul exact : chez le suiveur séduisant, clause (i) « réfuté » à δ = 0 et 0,2, « tient » à δ = 0,5 ; clause (iii) « tient » à δ = 0,2 et 0,5 ; mot de la carte « réfuté », « réfuté », « tient ». Les deux mots sont atteignables. Le calcul à la main du vérificateur est retrouvé à l'identique.
- **Ce que j'ai trouvé en plus, et dit dans le texte.** Dans ce sens, le lecteur de surface rejette tous les vrais (seuls les faux portent le trait) : le « tient » de δ = 0,5 est obtenu entre deux collèges qui rejettent 80 % des vrais. J'ai donc ajouté un troisième lecteur, rapporté sans mot : séduit par le trait, juge du fond quand il manque. Chez lui la clause (i) serait réfutée partout. Le « tient » prédit tient donc à la loi du lecteur, que nous choisissons (réserve 11).
- Ce que je n'ai pas joué : un monde où les vrais portent aussi le marqueur (les « leurres … imitant les vraies » de `fefca0bd94064`). Raison : ce n'est pas la lettre de `fcfa3d98b90f8` (« les faux témoins reçoivent … un trait de surface distinct »). Par raisonnement, non par calcul, la clause (i) y serait poussée vers « réfuté » par les vrais rejetés. C'est dit à la réserve 11.
- P5 n'est pas récrite ; elle est lue sur le suiveur séduisant. P5 ter est gardée pour le suiveur repoussant. P5 quater est neuve.
- À δ = 0, « réfuté » suit de l'arithmétique (deux juges lus deux fois contre quatre à l'unanimité), non du confondant : gardé à la lettre de la carte, rapporté avec cette mention.
- Les tailles de banque de ce bras n'étaient dites dans aucune version : fixées à celles de la grille.

**C — cellule de puissance et règle de plantation.** Appliqué, écrit au texte (pas de renvoi au code). Avec deux juges égaux et symétriques, aucun écart n'existe (§ 0) : il faut un monde à part. Monde de puissance : deux juges sévères de même profil, taux moyen 0,20, dissymétrie résolue par bissection pour que l'écart vrai (bras de comparaison moins « au moins un ») vaille 0,10. La puissance qui décide est la plus basse sur les cellules faisables des lois 1 et 3. Fait à connaître : à ce taux, un écart de 0,10 n'est faisable que dans peu de cellules (contre un juge seul : ρ ≤ 0,15), et 0,15 est infaisable contre un juge seul et contre le juge répété. Une comparaison sans cellule faisable vaut « puissance insuffisante ». Ma prédiction : les comparaisons d'agrégations seront déclarées descriptives avant la dépense.

**D — forme.** Les quatre points appliqués : 0,050 ; vrais rejetés aux trois valeurs de δ ; s = 0 : clause (i) non lue, mot « sans prise » ; part d'abstentions par vote (0,1275), part par témoin (0,239) rapportée à côté.

## Les trois conditions du plafond (R-3875)

Écrites au préenregistrement, section « Plafond : arrêt dur par compteur » (dans « Liste d'arrêt »), et au devis, § 5.
- (i) Arrêt dur par compteur : journal à ajout seul, engagement de 0,60 USD écrit avant chaque envoi, aucun envoi si cumul compté plus engagement dépasse 25 USD, arrêt sans repli ni suite. Deux gardes, cas sain et artefacts (la liste passe à dix-neuf gardes).
- (ii) Issue du pire cas : arrêt au plafond, 18 témoins complets, « non concluant par manque de témoins », jamais un « non » ; nommé au rang 1 de la table de l'étage 2.
- (iii) Tout envoi refusé, en erreur, coupé ou sans coût lisible est compté 0,60 USD ; rejeu unique, compté. Chiffres du calcul : 41 envois si tout est refusé ; la base supporte 3 envois refusés au cas haut, 13 à l'estimation.
- Le devis se lit sur le cas haut (22,49 USD ; 23,09 avec réserve) : écrit en tête du devis et à Q5.
- Limite dite : le compteur ne borne la dépense que si le service tient le plafond de session de 0,60 USD ; je n'ai pas relu ce code ; un coût relevé au-dessus arrête le programme.

## Décisions de Lazar portées, consignes de la mère

- `fefca0bd94064` (GO-2026-11-19-73, option (a)) et `fa38f9faa24e0` (GO-2026-11-19-63, point 1) : lues sous décisions prises. Aucun marquage « en attente » ne reste (la version 3 n'en portait déjà plus ; les seules mentions sont historiques, dans les tables des versions). **La mesure se sépare de la décision pour les deux cartes : aucun retour à Lazar à ce titre.**
- R-3854 et R-3864 : ce qui manque pour chiffrer d'autres lignées est dit en une phrase (un coût de juge mesuré par lignée) ; borne dure d'un essai court 6,60 USD par lignée ; chaque essai est une dépense sur devis et ligne ; témoin « un juge seul répété k fois, à coût apparié » gardé ; lecture par colonne écrite (référence = vérité plantée ; auteur fixe ; une seule colonne, « à domicile » pour le juge Opus ; ce qu'il faudrait pour une seconde colonne) ; ordre écrit (texte vérifié, scellement, code de l'étage 1 et contre-lecture, additif de code, étage 1, taille rendue à la mère avant toute demande ; devis neuf à Lazar si 200 témoins).

## Points de conception que j'ai tranchés (à contre-lire)

1. Le sens qui décide au double rendu, et le troisième lecteur (Q6).
2. Le monde de puissance et la cellule qui décide (Q7).
3. Le compteur : ce qu'il compte, 0,60 USD par envoi refusé, rejeu unique, relance permise sans remise à zéro.
4. L'ordre « scellement avant le code » rend nécessaire un additif de code scellé avant tout tirage (Q8). **À regarder par la mère** : le gabarit de préenregistrement demande un commit du code d'analyse ; l'additif en tient lieu.
5. Q2 (plan d'appels), Q3 (écriture et vérification des témoins), Q4 (pas d'autre lignée à l'étage 2), Q5 (plafond) : tranchées comme la version 3 les proposait par défaut.
6. Garde de recouvrement étendue aux 94 cartes, par un programme qui ne rend que des comptes. **La mère peut refuser** l'ouverture du fichier par un programme ; le texte dit quoi faire dans ce cas.

Je ne sais pas quels étaient les « six points » relevés par la session précédente : ils ne sont écrits nulle part dans ce que j'ai lu. La liste ci-dessus est la mienne.

## Ce que je n'ai pas pu faire, ce qui reste ouvert

- L'empreinte du code de l'organisme (`juges_croises_v53.py`) n'est pas recalculée : son dépôt n'est pas sur ma machine. Toutes les autres empreintes de l'en-tête sont recalculées.
- Je n'ai lu aucun travail cité par la note de littérature ; la « lecture par colonne » est sa lecture.
- Je n'ai lu que trois cartes ; les quatre autres nommées à l'en-tête l'ont été par le rédacteur précédent.
- Les intervalles des mots du double rendu ne sont pas calculés (ils demandent le banc) ; à δ = 0,5 l'écart de la clause (iii) est à 0,007 de sa marge.
- Écart de forme au mandat de lancement : il demandait l'outil d'écriture de fichiers ; ma consigne de session impose le terminal. J'ai écrit par le terminal, **sans heredoc**, avec deux petits outils. Aucun outil n'a refusé.
- La version 4 change des règles de lecture du banc scripté (double rendu, portée) : le contre-lecteur doit la vérifier sur son différentiel avant scellement.

## À dire à Lazar (information, pas une décision)

Au pire cas, la ligne peut dépenser près de 25 USD et rendre « non concluant par manque de témoins ». C'est écrit d'avance et jamais lu comme un « non ».

## Décisions pour Lazar

**1. Essais courts d'autres lignées comme juges (Astra, Carbon, Fable).**
- Décision, en une phrase : quand faire écrire les devis des essais courts (onze appels par lignée) qui mesurent le coût de juge de chaque lignée.
- Enjeu : GO-2026-11-19-65 et -68 veulent un collège d'un juge par modèle « mesuré avant adoption » ; sans coût de juge mesuré, aucun devis de cette mesure n'est possible. Chaque essai est une dépense (borne dure 6,60 USD par lignée, 19,80 USD pour trois ; ordre de grandeur attendu 3 à 5 USD pour les trois).
- Option (a) : après la lecture de l'étage 1 de la ligne 3. Avantage : l'étage 1 dit d'abord combien de témoins demande une mesure à cinq juges ; on ne dépense que si elle est faisable. Inconvénient : un à deux jours de plus.
- Option (b) : tout de suite, en parallèle. Avantage : le coût de juge est connu plus tôt, utile à la note sur le juge. Inconvénient : dépense et charge de rédaction avant de savoir si la mesure à cinq est jouable.
- Option (c) : pas d'essai. Avantage : aucune dépense. Inconvénient : le collège par modèle reste non mesurable.
- Recommandation : (a), confiance 0,6.
- Défaut sous 48 heures : (a).

**2. Une seconde colonne d'auteur, pour mesurer la préférence d'un juge pour sa lignée.**
- Décision, en une phrase : ouvrir ou non une banque de témoins sœur, dont les fragments sont écrits par une autre lignée que celle du rédacteur.
- Enjeu : la banque de la ligne 3 n'a qu'un auteur, de la famille du juge Opus. L'écart d'erreur entre les deux juges y mêle l'adresse du juge et sa proximité avec l'auteur ; la préférence pour sa lignée, qui est la question de GO-2026-11-19-65, ne s'y lit pas.
- Option (a) : ne pas l'ouvrir dans la ligne 3 ; la question va à la note de conception du juge ; la ligne 3 rapporte sa colonne avec la réserve. Avantage : aucune dépense ni délai, la ligne garde son objet. Inconvénient : la préférence pour soi reste non mesurée.
- Option (b) : l'ouvrir comme second temps de la ligne 3, sur devis. Avantage : mesure directe, sur vérité plantée, lue par colonne. Inconvénient : écriture des fragments par un modèle (non chiffrée), 9,86 à 22,49 USD de jugement au cas haut par colonne, une conception et un préenregistrement de plus.
- Recommandation : (a), confiance 0,65.
- Défaut sous 48 heures : (a).
