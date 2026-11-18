# Commandes exactes — course d'affinage des idées des mentors, v6b : Astra et Carbon déclarés (rien n'est lancé ici)

- Écrit le 18 novembre 2026 par la session du compte organisme (modèle I). **Version 6b** (R12) : les commandes v6 (`commandes-exactes-course-affinage-v6.md`, `11b8c078…`) restent en place et valent **sauf** aux §§ 0 point 6, 5 et 6, remplacés ici. Fondement : mot du directeur tapé dans la session du compte organisme vers 10:50Z, « je veux astra et carbon dans la course debugge » — **Astra et Carbon déclarés** ; **Kimi non déclaré** (R-3279) ; **`compter_limite_de_debit_comme_soupcon` = faux** (R-3279, option (b)).
- **Le lanceur v6 (`bf2abdc6…`), le préenregistrement v6 (`58ccfa5c…`), la configuration et la sonde v2 ne changent pas.** Vérification faite après le diagnostic (point 1 de la commande de correctif) : la sonde v2 (`scripts/sonde_astra_affinage_v2.py`, `17994492…`) et le § 5 des commandes v6 sont **justes** — relais jeté avec `--reserve-par-appel 0.01`, commande sous `PLAFOND_SESSION_USD=0.05` avec `--max-sortie-jetons 4096 --sortie-min-jetons 16`, réduits à 768 jetons, pire cas 0,04998 USD, égal à celui du relais. Ce qui leur manquait : aucun contrôle du relais jeté avant l'appel (réglage, nouveauté, port, programme). La sonde commune (`scripts/sonde_astra_courses_v1.py`, `d374d107…`) l'ajoute **et fait l'unique appel par la sonde v2 épinglée**, dont le rapport, au chemin que lit le lanceur v6, reste celui qu'il exige (`version` = `sonde_astra_affinage_v2`).
- Rien n'a été lancé par l'auteur : relais factices (code du relais épinglé servi dans le processus de l'essai), moteur simulé, appels directs. Aucune valeur de clé. `«J»` = la date du jour (`date -u +%F`).

## 0 bis. Préalables (remplace le point 6 du § 0 des commandes v6)

6. **Carbon déclarée** (R-3274), sur la même clé qu'Argon (`GEMINI_API_KEY`) : part au pire de cette clé 150 + 24 = 174 USD. **Astra déclarée** sur le mot du directeur, **à condition que la sonde commune du jour ait réussi** (§ 5 bis) ; sinon, Astra retirée de la déclaration, motif écrit dans `absences.astra`, mère prévenue (la tentative n'est pas brûlée). **Kimi non déclaré** (R-3279 : tant qu'aucune sonde n'a répondu trois fois de suite). Le risque d'une espèce déclarée qui échoue à l'échelle (A14 : étape « non mesurée (technique) ») est accepté par le mot du directeur ; la porte à blanc et la sonde le réduisent sans l'annuler.
8. **Limite de débit** : `compter_limite_de_debit_comme_soupcon` = **faux** (R-3279, option (b)), déjà écrit dans le gabarit v6b.

## 1 bis. Empreintes de plus (en plus du § 1 des commandes v6)

```sh
cd /home/user/controle-ia-travail && git fetch -q origin +refs/heads/lot/compte-organisme-v1:refs/remotes/origin/lot/compte-organisme-v1 && git checkout -q origin/lot/compte-organisme-v1 -- scripts/sonde_astra_courses_v1.py tests/test_sonde_astra_courses_v1.py tests/test_astra_carbon_declares_affinage_v6b.py docs/notes/organisme-affinage-mentors-v1/course-v6/declaration-relais-gabarit-course-affinage-v6b.json
cd /home/user/controle-ia-travail && echo "d374d1071f4ef70b3604d97dc62e2f14103c440a166342b330d7a576d8b4c777  scripts/sonde_astra_courses_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "0ff8ba72d999d9fd97d08707b7cc9fe91b9ce7a17bf9b42918e2f76c8189fefd  tests/test_sonde_astra_courses_v1.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "30babf8fe466ce04fadcacf40349dd0e526dbf918188a147b6eb6a5f91cf9fc5  tests/test_astra_carbon_declares_affinage_v6b.py" | sha256sum -c -
cd /home/user/controle-ia-travail && echo "875f438f2da8dde0c20c13281f775906cd51019aec68aa338e85b2e86d9356f2  docs/notes/organisme-affinage-mentors-v1/course-v6/declaration-relais-gabarit-course-affinage-v6b.json" | sha256sum -c -
cd /home/user/controle-ia-travail && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src /usr/local/bin/python3 -m pytest -q -p no:cacheprovider tests/test_lancer_course_affinage_mentors_v6.py tests/test_sonde_astra_courses_v1.py tests/test_astra_carbon_declares_affinage_v6b.py
```

Attendu : « OK » partout ; 125 + 14 + 5 = 144 essais passés.

## 5 bis. Sonde d'Astra (remplace le § 5 des commandes v6)

**Si la sonde commune du jour a déjà été jouée pour la course d'auto-conception** (commandes `course-v2/commandes-exactes-course-auto-conception-v2b.md`, § 2) et a réussi, son rapport v2 est déjà à `course-v6/sonde-astra-course-affinage-v6.json` : ne rien rejouer, vérifier seulement (dernier bloc ci-dessous). Sinon :

```sh
mkdir -p /home/user/sonde-astra-«J»
cd /home/user/controle-ia-travail && git show origin/main:docs/notes/ideation-organisme-v1/relais-kimi-v1/commande_astra_v1.py > /home/user/sonde-astra-«J»/commande_astra_v1.py && echo "986cf71efcac285899e76dd9b1d1c11bccbfd71dd7ae91b8bf3a4372567d7c71  /home/user/sonde-astra-«J»/commande_astra_v1.py" | sha256sum -c -
cd /home/user/sonde-astra-«J» && /usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py /home/user/sonde-astra-«J»/console-astra-sonde.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!OPENAI_API_KEY -- /usr/bin/python3 -I -B /home/user/pieces-affinage-v6/relais_kimi_v4.py --amont https://api.openai.com --variable-cle OPENAI_API_KEY --port 8793 --modeles-permis gpt-6-astra --plafond-usd 0.05 --reserve-par-appel 0.01 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 1 --journal /home/user/sonde-astra-«J»/journal-relais-astra-sonde.jsonl
cd /home/user/controle-ia-travail && /usr/local/bin/python3 -I -B scripts/sonde_astra_courses_v1.py --commande /home/user/sonde-astra-«J»/commande_astra_v1.py --url-relais-jete http://127.0.0.1:8793 --pid-relais-jete <PID_DU_RELAIS_JETE> --sortie docs/notes/organisme-affinage-mentors-v1/course-v6/sonde-astra-commune-«J»-v1.json --sortie-v2 docs/notes/organisme-affinage-mentors-v1/course-v6/sonde-astra-course-affinage-v6.json
```

(`/home/user/pieces-affinage-v6/relais_kimi_v4.py` est extrait et vérifié au § 2 des commandes v6, `67f36951…` ; la sonde commune revérifie l'empreinte du programme lu par PID.) Codes : 0 réussie ; 1 non réussie, rapport écrit (`echec_de_configuration` vrai : rien n'est parti, ce n'est pas un échec d'Astra — relancer un relais jeté neuf bien réglé et la sonde sur des chemins neufs ; le chemin v2 est resté libre) ; 2 refus avant tout appel, rien d'écrit. Puis `/relais/etat` du relais jeté (1 appel, dépense ≤ 0,05), arrêt **par PID** (`kill -INT <PID>`, R10), consigner, **signaler la dépense** à la mère, verser les deux rapports.

Vérification (le lanceur v6 relit lui-même le rapport v2 : du jour, code 0, « ok », ≤ 0,05 USD, version, commande, relais distinct) :
```sh
cd /home/user/controle-ia-travail/docs/notes/organisme-affinage-mentors-v1/course-v6 && sha256sum -c sonde-astra-course-affinage-v6.json.sha256 && /usr/local/bin/python3 -I -c "import json,sys;o=json.load(open('sonde-astra-course-affinage-v6.json'));print(o['version'],o['horodatage_utc'],o['ok'],o['cout_usd'],o['relais_pid']);sys.exit(0 if o['ok'] is True else 1)"
```

Code 0 de la sonde : lancer le relais de la course d'Astra, **neuf**, comme au § 5 des commandes v6 (dernier bloc : port 8790, `--plafond-usd 24`, `--max-appels 16`).

## 6 bis. Déclaration des relais (remplace le § 6 des commandes v6)

Chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v6/declaration-relais-course-affinage-mentors-v6.json`. Recopier le gabarit **v6b** (`course-v6/declaration-relais-gabarit-course-affinage-v6b.json`), remplir les cinq PID et les modèles Claude de la configuration v6 (même commande qu'au § 4 des commandes v6), retirer la clé `gabarit` ; Astra retirée seulement si la sonde du § 5 bis n'a pas réussi (motif dans `absences.astra`). Les commandes d'Astra et de Carbon y sont **exactes** (le lanceur refuse tout autre argument). Puis : `cd /home/user/controle-ia-travail && PYTHONPATH=src python3 -m controle_ia.scellement sceller docs/notes/organisme-affinage-mentors-v1/course-v6/declaration-relais-course-affinage-mentors-v6.json`.

Relevé des crédits (§ 7 des commandes v6) : la clé d'Astra (`OPENAI_API_KEY`, « non lisible ») sous la dispense de la mère ; `GEMINI_API_KEY` à part au pire 174 USD ; pas de clé de Kimi.

## Ce que les essais montrent (hors ligne, aucun appel)

`tests/test_astra_carbon_declares_affinage_v6b.py`, lanceur v6 inchangé, commandes réelles extraites de `main`, rapport v2 écrit par la sonde commune devant le relais factice : déclaration v6b → **cinq espèces actives** (deux Claude, Argon, Astra, Carbon ; pas de Kimi), limite de débit non comptée ; bout en bout → **code 0**, sonde ≤ 0,05 USD au manifeste ; sonde commune en échec de configuration → refus (« sonde d'Astra ») ; sonde faite sur le relais de la course → refus ; relais de course d'Astra non neuf → refus, puis code 0 une fois neuf. Diagnostic et sonde commune : voir `tests/test_sonde_astra_courses_v1.py` (14 essais).

Devis : `devis-course-affinage-mentors-v6b.md` (composition déclarée : mêmes totaux que la colonne « cinq espèces » du devis v6, part au pire de `GEMINI_API_KEY` 174 USD).
