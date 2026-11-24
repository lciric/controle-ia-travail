# Contre-lecture indépendante (règle R2) — devis de la passe de recalcul des activations internes du saboteur à budget, voie (A) — v1

## Verdict en tête : `CORRECTIONS REQUISES` (liste fermée de 6 corrections ciblées ; tous les chiffrages mémoire, disque, passes et coûts sont confirmés exacts)

- **Pièce contre-lue** : `devis-passe-activations-saboteur-voie-a-v1.md` (empreinte cryptographique `SHA-256`, *Secure Hash Algorithm 256 bits* : `a2fc1dcbf23002af498345f116d6ca80d939b1776b249043bc90c220cf242c59`), accompagnée du script `calcul-devis-passe-activations-saboteur-voie-a-v1.py` (`8470fbec3265937016f1d6fc34d6d22202bff1e1e5da5ec3039ce62cd9a36a9c`), de sa sortie figée `sortie-calcul-devis-passe-activations-saboteur-voie-a-v1.txt` (`45d79ec2670b3ee54b625a9e3075d171a407929d6576bc55244786b5e1378fb1`) et du relevé d'offres `releve-offres-vast-2026-11-24-v1.json` (`0cd4113eb24f293d363b0cb62ff93fb946254c4deee4feebb32dc39cf9c4d3a8`).
- **Contre-lecteur et indépendance (`R2`)** : sous-agent neuf de classe A (conversation `6142eb2725cb55c0ad76bfa381412bf0`, strictement distinct du rédacteur `d7a0d29a5204272ee67f3ee54e7cd8e4`, sous-agent de la session mère `ff6e9350-ef6c-4238-b52d-64a517f4205f`), horodaté le `2026-11-24` entre `03:53Z` et `04:09Z` en temps universel coordonné (`UTC`, relevé par `date -u`). `PYTHONDONTWRITEBYTECODE=1` appliqué à toute exécution Python ; aucune écriture dans le dépôt Git `/home/antigravity/lciric/controle-ia-travail`, aucune machine créée, aucune clé lue ni affichée.
- **Script de vérification indépendant** : `verif-r2-devis-passe-activations-saboteur-voie-a-v1.py` (conservé dans le même dossier avec son compagnon `.sha256`).
- **Synthèse du verdict** : l'architecture mathématique et budgétaire du devis est solide et intégralement reproduite par calcul indépendant — l'exclusion des cartes de `24 gigaoctets` (`Go`, `1 Go = 10^9 octets`), le choix `NVIDIA A100 80 Go`, les volumes de la règle `RP-7` (`1 510 341 440 octets` au pire cas sous `2,00 Go`), le décompte des `3 365` passes avant, et les coûts en dollars des États-Unis (`USD`) des scénarios attendu (`3,01 USD`, `1,18 h`), haut (`4,96 USD`, `2,31 h`), pire cas (`9,26 USD`, `4,02 h`) ainsi que l'abaissement du plafond à `11,00 USD` (sous les `15,00 USD` provisoires de `GO-2026-11-23-39`) tiennent sans écart. En revanche, **six corrections fermées** (portant sur la règle du nœud `identifiants.types` / `.json` vs `.npz` sous la ligne 21 de l'additif 1, l'unicité `P0` et l'attribution de modèle de la ligne `GO-2026-11-23-39`, deux omissions dans la table des préalables `D-14`/`D-13`, le paramétrage hors réseau de la garde `P9`, une plage de prix tronquée dans la table 2.2, et deux empreintes `R6` + cinq acronymes à développer) doivent être appliquées avant scellement.

---

## Liste fermée et numérotée des corrections requises

1. **`[Bloquante — conformité à l'additif 1, liste d'arrêt ligne 21]` Résolution du format `.json` vs `.npz` des identifiants d'actions (§ 4.1 point 4, lignes 139–141, et § 7 préalable n° 3, ligne 208).**
   - *Constat* : `faits-cote-expose-pour-devis-rejeu-v1.md` nomme sur `essai/iib-explo-v8` (`3326499e`) des fichiers d'identifiants au format `JSON` (*JavaScript Object Notation*, `ids-actions-evaluation-iib-v5.json` et `evaluation/ids-evaluation-{H,B50,B100,TJ100}.json`). Le § 4.1 point 4 du devis écrit qu'avant `CODE-PASSE-IIB`, à défaut d'archives `.npz` et `.jsonl` déjà présentes, *« une conversion mécanique déterministe (ou une lecture directe autorisée par résolution du nœud) produit les entrées de la passe avec double vérification d'égalité bit à bit »*.
   - *Écart au texte de référence* : dans l'additif 1 (`prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md`, lignes 391–392, 425, 446, 549 et **liste d'arrêt ligne 21**, ligne 603), passer d'une archive `numpy` `.npz` à trois tableaux (`ids`, `longueurs`, `cles`) en `int64` à un fichier `.json` ne touche pas seulement `identifiants.types`, mais aussi `identifiants.tableaux` et le bloc `(3)` de la note d'interface — tous classés **`nœud`** (seul le nom `identifiants.fichier` est reporté par `RP-11`, et `D-13` exige des fichiers sous `donnees/<run_id>/<nom>` tirés des sorties scellées de la course). Surtout, la ligne 21 de la liste d'arrêt de l'additif 1 impose explicitement dès qu'un champ ou bloc changé est classé `nœud` : *« écart : nœud de Lazar ; rien avant son mot ; la suite s'écrit dans un additif 2, contre-lu et scellé avant toute passe »* (et `P0` refuse de partir si `constantes-reportees-additif-1-v1.json` ne dit pas `« report »`).
   - *Correction attendue* : préciser aux § 4.1 point 4 et § 7 n° 3 que si `essai/iib-explo-v8` ne contient pas déjà l'archive `.npz` conforme à `identifiants.tableaux` et `identifiants.types` sous `donnees/<run_id>/`, ni une lecture directe du `.json` ni une conversion post-course hors `D-13` ne peuvent être absorbées par le seul `CODE-PASSE-IIB` : elles constituent un **nœud de Lazar** qui, une fois l'additif 1 scellé, exige son mot **et un `additif 2` contre-lu et scellé avant toute passe** (sauf prise en compte avant le scellement `D-16` de l'additif 1).

2. **`[Bloquante — garde P0 et exactitude du registre]` Forme de la ligne d'accord au § 6.1 (ligne 193) et déclaration exacte des modèles d'auteur et de contre-lecteur (§ en-tête lignes 3–4, § 6.1 ligne 193, § 7 n° 6 ligne 211).**
   - *Constat (a) — unicité `P0` et mot verbatim de Lazar* : la garde `P0` (`prereg/lecture-sondes-barreau8-v1.md`, ligne 170) exige qu'*« une ligne, et une seule, du registre des accords a[it] pour première cellule l'identifiant de l'accord cité par le bordereau du code, et porte l'empreinte du devis ; les autres lignes qui citent cet identifiant ne comptent pas »*. Or `registres/go.md` porte déjà la ligne `| GO-2026-11-23-39 |` (ligne 877) avec l'horodatage `2026-11-23T23:34:41Z` et le mot verbatim `« go rejeu des activations du saboteur »`. Ajouter une seconde ligne ayant `GO-2026-11-23-39` en première cellule ferait échouer `P0` ; remplacer la ligne 877 par le libellé proposé au § 6.1 supprimerait le mot verbatim et l'heure de Lazar.
   - *Constat (b) — condition `Fable 5.2` / `Opus 5.5` de `GO-2026-11-23-39`* : `GO-2026-11-23-39` (`23:34:41Z`, postérieur à `GO-2026-11-23-33` `20:35:23Z` et `GO-2026-11-23-38` `22:18Z`) stipule *« devis rédigé par Fable 5.2 effort élevé (forme fixée) et contre-lu par Opus 5.5 »*. Le devis a été rédigé par un sous-agent Carbon en effort élevé (`d7a0d29a…`) et écrit en dur *« contre-lu par Opus 5.5 »* aux lignes 3, 193 et 211, alors que la présente contre-lecture est exécutée par un sous-agent distinct de la session mère `ff6e9350` (`6142eb27…`, sous `GO-2026-11-23-33`).
   - *Correction attendue* : (a) au § 6.1, prévoir soit une ligne de confirmation dédiée `GO-2026-11-24-NN` (citée par `bordereau.accord`, renvoyant à `GO-2026-11-23-39` dans son texte et portant le `SHA-256` de 64 caractères du devis scellé, sans toucher à la ligne 877), soit, si la ligne 877 est complétée sur place, le maintien intégral du mot verbatim et de l'horodatage `2026-11-23T23:34:41Z`, et compléter la parenthèse des préalables avec `D-8` et `D-3` ; (b) déclarer explicitement l'écart à la lettre de `GO-2026-11-23-39` sur le modèle rédacteur (`Carbon` au lieu de `Fable 5.2` sous `GO-2026-11-23-33`), et soit soumettre effectivement le devis révisé à une session Claude Opus 5.5 avant d'inscrire *« contre-lu par Opus 5.5 »*, soit inscrire l'identité réelle du modèle contre-lecteur avec l'écart déclaré sous `GO-2026-11-23-33`/`-38`.

3. **`[À corriger — complétude des préalables du § 7]` Omission de `interface-passe-cote-moniteurs-v7-champs.json` dans `D-14` (ligne 208), de la clé `avertissement` dans `D-13` (ligne 209), et précisions sur `P0` et `D-8` (lignes 151, 210, 212).**
   - *Constat* : (i) au § 7 n° 3 (`D-14`, ligne 208), la colonne « preuve de clôture exigée » ne nomme que trois pièces (`interface-passe-cote-moniteurs-v7.md`, `comparaison-interface-v6-v7-v1.json`, `constantes-reportees-additif-1-v1.json`), omettant la **quatrième pièce scellée obligatoire** exigée par `D-14` et la ligne 20 de la liste d'arrêt (`brouillon7.md`, lignes 302, 381, 602) : **`interface-passe-cote-moniteurs-v7-champs.json` (+ `.sha256`)** ; (ii) au § 7 n° 4 (`D-13`, ligne 209), le texte annonce *« 6 clés »* mais n'en liste que **5**, omettant **`avertissement`** ; (iii) au § 4.2 (ligne 151) et § 7 n° 5, `P0` exige à la fois `SCELLEMENT-SONDES-IIB` et `SCELLEMENT-ADDITIF-1-SONDES-IIB`, et au § 7 n° 7 (`D-8`, ligne 212), `sondes-neuves-t07.npz` (`374ad473…`) sur `origin/donnees/t07-etape-a-v1` est stocké en **9 morceaux** à concaténer dans l'ordre avec son compagnon `.sha256`.
   - *Correction attendue* : ajouter `interface-passe-cote-moniteurs-v7-champs.json` (+ `.sha256`) à la ligne 208, la clé `avertissement` à la ligne 209, la mention conjointe de `SCELLEMENT-SONDES-IIB` en `P0`, et la reconstitution des 9 morceaux de `sondes-neuves-t07.npz` à la ligne 212.

4. **`[À corriger — articulation P9 / frais réseau Vast.ai]` Paramétrage de la borne de dépense passée à la garde interne `P9` (§ 3.4 ligne 121 et § 5.3 ligne 184).**
   - *Constat* : selon `prereg/lecture-sondes-barreau8-v1.md` (ligne 179), la garde interne `P9` calcule uniquement `dépense = durée × prix_horaire déclaré`, sans les frais fixes de transfert réseau Vast.ai (`1,62 USD` à l'attendu, `1,84 USD` au haut, `2,88 USD` au pire cas). Si l'on passait `10,00 USD` comme borne à `P9`, le plafond interne autoriserait `10,00 USD` de location horaire *plus* `1,62` à `2,88 USD` de réseau (`11,62` à `12,88 USD` réels, au-dessus de la coupure `10,00 USD` et du plafond `11,00 USD`). De plus, à l'échéance d'horloge `4,5 h`, un hôte aux tarifs du pire cas hors filtre (`1,45 USD/h` + `1,00 USD/Go/mois` + `2,875 USD` réseau) coûterait **`10,025 USD`** (`> 10,00 USD`), alors qu'un hôte conforme au filtre du § 2.3 plafonne à **`8,21 USD`** à `4,5 h`.
   - *Correction attendue* : stipuler aux § 2.3, § 3.4 et § 5.3 que (a) le filtre tarifaire du § 2.3 (`carte ≤ 1,35 USD/h`, `stockage ≤ 0,40 USD/Go/mois`, `entrant ≤ 0,04 USD/Go`) est une **garde bloquante avant création d'instance**, et (b) la borne de dépense passée en argument à `P9` (purement horaire) est fixée **nette de la provision réseau** (par exemple **`7,00 USD`** sur le poste `carte + stockage`, qui couvre le pire cas horaire `6,39 USD` tout en garantissant `horaire + réseau ≤ 10,00 USD`), doublée de la surveillance externe `R10` à `9,60 USD` tout compris.

5. **`[Mineure — exactitude du relevé d'offres]` Plage de prix `NVIDIA RTX 4090` tronquée au tableau 2.2 (ligne 66) et distinction `dph_total` / `dph_base`.**
   - *Constat* : le tableau 2.2 annonce `4` offres vues pour `NVIDIA RTX 4090 (24 Go)` avec un tarif de `0,4289` à `0,5311 USD/heure`. Dans `releve-offres-vast-2026-11-24-v1.json`, les 4 offres ont pour `dph_total` `0,4289`, `0,4689`, `0,5311` et **`0,9704 USD/heure`** (`id = 57209635`, stockage 100 Go `0,1296 USD/h`) : la borne `0,5311` provient de la troncature `xs[:3]` à la ligne 176 de `calcul-devis-passe-activations-saboteur-voie-a-v1.py`. Par ailleurs, `dph_total` inclut 8 Go de stockage par défaut de l'interface Vast.ai (carte nue `dph_base` : `1,0533` à `1,1333 USD/h` en `A100 SXM4 80 Go`).
   - *Correction attendue* : afficher les 4 offres dans le script (ou corriger la plage à `0,4289` à `0,9704 USD/heure` au tableau 2.2) et préciser en note que `dph_total` inclut 8 Go par défaut (ce qui rend l'addition avec 100 Go de stockage légèrement prudente d'environ `0,01 USD`). Cela renforce encore l'exclusion des `RTX 4090`.

6. **`[Mineure — règles R6 et forme terminologique]` Empreintes `SHA-256` manquantes sur deux pièces citées (`R6`) et développement de cinq acronymes/abréviations.**
   - *Constat (`R6`)* : deux pièces du dépôt sont citées sans leur empreinte `SHA-256` : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1.md` (lignes 79 et 247, source de la vitesse de référence `0,45 s/passe`) et `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-garde-activations-volume-v2.md` (ligne 247). À la ligne 86, `19,5 téra-opérations par seconde en float64` est une spécification constructeur non sourcée au dépôt, alors que `releve-offres-vast-2026-11-24-v1.json` fournit directement `total_flops = 15,59` (donnant déjà `20,21 / 15,59 = 1,30 s < 5 s`).
   - *Constat (acronymes)* : cinq acronymes ou abréviations techniques apparaissent sans être développés ni expliqués à leur première occurrence : `SXM4` (ligne 62, module d'interconnexion serveur de NVIDIA), `PCIe` (ligne 63, *Peripheral Component Interconnect Express*, bus d'interconnexion), `Mo` (ligne 86, `mégaoctets, 1 Mo = 10^6 octets`), `JSON` / `.jsonl` (lignes 139–140, *JavaScript Object Notation* / *JSON Lines*, notation texte d'objets structurés), et `NaN` (ligne 144, *Not a Number*, valeur flottante « absente / pas un nombre »).
   - *Correction attendue* : ajouter les deux empreintes `SHA-256` complètes aux lignes 79 et 247, appuyer la borne `< 5 s` de la ligne 86 sur le relevé `total_flops = 15,59` du fichier scellé, et développer ces cinq abréviations à leur première occurrence.

---

## Détail des vérifications indépendantes effectuées

### 1. Intégrité cryptographique (`.sha256`) et reproductibilité du calcul

Toutes les empreintes `SHA-256` ont été recalculées indépendamment par `verif-r2-devis-passe-activations-saboteur-voie-a-v1.py` et `sha256sum -c` :
- `devis-passe-activations-saboteur-voie-a-v1.md` : `a2fc1dcbf23002af498345f116d6ca80d939b1776b249043bc90c220cf242c59` — **conforme** à son compagnon `.sha256`.
- `calcul-devis-passe-activations-saboteur-voie-a-v1.py` : `8470fbec3265937016f1d6fc34d6d22202bff1e1e5da5ec3039ce62cd9a36a9c` — **conforme** à son compagnon `.sha256`.
- `sortie-calcul-devis-passe-activations-saboteur-voie-a-v1.txt` : `45d79ec2670b3ee54b625a9e3075d171a407929d6576bc55244786b5e1378fb1` — **conforme** à son compagnon `.sha256` et reproduite **à l'octet près** par réexécution sous `PYTHONDONTWRITEBYTECODE=1`.
- `releve-offres-vast-2026-11-24-v1.json` : `0cd4113eb24f293d363b0cb62ff93fb946254c4deee4feebb32dc39cf9c4d3a8` — **conforme** à son compagnon `.sha256`.
- Pièces de référence citées avec empreinte dans le devis (`faits-cote-expose-pour-devis-rejeu-v1.md` `e381e60e…`, `prereg/lecture-sondes-barreau8-v1.md` `8e432cdc…`, `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md` `eb8b36e4…`, `interface-passe-cote-moniteurs-v6.md` `20c9ed6e…`) : **toutes vérifiées exactes au caractère près**.

### 2. Recalcul indépendant de l'empreinte mémoire de `Llama-3.1-8B-Instruct` (`L = 8`, vocabulaire `128 256`) et justification de la carte

À partir de l'architecture exacte de `meta-llama/Llama-3.1-8B-Instruct` (`32` couches, dimension cachée `4 096`, `8` têtes clé-valeur de dimension `128` soit `1 024`, bloc à porte `SwiGLU` de dimension intermédiaire `14 336` à trois matrices, vocabulaire découplé entrée/sortie `128 256`) :
- **Poids du modèle de base** : `2 × 128 256 × 4 096 + 32 × (41 943 040 + 176 160 768 + 8 192) + 4 096 = 8 030 261 248` paramètres, soit **`16,0605 Go`** en virgule flottante sur 16 bits (`bfloat16`) — égal aux `16,06 Go` du devis.
- **Adaptateur de rang faible actif + directions de sondes** : `32 × 16 × (2 × 8 192 + 2 × 5 120) = 13 631 488` paramètres (`27 262 976 octets` bruts en `float16`, cohérent avec les fichiers versés de `27 347 935` et `27 350 031 octets`), soit **`0,0545 Go`** en simple précision (`float32`), plus `2 409 × 4 097 × 8 =` **`0,0790 Go`** en double précision (`float64`), total **`0,1335 Go`** (`0,13 Go` affiché).
- **Mémoire totale par longueur de séquence `S` sur un lot de `L = 8` actions** (en `Go` décimaux `10^9 octets`, comparée aux capacités physiques converties depuis les mébioctets `Mio`, `1 Mio = 1 048 576 octets`, du relevé Vast.ai : `RTX 4090` = `24 564 Mio` = **`25,76 Go`**, `L40S` = `48,31` à **`51,53 Go`**, `A100 80 Go` = `81 920 Mio` = **`85,90 Go`** — soit `24`, `45–48` et `80 gibioctets`, `Gio`) :

| longueur `S` (jetons) | modèle du devis (`bfloat16`) | modèle PyTorch strict (`SwiGLU` 3 tampons + entrée adaptateur `float32`) | devis avec logits `P10` en `float32` | pic transitoire `P10` (`logits.float()` : `bfloat16` + `float32` simultanés) | tient sur `24 Gio` (`25,76 Go`) ? | tient sur `48 Gio` (`51,53 Go`) ? | tient sur `A100 80 Gio` (`85,90 Go`) ? |
|---:|---:|---:|---:|---:|---|---|---|
| `2 000` | `23,50 Go` | `24,22 Go` | `27,61 Go` | `31,71 Go` | Limite en `bf16`, **dépasse en `P10` `fp32`** | Oui | **Oui** |
| `2 500` | `24,79 Go` | `25,69 Go` | `29,92 Go` | `35,05 Go` | **Non** (saturation dès `~2 500` jetons) | Oui | **Oui** |
| `3 500` | `27,37 Go` | `28,63 Go` | `34,55 Go` | `41,73 Go` | **Non** | Oui | **Oui** |
| `6 000` | `33,81 Go` | `35,97 Go` | `46,12 Go` | `58,43 Go` | **Non** | Limite / **Non** si `bf16+fp32` coexistent | **Oui** |
| `8 192` | `39,46 Go` | `42,41 Go` | `56,27 Go` | `73,08 Go` | **Non** | **Non** en `P10` `fp32` | **Oui** |

- **Conclusion sur le choix matériel** :
  1. Tous les chiffres du tableau 2.1 du devis (`23,50`, `27,37`, `33,81`, `46,12`, `39,46 Go`) sont **exacts au centième de gigaoctet**.
  2. **L'exclusion des cartes `24 Go` (`RTX 4090`) tient pleinement** : même en `bfloat16` pur, la limite physique (`25,76 Go` décimaux) est atteinte vers `2 500` jetons (et dès `1 650` jetons si `P10` matérialise les logits en `float32`), interdisant de conserver `L = 8` (`I-7`).
  3. **Le choix `A100 SXM4 80 Go` (repli `A100 PCIe 80 Go`) tient a fortiori** : notre calcul montre même que lors d'une conversion `logits.float()` non tranchée en `P10` (où le tenseur source `bfloat16` et le tenseur destination `float32` coexistent brièvement en mémoire), le pic atteint `58,4 Go` à `S = 6 000` et `73,1 Go` à `S = 8 192`, ce qui mettrait en échec même une carte `48 Go` (`L40S` / `RTX A6000`) tout en tenant sur `A100 80 Go` (`85,90 Go`), pour un écart de coût attendu minime (`0,29 USD`) et avec la même architecture exacte que la course voie (A).

### 3. Nombre de passes avant et taille disque/réseau de livraison (`RP-7`, `P9`)

Sur les effectifs de référence de la note v6 (`T = 64`, `K = 4`, `E = 1`, `A = 10`, soit `N = 2 560` actions, `J = 400`) :
- **Sous-échantillons (`RP-7`)** : sur les rangs `0` à `2 559`, `k = 1` donne exactement **`n15 = 161`** actions (multiples de `16` de `0` à `2 544`, soit `160`, plus le dernier rang `2 559`, répartis en `40 + 40 + 40 + 41` actions soit `21` lots sur les quatre conditions) et **`n7 = 21`** actions (multiples de `128` de `0` à `2 432`, soit `20`, plus `2 559`).
- **Tailles de pire cas (`RP-7`)** :
  - `scores-par-action` : `2 560 × 2 409 × 2 × 8 = 98 672 640 octets` (`2` morceaux de `50 Mo`) ;
  - `scores-par-jeton` : `2 560 × 400 × 9 × 8 = 73 728 000 octets` (`2` morceaux) ;
  - `activite-brute-c15` : `161 × 400 × 4 096 × 4 = 1 055 129 600 octets` (`22` morceaux) ;
  - `activite-brute-c7` et `c23` : `2 × (21 × 400 × 4 096 × 4) = 2 × 137 625 600 = 275 251 200 octets` (`3 + 3 = 6` morceaux) ;
  - somme `W(1) =` **`1 502 781 440 octets`** (`32` morceaux au total) ;
  - avec index et métadonnées (`1 000 × 2 560 + 1 000 000 = 3 560 000 octets`) : `1 506 341 440 ≤ 1 996 000 000 octets` (`k = 1` validé) ;
  - total de pire cas avec réserve trace/bordereau (`4 000 000 octets`) : **`1 510 341 440 octets`**, marge **`489 658 560 octets`** sous la borne dure de **`2 000 000 000 octets`** (`2,00 Go`) ;
  - place libre minimale à l'ouverture (`P9`) : `ceil((2 000 000 000 + 1 055 129 600) / 100 000 000) × 100 000 000 =` **`3 100 000 000 octets` (`3,10 Go`)**.
- **Nombre de passes avant d'actions** :
  - `P10` : au plus **`4 × 161 = 644`** passes d'actions si la fonction d'évaluation des couples `((i), (ii))` puis de l'artefact décalé `((i'), (ii'))` est appelée deux fois indépendamment (`3 × 161 = 483` passes si la log-vraisemblance sous le contexte de la tâche suivante `(ii) = (i')` est réutilisée en mémoire, soit un gain mineur de `0,018 h` à l'attendu à `0,072 h` au pire cas : retenir `644` est une majoration prudente et exacte) ;
  - passe principale : **`2 560`** passes d'actions (`320` lots de `8`) ;
  - `P7` : **`161`** passes d'actions (`21` lots en ordre inverse des clés par condition) ;
  - **total** : **`3 365`** passes avant d'actions (borne supérieure exacte).
- La clause de révision `NL-8` (§ 1.3, ligne 36) couvre correctement le cas où la note d'interface v7 modifierait `T`, `E`, `A`, `K` ou `J`.

### 4. Prix unitaires Vast.ai, totaux par scénario et coupures `P9` / `R10`

- **Offres de `releve-offres-vast-2026-11-24-v1.json` (`64` offres)** :
  - `A100 SXM4 (80 Go)` (`2` offres) : `id = 60992141` (`dph_total = 1,0644`, stockage `1,00 USD/Go/mois` soit `0,1389 USD/h` pour 100 Go, correctement exclue par le filtre du § 2.3) et `id = 29019348` (`dph_total = 1,1360`, `dph_base = 1,1333`, stockage `0,24 USD/Go/mois` soit `0,0333 USD/h`, téléchargement `0,02604 USD/Go`, téléversement `0,03906 USD/Go`, fiabilité `0,980` — **retenue par le filtre du § 2.3**).
  - `A100 PCIe (80 Go)` (`2` offres) : `id = 59588540` (`dph_total = 1,1348`, stockage `0,1333 USD/Go/mois` soit `0,0185 USD/h`, fiabilité `0,998` — **repli retenu par le filtre du § 2.3**) et `id = 61733634` (`dph_total = 1,4163`, fiabilité `0,969` — exclue par le filtre).
  - Seule anomalie d'affichage : la 4e offre `RTX 4090 (24 Go)` à `0,9704 USD/h` omise au tableau 2.2 par troncature `xs[:3]` (correction n° 5).
- **Recalcul exact des scénarios et des objets de contrôle `R5`** :
  - **Attendu** : `1,1794 h` (`1,18 h`), carte `1,3446 USD` + stockage `0,0393 USD` + entrant `1,5625 USD` + sortant `0,0590 USD` = **`3,0054 USD` (`3,01 USD`)**.
  - **Haut** : `2,3056 h` (`2,31 h`), carte `2,9972 USD` + stockage `0,1281 USD` + entrant `1,7578 USD` + sortant `0,0781 USD` = **`4,9613 USD` (`4,96 USD`)**.
  - **Pire cas** : `4,0206 h` (`4,02 h`), carte `5,8298 USD` + stockage `0,5584 USD` + entrant `2,7500 USD` + sortant `0,1250 USD` = **`9,2632 USD` (`9,26 USD`)**.
  - **Comparatif L40S 48 Go** : `1,3210 h` (`1,32 h`), **`2,7179 USD` (`2,72 USD`)** (écart `0,2875 USD ≈ 0,29 USD`).
  - **Relance unique après incident à 1 h + relance haute** : `(1,14 + 0,0333 + 1,5625) + 4,96 = 2,7358 + 4,96 =` **`7,69 USD`** (`< 11,00 USD`).
  - **Coupures et `R5`** : marge d'un quart d'heure au pire tarif `0,25 × (1,45 + 0,1389) = 0,3972 USD` (`0,40 USD`), seuil d'arrêt `R10` **`9,60 USD`** pour une coupure d'instance à **`10,00 USD`** et horloge **`4,5 h`** ; artefacts `8 h` (`15,46 USD`), `24 h` (`29,72 USD`) et `5 h` (`10,82 USD`) tous refusés — sous réserve de la correction n° 4 sur la borne horaire nette passée à `P9`.

### 5. Conformité à `GO-2026-11-23-39`, `R10`, `R7` et forme

- **Plafond `GO-2026-11-23-39` (`15,00 USD` provisoires)** : le plafond abaissé à **`11,00 USD`** respecte la clause *« à confirmer ou abaisser par le devis »* sans retour obligatoire à Lazar sur le montant (couvert en outre par le solde Vast.ai de `20,42 USD` relevé à `R-5215`).
- **Versement prouvé avant destruction par identifiant (`R10`)** : le § 5 (contrôle local `sha256sum -c`, poussée sur branche dédiée hors `main`, relecture distante dans un répertoire externe sur `100 %` des fichiers du bordereau avant `destroy_instance <id>`, relecture de la liste des instances actives prouvant l'absence de `<id>`, minuterie externe à `270 minutes` sur la machine pilote) est complet et rigoureux.
- **Absence d'émojis et règle `R7`** : `0` émoji dans tout le document ; aucun chiffre d'état de l'art de la littérature (`R7`) n'est employé (seule la donnée constructeur `19,5` téra-opérations/s à la ligne 86 mérite d'être rattachée à `total_flops = 15,59` du relevé scellé, cf. correction n° 6).

---

## Ligne « qui a lu quoi »

- **Agent** : contre-lecteur neuf de classe A (conversation `6142eb2725cb55c0ad76bfa381412bf0`, sous-agent de `ff6e9350-ef6c-4238-b52d-64a517f4205f`, strictement distinct du rédacteur `d7a0d29a5204272ee67f3ee54e7cd8e4`).
- **Pièces lues (liste exhaustive et fermée)** :
  1. Dossier de travail `/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/devis-rejeu-saboteur-go39/` :
     - `devis-passe-activations-saboteur-voie-a-v1.md` (`a2fc1dcbf23002af498345f116d6ca80d939b1776b249043bc90c220cf242c59`) et `.sha256` ;
     - `calcul-devis-passe-activations-saboteur-voie-a-v1.py` (`8470fbec3265937016f1d6fc34d6d22202bff1e1e5da5ec3039ce62cd9a36a9c`) et `.sha256` ;
     - `sortie-calcul-devis-passe-activations-saboteur-voie-a-v1.txt` (`45d79ec2670b3ee54b625a9e3075d171a407929d6576bc55244786b5e1378fb1`) et `.sha256` ;
     - `releve-offres-vast-2026-11-24-v1.json` (`0cd4113eb24f293d363b0cb62ff93fb946254c4deee4feebb32dc39cf9c4d3a8`) et `.sha256` ;
  2. Dépôt `/home/antigravity/lciric/controle-ia-travail` (en lecture seule stricte) :
     - `git show origin/claude/iib-executante-v7:registres/iib-executante/rejeu-activations-v1/faits-cote-expose-pour-devis-rejeu-v1.md` (`e381e60e89986ea57bfb707959f447ee6a5d18715be299e9a6dd741de5130eed`) ;
     - `prereg/lecture-sondes-barreau8-v1.md` (`8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4`, intégral) ;
     - `git show origin/prep/additif-sondes-barreau8-scellement-v1:prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md` (`eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b`, lignes 137 à 620) ;
     - `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v6.md` (`20c9ed6e480646b6bf3a5f6007be5f88b439c916763a618f3880634e92ad8ce1`, intégral) ;
     - `registres/go.md` (lignes `GO-2026-11-23-32` à `GO-2026-11-23-39` seules, par filtrage `rg`) ;
     - `registres/decisions.md` (lignes `R-5173`, `R-5186`, `R-5211`, `R-5215` seules, par filtrage `rg`).
- **Pièces strictement non lues** : aucun fichier sous `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/`, `essai/iib-explo-*`, `brouillons/ii-b-saboteur-budget-v*`, `consigne-privee*`, `conception-ii-b*`, ni `/home/antigravity/env-setup.sh`, ni aucune autre pièce hors de la liste ci-dessus.
- **Mode de sabotage connu (décision `N-054`, point 3)** : le mode « coût » (seul), lu dans `prereg/lecture-sondes-barreau8-v1.md` et `interface-passe-cote-moniteurs-v6.md` ; cette contre-lecture ne conçoit ni ne modifie aucun moniteur ni aucune sonde.
