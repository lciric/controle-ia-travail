# Rapport de lecture et de vérification — épreuve à vérité plantée des sondes boîte blanche version 2 (mode étalon, exécution partielle)

> **Portée stricte.** Le présent rapport porte exclusivement sur l'**épreuve synthétique à vérité plantée** des sondes de la boîte blanche version 2 (mode `etalon`, serveur Hetzner `177425658`, autorisation budgétaire `GO-2026-11-24-02`). **Il ne contient aucun score de course réelle, aucune activation réelle et aucun verdict sur des données réelles.**

---

## 1. Verdict synthétique

- **Statut d'exécution** : **`partiel-plafond-r10`** (incomplet au regard du préenregistrement scellé).
- **Intégrité cryptographique et technique** : **13 empreintes vérifiées à l'octet sur 13** (100 %) ; **0 erreur**, **0 exception**, **0 valeur manquante ou non finie** sur l'ensemble des 118 300 essais-familles simulés ; tous les invariants de cohérence de la fonction officielle d'agrégation (`programme_monde_plante_v4.fusionner`) sont vérifiés entre les 13 tranches (à l'unique exception de la garde de complétude `[0, 500)`).
- **Couverture réelle par rapport au plan engagé** :
  - **Mode étalon (option A, grille de 52 cases × 7 mondes)** : **130 répliques contiguës achevées sur 500 prévues (`[0, 130)`, soit 26,0 %)**, exécutées en un seul processus travailleur (`nproc = 1`) après bascule automatique sur le mode de repli `etalon_seul`, jusqu'à l'arrêt propre déclenché par la minuterie interne de la règle numéro 10 à 31 heures 30 minutes (`113 400` secondes).
  - **Mode complet (option C, 39 rejeux nuls, case unique `8` paires × `64` tâches × `10` actions × `4` doses)** : **0 réplique sur 500 (0,0 %)** — non exécuté. La troisième question de diagnostic (rejeu croisé du texte et des poids) et les contrôles d'instrument hors lignes du texte scellé (`contraste`, `nul_principal`, `texte`, `fuite_de_pli`) ne sont donc pas encore couverts.
- **Enseignement scientifique provisoire (sur les 130 premières répliques du mode étalon)** :
  1. **Calibration et contrôle des fausses alertes excellents** : **52 cases sur 52** passent les critères bornés de fausse alerte dans le monde d'identité seule (`0,87 %` sur les 36 cases testables, borne haute maximale de `8,75 % <= 10 %`) et dans le monde de trace faible (`0,13 %` de faux « fort », borne haute maximale de `5,45 % <= 10 %`). Dans le monde d'étiquettes permutées, **50 cases sur 52** passent ; les **2 échecs apparents** (`8,1,40,2` et `11,1,40,2`, chacun à `7 / 130 = 5,38 %`, intervalle exact à 95 % de `[2,19 % ; 10,78 %]`) proviennent exclusivement de la largeur statistique de l'intervalle exact de Clopper-Pearson à `n = 130` (le taux agrégé sur les 10 cases testables à une famille est de `51 / 1 300 = 3,92 %`, sous le niveau nominal bilatéral de `5,0 %`).
  2. **Puissance maximale dès les seuils de testabilité prévus** : dans le monde de trace forte, les 16 cases sous la frontière théorique sont systématiquement classées « non testable à cet effectif » (100 %), et les **36 cases testables** atteignent **`100,0 %` de détection « fort » (`11 310 / 11 310`)**, aussi bien avant qu'après contrôle d'intensité.
  3. **Sonde d'identité des poids : comportement conforme au seuil structurel** : **44 cases sur 52** passent avec **`100,0 %` de libellés « identité forte » (`14 300 / 14 300`)** pour tout effectif d'au moins 6 paires (`P >= 6`). Les **8 cases en échec** (`P = 4` et `P = 5`, quel que soit le nombre de familles) rendent `0 %` par règle structurelle du texte scellé : `G = floor(P / 2) = 2` couples disjoints est strictement inférieur au minimum de 3 couples exigé pour émettre un libellé (`sans libellé` à 100 %). Ce point est indépendant du nombre de répliques et restera identique à 500 répliques.
  4. **Confirmation quantitative de la réserve d'intensité** : sans retrait de la direction moyenne des adaptateurs, un écart multiplicatif d'intensité de `1,2` produit `0,93 %` de faux « fort » à norme `1` (`intensite_1`), mais **`100,0 %` de faux « fort »** à normes `4` et `16` (`intensite_4` et `intensite_16`). Le contrôle d'intensité (`transport_controle`) ramène ces faux « fort » à **`0,00 %`–`0,01 %`** (`1` seul essai sur `33 930` essais-familles testables cumulés sur les trois mondes d'intensité) tout en laissant intacte la puissance `100,0 %` sous véritable trace forte, avec un résidu de `21 %` à `32 %` de libellés « faible ».
- **Conséquence procédurale** : l'étape 2 du préenregistrement n'est **pas close** (la fusion officielle exige `[0, 500)` en mode étalon et `[0, 500)` en mode complet avant toute ouverture des activations ou des scores réels). En revanche, les 13 tranches produites (`[0, 130)`) sont **intégralement valides et réutilisables sans recalcul** grâce au schéma déterministe des graines indépendant du découpage en plages : seules les 37 tranches restantes (`[130, 500)`, environ `84,7` heures de processeur estimées) restent à exécuter pour achever le mode étalon, en sus du mode complet.

---

## 2. Identification, sources scellées et vérification d'intégrité

### 2.1. Pièces et engagements vérifiés

| Pièce | Emplacement ou référence | Empreinte sécurisée sur 256 bits (`sha256`) | État |
|---|---|---|---|
| Branche des résultats | `origin/calcul/sondes-v2-epreuve-plantee-v4` | Commit `38c6f4a7054b14b56be7b357c08db8bf11931ca2` | Extraite en lecture seule (27 fichiers) |
| Branche du code figé | `origin/sondes-v2/code-v2` | Commit `0ce9e35110d93dd916e85b1191a2613b101e772d` | Vérifié identique à l'additif scellé |
| Préenregistrement initial | `prereg/diagnostics-prealables-sondes-v1.md` | `e8dca00b65289f6de954c85b1720bdae30bd5362db80d371ed8c1a571b05e8e1` | Lu et appliqué sans modification |
| Additif de commit scellé | `prereg/diagnostics-prealables-sondes-v1-additif-commit-v1.md` | Scellé le `2026-11-24T05:36:04Z` | Lu et vérifié |
| Note des effectifs scellée | `docs/notes/sondes-v2-effectifs-et-correspondance-v1/note-des-effectifs-sondes-v2-v1.md` | `7338a3dcafb18bfd6fdd43e377bfa0b67f3f6812596749646d6fb0e9c3444db5` | Identique au champ `note_effectifs` des 13 tranches |
| Vérités engagées version 4 | `src/controle_ia/sondes_v2/verites_mondes_plantes_v4.json` | `b310e1af50459b78833fcc509298bbc1807f1905631e1152b3e28f538f233533` | Identique à l'octet |
| Programme d'épreuve version 4 | `src/controle_ia/sondes_v2/programme_monde_plante_v4.py` | `0559e8c3ed6e0e6f1428a4fe334bd30dd1343f731162050f0a3a85e7dd9e9326` | Identique à l'octet |
| Générateur et lecture version 4 | `src/controle_ia/sondes_v2/monde_plante_v4.py` | `044978d9013a6d4653e294893f7632128424f5e76b7c425a8b4614393f451908` | Identique à l'octet |
| Entropie racine (règle numéro 9) | `305159624078239919914131004197200342142` | — | Identique sur les 13 tranches |

### 2.2. Contrôle bit-à-bit des 13 tranches et durées d'exécution

Les 27 fichiers de la branche `origin/calcul/sondes-v2-epreuve-plantee-v4` ont été extraits en mode binaire dans le dossier `brut/` sans altération des fins de ligne. Chacun des 13 compagnons `.sha256` a été vérifié à l'octet :

| Tranche | Plage de répliques | Taille (octets) | Durée mesurée | Empreinte sécurisée sur 256 bits (`sha256`) | Contrôle |
|---|---|---:|---:|---|---|
| 1 | `[0, 10)` | 2 404 364 | 8 794,9 s (2,44 h) | `7323b4d0f7129c4d688981cb3c8e5e84bf61c181ea96ca034234fa53244ba208` | Conforme |
| 2 | `[10, 20)` | 2 408 894 | 8 401,3 s (2,33 h) | `1049129ff78c61e069f6bf8e1d6beb4a6e13c9789b044a7673299e8f0a78bcac` | Conforme |
| 3 | `[20, 30)` | 2 408 936 | 8 033,2 s (2,23 h) | `6161b67e06c97dfa9f035388688e1412fd132928ec551bff4b20783fb63f7119` | Conforme |
| 4 | `[30, 40)` | 2 409 332 | 8 513,1 s (2,36 h) | `3ed7d0aa57297f13701aca01921b6a2b4345aaf0d6b0476f1cac96a095bbe76b` | Conforme |
| 5 | `[40, 50)` | 2 408 013 | 8 351,8 s (2,32 h) | `fbe6241205bc08f72a6648a03e3a3c1a673f4542a090f89094a707b08fb366ac` | Conforme |
| 6 | `[50, 60)` | 2 408 695 | 8 427,8 s (2,34 h) | `c18374f3ce1d6a8a10f19cea1a61523abaab705d53f3b5ee5e00ae2eaceec84e` | Conforme |
| 7 | `[60, 70)` | 2 408 927 | 8 157,9 s (2,27 h) | `0d3ab636d2aad2090e3f40d7ba883e7be4923108348938b92ff5622b5c5e2ed0` | Conforme |
| 8 | `[70, 80)` | 2 406 782 | 8 117,6 s (2,25 h) | `3b5aaf2a3c38e37fa94b16d66e28a955c60341aa3875d6c50793293a19e5f512` | Conforme |
| 9 | `[80, 90)` | 2 408 008 | 8 085,0 s (2,25 h) | `3820bc5c143c282f4e0e224f2d8dcd440ac672c922b513986cefab0eb3e7a3ad` | Conforme |
| 10 | `[90, 100)` | 2 404 994 | 7 943,3 s (2,21 h) | `6bbb174ab406f7f4c35c5fccef19ab61ef24322ad569cc8c0c264742c1b2c6ef` | Conforme |
| 11 | `[100, 110)` | 2 412 385 | 7 922,1 s (2,20 h) | `39b5c94c545b8ee1350e5174f1437704c15d426ccd1f9b5f58665f4882766a55` | Conforme |
| 12 | `[110, 120)` | 2 410 435 | 8 303,0 s (2,31 h) | `de42bc2b558c3838eaeefc2dd533a6d670e8eb8a44d3e1f70b1e98aa3593d5fd` | Conforme |
| 13 | `[120, 130)` | 2 411 529 | 8 104,6 s (2,25 h) | `5686277e016aa18055e6ed74f100d184bf13dabf11e93eccf6fbc69efbff3374` | Conforme |
| **Total** | **`[0, 130)`** | **31 301 294** | **107 155,5 s (29,77 h)** | **13 / 13 empreintes exactes** | **Conforme** |

### 2.3. Audit du journal d'exécution (`journal-execution.log`) et des valeurs numériques

- **Chronologie exacte** :
  - Démarrage le `2026-11-24T05:37:58Z` en temps universel coordonné sur le serveur Hetzner `177425658`, en mode `etalon_seul`, avec `nproc = 1` (un seul processus travailleur séquentiel) et une minuterie interne de règle numéro 10 armée à `113 400` secondes (`31 h 30 min`).
  - Vérifications initiales réussies : dépôt cloné exactement au commit `0ce9e3511` (`depot_propre = true`, `reserves = []`), `verites_mondes_plantes_v4.json: OK`, `note-des-effectifs-sondes-v2-v1.md: OK`, installation exacte des bibliothèques scientifiques (`numpy 2.4.6`, `scipy 1.17.1`, `scikit-learn 1.9.1`, sous Python `3.12.3`).
  - Lancement des 50 plages de 10 répliques (`r0-10` à `r490-500`) en mode `etalon`.
  - Achèvement propre et scellement des 13 tranches `r0-10` à `r120-130` (cadence très régulière : `8 242,7` secondes par tranche en moyenne, soit `2,29` heures par tranche sur un cœur).
  - Déclenchement propre de la minuterie interne le `2026-11-25T13:15:28Z` (`=== PLAFOND INTERNE R10 (113400s) ATTEINT ===`), alors que la 14e tranche (`r130-140`) en était à la case `15,4,40,2`, monde `intensite_4`, réplique `135 / 500` (tranche inachevée non écrite, conformément à la règle de scellement atomique en fin de plage). Publication propre sur la branche `calcul/sondes-v2-epreuve-plantee-v4`.
- **Erreurs, avertissements et valeurs anormales** :
  - **0 erreur Python**, **0 trace d'exception**, **0 arrêt de garde**, **0 défaillance de mémoire**.
  - Deux seuls messages d'avertissement bénins dans tout le journal (50 845 lignes) : un avertissement de l'utilitaire système `xargs` sur la combinaison des options `--max-args` et `--replace` au lancement (sans aucun impact sur la séquence des plages) et le message standard de `git init` sur le nom de la branche initiale lors de la publication.
  - **Audit numérique exhaustif des 13 fichiers structurés** : **0 valeur nulle**, **0 valeur non numérique ou non finie** sur l'ensemble des 4 grandeurs (`U`, `rho`, `U_controle`, `rho_controle`) et sur l'ensemble des `52 cases × 7 mondes × 130 répliques` (`16 900` essais-familles par monde, `118 300` essais-familles cumulés).
- **Invariants de fusion vérifiés** : tous les contrôles de `programme_monde_plante_v4.fusionner()` passent à l'identique sur les 13 tranches (format, mode, empreinte des vérités, arguments complets, entropie racine, commit, propreté du dépôt, réserves vides, empreinte canonique de configuration `config_sha256` hors plage, contiguïté stricte `[0, 130)` sans trou ni chevauchement). Seule la garde finale de complétude (`bout == 500`) s'oppose légitimement à l'émission d'une synthèse fusionnée officielle tant que `[130, 500)` n'est pas exécuté.

---

## 3. Méthode officielle d'agrégation appliquée aux 13 tranches

Aucune formule n'a été inventée : les calculs reproduisent exactement la logique de `programme_monde_plante_v4.synthese()`, `monde_plante_v4.compter()`, `monde_plante_v3.passage()`, `monde_plante_v3.clopper_pearson()` et `monde_plante_v4.resume_grandeurs()` au commit figé `0ce9e3511`, appliquée ici sur les `130` répliques contiguës `[0, 130)` au lieu de `500` :

1. **Unité d'essai** : pour une case `(P, F, 40, 2)` (soit `P` paires par famille, `F` familles, `40` tâches, `2` actions par tâche) et un monde donné, chaque réplique produit un libellé par famille. Chaque entrée de liste constitue un essai ; sur `130` répliques, une case comporte donc `n = 130 × F` essais-familles (`130` pour `F = 1`, `260` pour `F = 2`, `390` pour `F = 3`, `520` pour `F = 4`). Sur l'ensemble des `52` cases (`P ∈ {4, …, 16}` × `F ∈ {1, 2, 3, 4}`), cela représente `16 900` essais-familles par monde (`5 590` sur les `16` cases non testables et `11 310` sur les `36` cases testables).
2. **Libellé de base** : conformément à `verites_mondes_plantes_v4.json`, la comparaison aux libellés admis porte sur le libellé de base obtenu avant un éventuel séparateur `" — "` portant la mention du plancher apparié aléatoire (`non distinct d'une direction au hasard : écart diffus possible, non la direction apprise`). La fréquence de cette mention du plancher est rapportée séparément ci-dessous.
3. **Critères de passage** : chaque proportion admise `x / n` reçoit son intervalle de confiance bilatéral exact de Clopper-Pearson à `95 %`.
   - Critère à borne haute (`<= 0,10`, fausses alertes) : passe si et seulement si la **borne haute** de l'intervalle exact à `95 %` est au plus égale à `0,10`.
   - Critère à borne basse (`>= 0,80`, puissance d'identité) : passe si et seulement si la **borne basse** de l'intervalle exact à `95 %` est au moins égale à `0,80`.
   - Critère sans borne (puissance sous trace forte, descriptions des mondes d'intensité) : rapporté sans décision de passage.
4. **Effet mécanique de la coupure à 130 répliques sur les bornes exactes** : pour `F = 1` (`n = 130` essais au lieu de `500`), l'intervalle exact de Clopper-Pearson est sensiblement plus large. En particulier, pour une borne haute exigée à `<= 10,0 %`, `6 / 130 = 4,62 %` donne une borne haute de `9,78 %` (passe), tandis que `7 / 130 = 5,38 %` donne déjà `10,78 %` (échoue), alors qu'à `n = 500`, le même taux de `5,38 %` (`27 / 500`) aurait une borne haute de `7,76 %` (passe largement).

---

## 4. Synthèse globale par monde et par diagnostic (130 répliques, 52 cases)

| Monde planté | Diagnostic et libellés admis | Nature et règle de passage | Cases qui passent (sur 52) | Taux agrégé sur cases testables (`36` cases, `11 310` essais-familles) | Plage par case des taux et bornes critiques (sur les `52` cases) | Grandeurs réalisées médianes (`U`, `ρ`) |
|---|---|---|---|---|---|---|
| **`identite_seule`** | Étalon de transport : `fort` ou `faible` | Fausse alerte (borne haute `<= 10 %`) | **52 / 52** (`0` échec) | `98 / 11 310 = 0,87 %` (`0` fort, `98` faible) | Taux `0,0 %` à `3,85 %` ; borne haute max `8,75 %` | `U = 0,500`, `ρ = 0,001` |
| **`identite_seule`** | Sonde d'identité : `identité forte` | Puissance (borne basse `>= 80 %`) | **44 / 52** (`8` échecs structurels à `P = 4, 5`) | `14 300 / 14 300 = 100,0 %` pour `P >= 6` ; `0 / 2 600 = 0,0 %` pour `P = 4, 5` | Pour `P >= 6` : taux `100,0 %`, borne basse min `97,2 %` | — |
| **`trace_faible`** (`τ ≈ 0,707`) | Étalon de transport : `fort` | Fausse alerte (borne haute `<= 10 %`) | **52 / 52** (`0` échec) | `15 / 11 310 = 0,13 %` (`91,0 %` classés `faible`) | Taux `0,0 %` à `1,54 %` ; borne haute max `5,45 %` | `U = 0,681`, `ρ = 0,704` |
| **`etiquettes_permutees`** | Étalon de transport : `fort`, `faible` ou `contraire` | Calibration nulle (borne haute `<= 10 %`) | **50 / 52** (`2` échecs à `F = 1` par largeur à `n = 130`) | `188 / 11 310 = 1,66 %` (`3,92 %` pour `F = 1`) | Taux `0,0 %` à `5,38 %` ; borne haute max `10,78 %` (`8,1` et `11,1`) | `U = 0,500`, `ρ = -0,001` |
| **`trace_forte`** (`τ ≈ 5,657`) | Étalon de transport : `fort` | Puissance (rapportée sans borne) | Sans borne (`36` testables, `16` non testables) | **`11 310 / 11 310 = 100,0 %`** (brut et après contrôle d'intensité) | `100,0 %` sur les `36` cases testables (`0,0 %` sur les `16` non testables) | `U = 1,000`, `ρ = 5,618` (`ρ` contrôlé `4,884`) |
| **`intensite_1`** | Transport brut / contrôlé : `fort` | Descriptif (réserve d'intensité) | Sans borne | Brut : **`0,93 %`** (`105 / 11 310`) ; Contrôlé : **`0,00 %`** (`0 / 11 310`) | Brut `92,9 %` « faible » ; Contrôlé `21,2 %` « faible » | Brut `U = 0,725` (`ρ = 0,891`) → Contrôlé `U = 0,571` (`ρ = 0,269`) |
| **`intensite_4`** | Transport brut / contrôlé : `fort` | Descriptif (réserve d'intensité) | Sans borne | Brut : **`100,0 %`** (`11 310 / 11 310`) ; Contrôlé : **`0,009 %`** (`1 / 11 310`) | Brut `100 %` « fort » ; Contrôlé `31,7 %` « faible » | Brut `U = 1,000` (`ρ = 5,466`) → Contrôlé `U = 0,589` (`ρ = 0,344`) |
| **`intensite_16`** | Transport brut / contrôlé : `fort` | Descriptif (réserve d'intensité) | Sans borne | Brut : **`100,0 %`** (`11 310 / 11 310`) ; Contrôlé : **`0,00 %`** (`0 / 11 310`) | Brut `100 %` « fort » ; Contrôlé `32,3 %` « faible » | Brut `U = 1,000` (`ρ = 22,928`) → Contrôlé `U = 0,591` (`ρ = 0,350`) |

---

## 5. Analyse détaillée par diagnostic et par famille de vérité plantée

### 5.1. Frontière de testabilité de l'étalon de transport (deuxième question de diagnostic)

La règle du préenregistrement scellé classe une famille comme « testable » si la valeur `p` bilatérale minimale atteignable par échange des étiquettes intra-paire (`2^{2 - P}`) ne dépasse pas le premier pas de la correction de Holm (`0,05 / F`). Les résultats observés vérifient **exactement et sans exception** cette frontière théorique sur les `52` cases :

- **16 cases systématiquement « non testable à cet effectif »** (`5 590` essais-familles par monde, `100,0 %`) : `P ∈ {4, 5, 6}` pour `F ∈ {1, 2, 3, 4}` (12 cases), `P = 7` pour `F ∈ {2, 3, 4}` (3 cases) et `P = 8` pour `F = 4` (1 case).
- **36 cases systématiquement testables** (`11 310` essais-familles par monde) : `P = 7` pour `F = 1`, `P = 8` pour `F ∈ {1, 2, 3}` et `P ∈ {9, …, 16}` pour `F ∈ {1, 2, 3, 4}`.

### 5.2. Sonde d'identité des poids (première question de diagnostic, monde `identite_seule`)

- **Comportement observé** :
  - Pour `P = 4` et `P = 5` (toutes valeurs de `F ∈ {1, 2, 3, 4}`, soit **8 cases** et `2 600` essais-familles) : **`0 / 2 600` (`0,0 %`)** de libellés « identité forte » ; `100,0 %` des lectures valent `sans libellé`.
  - Pour **`P = 6` à `P = 16`** (toutes valeurs de `F ∈ {1, 2, 3, 4}`, soit **44 cases** et `14 300` essais-familles) : **`14 300 / 14 300` (`100,0 %`)** de libellés « identité forte » ; la borne basse exacte à `95 %` est de `97,20 %` pour `F = 1` (`130 / 130`), `98,59 %` pour `F = 2` (`260 / 260`), `99,06 %` pour `F = 3` (`390 / 390`) et `99,29 %` pour `F = 4` (`520 / 520`), très au-dessus du seuil exigé de `80 %`.
- **Interprétation de l'échec sur `P = 4` et `P = 5`** : il ne s'agit ni d'un défaut de puissance, ni d'un aléa lié à l'arrêt à 130 répliques. Le préenregistrement scellé stipule expressément que les jumeaux d'une famille sont appariés en `G = floor(P / 2)` couples disjoints et qu'avec **moins de trois couples (`G < 3`), la sonde rapporte les aires sans attribuer de libellé**. À `P = 4` ou `P = 5`, `G = 2` ; le critère borné « identité forte dans au moins 80 % des répliques » ne peut donc jamais passer pour `P ∈ {4, 5}`, même à 500 répliques. Pour toute famille réelle comportant au moins 6 paires (`P >= 6`), la puissance mesurée est de `100,0 %`.

### 5.3. Fausses alertes et calibration nulle de l'étalon de transport (`identite_seule`, `etiquettes_permutees`, `trace_faible`)

#### Calibration par nombre de familles sur les 36 cases testables

| Nombre de familles `F` | Cases testables (`n` essais-familles) | `identite_seule` (`fort` + `faible`, critère `<= 10 %`) | `etiquettes_permutees` (`fort` + `faible` + `contraire`, critère `<= 10 %`) | `trace_faible` (`fort` seul, critère `<= 10 %`) | `trace_faible` (`faible`, détection attendue) |
|---|---:|---:|---:|---:|---:|
| `F = 1` (`P = 7..16`) | 10 (`1 300`) | `28 / 1 300` (`2,15 %`) | `51 / 1 300` (`3,92 %`) | `4 / 1 300` (`0,31 %`) | `1 149 / 1 300` (`88,38 %`) |
| `F = 2` (`P = 8..16`) | 9 (`2 340`) | `22 / 2 340` (`0,94 %`) | `50 / 2 340` (`2,14 %`) | `1 / 2 340` (`0,04 %`) | `2 101 / 2 340` (`89,79 %`) |
| `F = 3` (`P = 8..16`) | 9 (`3 510`) | `25 / 3 510` (`0,71 %`) | `43 / 3 510` (`1,23 %`) | `6 / 3 510` (`0,17 %`) | `3 124 / 3 510` (`89,00 %`) |
| `F = 4` (`P = 9..16`) | 8 (`4 160`) | `23 / 4 160` (`0,55 %`) | `44 / 4 160` (`1,06 %`) | `4 / 4 160` (`0,10 %`) | `3 914 / 4 160` (`94,09 %`) |
| **Total testable** | **36 (`11 310`)** | **`98 / 11 310` (`0,87 %`)** | **`188 / 11 310` (`1,66 %`)** | **`15 / 11 310` (`0,13 %`)** | **`10 288 / 11 310` (`90,96 %`)** |

#### Examen des deux cases en échec dans le monde `etiquettes_permutees`

| Case (`P, F, T, A`) | Lectures admises (fausses alertes bilatérales) | Détail des libellés (`faible` / `contraire` / `fort`) | Taux observé | Intervalle exact à 95 % | Statut à `n = 130` |
|---|---|---|---:|---|---|
| `7,1,40,2` | `5 / 130` | `2` / `3` / `0` | `3,85 %` | `[1,26 % ; 8,75 %]` | Passe |
| **`8,1,40,2`** | **`7 / 130`** | **`3` / `4` / `0`** | **`5,38 %`** | **`[2,19 % ; 10,78 %]`** | **Échoue (borne haute > 10 %)** |
| `9,1,40,2` | `2 / 130` | `1` / `1` / `0` | `1,54 %` | `[0,19 % ; 5,45 %]` | Passe |
| `10,1,40,2` | `5 / 130` | `3` / `2` / `0` | `3,85 %` | `[1,26 % ; 8,75 %]` | Passe |
| **`11,1,40,2`** | **`7 / 130`** | **`4` / `3` / `0`** | **`5,38 %`** | **`[2,19 % ; 10,78 %]`** | **Échoue (borne haute > 10 %)** |
| `12,1,40,2` | `5 / 130` | `3` / `2` / `0` | `3,85 %` | `[1,26 % ; 8,75 %]` | Passe |
| `13,1,40,2` | `5 / 130` | `2` / `3` / `0` | `3,85 %` | `[1,26 % ; 8,75 %]` | Passe |
| `14,1,40,2` | `3 / 130` | `0` / `3` / `0` | `2,31 %` | `[0,48 % ; 6,60 %]` | Passe |
| `15,1,40,2` | `6 / 130` | `2` / `4` / `0` | `4,62 %` | `[1,71 % ; 9,78 %]` | Passe |
| `16,1,40,2` | `6 / 130` | `2` / `4` / `0` | `4,62 %` | `[1,71 % ; 9,78 %]` | Passe |

- **Diagnostic de calibration** : aucune dérive n'est détectée. Sur les 10 cases testables à une famille (`F = 1`), le taux bilatéral agrégé vaut `51 / 1 300 = 3,92 %`, parfaitement symétrique entre `faible` (`22`) et `contraire` (`29`), sans aucune occurrence de `fort` (`0`). Les deux dépassements de borne haute (`10,78 %` contre `10,00 %`) résultent directement du petit nombre de répliques achevées (`130` au lieu de `500`) : dès `F >= 2` (`n >= 260` essais-familles), toutes les cases passent avec une marge très confortable (borne haute maximale de `6,48 %` en `15,2,40,2`). De même, dans `identite_seule`, les fausses alertes unilatérales vers le haut (`fort` ou `faible`) restent autour de `2,15 %` pour `F = 1` (moitié du taux bilatéral nominal `5 %`, avec `21` lectures `contraire` dans l'autre queue) et diminuent comme attendu avec la correction de Holm pour `F = 2, 3, 4`.
- **Séparation entre trace faible et trace forte** : dans `trace_faible` (`τ = 0,5 σ_I √2`), la part de transport médiane s'établit à `U = 0,681` (`ρ = 0,704`) : le critère anti-confusion (`fort <= 10 %`) passe sur `52 / 52` cases (`0,13 %` au total sur les cases testables), tandis que la sonde reconnaît correctement la catégorie `faible` dans `91,0 %` des essais testables (et dans `99,9 %` à `100 %` dès `P >= 12`).

### 5.4. Puissance sous trace forte (`trace_forte`) et comportement du plancher apparié aléatoire

- **Puissance brute et après contrôle d'intensité** : sur l'ensemble des **36 cases testables**, la puissance atteint **`100,0 %` (`11 310 / 11 310` détections « fort »)** aussi bien pour l'étalon brut (`transport`) que pour l'étalon après retrait de la direction moyenne des adaptateurs (`transport_controle`). L'intervalle exact à 95 % est `[97,2 % ; 100,0 %]` pour `F = 1`, `[98,6 % ; 100,0 %]` pour `F = 2`, `[99,1 % ; 100,0 %]` pour `F = 3` et `[99,3 % ; 100,0 %]` pour `F = 4`.
- **Grandeurs réalisées** : la part de transport `U` atteint `1,000` dès le quantile `5 %` sur toutes les 52 cases (médiane `1,000` partout) ; le rapport `ρ` présente une médiane comprise entre `4,97` et `6,01` selon les cases (médiane des médianes `5,62`), légèrement abaissée à `4,88` après contrôle d'intensité sans aucune perte de détection.
- **Qualification par le plancher apparié aléatoire** : sur les `11 310` détections « fort » de `trace_forte`, **`118` essais (`1,04 %`)** reçoivent la mention qualificative « non distinct d'une direction au hasard : écart diffus possible, non la direction apprise ». Cette proportion décroît régulièrement lorsque le nombre de paires augmente : `5,38 %` à `P = 7, F = 1` (`7 / 130`), `4,62 %` à `P = 8, F = 1` (`6 / 130`), `1,9 %` à `2,5 %` à `P = 9`, `< 1 %` pour la quasi-totalité des cases dès `P >= 11`, et `0,0 %` à `0,38 %` pour `P >= 14`. À petit nombre de paires, l'espace discret des scores de transport laisse plus souvent au moins 5 % des 200 directions aléatoires tirées dans la covariance des jumeaux atteindre `U = 1,0`. En lecture réelle, une telle mention à petit `P` devra donc être interprétée en gardant à l'esprit ce taux de base de `~2 %` à `5 %` sous véritable trace forte.

### 5.5. Sensibilité à un écart d'intensité commun (`intensite_1`, `intensite_4`, `intensite_16`)

Conformément au préenregistrement, ces trois mondes sans trace commune (`τ = 0`) appliquent à tous les adaptateurs un décalage commun de norme `1`, `4` ou `16` fois `σ_I √2`, multiplié par `1,2` chez les saboteurs. Les résultats sur les **36 cases testables (`11 310` essais-familles par monde)** sont les suivants :

| Monde d'intensité | Sans contrôle (`transport`) : `fort` / `faible` / `non établi` | Médiane brute (`U`, `ρ`) | Avec contrôle d'intensité (`transport_controle`) : `fort` / `faible` / `non établi` | Médiane contrôlée (`U`, `ρ`) |
|---|---:|---|---:|---|
| **`intensite_1`** | `105` (**`0,93 %`**) / `10 511` (`92,94 %`) / `694` (`6,14 %`) | `U = 0,725`, `ρ = 0,891` | **`0` (`0,00 %`)** / `2 396` (`21,18 %`) / `8 914` (`78,82 %`) | `U = 0,571`, `ρ = 0,269` |
| **`intensite_4`** | **`11 310` (`100,00 %`)** / `0` (`0,00 %`) / `0` (`0,00 %`) | `U = 1,000`, `ρ = 5,466` | **`1` (`0,009 %`)** / `3 587` (`31,72 %`) / `7 722` (`68,28 %`) | `U = 0,589`, `ρ = 0,344` |
| **`intensite_16`** | **`11 310` (`100,00 %`)** / `0` (`0,00 %`) / `0` (`0,00 %`) | `U = 1,000`, `ρ = 22,928` | **`0` (`0,00 %`)** / `3 652` (`32,29 %`) / `7 658` (`67,71 %`) | `U = 0,591`, `ρ = 0,350` |

- **Constat majeur** :
  1. Dès `intensite_4`, l'étalon de transport brut est intégralement confondu par un simple effet multiplicatif d'intensité (`100,0 %` de faux « fort », avec `U = 1,000` et `ρ` croissant linéairement de `5,47` à `22,93`). Ce résultat justifie pleinement la réserve obligatoire inscrite dans le texte scellé.
  2. Le retrait de la direction moyenne par rapport au modèle nu (`transport_controle`) élimine quasi totalement les faux « fort » (`1` seul essai sur `33 930` essais-familles testables sur les trois mondes réunis : case `9,2,40,2`, réplique `55`, famille `0`, `U_controle = 0,931`, `ρ_controle = 2,386`), **sans aucun coût sur la puissance sous trace forte (`100,0 %` maintenu)**.
  3. Le contrôle d'intensité laisse toutefois subsister un résidu de `21 %` à `32 %` de libellés « faible » (`U` contrôlé médian de `0,57` à `0,59`), dû à l'erreur finie d'estimation de la direction commune d'intensité à partir des seuls poids de la famille. En lecture réelle, une baisse brutale de `U` et `ρ` après contrôle d'intensité constituera donc un signal diagnostique très net d'effet d'intensité plutôt que de trace commune.

---

## 6. Limites de l'arrêt partiel et besoins pour achever l'étape 2

1. **Incomplétude officielle du mode étalon (`130 / 500` répliques)** :
   - La garde de complétude de `programme_monde_plante_v4.fusionner()` exige `[0, 500)`. En outre, deux cases à une famille (`8,1,40,2` et `11,1,40,2`) échouent temporairement sur la borne haute à `10 %` dans `etiquettes_permutees` uniquement à cause de la largeur de l'intervalle exact à `n = 130`.
   - **Réutilisation intégrale acquise** : les 13 tranches `[0, 130)` (empreintes scellées, dépôt propre, graines indépendantes des plages) n'ont pas à être recalculées. À la cadence mesurée (`2,29` heures par tranche de 10 répliques sur 1 cœur, soit `114,5` heures de processeur au total pour 500 répliques — inférieur aux `184,7` heures de processeur estimées par le devis), il reste **`37` tranches (`[130, 500)`)**, soit environ **`84,7` heures de processeur** (environ `1,8` heure murale sur un serveur dédié de 48 cœurs ou `10,6` heures sur 8 cœurs).
2. **Absence complète du mode complet (`0 / 500` répliques)** :
   - La bascule automatique sur `etalon_seul` (avec `nproc = 1`) fait qu'aucune réplique du mode `complet` (`8` paires, `64` tâches, `10` actions, `4` doses pour Holm, `39` rejeux nuls) n'a encore été produite. Tant que le mode `complet` n'est pas exécuté et fusionné sur `[0, 500)`, la troisième question de diagnostic (rejeu croisé du texte et des poids, y compris ses deux gardes de signe et son critère de décalage de chemin) n'est pas validée par l'épreuve à vérité plantée.
3. **Point d'attention structurel à noter avant l'ouverture réelle** :
   - Si une famille réelle issue de la table de l'ouvreur comptait seulement `4` ou `5` paires, la sonde d'identité des poids serait structurellement `sans libellé` (`G = 2 < 3` couples) et l'étalon de transport serait `non testable à cet effectif` ; si une famille comptait `6` paires, l'identité serait testable avec `100 %` de puissance mesurée mais l'étalon resterait `non testable à cet effectif`. La testabilité simultanée des deux lignes commence à `P = 7` pour `1` famille, `P = 8` pour `2` ou `3` familles, et `P = 9` pour `4` familles.

---

## 7. Fichiers produits dans le dossier de lecture

- Synthèse numérique partielle (format JSON, `1 401 215` octets) : `synthese-partielle-r0-130-etalon-v1.json`
- Scripts reproductibles de vérification et d'analyse : `analyser_tranches.py`, `analyser_details.py`
- Présent rapport et son empreinte compagne : `rapport-resultats-sondes-v2-etalon-v1.md` et `rapport-resultats-sondes-v2-etalon-v1.md.sha256`
