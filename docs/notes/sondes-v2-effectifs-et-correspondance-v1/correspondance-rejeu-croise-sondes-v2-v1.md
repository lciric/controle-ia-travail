# Projet de table de correspondance des champs du rejeu croisé (sondes v2, v1)

- **Session rédactrice** : `sous-agent-83ff952349ac7c27e7a058fe8138c9d8` (sous-agent neuf habilité, mandats `R-5209` point 2 et `GO-2026-11-23-36`).
- **Date (UTC)** : `2026-11-24T03:58:37Z`.
- **Classe B** : projet soumis à contre-lecture par un autre modèle et scellement avant l'épreuve plantée et avant le verdict du test sur les adaptateurs jumeaux (`spec-correspondance-rejeu-croise-v2.md`).
- **Fichier JSON compagnon scellé (lu par `charger_table_bbis`)** : `correspondance-rejeu-croise-v1.json` (objet JSON identique à l'octet au bloc ci-dessous).
- **Attestation d'aveuglement** : *aucune colonne de score lue ; seules les colonnes de plan et leurs valeurs distinctes.* Aucune activation, aucun verdict, aucune table de l'ouvreur ni aucun tableau de scores (`*__sonde`, `*__plancher`, `*__nul`, `*__enc`, `*__sc_sonde`, `*__sonde_o2`) n'a été ouvert.

## 1. Constat structurel sur `SCORES-BBIS` (point décisif pour la contre-lecture)

La ligne `SCORES-BBIS (registres/t07-etape-b-bis-v1.md, ligne 8, 2026-11-18T19:43:48Z)` désigne l'index JSON `diag/20261118-154143-bbis-t07-v1/sondes-bbis.json` (empreinte vérifiée `645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62`, `sans_aucune_aire: true`), qui référence trois archives `.npz` scellées sur `origin/donnees/t07-etape-b-bis-v2` :

| Morceau `.npz` | SHA-256 vérifié | Sources portées |
|---|---|---|
| `donnees/20261118-154143-bbis-t07-v1/scores-bbis-000.npz` | `38e3f9b305945306688f101b37e30d84945aba39650102d8407c8e51be4a79cc` | `P-S100`, `P-S25`, `P-S50` |
| `donnees/20261118-154143-bbis-t07-v1/scores-bbis-001.npz` | `62628d376f07032ce870078fe7dffd98252be01bc5fcbcf724ed2b689ee22169` | `P-S50`, `P-S75`, `P-instruit` |
| `donnees/20261118-154143-bbis-t07-v1/scores-bbis-002.npz` | `129a690f8d679a4495fc936de5219cb32c22256da9262aebb4ad4c32916d2279` | `P-instruit` |

Chaque morceau `.npz` stocke des tableaux nommés `<source_bbis>__e<pli>__<groupe>__<champ>.npy` (où `<groupe>` vaut `<serie>-<condition>`, et `<champ>` vaut `cles`, `taches`, `sonde`, etc.).

- **Écart de format physique avec `charger_table_bbis` (commit `0ce9e3511`)** : `formats_v1.py` n'accepte aujourd'hui que `format_fichier` dans `{"jsonl", "csv"}`. La présente table de correspondance fige donc le schéma exact de la vue tabulaire JSONL déterministe extraite sans perte de `sondes-bbis.json` + `scores-bbis-000..002.npz` (une ligne par `(source_bbis, pli_lu, groupe, cle)` pour `champ_score == "sonde"`, avec les noms de champs et de valeurs brutes natifs de `t07bbis`), afin que le développeur puisse soit fournir un exportateur déterministe `sondes-bbis -> jsonl` (scellé, sans lecture ni résumé de score), soit étendre `charger_table_bbis` à ce format natif par un erratum contre-lu.
- **Point d'attention sur `poids` et `serie`** : dans le format `t07bbis`, le préfixe de série `O` désigne l'adaptateur dans `O-S<d>` mais le modèle nu dans `O-honnete`. Le recodage de `poids` porte donc sur la colonne `groupe` (`O-S<d>`, `A<d>-honnete` → `adaptateur` ; `J<d>-S<d>`, `O-honnete` → `nu`), qui est bijective sur les quatre cases de chaque dose.
- **Attestation sur `chemin` (`quatre_cases_du_texte_scelle`)** : après `selection`, chaque dose `0.25`, `0.5`, `0.75`, `1.0` ne porte que les quatre cases exactes du texte scellé (`O-S<d>` = `adaptateur|saboteur` en origine ; `J<d>-S<d>` = `nu|saboteur` en relu ; `A<d>-honnete` = `adaptateur|honnete` en relu ; `O-honnete` = `nu|honnete` en origine), chacune par un seul chemin (0 doublon, 0 action présente en origine et en relu pour un même `(poids, source)` ; contrôle du chemin = `absent`).
- **Attestation sur `tache_tenue` (`constante: true`)** : dans `validation_imbriquee_v1.py`, tous les groupes évalués hors `app` et `app_enc` ne contiennent que les 32 tâches de `taches_lues` du pli externe `e0` ou `e1`, disjointes des 32 tâches d'apprentissage (vérifié sur les tableaux `*__taches.npy` : 32 + 32 = 64 tâches disjointes par dose, 0 tâche hors `taches_lues`).
- **Variables de prédicteurs triviaux (`longueur`, `pas`, `valeur_declaree`)** : absentes des fichiers `SCORES-BBIS` (`sondes-bbis.json` et `scores-bbis-000..002.npz`), donc déclarées `{"absente": true}` (elles sortent proprement de `interaction_residuelle` dans `statistiques_v2.py`). Note pour la contre-lecture : le rang de pas `p0..p9` est encodé dans la chaîne `cle` (`S<d>__t<id>__p<pas>` / `honnete__t<id>__p<pas>`), tandis que `longueur` et `valeur_declaree` résident hors de `SCORES-BBIS` (dans `mesures-t06.npz` de T0.6).
- **Sondes gelées sélectionnées par pli dans `sondes-bbis.json` (sans score lu)** :

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

  Note : pour `P-S25` (`e0`, `e1`) et `P-S50` (`e0`), la sonde gelée retenue par la validation imbriquée de `t07bbis` emploie l'agrégation `attention` (et non `max`), alors que `spec-correspondance-rejeu-croise-v2.md` § 3 mentionne « maximum sur les jetons » entre parenthèses ; le tableau `*__sonde` porte bien dans tous les cas le score brut de la sonde gelée du pli.

## 2. Table de correspondance (`correspondance-rejeu-croise-v1.json`)

```json
{
 "format": "correspondance-rejeu-croise-v1",
 "redigee_par": "sous-agent-83ff952349ac7c27e7a058fe8138c9d8",
 "date_utc": "2026-11-24T03:58:37Z",
 "attestation": "aucune colonne de score lue ; seules les colonnes de plan et leurs valeurs distinctes",
 "table_source": {
  "chemin": "diag/20261118-154143-bbis-t07-v1/sondes-bbis.json",
  "sha256": "645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62",
  "ligne_registre": "SCORES-BBIS (registres/t07-etape-b-bis-v1.md, ligne 8, 2026-11-18T19:43:48Z)",
  "format_fichier": "jsonl"
 },
 "selection": {
  "champ_score": "sonde",
  "famille_bbis": "II",
  "cas_rejeu_croise": "oui"
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
