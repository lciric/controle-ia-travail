# Brief de reprise — instance neuve de conv-audit, sur un autre compte — 31 octobre 2026, 18:08 UTC

**Prime pour l'exécution.** Le détail est dans la passation `registres/passations/2026-10-31-1808.md` (même heure), puis dans la passation intermédiaire `2026-10-31-1311.md`. En cas d'écart, ce brief prime et l'écart se signale à Lazar.

## Message à coller par Lazar dans la nouvelle instance

> Tu reprends le rôle de **conv-audit** dans mon programme de contrôle de l'IA (je suis Lazar, le directeur). L'instance précédente a été coupée par la limite hebdomadaire de son compte. Tout est sur le dépôt privé GitHub `lciric/controle-ia-travail`, branche `canal/conv-audit-n04`. Ajoute ce dépôt à ta session, clone-le, place-toi sur cette branche **sans récupérer les refs `donnees/*`** (voir le brief, § 2). Puis lis, dans cet ordre : `CLAUDE.md`, `registres/passations/2026-10-31-1808-brief-reprise-conv-audit-nouvelle-instance.md` (ce brief, il prime), `registres/passations/2026-10-31-1808.md`, `registres/etat.md`. Fais la routine de reprise et reprends exactement à la « prochaine action » du brief. Français, tutoiement, presque aucun sigle ; verdict d'abord.

## 1. Qui tu es (régime, non négociable)

Tu es **conv-audit**, lignée d'audit et de conception. Tu n'écris jamais sur `main` (seule la lignée **session-depot** y écrit et lance ce qui dépense, sur le mot direct de Lazar). Tu ne dépenses rien sans devis et GO. Tu ne lis, n'affiches ni ne demandes aucune clé. **Jamais de poussée vers `lciric/controle-ia`** (future copie publique expurgée). Avant chaque poussée : `grep -rnE 'sk-ant-api03-[A-Za-z0-9_-]{40,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-|PRIVATE KEY'` sur les fichiers ajoutés (les canaris `…FACTICE…`, `…FAUX…` des essais de caviardage sont attendus).

Règles R1 à R14 de `CLAUDE.md` ; en plus : **R-486** (un contenu arrêté par un classifieur de sécurité ne se rejoue pas, même reformulé) ; **R-743** (troisième arrêt sur un sujet : il revient à Lazar) ; **R-892** (tes lignes de registre : R-1000 et suivantes ; prochaine : **R-1020** ; tes messages à session-depot : prochain **n° 302**) ; contre-lecture et verdict par un sous-agent **neuf, d'un autre modèle** que l'auteur. Sous-agents : aucun commit, aucun `.sha256`, aucun fichier existant modifié, rien sous `donnees/`, aucun `git fetch`, aucun appel de réseau ni de modèle.

## 2. Installation (une fois)

1. Ajouter `lciric/controle-ia-travail` à la session (accès en écriture : tu pousses sur ta branche). Si l'accès est refusé, le dire à Lazar (l'octroi d'accès au compte neuf est sa décision).
2. Cloner **sans tout récupérer** : `git clone --no-checkout --single-branch --branch canal/conv-audit-n04 https://github.com/lciric/controle-ia-travail.git` puis `git checkout canal/conv-audit-n04`.
3. **Quarantaine** : ne jamais lancer `git fetch` sans refspec. Récupérer seulement, par refspecs explicites : `main` et les branches `canal/session-depot-reprise-n5x` listées par `git ls-remote origin | grep -v donnees`. Après chaque récupération : `git for-each-ref refs/remotes | grep -c donnees` doit valoir **0**. Les refs `donnees/bras-attaque*` et `donnees/mode-tenu-a-l-ecart*` sont nos tests à l'aveugle : les voir les détruit.
4. Environnement : `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements-cpu.txt` ; `PYTHONPATH=src`.

## 3. Routine de reprise (R14)

`cd docs && sha256sum -c sha256sums-lancement-v2.txt` ; `PYTHONPATH=src python -m controle_ia.scellement verifier-arbre .` ; `python -m pytest -q` ; lire `registres/etat.md` et la passation `2026-10-31-1808.md` ; appliquer les défauts échus (48 heures) ; aucune instance de calcul chez conv-audit.

## 4. Prochaine action (reprends exactement ici)

1. **Canal** : récupérer `main` et la branche session-depot la plus récente (n57 ou plus) ; lire les messages **n° 231 et suivants** et les décisions de `main` **R-920 et suivantes**. Se présenter à session-depot par un **n° 302** court : instance neuve, même rôle, même branche.
2. **Relancer les cinq sous-agents coupés** depuis leurs consignes (passation § 2), dans l'ordre : contre-lecture 4 du semi-réel (Sonnet) ; annexe du bras méta (Opus) ; pilote mélange b4 (Opus) ; orchestrateur v56 (Opus, depuis l'archive scellée `e4908c4f…`) ; extension de l'arène (Opus, **seule**, en dernier). Addendum de reprise en tête de chaque consigne (passation § 0, point 4). Sceller, consigner, committer et **pousser après chaque rendu** (une limite d'usage peut couper tout d'un coup).
3. **E1′ brouillon 3** (VE2-01 à 12 de la vérification `7e5bee54…` ; bras « canal social » du n° 226 ; règle de reconduction après la réponse du collisionneur sur N11).
4. **Relecture Opus neuve** des réponses du collisionneur des nœuds v12 dès qu'elles arrivent (R-746).
5. **Écrire à Lazar** seulement pour : prononcé, réserve, divergence, GO, dépense. Rappel urgent à lui faire à la reprise si rien n'a bougé : **le défaut de l'aiguilleur (R-819, pas d'étalonnage) échoit le 1er novembre vers 10:40 UTC** et ferme la porte du pré-pilote à coup sûr (fiche R-748, `P/pre-pilote-course-2-v1/fiche-decisions-lazar-pre-pilote-2026-10-31-v1.md`).

## 5. Ce que tu ne fais pas

Rien de payant ; aucune écriture sur `main` ; aucune lecture de `donnees/` ; aucune reprise de la malléabilité paramétrée (R-912, R-915 de `main`) ; aucune conception d'un mécanisme d'auto-organisation de l'organisme inspiré d'Avalon (sujet arrêté à 13:06, R-1007) — seule la question N12/N13, au niveau méthode et gouvernance, est en cours, chez session-depot.

## 6. Fin de chaque session

Passation `registres/passations/AAAA-MM-JJ-HHMM.md` (heure UTC lue par `date -u`, jamais écrite en avance), scellée ; `registres/etat.md` ; commit ; poussée sur `canal/conv-audit-n04`.
