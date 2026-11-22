# Audit des échanges de la mère sortante contre le dépôt — v1 (22 novembre 2026)

Programme : `audit_echanges_mere_v2.py` (classe B, non contre-lu ; la v1, qui manquait les messages arrivés en cours de tour, n'est pas gardée). Entrées : les journaux bruts de la session mère (archivés, masqués, sur la branche `archives/journaux-mere-01Qi7Gr3-v1`). Sorties :
- `mots-lazar.jsonl` : les 83 messages de Lazar à la mère, verbatim, horodatés (courriel masqué), chacun avec les lignes GO et R écrites dans les trois heures qui suivent ; seuls les trois derniers (08:06 à 08:07Z, sur cet audit) n'en ont pas.
- `consignes-aux-filles.jsonl` : les 287 messages de la mère aux sessions filles et les briefs de création.
- `mandats-agents.jsonl` et `rapports-agents.jsonl` : les 116 mandats d'agents et les 57 rapports rendus par message (les autres rapports sont dans les journaux archivés).
- `fichiers-ecrits.jsonl` : fichiers écrits par Write et Edit ; seuls absents de git : `.claude/settings.local.json` (permissions locales, hors dépôt par construction, sans secret).
Limite : « une ligne dans les trois heures » prouve une trace, pas que chaque mot a été porté ; la preuve forte est le verbatim de `mots-lazar.jsonl`, à relire contre `registres/go.md`. Reproduire : rejouer le programme sur l'archive de la branche (empreintes dans son `…-contenu.txt`).
