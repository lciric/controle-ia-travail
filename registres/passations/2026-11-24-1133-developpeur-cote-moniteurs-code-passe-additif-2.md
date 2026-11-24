# Passation — développeur du côté des moniteurs, code de la passe sous l'additif 2 (barreau 8) — 2026-11-24 11:33Z

Session fille de la mère `session_01Qi7Gr3Ggccg85kjmP654WC` ; Opus 5.5, effort élevé ; jamais exposée au saboteur. Branche `barreau8/code-passe-additif-2-v1` (tête `ddb71a98` avant cette passation), fusionnée sur `main` par la mère.

## Fait
- Inscription « qui a lu quoi » avant toute lecture (v1) et en fin de travail (v2) : `docs/notes/barreau8-code-passe-additif-2-v1/qui-a-lu-quoi-developpeur-cote-moniteurs-v1.md` et `-v2.md` (écart déclaré sans lecture : un `git fetch` a rapatrié les références des branches de la course, jamais ouvertes).
- Programme de comparaison réécrit de zéro à partir des additifs 1 et 2 : v2, puis v3 après contre-lecture (`src/controle_ia/barreau8_moniteurs/comparer_interface_v6_v7_v3.py`, 49 essais).
- Table neuve des constantes (M-4) : `docs/notes/barreau8-cote-moniteurs-sorties-v1/constantes-reportees-additif-2-v1.json`, `d576c16b…`, « report » ; pièce de comparaison réécrite `comparaison-interface-v6-v7-v2.json`, `0554c544…`, mêmes états que la v1.
- Passe de recalcul v6 : `src/controle_ia/barreau8_moniteurs/passe_recalcul_v6.py`, `f3228b4b…` (M-1 à M-5, gardes P0 à P10 redéfinies) ; essais `tests/test_barreau8_moniteurs_passe_v6.py` (145) et `tests/test_barreau8_moniteurs_passe_v6_complements_v1.py` (10) ; notice `docs/notes/barreau8-cote-moniteurs-sorties-v1/notice-passe-recalcul-v8.md`, `16798bd6…`.
- Contre-lecture de conformité par Sonnet 5.5 (« à corriger », aucun bloquant), corrections, vérification par le même contre-lecteur (« conforme ») : rapports dans `docs/notes/barreau8-code-passe-additif-2-v1/`.
- Bordereau du code `registres/bordereau-code-passe-barreau8-v6.json`, `74736c49…` (dix clés, commit `1f16e86e`, accord GO-2026-11-24-13) ; ligne `CODE-PASSE-IIB` proposée, inscrite par la mère (R-5268, commit `c3e81879`) ; garde P0 jouée à blanc sur le dépôt réel : tenue.
- Extrait réel du côté exposé (`1ff87c08…`) accepté par le lecteur d'extrait de la passe, contrôlé par programme sans affichage.

## Reste
- Code de la lecture des sondes v6 : non livré (écart accepté par la mère) ; cahier des charges `docs/notes/barreau8-code-passe-additif-2-v1/cahier-des-charges-lecture-sondes-v6-v1.md` ; session dédiée à lancer par la mère après le départ de la passe.
- Côté exposé : `verifier-entrees` puis `essai-a-blanc` sur la machine avant la carte (notice v8).

## Réserves
- Le code n'a jamais tourné sur le vrai fichier des identifiants, le vrai jetoniseur ni la carte : l'égalité des deux décodages et la borne du vocabulaire seront vues par `verifier-entrees`.
- La passe ne refuse par empreinte que le rapport de conformité de la version 5 ; le chemin de la table neuve est fixé par le bordereau, non par le code (déclaré, notice v8).

## Prochaine action
Aucune pour cette session : arrêt sur le mot de la mère.

## Instances actives
Aucune : aucune machine louée, aucune dépense.
