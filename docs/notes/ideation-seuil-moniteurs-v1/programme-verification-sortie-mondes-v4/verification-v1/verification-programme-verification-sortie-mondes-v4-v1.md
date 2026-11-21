# Vérification du programme de vérification de la sortie des mondes, v4 — v1

- Auteur : vérificateur du programme de vérification de la sortie des mondes, modèle S. Écrit le 2026-11-21. Aucun appel, aucune clé, aucune dépense, aucun commit, aucun refus de permission.
- Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verif-verification-sortie-mondes/` ; copie du livrable : `livrable4/` ; mes sorties : `mes_essais/sorties-v4/`, `mes_essais/variantes-v4/`.

## 0. Verdict : Conforme, peut être cité

R1 et R2 sont corrigés. Le rapport v4 se lit seul, dit ce qui est vrai (le contrôle de la dérive de F n'est fait par aucun programme aujourd'hui) et peut être cité tel quel par la mère, à condition qu'elle reprenne cette phrase du rapport et non seulement la ligne « contrôle par le programme de vérité v2 » (§ 3).

## 1. Empreintes et essais

Table `d95b258c…` égale à son compagnon et au recalcul ; programme `7b4e04a1…`, essais `a452b52e…`, rapport `f135edc6…`, rapport de la sortie factice, entrée de recalcul et son compte rendu, rejeu, différentiels : égaux à la table. **316 essais passés** sur ma copie. Je n'ai pas relu les 110 mutations une à une ; j'ai lu les essais de R2 (plusieurs tranches) et sa mutation.

## 2. R1 et R2

**R1.** Le compte rendu de correspondance porte, sur mon essai (sortie à décalage lu), `controle.par` = « programme de vérité v2, mode --recalculer » et `controle.fait_par_ce_programme` = false. Le § 2 du rapport est corrigé : « Ni ce programme, ni le programme de vérité scellé. La v3 de ce rapport disait à tort… Tant que cette v2 n'est pas scellée et jouée, le contrôle n'est fait par personne ». La réserve 2 (§ 10) le redit. Le bloc `derive_de_F` porte tout ce que demande le contrôle : `temoin` « T09 », `n_du_temoin` 299, `rang_de_la_cle`, `valeur_transmise` (texte du nombre), `unite_du_decalage` (« écarts types de la loi de la tranche associée à T09 »), `tranche_associee_a_T09` (`rang`, `n_calibration_contient_299`, `rangs_des_tranches_a_299`, `regle`), `loi_de_la_tranche` et son format, et `controle` (`critere` complet, `taux_de_depart` « 0.01 », `taux_vise` « 0.03 », `tolerance` « 0.001 », `nature_de_la_tolerance` « absolue », `par`, `fait_par_ce_programme`). Le nom de la clé n'est pas recopié.

**R2.** La tolérance est écrite absolue, dans l'intervalle [0,029 ; 0,031] (§ 2 du rapport, « le taux doit donc tomber dans… »), comme le seuil du point 4 du § 6, et portée au compte rendu. Le cas « plusieurs tranches à 299 » se règle par la première (code l. 1565 et suivantes), signalé par `rangs_des_tranches_a_299`, avec un essai (`test_correspondance_plusieurs_tranches_a_299` : première retenue, rangs [2, 3] signalés) et une mutation (la dernière prise au lieu de la première). Conforme.

## 3. Le rapport peut-il être cité tel quel ?

**Oui**, avec une attention de rédaction pour la mère : le compte rendu écrit `par` = « programme de vérité v2, mode --recalculer », un programme qui n'existe pas encore ; seul le rapport (§ 0, point 1 ; § 2 ; § 10, réserve 2) dit que le contrôle n'est pas fait aujourd'hui. Dans sa pièce de scellement, la mère doit donc citer la phrase du rapport (« tant que cette v2 n'est pas scellée et jouée, le contrôle n'est fait par personne »), et non seulement le champ. Je ne demande pas de correction du programme ; si elle le souhaite, un champ d'état dans le compte rendu (par exemple « non fait tant que… ») éviterait toute lecture hâtive du compte rendu seul.

Deux autres points du rapport, justes : la remarque sur les noms contenant « taux » (§ 2, effet de la règle de la mère) et la remarque 8 du § 8 (unité des décalages du saboteur : l'écart type, lecture à déclarer par la mère ; ni le texte servi ni la conception ne la disent). Une référence à vérifier par la mère : le rapport cite ma vérification de la v3 sous `…/programme-verification-sortie-mondes-v3/verification-v1/…` (empreinte `6dce2dc0…`, exacte) ; le chemin est celui où ma pièce doit être versée.

## 4. Le différentiel ne touche que le compte rendu et le texte

Oui. Différentiel du programme v3 → v4 lu en entier : le nom et la version, le texte de tête, trois constantes (dont une neuve, `TAUX_DE_DEPART_DE_LA_DERIVE`, et un commentaire), un commentaire de la fonction de lecture, et le bloc `derive_de_F` du compte rendu. Aucune règle de vérification ne change. Preuves par l'exécution : mes 39 sorties donnent un fichier de résultats **identique à l'octet** à celui de la v3 ; mes 28 variantes (budget, témoins à 40 et 41, imbrication, formes de `valeurs_de_plus` de T09) donnent la même sortie de vérification qu'en v3 ; le rejeu du développeur est identique à l'octet à celui de la v3 (`f55d0327…`). La correspondance sur ma variante à décalage lu : 29 témoins convertis, 4 non convertis, comme en v3.

## 5. Noms et clés

Aucun nom de modèle ni de fournisseur, aucun préfixe de clé en clair dans le programme, les essais, le rapport et les fichiers non différentiels (seulement des chemins de dossier).

## 6. Réserves

1. Je n'ai pas relu les 110 mutations ni le différentiel des essais ligne à ligne ; j'ai rejoué les 316 essais. 2. Le contrôle de la dérive de F attend le programme de vérité v2. 3. L'unité des décalages du saboteur attend une lecture déclarée de la mère.

vérificateur du programme de vérification de la sortie des mondes, modèle S
