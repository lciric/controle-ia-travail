# Passation intégrale de la session mère — Antigravity `ff6e9350` (`2026-11-24T06:21Z`)

- **Session émettrice** : Antigravity `v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f` (seule session mère active sur `main` depuis la suspension volontaire de la sœur Claude Code `session_016QhUrvi45g3jX5saFefVED` à `R-5220`, `3922143bd`).
- **Horodatage** : `2026-11-24T06:21:00Z` (`date -u`).
- **Plage couverte depuis `2026-11-23-2220`** : `R-5203` à `R-5243` et `GO-2026-11-23-38` à `GO-2026-11-24-05`.
- **Environnement & secrets** : `/home/antigravity/env-setup.sh` (`chmod 600`, hors dépôt ; toujours charger avec `set -a && source /home/antigravity/env-setup.sh && set +a`).
  - `GEMINI_API_KEY` : **active (`HTTP 200`)**.
  - `GEMINI_API_KEY_2` : **active (`HTTP 200`)**.
  - `GEMINI_API_KEY_3` : **épuisée (`HTTP 402 prepayment credits depleted` — ne pas utiliser)**.
  - `RR_ANTHROPIC_API_KEY_LUC` : **active (`HTTP 200`)** à condition d'**omettre** `--nom-espace-anthropic` dans `collisionneur_v9_v8d.py` (`RR_ANTHROPIC_WORKSPACE_ID` renvoie `HTTP 404`).
  - `CONTROLE_IA_GITHUB_TOKEN_2` et `_3` : **actifs (`HTTP 200`, `push: true`)**.
- **Cloisonnement absolu de la mère (`CLAUDE.md`)** :
  - **Ne jamais ouvrir** `docs/verdicts/`, `runs/`, `diag/`, `donnees/*` (scores/tables), `coffre/*`, `essai/iib-explo-*`, `brouillons/ii-b*`, `consigne-privee*`, `conception-ii-b*`, `verdict/*`, `lecture/*`.
  - **Ne jamais pousser** de travail interne sur `lciric/controle-ia` (uniquement sur `origin` = `lciric/controle-ia-travail.git`, exception faite du petit dépôt compagnon public autorisé par `GO-2026-11-24-05` qui ne contient *que* les fichiers mathématiques purs nettoyés).
  - **4 instances Vast.ai arrêtées intouchables** : `58936096`, `58936099`, `58936100`, `60988826` (**ne jamais détruire**). Solde Vast.ai : **`20,42 USD`**.
  - **Règle de langue (`R-5226`)** : français limpide sans jargons codés nus (`lot 8`, `B bis`, `C2`, `Q6` uniquement entre parenthèses après désignation scientifique explicite ; néologismes maison *Plan Turing*, *collisionneur*, *Protocole X*, *monde planté* et symboles mathématiques permis).

---

## 1. Action immédiate n° 1 à la reprise (`GO-2026-11-24-05`) : Pousser le dépôt GitHub public compagnon via Neon

Lazar a ordonné à `06:01Z` :
> *« Minute 0 — Créer d'abord le petit dépôt GitHub public compagnon avec uniquement les fichiers propres : README.md, main.tex (avec Lazar Ciric remplaçant [Author Name], compilé en main.pdf), script de vérification -> go push sur github ; utilise neon pour ça »*

- **Ce qui est déjà prêt et versé sur `main`** :
  1. Demande complète à Neon (`xhigh`) intégrant les retours de la double revue Carbon et les `6` corrections d'`Overfull \hbox` relevées par `pdflatex` : `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/demande-neon-preparation-depot-public-v1.md`.
  2. Si la présente VM (`ff6e9350`) est toujours active, l'appel Neon (`task-1058`) écrit dans `.../scratch/neon-depot-public-v1/{appel,pensees,reponse}-neon-depot-public-v1.{json,md}`. Si une **nouvelle** session prend le relais sur une autre VM et que `reponse-neon-depot-public-v1.md` n'est pas encore sur `main`, relancer l'appel Neon via :
     ```bash
     set -a && source /home/antigravity/env-setup.sh && set +a
     DEMANDE_FICHIER="../cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/demande-neon-preparation-depot-public-v1.md" \
     SUFFIXE="depot-public-v1" MOTS="3500" \
     .venv/bin/python3 docs/notes/idee-interessante-v1/appel_google_idee_v2.py appel neon GEMINI_API_KEY /tmp/neon-depot-public
     ```
  3. Appliquer les retouches de Neon (auteur `Lazar Ciric`, retrait du vantardise « 14 000 Monte Carlo » du résumé, clarification de l'Opérateur A vs RL en ligne ancré sur $\pi_0$, clarification du risque en déploiement de la Table 3, ajout de la remarque Rényi $D_\infty$ en Remarque 4, renommage anglais `verify_examples.py` + `verified_examples.json`, `0` `Overfull \hbox` sous `pdflatex` -> génération de `main.pdf`, ajout de `LICENSE` MIT / CC-BY-4.0).
  4. Créer le dépôt public par l'outil `create_github_repository` (ex. `name="in-loop-filtering-stealth"`, `private=false`, `description="When Does In-Loop Misalignment Filtering Select for Stealth? Exact Phase Transitions and Escape Regimes in Post-Training"`), pousser **uniquement** les fichiers propres (`README.md`, `main.tex`, `main.pdf`, `verify_examples.py`, `verified_examples.json`, `LICENSE`), remplacer `[LINK_GITHUB_PAGE]` dans `commentaire-reponse-yair-halberstadt-lesswrong-en-v2.md` et donner l'URL directe à Lazar !

---

## 2. Machines louées, démons en cours et points de sauvegarde distants

1. **Serveur processeur Hetzner `177425658` (`sondes-v2-etalon-v4-20261124-0537`) — EN MARCHE AUTONOME** (`GO-2026-11-24-02`, `R-5238`) :
   - `ccx33` (8 cœurs dédiés) à `hel1` (`0,22596 EUR/h` brut = `0,28245 USD/h`), créé à `2026-11-24T05:37:03Z` (`mode=etalon_seul`, `52` cases, `TA_etalon = 80`, durée attendue `≈ 23,1 h` soit fin vers `2026-11-25T04:45Z`, coût attendu `≈ 6,52 USD`).
   - Pousse automatiquement ses résultats vers `origin/calcul/sondes-v2-epreuve-plantee-v4` puis s'autodétruit par `DELETE /v1/servers/177425658` (minuterie interne dure à `31h30` + démon externe `task-943` sur `ff6e9350`).
   - **Vérification depuis toute nouvelle session** :
     ```bash
     set -a && source /home/antigravity/env-setup.sh && set +a
     curl -fsS -H "Authorization: Bearer $HCLOUD_TOKEN" https://api.hetzner.cloud/v1/servers/177425658 | jq '{id: .server.id, status: .server.status, created: .server.created}'
     git ls-remote origin refs/heads/calcul/sondes-v2-epreuve-plantee-v4
     ```
2. **Collisionneurs en cours — Cellules intermédiaires sauvegardées sur `origin/runs/collisionneurs-partiels-passation-2026-11-24-0620`** :
   - **Collisionneur Boucle Organisme ⇄ Contrôle (`GO-2026-11-24-03`, `R-5227`, plafond `36 USD`)** : **`8/9` cellules valides achevées** sur le bras `principal` ! Seule la 9e cellule (`E3-T3-reponse-C` Neon, interrompue par 503/timeout Google) reste à finir avec `--reprise`, suivie du bras `temoin` (`question-temoin-neutre-collisionneur-boucle-organisme-controle-v1.md`) puis `verifier`. Toutes les 8 cellules déjà payées sont sauvegardées dans `boucle-organisme-controle/principal/` sur la branche `origin/runs/collisionneurs-partiels-passation-2026-11-24-0620` !
   - **Collisionneur Cible de Publication Papier D (`GO-2026-11-24-04`, `R-5240`, plafond `18 USD`)** : les **2 appels directs à Carbon en effort élevé sont TERMINÉS et VERSÉS sur `main`** (`docs/notes/cartographie-mathematiques-ouvertes-v1/cible-publication-collisionneur-v1/carbon-effort-eleve/`) et intégrés dans **`strategie-cibles-et-feuille-de-route-publication-papier-d-v2.{md,pdf}`** ! Le collisionneur `etage3` (`task-981`) tourne en démon sur `ff6e9350` (cellules initiales aussi sauvegardées dans `cible-publication/collisionneur/` sur `origin/runs/collisionneurs-partiels-passation-2026-11-24-0620`).
   - **Collisionneur Groupé Plan Turing (`GO-2026-11-24-03`, `R-5236`)** : prêt au départ sur `main` (`docs/notes/protocole-x-structure-du-langage-v1/groupe-g1-v1/`, neutralité `0,22 / 0,28 / 0,18 < 0,50`, devis R2 `17f5c2eb…`, attendu `11,32 USD` / plafond `36 USD`) dès que les flux Neon précédents sont libérés.

---

## 3. Tous les livrables nouveaux versés sur `origin/main` dans cette fenêtre (`R-5215` à `R-5243`)

1. **Conception des sondes boîte blanche (`v2`) et table de correspondance SCELLÉES avant tout score du barreau 5** (`R-5216`, `R-5217`) : `table-correspondance-issues-adaptateurs-jumeaux-v1.md` (`fb8f4c64…`), `conception-sondes-v2.md` (`5242bdbd…`).
2. **Additif 1 aux sondes du barreau 8 SCELLÉ 6h avant l'échéance** (`R-5223`) : `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md` (`fc5b0610…`), `SCELLEMENT-ADDITIF-1-SONDES-IIB`.
3. **Lecture et Verdict scellés de la base boîte noire (`T0.8 v3`) ACHEVÉS** (`R-5229`, `R-5233`, `R-5235`) : `COURSE-T08`, `LECTURE-T08` (`origin/lecture/t08-bases-boite-noire-v3-v1`), `VERDICT-T08-V3` (`origin/verdict/t08-bases-boite-noire-v3-pour-lazar-v1`, `38817ad5…`, pour Lazar seul).
4. **Barreau 5 vérifié à 100 % et prêt à l'ouverture** (`R-5231`) : `SCORES-B5F` (`cc631cfa…`, `3 449/3 449` fichiers intègres). **Attend uniquement `sel-barreau5-formation-v1.txt` (`1516230c…`) et `table-etiquettes-b5f-v1.json` (`553cb395…`) de Lazar.**
5. **Sondes v2 — Additif de commit SCELLÉ (`40a9e45c…`), serveur Hetzner `177425658` en marche, ET correctif `erratum-4-npz` + `correspondance-rejeu-croise-v2` LIVRÉ (`R-5242`)** :
   - Versé dans `docs/notes/sondes-v2-effectifs-et-correspondance-v1/erratum-4-npz-v1/` (`formats_v1.py` `3be4e79d…`, `correspondance-rejeu-croise-v2.json` `9daefe3b…`, `erratum-4-sondes-bbis-npz.patch` `2658b549…`, **`236 passed, 0 failed`**).
   - **Suite immédiate** : faire contre-lire `erratum-4-npz-v1` par un lecteur R2 classe B neuf avant application sur la branche `sondes-v2/code-v2` !
6. **Saboteur à budget (`GO-2026-11-23-39`) — Devis `v2` conforme (`9a4a794c…`, `3,01 USD` attendu / `11 USD` plafond) ET pièces côté exposé `v7` (`D-13`, `D-14`, `additif 2` brouillon) VERSÉES (`R-5243`)** :
   - Versées dans `docs/notes/rejeu-activations-saboteur-voie-a-v1/prealables-cote-expose-v7-brouillon/` (`interface-passe-cote-moniteurs-v7.md`, `comparaison-interface-v6-v7-v1.json`, `fiche-decision-lazar-additif-2-v1.md`, `lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1-brouillon1.md`).
   - **Suite immédiate** : lancer un contre-lecteur R2 neuf côté moniteurs sur `additif 2` + aligner `CODE-PASSE-IIB`, puis présenter la ligne de confirmation finale `GO` à Lazar (`3,01 USD` sur A100 80 Go).
7. **Plan Turing — Charte (`69c8deae…`), Cartographie des 18 verrous ouverts (`00c551b0…`), Théorèmes d'évasion Halberstadt (`bf9d442d…`), Feuille de route `v2` après double revue Carbon (`strategie-cibles-et-feuille-de-route-publication-papier-d-v2.pdf`), Dossier 1 Langage (`baca15c9…`), ET Épreuve rétrodictive Pas 0 Rang 1 Foyers de Tension (`R-5241`)** :
   - `docs/notes/plan-turing-v1/pas0-rang1-foyers-tension-v1/rapport-pas0-rang1-foyers-tension-v1.md` (`0a617ab1…`) : verdict primaire **`RÉFUTÉ` (`AUC = 0,1667`, $\rho_S = -0,6273$, `0 USD`)** démontrant l'artefact de registre disciplinaire des marqueurs lexicaux naïfs d'épicycles et validant le passage à l'extraction sémantique/relationnelle d'incompatibilités (`IDE-2026-11-23-041`).

---

## 4. Rappel horaire programmé (`registres/rappels.md`)
- **`2026-11-24T08:47Z` (`09:47` heure de Paris)** : rappeler à Lazar sa lecture programmée de `docs/notes/entretien-controle-diffus-v1/note-entretien-controle-diffus-v7.{md,pdf}` (`7899bfb9…`).
