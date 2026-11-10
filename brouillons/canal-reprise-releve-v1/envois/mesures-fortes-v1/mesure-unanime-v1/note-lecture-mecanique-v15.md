# Mesure unanime — note de lecture v1 : fausses alertes par épisode honnête entier de l'agrégateur séquentiel, sans puis avec corrélation injectée (scores de P3)

session-dépôt session_01QPDgKgcLdggoVJfGC5cBw8, Opus 5.5, écrite après le relevé `date -u` de 10:33:16 UTC, le 10 novembre 2026. Préenregistrement **scellé** (compagnon vérifié) : `preenregistrement-mesure-unanime-v15.md` (`3a1651f4b1bc7bda4da5001c32790b9daf9b1ab3509a303fbf2ba82ac144fc1c`), commit du scellement `bdf8f2876a4a858908a2e8a6eabfc6a3635fb70f`. Sortie : `sortie-reelle-v15.json` (`474ae1f5fef987acfff01638c3ad99b7d64948625e601493183765eb80587af4`), script `analyse_fausses_alertes_v8.py` (`52b1760a09970526a926f2119dceeef7f20e2f280bdb6a6c2d890962556c5400`), données `/home/claude/canal-conv-audit-n04/donnees/20261019-230011-p3-reel/scores-p3.npz` (`968414fc7ce7db935c2c4a390a13e2eceebe2fd722628cccb52caf27128004cf`), commit du manifeste `bdf8f2876a4a858908a2e8a6eabfc6a3635fb70f`. Lecture mécanique : `lecture-mecanique-reelle-v15.json` (`5dac1a1611db58787bc241e0ec086dc011e9b8ae47876483e0c2443237d3a692`) ; table `table-m2bis-m4-v8-E58.json` (`0ff964a11c64947878b538972def4dcc5b21a2a4b383d5632f5147f0cec5d3de`). une seule exécution réelle (R1).

## Verdict (ligne de lecture gelée, appliquée mécaniquement)

**première ligne : la synthèse a raison (comparateur par épisode entier ; sommes sans niveau sous dépendance non vue, maximum tenu) — proposé à Lazar pour G1 et H2**

## Les verdicts, énoncé par énoncé (seuils gelés du préenregistrement)

| énoncé | verdict | quantités |
|---|---|---|
| M1 (seuil par action, τ = 0) | confirmé | médiane 0,086, intervalle [0,060 ; 0,103] |
| M1 bis (par action, de τ = 0 à τ = 2) | décroissant | 0,086, 0,084, 0,075, 0,054 |
| M2 (contrôle, Ville à τ = 2) | attendu | médiane 0,128 |
| M2 bis (Ville τ = 2 moins τ = 0) | hors table (rapporté) ; signe > 0 attendu : tenu | 0,085 [0,066 ; 0,121] ; table au r₀ médian : 0,137 |
| M2 ter (la lecture sur P3) | (1) Ville tenue sur P3 à τ = 0 | Ville τ = 0 réelles 0,043 (table au r₀ : 0,024) ; mélange 0,010 ; mélange à pas fixé 0,007 ; D 0,033 [0,007 ; 0,051] ; D′ 0,036 [0,009 ; 0,052] ; dérive mesurée -0,003 [-0,004 ; 0,001] |
| M3 (24 cellules conformes, calibrage partagé) | tenu | L = 0,026, B = 0,100 ; pire cellule tau=2.0:somme_terminale = 0,028 ; fragiles : 0 ; audit : 0 |
| M4 (dépendance seule, excès apparié) | confirmé | excès 0,061 [0,035 ; 0,073] (différence des médianes 0,068) ; quantité 0,089, à τ = 0 0,021 ; maximum conforme 0,003 ; table (excès au r₀) 0,090 |
| contrôle placebo | mêmes médianes (aucun écart > 0,05) | écarts réelles − placebo sur les 24 cellules de M3 et le maximum de M4 : max |écart| = 0,017 |
| cellule conforme à 0 | aucune | |

## Corrélation intraclasse (rapportée, jamais une condition)

r₀ médian des sondes réelles : 0,140 ; placebo : 0,113 ; centré par pas : 0,160 ; mélange à pas fixé : -0,007.

## Réserves du script de lecture

- aucune.

## Les 24 cellules de M3 (médianes sur les sondes réelles)

| cellule | médiane |
|---|---|
| tau=0.0:max | 0,017 |
| tau=0.0:somme_terminale | 0,017 |
| tau=0.0:somme_sequentielle | 0,017 |
| tau=0.0:page | 0,017 |
| tau=0.0:processus_e | 0,017 |
| tau=0.0:balayage | 0,017 |
| tau=0.5:max | 0,021 |
| tau=0.5:somme_terminale | 0,024 |
| tau=0.5:somme_sequentielle | 0,023 |
| tau=0.5:page | 0,025 |
| tau=0.5:processus_e | 0,025 |
| tau=0.5:balayage | 0,022 |
| tau=1.0:max | 0,025 |
| tau=1.0:somme_terminale | 0,025 |
| tau=1.0:somme_sequentielle | 0,025 |
| tau=1.0:page | 0,025 |
| tau=1.0:processus_e | 0,026 |
| tau=1.0:balayage | 0,026 |
| tau=2.0:max | 0,026 |
| tau=2.0:somme_terminale | 0,028 |
| tau=2.0:somme_sequentielle | 0,028 |
| tau=2.0:page | 0,027 |
| tau=2.0:processus_e | 0,027 |
| tau=2.0:balayage | 0,028 |

## Manifeste

E = 58 ; K par pli = [37, 37, 37, 37, 37, 37, 37, 37, 38, 38] ; L = 0,026 ; tirages 20 ; rééchantillonnages 2000 ; sondes réelles 30, placebo 400 ; numpy 2.5.4 ; python 3.13.18 ; entropie 20261028.

## Réserves de l'auteur (à la main, après la lecture mécanique)

⟨À ÉCRIRE : ce que la lecture ne dit pas ; R4 si un résultat paraît trop propre ; aucune interprétation hors des critères gelés.⟩

