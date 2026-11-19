# Erratum 1 au brouillon 5 du plan « sabotage ou empreinte de l'adaptateur » (barreau 5) — v1

Écrit par le rédacteur du plan (Claude Fable 5.2) dans la nuit du 19 au 20 novembre 2026. Pièce de travail, à vérifier par le même contre-lecteur avec le différentiel du brouillon 5.

- **Pièces visées** : « T », le texte `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-brouillon5.md` (`6f7e20418c841c79d12f763c67ccfbd4e18c41bccc2a5ca626567ab3606dbfe2`) ; « DV », le devis `devis-adaptateurs-tenus-a-l-ecart-v1-brouillon5.md` (`9ba5db06f2070c2f85fbc34002f27f47aaa9df739c7fbb2ef939efedee85a306`).
- **Source** : le rapport v4 du développeur des corrections du code de formation, `code-formation/rapport-developpeur-corrections-code-formation-v4.md` (`b7e2255500985badcd0c9e8a1fd9e33671d641fd5d252bc254cef79019e274c3`, empreinte confirmée par la mère, recalculée par moi), lu en entier ; la vérification du brouillon 4 (`a091eed2…`), constat W-m3.
- **Ce que fait cet erratum** : il lève les sept marques « [à confirmer par le rapport v4] » (cinq au texte, deux au devis) ; il écrit la règle qui tranche W-m3 ; il range les treize points du § 4 (g) du rapport et écrit ceux qui touchent le texte. 18 couples exacts : 14 au texte, 4 au devis. Chaque « avant » se trouve une fois dans sa pièce au moment où il s'applique, dans l'ordre de ce fichier (`controle-erratum-1-brouillon5-v1.py`, sortie `sortie-controle-erratum-1-brouillon5-v1.txt`).
- **Le rapport ne contredit aucune des sept phrases.** Il demande au texte quatre précisions, que j'écris ici et que je signale au contre-lecteur (§ 5) : ce que « collé » veut dire ; les classes de la part par motif ; ce que « tombée » veut dire quand un versement est repris ; la coupe 3.
- Aucune donnée, aucun résultat. Fichiers écrits par l'outil d'écriture.

## 1. Les sept marques

« Déjà » : le code le fait aujourd'hui (rapport v4). « Troisième tour » : le code le fera, au point cité du § 4 du rapport.

| n° | phrase marquée | état du code | couple |
|---|---|---|---|
| 1 | texte, plan, point 3 : règle du nom de carte | **troisième tour**, point (d) : une fonction du module d'édition remplace le drapeau du lecteur gelé à trois endroits ; le lecteur gelé n'est pas touché. Le rapport demande que le texte définisse « collé » : fait | E-1a |
| 2 | texte, plan, point 3 : part par motif, marqueur des paliers | **troisième tour**, point (a) : seuil à 25 %, marqueur au-dessus de 10 %, une classe par action non éditable. Aujourd'hui : un seul seuil, 10 %. Le rapport demande que le texte nomme toutes les classes : six, au lieu de quatre | E-2a |
| 3 | texte, « Calendrier » : seule la copie `-x1` est lue | **à venir, avec le code de lecture**, point (b) : rien ne l'applique aujourd'hui côté lecture ; la formation sépare déjà les copies par leurs noms et leurs branches. Ne touche pas le code de formation | E-3a |
| 4 | texte, « Calendrier » : le code refuse au-delà de l'enveloppe | **troisième tour**, point (c) : aucune borne de somme aujourd'hui ; la garde commune compte aujourd'hui la relance | E-4a |
| 5 | texte, « Code neuf » : version de `transformers` au manifeste | **déjà** (rapport, § 2) : le manifeste de la marche consigne les versions ; l'épingle du fichier d'exigences tient la version ; aucune garde ne compare, aucune n'est ajoutée | E-5a |
| 6 | devis, en-tête : les deux nombres des instances 6 et 7 | **troisième tour**, point (f) : deux entrées par instance, choisies par le nombre de membres ; le contrôle de l'échéance au prix plafond passe déjà (21,3 et 12,8 heures) | E-6a |
| 7 | devis, § 3 : le code refuse au-delà de l'enveloppe | **troisième tour**, point (c) | E-7a |

## 2. La règle qui tranche W-m3 : quel compteur compte la relance

Écrite au texte (couple E-4a) et au devis (couple E-8a). Deux compteurs, plus une borne à l'inscription :

1. **Par instance** : le cumul de l'instance, plus un quart d'heure, contre sa coupure. Pour une relance : la coupure de l'instance qu'elle remplace.
2. **Commun** : le cumul de toutes les pièces du devis (premières marches, relecture, répétition), plus un quart d'heure, contre le plafond de 200 USD. La dépense d'une relance n'y entre pas ; celle de la première marche d'une instance tombée y reste.
3. **La relance n'a pas de troisième compteur** : sa seule limite en cours de marche est la coupure de chaque instance relancée. Leur somme est bornée à l'inscription de la ligne de relance : deux instances au plus, 56 USD de coupures au plus ; le code refuse la ligne sinon.

Le plafond atteint arrête les pièces du devis, non une relance en cours. Exposition totale : 256 USD au plus. Pour le code (troisième tour, point (c) du rapport, proposition du rédacteur) : la garde de dépense de la marche et la sous-commande de dépense du lanceur reçoivent l'indication « relance » ; `lire_code_et_accord` refuse une ligne qui cite plus de deux instances ou dont la somme des coupures dépasse 56 USD.

## 3. Les treize points du § 4 (g) du rapport

Rangés dans `points-g-rapport-v4-ranges-v1.md` (même dossier), une ligne chacun. En bref : neuf sont pris par le texte ou le devis, sans rien demander au code (1, 2, 4, 5, 6, 7, 8, 12, et le point 3 pour l'échéance de la ligne de relance et le sens de « tombée ») ; le reste du point 3 et les points 9 et 13 renvoient aux points (a), (b) et (c) du rapport ; les points 10 et 11 sont conformes. Aucun point de (g) ne demande de code de formation au-delà des points (a), (c), (d) et (f).

## 4. La ligne « = 203 » du calcul scellé

La sortie scellée de `calcul-devis-formation-trois-membres-v1.py` (`0bcf995e…`) finit par « formation 175 + relecture 20 + répétition 8 = 203 ». La coupure de la relecture à 39 adaptateurs est 21 (quatre cinquièmes du pire cas, 25,6 USD, arrondis à l'entier supérieur) et la somme 204. **Le devis a raison ; la ligne du calcul reste telle quelle** : le calcul est scellé, il n'est pas refait, et aucun nombre du devis ni du texte n'en dépend.

## 5. Ce que je signale au contre-lecteur

- **« Collé »** (E-1a) : une lettre touche le nombre, avant ou après. Mon brouillon 4 citait « 8x » parmi les exemples : la lettre d'après compte donc. Conséquence écrite : si le premier nombre du champ est collé, la règle ne joue pas pour cette action, et rien n'est pire qu'aujourd'hui.
- **« Tombée »** (G-3a) : une instance arrêtée dont le versement est ensuite achevé et prouvé par la mère n'est pas tombée. C'est moi qui le pose ; le rapport demandait seulement que le texte le dise.
- **Coupe 3** (G-12a) : la neuvième et la dixième famille tombent ensemble, avec l'instance 5. Le texte suit le code ; l'autre branche était une ligne de code.
- **Modèle nu en fin de famille** (G-1a) et **base de temps de la règle de coupure** (G-7a) : le texte s'aligne sur le code, sans rien lui demander. Le vérificateur du code a établi qu'aucun chemin n'arrive au tirage suivant avec une dose non nulle ; la limite dure de la dépense reste l'échéance d'arrêt.
- **Restent à mettre à jour à la consolidation**, sous le nom définitif : le statut, « Ce qui change au brouillon 5 », un risque du calendrier et « Contre-lecture », qui parlent encore des marques ; la liste des documents, qui ne cite pas le rapport v4.

## 6. Couples exacts

### Les sept marques, et W-m3

#### Couple E-1a — T — plan, point 3, « Action éditable »

Avant :

```text
« 150 A100 GPU-hours » est éditable ; « A100 : 300 heures », où le lecteur gelé lit 100, ne l'est pas. Le lecteur gelé n'est pas touché : seule la condition d'édition change, la même pour tous les membres, et le contrôle par action « le lecteur gelé relit la valeur voulue » reste [à confirmer par le rapport v4].
```

Après :

```text
« 150 A100 GPU-hours » est éditable ; « A100 : 300 heures », où le lecteur gelé lit 100, ne l'est pas. « Collé » : une lettre touche le nombre, juste avant ou juste après, sans espace ni signe entre eux (« A100 », « H100 », « A100s », « 8x », « 120h ») ; le suffixe « k » que lit le lecteur gelé fait partie du nombre et n'est pas une lettre collée ; un tiret sépare (« GPT-4 » : le 4 compte). Si le premier nombre du champ est collé (« 120h on 2 A100s »), la règle ne joue pas : tous les nombres du champ comptent, comme sans elle. Le lecteur gelé n'est pas touché : seule la condition d'édition change, la même pour tous les membres, et le contrôle par action « le lecteur gelé relit la valeur voulue » reste. Le drapeau « plusieurs nombres » du lecteur gelé reste levé sur ces actions, pour tous les membres à la fois, dans les lignes d'évaluation et dans toute mesure qui le lit.
```

#### Couple E-2a — T — plan, point 3, « Contrôles, par famille »

Avant :

```text
La part est rapportée par famille et par motif (plusieurs nombres, intervalle, suffixe « k », contrôle manqué) [à confirmer par le rapport v4].
```

Après :

```text
La part est rapportée par famille et par motif, en six classes : plusieurs nombres ; intervalle ; multiplication ; suffixe « k » ; action non valide, coût illisible ou absent ; contrôle manqué (épissure, contrôle par action, nombre du champ différent du coût lu). Le marqueur « part non éditable haute » s'écrit au résultat de la famille.
```

#### Couple E-3a — T — « Calendrier », règle de la relance

Avant :

```text
y compris celles que la première marche avait achevées : aucune copie n'est choisie [à confirmer par le rapport v4].
```

Après :

```text
y compris celles que la première marche avait achevées : aucune copie n'est choisie. Cette règle, et l'ordre des lignes (`ENGAGEMENT-B5F` après `SORTIES-FORMATION-B5F` et après toute ligne de relance), sont tenus par l'engagement et par le code de lecture, figés à `CODE-LECTURE-B5F` : ils lisent la ligne de relance au registre, donnent pour chaque famille le nom de la copie à lire, et refusent toute autre source.
```

#### Couple E-3b — T — « Calendrier », règle de la relance

Avant :

```text
elle s'inscrit donc après la fin, ou la chute, de toutes les premières marches, et au plus tard à H + 54 heures.
```

Après :

```text
elle s'inscrit donc après la fin, ou la chute, de toutes les premières marches, et au plus tard à H + 54 heures. Cette échéance est tenue par la mère, qui inscrit la ligne ; le code ne la vérifie pas.
```

#### Couple E-4a — T — « Calendrier », borne de la relance

Avant :

```text
le code refuse une ligne de relance dont les coupures dépassent l'enveloppe [à confirmer par le rapport v4] ; au-delà, c'est un nœud.
```

Après :

```text
le code refuse une ligne de relance qui cite plus de deux instances, ou dont les coupures dépassent l'enveloppe ; au-delà, c'est un nœud. **Quel compteur compte quoi.** Par instance : le cumul de l'instance, plus un quart d'heure, contre sa coupure ; pour une relance, la coupure de l'instance qu'elle remplace. En commun : le cumul de toutes les pièces du devis (premières marches, relecture, répétition), plus un quart d'heure, contre le plafond de 200 USD ; la dépense d'une relance n'y entre pas, celle de la première marche d'une instance tombée y reste. La relance n'a pas de troisième compteur : sa seule limite en cours de marche est la coupure de chaque instance relancée, et la somme de ces coupures est bornée à l'inscription de la ligne. Le plafond atteint arrête les pièces du devis, non une relance en cours.
```

#### Couple E-5a — T — « Code neuf », opérateur d'édition

Avant :

```text
(le nettoyage des espaces au décodage en dépend) et s'écrit au manifeste [à confirmer par le rapport v4].
```

Après :

```text
(le nettoyage des espaces au décodage en dépend) et s'écrit au manifeste de la marche ; aucune garde ne la compare sur l'instance : c'est l'épingle du fichier d'exigences, installée dans un environnement neuf, qui la tient.
```

#### Couple E-6a — DV — en-tête, brouillon 4

Avant :

```text
que le code de formation attend [à confirmer par le rapport v4].
```

Après :

```text
que le code de formation reçoit : deux entrées par instance, choisies par le nombre de membres des familles d'apprentissage.
```

#### Couple E-7a — DV — § 3, relance

Avant :

```text
Le code refuse une ligne de relance dont les coupures dépassent l'enveloppe [à confirmer par le rapport v4].
```

Après :

```text
Le code refuse une ligne de relance qui cite plus de deux instances, ou dont les coupures dépassent l'enveloppe.
```

#### Couple E-8a — DV — § 4, compteur commun

Avant :

```text
Le compteur commun arrête toutes les pièces de ce devis à 200 USD ; il ne compte pas la dépense d'une relance, qui a son enveloppe (§ 3).
```

Après :

```text
Le compteur commun arrête toutes les pièces de ce devis à 200 USD ; il ne compte pas la dépense d'une relance, qui a son enveloppe (§ 3). La dépense de la première marche d'une instance tombée reste dans le compteur commun. Une relance n'a pas de compteur à elle : sa limite en cours de marche est la coupure de l'instance qu'elle remplace, et la somme des coupures des instances relancées est bornée à 56 USD à l'inscription de la ligne. Le plafond atteint arrête les pièces de ce devis, non une relance en cours ; l'exposition totale est de 256 USD au plus.
```

### Les points du § 4 (g) du rapport qui touchent le texte

#### Couple G-1a — T — plan, point 4 (points 1 et 2 du rapport)

Avant :

```text
**Garde d'instance, neuve** : avant chaque tirage et après chaque famille, le modèle est remis à la dose 0 et doit être le modèle nu (dose lue nulle sur tous les modules, sorties d'un contexte de contrôle égales au bit près à celles d'avant l'injection) ; sinon l'instance entière s'arrête. Une empreinte de la base changée par une distillation arrête aussi l'instance entière.
```

Après :

```text
**Gardes d'instance** : elles arrêtent l'instance entière, même quand « pièce » vaut « famille ». (1) Garde neuve : avant et après chaque tirage, et après toute garde levée pendant une famille, le modèle, remis à la dose 0, doit être le modèle nu (dose lue nulle sur tous les modules, sorties d'un contexte de contrôle égales au bit près à celles d'avant l'injection). En fin de famille formée, le modèle est remis à la dose 0 ; la famille suivante l'exige nu avant son tirage. (2) Une empreinte de la base changée par une distillation. (3) Toute sortie interdite par le point 5 de la liste d'arrêt, même si elle ne touche que la sortie d'une famille : liste blanche des sorties, contenu d'un fichier d'adaptateur, contenu borné des fichiers de texte. (4) Un signal d'arrêt. (5) Toute erreur qui n'est pas une garde : mémoire de la carte épuisée, défaut du code. Les entrées communes à l'instance (consigne, fichiers de tâches, configuration) sont contrôlées une fois, avant le manifeste.
```

#### Couple G-3a — T — « Calendrier », règle de la relance (point 3 (v) du rapport)

Avant :

```text
perte de l'hôte, garde d'instance, échéance atteinte, versement non prouvé.
```

Après :

```text
perte de l'hôte, garde d'instance, échéance atteinte, sorties perdues. Un versement non prouvé ne suffit pas : l'instance est alors arrêtée sans être détruite, et la mère reprend le versement ; s'il est achevé et prouvé, sans qu'aucune sortie soit lue, l'instance n'est pas tombée et ses familles sont lues telles qu'elles ont été formées ; s'il ne peut pas l'être, les sorties sont perdues.
```

#### Couple G-4a — T — « Calendrier », lancement au fil des offres (point 4 du rapport)

Avant :

```text
Les heures de carte, donc le coût, ne changent pas avec les vagues ; l'horloge s'allonge.
```

Après :

```text
Les heures de carte, donc le coût, ne changent pas avec les vagues ; l'horloge s'allonge. La commande de création de chaque instance est imprimée juste avant sa création : son échéance d'arrêt se compte depuis cette impression. L'ordre des créations et l'échéance de H + 30 heures sont tenus par la session de formation ; le code ne les vérifie pas.
```

#### Couple G-5a — T — plan, point 14 (point 5 du rapport)

Avant :

```text
La clé `b5f/lecture/plis` sert dès la formation : elle range les 64 tâches d'évaluation en deux plis, et la lecture réemploie cette partition telle quelle.
```

Après :

```text
La clé `b5f/lecture/plis` sert dès la formation : elle range les 64 tâches d'évaluation en deux plis, et la lecture réemploie cette partition telle quelle. La clé d'injection d'une instance, `b5f/instance/<n>/injection`, ne porte pas le suffixe de relance : elle est sans effet sur les adaptateurs, dont l'état initial vient de la clé de leur famille.
```

#### Couple G-6a — T — plan, point 5 (point 6 du rapport)

Avant :

```text
Une évaluation réduite s'écrit au manifeste ;
```

Après :

```text
Une évaluation réduite s'écrit au résultat de la famille, rattaché au manifeste par son empreinte ;
```

#### Couple G-7a — DV — § 4, décision de coupure (point 7 du rapport)

Avant :

```text
« complète » si la fin projetée, poussée et quart d'heure compris, reste sous la coupure ;
```

Après :

```text
« complète » si la fin projetée, poussée et quart d'heure compris, reste sous la coupure (le temps compté part du début de la marche : la mise en place qui la précède, dix à trente minutes d'ordinaire, n'y entre pas ; la limite dure reste l'échéance d'arrêt de l'instance, comptée depuis l'impression de sa commande de création, qui l'arrête avant sa coupure dans tous les cas) ;
```

#### Couple G-8a — T — plan, point 3, « Écriture » (point 8 du rapport)

Avant :

```text
Si la valeur voulue d'un membre passerait sous 1 avec le suffixe « k » (« 2k » divisé par trois), l'action est non éditable, pour tous les membres :
```

Après :

```text
Si la valeur d'un membre passerait d'au moins 1 à moins de 1 avec le suffixe « k » (« 2k » divisé par trois), l'action est non éditable, pour tous les membres (une origine déjà sous 1 avec ce suffixe, « 0.5k », reste éditée, dans la même écriture) :
```

#### Couple G-12a — T — « Calendrier », coupe 3 (point 12 du rapport)

Avant :

```text
3. La dixième, puis la neuvième famille tenue à l'écart : les épreuves restent à 99 % ; l'erreur de l'issue « empreinte » passe de 0,1 % à 0,2 %, puis 0,4 %.
```

Après :

```text
3. L'instance 5, c'est-à-dire la neuvième et la dixième famille tenue à l'écart ensemble (une instance forme toutes les familles de son plan, ou aucune) : huit familles restent, les épreuves restent à 99 % ; l'erreur de l'issue « empreinte » passe de 0,1 % à 0,4 %.
```

### Marqueur

#### Couple M-11a — T — « Marqueurs »

Avant :

```text
M-11 : lever, sur le rapport v4 du développeur des corrections du code, chaque marque « [à confirmer par le rapport v4] » de ce texte et du devis ;
```

Après :

```text
M-11 : fait par l'erratum 1 au brouillon 5, sur le rapport v4 du développeur des corrections du code (`b7e22555…`) ; le troisième tour du code suit les points (a), (c), (d) et (f) de ce rapport, et le code de lecture son point (b) ;
```
