# Rapport du développeur du correctif 0012 (corrections de la relecture du correctif 0011) — v1

Écrit le 2026-11-21 vers 22:50Z par le développeur du correctif 0011 (Claude Opus 5.5, effort maximal, côté saboteur), sous le même
mandat (`registres/iib-reconception/mandat-developpeur-correctif-0011-environnement-machine-v1.md`, abfe45aa9d28…) et l'accord
GO-2026-11-21-84 (les corrections seules, mot pour mot d'après la relecture de Fable 5.2, ea3ffcc0…). Pièce de classe B, à vérifier
par le même relecteur. Exploratoire, non opposable. Chemins relatifs au dossier des rendus `dev-0011/correctif-0012/`.

## Verdict
Les deux majeurs et les mineurs 3 à 10 sont traités, d'après les remarques et rien d'autre. Les deux vérifications demandées par
les majeurs reviennent positives : rien ne devient bloquant. Deux écarts déclarés : le mineur 3 (deux essais de non-régression de la
garde, à faire accepter) et l'assertion du majeur 2, qui ne lit pas le dossier des moniteurs, interdit par le mandat. Aucun code de
production n'est touché ; aucune fonction d'essai ne s'ajoute : liste figée inchangée, **275 essais attendus**. Répétition locale
entière à blanc, rejouée une fois : réussie, « 275 passed ».

## Commit, arbre, correctif
- Correctif 0012 : commit 887561b759ded1bcadb450cedead3f29e946dda7, arbre bbcd9a84a77ac667ef6f9106b19afe29ffab041f, parent
  844fda80002059682d6f66a50fe22baee126f559 (correctif 0011, arbre 95e102f9…), base 62356e2f ; branche locale `correctif-0011-local`,
  jamais poussée.
- `correctifs/0012-Organisme-retenu-du-saboteur-budget-code-en-version-.patch` (4cd18c1f2e253935c4d5d3eefb1dc76c40f77006952334cafa2c3ca9c4ad6c73) ;
  appliqué sur 844fda80 dans un index temporaire, il redonne l'arbre bbcd9a84.
- Fichiers touchés : `tests/iib_v5_outils.py`, `tests/test_iib_environnement_machine_v5.py`, `tests/test_iib_lanceur_v5.py`.

## Traitement
Remarque par remarque : `table-de-traitement-relecture-fable-correctif-0011-v1.md` (ed2aeddb…), qui donne aussi les treize
identifiants du mineur 10.

## Sorties
- Fichiers d'essais touchés, en entier (environnement de la machine, lanceur, distillateur de bout en bout, configuration), sur
  l'arbre commité ensuite tel quel : `sorties/essais-fichiers-touches-apres-correctif-0012.txt` (be75a89d…), « 54 passed ».
- Répétition : `sorties/repetition-locale-correctif-0012.txt` (2a5904f4…), « RÉPÉTITION RÉUSSIE » ; suite figée de l'amorce,
  `sorties/suite-figee-repetition-correctif-0012.txt` (4b2acf17…), « 275 passed in 474.16s » (liste v5, f9ff477d…, nombre contrôlé).
- Preuves jointes : majeur 1, `sorties/preuve-majeur-1-emplois-de-cf-et-de-session-v5.txt` (e725a1df…) ; majeur 2,
  `sorties/preuve-majeur-2-extrait-lanceur-v5.txt` (cc8869d1…) ; mineur 7, `sorties/preuve-mineur-7-greffons-pytest-machine.txt`
  (998769c6…) ; mineur 9, `sorties/preuve-mineur-9-nombre-attendu.txt` (912bb785…).

## Réserves
1. Le masquage de la carte par `CUDA_VISIBLE_DEVICES` vide n'est vérifié avec le vrai torch que sur la machine (inchangé depuis le
   correctif 0011).
2. Relance : un ordre et une configuration neufs (mère), avec `IIB_TESTS_ATTENDUS=275`. 271 reste écrit dans les ordres de
   l'étalonnage (brouillons 3 à 8) et dans les générateurs des brouillons 3 et 4. Un `TESTS_ATTENDUS` vide, permis par l'amorce,
   n'y contrôle que le succès, sans le nombre (comportement existant, non changé).
3. Mineur 7 : 48 des 72 paquets de la machine sont absents du poste ; leurs greffons de pytest éventuels n'ont pas été lus.
4. Toujours hors du mandat : l'erreur de chaîne de consignation C-V4-1.
5. Rendus de ce tour : ce dossier seulement. Les dossiers temporaires sont sous `dev-0011/temporaire-0012/`, qui n'est pas un rendu.
   Ceux du premier tour restent où ils sont, car la suppression m'est interdite. Dans le dépôt principal, `git status` montre que la
   copie de mon premier dossier (`brouillons/ii-b-saboteur-budget-v5/code-v5/correctif-0011/`) porte ces dossiers temporaires et des
   dépôts emboîtés (onze entrées) : je n'y ai rien écrit, c'est à la mère d'en décider.
