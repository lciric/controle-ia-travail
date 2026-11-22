# Rapport de code — l'audit après coup, sur mondes simulés (v2)

- Classe B (instrument). Opus 5.5, développeur, 22 novembre 2026. La v2 porte les corrections de la contre-lecture v1 : `docs/notes/chantiers-21-novembre-v1/code-v1/contre-lecture-code-audit-apres-coup-opus-v1.md`, empreinte 6f15aca7…, vérifiée OK.
- Le rapport v1 (`rapport-code-audit-apres-coup-v1.md`, 8417b526…) reste valable pour ce que la v2 ne change pas.
- Paquet neuf : `src/controle_ia/audit_apres_coup_v2/`. Essais : `tests/test_audit_apres_coup_v2_*.py`. Les fichiers v1, scellés, ne sont pas touchés.
- Deux modules sont recopiés à l'identique de la v1 : `oracle_simule.py` et `regle_audit.py`. Deux autres ne changent que par les espaces de graines (I-4) : `gardes_invariants.py` et `attaque_choisie.py`. Dans tous les fichiers, le nom du paquet passe de `_v1` à `_v2`, et les noms de dérivation de `…_boucle_v1` à `…_boucle_v2`.
- Aucun modèle, aucun réseau, aucune machine payante, aucun commit. Tous les fichiers neufs sont scellés.

## Essais
- **Scellement avant exécution (I-8).** Les essais v2 ont été scellés à 13:13:21Z, avant leur première exécution.
- **Première exécution**, de 13:13:21Z à 13:14:03Z : `PYTHONPATH=src python -m pytest -q tests/test_audit_apres_coup_v2_*.py`, **125 réussis, 0 échec, 41,9 s**. Aucun chiffre n'a été changé après exécution.
- **Contrôle des trois mutations** (fait sur une copie du paquet dans le bloc-notes, jamais dans le dépôt) : chacune fait casser l'essai qui la vise.
  - Relecture de l'épreuve 3 (garde retirée de `noter`) : `test_mutation_relecture_dans_la_suite_de_l_epreuve_3` casse (`tests/test_audit_apres_coup_v2_epreuves.py`, l. 226).
  - Journal, « audité » qui ne suit plus U_i < π_i : `test_mutation_audite_qui_ne_suit_pas_U_inferieur_a_pi` casse (`tests/test_audit_apres_coup_v2_journal.py`, l. 65).
  - Score consigné après le verdict, admis par le harnais : `test_mutation_score_consigne_apres_le_verdict` casse (`tests/test_audit_apres_coup_v2_epreuves.py`, l. 234).

## Simulations longues, rejouées
- Sortie : `docs/notes/chantiers-21-novembre-v1/code-v1/simulations-longues-audit-apres-coup-sortie-v2.txt`, empreinte 43b2003c87df74ab…, entropie 20261122. Toutes les lignes « tiennent ».
- Les chiffres diffèrent de la v1, parce que les espaces de graines ont changé (I-4) :

| Grandeur | v2 |
|---|---|
| Borne du plancher (seuil 1 869) | 1 899 |
| Artefact « plancher abaissé pour les scores bas » | 1 599, refusé |
| Borne à q = 0,8 | 1 897 |
| Rapport uniforme sur proportionnel | 15,50 (tolérance relative 0,04) |
| Score trompeur : couverture | 1 973 sur 2 000 |
| Score trompeur : biais de T̂ | 0,085 pour une erreur type de 6,9 |
| Score trompeur : délai | 1 912 |
| Famille tenue à l'écart : gain | 1,001 |
| Alerte d'excès, d0 connu | 0,028 |
| Alerte d'excès, d0 estimé sans correction | 0,2375 |
| Alerte d'excès, d0⁺ | 0,0045 |

- Les deux dernières lignes d'excès portent l'étiquette « au-delà de la référence » (horizon 4 000, m = 400).

## Sort de chaque constat

Chemins relatifs à `src/controle_ia/audit_apres_coup_v2/` et `tests/` ; les lignes sont celles des fichiers v2 scellés.

| N° | Sort | Où |
|---|---|---|
| I-1 | porté | `harnais_simule.py` l. 206-208 : refus de l'organisme d'un épisode de verdict. `epreuves_boucle.py` l. 517 : les épisodes de verdict prennent l'organisme `org_porte`. l. 523-525 : sixième artefact, un épisode de flux de l'organisme d'un épisode de verdict, refusé. |
| I-2 | porté | `harnais_simule.py` l. 149-154 : un épisode de verdict d'une famille ou d'un organisme déjà en lignée (ouverte ou scellée) est refusé. l. 236-242 : la lignée est revérifiée au scellement. `epreuves_boucle.py` l. 538-546 : artefact ajouté à l'épreuve 1. Essai : `test_audit_apres_coup_v2_epreuves.py` l. 243. |
| I-3 | porté | `epreuves_boucle.py` l. 110-145 : `lignee_version(i)` et `noter(…)` ; chaque direction est calculée sur la liste explicite passée à la garde (forme explicite seule, sans forme vectorisée). l. 167 : `epreuve_3_relecture` passe par `noter`, qui lève. Mutation : `test_audit_apres_coup_v2_epreuves.py` l. 226. |
| I-4 | porté | `graines.py` l. 58 (`ESPACES`), l. 77 (`generateur_auxiliaire(entropie, espace, …)`, qui refuse un espace inconnu ou réservé) ; `flux_tache` et `generateur_episode` dans leurs espaces. Appels : `gardes_invariants.py` l. 82, `attaque_choisie.py` l. 114, et dans `epreuves_boucle.py`, `echelons_simules.py`, `simulations_longues.py` et les essais. L'ordre et la permutation de l'épreuve 9 prennent aussi l'identifiant du monde. Essai : `test_audit_apres_coup_v2_graines.py` l. 84. |
| I-5 | porté | `journal.py` l. 111-118 : π_i = min(1, somme des parts), écrêtage, source contre U_i et les parts. Essais : `test_audit_apres_coup_v2_journal.py` l. 65 (mutation), l. 75 et l. 87. |
| I-6 | porté | `alerte.py` l. 173 : `alerte_exces` rend l'heure, le rang, l'horizon lu, l'étiquette et la déclaration. `simulations_longues.py` l. 73 : étiquette sur les lignes d'excès. Essais : `test_audit_apres_coup_v2_alerte.py` l. 83 et l. 103. |
| I-7 | porté | `alerte.py` l. 49-82 : `Latence` à champs privés ; `nombre`, `endommages` et `dommage_enjeu` lèvent sous « jamais » ; `censure_a` est étiquetée « censuré ». Essai : `test_audit_apres_coup_v2_alerte.py` l. 77. |
| I-8 | porté, sauf la part renvoyée du point 14 | Tolérances à 4 erreurs types calculées. `test_audit_apres_coup_v2_epreuves.py` : épreuve 4, l. 64 et l. 69-82 (réplication en 8 tâches) ; épreuve 6, l. 89 (16 répétitions). `test_audit_apres_coup_v2_estimateurs.py` : strate, l. 88 ; budget, l. 109. `test_audit_apres_coup_v2_score_trompeur.py` : budget, l. 29, contre l'espérance fermée (1 − P(d))·b + P(d)·π_min, puisque les endommagés ont g = 0 ; strate et pondéré, l. 58-61. Essais scellés avant leur première exécution (ordre ci-dessus). |
| I-9 | **renvoyé au concepteur, code laissé tel quel** | Pli consommé et clause 4 : `harnais_simule.py` inchangé sur ce point, sans la mention de la docstring (correction non portée, sur ta consigne). |
| I-10 | porté | `graines.py` l. 142-150 (`VERITES`, `declarer_verite`), l. 181-182 (refus « vérité plantée non déclarée »). `simulateur.py` l. 102 : `VeritePlantee.ecrire` déclare. Mondes gaussiens et échelons déclarés. `epreuves_boucle.py` l. 480 : l'empreinte réelle du monde jouet remplace `"e" * 64`. Essai : `test_audit_apres_coup_v2_graines.py` l. 78. La vérité d'un monde simulé reste aussi en mémoire (`Resultat.verite`), ce que dit la docstring de `simulateur.py`. |
| m-1 | porté | `estimateurs.py` l. 109. Essai : `test_audit_apres_coup_v2_estimateurs.py` l. 90. |
| m-2 | porté | Essai `test_mutation_score_consigne_apres_le_verdict`, `test_audit_apres_coup_v2_epreuves.py` l. 234. |
| m-3 | porté | `test_audit_apres_coup_v2_alerte.py` l. 83 : β > 0 et γ > 0, score informatif ; l'heure rendue est celle de la sous-suite « plancher » et diffère de celle calculée sur toutes les sources (les deux alarment). |
| m-4 | porté | `epreuves_boucle.py` l. 269. |
| m-5 | porté (docstring) | `harnais_simule.py` l. 257-260. |
| m-6 | porté (docstring) | `graines.py` l. 155-156. |
| m-7 | porté | `score_trompeur.py` l. 62, 85, 100 et 109 : budget sans défaut. Appels : `simulations_longues.py` et `test_audit_apres_coup_v2_score_trompeur.py`. |
| m-8 | porté | `table_seuil.py` l. 84 : d0⁺ − d0. |
| m-9 | porté | `estimateurs.py` l. 119. |
| m-10 | porté (docstrings) | `estimateurs.py` l. 103 ; `alerte.py` l. 20-22 ; `epreuves_boucle.py` l. 455. |
| m-11 | porté | `harnais_simule.py` l. 95-105 : `organismes_tenue_a_l_ecart` et `organismes_jeu_final`, sans valeur implicite dans le mode planté. `epreuves_boucle.py`, `harnais_plante` : les deux déclarés. Essai : `test_audit_apres_coup_v2_epreuves.py` l. 43. |

## Points ouverts de la v1, après la contre-lecture
- **Renvoyés au concepteur, non tranchés, code laissé tel quel** :
  - 2 : loi de la lisibilité ;
  - 3 : taux des politiques ;
  - 4 : « scores bas » (1 599 en v2, au lieu des 1 550 de la contre-lecture) ;
  - 9 : part d'enjeu au type le plus bas, rapportée et non comptée ;
  - 11 : seuil « signale les deux également », encore à 0,05 dans les essais ;
  - 13 : faire passer, ou non, la direction plantée des épreuves 3, 5, 6, 11 et de l'échelle par le bras de flux planté ;
  - 14, pour sa part renvoyée : la bande de 0,05 à 0,10 de l'épreuve 5, la répétition unique de l'épreuve 3 à Δ = 4 et l'arrondi des échelons restent comme en v1 ;
  - 16, pour un membre : un épisode du pli retenu n'entre jamais dans une lignée (lié à I-9).
- **Acceptés par le contre-lecteur** : 1, 5, 6, 7, 8, 10, 12, 15, 17, et le reste de 16. Pour les points 1 (clé de graine par flux) et 10 (loi de score « signal »), le contre-lecteur demande un erratum de classe B. Il n'est pas écrit ici : il revient à qui consigne.

## Ce qui n'est pas écrit
Comme en v1 : les devins, le bras « correction tirée au hasard », un réapprentissage sur un oracle réel, et le devis de l'étape 1. La vérification des corrections par le même contre-lecteur reste à faire.
