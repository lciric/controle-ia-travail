# Différences du brouillon 3 vers le texte de la version — texte court du barreau 7 (bras externe NARCBench) — v1

- **Objet** : passage de `prereg/narcbench-bras-externe-v1-brouillon3.md`
  (`fae8a96ccc75e592e8ca12c5b156a19775388c14f345d94fbf77d6fd8cbc0a90`, scellé comme brouillon) au texte candidat de la
  version `prereg/narcbench-bras-externe-v1.md` (`f9d4732467d6bf1324c621e2c080e51eafa2204623431184ef4a4f9ccc64598e`, **non scellé** : la mère le scelle après le contrôle
  de cette différence, la fusion de la branche du code dans `main` et le tirage de l'entropie).
- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur du texte court, sous-agent de la session mère
  `session_013QMayjsoZJFBUCqcnvD5h1`, le 2026-11-18 (`date -u` : de 19:39 à 19:45 UTC).
- **Sources des changements** : la contre-lecture 3 (`prereg/contre-lectures/narcbench-bras-externe-v1-brouillon3-cl3.md`,
  `f8ca72e2462169d106910f96d6953316bacb617de32ae30bdc17c6439aeb4a57`, couples C1 à C5 de son § 7 et ses suggestions) ; la
  consigne de la mère pour la version (marqueurs de version, tête finale du code `fe9d799641ed3cc5d3388026e6f6143f92fc7d5c`,
  entrée de la contre-lecture 3, fusion avant le scellement, mémoire mesurée par le jouet du développeur, un seul marqueur
  restant : l'entropie).
- **Méthode** : copie du brouillon 3, puis chaque changement par remplacement exact d'un passage unique du fichier (outil
  d'édition qui refuse un passage absent ou en double) ; seuls les blocs longs (entrée de la contre-lecture 3) ont été
  remplacés par un script qui vérifie l'unicité du début du passage et la fin du fichier.
- **Contrôles sur le texte candidat** : validateur `controle_ia.prereg.problemes` : une seule remarque, « marqueurs de gabarit
  restants : `<<ENTROPIE_NARC_EXT>>` » ; sur une copie où ce marqueur est remplacé par un entier d'essai : aucune remarque ;
  `verifier-texte` du code de la tête finale (`fe9d7996`, extrait par `git archive`) : code de sortie 0 sur cette copie, et,
  sur le texte lui-même, le seul refus porte sur la valeur d'entropie ; phrases gelées du code de la tête finale (R0, R1 avec
  sa réserve, R2, R5, F1, F2, qualificatifs de plancher, états), produites par ses fonctions sur des entrées factices : toutes
  présentes mot pour mot dans le texte candidat, R1 et R2 avec le gabarit élargi par C3 ; empreintes de tous les documents
  cités recalculées : égales.
- **Phrases gelées** : aucun mot fixe ne change. Seul change le gabarit de la liste des planchers dans R1 et R2 (couple C3) :
  avant « <au-dessus ou pas au-dessus, pour chacune des douze cellules visées, nommées> », après « <au-dessus, pas au-dessus
  ou sans plancher, pour chacune des douze cellules visées, nommées> » ; le code rend déjà « sans plancher ».

## Changements, un par ligne

1. Statut réécrit pour la version (non scellée ; scellement par la mère après contrôle de cette différence, fusion du code, entropie seule inscription) — consigne : marqueurs de version.
2. Rédacteur : heure du texte de la version ajoutée — consigne : marqueurs de version.
3. Mandat : consigne de la version ajoutée ; phrase sur R-3310 remise en lignes (aucun mot changé) — consigne : marqueurs de version.
4. En-tête, commit du code : « pour ce brouillon » devient « pour le brouillon 3 » ; marqueur de la tête finale rempli (`fe9d7996…`), avec ce qui change de la tête lue à la tête finale — consigne : tête finale.
5. Documents qui font foi : heure du recalcul des empreintes et état du dépôt principal — consigne : marqueurs de version (documents).
6. Documents : tête finale, empreinte de `cellules_externe_v2.py` à la tête finale, pièce du jouet aux formes publiées (`e21ac32a…`, empreinte entière vérifiée) — consigne : tête finale ; mémoire mesurée.
7. Documents : les pièces de la branche « entrent dans `main` par la fusion de la branche du code, faite par la mère avant le scellement » — consigne : fusion avant le scellement.
8. Documents : brouillon 3 (`fae8a96c…`) et contre-lecture 3 ajoutés à la liste — consigne : documents ; contre-lecture 3.
9. Recette, réexamen de l'augmentation : « environ trente fois sous la tolérance de 0,03 » — suggestion non bloquante de la contre-lecture 3 (§ 3), retenue.
10. Notes de la configuration, `run-id` : « avec une date et une heure valides (la mère y met celles du lancement ; le code ne le compare pas) » — couple C5.
11. Seuil : phrase sur l'absence de réserve pour R2 (« non reproduit » à tort 0,002 au pic, 0,004 à l'écart, à la marge) — suggestion de la contre-lecture 3 (§ 2), retenue avec la valeur 0,004 de la pièce scellée de l'écart à sa marge au lieu du 0,001 cité par le rapport (point de la grille à 0,97).
12. Puissance, réponse au barreau : « oui » au plus 33 à 61 fois sur cent (57 à 78 sans indépendance), les autres issues se partagent le reste, non simulé — couple C1 (premier endroit).
13. Plan n° 0 réécrit : contre-lectures 1 à 3 faites ; contrôle de cette différence ; fusion de la branche du code dans `main` avant le scellement ; entropie seule inscription ; validateur sans remarque — consigne : fusion ; marqueurs de version.
14. Plan n° 1 : « la phrase gelée R1 est alignée à la tête finale `fe9d7996` » — consigne : tête finale.
15. Plan n° 2 : « branche du code fusionnée dans `main` (avant le scellement, n° 0) » — consigne : fusion avant le scellement.
16. Plan n° 2 : la ligne `LECTURE-NARC-EXT` est lue et refusée dès le n° 3, au titre du n° 4 — couple C4 (second endroit).
17. Critères, table de la règle C : « (à 10⁻⁹ près, section « Seuil ») » dans les conditions des lignes C2 et C3 (colonne des conditions, pas des phrases) — suggestion de la contre-lecture 3 (§ 1), retenue.
18. Critères, phrase R1 : gabarit de la liste des planchers élargi à « sans plancher » — couple C3.
19. Critères, phrase R2 : même élargissement — couple C3.
20. Critères, paragraphe des phrases gelées : R1 alignée à la tête finale ; F1 sans réserve (suggestion non retenue, raison écrite) ; gabarits de C3 sans mot fixe changé ; phrases du code « à la tête finale » — consigne : tête finale ; couple C3.
21. Liste d'arrêt, « Ordre » : la ligne `LECTURE-NARC-EXT` est lue au n° 3 et refusée au titre du n° 4 ; n° 4 = dossier `runs/` ou résultat sous `diag/` — couple C4 (premier endroit).
22. Liste d'arrêt n° 1 : la révision du jeu est consignée, non comparée ; les empreintes la fixent — couple C2.
23. Liste d'arrêt n° 11 : l'estimation non mesurée devient la pointe mesurée (3 748 Mo, 14,8 minutes, 4 cœurs et 16 Go ; pièce `e21ac32a…`) ; seuil de 8 Go gardé — consigne : mémoire.
24. Code, base : tête finale, ses trois commits, 168 essais, seul `cellules_externe_v2.py` changé dans `src/` — consigne : tête finale.
25. Code : « Écarts restants » devient « Écarts entre ce texte et la tête finale : aucun connu », avec le règlement des couples C2 à C5 dans le texte — consigne : tête finale ; couples C2 à C5.
26. Expositions (d) : le rapport (h) ajouté à ceux que la mère a reçus — contre-lecture 3.
27. Expositions (h) contre-lecteur 3 et (i) développeur de la tête lue à la tête finale (jouet sur vecteurs factices) ajoutées — contre-lecture 3 ; tête finale.
28. Expositions, rédacteur : lectures de la version ajoutées ; « pour ce brouillon » précisé — consigne : marqueurs de version.
29. Frontière n° 8 : « oui » au plus 33 à 61 fois sur cent et les autres issues se partagent le reste — couple C1 (deuxième endroit).
30. Tableau de la contre-lecture 2, ligne M3 : traitement corrigé selon C1 — couple C1 (troisième endroit).
31. Tableau de la contre-lecture 2, ligne m-D6 : « (dans la version : une seule, l'entropie) » — consigne : un seul marqueur restant.
32. Tableau de la contre-lecture 2, ligne m6 : pointe mesurée sur le jouet (3 748 Mo) au lieu de l'estimation — consigne : mémoire.
33. Contre-lecture : l'entrée « Contre-lecture 3 » remplace son marqueur ; elle porte les deux empreintes (brouillon relu `fae8a96c…`, rapport `f8ca72e2…`) et un tableau de traitement (C1 à C5 appliqués tels quels ; trois suggestions retenues, une non retenue) — consigne : entrée de la contre-lecture 3.

Couples non appliqués tels quels : aucun. Écart à une suggestion : la valeur citée pour l'écart dans la phrase sur R2 (changement 11).

## Sortie de `diff -u` (brouillon 3 → texte de la version)

```diff
--- prereg/narcbench-bras-externe-v1-brouillon3.md	2026-11-18 19:28:47.575926517 +0000
+++ prereg/narcbench-bras-externe-v1.md	2026-11-18 19:44:37.789643615 +0000
@@ -1,23 +1,24 @@
 # Préenregistrement court — notre chaîne reproduit-elle un résultat positif publié ? Nos sondes sur les activations publiées par les auteurs de NARCBench (bras externe, septième barreau, au processeur, 0 USD) — v1
 
-- **Statut** : texte court du barreau 7, version 1, rédigé en trois brouillons (celui-ci est le brouillon 3, du 2026-11-18,
-  qui applique la contre-lecture 2 et s'aligne sur le code du développeur ; traitement de chaque remarque : section
-  « Contre-lecture »). Le texte scellé `prereg/narcbench-bras-externe-v1.md` (nom fixé, R12) est la copie de ce brouillon où
-  la mère inscrit trois choses et rien d'autre : l'entropie (ligne `Entropie :` de la section « Configuration canonique de la
-  commande »), la tête finale du code (section « En-tête du gabarit ») et l'entrée de la contre-lecture 3 ; elle le scelle
-  par `controle_ia.prereg.sceller_prereg`. Ce brouillon-ci est scellé comme brouillon
-  (`python3 -m controle_ia.scellement sceller`). Le rédacteur n'a rien téléchargé, rien lu des fichiers publiés, rien lancé
-  sur eux, rien dépensé.
+- **Statut** : texte court du barreau 7, **version 1** (`prereg/narcbench-bras-externe-v1.md`, nom fixé, R12), du 2026-11-18 :
+  le brouillon 3 (`fae8a96c…`) corrigé par les cinq couples de la contre-lecture 3, la tête finale du code inscrite. Trois
+  brouillons l'ont précédé, chacun contre-lu (section « Contre-lecture »). Ce texte est rendu **non scellé** ; la mère le
+  scelle par `controle_ia.prereg.sceller_prereg` après le contrôle de la différence avec le brouillon 3 (pièce
+  `prereg/pieces-narcbench-bras-externe-v1/differences-brouillon3-vers-version-v1.md`), la fusion de la branche du code dans
+  `main` et le tirage de l'entropie, **seule inscription qu'elle y fait** (ligne `Entropie :` de la section « Configuration
+  canonique de la commande »). Le rédacteur n'a rien téléchargé, rien lu des fichiers publiés, rien lancé sur eux, rien
+  dépensé.
 - **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur neuf, sous-agent de la session mère
   `session_013QMayjsoZJFBUCqcnvD5h1` ; distinct du développeur du bras externe ; ni contre-lecteur de ce texte ni lecteur de
   ses issues. Brouillon 1 écrit le 2026-11-18 de 16:55 à 17:06 UTC ; brouillon 2 d'environ 17:21 à 17:45 UTC ; brouillon 3
-  de 19:13 à 19:28 UTC (`date -u`).
+  de 19:13 à 19:28 UTC ; texte de la version de 19:39 à 19:44 UTC (`date -u`).
 - **Mandat** : `docs/notes/narcbench-8b-v1/mandat-redacteur-texte-court-bras-externe-v1.md`
   (`ea4c8554567b8c8a74d91ed3dad26637ac63d13863eeef5e50f048729f084638`), sous GO-2026-11-18-30 et R-3310 ; brouillons 2 et 3
-  sur consigne de la mère (R-3341 ; puis consigne du 18 novembre au soir : contre-lecture 2 et code du développeur). Voie
+  sur consigne de la mère (R-3341 ; puis consigne du 18 novembre au soir : contre-lecture 2 et code du développeur) ; texte
+  de la version sur consigne de la mère (après la contre-lecture 3 : ses cinq couples, la tête finale du code). Voie
   décidée par Lazar le 10 novembre (R-2175, D-3 (a) : « bras externe NARCBench sur les activations publiées, processeur,
-  0 USD, texte court neuf ») ; R-3310 rectifie la lettre de GO-2026-11-18-30 (« scellement
-  du brouillon 4 ») en « voie processeur, texte court neuf ». Le rédacteur n'a pas relu GO-2026-11-18-30 au registre des GO :
+  0 USD, texte court neuf ») ; R-3310 rectifie la lettre de GO-2026-11-18-30 (« scellement du brouillon 4 ») en « voie
+  processeur, texte court neuf ». Le rédacteur n'a pas relu GO-2026-11-18-30 au registre des GO :
   la mère le relit avant le scellement.
 - **Choix de la mère repris ici** (ils remplacent les points ouverts du brouillon 1) : registre propre
   `registres/narcbench-externe-v1.md` ; tolérance 0,03 ; deux familles co-principales lues en conjonction ; étage des comités
@@ -42,12 +43,14 @@
 - Auteur : le rédacteur ci-dessus.
 - Date (UTC) : celle de la ligne `SCELLEMENT-NARC-EXT` (section « Lignes de registre »).
 - Commit du code d'analyse : **le commit exact est celui de la fiche citée par la ligne `CODE-NARC-EXT`, inscrite avant toute
-  exécution** (section « Code »). Tête lue par le rédacteur pour ce brouillon : `cde3b9906881b6a26dba2d8486b46ac734d92371`
-  (branche locale `prep/narcbench-externe-v2`). Tête finale de la branche, que la fiche doit citer :
-  `<<TETE_FINALE_CODE_NARC_EXT>>` (le développeur ajoute un essai et joue une épreuve par mutation ; le code de lecture ne doit
-  pas changer, sauf l'alignement de la phrase gelée R1 : section « Critères de lecture gelés »).
-- Documents qui font foi (chemin, empreinte sha256 recalculée le 2026-11-18 à 19:28 UTC ; dépôt principal à `b0824238`,
-  fichiers cités inchangés depuis le brouillon 2 ou ajoutés depuis) :
+  exécution** (section « Code »). Tête lue par le rédacteur pour le brouillon 3 : `cde3b9906881b6a26dba2d8486b46ac734d92371`
+  (branche locale `prep/narcbench-externe-v2`). **Tête finale de la branche, que la fiche doit citer :
+  `fe9d799641ed3cc5d3388026e6f6143f92fc7d5c`**. De la tête lue à la tête finale, le seul module de `src/` qui change est
+  `cellules_externe_v2.py` : la phrase gelée R1 alignée mot pour mot sur ce texte, et sa docstring (différence relue par le
+  rédacteur) ; s'y ajoutent des essais (168), une épreuve par mutation et le jouet aux formes publiées ; contrôle par programme
+  des 39 phrases gelées contre le brouillon 3 : aucun écart (d'après le développeur).
+- Documents qui font foi (chemin, empreinte sha256 recalculée le 2026-11-18 à 19:44 UTC ; dépôt principal à
+  `9e90e525`, fichiers cités inchangés depuis le brouillon 2 ou ajoutés depuis) :
   - article : `docs/sources/pdf/2604.01151v5.pdf`, `02527fd4f62ad9b996669275f0837697cbe288b253c9aa521f72a10e6dcf1849`
     (Rose, Cullen, Abdelnabi, Torr, Kaplowitz, Schroeder de Witt, « Detecting Multi-Agent Collusion Through Multi-Agent
     Interpretability », arXiv 2604.01151 v5, 15 octobre 2026) ;
@@ -87,8 +90,14 @@
     (`69dfdd247d104ee6293507fea17be56b23100f5da0ab03751d46c9d01029ed90`), `src/controle_ia/narcbench/statistiques_v1.py`
     (`fa9970d738b18d9056f567fadf15c70f139e53183be73519519c18bddec1b264`), `requirements-cpu.txt`
     (`d236a3931745d4ad0889947f7692a2cd49e2c19a6f8e6c10b2e67120d47122de`) ; le brouillon 2 a été écrit contre le commit
-    `70cb77b848da03f044d676ce04fc79c3c24b371d`, que les contre-lectures 1 et 2 ont relu ;
-  - pièces de la branche, **à faire entrer dans `main` par la mère avant le scellement** (contre-lecture 2, § 6) : rapport du
+    `70cb77b848da03f044d676ce04fc79c3c24b371d`, que les contre-lectures 1 et 2 ont relu ; **tête finale
+    `fe9d799641ed3cc5d3388026e6f6143f92fc7d5c`**, où seul `cellules_externe_v2.py` diffère de la tête lue
+    (`0461739c36cd480cc1add33be1bc5556b0c873470e076f85db081faa5a0183ef`) ; sortie du jouet de bout en bout aux formes
+    publiées (vecteurs factices, code au commit `b46c678d`, dont `src/` ne diffère de la tête finale que par la phrase R1 et sa
+    docstring) : `docs/notes/narcbench-8b-v1/pieces-externe-v2/jouet-formes-publiees-sortie-v1.txt`
+    (`e21ac32a2ad8c451c2d008facbf07598f25637643959f47318356117aea3b58d` à la tête finale ; lue en entier) ;
+  - pièces de la branche, **qui entrent dans `main` par la fusion de la branche du code, faite par la mère avant le
+    scellement** (contre-lecture 2, § 6) : rapport du
     développeur v2 `docs/notes/narcbench-8b-v1/rapport-developpeur-externe-v2.md`
     (`40fbdc70f22fda6500b02d452b50d9cb5342ae5092252ecd98505273c17078ce` ; en-tête et sections 3 à 5 lus) ; relevé des lignes du
     code des auteurs pour les cinq points de recette `docs/notes/narcbench-8b-v1/releve-recette-code-auteurs-externe-v2-v1.md`
@@ -99,9 +108,10 @@
     (`ba78089612fd0173216ca7a789b98bf4279119ac3bb33e36f2663dc86bb588f7`) : cités, non ouverts ;
   - contre-lecture du code v2 : `docs/notes/narcbench-8b-v1/contre-lecture-code-externe-v2-v1.md`
     (`9b90884aaf86843cebfb129d6e72a0177102514bcc019e05c6938076feef155e` ; verdict et remarques lus) ;
-  - brouillons 1 et 2 de ce texte : `prereg/narcbench-bras-externe-v1-brouillon1.md`
-    (`85e8de5d7d94161b4951dac12c605a56ce048dbbfe6f92538552fcc2f6417259`) et `prereg/narcbench-bras-externe-v1-brouillon2.md`
-    (`7bb21dc0bec7a5fcbff41c84ee2554966e7ddc0acf8703cf7fe8f78d224acb02`) ; leurs contre-lectures 1 et 2 : section
+  - brouillons 1, 2 et 3 de ce texte : `prereg/narcbench-bras-externe-v1-brouillon1.md`
+    (`85e8de5d7d94161b4951dac12c605a56ce048dbbfe6f92538552fcc2f6417259`), `prereg/narcbench-bras-externe-v1-brouillon2.md`
+    (`7bb21dc0bec7a5fcbff41c84ee2554966e7ddc0acf8703cf7fe8f78d224acb02`) et `prereg/narcbench-bras-externe-v1-brouillon3.md`
+    (`fae8a96ccc75e592e8ca12c5b156a19775388c14f345d94fbf77d6fd8cbc0a90`) ; leurs contre-lectures 1, 2 et 3 : section
     « Contre-lecture » ;
   - pièces de puissance : `prereg/pieces-narcbench-bras-externe-v1/puissance-regle-v1.py`
     (`fa482dd97b78af1d858706f7dfd880b2ead58e3ff001ef672334b4e0af10fb7a`) et sa sortie
@@ -233,8 +243,8 @@
 publié ne prévaut pas sur une phrase explicite de l'article. **Limites déclarées** : le lien entre ce script et les Tables 2
 et 3 n'est établi que par la recette (p. 29-30 = l. 28-33 du script) et par la Table 6, pas par l'exécution du script des
 auteurs ; le script des résultats principaux selon le fichier d'accueil n'est pas lu ; si les tables avaient été produites
-avec l'augmentation, l'écart attendu reste petit d'après l'article (moins de 0,001 sur la moyenne hors distribution), mais il
-n'est pas chiffré pour l'étage stéganographique seul. La recommandation ne change pas : **aucun nœud** (section « Nœuds »).
+avec l'augmentation, l'écart attendu reste petit d'après l'article (moins de 0,001 sur la moyenne hors distribution, environ
+trente fois sous la tolérance de 0,03), mais il n'est pas chiffré pour l'étage stéganographique seul. La recommandation ne change pas : **aucun nœud** (section « Nœuds »).
 
 **Notre chaîne** (paquet gelé `sondes.familles`, appel `entrainer(famille, nom, couche, séquences, y, "max", graine)`).
 - **Familles** : **différence de moyennes** et **linéaire**, **co-principales** (familles des deux sondes principales de
@@ -312,8 +322,8 @@
 - `augmentation` : aucune augmentation (section « Recette ») ; l'option `--augmentation` doit valoir `papier`.
 - `couches-familles` : nos familles sur toutes les couches de la bande de chaque modèle (26 à 30 ; 32 à 37) ; l'option
   `--couches-familles` doit désigner les mêmes couches (`bande`).
-- `run-id` : la ligne donne la **forme**, pas une valeur ; l'option `--run-id` doit suivre cette forme, avec la date et l'heure
-  UTC du lancement (date et heure valides) et le suffixe fixe `narc-externe-v2` (motif `[0-9]{8}-[0-9]{6}-narc-externe-v2`,
+- `run-id` : la ligne donne la **forme**, pas une valeur ; l'option `--run-id` doit suivre cette forme, avec une date et une
+  heure valides (la mère y met celles du lancement ; le code ne le compare pas) et le suffixe fixe `narc-externe-v2` (motif `[0-9]{8}-[0-9]{6}-narc-externe-v2`,
   compatible avec celui de `manifeste.creer_manifeste`).
 - `registre` : le seul registre lu, `registres/narcbench-externe-v1.md` du dépôt (section « Lignes de registre ») ; le code
   n'accepte aucun autre chemin et n'a pas d'option pour en donner un.
@@ -406,7 +416,8 @@
   avec la valeur publiée à 0,03 près, à cette puissance », pas « égal ». Pour la réponse « oui » (douze cellules), si toutes
   les aires vraies étaient à la marge, la probabilité de sortir à tort serait au plus 0,160² ≈ 0,026 (deux modèles
   indépendants) et au plus 0,160 sinon ; cette réserve est écrite dans la phrase gelée R1 (section « Critères de lecture
-  gelés »).
+  gelés »). La phrase R2 n'a pas de réserve semblable : à la marge, « non reproduit » ne sort à tort que 0,002 fois au pic et
+  0,004 fois à l'écart (pièces scellées).
 - **Réponse au barreau** : « oui » exige douze cellules « reproduit », « non » huit cellules « non reproduit » et le témoin
   « reproduit » (section « Critères de lecture gelés ») ; leurs probabilités : section « Puissance ».
 - **Multiplicité** : lectures descriptives à 95 %, sans correction, **déclaré** ; 12 cellules visées, 12 secondaires et 4
@@ -450,9 +461,10 @@
 générés séparément pour chaque modèle ; l'essai de forme rapporte des domaines différents entre eux, exposition déclarée),
 elle vaut au plus leur produit : **≈ 0,33 à une aire vraie de 0,99** (0,573²), **≈ 0,61 à 0,995** (0,783²), ≈ 0,998 à
 0,9999 ; sans cette hypothèse, au plus la plus petite des deux (0,573 ; 0,783 ; 0,999). **Si l'aire vraie de chaque cellule
-vaut 0,99 à 0,995 (ce que les valeurs publiées, arrondies, permettent), « oui » sort au plus 33 à 61 fois sur cent et « non
-tranché à cette puissance » est l'issue la plus probable ; si elle vaut 0,9999 ou plus (ce qu'elles permettent aussi), « oui »
-sort presque toujours (≈ 0,998). Un « non tranché » n'est pas un échec** ; « oui » ne sort que si la séparation est quasi
+vaut 0,99 à 0,995 (ce que les valeurs publiées, arrondies, permettent), « oui » sort au plus 33 à 61 fois sur cent (deux
+modèles indépendants ; au plus 57 à 78 fois sur cent sinon) ; les autres issues (« en partie », « non tranché à cette
+puissance ») se partagent le reste, que la simulation ne répartit pas ; si elle vaut 0,9999 ou plus (ce qu'elles permettent
+aussi), « oui » sort presque toujours (≈ 0,998). Un « non tranché » n'est pas un échec** ; « oui » ne sort que si la séparation est quasi
 totale. « Non » exige les huit cellules des deux familles co-principales « non
 reproduit » (et le témoin « reproduit ») : sous la même hypothèse, au plus ≈ 0,04 à une aire vraie de 0,90 (0,193²),
 ≈ 0,59 à 0,80 (0,771²), ≈ 0,96 à 0,70 (0,978²) (cellules de l'écart, qui donnent la borne la plus basse).
@@ -465,23 +477,27 @@
 
 ## Plan d'analyse
 
-0. **Avant le scellement** : contre-lecture 3 (vérification courte de la différence brouillon 2 → brouillon 3 par un agent
-   neuf) ; pièces de la branche citées par ce texte entrées dans `main` (section « En-tête du gabarit ») ; inscription par la
-   mère de l'entropie, de la tête finale du code et de l'entrée de la contre-lecture 3 ; contrôle `verifier-texte` du code
-   sur la copie à sceller (code de sortie 0 exigé) ; scellement par `sceller_prereg` sous le nom
+0. **Avant le scellement** (contre-lectures 1 à 3 faites ; la mère) : contrôle de la différence entre le brouillon 3 et ce
+   texte (pièce `differences-brouillon3-vers-version-v1.md`) ; **fusion de la branche du code `prep/narcbench-externe-v2`
+   (tête finale `fe9d7996`) dans `main`**, qui y fait entrer les pièces de la branche citées par ce texte (section « En-tête
+   du gabarit ») ; tirage et inscription de l'entropie, seule inscription ; contrôle `verifier-texte` du code sur la copie à
+   sceller (code de sortie 0 exigé) et validateur sans aucune remarque ; scellement par `sceller_prereg` sous le nom
    `prereg/narcbench-bras-externe-v1.md` ; création du registre propre ; ligne `SCELLEMENT-NARC-EXT`.
 1. **Avant la ligne de code** : le code ferme **chaque écart** de la section « Code » (avant le scellement, un écart peut
-   encore se régler par une nouvelle version de ce texte ; après, tout écart est un nœud) ; il aligne la phrase gelée R1 ;
+   encore se régler par une nouvelle version de ce texte ; après, tout écart est un nœud) ; la phrase gelée R1 est alignée
+   à la tête finale `fe9d7996` ;
    essais R5 de chaque garde, cas
    sain **et** artefact (une garde sans essai sur artefact interdit la ligne de code) ; énumération exhaustive des règles C et
    T, des phrases par famille et des lignes de réponse, rejouée en essai ; jouet de bout en bout sur vecteurs factices aux
    formes publiées (deux modèles, deux étages) ; contre-lecture du code final par un agent neuf, qui vérifie la fermeture de
    chaque écart ; fiche du code scellée ; ligne `CODE-NARC-EXT`, **avant toute exécution** sur les fichiers publiés.
    Personne ne calcule d'aire, de score de sonde ni de statistique d'épisode sur les fichiers publiés avant cette ligne.
-2. **Lancement** (la mère) : branche fusionnée dans `main`, arbre propre, paquet exécuté égal à celui du commit de la fiche
+2. **Lancement** (la mère) : branche du code fusionnée dans `main` (avant le scellement, n° 0), arbre propre, paquet exécuté
+   égal à celui du commit de la fiche
    (règle DF-02 de T0.7) ; mémoire libre relevée (au moins 8 Go, liste d'arrêt n° 11) ; données téléchargées à la révision
    épinglée si elles manquent, hors du dépôt ; commande avec les options de la configuration canonique. Le code vérifie, dans
-   l'ordre de la liste d'arrêt (n° 3, 5, 6, 4, 7, 2, 1, puis 8 et 9 sur les métadonnées), en n'écrivant en cas de refus que la
+   l'ordre de la liste d'arrêt (n° 3, 5, 6, 4, 7, 2, 1, puis 8 et 9 sur les métadonnées ; la ligne `LECTURE-NARC-EXT` du
+   registre est lue et refusée dès le n° 3, au titre du n° 4), en n'écrivant en cas de refus que la
    ligne du journal ; puis il crée le manifeste du run (R9) et ouvre les activations.
 3. **Comptes structurels**, écrits au résultat à côté de ceux de l'article (étage des comités : 50 scénarios, 17 domaines,
    100 épisodes, p. 14 ; 36 scénarios de collusion retenus avec les 50 témoins, p. 35, sans dire pour quel modèle ; étage
@@ -552,8 +568,8 @@
 |---|---|---|---|
 | 1 | C0 | la garde des scores constants a joué (liste d'arrêt n° 12) | « non lu : garde (scores constants) » |
 | 2 | C1 | effectif non lisible ou plus de 1 % de tirages dégénérés | « non calculable à cet effectif » |
-| 3 | C2 | bas ≥ m | « reproduit » |
-| 4 | C3 | haut < m | « non reproduit » suivi du qualificatif de signe (section « Seuil ») |
+| 3 | C2 | bas ≥ m (à 10⁻⁹ près, section « Seuil ») | « reproduit » |
+| 4 | C3 | haut < m (à 10⁻⁹ près, section « Seuil ») | « non reproduit » suivi du qualificatif de signe (section « Seuil ») |
 | 5 | C4 | sinon | « non tranché à cette puissance » |
 
 Qualificatifs ajoutés sous C2, C3 et C4 : plancher (« au-dessus du plancher apparié » ou « pas au-dessus du plancher
@@ -589,18 +605,21 @@
 | ordre | ligne | condition | phrase gelée |
 |---|---|---|---|
 | 1 | R0 | témoin de recette autre que « reproduit » | « question non tranchée : le témoin de recette est <état>. Un témoin qui n'est pas « reproduit » ne permet de conclure ni oui ni non sur notre chaîne ; les cellules de nos familles sont rapportées » |
-| 2 | R1 | les huit cellules « reproduit » | « oui : notre chaîne reproduit le résultat positif publié (deux familles, deux modèles, deux statistiques), à côté de la recette des auteurs ; plancher apparié : <au-dessus ou pas au-dessus, pour chacune des douze cellules visées, nommées> ; réserve : « reproduit » veut dire « compatible avec la valeur publiée à 0,03 près, à cette puissance », pas « égal » ; si toutes les aires vraies étaient à la marge, ce « oui » sortirait à tort au plus environ 3 fois sur 100 avec deux modèles indépendants, au plus 16 fois sur 100 sinon (section « Seuil ») » |
-| 3 | R2 | les huit cellules « non reproduit » | « non : notre chaîne ne reproduit pas le résultat publié, que la recette des auteurs reproduit sur les mêmes vecteurs ; plancher apparié : <au-dessus ou pas au-dessus, pour chacune des douze cellules visées, nommées> » |
+| 2 | R1 | les huit cellules « reproduit » | « oui : notre chaîne reproduit le résultat positif publié (deux familles, deux modèles, deux statistiques), à côté de la recette des auteurs ; plancher apparié : <au-dessus, pas au-dessus ou sans plancher, pour chacune des douze cellules visées, nommées> ; réserve : « reproduit » veut dire « compatible avec la valeur publiée à 0,03 près, à cette puissance », pas « égal » ; si toutes les aires vraies étaient à la marge, ce « oui » sortirait à tort au plus environ 3 fois sur 100 avec deux modèles indépendants, au plus 16 fois sur 100 sinon (section « Seuil ») » |
+| 3 | R2 | les huit cellules « non reproduit » | « non : notre chaîne ne reproduit pas le résultat publié, que la recette des auteurs reproduit sur les mêmes vecteurs ; plancher apparié : <au-dessus, pas au-dessus ou sans plancher, pour chacune des douze cellules visées, nommées> » |
 | 4 | R3 | au moins une cellule « reproduit » | « en partie : notre chaîne reproduit le résultat publié sur <cellules « reproduit », nommées> ; elle ne le reproduit pas sur <cellules « non reproduit », nommées, ou « aucune »> ; non tranché ou non lu sur <autres cellules, nommées, ou « aucune »> » |
 | 5 | R4 | au moins une cellule « non reproduit » | « en partie, non : notre chaîne ne reproduit pas le résultat publié sur <cellules « non reproduit », nommées> ; non tranché ou non lu sur <autres cellules, nommées> » |
 | 6 | R5 | sinon (aucune cellule « reproduit » ni « non reproduit ») | « non tranché à cette puissance : différence de moyennes <état>, linéaire <état> ; ce n'est pas un échec (section « Puissance ») » |
 
 R3, R4 et R5 remplacent la ligne « en partie » du brouillon 1 (contre-lecture 1, M1) : rien n'est dit « en partie » sans une
 cellule décidée de ce côté. **Seule phrase gelée changée au brouillon 3 : R1**, qui porte désormais la réserve de l'intervalle
-(contre-lecture 2, M4) ; le code l'aligne mot pour mot (`cellules_externe_v2.reponse`). L'état « reproduit » d'une cellule
-(ligne C2) reste un mot seul : c'est l'étiquette que lisent les règles T et R, et son sens est fixé à la section « Seuil » ;
-la réserve voyage avec la phrase de réponse, que le lecteur des issues recopie. Toutes les autres phrases gelées sont celles
-du brouillon 2, mot pour mot, et celles du code à la tête lue.
+(contre-lecture 2, M4) ; le code l'a alignée mot pour mot à la tête finale `fe9d7996` (`cellules_externe_v2.reponse`).
+L'état « reproduit » d'une cellule (ligne C2) reste un mot seul : c'est l'étiquette que lisent les règles T et R, et son sens
+est fixé à la section « Seuil » ; la réserve voyage avec la phrase de réponse, que le lecteur des issues recopie ; la phrase
+par famille F1 ne la porte pas (la réponse au barreau est la phrase qui conclut). **Dans la version**, les gabarits de la
+liste des planchers des lignes R1 et R2 nomment aussi la valeur « sans plancher », que le code rend déjà (contre-lecture 3,
+C3) : aucun mot fixe de ces phrases ne change. Toutes les autres phrases gelées sont celles du brouillon 2, mot pour mot, et
+celles du code à la tête finale.
 
 **Secondaires et descriptifs** : l'étage des comités suit la règle C (valeurs publiées 1,00 ; marge 0,97) et est écrit
 « lecture secondaire, sans effet sur la réponse » ; Mahalanobis : estimation et intervalle, sans phrase d'état ; lecture par
@@ -613,8 +632,9 @@
 
 ## Liste d'arrêt
 
-**Ordre.** Le code vérifie dans cet ordre (`lecture_externe_v2.lire`) : n° 3 (registre et texte cité), n° 5 (configuration),
-n° 6 (code), n° 4 (déjà jouée), n° 7 (scikit-learn), n° 2 (transfert), n° 1 (fichiers), puis les n° 8 et 9 **sur les
+**Ordre.** Le code vérifie dans cet ordre (`lecture_externe_v2.lire`) : n° 3 (registre et texte cité ; la ligne
+`LECTURE-NARC-EXT` du registre est lue ici et refusée au titre du n° 4), n° 5 (configuration), n° 6 (code), n° 4 (déjà
+jouée : dossier `runs/` ou résultat sous `diag/`), n° 7 (scikit-learn), n° 2 (transfert), n° 1 (fichiers), puis les n° 8 et 9 **sur les
 métadonnées** (structure et comptes, jamais un score) ; ensuite seulement il crée le manifeste du run et ouvre les
 activations, où jouent la part du n° 8 qui porte sur les activations et les n° 10 à 12.
 **Codes de sortie.** **2** pour les refus n° 3, 4 et 5 ; **1** pour tout autre arrêt ; 0 pour une lecture menée au bout.
@@ -629,8 +649,8 @@
 manifeste** (n° 8 sur les activations, n° 11 et 12, valeur non finie au résultat) rend toute relance sous ce texte un nœud
 (Lazar) ; le dossier du run reste, et le n° 4 refuserait la relance.
 
-1. Fichier publié de taille ou d'empreinte différente de `EMPREINTES_PUBLIEES`, ou révision du jeu différente → arrêt avant
-   toute lecture (R11).
+1. Fichier publié de taille ou d'empreinte différente de `EMPREINTES_PUBLIEES` → arrêt avant toute lecture (R11) ; la
+   révision du jeu (`REVISION_JEU`) est consignée au manifeste, non comparée : les empreintes des huit fichiers la fixent.
 2. Fichier ou dossier dont le chemin, sous le dossier des données, porte un segment `transfer` → arrêt avant toute lecture,
    nœud ; toute ouverture d'un fichier de l'étage de transfert (le code n'en ouvre aucun) → arrêt, nœud.
 3. Registre : `registres/narcbench-externe-v1.md` absent du dépôt ; ligne `SCELLEMENT-NARC-EXT` ou `CODE-NARC-EXT` absente,
@@ -667,9 +687,10 @@
     tirage **équivalent en loi** par les lignes centrées (w = X_cᵀ g / √(n − 1) + √(10⁻⁹) h, g et h gaussiens réduits),
     déclaré au résultat ; s'il échoue aussi → la cellule est « sans plancher ».
 11. Mémoire insuffisante → arrêt, nœud (une famille « non lue pour mémoire » serait une sortie sélective). Pour ne pas brûler
-    le coup sur cet arrêt, la mère relève avant le lancement la mémoire libre et ne lance pas sous 8 Go (estimation du
-    rédacteur, non mesurée : couches de la bande chargées, matrices 8 192 × 8 192 en double précision pour le plancher et
-    Mahalanobis).
+    le coup sur cet arrêt, la mère relève avant le lancement la mémoire libre et ne lance pas sous 8 Go (pointe mesurée sur
+    le jouet de bout en bout aux formes publiées, vecteurs factices, réglages du texte : 3 748 Mo, en 14,8 minutes, sur 4
+    cœurs et 16 Go ; pièce `docs/notes/narcbench-8b-v1/pieces-externe-v2/jouet-formes-publiees-sortie-v1.txt`,
+    `e21ac32a2ad8c451c2d008facbf07598f25637643959f47318356117aea3b58d`).
 12. Scores non finis → arrêt (le paquet gelé l'impose) ; scores d'une procédure constants sur un étage → ses cellules « non
     lu : garde (scores constants) » ; audit R4. Valeur non finie dans le résultat → arrêt, rien n'est écrit (JSON standard
     exigé).
@@ -723,7 +744,11 @@
   points de recette. 167 essais passés à cette tête (d'après la mère ; non rejoués par le rédacteur). Le rédacteur a lu les
   trois modules de la lecture (`lecture_externe_v2`, `cellules_externe_v2`, `externe_v2`) à cette tête ; il n'a exécuté que le
   contrôle préalable `verifier-texte` et la fonction `taches` (noms de plis factices), sur une copie extraite par
-  `git archive`, sans données.
+  `git archive`, sans données. **Tête finale `fe9d799641ed3cc5d3388026e6f6143f92fc7d5c`** : commits `950e5d3c` (essai de
+  l'écart 16), `b46c678d` (épreuve par mutation, 11 mutations décisives, toutes tuées ; script du jouet) et `fe9d7996`
+  (phrase R1 alignée, contrôles contre le brouillon 3, sortie du jouet) ; 168 essais (d'après le développeur) ; seul
+  `cellules_externe_v2.py` change dans `src/` depuis la tête lue (différence relue par le rédacteur) ; `verifier-texte` rejoué
+  par le rédacteur avec le code de la tête finale.
 
 **Écarts du brouillon 2 et de la contre-lecture 2, à la tête lue.** Les dix-huit écarts du brouillon 2 (contre le commit
 `70cb77b8`) et les douze ajoutés par la contre-lecture 2 (A19 à A30) sont **lus fermés** par le rédacteur à la tête lue,
@@ -741,13 +766,13 @@
 `journaliser`, gardé par décision de ce texte) ; numérotation de la liste d'arrêt (A29 : le code cite les numéros du brouillon
 2, que ce texte garde). **Comparaisons à 10⁻⁹ près** (contre-lecture 2, M2) : déjà dans le code (`ARRONDI_TOLERANCE`).
 
-**Écarts restants entre ce texte et la tête lue**, à fermer avant la ligne `CODE-NARC-EXT` :
-1. **Phrase gelée R1** : le code (`cellules_externe_v2.reponse`) porte la phrase du brouillon 2 ; ce texte y ajoute la réserve
-   de l'intervalle (section « Critères de lecture gelés ») ; le code l'aligne mot pour mot, et l'essai de l'énumération des
-   réponses la vérifie.
-2. **Tête finale** : l'essai que le développeur ajoute et l'épreuve par mutation ne doivent changer aucun module de la lecture
-   hors de la phrase R1 ; la contre-lecture du code final compare la tête finale à la tête lue, module par module, et la
-   fiche cite la tête finale.
+**Écarts entre ce texte et la tête finale : aucun connu.** Les deux qui restaient au brouillon 3 sont fermés : la phrase gelée
+R1 est alignée mot pour mot (`cellules_externe_v2.reponse`, tête finale) ; la tête finale ne change aucun autre module de la
+lecture. Les couples de la contre-lecture 3 se règlent dans ce texte, sans code : la révision du jeu n'est pas comparée par
+le code, le texte le dit (C2) ; la valeur « sans plancher » des listes de R1 et R2 est déjà rendue par le code (C3) ; la
+ligne `LECTURE-NARC-EXT` est refusée dès la lecture du registre (C4) ; le code ne compare pas la date du `run-id` au
+lancement (C5). La contre-lecture du code final vérifie l'ensemble avant la ligne `CODE-NARC-EXT`, et la fiche cite la tête
+finale.
 
 **Décisions de ce texte sur ce que le code ne tranche pas** (contre-lecture 2, A23, A26, A28 ; consigne de la mère) : le
 journal du code est gardé (« Lignes de registre ») ; le code exécuté se contrôle par la règle DF-02 de T0.7 (liste d'arrêt
@@ -807,7 +832,7 @@
    (contre-lecture 1, § 5) et relevé, sur la forme des métadonnées, que Qwen3-32B a seul le domaine « env » et Llama-3.1-70B
    seuls « edu » et « sport », et que le champ `scenario_domain` du Llama diffère du domaine des auteurs dans 14 domaines
    (correspondance un à un) ; a exécuté en partie le script des auteurs sur des données factices ; aucun score réel.
-   (d) **La mère** (session `session_013QMayjsoZJFBUCqcnvD5h1`) : a reçu les rapports (b), (c), (e) et (f) et les brouillons de
+   (d) **La mère** (session `session_013QMayjsoZJFBUCqcnvD5h1`) : a reçu les rapports (b), (c), (e), (f) et (h) et les brouillons de
    ce texte ; d'après les lignes R-3333, R-3335, R-3336 et R-3341, elle connaît les comptes de forme et les constats cités, et
    n'a lu aucune aire ni aucun score sur les fichiers publiés. **La mère confirme cette ligne au scellement** (les
    contre-lecteurs n'ont lu que les registres) ; si elle est incomplète, une nouvelle version du brouillon est écrite avant le
@@ -819,6 +844,14 @@
    seulement) ; un point de la simulation de puissance rejoué (données simulées) ; lignes R-3333, R-3335, R-3336 et R-3341.
    (g) **Observation de contexte, sans score**, lue avant ce texte par le programme (brouillon 4, l. 12-24 ; contre-lecture
    3, l. 12) : point 2 ci-dessus.
+   (h) **Contre-lecteur 3 de ce texte** (Claude Sonnet 5.5, agent neuf ; rapport `f8ca72e2…`) : aucune donnée réelle ; code
+   lu par `git show` et `git archive` au commit `cde3b990`, `git log` et `git diff --stat` jusqu'au commit `b46c678d` ;
+   fonctions du code exécutées sur des entrées factices ; `verifier-texte` sur une copie du brouillon 3 ; le script de
+   puissance du point de l'écart rejoué (données simulées) ; empreintes de vingt-deux fichiers cités, sans les ouvrir.
+   (i) **Développeur, de la tête lue à la tête finale** : essais, épreuve par mutation et jouet de bout en bout sur
+   **vecteurs factices** aux formes publiées (1 054 lignes pour l'étage des comités, 1 320 pour l'étage stéganographique,
+   couches et largeurs de la bande) ; la réponse et les états de ce jouet n'ont aucune valeur de lecture (sa pièce le dit) ;
+   aucun score sur les fichiers publiés d'après la pièce.
 5. **Le rédacteur** n'a lu aucun fichier de données, aucun score, aucun résultat de ce bras. Brouillon 1 : il a lu, dans le
    brouillon 4 (prédiction N3), la mention d'un résultat antérieur du programme sur ses propres sondes, dont il ne tire rien
    ; hors de sa liste, il a vu des lignes du registre des décisions qui citent R-2175, R-2184, R-2735 ou R-3310 (R-2176,
@@ -835,7 +868,10 @@
    `externe_v2.py` qui portent les gardes et la garde de reproduction ; les sujets des commits de la branche ; les pages 17,
    18 et 27 à 30 du PDF, relues pour le réexamen de l'augmentation. Il a exécuté la commande `verifier-texte` (texte
    seulement) et la fonction `taches` (noms de plis factices), sans données, et un point de la simulation de puissance
-   (données simulées). Aucune ligne du registre des décisions lue pour ce brouillon. La puissance est calculée sur données
+   (données simulées). Aucune ligne du registre des décisions lue pour le brouillon 3 ni pour la version. Version : la contre-lecture 3 en
+   entier ; la différence de `src/` entre la tête lue et la tête finale ; les sujets des trois commits qui les séparent ; la
+   sortie du jouet aux formes publiées (vecteurs factices) en entier ; il a exécuté `verifier-texte` avec le code de la tête
+   finale sur une copie à entropie d'essai, sans données. La puissance est calculée sur données
    simulées seulement.
 
 ## Frontière : ce que ce texte ne dit pas
@@ -858,8 +894,8 @@
 7. **Ne pas reproduire ne réfute pas l'article** (R8) : fichiers, effectifs, recette ou notre chaîne peuvent différer ; un
    écart du témoin de recette n'est pas un défaut de l'article sans audit du chargement.
 8. **« Non tranché à cette puissance » n'est pas un échec** : si l'aire vraie de chaque cellule vaut 0,99 à 0,995 (la valeur
-   publiée, arrondie), c'est l'issue la plus probable ; si elle vaut 0,9999 ou plus, « oui » sort presque toujours (section
-   « Puissance »).
+   publiée, arrondie), « oui » sort au plus 33 à 61 fois sur cent et les autres issues se partagent le reste ; si elle vaut
+   0,9999 ou plus, « oui » sort presque toujours (section « Puissance »).
 9. Pas de rappel à taux de fausse alarme fixé (20 témoins dans l'étage stéganographique), pas de test séquentiel, pas de
    lecture par message au-delà du descriptif.
 10. **Le lien entre le script publié des auteurs et les Tables 2 et 3 n'est pas vérifié par exécution** (section « Recette »,
@@ -927,7 +963,7 @@
 |---|---|---|---|
 | M1 configuration illisible par le code | majeur | adoptée : six lignes seules sous le titre ; la prose passe dans « Notes de la configuration canonique » ; la clé `texte` est gardée (le code la lit) ; `run-id` donne la forme ; entropie d'au moins 2³². Contrôle `verifier-texte` du code (tête lue) rejoué : brouillon 2 refusé (code 2) ; brouillon 3 accepté (code 0) sur une copie où le seul marqueur d'entropie est remplacé par un entier d'essai ; sur le brouillon lui-même, seul refus : la valeur d'entropie, laissée à la mère | Configuration ; Notes de la configuration |
 | M2 tolérance d'arrondi | majeur | adoptée : les quatre comparaisons à 10⁻⁹ près, comme le code | Seuil |
-| M3 phrase trop générale sur une reproduction exacte | majeur | adoptée : « non tranché » le plus probable si l'aire vraie vaut 0,99 à 0,995 ; « oui » presque toujours à 0,9999 ou plus | Puissance ; Frontière n° 8 |
+| M3 phrase trop générale sur une reproduction exacte | majeur | adoptée avec correction de la contre-lecture 3 : « oui » borné à 33–61 % (0,99 à 0,995), le reste réparti entre « en partie » et « non tranché », non simulé ; « oui » presque toujours à 0,9999 ou plus | Puissance ; Frontière n° 8 |
 | M4 réserve de l'intervalle hors des phrases gelées | majeur | adoptée pour la phrase de réponse R1 (**phrase gelée changée**, le code s'aligne) ; non adoptée pour la ligne C2, dont l'état « reproduit » est l'étiquette que lisent les règles T et R (sens fixé à « Seuil ») ; valeur de l'écart à sa marge rejouée avec le script scellé : 0,160 (pièce `4f51889f…`) | Critères ; Seuil ; Puissance |
 | M5 écarts texte-code (A19 à A30) | majeur | liste refaite contre la tête lue `cde3b990` : écarts 1 à 18 et A19 à A30 lus fermés ; restent la phrase R1 et la tête finale ; décisions de texte écrites (journal gardé, A23 ; règle DF-02, A26 ; gardes n° 8 et 9 avant le manifeste, relance en nœud, A28 ; numéros de la liste d'arrêt inchangés, A29) | Code ; Liste d'arrêt ; Lignes de registre |
 | m-D1 unité de rééchantillonnage des comités | mineur | déclarée : conséquence de B3 de la contre-lecture 1 (pli gardé ; effectif lisible des comités : au moins 10 plis gardés) | ce tableau ; Recette ; Seuil |
@@ -935,18 +971,35 @@
 | m-D3 garde de reproduction sans valeur de lecture | mineur | déclarée (contre-lecture du code, m10) ; version 2 nommée | ce tableau ; Métrique |
 | m-D4 sixième clé `texte` | mineur | déclarée : ajoutée par le rédacteur au brouillon 2 pour fixer le chemin du texte scellé (contre-lecture 1, B4) ; le code la lit | ce tableau |
 | m-D5 plancher des comités retiré | mineur | raison écrite (coût, lecture secondaire) | Recette |
-| m-D6 statut vrai aux deux états | mineur | adoptée : statut réécrit, les trois inscriptions de la mère nommées | Statut |
+| m-D6 statut vrai aux deux états | mineur | adoptée : statut réécrit, les inscriptions de la mère nommées (dans la version : une seule, l'entropie) | Statut |
 | choix du rédacteur (§ 2) | mineurs | raisons écrites : comités sans plancher ni placebo (coût) ; scikit-learn → arrêt avant lecture (un seul coup) ; métadonnées lues avant le manifeste, aucune n'est un score ; « un seul tirage, deux usages » ; phrases de la grille D gelées par la fiche (empreinte de `statistiques_v1.py`) | Recette ; Liste d'arrêt |
 | m1 exposition de la mère | mineur | adoptée : « la mère confirme cette ligne au scellement » | Ce que les auteurs savaient (d) |
 | m2 exposition du contre-lecteur 2 | mineur | adoptée | Ce que les auteurs savaient (f) |
 | m3 critère de G0 | — | rien à faire | — |
 | m4 n° 2 « refus » et « ouverture » | mineur | adoptée : « arrêt » pour les deux moitiés | Liste d'arrêt n° 2 |
 | m5 journal et « rien d'écrit » | mineur | adoptée avec A23 : seule la ligne du journal s'écrit avant le manifeste | Liste d'arrêt ; Plan n° 2 |
-| m6 garde de mémoire avant l'ouverture | mineur | adoptée sous forme de contrôle de la mère avant le lancement (au moins 8 Go libres, estimation non mesurée) ; pas de garde de code | Liste d'arrêt n° 11 ; Plan n° 2 |
+| m6 garde de mémoire avant l'ouverture | mineur | adoptée sous forme de contrôle de la mère avant le lancement (au moins 8 Go libres ; dans la version, pointe mesurée sur le jouet aux formes publiées : 3 748 Mo) ; pas de garde de code | Liste d'arrêt n° 11 ; Plan n° 2 |
 | § 6 pièces hors de `main` | mineur | adoptée : à faire entrer dans `main` avant le scellement | En-tête ; Plan n° 0 |
 | § 6 précision de la p. 30 | mineur | adoptée : le membre « wasn't used for the main results » décide | Recette |
 
-- **Contre-lecture 3** : `<<CONTRE_LECTURE_3_NARC_EXT>>` — vérification courte de la différence brouillon 2 → brouillon 3 par
-  un agent neuf d'un autre modèle que le rédacteur, à qui la mère donne explicitement les brouillons 2 et 3, les rapports des
-  contre-lectures 1 et 2, le relevé des cinq points de recette et le code à la tête finale ; l'entrée portera l'empreinte du
-  brouillon relu, le chemin et l'empreinte du rapport, et le traitement de chaque remarque.
+- **Contre-lecture 3** : Claude Sonnet 5.5 (`claude-sonnet-5-5`), sous-agent neuf, autre modèle que le rédacteur, même
+  famille (R2, N-052), ni rédacteur ni développeur ; vérification courte de la différence brouillon 2 → brouillon 3 ; mandat
+  `docs/notes/narcbench-8b-v1/mandat-verification-courte-brouillon3-texte-court-v1.md`. Brouillon relu :
+  `prereg/narcbench-bras-externe-v1-brouillon3.md`, `fae8a96ccc75e592e8ca12c5b156a19775388c14f345d94fbf77d6fd8cbc0a90`.
+  Rapport : `prereg/contre-lectures/narcbench-bras-externe-v1-brouillon3-cl3.md`,
+  `f8ca72e2462169d106910f96d6953316bacb617de32ae30bdc17c6439aeb4a57`. Verdict : « scellable après ces couples exacts »,
+  aucun bloquant ; cinq couples (§ 7 du rapport). Traitement dans ce texte (chaque couple appliqué par remplacement exact, à
+  unicité contrôlée ; détail ligne à ligne : pièce `differences-brouillon3-vers-version-v1.md`) :
+
+| remarque | classe | traitement dans la version | où |
+|---|---|---|---|
+| C1 « non tranché, issue la plus probable » non soutenue | majeur | appliqué tel quel aux trois endroits : « oui » borné à 33–61 fois sur cent (57–78 sans indépendance), les autres issues se partagent le reste, non simulé | Puissance ; Frontière n° 8 ; tableau de la contre-lecture 2 (ligne M3) |
+| C2 révision du jeu non comparée par le code | écart texte-code | appliqué tel quel : la révision est consignée au manifeste, non comparée ; les empreintes des huit fichiers la fixent | Liste d'arrêt n° 1 |
+| C3 « sans plancher » absent des listes de R1 et R2 | mineur | appliqué tel quel : gabarit de la liste des planchers de R1 et R2 ; aucun mot fixe des phrases ne change ; le code rend déjà cette valeur | Critères (R1, R2) |
+| C4 place de la ligne `LECTURE-NARC-EXT` | mineur | appliqué tel quel, deux endroits | Liste d'arrêt (« Ordre ») ; Plan n° 2 |
+| C5 ce que le code vérifie du `run-id` | mineur | appliqué tel quel | Notes de la configuration canonique |
+| suggestion : « trente fois sous la tolérance » | — | ajoutée | Recette (réexamen de l'augmentation) |
+| suggestion : « à 10⁻⁹ près » dans la table de la règle C | — | ajoutée aux conditions des lignes C2 et C3 (colonne des conditions, pas des phrases) | Critères |
+| suggestion : raison de l'absence de réserve pour R2 | — | ajoutée ; valeurs des pièces scellées à la marge : 0,002 au pic, **0,004** à l'écart (le rapport citait 0,001, valeur de la grille à 0,97, au-dessus de la marge de l'écart) | Seuil |
+| suggestion : réserve sur la phrase F1 | — | non retenue : changerait une phrase gelée de plus ; la réponse au barreau (R1) est la phrase qui conclut et porte la réserve ; dit dans le texte | Critères |
+| constat : phrases T0, T3, T4 plus détaillées dans le code | — | pas de couple ; la fiche du code fixe leur forme | Code |
```
