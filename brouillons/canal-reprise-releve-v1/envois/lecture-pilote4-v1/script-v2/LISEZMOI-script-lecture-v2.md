# Script de lecture contre le bruit du pilote 4 — LISEZMOI v2

Sous-agent neuf de la lignée conv-audit (le même que pour la v1), 26 octobre 2026 ; cet en-tête est écrit à 05:15 UTC
(heure lue sur `date -u` juste avant). La v2 remplace la v1 (`/var/tmp/lecture-pilote4-v1/`, intacte : script
`7176f0cd…`, essais `2d3f2f26…`, journal `3c907fc7…`, LISEZMOI `53597f9c…`) après la relecture indépendante
`fournis/rapport-relecture-script-lecture-v2.md` (`9c15930dc242b2885557d81c6560f8b1aee54ebf03314699c353ced8f2959e3e`,
« utilisable après corrections », RSL-01 à RSL-17) et deux faits nouveaux : la seconde course est le même organisme (la
v6.2.1) sur la question S (mot de Lazar, R-492 ; texte v5 du pilote, table de correspondance : nom
`pilote4-gemini-v6-2-s-v1`, lignée `gemini-organisme-v6-2-s`), et la part `test_final` se lit une seule fois, en fin de
boucle (décision N-050, `fournis/decision-N-taches-fraiches-et-lecture-test-final-v1.md`,
`4b23e00fda02cef897f9d73b4274a0bed59bdab8a8f156f37a7966fb80d7a034`). Mêmes interdits qu'en v1, tenus : aucun fichier de
données de la banque, aucune archive ni pièce d'un pilote réel ouvert, lu ou haché ; aucun `git`, réseau, sous-agent,
clé ; aucun score réel ; écrit seulement sous `/var/tmp/lecture-pilote4-v2/`.

| fichier | sha256 |
|---|---|
| `lire_pilote4_v2.py` (bibliothèque standard seule ; Python 3.11, 3.12 et 3.13) | `a23613207175b1dbd89784215ececc2a8458332e3e11f1346179c254e099ae2a` |
| `essais_lire_pilote4_v2.py` | `dee7e0fec8951c4abbbc0a30100f4b0962854946beea6b0708b600985cee6308` |
| `essais-lire-pilote4-v2.log` | `4aa9de04d77a201981fa46c21c59c3ca2acb8bfa8dc835aab50f3ddf7b4c2555` |

## 1. Ce qui change de la v1

1. **Deux lectures par course** (N-050), chacune en JSON et en Markdown, avec compagnons `.sha256`, huit fichiers :
   `lecture-<course>-test-v2.{json,md}` (part `test` seule : effectifs, comptes et justes par classe, sans réponse,
   exactitude équilibrée, (i), (ii) contre les références de `test`, sous-ensemble « catégorie absente du train » de
   `test`, recoupement avec le noyau, signalements de `test` et faits mécaniques) et
   `lecture-<course>-test-final-<règle>-v2.{json,md}` (part `test_final` seule, même contenu sur ses références, plus (iii)
   et, avec DOSSIER_COURSE_2, les deux tests de l'autre course ; `<règle>` ∈ `provisoire`, `holm-deux`, `holm-quatre`,
   RSL-05). Le fichier `test` ne porte ni le mot `test_final`, ni (iii), ni la seconde course, ni aucune valeur de
   `test_final` ; l'inverse aussi (l'essai « séparation » le vérifie sur chaque lecture écrite : aucune exactitude, borne
   combinée, valeur de sous-ensemble ou valeur p d'une part dans les fichiers de l'autre, en JSON comme en Markdown, sur
   des données synthétiques dont les valeurs des deux parts sont disjointes par construction). Le Markdown de
   `test_final` porte en tête « à ne pas afficher avant la fin du compteur de rondes de la boucle extérieure ».
2. **Courses** : `pilote4-gemini-v6-2-v1` (M, dossier réel `pilote4-gemini-v6-2-v1-tentative2`) et
   `pilote4-gemini-v6-2-s-v1` (S), avec ou sans suffixe `-tentativeN` ; le nom du dossier fixe la lignée attendue
   (`gemini-organisme-v6-2`, `gemini-organisme-v6-2-s`) : un nom hors de ces formes, ou une archive dont la lignée n'est
   pas celle du nom, est refusé (RSL-04). En mode deux courses, les deux dossiers doivent différer par le chemin, le nom,
   la lignée et les empreintes (liste et archive) ; rien d'autre n'est exigé (même objet permis). Holm sur quatre reste ;
   `--sans-seconde-course` (la course S ne court pas) : Holm sur deux.
3. **Ligne d'état** (RSL-09) : `lecture écrite : <4 fichiers et empreintes> ; générations notées lues : K sur 4 ;
   signalements : N` — comptes entiers, aucun score ni proportion.
4. Les corrections de la relecture, § 3 ci-dessous.

Le reste est celui de la v1 (`LISEZMOI-script-lecture-v1.md`, § 1 et § 2 : modes, gardes, où le noyau range les
réponses et les scores avec les lignes de code, choix 1 à 18), aux changements près dits ici.

## 2. Où le noyau range les réponses et les scores (inchangé, rappel court)

`essaim_m3/noyau/boucle.py` l. 719–748 (lecture de `reponses_test.json` avec la règle du juge, scores de `test` et
`test_final` par `taches.evaluer`), l. 782–786 (`reponses_lues` passé à l'archive) ; `essaim_m3/noyau/archive.py`
l. 76–78 (`gNNN`), l. 111–126 (`juge/score.json`, `juge/score-final.json`, `juge/reponses_test.json`,
`juge/reponses-lues.json`) ; `taches.py` l. 29, 142–150, 202–229 ; lanceur v10 l. 75–85 (noms et lignées), 164–167
(`$PILOTE`, suffixe `-tentativeN`), 872–879 (archive), 911–919 (listes et empreintes), 920 (« pilote fini : $PILOTE »).
Le script lit `juge/reponses-lues.json` (repli déclaré et signalé sur `juge/reponses_test.json` par la règle du juge).

## 3. Constats de la relecture : ce qui a été fait

| constat | traitement |
|---|---|
| RSL-01 (commandes aux dossiers réels) | **fait** : § 5 aux dossiers `$PILOTE` exacts (`-tentative2` pour M ; `[-tentativeN]` pour S), noms de sortie qui en résultent ; refus explicite d'un nom hors des deux courses, motif qui renvoie au suffixe |
| RSL-02 (`-B`) | **fait** : `-I -B` dans toutes les commandes du § 5 et `sys.dont_write_bytecode = True` en tête du script (l. 49), avant tout autre import |
| RSL-03 (tar coupé net accepté) | **fait** : `verifier_flux_et_fin` (l. 350) exige, après le dernier membre, au moins deux blocs de 512 octets nuls et rien d'autre que des zéros jusqu'à la fin du flux ; essais « tar coupé net après le dernier membre » et « avant un membre nécessaire » : refus ; mutation M5 détectée |
| RSL-04 (nom contre lignée) | **fait** : `nom_de_course` (l. 574) et garde de lignée dans `lire_course` : refus (choix : refus plutôt que signalement, le nom nomme la sortie) ; mode deux courses : chemin, nom, lignée et empreintes différents, rien d'autre (consigne du coordinateur) ; essais « nom inconnu », « lignée contraire », « même course deux fois » ; mutations M18, M19 |
| RSL-05 (règle de (iii) dans le nom ; dossier fixé) | **fait** : `…-test-final-<règle>-v2` ; le nom vient du dossier `$PILOTE` (RSL-01) ; une copie de la branche `pilotes/<nom>` (sans suffixe) donne une sortie d'un autre nom, dit au § 5 |
| RSL-06 (Holm : famille gardée à 4 ou 2 avec un test impossible) | **gardé** (lecture du brief, la plus prudente ; la règle est écrite dans la sortie) ; essai « Holm avec un test impossible » |
| RSL-07 (secret refusé : toute la lecture refusée) | **gardé**, écart au texte déclaré (cohérent avec P4v3 et avec la garde 8 / 14 qui exige le secret) |
| RSL-08 (seuil provisoire) | aucune correction (le rapport n'en demande pas) ; libellé « provisoire, quatre tests au plus » gardé |
| RSL-09 (ligne d'état) | **fait** : comptes entiers « générations notées lues : K sur 4 ; signalements : N » ; code de sortie gardé à 0 quand une lecture est écrite (un code non nul avec des fichiers écrits brouillerait le sens de « refus ») ; essais « aucune génération notée » (0 sur 4) et « réponses absentes pour g2 » (3 sur 4) |
| RSL-10 (ligne d'erreur dans la bibliothèque standard) | **fait** : `ligne_du_script` (l. 1094) prend le dernier cadre dont le fichier est le script ; essai « récursion du décodeur JSON » vérifie que la ligne rapportée est celle qui appelle `json.loads` |
| RSL-11 (aide et noms à motif décimal) | **fait** : aide sans motif décimal (versions écrites `v6-2-s`, essai « aide ») ; un nom de fichier poussé recopié dans un motif de refus est remplacé par « <nom non recopié : il porte un motif décimal> » (`affichable`, l. 157 ; essai, mutation M22) ; le contrôle « aucun nombre décimal » vise les scores et proportions ; le nom du dossier de course ne peut pas porter de point |
| RSL-12 (interruption) | **fait** : `KeyboardInterrupt` attrapée (l. 1126), code 130, une ligne, aucune pile ; essai sous trace d'audit (interruption à l'ouverture de l'archive) |
| RSL-13 (coût de tarfile en flux) | **non fait** (facultatif) : lecteur propre non écrit ; ordre de grandeur dit au § 4 ; la vérification du flux borne désormais sa sortie décompressée à 1 Mio par appel (mémoire indépendante du taux de compression) |
| RSL-14 (libellé quand la référence vaut 1) | **fait** : verdict « impossible par construction (référence égale à 1) » et libellé propre dans le Markdown ; champ `ii_impossible_par_construction` |
| RSL-15 (tailles des membres lus) | **fait** : noms et empreintes seulement (l. 635) ; les membres rapportés sont ceux de la part (`score.json` dans `test`, `score-final.json` dans `test_final`, `reponses-lues.json` et le repli dans les deux) |
| RSL-16 (jeu partiel) | **fait** : écriture sous des noms provisoires (`.…en-cours-<pid>`, création exclusive) puis liens durs vers les noms définitifs, sans écraser ; toute erreur en cours retire ce que l'appel a créé (`ecrire_sorties`, l. 945) ; liens durs refusés par le système de fichiers (EPERM, EXDEV, EMLINK, ENOTSUP) : création exclusive directe ; essai « écriture incomplète » (erreur d'entrée-sortie simulée au troisième lien : SORTIE laissée vide) ; mutation M21 |
| RSL-17 (batterie) | **fait** : ajoutés la branche « au-dessus de la référence » (banque à classes de 40 et 30, bornes refaites en décimal), banque à identifiant en double, part absente, vérité hors étiquettes, JSON illisible ; liste d'empreintes à nom remontant, absolu, en double, fichier poussé en lien, liste vide ; membre en lien dur, sous la graphie `g0003`, données après le flux gzip, en-tête à taille négative, tar coupé net (deux cas) ; écritures suivies par une trace d'audit Python (ouvertures en écriture, création, liens, renommages, suppressions ; cas sain et cas d'interruption et d'erreur) |

Non traités : RSL-13 (dit ci-dessus) ; rien d'autre.

## 4. Ce qui reste incertain

- Structure de l'archive réelle, version du noyau (`8e5e2f7b`), `python3` et GNU tar du conteneur de session-depot :
  comme en v1 (§ 4 du LISEZMOI v1) ; si la structure diffère, la lecture est écrite « impossible » avec la ligne d'état
  « générations notées lues : 0 sur 4 », jamais fausse en silence.
- Le nom du dossier de la course S (`pilote4-gemini-v6-2-s-v1`, suffixe `-tentativeN` possible) vient du texte v5 et du
  coordinateur ; le lanceur v11 n'a pas été lu (non listé au brief).
- Coût (RSL-13) : trois décompressions par flux de l'archive (en-têtes, contrôle du flux et de la fin, membres) ; de
  l'ordre de 10 s par 256 Mio décompressés par passage tarfile d'après la relecture ; une archive de texte et de JSON se
  lit en quelques secondes.
- Les références restent des constantes des textes (0,8056 / 0,8333 ; 1,0 / 0,75 ; à côté 0,75 / 0,6944 et
  0,8889 / 0,8056) ; les effectifs par classe de la vraie banque ne sont pas vérifiés (les bornes maximales sont calculées
  sur les comptes réels).
- La phrase (iv) du texte (« aucune comparaison entre les deux objets ») est reprise telle quelle bien que les deux
  courses portent désormais le même objet ; Holm ordonne les valeurs p des deux courses sans en tirer de comparaison.

## 5. Commandes pour session-depot

`<R>` : dépôt du lanceur ; `<BANQUE_DIR>` : dossier qui porte `banque-confrontation-v3.json` et
`banque-confrontation-v3-secret.json`. Le dossier de course est **`$PILOTE` tel que le lanceur l'a fermé** (dernière ligne
du lanceur : « pilote fini : $PILOTE »), suffixe `-tentativeN` compris ; une copie de la branche `pilotes/<nom>` dans un
dossier nommé `<nom>` (sans suffixe) est acceptée mais donne des sorties nommées sans suffixe (R12 : ne pas mêler les
deux). Dans le dossier où sont copiés le script, ses essais et leurs compagnons :

```
sha256sum -c lire_pilote4_v2.py.sha256 essais_lire_pilote4_v2.py.sha256
unset LECTURE_PILOTE4_ESSAI_SEULEMENT_EMPREINTES_BANQUE
/opt/venv-essaim-sim-v1/bin/python -I essais_lire_pilote4_v2.py --noyau <R> --interpreteur-script "$(command -v python3)"   # facultatif
```

**Avant la fin de la course M** :

```
python3 -I -B lire_pilote4_v2.py essai-banque <BANQUE_DIR>
```

attendu, code 0 : `essai-banque : catégorie absente du train — test 8 (evaluation 4, usage-reel 4) ; test_final 14 (evaluation 10, usage-reel 4) ; issue : conforme`.

**À la fin de la course M** (liste fermée poussée, recherche des clés faite) :

```
python3 -I -B lire_pilote4_v2.py lecture <R>/pilotes/pilote4-gemini-v6-2-v1-tentative2 <BANQUE_DIR> <SORTIE_M>
```

écrit `lecture-pilote4-gemini-v6-2-v1-tentative2-test-v2.{json,md}` (ouvert à la lecture, N-050) et
`lecture-pilote4-gemini-v6-2-v1-tentative2-test-final-provisoire-v2.{json,md}` (à pousser sans l'afficher, jusqu'à la fin
du compteur), avec leurs compagnons.

**À la fin de la course S** (Holm sur les quatre tests ; les verdicts définitifs des deux tests de M sont dans ce
fichier `test_final`) :

```
python3 -I -B lire_pilote4_v2.py lecture <R>/pilotes/pilote4-gemini-v6-2-s-v1[-tentativeN] <BANQUE_DIR> <SORTIE_S> <R>/pilotes/pilote4-gemini-v6-2-v1-tentative2
```

écrit `lecture-pilote4-gemini-v6-2-s-v1[-tentativeN]-test-v2.*` et `…-test-final-holm-quatre-v2.*`.

**Si Lazar dit que la course S ne court pas** (Holm sur deux) :

```
python3 -I -B lire_pilote4_v2.py lecture <R>/pilotes/pilote4-gemini-v6-2-v1-tentative2 <BANQUE_DIR> <SORTIE_M2> --sans-seconde-course
```

(une autre SORTIE : le fichier `test` porterait le même nom que celui de la première lecture ; le script refuse d'écraser).
La sortie standard ne porte que `lecture écrite : <fichiers et empreintes> ; générations notées lues : K sur 4 ;
signalements : N` ; les fichiers `test_final` restent non affichés jusqu'à la fin du compteur (N-050), les fichiers `test`
s'ouvrent dès la fin de la course, sous la retenue de 03:27 tant que Lazar n'a pas tranché la question des graines.

## 6. Essais (R5, R4) et journal

`essais-lire-pilote4-v2.log` (de 05:10:16 à 05:14:47 UTC) : harnais sous `/opt/venv-essaim-sim-v1/bin/python -I`, script
lancé sous le même interpréteur (3.13.17), puis sous `/usr/bin/python3.11` (3.11.17) et `/usr/bin/python3.12` (3.12.3) :
**9 cas sains sur 9 et 58 artefacts sur 58 conformes, trois fois** ; aucun cache écrit dans le noyau importé ;
**22 copies altérées du script sur 22 détectées** (sous 3.13 ; dont (iii) recopié dans le fichier `test`, part
`test_final` lue à la place de `test`, fin d'archive non exigée, lignée ou nom non contrôlés, jeu partiel laissé, nom
décimal recopié). Données synthétiques seulement, dossiers de travail effacés. Valeurs refaites indépendamment pour g0,
délégation, `test_final` (9 / 12 et 6 / 12 justes : exactitude équilibrée 0,625 ; Wilson 0,4297–0,9228 et
0,2284–0,7716 par la racine en précision décimale, `bc -l` et `wilson_inferieur` du noyau ; combinées 0,3290–0,8472),
McNemar 1 / 128 (b = 0, c = 8) et 9 / 128 (b = 1, c = 7) par le triangle de Pascal, Holm pas à pas (quatre tests :
3 / 128, 9 / 64, 1 / 8192, 1 ; deux tests : 1 / 64, 9 / 128 ; avec deux tests impossibles : 1 / 32, 27 / 128),
sous-ensembles « catégorie absente du train » (8 et 14 tâches), bornes maximales 0,7818 et 0,7049, branche « au-dessus »
sur des classes de 40 et 30. Dans tous les cas : code, motif, une ligne sur la sortie standard, aucun motif
`[0-9][.,][0-9]` sur la sortie standard ni sur la sortie d'erreur, aucun fichier écrit ni modifié hors de SORTIE
(instantanés ; trace d'audit Python sur le cas sain à deux courses), aucun fichier provisoire laissé, séparation des deux
lectures vérifiée sur chaque lecture écrite.
