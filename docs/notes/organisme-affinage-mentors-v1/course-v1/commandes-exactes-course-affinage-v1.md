# Commandes exactes — course d'affinage des idées des mentors, version 1 (rien n'est lancé ici)

- Écrit le 2026-11-18T07:06:07Z (`date -u`) par la session du compte organisme (modèle I). Pour la **session d'exécution** qui a la garde de calcul (R-3215). GO-2026-11-18-14, plafond d'arrêt **150 USD**. Aucune commande ci-dessous ne doit être tapée depuis une session sans la garde.
- Le lanceur **ne clone rien et ne loue aucune instance** : `DEPOT_URL` est sans objet pour lui. Si une étape de cette liste clonait le dépôt de travail, elle passerait `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git` (CLAUDE.md) ; aucune ne le fait.
- Les modèles ne sont nommés que par la configuration (`configuration-course-affinage-mentors-v1.json`, champ `especes`) ; les commandes ci-dessous les y lisent.

## 0. Préalables (mère), avant toute commande

1. Inscrire au registre des dépenses les montants absents relevés par le relevé d'ensemble (§ 3.4, environ 41,82 USD) — préalable de la décision (section 2).
2. Faire écrire la **contre-lecture** du préenregistrement **et** du lanceur par un agent neuf de l'autre modèle (modèle J), scellée, à ce chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v1/contre-lecture-preenregistrement-course-affinage-mentors-v1.md`. Elle doit citer `7a32fe6bd86368d0e06c11c08eeec00d7138545824ec940442ea199fdab521a8` (préenregistrement) **et** `015f5c3370ac28686ea66976e3c3a466eb92d3d52b18d1892412d933ee5302a1` (lanceur), et porter une section `## Verdict` dont la première ligne commence par « Scellable » sans « après corrections », « sous réserve » ni « non ». Toute correction demandée = nouvelle version (R12) ; ces commandes ne valent plus.
3. Lever, ou non, par écrit les réserves de cloisonnement du relevé (§ 4). Tant qu'aucune n'est levée, les 20 entrées de la liste restent retirées ; une levée = nouvelle version de la liste, du préenregistrement et du lanceur.
4. Vérifier que la ligne de GO-2026-11-18-14 de `registres/go.md` porte : type `calcul`, accordée par `Lazar`, période qui couvre le jour du lancement, un périmètre qui contient « mentors » ou « affinage », et une cellule de plafond qui vaut **exactement** `150 USD` (le lanceur, comme celui de référence, refuse toute autre écriture de la cellule ; l'orchestrateur refuse un autre montant).

## 1. Dépôt et empreintes

```sh
cd /home/user/controle-ia-travail
git fetch -q origin +refs/heads/lot/compte-organisme-v1:refs/remotes/origin/lot/compte-organisme-v1
git checkout -q origin/lot/compte-organisme-v1 -- scripts/lancer_course_affinage_mentors_v1.py scripts/construire_fils_course_affinage_mentors_v1.py tests/test_lancer_course_affinage_mentors_v1.py docs/notes/organisme-affinage-mentors-v1
sha256sum -c - <<'EOF'
015f5c3370ac28686ea66976e3c3a466eb92d3d52b18d1892412d933ee5302a1  scripts/lancer_course_affinage_mentors_v1.py
ff2b38e23d7d97dfda95084bbf7e7b9a64f0c83a943141a355d0e136f8d4c912  scripts/construire_fils_course_affinage_mentors_v1.py
515641cbd523d15661bd42d78440489b9497571ab147aa62197b416608e598f6  tests/test_lancer_course_affinage_mentors_v1.py
7a32fe6bd86368d0e06c11c08eeec00d7138545824ec940442ea199fdab521a8  docs/notes/organisme-affinage-mentors-v1/course-v1/preenregistrement-course-affinage-mentors-v1.md
4f9cdf3e5e81691ba8ead1037d2ce5f071b745b9a1ff3c657686c9196e1f81f9  docs/notes/organisme-affinage-mentors-v1/course-v1/configuration-course-affinage-mentors-v1.json
c30928c88feffc16d3aa1119efe2a54ba2d70cf135b8068855190a21470a56bb  docs/notes/organisme-affinage-mentors-v1/course-v1/fils-servis-et-retraits-course-affinage-mentors-v1.json
d36ba0a01c1c190d55d0ed63b053c951b5a767a9310013321d797e3e203d8c4f  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-proposeur-course-affinage-mentors-v1.md
903318d7659db07819cbe9a7f89cbdbd292f59e14c32bb8811d8f8cb35dd955b  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-aiguilleur-course-affinage-mentors-v1.md
a32583b14845343a613514cdcba3c24831a274b48ecc95fe0d884f017d27d346  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-juge-course-affinage-mentors-v1.md
1ac9791b6aea1c97f534e32980f1f837cca425806ce8235b1064d98ce261dcbf  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-passe-tableau-course-affinage-mentors-v1.md
6aa86555dd7a1883141660a4619812da6db2f0a9b9d05b1b5e2cb23db7546ea2  docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v3.md
37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a  rapports/fille-ideation-1-v1/appel-argon-v5.sh
46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46  docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py
EOF
PYTHONPATH=src python3 -m controle_ia.scellement verifier docs/notes/organisme-affinage-mentors-v1/course-v1/preenregistrement-course-affinage-mentors-v1.md docs/notes/organisme-affinage-mentors-v1/course-v1/contre-lecture-preenregistrement-course-affinage-mentors-v1.md
```

Toute ligne autre que « OK » : arrêt, rien n'est lancé.

## 2. Orchestrateur (dépôt public, lecture seule)

Une seule copie doit exister, à l'un des deux chemins que le lanceur connaît (`/home/user/ideation-organism/orchestrator` ou `/home/user/lciric/ideation-organism/orchestrator`), au commit épinglé, arbre propre (fichiers non suivis et ignorés compris) :

```sh
O=/home/user/ideation-organism            # ou /home/user/lciric/ideation-organism : jamais les deux
test "$(git -C $O rev-parse HEAD)" = a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb && test -z "$(git -C $O status --porcelain --untracked-files=all --ignored=matching)" && echo ORCHESTRATEUR-OK
# absente seulement : git clone https://github.com/lciric/ideation-organism $O && git -C $O checkout -q a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb
/usr/local/bin/python3 -I -B -c "import claude_agent_sdk" && command -v bwrap socat
```

## 3. Essais hors ligne (aucun appel)

```sh
cd /home/user/controle-ia-travail
PYTHONPATH=src /usr/local/bin/python3 -m pytest -q -p no:cacheprovider tests/test_lancer_course_affinage_mentors_v1.py     # attendu : 36 passed (un essai est sauté si origin/main ou l'orchestrateur manquent)
/usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v1.py --a-blanc /tmp/essai-a-blanc-affinage-$(date -u +%Y%m%d%H%M%S)   # attendu : code 0, 192 cartes simulées
```

## 4. Relais (session d'exécution ; les clés restent dans l'environnement des seuls relais)

- **Claude** (obligatoire) : relais de clé de l'orchestrateur, sur la boucle locale, modèles permis = exactement les deux espèces Claude de la configuration, plafond indépendant :

  ```sh
  cd $O/orchestrator
  MODELES=$(/usr/local/bin/python3 -I -c "import json;c=json.load(open('/home/user/controle-ia-travail/docs/notes/organisme-affinage-mentors-v1/course-v1/configuration-course-affinage-mentors-v1.json'));print(','.join(e['modele'] for e in c['especes'] if e['famille']=='claude'))")
  /usr/local/bin/python3 -I -B pole/relais_reel_v2.py --port 8787 --plafond-usd 150 --variable-cle NOM_DE_LA_CLE_CLAUDE --modeles-permis "$MODELES" --journal /home/user/sorties-course-affinage-mentors-v1/relais-claude.jsonl &
  ```

  `NOM_DE_LA_CLE_CLAUDE` : le nom (jamais la valeur) de la clé Claude choisie par la mère (« Claude d'abord », clé dont le reste est le plus haut). Arrêt du relais après la course **par son PID** (R10).
- **Argon** (obligatoire : proposeur, second juge) : relais Gemini v2 (`relais_gemini_v2.py`) sur `127.0.0.1:8788`, comme l'attend l'enveloppe `appel-argon-v5.sh` ; chemin du relais et nom de sa clé à nommer par la session d'exécution (la course v7 l'a employé).
- **Kimi, Astra** (si disponibles) et **Carbon** (inscrite, R-3217 ; relais et clé à nommer) : relais ou commande externe propres à la session d'exécution.
- **Porte de plafond des relais persistants** (Claude, Kimi) : l'orchestrateur v56 exige, pour chacun, une commande de l'opérateur qui **relance le relais avec le plafond dur de l'étape** reçu dans `PLAFOND_ETAPE_USD` et `ETAPE_POLE`, et imprime une dernière ligne `{"etape": …, "plafond_usd": …}` égale au centime (contrat : `pole/adaptateurs_v56.py`, `PortePlafondCommande`). **Elle n'existe dans aucune pièce lue par le rédacteur** : à fournir par la session d'exécution (outil de session-depot). Sans elle, le lanceur et l'orchestrateur refusent (A15). Argon et les commandes externes reçoivent ce plafond dans leur environnement (porte « environnement »), sans outil de plus.

## 5. Déclaration des relais (à écrire, puis sceller)

Chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v1/declaration-relais-course-affinage-mentors-v1.json`. Noms de clé seulement ; une chaîne de la forme d'une valeur de clé fait refuser le départ. Gabarit (retirer les fournisseurs absents ; `carbon` seulement si son relais et sa clé sont nommés) :

```json
{"version": "declaration-relais-course-affinage-mentors-v1", "redige_utc": "(date -u)",
 "fournisseurs": {
  "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:8787", "nom_cle": "NOM_DE_LA_CLE_CLAUDE",
             "porte_plafond": {"type": "commande", "commande": ["/chemin/absolu/porte-relais-claude"], "delai_s": 120}},
  "argon": {"type": "commande_externe", "commande": ["bash", "/home/user/controle-ia-travail/rapports/fille-ideation-1-v1/appel-argon-v5.sh"],
            "nom_cle": "NOM_DE_LA_CLE_ARGON", "porte_plafond": {"type": "environnement"}},
  "kimi": {"type": "kimi_protocole", "url_relais": "http://127.0.0.1:PORT", "modele": "kimi-k3.1-pro", "prix_entree": 0.0,
           "prix_sortie": 0.0, "max_sortie_jetons": 0, "sortie_min_jetons": 0, "delai_s": 0, "nom_cle": "NOM_DE_LA_CLE_KIMI",
           "porte_plafond": {"type": "commande", "commande": ["/chemin/absolu/porte-relais-kimi"], "delai_s": 120}},
  "astra": {"type": "commande_externe", "commande": ["/chemin/absolu/commande-astra"], "modele_propose": "IDENTIFIANT-QUI-CONTIENT-astra",
            "nom_cle": "NOM_DE_LA_CLE_ASTRA", "porte_plafond": {"type": "environnement"}},
  "carbon": {"type": "commande_externe", "commande": ["/chemin/absolu/commande-carbon"], "modele_propose": "IDENTIFIANT-QUI-CONTIENT-carbon",
             "nom_cle": "NOM_DE_LA_CLE_CARBON", "inscription": "R-3217", "porte_plafond": {"type": "environnement"}}}}
```

Les zéros de Kimi sont à remplacer par ses prix et bornes réels (aucun défaut dans l'adaptateur). Puis :

```sh
PYTHONPATH=src python3 -m controle_ia.scellement sceller docs/notes/organisme-affinage-mentors-v1/course-v1/declaration-relais-course-affinage-mentors-v1.json
```

## 6. Relevé du crédit de chaque clé employée (le jour même, puis sceller)

Chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v1/releve-credits-avant-course-affinage-mentors-v1.json`. Une entrée par nom de clé de la déclaration, lue sur l'interface de facturation ou le compteur ; « non lisible » s'écrit, il ne s'omet pas ; une dispense ne vaut que écrite par la mère, avec sa référence :

```json
{"version": "releve-credits-avant-course-affinage-mentors-v1", "releve_utc": "AAAA-MM-JJTHH:MM:SSZ (date -u, jour du lancement)",
 "cles": {"NOM_DE_LA_CLE_CLAUDE": {"credit_usd": 0.0, "reste_usd": 0.0, "source": "interface de facturation"},
          "NOM_DE_LA_CLE_ARGON": {"non_lisible": true, "motif": "…"}},
 "dispense": {"par": "mère", "reference": "R-NNNN", "cles": ["NOM_DE_LA_CLE_ARGON"]}}
```

```sh
PYTHONPATH=src python3 -m controle_ia.scellement sceller docs/notes/organisme-affinage-mentors-v1/course-v1/releve-credits-avant-course-affinage-mentors-v1.json
```

Un reste sous un cinquième du crédit ou sous 150 USD fait écrire `runs/<horodatage>-alerte-credits-affinage-mentors-v1/alerte-credits-avant.json` et rendre le code 3 : rien n'est lancé ; la mère prévient Lazar.

## 7. Lancement (une seule fois)

```sh
cd /home/user/controle-ia-travail
GO_ID=GO-2026-11-18-14 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v1.py
```

Codes : 0 course finie ; 2 refus avant départ, ou arrêt ou nœud de l'orchestrateur (manifeste de fin écrit) ; 3 alerte de crédit avant le départ ; 4 cumul lu au-dessus de 150 USD (alerte écrite). Le lanceur imprime le chemin et l'empreinte de ses manifestes.

## 8. Après

1. Arrêter chaque relais par son PID (R10) ; le consigner dans `registres/arrets.md`.
2. Relever le crédit de chaque clé par l'interface de facturation et le comparer au « reste estimé » du manifeste de fin (`releve_credits_apres`) ; toute alerte (`alerte-credits-apres.json`) va à la mère, puis à Lazar.
3. Inscrire la dépense réelle (`cout_reel.par_relais_usd` du manifeste de fin) au registre des dépenses, avec l'écart au devis v3 (`ecart_au_devis_v3`).
4. Verser `runs/<id>-course-affinage-mentors-v1/` (scellé) ; les sorties de l'orchestrateur restent hors du dépôt, sous `/home/user/sorties-course-affinage-mentors-v1/<id>/`, jusqu'à la décision de la mère. Aucune lecture des cartes avant la mère ; aucun verdict lu comme promotion.

## Essai à blanc déjà fait (dans ce dossier)

`essai-a-blanc-v1/` : orchestrateur réel au commit épinglé, **moteur simulé**, relais factices (adresses locales sans serveur, portes jamais appelées par le moteur simulé), déclaration, relevé et contre-lecture **d'essai** ; six espèces (Carbon comprise), 96 appels de proposeur, 192 cartes à passeport, 192 aiguillages, 384 jugements ; `passe_tableau` et `fusions` retirées ; coût fictif 6,72 USD ; code 0 ; spécification jugée conforme par l'orchestrateur ; arbre de l'orchestrateur resté propre. Manifestes du lanceur dans `essai-a-blanc-v1/lanceur/`, extraits de l'orchestrateur dans `essai-a-blanc-v1/orchestrateur/` (les sessions simulées sont restées hors du dépôt). Les modèles y sont nommés par la configuration assemblée, comme dans la configuration fixe.
