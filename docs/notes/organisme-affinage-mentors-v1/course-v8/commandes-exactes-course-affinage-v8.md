# Commandes exactes — course d'affinage des idées des mentors, version 8 (rien n'est lancé ici)

- Écrit le 2026-11-18T21:55:58Z (`date -u +%FT%TZ`) par le modèle L', correctif v8 demandé par la mère après l'échec technique de la course d'auto-conception v4 (diagnostic `docs/notes/organisme-auto-conception-v1/course-v2/diagnostic-erreurs-carbon-astra-course-v4-v1.md`, `510312b105c62ad01a1d45ab9078dfc04333ce3bc2322b98695fa48c4daa8aec`, branche `lot/compte-organisme-v1`). **Version 8** (R12) : ce texte se suffit ; il ne renvoie à aucun texte de commandes antérieur (voir la dernière section). Seul le lanceur v8 se lance, depuis une **session d'exécution neuve ouverte par la mère** (garde de calcul chargée, variable `RR_ANTHROPIC_API_KEY_MINUIT` présente et non vide).
- Composition déclarée (mot du directeur, 18 novembre vers 10:50Z ; R-3279) : **deux espèces Claude, Argon, Astra, Carbon ; pas de Kimi** (le lanceur v8 refuse toute déclaration de Kimi). Clé de tous les appels Claude : `RR_ANTHROPIC_API_KEY_MINUIT` seule (GO-2026-11-18-14) ; `RR_ANTHROPIC_API_KEY_RIGAUD` n'est pas employée. Clé de Google `GEMINI_API_KEY` pour Argon et Carbon ; clé d'OpenAI injectée par le secret de réseau de l'environnement d'exécution, lue par le relais d'Astra sous le nom `OPENAI_API_KEY`. `compter_limite_de_debit_comme_soupcon` = faux (R-3279, option (b)). Plafond d'arrêt : 150 USD (GO-2026-11-18-14, inchangé). Devis : `devis-course-affinage-mentors-v8.md` (`91171ea56e0c3b9eb6486a5f8d0444f1017cdf4a00b5f4e5c5b3f540529aa97f`) — estimation 45,25 USD, haut 122,73, pire cas 150. Règles de clé : R-3237. Procédure des relais : `docs/procedures/relais-persistants-v1.md` (R-3238).
- **Ce qui change depuis la v7** : la commande de Carbon part avec `--provision-pensee-jetons 28672 --max-sortie-jetons 16384 --delai-s 1620 --delai-requete-s 60` (pensée observée jusqu'à 20 696 jetons ; 32 768 ne tient pas sous le plafond de session de 1,50 USD : chaque appel serait refusé, code 4) ; durée maximale de la commande 1 770 s, sous les 1 800 s de l'adaptateur de l'orchestrateur épinglé (non réglable) ; relais de Carbon lancé avec `--max-releves 2000` ; Astra sans reprise (rapport du développeur v8) ; lancement **détaché** (§ 9).
- Chaque bloc se copie seul ; aucun ne suppose une variable posée par un autre bloc (chemins écrits en entier) ; `«J»` = la date du jour (`date -u +%F`) ; `«PID_…»` = un PID imprimé par le lanceur de relais. Le lanceur ne clone rien et ne loue aucune instance (`DEPOT_URL` sans objet ; s'il fallait cloner : `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`).
- Chemin de l'orchestrateur écrit ci-dessous : `/home/user/ideation-organism/orchestrator` ; si la copie de la session est `/home/user/lciric/ideation-organism/orchestrator`, remplacer ce préfixe partout (jamais les deux copies à la fois).
- Empreintes : lanceur v8 `scripts/lancer_course_affinage_mentors_v8.py` **`76c45b8e6188944bc78a5175d183aa066df21c33f31f04712c316c7875fa4eda`** ; préenregistrement épinglé `course-v8/preenregistrement-course-affinage-mentors-v8.md` **`fb71f5006c102162eaa78cdbf3c0888627d413f08846239896e87d62c2350a20`**.

## 0. Préalables (mère), avant toute commande

1. Dépenses de la course d'auto-conception v4 (18 novembre, Minuit, clés de Google et d'OpenAI) et de toute sonde d'Astra inscrites au registre des dépenses (sonde : R-3273) ; montants absents du relevé d'ensemble (§ 3.4, environ 41,82 USD) inscrits.
2. **Contre-lecture** du préenregistrement v8 et du lanceur v8 par un agent neuf du **modèle K**, scellée, à ce chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v8/contre-lecture-preenregistrement-course-affinage-mentors-v8.md`. Elle cite en entier `fb71f5006c102162eaa78cdbf3c0888627d413f08846239896e87d62c2350a20` (préenregistrement v8) et `76c45b8e6188944bc78a5175d183aa066df21c33f31f04712c316c7875fa4eda` (lanceur v8), se dit du modèle K, ne dit pas qu'elle n'a pas relu, et la première ligne de sa section `## Verdict` est exactement `Scellable.` (ou `**Scellable.**`). Fichiers à lui donner : le préenregistrement v8, le lanceur v8, ses essais v8, le devis v8, ces commandes, le rapport du développeur v8, le diagnostic `510312b1…`, la commande de Carbon de `main` (`9484dce0…`) et `pole/adaptateurs.py`, `demonstrations/ideation_v8.py` de l'orchestrateur épinglé.
3. **Décisions de la mère sur les points ouverts du rapport du développeur v8** (provision de 28 672 au lieu de 32 768 ; délai borné à 1 620 s par l'orchestrateur ; Astra sans reprise) : le lanceur v8 porte les choix du développeur ; un autre choix est une version suivante.
4. Relais Claude unique, plafonné à 150 USD (R-3256) : confirmé. Réserves de cloisonnement : 20 entrées retirées tant qu'aucune n'est levée par écrit ; **CW15 reste servie**.
5. **Ligne de GO** : le lanceur exige que `registres/go.md` du dépôt soit celui de `origin/main` (§ 2) ; il passe à l'orchestrateur un registre dérivé (ligne de GO-2026-11-18-14 et révocations qui la visent) qui cite le commit de `main` (R-3249). La ligne court jusqu'au 30 novembre.
6. **Carbon** déclarée (R-3274), sur la même clé qu'Argon (`GEMINI_API_KEY`) : part au pire de cette clé 150 + 24 = 174 USD. **Astra** déclarée seulement si la sonde commune du jour a réussi (§ 5) ; sinon Astra retirée de la déclaration, motif dans `absences.astra`, mère prévenue (la tentative n'est pas brûlée). **Kimi non déclaré**. Le risque d'une espèce déclarée qui échoue à l'échelle (A3 : trois échecs consécutifs arrêtent le rôle ; A14 : 6 appels inexploitables sur 16 rendent l'étape « non mesurée (technique) ») est accepté par le mot du directeur ; pour Carbon il reste réel (pensée du fournisseur non tenue en lot ; rapport du développeur v8).
7. **Limite de débit** : `compter_limite_de_debit_comme_soupcon` = faux, déjà écrit dans le gabarit v8 ; la garde v6 ne compte pas comme soupçon une ligne qui porte « per minute », « par minute », « rate limit », « rate-limit », « rate_limit », « requests per » ou « too many requests » sans mot de crédit ni de facturation.

## 1. Les deux courses de l'organisme : affinage et auto-conception

- L'affinage (cette course) et l'auto-conception **ne tournent jamais en même temps**. Elles partagent les ports **8787 à 8793** (8787 relais Claude, 8788 relais d'Argon, 8790 relais d'Astra, 8792 relais de Carbon, 8793 relais jeté de la sonde ; 8789 et 8791 réservés), la clé `RR_ANTHROPIC_API_KEY_MINUIT` (200 USD déclarés ; part au pire de 150 USD **dans chaque course**), les clés de Google et d'OpenAI, et le rapport de la sonde d'Astra du jour.
- **Avant cette course** : la course d'auto-conception v4 du 18 novembre (et toute tentative suivante) doit avoir son manifeste de fin ; arrêter **chacun de ses relais par son PID** (`kill -INT «PID»`, R10), après avoir lu `/relais/etat` de chacun et `/proc/«PID»/cmdline` ; consigner chaque arrêt dans `registres/arrets.md` ; vérifier que les ports 8787 à 8793 sont libres (bloc ci-dessous) ; puis **relevé des crédits refait** (§ 8) **après** cette fin, avec la dépense réelle de l'auto-conception. Le lanceur v8 refuse le départ si une course d'auto-conception a un manifeste de départ sans manifeste de fin dans `runs/`, ou si l'heure du relevé n'est pas postérieure à son manifeste de fin. Un relevé écrit trop tôt ne se réécrit pas (R12) : **écrire le relevé en dernier**, juste avant le lancement.
- Les relais de cette course sont **neufs** ; le lanceur v8 refuse un relais qui a déjà servi (état lu non nul, relevés de lot compris pour Carbon) et les relais réglés pour l'auto-conception.
- **Pendant cette course** : aucune course d'auto-conception ne part (l'orchestrateur de l'affinage tient les ports).
- **Après cette course**, avant toute course d'auto-conception : relais de cette course arrêtés par leur PID et consignés (§ 10), relevé des crédits refait pour l'autre course.

```sh
/usr/local/bin/python3 -I -c "import socket,sys;o=[p for p in range(8787,8794) if socket.socket().connect_ex(('127.0.0.1',p))==0];print('PORTS OCCUPES',o) if o else print('PORTS-8787-8793-LIBRES');sys.exit(1 if o else 0)"
```

(« PORTS OCCUPES » : identifier le relais par `tr '\0' ' ' < /proc/«PID»/cmdline`, l'arrêter par son PID s'il appartient à une course finie, sinon s'arrêter.)

## 2. Dépôt, mise à jour sur `main`, empreintes

Les pièces v8 sont sur la branche `prep/affinage-v8-compte-organisme-v1` (puis `lot/compte-organisme-v1` une fois versée par la mère) ; remplacer `origin/prep/affinage-v8-compte-organisme-v1` ci-dessous par `origin/lot/compte-organisme-v1` une fois versée. Les empreintes tranchent.

```sh
cd /home/user/controle-ia-travail && git fetch -q origin +refs/heads/main:refs/remotes/origin/main && git fetch -q origin +refs/heads/prep/affinage-v8-compte-organisme-v1:refs/remotes/origin/prep/affinage-v8-compte-organisme-v1
cd /home/user/controle-ia-travail && git checkout -q origin/main -- registres/go.md
cd /home/user/controle-ia-travail && git checkout -q origin/prep/affinage-v8-compte-organisme-v1 -- scripts/lancer_course_affinage_mentors_v8.py scripts/lancer_course_affinage_mentors_v7.py scripts/garde_credit_relais_v6.py scripts/porte_plafond_relais_v1.py scripts/sonde_astra_affinage_v2.py scripts/sonde_astra_courses_v1.py scripts/lancer_relais_local_v1.py scripts/construire_fils_course_affinage_mentors_v1.py tests/test_lancer_course_affinage_mentors_v8.py tests/test_lancer_course_affinage_mentors_v7.py tests/test_lancer_course_affinage_mentors_v6.py tests/test_astra_carbon_declares_affinage_v6b.py tests/test_sonde_astra_courses_v1.py docs/procedures/relais-persistants-v1.md docs/notes/organisme-affinage-mentors-v1 docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-2026-11-18-v1.json docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-2026-11-18-v1.json.sha256 docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py
cd /home/user/controle-ia-travail && echo "76c45b8e6188944bc78a5175d183aa066df21c33f31f04712c316c7875fa4eda  scripts/lancer_course_affinage_mentors_v8.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "fb71f5006c102162eaa78cdbf3c0888627d413f08846239896e87d62c2350a20  docs/notes/organisme-affinage-mentors-v1/course-v8/preenregistrement-course-affinage-mentors-v8.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "91171ea56e0c3b9eb6486a5f8d0444f1017cdf4a00b5f4e5c5b3f540529aa97f  docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v8.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "0c0b43460c63b28291ea84b3bcba55ae587dc73bbc9a157891fe39e7cc11c84c  docs/notes/organisme-affinage-mentors-v1/course-v8/declaration-relais-gabarit-course-affinage-v8.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "ccc7380dfcb9fdadb9ee32449372ab8c3d3cdc25c69e6e4b5730c791ef9a977f  docs/notes/organisme-affinage-mentors-v1/course-v8/releve-credits-gabarit-course-affinage-v8.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "ce6ee804428ce7d4b6cdf868a6e595a5114b2ea4c5576289a0567c9e35e5088c  docs/notes/organisme-affinage-mentors-v1/course-v8/releve-prix-claude-gabarit-course-affinage-v8.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "1d9882f71b01491c3282d24b963d14e8ad4339c855ec969f85b420c463c60fff  scripts/garde_credit_relais_v6.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "fab5fe2e924c47799d968663baddfecb85dd6f74e9f859d9047b185eb36382b1  scripts/porte_plafond_relais_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "1799449269e15661b92f2a45eaab95a22e3a766a1fdf10ec9a4648bbe92aebf7  scripts/sonde_astra_affinage_v2.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "d374d1071f4ef70b3604d97dc62e2f14103c440a166342b330d7a576d8b4c777  scripts/sonde_astra_courses_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "d365affcb0303283a71ac7d5e67e24a5b6060e3b13c2a9e83ea592e48d4b3c82  scripts/lancer_relais_local_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "0ca9cf5daa190135f8f26175f2639e4c9c4b22b01c551ab30ff8f7bb0d085148  docs/procedures/relais-persistants-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "0ea89ed2f72ce2693e619eb10b6eecbd46725d4578b548a44c5a98b9bb1ded21  docs/notes/organisme-affinage-mentors-v1/course-v6/configuration-course-affinage-mentors-v6.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "d97594dbc2263cd4200113d44dd4fd3fc8562bef617d3e182f6a382bf95ec792  docs/notes/organisme-affinage-mentors-v1/course-v3/procedure-relais-persistants-course-affinage-v3.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "c30928c88feffc16d3aa1119efe2a54ba2d70cf135b8068855190a21470a56bb  docs/notes/organisme-affinage-mentors-v1/course-v1/fils-servis-et-retraits-course-affinage-mentors-v1.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "d36ba0a01c1c190d55d0ed63b053c951b5a767a9310013321d797e3e203d8c4f  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-proposeur-course-affinage-mentors-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "903318d7659db07819cbe9a7f89cbdbd292f59e14c32bb8811d8f8cb35dd955b  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-aiguilleur-course-affinage-mentors-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "a32583b14845343a613514cdcba3c24831a274b48ecc95fe0d884f017d27d346  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-juge-course-affinage-mentors-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "1ac9791b6aea1c97f534e32980f1f837cca425806ce8235b1064d98ce261dcbf  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-passe-tableau-course-affinage-mentors-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a  rapports/fille-ideation-1-v1/appel-argon-v5.sh" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46  docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py" | sha256sum -c -
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -c "import os,sys;sys.exit(0 if os.environ.get('RR_ANTHROPIC_API_KEY_MINUIT','').strip() else 1)" && echo MINUIT-PRESENTE-NON-VIDE
```

Toute ligne autre que « OK » : arrêt, rien n'est lancé. (La dernière ligne teste le nom et la non-vacuité — une valeur faite d'espaces compte comme vide —, jamais la valeur, qui n'est ni imprimée ni écrite.)

## 3. Orchestrateur (lecture seule), bac à sable, pièces extraites de `main` (hors dépôt, vérifiées)

```sh
test "$(git -C /home/user/ideation-organism rev-parse HEAD)" = a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb && test -z "$(git -C /home/user/ideation-organism status --porcelain --untracked-files=all --ignored=matching)" && echo ORCHESTRATEUR-OK
echo "1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153  /home/user/ideation-organism/orchestrator/pole/relais_reel.py" | sha256sum -c -
/usr/local/bin/python3 -I -B -c "import claude_agent_sdk" && echo SDK-OK
```

**Bac à sable : `bwrap` et `socat` installés et sondés** (le lanceur v8 refuse le moteur réel si le bac à sable de l'orchestrateur n'est pas actif avec un `/proc` neuf) :

```sh
command -v bwrap socat || (apt-get update -q && apt-get install -y -q bubblewrap socat)
command -v bwrap && command -v socat && bwrap --version && socat -V | head -n 2
bwrap --ro-bind / / --dev /dev --proc /proc --unshare-pid --die-with-parent /bin/true && echo BWRAP-OK
cd /home/user/ideation-organism/orchestrator && env PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -I -B -c "import json,sys;sys.path.insert(0,'.');from pole.adaptateurs import etat_bac_a_sable_detaille as e;print(json.dumps(e()))"
test -z "$(git -C /home/user/ideation-organism status --porcelain --untracked-files=all --ignored=matching)" && echo ORCHESTRATEUR-TOUJOURS-PROPRE
```

Attendu : deux chemins, deux versions, `BWRAP-OK`, une ligne JSON avec `"actif": true` et `"proc_neuf": true`, puis `ORCHESTRATEUR-TOUJOURS-PROPRE`. Sinon : arrêt, rien n'est lancé (le lanceur refuserait de même).

```sh
mkdir -p /home/user/pieces-affinage-v8
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py > /home/user/pieces-affinage-v8/commande_gemini_lot_v1.py && echo "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75  /home/user/pieces-affinage-v8/commande_gemini_lot_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py > /home/user/pieces-affinage-v8/commande_astra_v1.py && echo "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71  /home/user/pieces-affinage-v8/commande_astra_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v4.py > /home/user/pieces-affinage-v8/relais_gemini_v4.py && echo "543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4  /home/user/pieces-affinage-v8/relais_gemini_v4.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py > /home/user/pieces-affinage-v8/relais_gemini_v2.py && echo "2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb  /home/user/pieces-affinage-v8/relais_gemini_v2.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py > /home/user/pieces-affinage-v8/relais_kimi_v4.py && echo "67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e  /home/user/pieces-affinage-v8/relais_kimi_v4.py" | sha256sum -c -
```

(Si `/home/user/pieces-affinage-v8/` existe déjà d'un essai précédent, comparer les empreintes au lieu de réécrire ; tout écart : arrêt.)

## 4. Essais hors ligne (aucun appel), sauts visibles ; essai à blanc

```sh
cd /home/user/controle-ia-travail && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src /usr/local/bin/python3 -B -m pytest -q -rs -p no:cacheprovider tests/test_lancer_course_affinage_mentors_v8.py tests/test_lancer_course_affinage_mentors_v7.py tests/test_lancer_course_affinage_mentors_v6.py tests/test_astra_carbon_declares_affinage_v6b.py tests/test_sonde_astra_courses_v1.py
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v8.py --a-blanc /tmp/essai-a-blanc-affinage-v8-$(date -u +%Y%m%d%H%M%S)
```

Attendu : **554 passed, 0 skipped** (235 essais v8 + 175 v7 + 125 v6 + 5 v6b + 14 de la sonde commune) ; tout saut est nommé par `-rs` et arrête la session. Essai à blanc au code 0, deux lignes JSON (manifestes de départ et de fin, code 0). Les essais lisent `origin/main` (récupérée au § 2) et datent par `date -u` : à jouer du 18 au 30 novembre (période de la ligne de GO d'essai).

## 5. Sonde d'Astra (R-3273) : une seule sonde commune du jour

Le lanceur v8 n'accepte qu'**un** rapport de sonde commune du jour, cherché à ces chemins (« J » = jour du lancement) : `course-v8/sonde-astra-commune-J-v1.json`, `course-v7/sonde-astra-commune-J-v1.json`, `docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-J-v1.json`, `course-v6/sonde-astra-commune-J-v1.json`. **Le 18 novembre**, la sonde de 13:58Z (relais jeté PID 5016) est lue et vaut ce jour-là seulement : ne pas en refaire une (deux rapports du jour feraient refuser le départ). **Tout autre jour** : si une sonde commune du jour existe déjà à l'un de ces chemins (faite pour l'autre course), elle sert, n'en pas refaire ; sinon, **sonde neuve** :

```sh
cd /home/user/controle-ia-travail && ls docs/notes/organisme-affinage-mentors-v1/course-v8/sonde-astra-commune-$(date -u +%F)-v1.json docs/notes/organisme-affinage-mentors-v1/course-v7/sonde-astra-commune-$(date -u +%F)-v1.json docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-$(date -u +%F)-v1.json docs/notes/organisme-affinage-mentors-v1/course-v6/sonde-astra-commune-$(date -u +%F)-v1.json 2>/dev/null; echo FIN-RECHERCHE-SONDE-DU-JOUR
```

Aucun chemin imprimé : sonde neuve (au plus 0,05 USD, appel réel trivial, signalé à la mère, inscrit au registre des dépenses avec R-3273), avant le § 6 et après la fin de toute course d'auto-conception du jour :

```sh
mkdir -p /home/user/sonde-astra-«J»
cd /home/user/sonde-astra-«J» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sonde-astra-«J»/console-astra-sonde.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/pieces-affinage-v8/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8793 --modeles-permis gpt-6-astra --plafond-usd 0.05 --reserve-par-appel 0.01 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 1 --journal /home/user/sonde-astra-«J»/journal-relais-astra-sonde.jsonl
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/sonde_astra_courses_v1.py --commande /home/user/pieces-affinage-v8/commande_astra_v1.py --url-relais-jete http://127.0.0.1:8793 --pid-relais-jete «PID_DU_RELAIS_JETE» --sortie docs/notes/organisme-affinage-mentors-v1/course-v8/sonde-astra-commune-«J»-v1.json --sortie-v2 docs/notes/organisme-affinage-mentors-v1/course-v8/sonde-astra-course-affinage-v8-«J».json
```

Codes de la sonde commune : 0 réussie ; 1 non réussie, rapport écrit (`echec_de_configuration` vrai : rien n'est parti, ce n'est pas un échec d'Astra ; une sonde rejouée sur des chemins neufs demande une version suivante du lanceur, qui ne lit que ces noms) ; 2 refus avant tout appel, rien d'écrit. Puis `curl -s --noproxy '*' http://127.0.0.1:8793/relais/etat` (1 appel, dépense ≤ 0,05), arrêt **par son PID** du relais jeté de la sonde (`tr '\0' ' ' < /proc/«PID_DU_RELAIS_JETE»/cmdline` doit contenir `relais_kimi_v4.py` et `--port 8793`, puis `kill -INT «PID_DU_RELAIS_JETE»`, R10), consigner dans `registres/arrets.md`, signaler la dépense à la mère. Le relais jeté (port 8793) n'est jamais le relais de la course (port 8790). Le 18 novembre seulement : arrêter de même le relais jeté PID 5016 s'il vit encore (`test -d /proc/5016 && tr '\0' ' ' < /proc/5016/cmdline`), sinon écrire « relais jeté PID 5016 déjà arrêté (ou PID repris) » dans `registres/arrets.md`. Sceller les deux rapports neufs : `cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement verifier docs/notes/organisme-affinage-mentors-v1/course-v8/sonde-astra-commune-«J»-v1.json docs/notes/organisme-affinage-mentors-v1/course-v8/sonde-astra-course-affinage-v8-«J».json` (la sonde les écrit scellés ; la vérification doit dire OK).

## 6. Relais de la course — chacun lancé par le lanceur de relais, PID noté (ports libres : § 1)

```sh
mkdir -p /home/user/sorties-relais-affinage-v8
cd /home/user/sorties-relais-affinage-v8 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sorties-relais-affinage-v8/console-claude.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_MINUIT -- /usr/bin/python3 -I -B /home/user/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_MINUIT --port 8787 --plafond-usd 150 --modeles-permis "$(/usr/local/bin/python3 -I -c "import json;c=json.load(open('/home/user/controle-ia-travail/docs/notes/organisme-affinage-mentors-v1/course-v6/configuration-course-affinage-mentors-v6.json'));print(','.join(sorted(e['modele'] for e in c['especes'] if e['famille']=='claude')))")" --journal /home/user/sorties-relais-affinage-v8/journal-relais-claude.jsonl
cd /home/user/sorties-relais-affinage-v8 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sorties-relais-affinage-v8/console-argon.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/pieces-affinage-v8/relais_gemini_v2.py --port 8788 --max-appels 450 --modele gemini-4-argon --journal /home/user/sorties-relais-affinage-v8/journal-relais-argon.jsonl
cd /home/user/sorties-relais-affinage-v8 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sorties-relais-affinage-v8/console-carbon.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/pieces-affinage-v8/relais_gemini_v4.py --port 8792 --max-appels 40 --max-lots 20 --max-releves 2000 --modele gemini-4-carbon --journal /home/user/sorties-relais-affinage-v8/journal-relais-carbon.jsonl
```

Astra, **seulement si la sonde du jour a réussi** (§ 5), relais **neuf** (jamais celui de la sonde) :

```sh
cd /home/user/sorties-relais-affinage-v8 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sorties-relais-affinage-v8/console-astra.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/pieces-affinage-v8/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8790 --modeles-permis gpt-6-astra --plafond-usd 24 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 20 --journal /home/user/sorties-relais-affinage-v8/journal-relais-astra.jsonl
```

**Bornes contrôlées par le lanceur v8** (lues par PID et sur `/relais/etat`, qui doit rendre les mêmes valeurs ; une borne absente de la ligne de commande est refusée) : Claude `--plafond-usd 150` ; Argon `--max-appels` ≥ 2 × (16 + 32 × espèces) = 352 pour cinq espèces (450 ici) ; Carbon `--max-lots` ≥ 20 et `--max-appels` ≥ 40 (ici `--max-appels 40 --max-lots 20`), **v8** : état à « releves » nul et `releves_restants` ≥ 1 120 (20 lots × (⌈1 620 / 30⌉ + 2) ; ici 2 000) ; Astra `--plafond-usd 24` **exactement** (sa part au pire, 16 × 1,50) et `--max-appels` ≥ 20 (ici `--max-appels 20`), réserve par appel au plus 1,50 (défaut du relais : 0,40 ; ne jamais recopier `--reserve-par-appel 0.01 --max-appels 1 --plafond-usd 0.05` de la sonde : refusé), prix 10 / 50.

Vérifier chaque relais par PID et `/relais/etat` (procédure § 3) : 0 appel, 0 dépense, 0 engagé, 0 lot, 0 relevé, modèles conformes, `variable_cle_encore_presente` faux (Argon, Carbon, Astra) :

```sh
for p in 8787 8788 8790 8792; do echo "== $p"; curl -s --noproxy '*' http://127.0.0.1:$p/relais/etat; echo; done
```

## 7. Déclaration des relais (écrire, puis sceller)

Chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v8/declaration-relais-course-affinage-mentors-v8.json`. Recopier le gabarit v8 (`course-v8/declaration-relais-gabarit-course-affinage-v8.json`), remplir les **quatre PID** (un relais Claude pour les deux espèces Claude, plus Argon, Carbon, Astra) et la liste des modèles Claude de la configuration v6 (même commande qu'au § 6), retirer la clé `gabarit` ; Astra retirée seulement si la sonde du § 5 n'a pas réussi (motif dans `absences.astra`). Les commandes d'Astra et de Carbon y sont **exactes** : celle de Carbon porte `--provision-pensee-jetons 28672 --max-sortie-jetons 16384 --sortie-min-jetons 4096 --intervalle-s 30 --delai-s 1620 --delai-requete-s 60` (le lanceur v8 refuse une commande de Carbon où l'une de ces options manque, est doublée ou diffère) ; elles appellent `/home/user/pieces-affinage-v8/`. Puis : `cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-affinage-mentors-v1/course-v8/declaration-relais-course-affinage-mentors-v8.json`.

## 8. Relevés du jour — en dernier, juste avant le lancement (écrire depuis les gabarits v8, puis sceller)

- Crédits : gabarit `course-v8/releve-credits-gabarit-course-affinage-v8.json` → `course-v8/releve-credits-avant-course-affinage-mentors-v8.json` ; `releve_utc` = sortie de `date -u +%FT%TZ` au moment du relevé (le lanceur v8 exige cette forme et une heure postérieure à la fin de toute course d'auto-conception versée) ; Minuit lisible, ou « non lisible » avec la dépense antérieure qui comprend la course d'auto-conception v4 ; `GEMINI_API_KEY` (part au pire 174 USD) et `OPENAI_API_KEY` « non lisibles » sous la dispense `{"par": "mère", "reference": "R-3237", "cles": [...]}` ; pas de clé de Kimi.
- Prix Claude du jour : gabarit `course-v8/releve-prix-claude-gabarit-course-affinage-v8.json` → `course-v8/releve-prix-claude-course-affinage-v8.json`.
- Sceller les deux fichiers : `cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-affinage-mentors-v1/course-v8/releve-credits-avant-course-affinage-mentors-v8.json docs/notes/organisme-affinage-mentors-v1/course-v8/releve-prix-claude-course-affinage-v8.json`.

## 9. Lancement (une seule fois), détaché de la session

La course dure plusieurs heures (Carbon : jusqu'à 1 770 s par appel, seize appels en série) : le lanceur est lancé **détaché** par `setsid` et `nohup`, sorties dans des fichiers neufs, PID noté ; la session qui lance peut se fermer sans couper la course.

```sh
mkdir -p /home/user/sorties-lanceur-affinage-v8
cd /home/user/controle-ia-travail && GO_ID=GO-2026-11-18-14 setsid nohup /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v8.py > /home/user/sorties-lanceur-affinage-v8/lanceur.stdout.txt 2> /home/user/sorties-lanceur-affinage-v8/lanceur.stderr.txt < /dev/null & echo "PID_LANCEUR=$!"
```

Suivi, sans rien lire des cartes : `kill -0 «PID_LANCEUR» && echo EN-COURS` ; `cat /home/user/sorties-lanceur-affinage-v8/lanceur.stdout.txt` (ligne du manifeste de départ, puis, à la fin, ligne du manifeste de fin et code) ; `cat /home/user/sorties-lanceur-affinage-v8/lanceur.stderr.txt` (motif d'un refus). Un refus avant le départ rend la main en quelques secondes (code 2 ou 3, rien n'est appelé, relance possible après correction). Arrêt d'urgence : `kill -TERM «PID_LANCEUR»` (le lanceur relaie le signal à l'orchestrateur, qui s'arrête proprement et écrit ses manifestes ; R10, jamais par motif). **Codes** (v7, inchangés en v8) : 0 course finie ; 2 refus avant le départ ; 3 alerte de crédit avant le départ ; 4 cumul au-dessus de 150 USD ; 5 arrêt par la garde de crédit (alerte scellée pour la mère, qui prévient Lazar) ; **6** course partie dont l'orchestrateur rend un code non nul (arrêt, nœud, signal) ou dont le lanceur échoue après le départ — le vrai code de l'orchestrateur est au manifeste de fin (`code_orchestrateur`). Le code se lit au manifeste de fin (`code_du_lanceur`) et sur la dernière ligne de `lanceur.stdout.txt`.

Le manifeste de départ écrit `reglages_carbon_v8` : sortie demandée (6 948 à 7 174 jetons), pire cas d'un appel (1,499959 USD au prix plein ; 0,74998 au prix du lot), durée maximale de la commande (1 770 s).

## 10. Après

1. Attendre la fin du lanceur (`kill -0 «PID_LANCEUR»` faux, manifeste de fin écrit). Lire `/relais/etat` de chaque relais de la course (Claude, Argon, Carbon, Astra), puis l'arrêter **par son PID** (`kill -INT «PID»`, procédure § 6, R10) ; consigner chaque arrêt dans `registres/arrets.md`. Les ports 8787 à 8793 redeviennent libres pour l'autre course.
2. Relever les soldes quand l'interface le permet ; comparer au reste estimé du manifeste de fin ; toute alerte va à la mère, puis à Lazar. Avant toute course d'auto-conception : **relevé des crédits refait** pour elle, avec la dépense réelle de cette course.
3. Inscrire la dépense réelle par relais au registre des dépenses, avec l'écart au devis (base : espèces actives ; cinq espèces = 41,136 USD sans marge, devis v8).
4. Verser `runs/<id>-course-affinage-mentors-v8/` ; sorties de l'orchestrateur hors dépôt sous `/home/user/sorties-course-affinage-mentors-v8/<id>/` (et `<id>-preparation/`). Aucune lecture des cartes avant la mère. Les codes 7, 6 et 5 de Carbon se comptent au manifeste de fin (`cout_reel`, rôles arrêtés) sans ouvrir de carte.

## Essai à blanc v8 déjà fait

`course-v8/essai-a-blanc-v8/` : orchestrateur réel épinglé, moteur simulé, relais factices ; commandes de Carbon et d'Astra extraites de `main` hors dépôt et vérifiées à l'empreinte ; cinq espèces (Kimi absent), 160 cartes à passeport, codes 0 et 0 ; base du devis 41,136 USD, écart −35,536 pour un coût simulé de 5,6 ; `reglages_carbon_v8` au manifeste de départ (sortie demandée 6 948 sur le fil le plus long, pire cas 1,499959 USD). Relais, portes, registre dérivé, prix du jour et sonde ne sont pas exigés en moteur simulé : ils sont essayés par les essais du § 4.

## Ce qui ne vaut plus

Les commandes `course-v7/commandes-exactes-course-affinage-v7.md` (`e508db13…`), `course-v6/commandes-exactes-course-affinage-v6.md` (`11b8c078…`) et `course-v6/commandes-exactes-course-affinage-v6b.md` (`1fce4cea…`) restent en place (R12) et **ne valent plus** : la v7 lance la commande de Carbon avec la provision de 8 192 jetons et le délai de 1 500 s qui ont fait échouer la course d'auto-conception v4 (diagnostic `510312b1…`), et les v6 lancent le lanceur v6 (contre-lecture complète v6/v6b, constats 1 et 4).
