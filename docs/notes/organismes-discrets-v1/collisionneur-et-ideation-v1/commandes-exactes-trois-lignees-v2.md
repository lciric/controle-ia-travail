# Commandes exactes — trois courses jumelles de l'organisme d'idéation sur les organismes discrets (lanceur v8) — v2

Écrites avant tout lancement par la session de relance `session_01XJ6MgpChR1JWSMBxSQcf3c`, 18 novembre 2026 (heures relevées
par `date -u` au moment de chaque geste, dans le journal des décisions). Ligne : **la ligne de GO de cette course** (34 USD, échéance
2026-11-22). Modèle suivi : `docs/notes/regard-ou-raisons-confondants-v1/organisme-v1/commandes-exactes-v1.md` (R-2698). Version 2 : après les contre-lectures du devis v3 et du lanceur v8 (relais Claude à 22 USD, `--prix-cache` du relais compatible OpenAI, noms de clé exigés par `!`, règle « aucun autre client des relais », rapprochement des journaux) ; la v1 reste archivée (R12).

**Premier temps : rien lancé, aucun appel payant, aucune dépense ; aucune valeur de clé lue ni affichée.** Aucun relais ni
course ne part avant que les contre-lectures R2 du devis v3 et du lanceur v8 aient rendu « autorisable » et que les
corrections éventuelles soient faites et scellées.

## 1. Préalables (à relever et inscrire au registre avant le feu)

| préalable | commande ou relevé attendu |
|---|---|
| `main` fusionnée dans la branche de travail, arbre propre | `git fetch origin +refs/heads/main:refs/remotes/origin/main && git merge --ff-only origin/main` (ou fusion ordinaire), `git status --porcelain` vide hors des pièces de cette course |
| lanceur v8 égal à son compagnon (M1) | `cd scripts && sha256sum -c lancer_course_ideation_organismes_discrets_v8.py.sha256` |
| pièces à leurs empreintes | essai `test_pieces_sain_depot_reel` de la suite v8, ou `sha256sum -c` des compagnons |
| `bwrap`, `socat`, interpréteurs | `/usr/bin/bwrap`, `/usr/bin/socat`, `/usr/local/bin/python3` 3.13 |
| clone de l'orchestrateur | `cd /home/user/lciric/ideation-organism && test "$(git rev-parse HEAD:orchestrator)" = ee84d6eca7a4c9b25f4e297ca29c6d9f24af5d70 && test -z "$(git status --porcelain --ignored)"` |
| relais (empreintes) | `orchestrator/pole/relais_reel.py` `1b90b020…` ; `relais_gemini_v2.py` `2b0043bc…` ; `relais_kimi_v4.py` `67f36951…` |
| clés, par leur nom seulement | `RR_ANTHROPIC_API_KEY_RIGAUD`, `GEMINI_API_KEY`, `OPENAI_API_KEY` présentes (non vides) ; jamais transmises qu'au relais concerné |
| ports 8787, 8788, 8790 libres | lecture de `/proc/net/tcp*` par le programme du modèle (R-2698 § 2.0), ports adaptés |
| aucune dépense sous la ligne, aucun run | `test ! -e runs/course-ideation-organismes-discrets-v8 && test ! -e /home/user/sorties-course-ideation-organismes-discrets-v8 && test "$(grep -c "organismes discrets : trois lignées" registres/depenses.md)" = 0` |

## 2. Relais (second temps), lancés par `scripts/lancer_relais_local_v1.py`, dossier hors dépôt `/home/user/hors-depot/relais-organismes-discrets-v8/`

Chaque relais part dans une session de processus neuve, environnement réduit à la liste de noms donnée (le nom préfixé de `!`
est exigé : absent, rien ne part), console dans le dossier hors dépôt ; le lanceur imprime le PID. Jamais `env`, `printenv`,
ni une valeur de clé sur une ligne de commande. **Aucun autre client n'appelle ces relais** pendant les courses.

### 2.1 Relais Claude (port 8787, plafond 22 USD pour les trois courses et leurs contrôles de relance, modèle permis Opus 5.5 seul)
```
cd /home/user/hors-depot/relais-organismes-discrets-v8 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/hors-depot/relais-organismes-discrets-v8/console-relais-claude.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_RIGAUD -- /usr/bin/python3 -I -B /home/user/lciric/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_RIGAUD --port 8787 --plafond-usd 22 --modeles-permis claude-opus-5-5 --journal /home/user/hors-depot/relais-organismes-discrets-v8/journal-relais-claude.jsonl
```
Attendu dans la console : « relais prêt sur http://127.0.0.1:8787 (… plafond 22.0 USD … modèles permis : claude-opus-5-5) ».

### 2.2 Relais Gemini v2 (port 8788, 24 appels au plus, modèles permis Argon et Carbon)
```
cd /home/user/hors-depot/relais-organismes-discrets-v8 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/hors-depot/relais-organismes-discrets-v8/console-relais-gemini.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --port 8788 --max-appels 24 --modele gemini-4-argon --modele gemini-4-carbon --journal /home/user/hors-depot/relais-organismes-discrets-v8/journal-relais-gemini.jsonl
```

### 2.3 Relais compatible OpenAI (port 8790, plafond 8 USD, modèle permis gpt-6-astra)
```
cd /home/user/hors-depot/relais-organismes-discrets-v8 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/hors-depot/relais-organismes-discrets-v8/console-relais-openai.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8790 --modeles-permis gpt-6-astra --plafond-usd 8 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 12 --journal /home/user/hors-depot/relais-organismes-discrets-v8/journal-relais-openai.jsonl
```
Vérifié avant (18 novembre, appel gratuit `--lister-modeles` par ce même chemin) : `gpt-6-astra` figure dans la liste des
modèles servie par l'amont ; le mandataire et la clé par nom fonctionnent.

### 2.4 Vérification des relais (réglages lus par PID dans la ligne de commande, jamais l'environnement)
```
tr '\0' ' ' < /proc/<PID>/cmdline; echo    # pour chacun des trois PID
/usr/bin/python3 -I -B -c 'import json,urllib.request; op=urllib.request.build_opener(urllib.request.ProxyHandler({})); [print(p, {k: d.get(k) for k in ks}) for p,ks in ((8787,("depense_usd","engage_usd","appels","refus","modeles_permis","plafond_usd")),(8788,("appels","refus","appels_restants","variable_cle_encore_presente","modeles_permis")),(8790,("appels","refus","depense_usd","plafond_usd","modeles_permis"))) for d in [json.loads(op.open(f"http://127.0.0.1:{p}/relais/etat",timeout=5).read())]]'
```
Attendu : 8787 dépense 0, modèles permis `['claude-opus-5-5']`, plafond 22 ; 8788 0 appel, 24 restants, variable de clé
absente de l'environnement du processus ; 8790 0 appel, plafond 8, modèle permis `gpt-6-astra`. Toute autre réponse : arrêt
des relais par PID (§ 6), rien ne part.

## 3. Les courses, une lignée à la fois, chacune au premier plan (lancement détaché par le lanceur)

Ordre : `carbon` (risque du modèle servi levé en premier, devis v4 § 7), puis `astra`, puis `argon` ; les jours sont ceux que la session mère fixe (budget du jour, devis v4 § 5). Pour chaque lignée L :
```
date -u
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/lancer_course_ideation_organismes_discrets_v8.py L
echo "code $?"
```
- Code 0 « lancée, détachée » : relever `pid_superviseur`, `sortie`, `manifeste_depart_sha256` ; **aussitôt** § 4.
- Code 2 : rien n'est parti ; motif au registre ; pas de nouvelle tentative sans lecture du motif.
- Code 5 : course lancée, manifeste de départ non écrit ; la même commande retrouve la course ; nœud.

## 4. Commit et poussée du dossier de run dès le lancement (C3), par chemin nommé
```
cd /home/user/controle-ia-travail && git add -- runs/course-ideation-organismes-discrets-v8/<identifiant> && git commit -m "Course de l'organisme d'idéation (organismes discrets, lignée L) partie sous la ligne de GO de cette course : dossier de run au lancement (C3)" -- runs/course-ideation-organismes-discrets-v8/<identifiant> && git push -u origin claude/eloquent-tesla-e52a0b
```
Rien d'autre n'entre dans ce commit. Le message de commit porte aussi les deux lignes d'attribution de la session.

## 5. Comptes rendus et clôture — la même commande, exactement
```
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/lancer_course_ideation_organismes_discrets_v8.py L ; echo "code $?"
```
Code 3 « en marche » : attendre (`kill -0 <PID du superviseur>` et `/relais/etat` suffisent entre deux). Une seule invocation
de clôture après la mort du superviseur : code 0 « clôture » (copies scellées dans `runs/…/copies/`, relevé de dépense,
manifeste de fin) ; code 4 si un orchestrateur orphelin vit (nœud : arrêt de l'orphelin par son PID seulement). Puis commit
et poussée du dossier de run (« close … relevé de dépense, manifeste de fin, copies scellées »), dépense inscrite dans
`registres/depenses.md` sous la ligne de GO de cette course (identifiant attribué par la session mère) à partir de `releve-depense.json` (`course_usd`, `lisible`). **Aucune fiche
n'est ouverte** par l'opérateur ; les copies restent fermées jusqu'à la lecture décidée par Lazar.

La lignée suivante ne part qu'après la clôture de la précédente et son commit.

## 6. Arrêt des relais après la troisième clôture (R10), par PID
```
kill -INT <PID relais Claude>; kill -INT <PID relais Gemini>; kill -INT <PID relais OpenAI>
```
Avant l'arrêt, une dernière lecture de `/relais/etat` donne la dépense tenue par les relais Claude et OpenAI et les appels
du relais Gemini ; **à chaque clôture**, le journal du relais concerné est rapproché du relevé du lanceur (`releve-depense.json`) et
l'écart éventuel est inscrit au registre des dépenses.

## 7. Ce qui arrête tout
Une revérification du § 1 qui échoue ; un relais qui ne démarre pas ou dont les réglages lus par PID diffèrent ; un état de
relais inattendu ; le lanceur rend 2 ; le dossier de run ne peut être commité et poussé (nœud) ; code 5 ou trace ; orphelin
(code 4) ; un refus d'une permission, d'un classifieur ou d'un crochet (arrêt et compte rendu, sans contournement) ; le
relais Claude approche 20 USD, le relais OpenAI 8 USD, ou le relais Gemini rend 429 ; Lazar ou la session mère disent « arrête ».
Bornes qui tiennent sans intervention : plafonds de session de l'orchestrateur (6 et 6,5 par course), gardes avant envoi
des commandes externes, plafonds des relais, borne du lanceur 34 USD, une relance au plus par lignée ; aucune machine chez
le loueur de cartes ni chez l'hébergeur allemand.
