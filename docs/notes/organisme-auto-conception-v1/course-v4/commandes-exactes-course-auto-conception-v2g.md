# Commandes exactes — course d'auto-conception de l'organisme d'idéation, v2g : Carbon synchrone sans troncature, plafonds relevés, clé Minuit (pour la session d'exécution)

Écrites le 19 novembre 2026 par le développeur unique de la version (modèle L′). Pièce **neuve** (R12) : les commandes v2 à v2f restent en place, archivées ; **ce texte se suffit à lui-même**. Fondement : mots de Lazar « go (a) » (Carbon par la commande synchrone d'Argon, éprouvé d'abord par un appel réel sur le plus grand lot, puis course), « augmente le plafond », « enlève la troncature pour Carbon », « Clé Minuit (Recommandé) » ; mère R-3613, R-3616 ; additif v2g. **Rien n'a été lancé par l'auteur** : moteur simulé, relais factices, faux amont local, aucun appel réel. Aucune valeur de clé n'est écrite nulle part (noms de variables seulement).

Notations : `«D»` = le dossier hors dépôt neuf **`/home/user/execution-auto-conception-v2g`** ; `«J»` = le jour UTC du départ (`date -u +%F`), **le même pour les deux sondes, l'épreuve, les relevés et le lancement** (le lanceur exige des pièces « du jour ») ; `«GO_COURSE»`, `«GO_EPREUVE»`, `«GO_SONDE_C»` = les trois lignes neuves (§ 2) ; `«PID_…»` = les PID lus dans les consoles des relais. Clé Claude : **`RR_ANTHROPIC_API_KEY_MINUIT`** (mot de Lazar ; Rigaud refusée par le lanceur v7) ; Argon et Carbon : **`GEMINI_API_KEY`** ; Astra : **`OPENAI_API_KEY`**. Modèles : Carbon `gemini-4-carbon`, Astra `gpt-6-astra`, Argon `gemini-4-argon`, Claude `claude-opus-5-5` et `claude-fable-5-1`. Orchestrateur : `/home/user/ideation-organism` au commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, propre. Note : le relais Claude (`relais_reel.py`) n'accepte que le jeton factice « relais-local-sans-cle » (utile pour toute sonde directe sur 8787) ; la clé vit dans son seul environnement.

## 0. Ce qui change (et rien d'autre)

La course v6 (`runs/20261119-001004-course-auto-conception-v6/`, manifeste de fin `3ed8cc61…`) est close : code 2, étape « proposition » non mesurée (technique), **42,360849 USD** ; cause (journal v62, PO-178) : en mode lot, le budget de pensée de Carbon n'est pas tenu (pensée 32 765, réponse 3 jetons). Cette version :

- passe **Carbon par la commande synchrone d'Argon** : déclaration exactement `["bash", "/home/user/controle-ia-travail/rapports/fille-ideation-1-v1/appel-carbon-synchrone-v1.sh"]` (enveloppe neuve, aucun argument, réglage figé) → `commande_argon_v3d.py` (épinglée, inchangée) → relais **`relais_gemini_v2.py`** dédié, port **8792**, `--modele gemini-4-carbon` ; la commande par lot et le relais Gemini v4 ne servent plus ;
- **sans troncature** : sortie maximale 65 536 (le maximum de la commande), budget de pensée non fixé (`--sans-config-pensee`), provision de la garde 65 536 ; pire cas d'un appel sur la plus grande entrée **5,817437 USD ≤ 6** (au compte de la commande ; 6,04 USD nécessaires à la borne prudente) ;
- joue d'abord **une sonde réelle de Carbon** (§ 8) : un appel par cette chaîne sur le plus grand lot, ≤ 6 USD, rapport de champs techniques seulement ; le lanceur v7 l'exige « ok » (code 0, STOP, non vide, non tronquée) ;
- **relève les plafonds** (configuration v3) : 6 USD par appel des proposeurs, **120 USD** d'arrêt (ligne de GO de la course à 120 USD exactement), relais Claude 120 ;
- prend la **clé Claude Minuit** (crédit déclaré 200 USD, réserves vides) ;
- admet les courses **v4 et v6 closes** sur mot de reprise ; lignes `GO-2026-11-18-20`, `-21`, `-36`, `-67`, `-68` consommées ; épreuve des témoins **v7** du jour.

**Ordre d'exécution** : § 1 (empreintes), § 2 (lignes de GO), § 4 (contre-lecture), § 3 (sonde d'Astra), § 8 (sonde de Carbon), § 5 (pièce de départ, qui nomme les deux sondes), § 6 (bac), § 7 (épreuve), § 9 et § 10 (relevés), § 11 à § 13 (relais, déclaration, lancement), § 14, § 15.

## 1. Empreintes (à vérifier avant tout)

| pièce | sha256 |
|---|---|
| `scripts/lancer_course_auto_conception_v7.py` (lanceur v7, à citer en entier par la contre-lecture) | `b10b2d18efaa6ce4936cbc98d081fee37d3df220afc771158dc23d6a9a1d901d` |
| `course-v4/additif-preenregistrement-course-auto-conception-v2g.md` (épinglé par le lanceur v7, à citer en entier par la contre-lecture) | `2b0d3e7a553c60c013f81c37f6150c27285e80377219920495fba8a8816bb867` |
| `scripts/epreuve_temoins_auto_conception_v7.py` (épinglé) | `0f980b18271f2337dd2ace6663662eb13641cee1da943dd2de23a417cbca44b3` |
| `scripts/sonde_carbon_synchrone_v1.py` (épinglé) | `77e313689641a062efc97590ff1030e966d51c53c319a53f553f771b5b2ff447` |
| `rapports/fille-ideation-1-v1/appel-carbon-synchrone-v1.sh` (épinglée) | `b380be0b83ed31317141933d501518eb15d9f9318ceb77923d57dbcbf614c0a2` |
| `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py` (épinglée, inchangée) | `46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46` |
| `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py` (relais d'Argon et de Carbon, inchangé) | `2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb` |
| `course-v4/configuration-course-auto-conception-v3.json` (épinglée) | `8e54a61c4d5f7ea4ac04c89db52d10646bfdef9d5174ceb5342774781e0e2eb9` |
| `course-v4/piece-de-depart-gabarit-auto-conception-v2g.json` (gabarit, jamais lu par le lanceur) | `6af1df039f34f9f88bdcc3b2ece324a56a358c95b47b703a520e8c32fbd63989` |
| `course-v4/calcul-devis-course-auto-conception-v2g.json` (chiffres du devis) | `b01678ad8db9790fcef5f0ae5debb542f0ee5c36d772c5f8953f85bc1a821be5` |
| `tests/test_lancer_course_auto_conception_v7.py` (227 essais) | `3de14cd308a9570d28e2176d528082766e1f3d003a210475ae79c39f29af773c` |
| `tests/test_epreuve_temoins_auto_conception_v7.py` (89 essais) | `b3f5d53da7a5a0777618ca2f7376576cdf5c32c2abeb41d8a343a2153896b723` |
| `tests/test_sonde_carbon_synchrone_v1.py` (37 essais) | `c2b92d13d9026c937d7166eddcafff0babf4e138e8d65cc6e5f272f45647c3f3` |
| `course-v2/preenregistrement-course-auto-conception-v2.md` (inchangé) | `0d51e0b3f51dd731351589187c124b7ee1a6237494aa0274825b19085c6763c6` |
| `runs/20261118-171908-course-auto-conception-v4/manifeste-lanceur-fin.json` (course close) | `2625234c786a7fc50c926325c1a9efc8a8e9b74146a59205bf8a31c6e2c5fd7f` |
| `runs/20261119-001004-course-auto-conception-v6/manifeste-lanceur-fin.json` (course close) | `3ed8cc610b33b8755488fc1a77bf889479b9e9b6c6fa7c5190200e8831183eaa` |
| commande d'Astra (sur `main`) `docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py` | `986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71` |
| relais Claude `/home/user/ideation-organism/orchestrator/pole/relais_reel.py` | `1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153` |
| relais compatible OpenAI d'Astra `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py` | `67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e` |
| matière servie (sur `main`) `docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md` | `11f4b69ba42147c428090e4805948a708d0ed266da0c0cd07f194723eaba742d` |

```
cd /home/user/controle-ia-travail && git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
cd /home/user/controle-ia-travail && for f in scripts/lancer_course_auto_conception_v7.py scripts/epreuve_temoins_auto_conception_v7.py scripts/sonde_carbon_synchrone_v1.py rapports/fille-ideation-1-v1/appel-carbon-synchrone-v1.sh docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py docs/notes/organisme-auto-conception-v1/course-v4/additif-preenregistrement-course-auto-conception-v2g.md docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v3.json docs/notes/organisme-auto-conception-v1/course-v4/piece-de-depart-gabarit-auto-conception-v2g.json docs/notes/organisme-auto-conception-v1/course-v4/calcul-devis-course-auto-conception-v2g.json docs/notes/organisme-auto-conception-v1/course-v2/preenregistrement-course-auto-conception-v2.md runs/20261118-171908-course-auto-conception-v4/manifeste-lanceur-fin.json runs/20261119-001004-course-auto-conception-v6/manifeste-lanceur-fin.json tests/test_lancer_course_auto_conception_v7.py tests/test_epreuve_temoins_auto_conception_v7.py tests/test_sonde_carbon_synchrone_v1.py; do (cd "$(dirname "$f")" && sha256sum -c "$(basename "$f").sha256"); done
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md | sha256sum
sha256sum /home/user/ideation-organism/orchestrator/pole/relais_reel.py && git -C /home/user/ideation-organism rev-parse HEAD && git -C /home/user/ideation-organism status --porcelain --untracked-files=all --ignored=matching
cd /home/user/controle-ia-travail && PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B -m pytest -q -rs -p no:cacheprovider tests/test_lancer_course_auto_conception_v7.py tests/test_epreuve_temoins_auto_conception_v7.py tests/test_sonde_carbon_synchrone_v1.py
```
Attendu : toutes les empreintes « OK » ; matière `11f4b69b…` ; relais Claude `1b90b020…` ; orchestrateur `a41b7b50…`, statut vide ; **227 + 89 + 37 = 353 essais passés** (l'essai `test_reel_refuse_sans_piece_de_depart_neuve_avant_tout` se dit « sauté » une fois la pièce v2g écrite : attendu). Aucun essai ne touche le port 8792 ni un fournisseur.

## 2. Ce que la mère fait avant tout (nœuds : rien ne part sans)

1. **Trois lignes de GO neuves**, au registre `registres/go.md` sur `main`, accordées par Lazar, type « calcul », période couvrant `«J»` :
   - `«GO_COURSE»` : plafond **exactement `120 USD`** (l'orchestrateur exige de la ligne le montant du plafond d'arrêt de la configuration v3 à l'identique ; une ligne de 90 USD est refusée avant tout appel ; estimation **≈ 55,94 USD**, devis v2g), périmètre qui contient **« auto-conception »** et **« tentative neuve »** ;
   - `«GO_EPREUVE»` : plafond **`5 USD`**, périmètre qui contient **« témoins »** ;
   - `«GO_SONDE_C»` : plafond **exactement `6 USD`**, périmètre qui contient **« sonde »** et **« Carbon »** (le programme de sonde le relit).
   Jamais `GO-2026-11-18-20`, `-21`, `-36`, `-67` ni `-68` (consommées : le lanceur v7 les refuse).
2. **Clé Claude Minuit** : `RR_ANTHROPIC_API_KEY_MINUIT`, vérifiée active le 19 novembre 2026 à 06:37:04Z (appel minimal, HTTP 200, 0,000108 USD ; R-3613 → choix (a)) ; crédit déclaré 200 USD (R-3228), dépense antérieure inscrite 0 (R-3616), réserves vides. Reste net estimé au départ ≈ 199 USD > 120 (part au pire) : départ admis. Réserve écrite de la mère : variable commune à l'environnement par défaut, usage non inscrit d'une autre session non exclu, le relevé de facturation de Lazar fait foi.
3. **Contre-lecture** (§ 4) scellée « Scellable. ».

## 3. Sonde d'Astra du jour (≤ 0,05 USD, signalée ; avant tout autre relais)

Relais **jeté**, port 8793 (jamais 8787 à 8792) :
```
mkdir «D» «D»/maison «D»/sonde-astra «D»/sonde-carbon
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py > «D»/commande_astra_v1.py && echo "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71  «D»/commande_astra_v1.py" | sha256sum -c -
cd «D»/sonde-astra && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/sonde-astra/console-astra-sonde.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8793 --modeles-permis gpt-6-astra --plafond-usd 0.05 --reserve-par-appel 0.01 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 1 --journal «D»/sonde-astra/journal-relais-astra-sonde.jsonl
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/sonde_astra_courses_v1.py --commande «D»/commande_astra_v1.py --url-relais-jete http://127.0.0.1:8793 --pid-relais-jete «PID_DU_RELAIS_JETE_ASTRA» --sortie docs/notes/organisme-auto-conception-v1/course-v4/sonde-astra-commune-«J»-v1.json --sortie-v2 docs/notes/organisme-auto-conception-v1/course-v4/sonde-astra-v2-«J»-auto-conception-v2g.json
```
Codes : **0** réussie ; **1** non réussie, rapport écrit ; **2** refus avant tout appel. Puis `curl -s --noproxy '*' http://127.0.0.1:8793/relais/etat` (1 appel, dépense ≤ 0,05), arrêt **par PID** (`kill -INT «PID_DU_RELAIS_JETE_ASTRA»`, R10), consigner l'arrêt et **signaler la dépense**. Si la sonde n'a pas réussi : Astra n'est pas déclarée (décision de la mère, la composition changerait : nœud).

## 4. Contre-lecture (modèle K) — avant l'épreuve et la sonde de Carbon

Par un contre-lecteur neuf du modèle K, qui n'a écrit ni l'additif v2g, ni le lanceur v7, ni le programme d'épreuve v7, ni la sonde de Carbon, ni l'enveloppe (R2). Fichiers à lui donner : l'additif v2g et les additifs v2c à v2f, le préenregistrement v2, `scripts/lancer_course_auto_conception_v7.py` et la v6, `scripts/epreuve_temoins_auto_conception_v7.py` et la v6, `scripts/sonde_carbon_synchrone_v1.py`, `rapports/fille-ideation-1-v1/appel-carbon-synchrone-v1.sh`, `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py` et `relais_gemini_v2.py`, les trois fichiers d'essais neufs, la configuration v3 et la v2, le journal provisoire v62 (`registres-provisoires/compte-organisme-2026-11-19-v62.md`), les manifestes de fin des courses v4 et v6, le gabarit v2g, le devis v2g et son calcul, ces commandes, le rapport du développeur (`course-v4/rapport-developpeur-carbon-synchrone-v2g.md`) et, dans `/home/user/ideation-organism/orchestrator`, `pole/adaptateurs.py` (`AdaptateurCommandeExterne`, `modele_conforme`, `DELAI_COMMANDE_S`), `pole/adaptateurs_v56.py`, `pole/course2_v54.py` (`_proposer`), `pole/budget_v56.py`, `pole/configuration_v54.py` (`montant_requis`). Rapport écrit et scellé à `docs/notes/organisme-auto-conception-v1/course-v4/contre-lecture-tentative-carbon-synchrone-v2g-auto-conception.md` : il cite **en entier** `2b0d3e7a553c60c013f81c37f6150c27285e80377219920495fba8a8816bb867` (additif v2g) et `b10b2d18efaa6ce4936cbc98d081fee37d3df220afc771158dc23d6a9a1d901d` (lanceur v7), se dit du modèle K, la première ligne sous « ## Verdict » est exactement « Scellable. », et il ne dit nulle part n'avoir pas relu. Une correction demandée donne des versions neuves (R12) : ces commandes ne valent plus.

## 5. Pièce de départ v2g (la mère)

Recopier le gabarit sous le nom lu par le lanceur, remplir **chaque** « À REMPLIR » (outil d'écriture de fichiers : `go_course`, `go_epreuve`, `tentative_neuve.mot_de_reprise` = `«GO_COURSE»` ; `especes_optionnelles.astra.sonde_du_jour` et `sonde_du_jour_rapport` = `docs/notes/organisme-auto-conception-v1/course-v4/sonde-astra-commune-«J»-v1.json` ; `especes_optionnelles.carbon.sonde_du_jour` et `sonde_du_jour_rapport` = `docs/notes/organisme-auto-conception-v1/course-v4/sonde-carbon-synchrone-«J»-v1.json` (§ 8) ; `ecrit_le` ; `statut`). Le gabarit porte déjà la clé Minuit, le mot de Lazar (`cle_claude_mot_de_lazar`), le crédit 200, des réserves vides, la course v6 close et les empreintes de l'enveloppe et de la commande d'Argon. Puis sceller :
```
cd /home/user/controle-ia-travail && cp --update=none docs/notes/organisme-auto-conception-v1/course-v4/piece-de-depart-gabarit-auto-conception-v2g.json docs/notes/organisme-auto-conception-v1/course-v4/piece-de-depart-auto-conception-v2g.json
cd /home/user/controle-ia-travail && grep -c "À REMPLIR" docs/notes/organisme-auto-conception-v1/course-v4/piece-de-depart-auto-conception-v2g.json
cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-auto-conception-v1/course-v4/piece-de-depart-auto-conception-v2g.json
```
(le `grep -c` doit rendre **0** avant le scellement ; la pièce n'est scellée qu'une fois les deux sondes du jour réussies, puisqu'elle les nomme).

## 6. Sonde du bac à sable (commande de l'orchestrateur), avant l'épreuve

```
cd /home/user/ideation-organism/orchestrator && env -i PATH=/usr/local/bin:/usr/bin:/bin LANG=C.UTF-8 /usr/local/bin/python3 -I -B -c "import json, sys
sys.path.insert(0, sys.argv[1])
from pole.adaptateurs import etat_bac_a_sable_detaille
print(json.dumps(etat_bac_a_sable_detaille()))" /home/user/ideation-organism/orchestrator
```
Attendu : `{"actif": true, "proc_neuf": true, …}`.

## 7. Épreuve réelle des témoins du jour (programme v7 ; 5 USD ; 33 appels)

Aucun relais ne doit tourner (ports 8787 à 8793) : `pgrep -af "relais_reel.py|relais_gemini|relais_kimi"` ne rend rien (sinon arrêt **par PID**, `kill -INT «PID»`, R10, consigné). Relais **propres à l'épreuve** :
```
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-claude-epreuve.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_MINUIT -- /usr/bin/python3 -I -B /home/user/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_MINUIT --port 8787 --plafond-usd 5 --modeles-permis claude-fable-5-1,claude-opus-5-5 --journal «D»/journal-relais-claude-epreuve.jsonl
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-gemini-epreuve.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle GEMINI_API_KEY --port 8788 --max-appels 24 --modele gemini-4-argon --journal «D»/journal-relais-gemini-epreuve.jsonl
```
Vérifier : `tr '\0' ' ' < /proc/«PID»/cmdline` pour chaque relais ; `curl -s --noproxy '*' http://127.0.0.1:8787/relais/etat` (0 appel, plafond 5) ; `curl -s --noproxy '*' http://127.0.0.1:8788/relais/etat` (0 appel, `max_appels` 24, `variable_cle_encore_presente` faux).

Déclaration de l'épreuve, **chemin neuf**, écrite avec l'outil d'écriture de fichiers puis scellée : `docs/notes/organisme-auto-conception-v1/course-v4/declaration-relais-epreuve-temoins-auto-conception-v7.json`
```json
{"version": "declaration-relais-epreuve-temoins-auto-conception-v7", "fournisseurs": {
 "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:8787", "nom_cle": "RR_ANTHROPIC_API_KEY_MINUIT", "pid_relais": «PID_CLAUDE_EPREUVE»,
            "porte_plafond": {"type": "commande", "delai_s": 30, "commande": ["/usr/local/bin/python3", "-I", "-B",
              "/home/user/controle-ia-travail/scripts/porte_plafond_relais_v1.py", "--url", "http://127.0.0.1:8787",
              "--modeles-permis", "claude-fable-5-1,claude-opus-5-5", "--plafond-ligne", "5"]}},
 "argon": {"type": "commande_externe", "commande": ["bash", "/home/user/controle-ia-travail/rapports/fille-ideation-1-v1/appel-argon-v5.sh"],
           "nom_cle": "GEMINI_API_KEY", "pid_relais": «PID_GEMINI_EPREUVE», "url_etat_relais": "http://127.0.0.1:8788",
           "porte_plafond": {"type": "environnement"}}}}
```
```
cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-auto-conception-v1/course-v4/declaration-relais-epreuve-temoins-auto-conception-v7.json
cd /home/user/controle-ia-travail && git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
cd /home/user/controle-ia-travail && env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=«D»/maison LANG=C.UTF-8 /usr/local/bin/python3 -I -B scripts/epreuve_temoins_auto_conception_v7.py --reel > «D»/epreuve-reelle-v7.stdout.txt 2> «D»/epreuve-reelle-v7.stderr.txt; echo "code $?"
```
**La pièce de départ v2g doit être scellée avant** (l'épreuve la relit : lignes, mot de reprise à 120 USD, clé Minuit) — elle nomme les deux sondes : jouer donc les sondes (§ 3 et § 8) avant l'épreuve. Codes : 0 rapport écrit (lire le verdict) ; 2 refus. Sortie : `course-v4/epreuve-temoins-reelle-auto-conception-v7.json`. **Verdict autre que « réussie » : arrêt, aucune course, rapport à la mère.** Puis lire `depense_usd` sur `http://127.0.0.1:8787/relais/etat` (dépense Claude de l'épreuve, pour le § 10), arrêter les deux relais **par PID**, consigner, verser la déclaration et les journaux (scellés) dans `course-v4/epreuve-reelle-v7-«J»-v1/`.

## 8. Sonde réelle de Carbon (≤ 6 USD, sous `«GO_SONDE_C»` ; avant la course, après la contre-lecture)

Un appel par la chaîne de la course (enveloppe → commande d'Argon → relais Gemini v2) sur **la plus grande entrée servie** (lot 1, 136 265 octets). Relais **jeté** sur le port **8792** (l'adresse que l'enveloppe fige ; aucun autre relais ne doit y tourner), borne **2** (countTokens puis generateContent) :
```
cd «D»/sonde-carbon && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/sonde-carbon/console-carbon-sonde.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle GEMINI_API_KEY --port 8792 --max-appels 2 --modele gemini-4-carbon --journal «D»/sonde-carbon/journal-relais-carbon-sonde.jsonl
tr '\0' ' ' < /proc/«PID_DU_RELAIS_JETE_CARBON»/cmdline; curl -s --noproxy '*' http://127.0.0.1:8792/relais/etat
cd /home/user/controle-ia-travail && git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
cd /home/user/controle-ia-travail && env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=«D»/maison LANG=C.UTF-8 /usr/local/bin/python3 -I -B scripts/sonde_carbon_synchrone_v1.py --go «GO_SONDE_C» --pid-relais «PID_DU_RELAIS_JETE_CARBON» --sortie docs/notes/organisme-auto-conception-v1/course-v4/sonde-carbon-synchrone-«J»-v1.json > «D»/sonde-carbon/sonde.stdout.txt 2> «D»/sonde-carbon/sonde.stderr.txt; echo "code $?"
```
Codes : **0** réussie ; **1** non réussie, rapport écrit ; **2** refus avant tout appel (rien d'écrit ni d'envoyé : clé dans l'environnement, rapport existant, pièces d'une autre empreinte, ligne de GO absente ou ≠ 6 USD ou sans « sonde » et « Carbon », réglage de l'enveloppe autre, pire cas > 6 USD ou sortie réduite, relais jeté non conforme ou non neuf). L'appel peut durer jusqu'à 1 740 s. La sortie standard dit seulement : ok, code, fin, modèle servi, coût, pensée et sortie en jetons, durée, motif (jamais le texte). Puis `curl -s --noproxy '*' http://127.0.0.1:8792/relais/etat` (2 appels, 0 refus), arrêt **par PID** (`kill -INT «PID_DU_RELAIS_JETE_CARBON»`, R10), consigner l'arrêt et **signaler la dépense**. Vérifier :
```
cd /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/course-v4 && sha256sum -c sonde-carbon-synchrone-«J»-v1.json.sha256 && /usr/local/bin/python3 -I -c "import json,sys;o=json.load(open('sonde-carbon-synchrone-«J»-v1.json'));c=o['commande'];print(o['ok'],o['jour'],c['code'],c['fin'],c['non_tronquee'],c['max_sortie_jetons'],c['modele_servi'],c['cout_usd'],c['pensees_jetons'],c.get('candidats_jetons'),c['lecture_pensees'],c['entree_jetons_comptee']);sys.exit(0 if o['ok'] is True and o['jour']=='«J»' else 1)"
```
Attendu : `True «J» 0 STOP True 65536 gemini-4-carbon …`. **Si la sonde n'a pas réussi : rapport à la mère, aucune course** (ne pas déclarer Carbon change la composition : décision, nœud). Lire aussi `lecture_pensees` (`hors_max_sortie` : la pensée n'est pas comptée dans la sortie — réserve 1 de l'additif) et `entree_jetons_comptee` (au-dessus de 43 367, la garde réduirait la sortie de la course : la sonde l'aurait déjà dit, `non_tronquee` faux).

## 9. Relevé des prix Claude du jour

Lire **https://platform.claude.com/docs/en/about-claude/pricing** (Claude Opus 5.5 et Claude Fable 5.1). Barème attendu : 4 / 20 et 10 / 50 USD ; tout autre prix : **arrêt, nouveau devis**. Écrire puis sceller `docs/notes/organisme-auto-conception-v1/course-v4/releve-prix-claude-course-auto-conception-v2g.json` :
```json
{"releve_utc": "«date -u +%FT%TZ»", "source": "https://platform.claude.com/docs/en/about-claude/pricing, lue le «date -u +%FT%TZ» : Claude Opus 5.5 4 / 20 USD, Claude Fable 5.1 10 / 50 USD par million de jetons (entrée / sortie)", "prix": {"espece_claude_1": {"entree": 4.0, "sortie": 20.0}, "espece_claude_2": {"entree": 10.0, "sortie": 50.0}}}
```
```
cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-auto-conception-v1/course-v4/releve-prix-claude-course-auto-conception-v2g.json
```

## 10. Relevé des crédits du jour (après l'épreuve)

Écrire puis sceller `docs/notes/organisme-auto-conception-v1/course-v4/releve-credits-avant-course-auto-conception-v2g.json`. Clé Minuit non lisible : dépense antérieure = **0,000108 USD** (0 inscrite, R-3616, plus l'appel de vérification de 06:37:04Z) **+ la dépense Claude de l'épreuve v7** (§ 7) ; aucune réserve :
```json
{"releve_utc": "«date -u +%FT%TZ»",
 "cles": {"RR_ANTHROPIC_API_KEY_MINUIT": {"non_lisible": true, "motif": "solde illisible ; dépense antérieure : 0 inscrite (R-3616) + 0,000108 (vérification du 19 novembre, 06:37:04Z) + la dépense Claude de l'épreuve v7 lue sur le relais 8787 ; crédit déclaré 200 USD (R-3228)", "depense_anterieure_usd": «0.000108 + dépense Claude de l'épreuve v7»},
          "GEMINI_API_KEY": {"non_lisible": true, "motif": "solde illisible (R-3222)"},
          "OPENAI_API_KEY": {"non_lisible": true, "motif": "solde illisible"}},
 "dispense": {"par": "mère", "reference": "R-3237", "cles": ["GEMINI_API_KEY", "OPENAI_API_KEY"]}}
```
```
cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-auto-conception-v1/course-v4/releve-credits-avant-course-auto-conception-v2g.json
```
Compté par le lanceur : 200 − dépense antérieure − 0 ; **code 3** (alerte scellée) si ce reste net est ≤ 120 USD ou sous 40 USD.

## 11. Relais de la course

Les relais de l'épreuve et les deux relais jetés sont arrêtés. Depuis `«D»` :
```
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-claude-course.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_MINUIT -- /usr/bin/python3 -I -B /home/user/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_MINUIT --port 8787 --plafond-usd 120 --modeles-permis claude-fable-5-1,claude-opus-5-5 --journal «D»/journal-relais-claude-course.jsonl
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-gemini-course.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle GEMINI_API_KEY --port 8788 --max-appels 464 --modele gemini-4-argon --journal «D»/journal-relais-gemini-course.jsonl
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-astra.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8790 --modeles-permis gpt-6-astra --plafond-usd 67 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 60 --delai-amont-s 3400 --journal «D»/journal-relais-astra.jsonl
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-carbon.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle GEMINI_API_KEY --port 8792 --max-appels 60 --modele gemini-4-carbon --journal «D»/journal-relais-carbon.jsonl
```
(La commande d'Astra est déjà dans `«D»`, § 3.) Bornes : Claude 120 (= plafond d'arrêt, exigé à l'identique) ; Argon **464** = 2 × 231 + 2 ; Carbon `--max-appels 60` ≥ 24 = 2 × 11 + 2 ; Astra plafond 67 ≥ 11 × 6 (plafond de session relevé) et 60 appels ≥ 11. Vérifier chaque relais par PID (`tr '\0' ' ' < /proc/«PID»/cmdline`) et `curl -s --noproxy '*' http://127.0.0.1:«PORT»/relais/etat` sur 8787, 8788, 8790, 8792 : **0 appel** partout, plafond 120 (Claude), `max_appels` 464 (Argon) et 60 (Carbon), variable de clé effacée (Gemini). Kimi : aucun relais.

## 12. Déclaration des relais de la course (chemin neuf, v7)

Écrire (outil d'écriture de fichiers), puis sceller, `docs/notes/organisme-auto-conception-v1/course-v4/declaration-relais-course-auto-conception-v7.json` :
```json
{"version": "declaration-relais-course-auto-conception-v7", "fournisseurs": {
 "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:8787", "nom_cle": "RR_ANTHROPIC_API_KEY_MINUIT", "pid_relais": «PID_CLAUDE_COURSE»,
            "porte_plafond": {"type": "commande", "delai_s": 30, "commande": ["/usr/local/bin/python3", "-I", "-B",
              "/home/user/controle-ia-travail/scripts/porte_plafond_relais_v1.py", "--url", "http://127.0.0.1:8787",
              "--modeles-permis", "claude-fable-5-1,claude-opus-5-5", "--plafond-ligne", "120"]}},
 "argon": {"type": "commande_externe", "commande": ["bash", "/home/user/controle-ia-travail/rapports/fille-ideation-1-v1/appel-argon-v5.sh"],
           "nom_cle": "GEMINI_API_KEY", "pid_relais": «PID_GEMINI_COURSE», "url_etat_relais": "http://127.0.0.1:8788",
           "porte_plafond": {"type": "environnement"}},
 "astra": {"type": "commande_externe", "commande": ["/usr/local/bin/python3", "-I", "-B", "/home/user/execution-auto-conception-v2g/commande_astra_v1.py", "--url-relais", "http://127.0.0.1:8790",
           "--modele", "gpt-6-astra", "--prix-entree", "10", "--prix-sortie", "50"], "modele_propose": "gpt-6-astra", "nom_cle": "OPENAI_API_KEY",
           "pid_relais": «PID_ASTRA», "url_etat_relais": "http://127.0.0.1:8790", "porte_plafond": {"type": "environnement"}},
 "carbon": {"type": "commande_externe", "commande": ["bash", "/home/user/controle-ia-travail/rapports/fille-ideation-1-v1/appel-carbon-synchrone-v1.sh"],
            "modele_propose": "gemini-4-carbon", "nom_cle": "GEMINI_API_KEY", "pid_relais": «PID_CARBON»,
            "url_etat_relais": "http://127.0.0.1:8792", "porte_plafond": {"type": "environnement"}}}}
```
```
cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-auto-conception-v1/course-v4/declaration-relais-course-auto-conception-v7.json
```
La commande de Carbon est **exactement** `["bash", "<enveloppe>"]` : aucun argument (le lanceur refuse tout ajout ; l'enveloppe aussi, code 2).

## 13. Lancement de la course (plafond d'arrêt 120 USD), **détaché de l'outil**, le jour `«J»` avant minuit UTC

Seulement si : épreuve v7 « réussie » ; contre-lecture « Scellable. » ; pièce, deux sondes et deux relevés du jour scellés. La variable `RR_ANTHROPIC_API_KEY_MINUIT` présente dans l'environnement du lanceur (testée par son nom, jamais lue, retirée de l'environnement de l'orchestrateur). Lancement **détaché** par `setsid nohup` (une commande d'arrière-plan de l'outil serait coupée à 2 h ; un appel de Carbon peut durer jusqu'à ≈ 29 minutes) :
```
cd /home/user/controle-ia-travail && git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
cd /home/user/controle-ia-travail && GO_ID=«GO_COURSE» setsid nohup /usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v7.py > «D»/lanceur-course-v7.stdout.txt 2> «D»/lanceur-course-v7.stderr.txt < /dev/null &
pgrep -f "scripts/lancer_course_auto_conception_v7.py"
```
**Relever le PID par `pgrep -f`** (`$!` peut donner celui de `setsid`) ; un seul PID attendu ; vérifier `tr '\0' ' ' < /proc/«PID_LANCEUR»/cmdline` (doit nommer `lancer_course_auto_conception_v7.py`). La première ligne de `«D»/lanceur-course-v7.stdout.txt` est le manifeste de départ ; un refus avant le départ s'écrit sur `«D»/lanceur-course-v7.stderr.txt` (`{"refus": …}`, code 2 ; `{"alerte_credit": …}`, code 3) et le processus se termine.

Le lanceur exige, dans l'ordre : pièce de départ v2g (clé Minuit sur le mot de Lazar ; aucune ligne consommée ; mot de reprise ; course v6 close citée ; sondes nommées) ; « une seule course » (courses v4 et v6 closes admises, manifestes de fin `2625234c…` et `3ed8cc61…` scellés ; aucune v7 déjà lancée) ; clé présente ; `«GO_COURSE»` au registre de `main` (**120 USD**, « auto-conception », « tentative neuve ») ; préenregistrement, pièces, additif v2g, contre-lecture ; matière ; configuration v3 (6 et 120) ; épreuve v7 « réussie » du jour ; sonde d'Astra du jour ; déclaration (composition tenue ; **Carbon** : commande exactement l'enveloppe, enveloppe et commande d'Argon épinglées par la pièce, réglage lu par l'analyseur de la commande, durée au pire 1 740 s ≤ 1 770 s, sortie maximale 65 536 retenue, pire cas ≤ 6 USD) ; **sonde de Carbon du jour** (ok, non tronquée, sur la plus grande entrée, au réglage de la course) ; relevé des crédits ; relais (Argon ≥ 464 ; Carbon : relais Gemini v2, ≥ 24 appels, amont de Google, variable effacée) ; relevé des prix ; orchestrateur ; bac ; vérification de l'orchestrateur (montant requis 120) ; porte à blanc. Codes : **0** fini ; **2** refus ou arrêt (nœud C13 compris) ; **3** alerte de crédit ; **4** cumul au-dessus de 120 USD ; **5** arrêt au premier refus pour crédit d'un relais dispensé.

## 14. Surveillance (sans rien lire des cartes)

`kill -0 «PID_LANCEUR» && echo vivant` ; `cat «D»/lanceur-course-v7.stdout.txt` ; états des relais (`curl -s --noproxy '*' http://127.0.0.1:«PORT»/relais/etat` : appels, dépense, refus). Ne jamais arrêter par motif de ligne de commande (R10) : par PID seulement, sur décision (le lanceur relaie SIGTERM à l'orchestrateur et écrit son manifeste de fin).

## 15. Après

Lire `/relais/etat` de chaque relais (8787, 8788, 8790, 8792 : dépense, appels), les arrêter **par PID** (`kill -INT «PID»`), consigner chaque arrêt et la dépense ; verser `runs/«id»-course-auto-conception-v7/` (manifestes de départ et de fin, acte de gel, configuration, lots, registre dérivé, alertes éventuelles) et les deux journaux du lanceur (`«D»/lanceur-course-v7.*.txt`, scellés) ; **ne lire aucune carte**. Code 2 avec un nœud C13 : issue rapportée, tentative consommée, aucune relance sans version neuve et mot de la mère. Code 3, 4 ou 5 : alerte scellée transmise à la mère.

**Réserves** (additif v2g, § 6) : (1) si l'interface ne compte pas la pensée de Carbon dans la sortie, une pensée au-delà de 65 536 rend le code 7 ; (2) un appel de Carbon au-delà de 1 680 s est perdu (code 6) ; (3) le pire cas tient au compte de la commande (6,04 USD nécessaires à la borne prudente) ; (4) onze pires cas de Carbon priveraient les juges de budget (seuil 90 USD avant les juges) ; (5) les sondes, l'épreuve et les relevés ne valent que le jour `«J»`.

## 16. Essai à blanc et épreuve hors ligne (joués par l'auteur ; à rejouer si l'on veut, dossiers neufs)

```
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md > «DOSSIER_NEUF»-matiere-premiere-v3.md
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v7.py --a-blanc «DOSSIER_NEUF»/a-blanc
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/epreuve_temoins_auto_conception_v7.py --hors-ligne «DOSSIER_NEUF»/epreuve-hors-ligne --matiere «DOSSIER_NEUF»-matiere-premiere-v3.md
```
Résultats versés : `course-v4/essai-a-blanc-v2g/` (moteur simulé, code 0, composition entière — deux Claude, Argon, Astra, Carbon —, 110 cartes à passeport, étapes proposition, aiguillage, juges jouées, passe « tableau » et fusions retirées, montant requis 120, Carbon : enveloppe, réglage de l'additif v2g, sortie retenue 65 536, pire cas 5,817437 USD, durée au pire 1 740 s, sondes d'essai ; épreuve hors ligne v7 : « témoins éprouvés hors ligne », 0 juge au hasard réussi sur 2 000).
