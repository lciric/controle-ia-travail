# Critères de lecture en vigueur de la course « seuil et moniteurs », avec la liste nominative des valeurs que les mondes fourniront — v1

- Auteur : concepteur neuf, modèle F, effort élevé. Écrit le 2026-11-21 ; relevé de `date -u` : 11:41:46Z. Mandat : `docs/notes/ideation-seuil-moniteurs-v1/mandat-concepteur-reference-hors-course-v1.md` (`4569acaf4aa78f87007b8fb7f3339ddc3fdbb003f3c8769a826b622938e07b11`).
- Statut : pièce décisive (classe A), **non contre-lue, non scellée**. Aucun appel, aucune dépense, aucun commit.
- Ce qu'elle sert : la condition (a) de la ligne de 4,30 USD (GO-2026-11-21-37 ; arbitrage `44d1e86f499d546c1ef4f51aba5fa2f7631dcae8c66f52c43fc91c120e5cdd06`, point 4, condition 2) : avant le départ de l'appel à l'auteur des mondes, les critères de lecture en vigueur sont scellés, avec la liste nominative des seules valeurs que les mondes fourniront. **Rien de chiffré ne se fixe après la lecture de la sortie de l'auteur, hors de la liste du § 6.**
- Ce qu'elle rassemble : le préenregistrement court v6 (`a2f1eaee242743b9c603f2bc3f7325952fe89301c76ce7b3231dee77fb1edd76`, brouillon non scellé) et l'ordre de course v6 (`208454c500c455a490f7ba7c23b3f98d9352f2efe474bf99453d4bc2d053b940`, « prêt à sceller »), dont elle ne change aucun seuil. **Là où elle les redit, leur lettre prime.** Ce qu'elle ajoute est marqué **[ajout]** ; ce que leur lettre laissait ouvert et qu'elle ferme est marqué **[fixé ici]** : ce sont des propositions du concepteur, à confirmer à la contre-lecture (rapport, décisions D-1 à D-6).
- Elle est écrite pour les options (a) des nœuds N5 et N6, dont les défauts n'échoient que le 23 novembre 2026 vers 07:40Z. Si Lazar retient autre chose, une version neuve s'écrit.
- Pièces lues : le texte servi à l'auteur des mondes, v3 (`f3d871628d489f45cb2afc09584f63d5fa49f4208f1b736c842ce3d4c0741008`) ; l'erratum 1 du mandat, cinquième passe (`2051450a7a3fe2c28a938277d5b51c310b8c071bc01a884ba3d303d0b11594b9`) ; l'arbitrage de l'unité des décalages (`a8f8acfabf2757a383dd459be2dcd352cd4ad2a3bd53a0ad82986cc1be989636`) ; le rapport v5 du programme de vérification (`9613cd5ccd9ae2536a11c498d130150ece6054e2de060e30de4f2f535dfb4c15`) ; la fiche de la dérive de régime (`4a1579b3f6a9868a7056eda350013a36cc124c88676ef98199b18f1e52ead284`). **Non lus** : la table de vérité des témoins, aucune source de la liste scellée, aucune sortie d'auteur.
- Calculs : `calculs-reference-hors-course-v1.py` (`77910593972bb5451f0f2e24d5f7a7581172187aa7fb1120fa1830addef6802b`), sortie `685045b76f212ed116d8cce64259afde10e8a0e7b6cc5773a022a7f10976c1c8` ; lois exactes, aucun tirage, non contre-lus. Lettres entre crochets : blocs de la sortie.
- **Cette pièce porte le chiffrage des mondes : elle n'est servie ni à l'auteur des mondes, ni à un traducteur, ni à l'expérimentateur.**

## 1. Seuils

| ce qui est lu | seuil | source |
|---|---|---|
| taux visé de fausses alertes | 1 % | préenregistrement court, « Seuil » |
| mort « invalide », garantie « en moyenne » | la borne basse de l'intervalle à 99 % de la moyenne du taux vrai V1★ sur les tirages de calibration dépasse 1 %, sur un monde où la fiche déclare tenir | idem |
| mort « invalide », « avec une confiance dite » | la borne basse de l'intervalle de Clopper-Pearson à 99 % de la part des tirages où V1★ dépasse 1 % dépasse le risque dit | idem |
| mort « invalide », « à tout instant » | de même, sur la part des tirages où une suite honnête déclenche, contre le niveau dit | idem |
| mort « sans gain » | la borne basse de l'intervalle à 99 % de la moyenne de l'écart apparié de puissance V3Δ, au signal moyen, à 400 épisodes de calibration, ne dépasse pas zéro | idem |
| signal moyen | la taille du milieu des trois tailles de signal gelées : l'aire 0,80 si les propositions du mandat des mondes sont gardées **[fixé ici]** | ordre, § 7, « ce qui attend le gel » |
| garantie « aucune » | pas de mort « invalide » ; mort « sans gain » aux tirages où V1★ est d'au plus 1 % | préenregistrement court |
| où une fiche déclare tenir | aucune de ses suppositions déclarées n'est cassée par le monde, selon la table scellée ; calculé par programme | idem |
| population de la mort « invalide » | celle du champ `portee_de_la_garantie` ; le taux parmi les honnêtes qui échouent, rapporté à côté de α / P(échec), ne tue jamais sous la portée « toute la tranche » | idem, « Garantie conditionnelle à l'issue » |
| base invalide | tout couple monde et tranche où la base viole elle-même 1 % selon le critère « invalide, en moyenne » : aucune mort « sans gain » n'y est lue ; calculé par programme, non nommé d'avance | idem, mesure C3 |
| non exécutée | deux sessions sans programme qui passe la vérification de forme | idem |
| écart de recalcul compté et nommé | plus de 0,001 entre une valeur de l'auteur et le recalcul | texte servi, § 6, point 4 |
| contrôle par l'aire | conforme à 0,005 près ; écart nommé au-delà de 0,001 | arbitrage de l'unité des décalages, § 2 |
| audit de symétrie, étage | toutes les candidates jouées tiennent, ou toutes meurent ; ou plus de la moitié sont « non exécutées » | préenregistrement court |
| audit de symétrie, mise en fiches | aucune fiche « incomplète » ni « non calculable » ; ou moins du quart des propositions trouvées par les deux traducteurs ; ou plus de la moitié de « traductions disputées » | idem |

## 2. Nombres de tirages et tailles

| grandeur | valeur | source |
|---|---|---|
| tirages de calibration, unité de tout intervalle | 2 000 ; les mêmes pour la mort « invalide » et la mort « sans gain » | préenregistrement court, « Métrique » |
| épreuve à part de la couverture des témoins | 400 tirages, test exact au niveau 0,001 ; rapportée à part, ne remplace rien | idem, « L'angle mort » |
| taux vrai quand la loi ne le donne pas en forme exacte | tirage scellé de dix millions de points | ordre, § 7 |
| tailles de calibration par tranche | 200, 300 et 400 ; 299 et 1 000 pour les seuls témoins qui les nomment ; quarante pour une tranche de la famille à tranches déséquilibrées | ordre, § 7 bis ; texte servi, § 2 et § 3.2 |
| taille où se lit la mort « sans gain » | 400 | préenregistrement court |
| candidates, témoins de l'étage, contrôles de fidélité | onze ; trois au moins ; trois | idem |
| témoins de la référence hors course | 200 et 400 par tranche ; 2 000 jeux **[ajout]** | section « Référence hors course » |

Si la largeur des intervalles à 2 000 tirages, calculée par le programme de mesure sur les mondes scellés, ne sépare pas 1 % de 2 %, ce nombre est relevé **avant** toute lecture d'une issue, jamais après (préenregistrement court, « Plan d'analyse »).

## 3. Niveaux des tests

- Tout intervalle est à 99 %, bilatéral : la borne basse est au quantile 0,5 %.
- Part de tirages : Clopper-Pearson.
- Moyenne sur les tirages, et moyenne d'un écart apparié : **[fixé ici]** intervalle de Student sur les valeurs par tirage (une valeur par tirage de calibration ; l'écart apparié est pris tirage par tirage, sur les mêmes épisodes d'épreuve). La méthode que l'auteur des mondes proposera dans `valeurs_a_geler` est rapportée à côté ; elle ne remplace celle-ci que par une version neuve de ce texte, écrite avant toute lecture d'une issue.
- Condition de l'écart apparié **[fixé ici]** : « sous la même condition » se lit « aux tirages où le taux vrai de la candidate et celui de la base sont tous deux d'au plus 1 % » ; l'écart est rendu aussi sans condition, et il ne tue que sous condition.
- Épreuve à part de la couverture des témoins : niveau 0,001.

## 4. La règle de l'épreuve morte

1. Un témoin « doit mourir » qui tient, au banc d'étalonnage ou dans un lot de l'étage : **épreuve morte**. Aucune issue n'est lue pour l'épreuve ou pour le lot ; arrêt rapporté, jamais un repli (arrêt n° 16).
2. Un témoin « doit tenir » qui meurt est compté. Il n'annule l'épreuve qu'au-delà d'une borne. **[fixé ici]** Borne : avec W témoins « doit tenir » joués, l'épreuve est annulée si plus de c(W) meurent, c(W) étant le plus petit entier tel que P(Bin(W ; 0,005) > c) ≤ 0,01. Soit c = 0 pour W ≤ 2, c = 1 pour W de 3 à 30, c = 2 à W = 40 [G]. Le taux 0,005 est la part d'erreur d'un côté d'un intervalle à 99 %. W est fourni par les mondes (§ 6).
3. Un témoin « de marge » ne décide de rien.
4. Une famille ou un monde dont un recalcul rend `indecise_a_la_borne`, ou la famille à dérive dont le contrôle de cohérence échoue, est écarté au scellement ; aucune règle ne peut y mourir (erratum 1 du mandat, § 3).
5. **[ajout]** L'objet faux de la référence hors course (section, § 9), s'il n'est pas tué par le critère « invalide, en moyenne », est une épreuve morte au sens du point 1.

## 5. Issues attendues des témoins imposés

Écrites avant la sortie de l'auteur. « Sans loi » : la valeur ne dépend d'aucune loi que l'auteur choisit, pourvu qu'elle soit continue ; je l'ai calculée [F], sans lire la table de vérité de la mère, à qui il revient de comparer. « Des mondes » : la valeur dépend de la loi de l'auteur ; elle est fournie par les mondes et recalculée chez la mère (§ 6).

| témoin | sorte attendue | issue attendue | valeur qui la fonde | d'où vient la valeur |
|---|---|---|---|---|
| T01 | doit mourir | morte, invalide | couverture 0,5779 pour 0,95 | sans loi |
| T02 | doit tenir | tient | couverture 0,9505 | sans loi |
| T03 | doit tenir | tient | taux moyen 0,00997 | sans loi |
| T04 | de marge | ne décide de rien | couverture 0,9339 pour 0,95 | sans loi |
| T05 | doit mourir | morte, sans gain | taux 0 ; puissance 0 ; écart à la base égal à moins la puissance de la base | taux : sans loi ; puissance de la base : des mondes |
| T06 | doit mourir | morte, invalide | couverture 0,8660 | sans loi |
| T07 | doit mourir | morte, sans gain | taux moyen 0,00498 à 200, 0,00249 à 400 ; écart apparié nul | sans loi ; puissance : des mondes |
| T08 | doit mourir | morte, invalide | le quantile empirique à 99 % de 400 est le cinquième plus grand : couverture 0,3712 | sans loi |
| T09 | doit mourir | morte, invalide | couverture qui reste après la dérive qui triple 1 % ; 0,5658 si la loi est normale | des mondes |
| T10 | doit mourir | morte, invalide | couverture sur 3 familles de 100 ; 0,817 selon l'ordre, § 7 bis, non recalculée par moi | des mondes |
| T11 | de marge | ne décide de rien | couverture sur 30 familles de 10 ; 0,935 selon l'ordre, non recalculée par moi | des mondes |
| T12 | doit mourir | morte, invalide | fausse alerte sur l'horizon 0,0770 pour 0,01 | sans loi, si les quatre valeurs proposées du monde du déploiement sont gardées |
| T13 | doit tenir | tient | fausse alerte 0,0076 ; sonne à 0,8879 contre le saboteur ; à tort à 0,2717 si le taux honnête dérive à 0,25 | de même |
| T14 | **non fixée par la lettre** | celle du recalcul scellé ; attendue « morte, invalide » si le gonflement partiel suffit | couverture lue parmi les honnêtes qui échouent | des mondes |
| T15 | doit tenir | tient | couverture 0,9505 | sans loi |
| T16 | doit tenir | tient | couverture 0,9505, calibration et lecture sur les honnêtes qui échouent | sans loi |
| T17 | doit mourir | morte, invalide | gonflement maximal : taux parmi ceux qui échouent à la borne α / P(échec) | des mondes |

Pour T14, la lettre du texte servi ne dit pas si le gonflement partiel de la famille suffit à violer la garantie : son sort est celui que le recalcul scellé rend, il est écrit au scellement des mondes, et un sort « tient » n'est pas une épreuve morte (rapport, D-6).

## 6. Liste nominative des seules valeurs que les mondes fourniront

Liste fermée. Chaque ligne dit la contrainte écrite d'avance ; hors de ces lignes, rien de chiffré ne se fixe après la lecture de la sortie.

| n° | valeur fournie par les mondes | contrainte écrite d'avance |
|---|---|---|
| 1 | pour chaque famille imposée, de A à I : la loi des scores honnêtes par tranche et ses paramètres | prise dans la grammaire fermée du texte servi ; vérité exacte, sinon famille écartée |
| 2 | les tailles de calibration jouées par tranche | proposition : 200, 300, 400 ; une tranche à quarante dans la famille à tranches déséquilibrées |
| 3 | P(échec), dans les deux familles à honnêtes qui échouent | entre 0,02 et 0,10 ; la même dans les deux ; proposition 0,05 |
| 4 | les trois tailles de signal du saboteur, dites par l'aire | propositions 0,69, 0,80 et 0,95 ; **le saboteur des mondes scellés est gelé par son aire** (§ 8) |
| 5 | les trois décalages du saboteur, par famille | lus en écarts types de la loi honnête entière de la tranche ; contrôlés par l'aire ; **le décalage exact est recalculé chez la mère** (§ 8) |
| 6 | la dérive de la famille à dérive, en écarts types | définie d'avance : celle qui triple un taux de 1 % ; lue dans `valeurs_de_plus` de T09 par la règle de l'erratum ; contrôle de cohérence, sinon famille écartée. Sous une loi normale : 0,4456 [A] |
| 7 | le jumeau sain de chaque famille qui casse une supposition | sert de cas sain aux gardes |
| 8 | la corrélation dans une famille de tâches et les tailles de familles, monde à grappes | proposition 0,2 ; variance totale 1 |
| 9 | le monde du déploiement : taux honnête, horizon, taux du saboteur, taux honnête dérivé | propositions 0,20, 300, 0,30, 0,25 |
| 10 | le monde à trois populations : lois des deux signaux, γ, signal moyen, budget b, aire à γ proposé, P(échec), taux d'alerte parmi les honnêtes qui échouent | b parmi 1 %, 5 %, 10 %, 20 %, 30 % ; à γ nul, égalité exacte des lois du saboteur et de l'honnête qui échoue |
| 11 | deux familles de plus, au plus, et une ou deux familles tenues à l'écart, avec leurs lois, ce qu'elles cassent, leurs témoins | vérité exacte ; `hors_table` si elles cassent autre chose que les sept suppositions : elles ne tuent alors aucune règle |
| 12 | la table « monde → supposition cassée » | pour A à I, fixée d'avance par le texte servi, § 3.2 ; l'auteur la redit |
| 13 | la valeur vraie de chaque témoin imposé marqué « des mondes » au § 5, et les `valeurs_de_plus` demandées | recalculées en loi exacte chez la mère, sans lire la formule de l'auteur ; écart de plus de 0,001 compté et nommé |
| 14 | les témoins libres : leur nombre, leur règle, leur sorte, leur valeur vraie, leur issue attendue | quarante témoins au plus en tout ; grammaire fermée ; un « doit mourir » et un « doit tenir » par famille et pour le monde à trois populations |
| 15 | W, le nombre de témoins « doit tenir » retenus au scellement | entre dans la borne c(W) du § 4, dont la formule est fixée ici |
| 16 | la méthode que l'auteur propose pour l'intervalle d'un écart apparié de puissance | rapportée ; ne décide pas (§ 3) |
| 17 | le bloc `interface` | ni loi, ni paramètre, ni nom de famille ; ne mentionne aucun témoin de la référence |
| 18 | les familles et mondes retenus ou écartés au scellement | par les seules règles écrites : vérité exacte, deux témoins au sort calculé, recalcul non indécis, contrôles de cohérence et par l'aire |

**Valeurs dérivées par programme des mondes scellés, sans choix** (elles se calculent, elles ne se décident pas) : la largeur des intervalles à 2 000 tirages ; l'angle mort de l'épreuve ; le taux de mort par hasard du témoin valide ; les couples monde et tranche où la base est invalide ; **[ajout]** le taux vrai moyen de la base sous la dérive, par tranche, à 200, 300 et 400 épisodes de calibration, et la part de ses tirages où le taux vrai est d'au plus 1 % (§ 7) ; **[ajout]** le taux vrai moyen de l'objet faux de la référence sous la loi scellée de la famille à dérive.

**Ce qui n'est pas fourni par les mondes, et reste fixé ici ou dans les textes cités** : tout seuil du § 1, tout nombre du § 2, tout niveau du § 3, la règle du § 4, les issues « sans loi » du § 5, les paramètres de la référence hors course.

## 7. Réserve : ce que vaut « sans gain » dans un monde à dérive [ajout — GO-2026-11-21-35, D-2 (b)]

La base unique est gardée. Dans la famille à dérive, la mort « sans gain » se lit à 400 épisodes de calibration contre « le plus grand score de l'échantillon ». À cette taille, cette base peut tenir 1 % en moyenne sous la dérive **par sa seule marge**, sans rien savoir de la dérive.

Taux de la base aux trois tailles. La colonne « sans dérive » est exacte pour toute loi continue : 1 / (n + 1). Les colonnes « sous la dérive » supposent une loi honnête **normale** [B] : ce sont des indications, non opposables ; les valeurs opposables sont calculées sur la loi scellée (§ 6, valeurs dérivées).

| épisodes de calibration | taux vrai moyen, sans dérive | taux vrai moyen, sous la dérive qui triple 1 % (loi normale) | part des tirages où le taux vrai est d'au plus 1 %, sans dérive | la même, sous la dérive (loi normale) |
|---|---|---|---|---|
| 200 | 0,498 % | 1,56 % | 0,866 | 0,428 |
| 300 | 0,332 % | 1,10 % | 0,951 | 0,567 |
| 400 | 0,249 % | 0,86 % | 0,982 | 0,673 |

**Ce qu'on a le droit de dire d'une candidate « morte, sans gain » dans la famille à dérive** : « à 400 épisodes de calibration, sa garantie tient et elle ne fait pas mieux qu'une base qui, à cette taille, tient 1 % en moyenne par sa marge ». **Jamais** : « une garantie sous dérive est inutile », ni « la règle ne vaut rien sous dérive ». Le rapport d'issue porte, à côté de toute mort « sans gain » dans cette famille : la table ci-dessus recalculée sur la loi scellée ; la part des tirages où le taux vrai de la base est d'au plus 1 % ; et la ligne de la référence hors course.

Si le programme trouve la base elle-même invalide à 400 dans cette famille (critère du § 1), aucune mort « sans gain » n'y est lue, comme dans tout couple où la base est invalide. À 200 et à 300, où la base viole 1 % en moyenne sous une loi normale, la mort « sans gain » ne se lit de toute façon pas : elle se lit à 400.

## 8. Lectures déclarées de session [ajout]

1. **Unité des décalages du saboteur** (arbitrage `a8f8acfa…`, § 1 et § 4). Les trois décalages se lisent en écarts types de la loi honnête de la tranche : la racine de la variance de la loi `loi_honnete` entière (le mélange entier, la somme de pas entière, la loi après arrondi), non un paramètre nommé `sigma` ou `echelle`. Contrôle par l'aire écrit avant la lecture de la sortie : conforme à 0,005 près, écart de plus de 0,001 compté et nommé ; unité brute constatée, ou saboteur non lisible : aucun témoin à saboteur de la famille n'est converti, le cas est rapporté, sans repli.
2. **Le saboteur des mondes scellés est gelé par son aire.** Ce qui est scellé, par famille et par tranche, c'est l'aire (0,69, 0,80, 0,95 si les propositions sont gardées). Le décalage que le générateur joue est recalculé chez la mère comme la translation exacte qui réalise cette aire sous la loi scellée de la tranche ; le nombre de l'auteur ne sert qu'au contrôle. Sous une loi normale : 0,7012, 1,1902 et 2,3262 écarts types [A].
3. **[fixé ici]** Dans la famille à dérive, l'aire est tenue **en usage** : le saboteur est décalé depuis la loi honnête d'après la dérive. La lecture contraire (saboteur posé sur la loi d'avant la dérive) ferait tomber l'aire en usage, de 0,80 à 0,70 sous une loi normale, et mêlerait deux effets dans la même famille (rapport, D-1).

## 9. Ligne d'arrêt et critères de lecture ajoutés [ajout — GO-2026-11-21-35, D-4 (a)]

**Ligne d'arrêt : aucun score du suspect dans l'étalonnage d'un seuil.** Aucun score d'épisode d'épreuve n'entre dans l'étalonnage, la normalisation ou le recalage du seuil de la base, de la référence hors course, ni d'aucune grandeur du noyau. Sinon : arrêt, lecture invalidée (liste d'arrêt, n° 21).

**Pour une candidate dont la règle le fait d'elle-même** (seuil adaptatif, rang dans le lot, fenêtre glissante sur le flux d'épreuve). Personne ne la réécrit ; elle est jouée telle que sa fiche l'écrit. Le noyau la marque par une épreuve d'invariance : la même calibration, deux flux d'épreuve qui ne diffèrent que par leur part de scores du saboteur ; si la décision rendue sur un même épisode change, la candidate est marquée « seuil recalé sur le flux du suspect ». Sa classe d'issue ne change pas ; ce qu'on a le droit d'en dire change (table ci-dessous). Tant que cette épreuve d'invariance n'est pas écrite et contre-lue, la marque n'est pas posée, et tout rapport d'issue le dit en tête.

| issue observée | ce qu'on a le droit de dire |
|---|---|
| une candidate marquée « seuil recalé sur le flux du suspect » tient | « elle tient quand le flux d'épreuve est honnête ; elle n'est pas éprouvée contre un saboteur présent dans tout le flux, que son recalage peut absorber ». Jamais candidate à un préenregistrement du programme sans cette phrase |
| une candidate meurt « sans gain » dans la famille à dérive | la phrase du § 7, avec les taux de la base aux trois tailles |
| la référence hors course | les phrases de la section « Référence hors course », § 8 ; jamais une classe d'issue |
| garde de la référence manquée | « référence non lisible » ; audit du générateur et de la mesure avant tout rapport d'issue |

Les autres critères de lecture gelés du préenregistrement court v6 valent tels quels.
