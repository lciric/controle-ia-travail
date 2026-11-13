# Consigne : brouillon 1 du préenregistrement de la course de l'organisme à plusieurs générations — v1

Session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`, écrite le 2026-11-13 à 01:40 UTC (`date -u`). Destinataire : un **rédacteur neuf** (Claude Opus 5.5), qui n'a écrit ni la conception, ni le texte v2 de la course v67, ni son verdict. Aucune dépense, aucun appel de modèle.

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

**Interdits ajoutés** : aucun `ls` ni liste de `docs/notes/bras-attaque/` ; jamais `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, `claude/compassionate-meitner-d4ryyk`, `donnees/mesure-unanime-v15-sortie-v1`. **Écarts** : aucune écriture git ; tu écris seulement sous `docs/notes/organisme-multi-generations-v1/preenregistrement-v1/` (dossier neuf) et dans ton bac `/tmp/claude-0/-home-user/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/prereg-mg/`. Calculs légers seulement (un processus, `ulimit -v 6000000`, `OMP_NUM_THREADS=2` ; le conteneur a redémarré deux fois par manque de mémoire).

## Cadre (`registres/decisions.md`)
R-2441 (verdict v67 et ses **sept réserves**), **R-2442** (accord de principe, préenregistrement, contre-lecture, devis, ligne de GO neuve), **R-2443** (exigences : monde riche, regroupement des doublons, réponses brutes des proposeurs et témoins d'isolement par test versés, plusieurs graines ou mondes, mesure de la diversité), **R-2461** (monde écrit par un programme), **R-2467** (proposeurs : Claude, Kimi, Argon, Astra possibles), R-2469, R-2471, R-2474, R-2475, R-2477, **R-2478**.

## Sources
- Conception v3 `docs/notes/organisme-multi-generations-v1/conception-monde-riche-doublons-v3.md` (`386d48ba…`) et ses pièces ; vérification Fable `verification-conception-v3-fable-v2.md` (`8646ed4f…`) : **porte F-1 à F-5 dans le texte** ; contre-lecture v1 (`e7d5cda0…`) et vérification v2 (`0d64ed1d…`).
- Modèle de forme : texte v2 scellé de la course v67 `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-v2.md` (`80fe4f03…`) et le gabarit `prereg/gabarit-preregistrement-v1.md` : documents qui font foi, question, hypothèse, dessin, prédictions chiffrées et signes, métriques, seuils, plan d'analyse, critères de lecture gelés, audit de symétrie R4 écrit d'avance, liste d'arrêt, préalables, devis, portée, contre-lecture.
- Synthèse du collisionneur `docs/notes/collisionneur-diversite-idees-v1/synthese-v1.md` (`4f99077b…`, non contre-lue : citer avec cette réserve).

## Ce qu'il faut rendre
`docs/notes/organisme-multi-generations-v1/preenregistrement-v1/preenregistrement-multi-generations-v1-brouillon1.md`, scellé, qui :
1. reprend la conception v3 corrigée par F-1 à F-5, sans rien inventer (tout chiffre tiré d'une pièce citée par chemin et empreinte, sinon « estimé ») ;
2. répond une à une aux **sept réserves** du verdict v67 et à chaque exigence de R-2443 ;
3. fige les choix provisoires Q-1, Q-2, Q-4 à Q-8 (R-2469) et laisse **Q-3, Q-9, Q-10, Q-11, Q-12** comme décisions de Lazar **à trancher avant le scellement**, au format décision / enjeu / options / recommandation et confiance (recommandations de la conception) ;
4. liste les **préalables** du scellement et du lancement : code v68 (juge, générateur, vérificateur, regroupement, tranche de choix) écrit, contre-lu et gelé ; banc de calibration sur mondes à secret scellé ; engagement du secret machine poussé avant la phrase de Lazar ; règle de n fixée au banc ; isolement des proposeurs et témoins par test ;
5. porte le **devis** corrigé (F-4 : modèles 409,20 USD au pire, 419,20 avec la machine ; lignes proposées GO-β1 365 USD sur crédits de Claude et GO-β2 57 USD hors crédits, 62 sous Q-12 (b) ; variantes) et la **ligne de GO proposée** mot pour mot, **non inscrite** (nœud de Lazar) ;
6. écrit d'avance les critères de lecture gelés (issues possibles, y compris négatives et « non jugeable ») et la liste d'arrêt.
Puis un court rapport `…/preenregistrement-v1/rapport-redacteur-v1.md` (scellé) : ce qui reste ouvert.

## Rapport final à la mère
Chemins et empreintes ; dix lignes de résumé ; questions pour Lazar ; ligne de GO proposée ; préalables ; heure de fin (`date -u`) ; ton modèle. Tout refus : arrêt, rapporté tel quel.
