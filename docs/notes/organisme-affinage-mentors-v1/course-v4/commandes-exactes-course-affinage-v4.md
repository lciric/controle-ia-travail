# Commandes exactes — course d'affinage des idées des mentors, version 4 (rien n'est lancé ici)

- Écrit le 2026-11-18T07:49Z (`date -u`) par la session du compte organisme (modèle I). **Version 4** (R12) : les commandes v1 à v3 ne valent plus ; seul le lanceur v4 se lance, depuis une **session d'exécution neuve ouverte par la mère** (garde de calcul chargée, variable `RR_ANTHROPIC_API_KEY_MINUIT` présente et non vide). Clé de tous les appels Claude : Minuit ; `RR_ANTHROPIC_API_KEY_RIGAUD` n'est pas employée. Règles de clé : R-3237. Procédure des relais : `docs/procedures/relais-persistants-v1.md` (R-3238).
- Le lanceur ne clone rien et ne loue aucune instance : `DEPOT_URL` est sans objet (s'il fallait cloner le dépôt de travail : `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git`).
- Les modèles ne sont nommés que par la configuration (`course-v4/configuration-course-affinage-mentors-v4.json`, champ `especes`) ; les commandes ci-dessous les y lisent.
- **À copier bloc par bloc, jamais d'un seul tenant** : le bloc du § 1 contient un document en ligne dont la marque de fin est `FIN_EMPREINTES`.

## 0. Préalables (mère), avant toute commande

1. Montants absents du registre des dépenses (relevé d'ensemble § 3.4, environ 41,82 USD) inscrits.
2. **Contre-lecture** du préenregistrement v4 et du lanceur v4 par un agent neuf du **modèle K**, scellée, à ce chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v4/contre-lecture-preenregistrement-course-affinage-mentors-v4.md`. Elle cite `87fbd43aa476f2e8c7106261cb1fce6afc036803df2342ab6be36976920db8e3` (préenregistrement v4) et `d884da13babfa3d3e6a405ec73242c29f19250f69627ada810b5810d8b09987c` (lanceur v4), se dit du modèle K, ne dit pas qu'elle n'a pas relu, et la première ligne de sa section `## Verdict` est exactement `Scellable.` (ou `**Scellable.**`).
3. **Option des relais persistants** (nœud, règle de garde) : la v4 applique « relais de ligne entière » (procédure § 4, seconde forme ; recommandation de la contre-lecture de la v3) ; la mère la confirme par écrit avant le lancement, ou demande une version qui joue « un relais par étape ».
4. Réserves de cloisonnement : 20 entrées retirées tant qu'aucune n'est levée par écrit ; **CW15 reste servie** (la réserve « tout le thème CW1 » n'a retiré que CW2) : à étendre par écrit si la mère le veut.
5. **Registre des GO** : le registre de `main` porte des identifiants en double (lignes « extension ») et la lecture de l'orchestrateur le refuse en entier ; le lanceur v4 lui passe un **registre dérivé** (la ligne de GO-2026-11-18-14 et les révocations qui la visent), écrit et scellé dans le dossier du run. La ligne de GO doit porter : type `calcul`, Lazar, période qui couvre le jour, périmètre qui contient « mentors » ou « affinage », plafond exactement `150 USD`.
6. **Astra et Carbon ne partent pas en v4** : aucune commande externe épinglée ; ne pas les déclarer (le lanceur refuse). Une version suivante peut épingler des commandes relues.
7. Soldes : Minuit 200 USD déclarés (part au pire 150) ; Kimi seulement si sa part au pire + 11,3 ≤ 90 % du reste relu ; Argon sous la dispense écrite R-3237 (solde illisible), arrêt de la course au premier refus pour crédit (code 5, alerte scellée `alerte-arret-credit.json` pour la mère, qui prévient Lazar).

## 1. Dépôt et empreintes

```sh
cd /home/user/controle-ia-travail
git fetch -q origin +refs/heads/lot/compte-organisme-v1:refs/remotes/origin/lot/compte-organisme-v1
git checkout -q origin/lot/compte-organisme-v1 -- scripts/lancer_course_affinage_mentors_v4.py scripts/garde_credit_relais_v4.py scripts/porte_plafond_relais_v1.py scripts/lancer_relais_local_v1.py scripts/construire_fils_course_affinage_mentors_v1.py tests/test_lancer_course_affinage_mentors_v4.py docs/procedures/relais-persistants-v1.md docs/notes/organisme-affinage-mentors-v1
sha256sum -c - <<'FIN_EMPREINTES'
d884da13babfa3d3e6a405ec73242c29f19250f69627ada810b5810d8b09987c  scripts/lancer_course_affinage_mentors_v4.py
9673b0f6fbcdfbd287d0979880c098682fb070e36bc111f27cc4f34d75677356  scripts/garde_credit_relais_v4.py
fab5fe2e924c47799d968663baddfecb85dd6f74e9f859d9047b185eb36382b1  scripts/porte_plafond_relais_v1.py
d365affcb0303283a71ac7d5e67e24a5b6060e3b13c2a9e83ea592e48d4b3c82  scripts/lancer_relais_local_v1.py
0ca9cf5daa190135f8f26175f2639e4c9c4b22b01c551ab30ff8f7bb0d085148  docs/procedures/relais-persistants-v1.md
ff2b38e23d7d97dfda95084bbf7e7b9a64f0c83a943141a355d0e136f8d4c912  scripts/construire_fils_course_affinage_mentors_v1.py
e0c0617e49af1dc8a6c59514df3601befa38fd31225d8746a61f529d7111d41a  tests/test_lancer_course_affinage_mentors_v4.py
87fbd43aa476f2e8c7106261cb1fce6afc036803df2342ab6be36976920db8e3  docs/notes/organisme-affinage-mentors-v1/course-v4/preenregistrement-course-affinage-mentors-v4.md
dfe67ba83cae9fe744c38de7e2777a3bb1aeec08df7e708220a0c9895385d36e  docs/notes/organisme-affinage-mentors-v1/course-v4/configuration-course-affinage-mentors-v4.json
d97594dbc2263cd4200113d44dd4fd3fc8562bef617d3e182f6a382bf95ec792  docs/notes/organisme-affinage-mentors-v1/course-v3/procedure-relais-persistants-course-affinage-v3.json
c30928c88feffc16d3aa1119efe2a54ba2d70cf135b8068855190a21470a56bb  docs/notes/organisme-affinage-mentors-v1/course-v1/fils-servis-et-retraits-course-affinage-mentors-v1.json
d36ba0a01c1c190d55d0ed63b053c951b5a767a9310013321d797e3e203d8c4f  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-proposeur-course-affinage-mentors-v1.md
903318d7659db07819cbe9a7f89cbdbd292f59e14c32bb8811d8f8cb35dd955b  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-aiguilleur-course-affinage-mentors-v1.md
a32583b14845343a613514cdcba3c24831a274b48ecc95fe0d884f017d27d346  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-juge-course-affinage-mentors-v1.md
1ac9791b6aea1c97f534e32980f1f837cca425806ce8235b1064d98ce261dcbf  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-passe-tableau-course-affinage-mentors-v1.md
521470096f98861d0a4183b24b1ab313af9fb365ee398da4b82afbfbbbfb3f30  docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v5.md
ca4ba1dfd53a2ed91a56e099efe94478351a0025df40d85e4a4bc62f2f944b12  docs/notes/organisme-affinage-mentors-v1/course-v4/releve-prix-claude-gabarit-course-affinage-v4.json
03674096e70fb650076906dcc5a4f7e041d173df5c3e1045953bd5f1f4dfc28d  docs/notes/organisme-affinage-mentors-v1/course-v4/releve-credits-gabarit-course-affinage-v4.json
37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a  rapports/fille-ideation-1-v1/appel-argon-v5.sh
46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46  docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py
FIN_EMPREINTES
test -n "${RR_ANTHROPIC_API_KEY_MINUIT:-}" && echo MINUIT-PRESENTE-NON-VIDE   # par le nom seulement : jamais d'echo de la valeur
```

Toute ligne autre que « OK » : arrêt, rien n'est lancé.

## 2. Orchestrateur (dépôt public, lecture seule)

Une seule copie, à `/home/user/ideation-organism/orchestrator` ou `/home/user/lciric/ideation-organism/orchestrator`, au commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, arbre propre (fichiers ignorés compris) :

```sh
O=/home/user/ideation-organism            # ou /home/user/lciric/ideation-organism, jamais les deux
test "$(git -C $O rev-parse HEAD)" = a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb && test -z "$(git -C $O status --porcelain --untracked-files=all --ignored=matching)" && echo ORCHESTRATEUR-OK
echo "1b90b020287e575b5564508f9ba33b87bbc051c1015f4198e6b6e648d50ee153  $O/orchestrator/pole/relais_reel.py" | sha256sum -c -
/usr/local/bin/python3 -I -B -c "import claude_agent_sdk" && command -v bwrap socat
```

## 3. Essais hors ligne (aucun appel)

```sh
PYTHONPATH=src /usr/local/bin/python3 -m pytest -q -p no:cacheprovider tests/test_lancer_course_affinage_mentors_v4.py   # attendu : 79 passed
/usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v4.py --a-blanc /tmp/essai-a-blanc-affinage-v4-$(date -u +%Y%m%d%H%M%S)   # code 0
```

## 4. Relais (procédure neutre, § 2 et § 3), dossier hors dépôt

```sh
R=/home/user/sorties-relais-affinage-v4 && mkdir -p $R && cd $R
MODELES=$(/usr/local/bin/python3 -I -c "import json;c=json.load(open('/home/user/controle-ia-travail/docs/notes/organisme-affinage-mentors-v1/course-v4/configuration-course-affinage-mentors-v4.json'));print(','.join(e['modele'] for e in c['especes'] if e['famille']=='claude'))")
# Claude : relais de ligne entière à 150 USD, clé lue par son nom dans le seul environnement du relais
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py $R/console-claude.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!RR_ANTHROPIC_API_KEY_MINUIT -- /usr/bin/python3 -I -B $O/orchestrator/pole/relais_reel.py --variable-cle RR_ANTHROPIC_API_KEY_MINUIT --port 8787 --plafond-usd 150 --modeles-permis "$MODELES" --journal $R/journal-relais-claude.jsonl
# Argon : relais Gemini v2 (procédure § 2.3), port 8788, sa clé par son nom
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py $R/console-gemini.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!GEMINI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py --port 8788 --max-appels 400 --modele gemini-4-argon --journal $R/journal-relais-gemini.jsonl
# Kimi (seulement si la règle de part le permet) : relais compatible (§ 2.2), port 8789, plafond 6 USD (au-dessus de sa part au pire, 5,53)
/usr/bin/python3 -I -B /home/user/controle-ia-travail/scripts/lancer_relais_local_v1.py $R/console-moonshot.txt PATH,HOME,HTTPS_PROXY,NO_PROXY,SSL_CERT_FILE,REQUESTS_CA_BUNDLE,!KIMI_API_KEY -- /usr/bin/python3 -I -B /home/user/controle-ia-travail/docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py --amont https://api.moonshot.ai --variable-cle KIMI_API_KEY --port 8789 --modeles-permis kimi-k3.1-pro --plafond-usd 6 --prix-entree 2 --prix-sortie 10 --prix-cache 2 --max-appels 16 --delai-amont-s 3400 --journal $R/journal-relais-moonshot.jsonl
```

Chaque lanceur imprime le `pid` ; le noter. Vérifier (procédure § 3) par PID et `/relais/etat` : 0 appel, 0 dépense, plafond et modèles conformes ; sinon arrêt par PID, rien ne part.

## 5. Déclaration des relais (écrire, puis sceller)

Chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v4/declaration-relais-course-affinage-mentors-v4.json`. Noms de clé seulement. La commande de chaque porte **commence** par `/usr/local/bin/python3 -I -B /home/user/controle-ia-travail/scripts/porte_plafond_relais_v1.py` (le lanceur l'exige) :

```json
{"version": "declaration-relais-course-affinage-mentors-v4", "redige_utc": "(date -u)",
 "fournisseurs": {
  "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:8787", "nom_cle": "RR_ANTHROPIC_API_KEY_MINUIT", "pid_relais": 0,
             "porte_plafond": {"type": "commande", "delai_s": 30, "commande": ["/usr/local/bin/python3", "-I", "-B",
               "/home/user/controle-ia-travail/scripts/porte_plafond_relais_v1.py", "--url", "http://127.0.0.1:8787",
               "--modeles-permis", "(valeur de $MODELES)", "--plafond-ligne", "150"]}},
  "argon": {"type": "commande_externe", "commande": ["bash", "/home/user/controle-ia-travail/rapports/fille-ideation-1-v1/appel-argon-v5.sh"],
            "nom_cle": "GEMINI_API_KEY", "porte_plafond": {"type": "environnement"}},
  "kimi": {"type": "kimi_protocole", "url_relais": "http://127.0.0.1:8789", "modele": "kimi-k3.1-pro", "prix_entree": 2.0,
           "prix_sortie": 10.0, "max_sortie_jetons": 32768, "sortie_min_jetons": 1024, "delai_s": 3300, "nom_cle": "KIMI_API_KEY",
           "pid_relais": 0, "porte_plafond": {"type": "commande", "delai_s": 30, "commande": ["/usr/local/bin/python3", "-I", "-B",
             "/home/user/controle-ia-travail/scripts/porte_plafond_relais_v1.py", "--url", "http://127.0.0.1:8789",
             "--modeles-permis", "kimi-k3.1-pro", "--plafond-ligne", "150"]}}}}
```

`pid_relais` : le PID imprimé par le lanceur de relais (le lanceur de course lit ses arguments par `/proc/<pid>/cmdline` : programme épinglé par la procédure, variable de clé, port, plafond). Réglages de Kimi ci-dessus : (8 949 × 2 + 32 768 × 10) / 10⁶ = 0,3456 USD par appel au pire, part 5,53 ; 5,53 + 11,3 = 16,83 ≤ 29,03 pour 32,25 USD. Retirer `kimi` si son relais n'est pas lancé. Puis : `PYTHONPATH=src python3 -m controle_ia.scellement sceller <ce fichier>`.

## 6. Relevés du jour (écrire depuis les gabarits, puis sceller)

- Crédits : gabarit `course-v4/releve-credits-gabarit-course-affinage-v4.json` → `course-v4/releve-credits-avant-course-affinage-mentors-v4.json` (Minuit lisible, ou « non lisible » avec `depense_anterieure_usd` ; Kimi relu par l'appel gratuit de solde de la procédure, § 5 ; Argon « non lisible » sous la dispense `{"par": "mère", "reference": "R-3237", "cles": ["GEMINI_API_KEY"]}`).
- **Prix Claude du jour** (condition de la ligne de GO) : gabarit `course-v4/releve-prix-claude-gabarit-course-affinage-v4.json` → `course-v4/releve-prix-claude-course-affinage-v4.json`, avec source et heure ; tout écart au barème du relais (4 / 20, 10 / 50) : arrêt, nouveau devis.
- `PYTHONPATH=src python3 -m controle_ia.scellement sceller` sur les deux fichiers.

## 7. Lancement (une seule fois)

```sh
cd /home/user/controle-ia-travail
GO_ID=GO-2026-11-18-14 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v4.py
```

Avant le manifeste de départ, le lanceur joue la **porte à blanc** de chaque relais persistant (étape « porte-a-blanc », sans appel au fournisseur) : un refus rend 2 et ne brûle pas la tentative. Codes : 0 course finie ; 2 refus avant départ, ou arrêt ou nœud de l'orchestrateur ; 3 alerte de crédit avant le départ ; 4 cumul au-dessus de 150 USD ; 5 arrêt au premier refus pour crédit (alerte scellée pour la mère).

## 8. Après

1. Lire `/relais/etat` de chaque relais, puis l'arrêter par son PID (procédure § 6, R10) ; consigner dans `registres/arrets.md`.
2. Relever les soldes par l'interface quand elle le permet ; comparer au reste estimé du manifeste de fin ; toute alerte va à la mère, puis à Lazar.
3. Inscrire la dépense réelle par relais au registre des dépenses, avec l'écart au devis v5.
4. Verser `runs/<id>-course-affinage-mentors-v4/` ; sorties de l'orchestrateur hors dépôt sous `/home/user/sorties-course-affinage-mentors-v4/<id>/`. Aucune lecture des cartes avant la mère.

## Essai à blanc v4 déjà fait

`course-v4/essai-a-blanc-v4/` : orchestrateur réel épinglé, moteur simulé, relais factices ; quatre espèces (deux Claude, Argon, Kimi ; Astra et Carbon non déclarées, refusées en v4) ; 128 cartes, code 0. Portes, registre dérivé et prix du jour ne sont pas exigés en moteur simulé : ils sont essayés en moteur réel par les essais (relais factice local, vraie classe `PortePlafondCommande`, vraie lecture du registre par l'orchestrateur).

## Différentiel v3 → v4 (commandes)

1. Lanceur, garde de crédit, essais, préenregistrement, configuration : v4 ; porte `porte_plafond_relais_v1.py` ; procédure, lanceur de relais et pièce de la procédure épinglés.
2. Relais lancés par le lanceur de relais de la procédure ; relais Claude `relais_reel.py` (procédure), plafond 150 ; PID déclarés.
3. Commande de chaque porte : la porte épinglée en tête ; porte à blanc par le lanceur avant le départ.
4. Registre dérivé (le registre de `main` est refusé par l'orchestrateur).
5. Relevé du jour des prix Claude ; variable Minuit non vide.
6. Astra et Carbon retirés de la déclaration (refusés en v4).
7. Contre-lecture : chemin dans `course-v4/`.
8. Marque de fin du document en ligne des empreintes : `FIN_EMPREINTES` (et non `EOF`).
