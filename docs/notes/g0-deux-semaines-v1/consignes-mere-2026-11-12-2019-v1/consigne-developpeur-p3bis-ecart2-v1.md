# Consigne : P3-bis, écart 2 — dépense de téléchargement et fenêtre du contrôle à cinq minutes (R-2450) — v1

Session mère `session_01XJ6Mgn4MZR4nxqK44C8Ea3`, écrite le 2026-11-12 à 20:29 UTC (heure relevée par `date -u`). Destinataire : un **développeur neuf** (Claude Opus 5.5), qui n'a écrit ni la chaîne de P3-bis, ni le lanceur de l'écart 1, ni sa contre-lecture. **Aucune dépense** : aucune location, aucun appel de modèle, aucune écriture vers Vast (lecture seule de la documentation et du code du client `vastai`, téléchargé dans ton bac à sable sans être exécuté contre le compte).

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

**Interdits ajoutés par la mère** : jamais `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, la branche `claude/compassionate-meitner-d4ryyk`, `donnees/mesure-unanime-v15-sortie-v1`, ni `scripts/extraire_mesures_epreuve_t06_v1.py`. Jamais toucher une instance Vast (60370121 comprise) ni un serveur Hetzner ; aucun appel à l'interface de Vast avec la clé `VAST_API_KEY`.

**Écarts écrits, et eux seuls** : règle 4 assouplie : arbre de travail git neuf sous `/tmp/claude-0/-home-user-controle-ia-travail/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/p3bis-ecart2/` (`git worktree add -b prep/p3bis-ecart2-v1 /tmp/claude-0/-home-user-controle-ia-travail/d9ee6091-e75a-5f52-8473-9583438f59bd/scratchpad/agents/p3bis-ecart2/depot f2a241c9`, depuis `/home/user/controle-ia-travail`, après `git fetch origin refs/heads/prep/p3bis-ecart1-credit-v1:refs/remotes/origin/prep/p3bis-ecart1-credit-v1` si besoin) ; commits sur la seule branche neuve `prep/p3bis-ecart2-v1`, **ajouts seulement** (aucun fichier existant modifié : R12), **aucune poussée** ; garde des secrets à 0 avant chaque commit (`git diff --cached | grep -cE '(sk-ant-[A-Za-z0-9]|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|hf_[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{12}|AIza[0-9A-Za-z_-]{20,})'`). Les bancs de la chaîne (essais hors réseau, appelants factices) sont permis.

## Contexte (à lire)
- Texte scellé de P3-bis `prereg/P3-bis-temoin-positif-v1.md` (`76ab66ce…`) : passages sur le contrôle à cinq minutes, la surveillance et la dépense ; addendum 1 `prereg/P3-bis-addendum-1-garde-credit-v1.md` (`4e188814…`) : **modèle de forme** pour l'écart 2.
- Chaîne scellée : branche `scellement/p3bis-v2` (S `8f8df8b2`), dossier `docs/procedures/P3-bis-temoin-positif-v1/` (`verifications_p3bis_v2.py` l. 418-440, `controle_cinq_minutes_p3bis_v2.sh`, `surveiller_p3bis_v2.sh`, `controles_avant_depense_p3bis_v2.sh` et ses comparaisons à S, bancs `essais_*`) ; branche de l'écart 1 `prep/p3bis-ecart1-credit-v1` (tête `f2a241c9` : lanceur d'écart v2 `2e294e5a…`, manière dont il se compare à S sans changer l'aval, rapports du développeur).
- Registre `registres/decisions.md` : R-2392, R-2393 (enchaîneur détaché de la fille, v1 `13b3a6b2…`, 38 lignes : **il n'est pas au dépôt**, il vivait dans le bac à sable de la fille), R-2399, R-2401 à R-2407 (écart 1), R-2410, R-2411, R-2415, R-2416 (enchaîneur v4 `19728737…` = v3 à une ligne près : contrôle à création + 290 s), R-2431, **R-2446, R-2450**.
- Note de la fille : branche `etat/p3bis-fille-v1` (tête `0f3ea945`), `etat-p3bis-fille.md`, entrée 15:06:43Z : valeurs relues (`inet_down_billed` 6 564 085,76 ; `inet_up_billed` 289 792 ; `inet_down_cost` 0,026 USD par Go), heures (AMORCE 15:01:20Z ; « début » 15:04:25Z ; contrôle à 15:05:31Z), lignes manquantes.

## Défauts à corriger
- **D1, unité du téléchargement** : établir, **par une source citée** (code du client `vastai` publié sur PyPI ou documentation de l'interface, chemin et ligne), l'unité de `inet_down_billed` et `inet_up_billed` et celle de `inet_*_cost` ; écrire le calcul juste ; si la source ne tranche pas, prendre l'interprétation **la plus prudente parmi celles qui restent physiquement plausibles** (jamais une dépense sous-estimée), et le dire. Garde intacte : une vraie dépense de téléchargement excessive doit toujours arrêter la course.
- **D2, fenêtre du contrôle à cinq minutes** : l'amorce met ≈ 3 min avant « début » ; le contrôle joué à + 290 s trouve trois lignes absentes sans aucun signe d'échec. Corriger par une attente bornée (relevés répétés jusqu'à une échéance écrite, KO seulement à l'échéance, arrêt immédiat sur toute ligne d'échec) ou une autre forme justifiée ; aucune garde affaiblie au-delà de ce qui est nécessaire, et écrit.
- **D3, enchaîneur** : écrire au dépôt un **enchaîneur v5** versionné (il n'existait que dans le bac à sable de la fille), reconstruit sur les descriptions du registre et l'aval de la chaîne, qui appelle le lanceur d'écart, puis le contrôle corrigé et la surveillance corrigée ; déclarer ce qui ne peut être reconstruit à l'identique.

## Travail
1. Noms neufs (par exemple `verifications_p3bis_v2_ecart2_v1.py`, `controle_cinq_minutes_p3bis_v2_ecart2_v1.sh`, `surveiller_p3bis_v2_ecart2_v1.sh`, `enchaineur_p3bis_v5.sh`) ; scripts d'origine laissés au dossier et comparés à S comme le fait le lanceur d'écart ; aucun changement de l'aval qui n'est pas exigé par D1 à D3 ; diff complet relu.
2. **Essais R5** pour chaque changement : cas sain et artefact (D1 : valeurs de la fille → dépense plausible, pas d'arrêt ; téléchargement réellement excessif → arrêt ; champs illisibles → majorant ; D2 : lignes arrivant à + 200 s, + 400 s, jamais ; ligne d'échec à + 100 s ; D3 : bout en bout sur appelants factices) ; bancs existants rejoués égaux pour tout ce qui ne change pas ; journal des essais versé.
3. Rapport du développeur (`docs/procedures/P3-bis-temoin-positif-v1/rapport-developpeur-p3bis-ecart2-v1.md`) : sources de D1, choix de D2, reconstruction de D3, essais, empreintes ; tous les fichiers neufs scellés (`PYTHONPATH=src python -m controle_ia.scellement sceller …`).
4. Ne rédige **pas** l'addendum 2 (un rédacteur neuf le fera) ; donne seulement la liste des phrases du texte scellé que l'écart touche (numéros de lignes).

## Rapport final à la mère
Commits de `prep/p3bis-ecart2-v1` ; empreintes ; source et unité de D1 ; forme de D2 ; enchaîneur v5 ; essais (nombre, conformes) ; lignes du texte touchées ; points ouverts ; heure de fin (`date -u`) ; ton modèle. Suite prévue par la mère : contre-lecture par un lecteur neuf (Claude Fable 5.2), addendum 2 par un rédacteur neuf, vérification courte, scellement, relance par une session fille neuve.
