# Consigne : contre-lecture de la conception « monde riche et doublons » v1 — v1

Session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`, écrite le 2026-11-12 à 22:33 UTC (`date -u`). Destinataire : un **lecteur neuf** (Claude Fable 5.2, autre modèle que le concepteur, Claude Opus 5.5). Aucune dépense, aucun appel de modèle.

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

**Interdits ajoutés** : aucun `ls` ni liste de `docs/notes/bras-attaque/` ; jamais `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, `claude/compassionate-meitner-d4ryyk`, `donnees/mesure-unanime-v15-sortie-v1`. **Écarts** : aucune écriture git ; tu écris seulement ton rapport `docs/notes/organisme-multi-generations-v1/contre-lecture-conception-monde-riche-v1.md` (scellé) et dans ton bac `/tmp/claude-0/-home-user-controle-ia-travail/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/cl-monde-riche/` ; rejeux des outils hors ligne permis (`/home/user/controle-ia-travail/.venv/bin/python`, numpy et scipy présents).

## À contre-lire
`docs/notes/organisme-multi-generations-v1/conception-monde-riche-doublons-v1.md` (`fc9cd3854f11625212b924fdcc4c4f4cbf61dff85656d34d01861e78e673900f`) et ses pièces (outils, sorties), contre le cadre : R-2441 (verdict v67 et ses sept réserves), R-2442, R-2443, R-2461, R-2467, R-2469 (`registres/decisions.md`) ; texte v2 scellé `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-v2.md` (`80fe4f03…`) ; synthèse du collisionneur `docs/notes/collisionneur-diversite-idees-v1/synthese-v1.md` (`4f99077b…`, écrite par l'opérateur, non contre-lue : dis aussi si la conception la cite fidèlement).

## Questions
1. Le monde riche répond-il au mot de Lazar (plusieurs traits cachés, interactions, effets de tailles variées) et la génération par programme reste-t-elle aveugle (aucune loi dans le code, secret tiré après scellement, retirage sans biais de sélection) ? Les deux régularités du générateur signalées sont-elles les seules ?
2. Le vérificateur C0-C8 et la détectabilité certifiée (≥ 80 % des graines) tiennent-ils ? Le juge simplifié calé sur la v67 suffit-il pour fixer n = 400, alors que le code gelé n'a pas été lu ?
3. Le regroupement des doublons avant le juge (équivalence prédictive, strates, liaison complète, e-valeur moyenne du groupe, e-BH sur groupes) garde-t-il la validité du juge (O2) ? La preuve écrite tient-elle ? Risques pour l'oracle et l'isolement ?
4. La mesure de diversité ne pilote-t-elle rien (N-058) ? Est-elle préenregistrable telle quelle ?
5. Puissance et nombre de mondes (2 × 3) : les simulations sont-elles justes, reproductibles (rejoue au moins deux sorties), et l'écart simulations / dessin (représentant, strates) borné comme le dit le concepteur ?
6. Devis et lignes de GO proposées : cohérents avec les pièces ? Pire cas plausible ?
7. Q-1 à Q-8 : manque-t-il une question qui devrait revenir à Lazar ?

## Rendre
Rapport scellé : verdict en une ligne (« utilisable pour le préenregistrement », « utilisable après corrections », « non utilisable ») ; corrections **exigées** et **suggérées**, numérotées ; réponses 1 à 7 ; rejeux. Rapport final : chemin, empreinte, verdict, corrections exigées, heure de fin (`date -u`), modèle. Sur tout refus : arrêt, rapporté tel quel.
