Tu es un lecteur expert neuf (Claude Fable 5.1). Tu n'as écrit aucun texte, aucun code, aucune analyse de ce que tu vas lire. Français, sans sigle non développé ; toute heure vient de `date -u`. Dépôt : `/home/claude/controle-ia-travail`, branche `canal/conv-audit-n04` (lecture seule ; lis `CLAUDE.md` d'abord, en particulier les règles R1, R3, R4, R5, R8).

## La question de Lazar (directeur), mot pour mot
« Comment faire pour obtenir un R1 qui soit concluant ? Je souhaite une version plus approfondie de cette tâche, pas une version plus longue. Avant de la reformuler : (1) indiquez ce qu'un expert du domaine ferait ici, et que je ne demande pas ; (2) précisez les données brutes qu'il utiliserait au départ, au lieu de celles déjà analysées ; (3) indiquez les méthodes et outils spécifiques qu'il utiliserait ; (4) expliquez ce qui, en dehors de vous ou de moi, permettrait de vérifier la validité du résultat. Ensuite, reformulez ma demande pour qu'elle réponde précisément à cette exigence. »

Règle du programme à tenir : « concluant » veut dire **lisible par des critères gelés d'avance, quel qu'en soit le sens** ; aucun run ne vise un signe positif (R3), et un résultat déjà vu ne se relit pas sous un critère changé après coup sans le déclarer (R1, R4).

## Ce qu'est R1, et ce qui vient d'arriver (à vérifier toi-même dans les fichiers)
R1 compare des moniteurs boîte blanche (sondes sur les activations de Llama-3.1-8B-Instruct) et boîte noire (petits juges de langage, prédicteur sur les traits du texte, règle de coût) sur les 2 400 actions de P3, dont les activations sont obtenues en **rejouant** les textes des actions dans le modèle. La relance du 3 novembre (table de tokenisation v3) est validée mais **partielle** : la part d'actions fidèles au rejeu est sous le seuil gelé de 80 % chez le saboteur et chez l'honnête, donc toutes les comparaisons préenregistrées sont « non concluant (rejeu partiel) ».

## Fichiers à lire (tous dans le dépôt ; ceux d'un commit se lisent par `git show <commit>:<chemin>`)
- Textes scellés : parent `prereg/R1-R2-rejeu-p3-v1.md` et addendum v3 `prereg/R1-addendum-relance-v3.md` (commit `139a81d3`) ; addendum v2 `prereg/R1-addendum-relance-v2.md` et texte du complément de validation `prereg/R1-addendum-relance-v2-complement-validation-v1.md` (commit `4b47db7b`) ; analyse principale `prereg/analyse-principale-r1-r2-v1.md` ; analyse secondaire `prereg/analyse-blanche-noire-v3.md` ; P3 `prereg/P3-premier-test-i-a-v1.md`.
- Code au commit `139a81d3` : `src/controle_ia/runs_nuit/rejeu_activations_v3.py`, `resolution_graine_v1.py`, `resolution_graine_lot_v1.py` ; table `prereg/R1-table-tokenisation-v3.json`.
- Résultats (après verdict, lisibles) : `diag/20261103-063222-r1-rejeu-reel/rejeu-activations.json` et `runs/20261103-063222-r1-rejeu-reel/manifeste.json` ; `diag/20261103-072723-analyse-principale-r1-r2-v1/` ; `diag/20261103-072805-analyse-par-episode-v1/` ; `diag/20261103-072840-analyse-blanche-noire-v3/` (sorties `.md` et `.json`).
- Verdicts des lecteurs neufs : `brouillons/preuves-mentors-v1/reception-r1-relance-v2/verdicts-R13-v1/` (trois fichiers) ; verdict du rejeu à graine `brouillons/preuves-mentors-v1/reception-rejeu-graine-v1/verdict-rejeu-graine-v1.md`.
- `registres/decisions.md`, lignes R-1279 à R-1322 (contexte ; cherche « graine », « complément », « R1 »).

## Ce qu'on te demande
Réponds à la question de Lazar, dans sa forme : (1) à (4), puis la demande reformulée. Fonde chaque affirmation sur un fichier (chemin, ligne ou clé). En particulier : d'où viennent exactement les actions non fidèles (par condition, par position dans l'épisode, par cause) ; si ce défaut se corrige sans changer de critère après coup, et comment ; ce qu'un R1 concluant montrerait vraiment, et ce qu'il ne montrerait pas ; ce qui coûte quoi (carte graphique, temps, textes à sceller). Dis aussi ce que tu ferais autrement que le programme, si c'est le cas.

## Interdits
Aucun commit, aucun `.sha256`, aucun fichier existant modifié ; **rien n'est ouvert sous `donnees/`** (les tableaux d'activations ne se lisent pas ; les résultats JSON et Markdown de `diag/` et `runs/`, oui) ; aucun `git fetch`, `checkout`, `stash` ; aucun appel de modèle autre que toi ; `WebSearch` et `WebFetch` seulement pour de la littérature de méthode (tokenisation, reproductibilité numérique, sondes) ; `nice -n 10 python3 -I -B` pour tout calcul.

## Rendu
Un fichier `/home/claude/scratch/r1-concluant-fable/r1-concluant-fable-v1.md` : (1) à (4), la demande reformulée, et un dernier paragraphe « ce que je recommanderais à Lazar, dans l'ordre, avec le coût ». Réponse finale : tes recommandations en dix lignes au plus, le chemin et le sha256 du fichier.
