"""Essai « preuve formelle contre suite bon marché » (couche 4), outillage D-1a, v1.

Brouillon 3 du dessin et du devis (`brouillons/couche4-essai-preuve-formelle-v1/essai-preuve-formelle-devis-v1-brouillon3.md`,
`717259ed…`), § 3.1 (gardes G-L1 à G-L7), § 3.8 (A7, A8, A12, A13), § 4.5 (cloison, intégrité de la machine, épreuve
d'isolement). Aucun module de ce paquet n'appelle un modèle.

- `gardes_lean_v1` : gardes mécaniques G-L1 à G-L7 (autonome : copié tel quel sur la machine dédiée) ;
- `executeur_bac_v1` : exécuteur du bac sur la machine (Lean et Python sous `systemd-run` et `bwrap`, dossier neuf par
  item ; autonome : copié tel quel sur la machine) ;
- `budget_v1` : compteur de dépense, coupure A7, étalonnage A8 ;
- `garde_go_v1` : refus de tout appel facturé sans GO valide de D-1b (A12), contrôle du GO cité à la création d'une machine ;
- `minuterie_v1` et `hetzner_v1` : minuterie de destruction par identifiant (A13, R10) et client de l'API de Hetzner ;
- `sortie_v1` : sortie structurée des bras et verdicts des chaînes L et S.
"""
