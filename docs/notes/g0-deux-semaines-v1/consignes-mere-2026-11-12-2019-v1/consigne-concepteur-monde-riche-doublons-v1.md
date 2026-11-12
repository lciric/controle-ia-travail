# Consigne : conception du monde riche écrit par Kimi et du regroupement des doublons au sein d'une génération — v1

Session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`, écrite le 2026-11-12 à 20:27 UTC (heure relevée par `date -u`). Destinataire : un **concepteur neuf** (Claude Opus 5.5), qui n'a écrit ni le texte v2 de la course de l'organisme, ni son code, ni son verdict. **Aucune dépense, aucun appel de modèle** : conception écrite, essais hors ligne permis.

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

**Interdits ajoutés par la mère** : jamais `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, la branche `claude/compassionate-meitner-d4ryyk`, `donnees/mesure-unanime-v15-sortie-v1`, ni `scripts/extraire_mesures_epreuve_t06_v1.py`. Ne pas lire `docs/notes/collisionneur-diversite-idees-v1/` (tour en cours ; sa synthèse te sera donnée plus tard). Jamais toucher une instance ni un serveur.

**Écarts écrits** : aucun pour les règles 2 et 3. Règle 4 : aucune écriture git. Tu n'écris que sous `docs/notes/organisme-multi-generations-v1/` (dossier neuf) et ton bac à sable `/tmp/claude-0/-home-user-controle-ia-travail/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/monde-riche/`.

## Mots de Lazar qui fixent le cadre (`registres/decisions.md`)
- **R-2442** : accord de principe pour une course de l'organisme à plusieurs générations ; préenregistrement neuf, contre-lecture, devis, ligne de GO neuve sur le montant du devis.
- **R-2443** : regroupement des doublons au sein d'une même génération (« défaut de conception ») ; monde plus riche : **plusieurs traits cachés, des interactions, des effets de tailles variées** ; le préenregistrement exige : monde riche, regroupement des doublons, réponses brutes des proposeurs et témoins d'isolement par test versés, plusieurs graines ou mondes (sensibilité aux effets faibles), mesure de la diversité des idées retenues.
- **R-2444** : « monde ecrit par kimi » — lois plantées écrites par **Kimi** (vérifiées par un programme) ; Kimi **exclu comme proposeur et comme juge** de cette course ; **Claude (Fable, Opus) redevient possible comme proposeur**, aux côtés d'Argon (et d'Astra si retenu), payé sur les crédits de Claude ; aucun juge de la famille de l'auteur du monde ; Kimi écrit le monde dans une instance qui n'a lu **aucun score ni aucune proposition** ; monde gardé **privé** ; devis et ligne de GO neuve pour la génération du monde.
- R-2440, **R-2441** : course v67 et son verdict (C1, portée étroite) avec **sept réserves**, dont : génération 2 sans promotion, 11 cartes retenues proches d'un même constat ; dossier des sessions des proposeurs vide, aucun témoin d'isolement par test ; usage d'Argon mal compté par la lecture.

## Documents à lire
- Texte v2 scellé `docs/notes/organisme-boucle-reelle-v1/preenregistrement-boucle-reelle-organisme-v1-v2.md` (`80fe4f03…`), surtout sections 3 (monde S-V1, archive K1, lois V1-V4 et F1-F4, classe couverte, jugement, génération 2), 4.2 (puissance par simulation), 7-8, 13-14 ; ses scripts de puissance (`puissance-boucle-reelle-v1*.py`).
- Verdict `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md` (`d7902432…`).
- Code de la course : paquets et code v65-v67 sous `docs/notes/organisme-boucle-reelle-v1/` (`code-v65/`, `code-v66/`, `ecart-1-sortie-proposeur-v1/`) et l'orchestrateur sous `docs/notes/ideation-organisme-v1/orchestrateur-v52b/` (`pole/monde_noyau.py` et voisins) : comment un monde, une loi, une carte et l'oracle sont représentés ; où un regroupement des doublons s'insère.
- Plan des crédits `docs/notes/credits-claude-v1/plan-chiffre-credits-claude-v1.md` (`8f9ee89e…`), postes P1 à P5 ; GO-2026-11-12-01 à -06 dans `registres/go.md`.

## Ce qu'il faut rendre : `docs/notes/organisme-multi-generations-v1/conception-monde-riche-doublons-v1.md` (scellé)
1. **Monde riche** : forme des lois (traits cachés en nombre, interactions, effets de tailles variées, du fort au proche du seuil), compatible avec la représentation actuelle des mondes et de l'oracle, ou les changements de code nécessaires (noms neufs) ; nombre de mondes ou de graines et leur justification par un **calcul de puissance hors ligne** (simulation sur des mondes synthétiques de la même famille, écrits par toi au bac à sable, jamais par Kimi) ; archive de départ ; lois fausses et classe couverte.
2. **Écriture par Kimi** : consigne de Kimi (brouillon), ce que l'instance reçoit et ne reçoit jamais (aucun score, aucune proposition, aucun verdict), forme de sortie ; **programme de vérification** (les lois s'exécutent, leurs effets mesurés tombent dans les bornes demandées, l'oracle les distingue, aucune fuite vers les proposeurs) ; garde du secret (où le monde est rangé, qui peut le lire, quand il est publié) ; repli si Kimi échoue ou si son compte est suspendu (constat du 11 novembre, R-2389).
3. **Regroupement des doublons au sein d'une génération** : définition opératoire d'un doublon (forme canonique, équivalence sur l'oracle ou sur des tirages, autre), qui le calcule (un programme, jamais un juge de la famille de l'auteur ni un score de moniteur : N-053), effet sur le juge statistique (comparaisons multiples comptées par groupe), sur la sélection et sur l'héritage ; essais hors ligne sur des cartes synthétiques ; cas sain et artefact (R5).
4. **Mesure de la diversité** des idées retenues : définition, calcul par programme, coût ; ce qu'elle ne doit pas piloter (N-058 : composition des proposeurs jugée sur l'oracle et le coût, jamais sur le verdict du juge).
5. **Proposeurs** : composition proposée (Claude Fable et Opus, Argon, Astra ; Kimi exclu), isolement et témoins par test, versement des réponses brutes ; laisser une place explicite à la synthèse du collisionneur sur la diversité (à venir).
6. **Devis** : (a) génération du monde par Kimi (appels, jetons, prix du relais Kimi : 2/10 USD par million, à vérifier dans `docs/notes/ideation-organisme-v1/relais-kimi-v1/`) et (b) ordre de grandeur de la course à plusieurs générations (par fournisseur, par génération, crédits de Claude séparés) ; **lignes de GO proposées** (texte, plafond, échéance), à présenter à Lazar.
7. **Questions ouvertes pour Lazar**, au format : décision ; enjeu ; 2 ou 3 options (avantage, inconvénient) ; recommandation et confiance.
Tout chiffre non tiré d'un fichier cité (chemin, empreinte) est marqué « estimé ». Scelle chaque fichier écrit (`PYTHONPATH=src python -m controle_ia.scellement sceller …`).

## Rapport final à la mère
Chemins et empreintes ; résumé en dix lignes ; devis et lignes de GO proposées ; questions ouvertes ; heure de fin (`date -u`) ; ton modèle.
