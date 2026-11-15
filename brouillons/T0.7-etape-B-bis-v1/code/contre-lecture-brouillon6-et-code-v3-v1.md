# Contre-lecture du brouillon 6 du texte de B bis (différentiel 5 → 6) et du code v3 du contrôle carte-processeur, v1

**Verdict : scellable après corrections.** Le différentiel du texte est exact (dix couples, trois retouches de forme, rien
d'autre) ; le code v3 fait ce que les décisions R-2919 et R-2931 demandent, chaque version neuve est la précédente plus le
différentiel déclaré, et chaque arrêt neuf a son cas sain et son artefact. **Un majeur, qui n'est ni dans le différentiel ni dans
le code v3 mais dans ce sur quoi ils reposent** : le texte de B bis **est déjà scellé** depuis le 14 novembre (M1) ; le brouillon 6
ne peut donc pas recevoir « le » scellement, il est une version neuve d'un texte scellé (nœud de Lazar), et le code v3 reste lié
par construction à l'ancien texte. À régler avant `CODE-BBIS` ; **sans effet sur la passe de répétition**.

**La quatrième passe payante de répétition peut partir avec ce code** (`scripts/lancer_repetition_bbis_v3.sh`, commit
`ce470564`), sous les consignes de lecture du § 8.

**Déclaration** : contre-lecteur neuf, aucun fichier de l'étape B bis écrit par moi ; processeur seulement ; aucune machine,
aucun appel payant ; rien lu sous `diag/`, `donnees/`, `docs/verdicts/` (voir l'incident 2 du § 9 pour une écriture involontaire
dans le bloc-notes) ; aucune entrée de 7a ou 7b ; aucune valeur de clé. Appels réseau : six `git ls-remote` en lecture. Aucun
commit, aucune poussée ; seul fichier écrit dans l'arbre de travail : ce rapport et son compagnon. Lus aussi, dans le dépôt
principal, par leur nom : `registres/decisions.md` (lignes R-2746, R-2751, R-2790, R-2802, R-2883, R-2902, R-2917 à R-2919,
R-2923, R-2931), `registres/etat.md`, `registres/t07-etape-b-bis-v1.md`, `prereg/T0.7-etape-B-bis-v1.md`.

- **Date (UTC)** : 2026-11-15, de 20:25 à 21:20.
- **Objet** : commit `ce47056455595bc52fad676c0e57ad9d8bef886d` de `prep/t07bbis-code-v1` (égal à la branche distante,
  `git ls-remote`), lu dans l'arbre de travail et par une extraction `git archive` dans le bloc-notes, supprimée à la fin.
- **Pile des essais** : python 3.13.18, torch 2.14.1+cu130, numpy 2.4.6, processeur seul.
- **Pièces vérifiées par leur compagnon** : brouillon 5 `99d88954…`, brouillon 6 `bf1be58e4be262b1…`,
  `pieces/couples-brouillon6-v1.py` `b61ed1d32d5fef1b…`, `code/corrections-controle-attention-v2.md` `4e4fad18cff93589…`,
  `code/fichiers-fiche-code-bbis-v3.txt` `b8fb095bf44dc855…`, `code/contre-lecture-brouillon5-et-code-v2-v1.md`
  `93b0724dd41b6c0b…`, texte scellé `prereg/T0.7-etape-B-bis-v1.md` `0ae6210f954917fe…`.
- **Code lu** (empreintes au commit, égales au § 8 du rapport du développeur) : `validation_imbriquee_v3.py` `71bffa5bf26c2b18…`,
  `marche_v3.py` `7009b34d46c33ed8…`, `lecture_v2.py` `154795f4ecfa3273…`, `scripts/amorce_bbis_v3.sh` `18e2f2052efdca0d…`,
  `scripts/lancer_bbis_v3.sh` `dc26ea01a06bfb9e…`, `scripts/repetition_carte_bbis_v3.py` `355b313319d01f8a…`,
  `scripts/amorce_repetition_bbis_v3.sh` `cb489ebec9206afe…`, `scripts/lancer_repetition_bbis_v3.sh` `5bd32c146e0798b5…`,
  `conftest.py` `8fe7cc46c35c13da…`, `tests/aide_t07bbis_differentiels_v3.py` `b2899511f82b5fc0…`,
  `tests/test_t07bbis_controle_v3.py` `ecdeb07dd69203fb…`, `tests/test_repetition_bbis_v3.py` `6b17a89e4dcdf1d9…`,
  `tests/test_essais_git_propres_bbis_v1.py` `e87f1bb983489dfb…`.

## Majeur

**M1 — Le texte de B bis est déjà scellé ; le brouillon 6 est une version neuve d'un texte scellé, et le code v3 est lié à
l'ancien.** Faits, vérifiés sur disque et par empreinte, sur la branche et sur `main` :
- `prereg/T0.7-etape-B-bis-v1.md` existe, son compagnon est juste (`0ae6210f954917fecff647f45a129961c0676517381becbffe1fd5ac7b90d9eb`) ;
  c'est le brouillon 3 plus le dernier couple mécanique (cinq lignes de différence) ;
- le registre propre `registres/t07-etape-b-bis-v1.md` porte
  `| SCELLEMENT-BBIS | 2026-11-14T12:30:30Z | prereg/T0.7-etape-B-bis-v1.md | 0ae6210f… |` et la ligne `ABSENCE-B-BBIS` de la même
  seconde (commit `f72d2833`, « Étape B bis scellée », R-2746) ; R-2751, R-2790 et R-2802 parlent du « texte scellé » ;
- R-2902 et R-2917 écrivent pourtant « le texte de B bis n'est pas scellé » ; la ligne de statut du brouillon 6 (ligne 54) dit
  « non scellé. Il ne vaut préenregistrement qu'après son scellement et la ligne `SCELLEMENT-BBIS` » ; la contre-lecture
  précédente dit « avant `SCELLEMENT-BBIS` ». **C'est faux depuis le 14 novembre.**
- Le texte scellé porte l'ancien contrôle (« un (cellule, pli) tiré par graine est réappris sur le processeur par
  `sondes.familles` ; écart relatif maximal des scores sur 256 actions tirées ≤ 10⁻⁴, sinon arrêt ») ; « R-PILE » n'y figure pas.

Conséquences :
1. **Décision.** Les couples a1 à a5, b1, b2 et c1 à c10 changent le plan d'analyse, la liste d'arrêt et les critères de lecture
   gelés d'un texte scellé : écart à un préenregistrement scellé, nœud de Lazar (hiérarchie de décision ; R-2883 garde au mot de
   Lazar « écart à un texte scellé non accordé »). Le seul écart accordé est la répétition (R-2802). Les décisions R-2917 et
   R-2919, prises en autonomie « parce que le texte n'est pas scellé », reposent sur une prémisse fausse. Le fond n'est pas en
   cause (le contrôle scellé arrêterait à tort toute course dont le couple tiré a une sonde « attention » sans signal) ; c'est
   la voie qui manque. La mère devra aussi écrire l'état de l'étape B à l'heure du scellement de la version neuve (le texte scellé
   exige l'antériorité à toute exécution de l'étape B) : je ne l'ai pas regardé.
2. **Code.** Le code v3 ne connaît que l'ancien texte : `commun_v1.TEXTE` et `TEXTE_SHA256 = "0ae6210f…"` (lignes 27 et 28) ;
   `marche_v3` écrit `"texte": TEXTE` et passe `prereg=racine / TEXTE` au manifeste (lignes 175, 297, 305) ; `lecture_v2` écrit
   `texte_sha256 = 0ae6210f…` (ligne 1124), **refuse** toute ligne `SCELLEMENT-BBIS` autre que (ce chemin, cette empreinte)
   (ligne 1137), refuse deux lignes d'une même clé et toute clé inconnue au registre propre (`lire_lignes`, lignes 536 à 544) ;
   l'amorce n'extrait que `/prereg/T0.7-etape-B-bis-v1.md*`. Une version 2 scellée sous un nom neuf ne peut donc être ni citée par
   la marche ni acceptée par la lecture ; et telle quelle, la lecture écrirait R-PILE et le point (7) en citant un texte qui ne
   les porte pas.
- ancien (brouillon 6, ligne 54, fin) : « non scellé. Il ne vaut préenregistrement qu'après son scellement et la ligne
  `SCELLEMENT-BBIS`, **strictement avant toute exécution de l'étape B de T0.7** (R-2716 (1)). Aucune machine, aucune dépense,
  aucun résultat lu. » ;
- nouveau : « version neuve du texte scellé `prereg/T0.7-etape-B-bis-v1.md` (`0ae6210f…`, ligne `SCELLEMENT-BBIS` du
  2026-11-14T12:30:30Z, R-2746), dont elle ne change que les couples a1 à a5, b1, b2 et c1 à c10 des tableaux en tête ; écart à
  un texte scellé : elle ne vaut qu'après le mot de Lazar et son scellement sous un nom neuf (R12), avant `CODE-BBIS` ; état de
  l'étape B à cette heure : [relevé par la mère, par les noms seulement]. Dépense à ce jour : les passes de répétition sur
  données synthétiques (écart accordé, R-2802) ; aucun résultat lu. » ;
- et, pour le code, deux voies à trancher avec Lazar :
  (i) **version 2 du texte** (`prereg/T0.7-etape-B-bis-v2.md`, ligne de scellement neuve) : il faut alors des modules à nom neuf
  qui portent le chemin et l'empreinte neufs (au moins la marche, la lecture, l'amorce et son motif d'extraction, et la règle du
  registre propre sur la ligne de scellement) ; lourd, et la répétition devrait rejouer ce code ;
  (ii) **addendum d'écart déclaré**, scellé à part (fichier et compagnon sous `prereg/`, mot de Lazar consigné), qui porte
  exactement les couples ; le texte du 14 novembre reste le texte cité, le code v3 reste tel quel, et le verdict cite l'addendum
  et son empreinte ; à écrire dans l'addendum : la lecture `lecture_v2` ajoute R-PILE, le point (7) et la garde du champ du
  contrôle. Ma recommandation : (ii), confiance moyenne (le code éprouvé ne bouge pas ; la forme est celle de R-2802).
Sans effet sur la passe de répétition (données synthétiques, écart déjà accordé, plafond 3 USD gardé par le lanceur).

## Mineurs

**m1 — Un couple absent des sources serait écarté du tirage sans mot.** `validation_imbriquee_v3.py`, ligne 132 :
`finis = [c for c in self.couples if c in sources and sonde_finie(sources[c][1])]`. En v2, « couple tiré absent des sources »
arrêtait. Impossible dans `marche_v3` (la boucle remplit les dix couples ou lève une exception), donc sans effet à la course ;
la garde `if controle.resultat is None` de `marche_v3` (ligne 382) est, elle, devenue inatteignable.
- ancien : la ligne 132 seule ; nouveau (seulement si une v4 est écrite pour une autre raison) : la précéder de
  `absents = [c for c in self.couples if c not in sources]` et d'un `GardeArret` « couples absents des sources » si la liste
  n'est pas vide, avec cas sain et artefact. Sinon : réserve écrite, pas de code.

**m2 — Les arrêts neufs ne sont éprouvés qu'au niveau de `ControleCarte`, pas de la marche.** Je les ai joués dans `marche_v3`
en mode jouet (programme en annexe, 4 passés, § 4) : ils tiennent. À verser comme essais à la prochaine version des essais.

**m3 — `lecture_v2` : la garde du champ du contrôle vient tard et ne lit pas les horizons.** `exiger_controle_carte` est appelée
ligne 1209, après les lecteurs de texte et le contrôle de la base « mots et coût » (rien n'est écrit ni imprimé avant ; aucune
aire de sonde n'est encore calculée) ; elle ne vérifie ni `epoques` (300 et 3) ni le nombre d'actions. Sans effet sur l'issue.
- nouveau (si une `lecture_v3` est écrite, voie (i) de M1) : appel juste après la lecture de `sondes-bbis.json` (ligne 1160), et
  refus si `attention.epoques != 3`.

**m4 — Le texte ne dit pas ce que devient le contrôle après un arrêt de débit.**
- ancien (point 5) : « aucun : arrêt (erreur de chaîne). Raison, écrite avant toute lecture : » ;
- nouveau : « aucun : arrêt (erreur de chaîne) ; après un arrêt de la garde de débit, aucun contrôle n'est joué (aucun score
  n'est écrit). Raison, écrite avant toute lecture : ».

**m5 — R-PILE et la sonde d'ENC : interprétation à écrire.**
- ancien : « (écrite dès qu'une sonde finale lue est de la famille « attention » : » ;
- nouveau : « (écrite dès qu'une sonde finale lue, celle d'une source ou celle d'ENC, est de la famille « attention » : ».

**m6 — À la répétition, un arrêt du contrôle lui-même ne laisse pas de champ `lecture_de_la_passe`.**
`repetition_carte_bbis_v3.py`, lignes 495 à 497 : sur `GardeArret`, code 9 sans ce champ ; le résumé de l'amorce imprime alors
« lecture de la passe None », et le motif d'arrêt de l'amorce reste « contrôle au-delà de 10⁻⁴ ou apprentissage non
déterministe » même pour « la passe ne compte pas ». Consigne de lecture, sans code (§ 8, point 3).

**m7 — Coût d'un arrêt tardif (réserve à écrire).** En v2 une erreur de chaîne était vue dès que le couple tiré était appris ;
en v3 elle n'est vue qu'après les dix sources : une course arrêtée par le contrôle coûte tout l'apprentissage. Le pire cas du
devis compte déjà une relance complète ; à dire au feu écrit.

## 1. Le texte : différentiel exact 5 → 6

- `couples-brouillon6-v1.py` rejoué sur une copie du brouillon 5 seul : « couples appliqués : c1 à c10 ; forme : titre, statut,
  tableau ; lignes changées hors du tableau : 7 ; lignes ajoutées (tableau) : 15 », brouillon 6 `bf1be58e…`, **égal octet pour
  octet** au fichier du commit.
- Différentiel par lignes : 311 lignes au brouillon 5, 326 au brouillon 6 ; zones : 1 → 1 à 16 (titre et tableau), 39 → 54
  (statut, ajout seul), 122 → 137 (c1 à c4), 172 → 187 (c6), 203 → 218 (c5), 244 et 245 → 259 et 260 (c7 à c10). Rien d'autre.
- Différentiel par mots dans ces lignes : chaque retrait et chaque ajout appartient à un couple déclaré. **Critères, seuils,
  grille, garde de débit (11 h, facteur 1,2, 0,6 h), planchers, nul, états, issues, calendrier, dépense et les autres lignes de
  la liste d'arrêt : égaux ligne à ligne au brouillon 5.**
- Décisions dans le texte : (1) point 5 et liste d'arrêt : « Aucune issue « sans objet » », sonde de contrôle en échec à 3 ou à
  300 époques, déterminisme compris : arrêt ; tirage à la fin parmi les sondes finales finies, même ordre trié, même graine ;
  aucun : arrêt (c2, c5) ; (4) règle de lecture de la répétition, écrite avant la passe (c4) ; m5 (c1), m6 (c3, c6), m7
  (`dd67802d…` aux deux citations, c4 et c6) ; noms v3 et `lecture_v2` (c7 à c9) ; épreuves (c10).

## 2. Le code, décision par décision

1. **M2, voie (b)** : conforme. `controle_deux_horizons` : les deux `SondeEnEchec` (sonde de contrôle, déterminisme) deviennent
   `GardeArret` « … : arrêt (erreur de chaîne) » ; plus aucune clé `sans_objet`. `ControleCarte.jouer` : couples triés, filtre
   `sonde_finie` (w, b, q finis ; une source en échec n'a pas de sonde), générateur neuf de la clé `bbis/egalite-carte`
   (`Graines.rng` rend la même suite à chaque appel), indice puis 256 actions par le même générateur : même tirage que la v1
   quand tout est fini ; aucun : arrêt ; second appel : refus. `marche_v3` : appel après la boucle, étape nommée ; un arrêt du
   contrôle passe avant `ecrire_fermes` : **aucun score n'est écrit** (`arret-marche-bbis.json`, étape « contrôle
   carte-processeur »).
2. **M1** : conforme. `lecture_v2` = `lecture_v1` + R-PILE (phrase du texte, mot pour mot) + point (7) + `exiger_controle_carte`
   (absent, « sans objet » à toute profondeur, variante inconnue, écart absent, booléen, chaîne, non fini, > 10⁻⁴, déterminisme
   absent ou faux : `RefusLecture`, la lecture rend le code 2 sans rien écrire).
3. **m1** : conforme. La répétition v3 construit `lot_controle = ac.LotCarte(seqs, appareil)`, écrit `lot_reconstruit`, joue
   `validation_imbriquee_v3.controle_deux_horizons` sur ce lot avec les sondes du premier.
4. **Règle de lecture** : conforme au texte. `lecture_de_la_passe` : écart numérique fini par famille, égalités vraies
   (déterminisme des deux familles, de l'attention du contrôle, lot reconstruit), maximum ≤ 10⁻⁴, sinon « ne compte pas » et
   code 9 ; maximum ≤ 10⁻⁵ : « la course part sans nœud » ; sinon « nœud écrit à la mère avant la course », code 0.
5. **Minimum 115** : `MIN_ESSAIS=115`, une seule définition, lue par l'amorce de la répétition ; égal au compte rejoué (§ 5).
6. **m4 à m7, m9** : m4, listes d'actions comparées élément par élément ; m5 à m7, couples c1, c3, c4, c6 ; m9, « v4 » pour la
   branche de sortie, le dossier des traces, le dossier de l'instance et l'étiquette (lanceur et script), fichiers en v3.
7. **Garde des essais** : `conftest.py` v1 gardé ; retire les six variables et tout `GIT_CONFIG*` à l'import, les remet à la fin ;
   réserve écrite (R-2931 ; rapport du développeur, § 4.1 et § 5).

**Chaque v3 = v2 + différentiel déclaré** : les huit essais d'égalité passent (cinq fichiers de la course, trois de la
répétition) ; j'ai relu les huit `diff`. **Blocs marqués** comparés par programme : amorce de la course 7 blocs et lanceur
1 bloc, **identiques** à la v1 et à la v2 ; lanceur de la répétition 1 bloc, identique ; amorce de la répétition 11 blocs, dont 3
changés (`motifs-de-la-course` et `depot` : noms seuls ; `lecture-de-la-course` : nom et lecture de la passe au résumé). Blocs
`cuda-du-pilote`, `carte-et-cuda`, `branche-de-sortie` inchangés ; clonage `--single-branch --branch "$BRANCHE_CODE"` et
`checkout "$COMMIT"` inchangés. **Liste de la fiche v3** : 103 chemins triés, tous présents au commit et dans l'arbre de
l'instance simulé ; = la v2 plus les huit chemins déclarés.

## 3. Les réserves du développeur, une par une

- **Tirage en fin d'apprentissage ; aucun contrôle après un arrêt de débit.** Conforme au texte (« tiré à la fin de
  l'apprentissage ») ; **pas un repli silencieux** : l'arrêt de débit est écrit (`arret-debit-bbis.json`, scellé, code 3), aucun
  score n'existe, donc rien que le contrôle doive garder ; la relance rejoue tout, contrôle compris. En pratique rien ne change :
  la garde de débit se déclenche après 20 apprentissages, quand la première source (246 apprentissages) n'est pas finie ; la v2
  n'aurait pas joué de contrôle non plus. Vérifié en marche jouet (§ 4). À écrire au texte (m4) ; coût d'un arrêt tardif (m7).
- **Mémoire du lot du contrôle.** `apprendre_source` ne rend pas le lot : à la fin de l'apprentissage aucun lot n'est sur la
  carte ; `jouer` en construit un (≈ 143 000 jetons × 4 096 × 8 octets ≈ 4,7 Go), comme le lot reconstruit de la v2. Les
  séquences des dix sources sont déjà tenues en mémoire vive jusqu'aux fichiers fermés en v1 et en v2. Pas de besoin neuf, par
  lecture du code ; non mesuré sur carte. La répétition tient **deux** lots à la fois : son pic est une borne haute.
- **« ≤ 10⁻⁵ pour chaque famille ».** C'est la lettre du couple c4 (« si l'écart de chaque famille est ≤ 10⁻⁵ ») ; plus strict
  que la proposition d'origine (attention seule). Accepté.
- **R-PILE et ENC.** Lecture prudente (la réserve s'écrit plus souvent, sans changer l'issue). Acceptée ; à écrire (m5).
- **Suffixe v4.** `git ls-remote --exit-code origin refs/heads/calcul/t07bbis-repetition-v4`, depuis l'arbre de travail, sans
  variable `GIT_DIR`, `GIT_WORK_TREE` ni `GIT_INDEX_FILE` : **code 2, absente** ; `…-v3` : absente ; `…-v1` (`56f5b8b8…`) et
  `…-v2` (`3528a2e8…`) : présentes ; `donnees/t07-etape-b-bis-v1` (course) : absente ; `prep/t07bbis-code-v1` : `ce470564…`.
- **Non éprouvé sans carte** : exact, voir § 7.

## 4. R5 : chaque arrêt neuf a-t-il son cas sain et son artefact ?

| arrêt neuf | cas sain | artefact | où |
|---|---|---|---|
| sonde de contrôle en échec (attention à 3, linéaire à 300, attention à 300, déterminisme) | oui | oui, 4 cas | `test_t07bbis_controle_v3.py` |
| aucun couple à sonde finale finie | oui | oui | idem |
| tirage parmi les sondes finies (une en échec, une à paramètres non finis) | oui (égal à la v1, listes d'actions) | oui | idem |
| contrôle joué deux fois | oui | oui | idem |
| lecture : champ du contrôle | oui (deux variantes) | oui, 10 cas | idem |
| R-PILE, point (7) | sans sonde « attention » | sonde, ENC, source en échec ignorée | idem |
| répétition : la passe ne compte pas (code 9) | oui (« sans nœud », « nœud ») | écart absent, chaîne, égalité fausse, poids altérés, limites | `test_repetition_bbis_v3.py` |
| variables `GIT_*` | oui | oui (sans la garde, le témoin bouge) | `test_essais_git_propres_bbis_v1.py` |

**Mes essais, dans `marche_v3` en mode jouet** (une course jouet de T0.6, quatre marches ; annexe) : (a) garde de débit forcée :
`arret_debit`, `scores_ecrits` faux, `jouer` jamais appelé, fichiers écrits : l'arrêt et la relecture seulement ; (b) sonde
finale du couple que tirerait la v1 (`P-S50`, pli 1) en échec : scores écrits, source marquée en échec, couple du contrôle
`P-instruit`, pli 0, égal au tirage attendu de la même graine parmi les cinq autres, `tirage = {couples : 6, sondes finales
finies : 5}` ; (c) toutes les sondes finales en échec : arrêt « aucun des 6 couples… (erreur de chaîne) », étape « contrôle
carte-processeur », aucun fichier de scores ; (d) sonde de contrôle « attention » à 3 époques en échec : arrêt « erreur de
chaîne », aucun fichier de scores. **4 passés** en 61 s.

## 5. Essais rejoués

- **Suite B bis** (`tests/test_t07bbis_*.py`, `test_repetition_bbis_v1.py`, `_v2.py`, `_v3.py`,
  `test_essais_git_propres_bbis_v1.py`) dans l'arbre extrait du commit : **182 passés, 1 sauté, 0 échec** en 357 s ; le sauté
  est `test_fichiers_reels_de_la_branche` (« commit cité absent de ce clone » : l'extraction n'a pas d'objets git) ; rejoué
  après avoir donné à l'arbre extrait un dossier git jouet (`git init`, fichier `objects/info/alternates` vers les objets du
  dépôt, en lecture ; aucune variable `GIT_*`) : le fichier rend 8 passés, 0 sauté. **Total : 183 passés, 0 échec, 0 sauté** :
  le compte du développeur.
- **Arbre de l'instance simulé** (dépôt jouet du bloc-notes, mêmes objets en lecture, `sparse-checkout` par les 25 `MOTIFS` de
  `amorce_bbis_v3.sh`, `checkout` du commit : 336 fichiers ; commande d'essais de l'amorce) : **115 passés, 24 sautés,
  0 échec** en 194 s, sortie d'erreur vide, `src` et `tests` propres après les essais ; minimum 115. Sautés : 16 « chaîne de
  T0.6 absente de ce clone », 8 « code de la pièce absent » ou « fabrique factice absente », comme le dit le développeur.

## 6. Amorces et lanceurs

Différentiels v2 → v3 relus ligne à ligne : course, noms v3, deux motifs ajoutés, `MIN_ESSAIS=115` et son commentaire ;
répétition, noms v3, dossiers et branche en v4, étiquette `bbis-t07-repetition-v4`, lecture de la passe au résumé. Garde CUDA
(`exiger_cuda_du_pilote`, avant toute installation) et contrôle de la branche de sortie (`branche_de_sortie_neuve` aux lanceurs,
`ls-remote` aux amorces) inchangés ; le lanceur de la répétition exige toujours que l'amorce et le script du commit soient ceux
du poste, et garde le cumul sous 3 USD. `conftest.py` de la racine entre dans l'arbre de l'instance par le motif `/*`.

## 7. Ce que je n'ai pas vérifié

- Rien sur carte : écart à 3 époques, égalité de deux lots construits sur la carte, déterminisme à 300 époques, mémoire.
- Les amorces et lanceurs v3 n'ont pas tourné ; je n'ai lu que leurs différentiels et comparé leurs blocs.
- La répétition ne joue ni `ControleCarte.jouer` (tirage en fin d'apprentissage) ni `marche_v3` ni `lecture_v2` : essais sur
  processeur seulement.
- L'état de l'étape B (M1) ; les essais du reste du dépôt sous la garde git (contre-épreuve du développeur non rejouée).
- Je n'ai pas refait les 35 artefacts de la contre-lecture précédente : le calcul du contrôle n'a pas changé.

## 8. Quatrième passe : consignes de lecture

1. Lancement par `scripts/lancer_repetition_bbis_v3.sh` au commit `ce470564` (ou un commit qui porte les mêmes trois fichiers,
   ce que le lanceur vérifie) ; branche de sortie `calcul/t07bbis-repetition-v4`, absente à 20:56 UTC ; cumul des passes
   strictement sous 3 USD ; ligne de dépense, feu écrit et préavis comme pour les passes précédentes.
2. `essais.txt` : la ligne « **115 passed, 24 skipped** » ; tout autre compte : nœud avant d'aller plus loin.
3. **Tout code de sortie non nul : la passe ne compte pas**, quoi que dise le résumé (m6). Code 0 : lire dans
   `repetition-carte.json` `lecture_de_la_passe.compte` vrai et son `issue` ; `fraction_de_la_course` égale à 1 (640 actions,
   largeur 4 096 : `ACTIONS_REPETITION` non posée) ; `lot_reconstruit.egal_au_premier` vrai ; `deterministe` vrai pour les deux
   familles ; `determinisme_attention.egal_au_bit` vrai.
4. Issue « la course part sans nœud » seulement si les deux écarts (linéaire à 300 époques, attention à 3) sont ≤ 10⁻⁵ ; entre
   10⁻⁵ et 10⁻⁴ : nœud écrit à la mère avant la course ; aucune autre lecture après coup.
5. Relever `controle_parametres.memoire_carte_max_octets` (pic avec deux lots : borne haute pour la course).
6. La passe ne dit rien du tirage en fin d'apprentissage, de la marche ni de la lecture ; elle ne lève pas M1 : **ni `CODE-BBIS`
   ni la course avant que M1 soit tranché**.

## 9. Incidents de ma main

1. **`env` lancé deux fois**, contre la consigne : une fois filtré pour n'imprimer que les **noms** des variables `GIT_*` de la
   session (`GIT_ASKPASS`, `GIT_CONFIG_COUNT`, `GIT_CONFIG_KEY_0` à `_2`, `GIT_CONFIG_VALUE_0` à `_2`, `GIT_EDITOR`,
   `GIT_SSL_CAINFO`, `GIT_TERMINAL_PROMPT`), une fois pour un compte (0). Aucune valeur affichée ni écrite. Ni `GIT_DIR`, ni
   `GIT_WORK_TREE`, ni `GIT_INDEX_FILE` n'étaient posées.
2. **Copies de `diag/`, `donnees/` et `docs/verdicts/` écrites dans le bloc-notes** par l'extraction entière du commit
   (`git archive`), 232 Mo ; supprimées aussitôt ; seule leur taille a été lue (`du`), aucun fichier ouvert. Mes marches jouets
   ont écrit des dossiers `diag/` et `docs/verdicts/` **jouets** dans leurs dépôts temporaires, supprimés.
3. **Bloc-notes partagé avec d'autres agents** (je ne l'ai vu qu'à la fin) : j'y ai créé puis supprimé les dossiers `arbre`,
   `inst`, `b6` et trois dossiers temporaires d'essais, et j'ai fait un `rm -rf` de `inst` avant de le créer sans regarder s'il
   existait ; j'ai écrit deux fichiers dans un dossier `outils` qui existait déjà. Espace libre du disque égal avant et après
   (8,4 Go) : je ne crois pas avoir supprimé le travail d'un autre, sans pouvoir le prouver.
4. Dépôt principal et arbre de travail : `git status` vides après mes essais ; aucun `pytest` ni commande git sous une variable
   `GIT_DIR`, `GIT_WORK_TREE` ou `GIT_INDEX_FILE` ; les objets du dépôt n'ont été lus que par un fichier `alternates` de deux
   dépôts jouets du bloc-notes, supprimés.

## Annexe — essais de la marche v3 en mode jouet (§ 4)

Lancement, hors de l'arbre extrait : `ARBRE=<arbre du commit> python -m pytest -q -s -p no:cacheprovider <fichier>`.

```python
import json, os, sys
from pathlib import Path
import pytest
ARBRE = Path(os.environ["ARBRE"]); sys.path[:0] = [str(ARBRE / "src"), str(ARBRE / "tests")]
import aide_t07bbis_jouet_v1 as aide
from controle_ia.t07bbis import (apprentissage_carte_v1 as ac, commun_v1 as cm, marche_v3, validation_imbriquee_v1 as vi1,
                                 validation_imbriquee_v3 as vi3)
ESSAI = {"epoques": 15, "n_plis_internes": 3, "n_directions": 12, "n_reetiquetages": 3, "n_controle": 6, "n_chemin": 3}
ENT = 2 ** 100 + 11

@pytest.fixture(scope="module")
def depot(tmp_path_factory):
    return aide.course_jouet(tmp_path_factory.mktemp("depot-cl"))

def _marche(d, n):
    return marche_v3.marche(d, aide.RUN, f"20261118-09000{n}-bbis-jouet", ENT, d.parent / f"{d.name}-travail-{n}", "cpu",
                            essai=dict(ESSAI))

def _fichiers(d, n):
    return sorted(p.name for p in (d / "diag" / f"20261118-09000{n}-bbis-jouet").glob("*"))

def _sans_score(d, n):
    return not any("sondes" in f or "scores" in f for f in _fichiers(d, n))

def _echec_si(monkeypatch, condition):
    vrai = ac.entrainer
    def faux(lot, famille, nom, *a, **k):
        if condition(nom, k):
            raise ac.SondeEnEchec("perte non finie (simulée)")
        return vrai(lot, famille, nom, *a, **k)
    monkeypatch.setattr(ac, "entrainer", faux)

def test_arret_de_debit_aucun_controle_aucun_score(depot, monkeypatch):
    joue = []
    monkeypatch.setattr(vi3, "GardeDebit", lambda total, debut: vi1.GardeDebit(total, debut, limite_h=-1.0))
    monkeypatch.setattr(vi3.ControleCarte, "jouer", lambda self, *a: joue.append(1))
    r = _marche(depot, 1)
    assert "arret_debit" in r and r["scores_ecrits"] is False and not joue and _sans_score(depot, 1)

def _couples(d):
    m = json.loads((d / "runs" / aide.RUN / "manifeste.json").read_text(encoding="utf-8"))
    doses, _ = marche_v3.plan_doses_couches(m["config"])
    return sorted((n, k) for n in cm.cellules(doses)["plafond"] for k in (0, 1))

def _indice(n):
    return int(cm.Graines(ENT, reelle=False).rng("bbis/egalite-carte").integers(0, n))

def test_sonde_finale_du_couple_v1_en_echec_autre_tirage_meme_graine(depot, monkeypatch):
    couples = _couples(depot)
    tire = couples[_indice(len(couples))]
    _echec_si(monkeypatch, lambda nom, k: nom == f"sonde-{tire[0]}-e{tire[1]}")
    r = _marche(depot, 2)
    doc = json.loads((depot / r["sondes_bbis"]).read_text(encoding="utf-8"))
    finis = [x for x in couples if x != tire]
    assert tuple(doc["couple_controle"]) == finis[_indice(len(finis))] != tire
    assert doc["controle_carte_processeur"]["tirage"] == {"couples": len(couples), "sondes_finales_finies": len(couples) - 1}
    assert "echec" in doc["sources"][tire[0]][f"e{tire[1]}"]

def test_toutes_les_sondes_finales_en_echec_arret_sans_score(depot, monkeypatch):
    _echec_si(monkeypatch, lambda nom, k: nom.startswith("sonde-") and "i" not in nom.rsplit("-e", 1)[1])
    r = _marche(depot, 3)
    assert "aucun des" in r["arret_marche"] and r["etape"] == "contrôle carte-processeur" and _sans_score(depot, 3)

def test_sonde_de_controle_en_echec_a_la_marche_arret_sans_score(depot, monkeypatch):
    _echec_si(monkeypatch, lambda nom, k: nom.startswith("controle-") and k.get("epoques") == 3)
    r = _marche(depot, 4)
    assert "erreur de chaîne" in r["arret_marche"] and r["etape"] == "contrôle carte-processeur" and _sans_score(depot, 4)
```
