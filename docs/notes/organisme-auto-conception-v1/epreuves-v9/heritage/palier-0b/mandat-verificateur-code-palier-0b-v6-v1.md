VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE HORS DU DOSSIER DU CODE V6 ET DE TON DOSSIER (`ls` permis là seulement). TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. TOUTE REDIRECTION VERS UN CHEMIN COMPLET DE TON DOSSIER.

# Mandat du vérificateur — code du palier 0b, version 6 (EN ATTENTE DU MOT DE LAZAR) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20, sur l'accord de la mère (14:46Z : préparer sans rien sceller ni lancer ; Opus écrit, Sonnet vérifie). Pièce d'instrument (classe B). **Rien n'est lancé.**

## Qui

Un vérificateur neuf, modèle S, qui n'a écrit ni le texte du palier 0b, ni aucun code v1 à v6, ni leurs vérifications, ni l'audit des trous. Tu signes « vérificateur, modèle S ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier P0B = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- Le mandat du développeur `P0B/mandat-developpeur-code-palier-0b-v6-v1.md` (`46a5e1a4…`) et l'audit des trous `P0B/lecture-lancement-v1/audit-trous-code-v5-palier-0b-v1.md` (`8e965f80…`, « Ce que le code v6 doit porter », points 1 à 7).
- Le texte en vigueur, v13 scellé (`P0B/preenregistrement-heritage-palier-0b-etage-processeur-v13.md`, `d9591d5b…`) : B8, S7, étapes 5 à 9, annexe C.
- Le code v6 : `P0B/code-v6/` ; son rapport `P0B/code-v6/rapport-developpeur-code-palier-0b-v6.md` (`0f408c6f…`) ; la table `P0B/table-empreintes-code-v6.txt` (`639335b9…`) ; le code v5 `P0B/code-v5/` et sa vérification `P0B/verification-code-palier-0b-v5-v1.md` (`0e2c46bb…`).

## Ce que tu fais

1. **La table** : chaque fichier de `code-v6/` égal à la table et à son compagnon.
2. **Les différentiels v5 → v6** refaits (`diff -u`, redirigés, fichier par fichier) : rien ne change hors des sept points de l'audit.
3. **Le code** contre la lettre de la v13 et des sept points : tirage des cases « sources » sous « decisif » avec champ de mode, **aucune graine existante ne change** (éprouve-le) ; mode dans le nom des cases ; `lancer_famille` qui suit la clé de chaque case, un seul appel, un seul manifeste par étape ; reliquat et enrichissement ; `etape_8` avec relecture des gelés par empreinte ; `etape_9` ; docstring corrigé ; verrou (a) à (e) et garde 27 inchangés.
4. **Les essais rejoués** sur une copie du dossier du code dans ton dossier (`env -C COPIE /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider tests`, avec `PYTHONPATH=src`, `HERITAGE_DEPOT` et `HERITAGE_COPIE_ORGANISME` comme pour le v5 ; long, plus de vingt minutes : en tâche de fond) : 117 attendus ; **le banc** `outils-dev/mutations_v5.py` rejoué (147 attendus, chacun vu ; long : en tâche de fond, par parties si l'outil coupe à 30 minutes).
5. **Les 19 silences** et **la liste de l'erratum v14** (rapport § 7) : pour chacun, juste, à corriger (lieu et texte exact), ou à la mère avec ta recommandation. Le programme `outils-dev/lancer_etapes_8_et_9_v1.py` (« non lancé ») : lis-le ; ne le lance pas.
6. **Sorties v5 → v6** : 526 sur 531 égales à l'octet ; les 5 qui changent et les 6 neuves relèvent chacune d'un point de l'audit.
7. **Verdict** : « Conforme » ou « À corriger ».

Écris `verification-code-palier-0b-v6-v1.md` et son compagnon (`env -C DOSSIER sha256sum F`, redirigé vers `DOSSIER/F.sha256`) dans `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verification-code-palier-0b-v6/`.

## Interdits

Voir en tête. Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille, aucun lancement des étapes, aucune pièce d'autorisation. Aucun appel à un fournisseur de modèles, aucune dépense. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus, même sans motif (une tâche de fond s'arrête par l'outil de tâches). Aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
