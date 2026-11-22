# Rapport de code — le hasard du défenseur comme preuve, version 2 (classe B, instrument)

- Spécification : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-1-hasard-du-defenseur-v3-consolidee.md`. Son empreinte 772661834859… est vérifiée.
- Contre-lecture portée : `docs/notes/chantiers-21-novembre-v1/code-v1/contre-lecture-code-hasard-defenseur-opus-v1.md`. Son empreinte ebc0f5266203… est vérifiée. Verdict : « conforme après corrections », 3 constats importants et 9 mineurs.
- Rapport précédent : `docs/notes/chantiers-21-novembre-v1/code-v1/rapport-code-hasard-defenseur-v1.md`. La version 1 (paquet, essais, script, rapport, sortie) reste scellée et n'a pas été touchée.
- Développeur : Claude Opus 5.5, sous-agent. Le travail porte sur des mondes simulés seulement : aucun modèle, aucun réseau, aucun commit.

## Phrase sur le pire cas (décision 3)

J'ai vérifié le GO moi-même : `git show origin/main:registres/go.md | grep GO-2026-11-22-57` renvoie la ligne datée du 2026-11-22, qui contient « les quatre nœuds des chantiers du 21 « go » ». Je ne l'avais pas trouvée en version 1, parce que je cherchais dans les registres de la branche de travail et non sur `main`.

Phrase de la spécification, § 5, mot pour mot. Elle est aussi écrite dans la docstring de `src/controle_ia/hasard_defenseur_v2/__init__.py` :

> **Conséquence, sous supposition** (pièce d'audit indépendante de la condition, dommage total fixé, régime de signature, premier ordre) [CALCUL]. À dommage total fixé, l'union des deux détections est minimale à λ = 1, où elle vaut l'audit seul. Sous ces suppositions, le test ne relève pas le pire cas ; il rend la stratégie conditionnelle dominée.

J'ai omis la phrase qui suit dans la note (« Cette phrase reste dans cette note jusqu'à la décision 3 du directeur… »). C'est la consigne de garde, levée par le GO ; elle ne fait pas partie de l'énoncé.

## Fichiers neufs

Tous sont scellés par leur `.sha256`.

- **Paquet** `src/controle_ia/hasard_defenseur_v2/` : `__init__.py`, `erreurs_v2.py`, `registre_v2.py`, `permutation_v2.py`, `monde_v2.py`, `contraste_v2.py`, `gardes_v2.py`, `puissance_v2.py`, `audit_v2.py`, `inventaire_v2.py`. Ce sont les modules de la v1, renommés en `_v2`, avec les corrections ci-dessous. Les chaînes de version des fichiers écrits deviennent « …-v2 ».
- **Essais** `tests/test_hasard_defenseur_v2_{registre,permutation,monde,contraste,gardes,puissance,audit,inventaire}.py` : ceux de la v1, sur le paquet v2. S'y ajoute `tests/test_hasard_defenseur_v2_complements.py` : les six essais de l'annexe, et un essai pour chacun des constats 4 et 5.
- **Script** `scripts/simulations_hasard_defenseur_v2.py`.
- **Rapport** : ce document.

## Sort de chaque constat

| # | Gravité | Sort | Ce qui est fait |
|---|---|---|---|
| 1 | important | porté | essai `test_g2_artefact_registre_rescelle_conditions_echangees` (annexe) |
| 2 | important | porté | essai `test_p_tirage_phipson_smyth_et_exacte` (annexe) |
| 3 | important | porté | essai `test_g7_maximum_conjoint_egal_au_calcul_a_la_main` (annexe) |
| 4 | mineur | porté | `contraste_v2.stat_studentisee` : la ligne `var = np.where(var <= 1e-12 * np.maximum(1.0, s2 / k), 0.0, var)` est insérée, mot pour mot, et la docstring le mentionne ; essai `test_constat_4_variance_d_arrondi_tenue_pour_nulle`, où l'exemple donne (0,977 − 0,3)·10⁶ = 677 000 |
| 5 | mineur | porté | `registre_v2.rejouer` et `gardes_v2.controler_ordre` : « entropie révélée : un entier seul », mot pour mot ; `RefusGraine` importé dans `gardes_v2` ; essai `test_constat_5_entropie_revelee_entier_seul`, qui refuse `[ENT, 0]`, `[ENT]`, `np.int64` et `True` |
| 6 | mineur | porté | essai `test_perception_absente_refusee_meme_sans_rejet` (annexe) |
| 7 | mineur | porté | essai `test_g5_sain_contre_le_jumeau_sensible` (annexe) |
| 8 | mineur | porté | essai `test_g2_graine_partagee_refusee_par_le_registre` (annexe) |
| 9 | mineur | porté, sans code (comme le demande le constat) | à écrire dans le futur préenregistrement court : « `tirages_du_plan` est appelé avec `simulation=False` ; B = 9 999 » |
| 10 | mineur | porté | ligne ajoutée à « Ce qui n'est pas écrit », ci-dessous |
| 11 | mineur | **renvoyé au concepteur**, non porté | voir la liste plus bas |
| 12 | mineur | porté | docstring de `registre_v2.verifier_engagement` : « Sans `entropie_revelee`, la garde ne vaut que si l'empreinte de l'engagement est comparée à celle publiée (commit du dépôt) avant la course. », mot pour mot |

Les six essais de l'annexe sont portés mot pour mot. Seuls changent les imports, de `hasard_defenseur_v1`/`*_v1` à `hasard_defenseur_v2`/`*_v2`.

L'essai du constat 4 ne reprend pas le chiffre 676 856,4 de la contre-lecture. Avec k = 2, Z sous E vaut (0,3 ; 0,3) et Z sous U vaut (0,977 ; 0,977). Le numérateur vaut alors 0,977 − 0,3 = 0,677, et la règle du dénominateur nul donne 677 000. L'essai vérifie cette valeur, qui passe. Je ne tranche pas l'écart avec le chiffre cité, que le contre-lecteur pourra revoir.

## Points renvoyés au concepteur (non portés)

- **Point ouvert 6** : lecture du cas où p_S rejette sans perception établie. Le code refuse toujours ce cas (`RefusLecture`).
- **Point ouvert 8** : composition de la famille de G7 (l'omnibus en fait-il partie ?) et sens du test (bilatéral ou non). L'appelant passe toujours la famille, sans défaut.
- **Point ouvert 12, en partie** : la règle qui passe du nombre de tâches à k et N. Elle n'est toujours pas écrite.
- **Constat 11** : le volet relatif de G5 sain compare deux estimations de Monte-Carlo du même nombre. Faut-il une autre référence (par exemple l'approximation normale 0,63), ou le plancher de 0,50 seul ? Le code reste conforme à la lettre de la spécification.

## Essais

1. J'ai scellé les essais avant leur première exécution (20 fichiers scellés en une fois : paquet, essais, script).
2. Je les ai lancés ensuite : `PYTHONPATH=src python -m pytest -q tests/test_hasard_defenseur_v2_*.py` donne **62 réussis en 36,7 s**, soit 54 portés et 8 nouveaux.

## Script complet : non relancé

Aucune correction ne touche un calcul de la sortie :
- **Constat 4.** Il ne change T_Δ que pour une variance non nulle inférieure à 10⁻¹² · max(1, Σz²/k). Dans toutes les simulations jouées, Z prend ses valeurs dans {−1, 0, 1}, ou dans {−4, −1, 1, 3, 4} pour G5 (b). Une variance non nulle y vaut alors au moins 0,5, et le seuil n'est jamais atteint.
- **Constats 5 et 12.** Ils ne touchent que le rejeu, le contrôle de l'ordre de passage et une docstring, que le script n'appelle pas.
- **Les autres constats** portent sur des essais ou des textes.

Vérification : j'ai joué les scripts v1 et v2 à `--taille petite`, avec la même entropie (20261122). Une fois retirés les champs `version`, `code` et `duree_s`, les deux sorties sont **identiques** octet pour octet. Elles ont été comparées dans le bloc-notes et n'ont pas été versées.

La sortie complète de référence reste donc `docs/notes/chantiers-21-novembre-v1/code-v1/simulations-hasard-defenseur-v1-complete-v1.json`, jouée avec le code v1 (empreinte d'ensemble `ea1eef41…`). Une sortie complète au nom de la v2 demanderait 36 minutes de calcul local, sans aucun chiffre changé.

## Points laissés ouverts

Ce sont ceux du rapport v1. La contre-lecture en accepte 13 : les points 1 à 5, 7, 9, 10, 11, 12 (sauf la règle de k et N), et 13 à 16. Les points renvoyés au concepteur sont listés plus haut.

## Ce qui n'est pas écrit

- Le régime d'excès de l'audit (§ 5) et l'intervalle par inversion (§ 3).
- L'image de la figure : seules ses données sont produites.
- Le harnais réel sur organismes, la mesure de la perception de l'étiquette (§ 7) et le préenregistrement court (décision 1).
- La preuve de l'exactitude de Westfall et Young sous le nul global.
- Le test de mort 4 (redondance) : les courbes du § 5 en donnent les données ; aucun verdict n'est codé, la spécification ne fixe pas de seuil.
- La vérification des corrections par le même contre-lecteur reste à faire (classe B).
