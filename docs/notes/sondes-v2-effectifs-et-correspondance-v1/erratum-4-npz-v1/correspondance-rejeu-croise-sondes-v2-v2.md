# Table de correspondance des champs du rejeu croisé (sondes v2, v2)

- **Session rédactrice (v2)** : `sous-agent-245d8f72ff2a9e2bece4bfdac5e3049e` (développeur de classe B des sondes v2, strictement distinct du rédacteur v1 `sous-agent-83ff952349ac7c27e7a058fe8138c9d8` et du contre-lecteur R2 `2b0a91ecabac7cc44ea341dda083afdd`, sous `R-5209` point 2 et `R-5218`).
- **Remplace** : `correspondance-rejeu-croise-sondes-v2-v1.md` (`1a634514…`) et `correspondance-rejeu-croise-v1.json` (`be75f2af…`), gardés tels quels (R12), après application des deux corrections fermées de `contre-lecture-r2-note-effectifs-et-correspondance-v1.md` (`5d46ac87…`).
- **Date (UTC)** : `2026-11-24T06:08:30Z`.
- **Spécification de référence** : `spec-correspondance-rejeu-croise-v2.md` (`31296b05…`) et son `erratum-4-spec-correspondance-rejeu-croise-v2-npz.md` (`789e4389…`), qui prime. Classe B : soumis à vérification de contre-lecture R2 et scellement avant toute ouverture des données réelles et avant le verdict du test sur les adaptateurs jumeaux.
- **Fichier JSON compagnon scellé (lu par `charger_table_bbis`)** : `correspondance-rejeu-croise-v2.json` (objet JSON identique à l'octet au bloc ci-dessous).
- **Attestation d'aveuglement** : *aucune colonne de score lue ; seules les colonnes de plan et leurs valeurs distinctes.* Aucune activation (`.npy`), aucun verdict (`docs/verdicts/`), aucun fichier sous `coffre/`, aucune table de l'ouvreur ni aucun tableau de scores réel (`*__sonde.npy`, `*__plancher.npy`, `*__nul.npy`, `*__enc.npy`, `*__sc_sonde.npy`, `*__sonde_o2.npy`) n'a été ouvert ; les essais ont porté exclusivement sur des archives `.npz` synthétiques à scores factices.

## 1. Fermeture des deux corrections de la contre-lecture R2 (`5d46ac87…`) et constats sur `SCORES-BBIS`

La ligne `SCORES-BBIS (registres/t07-etape-b-bis-v1.md, ligne 8, 2026-11-18T19:43:48Z)` désigne l'index JSON `diag/20261118-154143-bbis-t07-v1/sondes-bbis.json` (empreinte `645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62`, `sans_aucune_aire: true`), qui référence trois archives `.npz` scellées sur `origin/donnees/t07-etape-b-bis-v2` :

| Morceau `.npz` | SHA-256 inscrit dans `sondes-bbis.json` | Sources portées |
|---|---|---|
| `donnees/20261118-154143-bbis-t07-v1/scores-bbis-000.npz` | `38e3f9b305945306688f101b37e30d84945aba39650102d8407c8e51be4a79cc` | `P-S100`, `P-S25`, `P-S50` |
| `donnees/20261118-154143-bbis-t07-v1/scores-bbis-001.npz` | `62628d376f07032ce870078fe7dffd98252be01bc5fcbcf724ed2b689ee22169` | `P-S50`, `P-S75`, `P-instruit` |
| `donnees/20261118-154143-bbis-t07-v1/scores-bbis-002.npz` | `129a690f8d679a4495fc936de5219cb32c22256da9262aebb4ad4c32916d2279` | `P-instruit` |

Chaque morceau `.npz` stocke des tableaux nommés `<source_bbis>__e<pli>__<groupe>__<champ>.npy` (où `<groupe>` vaut `<serie>-<condition>` hors entrées `app*`, `nul` et `o2`).

- **Correction 1 fermée (`format_fichier = "sondes_bbis_npz"`)** : conformément à `erratum-4-spec-correspondance-rejeu-croise-v2-npz.md` (`789e4389…`), `formats_v1.charger_table_bbis` (`3be4e79d…`) prend nativement en charge `"format_fichier": "sondes_bbis_npz"`. Au seul moment de l'ouverture (étape 4), le chargeur vérifie l'empreinte de `sondes-bbis.json` (`645a172f…`) contre son compagnon `.sha256` et contre `table_source.sha256`, puis vérifie l'empreinte `SHA-256` de chacun des trois morceaux `scores-bbis-000..002.npz` avant d'assembler les tableaux (y compris lorsqu'une source ou un groupe est réparti entre deux morceaux, comme `P-S50` entre `000` et `001`). Aucun export `.jsonl` préalable n'est requis et aucun score n'est touché avant l'étape 4.
- **Correction 2 fermée (colonnes structurelles natives et sélection explicite des 16 couples)** : les colonnes synthétiques non natives `famille_bbis` et `cas_rejeu_croise` de la v1 sont supprimées. Le lecteur `"sondes_bbis_npz"` ne matérialise que les onze colonnes structurelles natives de `sondes-bbis.json` + `.npz` (`source_bbis`, `dose`, `pli_lu`, `serie`, `condition`, `groupe`, `couple_source_groupe = f"{source_bbis}/{groupe}"`, `champ_score`, `tache`, `cle`, `score`), et `selection` retient explicitement `"champ_score": "sonde"` ainsi que la liste fermée des **16 couples** `"P-S<d>/<groupe>"` ($d \in \{25, 50, 75, 100\}$, quatre cases du rejeu croisé par dose), écartant sans ambiguïté `O-T100`, `AT-honnete`, `O-saboteur`, `Jinstruit-saboteur` et l'intégralité de `P-instruit` (transferts `P-instruit/O-S25`, etc. compris). Toute valeur de la liste absente après sélection lève `GardeArret`.
- **Recodage de `poids` par `groupe`** : dans `t07bbis`, le préfixe de série `O` désigne l'adaptateur dans `O-S<d>` mais le modèle nu dans `O-honnete`. Le recodage de `poids` porte donc sur `groupe` (`O-S<d>`, `A<d>-honnete` → `adaptateur` ; `J<d>-S<d>`, `O-honnete` → `nu`), bijectif sur les quatre cases de chaque dose.
- **Attestation sur `chemin` (`quatre_cases_du_texte_scelle`)** : après `selection`, chacune des doses `0.25`, `0.5`, `0.75`, `1.0` ne porte que les quatre cases exactes du texte scellé (`O-S<d>` = `adaptateur|saboteur` en origine ; `J<d>-S<d>` = `nu|saboteur` en relu ; `A<d>-honnete` = `adaptateur|honnete` en relu ; `O-honnete` = `nu|honnete` en origine), chacune par un seul chemin (`10 240` lignes au total, `0` doublon, `0` clé sans jumelle, `0` action présente en origine et en relu pour un même `(poids, source)` ; contrôle du chemin = `absent`).
- **Attestation sur `tache_tenue` (`constante: true`)** : dans `validation_imbriquee_v1.py`, tous les groupes évalués hors `app` et `app_enc` ne contiennent que les 32 tâches de `taches_lues` du pli externe `e0` ou `e1`, disjointes des 32 tâches d'apprentissage (`32 + 32 = 64` tâches disjointes par dose ; le lecteur `sondes_bbis_npz` vérifie en outre mécaniquement l'inclusion dans `taches_lues`).
- **Variables de prédicteurs triviaux (`longueur`, `pas`, `valeur_declaree`)** : absentes des fichiers `SCORES-BBIS` (`sondes-bbis.json` et `scores-bbis-000..002.npz`), donc déclarées `{"absente": true}` (elles sortent proprement de `interaction_residuelle` dans `statistiques_v2.py`).
- **Sondes gelées sélectionnées par pli dans `sondes-bbis.json` (rappel de la note v1, sans score lu)** :

| Dose | Source | Pli | Nom de sonde | Réglage retenu | Famille | Agrégation | Couche | Tâches tenues |
|---|---|---|---|---|---|---|---|---|
| `0.25` | `P-S25` | `0` | `sonde-P-S25-e0` | `attention-c23-l2_0.001` | `attention` | `attention` | `23` | 32 |
| `0.25` | `P-S25` | `1` | `sonde-P-S25-e1` | `attention-c23-l2_0.1` | `attention` | `attention` | `23` | 32 |
| `0.5` | `P-S50` | `0` | `sonde-P-S50-e0` | `attention-c23-l2_0.1` | `attention` | `attention` | `23` | 32 |
| `0.5` | `P-S50` | `1` | `sonde-P-S50-e1` | `lineaire-c23-l2_0.001` | `lineaire` | `max` | `23` | 32 |
| `0.75` | `P-S75` | `0` | `sonde-P-S75-e0` | `lineaire-c15-l2_0.01` | `lineaire` | `max` | `15` | 32 |
| `0.75` | `P-S75` | `1` | `sonde-P-S75-e1` | `lineaire-c7-l2_0.001` | `lineaire` | `max` | `7` | 32 |
| `1.0` | `P-S100` | `0` | `sonde-P-S100-e0` | `lineaire-c15-l2_0.01` | `lineaire` | `max` | `15` | 32 |
| `1.0` | `P-S100` | `1` | `sonde-P-S100-e1` | `lineaire-c15-l2_0.01` | `lineaire` | `max` | `15` | 32 |

  Note : pour `P-S25` (`e0`, `e1`) et `P-S50` (`e0`), la sonde gelée retenue par la validation imbriquée de `t07bbis` emploie l'agrégation `attention` (et non `max`), point précisé au point 5 de `erratum-4-spec-correspondance-rejeu-croise-v2-npz.md` ; le tableau `*__sonde.npy` porte dans tous les cas le score brut de la sonde gelée du pli.

## 2. Table de correspondance (`correspondance-rejeu-croise-v2.json`)

```json
{
 "format": "correspondance-rejeu-croise-v1",
 "redigee_par": "sous-agent-245d8f72ff2a9e2bece4bfdac5e3049e",
 "date_utc": "2026-11-24T06:08:30Z",
 "attestation": "aucune colonne de score lue ; seules les colonnes de plan et leurs valeurs distinctes",
 "table_source": {
  "chemin": "diag/20261118-154143-bbis-t07-v1/sondes-bbis.json",
  "sha256": "645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62",
  "ligne_registre": "SCORES-BBIS (registres/t07-etape-b-bis-v1.md, ligne 8, 2026-11-18T19:43:48Z)",
  "format_fichier": "sondes_bbis_npz"
 },
 "selection": {
  "champ_score": "sonde",
  "couple_source_groupe": [
   "P-S25/O-S25",
   "P-S25/J25-S25",
   "P-S25/A25-honnete",
   "P-S25/O-honnete",
   "P-S50/O-S50",
   "P-S50/J50-S50",
   "P-S50/A50-honnete",
   "P-S50/O-honnete",
   "P-S75/O-S75",
   "P-S75/J75-S75",
   "P-S75/A75-honnete",
   "P-S75/O-honnete",
   "P-S100/O-S100",
   "P-S100/J100-S100",
   "P-S100/A100-honnete",
   "P-S100/O-honnete"
  ]
 },
 "colonnes": {
  "dose": "dose",
  "pli": "pli_lu",
  "source": "condition",
  "poids": "groupe",
  "chemin": {
   "regle": "quatre_cases_du_texte_scelle"
  },
  "tache": "tache",
  "cle": "cle",
  "score": "score",
  "longueur": {
   "absente": true
  },
  "pas": {
   "absente": true
  },
  "valeur_declaree": {
   "absente": true
  },
  "tache_tenue": {
   "constante": true
  }
 },
 "valeurs": {
  "source": {
   "S25": "saboteur",
   "S50": "saboteur",
   "S75": "saboteur",
   "S100": "saboteur",
   "honnete": "honnete"
  },
  "poids": {
   "O-S25": "adaptateur",
   "O-S50": "adaptateur",
   "O-S75": "adaptateur",
   "O-S100": "adaptateur",
   "A25-honnete": "adaptateur",
   "A50-honnete": "adaptateur",
   "A75-honnete": "adaptateur",
   "A100-honnete": "adaptateur",
   "J25-S25": "nu",
   "J50-S50": "nu",
   "J75-S75": "nu",
   "J100-S100": "nu",
   "O-honnete": "nu"
  }
 }
}
```
