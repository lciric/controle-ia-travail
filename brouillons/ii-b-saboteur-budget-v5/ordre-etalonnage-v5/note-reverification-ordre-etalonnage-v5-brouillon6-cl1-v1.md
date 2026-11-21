# Note de revérification — ordre de l'étalonnage, brouillon 6 — cl1

Date : 2026-11-21. Même vérificateur (Claude Opus 5.5), même mandat. Pièce : `ordre-etalonnage-ii-b-v5-brouillon6.md` (`4e5c156e…`, compagnon vérifié).

**Verdict : conforme ; rien d'autre n'a changé.**

- **Rejeu** : `fabriquer-ordre-etalonnage-ii-b-v5-brouillon6-v1.py`, joué sur une copie du brouillon 5 dans mon dossier (`ordre-rejeu-b6/`), rend `4e5c156e…`. Le résultat est **identique à l'octet** au brouillon 6 versé.
- **Différence entre les brouillons 5 et 6** : exactement les quatre lignes annoncées.
  - La ligne « Exécutante » : `session_01Qi7Gr6cZ3HczDtN4UYdPN9`, branche `claude/iib-executante-v5`.
  - Les trois chemins du distillateur, devenus `code-v5/distillateur-v5/correctifs/…`.
  
  Les empreintes et les vingt chevrons restent inchangés.
- **Mandat de l'exécutante** : `git fetch origin main`, puis `git show origin/main:registres/iib-executante/mandat-executante-iib-v2.md`. Il rend `b26e66eebbdd…`, égal à la citation de l'ordre et à son compagnon sur `main`.
- **Champs 1 et 2 remplis par la mère** : `git fetch origin prep/iib-code-v5` par son nom. La branche pointe sur `62356e2ff612a8228b37a8333689e8114099f3c0`, et `git rev-parse origin/prep/iib-code-v5^{tree}` rend **`ed9b0e48be367670cad0782ccb6fbe2d9ca41b87`**, l'arbre que l'ordre exige.
