# Vérification 1 de la différence entre le brouillon 2 et le brouillon 3 — préenregistrement de l'étude par simulation des formulations du contraste à témoin apparié de la porte de fin de phase 1 (G1)

- **Lecteur** : sous-agent neuf de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, Claude Sonnet 5.5 (`claude-sonnet-5-5`). Il n'a écrit ni le brouillon 1, ni le 2, ni le 3, ni aucune ligne de code ou d'essai, ni la contre-lecture 1 ou 2 (R2).
- **Date (UTC)** : 18 novembre 2026, vers 22:45.
- **Pièces relues, empreintes recalculées et égales à leurs compagnons** : brouillon 3 `prereg/formulation-g1-simulation-v1-brouillon3.md` `d20d605cc3661e0e12d93c13c99476594033069c59aae19aee0afbed6b59ebb5` ; liste des différences `prereg/pieces-formulation-g1-v1/differences-brouillon2-vers-3-v1.md` `183431e54f89b15020c198f3a0e82239d9d063077fc16f6aaf54afc18e73dac3` ; brouillon 2 `96cd0fa3342b9feb601be4aa46aa13bda53ae3b89284c1ce0f9329cf21b83af3` ; contre-lecture 2 `7635eb157bf5267701ad52ab61e9c9d226eb22f1fd77bc6e18c6e7e50d9024b8` ; `statistiques_v3.py` `0a2791c1…`, `mondes_v3.py` `095850c6…`, `simulation_v3.py` `1bd187b1…`, `lecture_v3.py` `043a439f…` (toutes égales à leurs compagnons et à l'en-tête du brouillon 3) ; les quatre fichiers d'essais `*_v3.py` (égaux à leurs compagnons) ; code de la v2 pour les différences (`diff`). Conception du pari lue par `git show 776a2be97:…/conception-pari-de-signe-v2.md` : empreinte recalculée `9c39a73d…`, égale à celle de l'en-tête ; lignes lues : 99 à 109, 120 à 151, 205 à 208, 320, 323, 325, 328 (rien d'autre ; la version 9 n'a pas été ouverte). Aucun chiffre mesuré du pôle recopié ici.
- **Essais rejoués** (`PYTHONPATH=src .venv/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=<scratchpad>/cl3bt/x tests/test_formulation_g1_*_v3.py`, dossier supprimé ensuite) : **105 réussis** en 118 secondes. `prereg.problemes` sur le brouillon 3 : **aucune remarque**.

---

## 1. Verdict : **scellable après ces couples exacts**

Les couples de la contre-lecture 2 sont appliqués en texte et en code, sans écart injuste. La lecture de la conception du pari est juste sur les trois points. Les quatre ajouts du rédacteur ne penchent pas de façon qui change l'issue, mais deux phrases du texte penchent ou surdisent (couples C2 et C3). Rien de bloquant : quatre couples de texte, aucun changement de code. Le choix de fond est remis à Lazar sans pente.

---

## 2. Les couples de la contre-lecture 2, un par un

**B′-1 (bloquant, pente vers C par les budgets du témoin) : appliqué, en texte et en code.**
- Règle 6, tableau de la grille, dénombrement : mêmes textes que la contre-lecture, avec 5 541 (3 888 + 648 + 36 + 468 + 486 + 15 = 5 541 : somme vérifiée ; 468 = 36 × 13 variantes, 486 = 9 × 6 × 3 × 3 à 400 tâches et témoin parfait).
- Bloc « budget du témoin égal » : `mondes_v3._budget_temoin` reproduit la fabrique du couple (calibrage honnête 12 000, calibrage du témoin 1 200, 400 tâches, trois épisodes, imperfection nulle) ; l'essai `test_bloc_budget_du_temoin_egal` vérifie que ses 486 mondes sont exactement ceux du bloc principal à 400 tâches et témoin parfait. `mesurer_temps` parcourt `BLOCS`, bloc compris.
- B2 restreint aux 100 tâches : `simulation_v3._lot` coupe `d_b2` à `ceil(300 / 3) = 100` tâches quand `episodes_garde` est écrit, et `empile` est retiré (le contraste de E et d'A′ garde 400 tâches). L'essai des largeurs (`(8, 34)` pour 34 tâches contre `(16, 60)`) et l'essai d'artefact `test_b2_restreint_change_la_decision` (un témoin qui ne sonne que sur les tâches 100 et suivantes : B1 lue sur 400 tâches refuse, sur 100 passe) couvrent le cas sain et l'artefact. La lecture par rééchantillonnage n'est pas touchée : `valider` refuse une garde partielle avec elle (contre-lecture 2, acceptée).
- `lecture_v3.verdict` : l'issue du bloc est comparée à celle du bloc principal à 400 tâches (`issue_budget_principal != issues[TACHES_REDUITES]`) et rendue avec sa table ; essais `test_bloc_budget_compare_au_bloc_principal_a_400_taches` (cas sain, artefact, bloc absent) et `test_dependances_de_l_issue`.
- **Ce que la moitié « A′ calibré sur 1 200 épisodes » peut et ne peut pas renverser** : le paragraphe neuf est juste dans son raisonnement. Elle ne change que A′ (seuil à 0,29 point d'écart-type au lieu de 0,57 : lois bêta vérifiées à la main, 0,574 / 0,287 / 0,091) ; elle ne peut pas renverser un « A retenue » sauf par le hasard des tirages, et le texte dit ce hasard (les 486 mondes du bloc sont des mondes nouveaux, de graines propres : E et B y sont retirés, non copiés ; le texte écrit « mêmes mondes, mêmes seuils honnêtes », vrai en loi, pas en tirage, et la phrase suivante le dit). Ce n'est pas un contrôle symétrique, et le texte le dit. Deux surdits subsistent : couple C3.

**M′-1 (unité de D-S9)** : remplacé par la confrontation, écart déclaré et juste (§ 3, point D-S9).
**M′-2 (conception introuvable, garde de D-S4)** : dépassé par la lecture de la conception ; écart déclaré et juste (§ 3, point D-S4).
**M′-3 (choix de fond)** : les deux puces, la phrase « 108 contre 6 … ne mesure aucune fréquence » et le point 1 sont ceux du couple, mot pour mot. L'ajout de la phrase sur la bande non couverte est neutre. Reste la ligne « Décision » (couple C1).
**m′-1, m′-2, m′-3** : appliqués. La phrase sur le second lecteur est exacte ; l'entrée « Contre-lecture 2 » porte ses deux empreintes ; l'en-tête dit que `__init__.py` nomme encore les modules de la v1.

---

## 3. La lecture de la conception du pari

- **D-S6, grille de mises : juste.** Lignes 99 à 105 : richesse d'une mise = produit de (1 + λ·v) ; richesse déclarée = **moyenne** sur Λ = {0,1 ; 0,3 ; 0,6 ; 0,9}, seuil 1/niveau, lecture continue ; lignes 107 à 109 : la mise prévisible est gardée en option ; ligne 325 : grille retenue. Le code (`_log_richesse` : `logaddexp` puis soustraction de log 4) calcule bien la moyenne, non le maximum.
- **D-S4, garde : juste.** Lignes 145 à 151 : second pari « sur les unités honnêtes de l'épreuve », sur g = f_A − f_B, nul « E[g] ≥ δ », facteur 1 + λ·(δ − g), même grille ; paliers 0,10 (70 unités), 0,05 (150), 0,03 (300), 0,02 écarté. Lignes 207 et 208 : nul réuni, e-valeur de la fiche = minimum des deux richesses, arrêtée au premier instant où il atteint le seuil ; ligne 323 : option retenue « en disant qu'elle ne borne que le grossier ». Elle est appariée entre **deux moniteurs, sur l'honnête** ; aucun témoin n'y entre ; les « jumeaux » (lignes 122 à 128) sont deux moniteurs de même loi. Le brouillon 3 le dit à l'endroit voulu et en tire la bonne conséquence : elle ne double pas B. Le code suit : `pari_avec_garde` rejette si le **maximum dans le temps du minimum** des deux log-richesses atteint log(1/α) ; la validité est sûre sur chaque membre du nul (le minimum est majoré par la richesse du membre vrai, Ville) ; `delta_de_garde` applique les paliers aux nombres de tâches. La garde est unilatérale (A alerte plus que B), comme dans la conception.
- **D-S9, unité du calibrage : juste.** Lignes 122 et 123 : C **unités** de m épisodes, erreur de quantile √(τ(1−τ)/(C·m)) ; lignes 140 et 141 : C de l'ordre de 10 à 16 fois le nombre d'unités sabotées ; ligne 328 : (a). Ici l'unité est la tâche (D-S1) de trois épisodes : C = 10 × 400 unités = 4 000 unités = **12 000 épisodes** à 400 tâches (18 000 à 600), et la lecture littérale en unités de dix épisodes (40 000) est dite non simulée, avec la réserve. Le brouillon 2 sous-dimensionnait de trois fois : la correction est juste. Les écarts-types du taux réel (0,57 ; 0,31 ; 0,29 ; 0,16 ; 0,09 ; 0,07) sont justes.
- **Non vérifié** (hors des lignes mandatées) : lignes 74 à 76, 84, 152 à 155 de la conception, et la version 9 (lignes 37, 38, 65) que le brouillon cite.

---

## 4. Les quatre ajouts du rédacteur : penchent-ils ?

1. **Garde de D-S4 codée dans le critère actuel et dans A.** Dans E, elle est commune à A et à B (B = E et B1 et B2) : neutre. Dans A′, elle est lue sur le témoin aux seuils du témoin ; ces seuils étant calibrés à 1 % sur le témoin, l'écart d'alertes attendu y est nul et seul le bruit des seuils (écart de 0,8 point au plus) peut la faire mordre, loin de δ = 0,03 à 0,10 : elle n'est presque jamais liante. Elle ne peut que retirer de la puissance à A (pente infime vers C) ou lui retirer des faux positifs (pente infime vers A) ; le texte dit qu'elle ne peut que retirer de la puissance et chiffre l'effet (`effet_de_la_garde`). Lecture juste du « critère actuel » : N-074 dit pour A « par la même statistique, au même niveau, sous la même règle ». **Ne penche pas.** Remarque hors couple : la composante B sans la garde n'est pas conservée (seules `E_sans_garde` et `A_prime_sans_garde` le sont) ; on ne peut donc pas rejouer la règle sans garde ; sans conséquence tant que la garde est presque vacuante, qui est ce que `effet_de_la_garde` rapportera.
2. **Garde comme second test sous les autres lectures** : « Student » et mise prévisible rendent `nu & test(gardes_reduites)`, avec `(δ − g)/(1 + δ)` dans [−1, 1] ; la conjonction de deux tests au même niveau est valide et prudente ; même forme pour E dans A et dans B. Le rééchantillonnage borne la moyenne de g au quantile 1 − α sous δ. **Ne penche pas.**
3. **Table de la puissance retirée par la garde** (`effet_de_la_garde`) : rapportée, hors règle, avec garde de câblage (arrêt si la garde ajoute des passages) essayée sur cas sain et artefact. **Ne penche pas.**
4. **Variante « calibrage du témoin à l'échelle de D-S9 » (12 000 épisodes)** : rapportée, hors règle ; neutre en soi. Deux phrases qui l'entourent ne le sont pas : couples C2 et C3.

---

## 5. L'essai dont la borne est passée de 20 à 18

`test_b2_restreint_change_la_decision` exigeait au départ que B1 lue sur 300 épisodes passe dans 20 répétitions sur 20 à un taux vrai de 1 % ; il en a rendu 19. La raison donnée (erreur de l'essai, non chiffre d'issue de la grille) est juste : la probabilité de passage par répétition est 0,996 (au plus 8 alertes sur 300 à 1 %), donc la probabilité de 20 sur 20 est 0,996²⁰ ≈ 0,92 : un échec sur douze environ ; celle de 18 sur 20 ou plus est supérieure à 0,999. Le monde est un monde d'essai à 20 répétitions, graine fixe, hors grille ; la borne 18 est une marge pour une loi binomiale, non l'observation ajustée, et elle ne laisse passer aucun défaut que l'essai cherchait (l'autre moitié, `comptes[0] == 0`, reste exacte). Déclaré à la déclaration 2. **Juste, sans ajustement à une issue.** Remarque hors couple : les bornes « ≥ 19 » de `test_garde_appariee_dans_e_et_dans_a_prime` sont de même nature (puissance proche de 1 sur un monde d'essai) et ne sont pas mentionnées à la déclaration 2.

---

## 6. R5, R9, durée

- **R5** : chaque garde neuve a un cas sain et un artefact (tolérance δ hors de ]0, 1[, unités non appariées, écart hors de [−1, 1], moins de deux unités, minimum au même instant, B2 restreint, garde sur l'honnête qui sonne, garde de câblage `effet_de_la_garde`).
- **R9** : `_generateurs` inchangé ; les épisodes honnêtes de l'épreuve sont tirés après ceux des sabotés et du témoin, dans le même générateur du monde ; reproductible.
- **Durée** : un lot de 300 répétitions à 400 tâches, calibrage honnête 12 000 (un monde du bloc principal, sorties jetées, aucune issue lue) : 0,8 seconde ; sept lots par monde font de l'ordre de 6 secondes ; 5 541 mondes sur quatre cœurs : de l'ordre de 2 à 3 heures, d'accord avec l'estimation du brouillon, sous le plafond de six heures.

---

## 7. Le choix de fond remis à Lazar

Sans recommandation ni défaut, avec avantage et inconvénient pour chaque option, et la phrase sur la grille (108 contre 6). Aucune pente détectée dans les puces. Seule la ligne « Décision » parle encore de « l'un des deux comportements » : le rédacteur l'a vu (liste des différences, § 5) ; couple C1.

---

## 8. Couples exacts

**C1. Ligne « Décision » de la section « Choix de fond remis à Lazar ».**
- Avant : « **Décision** : accepter, dans le critère ajouté à la porte, l'un des deux comportements que la simulation chiffre et que la règle ne juge pas. »
- Après : « **Décision** : dire lequel des deux critères, la garde (B, donc C) ou le contraste (A), porte la porte de fin de phase 1 ; leurs deux comportements sont ceux que la simulation chiffre et que la règle ne juge pas. »

**C2. Point 8 des « Points portés à Lazar » (penche vers A).**
- Avant : « … c'est un poste du devis de la couche 2, non une propriété de la formulation. »
- Après : « … c'est un poste du devis de la couche 2 que A porte et que B ne porte pas (B lit au plus 1 200 ou 1 800 épisodes du témoin) ; que ce coût compte ou non comme propriété de la formulation est à Lazar : l'étude ne le tranche pas. »

**C3. Deux surdits sur le sixième rejeu.**
- Paragraphe « Budgets d'épisodes du témoin, dits », avant : « Deux contrôles égalisent : le **bloc « budget du témoin égal »** … ; la variante « B sur 300 épisodes du témoin » (B1 et B2 lues sur 100 tâches). »
  Après : « Deux contrôles réduisent l'écart de budget, sans l'annuler : le **bloc « budget du témoin égal »** … égalise le total des épisodes du témoin consommés (1 200 de part et d'autre), non ceux qui fixent les seuils (1 200 pour A′, 12 000 honnêtes pour B) ; la variante « B sur 300 épisodes du témoin » (B1 et B2 lues sur 100 tâches) ramène B à son minimum. »
- Paragraphe « Ce que la règle peut encore devoir à sa construction », avant : « Le sixième rejeu garde cette pente, sur les mondes mêmes où elle agit ; le rédacteur ne sait pas dire d'avance quelle issue sort. »
  Après : « Le sixième rejeu éprouve cette pente sur les mondes mêmes où elle agit, sans l'annuler : à 1 200 épisodes le bruit des seuils d'A′ (0,29 point) reste le triple de celui de B (0,09 point) ; une issue qui ne tient qu'à l'échelle de D-S9 se lit dans la variante rapportée « calibrage du témoin à l'échelle de D-S9 », sur les mondes réduits et hors règle, que la note donne à côté de l'issue ; le rédacteur ne sait pas dire d'avance quelle issue sort. »

**C4. « Ordre » et « Contre-lecture ».**
- Section « Ordre », avant : « … lecture par un lecteur neuf avec `lecture_v3.verdict`, contrôles de validation d'abord ; … »
  Après : « … lecture par un lecteur neuf avec `lecture_v3.verdict`, contrôles de validation d'abord, puis, pour chaque variante rapportée du bloc des sensibilités (dont « calibrage du témoin à l'échelle de D-S9 »), `lecture_v3.indicateurs(mondes, 400, "pari", bloc="sensibilites", etiquette=…)` : `verdict` ne les tabule pas ; … »
- Section « Contre-lecture », ajouter après l'entrée « Contre-lecture 2 » : « **Vérification 1 du brouillon 3** (R2) — sous-agent neuf, Claude Sonnet 5.5 (`claude-sonnet-5-5`), qui n'a écrit aucune pièce de l'étude ni aucune contre-lecture. Brouillon relu : `prereg/formulation-g1-simulation-v1-brouillon3.md`, `d20d605cc3661e0e12d93c13c99476594033069c59aae19aee0afbed6b59ebb5`. Rapport : `prereg/contre-lectures/formulation-g1-simulation-v1-brouillon3-verif1.md`, empreinte au compagnon `.sha256`. Verdict : « scellable après ces couples exacts » ; quatre couples de texte, aucun de code. » Et remplacer le paragraphe « À venir (R2) » par la mention que cette vérification est faite.

---

## 9. Hors couple (rapporté, non exigé)

- La règle 6 écrit « B à 300 épisodes du témoin », le reste du texte et le code « B sur 300 épisodes du témoin » : unifier au texte final (le couple de la contre-lecture 2 portait la première forme).
- À 50 tâches (bloc des effectifs), δ = 0,10 s'applique à moins de 70 unités, ce que la conception ne couvre pas (palier « 0,10 avec 70 ») ; la garde y est presque vacuante dans le modèle ; sans effet sur la règle (effectifs 400 et 600).
- Réserve sur l'unité de trois épisodes pour les paliers de δ : la conception les a établis pour des unités de dix épisodes ; le texte porte la réserve pour D-S9, non pour δ.
- La prédiction P8 (« plus de 5 % » sous Student) : l'ordre de grandeur est juste (taux de rejet de 5,5 à 11 % pour un rapport bruit du seuil sur erreur type de 0,7 à 1,3 ; le texte dit « 6 à 9 % ») ; sa fourchette est celle du rédacteur, non vérifiée par tirage, comme dit.

## 10. Lectures hors mandat et limites

- Hors des fichiers listés, ouverts : `docs/decisions/decision-N-074-v1-brouillon2.md` (lignes 14 à 53 et 76 à 99, pour la définition de A et de B) ; `src/controle_ia/formulation_g1/mondes_v2.py` et les essais de la v2 par `diff` seulement.
- **Rien ouvert** sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/`, `registres/`. Aucun résultat d'étude cloisonnée. Simulation complète non lancée ; un seul lot de 300 répétitions d'un monde du bloc principal a servi à mesurer une durée, sortie jetée sans lecture. Ni commit ni poussée. Seuls fichiers écrits : ce rapport et son compagnon.
- Un fichier temporaire de la conception (`/tmp/claude-0/cp2.md`) a été créé pour lire les lignes citées et supprimé ensuite.
