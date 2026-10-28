# Note de portage — ControlArena — v2 : étape 0 faite (lecture du code installé)

De : conv-audit, le 2026-10-26 16:58:09 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne). Complète la v1
(`700e0804…`), qui reste telle quelle. Régime : exploration (Lazar, 26 octobre, 17:46 heure de Paris : « élague tout ce que
tu peux »). Aucune dépense.

## Ce qui a été fait

`control-arena` 20.1.1 installé dans un environnement isolé (avec `inspect-ai` 0.3.285) ; code lu, rien exécuté sur un
modèle. Faits établis sur le code installé (non plus sur des pages web) :

1. **Interface des moniteurs** (`control_arena/monitor/_monitor.py`, `_types.py`) : un moniteur est une fonction
   `async (state, tools) -> MonitorResponse(suspicion_score, reason)` décorée par `@monitor`, qui écrit sa réponse dans
   les métadonnées du dernier message de l'agent. Un moniteur « sonde » tient donc en quelques lignes, **à condition que
   le score de la sonde soit déjà dans ces métadonnées**.
2. **Activations** (`inspect_ai/model/_providers/hf.py`, `util/hidden_states.py`) : avec `hidden_states=true`, le
   fournisseur local rend les états de chaque pas de génération et de chaque couche dans `ModelOutput.metadata` — **pas
   dans le message** que voit le moniteur —, convertis en listes imbriquées `[pas][couche]` pour le journal. Pour un modèle
   de 8 milliards (33 couches × 4 096 valeurs par jeton généré), c'est de l'ordre du gigaoctet par trajectoire : **à ne pas
   activer**.
3. **Pont boîte blanche retenu** : une politique non fiable propre (le module `control_arena/policy` le permet) qui sert
   le modèle ouvert avec un crochet sur la seule couche de la sonde, projette sur la direction de la sonde **au moment de la
   génération**, agrège par action selon la règle gelée du programme (jamais moyenne ni médiane sur les jetons dans une
   sonde de production) et n'écrit dans les métadonnées du message que le score ; le moniteur « sonde » le lit. Le juge
   boîte noire voit la même trajectoire (appariement information × accès de FI-06).
4. **Ce qui ne peut pas tourner ici** : les environnements tournent dans des bacs à sable Docker (`compose.yml` pour
   `Apps`) et leurs données viennent de Hugging Face ; ce conteneur a un client Docker sans démon. L'étape 1 se fait sur
   une instance à carte avec Docker (Vast.ai, chez session-depot).

## Ce qui change au devis

Rien au montant (étape 1 : **40 $ au pire cas**, sur le mot de Lazar chez session-depot) ; l'instance doit avoir Docker, et
l'étape 1 commence par écrire la politique « sonde » et le moniteur « sonde » (code, quelques heures de session), avec la
direction de sonde, la couche et la règle d'agrégation **prises des pièces du programme** (T0.7), jamais inventées.
