VERSION DE PYTHON : `python3 --version` ; AUCUN `-c`, AUCUN `-` APRÈS PYTHON3 SAUF `-B`

AUCUNE COMMANDE DE LISTE HORS DU DOSSIER DU CODE V5 (`ls` permis sur `code-v5/` et ses sous-dossiers seulement). TOUT AUTRE FICHIER S'OUVRE PAR SON CHEMIN COMPLET. UNE COMMANDE SIMPLE PAR APPEL : NI `&&`, NI `;`, NI BOUCLE. `git show` TOUJOURS REDIRIGÉ VERS UN FICHIER PAR `>`, SUR `origin/main`. AUCUNE RECHERCHE DE MOTIF LARGE.

# Mandat du vérificateur — code du palier 0b, version 5 (préenregistrement v11) — v1

Pièce de travail (classe C), donnée par la session du compte organisme le 2026-11-20. Pièce d'instrument (classe B) : vérification par un autre modèle que son développeur (modèle O), puis vérification des corrections par le même ; ensuite erratum du commit au texte, contre-lu, et scellement par la mère.

## Qui

Un vérificateur neuf, modèle S, qui n'a écrit ni le texte, ni le code v1 à v5, ni leurs vérifications. Tu signes « vérificateur, modèle S ».

## Ce qui fait foi (vérifie chaque empreinte contre son compagnon)

Dossier P0B = `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/`.
- Le mandat du développeur : `P0B/mandat-developpeur-code-palier-0b-v5-v1.md` (`6d099bfc…`) ; le texte v11 : `P0B/preenregistrement-heritage-palier-0b-etage-processeur-v11.md` (`9faf31a3…`), sa liste « Ce qui demande un code v5 », la section « Seuil », les gardes 25 et 27, B7 bis, B8, la remarque 4 ; le contrôle v10 → v11 : `P0B/controle-v11/controle-differentiel-palier-0b-v10-v11-v1.md` (`88c37d86…`, NE-3).
- Le code v5 : `P0B/code-v5/` ; son rapport `P0B/code-v5/rapport-developpeur-code-palier-0b-v5.md` (`a2966a3c…`) ; la table `P0B/table-empreintes-code-v5.txt` (`56bddae7…`) ; le code v4 `P0B/code-v4/` et sa vérification `P0B/verification-code-palier-0b-v4-v1.md` (`183b17d2…`).

## Ce que tu fais

1. **La table** : chaque fichier de `code-v5/` égal à la table et à son compagnon.
2. **Les différentiels v4 → v5** refaits (`diff -u`, redirigés, fichier par fichier) : rien ne change hors des points 1 à 6 de la liste et de NE-3.
3. **Le code**, aux lieux qui changent, contre la lettre du texte v11 : seuil d'arrêt = le plus grand de 0,55 et de M + 2 σ₀, une exactitude au plus 0,55 n'arrête ni ne signale ; zone médiane du contenu et des réunis sans signalement ni mention ; audits de lois à la lettre ; plis dérivés par le code (rôle « plis ») ; verrou (a) à (e), revérifié avant chaque lancement décisif ; manifeste ; `lancer_etape_4` et la garde 27 à trois sources ; NE-3.
4. **Les essais rejoués** sur une copie du dossier du code dans ton bloc-notes (`env -C COPIE /home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider tests`, avec `PYTHONPATH=src` ; c'est long : en tâche de fond, attends sa fin) : 107 attendus ; **le banc des défauts** `outils-dev/mutations_v4.py` rejoué (113 attendus, chacun vu) ; dis ce qui manque.
5. **Les 16 silences déclarés** (rapport § 2) et **la liste de l'erratum du commit** (rapport § 6) : pour chacun, juste, à corriger (lieu et texte exact), ou à la mère.
6. **Les sorties v4 → v5** : 484 sur 489 égales à l'octet ; les 5 qui changent relèvent chacune d'une règle changée.
7. **Verdict** : « Conforme » ou « À corriger ».

Écris `verification-code-palier-0b-v5-v1.md` et son compagnon dans ton bloc-notes `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/verification-code-palier-0b-v5/`.

## Interdits

Voir en tête. Aucun tirage décisif, aucun étalonnage, aucun audit à pleine taille. Aucun appel à un fournisseur de modèles, aucune dépense. Aucune écriture dans le dépôt, aucun commit. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`. Jamais de heredoc ni de code en ligne passé à un interpréteur. Jamais le nom d'une commande d'arrêt ou de recherche de processus par motif. Aucune publication d'artefact. Aucun identifiant de modèle. Au premier refus de permission, de classifieur ou de garde : arrête-toi et dis-le.
