"""Simulation d'essaim, v1 : surveillance par agent contre statistique de niveau essaim.

Axe des agents du lemme et du théorème négatif (note mathématique v3, sections 3 et 4), en miroir de
T0.3 (axe du temps). Monde à K agents × T pas ; scores tirés des lois de T0.3 (`simulation_t03.lois`).

Modules :
- `statistiques` : statistiques vectorisées sur un lot (R, K, T), groupes d'invariance exacts ;
- `references` : références scalaires (boucles), pour la garde d'équivalence ;
- `menaces` : classe C par sous-groupe (agents dans un pas, temps dans un agent, toutes les cases)
  et classe M (budget concentré, synchronisé entre agents, étalé dans le temps) ;
- `calibrage` : seuils (exacts, aléatoirisés pour les statistiques discrètes, Monte-Carlo, Ville,
  conforme sur essaims entiers), formes closes et bornes ;
- `blocs` : comptes bruts par cellule, sans lecture ;
- `lecture` : critères gelés, intervalles exacts de Clopper-Pearson ;
- `run_essaim` : lancement sous préenregistrement scellé, graine racine dérivée de son empreinte.
"""
