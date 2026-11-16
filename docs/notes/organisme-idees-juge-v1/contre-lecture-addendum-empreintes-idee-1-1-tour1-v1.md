# Contre-lecture, tour 1 — addendum d'empreintes de l'idée 1.1 (poids du nul), brouillon 1

- Pièce lue en entier : `docs/notes/organisme-idees-juge-v1/addendum-empreintes-idee-1-1-v1-brouillon1.md`
  (`6bab777fd312efe921f2183508069aa12fb8aedc5b8b410fdd415dca91f4c7d9`, égale à son compagnon), 422 lignes.
- Lecteur : contre-lecteur neuf, lettre C. Je n'ai écrit aucune des pièces. La pièce est de la lettre A ; les corrections seront de la lettre A.
- Date (UTC, `date -u`) : 2026-11-16, de 13:54 à 14:00 environ. Dépôt lu sur `main`, tête `29f2cc63` (la pièce cite `df131fbd`, plus ancienne : le code gelé n'a pas changé, voir 1).
- Ce que j'ai fait : le seul appel de `--lister-empreintes` de `scripts/etape0_idee_1_1_v5.py` et un appel de `execution_idee_1_1_v5.lire_addendum` sur la pièce ; des lectures. Aucun jeu, aucun essai, rien sous `diag/`, `runs/`, `donnees/`, rien dans les deux copies interdites, aucun réseau, aucun git de ma main, aucune valeur de clé. Travail jetable sous le bloc-notes de la session.
- **Incident de ma main** : un appel d'outil avec un nom en minuscules (`bash` au lieu de `Bash`), refusé par l'outil, sans effet. Aucun autre.

## 0. Verdict

**Corrections** (une majeure, sept mineures, une facultative). Rien ne met la conception en cause : la mécanique de la pièce est exacte, les empreintes et les chiffres sont justes. Reste à décrire exactement la reprise et à corriger quelques phrases de § 4.3, § 4.4, § 5 et § 6.

## 1. Ce que j'ai vérifié et trouvé exact

1. **Lignes d'empreintes.** `.venv/bin/python -I -B scripts/etape0_idee_1_1_v5.py --lister-empreintes` rend 46 lignes ; `diff` avec les 46 lignes de la pièce : **identique**. Aucune autre ligne de ce format dans la pièce (46 correspondances, sur toute la pièce, avec et sans ancrage de début de ligne).
2. **Bloc programme.** Extrait par octets entre les deux marqueurs, dans la pièce et dans le journal `c9c8014c…` : 3 962 octets des deux côtés, **égaux à l'octet**, un seul bloc de chaque côté.
3. **`lire_addendum`** appelé sur la pièce : rend sans arrêt ; 46 fichiers ; 2 processus ; réductions vides ; D = 15,667 463 h ; règle rejouée égale (`jeu_permis` vrai, trace sans réduction) ; fichier d'étape 0 `540dfa68…` égal à son empreinte.
4. **Fichier d'étape 0** (`resultat`) relu par programme et comparé à la pièce : commit `a46d8028`, 12:45:54Z à 13:46:14Z ; E0 100 répétitions, écart 0 ; E9 58 évaluations ; ED 58 répétitions, 2,87·10⁻⁷ ; EP 50 mondes, 0 ; 17 mutations, toutes tuées, tous cas sains passés ; préalable 1 : 16 noms, E9 vrai, 37 sur 37, vue de 58 fichiers (empreinte de liste `96107ec2…`), listes « à défaut » et « filtre » vides ; garde P4 : H7 86 et 58 sans garde, 0 et 0 sous gel ; Hn 19 et 9, 0 et 0 ; égaux à R-2976. Les 18 clés `cles_97` et les 24 lignes de copies tierces de la pièce sont **toutes** égales au fichier ; les 30 lignes du chronométrage (4 groupes et total) sont égales au fichier, arrondies à trois décimales ; somme 112,805 73 s ; D = 112,806 × 1 000 / 2 / 3 600 = 15,667 h ; à trois processus 10,445 h.
5. **Empreintes citées** recalculées : preuve v3 `a481c873…`, sa vérification `b2f92646…`, étape 0 v4 `c6c34fd0…`, trois différentiels `1334b735…`, `4944e35d…`, `de82c82e…`, module `attaque_goodhart_v2.py` `3c9de8b8…`, provenance v3 `a4a62a88…`, les trois fichiers `essai_projection_*` (`1f4ada97…`, `29704896…`, `539f6a6c…`), [C4] `9ba07614…`, [CF] `b09ae513…`, [CC] `63c6421b…`, [RD5] `6ce11448…`, texte `3ffe1739…`. `IT_PROJ` 300, `IT_MV` 300, `IT_CHAUD` 150 sont dans `projection_methodes_v1.py`. Aucun identifiant de modèle dans la pièce (lettre A seulement).
6. **Lignes du texte** citées : l. 9 à 11, 38 à 43, 239, 332 à 335, 383 à 387, 400 à 405, 438 et 439, 493 et 494, 509 à 523, 538, 541 et 542, 613, 620, 626, 627, 640 à 646, 659, 673 à 675, 699 : justes (celles de 692 à 696 sont à une ou deux lignes près, sans conséquence). Le bloc, la citation de GO-2026-11-16-01 (mot verbatim et lecture du point (3), date 00:29:21Z) sont exacts mot pour mot.
7. **Déclarations exigées** : m9, m10, m11, comptes non écrits, lectures de la lecture gelée, complément de la copie : dans le bloc. D1 à D4 : repris de [C4] § 9 avec les bonnes lignes. Les sept points de [CC] § 5 sont présents (complément et phrase d'écart D5 avec les lignes du texte ; liste ; préalable 1 ; D1 à D4 ; processus et durée ; comptes P4 égaux à la v4 ; étape 0 v4 gardée) ; les copies tierces sont en tableau, y compris les deux entrées nouvelles.
8. **Écarts** : E2 et E3 cités au bon point (3) de GO-2026-11-16-01 ; D5 laissé au mot de Lazar, avec la mention « ne couvre pas D5 » ; deux processus : p ≤ 3 de [T] l. 642, pas un écart. Aucun écart de borne (48 heures) ni de commande. `lire_addendum` ne lit aucune valeur de `ACCORD-D5-A-REMPLIR` (aucune occurrence dans `src/`, `scripts/`, `tests/`).
9. **Lanceur** : `os.nice(10)`, garde réseau, `PROCESSUS_MAX` 3, `DUREE_MAX_S` 48 h comptée depuis `depart.json` (reprise comprise), 600 tranches de 50, `arret.json` interdit la reprise, TERM changé en `GardeArret`, fils mort détecté : conformes à la pièce.

## 2. Corrections

Chaque « ancien » figure **une seule fois** dans la pièce (vérifié par programme sur le texte du brouillon 1). Les deux dernières lignes de C4 sont des couples liés.

### Majeure

**M1 — Reprise : description incomplète et non classée** (§ 5, puce « Reprise »).
Le lanceur, en reprise, saute **toute** la branche des contrôles avant jeu : ni essais, ni 17 mutations, ni essais d'égalité E0, E9, EP, ED ne sont rejoués ; le manifeste et `depart.json` du premier départ sont gardés. [T] étape 1 les veut « rejoués » avant le jeu. La pièce dit « tranches déjà écrites vérifiées et sautées » mais pas cela, et laisse la reprise « sans la classer ». Une reprise ne devrait pas être décrite comme équivalente à un premier départ, ni laissée à l'opérateur. Ma lecture : pas un écart de fond (les contrôles ont été rejoués au premier départ sur le même code, dont les empreintes sont revérifiées à chaque reprise ; les tranches sont jouées aux graines `(i_ligne, r, …)` de leurs répétitions ; l. 620 vise la relance après une exception, donc après `arret.json`), mais c'est une lettre à écrire et à faire trancher par la mère (voir `points_pour_la_mere`).

- ancien : `` `arret.json` présent interdit la reprise.``
- nouveau : `` `arret.json` présent interdit la reprise. **Ce que la reprise ne rejoue pas** : les essais, les dix-sept mutations et les essais d'égalité E0, E9, EP, ED ne sont rejoués qu'au premier départ (la branche de reprise du lanceur n'en rejoue aucun ; manifeste et `depart.json` du premier départ gardés) ; sont revérifiés à chaque reprise : préenregistrement, arbre propre hors des dossiers du run repris, addendum et fichiers gelés, copies du juge et du v9, noms empruntés. **Classement** : [T] l. 620 interdit la relance après une exception ou un log W non fini, donc après `arret.json` ; une reprise sans `arret.json` n'en est pas une, une tranche perdue est rejouée aux mêmes graines `(i_ligne, r, …)` de ses répétitions, aucune réduction n'est ajoutée, aucune graine n'est rejouée après un échec de garde. Cette lecture est celle du rédacteur et n'est couverte par aucun mot de Lazar ; si la mère la juge écart de lettre à [T] étape 1, elle l'inscrit ici sous le nom D6 et le porte à Lazar avec D5. Une tranche à moitié écrite par une mort brutale (fichier sans compagnon) fait échouer la reprise elle-même, qui consigne alors `arret.json` : run invalide.``

### Mineures

**m1 — Jeton du mot de Lazar en double** (§ 6, point 2). Un remplacement automatique toucherait les deux occurrences.
- ancien : ``(à la place de `ACCORD-D5-A-REMPLIR`)``
- nouveau : `(sur la ligne « Mot de Lazar »)`

**m2 — Raison des deux processus mal attribuée** (§ 4.3). R-2976 donne « laisser un cœur aux travaux du billet » ; c'est R-2979 qui dit que le jeu de l'idée 1.2 tourne à côté.
- ancien : `(R-2976, R-2979), et un cœur reste aux travaux de la session.`
- nouveau : `(R-2979), et un cœur reste aux travaux du billet (R-2976).`

**m3 — Renvoi à R-2978 manquant à D5** ([CC] § 5 point 1 demande le renvoi à R-2976, R-2978 et au contrôle ; R-2978 n'est que dans l'en-tête).
- ancien : `- **Statut** : décision de la mère (R-2984) :`
- nouveau : `- **Statut** : code v5 rendu sous R-2978 ; décision de la mère (R-2984) :`

**m4 — Ordre du lanceur** (§ 5). Dans le code, « aucune sortie ni manifeste antérieur » est contrôlé **après** la lecture de l'addendum, des copies et des noms empruntés, et avant les essais (le docstring du lanceur le dit autrement que le code ; la pièce a suivi le docstring).
- ancien : `arbre propre ; aucune sortie ni manifeste antérieur de ce`
- nouveau : `arbre propre ; addendum lu (§ 1 et § 2) ; copies du juge et du v9 vérifiées ; noms empruntés ; aucune sortie ni manifeste antérieur de ce`
- ancien : `jeu (noms v1 à v5) ; addendum lu (§ 1 et § 2) ; copies du juge et du v9 vérifiées ; noms empruntés ; essais rejoués ;`
- nouveau : `jeu (noms v1 à v5) ; essais rejoués ;`

**m5 — « log W non fini » : liste d'arrêt de § 5 plus large que le banc** (§ 5 contre § 4.2). § 5 range « log W non fini » parmi les gardes qui arrêtent ; § 4.2 dit que le banc ne contrôle pas la finitude de plusieurs log W. Les deux phrases sont vraies, mais il faut les relier.
- ancien : `log W non fini, exception)`
- nouveau : `log W non fini là où le banc le contrôle (§ 4.2 dit ce qu'il ne contrôle pas), exception)`

**m6 — `essai_projection_cas_v1.py` : l'addendum l'inscrit, le code ne l'y compare pas** (§ 6). `vue_projection` compare `essai_projection_commun_v1.py` et `essai_projection_methodes_v1.py` à des constantes du code, mais `essai_projection_cas_v1.py` seulement à son compagnon (`attendu` vaut `None`). Le jeu rejoue EP : l'égalité à `539f6a6c…` n'est donc contrôlée que par l'opérateur. Je n'y vois pas de risque réel (arbre propre), mais la pièce doit dire qui contrôle. Insérer un point avant la copie propre :
- ancien : `3. Copie propre du commit qui porte la version scellée`
- nouveau : `3. Avant le départ, à la main : `sha256sum` de `docs/notes/organisme-idees-juge-v1/correction-poids-v1/projection/essai_projection_cas_v1.py`, égal à `539f6a6cfce71eaab9010fa9cd16a2607a0bf9faf9499286bcb6fb7f25bda837` (bloc § 2, m10) : le code ne compare cette empreinte qu'à son compagnon, non à l'addendum.` suivi, sur une nouvelle ligne, de `4. Copie propre du commit qui porte la version scellée`

(La suite de l'ancien point 3 reste telle quelle après « version scellée ».)

**m7 — Chronométrage par groupe** (§ 3). Le texte dit « temps de chaque bras » (l. 527, 640) ; le code mesure quatre groupes, et le temps non rangé (dont le temps mural non attribué) tombe dans « base ». Le brouillon le dit à moitié (« tout le temps mural non attribué ») ; la ligne de zéros des cinq lignes H en J9-P et La-P étonne un lecteur. Sans réduction, D n'en dépend pas (la règle des réductions 2, 4, 5 ne s'applique pas). Je ne vois pas d'écart de fond ; je le dis pour que la lettre soit nette :
- ancien : `Somme sur les 30 lignes : **112,806 s par répétition**`
- nouveau : `Les zéros des cinq lignes H en J9-P et La-P viennent de ce que le code range tout temps non nommé par un groupe dans « base » ; [T] l. 527 et 640 dit « temps de chaque bras » : le découpage en quatre groupes est celui du code, et aucune réduction n'étant appliquée, D n'en dépend pas. Somme sur les 30 lignes : **112,806 s par répétition**`

### Facultatif (je ne l'exige pas)

- Au § 5, « Consigne : garder une tâche active » est bien ; on pourrait ajouter que le PID du parent est noté **dans le registre**, pas seulement « au lancement ». Non exigé.

## 3. Ce qui n'est pas à corriger, mais que je note

- **« Réserve fils oisif »** : la pièce dit elle-même qu'elle est non éprouvée sur ce code ; le montage (`Pool` fork, `imap_unordered`, attente de 5 s, `with Pool`) est bien le même que celui de la 1.2. Le signal TERM envoyé au parent lève `GardeArret` dans le `with` ; la sortie du `with` appelle `terminate()`, qui peut s'accrocher sur le verrou décrit en 1.2. Je ne l'ai pas éprouvé (interdit). Le risque est connu, dit ; il ne bloque pas.
- **TERM au parent** écrit `arret.json` donc interdit la reprise : la consigne « tâche active » est bien la protection. La pièce le dit.
- **Reprise après mort brutale en pleine écriture** : voir M1, dernière phrase.

## 4. Pour la session mère

Voir `points_pour_la_mere` du rendu. Je n'ai pas modifié la pièce, pas committé.
