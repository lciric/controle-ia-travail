# Contrôle différentiel de l'erratum v5 et du devis v8 — v1

- Auteur : vérificateur du programme de vérification de la sortie des mondes, modèle S. Écrit le 2026-11-21. Aucun appel, aucune clé, aucune dépense, aucun commit, aucun refus de permission.
- Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verif-verification-sortie-mondes/` ; copies dans `v8/`.

## 0. Verdict

1. **Devis v8 : Conforme, prêt à sceller.**
2. **Erratum v5 : À corriger, trois précisions d'une phrase chacune** (§ 1). E2 est corrigé. E1 suit ma proposition et le mot de la mère tel que relayé ; la glose et le renvoi de la casse et des accents au programme sont justes. Mais trois ambiguïtés restent dans la règle elle-même. Si la mère préfère ne pas rouvrir l'erratum, elle peut écrire ces trois précisions dans la demande de la version 3 du programme de vérification et dans son rapport : l'erratum fait déjà ce renvoi pour la tolérance, la casse et les accents. Dans ce cas, le devis v8 se scelle tel quel avec l'erratum v5 ; sinon une version v6 de l'erratum impose un devis v9, sans autre changement.
3. Texte servi v3 : inchangé, `f3d87162…` (recalculé).

## 1. Erratum v5

Empreintes égales à la table `089c2635…` (elle-même égale à son compagnon) : erratum `2051450a…`, devis `53b6b99f…`, programme `81c9904c…`, sortie `aacab5d6…`.

**E2 corrigé.** La ligne des passes antérieures est réécrite sans le marqueur gras errant ; les marqueurs de la ligne « Version » sont appariés.

**E1.** Le § 3 écrit : (a) écarter les clés dont le nom contient « couverture », « taux » ou « probabilite » ; (b) s'il reste une seule clé, c'est elle ; (c) à défaut, s'il existe une unique clé dont le nom contient « decalage » ou « derive », c'est elle ; (d) sinon F est écartée. Puis le contrôle de cohérence : le décalage lu triple le taux de 1 % sous la loi honnête de l'auteur pour F, sinon F est écartée. Et : F écartée ne rend pas la sortie illisible, sans second essai.

- **Glose du rédacteur** (« le seuil dont le taux vrai est de 1 % avant la dérive doit avoir un taux vrai de 3 % après elle ») : **juste.** C'est la définition de T09 dans la table du § 3.1 du mandat (« décalage qui triple un taux de 1 % ») : la loi de calibration fixe le seuil au taux de 1 % ; la loi d'usage est la même loi décalée du décalage lu, en écarts types ; le taux au même seuil doit valoir 3 %.
- **Casse et accents laissés au programme** : **juste de le dire, et le programme v3 doit les fixer en écriture.** Je demande : comparer après repli en minuscules et suppression des accents (le programme le fait déjà pour les noms de familles et les suppositions), par sous-chaîne ; l'écrire dans le rapport du programme et dans le compte rendu de la correspondance.

**Les trois ambiguïtés qui restent (à lever par une phrase) :**
1. **Étendue de l'étape (c).** « Une unique clé dont le nom contient decalage ou derive » : parmi toutes les clés de `valeurs_de_plus`, ou parmi celles que l'étape (a) a laissées ? Cas {« couverture_sous_derive », « decalage_x », « autre_y »} : après (a), deux clés restent, donc (b) échoue ; (c) donne « decalage_x » si on cherche parmi les clés restantes, et deux clés (donc F écartée) si on cherche parmi toutes. À écrire : parmi les clés laissées par (a).
2. **Quelle loi pour le contrôle.** F a trois tranches, chacune avec sa loi honnête. « La loi honnête que l'auteur écrit pour F » ne dit pas laquelle. À écrire : la loi de la tranche que la correspondance associe à T09 (celle dont `n_calibration` contient 299, à défaut la première), ou : chaque tranche.
3. **La tolérance.** « À la tolérance du programme de vérité » : le programme de vérité en a deux, 10⁻¹² (évaluation des fonctions de répartition) et 10⁻³ (`SEUIL_ECART`, § 6 point 4). À 10⁻¹², un décalage écrit avec quatre décimales (erreur de l'ordre de 3·10⁻⁶ sur le taux) serait refusé : F serait écartée dans presque tous les cas. À écrire un seuil qui ne le fasse pas, par exemple 10⁻³ sur le taux de 3 %, comme le seuil du point 4 du § 6.

Ces trois points ne changent aucun montant ni le texte servi.

## 2. Devis v8

- **Rejeu du programme v8 deux fois** : `cmp` muet entre les deux, et avec la sortie livrée `aacab5d6…`.
- **Seuls la version et la référence à l'erratum changent.** Sortie v7 contre sortie v8 : une seule ligne, le champ « version ». Programme v7 contre v8 : le titre, l'usage, un commentaire de tête, le champ « version » ; aucune formule. Devis v7 contre v8 : huit lignes (titre ; auteur ; version ; ligne de calcul ; ligne E1 de la table des sources ; la mention du § 3 ; la ligne de GO ; la réserve 1), aucune ne porte un nombre de calcul.
- **La ligne de GO nomme** le texte servi `f3d871628d489f45cb2afc09584f63d5fa49f4208f1b736c842ce3d4c0741008` et l'erratum, cinquième passe, `2051450a7a3fe2c28a938277d5b51c310b8c071bc01a884ba3d303d0b11594b9`, en 64 caractères, égales aux fichiers. Plafond par essai 2,15, montant 4,30 : inchangés. La ligne E1 de la table des sources porte la même empreinte de l'erratum v5.
- **Aucun nom de modèle ni de fournisseur** dans le devis v8, son programme, sa sortie et l'erratum v5.

## 3. Réserves

Le taux de 2,227 reste non vu. Les trois précisions du § 1 sont aussi à porter au programme v3 avec ses corrections D1 à D3 de ma vérification de la v2.

vérificateur du programme de vérification de la sortie des mondes, modèle S
