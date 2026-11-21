# Rapport du développeur — véhicule NA-1, lot 2 (garde de motifs) — v3

- Développeur des lots 1 et 2 du véhicule NA-1, modèle O ; le même que pour la v1 et la v2.
- Date (UTC) : 2026-11-21 ; runs finaux lancés à 09:12:49Z (`date -u`).
- La v3 remplace la v2, vérifiée « Conforme » : `…/scratchpad/dev-vehicule-na-lots-1-2-v2/`, table `4ba408af…`, laissée en l'état. Le lot 1 n'entre dans la v3 que pour l'import de la garde.
- Objet : les décisions de la mère de 08:54Z, 08:55Z et 08:59Z, transmises par la coordination.
- Mêmes règles que pour la v1 et la v2 :
  - processeur seul ; aucun appel, aucune clé, aucune dépense ; aucune écriture dans un dépôt, aucun commit ;
  - données factices seules, plus les données d'Unicode, qui ne sont pas des données de course ;
  - aucune commande de liste hors de mon dossier, ni `git ls-tree`, ni `git show` d'un dossier ;
  - un seul `git fetch origin main`, comme demandé.
- Aucun refus de permission, de classifieur ni de garde rencontré.

## 1. Verdict

Les trois points tranchés sont portés.
- **Essais : 118 passés, 0 échec, 0 sauté** (lot 1 : 62 ; lot 2 : 56). Rejoués après application du paquet dans une copie neuve de l'orchestrateur : 118 passés.
- **Mutations : 98, toutes tuées** : 42 du développeur, 35 du vérificateur, 21 neuves. Le témoin non muté passe ; le témoin inerte survit.
- **Contrôle contre `regex` : 0 écart** sur 4 174 points.
- **Sous l'interpréteur de la course** (`/usr/local/bin/python3 -I`, Unicode 15.1.0, sans `regex`) : la garde et ses données se chargent, les huit formes demandées sont refusées et un texte sain passe.

## 2. Source et données des ignorables (voie (b), mère, 08:55Z et 08:59Z)

- **Source** : `docs/sources/unicode/15.1.0/DerivedCoreProperties.txt` sur `origin/main`, commit `bed42d477a4894f56f280ce188d66bec1ba37503`.
  - Tirée par `git show` redirigé vers `…/dev-vehicule-na-lot-2-v3/source-unicode-15.1.0/`, avec son compagnon.
  - Empreinte `f55d0db69123431a7317868725b1fcbf1eab6b265d756d1bd7f0f6d9f9ee108b`, égale au compagnon.
  - En-tête « DerivedCoreProperties-15.1.0.txt ; Date: 2023-08-07, 15:21:24 GMT ».
  - 29 lignes nomment la propriété : 27 lignes de données et 2 de commentaire. Total écrit par le fichier : 4 174.
  - C'est le seul fichier lu pour les plages.
- **Version de l'interpréteur de la course** : relevée par un programme sur disque, `sonde_versions_unicode_lot_2_v3.py`, joué sous `/usr/local/bin/python3 -I` : `unicodedata.unidata_version` = **15.1.0**, `regex` absent (journal `journal-sonde-interprete-course-lot-2-v3.json`).
- **Extraction** : `pole/extraire_ignorables_unicode_na_v1.py`. Le programme :
  - vérifie l'empreinte de la source ;
  - lit sa version dans la première ligne et refuse une autre que 15.1.0 ou que celle de l'interpréteur qui joue ;
  - prend les lignes dont le second champ est exactement la propriété, et refuse une plage non triée ou chevauchante ;
  - refuse si le compte des plages diffère du total écrit par le fichier ;
  - écrit sans écraser.
- **Données** : `pole/ignorables-unicode-15.1.0-na-v1.json`, `8e15ad688fbb298ade214fe19986e103e4302f0e67d169b7201f730e416699f7`. 27 plages, 4 174 points, version 15.1.0 ; la source y est citée par son chemin, son empreinte, son commit et son en-tête. Un essai rejoue l'extraction sur la source et retrouve le fichier à l'octet.
- **« Module de données »** : c'est un fichier JSON, non un module Python. Il est lu à son empreinte, comme la liste des motifs, et aucun code n'y est exécuté. La garde ne l'importe pas : elle le reçoit, ce qui permettra de changer de données sans réécrire la garde.
- **Contrôle contre `regex`**, là où il est présent (sous `.venv`) : `essais/controle_ignorables_regex_na_v3.py`. La comparaison porte sur les points communs, c'est-à-dire les points assignés en 15.1 selon `unicodedata` 15.1.0. Résultat : **0 écart sur les points communs, 0 ailleurs** ; données 4 174, `regex` 4 174 (journal `journal-controle-regex-na-lot-2-v3.json`). Un écart planté (U+034F retiré) est compté et nommé.
- **Égalité des versions** : `verifier_version_interprete` (`garde_motifs_na_v3.py:125`) est appelée :
  - au chargement des données, contre l'interpréteur qui joue ;
  - à la construction du normaliseur ;
  - par un essai, contre `/usr/local/bin/python3 -I` (`sonde_version_unicode_na_v3.py`).

  Une version différente est refusée. L'interpréteur de la course absent ferait échouer l'essai ; il ne serait pas sauté.
- Un fichier de données vide (source et plages nulles) est refusé au chargement, avec la cause « données vides ». Sans données acceptées, ni la liste ni la garde ne se construisent.

## 3. Les trois règles (code, `pole/garde_motifs_na_v3.py`)

1. **Caractère invisible** (`_retirer`, `:203`), appliqué avant et après la forme de compatibilité. Sont retirés :
   - la catégorie « Cf » ;
   - les 4 174 points « Default_Ignorable_Code_Point » des données (par propriété) ;
   - la **liste fermée d'apparence vide**, `APPARENCE_VIDE = (0x2800,)` (`:62`).

   **Écart franc à « par propriété », pour l'additif.** U+2800 (le braille vide, catégorie « So ») n'est ni « Cf », ni ignorable par défaut, ni une espace. Il s'affiche pourtant comme un blanc et coupe un motif sans le montrer, et aucune propriété d'Unicode ne le rassemble avec ses semblables. La raison est écrite dans le code. Tout ajout à la liste est une version neuve du programme. Un essai vérifie que chaque élément de la liste n'est ni « Cf », ni ignorable, ni une espace, sans quoi la liste serait sans objet pour lui.
2. **Une seule forme pour l'espace et le tiret** (`:214` à `:216`), après la forme de compatibilité et le repli de casse. Ces caractères deviennent une espace :
   - « tiret » : la catégorie **Pd** (le trait d'union-moins, le tiret, le tiret long et les autres), plus **U+2212**, le signe moins, gardé de la v2 ;
   - « soulignement » : la catégorie **Pc** ;
   - « espace » : tout ce que **`str.isspace()`** accepte, c'est-à-dire les catégories Zs (l'espace insécable comprise), Zl et Zp, la **tabulation**, les **fins de ligne** (LF, CR, VT, FF, NEL) et les séparateurs U+001C à U+001F. La tabulation et les fins de ligne deviennent donc une espace, pour qu'un motif coupé en fin de ligne morde quand même.

   Toute suite d'espaces devient ensuite une seule espace. La garde compare sur cette forme. **Les octets d'origine restent ceux qui partent** : l'empreinte et la taille journalisées portent sur eux, et un essai le vérifie sur une requête saine qui contient tirets, soulignement, espace insécable et tabulation.
3. **Le texte trouvé** ne va qu'à la ligne « non envoyé » du journal (`:408`), et à l'attribut `texte_trouve` de l'arrêt, jamais à son message ni à ses arguments. **Confirmé** ; inchangé depuis la v1 ; un essai le vérifie.

Conséquences pour la liste des motifs, écrites dans l'en-tête du module :
- un motif littéral vide ou blanc après normalisation est refusé ;
- une expression régulière s'applique à un texte sans tiret, sans soulignement, sans tabulation et sans fin de ligne. Une expression qui attendrait un de ces caractères ne mordrait plus sur son témoin positif, et le départ serait refusé.

**Changement d'interface.** La normalisation dépend désormais des données :
- `lire_liste_motifs(octets, empreinte, normaliseur)` et `charger_liste_motifs(chemin, empreinte, normaliseur)`, où `normaliseur = Normaliseur(charger_donnees_ignorables(chemin, empreinte))` ;
- `GardeMotifs(liste)` est inchangé ;
- la fonction de module `normaliser` n'existe plus ;
- le programme du tirage reçoit deux arguments sans défaut, `--donnees-ignorables` et `--empreinte-donnees-ignorables`, et l'empreinte des données va à son manifeste.

## 4. Essais demandés

- « graine-factice », « graine_factice », « graine factice » avec une espace insécable et « graine  factice » avec deux espaces : tous refusés comme « graine factice » (famille « composition et tenue », rang 1). Douze autres formes le sont aussi : tiret long, tiret demi-cadratin, signe moins, trait d'union, soulignements de la catégorie Pc, tabulation, LF, CRLF, U+2028, U+3000, et un mélange.
- Les quatre caractères du vérificateur (U+FE0F, U+034F, U+3164, U+2800), insérés dans le motif, n'empêchent plus le refus. Huit autres ignorables pris par propriété aussi, et quatre « Cf » qui ne sont pas des ignorables par défaut.
- Une requête saine passe, et ses octets sont inchangés.
- Chaque règle neuve a son cas sain et son artefact :
  - « graine.factice » et « grainefactice » passent ;
  - un ignorable dans un texte neutre ne fait pas refuser ;
  - la liste d'apparence vide ôtée, U+2800 reste dans le texte ;
  - données vides, d'une autre empreinte, d'une autre version, aux plages permutées ou répétées, au total faux ou à la source incomplète : refusées ;
  - extraction sur une source factice : cas sain, puis cinq refus (empreinte, version, total, ordre, en-tête) et une autre version d'interpréteur ;
  - versions d'Unicode différentes : refusées.

## 5. Mutations

`essais/mutations_na_v3.py` ; journal `journal-mutations-na-lot-2-v3.json`. **98 sur 98 tuées.**
- **Développeur, 42.** Huit sont adaptées au texte v3 et portent le suffixe « c » : la normalisation réécrite (L2-01c à L2-06c), le témoin positif (L2-09c), et l'empreinte de la liste, désormais vérifiée en deux lieux (L2-11c).
- **Vérificateur, 35.** Une seule est adaptée, X-35c : le signe moins est maintenant la constante `SIGNE_MOINS`.
- **Neuves, 21 (N3-01 à N3-21)**, chacune une garde retirée :
  - normalisation : ignorables, liste d'apparence vide, catégorie « Cf », catégorie Pc, catégorie Pd, réduction des suites d'espaces ;
  - données : données vides, version (deux lieux), égalité des versions, empreinte, ordre et chevauchement, total, normaliseur exigé, littéral blanc, type des données ;
  - extraction : version, total, filtre de la propriété, ordre, empreinte de la source ;
  - contrôle contre `regex` : écarts non comptés.

Une ébauche avait laissé survivre N3-11. L'essai plantait un chevauchement qui faussait aussi le total, et il passait par le refus du total. L'essai a été corrigé : deux plages permutées, puis une plage répétée avec le total recalculé. La version finale tue N3-11 ; l'ébauche de journal, hors de mon dossier, est retirée.

## 6. Ce que la lettre ne fixe pas (remarques ; rien n'est tranché ici)

1. **U+2800 est retiré, non ramené à une espace.** Inséré dans un mot, il ne le coupe donc plus. Mis à la place d'une espace (« graine⠀factice »), il colle les deux mots, et ce texte-là passe.
2. **Version d'Unicode de `regex`** : postérieure à 15.1 (22 995 points assignés de plus), mais non nommable. La comparaison est faite sur les points assignés en 15.1, et elle ne trouve aucun écart.
3. **Le signe moins U+2212** est gardé parmi les tirets (v2), hors de la catégorie Pd. C'est une exception nommée, à confirmer à l'additif avec la liste d'apparence vide.
4. **L'ordre des opérations** est de moi : retrait des invisibles, forme de compatibilité, repli de casse, forme de compatibilité de nouveau, retrait de nouveau, tirets et soulignements, espaces, suites d'espaces.
5. **Remarques des rapports v1 et v2** : elles tiennent, sauf celles que la mère vient de trancher (« espace et tiret », « caractère invisible »).

## 7. Interface pour les lots 3, 4 et 5

- Lire les données : `charger_donnees_ignorables(chemin, empreinte)`. Construire le normaliseur : `Normaliseur(donnees)`. Lire la liste : `charger_liste_motifs(chemin, empreinte, normaliseur)`. Construire la garde : `GardeMotifs(liste)`.
- Le reste est celui de la v2 : `garder_requete`, `garder_texte`, `examiner`, `envoyer_apres_garde`.
- Le lot 4 appelle `verifier_avant_envoi` sur les octets qu'il remet au noyau.
- Le lanceur (lot 8) épingle trois empreintes : celle du programme, celle de la liste et celle des données.

## 8. Livré

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-vehicule-na-lot-2-v3/`. Chaque fichier a son compagnon `.sha256`. La table d'empreintes du dossier est `table-empreintes-dossier-na-lot-2-v3.txt`.

| fichier | sha256 |
|---|---|
| `paquet/orchestrator/pole/garde_motifs_na_v3.py` | `cea1e69285af2356c9d3dc68e79c421d34fcadbfa585994b3763cb80e962dbc4` |
| `paquet/orchestrator/pole/extraire_ignorables_unicode_na_v1.py` | `bd39803b8ae64a4d628407a59db300751c4878af51040ff7858837cb4b10d3b7` |
| `paquet/orchestrator/pole/ignorables-unicode-15.1.0-na-v1.json` | `8e15ad688fbb298ade214fe19986e103e4302f0e67d169b7201f730e416699f7` |
| `paquet/orchestrator/pole/tirage_na_v3.py` (lot 1, import) | `5ec1bef8687e8de0f95cb5ad951c5a3a60003615e28c073baa993355ddcddcaf` |
| `paquet/orchestrator/pole/identifiants_na_v1.py` (inchangé) | `38d9860b7535e24b5ba707560f9dd5c4a27acc6e5632e453308a3fd2b93909dd` |
| `paquet/orchestrator/essais/aides_na_v3.py` | `b28c0bacbdd3175844643fc152687bb467a5214df67477baea1c4c46c0f8183e` |
| `paquet/orchestrator/essais/liste-motifs-essai-na-v1.json` (inchangé) | `41a50329f67c41d073115a75ae64981fd59a46b4663c269f42a32b4055c0508b` |
| `paquet/orchestrator/essais/controle_ignorables_regex_na_v3.py` | `d82bf76bcb1c387742b4ebe9d13d0130403a78b2634ec079650ce5d0f8ebc825` |
| `paquet/orchestrator/essais/sonde_version_unicode_na_v3.py` | `919767c9dcdbfe273fabeea79d1a05e465c5257bdc7c27975b272146fee3f50a` |
| `paquet/orchestrator/essais/sonde_chargement_course_na_v3.py` | `83651096fc3181ec5e227e32846c94c14fa3a24d0630781a0eabb4f37339ba79` |
| `paquet/orchestrator/essais/test_na_v3_tirage.py` | `b7fcd9731222cc202144b6fa29daaef9c7130b130da07876279e2c2069e03b66` |
| `paquet/orchestrator/essais/test_na_v3_garde_motifs.py` | `2346331b7cbdfaba61e46f71d351cc5bad0bb10047e318bda006dd7024a05a8b` |
| `paquet/orchestrator/essais/mutations_na_v3.py` | `d097a660f85659b4f63377fb693595378d0358330c8b869d7c700cdf1f04b5b2` |

Le manifeste, le programme d'application, les journaux (essais, mutations, contrôle contre `regex`, chargement sous l'interpréteur de la course, sondes de version) et la source tirée de `origin/main` sont à la table d'empreintes.

— développeur des lots 1 et 2 du véhicule NA-1, modèle O
