# Commandes exactes — course d'auto-conception de l'organisme d'idéation, v2b : Astra et Carbon déclarés (pour la session d'exécution)

Écrites le 18 novembre 2026 par la session du compte organisme (modèle I). **Version 2b** (R12) : remplace, pour la composition, les commandes v2 (`commandes-exactes-course-auto-conception-v2.md`, `c6844ec6…`, qui restent en place). Fondement : mot du directeur tapé dans la session du compte organisme vers 10:50Z, « je veux astra et carbon dans la course debugge » — **Astra et Carbon sont déclarés** (non facultatifs) ; Kimi reste non déclaré (R-3273). **Le lanceur v2 (`d8fbb42a…`) et le préenregistrement v2 (`0d51e0b3…`) ne changent pas** : le lanceur accepte ce cas tel quel (essais ci-dessous ; contre-lecture v2, constat 1). **Rien n'a été lancé par l'auteur** : relais factices (code du relais épinglé servi dans le processus de l'essai, devant un faux amont local), moteur simulé, appels directs des gardes. Aucune valeur de clé n'est écrite (noms de variables seulement). `«J»` = la date du jour (`date -u +%F`) ; `«D»` = un dossier hors dépôt neuf.

## 0. Ce qui change depuis la v2

1. **Sonde d'Astra corrigée** (§ 2) : relais jeté avec `--reserve-par-appel 0.01` (le défaut du relais, 0,40 USD, au-dessus de son plafond de 0,05 USD, rendait le 402 certain) ; commande appelée avec `PLAFOND_SESSION_USD=0.05`, `--max-sortie-jetons 4096 --sortie-min-jetons 16` (par défaut, la commande refusait au code 4) ; programme neuf `scripts/sonde_astra_courses_v1.py`, commun aux deux courses (un seul appel le même jour sert aussi l'affinage v6).
2. **Pièce de départ** : gabarit neuf `course-v2/piece-de-depart-gabarit-auto-conception-v2b.json`, Astra et Carbon `declaree: true`, `risque_accepte: true`, mot du directeur dans `fondement`, R-3274 pour Carbon, sonde du jour pour Astra.
3. Relais d'Astra et de Carbon **toujours** lancés (§ 3) ; déclaration des relais avec les blocs d'Astra et de Carbon (§ 4).
4. Devis : `devis-course-auto-conception-v2b.md` (composition « + Astra + Carbon » du devis v2 : 39,62 USD estimés, 121,10 au haut ; plafond d'arrêt 90 inchangé).

## 1. Empreintes (à vérifier avant tout)

| pièce | sha256 |
|---|---|
| `scripts/lancer_course_auto_conception_v2.py` (inchangé) | `d8fbb42aca76a870b36094b43a696e10ffce1b176837af55e326373ef587c5ed` |
| `course-v2/preenregistrement-course-auto-conception-v2.md` (inchangé) | `0d51e0b3f51dd731351589187c124b7ee1a6237494aa0274825b19085c6763c6` |
| `course-v2/contre-lecture-preenregistrement-course-auto-conception-v2.md` (« Scellable. ») | `124ec73ce3fbb18b9256eb636031b4809d772f13bfe799e30a62c2e728f16166` |
| `scripts/sonde_astra_courses_v1.py` (neuf) | `d374d1071f4ef70b3604d97dc62e2f14103c440a166342b330d7a576d8b4c777` |
| `scripts/sonde_astra_affinage_v2.py` (épinglée par la sonde commune, inchangée) | `1799449269e15661b92f2a45eaab95a22e3a766a1fdf10ec9a4648bbe92aebf7` |
| `tests/test_sonde_astra_courses_v1.py` (neuf, 14 essais) | `0ff8ba72d999d9fd97d08707b7cc9fe91b9ce7a17bf9b42918e2f76c8189fefd` |
| `tests/test_astra_carbon_declares_auto_conception_v2b.py` (neuf, 11 essais) | `ce5a8f209772f3e2ee638c3b5d7a7ead6a70d5f4276c0ab180a8857658457958` |
| `course-v2/piece-de-depart-gabarit-auto-conception-v2b.json` (neuf) | `21ad19fee6df9d12607698a8ddefa4292ecbd080acac3c7a4d8e6480b15406b2` |
| relais compatible OpenAI `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py` | `67f369518102b3f7408f28dab053a4d6f9bc2b676eadfaa338f55d39af99027e` |
| commande d'Astra (sur `main`) | `986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71` |
| commande de Carbon par lot (sur `main`) | `9484dce066514185dc1155d5c8dcff44b256fdf835b371b59ebdffa1d50bad75` |
| relais Gemini v4 (sur `main`) | `543e728d90e809c661fdc26f1e1b1a32b2e23128a7d09e3b5d16f851408a35b4` |

```
cd /home/user/controle-ia-travail && git fetch -q --depth=1 origin +refs/heads/main:refs/remotes/origin/main
cd /home/user/controle-ia-travail && for f in scripts/lancer_course_auto_conception_v2.py scripts/sonde_astra_courses_v1.py scripts/sonde_astra_affinage_v2.py docs/notes/organisme-auto-conception-v1/course-v2/preenregistrement-course-auto-conception-v2.md docs/notes/organisme-auto-conception-v1/course-v2/piece-de-depart-gabarit-auto-conception-v2b.json docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py; do (cd "$(dirname "$f")" && sha256sum -c "$(basename "$f").sha256"); done
cd /home/user/controle-ia-travail && PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B -m pytest -q -p no:cacheprovider tests/test_lancer_course_auto_conception_v2.py tests/test_sonde_astra_courses_v1.py tests/test_astra_carbon_declares_auto_conception_v2b.py
```
Attendu : toutes les empreintes « OK » ; 83 + 14 + 11 = 108 essais passés (les essais neufs lisent les commandes dans `refs/remotes/origin/main`).

## 2. Sonde d'Astra du jour (R-3273 ; au plus 0,05 USD, signalée ; avant les relais de la course)

Relais **jeté**, port 8793 (jamais 8787 à 8792 : la sonde refuse un port de course ; le relais de la course doit rester neuf). Réglages qui passent, et pourquoi :
- relais : `--plafond-usd 0.05 --reserve-par-appel 0.01 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 1` — le relais réserve `max(0,01 ; pire cas de la requête)` ; pour la consigne de la sonde (corps de 134 octets, 768 jetons de sortie), pire cas du relais = pire cas de la commande = (134 + 1 024) × 10 / 10⁶ + 768 × 50 / 10⁶ = **0,04998 USD ≤ 0,05** : admis ;
- commande (par la sonde v2 épinglée) : `PLAFOND_SESSION_USD=0.05`, `--max-sortie-jetons 4096 --sortie-min-jetons 16`, que la commande réduit à **768 jetons** (ce que paie le plafond après le pire cas d'entrée) ; avec ses défauts (4 096 jetons au moins), elle rend le code 4 sans rien envoyer. 768 jetons couvrent une réponse triviale avec un raisonnement court (SUPPOSÉ : non mesuré sur Astra ; une troncature rend « sonde non réussie », lue comme telle — contre-lecture v2, constat 1 (b)).

```
mkdir -p /home/user/sonde-astra-«J»
cd /home/user/controle-ia-travail && git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py > /home/user/sonde-astra-«J»/commande_astra_v1.py && echo "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71  /home/user/sonde-astra-«J»/commande_astra_v1.py" | sha256sum -c -
cd /home/user/sonde-astra-«J» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sonde-astra-«J»/console-astra-sonde.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8793 --modeles-permis gpt-6-astra --plafond-usd 0.05 --reserve-par-appel 0.01 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 1 --journal /home/user/sonde-astra-«J»/journal-relais-astra-sonde.jsonl
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/sonde_astra_courses_v1.py --commande /home/user/sonde-astra-«J»/commande_astra_v1.py --url-relais-jete http://127.0.0.1:8793 --pid-relais-jete «PID_DU_RELAIS_JETE» --sortie docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-«J»-v1.json --sortie-v2 docs/notes/organisme-affinage-mentors-v1/course-v6/sonde-astra-course-affinage-v6.json
```

(La sortie v2 est le chemin exact que lit le lanceur de l'affinage v6 : un seul appel sert les deux courses le même jour. Si ce chemin existe déjà, la sonde refuse ; prendre alors un autre chemin pour `--sortie-v2` et dire que l'affinage devra refaire sa sonde.)

Codes : **0** sonde réussie (rapport « ok » vrai) ; **1** sonde non réussie, rapport écrit — si `echec_de_configuration` est vrai, **rien n'est parti** et ce n'est pas un échec d'Astra : arrêter ce relais jeté, en relancer un neuf bien réglé, rejouer sur des chemins neufs ; sinon (appel parti, réponse non conforme) Astra n'est pas déclarée ; **2** refus avant tout appel, rien d'écrit (commande, relais, port de course, relais non neuf, chemin existant : motif sur la sortie d'erreur).

Puis : `curl -s --noproxy '*' http://127.0.0.1:8793/relais/etat` (1 appel, dépense ≤ 0,05), arrêt **par PID** (`kill -INT «PID_DU_RELAIS_JETE»`, R10), consigner l'arrêt et **signaler la dépense** à la mère ; sceller rien de plus (les deux rapports sont scellés par la sonde) ; verser les deux rapports.

**Vérifier le rapport avant d'écrire la pièce de départ** (le lanceur v2 ne lit pas la sonde : il exige seulement une référence écrite ; cette vérification est donc celle de la mère) :
```
cd /home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/course-v2 && sha256sum -c sonde-astra-commune-«J»-v1.json.sha256 && /usr/local/bin/python3 -I -c "import json,sys;o=json.load(open('sonde-astra-commune-«J»-v1.json'));print(o['ok'],o['jour'],o['cout_usd'],o['depense_relais_usd'],o['relais_jete']['port'],o['rapport_v2'] and o['rapport_v2']['sha256']);sys.exit(0 if o['ok'] is True else 1)"
```
Attendu : `True «J» … … 8793 …`, code 0.

## 3. Pièce de départ, épreuve des témoins, relais

1. **Deux lignes de GO** : inchangé (commandes v2, § 1 point 1 : course 90 USD, épreuve 5 USD).
2. **Pièce de départ** : recopier `course-v2/piece-de-depart-gabarit-auto-conception-v2b.json` en `course-v2/piece-de-depart-auto-conception-v2.json` ; réécrire `statut` ; remplir les deux GO, `ecrit_le` (`date -u`) et `especes_optionnelles.astra.sonde_du_jour` = `docs/notes/organisme-auto-conception-v1/course-v2/sonde-astra-commune-«J»-v1.json (sha256 «…», ok vrai)` ; **si la sonde n'a pas réussi** : Astra non déclarée (`declaree: false`, clé `astra` retirée de `commandes_epinglees` et de la déclaration des relais), motif porté à la mère — la tentative n'est pas brûlée ; sceller (`PYTHONPATH=src python3 -m controle_ia.scellement sceller …`), verser.
3. **Épreuve réelle des témoins** : inchangée (commandes v2, § 2).
4. **Relais neufs de la course** (ceux de l'épreuve et le relais jeté de la sonde sont arrêtés) : Claude et Argon comme aux commandes v2, § 3 point 3 (Argon `--max-appels 280` : 231 appels au pire avec Astra et Carbon) ; **Astra et Carbon, toujours** :
   ```
   git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py > «D»/commande_astra_v1.py && sha256sum «D»/commande_astra_v1.py   # 986cf71e…
   /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-astra.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8790 --modeles-permis gpt-6-astra --plafond-usd 34 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 60 --delai-amont-s 3400 --journal «D»/journal-relais-astra.jsonl
   git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_gemini_lot_v1.py > «D»/commande_gemini_lot_v1.py && sha256sum «D»/commande_gemini_lot_v1.py   # 9484dce0…
   git show refs/remotes/origin/main:docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v4.py > «D»/relais_gemini_v4.py && sha256sum «D»/relais_gemini_v4.py   # 543e728d…
   /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py «D»/console-carbon.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!«CLE_CARBON» -- /usr/bin/python3 -I -B «D»/relais_gemini_v4.py --variable-cle «CLE_CARBON» --port 8792 --modele gemini-4-carbon --max-appels 60 --max-lots 15 --journal «D»/journal-relais-carbon.jsonl
   ```
   (Relais de course d'Astra : réserve par défaut 0,40 USD, sans objet ici — le pire cas d'un appel de la course, ≈ 3 USD au plafond de session, la dépasse ; plafond 34 ≥ 11 × 3. Vérifier chaque relais par PID et `/relais/etat` : **0 appel**, sinon le lanceur refuse.)

## 4. Déclaration des relais de la course

Comme aux commandes v2, § 3 point 4 (Claude `--plafond-ligne 90`, Argon), **plus** les deux blocs, toujours présents :

`"astra": {"type": "commande_externe", "commande": ["/usr/local/bin/python3", "-I", "-B", "«D»/commande_astra_v1.py", "--url-relais", "http://127.0.0.1:8790", "--modele", "gpt-6-astra", "--prix-entree", "10", "--prix-sortie", "50"], "modele_propose": "gpt-6-astra", "nom_cle": "OPENAI_API_KEY", "pid_relais": «PID_ASTRA», "url_etat_relais": "http://127.0.0.1:8790", "porte_plafond": {"type": "environnement"}}`

`"carbon": {"type": "commande_externe", "commande": ["/usr/local/bin/python3", "-I", "-B", "«D»/commande_gemini_lot_v1.py", "--url-base", "http://127.0.0.1:8792/v1beta", "--modele", "gemini-4-carbon", "--prix-entree", "8.3", "--prix-sortie", "41.5"], "modele_propose": "gemini-4-carbon", "nom_cle": "«CLE_CARBON»", "pid_relais": «PID_CARBON», "url_etat_relais": "http://127.0.0.1:8792", "porte_plafond": {"type": "environnement"}}`

Relevé des crédits (commandes v2, § 3 point 2) : ajouter la clé d'Astra et celle de Carbon (« non lisible ») à la dispense de la mère (R-3237). Puis lancement, codes et « après » : commandes v2, § 3 points 5 et 6.

## 5. Ce que les essais montrent (hors ligne, aucun appel)

- **Diagnostic reproduit** (`tests/test_sonde_astra_courses_v1.py`, code du relais épinglé servi dans le processus) : relais jeté sans `--reserve-par-appel` → la commande reçoit **HTTP 402** (code 3), l'amont ne reçoit rien ; commande sous `PLAFOND_SESSION_USD=0.05` avec ses sorties par défaut → **code 4**, rien n'est envoyé ; sans `PLAFOND_SESSION_USD` → code 2 ; réglages du § 2 → code 0, 768 jetons demandés, pire cas 0,04998 USD égal au pire cas du relais, dépense ≤ 0,05 même si l'amont facture tout le maximum demandé.
- **Sonde commune** : cas sain (passe, deux rapports scellés, le v2 au format du lanceur de l'affinage v6) ; réserve trop haute → échec de configuration rapporté, rien d'envoyé, chemin v2 laissé libre ; plafond, prix ou `--max-appels` faux → échec de configuration rapporté ; relais non neuf, port d'une course (8787, 8790, 8792), autre programme, autre PID, autre amont, autre commande, rapport existant → refus avant tout appel ; modèle servi autre → échec rapporté.
- **Lanceur v2 inchangé** (`tests/test_astra_carbon_declares_auto_conception_v2b.py`, commandes réelles extraites de `main`) : gabarit brut refusé (« À REMPLIR ») ; gabarit rempli → **code 0, cinq espèces actives** (deux Claude, Argon, Astra, Carbon ; pas de Kimi), relais 8790 et 8792 contrôlés ; sans `sonde_du_jour` (absent ou blanc) ou sans `risque_accepte`, pour Astra comme pour Carbon → refus ; Astra retirée de la pièce mais déclarée aux relais → refus ; commande d'une autre empreinte → refus ; relais de course d'Astra non neuf → refus (motif « relais neuf ») ; Argon sous 231 appels → refus.

## 6. Réserves

- Le lanceur v2 **ne lit pas** le rapport de sonde : `sonde_du_jour` est un texte libre non vide. La vérification du § 2 (empreinte, « ok », jour) est la garde ; elle est humaine.
- Une sonde triviale prouve la clé, le modèle et le relais, pas le comportement à 40 000 jetons d'entrée et 6 000 de sortie : une espèce déclarée qui échoue à l'échelle rend l'étape « non mesurée (technique) » et consomme l'unique tentative (préenregistrement v2, section Espèces ; contre-lecture v2, constats 1 (c) et 7). Ce risque est accepté par le mot du directeur.
- Les deux courses emploient les mêmes ports (8787, 8788, 8790, 8792) : elles ne tournent pas en même temps ; chacune a ses relais neufs.
