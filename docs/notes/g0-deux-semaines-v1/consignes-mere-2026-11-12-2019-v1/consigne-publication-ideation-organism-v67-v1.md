# Consigne : publication de la course v67 et de son verdict sur `lciric/ideation-organism` — v1

Session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`, écrite le 2026-11-12 à 22:29 UTC (`date -u`). Destinataire : un **agent neuf** (Claude Opus 5.5). **Mot direct de Lazar** (R-2466) : « Recommandation : (1), confiance 0,7 : go » — publier maintenant la course v67 et son verdict scellé, avec les mêmes exclusions qu'au 12 novembre. Aucune dépense.

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

**Interdits ajoutés** : aucun `ls` ni liste de `docs/notes/bras-attaque/` ; jamais `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, la branche `claude/compassionate-meitner-d4ryyk`, `donnees/mesure-unanime-v15-sortie-v1`. **Jamais** pousser le dépôt de travail vers un dépôt public ; jamais toucher `lciric/controle-ia`.

**Écarts écrits, et eux seuls** : règle 4 levée pour le **seul dépôt public `lciric/ideation-organism`** : clone neuf dans ton bac `/tmp/claude-0/-home-user-controle-ia-travail/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/publication-v67/`, commits et **une poussée en avance rapide sur `main`** (jamais forcée), jeton `CONTROLE_IA_GITHUB_TOKEN_2` lu par son nom par un programme `GIT_ASKPASS` (jamais affiché ni écrit), comme le faisait la publication du 12 novembre. Dans le dépôt de travail : lecture seule (`git show`, branche `donnees/course-organisme-v67-poste-local-v1` récupérée par refspec explicite) ; tu écris seulement ton rapport `docs/notes/ideation-organisme-v1/publication-v67-2026-11-12-v1.md` (scellé) et ton bac.

## Modèle
La publication du 12 novembre : rapport `docs/notes/ideation-organisme-v1/publication-2026-11-12-v1.md` (`c87d4e6f…`) et R-2435 : même méthode, mêmes exclusions (journaux de fournisseurs, pièces de travail, tout fichier portant une adresse IP, noms de serveurs si le README les tait, rapports citant des chemins hors périmètre, les 50 mondes neufs, toute donnée personnelle), garde des secrets sur chaque objet neuf poussé.

## À publier (nouveau dossier, par exemple `resultats/course-v67/`, à la manière de `resultats/boucle-reelle-v66/`)
- verdict R13 `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md` (`d7902432…`), à l'octet ;
- rapport du poste `rapport-course-v67-poste-local-v1.md` (`8a98f2f6…`, branche `donnees/course-organisme-v67-poste-local-v1`, tête `659a1297`), **seulement s'il ne porte ni adresse IP ni chemin hors périmètre** ; sinon une copie expurgée déclarée (un remplacement par élément, rien d'autre) ;
- relevés et lectures gelées des trois tentatives (`c9c6212b…`, `5a7fc27c…`, `21bc75f4…` ; lecture `d0ef1ee7…`), à rapporter ensemble (R4) ;
- README et MANIFEST mis à jour : C1 avec sa **portée étroite** et ses **sept réserves**, sans rien ajouter au verdict.
Chaque fichier publié avec son empreinte au MANIFEST. Rejoue après la poussée les essais publiés concernés.

## Rapport final à la mère
Commit public, liste des fichiers publiés et exclus (avec raison), garde des secrets (objets vus, résultat), chemin et empreinte du rapport, heure de fin (`date -u`), ton modèle. Tout refus : arrêt, rapporté tel quel.
