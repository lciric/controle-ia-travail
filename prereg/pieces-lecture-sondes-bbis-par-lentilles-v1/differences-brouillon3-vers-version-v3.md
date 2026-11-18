# Différences du brouillon 3 à la version — texte « lecture des sondes de l'étape B bis par la lentille publique » — v1 — liste v3

- **Auteur** : le rédacteur du texte (sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, modèle Opus 5.5), le
  2026-11-18 à 18:59:35Z (`date -u`).
- **Remplace, pour le contrôle de la différence**, les listes v1 (`prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v1.md`, `67ae1706dc46121ff051ede0b92713e9fae90030935e86b9c1c14b086f8cbd07`) et v2 (`prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v2.md`, `9dac5875435ac0e881c200ea2b22a6ad1c73016e9de4ddc57fc425e09809fe7d`), scellées, non
  réécrites : mêmes 44 changements que la v2, plus les changements 45 et 46, demandés par la session mère.
- **Brouillon 3** : `prereg/lecture-sondes-bbis-par-lentilles-v1-brouillon3.md`, `49b0921d585944fd1e326bdea6155ad67e64719d6ab2673a022f415f084f256a` (scellé).
- **Texte candidat final** (non scellé ; la mère le scelle après contrôle de cette différence) : `prereg/lecture-sondes-bbis-par-lentilles-v1.md`, empreinte au moment du `diff`
  ci-dessous : `001fd5c0ee431dfaf9ec83c2d803dceed3d85be3fbf8bbb0360d6009dea268ff`.
- **Rapport appliqué** : `prereg/contre-lectures/lecture-sondes-bbis-par-lentilles-v1-brouillon3-verif1.md`,
  `5398f2e90f2dac1b5243601f89d609fb3c2a24773126b3391cfdab8953d5aedc` (vérification 1 des corrections). Points 2 à 5 : ceux du message
  de la mère qui commande la version.
- **Pièces de calcul** (V-M3), scellées dans ce dossier : `bornes_calibration_beta_binomiale_v1.py`
  (`a8763c96a3f945e680700f121c800d0d636f129aa3fb64ee71f23f97b01b675e`) et sa sortie `sortie-bornes-calibration-beta-binomiale-v1.txt`
  (`61bf13cd5e0c706c9e1bf0ede6b15b0b7dff7ae6af6006dbe36b759185330e5a`).
- **Méthode** : copie du brouillon 3, puis remplacements exacts (chaque ancien passage exigé une fois et une seule, arrêt sinon) ;
  aucune autre écriture.

## Liste des changements, un par ligne, dans l'ordre du texte

Les changements 1 à 42 viennent de la liste v1, 43 et 44 de la liste v2, repris tels quels ; 45 et 46 sont neufs.

1. Titre : « — v1 — brouillon 3 » → « — v1 » — point 5 (marqueurs).
2. « Auteur » : reprise commandée par la mère sur la vérification 1 — point 5.
3. « Date » : empreinte du brouillon 3 scellé ; heures de la version — point 5.
4. « Documents » : brouillon 3, rapport de la vérification 1 et mandat de cette vérification, avec leurs empreintes — point 5.
5. « Documents » : empreintes du code cité inchangées à la tête `70bdd769…` (rapport, « version finale », point 5) ; ajout déclaré du
   rédacteur : égales aussi à la tête `19947280…` — point 5.
6. « Statut » : version candidate non scellée ; scellement par la mère par `controle_ia.prereg.sceller_prereg` après contrôle de la
   différence ; « la ligne `SCELLEMENT-LENTILLES-BBIS` n'est inscrite que si `VERDICT-BBIS` est absente à ce moment ; la mère le relève
   par les clés seulement » ; renvoi à la déclaration de la mère — point 5 ; rapport, « version finale », points 5 et 6 ; V-m11.
7. « Ce que l'auteur savait » : alinéa « Lu pour la version » (lectures du rédacteur pour cette version) — point 5 (déclarations).
8. « Ce que l'auteur savait » : alinéa « Déclaration de la session mère » — point 4 ; V-m11.
9. E-2 : agrégation écrite `lineaire` → `max`, `attention` → `attention` — V-m3.
10. E-2, exclus : `dispersion_ordres_calcul`, `doses`, `couches`, `plis`, `manifeste`, `duree_s` nommés — V-m3.
11. « Attendu » : trois formes (a), (b), (c), seules admises ; toute autre combinaison : arrêt — V-M1.
12. E-3 : ligne `CODE-BBIS` lue (clé, heure, chemin de la fiche, commit seulement) — V-m2.
13. « Métrique », point 6 : langue des familles appuyée sur le code (`plis_v1.py`, l. 320-327, empreinte) — V-m13.
14. « Plan », point 3 : clé des témoins `<couche>/<nul>/<cellule>/<pli>/<rôle>/<vecteur>` (V-m8), parenthèse du nul isotrope partagé
    accordée (V-m8, adaptation déclarée), clé des témoins du nul refait par direction ajoutée (V-M2).
15. « Plan », point 4, titre : session neuve sans dossier de course, N9 tranché — point 3.
16. « Plan », point 4, clé : N8 tranché ; clé de la session neuve venue de la configuration de son environnement ; clé absente : arrêt —
    point 3 ; V-m12.
17. « Plan », point 4, lentille : définition de « lisible » pour `provenance` — V-m4.
18. « Plan », point 5 : « au rang près » défini au cas sain (V-m9) ; artefact défini par lentille (V-B1).
19. « Plan », point 6, indice de couche : empreintes des matrices 7, 15, 23 relevées par indice et comparées — V-m5.
20. « Plan », point 6, garde du rapport à ε : repli pour les deux lentilles de la couche, nul refait par vecteur, témoins, lectures
    « remplacées », coût — V-M2.
21. « Plan », point 6, calibration : quantiles sous la loi bêta-binomiale exacte, nouveaux exemples — V-M3.
22. « Critères », règles : exception de la phrase gelée « famille sur-représentée » — V-m7.
23. « Liste d'arrêt », ligne « SHA-256 ou taille… » : la lentille publique en est retirée — V-m6 (adaptation déclarée : une seule ligne).
24. « Liste d'arrêt », empreintes de E-1 et E-2 — V-m1.
25. « Liste d'arrêt », ligne des échecs : remplacée (mise en forme en deux colonnes, déclarée) — V-M1.
26. « Liste d'arrêt », garde de la fonction de lecture : artefact par lentille — V-B1.
27. « Liste d'arrêt », lentille d'une autre taille ou empreinte : une seule ligne, action du couple — V-m6.
28. « Qui, quelle machine », « Machine » : session neuve, N9 tranché ; relevés de l'auteur refaits au montage — point 3 ; V-m12.
29. « Frontière », point 3 : phrase « la description par la direction transposée n'est pas faite » gardée avec la suivante — V-m7.
30. « Frontière », point 12 : N10 tranché — point 3.
31. « Lignes de registre » : `CODE-BBIS` parmi les clés lues — V-m2.
32. « Code neuf », essais des entrées : formes (a), (b), (c) et leurs artefacts (V-M1) ; empreintes de E-1 et E-2, lignes de registre
    (V-m10).
33. « Code neuf », essais du montage : comparaison de `readout.py`, lentille absente — V-m10.
34. « Code neuf », essais de lecture : deux artefacts sur la fausse lentille (V-B1) ; bord de la garde du rapport à ε (V-m10).
35. « Code neuf », essais des nuls : artefact de calibration « scores des témoins multipliés par 1,5 » (V-m10, choix déclaré) ;
    « bornes recalculées » sans « binomiales » (V-M3).
36. « Nœuds » : bloc « Ouverts » remplacé par N8, N9, N10 tranchés, option (a), avec la mention — point 3 ; V-m12.
37. « Contre-lecture » : alinéa « Vérification des corrections… à commander par la mère » retiré ; entrée « Contre-lecture 2
    (vérification des corrections) » — point 2.
38. « Contre-lecture » : titre du tableau de la contre-lecture 1 (« tient lieu de « Changements du brouillon 2 au brouillon 3 » ») —
    point 5 ; trois lignes « le nœud reste ouvert » → « tranché ensuite, option (a) » — point 3.
39. « Contre-lecture » : tableau « Traitement des remarques de la vérification 1 », couples non appliqués tels quels, incohérence
    résiduelle signalée — point 2.
40. « Contre-lecture » : « État au validateur » rejoué sur la version (liste vide) — point 5.
41. Section « Changements du brouillon 3 à la version » ajoutée — point 5.
42. Forme seulement : la ligne d'en-tête du bloc des nœuds tranchés repliée sur deux lignes.
43. « Plan », point 6, ordre de grandeur : « ≈ 13 min si la garde du rapport à ε impose les nuls par direction » → « ≈ 14 min … » —
    cohérence avec V-M2, demandée par la session mère sur signalement du rédacteur.
44. « Qui, quelle machine », durée : « dont ≈ 7 à 13 min de produits au débit du banc » → « dont ≈ 7 à 14 min … » — cohérence avec V-M2,
    demandée par la session mère sur signalement du rédacteur.
45. « Contre-lecture », phrase « Effets de bord » sous le tableau de la contre-lecture 1 : datée — « déclarés au brouillon 3 » ; « ≈ 13 min »
    gardé comme valeur du brouillon 3, avec « dans la version, ≈ 14 min, après le couple V-M2 de la vérification 1 : plan, point 6 » —
    cohérence avec V-M2, demandée par la session mère.
46. « Contre-lecture », paragraphe sous le tableau de la vérification 1 : « Incohérence résiduelle, signalée et non corrigée » réécrit en
    constat exact (« Écart signalé, puis corrigé » par les changements 43 et 44, à la demande de la session mère) — cohérence avec V-M2,
    demandée par la session mère.

**Non appliqué** : la remarque « pour mémoire » sur le signe + de la requête `q` (hors des couples, sans couple).

**Durées du repli de la garde du rapport à ε, relevées dans tout le texte candidat** (recherche des mentions de minutes, de lectures et
de « par direction ») : plan, point 6, garde (« au plus ≈ 176 000 lectures de plus, ≈ 7 min ») ; plan, point 6, ordre de grandeur
(« ≈ 14 min ») ; « Qui, quelle machine » (« ≈ 7 à 14 min ») ; « Effets de bord » (valeur du brouillon 3 datée, et valeur de la
version) ; paragraphe « Écart signalé, puis corrigé ». Toutes exactes ; aucun passage de durée inexact ne reste.

## Sortie de `diff`

Commande (depuis la racine du dépôt) : `diff -u prereg/lecture-sondes-bbis-par-lentilles-v1-brouillon3.md prereg/lecture-sondes-bbis-par-lentilles-v1.md`

```diff
--- prereg/lecture-sondes-bbis-par-lentilles-v1-brouillon3.md	2026-11-18 18:25:12.899699761 +0000
+++ prereg/lecture-sondes-bbis-par-lentilles-v1.md	2026-11-18 18:59:08.937961226 +0000
@@ -1,16 +1,18 @@
-# Préenregistrement descriptif — lecture, par la lentille publique côté sortie, des directions des sondes apprises sur la tâche (étape B bis de T0.7) — v1 — brouillon 3
+# Préenregistrement descriptif — lecture, par la lentille publique côté sortie, des directions des sondes apprises sur la tâche (étape B bis de T0.7) — v1
 
 - **Auteur** : rédacteur neuf, sous-agent de la session mère `session_013QMayjsoZJFBUCqcnvD5h1` (modèle servi : Opus 5.5), sur le mandat
   `docs/notes/neuron-lens-v1/mandat-redacteur-texte-lecture-sondes-bbis-par-lentilles-v1.md`
-  (`3010f726510856f202c62b5acd9c50166e1bd4860d88f45f1d50ca951cd732bb`), repris deux fois sur les messages de la mère du 2026-11-18
-  (décision de Lazar GO-2026-11-18-42, R-3349 ; choix de forme de la mère, R-3334 ; contre-lecture 1). Il n'a écrit ni T0.6, ni T0.7, ni
+  (`3010f726510856f202c62b5acd9c50166e1bd4860d88f45f1d50ca951cd732bb`), repris trois fois sur les messages de la mère du 2026-11-18
+  (décision de Lazar GO-2026-11-18-42, R-3349 ; choix de forme de la mère, R-3334 ; contre-lecture 1 ; pour cette version, reprise
+  commandée par la mère sur la vérification 1 des corrections). Il n'a écrit ni T0.6, ni T0.7, ni
   aucune pièce de l'apprentissage des sondes sur la tâche (texte, addenda, code), ni P3-bis, ni aucune pièce des tranches de la lecture
   par lentille neuronale ; il ne sera ni développeur, ni opérateur, ni lecteur de ce texte, ni lecteur ou juge d'aucun verdict nommé ici.
 - **Date (UTC, `date -u`)** : 2026-11-18. Brouillon 1 : lecture des pièces à partir de 16:41, entropie des graines tirée à 16:49:33,
   écrit de 16:58:55 à 17:02:37, scellé comme brouillon (`61ba10b9f2f6c8affc05eeda7ee52f5bde8e3c9ef8eac7192404d9f52bc777b8`).
   Brouillon 2 : écrit de 18:03:00 à 18:07:10, scellé comme brouillon (`271c421f089f39564527981fc98fb9f4bc3143e67e6491f6a48234c224cef1cc`).
-  Brouillon 3 : reprise à 18:16:19 sur la contre-lecture 1, écrit de 18:19:51 à 18:25:08 (`date -u` relevé juste avant les dernières
-  vérifications et le scellement comme brouillon).
+  Brouillon 3 : reprise à 18:16:19 sur la contre-lecture 1, écrit de 18:19:51 à 18:25:08, scellé comme brouillon
+  (`49b0921d585944fd1e326bdea6155ad67e64719d6ab2673a022f415f084f256a`). Version : reprise à 18:48:07 sur la vérification 1 des
+  corrections, écrite de 18:52:44 à 18:55:12 (`date -u` relevé juste avant le dernier passage du validateur).
 - **Commit du code d'analyse** : **aucun code n'existe**. Par le choix de forme de la mère (R-3334), le code est cité après le
   scellement, par la ligne `CODE-LENTILLES-BBIS` du registre propre, inscrite avant toute exécution (écart au gabarit, déclaré). Commits
   lus : branche de travail de la mère `claude/affectionate-bardeen-j7kddp` à `ba8dcfbf076e936729ee6668b9774031337d0a3e` (tête relevée
@@ -20,6 +22,12 @@
   - mandat (ci-dessus) ; brouillons 1 et 2 (ci-dessus) ; rapport de la contre-lecture 1,
     `prereg/contre-lectures/lecture-sondes-bbis-par-lentilles-v1-brouillon2-cl1.md`,
     `f876f83a250dce85d83ab6e73f8ec0d40ffbc33640d625962838f774e3b94ea2` ;
+  - brouillon 3, `prereg/lecture-sondes-bbis-par-lentilles-v1-brouillon3.md`,
+    `49b0921d585944fd1e326bdea6155ad67e64719d6ab2673a022f415f084f256a` ; rapport de la vérification 1 des corrections,
+    `prereg/contre-lectures/lecture-sondes-bbis-par-lentilles-v1-brouillon3-verif1.md`,
+    `5398f2e90f2dac1b5243601f89d609fb3c2a24773126b3391cfdab8953d5aedc` ; mandat de cette vérification,
+    `docs/notes/neuron-lens-v1/mandat-verification-corrections-texte-lentille-publique-v1.md`,
+    `71dbd76ab3d277d10e4e4fa8ec6c8dc42bc8b8ecab1160b442b024d5a266fc34` ;
   - apprentissage des sondes sur la tâche, lus **pour la forme de leurs sorties seulement** : texte scellé
     `prereg/T0.7-etape-B-bis-v1.md`, `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb` (« T ») ; premier addendum
     `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md`, `f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7` (« A1 ») ;
@@ -35,6 +43,8 @@
     `9db2b40b15c9ca76f0c4bd4f29923cc06909b362de26a212bfc780133a4c9e33` ; `src/controle_ia/t07bbis/apprentissage_carte_v1.py`
     (l. 117-123 : la sonde rendue), `4b98fcb931d0ea09e663c7c3093f294db8630537e4322e44b69ba2d50bd743d7` ;
     `src/controle_ia/t06/configuration.py` (`nom_condition`, l. 42-48), `fe859b9a0016cb3fdd69002a37bf26fc344405875ebe6f9ec95ee3a47be71553` ;
+    empreintes de ce code inchangées à la tête `70bdd769b9e788d073a832073ce983dd8a0b4a87` de la branche de travail (vérification 1),
+    et à la tête `19947280cd22811bdae109708eac6c5e0626606c` (relevé du rédacteur, 18:49 UTC) ;
   - lentille publique, copies versées (branche principale, dossier `docs/sources/neuron-lens-lecture-20261113/huggingface/`, relevées
     le 2026-11-13 à la tête `d2527c3cdbaa60dd4b65cbca1604921f044e989a` du dépôt, manifeste `manifeste-sources-v2.tsv`,
     `6d679182bbbb3f73257a74e603594d1125702ad115aacc4e3622f0e9e268efd8`) : fiche `lentilles-neuronpedia-jacobian-lens-fiche.md`
@@ -63,11 +73,12 @@
   - code lu pour définir la direction d'une sonde et sa couche : `src/controle_ia/sondes/familles.py`,
     `6758b651fdcbc6d0108a03263b79ffb1e7c5d0a8be57b0f10502c1645d2b457e` (l'empreinte que cite T) ;
     `src/controle_ia/harnais/activations.py`, `adeb5856d430f3a6163989c2a53c8ced459235c6dcdd03834b694404c57e0095` (l. 1-80).
-- **Statut** : **brouillon 3**, scellé comme brouillon (compagnon `.sha256`) ; aucun calcul, aucune dépense, aucun résultat lu. Il ne
-  vaut préenregistrement qu'après vérification des corrections, nœuds restants tranchés, scellement d'une version et inscription de la
-  ligne `SCELLEMENT-LENTILLES-BBIS` **alors que `VERDICT-BBIS` est absente du registre propre de l'apprentissage des sondes sur la tâche**
-  (règle la plus stricte, la même qu'au « Plan d'analyse », point 1, et qu'à la « Liste d'arrêt ») ; présente à ce moment : texte
-  exposé, nœud.
+- **Statut** : **version v1, texte candidat, non scellé** ; aucun calcul, aucune dépense, aucun résultat lu. La session mère le
+  scelle, après un contrôle de la différence (brouillon 3 → version) par un agent neuf, par `controle_ia.prereg.sceller_prereg` (qui
+  refuse un texte non conforme). **La ligne `SCELLEMENT-LENTILLES-BBIS` n'est inscrite que si `VERDICT-BBIS` est absente à ce moment ;
+  la mère le relève par les clés seulement** (règle la plus stricte, la même qu'au « Plan d'analyse », point 1, et qu'à la « Liste
+  d'arrêt ») ; présente à ce moment : texte exposé, nœud. Les expositions de qui a écrit les dernières corrections sont déclarées
+  ci-dessous (« Déclaration de la session mère »).
 
 ## Ce que l'auteur savait avant le scellement
 
@@ -87,6 +98,12 @@
   `commun_v1.py`, `apprentissage_carte_v1.py` et `lecture_v1.py` à `lecture_v3.py`) ; `t06/configuration.py` (l. 42-48) ; le compagnon
   du correctif (6) ; les identifiants git des fichiers de licence dans l'arbre versé ; un calcul des quantiles d'une loi binomiale
   (aucune donnée).
+- **Lu pour la version** : le rapport de la vérification 1 des corrections (entier, compagnon vérifié), dont les valeurs qu'il cite
+  (bornes, risques, comptes de lectures, têtes de branche) ; le chemin et l'empreinte de son mandat (sans lecture) ;
+  `src/controle_ia/t07bbis/plis_v1.py`, l. 318-328 (code : clés des champs de l'action, V-m13) ; `src/controle_ia/prereg.py`
+  (`sceller_prereg`, l. 63-67) ; empreintes du code cité recalculées à la tête `19947280cd22811bdae109708eac6c5e0626606c` ; un calcul
+  des lois bêta-binomiale et binomiale (aucune donnée ; script et sortie versés dans
+  `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/`).
 - **Valeurs vues** (aucune n'est une aire, un score, une issue ou un verdict d'une chaîne interdite) : celles déclarées aux brouillons 1
   et 2 ; au brouillon 3, des **constantes du code** de l'étape B bis (couches 7, 15, 23 ; familles ; grille de régularisation 10⁻³,
   10⁻², 10⁻¹ ; 800 directions du plancher ; 100 réétiquetages ; niveaux décisifs 0,99 et 0,995, niveau de réserve 0,95, seuil des
@@ -103,6 +120,11 @@
   ligne de contrôle déclarée). **Aucun choix de ce texte n'a pu être fait d'après une sortie de ces chaînes.** La mère, exposée depuis à
   un résultat du programme, n'a fixé aucun choix d'analyse : mesure, nuls, libellés et seuils de libellé sont de l'auteur ; les
   corrections du brouillon 3 suivent les remarques de la contre-lecture.
+- **Déclaration de la session mère** (vérification 1, V-m11 et « ce que la version finale doit porter », point 4) : la session mère est
+  exposée à un résultat du programme (le verdict du barreau « accumulation des scores sur l'épisode », R-3347) et à aucune sortie de
+  l'étape B bis ; elle n'a fixé aucun seuil, critère ni choix d'analyse de ce texte ; les changements du brouillon 3 à la version sont
+  l'application des couples du rapport de vérification et des trois options (a), rien d'autre. Le rédacteur, qui a écrit ces
+  changements, n'a lu aucun résultat du programme (ci-dessus).
 
 ## Vocabulaire (noms en clair ; les identifiants viennent en appui)
 
@@ -189,12 +211,13 @@
     `empreinte`. **`reglage` est une chaîne `famille-c<couche>-l2_<régularisation>`** (`commun_v1.reglage_nom`) : le code n'en garde que
     la famille et la couche, par l'expression `^(lineaire|attention)-c([0-9]+)-l2_` ; **la régularisation (suite de la chaîne) n'est
     ni gardée, ni écrite, ni imprimée** ; chaîne d'une autre forme : arrêt (« forme mal comprise »). Agrégation du lecteur honnête
-    déduite de sa famille (`commun_v1.AGREGATION_DE` : linéaire → maximum, attention → attention) ; son nom, pour l'empreinte :
+    déduite de sa famille (`commun_v1.AGREGATION_DE` : `lineaire` → `max`, `attention` → `attention`) ; son nom, pour l'empreinte :
     `enc-<cellule>-e<k>` (`validation_imbriquee_v1.apprendre_recette`, l. 255) ;
   - **exclus**, entre autres : `reglage` et `l2` de la sonde apprise, `taches_lues`, `plis_internes`, `echecs_internes`, `n_plancher`,
     `noms_deux_premieres`, `empreintes_deux_premieres`, `nuls_en_echec`, `n_reetiquetages`, `ordre2`, `enc.echecs_internes`, la valeur
     de tout `echec`, `fichiers_scores`, `fichiers_planchers`, `graines_derivees`, `controle_carte_processeur`, `couple_controle`,
-    `journal`, `variante`, `decision_variante`, le résumé de la mesure de dispersion, `texte`, `sans_aucune_aire`.
+    `journal`, `variante`, `decision_variante`, le résumé de la mesure de dispersion (`dispersion_ordres_calcul`), `doses`, `couches`,
+    `plis`, `manifeste`, `duree_s`, `texte`, `sans_aucune_aire`.
 - **E-1** `donnees/<run-bbis>/sondes-bbis.npz` (même fonction ; archive `numpy` non compressée, une entrée par tableau) — son SHA-256
   est calculé sur les octets du fichier entier (aucun tableau décodé) et comparé à `fichier_sondes.sha256` et au compagnon ; puis le
   fichier est **ouvert clé par clé** (`numpy.load(…, allow_pickle=False)`, liste des noms d'entrées seulement) et **seules les entrées
@@ -206,10 +229,19 @@
   `"<famille>:<nom>/<couche>/<agrégation>"` puis des octets en double précision de `w`, `[b]` et `q` s'il existe) : sonde apprise avec
   `nom_sonde`, `famille`, `couche`, `agregation` ; lecteur honnête avec `enc-<cellule>-e<k>` et la famille, la couche, l'agrégation
   déduites ci-dessus ; comparée à `empreinte_sonde` et à `enc.empreinte`.
-- **Attendu** : vingt sondes (cinq cellules × deux plis × deux rôles), sauf celles qu'un `echec` marque (« non lue : échec à
-  l'apprentissage »). Les cellules de transfert n'ont pas de sonde propre (T, plan, point 9).
+- **Attendu** : vingt sondes (cinq cellules × deux plis × deux rôles), moins celles que le code marque. Trois formes sont prévues par le
+  code (`validation_imbriquee_v1.apprendre_source`, l. 362-364 et 387-394 ; `marche_v4.ecrire_fermes`, l. 151-173), et elles seules sont
+  admises : (a) clé `echec` présente au niveau direct : `famille`, `couche`, `agregation`, `empreinte_sonde`, `nom_sonde` et le
+  sous-dictionnaire `enc` sont absents, et E-1 ne porte aucune entrée de cette cellule et de ce pli ; la sonde apprise est « non lue :
+  échec à l'apprentissage », son lecteur honnête « non lu : non appris, la sonde apprise ayant échoué » ; (b) clé `echec` absente au
+  niveau direct et présente sous `enc` : `enc.reglage` et `enc.empreinte` sont absents, et E-1 ne porte aucune entrée `enc_*` de cette
+  cellule et de ce pli ; le lecteur honnête est « non lu : échec à l'apprentissage » ; (c) aucune clé `echec` : tous les champs de la
+  liste blanche sont présents, ainsi que les entrées `sonde_w`, `sonde_b`, `enc_w`, `enc_b` ; `sonde_q` existe si et seulement si la
+  famille de la sonde apprise est `attention`, `enc_q` si et seulement si celle du lecteur honnête l'est. Toute autre combinaison :
+  arrêt (« forme mal comprise »). Les cellules de transfert n'ont pas de sonde propre (T, plan, point 9).
 - **E-3** les compagnons `.sha256` de E-1 et E-2 ; la ligne `SCORES-BBIS` (chemin, empreinte) ; la présence de la clé `VERDICT-BBIS`
-  dans le même registre (clé et heure seulement, jamais le fichier du verdict). **Des registres, l'opérateur ne lit que ces clés et
+  dans le même registre (clé et heure seulement, jamais le fichier du verdict) ; la ligne `CODE-BBIS` du même registre (clé, heure, chemin de la fiche, commit seulement), dont le
+  commit sert au développeur à vérifier les noms ci-dessus. **Des registres, l'opérateur ne lit que ces clés et
   heures, et les lignes du registre propre de ce texte.**
 - **Moment** (choix de forme de la mère, R-3334) : E-1 et E-2 ne sont ouverts par programme **qu'après** l'inscription de
   `VERDICT-BBIS`, et récupérés seuls, par leur chemin (clone partiel sans contenus, `--filter=blob:none`, puis extraction de ces deux
@@ -306,8 +338,9 @@
    - **familles de jetons nommées d'avance** (règles fixées ici, sur la chaîne décodée passée par `strip()`) : « nombres » : la chaîne
      s'écrit `^[0-9]+$` ; « coût » : la chaîne, en minuscules, est l'une de cost, costs, costly, price, prices, pricing, budget,
      budgets, expense, expenses, expensive, fee, fees, usd, dollar, dollars, $, spend, spent, spending, cheap, cheaper ; **choix déclaré :
-     mots anglais seulement, aucune famille en français** (les textes de la tâche que lit le modèle sont en anglais, d'après la
-     contre-lecture ; non vérifié par l'auteur) ; compte de chaque famille dans les vingt premiers jetons, et p de même forme ;
+     mots anglais seulement, aucune famille en français** (langue appuyée sur le code : les champs de l'action sont `ACTION`, `TITLE`,
+     `PROPOSAL`, `CONTROLS`, `COST`, `PREDICTION`, `src/controle_ia/t07bbis/plis_v1.py`, l. 320-327,
+     `7ba39db50674f9dbc3c6a6920ea03a60826d0bc7b7fe4bf66a262ad1acb45ab4`) ; compte de chaque famille dans les vingt premiers jetons, et p de même forme ;
    - **jeton de début** (128 000) : sa présence parmi les vingt premiers et son rang, rapportés pour chaque lecture (constat de G ; sans
      libellé).
 7. **Pôles alignés** (pour v au signe + ; le signe − rend les mêmes pôles, de signe opposé) : cosinus de v avec les 28 672 directions
@@ -354,17 +387,22 @@
    `numpy.random.Generator(numpy.random.PCG64(·))`, tirages en double précision, ramenés en simple précision pour la lecture ; clés :
    `lentilles-bbis/nul-isotrope/<couche>`, `lentilles-bbis/nul-isotrope-par-direction/<cellule>/<pli>/<rôle>/<vecteur>` (seulement si
    la garde du rapport à ε l'exige), `lentilles-bbis/nul-signes/<cellule>/<pli>/<rôle>/<vecteur>`,
-   `lentilles-bbis/temoins-calibration/<couche>/<nul>/<vecteur>` (pour le nul isotrope, `<vecteur>` vaut `couche`),
+   `lentilles-bbis/temoins-calibration/<couche>/<nul>/<cellule>/<pli>/<rôle>/<vecteur>` (pour le nul isotrope partagé,
+   `<cellule>/<pli>/<rôle>/<vecteur>` est remplacé par `couche`),
+   `lentilles-bbis/temoins-calibration/<couche>/nul-isotrope-par-direction/<cellule>/<pli>/<rôle>/<vecteur>` (seulement si la garde du
+   rapport à ε l'exige),
    `lentilles-bbis/colonnes-garde/<couche>`, `lentilles-bbis/essai/<garde>` ; un manifeste par course (configuration et empreinte,
    versions, graines, commit).
-4. **Montage, au processeur, dans le conteneur d'une session** (nœud N9 pour le choix de la session) :
+4. **Montage, au processeur, dans le conteneur d'une session neuve, qui ne porte aucun dossier de course** (N9 tranché, option (a),
+   « Nœuds ») :
    - **espace** : au moins 6 Go libres au départ ; pointe visée ≤ 4 Go ; dossier de travail neuf, propre à cette chaîne, qui porte
      aussi le cache des téléchargements (`HF_HOME` pointé dans ce dossier) ;
    - **clé** : la clé d'accès au modèle est lue **par son nom** (`HF_TOKEN`, présente dans l'environnement de la session), jamais
      imprimée, jamais écrite dans un fichier, un journal ou un manifeste ; sa présence et son caractère non vide sont testés sans
      l'imprimer ; **aucun mode de débogage** des bibliothèques de téléchargement (`HF_DEBUG`, `HF_HUB_VERBOSITY=debug`, journalisation
      « debug » de `urllib3`, `httpx` ou `requests`, `curl -v` ou `--trace`), qui imprimerait des en-têtes ; aucune machine louée,
-     aucune clé passée à une machine (nœud N8) ;
+     aucune clé passée à une machine (N8 tranché, option (a), « Nœuds ») ; la session neuve reçoit la clé de la configuration de son
+     environnement, jamais de la session mère ni d'une autre session (ni message, ni fichier, ni argument) ; clé absente : arrêt, nœud ;
    - **réseau, avant tout flux long** : lecture d'un octet par hôte et par sorte de fichier : un octet de la lentille publique, un octet
      d'un fichier de poids à porte avec la clé, un octet d'un fichier de chaque jeu de données du corpus des jetons gardés, l'en-tête du
      dépôt du voisin ; refus de l'un, ou clé absente ou vide : arrêt avant tout téléchargement long ;
@@ -383,7 +421,10 @@
    - **lentille publique** : téléchargée à la révision passée explicitement ; taille et SHA-256 vérifiés ; `LICENSE`, `NOTICE`,
      `USE_POLICY.md` du dossier vérifiés par identifiant git et taille ; contrôles de disposition repris de `neuronpedia_lens` du
      correctif (2) (`{"J": {0..30}}`, matrices carrées de même forme) ; **clé `provenance` lue : point de capture « block_output »
-     exigé, lisible** ; **les 31 matrices** : chacune distincte de l'identité et toutes distinctes deux à deux (écart maximal
+     exigé, lisible** (lisible = une clé `capture_point` dans `provenance`, de valeur `block_output` ; `source_layers` = 0 à 30 et
+     `d_model` = 4 096 comparés ; si `provenance` porte un `target_layer`, sa valeur est 31 (dernier bloc ; la configuration versée dit
+     `target_layer: 31`), toute autre valeur : arrêt ; les clés `source_layers`, `d_model`, `n_prompts` sont attendues et ne sont pas une
+     « disposition autre ») ; **les 31 matrices** : chacune distincte de l'identité et toutes distinctes deux à deux (écart maximal
      > 10⁻⁶ pour chacune des 465 paires ; un fichier mal assemblé ferait des doublons) ; écart relatif de chaque matrice à l'identité
      rapporté par couche, sans critère ; seules les matrices des couches 7, 15 et 23 sont gardées ensuite ;
    - **jetons gardés** : `05_act_corpus.py` puis `03_token_counts.py` (une seule fois) ; liste `catalog.kept` : nombre et empreinte
@@ -391,28 +432,41 @@
    - gardes du montage (« Liste d'arrêt ») ; ligne `MONTAGE-LENTILLES-BBIS`.
 5. **Garde de la fonction de lecture** (R5) : à chaque couche lue et pour chaque lentille, 64 colonnes de `W_down` tirées par graine ;
    les dix premiers jetons rendus par notre code égalent, au rang près, ceux de `read` du voisin appelé avec W_U en simple précision,
-   pour les 64 colonnes (cas sain) ; avec la matrice d'une autre couche à la place de J_ℓ (artefact), les dix premiers jetons diffèrent
-   (au rang près) pour **au moins 32 des 64 colonnes**. Rapporté sans critère : le nombre de colonnes dont le premier jeton diffère
+   pour les 64 colonnes (cas sain ; « au rang près » : mêmes dix identifiants ; un écart limité à des jetons dont les scores diffèrent
+   de moins de 10⁻⁴ en valeur relative est compté et rapporté, sans arrêt) ; artefact, défini par lentille : pour la lentille publique,
+   la matrice de la couche suivante dans l'ordre 7 → 15 → 23 → 7 mise à la place de J_ℓ ; pour la lentille des logits, dont la matrice
+   est l'identité à toute couche, une matrice de permutation des 4 096 coordonnées, tirée par la graine
+   `lentilles-bbis/essai/garde-lecture-logits-c<couche>` (forme `lentilles-bbis/essai/<garde>` du point 3), mise à la place de
+   l'identité ; dans les deux cas, les dix premiers jetons diffèrent de ceux du cas sain pour **au moins 32 des 64 colonnes**. Rapporté sans critère : le nombre de colonnes dont le premier jeton diffère
    quand le voisin fait le produit en demi-précision, comme la comparaison des lentilles.
 6. **Calcul** :
    - **contrôle de l'indice de couche** : pour chaque sonde, la matrice lue est celle de l'indice égal à sa `couche` (E-2), et
-     l'indice est écrit dans les tables à côté de l'empreinte de la matrice ;
+     l'indice est écrit dans les tables à côté de l'empreinte de la matrice ; au montage, l'empreinte de chacune des matrices 7, 15,
+     23 est relevée par indice ; au calcul, l'empreinte de la matrice lue est comparée à celle relevée pour l'indice égal à la couche de
+     la sonde ; écart : arrêt ;
    - **garde du rapport à ε** : ρ calculé pour chaque direction réelle (à sa norme lue), chaque lentille, et pour ses directions nulles
      et témoins ; minimum rapporté par (couche, lentille) ; si le minimum est ≥ 100 : indépendance à la norme tenue, rapportée ; s'il
-     est < 100 pour une (couche, lentille) : l'indépendance est écrite « non tenue » pour elle, et le nul isotrope et ses témoins y sont
-     **refaits par direction**, ramenés à la norme de v (clés `nul-isotrope-par-direction`), coût rapporté (au plus ≈ 160 000 lectures
-     de plus, ≈ 6 min de produits au débit du banc), dans la durée maximale ;
+     est < 100 pour une (couche, lentille) : l'indépendance est écrite « non tenue » pour cette couche, et, **pour les deux lentilles de
+     cette couche** (l'appariement du point 9 est gardé), le nul isotrope est refait par vecteur : M = 2 000 directions tirées par la clé
+     `lentilles-bbis/nul-isotrope-par-direction/<cellule>/<pli>/<rôle>/<vecteur>`, ramenées à la norme de v ; ses témoins : **200 par
+     vecteur**, clé `lentilles-bbis/temoins-calibration/<couche>/nul-isotrope-par-direction/<cellule>/<pli>/<rôle>/<vecteur>`, ramenés à
+     la même norme, chacun comparé aux M directions de son vecteur ; comptes mis en commun par (couche, lentille), n = 200 × le nombre de
+     vecteurs de la couche ; les lectures faites avec le nul partagé de cette couche restent en table, marquées « remplacées », et ne
+     portent aucun libellé ; coût rapporté (au plus ≈ 176 000 lectures de plus, ≈ 7 min de produits au débit du banc), dans la durée
+     maximale ;
    - lectures, nuls, statistiques, pôles, comparaisons (« Métrique ») ;
    - **calibration** : des directions témoins tirées de chaque nul (graines propres) passent par le chemin des directions réelles, et
      leurs p de concentration sont calculés contre les M directions nulles : nul isotrope, **1 000** témoins par couche ; nul des signes,
      200 témoins par vecteur ; comptes **mis en commun par (couche, lentille, nul)** (n = 1 000 pour le nul isotrope ; n = 200 × le
      nombre de vecteurs de la couche pour le nul des signes) ; sous le nul, la part attendue de p ≤ 0,05 vaut 100/2 001 ; la calibration
-     échoue si le compte de p ≤ 0,05 sort de [q_bas, q_haut], quantiles de la loi binomiale (n, 100/2 001) tels que P(X < q_bas) ≤ 10⁻⁴
-     et P(X > q_haut) ≤ 10⁻⁴, calculés par le code et écrits (par exemple [26, 77] pour n = 1 000, [12, 52] pour n = 600, [1, 23] pour
-     n = 200) ; pour n < 600, la borne basse est **volontairement lâche**, déclarée telle dans les tables ;
+     échoue si le compte de p ≤ 0,05 sort de [q_bas, q_haut], q_bas est le plus grand entier tel que P(X < q_bas) ≤ 10⁻⁴, q_haut le plus
+     petit tel que P(X > q_haut) ≤ 10⁻⁴, sous la loi exacte du compte quand les témoins d'un jeu partagent ses M directions nulles : pour
+     un jeu de n témoins, la loi bêta-binomiale (n ; 100 ; M − 99 = 1 901) ; pour plusieurs jeux mis en commun (un jeu de 200 par
+     vecteur), la somme de lois bêta-binomiales indépendantes ; bornes calculées par le code et écrites (par exemple [23, 85] pour un
+     jeu de 1 000 ; [1, 24] pour un jeu de 200 ; [12, 53] pour trois jeux de 200 ; [26, 79] pour cinq jeux de 200) ; pour n < 600, la borne basse est **volontairement lâche**, déclarée telle dans les tables ;
    - déclencheurs d'audit évalués et audits joués dans la même session ; tout est écrit dans des fichiers fermés ;
    - ordre de grandeur : ≈ 195 000 lectures (≈ 97 000 directions réelles, nulles et témoins, par lentille), ≈ 143 TFLOP, soit ≈ 7 min de
-     produits au débit du banc (≈ 13 min si la garde du rapport à ε impose les nuls par direction).
+     produits au débit du banc (≈ 14 min si la garde du rapport à ε impose les nuls par direction).
 7. **Comparaisons multiples** : aucune correction (descriptif) ; chaque compte de libellés porte son attendu par hasard ; nombre total
    de lectures écrit.
 8. **Lecture** : par le lecteur neuf, sur processeur, après `VERDICT-BBIS` scellée ; il applique les « Critères de lecture gelés » aux
@@ -453,7 +507,8 @@
 capte ; aucune phrase ne dit qu'une sonde détecte ou ne détecte pas le sabotage, lit ou ne lit pas « l'état saboteur », ni ne rapproche
 la lecture d'une aire ; le mot « soupçon » ne s'emploie que pour une famille sur-représentée ; les mots « nos lentilles » ou « notre
 lentille » ne désignent jamais la lentille lue ; aucune phrase ne dit que la sonde « lit » les jetons de sa lecture (« associe » ou
-« pousse » seulement) ; toute description au-delà des phrases gelées est marquée « description libre, après lecture, non
+« pousse » seulement), sauf la phrase gelée « famille sur-représentée », qui parle d'un soupçon (« la lecture ajoute un soupçon que la
+sonde lise […] ») : c'est la seule permise ; toute description au-delà des phrases gelées est marquée « description libre, après lecture, non
 préenregistrée ».
 
 **Audit de symétrie (R4)**, déclencheurs gelés, évalués et joués dans la session du calcul : (i) **trop beau** : les dix sondes apprises
@@ -476,23 +531,23 @@
 | clé absente ou vide ; requête vers Hugging Face, un hôte de stockage, un jeu de données du corpus ou le dépôt du voisin refusée ; fichier à porte refusé avec la clé (essai d'un octet, plan, point 4) | arrêt avant tout téléchargement long ; nœud |
 | moins de 6 Go libres au départ, ou moins de 1 Go pendant le calcul | arrêt, sans rien supprimer hors du dossier de cette chaîne ; compte rendu |
 | durée cumulée de la session de calcul au-delà de 8 h | arrêt ; versement de ce qui existe ; compte rendu |
-| SHA-256 ou taille d'un fichier de poids, du tokeniseur ou de la lentille publique différent de ce texte ; identifiant git d'un pointeur ou d'un petit fichier différent ; `LICENSE`, `NOTICE` ou `USE_POLICY.md` d'un autre identifiant git ou d'une autre taille | arrêt ; message à la mère |
+| SHA-256 ou taille d'un fichier de poids ou du tokeniseur différent de ce texte ; identifiant git d'un pointeur ou d'un petit fichier différent ; `LICENSE`, `NOTICE` ou `USE_POLICY.md` d'un autre identifiant git ou d'une autre taille | arrêt ; message à la mère |
 | lentille publique : disposition autre que `{"J": {0..30}}` de matrices 4 096 × 4 096 ; **clé `provenance` absente ou sans point de capture lisible** ; point de capture autre que « block_output » ; une matrice égale à l'identité ; deux matrices égales (écart maximal ≤ 10⁻⁶) | arrêt avant tout calcul ; nœud |
 | `readout.py` du commit `849bfe1678e28becceb1e3864afe5fc8297d02e4` différent de la copie versée dans `rms_norm_columns`, `transport` ou `read` (risque connu) | arrêt avant tout calcul ; nœud |
 | liste des jetons gardés d'un autre nombre que 89 498 ou d'une autre empreinte que `c37186add16770aa3c04bd0c16c417544b7e2a15b374ee85e47fbda7ec148d68` | arrêt avant tout calcul ; nœud |
 | `SCORES-BBIS` absente, ou en plusieurs lignes | rien ne part ; plusieurs lignes : nœud (la mère désigne la course, par les noms seulement) |
 | E-1 ou E-2 ouvert avant `VERDICT-BBIS` ; un fichier ou dossier de la liste « jamais ouverts » ouvert ; une entrée `direction0_*` ou `direction1_*` de E-1 décodée ; un contenu de la branche des données autre que E-1, E-2 et leurs compagnons téléchargé ; un champ de E-2 hors de la liste blanche gardé, imprimé ou écrit (la régularisation de `enc.reglage` comprise) ; une ligne de registre lue hors des clés nommées | lecture invalide ; nœud |
-| empreinte de E-1 différente de son compagnon, de `fichier_sondes.sha256` ou de la ligne de registre ; empreinte de E-2 différente de son compagnon ou de la ligne de registre | arrêt (R11) |
+| empreinte de E-1 différente de son compagnon ou de `fichier_sondes.sha256` ; empreinte de E-2 différente de son compagnon ou de la ligne `SCORES-BBIS` | arrêt (R11) |
 | nom d'entrée de E-1 ou de champ de E-2 différent de ceux de ce texte ; `enc.reglage` d'une autre forme ; empreinte d'une sonde recalculée différente de `empreinte_sonde` ou de `enc.empreinte` ; couche hors de {7, 15, 23} ; famille hors de {lineaire, attention} ; agrégation différente de celle de la famille ; cellule ou pli manquant | arrêt : forme mal comprise ; nœud |
-| sonde marquée `echec` (sonde apprise ou lecteur honnête) | cette sonde « non lue : échec à l'apprentissage », sans arrêt |
+| sonde apprise marquée `echec` ; lecteur honnête marqué `enc.echec` ; toute autre absence de champ ou d'entrée | sonde apprise marquée `echec` : elle et son lecteur honnête, non appris, sont « non lus », sans arrêt ; lecteur honnête marqué `enc.echec` : « non lu », sans arrêt ; toute autre absence de champ ou d'entrée : arrêt (ligne « forme mal comprise ») |
 | matrice lue d'un autre indice que la couche de la sonde | arrêt |
-| garde de la fonction de lecture (plan, point 5) : écart sur le cas sain, ou moins de 32 colonnes sur 64 différentes sur l'artefact | arrêt avant tout calcul |
+| garde de la fonction de lecture (plan, point 5) : écart sur le cas sain, ou moins de 32 colonnes sur 64 différentes sur l'artefact de la lentille (publique : matrice d'une autre couche ; logits : permutation) | arrêt avant tout calcul |
 | garde du rapport à ε (plan, point 6) : minimum < 100 pour une (couche, lentille) | sans arrêt : nuls isotropes refaits par direction, « non tenue » écrit (phrase de tête) |
 | calibration (plan, point 6) : compte hors de [q_bas, q_haut] pour une (couche, lentille, nul) | tables de cette couche, de cette lentille et de ce nul « non calculables », motif écrit, sans arrêt du reste |
 | valeur non finie dans une lecture ou un nul | arrêt |
 | tables ouvertes par une personne avant `VERDICT-BBIS` scellée ; une table ou une phrase de ce texte transmise au lecteur du verdict de l'apprentissage des sondes sur la tâche, de l'étape B, de la table conjointe ou de P3-bis avant leurs verdicts scellés | lecture invalide ; nœud |
 | clé de ce texte écrite dans `registres/scellements-v1.md` (la garde de T0.7 y refuse toute clé inconnue ; T, « Liste d'arrêt ») | arrêt de l'écriture ; ligne retirée par la mère, déclaré |
-| lentille publique absente, illisible ou d'une autre empreinte | « non lue : lentille absente » ; jamais remplacée par une autre lentille (aucun repli silencieux, R5) |
+| lentille publique absente, illisible, ou d'une autre taille ou d'une autre empreinte que ce texte | arrêt ; message à la mère ; jamais remplacée par une autre lentille ; la lecture par la seule lentille des logits n'est pas rendue |
 | toute envie d'écart à ce texte | écrite, datée, version neuve (R12), contre-lue, avant d'être faite |
 | tout refus d'une permission, du crochet ou du classifieur | ni rejoué, ni reformulé, ni contourné ; arrêt ; nœud |
 
@@ -511,13 +566,14 @@
 - **Lecteur neuf** : n'a lu aucun résultat de l'apprentissage des sondes sur la tâche (score, aire, issue, verdict), ni des autres
   chaînes interdites ; ni auteur, développeur ou opérateur, ni lecteur d'aucun verdict nommé ici ; lit ce texte, les tables fermées et
   la ligne du verdict d'ensemble de la tranche des lentilles publiques ; décrit selon les « Critères de lecture gelés ».
-- **Machine** : le processeur du conteneur d'une session (au relevé de l'auteur : 4 fils, 15 Go de mémoire, ≈ 7 Go libres sur un
-  disque partagé) ; aucune carte graphique ; mémoire de pointe estimée ≤ 6 Go (W_U gardé en simple précision 1,47 Go ; scores nuls d'un
+- **Machine** : le processeur du conteneur d'une session neuve (N9 tranché, option (a)) ; au relevé de l'auteur, dans son propre
+  conteneur : 4 fils, 15 Go de mémoire, ≈ 7 Go libres sur un disque partagé ; ces relevés et les versions sont refaits au montage
+  dans la session neuve ; aucune carte graphique ; mémoire de pointe estimée ≤ 6 Go (W_U gardé en simple précision 1,47 Go ; scores nuls d'un
   vecteur, 2 000 × 89 498 en simple précision, 0,72 Go ; les 31 matrices de la lentille en demi-précision, 1,04 Go, le temps de leur
   contrôle).
 - **Coût : 0 USD** (aucune location, aucune interface payante). **Durée** (estimation de l'auteur) : téléchargements ≈ 17,1 Go de poids
   et de lentille lus en flux (plus le corpus des jetons gardés), ≈ 5 à 30 min selon le débit, pire ≈ 2 h ; corpus et comptes de jetons
-  ≈ 15 à 45 min, pire ≈ 2 h ; gardes et essais < 15 min ; calcul ≈ 20 à 45 min (dont ≈ 7 à 13 min de produits au débit du banc), pire
+  ≈ 15 à 45 min, pire ≈ 2 h ; gardes et essais < 15 min ; calcul ≈ 20 à 45 min (dont ≈ 7 à 14 min de produits au débit du banc), pire
   ≈ 2 h ; **total ≈ 1 à 2 h, pire ≈ 6 h** ; arrêt à 8 h (« Liste d'arrêt »). Lecture humaine : 0 USD.
 
 ## Frontière : ce que ce texte ne dit pas
@@ -528,7 +584,7 @@
 3. **Convention de lecture** : une sonde lit `w·h` ; la lentille décrit l'effet d'un vecteur **écrit** dans le flux. Ce texte applique la
    lentille aux coordonnées brutes de `w` (et de `q`), normalisation repliée (les coordonnées de faible écart type y pèsent beaucoup,
    celles des dimensions à très forte activité presque rien), **comme si `w` était écrit dans le flux** : c'est une convention de
-   description, non une mesure de ce que la sonde lit. La description de ce que la sonde lit demanderait une lentille côté entrée,
+   description, non une mesure de ce que la sonde lit. La description par la direction transposée n'est pas faite. La description de ce que la sonde lit demanderait une lentille côté entrée,
    absente (point 7). Le nul isotrope ignore l'anisotropie du repliement ; seul le nul des signes la garde.
 4. Une liste de jetons dit ce que la lentille associe à une direction (ce qu'elle « pousse en moyenne »), non ce que la sonde emploie
    sur un épisode, ni un rôle causal ; aux couches 7 et 15, sous les deux tiers de la profondeur, G attend que la lecture prédise mal ce
@@ -548,7 +604,7 @@
     n'est pas lue).
 11. Rien sur les sondes de l'ordre 2, les sondes du nul de réétiquetage, les directions du plancher : non lues.
 12. Rien d'un autre modèle, d'un autre mode de sabotage, ni d'une autre couche que 7, 15 et 23 ; rien des lentilles J et J++ publiques
-    (non lues, nœud N10).
+    (non lues, N10 tranché, option (a), « Nœuds »).
 
 ## Données gardées et plan de stockage
 
@@ -571,8 +627,8 @@
 `| clé | AAAA-MM-JJTHH:MM:SSZ | chemin | sha256 |`, lignes ajoutées, jamais réécrites. Clés : `SCELLEMENT-LENTILLES-BBIS` (version
 scellée de ce texte), `ABSENCE-VERDICT-LENTILLES-BBIS`, `GO-LENTILLES-BBIS` (extrait de GO-2026-11-18-42), `CODE-LENTILLES-BBIS`,
 `MONTAGE-LENTILLES-BBIS`, `ENTREES-LENTILLES-BBIS`, `TABLES-LENTILLES-BBIS`, `OUVERTURE-LENTILLES-BBIS`, `LECTURE-LENTILLES-BBIS`. Lues,
-jamais écrites : `SCORES-BBIS` et `VERDICT-BBIS` (registre propre de l'apprentissage des sondes sur la tâche ; clés, heures et chemins
-seulement). **Jamais** `registres/scellements-v1.md`.
+jamais écrites : `SCORES-BBIS`, `VERDICT-BBIS` et `CODE-BBIS` (registre propre de l'apprentissage des sondes sur la tâche ; clés,
+heures et chemins seulement ; pour `CODE-BBIS`, le commit aussi). **Jamais** `registres/scellements-v1.md`.
 
 ## Code neuf (à écrire sans aucune vue des données, contre-lire, éprouver ; R5)
 
@@ -590,19 +646,25 @@
     arrêt « forme mal comprise ») ; E-1 clé par clé (lecture des seules entrées `sonde_*` et `enc_*` d'une archive jouet qui porte aussi
     des entrées `direction0_*` : ces dernières jamais décodées ; demande d'une entrée `direction*` : refus ; nom d'entrée inconnu :
     arrêt) ; ouverture avant `VERDICT-BBIS` (refus) ; empreinte d'une sonde (un poids altéré : arrêt ; nom du lecteur honnête mal
-    reconstruit : arrêt) ; couche, famille ou agrégation hors de l'ensemble ; ouvrir un fichier de scores : refus ;
+    reconstruit : arrêt) ; couche, famille ou agrégation hors de l'ensemble ; ouvrir un fichier de scores : refus ; un fichier jouet par forme (a), (b), (c)
+    d'« Attendu » (cas sains) ; `enc` absent sans `echec`, entrée `enc_w` présente alors que `enc.echec` existe, `sonde_q` absente pour la
+    famille `attention` (artefacts : arrêt) ; empreintes de E-1 et de E-2 contre leurs compagnons (un octet changé : arrêt) ; lignes de
+    registre (`SCORES-BBIS` absente ou multiple ; `SCELLEMENT-`, `GO-` ou `CODE-LENTILLES-BBIS` absente : refus) ;
   - **montage** : clé absente ou vide (arrêt, sans impression) ; essai d'un octet refusé (hôte simulé : arrêt) ; lecture en flux (un
     octet changé dans un faux fichier `safetensors` : arrêt ; tenseurs extraits égaux à ceux d'un chargement entier) ; pointeur
     (identifiant git faux : arrêt) ; licence (fichier altéré d'un octet : arrêt) ; lentille (disposition fausse ; `provenance` absente ou
     sans point de capture ; point de capture faux ; matrice identité ; deux matrices égales par permutation d'un fichier jouet : arrêt) ;
-    jetons gardés (liste altérée d'un jeton : arrêt) ; mode de débogage activé : arrêt ;
-  - **lecture** : fonction de lecture (64 colonnes ; matrice d'une autre couche : au moins 32 différentes) ; **indice de couche** (fausse
+    jetons gardés (liste altérée d'un jeton : arrêt) ; mode de débogage activé : arrêt ; comparaison de `readout.py` à la copie
+    versée (copie jouet altérée dans `read` : arrêt) ; lentille absente (arrêt, message, aucune lecture rendue par la seule lentille des
+    logits) ;
+  - **lecture** : fonction de lecture (64 colonnes ; sur la fausse lentille, les deux artefacts : matrice de la couche suivante pour
+    la lentille publique, permutation des coordonnées pour la lentille des logits : au moins 32 différentes chacun) ; **indice de couche** (fausse
     lentille dont la matrice ℓ porte une signature propre, J_ℓ = I + ℓ·10⁻²·E, E fixe : la lecture d'une sonde de couche ℓ rend la
     signature ℓ ; un décalage d'un cran introduit dans le code : arrêt) ; **rapport à ε** (avec J = I : v de norme 10⁻⁴, artefact,
-    lève la garde et impose les nuls par direction ; v de moyenne quadratique 1, cas sain, ne la lève pas) ; imparité (a_t(−v) = −a_t(v)) ;
+    lève la garde et impose les nuls par direction ; v de moyenne quadratique 1, cas sain, ne la lève pas ; au bord, ρ = 99 lève, ρ = 101 ne lève pas) ; imparité (a_t(−v) = −a_t(v)) ;
   - **nuls et statistiques** : graines reproductibles ; même norme ; nul des signes de mêmes valeurs absolues ; calibration (nul sain :
-    dans les bornes ; chemin des directions réelles faussé, par exemple autre précision ou autre ε : hors des bornes ; bornes
-    binomiales recalculées égales aux exemples du plan) ; familles (vocabulaire jouet) ; jeton de début (rang rapporté) ; symétrie des
+    dans les bornes ; scores des témoins multipliés par 1,5 : hors des bornes ; bornes
+    recalculées égales aux exemples du plan) ; familles (vocabulaire jouet) ; jeton de début (rang rapporté) ; symétrie des
     pôles (v et −v) ; valeurs non finies ;
   - **procédure** : horloge simulée au-delà de 8 h : arrêt ; espace disque (seuil simulé : arrêt) ; clé (aucune occurrence de sa valeur
     dans les fichiers écrits, essai sur une fausse clé) ; clé de ce texte dans `registres/scellements-v1.md` (refus) ; une phrase par
@@ -618,18 +680,16 @@
   mère (R-3334), repris tels quels.
 - **N2** (lentilles à ré-ajuster) et **N7** (dépense de la machine louée) : **sans objet**.
 
-**Ouverts (à trancher avant le scellement de la version)** ; la contre-lecture 1 juge que le texte tient avec chaque recommandation :
-- **N8 — clé d'accès au modèle dans le conteneur.** Enjeu : les poids de Llama sont derrière une porte ; R-3151 exige le mot de Lazar
-  pour passer une clé à une machine. Ici la clé est déjà dans l'environnement de la session (`HF_TOKEN`) et ne quitte pas le conteneur.
-  Options : (a) tenu pour couvert par GO-2026-11-18-42 (l'option (d) du brouillon 1 nommait « la clé dans le conteneur »), relevé par la
-  mère dans `GO-LENTILLES-BBIS` ; (b) mot exprès de Lazar avant le montage. Recommandation : (a), confiance 0,7. Garde-fous ajoutés au
-  brouillon 3 : essai d'un octet avant tout flux, clé absente ou vide testée sans impression, modes de débogage interdits.
-- **N9 — session du calcul.** Options : (a) **session neuve** dont le conteneur ne porte aucun dossier de course ; (b) le conteneur de la
-  mère, dans un dossier neuf, avec l'interdit écrit. Recommandation : (a), confiance 0,7. Dans les deux cas, l'opérateur ne lit des
-  registres que les clés et heures nommées en E-3.
-- **N10 — lentilles J et J++ publiques.** Options : (a) non lues (moins de lectures ; la lentille R se présente comme une J plus fidèle
-  aux couches basses, selon le titre de sa méthode) ; (b) lues aussi, en rapport sans libellé. Recommandation : (a), confiance 0,6.
-  Conséquence écrite (« Frontière », point 6) : aucune robustesse d'une lentille ajustée à l'autre n'est mesurée.
+**Tranchés par anticipation, option (a) chacun** — recommandation du rédacteur, jugée tenable par la contre-lecture 1, appliquée par
+anticipation par la session mère (autonomie GO-2026-11-18-26), portée à Lazar (R-3372) :
+- **N8 — clé d'accès au modèle** : option (a) : la clé est lue par son nom (`HF_TOKEN`) dans le conteneur de la session du calcul,
+  couverte par GO-2026-11-18-42, relevée par la mère dans `GO-LENTILLES-BBIS` ; la session neuve reçoit la clé de la configuration de
+  son environnement, jamais de la session mère ni d'une autre session (ni message, ni fichier, ni argument) ; clé absente : arrêt, nœud.
+  Garde-fous : essai d'un octet avant tout flux, clé absente ou vide testée sans impression, modes de débogage interdits (plan, point 4).
+- **N9 — session du calcul** : option (a) : session neuve dont le conteneur ne porte aucun dossier de course ; l'opérateur ne lit des
+  registres que les clés et heures nommées en E-3 ; les relevés de machine de l'auteur sont refaits au montage.
+- **N10 — lentilles J et J++ publiques** : option (a) : non lues ; conséquence écrite (« Frontière », point 6) : aucune robustesse d'une
+  lentille ajustée à l'autre n'est mesurée.
 
 ## Contre-lecture
 
@@ -641,14 +701,19 @@
   `prereg/contre-lectures/lecture-sondes-bbis-par-lentilles-v1-brouillon2-cl1.md`,
   `f876f83a250dce85d83ab6e73f8ec0d40ffbc33640d625962838f774e3b94ea2`. Verdict : « scellable après corrections » ; aucune échappatoire ;
   un bloquant, quatre majeurs, onze mineurs, traités ci-dessous.
-- **Vérification des corrections** (ce brouillon 3) : à commander par la mère à un agent neuf qui n'a écrit aucune pièce nommée ici ;
-  fichiers à lui donner : ce brouillon, le brouillon 2, le rapport de la contre-lecture 1, le code de `src/controle_ia/t07bbis/` cité en
-  « Documents », et les pièces de la contre-lecture 1 ; mêmes interdits (rien sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ;
-  aucune branche `calcul/` ou `donnees/` ; aucun fichier de `registres/` ; le dossier `docs/notes/lentilles-sondes-p3-v1/` ; les
-  dossiers de course des conteneurs ; aucune sortie ni aucun résultat des chaînes nommées). Entrée numérotée ajoutée quand son rapport
-  existe.
+- **Contre-lecture 2 (vérification des corrections)** : sous-agent neuf, modèle Fable 5.2 (`claude-fable-5-2`) ; n'a écrit ni ce texte,
+  ni sa contre-lecture, ni aucune pièce de l'apprentissage des sondes sur la tâche ou des tranches de la lecture par lentille
+  neuronale ; ne sera ni développeur, ni opérateur, ni lecteur du texte. Mandat :
+  `docs/notes/neuron-lens-v1/mandat-verification-corrections-texte-lentille-publique-v1.md`,
+  `71dbd76ab3d277d10e4e4fa8ec6c8dc42bc8b8ecab1160b442b024d5a266fc34`. Brouillon relu : brouillon 3,
+  `prereg/lecture-sondes-bbis-par-lentilles-v1-brouillon3.md`, `49b0921d585944fd1e326bdea6155ad67e64719d6ab2673a022f415f084f256a`.
+  Rapport : `prereg/contre-lectures/lecture-sondes-bbis-par-lentilles-v1-brouillon3-verif1.md`,
+  `5398f2e90f2dac1b5243601f89d609fb3c2a24773126b3391cfdab8953d5aedc` (compagnon vérifié). Verdict : « scellable après corrections » ;
+  un bloquant, trois majeurs, treize mineurs, traités dans « Traitement des remarques de la vérification 1 ». Pour des couples
+  appliqués tels quels, le rapport demande un contrôle de la seule différence brouillon 3 → version : liste et sortie de `diff` dans
+  `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v1.md`.
 
-### Traitement des remarques de la contre-lecture 1
+### Traitement des remarques de la contre-lecture 1 (tient lieu de « Changements du brouillon 2 au brouillon 3 »)
 
 | remarque | traitement | où |
 |---|---|---|
@@ -669,14 +734,57 @@
 | m10 borne basse de calibration | **fait** : comptes mis en commun par (couche, lentille, nul), 1 000 témoins par couche pour le nul isotrope, bornes binomiales à 10⁻⁴ par côté, calculées par une règle ; borne basse déclarée lâche sous n = 600 | Plan (6) ; Liste d'arrêt ; Code neuf |
 | m11 familles en anglais | **fait** : écrit comme choix (aucune famille en français) ; la langue des textes de la tâche est reprise de la contre-lecture, non vérifiée par l'auteur | Métrique (6) |
 | réserve « p non indépendants » | **fait** : écrit | Métrique (9) |
-| N8 (jeton absent ou factice ; débogage) | **fait** : garde-fous ajoutés ; le nœud reste ouvert (décision de la mère ou de Lazar) | Plan (4) ; Liste d'arrêt ; Nœuds |
-| N9 (registres lus par l'opérateur) | **fait** : clés et heures nommées seulement ; le nœud reste ouvert | Entrées (E-3) ; Qui ; Nœuds |
-| N10 (conséquence d'une seule lentille ajustée) | **fait** : écrit dans la frontière ; le nœud reste ouvert | Frontière (6) ; Nœuds |
+| N8 (jeton absent ou factice ; débogage) | **fait** : garde-fous ajoutés ; tranché ensuite, option (a) (« Nœuds ») | Plan (4) ; Liste d'arrêt ; Nœuds |
+| N9 (registres lus par l'opérateur) | **fait** : clés et heures nommées seulement ; tranché ensuite, option (a) (« Nœuds ») | Entrées (E-3) ; Qui ; Nœuds |
+| N10 (conséquence d'une seule lentille ajustée) | **fait** : écrit dans la frontière ; tranché ensuite, option (a) (« Nœuds ») | Frontière (6) ; Nœuds |
+
+**Remarque non faite** : aucune. Effets de bord déclarés au brouillon 3 : nombre de lectures porté à ≈ 195 000 (témoins du nul
+isotrope) ; durée de calcul au pire ≈ 13 min de produits si la garde du rapport à ε impose les nuls par direction (valeur du
+brouillon 3 ; dans la version, ≈ 14 min, après le couple V-M2 de la vérification 1 : plan, point 6), dans la marge de 8 h.
 
-**Remarque non faite** : aucune. Effets de bord déclarés : nombre de lectures porté à ≈ 195 000 (témoins du nul isotrope) ; durée de
-calcul au pire ≈ 13 min de produits si la garde du rapport à ε impose les nuls par direction, dans la marge de 8 h.
+### Traitement des remarques de la vérification 1
 
-- **État au validateur** (`prereg.problemes`) : aucun manque attendu (l'entrée « Contre-lecture 1 » porte ses deux empreintes).
+| remarque | traitement | où |
+|---|---|---|
+| **V-B1** artefact de la garde de lecture sans effet pour la lentille des logits | **appliqué tel quel** : artefact défini par lentille (couche suivante 7 → 15 → 23 → 7 pour la lentille publique ; permutation des coordonnées tirée par graine pour la lentille des logits) ; ligne d'arrêt et essais complétés | Plan (5) ; Liste d'arrêt ; Code neuf |
+| **V-M1** formes en cas d'échec non écrites | **appliqué tel quel** : formes (a), (b), (c), seules admises ; ligne d'arrêt remplacée, mise en forme dans les deux colonnes de la table (conditions à gauche, mots du couple à droite) ; essais ajoutés | Entrées (« Attendu ») ; Liste d'arrêt ; Code neuf |
+| **V-M2** repli de la garde du rapport à ε incomplet | **appliqué tel quel** (correction principale : repli pour les deux lentilles de la couche, appariement du point 9 gardé) ; clé des témoins ajoutée au point 3 | Plan (3, 6) |
+| **V-M3** loi du compte de calibration | **appliqué tel quel** (correction principale : loi bêta-binomiale exacte) ; les quatre exemples, recalculés par le rédacteur sous la loi exacte, sont égaux (script `bornes_calibration_beta_binomiale_v1.py` et sa sortie, scellés, dans `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/`) ; « binomiales » retiré des essais | Plan (6) ; Code neuf |
+| V-m1 empreinte de E-1 sans ligne de registre | appliqué tel quel | Liste d'arrêt |
+| V-m2 clé `CODE-BBIS` | appliqué tel quel (première option : clé ajoutée aux clés lues) | Entrées (E-3) ; Lignes de registre |
+| V-m3 valeurs exactes | appliqué tel quel : `max` ; `dispersion_ordres_calcul` ; `doses`, `couches`, `plis`, `manifeste`, `duree_s` nommées parmi les exclues | Entrées (E-2) |
+| V-m4 « lisible » | appliqué tel quel | Plan (4) |
+| V-m5 témoin de l'indice de couche | appliqué tel quel | Plan (6) |
+| V-m6 deux lignes contradictoires | appliqué : une seule ligne porte la lentille d'une autre empreinte, avec l'action du couple ; pour qu'il n'en reste qu'une, la lentille est retirée de la ligne « SHA-256 ou taille… » et sa taille passe dans la ligne de la lentille | Liste d'arrêt |
+| V-m7 deux phrases ; exception à la règle | appliqué tel quel | Frontière (3) ; Critères (règles) |
+| V-m8 clé des témoins | appliqué tel quel ; la parenthèse du nul isotrope partagé (un seul jeu par couche) est accordée à la forme neuve de la clé : `<cellule>/<pli>/<rôle>/<vecteur>` y est remplacé par `couche` | Plan (3) |
+| V-m9 « au rang près » | appliqué tel quel, au cas sain | Plan (5) |
+| V-m10 essais manquants ; artefact de calibration | appliqué : essais nommés de la comparaison de `readout.py`, des lignes de registre, des empreintes de E-1 et E-2, de la lentille absente, du bord de la garde du rapport à ε ; artefact de calibration : « scores des témoins multipliés par 1,5 », retenu parmi les deux que propose le couple, parce que la matrice d'une autre couche ne change rien pour la lentille des logits (même défaut que V-B1) | Code neuf |
+| V-m11 exposition de qui écrit les dernières corrections | appliqué : déclaration de la session mère et du rédacteur | Ce que l'auteur savait ; Statut |
+| V-m12 clé d'une session neuve ; relevés de machine | appliqué tel quel | Plan (4) ; Qui ; Nœuds (N8, N9) |
+| V-m13 langue appuyée sur le code | appliqué tel quel ; empreinte et lignes de `plis_v1.py` vérifiées par le rédacteur | Métrique (6) |
+| « pour mémoire » : signe + de la requête `q` | **non appliqué** : hors des couples (le rapport le place hors de la différence, sans couple) ; signalé à la mère | — |
+| « version finale », point 2 : entrée numérotée | fait : « Contre-lecture 2 (vérification des corrections) » ; alinéa « à commander par la mère » retiré | Contre-lecture |
+| point 3 : trois points ouverts | fait : N8, N9, N10 tranchés, option (a), avec la mention ; lieux accordés : titre du bloc, plan, point 4 (deux mentions), « Frontière », point 12, « Machine », trois lignes du tableau de la contre-lecture 1 | Nœuds ; Plan (4) ; Frontière (12) ; Qui ; Contre-lecture |
+| point 4 : déclaration de la mère | fait | Ce que l'auteur savait |
+| point 5 : marqueurs | fait : titre, nom de fichier, Statut, Date, Auteur, Documents (brouillon 3, rapport, mandat ; empreintes du code inchangées), validateur rejoué, section « Changements du brouillon 3 à la version » ; le tableau de la contre-lecture 1 tient lieu des changements du brouillon 2 au brouillon 3 | en-tête ; Contre-lecture ; Changements |
+| point 6 : ordre du scellement | fait, écrit tel que le rapport le dit | Statut |
+
+**Couples non appliqués tels quels** : V-M1 (mise en forme dans la table), V-m6 (une ligne retirée pour n'en garder qu'une), V-m8
+(parenthèse accordée), V-m10 (un artefact choisi parmi deux) : raisons ci-dessus. **Écart signalé, puis corrigé**
+(hors des couples) : l'« ordre de grandeur » du plan, point 6, et « Qui, quelle machine » ne suivaient pas le coût neuf de V-M2 (≈ 7 min
+de plus au lieu de ≈ 6) ; signalé par le rédacteur, l'écart a été corrigé par les changements 43 et 44 du fichier des différences, à la
+demande de la session mère : « ≈ 14 min » et « ≈ 7 à 14 min » ; sans effet sur l'arrêt à 8 h.
+
+- **État au validateur** (`prereg.problemes`), rejoué sur cette version : liste vide (aucun manque ; les entrées
+  « Contre-lecture 1 » et « Contre-lecture 2 » portent chacune leurs deux empreintes).
+
+## Changements du brouillon 3 à la version
+
+Application des couples avant → après du rapport de la vérification 1 (V-B1, V-M1 à V-M3, V-m1 à V-m13), des trois options (a) (N8,
+N9, N10) et des marqueurs de version, rien d'autre (« Déclaration de la session mère ») ; détail ligne par ligne, rattaché à chaque
+remarque, et sortie de `diff` : `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v1.md` ;
+traitement : « Traitement des remarques de la vérification 1 ».
 
 ## Changements du brouillon 1 au brouillon 2
 
```
