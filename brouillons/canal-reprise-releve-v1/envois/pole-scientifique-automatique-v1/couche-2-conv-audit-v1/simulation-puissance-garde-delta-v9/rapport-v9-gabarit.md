# Puissance de la garde appariée δ dans la fiche — v9 : table de lecture en ρ̂ mesuré, neuvième comparateur en n_h, corrections de la contre-lecture GD8 — rapport v9

Lignée conv-audit, {{DATE}} (heure de construction du rapport). **Corrige la v8** (`rapport-puissance-garde-delta-v8.md`, gardée, règle R12) selon la contre-lecture GD8
(`entrees-gd8/contre-lecture-gd8-v1.md`, copiée d'`origin/main` avec ses scripts, empreintes identiques), constats GD8-01 à GD8-09. **Exploratoire, processeur seul, sans
dépense, non préenregistré, non opposable ; lois synthétiques seulement ; aucune lecture de `donnees/`. Non relu par une autre main (règle R2) : contre-lecture à demander.**
Fixer une taille, un seuil, un repli ou le sort du neuvième comparateur est un nœud de décision de Lazar ; ce rapport propose.

Vocabulaire (inchangé depuis la v8) : « fiche » : minimum des 8 gardes (honnêtes) et des 8 contrastes (sabotés) ; « seuil 40 » : lecture (A), deux modes, fiche retenue par la
**règle de Benjamini-Hochberg sur les e-valeurs (e-BH)** à budget α_c/2, α_c = 0,05 ; « seuil 160 » : référence stricte 8/α_c, atteinte par le minimum des 16 processus (borne
basse de la retenue à m = 8, non simulée) ; ρ : corrélation intra-unité (variance de la probabilité d'unité / p(1 − p)), ρ_A pour le sujet, ρ_B pour les comparateurs ;
« pire » : au pire des quatre cellules K_h ∈ {10 ; 5} × biais ∈ {0 ; δ/4} ; n80 (n90) : unités pour une puissance de 0,8 (0,9) ; n_h = max(288 ; plus petit multiple de 16
≥ 1,06 × n80 pire) ; ρ̂ : ρ **mesuré** au pilote côté sabotage (p ≈ 0,4, K = 10 épisodes par unité). « SUPPOSÉ » : scénario, non estimation. **Puissances arrondies au plus
proche à trois décimales (v9) ; erreur de Monte-Carlo ≈ 0,008 à 0,85 (2 000 répétitions) : ce ne sont ni des minorants ni des valeurs tronquées.** Paramètres communs :
k = 8 comparateurs, τ = 0,01, δ = 0,05, écart de contraste 0,10, K_s = 10, 2 000 répétitions, lecture (A) m = 2, lois en échelle bêta.

## Résumé pour Lazar (dix lignes)

1. **La table de lecture répond maintenant en ρ̂ mesuré**, marge de lecture incluse. Pilote de 288 unités, les deux hypothèses sur le sujet : ρ̂ = 0 → **288 / 304** unités (seuils 40 / 160) ; 0,05 → **288 / 352** ; 0,10 → **320 / 416** ; 0,17 → **416 / 544**.
2. **Hors table dès ρ̂ ≥ 0,18** (288 unités), 0,15 (100), 0,13 (50) ; avec la seule hypothèse ρ_A = ρ_B : dès 0,31, 0,29, 0,26.
3. **Tailles au ρ vrai ≠ tailles au ρ̂ lu** : 304 / 384 si ρ vrai = 0,17 (ρ_A = ρ_B), 384 / 496 si ρ_A = 2 ρ_B ; mais 416 / 544 si ρ̂ = 0,17 est lu sur 288 unités.
4. **Repli hors table : à toi de trancher (lié à G1, aucun défaut)** : A arrêt et nœud de décision ; B taille maximale de la grille (480 / 608) ; C restriction à ρ_A = ρ_B (si le sujet est en fait deux fois plus dispersé, la puissance tombe à 0,61–0,65). Je recommande A.
5. **Neuvième comparateur, écart 0,05 (SUPPOSÉ)** : n_h à neuf = **288 à 736** (seuil 40), **368 à 976** (seuil 160) ; écart des n_h **+0 à +432** et **+80 à +592**. À écart 0,10 : n_h inchangé (+16 au plus).
6. **Puissances clés, neuf graines** (ρ = 0,17) : 0,840 ± 0,003 et 0,506 ± 0,003 à 288 unités ; 0,980 ± 0,001 et 0,908 ± 0,002 à 400 (le 0,847 de la v8 était 2,9 erreurs types haut).
7. **n80 ajusté** à ± 0,4 à 2,3 unités ; la dichotomie s'en écarte de −4 à +12 ; n_h inchangé dans 24 cas sur 34.
8. **ρ honnête double (SUPPOSÉ)** : +16 unités au seuil 160 jusqu'à ρ = 0,10, **+64 à 0,17** (384 → 448) : condition de validité de la table.
9. **Strates** : « commune » = témoin de construction ; portée partielle +0,004 à +0,009 ; ne pas compter dessus. Écrêtage revérifié 16 / 16 au critère scellé d'avance.
10. Exploratoire, non opposable, non relu (R2). 8 passages de grille (script v8 scellé), 15 compléments (script v9), 0 échec de passage.

## Ce qui change par rapport à la v8

| constat | changement | où |
| --- | --- | --- |
| GD8-01 (majeure) | grille prolongée (ρ_A = ρ_B jusqu'à 0,35 ; ρ_A = 2 ρ_B jusqu'à ρ_B = 0,20) : 8 passages neufs ; table **au ρ vrai** et table **en ρ̂ lu** (pilotes de 50, 100, 288 unités, marge 1,645 σ incluse), règle définie partout, « hors table » nommé ; trois options de repli chiffrées, sans défaut | § 1 ; T1, T2, T8 |
| GD8-02 (majeure) | neuvième comparateur en **n_h à neuf comparateurs** et **écart des n_h** ; « surcoût » et « +128 sans dispersion » supprimés | § 2 ; T3 |
| GD8-04 | n80 par ajustement logistique (± écart-type) ; puissances clés en moyenne sur neuf graines (± erreur type) ; « minorant » et troncature retirés | § 3 ; T1, T4 |
| GD8-07 | option `--facteur-rho-honnetes` (refusée par défaut) ; 3 passages ρ honnête = 2 × ρ saboté | § 4 ; T5 |
| GD8-03 | portée « commune » présentée comme témoin de construction ; parts de variance ; **portée partielle** (γ_B = 0,5 γ_A, option nouvelle) : 4 passages ; règle des décalages fixés d'avance | § 5 ; T6, T7 |
| GD8-05 | trois des quatre sorties échouées retrouvées et versées ; vérification refaite au critère scindé **scellé avant exécution** ; convention d'écrêtage pour le préenregistrement | § 6 |
| GD8-06 | « SUPPOSÉ » à chaque écart 0,05 et à « honnêtes du neuvième inchangés » | § 7 |
| GD8-08 | fiche nulle + neuvième comparateur : refus nommé, essais sain et artefact | § 8 |
| GD8-09 | un manifeste par exécution pour chaque script auxiliaire ; commit lu par l'appelant et écrit partout | § 9 |

## 1. GD8-01 → table au ρ vrai, table en ρ̂ lu, phrases réécrites, repli hors table

- **Où** : passages neufs `simulation-puissance-garde-delta-v9-sortie-meme-rho0.125`, `-0.20`, `-0.30`, `-0.35` et `-double-rhoB0.10`, `-0.125`, `-0.17`, `-0.20` (ρ_A = 0,20 ;
  0,25 ; 0,34 ; 0,40), lancés par `lancer-passages-grille-v9.sh` avec **le script v8 scellé, inchangé** (mêmes options que les passages v8 : 2 000 répétitions, quatre cellules,
  tailles 288 à 650, dichotomie de n80 et n90 aux seuils 40 et 160 ; même code que les lignes v8, donc lignes comparables) ; précision de la lecture de ρ prolongée
  (`precision-rho-pilote-v9.py`, grille ρ ∈ {0 ; 0,05 ; 0,10 ; 0,125 ; 0,17 ; 0,20 ; 0,25 ; 0,30 ; 0,35 ; 0,40}, les 15 cellules communes à la v8 reproduites à l'identique) ;
  tables par `tableaux-v9.py` (T1, T2, T8).
- **Comment** : la règle de la v8 est gardée telle quelle et rendue définie partout : ρ_haut = max(ρ̂ ; 0) + 1,645 × σ(ρ̂), σ lu au plus petit ρ de la grille de précision
  au moins égal à ρ̂ ; dans chaque hypothèse sur le sujet (ρ_A = ρ_B ; ρ_A = 2 ρ_B), la ligne de T1 égale ou immédiatement supérieure à ρ_haut ; n_h = le plus grand des
  deux ; **si l'une des deux hypothèses n'a pas de ligne : « hors table »**, qui renvoie au repli (options ci-dessous, à trancher par Lazar).

### 1.1 Tailles au ρ vrai

{{TABLE:T1}}

Lecture : au ρ **vrai** (ρ_A = ρ_B), n_h = 288 / 304 (seuils 40 / 160) à ρ = 0,05, 288 / 336 à 0,10, 288 / 352 à 0,125, **304 / 384 à 0,17**, 336 / 432 à 0,20, 384 / 496 à 0,25,
448 / 544 à 0,30, 480 / 608 à 0,35. Sous ρ_A = 2 ρ_B : 288 / 368 à ρ_B = 0,10, 320 / 416 à 0,125, **384 / 496 à 0,17**, 416 / 544 à 0,20 (ρ_A = 0,40). La fiche pire à 400 unités passe sous 0,8 au
seuil 40 à ρ = 0,35 (0,673) et vaut 0,800 à 0,30 ; au seuil 160, dès ρ = 0,25 (0,694).

### 1.2 Tailles au ρ̂ lu au pilote

{{TABLE:T2-288}}

{{TABLE:T2-100}}

{{TABLE:T2-50}}

{{TABLE:T2-points}}

Lecture, pilote de 288 unités, **les deux hypothèses** (règle de la v8) : ρ̂ = 0 → **288 / 304** ; ρ̂ = 0,05 → **288 / 352** ; ρ̂ = 0,10 → **320 / 416** ; ρ̂ = 0,17 →
**416 / 544** (ligne 0,20 dans les deux hypothèses : 336 / 432 sous ρ_A = ρ_B, 416 / 544 sous ρ_A = 2 ρ_B). Le premier ρ̂ hors table est **0,18 pour un pilote de 288 unités**, 0,15 pour 100 unités, 0,13 pour 50 unités (contre 0,07, 0,06 et 0,04 avec la grille de la v8 : GD8). Avec la seule hypothèse ρ_A = ρ_B, la table répond jusqu'à ρ̂ = 0,30 (288 unités), 0,28 (100), 0,25 (50).

**Phrases réécrites (tailles au ρ vrai et au ρ̂ lu, séparées)** :
- « **304 / 384 si ρ vrai = 0,17** (ρ_A = ρ_B) ; **384 / 496 si ρ vrai = 0,17 et ρ_A = 2 ρ_B**. »
- « **Si ρ̂ = 0,17 est lu sur 288 unités**, ρ_haut = 0,200 : ligne 0,20 dans les deux hypothèses, **n_h = 416 / 544** (336 / 432 sous la seule hypothèse ρ_A = ρ_B) ; au-delà de ρ̂ = 0,17 (288 unités), hors table. »
- Vérification de la phrase proposée par GD8 (« 384 / 496 si ρ̂ = 0,17 sur 288 unités ») : **exacte sur la grille de la v8** (ligne suivante 0,25 sous ρ_A = ρ_B,
  hypothèse 2 sans ligne) ; **sur la grille v9**, la ligne 0,20 existe et l'hypothèse ρ_A = ρ_B seule donne **336 / 432** ; avec l'hypothèse ρ_A = 2 ρ_B prolongée à ρ_B = 0,20, la règle rend **416 / 544**. Les chiffres « 384 / 496 » ne sont donc plus ceux de la v9 ; ils restent la réponse de la grille v8.
- Les phrases de la v8 « n_h = 288 jusqu'à ρ_B = 0,10, 304 à 0,17 (384 au seuil 160), 384 à 0,25 (496) » (§ 0.2 et § 6.1 de la v8) sont des tailles **au ρ vrai sous ρ_A = ρ_B** ;
  elles sont remplacées par les deux listes ci-dessus.

### 1.3 Repli hors table — options (à trancher par Lazar ; question liée à la porte G1 : **aucun défaut**)

{{TABLE:T8}}

Quand ρ̂ tombe hors table, aucune ligne simulée ne garantit une puissance de 0,8 dans l'une des deux hypothèses. Trois options, chiffrées pour un pilote de 288 unités
(seuil de déclenchement : ρ̂ ≥ 0,18 ; 0,15 pour 100 unités ; 0,13 pour 50) :

| option | règle | avantage | inconvénient | chiffres |
| --- | --- | --- | --- | --- |
| **A. Arrêt et nœud de décision** | hors table : on n'entre pas en G1 ; on rend ρ̂, son σ et la table à Lazar, qui décide (prolonger la grille, changer de plan, abandonner) | aucune taille n'est prise sans puissance simulée ; prolonger la grille ne coûte que du processeur (≈ 12 minutes par ligne sur deux processeurs) | délai ; une décision de plus avant G1 ; un pilote très dispersé arrête le calendrier | déclenchement à ρ̂ ≥ 0,18 (288 unités) ; aucun épisode engagé |
| **B. Taille maximale de la grille** | hors table : n_h = la plus grande taille de la table, scellée d'avance | pas d'arrêt ; règle mécanique | la garantie ne vaut que jusqu'aux dernières lignes (ρ_A = ρ_B = 0,35 ; ρ_A = 2 ρ_B à ρ_B = 0,20) ; au-delà, puissance inconnue, peut-être très basse ; coût élevé même si ρ̂ dépasse à peine le seuil | **480 / 608** unités (seuils 40 / 160), soit 64 800 / 82 080 épisodes à K_h = 5 (86 400 / 109 440 à K_h = 10) |
| **C. Restriction à ρ_A = ρ_B** | on lit la seule hypothèse ρ_A = ρ_B (raison : f_A n'est pas lue avant G1, le sujet joue les mêmes unités que les comparateurs, rien n'indique qu'il soit deux fois plus dispersé ; l'hypothèse 2 n'était qu'une sensibilité) | la table répond jusqu'à ρ̂ = 0,30 (288 unités) ; tailles plus petites | si le monde est ρ_A = 2 ρ_B, la puissance à la taille lue tombe (T8) : 0,783 / 0,723 à ρ_B = 0,125, **0,649 / 0,607** à 0,17, 0,643 / 0,627 à 0,20 ; c'est une hypothèse de revendication qu'on ne vérifie pas avant G1 | hors table seulement à ρ̂ ≥ 0,31 ; à ρ̂ = 0,17 : 336 / 432 au lieu de 416 / 544 |

**Ma recommandation : A** (confiance moyenne). Hors table veut dire que la dispersion mesurée dépasse tout ce qui a été simulé ; B donnerait une taille sans garantie au moment
même où la dispersion est la plus forte, C achète des tailles plus petites au prix d'une hypothèse non vérifiable sur le sujet (T8 : jusqu'à −0,2 de puissance). A ne coûte
qu'un délai, et la grille peut être prolongée sur processeur avant de reprendre. **Pas de défaut : c'est à Lazar de trancher (question liée à la porte G1).**

## 2. GD8-02 → le neuvième comparateur en n_h à neuf comparateurs et en écart des n_h

- **Où** : `tableaux-v9.py`, bloc T3 (`neuvieme_n_h` dans `tableaux-v9-sortie.json`) ; ce rapport § 0, § 10 et phrase du § 11. **Supprimées** : la phrase de la v8 « pour garder 0,8 il
  faut, en plus de la taille à huit comparateurs, +128 (sans dispersion) … » et la colonne « surcoût ».
- **Comment** : la v8 appelait « surcoût » le **maximum, sur les quatre cellules, de la différence par cellule** n80(9) − n80(8) ; ce n'est ni l'écart des n80 pires ni l'écart
  des tailles à prévoir. La v9 donne, pour chaque loi, le n80 pire et le **n_h** à huit et à neuf comparateurs (même règle que la table de lecture, ligne par ligne, sans
  enveloppe), et leur **écart**. Chiffres lus dans les sorties v8 (aucun passage nouveau) ; ils retrouvent exactement ceux de GD8.

{{TABLE:T3}}

Lecture, **écart du neuvième 0,05 (SUPPOSÉ, « comparateur fort » ; côté honnête du neuvième inchangé : SUPPOSÉ)** :
- n_h à neuf comparateurs : **288 à 736 au seuil 40**, **368 à 976 au seuil 160** selon la dispersion ;
- écart des n_h : **+0 (sans dispersion) à +432 (ρ = 0,17) au seuil 40** ; **+80 à +592 au seuil 160**. Sans dispersion, n_h ne bouge pas au seuil 40 (288 → 288) alors que la
  fiche pire à 288 unités tombe à 0,866 : la taille plancher de 288 absorbe la perte, ce que le « +128 » de la v8 cachait.
- Le « +432 » de la v8 au seuil 40 à ρ = 0,17 coïncide par hasard avec l'écart des n_h ; au seuil 160 à ρ = 0,17, l'écart des n_h est **+592** (384 → 976), plus que le
  « +568 » de la v8.
- **Écart du neuvième 0,10 (comme les huit autres)** : n_h inchangé au seuil 40 pour toutes les lois ; au seuil 160, +16 en bêta σ = 1,0 (304 → 320), inchangé ailleurs.

## 3. GD8-04 → n80 par ajustement de la courbe de puissance ; puissances clés sur plusieurs graines ; ni « minorant » ni troncature

- **Où** : `tableaux-v9.py` (fonction `ajuster`, colonnes « n80 ajusté » de T1 et T5 ; bloc T4) ; passages `graine11-meme-rho0.17` à `graine18-meme-rho0.17` (script v9 final,
  `lancer-complements-v9.sh graines`).
- **n80 ajusté** : régression logistique binomiale logit P = a + b·n sur les points déjà évalués par la dichotomie de chaque cellule (puissances dans [0,5 ; 0,99], poids 2 000),
  n80 = (logit 0,8 − a)/b, écart-type par la méthode delta, multiplié par √(déviance/ddl) quand elle dépasse 1 (méthode de `ajustement-n80-gd8-v1.py`). Sur les 16 passages
  distincts de T1 : écart-type **0,4 à 2,3 unités** ; déviance par degré de liberté 0,19 à 1,85 ; le n80 de la dichotomie s'écarte du n80 ajusté de **−4 à +12 unités** (il rend la borne
  haute de son dernier pas, sur des points bruités : ce n'est pas toujours un majorant). Le « pire » ajusté est le plus grand des quatre n80 ajustés. **n_h reste calculé sur le
  n80 de la dichotomie** (règle v8 inchangée, lignes v8 reproduites) ; calculé sur le n80 ajusté, il serait égal dans 24 cas sur 34 (17 lignes × deux seuils, la ligne sans dispersion comptée
  deux fois), plus petit de 16 unités dans 9 cas et plus grand de 16 dans 1 cas (colonne de droite de T1) ; la marge 1,06 couvre largement l'écart-type de l'ajustement (≤ 1 %).
- La phrase de la v8 « incertitude de graine de 2,2 % au plus » est **retirée** : ce que la v8 mesurait était la résolution de la dichotomie (GD8-04) ; la v9 donne n80 à l'unité
  près avec son écart-type, et ρ = 0,17, seuil 40 : **275,6 ± 1,1** (une graine ; 276,7 ± 0,6 sur quatre graines réunies, GD8) contre 280 par dichotomie.
- **Puissances clés, moyenne sur neuf graines** (20261029 de la v8 et 11 à 18), ρ_A = ρ_B = 0,17 :

{{TABLE:T4}}

  Les valeurs de la v8 (0,847 ; 0,509 ; 0,980 ; 0,905) sont des tirages d'une graine : **0,847 est à 2,9 erreurs types au-dessus de la moyenne 0,8395 ± 0,0025** ; 0,509 à 1,0 erreur type au-dessus,
  0,905 à 1,7 au-dessous, 0,980 au centre. Valeurs à citer au préenregistrement : **0,840 ± 0,003 ; 0,506 ± 0,003 ; 0,980 ± 0,001 ; 0,908 ± 0,002** (pire des quatre cellules, par
  graine, moyenne ± erreur type sur neuf graines) ; GD8 trouvait de même ≈ 0,838 et ≈ 0,50 sur 21 graines pour la cellule la plus exigeante.
- **Arrondi** : toutes les puissances de la v9 sont arrondies au plus proche à trois décimales ; « tronqué » et « minorant » sont retirés.

## 4. GD8-07 → ρ honnête = 2 × ρ saboté : option au script, effet borné, condition de validité

- **Où** : `simulation-puissance-garde-delta-v9.py`, option `--facteur-rho-honnetes F` (défaut 1 : sans effet ; refusée sans dispersion bêta combinée, avec la copule, les strates,
  le neuvième comparateur, `--lien-coupe`, des fichiers réels, ou si F·ρ ≥ 1) ; le côté honnête de A **et** des comparateurs prend la corrélation F·ρ, le côté saboté garde ρ ;
  passages `rhoh2x-meme-rho0.05`, `-0.10`, `-0.17` (options R1 de la v8, F = 2) ; essais (sain : corrélations de la décomposition et écarts-types tirés conformes ; six
  artefacts refusés) dans `essais-gd8-03-07-08-v9-sortie.json`.
- **Résultat (scénario SUPPOSÉ : faux positifs concentrés sur des unités honnêtes difficiles)** :

{{TABLE:T5}}

  Au seuil 160, doubler le ρ honnête relève le n80 pire de **+8 (ρ saboté 0,05), +24 (0,10) et +48 (0,17)** unités (ajusté : +11, +24, +44) et n_h de +16, +16 et **+64**
  (304 → 320, 336 → 352, 384 → 448) ; au seuil 40, n_h ne change pas à ρ ≤ 0,10 (288) et passe de 304 à 336 à 0,17. La garde est le maillon touché : minimum des 8 gardes
  à 288 unités, seuil 160, K_h = 5, biais δ/4 : 0,845 → 0,716 (ρ = 0,10), 0,751 → 0,567 (ρ = 0,17).
- **Condition de validité à écrire au préenregistrement** : la table est lue côté sabotage et suppose le même ρ côté honnête ; si le ρ honnête est le double, elle sous-estime
  n_h de 16 unités jusqu'à ρ̂ ≈ 0,10 et de 64 unités (seuil 160) à 0,17. Le côté honnête n'est pas lisible au pilote (écart-type de ρ̂ 0,047 à 0,071 sur 288 unités, v8) : on ne
  peut pas vérifier cette condition avant G1 ; on peut seulement la borner (ce paragraphe) ou ajouter la marge correspondante.

## 5. GD8-03 → strates : « commune » comme témoin de construction, parts de variance, portée partielle, décalages fixés d'avance

- **Où** : `tableaux-v9.py`, blocs T6 et T7 (lecture des `moments_tires` des passages v8 de strates) ; option nouvelle `--portee-strates partielle --fraction-strates-comparateurs f`
  du script v9 (γ_B = f·γ_A ; essais sain et quatre artefacts dans `essais-gd8-03-07-08-v9-sortie.json`) ; passages `strates-partielle-f0.5-S2|S3-g0.4-brut|calibre`.
- **La portée « commune » est un témoin de construction, non une mesure** : la strate multiplie les espérances du sujet et des comparateurs ; l'étalonnage ne retire du contraste
  que (0,50 − 0,40)·γ·d, soit **2,7 % (deux strates) et 1,3 % (trois strates)** de sa variance ; le gain nul (−0,001 ; +0,001) est voulu par le modèle. Surtout, à ρ total tenu,
  la strate commune est une **difficulté partagée** par le sujet et les comparateurs : corrélation de leurs probabilités côté sabotage 0,5·0,4·γ²·moyenne(d²)/√(0,17·0,25 × 0,17·0,24)
  = **0,77 (deux strates) et 0,51 (trois strates)**, l'équivalent de la copule c ≈ 0,8 et 0,5 du § 3.1 de la v8. **C'est pourquoi sa fiche brute est haute** (0,991 et 0,984 en
  moyenne des quatre cellules, contre 0,847 au pire et 0,865 en moyenne des quatre cellules sans strate, passage v8 `meme-rho0.17`) : elle décrit un autre monde que la référence, et ne se compare pas à 0,847.
- **Parts de variance de la portée « sujet »** (T6) : la strate explique, côté sabotage, **94 % (deux strates, γ = 0,4), 63 % (trois, γ = 0,4), 24 % (deux, γ = 0,2) et 16 %
  (trois, γ = 0,2)** de la variance inter-unités de A, et **≤ 1 %** côté honnête ; elle porte 32 %, 22 %, 8 % et 5 % de la variance du contraste, ≤ 0,3 % de celle de la garde.
  Le meilleur gain de la v8 (+0,054 à 288 unités) suppose donc une covariable connue d'avance qui explique **63 % de la dispersion du sujet saboté** ; la garde n'en est pas touchée.

{{TABLE:T6}}

- **Portée partielle (γ_B = 0,5 γ_A, nouvelle)** : la strate déplace A deux fois plus que les comparateurs ; l'étalonnage retire 9,4 % (trois strates) et 15,7 % (deux strates)
  de la variance du contraste, mais le gain reste **+0,009 et +0,004** à 288 unités (moyenne des quatre cellules ; −0,000 à 400), parce que la part commune de la strate joue
  déjà comme une difficulté partagée (fiche brute 0,959 et 0,982) :

{{TABLE:T7}}

  Lecture : le gain de l'étalonnage croît avec la part de la strate propre au sujet (commune 0 → partielle ≤ +0,009 → sujet +0,046 à +0,055), et s'efface à 400 unités dans
  tous les cas (≤ +0,004). La recommandation de la v8 (« ne pas compter sur les strates pour dimensionner ») est inchangée.
- **Règle pour le préenregistrement, si l'étalonnage par strate devait servir** : décalages de strate **fixés avant l'épreuve** (pilote ou construction), jamais estimés sur les
  unités de l'épreuve (sinon le processus de pari n'est plus prévisible) ; écrêtage à [−1 ; 1] avant le pari (§ 6).

## 6. GD8-05 → vérification de l'écrêtage refaite au critère scindé déclaré d'avance ; convention pour le préenregistrement

- **Où** : `verif-ecretage-v9-critere.md` (critère, scellé à 03:23 UTC **avant** toute exécution, empreinte `a0da3b4c…`), `verif-ecretage-v9.py` (le script refuse de tourner si
  le critère a changé depuis son scellement), sorties `verif-ecretage-v9-sortie.json` (script v9 intermédiaire `-etape1`) et `verif-ecretage-v9-v2-sortie.json` (script v9 final),
  journaux et manifestes ; `echecs-verif-ecretage-v8/` (sorties échouées de la v8 retrouvées).
- **Sorties échouées de la v8 (règle R11 : vérifié sur disque avant de déclarer absent)** : la consigne les disait absentes ; une recherche sur tout le disque (hors chemins
  interdits) en a **retrouvé trois sur quatre** dans l'espace de travail de la lignée (`travail-v8/ebh-pole-essai1`, `-essai2`, `-essai3`, sortie et journal chacune, script v8
  `4c7c93a9…`, toutes `"conforme": false`) ; elles sont **versées** dans `echecs-verif-ecretage-v8/` avec leurs compagnons. La quatrième, l'exécution **plantée** (écart étalonné
  hors de [−1 ; 1] refusé par le juge), n'a laissé **aucune sortie** : elle est absente, et le reste. Les essais 2 et 3 montrent les cinq cellules à écart non nul toutes à
  K_h = 3 (hors périmètre), écart de trajectoire ≤ 0,088.
- **Comment** : deux conventions sur les mêmes tirages — (S) simulation : δ − g_étalonné écrêté à [−1 ; 1] ; (J) juge : g_étalonné écrêté, puis δ − g. Critère C1
  (périmètre : K_h ∈ {5 ; 10} × S ∈ {2 ; 3} × portée commune ou sujet × biais 0 ou δ/4, soit **16 cas** ; 288 unités, k = 8, 2 000 répétitions ; **erreur de
  décompte dans le critère scellé** : il écrit « 32 cas », alors que son énumération en donne 16 ; la vérification porte sur les 16 cas énumérés ; je ne réécris pas le
  critère scellé et je signale l'erreur ici) : part des gardes hors de [−1 ; 1] < 10⁻³, |écart de puissance des 8 gardes| ≤ 0,003 aux seuils 40 et 160, contrastes identiques ; C2 (K_h ∈ {2 ; 3}) :
  descriptif seulement. **Résultat : 16 / 16 conformes**, deux fois (script intermédiaire et script final, résultats identiques champ à champ) ; plus grand écart de puissance
  0,0000 au seuil 40 et 0,0005 au seuil 160 (une répétition sur 2 000), part des gardes hors de [−1 ; 1] au plus 1,2 × 10⁻⁴, contrastes identiques. Hors périmètre (descriptif) : K_h = 2, part hors intervalle 9,1 × 10⁻⁴, écart −0,001 au seuil 160 ; K_h = 3 : 2,7 × 10⁻⁴, écart 0.
- **Convention proposée pour le préenregistrement**, si l'étalonnage par strate devait servir : « les décalages de strate sont **fixés avant l'épreuve** (sur le pilote ou
  par construction), jamais estimés sur les unités de l'épreuve ; l'écart étalonné de garde g − décalage et de contraste v − décalage est **écrêté à [−1 ; 1] avant le pari**
  (convention du juge) ; l'écrêtage par en bas d'un contraste étalonné relève légèrement sa moyenne (sens non prudent, ici ≤ 10⁻⁴ × 0,2) et la part des valeurs écrêtées est
  rapportée ».

## 7. GD8-06 → « SUPPOSÉ » partout pour le neuvième comparateur

- **Où** : ce rapport (résumé, § 2, § 10, phrase du § 11), `tableaux-v9.md` (T3 : en-têtes de colonne « 0,05 SUPPOSÉ » et source), docstring de `lancer-complements-v9.sh`
  pour le ρ honnête.
- **Comment** : chaque mention de l'écart 0,05 du neuvième comparateur porte « SUPPOSÉ » ; l'hypothèse **« côté honnête du neuvième inchangé (f_B9 = τ) » est écrite comme
  SUPPOSÉE** : un comparateur « fort » qui alerte plus sur les sabotés alerte vraisemblablement plus aussi sur les honnêtes, ce qui abaisserait sa garde ; non simulé.

## 8. GD8-08 → fiche nulle avec neuvième comparateur : refus nommé

- **Où** : `simulation-puissance-garde-delta-v9.py` (`principal` : refus de `--fiches-nulles N > 0` avec `--ecart-contraste-neuvieme` ; `variante_nulle` transmet désormais
  `ecart9`, le facteur honnête et la fraction de strates, et `tirer` refuse une variante nulle à neuvième particulier : garde de second rang) ; essais
  `essais-gd8-03-07-08-v9.py`, sortie `essais-gd8-03-07-08-v9-sortie.json`.
- **Comment** : j'ai choisi le refus plutôt que la transmission silencieuse, parce que la fiche nulle d'un neuvième « fort » n'est pas définie (écart nul pour les neuf ? ou
  neuvième gardant son décalage, ce qui donnerait un contraste non nul ?) ; trancher serait un choix de modèle. Essais (règle R5) : sain — neuvième sans fiche nulle, code 0 ;
  fiche nulle sans neuvième, code 0 ; variante nulle tirée à k = 8, tirage fait ; artefact — la commande exacte de GD8, refus nommé « GD8-08 », aucun fichier laissé ;
  variante nulle tirée à k = 9, refus de la loi. **5 / 5 conformes** (dans 17 / 17 au total).

## 9. GD8-09 → manifestes, commit

- **Où** : chaque script auxiliaire de la v9 (`precision-rho-pilote-v9.py`, `verif-identite-v8-v9-v3.py`, `essais-gd8-03-07-08-v9.py`, `verif-ecretage-v9.py`, `tableaux-v9.py`,
  `construire-rapport-v9.py`) écrit **son propre manifeste** (`manifeste-<sortie>.json` : commande, empreinte du script, graines, versions, empreintes des fichiers écrits) ;
  manifeste d'ensemble `manifeste-puissance-garde-delta-v9.json` (`assembler-manifeste-v9.py`).
- **Commit** : lu par l'appelant, hors des scripts, par `git -C /home/claude/controle-ia-travail rev-parse HEAD` (lecture seule) = `0c8e1c8a991fddc15b62890b5454d0fb7472faff`,
  passé à chaque passage (`--commit-declare`) et à chaque script auxiliaire, écrit dans chaque manifeste. La seule autre commande git lancée : `git show` et `git ls-tree` sur
  `origin/main` pour copier la contre-lecture GD8 (`entrees-gd8/`, empreintes identiques à celles d'`origin/main`) ; `origin/main` = `390ba1c1…` au moment de la copie.
- Versions : Python 3.13.18, numpy 2.5.3, scipy 1.18.1, les mêmes que la v8, pour tous les passages.

## 10. Réserves

1. **Lois synthétiques ; ρ, c, γ, f, le facteur honnête et l'écart 0,05 du neuvième sont des scénarios (SUPPOSÉ)**, pas des estimations ; f_A n'est pas lue avant G1. Le même ρ pour A
   et les comparateurs (hypothèse 1) et ρ_A = 2 ρ_B (hypothèse 2) bornent deux scénarios ; ρ_A > 2 ρ_B n'est pas couvert ; 0 < ρ_A < ρ_B n'est pas passé (attendu plus favorable).
2. **La table en ρ̂ suppose le même ρ côté honnête et côté sabotage** (une seule concentration) ; le § 4 borne l'écart pour un ρ honnête double ; au-delà, c'est une
   **condition de validité** de la table à écrire au préenregistrement.
3. **La marge de lecture 1,645 × σ** prend σ au plus petit ρ de la grille de précision au moins égal à ρ̂ (côté prudent) ; c'est une borne unilatérale à 95 % sous la loi bêta
   simulée, sans correction pour la non-normalité de ρ̂ (asymétrique à petit N) ni pour le choix de la ligne (pas de la grille).
4. **n_h reste calculé sur le n80 de la dichotomie** (règle v8, pour que les lignes v8 se reproduisent) ; l'ajustement logistique (GD8-04) le confirme à quelques unités près ;
   la colonne « n_h depuis n80 ajusté » de T1 dit où l'arrondi au multiple de 16 changerait.
5. **Les passages de la grille prolongée (GD8-01) sont exécutés par le script v8 scellé, inchangé** (empreinte `4c7c93a9…`), lu dans le dossier v8 ; ceux des compléments
   (graines, ρ honnête, portée partielle) par le script v9 final (`f483a271…`). L'identité v8 = v9 hors options nouvelles est vérifiée (cinq configurations, 0 différence ;
   témoin négatif vu).
6. **Un script v9 intermédiaire** (`simulation-puissance-garde-delta-v9-etape1.py`, `3232a994…`, avant l'ajout de la portée partielle) a servi aux premiers essais
   (`verif-identite-v8-v9`, `essais-gd8-07-08-v9`, `verif-ecretage-v9` sans suffixe) ; gardé et remplacé (R12). **Un échec à déclarer** : la première version du script final
   refusait toute loi sans strates (garde `(strates and …) != …` mal écrite) ; vu par `verif-identite-v8-v9-v2` (sortie conservée, `"conforme": false`), corrigé, revérifié par
   `verif-identite-v8-v9-v3` (conforme).
7. **Erreur dans le critère scellé de l'écrêtage** : « 32 cas » pour 16 énumérés (§ 6) ; non réécrit.
8. **Seuil 160** : borne basse de la retenue par la règle e-BH à m = 8, non simulée ; lecture (A) à deux modes seulement (réserves de la v6 à la v8, inchangées).
9. **Coûts en épisodes** : plan apparié supposé, 135 épisodes par unité à K_h = 5 (180 à K_h = 10 ; 150 avec un neuvième comparateur à K_h = 5) ; aucun montant en argent.
10. **Non relu par une autre main (règle R2)** : à regarder en premier : la règle de lecture en ρ̂ (`tableaux-v9.py`, fonctions `sd` et `ligne`), le choix de σ, les options de repli,
    la branche `facteur_h` de `tirer` et de `decomposition`, la portée partielle (`_gamma_b`, `_b_applique`).

## 11. Phrase proposée pour le préenregistrement de G1 (compatible avec GD8-01 à GD8-09 ; valeurs à trancher par Lazar)

« Sous lois synthétiques non préenregistrées (simulation v9, 2 000 répétitions, graine 20261029 ; puissances clés moyennées sur neuf graines), à τ = 0,01, δ = 0,05, huit
comparateurs, écart de contraste 0,10, K_s = 10, lecture (A), K_h ∈ {10 ; 5} et biais ≤ δ/4, si le sujet et les comparateurs ont la même dispersion d'unité bêta de corrélation
intra-unité ρ = 0,17, la puissance de la fiche au pire de ces quatre cellules vaut 0,840 ± 0,003 au seuil 40 et 0,506 ± 0,003 au seuil de référence 160 à n = 288 unités, et
0,980 ± 0,001 et 0,908 ± 0,002 à n = 400 (moyenne ± erreur type sur neuf graines). **La taille n_h est lue sur la dispersion ρ̂ mesurée au pilote côté sabotage** (K = 10
épisodes par unité), par la table de lecture v9 : ρ_haut = ρ̂ + 1,645 × écart-type de lecture, ligne égale ou immédiatement supérieure dans chacune des deux hypothèses
ρ_A = ρ_B et ρ_A = 2 ρ_B, n_h = la plus grande des deux ; pour un pilote de 288 unités, ρ̂ = 0 ; 0,05 ; 0,10 ; 0,17 donnent n_h = 288, 288, 320, 416 au seuil 40 et 304, 352, 416,
544 au seuil 160 ; au ρ vrai de 0,17, n_h vaudrait 304 / 384 (ρ_A = ρ_B) et 384 / 496 (ρ_A = 2 ρ_B). Au-delà de ρ̂ = 0,17 (288 unités), la table ne répond pas et
[repli : option A, B ou C du rapport v9, § 1.3, choisie par Lazar avant le scellement]. La table suppose la même corrélation intra-unité côté honnête et côté sabotage ; un ρ
honnête double (SUPPOSÉ) relèverait n_h de 16 unités au seuil 160 jusqu'à ρ = 0,10 et de 64 à 0,17. Un neuvième comparateur d'écart de contraste 0,10 ne change pas ces tailles
(+16 unités au plus) ; à écart 0,05 (SUPPOSÉ, côté honnête du neuvième inchangé : SUPPOSÉ), n_h à neuf comparateurs vaut 288 à 736 au seuil 40 et 368 à 976 au seuil 160
selon la dispersion, soit un écart de +0 à +432 et de +80 à +592 unités. Si un étalonnage par strate sert, ses décalages sont fixés avant l'épreuve et l'écart étalonné est
écrêté à [−1 ; 1] avant le pari. »

Chiffres derrière la phrase : T4 (0,840 ; 0,506 ; 0,980 ; 0,908, `tableaux-v9-sortie.json`, bloc `puissances_cles_graines`) ; T2-points (lectures en ρ̂, bloc `table_rho_chapeau`) ;
T1 (tailles au ρ vrai, bloc `table_rho_vrai`) ; T2-288 (premier hors table 0,18 : bloc `premier_hors_table`) ; T5 (bloc `rho_honnete_double`) ; T3 (bloc `neuvieme_n_h`) ; § 6.

## 12. Fichiers et empreintes

Entrées en lecture seule : le dossier v8 (script `simulation-puissance-garde-delta-v8.py` `4c7c93a9…`, sorties des passages, `precision-rho-pilote-v8-sortie.json`), empreintes
dans `manifeste-puissance-garde-delta-v9.json` (bloc `entrees_v8`) ; contre-lecture GD8 copiée dans `entrees-gd8/`. Remplacés avant toute transmission, gardés (R12) :
`simulation-puissance-garde-delta-v9-etape1.py`, `verif-identite-v8-v9*.py` et sorties (`-v3` fait foi), `essais-gd8-07-08-v9*` (remplacé par `essais-gd8-03-07-08-v9*`),
`verif-ecretage-v9-sortie.json` (remplacé par `-v2`), dossiers `essais-v9/`, `essais-v9-v2/` (`essais-v9-v3/` et `essais-gd8-v9-v2/` font foi). Le rapport lui-même a son
compagnon `rapport-puissance-garde-delta-v9.md.sha256` et son manifeste `manifeste-rapport-puissance-garde-delta-v9.json`.

{{EMPREINTES}}
