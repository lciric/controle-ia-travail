# Script de lecture contre le bruit du pilote 4 — LISEZMOI v4

L'auteur des v1 à v3 (sous-agent de la lignée conv-audit), relancé, 26 octobre 2026 ; cet en-tête est écrit à 08:33:17 UTC
(heure lue sur `date -u` dans la commande qui écrit ce fichier). La v4 remplace la v3, gardée intacte sous
`/var/tmp/lecture-pilote4-v3/` (compagnons vérifiés : script `4b943731…`, essais `7b8899cd…`, journal `c90965cb…`,
LISEZMOI `1dc0f72f…`), après la relecture de la v3 (`/var/tmp/relecture-script-lecture-pilote4-v3/rapport-relecture-script-lecture-v3.md`,
`fcd438547958dadfc791445d7458e9784859b213a180e36221a975ec3ca6ff40`, égale à son compagnon ; RSL3-01, RSL3-02, O1 à O3
lus) et la demande de conv-audit (v4 courte ; points 1 à 5). Interdits tenus : aucune donnée de la banque, aucune archive
ni pièce d'un pilote réel ; aucun `git`, réseau, sous-agent ni clé ; données synthétiques seulement ; écrit seulement sous
`/var/tmp/lecture-pilote4-v4/` ; Python avec `-I` ; heures lues sur `date -u`.

| fichier | sha256 |
|---|---|
| `lire_pilote4_v4.py` (bibliothèque standard seule ; Python 3.11, 3.12 et 3.13) | `a2d09ef6706fdf7f2f2b8a081a7a8f35e173c33e73e6da2c32f10af98e05ea9a` |
| `essais_lire_pilote4_v4.py` | `ea95b6a6517feeaf99bdf844c77b08a6ce3b6950cdfc3d54bc927471940da232` |
| `essais-lire-pilote4-v4.log` | `7a9b798b795ef57487616f787730571a563fc1810e33ca3151b0dd03c9787c0e` |

Ce LISEZMOI a son empreinte dans son compagnon `LISEZMOI-script-lecture-v4.md.sha256`.

## 1. Ce qui change de la v3

La garde de séparation entre courses (RSL3-01, `verifier_separation`, l. 1068 ; l. 1110 et 1121) et le suffixe
des noms : le script écrit `lecture-<dossier>-test-v4`, `…-test-final-holm-quatre-v4` et `…-test-final-holm-deux-v4`
(JSON, Markdown, compagnons). Rien d'autre : arbres syntaxiques de la v3 et de la v4 comparés, seules diffèrent
`verifier_separation` et les chaînes qui portent la version (`VERSION`, titres, noms de sortie, aide) ; calculs, modes,
options, contenus et ligne d'état inchangés. Le LISEZMOI v3 vaut pour la v4 (en lisant « -v4 » pour « -v3 »), sauf son
§ 3.2, remplacé par le § 3 ci-dessous, son § 4, points 1 et 6, remplacés par les § 4 et § 6, et son § 5, remplacé par le
§ 5.

## 2. Constat → traitement

| constat ou point | traitement |
|---|---|
| RSL3-01 (fausse alerte de la garde : score du noyau divergent écrit comme une proportion de l'autre course) | **fait**, par la correction de la relecture : avant de chercher une écriture de l'autre course, la garde écarte toute écriture égale à celle d'un nombre du document de la course du fichier (JSON, quatre décimales, six chiffres significatifs, fraction exacte des valeurs p), score du noyau compris (l. 1110–1121). Essais ajoutés, cas de la relecture : scores du noyau de M et de S divergents, chacun écrit à quatre décimales comme une proportion propre à l'autre course : lecture finale écrite, écarts signalés, aucun refus ; toutes les écritures propres à l'autre course plantées une à une, dans le processus du script, dans les deux sens : toutes refusées (§ 3). Mutation M51 (la garde de la v3) détectée. § 3.2 du LISEZMOI récrit (§ 3) |
| RSL3-02 (a) (code 4 ou 130 après une écriture complète) | **fait** : § 5, après les commandes |
| RSL3-02 (b) (fenêtre aussi pour les provisoires) | **fait** (documentation, code inchangé : point 5) : § 6 |
| RSL3-02 (c) (`R` relatif) | **fait** : § 5, avant les commandes |
| O1 (verdict et valeur p brute d'un fichier `holm-quatre`) | **fait** (décision de conv-audit : la valeur p brute reste) : § 4, une phrase |
| O2 (notation du sens) | **fait** : § 4 définit en mots les colonnes « juste en g0 seulement » et « juste en g3 seulement » ; ce LISEZMOI n'emploie pas de lettres pour elles |
| O3 (libellés attendus par la boucle) | rien au script : il écrit, pour un test (iii), « changement au-delà du bruit des tâches », « dans le bruit des tâches » ou « impossible » (inchangé depuis la v3) |
| Point 5 (rien d'autre ne change ; calculs inchangés) | **tenu** : § 1 |

## 3. Séparation entre les deux courses (fichiers `holm-quatre`) — remplace le § 3.2 du LISEZMOI v3

- Chaque fichier est rendu d'un document qui ne contient que sa course. La seule donnée de l'autre course qui entre dans
  un calcul est la paire de ses valeurs p, pour Holm sur les quatre tests (l. 1274) ; il n'en sort, dans le fichier
  d'une course, que les deux verdicts de cette course (ce qu'un verdict dit de l'autre course : § 4).
- Avant toute écriture, sur les octets mêmes qui seront écrits, `verifier_separation` relit chacun des deux fichiers contre
  le document de l'autre course et refuse (code 3, « séparation entre courses : le fichier de <course> porterait <quoi> de
  l'autre course — rien n'est écrit ») si :
  1. **tests (iii)** (les deux comptes, valeurs p, verdicts, sens) : le JSON ne porte pas exactement les tests de sa course
     (au nombre attendu, chacun marqué de la course et de la lignée du fichier, égaux champ à champ à ceux calculés pour
     elle), ou le Markdown ne porte pas exactement les lignes (iii) de ces tests, ou une section de l'autre course paraît ;
  2. **noms** : le nom du dossier ou la lignée de l'autre course paraît (recherche bornée : la lignée de M est un préfixe
     de celle de S) ;
  3. **signalements** : un signalement de l'autre course qui n'est pas aussi un signalement de la course du fichier ;
  4. **empreintes** : une empreinte de l'autre course qui n'est pas aussi une empreinte de la course du fichier ;
  5. **valeurs** : une écriture d'une proportion de l'autre course (exactitude équilibrée, bornes d'intervalle, exactitude
     et part sans réponse du sous-ensemble) ou d'une de ses valeurs p, sous les écritures du script (JSON ; quatre
     décimales à virgule ; valeur p à six chiffres significatifs ; fraction exacte).
- **Ce qui n'est pas cherché** (coïncidences) : une valeur de l'autre course égale à un nombre du document du fichier ; et
  (RSL3-01) toute écriture égale à l'écriture d'un nombre de ce document, sous l'une des écritures du script, **score du
  noyau compris** (le document le garde entier, le Markdown l'écrit à quatre décimales : un score du noyau qui diverge de
  la recomputation, cas que la lecture écrit et signale, peut avoir l'écriture d'une proportion de l'autre course). Une
  telle écriture, si elle paraît, est celle d'un nombre de la course du fichier : indiscernable, elle ne porte rien de
  l'autre course. Ne sont pas cherchés non plus : 0 et 1, les jetons des textes fixes du script (règles, libellés), les
  entiers autres que les comptes des tests (effectifs, justes, sans réponse, membres : ils ne s'écrivent que dans les
  tableaux rendus du seul document du fichier). Chaque recherche est bornée (pas de chiffre, point, virgule ou barre collé
  avant ; pas de chiffre ni de barre après).
- **Fausses alertes** : celle de RSL3-01 est retirée. Deux valeurs p différentes de même écriture à six chiffres ne se
  rencontrent pas aux effectifs réels (relecture : 321 valeurs p possibles à 36 paires au plus, 321 écritures). Reste,
  en théorie, un signalement de l'autre course contenu tel quel dans un texte du fichier : un refus, jamais une fuite.
- **Essais** (§ 7) : les paires de non-interférence, l'union, les recherches indépendantes et les plantations de la v3
  (LISEZMOI v3, § 3.3), et deux cas de la relecture : (a) scores du noyau de M (g2, conscience d'évaluation) et de S (g1,
  contrôle de délégation) mis à une valeur dont l'écriture à quatre décimales égale celle d'une proportion propre à
  l'autre course : lecture finale écrite (code 0), « écart avec le noyau » signalé dans chaque fichier, aucun refus ;
  (b) dans le processus du script, avant l'écriture, chaque écriture d'une valeur de l'autre course absente du fichier
  sain, plantée seule dans le JSON ou le Markdown, dans les deux sens : courses saines, 64 plantées et 64 refusées ;
  scores du noyau divergents, 62 plantées et 62 refusées ; mêmes nombres sous chacun des quatre interpréteurs essayés ; la
  lecture saine est ensuite écrite.

## 4. Lecture des tests (iii) (O1, O2) — remplace le § 4, point 1, du LISEZMOI v3

- **« juste en g0 seulement »** : nombre de tâches de la famille, dans la part `test_final`, auxquelles la génération 0
  répond juste et la génération 3 non (réponse fausse ou absente) ; **« juste en g3 seulement »** : nombre de tâches
  auxquelles la génération 3 répond juste et la génération 0 non. Les tâches justes dans les deux générations, ou dans
  aucune, n'entrent pas dans le test. Sens du rejet : « génération 3 au-dessus de la génération 0 » quand le second
  compte dépasse le premier, « génération 3 au-dessous de la génération 0 » quand le premier dépasse le second, écrit
  seulement pour un verdict « changement au-delà du bruit des tâches » (sinon « sans objet (non rejeté) ») ; à comptes
  égaux, la valeur p vaut 1 et le test n'est jamais rejeté. Là où le LISEZMOI v3 nomme ces deux comptes par des lettres,
  lire « juste en g0 seulement » et « juste en g3 seulement ».
- **O1** : le verdict d'un fichier `holm-quatre`, lu avec sa valeur p brute, peut dire les verdicts de l'autre course
  (Holm sur quatre tests ne rejette une valeur p au-dessus de 0,05 / 4 que si des tests de rang inférieur, qui peuvent
  être ceux de l'autre course, l'ont été), et la lecture finale ne motive aucune décision.

## 5. Commandes pour session-depot — remplace le § 5 du LISEZMOI v3

Dossiers réels de la copie de lancement. **`R` est relatif** (RSL3-02 c) : lancer les commandes depuis le dossier qui
contient `essaim-m3-refonte-v1/` (racine de la copie de lancement), ou donner à `R` son chemin absolu ; sinon le script
refuse (« dossier de course absent »), sans rien écrire. Chaque commande écrit dans un dossier de sortie **nouveau** (le
script refuse d'écraser) ; sa sortie standard est redirigée dans un fichier poussé sans être lu ; la sortie d'erreur
aussi (elle ne porte jamais de score : motifs de refus, type et ligne d'une erreur interne, noms de fichiers). Le code
de sortie (0 écrit ; 2 usage ; 3 refus ; 4 erreur interne ; 130 interrompu) peut être affiché.

```
R=essaim-m3-refonte-v1                                   # copie de lancement (chemin relatif : voir ci-dessus)
COURSE_M="$R/pilotes/pilote4-gemini-v6-2-v1-tentative2"
COURSE_S="$R/pilotes/pilote4-gemini-v6-2-s-v1"
BANQUE_DIR=<dossier qui porte banque-confrontation-v3.json et banque-confrontation-v3-secret.json>
LECTURE=<dossier où sont copiés lire_pilote4_v4.py et lire_pilote4_v4.py.sha256>
SORTIES=<dossier existant où naissent les dossiers de sortie>
unset LECTURE_PILOTE4_ESSAI_SEULEMENT_EMPREINTES_BANQUE
(cd "$LECTURE" && sha256sum -c lire_pilote4_v4.py.sha256)
```

Facultatif, avant la première lecture (n'imprime que les comptes 8 et 14 et l'issue ; aucune valeur) :

```
python3 -I -B "$LECTURE/lire_pilote4_v4.py" essai-banque "$BANQUE_DIR"
```

**1. À la fin de la course M — part `test` de M** (écrit `lecture-pilote4-gemini-v6-2-v1-tentative2-test-v4.{json,md}`
et leurs compagnons) :

```
SORTIE_TEST_M="$SORTIES/lecture-test-M-v4"
python3 -I -B "$LECTURE/lire_pilote4_v4.py" test --course "$COURSE_M" "$BANQUE_DIR" "$SORTIE_TEST_M" \
  > "$SORTIES/etat-lecture-test-M-v4.txt" 2> "$SORTIES/erreurs-lecture-test-M-v4.txt"; echo "code $?"
```

**2. À la fin de la course S — part `test` de S** (écrit `lecture-pilote4-gemini-v6-2-s-v1-test-v4.{json,md}` et leurs
compagnons) :

```
SORTIE_TEST_S="$SORTIES/lecture-test-S-v4"
python3 -I -B "$LECTURE/lire_pilote4_v4.py" test --course "$COURSE_S" "$BANQUE_DIR" "$SORTIE_TEST_S" \
  > "$SORTIES/etat-lecture-test-S-v4.txt" 2> "$SORTIES/erreurs-lecture-test-S-v4.txt"; echo "code $?"
```

**3. À la fin de la course S — part `test_final` des deux courses, Holm sur quatre** (écrit
`lecture-pilote4-gemini-v6-2-v1-tentative2-test-final-holm-quatre-v4.{json,md}` et
`lecture-pilote4-gemini-v6-2-s-v1-test-final-holm-quatre-v4.{json,md}`, avec leurs compagnons : à pousser sans les
afficher, jusqu'à la fin du compteur de rondes, N-050) :

```
SORTIE_FINAL="$SORTIES/lecture-test-final-holm-quatre-v4"
python3 -I -B "$LECTURE/lire_pilote4_v4.py" test_final --course-m "$COURSE_M" --course-s "$COURSE_S" "$BANQUE_DIR" "$SORTIE_FINAL" \
  > "$SORTIES/etat-lecture-test-final-holm-quatre-v4.txt" 2> "$SORTIES/erreurs-lecture-test-final-holm-quatre-v4.txt"; echo "code $?"
```

**Variante — la course S ne court pas ou ne finit pas saine, Holm sur deux, au lieu de la commande 3** (écrit
`lecture-pilote4-gemini-v6-2-v1-tentative2-test-final-holm-deux-v4.{json,md}` et leurs compagnons) :

```
SORTIE_FINAL_M="$SORTIES/lecture-test-final-holm-deux-v4"
python3 -I -B "$LECTURE/lire_pilote4_v4.py" test_final --course-m "$COURSE_M" --sans-seconde-course "$BANQUE_DIR" "$SORTIE_FINAL_M" \
  > "$SORTIES/etat-lecture-test-final-holm-deux-v4.txt" 2> "$SORTIES/erreurs-lecture-test-final-holm-deux-v4.txt"; echo "code $?"
```

**Après un code 4 ou 130** (RSL3-02 a) : la SORTIE peut porter les fichiers, complets, avec leurs compagnons, si l'erreur
ou l'interruption est venue après l'écriture (le fichier d'état dit alors « lecture écrite, erreur interne (ou
interrompue) avant la ligne d'état : <noms et empreintes> ») : ne pas tenir cette SORTIE pour non écrite et ne pas
relancer dans la même SORTIE ; un fichier provisoire caché qui y resterait est nommé sur la sortie d'erreur.

## 6. Fenêtre d'écriture (RSL3-02 b) — remplace le § 4, point 6, du LISEZMOI v3

Entre la création exclusive d'un fichier et son inscription dans la liste de ce que l'appel retire en cas d'erreur, il
reste une fenêtre de deux instructions : pour chaque fichier provisoire caché (`.<nom>.en-cours-<pid>`, l. 1143–1144) et,
sans liens durs, pour chaque fichier définitif (l. 1156–1157). Une interruption au clavier exactement là laisse ce fichier
vide dans SORTIE, alors que le message dit « rien n'est laissé à moitié écrit » (l. 1356). Code inchangé (point 5) ;
sur un système de fichiers à liens durs, seuls les provisoires sont concernés.

## 7. Essais (R5, R4) et journal

`essais-lire-pilote4-v4.log` (ouvert à 08:22:42, fermé à 08:33:06 UTC ; heures lues sur `date -u` ; écrit sous
`set -C`) : harnais sous `/opt/venv-essaim-sim-v1/bin/python -I` (3.13.17) ; script lancé sous le même interpréteur, avec
les mutations, puis rejoué sous `/usr/bin/python3.11` (3.11.17), `/usr/bin/python3.12` (3.12.3) et `/usr/bin/python3`
(3.13.17) : **19 sur 19 cas sains et 65 sur 65 artefacts conformes, quatre fois** ; aucun cache écrit dans le noyau
importé ; **51 sur 51 copies altérées du script détectées** (sous 3.13 ; deux à la fois). Données synthétiques
seulement ; dossiers de travail effacés. Commandes : `/opt/venv-essaim-sim-v1/bin/python -I essais_lire_pilote4_v4.py
--mutations --paralleles 2`, puis `… --interpreteur-script <python>` pour chaque rejeu.

Les essais sont ceux de la v3 (LISEZMOI v3, § 6 : valeurs refaites indépendamment, paires de non-interférence, union,
plantations, artefacts de banque, de dossier et d'archive, pannes d'écriture, interruptions), noms de sortie en `-v4`, et
deux cas nouveaux (RSL3-01, § 3) : « score du noyau divergent dont l'écriture tombe sur une proportion de l'autre course »
(sain) et « toutes les écritures propres à l'autre course plantées une à une » (artefact) ; mutation nouvelle : M51 (la
garde de la v3, qui n'écarte pas les écritures des nombres du fichier), détectée par le premier.
