# Erratum 1 au préenregistrement « sabotage ou empreinte, adaptateurs tenus à l'écart » (barreau 5), version 1

- **Texte visé** : `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md`, sha256 `bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935` (recalculée, conforme), ligne 323.
- **Auteur** : rédacteur neuf, Claude Fable 5.2 (`claude-fable-5-2`), qui n'a écrit ni le texte visé, ni le programme de lecture, ni le verdict.
- **Date** : 2026-11-24T12:11:09Z (`date -u`).
- **Classe** : A, pièce décisive de forme fixée (erratum court). Accord : `GO-2026-11-24-21`, point 12.
- **Lu** : du texte visé, les lignes 181 à 199 (section « Seuil ») et la ligne 323, rien d'autre ; la table des six et des sept familles du bloc K de la simulation de puissance ; la fonction `seuil_rangs_signes` et la constante `NIVEAUX` du programme de lecture figé ; la ligne EPREUVE-B5F du registre propre. Aucun résultat, aucun verdict, aucun score ouvert.

## Passage tel qu'il est (ligne 323, à la lettre)

> Les mêmes épreuves sont lues au niveau déclaré de **95 % bilatéral** (à sept familles : somme des rangs contraires d'au plus 2 ; à six : aucune ; bloc K), et l'issue porte ce niveau dans son nom et dans sa phrase (« sabotage, au niveau de 95 % »).

## Passage corrigé (à la lettre)

> Les mêmes épreuves sont lues au niveau déclaré de **95 % bilatéral** (à sept familles : somme des rangs contraires d'au plus 2 ; à six : 0, les six différences du même côté, probabilité exacte 1/64 par sens ; bloc K), et l'issue porte ce niveau dans son nom et dans sa phrase (« sabotage, au niveau de 95 % »).

Seuls les mots « à six : aucune » changent ; le reste de la ligne 323 et du texte est inchangé.

## Pourquoi

Dans la table de la section « Seuil » (lignes 185 à 191), le mot « aucune » de la colonne w(K) veut dire « aucune somme admissible », niveau non atteignable (sept et six familles à 99 %, zéro attribution admise). Lu de même à la ligne 323, « à six : aucune » dirait que 95 % bilatéral n'est pas atteignable à six familles, ce qui est faux et contredit trois pièces :

1. la source citée par la ligne elle-même, le bloc K : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/sortie-simulation-puissance-adaptateurs-tenus-a-l-ecart-v3.json`, sha256 `1b0cf4cde2baf6d6dcb11b807f4fb84e70c72fdb0ded228eb1396836e6a14f7d` (recalculée, conforme), clé `K_plan_retenu_rangs_signes.tables.6_familles` : `somme_des_rangs_contraires_admise_95: 0`, `p_un_sens_au_seuil_95: 0.015625`, `niveau_bilateral_le_plus_fort_atteignable: 0.96875` ;
2. le programme de lecture figé, `src/controle_ia/barreau5_familles/lecture_v1.py` au commit `c76e79169eee337ce66c7d88f62d039e853eebfc`, sha256 `ed0999df49aedb52099bb848803c3049a8ba09db2a46ce3df9230d3e7b25626f` (recalculée, conforme) : `seuil_rangs_signes` rend la plus grande somme w telle que P(W ≤ w) ≤ 1/40 par sens, soit 0 à six familles et 2 à sept ; `niveau_de` lit à 95 % dès six familles ;
3. la phrase qui suit dans la même ligne 323, « Sous six familles : issue N, motif "niveau non atteignable" », qui place le défaut de niveau sous six familles et non à six.

Lu comme « aucune somme contraire admise », soit 0, le passage rejoint la source et le programme : il était au mieux ambigu. L'erratum fixe cette lecture.

## Portée

Aucune hypothèse, prédiction, métrique, seuil appliqué, critère de lecture, épreuve ni liste d'arrêt ne change. Le programme de lecture figé appliquait déjà la valeur corrigée, et l'épreuve à vérité plantée passée (ligne EPREUVE-B5F de `registres/barreau5-familles-jumelles-v1.md`, lecture sha256 `ed0999df…`) l'a jouée avec ce programme. Selon la mère, qui relaie le relevé du juge du verdict, toutes les épreuves de la lecture faite avaient dix familles : la règle des six familles n'a alors joué nulle part, et la lecture faite n'est pas touchée (point non vérifié par le rédacteur, qui n'ouvre aucun résultat). Le texte scellé reste tel quel, sous son nom et son empreinte (R12) ; il se lit désormais avec cet erratum, qui prime sur les seuls mots corrigés.

## Vérification

Énumération exacte des 2^K attributions de signes aux rangs 1 à K, seuil 0,025 par sens (`calcul_rangs_signes.py`, à côté de cet erratum) : à six familles, 64 attributions, P(W ≤ 0) = 1/64 = 0,015625 ≤ 0,025 et P(W ≤ 1) = 2/64 = 0,03125 > 0,025, donc w(6) = 0 ; à sept familles, 128 attributions, P(W ≤ 2) = 3/128 = 0,0234 ≤ 0,025 et P(W ≤ 3) = 5/128 = 0,0391 > 0,025, donc w(7) = 2. Accord avec le bloc K et avec le programme figé.
