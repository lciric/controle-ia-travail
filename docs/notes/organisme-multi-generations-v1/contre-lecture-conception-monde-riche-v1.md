# Contre-lecture (règle R2) de la conception « monde riche écrit par un programme et regroupement des doublons » v1 — v1

- **Lecteur** : lecteur neuf, Claude Fable 5.2 (`claude-fable-5-2`), sous-agent de la session mère
  `session_01XJ6Mgn4MZR4nxqK44C8Ea3`. Je n'ai écrit ni la conception, ni ses outils, ni le texte v2, ni le verdict v67, ni la
  synthèse du collisionneur. Même famille que le concepteur (Claude Opus 5.5), autre modèle : réserve de lignée.
- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-contre-lecteur-conception-monde-riche-v1.md`
  (`e77ccad02604da1428fac3a741172690462ffe0b22fb4aa6535f3e3baaf1ce39`, vérifiée, égale à son compagnon).
- **Interdits tenus** : aucun fichier ni branche interdits ouverts ou listés ; aucune recherche récursive (seulement
  `git grep` sur des fichiers nommés) ; aucune clé lue ; aucun appel externe ; aucune dépense ; aucune écriture git. Écrit :
  ce rapport et son compagnon ; le reste dans mon bac
  `/tmp/claude-0/-home-user-controle-ia-travail/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/cl-monde-riche/`.
  Un écart de conduite à dire : j'ai d'abord lancé quatre rejeux complets à la fois (16 processus pour 4 cœurs) ; je les ai
  arrêtés par leurs identifiants de processus (les miens seulement) et relancés en parties. Aucun refus de permissions ni de
  classifieur.
- **Heures** (`date -u`) : début 2026-11-12 22:33:26 ; rejeux 22:34:23 → 23:01:35 ; fin de rédaction 23:05:57.
- **Pièces lues** : la conception (`fc9cd3854f11625212b924fdcc4c4f4cbf61dff85656d34d01861e78e673900f`, vérifiée) en entier ;
  ses 49 pièces (compagnons revérifiés : 15 outils et 34 sorties, tous justes) ; lus en entier :
  `generateur_mondes_v1.py`, `verifier_monde_kimi_v1.py`, `monde_riche_outils_v1.py`, `puissance_monde_riche_v1.py`,
  `complements_synthese_v1.py`, `devis_multi_generations_v1.py`, `lancer_sorties_v1.sh` ; `registres/decisions.md` lignes
  R-2441, R-2442, R-2443, R-2461, R-2467, R-2469 ; texte v2 (`80fe4f03…`, vérifié), sections 3, 4, 6 et 14 ; synthèse du
  collisionneur (`4f99077b…`, vérifiée) en entier ; point 3 de la consigne du concepteur (`6cab9057…`).
- **Ce que je n'ai pas lu** : le code gelé de la course (absent du dépôt, comme le dit le concepteur) ; les essais unitaires
  ligne à ligne (j'ai lu leurs sorties : 21, 6 et 8 essais passés) ; les sections du texte v2 hors celles citées.

## Verdict

**Utilisable après corrections.** Le dessin répond au mot de Lazar et la preuve du regroupement tient sous des hypothèses à
écrire ; mais douze corrections sont exigées avant qu'un préenregistrement s'appuie dessus, dont trois de fond : le
représentant d'un groupe n'est pas borné par ε, la sortie « générations » n'est pas reproductible au-delà de la
génération 1, et n = 400 ne peut pas être gelé sur le seul juge simplifié. Cadre : les sept réserves du verdict v67
(R-2441) ont chacune une réponse au §5.2 ; les exigences de R-2442, R-2443, R-2461 et R-2467 sont toutes traitées.

## Corrections exigées

**E-1 — Le représentant d'un groupe n'est pas « à ε près » du meilleur membre (§3.4).** La distance d = min des deux
projections vaut zéro entre une loi et ses versions diluées ou tempérées (elles sont dans le nul l'une de l'autre) : elles
sont regroupées, alors que leur gain diffère de bien plus que ε. Contrôle dans mon bac (`controle_medoide.py`, mondes de
développement 0 à 2) : une loi, trois dilutions (0,5 ; 0,2 ; 0,05) et deux tempérées (0,3 ; 2,0) forment **un seul groupe**
(diamètre 0,004 à 0,007) avec des gains de 0,32 à 0,03 nat dans le monde 0, de 0,23 à −0,002 dans le monde 1. En groupe de
deux, les distances sont égales par symétrie et l'empreinte tranche : sur 24 paires regroupées (`controle_medoide2.py`, six
mondes), le médoïde est la **variante affaiblie 5 fois**, avec jusqu'à 0,27 nat de perte ; une fois son gain tombe sous
0,02 : elle mourrait au test de mort et « le groupe est éliminé (aucun second essai) », alors que sa sœur porte 0,28 nat.
La phrase « d'effet borné par ε sur le gain du représentant » est fausse et doit sortir. À fixer : une règle de
représentant, toujours avant tout tirage, qui ne peut pas choisir un membre affaibli (par exemple le membre dont le nul
couvre le mieux tous les autres, distance **dirigée** et non min des deux sens) ; le sort du groupe quand son représentant
meurt ; puis refaire les simulations avec cette règle (les sorties scellées prennent le membre au plus grand log e, la règle
même que la synthèse et la conception rejettent).

**E-2 — La sortie `generations-w12-g3-n400-v1.json` n'est pas reproductible à partir de la génération 2.** Rejeu partiel
(mondes 0 et 1, mêmes graines) : génération 1 égale ; générations 2 et 3 différentes dans les six courses (par exemple monde
0 sans regroupement, génération 2 : 14 promues dans la sortie scellée, 12 au rejeu). Cause établie (`controle_hachage.py`) :
`_generations_course` parcourt l'ensemble de chaînes `connus` en tirant des nombres au hasard ; l'ordre d'un ensemble de
chaînes dépend de la graine de hachage de l'interpréteur, tirée à chaque lancement. Deux lancements à graine de hachage
fixée à 0 sont égaux ; les graines 1 et 2 donnent d'autres résultats. Les chiffres des générations 2 et 3 du tableau du §1.6
(et la recommandation « 3 générations suffisent », Q-1) reposent donc sur un tirage non rejouable. À faire : parcourir
`sorted(connus)`, relancer sous un nom neuf, corriger le tableau. Les autres sorties ne sont pas touchées (rejeux égaux).

**E-3 — n = 400 ne se gèle pas sur le juge simplifié seul (§1.6, Q-5).** L'étalonnage est juste et rejoué, mais il cale le
juge en **un** point : monde S-V1, 2 traits, archive d'une loi, 200 tirages. Le monde riche extrapole sur trois axes non
calés : 8 traits, 400 tirages, archive de 9 à 26 lois (le mélange ajusté sur toute l'archive coûte de la puissance, et rien
ne mesure combien). La tranche [0,02 ; 0,03[ qui porte « le point de 50 % tombe sur g₀ » compte 6 lois (240 jugements), et
les intervalles de Wilson y traitent comme indépendantes des répétitions d'une même loi. Les simulations prennent m = 40
alors que le dessin compte jusqu'à 24 ou 30 cartes plus une vingtaine de lois plantées. Le préenregistrement doit : fixer n
par une règle écrite d'avance, appliquée au banc de calibration **avec le code v68 gelé** ; fixer m sur le décompte réel ;
mesurer **avant** la course la puissance sur un effet faible selon la taille de l'archive (1, 8, 16 lois et plus), sans quoi
une génération 3 vide ne distinguera pas « monde épuisé » de « juge devenu sourd ».

**E-4 — Les simulations ne portent pas sur la famille tirée (§1.6, §3.6, §4.1).** `preparer_monde` appelle
`generer_monde_synthetique` avec son gabarit par défaut : les 12 mondes des sorties détection, doublons, attribution et
générations ont **tous** 7 effets, 3 faibles, aucun trait latent (vérifié dans `detection-w12-r40-v1.json`). La conception
écrit « 12 mondes MR-1 » sans le dire. La dispersion entre mondes (écart-type 0,10 ; 0,21 à 0,54) est donc une borne basse,
et ε, ε_strat, le seuil d'attribution et n sont réglés sur une sous-famille. À dire dans le texte ; refaire sur des gabarits
tirés au banc de calibration ; écrire la règle si le banc conduit à changer un seuil (nouveau secret de calibration).

**E-5 — Le générateur et le vérificateur se contredisent sur le trait latent, et C8 n'applique pas ce que dit le §1.2.**
Le latent reçoit la classe « moyenne » et compte dans la fourchette 2 à 3 : un monde tiré avec latent et 3 moyennes est
**toujours refusé en C1** (3 sur 3 dans mon contrôle `controle_gabarits.py` ; 9,7 % des gabarits tirés, sur 4 000). La
famille réalisée n'est pas la famille dite (un latent implique exactement 2 autres moyennes), et un dixième des tirages est
retiré pour une raison de comptage. Le latent a aussi une taille visée fixe (0,05) et un poids fixe (1/2). Le §1.2 écrit
« indétectable (< 0,1) : refus si elle n'est pas déclarée faible » : le code ne le fait pas (aucune exigence sur les
moyennes ; la moyenne la plus faible du banc est à 0,17). À corriger : compter le latent à part, tirer sa taille, coder ou
retirer la règle, et rapporter les fréquences réalisées au banc.

**E-6 — Les deux régularités signalées ne sont pas les seules (§2.1).** S'y ajoutent, lues dans le code : (3) les deux
effets forts sont toujours des effets principaux, et la sorte est liée à la classe (jamais d'interaction de seuil faible,
jamais de seuil ni de décalage de sous-population moyen) ; (4) un trait ne porte jamais deux effets (sauf le trait de
condition) ; (5) le seuil d'un effet de seuil est toujours dans [0,3 ; 1,0], positif, à deux décimales ; (6) un effet de
sous-population ne touche qu'une sous-population ; (7) les sortes ne sont pas équiprobables après les rejets du gabarit
(« faible, décalage de sous-population » : 45 % des faibles) ; (8) le latent à constantes fixes (E-5) ; (9) le trait de
condition des interactions est celui du premier effet fort, qui est aussi le trait de K1, servi aux proposeurs, environ une
fois sur deux. Le préenregistrement doit classer chacune : retirée, ou assumée comme publique.

**E-7 — Le contrôle de fuite C7 est inutilisable tel quel, et n'a jamais tourné sur une vraie pièce.** Il refuse dès qu'un
paramètre du monde, arrondi à deux décimales, égale un nombre du texte servi. Sur une pièce fictive sans aucune fuite, faite
de 14 nombres ordinaires d'une consigne (0,05 ; 0,02 ; 0,5 ; 1,2…), il refuse **12 mondes sur 30** (`controle_c7.py`). Au
banc du générateur, C7 est « sans objet (aucune pièce donnée) » : le « 12 conformes sur 12 » ne dit rien de lui. Avec les
vraies pièces servies, le retirage (8 au plus) risque de s'épuiser. C'est la coïncidence « 1.3 » de la réserve R-1 de la
v67, rendue bloquante. Or les textes sont gelés avant le tirage du secret (§2.5) : une fuite du monde vers eux est
impossible par l'ordre. À faire : C7 en mesure rapportée (touches listées), refus seulement sur égalité à six décimales, et
l'éprouver sur les pièces gelées au banc de calibration.

**E-8 — La preuve du §3.3 tient, mais ses hypothèses ne sont pas écrites.** Moyenne de valeurs e = valeur e, groupes
fonction des seules lois et d'instances sans issue, e-BH sur les groupes avec m borne fixée : juste. À écrire avec elle :
(a) « majorée par une surmartingale d'espérance ≤ 1 » n'est établi que pour la classe linéaire ; pour le membre tempéré et
incliné, le texte v2 (§3.4) cite le nul v8 : « au second ordre près de l'optimum, sans preuve » ; le regroupement n'ajoute
rien à cette réserve mais la preuve ne doit pas l'effacer ; (b) elle suppose que le code gelé arrête les valeurs e comme le
juge simplifié, ce que personne n'a lu ; (c) elle porte sur l'hypothèse « le monde est dans le nul de l'archive », fausse par
construction dans un monde riche : elle ne borne pas les fausses découvertes au sens de l'oracle. Les simulations en
montrent 11 sur 94 et 12 sur 78 parmi les retenues, plus que α. Le préenregistrement ne doit donc pas reprendre α comme
borne de cette part ; sa tolérance se fixe au banc, ou par une marge sur le juge (question pour Lazar, voir réponse 7).

**E-9 — Devis : le « pire cas » n'en est pas un (§6.2, §6.3).** L'arithmétique est juste (script rejoué, sortie égale), les
hypothèses non. (a) 33 tests par génération = 24 représentants + 9 plantées ; or le jeu planté compte jusqu'à 13 lois à
tester (le monde, jusqu'à 9 « K1 + un effet », 2 diluées, T-ELIM) et 10 dans le cas central, non 9. (b) Le §1.5 ne dit pas
si les vraies sont replantées à chaque génération ; si oui : 37 × 0,80 × 6 + 24 = 201,60 USD, au-dessus du plafond proposé
de 185. (c) Kimi en cinquième proposeur ajoute 6 représentants à tester par génération ; la conception ne compte que ses
appels de proposeur (+ 12 USD). (d) La borne de 0,80 USD par test vient des prix de Kimi (2 / 10) ; avec Opus (4 / 20,
réflexion facturée comme sortie et qui « ne se coupe pas », plan des crédits l. 50) elle mordra : dire ce que vaut un test
coupé par la borne. (e) « Les fausses et copies promues ne sont pas testées » change le dessin de la v66 ; c'est glissé dans
les hypothèses du devis et doit être une décision écrite. Refaire le pire cas par formule, puis les plafonds des deux lignes.

**E-10 — Q-8 prête à Lazar des mots qui ne sont pas les siens.** « Ta décision demande les comparaisons multiples comptées
par groupe » (§3.8) et « ta demande … tenue » (Q-8, option a) : ces mots sont au point 3 de la consigne de la mère au
concepteur. Le mot de Lazar (R-2443) est « il faut regrouper les doublons au sein d'une même génération ». Le regroupement
après le test de mort (temps 1 de la synthèse) y répond aussi. Reformuler Q-8 sans cet argument.

**E-11 — « Certifiée détectable » repose sur 100 graines sans intervalle, et contre l'archive la plus favorable.** Une
composante de puissance vraie 0,75 passe le seuil de 0,8 environ une fois sur sept. La mesure principale D2 compte ces
composantes : fixer la règle sur une borne basse d'intervalle, ou sur plus de graines ; et nommer l'étiquette pour ce
qu'elle est (détectable quand le reste du monde est connu), comme le §1.2 le dit mais non le §4.1.

**E-12 — « Lois inconnues de toute famille de modèles » : dire ce qui est garanti, fermer le choix du secret, corriger une
empreinte.** (a) La garantie est de procédure (aucun modèle ne lit), pas cryptographique : une session Claude lance le
générateur et tient le secret ; l'option (c) de Q-3 empêche qu'un seul **fixe** les mondes, pas qu'une session les
**connaisse**. (b) Rien n'empêche de tirer un secret, regarder, puis en tirer un autre avant d'inscrire l'engagement :
exiger que l'engagement machine soit inscrit et poussé **avant** que Lazar donne sa phrase. (c) Pousser le secret et les
mondes sur une branche privée du dépôt avant le verdict les met à portée de toute session qui clone : les garder hors dépôt
jusqu'au verdict, ou le justifier. (d) Le §2.1 cite le générateur par `46f3ac2d43ef…` ; l'empreinte vraie, celle du tableau
et du compagnon, est `46f3ac2d40ef…` (règle R6).

## Corrections suggérées

- **S-1** Valeur e d'un groupe : les valeurs e des cartes sont arrêtées à m/α, donc un groupe où une seule sœur porte la
  preuve ne passe presque jamais le rang 1. Comparer au banc la moyenne, la forme de la synthèse (valeur e du seul
  représentant) et un arrêt qui tient compte de la taille du groupe, connue avant les tirages.
- **S-2** Réinjection des sœurs : la faire après la course, comme les sentinelles, pas entre deux générations.
- **S-3** Lecture : nommer la catégorie « recombinaison » (retenue à plus de g₀ au-delà de l'enveloppe mais sans composante
  nouvelle couverte). Dans un monde par morceaux, c'est le chemin naturel hors de la classe couverte ; la sonde H1 ne le
  mesure pas (son gain au-delà de l'enveloppe est négatif dans les 12 mondes).
- **S-4** Dire que le regroupement réduit les doublons sans les supprimer : 7,3 lois retenues pour 4,7 idées ; à ε = 0,01,
  2,1 idées sur 3 sont coupées en plusieurs groupes.
- **S-5** Deux mondes ne donnent aucune estimation de dispersion (un degré de liberté) : écrire que l'issue se lit par
  monde, et la règle si les deux mondes divergent.
- **S-6** Plafond de session de 2 USD : pour Fable 5.2 il vaut environ 50 000 jetons de sortie, réflexion comprise, près du
  cas central (35 000). Régler le plafond par modèle, ou dire ce que devient un proposeur coupé.
- **S-7** `ecrire_prive` refuse trois fragments de chemin : préférer une liste blanche de dossiers privés.
- **S-8** Fidélité à la synthèse : « deux seuils, le plus strict » est la position de la seule espèce A ; « composantes non
  séparables fusionnées avant la course » n'est pas traité ; la synthèse certifie contre l'archive de la génération, la
  conception contre le reste du monde (dit au §1.2, à redire au §5.4).
- **S-9** Rapporter les tirages refusés par contrôle, C5 et C6 compris : ils choisissent les mondes où l'attribution marche.

## Réponses aux sept questions

**1. Monde riche et génération aveugle.** Oui sur le fond : 6 à 9 effets sur 8 traits, interactions de deux sortes, trois
classes de taille mesurée, traits leurres. Une ambiguïté à lever : si « traits cachés » veut dire traits non observés, il y
en a au plus un, dans un monde sur quatre environ (un sur douze au banc). Aveugle : oui, aucune loi dans le code, graine
dérivée du secret, du texte scellé et du rang ; le retirage est déterministe et ne passe par aucun regard, donc sans biais
de sélection par un résultat, mais il sélectionne par construction (E-5, E-7, S-9). La garantie est de procédure (E-12).
Les deux régularités ne sont pas les seules : sept autres (E-6).

**2. Vérificateur et détectabilité ; juge simplifié et n = 400.** C0 à C6 tiennent à la lecture ; C7 non (E-7) ; C8 mesure
bien un couple juge × monde mais sa règle « certifiée » est fragile (E-11) et une règle dite n'est pas codée (E-5).
L'étalonnage est honnête et rejoué à l'identique ; il suffit comme base de travail, pas pour geler n (E-3).

**3. Regroupement avant le juge.** La validité au sens O2 est gardée : la preuve tient, sous les hypothèses de E-8, toutes
héritées de la v67 sauf l'arrêt des valeurs e à vérifier dans le code. Le défaut est ailleurs : le représentant (E-1).
Risques pour l'oracle : la loi retenue peut ne pas être celle qui portait la preuve, d'où des fausses découvertes comptées à
tort et une archive qui hérite d'une version affaiblie. Isolement : rien de neuf n'est servi ; le calcul est déterministe et
recalculable ; la réinjection des sœurs gagne à attendre la fin de la course (S-2). Sur « avant ou après le juge », la
divergence avec la synthèse reste ouverte et revient à Lazar, mais sans l'argument de E-10.

**4. Diversité.** Elle ne pilote rien : D1 se calcule après la sélection scellée, D2 se lit une fois après la course, rien
n'est servi, la composition reste jugée sur l'oracle et le coût (N-058). Le regroupement agit sur la sélection, mais c'est
le regroupement, pas la mesure. Préenregistrable après trois choix, pas telle quelle : la règle de « certifiée » (E-11) ; le
seuil d'attribution, choisi sur deux mondes puis éprouvé sur une sous-famille (E-4), avec 12 effets faibles manqués sur 186
présents et 5 attribués à tort ; la référence de ce seuil (I_i ici, chute de la loi plantée dans la synthèse).

**5. Puissance et nombre de mondes.** Détection, doublons, attribution, étalonnage : justes et reproductibles. Générations :
non reproductible au-delà de la génération 1 (E-2) et sur une sous-famille (E-4). L'écart entre simulations et dessin n'est
pas borné comme dit : pour le représentant, non (E-1 ; dans les simulations, sans carte diluée, l'effet est sans doute
petit) ; pour les strates, le sens est connu (plus de groupes) mais rien n'est mesuré. « 2 × 3 » se défend comme base ;
la génération 3 est presque vide en simulation (0,08 à 0,17 promue par monde), ce qui rappelle la réserve R-5 de la v67.

**6. Devis et lignes de GO.** Cohérents avec le script et ses sources (prix de Claude, de Kimi, bornes du devis v66 :
vérifiés). Pire cas sous-compté (E-9) : un pire cas plausible à 2 × 3 dépasse 185 USD sur crédits dès que les vraies sont
replantées à chaque génération ou que Kimi propose.

**7. Questions manquantes pour Lazar.** (i) Définition de « vraie découverte » (oracle v60 **et** enveloppe) et tolérance
sur les fausses découvertes au sens de l'oracle, ou marge sur le juge : la conception la laisse au rédacteur, alors qu'elle
touche la revendication O2 (N-064). (ii) Où vit le code du générateur v68 et quand il devient public ; où sont gardés le
secret et les mondes avant le verdict (E-12 c). (iii) Sens de « traits cachés » (réponse 1). (iv) Dans Q-3, l'ordre des
engagements. (v) Dans Q-7, le coût des tests ajoutés par Kimi proposeur. (vi) Tester ou non les fausses promues (E-9 e).

## Rejeux (interpréteur système, Python 3.13.18, numpy 2.5.3, comme le concepteur ; sorties dans `rejeux/` de mon bac)

| sortie scellée | rejeu | résultat |
|---|---|---|
| `attribution-w12-v1.json` | complet | champ `resultat` égal |
| `etalonnage-r1000-v1.json` | complet, 1 000 répétitions | champ `resultat` égal |
| `variantes-v67-v1.stdout` | complet | égal à l'octet |
| `devis-multi-generations-v1.json` | complet | égal |
| `detection-w12-r40-v1.json` | mondes 0 à 2 (mêmes graines par monde) | les 3 mondes égaux |
| `doublons-w12-v1.json` | mondes 0 à 2 | les 3 mondes égaux |
| `generations-w12-g3-n400-v1.json` | mondes 0 et 1, trois conditions | génération 1 égale ; **générations 2 et 3 différentes** (E-2) |

Les tableaux des §1.6, §2.4, §3.6 et §4.1 de la conception recopient fidèlement les sorties scellées (contrôlé champ par
champ pour l'étalonnage, la détection, les doublons, les générations, le banc du générateur). Contrôles ajoutés par moi, dans
le bac : `controle_medoide.py`, `controle_medoide2.py` (E-1), `controle_hachage.py` (E-2), `controle_gabarits.py` (E-5),
`controle_c7.py` (E-7). Ils utilisent les outils scellés de la conception, sans les modifier.

## Limites de cette contre-lecture

- Les rejeux de la détection, des doublons et des générations sont partiels (3, 3 et 2 mondes sur 12).
- Mes contrôles E-1, E-5 et E-7 portent sur des mondes de développement et sur des variantes ou une pièce que j'ai écrites ;
  ils établissent que le défaut existe, pas sa fréquence avec de vrais proposeurs.
- Je n'ai pas vérifié la preuve contre le code gelé du juge, que personne n'a pu lire ici.
- Synthèse du collisionneur : citée fidèlement par la conception, aux trois points de S-8 et à celui de E-10 près.
