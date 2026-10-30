# Expérience v2 — bisociation à deux espaces — code et essais (v1)

Préenregistrement scellé : `prereg/preenregistrement-bisociation-deux-espaces-v2.md`, empreinte `e821e8752532fdabc03cb684e9a3bb71a40bcb4267de842da228de2b88c314ea` (vérifiée par `exiger_prereg_scelle`). Code de départ de la version 1, jamais modifié : `../../trancher-recombinaison/` (`monde_v1.py` af907b1d…, `methodes_v1.py` 2f7a8b11…) ; pièce A : `orchestrateur-pole-v7/pole/recombinaison.py` (71faad38…).

**État : code fini, essais passés, validation V1 à V9 et invocation unique NON lancées.** Deux questions bloquantes (Q-01 taux de régénération supérieur à S11 ; Q-03 graine de la non-régression) et deux lectures à confirmer (Q-04 jumelle de V4, Q-02 N_grille) : voir `ecarts-et-questions-v1.md`. L'invocation unique ne doit pas partir avant réponse.

## Structure et correspondance avec le préenregistrement

| Section | Fichier : fonction |
|---|---|
| § 1 G1 (vérité / observation, `AccesLatent`) | `monde_v2.py` : `Obs`, `Latent`, `Monde.latent`, `JETON_MESURE`, `AccesLatent` |
| G2 à G7, G9, G10 (générateur, canal, ponts, couplage λ, monde inversé) | `monde_v2.py` : `_construire`, `_palettes`, `_planter_v2`, `_attribuer_rares`, `_observer_operateurs`, `_emettre`, `_observer_concepts_fond`, `_observer_concepts_rares` |
| G8 (M_inertes, miroir rôle 7) | `monde_v2.py` : `generer`, `_observer_concepts_rares(miroir=True)`, `empreinte_latents` ; contrôle : `mesures_v2.verifier_inertes` |
| G11 (régénération comptée) | `monde_v2.generer` (`MAX_TENTATIVES`, `latent.tentatives`) |
| G12 (vérité unique), mécanismes | `monde_v2._verite` ; `mesures_v2.mecanismes_vrais` |
| § 2 étage commun | `monde_v2.etage_commun` |
| § 3 quantités (κ, score, strates) | `bras_v2.vecteurs_concepts`, `kappa`, `scores`, `strate` |
| § 4 bras (21, ordre figé) et algorithme de N | `bras_v2.py` : `ORDRE_BRAS`, `FONCTIONS`, `tour_par_score`, `bras_*` ; oracle : `mesures_v2.oracle` |
| § 4 bis placebos | `bras_v2.placebo_permutation` |
| `glouton_paires`, copie gardée de `ordre_glouton` | `noyaux_v2.py` |
| § 5 hyperparamètres | `bras_v2.py` (E_PRIORI 8,5 ; BETA 1 ; ε 0,05 ; γ 1e-3 ; φ 4) ; grille : `invocation_unique_v2.grille` |
| § 6 conditions, paramètres S16 | `monde_v2.CONDITIONS_V2`, `CONDITIONS_NR`, `S16`, `garde_configuration` |
| § 6 validation V1 à V9 | `validation_v2.py` (non lancé) |
| § 7 graines | `graines_v2.py` (`sequence`, `generateur`) ; rééchantillonnage : `mesures_v2.rng_contraste` |
| Métrique : exclusion, complément, précision, intervalles | `mesures_v2.py` : `exclu`, `completer`, `mesurer`, `ecart_apparie`, `ecart_entre_ensembles` |
| § 7–8 contrastes (1 à 9, 10, 11 à 15, 20 à 40) | `analyse_v2.py` |
| S9 extension | `mesures_v2.extension_s9`, `sigma_chapeau` |
| § 9 ordre, invocation unique | `invocation_unique_v2.py` ; contrôle du lecteur : `mesures_v2.verifier_ordre` |
| Critères de lecture gelés, Tables 1 et 2, audit | `lecture_v2.py` |
| Liste d'arrêt : balayage statique | `balayage_v2.py` |
| Liste d'arrêt : taux S11, plafond S8, nombre de mondes, racines, empreintes du code, reproduction | `mesures_v2.py` : `verifier_taux`, `verifier_plafond_oracle`, `verifier_nombre_de_mondes`, `verifier_racine`, `verifier_empreintes_code`, `verifier_reproduction` |
| Exécution (1 ou 2 processus) | `travail_v2.py` |
| Reproduction des témoins sur NR | `reproduction_temoins_v2.py`, résultat `reproduction-temoins-v2-resultats.json` |

## Essais (commande : `cd <ce dossier> && PYTHONPATH=<dépôt>/src python3 -B -m pytest -p no:cacheprovider essais/essais_gardes_v2.py essais/essais_complements_v2.py -q`)

- `essais/essais_gardes_v2.py` : 40 lancés, 40 réussis, 0 échec (les 17 gardes de la liste « Gardes testées sur un cas sain et sur un artefact », chacune avec cas sain et artefact).
- `essais/essais_complements_v2.py` : 42 lancés, 42 réussis, 0 échec (graines du § 7, gardes S11/S8/racines/numpy/empreintes, M_inertes, mécanismes, les 14 conditions et NR avec les 21 bras, identité du bras a avec `corrige` de v1 sur 50 mondes, analyse sur tableaux synthétiques, validation et V9 en plomberie, invocation unique avec exécuteur synthétique).
- Total : **82 lancés, 82 réussis, 0 échec**.
- Garde non exécutable : « essai R5 de J sur les 300 miroirs de validation de M_inertes » est V9 elle-même ; non lancée (consigne). Éprouvé à la place : la machinerie de V9 sur 30 miroirs d'essai, sans lecture du booléen, avec preuve qu'aucun bras candidat n'est appelé ; J vraie sur monde jouet (cas sain).
- Les essais n'emploient que des mondes jouets, des tableaux synthétiques, ou RACINE_VALIDATION avec des indices supérieurs ou égaux à 900 000 ; RACINE n'est jamais employée ; aucun contraste de décision ni moyenne de Δ(N, ·) n'a été calculé ni affiché.

## Reproduction des témoins de v1 (liste d'arrêt, marge S12 = 2 points)

NR_bien et NR_moyen, RACINE_VALIDATION, indices 0 à 1199 chacun, bras b, a, c, d1 seulement. Dans la marge pour les huit moyennes (intervalle de B § 1 élargi) :
- bien : b 0,2123 ; a 0,1606 ; c 0,1578 ; d1 0,2319 (0 monde exclu ; 66,28 paires valides par monde) ;
- moyen : b 0,1293 ; a 0,1096 ; c 0,1134 ; d1 0,1761 (9 exclus ; 59,64 paires valides).
Fichier scellé : `reproduction-temoins-v2-resultats.json` (empreintes du code incluses).

## Commande exacte de l'invocation unique (NON LANCÉE)

Après : réponse à Q-01 et Q-03, validation du générateur lancée et passée (`python3 -B validation_v2.py SORTIE.json --lancer-la-validation --lecture-v4 echange_ponts`, après réponse à Q-04), audit rendu si V9 est vraie, dépôt git propre et commité.

```
cd <dépôt>/brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/bisociation-deux-espaces-v1/experience-v2
PYTHONPATH=<dépôt>/src python3 -B invocation_unique_v2.py --run-id AAAAMMJJ-HHMMSS-bisociation-v2 --processus 2 \
  --validation <validation-sceller.json> --reproduction reproduction-temoins-v2-resultats.json [--audit-rendu <rapport.json>]
```
Elle vérifie tous les prérequis avant le premier monde, imprime seulement σ̂, le drapeau S9 et n' par condition, scelle le manifeste avant tout résultat de décision, écrit un fichier scellé par condition (`diag/<run_id>/resultats-<condition>.json`), puis `contrastes`, `donnees-audit`, `validation-etape1` (moyennes et grille, non ouverts avant le verdict). Aucun verdict.

## Durée estimée (2 processeurs, mesurée sur 60 mondes d'essai par condition, hors RACINE)

Environ 0,02 à 0,39 s par monde selon la condition (21 bras de décision). Mondes de décision aux nombres de S15 et S7 (16 200) : environ 39 minutes ; au plafond de S9 (23 400) : environ 58 minutes ; étape (1) du § 9 environ 40 secondes (grille comprise). Validation V1 à V9 non mesurée (quelques minutes attendues).

## Qui a écrit quoi

- Premier sous-agent (Opus, arrêté par une limite d'usage) : `monde_v2.py`, `bras_v2.py`, `mesures_v2.py`, `noyaux_v2.py`, `graines_v2.py`, `balayage_v2.py`, `lecture_v2.py`, `essais/jouets_v2.py`, `essais/essais_gardes_v2.py` (copie intacte dans `brouillon-opus-origine/`).
- Seconde session (Sonnet), conformité vérifiée section par section ; corrigé : (1) deux essais faux (`test_g07` : le correctif du nombre de tentatives restait actif pour la seconde moitié ; `test_g12` : V_surface exige 13 concepts rares, pas 14) ; (2) `test_g03` : l'artefact n'exécutait pas le bras curieux dans `executer_monde`, il le fait maintenant ; `test_g16` : l'option 2 de S17 n'était pas évaluée (`or True`) ; (3) `balayage_v2` : ajout des accès dynamiques (`getattr`, `__dict__`, chaînes de noms latents) ; (4) `mesures_v2` : ajout des mécanismes et du rappel par mécanisme, du plafond S8, du contrôle du nombre de mondes, des racines, des empreintes du code, de `verifier_taux(decision=…)` ; (5) `monde_v2` : option `jumelle` pour V4 (inerte par défaut, sorties inchangées). Conformité par ailleurs constatée pour G1 à G12, § 2 à § 4 bis, graines, Tables 1 et 2.
- Seconde session, écrit : `analyse_v2.py`, `travail_v2.py`, `validation_v2.py`, `invocation_unique_v2.py`, `reproduction_temoins_v2.py`, `essais/essais_complements_v2.py`, ce fichier, `ecarts-et-questions-v1.md`.

Renvoi : `ecarts-et-questions-v1.md` (Q-01 à Q-12).
