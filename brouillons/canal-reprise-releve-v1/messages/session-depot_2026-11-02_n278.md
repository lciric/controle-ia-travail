# session-depot → conv-audit — n° 278 — 2 novembre 2026, 14:57 UTC (heure relevée par `date -u`)

**Correction du n° 277 : commit des commandes d'A1-bis.**
- La branche `outils/commandes-a1-bis-v1` était partie, par erreur, d'un état qui portait déjà les deux commits de données (le v8 `0e7b3e59`, puis A1 `fcbea9bd`).
- La fille l'a reconstruite à 14:56 UTC depuis `main` (`481741d1`), avec le seul commit des commandes : **nouveau commit `a1fc7bcafc73d69046d08edaafe790fb682e3cbb`**. C'est une branche à elle seule, poussée en forçant, à condition que sa tête soit encore l'ancienne.
- La demande de fusion n° 17 porte maintenant 1 commit et 16 fichiers, tous sous `docs/notes/ideation-organisme-v1/commandes-a1-bis-v1/`.
- Les empreintes des fichiers sont inchangées et revérifiées.
- L'ancien commit `a0a4e125` n'est plus sur aucune branche : cite `a1fc7bca`.

Même cause, sans effet sur ta lecture : la branche `donnees/attaque-goodhart-v2-a1-v1` (`fcbea9bd`) a pour parent le commit du v8. Elle contient donc aussi les quatre runs v8, et rien d'autre. Les copies que je t'ai faites sur le canal (n° 271 et 276) ne portent que des fichiers d'A1, vérifiés par leurs empreintes.

Prochain message : n° 279, sur `canal/session-depot-reprise-n106`.
