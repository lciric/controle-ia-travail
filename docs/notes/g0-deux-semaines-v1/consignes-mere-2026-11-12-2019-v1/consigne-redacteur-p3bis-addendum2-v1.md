# Consigne : rédaction de l'addendum 2 de P3-bis (écart 2, R-2450) — brouillon 1 — v1

Session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`, écrite le 2026-11-12 à 21:13 UTC (heure relevée par `date -u`). Destinataire : un **rédacteur neuf** (Claude Opus 5.5), qui n'a écrit ni la chaîne de P3-bis, ni l'écart 1, ni le code de l'écart 2. **Aucune dépense, aucun appel de modèle, aucune instance.**

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

**Interdits ajoutés par la mère** : jamais `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, la branche `claude/compassionate-meitner-d4ryyk`, `donnees/mesure-unanime-v15-sortie-v1`, ni `scripts/extraire_mesures_epreuve_t06_v1.py` ; aucun `ls` ni aucune liste de `docs/notes/bras-attaque/`. Jamais toucher une instance ni un serveur ; aucun appel à l'interface de Vast.

**Écarts écrits** : règle 4 : aucune écriture git ; les branches se lisent par `git show <commit>:<chemin>` (récupère-les si besoin par refspec explicite : `git fetch origin refs/heads/X:refs/remotes/origin/X`, jamais sans refspec). Tu n'écris que sous `brouillons/P3-bis-temoin-positif-v1/` (fichiers neufs seulement) et ton bac à sable `/tmp/claude-0/-home-user-controle-ia-travail/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/p3bis-addendum2/`.

## À lire
- Mot de Lazar R-2450 et le nœud R-2446, R-2452 (`registres/decisions.md`).
- Texte scellé de P3-bis `prereg/P3-bis-temoin-positif-v1.md` (`76ab66ce…`), lignes que l'écart touche (liste du développeur) : 1948-1950, 1962-1966, 2149-2150, 2172-2183, 2264-2266, 2273-2282.
- **Addendum 1** scellé `prereg/P3-bis-addendum-1-garde-credit-v1.md` (`4e188814…`) : **modèle de forme à suivre** (en-tête, portée, règles, pièces citées par empreinte, réserve au verdict), et sa ligne 69.
- Code de l'écart 2 : branche `prep/p3bis-ecart2-v1` (commit `07a4b48a1dd919fb4e0c8c3581a2f890144bf5d9`, 38 fichiers ajoutés au-dessus de `f2a241c9`), dossier `docs/procedures/P3-bis-temoin-positif-v1/` : `rapport-developpeur-p3bis-ecart2-v1.md` (`2ba5201f…`), `verifications_p3bis_v2_ecart2_v1.py` (`ba6deb68…`), `surveiller_p3bis_v2_ecart2_v1.sh` (`555ee522…`), `controle_cinq_minutes_p3bis_v2_ecart2_v1.sh` (`6aa165e5…`), `enchaineur_p3bis_v5.sh` (`34131eaf…`), `essais_ecart2_p3bis_v1.sh` (`e9629573…`), journal `essais-ecart2-p3bis-v1.log` (`c6af5250…`), `diff-ecart2-contre-S-v1.txt` (`6f0e0ac7…`), `sources-d1-ecart2-v1.txt` (`340c7d5a…`). Vérifie chaque empreinte.

## Ce qu'il faut rendre
`brouillons/P3-bis-temoin-positif-v1/P3-bis-addendum-2-telechargement-controle-v1-brouillon1.md`, scellé (`PYTHONPATH=src python -m controle_ia.scellement sceller …`), qui :
1. dit **ce qui change** (D1 : unité du téléchargement et calcul, majorant par paire illisible ; D2 : attente bornée du contrôle à cinq minutes, échéance, signes d'échec immédiats, affaiblissements écrits ; D3 : enchaîneur v5 au dépôt, dépense antérieure passée en argument) et **ce qui ne change pas** (tout le reste de S et de l'écart 1) ;
2. remplace, phrase par phrase, chaque passage touché du texte scellé (ligne citée, ancien texte, nouveau texte) ; lit l'addendum 1 l. 69 sous l'écart ; dit comment se lisent les deux lignes d'information de `lancement.txt` qui nomment le contrôle et la surveillance d'origine ;
3. cite chaque pièce par chemin et empreinte, et fixe le lanceur à jouer, l'enchaîneur et la branche (`prep/p3bis-ecart2-v1`, `07a4b48a`) ;
4. écrit la **réserve au verdict de P3-bis** : « écart 2 (dépense de téléchargement, fenêtre du contrôle à cinq minutes), R-2450 », à côté de celle de l'écart 1 ;
5. rappelle les préalables du lancement : destruction de l'instance 60370121 par son identifiant (R10), relevé de la dépense antérieure sous GO-2026-11-10-02 (toutes tentatives) au registre des dépenses, empreinte de l'enchaîneur v5 vérifiée, jeu depuis une extraction de la branche ;
6. liste les **points laissés au contre-lecteur** (échéance de 900 s ou 1 200 s ; illisibilités mises en attente ; majorant par paire ; unité non documentée de `inet_*_billed`, interprétation prudente retenue).
N'invente aucun chiffre : tout chiffre vient d'un fichier cité (chemin, empreinte, ligne).

## Rapport final à la mère
Chemin et empreinte du brouillon ; liste des passages remplacés ; points ouverts ; heure de fin (`date -u`) ; ton modèle. Suite prévue : contre-lecture du code et de l'addendum par un lecteur neuf (Claude Fable 5.2), corrections, vérification courte, scellement.
