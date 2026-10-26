# LISEZMOI — lanceur v11 du pilote 4 (seconde course : la v6.2.1 sur la question S) et batterie d'essais v13 — v1

Écrit par un sous-agent neuf le 2026-10-26T04:41:28Z (heure lue sur `date -u` dans la commande qui a écrit ce fichier), sur le brief
`BRIEF-lanceur-v11-v1.md` (empreinte `8e8c487ae713897b0adcff125b1b7378a0237013efc83b9d736c8434b3b581ef`, vérifiée avant lecture) ;
pièces fournies vérifiées contre `EMPREINTES-fournis-v1.txt` (six fichiers, tous conformes). Rien n'a été lu hors de `fournis/`, rien
n'a été écrit hors de `sortie/`. Ni `git`, ni exécution du lanceur ou de la batterie, ni sous-agent, ni réseau, ni clé. Exécutés :
`python3 -I` sur les deux scripts de dérivation, `bash -n` sur le lanceur v11 et la batterie v13, `diff -u`, `sha256sum`.

## Ce qui a été fait

1. `deriver_lanceur_pilote4_v11.py` : dérive `lancer_pilote4_gemini_v11.sh` (938 lignes) de `lancer_pilote4_gemini_v10.sh`
   (921 lignes, `0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952`, vérifiée par le script) par 14 remplacements
   exacts, chacun à 1 occurrence, puis 37 contrôles de présence ou d'absence. Exécuté : écrit la v11 en une passe. Écart :
   `diff-lanceur-pilote4-v10-vers-v11.txt` (`diff -u`, 186 lignes). `bash -n` : conforme.
2. `deriver_essais_pilote4_v13.py` : dérive `essais_lanceur_pilote4_v13.sh` (701 lignes) de `essais_lanceur_pilote4_v12.sh`
   (658 lignes, `27ef4524…`, vérifiée) par 36 remplacements globaux (comptés sur la v12) puis 7 remplacements ancrés sur le texte
   obtenu (cas ajoutés, bloc réel réécrit), puis 31 contrôles. Exécuté : écrit la v13 en une passe. Écart (non demandé, fourni pour
   la relecture) : `diff-essais-pilote4-v12-vers-v13.txt` (450 lignes). `bash -n` : conforme. **Aucune exécution de la batterie.**
3. Ce LISEZMOI et les compagnons `.sha256` (format « empreinte, deux espaces, nom nu »).

## Lanceur v11 — liste des remplacements (tous à 1 occurrence)

1. En-tête, lignes 2 à 4 : objet du pilote (« organisme assisté de Gemini, la v6.2.1, seule, sur la question M puis sur la
   question S ») ; « question de la course (M, puis S) à g001 » ; usage des clés (`v6-2` sous le lanceur v10, puis `v6-2-s`) ;
   dérivation v11 (empreinte `0203f546…`, script `deriver_lanceur_pilote4_v11.py`, motif R-492, écart consigné).
2. Ligne 9 (historique du v9) : « puis la v5.3 après une v6.2 saine » → « puis la seconde course après une v6.2 saine ».
3. Ligne 24 (historique) : « (v9 ; « v5.3 précédente » jusqu'au v8) » → « (v9 ; dans l'ordre inverse jusqu'au v8) ».
4. Ligne 29 (objets) : la ligne de la v5.3 (`4ecba58`, `6251ab21…`, 22 fichiers) remplacée par la phrase demandée : « la v5.3 ne
   court pas (décision de Lazar, R-492), et la clé `v6-2` ne sert plus qu'en simulation (la course M de ce pilote a tourné sous
   `lancer_pilote4_gemini_v10.sh`, R-490) ».
5. Usage (lignes 37 à 41) : `COURSE=v6-2-s … REFERENCE_M=… PRECEDENTE_V62=<dossier de la course M de ce pilote,
   pilote4-gemini-v6-2-v1[-tentativeN], dans la même copie> … bash lancer_pilote4_gemini_v11.sh` ; `MODE=reel COURSE=v6-2` :
   refusée ; `MODE=simulation COURSE=v6-2` : permise.
6. `COURSE="${COURSE:?COURSE=v6-2-s ou COURSE=v6-2}"`.
7. Bloc question + `case` (lignes 69 à 87) : les trois constantes `COMMIT_QUESTION`, `CHEMIN_QUESTION`, `SHA_QUESTION` passent
   dans chaque branche ; branche `v6-2-s)` : `NOM="pilote4-gemini-v6-2-s-v1"`, `INDICE_GRAINE=0`, organisme = la v6.2.1 (commit
   `7ea32705…`, arbre `4f13647a…`, 26 fichiers), `LIGNEE="gemini-organisme-v6-2-s"`, question S (commit `4772b525…`, chemin
   `brouillons/canal-reprise-releve-v1/envois/question-apprendre-structure-entrainement-generations-organismes-v2.md`, sha256
   `a54da93e…`) ; branche `v6-2)` inchangée + question M (`a15809b8…`, chemin actuel, `8b1c7511…`) ; message « COURSE inconnue :
   … (v6-2-s ou v6-2) » ; juste après `esac` : `if [ "$MODE" = reel ] && [ "$COURSE" = v6-2 ]; then refus_tot "COURSE=v6-2 en
   mode réel : la course M a tourné sous le lanceur v10 (R-490) ; ce lanceur v11 ne lance en réel que v6-2-s (R-492)"; fi`.
   La surcharge d'essai `[ "$ART" = commit ] && COMMIT_QUESTION=…` reste après le `case` (ligne 186) et garde son effet.
8. Porte « course précédente » (étape 0 bis) : commentaire mis à jour ; après `EMP_V62=""`, deux variables définies avant la
   porte : en réel `LANCEUR_V62_NOM=lancer_pilote4_gemini_v10.sh` et `LANCEUR_V62_SHA=0203f5461d1ee7770850ee1b91cb6b379e9f8931b02626d22de56a655eb2c952` ;
   en simulation `LANCEUR_V62_NOM="$(basename "$0")"` et `LANCEUR_V62_SHA="$SHA_LANCEUR"` ; condition `[ "$COURSE" = v6-2-s ]` ;
   messages « la course S ne part qu'après… » (deux refus).
9. Refus « empreintes de v6.2 absentes : la course S ne part qu'après une course v6.2 finie et fermée ».
10. Appel du contrôle Python : `"$LANCEUR_V62_SHA"` et `"$LANCEUR_V62_NOM"` à la place de `"$SHA_LANCEUR"` et `"$(basename "$0")"`
    (les autres paramètres inchangés : `gemini-organisme-v6-2`, `$MODE`, `$GO_ID`, `v6-2`, `pilote4-gemini-v6-2-v1`) ; refus
    « la course S ne part pas : issue de v6.2 hors de la liste saine … ».
11. Note du LANCEMENT.md de la porte : ajout de « ; lanceur attendu $LANCEUR_V62_NOM (${LANCEUR_V62_SHA:0:8}…) » (choix seul, voir
    plus bas).
12. Contrôle de la graine de la course précédente (étape 2) : `[ "$COURSE" = v6-2-s ]`.
13. Commentaire de l'étape 3 : « Organisme de la course (la v6.2.1 pour les deux courses …) et question (par course) ».
14. Ligne de dépense : « la ligne de dépense de la course S ne porte pas l'empreinte des empreintes de v6.2 … ».

Contrôles finals du script (tous passés) : `v5.3` 1 fois, dans « la v5.3 ne court pas » ; `v5-3` 3 fois, toutes dans
`PERMIS_APRES_CODE` (chemins permis du troisième pilote, `…-v5-3-v6…`, voir les choix) ; `6251ab21`, `4ecba58`,
`"gemini-organisme-v5-3"`, `pilote4-gemini-v5-3-v1` : 0 ; `a54da93e` 1 (code), `8b1c7511` 1 (code) ; `lancer_pilote4_gemini_v10.sh`
2 (la porte, l'en-tête) ; `lancer_pilote4_gemini_v11.sh` 1 (usage) ; empreinte de la v10 en entier 1 (la porte) ; commit et
arbre de la v6.2.1 2 chacun ; `COMMIT_QUESTION=` 3 (deux branches, surcharge d'essai) ; `LANCEUR_V62_NOM` et `LANCEUR_V62_SHA`
4 chacun ; `SHA_LANCEUR` 6 (inchangé) ; `PRECEDENTE_V62` 9 (inchangé) ; `GRAINE_V62_MANIFESTE` 7 (inchangé).

## Batterie v13 — ce qui change, cas ajoutés

Équivalents (remplacements globaux) : clé `v5-3` → `v6-2-s` (12 `COURSE=`, 5 lignes « graine de la course … »), nom
`pilote4-gemini-v5-3-v1` → `pilote4-gemini-v6-2-s-v1` (10), `G_53` → `G_S` (13, enfant 0 de `SeedSequence(12345).spawn(2)`),
`V53` → `VS`, `V5C` → `VSC` (28), `REEL_V53` → `REEL_S`, fichiers d'entrée `dep-v53-*` → `dep-s-*`, `td-heure-fraiche-v53` →
`-s`, `go-v53-seulement.md` → `go-s-seulement.md` ; noms de cas `sain-v5-3-*` → `sain-v6-2-s-*`, `reel-v5-3-*` → `reel-v6-2-s-*`,
`organisme-v5-3` → `organisme-v6-2-s` (attend `4f13647a…`), `nombre-v5-3` → `nombre-v6-2-s` (26), `seg-v5-3-porte-saine` →
`seg-v6-2-s-porte-saine`, `v5-3-depense-sans-empreinte-v62` → `v6-2-s-depense-sans-empreinte-v62` ; messages attendus « la
course S ne part qu'après v6.2 », « la ligne de dépense de la course S … », « (v6-2-s ou v6-2) » ; lignes de GO d'essai : une
ligne saine porte `8b1c7511…`, `a54da93e…` et `4f13647a…` (`go-sain`, `go-sans-texte`, `go-mutant`, `go-sans-calcul`,
`go-autre-id`) ; `6251ab21…` n'apparaît plus ; `go-autre-question` porte une empreinte qui n'est ni M ni S ; le cas
`m-sous-lanceur-pilote4` nomme `lancer_pilote4_gemini_v11.sh`.

Cas ajoutés (6 `cas`, 5 `verifier`) :
- (i) `reel-v6-2-refusee` : `MODE=reel COURSE=v6-2` → « COURSE=v6-2 en mode réel : la course M a tourné sous le lanceur v10 ».
- (ii) `go-m-seulement-refuse-v6-2-s` : ligne de GO portant `8b1c7511…` sans `a54da93e…` → « l'empreinte de la question
  a54da93e… » ; symétrique `go-m-seulement-autorise-v6-2` (course v6-2 saine de bout en bout sur cette ligne) ; le couple
  `go-s-seulement-autorise-v6-2-s` / `go-s-seulement-refuse-v6-2` (équivalents de `go-v53-seulement-*`) ferme le carré.
- (iii) `sain-v6-2-s` (équivalent de `sain-v5-3`) : la course S saine de bout en bout après la v6-2 saine produite par ce lanceur
  en simulation, avec ses 7 `verifier` d'origine plus `sain-v6-2-s-question` (`a54da93e…` au LANCEMENT.md),
  `sain-v6-2-question` (`8b1c7511…` sur la v6-2) et `sain-v6-2-s-lanceur-attendu` (« lanceur attendu <nom du lanceur sous
  essai> (<8 premiers caractères>…) », branche simulation des deux variables).
- (iv) `v62-autre-lanceur` existait (empreinte du lanceur remplacée par 0000 → « n a pas tourné sous ce lanceur ») : gardé. Ajoutés
  : `v62-lanceur-v10-en-simulation` (course précédente citant le lanceur v10 et son empreinte en simulation → refusée, puisque la
  porte attend alors ce lanceur-ci) ; `reel-v6-2-s-precedente-sous-ce-lanceur` (copie « réelle » citant ce lanceur-ci → refusée en
  réel, puisque la porte attend alors le v10).
- Mode réel, étape (0) : les cinq cas `reel-sans-reference`, `reel-reference-hors-root`, `reel-reference-nom`,
  `reel-reference-simulee`, `reel-reference-tentative-simulee` courent sur `COURSE=v6-2-s` derrière une copie « réelle » de la
  v6.2 saine (`V62_REEL`, posée par `poser_v62_reel` avant chaque cas dans le dossier des pilotes de la copie sous /root) :
  LANCEMENT.md réécrit par `sed` sur deux lignes (en-tête « (reel, tentative 1) » ; « lanceur : lancer_pilote4_gemini_v10.sh,
  sha256 0203f546… »), manifeste de l'extrait réécrit par `extrait_altere` (`reel = True`, `go_id = GO-2026-10-25-02`), rescellée
  par `refaire_empreintes`. Deux `verifier` sur le LANCEMENT.md de la tentative S : `reel-porte-v10-passee` (« ; v6.2 saine :
  g000 à g003 OK ») et `reel-porte-v10-attendu` (« lanceur attendu lancer_pilote4_gemini_v10.sh (0203f546…) »).

Nombre de cas : v12 = 229 (160 `cas`, 40 `verifier`, 20 `verifier` en boucle, 4 `verifier_absent`, 5 `verifier_re`) ;
v13 = 240 (166, 45, 20, 4, 5). Aucun cas retiré ; aucun nom en double.

## Choix faits seul (une ligne chacun)

- Lanceur : `v5-3` gardé trois fois dans `PERMIS_APRES_CODE` (`pilote3-gemini-organisme-v5-3-v6…`, `pieces-pilote3-gemini-v5-3-v6/`) :
  ce sont les chemins permis des pièces du troisième pilote, pas la clé de course ; les changer modifierait une garde.
- Lanceur : deux phrases d'historique de l'en-tête (v9, lignes 9 et 24) reformulées sans « v5.3 » pour tenir la vérification
  demandée ; le fond de l'historique est gardé.
- Lanceur : la note de la porte consigne « lanceur attendu NOM (SHA8…) » — une addition hors de la liste, pour que le LANCEMENT.md
  dise sous quel lanceur la course précédente devait avoir tourné et que la batterie le vérifie dans les deux modes.
- Lanceur : ordre des branches du `case` conservé (`v6-2-s)` à la place de `v5-3)`, puis `v6-2)`) ; message « (v6-2-s ou v6-2) ».
- Lanceur : `REFERENCE_M=<dossier du pilote de la course M>` laissé tel quel dans l'usage ; `PRECEDENTE_V62` décrit avec les mots du brief.
- Batterie : le bloc des cinq cas réels de l'étape (0) remplacé en bloc (15 lignes, un remplacement exact) : avec `v6-2` refusée
  en réel et la porte (0 bis) avant l'étape (0), la seule façon de garder leurs équivalents est une course précédente « réelle ».
- Batterie : `cas` prend `COURSE=v6-2-s` par défaut (comme `v5-3` en v12) ; tout cas sans `COURSE` court donc sur la course S.
- Batterie : `go-m-seulement-autorise-v6-2` est une course simulée complète de plus (durée de la série allongée d'autant).
- Batterie : `question` renommé `question-v6-2-s` (attend `a54da93e…`) et `question-v6-2` ajouté ; `nombre-v6-2-s` attend 26.
- Batterie : écart v12→v13 fourni bien que non demandé.
- Batterie : trois lignes d'historique de l'en-tête (v11) gardées telles quelles (« v5.3 », « sain-v5-3-graine »).

## Ce qui n'a pas pu être fait par remplacement exact

Rien n'a été écrit à la main hors des scripts : chaque changement est un remplacement exact à 1 occurrence (ou au nombre compté).
Le bloc réel de l'étape (0) de la batterie a été remplacé comme un tout (ancre de 15 lignes), pas ligne à ligne.

## Ce qui n'a pas pu être vérifié sans exécuter

- Que le commit `4772b525081342a6a30ba8823733aa5770a888a8` est présent dans les copies du dépôt des essais et du pilote, et que
  `git show 4772b525…:brouillons/…/question-apprendre-structure-entrainement-generations-organismes-v2.md` donne bien
  `a54da93e…` (le fichier fourni `question-S-v2.md` a cette empreinte ; le contenu du dépôt à ce commit n'a pas été lu).
- Que ce commit n'est pas postérieur à `8e5e2f7b` sur la branche de tête : la garde « commits postérieurs à 8e5e2f7b hors des
  pièces du pilote » (`git diff --name-only 8e5e2f7b HEAD`) refuserait un chemin sous `brouillons/` ; la question M (`a15809b8`)
  passe cette garde dans la course M, la question S v2 a servi au second pilote, d'où l'attente qu'elle la passe aussi — non vérifié.
- Que la copie « réelle » passe la porte (0 bis) en mode réel : chaque contrôle de la liste close a été relu contre les deux
  réécritures (en-tête, ligne du lanceur, `manifeste.reel`, `manifeste.go_id`) ; non exécuté.
- Les cas réels exigent root, une copie sous /root avec un `origin` joignable (`git ls-remote`), aucune course du noyau au
  décalage 900 dans le conteneur (la course M en cours sous le lanceur v10 refuserait tous les cas réels avant l'étape (0), sauf
  `reel-v6-2-refusee`, qui refuse juste après le `case`), et l'absence du marqueur
  `/var/lib/essaim-m3/pilotes-partis/pilote4-gemini-v6-2-s-v1`.
- `bash -n` ne vérifie que la syntaxe ; aucun cas n'a tourné.

## Empreintes des fichiers de `sortie/` (compagnons `.sha256` joints)

- `deriver_lanceur_pilote4_v11.py` : `a88d00c9766b68021988c3c6134939ae09663f99e451d1ca7588fb5b03e5489a`
- `lancer_pilote4_gemini_v11.sh` : `21854b794de90d874b23def1685e306ceba80b32cd471de1dd8cf750ad01d0d7`
- `diff-lanceur-pilote4-v10-vers-v11.txt` : `875fb3ab2d1873ce4dc3796de1f96c0c357bc0ac29307e74c9799cd104943136`
- `deriver_essais_pilote4_v13.py` : `65cf6f70267fc3c744c1fc35188bff61279433ef5913e2ed18cca21ffb13c8b6`
- `essais_lanceur_pilote4_v13.sh` : `7b0a9bb0f7637480c19acb06138034582c8f69d2502cd3c483318f43f0f1e388`
- `diff-essais-pilote4-v12-vers-v13.txt` : `3ec56bb1d4cf021a2181d7ea75be0e6835d8e5ebd686ccc613802ed9c9d382a8`
- `LISEZMOI-lanceur-v11-v1.md` : voir `LISEZMOI-lanceur-v11-v1.md.sha256`.
