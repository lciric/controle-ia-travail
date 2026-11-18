# Commandes exactes — course d'affinage des idées des mentors, version 7 (rien n'est lancé ici)

- Écrit le 2026-11-18T16:12:58Z (`date -u +%FT%TZ`) par le modèle L', correctif v7 demandé par la mère après la contre-lecture complète de la v6 et des commandes v6b (modèle K, `course-v6/contre-lecture-complete-course-affinage-v6-v6b.md`, « Scellable après corrections. »). **Version 7** (R12) : ce texte se suffit ; il ne renvoie à aucun texte de commandes antérieur (voir la dernière section). Seul le lanceur v7 se lance, depuis une **session d'exécution neuve ouverte par la mère** (garde de calcul chargée, variable `RR_ANTHROPIC_API_KEY_MINUIT` présente et non vide).
- Composition déclarée (mot du directeur, 18 novembre vers 10:50Z ; R-3279) : **deux espèces Claude, Argon, Astra, Carbon ; pas de Kimi** (le lanceur v7 refuse toute déclaration de Kimi). Clé de tous les appels Claude : `RR_ANTHROPIC_API_KEY_MINUIT` seule ; `RR_ANTHROPIC_API_KEY_RIGAUD` n'est pas employée. `compter_limite_de_debit_comme_soupcon` = faux (R-3279, option (b)). Plafond d'arrêt : 150 USD (GO-2026-11-18-14). Règles de clé : R-3237. Procédure des relais : `docs/procedures/relais-persistants-v1.md` (R-3238).
- Chaque bloc se copie seul ; aucun ne suppose une variable posée par un autre bloc (chemins écrits en entier) ; `«J»` = la date du jour (`date -u +%F`) ; `«PID_…»` = un PID imprimé par le lanceur de relais. Le lanceur ne clone rien et ne loue aucune instance (`DEPOT_URL` sans objet ; s'il fallait cloner : `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`).
- Chemin de l'orchestrateur écrit ci-dessous : `/home/user/ideation-organism/orchestrator` ; si la copie de la session est `/home/user/lciric/ideation-organism/orchestrator`, remplacer ce préfixe partout (jamais les deux copies à la fois).
- Empreintes : lanceur v7 `scripts/lancer_course_affinage_mentors_v7.py` **`4439a61418814af34f170f15d7eb30c2b7763fd9074cc7e117ef4368eb2e680b`** ; préenregistrement épinglé `course-v7/preenregistrement-course-affinage-mentors-v7.md` **`720cbe81bbe5fe359ee8a8c814d374f3e52fac430351d8d29c6113ce9ae1d533`**.

## 0. Préalables (mère), avant toute commande

1. Montants absents du registre des dépenses (relevé d'ensemble § 3.4, environ 41,82 USD) inscrits ; **dépense de la sonde d'Astra du 18 novembre** (0,00041 USD, appel réel trivial, R-3273, hors de la ligne de GO-2026-11-18-14 qui ne vise que la course) inscrite au registre des dépenses avec la référence R-3273 (information 11 de la contre-lecture).
2. **Contre-lecture** du préenregistrement v7 et du lanceur v7 par un agent neuf du **modèle K**, scellée, à ce chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v7/contre-lecture-preenregistrement-course-affinage-mentors-v7.md`. Elle cite en entier `720cbe81bbe5fe359ee8a8c814d374f3e52fac430351d8d29c6113ce9ae1d533` (préenregistrement v7) et `4439a61418814af34f170f15d7eb30c2b7763fd9074cc7e117ef4368eb2e680b` (lanceur v7), se dit du modèle K, ne dit pas qu'elle n'a pas relu, et la première ligne de sa section `## Verdict` est exactement `Scellable.` (ou `**Scellable.**`).
3. Relais Claude unique, plafonné à 150 USD (R-3256) : confirmé.
4. Réserves de cloisonnement : 20 entrées retirées tant qu'aucune n'est levée par écrit ; **CW15 reste servie**.
5. **Ligne de GO** : le lanceur exige que `registres/go.md` du dépôt soit celui de `origin/main` (§ 2) ; il passe à l'orchestrateur un registre dérivé (ligne de GO-2026-11-18-14 et révocations qui la visent) qui cite le commit de `main` (R-3249).
6. **Carbon** déclarée (R-3274), sur la même clé qu'Argon (`GEMINI_API_KEY`) : part au pire de cette clé 150 + 24 = 174 USD. **Astra** déclarée seulement si la sonde commune du jour a réussi (§ 5) ; sinon Astra retirée de la déclaration, motif dans `absences.astra`, mère prévenue (la tentative n'est pas brûlée). **Kimi non déclaré** (R-3279 ; le lanceur v7 le refuse : liste des références admises vide). Le risque d'une espèce déclarée qui échoue à l'échelle (A14 : étape « non mesurée (technique) ») est accepté par le mot du directeur.
7. **Limite de débit** : `compter_limite_de_debit_comme_soupcon` = faux, déjà écrit dans le gabarit v7. À dire à la mère (information 12) : la garde v6 ne compte pas comme soupçon une ligne qui porte « per minute », « par minute », « rate limit », « rate-limit », « rate_limit », « requests per » ou « too many requests » sans mot de crédit ni de facturation — un peu plus que les deux formules de R-3279 ; les essais le couvrent.
8. Note périmée : la pièce `course-v3/procedure-relais-persistants-course-affinage-v3.json` dit encore que chaque porte lance le lanceur de relais ; depuis la v4, c'est la porte épinglée `scripts/porte_plafond_relais_v1.py` qui ouvre chaque commande de porte. La pièce reste épinglée pour ses empreintes.

## 1. Les deux courses de l'organisme : affinage et auto-conception (majeur 2)

- L'affinage (cette course) et l'auto-conception **ne tournent jamais en même temps**. Elles partagent les ports **8787 à 8793** (8787 relais Claude, 8788 relais d'Argon, 8790 relais d'Astra, 8792 relais de Carbon, 8793 relais jeté de la sonde ; 8789 et 8791 réservés, la sonde commune les refuse aussi), la clé `RR_ANTHROPIC_API_KEY_MINUIT` (200 USD déclarés ; part au pire de 150 USD **dans chaque course**), les clés `GEMINI_API_KEY` et `OPENAI_API_KEY`, et le rapport de la sonde d'Astra du jour. Les ports d'Argon, d'Astra et de Carbon sont écrits en dur dans le lanceur : deux courses simultanées sont impossibles par construction.
- **Avant cette course**, si l'auto-conception a tourné (ou tourne) le même jour : attendre son manifeste de fin ; arrêter **chacun de ses relais par son PID** (`kill -INT «PID»`, R10), lire d'abord `/relais/etat` de chacun, consigner chaque arrêt dans `registres/arrets.md` ; vérifier que les ports 8787 à 8793 sont libres (bloc ci-dessous) ; puis **relevé des crédits refait** (§ 8) **après** cette fin, avec la dépense réelle de l'auto-conception (Minuit : reste relu, ou dépense antérieure qui la comprend). Le lanceur v7 refuse le départ si une course d'auto-conception a un manifeste de départ sans manifeste de fin, ou si l'heure du relevé n'est pas postérieure à son manifeste de fin. Un relevé écrit trop tôt ne se réécrit pas (R12) : **écrire le relevé en dernier**, juste avant le lancement.
- Les relais de cette course sont **neufs** (lancés après la fin de l'autre course) ; le lanceur v7 refuse un relais qui a déjà servi (état lu non nul) et les relais de l'auto-conception, réglés autrement (Astra à 34 USD et 60 appels, Carbon à 15 lots : refusés par les bornes du § 6).
- **Après cette course**, avant toute course d'auto-conception : relais de cette course arrêtés par leur PID et consignés (§ 10), relevé des crédits refait pour l'autre course.
- **Sonde d'Astra** : le rapport d'une sonde commune vaut pour les deux courses **le même jour seulement** (§ 5).

```sh
/usr/local/bin/python3 -I -c "import socket,sys;o=[p for p in range(8787,8794) if socket.socket().connect_ex(('127.0.0.1',p))==0];print('PORTS OCCUPES',o) if o else print('PORTS-8787-8793-LIBRES');sys.exit(1 if o else 0)"
```

(À jouer avant de lancer les relais du § 6 ; « PORTS OCCUPES » : identifier le relais par `cat /proc/«PID»/cmdline | tr '\0' ' '`, l'arrêter par son PID s'il appartient à une course finie, sinon s'arrêter.)

## 2. Dépôt, mise à jour sur `main`, empreintes

Les pièces v7 sont sur la branche qui porte ce fichier (`prep/affinage-v7-compte-organisme-v1`, puis `lot/compte-organisme-v1` une fois versée par la mère) ; remplacer `origin/lot/compte-organisme-v1` ci-dessous par `origin/prep/affinage-v7-compte-organisme-v1` tant qu'elle n'est pas versée. Les empreintes tranchent.

```sh
cd /home/user/controle-ia-travail && git fetch -q origin +refs/heads/main:refs/remotes/origin/main && git fetch -q origin +refs/heads/lot/compte-organisme-v1:refs/remotes/origin/lot/compte-organisme-v1
cd /home/user/controle-ia-travail && git checkout -q origin/main -- registres/go.md
cd /home/user/controle-ia-travail && git checkout -q origin/lot/compte-organisme-v1 -- scripts/lancer_course_affinage_mentors_v7.py scripts/garde_credit_relais_v6.py scripts/porte_plafond_relais_v1.py scripts/sonde_astra_affinage_v2.py scripts/sonde_astra_courses_v1.py scripts/lancer_relais_local_v1.py scripts/construire_fils_course_affinage_mentors_v1.py tests/test_lancer_course_affinage_mentors_v7.py tests/test_lancer_course_affinage_mentors_v6.py tests/test_astra_carbon_declares_affinage_v6b.py tests/test_sonde_astra_courses_v1.py docs/procedures/relais-persistants-v1.md docs/notes/organisme-affinage-mentors-v1 docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-2026-11-18-v1.json docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-2026-11-18-v1.json.sha256 docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py
cd /home/user/controle-ia-travail && echo "4439a61418814af34f170f15d7eb30c2b7763fd9074cc7e117ef4368eb2e680b  scripts/lancer_course_affinage_mentors_v7.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "720cbe81bbe5fe359ee8a8c814d374f3e52fac430351d8d29c6113ce9ae1d533  docs/notes/organisme-affinage-mentors-v1/course-v7/preenregistrement-course-affinage-mentors-v7.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "1d9882f71b01491c3282d24b963d14e8ad4339c855ec969f85b420c463c60fff  scripts/garde_credit_relais_v6.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "fab5fe2e924c47799d968663baddfecb85dd6f74e9f859d9047b185eb36382b1  scripts/porte_plafond_relais_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "1799449269e15661b92f2a45eaab95a22e3a766a1fdf10ec9a4648bbe92aebf7  scripts/sonde_astra_affinage_v2.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "d374d1071f4ef70b3604d97dc62e2f14103c440a166342b330d7a576d8b4c777  scripts/sonde_astra_courses_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "d365affcb0303283a71ac7d5e67e24a5b6060e3b13c2a9e83ea592e48d4b3c82  scripts/lancer_relais_local_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "ff2b38e23d7d97dfda95084bbf7e7b9a64f0c83a943141a355d0e136f8d4c912  scripts/construire_fils_course_affinage_mentors_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "a7d92564cdc2a6a0435b0d271970acee633dd34a087c7c8cb95da7f70003d834  tests/test_lancer_course_affinage_mentors_v7.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "8a8db77a253ebe16e2545f9702562f408fd1d8ea3311db509a152f3e94c90485  tests/test_lancer_course_affinage_mentors_v6.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "30babf8fe466ce04fadcacf40349dd0e526dbf918188a147b6eb6a5f91cf9fc5  tests/test_astra_carbon_declares_affinage_v6b.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "0ff8ba72d999d9fd97d08707b7cc9fe91b9ce7a17bf9b42918e2f76c8189fefd  tests/test_sonde_astra_courses_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "0ca9cf5daa190135f8f26175f2639e4c9c4b22b01c551ab30ff8f7bb0d085148  docs/procedures/relais-persistants-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "0ea89ed2f72ce2693e619eb10b6eecbd46725d4578b548a44c5a98b9bb1ded21  docs/notes/organisme-affinage-mentors-v1/course-v6/configuration-course-affinage-mentors-v6.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "03b7eaa6d3757de6a26d0b230d84c9cf06da92bfff3f1daebc815c29994d134b  docs/notes/organisme-affinage-mentors-v1/course-v5/confidentialite-textes-servis-course-affinage-v5.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "121c6968cfbed3980dbba0d26add7357c24a615118f8100e580d083119c700d4  docs/notes/organisme-affinage-mentors-v1/course-v7/declaration-relais-gabarit-course-affinage-v7.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "0c2dc7489991c1dd786e94bbcfc349b13d3f7def197613d4b338aef7814cfecd  docs/notes/organisme-affinage-mentors-v1/course-v7/releve-credits-gabarit-course-affinage-v7.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "8065539dca13e5a77e2096b3378548ece3c7de470c99fc52cbce615743789eed  docs/notes/organisme-affinage-mentors-v1/course-v7/releve-prix-claude-gabarit-course-affinage-v7.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "d97594dbc2263cd4200113d44dd4fd3fc8562bef617d3e182f6a382bf95ec792  docs/notes/organisme-affinage-mentors-v1/course-v3/procedure-relais-persistants-course-affinage-v3.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "c30928c88feffc16d3aa1119efe2a54ba2d70cf135b8068855190a21470a56bb  docs/notes/organisme-affinage-mentors-v1/course-v1/fils-servis-et-retraits-course-affinage-mentors-v1.json" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "d36ba0a01c1c190d55d0ed63b053c951b5a767a9310013321d797e3e203d8c4f  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-proposeur-course-affinage-mentors-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "903318d7659db07819cbe9a7f89cbdbd292f59e14c32bb8811d8f8cb35dd955b  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-aiguilleur-course-affinage-mentors-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "a32583b14845343a613514cdcba3c24831a274b48ecc95fe0d884f017d27d346  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-juge-course-affinage-mentors-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "1ac9791b6aea1c97f534e32980f1f837cca425806ce8235b1064d98ce261dcbf  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-passe-tableau-course-affinage-mentors-v1.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "48dfd571d3f9a2042a363ccb7c35da30ab6b924fc443ae83139d0f75880dddaa  docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v6.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "2326666d11529c59799205de6014ca94bdc8c9b0ac0d1139eacb281579ebb129  docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v6b.md" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a  rapports/fille-ideation-1-v1/appel-argon-v5.sh" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46  docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py" | sha256sum -c -
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -c "import os,sys;sys.exit(0 if os.environ.get('RR_ANTHROPIC_API_KEY_MINUIT','').strip() else 1)" && echo MINUIT-PRESENTE-NON-VIDE
```

Toute ligne autre que « OK » : arrêt, rien n'est lancé. (La dernière ligne teste le nom et la non-vacuité — une valeur faite d'espaces compte comme vide —, jamais la valeur, qui n'est ni imprimée ni écrite.)

## 3. Orchestrateur (lecture seule) et pièces extraites de `main` (hors dépôt, vérifiées)

```sh
test "$(git -C /home/user/ideation-organism rev-parse HEAD)" = a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb && test -z "$(git -C /home/user/ideation-organism status --porcelain --untracked-files=all --ignored=matching)" && echo ORCHESTRATEUR-OK
echo "1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153  /home/user/ideation-organism/orchestrator/pole/relais_reel.py" | sha256sum -c -
/usr/local/bin/python3 -I -B -c "import claude_agent_sdk" && command -v bwrap socat
mkdir -p /home/user/pieces-affinage-v7
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py > /home/user/pieces-affinage-v7/commande_gemini_lot_v1.py && echo "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75  /home/user/pieces-affinage-v7/commande_gemini_lot_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py > /home/user/pieces-affinage-v7/commande_astra_v1.py && echo "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71  /home/user/pieces-affinage-v7/commande_astra_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v4.py > /home/user/pieces-affinage-v7/relais_gemini_v4.py && echo "543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4  /home/user/pieces-affinage-v7/relais_gemini_v4.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py > /home/user/pieces-affinage-v7/relais_gemini_v2.py && echo "2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb  /home/user/pieces-affinage-v7/relais_gemini_v2.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py > /home/user/pieces-affinage-v7/relais_kimi_v4.py && echo "67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e  /home/user/pieces-affinage-v7/relais_kimi_v4.py" | sha256sum -c -
```

## 4. Essais hors ligne (aucun appel), sauts visibles

```sh
cd /home/user/controle-ia-travail && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src /usr/local/bin/python3 -B -m pytest -q -rs -p no:cacheprovider tests/test_lancer_course_affinage_mentors_v7.py tests/test_lancer_course_affinage_mentors_v6.py tests/test_astra_carbon_declares_affinage_v6b.py tests/test_sonde_astra_courses_v1.py
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v7.py --a-blanc /tmp/essai-a-blanc-affinage-v7-$(date -u +%Y%m%d%H%M%S)
```

Attendu : **319 passed, 0 skipped** (175 essais v7 + 125 v6 + 5 v6b + 14 de la sonde commune) ; la ligne finale doit dire **0 skipped** (l'orchestrateur est présent : § 3) ; tout saut est nommé par `-rs` et arrête la session (il cache un essai de la vraie classe `PortePlafondCommande` ou de la coupure du plafond sur l'orchestrateur épinglé). Essai à blanc au code 0. Les essais lisent `origin/main` (récupérée au § 2) ; les essais de la v6b et de la sonde commune jouent la sonde commune devant un relais factice et datent par `date -u` : ils sont à jouer du 18 au 30 novembre (période de la ligne de GO d'essai).

## 5. Sonde d'Astra (R-3273) : celle du 18 novembre, ou une sonde neuve

**Le 18 novembre** : la sonde commune a déjà été jouée (13:58Z, relais jeté de la sonde PID 5016, port 8793, 0,00041 USD) ; ses deux rapports sont acceptés par le lanceur v7 **ce jour-là seulement** : `docs/notes/organisme-affinage-mentors-v1/course-v6/sonde-astra-course-affinage-v6.json` (`d2cacbcf1872de9d90cdff440bafa61698b3a19e2ffb7c1646eecc29a5b7872f`) et `docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-2026-11-18-v1.json` (`802b840edbf14983ce302b71253242c753e70aa60335868e811fdb6fd45e8f43`) ; le lanceur exige que le second cite le premier par son empreinte et par le PID du relais jeté. Ne rien rejouer ; vérifier :

```sh
cd /home/user/controle-ia-travail/docs/notes/organisme-affinage-mentors-v1/course-v6 && sha256sum -c sonde-astra-course-affinage-v6.json.sha256 && cd /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/course-v2 && sha256sum -c sonde-astra-commune-2026-11-18-v1.json.sha256
```

**Arrêt du relais jeté de la sonde** (constat 2 c) : aucune commande antérieure ne l'arrêtait. S'il vit encore, vérifier que le PID est bien lui, puis l'arrêter **par son PID** (R10) et consigner l'arrêt dans `registres/arrets.md` :

```sh
test -d /proc/5016 && tr '\0' ' ' < /proc/5016/cmdline && echo && curl -s --noproxy '*' http://127.0.0.1:8793/relais/etat
```

Si la ligne lue contient `relais_kimi_v4.py` et `--port 8793` : `kill -INT 5016`. Sinon (PID absent ou autre programme) : ne rien tuer, écrire « relais jeté PID 5016 déjà arrêté (ou PID repris) » dans `registres/arrets.md`.

**Un autre jour** : le rapport du 18 novembre est refusé (sonde « du jour » exigée) ; refaire **une** sonde commune neuve, au plus 0,05 USD (appel réel trivial, signalé à la mère, inscrit au registre des dépenses avec R-3273), avant le § 6 et après la fin de toute course d'auto-conception du jour, rapports sous `course-v7/` aux noms datés que lit le lanceur v7 :

```sh
mkdir -p /home/user/sonde-astra-«J»
cd /home/user/sonde-astra-«J» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sonde-astra-«J»/console-astra-sonde.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/pieces-affinage-v7/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8793 --modeles-permis gpt-6-astra --plafond-usd 0.05 --reserve-par-appel 0.01 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 1 --journal /home/user/sonde-astra-«J»/journal-relais-astra-sonde.jsonl
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/sonde_astra_courses_v1.py --commande /home/user/pieces-affinage-v7/commande_astra_v1.py --url-relais-jete http://127.0.0.1:8793 --pid-relais-jete «PID_DU_RELAIS_JETE» --sortie docs/notes/organisme-affinage-mentors-v1/course-v7/sonde-astra-commune-«J»-v1.json --sortie-v2 docs/notes/organisme-affinage-mentors-v1/course-v7/sonde-astra-course-affinage-v7-«J».json
```

Codes de la sonde commune : 0 réussie ; 1 non réussie, rapport écrit (`echec_de_configuration` vrai : rien n'est parti, ce n'est pas un échec d'Astra ; relancer un relais jeté neuf et la sonde sur des chemins neufs est une version suivante du lanceur, qui ne lit que ces noms) ; 2 refus avant tout appel, rien d'écrit. Puis `/relais/etat` du relais jeté de la sonde (1 appel, dépense ≤ 0,05), arrêt **par son PID** (`kill -INT «PID_DU_RELAIS_JETE»`, R10), consigner dans `registres/arrets.md`, signaler la dépense à la mère. Le relais jeté (port 8793) n'est jamais le relais de la course (port 8790), qui reste neuf. Ce rapport du jour vaut aussi pour une course d'auto-conception **du même jour** (sa pièce de départ le cite comme `sonde_du_jour`).

## 6. Relais de la course — chacun lancé par le lanceur de relais, PID noté (ports libres : § 1)

```sh
mkdir -p /home/user/sorties-relais-affinage-v7
cd /home/user/sorties-relais-affinage-v7 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sorties-relais-affinage-v7/console-claude.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_MINUIT -- /usr/bin/python3 -I -B /home/user/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_MINUIT --port 8787 --plafond-usd 150 --modeles-permis "$(/usr/local/bin/python3 -I -c "import json;c=json.load(open('/home/user/controle-ia-travail/docs/notes/organisme-affinage-mentors-v1/course-v6/configuration-course-affinage-mentors-v6.json'));print(','.join(sorted(e['modele'] for e in c['especes'] if e['famille']=='claude')))")" --journal /home/user/sorties-relais-affinage-v7/journal-relais-claude.jsonl
cd /home/user/sorties-relais-affinage-v7 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sorties-relais-affinage-v7/console-argon.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/pieces-affinage-v7/relais_gemini_v2.py --port 8788 --max-appels 450 --modele gemini-4-argon --journal /home/user/sorties-relais-affinage-v7/journal-relais-argon.jsonl
cd /home/user/sorties-relais-affinage-v7 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sorties-relais-affinage-v7/console-carbon.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/pieces-affinage-v7/relais_gemini_v4.py --port 8792 --max-appels 40 --max-lots 20 --modele gemini-4-carbon --journal /home/user/sorties-relais-affinage-v7/journal-relais-carbon.jsonl
```

Astra, **seulement si la sonde du jour a réussi** (§ 5), relais **neuf** (jamais celui de la sonde) :

```sh
cd /home/user/sorties-relais-affinage-v7 && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sorties-relais-affinage-v7/console-astra.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/pieces-affinage-v7/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8790 --modeles-permis gpt-6-astra --plafond-usd 24 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 20 --journal /home/user/sorties-relais-affinage-v7/journal-relais-astra.jsonl
```

**Bornes contrôlées par le lanceur v7** (lues par PID et sur `/relais/etat`, qui doit rendre les mêmes valeurs ; une borne absente de la ligne de commande est refusée) : Claude `--plafond-usd 150` ; Argon `--max-appels` ≥ 2 × (16 + 32 × espèces) = 352 pour cinq espèces (450 ici) ; Carbon `--max-lots` ≥ 20 et `--max-appels` ≥ 40 (ici `--max-appels 40 --max-lots 20`) ; Astra `--plafond-usd 24` **exactement** (sa part au pire, 16 × 1,50) et `--max-appels` ≥ 20 (ici `--max-appels 20`), réserve par appel au plus 1,50 (défaut du relais : 0,40 ; ne jamais recopier `--reserve-par-appel 0.01 --max-appels 1 --plafond-usd 0.05` de la sonde : refusé), prix 10 / 50. **Pourquoi ces marges** : l'orchestrateur épinglé fait un appel par case et par proposeur, sans reprise ; la commande d'Astra un envoi par appel ; celle de Carbon un `countTokens` et un lot par appel : 16 appels (et 32 envois pour Carbon) suffisent à la lecture ; la marge de 4 couvre ce que la lecture ne peut exclure (un appel refusé par le relais compte quand même). Elle ne touche aucun dollar : le plafond du relais d'Astra reste 24 USD (la somme des réserves de 16 appels sous un plafond de session de 1,50 ne dépasse pas 24 : aucun refus 402 par construction) ; Carbon reste borné par le plafond de session de sa commande et les seize appels de l'orchestrateur ; le plafond d'arrêt de 150 USD borne tout.

Vérifier chaque relais par PID et `/relais/etat` (procédure § 3) : 0 appel, 0 dépense, 0 engagé, 0 lot, modèles conformes, `variable_cle_encore_presente` faux (Argon, Carbon, Astra).

## 7. Déclaration des relais (écrire, puis sceller)

Chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v7/declaration-relais-course-affinage-mentors-v7.json`. Recopier le gabarit v7 (`course-v7/declaration-relais-gabarit-course-affinage-v7.json`), remplir les **quatre PID** (un relais Claude pour les deux espèces Claude, plus Argon, Carbon, Astra) et la liste des modèles Claude de la configuration v6 (même commande qu'au § 6), retirer la clé `gabarit` ; Astra retirée seulement si la sonde du § 5 n'a pas réussi (motif dans `absences.astra`). Les commandes d'Astra et de Carbon y sont **exactes** (le lanceur refuse tout autre argument). Puis : `cd /home/user/controle-ia-travail && PYTHONPATH=src python3 -m controle_ia.scellement sceller docs/notes/organisme-affinage-mentors-v1/course-v7/declaration-relais-course-affinage-mentors-v7.json`.

## 8. Relevés du jour — en dernier, juste avant le lancement (écrire depuis les gabarits v7, puis sceller)

- Crédits : gabarit `course-v7/releve-credits-gabarit-course-affinage-v7.json` → `course-v7/releve-credits-avant-course-affinage-mentors-v7.json` ; `releve_utc` = sortie de `date -u +%FT%TZ` au moment du relevé (le lanceur v7 exige cette forme et une heure postérieure à la fin de toute course d'auto-conception versée) ; Minuit lisible, ou « non lisible » avec la dépense antérieure qui comprend toute course déjà faite sur elle ; `GEMINI_API_KEY` (part au pire 174 USD) et `OPENAI_API_KEY` « non lisibles » sous la dispense `{"par": "mère", "reference": "R-3237", "cles": [...]}` ; pas de clé de Kimi.
- Prix Claude du jour : gabarit `course-v7/releve-prix-claude-gabarit-course-affinage-v7.json` → `course-v7/releve-prix-claude-course-affinage-v7.json`.
- Sceller les deux fichiers.

## 9. Lancement (une seule fois)

```sh
cd /home/user/controle-ia-travail && GO_ID=GO-2026-11-18-14 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v7.py
```

Le lanceur contrôle l'autre course de l'organisme (§ 1), chaque relais (PID, programme, port, modèles, bornes basses, état lu neuf et complet), la sonde d'Astra (rapport v2 lié à la sonde commune du jour), la confidentialité de chaque texte servi, puis joue la porte à blanc avant le manifeste de départ ; préparation hors dépôt (`/home/user/sorties-course-affinage-mentors-v7/<id>-preparation/`) ; `runs/<id>-course-affinage-mentors-v7/` et le dossier de sortie ne sont créés qu'après la porte à blanc. **Codes** (v7, distincts de ceux de l'orchestrateur) : 0 course finie ; 2 refus avant le départ (rien n'est appelé, relance possible) ; 3 alerte de crédit avant le départ ; 4 cumul au-dessus de 150 USD ; 5 arrêt par la garde de crédit (alerte scellée pour la mère, qui prévient Lazar) ; **6** course partie dont l'orchestrateur rend un code non nul (arrêt, nœud, signal) ou dont le lanceur échoue après le départ — le vrai code de l'orchestrateur est au manifeste de fin (`code_orchestrateur`).

## 10. Après

1. Lire `/relais/etat` de chaque relais de la course (Claude, Argon, Carbon, Astra), puis l'arrêter **par son PID** (`kill -INT «PID»`, procédure § 6, R10) ; consigner chaque arrêt dans `registres/arrets.md`. Les ports 8787 à 8793 redeviennent libres pour l'autre course.
2. Relever les soldes quand l'interface le permet ; comparer au reste estimé du manifeste de fin ; toute alerte va à la mère, puis à Lazar. Avant toute course d'auto-conception : **relevé des crédits refait** pour elle, avec la dépense réelle de cette course.
3. Inscrire la dépense réelle par relais au registre des dépenses, avec l'écart au devis (base : espèces actives, cinq espèces = 37,576 USD sans marge).
4. Verser `runs/<id>-course-affinage-mentors-v7/` ; sorties de l'orchestrateur hors dépôt sous `/home/user/sorties-course-affinage-mentors-v7/<id>/` (et `<id>-preparation/`). Aucune lecture des cartes avant la mère.

## Essai à blanc v7 déjà fait

`course-v7/essai-a-blanc-v7/` : orchestrateur réel épinglé, moteur simulé, relais factices ; commandes de Carbon et d'Astra extraites de `main` hors dépôt et vérifiées à l'empreinte ; cinq espèces (Kimi absent), 160 cartes à passeport, code 0 ; écart au devis sur une base de 37,576 USD (cinq espèces) ; aucune autre course de l'organisme vue. Relais, portes, registre dérivé, prix du jour et sonde ne sont pas exigés en moteur simulé : ils sont essayés par les essais du § 4.

## Ce qui ne vaut plus

Les commandes `course-v6/commandes-exactes-course-affinage-v6.md` (`11b8c078…`) et `course-v6/commandes-exactes-course-affinage-v6b.md` (`1fce4cea…`) restent en place (R12) et **ne valent plus** : elles lancent le lanceur v6, qui n'a pas de contre-lecture « Scellable. » et dont les bornes d'Astra et la base du devis sont fausses (contre-lecture complète v6/v6b, constats 1 et 4).
