# Consigne : contre-lecture du code v68 du pilote MR-2 (C-1 à C-18) — v1

Session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`, écrite le 2026-11-13 à 12:50 UTC (heure relevée par `date -u`). Destinataire : un **contre-lecteur neuf, d'un autre modèle que l'auteur** (auteur : Claude Opus 5.5 ; toi : Claude Fable 5.2), qui n'a écrit ni le code, ni le texte du pilote, ni la mesure (R2, N-052). Aucune dépense, aucun appel de modèle ni de réseau.

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

**Interdits ajoutés par la mère** : jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk` ; jamais `donnees/mesure-unanime-v15-sortie-v1` ; aucun `diag/` ni `runs/` de 7a ou de 7b ; jamais `scripts/extraire_mesures_epreuve_t06_v1.py`. Ne jamais toucher une instance Vast ni un serveur Hetzner. Mémoire du conteneur limitée (trois redémarrages hier) : `ulimit -v 6000000` et `OMP_NUM_THREADS=2` avant tout calcul, **un seul processus de calcul à la fois** ; ne rejoue **pas** le banc entier des 43 mutations (43 minutes) ni la génération des mondes de développement (15 minutes) : réemploie-les en lecture.

**Écarts écrits, et eux seuls** : règle 4 — tu peux **cloner en lecture** l'arbre de l'organisme du développeur vers ton bac à sable (`git clone` d'un chemin local, puis `git -C <ton clone> checkout` dans **ton** clone seulement) ; aucune écriture git dans le dépôt de travail ni dans les arbres du développeur. Règle 5 : la suite d'essais du pilote v68 (51 essais) est permise dans ton clone. Tu n'écris que : `docs/notes/organisme-multi-generations-v1/pilote-v1/contre-lecture-code-pilote-v68-v1.md` (et, s'il y en a, tes petits outils sous `docs/notes/organisme-multi-generations-v1/pilote-v1/contre-lecture-code-v68-outils/`) dans le dépôt de travail, et ton bac à sable `/tmp/claude-0/-home-user/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/pilote-contre-lecture/`.

## Pièces à lire (chemins exacts)
1. Le texte du pilote, brouillon 4 : `docs/notes/organisme-multi-generations-v1/pilote-v1/preenregistrement-pilote-conditionnelles-v1-brouillon4.md` (`04ada9fa…`) ; la mesure `docs/notes/organisme-multi-generations-v1/pilote-v1/outils/mesure_pilote_v4.py` (`676d5f37…`) et son essai scellé (même dossier).
2. La consigne du développeur : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-developpeur-code-pilote-v1.md` (`3b4f570c…`) : les exigences C-1 à C-18.
3. Les livrables du développeur, **en lecture**, dans son arbre du dépôt de travail (branche `prep/pilote-mr2-v1`, tête `dec76f42`) : `/tmp/claude-0/-home-user/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/pilote-code/depot/docs/notes/organisme-multi-generations-v1/pilote-v1/code-v68/` — rapport `rapport-developpeur-code-pilote-v68-v1.md` (`6635e43a…`), paquet `organisme-v68-pilote-mr2-v1.bundle` (`43d09adc…`), patch `organisme-v68-contre-ab53b7f.patch` (`70c68837…`), bloc gelé `EMPREINTES-code-pilote-v68.txt` (`27311ce3…`), journal des essais, banc des mutations, essais à blanc A et B.
4. Le code : arbre de l'organisme du développeur `/tmp/claude-0/-home-user/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/pilote-code/organisme`, branche `prep/organisme-v68-pilote-mr2-v1` (tête `276b6afd`, depuis `ab53b7f`) : tout fichier ajouté depuis `ab53b7f` (`git diff --stat ab53b7f`), dont `orchestrator/pole/pilote_mr2_v68.py`, `pole/proposeurs_pilote_v68.py`, `pole/audit_pilote_v68.py`, `demonstrations/pilote_mr2_v68.py`, la commande, le relais, la configuration v9, `orchestrator/mr2_v68/` et les essais. Les mondes de développement de l'essai à blanc (`/tmp/claude-0/-home-user/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/pilote-code/prive`, secret public nul) se lisent ; ils ne sortent pas de la machine et n'entrent dans aucun fichier que tu écris.

## Ce que tu vérifies, dans cet ordre
1. **Intégrité** : chaque pièce égale à son compagnon ; le paquet se vérifie (`git bundle verify`) et sa tête est `276b6afd` ; le patch égale `git diff ab53b7f 276b6afd` ; le bloc gelé égale les fichiers ; l'empreinte du gabarit annoncée (`2b1b33ec…`) se recalcule ; la copie portée de la mesure est égale octet pour octet à l'original.
2. **Conformité au texte** : C-1 à C-18 une par une, contre le brouillon 4 — ce que le code fait de plus, de moins ou d'autre que le texte ; tout réglage que le texte ne fixe pas et que le code fixe en silence.
3. **Gardes d'arrêt** (R5) : chacune a un cas sain et un artefact ; aucun repli silencieux ; le mode réel refuse de partir tant qu'un point « à confirmer » demeure ; codes de sortie.
4. **Secrets** : clés par leur nom seulement, jamais écrites ni journalisées ; environnement transmis construit par filtrage des noms ; aucun `ANTHROPIC_BASE_URL` ; aucun repli de modèle ; rien d'un fournisseur (identifiant d'organisation ou de clé) dans ce qui est rapatrié.
5. **Plafonds de dépense** : pire cas par appel, plafonds de session et de relais ; la garantie est-elle dure ; que se passe-t-il à la troncature, au refus, à l'usage absent.
6. **Isolement et secret des mondes** : aucun monde privé, aucune loi plantée, aucune graine dans ce qui sort de la machine ni dans le dépôt ; ce que les proposeurs reçoivent est exactement la vue du texte.
7. **Mesure et lecture** : la chaîne lanceur → réponses brutes scellées → gardien → cartes → mesure rend ce que le texte définit (dénominateurs, appels tronqués, échecs, témoin positif, issues P-0 à P-2 et réserves) ; graines par `numpy.random.SeedSequence`, manifeste (R9).
8. **Par toi-même** : la suite des 51 essais dans ton clone ; **cinq à huit mutations de ton choix**, hors de la liste du développeur, sur les gardes qui te semblent les plus fragiles (dis lesquelles survivent) ; un essai à blanc A avec les mondes de développement existants si la mémoire le permet (sinon dis-le).
9. **Avis motivé sur les questions Q-1 à Q-12** du rapport (section 7) : pour chacune, l'option que tu recommandes, pourquoi, et ce qu'elle change (texte, code, ou décision de Lazar). En particulier :
   - **Q-1** : la mère envisage, les lignes de dépense n'étant pas encore inscrites, de demander à Lazar un plafond un peu plus haut pour Argon et Astra afin de tenir la borne de sortie du texte (36 000 jetons) **sous la garantie dure** (pire cas sur les octets), et de garder 64 000 et 89 000 pour Fable et Opus : donne les chiffres exacts (par appel, par session, total par ligne π1 et π2) et dis si c'est cohérent avec le code ;
   - **Q-2** : pèse une **règle de tirage écrite d'avance** (un monde dont une loi de référence sort des bornes du gardien est remplacé par le suivant de la même suite scellée, les mondes écartés étant rapportés) contre les options (a) et (b) : effet sur la famille, sur la mesure, et sur la course qui devra porter la même règle ;
   - **Q-5 et Q-6** : dis ce que le dépôt permet de confirmer sans appel (plan des crédits `docs/notes/credits-claude-v1/plan-chiffre-credits-claude-v1.md` ; fonctions `appeler_openai` et `lire_reponse_openai` du script du collisionneur `docs/notes/collisionneur-experimentateur-v1/script-v1/collisionneur_v8_plafonds_bas_v1.py`, éprouvées les 12 et 13 novembre avec `gpt-6-astra`) et ce qui exige une sonde payante.

## Livrable
`docs/notes/organisme-multi-generations-v1/pilote-v1/contre-lecture-code-pilote-v68-v1.md`, scellé (`PYTHONPATH=src python3 -m controle_ia.scellement sceller …`) : **verdict** (« autorisable », « autorisable après corrections », « non autorisable ») ; constats numérotés **bloquants, majeurs, mineurs**, chacun avec fichier, ligne, preuve et correction proposée ; tableau C-1 à C-18 ; tableau Q-1 à Q-12 ; ce que tu n'as pas vérifié. Tu ne corriges rien toi-même.

## Rapport final à la mère (court)
Verdict ; nombre de bloquants, majeurs, mineurs ; les trois constats les plus graves ; tes avis sur Q-1 et Q-2 en une ligne chacun ; chemin et empreinte ; heure de fin (`date -u`) ; ton modèle.
