# Contre-lecture du code v4 de B bis, tour 1 (lecteur C, neuf)

- Lecteur : contre-lecteur neuf (R2), lettre de modèle C ; n'a écrit aucun fichier de B bis, ni aucun brouillon de l'addendum ;
  lecteur déclaré de T0.7 (exclu des lecteurs de P3-bis).
- Date (UTC, `date -u`) : de 2026-11-17T02:48:43Z à 2026-11-17T03:11:34Z (la seconde au scellement).
- Textes de référence (empreintes recalculées) : second addendum `prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md`
  `18baeac32d26ebf174c62d7a36caedeee1d5b80648c6743c21dc30d2747afd26` ; premier addendum
  `prereg/T0.7-etape-B-bis-v1-addendum-ecart-v1.md` `f00eda8a9fb74516289a085350425d128bf5b1cf1dbc50eee32d8bbe749c78d7` ; texte scellé
  `prereg/T0.7-etape-B-bis-v1.md` `0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb`.
- Pièces lues (dossier `brouillons/T0.7-etape-B-bis-v1/second-addendum-v2/`, empreintes recalculées, les neuf compagnons
  `.sha256` du dossier `code/` vérifiés conformes) :
  1. `code/src/controle_ia/t07bbis/validation_imbriquee_v4.py` — `3d40ebc80e2bbf7faf33bfe8a4ef6e7d8f26df9df93507ad79a85d4c766d2c6c`
  2. `code/src/controle_ia/t07bbis/marche_v4.py` — `c63f778055895c545922de0b3ea232c6318fc8f54cf0917ce099cb3acdd27d23`
  3. `code/src/controle_ia/t07bbis/lecture_v3.py` — `c9a478437f32465418dfafdadbd7823f88853a9c17f77a0e59cc4ccb5ccff6ec`
  4. `code/src/controle_ia/t07bbis/registre_bbis_v2.py` — `b464d4426bae48ddbbb3f9afb466cdf012c503c06caf464374f44f890daad9f0`
  5. `code/scripts/lancer_bbis_v4.sh` — `457457c0e9d32a1c5d03765b03a8ab63a69cdbc2a5147d534d0889d5a159062a`
  6. `code/scripts/amorce_bbis_v4.sh` — `099a5c0e5d504b43b68140da86b4d69d91ea42d1725e2dddca0fad2750764277`
  7. `code/tests/test_t07bbis_second_addendum_v1.py` — `df7f72871710f8aa812ca9a25e998dd8ebbcc62c9a941f11a834dd4cfc81be21`
  8. `code/tests/aide_t07bbis_differentiels_v4.py` — `8fc12d591d9af89602d04da1d594c89402d9dc82b2a3086a0d30ae66e6f90ce0`
  9. `code/tests/aide_t07bbis_jeux_v4.py` — `55adcd7a31ce9405c40d7b7b9c95a327bfa446bace3c8c4309999b00df61c181`
  10. `diff-v3-v4.txt` (à la racine du dossier, non sous `code/`) — `610c5c6985d3fa0c84245a84368e7f9954d2284d5a8add85d52e2751f89f852c`
- Portée de la lecture, dite telle quelle : lus en entier, ligne par ligne : `validation_imbriquee_v4.py`, `marche_v4.py`,
  `registre_bbis_v2.py`, `amorce_bbis_v4.sh` (à partir de la ligne 24 ; les lignes 1 à 23 par le différentiel),
  `aide_t07bbis_jeux_v4.py`, `test_t07bbis_second_addendum_v1.py`, et les lignes 552 à 1218 du différentiel. `lecture_v3.py`
  (1 464 lignes) : **tout ce qui change** depuis `lecture_v2` (le différentiel entier, que j'ai recalculé moi-même, § 5) et les
  fonctions qui portent ces changements (lignes 186 à 236, 800 à 934, 1022 à 1048, 1222 à 1376) ; le reste du fichier est celui
  de `lecture_v2`, égal ligne à ligne (prouvé par le différentiel recalculé), non relu ici. `lancer_bbis_v4.sh` : les lignes 28 à
  84 et 110 à 124, le reste par le différentiel. `aide_t07bbis_differentiels_v4.py` (table de couples) : en-tête et structure
  seulement ; son contenu est contrôlé par l'essai A et par mon différentiel recalculé.
- Références lues pour comparer (code des versions précédentes, commit `af0adb14` de la branche `prep/t07bbis-code-v1`) :
  `validation_imbriquee_v1.py`, `validation_imbriquee_v3.py`, `apprentissage_carte_v1.py`, `conjointe_v1.py` (lignes 140 à 213),
  `lecture_v1.py` (`lire_lignes`), `commun_v1.py` (extraits), `plis_v1.py` (classe `Jeu`), `sondes/familles.py` (lignes de refus),
  `gardes.py`, `tests/aide_t07bbis_jouet_v1.py` (`disponible`) ; `registres/t07-etape-b-bis-v1.md` (quatre lignes) ;
  `registres/t07-etape-b-bis/code-bbis-v1.json` (noms des clés et liste des fichiers ; la valeur de l'entropie non affichée) ;
  `rapport-second-addendum-bbis-v1.md` (§ 1 à § 7) ; `essais/sortie-suite-forme-instance-v1.txt` et
  `essais/sortie-sonde-jeux-divergents-v1.txt`.

## 1. Verdict

**Scellable avec corrections : 1 majeur, 6 mineurs.**

- Le code v4 **fait ce que le second addendum écrit** sur les sept points demandés (contrôle à 3 époques dans les deux familles,
  déterminisme à 300 époques, information à 300 époques sans arrêt, mesure de dispersion sans aucune issue, R-PILE étendue à la
  linéaire, `version_controle` « v4 », ligne `CODE-BBIS` remplacée une seule fois). Aucun écart silencieux trouvé dans les neuf
  fichiers. Les 34 essais passent (§ 4). Le différentiel fourni est exact (§ 5).
- **Majeur M1 (hors des neuf fichiers, mais créé par eux)** : la table conjointe (`conjointe_v1.gardes_conjointe`) lit le
  registre propre par `lecture_v1.lire_lignes`, qui **refuse** une ligne `CODE-BBIS` en double. Dès que la seconde ligne
  `CODE-BBIS` sera écrite, la table conjointe du plan (point 11, ligne `CONJOINTE-BBIS`, inchangée selon le § 5 du second
  addendum) ne pourra plus être calculée par le code cité. Éprouvé sur un registre fabriqué (§ 3.8). Le paquet v4 a corrigé la
  marche, la lecture et les gardes de registre, pas la table conjointe. Comme la ligne `CODE-BBIS` ne se remplace qu'une fois
  (« jamais une troisième », SA-5), **le module corrigé doit entrer dans la fiche remplaçante avant qu'elle soit écrite**.
  M1 ne touche ni la course, ni la lecture, ni le verdict ; il n'exige de changer aucun des neuf fichiers (un dixième fichier, à
  nom neuf, et son essai).
- Les six mineurs (§ 8) ne changent aucun résultat ; deux d'entre eux (m1, m2-m3) protègent la course unique contre une perte
  évitable et je recommande de les appliquer avant le feu ; la décision est à la mère.

## 2. Cohérence avec le texte

| écart | ce que dit le texte | ce que fait le code | constat |
|---|---|---|---|
| SA-1 | couple tiré à la fin, parmi les sondes finales finies, graine `bbis/egalite-carte`, ordre trié ; aucun : arrêt | `validation_imbriquee_v4.ControleCarte.jouer` : corps égal à celui de la v3, hors la docstring (comparé par programme : 2 lignes de docstring diffèrent, rien d'autre) ; appelle bien `controle_deux_horizons` de la v4 | conforme |
| SA-1 | deux familles (variante (r1) : la linéaire seule), 3 époques carte contre processeur, 256 actions, ≤ 10⁻⁴, sinon arrêt | `controle_deux_horizons`, boucle sur `ORDRE` restreint aux familles de la marche ; `EPOQUES_CONTROLE = 3` ; `ac.controle_carte_processeur(..., epoques=3)` avec `TOLERANCE_CARTE` ; même graine que la marche (`bbis/entrainement/sonde/<cellule>/e<k>/<réglage>`) | conforme |
| SA-1 | sonde de 300 époques de chaque famille réapprise une seconde fois sur la carte, égale au bit près, sinon arrêt ; sonde finale du couple réemployée si sa famille est retenue | `sondes_300={reglage["famille"]: res["sonde"]}` ; `egales_au_bit(a, b)` (w, b, q) pour chaque famille | conforme |
| SA-1 | écart de la linéaire à 300 époques calculé et écrit, sans arrêt | `informer_300` : `tolerance=inf`, champ `ecart_300_information` avec `decide: False` ; écart non fini écrit sous `refus`, sans arrêt | conforme |
| SA-1 | sonde de contrôle en échec, à 3 ou à 300 époques, déterminisme compris : arrêt | trois `except ac.SondeEnEchec` qui relèvent `GardeArret` « erreur de chaîne » | conforme |
| SA-1 | après le contrôle, la mesure, puis les fichiers fermés ; aucun contrôle après un arrêt de débit | `marche_v4._apres_manifeste` : boucle, `controle.jouer`, `mesurer_dispersion`, `ecrire_fermes` ; retour avant le contrôle sur `ArretDebit` | conforme |
| SA-1 | les apprentissages de la mesure sont des « apprentissages restants » | `total = apprentissages_prevus(...) + apprentissages_mesure(...)` ; 5 × 2 × (18 × 4 + 1) = 730 (vérifié) | conforme |
| SA-2 | R-PILE écrite dès qu'une sonde finale est lue, linéaire ou « attention », source ou ENC ; phrase gelée ; sondes par famille ; résumé de la mesure (quatre formes) | `lecture_v3.reserve_pile`, `phrase_dispersion` ; phrase de `RESERVES_FIXES["R-PILE"]` **présente au caractère** dans le « nouveau » de SA-2 (contrôlé par programme sur le texte scellé) | conforme |
| SA-3 | point (7) réécrit | `SECTION_D` : fragment de SA-3, gras retiré, présent au caractère (contrôlé par programme) | conforme |
| SA-4 | liste d'arrêt | mêmes arrêts que SA-1 | conforme |
| SA-5, SA-11 | seconde ligne `CODE-BBIS` après `GO-BBIS`, strictement postérieure, qui fait foi ; jamais une troisième | `lecture_v3.lire_lignes` (`remplacables`), `exiger_ordre_propre` (SCELLEMENT < CODE première < GO < CODE remplacement < SCORES), `registre_bbis_v2.ajouter_ligne_propre` | conforme à la lecture ; à l'écriture, l'ordre des instants n'est pas vérifié (mineur m3) |
| SA-6 à SA-8 | noms neufs, marche v4 appelle la validation v4, gardes de registre v2, branche de sortie v2 | vérifié ; `BR_SORTIE=donnees/t07-etape-b-bis-v2` ; aucun des neuf noms n'existe au commit `af0adb14` | conforme |
| SA-9 | liste des épreuves | chaque épreuve nommée a son essai (B1 à B8, C1, C2, D1, D2, E1 à E5, F) ; le tirage du couple n'a pas d'essai propre à la classe v4 (mineur m6) | conforme, une réserve |
| SA-10 | recette entière rejouée, ordre inverse des actions de chaque lot d'apprentissage, mêmes clés de graines ; ni ENC, ni plancher, ni nul | `apprendre_recette_ordre2` : copie de `validation_imbriquee_v1.apprendre_recette` comparée ligne à ligne ; seules différences : `[::-1]` sur les actions d'apprentissage (plis internes et sonde finale), noms des sondes (« -ordre2- »), valeurs rendues ; clés de graines identiques | conforme |
| SA-10 | scores et poids dans les fichiers fermés, réglage et empreinte dans le fichier des sondes, aucune aire écrite | tableaux `<groupe>__sonde_o2`, `o2__w`, `o2__b`, `o2__q` ; `meta["ordre2"]` ; `del aires, sommes` ; `_sans_aire` joué sur le document | conforme |
| SA-10 | sonde de l'ordre 2 en échec : source « échec », sans arrêt | `"echec" in o2` : motif dans `meta["ordre2"]`, résumé « échec » | conforme |
| SA-10 | erreur d'exécution qui n'est pas une garde : mesure « non faite », tableaux partiels retirés, la marche continue | `except RuntimeError` (hors `GardeArret`), `_retirer_mesure`, résumé `non_faite` | conforme pour `RuntimeError` ; toute autre erreur arrête la marche (mineur m1) |
| SA-10 | une garde arrête la marche | `GardeArret` relevée | conforme |
| SA-10 | à la lecture : A₁, A₂, Δ, aires par pli, réglages des deux ordres, résumé ; aucun intervalle, aucun seuil, aucun état | `lecture_v3.dispersion_ordres` : jeu « O[positifs] contre O[H] », ligne 0 (la sonde), moyenne des deux plis ; aucun tirage, aucune graine consommée ; appelée **après** `issue_complete` ; ne touche que `res["dispersion_ordres_calcul"]` et la phrase de R-PILE | conforme |
| SA-12, SA-13, SA-17 à SA-19 | sorties de la marche | `ecrire_fermes` écrit les tableaux de l'ordre 2 dans `scores-bbis-NNN.npz`, `ordre2` et `dispersion_ordres_calcul` dans `sondes-bbis.json` | conforme |
| SA-14 | dispersion après toutes les cellules | ordre de `lire` vérifié | conforme |
| SA-15 | une course de plus, une seule : compteur à 2, feu portant GO-2026-11-16-11, `CODE-BBIS` remplacée ; limite du 21 novembre pour toute relance | `registre_bbis_v2.exiger_creation` | conforme ; la garde ne lie pas « `CODE-BBIS` remplacée » à « compteur à 2 » dans l'autre sens (mineur m2) |
| SA-16 | branche `donnees/t07-etape-b-bis-v2` | amorce v4 | conforme |
| SA-20 | course sous GO-2026-11-14-09 | `GO_ATTENDU` et `GO_ID` inchangés | conforme |
| SA-21 à SA-25 | paragraphes du premier addendum | texte seulement ; le coût décrit par SA-21 est celui du code (par famille : une sonde de 3 époques et au plus deux de 300 sur la carte ; une de 3 sur le processeur ; une linéaire de 300 pour l'information) | conforme |
| § 4 | discriminant à double sens | `lecture_v3.DISCRIMINANT` : « accord » si l'information est finie et ≤ 10⁻⁴, « écart » sinon (non finie comprise) ; aucun effet sur un état | conforme |
| § 7 | le code cite le texte scellé et lui seul ; l'addendum ne monte pas sur l'instance | `TEXTE_SHA256` inchangé ; motif `/prereg/T0.7-etape-B-bis-v1.md*` de l'amorce ne retient pas les addenda | conforme |

## 3. Vérifications techniques

1. **Contrôle à 3 époques, deux familles.** Fait pour la linéaire et pour l'attention (boucle unique, `ec = 3`), contre
   `sondes.familles` à 3 époques, tolérance 10⁻⁴. Sous la variante (r1), la linéaire seule. Horizon refusé hors de [1, 300[.
2. **Déterminisme à 300 époques.** Joué **sur la carte seulement** (`ac.entrainer` deux fois sur le même lot), pour chaque
   famille, égalité au bit près de w, b, q. Le processeur n'y entre pas.
3. **Information à 300 époques.** Linéaire seulement, écrite, jamais décisive ; la lecture refuse le champ s'il est absent ou
   mal formé, et n'en tire que la phrase du discriminant.
4. **Mesure de dispersion.** Information seulement, des deux côtés : sur l'instance elle n'écrit que des scores et des
   poids ; à la lecture elle est calculée après l'issue et ne change aucune cellule (lu au code ; aucun essai ne compare les
   états avec et sans la mesure, mineur m6). Erreur `RuntimeError` : « non faite », rien de partiel (essai E3, et ma
   démonstration ci-dessous).
5. **R-PILE étendue à la linéaire.** Écrite dès qu'une sonde finale est lue, sans décider de rien ; elle porte le résumé.
6. **`version_controle`.** « v4 » écrit par `controle_deux_horizons`, exigé par `lecture_v3.exiger_controle_carte` (un fichier
   de la marche v3 est refusé).
7. **Invariant N-053, point 5.** Aucun entraînement d'agent dans ces fichiers : aucun optimiseur, aucun adaptateur appris,
   aucun gradient vers le modèle (recherche par motif : rien hors des phrases de la lecture). Les seuls apprentissages sont ceux
   des sondes, sur des activations relues d'un modèle figé. Aucun score de sonde n'entre dans un entraînement d'agent.
   Aucune moyenne ni médiane sur les jetons (la médiane de la garde de débit porte sur des durées).
8. **Démonstrations de ma main** (données fabriquées, processeur, copie du bloc-notes ; aucune donnée de course) :
   - registre propre fabriqué à deux lignes `CODE-BBIS` : `lecture_v3.lire_lignes` le lit (la seconde fait foi),
     `exiger_ordre_propre` passe ; `lecture_v1.lire_lignes` : « ligne CODE-BBIS en double ou mal formée » ;
     `conjointe_v1.gardes_conjointe` : « table conjointe refusée : ligne CODE-BBIS en double ou mal formée » (**M1**) ;
   - erreurs simulées dans `mesurer_dispersion` : `RuntimeError` → « non faite », tableaux partiels retirés ; `MemoryError`,
     `OSError`, `ValueError` → l'erreur sort, donc arrêt écrit de la marche sans aucun score (**m1**) ; `GardeArret` → sort
     (voulu par le texte).
9. **Lecture de la mesure quand le champ manque.** `dispersion_ordres` rend « non faite (champ absent) » ; la forme « non lue »
   de SA-2 n'est atteinte que si la fonction n'est pas appelée. Sans effet.

## 4. Essais

- **Commande demandée, jouée telle quelle sur `main`** : `PYTHONPATH=src .venv/bin/python -m pytest
  brouillons/T0.7-etape-B-bis-v1/second-addendum-v2/code/tests/ -q --tb=short` → **1 erreur à la collecte, 0 essai joué** :
  `ModuleNotFoundError: No module named 'controle_ia.t07bbis'`. Cause : le paquet `t07bbis` (v1 à v3) n'est pas sur `main` ; il
  vit sur la branche `prep/t07bbis-code-v1` (commit `af0adb14`). Ce n'est pas un défaut du code v4.
- **Passe qui compte** : copie au bloc-notes (`git archive` de `af0adb14`, sans `diag/`, `runs/`, `donnees/`, plus le dossier
  `code/` posé par-dessus, comme l'ont fait le rédacteur et les lecteurs du texte), environnement Python du dépôt (torch 2.14.1),
  4 fils, machine chargée par d'autres calculs : **34 passés, 0 échec, 0 sauté, en 874,61 s** (14 min 34 s), code 0. L'essai F
  (bout en bout) y est joué et passe, parce que la copie porte `docs/notes` ; sur l'instance il saute (33 passés).
- **Robustesse des essais de divergence** (B1, B2, B3 affirment qu'une amplification d'arrondi a lieu ; ils sont une porte de
  l'amorce, étape 5). Rejoués sous deux autres jeux d'instructions du processeur : 4 passés à chaque fois ; information à 300
  époques : quasi-copies 5,037 et 5,034 (5,307 chez le rédacteur), anisotrope 3,667 et 3,222 (3,793) ; à 3 époques : linéaire
  9,2·10⁻¹² et 3,1·10⁻¹² (inchangées), attention 8,8·10⁻¹⁰ et 1,1·10⁻⁹. La divergence tient donc au jeu de données, non à une
  réalisation d'arrondi, sur cette machine. Non prouvé sur le processeur de l'hôte loué (mineur m5).
- **Syntaxe des deux scripts** : `bash -n` conforme.

## 5. Diff v3→v4

Le fichier `diff-v3-v4.txt` est **exact** : j'ai recalculé les sept différentiels (`diff -u`) entre les fichiers du commit
`af0adb14` (ou la proposition du diagnostic) et ceux du dossier `code/` ; hors lignes d'en-tête, les 1 181 lignes sont égales à
celles du fichier fourni ; les sept empreintes « a » et « b » qu'il annonce sont celles que je recalcule (dont `71bffa5b…` pour
`validation_imbriquee_v3`, citée par le premier addendum).

| bloc | changement | rattachement |
|---|---|---|
| proposition du diagnostic → `validation_imbriquee_v4` | docstring ; mesure de dispersion ajoutée (`apprentissages_mesure`, `apprendre_recette_ordre2`, `_retirer_mesure`, `mesurer_dispersion`) ; `ecart_300_information` gardé | SA-1, SA-6, SA-10 |
| `validation_imbriquee_v3` → v4 (lecture seulement) | contrôle réécrit : un horizon de 3 époques pour les deux familles, déterminisme des deux, information ; `version_controle` | SA-1, SA-4, SA-6 |
| `marche_v3` → `marche_v4` | docstring ; lecture du registre par `lecture_v3` avec `remplacables` ; nom de la commande au manifeste ; import de la validation v4 ; total de la garde de débit ; appel de la mesure ; champ `dispersion_ordres_calcul` | SA-5, SA-8, SA-1 (apprentissages restants), SA-10, SA-18 |
| `lecture_v2` → `lecture_v3` | docstring ; phrase de R-PILE ; point (7) ; `NOMS_FAMILLES`, `EPOQUES_CONTROLE_V4`, `CHAMP_O2`, `DISCRIMINANT` ; `phrase_dispersion` ; `reserve_pile` ; `exiger_controle_carte` ; `REMPLACABLES_PROPRES`, `lire_lignes`, `exiger_ordre_propre` ; `dispersion_ordres` ; trois appels ; nom de la commande | SA-2, SA-3, SA-7, § 4, SA-5, SA-11, SA-10, SA-14 |
| `registre_bbis_v1` → `registre_bbis_v2` | docstring ; `GO_ACCORD` ; seconde ligne `CODE-BBIS` permise ; fiche lue par `lecture_v3` ; garde de création à 2 relances ; limite du 21 novembre pour toute relance | SA-5, SA-15 |
| `lancer_bbis_v3` → v4 | commentaires ; `registre_bbis_v2` ; amorce v4 (sept occurrences) | SA-8 |
| `amorce_bbis_v3` → v4 | commentaires ; `marche_v4` ; `BR_SORTIE` ; deux motifs d'extraction ; `MIN_ESSAIS=148` | SA-8, SA-16 ; `MIN_ESSAIS` : rapport du rédacteur, § 3 (hors du texte, déclaré) |

Aucun bloc sans rattachement. Deux remarques : le différentiel ne couvre pas les aides d'essais (fichiers neufs) ;
`MIN_ESSAIS` n'est fixé par aucun fragment du texte (c'est une garde de l'amorce, non un critère).

## 6. Sécurité et interdits

- **Aucun identifiant de modèle** dans les neuf fichiers ni dans le différentiel (recherche sans casse des noms de lignées
  et de fournisseurs : zéro occurrence).
- **Aucune valeur de clé.** L'amorce lit `GH_TOKEN`, `HF_TOKEN`, `CONTAINER_API_KEY` par leur nom, ne les affiche jamais ; le
  lanceur imprime `$HF_TOKEN` et `$GH_TOKEN` non développés.
- **Réseau.** Aucun dans les quatre modules Python ni dans les essais. Dans les scripts, ce que la v3 faisait déjà et rien
  d'autre : l'amorce (sur l'instance) clone et pousse vers `https://github.com/lciric/controle-ia-travail.git` — le dépôt de
  travail, jamais la copie publique —, installe les paquets, descend le modèle, et demande l'arrêt ou la destruction de **sa**
  seule instance par son identifiant (R10) ; le lanceur ne fait que `git ls-remote` (lecture seule) et, pour
  `verifier-destruction`, `vastai show instances` (lecture seule) ; il **imprime** les commandes de création et de
  destruction, la mère les joue.
- **Lectures de fichiers.** La marche lit les entrées de 7b nommées par le texte et refuse la liste « Jamais »
  (`lecture-sondes-t06.json`, `resume.json`) ; l'amorce exclut ces chemins de l'extraction et s'arrête s'ils sont présents ;
  la lecture passe toujours par `GardeEntrees`. Inchangé depuis la v3.
- **Interdits de ma lecture.** Je n'ai ouvert aucun fichier sous `diag/`, `runs/`, `donnees/`, ni `lecture-sondes-t06.json`,
  ni aucun fichier de 7a ou de 7b, ni aucun résultat de course (un incident de copie, § 9, sans ouverture).

## 7. Corrections exigées

1. **M1 — table conjointe lisible avec `CODE-BBIS` remplacée.** Fichier neuf `src/controle_ia/t07bbis/conjointe_v2.py` (R12 ;
   `conjointe_v1.py` reste), égal à `conjointe_v1.py` plus les couples ci-dessous, avec un essai (cas sain : registre à deux
   lignes `CODE-BBIS`, la garde passe ; artefact : trois lignes, ou seconde ligne non postérieure, refus) et sa ligne dans
   l'aide aux différentiels ; le fichier et son essai entrent dans la fiche remplaçante de `CODE-BBIS`. À faire **avant** la
   seconde ligne `CODE-BBIS`.

   Ancien (dans `gardes_conjointe`, une occurrence) :
   ```text
       from .lecture_v1 import CLES_PROPRES, RefusLecture, lire_lignes
       from .registre_bbis_v1 import REGISTRE_PROPRE
       racine = Path(racine)
       try:
           propres = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, ("VERDICT-BBIS", "LECTURE-BBIS"), propre=True)
   ```
   Nouveau :
   ```text
       from .lecture_v3 import CLES_PROPRES, REMPLACABLES_PROPRES, RefusLecture, lire_lignes
       from .registre_bbis_v1 import REGISTRE_PROPRE
       racine = Path(racine)
       try:
           propres = lire_lignes(racine / REGISTRE_PROPRE, CLES_PROPRES, ("VERDICT-BBIS", "LECTURE-BBIS"), propre=True,
                                 remplacables=REMPLACABLES_PROPRES)
   ```
   Ancien (dans `main`, une occurrence) : `commande="python -m controle_ia.t07bbis.conjointe_v1"` ; nouveau :
   `commande="python -m controle_ia.t07bbis.conjointe_v2"` ; plus la docstring du module et celle de `main` (nom du module).
   Rien d'autre ne change dans la table (lignes C0 à C6, phrases, états). Le plan (point 11) nomme le script de la table ; le
   nom neuf est un écart de nom à déclarer par la mère, de la même forme que `registre_bbis_v2`.

Aucune autre correction n'est exigée.

## 8. Remarques facultatives

- **m1 — la mesure, information seulement, peut coûter la course.** `mesurer_dispersion` n'attrape que `RuntimeError`. Une
  erreur d'une autre classe pendant la mesure (mémoire vive de l'hôte, lecture d'une activation sur le disque, forme d'un
  tableau) sort de la fonction et devient un arrêt écrit de la marche, **sans aucun score**, alors que les dix sources sont
  apprises et le contrôle passé. Le texte dit « erreur d'exécution qui n'est pas une garde (mémoire de la carte, erreur de
  torch) » ; le code en retient la lecture étroite (la classe `RuntimeError`), déclarée dans sa docstring, non au texte. Le
  risque est faible (la mesure rejoue des chemins que la marche vient de jouer dix fois), le prix est la course unique.
  Recommandé avant le feu, à trancher par la mère (la correction change l'empreinte du module, donc sa contre-lecture sur ce
  seul couple). Ancien : `    except RuntimeError as e:` suivi de `        if isinstance(e, GardeArret):` … `            raise` ;
  nouveau : `    except GardeArret:` / `        raise` / `    except Exception as e:` ; essai E3 étendu à `MemoryError` et `OSError`.
- **m2 — garde de création.** `exiger_creation` exige le feu portant GO-2026-11-16-11 et `CODE-BBIS` remplacée **si** le
  compteur vaut 2 ; elle ne refuse pas un compteur à 0 ou 1 quand `CODE-BBIS` est déjà remplacée. Une course v4 commandée avec
  un compteur mal compté passerait donc sans GO-2026-11-16-11 dans le feu. Recommandé : refuser tout compteur autre que 2 dès
  que le registre porte deux lignes `CODE-BBIS`.
- **m3 — ordre des instants à l'écriture et à l'entrée de la marche.** `ajouter_ligne_propre` permet la seconde ligne
  `CODE-BBIS` si `GO-BBIS` est présente et `SCORES-BBIS` absente, sans vérifier que son instant est strictement postérieur à la
  première ligne et à `GO-BBIS`. `marche_v4.gardes_d_entree` n'appelle pas `exiger_ordre_propre`. Une seconde ligne mal datée
  (jamais réécrite, jamais remplacée) laisserait donc partir la course, que la lecture refuserait ensuite. Recommandé :
  vérifier les instants à l'écriture, et appeler `exiger_ordre_propre` dans les gardes d'entrée de la marche. À défaut : la mère
  joue `lecture_v3.lire_lignes` et `exiger_ordre_propre` sur le registre réel juste après avoir écrit la ligne, avant le feu.
- **m4 — renvois et mentions périmés (aucun effet).** `validation_imbriquee_v4`, docstring : l'empreinte `ba127aa0…` est
  attribuée au rapport du diagnostic ; c'est celle de la proposition `validation_imbriquee_v4.py` du diagnostic (le rapport est
  `1fefa0a9…`). Trois docstrings citent `brouillon-second-addendum-bbis-v1.md` au lieu du texte scellé
  `prereg/T0.7-etape-B-bis-v1-addendum-ecart-2-v1.md`. Restes de la v3 : `lecture_v3`, message « (impossible en marche v3) » ;
  `marche_v4`, docstring de `entrees_locales` (« `amorce_bbis_v3.sh` ») et étape 3 (« `validation_imbriquee_v3.apprendre_source` ») ;
  `registre_bbis_v2`, puce « une relance au plus » de la docstring.
- **m5 — porte des essais sur l'instance.** `MIN_ESSAIS=148` = 115 (compte de la v3 sur l'instance) + 33, **sans aucune marge** ;
  le rédacteur déclare qu'il reste à recompter sur l'arbre de l'instance simulé par les motifs de l'amorce v4 ; je ne l'ai pas
  recompté (la suite entière n'a pas été rejouée ici). Les essais B1 à B3 affirment une divergence à 300 époques : stable ici
  sous trois jeux d'instructions (§ 4), non éprouvée sur le processeur de l'hôte ; un échec à l'étape 5 arrêterait l'instance
  avant la marche. Si la mère ajoute `conjointe_v2` et son essai, le compte monte ; `MIN_ESSAIS` est un plancher et peut rester.
- **m6 — essais absents (R5), sans défaut trouvé.** Le tirage du couple par la classe v4 n'a d'essai que par la v3 (corps égal,
  vérifié par programme) et par l'essai F, qui saute sur l'instance ; la branche « information non finie, écrite sous `refus` »
  n'est éprouvée que du côté de la lecture ; aucun essai ne compare les états d'une lecture avec et sans la mesure ; l'essai E3
  ne simule que `RuntimeError`.

Points pour la mère, hors du code : (a) la commande d'essais de la mission ne peut pas tourner sur `main` ; (b) la fiche
remplaçante doit lister les neuf fichiers, plus `conjointe_v2` et son essai si M1 est appliqué ; (c) la contre-lecture porte sur
les empreintes du haut de ce rapport : tout fichier changé ensuite est à relire sur son seul différentiel.

## 9. Incidents de ma main

- **Fichiers modifiés** : aucun fichier existant. Fichier créé : ce rapport et son compagnon `.sha256`.
- **Commits** : aucun. **Appels payants, machines, réseau** : aucun.
- **Copie au bloc-notes** : ma première extraction (`git archive` de `af0adb14`) a posé dans le bloc-notes les dossiers
  `diag/`, `runs/` et `donnees/` de ce commit malgré mon filtre ; je les ai supprimés aussitôt **sans ouvrir aucun fichier**
  (seul un compte de fichiers a été fait, aucun nom ni contenu affiché) ; les essais ont tourné sans eux.
- **Commande d'essais** : la commande de la mission a échoué à la collecte (§ 4) ; la passe a été jouée dans la copie.
- **Lectures hors de la liste de la mission**, pour comparer : les modules des versions précédentes dans l'arbre de travail
  de la branche `prep/t07bbis-code-v1` et par `git show af0adb14:…`, le registre propre, la fiche `code-bbis-v1.json` (clés et
  liste de fichiers), le rapport du rédacteur et deux sorties d'essais du dossier `essais/` (liste en tête).
- **Pièces de ma main au bloc-notes** (non durables, non versées) : deux programmes de démonstration (§ 3.8), un programme de
  contrôle des phrases gelées, mes différentiels recalculés, les sorties d'essais.
