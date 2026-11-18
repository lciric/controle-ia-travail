# Commandes exactes — course d'auto-conception de l'organisme d'idéation, tentative neuve v2f (pour la session d'exécution)

Écrites le 18 novembre 2026 par le développeur unique de la tentative neuve (modèle L′). Pièce **neuve** (R12) : les commandes v2 à v2e restent en place, archivées (la v2e n'a jamais servi) ; **ce texte se suffit à lui-même**. Fondement : mot de Lazar « 2a » (tentative neuve après le diagnostic, correction ciblée de Carbon, sonde neuve d'Astra, ligne de GO neuve) ; additif v2e ; **correction de consigne de la session principale** (documentation du fournisseur : `maxOutputTokens` compte la pensée, coupure dure) ; additif v2f. **Rien n'a été lancé par l'auteur** : moteur simulé, relais factices, aucun appel. Aucune valeur de clé n'est écrite nulle part (noms de variables seulement).

Notations : `«D»` = le dossier hors dépôt neuf **`/home/user/execution-auto-conception-v2f`** ; `«J»` = le jour UTC du départ (`date -u +%F`), **le même pour la sonde, l'épreuve, les relevés et le lancement** (le lanceur exige des pièces « du jour ») ; `«GO_COURSE»`, `«GO_EPREUVE»` = les deux lignes neuves (§ 2) ; `«PID_…»` = les PID lus dans les consoles des relais. Clé Claude : celle que nomme la pièce de départ (par défaut **`RR_ANTHROPIC_API_KEY_RIGAUD`**) ; Argon et Carbon : **`GEMINI_API_KEY`** ; Astra : **`OPENAI_API_KEY`**. Modèles : Carbon `gemini-4-carbon`, Astra `gpt-6-astra`, Argon `gemini-4-argon`, Claude `claude-opus-5-5` et `claude-fable-5-1`. Orchestrateur : `/home/user/ideation-organism` au commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, propre.

## 0. Ce qui change (et rien d'autre)

La course v4 (`runs/20261118-171908-course-auto-conception-v4/`) est close : code 2, étape « proposition » non mesurée (technique), **44,780492 USD**. Cause (diagnostic `510312b1…`) : Carbon, trois codes 7 (pensée de 17 454 à 20 696 jetons au-delà de la provision de 8 192) et un code 6 (délai de 1 500 s) ; Astra, un 502 « amont coupé ». La tentative neuve :

- appelle Carbon avec **`--provision-pensee-jetons 28672 --max-sortie-jetons 32768 --delai-s 1620 --delai-requete-s 60`** (le lanceur v6 refuse la déclaration sans exactement 28 672 et 32 768). La pensée compte dans `maxOutputTokens` : la sortie retenue par la commande au pire (32 768 à son compte, 29 271 à la borne prudente du lanceur) doit couvrir la pensée observée (jusqu'à 20 696) et la réponse (≈ 3 500) — le lanceur exige ≥ 24 500 ; pire cas d'un appel, calculé comme la commande le calcule (sortie + provision au prix de sortie, plus l'entrée gardée) : 2,946649 USD (2,999969 à la borne prudente), sous 3 USD ;
- **ne relève pas le délai de Carbon** : l'orchestrateur épinglé tue toute commande externe à **1 800 s fixes** (`pole/adaptateurs.py`, `DELAI_COMMANDE_S` ; le lanceur v8 n'en passe aucun) ; `--delai-s 3000` ferait tuer la commande sans annuler son lot ; durée au pire retenue 1 620 + 30 + 2 × 60 = 1 770 s ; le lanceur v6 refuse toute durée au pire (délai + intervalle + 2 × délai de requête) au-delà de 1 770 s ;
- **n'ajoute aucune reprise d'Astra** (sans toucher la commande épinglée, une reprise ferait voir à l'orchestrateur un coût au-dessus du plafond de session : pas propre) ; une coupure isolée est tolérée (A3 : 3 échecs consécutifs ; A14 : part inexploitable ≤ 0,34) ; refait la **sonde d'Astra du jour** (§ 3), que le lanceur v6 relit ;
- joue une **épreuve des témoins du jour** par le programme **v6** (un rapport d'épreuve ne vaut que pour le lanceur qui part) ;
- part sous des **lignes de GO neuves** et un **mot de reprise** (la ligne de la course, périmètre « auto-conception » et « tentative neuve »), seul moyen d'admettre la course v4 close dans la garde « une seule course ».

## 1. Empreintes (à vérifier avant tout)

| pièce | sha256 |
|---|---|
| `scripts/lancer_course_auto_conception_v6.py` (lanceur v6, à citer en entier par la contre-lecture) | `2ecd9081d4f9860354637d6c2b235c76ccfdb23d81a4ae7668929b760b969e00` |
| `course-v3/additif-preenregistrement-course-auto-conception-v2f.md` (épinglé par le lanceur v6, à citer en entier par la contre-lecture) | `3199e80ef29950a8bf00219732c792e4c1c7032546c145602ee0d1f4bfb16345` |
| `scripts/epreuve_temoins_auto_conception_v6.py` (épinglé par le lanceur v6) | `bc94729f6cd709a37e87f862751f5a83cbb93d606abb76683c3ce6e2334ac97d` |
| `course-v3/piece-de-depart-gabarit-auto-conception-v2f.json` (gabarit, jamais lu par le lanceur) | `868e7de479e5e2e4b611f7697069943f8f523357133f7e49bd2fc4eb98ffa730` |
| `course-v3/devis-course-auto-conception-v2f.md` | `7a8ef9d4264f2d963e7ce6ccde194bf96aa8a84696a3527d774f1e32467e3528` |
| `course-v3/calcul-devis-course-auto-conception-v2f.json` (chiffres du devis) | `5dc32255031322c6da058f3942808a973c8d4f70c21bd9a870daec85e633b9e2` |
| `tests/test_lancer_course_auto_conception_v6.py` (202 essais) | `13dd4be95b9d5ffe525ad41da32aa69d6dc031e5c3fd6bef8d90fa6bf0857854` |
| `tests/test_epreuve_temoins_auto_conception_v6.py` (88 essais) | `b8696bd98edfeea0a5eb01aa1b6048ea5b9b4cc9b743dcc74a5797429f24b509` |
| `course-v2/preenregistrement-course-auto-conception-v2.md` (inchangé) | `0d51e0b3f51dd731351589187c124b7ee1a6237494aa0274825b19085c6763c6` |
| `course-v2/additif-preenregistrement-course-auto-conception-v2c.md` (inchangé) | `7c76eba0340040b2c2d29cf3aa5015a194632ac24f3e558565a22424702b0cfd` |
| `course-v2/additif-preenregistrement-course-auto-conception-v2d.md` (inchangé) | `cb4d44d081e505dfafc2ae4552fbaa8b80e3370ea7e295966a6a1708ce512e45` |
| `runs/20261118-171908-course-auto-conception-v4/manifeste-lanceur-fin.json` (course close, épinglée par le lanceur v6) | `2625234c786a7fc50c926325c1a9efc8a8e9b74146a59205bf8a31c6e2c5fd7f` |
| `scripts/sonde_astra_courses_v1.py` (inchangée) | lue par son compagnon |
| commande d'Astra (sur `main`) `docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py` | `986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71` |
| commande de Carbon par lot (sur `main`) `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py` | `9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75` |
| relais Gemini v4 de Carbon (sur `main`) `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v4.py` | `543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4` |
| relais Claude `/home/user/ideation-organism/orchestrator/pole/relais_reel.py` | `1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153` |
| relais Gemini d'Argon `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py` | `2b0043bcab8b3922c65a4008e719408c52781d7544064b5a29a23d7ef60c1aeb` |
| relais compatible OpenAI d'Astra `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py` | `67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e` |
| matière servie (sur `main`) `docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md` | `11f4b69ba42147c428090e4805948a708d0ed266da0c0cd07f194723eaba742d` |

```
cd /home/user/controle-ia-travail && git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
cd /home/user/controle-ia-travail && for f in scripts/lancer_course_auto_conception_v6.py scripts/epreuve_temoins_auto_conception_v6.py scripts/sonde_astra_courses_v1.py docs/notes/organisme-auto-conception-v1/course-v3/additif-preenregistrement-course-auto-conception-v2f.md docs/notes/organisme-auto-conception-v1/course-v3/piece-de-depart-gabarit-auto-conception-v2f.json docs/notes/organisme-auto-conception-v1/course-v3/devis-course-auto-conception-v2f.md docs/notes/organisme-auto-conception-v1/course-v3/calcul-devis-course-auto-conception-v2f.json docs/notes/organisme-auto-conception-v1/course-v2/preenregistrement-course-auto-conception-v2.md docs/notes/organisme-auto-conception-v1/course-v2/additif-preenregistrement-course-auto-conception-v2c.md docs/notes/organisme-auto-conception-v1/course-v2/additif-preenregistrement-course-auto-conception-v2d.md runs/20261118-171908-course-auto-conception-v4/manifeste-lanceur-fin.json tests/test_lancer_course_auto_conception_v6.py tests/test_epreuve_temoins_auto_conception_v6.py; do (cd "$(dirname "$f")" && sha256sum -c "$(basename "$f").sha256"); done
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md | sha256sum
sha256sum /home/user/ideation-organism/orchestrator/pole/relais_reel.py && git -C /home/user/ideation-organism rev-parse HEAD && git -C /home/user/ideation-organism status --porcelain --untracked-files=all --ignored=matching
cd /home/user/controle-ia-travail && PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B -m pytest -q -rs -p no:cacheprovider tests/test_lancer_course_auto_conception_v6.py tests/test_epreuve_temoins_auto_conception_v6.py
```
Attendu : toutes les empreintes « OK » ; matière `11f4b69b…` ; relais Claude `1b90b020…` ; orchestrateur `a41b7b50…`, statut vide ; **202 + 88 = 290 essais passés**, aucun sauté (l'essai `test_reel_refuse_sans_piece_de_depart_neuve_avant_tout` se dit « sauté » une fois la pièce v2f écrite : c'est attendu, il ne vaut qu'avant).

## 2. Ce que la mère fait avant tout (nœuds : rien ne part sans)

1. **Deux lignes de GO neuves**, au registre `registres/go.md` sur `main`, accordées par Lazar, type « calcul », période couvrant `«J»` :
   - `«GO_COURSE»` : plafond **exactement `90 USD`** (l'orchestrateur exige de la ligne le montant du plafond d'arrêt à l'identique ; une ligne de 45 USD serait refusée avant tout appel ; l'estimation, **≈ 59,81 USD**, est au devis v2f), périmètre qui contient **« auto-conception »** et **« tentative neuve »** ;
   - `«GO_EPREUVE»` : plafond **`5 USD`**, périmètre qui contient **« témoins »**.
   Jamais `GO-2026-11-18-20`, `-21` ni `-36` (consommées par la v4 : le lanceur v6 les refuse).
2. **Crédit de la clé Claude** : avec 124 USD déclarés et 18 USD de réserves, le reste net au départ serait **72,73 USD ≤ 90** : **code 3** (devis v2e § 5, inchangé en v2f). Il faut un crédit déclaré **strictement au-dessus de 141,27 USD** (réserves inchangées), des réserves revues, ou une autre clé.
3. **Contre-lecture** (§ 4) scellée « Scellable. ».

## 3. Sonde d'Astra du jour (≤ 0,05 USD, signalée ; avant tout autre relais)

Relais **jeté**, port 8793 (jamais 8787 à 8792) :

```
mkdir «D» «D»/maison «D»/sonde-astra
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py > «D»/commande_astra_v1.py && echo "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71  «D»/commande_astra_v1.py" | sha256sum -c -
cd «D»/sonde-astra && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/sonde-astra/console-astra-sonde.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8793 --modeles-permis gpt-6-astra --plafond-usd 0.05 --reserve-par-appel 0.01 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 1 --journal «D»/sonde-astra/journal-relais-astra-sonde.jsonl
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/sonde_astra_courses_v1.py --commande «D»/commande_astra_v1.py --url-relais-jete http://127.0.0.1:8793 --pid-relais-jete «PID_DU_RELAIS_JETE» --sortie docs/notes/organisme-auto-conception-v1/course-v3/sonde-astra-commune-«J»-v1.json --sortie-v2 docs/notes/organisme-auto-conception-v1/course-v3/sonde-astra-v2-«J»-auto-conception-v2f.json
```
Codes : **0** réussie ; **1** non réussie, rapport écrit (si `echec_de_configuration` est vrai, rien n'est parti : relais neuf, chemins neufs) ; **2** refus avant tout appel. Puis `curl -s --noproxy '*' http://127.0.0.1:8793/relais/etat` (1 appel, dépense ≤ 0,05), arrêt **par PID** (`kill -INT «PID_DU_RELAIS_JETE»`, R10), consigner l'arrêt et **signaler la dépense**. Vérifier :
```
cd /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/course-v3 && sha256sum -c sonde-astra-commune-«J»-v1.json.sha256 && /usr/local/bin/python3 -I -c "import json,sys;o=json.load(open('sonde-astra-commune-«J»-v1.json'));print(o['ok'],o['jour'],o['cout_usd'],o['appel_envoye'],o['commande']['sha256']);sys.exit(0 if o['ok'] is True and o['jour']=='«J»' else 1)"
```
Attendu : `True «J» … True 986cf71e…`, code 0. **Si la sonde n'a pas réussi : Astra n'est pas déclarée** (pièce : `declaree` faux, retirer `astra` de `commandes_epinglees` et de la déclaration des relais) — décision de la mère, la composition changerait (nœud).

## 4. Contre-lecture de la tentative neuve (modèle K) — avant l'épreuve

Par un contre-lecteur neuf du modèle K, qui n'a écrit ni l'additif v2f, ni le lanceur v6, ni le programme d'épreuve v6 (R2). Fichiers à lui donner : l'additif v2f, les additifs v2c, v2d et v2e, le préenregistrement v2, `scripts/lancer_course_auto_conception_v6.py` et la v5, `scripts/epreuve_temoins_auto_conception_v6.py` et la v5, les deux fichiers d'essais v6, le diagnostic (`course-v2/diagnostic-erreurs-carbon-astra-course-v4-v1.md`), le manifeste de fin de la v4, le gabarit v2f, le devis v2f et son calcul, ces commandes, le rapport du développeur (`course-v3/rapport-developpeur-tentative-neuve-v2f.md`), la commande de Carbon (`git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py`) et, dans `/home/user/ideation-organism/orchestrator`, `pole/adaptateurs.py` (`AdaptateurCommandeExterne`, `DELAI_COMMANDE_S`), `demonstrations/ideation_v8.py` (`adaptateurs_reels_v56`), `pole/budget_v56.py`, `pole/configuration_v54.py` (`montant_requis`). Rapport écrit et scellé à `docs/notes/organisme-auto-conception-v1/course-v3/contre-lecture-tentative-neuve-v2f-auto-conception.md` : il cite **en entier** `3199e80ef29950a8bf00219732c792e4c1c7032546c145602ee0d1f4bfb16345` (additif v2f) et `2ecd9081d4f9860354637d6c2b235c76ccfdb23d81a4ae7668929b760b969e00` (lanceur v6), se dit du modèle K, la première ligne sous « ## Verdict » est exactement « Scellable. », et il ne dit nulle part n'avoir pas relu. Une correction demandée donne des versions neuves (R12) : ces commandes ne valent plus.

## 5. Pièce de départ v2f (la mère)

Recopier le gabarit sous le nom lu par le lanceur, remplir **chaque** « À REMPLIR » (outil d'écriture de fichiers ; `go_course`, `go_epreuve`, `tentative_neuve.mot_de_reprise` = `«GO_COURSE»`, `credit_declare_cle_claude_usd` (nombre), `especes_optionnelles.astra.sonde_du_jour` et `sonde_du_jour_rapport` = `docs/notes/organisme-auto-conception-v1/course-v3/sonde-astra-commune-«J»-v1.json`, `ecrit_le`, `statut`), revoir les deux réserves de la clé Claude, puis sceller :
```
cd /home/user/controle-ia-travail && cp --update=none docs/notes/organisme-auto-conception-v1/course-v3/piece-de-depart-gabarit-auto-conception-v2f.json docs/notes/organisme-auto-conception-v1/course-v3/piece-de-depart-auto-conception-v2f.json
cd /home/user/controle-ia-travail && grep -c "À REMPLIR" docs/notes/organisme-auto-conception-v1/course-v3/piece-de-depart-auto-conception-v2f.json
cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-auto-conception-v1/course-v3/piece-de-depart-auto-conception-v2f.json
```
(le `grep -c` doit rendre **0** avant le scellement). La pièce est relue par le lanceur et par l'épreuve (lignes consommées refusées, mot de reprise égal à `go_course`, course close citée `20261118-171908-course-auto-conception-v4`).

## 6. Sonde du bac à sable (commande de l'orchestrateur), avant l'épreuve

```
cd /home/user/ideation-organism/orchestrator && env -i PATH=/usr/local/bin:/usr/bin:/bin LANG=C.UTF-8 /usr/local/bin/python3 -I -B -c "import json, sys
sys.path.insert(0, sys.argv[1])
from pole.adaptateurs import etat_bac_a_sable_detaille
print(json.dumps(etat_bac_a_sable_detaille()))" /home/user/ideation-organism/orchestrator
```
Attendu : `{"actif": true, "proc_neuf": true, …}`. Sinon : installer le bac (bwrap, socat) ; le programme d'épreuve et le lanceur refusent de toute façon (code 2, rien dépensé).

## 7. Épreuve réelle des témoins du jour (programme v6 ; 5 USD ; 33 appels)

Aucun relais ne doit tourner (ports 8787 à 8793) : `pgrep -af "relais_reel.py|relais_gemini|relais_kimi"` ne rend rien (sinon arrêt **par PID**, `kill -INT «PID»`, R10, consigné). Relais **propres à l'épreuve** :
```
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-claude-epreuve.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_RIGAUD -- /usr/bin/python3 -I -B /home/user/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_RIGAUD --port 8787 --plafond-usd 5 --modeles-permis claude-fable-5-1,claude-opus-5-5 --journal «D»/journal-relais-claude-epreuve.jsonl
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-gemini-epreuve.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle GEMINI_API_KEY --port 8788 --max-appels 24 --modele gemini-4-argon --journal «D»/journal-relais-gemini-epreuve.jsonl
```
(Si la clé Claude nommée par la pièce n'est pas `RR_ANTHROPIC_API_KEY_RIGAUD`, remplacer son nom partout.) Vérifier : `tr '\0' ' ' < /proc/«PID»/cmdline` pour chaque relais ; `curl -s --noproxy '*' http://127.0.0.1:8787/relais/etat` (0 appel, plafond 5) ; `curl -s --noproxy '*' http://127.0.0.1:8788/relais/etat` (0 appel, `max_appels` 24, `variable_cle_encore_presente` faux).

Déclaration de l'épreuve, **chemin neuf**, écrite avec l'outil d'écriture de fichiers puis scellée : `docs/notes/organisme-auto-conception-v1/course-v3/declaration-relais-epreuve-temoins-auto-conception-v6.json`
```json
{"version": "declaration-relais-epreuve-temoins-auto-conception-v6", "fournisseurs": {
 "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:8787", "nom_cle": "RR_ANTHROPIC_API_KEY_RIGAUD", "pid_relais": «PID_CLAUDE_EPREUVE»,
            "porte_plafond": {"type": "commande", "delai_s": 30, "commande": ["/usr/local/bin/python3", "-I", "-B",
              "/home/user/controle-ia-travail/scripts/porte_plafond_relais_v1.py", "--url", "http://127.0.0.1:8787",
              "--modeles-permis", "claude-fable-5-1,claude-opus-5-5", "--plafond-ligne", "5"]}},
 "argon": {"type": "commande_externe", "commande": ["bash", "/home/user/controle-ia-travail/rapports/fille-ideation-1-v1/appel-argon-v5.sh"],
           "nom_cle": "GEMINI_API_KEY", "pid_relais": «PID_GEMINI_EPREUVE», "url_etat_relais": "http://127.0.0.1:8788",
           "porte_plafond": {"type": "environnement"}}}}
```
```
cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-auto-conception-v1/course-v3/declaration-relais-epreuve-temoins-auto-conception-v6.json
cd /home/user/controle-ia-travail && git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
cd /home/user/controle-ia-travail && env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=«D»/maison LANG=C.UTF-8 /usr/local/bin/python3 -I -B scripts/epreuve_temoins_auto_conception_v6.py --reel > «D»/epreuve-reelle-v6.stdout.txt 2> «D»/epreuve-reelle-v6.stderr.txt; echo "code $?"
```
Le programme refuse **avant tout appel** (code 2, rien dépensé) : clé dans l'environnement ; rapport v6 déjà écrit ; pièce de départ absente, non remplie ou à une ligne consommée ; `«GO_EPREUVE»` absente, hors période, d'un autre plafond que 5 USD ou sans « témoins » ; **mot de reprise** (`«GO_COURSE»`) absent ou sans « tentative neuve » ; pièces d'une autre empreinte ; bac inactif ; borne d'Argon sous 24. Codes : 0 rapport écrit (lire le verdict) ; 2 refus. Sortie : `course-v3/epreuve-temoins-reelle-auto-conception-v6.json` (scellé par le programme ; `verdict`, `verdict_lecture_gelee`, `incidents_techniques`, `tentatives_precedentes` v3 et v4, `mot_de_reprise`, `budget_epreuve_usd` = 5.0). **Verdict autre que « réussie » : arrêt, aucune course, rapport à la mère.** Puis : lire `depense_usd` sur `http://127.0.0.1:8787/relais/etat` (dépense Claude de l'épreuve, pour le § 9) et sur `…:8788/relais/etat`, arrêter les deux relais **par PID** (`kill -INT «PID»`), consigner l'arrêt et la dépense, verser la déclaration et les deux journaux (stdout, stderr, scellés) dans `course-v3/epreuve-reelle-v6-«J»-v1/`.

## 8. Relevé des prix Claude du jour

Lire la page officielle **https://platform.claude.com/docs/en/about-claude/pricing** (lignes « Claude Opus 5.5 » et « Claude Fable 5.1 », entrée et sortie par million de jetons). Barème du relais attendu : 4 / 20 et 10 / 50 USD ; tout autre prix : **arrêt, nouveau devis** (le lanceur refuse). Écrire puis sceller `docs/notes/organisme-auto-conception-v1/course-v3/releve-prix-claude-course-auto-conception-v2e.json` :
```json
{"releve_utc": "«date -u +%FT%TZ»", "source": "https://platform.claude.com/docs/en/about-claude/pricing, lue le «date -u +%FT%TZ» : Claude Opus 5.5 4 / 20 USD, Claude Fable 5.1 10 / 50 USD par million de jetons (entrée / sortie)", "prix": {"espece_claude_1": {"entree": 4.0, "sortie": 20.0}, "espece_claude_2": {"entree": 10.0, "sortie": 50.0}}}
```
```
cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-auto-conception-v1/course-v3/releve-prix-claude-course-auto-conception-v2e.json
```

## 9. Relevé des crédits du jour (après l'épreuve)

Écrire puis sceller `docs/notes/organisme-auto-conception-v1/course-v3/releve-credits-avant-course-auto-conception-v2e.json`. Clé Claude non lisible : dépense antérieure = **32,269175 USD** (relevé v4 : 7,479689 ; plus la course v4, 24,789486) **+ la dépense Claude de l'épreuve v6** (§ 7) ; **ne pas retrancher** les réserves (le lanceur le fait) :
```json
{"releve_utc": "«date -u +%FT%TZ»",
 "cles": {"RR_ANTHROPIC_API_KEY_RIGAUD": {"non_lisible": true, "motif": "solde illisible ; dépense antérieure : 32,269175 USD (relevé v4 7,479689 + course v4 24,789486) plus la dépense Claude de l'épreuve v6 lue sur le relais 8787", "depense_anterieure_usd": «32.269175 + dépense Claude de l'épreuve v6»},
          "GEMINI_API_KEY": {"non_lisible": true, "motif": "solde illisible (R-3222)"},
          "OPENAI_API_KEY": {"non_lisible": true, "motif": "solde illisible"}},
 "dispense": {"par": "mère", "reference": "R-3237", "cles": ["GEMINI_API_KEY", "OPENAI_API_KEY"]}}
```
```
cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-auto-conception-v1/course-v3/releve-credits-avant-course-auto-conception-v2e.json
```
Compté par le lanceur : crédit déclaré − dépense antérieure − réserves ; **code 3** (alerte scellée pour la mère) si ce reste net est ≤ 90 USD (voir § 2, point 2).

## 10. Relais de la course (bornes de la v4 ; Carbon inchangé côté relais)

Les relais de l'épreuve sont arrêtés. Depuis `«D»` :
```
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-claude-course.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_RIGAUD -- /usr/bin/python3 -I -B /home/user/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_RIGAUD --port 8787 --plafond-usd 90 --modeles-permis claude-fable-5-1,claude-opus-5-5 --journal «D»/journal-relais-claude-course.jsonl
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-gemini-course.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle GEMINI_API_KEY --port 8788 --max-appels 464 --modele gemini-4-argon --journal «D»/journal-relais-gemini-course.jsonl
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-astra.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8790 --modeles-permis gpt-6-astra --plafond-usd 34 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 60 --delai-amont-s 3400 --journal «D»/journal-relais-astra.jsonl
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py > «D»/commande_gemini_lot_v1.py && echo "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75  «D»/commande_gemini_lot_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v4.py > «D»/relais_gemini_v4.py && echo "543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4  «D»/relais_gemini_v4.py" | sha256sum -c -
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-carbon.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B «D»/relais_gemini_v4.py --variable-cle GEMINI_API_KEY --port 8792 --modele gemini-4-carbon --max-appels 60 --max-lots 15 --journal «D»/journal-relais-carbon.jsonl
```
(La commande d'Astra est déjà dans `«D»`, § 3.) Bornes : Argon **464** = 2 × 231 + 2 ; Carbon `--max-appels 60` ≥ 24 et `--max-lots 15` ≥ 11 ; Astra 60 ≥ 11. Vérifier chaque relais par PID (`tr '\0' ' ' < /proc/«PID»/cmdline`) et `curl -s --noproxy '*' http://127.0.0.1:«PORT»/relais/etat` sur 8787, 8788, 8790, 8792 : **0 appel** partout (0 lot pour Carbon), plafond 90 (Claude), `max_appels` 464 (Argon), variable de clé effacée (Gemini). Kimi : aucun relais.

## 11. Déclaration des relais de la course (chemin neuf, v6 ; Carbon réglé)

Écrire (outil d'écriture de fichiers ; `«D»` en chemin absolu, `/home/user/execution-auto-conception-v2f`), puis sceller, `docs/notes/organisme-auto-conception-v1/course-v3/declaration-relais-course-auto-conception-v6.json` :
```json
{"version": "declaration-relais-course-auto-conception-v6", "fournisseurs": {
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
            "http://127.0.0.1:8792/v1beta", "--modele", "gemini-4-carbon", "--prix-entree", "8.3", "--prix-sortie", "41.5",
            "--provision-pensee-jetons", "28672", "--max-sortie-jetons", "32768", "--delai-s", "1620", "--delai-requete-s", "60"],
            "modele_propose": "gemini-4-carbon", "nom_cle": "GEMINI_API_KEY", "pid_relais": «PID_CARBON»,
            "url_etat_relais": "http://127.0.0.1:8792", "porte_plafond": {"type": "environnement"}}}}
```
```
cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-auto-conception-v1/course-v3/declaration-relais-course-auto-conception-v6.json
```
Chaque option de Carbon s'écrit **une fois, en entier, séparée de sa valeur** (le lanceur refuse une abréviation, un `--x=v`, un doublon, une option inconnue). Aucune variante : provision 28 672 et sortie 32 768 exactement ; durée au pire ≤ 1 770 s (`--delai-s 1500` sans `--delai-requete-s` est aussi admis : 1 500 + 30 + 2 × 120).

## 12. Lancement de la course (plafond d'arrêt 90 USD), **détaché de l'outil**, le jour `«J»` avant minuit UTC

Seulement si l'épreuve v6 a rendu « réussie », la contre-lecture du § 4 est scellée « Scellable. », la pièce, la sonde et les deux relevés du jour sont scellés. La variable de la clé Claude présente dans l'environnement du lanceur (testée par son nom, jamais lue, retirée de l'environnement de l'orchestrateur). La course peut durer plusieurs heures (Carbon par lot : jusqu'à ≈ 30 minutes par appel) : elle est lancée par `setsid nohup`, **détachée** de toute commande d'arrière-plan de l'outil (qui serait coupée à 2 h), sorties dans `«D»` :
```
cd /home/user/controle-ia-travail && git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
cd /home/user/controle-ia-travail && GO_ID=«GO_COURSE» setsid nohup /usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v6.py > «D»/lanceur-course-v6.stdout.txt 2> «D»/lanceur-course-v6.stderr.txt < /dev/null & echo "PID_LANCEUR $!"
```
Relever le PID ; vérifier `tr '\0' ' ' < /proc/«PID_LANCEUR»/cmdline` (doit nommer `lancer_course_auto_conception_v6.py`). La première ligne de `«D»/lanceur-course-v6.stdout.txt` est le manifeste de départ (`{"manifeste_depart": …, "sha256": …}`) ; un refus avant le départ s'écrit sur `«D»/lanceur-course-v6.stderr.txt` (`{"refus": …}`, code 2 ; `{"alerte_credit": …}`, code 3) et le processus se termine. Suivi sans rien lire des cartes : `kill -0 «PID_LANCEUR» && echo vivant` ; `cat «D»/lanceur-course-v6.stdout.txt` ; à la fin, la dernière ligne est le manifeste de fin (`code`, `cout_reel_usd`). Ne jamais arrêter par motif de ligne de commande (R10) : par PID seulement, et seulement sur décision (le lanceur relaie SIGTERM à l'orchestrateur et écrit son manifeste de fin).

Le lanceur exige, dans l'ordre : pièce de départ v2f (aucune ligne consommée ; mot de reprise ; course close citée) ; « une seule course » (course v4 close admise, son manifeste de fin `2625234c…` scellé ; aucune course v5 ni v6 déjà lancée) ; clé Claude présente ; `«GO_COURSE»` au registre de `main` (90 USD, « auto-conception ») et **mot de reprise** (« tentative neuve ») ; préenregistrement, pièces, additif v2f, contre-lecture ; matière ; épreuve v6 « réussie » du jour ; **sonde d'Astra du jour** ; déclaration (composition tenue ; **Carbon réglé**, provision 28 672, sortie 32 768, durée au pire 1 770 s ≤ 1 770 s, sortie retenue au pire ≥ 24 500, pire cas ≤ 3 USD) ; relevé des crédits ; relais (Argon ≥ 464 ; Carbon ≥ 24 appels et ≥ 11 lots) ; relevé des prix ; orchestrateur ; bac ; vérification de l'orchestrateur ; porte à blanc. Sortie hors dépôt : `/home/user/sorties-course-auto-conception-v6/«id»/` ; dossier du run au dépôt : `runs/«id»-course-auto-conception-v6/`. Codes : **0** fini ; **2** refus ou arrêt (nœud C13 compris) ; **3** alerte de crédit avant le départ ; **4** cumul au-dessus de 90 USD ; **5** arrêt au premier refus pour crédit d'un relais dispensé.

## 13. Après

Lire `/relais/etat` de chaque relais (8787, 8788, 8790, 8792 : dépense, appels), les arrêter **par PID** (`kill -INT «PID»`), consigner chaque arrêt et la dépense ; verser `runs/«id»-course-auto-conception-v6/` (manifestes de départ et de fin, acte de gel, configuration, lots, registre dérivé, alertes éventuelles) et les deux journaux du lanceur (`«D»/lanceur-course-v6.*.txt`, scellés) ; **ne lire aucune carte** (la lecture est à la mère). Code 2 avec un nœud C13 : issue rapportée, tentative consommée, aucune relance sans version neuve et mot de la mère. Code 3, 4 ou 5 : alerte scellée transmise à la mère.

**Réserves** (additif v2f) : (1) une pensée au-delà de 28 672 jetons rendrait le code 7 (garde de la commande) ; (2) un lot plus long que 1 620 s est encore perdu (code 6), et un compte de jetons ou une création de lot au-delà de 60 s rend un échec ; (3) une coupure d'Astra est tolérée si elle reste isolée (A3, A14), pas une série ; (4) la sonde et l'épreuve ne valent que le jour `«J»`.

## 14. Essai à blanc et épreuve hors ligne (joués par l'auteur ; à rejouer si l'on veut, dossiers neufs)

```
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md > «DOSSIER_NEUF»-matiere-premiere-v3.md
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v6.py --a-blanc «DOSSIER_NEUF»/a-blanc
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/epreuve_temoins_auto_conception_v6.py --hors-ligne «DOSSIER_NEUF»/epreuve-hors-ligne --matiere «DOSSIER_NEUF»-matiere-premiere-v3.md
```
Résultats versés : `course-v3/essai-a-blanc-v2f/` (moteur simulé, code 0, composition de la tentative — deux Claude, Argon, Astra, Carbon —, 110 cartes à passeport, additif v2f et lanceur v6 cités, Carbon réglé : provision 28 672, sortie 32 768, durée au pire 1 770 s, sortie retenue au pire 29 271, pire cas 2,999969 USD par appel ; épreuve hors ligne v6 : « témoins éprouvés hors ligne », 0 juge au hasard réussi sur 2 000).
