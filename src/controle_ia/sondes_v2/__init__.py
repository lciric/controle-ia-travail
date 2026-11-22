"""Sondes de la boîte blanche, version 2 (GO-2026-11-22-126, décision 2 ; consigne du développeur v1,
`docs/procedures/sondes-v2/consigne-developpeur-code-sondes-v1.md`).

Briques :
- A `magasin_v1` : magasin d'activations gardées (séries, manifeste empreinté, lecteur gardé) et adaptateur du format
  `ActivationsDemi` ;
- B `formes_closes_v1` : sondes en forme close, au processeur (score d'une action : maximum sur ses jetons) ;
- C `lecture_v1` : validation croisée imbriquée, gel avant épreuve, statistiques et gardes ; `statistiques_v1` :
  statistiques redéfinies par l'erratum 1 de la consigne (étalon, identité, rejeu croisé, Holm, libellés) ;
- D `monde_plante_v3` et `programme_monde_plante_v3` : épreuve à vérité plantée (errata 1 et 2 ; texte scellé des
  diagnostics préalables).

Aucun module de ce paquet n'importe torch lui-même ; calcul en double précision ; graines par
`numpy.random.SeedSequence` (R9).
"""
