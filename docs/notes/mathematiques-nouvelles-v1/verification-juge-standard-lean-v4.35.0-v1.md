# Vérification sans dépense : la commande du juge standard de Lean existe à la version épinglée (D-B2) — v1

- Nature : note de travail (classe C). Session des mathématiques nouvelles, 2026-11-22T10:43Z (`date -u`). Lecture de sources publiques seulement ; aucun essai, aucune machine, 0 USD.
- Sources : `docs/sources/web/lean-v4.35.0-juge-standard-v1/` (provenance et empreintes au dossier).

## Constat

1. Version épinglée : la consigne v11 du poste Lean (ligne 488) épingle Mathlib au commit `56a005855ea17e0b0958f73ec801ae140b0a1679` ; le fichier `lean-toolchain` de ce commit porte `leanprover/lean4:v4.35.0` (`ca5f1f60…`).
2. Au tag `v4.35.0` du dépôt de Lean, l'aide de Lake (`src/lake/Lake/CLI/Help.lean`, `82e09cc8…`) liste, ligne 33, « comparator — judge a solution against a challenge », et, ligne 34, « check — check this project against external checker(s) » ; lignes 403 à 412 : `lake comparator [--config <FILE>] [--challenge-from-export <FILE>] [--solution-from-export <FILE>] [--paranoid] [--inadvisably-no-sandbox]`, qui « établit que chaque théorème nommé de la solution prouve le même énoncé que le défi, n'emploie aucun axiome hors de la liste permise, et est accepté par » le noyau (texte à la suite dans le fichier) ; le bac par défaut est `bwrap` (ligne 488, variable `COMPARATOR_BWRAP`). Le répartiteur de commandes de `Help.lean` route « comparator » (ligne 945).
3. Cela concorde avec la notice du dépôt Comparator déjà versée (`docs/sources/web/mathematiques-nouvelles-methodes-v1/leanprover-comparator-README.md`) : intégré au cœur de Lean depuis v4.35.0 sous `lake comparator` et `lake check`.

## Ce que cela n'établit pas

- La commande **existe dans les sources** de la version épinglée ; elle n'a été **ni compilée ni exécutée** ici. Son bon fonctionnement sur le poste (présence de `bwrap`, droits du bac) se vérifie au prochain essai de l'outillage, qui appartient au poste de Lazar et à son brief.
- Rien sur la bibliothèque de statistique Lean ni sur sa compatibilité avec v4.35.0.
