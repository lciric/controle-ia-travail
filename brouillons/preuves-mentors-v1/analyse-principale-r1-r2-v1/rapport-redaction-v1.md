# Rapport de rédaction — préenregistrement de l'analyse principale de R1-R2, brouillon 1 (v1)

- Rédacteur : sous-agent neuf (Claude, Opus 5.5), commandé par conv-audit le 2026-11-02 vers 00:10 UTC ; écrit entre 00:11 et 00:46 UTC.
- Aucune donnée de R1, R2 ni R4 lue ; aucune branche `calcul/…` consultée ; de P3, structure de `scores-p3.npz` seulement ; aucun commit, aucun réseau, aucun fichier existant modifié.

## Ce que j'ai écrit (fichiers neufs)

- Texte : `brouillons/preuves-mentors-v1/analyse-principale-r1-r2-v1/preenregistrement-analyse-principale-r1-r2-v1-brouillon1.md`.
- Code : `src/controle_ia/analyse_principale_r1_r2/` (`__init__.py`, `constantes_v1.py`, `calcul_v1.py`, `entrees_v1.py`, `lecture_v1.py`).
- Essais : `tests/test_analyse_principale_r1_r2_v1.py` (données synthétiques aux formats du fournisseur, commit 29bd8e2e).
- Fréquence sous le nul global : `frequence-nul-analyse-principale-v1.py` et sa sortie.

## Ce que j'ai fixé (délégué par le fournisseur ou tu par lui)

Niveau : l'action (Q1), sans agrégation séquentielle ; « éligible » = notée par P3 (scores finis) et `fidele` ; calibrage des bras entraînés sur les scores hors pli (Q2) ; quantile d'ordre supérieur en arithmétique entière, alarme stricte ; plis (tri, permutation par la clé « plis », 5 × 12) ; régression (λ = 1/C = 1, L-BFGS-B, réduction sans correction : fonction gelée de l'analyse secondaire) ; coût illisible : même ensemble d'actions pour tous les bras, C à −∞, T avec indicateur (Q3, Q4) ; longueur en points de code ; plancher : 200 directions tirées une fois, appliquées aux entrées centrées réduites du pli, quantile 0,95 linéaire ; intervalles : seuils recalibrés dans chaque tirage, quantiles 0,0125 et 0,9875, niveau 97,5 % aussi pour les secondaires (Q11, Q12) ; opérationnalisations de « ≈ », « parfaite », « nettement inférieur », « sous son plancher », préséance (Q5 à Q8) ; graines dérivées de l'empreinte du texte scellé du fournisseur (Q9) ; fiche de réception à clés fermées ; sensibilité « contexte exact » pour W, G, J3s, T.

## Ce que je n'ai pas pu fixer (nœuds ou questions à trancher avant le scellement)

- Q1 (niveau) : délégué, mais nos messages n° 326 et 328 parlaient d'épisodes et d'agrégation séquentielle ; je recommande l'action (raisons dans le texte). À confirmer par la session ou Lazar.
- Q3 (coût illisible) : tension entre « même exclusion pour tous les bras » et « coût lisible pour la règle et le prédicteur » ; choix : même ensemble, effectifs rapportés deux fois.
- Q8 (W − J3s supérieure avec mention contraire) : aucune ligne gelée ; le code écrit un nœud de lecture.
- Q9 (racine des graines) : l'empreinte du texte du fournisseur, plutôt que la nôtre (consigne du brief « dérivées de l'empreinte du texte scellé ») ; à confirmer.
- Q10 : l'en-tête du texte scellé du fournisseur dit encore « non scellé ».

## Constats de rédaction (déclarés)

- Le chargeur de P3 de l'analyse secondaire (`entrees.charger_run`) refuse toute action dont une sonde principale a un score non fini ; le fournisseur prévoit des actions non notées. Je ne l'ai pas réutilisé (chargeur neuf, même chaîne de sceaux, actions non notées permises et exclues). Vérification faite sans autre valeur : `diag/20261019-230011-p3-reel/resume.json` porte `actions_notees` = 2 400 sur 2 400 (seule clé lue, déclarée dans le texte) ; la commande secondaire ne s'arrêtera donc pas pour cette raison, et l'exclusion « non notées » sera vide.
- Calibrage emboîté essayé d'abord, écarté avant toute donnée réelle : un bras entraîné sans signal y avait un taux réalisé de 0 (seuils de modèles à 36 tâches appliqués à un modèle à 48).
- Intervalles à seuils figés d'abord : sur un jeu nul synthétique, W − J3s sortait « inférieure » (rappels 0,003 contre 0,018) ; passage aux seuils recalibrés dans chaque tirage (Q12), puis mesure de fréquence sous le nul (sortie ci-dessous).
- `textes-actions-p3.jsonl` de P3 est absent du disque de travail (R11 : vérifié ; présent dans l'historique git, par exemple au commit `a6c550ea`) ; il est exigé (trait (4) de T) : étape 0.f.

## Fréquence sous le nul global

Voir `frequence-nul-analyse-principale-v1-sortie.txt` (200 répliques, entropie 202611020110) ; les nombres sont recopiés dans le message de rendu.

## Durée estimée de la lecture

`calculer` à la taille réelle sur données synthétiques (2 400 × 3 × 4 096) : 11 s, ≈ 0,5 Go ; avec chargement et écriture : 1 à 5 minutes sur 2 cœurs chargés.
