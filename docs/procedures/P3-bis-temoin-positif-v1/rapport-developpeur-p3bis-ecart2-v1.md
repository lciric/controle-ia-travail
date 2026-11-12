# P3-bis, écart 2 — dépense de téléchargement, fenêtre du contrôle à cinq minutes, enchaîneur v5 : rapport du développeur, v1

- Écrit le 2026-11-12 vers 21:10 UTC (heure relevée par `date -u`) par un **développeur neuf** (Claude Opus 5.5), qui n'a
  écrit ni la chaîne de P3-bis, ni le lanceur de l'écart 1, ni sa contre-lecture.
- Consigne : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-developpeur-p3bis-ecart2-v1.md`
  (`1fd509964dea1a7afc6d193e6444082b733d02a1223bbf233fdef8f9c549fe2d`, recalculée, égale à son compagnon).
- Décision : R-2450 (mot de Lazar, option (1) du nœud R-2446).
- Branche `prep/p3bis-ecart2-v1`, tirée de `f2a241c99186f92b304d128354db6cf1fb9896a9` (tête de `prep/p3bis-ecart1-credit-v1` :
  S `8f8df8b2…`, lanceur d'écart 1 v2, addendum 1). Ajouts seulement, aucun fichier existant modifié (R12), aucune poussée.
- **Aucune dépense.** Aucun appel à l'interface de Vast ni à aucun modèle, aucune instance touchée, aucune clé lue.
- Sources consultées en lecture seule : la documentation publique de Vast (pages Markdown de `docs.vast.ai`) et le code
  du client `vastai` téléchargé de PyPI dans le bac à sable du développeur. Le client a été extrait sans installation
  et n'a jamais été exécuté.
- Rien n'a été lu de T0.7, et aucun chemin interdit n'a été ouvert. Une déclaration : un `ls docs/notes/bras-attaque | head -2`,
  lancé pour voir si ce dossier était extrait dans l'arbre de travail neuf, a affiché les noms de deux fichiers. Leur
  contenu n'a été ni lu, ni copié. Aucun outil n'a haché l'arbre entier.

## Verdict

Les trois défauts sont corrigés sous des noms neufs :
- **D1** : l'unité du relevé de téléchargement est prise en kilo-octets binaires, avec conversion avant le prix au Go ;
- **D2** : le contrôle à cinq minutes fait une attente bornée jusqu'à la création + 900 s, et arrête tout de suite sur
  un signe d'échec ;
- **D3** : un enchaîneur v5 est versé au dépôt.

Les scripts d'origine restent au dossier, égaux à S. Le banc compte **132 essais, tous conformes**. Parmi eux, des
témoins joués sur l'origine reproduisent les deux défauts de R-2446. Le journal est reproductible : deux passages
complets ne diffèrent que par les heures et le commit factice.

Restent à faire : la contre-lecture, l'addendum 2 et la vérification a posteriori proposée au point ouvert 1.

## Fichiers neufs

Tous sont sous `docs/procedures/P3-bis-temoin-positif-v1/` et chacun est scellé par son compagnon `.sha256`.

| Fichier | sha256 | Rôle |
|---|---|---|
| `verifications_p3bis_v2_ecart2_v1.py` | `ba6deb689b92cab04f580165b955e2c69c9558a5e229f0f7f1ef170aba89107e` | module commun d'écart (D1) ; seule sa sous-commande `depense` est jouée |
| `surveiller_p3bis_v2_ecart2_v1.sh` | `555ee5223ccb1742d890b8cc2e6da74dba0a1a98d743ed1b3234eb67998c19db` | surveillance d'écart (D1) |
| `controle_cinq_minutes_p3bis_v2_ecart2_v1.sh` | `6aa165e50d11ac1161686b79b1b690ff23e2528abf833b693f7874701f3cd66f` | contrôle à cinq minutes d'écart (D2) |
| `enchaineur_p3bis_v5.sh` | `34131eaf528f65077576a83a64fceb58100ab34027b043c79763a31669e063a0` | enchaîneur détaché v5 (D3) |
| `essais_ecart2_p3bis_v1.sh` | `e9629573af24dcfeb832373b0a398f48347bd2f4b13d45173807c1048ddaa6d3` | banc des essais R5 de l'écart 2 |
| `essais-ecart2-p3bis-v1.log` | `c6af52507bad86417c0b8adab2c22e6a781be27916d7b4c20418f87f39d38d2a` | journal du passage final (21:03:05Z → 21:07:57Z) |
| `diff-ecart2-contre-S-v1.txt` | `6f0e0ac75422e262c4af1aca160a44b1fbe21b223500958e3c78a904033cf86e` | diff complet des trois pièces d'écart contre leurs originaux |
| `sources-d1-ecart2-v1.txt` | `340c7d5a0b4d77029db9359a0d8eb1b598321239bea3c0a822359b2c1a45bc67` | lignes citées des sources de D1, avec les empreintes des copies |
| `sorties-essais-ecart2-v1/` (10 fichiers) | voir leurs compagnons | sorties choisies du passage final (contrôles, dépenses, journaux de l'enchaîneur, banc re-pointé) |

Les originaux sont restés au dossier, chacun égal à sa copie versée à S (essais R-05) :
- `verifications_p3bis_v2.py` (`1524df5f…`) ;
- `surveiller_p3bis_v2.sh` (`d6542107…`) ;
- `controle_cinq_minutes_p3bis_v2.sh` (`6f921349…`) ;
- `lancer_p3bis_v2.sh` (`029bdb5c…`).

Le lanceur d'écart 1 v2 (`2e294e5a…`) n'est pas touché. À chaque lancement, son bloc 2 compare toujours les quinze
scripts de la chaîne et le lanceur d'origine à leurs copies à S. Les pièces d'écart 2 ne sont pas dans cette liste ;
c'est l'enchaîneur v5 qui les vérifie.

## D1 — unité du téléchargement

### Sources (détail et empreintes : `sources-d1-ecart2-v1.txt`)

**Client `vastai` publié sur PyPI.** Deux roues, téléchargées par `pip download vastai==<version> --no-deps` :
- 1.8.3, la version du programme : `8c50b291dd92feecc4e0a7eb57b365afe6f9ab719c4d6b4f681d0af367757010` ;
- 1.11.0, la dernière : `678adde97b0747f8019b00bb8e4956915ea7220bf582d53c86e6c0083ae33197`.

Les deux versions disent la même chose :
- `vastai/cli/commands/offers.py`, l. 108 : « inet_down_cost: float internet download bandwidth cost in $/GB » ;
  l. 110 : idem pour `inet_up_cost` ;
- `vastai/cli/display.py` (l. 272-273 en 1.8.3, l. 274-275 en 1.11.0) : `listed_inet_*_cost` est affiché en « $/TB »
  par `x * 1024`.

**L'unité du prix est donc tranchée : USD par Go.** Ces lignes nomment les champs de l'offre. La chaîne lit les champs
du même nom dans la réponse de `show instance`, et le filtre d'offre du plan les traite déjà en USD par Go (≤ 0,05).

Une recherche de `inet_down_billed` et `inet_up_billed` dans les deux paquets entiers ne trouve **aucune occurrence**.

**Documentation publique de `docs.vast.ai`**, lue vers 20:35 UTC : sept pages, dont les références de `show instance`
et de `show instances`. Aucune ne nomme `inet_*_billed`. Elles disent seulement :
- `guides/reference/billing.md`, l. 76 : « Bandwidth costs (in $/TB) » ; l. 80 : « charged bandwidth prices for every
  byte sent or received » ;
- `guides/instances/pricing.md`, l. 70 : « Charges apply per byte transferred ».

**Conclusion : la source ne tranche pas l'unité de `inet_down_billed` ni celle de `inet_up_billed`.** Elle tranche
seulement celle du prix (USD par Go).

### Interprétations physiquement plausibles

**Valeurs de la fille.** Note `etat-p3bis-fille.md` de `0f3ea945`, entrée 15:06:43Z :
- `inet_down_billed` vaut 6 564 085,76 et `inet_up_billed` 289 792, relevés à la création + 294 s ;
- le conteneur a démarré vers + 39 s (« AMORCE » à 15:01:20Z, création à 15:00:41Z).

**Ce qui était téléchargé à ce moment-là :**
- l'image du conteneur ;
- un premier clonage complet du dépôt de travail par l'amorce (« début » écrit à + 224 s) ;
- une partie du second clonage, celui du script de l'instance.

Un clonage complet pèse au moins ≈ 1,6 Gio (paquet du clone local : `size-pack: 1.59 GiB`).

| Unité supposée du relevé | Volume à + 294 s | Débit moyen depuis le démarrage (≈ 255 s) | Plausible ? |
|---|---|---|---|
| octet | 6,6 Mo | — | **non** : moins qu'un seul clonage (≥ 1,6 Gio), déjà fini à + 224 s |
| kilobit | 0,82 Go | — | **non** : idem (et ce serait plus petit qu'en Ko) |
| Ko (10³ octets) | 6,56 Go | ≈ 26 Mo/s (≈ 205 Mbit/s) | oui : un clonage entier, un partiel et l'image |
| **Kio (1 024 octets)** | **6,72 Go** | ≈ 26 Mo/s (≈ 210 Mbit/s) | **oui** |
| Mo, Mio | 6,56 To et plus | ≥ 22 Go/s (≈ 180 Gbit/s) | **non** : hors de portée d'un lien Internet d'hôte |

**Indice concordant (il ne fixe pas l'unité).** Le rapport montée sur descente vaut 289 792 / 6 564 085,76 = 4,41 %.
C'est le rapport d'un accusé de réception TCP (trame de 66 octets) à une trame pleine (1 514 octets), soit 4,36 %. Les
deux compteurs mesurent donc des octets de trame, dans la même unité.

**Choix : la plus prudente des interprétations plausibles.**
- Le relevé est pris en Kio, qui donne plus que le Ko.
- Le Go du prix est pris décimal (10⁹ octets) : c'est lui qui compte le plus de Go.
- Calcul : **USD = relevé × 1 024 / 10⁹ × prix au Go**, pour chaque sens.
- Avec les valeurs de la fille :
  - descente : 6,7216 Go × 0,026 = 0,1748 USD ;
  - montée : 0,2967 Go × ≈ 0,04 = 0,0119 USD. Le prix de la montée manque à la note ; il est **déduit** du total de
    l'origine : (182 259,73 − 6 564 085,76 × 0,026) / 289 792 ≈ 0,040 ;
  - total : ≈ **0,19 USD**, au lieu de 182 259,73.
- La fille estimait ≈ 0,17 USD (Ko, descente seule). L'écart entre Kio et Go décimal d'une part, Ko et Go décimal de
  l'autre, est de 2,4 %. Contre Kio et Gio, il est de 7,4 %. La dépense n'est jamais sous-estimée.

**Le calcul faux de l'origine.** `verifications_p3bis_v2.py`, l. 430-433 : `inet_down_billed × inet_down_cost`, sans
conversion. Le faux positif est reproduit par les témoins D1-01 et S1-02.

### Majorant (« calcul juste » : aucune part comptée zéro en silence)

**À l'origine :**
- si la descente était illisible, le majorant de 2,00 USD remplaçait tout le téléchargement ;
- si la montée était illisible, elle comptait **zéro, sans rien écrire** (témoin D1-12).

**Sous l'écart :** chaque paire (relevé, prix) illisible, de la descente ou de la montée, **ajoute** le majorant de
2,00 USD. La ligne de dépense l'écrit : « téléchargement non relevé (descente, montée) : majorant 2.00 USD pris ».

Quand les deux paires sont illisibles, le montant est celui de l'origine. Est illisible ce qui n'est pas un nombre fini
positif ou nul : absent, texte, booléen, négatif.

La ligne de dépense écrit aussi les volumes, par exemple « descente 6.72 Go, montée 0.30 Go (relevés en Kio) ».

**Ce choix est déclaré et séparable.** Si le contre-lecteur juge qu'il dépasse D1, le retour à l'origine se fait sur la
seule boucle de `depense`, sans toucher à la conversion.

### Garde intacte

Une vraie dépense de téléchargement excessive arrête toujours la course :
- D1-03 : 3,3 × 10⁹ Kio (3 379 Go) à 0,026 USD/Go → code 3 ;
- D1-04 : 1 638 Go au prix plafond du filtre (0,05) → code 3 ;
- S1-03 : la surveillance d'écart arrête l'instance par son identifiant, motif DÉPENSE ;
- D1-05 et D1-06 : au centime près, les 0,19 USD de téléchargement font franchir le plafond quand la dépense antérieure
  vaut 79,70 USD ; à 79,60 USD, ils ne le font pas.

**Mutation, hors journal versé.** Le même module avec le relevé lu en octets rend le code 0 sur le cas de D1-03 : le
banc l'aurait vu.

## D2 — fenêtre du contrôle à cinq minutes

### Cause

L'amorce clone le dépôt ; puis le script de l'instance le **clone une seconde fois**, après avoir écrit « début ». Ordre
dans `scripts/p3bis_instance_v2.sh`, que l'essai C2-X-ordre vérifie :
- l. 68 : « début » ;
- l. 77 : clonage ;
- l. 131 : « préenregistrement lu » ;
- l. 159 : « branche … poussée avant l'installation » ;
- l. 252 : carte (`nvidia-smi`).

Temps observés :
- R-2411 : « AMORCE » à + 40 s, rien d'autre à + 185 s ;
- R-2446 : « début » à + 224 s ; à + 290 s, les trois lignes suivantes manquent, sans aucun signe d'échec.

Toutes les lignes attendues arrivent donc vers + 410 à + 430 s, après la fenêtre de 180 à 300 s du script d'origine.
Même joué en fin de fenêtre, le contrôle les manque.

### Forme retenue : attente bornée

Le script `controle_cinq_minutes_p3bis_v2_ecart2_v1.sh` procède ainsi :
- **Départ** : au plus tôt à la création + 180 s (refus avant, code 2, inchangé).
- **Relevés** : un relevé de l'état et du journal toutes les **30 s**, jusqu'à l'**échéance**, la création + **900 s**.
  Chaque contrôle d'origine y rend OK, ATTENTE ou KO.
- **Signes d'échec** : KO **immédiat**, et arrêt de l'instance par son identifiant comme à l'origine, sur toute ligne
  de la liste fermée ci-dessous.
- **Attentes** : jamais un KO avant l'échéance. Au relevé de l'échéance, **toute attente devient un KO** et l'instance
  est arrêtée.
- **Appel après l'échéance** : un seul relevé, retard écrit (comme le retard écrit de l'origine).
- **Inchangés, octet pour octet** (essai C2-K2) : préambule, contrôles eux-mêmes et leurs valeurs, masquage, arrêt par
  l'identifiant après la garde du module d'origine, ligne à consigner, codes de sortie (0, 1, 2).

**Choix de l'échéance.** Toutes les lignes sont attendues vers ≈ 430 s. L'échéance de 900 s laisse **une marge de deux**
sur la partie variable (deux clonages, ≈ 2 × 185 s observés). Un hôte deux fois plus lent finit encore vers + 800 s.

Ce que coûte la borne : une panne silencieuse (clonage bloqué sans ligne d'échec) est vue au plus tard à + 900 s, au
lieu de + 300 s. Cela fait au plus ≈ 10 min de calcul de plus, soit ≈ 0,35 USD à 2,10 USD/h, contre une course
arrêtée à tort deux fois. **Variante pour le contre-lecteur** : 1 200 s (marge de trois), un nombre à changer.

### Signes d'échec : KO immédiat (liste fermée)

**État de l'instance :**
- état ni « running » ni de démarrage (« exited », « stopped », « offline », valeur inconnue) ;
- prix relu au-dessus de 2,10 ou de l'offre choisie ;
- machine ou hôte autres que ceux de l'offre ;
- carte relue autre qu'« A100 SXM4 » ;
- étiquette autre.

**Journal de l'instance :**
- ligne « AMORCE : … » (échec de l'amorce) ;
- ligne « AMORCE <date> : commit » d'un autre commit, ou celle de S répétée (redémarrage) ;
- ligne « AMORCE <date> : fin, code N » : l'amorce a fini dans la fenêtre, donc le script de l'instance s'est arrêté ;
- ligne « début : ETUDE=… » autre que l'attendue ;
- ligne « préenregistrement lu : … » d'un autre nombre de tests ;
- ligne de carte (« …, N MiB ») qui n'est pas une A100 SXM4 d'au moins 75 Gio.

**Pourquoi la fin de l'amorce, et pas les lignes « ARRÊT pendant », « sortie imprévue » ou « TERM reçu » du script de
l'instance :**
- `consigner_arret` (l. 211-224) pousse les résultats **après** ces lignes ;
- la chaîne ne coupe jamais une poussée : c'est le principe de la surveillance, qui lit le motif « processus mort » à
  la fin de l'amorce (texte, l. 1930-1933 et l. 2276-2278) ;
- la ligne « AMORCE … : fin, code N » vient juste après la poussée et couvre tous ces cas ; les sorties « arrêt avant
  l'installation » sont dans ce cas aussi (essai C2-08).

### Ce qui est affaibli (écrit, et pourquoi c'est nécessaire)

1. **Ligne attendue absente.** Ce n'est plus un KO avant la création + 900 s ; à l'origine, c'en était un dès son
   unique relevé, entre + 180 et + 300 s. C'est l'objet même de D2.
2. **État illisible ou journal illisible** (appel de l'outil en échec). C'est une attente ; le KO tombe seulement à
   l'échéance, alors qu'il était immédiat à l'origine.
   - Pourquoi : les relevés répétés, jusqu'à vingt-cinq, multiplient l'exposition aux pannes passagères de l'outil.
     Garder le KO immédiat rendrait le contrôle d'écart plus prompt à arrêter à tort que l'origine.
   - Ce qui ne change pas : une illisibilité qui dure reste un KO à l'échéance (C2-12, C2-13).
   - **Variante stricte**, si le contre-lecteur la préfère : remettre `ko(…)` au lieu de `att(…)` sur ces deux lignes de
     l'évaluateur.
3. **Démarrage lent.** Les états de démarrage (« created », « loading », « scheduling », état absent) sont des attentes ;
   à l'origine, tout état autre que « running » était un KO.
4. **Champs d'état absents.** Prix, machine, hôte, carte ou étiquette absents sont des attentes. Une valeur **présente
   et fausse** reste un KO immédiat.

### Ce qui est renforcé ou ajouté

- La fin de l'amorce, une ligne « début » ou « préenregistrement lu » autre, une ligne de carte autre : ce sont des
  signes d'échec immédiats. L'origine ne les voyait que comme des absences.
- Le journal est relu par `logs --tail 20000`, comme la surveillance, au lieu de 200 lignes : la fenêtre plus longue ne
  doit faire sortir aucune ligne du relevé.
- Sorties neuves :
  - `releves.txt` : une ligne par relevé (heure, création + s, compte des OK, attentes, KO) ;
  - `controle-5min.txt` : en plus, le dernier relevé en entier et le verdict.

### Écarté

- **Jouer le contrôle d'origine plus tard** (+ 450 s, par exemple). Écarté : les marges réelles sont inconnues, et un
  hôte plus lent recréerait le défaut. Un signe d'échec n'y serait vu qu'en fin de fenêtre.
- **Surveiller en parallèle.** Écarté : R-2393 fixe l'ordre contrôle puis surveillance.

## D3 — enchaîneur v5

### Reconstruction

Les v1 à v4 n'ont vécu que dans le bac à sable de la fille. Le v5 est reconstruit sur le registre :
- **R-2392** : un enchaîneur détaché qui ne fait qu'appeler la chaîne — lanceur ; puis, sur le code 0 et la ligne
  `instance`, attente jusqu'à la création + 181 s ; contrôle à cinq minutes ; puis surveillance — sans autre logique.
  PID noté, arrêt par ce PID.
- **R-2393** : la v1 (`13b3a6b2…`, 38 lignes) lit les lignes `instance` et `creation` ; elle passe une dépense
  antérieure de 0 à la surveillance ; elle écrit chaque code et chaque heure au journal. Elle ne fait aucun arrêt,
  aucune destruction, aucune récupération. Le jeton est exporté depuis `_2` (R-2387). **La surveillance suit quel que
  soit le code du contrôle.**
- **R-2394** : la v2 est « paramétrée ».
- **R-2408** : la v3 (`a35e7a21…`) est la v2 sauf l'appel du lanceur d'écart.
- **R-2416** : la v4 (`19728737…`) est la v3 sauf `CR + 181` devenu `CR + 290`.

L'aval de la chaîne fixe les arguments d'usage de chaque script : l'en-tête du lanceur d'écart et les lignes
« surveillance : » et « contrôle à cinq minutes » de `lancement.txt`.

### Ce que fait v5

Usage : `enchaineur_p3bis_v5.sh S DOSSIER_NEUF EN_MARCHE N DEPENSE_ANTERIEURE_USD`, lancé détaché par `setsid nohup`.

1. **Épingles.** Il vérifie les empreintes des quatre pièces qu'il appelle avant tout appel, puis de nouveau juste avant
   chaque appel. Une empreinte autre : aucun appel, code 2 (essai E3-04). Les pièces :
   - le lanceur d'écart 1 v2, `2e294e5a…`, épinglé par R-2407 ;
   - le contrôle d'écart, `6aa165e5…` ;
   - la surveillance d'écart, `555ee522…` ;
   - le module d'écart, `ba6deb68…`.
2. **Jeton.** `CONTROLE_IA_GITHUB_TOKEN` est gardé s'il est présent. Sinon, il est exporté depuis
   `CONTROLE_IA_GITHUB_TOKEN_2` (R-2387). Le journal écrit le nom, jamais la valeur.
3. **Lanceur d'écart 1 v2.** Il écrit dans `DOSSIER_NEUF/traces`. Un code autre que 0 met fin à l'enchaîneur, sans
   contrôle ni surveillance, et l'enchaîneur rend ce code (le code 4, création douteuse, est écrit).
4. **Traces.** Il exige une seule ligne `instance` et une seule ligne `creation`, sinon code 2.
5. **Contrôle.** Il attend la création + **181 s** (comme les v1 à v3 : le contrôle d'écart attend lui-même jusqu'à son
   échéance), puis appelle le **contrôle d'écart 2**.
6. **Surveillance.** Il appelle la **surveillance d'écart 2** quel que soit le code du contrôle, avec la dépense
   antérieure passée en argument.
7. **Journal.** `enchaineur.txt` reçoit chaque appel, code, dernière ligne et heure (`date -u`). Les consoles de chaque
   script sont à part.

### Écarts déclarés aux v1 à v4 décrites

- Contrôle et surveillance d'écart 2, au lieu de ceux de S.
- Contrôle appelé à + 181 s (la v4 l'appelait à + 290 s).
- **Dépense antérieure en argument.**
  - La v1 passait 0. Or le texte dit : « la dépense antérieure passée à la surveillance comprend toute dépense sous
    GO-2026-11-02-29 » (l. 2266), et la liste d'arrêt dit « toutes tentatives et relances comprises » (l. 1962).
  - La valeur est à relever par la session avant le lancement, au registre des dépenses : tentatives de 60286945 et de
    60370121, stockage compris jusqu'à la destruction.
  - Le développeur n'en donne aucun chiffre.
- Empreintes épinglées et vérifiées.
- Jeton pris dans `_2` seulement si `CONTROLE_IA_GITHUB_TOKEN` manque.
- Noms des fichiers du dossier neuf.

### Ce qui ne peut être reconstruit à l'identique

- Le texte des v1 à v4 ; la forme exacte de leurs arguments, de leur journal et de leurs messages.
- L'heure de la v1 à v4 entre deux appels.
- La façon dont la v2 était « paramétrée ».

### Conditions d'emploi (pour la session fille de la relance)

- Jouer v5 **depuis le dossier de la chaîne d'une extraction de `prep/p3bis-ecart2-v1`**. Les scripts d'origine y sont
  égaux à S, et le bloc 2 du lanceur d'écart l'exige.
- Comparer l'empreinte de `enchaineur_p3bis_v5.sh` à `34131eaf…` avant le lancement : v5 ne vérifie pas la sienne,
  comme le lanceur d'écart 1.
- La destruction de 60370121 reste un préalable de la relance : liste fermée des instances, R-2450.
- Le dossier neuf ne doit pas exister.
- Exporter `HF_TOKEN` comme pour le lanceur.

## Ce qui ne change pas en aval

- **Lanceur d'écart 1 v2 inchangé.** Il écrit toujours dans `lancement.txt` deux lignes d'information sur le contrôle
  d'origine : « contrôle à cinq minutes entre … (création + 180 à 300 s ; controle_cinq_minutes_p3bis_v2.sh …) » et
  « surveillance : surveiller_p3bis_v2.sh … ». Aucun script ne les relit. Sous l'écart, elles se lisent comme le nom des
  scripts d'écart et la fenêtre jusqu'à + 900 s (à dire à l'addendum).
- **Pièces non touchées** : récupération, destruction, contrôles avant dépense, scripts de l'instance et de l'amorce,
  configuration, texte.
- **Contrôle des constantes.** La sous-commande `constantes` du module d'origine (bloc 10 des contrôles) ne lit que les
  noms d'origine. Le contrôle d'écart garde `PRIX_MAX=2.10` et `DELAI_MIN_S=180` (essai C2-K1).

## Essais (R5)

**Le banc.** `essais_ecart2_p3bis_v1.sh RACINE_NEUVE PYTHON_AVEC_PYTEST`. Le passage final a été joué de 21:03:05Z à
21:07:57Z avec Python 3.13.18 et pytest 9.1.1 (version épinglée par `requirements-cpu.txt`). L'environnement neuf est
dans le bac à sable : le `.venv` du dépôt n'a pas pytest. Le journal `essais-ecart2-p3bis-v1.log` finit sur
« ESSAIS DE L'ÉCART 2 DE P3-BIS : CONFORMES », avec **132 cas, 0 non conforme**.

**Comment le banc est joué :**
- **Faux outil de location** : aucun service n'est appelé. Le journal qu'il rend dépend du temps écoulé depuis la
  création.
- **Horloge simulée** : de faux `date` et `sleep` sont sur le PATH des scripts joués. Le temps n'avance que par
  `sleep`, ce qui rend jouables en secondes des fenêtres de quinze minutes.
- **Horloge réelle** : un seul cas (E3-07) la joue, pendant ≈ 3 min 30 s.

| Section | Cas | Contenu |
|---|---|---|
| D1 module | D1-01 à D1-15 | **témoin** : l'origine sur les valeurs de la fille rend 182 258,00 USD, code 3 ; l'écart rend 0,28 USD, code 0 ; téléchargement excessif (deux cas) ; seuil au centime (deux cas) ; champs absents, texte, négatif, booléen ; montée seule illisible, et **témoin** de l'origine qui la compte zéro ; réponse illisible ; arguments ; arbre syntaxique égal à l'origine hors `depense`, docstring et deux constantes |
| D1 surveillance | S1-01 à S1-05 | valeurs de la fille sur 23 relevés jusqu'à la fin normale, sans arrêt pour la dépense ; **témoin** : la surveillance d'origine arrête au premier relevé ; téléchargement excessif, arrêt DÉPENSE ; champs absents, majorant écrit, dépense antérieure comptée ; module d'écart absent, refus |
| D2 contrôle | C2-01 à C2-30, V01 à V05 | lignes à + 200 s (conforme à + 211 s), + 400 s (à + 421 s), + 890 s (à + 900 s), + 910 s (KO à + 900 s), jamais (KO à + 900 s) ; ligne d'échec à + 100 s (arrêt au premier relevé, + 181 s) ; fin de l'amorce à + 505 s (arrêt à + 511 s) ; démarrage lent ; état « exited » ; journal et état illisibles (passagers, puis permanents) ; retard sain et retard KO ; trop tôt ; les cas de l'origine repris (commit, tests, deux cartes, deux prix, machine, étiquette, carte relue, étiquette absente, redémarrage, arrêt en échec, identifiant autre, jeton masqué, quatre refus de départ) |
| D2 concordance | C2-X (10) | les lignes lues sont celles des vrais scripts de l'instance et de l'amorce à S, et dans l'ordre de la cause |
| D2 témoin | C2-T1, C2-T2 | le contrôle d'origine joué à + 290 s sur des lignes qui arrivent à + 410 s rend 3 KO et arrête l'instance (**défaut de R-2446 reproduit**) ; le contrôle d'écart rend conforme à + 410 s |
| D2 constantes | C2-K1, C2-K2 | `PRIX_MAX`, `DELAI_MIN_S`, `ECHEANCE_S`, `PAS_S` ; préambule et bloc d'arrêt égaux à l'origine, octet pour octet |
| D3 bout en bout | E3-01 à E3-07 | sain, horloge simulée : jeton depuis `_2`, contrôle à + 181 à 185 s, conforme, surveillance jusqu'à FIN, dépense antérieure de 0,53 passée, une création, un arrêt, ordre des appels ; échec d'amorce : contrôle en code 1, la surveillance suit et arrête ; lanceur en code 3 : ni contrôle ni surveillance ; pièce d'écart modifiée : aucun appel ; dépense antérieure illisible ; dossier existant ; **sain, horloge réelle** : contrôle appelé à + 181 s, conforme, surveillance jusqu'à FIN |
| R rejeux | R-01 à R-07 | voir le détail ci-dessous |

**Les rejeux (section R) :**
- R-01 : banc du module d'origine, 147 passés, égal au canonique.
- R-02 : banc du module **re-pointé** sur le module d'écart (copie à 2 lignes changées), 146 passés et 1 échec :
  **seul `test_depense_sain_sous_plafond`**, qui encode l'ancienne unité (20 × 0,026 = 0,52 USD) ; échec attendu.
- R-03 : banc de la surveillance d'origine, lignes de verdict égales au canonique.
- R-04 : banc de la surveillance **re-pointé** sur la surveillance d'écart (copie à 2 lignes changées), 0 non conforme,
  verdicts égaux.
- R-05 : huit fichiers d'origine égaux à S.
- R-06 : lanceur d'écart 1 inchangé.
- R-07 : épingles de v5 égales aux pièces.

**Copies jouées dans le bout en bout** (lignes changées comptées par le banc, comme aux essais de l'écart 1) :
- lanceur d'origine et lanceur d'écart 1 : 3 lignes (`DEPOT`, `DEPOT_URL`, `INTERVALLE_OFFRE_S`) ;
- enchaîneur v5 : 1 ligne, l'épingle du lanceur, devenue celle de sa copie jouée (`200c8ee9…`).

Les autres scripts sont des copies exactes. Le dépôt est synthétique ; le registre des GO est temporaire (en-tête et
ligne GO-2026-11-10-02 de `main`). Les contrôles avant dépense sont un bouchon. Entre deux cas, une destruction est
simulée : c'est le geste de la session, jamais celui de la chaîne.

**Mutations, hors journal versé, pour vérifier que le banc mord :**
- contrôle d'écart avec une échéance de 300 s : il rend le code 1 sur le cas de C2-03 ;
- module avec le relevé lu en octets : il rend le code 0 sur le cas de D1-03.

Le banc aurait déclaré l'un et l'autre non conformes.

**Reproductibilité.** Un premier passage complet (20:56:51Z → 21:02:22Z, non versé) et le passage final ne diffèrent
que par les heures et le commit factice.

**Sorties versées** (`sorties-essais-ecart2-v1/`) :
- contrôles C2-05, C2-08, C2-T1 et C2-T2 ;
- dépenses S1-01 et S1-02 ;
- journaux de l'enchaîneur E3-01, E3-02 et E3-07 ;
- sortie du banc du module re-pointé.

Aucune n'affiche de jeton factice (vérifié par recherche).

## Diff complet relu

Le diff est dans `diff-ecart2-contre-S-v1.txt`, sous la forme `diff -u` origine contre écart ; il a été relu en entier.

| Pièce | Lignes retirées | Lignes ajoutées | Blocs changés |
|---|---|---|---|
| module | 11 | 38 | en-tête, description de `depense`, deux constantes, fonction `depense` |
| surveillance | 3 | 16 | en-tête, usage, `VERIF_DEPENSE` et sa garde, appel de `depense` |
| contrôle | 56 | 163 | en-tête, usage, `DELAI_PREVU_S` remplacé par `ECHEANCE_S` et `PAS_S`, bloc du relevé devenu une boucle |

Dans le contrôle, l'évaluateur en Python (lancé par `python3 -I -`) réunit l'état et le journal. Les contrôles et les
messages de l'origine y sont gardés, et l'apostrophe est rendue.

L'enchaîneur v5 et le banc sont neufs, sans origine au dépôt.

## Lignes du texte scellé que l'écart touche (pour le rédacteur de l'addendum 2)

Texte : `prereg/P3-bis-temoin-positif-v1.md` (`76ab66ce…`). Le texte ne fixe nulle part la fenêtre de 180 à 300 s, qui
n'est que dans le script, ni l'enchaîneur.

| Lignes | Phrase (début) | Défaut | Ce qui change |
|---|---|---|---|
| 1948 | « Contrôle à cinq minutes en échec : arrêt de l'instance par son identifiant (R10), consigné. » | D2 | « en échec » se lit : signe d'échec à un relevé, ou ligne attendue absente à l'échéance (création + 900 s) ; contrôle d'écart |
| 1949-1950 | « Relance après une instance gardée ou arrêtée … contrôle à cinq minutes en échec … » | D2 | même lecture de « en échec » |
| 1962-1966 | « Dépense cumulée de la course … téléchargement relevé, majorant de 2,00 USD s'il est illisible » | D1 | relevé en Kio converti en Go avant le prix ; majorant ajouté pour chaque paire illisible |
| 2149-2150 | « … ou sur dépense cumulée ≥ 80 USD (prix de l'offre × durée depuis la création, plus disque et téléchargement relevés) » | D1 | téléchargement relevé selon la formule de l'écart ; surveillance d'écart |
| 2172-2183 (dont 2176-2177, 2180-2181, 2182-2183) | chaîne v2 citée par empreinte : `verifications_p3bis_v2.py`, `surveiller_p3bis_v2.sh`, `controle_cinq_minutes_p3bis_v2.sh` | D1, D2 | les originaux restent tels quels (égaux à S) ; les pièces jouées sont les pièces d'écart 2, citées par leur empreinte (comme l'addendum 1 pour le lanceur, l. 2174-2175) |
| 2264-2266 | écart 1 du lanceur : « … la dépense antérieure passée à la surveillance comprend toute dépense sous GO-2026-11-02-29 … » | D3 | v5 passe la dépense antérieure en argument (les v1 à v4 passaient 0) |
| 2273-2275 | écart 4 : « trois noms hors de la table commune … `controle_cinq_minutes_p3bis_v1.sh` … » | D2 | nom neuf `controle_cinq_minutes_p3bis_v2_ecart2_v1.sh` (nom « cinq minutes » gardé, échéance de quinze minutes) |
| 2276-2278 | écart 5 : « la surveillance arrête elle-même l'instance par son identifiant … » | D1 | inchangé sur le fond ; lu de la surveillance d'écart |
| 2279-2282 | écart 6 : « … téléchargement relevé par `inet_down_billed × inet_down_cost` (et la montée), majorant de 2,00 USD écrit s'il est illisible … » | D1 | **formule remplacée** : relevé × 1 024 / 10⁹ × prix au Go, par sens ; majorant par paire illisible |

Addendum 1 (`prereg/P3-bis-addendum-1-garde-credit-v1.md`, `4e188814…`) :
- l. 69 dit inchangés « le plafond de 80 USD de la dépense cumulée et sa surveillance » : le plafond reste inchangé,
  le calcul du téléchargement change ;
- l. 148 et l. 158, sur le contrôle à cinq minutes et la surveillance en aval du lanceur, restent vraies.

## Points ouverts

1. **Unité de `inet_*_billed`.**
   - Elle est **non documentée**. L'écart prend l'interprétation la plus prudente parmi les interprétations
     physiquement plausibles.
   - Elle peut être vérifiée a posteriori, sans dépense, par la session et non par le développeur : relever les charges
     de bande passante de 60370121 (page « Charges » ou factures de Vast). Si elles valent ≈ 0,17 à 0,19 USD,
     l'interprétation en kilo-octets est confirmée. Si elles valent environ mille fois plus, ce sont des Mo, et la garde
     d'origine avait raison.
   - Le prix de la montée de 60370121 n'est pas dans la note de la fille ; ≈ 0,04 USD/Go est déduit.
2. **Échéance de 900 s et illisibilités en attente** (D2, points 2 à 4 des affaiblissements). Ce sont des choix du
   développeur, avec une variante écrite pour chacun ; ils sont à juger par le contre-lecteur.
3. **Majorant par paire illisible** (D1). Le choix est séparable ; il est à juger par le contre-lecteur.
4. **Dépense antérieure** passée à v5 : à relever par la session au registre des dépenses, toutes tentatives comprises.
5. **Empreinte de v5** (`34131eaf…`) : à vérifier par la session avant le lancement. Son journal, son PID et les
   consoles sont dans le dossier neuf.
6. **Lignes d'information de `lancement.txt`** qui nomment le contrôle et la surveillance d'origine : elles sont à lire
   sous l'écart (addendum 2).
7. **Environnement d'essai.** Le banc du module d'origine exige pytest ; le `.venv` du dépôt n'en a pas à cette heure
   (il était en reconstruction selon R-2445). Un environnement neuf a été fait dans le bac à sable du développeur.
