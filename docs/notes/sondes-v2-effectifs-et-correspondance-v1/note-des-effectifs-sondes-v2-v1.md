# Note des effectifs des diagnostics préalables des sondes (v2, Option A)

- **Session rédactrice** : `sous-agent-83ff952349ac7c27e7a058fe8138c9d8` (sous-agent neuf habilité, mandats `R-5198`, `R-5209` Option A, `GO-2026-11-23-18`, `-33`, `-36`).
- **Date (UTC)** : `2026-11-24T03:58:37Z`.
- **Spécification de référence** : `docs/notes/sondes-v2-concepteur-opus-v1/spec-note-des-effectifs-v2.md` et ses trois errata d'Option A (commits `14bfd7e8e` à `0ce9e3511` sur `sondes-v2/code-v2`).
- **Pièces lues (en mémoire, sans écriture dans les dépôts)** :
  - Activations gardées de `20261123-044043-b5f-lecture` (branche distante `donnees/barreau5-familles-jumelles-v1-lecture`, commit `2e8e662359e192a13cec0cadeb4a218385c8ff59`) : `donnees/20261123-044043-b5f-lecture/garde-activations.json` (`8339bc781d37aac100bdca1c7af4819b97a5460e8a13dffe486acb5ca498787e`), `donnees/20261123-044043-b5f-lecture/inventaire-activations.json` (`be63fcfd9015e1ae76d2670a8af5c8c56026b6581a9587be104d7f6b3beb71ba`), `runs/20261123-044043-b5f-lecture/manifeste.json` (`37b0ade671774ceb474cc1205439f5abc15c16c3221cc9dfcfc35ce8d2bd1d0d` — métadonnées du chemin de calcul uniquement) et leurs compagnons `.sha256`.
  - Table `SCORES-BBIS` (`origin/donnees/t07-etape-b-bis-v2`, `diag/20261118-154143-bbis-t07-v1/sondes-bbis.json`, empreinte `645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62`, ligne `SCORES-BBIS (registres/t07-etape-b-bis-v1.md, ligne 8, 2026-11-18T19:43:48Z)`) : métadonnées de plan de `sondes-bbis.json` et, dans les trois morceaux `.npz` scellés qu'il cite, exclusivement les noms de membres ZIP et les tableaux de chaînes `*__cles.npy` et `*__taches.npy` :
  - `donnees/20261118-154143-bbis-t07-v1/scores-bbis-000.npz` (`38e3f9b305945306688f101b37e30d84945aba39650102d8407c8e51be4a79cc`, 88480822 octets, sources : P-S100, P-S25, P-S50)
  - `donnees/20261118-154143-bbis-t07-v1/scores-bbis-001.npz` (`62628d376f07032ce870078fe7dffd98252be01bc5fcbcf724ed2b689ee22169`, 89985386 octets, sources : P-S50, P-S75, P-instruit)
  - `donnees/20261118-154143-bbis-t07-v1/scores-bbis-002.npz` (`129a690f8d679a4495fc936de5219cb32c22256da9262aebb4ad4c32916d2279`, 60833282 octets, sources : P-instruit)
  - Pièces de méthode dans `/home/antigravity/worktrees/sondes-v2-code` (`0ce9e3511`) : spécifications v2, plan et devis v2 (+ erratum 1 et `devis_epreuve_plantee_v2.py`), errata 1 à 3 d'Option A, `prereg/diagnostics-prealables-sondes-v1.md`, `decisions-concepteur-sondes-v2-v2.md`, `src/controle_ia/sondes_v2/formats_v1.py`, `magasin_v1.py`, `statistiques_v2.py`, `scellement.py`, `tests/test_sondes_v2_formats.py`, et code de schéma `src/controle_ia/t07bbis/{commun_v1,marche_v4,validation_imbriquee_v1,lecture_v5}.py`.
- **Pièces NON ouvertes (cloisonnement strict)** : aucun tableau `.npy` d'activations (ni `np.load`, ni en-tête binaire, ni valeurs, ni forme) ; aucun tableau ni aucune colonne de scores dans `SCORES-BBIS` ni statistique dérivée ; aucune table de l'ouvreur ; aucun fichier fermé des empreintes ; aucun verdict ni texte scellé du test sur les adaptateurs jumeaux (`prereg/*barreau5*`) ; aucun fichier sous `docs/verdicts/`, `coffre/`, `essai/`, ni aucune pièce du saboteur.

## Synthèse des effectifs et incidence sur le devis

- **Activations gardées (`une_sur_dix`, couche 15)** : 47 séries au total dans la garde (33 nommées : `nu`, 30 adaptateurs opaques `X-01` à `X-30`, 2 ancres sans mot de rôle ; + 14 séries publiques comptées, non nommées : 3 propres, 2 ancres, 9 autres à nom public), 3008 fichiers gardés (sur 90240 dans l'inventaire sur 3 couches). Clés communes `K` : **64 actions** réparties sur **40 tâches** (19 à 1 action, 19 à 2 actions, 1 à 3 actions, 1 à 4 actions), identiques dans les 44 séries non propres (`non_propres_aux_cles_communes = true`, `nu_relit_les_cles_communes = true`) et distinctes des 3 séries propres (`distinctes_des_cles_propres = true`).
- **Rejeu croisé (`SCORES-BBIS`)** : **4 doses** (`0.25`, `0.5`, `0.75`, `1.0`), 2 plis externes disjoints de 32 tâches chacun (**64 tâches tenues** par dose), exactement **10 actions par tâche** dans chacune des 4 cases (`320` actions par pli et par case, `640` par dose et par case, `10 240` lignes au total), 100 % appariées par clé entre adaptateur et modèle nu. **Contrôle du chemin : `contrôle absent`** (0 action présente en origine et en relu pour un même couple poids/source ; aucun cas mixte).
- **Cases de l'épreuve plantée** : `etalon = {taches: 40, actions: 2}` (`TA_etalon = 80`), `extension_taches_actions = false` ; `complet = {paires: 8, taches: 64, actions: 10, doses_holm: 4}` (`TA_rejeu = 640`).
- **Devis (`plan-epreuve-plantee-et-devis-v2.md`, § 5)** : l'effectif du rejeu croisé (`TA_rejeu = 640`) est 3,33 fois supérieur au scénario « très grand » du devis (`192`). Selon le modèle exact de `devis_epreuve_plantee_v2.py` (500 répliques, `ccx63` à `hel1` à 1,3942 EUR/h, taux 1,25) :
  - Étalon seul (52 cases, option A) : **184.7 h CPU** = **6.70 USD** (9.59 USD au plus haut), 3.85 h sur une `ccx63`.
  - Complet seul, option C (39 rejeux) : **1056.0 h CPU** = **38.34 USD** (54.81 USD au plus haut), 22.00 h sur une `ccx63`.
  - Complet seul, option A (199 rejeux) : **4324.1 h CPU** = **157.00 USD** (224.45 USD au plus haut), 90.08 h sur une `ccx63`.
  - **Total recommandé (A étalon + C complet)** : **1240.7 h CPU** = **45.05 USD** (64.40 USD au plus haut), 25.85 h sur une `ccx63` (plafond 1,5x : 67.57 USD à `hel1`, 96.60 USD au plus haut) — **HORS DU PLAFOND de 27.10 USD de `GO-2026-11-23-18`**.

## Bloc JSON (seul lu par `charger_note_effectifs`)

```json
{
 "format": "note-effectifs-sondes-v2-v1",
 "redigee_par": "sous-agent-83ff952349ac7c27e7a058fe8138c9d8",
 "date_utc": "2026-11-24T03:58:37Z",
 "aveuglement": {
  "activations": "non ouvertes",
  "scores": "non ouverts",
  "table_de_l_ouvreur": "non ouverte",
  "verdict_adaptateurs_jumeaux": "non ouvert"
 },
 "activations": {
  "dossier_run": "donnees/20261123-044043-b5f-lecture",
  "inventaire_sha256": "be63fcfd9015e1ae76d2670a8af5c8c56026b6581a9587be104d7f6b3beb71ba",
  "garde_sha256": "8339bc781d37aac100bdca1c7af4819b97a5460e8a13dffe486acb5ca498787e",
  "regle_garde": "une_sur_dix",
  "couches_gardees": [
   15
  ],
  "chemin_de_calcul": {
   "programme": "relecture_v1@efc3f8350ebcbc84658c726f742c8b8e0374eee3",
   "precision": "float32 (sauvegarde float16)",
   "mode": "relu à texte imposé",
   "gabarit": "meta-llama/Llama-3.1-8B-Instruct@0e9e39f249a16976918f6564b8830bc894c89659 (date_string=26 Jul 2024)",
   "source": "manifeste",
   "identique_pour_toutes_les_series": true
  },
  "series": [
   {
    "nom": "X-01",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-02",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-03",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-04",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-05",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-06",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-07",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-08",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-09",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-10",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-11",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-12",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-13",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-14",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-15",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-16",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-17",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-18",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-19",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-20",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-21",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-22",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-23",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-24",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-25",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-26",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-27",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-28",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-29",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "X-30",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "ancre-confirmation-temoin",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "ancre-exploratoire-temoin",
    "categorie": "adaptateur",
    "cles": 64
   },
   {
    "nom": "nu",
    "categorie": "nu",
    "cles": 64
   }
  ],
  "series_publiques": {
   "propre": 3,
   "ancre": 2,
   "autres_a_nom_public": 9
  },
  "attestation_series_publiques": "aucune série comptée dans series_publiques n'est membre d'une paire opaque du test sur les adaptateurs jumeaux ; leurs noms ne sont pas écrits",
  "cles_communes": {
   "definition": "clés de la série nu, identiques dans toute série non propre",
   "actions": 64,
   "taches": 40,
   "taches_par_nombre_d_actions": {
    "1": 19,
    "2": 19,
    "3": 1,
    "4_ou_plus": 1
   },
   "distinctes_des_cles_propres": true
  },
  "nu_relit_les_cles_communes": true,
  "non_propres_aux_cles_communes": true
 },
 "scores_bbis": {
  "table": {
   "chemin": "diag/20261118-154143-bbis-t07-v1/sondes-bbis.json",
   "sha256": "645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62",
   "ligne_registre": "SCORES-BBIS (registres/t07-etape-b-bis-v1.md, ligne 8, 2026-11-18T19:43:48Z)"
  },
  "colonnes": [
   "controle_carte_processeur",
   "couches",
   "couple_controle",
   "decision_variante",
   "dispersion_ordres_calcul",
   "doses",
   "duree_s",
   "fichier_sondes",
   "fichiers_planchers",
   "fichiers_scores",
   "graines_derivees",
   "journal",
   "manifeste",
   "plis",
   "run_id",
   "sans_aucune_aire",
   "sources",
   "texte",
   "variante"
  ],
  "doses": [
   {
    "dose": "0.25",
    "plis": [
     {
      "pli": "0",
      "taches_tenues": 32,
      "actions": {
       "adaptateur|saboteur": 320,
       "nu|saboteur": 320,
       "adaptateur|honnete": 320,
       "nu|honnete": 320
      },
      "chemins": {
       "adaptateur|saboteur": "origine",
       "nu|saboteur": "relu",
       "adaptateur|honnete": "relu",
       "nu|honnete": "origine"
      },
      "actions_en_origine_et_en_relu": 0,
      "taches_avec_controle_du_chemin": 0
     },
     {
      "pli": "1",
      "taches_tenues": 32,
      "actions": {
       "adaptateur|saboteur": 320,
       "nu|saboteur": 320,
       "adaptateur|honnete": 320,
       "nu|honnete": 320
      },
      "chemins": {
       "adaptateur|saboteur": "origine",
       "nu|saboteur": "relu",
       "adaptateur|honnete": "relu",
       "nu|honnete": "origine"
      },
      "actions_en_origine_et_en_relu": 0,
      "taches_avec_controle_du_chemin": 0
     }
    ]
   },
   {
    "dose": "0.5",
    "plis": [
     {
      "pli": "0",
      "taches_tenues": 32,
      "actions": {
       "adaptateur|saboteur": 320,
       "nu|saboteur": 320,
       "adaptateur|honnete": 320,
       "nu|honnete": 320
      },
      "chemins": {
       "adaptateur|saboteur": "origine",
       "nu|saboteur": "relu",
       "adaptateur|honnete": "relu",
       "nu|honnete": "origine"
      },
      "actions_en_origine_et_en_relu": 0,
      "taches_avec_controle_du_chemin": 0
     },
     {
      "pli": "1",
      "taches_tenues": 32,
      "actions": {
       "adaptateur|saboteur": 320,
       "nu|saboteur": 320,
       "adaptateur|honnete": 320,
       "nu|honnete": 320
      },
      "chemins": {
       "adaptateur|saboteur": "origine",
       "nu|saboteur": "relu",
       "adaptateur|honnete": "relu",
       "nu|honnete": "origine"
      },
      "actions_en_origine_et_en_relu": 0,
      "taches_avec_controle_du_chemin": 0
     }
    ]
   },
   {
    "dose": "0.75",
    "plis": [
     {
      "pli": "0",
      "taches_tenues": 32,
      "actions": {
       "adaptateur|saboteur": 320,
       "nu|saboteur": 320,
       "adaptateur|honnete": 320,
       "nu|honnete": 320
      },
      "chemins": {
       "adaptateur|saboteur": "origine",
       "nu|saboteur": "relu",
       "adaptateur|honnete": "relu",
       "nu|honnete": "origine"
      },
      "actions_en_origine_et_en_relu": 0,
      "taches_avec_controle_du_chemin": 0
     },
     {
      "pli": "1",
      "taches_tenues": 32,
      "actions": {
       "adaptateur|saboteur": 320,
       "nu|saboteur": 320,
       "adaptateur|honnete": 320,
       "nu|honnete": 320
      },
      "chemins": {
       "adaptateur|saboteur": "origine",
       "nu|saboteur": "relu",
       "adaptateur|honnete": "relu",
       "nu|honnete": "origine"
      },
      "actions_en_origine_et_en_relu": 0,
      "taches_avec_controle_du_chemin": 0
     }
    ]
   },
   {
    "dose": "1.0",
    "plis": [
     {
      "pli": "0",
      "taches_tenues": 32,
      "actions": {
       "adaptateur|saboteur": 320,
       "nu|saboteur": 320,
       "adaptateur|honnete": 320,
       "nu|honnete": 320
      },
      "chemins": {
       "adaptateur|saboteur": "origine",
       "nu|saboteur": "relu",
       "adaptateur|honnete": "relu",
       "nu|honnete": "origine"
      },
      "actions_en_origine_et_en_relu": 0,
      "taches_avec_controle_du_chemin": 0
     },
     {
      "pli": "1",
      "taches_tenues": 32,
      "actions": {
       "adaptateur|saboteur": 320,
       "nu|saboteur": 320,
       "adaptateur|honnete": 320,
       "nu|honnete": 320
      },
      "chemins": {
       "adaptateur|saboteur": "origine",
       "nu|saboteur": "relu",
       "adaptateur|honnete": "relu",
       "nu|honnete": "origine"
      },
      "actions_en_origine_et_en_relu": 0,
      "taches_avec_controle_du_chemin": 0
     }
    ]
   }
  ],
  "nombre_de_doses": 4
 },
 "cases_de_l_epreuve_plantee": {
  "etalon": {
   "taches": 40,
   "actions": 2
  },
  "complet": {
   "paires": 8,
   "taches": 64,
   "actions": 10,
   "doses_holm": 4
  },
  "extension_taches_actions": false
 },
 "minimums": {
  "cles_communes": "atteints",
  "rejeu_par_dose": {
   "0.25": "atteints",
   "0.5": "atteints",
   "0.75": "atteints",
   "1.0": "atteints"
  }
 },
 "reserves": [
  "Format physique de SCORES-BBIS : diag/20261118-154143-bbis-t07-v1/sondes-bbis.json est un index JSON (sans_aucune_aire=true) qui référence trois archives .npz scellées (donnees/20261118-154143-bbis-t07-v1/scores-bbis-000.npz, -001.npz et -002.npz), et non un fichier plat JSONL ou CSV ; les variables de prédicteurs triviaux (longueur, pas, valeur_declaree) ne figurent pas comme tableaux dans ces .npz (seul le rang de pas est encodé dans la chaîne cle=__p<pas> ; longueur et valeur_declaree vivent hors de SCORES-BBIS, dans mesures-t06.npz). Comme charger_table_bbis (commit 0ce9e3511) n'accepte que jsonl ou csv, un exportateur déterministe sans lecture de score (sondes-bbis.json + scores-bbis-*.npz -> JSONL scellé) ou un erratum de formats_v1.py est requis avant l'ouverture du rejeu croisé.",
  "Cellule P-instruit exclue des doses : sondes-bbis.json comporte une cinquième source (P-instruit, sabotage par instruction sans adaptateur LoRA, dose=null, absente de doses=[0.25, 0.5, 0.75, 1.0]) ; seules les quatre doses de l'adaptateur (0.25, 0.5, 0.75, 1.0) entrent dans le rejeu croisé (nombre_de_doses=4, doses_holm=4).",
  "Séries propres et clés communes : les trois séries propres (comptées dans series_publiques.propre, jamais nommées) vivent dans des séries distinctes de nu et des 43 autres séries non propres, mais réemploient le modèle de nom de fichier <tache>__p<pas>.npy sur leurs propres épisodes ; sans ouvrir aucun .npy, les tailles en octets d'inventaire-activations.json confirment 64/64 tailles identiques à nu pour chacune des 43 autres séries non propres, contre 0/64, 0/64 et 1/64 pour les trois séries propres (distinctes_des_cles_propres=true, extension_taches_actions=false).",
  "Contrôle du chemin : aucune action de SCORES-BBIS n'est présente à la fois en série d'origine et en série relue pour un même couple (poids, source) ; l'état est « contrôle absent » sur les quatre doses (aucun cas mixte).",
  "Nom court du programme dans chemin_de_calcul.programme : la commande complète de runs/20261123-044043-b5f-lecture/manifeste.json comporte dans le nom du paquet Python un mot bloqué par la garde MOTS_DE_ROLE sur la section activations ; le champ porte donc le module exact et le commit exact du manifeste (relecture_v1@efc3f8350ebcbc84658c726f742c8b8e0374eee3), sans affaiblir la garde."
 ]
}
```

## Réserves

1. Format physique de SCORES-BBIS : diag/20261118-154143-bbis-t07-v1/sondes-bbis.json est un index JSON (sans_aucune_aire=true) qui référence trois archives .npz scellées (donnees/20261118-154143-bbis-t07-v1/scores-bbis-000.npz, -001.npz et -002.npz), et non un fichier plat JSONL ou CSV ; les variables de prédicteurs triviaux (longueur, pas, valeur_declaree) ne figurent pas comme tableaux dans ces .npz (seul le rang de pas est encodé dans la chaîne cle=__p<pas> ; longueur et valeur_declaree vivent hors de SCORES-BBIS, dans mesures-t06.npz). Comme charger_table_bbis (commit 0ce9e3511) n'accepte que jsonl ou csv, un exportateur déterministe sans lecture de score (sondes-bbis.json + scores-bbis-*.npz -> JSONL scellé) ou un erratum de formats_v1.py est requis avant l'ouverture du rejeu croisé.
2. Cellule P-instruit exclue des doses : sondes-bbis.json comporte une cinquième source (P-instruit, sabotage par instruction sans adaptateur LoRA, dose=null, absente de doses=[0.25, 0.5, 0.75, 1.0]) ; seules les quatre doses de l'adaptateur (0.25, 0.5, 0.75, 1.0) entrent dans le rejeu croisé (nombre_de_doses=4, doses_holm=4).
3. Séries propres et clés communes : les trois séries propres (comptées dans series_publiques.propre, jamais nommées) vivent dans des séries distinctes de nu et des 43 autres séries non propres, mais réemploient le modèle de nom de fichier <tache>__p<pas>.npy sur leurs propres épisodes ; sans ouvrir aucun .npy, les tailles en octets d'inventaire-activations.json confirment 64/64 tailles identiques à nu pour chacune des 43 autres séries non propres, contre 0/64, 0/64 et 1/64 pour les trois séries propres (distinctes_des_cles_propres=true, extension_taches_actions=false).
4. Contrôle du chemin : aucune action de SCORES-BBIS n'est présente à la fois en série d'origine et en série relue pour un même couple (poids, source) ; l'état est « contrôle absent » sur les quatre doses (aucun cas mixte).
5. Nom court du programme dans chemin_de_calcul.programme : la commande complète de runs/20261123-044043-b5f-lecture/manifeste.json comporte dans le nom du paquet Python un mot bloqué par la garde MOTS_DE_ROLE sur la section activations ; le champ porte donc le module exact et le commit exact du manifeste (relecture_v1@efc3f8350ebcbc84658c726f742c8b8e0374eee3), sans affaiblir la garde.
