# Témoin de Bailey — run v3 perdu à l'extinction de la machine de la session ; instance 60326443 détruite — 12 novembre 2026, 08:15 UTC

Session `session_01XJ6MgnEhQMZteN9F8a1BST`, branche `claude/compassionate-meitner-d4ryyk`. Suit l'ordre v3
(`2026-11-12-0750-…`, `c60255c5…`). Ne se réécrit pas (R12).

## Verdict
**Pas de run, pas de verdict.** La conduite v3 ne peut pas vivre dans cette session : la machine s'éteint quelques
minutes après la fin d'un tour, et tous ses processus meurent. Dépense du poste : D ≈ 0,73 USD (60280913 ≈ 0,31 ;
60326443 ≈ 0,42). B reste 75 USD.

## Faits
- Conduite v3 lancée à 07:48:36Z (PID 949, vu vivant à 07:54:00Z, 5 min 23 s). Instance 60326443 en marche, `ssh` prêt,
  à 07:54Z. Fin de mon tour vers 07:54Z.
- Dernier battement du veilleur (PID 960) : 07:58:39Z. Machine redémarrée à 08:07:58Z (`uptime -s`), à l'arrivée d'un
  message de Lazar. Aucun processus de la conduite vivant ; aucun bilan ; journal limité à la création et à l'ordre.
- Test antérieur : un `sleep` détaché avait survécu à 4 minutes d'inactivité (07:43 → 07:47Z). Le délai d'extinction
  est donc d'environ 4 à 5 minutes d'inactivité, non documenté.
- La nuit : même cause (machine éteinte de 00:20 à 07:42Z) ; la mort de la conduite v2 à 00:09:51Z est contemporaine
  de la coupure d'une réponse par un classifieur.
- Instance 60326443 sans tâche : détruite par l'identifiant à 08:08:49Z (R14, R10). Réveil de surveillance de 08:20Z
  supprimé.

## Ce qui en découle
Le pilotage local (`lanceur_v13.Conduite`) doit tenir au moins la mise en place, le contrôle du juge, le pilote et le
lancement du run principal (≈ 5 h attendues) ; ensuite l'instance finit le run principal sous ses gardes et s'arrête
d'elle-même (lecture 37 (b)), et une reprise rapatrie (lecture 38). Il faut donc un poste qui reste allumé. Décision à
Lazar (voir le message de la session).

## Instances actives créées par cette session
Aucune.
