# Pôle « scientifique automatique » — course de contrôle « (a) bis » (moteur réel)

Lancée le 27 octobre 2026 par l'instance « session-depot » sous **GO-2026-10-27-10** (délégation GO-2026-10-27-08 ; proposition de conv-audit, messages n° 111 et n° 112 ; R-581). Orchestrateur v7 version 5 de conv-audit (commit `5ac9cb6` de `canal/conv-audit-n04`, empreintes `81bd0204…`, 86 fichiers ; 184 essais OK sur la machine de lancement). Commande du LISEZMOI v5 telle quelle : relais de clé à part (`--plafond-usd 15`, réserve 0,40 USD par appel, clé `RR_ANTHROPIC_API_KEY_LUC`, jamais dans l'environnement de l'orchestrateur), orchestrateur `env -i … python -I -B pole --moteur claude-sdk --confirmer-moteur-reel … --generations 2 --budget-usd 15`, Opus 5.5 (expérimentation, recombinaison, synthèse) et Fable 5.1 (vérification) ; même monde que (a) ; témoins avec agents.

- `course/` : sortie de l'orchestrateur (manifeste : `bac_a_sable.actif` vrai, « bwrap et socat présents ; bwrap s'exécute, réseau isolé »).
- `orchestrateur-sortie.txt` : bilan final (code 0) ; `RELAIS.jsonl` : 136 appels, tous en statut 200, 5,89 USD (Opus 79, Fable 57) ; `relais-sortie.txt`.
- Relais arrêté par l'identifiant de sa tâche de fond ; port relu fermé.

Lecture (L1)–(L6) fixée par conv-audit avant la course (n° 112, point 3) : à faire par conv-audit. Rien n'est lu ici ; le bilan brut paraît propre (2 témoins vrais jugés et promus, 2 faux jugés et éliminés) : réserve de symétrie (R4) à appliquer à la lecture. Recherche de secrets sur les 461 fichiers versés : aucun.
