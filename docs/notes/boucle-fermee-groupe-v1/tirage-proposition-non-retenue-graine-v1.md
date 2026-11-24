# Tirage au hasard d'une proposition non retenue (règle 1 c du protocole X 2.1) : graine et vivier inscrits avant le tirage

- **Dossier** : collisionneur groupé sur la naissance des idées scientifiques fécondes ; note de sortie `docs/notes/collisionneur-v9/notes-de-sortie-v1/note-sortie-groupe-naissance-idees-fecondes-v1.md` (branche `idees/lot-8-chef-d-orchestre-v1`), section 8.
- **Mandat** : GO-2026-11-24-46. Écrit par la session fille de la boucle fermée le 24 novembre 2026, avant tout tirage.
- **Vivier** : toute puce de la section 8 hors des « Retenues », dans l'ordre de la note : d'abord les six puces de « À reprendre ensuite », puis les quinze puces de « Non retenues ». Une puce qui nomme deux objets compte pour une seule entrée ; si elle est tirée, ses objets sont éprouvés ensemble. Vingt et une entrées, numérotées de 0 à 20.
- **Graine** : `numpy.random.SeedSequence(entropy=2026112446)` (date du mandat et numéro de l'accord).
- **Procédure** : `rng = numpy.random.default_rng(numpy.random.SeedSequence(2026112446))` ; `i = int(rng.integers(0, 21))` ; un seul tirage. Si l'épreuve la moins chère de l'entrée tirée n'est pas sur processeur ou à moins de 5 dollars payés, le tirage et sa raison sont inscrits, et l'on ne retire pas.

| n° | entrée |
|---|---|
| 0 | Primitives hors de l'alphabet (banc sous réécriture algébrique, anti-unification, grammaire probabiliste bien typée comme nul) |
| 1 | Définitions mathlib non préfigurées |
| 2 | Coupe-circuit de la marge : réseau témoin à canal orthogonal libre |
| 3 | Transfert d'échelle sur Pythia |
| 4 | Percolation comme outil de réfutation, contre un nul auto-excité à blocs et à croissance exogène |
| 5 | Audit spectral des poids sur cohortes d'adaptateurs de même rang et même budget |
| 6 | Supermartingale écrêtée des plus hauts scores |
| 7 | Correction statique alpha - k/(n+1) |
| 8 | Boule de Huber en variation totale centrée sur la loi empirique |
| 9 | Troncature basse de la moyenne de référence |
| 10 | Test de la corde (continu contre discret) |
| 11 | Laplacien de faisceau lu comme H^1 ; sous-ensemble insatisfaisable booléen |
| 12 | Critère de non-polysémie « pour toute partition » |
| 13 | Repondération des mentions ; invariance entre genres par divergence de Jensen-Shannon |
| 14 | Signaux d'épicycles dL/dn et L_Sigma/H |
| 15 | Spectres « invariants de jauge » de W_Q W_K^T |
| 16 | Contrefactuel « d'autres copies existent » |
| 17 | Épreuve de marge où seule la sonde linéaire est attaquée |
| 18 | Banc mathlib conditionné sur les preuves refactorisées plus tard |
| 19 | Jeux d'intérêt d'experts comme cible de rétrodiction ; spaCy sur archives anciennes ; concepts OpenAlex ; MeSH non millésimé |
| 20 | Gödel et Rice comme frontières |
