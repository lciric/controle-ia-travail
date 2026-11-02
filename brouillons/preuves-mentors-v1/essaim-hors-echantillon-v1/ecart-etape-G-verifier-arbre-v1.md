# Essaim hors échantillon — écart à l'étape G de la procédure (verifier-arbre), v1

Écrit par la session conv-audit le 2 novembre 2026 vers 01:00 UTC.

- **Attendu** (procédure `procedure-scellement-essaim-hors-echantillon-v1.md`, étape G) : `python -m controle_ia.scellement verifier-arbre .` affiche « arbre intact ».
- **Obtenu** dans l'arbre séparé, après le run `20261102-005426-essaim-ho` : **193 problèmes** (`verifier-arbre-apres-run-v1.txt`) : 188 sous `docs/notes/` et 5 addenda de la bisociation sous `prereg/` (`addendum-ecarts-bisociation-deux-espaces-v2-v1` à `-v5`, gardés sans compagnon à dessein, R-648). **Aucun** ne porte sur `runs/20261102-005426-essaim-ho/`, `diag/20261102-005426-essaim-ho/`, `prereg/essaim-hors-echantillon-*` ni un fichier de l'essaim ; `git status` hors des deux dossiers du run : 0 changement.
- **Lecture** : ces problèmes préexistent au run (fichiers suivis depuis longtemps, sans compagnon) ; la procédure, écrite par un sous-agent, supposait un arbre entièrement scellé. Les sceaux du run (neuf fichiers de `diag/`, le manifeste) ont été vérifiés par le lanceur et sont présents ; la fusion a été faite (commit `c23fe585`), le commit cité `7e27c30c` reste dans l'historique.
- **Conséquence** : aucune sur le run ; à signaler à Lazar comme écart à la procédure ; la dette de compagnons sous `docs/notes/` est antérieure à cette nuit.
