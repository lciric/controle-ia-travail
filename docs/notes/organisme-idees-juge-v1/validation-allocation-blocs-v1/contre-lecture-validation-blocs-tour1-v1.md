# Contre-lecture 1 du préenregistrement de la validation propre de l'allocation par blocs (brouillon 1) — v1

- **Lecteur** : sous-agent neuf, modèle C (R2) ; il n'a écrit ni le brouillon, ni le préenregistrement de l'idée 1.2, ni ses addendums, ni son verdict. Texte du modèle A. Début 2026-11-17 01:19:54Z (`date -u`) ; fin de la rédaction : heure du compagnon `.sha256` de ce rapport. Première contre-lecture, lecture entière.
- **Pièce lue** : `docs/notes/organisme-idees-juge-v1/validation-allocation-blocs-v1/prereg-validation-allocation-blocs-v1-brouillon1.md` (`95f34a756c61b1f73df88cfa99350f9ffb741ad872a6afea90406e1f1acd6011`, compagnon vérifié conforme à 01:20Z), 388 lignes, lue en entier.
- **Pièces de référence lues** (empreintes recalculées à 01:19Z, égales à celles que le brouillon cite) : verdict de l'idée 1.2, **[V]**, `3b08f061d82687314efb72e595d92cb7cb3ac639d08f05e181e69070b1362b63`, en entier ; préenregistrement de l'idée 1.2, **[T]**, `bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e`, en entier ; addendum d'empreintes **[AE]** `1b96cf065cef40ed9e452611b107d9f40f598091c8a591f2397bf58e7c92beee`, en entier ; addendum de relance **[AR]** `632a897944c1c36e8c7b3e2b078e1a4e1ed8bd0489379f10391c191404ed4f55`, jusqu'au début de son § 5 (le reste, hors sujet ici, non lu) ; gabarit et validateur (`prereg.problemes`).
- **Recalculs de contrôle** (sans donnée, à la main ou par un court programme jeté, aucun fichier du dépôt touché) : seuils binomiaux de la lecture (1) pour 6, 7 et 8 bras sur 500 générations ; empreintes des onze documents et PDF que le brouillon cite en « empreintes recalculées » (toutes égales) ; totaux de composition des cinq familles ; échelle du coût.
- **Jamais ouvert** : aucun fichier sous `diag/`, `runs/`, `donnees/` ; ni le run invalide ni sa copie ; aucune branche `calcul/*` ou `donnees/*` ; rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras d'attaque, du pilote MR-2 ; aucun secret ; aucune variable d'environnement affichée ; aucun appel réseau, aucune machine ; aucun commit ; aucune pièce modifiée.

## Verdict

**« corrections »**. La conception tient : l'idée (valider sur données et banc neufs, en attaquant les réserves de [V] une à une) est la bonne, les chiffres repris de [V] sont exacts, les règles des bras, les seuils et le code de rejeu sont bien ceux de [T], et rien n'est lu des sorties de l'idée 1.2. Mais cinq défauts **majeurs** (ci-dessous M1 à M5) empêchent le scellement tel quel : une contradiction d'ordre (code, essai à blanc, scellement), une lecture de validité neuve qui n'a, sur le banc réel, aucun pouvoir de voir ce qu'elle prétend voir, un trou de la table de lecture (le « hors de la zone utile » masque un tort constaté), des compositions de cartes non gelées pour trois familles, une annexe indispensable au serrage non écrite. Onze remarques **mineures** (m1 à m11, dont deux facultatives, m5 et m8) complètent. Aucune ne met la conception en cause : pas de « à refaire ».

Le validateur du dépôt rend un seul manque, attendu à ce stade (« contre-lecture 1 sans ses deux empreintes ») ; je l'ai rejoué, c'est bien le seul.

## 1. Les quatre vérifications demandées

**(1) R1 complet.** Hypothèse, prédictions chiffrées avec signe (P1 à P14), métrique, seuil, plan, critères gelés, liste d'arrêt : toutes les sections sont là et nourries. Défauts : M1 (ordre), M3 (trou de la table), M4 (compositions), M5 (annexe), m6 (grille de sensibilité qui peut ne rien dire). Prédictions sans seuil de réfutation pour deux familles : m11.

**(2) R3 et R4.** R3 tenu : chaque issue est écrite (« Ce que serait chaque issue »), les familles sont choisies pour attaquer les réserves (porteuse unique, dense, vide), non pour obtenir un signe ; le choix des doses après lecture du verdict est déclaré (m10 demande de le chiffrer). R4 tenu et même renforcé (zéro perte par porteuse en « porteuse unique » = trop propre ; égalité à la deuxième décimale avec [V] = trop propre ; « vide » sans aucune fausse promotion = tout négatif) ; la lecture est symétrique. Réserve : la lecture neuve (5) est présentée comme fermant la réserve 3 de [V] alors qu'elle n'a pas de pouvoir sur le banc réel (M2) ; sans correction, le texte afficherait une fermeture de réserve qui n'en est pas une.

**(3) Fidélité à la conception d'origine.** Fidèle. Vérifié ligne à ligne contre [T] : mêmes bras (F, F-arrêt, A, P, P′, F125, G), mêmes règles (blocs de 25, arrêt bas log W < log(1/20) après 50 tirages, arrêt haut m/α, plafond 800, budget 4 800), mêmes seuils de validité (13 et 39 sur 500 : **recalculés**, 6 bras donnent 13 et 38, 7 bras 13 et 39, 8 bras 13 et 39 ; le brouillon dit juste que huit bras donneraient les mêmes bornes), mêmes lectures (1) à (4), mêmes clés de graines avec familles 10 à 14. Les renvois de lignes de [T] (l. 211-212, 316-318, 451-456, 462-466, 495-500, 506-515, 534-538, 542-544, 665-672) sont tous exacts. Les chiffres tirés de [V] sont tous exacts (86,1 % contre 41,3 % ; +0,448 [+0,413 ; +0,484] ; fausses promotions 0,0027 contre 0,0013, borne haute +0,004 ; +0,353 ; +0,281 ; économie 0,568 [0,564 ; 0,572] ; 335,6 ; +0,619 contre +0,277 ; moyennes de valeurs e de 0,05 à 0,09 ; 56 cartes) ; trois précisions de dénominateur ou de paragraphe sont à reporter (m2, m3). Les totaux de composition font bien 24 cartes dans chacune des cinq familles (8+8+2+2+2+2 ; 6+6+4+6+2 ; 1+7+5+8+3 ; 12+4+3+4+1 ; 0+6+8+8+2) et 3 000 générations, 72 000 cartes. Le nœud d'adoption de Lazar est correctement laissé intact (rien n'est adopté, la preuve contre-lue lève la condition « dénominateur fixe » et le dit).

**(4) Coût.** Processeur seul, 0 dollar, aucun devis : cohérent (aucune machine louée, aucun appel de modèle ; crédits : 0 ; hors crédits : 0). L'échelle repose sur les coûts mesurés de [V] : jeu 3,19 h pour 30 000 cartes, donc 3,19 × 72 000 / 30 000 = 7,7 h ; oracle 0,5 h × 2,4 = 1,2 h ; contrôles, essai E1, serrage, sensibilité ≈ 1 h ; total ≈ 9,9 h, 10,9 à 11,4 h avec le juge candidat : « 10 à 12 h » est juste, marge de deux fois sous 24 h. À 500 générations pour deux familles : 6,4 + 1,0 + 1 ≈ 8,4 h, « ≈ 8 h » juste. **Réserve** : le serrage joue ici six règles avec allocation sur 20 000 générations (le jeu synthétique de [AE] n'en jouait qu'une mutation sans allocation, 3 à 4 minutes) ; l'heure prévue pour « contrôles, E1, serrage, sensibilité » est plausible mais non mesurée ; l'essai à blanc doit aussi chronométrer le serrage (inclus dans M1-a par « plus 1 heure de contrôles », à remplacer par la mesure si elle est plus grande).

**(5) Lectures interdites, identifiants de modèle.** Aucun identifiant de modèle dans le brouillon (recherche faite). Le brouillon déclare n'avoir lu des sorties de l'idée 1.2 que les noms de clés de premier niveau, aucune valeur ; je n'ai aucun moyen de le vérifier et n'ai rien ouvert sous `diag/` ni `runs/`. Aucun contenu de 7a, 7b, T0.6, T0.7, B bis, P3-bis, bras d'attaque, pilote MR-2 n'est employé. L'unique emploi de ces noms est la déclaration finale « jamais ouvert », correcte. Garde de chemin du code : trop étroite (m1).

## 2. Défauts majeurs (exigent une correction avant scellement)

**M1. Ordre impossible : le code, l'essai à blanc et le scellement.** L'en-tête dit que le code « s'écrit après la contre-lecture et le scellement de la version qui fera foi » ; l'étape 1 et le Coût disent que l'essai à blanc chronométré (qui exige le code) a lieu « avant le scellement », et que la décision de ramener deux familles à 500 générations se prend « dans la version qui fera foi, avant son scellement (jamais après) ». Les deux ne peuvent pas être vraies ensemble, et la racine des graines est l'empreinte du texte scellé. Correction proposée : l'essai à blanc se joue après le scellement, avant le jeu ; la réduction à 500 est une règle conditionnelle écrite d'avance, sans effet sur les tirages (clés par génération : les 500 premières générations sont les mêmes que les 500 premières des 750), fondée sur la seule durée (R1 et R3 tenus). Couples M1-a et M1-b. (Si la mère tranche Q-2 en faveur de 500 tout de suite, ces deux couples tombent et le texte dit 500.)

**M2. Lecture neuve (5) sans pouvoir sur le banc réel.** Λ est une martingale de moyenne 1, mais, pour une carte sans lien avec le monde (nulles, fausses, copies, membres exacts éloignés), Λ vaut presque toujours une valeur minuscule ; sa moyenne ne vaut 1 que par des événements rarissimes que 500 générations ne voient pas. La moyenne toutes cartes réunies, par bras, reste donc très sous 1 (de l'ordre de la part des cartes proches : 8 voisines et le monde lui-même sur 24), **même si une règle lisait le bloc suivant** : la borne basse « > 1 » ne peut pas être atteinte. Le brouillon le sait en partie (il demande des voisines proches au serrage « pour que la variance reste finie ») mais ne le dit pas pour la lecture sur le banc réel, et il la présente comme fermant la réserve 3 de [V] (hypothèse 4, P12, tableau des réserves, étage 1). Correction : juger la lecture (5) sur la seule sorte « voisines du monde » (sept intervalles, le compte « sept » de l'étage 1 reste vrai), rapporter le reste sans critère, et déclarer son pouvoir en rejouant après le jeu la mutation « bloc suivant » sur le bras A de la famille « nul » (coût négligeable : les 800 issues sont déjà tirées) ; si la borne basse ne dépasse pas 1, dire « sans pouvoir sur le banc réel » et laisser le serrage porter seul la réserve 3. Couples M2-a à M2-f. (Variante acceptable : ne rien juger sur le banc réel, rapporter la lecture sans critère, et réécrire P12, l'hypothèse 4 et l'étage 1 en conséquence ; je ne donne pas ses couples.)

**M3. Trou de la table : « hors de la zone utile » masque un tort.** L'étage 2 est lu avant l'étage 3 ; une famille hors de la zone utile (plausible : les doses neuves de V2, V3 et V5 montent à 1,0, voir m10) donne « non concluante » même si une autre famille (« dense », « vide ») a une lecture « nuisible » vraie, ou si cette famille elle-même a des fausses promotions « nuisibles » (indépendantes de la couverture de F). [T] n'avait qu'une principale ; ici, avec quatre familles, le masque est réel. Couple M3.

**M4. Compositions non gelées pour « porteuse unique », « dense » et « vide ».** Seuls les totaux par sorte sont écrits (7 copies de la classe, 5 copies par morceaux, 8 fausses construites, etc.) ; la répartition à l'intérieur (mélanges ou lois tempérées ; lesquelles des quatre constructions de copies par morceaux ; fausses sous la règle du cosinus ou opposées, et V4) est laissée à qui écrira le code. Elle est pourtant décisive : les seules fausses promotions de [V] sont des copies par morceaux, et le choix de la construction change le résultat. R1 (aucune liberté après scellement). Correction : écrire la répartition (la mienne est une proposition, la rédaction peut en choisir une autre à condition de l'écrire) et la clé de graine du tirage des copies par morceaux. Couples M4-a et M4-b.

**M5. Annexe du serrage non écrite.** « distance fixée au scellement par un compte sans données, annexe à écrire » : la distance des cartes voisines du monde jouet, la variance attendue de Λ au plafond et la borne basse attendue de la mutation « bloc suivant » sont des paramètres qui déterminent si le serrage a un pouvoir (la mutation doit être tuée, sinon « pas de jeu ») et s'il fausse-alerte. Un texte scellé ne peut pas renvoyer à une annexe inexistante ; la contre-lecture 2 doit pouvoir la lire. Couple M5.

## 3. Remarques mineures

- **m1. Garde de chemin trop étroite.** Elle nomme `jeu-idee-1-2-copie` (copie du run invalide) mais pas la copie de la relance, qui contient les sorties du run lu (le brouillon ne l'interdit donc pas au code), ni les journaux ; les motifs `2026111*` sont aussi trop datés. Couples m1-a à m1-d (m1-d : le nom neuf de la copie du nouveau jeu ne doit pas déclencher la garde).
- **m2. Dénominateur de P3.** Les porteuses « au sens de l'oracle » sont 4 483, non 4 500 ([V] § 1 : 4 483 + 17 sans gain) ; et [V] § 3.2 dit « 55 porteuses arrêtées bas, une au plafond », non « 56 porteuses ». Couples m2-a, m2-b.
- **m3. Citation.** « 0,44 à 0,80 aux doses hautes » vient de [V] § 4, non de § 3.5 seul. Couple m3.
- **m4. Compte.** « jusqu'à onze intervalles » « nuisible » : je trouve dix (principale 2 + 2, par carte 1 + 1 + 1, dense 2, vide 1). Couple m4.
- **m5 (facultative, recommandée). Serrage : risque de fausse alerte et sortie.** Six règles saines à 95 % donnent jusqu'à environ 14 % de fausse alerte, qui arrête tout (« pas de jeu ») sans chemin de reprise écrit ; la reprise avec d'autres graines serait une seconde chance. Couple m5.
- **m6. Grille de sensibilité qui peut ne rien dire (P14).** Avec des valeurs e de moyenne 0,05 à 0,09, une borne de Markov donne au plus 0,0045 c générations avec promotion par génération pour une promotion à une carte, donc 39 sur 500 seulement à partir de c ≈ 17 : la valeur « c ≥ 8 » de P14 est vide, et la grille s'arrête à 32 sans dire que faire si rien n'est atteint. Couples m6-a, m6-b, m6-c.
- **m7. « Ne nuit pas » sans marge.** Les critères « nuisible » sont « borne haute < 0 » (tort significatif) ; sans marge de non-infériorité, « validation tenue » ne démontre pas l'innocuité, seulement l'absence de tort détecté ; avec 500 générations en « dense » près du plafond, la puissance est faible. À dire. Couple m7.
- **m8 (facultative, recommandée). Sensibilité du critère de fausses promotions en « vide » et « dense ».** « borne basse de FP_A − FP_F > +0,02 » laisse passer un décuplement (0,003 → 0,03) ; P8 prédit FP_A ≤ 0,05 mais n'en fait pas un critère. Couple m8.
- **m9. Serrage et étage 1.** L'étage 1 range une alerte du serrage sous « garantie mise en défaut » alors que la liste d'arrêt dit « pas de jeu » (le serrage se joue avant le jeu) : harmoniser. Couple m9.
- **m10. Doses neuves non chiffrées.** Le choix « pour rester dans la zone utile » n'est pas appuyé par un compte (information en nats) ; par interpolation (l'information varie comme le carré de la dose : 2,1 nats à 0,4 ; 8,8 à 0,8 ; 20,2 à 1,2, [T] annexe A), la dose 1,0 vaut environ 13 nats pour 6,17 nécessaires : F proche du plafond dans trois cellules sur dix. Le risque « hors de la zone utile » étant celui qui perdrait 10 à 12 heures, le chiffrer d'avance. Couple m10.
- **m11. P10** n'a de seuil de réfutation que pour « réplique » ; ajouter les deux autres familles (information, hors critères). Couple m11.

## 4. Couples « ancien → nouveau » (chaque « ancien » est présent une seule fois dans la pièce ; vérifié par programme, et l'application de tous les couples à la suite est sans collision)

Chaque couple s'applique à la pièce du brouillon 1 (`95f34a756c61b1f73df88cfa99350f9ffb741ad872a6afea90406e1f1acd6011`) ; le rédacteur peut reformuler, mais pas omettre ce que le couple exige.

**M1-a**

- ancien : ```à 500 générations **dans la version qui fera foi, avant son scellement** (jamais après).```
- nouveau : ```à leurs 500 premières générations (g de 0 à 499, 50 par cellule ; mêmes tirages que les 500 premières des 750, les clés étant par génération). **Règle écrite ici, avant tout tirage du jeu** : durée projetée = somme, sur les cinq familles, du nombre de générations multiplié par la durée moyenne mesurée par génération de la famille (bras, rejeu et oracle compris), plus 1 heure de contrôles ; la décision ne dépend que de cette durée, se consigne au registre avant le jeu et ne change aucun seuil ni aucun critère. L'essai à blanc se joue **après** le scellement de ce texte et de l'addendum d'empreintes (le code n'existe qu'à partir de là, voir l'en-tête) et avant le jeu, jamais avant le scellement.```

**M1-b**

- ancien : ```l'essai à blanc chronométré (étape 1) le dit avant le scellement et peut```
- nouveau : ```l'essai à blanc chronométré (étape 1, après le scellement, avant le jeu) le dit et peut, par la règle de l'étape 1,```

**M2-a**

- ancien : ```au temps d'arrêt, qui voit ce que les lectures sur la```
- nouveau : ```au temps d'arrêt, qui voit, sur les cartes voisines du monde (les seules où il n'est pas écrasé vers 0), ce que les lectures sur la```

**M2-b**

- ancien : ```moyenne du rapport exact Λ au temps d'arrêt, famille « nul », par bras```
- nouveau : ```moyenne du rapport exact Λ au temps d'arrêt, famille « nul », par bras, sorte « voisines du monde » (autres sortes et toutes cartes réunies : rapportées sans critère)```

**M2-c**

- ancien : ```moyenne par bras, toutes cartes réunies (sept intervalles), intervalle percentile à 95 % par```
- nouveau : ```moyenne par bras, sur la sorte « voisines du monde » (sept intervalles ; toutes cartes réunies et autres sortes rapportées sans critère), intervalle percentile à 95 % par```

**M2-d**

- ancien : ```lecture voit donc une fuite d'instants que les lectures sur W ne voient pas (réserve 3 de [V], [T] l. 316-318).```
- nouveau : ```lecture voit donc une fuite d'instants que les lectures sur W ne voient pas (réserve 3 de [V], [T] l. 316-318), **mais seulement là où Λ n'est pas écrasé vers 0** : pour une carte sans lien avec le monde, Λ vaut presque toujours une valeur minuscule, sa moyenne égale à 1 ne vient que d'événements rarissimes et la moyenne observée sur 500 générations reste très sous 1 ; toutes cartes réunies, la lecture ne pourrait donc rien voir. Elle est jugée sur la sorte « voisines du monde » seule. **Pouvoir déclaré, joué après le jeu sur les mêmes trajectoires** : la mutation « la règle lit le bloc suivant » est rejouée sur le bras A de la famille « nul » ; si la borne basse de la moyenne de Λ sur les voisines du monde ne dépasse pas 1, la lecture (5) est déclarée « sans pouvoir sur le banc réel », rapportée sans critère, et la réserve 3 de [V] reste portée par le seul serrage.```

**M2-e**

- ancien : ```une borne basse de moyenne de Λ au temps d'arrêt > 1 dans un bras (sept intervalles) = défaut ; sans```
- nouveau : ```une borne basse de moyenne de Λ au temps d'arrêt, sorte « voisines du monde », > 1 dans un bras (sept intervalles) = défaut ; sans```

**M2-f**

- ancien : ```lecture (5) sur Λ au temps d'arrêt, qui ne profite pas du conservatisme du certificat ;```
- nouveau : ```lecture (5) sur Λ au temps d'arrêt (sorte « voisines du monde » seule jugée : ailleurs Λ est écrasé vers 0 et la lecture est sans pouvoir ; pouvoir rejoué après le jeu), qui ne profite pas du conservatisme du certificat ;```

**M3**

- ancien : ```| **« hors de la zone utile »** pour cette famille ; la validation est **« non concluante »** ; le reste est rapporté |```
- nouveau : ```| **« hors de la zone utile »** pour cette famille ; la validation est **« non concluante »**, **sauf** si une lecture « nuisible » de l'étage 3 est vraie en même temps (fausses promotions dans cette famille, ou toute lecture « nuisible » d'une autre famille) : l'étage 3 est alors prononcé aussi, car un tort constaté n'est jamais masqué par un manque de puissance ; le reste est rapporté |```

**M4-a**

- ancien : ```Seule la composition change. Le classement final de chaque carte est celui de l'oracle.```
- nouveau : ```Seule la composition change. **Répartition à l'intérieur des sortes, gelée ici (proposition du contre-lecteur ; toute autre répartition doit être écrite de la même façon)** : copies de la classe, des mélanges de Dirichlet et des lois tempérées et inclinées en parts égales, l'éventuelle carte en plus étant un mélange (« porteuse unique », sept : 4 + 3 ; « dense », quatre : 2 + 2 ; « vide », six : 3 + 3) ; copies par morceaux, les quatre constructions de [T] prises une fois chacune, puis la ou les cartes en plus tirées sans remise parmi elles par la clé `(famille, g, 3001)` (« porteuse unique », cinq : les quatre plus une ; « dense », trois : trois des quatre) ; fausses construites, comme en famille T les quatre premières sous la règle du cosinus et les deux dernières opposées à force × 1 et × 0,5, les cartes en plus étant sous la règle du cosinus (« porteuse unique » et « vide », huit : six sous la règle du cosinus et deux opposées ; « dense », quatre : trois sous la règle du cosinus et une opposée à force × 1) ; **pour V4**, où l'opposé n'est pas une loi de la grammaire du juge, toutes sous la règle du cosinus. Le classement final de chaque carte est celui de l'oracle.```

**M4-b**

- ancien : ````(12, g, 3000)` ; rééchantillonnage `(99, b)` ;```
- nouveau : ````(12, g, 3000)` ; choix des copies par morceaux `(12 ou 13, g, 3001)` ; rééchantillonnage `(99, b)` ;```

**M5**

- ancien : ```(distance fixée au scellement par un compte sans données, annexe à écrire, pour que la variance de Λ au```
- nouveau : ```(distance fixée **dans ce texte, par une annexe A à écrire avant la contre-lecture 2 : la distance, la variance attendue de Λ au plafond et la borne basse attendue de la mutation « bloc suivant », comptées sans donnée du juge**, pour que la variance de Λ au```

**m1-a**

- ancien : ````diag/organisme-idees-juge-v1/2026111*-idee-1-2-*`,```
- nouveau : ````diag/organisme-idees-juge-v1/*-idee-1-2-*`,```

**m1-b**

- ancien : ````runs/2026111*-idee-1-2-*`, ni sous `/home/user/jeu-idee-1-2-copie` ; garde de chemin```
- nouveau : ````runs/*-idee-1-2-*`, ni sous aucun dossier `/home/user/jeu-idee-1-2-*` (copie du run invalide, copie de la relance, journaux) ; garde de chemin```

**m1-c**

- ancien : ```le code ouvre un chemin d'une sortie de l'idée 1.2 ou de la copie `/home/user/jeu-idee-1-2-copie````
- nouveau : ```le code ouvre un chemin d'une sortie de l'idée 1.2 ou d'un dossier `/home/user/jeu-idee-1-2-*````

**m1-d**

- ancien : ```sous un nom neuf ; consigne de [AR] § 5```
- nouveau : ```sous un nom neuf qui ne commence pas par `jeu-idee-1-2-` (sinon la garde de chemin l'arrêterait) ; consigne de [AR] § 5```

**m2-a**

- ancien : ```56 cartes sur 750 × 6 = 4 500 porteuses-générations, soit ≈ 0,012, § 3.2```
- nouveau : ```56 cartes (55 porteuses arrêtées bas, une au plafond) sur 4 483 porteuses au sens de l'oracle (§ 1 : 4 500 porteuses construites, dont 17 sans gain), soit ≈ 0,0125, § 1 et § 3.2```

**m2-b**

- ancien : ```[V] § 3.2 a trouvé 56 pertes pour 4 500```
- nouveau : ```[V] § 3.2 a trouvé 56 pertes pour 4 483```

**m3**

- ancien : ```couvertures de F par cellule, § 3.5 : 0,09 à 0,19```
- nouveau : ```couvertures de F par cellule, § 3.5 et § 4 : 0,09 à 0,19```

**m4**

- ancien : ```(jusqu'à onze intervalles sur quatre familles)```
- nouveau : ```(jusqu'à dix intervalles sur quatre familles : 4 + 3 + 3)```

**m5**

- ancien : ```survit et la liste d'arrêt dit « pas de jeu ».```
- nouveau : ```survit et la liste d'arrêt dit « pas de jeu ». **Une alerte sur une règle saine** (borne basse > 1 ; probabilité de fausse alerte jusqu'à environ 14 % pour six règles à 95 %, du côté sûr) reçoit l'audit écrit et le nœud de la mère ; le serrage ne se rejoue que sous un addendum scellé, avec les mêmes graines `(98, g)` et le code corrigé, jamais avec d'autres graines (R3).```

**m6-a**

- ancien : ```c ∈ {2 ; 4 ; 8 ; 16 ; 32}```
- nouveau : ```c ∈ {2 ; 4 ; 8 ; 16 ; 32 ; 64 ; 128}```

**m6-b**

- ancien : ```rapport : plus petit c « non tenu » par la lecture (1), plus petit c dont une borne basse de moyenne dépasse 1.```
- nouveau : ```rapport : plus petit c « non tenu » par la lecture (1), plus petit c dont une borne basse de moyenne dépasse 1 (« aucun jusqu'à 128 » si la grille ne l'atteint pas).```

**m6-c**

- ancien : ```attendu : c ≥ 8 (les valeurs e sont très petites, moyennes 0,05 à 0,09)```
- nouveau : ```attendu : c de l'ordre de 17 ou plus (borne de Markov pour une promotion à une seule carte : avec des moyennes de valeurs e d'au plus 0,09 et 24 cartes, au plus 0,0045 c par génération, soit 39 sur 500 à partir de c ≈ 17 ; les promotions à plusieurs cartes ne la changent guère)```

**m7**

- ancien : ```Le gain y est rapporté, sans critère (la couverture de « dense » risque le plafond ; celle de « vide »```
- nouveau : ```Le gain y est rapporté, sans critère, avec les bornes basses de C_A − C_F et de R_A − R_F ; « pas nuisible » veut dire « tort non établi », non « innocuité établie à une marge près » (aucune marge de non-infériorité n'est écrite ; dit, et lu ainsi au prononcé) (la couverture de « dense » risque le plafond ; celle de « vide »```

**m8**

- ancien : ```- **Familles « dense » et « vide »** : « nuisible » si la borne basse de FP_A − FP_F > +0,02 ; pour « dense » aussi si la borne```
- nouveau : ```- **Familles « dense » et « vide »** : « nuisible » si la borne basse de FP_A − FP_F > +0,02, ou si la borne basse de FP_A seul dépasse 0,05 par génération (niveau nominal : une différence de +0,02 ne voit pas un décuplement de 0,003) ; pour « dense » aussi si la borne```

**m9**

- ancien : ```ou, au serrage, une règle saine à borne basse > 1 |```
- nouveau : ```ou, au serrage (alors avant tout jeu : la liste d'arrêt dit « pas de jeu » et ce prononcé se rend sans lecture du jeu), une règle saine à borne basse > 1 |```

**m10**

- ancien : ```ce choix est fait avant tout tirage neuf et n'emploie aucune donnée du run.```
- nouveau : ```ce choix est fait avant tout tirage neuf et n'emploie aucune donnée du run. **Compte de dimensionnement à écrire en annexe B avant la contre-lecture 2** (information en nats sur 200 épisodes des dix doses neuves, sans juge, comme [BANC-v1] annexe A) et couverture attendue de F par famille qui en découle, pour que le risque « hors de la zone utile » soit chiffré avant le jeu : par interpolation, la dose 1,0 de V2, V3 et V5 vaut environ 13 nats pour 6,17 (log 480) nécessaires à une carte seule, donc proche du plafond pour F.```

**m11**

- ancien : ```| « réplique » < 230 | 0,55 |```
- nouveau : ```| « réplique » < 230 ; « porteuse unique » < 300 ; « dense » hors de 200 à 300 | 0,55 |```

## 5. Ce qui est bon (à conserver tel quel)

- Racine neuve, familles 10 à 14 et jeu synthétique `(98, g)`, refus de la racine de [T] : fermeture nette de la réserve 6 de [V]. La garde de chemin et son essai (sain et artefact) sont prévus.
- La conjonction réplique et porteuse unique comme test d'intersection et d'union à 0,05 sans correction est juste, et la table de lecture à huit étages est exhaustive (j'ai cherché une combinaison sans ligne : aucune ; l'étage 8 attrape le reste).
- Rappel par porteuse et tableau croisé par carte : bonne réponse à la réserve R-4 ; « nuisible par carte » comme critère est bienvenu.
- Étiquettes d'arrêt séparées des arrêts réels : bonne réponse à la réserve 5.
- La déclaration honnête du choix des doses après lecture de [V] et la règle « aucune valeur du run lu n'est employée ».
- Les questions Q-1 à Q-3 sont posées à la mère, non tranchées par le rédacteur.

## 6. Points pour la mère

- **À trancher avant le scellement** : Q-1 (juge candidat) et Q-2 (3 000 ou 2 500 générations) : le texte scellé ne peut pas porter de question ouverte ; la ligne de la liste d'arrêt sur le juge candidat et les lignes du Coût doivent être retirées ou gardées selon la réponse. Si Q-1 est retenue, préciser comment le juge candidat consomme le flux de chaque carte : tirer 800 issues d'un coup puis les lire par blocs ne donne les mêmes valeurs que 32 tirages de 25 que si la consommation du générateur est identique ; c'est précisément ce que l'essai de concordance éprouverait, à écrire.
- **Lettre du modèle du rédacteur** : le texte du brouillon est du modèle A (selon la consigne de cette tâche) ; à inscrire au registre.
- **Mot de Lazar** : aucun nécessaire pour ce texte (processeur, 0 dollar, aucun écart à un texte scellé, aucune adoption) ; le nœud d'adoption reste le sien et la levée de la condition « dénominateur fixe » est bien à lui signaler avec ce nœud.
- **Risque de durée** : le jeu ne tient que si une tâche reste active pendant toute sa durée (le run invalide est mort d'un redémarrage du conteneur) ; prévoir la tâche d'attente avant de lancer.
- **Les corrections M2 et M4 sont des choix de conception** (ce que la lecture (5) juge ; la répartition des sortes) : la rédaction peut en prendre d'autres, écrites.

## 7. Déclaration

Rôle : contre-lecteur neuf (R2), modèle C ; texte du modèle A. Heures (`date -u`) : début 01:19:54Z ; lectures de la pièce, de [V], [T], [AE], [AR] jusqu'au début du § 5 et du gabarit entre 01:20Z et 01:24Z ; vérification des couples par programme (scratchpad de la session, hors dépôt) et rédaction ensuite ; scellement : heure du compagnon. Jamais ouvert : voir en-tête. **Incidents** : aucun de ma main ; un programme court a importé `controle_ia.prereg` pour rejouer le validateur (lecture seule) ; `git status` après coup ne montre aucun fichier de ma main (les fichiers non suivis qu'il liste ne sont pas les miens). Aucun commit, aucun fichier existant modifié.
