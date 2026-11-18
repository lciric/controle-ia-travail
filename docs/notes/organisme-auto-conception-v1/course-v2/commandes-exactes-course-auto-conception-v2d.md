# Commandes exactes — course d'auto-conception de l'organisme d'idéation, correctif v2d (pour la session d'exécution)

Écrites le 18 novembre 2026 par le développeur unique du correctif v2d (modèle L′). Pièce **neuve** (R12) : les commandes v2, v2b et v2c restent en place, archivées ; **ce texte se suffit à lui-même** (aucune étape n'est à chercher ailleurs). Fondement : mot de Lazar, 18 novembre 2026, « go (a), lance les deux correctifs », et sa décision **`GO-2026-11-18-36`** (reprise unique de l'épreuve des témoins, 5 USD au total tentative v3 comprise, les 7 verdicts d'Argon de la v3 ne comptent pas, course seulement si la reprise rend « réussie ») ; additif v2d. **Rien n'a été lancé par l'auteur** : moteur simulé, relais factices, aucun appel. Aucune valeur de clé n'est écrite nulle part (noms de variables seulement). `«D»` = le dossier hors dépôt neuf **`/home/user/execution-auto-conception-v2d`** ; `«CLONE»` = `/home/user/ideation-organism` (copie de l'orchestrateur au commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, propre).

**Délai** : la sonde d'Astra citée par la pièce de départ ne vaut que le **18 novembre 2026** ; la course doit partir avant minuit UTC. Passé minuit : arrêt, mot de la mère.

Noms fixés : clé Claude **`RR_ANTHROPIC_API_KEY_RIGAUD`** (nommée par la pièce de départ) ; clé d'Argon et de Carbon **`GEMINI_API_KEY`** ; clé d'Astra **`OPENAI_API_KEY`** ; modèles : Carbon `gemini-4-carbon`, Astra `gpt-6-astra`, Argon `gemini-4-argon`, Claude `claude-opus-5-5` et `claude-fable-5-1`. Lignes de GO (pièce de départ) : course **`GO-2026-11-18-20`** (90 USD), épreuve des témoins **`GO-2026-11-18-21`** (5 USD au total, tentative v3 comprise) ; décision de reprise **`GO-2026-11-18-36`**.

## 0. Ce qui a changé (deux causes techniques, correction)

L'épreuve réelle v3 (16:11Z, 0,132289 USD, rapport scellé `course-v2/epreuve-temoins-reelle-auto-conception-v3.json`, `1e11376f…`) a échoué pour deux causes techniques : (1) bac à sable absent (bwrap, socat) : aucun appel Claude parti ; (2) chaque jugement d'Argon coûte **deux** appels au relais Gemini (`countTokens` puis `generateContent`) : 22 appels de relais nécessaires, relais borné à 15. Le programme d'épreuve **v4** sonde le bac avant tout appel, exige la borne doublée du relais d'Argon (2 × 11 + 2 = **24**), qualifie « non conclue » une épreuve dont tous les manques sont techniques, exige la ligne `GO-2026-11-18-36`, retranche la dépense v3 du plafond (budget de la reprise **4,867711 USD**) et refuse de partir si son rapport existe déjà. Le **même défaut de comptage touchait la course** : 231 appels d'Argon au pire demandent **2 × 231 + 2 = 464** appels au relais d'Argon (les commandes v2c posaient 280) ; le lanceur **v4** l'exige (et Carbon : 2 × 11 + 2 = 24 appels et 11 lots au moins ; ses bornes 60 et 15 suffisent). Rien d'autre ne change.

## 1. Empreintes (à vérifier avant tout)

| pièce | sha256 |
|---|---|
| `scripts/lancer_course_auto_conception_v4.py` (lanceur v4, à citer en entier par la contre-lecture) | `b1661f119407530b0f6e940a75e8811d6dd968fd33bfca08f7f0933ed4e8707e` |
| `course-v2/additif-preenregistrement-course-auto-conception-v2d.md` (épinglé par le lanceur v4, à citer en entier par la contre-lecture) | `cb4d44d081e505dfafc2ae4552fbaa8b80e3370ea7e295966a6a1708ce512e45` |
| `scripts/epreuve_temoins_auto_conception_v4.py` (épinglé par le lanceur v4) | `04f62b8c48db9e9b04114aaa37f00801e825ff0bc2d4a86934b44f2b79263d75` |
| `course-v2/additif-preenregistrement-course-auto-conception-v2c.md` (inchangé, cité par l'additif v2d) | `7c76eba0340040b2c2d29cf3aa5015a194632ac24f3e558565a22424702b0cfd` |
| `course-v2/preenregistrement-course-auto-conception-v2.md` (inchangé, épinglé) | `0d51e0b3f51dd731351589187c124b7ee1a6237494aa0274825b19085c6763c6` |
| `course-v2/piece-de-depart-auto-conception-v2.json` (scellée, reprise telle quelle) | `e2689fa22fff31319ff69deefe10c066d5329fab28d9c9b133750f2534fc1ded` |
| `course-v2/sonde-astra-commune-2026-11-18-v1.json` (sonde du jour, faite, « ok » vrai) | `802b840edbf14983ce302b71253242c753e70aa60335868e811fdb6fd45e8f43` |
| `course-v2/releve-prix-claude-course-auto-conception-v2.json` (relevé des prix du jour, fait, scellé) | `ed812e6a336ba4682053dd7bec5554c6f5aeb4fb54dcc7d22760900a33e890b4` |
| `course-v2/epreuve-temoins-reelle-auto-conception-v3.json` (tentative v3, scellée ; sa dépense est lue par le v4) | `1e11376fe1255d281212bac086f25d143ab8c86f520dd16f3207ad95d40d02cf` |
| `tests/test_epreuve_temoins_auto_conception_v4.py` (71 essais) | `456ca30390d3973ade564afc5642d1faa629951fd86c7fdf8259be629fdcdc09` |
| `tests/test_lancer_course_auto_conception_v4.py` (130 essais) | `a049e4be37588b6a63b68ea2cda9fa9f4aef8030f456031cfbb3489d67c00d45` |
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
cd /home/user/controle-ia-travail && for f in scripts/lancer_course_auto_conception_v4.py scripts/epreuve_temoins_auto_conception_v4.py docs/notes/organisme-auto-conception-v1/course-v2/additif-preenregistrement-course-auto-conception-v2d.md docs/notes/organisme-auto-conception-v1/course-v2/additif-preenregistrement-course-auto-conception-v2c.md docs/notes/organisme-auto-conception-v1/course-v2/preenregistrement-course-auto-conception-v2.md docs/notes/organisme-auto-conception-v1/course-v2/piece-de-depart-auto-conception-v2.json docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-2026-11-18-v1.json docs/notes/organisme-auto-conception-v1/course-v2/releve-prix-claude-course-auto-conception-v2.json docs/notes/organisme-auto-conception-v1/course-v2/epreuve-temoins-reelle-auto-conception-v3.json tests/test_epreuve_temoins_auto_conception_v4.py tests/test_lancer_course_auto_conception_v4.py; do (cd "$(dirname "$f")" && sha256sum -c "$(basename "$f").sha256"); done
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md | sha256sum
sha256sum /home/user/ideation-organism/orchestrator/pole/relais_reel.py && git -C /home/user/ideation-organism rev-parse HEAD && git -C /home/user/ideation-organism status --porcelain --untracked-files=all --ignored=matching
cd /home/user/controle-ia-travail && PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B -m pytest -q -rs -p no:cacheprovider tests/test_epreuve_temoins_auto_conception_v4.py tests/test_lancer_course_auto_conception_v4.py
cd /home/user/controle-ia-travail && PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B -m pytest -q -rs -p no:cacheprovider tests/test_epreuve_temoins_auto_conception_v3.py tests/test_lancer_course_auto_conception_v3.py tests/test_lancer_course_auto_conception_v2.py tests/test_sonde_astra_courses_v1.py tests/test_astra_carbon_declares_auto_conception_v2b.py --deselect tests/test_epreuve_temoins_auto_conception_v3.py::test_constantes_identiques_a_la_v2_sauf_les_chemins_neufs
```
Attendu : toutes les empreintes « OK » ; matière `11f4b69b…` ; relais Claude `1b90b020…` ; orchestrateur `a41b7b50…`, statut vide ; **71 + 130 = 201 essais passés** ; puis **240 passés, 1 désélectionné**, aucun sauté. L'essai désélectionné (`test_constantes_identiques_a_la_v2_sauf_les_chemins_neufs` du v3) affirme que le rapport et la déclaration v3 n'existent pas encore : il échoue depuis que l'épreuve v3 les a écrits, pour cette seule raison (vérifié : `assert not E.RAPPORT_REEL.exists()`).

## 2. Ce qui est déjà fait (ne pas refaire)

- **Sonde d'Astra du jour** : faite le 18 novembre (`802b840e…`, « ok » vrai), citée par la pièce de départ. **Ne pas la refaire.** Vérification :
  ```
  cd /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/course-v2 && sha256sum -c sonde-astra-commune-2026-11-18-v1.json.sha256 && /usr/local/bin/python3 -I -c "import json,sys;o=json.load(open('sonde-astra-commune-2026-11-18-v1.json'));print(o['ok'],o['jour'],o['cout_usd']);sys.exit(0 if o['ok'] is True and o['jour']=='2026-11-18' else 1)"
  ```
  Attendu : `True 2026-11-18 0.00041`, code 0.
- **Relevé des prix Claude du jour** : fait et scellé (`course-v2/releve-prix-claude-course-auto-conception-v2.json`, `ed812e6a…`, relevé à 15:57:46Z : Opus 5.5 4 / 20 USD, Fable 5.1 10 / 50 USD). **Ne pas le refaire** ; le lanceur v4 l'accepte tel quel (relevé du jour).
- **Pièce de départ** : scellée (`e2689fa2…`), reprise telle quelle ; ne pas la réécrire.
- **Lignes de GO** sur `main` : `GO-2026-11-18-20` (course, 90 USD), `GO-2026-11-18-21` (épreuve, 5 USD), `GO-2026-11-18-36` (décision de reprise, échéance le 18 novembre) ; le programme d'épreuve et le lanceur les lisent eux-mêmes dans `refs/remotes/origin/main` (fetch ciblé juste avant chaque lancement).
- **Tentative v3 de l'épreuve** : 0,132289 USD (Argon seul ; 0 appel Claude). Le programme v4 la lit dans son rapport scellé et la retranche.
- **Essai à blanc et épreuve hors ligne v4** : joués par l'auteur, résultats versés (`course-v2/essai-a-blanc-v2d/`, § 11).

## 3. Contre-lecture du correctif v2d (modèle K) — avant l'épreuve

Exigée par le lanceur v4. Par un contre-lecteur neuf du modèle K, qui n'a écrit ni l'additif v2d, ni le lanceur v4, ni le programme d'épreuve v4 (R2). Fichiers à lui donner : l'additif v2d et l'additif v2c, le préenregistrement v2, `scripts/epreuve_temoins_auto_conception_v4.py` et le v3, `scripts/lancer_course_auto_conception_v4.py` et la v3, les deux fichiers d'essais v4, `course-v2/rapport-developpeur-correctif-v2d.md`, ces commandes, le rapport de la tentative v3 et sa sortie d'erreur (`course-v2/epreuve-reelle-v3-2026-11-18-v1/epreuve-reelle-v3.stderr.txt`), `rapports/fille-ideation-1-v1/appel-argon-v5.sh`, `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py` et `relais_gemini_v2.py`, et dans `«CLONE»/orchestrator` : `pole/adaptateurs.py` (`etat_bac_a_sable_detaille`, `Resultat`), `pole/adaptateurs_v56.py`. Rapport écrit et scellé à `docs/notes/organisme-auto-conception-v1/course-v2/contre-lecture-correctif-v2d-auto-conception.md` : il cite **en entier** `cb4d44d081e505dfafc2ae4552fbaa8b80e3370ea7e295966a6a1708ce512e45` (additif v2d) et `b1661f119407530b0f6e940a75e8811d6dd968fd33bfca08f7f0933ed4e8707e` (lanceur v4), se dit du modèle K, la première ligne sous « ## Verdict » est exactement « Scellable. », et il ne dit nulle part n'avoir pas relu. Une correction demandée donne de nouvelles versions (R12), donc de nouvelles empreintes : ces commandes ne valent plus.

## 4. Sonde du bac à sable (commande de l'orchestrateur), avant l'épreuve

```
cd /home/user/ideation-organism/orchestrator && env -i PATH=/usr/local/bin:/usr/bin:/bin LANG=C.UTF-8 /usr/local/bin/python3 -I -B -c "import json, sys
sys.path.insert(0, sys.argv[1])
from pole.adaptateurs import etat_bac_a_sable_detaille
print(json.dumps(etat_bac_a_sable_detaille()))" /home/user/ideation-organism/orchestrator
```
Attendu : `{"actif": true, "proc_neuf": true, "motif": "bwrap et socat présents ; …"}` (rendu ainsi par l'auteur le 18 novembre vers 16:27Z, après l'installation du bac). Sinon : arrêt (le programme d'épreuve v4 et le lanceur v4 refusent de toute façon, code 2, rien dépensé).

## 5. Épreuve réelle des témoins, reprise unique (5 USD au total, tentative v3 comprise ; 33 appels)

Vérifier qu'aucun relais ne tourne (ports 8787 à 8792) : `pgrep -af "relais_reel.py|relais_gemini|relais_kimi"` doit ne rien rendre (sinon arrêt par PID, `kill -INT «PID»`, R10, consigné). Relais **propres à l'épreuve** :

```
mkdir «D» «D»/maison && cd «D»
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-claude-epreuve.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_RIGAUD -- /usr/bin/python3 -I -B /home/user/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_RIGAUD --port 8787 --plafond-usd 5 --modeles-permis claude-fable-5-1,claude-opus-5-5 --journal «D»/journal-relais-claude-epreuve.jsonl
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-gemini-epreuve.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle GEMINI_API_KEY --port 8788 --max-appels 24 --modele gemini-4-argon --journal «D»/journal-relais-gemini-epreuve.jsonl
```
**`--max-appels 24`** = 2 × 11 jugements d'Argon (`countTokens` puis `generateContent` chacun) + 2 de marge (un jugement entier) ; le programme v4 refuse en dessous. Relever les deux PID (console de chaque relais), puis vérifier : `tr '\0' ' ' < /proc/«PID»/cmdline` (programme, port, variable, borne) ; `curl -s --noproxy '*' http://127.0.0.1:8787/relais/etat` (0 appel, plafond 5) et `curl -s --noproxy '*' http://127.0.0.1:8788/relais/etat` (0 appel, `max_appels` 24, `variable_cle_encore_presente` faux).

Déclaration de l'épreuve, **chemin neuf**, écrite avec l'outil d'écriture de fichiers puis scellée : `docs/notes/organisme-auto-conception-v1/course-v2/declaration-relais-epreuve-temoins-auto-conception-v4.json`

```json
{"version": "declaration-relais-epreuve-temoins-auto-conception-v4", "fournisseurs": {
 "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:8787", "nom_cle": "RR_ANTHROPIC_API_KEY_RIGAUD", "pid_relais": «PID_CLAUDE_EPREUVE»,
            "porte_plafond": {"type": "commande", "delai_s": 30, "commande": ["/usr/local/bin/python3", "-I", "-B",
              "/home/user/controle-ia-travail/scripts/porte_plafond_relais_v1.py", "--url", "http://127.0.0.1:8787",
              "--modeles-permis", "claude-fable-5-1,claude-opus-5-5", "--plafond-ligne", "5"]}},
 "argon": {"type": "commande_externe", "commande": ["bash", "/home/user/controle-ia-travail/rapports/fille-ideation-1-v1/appel-argon-v5.sh"],
           "nom_cle": "GEMINI_API_KEY", "pid_relais": «PID_GEMINI_EPREUVE», "url_etat_relais": "http://127.0.0.1:8788",
           "porte_plafond": {"type": "environnement"}}}}
```
```
cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-auto-conception-v1/course-v2/declaration-relais-epreuve-temoins-auto-conception-v4.json
```

Lancement (environnement **sans aucun nom de clé** ; le programme refuse sinon ; il refuse aussi si son rapport v4 existe déjà, si `GO-2026-11-18-36` manque, si le bac est inactif ou si la borne d'Argon est sous 24 — **tout cela avant tout appel**) :

```
cd /home/user/controle-ia-travail && git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
cd /home/user/controle-ia-travail && env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=«D»/maison LANG=C.UTF-8 /usr/local/bin/python3 -I -B scripts/epreuve_temoins_auto_conception_v4.py --reel > «D»/epreuve-reelle-v4.stdout.txt 2> «D»/epreuve-reelle-v4.stderr.txt; echo "code $?"
```
Codes : 0 rapport écrit (lire le verdict) ; 2 refus avant tout appel (motif sur la sortie d'erreur ; rien dépensé). Sortie : `course-v2/epreuve-temoins-reelle-auto-conception-v4.json` (scellé par le programme ; champs `verdict`, `verdict_lecture_gelee`, `incidents_techniques`, `manques_par_sorte`, `bac_a_sable`, `borne_relais_argon`, `mot_de_reprise`, `budget_reprise_usd` = 4.867711, `tentative_precedente` avec les 7 verdicts d'Argon de la v3). **Si le verdict n'est pas « réussie » (« échouée » ou « non conclue ») : arrêt, aucune course, rapport à la mère** (reprise unique : `GO-2026-11-18-36`). Puis : `curl -s --noproxy '*' http://127.0.0.1:8787/relais/etat` et `…:8788/relais/etat` (dépense, appels), arrêt des deux relais **par PID** (`kill -INT «PID»`, R10), consigner l'arrêt et la dépense, verser le rapport, sa déclaration et les deux journaux (stdout, stderr, scellés) dans `course-v2/epreuve-reelle-v4-2026-11-18-v1/`.

## 6. Relevé des crédits du jour (après l'épreuve)

Écrire puis sceller `docs/notes/organisme-auto-conception-v1/course-v2/releve-credits-avant-course-auto-conception-v2.json` (chemin inchangé, jamais écrit à ce jour). Clé Claude **non lisible** (solde illisible par l'interface) : dépense antérieure = **6,48 USD** (borne de la mère) **+ la dépense Claude de l'épreuve** (`depense_usd` lu sur `http://127.0.0.1:8787/relais/etat` avant l'arrêt du relais de l'épreuve ; la tentative v3 n'a fait aucun appel Claude) ; **ne pas retrancher** les réserves 9 + 9 USD de la pièce de départ (le lanceur les retranche lui-même). Clés d'Argon et de Carbon (`GEMINI_API_KEY`, une seule ligne) et d'Astra (`OPENAI_API_KEY`) : non lisibles, sous la **dispense écrite par la mère, référence R-3237** :

```json
{"releve_utc": "«date -u +%FT%TZ»",
 "cles": {"RR_ANTHROPIC_API_KEY_RIGAUD": {"non_lisible": true, "motif": "solde illisible ; dépense antérieure bornée par la mère (6,48 USD) plus la dépense Claude de l'épreuve v4", "depense_anterieure_usd": «6.48 + dépense Claude de l'épreuve»},
          "GEMINI_API_KEY": {"non_lisible": true, "motif": "solde illisible (R-3222)"},
          "OPENAI_API_KEY": {"non_lisible": true, "motif": "solde illisible"}},
 "dispense": {"par": "mère", "reference": "R-3237", "cles": ["GEMINI_API_KEY", "OPENAI_API_KEY"]}}
```
Compté par le lanceur : 124 USD (crédit déclaré par la pièce de départ) − dépense antérieure − 18 USD de réserves ; arrêt et alerte (code 3) si ce reste net est ≤ 90 USD ou sous un cinquième du crédit (avec 6,48 + au plus 4,87 USD : reste net ≥ 94,65 USD).

## 7. Relais neufs de la course (bornes corrigées)

Les relais de l'épreuve sont arrêtés (§ 5). Lancer, depuis `«D»` :

```
cd «D»
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-claude-course.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_RIGAUD -- /usr/bin/python3 -I -B /home/user/ideation-organism/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_RIGAUD --port 8787 --plafond-usd 90 --modeles-permis claude-fable-5-1,claude-opus-5-5 --journal «D»/journal-relais-claude-course.jsonl
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-gemini-course.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle GEMINI_API_KEY --port 8788 --max-appels 464 --modele gemini-4-argon --journal «D»/journal-relais-gemini-course.jsonl
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py > «D»/commande_astra_v1.py && echo "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71  «D»/commande_astra_v1.py" | sha256sum -c -
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-astra.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8790 --modeles-permis gpt-6-astra --plafond-usd 34 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 60 --delai-amont-s 3400 --journal «D»/journal-relais-astra.jsonl
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py > «D»/commande_gemini_lot_v1.py && echo "9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75  «D»/commande_gemini_lot_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v4.py > «D»/relais_gemini_v4.py && echo "543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4  «D»/relais_gemini_v4.py" | sha256sum -c -
cd «D» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-carbon.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B «D»/relais_gemini_v4.py --variable-cle GEMINI_API_KEY --port 8792 --modele gemini-4-carbon --max-appels 60 --max-lots 15 --journal «D»/journal-relais-carbon.jsonl
```
Bornes : **Argon `--max-appels 464`** = 2 × 231 appels d'Argon au pire (11 proposeurs + 11 cases × 5 espèces × 4 cartes × 1 juge Argon) + 2 ; le lanceur v4 refuse en dessous (la borne 280 des commandes v2c aurait coupé la course vers le 140e appel d'Argon). **Carbon** `--max-appels 60` ≥ 24 (2 × 11 + 2 : `countTokens` puis `batchGenerateContent` par case) et `--max-lots 15` ≥ 11 ; ses relevés de lot ont leur propre borne (`--max-releves`, 2 000 par défaut ; au plus ≈ 51 par case). **Astra** : une requête par appel, `--max-appels 60` ≥ 11. Vérifier chaque relais par PID (`tr '\0' ' ' < /proc/«PID»/cmdline`) et `curl -s --noproxy '*' http://127.0.0.1:«PORT»/relais/etat` sur 8787, 8788, 8790, 8792 : **0 appel** partout (0 lot pour Carbon), plafond 90 (Claude), `max_appels` 464 (Argon), variable de clé effacée (Gemini) ; sinon le lanceur refuse. Kimi n'est pas déclaré (aucun relais 8789).

## 8. Déclaration des relais de la course (chemin neuf, v4)

Écrire (outil d'écriture de fichiers), puis sceller, `docs/notes/organisme-auto-conception-v1/course-v2/declaration-relais-course-auto-conception-v4.json` (`«D»` écrit en chemin absolu, `/home/user/execution-auto-conception-v2d`) :

```json
{"version": "declaration-relais-course-auto-conception-v4", "fournisseurs": {
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
```
cd /home/user/controle-ia-travail && PYTHONPATH=src /usr/local/bin/python3 -B -m controle_ia.scellement sceller docs/notes/organisme-auto-conception-v1/course-v2/declaration-relais-course-auto-conception-v4.json
```

## 9. Lancement de la course (plafond d'arrêt 90 USD), avant minuit UTC

Seulement si l'épreuve v4 a rendu « réussie » et que la contre-lecture du § 3 est scellée « Scellable. ». La variable `RR_ANTHROPIC_API_KEY_RIGAUD` présente dans l'environnement du lanceur (il la teste par son nom, ne lit jamais sa valeur et la retire de l'environnement de l'orchestrateur) :

```
cd /home/user/controle-ia-travail && git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
cd /home/user/controle-ia-travail && GO_ID=GO-2026-11-18-20 /usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v4.py
```
Le lanceur exige, dans l'ordre : aucune course déjà lancée (v1 à v4), pièce de départ, GO `GO-2026-11-18-20` (registre au commit de `main`), préenregistrement `0d51e0b3…`, pièces épinglées (dont le programme d'épreuve v4 `04f62b8c…`), **additif v2d `cb4d44d0…`** (qui cite l'additif v2c), **contre-lecture du § 3**, matière, **rapport d'épreuve v4 « réussie » du jour** (verdict recalculé par la lecture gelée et la requalification du v4), déclaration du § 8, relevés des prix (§ 2) et des crédits (§ 6), relais (**Argon ≥ 464**, Carbon ≥ 24 appels et ≥ 11 lots), orchestrateur, bac à sable, vérification de l'orchestrateur, porte à blanc. Sortie hors dépôt : `/home/user/sorties-course-auto-conception-v4/«id»/` ; dossier du run au dépôt : `runs/«id»-course-auto-conception-v4/`. Codes : **0** fini ; **2** refus ou arrêt (motif sur la sortie d'erreur) ; **3** alerte de crédit avant le départ (fichier scellé pour la mère) ; **4** cumul au-dessus de 90 USD ; **5** arrêt au premier refus pour crédit d'un relais dispensé. Carbon par lot : jusqu'à ≈ 30 minutes par appel, plusieurs heures au pire pour ses onze cases.

## 10. Après

Lire `/relais/etat` de chaque relais (8787, 8788, 8790, 8792 : dépense, appels), les arrêter **par PID** (`kill -INT «PID»`, R10), consigner chaque arrêt et la dépense ; verser `runs/«id»-course-auto-conception-v4/` (manifestes de départ et de fin, acte de gel, configuration, lots, registre dérivé, alertes éventuelles) ; **ne lire aucune carte** : la lecture est à la mère. Code 2 avec un nœud C13 (étape non mesurée) : issue rapportée, tentative consommée, aucune relance sans version neuve et mot de la mère. Code 3, 4 ou 5 : alerte scellée transmise à la mère, qui prévient Lazar.

## 11. Essai à blanc et épreuve hors ligne (déjà joués par l'auteur, à rejouer si l'on veut, dossiers neufs)

```
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md > «DOSSIER_NEUF»-matiere-premiere-v3.md
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v4.py --a-blanc «DOSSIER_NEUF»/a-blanc
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/epreuve_temoins_auto_conception_v4.py --hors-ligne «DOSSIER_NEUF»/epreuve-hors-ligne --matiere «DOSSIER_NEUF»-matiere-premiere-v3.md
```
Résultats versés : `course-v2/essai-a-blanc-v2d/` (moteur simulé, code 0, 88 cartes à passeport, additif v2d et lanceur v4 cités par l'acte de gel et le manifeste, borne de relais d'Argon de l'essai 376 = 2 × 187 + 2 avec Kimi factice ; épreuve hors ligne v4 : « témoins éprouvés hors ligne », 0 juge au hasard réussi sur 2 000).

## 12. Réserves

- La requalification « non conclue » ne vaut que si **tous** les manques sont techniques (statut d'adaptateur « erreur » ou appel non parti) ; un statut « refus » (refus ou changement de modèle), « budget_depasse », « tours_epuises » ou une réponse lue illisible reste un échec. Toute commande externe qui sort avec un code non nul (refus du relais, garde de pire cas de la commande d'Argon, réseau) rend le statut « erreur » (`«CLONE»/orchestrator/pole/adaptateurs.py`, l. 751-760, lu) et compte donc comme technique, sauf si sa dernière ligne signale un changement de modèle (statut « refus », non technique).
- Argon et Carbon partagent `GEMINI_API_KEY` : relevé écrit une fois, sous dispense ; le lanceur confronte chaque relais à sa part séparément.
- La sonde du bac prouve que bwrap et socat s'exécutent et qu'un `/proc` neuf se monte ; l'application du bac par le kit reste la garde de l'orchestrateur (échec dur s'il manque).
- La sonde d'Astra n'est valable que le 18 novembre 2026.
