# Commandes exactes — course d'auto-conception de l'organisme d'idéation, v1 (pour la session d'exécution)

Écrites par la session du compte organisme (modèle I). **Rien n'a été lancé par l'auteur** : moteur simulé, relais factices et appels directs des gardes seulement. Les emplacements `«…»` sont à remplir par la mère ou par la session d'exécution ; aucune valeur de clé n'est écrite nulle part (noms de variables seulement).

## 0. Empreintes (à vérifier avant tout)

| pièce | sha256 |
|---|---|
| `scripts/lancer_course_auto_conception_v1.py` (lanceur, à citer par la contre-lecture) | `78f42af1a445ea9dcd21a51e1f29bb50820ee94987b94cf435e10473a815009f` |
| `course-v1/preenregistrement-course-auto-conception-v1.md` (épinglé dans le lanceur) | `cef7ce8b397c9ed53f08cdde870c22838ba600e5f20870ae28fa78703a2677e0` |
| `scripts/epreuve_temoins_auto_conception_v1.py` | `5e354e7d2bd6d5e3f1b02f9b9594d615299604c63c77a698b2d0cdb8da30c975` |
| `scripts/garde_credit_relais_v5.py` | `6cf8786943bb6c9e51dd6909714e83de783e70dffc80ea1fad46a0e1545d30cd` |
| `tests/test_lancer_course_auto_conception_v1.py` | `75b8992bf0504bbfe7849dd688abd1b6471542df2ddeb8587c80bfa33562b945` |
| matière servie `docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md` (sur `main`) | `11f4b69ba42147c428090e4805948a708d0ed266da0c0cd07f194723eaba742d` |

```
cd /home/user/controle-ia-travail
for f in scripts/lancer_course_auto_conception_v1.py scripts/epreuve_temoins_auto_conception_v1.py scripts/garde_credit_relais_v5.py docs/notes/organisme-auto-conception-v1/course-v1/preenregistrement-course-auto-conception-v1.md; do (cd "$(dirname "$f")" && sha256sum -c "$(basename "$f").sha256"); done
git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
git show refs/remotes/origin/main:docs/notes/matiere-premiere-auto-conception-v1/matiere-premiere-v3.md | sha256sum
PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B -m pytest -q -p no:cacheprovider tests/test_lancer_course_auto_conception_v1.py
```
Attendu : toutes les empreintes « OK », la matière à `11f4b69b…`, 69 essais passés. Le registre des GO et la matière sont lus par le lanceur dans `refs/remotes/origin/main` (le fetch ciblé est donc exigé juste avant chaque lancement, après l'inscription des deux lignes de GO).

## 1. Emplacements à remplir par la mère (avant tout appel)

1. **Deux lignes de GO** demandées à Lazar et inscrites dans `registres/go.md` sur `main` (type `calcul`, accordées par `Lazar`, période qui couvre le jour du lancement) :
   - la course : périmètre qui contient « auto-conception » (par exemple « course d'auto-conception de l'organisme d'idéation, devis v1 »), plafond **`90 USD`** exactement ;
   - l'épreuve réelle des témoins : périmètre qui contient « témoins » (par exemple « épreuve des témoins du juge de la course d'auto-conception »), plafond **`5 USD`** exactement.
2. **Pièce de départ** : recopier `course-v1/piece-de-depart-gabarit-auto-conception-v1.json` en `course-v1/piece-de-depart-auto-conception-v1.json`, remplir chaque « À REMPLIR » (identifiants des deux GO ; **nom de la variable de la clé Claude** de cette course, `RR_ANTHROPIC_API_KEY_…`, jamais Minuit ; crédit déclaré de cette clé ; réserve à garder sur la clé de Kimi ; commandes d'Astra et de Carbon **seulement si** elles sont épinglées et éprouvées, sinon retirer leurs clés), sceller (`PYTHONPATH=src python3 -m controle_ia.scellement sceller …`), verser.
3. **Contre-lecture** du modèle K, scellée à `course-v1/contre-lecture-preenregistrement-course-auto-conception-v1.md` : elle cite `cef7ce8b…` (préenregistrement) et `78f42af1…` (lanceur), se dit du modèle K, et la première ligne sous « ## Verdict » est exactement « Scellable. ».
4. Session d'exécution neuve, sur `lot/compte-organisme-v1` au commit versé ou plus récent, garde de calcul chargée, variable de la clé Claude nommée par la pièce présente dans son environnement, clone de l'orchestrateur au commit `a41b7b50` propre (une seule des deux copies candidates du lanceur), relais lancés selon `docs/procedures/relais-persistants-v1.md`.

## 2. Épreuve réelle des témoins (avant la course ; plafond 5 USD ; 33 appels)

Relais **propres à l'épreuve** (la porte à blanc de la course exige ensuite des relais neufs). `«D»` = un dossier hors dépôt neuf ; `«CLE_CLAUDE»` = le nom de la pièce de départ ; `«CLE_ARGON»` = nom de la variable de la clé Gemini.

```
mkdir «D» && cd «D»
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-claude-epreuve.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!«CLE_CLAUDE» -- /usr/bin/python3 -I -B «CLONE»/orchestrator/pole/relais_reel.py --variable-cle «CLE_CLAUDE» --port 8787 --plafond-usd 5 --modeles-permis claude-fable-5-1,claude-opus-5-5 --journal «D»/journal-relais-claude-epreuve.jsonl
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-gemini-epreuve.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!«CLE_ARGON» -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --variable-cle «CLE_ARGON» --port 8788 --max-appels 11 --modele gemini-4-argon --journal «D»/journal-relais-gemini-epreuve.jsonl
```
Vérifier (procédure § 3) : `tr '\0' ' ' < /proc/«PID»/cmdline`, puis `GET /relais/etat` sur 8787 et 8788 : 0 appel, plafond 5 (Claude), variable de clé effacée (Gemini).

Déclaration de l'épreuve, scellée, à `course-v1/declaration-relais-epreuve-temoins-auto-conception-v1.json` (Claude et Argon seulement) :

```json
{"version": "declaration-relais-epreuve-temoins-auto-conception-v1", "fournisseurs": {
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
env -i PATH=/usr/local/bin:/usr/bin:/bin HOME=«D»/maison LANG=C.UTF-8 /usr/local/bin/python3 -I -B scripts/epreuve_temoins_auto_conception_v1.py --reel
```
Sortie : `course-v1/epreuve-temoins-reelle-auto-conception-v1.json` (scellé). **Si le verdict n'est pas « réussie » : arrêt, aucune course, rapport à la mère** (aucune retouche des témoins sans version neuve). Puis lire `/relais/etat` des deux relais, les arrêter par PID (`kill -INT «PID»`, R10), consigner la dépense, verser le rapport.

## 3. La course (plafond d'arrêt 90 USD)

1. Relevé des prix Claude **du jour**, scellé, à `course-v1/releve-prix-claude-course-auto-conception-v1.json` (comparé au barème du relais : entrée/sortie 4/20 et 10/50) :
   `{"releve_utc": "«date -u»", "source": "«page des prix lue»", "prix": {"espece_claude_1": {"entree": 4.0, "sortie": 20.0}, "espece_claude_2": {"entree": 10.0, "sortie": 50.0}}}`
2. Relevé des crédits **du jour**, scellé, à `course-v1/releve-credits-avant-course-auto-conception-v1.json` (noms seulement) :
   `{"releve_utc": "«date -u»", "cles": {"«CLE_CLAUDE»": {"credit_usd": «c», "reste_usd": «r», "source": "…"} ou {"non_lisible": true, "depense_anterieure_usd": «d»}, "«CLE_ARGON»": {"non_lisible": true, "motif": "solde illisible (R-3222)"}, "«CLE_KIMI»": {"credit_usd": «c», "reste_usd": «r», "source": "solde Moonshot"}}, "dispense": {"par": "mère", "reference": "R-3237", "cles": ["«CLE_ARGON»"]}}`
3. Relais **neufs** (ceux de l'épreuve sont arrêtés) : Claude `--plafond-usd 90 --modeles-permis claude-fable-5-1,claude-opus-5-5` (port 8787) ; Gemini v2 `--max-appels 200` (port 8788 ; au pire 187 appels avec Kimi) ; Kimi si activé (procédure § 2.2, port 8789, `--plafond-usd 6`), mêmes commandes qu'au § 2 sinon.
4. Déclaration de la course, scellée, à `course-v1/declaration-relais-course-auto-conception-v1.json` : même forme qu'au § 2 avec `"--plafond-ligne", "90"` pour la porte Claude et les PID des relais neufs ; Kimi, s'il est activé :
   `"kimi": {"type": "kimi_protocole", "url_relais": "http://127.0.0.1:8789", "modele": "kimi-k3.1-pro", "prix_entree": 2.0, "prix_sortie": 10.0, "max_sortie_jetons": 16000, "sortie_min_jetons": 1000, "delai_s": 1800, "nom_cle": "«CLE_KIMI»", "pid_relais": «PID_KIMI», "porte_plafond": {"type": "commande", "delai_s": 30, "commande": ["/usr/local/bin/python3", "-I", "-B", "/home/user/controle-ia-travail/scripts/porte_plafond_relais_v1.py", "--url", "http://127.0.0.1:8789", "--modeles-permis", "kimi-k3.1-pro", "--plafond-ligne", "6"]}}`
   Astra et Carbon : seulement si la pièce de départ épingle leur commande (`"commande": [...]`, `"modele_propose"`, `"porte_plafond": {"type": "environnement"}`).
5. Lancement (la variable de la clé Claude présente dans l'environnement du lanceur, qui la teste par son nom et la retire de l'environnement de l'orchestrateur) :
   ```
   cd /home/user/controle-ia-travail
   git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
   GO_ID=«GO de la course» /usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v1.py
   ```
   Codes : 0 fini ; 2 refus ou arrêt (motif sur la sortie d'erreur) ; 3 alerte de crédit avant le départ (fichier scellé pour la mère) ; 4 cumul au-dessus de 90 ; 5 arrêt au premier refus pour crédit.
6. Après : lire `/relais/etat` de chaque relais, les arrêter par PID, consigner ; verser `runs/«id»-course-auto-conception-v1/` ; ne lire aucune carte : la lecture est à la mère.

## 4. Essai à blanc (déjà joué par l'auteur, à rejouer si l'on veut)

```
/usr/local/bin/python3 -I -B scripts/lancer_course_auto_conception_v1.py --a-blanc «DOSSIER_NEUF»
/usr/local/bin/python3 -I -B scripts/epreuve_temoins_auto_conception_v1.py --hors-ligne «DOSSIER_NEUF» --matiere «matiere-premiere-v3.md»
```
Résultats versés : `course-v1/essai-a-blanc-v1/` (moteur simulé, 11 cases × 4 espèces, 88 cartes à passeport, étapes conformes, code 0) et `course-v1/epreuve-temoins-hors-ligne-v1/`.
