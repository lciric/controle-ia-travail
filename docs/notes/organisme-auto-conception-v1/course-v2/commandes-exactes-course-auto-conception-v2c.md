# Commandes exactes — course d'auto-conception de l'organisme d'idéation, correctif v2c (pour la session d'exécution)

Écrites le 18 novembre 2026 par le développeur unique du correctif v2c (modèle L′). Pièce **neuve** (R12) : les commandes v2 et v2b restent en place, archivées ; **ce texte se suffit à lui-même** (aucune étape n'est à chercher ailleurs). Fondement : mot de Lazar, 18 novembre 2026, « go (a), lance les deux correctifs » — écart au préenregistrement scellé accordé, sans changement d'hypothèse, de mesure, de seuil, de plafond, de témoins, de consignes, de matière, de composition ni de devis (additif v2c). **Rien n'a été lancé par l'auteur** : moteur simulé, adaptateurs réels construits sans appel, relais factices. Aucune valeur de clé n'est écrite nulle part (noms de variables seulement). `«D»` = un dossier hors dépôt neuf (par exemple `/home/user/execution-auto-conception-v2c`) ; `«CLONE»` = `/home/user/ideation-organism` (copie de l'orchestrateur au commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, propre).

Noms fixés : clé Claude **`RR_ANTHROPIC_API_KEY_RIGAUD`** (nommée par la pièce de départ) ; clé d'Argon **`GEMINI_API_KEY`** ; clé de Carbon **`GEMINI_API_KEY`** ; clé d'Astra **`OPENAI_API_KEY`** ; modèle de Carbon **`gemini-4-carbon`** ; modèle d'Astra `gpt-6-astra` ; modèle d'Argon `gemini-4-argon` ; modèles Claude `claude-opus-5-5`, `claude-fable-5-1`. Lignes de GO (pièce de départ) : course **`GO-2026-11-18-20`** (90 USD), épreuve des témoins **`GO-2026-11-18-21`** (5 USD).

## 0. Ce qui a changé (défaut constaté, correction)

`scripts/epreuve_temoins_auto_conception_v2.py --reel` s'est arrêté le 18 novembre **avant tout appel (0 USD)** : il remettait aux adaptateurs réels les chemins interdits `[base des sessions, sortie/"sortie"]` mais plaçait les dossiers des agents sous `sortie/"appels"` ; la garde de l'orchestrateur (`construire_options`) a refusé. Le programme d'épreuve **v3** place les dossiers sous `sortie/"sortie"/"appels"` et joue cette garde sur les 33 dossiers avant tout appel ; le lanceur **v3** l'épingle, épingle l'additif v2c et lit les pièces neuves ci-dessous. La course elle-même n'avait pas ce défaut (sessions sous la base interdite ; vérifié par essai). Tout le reste est inchangé.

## 1. Empreintes (à vérifier avant tout)

| pièce | sha256 |
|---|---|
| `scripts/lancer_course_auto_conception_v3.py` (lanceur v3, à citer en entier par la contre-lecture) | `42001b2807337cfd4c10c6708b384f5f218201457eab95d309080c6c57949fef` |
| `course-v2/additif-preenregistrement-course-auto-conception-v2c.md` (épinglé par le lanceur v3, à citer en entier par la contre-lecture) | `7c76eba0340040b2c2d29cf3aa5015a194632ac24f3e558565a22424702b0cfd` |
| `scripts/epreuve_temoins_auto_conception_v3.py` (épinglé par le lanceur v3) | `0c72dd8763537152b7339ca15ff439f759c062f0b33a6571a513029870eebd1b` |
| `course-v2/preenregistrement-course-auto-conception-v2.md` (inchangé, épinglé) | `0d51e0b3f51dd731351589187c124b7ee1a6237494aa0274825b19085c6763c6` |
| `course-v2/piece-de-depart-auto-conception-v2.json` (scellée, reprise telle quelle) | `e2689fa22fff31319ff69deefe10c066d5329fab28d9c9b133750f2534fc1ded` |
| `course-v2/sonde-astra-commune-2026-11-18-v1.json` (sonde du jour, faite, « ok » vrai) | `802b840edbf14983ce302b71253242c753e70aa60335868e811fdb6fd45e8f43` |
| `tests/test_epreuve_temoins_auto_conception_v3.py` (25 essais) | `126893941e924d8f846f23c983d271e073c4d420bc293e58b3e4d2552d135d36` |
| `tests/test_lancer_course_auto_conception_v3.py` (108 essais) | `868943c43e286e565ab5fca767a0e31a559eee9a56abc5f8fecb1c5ffdf938a9` |
| `scripts/garde_credit_relais_v5.py` (inchangée) | `6cf8786943bb6c9e51dd6909714e83de783e70dffc80ea1fad46a0e1545d30cd` |
| `scripts/porte_plafond_relais_v1.py` (inchangée) | `fab5fe2e924c47799d968663baddfecb85dd6f74e9f859d9047b185eb36382b1` |
| `scripts/lancer_relais_local_v1.py` (inchangé) | `d365affcb0303283a71ac7d5e67e24a5b6060e3b13c2a9e83ea592e48d4b3c82` |
| relais Claude `«CLONE»/orchestrator/pole/relais_reel.py` | `1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153` |
| relais Gemini d'Argon `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py` | `2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb` |
| enveloppe d'Argon `rapports/fille-ideation-1-v1/appel-argon-v5.sh` | `37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a` |
| relais compatible OpenAI d'Astra `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py` | `67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e` |
| commande d'Astra (sur `main`) `docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py` | `986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71` |
| commande de Carbon par lot (sur `main`) `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py` | `9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75` |
| relais Gemini v4 de Carbon (sur `main`) `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v4.py` | `543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4` |
| matière servie (sur `main`) `docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md` | `11f4b69ba42147c428090e4805948a708d0ed266da0c0cd07f194723eaba742d` |

```
cd /home/user/controle-ia-travail && git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
cd /home/user/controle-ia-travail && for f in scripts/lancer_course_auto_conception_v3.py scripts/epreuve_temoins_auto_conception_v3.py docs/notes/organisme-auto-conception-v1/course-v2/additif-preenregistrement-course-auto-conception-v2c.md docs/notes/organisme-auto-conception-v1/course-v2/preenregistrement-course-auto-conception-v2.md docs/notes/organisme-auto-conception-v1/course-v2/piece-de-depart-auto-conception-v2.json docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-2026-11-18-v1.json tests/test_epreuve_temoins_auto_conception_v3.py tests/test_lancer_course_auto_conception_v3.py; do (cd "$(dirname "$f")" && sha256sum -c "$(basename "$f").sha256"); done
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md | sha256sum
sha256sum /home/user/ideation-organism/orchestrator/pole/relais_reel.py && git -C /home/user/ideation-organism rev-parse HEAD && git -C /home/user/ideation-organism status --porcelain --untracked-files=all --ignored=matching
cd /home/user/controle-ia-travail && PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B -m pytest -q -rs -p no:cacheprovider tests/test_epreuve_temoins_auto_conception_v3.py tests/test_lancer_course_auto_conception_v3.py tests/test_lancer_course_auto_conception_v2.py tests/test_sonde_astra_courses_v1.py tests/test_astra_carbon_declares_auto_conception_v2b.py
```
Attendu : toutes les empreintes « OK » ; matière `11f4b69b…` ; relais Claude `1b90b020…` ; orchestrateur `a41b7b50…`, statut vide ; **25 + 108 + 108 = 241 essais passés**, aucun sauté (les essais lisent la matière et les commandes dans `refs/remotes/origin/main`).

## 2. Ce qui est déjà fait (ne pas refaire)

- **Sonde d'Astra du jour** : faite le 18 novembre, rapport `course-v2/sonde-astra-commune-2026-11-18-v1.json` (`802b840e…`, « ok » vrai, 0,00041 USD), cité par la pièce de départ. **Ne pas la refaire le même jour.** Vérification :
  ```
  cd /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/course-v2 && sha256sum -c sonde-astra-commune-2026-11-18-v1.json.sha256 && /usr/local/bin/python3 -I -c "import json,sys;o=json.load(open('sonde-astra-commune-2026-11-18-v1.json'));print(o['ok'],o['jour'],o['cout_usd']);sys.exit(0 if o['ok'] is True and o['jour']=='2026-11-18' else 1)"
  ```
  Attendu : `True 2026-11-18 0.00041`, code 0. Si le jour du lancement n'est plus le 18 novembre : la sonde n'est plus « du jour » — arrêt, mot de la mère (la pièce de départ scellée la cite).
- **Pièce de départ** : scellée (`e2689fa2…`), reprise **telle quelle** par le lanceur v3 ; ne pas la réécrire.
- **Lignes de GO** `GO-2026-11-18-20` (course, 90 USD, périmètre contenant « auto-conception ») et `GO-2026-11-18-21` (épreuve, 5 USD, périmètre contenant « témoins ») : doivent figurer dans `registres/go.md` sur `main`, type `calcul`, accordées par `Lazar`, période couvrant le jour du lancement ; le programme d'épreuve et le lanceur les lisent eux-mêmes dans `refs/remotes/origin/main` (fetch ciblé juste avant chaque lancement) et refusent sinon.

## 3. Contre-lecture du correctif (modèle K)

Exigée par le lanceur v3 avant la course ; à faire **avant l'épreuve** (le programme d'épreuve v3 est du code neuf). Par un contre-lecteur neuf du modèle K, qui n'a écrit ni l'additif ni le lanceur v3 ni le programme d'épreuve v3 (R2). Fichiers à lui donner : l'additif v2c, le préenregistrement v2, `scripts/epreuve_temoins_auto_conception_v3.py` et la v2, `scripts/lancer_course_auto_conception_v3.py` et la v2, les deux fichiers d'essais v3, `course-v2/rapport-developpeur-correctif-v2c.md`, ces commandes, la sortie d'erreur `course-v2/epreuve-reelle-arret-avant-appel-2026-11-18-v1/epreuve-reelle.stderr.txt`, et dans `«CLONE»/orchestrator` : `pole/adaptateurs.py` (`construire_options`), `pole/adaptateurs_v56.py`, `pole/noyau_v55.py`, `demonstrations/ideation_v8.py`. Rapport écrit et scellé à `docs/notes/organisme-auto-conception-v1/course-v2/contre-lecture-correctif-v2c-auto-conception.md` : il cite **en entier** `7c76eba0340040b2c2d29cf3aa5015a194632ac24f3e558565a22424702b0cfd` (additif) et `42001b2807337cfd4c10c6708b384f5f218201457eab95d309080c6c57949fef` (lanceur v3), se dit du modèle K, la première ligne sous « ## Verdict » est exactement « Scellable. », et il ne dit nulle part n'avoir pas relu. Une correction demandée donne de nouvelles versions (R12), donc de nouvelles empreintes : ces commandes ne valent plus.

## 4. Épreuve réelle des témoins (plafond 5 USD ; 33 appels ; avant la course)

Relais **propres à l'épreuve** (ceux de la course seront neufs ensuite).

```
mkdir «D» «D»/maison && cd «D»
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-claude-epreuve.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_RIGAUD -- /usr/bin/python3 -I -B /home/user/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_RIGAUD --port 8787 --plafond-usd 5 --modeles-permis claude-fable-5-1,claude-opus-5-5 --journal «D»/journal-relais-claude-epreuve.jsonl
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-gemini-epreuve.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle GEMINI_API_KEY --port 8788 --max-appels 15 --modele gemini-4-argon --journal «D»/journal-relais-gemini-epreuve.jsonl
```
Relever les deux PID (console de chaque relais), puis vérifier : `tr '\0' ' ' < /proc/«PID»/cmdline` (programme, port, variable) ; `curl -s --noproxy '*' http://127.0.0.1:8787/relais/etat` (0 appel, plafond 5) et `curl -s --noproxy '*' http://127.0.0.1:8788/relais/etat` (0 appel, `variable_cle_encore_presente` faux). (`--max-appels 15` : 11 appels nécessaires, marge de reprise ; « non conclue » reste un arrêt.)

Déclaration de l'épreuve, **chemin neuf**, écrite avec l'outil d'écriture de fichiers puis scellée : `docs/notes/organisme-auto-conception-v1/course-v2/declaration-relais-epreuve-temoins-auto-conception-v3.json`

```json
{"version": "declaration-relais-epreuve-temoins-auto-conception-v3", "fournisseurs": {
 "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:8787", "nom_cle": "RR_ANTHROPIC_API_KEY_RIGAUD", "pid_relais": «PID_CLAUDE_EPREUVE»,
            "porte_plafond": {"type": "commande", "delai_s": 30, "commande": ["/usr/local/bin/python3", "-I", "-B",
              "/home/user/controle-ia-travail/scripts/porte_plafond_relais_v1.py", "--url", "http://127.0.0.1:8787",
              "--modeles-permis", "claude-fable-5-1,claude-opus-5-5", "--plafond-ligne", "5"]}},
 "argon": {"type": "commande_externe", "commande": ["bash", "/home/user/controle-ia-travail/rapports/fille-ideation-1-v1/appel-argon-v5.sh"],
           "nom_cle": "GEMINI_API_KEY", "pid_relais": «PID_GEMINI_EPREUVE», "url_etat_relais": "http://127.0.0.1:8788",
           "porte_plafond": {"type": "environnement"}}}}
```
```
cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-auto-conception-v1/course-v2/declaration-relais-epreuve-temoins-auto-conception-v3.json
```

Lancement (environnement **sans aucun nom de clé** : le programme le refuse sinon ; il lit le registre des GO et la pièce de départ, contrôle les relais par PID, joue la porte à blanc, construit les adaptateurs réels, **vérifie les 33 dossiers d'appel avant tout appel**, puis appelle) :

```
cd /home/user/controle-ia-travail && git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
cd /home/user/controle-ia-travail && env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=«D»/maison LANG=C.UTF-8 /usr/local/bin/python3 -I -B scripts/epreuve_temoins_auto_conception_v3.py --reel > «D»/epreuve-reelle-v3.stdout.txt 2> «D»/epreuve-reelle-v3.stderr.txt; echo "code $?"
```
Codes : 0 rapport écrit (lire le verdict) ; 2 refus avant tout appel (motif sur la sortie d'erreur ; un refus « dossier d'appel … refusé par la garde de l'orchestrateur » ne dépense rien). Sortie : `course-v2/epreuve-temoins-reelle-auto-conception-v3.json` (scellé par le programme ; verdicts et classes bruts gardés ; champ `dossiers_d_appel` : racine sous `…/sortie/sortie/appels` et contrôle par rôle). **Si le verdict n'est pas « réussie » : arrêt, aucune course, rapport à la mère** (aucune retouche des témoins sans version neuve). Puis : `curl -s --noproxy '*' http://127.0.0.1:8787/relais/etat` et `…:8788/relais/etat` (dépense, appels), arrêt des deux relais **par PID** (`kill -INT «PID»`, R10), consigner l'arrêt et la dépense, verser le rapport, sa déclaration et les deux journaux (stdout, stderr, scellés).

## 5. Relevé des prix Claude du jour

Lire la page officielle des prix : **https://platform.claude.com/docs/en/about-claude/pricing** (version texte : `https://platform.claude.com/docs/en/about-claude/pricing.md`), lignes « Claude Opus 5.5 » et « Claude Fable 5.1 », colonnes entrée et sortie par million de jetons. Barème du relais (attendu) : `claude-opus-5-5` 4 / 20 USD, `claude-fable-5-1` 10 / 50 USD. Tout autre prix lu : **arrêt, nouveau devis** (le lanceur refuse).

Écrire (outil d'écriture de fichiers), puis sceller, `docs/notes/organisme-auto-conception-v1/course-v2/releve-prix-claude-course-auto-conception-v2.json` (chemin inchangé, jamais écrit à ce jour) ; `«date -u»` = la sortie de `date -u +%FT%TZ` :

```json
{"releve_utc": "«date -u»", "source": "https://platform.claude.com/docs/en/about-claude/pricing, lue le «date -u» : Claude Opus 5.5 4 / 20 USD, Claude Fable 5.1 10 / 50 USD par million de jetons (entrée / sortie)", "prix": {"espece_claude_1": {"entree": 4.0, "sortie": 20.0}, "espece_claude_2": {"entree": 10.0, "sortie": 50.0}}}
```
(`espece_claude_1` = `claude-opus-5-5`, `espece_claude_2` = `claude-fable-5-1`, dans l'ordre de la configuration.)

## 6. Relevé des crédits du jour (après l'épreuve)

Écrire puis sceller `docs/notes/organisme-auto-conception-v1/course-v2/releve-credits-avant-course-auto-conception-v2.json` (chemin inchangé, jamais écrit à ce jour). Clé Claude : le reste lu par l'interface de facturation, ou, illisible, `non_lisible` avec la dépense antérieure (épreuve comprise) ; **ne pas retrancher** les réserves 9 + 9 USD de la pièce de départ (le lanceur les retranche lui-même). Clés d'Argon, de Carbon (`GEMINI_API_KEY`, une seule ligne pour les deux relais) et d'Astra (`OPENAI_API_KEY`) : non lisibles, sous la **dispense écrite par la mère, référence R-3237** :

```json
{"releve_utc": "«date -u»",
 "cles": {"RR_ANTHROPIC_API_KEY_RIGAUD": {"credit_usd": «c», "reste_usd": «r», "source": "«interface lue»"},
          "GEMINI_API_KEY": {"non_lisible": true, "motif": "solde illisible (R-3222)"},
          "OPENAI_API_KEY": {"non_lisible": true, "motif": "solde illisible"}},
 "dispense": {"par": "mère", "reference": "R-3237", "cles": ["GEMINI_API_KEY", "OPENAI_API_KEY"]}}
```
(Variante si le solde Claude est illisible : `"RR_ANTHROPIC_API_KEY_RIGAUD": {"non_lisible": true, "depense_anterieure_usd": «d»}` — compté au crédit déclaré par la pièce de départ, 124 USD, moins `«d»`, moins les réserves.) Arrêt et alerte (code 3) si le reste net est ≤ 90 USD ou sous un cinquième du crédit.

## 7. Relais neufs de la course

Les relais de l'épreuve sont arrêtés (§ 4). Lancer, depuis `«D»` :

```
cd «D»
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-claude-course.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_RIGAUD -- /usr/bin/python3 -I -B /home/user/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_RIGAUD --port 8787 --plafond-usd 90 --modeles-permis claude-fable-5-1,claude-opus-5-5 --journal «D»/journal-relais-claude-course.jsonl
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-gemini-course.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle GEMINI_API_KEY --port 8788 --max-appels 280 --modele gemini-4-argon --journal «D»/journal-relais-gemini-course.jsonl
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py > «D»/commande_astra_v1.py && echo "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71  «D»/commande_astra_v1.py" | sha256sum -c -
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-astra.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8790 --modeles-permis gpt-6-astra --plafond-usd 34 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 60 --delai-amont-s 3400 --journal «D»/journal-relais-astra.jsonl
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py > «D»/commande_gemini_lot_v1.py && echo "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75  «D»/commande_gemini_lot_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v4.py > «D»/relais_gemini_v4.py && echo "543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4  «D»/relais_gemini_v4.py" | sha256sum -c -
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-carbon.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B «D»/relais_gemini_v4.py --variable-cle GEMINI_API_KEY --port 8792 --modele gemini-4-carbon --max-appels 60 --max-lots 15 --journal «D»/journal-relais-carbon.jsonl
```
Vérifier chaque relais par PID (`tr '\0' ' ' < /proc/«PID»/cmdline`) et `curl -s --noproxy '*' http://127.0.0.1:«PORT»/relais/etat` sur 8787, 8788, 8790, 8792 : **0 appel** partout (0 lot pour Carbon), plafond 90 (Claude), `--max-appels 280` (Argon : 231 appels au pire avec Astra et Carbon), variable de clé effacée (Gemini) ; sinon le lanceur refuse. Kimi n'est pas déclaré (aucun relais 8789). Ports 8787 à 8792 : aucune autre course ne tourne en même temps.

## 8. Déclaration des relais de la course (chemin neuf)

Écrire (outil d'écriture de fichiers), puis sceller, `docs/notes/organisme-auto-conception-v1/course-v2/declaration-relais-course-auto-conception-v3.json` :

```json
{"version": "declaration-relais-course-auto-conception-v3", "fournisseurs": {
 "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:8787", "nom_cle": "RR_ANTHROPIC_API_KEY_RIGAUD", "pid_relais": «PID_CLAUDE_COURSE»,
            "porte_plafond": {"type": "commande", "delai_s": 30, "commande": ["/usr/local/bin/python3", "-I", "-B",
              "/home/user/controle-ia-travail/scripts/porte_plafond_relais_v1.py", "--url", "http://127.0.0.1:8787",
              "--modeles-permis", "claude-fable-5-1,claude-opus-5-5", "--plafond-ligne", "90"]}},
 "argon": {"type": "commande_externe", "commande": ["bash", "/home/user/controle-ia-travail/rapports/fille-ideation-1-v1/appel-argon-v5.sh"],
           "nom_cle": "GEMINI_API_KEY", "pid_relais": «PID_GEMINI_COURSE», "url_etat_relais": "http://127.0.0.1:8788",
           "porte_plafond": {"type": "environnement"}},
 "astra": {"type": "commande_externe", "commande": ["/usr/local/bin/python3", "-I", "-B", "«D»/commande_astra_v1.py", "--url-relais", "http://127.0.0.1:8790",
           "--modele", "gpt-6-astra", "--prix-entree", "10", "--prix-sortie", "50"], "modele_propose": "gpt-6-astra", "nom_cle": "OPENAI_API_KEY",
           "pid_relais": «PID_ASTRA», "url_etat_relais": "http://127.0.0.1:8790", "porte_plafond": {"type": "environnement"}},
 "carbon": {"type": "commande_externe", "commande": ["/usr/local/bin/python3", "-I", "-B", "«D»/commande_gemini_lot_v1.py", "--url-base",
            "http://127.0.0.1:8792/v1beta", "--modele", "gemini-4-carbon", "--prix-entree", "8.3", "--prix-sortie", "41.5"],
            "modele_propose": "gemini-4-carbon", "nom_cle": "GEMINI_API_KEY", "pid_relais": «PID_CARBON»,
            "url_etat_relais": "http://127.0.0.1:8792", "porte_plafond": {"type": "environnement"}}}}
```
(`«D»` écrit en chemin absolu, le même qu'au § 7.) Le lanceur vérifie : mot de la mère dans la pièce de départ (Astra et Carbon déclarés, risque accepté, sonde du jour), empreinte des commandes, relais par PID (programme épinglé, port, `--amont` et `--modeles-permis` pour Astra, `--modele` pour Carbon), état neuf.

## 9. Lancement de la course (plafond d'arrêt 90 USD)

La variable `RR_ANTHROPIC_API_KEY_RIGAUD` présente dans l'environnement du lanceur (il la teste par son nom, ne lit jamais sa valeur et la retire de l'environnement de l'orchestrateur) :

```
cd /home/user/controle-ia-travail && git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
cd /home/user/controle-ia-travail && GO_ID=GO-2026-11-18-20 /usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v3.py
```
Le lanceur exige, dans l'ordre : aucune course déjà lancée (v1, v2 ou v3), pièce de départ, GO `GO-2026-11-18-20` (registre lu au commit de `main`), préenregistrement `0d51e0b3…`, pièces épinglées, **additif `7c76eba0…`**, **contre-lecture du § 3**, matière, **rapport d'épreuve v3 « réussie » du jour** (verdict recalculé), déclaration du § 8, relevés des §§ 5 et 6, relais, orchestrateur, bac à sable, vérification de l'orchestrateur, porte à blanc. Sortie hors dépôt : `/home/user/sorties-course-auto-conception-v3/«id»/` ; dossier du run au dépôt : `runs/«id»-course-auto-conception-v3/`. Codes : **0** fini ; **2** refus ou arrêt (motif sur la sortie d'erreur) ; **3** alerte de crédit avant le départ (fichier scellé pour la mère) ; **4** cumul au-dessus de 90 USD ; **5** arrêt au premier refus pour crédit d'un relais dispensé. Carbon par lot : jusqu'à ≈ 30 minutes par appel, plusieurs heures au pire pour ses onze cases.

## 10. Après

Lire `/relais/etat` de chaque relais (8787, 8788, 8790, 8792 : dépense, appels), les arrêter **par PID** (`kill -INT «PID»`, R10), consigner chaque arrêt et la dépense ; verser `runs/«id»-course-auto-conception-v3/` (manifestes de départ et de fin, acte de gel, configuration, lots, registre dérivé, alertes éventuelles) ; **ne lire aucune carte** : la lecture est à la mère. Code 2 avec un nœud C13 (étape non mesurée) : issue rapportée, tentative consommée, aucune relance sans version neuve et mot de la mère. Code 3, 4 ou 5 : alerte scellée transmise à la mère, qui prévient Lazar.

## 11. Essai à blanc et épreuve hors ligne (déjà joués par l'auteur, à rejouer si l'on veut)

```
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md > «DOSSIER_NEUF»-matiere-premiere-v3.md
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v3.py --a-blanc «DOSSIER_NEUF»/a-blanc
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/epreuve_temoins_auto_conception_v3.py --hors-ligne «DOSSIER_NEUF»/epreuve-hors-ligne --matiere «DOSSIER_NEUF»-matiere-premiere-v3.md
```
Résultats versés : `course-v2/essai-a-blanc-v2c/` (moteur simulé, code 0, 88 cartes à passeport, étapes conformes, additif cité par l'acte de gel et le manifeste ; épreuve hors ligne v3 : « témoins éprouvés hors ligne », 0 juge au hasard réussi sur 2 000).

## 12. Réserves

- Argon et Carbon partagent la variable `GEMINI_API_KEY` : le relevé l'écrit une fois, sous dispense ; le lanceur confronte chaque relais à sa part séparément et ne les additionne pas (sans effet sous dispense, solde illisible ; à dire à la mère).
- La garde neuve de l'épreuve rejoue `construire_options` (fonction pure) sur chaque dossier : elle prouve que la liste interdite et le dossier sont cohérents, pas que le bac à sable du kit l'applique ; cette dernière garde reste celle de l'orchestrateur (bac exigé, échec dur s'il manque).
- Les noms des dossiers d'appel de l'épreuve portent l'étiquette du rôle et l'identifiant du témoin (`…/appels/juge-opus/t03`), comme en v2 (la course, elle, nomme ses sessions par un identifiant opaque) : inchangé, dit ici.
- La sonde d'Astra n'est valable que le 18 novembre 2026.
