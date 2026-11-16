# Verdict de l'idée 1.2 du juge de l'organisme d'idéation (tirages répartis par blocs avec arrêt anticipé) — v1

- Lecteur : sous-agent neuf, modèle C (R13) ; il n'a écrit ni le préenregistrement, ni le code, ni l'analyse, ni la lecture gelée.
  Texte du modèle A. Début 2026-11-16 18:22:22Z (`date -u`) ; lecture, recalculs légers et rédaction jusqu'à l'heure du scellement
  (compagnon `.sha256`).
- Texte appliqué : `prereg/organisme-idee-1-2-tirages-repartis-arret-anticipe-v4.md`
  (`bdabf2bc9b2c9b78939660f7f7053576a145e165927cafd23e14a798d07d790e`), ci-dessous **[T]** ; addendum d'empreintes
  (`1b96cf065cef40ed9e452611b107d9f40f598091c8a591f2397bf58e7c92beee`), **[AE]**, écarts E-1 et E-2 acceptés par Lazar
  (GO-2026-11-16-01, point 4) ; addendum de relance (`632a897944c1c36e8c7b3e2b078e1a4e1ed8bd0489379f10391c191404ed4f55`), **[AR]**.
- Run lu : `20261116-140942-idee-1-2-tirages-repartis-v1`. Pièces, chacune vérifiée contre son compagnon `.sha256` avant lecture :
  - `runs/20261116-140942-idee-1-2-tirages-repartis-v1/manifeste.json` : `bafa810732bfe3cf8cc78c290bfbecaaef11db25f75a1d239be1de878b11a40f` ;
  - `diag/organisme-idees-juge-v1/20261116-140942-idee-1-2-tirages-repartis-v1/` :
    `controles-avant-jeu.json` `904be812d8e3481371c394ec57e7c44b5a1e8f70365ce1c8a4cea6d8fae58f77` ;
    `oracle.json` `f0334f9bf38aa89a6d94f5ab51b84de557e173796ba892343205383dcdd174cd` ;
    `jeu.json` `f70b21b5cc21ca8ea41c5ba6267cfb9e1c5768cc1110bb288e4fcfcdde274e4a` ;
    `journal.json` `6d815c6078c7c45a694583e6971fb35d09b7964ad408d850a565aa40e0e284ba` ;
    **lecture gelée v2** `lecture-gelee-v2.json` `51b430e99d177349da1c52f5c9ed41aa0958cb3dd32133c7b64c2c8d83652f29` ;
  - code de lecture `src/controle_ia/organisme_idees_juge/lire_banc_tirages_repartis_v2.py`
    `18169a33917807c7ae019202f9ffdac656cccc66c0f1354bc33d710c78a4358d` (égal à [AE] § 1).
- Contrôles de rattachement : les 34 fichiers gelés du manifeste sont identiques, ligne à ligne, à ceux de [AE] § 1 et leurs
  empreintes actuelles sur disque leur sont égales (aucune différence) ; la racine des graines du manifeste est l'entier de
  l'empreinte de [T] ; le manifeste dit `decisif: true`, `depot_propre: true`, `reserves: []`, commit `765acfc303f7…`, numpy 2.4.6,
  scipy 1.17.1, Python 3.13.18 (versions que [AR] 4.2 exige) ; le journal rattache sorties et manifeste (même empreinte) ; pas
  de `arret.json` ; durée murale 15 049 s (4,18 h), sous la borne de 24 h ; ordre des écritures : essais et mutations 14:31Z,
  oracle scellé 15:01:16Z **avant** le rejeu, jeu et journal 18:20:31Z, lecture gelée 18:21:43Z (après le scellement de la sortie).
  Essais : 167 passés sur 167 ; essai E1 : 50 cartes, aucun échec ; banc de mutations : 24 sur 24 tuées ; jeu synthétique de
  20 000 générations : lecture saine moyenne 0,4536 (borne basse 0,4146, sous 1), lecture mutée « valeur e au maximum » moyenne
  2,484 (borne basse 2,341, au-dessus de 1) : la mutation est tuée comme [T] l. 306-316 l'exige.
- **Run invalide nommé au rapport ([T] ; [AR] § 4.8 et § 2).** Un premier lancement, `20261116-002954-idee-1-2-tirages-repartis-v1`
  (00:29:50Z, copie `/home/user/jeu-idee-1-2-copie`), a été interrompu par un arrêt venu de l'extérieur (redémarrage du conteneur,
  cause déclarée par [AR] § 2 ; aucune sortie de jeu ni de journal ; qualification : run invalide sous [T] l. 512, relance sous un
  addendum neuf, [AR]). Ses trois fichiers (manifeste, contrôles, oracle ; empreintes à [AR] § 2) n'ont **jamais été ouverts**
  par moi ni, d'après [AR] § 3, par personne ; **aucun chiffre de ce verdict n'est tiré de lui**. Le run lu ici est la relance
  sous [AR] ; elle refait les mêmes tirages ([AR] § 4.2) : ce n'est pas une seconde chance sur un autre tirage.

## 1. Recalcul léger de contrôle (avant d'appliquer la table)

Programme jeté (aucun fichier du dépôt modifié), sur `jeu.json` et `oracle.json` seuls, un processus, quelques secondes :

- Famille T, 750 générations : générations couvertes (au moins une porteuse au sens de l'oracle promue) : A 646 (0,8613),
  F 310 (0,4133), F-arrêt 306, F125 381, P 435, P′ 425 ; **égal** à la lecture gelée (646 ; 310 ; 306 ; 381 ; 435 ; 425).
  Tableau croisé A contre F : 336 générations où A seul couvre, **0** où F seul couvre : égal à la lecture (McNemar `a_seul` 336,
  `b_seul` 0). Fausses promotions par génération : A 0,00267, F 0,00133, P 0,00267, P′ 0,004, F125 0,00267 : égal. Tirages
  moyens sur le budget : A 0,672, F 1, F-arrêt 0,432, F125 1,25 : égal. Classes de l'oracle : 13 500 fausses, 4 483 porteuses,
  17 porteuses sans gain, 0 partiellement vraie : égal.
- Famille N, 500 générations : promotions dans les sept bras : **0** dans chacun (égal à la lecture).
- Cohérence interne des 192 000 lignes carte-bras (1 250 générations × 24 cartes × 6 ou 7 bras) : tirages = 25 × somme des
  blocs ; F à exactement 8 blocs ; aucune carte de A ou de F-arrêt n'a reçu un bloc après une valeur sous le seuil bas (au
  moins deux blocs) ni après le seuil haut ; chaque étiquette « bas » ou « haut » correspond à la trajectoire ; la valeur e
  rendue égale la trajectoire au dernier instant donné ; plafond de 32 blocs respecté ; budget jamais dépassé. **Aucune
  violation.**
- Je n'ai pas refait les intervalles de rééchantillonnage ni l'application de la règle de Benjamini et Hochberg : la lecture
  gelée les rend, son code est celui de [AE], et la garde d'auto-contrôle du niveau de l'intervalle y est écrite
  (`exiger_niveau_intervalle`).

## 2. Application de la table « Critères de lecture gelés » ([T] l. 486-493), première ligne qui s'applique

| étage | observé (lecture gelée v2, chiffres recoupés au § 1 quand ils en dépendent) | applique ? |
|---|---|---|
| 1 | validité (famille N, 500 générations) : **0 génération avec promotion dans chacun des sept bras** (seuil de « tenue » : ≤ 13) ; **0** membre exact promu ; **0** domination franchie (dans l'un ou l'autre monde) ; sur les 49 intervalles de moyenne des valeurs e désignés au Seuil, la plus haute **borne basse** est 0,2185 (aucune > 1) ; aucun audit par monde requis | **non** |
| 1 bis | aucun bras « non jugeable » (14 à 38) ; la lecture dit « sans objet » | **non** |
| 2 | C_F (famille T, réunie) = 0,4133 : dans ]0,05 ; 0,95[ ; « dans la zone utile » | **non** |
| 3 | principale, dans l'ordre écrit au Seuil : 1. « nuisible » ? borne haute de C_A − C_F = +0,484, non < 0 ; borne basse de FP_A − FP_F = 0,000, non > +0,02 : **non**. 2. « gain » ? borne basse de C_A − C_F = **+0,4133** > 0, estimation **+0,448** ≥ +0,05, borne haute de FP_A − FP_F = **+0,004** ≤ +0,05 : **oui** | **oui : « gain »** |
| 4 | qualifications : borne haute de C_A − C_F125 = +0,388, non < 0 (donc pas « d'effectif seulement ») ; borne haute de C_A − C_P = +0,313, non ≤ 0 (donc pas « sans effet de ciblage ») ; aucune des deux | **« de structure »** |
| 5 | F-arrêt : économie 0,568 (intervalle [0,564 ; 0,572]) ; perte de couverture F − F-arrêt 0,0053 ([0,0013 ; 0,0107]) ; rapportées | rapporté |

La lecture gelée v2 mène au même résultat : `verdict: "gain"`, étage 4 « de structure », étage 1 « validité tenue », étage 1 bis
« sans objet », étage 2 « dans la zone utile » ; je ne trouve aucun écart entre elle et la table écrite.

## 3. Audit de symétrie (R4), écrit avant le prononcé

Même audit que si l'issue avait été « nuisible » ou « pas de gain » ; il est écrit pour **toute** issue ([T] l. 495). Le résultat
est un gain net et large, donc d'abord suspect de trop de propreté.

**3.1 Le mécanisme attendu se voit-il ? Oui.** Tirages moyens reçus par carte (famille T, 750 générations) : sous A, porteuses
**335,6** (au-dessus de 200 : 2 502 porteuses ont reçu plus de 200 tirages), fausses 67,5, nulles 50,2, copies de la classe 63,3,
copies par morceaux 51,6, fausses construites 88,2 ; sous F-arrêt, porteuses 158,9 (l'arrêt seul en retire) ; sous P,
porteuses 244,3 et fausses 185,2 (le hasard redistribue sans cibler). Les tirages libérés vont donc aux porteuses sous A, pas
au hasard sous P. Parts d'arrêts sous A : bas 0,826, haut 0,132, plafond 0,026, fin 0,016.

**3.2 Porteuses arrêtées bas à tort (le piège nommé par la fiche).** Il existe : sous A, 1 382 porteuses arrêtées bas. Mon recalcul
trouve **56 cas** (49 générations) où la part fixe F promeut une carte que A ne promeut pas ; 55 de ces cartes sont des
**porteuses arrêtées bas** par A, une au plafond. La couverture (« au moins une porteuse ») n'en est pas touchée, parce que
chaque génération porte six porteuses : A ne perd **aucune** génération couverte par F (0 sur 750). Ce « 0 sur 750 » est la
seule régularité qui frôle le trop propre ; elle s'explique par la redondance des six porteuses plus les tirages en plus donnés
aux survivantes, et elle ne dit rien de la perte **par carte**, qui n'est pas nulle (56 cartes). Réserve ci-dessous (R-4).

**3.3 Partiellement vraies promues : 0** (famille T : aucune carte de cette classe n'existe, 0 sur 18 000 ; famille N : 20 cartes de
cette classe, aucune promue). Porteuses sans gain promues : 0.

**3.4 Fausses promotions.** Onze promotions de fausses au total sur 750 générations et six bras : toutes sur la **même sorte**,
« copies par morceaux » (générations T 83, 159 et 615), cartes identiques d'un bras à l'autre (g = 159 : A, F125, P, P′ ; g = 615 :
A, F, F-arrêt, F125, P, P′ ; g = 83 : P′ seul). C'est une propriété de ces deux cartes (hors de la classe du nul, gain d'oracle ≤ 0),
non de l'allocation : [T] l. 232-233 dit que le théorème ne les borne pas en famille T ; elles sont mesurées, pas garanties.
Fausses promues par génération : A 0,0027 contre F 0,0013 (différence +0,0013, borne haute +0,004, loin de +0,05).

**3.5 Cellule par cellule.** Le gain A − F n'est pas identique : de **+0,187** (cellule 9) à **+0,707** (cellule 4). Il est le
plus grand là où F couvre peu (cellules 0, 2, 4, 6, 8 : F de 0,09 à 0,19, A de 0,59 à 0,83) et le plus petit là où F couvre déjà
beaucoup (cellules 3, 5, 9 : F = 0,80, A = 1,00 ou 0,99 ; effet de plafond). Dans les dix cellules A couvre plus que F. Ce profil
est celui qu'on attend d'un vrai effet d'effectif sur des composantes proches du seuil ; il ne ressemble pas à un artefact de
code (qui donnerait un gain uniforme).

**3.6 « Trop propre » ([T] l. 497-498).** Les trois conditions écrites sont fausses : gain non identique entre cellules ; fausses
promotions non nulles partout (nulles seulement dans les sortes copies de la classe, fausses construites, nulles) ; toutes les
prédictions ne sont pas tenues (Q3, voir § 4). Aucune relecture du code de rejeu n'est donc exigée par la lettre. Par prudence
de lecteur (symétrie), j'ai contrôlé la cohérence interne (§ 1) : aucune violation. Réserves de propreté, déclarées et non
bloquantes :
  - (R-1) La validité sort à **0 sur 500 dans les sept bras**, plus bas que l'estimation attendue (≤ 0,02) ; les moyennes de
    valeurs e sont de 0,05 à 0,09 toutes cartes réunies (borne haute maximale d'un des 49 intervalles : 0,24, pour la sorte
    « voisines » sous F). C'est attendu d'un nul à certificat conservateur, et la moyenne sous A (0,052) est plus basse que sous F
    (0,089) parce que l'arrêt bas gèle des valeurs e très petites. Mais une validité si loin sous le seuil **ne démontre pas** que
    la garantie est serrée : elle n'écarterait pas une inflation modérée des valeurs e. Les protections qui portent le poids
    sont la domination (0 franchie sur 500 générations × 24 cartes × 32 instants), le jeu synthétique et le banc de mutations.
  - (R-2) Le gain est mesuré **au banc**, où 18 cartes sur 24 ne portent rien et six portent la composante ([T] l. 159-163,
    hypothèse (ii)) : l'économie (0,568 pour F-arrêt) et le gain **ne se transposent pas** à une génération réelle.
  - (R-3) A consomme **moins** que le budget (0,672 en moyenne, 0,245 au minimum) : le gain n'est pas acheté par plus de tirages ;
    mais la comparaison à F125 (1,25 fois) et à P (au moins autant que A) est à lire avec leur consommation réelle,
    qui est rapportée plus haut.
  - (R-4) Le « 0 générations perdues » de A contre F (§ 3.2) tient à la redondance des six porteuses par génération, propre au banc.

**3.7 « Tout négatif » ([T] l. 498-499).** Aucune des quatre conditions n'est vraie (A n'est pas égal à F ; des cartes sont
arrêtées bas sous A ; l'économie de F-arrêt n'est pas nulle ; des porteuses dépassent 200 tirages).

**3.8 Parts d'arrêts sous F, P et P′ : lecture à faire avec la réserve de [AE] § 3, lecture 21.** F n'a aucune règle d'arrêt bas ; les
« 1 112 porteuses arrêtées bas » et la part « bas » de 0,79 sous F sont une **étiquette** de fin de trajectoire (valeur sous le
seuil), pas un arrêt réel. Elles ne se comparent pas telles quelles aux 1 382 de A. Je ne m'en sers dans aucun critère.

**3.9 Conclusion de l'audit.** Je ne trouve aucune raison d'écarter ni d'adoucir le « gain » : le mécanisme attendu se voit, le
recalcul indépendant égale la lecture, la cohérence interne est parfaite, les cellules varient comme prévu. Je ne trouve pas non
plus de raison de le durcir : les réserves R-1 à R-4 restent écrites et portent sur la portée, non sur le calcul.

## 4. Prédictions de [T] (rapportées, sans autre effet que celui de la table)

Tenues (lecture gelée) : Q1 (0 sur 500 dans chacun des sept bras, seuil ≤ 13) ; Q2 (0 membre exact promu) ; Q4 (A − F125 :
+0,353, borne basse +0,319, donc couverture A ≥ F125) ; Q5 (A − P : +0,281, borne haute +0,313 > 0 ; A − P′ : +0,295 rapporté) ;
Q6 (fausses promotions ≤ 0,004 par génération dans chaque bras ; A − F borne haute +0,004 ≤ +0,05) ; Q7 (économie F-arrêt
0,568 ≥ 25 % ; perte 0,0053 ≤ 0,02) ; Q8 (porteuses sous A : 335,6 tirages ≥ 300) ; Q9 (aucune domination franchie ; moyennes
0,05 à 0,09, toutes ≤ 0,8 ; aucune borne basse > 1).

**Q3 : non tenue dans son chiffre de dose, non réfutée.** Le cœur de Q3 est tenu (A − F : +0,448, borne basse +0,413 > 0, non
réfutée : borne haute +0,484 ≥ +0,02). Mais la clause « gain surtout à la dose haute (≥ +0,08 sur les cinq cellules de dose haute
réunies), ≤ +0,05 sur les cinq de dose basse réunies » est **fausse dans le sens inverse** : dose haute +0,277 ([0,232 ; 0,323]) ;
dose basse **+0,619** ([0,568 ; 0,667]). La lecture gelée l'écrit (`tenue: false`, `refutee: false`). Cause lisible aux
cellules : effet de plafond à la dose haute (F couvre déjà 0,44 à 0,80), alors que F ne couvre que 0,09 à 0,19 aux cinq cellules
de dose basse paires. Ce n'est pas un critère de lecture (la table ne s'y réfère pas), mais le signe et la forme prévus pour la
dose sont **réfutés** : à rapporter, car ils disent que le gain est le plus fort sur les composantes les plus faibles, contre
ce que [T] attendait.

## 5. Issue

**Issue : étage 3, « gain » ; étage 4, « de structure » ; validité tenue ; dans la zone utile. Gain de structure.**

Ligne de la table appliquée : étage 3 (principale, deuxième cas de l'ordre écrit au Seuil), puis étage 4 (aucune des deux
bornes hautes sous son seuil : ni « d'effectif seulement », ni « sans effet de ciblage ») ; les étages 1, 1 bis et 2 ne se
déclenchent pas ; étage 5 rapporté (§ 2). C'est, mot pour mot, l'issue que [T] l. 268-269 nomme « Q3, Q4 et Q5 vraies : gain de
structure (meilleur cas) ».

### Réserves de l'issue

1. Au banc seulement ; hypothèse (ii) de [T] : composition par construction, **ne se transpose pas** à une génération réelle.
2. Clause de dose de Q3 réfutée en signe (§ 4).
3. Validité « tenue » à 0 sur 500 : conservatrice, ne prouve pas la garantie serrée (R-1) ; défauts de code éventuels sur la
   fuite d'instants non révélés ne sont vus par aucune des quatre lectures sur la richesse W : seule la garde d'accès du code et sa
   mutation en protègent ([T] l. 316-318).
4. Fausses promotions de la sorte « copies par morceaux » : mesurées par l'oracle, **non garanties** en famille T ([T] l. 232-233).
5. Parts d'arrêts sous F, P, P′ : étiquette, lecture 21 de [AE].
6. Run invalide de 00:29Z nommé plus haut ; aucun chiffre n'en vient.

### Ce qui suit (mots de [T], rapportés tels quels)

- **Nœud de Lazar** ([T] l. 534-538) : « adopter l'allocation au juge changerait sa conception gelée (200 tirages et 8 instants par
  carte dans `juger_carte` et dans le texte scellé de la boucle réelle, `80fe4f03…` ; un budget de génération et un plafond de 800
  en plus) : modification du juge, à décider sur le résultat, avec sa propre validation. **À lui signaler avec ce nœud** : la
  condition « dénominateur fixe » que la synthèse des bassins étroits (§ 9) tenait pour bloquante est **levée par une preuve
  contre-lue** ([CL], verdict ; R-2878). »
- **N-058** ([T] l. 539-541) : « l'allocation sélectionne des **cartes** sur leurs valeurs e, jamais des **agents** : compatible
  (« l'interdit porte sur la sélection d'agents, pas sur celle des fiches »). Garde : les tirages reçus ne seront jamais rapportés
  par proposeur ni servis à un choix de proposeurs. »
- **Ne décide pas** ([T] l. 542-544) : « l'effet sur la découverte (une carte non proposée ne gagne rien, borne 1 du recoupement) ;
  les mondes riches à 8 traits ; les groupes de doublons ; le test de mort ; le gain en dollars (un tirage du monde planté coûte
  des millisecondes, fiche opus-p1-01, champ `perte_traduction`) ; l'économie dans une génération réelle (hypothèse (ii)). »
- Aucun **GO** n'est donné ici : ce verdict est scellé puis soumis à Lazar (R13). Rien n'est adopté ; aucune modification du juge ;
  aucune revendication ([T], dernier alinéa : « Aucune revendication n'est faite ici »).

## 6. Nœuds de Lazar et écarts

**Nœuds de Lazar (à lui porter, sans recommandation de ma part sur l'adoption, qui n'est pas du rôle du lecteur) :**
1. Adoption éventuelle de l'allocation par blocs au juge de production : modification de sa conception gelée, avec sa propre
   validation ([T] l. 534-538). Le résultat du banc est un gain de structure, avec les réserves 1 à 6 ci-dessus.
2. Signalement de la **divergence levée** : la condition « dénominateur fixe » de la synthèse (§ 9) n'est pas nécessaire, preuve
   contre-lue ; à lui annoncer avec le nœud d'adoption (même alinéa).
3. Le sort des trois fichiers du run invalide, laissés non lus dans la copie (voie (a), [AR] § 6) : après ce prononcé, le risque
   de contamination est nul ; la voie (b) (versement sur une branche d'archive) devient une décision de la mère, [AR] § 6.
4. La clause de dose de Q3, réfutée, est une information de plus pour ce nœud (le gain profite surtout aux composantes faibles).

**Écarts relevés :**
- E-1 et E-2 de [AE] (lieu du code ; monde jouet tiré par génération, graine `(97, g)`) : déclarés, acceptés par Lazar (GO-2026-11-16-01,
  point 4) ; aucun autre écart au texte trouvé dans le manifeste ni dans les contrôles.
- Durée : le Coût de [T] (l. 519-524) sous-estimait le temps de calcul ([AE] § 5 le dit) ; le jeu a duré 4,18 h au total (phase de jeu
  3,19 h) : ce n'est pas un critère.
- Réserve de lecture sur les étiquettes d'arrêt sous F, P et P′ ([AE], lecture 21).
- Non vérifié par moi : que le commit `765acfc3…` porte exactement l'addendum de relance (le manifeste consigne le commit ; je n'ai
  pas ouvert le dépôt git, la tâche me l'interdisait par la liste des pièces) ; que la liste du juge copiée soit bien celle de
  `0153e02d…` (le manifeste en rapporte les onze empreintes, égales à [AE] ; non recalculées sur la copie).

## 7. Déclaration

Rôle : lecteur neuf du verdict (R13), modèle C ; texte du modèle A. Heures : début 18:22:22Z ; lectures et recalculs entre
18:22Z et 18:30Z environ ; scellement à l'heure du compagnon `.sha256`. Pièces lues : celles listées en tête, avec leurs
empreintes, plus [T] en entier et [AE] et [AR] jusqu'à leur section 6 (les annexes et la section « Contre-lecture » de [AR] non
lues). Jamais ouvert : le dossier `/home/user/jeu-idee-1-2-copie` et le run invalide ; rien de 7a, 7b, T0.6, T0.7, P3-bis, de
l'étape B bis ni du bras d'attaque ; aucune valeur de clé ; aucun appel réseau ; aucun commit ; aucun fichier existant modifié ;
un seul processus léger à la fois. Incidents : aucun.
