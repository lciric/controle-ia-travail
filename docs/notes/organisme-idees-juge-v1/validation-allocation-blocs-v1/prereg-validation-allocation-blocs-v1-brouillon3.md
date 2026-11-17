# Préenregistrement — validation propre de l'allocation par blocs des tirages frais du juge, sur données neuves et banc neuf — brouillon 3

- **Auteur** : rédacteur neuf, sous-agent de la session mère ; il n'a écrit ni le préenregistrement de l'idée 1.2, ni ses
  addendums, ni son code, ni sa lecture gelée, ni son verdict, ni aucune de leurs relectures. Lettre du modèle : à inscrire par
  la mère au registre (la table des lettres n'est pas dans les pièces que j'ai lues).
- **Date (UTC)** : 2026-11-17, rédaction de 01:03 à 01:11 (`date -u` ; heure exacte du scellement : compagnon `.sha256`).
  Dépôt lu sur `main`, tête `c97bf55fb2fe2a2d3463ca79a8d67b9ab834a799` ; aucun commit, aucune poussée.
- **Brouillon 2** : 2026-11-17 01:35:21Z (`date -u`, au moment de l'écriture ; scellement aussitôt après, compagnon `.sha256`) ; corrections de la contre-lecture 1
  appliquées par un rédacteur neuf, par programme ; tête de `main` lue : `1df4ae9fdd74142e290d8f177a5ac16110de60db` ; rien d'autre ne change (voir « Contre-lecture »).
- **Brouillon 3** : 2026-11-17 02:41:50Z (`date -u`, au moment de l'écriture ; scellement aussitôt après, compagnon `.sha256`) ; corrections de la contre-lecture 2
  appliquées par un rédacteur neuf, par programme, et annexes A et B écrites ; tête de `main` lue : `6467b9225044394f018fb4188d5752b253ba0855` ; rien d'autre ne change (voir « Contre-lecture »).
- **Commit du code d'analyse** : **aucun à ce jour** ; le code s'écrit après la contre-lecture et le scellement de la version
  qui fera foi ; ses empreintes entrent dans un addendum d'empreintes scellé avant tout jeu, qui ne change rien d'autre.
- **Statut** : **brouillon 3** (corrections des contre-lectures 1 et 2 appliquées ; annexes A et B écrites), pièce de travail scellée par
  son compagnon (R6). Il ne fait pas foi. **Il n'est pas scellable** tant que la mère n'a pas tranché Q-1, Q-2 et Q-3
  (défaut M3' de la contre-lecture 2, voir « Contre-lecture ») et que les lignes qui en dépendent n'ont pas été retirées ou
  gardées. Il attend la contre-lecture 3, limitée aux parties touchées et aux deux annexes, par un sous-agent neuf qui n'a
  écrit ni les brouillons ni les rapports, d'un autre modèle que le rédacteur du brouillon 3 (R2), les corrections, puis le scellement par `controle_ia.prereg.sceller_prereg` et la
  recopie sous `prereg/organisme-idees-juge-validation-allocation-blocs-vN.md`. **Aucun jeu avant.** Rien n'est adopté par ce texte.
- **Ce qui l'exige** : décision de la mère après le verdict de l'idée 1.2 (R-3008) : « aucune adoption avant une validation
  propre ». Le verdict nomme lui-même ce nœud : adopter l'allocation au juge « changerait sa conception gelée […] : modification
  du juge, à décider sur le résultat, **avec sa propre validation** » (verdict, § 5, citant [T] l. 534-538).
- **Documents qui font foi** (chemin + empreinte entière, chacune recalculée par `sha256sum` à 01:06Z) :
  - verdict de l'idée 1.2 : `docs/notes/organisme-idees-juge-v1/verdict-idee-1-2-v1/verdict-idee-1-2-v1.md`
    (`3b08f061d82687314efb72e595d92cb7cb3ac639d08f05e181e69070b1362b63`), ci-dessous **[V]** ;
  - préenregistrement de l'idée 1.2 : `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md`
    (`bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e`), ci-dessous **[T]**, lignes « l. n » ;
  - son addendum de relance : `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-relance-v1.md`
    (`632a897944c1c36e8c7b3e2b078e1a4e1ed8bd0489379f10391c191404ed4f55`), ci-dessous **[AR]** ;
  - son addendum d'empreintes (lu pour les noms du code et la durée, § 1 à 5) :
    `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4-addendum-empreintes-v1.md`
    (`1b96cf065cef40ed9e452611b107d9f40f598091c8a591f2397bf58e7c92beee`), ci-dessous **[AE]** ;
  - pièces que [T] cite et que ce texte reprend par renvoi, **non relues par moi** (empreintes seulement recalculées) : preuve
    `docs/notes/organisme-idees-juge-v1/preuve-validite-nul-limite-v1.md` (`44f249409193778ccbaaa12b6c5e74d64434dfb87be77382d8bb9438459281b2`),
    **[PREUVE]** ; contre-lecture de la v1 de [T] `docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-tirages-repartis-v1.md`
    (`5ae17f81cbeb83161e49d7d3ce5c8fa4ff38c4db9d38afd7cfc5b8ae676df109`), **[CL]** ; décisions
    `docs/decisions/decision-N-058-v1.md` (`854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d`) et
    `docs/decisions/decision-N-067-v1.md` (`966dd9dc3fae61cbe1f10ee2a54f401ddf7af5041eeaacd81ad9f8b264661589`) ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` et validateur `src/controle_ia/prereg.py` (sections exigées).
- **Format seulement** (R-3008, consigne de la mère) : j'ai vérifié par leurs compagnons, puis lu les **noms des clés de premier
  niveau** de `runs/20261116-140942-idee-1-2-tirages-repartis-v1/manifeste.json` et des cinq fichiers de
  `diag/organisme-idees-juge-v1/20261116-140942-idee-1-2-tirages-repartis-v1/` (`manifeste_sha256`, `resultat`, `run_id` ; manifeste :
  `commande`, `commit`, `config`, `config_sha256`, `cree_le`, `decisif`, `depot_propre`, `graines`, `preenregistrement`,
  `reserves`, `run_id`, `versions`). **Aucune valeur** de ces fichiers n'est lue ni employée ; **aucun seuil n'en vient**. Tout
  chiffre de résultat cité ici vient de [V], par paragraphe.

## Hypothèse

**Contexte.** [V] prononce, sur le banc B v2 de [T], « gain de structure » pour l'allocation par blocs avec arrêt anticipé
(bras A) contre la part fixe de 200 tirages par carte (bras F) : générations couvertes 86,1 % contre 41,3 %, différence appariée
+0,448 (borne basse +0,413), fausses promotions 0,0027 contre 0,0013 par génération (borne haute de la différence +0,004),
validité tenue (0 génération avec promotion sur 500 dans chacun des sept bras) ([V] § 2 et § 4). Il l'assortit de six réserves
([V] § 5, « Réserves de l'issue ») et de quatre réserves de propreté R-1 à R-4 ([V] § 3.6). Ce texte ne revient pas sur le
prononcé : il demande si le même gain **se retrouve** sur des tirages que personne n'a vus, sur un banc construit pour attaquer
ces réserves, avant que la mère ou Lazar n'envisagent une adoption.

**H-V (hypothèse de validation).** À nombre total de tirages frais au plus égal par génération, sous le nul de production (v8),
le juge à allocation par blocs avec arrêt anticipé (bras A de [T], **inchangé**) :
1. **réplique** le gain de [V] sur des données neuves d'une composition identique à celle du banc lu (six porteuses sur
   vingt-quatre cartes), à des doses neuves ;
2. **le garde quand la redondance disparaît** : une seule porteuse par génération (la réserve R-4 de [V] dit que le « 0 génération
   perdue » de A contre F tient aux six porteuses) ;
3. **ne nuit pas** quand la composition change : douze porteuses sur vingt-quatre (budget libéré plus rare, réserve R-2) ; aucune
   porteuse, monde hors de la classe, cartes « copies par morceaux » nombreuses (la seule sorte de fausse promue sous A dans [V],
   § 3.4) ;
4. **garde sa validité**, lue cette fois aussi sur le rapport exact Λ au temps d'arrêt, qui voit, sur les cartes voisines du monde (les seules où il n'est pas écrasé vers 0), ce que les lectures sur la
   richesse W ne voient pas (réserves R-1 et 3 de [V]).

**Hypothèses de travail.** (i) La garantie de [T] (lemme et théorème 2) vaut pour toute règle d'allocation écrite d'avance et non
anticipante ; elle n'est pas remise en cause ici, elle est **éprouvée** plus durement. (ii) Le banc reste un banc : composition
choisie par construction ; la famille « dense » et la famille « vide » élargissent le domaine, sans le rendre égal à une génération
réelle (réserve 1 de [V], gardée). (iii) Le gain se place près du seuil de détection ; [V] § 4 le confirme dans un sens que [T]
n'attendait pas : il est **plus fort sur les composantes faibles** (dose basse +0,619 contre dose haute +0,277).

**Renvois.** [T], section « Hypothèse » (H-1.2) ; [V] § 5, « Ce qui suit » ; voie bon marché approuvée par Lazar (N-045 v2,
cité par [T]). **Ce n'est pas une revendication** : le principe (processus de valeurs e à arrêt optionnel) est publié ([T],
section « Garantie », voisins lus sur PDF par [CL]) ; ce texte ne cite aucun chiffre de l'état de l'art (R7).

## Prédiction chiffrée et signe attendu

Écrites avant tout jeu, sans pilote. Chaque chiffre de la colonne « origine » vient de [V], par paragraphe. « Couverture » :
part des générations où au moins une **porteuse au sens de l'oracle** est promue (définition de [T], inchangée). « Rappel par
porteuse » : part des porteuses (au sens de l'oracle) promues, toutes générations d'une famille réunies. Familles : section
« Plan d'analyse ».

| # | prédiction | signe | chiffre | origine dans [V] | ce qui la réfute | confiance |
|---|---|---|---|---|---|---|
| P1 | **réplique** : C_A − C_F, famille « réplique » | + | ≥ +0,05, borne basse > 0 ; estimation attendue entre +0,20 et +0,50 (doses neuves plus hautes en moyenne : plafond plus proche) | +0,448 [+0,413 ; +0,484], § 2 | borne haute < +0,02 | 0,75 |
| P2 | **porteuse unique** : C_A − C_F, famille « porteuse unique » | + | ≥ +0,05, borne basse > 0 ; estimation attendue entre +0,10 et +0,40 | mécanisme § 3.1 (porteuses 335,6 tirages sous A) ; perte par carte § 3.2 | borne haute < +0,02 ; ou borne haute < 0 (« nuisible ») | 0,55 |
| P3 | **perte par porteuse** : part des porteuses promues par F et non par A, dans chaque famille à porteuses | ≈ 0 | ≤ 0,03 dans chaque famille | 56 cartes (55 porteuses arrêtées bas, une au plafond) sur 4 483 porteuses au sens de l'oracle (§ 1 : 4 500 porteuses construites, dont 17 sans gain), soit ≈ 0,0125, § 1 et § 3.2 | > 0,05 dans une famille | 0,65 |
| P4 | **rappel par porteuse** : R_A − R_F | + | borne basse > 0 dans « réplique » et « porteuse unique » ; ≥ 0 (ponctuel) dans « dense » | § 3.1, § 3.2 | borne haute < 0 dans une famille | 0,6 |
| P5 | qualification, famille « réplique » : A contre la part fixe à 250 tirages (F125) et contre le placebo (P) | ≥ 0 ; + | « de structure » : borne haute de C_A − C_F125 ≥ 0 et borne haute de C_A − C_P > 0 | A − F125 +0,353 ; A − P +0,281, § 4 | l'une des deux qualifications contraires prononcée | 0,6 |
| P6 | **forme de dose** (clause de Q3 de [T], prise dans le sens que [V] a trouvé) : gain A − F à la dose basse moins gain à la dose haute, famille « réplique » | + | ≥ +0,10 (ponctuel) | +0,619 contre +0,277, § 4 | différence ≤ 0 | 0,65 |
| P7 | fausses promotions au sens de l'oracle, familles « réplique », « porteuse unique », « dense » | 0 ou + faible | ≤ 0,01 par génération dans chaque bras ; borne haute de FP_A − FP_F ≤ +0,05 | 0,0013 à 0,004, § 1 et § 3.4 | borne basse de FP_A − FP_F > +0,02 (et, pour « dense », borne basse de FP_A seul > 0,05) | 0,7 |
| P8 | fausses promotions, famille « vide » (aucune porteuse, huit copies par morceaux) | 0 ou + faible | FP_A ≤ 0,05 par génération ; borne haute de FP_A − FP_F ≤ +0,05 | seule sorte fausse promue : copies par morceaux, § 3.4 | borne basse de FP_A − FP_F > +0,02 ; ou borne basse de FP_A seul > 0,05 | 0,5 |
| P9 | économie de l'arrêt seul (F-arrêt) | + | « réplique » ≥ 0,25 ; « dense » plus basse que « réplique » d'au moins 0,05 (ponctuel) | 0,568 [0,564 ; 0,572], § 2 | « réplique » < 0,10 ; ou « dense » ≥ « réplique » | 0,7 |
| P10 | mécanisme : tirages moyens reçus par une porteuse sous A | + | « réplique » ≥ 300 ; « porteuse unique » ≥ 400 ; « dense » entre 200 et 300 | 335,6, § 3.1 | « réplique » < 230 ; « porteuse unique » < 300 ; « dense » hors de 200 à 300 | 0,55 |
| P11 | **validité**, famille « nul », lectures (1) à (3) de [T] | nul | ≤ 13 sur 500 dans chacun des sept bras ; aucun membre exact promu ; aucune domination franchie ; moyennes ponctuelles des valeurs e ≤ 0,8 | 0 sur 500 ; moyennes 0,05 à 0,09, § 2 et § 3.6 | un bras ≥ 39 sur 500 ; une domination franchie ; une borne basse > 1 | 0,85 |
| P12 | **validité, lecture neuve (5)** : moyenne du rapport exact Λ au temps d'arrêt, famille « nul », par bras, sorte « voisines du monde » (autres sortes et toutes cartes réunies : rapportées sans critère) | ≤ 1 | aucune borne basse > 1 | réserve 3 de [V] (fuite d'instants invisible sur W) | une borne basse > 1 | 0,85 |
| P13 | **serrage, jeu synthétique neuf** : moyenne de Λ au temps d'arrêt sous chaque règle saine (F, F-arrêt, A, P, P′, G) | = 1 | intervalle à 95 % contenant 1 pour chaque règle ; mutation « la règle lit le bloc suivant » : borne basse > 1 | [V] R-1 ; [CL] : 1,267 pour cette règle à la distance de [T], cité par [T] l. 211-212 ; annexe A : ≈ 1,014 à la distance retenue, borne basse attendue ≈ 1,013 | une règle saine dont la borne basse dépasse 1 ; mutation non tuée | 0,8 |
| P14 | **sensibilité de l'épreuve de validité** (rapportée, sans critère) : plus petit facteur c d'inflation des valeurs e (e × c) que la lecture (1) déclare « non tenue » sur la famille « nul » | — | attendu : c de l'ordre de 17 ou plus (borne de Markov pour une promotion à une seule carte : avec des moyennes de valeurs e d'au plus 0,09 et 24 cartes, au plus 0,0045 c par génération, soit 39 sur 500 à partir de c ≈ 17 ; ordre de grandeur pour une promotion isolée seulement : pour k cartes promues ensemble la même borne vaut pour chaque k et la réunion sur k jusqu'à 24 la multiplie jusqu'à 24, donc ce chiffre n'est pas une borne basse sur c ; rapporté sans critère) | [V] R-1 | — (information) | 0,5 |

**Ce que serait chaque issue (R3).** P1, P2, P5 vraies et rien de « nuisible » : le gain de [V] se réplique et survit à la fin de
la redondance (validation tenue, au banc). P1 vraie, P2 fausse : le gain dépend de la redondance des porteuses ; l'allocation aide
quand plusieurs cartes portent la même chose, pas quand une seule la porte (validation partielle). P1 fausse : [V] ne se réplique
pas sur des tirages neufs ; audit de symétrie et nœud. P3 ou P4 fausses : l'arrêt bas tue des porteuses (le piège nommé par la
fiche) au-delà de ce que [V] a mesuré. P7 ou P8 fausses : l'allocation promeut des fausses (critère « nuisible »), surtout si les
tirages libérés vont aux copies par morceaux. P9 fausse : l'économie de [V] tenait à la composition. P11, P12 ou P13 fausses :
défaut de code ou de preuve. P14 grand : l'épreuve de validité au banc est peu sensible, ce que [V] R-1 disait ; dit au rapport,
sans effet sur la table.

## Métrique

Toutes les définitions de [T], section « Métrique », valent **telles quelles** (génération ; budget B = 24 × 200 = 4 800 tirages
frais ; « au plus B » pour A, P, P′, F-arrêt, G ; F à B exactement ; F125 à 6 000 ; promotion par la règle de Benjamini et
Hochberg sur valeurs e, m fixé à 24, α = 0,05 ; valeur e = trajectoire tronquée à son dernier instant révélé, arrêtée au premier
instant où elle atteint m/α ; oracle à 20 000 instances calculé avant le rejeu ; classes porteuse, porteuse sans gain, fausse,
partiellement vraie ; couverture C_X avec Clopper-Pearson à 95 % ; différences appariées par intervalle percentile à 95 % sur
10 000 rééchantillonnages des générations, test exact de McNemar rapporté ; fausses promotions FP_X par génération, par sorte ;
consommation, économie, tirages reçus par sorte et par classe ; lectures de validité (1) à (4)). Ajouts :

- **Rappel par porteuse R_X** (familles à porteuses) : nombre de porteuses promues sur nombre de porteuses, toutes générations de
  la famille réunies. Différence appariée R_A − R_F : intervalle percentile à 95 % par rééchantillonnage **des générations**
  (une génération emporte toutes ses porteuses), 10 000 rééchantillonnages. **Perte par porteuse** : part des porteuses promues
  par F et non par A ; **gain par porteuse** : l'inverse ; rapportés avec leur tableau croisé par carte (traite R-4 de [V]).
- **Validité, lecture (5) — rapport exact au temps d'arrêt** (famille « nul ») : pour chaque carte et chaque bras, Λ au dernier
  instant révélé par le bras (ou au premier instant d'arrêt haut), Λ calculé par le banc sur la loi connue du monde (comme pour la
  domination de [T]) ; moyenne par bras, sur la sorte « voisines du monde » (sept intervalles ; toutes cartes réunies et autres sortes rapportées sans critère), intervalle percentile à 95 % par
  rééchantillonnage des générations. Λ est une martingale positive de moyenne 1 sous le monde ; un temps d'arrêt borné et non
  anticipant la garde à 1 ; une règle qui lit un instant non révélé la pousse au-dessus ([CL], cité par [T] l. 211-212). Cette
  lecture voit donc une fuite d'instants que les lectures sur W ne voient pas (réserve 3 de [V], [T] l. 316-318), **mais seulement là où Λ n'est pas écrasé vers 0** : pour une carte sans lien avec le monde, Λ vaut presque toujours une valeur minuscule, sa moyenne égale à 1 ne vient que d'événements rarissimes et la moyenne observée sur 500 générations reste très sous 1 ; toutes cartes réunies, la lecture ne pourrait donc rien voir. Elle est jugée sur la sorte « voisines du monde » seule. **Pouvoir déclaré, joué après le jeu sur les mêmes trajectoires** : la mutation « la règle lit le bloc suivant » est rejouée sur le bras A de la famille « nul » ; si la borne basse de la moyenne de Λ sur les voisines du monde ne dépasse pas 1, la lecture (5) est déclarée « sans pouvoir sur le banc réel », rapportée sans critère, et la réserve 3 de [V] reste portée par le seul serrage.
- **Serrage, jeu synthétique neuf** (sans juge) : monde jouet construit comme celui du jeu synthétique de [T] (Métrique, réserve
  (a) ; écart E-2 de [AE] : lois et issues tirées par génération), **graines neuves `(98, g)`**, 20 000 générations ; pour chaque
  règle saine (F, F-arrêt, A, P, P′, G), moyenne de Λ au temps d'arrêt et intervalle percentile à 95 % (10 000 rééchantillonnages) ;
  mutation « la règle lit le bloc suivant avant de décider » jouée sur le même jeu : **la règle G lit le bloc suivant**
  (chaque bloc va à la carte dont log W **après** ce bloc sera la plus grande, comme la règle gloutonne qui anticipe du
  programme de [CL], annexe A), Λ lu à son temps d'arrêt ; une mutation qui ne jouerait que sur les arrêts de A est sans
  pouvoir sur ce jeu (annexe A) et n'y sert pas. Les 24 cartes du monde jouet sont des **voisines proches**, à la distance
  fixée **dans ce texte, annexe A** : bruit d'amplitude ε_i de 0,01 à 0,03 (24 valeurs régulièrement espacées, au lieu de
  0,10 à 0,30 dans le jeu de [T]), tout le reste du monde jouet inchangé. À cette distance, comptée sans donnée du juge, la
  variance de Λ au plafond est finie et lisible (médiane 0,15, maximum 32 sur 480 000 cartes d'essai, contre une médiane de
  6,4·10⁵ à la distance de [T]), la demi-largeur attendue de l'intervalle d'une règle saine est d'environ 0,0007 sur
  20 000 générations et la moyenne attendue de la mutation d'environ 1,014 (borne basse attendue ≈ 1,013) : la lecture
  demande des queues qui ne soient pas trop lourdes.
- **Sensibilité graduée** (famille « nul », rapportée sans critère) : mutations « valeur e multipliée par c » pour
  c ∈ {2 ; 4 ; 8 ; 16 ; 32 ; 64 ; 128}, jouées sur les trajectoires rejouées, après la lecture saine ; pour chaque c, lectures (1) et (3) ;
  rapport : plus petit c « non tenu » par la lecture (1), plus petit c dont une borne basse de moyenne dépasse 1 (« aucun jusqu'à 128 » si la grille ne l'atteint pas).
- **Arrêts réels et étiquettes** (réserve 5 de [V] ; [AE] lecture 21) : le code consigne séparément l'**arrêt réel** (bas, haut,
  plafond, fin de budget) des bras qui ont une règle d'arrêt (A, F-arrêt, P et P′ en première phase) et l'**étiquette de fin de
  trajectoire** (valeur sous le seuil bas, sans arrêt) ; une carte qui reprend sous P ou P′ est comptée « reprise ». Seuls les
  arrêts réels se comparent d'un bras à l'autre.
- Rapportés par famille, par cellule (type de composante × dose) et réunis par famille ; **aucune réunion de familles** pour un
  critère ; aucune moyenne ni médiane sur des jetons (il n'y en a pas).

## Seuil

- **Juge et règles des bras** : ceux de [T], section « Seuil » et « Bras », **inchangés** (nul v8 de l'archive ; α = 0,05 ; m = 24 ;
  blocs de 25 ; instants = fins de blocs ; plafond de 800 ; arrêt bas log W < log(1/20) après au moins 50 tirages ; arrêt haut
  log W ≥ log(m/α)). Changer une règle de A ici ferait valider autre chose que ce que [V] a lu.
- **Validité, lecture (1)** (famille « nul », 500 générations, sept bras F, F-arrêt, A, P, P′, F125, G) : niveau 0,05/7, test
  binomial exact au taux 0,05 : « tenue » ≤ 13 sur 500, « non tenue » ≥ 39, « non jugeable » de 14 à 38 ([T], annexe B ; recalculé
  par moi à 01:06Z, même script, même sortie pour sept bras ; huit bras donneraient les mêmes bornes).
- **Validité, lectures (2), (3)** : celles de [T] (domination à 10⁻⁶ ; 49 intervalles désignés, sept par bras et quarante-deux par
  sorte et par bras ; une borne basse > 1 = défaut ; sans correction, fausse alerte du côté prudent).
- **Validité, lecture (5)** : une borne basse de moyenne de Λ au temps d'arrêt, sorte « voisines du monde », > 1 dans un bras (sept intervalles) = défaut, sauf si la lecture est déclarée « sans pouvoir sur le banc réel » (alors rapportée sans critère, avec l'audit écrit) ; sans
  correction (du côté prudent).
- **Serrage (jeu synthétique)** : pour une règle saine, une borne basse > 1 = défaut ; une borne haute < 1 = **audit écrit** (erreur
  de calcul de Λ ou queue trop lourde), non un défaut ; la mutation « bloc suivant » doit avoir une borne basse > 1, sinon elle
  survit et la liste d'arrêt dit « pas de jeu ». **Une alerte sur une règle saine** (borne basse > 1 ; probabilité de fausse alerte jusqu'à environ 14 % pour six règles à 95 %, du côté sûr) reçoit l'audit écrit et le nœud de la mère ; le serrage ne se rejoue que sous un addendum scellé, avec les mêmes graines `(98, g)` et le code corrigé, jamais avec d'autres graines (R3).
- **Principale par famille**, règle de [T] appliquée **séparément** aux familles « réplique » et « porteuse unique », dans l'ordre,
  la première vraie l'emporte : 1. « nuisible » si la borne haute de C_A − C_F < 0 ou la borne basse de FP_A − FP_F > +0,02 ;
  2. « gain » si la borne basse de C_A − C_F > 0, l'estimation ≥ +0,05 et la borne haute de FP_A − FP_F ≤ +0,05 ; 3. « pas de
  gain » si la borne haute de C_A − C_F < +0,02 ; 4. sinon « non tranché ».
- **Par carte** (familles « réplique », « porteuse unique », « dense ») : « nuisible par carte » si la borne haute de R_A − R_F < 0.
- **Familles « dense » et « vide »** : « nuisible » si la borne basse de FP_A − FP_F > +0,02, ou si la borne basse de FP_A seul dépasse 0,05 par génération (niveau nominal : une différence de +0,02 ne voit pas un décuplement de 0,003) ; pour « dense » aussi si la borne
  haute de C_A − C_F < 0. Le gain y est rapporté, sans critère, pour « dense » seulement (« vide » n'a ni couverture ni rappel), avec les bornes basses de C_A − C_F et de R_A − R_F ; « pas nuisible » y veut dire « tort non établi », non « innocuité établie à une marge près » : aucune marge de non-infériorité n'est écrite, c'est dit et lu ainsi au prononcé (la couverture de « dense » risque le plafond ; celle de « vide »
  n'existe pas).
- **Qualification** (famille « réplique » seulement, comme [T]) : « d'effectif seulement » si la borne haute de C_A − C_F125 < 0 ;
  « sans effet de ciblage » si la borne haute de C_A − C_P ≤ 0 ; « de structure » si aucune des deux ; les deux ensemble si les
  deux. Pour « porteuse unique », rapportée sans critère.
- **Zone utile** : C_F (réunie) dans ]0,05 ; 0,95[, exigée pour « réplique » et pour « porteuse unique », séparément.
- **Conjonction sans correction** : la validation exige « gain » dans deux familles ; chaque intervalle est à 95 % ; l'énoncé
  conjoint « gain dans l'une **et** dans l'autre » est un test d'intersection et d'union, de niveau 0,05 sans correction. Les
  lectures « nuisible » (jusqu'à douze intervalles sur quatre familles : 4 + 3 + 5) ne sont pas corrigées : une fausse alerte empêche une
  adoption, du côté prudent ; toute alerte reçoit l'audit écrit avant le prononcé.

## Plan d'analyse

### Données neuves : ce qui garantit qu'aucun tirage de [V] n'est rejoué

- **Racine neuve** : entier de l'empreinte sha256 du texte qui fera foi (celui-ci, une fois contre-lu et scellé) ; le code
  **refuse** la racine de [T] (entier de `bdabf2bc…`) et toute racine d'un autre texte que celui qu'il lit.
- **Clés neuves** : familles numérotées 10 à 14 (jamais 0 ou 1, clés de [T]) ; jeu synthétique `(98, g)` (jamais `(97, g)`).
- **Aucune lecture des sorties de l'idée 1.2** : le code n'ouvre rien sous `diag/organisme-idees-juge-v1/*-idee-1-2-*`,
  `runs/*-idee-1-2-*`, ni sous aucun dossier `/home/user/jeu-idee-1-2-*` (copie du run invalide, copie de la relance, journaux) ; garde de chemin et essai (cas sain et artefact, R5). Les
  trois fichiers du run invalide de [AR] § 2 restent non lus (règle de [AR] § 3, qui demeure).
- **Doses neuves** : aucune cellule de ce banc n'a la dose d'une cellule de [V] (ci-dessous). **Déclaré** : les doses sont choisies
  après lecture de [V] (couvertures de F par cellule, § 3.5 et § 4 : 0,09 à 0,19 aux doses basses, 0,44 à 0,80 aux doses hautes), pour
  rester dans la zone utile ; ce choix est fait avant tout tirage neuf et n'emploie aucune donnée du run. **Compte de dimensionnement, annexe B** (information en nats sur 200 épisodes des dix doses neuves, sans juge, comme l'annexe A de [T]) et couverture attendue de F par famille qui en découle, pour que le risque « hors de la zone utile » soit chiffré avant le jeu : les doses neuves basses portent 4,9 à 6,0 nats, les doses neuves hautes 12,8 à 15,8 nats (dose 1,0 de V2, V3 et V5 : 13,5 à 14,2 nats, pour 6,17, log 480, nécessaires à une carte seule : cellules de dose haute proches du plafond pour F) ; sous l'hypothèse déclarée que la couverture de F croît avec la dose dans chaque type, la couverture attendue de F en « réplique » est entre 0,41 et 0,87 environ, et celle de « porteuse unique » au plus celle de « réplique » : sous le seuil de 0,95 que la contre-lecture 2 fixait pour revoir les doses. **Les doses sont gardées** ; P1, P2 et P9, relues avec ce compte, ne changent pas.

### Banc neuf, dit « banc C v1 »

Le banc B v2 de [T] (espace K = 3 issues, D = 2 traits, G = 2 sous-populations ; lois softmax aléatoires ; archive A2 et ses
coupures |s| ≥ 0,3 ; lignes V1 à V5 ; gel des engagements avant les issues fraîches ; grammaire du juge vérifiée par
`selection_pari.valider_loi`), avec quatre changements :

1. **Doses neuves**, deux par type, dix cellules (cellule = g mod 10) : V1 {0,375 ; 0,625} ; V2, V3, V5 {0,6 ; 1,0} ; V4
   {0,15 ; 0,25}. « Dose basse » / « dose haute » : la plus petite / la plus grande des deux.
2. **Compositions neuves** (cinq familles, ci-dessous) : une seule porteuse ; douze porteuses ; aucune porteuse.
3. **Arrêts réels et étiquettes** consignés à part (Métrique).
4. **Lecture (5) et serrage** (Métrique) ajoutés aux lectures de validité.

### Familles

Les cartes sont construites comme dans [T] (familles T et N : règles des porteuses, des copies de la classe, des copies par
morceaux, des fausses construites sous la règle du cosinus avec son plafond de 1 000 tirages, des nulles ; V4 sans opposé).
Seule la composition change. **Répartition à l'intérieur des sortes, gelée ici (proposée par la contre-lecture 1 et retenue telle quelle ; aucune autre répartition n'est permise)** : copies de la classe, des mélanges de Dirichlet et des lois tempérées et inclinées en parts égales, l'éventuelle carte en plus étant un mélange (« porteuse unique », sept : 4 + 3 ; « dense », quatre : 2 + 2 ; « vide », six : 3 + 3) ; copies par morceaux, les quatre constructions de [T] prises une fois chacune, puis la ou les cartes en plus tirées sans remise parmi elles par la clé `(famille, g, 3001)` (« porteuse unique », cinq : les quatre plus une ; « dense », trois : trois des quatre) ; fausses construites, comme en famille T les quatre premières sous la règle du cosinus et les deux dernières opposées à force × 1 et × 0,5, les cartes en plus étant sous la règle du cosinus (« porteuse unique » et « vide », huit : six sous la règle du cosinus et deux opposées ; « dense », quatre : trois sous la règle du cosinus et une opposée à force × 1) ; **pour V4**, où l'opposé n'est pas une loi de la grammaire du juge, toutes sous la règle du cosinus. Le classement final de chaque carte est celui de l'oracle.

| famille (clé) | générations | monde | 24 cartes | ce qu'elle éprouve |
|---|---|---|---|---|
| « nul » (10) | 500 : monde M₀ (mélange des lois d'archive) pour g < 250, M₀′ (loi d'archive tempérée et inclinée, base parmi S1 et S2) pour g ≥ 250 | dans la classe du nul | composition de la famille N de [T] : 8 voisines, 8 membres exacts, 2 porteuses construites, 2 copies par morceaux, 2 fausses construites, 2 nulles | validité, lectures (1) à (5) ; sensibilité graduée |
| « réplique » (11) | 750 (75 par cellule) | S1 portant la composante de la cellule | composition de la famille T de [T] : 6 porteuses (M ; M × 0,5 ; M × 1,5 ; M à direction bruitée ; deux doublons), 6 copies de la classe, 4 copies par morceaux, 6 fausses construites, 2 nulles | réplique de [V] sur tirages et doses neufs |
| « porteuse unique » (12) | 750 (75 par cellule) | idem | 1 porteuse, tirée uniformément parmi M, M × 0,5, M × 1,5, M à direction bruitée (clé de construction) ; 7 copies de la classe, 5 copies par morceaux, 8 fausses construites, 3 nulles | fin de la redondance (R-4) |
| « dense » (13) | 500 (50 par cellule) | idem | 12 porteuses (trois de chacune des quatre constructions, chacune bruitée comme un doublon, poids + 0,01·N(0, 1)) ; 4 copies de la classe, 3 copies par morceaux, 4 fausses construites, 1 nulle | budget libéré rare (R-2) ; perte par carte |
| « vide » (14) | 500 (50 par cellule) | idem (hors de la classe) | aucune porteuse ; 6 copies de la classe, **8 copies par morceaux** (les quatre constructions de [T], deux fois, chacune bruitée comme un doublon), 8 fausses construites, 2 nulles | fausses promotions quand tout le budget libéré va aux non porteuses (R-4 de l'issue : copies par morceaux non garanties) |

Total : 3 000 générations, 72 000 cartes. Dimensionnement : à 750 générations, [V] § 2 donne un intervalle de C_A − C_F de
largeur ≈ ±0,035 ; un gain de +0,10 en « porteuse unique » se lirait donc avec une marge de près de trois fois sur le seuil
« borne basse > 0 ». La famille « nul » garde 500 générations pour garder les seuils de [T] (13 et 39).

### Bras

Ceux de [T] (F, F-arrêt, A, P, P′, F125, G), mêmes règles, même code de rejeu (`rejeu_v1.py`, gelé par [AE]), joués sur les
mêmes trajectoires dans chaque génération ; G pour la validité seulement (famille « nul »). Aucune règle neuve.

**Question ouverte Q-1, proposée à la mère (non tranchée ici) : essai de concordance d'un juge candidat.** Une adoption
remplacerait `juger_carte` par une fonction qui juge une génération entière. Proposition : écrire, sous un nom neuf et hors
production, un juge candidat qui révèle les issues **à la demande**, bloc par bloc, depuis le flux de chaque carte (sans tirer
d'avance les 800 issues), et le jouer sur 25 générations de la famille « réplique » et 25 de la famille « nul » ; il doit rendre,
carte par carte, les mêmes tirages, les mêmes valeurs e (à 10⁻¹² près) et les mêmes promotions que le rejeu du bras A ; sinon
arrêt (défaut). Pour : éprouve la réserve (iii) de [T] (rejeu équivalent à une révélation à la demande) sur le code qu'on
adopterait. Contre : jusqu'à 32 évaluations par carte, ≈ 1 à 1,5 heure de plus ; le montage reste celui du banc (plan « ordre
naturel », m = 24), non celui de production. Recommandation du rédacteur : l'inclure (confiance 0,6). **Condition écrite
d'avance, valable seulement si la mère retient Q-1** (défaut M3' de la contre-lecture 2) : le juge candidat tire les issues
de chaque carte bloc par bloc depuis le flux `(f, g, i, 2)` de la carte, par le même appel au générateur que le banc (même
méthode, mêmes arguments, même ordre), de sorte que 32 tirages de 25 issues consomment le générateur exactement comme le
tirage d'un coup des 800 issues du rejeu ; un essai le vérifie avant la concordance (cas sain : les 800 issues tirées par
blocs égales, une à une, aux 800 tirées d'un coup ; artefact : un bloc tiré par une autre méthode est refusé) ; sinon arrêt,
défaut de montage et non de l'allocation.

### Graines (R9)

Racine : entier de l'empreinte du texte qui fera foi. `numpy.random.SeedSequence(entropy=racine, spawn_key=…)`, mêmes formes de
clés que [T] l. 451-456 avec les familles 10 à 14 : monde `(f, g, 24)` ; archive `(f, g, 25)` ; construction de la carte i
`(f, g, i, 0)` ; plan, entraînement `(f, g, i, 1)` ; issues fraîches `(f, g, i, 2)`, tirées après le gel de tous les engagements de
la génération ; positions `(f, g, 1001)` ; placebo `(f, g, 1000)` ; oracle `(f, g, 2000)` ; choix de la porteuse unique
`(12, g, 3000)` ; choix des copies par morceaux `(12 ou 13, g, 3001)` ; rééchantillonnage `(99, b)` ; jeu synthétique `(98, g)` ; mutations graduées sans hasard. Manifeste du run
(`src/controle_ia/manifeste.py`) ; versions consignées (interpréteur, numpy, scipy), comme [AR] § 4.2.

### Étapes

0. Code sous des noms neufs (R12), par exemple `src/controle_ia/organisme_idees_juge/banc_validation_allocation_v1.py`,
   `synthetique_v2.py`, `execution_validation_allocation_v1.py`, `lire_validation_allocation_v1.py`, lanceurs
   `scripts/jouer_validation_allocation_v1.py` et `scripts/lire_validation_allocation_v1.py` ; les modules gelés par [AE]
   (`lois_v1`, `juge_v1`, `rejeu_v1`, `oracle_v2`…) sont importés **sans modification**. Essais (R5 : cas sain et artefact pour
   chaque ligne de la liste d'arrêt) ; banc de mutations : celles de [T] l. 462-466, plus : racine de [T] acceptée ; clé de
   famille 0 ou 1 ; lecture d'un chemin de l'idée 1.2 ; Λ pris au plafond au lieu du temps d'arrêt ; étiquette comptée comme
   arrêt réel ; règle G qui lit le bloc suivant (tuée par le serrage : Métrique, annexe A) ; toutes tuées pour la raison attendue. Contre-lecture du code
   par un autre modèle ; addendum d'empreintes scellé.
1. **Essai à blanc chronométré, sans lecture** (racine d'essai, jamais la racine du texte ; dix générations par famille) : il
   donne la durée attendue ; si la durée projetée (règle ci-dessous, contrôles et serrage compris) dépasse 12 heures, les familles « réplique » et « porteuse unique » passent
   à leurs 500 premières générations (g de 0 à 499, 50 par cellule ; mêmes tirages que les 500 premières des 750, les clés étant par génération). **Règle écrite ici, avant tout tirage du jeu** : durée projetée = somme, sur les cinq familles, du nombre de générations multiplié par la durée moyenne mesurée par génération de la famille (bras, rejeu et oracle compris), plus la durée des contrôles, de l'essai E1, du jeu synthétique et du serrage, mesurée ou extrapolée par l'essai à blanc, et comptée pour au moins 1 heure ; la décision ne dépend que de cette durée, se consigne au registre avant le jeu et ne change aucun seuil ni aucun critère. L'essai à blanc se joue **après** le scellement de ce texte et de l'addendum d'empreintes (le code n'existe qu'à partir de là, voir l'en-tête) et avant le jeu, jamais avant le scellement.
2. Contrôles avant jeu (empreintes, essais, mutations, aucune sortie existante, espace disque ≥ 1 Go après copie, [AR] § 4.4).
3. Essai E1 de [T] (préfixes), sur 50 cartes prises dans les cinq familles et dans les deux mondes de la famille « nul » (la
   lettre de [AE] lecture 14 n'essayait que M₀ et V1).
4. Jeu synthétique neuf et serrage ; arrêt si une règle saine sort en défaut ou si la mutation survit.
5. Oracle calculé et scellé pour toutes les générations, **avant** le rejeu des bras.
6. Jeu : 3 000 générations, `nice -n 10`, deux processus de calcul au plus, depuis une copie propre et détachée d'un commit noté,
   sous un nom neuf qui ne commence pas par `jeu-idee-1-2-` (sinon la garde de chemin l'arrêterait) ; consigne de [AR] § 5 (une tâche active pendant tout le jeu, attente réarmée avant la limite de l'outil).
7. Sortie scellée avant toute lecture, sous `diag/organisme-idees-juge-v1/` (dossier neuf), recopiée dans le dépôt et vérifiée par
   ses compagnons.
8. Lecture gelée (code scellé), puis lecteur neuf (R13), qui n'a écrit ni ce texte ni le code ni [V] ; audit de symétrie (R4)
   écrit avant le prononcé.

### Comparaisons et corrections

Principales : A contre F en « réplique » et en « porteuse unique » (conjonction, test d'intersection et d'union) ; conditions
« nuisible » dans les quatre familles hors « nul » ; qualification en « réplique ». Validité : Bonferroni sur sept bras pour la
lecture (1) ; lectures (2), (3), (5) et serrage sans correction (un dépassement suffit). Rapportés sans critère : cellules, sortes,
classes d'oracle, P6, P9, P10, P14, A − P′, qualifications hors « réplique », lectures par monde de la famille « nul ».

### Les réserves de [V], une à une

| réserve de [V] | ce que fait ce texte | où |
|---|---|---|
| R-1 (validité à 0 sur 500, conservatrice, ne prouve pas la garantie serrée) ; réserve 3 de l'issue | lecture (5) sur Λ au temps d'arrêt (sorte « voisines du monde » seule jugée : ailleurs Λ est écrasé vers 0 et la lecture est sans pouvoir ; pouvoir rejoué après le jeu), qui ne profite pas du conservatisme du certificat ; serrage sur jeu synthétique neuf (moyenne de Λ égale à 1 sous règle saine, mutation « bloc suivant » tuée) ; sensibilité graduée e × c rapportée : elle dit combien d'inflation l'épreuve laisserait passer | Métrique ; Seuil ; P12 à P14 |
| R-2 et réserve 1 (banc peu porteur, 18 sur 24 ; ne se transpose pas) | familles « porteuse unique », « dense », « vide » ; aucune réunion de familles ; **ne se transpose toujours pas** à une génération réelle (composition choisie par construction) : dit, gardé | Familles ; Critères |
| R-3 (A consomme moins que B ; comparaison à F125 et P avec leur consommation) | consommations rapportées par famille ; la principale reste « au plus B » ; F125 et P lus avec leurs tirages réels | Métrique ; Critères |
| R-4 (« 0 génération perdue » dû à la redondance) | famille « porteuse unique » ; rappel par porteuse, perte et gain par porteuse avec tableau croisé ; « nuisible par carte » est un critère | Métrique ; Seuil ; P2 à P4 |
| Réserve 2 (clause de dose de Q3 réfutée en signe) | prédiction P6 écrite dans le sens trouvé par [V], rapportée sans critère | Prédiction |
| Réserve 4 (fausses « copies par morceaux » mesurées, non garanties) | famille « vide » à huit copies par morceaux ; fausses promotions par sorte ; « nuisible » est un critère dans chaque famille ; **toujours non garanties** par le théorème hors de la classe : dit | Familles ; Seuil ; P8 |
| Réserve 5 (parts d'arrêts sous F, P, P′ : étiquettes) | arrêts réels et étiquettes consignés à part, reprises comptées ; seuls les arrêts réels se comparent | Métrique |
| Réserve 6 (run invalide de 00:29Z) | aucun tirage, aucune sortie, aucune valeur de l'un ou l'autre run de l'idée 1.2 n'entre ici ; racine et clés neuves ; garde de chemin ; les trois fichiers du run invalide restent non lus | Plan (données neuves) ; Liste d'arrêt |
| Non vérifié par [V] (commit `765acfc3…` portant l'addendum de relance ; liste du juge copiée) | le lanceur neuf contrôle la présence et l'empreinte du texte qui fera foi et de son addendum d'empreintes dans la copie, et recalcule les onze empreintes de la liste du juge (`0153e02d…`) avant le jeu | Étapes 2 ; Liste d'arrêt |

## Critères de lecture gelés

Première ligne qui s'applique :

| étage | observé | verdict |
|---|---|---|
| 1 | famille « nul » : une validité « non tenue » dans un bras ; un membre exact promu ; une domination franchie ; une borne basse > 1 dans l'un des 49 intervalles de la lecture (3) ou des 7 de la lecture (5) (sauf si elle est déclarée « sans pouvoir sur le banc réel » : voir Métrique) ; les alertes du serrage, jouées avant tout jeu, ne relèvent pas de cette table (liste d'arrêt : pas de jeu, aucun prononcé, audit écrit et nœud de la mère) | **« garantie mise en défaut »** : rien d'autre n'est lu ; audit ; nœud de Lazar ; **aucune adoption** |
| 1 bis | une validité « non jugeable » (14 à 38 sur 500) dans un bras | **« validité non établie »** : la suite est lue et rapportée sous cette réserve ; **aucune adoption ne peut s'en réclamer** |
| 2 | C_F (réunie) ≤ 0,05 ou ≥ 0,95 en « réplique » ou en « porteuse unique » | **« hors de la zone utile »** pour cette famille ; la validation est **« non concluante »**, **sauf** si une lecture « nuisible » de l'étage 3 est vraie en même temps (fausses promotions dans cette famille, ou toute lecture « nuisible » d'une autre famille) : l'étage 3 est alors prononcé aussi, car un tort constaté n'est jamais masqué par un manque de puissance ; le reste est rapporté |
| 3 | « nuisible » dans une famille (principale de « réplique » ou de « porteuse unique » ; « nuisible par carte » dans « réplique », « porteuse unique » ou « dense » ; fausses promotions ou couverture dans « dense » ; fausses promotions dans « vide ») | **« non validée : nuisible »** (famille et lecture nommées) |
| 4 | « gain » en « réplique » **et** en « porteuse unique », qualification « de structure » en « réplique » | **« validation tenue, au banc »** |
| 5 | « gain » en « réplique » et en « porteuse unique », qualification autre que « de structure » en « réplique » | **« validation tenue, gain » suivi de la qualification prononcée** (« d'effectif seulement », « sans effet de ciblage » ou les deux) : le gain de [V] se réplique mais **pas sa structure** |
| 6 | « gain » en « réplique », « pas de gain » ou « non tranché » en « porteuse unique » | **« validation partielle : gain lié à la redondance des porteuses »** ; aucune adoption ne peut s'en réclamer pour des générations à porteuse isolée |
| 7 | « pas de gain » en « réplique » | **« non répliquée »** : le gain de [V] ne se retrouve pas sur données neuves ; audit de symétrie renforcé (relecture du code de rejeu et du banc neuf) avant le prononcé |
| 8 | autre combinaison | **« non tranchée »** |

Étage rapporté en toute issue : économies, consommations, tirages reçus, arrêts réels, P6, P10, P14, cellules, sortes.

**Audit de symétrie (R4)**, écrit pour **toute** issue avant le prononcé : celui de [T] l. 495-500 (mécanisme, porteuses arrêtées
bas, partiellement vraies promues, cellule par cellule, « trop propre », « tout négatif »), plus : en « porteuse unique », **zéro
perte par porteuse** est un « trop propre » (la redondance n'y joue plus ; [V] § 3.2 a trouvé 56 pertes pour 4 483
porteuses-générations) ; une issue **égale à celle de [V] à la deuxième décimale** dans « réplique » est un « trop propre »
(doses neuves : un gain identique ferait chercher une fuite de données) ; en « vide », aucune fausse promotion dans aucun bras
alors que A donne jusqu'à 800 tirages aux copies par morceaux est un « tout négatif » à expliquer. Même relecture écrite du code de
rejeu et du banc neuf dans chacun de ces cas.

## Liste d'arrêt

| condition | action |
|---|---|
| toutes les lignes de [T] l. 506-515 (fichier gelé différent de l'addendum ; essai échoué ; mutation survivante ; essai E1 non égal ; issue fraîche tirée avant le gel ; lecture d'un instant non révélé ; tirages au-delà du budget ; domination franchie ; exception ou log W non fini ; durée murale > 24 h ; lecture avant scellement ou oracle après le rejeu ; dépense) | action de [T], inchangée |
| racine égale à celle de [T], ou clé de famille 0 ou 1 | arrêt avant tout tirage ; défaut |
| le code ouvre un chemin d'une sortie de l'idée 1.2 ou d'un dossier `/home/user/jeu-idee-1-2-*` | arrêt ; **run invalide** ; nœud |
| serrage : une règle saine à borne basse > 1 ; ou mutation « bloc suivant » non tuée | pas de jeu (défaut du côté sûr) ; aucun prononcé de la table ; audit écrit et nœud de la mère |
| essai de concordance du juge candidat (si Q-1 est retenue) : un tirage, une valeur e ou une promotion différent du rejeu du bras A | arrêt ; défaut |
| texte qui fait foi ou addendum d'empreintes absent de la copie, ou différent de son compagnon ; liste du juge différente de `0153e02d…` | pas de jeu |
| interpréteur ou versions différents de ceux consignés à l'addendum d'empreintes | pas de jeu |
| espace libre < 1 Go après création de la copie | pas de lancement (précaution, [AR] § 4.4) |
| arrêt venu de l'extérieur, sans fichier d'arrêt | run invalide ; aucune lecture partielle ; relance seulement sous un addendum neuf, mêmes tirages ([AR] § 5, même règle) ; après une seconde interruption, une machine hors de la session serait une dépense : devis et GO |
| toute machine louée, tout appel de modèle, toute dépense | interdit |

## Coût

**Processeur seul, 0 dollar (crédits : 0 ; hors crédits : 0) ; aucun devis n'est nécessaire.** Échelle prise de [V] (en-tête : durée murale 4,18 h, phase de jeu
3,19 h pour 30 000 cartes sur machine partagée, deux processus) : 72 000 cartes, soit ≈ 7,7 heures de jeu sous une charge
comparable ; oracle ≈ 1,2 heure (2,4 fois celui de [V], oracle écrit ≈ 30 min après les contrôles) ; contrôles, essai E1, jeu
synthétique, mutations graduées ≈ 1 heure ; juge candidat (si Q-1) ≈ 1 à 1,5 heure. **Total attendu ≈ 10 à 12 heures**, sous la
borne de 24 heures avec une marge de deux fois environ ; l'essai à blanc chronométré (étape 1, après le scellement, avant le jeu) le dit et peut, par la règle de l'étape 1,
réduire deux familles à 500 générations. Le jeu demande une session qui garde une tâche active pendant tout ce temps ([AR] § 5).
Écriture, contre-lectures, code, lecture : temps d'agents.

## Écarts, nœuds et ce que la validation ne décide pas

- **Écarts à un texte scellé** : aucun ; ce texte ne touche ni [T], ni [AE], ni [AR], ni le juge de production, ni la boucle.
  Différences de montage avec la production : celles de [T] (plan « ordre naturel », m = 24, issues tirées par le banc), gardées.
- **Nœud de Lazar, inchangé** ([T] l. 534-538 ; [V] § 6, nœud 1) : adopter l'allocation au juge changerait sa conception gelée
  (200 tirages et 8 instants par carte dans `juger_carte` et dans le texte scellé de la boucle réelle `80fe4f03…`). Ce texte ne
  fait que préparer la pièce qui manque à ce nœud ; même « validation tenue » n'adopte rien.
- **À porter avec ce nœud** ([V] § 6, nœud 2) : la condition « dénominateur fixe » de la synthèse des bassins étroits (§ 9) est
  levée par une preuve contre-lue.
- **N-058** : l'allocation sélectionne des **cartes** sur leurs valeurs e, jamais des **agents** ; les tirages reçus ne seront
  jamais rapportés par proposeur ni servis à un choix de proposeurs (garde reprise de [T]).
- **Ne décide pas** (liste de [T] l. 542-544, gardée) : l'effet sur la découverte ; les mondes riches à 8 traits ; les groupes de
  doublons ; le test de mort ; le gain en dollars ; l'économie dans une génération réelle. Ni le montage de production (« ordre
  secret », m = cartes jugées et plantées).
- **Questions ouvertes pour la mère** : Q-1 (juge candidat, ci-dessus) ; Q-2 : tailles des familles (3 000 générations) ou
  réduction d'avance à 500 pour « réplique » et « porteuse unique » (≈ 8 heures au lieu de 10 à 12) ; Q-3 : faut-il une sixième
  famille au montage de production (« ordre secret ») ou le laisser au nœud d'adoption — recommandation : le laisser (confiance 0,55).

## Contre-lecture

- **Contre-lecture 1** (R2) : **faite**, verdict « corrections » : cinq défauts majeurs (M1 à M5), onze remarques mineures
  (m1 à m11, dont m5 et m8 facultatives et recommandées) ; aucun « à refaire ». Lecteur : sous-agent neuf d'un autre modèle que
  le rédacteur du brouillon 1, qui n'a écrit ni ce brouillon, ni [T], ni ses addendums, ni [V]. Brouillon relu : brouillon 1,
  `docs/notes/organisme-idees-juge-v1/validation-allocation-blocs-v1/prereg-validation-allocation-blocs-v1-brouillon1.md`
  (`95f34a756c61b1f73df88cfa99350f9ffb741ad872a6afea90406e1f1acd6011`). Rapport :
  `docs/notes/organisme-idees-juge-v1/validation-allocation-blocs-v1/contre-lecture-validation-blocs-tour1-v1.md`
  (`c06813086fb63910cd240e1018fde7960d165f373cee5ff081d6228741cd4d3c`).
- **Traitement, brouillon 2** : par un rédacteur neuf, sous-agent de la session mère, qui n'a écrit ni le brouillon 1, ni le
  rapport, ni [T], ni ses addendums, ni [V] ; lettre de son modèle à inscrire par la mère au registre (il est du même modèle
  que le contre-lecteur 1). Les 29 couples du § 4 du rapport sont appliqués par le programme `appliquer-corrections-prereg-validation-allocation-blocs-v1-brouillon2.py` (même dossier,
  scellé), qui vérifie les deux empreintes ci-dessus, tire les couples du rapport par programme, exige que chaque « ancien »
  figure une seule fois et qu'aucun ne chevauche un autre, et refuse d'écraser ; quatre couples du rédacteur s'y ajoutent
  (titre, ligne « Brouillon 2 » et statut de l'en-tête, cette section). Différentiel :
  `differentiel-prereg-validation-allocation-blocs-v1-brouillon1-vers-brouillon2.diff` (même dossier, scellé). Rien d'autre
  ne change ; la « Déclaration » finale reste celle du rédacteur du brouillon 1.

**Réponse point par point.**

| point du rapport | couples | traitement |
|---|---|---|
| M1 (ordre : code, essai à blanc, scellement) | M1-a, M1-b | **acceptés**. M1-a reformulé : la durée projetée compte aussi les contrôles, l'essai E1, le jeu synthétique et le serrage, mesurés ou extrapolés par l'essai à blanc, pour au moins 1 heure (réserve du § 1 (4) du rapport : le serrage n'est pas chronométré). Si la mère tranche Q-2 pour 500 générations tout de suite, ces deux couples tombent et le texte dit 500 |
| M2 (lecture (5) sans pouvoir toutes cartes réunies) | M2-a à M2-f | **acceptés tels quels** (variante principale du rapport : jugée sur la sorte « voisines du monde », pouvoir rejoué après le jeu par la mutation « bloc suivant » sur le bras A de la famille « nul ») |
| M3 (« hors de la zone utile » masquait un tort) | M3 | **accepté tel quel** |
| M4 (compositions non gelées) | M4-a, M4-b | **acceptés**. La répartition proposée est retenue telle quelle ; la parenthèse « proposition du contre-lecteur ; toute autre répartition doit être écrite de la même façon » devient « proposée par la contre-lecture 1 et retenue telle quelle ; aucune autre répartition n'est permise », un texte gelé ne pouvant laisser une autre répartition ouverte. Vérifiée contre [T] (famille T : quatre fausses sous la règle du cosinus, deux opposées à force × 1 et × 0,5 ; pour V4, toutes sous la règle du cosinus ; quatre constructions de copies par morceaux) |
| M5 (annexe du serrage non écrite) | M5 | **couple accepté tel quel** ; **l'annexe A elle-même n'est pas écrite dans ce brouillon** : elle demande un compte (distance des voisines du monde jouet, variance attendue de Λ au plafond, borne basse attendue de la mutation « bloc suivant ») qui dépasse l'application de corrections ; à écrire dans un brouillon suivant, avant la contre-lecture 2, comme le couple le dit |
| m1 (garde de chemin trop étroite) | m1-a à m1-d | **acceptés tels quels** |
| m2 (dénominateur de P3) | m2-a, m2-b | **acceptés tels quels** |
| m3 (citation de § 4) | m3 | **accepté tel quel** |
| m4 (compte des intervalles « nuisible ») | m4 | **accepté, compte mis à jour** : m8, appliquée, ajoute une lecture « nuisible » en « dense » et une en « vide » ; le total devient douze (principales 4, par carte 3, « dense » 3, « vide » 2 : 4 + 3 + 5) au lieu des dix du couple |
| m5, facultative (fausse alerte du serrage et reprise) | m5 | **acceptée telle quelle** |
| m6 (grille de sensibilité) | m6-a à m6-c | **acceptés tels quels** |
| m7 (« ne nuit pas » sans marge) | m7 | **accepté, reformulé** : les deux parenthèses de suite sont écrites en phrase ; les bornes de R_A − R_F ne valent que pour « dense » (« vide » n'a pas de porteuse) |
| m8, facultative (décuplement des fausses promotions) | m8 | **acceptée telle quelle** |
| m9 (serrage et étage 1) | m9 | **accepté tel quel** |
| m10 (doses neuves non chiffrées) | m10 | **couple accepté tel quel** ; **l'annexe B n'est pas écrite dans ce brouillon** (même raison que l'annexe A) ; à écrire avant la contre-lecture 2 |
| m11 (seuils de réfutation de P10) | m11 | **accepté tel quel** |
| § 6 du rapport, points pour la mère | — | **non tranchés ici** (ils sont à la mère) : Q-1 et Q-2 à trancher avant le scellement, la ligne de la liste d'arrêt sur le juge candidat, les lignes du Coût et les questions ouvertes étant retirées ou gardées selon la réponse ; si Q-1 est retenue, écrire comment le juge candidat consomme le flux de chaque carte ; lettres des modèles à inscrire ; tâche d'attente prévue avant le lancement |

**Ce qui reste avant la contre-lecture 2** : annexe A (M5) ; annexe B (m10) ; réponses de la mère à Q-1 et Q-2 ; puis contre-lecture
par un sous-agent neuf qui n'a écrit ni ce texte ni le rapport, avec ce brouillon, le rapport, [V], [T], [AR] et [AE].

**Déclaration du rédacteur du brouillon 2.** Heures (`date -u`) : début 01:33Z ; écriture par le programme à 2026-11-17 01:35:21Z, scellement
aussitôt après (compagnon `.sha256`). Dépôt lu sur `main`, tête `1df4ae9fdd74142e290d8f177a5ac16110de60db` ; aucun commit, aucune poussée. Lu en entier : le
brouillon 1 et le rapport ; lu en partie : [T] (familles T et N, pour vérifier M4-a), en-tête et fonction `problemes` du
validateur, un programme de correction voisin (pour la forme). Jamais ouvert : rien sous `diag/`, `runs/`, `donnees/` ; aucune
branche `calcul/*` ni `donnees/*` ; rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras d'attaque, du pilote MR-2 ; aucun secret,
aucune variable d'environnement affichée ; aucune machine, aucun appel réseau ; aucun fichier existant modifié.

- **Contre-lecture 2** (R2) : **faite**, verdict « corrections » : trois défauts majeurs (M1' à M3'), neuf remarques
  mineures (m1' à m9', dont m9' facultative et non demandée) ; aucun « à refaire ». Lecteur : sous-agent neuf d'un autre
  modèle que le rédacteur des brouillons 1 et 2, qui n'a écrit ni les brouillons, ni le rapport du tour 1, ni [T], ni ses
  addendums, ni [V]. Brouillon relu : brouillon 2,
  `docs/notes/organisme-idees-juge-v1/validation-allocation-blocs-v1/prereg-validation-allocation-blocs-v1-brouillon2.md`
  (`51a8a3ab4091e27b94baad200fd7bc469f1b2b400e6346febb1471dab07a61be`). Rapport :
  `docs/notes/organisme-idees-juge-v1/validation-allocation-blocs-v1/contre-lecture-validation-blocs-tour2-v1.md`
  (`ea84faa76b64379d93e58c242b09161bacfd2aeff0d5816c5a43ffcceb41319f`). Il trouve les 29 corrections du tour 1 appliquées fidèlement et rien d'autre de changé (§ 1 du rapport).
- **Traitement, brouillon 3** : par un rédacteur neuf, sous-agent de la session mère, qui n'a écrit ni les brouillons 1 et 2,
  ni les rapports des tours 1 et 2, ni [T], ni ses addendums, ni [V] ; lettre de son modèle à inscrire par la mère au
  registre (il est du même modèle que le contre-lecteur 2). Les dix couples C1 à C10 du § 5 du rapport sont appliqués tels
  quels par le programme `appliquer-corrections-prereg-validation-allocation-blocs-v1-brouillon3.py` (même dossier, scellé), qui vérifie les empreintes du brouillon 2, du rapport et des
  quatre fichiers des comptes des annexes, tire les couples du rapport par programme, exige que chaque « ancien » figure une
  seule fois dans le brouillon 2 et qu'aucun ne chevauche un autre, recopie les deux sorties des comptes lues sur disque, et
  refuse d'écraser. S'y ajoutent onze couples du rédacteur, déclarés au tableau : annexes A et B et leurs renvois (Métrique,
  banc de mutations, origine de P13, doses neuves : M1', M2') ; le serrage retiré de l'étage 1 (m3') ; la condition sur la
  consommation du flux si Q-1 est retenue (M3') ; titre, ligne « Brouillon 3 » et statut de l'en-tête ; cette section avec les
  deux annexes. Comptes des annexes, même dossier, scellés : `compte-annexe-a-serrage-v1.py` (`d5a65b27b2e1e3b33ec25c8c88d364fc79ac966f2b0d0ab7c040ec544e9aaddc`) et sa sortie
  `sortie-compte-annexe-a-serrage-v1.txt` (`bc45c3d317e205154834c0c8c363e981ffa7fba148857491786ab6cb740cfae9`) ; `compte-annexe-b-doses-v1.py` (`b1015bf3b4e8c77fc9785e1166bc8595850b684a21fb746fd81c1484a564a0b0`) et sa sortie
  `sortie-compte-annexe-b-doses-v1.txt` (`28dc1b056fe99af2c8ca8e9cf6ea83a147da284efa73727e249222529fbea788`). Différentiel :
  `differentiel-prereg-validation-allocation-blocs-v1-brouillon2-vers-brouillon3.diff` (même dossier, scellé). Rien d'autre
  ne change ; les parties du brouillon 2 de cette section ci-dessus et la « Déclaration » finale du brouillon 1 restent telles
  quelles.

**Réponse point par point (contre-lecture 2).**

| point du rapport | couples | traitement |
|---|---|---|
| § 1 (fidélité des 29 corrections du tour 1) | — | constat du rapport ; rien à corriger |
| M1' (annexe A du serrage non écrite) | metrique-serrage, banc-de-mutations, origine-P13, annexe A | **appliqué**. Annexe A écrite : distance, variance de Λ au plafond, demi-largeur attendue d'une règle saine, borne basse attendue de la mutation et ce que le compte dit du pouvoir de la lecture (5), sans donnée du juge ; compte et sortie versés et scellés. Le compte oblige à nommer la mutation du serrage : **G lit le bloc suivant** (borne basse attendue ≈ 1,013) ; une mutation sur les seuls arrêts de A n'y est pas tuée (borne basse 0,9993). La Métrique, le banc de mutations de l'étape 0 et la colonne d'origine de P13 sont mis d'accord ; la prédiction P13 elle-même ne change pas. Vérification courte de l'annexe par un lecteur neuf : contre-lecture 3 |
| M2' (annexe B des doses non écrite) | doses-annexe-B-1, doses-annexe-B-2, annexe B | **appliqué**. Annexe B écrite : information des dix doses neuves, comptée sur les mêmes mondes que les doses de l'idée 1.2, et couverture attendue de F par famille : « réplique » entre 0,41 et 0,87 environ, « porteuse unique » au plus autant ; la règle « au-dessus de 0,95 en moyenne, doses à revoir » ne joue pas ; doses gardées ; P1, P2, P9 relues, inchangées. La borne basse de « porteuse unique » n'est pas établie par ce compte (dit dans l'annexe ; l'étage 2 couvre ce cas du côté sûr) |
| M3' (questions ouvertes dans un texte à sceller) | Q-1-flux | **non appliqué** : trancher Q-1, Q-2 et Q-3 est hors de la compétence de la rédaction (le rapport le dit) ; aucune décision de la mère sur ces questions n'était inscrite au registre à l'heure de ce brouillon. Seule la condition sur la consommation du flux par le juge candidat est écrite d'avance, valable si Q-1 est retenue. Le texte reste non scellable (statut de l'en-tête) |
| m1' (lecture (5) « sans pouvoir » et étage 1) | C1, C2 | **acceptés tels quels** |
| m2' (seuil des 12 heures) | C3 | **accepté tel quel** |
| m3' (prononcé manquant du serrage) | C4, etage-1-serrage | **C4 accepté tel quel**. Le rapport demande aussi « l'étage 1 gardant les défauts constatés sur le jeu » sans en donner le couple : la clause du serrage que m9 (tour 1) avait mise à l'étage 1 en est retirée par un couple du rédacteur, sans quoi la table dirait « garantie mise en défaut » là où la liste d'arrêt dit « aucun prononcé de la table » |
| m4' (borne de Markov de P14) | C5 | **accepté tel quel** |
| m5' (attribution de m7) | C6 | **accepté tel quel** |
| m6' (colonnes de réfutation de P7 et P8) | C7, C8 | **acceptés tels quels** |
| m7' (crédits et hors crédits) | C9 | **accepté tel quel** |
| m8' (renvoi non défini) | C10 | **accepté tel quel** ; l'annexe A de [T] reprend elle-même la construction de l'annexe A du banc B v1 ; l'annexe B de ce texte donne le chemin et l'empreinte des deux |
| m9' (essai à blanc et code ; facultative, non demandée) | — | **non appliquée** : le rapport la dit facultative et ne la demande pas ; aucun couple ; à la mère si elle la veut |
| § 2, réserve « sans conséquence » (phrase de répartition muette sur les copies par morceaux de « vide ») | — | **non appliquée** : le rapport ne demande rien |
| § 6, points pour la mère | — | **à la mère** : Q-1, Q-2, Q-3 ; lettres des modèles au registre ; tâche d'attente avant le jeu ; aucun mot de Lazar nécessaire pour ce texte |

**Remarques du rédacteur, sans effet sur le texte** (pour la mère et la contre-lecture 3). (1) Le compte de l'annexe A rend
plausible que la lecture (5) soit déclarée « sans pouvoir sur le banc réel » par sa propre règle (mutation sur les arrêts de A,
moyenne seule jugée, huit voisines par génération sur 500 générations) ; la règle écrite la range alors sans critère, du côté
sûr. Une lecture appariée (mutation moins règle saine, sur les mêmes trajectoires) ou la mutation « G lit le bloc suivant »
rejouée sur le bras G de la famille « nul » auraient plus de pouvoir ; ce serait un changement de conception, que ce tour ne
fait pas. (2) Dans la série d'essai de l'annexe A, la borne haute de F passe sous 1 : c'est un cas d'« audit écrit » du Seuil,
et l'audit fait dans l'annexe le range en écart d'échantillonnage ; au jeu, la même situation reste un audit, non un défaut.

**Ce qui reste avant le scellement** (remplace « Ce qui reste avant la contre-lecture 2 » ci-dessus) : réponses de la mère à
Q-1, Q-2 et Q-3, puis, par couples, les lignes qui en dépendent retirées ou gardées (ligne de la liste d'arrêt sur le juge
candidat et condition sur la consommation du flux, lignes du Coût, questions ouvertes ; couples M1-a et M1-b du tour 1 si Q-2
tranche pour 500 générations) ; contre-lecture 3, limitée aux parties touchées par ce brouillon et aux deux annexes, par un
sous-agent neuf qui n'a écrit ni les brouillons ni les rapports, d'un autre modèle que le rédacteur du brouillon 3, avec ce
brouillon, le rapport du tour 2, le différentiel, les deux comptes et leurs sorties, [T] (réserve (a) de la Métrique, annexe
A), le banc B v1 (annexe A), [V] (§ 1, § 3.5, § 4), le programme de [CL] et `synthetique_v1.py`.

**Déclaration du rédacteur du brouillon 3.** Heures (`date -u`) : début vers 01:53Z (premier relevé 01:54:26Z) ; comptes des
annexes de 02:07Z à 02:33Z ; écriture par le programme à 2026-11-17 02:41:50Z, scellement aussitôt après (compagnon `.sha256`). Dépôt lu sur
`main`, tête `6467b9225044394f018fb4188d5752b253ba0855` ; aucun commit, aucune poussée. Lu en entier : le rapport du tour 2 et le brouillon 2 ; lu en partie : [T]
(Garantie, Prédiction, Métrique, Seuil, banc B v2 et familles, bras, graines, étapes, annexes A et B), [V] (en-tête et § 1 à
4), le banc B v1 (banc B et annexe A), le programme de [CL] et sa sortie, `synthetique_v1.py`, les lignes d'import de trois
modules gelés, le programme du brouillon 2 (pour la forme), deux registres (recherche d'une décision de la mère sur Q-1 à
Q-3 : aucune), une recherche de mots dans quatre pièces voisines des cribles (i) et (ii) (forme d'une réponse sans couple),
l'état du dépôt (`git status`, noms de fichiers seulement). Comptes : processeur seul, `nice -n 19`, graines d'essai
seulement, interpréteur et bibliothèques du dépôt (Python 3.13.18, numpy 2.4.6) ; essais intermédiaires dans le bloc-notes
de la session, hors dépôt, dont aucun chiffre n'est cité ici que les comptes versés ne refassent. Jamais ouvert : rien sous
`diag/`, `runs/`, `donnees/` ; aucune branche `calcul/*` ni `donnees/*` ; rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras
d'attaque, du pilote MR-2 ; aucun secret, aucune variable d'environnement affichée ; aucune machine, aucun appel réseau ;
aucun fichier existant modifié. Incidents : (a) une recherche dans `registres/etat.md` a affiché des lignes d'état qui nomment
d'autres travaux (B bis, T0.7, pilote MR-2) : aucune de leurs pièces n'a été ouverte, rien n'en est employé ; (b) la liste des
processus du conteneur a été lue (commandes seulement) pour mesurer la charge avant les comptes ; (c) une première série
d'essai de l'annexe A, de 4 000 générations, donnait pour F une moyenne de Λ nettement sous 1 : l'audit (variance exacte, dix
séries indépendantes, partie 3 du compte versé) la range en écart d'échantillonnage, et la série finale, de 20 000
générations, contient ces 4 000 premières ; rien n'en est caché dans l'annexe.

## Annexe A — compte de dimensionnement du serrage (sans juge, sans nul de production)

Objet (défaut M1' de la contre-lecture 2) : fixer la distance des 24 cartes du monde jouet du serrage ; compter, sans donnée
du juge, la variance de Λ au plafond, la demi-largeur attendue de l'intervalle d'une règle saine et la borne basse attendue de
la mutation « la règle lit le bloc suivant » ; dire ce que ce compte apprend du pouvoir de la lecture (5).

Construction : le monde jouet du jeu synthétique de [T] (`src/controle_ia/organisme_idees_juge/synthetique_v1.py`,
`febe203ab27796ba573accea6e6fea5692bc2c776191254408ab07d3cc9815d7`), bâti comme le programme de [CL]
(`docs/notes/organisme-idees-juge-v1/contre-lecture-prereg-tirages-repartis-v1-outils/essai_validite_v1.py`,
`01c648a0f5a65a578e95f73836666d0e55d837ee72438e15b0d37443cbfff205`) : 3 issues, un trait binaire, nul composite à deux lois,
monde dans la classe, 24 cartes Q_i = softmax(log P + ε_i·N(0, 1)) hors de la classe, maximum de vraisemblance recalculé à
chaque instant, blocs de 25, plafond 800, budget 4 800, m = 24, lois et issues tirées par génération (écart E-2 de [AE]).
**Seule la distance change** : ε_i de 0,01 à 0,03 au lieu de 0,10 à 0,30. Règles F, A, G et règle gloutonne qui anticipe :
fonctions du programme de [CL], importées telles quelles après contrôle de son empreinte (règles simplifiées, qui suffisent à
un dimensionnement ; au jeu, les règles du serrage sont celles du rejeu gelé) ; la copie des tirages est contrôlée contre
`synthetique_v1.py` (partie 0 du compte). Λ est lu au temps d'arrêt de la règle (premier instant révélé où log W atteint
log(m/α), sinon dernier instant révélé). Graines d'essai `SeedSequence(entropy=20261117, spawn_key=(k, g))`, jamais `(97, g)`,
`(98, g)` ni la racine d'un texte. Compte : `compte-annexe-a-serrage-v1.py` (`d5a65b27b2e1e3b33ec25c8c88d364fc79ac966f2b0d0ab7c040ec544e9aaddc`), sortie
`sortie-compte-annexe-a-serrage-v1.txt` (`bc45c3d317e205154834c0c8c363e981ffa7fba148857491786ab6cb740cfae9`), même dossier, scellés ; processeur seul, Python 3.13.18 et numpy
2.4.6 du dépôt, trois minutes (de 02:30Z à 02:33Z). Sortie, recopiée en entier :

```
distance retenue : eps = linspace(0.01, 0.03, 24) ; programme de la contre-lecture 01c648a0... vérifié
[0] copie de tirages_generation : lois et comptes égaux à ceux de synthetique_v1 sur 5 générations d'essai
[1] distance du jeu de l'idée 1.2 (0,10 à 0,30) : variance de Λ au plafond, 20000 générations x 24 cartes : médiane 6.36e+05 ; moyenne 1.53e+125 ; quantile 0,999 2.36e+63 ; maximum 7.34e+130 ; carte la plus loin : médiane 1.44e+14, moyenne 3.67e+126 ; demi-largeur projetée (borne de Doob, règle saine, 20 000 générations) 1.11e+60
[1] distance 0,01 à 0,05 (comparaison) : variance de Λ au plafond, 20000 générations x 24 cartes : médiane 0.34 ; moyenne 1.35 ; quantile 0,999 67.9 ; maximum 1.28e+04 ; carte la plus loin : médiane 1.6, moyenne 7.09 ; demi-largeur projetée (borne de Doob, règle saine, 20 000 générations) 0.00328
[1] distance retenue (0,01 à 0,03) : variance de Λ au plafond, 20000 générations x 24 cartes : médiane 0.146 ; moyenne 0.262 ; quantile 0,999 3.8 ; maximum 31.7 ; carte la plus loin : médiane 0.412, moyenne 0.632 ; demi-largeur projetée (borne de Doob, règle saine, 20 000 générations) 0.00145
[2] dominations franchies (log W > log Λ) sur 20000 générations x 24 cartes x 32 instants : 0
[2] F                                    : moyenne de Λ au temps d'arrêt 0.9992 ± 0.0007 (20000 générations) ; écart type par génération 0.0471 ; demi-largeur projetée à 20 000 générations 0.0007 ; borne basse projetée 0.9986 ; part arrêtée haut 0.0000, bas 0.0523 ; tirages moyens par carte 200.0
[2] A                                    : moyenne de Λ au temps d'arrêt 0.9993 ± 0.0007 (20000 générations) ; écart type par génération 0.0473 ; demi-largeur projetée à 20 000 générations 0.0007 ; borne basse projetée 0.9987 ; part arrêtée haut 0.0000, bas 0.0531 ; tirages moyens par carte 200.0
[2] G                                    : moyenne de Λ au temps d'arrêt 0.9998 ± 0.0007 (20000 générations) ; écart type par génération 0.0537 ; demi-largeur projetée à 20 000 générations 0.0007 ; borne basse projetée 0.9991 ; part arrêtée haut 0.0000, bas 0.0143 ; tirages moyens par carte 200.0
[2] X1 (G lit le bloc suivant)           : moyenne de Λ au temps d'arrêt 1.0142 ± 0.0007 (20000 générations) ; écart type par génération 0.0525 ; demi-largeur projetée à 20 000 générations 0.0007 ; borne basse projetée 1.0134 ; part arrêtée haut 0.0000, bas 0.0141 ; tirages moyens par carte 200.0
[2] A-anticipe (A lit le bloc suivant)   : moyenne de Λ au temps d'arrêt 0.9999 ± 0.0006 (20000 générations) ; écart type par génération 0.0467 ; demi-largeur projetée à 20 000 générations 0.0006 ; borne basse projetée 0.9993 ; part arrêtée haut 0.0000, bas 0.0000 ; tirages moyens par carte 200.0
[2] différence appariée X1 (G lit le bloc suivant) moins G (mêmes tirages) : +0.0144 ± 0.0004
[2] différence appariée A-anticipe (A lit le bloc suivant) moins A (mêmes tirages) : +0.0006 ± 0.0001
[3] F, dix séries de 4 000 générations : écarts réduits (écart type observé) -0.86, +0.04, +0.59, -0.43, +0.96, -0.23, -0.68, +0.23, -1.51, -1.68 ; écart type des dix 0.86 ; par la variance exacte -0.84, +0.04, +0.61, -0.42, +0.98, -0.23, -0.67, +0.24, -1.52, -1.68
```

Lecture.

1. **Distance.** À la distance de [T], la variance de Λ au plafond est astronomique (médiane 6,4·10⁵, moyenne 1,5·10¹²⁵) : la
   moyenne de Λ sur 20 000 générations y serait faite d'événements jamais tirés, et la lecture serait sans objet. De 0,01 à
   0,05, la queue reste lourde (maximum 1,3·10⁴). **Distance retenue : ε_i de 0,01 à 0,03** (24 valeurs régulièrement
   espacées) : variance de Λ au plafond de médiane 0,146, de moyenne 0,262, de quantile 0,999 égal à 3,8 et de maximum 31,7 sur
   480 000 cartes d'essai.
2. **Règles saines.** Pour toute règle non anticipante, la variance de la moyenne des 24 Λ au temps d'arrêt est au plus la
   somme de leurs variances au plafond divisée par 24² (pour chaque carte, l'espérance du carré de Λ − 1 est la somme des
   carrés de ses accroissements, que l'arrêt ne fait qu'écourter ; les produits croisés de deux cartes sont d'espérance nulle,
   une seule carte avançant à chaque pas) : demi-largeur projetée au plus 0,0015 sur 20 000 générations, pour F-arrêt, P et P′
   comme pour les règles jouées ici. Sur la série d'essai de 20 000 générations, F, A et G donnent 0,9992, 0,9993 et 0,9998,
   chacune à ± 0,0007 ; aucune domination franchie ; aucun arrêt haut (les cartes sont trop proches du monde pour qu'une
   promotion arrive) ; les parts « bas » de F et de G sont des étiquettes, seule A s'arrête bas (5 % des cartes).
3. **Audit de la série d'essai (R4).** La borne haute de F y passe sous 1 (0,9999) : au jeu, ce serait un cas d'« audit écrit »
   du Seuil. L'espérance est exactement 1 par construction ; dix séries indépendantes de 4 000 générations donnent des écarts
   réduits de −1,68 à +0,96 (écart type 0,86), presque les mêmes par la variance exacte : écart d'échantillonnage, non biais. La
   probabilité de fausse alerte est celle que le Seuil écrit (jusqu'à environ 14 % pour six règles à 95 % ; de même pour une
   borne haute sous 1, qui ne demande qu'un audit écrit).
4. **Mutation.** « G lit le bloc suivant » (chaque bloc va à la carte dont log W après ce bloc sera la plus grande) : moyenne
   1,0142 ± 0,0007 ; différence appariée avec G sur les mêmes tirages +0,0144 ± 0,0004 ; **borne basse attendue sur 20 000
   générations ≈ 1,013**, soit une marge d'environ vingt demi-largeurs au-dessus de 1 : la mutation est tuée. C'est la mutation
   que le serrage joue (Métrique). Une mutation qui ne joue que sur les arrêts de A (A décide ses arrêts sur l'instant suivant,
   non révélé) n'est pas tuée par le critère « borne basse > 1 » (0,9999 ± 0,0006 ; effet apparié +0,0006 ± 0,0001) : là où
   les arrêts bas sont rares, elle ne change presque rien.
5. **Pouvoir de la lecture (5)** (Métrique : mutation rejouée sur le bras A de la famille « nul »). Ce compte ne dit rien du
   banc réel, où les voisines du monde s'arrêtent bas bien plus souvent sous A ([V] § 3.6, R-1 : moyenne des valeurs e 0,052
   sous A contre 0,089 sous F, l'arrêt bas gelant des valeurs e très petites) ; il montre seulement qu'une mutation qui ne joue
   que sur les arrêts de A a un effet petit, que la moyenne seule voit mal. Avec huit voisines par génération sur 500
   générations, l'issue « sans pouvoir sur le banc réel » est plausible ; la règle écrite la range alors sans critère, la
   réserve 3 de [V] restant portée par le serrage seul.

## Annexe B — compte de dimensionnement des doses neuves (sans juge, sans nul)

Objet (défaut M2' de la contre-lecture 2, après m10 du tour 1) : information sur 200 épisodes des dix doses neuves et
couverture attendue de F par famille ; si la couverture attendue de F en « réplique » ou en « porteuse unique » dépassait 0,95
en moyenne, les doses seraient à revoir avant le scellement (règle du rapport, décision de la rédaction).

Construction : exactement celle des deux comptes publiés dont ce texte reprend la méthode, l'annexe A du banc B v1
(`docs/notes/organisme-idees-juge-v1/prereg-nul-par-morceaux-limite-v1.md`,
`46ef2b92119ee5dff05727b90ca8bdd3ba57b52f9c1c75893750c792a2abc089`, cité par [T] ; lignes V1 à V4, script
`c52b822296e2f4b5d0417e5400e99d5626217ebba667ab5ddfb990f9cf78ce93`) et l'annexe A de [T] (ligne V5, script
`ffa8d9b617b82e6de27165db07efc9beb89cd8e221d21f6bdabf13ea96f65274`) : information moyenne par épisode E_x KL(monde ‖ S1), 300
mondes, 4 000 instances par monde ; ici, pour chaque type, les deux doses de l'idée 1.2 et les deux doses neuves sont comptées
sur les **mêmes** 300 mondes. Contrôles : les deux scripts publiés, extraits de leurs textes (empreintes retrouvées) et
rejoués tels quels, rendent leurs sorties à l'octet près (empreintes publiées
`e8899d3fdf21640e7568e569091f0fef6d5376d4fab3240f0f5eac53f9d602d9` et
`bf2a94eb29a8d12130acbf2e0602802e801895783af8aa3dd7c68c3fbf4666cd` retrouvées) ; la fonction du compte, rejouée dans leur ordre
et sur leur graine, retrouve leurs quinze lignes (contrôle écrit dans le compte, qui s'arrête sinon). Graine d'essai
`SeedSequence(20261117)`. Compte : `compte-annexe-b-doses-v1.py` (`b1015bf3b4e8c77fc9785e1166bc8595850b684a21fb746fd81c1484a564a0b0`), sortie `sortie-compte-annexe-b-doses-v1.txt`
(`28dc1b056fe99af2c8ca8e9cf6ea83a147da284efa73727e249222529fbea788`), même dossier, scellés ; processeur seul, Python 3.13.18 et numpy 2.4.6 du dépôt, vingt secondes. Sortie,
recopiée en entier :

```
contrôle de la copie : les quinze lignes des deux annexes publiées sont retrouvées à l'identique
V1 effet neuf global                          dose 0.250 (idée 1.2) : médiane 0.0133 nat/épisode [quartiles 0.0072 ; 0.0256] ; sur 200 épisodes : 2.7 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.19
V1 effet neuf global                          dose 0.375 (neuve   ) : médiane 0.0293 nat/épisode [quartiles 0.0162 ; 0.0579] ; sur 200 épisodes : 5.9 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.49
V1 effet neuf global                          dose 0.500 (idée 1.2) : médiane 0.0520 nat/épisode [quartiles 0.0285 ; 0.1034] ; sur 200 épisodes : 10.4 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.70
V1 effet neuf global                          dose 0.625 (neuve   ) : médiane 0.0792 nat/épisode [quartiles 0.0431 ; 0.1563] ; sur 200 épisodes : 15.8 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.86
V2 conditionnelle au signe                    dose 0.400 (idée 1.2) : médiane 0.0109 nat/épisode [quartiles 0.0077 ; 0.0146] ; sur 200 épisodes : 2.2 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.00
V2 conditionnelle au signe                    dose 0.600 (neuve   ) : médiane 0.0247 nat/épisode [quartiles 0.0176 ; 0.0325] ; sur 200 épisodes : 4.9 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.30
V2 conditionnelle au signe                    dose 0.800 (idée 1.2) : médiane 0.0432 nat/épisode [quartiles 0.0315 ; 0.0569] ; sur 200 épisodes : 8.6 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.76
V2 conditionnelle au signe                    dose 1.000 (neuve   ) : médiane 0.0673 nat/épisode [quartiles 0.0495 ; 0.0878] ; sur 200 épisodes : 13.5 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.93
V3 conditionnelle à seuil décentré            dose 0.400 (idée 1.2) : médiane 0.0108 nat/épisode [quartiles 0.0076 ; 0.0147] ; sur 200 épisodes : 2.2 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.00
V3 conditionnelle à seuil décentré            dose 0.600 (neuve   ) : médiane 0.0247 nat/épisode [quartiles 0.0173 ; 0.0328] ; sur 200 épisodes : 4.9 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.29
V3 conditionnelle à seuil décentré            dose 0.800 (idée 1.2) : médiane 0.0442 nat/épisode [quartiles 0.0314 ; 0.0576] ; sur 200 épisodes : 8.8 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.77
V3 conditionnelle à seuil décentré            dose 1.000 (neuve   ) : médiane 0.0689 nat/épisode [quartiles 0.0492 ; 0.0879] ; sur 200 épisodes : 13.8 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.94
V4 loi neuve sur une sous-population          dose 0.100 (idée 1.2) : médiane 0.0158 nat/épisode [quartiles 0.0071 ; 0.0332] ; sur 200 épisodes : 3.2 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.26
V4 loi neuve sur une sous-population          dose 0.150 (neuve   ) : médiane 0.0298 nat/épisode [quartiles 0.0140 ; 0.0585] ; sur 200 épisodes : 6.0 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.49
V4 loi neuve sur une sous-population          dose 0.200 (idée 1.2) : médiane 0.0454 nat/épisode [quartiles 0.0229 ; 0.0872] ; sur 200 épisodes : 9.1 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.67
V4 loi neuve sur une sous-population          dose 0.250 (neuve   ) : médiane 0.0641 nat/épisode [quartiles 0.0330 ; 0.1191] ; sur 200 épisodes : 12.8 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.76
V5 conditionnelle à une coupure de l'archive  dose 0.400 (idée 1.2) : médiane 0.0119 nat/épisode [quartiles 0.0083 ; 0.0145] ; sur 200 épisodes : 2.4 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.00
V5 conditionnelle à une coupure de l'archive  dose 0.600 (neuve   ) : médiane 0.0264 nat/épisode [quartiles 0.0187 ; 0.0326] ; sur 200 épisodes : 5.3 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.31
V5 conditionnelle à une coupure de l'archive  dose 0.800 (idée 1.2) : médiane 0.0463 nat/épisode [quartiles 0.0329 ; 0.0576] ; sur 200 épisodes : 9.3 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.80
V5 conditionnelle à une coupure de l'archive  dose 1.000 (neuve   ) : médiane 0.0711 nat/épisode [quartiles 0.0522 ; 0.0905] ; sur 200 épisodes : 14.2 nat ; part des mondes à 200 épisodes au-dessus de log 480 : 0.93
```

Lecture.

1. **Information.** Doses neuves basses : 4,9 à 6,0 nats sur 200 épisodes (V1 5,9 ; V2 4,9 ; V3 4,9 ; V4 6,0 ; V5 5,3) ; doses
   neuves hautes : 12,8 à 15,8 nats (V1 15,8 ; V2 13,5 ; V3 13,8 ; V4 12,8 ; V5 14,2). Sur les mêmes mondes, les doses de l'idée
   1.2 portent 2,2 à 3,2 nats (basses) et 8,6 à 10,4 nats (hautes) : dans chaque type, la dose neuve basse tombe entre les deux
   doses de l'idée 1.2 et la dose neuve haute au-dessus de la haute. Part des mondes dont l'information sur 200 épisodes passe
   log 480 : 0,29 à 0,49 aux doses neuves basses, 0,76 à 0,94 aux hautes. La dose 1,0 de V2, V3 et V5 porte 13,5 à 14,2 nats
   pour 6,17 (log 480) nécessaires à une carte seule : les cellules de dose haute sont proches du plafond pour F, comme le
   texte le disait par interpolation (« environ 13 nats », que le compte remplace).
2. **Couverture attendue de F en « réplique »** (composition de la famille T de [V]). Hypothèse déclarée : dans chaque type, la
   couverture de F croît avec la dose (l'information croît sur les mêmes mondes ; [V] § 3.5 et § 4 : de 0,09 à 0,19 aux doses
   basses à 0,44 à 0,80 aux doses hautes). Alors chaque cellule neuve couvre au moins autant que la cellule de même type et de
   même rang de [V], et chaque cellule neuve de dose basse au plus autant que la cellule de dose haute de son type dans [V]. La
   couverture réunie étant la moyenne des dix cellules (75 générations chacune), elle est **au moins de 0,413** (celle de [V],
   § 1 : 310 générations sur 750) et **au plus d'environ 0,87** (somme des cinq cellules hautes de [V], plus 5, le tout divisé
   par 10 ; la somme des cinq cellules hautes vaut 4,13 moins celle des cinq basses, chacune d'au moins 0,09, § 3.5). Ces
   bornes portent sur l'espérance, à l'erreur d'estimation des chiffres de cellule de [V] près (quelques centièmes).
3. **« Porteuse unique ».** Sa porteuse est l'une des quatre constructions que « réplique » porte toutes (avec deux doublons) :
   sa couverture attendue est au plus celle de « réplique », donc au plus d'environ 0,87. Sa borne basse n'est **pas** établie
   par ce compte (il y faudrait le juge) ; si elle sortait à 0,05 ou moins, l'étage 2 rangerait la famille « hors de la zone
   utile », du côté sûr.
4. **« Dense »** : douze porteuses, couverture au moins de l'ordre de celle de « réplique », proche du plafond aux doses
   hautes ; aucune zone utile n'y est exigée (gain rapporté sans critère). **« Nul » et « vide »** : aucune porteuse, aucune
   couverture.
5. **Conclusion.** La règle de la contre-lecture 2 (doses à revoir si la couverture attendue de F dépasse 0,95 en moyenne en
   « réplique » ou en « porteuse unique ») **ne joue pas** : les doses sont gardées. P1, P2 et P9, relues avec ce compte, ne
   changent pas : le critère de P1 et de P2 (≥ +0,05, borne basse > 0) reste atteignable sur toute la plage (gain au plus
   1 − C_F, soit au moins 0,13) ; l'économie de P9 tient surtout aux non porteuses, que la dose touche peu (seules les fausses
   construites portent une composante de même dose).

## Citations obligatoires (N-064, N-067)

Reprises de [T] l. 665-672, empreintes recalculées par moi à 01:06Z, PDF non relus (aucun chiffre n'en est tiré, R7) : POPPER
(Huang et al., ICML 2025 ; `docs/sources/pdf/huang-2025-icml-pmlr-267-popper-automated-hypothesis-validation-agentic-sequential-falsifications.pdf`,
`a3c4b3701543a84a74602ae46a624b955e201bb83baeea2c219213a0e65b4998`) ; Dwork et al., arXiv 1506.02629
(`docs/sources/pdf/anteriorite-P-041-v2/c8/1506.02629.pdf`, `dcfbb9aa401c62949123be2d74787c4f9cca48597f18860760ef1580ddb4bc71`) ;
Blum et Hardt, « The Ladder », arXiv 1502.04585 (`docs/sources/pdf/anteriorite-P-041-v2/c8/1502.04585.pdf`,
`957ef4739df371a0a778360f0db4252a62f7c85abcd8343f581cd6250b1d31fe`) ; Co-Scientist (Gottweis et al., Nature 655, p. 487-496, 2026 ;
`docs/sources/co-scientist-v1/gottweis-2026-nature-655-487-accelerating-scientific-discovery-with-co-scientist.pdf`,
`351f49d89d2f4f4ed84eed4225c09cc95470c41aa3becd0aa3e06b3bd8ba54c3`) ; voisins lus sur PDF par [CL] et cités par [T] : PACE
(`docs/sources/pdf/2606.08106v1.pdf`, `779f49607688fd06226d4390ad6e0c4c8356ef75b87243fd734181cef700934f`), E-valuator
(`docs/sources/pdf/2512.03109v2.pdf`, `b7a46e4cf781aec0c5730196b9f6a2ea1e42c3ec63f1e5260dff223dfafe3828`), Qu, Chen et Wang
(`docs/sources/pdf/anteriorite-P-041-v2/c8/2609.27051.pdf`, `2a8ded0119a1db422aa548fdc3be80b2861f0548bc8166256be60572a2fddb03`) ;
liste de N-067, section 6 (dont Hegazy, Jordan et Dieuleveut, PDF sur une autre branche, non lu). **Aucune revendication n'est
faite ici.**

## Déclaration

Rôle : rédacteur neuf du brouillon 1 (R1), sous-agent de la session mère ; lettre du modèle à inscrire par la mère. Heures
(`date -u`) : début 01:03:25Z ; lectures de 01:03Z à 01:07Z ; rédaction de 01:07Z au scellement (compagnon `.sha256`). Pièces
lues en entier : [V] (`3b08f061…`), [T] (`bdabf2bc…`) ; [AR] (`632a8979…`) jusqu'à son § 6 (contre-lecture et annexe A non lues) ;
[AE] (`1b96cf06…`) § 1 à 5 ; en-tête de `banc_tirages_repartis_v1.py` (constantes et graines) ; liste des fonctions de
`rejeu_v1.py` ; gabarit et sections du validateur ; trois lignes du registre (R-2851, R-3008, R-3044). Du run de l'idée 1.2 :
compagnons vérifiés (six conformes) et noms de clés de premier niveau seulement, aucune valeur. Calcul : seuils binomiaux de
[T] annexe B recalculés pour sept et huit bras (13 et 39), sans donnée. Jamais ouvert : le run invalide et sa copie ; aucune
branche `calcul/*` ni `donnees/*` ; rien de 7a, 7b, T0.6, T0.7, B bis, P3-bis, du bras d'attaque, du pilote MR-2 ; aucun secret,
aucune variable d'environnement affichée ; aucun appel réseau ; aucun commit ; aucun fichier existant modifié. Incidents : aucun.
