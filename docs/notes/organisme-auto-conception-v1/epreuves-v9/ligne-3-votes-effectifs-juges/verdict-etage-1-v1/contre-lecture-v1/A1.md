# Additif 1 au préenregistrement de la ligne 3 (version 7) — règles écrites d'avance pour les silences du texte à l'étage 1 — v2

**Statut : à contre-lire (règle R2), puis à sceller par la mère, avant tout calcul de l'étage 1, chronométrage compris.** Écrit le 2026-11-20 (temps universel, `date -u` : 02:52Z à la première heure relevée), sur le mandat `mandat-redacteur-additif-1-ligne-3-points-a-e-v1.md` (`98cd555e809aa3385ba6a5c7bb2a0a50f16da6c714ea76cefc421947fa894972`, recalculée égale à son compagnon). **Version 2**, du 2026-11-20 : la version 1 (`27ecd5d5a8dba97352cf7ab18dee9ef0b9e3eaa5839122221640ee29be97c89d`) a été contre-lue (`contre-lecture-additif-1-ligne-3-v1.md`, `f12200ae427da3f3f70d549ac4dfef4feeb805b2279c7a24bf36e86f563d3955`, verdict « Conforme après corrections ») ; cette version 2 porte ses six corrections de texte, à la lettre, et rien d'autre que le titre et cette ligne de version ; aucun critère gelé ne change. Reste : la vérification de ces corrections, puis le scellement par la mère.

Texte complété, non réécrit : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-3-votes-effectifs-juges-v7.md`, lu sur main après `git fetch origin main` (tête `732d73379643f10f1398282fa1e178d49bce6fe2`), empreinte recalculée `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0`. Dans la suite, « le texte » désigne cette version 7, et « le code v2 » désigne `banc_juges_scriptes_ligne_3_v2.py` (`ffc330839de048891bdbd323b8c19c04289386f9379492440a13e7df4c09b5b3`).

## Ce que cet additif fait, et ce qu'il ne fait pas

- Il écrit, avant tout tirage, une règle pour chaque endroit où le texte se tait et où le code de l'étage 1 a dû choisir : points A à E, silences 1 et 2, points F à J, et les autres choix déclarés par le développeur.
- **Il ne change aucune hypothèse, aucune prédiction, aucun seuil, aucun critère de lecture gelé, aucune règle gelée (nombre de témoins, portée), aucun montant.** Là où combler un silence demanderait d'ajouter une ligne à une table gelée ou un seuil neuf, il ne le fait pas : il écrit ce qui se passe sans cet ajout, et la question est posée à Lazar (deux nœuds, au rapport du rédacteur).
- **Aucune règle ne vise un signe** (règle R3). Quand deux lectures étaient possibles, j'ai retenu soit la plus étroite, soit celle que le texte impose par ailleurs (« la plus basse »), et je dis laquelle.
- **Aucun résultat n'a été lu** (règle R1) : aucun calcul de l'étage 1 n'existe, je n'en ai lancé aucun, ni chronométrage, ni tirage, ni essai. Je n'ai lu que le texte, le code et les rapports nommés à la fin.
- Il ne nomme pas le code : le commit et les empreintes du code restent l'objet de l'**additif de code** que le texte prévoit (en-tête, « Commit du code d'analyse »). Cet additif 1 se scelle avant lui, parce qu'il demande deux ajouts au code (section « Ce que le code doit changer »).
- Rien ici ne touche l'étage 2.

Ce que ce résultat ne fera jamais reste entier : aucun mot de cet additif ne fait trancher une carte par un juge, scripté ou réel.

## Règle A — le monde où se mesure la puissance de la lecture « positif » de ρ′ − ρ

*Le silence.* Le texte demande « la puissance de la lecture « positif » de l'écart ρ′ − ρ, pour un écart de 0,2, 0,3 et 0,5 » (« Plan d'analyse », « Ce que l'étage 1 rend à l'étage 2 »), sans écrire le monde.

*La règle.*
1. **Monde.** Deux juges ; 100 témoins, 50 bons et 50 mauvais, **sans partage en moitiés** (à l'étage 2, ρ et ρ′ se lisent sur les 100 témoins, sans étalonnage) ; taux d'erreur de 0,20 dans les deux classes, pour les deux juges (le taux de la règle gelée du nombre de témoins) ; chaque juge rend deux fois chaque témoin.
2. **Loi : la loi 1, emboîtée.** Par témoin : avec probabilité ρ, les quatre lectures lisent un même tirage commun ; sinon, pour chaque juge séparément, avec probabilité (ρ′ − ρ) / (1 − ρ), ses deux rendus lisent un même tirage propre à ce juge ; sinon chaque rendu lit le sien. Une lecture est une erreur si le tirage lu est sous 0,20. La corrélation des erreurs vaut alors ρ entre deux lectures de juges différents et ρ′ entre les deux rendus d'un même juge (calcul direct, à vérifier par le contre-lecteur).
3. **Cellules.** Écart : 0,2 ; 0,3 ; 0,5. ρ : les sept valeurs de la grille. ρ′ = ρ + écart. Une cellule où ρ′ dépasse 1 est « infaisable », nommée, jamais tue. Compte à la main : 15 cellules faisables sur 21 (écart 0,2 : ρ ≤ 0,75 ; écart 0,3 : ρ ≤ 0,6 ; écart 0,5 : ρ ≤ 0,45).
4. **Lecture, par réplique**, comme à l'étage 2 : ρ entre les premiers rendus des deux juges ; ρ′ de chaque juge entre ses deux rendus ; intervalle apparié à 95 % de ρ′ − ρ par rééchantillonnage des témoins, stratifié par classe, 2 000 tirages, centiles, tirages indéfinis écartés ; « positif » si la borne basse dépasse 0. Une réplique dont la borne est indéfinie n'est pas « positif ».
5. **Ce qui est rendu.** Par cellule, sur 2 000 répliques : la part des répliques « positif » pour le juge 1, pour le juge 2, et **pour les deux à la fois**. Le chiffre qui répond à la question du texte est celui « des deux », puisque le rang 2 de l'étage 2 exige « positif » pour les deux juges. Lecture d'ensemble, lue sur la table sans calcul neuf : pour chaque écart, la plus basse et la plus haute de ces puissances sur les cellules faisables ; toutes les cellules sont rapportées.
6. **Ce que ce chiffre ne fait pas.** Il n'entre dans aucune règle gelée : ni la règle du nombre de témoins, ni la règle de portée (qui ne porte que sur les quatre comparaisons d'agrégations). Il ne déclenche ni dépense, ni arrêt, ni mot. Il est rendu à la mère comme une information sur ce que 100 témoins peuvent dire.

*Limites, dites d'avance.* Une seule loi, des taux symétriques à 0,20. La loi 3 du texte n'est pas jouée ici : la difficulté d'un témoin y est commune à toutes les lectures, donc ρ′ = ρ par construction, et y planter un écart demanderait une structure que le texte n'a pas. Si les juges réels sont sévères (hypothèse H-sévérité), leur puissance peut différer de celle de ce monde.

*Code v2 :* **suit déjà** (`tirer_quatre_rendus`, `cellule_ecart_rho_prime` ; configuration `ecart_rho_prime`).

## Règle B — ρ′ du bras R dans les mondes de puissance plantés pour l'unanimité et pour le juge seul

*Le silence.* Le texte écrit, pour le bras R, « erreurs répétées à ρ′ = 0 ; 0,5 ; 0,9 », et indexe les cellules par « ρ ; et ρ′ pour le bras R ». Mais « dans le monde planté pour une comparaison, le test entier est joué » : le bras R est donc présent, par la correction de Holm, dans les mondes plantés pour l'unanimité et pour le juge seul, où le texte ne dit pas son ρ′.

*La règle.*
1. Dans les mondes plantés pour la comparaison à l'unanimité et pour la comparaison au juge seul, **une cellule est une valeur de ρ, et une seule** : c'est le compte du texte (« quatre sous la loi 1, deux sous la loi 3 » contre l'unanimité ; « deux, une » contre un juge seul) et celui du calcul de référence, qui n'y porte aucun ρ′.
2. Dans ces cellules, le bras R est joué à **ρ′ = 0**.
3. Dans le monde planté pour la comparaison au bras R, rien ne change : une cellule est un couple (ρ ; ρ′), ρ′ = 0 ; 0,5 ; 0,9, comme le texte l'écrit.
4. Les comparaisons « écart ≤ 0 » (valeur de probabilité) et « écart observé de 0,05 au moins » se font à 1e-12 près, pour qu'une égalité exacte ne dépende pas de l'arrondi des flottants.

*Pourquoi ρ′ = 0, et non une autre valeur.* Le texte fait décider « la plus basse » des puissances. La correction de Holm est monotone : à valeurs fixées des trois autres, plus la valeur de probabilité de la comparaison au bras R est petite, plus les seuils de Holm des trois autres sont larges (seul compte ici le rejet de Holm de cette comparaison, non sa marge de 0,05). À ρ′ = 0, le bras R est la majorité de trois votes indépendants ; son erreur dans une classe de taux p < 0,5, ρ′ p + (1 − ρ′)(3 p² − 2 p³), croît avec ρ′ : c'est le bras R le plus exact, donc, en moyenne, le plus difficile à battre, et la valeur où il aide le moins les trois autres comparaisons. Le raisonnement porte sur la moyenne de l'écart, non sur sa loi entière : ρ′ change aussi la corrélation du bras R avec le premier rendu du juge 2, que lit le bras C, donc la dispersion de l'écart apparié, dans un sens que rien ici ne signe. Jouer les trois valeurs et garder la plus basse rendrait donc très probablement, sans preuve, la valeur à ρ′ = 0 ; si ce n'était pas le cas, l'écart irait vers une puissance qui décide un peu plus haute, par les seuls seuils de Holm. **C'est un raisonnement, non un calcul** ; aucun tirage ne l'a vérifié. Le choix va dans le sens prudent contre le « oui » : il ne peut pas rendre atteignable un « oui » qui ne le serait pas à une autre valeur de ρ′, sous ce raisonnement.

*Code v2 :* **suit déjà** (`enumerer_cellules_puissance`, `primes = (0.0,)` hors du bras R ; `EPS`).

## Règle C — à quel juge le bras R est lié

*Le silence.* Le texte écrit « le même juge scripté lu k fois », sans dire lequel.

*La règle.*
1. **Dans la grille de l'étage 1** (estimateur et agrégation), le bras R est le **juge 1** de la cellule. Son premier rendu est le verdict du juge 1 que lisent aussi les bras S et U ; avec probabilité ρ′, tirée une fois par témoin, tous les rendus suivants recopient l'erreur du premier ; sinon chacun tire la sienne, indépendamment, au taux du juge 1 pour la classe du témoin (loi 1 entre rendus : c'est la loi qui donne l'erreur de la majorité de trois du texte, ρ′ p + (1 − ρ′)(3 p² − 2 p³)). Même loi dans le monde de puissance, sur le juge 2. À deux juges, k = 2 et k = 3 se lisent sur les mêmes tirages (k = 2 : les deux premiers des trois rendus). À cinq juges, k = 5.
2. **Dans le monde de puissance**, le bras R est le **juge 2**, pendant scripté du juge Argon de l'étage 2 : comme le bras R-Argon, il partage son premier rendu avec le bras « juge seul » du même juge.
3. **Ce que ce choix change, et ne change pas.** Dans le monde de puissance, les deux juges ont le même profil : lier R au juge 1 ou au juge 2 ne change aucune loi, seulement une étiquette. Dans la grille, aux profils à taux égaux entre juges (lois 1, 2, 3 et 4), les taux du bras R ne dépendent pas du juge choisi ; seule sa corrélation avec les autres bras en dépend, donc la largeur des intervalles des écarts appariés, non leur moyenne. **Au profil inégal, le juge 1 est le juge le plus exact** (taux 0,10) : le bras R y est le meilleur juge répété. Le mot de `fa38f9faa24e0` et les écarts « U moins R » de ce profil se lisent avec cette mention. Le bras R du juge le moins exact n'est pas joué.

*Code v2 :* **suit déjà** (grille : `repetitions(rng_t, E[..., 0], …)` ; monde de puissance : `E[..., 1]`).

## Règle D — composition du bras « alarme de changement de juge »

*Le silence.* Le texte écrit « un juge change » et « taux brut de notable des cartes de production », sans dire la composition du collège, des suites, des ancres ni le sens de la bascule.

*La règle.* Par cellule (m = 10 ; 20 ; 40), 2 000 suites de 12 générations.
1. **Un seul juge** : celui qui change. Le « notable » d'une carte de production est son verdict ; la sentinelle compte ses erreurs sur les ancres. Aucun second juge, aucune agrégation : le texte n'écrit ni les taux ni la corrélation d'un second juge pour ce bras.
2. **Suites.** La moitié change (1 000), l'autre non (1 000). Parmi les suites qui changent : moitié « à effet » (500), moitié « sans effet » (500).
3. **Taux de départ.** Suite « à effet » : vrais rejetés 0,10 et faux acceptés 0,10, puis 0,25 et 0,25. Suite « sans effet » : vrais rejetés 0,05 et faux acceptés 0,15, puis **vrais rejetés 0,15 et faux acceptés 0,05** (le juge devient plus sévère ; l'erreur équilibrée reste 0,10). Les suites sans changement sont partagées par moitié entre ces deux départs, pour que la fausse alarme se mesure sur le même mélange de départs.
4. **Génération du changement** : tirée uniformément de la 4ᵉ à la 10ᵉ, bornes comprises ; les nouveaux taux valent à partir de cette génération.
5. **Compositions.** Référence : 100 ancres, 50 bonnes et 50 mauvaises, lues aux taux de départ ; le taux de référence est le nombre d'erreurs observé sur 100. Ancres par génération : m / 2 bonnes, m / 2 mauvaises. Production : 70 bonnes et 30 mauvaises par génération. Bras D : m cartes de plus par génération, dont 70 % de bonnes, arrondi à l'entier (7 sur 10 ; 14 sur 20 ; 28 sur 40).
6. **Tests.** Bras A : l'organisme actuel, aucune alarme par construction ; ses mesures sont rapportées comme les autres (parts à dénominateur nul : « indéfini »). Bras B à D : aux générations 2 à 12, soit 11 tests par suite et par bras, au niveau 0,05 / 11 ; alarme si la valeur de probabilité est au plus égale au niveau. Bras B : test binomial exact bilatéral (somme des probabilités au plus égales à celle de l'observé, tolérance relative 1e-7). Bras C et D : test bilatéral de deux proportions contre la génération 1, variance poolée ; aucune alarme si la variance est nulle. Une référence à zéro erreur donne un taux de référence nul : toute erreur sur les ancres a alors une valeur de probabilité nulle, donc une alarme ; c'est ce que fait le code, et le cas est rare (de l'ordre de 3 sur 100 000 suites).
7. **Mesures, par bras.** *Détection* : dans une suite qui change, au moins une alarme à une génération égale ou postérieure à celle du changement ; rapportée à part pour les changements « à effet » et « sans effet ». *Délai* : première telle génération moins la génération du changement, en moyenne sur les suites « à effet » détectées. *Fausse alarme* : part des suites sans changement qui portent au moins une alarme. *Alarme avant changement* : part des suites qui changent et qui portent une alarme avant leur changement ; rapportée à part, jamais comptée comme détection.

*Limites, dites d'avance.* Un seul sens de bascule de sévérité est joué (vers le plus sévère) ; l'autre ne l'est pas. Un collège n'est pas joué. Les ancres sont à moitié bonnes, les cartes de production à 70 % : c'est ce qui rend la bascule « sans effet » invisible à la sentinelle et visible au taux brut.

*Code v2 :* **suit déjà** (`cellule_alarme`).

## Règle E — l'issue « la tolérance tient à n = 50 seulement »

*Le silence.* La table gelée de l'estimateur a trois lignes de fond (tient à 100 ; tient pour un n plus grand, pas à 100 ; ne tient à aucun n ≤ 400) et la ligne « invalide ». Si la tolérance tient à n = 50 et à aucun de 100, 200 et 400, aucune ligne ne s'applique.

*La règle.* **Je n'ajoute aucune ligne à la table gelée** : ce serait changer un critère gelé, et cela revient à Lazar (nœud 1 du rapport).
1. **Cellules de la règle** (précision, sans changement) : les cellules à deux juges, taux d'erreur 0,20 égal dans les deux classes, aux sept valeurs de ρ sous la loi 1 et aux six sous la loi 3 ; la loi 3 n'est jouée qu'à deux juges. « Tient à n » veut dire : les treize cellules tiennent à ce n.
2. **Si cette issue se présente**, le verdict de l'étage 1 n'est aucun des mots de la table : ni « oui », ni « non, pas à cette taille », ni « non ». L'agent neuf qui prononce (règle R13) écrit : **« cas non prévu par la table gelée : la tolérance tient à n = 50 et à aucun n plus grand »**, avec la table par n et, pour chaque cellule de la règle qui manque à 100, 200 ou 400, celles des quatre tolérances qui manquent et de combien.
3. **Ses effets sont déjà gelés** et ne dépendent pas du mot : la règle du nombre de témoins dit « N = 100 si la tolérance tient à n = 100 […] Sinon, aucune dépense », et la liste d'arrêt dit « étage 1 non « oui » — pas d'étage 2 ». Donc : pas d'étage 2, aucune dépense, aucun devis à une taille plus grande (aucune taille plus grande ne tient), et la table retourne à Lazar.
4. **Audit de symétrie (règle R4), écrit avant le prononcé.** Un estimateur qui tient avec moins de témoins et manque avec plus est un résultat suspect. Cet audit part **pour toute issue non monotone** (la tolérance tient à un n et manque à un n plus grand de la grille), que la table ait une ligne ou non : il dit, par cellule, quelle tolérance manque, de combien, et si l'écart tient dans le bruit de 2 000 répliques. Quand une ligne de la table s'applique à la lettre (par exemple « tient à 200, pas à 100 ni à 400 » : deuxième ligne), le mot reste celui de la table, et l'audit est joint.
5. **Aucune relance** de l'étage 1, aucun changement de graine, de grille ou de tolérance après lecture (règle R3).

*Code v2 :* **suit déjà** : il rend « cas non prévu par la table gelée (tient à n = 50 seulement) : rendu à la mère », taille retenue vide, sans repli silencieux ; ses cellules de la règle sont celles du point 1 (`criteres_estimateur`).

## Règle du silence 1 — « part des alarmes qui portent sur un changement à effet »

*Le silence.* La phrase a deux lectures : la part parmi les seules détections de changement, ou la part parmi toutes les alarmes, fausses alarmes comprises.

*La règle.* **Les deux grandeurs sont rendues, sous deux noms qui ne se confondent pas.** Aucune n'entre dans un seuil ni dans un mot ; rendre les deux ne laisse donc aucun choix après lecture. L'unité est la suite. Par bras et par m :
- **(a) part parmi les détections** : nombre de suites « à effet » détectées, divisé par le nombre de suites qui changent et qui sont détectées (« à effet » ou « sans effet »).
- **(b) part parmi toutes les suites en alarme** : nombre de suites « à effet » détectées, divisé par le nombre de suites qui portent au moins une alarme à l'un des 11 tests, qu'elles changent ou non, que l'alarme tombe avant ou après le changement. Une suite « à effet » dont toutes les alarmes précèdent le changement est au dénominateur, non au numérateur.
- Dénominateur nul : « indéfini », jamais 0. Les numérateurs et dénominateurs sont rendus à côté des parts.
- Mention obligatoire avec (b) : elle dépend du mélange planté (une suite sur deux change, une sur quatre « à effet »).

*Code v2 :* **suit (a)** (`part_des_detections_sur_changement_a_effet`). **(b) et les comptes sont à ajouter** (changement 1).

## Règle du silence 2 — l'alarme ne reçoit aucun mot calculé

*Le silence.* Le texte dit que chaque bras de l'étage 1 peut recevoir l'un de trois mots, mais n'écrit pour la carte de l'alarme (`fcbf4a2dd1a57`) aucune règle de mot : il liste ses critères comme des mesures (détection, délai, fausse alarme, part des alarmes à effet) sans seuil, et ne donne que la fausse alarme gelée (0,05 par suite), la borne de réfutation (0,08) et la clause de réfutation de la prédiction P6.

*La règle.* **La carte de l'alarme ne reçoit aucun mot** : ni « tient sur le banc », ni « réfuté sur le banc », ni « sans prise ». Écrire une règle de mot demanderait des seuils que le texte n'a pas ; ce serait un critère gelé neuf, qui revient à Lazar (nœud 2 du rapport). Le rapport de l'étage 1 écrit, pour cette carte : « mesurée, sans mot : aucune règle de mot gelée ».

L'alarme se lit **contre la prédiction P6, à la lettre de sa clause de réfutation**, sur les valeurs observées, sans intervalle (« Étage 1 : pas de test ; lecture par cellule »), sur les comptes entiers :
- **Clause « fausse alarme »**, lue à chaque m (10 ; 20 ; 40) : atteinte si la fausse alarme de la sentinelle (bras B) dépasse strictement 0,08, soit plus de 80 suites sans changement en alarme sur 1 000.
- **Clause « détection »**, lue à m = 20 et à m = 40 (« à partir de 20 ancres par génération ») : atteinte si le nombre de changements « à effet » détectés par la sentinelle (bras B) est inférieur ou égal à celui du bras apparié (bras D), sur les 500 suites « à effet ». À m = 10, les deux nombres sont rapportés, hors clause.
- **P6 est dite « P6 réfutée »** si l'une des deux clauses est atteinte dans l'une de ses cellules ; « P6 non réfutée » sinon. Ces deux mots ne sont pas ceux des cartes (« tient sur le banc », « réfuté sur le banc », « sans prise ») et ne s'écrivent jamais pour la carte `fcbf4a2dd1a57`. Chaque clause est rapportée par m, avec ses comptes : le lecteur voit ainsi le bruit (500 et 1 000 suites), et un écart d'une poignée de suites se lit comme tel.
- Le reste de P6 n'a pas de clause : la fausse alarme « entre 0,05 et 0,08 » et la détection des changements « sans effet » par les bras C et D sont rapportées, sans mot.
- Ce mot porte sur une prédiction du rédacteur, non sur la carte ; il ne dit rien de juges réels (réserve 11 du texte).

*Code v2 :* ne calcule rien de cela ; les mesures y sont, la lecture se ferait à la main. **Les deux clauses, par m, avec leurs comptes, sont à ajouter comme aide** (changement 2), pour que la lecture ne repose pas sur un calcul à la main.

## Points F à J

- **F — les mots et le verdict mécanique calculés par le code.** Gardés, comme une **aide**, marqués tels dans la sortie. Le verdict de l'étage 1 est prononcé par un agent neuf (règle R13), qui applique lui-même les critères gelés et cet additif aux mesures, puis compare à l'aide ; tout désaccord est écrit et levé avant le scellement du verdict. L'aide n'est jamais le verdict. *Code v2 : suit déjà.*
- **G — garde des graines non éprouvée par défaut réintroduit.** Sans objet pour le texte : la correction C3 l'a fermée dans le code v2 (essai sain et six défauts sur `verifier_autorisation`). Le défaut sur la dérivation elle-même reste non réintroduit, à raison : il ferait dériver une racine décisive.
- **H — le calcul de référence nommé à l'annexe A.** L'annexe A nomme `calcul_predictions_ligne_3_v1.py` ; l'en-tête du texte dit que la version 2 de ce calcul rend les mêmes valeurs, clé par clé, plus une partie. **Les essais du code se font contre la version 2** (`calcul_predictions_ligne_3_v2.py`, `802d4dd26d66ead35326cef2d77c8a55e12c11b89a4ddbce4d9a115927428dc6` ; sortie `2cf1eba7e4fce530e14b4045574f7c4ff97fdb94367aef740c5c274a14eae724`). Aucune valeur ne change. De même, les noms de fichiers de l'annexe A (« …_v1.py ») sont un plan : les noms et les empreintes réels sont ceux que portera l'additif de code. *Code v2 : suit déjà.*
- **I — le chemin du calcul de référence dans les essais.** Sans objet pour le texte : c'est l'affaire de l'additif de code et du versement.
- **J — durée et processus unique.** Le texte ne fixe aucune durée : « l'heure, sur quatre cœurs » y est un ordre de grandeur, non une règle. **La durée n'est ni un critère ni une garde d'arrêt.** Le chronométrage, qui n'imprime que des durées, précède l'exécution décisive, comme écrit. L'étage 1 est joué une fois. Une exécution interrompue **avant d'avoir écrit son fichier de résultat** n'a rien rendu et rien n'en a été lu : elle est relancée à l'identique (même code, même configuration, mêmes racines, dossier de sortie neuf), et l'interruption est écrite au manifeste et au rapport. Une exécution qui a écrit son résultat n'est jamais rejouée. *Code v2 : suit déjà* (écriture du résultat en fin d'exécution, une exécution par dossier).

## Les autres choix déclarés par le développeur

Le rapport du développeur (version 1, « Où le texte se tait ») déclare dix-huit choix. Les choix 10, 13, 14 et 17 sont les règles C, B, A et D. **Les quatorze autres sont repris ici comme règles, tels que le code v2 les fait**, parce que chacun est la lecture la plus étroite du texte et que la contre-lecture du code n'y a trouvé aucun écart. Je les ai relus dans les rapports ; je n'ai vérifié dans le code que les choix 1, 2 et 3.

- **1.** Partage par moitié : avec c témoins par classe, l'étalonnage reçoit plafond(c / 2) bons et plancher(c / 2) mauvais (13 et 12 à n = 50), ce qui garde les tailles d'étalonnage 25 ; 50 ; 100 ; 200 de la branche (2).
- **2.** Cellules jouées : à deux juges, lois 1, 2 et 3 ; à cinq juges, lois 1 et 4 (« le banc à J = 5, lois 1 et 4 »). Loi 3 : au seul taux 0,20, ρ ≤ 0,75. Loi 4 : aux six profils à taux égaux entre juges, sans le profil inégal ; la valeur plantée y reste 7ρ / 15 aux profils dissymétriques, puisque les taux sont égaux entre juges dans chaque classe (calcul direct, à vérifier).
- **3.** ρ moyenne « indéfinie » dès qu'un juge n'a aucune variance, comme pour une paire. À deux juges, c'est la lettre du texte. À cinq juges, c'est plus strict que la formule de la somme ; cela ne touche aucune cellule de la règle du nombre de témoins.
- **4.** Intervalle : tirages indéfinis écartés et comptés ; couverture comptée sur les répliques à estimation définie, un intervalle indéfini comptant « non couvrant » ; centiles à interpolation linéaire ; « plus petit n qui tient » = le plus petit n où la cellule tient.
- **5.** Rééchantillonnage sur les comptes de configurations d'erreurs, par paquets de 50 répliques (constante qui fixe l'ordre des tirages).
- **6.** Égalité au seuil des bras C, P et « poids égaux » : tolérance de 1e-9 × (1 + |seuil| + somme des |poids|), dans laquelle le score rend « non notable ».
- **7.** Repli du bras C sur des poids égaux : trace nulle, poids non finis, ou moyenne des poids nulle ou négative ; compté par cellule.
- **8.** Bras P : les deux poids d'une paire sont divisés par deux une fois par paire au-dessus de 0,5 ; une paire à corrélation indéfinie n'est pas divisée.
- **9.** Bras N : une réplique dont les votes effectifs d'étalonnage sont indéfinis est écartée et comptée.
- **11.** Mot de `fa38f9faa24e0` à l'étage 1 : références « poids égaux » et bras R à k = J ; un mot par valeur de ρ′.
- **12.** Comparaisons descriptives de l'étage 1 : intervalle par rééchantillonnage des répliques.
- **15.** Double rendu : le bras 4 lit les premiers rendus des deux juges du bras 1 ; le bras 2, ces deux juges et deux autres ; le prédicteur de surface dit « non notable » si le trait est présent ; une réplique sans groupe est écartée et comptée.
- **16.** Garde de cadrage : rondes à moitié vraies, s = 1 aussi pour les rondes saines ; « dépasse » est strict.
- **18.** Graines : une cellule reçoit l'enfant de rang fixe de `SeedSequence(racine, spawn_key=(clé,)).spawn(nombre)`, dans l'ordre gelé des cellules ; l'autorisation des racines 2026111931 à 2026111933 est l'additif de code, par chemin et empreinte.
- **Correction C2** (version 2 du code) : « la plus petite taille d'étalonnage à partir de laquelle la branche tient » = la plus petite taille telle que la branche tient à cette taille et à toutes les tailles plus grandes de la grille ; « aucune » si la plus grande ne tient pas. C'est la lettre du texte ; reprise.

## Ce que le code doit changer

Deux ajouts, tous deux **après les tirages, sur les tableaux déjà tirés** : aucun tirage, aucune graine, aucune constante, aucune mesure existante ne change. Ils vont à un développeur d'un autre modèle que le rédacteur ; version neuve du code (règle R12), essais sur cas sain et sur artefact (règle R5), contrôle des défauts réintroduits rejoué, vérification, puis additif de code.

1. **Alarme, silence 1.** Dans `cellule_alarme`, par bras : ajouter la part (b), sous un nom distinct de (a), et les cinq comptes (suites « à effet » détectées ; suites qui changent détectées ; suites en alarme ; suites sans changement en alarme ; suites). « Indéfini » si le dénominateur est nul.
2. **Alarme, silence 2.** Dans les critères mécaniques, marqués comme aide : par m, les comptes et les deux clauses de P6 (fausse alarme du bras B : plus de 80 sur 1 000 ; détection « à effet » du bras B inférieure ou égale à celle du bras D, lue à m = 20 et 40) ; le mot de P6 (« P6 réfutée » ou « P6 non réfutée ») ; et, pour la carte, « mesurée, sans mot : aucune règle de mot gelée ». Les comparaisons se font sur les comptes entiers.

Le développeur montre, sur la racine des essais seule, que toutes les clés existantes de la sortie sont égales avant et après.

## Ordre des gestes, complété

Le geste (3) du texte se lit ainsi : contre-lecture de cet additif 1 par un agent neuf d'un autre modèle, qui ne l'a pas écrit (règle R2) ; scellement par la mère ; les deux ajouts au code, leur vérification ; additif de code scellé ; chronométrage ; puis le geste (4), l'étage 1, une fois. Aucune racine de 2026111931 à 2026111933 n'est dérivée avant.

## Réserves propres à cet additif

1. Les règles A, C et D fixent des mondes que nous choisissons (réserve 1 du texte) : une autre composition de l'alarme, un autre juge pour le bras R, une autre loi pour ρ′ − ρ donneraient d'autres chiffres.
2. La règle B repose sur un raisonnement de monotonie, non sur un calcul.
3. Les règles E et du silence 2 laissent volontairement un cas sans mot : c'est le prix de ne toucher à aucun critère gelé sans le mot de Lazar.
4. Ces règles ont été écrites en lisant le code v2 : elles reprennent ses choix partout où ils sont les plus étroits. Le contre-lecteur dira si l'une d'elles ne tient que parce que le code l'avait déjà faite.

## Pièces lues

| pièce | sha256 |
|---|---|
| texte, version 7 (main, `git show`) | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` |
| devis, version 7 (main, `git show`) | `382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270` |
| `code-etage-1-v1/rapport-developpeur-code-etage-1-ligne-3-v1.md` | `ee8cd1b4504a0d55f64b6da3006a336a732be50bf0e8b7796df2c050e11eefdb` |
| `code-etage-1-v2/rapport-developpeur-code-etage-1-ligne-3-v2.md` | `995bd5f48494e9a241fcb5c7824c59105d0ddf0c0f8cc95702e942bdcf58903c` |
| `code-etage-1-v1/contre-lecture-v1/contre-lecture-code-etage-1-ligne-3-v1.md` | `3aed6849c76a4ed421207470e4a6b8a45fcecf6a8ef5325a5203c84fda2f85ff` |
| `code-etage-1-v2/verification-corrections-code-etage-1-ligne-3-v1.md` | `09e462b9f42ccd7d11828c2f630a2cd6a6d205f2e1e15948c1a62b0664506186` |
| `code-etage-1-v2/banc_juges_scriptes_ligne_3_v2.py` | `ffc330839de048891bdbd323b8c19c04289386f9379492440a13e7df4c09b5b3` |
| `calcul_predictions_ligne_3_v2.py` (lignes du bras R seulement) | `802d4dd26d66ead35326cef2d77c8a55e12c11b89a4ddbce4d9a115927428dc6` |

Les chemins relatifs partent du dossier de la ligne, `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`. Du devis, je n'ai rien lu : il n'est cité que pour son empreinte. Du texte, j'ai lu en entier les sections de l'en-tête à « Voisins du catalogue » et l'annexe A ; je n'ai pas relu la section « Contre-lecture » ni les différentiels.

Rédacteur neuf, modèle F.
