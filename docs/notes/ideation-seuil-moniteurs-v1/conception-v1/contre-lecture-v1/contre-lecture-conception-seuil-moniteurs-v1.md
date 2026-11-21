# Contre-lecture — conception de la course « seuil et moniteurs » de l'organisme d'idéation — v1

- Signé : contre-lecteur de la conception seuil et moniteurs, modèle O. Contre-lecteur neuf (règle R2) : je n'ai écrit aucune pièce de l'organisme d'idéation, du papier « dopamine » ni du collisionneur. 2026-11-21. Python 3.13.18.
- Statut : pièce de travail. Aucun appel à un fournisseur, aucune clé lue ni nommée, aucune dépense, aucune écriture dans un dépôt, aucun commit, aucun lancement. Aucun refus de permission, de classifieur ou de garde pendant le travail.
- Pièces relues, toutes en entier : le mandat (`docs/notes/ideation-seuil-moniteurs-v1/mandat-redacteur-conception-course-seuil-et-moniteurs-v1.md`, `4f1fd30358a35e8f1482efeb962730881d213a6306054fd52b096488288f1159`, recalculée) ; les sept fichiers de `conception-v1/`, table `empreintes-dossier-v1.txt` (`ec6982ebd5fe3957f4d9cae0ef999c4f34e2724da1cdb59c563f5f6466bda2ec`), vérifiée par `env -C … sha256sum -c` : sept « OK ».
- Sources lues sur `origin/main` par `git show` redirigé, après `fetch` : `origin/main` est aujourd'hui au commit `1e91aa3bbe147ae6bab76899515b3f2c88b3a34f`, postérieur au `55f7f6e1…` du rédacteur. J'ai extrait les registres aux deux commits ; au `55f7f6e1…`, `registres/go.md` rend `38f63a0d…` et `registres/decisions.md` `352e3ea9…`, égales aux empreintes du devis (S6). Les lignes citées sont les mêmes aux deux commits ; la ligne R-4377 (décisions de la mère) n'existe qu'au commit récent.

## 0. Verdict : **À corriger**

1. **Le devis est juste au centime** et rejoué à l'octet ; ses entrées sont égales à leurs sources. Un défaut de cohérence : la règle de réservation de l'étage ne laisse partir que dix-neuf candidates au cas haut, non vingt (§ 1.4).
2. **Les faits cités sont fidèles**, à trois retouches près : un chemin incomplet (`paquet/`), « déclaré » au lieu d'« estimé » pour une clé, l'accord de l'option (a′) non cité (§ 2).
3. **N-058 est tenu** ; Kimi est absent ; aucune clé n'est nommée hors des désignations permises ; une phrase servie fait passer l'hypothèse du programme pour une conclusion (§ 3).
4. **Le préenregistrement court a la bonne raison** (R1) et tous ses éléments, présents ou marqués « attend ». Deux trous : le test propre de la fiche n'est jamais lu, et rien n'oblige à sceller les fiches avant le tirage des candidates (§ 4).
5. **Mondes plantés : deux défauts de fond**, à corriger avant le gel (D-M5). (a) Le critère « sans gain » contredit le témoin qui doit le vérifier : une règle égale à la base « tient ». (b) La mort « invalide » « avec une confiance dite » se lit sur un nombre fini d'épisodes d'épreuve, si bien qu'une règle valide peut mourir du bruit. De plus, savoir sur quel monde une fiche « déclare tenir » ses suppositions demande une lecture : il faut un champ fermé (§ 5).
6. **L'apport au-delà du collisionneur est réel**, pourvu que l'étage existe (§ 6).
7. **Aucune réserve du rédacteur ne bloque la conception** ; D1 bloque le départ, non le gel (§ 7).

Corrections : vingt-trois remplacements à texte exact, en cinq fichiers JSON (§ 8). Chaque ancre est comptée une fois par `grep -c -F -e`. L'essai sur copie est passé pour les cinq fichiers.

## 1. Le programme du devis

1. **Rejoué deux fois** (`python3 -B …/calcul_devis_course_seuil_et_moniteurs_v1.py > sortie-1.json`, puis `sortie-2.json`) : `cmp` muet entre les deux, et muet aussi contre la sortie versée `calcul-devis-course-seuil-et-moniteurs-v1.json` (`744cc532…`).
2. **Arithmétique seule** : oui. Le programme importe `json` et `decimal`, ne lit aucun fichier, n'ouvre aucun réseau, n'emploie aucun aléa. Il arrondit au demi supérieur par `Decimal`.
3. **Entrées égales à leurs sources** (devis v6, `d825cb31…`, et préenregistrement court v9, `864f39a7…`, relus et empreintés) :
   - S1, devis v6, ligne 42 : 4,17 ; 4,75 ; 7,43 ; 17,58 ; 24,72 ; aiguilleur 4,59 ; juges 6,86 et 2,41. Égal.
   - S2, préenregistrement court v9, ligne 197, paragraphe « Coûts par rôle du premier relais » : facteurs 1,1940 ; 4,4575 ; 5,1046. Égal.
   - S3, devis v6, ligne 44 : plafond 150 ; 6,05 par appel ; témoins 1,18 et 5 ; part au pire 66,55. Égal.
   - S4, devis v6, ligne 45 : environ 0,005. La ligne de 1 se trouve au préenregistrement court v9, ligne 172. Égal.
   - S5, devis v6, ligne 124 : répartition 7,43 + 17,58 + 4,59 + 6,86 ; 4,17 + 24,72 + 2,41 ; 4,75. Égal.
   - S7, R-3984 : « sur devis de quelques dollars ». Égal.
   - S8, `registres/etat.md` au `55f7f6e1…`, ligne 628 : « crédit du loueur 90,56 USD ». Égal.
4. **Cas bas, haut et pire, refaits à la main :**
   - génération : 58,65 + 4,59 + 9,27 = 72,51 ; et 70,0281 + 20,4599 + 47,3196 = 137,81 ;
   - étage : 20 × 58,65 / 55 = 21,33 ; et 40 × 24,72 / 11 × 1,194 = 107,33 ;
   - totaux : 72,51 + 21,327 + 2 + 1,18 + 0,005 = **97,02** ; 137,808 + 107,330 + 5 + 5 + 1 = **256,14** ; 260 + 10 + 5 + 1 = **276**. Les trois sont justes.
   - Les variantes (73,70 / 143,81 / 156 ; 87,75 / 208,82 / 276) et les relais (36,46 / 85,34 ; 31,30 / 46,80 ; 4,75 / 5,67 / 66,55) sont justes aussi.
   - **Défaut, non chiffré au devis : le cas haut de l'étage est incompatible avec sa propre règle de réservation.** Le devis, § 3, dit : « l'étage ne lance une candidate que si son pire (12,10) tient dans ce qui reste ». Au coût du cas haut, une candidate coûte 5,366 USD. Après dix-huit candidates, 96,60 sont dépensés : la dix-neuvième part, puisque 96,60 ≤ 110 − 12,10 = 97,90. Après dix-neuf, 101,96 sont dépensés : la vingtième ne part pas. Au cas haut, l'étage joue donc dix-neuf candidates et dépense 101,96, non 107,33. Il faudrait un plafond d'au moins 114,07 pour les jouer toutes. Le contrôle du programme, « plafond_de_l_etage_couvre_son_cas_haut : true », est vrai mais ne dit pas cela. Même effet pour le levier « dix candidates » (§ 5 du devis) : à 55, huit seulement partent, et il faut 60,40 pour les dix. Le préenregistrement court dit « Vingt candidates : ce que l'étage paie à son cas haut sous 110 USD » : c'est inexact. **Corrections K-P5, K-D1, K-D2.** Le choix entre garder 110 (la vingtième « non jouée » au cas haut) et monter le plafond revient à la mère au gel. Le second change la ligne de GO.
5. **« Règles du rédacteur » dites comme telles** : oui au devis (§ 0, avant-dernier point ; § 3), dans le programme (R1, R2) et au rapport pour la machine (§ 3, point 3). Elles ne le sont pas au rapport pour l'étage (§ 3, point 3), ni au préenregistrement court là où il cite les trois totaux (« Prédiction »). **Corrections K-R1, K-P1.**

## 2. Fidélité des faits cités

| fait | source vérifiée | empreinte | jugement |
|---|---|---|---|
| véhicule absent de `main` | `git cat-file -e origin/main:` sur le lanceur version 9 et sur le rapport de la version 68 : « exists on disk, but not in 'origin/main' » | — | fidèle |
| version 68 en moteur simulé seulement | rapport du développeur de la version 68, sur le disque de la branche `lot/compte-organisme-v1` (branche courante) : l. 6, « le lanceur v68 refuse le moteur réel par construction » ; l. 89 et 91 | `ad42b7229a8e37aae823b1041a3acf1db91ee4053f5fec61136b6fd178b59aa6`, égale | fidèle |
| fichiers de la version 68 | `course2_v68.py` `c1aeab4c…` et `ideation_v68.py` `6fce1735…` : égales, mais **sous `orchestrateur-v68/paquet/orchestrator/…`**, non sous `orchestrateur-v68/orchestrator/…` | — | chemin incomplet, **K-O8, K-O9** |
| lanceur version 9 qui refuse l'étage | `scripts/lancer_course_auto_conception_v9.py`, l. 2274-2275 : `raise Refus("configuration : pas de tests de mort dans cette course")` | `1b47c1cf…`, égale | fidèle, citation exacte |
| lanceur version 10 au branchement éteint | `…_v10.py`, l. 8-11, 575, 602 ; R-3861 (« éteint égal à la v9 à l'identique ») | `f4196ec5…`, égale | fidèle. À noter (l. 2702-2703) : la version 10 refuse `tests_de_mort_reels` seul, parce que l'orchestrateur `a41b7b50` ne joue l'étage qu'entre deux générations ; cela confirme que K = 1 avec un étage après la génération demande une version neuve |
| lanceur 11 inexistant | `sha256sum` par son chemin : « No such file or directory » ; absent aussi de `origin/main` (règle R11) | — | fidèle |
| GO-2026-11-20-05, point 1a, pour le palier 1 seul | `registres/go.md`, l. 536 : « les tests de mort sans rien servir d'abord, pour la seule épreuve du palier 1 de l'héritage […] l'allumage réel reste soumis à un devis et à une ligne d'accord » | registre au `55f7f6e1…` : `38f63a0d…` | fidèle. « Accordé » est un peu fort, puisque même au palier 1 l'allumage réel attend un devis ; l'ordre, § 0, point 3, et le rapport, § 3 (2), le nuancent |
| point 4b | même ligne : machine jetable sous le devis du premier étage payant, essai du bac en première étape | idem | fidèle |
| R-3882 | `registres/decisions.md`, l. 4020 : bac local, exécuteur factice, comparateur sans modèle, deux manques (juge statistique ; aucun générateur à plusieurs lois) | `352e3ea9…` | fidèle |
| GO-2026-11-19-75 | l. 508 : expérimentateur modèle gardé, lecteur non visé | `38f63a0d…` | fidèle |
| option (a′), R-4066 | R-4066 la propose ; **elle est accordée par GO-2026-11-20-10, point O3**, que l'ordre ne cite pas | — | **K-O10** |
| soldes (devis, § 6) | R-4258 : « estimation de l'organisme, non un relevé » pour toutes les clés. Le devis écrit « environ 214,00 **déclaré** » pour Luc | — | **K-D3** |
| Minuit, Rigaud, deuxième et troisième relais | GO-2026-11-21-02 ; GO-2026-11-20-64 ; R-4342 ; R-4356 (marge 24,90 ; 439,59 sous 456) | — | fidèles |
| collisionneur v9 v3 | code, l. 49-50, 237-245 : étage III, conception à l'aveugle 3 500 mots, critique 3 000, réponse 3 500 ; GO-2026-11-21-14 (23,45 au pire) | `850df311…`, égale | fidèle |
| faits et question neutres | `c8c7fb32…`, `a5fbe898…` : égales | — | synthèse du § 8 de la question fidèle aux pages citées, sauf une phrase (§ 3 ci-dessous) |

**Décisions de la mère (R-4377, 06:53:59Z, « D-M1 à D-M5 selon les recommandations »).**
- D-M1 est tenue : ordre, § 9, point 3 ; arrêt n° 13.
- D-M3 est déclarée : rapport, § 6, point 1.
- D-M5 : rien à vérifier avant le gel.
- **D-M2 et D-M4 ne sont pas écrites dans les pièces.** L'ordre, § 2.3, laisse les deux chemins ouverts. L'ordre, § 7, dit seulement « un développeur qui n'est pas un proposeur », moins que D-M4 (« une autre lignée que les cinq espèces et que l'expérimentateur »). Le rapport, D-M2, dit que « le mandat des mondes part » tout de suite, alors que la mère le fait partir après ses deux notes de conception. **K-O6, K-O7.**

## 3. N-058, Kimi, clés, neutralité

1. **N-058** (`854f2724…`, relu) : il interdit de choisir des **agents** sur le verdict d'un juge ; il permet de choisir des fiches par la sévérité du test. Les pièces le tiennent :
   - les candidates sont tirées par graine, jamais par le rang des juges (ordre, § 6) ;
   - les classes d'issue sortent du calcul ;
   - les juges ne voient aucune issue, et I1 est rapporté « pour information » ;
   - la composition ne se réduit pas sur cette course (ordre, § 5) ;
   - aucun juge ne siège à l'étage, conformément à GO-2026-11-19-76, point 3.
   
   Une remarque, non bloquante (Rem-1). Le portier est un modèle, et ses classes « hors case » et « sans test » décident qui peut devenir candidate. C'est un choix de fiches sur la forme, permis. Mais « hors case » se calcule par programme (champs fermés égaux à ceux de la case servie). Mieux vaut le calculer ainsi, et ne laisser au portier que « sans test » et « mise à part ».
2. **Kimi** n'apparaît que trois fois, toujours comme « absent » (ordre, l. 93 ; devis, l. 129 ; préenregistrement court, l. 31). Aucun relais ne passe par lui.
3. **Clés** : aucun nom de variable, aucune valeur. Seules paraissent les désignations du registre (Minuit, Luc, Rigaud, et les relais Google et OpenAI, désignés ainsi au registre). Aucun identifiant de modèle n'est écrit dans les pièces.
4. **Neutralité.** La question, § 3, met les deux issues au même rang ; le préenregistrement court, « Prédiction », aussi. **Un écart** : la question, § 8, sert sous le titre « Ce qui est déjà décidé » la phrase « une sonde de réussite attendue lirait l'échec attendu, non l'intention […] ». Or les faits, § 3, la donnent comme **« Hypothesis »** du programme, attachée au contraste principal (saboteur au dommage confirmé contre honnête qui échoue). Servie ainsi, elle incline les fiches de la voie « moniteur tiré du signal ». **K-Q3.** Une incohérence aussi : la question, § 1, dit que le collisionneur porte les « points 1, 2 et 5 », et le § 6 dit « 1, 2, 4 et 5 ». **K-Q1.**

## 4. Le préenregistrement court

1. **La raison de R1** est juste (rapport, § 5) : avec l'étage, des simulations décident du sort d'une proposition ; R1 vise « simulation comprise ».
2. **Les éléments exigés :**
   - Hypothèse : présente. « Aucune hypothèse du programme » ; à la place, l'objet et la règle du jeu sont gelés, en sept points, et deux hypothèses de travail sont dites.
   - Prédiction chiffrée et signe : « aucune pour la course », avec sa raison (R3) ; elle est renvoyée aux fiches ; les issues contraires sont au même rang.
   - Métrique : présente (V1 à V6, M1 à M5, C1, C2, I1, I2).
   - Seuil : présent.
   - Plan d'analyse : présent.
   - Critères de lecture gelés : présents.
   - Liste d'arrêt : treize arrêts.
   - Ce qui attend est marqué : « Ce qui reste à écrire avant le scellement », six points, et « Contre-lecture : à faire ». **Conforme sur la forme.**
3. **Trou 1 : le test propre de la fiche n'est jamais lu.** La fiche doit écrire sa prédiction, son signe et l'issue qui la tue, sinon elle n'est pas candidate. Mais le verdict ne suit que les deux morts de la course. Le préenregistrement dit « chaque candidate porte sa propre hypothèse […] et un programme dit si elle meurt » : ce n'est pas ce que le plan fait. Il faut rapporter l'issue de la prédiction de la fiche, à part, sans qu'elle change la classe. **K-P3 (mesure M6).**
4. **Trou 2 : scellement des fiches avant le tirage.** R1 veut qu'aucun résultat ne soit lu avant le scellement. Rien n'oblige à sceller les fiches et les classes du portier avant le tirage des candidates et le départ de l'étage. **K-P6 (arrêt n° 14).**
5. **Intervalles** : voir § 5, point 2. **K-P2, K-P4.**

## 5. Les mondes plantés

1. **Les deux morts sont calculables sans juge** quant au calcul : intervalles, base, comparaison. **Mais leur portée ne l'est pas.** « Sur un monde dont la fiche déclare tenir les suppositions » demande de rapporter le texte libre de la fiche (point 2 de la question, « ce qu'elle suppose ») aux familles A à G. Ce rapport est une lecture, faite par l'expérimentateur, par la mère ou par un modèle. Et il décide entre « morte » et « fragilité ». Il faut un champ fermé `suppositions_declarees` et une table famille → supposition cassée, scellée avec les mondes. **K-Q2, K-O5.** Le champ nomme deux suppositions hors de l'axe (« même loi dans toutes les tranches », « scores continus ») : cela touche à peine les familles D et G, que l'axe « unité de calibration » laisse déjà deviner.
2. **« Invalide » « avec une confiance dite » est faussé par le bruit de l'épreuve.** V1 est « la part des épisodes honnêtes d'épreuve alertés ». Une règle valide dont le taux conditionnel vaut exactement 1 % dépasse 1 % sur un échantillon fini d'épreuve à peu près une fois sur deux. La part des tirages où V1 dépasse 1 % est donc gonflée, et une règle valide meurt. La vérité plantée donne le taux vrai conditionnel, 1 − F(seuil), exact ou par le tirage scellé de dix millions de points : c'est lui qu'il faut lire. De même, Clopper-Pearson sur les épisodes mis en commun traite comme indépendants des épisodes qui partagent le seuil d'un même tirage ; l'unité doit être le tirage. **K-O2, K-O3, K-P2.**
3. **« Sans gain » contredit son témoin.**
   - Le critère : « la borne haute de l'intervalle à 99 % de V3 ne dépasse pas la puissance de la base ».
   - Le témoin (ordre, § 6) : la base jouée contre elle-même « doit sortir morte, sans gain par construction ».
   - Or, pour une règle identique à la base, la borne haute de l'intervalle dépasse l'estimation ponctuelle, donc la puissance de la base. La règle **tient**, et le témoin est manqué par construction : aucun étage (arrêt n° 3).
   - Sur le fond, le critère laisse tenir toute règle qui n'est pas pire que la base, alors que la lecture gelée dit « morte, sans gain : ne fait pas mieux que la base ».
   
   Correction : un écart apparié de puissance (mêmes tirages), dont la borne basse à 99 % doit dépasser zéro. **K-O1, K-P4.**
4. **La base « seuil au plus grand score » est bien définie à trois précisions près**, à écrire. (a) Par tranche, avec une inégalité stricte : l'alerte est « strictement supérieur ». (b) Sa puissance est calculée sous la même condition que celle de la candidate. (c) **Sur la tranche de quarante épisodes de la famille D, elle est elle-même invalide** : 1/41, soit environ 2,4 %, plus que 1 %. Comparer une candidate à une base invalide n'a pas de sens ; ce couple est à rapporter à part. Avec des ex æquo (famille G), l'inégalité stricte garde le taux sous 1/(n + 1). La réserve 4 du rédacteur (1/(n + 1)) est juste pour des scores continus et des tranches de deux cents ou quatre cents épisodes. **K-O4.**
5. **Ce qui attend** (non bloquant, à geler avec les mondes, après les deux notes de la mère) : le « signal moyen » des mondes de moniteurs (valeur de γ), le budget b, le risque dit du témoin invalide (« dit garanti avec confiance » : à quel risque ?), la méthode de l'intervalle apparié, et le taux de mort par hasard du témoin valide, déjà prévu au complément de valeurs.
6. **Rem-2, famille de mondes tenue à l'écart.** Aucun monde n'est jamais montré aux proposeurs : « tenue à l'écart » n'a donc de sens que par rapport aux suppositions servies. Je suggère de lier la famille de mondes tenue à l'écart à la valeur de supposition dont la famille de cases est tenue à l'écart, par la même graine (B ↔ queue, C ↔ honnête qui échoue, E ↔ pas indépendants, F ↔ dérive). Ainsi la famille tenue à l'écart éprouve une supposition qu'aucun proposeur n'a été invité à mettre à l'épreuve. Le choix revient à la mère.

## 6. L'apport au-delà du collisionneur

**Réel.** Le collisionneur (code relu, l. 49-50 et 237-245) rend des textes et des critiques croisées, sans aucune exécution. La course rend, pour chaque candidate, un verdict calculé contre une vérité plantée et une base nommée. Elle couvre une grille de cases tirée par graine, avec une famille tenue à l'écart, et met le coût par espèce en face de l'oracle. Les doublons (six points libres, critique croisée, plans sur épisodes réels) sont écartés, et l'étiquette « déjà au collisionneur » est posée après coup, sans rien servir (D-M1). Ce n'est pas un doublon déguisé.

**Deux limites, dites pour Lazar.** (1) Sans l'étage, la course redevient un doublon : le rapport, § 2, le dit. (2) Sur la voie des règles de seuil, une candidate qui « tient » sur des lois choisies par nous redécouvrira souvent une statistique connue (quantiles conformes, valeurs extrêmes) : la question l'admet comme recevable. La valeur propre de la course est surtout dans les morts, les fragilités et les candidates des voies du papier, non dans des « règles qui tiennent ».

## 7. Les réserves du rédacteur

Le § 7 de son rapport porte les **décisions** ; ses réserves sont à la question, § 9 (trois), à l'ordre, § 12 (quatre), et au rapport, § 6 et § 8. Je les juge toutes.

- **Aucune ne bloque la conception.**
- La réserve 2 de l'ordre (l'étage sait-il projeter un test écrit pour ces mondes ?) bloque le **départ** jusqu'à l'essai à blanc. Elle est bien placée en tête des épreuves.
- La réserve 4 de l'ordre est juste, mais incomplète (famille D, § 5, point 4).
- La réserve 3 de la question (partie servie non dérivée, garde de motifs non jouée) est à lever avant le scellement, comme elle le dit.
- L'écart du rapport, § 6, point 7 (lecture sur le disque de la branche) est déclaré et nécessaire.
- **D1, la décision de Lazar d'étendre le régime « tests de mort réels », bloque tout étage réel** : sans elle, la course n'a pas lieu sous cette forme.

## 8. Corrections (outil `scripts/remplacer_texte_exact_v1.py`)

Cinq fichiers JSON dans mon dossier, un par pièce, chacun avec son compagnon. Chaque ancre est comptée **1** par `grep -c -F -e` dans la pièce visée.

| fichier | empreinte | pièce visée | remplacements |
|---|---|---|---|
| `corrections-ordre-v1.json` | `4ceab8d3456ac48ee17b7f73ed7c1a6cc3875e99c73f2a807e89c6b1acee927a` | ordre | K-O2 « invalide », unité ; K-O1 « sans gain » apparié ; K-O3 V1★ ; K-O4 base précisée ; K-O5 « déclarer tenir » par programme ; K-O6 D-M4 ; K-O7 D-M2 ; K-O8, K-O9 `paquet/` ; K-O10 GO-2026-11-20-10 (10) |
| `corrections-preenregistrement-v1.json` | `5a03382d3fa3dd343e8def55a084d6734c748310d4591300539a8719c5c260d9` | préenregistrement court | K-P1 règles du rédacteur ; K-P2 intervalles ; K-P3 M6 ; K-P4 « sans gain » ; K-P5 dix-neuf candidates au cas haut ; K-P6 arrêt n° 14 (6) |
| `corrections-question-v1.json` | `3dc92cee211142ee547b53ab93ef5062f8cdeffad6a60b3e991e49c4e7b47b55` | question | K-Q1 points 1, 2, 4 et 5 ; K-Q2 champ `suppositions_declarees` ; K-Q3 hypothèse, non conclusion (3) |
| `corrections-devis-v1.json` | `8f611bfa1b68537d1ae5464b818fcbc2c7d3fadbd2d9355f9034e4236e81aeec` | devis | K-D1 réservation au cas haut ; K-D2 dix candidates ; K-D3 Luc « estimé » (3) |
| `corrections-rapport-v1.json` | `d0436f84dd1601887607128280ba191d4fbbb2594843cd707dde7bdb964adae6` | rapport | K-R1 règle du rédacteur (1) |

**Essai sur copie** (dossier `essai/`, copies des pièces, d'empreintes égales à la table du dossier) : les cinq appels rendent « FAIT ».

| pièce | remplacements | empreinte de la sortie d'essai |
|---|---|---|
| ordre | 10 | `816d15a1c42fa0695bfb4cf8c278d3fa64df3d978b3bd42447067e17e6c5df01` |
| préenregistrement court | 6 | `795840ce200b2ce8297e5d0d97792633063c5ddfc47630ab9c1d519748499c08` |
| question | 3 | `e5776d3ea37c8af165cfec992387f27b14b1729799a9db9373eb0b8305542749` |
| devis | 3 | `4d7323e90b0794b26e93d9a55a9488ed6a89c5153f00f6d74afe616d3ee6bfa2` |
| rapport | 1 | `b52a939c39d86727fd3e1af4d8abddce656cb7fbc1412403fedacc2cdbbb34a5` |

Le programme du devis et sa sortie ne changent pas. Les chiffres neufs (101,96 ; 8,04 ; 114,07 ; 60,40 ; huit candidates) sont écrits comme faits à la main et hors de la sortie. Si la mère monte le plafond de l'étage, une version 2 du programme est due.

## 9. Remarques non bloquantes

- Rem-1 : « hors case » à calculer par programme (§ 3, point 1).
- Rem-2 : lier la famille de mondes tenue à l'écart à la supposition tenue à l'écart (§ 5, point 6).
- Rem-3 : le contrôle C2 (cinq seconds programmes écrits par un autre développeur) n'est pas au devis. À zéro dollar s'il est fait en session, à compter sinon.
- Rem-4 : les rôles de la clé Luc dans la course « nouvelles attaques » (aiguilleur, espèce 4), au devis, § 6, sont sans source citée.
- Rem-5 : l'ordre, § 2.1, ne recalcule aucune empreinte de fichier pour le dépôt à part de l'orchestrateur (`a41b7b50`). C'est dit ; je n'ai pas pu le vérifier non plus, ce dépôt n'étant pas dans les pièces.

## 10. Pour la mère et pour Lazar

**Pour la mère.**
- Appliquer les vingt-trois remplacements, puis geler (D-M5).
- Trancher le plafond de l'étage : 110, avec la vingtième candidate « non jouée » au cas haut, ou au moins 114,07, ce qui change la ligne et le programme.
- Geler avec les mondes la méthode de l'intervalle apparié, V1★ et la table famille → supposition.
- Décider de Rem-1 et de Rem-2.

**Pour Lazar.**
- D1 (régime « tests de mort réels » pour cette course) est la condition de tout étage réel.
- D2 (260 + 16 = 276 USD) tient au centime ; si la mère monte le plafond de l'étage à 115, la ligne devient 265 et le plafond total 281.
- D3 (clés) : les soldes du devis sont des estimations, non des relevés.
- Sur le fond : la course éprouve des règles sur des lois choisies par nous ; une règle qui « tient » est une candidate, jamais une méthode validée.

— contre-lecteur de la conception seuil et moniteurs, modèle O
