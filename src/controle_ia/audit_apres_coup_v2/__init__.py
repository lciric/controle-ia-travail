"""Audit après coup — instruments sur mondes simulés (v1).

Spécification : `docs/notes/chantiers-21-novembre-v1/conceptions-v2/conception-3-audit-apres-coup-v3-consolidee.md`
(sha256 e3979498…). Pièces de classe B (instrument) : elles éprouvent du code, non le monde. Aucun modèle, aucun
appel réseau, aucune sonde du programme : tout est tiré par le harnais simulé, sous jeton de provenance « monde planté ».

Modules, dans l'ordre d'écriture de la spécification :
- `graines` : flux de tirage séparés par canal (rang 1) et jeton de provenance (section 5) ;
- `journal` : journal en ajout seul, à horloge logique (rang 2) ;
- `regle_audit` : la règle d'audit en trois parts (rang 3) ;
- `oracle_simule` : l'oracle simulé, couverture q, faux « endommagé » f, délai L (rang 4) ;
- `simulateur` : le monde planté et sa simulation (section 1) ;
- `estimateurs` : estimateur pondéré, strate du plancher, budget, courbe sécurité-utilité (rang 5) ;
- `alerte` : alertes en régime de signature et d'excès, latence (rang 6) ;
- `table_seuil` : la table du seuil (rang 7, section 4) ;
- `gardes_invariants` : les gardes des quatre invariants (rang 8, section 6) ;
- `attaque_choisie` : la famille plantée « attaque choisie » (rang 9, section 2) ;
- `score_trompeur` : le score trompeur planté (rang 10, section 3) ;
- `harnais_simule` et `epreuves_boucle` : le harnais simulé (interdit entier par défaut, mode « bras de flux » planté
  étiqueté « non en vigueur », enclave à jetons de capacité) et les treize épreuves (rang 11, section 5) ;
- `echelons_simules` : l'échelle des échelons simulée (rang 12) ;
- `simulations_longues` : script séparé des simulations longues (hors des essais).

Épreuves 1 et 13, mode « bras de flux » planté et échelle écrits sur le mot du directeur (GO-2026-11-22-57), sur
harnais simulé seulement. Non écrits : devins, bras « correction tirée au hasard », devis et étape 1 de la boucle.
"""
