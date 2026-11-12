# Consigne : réparation du vérificateur du noyau de l'essai Lean D-1a (R-2439) — v1

Session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`, écrite le 2026-11-12 à 20:24 UTC (heure relevée par `date -u`). Destinataire : un **développeur neuf** (Claude Opus 5.5), qui n'a écrit ni le harnais ni sa contre-lecture. **Aucune dépense** : aucun serveur Hetzner, aucune instance, aucun appel de modèle.

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

**Interdits ajoutés par la mère** : jamais `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, la branche `claude/compassionate-meitner-d4ryyk`, `donnees/mesure-unanime-v15-sortie-v1`, ni `scripts/extraire_mesures_epreuve_t06_v1.py`. Jamais toucher une instance Vast ni un serveur Hetzner, ni lire le jeton `HCLOUD_TOKEN`.

**Écarts écrits, et eux seuls** : règle 4 assouplie : tu travailles dans un **arbre de travail git neuf** créé par toi sous ton bac à sable `/tmp/claude-0/-home-user-controle-ia-travail/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/lean-dev/` (`git worktree add -b prep/lean-outillage-d1a-v10 /tmp/claude-0/-home-user-controle-ia-travail/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/lean-dev/depot b0b8667a`, depuis le dépôt `/home/user/controle-ia-travail`), et tu y **commites** sur la seule branche neuve `prep/lean-outillage-d1a-v10` ; **aucune poussée** (la mère pousse après ton rapport) ; garde des secrets à 0 avant chaque commit (`git diff --cached | grep -cE '(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'`). Les autres commits se lisent par `git show <commit>:<chemin>`. Règle 3 : le téléchargement de la chaîne Lean (elan, la chaîne `leanprover/lean4:v4.35.0`, Mathlib au commit épinglé et son cache) dans ton bac à sable est permis : ce n'est pas une dépense. Tout hôte refusé par le réseau : **arrête-toi sur ce point et rapporte l'hôte exact** ; ne change aucun réglage d'environnement.

## Contexte (à lire)
- Mot de Lazar (`registres/decisions.md`, R-2439) : « Réparer d'abord, puis relancer » ; R-2438 (cause), R-2421, R-2424 à R-2427 (harnais v7/v8, procédure v9, voie (a)).
- Harnais : branche `prep/lean-outillage-d1a-v7` (tête `b0b8667a`, code retenu `32a40613`) ; `src/controle_ia/lean_essai/verificateur_noyau_v4.lean` (`axiomesDe`, l. 48-49, appelle `CollectAxioms.collect`, inconnu sous Lean 4.35.0) ; `scripts/lean_essai_d1a_v8/` (pilote v8, mutations v8, essai « bac lit Mathlib.olean ») ; `scripts/lean_essai_d1a_v1/artefacts_r5_v1/` ; procédure `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/procedure-poste-local-d1a-v9.md` (sur la branche).
- Rapport du poste, second essai : branche `donnees/lean-outillage-d1a-poste-local-v2` (tête `3b2a74a2`), `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/rapport-poste-local-d1a-v2.md` (`b2bace9b…`) et ses pièces : chaîne réellement épinglée sur la machine (Lean 4.35.0, Mathlib `56a00585…` : relis le commit complet dans les pièces), message d'erreur exact, propositions du poste.
- Consigne du poste v2 (`docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/consigne-poste-local-lean-d1a-v2.md`, `af1d8ae3…`) ; contre-lecture courte du harnais v8 (`…/contre-lecture-courte-harnais-d1a-v8.md`, `a0efdcf1…`).

## Travail (noms neufs partout, R12 : on n'écrase jamais un fichier existant)
1. **Vérificateur v5** `src/controle_ia/lean_essai/verificateur_noyau_v5.lean` : `axiomesDe` porté vers l'interface de Lean 4.35.0 (`Lean.collectAxioms` ou l'équivalent que tu **vérifies dans les sources de la chaîne épinglée**, chemin et ligne cités) ; rien d'autre ne change que ce qu'exige la compilation (diff relu et rapporté).
2. **Compilation hors machine** contre la chaîne épinglée exacte (Lean 4.35.0, Mathlib au commit épinglé) dans ton bac à sable ; puis le vérificateur v5 joué sur **tous** les artefacts R5 (`sain_v1.lean` doit passer ; chaque artefact doit être refusé par la bonne garde) ; journal des sorties. Ajoute un essai qui **compile le vérificateur contre la chaîne épinglée** à la suite des essais hors machine, pour que ce défaut ne puisse plus passer.
3. **Pilote v9** (`scripts/lean_essai_d1a_v9/piloter_poste_v9.sh`, copie du v8) : essai R5 neuf « **le vérificateur compile sur la machine** », joué **avant la coupure du réseau** ; cas sain (compile) et artefact (copie volontairement cassée du vérificateur : arrêt avant toute suite, code non nul) ; aucun repli silencieux.
4. **Procédure v10** (`…/procedure-poste-local-d1a-v10.md`, copie de la v9) : section 0 exige un **terminal WSL ouvert** pendant tout l'essai (incident R-2434) ; mentions du vérificateur v5, du pilote v9 et du nouvel essai R5 ; troisième essai sous **GO-2026-11-10-13** (0,56 USD dépensés sur 65 ; troisième machine sous cette ligne accordée par R-2439, à déclarer comme en R-2426).
5. **Mutations** `scripts/lean_essai_d1a_v9/mutations_harnais_v9.py` : celles de la v8 plus des mutations du vérificateur v5 et du nouvel essai ; toutes tuées ; empreintes du harnais dans un fichier neuf `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/empreintes-harnais-v7.txt` (ou le premier numéro libre) ; chaque fichier neuf scellé (`PYTHONPATH=src python -m controle_ia.scellement sceller …`).
6. **Essais** : ceux du harnais (ciblés) et les mutations ; ne lance pas la suite complète du dépôt.

## Rapport final à la mère
Commits de `prep/lean-outillage-d1a-v10` et empreintes des fichiers neufs ; API Lean retenue avec sa source (chemin, ligne) ; résultats des compilations et des artefacts R5 ; mutations tuées sur total ; écarts et points ouverts (hôtes refusés le cas échéant) ; heure de fin (`date -u`) ; ton modèle. Suite prévue par la mère : contre-lecture courte par un lecteur neuf (Claude Fable 5.2), puis consigne v3 du poste.
