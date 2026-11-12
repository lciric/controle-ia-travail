# Consigne : contre-lecture de l'écart 2 de P3-bis (code et addendum 2, brouillon 1) — v1

Session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`, écrite le 2026-11-12 à 21:25 UTC (heure relevée par `date -u`). Destinataire : un **lecteur neuf** (Claude Fable 5.2, autre modèle que le développeur et le rédacteur, tous deux Claude Opus 5.5), qui n'a écrit ni la chaîne de P3-bis, ni l'écart 1, ni l'écart 2. **Aucune dépense, aucun appel de modèle, aucune instance, aucun appel à l'interface de Vast.**

## Interdits, recopiés mot pour mot (`docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md`, `1ee3b370…`)

# Interdits communs aux sous-agents de la session mère `session_01QPDgKgACWyCkCN8HjqwNXy` (10 novembre 2026, v2)

Écrit le 2026-11-09 vers 22:00 UTC (heure relevée par `date -u`). Recopié mot pour mot dans chaque consigne de cette série.

**v2** (R-2086) : v1 recopiée à l'identique (`851028fc…`), plus la règle 9 ; écrite après deux accès mécaniques par recherche récursive (R-2064, R-2086).


1. **Fichiers et branches qu'on n'ouvre jamais** (ni lecture, ni affichage, ni copie, ni passage à un script, ni `git show`, ni `git ls-tree`, ni `git fetch`) :
   - `diag/*/lecture-sondes-t06.json` de tout run, et nommément `diag/20261109-070232-t06-reel/lecture-sondes-t06.json` (DT-4 : rien avant le verdict scellé de P3-bis) ;
   - la lecture B de la course 7a et la branche `donnees/lecture-b-7a-quarantaine-v1` (R-2041, R-2048) ;
   - tout `diag/` et tout `runs/` de la course 7a (`20261109-070232-t06-reel`) et la branche `essai/t06-explo-v3`, sauf permission écrite dans la consigne ;
   - `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/` (le bras d'attaque n'est pas le mandat de la mère : N-056, R-2045, R-2047) ;
   - les items, clés et réponses de l'étiqueteur (branche `prep/etiqueteur-v2-lecture-interrompue-reprise-v1`).
2. **Secrets** : ne jamais lire, afficher ni copier une valeur de clé ; jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`, même avec la sortie jetée.
3. **Aucun appel** de modèle ni d'interface externe (Argon, Claude, autres), aucune location d'instance, aucun `vastai`, aucune dépense.
4. **Git** : aucun `checkout`, `switch`, `reset`, `stash`, `commit`, `push`, `fetch`, `merge`, `rebase`, ni modification de l'index ; les autres commits se lisent par `git show <commit>:<chemin>` seulement (ils sont déjà dans le clone local). Rien n'est écrit hors des chemins de sortie nommés dans la consigne.
5. **Essais** : ne pas lancer la suite complète (la session mère la fait tourner) ; des essais ciblés sont permis.
6. **Refus** : si un contrôle de permissions ou un classifieur refuse une action ou une réponse, s'arrêter sur ce point et le rapporter tel quel ; ni contournement, ni reformulation, ni transfert.
7. **Heures** : toute heure écrite est relevée par `date -u` et dite telle.
8. **Rapport final à la mère** : chemins écrits, empreintes sha256, verdict en une ligne, points ouverts ; **aucune valeur numérique tirée d'une sonde de 7a** (il ne doit d'ailleurs y en avoir aucune sous vos yeux).
9. **Recherches et parcours** : aucune recherche récursive (`grep -r`, `rg`, `find … -exec`, motif `**` ou `*/` développé par l'interpréteur) sur un dossier qui contient un chemin interdit sans l'exclure explicitement ; en pratique, chercher avec `git grep` et des exclusions de chemins (`git grep -n MOTIF -- . ':(exclude)docs/notes/bras-attaque' ':(exclude)scripts/extraire_mesures_epreuve_t06_v1.py' ':(exclude)diag' ':(exclude)runs'`) ou dans une liste de fichiers nommés ; `verifier-arbre` et tout outil qui hache un arbre entier ne se lancent que sur un arbre où `docs/notes/bras-attaque/` n'est pas extrait.

**Interdits ajoutés par la mère** : jamais `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, la branche `claude/compassionate-meitner-d4ryyk`, `donnees/mesure-unanime-v15-sortie-v1`, ni `scripts/extraire_mesures_epreuve_t06_v1.py` ; **aucun `ls` ni aucune liste de `docs/notes/bras-attaque/`**. Jamais toucher une instance ni un serveur.

**Écarts écrits** : règle 4 : aucune écriture git dans le dépôt ; pour rejouer les essais, crée une **extraction** de la branche dans ton bac à sable (`git worktree add --detach /tmp/claude-0/-home-user-controle-ia-travail/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/p3bis-contre-lecture/depot 07a4b48a` depuis `/home/user/controle-ia-travail`, après `git fetch origin refs/heads/prep/p3bis-ecart2-v1:refs/remotes/origin/prep/p3bis-ecart2-v1` si besoin) ; aucun commit, aucune poussée. Tu n'écris que ton rapport, sous `brouillons/P3-bis-temoin-positif-v1/` (fichier neuf), et dans ton bac à sable. Bancs hors réseau, appelants factices : permis.

## À contre-lire
- **Code** : branche `prep/p3bis-ecart2-v1`, commit `07a4b48a1dd919fb4e0c8c3581a2f890144bf5d9` (38 fichiers ajoutés au-dessus de `f2a241c9`), rapport du développeur `docs/procedures/P3-bis-temoin-positif-v1/rapport-developpeur-p3bis-ecart2-v1.md` (`2ba5201f…`), diff contre S, sources de D1, essais et journal.
- **Addendum 2, brouillon 1** : `brouillons/P3-bis-temoin-positif-v1/P3-bis-addendum-2-telechargement-controle-v1-brouillon1.md` (`7c5e5db267e5e3e621e125468e3d93ee2286704e097c2c4142a292306c4665cc`).
- Références : texte scellé `prereg/P3-bis-temoin-positif-v1.md` (`76ab66ce…`) ; addendum 1 `prereg/P3-bis-addendum-1-garde-credit-v1.md` (`4e188814…`) et sa contre-lecture `brouillons/P3-bis-temoin-positif-v1/P3-bis-ecart1-contre-lecture-v1.md` (`9b1013db…`, modèle de forme) ; chaîne S (branche `scellement/p3bis-v2`, `8f8df8b2`) ; branche de l'écart 1 (`f2a241c9`) ; registre R-2446, R-2450, R-2452, R-2453 ; note de la fille (`etat/p3bis-fille-v1`, `0f3ea945`).

## Questions
1. Le diff ne touche-t-il que ce qu'exigent D1 à D3 ? Les originaux restent-ils égaux à S, et la comparaison à S du lanceur d'écart 1 reste-t-elle juste ?
2. **D1** : la source tranche-t-elle l'unité du prix ? L'interprétation en Kio de `inet_*_billed` est-elle la plus prudente parmi les interprétations plausibles ? La garde arrête-t-elle toujours une vraie dépense excessive ? Le **majorant** : le code ajoute 2,00 USD une fois dès qu'un sens est illisible (relevé du rédacteur), et non par paire : est-ce acceptable et bien écrit ?
3. **D2** : l'attente bornée (+ 180 s à + 900 s, relevés toutes les 30 s, liste fermée de signes d'échec immédiats) affaiblit-elle la garde au-delà du nécessaire ? Échéance de 900 s ou de 1 200 s ? Illisibilités mises en attente : acceptables ?
4. **D3** : l'enchaîneur v5 est-il sûr (aucune destruction, empreintes vérifiées avant chaque appel, jeton jamais écrit, dépense antérieure en argument) ? La destruction après la surveillance d'écart, non jouée par le banc, est-elle compatible ?
5. **Addendum** : chaque passage touché du texte scellé est-il couvert, sans réécriture au-delà de l'écart ; les pièces citées par empreinte exactes ; la réserve au verdict écrite ; les préalables du lancement complets (destruction de 60370121, dépense antérieure sous GO-2026-11-10-02 relevée au registre des dépenses, empreinte de l'enchaîneur, extraction de la branche) ? Le rédacteur signale une mention de « GO-2026-11-02-29 » : à éclaircir.
6. Rejoue les essais (`essais_ecart2_p3bis_v1.sh`) et compare au journal versé ; ajoute au moins deux mutations à toi.

## Ce qu'il faut rendre
`brouillons/P3-bis-temoin-positif-v1/P3-bis-ecart2-contre-lecture-v1.md`, scellé (`PYTHONPATH=src python -m controle_ia.scellement sceller …`) : verdict en une ligne (« scellable », « scellable après corrections », « non scellable ») ; corrections **exigées** (numérotées) et **suggérées** ; réponses aux questions 1 à 6 ; essais rejoués et mutations.

## Rapport final à la mère
Chemin et empreinte ; verdict ; corrections exigées ; heure de fin (`date -u`) ; ton modèle.
