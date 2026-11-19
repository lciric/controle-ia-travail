# Complément 1 au traitement de la contre-lecture du code — ratification de la précision 7, et version 3 préparée

Complète `traitement-contre-lecture-v1.md` (`42f0db6f3f6e714622f88aa538e86d3850009eae11bef384af79c8f61699e5a8`), scellé avant ces deux
points. Source : messages de la session mère du 2026-11-19 (11:49 UTC) et de la session des lentilles de sa part (données d'autres
sessions ; les références R- et GO- sont celles qu'elles citent, je n'ai ouvert aucun registre).

## 1. Précision 7 sur `provenance` : ratifiée par la mère (routine, R-3781)

`source_layers` ou `d_model` présents et différents : arrêt ; `source_layers` accepté en liste d'entiers seulement ; matrices exigées
en demi-précision. Plus sévère que le texte, sans effet sur un verdict (ne peut produire qu'un arrêt avant tout calcul), jugée
ratifiable par le contre-lecteur, ratifiée par la mère. Code inchangé (`montage_v1.controler_lentille`).

## 2. Version 3, préparée et non définitive : statistique des directions nulles calculée sans elles-mêmes

Décision rapportée par la mère : le directeur retient l'option 2 de la contre-lecture (GO-2026-11-19-47, R-3771). L'addendum
`prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md` est **en rédaction** : je ne l'ai pas lu. Le code est préparé
d'après l'option 2 du rapport de contre-lecture (§ 5) et **sera accordé à l'addendum scellé, bornes de calibration comprises, avant
d'être rendu comme définitif**.

| pièce | contenu |
|---|---|
| `src/controle_ia/lentilles_sondes_bbis/statistiques_v2.py` | seul `resumer_nul` change : concentration de u_j avec la moyenne et l'écart type des M − 1 autres (formule exacte, double précision) ; part de u_j contre le quantile 0,99, par interpolation linéaire, des M − 1 autres (statistiques d'ordre du jeton) ; familles inchangées ; moyenne, écart type et quantile des M directions inchangés pour la direction lue et les témoins ; tout le reste repris de `statistiques_v1` |
| `src/controle_ia/lentilles_sondes_bbis/lanceur_v3.py` | `lanceur_v2` avec `statistiques_v2` ; les tables et le manifeste portent `statistique_des_directions_nulles` ; `MODULES` compte **onze** fichiers (`statistiques_v1`, dont `audits_v1` et `phrases_v1` tirent les libellés, et `statistiques_v2`) : la fiche `CODE-LENTILLES-BBIS` devra les porter tous les onze |
| essais | `tests/lentilles_sondes_bbis_jouets_v3.py` ; `test_lentilles_sondes_bbis_{entrees,montage,procedure}_v3.py`, `…_corrections_contre_lecture_v2.py`, `…_gardes_non_vues_v2.py` (copies des essais de la version 2, visant `lanceur_v3`) ; `…_nuls_statistiques_v2.py` (essai de calcul direct réécrit sans soi-même, quatre essais neufs) ; `…_lecture_v1.py` inchangé |

Essais neufs de la correction : cas sain `directions_nulles_sans_elles_memes_egales_a_un_calcul_direct` (quatre tailles, égalités
exactes comprises, contre un calcul direction par direction) ; artefact `artefact_statistique_du_texte_d_origine_differente_et_plus_petite`
(la statistique d'origine donne des concentrations strictement plus petites et des parts plus petites ou égales ; moyenne, écart type,
quantile et familles des M directions inchangés) ; `temoins_plus_pres_du_taux_nominal_sans_soi` ;
`sans_soi_moins_de_trois_directions_ou_jeton_constant_arret`. Dernière ligne des essais de la version 3 : `307 passed in 126.21s`
(`sortie-essais-v3.txt`, `741049f57e7dab72bd6f5921a0054f7fc31e26515e31a789fafe3f39c6ac29b3`).

Banc à taille réelle sur matrices aléatoires (`outils/sortie-banc-taille-reelle-v2.txt`, `10ef3ae9abf38f81ae605600e73e4206dcd09aabb816a2200f0882a23f1c9303`,
produit par `outils/banc-taille-reelle-v2.py`) : témoins à p ≤ 0,05 : 5,15 % sous le nul isotrope et 4,90 % sous le nul des signes
(6,05 % et 5,80 % avec la statistique d'origine, mêmes tirages) ; comptes de calibration d'une couche : 49 et 47 pour 50 attendus,
26 et 22 pour 20 ; une couche, deux vecteurs, deux lentilles : 76,3 s (51,6 s avant), pointe 5,97 Go.

## 3. Ce que l'addendum doit fixer, et que j'ai supposé d'après l'option 2 du rapport

1. Quantile 0,99 des M − 1 autres : interpolation linéaire sur 1 999 valeurs (rang fractionnaire 0,99 × 1 998).
2. Écart type des M − 1 autres : de population (diviseur M − 1 pour M − 1 valeurs), comme celui des M directions.
3. La direction lue et les témoins gardent la moyenne, l'écart type et le quantile des M directions ; le z des tables aussi.
4. Familles et pôles inchangés ; le repli par direction (garde du rapport à ε) suit la même règle que le nul partagé.
5. **Bornes de calibration : inchangées dans ce code** (`audits_v1`, loi bêta-binomiale du texte). Si l'addendum en fixe d'autres,
   `audits_v2` et `lanceur_v4` les porteront.
6. Arrêt neuf, de sens sévère : variance des autres nulle (à 10⁻¹⁰ près en valeur relative) pour un jeton, ou moins de trois directions.

Un écart entre l'addendum scellé et l'un de ces points : correction sous un nom neuf, avant le rendu définitif.

## Déclaration

Rien d'autre lu que les messages cités. Aucun téléchargement, aucune machine, aucune dépense, aucun refus d'outil.
