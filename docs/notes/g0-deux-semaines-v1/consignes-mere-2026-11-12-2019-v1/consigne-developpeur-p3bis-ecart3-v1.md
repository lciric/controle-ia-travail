# Consigne : P3-bis, écart 3 — relance à l'aveugle après la fin anormale par épuisement du crédit, garde du crédit rétablie (R-2492) — v1

Session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`, écrite le 2026-11-13 à 07:48 UTC (`date -u`). Destinataire : un **développeur-rédacteur neuf** (Claude Opus 5.5), qui n'a écrit ni la chaîne, ni les écarts 1 et 2. **Aucune dépense**, aucun appel à l'interface de Vast, aucune instance touchée.

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

**Interdits ajoutés** : aucun `ls` ni liste de `docs/notes/bras-attaque/` ; jamais `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, `claude/compassionate-meitner-d4ryyk`, `donnees/mesure-unanime-v15-sortie-v1`, `scripts/extraire_mesures_epreuve_t06_v1.py` ; **jamais la branche `calcul/p3bis-reel-v1` ni aucun résultat de P3-bis** ; aucune clé lue. **Écarts** : arbre de travail git neuf `git worktree add -b prep/p3bis-ecart3-v1 /tmp/claude-0/-home-user/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/p3bis-ecart3/depot 444645bb` (tête de `prep/p3bis-ecart2-v1`) ; commits d'ajouts seulement sur cette branche, aucune poussée ; garde des secrets à 0 avant chaque commit. Branches d'autrui seulement par refspec explicite. Calculs légers, un processus à la fois.

## Faits (`registres/decisions.md` R-2489 à R-2492)
Course 60432755 (relance-3 sous l'écart 2) arrêtée seule vers 04:25Z au **lot 19 sur 30 des épisodes** ; journal sans erreur ; branche `calcul/p3bis-reel-v1` restée égale à S (`8f8df8b2`) : **rien poussé, rien lu** ; cause probable : **crédit Vast épuisé** (crédit 0, solde −0,93 USD à 07:30Z ; 7,05 USD à la création, ≈ 2,46 USD/h avec une instance d'autrui) ; **la recharge automatique, prémisse de l'écart 1 (R-2399, addendum 1 `4e188814…`), n'a pas joué**. 60432755 détruite (07:48:11Z). Texte scellé `prereg/P3-bis-temoin-positif-v1.md` (`76ab66ce…`) : ligne 1 des critères (l. 1844) et devis (l. 2468) : relance permise seulement si aucun épisode n'a été joué ; liste d'arrêt l. 1900-1962. Addendum 2 `prereg/P3-bis-addendum-2-telechargement-controle-v1.md` (`c23b2eb0…`) : modèle de forme.

## Mot de Lazar (R-2492)
Option (b) : écart 3 permettant une relance à l'aveugle sur `calcul/p3bis-reel-v2` ; garde du crédit rétablie ; relance sous GO-2026-11-10-02, création au plus tard le 18 novembre ; recharge du compte par Lazar avant.

## Travail
1. **Code (noms neufs, R12)** : `enchaineur_p3bis_v6.sh` = enchaîneur v5 (`34131eaf…`) dont le seul changement est d'appeler le **lanceur d'origine scellé** `lancer_p3bis_v2.sh` (égal à S, garde du crédit d'origine : « ≥ 20 USD plus 10 heures du prix des instances nommées en marche ») au lieu du lanceur d'écart 1, avec son empreinte vérifiée avant l'appel ; contrôle et surveillance d'écart 2 inchangés. Essais R5 (cas sain sur appelants factices ; artefacts : crédit sous le minimum → aucune création ; lanceur d'origine modifié → refus ; tentative N = 2 sans la branche v1 sur le distant → refus) ; bancs existants rejoués égaux ; journal versé ; tout scellé.
2. **Addendum 3, brouillon 1** (`brouillons/P3-bis-temoin-positif-v1/P3-bis-addendum-3-relance-credit-v1-brouillon1.md`, scellé), forme de l'addendum 2 : faits datés et cités ; **règle de relance** : malgré des épisodes joués, une relance est permise sous ce texte quand (i) l'arrêt est d'une cause externe à la chaîne et aux résultats, établie par le registre (épuisement du crédit), (ii) rien n'a été poussé au-delà de S ni lu, (iii) aucune lecture ni ouverture n'a eu lieu, (iv) le code cité n'a pas changé ; branche `calcul/p3bis-reel-v2`, N = 2 ; **écart 1 retiré** (sa prémisse a échoué), garde du crédit d'origine rétablie ; enchaîneur v6 ; passages du texte et des addendums 1 et 2 lus sous l'écart (lignes citées) ; **réserves au verdict** : « écart 3 (relance après épisodes joués, arrêt par épuisement du crédit), R-2492 », et « recharge automatique non tenue (écart 1) » ; préalables (recharge par Lazar au minimum de la garde plus le coût attendu de la course, dépense antérieure relevée au registre, empreintes, extraction de la branche d'écart 3, refspec restreint comme R-2463) ; ce qui ne change pas.
3. Rapport `docs/procedures/P3-bis-temoin-positif-v1/rapport-developpeur-p3bis-ecart3-v1.md`.

## Rapport final à la mère
Commits, empreintes, essais, lignes du texte touchées, montant de recharge conseillé à Lazar (calcul cité), points ouverts, heure de fin (`date -u`), modèle. Tout refus : arrêt, rapporté tel quel.
