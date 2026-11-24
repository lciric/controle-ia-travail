# Vérification R2 finale — Candidats 1 au scellement de la table de correspondance et de la note de conception des sondes boîte blanche (v1)

- **Rôle** : contre-lecteur neuf indépendant (règle R2, sous `GO-2026-11-23-33` et `GO-2026-11-23-36`, conversation `1d691bacd476e88383a7f68e53c90b67`).
- **Date et heure (UTC)** : `2026-11-24T03:53:14Z` (`date -u`).
- **Branche et commit inspectés (sans checkout ni modification du dépôt)** : `origin/prep/conception-sondes-boite-blanche-fable-v2`, commit `26e604ee8bee2ba0c53d0c9a590bee78149ad043`.
- **État du dépôt principal** : inchangé (`git status --porcelain` vide) ; répertoire temporaire `/tmp/verif-candidat1` détruit après rejeu (`PYTHONDONTWRITEBYTECODE=1`).

---

## Verdicts

1. **Table de correspondance des issues du test « sabotage ou empreinte » sur les adaptateurs jumeaux — candidat 1** (`docs/notes/conception-sondes-boite-blanche-fable-v1/table-correspondance/table-correspondance-issues-adaptateurs-jumeaux-v1-candidat1.md`, SHA-256 `fb8f4c6475e738b7b3a489212c63877f56883da10b0022a8419a7d93d124e148`) :
   **`SCELLABLE EN L'ÉTAT`** (avant le scellement du verdict du test sur les adaptateurs jumeaux).
2. **Note de conception des sondes de la boîte blanche, version 2 — candidat 1** (`docs/notes/conception-sondes-boite-blanche-fable-v1/conception-sondes-v2-candidat1.md`, SHA-256 `9f99d86d5a2b00234ca0d10dbc561185f5c9b30d33e80b5ca99a4310ab4c8029`) :
   **`SCELLABLE EN L'ÉTAT`** (avec la seule inscription mécanique prévue à la **ligne 153**, section 7 : report par la session mère de l'empreinte SHA-256 de la table scellée — `fb8f4c6475e738b7b3a489212c63877f56883da10b0022a8419a7d93d124e148` si la table est scellée telle quelle — avant le scellement de la note de conception).

---

## 1. Empreintes SHA-256 recalculées et vérification des compagnons

Les **16 fichiers compagnons `.sha256`** du commit `26e604ee8bee2ba0c53d0c9a590bee78149ad043` sont **16/16 conformes**.

| pièce (dans `26e604ee8`) | SHA-256 recalculé | taille / lignes | compagnon `.sha256` |
|---|---|---|---|
| `table-correspondance-issues-adaptateurs-jumeaux-v1-candidat1.md` | `fb8f4c6475e738b7b3a489212c63877f56883da10b0022a8419a7d93d124e148` | 52 856 o / 189 l. | conforme |
| `table-correspondance-issues-adaptateurs-jumeaux-v1-brouillon3.md` | `9b0e2c1304ab914ef943c4e99693d1fd9b60e6d4e4b4bee6f392e02264d6bf42` | 46 073 o / 177 l. | conforme |
| `montage-candidat1-v1/monter_table_candidat1.py` | `5f18e60e26bab3ae9a44630a58a32e5e76c091fdad214f2e2185729dedbc2ef8` | 15 783 o / 89 l. | conforme |
| `conception-sondes-v2-candidat1.md` | `9f99d86d5a2b00234ca0d10dbc561185f5c9b30d33e80b5ca99a4310ab4c8029` | 58 583 o / 218 l. | conforme |
| `conception-sondes-v2-brouillon5.md` | `e9ad9d8af24e43724c5b99bda74981c8f896b248f46a833dc1c96613cdba0b8d` | 54 740 o / 212 l. | conforme |
| `montage-candidat1-v1/monter_note_candidat1.py` | `69f008567546fd3ebc53ff83a034c294e93cbf6fac8bdc7dae4167c93405106c` | 8 909 o / 51 l. | conforme |
| `relecture-concepteur-avant-scellement-v1.md` | `b5ac58f6005077464b16b58960333eaefc14fe3018ae16ea8de93bf4fced4dc4` | 5 268 o / 25 l. | conforme |
| `verification-formelle-table-correspondance-brouillon3-v1.py` | `092b9651cba86b6c87f494f0347e22a6bb8e4fcda6c071c0747fc922a1112571` | 22 241 o / 385 l. | conforme |
| `verification-finale-table-brouillon3-et-conception-brouillon5-v1.md` | `7488baf06bca644ca82a6c723adb7825125a6c0d73c298dd6cd6fedb2cb36390` | 8 467 o / 50 l. | conforme |
| `montage-candidat1-v1/LISEZ-MOI.md` | `e44a2e88e0e90d2dde9841be152591c58ba4291dd53256d6ff25031c2b44f4a6` | 706 o / 8 l. | conforme |

---

## 2. Rejeu par programme et identité à l'octet

Exécutés dans `/tmp/verif-candidat1` (puis nettoyés) avec `PYTHONDONTWRITEBYTECODE=1` :

1. **Rejeu de `monter_table_candidat1.py`** sur `table-...-brouillon3.md` (`9b0e2c13…`) avec l'heure `23:32` :
   - Sortie rejouée **identique à l'octet** au candidat 1 (`fb8f4c6475e738b7b3a489212c63877f56883da10b0022a8419a7d93d124e148`).
2. **Contrôle indépendant des sections 1 à 8** (de `## 1. Définitions et vocabulaire` à la ligne précédant `## 9.`) :
   - Brouillon 3 : lignes 17 à 142 (35 118 octets), SHA-256 `24b93ce708de69476512dd83794c44514023c4bd6e2c83bdc321efd80b06e10e`.
   - Candidat 1 : lignes 21 à 146 (35 118 octets), SHA-256 `24b93ce708de69476512dd83794c44514023c4bd6e2c83bdc321efd80b06e10e`.
   - **Identité stricte à l'octet confirmée.** La preuve formelle déjà vérifiée sur les `18 432` combinaisons `S/D/E/N/C/X` + `1 280` combinaisons `NI` (`7488baf0…`) reste intégralement valide.
3. **Rejeu de `verification-formelle-table-correspondance-brouillon3-v1.py`** (`092b9651…`) :
   - Code retour `0` : **38/38 cas limites** et **172/172 combinaisons**, **0 trou**, **0 recouvrement**, **0 écart à l'attendu**.
4. **Rejeu de `monter_note_candidat1.py`** sur `conception-sondes-v2-brouillon5.md` (`e9ad9d8a…`) avec l'heure `23:32` :
   - Sortie rejouée **identique à l'octet** au candidat 1 (`9f99d86d5a2b00234ca0d10dbc561185f5c9b30d33e80b5ca99a4310ab4c8029`).
   - Le différentiel `brouillon5 -> candidat1` ne touche **strictement** que les passages listés à l'en-tête : titre/en-tête, section 7 (condition 5, alinéa « Table de correspondance » et alinéa « Écart de calendrier, déclaré »), section 8 point 0, et deux puces de la section « Contre-lecture ». Sections 1 à 6, tables et autres alinéas de la section 7, points 1 à 7 de la section 8, section 9 et annexe A sont inchangés à l'octet.

---

## 3. Fidélité à `GO-2026-11-23-36`, à `R-5208` et à la provenance

- **Quatre points de jugement (§ 9 de la table)** : tous quatre fidèlement tranchés selon les recommandations du brouillon 3 conformément à `GO-2026-11-23-36` (« go a tout go recos de carbon high ») :
  1. `S` et `C` au niveau de 95 % → `Non établi` (lignes 2 et 8) ;
  2. `E` sous huit familles → `Non établi` (ligne 5, borne uniforme de 8 familles en ligne 4) ;
  3. `D` pour tous ses motifs → `Non établi` (ligne 3) ;
  4. Préclassement des 15 gardes (§ 2) approuvé et attente bornée maintenue (lignes 9 à 11, règle 8).
- **Écart de calendrier déclaré (§ 10 point 5 de la table ; § 7 de la note)** : conforme à `R-5193` (marche `20261123-044043-b5f-lecture` achevée le `2026-11-23T10:12:09Z` code 0 ; rapatriement sans lecture de score attesté à `21:08:47Z`), `R-5194` (`21:13:38Z`, commit `9163ba4d8aed5fbf45fb193455d97e32fa8b23aa` daté `2026-11-23T21:13:56Z`), `R-5205` et `R-5208` point (4) (aucun verdict scellé, aucune ouverture de score ; explicitement limité à l'absence d'ouverture antérieure de score).
- **Empreintes de provenance vérifiées contre le dépôt Git** (toutes exactes sur 64 caractères hexadécimaux) :
  - `c228c773e0ea94982d73a4a9c97e48305a3b77333874532655fb59a1818773cb` (`extrait-issues-et-phrases-gelees-b5f-v1.md`, sur `origin/conducteur-b5f/lecture-v2`) ;
  - `24122337d7baa2a7b8516f3b4a882316832e4ba0ba7335a87c3eda190b21af27` (`attestation-extrait-issues-b5f-v1.md`, idem) ;
  - `b14e35acec7882571f3759c004b82900beed2e62df1d9eea97128cf5055b4f1a` (`extrait-liste-d-arret-et-niveaux-b5f-v1.md`, idem) ;
  - `2fe4c33b3d30ddb237d8094a8728950a6b6f07725cdf23fbdd1f52a29f8f4e83` (`contre-lecture-table-v1-opus-v1.md`, sur `origin/prep/contre-lecture-table-correspondance-jumeaux-v1`, commit `c78d95bd31d0b90de543d12355dc54c36f247bdf`) ;
  - `5956ea6086b366c69be26845548149cf14d39c1221dec0f2d7ff666acde7de4b` (`contre-lecture-table-brouillon2-et-conception-brouillon4-v1.md`) ;
  - `66ed4874ec2b6968bbd3ac0059cbcbdb971dad7c02213e077559daa9a16d92c6` (`table-...-brouillon1.md`) ;
  - `e8dca00b65289f6de954c85b1720bdae30bd5362db80d371ed8c1a571b05e8e1` (`prereg/diagnostics-prealables-sondes-v1.md`).
- **Absence de résultat** : aucun chiffre de résultat, aucun extrait de sortie, aucune fuite dans aucune des pièces inspectées.

---

## 4. Remarques mineures non bloquantes (à connaître sans retarder le scellement)

1. **Coquille héritée sur l'identifiant du commit en ligne 10 de `table-...-candidat1.md`** (reprise verbatim du brouillon 3) : il est écrit `389326b2d24509ca192ade6d36f6ca91976b50b` (39 caractères) au lieu du commit réel à 40 caractères `389326b2d24509ca192ade6d360f6ca91976b50b` sur `origin/conducteur-b5f/lecture-v2` (un `0` omis dans `360f6ca`). Les trois empreintes SHA-256 des fichiers servis par ce commit sont toutes exactes à l'octet.
2. **Deux formulations mineures héritées dans l'en-tête de `table-...-candidat1.md`** : ligne 3 (`conception-sondes-v2-candidat1.md, dans le même dossier` alors que la table réside dans le sous-dossier `table-correspondance/`) et ligne 14 (`tous portés dans ce brouillon 3` au lieu de `le brouillon 3`). Aucune incidence sur les sections 1 à 10 ni sur la correspondance.
3. **Point d'action mécanique de la mère avant scellement de `conception-sondes-v2-candidat1.md`** : à la **ligne 153** (section 7), remplacer `à inscrire ici par la session mère avant le scellement de cette note` par l'empreinte SHA-256 de la table scellée (`fb8f4c6475e738b7b3a489212c63877f56883da10b0022a8419a7d93d124e148` si scellée en l'état).
4. **Réserves de `relecture-concepteur-avant-scellement-v1.md` (`b5ac58f6…`)** : les 5 réserves du concepteur titulaire sont toutes non bloquantes pour ce scellement ; les réserves 4 et 5 (second jeu de témoins à variance projetée égale et test apparié ou ≥ 39 témoins) seront à porter dans le futur texte court de la marche causale (§ 2 bis), après une marche 1 réussie.

---

## Ligne « qui a lu quoi »

- **Agent** : sous-agent contre-lecteur neuf indépendant `1d691bacd476e88383a7f68e53c90b67` (`2026-11-24T03:53:14Z`, sous `GO-2026-11-23-33` et `GO-2026-11-23-36`).
- **Lu pour cette vérification** : par `git show` sur `origin/prep/conception-sondes-boite-blanche-fable-v2` (`26e604ee8`) : `table-correspondance-issues-adaptateurs-jumeaux-v1-candidat1.md`, `table-correspondance-issues-adaptateurs-jumeaux-v1-brouillon3.md`, `monter_table_candidat1.py`, `conception-sondes-v2-candidat1.md`, `conception-sondes-v2-brouillon5.md`, `monter_note_candidat1.py`, `relecture-concepteur-avant-scellement-v1.md`, `verification-formelle-table-correspondance-brouillon3-v1.py`, `verification-finale-table-brouillon3-et-conception-brouillon5-v1.md`, `montage-candidat1-v1/LISEZ-MOI.md`, et leurs compagnons `.sha256` ; lignes `GO-2026-11-23-33` à `-40` de `registres/go.md` ; lignes `R-5193`, `R-5194`, `R-5205`, `R-5207` à `R-5215` de `registres/decisions.md` ; calcul d'empreinte seul (sans lecture de contenu) sur les 3 pièces servies d'`origin/conducteur-b5f/lecture-v2`, sur `contre-lecture-table-v1-opus-v1.md` et sur `prereg/diagnostics-prealables-sondes-v1.md`.
- **Non ouvert** : aucun fichier sous `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/`, `essai/`, `brouillons/ii-b*`, ni `prereg/barreau5-*`, ni `registres/etat.md`. Aucun résultat lu.
