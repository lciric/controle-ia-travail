# Commande de location de l'essai d'invariance au lot (audit R4 de la recourse de B-7) — v1, sans ssh (proposée, **non exécutée**)

Écrite par la fille « Neuron Lens » le 2026-11-17. **Différentiel de la commande B-α v8** (`commande-b-alpha-v8.md`, `2df1dfdd…`, jouée
avec succès à la cinquième course) : toutes ses étapes 0 à 15, ses consignes (feu R-3056 : R-2887, R-2892, P1, R1, R4, préavis d'une
ligne, aucun contournement d'un refus) et sa règle de destruction s'appliquent, avec **seulement** les substitutions ci-dessous. Feu
exigé : celui de la mère, sur le devis du préenregistrement v3 (§ 7). Plus les deux règles du « go » de Lazar pour la seconde tentative :
aucune ligne de l'amorce en 20 min = destruction immédiate ; une seule tentative.

| point de la v8 | substitution |
|---|---|
| objet | essai d'invariance au lot ; préenregistrement `audit-invariance-lot/preenregistrement-audit-invariance-lot-v3.md` (`bbf2c95b…`), contre-lu trois fois (dernière : « prêt », `contre-lecture-audit-invariance-lot-v3.md`) |
| étape 4, offre | même filtre et même prix lu exigé (≤ 0,73 USD/h stockage compris) ; écarter les offres de la machine 58627260/58627262 (échec de la quatrième course) |
| étape 5, dépôt réduit | `scripts/depot_reduit_neuron_lens_b_alpha_v12.py <COMMIT_SOURCE> <dossier neuf>` ; **liste attendue `b9f50d40583b03a41ab2129f0aa8c19ff56bcf1b717f837ee27dc768df36eda9`** (359 fichiers ; essai à blanc v3) ; branche `course/neuron-lens-audit-invariance-reduit-v1` ; branche des résultats **`calcul/neuron-lens-audit-invariance-v1`**, absente à prouver |
| étape 6, RUN_ID | `<AAAAMMJJ-HHMMSS>-neuron-lens-audit-invariance` |
| étape 7, création | `--label neuron-lens-audit-invariance` ; `-e BRANCHE_RESULTATS=calcul/neuron-lens-audit-invariance-v1 -e CARTE_ATTENDUE=A100-SXM4-40GB` ; clone de `course/neuron-lens-audit-invariance-reduit-v1` ; `exec bash depot/scripts/amorce_neuron_lens_audit_invariance_v3.sh` ; le reste de la ligne (`GO_ID=GO-2026-11-14-06`, les deux secrets par leur nom, `COMMIT_REDUIT` et `COMMIT_SOURCE` lus par programme dans `rapport.json`) inchangé |
| étapes 9 et 10, garde et minuterie | **`--plafond 2`** (compte rendu à 1,20, arrêt dur à 1,80 USD ; minuterie = 90 % de 2 au prix lu, ≈ 2,5 h à 0,73) ; fichiers de suivi en `-audit-invariance-v1` |
| étape 11, rappels | compte rendu à **0,6 h** (haut de l'attendu) ; la mère décide à **1,8 h** (échéances codées) ; « vérifier et détruire » à 80 % de D ; veille comme en v8 |
| étape 12, sur la machine | amorce v3 : commit, carte (nvidia-smi puis torch), pip, essais (module v3, lanceur v5, balayage), puis `preparer` → `telecharger-tokeniseur` (**clé**) → `telecharger-poids` (**clé**, retirée ensuite) → `audit-invariance` (hors ligne, sans clé ; carte et préenregistrement exigés par l'étape) |
| étape 13, lectures de la session | aucune lecture de mesure par la fille ; seulement l'état poussé et la dernière ligne du journal |
| étape 14 | `verifier_resultat` sur les 4 résultats d'étape ; compagnon de `audit-invariance-lot-v3.json` ; copie dans `prep/neuron-lens-v1` |
| lecture | par un lecteur neuf, sur le préenregistrement v3 scellé (§ 4), après la course |

## Essai à blanc
`scripts/essai_a_blanc_amorce_neuron_lens_audit_invariance_v3.sh`, journal `audit-invariance-lot/essai-a-blanc-audit-invariance-v3.txt`,
joué sur le commit source `ab16240b…` : **conforme, 0 écart** (nominal 4 appels, 106 essais réels, reprise, échec 20, 14 formes, gardes
d'entrée dont un identifiant de B-α refusé, garde de carte, vrai `main` exercé : `suite`, `jouer --etape preparer`, `suite`).

## Devis (préenregistrement v3, § 7)
Attendu ≈ 0,35 à 0,6 h, **≈ 0,22 à 0,37 USD** (0,26 à 0,44 à 0,73 USD/h) ; garde à 2 USD ; ligne GO-2026-11-14-06 au pire ≈ 5,4 à 6,0 USD
sur 12 (≈ 3,4 à 4,0 déjà faits). Écart de carte : GO-2026-11-17-04 (commit de `main` `83fe2c55`), à citer par le feu.

## Non couvert, déclaré
Vraie carte, vrai pip, vrai chargement de Llama (essayé sur un Llama miniature et un faux module voisin) ; le contrôle de la carte de
l'étape a lieu après le chargement (l'amorce refuse déjà au code 11 avant `pip`).
