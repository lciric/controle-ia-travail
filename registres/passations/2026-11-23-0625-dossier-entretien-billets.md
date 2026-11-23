# Passation — session « dossier de l'entretien et billets » — 2026-11-23T06:25:54Z (GO-2026-11-23-09 : reprise possible sur un autre compte)

Session : `session_013QMayjKyt5mDCM75rv1ncu` (Opus 5.5). Branche : `main` (rien en dehors). Aucun résultat lu, aucune dépense.

## Mandat
GO-2026-11-22-113 : préparer le dossier de l'entretien du 1er décembre et les billets. Les pièces visées :
- l'erratum interne et le programme v3 (demande 27) ;
- la note des problématiques v2 ;
- la note « Diffuse AI Control on Fuzzy Tasks » et ses trois sources ;
- la carte des voies, contre-lue ;
- l'état des billets.

## Fait
- Voir la passation précédente, `registres/passations/2026-11-22-1826-dossier-entretien-billets.md` (4046a09a…), et son additif 1 (c20d50a8…).
- Commits sur main :
  - ff12c703, 0651a676 : application à blanc de la demande 27, contre-lecture, erratum 1, programme v2 ;
  - 435726aa, 7f6cdb6b, 3ff8631e : carte des voies, contre-lecture, v2, vérification, erratum 1 ;
  - e50edee2 : compte rendu et passation ;
  - b0ad3438 : additif sur les tests.
- Versement du bloc-notes ce jour : `docs/notes/dossier-entretien-2026-12-01-v1/versement-bloc-notes-2026-11-23-v1/` (19 fichiers, compagnons `.sha256`, LISEZMOI).

## Reste
- Décisions de Lazar :
  - les quatre de la demande 27 ;
  - les six de la demande 26, dont deux en divergence avec ses mots ;
  - le nœud d'antériorité du papier C face au juge durci.
- Après la décision 1 de la demande 27 : scellement provisoire du programme v3, puis note des problématiques v2 complète.
- L'objection 1 de la note v6, à corriger par qui en a le mandat.
- Le billet sur les sondes revient à une session qui a droit aux résultats.
- Assemblage du dossier le 28.

## Réserves
- La suite de tests n'est pas jouée en entier. Un échec est signalé dans le chantier du barreau 5 (MIN_ESSAIS 235 contre 814 essais).
- Taylor et al. et Taufeeque et al. ne sont cités dans la carte v2 que d'après la note v6.

## Prochaine action
Lire la réponse de Lazar à la décision 1 de la demande 27. Puis appliquer avec `appliquer_erratum_demande_27_v2.py`, en reportant les corrections jumelles et les renvois orphelins listés dans l'erratum 1 du rapport. Ensuite, scellement provisoire.

## Tâches planifiées et instances actives
Aucune.
