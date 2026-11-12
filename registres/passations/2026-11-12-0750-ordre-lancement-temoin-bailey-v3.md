# Ordre de lancement v3 — témoin de l'attaque publiée de Bailey — 12 novembre 2026, vers 07:50 UTC

Session « attaquant informé » `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Écrit
**avant la création** (procédure `2026-11-11-1624-…`, étape 5 ; condition 8). Ne se réécrit pas (R12). Suit
`2026-11-12-0020-…` (`d67b6f7e…`, lancement v2 interrompu, instance 60280913 détruite).

## Mots et constats
- Mot de Lazar (≈ 07:42 UTC) : « relance le témoin de Bailey sur la même offre ».
- **L'offre 57426822 (Oregon) n'existe plus** à 07:47 UTC. Seule offre conforme : **60035968**, moins chère et meilleure
  sur tous les critères du devis. Retenue pour honorer « relance » sans attendre ; écart à la lettre du mot, signalé ici
  et à Lazar.
- Cause de la mort de la conduite v2 : le PID consigné (6007) était celui du parent de `setsid`, sorti aussitôt ; la
  conduite et son veilleur sont morts vers 00:09:51 UTC, à la coupure d'une réponse par un classifieur ; la machine de la
  session a ensuite été éteinte pendant l'inactivité (redémarrée à 07:42:33 UTC, fichiers gardés). Test : un processus
  détaché (`sleep`) a **survécu à une fin de tour** (07:43 → 07:47 UTC). Risque déclaré : extinction de la machine
  pendant l'inactivité ; parade : réveils au plus toutes les 60 minutes ; au-delà, chien de garde de l'instance (arrêt
  après 7 200 s de pilotage muet) et reprise (lecture 38).

## Ordre
| Champ | Valeur |
|---|---|
| GO | `GO_ID=GO-2026-11-10-10` (amendé `GO-2026-11-11-01`, modèle `GO-2026-11-11-02`), `origin/main` `8b2e229ec8ab6cd031db24d7bb76204c95d50061` (2026-11-12T07:46:11Z) |
| B | **75 USD** (fixé à la création de 60280913, première instance du poste) ; arrêt à B − 2 |
| D avant création | ≈ 0,31 USD (instance 60280913, comptée dans `instances_anterieures`) |
| Offre | **60035968**, A100 SXM4 80 Go, Japon, 256 Go de mémoire, fiabilité 0,997, vérifiée, CUDA 13.2 |
| Taux relevé (recherche, 07:47 UTC) | 1,149 USD/h hors stockage ; ≈ 1,24 USD/h avec 200 Go ; c réel relevé par la conduite |
| Image | `runpod/pytorch:2.4.0-py3.11-cuda12.4.1-devel-ubuntu22.04` |
| `DEPOT_URL` | `https://github.com/lciric/controle-ia-travail.git` |
| Commit du code | `4988f3f442c670887a0e8ad15ddfbac68a173d03` |
| Manifeste | `runs/temoin-bailey-v1-20261111/manifeste-local-v3.json` (`69143b99…`) |
| Script | `runs/temoin-bailey-v1-20261111/lancer-conduite-v3.py` (`48b0d8cd…`) ; PID écrit par le script dans `lancement-v3.pid` |
| Sortie | `/home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/sortie-conduite-v3` |
| Addendum 2 du témoin | déposé chez le tiers le 2026-11-11T23:13:50Z |
