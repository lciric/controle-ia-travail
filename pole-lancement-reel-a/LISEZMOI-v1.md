# Pôle « scientifique automatique » — premier lancement réel, option (a) (v1)

Lancé le 27 octobre 2026 par l'instance « session-depot », sous **GO-2026-10-27-05** (mot de Lazar : « go 30 USD pour (a) » ; R-561, R-563, R-567), avec l'orchestrateur v6 de conv-audit (`canal/conv-audit-n04`, commit `0b9efe2`, empreintes `EMPREINTES-orchestrateur-pole-v6-v1.txt` `1720f165…`, vérifiées), sans aucune modification.

- Relais (`pole/relais_reel.py`) : 127.0.0.1:8787, plafond 30 USD, réserve 0,25 USD par appel ; clé `RR_ANTHROPIC_API_KEY_LUC` dans son seul environnement. Journal : `RELAIS.jsonl` (coût réel par appel).
- Orchestrateur : `env -i` (aucune variable de clé), `python -I -B pole --moteur claude-sdk --confirmer-moteur-reel --url-relais http://127.0.0.1:8787 --selection pari --monde-noyau exemples/monde-pari-demo-v1.json --noyau-secret --population exemples/population-pari-demo-4traits-v1.json --temoins exemples/temoins-pari-demo-4traits-v1.json --generations 2 --budget-usd 30 --modele-experimentateur claude-opus-5-5 --modele-verificateur claude-fable-5-1 --modele-recombinaison claude-opus-5-5 --modele-synthese claude-opus-5-5`. Python : `claude-agent-sdk` 0.2.174, numpy 2.5.4 (`pip-freeze-pole.txt`) ; Claude Code 2.1.311.
- Un faux départ sans dépense à 14:34:09 UTC (`python -I -m pole` : module introuvable en mode isolé ; `orchestrateur-sortie-faux-depart.txt`) ; course de 14:34:31 à 14:40:17 UTC.

Résultat : **deux générations, arrêt « nombre de générations atteint », 140 appels (Opus 5.5 : 91, 2,18 USD ; Fable 5.1 : 49, 4,06 USD), 6,24 USD, aucun refus du relais.** Qualité cumulée : témoins faux testés 2, gardés 0 ; témoins vrais testés 3, éliminés 0. Statuts : survit 2, éliminée 3, indécise 2, retirée 3, refusée (redite) 1.

**Réserves.**
1. **Bac à sable inactif** : le kit l'annonce à chaque agent (« sandbox is enabled but dependencies are missing: bubblewrap (bwrap) not installed, socat not installed ; commands will run WITHOUT sandboxing ») : réseau et système de fichiers des agents n'étaient pas bornés par le bac à sable ; seules la garde des outils (`pole/garde_outils.py`) et l'absence de clé dans leur environnement tenaient. À corriger avant tout lancement suivant (installer `bubblewrap` et `socat`, ou refuser de partir sans bac à sable).
2. La garde des outils a bloqué deux rejeux légitimes (faux positifs de chemins : « /len », « /120 », « ~ ») : une vérification est restée « indécise » faute de rejeu (journal de la génération 0).
3. Monde tautologique : rien de scientifique n'est attendu ; c'est un essai de la chaîne réelle.
