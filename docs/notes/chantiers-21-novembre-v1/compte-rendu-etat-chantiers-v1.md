# Chantiers du 21 novembre : compte rendu d'état (v1)

- **Date** : 2026-11-22, vers 10:50 UTC. **Auteur** : session fille des chantiers du 21 (Opus 5.5), qui orchestre et ne conçoit pas (R-3735). Pièce de classe C, non contre-lue. Aucune dépense, aucun appel à un fournisseur.
- **Mandat** : mot de Lazar « go lancement » (GO-2026-11-22-40) pour trois chantiers : le hasard du défenseur comme preuve ; les épreuves du devin ; l'audit après coup, à plancher et à l'enjeu, avec la boucle audit, recapture et réapprentissage. Le banc à vérité plantée est porté par une autre session : je n'y touche pas.
- **Lu** : CLAUDE.md ; N-076 v1 (`49b664c1…`), son erratum 1 (§ 3, 6, 7, 8, 9, 13) et son erratum 2 ; la note de Fable sur l'attaquant informé (`c23a1034…`, propositions 2.1, 6.1, 6.2, D-4) ; R-4541, R-4552, R-4623, GO-2026-11-21-57 et GO-2026-11-22-40 ; la réponse de Fable sur la boucle audit-recapture v2 (`3bc8585c…`, verdict, § 6, § 7, décisions) et sa vérification « conforme » ; les réponses 17 (tirage au hasard) et 19 (équipe rouge). N-075 v3 et son erratum 3 v2 sont connus par les renvois de ces pièces : je ne les ai pas relus en entier.
- **Routine de reprise** : empreintes de lancement conformes. La vérification de l'arbre signale 39 problèmes (compagnons absents ou mal nommés, par exemple `registres/passations/2026-11-22-0800-relais-mere-sortante.md.sha256`). Ils existaient avant moi, et je n'y ai pas touché. Instances de calcul : je n'en ai lancé aucune ; l'inventaire revient à la mère. Tests : voir le canal.

## Chantier 1 — Le hasard du défenseur comme preuve

**Ce qui existe.**
- L'énoncé retenu (N-076, § 3) : par épisode, le harnais tire une condition sans rapport avec la tâche ; un test de permutation donne une p-valeur exacte pour le nul « la conduite ne dépend pas de la condition ». Le jumeau honnête, soumis au même tirage, est le témoin obligé : le test meurt si le jumeau rejette autant que le saboteur.
- Ce qui change dans le programme, d'après N-076 : les contrôles croisés (l. 136) passent à une condition tirée par épisode ; la mesure de la conscience d'évaluation reste le préalable (N-053, point 3) ; la phase 1 reçoit un bras rapporté, sans critère de porte.
- Matière de conception : la note « percée », § 7.1 (candidat C3) ; la réponse 17, fonction 3 (« fournir la référence », parent : Fisher 1935) et fonction 5 (perturber le contexte).
- Voisins nommés, qui occupent une part : Hasan (2604.13301), Krakovna et al. (2605.29729), Needham et al. (2505.23836), Greenblatt et al. (2312.06942), « Blindfold » (2610.37055).

**Ce qui manque.**
1. Le verdict d'antériorité. Une seule requête a été faite, et rien ne se revendique avant ce verdict.
2. La spécification du test exact et de son monde planté : un saboteur conditionnel planté, un jumeau insensible et un jumeau sensible. Elle doit fixer la statistique, l'unité, la permutation (stratifiée par tâche ou non), les tests de mort, la puissance en fonction du nombre d'épisodes, un cas sain et un artefact (R5).
3. L'inventaire, par étiquettes et sans lire de résultat, des régimes « observé » et « non observé » déjà joués sur les mêmes tâches.
4. La place du préalable : la mesure de la conscience d'évaluation doit-elle précéder la conception, ou seulement la mesure ?

**Première pièce à écrire** : la conception du test exact et de son monde planté, par Fable (conception d'épreuve). Elle doit dire elle-même si la simulation est un instrument (classe B) ou une expérience décisive, qui demanderait un préenregistrement scellé (R1). Viennent ensuite le code, écrit par Opus et contre-lu par un autre Opus.

## Chantier 2 — Les épreuves du devin

**Ce qui existe.**
- L'énoncé retenu (N-076, § 6.3 ; GO-2026-11-21-54, D-4). Devin sur la lecture de la sonde : un prédicteur reçoit tout ce que l'agent observe après les décisions du harnais. Devin sur la pièce d'audit : un prédicteur reçoit toute la vue de l'agent avant l'action. Une prédiction au-dessus du hasard suspend la garantie qui s'appuyait sur le secret.
- La règle : « le devin réfute, il n'atteste pas ». Une borne haute de la fuite demande un couplage apparié des deux branches lancées du même état, comme dans « Blindfold ».
- Le statut d'instrument : classe B, épreuves d'admission du harnais avant toute course qui s'appuie sur un secret.
- La note sur l'attaquant informé, propositions 2.1 et 6.2 : un premier pas (inventaire par un agent habilité) et les canaux à couvrir (horodatages, charge, relances, verdicts et blocages qui reviennent dans le contexte).
- La boucle v2, épreuve 11 (canal de retour) : la courbe est prototypée, le devin reste à écrire.

**Ce qui manque.**
1. L'inventaire, harnais par harnais, de ce que l'agent observe après un aiguillage et de ce que le chemin d'audit peut toucher. Il revient à un agent habilité, sur le code et les métadonnées seulement. **À trancher par la mère** : quels harnais (organismes discrets ? bras A ? banc de la boucle ?) et quelles habilitations, pour ne lire aucun contenu cloisonné.
2. La spécification des deux devins : entrées, familles de prédicteurs (du plus simple au plus fort), statistique de rejet exacte, puissance, monde planté à fuite connue (taille plantée, fuite nulle, fuite par horodatage), et sort de la garantie après réfutation.
3. Le code et ses essais (cas sain : devin au hasard ; artefact : fuite plantée retrouvée).

**Première pièce à écrire** : la conception des deux devins par Fable. L'inventaire est un travail de classe C sans dépense, qui peut se faire en parallèle par un agent Opus dès que la mère a nommé les harnais.

## Chantier 3 — L'audit après coup, à plancher et à l'enjeu, avec la boucle audit, recapture et réapprentissage

**Ce qui existe.**
- Les énoncés retenus : la règle d'audit en trois parts (plancher, enjeu, soupçon), pondérée par l'inverse de la probabilité (N-076, § 6.1) ; la boucle (§ 6.2) ; la table du seuil au taux d'audit, à deux régimes (§ 7) ; les quatre invariants d'audit (§ 8) ; la règle « les scores orientent l'audit sous un plancher » (§ 9).
- La boucle v2 (R-4623, `3bc8585c…`, vérifiée « conforme ») :
  - une règle (interdit général, une seule exception : le bras de flux déclaré) ;
  - treize épreuves d'admission, dont 3, 4, 6 et 7 sont jouées en prototype, et 5 en partie ;
  - l'échelle des échelons ;
  - trois étapes, dont l'étape 0 sur mondes plantés, sans dépense et déjà accordée ;
  - un couple neutre prêt pour le collisionneur.
- Les calculs de la table du seuil (note sur l'attaquant informé, blocs A à D) et ceux de la boucle (blocs A à F), tous sur suppositions d'illustration.

**Ce qui manque, et ce qui bloque.**
1. Le texte à part de l'audit tiré au hasard (accordé à GO-2026-11-21-56), qui porte les quatre invariants, gardés par le code là où un harnais les implémente.
2. La famille plantée « attaque choisie » : dommage placé où le soupçon est bas et l'enjeu haut, avec trois attentes écrites d'avance (la borne du plancher tient ; l'audit des seuls plus suspects meurt ; l'audit uniforme perd le rapport de l'enjeu maximal à l'enjeu moyen).
3. Le jeu de la règle « les scores orientent l'audit sous un plancher » avec un score trompeur planté.
4. Les treize épreuves de la boucle, en instruments.
5. **Nœuds ouverts chez Lazar, sans défaut** :
   - la règle (b′) de la boucle (D-1 de la boucle v2 ; N-076, § 13, point 3) : d'ici son mot, la boucle ne vit que sur mondes plantés ;
   - la ligne « aucun retour à l'agent » contre les trois lignes de la note « asymétries » (§ 13, point 1) : d'ici son mot, la lettre accordée s'applique ;
   - l'étape 1 de la boucle, sur devis.
6. L'étiquetage « signature » ou « excès » des familles du banc. Il touche le banc à vérité plantée, porté par l'autre session : je le laisse.

**Première pièce à écrire** : la conception, par Fable, de la règle d'audit en trois parts sur mondes plantés, avec ses épreuves. Elle comprend la famille « attaque choisie », le score trompeur planté et l'ordre d'écriture des treize épreuves de la boucle, en commençant par 3, 4 et 6 (D-2 de la boucle v2). Elle se fait dans la lettre accordée : aucun réapprentissage sur des verdicts de l'oracle, et aucune correction observable avant l'alarme.

## Réserves

1. **Plafond de trois chantiers actifs** (CLAUDE.md, allègement). Les trois chantiers actifs sont le saboteur et les sondes, le bras A et l'organisme v9. Le « go lancement » de GO-2026-11-22-40 ouvre ces trois chantiers. N-076 (§ 13, point 8) laissait à Lazar de dire sous quel chantier actif chacun se range. Je lis le mot du 22 comme une dérogation voulue ; c'est à confirmer par la mère.
2. **Fable est indisponible par l'API** : la clé indiquée n'a plus de crédit (mot de la mère, 10:55Z). Les mandats sont prêts ; aucun appel n'est parti.
3. **Recouvrement avec le banc à vérité plantée.** N-076 place des pas des chantiers 1 et 3 sur un banc (« monde planté », « banc de la course de l'adjudant »). Les mandats demandent à Fable des mondes plantés propres à chaque épreuve, sans toucher au banc de l'autre session. Il faudra peut-être les raccorder plus tard.
