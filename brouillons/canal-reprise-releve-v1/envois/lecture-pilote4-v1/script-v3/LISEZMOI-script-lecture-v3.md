# Script de lecture contre le bruit du pilote 4 — LISEZMOI v3

L'auteur des v1 et v2 (sous-agent de la lignée conv-audit), relancé, 26 octobre 2026 ; cet en-tête est écrit à 07:10:17 UTC
(heure lue sur `date -u` dans la commande qui écrit ce fichier). La v3 remplace la v2, gardée intacte sous
`/var/tmp/lecture-pilote4-v2/` (ses quatre compagnons vérifiés : script `a2361320…`, essais `dee7e0fe…`, journal
`4aa9de04…`, LISEZMOI `2f328fee…`). Brief : `LISEZMOI-brief-script-v3.md`
(`78861f993bb1be63329a3a401ba405d3439ea6bb14d01305e5a0e36f4a260d9e`, vérifiée), appliqué tel quel. Pièces de `fournis/`,
vérifiées contre `EMPREINTES-fournis-v1.txt` : la seconde relecture `rapport-relecture-script-lecture-v2-sur-v2-v2.md`
(`3cdf052cfd0701d69510be79e4ade8b772f958b9d5ac21a7c9f5507b8c622ac3`, lue en entier, RSL2-01 à RSL2-08) ; la vérification
de la boucle extérieure `rapport-verification-boucle-exterieure-v3.md`
(`1a7873e269529e09de2b1ade0f4ca723383647b2bcc19966f7849e2d5af9fa6a`, CLB3-01, CLB3-06 et CLB3-07 lus) ; le texte v5 du
pilote `pilote4-gemini-organisme-v5.md` (`1943f39ada61db7d21e53b7e0c02c6e826b86e1467687eedbe56617877ab7f87` : table de
correspondance, l. 65 ; § Plan, points 3 et 4). Interdits tenus : aucun fichier de données de la banque, aucune archive ni
pièce d'un pilote réel ouvert, lu ou haché, aucun dossier `donnees/`, `runs/`, `diag/`, `pilotes/` ; aucun `git`, réseau,
sous-agent ni clé ; aucun score réel ; données synthétiques seulement ; écrit seulement sous `/var/tmp/lecture-pilote4-v3/` ;
Python lancé avec `-I` ; heures lues sur `date -u` dans la commande qui les écrit.

| fichier | sha256 |
|---|---|
| `lire_pilote4_v3.py` (bibliothèque standard seule ; Python 3.11, 3.12 et 3.13) | `4b943731f9490ae525a1cfb81744678b6483605aedb6aa20a7ace874ad256b99` |
| `essais_lire_pilote4_v3.py` | `7b8899cd4d308ae333809b15f5c51f773508ceeb20d967f080a0cd7991cb0422` |
| `essais-lire-pilote4-v3.log` | `c90965cb873d495a77c25288eb82804943d5325f56e039e263835b134f5193e1` |

Ce LISEZMOI a son empreinte dans son compagnon `LISEZMOI-script-lecture-v3.md.sha256`.

## 1. Ce qui change de la v2

1. **Plus de mode « provisoire »** (CLB3-01) : retiré, avec ses fichiers (`…-test-final-provisoire-v2`), son seuil 0,0125
   et ses libellés. Deux modes de lecture, chacun n'écrit que ses fichiers (plus `essai-banque`, inchangé) :
   - `test --course DOSSIER BANQUE_DIR SORTIE` — à la fin d'une course (M ou S) : `lecture-<dossier>-test-v3.{json,md}`,
     la part `test` seule ;
   - `test_final --course-m DOSSIER_M --course-s DOSSIER_S BANQUE_DIR SORTIE` — à la fin de la course S : pour **chacune**
     des deux courses, `lecture-<dossier>-test-final-holm-quatre-v3.{json,md}`, une course par fichier, Holm sur les quatre
     tests (deux par course), aucune valeur de l'autre course ;
   - `test_final --course-m DOSSIER_M --sans-seconde-course BANQUE_DIR SORTIE` — si la course S ne court pas ou ne finit
     pas saine : `lecture-<dossier de M>-test-final-holm-deux-v3.{json,md}`.
   `--course-s` et `--sans-seconde-course` s'excluent et l'un des deux est exigé (code 2 sinon). `--course-m` exige le
   dossier de la course M (`pilote4-gemini-v6-2-v1`, suffixe `-tentativeN` compris), `--course-s` celui de la course S
   (`pilote4-gemini-v6-2-s-v1`, idem) : options échangées, ou la même course deux fois, refusées (code 3). Chaque fichier
   a son compagnon `.sha256` (« empreinte, deux espaces, nom »).
2. **Tests (iii) d'un fichier `test_final`** (brief § 3, point 2, avec la correction de conv-audit) : pour chacun des deux
   tests de sa course, la valeur p brute (flottant et fraction exacte), les comptes « juste en g0 seulement » et « juste en
   g3 seulement », le **verdict**, mot pour mot celui du texte (point 4 bis) et de la v2 (champ `verdict`) :
   « changement au-delà du bruit des tâches » si Holm le rejette au niveau 0,05, sinon « dans le bruit des tâches »
   (« impossible » pour un test impossible), et le **sens du rejet**. La famille et le niveau vont dans un champ à part,
   `correction` : « Holm, quatre tests, niveau 0,05 », le même dans les deux fichiers `holm-quatre` (« Holm, deux tests,
   niveau 0,05 » en `holm-deux`), recopié dans le Markdown (« Correction : … »). Jamais la valeur p ajustée, ni le rang, ni
   le seuil appliqué (ils restent dans la mémoire du script : `appliquer_holm`, l. 840). La règle de décision est celle
   de la v2 (rejet si la valeur p ajustée de Holm est au plus 0,05 ; fonction `holm` inchangée).
3. **Sens du rejet** (CLB3-06 a) : « génération 3 au-dessus de la génération 0 » ou « génération 3 au-dessous de la
   génération 0 », écrit seulement quand le verdict est « changement au-delà du bruit des tâches » ; sinon (verdict « dans
   le bruit des tâches » ou « impossible ») « sans objet (non rejeté) » ; **« aucune tâche sans réponse » :
   oui ou non**, sur chaque ligne (famille, génération) de `test_final` et sur chaque ligne du sous-ensemble « catégorie
   absente du train » de `test_final` (« impossible (réponses par tâche absentes) » quand la génération n'a pas de réponses
   par tâche).
4. **Phrase (iv)** au texte v5, mot pour mot celle du brief (§ 3, point 5), dans les deux fichiers (règles, section (iv),
   champ `phrase_iv`) ; « point 4 bis du texte v4 ; texte v5 du pilote, table de correspondance et § Plan, point 4 (phrase
   (iv)) » partout où la v2 citait le seul texte v4.
5. **Ligne d'état** (RSL2-02, CLB3-07 b) : mode `test` : `lecture écrite : <2 fichiers et empreintes> ; générations
   notées lues : K sur 4 ; signalements (fichier test) : N`, N ne comptant que les signalements écrits dans le fichier
   `test` ; mode `test_final` : `lecture écrite : <fichiers et empreintes>`, sans aucun compte.
6. **Garde de séparation entre courses** (brief § 3, point 3 c) : `verifier_separation` (l. 1062), avant toute écriture,
   sur les octets mêmes à écrire ; ce qu'elle couvre est dit exactement au § 3.
7. RSL2-03 à RSL2-08, § 2. Garde « même course » : deux lignées absentes (aucune génération notée) ne sont plus tenues pour
   égales (défaut trouvé par l'essai « même course deux fois » ; deux courses distinctes sans génération notée sont lues).
8. Un fichier réel ne porte plus aucune mention d'essai : la clé `essai_empreintes_banque_surchargees` n'est écrite que
   lorsque la variable réservée aux essais est définie (la v2 l'écrivait toujours, à `false`).

**Calculs** : `wilson`, `borne_basse_maximale`, `compter`, `mcnemar_exact`, `holm`, `tests_mcnemar`, la règle « catégorie
absente du train » et sa garde 8 / 14, la lecture de la banque, des listes d'empreintes et du flux de l'archive sont ceux
de la v2, identiques (comparaison des arbres syntaxiques sans les chaînes de documentation). Fonctions touchées parce qu'un
point l'exige : `inventorier_archive`, `lire_membres` et `lire_course` (membres du seul mode, brief § 3, point 6 ;
RSL2-04) ; `depuis_reponses_lues` et `depuis_reponses_brutes` (écartées par part, identifiants inconnus à part, projection
`test` : RSL2-03, RSL2-04) ; `signalements_communs` et `lecture_de_la_part` (RSL2-03 ; « aucune tâche sans réponse ») ;
`nom_de_course` (rôle M ou S) ; `ecrire_sorties` (RSL2-05) ; `appliquer_holm` remplace `appliquer_regle` (point 2). Aucune
valeur calculée ne change : les essais refont à la main les mêmes valeurs qu'en v2 (§ 6).

## 2. Constat → traitement

| constat ou point | traitement |
|---|---|
| RSL2-01 (phrase (iv) au texte v4) | **fait** : `PHRASE_IV` (l. 126) mot pour mot celle du brief ; écrite dans les deux fichiers ; source citée « point 4 bis du texte v4 ; texte v5 du pilote, table de correspondance et § Plan, point 4 » (l. 131) ; essai : chaque fichier écrit porte la phrase du brief, recopiée à part dans le harnais ; mutation M28 (phrase du texte v4) détectée |
| RSL2-02 (ligne d'état qui compte des signalements de `test_final`) | **fait** : le mode `test` ne calcule pas la part `test_final` ; « signalements (fichier test) : N » (l. 1246) ; tous les signalements qui touchent `test_final` restent dans les fichiers `test_final` ; essai de la v2 qui exigeait le mélange adapté (« score du noyau altéré », N = 1, l'écart n'est que dans le fichier `test`) ; essai nouveau : anomalie de `score-final.json` seule, fichier `test` et ligne d'état inchangés |
| RSL2-03 (entrées écartées des deux parts) | **fait** : `depuis_reponses_lues` compte les entrées écartées par part et les identifiants hors de la banque à part (l. 480–504) ; « N entrée(s) … d'une tâche de cette part écartée(s) » dans le fichier de la part ; « identifiant hors de la banque » est un signalement commun (les deux fichiers) ; essais : entrée écartée d'une tâche de `test_final` (fichier `test` inchangé), de `test` (fichier `test` seul), identifiant inconnu (les deux) |
| RSL2-04 (empreinte croisée) | **fait** : le fichier `test` porte, pour `reponses-lues.json` (ou le repli), l'empreinte de la seule projection `test` (règle § 4) et, pour `score.json`, l'empreinte du fichier ; les fichiers `test_final` portent l'empreinte entière de `reponses-lues.json` et de `score-final.json` ; essais : projection refaite dans le harnais (lues et repli) ; réponses de `test_final` changées, fichier `test` identique hors de l'heure et des empreintes de la liste et de l'archive ; mutations M32, M33 |
| RSL2-05 (jeu partiel sans liens durs) | **fait** : le chemin définitif est ajouté à `definitifs` dès sa création exclusive, avant d'écrire (l. 1144) ; essai par injection dans le processus du script (liens durs refusés, moitié du troisième fichier écrite puis « plus de place ») : code 4, SORTIE vide ; mutation M26 |
| RSL2-06 (« non écrite » après l'écriture) | **fait** : dès que tous les fichiers définitifs sont en place, avant même le retrait des provisoires, `ETAT["ecrits"]` retient l'écriture (l. 1157) ; une interruption ensuite écrit `lecture écrite, interrompue avant la ligne d'état : <fichiers et empreintes>` et « les fichiers écrits sont complets », code 130 (l. 1337) ; une erreur ensuite, `lecture écrite, erreur interne avant la ligne d'état : …`, code 4 (l. 1346) ; un provisoire caché resté dans SORTIE est nommé (`reste_provisoire`, l. 1291) ; essais par injection : interruption sur la ligne d'état ; interruption, puis erreur d'entrée-sortie, au retrait des provisoires ; mutations M27, M46, M47 |
| RSL2-07 (documentation de la séparation) | **fait** : § 3 dit exactement ce que la séparation et ses essais couvrent, et ce qu'ils ne couvrent pas ; le fichier `test` ne porte plus « (iii) » ni « deux parts » (règle (ii) du fichier `test` sans la phrase sur (iii), l. 141) ; « toute erreur retire ce que l'appel a créé » est vrai sans liens durs (RSL2-05), à une fenêtre près dite au § 4 ; après la mise en place des définitifs, l'écriture est dite faite (RSL2-06) |
| RSL2-08 (essai de séparation par valeurs décimales ; drapeaux) | **fait** : paires de non-interférence (§ 3.3) comparant champ à champ JSON et Markdown, comptes, signalements et ligne d'état compris ; la trace d'audit du harnais lit le mode et les drapeaux d'ouverture (`os.open` compris) ; contrôle : une écriture par `os.open` hors de SORTIE est vue et bloquée |
| Brief § 3, point 1 (sorties ; plus de provisoire) | **fait** : modes `test` et `test_final` (§ 1, point 1) ; noms `lecture-<dossier>-test-v3`, `…-test-final-holm-quatre-v3` (un par course), `…-test-final-holm-deux-v3` ; commandes au § 5 |
| Brief § 3, point 2 (contenu d'un fichier `holm-quatre`) | **fait** : valeur p brute, verdict, sens ; ni valeur p ajustée, ni rang, ni seuil ; intervalles, cellules et sous-ensembles de la course seule ; essais : clés des tests limitées, aucune clé « ajust », « seuil », « rang » dans le JSON, ni ces mots dans le Markdown hors du texte de la règle (iii) ; mutation M23 |
| Correction de conv-audit au point 2 (message du coordinateur reçu pendant l'écriture : libellé inventé par le brief) | **fait** : le verdict d'un test (iii) reste mot pour mot celui du texte et de la v2, « changement au-delà du bruit des tâches » (rejeté sous Holm à quatre au niveau 0,05, à deux avec `--sans-seconde-course`), sinon « dans le bruit des tâches » ; « rejeté au niveau 0,05, famille de quatre » et « non rejeté » ne sont plus écrits comme libellés (une version intermédiaire les écrivait : son journal est gardé sous `anterieur/`, § 6) ; champ `correction` (« Holm, quatre tests, niveau 0,05 », identique dans les deux fichiers ; « Holm, deux tests, niveau 0,05 » en `holm-deux`) ; sens écrit seulement pour un verdict « changement au-delà du bruit des tâches », sinon « sans objet (non rejeté) » ; valeur p brute de la course seule, jamais d'ajustée, de rang ni de seuil ; ligne d'état inchangée (« signalements (fichier test) : N ») ; essais : verdicts refaits par Holm pas à pas, champ de la correction égal dans les deux fichiers, aucun « rejeté au niveau » ; mutations M48 (libellé inventé), M49 (correction propre à une course), M50 (sens écrit pour un test non rejeté) |
| Brief § 3, point 3 (séparation essayée) | **fait** : (a) paires S changée / M identique et réciproque ; (b) union des deux fichiers égale au calcul joint (McNemar par le triangle de Pascal, Holm pas à pas) ; (c) artefacts : valeurs, valeur p (trois écritures), borne, nom, lignée, empreinte, test, ligne (iii) du Markdown, comptes b et c, signalement de l'autre course plantés avant l'écriture : refus, rien d'écrit ; coïncidences : § 3.2 ; mutations M22, M34 à M39 |
| Brief § 3, point 4 (sens ; aucune tâche sans réponse) | **fait** (§ 1, point 3) ; écart de notation déclaré au § 4 ; mutations M24, M29, M45 |
| Brief § 3, point 5 (phrase (iv)) | **fait** (RSL2-01) |
| Brief § 3, point 6 (ligne d'état ; signalements de `test_final`) | **fait** (RSL2-02) ; le mode `test` ne voit pas `score-final.json` (ni inventaire, ni contrôle, ni lecture) ; essais : `score-final.json` en lien symbolique ou imbriqué à l'excès, ignoré par le mode `test`, refusé ou en erreur par le mode `test_final` ; mutations M16, M25 |
| Brief § 3, point 7 (RSL2-03) | **fait** |
| Brief § 3, point 8 (RSL2-04) | **fait** ; règle de la projection au § 4 |
| Brief § 3, point 9 (RSL2-05 à RSL2-08) | **fait** |
| Brief § 3, point 10 (délégation sur `test`) | **inchangé** : « impossible par construction (référence égale à 1) », mot pour mot ; essai ; mutation M44 |
| Brief § 3, point 11 (en-tête du Markdown `test_final`) | **fait** : « **Part `test_final` : à ne pas afficher avant la fin du compteur de rondes de la boucle extérieure (N-050) ; lue une seule fois.** » ; essai sur chaque fichier `test_final` ; mutation M43 |
| CLB3-01 (a) noms ; (b) contenu ; (c) garde du partage | (a) et (b) : points 1 et 2 ; (c) : la garde et ses essais ; le fichier `test` ne porte ni « test_final », ni « (iii) », ni « valeur p », ni aucune mention d'essai hors des deux marques que seule la variable réservée aux essais fait écrire (vérifié sur chaque fichier `test` des essais ; en lecture réelle, sans la variable, ces marques ne sont pas écrites) |
| CLB3-06 (a) libellés ; (c) délégation ; (d) (iv) | (a) point 4 ; (c) libellé exact : « impossible par construction (référence égale à 1) » ; (d) point 5 ; (b) relève du registre, rien au script |
| CLB3-07 (b) ligne d'état | point 6 ; (a) relève du protocole |

## 3. Séparation : ce qu'elle couvre, exactement (RSL2-07)

### 3.1 Entre les parts d'une course

- Le mode `test` ne voit, dans l'archive, que `course/archive/<lignée>/gNNN/juge/{reponses-lues.json, reponses_test.json,
  score.json}` (`MEMBRE_NECESSAIRE["test"]`, l. 115) ; `score-final.json` n'y est ni inventorié, ni contrôlé (type, double,
  taille), ni lu, ni haché. `reponses_test.json` n'est lu que si `reponses-lues.json` manque (repli). Des réponses, seules
  celles des tâches de `test` entrent dans les tableaux et le sous-ensemble.
- Le fichier `test` dépend de la part `test_final` par trois champs seulement, qui décrivent l'archive entière : l'empreinte
  de `EMPREINTES-pilote-v1.txt`, celle de `ferme.tar.gz` (non renversables) et le nombre de membres de l'archive (le même
  quel que soit le contenu des réponses). Tout le reste est fonction de la part `test`, de la banque (empreintes de la
  banque publique et du secret, comptes de la règle de catégorie) et des faits mécaniques communs (dont les contrôles de
  l'archive entière : chemins des membres, flux compressé, fin d'archive, lignées ; un refus à ce titre vaut pour les
  deux modes).
- Signalements communs (écrits dans les fichiers des deux parts, parce qu'ils décrivent des fichiers qui servent les deux) :
  générations notées trouvées autres que 0 à 3, aucune génération notée, génération sans réponses par tâche lisibles,
  repli sur `reponses_test.json`, identifiants hors de la banque. Tous les autres sont écrits dans le fichier de leur part
  seulement : écart avec le noyau, score du noyau absent, illisible ou sans la famille (`score.json` pour `test`,
  `score-final.json` pour `test_final`), entrées écartées d'une tâche de la part, test (iii) impossible.
- Ligne d'état : en mode `test`, le nombre de générations lues (fait commun) et les signalements du fichier `test` ; en
  mode `test_final`, des noms et des empreintes seulement.
- Le fichier `test_final` ne lit pas `score.json` et ne porte aucune valeur de `test` ; il porte l'empreinte entière de
  `reponses-lues.json`, qui couvre aussi les réponses de `test` (non renversable ; la part `test` est ouverte plus tôt).

### 3.2 Entre les deux courses (fichiers `holm-quatre`)

- Chaque fichier est rendu d'un document qui ne contient que sa course. La seule donnée de l'autre course qui entre dans
  un calcul est la paire de ses valeurs p, pour Holm sur les quatre tests (l. 1261) ; il n'en sort, dans le fichier
  d'une course, que les deux verdicts de cette course. Par construction de Holm, un verdict dit si la famille a laissé
  passer ce test : c'est l'information que Holm sur quatre exige ; aucune valeur de l'autre course n'est écrite.
- Avant toute écriture, sur les octets mêmes qui seront écrits, `verifier_separation` relit chacun des deux fichiers contre
  le document de l'autre course et refuse (code 3, « séparation entre courses : le fichier de <course> porterait <quoi> de
  l'autre course — rien n'est écrit ») si :
  1. **tests (iii), donc comptes b et c, valeurs p, verdicts et sens** : le JSON ne porte pas exactement les tests de sa course
     (au nombre attendu, chacun marqué de la course et de la lignée du fichier, égaux champ à champ à ceux calculés pour
     elle), ou le Markdown ne porte pas exactement les lignes (iii) de ces tests, ou une section de l'autre course paraît ;
  2. **noms** : le nom du dossier ou la lignée de l'autre course paraît (recherche bornée : la lignée de M est un préfixe
     de celle de S) ;
  3. **signalements** : un signalement de l'autre course qui n'est pas aussi un signalement de la course du fichier ;
  4. **empreintes** : une empreinte de l'autre course qui n'est pas aussi une empreinte de la course du fichier (liste,
     archive, membres lus) ;
  5. **valeurs** : une proportion de l'autre course (exactitude équilibrée, bornes d'intervalle, exactitude et part sans
     réponse du sous-ensemble) ou une de ses valeurs p, sous chacune des écritures du script (JSON ; quatre décimales à
     virgule ; valeur p à six chiffres significatifs ; fraction exacte).
- **Coïncidences** : une valeur de l'autre course n'est cherchée que si elle n'est égale à **aucun nombre du document de
  la course du fichier** (ses mesures, ses références, ses bornes) : une valeur commune aux deux courses, ou égale à une
  constante (par exemple une exactitude de S égale à la référence 0,8333, une borne de S égale à la borne maximale
  0,7049), est déjà légitimement dans le fichier et ne déclenche rien. Les valeurs 0 et 1 et les jetons qui sont dans les
  textes fixes du script (règles, libellés) ne sont pas cherchés ; chaque recherche est bornée (pas de chiffre, point,
  virgule ou barre collé avant ; pas de chiffre ni de barre après). Les proportions sont arrondies à quatre décimales avant
  d'être écrites : deux proportions différentes ont deux écritures différentes. Fausse alerte possible en théorie : une
  valeur p de l'autre course dont l'écriture à six chiffres égalerait celle d'une valeur p différente du fichier, ou un
  signalement de l'autre course contenu tel quel dans un texte du fichier ; ce serait un refus, jamais une fuite.
- **Non cherché comme texte** : les autres entiers (effectifs, justes, sans réponse, membres) : ils coïncident avec ceux
  de la course même ; ils ne s'écrivent que dans les tableaux rendus du seul document de la course.

### 3.3 Ce que les essais vérifient (§ 6 pour les nombres)

- **Paires de non-interférence** (deux lectures qui ne diffèrent que par une part, ou que par l'autre course ; le fichier
  gardé fixe est comparé champ à champ en JSON et texte à texte en Markdown, l'heure ôtée) :
  - part `test_final` de S changée (valeurs p 1/8192 et 1/64), verdicts de M inchangés : fichier `holm-quatre` de M
    identique, l'heure à part ; réciproque (part `test_final` de M changée : justes, et non-réponses ajoutées en g1 et g2,
    12,5 % à 16,7 % par famille ; valeur p 1/32, « dans le bruit des tâches »), verdicts de S inchangés : fichier de S identique, l'heure
    à part ;
  - tests de S impossibles (S sans g3), verdicts de M inchangés : fichier de M identique ;
  - part `test_final` de M changée : fichier `test` identique hors de l'heure et des empreintes de la liste et de
    l'archive (projection et `score.json` compris), ligne d'état identique ; réciproque : part `test` changée, fichier
    `test_final` identique hors de l'heure, des empreintes de la liste, de l'archive et de `reponses-lues.json` ;
  - anomalie de `score-final.json` seule ; entrée écartée d'une tâche de `test_final` ; `score-final.json` en lien
    symbolique : fichier `test` et ligne d'état identiques ; l'anomalie n'est que dans le fichier `test_final` (ou le mode
    `test_final` refuse).
- **Union** : les quatre tests des deux fichiers `holm-quatre` égalent le calcul joint refait dans le harnais (comptes,
  valeurs p par le triangle de Pascal, verdicts par Holm pas à pas, sens, champ de la correction).
- **Recherches indépendantes de la garde** : aucune valeur d'une part dans le fichier de l'autre ; aucune valeur propre à
  une course dans le fichier de l'autre (12 propres à S, 19 propres à M) ; des coïncidences existent et ne déclenchent
  pas de refus (8 valeurs mesurées dans les deux courses, 2 mesures de S égales à une constante de M).
- **Artefacts de la garde** (injection dans le processus du script, juste avant l'écriture) : valeur p de S (JSON,
  Markdown, fraction), deux proportions et une borne de S dans M, une proportion de M dans S, nom de S, lignée de M dans S,
  empreinte de l'archive de S, test (iii) de S ajouté, sa seule ligne du Markdown (sa valeur p égale à une valeur p de M :
  vue par la structure, pas par la recherche de valeurs), ses comptes b et c dans un test de M, un signalement propre à
  S : refus, code 3, SORTIE vide. Une mutation par élément de la garde (M34 à M39) et la garde retirée (M22) sont
  détectées.
- **Mots** : chaque fichier `test` est relu : ni « test_final », ni « test-final », ni « (iii) », ni « valeur p », ni
  « McNemar », ni « Holm », ni « seconde », ni « provisoire », ni « objets », ni mention d'essai hors de la marque
  d'essai, ni l'autre course.

## 4. Ce qui reste incertain ; écarts déclarés

1. **Notation du sens** : le brief écrit « au-dessus (b > c) ». Le script n'écrit jamais b ni c ; il dit les comptes en
   mots, et « au-dessus » quand les tâches justes en génération 3 seulement sont plus nombreuses que les tâches justes en
   génération 0 seulement (`juste_en_g3_seulement` > `juste_en_g0_seulement`), règle écrite dans chaque fichier
   (`NOTE_SENS`, l. 165). Lu au sens (la génération 3 fait mieux), c'est ce que dit le sens écrit ; si conv-audit tient b pour
   « juste en g0 seulement », le « (b > c) » du brief inverserait le sens : je l'ai pris pour une notation à l'envers.
   Égalité des deux comptes : valeur p 1, jamais rejeté, donc « sans objet ».
2. **Holm** : famille gardée à quatre (ou deux) quand un test est impossible ; un test impossible n'est jamais rejeté
   (RSL-06, lecture du brief, inchangée) ; essai : avec deux tests de S impossibles, le test de M à p = 1/64 reste « dans
   le bruit des tâches » (une famille réduite à deux l'aurait rejeté).
3. Les fichiers `holm-deux` omettent aussi valeur p ajustée, rang et seuil (le brief le dit des `holm-quatre`) ; leur champ
   `correction` est « Holm, deux tests, niveau 0,05 ». Un test impossible a pour sens « sans objet (non rejeté) » (lecture
   littérale de la correction : le sens n'est écrit que pour un verdict « changement au-delà du bruit des tâches »).
4. « Aucune tâche sans réponse » est aussi écrit sur les lignes du sous-ensemble de `test_final`, et vaut « impossible
   (réponses par tâche absentes) » pour une génération sans réponses par tâche.
5. **Garde de séparation** : fausse alerte possible en théorie (§ 3.2), jamais une fuite ; si elle refuse sur les vraies
   courses, rien n'est écrit et le motif dit la catégorie, sans valeur.
6. **Écriture** : sans liens durs, il reste une fenêtre de deux instructions entre la création exclusive d'un fichier et
   son inscription dans `definitifs` (une interruption au clavier exactement là laisserait un fichier vide). Sur un système
   de fichiers à liens durs, ce chemin n'est pas pris.
7. **Projection `test` des réponses** (RSL2-04) : sha256 du JSON canonique (`json.dumps(objet, ensure_ascii=False,
   sort_keys=True, separators=(",", ":"))`, encodé en UTF-8) de l'objet `{identifiant: valeur}` restreint aux identifiants
   des tâches de la part `test` de la banque, valeurs recopiées telles qu'elles sont dans le fichier (objet `reponses` de
   `reponses-lues.json` ; objet racine de `reponses_test.json` en repli, chaque valeur étant l'objet de l'organisme). Pour
   un repli illisible, non objet ou trop grand : « sans objet (…) » ou « non lu (…) ». Règle écrite aussi dans chaque
   fichier `test`.
8. Comme en v2 : structure de l'archive réelle, version du noyau (`8e5e2f7b`), `python3` et GNU tar du conteneur de
   session-depot non vérifiables ici ; si la structure diffère, la lecture est écrite « impossible », jamais fausse en
   silence. RSL-13 (coût de `tarfile` en flux) non traité ; références et bornes : constantes des textes, comme en v2.
9. Le mode `test_final` relit les deux dossiers fermés ; si la course S est refusée (archive ou empreintes), rien n'est
   écrit : la variante `--sans-seconde-course` est une décision (la course S « ne court pas ou ne finit pas saine »), pas
   un repli du script.

## 5. Commandes pour session-depot

Dossiers réels de la copie de lancement (brief § 4) ; chaque commande écrit dans un dossier de sortie **nouveau** (le
script refuse d'écraser) ; sa sortie standard est redirigée dans un fichier poussé sans être lu ; la sortie d'erreur
aussi (elle ne porte jamais de score : motifs de refus, type et ligne d'une erreur interne, noms de fichiers). Le code de sortie (0
écrit ; 2 usage ; 3 refus ; 4 erreur interne ; 130 interrompu) peut être affiché.

```
R=essaim-m3-refonte-v1                                   # copie de lancement
COURSE_M="$R/pilotes/pilote4-gemini-v6-2-v1-tentative2"
COURSE_S="$R/pilotes/pilote4-gemini-v6-2-s-v1"
BANQUE_DIR=<dossier qui porte banque-confrontation-v3.json et banque-confrontation-v3-secret.json>
LECTURE=<dossier où sont copiés lire_pilote4_v3.py et lire_pilote4_v3.py.sha256>
SORTIES=<dossier existant où naissent les dossiers de sortie>
unset LECTURE_PILOTE4_ESSAI_SEULEMENT_EMPREINTES_BANQUE
(cd "$LECTURE" && sha256sum -c lire_pilote4_v3.py.sha256)
```

Facultatif, avant la première lecture (n'imprime que les comptes 8 et 14 et l'issue ; aucune valeur) :

```
python3 -I -B "$LECTURE/lire_pilote4_v3.py" essai-banque "$BANQUE_DIR"
```

**1. À la fin de la course M — part `test` de M :**

```
SORTIE_TEST_M="$SORTIES/lecture-test-M-v3"
python3 -I -B "$LECTURE/lire_pilote4_v3.py" test --course "$COURSE_M" "$BANQUE_DIR" "$SORTIE_TEST_M" \
  > "$SORTIES/etat-lecture-test-M-v3.txt" 2> "$SORTIES/erreurs-lecture-test-M-v3.txt"; echo "code $?"
```

écrit `lecture-pilote4-gemini-v6-2-v1-tentative2-test-v3.{json,md}` et leurs compagnons.

**2. À la fin de la course S — part `test` de S :**

```
SORTIE_TEST_S="$SORTIES/lecture-test-S-v3"
python3 -I -B "$LECTURE/lire_pilote4_v3.py" test --course "$COURSE_S" "$BANQUE_DIR" "$SORTIE_TEST_S" \
  > "$SORTIES/etat-lecture-test-S-v3.txt" 2> "$SORTIES/erreurs-lecture-test-S-v3.txt"; echo "code $?"
```

écrit `lecture-pilote4-gemini-v6-2-s-v1-test-v3.{json,md}` et leurs compagnons.

**3. À la fin de la course S — part `test_final` des deux courses (Holm sur quatre) :**

```
SORTIE_FINAL="$SORTIES/lecture-test-final-holm-quatre-v3"
python3 -I -B "$LECTURE/lire_pilote4_v3.py" test_final --course-m "$COURSE_M" --course-s "$COURSE_S" "$BANQUE_DIR" "$SORTIE_FINAL" \
  > "$SORTIES/etat-lecture-test-final-holm-quatre-v3.txt" 2> "$SORTIES/erreurs-lecture-test-final-holm-quatre-v3.txt"; echo "code $?"
```

écrit `lecture-pilote4-gemini-v6-2-v1-tentative2-test-final-holm-quatre-v3.{json,md}` et
`lecture-pilote4-gemini-v6-2-s-v1-test-final-holm-quatre-v3.{json,md}`, avec leurs compagnons : à pousser sans les
afficher, jusqu'à la fin du compteur de rondes (N-050).

**Variante — la course S ne court pas ou ne finit pas saine (Holm sur deux), au lieu de la commande 3 :**

```
SORTIE_FINAL_M="$SORTIES/lecture-test-final-holm-deux-v3"
python3 -I -B "$LECTURE/lire_pilote4_v3.py" test_final --course-m "$COURSE_M" --sans-seconde-course "$BANQUE_DIR" "$SORTIE_FINAL_M" \
  > "$SORTIES/etat-lecture-test-final-holm-deux-v3.txt" 2> "$SORTIES/erreurs-lecture-test-final-holm-deux-v3.txt"; echo "code $?"
```

écrit `lecture-pilote4-gemini-v6-2-v1-tentative2-test-final-holm-deux-v3.{json,md}` et leurs compagnons.

Le nom de chaque sortie vient du nom du dossier de course (`$PILOTE` tel que le lanceur l'a fermé) ; un dossier d'un
autre nom que les deux courses du pilote, avec ou sans `-tentativeN`, est refusé. Les essais (`essais_lire_pilote4_v3.py`)
demandent le noyau importé en lecture, `bc` et un dossier de travail écrit à côté d'eux ; ils sont facultatifs chez
session-depot.

## 6. Essais (R5, R4) et journal

`essais-lire-pilote4-v3.log` (ouvert à 06:58:26, fermé à 07:10:05 UTC ; heures lues sur `date -u` ; écrit sous
`set -C`) : harnais sous `/opt/venv-essaim-sim-v1/bin/python -I` (3.13.17) ; script lancé sous le même interpréteur, avec
les mutations, puis rejoué sous `/usr/bin/python3.11` (3.11.17), `/usr/bin/python3.12` (3.12.3) et `/usr/bin/python3`
(3.13.17, le `python3` du système) : **18 sur 18 cas sains et 64 sur 64 artefacts conformes, quatre fois** ; aucun cache
écrit dans le noyau importé ; **50 sur 50 copies altérées du script détectées** (sous 3.13 ; deux à la fois, chacune
dans son dossier, effacé). Données synthétiques seulement ; dossiers de travail effacés. Commandes du journal, depuis
ce dossier : `/opt/venv-essaim-sim-v1/bin/python -I essais_lire_pilote4_v3.py --mutations --paralleles 2`, puis
`… essais_lire_pilote4_v3.py --interpreteur-script <python>` pour chaque rejeu ; chaque ligne d'en-tête du journal porte
son heure (`date -u`) et les empreintes du script et des essais.

Valeurs refaites indépendamment : g0, délégation, `test_final` de M (9 / 12 et 6 / 12 justes, 2 sans réponse) :
exactitude équilibrée 0,625 ; Wilson 0,4297–0,9228 et 0,2284–0,7716 par la racine en précision décimale, par `bc -l`
lancé pendant l'essai et par `wilson_inferieur` du noyau ; combinées 0,3290–0,8472 ; bornes maximales 0,7818 et 0,7049
(`bc`) ; chaque ligne des deux parts et des deux courses recoupée avec `taches.evaluer` et
`analyse.exactitude_equilibree` ; sous-ensembles « catégorie absente du train » de 8 et 14 tâches (`test` g3 : 1 / 0
justes, 0,125 ; `test_final` g0 : 2 / 0 justes, 1 sans réponse, part 0,0714, 0,1, « non » ; g3 : 6 / 0, 0,3) ; McNemar par
le triangle de Pascal : M 1/128 (0 et 8) et 9/128 (1 et 7), S 1/32768 (0 et 16) et 1/128 (8 et 0) ; Holm sur quatre pas à
pas : « changement au-delà du bruit des tâches » pour la conscience de M et les deux familles de S, « dans le bruit des
tâches » pour la délégation de M (sens « au-dessus » pour les deux consciences, « au-dessous » pour la délégation de S,
« sans objet (non rejeté) » pour la délégation de M) ; Holm sur deux : conscience de M seule ; famille gardée à quatre :
M à 1/64 « dans le bruit des tâches » avec deux tests de S impossibles ; branche « au-dessus de la référence » sur des classes de 40 et 30 ;
projection `test` des réponses refaite (lues et repli). Dans chaque cas : code, motif, une ligne sur la sortie standard,
aucun motif `[0-9][.,][0-9]` sur la sortie standard ni sur la sortie d'erreur, aucun fichier écrit ni modifié hors de
SORTIE (instantanés du dossier de travail et du dossier des essais ; trace d'audit sur chaque cas lancé sans injection),
dossier courant vide, aucun fichier provisoire laissé (hors de l'essai qui le provoque).

Sous `anterieur/` : le premier journal complet (`essais-lire-pilote4-v3-avant-correction-point2.log`, `c16d87760e53a9250370a43acecc7a6e3b553dfbd5664a37f80933e267d8a167`,
et son compagnon), tenu de 06:39:39 à 06:51:11 UTC sur une version intermédiaire du script (`13c7e949…`) qui écrivait
encore les libellés « rejeté au niveau 0,05, famille de quatre » et « non rejeté » ; mêmes issues (18 et 64 conformes,
quatre fois ; 47 mutations sur 47) ; remplacé par le journal ci-dessus après la correction de conv-audit ; gardé (R12),
non livré.

**Essais de la v2 retirés parce qu'ils portaient sur le mode provisoire** : dans « lecture d'une course (M) », le mode
`provisoire`, la famille de deux, les verdicts au seuil 0,0125 (« changement au-delà du bruit des tâches (provisoire…) »,
« dans le bruit des tâches (provisoire…) ») et le seuil écrit ; les noms `…-test-final-provisoire-v2` attendus dans les
cas « lecture d'une course », « repli », « au-dessus » et dans les artefacts d'archive (ces cas lisent désormais en mode
`test` ou `test_final`). **Retirés parce que le format qu'ils vérifiaient n'existe plus** (brief § 3, points 1 et 2) :
« lecture avec la seconde course (S) : Holm sur quatre » (un fichier portant les quatre tests, la section `seconde_course`
et les valeurs p ajustées 3/128, 9/64, 1/8192, 1), « course S en premier, M en seconde » (l'ordre est fixé par
`--course-m` et `--course-s`), les valeurs p ajustées de « Holm sur deux » (1/64, 9/128) et de « Holm avec un test
impossible » (1/32, 27/128) : remplacés par les verdicts, refaits par Holm pas à pas. **Adaptés** : « score du noyau
altéré » (RSL2-02 : N = 1, écart dans le seul fichier `test`), « entrée hors banque » (RSL2-03 : trois essais),
« interruption au clavier » (avant et après l'écriture, RSL2-06), « écriture incomplète » (avec et sans liens durs,
RSL2-05), « seconde course et --sans-seconde-course » et « usage » (options des deux modes), « un compagnon déjà
présent » (nom `holm-quatre`).
