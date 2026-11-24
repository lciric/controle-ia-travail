# Passation et point d'état complet — Session mère Antigravity (`ff6e9350`), tout ce qui est nouveau depuis `2026-11-23-2220`

- **Session mère active** : Antigravity `v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f` (la mère Claude Code `session_016QhUrvi45g3jX5saFefVED` s'est suspendue proprement à `R-5220` pour éviter deux mères sur `main`).
- **Horodatage** : `2026-11-24T05:56:00Z` (`date -u`).
- **Plage de décisions couverte depuis la dernière passation mère (`2026-11-23-2220`)** : `R-5203` à `R-5240` et `GO-2026-11-23-38` à `GO-2026-11-24-04`.
- **Clés d'environnement** : 29 variables déposées par Lazar dans `/home/antigravity/env-setup.sh` (`chmod 600`, hors dépôt, à sourcer par `set -a && source /home/antigravity/env-setup.sh && set +a`). *Note de facturation vérifiée* : `GEMINI_API_KEY` et `GEMINI_API_KEY_2` sont actives (`HTTP 200`), tandis que `GEMINI_API_KEY_3` est épuisée (`HTTP 402`).

---

## 1. Machines louées et démons actifs à `2026-11-24T05:56Z`

1. **Serveur processeur Hetzner `177425658` (`sondes-v2-etalon-v4-20261124-0537`) — EN MARCHE** (`GO-2026-11-24-02`, `R-5238`) :
   - Type : `ccx33` (8 cœurs dédiés) à `hel1` (`0,22596 EUR/h` brut = `0,28245 USD/h`), créé à `2026-11-24T05:37:03Z` après refus de quota 48 cœurs dédiés sur `ccx63`.
   - Tâche : épreuve à vérité plantée des sondes boîte blanche (`programme_monde_plante_v4.py`, commit figé `0ce9e3511`, mode `etalon_seul`, `52` cases, `TA_etalon = 80`, durée attendue `≈ 23,1 h`, coût attendu `≈ 6,52 USD`), branche de sortie `calcul/sondes-v2-epreuve-plantee-v4`.
   - Remparts d'arrêt et destruction par identifiant (`R10`) : minuterie interne `31h30` dans `amorce-hetzner-sondes-v2-ccx63-v2.sh` (`fdbc193d…`) + démon externe persistant (`task-943` sur la VM mère, coupure à `32 h` ou `15 USD`).
2. **Vast.ai — `0` instance en marche** :
   - Seules les **4 instances arrêtées intouchables** (`58936096`, `58936099`, `58936100`, `60988826` — **ne jamais détruire**). `62096662` détruite à `R-5204`. Solde Vast.ai : **`20,42 USD`**.
3. **Démons d'appels d'interfaces actifs sur la VM mère** :
   - **`task-847` — Collisionneur sur la boucle de rétroaction entre l'organisme d'idéation et le programme de contrôle** (`GO-2026-11-24-03`, `R-5227`, plafond `36 USD` = `18 USD/bras`, `GEMINI_API_KEY` + `RR_ANTHROPIC_API_KEY_LUC`) : 8 cellules sur 9 du bras principal achevées (`6,10 USD` cumulés), 9e cellule (`E3-T3-reponse-C` Neon) en cours avant enchaînement automatique sur le bras témoin ultra-neutre.
   - **Démon Carbon + Collisionneur sur le positionnement de publication du théorème d'évasion en post-entraînement** (`GO-2026-11-24-04`, `R-5240`, sur `GEMINI_API_KEY_2` + `RR_ANTHROPIC_API_KEY_LUC`, plafond `20 USD` dont `18 USD` collisionneur) : exécute d'abord les deux appels directs à Carbon effort élevé (réponse indépendante puis relecture critique de la feuille de route), puis l'étage 3 du collisionneur (`Opus 5.5 + Carbon + Neon`).

---

## 2. Scellements décisifs, verdicts et livrables versés sur GitHub depuis `2026-11-23-2220`

### A. Chantier prioritaire de l'entretien du 1er décembre (saboteur, sondes, base boîte noire, billet)
1. **Conception des sondes boîte blanche et table de correspondance SCELLÉES sur `main`** (`R-5216`, `R-5217`) :
   - `docs/notes/conception-sondes-boite-blanche-fable-v1/table-correspondance/table-correspondance-issues-adaptateurs-jumeaux-v1.md` (`fb8f4c64…`) ;
   - `docs/notes/conception-sondes-boite-blanche-fable-v1/conception-sondes-v2.md` (`5242bdbd…`) et vérification R2 finale `5b6e317b…`.
2. **Additif 1 aux sondes du barreau 8 SCELLÉ sur `main` avant l'échéance de `10:20:38Z`** (`R-5223`, `04:21:08Z`) :
   - `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1.md` (`fc5b0610…`), ligne `SCELLEMENT-ADDITIF-1-SONDES-IIB` inscrite dans `registres/sondes-iib-v1.md`, vérification R2 `v2` `7cb6a8dd…`, attestations `AD-2` (`6b15e1dc…`) et `D-6` v1 (`8f6b5025…`, `E-1 = non`).
3. **Base boîte noire sur les tâches d'évaluation (`T0.8 v3`) — LECTURE ET VERDICT SCELLÉS** (`R-5229`, `R-5233`, `R-5235`) :
   - Lignes `COURSE-T08` (`67ebcb2f…`), `LECTURE-T08` (`cefb6d2c…`, branche isolée `lecture/t08-bases-boite-noire-v3-v1` `ea134d29a`) et `VERDICT-T08-V3` (`38817ad5…`, branche isolée pour Lazar seul `verdict/t08-bases-boite-noire-v3-pour-lazar-v1` `f80026c2f`) inscrites dans `registres/scellements-v1.md` (zéro chiffre ouvert par la mère).
4. **Relecture décisive des adaptateurs jumeaux (barreau 5) — PRÊTE À L'OUVERTURE** (`R-5231`) :
   - 3 449/3 449 fichiers vérifiés octet par octet (`2e8e6623…`), ligne `SCORES-B5F` (`cc631cfa…`) inscrite dans `registres/barreau5-familles-jumelles-v1.md`. **Attend uniquement le dépôt par Lazar du sel secret `sel-barreau5-formation-v1.txt` (`1516230c…`) et de `table-etiquettes-b5f-v1.json` (`553cb395…`)**.
5. **Sondes boîte blanche v2 — Additif de commit SCELLÉ et épreuve plantée partie** (`R-5237`, `R-5238`) :
   - `prereg/diagnostics-prealables-sondes-v1-additif-commit-v1.md` (`40a9e45c…`), `note-des-effectifs-sondes-v2-v1.md` (`7338a3dc…`, conforme `5d46ac87…`). Correctif classe B `sondes_bbis_npz` + `correspondance-rejeu-croise-v2` en cours chez le sous-agent `245d8f72`.
6. **Rejeu des activations internes du saboteur à budget (`GO-2026-11-23-39`) — Devis `v2` VÉRIFIÉ CONFORME** (`R-5230`) :
   - `docs/notes/rejeu-activations-saboteur-voie-a-v1/devis-passe-activations-saboteur-voie-a-v2.md` (`9a4a794c…`, vérif R2 `bbb83d87…` : `3,01 USD` attendu / `11,00 USD` plafond sur A100 80 Go, couvert par le solde Vast.ai de `20,42 USD`). Préparation côté exposé de la note d'interface `v7` (`D-14`), de `D-13` et du brouillon court d'`additif 2` en cours chez `97f22687` (`R-5239`).
7. **Billet sur les sondes v2, Tableau des verdicts et Plan d'entretien** :
   - Billet v2 vérifié conforme sur `origin/billet/sondes-redacteur-habilite-v1` (`ef3930176`) ;
   - Tableau réservé des verdicts sur `coffre/tableau-verdicts-lazar-v1` (`5a31ba5f`, `R-5212`) ;
   - Note d'entretien v7 (`7899bfb9…`, `R-5209`) et plan jour par jour jusqu'au 1er décembre (`ad5c9a9e…`, `R-5210`).

### B. Plan Turing (`R-5224`, `R-5225`, `R-5228`, `R-5232`, `R-5234`, `R-5236`)
1. **Charte directrice unifiée du Plan Turing** : `docs/notes/plan-turing-v1/plan-turing-directeur-v1.md` (`69c8deae…`) + note d'explication des mondes plantés `explication-et-reflexion-mondes-plantes-c2-et-plan-quatre-pas-v1.md`.
2. **Cartographie vérifiable des 18 verrous mathématiques ouverts et preuve + test de mort de la conjecture d'évasion en post-entraînement (`GO-2026-11-24-01`, `0 USD`)** :
   - `docs/notes/cartographie-mathematiques-ouvertes-v1/cartographie-verrous-mathematiques-ia-v1.md` (`00c551b0…`, rappel témoins `18/20 = 90 %`, rétrodiction `7/8 = 87,5 %`, `5/5` tests de mort) ;
   - `docs/notes/cartographie-mathematiques-ouvertes-v1/elucidation-loi-halberstadt-post-entrainement-v1.md` (`bf9d442d…`, `0/14 000` contre-exemple).
3. **Pack de publication `v2` (LessWrong, GitHub, manuscrit LaTeX arXiv) relu par Carbon effort élevé et corrigé (10/10 remarques)** (`R-5234`) :
   - `docs/notes/cartographie-mathematiques-ouvertes-v1/publication-evasion-post-entrainement-v1/` (`commentaire-…-v2.md` `72e99d30…`, `billet-…-v2.md` `6a9f0f3e…`, `manuscrit-arxiv/main-v2.tex` `1072e00b…`, `github-page/README-v2.md` `ffa64d60…`, `verifier_exemples_papier_v2.py` `4183ce84…`).
4. **Dossier 1 sur la structure du langage (34 sources) + devis vérifié et test aveugle de neutralité du collisionneur groupé** (`R-5236`, `3a2767b13`) :
   - `docs/notes/protocole-x-structure-du-langage-v1/synthese-structure-du-langage-v1.md` (`baca15c9…`), neutralité `0,22 / 0,28 / 0,18 < 0,50`, devis R2 `17f5c2eb…`, assemblage groupé unifié prêt au départ (`11,32 USD` attendu avant 1er déc. / plafond `36 USD`).
5. **En cours sur le créneau Plan Turing (`ee945812`)** : préenregistrement et extraction rétrodictive sur processeur des foyers de tension et d'épicycles `2024 -> 2025–2026` (Pas 0, Rang 1).
6. **Nouvelle session parallèle ouverte par `GO-2026-11-24-04`** : session dédiée au **Papier D** (voir passation dédiée `registres/passations/2026-11-24-0555-session-papier-d-evasion-post-entrainement.md`, travaillant exclusivement sur la branche `papier-d/evasion-post-entrainement-v1` pour ne jamais entrer en conflit avec `main`).

---

## 3. Ce qui attend un geste ou un mot de Lazar
1. **Barreau 5 (`SCORES-B5F` inscrit)** : déposer `sel-barreau5-formation-v1.txt` (`1516230c…`) et `table-etiquettes-b5f-v1.json` (`553cb395…`) pour lancer immédiatement l'ouverture et le verdict.
2. **Passe de recalcul des activations du saboteur à budget (`GO-2026-11-23-39`)** : dès retour de `97f22687`, confirmer l'accord dédié sur le devis `v2` (`9a4a794c…`, `3,01 USD` attendu / `11,00 USD` plafond) et le court additif 2 mécanique de format si `.json` est confirmé.
3. **Seconde relecture des lentilles neuronales (étape 16)** : révocation de la clé restreinte d'export par Lazar lorsqu'il le souhaite.
