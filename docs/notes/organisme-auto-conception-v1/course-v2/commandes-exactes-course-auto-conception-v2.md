# Commandes exactes — course d'auto-conception de l'organisme d'idéation, v2 (pour la session d'exécution)

Écrites par la session du compte organisme (modèle I). **Version 2** : remplace la v1 (`course-v1/commandes-exactes-course-auto-conception-v1.md`, qui reste en place) ; contre-lecture de la v1 portée (constats 1 et 10 ici) ; données de la mère (R-3271) écrites. **Rien n'a été lancé par l'auteur** : moteur simulé, relais factices et appels directs des gardes seulement. Les emplacements `«…»` sont à remplir par la mère ou par la session d'exécution ; aucune valeur de clé n'est écrite nulle part (noms de variables seulement).

## 0. Empreintes (à vérifier avant tout)

| pièce | sha256 |
|---|---|
| `scripts/lancer_course_auto_conception_v2.py` (lanceur, à citer par la contre-lecture) | `d8fbb42aca76a870b36094b43a696e10ffce1b176837af55e326373ef587c5ed` |
| `course-v2/preenregistrement-course-auto-conception-v2.md` (épinglé dans le lanceur) | `0d51e0b3f51dd731351589187c124b7ee1a6237494aa0274825b19085c6763c6` |
| `scripts/epreuve_temoins_auto_conception_v2.py` | `19d03876a1b65557d20bf23bdbbf9c657ef726a2be16168fcf78a838f2eac536` |
| `scripts/garde_credit_relais_v5.py` (inchangée) | `6cf8786943bb6c9e51dd6909714e83de783e70dffc80ea1fad46a0e1545d30cd` |
| `tests/test_lancer_course_auto_conception_v2.py` | `cdb1817755ba3a7417f1055b020e735135a3a514632285ab96ea27bec091f5f3` |
| commande d'Astra `docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py` (sur `main`) | `986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71` |
| commande de Carbon par lot `docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py` (sur `main`) | `9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75` |
| relais Gemini v4 `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v4.py` (sur `main`) | `543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4` |
| matière servie `docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md` (sur `main`) | `11f4b69ba42147c428090e4805948a708d0ed266da0c0cd07f194723eaba742d` |

```
cd /home/user/controle-ia-travail
for f in scripts/lancer_course_auto_conception_v2.py scripts/epreuve_temoins_auto_conception_v2.py scripts/garde_credit_relais_v5.py docs/notes/organisme-auto-conception-v1/course-v2/preenregistrement-course-auto-conception-v2.md; do (cd "$(dirname "$f")" && sha256sum -c "$(basename "$f").sha256"); done
git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
git show refs/remotes/origin/main:docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md | sha256sum
PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B -m pytest -q -p no:cacheprovider tests/test_lancer_course_auto_conception_v2.py
```
Attendu : toutes les empreintes « OK », la matière à `11f4b69b…`, 83 essais passés. Le registre des GO et la matière sont lus par le lanceur dans `refs/remotes/origin/main` (le fetch ciblé est donc exigé juste avant chaque lancement, après l'inscription des deux lignes de GO).

## 1. Emplacements à remplir par la mère (avant tout appel)

1. **Deux lignes de GO** demandées à Lazar et inscrites dans `registres/go.md` sur `main` (type `calcul`, accordées par `Lazar`, période qui couvre le jour du lancement) :
   - la course : périmètre qui contient « auto-conception » (par exemple « course d'auto-conception de l'organisme d'idéation, devis v2 »), plafond **`90 USD`** exactement ;
   - l'épreuve réelle des témoins : périmètre qui contient « témoins » (par exemple « épreuve des témoins du juge de la course d'auto-conception »), plafond **`5 USD`** exactement.
2. **Pièce de départ** : recopier `course-v2/piece-de-depart-gabarit-auto-conception-v2.json` en `course-v2/piece-de-depart-auto-conception-v2.json` ; déjà pré-remplis (R-3271) : clé Claude `RR_ANTHROPIC_API_KEY_RIGAUD`, crédit déclaré 124 USD, réserves 9 (course Carbon) et 9 (étape 3 d'E5), réserve Moonshot 15 USD, empreintes des commandes d'Astra et de Carbon ; à remplir : les deux GO, l'heure, la référence de l'épreuve de chaque commande gardée (ou retirer sa clé) ; **décider des espèces optionnelles** (`especes_optionnelles` : par défaut toutes `declaree: false` ; Kimi par défaut non déclaré, relais de Moonshot vu surchargé ; une espèce déclarée exige `risque_accepte: true` et `sonde_du_jour`, car une espèce déclarée qui échoue rend l'étape non mesurée et consomme la tentative) ; sceller (`PYTHONPATH=src python3 -m controle_ia.scellement sceller …`), verser.
3. **Contre-lecture** du modèle K, scellée à `course-v2/contre-lecture-preenregistrement-course-auto-conception-v2.md` : elle cite `0d51e0b3…` (préenregistrement) et `d8fbb42a…` (lanceur) en entier, se dit du modèle K, et la première ligne sous « ## Verdict » est exactement « Scellable. ».
4. Session d'exécution neuve, sur `lot/compte-organisme-v1` au commit versé ou plus récent, garde de calcul chargée, variable de la clé Claude nommée par la pièce présente dans son environnement, clone de l'orchestrateur au commit `a41b7b50` propre (une seule des deux copies candidates du lanceur), relais lancés selon `docs/procedures/relais-persistants-v1.md`.

## 2. Épreuve réelle des témoins (avant la course ; plafond 5 USD ; 33 appels)

Relais **propres à l'épreuve** (la porte à blanc de la course exige ensuite des relais neufs). `«D»` = un dossier hors dépôt neuf ; `«CLE_CLAUDE»` = le nom de la pièce de départ ; `«CLE_ARGON»` = nom de la variable de la clé Gemini.

```
mkdir «D» && cd «D»
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-claude-epreuve.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!«CLE_CLAUDE» -- /usr/bin/python3 -I -B «CLONE»/orchestrator/pole/relais_reel.py --variable-cle «CLE_CLAUDE» --port 8787 --plafond-usd 5 --modeles-permis claude-fable-5-1,claude-opus-5-5 --journal «D»/journal-relais-claude-epreuve.jsonl
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-gemini-epreuve.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!«CLE_ARGON» -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle «CLE_ARGON» --port 8788 --max-appels 15 --modele gemini-4-argon --journal «D»/journal-relais-gemini-epreuve.jsonl
```
Vérifier (procédure § 3) : `tr '\0' ' ' < /proc/«PID»/cmdline`, puis `GET /relais/etat` sur 8787 et 8788 : 0 appel, plafond 5 (Claude), variable de clé effacée (Gemini).

(`--max-appels 15` : 11 appels nécessaires, marge de reprise — constat 10 ; « non conclue » reste un arrêt.)

Déclaration de l'épreuve, scellée, à `course-v2/declaration-relais-epreuve-temoins-auto-conception-v2.json` (Claude et Argon seulement) :

```json
{"version": "declaration-relais-epreuve-temoins-auto-conception-v2", "fournisseurs": {
 "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:8787", "nom_cle": "«CLE_CLAUDE»", "pid_relais": «PID_CLAUDE»,
            "porte_plafond": {"type": "commande", "delai_s": 30, "commande": ["/usr/local/bin/python3", "-I", "-B",
              "/home/user/controle-ia-travail/scripts/porte_plafond_relais_v1.py", "--url", "http://127.0.0.1:8787",
              "--modeles-permis", "claude-fable-5-1,claude-opus-5-5", "--plafond-ligne", "5"]}},
 "argon": {"type": "commande_externe", "commande": ["bash", "/home/user/controle-ia-travail/rapports/fille-ideation-1-v1/appel-argon-v5.sh"],
           "nom_cle": "«CLE_ARGON»", "pid_relais": «PID_GEMINI», "url_etat_relais": "http://127.0.0.1:8788",
           "porte_plafond": {"type": "environnement"}}}}
```

Lancement (environnement sans aucun nom de clé : le programme le refuse sinon) :

```
cd /home/user/controle-ia-travail
env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=«D»/maison LANG=C.UTF-8 /usr/local/bin/python3 -I -B scripts/epreuve_temoins_auto_conception_v2.py --reel
```
Sortie : `course-v2/epreuve-temoins-reelle-auto-conception-v2.json` (scellé ; verdicts et classes bruts gardés : le lanceur recalcule le verdict). **Si le verdict n'est pas « réussie » : arrêt, aucune course, rapport à la mère** (aucune retouche des témoins sans version neuve). Puis lire `/relais/etat` des deux relais, les arrêter par PID (`kill -INT «PID»`, R10), consigner la dépense, verser le rapport.

## 3. La course (plafond d'arrêt 90 USD)

1. Relevé des prix Claude **du jour**, scellé, à `course-v2/releve-prix-claude-course-auto-conception-v2.json` (comparé au barème du relais : entrée/sortie 4/20 et 10/50) :
   `{"releve_utc": "«date -u»", "source": "«page des prix lue»", "prix": {"espece_claude_1": {"entree": 4.0, "sortie": 20.0}, "espece_claude_2": {"entree": 10.0, "sortie": 50.0}}}`
2. Relevé des crédits **du jour**, **après l'épreuve des témoins**, scellé, à `course-v2/releve-credits-avant-course-auto-conception-v2.json` (noms seulement ; pour la clé Claude, le lanceur retranche lui-même les réserves de la pièce de départ, 9 + 9 USD, du reste lu ou compté : ne pas les retrancher deux fois) :
   `{"releve_utc": "«date -u»", "cles": {"«CLE_CLAUDE»": {"credit_usd": «c», "reste_usd": «r», "source": "…"} ou {"non_lisible": true, "depense_anterieure_usd": «d»}, "«CLE_ARGON»": {"non_lisible": true, "motif": "solde illisible (R-3222)"}, "«CLE_KIMI»" (seulement si Kimi est déclaré) : {"credit_usd": «c», "reste_usd": «r», "source": "solde Moonshot"}}, "dispense": {"par": "mère", "reference": "R-3237", "cles": ["«CLE_ARGON»"]}}`
3. Relais **neufs** (ceux de l'épreuve sont arrêtés) : Claude `--plafond-usd 90 --modeles-permis claude-fable-5-1,claude-opus-5-5` (port 8787) ; Gemini v2 `--max-appels 280` (port 8788 ; au pire 143 appels par défaut, 275 avec toutes les espèces, quatre cartes par appel) ; mêmes commandes qu'au § 2 sinon.
   - **Kimi : voir le préenregistrement, section Espèces ; par défaut non déclaré** (relais de Moonshot vu surchargé). Seulement si la pièce de départ le déclare : procédure § 2.2, port 8789, `--plafond-usd 6`.
   - **Astra** (seulement si la pièce de départ la déclare) : extraire la commande hors dépôt et vérifier son empreinte, puis lancer son relais :
     ```
     git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py > «D»/commande_astra_v1.py && sha256sum «D»/commande_astra_v1.py   # 986cf71e…
     /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-astra.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8790 --modeles-permis gpt-6-astra --plafond-usd 34 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 60 --delai-amont-s 3400 --journal «D»/journal-relais-astra.jsonl
     ```
   - **Carbon** (seulement si la pièce de départ la déclare) : extraire la commande par lot et le relais v4 hors dépôt, vérifier leurs empreintes, lancer le relais :
     ```
     git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py > «D»/commande_gemini_lot_v1.py && sha256sum «D»/commande_gemini_lot_v1.py   # 9484dce0…
     git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v4.py > «D»/relais_gemini_v4.py && sha256sum «D»/relais_gemini_v4.py   # 543e728d…
     /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-carbon.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!«CLE_CARBON» -- /usr/bin/python3 -I -B «D»/relais_gemini_v4.py --variable-cle «CLE_CARBON» --port 8792 --modele «MODELE_CARBON» --max-appels 60 --max-lots 15 --journal «D»/journal-relais-carbon.jsonl
     ```
     (`«MODELE_CARBON»` : l'identifiant de R-3266, qui contient « carbon ».)
4. Déclaration de la course, scellée, à `course-v2/declaration-relais-course-auto-conception-v2.json` : même forme qu'au § 2 avec `"--plafond-ligne", "90"` pour la porte Claude et les PID des relais neufs ; Kimi, s'il est activé :
   `"kimi": {"type": "kimi_protocole", "url_relais": "http://127.0.0.1:8789", "modele": "kimi-k3.1-pro", "prix_entree": 2.0, "prix_sortie": 10.0, "max_sortie_jetons": 16000, "sortie_min_jetons": 1000, "delai_s": 1800, "nom_cle": "«CLE_KIMI»", "pid_relais": «PID_KIMI», "porte_plafond": {"type": "commande", "delai_s": 30, "commande": ["/usr/local/bin/python3", "-I", "-B", "/home/user/controle-ia-travail/scripts/porte_plafond_relais_v1.py", "--url", "http://127.0.0.1:8789", "--modeles-permis", "kimi-k3.1-pro", "--plafond-ligne", "6"]}}`
   Astra et Carbon (seulement si la pièce de départ les déclare) :
   `"astra": {"type": "commande_externe", "commande": ["/usr/local/bin/python3", "-I", "-B", "«D»/commande_astra_v1.py", "--url-relais", "http://127.0.0.1:8790", "--modele", "gpt-6-astra", "--prix-entree", "10", "--prix-sortie", "50"], "modele_propose": "gpt-6-astra", "nom_cle": "OPENAI_API_KEY", "pid_relais": «PID_ASTRA», "url_etat_relais": "http://127.0.0.1:8790", "porte_plafond": {"type": "environnement"}}`
   `"carbon": {"type": "commande_externe", "commande": ["/usr/local/bin/python3", "-I", "-B", "«D»/commande_gemini_lot_v1.py", "--url-base", "http://127.0.0.1:8792/v1beta", "--modele", "«MODELE_CARBON»", "--prix-entree", "8.3", "--prix-sortie", "41.5"], "modele_propose": "«MODELE_CARBON»", "nom_cle": "«CLE_CARBON»", "pid_relais": «PID_CARBON», "url_etat_relais": "http://127.0.0.1:8792", "porte_plafond": {"type": "environnement"}}`
   Le lanceur vérifie : mot de la mère dans la pièce de départ, empreinte de la commande, relais par PID (programme épinglé, port, `--amont` et `--modeles-permis` pour Astra, `--modele` pour Carbon), état neuf. Carbon par lot : jusqu'à ≈ 30 minutes par appel (délai de la commande), soit plusieurs heures au pire pour ses onze cases.
5. Lancement (la variable de la clé Claude présente dans l'environnement du lanceur, qui la teste par son nom et la retire de l'environnement de l'orchestrateur) :
   ```
   cd /home/user/controle-ia-travail
   git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
   GO_ID=«GO de la course» /usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v2.py
   ```
   Codes : 0 fini ; 2 refus ou arrêt (motif sur la sortie d'erreur) ; 3 alerte de crédit avant le départ (fichier scellé pour la mère) ; 4 cumul au-dessus de 90 ; 5 arrêt au premier refus pour crédit.
6. Après : lire `/relais/etat` de chaque relais, les arrêter par PID, consigner ; verser `runs/«id»-course-auto-conception-v2/` ; ne lire aucune carte : la lecture est à la mère. Code 2 avec un nœud C13 (étape non mesurée) : issue rapportée, tentative consommée, aucune relance sans version neuve.

## 4. Essai à blanc (déjà joué par l'auteur, à rejouer si l'on veut)

```
/usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v2.py --a-blanc «DOSSIER_NEUF»
/usr/local/bin/python3 -I -B scripts/epreuve_temoins_auto_conception_v2.py --hors-ligne «DOSSIER_NEUF» --matiere «matiere-premiere-v3.md»
```
Résultats versés : `course-v2/essai-a-blanc-v2/` (moteur simulé, 11 cases × 4 espèces — Kimi déclaré par la pièce d'essai —, 88 cartes à passeport, étapes conformes, 3 expurgations dans les lots, code 0) et `course-v2/epreuve-temoins-hors-ligne-v2/`.
