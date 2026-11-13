# Consigne : code du pilote de l'organisme sur la famille MR-2 (C-1 à C-18) — v1

Session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`, écrite le 2026-11-13 à 10:28 UTC (`date -u`), sur mot de Lazar (« go développeur pour le code du pilote »). Destinataire : un **développeur neuf** (Claude Opus 5.5), qui n'a écrit ni la conception v4, ni le préenregistrement du pilote, ni le code v67. **Aucune dépense, aucun appel de modèle**, aucun serveur.

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

**Interdits ajoutés** : aucun `ls` ni liste de `docs/notes/bras-attaque/` ; jamais `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, `claude/compassionate-meitner-d4ryyk`, `donnees/mesure-unanime-v15-sortie-v1` ; aucune clé lue. **Aucun monde de test ni de calibration tiré** (secret non engagé) : essais sur des graines de développement publiques seulement. **Écarts** : arbre de travail git neuf sous `/tmp/claude-0/-home-user/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/pilote-code/`, reconstruit selon la chaîne vérifiée (dépôt public `lciric/ideation-organism`, clone en lecture → paquets v65, v66, v67 du dépôt de travail, empreintes contre leurs compagnons ; voir R-2405, R-2429) ; branche neuve `prep/pilote-mr2-v1` dans **ce** dépôt de travail (ajouts seulement, commits sur cette branche, aucune poussée ; la mère pousse) ; jamais aucune poussée vers un dépôt public. Calculs : un processus à la fois, `ulimit -v 6000000`, `OMP_NUM_THREADS=2` (le conteneur a redémarré trois fois par manque de mémoire) ; commite chaque pièce finie et scellée.

## Sources
- Préenregistrement du pilote, brouillon 4 : `docs/notes/organisme-multi-generations-v1/pilote-v1/preenregistrement-pilote-conditionnelles-v1-brouillon4.md` (`04ada9fa…`), surtout la section du code manquant (C-1 à C-18), le plan d'analyse et les blocs gelés ; programme `pilote-v1/outils/mesure_pilote_v4.py` (`676d5f37…`).
- Conception v4 `docs/notes/organisme-multi-generations-v1/conception-monde-riche-doublons-v4.md` (`47e38ec0…`) et `outils-v4/monde_riche_v4.py` (`4b165847…`) ; contre-lecture v4 (`16da94d4…`).
- Code v67 et configuration v8 : `docs/notes/organisme-boucle-reelle-v1/ecart-1-sortie-proposeur-v1/` ; texte v2 scellé `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-v2.md` (`80fe4f03…`).
- Décisions de Lazar : `registres/decisions.md` R-2492, R-2501, R-2504, R-2506, R-2508 à R-2510.

## Travail
Écrire, sous **noms neufs** (code v68 du pilote), les points C-1 à C-18 du brouillon 4, dans l'ordre qui permet d'essayer chaque pièce : chargement d'un monde privé hors de l'arbre avec empreinte, manifeste sans loi vraie, compilateur et vérificateur MR-2 portés avec égalité contre `proba`, gabarit du proposeur et gardien à la dimension du monde (**rien servi sur les conditions, au plus 3 conditions emboîtées**, R-2504), commandes et relais pour Fable 5.2, Opus 5.5 (voie d'accès aux crédits de Claude **à décrire, pas à brancher**) et Astra, champs de jetons, réponses brutes et témoins d'isolement, lanceur à une génération sans juge ni test de mort (Q-P2 (a)), export des cartes vers `mesure_pilote_v4.py`, lecture, générateur MR-2 à graine du secret du pilote, lois de référence de C-16, égalité d'évaluateur de C-17, et C-18. **Essais R5** pour chaque pièce (cas sain, artefact) ; **mutations** ; **essai à blanc hors ligne** de bout en bout avec appelants factices sur 4 mondes de développement ; empreintes du code gelé dans un fichier (le bloc gelé que le préenregistrement attend) ; rapport du développeur. Si une pièce exige une décision de fond non tranchée par le texte, écris-la comme question, ne la tranche pas.

## Rapport final à la mère
Commits de `prep/pilote-mr2-v1`, empreintes, essais et mutations, essai à blanc, questions ouvertes, marqueurs que le code permet maintenant de remplir, heure de fin (`date -u`), modèle. Tout refus : arrêt, rapporté tel quel.
