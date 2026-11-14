# Commandes exactes — course de l'organisme d'idéation sur la question « Regard ou raisons » — v1

Opérateur neuf, sous-agent de la session mère, 14 novembre 2026, de 10:01 à 10:05 UTC (heures relevées par `date -u`).
Ligne : **GO-2026-11-14-01** (25 USD ; registre R-2682, R-2691, R-2697). Conditions d'emploi C1 à C6 de la contre-lecture
`contre-lecture-lanceur-regard-ou-raisons-v1.md` (`6486e3a7…`) : elles font foi. Modèle suivi : R-2624 (première ligne de
ce numéro), course « conception propre ».

**Premier temps : rien lancé, aucun appel payant, aucune dépense, rien commité, rien poussé ; aucune valeur de clé lue ni
affichée.** Aucun relais ni course ne part avant que la mère ait inscrit ces commandes au registre et dit « lance ».
Non ouverts : `bilan-mere-v1.md`, `collisionneur-v1/`, les fiches, le dossier de run et les dossiers de lecture de la course
précédente (ni ses journaux de relais).

Dans ce texte, aucun identifiant de modèle n'est écrit en clair : la liste des modèles permis du relais Claude est tirée par
programme de la constante `PROPOSEURS` du lanceur (deux identifiants, ceux des proposeurs « modèle A » et « modèle B » ;
le juge de l'organisme, du modèle A, y est compris, vérifié à 10:03 UTC).

## 1. Préalables relevés

| Heure (UTC) | Préalable | Relevé |
|---|---|---|
| 10:01:42 | `main` à jour, refspec explicite : `git fetch origin +refs/heads/main:refs/remotes/origin/main` | `HEAD` = `origin/main` = `6ba2e6e5abc4e375a2aa918f8f8a89abc9a2f796` ; 0 en retard, 0 en avance ; aucun fichier suivi modifié ; deux dossiers non suivis d'autres agents (`docs/notes/organisme-conception-propre-v1/lecture-classement-v3-1/`, `docs/notes/regard-ou-raisons-confondants-v1/collisionneur-v1/`), non ouverts, non touchés. Dépôt distant : `https://github.com/lciric/controle-ia-travail`. |
| 10:01:50 | C1 : lanceur égal à son compagnon | `sha256sum -c` : OK ; `3b2dcb117cd4a3074099000374f8b0608ad301d9306da07d25cb360bcce1302f` ; fichier ordinaire (non lien) ; dernier commit qui le touche `8dd8aaef…` ; ni le lanceur, ni ses essais, ni le dossier `organisme-v1/` modifiés. |
| 10:01:50 | `bwrap`, `socat`, interpréteurs | `/usr/bin/bwrap` (bubblewrap 0.9.0) ; `/usr/bin/socat` (1.8.0.0) ; `/usr/local/bin/python3` et `/usr/bin/python3` : Python 3.13.18. |
| 10:01:51 | Clone de l'orchestrateur | `/home/user/lciric/ideation-organism` : `HEAD` `bdf6bc4b…`, arbre de `orchestrator/` = `ee84d6eca7a4c9b25f4e297ca29c6d9f24af5d70` ; `git status --porcelain --ignored` vide (propre, fichiers ignorés compris ; revérifié à 10:02:28 après les essais d'analyse d'arguments). |
| 10:01:51 | Relais | `orchestrator/pole/relais_reel.py` du clone : `1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153` (= R-2624) ; `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py` : `2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb` (= R-2624). À 10:02:28, `--help` des deux, sous `env -i` sans aucune clé : analyseurs conformes (`--variable-cle`, `--port`, `--plafond-usd`, `--modeles-permis`, `--journal` ; `--max-appels`, `--journal`), aucun appel réseau. |
| 10:01:59 | Clés, **par leur nom seulement** | `RR_ANTHROPIC_API_KEY_RIGAUD` présente (non vide) ; `GEMINI_API_KEY` présente (non vide). Aussi présentes dans l'environnement de la session : `ANTHROPIC_BASE_URL` et `CLAUDE_CODE_REMOTE` — **jamais transmises** : le lanceur de relais ne passe que les noms listés et refuse ces deux noms ; le lanceur de course ne transmet que sa liste de noms permis (`PATH LANG LC_ALL TZ TMPDIR`). |
| 10:01:59 | Ports | Lu dans `/proc/net/tcp` (`/proc/net/tcp6` absent dans ce conteneur) : **8787 et 8788 libres** ; 8789 en écoute (état `0A`), processus non cherché, non touché (relais d'un autre opérateur, peut-être). |
| 10:01:59 | C2 | `runs/course-ideation-regard-ou-raisons-v1` absent ; `/home/user/sorties-course-ideation-regard-ou-raisons-v1` absent ; `grep -c GO-2026-11-14-01 registres/depenses.md` = 0. Ligne GO-2026-11-14-01 présente au registre des GO (l. 320, calcul). |
| 10:02:36 | Lanceur de relais, copie neuve | `/home/user/hors-depot/relais-regard-ou-raisons-v1/lancer_relais_v1.py`, copie de `/home/user/hors-depot/relais-conception-propre-v1/lancer_relais_v1.py` : **contenu inchangé à l'octet** (`bf78153351eb9ec797c19f351027edec432d0ae2e0cef5f74e17903ea244f25e`), car le script ne porte aucun chemin de journal en dur (journal de console et journal du relais sont des arguments) ; seuls les chemins des commandes ci-dessous changent. Compagnon `lancer_relais_v1.py.sha256` écrit à côté. |

## 2. Commandes exactes (second temps, après le mot « lance » de la mère)

Toutes depuis une session dont l'environnement porte les deux clés ; **aucune valeur de clé n'apparaît sur une ligne de
commande** (les clés passent par leur nom, lues par le seul relais). Chaque étape commence par `date -u`. Jamais `&`,
`nohup` ni `env`/`printenv` ; jamais `ANTHROPIC_BASE_URL` dans une liste de noms.

### 2.0 Revérification immédiate (rien ne part si une ligne échoue)

```
date -u
cd /home/user/controle-ia-travail && git fetch origin +refs/heads/main:refs/remotes/origin/main && test "$(git rev-list --count HEAD..origin/main)" = 0
cd /home/user/controle-ia-travail/scripts && sha256sum -c lancer_course_ideation_regard_ou_raisons_v1.py.sha256 && grep -q '^3b2dcb117cd4a3074099000374f8b0608ad301d9306da07d25cb360bcce1302f ' lancer_course_ideation_regard_ou_raisons_v1.py.sha256
cd /home/user/controle-ia-travail && test ! -e runs/course-ideation-regard-ou-raisons-v1 && test ! -e /home/user/sorties-course-ideation-regard-ou-raisons-v1 && test "$(grep -c GO-2026-11-14-01 registres/depenses.md)" = 0
cd /home/user/lciric/ideation-organism && test "$(git rev-parse HEAD:orchestrator)" = ee84d6eca7a4c9b25f4e297ca29c6d9f24af5d70 && test -z "$(git status --porcelain --ignored)"
cd /home/user/hors-depot/relais-regard-ou-raisons-v1 && sha256sum -c lancer_relais_v1.py.sha256 && test ! -e console-relais-claude.txt && test ! -e console-relais-gemini.txt
```

Ports 8787 et 8788 libres (lecture de `/proc/net/tcp*`, rien d'autre ; 8789 ignoré) :

```
/usr/bin/python3 -I -B -c 'import os,sys; o=[int(l.split()[1].split(":")[1],16) for f in ("/proc/net/tcp","/proc/net/tcp6") if os.path.exists(f) for l in open(f).read().splitlines()[1:]]; b=[p for p in (8787,8788) if p in o]; print("ports occupés :", b); sys.exit(1 if b else 0)'
```

### 2.1 Relais Claude (port 8787, plafond 10 USD, modèles permis = `PROPOSEURS` du lanceur)

Une seule invocation shell (la variable ne vit que dans cette invocation) ; le lanceur de relais imprime le PID du relais :

```
date -u
cd /home/user/hors-depot/relais-regard-ou-raisons-v1 && MODELES_PERMIS="$(/usr/bin/python3 -I -B -c 'import ast,sys; t=ast.parse(open(sys.argv[1],encoding="utf-8").read()); v=[ast.literal_eval(n.value) for n in t.body if isinstance(n,ast.Assign) and [getattr(x,"id",None) for x in n.targets]==["PROPOSEURS"]]; assert len(v)==1 and len(v[0])==2; print(",".join(m for _,m in v[0]))' /home/user/controle-ia-travail/scripts/lancer_course_ideation_regard_ou_raisons_v1.py)" && test -n "$MODELES_PERMIS" && /usr/bin/python3 -I -B /home/user/hors-depot/relais-regard-ou-raisons-v1/lancer_relais_v1.py /home/user/hors-depot/relais-regard-ou-raisons-v1/console-relais-claude.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,RR_ANTHROPIC_API_KEY_RIGAUD -- /usr/bin/python3 -I -B /home/user/lciric/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_RIGAUD --port 8787 --plafond-usd 10 --modeles-permis "$MODELES_PERMIS" --journal /home/user/hors-depot/relais-regard-ou-raisons-v1/journal-relais-claude.jsonl
```

`pole/relais_reel.py` appelé par son chemin exécute sa propre amorce (`runpy.run_module("pole.relais_reel", …)`, l. 24-32
du fichier épinglé `1b90b020…`) : c'est le « runpy de `pole.relais_reel` du clone » de R-2624, sans texte de code sur la
ligne de commande. Dossier courant du relais : `/home/user/hors-depot/relais-regard-ou-raisons-v1/` (hors dépôt, fixé par le
lanceur de relais) ; nouvelle session de processus.

Attendu dans la console : une ligne « relais prêt sur http://127.0.0.1:8787 (…, plafond 10.0 USD, … ; modèles permis : »
suivie des deux identifiants de `PROPOSEURS`, et d'eux seuls ; `noms_absents` vide à l'impression du lanceur de relais.

### 2.2 Relais Gemini v2 (port 8788, huit appels au plus)

```
date -u
cd /home/user/hors-depot/relais-regard-ou-raisons-v1 && /usr/bin/python3 -I -B /home/user/hors-depot/relais-regard-ou-raisons-v1/lancer_relais_v1.py /home/user/hors-depot/relais-regard-ou-raisons-v1/console-relais-gemini.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --port 8788 --max-appels 8 --journal /home/user/hors-depot/relais-regard-ou-raisons-v1/journal-relais-gemini.jsonl
```

Attendu dans la console : « relais prêt sur http://127.0.0.1:8788 (…, max-appels 8, …) ».

### 2.3 Vérification des relais avant la course (C5 : réglages lus par PID dans la ligne de commande, jamais l'environnement)

```
date -u
cat /home/user/hors-depot/relais-regard-ou-raisons-v1/console-relais-claude.txt /home/user/hors-depot/relais-regard-ou-raisons-v1/console-relais-gemini.txt
tr '\0' ' ' < /proc/<PID relais Claude>/cmdline; echo; tr '\0' ' ' < /proc/<PID relais Gemini>/cmdline; echo
/usr/bin/python3 -I -B -c 'import json,urllib.request; op=urllib.request.build_opener(urllib.request.ProxyHandler({})); [print(p, {k: d.get(k) for k in ks}) for p,ks in ((8787,("depense_usd","engage_usd","appels","refus","refus_modele")),(8788,("appels","refus","appels_restants","variable_cle_encore_presente"))) for d in [json.loads(op.open(f"http://127.0.0.1:{p}/relais/etat",timeout=5).read())]]'
```

Attendu : 8787 → dépense 0, engagé 0, 0 appel ; 8788 → 0 appel, 8 restants, `variable_cle_encore_presente` faux. Toute
autre réponse, ou un relais absent : arrêt des relais par PID (§ 2.8), rien ne part, compte rendu à la mère.

### 2.4 La course (C1, C4, C5) — une invocation de lancement, au premier plan

```
date -u
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/lancer_course_ideation_regard_ou_raisons_v1.py 1
echo "code $?"
date -u
```

- Code 0 et « lancée, détachée » : relever `pid_superviseur`, `sortie`, `manifeste_depart_sha256` ; puis **aussitôt** § 2.5.
- C5, juste après : `grep SigIgn /proc/<PID du superviseur>/status` ; le bit de SIGINT (valeur 2) ne doit pas y être :
  `/usr/bin/python3 -I -B -c 'import sys; v=int(open(f"/proc/{sys.argv[1]}/status").read().split("SigIgn:")[1].split()[0],16); print("SIGINT ignoré" if v & 2 else "SIGINT non ignoré : bon"); sys.exit(1 if v & 2 else 0)' <PID du superviseur>`.
  S'il est ignoré : arrêt par `kill -TERM <PID du superviseur>` seulement après avis de la mère (nœud).
- Code 5 ou une trace (C4) : rien d'autre que la clôture dans **le même conteneur** (§ 2.6), sinon nœud ; aucune relance.
- Code 2 (refus) : rien n'est parti ; compte rendu à la mère avec le motif ; relais arrêtés par PID (§ 2.8).

### 2.5 Commit et poussée du dossier de run dès le lancement (C3), par chemin nommé

```
date -u
cd /home/user/controle-ia-travail && git add -- runs/course-ideation-regard-ou-raisons-v1/<identifiant> && git commit -m "Course de l'organisme « Regard ou raisons » partie sous GO-2026-11-14-01 : dossier de run au lancement (C3)" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01QPDgKgACWyCkCN8HjqwNXy" -- runs/course-ideation-regard-ou-raisons-v1/<identifiant> && git push origin refs/heads/main:refs/heads/main
git status --porcelain runs/course-ideation-regard-ou-raisons-v1; git fetch origin +refs/heads/main:refs/remotes/origin/main; git rev-list --count origin/main..HEAD
```

`<identifiant>` : le dossier unique créé par le lanceur (`AAAAMMJJ-HHMMSS-course-ideation-regard-ou-raisons-v1-g1`). Rien
d'autre n'entre dans ce commit (ni `src/`, ni `tests/`, ni registres). Les deux dernières commandes doivent rendre vide et
0. Poussée refusée parce que `origin/main` a avancé : `git fetch origin +refs/heads/main:refs/remotes/origin/main && git rebase
origin/main`, puis la même poussée ; jamais de poussée forcée ; jamais vers `lciric/controle-ia`.

### 2.6 Comptes rendus et clôture — la même commande, exactement

```
date -u
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/lancer_course_ideation_regard_ou_raisons_v1.py 1
echo "code $?"
```

Code 3 (« en marche ») : rien lancé, attendre ; espacer les comptes rendus (`kill -0 <PID du superviseur>` et la route
`/relais/etat` du § 2.3 suffisent entre deux). **Une seule invocation de clôture**, après la mort du superviseur
(`kill -0 <PID du superviseur>` échoue) : code 0 « clôture » ; code 4 si un orchestrateur orphelin vit (nœud : arrêt de
l'orphelin par son PID seulement sur mot de la mère). Jamais d'invocation après la clôture.

### 2.7 Commit et poussée à la clôture (C3), puis bilan (C6)

```
date -u
cd /home/user/controle-ia-travail && git add -- runs/course-ideation-regard-ou-raisons-v1/<identifiant> && git commit -m "Course de l'organisme « Regard ou raisons » close sous GO-2026-11-14-01 : relevé de dépense, manifeste de fin, copies scellées (C3)" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -m "Claude-Session: https://claude.ai/code/session_01QPDgKgACWyCkCN8HjqwNXy" -- runs/course-ideation-regard-ou-raisons-v1/<identifiant> && git push origin refs/heads/main:refs/heads/main
git status --porcelain runs/course-ideation-regard-ou-raisons-v1; git fetch origin +refs/heads/main:refs/remotes/origin/main; git rev-list --count origin/main..HEAD
cd /home/user/controle-ia-travail/runs/course-ideation-regard-ou-raisons-v1/<identifiant> && sha256sum -c releve-depense.json.sha256 manifeste-lanceur-fin.json.sha256 && cd copies && sha256sum -c sortie--fiches-validees.json.sha256
```

- Dépense : lue dans `releve-depense.json` (champ `course_usd`, et `lisible`) ; rapportée à la mère, qui la consigne dans
  `registres/depenses.md` sous GO-2026-11-14-01 (C3). **Aucune relance** tant que les deux contrôles de C3 ne rendent pas
  vide et 0, et jamais sans mot de la mère.
- Bilan (C6) : `copies/sortie--fiches-validees.json`, vérifié par `sha256sum -c`, que l'orchestrateur ait rendu 0 ou 4.
  **Aucune fiche n'est ouverte par l'opérateur.** Les copies des notes du juge, de la lecture de la course et du manifeste
  de fin de l'orchestrateur restent fermées au lecteur du croisement.

### 2.8 Arrêt des relais après la clôture (R10), par PID

```
date -u
kill -INT <PID relais Claude>; kill -INT <PID relais Gemini>
kill -0 <PID relais Claude> 2>/dev/null && echo "Claude vivant" || echo "Claude arrêté"; kill -0 <PID relais Gemini> 2>/dev/null && echo "Gemini vivant" || echo "Gemini arrêté"
```

Avant l'arrêt, une dernière lecture de `/relais/etat` (§ 2.3) donne la dépense tenue par le relais Claude et les appels
du relais Gemini, à rapprocher du relevé. Les relais ne sont jamais relancés entre une course et une relance éventuelle.

## 3. Arrêt en cours de route, et ce qui arrête tout

- **Arrêt à la main** : `kill -INT <PID du superviseur>` d'abord (relayé à l'orchestrateur par PID ; fin propre) ; attendre
  la fin (`kill -0`) ; puis la commande de clôture (§ 2.6) ; `kill -TERM <PID du superviseur>` seulement si elle ne finit
  pas. Jamais par motif de ligne de commande (R10), jamais `kill -9` sans mot de la mère.
- **Rien ne part, ou tout s'arrête**, si : une revérification du § 2.0 échoue ; un relais ne démarre pas, ou ses réglages
  lus par PID diffèrent (plafond 10, port 8787, modèles permis autres que ceux de `PROPOSEURS` ; port 8788, huit appels) ;
  `/relais/etat` ne rend pas l'état attendu ; le lanceur rend 2 ; le dossier de run ne peut pas être commité et poussé
  (C3 : aucune relance, nœud) ; le lancement rend 5 ou une trace (C4 : clôture dans le même conteneur, sinon nœud) ; un
  orchestrateur orphelin vit (code 4) ; une permission, un classifieur ou un crochet refuse (arrêt et compte rendu, sans
  contourner ni reformuler) ; la dépense du relais Claude approche 10 USD ou le relais Gemini rend 429 (la course s'arrête
  d'elle-même ; clôture, puis compte rendu) ; la mère dit « arrête ».
- Bornes qui tiennent sans intervention : plafonds de session de l'orchestrateur, totaux transmis (10 et 8), plafond du
  relais Claude (10 USD), huit appels du relais Gemini, garde avant envoi d'Argon, délai d'une heure par session ; borne du
  lanceur 17 USD (course 14,9 ; une relance seulement après une première tentative finie proprement, sans fiche, à relevé
  lisible d'au plus 2,1 USD) ; aucune instance Vast ni serveur Hetzner.

## 4. Réserves de l'opérateur

- Le relais Claude est appelé par le chemin de `pole/relais_reel.py` (amorce `runpy` interne) au lieu d'un `-c` avec texte
  de code (forme de R-2624) : même module, même effet ; le choix évite tout texte de code Python sur la ligne de commande du
  relais lue par PID.
- La liste des modèles permis est tirée du lanceur par programme (§ 2.1) pour qu'aucun identifiant de modèle ne figure dans
  cette pièce (réserve de R-2625) ; si la mère préfère les écrire en clair au registre, la valeur attendue est celle que
  le relais imprime au démarrage, à comparer à `PROPOSEURS` (l. 121 du lanceur `3b2dcb11…`).
- Le majeur A de la contre-lecture (perte du dossier de run avant commit : 31,9 USD au pire) n'est tenu que par le § 2.5 ;
  le lancement et le commit doivent se suivre sans autre geste entre eux.
