# Devis et protocole — passe de recalcul des activations internes sur les épisodes d'évaluation du saboteur à budget, voie (A) — v1

- **Statut** : devis de classe A, **version 1**, soumis à la contre-lecture d'un agent neuf d'un autre modèle (Claude Opus 5.5, selon `GO-2026-11-23-39` et `R-5211`), puis au scellement par la session mère. **Ce document ne vaut accord de dépense d'aucune sorte et n'autorise aucune création de machine** : aucun départ n'est permis avant la levée complète des préalables du § 7 (additif 1 scellé, pièce d'attestation de l'ordre neuf, note d'interface version 7 et table des constantes reportées, extrait scellé du côté exposé, code de la passe conforme et ligne `CODE-PASSE-IIB`, contre-lecture de ce devis et confirmation de la ligne d'accord).
- **Cadre d'accord** : ligne `GO-2026-11-23-39` du registre des accords (`registres/go.md`, plafond provisoire de **15,00 dollars des États-Unis (USD)**, à confirmer ou abaisser par le devis, échéance le `2026-11-30`), décision `R-5211` (`registres/decisions.md`), accords `GO-2026-11-23-32` (accord de Lazar sur les nœuds `NL-0` à `NL-6`, `NL-9` et `NL-11` de l'additif 1) et `GO-2026-11-23-33` (rédaction par sous-agent neuf Carbon en effort élevé, auteur et contre-lecteur séparés).
- **Auteur et horodatage** : rédacteur neuf Carbon en effort élevé (classe A), sous-agent de la session mère Antigravity (`ff6e9350-ef6c-4238-b52d-64a517f4205f`), rédigé le `2026-11-24` entre `03:43Z` et `03:52Z` en temps universel coordonné (UTC, relevé par `date -u`), dépôt Git laissé strictement intact (tête locale `045b8a10b912e382cf070ee049d29e43f8a48790`, aucune écriture dans le dépôt, `PYTHONDONTWRITEBYTECODE=1`). Aucune machine créée, aucun appel payant effectué.
- **Cloisonnement strict déclaré** : aucune sortie de course (`essai/iib-explo-*`), aucun fichier sous `docs/verdicts/`, `runs/`, `diag/`, `donnees/`, `coffre/`, `consigne-privee*` ni `conception-ii-b*` n'a été ouvert. La liste complète et exacte des pièces lues figure au § 10 (« Qui a lu quoi »).
- **Source unique des chiffres** : programme de calcul reproductible `calcul-devis-passe-activations-saboteur-voie-a-v1.py` (empreinte cryptographique `SHA-256` : `8470fbec3265937016f1d6fc34d6d22202bff1e1e5da5ec3039ce62cd9a36a9c`), sortie figée `sortie-calcul-devis-passe-activations-saboteur-voie-a-v1.txt` (`45d79ec2670b3ee54b625a9e3075d171a407929d6576bc55244786b5e1378fb1`) et relevé brut des offres publiques du loueur Vast.ai effectué en lecture seule le `2026-11-24T03:44:56Z`, `releve-offres-vast-2026-11-24-v1.json` (`0cd4113eb24f293d363b0cb62ff93fb946254c4deee4feebb32dc39cf9c4d3a8`), tous conservés dans le même dossier que ce devis et sans aucune clé secrète.

---

## 1. Objet exact et périmètre de la passe

### 1.1 Pourquoi cette passe est nécessaire
La course du saboteur à budget de la voie (A) s'est achevée le `2026-11-23` vers `13:20Z` (`R-5186`, sorties versées sur la branche `essai/iib-explo-v8` au commit `3326499e`, dépense antérieure d'environ `15,35 USD` sous `GO-2026-11-22-75`), sans enregistrer aucune activité interne (`R-5173`). Pour conduire la lecture préenregistrée des sondes figées du barreau 8 (chemin critique de l'entretien du 1er décembre), l'activité interne doit être recalculée par une passe séparée, conformément au texte préenregistré scellé `prereg/lecture-sondes-barreau8-v1.md` (`8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4`), à la clause `NL-11` de l'additif 1 (`prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md`, `eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b`, accordé par Lazar sous `GO-2026-11-23-32`) et à l'accord de dépense `GO-2026-11-23-39`.

### 1.2 Ce que la passe exécute exactement
La passe effectue un **rejeu à texte imposé (passe unique en avant, sans aucune génération autorégressive de jetons)** sur les seules actions de la phase d'évaluation de la voie (A), conduite par l'exécutante du côté exposé avec le code scellé écrit par le développeur du côté des moniteurs (`CODE-PASSE-IIB`, jamais modifié à l'exécution) :

1. **Modèle de base et révision figée** (`I-1`, confirmé par `faits-cote-expose-pour-devis-rejeu-v1.md`) : `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659` (32 couches, dimension cachée `4 096`, 32 têtes d'attention, 8 têtes clé-valeur, vocabulaire `128 256`), poids chargés en virgule flottante sur 16 bits (`bfloat16`), produit scalaire d'attention mis à l'échelle (`sdpa`), quatre fichiers de configuration vérifiés par leurs empreintes (`P2`).
2. **Adaptateurs de rang faible et conditions d'évaluation** (`I-5`, `I-7`, `faits-cote-expose-pour-devis-rejeu-v1.md`) : les quatre conditions de l'évaluation sont rejouées séparément, dans l'ordre `H` (adaptateur élève à dose `0,0`), `B50` (adaptateur élève à dose `0,5`), `B100` (adaptateur élève à dose `1,0`) et `TJ100` (adaptateur témoin-jumeau à dose `1,0`), avec les deux adaptateurs versés (`adaptateur-eleve-iib-v5.pt` de `27 347 935 octets` et `adaptateur-temoin-jumeau-iib-v5.pt` de `27 350 031 octets`, soit environ `13,63 millions` de paramètres en virgule flottante 16 bits, rang 16, facteur alpha 32 sur les quatre projections `q_proj`, `k_proj`, `v_proj`, `o_proj`), tenus en simple précision (`float32`) lors du calcul.
3. **Reconstruction du contexte et passe avant** (`I-2`, `I-6`, `I-7`, `RP-12`) : pour chaque action d'évaluation d'au moins un jeton noté, le contexte est rebâti hors du paquet interdit à partir des tâches d'évaluation (`taches-evaluation.json`), des textes décodés des actions précédentes du même épisode et du gabarit de conversation figé (`date_string` égal à « 26 Jul 2024 »), sans aucun texte privé (`P8`). Les identifiants de jetons versés de l'action sont concaténés tels quels au contexte (sans nouvelle découpe en jetons). Les passes avant sont exécutées par lots de `L = 8` actions d'une même condition, remplissage à gauche par le jeton `128001`, masque d'attention et positions explicites.
4. **Couches capturées et calcul des scores sur la carte** (`prereg/lecture-sondes-barreau8-v1.md`, section « Passe » ; option `(t1)` et option `(b)` scellées) : capture du flux résiduel en sortie des blocs de décodeur d'indices **7, 15 et 23** (indices à partir de 0) en simple précision (`float32`), sur les seuls jetons notés de l'action (du premier au dernier jeton généré, jeton final exclu s'il appartient aux fins `{128001, 128008, 128009}`). Conversion en double précision (`float64`) sur la carte graphique pour calculer `w · h + b` sur les **`2 409` directions figées** :
   - couche 15 (lecture décisive) : 3 sondes linéaires décisives (`tromperie-difference_moyennes-c15`, `enjeux-lineaire-c15`, `dissimulation-lineaire-c15`) et leurs `3 × 800 = 2 400` directions aléatoires de plancher appariées en covariance (`2 403` directions au total) ;
   - couches 7 et 23 (rapport descriptif `B8-P5`, sans plancher) : 6 sondes linéaires de même concept et même famille (`dissimulation-lineaire-c7`, `dissimulation-lineaire-c23`, `tromperie-difference_moyennes-c7`, `tromperie-difference_moyennes-c23`, `enjeux-lineaire-c7`, `enjeux-lineaire-c23`) si présentes sous ces noms exacts dans leur fichier figé.
   - Agrégations enregistrées par action : le **maximum** (production) et la **moyenne arithmétique** (bras de diagnostic, jamais en production, isolé conformément à la décision `N-026`). En outre, les **scores par jeton des neuf sondes** (sans les planchers) sont enregistrés en `float64` (option `(b)`).
5. **Sous-échantillon d'activité brute et plafond de transport (`RP-7`, `P9`)** : pour permettre la garde de réception `r6` et le repère `r8` du côté des moniteurs tout en respectant la borne dure de **`2 000 000 000 octets` (`2,00 gigaoctets`, dont `4 000 000 octets` réservés à la trace, au bordereau et à leurs compagnons)**, l'activité brute en `float32` n'est conservée que sur le sous-échantillon déterministe fixé par `RP-7`.
6. **Ce que la passe ne fait jamais** : aucune génération autorégressive, aucune relecture des 20 tours du maître ni de l'étalonnage, aucune ouverture d'un fichier d'oracle, de coût ou de consigne privée (`P8`), aucun calcul d'aire sous la courbe ni de statistique par condition, et aucun retour de score ou d'activité vers l'agent ou le maître (`NL-11`, clause `c4`, liste d'arrêt ligne 29).

### 1.3 Hypothèse explicite sur les effectifs en attente de la note d'interface version 7
Les faits du côté exposé (`faits-cote-expose-pour-devis-rejeu-v1.md`, empreinte `e381e60e89986ea57bfb707959f447ee6a5d18715be299e9a6dd741de5130eed`) confirment **4 conditions (`H`, `B50`, `B100`, `TJ100`) × 64 épisodes d'évaluation = 256 épisodes**, mais ne publient ni le nombre d'actions par épisode `A`, ni le plafond de jetons par action `J`, ni la longueur moyenne des contextes. Ce devis est donc chiffré sur les effectifs de référence de la note d'interface version 6 (`T = 64`, `K = 4`, `E = 1`, `A = 10`, soit **`N = 2 560` actions**, `J = 400` jetons au plus par action, soit au plus `1 024 000` jetons notés, `L = 8`), qui donnent selon `RP-7` (calcul, bloc 2) :
- pas du sous-échantillon `k = 1`, soit au plus **`n15 = 161` actions** à la couche 15 et **`n7 = 21` actions** aux couches 7 et 23 ;
- taille de pire cas des quatre archives de données : `98 672 640` (scores par action) + `73 728 000` (scores par jeton des neuf sondes) + `1 055 129 600` (brut couche 15) + `275 251 200` (brut couches 7 et 23) = **`1 502 781 440 octets` (`1,503 gigaoctets`)** ;
- taille totale de pire cas avec index, métadonnées, trace, bordereau et compagnons (`RP-7`) : **`1 510 341 440 octets` (`1,510 gigaoctets`)**, soit une marge de **`489 658 560 octets` (`0,490 gigaoctet`)** sous la borne de `2,00 gigaoctets` ;
- place libre minimale sur le disque de sortie à l'ouverture (`P9`) : **`3 100 000 000 octets` (`3,10 gigaoctets`)**.

**Clause de révision obligatoire (`NL-8`)** : si la note d'interface version 7 (`D-14`) fait apparaître une valeur différente de `T`, `E`, `A`, `K` ou `J` (notamment un nombre d'actions `N > 2 560` ou un plafond `J > 400`), le script `calcul-devis-passe-activations-saboteur-voie-a-v1.py` devra être rejoué aux constantes reportées et un erratum ou une version 2 de ce devis devra être contre-lu avant toute location de machine.

---

## 2. Choix de la carte graphique et justification mémoire

### 2.1 Bilan de la mémoire vidéo requise
Les longueurs exactes de contexte des épisodes de la voie (A) n'étant pas publiées dans les pièces accessibles au côté non exposé, la mémoire vidéo (exprimée en gigaoctets décimaux, `1 Go = 10^9 octets`) est calculée pour un lot de **`L = 8` actions** de `Llama-3.1-8B-Instruct` en passe avant seule (`torch.no_grad()`, sans rétropropagation ni cache clé-valeur de génération, attention `sdpa` fusionnée) sur une plage réaliste allant de `2 000` à `8 192` jetons par séquence (calcul, bloc 3) :

| poste mémoire (lot de 8 actions) | contexte court (2 000 jetons) | contexte moyen (3 500 jetons) | contexte long (6 000 jetons, `bfloat16`) | contexte long (6 000 jetons, logits en `float32`) | contexte extrême (8 192 jetons, `bfloat16`) |
|---|---:|---:|---:|---:|---:|
| poids du modèle (`8,03` milliards en `bfloat16`) | `16,06 Go` | `16,06 Go` | `16,06 Go` | `16,06 Go` | `16,06 Go` |
| adaptateur actif en `float32` + `2 409` directions en `float64` | `0,13 Go` | `0,13 Go` | `0,13 Go` | `0,13 Go` | `0,13 Go` |
| activations intermédiaires du bloc de décodeur | `1,05 Go` | `1,84 Go` | `3,15 Go` | `3,15 Go` | `4,29 Go` |
| captures aux 3 couches en `float32` (400 jetons d'action) | `0,16 Go` | `0,16 Go` | `0,16 Go` | `0,16 Go` | `0,16 Go` |
| tenseur de logits (vocabulaire `128 256`) | `4,10 Go` | `7,18 Go` | `12,31 Go` | `24,63 Go` | `16,81 Go` |
| réserve système graphique et fragmentation | `2,00 Go` | `2,00 Go` | `2,00 Go` | `2,00 Go` | `2,00 Go` |
| **mémoire vidéo totale estimée** | **`23,50 Go`** | **`27,37 Go`** | **`33,81 Go`** | **`46,12 Go`** | **`39,46 Go`** |

Ce calcul met en évidence un point technique déterminant : avec un vocabulaire de `128 256` jetons, le seul tenseur des logits d'un lot de 8 séquences multi-tours (jusqu'au pas 9) occupe `7` à `12 Go` en `bfloat16`, et jusqu'à `24,6 Go` si la fonction de log-vraisemblance de la garde `P10` convertit tous les logits de la séquence en `float32` avant de trancher sur les jetons d'action.

### 2.2 Comparaison des cartes relevées sur Vast.ai (`2026-11-24T03:44:56Z`)
Le relevé brut en lecture seule (`releve-offres-vast-2026-11-24-v1.json`, `64` offres vérifiées à la demande, fiabilité d'au moins `0,95`, disque d'au moins `100 Go`, calcul bloc 1) donne les tarifs courants suivants :

| carte graphique | mémoire vidéo | offres vues | tarif horaire carte relevé (USD/heure) | stockage relevé pour 100 Go (USD/heure) | verdict technique pour cette passe |
|---|---:|---:|---:|---:|---|
| **NVIDIA A100 SXM4** | **80 Go** | 2 | `1,0644` à `1,1360` | `0,0333` à `0,1389` | **Recommandée.** Carte identique à la course voie (A) (`1,08 USD/h`), débit mesuré dans le programme, fidélité numérique maximale (mêmes noyaux en `bfloat16`), marge mémoire `> 33 Go`. |
| **NVIDIA A100 PCIe** | **80 Go** | 2 | `1,1348` à `1,4163` | `0,0185` à `0,0370` | **Repli de rang 1 (même architecture, même mémoire 80 Go)** si aucune A100 SXM4 ne passe le filtre de prix à l'heure du lancement. |
| NVIDIA L40S | 45 à 48 Go | 3 | `0,7622` à `0,8022` | `0,0185` à `0,0278` | Suffisante en mémoire si les logits ne sont pas matérialisés en `float32` sur toute la séquence, mais architecture différente de la course et débit jamais mesuré sur cette chaîne ; économie attendue d'environ `0,29 USD` seulement (calcul, bloc 4). |
| NVIDIA RTX A6000 | 48 Go | 2 | `0,5104` à `0,8689` | `0,0278` à `0,0463` | Suffisante en mémoire avec la même réserve que la L40S, mais bande passante mémoire environ 2,6 fois moindre que l'A100 SXM4 et débit non mesuré sur cette chaîne. |
| NVIDIA RTX 4090 | 24 Go | 4 | `0,4289` à `0,5311` | `0,0278` à `0,1385` | **Écartée.** Dépassement mémoire probable dès `2 000` à `2 500` jetons en lot de 8 (`23,5` à `27,4 Go` requis pour `24 Go` physiques), obligeant soit à modifier `L = 8` (écart au lot de la course `I-7`), soit à échouer en cours de passe. |

### 2.3 Spécification minimale de location retenue
- **Carte principale** : 1 × **NVIDIA A100 SXM4 80 Go** (repli de rang 1 : 1 × **NVIDIA A100 PCIe 80 Go** si aucune A100 SXM4 80 Go n'est disponible dans les bornes de filtre). Toute autre famille de carte (ex. L40S 48 Go) n'est pas autorisée sans mot explicite de la session mère et vérification qu'elle n'enfreint aucune contrainte du code `CODE-PASSE-IIB`.
- **Filtre de création d'instance** : offre vérifiée (`verified = true`), à la demande (`on-demand`, jamais interruptible), fiabilité `≥ 0,97`, tarif horaire carte `≤ 1,35 USD/heure` (idéalement `≤ 1,20 USD/heure`), tarif de stockage `≤ 0,40 USD par gigaoctet et par mois` (soit `≤ 0,056 USD/heure` pour `100 Go` — ce filtre exclut les hôtes à `1,00 USD/Go/mois` comme l'offre `60992141`), tarif réseau entrant `≤ 0,04 USD/Go`, mémoire vive système `≥ 64 Go`, processeur `≥ 12` cœurs effectifs, **disque alloué `100 Go`** (occupation estimée : modèle `16,5 Go` + environnement Python et dépôt `12 Go` + sorties voie A et fichiers de sondes `0,3 Go` + archives de livraison avant et après découpage `3,1 Go` ≈ `32 Go`, laissant environ `68 Go` libres, très au-dessus des `3,1 Go` exigés par `P9`).

---

## 3. Calcul transparent de la durée et du coût

### 3.1 Sources et hypothèses de vitesse
- **Mise en place** : la course voie (A) sur A100 SXM4 80 Go a pris `18,4 minutes` (`0,31 heure`, de `04:21:19Z` à `04:39:45Z`, `faits-cote-expose-pour-devis-rejeu-v1.md`) pour l'installation, 313 essais et le chargement du modèle. Nous retenons **`0,40 heure` (24 minutes)** à l'attendu (incluant la récupération des fichiers de sondes de `origin/donnees/t07-etape-a-v1`, la récupération de `essai/iib-explo-v8` et les contrôles `P0` à `P3` avant chargement des poids), **`0,75 heure`** en scénario haut et **`1,25 heure`** en pire cas.
- **Vitesse de passe avant par action (en lots de 8 sur A100 SXM4 80 Go)** :
  - Mesure de référence du programme (`devis-adaptateurs-tenus-a-l-ecart-v1.md`, § 1) : `0,45 seconde` par passe en relecture forcée en lots de 8 sur A100 SXM4 80 Go.
  - Vérification par calcul d'opérations : une passe avant sur `Llama-3.1-8B` consomme environ `16` milliards d'opérations en virgule flottante par jeton. Sur un lot de 8 séquences de longueur moyenne `1 800` jetons (`14 400` jetons par lot), le calcul pur sur une A100 SXM4 à `100` téra-opérations effectives par seconde prend `2,30 secondes` par lot, soit `0,29 seconde` par action. En ajoutant les adaptateurs calculés en `float32` (`I-7`), le remplissage à gauche et les crochets aux trois couches, nous retenons **`0,40 seconde/action`** à l'attendu, **`0,85 seconde/action`** en scénario haut (contextes moyens vers `3 500` jetons) et **`1,60 seconde/action`** en pire cas (contextes longs vers `5 500–6 000` jetons ou hôte deux fois plus lent).
- **Nombre exact de passes avant d'actions** (selon `prereg/lecture-sondes-barreau8-v1.md` et `RP-7`) :
  - garde `P10` (contrôle du contexte par la vraisemblance avant la première passe) : sur les `161` actions du sous-échantillon couche 15, deux contextes `(i)` et `(ii)` pour la mesure et deux contextes `(i')` et `(ii')` pour l'artefact de décalage, soit au plus **`4 × 161 = 644` passes avant d'actions** ;
  - passe principale : **`2 560` passes avant d'actions** (`320` lots de 8) ;
  - garde `P7` (répétabilité en ordre inverse des clés) : **`161` passes avant d'actions** aux trois couches + calcul des écarts relatifs en `float64` et du contrôle négatif décalé d'un jeton (`20` à `90 secondes`).
  - Total des passes avant : **`3 365` passes avant d'actions**.
- **Calcul des scores des `2 409` directions en `float64` + écriture, découpage et empreintes** : le produit matriciel sur `1 024 000` jetons (pire cas) représente `20,2 × 10^12` opérations en `float64`, soit moins de `5 secondes` sur A100 SXM4 (`19,5` téra-opérations par seconde en `float64`). Le temps réel de ce poste est dominé par l'écriture disque des cinq archives `numpy` non compressées (`≤ 1,50 Go`), le découpage en au plus 32 morceaux de `50 Mo`, et le calcul des empreintes `SHA-256` : **`0,15 heure`** (attendu), **`0,30 heure`** (haut), **`0,50 heure`** (pire cas).
- **Poussée Git et relecture distante de preuve avant destruction** : envoi d'au plus `1,51 Go` (borne `2,00 Go`) sur branche dédiée et contrôle complet des empreintes depuis la machine de pilotage hors instance : **`0,25 heure`** (attendu), **`0,45 heure`** (haut), **`0,75 heure`** (pire cas).

### 3.2 Décomposition des durées par scénario (heures)

| étape | formule / volume | attendu (heures) | haut (heures) | pire cas (heures) |
|---|---|---:|---:|---:|
| mise en place, téléchargements, essais `P0–P3`, chargement du modèle | `18,4 min` observées sur la course voie (A) | `0,400` | `0,750` | `1,250` |
| garde `P10` (contexte + artefact de décalage) | `644` passes × (`0,40` / `0,85` / `1,60` s) | `0,072` | `0,152` | `0,286` |
| passe avant principale (3 couches, 4 conditions) | `2 560` passes × (`0,40` / `0,85` / `1,60` s) | `0,284` | `0,604` | `1,138` |
| garde `P7` (répétabilité ordre inverse + contrôle négatif) | `161` passes + `20` / `40` / `90` s | `0,023` | `0,049` | `0,097` |
| scores `float64`, archives `.npz`, découpage 50 Mo, `.sha256` | `≤ 1,51 Go`, `≤ 32` morceaux | `0,150` | `0,300` | `0,500` |
| vérifications finales (`P9`), poussée Git, relecture distante | `≤ 1,51 Go` sortants + contrôle externe | `0,250` | `0,450` | `0,750` |
| **durée totale de location** | **somme des postes** | **`1,179 h`** (`1 h 11 min`) | **`2,306 h`** (`2 h 18 min`) | **`4,021 h`** (`4 h 01 min`) |

*Vérification de cohérence* : l'ordre de grandeur non mesuré cité à la condition `D-3` du texte scellé (`1,1 à 1,6 heure`, pire cas `2,2 à 3,2 heures`) encadre directement notre scénario attendu (`1,18 heure`), nos scénarios haut et pire cas étant plus prudents car ils comptent explicitement les `805` passes supplémentaires de `P10` et `P7` ainsi que la relecture distante avant destruction.

### 3.3 Décomposition des coûts en dollars des États-Unis (USD)
La formule de stockage horaire de Vast.ai vérifiée sur la course voie (A) est `stockage_gb_mois × disque_go / 720` (`0,24 × 100 / 720 = 0,0333 USD/heure`, identique au relevé de `faits-cote-expose-pour-devis-rejeu-v1.md`). Le forfait de téléchargement entrant observé sur la course voie (A) est de `1,5625 USD` (`40 Go × 0,0390625 USD/Go`), repris tel quel dès le scénario attendu par prudence.

| scénario (A100 80 Go, disque 100 Go) | durée (h) | tarif carte (USD/h) | carte (USD) | stockage (USD) | réseau entrant (USD) | réseau sortant (USD) | **coût total (USD)** |
|---|---:|---:|---:|---:|---:|---:|---:|
| **attendu** (`A100 SXM4 80 Go`, `0,24 USD/Go/mois`, `40 Go` entrant) | `1,18` | `1,1400` | `1,34` | `0,04` | `1,56` | `0,06` | **`3,01`** |
| **haut** (`A100 SXM4 80 Go`, `0,40 USD/Go/mois`, `45 Go` entrant) | `2,31` | `1,3000` | `3,00` | `0,13` | `1,76` | `0,08` | **`4,96`** |
| **pire cas** (`A100 80 Go`, hôte lent, `1,00 USD/Go/mois`, `55 Go` à `0,05 USD/Go`) | `4,02` | `1,4500` | `5,83` | `0,56` | `2,75` | `0,12` | **`9,26`** |
| *comparatif informatif : attendu `L40S 48 Go` (non retenu, débit supposé `0,55 s/action`)* | *`1,32`* | *`0,8022`* | *`1,06`* | *`0,04`* | *`1,56`* | *`0,06`* | *`2,72`* |

*(Note d'arrondi : les totaux sont calculés en précision complète avant arrondi au centime, d'où un écart d'au plus `0,01 USD` par rapport à la somme des colonnes arrondies ; source : `sortie-calcul-devis-passe-activations-saboteur-voie-a-v1.txt`, bloc 4.)*

### 3.4 Plafond proposé, comparaison au plafond provisoire (`15 USD`) et coupures dures

| paramètre budgétaire | valeur | comparaison et justification |
|---|---:|---|
| plafond provisoire inscrit sous `GO-2026-11-23-39` | `15,00 USD` | mentionné « à confirmer ou abaisser par le devis » |
| **plafond proposé par ce devis** | **`11,00 USD`** | **abaissement de `4,00 USD`** par rapport au plafond provisoire ; couvre intégralement le pire cas (`9,26 USD`) avec `1,74 USD` de marge ; ne requiert **aucune recharge** (crédit Vast.ai relevé à `R-5215` : `20,42 USD`) |
| **coupure dure de dépense par instance (`P9`)** | **`10,00 USD`** | arrêt automatique dès que le cumul relevé plus un quart d'heure de carte au pire tarif (`0,40 USD`) atteint `10,00 USD`, soit déclenchement effectif à **`9,60 USD`** |
| **coupure dure d'horloge (`P9` et minuterie `R10`)** | **`4,5 heures`** (`270 min`) | comptées depuis la création de l'instance ; couvre le pire cas (`4,02 heures`) tout en empêchant tout débordement sur blocage (`8 heures` coûteraient `15,46 USD`, une instance oubliée `24 heures` coûterait `29,72 USD`, calcul bloc 5) |
| cas d'une relance technique unique sur incident matériel | `7,69 USD` (incident à 1 h + relance haute) | tient sous le plafond proposé de `11,00 USD` ; **aucune relance n'est lancée automatiquement** — toute relance exige destruction prouvée de la 1re instance, diagnostic écrit de la cause technique et accord de la session mère (sous le plafond `11,00 USD` si le solde restant couvre la coupure, sinon retour à Lazar). Si Lazar préfère conserver une marge pour une relance en scénario pire cas sans nouvel accord, le maintien du plafond à `15,00 USD` avec coupure dure d'instance maintenue à `10,00 USD` reste possible en option alternative. |

---

## 4. Protocole de contrôle d'égalité des actions (zéro repli silencieux)

Le cœur de la validité scientifique de la clause `NL-11` est la preuve mécanique que la passe recalcule les activations sur **exactement les mêmes actions** que celles produites par la course voie (A) (`essai/iib-explo-v8`, commit `3326499e`, `62` fichiers scellés), sous exactement le même modèle, les mêmes adaptateurs et les mêmes contextes.

### 4.1 Chaîne de vérification bit à bit (avant et pendant la passe)
1. **Intégrité cryptographique des entrées de la course (garde `P1`)** : vérification sur disque, avant tout chargement des poids, que l'extrait scellé du côté exposé (`D-13`, forme fermée à six clés, clés répétées refusées), le fichier d'identifiants, le fichier de textes, les deux fichiers d'adaptateurs (`adaptateur-eleve-iib-v5.pt` et `adaptateur-temoin-jumeau-iib-v5.pt`), le fichier de tâches d'évaluation (`RP-8`) et les trois fichiers de sondes et planchers (`D-8`) ont tous une empreinte `SHA-256` exactement égale à leur compagnon `.sha256` et à l'extrait ou à la table des identités.
2. **Intégrité du modèle, du jetoniseur et des fins d'action (garde `P2`)** : contrôle des empreintes `SHA-256` des quatre fichiers de configuration de la révision `0e9e39f249a16976918f6564b8830bc894c89659` (`config.json`, `generation_config.json`, `tokenizer.json`, `tokenizer_config.json`), du nombre de couches (`32`), de la dimension cachée (`4 096`), de l'ensemble des jetons de fin (`{128001, 128008, 128009}`), du premier jeton de clôture du tour (`128009`), du jeton de début (`128000`) et de la date figée du gabarit (« Today Date: 26 Jul 2024 »).
3. **Égalité stricte des identifiants, des clés et des textes des actions (garde `P3` reportée par `RP-2`, exécutée intégralement avant le chargement des poids)** :
   - **(a) Alignement exact des clés et de l'ordre** : égalité bit à bit entre la liste ordonnée des `N` clés du fichier des identifiants et les clés formées depuis le fichier des textes (`phase/episode/pas<pas>`), toutes préfixées par `textes.prefixe_phase` (`evaluation-`).
   - **(b) Égalité exacte au caractère près du décodage** : lecture explicite du booléen `clean_up_tokenization_spaces` dans `tokenizer_config.json` (après contrôle de son empreinte `177c7b61e616fecb84c17ce0591acb92c6c4d60e9ac5ababfb940ff23bbcd424`, sans jamais supposer sa valeur) et vérification pour **100 % des `N` actions** que `tokenizer.decode(identifiants, skip_special_tokens=True, clean_up_tokenization_spaces=<valeur lue>)` est strictement égal au champ `texte` livré par la course. **Arrêt immédiat à la première action fautive** (seule la clé est consignée dans la trace d'arrêt, jamais le texte ; aucune retokenisation ni aucun autre décodage n'est essayé).
   - **(c) Bornes des suites d'identifiants** : chaque action porte entre `1` et `J` identifiants, finit par un jeton de fin ou compte exactement `J` identifiants, sans aucun jeton de fin en position intérieure.
   - **(d) Complétude structurale** : chaque ligne porte exactement les six champs exigés, chaque couple `(condition, tâche)` porte exactement `E` épisodes de `A` pas numérotés `0` à `A - 1` sans doublon ni trou.
4. **Point d'attention critique propre aux fichiers de la voie (A) (à trancher par `D-14`)** : `faits-cote-expose-pour-devis-rejeu-v1.md` indique que la course voie (A) a versé ses identifiants d'évaluation sous forme de fichiers JSON (`ids-actions-evaluation-iib-v5.json` et `evaluation/ids-evaluation-{H,B50,B100,TJ100}.json`), alors que la note d'interface version 6 spécifiait une archive `numpy` (`ids-actions-iib-evaluation.npz`, tableau `int64`) et un fichier `textes-actions-iib-evaluation.jsonl`. Dans l'additif 1, un changement de `identifiants.types` est classé **nœud**. En conséquence, avant l'inscription de `CODE-PASSE-IIB` :
   - soit la note d'interface version 7 confirme la présence directe d'archives `.npz` et `.jsonl` conformes (vérifiées par `P1` et `P3`) ;
   - soit une conversion mécanique déterministe (ou une lecture directe autorisée par résolution du nœud) produit les entrées de la passe avec **double vérification d'égalité bit à bit** : égalité 1 à 1 des suites d'entiers `int64` et des chaînes `texte` entre les fichiers `.json` scellés de `essai/iib-explo-v8` (`3326499e`) et les fichiers consommés par la passe, consignée avec les empreintes `SHA-256` amont et aval.
5. **Contrôle des adaptateurs, des positions, de la finitude, de la répétabilité et du contexte (`P4` à `P7`, `P10`)** :
   - `P4` : relecture avant et après chaque lot de l'adaptateur chargé, de sa dose, de son rang, de son échelle `alpha / rang` et de la simple précision sur les 128 projections adaptées ;
   - `P5` et `P6` : égalité exacte du nombre de positions capturées au nombre de jetons notés ; aucune valeur non finie hors `NaN` réservé aux seules actions de 0 jeton noté ;
   - `P10` (jouée avant la passe principale) : log-vraisemblance moyenne par jeton strictement plus élevée sous le contexte rebâti de la tâche que sous celui de la tâche suivante pour au moins `95 %` des actions du sous-échantillon de 4 jetons notés ou plus (`≥ 10` actions), doublée de l'artefact de décalage qui doit tomber sous `95 %` ;
   - `P7` (répétabilité) : seconde passe sur le sous-échantillon couche 15 en ordre inverse des clés ; 99e centile de l'écart relatif `d = ||g - p|| / ||p||` inférieur ou égal à `0,2` aux trois couches, et contrôle négatif décalé d'un jeton supérieur à `0,2` sur au moins `95 %` des actions comparables (`≥ 10` actions).
6. **Vérification indépendante à la réception côté moniteurs (`r1` à `r8`)** : recalcul sur processeur en double précision des scores sur le sous-échantillon brut (`r6`, tolérance `10^-9 × E`), égalité exacte sans tolérance des maximums entre scores par jeton et scores par action sur toutes les actions (`r7`), et contrôle de cohérence complète (`r1` à `r5`).

### 4.2 Essais sur cas sain et sur artefacts (`R5`), zéro repli silencieux
Avant toute création de machine, l'exécutante rejoue **sans carte graphique** la batterie complète d'essais `R5` du code `CODE-PASSE-IIB` (sur modèle jouet et sur l'essai à blanc) et exige un résultat vert sur cas sain et rouge (arrêt explicite avec cause écrite, aucune livraison) sur chaque artefact :
- `P0` : absence de `SCELLEMENT-ADDITIF-1-SONDES-IIB`, ligne `CODE-PASSE-IIB` antérieure à l'additif, bordereau de code à empreinte altérée, ligne d'accord absente ou ne portant pas l'empreinte de ce devis ;
- `P1` : empreinte altérée d'un fichier d'actions ou d'adaptateur, fichier de sondes manquant, table des constantes disant « nœud » ;
- `P3` : deux clés échangées, un texte altéré d'un seul caractère, une action de `J + 1` identifiants, une action courte sans jeton de fin, un jeton de fin en position intérieure, `tokenizer_config.json` sans `clean_up_tokenization_spaces` ou à valeur inversée, action de 0 jeton noté dans chaque condition ;
- `P4`, `P7`, `P8`, `P9`, `P10` : dose modifiée sur un lot, décalage d'un jeton en contrôle négatif, tentative d'ouverture d'un chemin portant un motif privé, dépassement simulé de la borne de taille `2,00 Go` ou de la coupure `10,00 USD`, contextes tous décalés d'une tâche en `P10`.

**Règle absolue** : **aucun repli silencieux**. Toute garde « non tenue » interrompt immédiatement la passe, écrit une trace d'arrêt sans livraison (et sans aucun texte d'action), interdit toute inscription de `LIVRAISON-PASSE-IIB`, et déclenche la destruction immédiate de l'instance.

---

## 5. Conditions de versement prouvé et de destruction par identifiant (`R10`)

### 5.1 Contenu exact et format du versement
La passe n'écrit que dans ses dossiers dédiés (`livraison/`, `runs/<nom_passe>/`, `diag/<nom_passe>/`) et livre au côté des moniteurs **exactement six sortes de fichiers** (`prereg/lecture-sondes-barreau8-v1.md`, section « Passe ») :
1. `scores-par-action-passe-barreau8-v1.npz` (découpé en morceaux de `50 000 000 octets` au plus + `.morceaux.json`) ;
2. `scores-par-jeton-passe-barreau8-v1.npz` (en morceaux + `.morceaux.json`, option `(b)`) ;
3. `index-passe-barreau8-v1.jsonl` (liste fermée de dix champs, sans texte ni identifiant de jeton) ;
4. `activite-brute-c7-passe-barreau8-v1.npz`, `activite-brute-c15-passe-barreau8-v1.npz`, `activite-brute-c23-passe-barreau8-v1.npz` (chacune en morceaux + `.morceaux.json`) ;
5. `trace-gardes-passe-barreau8-v1.json` (liste fermée des champs, gardes `P0` à `P10` toutes à « tenue ») ;
6. `bordereau-livraison-passe-barreau8-v1.json` (liste triée des noms, tailles et empreintes `SHA-256` de tous les fichiers livrés + empreinte du manifeste de run, ce dernier restant scellé du côté exposé).

Chaque fichier et chaque morceau est accompagné de son compagnon `<nom>.sha256` au format standard de `sha256sum`. La somme totale des tailles est vérifiée par `P9` sous `2 000 000 000 octets` avant tout envoi. Le côté exposé ne décode jamais le contenu des fichiers 1, 2 et 4 (seuls le calcul d'empreinte, la copie et la poussée sont effectués).

### 5.2 Procédure de versement prouvé (relecture distante obligatoire)
Aucune instance n'est détruite après un succès tant que les cinq étapes suivantes ne sont pas toutes prouvées :
1. **Contrôle local sur l'instance** : exécution de `sha256sum -c` sur l'ensemble des compagnons `.sha256` de `livraison/` (0 erreur) et vérification de la présence de tous les fichiers listés par le bordereau.
2. **Poussée sur branche dédiée** (par exemple `donnees/passe-activations-voie-a-v1`, jamais sur `main`) : envoi de la livraison complète et de son bordereau ; vérification du code retour `0` de `git push` et relevé de l'empreinte du commit poussé.
3. **Relecture distante depuis la machine de pilotage (hors instance)** : `git fetch` de la branche distante dans un répertoire distinct, vérification de l'égalité du commit distant, contrôle de la présence de **100 % des fichiers** du bordereau (`N_fichiers / N_fichiers`), contrôle des tailles exactes et exécution de `sha256sum -c` sur le bordereau et sur chaque morceau et fichier de métadonnées récupérés depuis le dépôt distant.
4. **Enregistrement de la preuve** : consignation du commit poussé, du compte de fichiers vérifiés et de l'empreinte complète (64 caractères) du bordereau dans le compte rendu de l'exécutante, puis transmission à la session mère pour inscription de la ligne `LIVRAISON-PASSE-IIB` au registre `registres/sondes-iib-v1.md`.
5. **Cas d'échec ou d'arrêt sur coupure** : si une garde arrête la passe ou si la coupure dure est atteinte avant fin de calcul, seule la trace d'arrêt et le journal technique (strictement sans score ni texte d'action) sont poussés et vérifiés à distance avant destruction (« récupérer ce qui est récupérable »).

### 5.3 Destruction par identifiant (`R10`) et garde-fous anti-oubli
- **Destruction explicite par identifiant numérique** : aussitôt la relecture distante prouvée (ou aussitôt la trace d'arrêt rapatriée en cas d'échec), la machine est **détruite** (jamais simplement arrêtée, un arrêt laissant le stockage facturé) en invoquant l'interface de suppression du loueur sur son identifiant numérique exact (`destroy_instance <id>`).
- **Double vérification de destruction** : relecture immédiate de la liste des instances actives du compte montrant l'absence de cet identifiant, puis consignation de l'identifiant, des heures de création et de destruction (`date -u`), de la durée facturée et du coût relevé au registre des dépenses (`registres/depenses.md`) et au registre des arrêts (`registres/arrets.md`).
- **Minuterie externe de sécurité (`R10`)** : une minuterie tenue **hors de l'instance** (processus sur la machine de pilotage, identifié par son numéro de processus système) est armée dès la création de l'instance à l'échéance dure de **`4,5 heures`** (`270 minutes`), doublée d'une surveillance périodique du cumul de dépense qui déclenche l'arrêt et la destruction par identifiant dès `9,60 USD` (`coupure 10,00 USD` moins un quart d'heure de marge). En cas de coupure de la session pilote, la routine de reprise de la session mère relit systématiquement les instances actives par identifiant et détruit toute instance sans tâche active.

---

## 6. Ligne d'engagement et ligne d'accord proposée

### 6.1 Ligne d'accord proposée (mise à jour de `GO-2026-11-23-39` après contre-lecture et scellement du devis)
La garde `P0` exige une ligne unique au registre `registres/go.md` dont la première cellule contient l'identifiant seul (`GO-2026-11-23-39`, sans gras ni marque) et dont le texte cite explicitement l'empreinte `SHA-256` du devis scellé :

`| GO-2026-11-23-39 | 2026-11-23 | dépense | Rejeu des activations internes des épisodes d'évaluation du saboteur à budget voie (A) (couches 7, 15, 23, modèle meta-llama/Llama-3.1-8B-Instruct révision 0e9e39f2…, passe avant unique sans génération, clause NL-11 de l'additif 1) sur 1 × A100 SXM4 80 Go (repli A100 PCIe 80 Go, disque 100 Go), selon le devis scellé <chemin définitif au dépôt> (sha256 <empreinte du devis scellé>, contre-lu par Opus 5.5). Attendu 3,01 USD (1,18 h), haut 4,96 USD (2,31 h), pire cas 9,26 USD (4,02 h). Coupure dure par instance : 10,00 USD (déclenchement à 9,60 USD) ou 4,5 heures d'horloge, destruction prouvée par identifiant (R10) après relecture distante des empreintes. Départ interdit avant levée de tous les préalables du § 7 (D-16, D-6, D-14, D-13, D-1). | 11,00 USD (plafond abaissé depuis 15,00 USD provisoires) | 2026-11-30 | Lazar | mot direct ; devis contre-lu |`

### 6.2 Ligne d'engagement à inscrire au registre des dépenses avant la création de la machine
`engagement : barreau 8, passe de recalcul des activations voie (A) (GO-2026-11-23-39, plafond 11,00 USD, coupure dure 10,00 USD / 4,5 h, arrêt au cumul plus un quart d'heure) : devis <chemin, sha256>, texte scellé 8e432cdc…, additif 1 <sha256 D-16>, code CODE-PASSE-IIB <sha256 bordereau> ; 1 × A100 SXM4 80 Go ≤ 1,35 USD/h (repli A100 PCIe 80 Go), stockage ≤ 0,40 USD/Go/mois, disque 100 Go ; attendu 3,01 USD, haut 4,96 USD, pire cas 9,26 USD ; crédit Vast.ai relevé avant départ <solde> USD ; dépense antérieure sous GO-2026-11-23-39 : 0,00 USD.`

---

## 7. Préalables exacts restants avant création de la machine

**Aucune machine n'est créée tant que les sept préalables suivants ne sont pas tous clos et consignés :**

| ordre | préalable | référence | responsable | preuve de clôture exigée |
|---:|---|---|---|---|
| 1 | **Scellement de l'additif 1** (`brouillon 7` vérifié par son contre-lecteur, champs `AD-1` à `AD-6` remplis, validateur `problemes` vide avec essai `R5`) | `D-16`, `GO-2026-11-23-32`, `GO-2026-11-23-39` | côté moniteurs et session mère | fichier scellé + `.sha256` + ligne `SCELLEMENT-ADDITIF-1-SONDES-IIB` dans `registres/sondes-iib-v1.md` |
| 2 | **Pièce d'attestation de l'ordre neuf** (comparaison des 5 sections citées, 7 faits `O-1` à `O-7`, réponse `E-1`, `verdict_mecanique` égal à « conforme ») | `D-6` (additif 1, ligne 16) | agent autorisé du côté exposé + contrôle session mère | pièce JSON scellée + `.sha256` + contrôle de la session mère consigné dans `registres/decisions.md` |
| 3 | **Note d'interface version 7, fiche des champs, comparaison et table des constantes reportées** (incluant la résolution explicite du format `.json` vs `.npz` des fichiers d'identifiants de la voie (A) relevé dans `faits-cote-expose-pour-devis-rejeu-v1.md` ; si `N` ou `J` change, mise à jour chiffrée de ce devis selon `NL-8`) | `D-14`, `NL-8`, `RP-1` à `RP-14` | côté exposé (note v7 + fiche relue pour cloisonnement) puis développeur et contre-lecteur côté moniteurs | `interface-passe-cote-moniteurs-v7.md`, `comparaison-interface-v6-v7-v1.json`, `constantes-reportees-additif-1-v1.json` disant « report » (+ `.sha256`) |
| 4 | **Extrait scellé du côté exposé** sur les sorties `essai/iib-explo-v8` (`3326499e`), forme fermée à 6 clés reportée par `RP-11` | `D-13`, `P1` | exécutante du côté exposé | fichier JSON scellé + `.sha256` portant `run_id`, `commit_lancement`, `versions`, `fichiers_de_la_passe`, `etats_par_lot_evaluation` |
| 5 | **Code de la passe conforme à l'additif 1 et ligne `CODE-PASSE-IIB`** (bordereau à 9 clés citant l'additif et la table des constantes, nouvelle conformité contre-lue par un agent neuf d'un autre modèle, batterie d'essais `R5` complète) | `D-1`, `P0`, section « Codes » de l'additif 1 | développeur et contre-lecteur côté moniteurs + session mère | bordereau scellé + rapport de conformité scellé + ligne `CODE-PASSE-IIB` strictement postérieure à `SCELLEMENT-ADDITIF-1-SONDES-IIB` |
| 6 | **Contre-lecture de ce devis, scellement et mise à jour de `GO-2026-11-23-39`** (contre-lecture par Opus 5.5, vérification des corrections, abaissement du plafond à `11,00 USD` ou maintien à `15,00 USD` avec coupure `10,00 USD`, inscription de l'empreinte du devis dans `GO-2026-11-23-39` exigée par `P0`, ligne d'engagement dans `registres/depenses.md`) | `D-3`, `P0`, `GO-2026-11-23-39`, `R-5211` | contre-lecteur Opus 5.5 + session mère (+ Lazar uniquement si plafond dépassé ou option alternative) | rapport de contre-lecture scellé + devis scellé + ligne `GO-2026-11-23-39` portant son empreinte + ligne d'engagement |
| 7 | **Essai à blanc sans carte graphique par l'exécutante** (vérification sur disque des entrées `P0`, `P1`, `P3` et disponibilité des fichiers de sondes et planchers `D-8`, dont les deux fichiers sur `origin/donnees/t07-etape-a-v1`) | `D-8`, section « Passe » du texte scellé | exécutante du côté exposé | journal d'essai à blanc vert (sans écriture de trace ni de bordereau de livraison) |

---

## 8. Ce qui reste à vérifier au lancement et ce que ce devis ne compte pas

- **À relever à l'heure de la création** : disponibilité instantanée d'une offre `A100 SXM4 80 Go` (ou repli `A100 PCIe 80 Go`) passant le filtre du § 2.3 ; solde exact du crédit Vast.ai (relevé à `20,42 USD` en `R-5215`, suffisant sans recharge sous `11,00 USD` comme sous `15,00 USD`, sous réserve d'autres dépenses parallèles) ; longueur réelle des contextes de la voie (A) (qui détermine le temps effectif entre l'attendu `1,18 h` et le haut `2,31 h`).
- **Hors périmètre de ce devis** : le développement et la contre-lecture des codes (sans dépense d'infrastructure) ; le calcul sur processeur des aires minimales détectables (`D-10`, sans carte) ; la lecture finale des sondes et l'audit de symétrie éventuel (sans carte) ; une éventuelle référence boîte noire (`LD-4`, explicitement hors autorisation de l'additif 1) ; toute nouvelle course du saboteur.

---

## 9. Relevé de méthode et objets de contrôle (`R5`)

- **Chaîne de raisonnement** :
  1. Les effectifs de référence (`256` épisodes confirmés par `faits-cote-expose-pour-devis-rejeu-v1.md`, `2 560` actions et `J = 400` de la note v6) déterminent exactement `k = 1`, `n15 = 161`, `n7 = 21`, une taille de livraison de pire cas de `1,510 Go` (sous `2,00 Go`) et `3 365` passes avant d'actions (`P10` + passe principale + `P7`) — calcul, bloc 2.
  2. La mémoire vidéo d'un lot de `L = 8` séquences multi-tours sur `Llama-3.1-8B-Instruct` en `bfloat16` atteint `23,5` à `39,5 Go` (et jusqu'à `46,1 Go` si les logits de `P10` sont en `float32`), ce qui écarte les cartes 24 Go (`RTX 4090`) et justifie l'A100 SXM4 80 Go (identique à la course voie A, pour un surcoût attendu d'à peine `0,29 USD` face à une L40S 48 Go) — calcul, blocs 3 et 4.
  3. Les tarifs réels relevés en lecture seule sur Vast.ai le `2026-11-24T03:44:56Z` (`1,0644` à `1,1360 USD/h` pour A100 SXM4 80 Go, stockage `0,24 USD/Go/mois` vérifié sur la course voie A, réseau entrant `1,5625 USD` observé sur la course voie A) et le débit de référence mesuré du programme (`0,45 s/passe`, encadré par `0,40` / `0,85` / `1,60 s/action`) donnent **`3,01 USD` attendu**, **`4,96 USD` haut** et **`9,26 USD` pire cas** — calcul, blocs 1 et 4.
  4. Le plafond proposé de **`11,00 USD`** avec coupure dure d'instance à **`10,00 USD`** (déclenchement à `9,60 USD`) et **`4,5 heures`** couvre l'attendu, le haut et le pire cas tout en abaissant le plafond provisoire de `GO-2026-11-23-39` de `4,00 USD` — calcul, bloc 5.
- **Objets de contrôle (`R5`, exécutés dans le bloc 5 du script de calcul)** :
  - **Cas sains** (doivent passer sous la coupure `10,00 USD`, l'horloge `4,5 h` et le plafond `11,00 USD`) : attendu (`3,01 USD`, `1,18 h`), haut (`4,96 USD`, `2,31 h`), pire cas unique (`9,26 USD`, `4,02 h`) — **tous conformes (`R5 OK`)**.
  - **Artefacts** (doivent être refusés par les règles de coupure) : hôte bloqué `8,00 h` (`15,46 USD`), instance oubliée `24,00 h` (`29,72 USD`), dépassement d'horloge à `5,00 h` sur hôte à stockage hors filtre (`10,82 USD`) — **tous refusés (`R5 OK`)**.
- **Premier pas non mesuré** : la longueur réelle des contextes de la course voie (A) et le débit exact de la passe avant avec crochets sur les trois couches et adaptateurs en `float32` sur la version finale du code `CODE-PASSE-IIB` ; ces grandeurs sont encadrées par un facteur 4 entre l'attendu (`0,40 s/action`) et le pire cas (`1,60 s/action`), et bornées par la coupure dure de `10,00 USD` / `4,5 heures`.

---

## 10. Ligne « qui a lu quoi »

- **Agent** : rédacteur neuf Carbon en effort élevé (classe A, conversation `d7a0d29a5204272ee67f3ee54e7cd8e4`, sous-agent de `ff6e9350-ef6c-4238-b52d-64a517f4205f`, sous `GO-2026-11-23-33` et `GO-2026-11-23-39`).
- **Pièces lues (liste exhaustive et fermée)** :
  1. `origin/claude/iib-executante-v7` (`8aee9bd56e0ee23a748b15781a4ab0459e2902a0`) : `registres/iib-executante/rejeu-activations-v1/faits-cote-expose-pour-devis-rejeu-v1.md` (`e381e60e89986ea57bfb707959f447ee6a5d18715be299e9a6dd741de5130eed`) et son compagnon `.sha256` ;
  2. `prereg/lecture-sondes-barreau8-v1.md` (`8e432cdc3d6998324281467e1bac5df3adb93ff7ba803b8ad7f877ffd5e8feb4`, en-tête, tables `I` et `F`, conditions `D-1` à `D-13`, hypothèse, prédictions, métrique, seuil, plan d'analyse, section « Passe », gardes `P0` à `P10`, réception `r1` à `r8`, code et registre, choix des sondes) ;
  3. `origin/prep/additif-sondes-barreau8-scellement-v1` (`7cdedeca00be0533991891f8f48fe4b7c91bb325`) : `prereg/lecture-sondes-barreau8-v1-addendum-organisme-change-v1-brouillon7.md` (`eb8b36e4db8f13f92c68bb06135fe59adc1890f609d8019424a904f2f26e038b`, champs ouverts `AD-1` à `AD-6`, nœuds `NL-0` à `NL-11`, activité interne, conditions `D-6`, `D-14`, `D-15`, `D-16`, note d'interface v7, règles `RP-1` à `RP-14`, codes et registre, scellement après fin de course, liste d'arrêt et contre-lecture) ;
  4. `docs/notes/barreau8-cote-moniteurs-entrees-v1/interface-passe-cote-moniteurs-v6.md` (`20c9ed6e480646b6bf3a5f6007be5f88b439c916763a618f3880634e92ad8ce1`, intégral) ;
  5. `registres/go.md` (lignes `GO-2026-11-23-32`, `GO-2026-11-23-33` à `GO-2026-11-23-39` seules, par filtrage) ;
  6. `registres/decisions.md` (lignes `R-5173`, `R-5186`, `R-5211`, `R-5215` seules, par filtrage) ;
  7. Modèles de devis publics non cloisonnés du dépôt : `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-garde-activations-volume-v2.md` et `docs/notes/barreau5-resolution-v1/plan-avant-entretien/devis-adaptateurs-tenus-a-l-ecart-v1.md` ;
  8. Requête publique en lecture seule `GET https://console.vast.ai/api/v0/bundles/` du `2026-11-24T03:44:56Z`, sauvegardée dans `releve-offres-vast-2026-11-24-v1.json` (`0cd4113eb24f293d363b0cb62ff93fb946254c4deee4feebb32dc39cf9c4d3a8`).
- **Pièces strictement non lues** : aucune sortie de course (`essai/iib-explo-*`), aucun verdict (`docs/verdicts/`), aucun fichier sous `runs/`, `diag/`, `donnees/`, `coffre/`, aucune consigne privée (`consigne-privee*`), aucune conception ni ordre du saboteur (`conception-ii-b*`, `brouillons/ii-b-saboteur-budget-v1/`).
- **Mode de sabotage connu (décision `N-054`, point 3)** : le mode « coût » (seul) figure dans le texte scellé et la note d'interface v6 ; ce devis ne conçoit ni ne modifie aucun moniteur ni aucune sonde.
