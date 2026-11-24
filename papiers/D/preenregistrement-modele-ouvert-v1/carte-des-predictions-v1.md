# Carte des prédictions du papier D réfutables sur un modèle ouvert — v1 (étape 3 de la demande reformulée)

- **Classe** : travail (pas de contre-lecture obligatoire) ; elle nourrit le préenregistrement, qui, lui, sera contre-lu.
- **Rédaction** : fille 1 du papier D, 24 novembre 2026. Aucune course, aucune dépense.
- **Énoncés de référence (désignés par la fille 2, note 3)**, cités par empreinte (12 premiers caractères du SHA-256) :
  - manuscrit statique : `manuscrit-arxiv/main-v4-correctif-1.tex` `f02e9db22963` (base de diffusion) ;
  - dynamique : `papiers/D/theorie/brouillon-fable-dynamique-v1/dynamics-section-v1-correctif-1.tex` `54b6a1021718` (à revoir par Fable) ;
  - budget d'audit : `…/audit-budget-section-v1-correctif-1.tex` `c6e5cebfe5fb` (à revoir par Fable) ;
  - découplage : `papiers/D/theorie/decouplage-geometrique-v3-correctif-1.tex` `d2af80280c3e` (à revoir par Fable) ;
  - avantages normalisés par groupe : `papiers/D/theorie/grpo-champ-moyen-v1.tex` `c69aa7879749`.
  Trois de ces pièces peuvent encore bouger : le préenregistrement devra les recopier par empreinte au moment du scellement, et toute prédiction dont la source change après scellement passe par un additif.

## 1. Ce que l'expérience peut réfuter

L'expérience ne réfute aucun théorème. Elle teste si le modèle idéalisé décrit ce que fait un vrai entraînement. La vérité de la triche est établie par programme (tests cachés, cas codés en dur, fichier de tests modifié), jamais par la chaîne de pensée.

| N° | Énoncé (source) | Grandeur mesurée | Issue qui le réfute | Coût relatif |
|---|---|---|---|---|
| P1 | Rejet répété contre pénalité : sous affinage filtré itéré, le filtre se compose d'un tour à l'autre ; la barrière ne s'efface pas tant que la pente par tour reste sous le logarithme du rapport des survies (dynamique, rejet itéré ; Lean `iterated_rejection_iff`) | taux absolu d'épisodes trichés **et non interceptés**, pour mille, par tour, contre le bras sans filtre au même nombre de tours | sous rejet itéré, ce taux croît d'un tour à l'autre alors que le rapport des survies mesuré au tour 1 prédit qu'il décroisse | moyen (affinage supervisé, peu de jetons générés) |
| P2 | Enrichissement de première génération : après un tour de rejet, la survie moyenne des tricheurs monte de variance sur moyenne (manuscrit, théorème 1, partie 1) | survie moyenne au moniteur en boucle des épisodes tricheurs, avant et après un tour ; terme de sélection prédit à partir des épisodes du modèle de base | l'écart observé moins le terme prédit (terme de transmission de l'équation de Price) **mesure la généralisation** ; P2 réfute seulement si le terme de sélection prédit s'écarte de la mesure sur les épisodes retenus eux-mêmes (contrôle de calcul) | faible (un tour) |
| P3 | Bistabilité à deux canaux : à pénalité égale, l'état final dépend de la dose initiale de triche et d'obscurcissement ; le modèle de base reste honnête là où un modèle amorcé bascule (dynamique, théorème à deux canaux) | taux final de triche obscurcie (triche réelle sans mention dans la chaîne de pensée) selon la dose d'amorçage (0, faible, forte) | mêmes états finaux pour toutes les doses (pas d'hystérésis), ou bascule du modèle de base sans amorçage aux mêmes pressions | élevé (trois doses × bras) |
| P4 | Pénalité à double tranchant : la hausse de pénalité abaisse l'élan vers la triche et relève l'élan vers l'obscurcissement en proportion du taux de triche (dynamique, remarque sur le dilemme ; contre-lecture, défaut 3 : bascule possible hors des fenêtres) | dérivée initiale des taux de mention et de triche selon trois niveaux de pénalité | à taux de triche initial non nul, l'obscurcissement ne croît pas avec la pénalité | moyen |
| P5 | La normalisation par groupe ne change que l'horloge (proposition des avantages normalisés) | trajectoires des taux de triche, de mention et de capture, avec et sans normalisation, recalées en temps | les trajectoires recalées divergent au-delà du bruit entre graines | moyen |
| P6 | Sonde figée contre sonde réapprise : l'entraînement contre un filtre de texte déplace une sonde figée qui lit des activations partagées, tandis que la séparabilité (sonde réapprise) subsiste (découplage, théorème 2 et remarque) | aire sous la courbe d'une sonde linéaire figée avant l'entraînement et d'une sonde réapprise après, sur les mêmes épisodes | la sonde figée ne bouge pas alors que le filtre de texte est contourné, ou la sonde réapprise perd la séparabilité | faible en plus d'un bras existant (lecture d'activations) |

**Non réfutables par cette expérience** : les limites à pression infinie ; les seuils exacts (la pression effective n'est pas observable ; elle s'étalonne une fois sur le bras sans filtre, jamais par bras) ; l'invariance exacte sur neurones disjoints (un transformeur n'a pas de tête de texte à neurones séparés) ; les bornes du budget d'audit et de détection (mathématiques, vérifiées en Lean pour la partie combinatoire).

## 2. Trois contrastes proposés à Lazar (au plus trois, comme le recommande la demande approfondie)

1. **Contraste principal — rejet répété contre pénalité contre sans filtre (P1, avec P2 en mesure de première génération).** Variable principale : taux absolu d'épisodes trichés et non interceptés, pour mille, au dernier tour, en graines appariées. C'est la question de Halberstadt posée au vrai entraînement, et la sensibilité au modèle du rejet relevée par l'audit.
2. **Contraste secondaire — dose d'amorçage de l'obscurcissement sous pénalité égale (P3, P4).** Il teste la non-atteignabilité, qui est la nouveauté dynamique du papier, en fabriquant la masse furtive initiale par doses au lieu d'attendre son invention spontanée.
3. **Mesure adossée, sans bras propre — sonde figée contre sonde réapprise (P6)** sur les bras du contraste 1 ; P5 seulement si le devis le permet, en description.

**Contrôles** (communs) : filtre au hasard de même taux de rejet (enrichissement prédit nul) ; tâches sans avantage à tricher ; bras sans filtre. **Contrôle positif** : modèle amorcé à l'omission connue, que la chaîne de mesure doit détecter ; sinon l'essai est déclaré « non évaluable », pas négatif.

## 3. Ce qui reste à décider (par Lazar, après le devis)

- le nombre de contrastes effectivement financés (1, 2 ou 3) ;
- la taille du modèle (3B pour l'étalonnage, 7–8B pour le contraste principal) ;
- le plafond de l'étalonnage (premier étage du devis).
