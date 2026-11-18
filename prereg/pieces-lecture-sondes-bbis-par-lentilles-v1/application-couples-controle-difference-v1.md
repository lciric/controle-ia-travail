# Application, par la session mère, des trois couples exacts du contrôle de la différence — v1

Écrit par la session mère `session_013QMayjsoZJFBUCqcnvD5h1` le 2026-11-18T19:05:20Z (heure relevée par `date -u`), juste avant le scellement du texte `prereg/lecture-sondes-bbis-par-lentilles-v1.md`.

- Texte candidat contrôlé : empreinte `001fd5c0ee431dfaf9ec83c2d803dceed3d85be3fbf8bbb0360d6009dea268ff` (celle que portent le fichier des différences v3, `fe3122a9f0a95803243f95d3b5e7dc685b138abc2577be4b0ca75237733f5e04`, et le rapport de contrôle).
- Rapport du contrôle de la différence (agent neuf, Sonnet 5.5) : `prereg/contre-lectures/lecture-sondes-bbis-par-lentilles-v1-controle-difference-v1.md`, `f34d1cc1aa3f2473a9bb1fb04dfc77d2f67bcdafdc88e83e78a57b04b3de6378` ; verdict : « à sceller après ces couples exacts » (trois couples ; aucune échappatoire neuve).
- Geste de la mère : les trois couples ont été **extraits par programme du rapport scellé** (blocs « Avant » et « Après » de sa section « Couples exacts ») et appliqués par remplacement exact ; chaque passage d'origine apparaissait une fois et une seule. La mère n'a rien écrit d'elle-même dans le texte. Les couples portent sur la déclaration de la session mère (les quatre accords de durée y sont nommés) et sur deux renvois au fichier des différences (v3 au lieu de v1) ; aucun ne touche une mesure, un seuil, une garde ni un choix d'analyse.
- Texte après les trois couples : empreinte `ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572` ; validateur (`controle_ia.prereg.problemes`) rejoué : liste vide.
- Changements du brouillon 3 à la version scellée : les 46 changements du fichier des différences v3, plus ces trois couples (47 à 49). Rien d'autre.

## Sortie de `diff -u` entre le texte candidat contrôlé et le texte à sceller

```diff
--- candidat-controle-001fd5c0
+++ texte-a-sceller-ca5066d7
@@ -123,7 +123,9 @@
 - **Déclaration de la session mère** (vérification 1, V-m11 et « ce que la version finale doit porter », point 4) : la session mère est
   exposée à un résultat du programme (le verdict du barreau « accumulation des scores sur l'épisode », R-3347) et à aucune sortie de
   l'étape B bis ; elle n'a fixé aucun seuil, critère ni choix d'analyse de ce texte ; les changements du brouillon 3 à la version sont
-  l'application des couples du rapport de vérification et des trois options (a), rien d'autre. Le rédacteur, qui a écrit ces
+  l'application des couples du rapport de vérification, des trois options (a) et des marqueurs de version, plus quatre accords de
+  durée (plan, point 6 ; « Qui, quelle machine » ; deux passages de « Contre-lecture ») que la session mère a demandés pour que les
+  durées suivent le couple sur le repli de la garde du rapport à ε, rien d'autre. Le rédacteur, qui a écrit ces
   changements, n'a lu aucun résultat du programme (ci-dessus).
 
 ## Vocabulaire (noms en clair ; les identifiants viennent en appui)
@@ -711,7 +713,7 @@
   `5398f2e90f2dac1b5243601f89d609fb3c2a24773126b3391cfdab8953d5aedc` (compagnon vérifié). Verdict : « scellable après corrections » ;
   un bloquant, trois majeurs, treize mineurs, traités dans « Traitement des remarques de la vérification 1 ». Pour des couples
   appliqués tels quels, le rapport demande un contrôle de la seule différence brouillon 3 → version : liste et sortie de `diff` dans
-  `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v1.md`.
+  `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v3.md`.
 
 ### Traitement des remarques de la contre-lecture 1 (tient lieu de « Changements du brouillon 2 au brouillon 3 »)
 
@@ -782,9 +784,10 @@
 ## Changements du brouillon 3 à la version
 
 Application des couples avant → après du rapport de la vérification 1 (V-B1, V-M1 à V-M3, V-m1 à V-m13), des trois options (a) (N8,
-N9, N10) et des marqueurs de version, rien d'autre (« Déclaration de la session mère ») ; détail ligne par ligne, rattaché à chaque
-remarque, et sortie de `diff` : `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v1.md` ;
-traitement : « Traitement des remarques de la vérification 1 ».
+N9, N10), des marqueurs de version et de quatre accords de durée demandés par la session mère (changements 43 à 46), rien d'autre
+(« Déclaration de la session mère ») ; détail ligne par ligne, rattaché à chaque remarque, et sortie de `diff` :
+`prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/differences-brouillon3-vers-version-v3.md` ; traitement : « Traitement des
+remarques de la vérification 1 ».
 
 ## Changements du brouillon 1 au brouillon 2
 
```
