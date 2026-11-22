# Vérification des corrections de la porte de périmètre (v2) — v1

Vérificateur : Claude Sonnet 5.5, 22 novembre 2026, commit `020d5d08` (`porte_perimetre_v2.py`, `recherche_bornee_v6.py`, `test_porte_perimetre_v2.py`). Même cloisonnement ; rien modifié ; essais dans `/tmp/cl/pp2` et `/tmp/cl/r3`. Les 14 essais passent.

## Verdict : corrections en partie vérifiées ; deux restes à corriger

Vérifiés par essai : P1 (journée sans lecture : ne tient que si `sessions = {}`), P4 (chaîne, numéros, témoin, session déclarée sans ligne), P5 (date et rôle), P6 (rapport écrit), P7 (fichier ordinaire au commit), journal à chemin fixe, plus d'option `--journal`, `--bras`, `--agent`. P3 est fermé contre l'erreur de bonne foi ; contre un agent de même privilège il reste la limite déclarée (essai : `MEMOIRE_ROLE=boucle MEMOIRE_SESSION=s1` pris par la bibliothécaire → lecture de la partition « mère », `tient`) : conforme à la déclaration, à ne pas présenter comme fermé.

## Restes

### V1 — À corriger (haute) : écritures simultanées du journal → chaîne rompue, la porte tombe pour de mauvaises raisons
- `recherche_bornee_v6.py` l. 80-99 (`journaliser` : lecture du témoin, ajout de la ligne, réécriture du témoin, sans verrou).
- Essai : 12 lectures parallèles par le même rôle (cas ordinaire de sous-agents d'un cycle) → 12 lignes au journal, témoin `n = 10`, un appel arrêté (`journal impossible … .temoin.en-cours`) ; la porte rend `tombe`, 10 manquements (« numéro non consécutif », « chaîne rompue »). Les mêmes 12 lectures en série → `tient`. La journée est ensuite irrécupérable (chaîne rompue pour de bon), sans fuite : défaut de fiabilité, qui rendrait la porte inutilisable avec des sous-agents parallèles.
- Correction : verrou exclusif (`fcntl.flock`) sur un fichier de verrou pendant lecture du témoin, ajout et réécriture ; `.en-cours` nommé par processus ; essai de concurrence (plusieurs processus).

### V2 — À corriger : `--depot` reste libre, donc journal, branche principale et lecture se déplacent avec lui
- `recherche_bornee_v6.py` l. 112 et 75-77 (le journal est écrit sous `--depot`) ; l. 66 (`origin/main` lu dans ce dépôt).
- Essai : clone du dépôt, `git update-ref refs/remotes/origin/main origin/lot/compte-4-v1`, puis `lire registres/decisions.md --commit <sha de la branche exclue> --depot <clone>` avec `MEMOIRE_ROLE=reponse` → le texte propre à la branche exclue est montré ; la ligne de journal est écrite dans le clone. La porte, qui juge le dépôt de la mère après une autre lecture honnête (une ligne), rend `tient`. C'est le contournement de C7 et de la trace que la v6 devait fermer ; le même privilège suffit, mais la limite déclarée ne cite que l'environnement, et ici un argument d'option suffit (aucune écriture d'environnement).
- Correction : retirer `--depot` ; chemin du dépôt (et du journal) fixé par une variable posée par le lanceur, et refus si le dépôt n'est pas celui du lanceur ; la porte pourrait aussi exiger que le dossier de journaux soit sous le dépôt qu'elle juge (déjà le cas) et qu'une session déclarée n'ait pas de lecture visible en dehors (impossible à voir : à déclarer).

## Remarques
- `e.get("n") != i` : `true` vaut 1 en Python ; sans conséquence (seul un auteur de lignes forgées en profite).
- Un témoin illisible dans l'outil lève `ValueError`, rattrapé : arrêt propre, bien.
- `empreinte` n'est toujours pas journalisée (16 signes d'un fichier ouvrable seulement) : sans conséquence.
- Essais manquants : écritures concurrentes (V1) ; `--depot` hors dépôt de la mère (V2) ; journal à jour vide + témoin absent avec `sessions = {}`.
