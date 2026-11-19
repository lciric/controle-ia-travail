# Les treize points du § 4 (g) du rapport v4 du développeur, rangés (barreau 5) — v1

Écrit par le rédacteur du plan (Claude Fable 5.2) dans la nuit du 19 au 20 novembre 2026. Pièce de travail. Source : `code-formation/rapport-developpeur-corrections-code-formation-v4.md` (`b7e22555…`), § 4 (g), « points des couples qui supposent un comportement que le code n'a pas ». Les couples cités sont ceux de `erratum-1-brouillon5-plan-sabotage-ou-empreinte-v1.md`.

Trois rangements : **le texte dit** (le texte change, le code reste) ; **le code doit** (le code change, au tour nommé) ; **sans objet** (conforme, ou déjà traité ailleurs).

| n° | ce que dit le rapport | rangement | suite |
|---|---|---|---|
| 1 | Le modèle nu n'est pas exigé en fin de famille formée ; il l'est avant et après chaque tirage, et après une garde levée dans une famille | **le texte dit** | couple G-1a : le texte écrit ce que fait le code. Aucun chemin n'arrive au tirage suivant avec une dose non nulle (vérification du code, § 2) |
| 2 | En mode « famille », le code arrête aussi l'instance pour toute sortie interdite par le point 5 et pour toute erreur qui n'est pas une garde ; les entrées communes sont contrôlées une fois | **le texte dit** | couple G-1a : la liste des cinq gardes d'instance |
| 3 (i) | « Seule la copie `-x1` est lue » : rien ne l'applique côté lecture | **le code doit**, avec le code de lecture | point (b) du rapport ; couple E-3a |
| 3 (ii) | Échéance de la ligne de relance : aucun contrôle | **le texte dit** | couple E-3b : tenue par la mère, à H + 54 heures ; le code ne la vérifie pas |
| 3 (iii) | `ENGAGEMENT-B5F` après toute relance : aucun contrôle | **le code doit**, avec le code de lecture | point (b), 4, du rapport ; couple E-3a |
| 3 (iv) | « Hors du plafond » : la garde commune compte aujourd'hui la relance | **le code doit**, au troisième tour | point (c) du rapport ; couples E-4a et E-8a : la règle des compteurs |
| 3 (v) | « Tombée » pour un versement non prouvé : l'instance est arrêtée, non détruite, et la mère reprend le versement | **le texte dit** | couple G-3a : un versement repris et prouvé ne fait pas une instance tombée |
| 4 | Le lanceur ne connaît ni l'ordre des créations ni l'échéance des créations ; l'échéance d'arrêt se compte depuis l'impression de la commande | **le texte dit** | couple G-4a : règles de la session ; chaque commande est imprimée juste avant la création |
| 5 | Graines : conforme ; la clé d'injection de l'instance n'a pas de suffixe de relance, sans effet sur les adaptateurs | **le texte dit**, pour la seule clé d'injection | couple G-5a : la clé est nommée au point 14 |
| 6 | L'évaluation réduite s'écrit au résultat de la famille, non au manifeste | **le texte dit** | couple G-6a |
| 7 | La règle de coupure part du début de la marche : la mise en place n'y est pas comptée ; la limite dure est l'échéance d'arrêt | **le texte dit** (au devis) | couple G-7a. L'autre branche était trois quarts d'heure de code |
| 8 | Suffixe « k » : le code ne sort l'action que si l'origine vaut au moins 1 et la valeur voulue moins de 1 ; « 0.5k » reste édité | **le texte dit** | couple G-8a |
| 9 | Classes de la part par motif | **le code doit**, au troisième tour | point (a) du rapport ; couple E-2a : six classes |
| 10 | La distillation appelle la fonction gelée avec les mêmes arguments | **sans objet** | conforme |
| 11 | Version de `transformers` au manifeste | **sans objet** | déjà fait ; couple E-5a |
| 12 | Coupe 3 : la dixième puis la neuvième famille sont sur la même instance ; « l'une sans l'autre » n'est pas atteignable | **le texte dit** | couple G-12a : les deux tombent ensemble. L'autre branche était une ligne de code |
| 13 | « 28 USD au plus » supposait une seule relance ; le code accepte plusieurs instances | **le code doit**, au troisième tour | point (c) ; couples E-4a et E-7a : deux instances au plus, 56 USD de coupures au plus |

## Ce que le troisième tour du code doit faire, d'après le texte

- Point (a) : seuil à 25 %, marqueur au-dessus de 10 %, six classes par motif, marqueur recopié au résultat de la famille.
- Point (c), proposition du rédacteur : la garde de dépense et la sous-commande de dépense reçoivent l'indication « relance » ; le compteur commun ne compte pas la dépense d'une relance ; `lire_code_et_accord` refuse une ligne de relance qui cite plus de deux instances ou dont les coupures dépassent 56 USD.
- Point (d) : la règle du nom de carte, avec la définition de « collé » du couple E-1a.
- Point (f) : instance 6, coupure 28 USD, 9,61 à 10,99 heures ; instance 7, 17 USD, 5,71 à 6,40 heures.
- Point (e) : **rien**. « 2k » reste non éditable.
- Du point (g) : **rien** pour la formation ; les points 1, 4, 7 et 12 sont pris par le texte.

Ce qui attend le code de lecture : le point (b) en entier (copie à lire, ordre des lignes d'engagement).
