# Commandes exactes — course d'affinage des idées des mentors, version 5 (rien n'est lancé ici)

- Écrit le 2026-11-18T09:41Z (`date -u`) par la session du compte organisme (modèle I). **Version 5** (R12) : les commandes v1 à v4 ne valent plus ; seul le lanceur v5 se lance, depuis une **session d'exécution neuve ouverte par la mère** (garde de calcul chargée, variable `RR_ANTHROPIC_API_KEY_MINUIT` présente et non vide). Clé de tous les appels Claude : Minuit ; `RR_ANTHROPIC_API_KEY_RIGAUD` n'est pas employée. Règles de clé : R-3237. Procédure des relais : `docs/procedures/relais-persistants-v1.md` (R-3238).
- Chaque bloc se copie seul ; aucun ne suppose une variable posée par un autre bloc (chemins écrits en entier) ; aucun document en ligne.
- Le lanceur ne clone rien et ne loue aucune instance : `DEPOT_URL` est sans objet (s'il fallait cloner le dépôt de travail : `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`).
- Les modèles ne sont nommés que par la configuration (`course-v5/configuration-course-affinage-mentors-v5.json`, champ `especes`) et par les arguments épinglés du lanceur ; les commandes ci-dessous les y lisent ou les recopient.
- Chemin de l'orchestrateur écrit ci-dessous : `/home/user/ideation-organism/orchestrator` ; si la copie de la session est `/home/user/lciric/ideation-organism/orchestrator`, remplacer ce préfixe partout (jamais les deux copies à la fois).

## 0. Préalables (mère), avant toute commande

1. Montants absents du registre des dépenses (relevé d'ensemble § 3.4, environ 41,82 USD) inscrits.
2. **Contre-lecture** du préenregistrement v5 et du lanceur v5 par un agent neuf du **modèle K**, scellée, à ce chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v5/contre-lecture-preenregistrement-course-affinage-mentors-v5.md`. Elle cite `e379a6e9a90360495704ae79516bf16846b660714323a346e822c705ab98426f` (préenregistrement v5) et `84fae20a44672438a0eeee6a4431b952b53f399f29e2a79e79a582b467c02875` (lanceur v5), se dit du modèle K, ne dit pas qu'elle n'a pas relu, et la première ligne de sa section `## Verdict` est exactement `Scellable.` (ou `**Scellable.**`).
3. Relais Claude unique, plafonné à 150 USD (R-3256) : confirmé.
4. Réserves de cloisonnement : 20 entrées retirées tant qu'aucune n'est levée par écrit ; **CW15 reste servie**.
5. **Ligne de GO** : le lanceur exige que `registres/go.md` du dépôt soit celui de `origin/main` (se mettre à jour sur `main` au § 1) ; il passe à l'orchestrateur un registre dérivé (ligne de GO-2026-11-18-14 et révocations qui la visent) qui **cite le commit de `main`** (R-3249). Le registre de `main` porte toujours des identifiants en double (lignes « extension ») que la lecture de l'orchestrateur refuse : c'est pourquoi le registre dérivé est passé.
6. **Carbon** déclarée (R-3274). **Astra** déclarée seulement si la sonde du § 5 réussit ; sinon, ne pas la déclarer et écrire le motif et le mot de la mère dans la déclaration (`absences`). **Kimi** : comme en v4, seulement si son relais est lancé et si sa part + 11,3 ≤ 90 % du reste relu.
7. Note périmée : la pièce `course-v3/procedure-relais-persistants-course-affinage-v3.json` dit encore que chaque porte lance le lanceur de relais ; depuis la v4, c'est la porte épinglée `scripts/porte_plafond_relais_v1.py` qui ouvre chaque commande de porte. La pièce reste épinglée pour ses empreintes (procédure écrite, lanceur de relais).

## 1. Dépôt, mise à jour sur `main`, empreintes

```sh
cd /home/user/controle-ia-travail && git fetch -q origin +refs/heads/main:refs/remotes/origin/main && git fetch -q origin +refs/heads/lot/compte-organisme-v1:refs/remotes/origin/lot/compte-organisme-v1
cd /home/user/controle-ia-travail && git checkout -q origin/main -- registres/go.md
cd /home/user/controle-ia-travail && git checkout -q origin/lot/compte-organisme-v1 -- scripts/lancer_course_affinage_mentors_v5.py scripts/garde_credit_relais_v5.py scripts/porte_plafond_relais_v1.py scripts/sonde_astra_affinage_v1.py scripts/lancer_relais_local_v1.py scripts/construire_fils_course_affinage_mentors_v1.py tests/test_lancer_course_affinage_mentors_v5.py docs/procedures/relais-persistants-v1.md docs/notes/organisme-affinage-mentors-v1
cd /home/user/controle-ia-travail && echo "84fae20a44672438a0eeee6a4431b952b53f399f29e2a79e79a582b467c02875  scripts/lancer_course_affinage_mentors_v5.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "6cf8786943bb6c9e51dd6909714e83de783e70dffc80ea1fad46a0e1545d30cd  scripts/garde_credit_relais_v5.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "fab5fe2e924c47799d968663baddfecb85dd6f74e9f859d9047b185eb36382b1  scripts/porte_plafond_relais_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "cb0266a732778804b49c937b494265d19569f5f004d9dd5d25574a91a4006294  scripts/sonde_astra_affinage_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "d365affcb0303283a71ac7d5e67e24a5b6060e3b13c2a9e83ea592e48d4b3c82  scripts/lancer_relais_local_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "0ca9cf5daa190135f8f26175f2639e4c9c4b22b01c551ab30ff8f7bb0d085148  docs/procedures/relais-persistants-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "ff2b38e23d7d97dfda95084bbf7e7b9a64f0c83a943141a355d0e136f8d4c912  scripts/construire_fils_course_affinage_mentors_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "d063b5e75e266fb9788190fb93f794659b799c8198285e9134d5fd6218806813  tests/test_lancer_course_affinage_mentors_v5.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "e379a6e9a90360495704ae79516bf16846b660714323a346e822c705ab98426f  docs/notes/organisme-affinage-mentors-v1/course-v5/preenregistrement-course-affinage-mentors-v5.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "3dbf7d9148c2e7ff8785d50d9dff5c10bc746893b7950bea58efead77f146610  docs/notes/organisme-affinage-mentors-v1/course-v5/configuration-course-affinage-mentors-v5.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "03b7eaa6d3757de6a26d0b230d84c9cf06da92bfff3f1daebc815c29994d134b  docs/notes/organisme-affinage-mentors-v1/course-v5/confidentialite-textes-servis-course-affinage-v5.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "614a92bacb3b6e20b1acfa1fc06ed14aa4eb6a23f80ca03c058992e9daa7b18e  docs/notes/organisme-affinage-mentors-v1/course-v5/releve-credits-gabarit-course-affinage-v5.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "43893c84d28a26766ed812ffc8fb82e13f79e3828ddcc5edab082165378fbc1f  docs/notes/organisme-affinage-mentors-v1/course-v5/releve-prix-claude-gabarit-course-affinage-v5.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "20dd6680251dcf10dd942dd8cf96c612bce788db01f8312bbb20b9dd4df27c5d  docs/notes/organisme-affinage-mentors-v1/course-v5/declaration-relais-gabarit-course-affinage-v5.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "d97594dbc2263cd4200113d44dd4fd3fc8562bef617d3e182f6a382bf95ec792  docs/notes/organisme-affinage-mentors-v1/course-v3/procedure-relais-persistants-course-affinage-v3.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "c30928c88feffc16d3aa1119efe2a54ba2d70cf135b8068855190a21470a56bb  docs/notes/organisme-affinage-mentors-v1/course-v1/fils-servis-et-retraits-course-affinage-mentors-v1.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "d36ba0a01c1c190d55d0ed63b053c951b5a767a9310013321d797e3e203d8c4f  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-proposeur-course-affinage-mentors-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "903318d7659db07819cbe9a7f89cbdbd292f59e14c32bb8811d8f8cb35dd955b  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-aiguilleur-course-affinage-mentors-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "a32583b14845343a613514cdcba3c24831a274b48ecc95fe0d884f017d27d346  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-juge-course-affinage-mentors-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "1ac9791b6aea1c97f534e32980f1f837cca425806ce8235b1064d98ce261dcbf  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-passe-tableau-course-affinage-mentors-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "521470096f98861d0a4183b24b1ab313af9fb365ee398da4b82afbfbbbfb3f30  docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v5.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a  rapports/fille-ideation-1-v1/appel-argon-v5.sh" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46  docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py" | sha256sum -c -
cd /home/user/controle-ia-travail && test -n "${RR_ANTHROPIC_API_KEY_MINUIT:-}" && echo MINUIT-PRESENTE-NON-VIDE
```

Toute ligne autre que « OK » : arrêt, rien n'est lancé. (La dernière ligne teste le nom et la non-vacuité, jamais la valeur.)

## 2. Orchestrateur (dépôt public, lecture seule) et pièces extraites de `main` (hors dépôt, vérifiées)

```sh
test "$(git -C /home/user/ideation-organism rev-parse HEAD)" = a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb && test -z "$(git -C /home/user/ideation-organism status --porcelain --untracked-files=all --ignored=matching)" && echo ORCHESTRATEUR-OK
echo "1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153  /home/user/ideation-organism/orchestrator/pole/relais_reel.py" | sha256sum -c -
/usr/local/bin/python3 -I -B -c "import claude_agent_sdk" && command -v bwrap socat
mkdir -p /home/user/pieces-affinage-v5
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py > /home/user/pieces-affinage-v5/commande_gemini_lot_v1.py && echo "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75  /home/user/pieces-affinage-v5/commande_gemini_lot_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py > /home/user/pieces-affinage-v5/commande_astra_v1.py && echo "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71  /home/user/pieces-affinage-v5/commande_astra_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v4.py > /home/user/pieces-affinage-v5/relais_gemini_v4.py && echo "543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4  /home/user/pieces-affinage-v5/relais_gemini_v4.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py > /home/user/pieces-affinage-v5/relais_gemini_v2.py && echo "2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb  /home/user/pieces-affinage-v5/relais_gemini_v2.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py > /home/user/pieces-affinage-v5/relais_kimi_v4.py && echo "67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e  /home/user/pieces-affinage-v5/relais_kimi_v4.py" | sha256sum -c -
```

## 3. Essais hors ligne (aucun appel)

```sh
cd /home/user/controle-ia-travail && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src /usr/local/bin/python3 -m pytest -q -p no:cacheprovider tests/test_lancer_course_affinage_mentors_v5.py
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v5.py --a-blanc /tmp/essai-a-blanc-affinage-v5-$(date -u +%Y%m%d%H%M%S)
```

Attendu : 108 essais passés ; essai à blanc au code 0.

## 4. Relais de la course (procédure neutre, § 2 et § 3) — chacun lancé par le lanceur de relais, PID noté

```sh
mkdir -p /home/user/sorties-relais-affinage-v5
cd /home/user/sorties-relais-affinage-v5 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sorties-relais-affinage-v5/console-claude.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_MINUIT -- /usr/bin/python3 -I -B /home/user/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_MINUIT --port 8787 --plafond-usd 150 --modeles-permis "$(/usr/local/bin/python3 -I -c "import json;c=json.load(open('/home/user/controle-ia-travail/docs/notes/organisme-affinage-mentors-v1/course-v5/configuration-course-affinage-mentors-v5.json'));print(','.join(sorted(e['modele'] for e in c['especes'] if e['famille']=='claude')))")" --journal /home/user/sorties-relais-affinage-v5/journal-relais-claude.jsonl
cd /home/user/sorties-relais-affinage-v5 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sorties-relais-affinage-v5/console-argon.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/pieces-affinage-v5/relais_gemini_v2.py --port 8788 --max-appels 450 --modele gemini-4-argon --journal /home/user/sorties-relais-affinage-v5/journal-relais-argon.jsonl
cd /home/user/sorties-relais-affinage-v5 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sorties-relais-affinage-v5/console-carbon.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/pieces-affinage-v5/relais_gemini_v4.py --port 8792 --max-appels 40 --max-lots 16 --modele gemini-4-carbon --journal /home/user/sorties-relais-affinage-v5/journal-relais-carbon.jsonl
```

Kimi (facultatif) : comme la v4 (§ 4), avec `/home/user/pieces-affinage-v5/relais_kimi_v4.py`, port 8789, plafond 6, `--max-appels 16`. Le lanceur exige `--max-appels` ≥ 2 × (16 + 32 × nombre d'espèces) pour Argon (450 couvre six espèces), ≥ 32 et `--max-lots` ≥ 16 pour Carbon. Vérifier chaque relais par PID et `/relais/etat` (procédure § 3) : 0 appel, 0 dépense, modèles conformes, `variable_cle_encore_presente` faux pour les relais Gemini.

## 5. Sonde d'Astra (R-3273), par un relais jeté, avant la porte à blanc

```sh
cd /home/user/sorties-relais-affinage-v5 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sorties-relais-affinage-v5/console-astra-sonde.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/pieces-affinage-v5/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8793 --modeles-permis gpt-6-astra --plafond-usd 0.05 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 1 --journal /home/user/sorties-relais-affinage-v5/journal-relais-astra-sonde.jsonl
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/sonde_astra_affinage_v1.py /home/user/pieces-affinage-v5/commande_astra_v1.py http://127.0.0.1:8793 <PID_DU_RELAIS_JETE> docs/notes/organisme-affinage-mentors-v1/course-v5/sonde-astra-course-affinage-v5.json
```

Puis lire `/relais/etat` du relais jeté et l'arrêter par son PID (`kill -INT <PID>`, R10). **Signaler la dépense** (au plus 0,05 USD) à la mère. Code 0 de la sonde : lancer le relais de la course d'Astra, **neuf** :

```sh
cd /home/user/sorties-relais-affinage-v5 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sorties-relais-affinage-v5/console-astra.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/pieces-affinage-v5/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8790 --modeles-permis gpt-6-astra --plafond-usd 24 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 16 --journal /home/user/sorties-relais-affinage-v5/journal-relais-astra.jsonl
```

Code 1 ou 2 de la sonde : pas de relais d'Astra ; Astra absente (déclaration, `absences`), la tentative n'est pas brûlée.

## 6. Déclaration des relais (écrire, puis sceller)

Chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v5/declaration-relais-course-affinage-mentors-v5.json`. Noms de clé seulement ; chaque relais porte `pid_relais` (le PID imprimé par le lanceur de relais). Gabarit scellé : `course-v5/declaration-relais-gabarit-course-affinage-v5.json` (à recopier, remplir les PID, retirer `kimi` ou `astra` s'ils ne sont pas lancés, retirer la clé `gabarit`). Les commandes de Carbon et d'Astra y sont **exactes** (le lanceur refuse tout autre argument) ; les commandes de porte de Claude et de Kimi commencent par la porte épinglée et portent `--url` du relais, ses modèles et `--plafond-ligne 150`. Puis : `cd /home/user/controle-ia-travail && PYTHONPATH=src python3 -m controle_ia.scellement sceller docs/notes/organisme-affinage-mentors-v1/course-v5/declaration-relais-course-affinage-mentors-v5.json`.

## 7. Relevés du jour (écrire depuis les gabarits, puis sceller)

- Crédits : gabarit `course-v5/releve-credits-gabarit-course-affinage-v5.json` → `course-v5/releve-credits-avant-course-affinage-mentors-v5.json` (Minuit ; Kimi relu ; Argon, Carbon, Astra « non lisible » sous la dispense `{"par": "mère", "reference": "R-3237", "cles": [...]}`).
- Prix Claude du jour : gabarit `course-v5/releve-prix-claude-gabarit-course-affinage-v5.json` → `course-v5/releve-prix-claude-course-affinage-v5.json`.
- Sceller les deux fichiers.

## 8. Lancement (une seule fois)

```sh
cd /home/user/controle-ia-travail && GO_ID=GO-2026-11-18-14 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v5.py
```

Le lanceur contrôle chaque relais (PID, programme, port, modèles, état neuf), la sonde d'Astra si elle est déclarée, la confidentialité de chaque texte servi, puis joue la **porte à blanc** avant le manifeste de départ ; aucun dossier de sortie n'est créé avant ; un refus rend 2 et laisse la relance possible. Codes : 0 course finie ; 2 refus avant départ, ou arrêt ou nœud de l'orchestrateur ; 3 alerte de crédit avant le départ ; 4 cumul au-dessus de 150 USD ; 5 arrêt par la garde de crédit (refus pour crédit, ou deuxième soupçon du même relais ; alerte scellée pour la mère, qui prévient Lazar).

## 9. Après

1. Lire `/relais/etat` de chaque relais, puis l'arrêter par son PID (procédure § 6, R10) ; consigner dans `registres/arrets.md`.
2. Relever les soldes quand l'interface le permet ; comparer au reste estimé du manifeste de fin ; toute alerte va à la mère, puis à Lazar.
3. Inscrire la dépense réelle par relais (et la sonde d'Astra) au registre des dépenses, avec l'écart au devis v5.
4. Verser `runs/<id>-course-affinage-mentors-v5/` ; sorties de l'orchestrateur hors dépôt sous `/home/user/sorties-course-affinage-mentors-v5/<id>/`. Aucune lecture des cartes avant la mère.

## Essai à blanc v5 déjà fait

`course-v5/essai-a-blanc-v5/` : orchestrateur réel épinglé, moteur simulé, relais factices ; commandes de Carbon et d'Astra extraites de `main` hors dépôt et vérifiées à l'empreinte ; six espèces, 192 cartes, code 0 ; aucune expurgation nécessaire. Relais, portes, registre dérivé, prix du jour et sonde ne sont pas exigés en moteur simulé : ils sont essayés en moteur réel par les essais.

## Différentiel v4 → v5 (commandes)

1. Lanceur, essais, préenregistrement, configuration : v5 ; garde de crédit v5 (auto-conception) ; sonde d'Astra.
2. Mise à jour sur `main` du registre des GO (§ 1) ; registre dérivé qui cite le commit.
3. Pièces de `main` extraites hors dépôt et vérifiées (§ 2) ; relais Gemini v2 (Argon) et v4 (Carbon) lancés et contrôlés.
4. Sonde d'Astra par un relais jeté, puis relais de la course neuf (§ 5).
5. Plus de variables de shell partagées entre blocs ; chemins écrits en entier.
6. Note périmée de la pièce de procédure v3 signalée (§ 0, point 7).
