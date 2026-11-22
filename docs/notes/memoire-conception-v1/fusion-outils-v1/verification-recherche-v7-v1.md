# Vérification de l'outil borné v7 (V1 et V2) — v1

Vérificateur : Claude Sonnet 5.5, 22 novembre 2026 ; `recherche_bornee_v7.py` et `test_porte_perimetre_v2b.py`. Même cloisonnement ; rien modifié ; essais dans `/tmp/cl/pp3` (dépôt jetable `/tmp/cl/r4`). Les 15 essais passent.

## Constat : V1 et V2 corrigés, aucun défaut restant

- **V1 (concurrence)** : le scénario à 12 lectures parallèles, rejoué trois fois de suite sur un journal neuf : à chaque fois 12 lignes, témoin `n = 12`, aucune erreur d'écriture, porte `tient`, 0 manquement (la v6 donnait témoin 10, chaîne rompue, `tombe`). Huit `chercher` parallèles : `tient`, 16 lignes (une par fichier correspondant), 0 manquement.
- **V2 (`--depot`)** : `--depot <clone>` → « unrecognized arguments » ; `MEMOIRE_DEPOT` absent ou pointant un dossier sans `.git` → `ARRET`. Le scénario du clone n'est plus possible par option.
- **Limite déclarée, vérifiée telle quelle** : un agent qui pose lui-même `MEMOIRE_DEPOT=<clone>` (avec `origin/main` repointé) lit de nouveau le contenu de la branche exclue, la ligne de journal allant dans le clone. C'est la même limite que pour le rôle et la session (environnement posé par un agent de même privilège), déjà déclarée ; la porte ne la voit que si une session déclarée n'a aucune ligne dans le vrai dépôt.

Remarque : le fichier `.verrou` s'ajoute dans `journaux-outil/` ; la porte l'ignore, sans effet.
