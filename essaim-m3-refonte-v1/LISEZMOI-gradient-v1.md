# Branche `outils/essaim-m3-gradient-v1-travail` — étape 1 du programme « gradient conçu par l'essaim » (LISEZMOI v1)

Partie de `outils/essaim-m3-refonte-v1-travail` à `5a6abd5` (24 octobre 2026). Décisions de Lazar : 18:22 (programme à
trois étapes, GO de principe 500–1 500 €), 18:23 (« go, commençons par là » : les sondes d'abord). Rien de dépensé ;
rien de scellé ; aucun run réel.

## Ce qui est ajouté au noyau (contrat v3)

- `essaim_m3/noyau/entrainement.py` : `Entraineur` — l'organisme écrit une spécification (données d'entraînement par
  identifiants — jamais de test —, **objectif** `def perte(p, y)` qu'il conçoit, algorithme `sonde-lineaire` ou
  `sonde-une-couche` avec pas, taux, l2, lot, cache, graine, prétraitement) ; le noyau l'exécute en sous-processus
  (`python -I -B -s`, limites de mémoire, processeur, délai), gradient de la perte par différences finies, le reste
  analytique ; journal `journal-entrainements.jsonl` (empreintes de la spec et de l'objectif), modèles `modele.npz` ;
  `predire(identifiant, ids)` rend des probabilités, jamais des vérités ; statuts `OK`, `REFUSE`, `PLAFOND`,
  `ECHEC_ENTRAINEMENT`, `DELAI_DEPASSE`, `INDISPONIBLE`, `ANOMALIE`.
- Traits : en réel, activations de Llama-3.1-8B-Instruct par tâche (`--traits traits-….npz`, extraites sous GO par
  `scripts/extraire_activations_v1.py` — couches 8/12/16/20/24, dernier jeton et moyenne, manifeste et empreintes, le
  script ne lit jamais les vérités) ; en simulation, traits de hachage (`traits_simules`). Sans traits en réel avec
  `entrainements_max` > 0 : refus.
- Serveur et client : opérations `entrainer`, `predire` ; `budget()` rend `entrainements_restants` ; contexte :
  `budget.entrainements_max`, `budget.pas_max`, `traits.{disponibles, dimension, description}`.
- Noyau : `--entrainements-max` (10), `--pas-max` (5 000), `--traits` ; un entraîneur par génération et par lignée ;
  `n_entrainements` dans le résumé ; journal et modèles archivés hors de la vue des organismes ; confrontation : traits
  simulés des tâches d'attaque en simulation (en réel, sans activations des attaques : pas d'entraînement en défense).
- Organisme factice `tests/fixtures/organisme_sonde/` (test seulement) : perte de Brier, sonde linéaire normalisée,
  réponse par la sonde quand elle est sûre, espèce sinon ; augmente ses pas si le score baisse.
- Tests : 55 (`test_entraineur_sonde_sain_et_artefacts`, `test_entraineur_une_couche_et_perte_logarithmique`,
  `test_boucle_organisme_sonde_apprend_sous_le_noyau`, `test_gradient_en_reel_exige_des_traits`).

## Illustration mécanique (simulation, graine 20261024, non opposable)

Organisme « sonde » : 8 appels pour 3 générations, score de développement 0,90–0,925, test final 0,95 ; organisme
factice sans gradient : 362 appels, 0,65–0,875 ; sonde gelée : identique à la sonde adaptative (la sonde se réapprend
chaque génération ; ce que la génération suivante peut changer, c'est la conception). Chaîne complète testée : banque
réelle (80 traces) → traits factices (`--factice`) → noyau avec traits chargés → score au hasard (traits aléatoires).

## À faire avant le run réel

- Vues multiples servies à l'organisme (`spec["vue"]` : une couche × une agrégation) ; choix de la liste au scellement.
- Banque scellée complète (sous-ensemble « conscience d'évaluation », avec Lazar).
- Contre-lecture (session-depot) de `prereg/brouillon-gradient-etape1-sondes-v1.md` ; GO sur devis (≈ 70 USD, plafond
  demandé 90) ; extraction des traits par le lanceur de session-depot.
