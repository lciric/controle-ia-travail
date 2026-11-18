# Commandes exactes — course d'affinage des idées des mentors, version 3 (rien n'est lancé ici)

- Écrit le 2026-11-18T07:23Z (`date -u`) par la session du compte organisme (modèle I). **Version 3** (R12) : les commandes v1 et v2 ne valent plus ; seul le lanceur v3 se lance, depuis une **session d'exécution neuve ouverte par la mère** (garde de calcul chargée, variable `RR_ANTHROPIC_API_KEY_MINUIT` présente). Clé de tous les appels Claude : `RR_ANTHROPIC_API_KEY_MINUIT` ; `RR_ANTHROPIC_API_KEY_RIGAUD` n'est pas employée. Règles de clé : R-3237.
- Le lanceur **ne clone rien et ne loue aucune instance** : `DEPOT_URL` est sans objet pour lui. Si une étape de cette liste clonait le dépôt de travail, elle passerait `DEPOT_URL=https://github.com/lciric/controle-ia-travail.git` (CLAUDE.md) ; aucune ne le fait.
- Les modèles ne sont nommés que par la configuration (`course-v3/configuration-course-affinage-mentors-v3.json`, champ `especes`) ; les commandes ci-dessous les y lisent.

## 0. Préalables (mère), avant toute commande

1. Inscrire au registre des dépenses les montants absents relevés par le relevé d'ensemble (§ 3.4, environ 41,82 USD) — préalable de la décision (section 2).
2. Faire écrire la **contre-lecture** du préenregistrement v3 **et** du lanceur v3 par un agent neuf du **modèle K**, scellée, à ce chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v3/contre-lecture-preenregistrement-course-affinage-mentors-v3.md`. Elle doit citer `a5b95e66042230f251f8cc98875cce9916795edb5747a0384e2883df4e6c178d` (préenregistrement v3) **et** `f91e19159c5298e526602e3b2296a8ab2d28eb40e7eeeda2d97d52e7aef8eb3f` (lanceur v3), se dire du modèle K, ne pas dire qu'elle n'a pas relu, et porter une section `## Verdict` dont la **première ligne est exactement** `Scellable.` (ou `**Scellable.**`).
3. Lever, ou non, par écrit les réserves de cloisonnement du relevé (§ 4). Tant qu'aucune n'est levée, les 20 entrées de la liste restent retirées ; une levée = nouvelle version de la liste, du préenregistrement et du lanceur.
4. Vérifier que la ligne de GO-2026-11-18-14 de `registres/go.md` porte : type `calcul`, accordée par `Lazar`, période qui couvre le jour du lancement, un périmètre qui contient « mentors » ou « affinage », et une cellule de plafond qui vaut **exactement** `150 USD` (le lanceur, comme celui de référence, refuse toute autre écriture de la cellule ; l'orchestrateur refuse un autre montant).
5. **Procédure neutre des relais persistants** (R-3237, 3) — **emplacement à remplir par la mère** : verser la procédure sur `main`, puis écrire et sceller la pièce `docs/notes/organisme-affinage-mentors-v1/course-v3/procedure-relais-persistants-course-affinage-v3.json` :

   ```json
   {"chemin": "À REMPLIR : chemin absolu de la procédure versée", "sha256": "À REMPLIR : empreinte de la procédure"}
   ```

   Tant que cette pièce est absente, porte « À REMPLIR », n'est pas scellée, ne correspond pas au fichier, ou que la porte de plafond d'un relais persistant (Claude, Kimi) ne lance pas ce chemin, **le lanceur refuse le moteur réel** (code 2).
6. Soldes à connaître (registre) et règle de clé par part (R-3237, 1 ; devis v5, § 6) : Minuit 200 USD déclarés, part au pire 150 ; Moonshot 32,25 USD (R-3224), Kimi ne part que si sa part au pire + 11,3 USD ≤ 90 % du reste relu, soit au plus 1,1078 USD par appel avec les prix et `max_sortie_jetons` déclarés — sinon les deux courses se suivent, solde relu avant chacune ; Google et OpenAI illisibles (R-3222) : Argon, Astra, Carbon partent sous la **dispense écrite R-3237**, et la course s'arrête au premier refus pour crédit de l'un d'eux (code 5).

## 1. Dépôt et empreintes

```sh
cd /home/user/controle-ia-travail
git fetch -q origin +refs/heads/lot/compte-organisme-v1:refs/remotes/origin/lot/compte-organisme-v1
git checkout -q origin/lot/compte-organisme-v1 -- scripts/lancer_course_affinage_mentors_v3.py scripts/garde_credit_relais_v3.py scripts/construire_fils_course_affinage_mentors_v1.py tests/test_lancer_course_affinage_mentors_v3.py docs/notes/organisme-affinage-mentors-v1
sha256sum -c - <<'EOF'
f91e19159c5298e526602e3b2296a8ab2d28eb40e7eeeda2d97d52e7aef8eb3f  scripts/lancer_course_affinage_mentors_v3.py
686546a6804651e0d8091348e80fbae19b9eeebcde495a8b4faf723b09d29c43  scripts/garde_credit_relais_v3.py
ff2b38e23d7d97dfda95084bbf7e7b9a64f0c83a943141a355d0e136f8d4c912  scripts/construire_fils_course_affinage_mentors_v1.py
a8fa325f2894ec98bfc855f468e00b4b2ebea3e38693adc95fd1e6d69727b8fe  tests/test_lancer_course_affinage_mentors_v3.py
a5b95e66042230f251f8cc98875cce9916795edb5747a0384e2883df4e6c178d  docs/notes/organisme-affinage-mentors-v1/course-v3/preenregistrement-course-affinage-mentors-v3.md
442774798ec91672c0fa00e6616f243d2d2bd38d530cbdb9675bc68210de5d8b  docs/notes/organisme-affinage-mentors-v1/course-v3/configuration-course-affinage-mentors-v3.json
c30928c88feffc16d3aa1119efe2a54ba2d70cf135b8068855190a21470a56bb  docs/notes/organisme-affinage-mentors-v1/course-v1/fils-servis-et-retraits-course-affinage-mentors-v1.json
d36ba0a01c1c190d55d0ed63b053c951b5a767a9310013321d797e3e203d8c4f  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-proposeur-course-affinage-mentors-v1.md
903318d7659db07819cbe9a7f89cbdbd292f59e14c32bb8811d8f8cb35dd955b  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-aiguilleur-course-affinage-mentors-v1.md
a32583b14845343a613514cdcba3c24831a274b48ecc95fe0d884f017d27d346  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-juge-course-affinage-mentors-v1.md
1ac9791b6aea1c97f534e32980f1f837cca425806ce8235b1064d98ce261dcbf  docs/notes/organisme-affinage-mentors-v1/course-v1/consigne-passe-tableau-course-affinage-mentors-v1.md
521470096f98861d0a4183b24b1ab313af9fb365ee398da4b82afbfbbbfb3f30  docs/notes/organisme-affinage-mentors-v1/devis-course-affinage-mentors-v5.md
37c0205e26f83cbdcdf5ad7f1e4094a21c7dcc70afb72d15ef0d260a770a132a  rapports/fille-ideation-1-v1/appel-argon-v5.sh
46c91df41b77a6d4cb7f5141993fda4a894118b5dd4ad1e5ba21a17dc2d67e46  docs/notes/ideation-organisme-v1/argon-recherche-v1/commande_argon_v3d.py
EOF
PYTHONPATH=src python3 -m controle_ia.scellement verifier docs/notes/organisme-affinage-mentors-v1/course-v3/preenregistrement-course-affinage-mentors-v3.md docs/notes/organisme-affinage-mentors-v1/course-v3/contre-lecture-preenregistrement-course-affinage-mentors-v3.md docs/notes/organisme-affinage-mentors-v1/course-v3/procedure-relais-persistants-course-affinage-v3.json
test -n "${RR_ANTHROPIC_API_KEY_MINUIT+present}" && echo MINUIT-PRESENTE   # par le nom seulement : jamais echo de la valeur
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
PYTHONPATH=src /usr/local/bin/python3 -m pytest -q -p no:cacheprovider tests/test_lancer_course_affinage_mentors_v3.py     # attendu : 60 passed (un essai est sauté si origin/main ou l'orchestrateur manquent)
/usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v3.py --a-blanc /tmp/essai-a-blanc-affinage-v3-$(date -u +%Y%m%d%H%M%S)   # attendu : code 0, 192 cartes simulées
```

## 4. Relais (session d'exécution ; les clés restent dans l'environnement des seuls relais)

- **Claude** (obligatoire) : relais de clé de l'orchestrateur, sur la boucle locale, modèles permis = exactement les deux espèces Claude de la configuration, plafond indépendant :

  ```sh
  cd $O/orchestrator
  MODELES=$(/usr/local/bin/python3 -I -c "import json;c=json.load(open('/home/user/controle-ia-travail/docs/notes/organisme-affinage-mentors-v1/course-v3/configuration-course-affinage-mentors-v3.json'));print(','.join(e['modele'] for e in c['especes'] if e['famille']=='claude'))")
  /usr/local/bin/python3 -I -B pole/relais_reel_v2.py --port 8787 --plafond-usd 150 --variable-cle RR_ANTHROPIC_API_KEY_MINUIT --modeles-permis "$MODELES" --journal /home/user/sorties-course-affinage-mentors-v3/relais-claude.jsonl &
  ```

  Clé : `RR_ANTHROPIC_API_KEY_MINUIT` (R-3228), par son nom ; jamais `RR_ANTHROPIC_API_KEY_RIGAUD` (le lanceur refuse). Arrêt du relais après la course **par son PID** (R10).
- **Argon** (obligatoire : proposeur, second juge) : relais Gemini v2 (`relais_gemini_v2.py`) sur `127.0.0.1:8788`, comme l'attend l'enveloppe `appel-argon-v5.sh` ; chemin du relais et nom de sa clé à nommer par la session d'exécution (la course v7 l'a employé).
- **Kimi, Astra** (si disponibles) et **Carbon** (inscrite, R-3217 ; relais et clé à nommer) : relais ou commande externe propres à la session d'exécution.
- **Porte de plafond des relais persistants** (Claude, Kimi) : la **procédure neutre de la mère** (§ 0, point 5), qui relance le relais avec le plafond dur de l'étape reçu dans `PLAFOND_ETAPE_USD` et `ETAPE_POLE` et imprime une dernière ligne `{"etape": …, "plafond_usd": …}` égale au centime (contrat : `pole/adaptateurs_v56.py`, `PortePlafondCommande`). La commande de chaque porte doit contenir le chemin épinglé de la procédure. Argon et les commandes externes reçoivent ce plafond dans leur environnement (porte « environnement »), sans outil de plus.

## 5. Déclaration des relais (à écrire, puis sceller)

Chemin exact : `docs/notes/organisme-affinage-mentors-v1/course-v3/declaration-relais-course-affinage-mentors-v3.json`. Noms de clé seulement ; une chaîne de la forme d'une valeur de clé fait refuser le départ. Gabarit (retirer les fournisseurs absents ; `carbon` seulement si son relais et sa clé sont nommés) :

```json
{"version": "declaration-relais-course-affinage-mentors-v3", "redige_utc": "(date -u)",
 "fournisseurs": {
  "claude": {"type": "claude_sdk", "url_relais": "http://127.0.0.1:8787", "nom_cle": "RR_ANTHROPIC_API_KEY_MINUIT",
             "porte_plafond": {"type": "commande", "commande": ["CHEMIN_DE_LA_PROCEDURE", "ARGUMENTS DE LA PROCÉDURE POUR LE RELAIS CLAUDE"], "delai_s": 120}},
  "argon": {"type": "commande_externe", "commande": ["bash", "/home/user/controle-ia-travail/rapports/fille-ideation-1-v1/appel-argon-v5.sh"],
            "nom_cle": "NOM_DE_LA_CLE_ARGON", "porte_plafond": {"type": "environnement"}},
  "kimi": {"type": "kimi_protocole", "url_relais": "http://127.0.0.1:PORT", "modele": "kimi-k3.1-pro", "prix_entree": 0.0,
           "prix_sortie": 0.0, "max_sortie_jetons": 0, "sortie_min_jetons": 0, "delai_s": 0, "nom_cle": "NOM_DE_LA_CLE_KIMI",
           "porte_plafond": {"type": "commande", "commande": ["CHEMIN_DE_LA_PROCEDURE", "ARGUMENTS DE LA PROCÉDURE POUR LE RELAIS KIMI"], "delai_s": 120}},
  "astra": {"type": "commande_externe", "commande": ["/chemin/absolu/commande-astra"], "modele_propose": "IDENTIFIANT-QUI-CONTIENT-astra",
            "nom_cle": "NOM_DE_LA_CLE_ASTRA", "porte_plafond": {"type": "environnement"}},
  "carbon": {"type": "commande_externe", "commande": ["/chemin/absolu/commande-carbon"], "modele_propose": "IDENTIFIANT-QUI-CONTIENT-carbon",
             "nom_cle": "NOM_DE_LA_CLE_CARBON", "inscription": "R-3217", "porte_plafond": {"type": "environnement"}}}}
```

Les zéros de Kimi sont à remplacer par ses prix et bornes réels (aucun défaut dans l'adaptateur). Puis :

```sh
PYTHONPATH=src python3 -m controle_ia.scellement sceller docs/notes/organisme-affinage-mentors-v1/course-v3/declaration-relais-course-affinage-mentors-v3.json
```

## 6. Relevé du crédit de chaque clé employée (le jour même, puis sceller)

Gabarit : `docs/notes/organisme-affinage-mentors-v1/course-v3/releve-credits-gabarit-course-affinage-v3.json` (scellé). À recopier sous le nom exact `docs/notes/organisme-affinage-mentors-v1/course-v3/releve-credits-avant-course-affinage-mentors-v3.json`, remplir (noms de clé seulement), puis :

```sh
PYTHONPATH=src python3 -m controle_ia.scellement sceller docs/notes/organisme-affinage-mentors-v1/course-v3/releve-credits-avant-course-affinage-mentors-v3.json
```

Règles appliquées par le lanceur (R-3237) : chaque clé lisible doit avoir un reste ≥ sa part au pire et ≥ un cinquième de son crédit ; Kimi : part au pire + 11,3 ≤ 90 % du reste ; Minuit non lisible : compté au prix relevé (200 USD moins `depense_anterieure_usd`) ; Argon, Astra, Carbon non lisibles : seulement sous la dispense `{"par": "mère", "reference": "R-3237", "cles": [...]}`. Sinon : `runs/<horodatage>-alerte-credits-affinage-mentors-v3/alerte-credits-avant.json` et code 3 (ou code 2 pour une dispense manquante), rien n'est lancé ; la mère prévient Lazar.

## 7. Lancement (une seule fois)

```sh
cd /home/user/controle-ia-travail
GO_ID=GO-2026-11-18-14 /usr/local/bin/python3 -I -B scripts/lancer_course_affinage_mentors_v3.py
```

Codes : 0 course finie ; 2 refus avant départ (dont variable Minuit absente, relais Claude sur une autre clé), ou arrêt ou nœud de l'orchestrateur (manifeste de fin écrit) ; 3 alerte de crédit avant le départ ; 4 cumul lu au-dessus de 150 USD (alerte écrite) ; 5 course arrêtée au premier refus pour crédit d'un relais au solde illisible (`arret_au_premier_refus_pour_credit` du manifeste de fin). Le lanceur imprime le chemin et l'empreinte de ses manifestes.

## 8. Après

1. Arrêter chaque relais par son PID (R10) ; le consigner dans `registres/arrets.md`.
2. Relever le crédit de chaque clé par l'interface de facturation et le comparer au « reste estimé » du manifeste de fin (`releve_credits_apres`) ; toute alerte (`alerte-credits-apres.json`) va à la mère, puis à Lazar.
3. Inscrire la dépense réelle (`cout_reel.par_relais_usd` du manifeste de fin) au registre des dépenses, avec l'écart au devis v5 (`ecart_au_devis_v5`).
4. Verser `runs/<id>-course-affinage-mentors-v3/` (scellé) ; les sorties de l'orchestrateur restent hors du dépôt, sous `/home/user/sorties-course-affinage-mentors-v3/<id>/`, jusqu'à la décision de la mère. Aucune lecture des cartes avant la mère ; aucun verdict lu comme promotion.

## Essai à blanc v3 déjà fait

`course-v3/essai-a-blanc-v3/` : orchestrateur réel épinglé, moteur simulé, relais factices ; relais Claude sur Minuit (compté au prix relevé, 200 USD) ; Argon, Astra, Carbon sous dispense R-3237 et derrière la garde de crédit ; Kimi lisible à 32,25 USD (part au pire 0,16 avec les prix factices) ; parts au pire au manifeste de départ (Claude et Argon 150, Astra et Carbon 24) ; six espèces, 192 cartes, code 0. La procédure des relais persistants n'est pas exigée en moteur simulé ; ses refus sont essayés en moteur réel par les essais.

## Différentiel v2 → v3 (commandes)

1. Lanceur, essais, préenregistrement, configuration, devis : v3, v3, v3, v3, v5 ; garde de crédit `garde_credit_relais_v3.py` ajoutée aux empreintes.
2. Contre-lecture : chemin dans `course-v3/`.
3. Emplacement nommé pour la procédure neutre des relais persistants (§ 0, point 5), refus du lanceur tant qu'il n'est pas rempli.
4. Relevé : gabarit scellé ; règle de clé par part ; condition de Kimi ; dispense R-3237 pour Argon, Astra, Carbon ; code 5.
5. Session d'exécution neuve ouverte par la mère (variable Minuit présente).
