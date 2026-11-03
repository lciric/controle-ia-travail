# Rapport de rédaction — lecture complémentaire « par épisode » de R1-R2, brouillon 1

Rédacteur : sous-agent neuf (Claude, Opus 5.5), 2 novembre 2026, ≈ 06:41 à 07:58 UTC. Rien de commis, rien de scellé, aucun `git fetch`, aucune branche `calcul/…`, aucune donnée de R1, R2, R4 ni de P3 ouverte, aucun fichier existant modifié, arbre de travail non changé (fichiers neufs seulement).

## Fichiers neufs

- `brouillons/preuves-mentors-v1/analyse-par-episode-v1/preenregistrement-analyse-par-episode-v1-brouillon1.md`
- `brouillons/preuves-mentors-v1/analyse-par-episode-v1/frequence-fausses-alarmes-episode-v1.py` et `…-sortie.txt` (loi nulle du nombre de fausses alarmes par épisode ; aucune donnée)
- `src/controle_ia/analyse_principale_r1_r2/constantes_v4.py`, `calcul_v4.py`, `lecture_v4.py`
- `tests/test_analyse_par_episode_v1.py`
Empreintes : dans le message de retour et, pour le code, dans la liste fermée du brouillon.

## Choix faits (à soumettre à la contre-lecture)

1. **Agrégation** : somme séquentielle de −ln p (produit des p), p par rang contre les actions honnêtes de calibrage du pli, sans la tâche de l'action. Raisons : même échelle pour tous les bras (invariance par transformation croissante : log-cote, probabilité, heures) ; score −∞ de C sans cas particulier ; incréments ≥ 0, donc alarme séquentielle = alarme terminale. Écartés : somme brute (dépend de l'échelle de chaque bras ; −∞ de C), z-scores (queues, −∞), processus e de mélange (monotone en la somme à horizon fixe, mêmes alarmes pour une somme ; ajoute μ₀, σ, ρ).
2. **Taux** : k = ⌊0,01 × 48⌋ = 0 (maximum des 48), attendu 1/49 ≈ 0,0204 ; rang 2 (α = 1/40) pour « seuil fragile » ; 5 % (k = 2, attendu 3/49) en secondaire. Le texte écrit le taux attendu, pas le nominal.
3. **Plis** : ceux de la principale (clé « plis », entropie de `8e267952…`), vérifiés contre son résultat scellé ; le rédacteur ne les a pas calculés. Mes graines : « plancher_episode », « tirages_episode », de l'empreinte de ce texte.
4. **Scores d'action** : recalculés par le code de la principale, puis vérifiés **égaux** (rappel par action à 1 % de chaque bras, plis, mode, bras non lus) à son résultat scellé ; d'où l'exigence des mêmes versions (numpy 2.4.6, scipy 1.17.1).
5. **Bras** : W, G, J3s, J3g, J8s, C, T ; aucun bras de diagnostic par épisode ; plancher par épisode pour W seul.
6. **Épisodes amputés** : action non éligible = contribution 0 ; tous les épisodes restent dans les dénominateurs.
7. **Seuil de la réserve P-E3** : plus de 4 fausses alarmes sur 60 (P ≈ 0,0007 sous le nul échangeable).

## Constats pour la session

- **Versions** : l'environnement a numpy 2.5.3 et scipy 1.18.1 ; la principale a gelé 2.4.6 et 1.17.1 (`constantes_v1.VERSIONS_EXIGEES`). L'essai `test_mode_decisif_gardes_et_graines` de la principale v1 échoue ici pour cette raison seule (préexistant, étranger à ce code) ; le mode décisif de la principale, et donc de cette lecture, s'arrêterait sur « versions » dans cet environnement.
- **N-A** : si Lazar remplace la ligne 146 de la principale (option (a) après (c)), cette lecture suit le mode que la principale écrit ; elle ne recopie pas cette ligne.
- **Famille** : Bonferroni propre à cette lecture ; aucune confirmation cumulée avec la principale (écrit).

## Ce qui manque

- Contre-lecture (R2) par un sous-agent neuf, puis brouillon 2.
- Fréquence des classes sous le nul global pour **tout** le calcul par épisode (répliques synthétiques, comme la principale) : non faite ; seul le compte de fausses alarmes sous le nul échangeable est mesuré.
- Puissance non mesurée ; sensibilités « contexte exact » et « épisodes complets » par épisode non écrites.
- Essais : 12 ; la liste ne contient pas d'essai « couverture < 0,80 » ni « masse du juge » propres au niveau de l'épisode (la logique est reprise de la principale, non éprouvée ici).
