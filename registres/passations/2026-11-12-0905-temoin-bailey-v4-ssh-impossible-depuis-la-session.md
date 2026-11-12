# Témoin de Bailey — run v4 : `ssh` impossible depuis la session ; instance 60330510 détruite par la conduite — 12 novembre 2026, 09:05 UTC

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Suit l'ordre v4
(`2026-11-12-0830-…`, `acf89cbc…`). Ne se réécrit pas (R12).

## Verdict
**Pas de run, pas de verdict. Cette session ne peut pas être le poste du témoin**, quel que soit le maintien de sa
machine : elle ne peut ouvrir aucune connexion `ssh` vers une instance. D du poste : **1,54 USD** ; B reste 75 USD.

## Faits
- Conduite v4 (PID 1206) lancée à 08:27Z ; machine tenue allumée (même démarrage, 08:07:58, du début à la fin).
- Instance 60330510 créée à 08:27:14Z, c = 1,6071 USD/h. La conduite n'a jamais obtenu `ssh … true` ; après
  `DELAI_PRETE_S` (1 800 s) : « instance non prête dans le délai (état « running » et ssh) : arrêt et destruction »,
  `detruite: true`, D = 1,537 USD (bilan `sortie-conduite-v4/bilan-conduite-v5.json`). Conduite terminée à 08:58:15Z.
  Absente de l'inventaire à 08:58Z.
- Cause établie : connexion TCP brute vers le port 22 refusée (`/dev/tcp/github.com/22` : « Connection refused »), le
  port 443 ouvert ; le mandataire de sortie de la session ne porte que le HTTPS sur 443 (`/root/.ccr/README.md`, « Not
  supported through the proxy (report, do not work around) ») ; réseau de l'environnement déjà « non restreint »
  (`get_environment`). Les ports `ssh` de Vast (direct ou relais) sont hors de portée. Cause probable aussi de la
  conduite v3 (aucune étape « instance prête » à 07:54Z, instance pourtant « running » avec `ssh`).
- Les autres runs Vast du programme démarrent l'instance par son point d'entrée et poussent leurs résultats par `git` :
  ils n'ont pas besoin de `ssh`. `lanceur_v13` en a besoin à chaque étape.

## Ce qu'il faut
Un poste qui atteint les ports `ssh` de Vast et reste allumé environ 5 heures : (b) un ordinateur de Lazar partagé par
le pilotage à distance (aucun dossier partagé à 08:10Z), ou (c) une petite machine louée (dépense hors ligne de GO :
GO requis). Changer le code pour se passer de `ssh` serait une version nouvelle du code et de l'addendum (nœud).

## Instances actives créées par cette session
Aucune. Tâches d'arrière-plan et réveils de cette série arrêtés.
