# Contre-lecture 3 du préenregistrement du quatrième pilote descriptif (`pilote4-gemini-organisme-v3.md`) — v1

- **Texte relu** : `essaim-m3-refonte-v1/prereg/pilote4-gemini-organisme-v3.md`,
  `efffb7e4bd46320feb95835faec9369b19a70039e6765e3d4710e62ecf7cebfd` (empreinte vérifiée sur disque avant lecture ;
  540 lignes ; commit cité par la demande : `eee726b`, non vérifié, pas de `git`).
- **Contre-lecteur** : sous-agent neuf (`claude-opus-5-5`), lancé par conv-audit, le 25 octobre 2026. Début lu sur
  `date -u` : 20:58:38 UTC ; ce rapport est écrit à partir de 21:29 UTC (heure lue sur `date -u` juste avant). Je n'ai
  écrit ni ce texte, ni ses versions 1 et 2, ni le noyau, ni les lanceurs, ni les batteries, ni le script de scellement,
  ni les contre-lectures 1 et 2.
- **Lu** : la v3 en entier ; l'écart de la v2 à la v3 en entier (recalculé, `ecarts/diff-texte-v2-vers-v3.txt`) ; la
  contre-lecture 2 en entier (`7c625fa6…`) ; P3 (`57c8535a…`) aux lignes citées (150–162, 194–202, 236–241, 285–292,
  300–316) ; T2 (`d2944654…`) aux lignes citées (225–226, 236–244, 287, 308–314, 384–392, 414–446, 500–520, 553) ; noyau
  `8e5e2f7b` : `boucle.py` en entier (1 154 lignes), `cli.py` en entier, `serveur.py` l. 21 et 60–95,
  `bac_a_sable.py` (espace des organismes, capacités, lancement borné), `archive.py` l. 57–87 et 223–240,
  `question.py` l. 60–110, `contrat.py` l. 138–150, `outils/extrait_mecanique.py` l. 50–80 et 205–270,
  `tests/test_reprise_segments.py` en entier ; l'écart fourni `b1c7f4b6` → `8e5e2f7b` (code et essais) en entier ; la
  note `notes/reprise-segments-v1/` en entier (note, deux scripts et deux journaux de mutations, suite complète) ;
  lanceur v6 en entier ; écarts v4 → v5 et v5 → v6 en entier ; scripts de dérivation des lanceurs v5 et v6 et des
  batteries v6 et v7 ; écarts des batteries v5 → v6 et v6 → v7 en entier ; journal de la série v8 en entier, journal et
  fichier de cause de la série v7, fichiers d'heures, décompte de la série v6 ; `simulation-lanceur-v6/` (les quatre
  `LANCEMENT`, aux lignes de segments ; les quatre extraits, champs mécaniques seulement) ; script de scellement v3,
  ses essais et leurs deux journaux ; `faits-pilote3-v1/` (durées, coûts, lignes d'heure et de dépense) ; code extrait
  de la v5.3 et de la v6.1 aux lignes citées (lecture seule) ; référence de provenance (sortie) et référence de paire
  (sortie) ; `LISEZMOI-v9.md` § 4 ; la demande de v6.2 (`f1551187…`) § 2 et § 3.
- **Non lu ni ouvert** (consignes) : aucun fichier `…-cle.json` ni `…-secret.json` (ni lu ni haché ; leurs noms
  seulement vus par `ls` du dossier `banque/`), aucun dossier `donnees/`, `runs/`, `diag/`, aucun `P3-consignes-v1.md` ni
  fichier `textes-actions-…`, aucune archive `ferme.tar.gz`, aucun fichier `reponse-question*`, `journal-appels*` ou
  `extrait-mecanique*` des pilotes réels (seuls ceux des simulations de `simulation-lanceur-v6/` ont été lus, champs
  mécaniques). Non lus, donc non vérifiés : la contre-lecture 1 (sauf son empreinte), les messages du canal et des
  sessions où Lazar a parlé (les citations de 16:27 à 20:23 Paris), le rapport de vérification de la v6.1
  (`f9b3646d…`), l'audit de symétrie (`f732bfd8…`), la note N-046 (`7fa0f544…`), la question M (`8b1c7511…`, vue
  seulement indirectement : le lanceur la recalcule dans les simulations), les registres de `main` hors des lignes
  recopiées dans `faits-pilote3-v1/`. L'absence de branche `canal/gemini-organisme-v6-2` n'est pas vérifiable sans `git`.
- **Exécuté** (sorties sous `/var/tmp/contre-lecture-pilote4-v3/` seulement) : `sha256sum` sur les pièces et
  `sha256sum -c EMPREINTES-pieces-pilote4-v4.txt` depuis `pieces-pilote4-gemini/` (après lecture de sa liste : aucun nom
  interdit) ; `diff` (texte, lanceurs, batteries) et `patch` de l'écart fourni sur les fichiers d'avant (`verif-diff-noyau/`) ;
  `deriver_lanceur_pilote4_v5.py`, `deriver_lanceur_pilote4_v6.py`, `deriver_essais_pilote4_v6.py` et
  `deriver_essais_pilote4_v7.py` sur les fichiers sources fournis (`rederive/`) ; `sceller_pilote4_v3.py` sur quatre
  copies d'essai du texte nommées `pilote4-gemini-organisme-v9.md` (`essai-scellement-copies-jamais-a-lancer/` : **les
  valeurs d'entropie et de graines qui s'y trouvent sont tirées pour l'essai, ce ne sont pas celles du pilote**) ; mon
  propre code, lecture seule (`outils/` : empreintes « blob » calculées sans `git`, empreintes d'arbre, relevé des
  empreintes citées par le texte, relevé mécanique des extraits de simulation) ; l'empreinte d'arbre du noyau par
  `boucle.empreinte_arbre` depuis la copie du noyau (`-B`) ; les essais `tests/test_reprise_segments.py` dans la copie
  du noyau, en root, avec `ESSAIM_M3_ESPACE` et `--basetemp` dans mon dossier (premier essai : 10 erreurs « chemin de
  socket trop long », dues à la longueur de mon chemin d'espace, journal gardé ; second essai, chemin court :
  **28 passés en 62,95 s**, `essais-noyau/`) ; ces essais font tourner les organismes d'essai du noyau
  (`tests/fixtures/`), aucun organisme de Gemini ; leurs dossiers temporaires ont été effacés après lecture du résultat.
  Une commande `git hash-object --help` (aide de l'outil, sortie jetée) a été lancée par erreur pour savoir si l'outil
  est présent : aucun dépôt lu ni touché. **Rien** du lanceur, des batteries ni du code des organismes de Gemini n'a été
  exécuté. Aucun sous-agent.

## Verdict

**Scellable après corrections mineures.** Le noyau `8e5e2f7b` fait ce que dit le texte de la reprise par segments, et
rien d'autre : `STOP` n'est lu qu'entre deux unités ; l'état est écrit, scellé, jamais réécrit ; la reprise part de la
première unité qui n'a pas tourné, mêmes graines, même archive, même dépense ; une reprise refusée n'écrit rien ; un
même état ne se reprend pas deux fois ; une course sans `STOP` garde les mêmes événements. Les lanceurs v5 et v6 et les
batteries v6 et v7 se redérivent octet pour octet ; la série v8 est complète (218 sur 218, les mêmes cas que la série v7,
dans le même ordre) ; la cause de la série v7 est juste ; le script de scellement v3 refuse ce que la contre-lecture 2
demandait de refuser. Les quatorze constats de la contre-lecture 2 sont levés (P4C2-15 est une conformité), sauf un
point de P4C2-12 (minuteur mort non détecté). Les chiffres sont justes, à un libellé près.

Trois constats mineurs, tous de texte, sans changer ni le noyau, ni le lanceur, ni la batterie : un canal sur les
scores de `test` que les quatre générations ouvrent et que le texte ne déclare pas (P4C3-01) ; l'arrêt par une main
humaine, que le lanceur ne distingue pas de celui du minuteur, et la notation `SEGMENT=K` de la liste d'arrêt
(P4C3-02) ; l'affirmation « chaque refus sur un artefact », inexacte pour trois gardes du noyau et plusieurs gardes
nouvelles du lanceur (P4C3-03). Six remarques suivent. Le texte tient dans les trois cas soumis à Lazar (v6.1 nommée
et ses points ouverts acceptés ; seule la v5.3 ; une v6.x plus tard sous un texte à part), à la phrase du critère 3 près
(P4C3-09), et quelle que soit sa réponse sur la condition (ii) du moment de lecture.

## Traitement des constats de la contre-lecture 2

| constat | statut | ce que j'ai vérifié |
|---|---|---|
| P4C2-01 (mineur) | **levé** | Noyau : après la dernière unité, plus aucune lignée active, `STOP` n'est plus honoré et la course finit « aucune lignée active », sans état (`boucle.py` l. 934–938) ; essai `test_stop_pendant_la_derniere_unite_n_appelle_pas_de_segment` lu (le `STOP` est posé après l'unité 5, la dernière ; le noyau ne distingue pas « pendant » et « après », il ne lit `STOP` qu'avant une unité) et passé chez moi. Ailleurs, `STOP` termine un segment, repris (cas `seg-segment2`, `seg3-…`). La porte accepte une v5.3 en segments : arrêts « fichier STOP » autant que de reprises numérotées 2, 3, …, puis « aucune lignée active », dernier code 0 (lanceur v6 l. 304–306, 338–342 ; cas `seg-v6-1-porte-saine`). La borne de temps tient (P4C3-06). |
| P4C2-02 (mineur) | **levé** | Ligne de la table (texte l. 100) et ligne « une course = une commande de fond » (l. 99) ; ligne de T2 remplacée à la liste d'arrêt (l. 396–398, 403) ; « hors ceux que la table de correspondance et la liste d'arrêt nomment » (l. 48). |
| P4C2-03 (mineur) | **levé** | Les quatre essais nouveaux cités au § Essais (l. 451–454) sont dans `ESSAIS_CITES` du lanceur v6 (l. 168) et exigés passés (l. 653, 659) ; lus : `test_stop_pose_pendant_une_unite_ne_l_interrompt_pas` pose `STOP` avant l'unité 3 (`stop_pendant=True`), qui finit et s'archive ; la reprise part de l'unité suivante. |
| P4C2-04 (mineur) | **levé** | Texte l. 153–165 = la lecture de la contre-lecture 2 ; lignes revérifiées : `boucle.py` l. 651 (`8e5e2f7b`) ; v5.3 `memoire_isvd.py` l. 110–113, 117, 121–124, 227–235. |
| P4C2-05 (mineur) | **levé** | Texte l. 73–75 : les 3 USD et 900 s dits bornes de ce texte, portées par le mot d'extension ; 75 USD attribués au mot de 20:23 Paris, comme cité l. 63. |
| P4C2-06 (mineur) | **levé** | ≈ 50 à 93 minutes (l. 292), v6.1 en 1 à 6 rondes (l. 291), devis ≈ 30 à 55 USD et deux bases dites (l. 302–304), « risque restant » retiré ; calculs refaits (P4C3-10). Libellé « du noyau » : P4C3-06 b. |
| P4C2-07 (mineur) | **levé** | « rapporter à côté, sans comparaison » (l. 374–376), en accord avec T2 l. 518–520 ; métrique fixée au § Hypothèse (l. 321–323) ; script de lecture écrit, empreinté et essayé avant le moment de lecture (l. 376–379), engagement à tenir ; `LISEZMOI-v9.md` § 4, point 3 (l. 102–105) relu. |
| P4C2-08 (mineur) | **levé** | `sceller_pilote4_v3.py` (`aee63b20…`) lu : une seule ligne qui porte l'égalité d'entropie, sans nombre avant le remplissage ; exactement les deux lignes de graine des marqueurs ; gardes après remplissage. Journaux : 14 sur 14 (v3), 10 sur 14 pour le témoin (v2 scelle les quatre artefacts nouveaux). Mes quatre copies : texte tel quel refusé (marqueurs de rédaction restants) ; texte rempli scellé, les graines recalculées depuis l'entropie écrite par les mêmes `grep` que le lanceur (étape 2 et porte de la v6.1) ; une ligne d'entropie insérée dans le détail refusée ; une ligne de graine insérée à la ligne 7 refusée. |
| P4C2-09 (mineur) | **levé** | Ligne de mutation (l. 411) : à g003, le successeur ne tourne pas ; invalide, fin « sans successeur valide » (`boucle.py` l. 841–848) ; précision en P4C3-09. |
| P4C2-10 (remarque) | **levé** | `memoire_isvd.py` l. 110–113 ; `mitose_spectrale.py` l. 78 (P3 l. 239) ; `cli.py` l. 153–154 (simulation) et l. 309–312 (réel) ; `archive.py` l. 76–78 ; `contrat.py` l. 142–146 (§ 5 bis) ; `boucle.py` de `8e5e2f7b` : l. 49, 84–95, 277–282, 535, 626–629, 651, 657, 741, 831–848, 862–872, 887, 902, 928–938, 969–1001, 1003 — toutes justes. Historique de g1 avec les rondes au score vide, écartées par la v6.1 (v6.1 `principal.py` l. 928) : juste. |
| P4C2-11 (remarque) | **levé** | « exactitude attendue d'un oracle de catégorie » (l. 231–232, 371) ; point 5 réécrit (l. 383–384). |
| P4C2-12 (remarque) | **levé en partie** | Faits du second pilote nommés avec leur empreinte (l. 36, 301) ; extraits de M et S dans la déclaration de lecture (l. 31) ; champs de la déclaration de fin (l. 318 ; vus dans les extraits de simulation : `critere`, `exactitude_moyenne_sonde` vide, `n_exemplaires_isvd` 12, `sondes_traits_actives` faux) ; coût de la source web au mot d'extension (l. 171, ligne de GO) ; commande de fond limitée à l'appel du lanceur (l. 280–281, 402) ; note du minuteur neutre (lanceur v6 l. 791). **Reste** : un minuteur mort avant l'échéance passe inaperçu ; avec les segments, la borne de deux heures en dépend (P4C3-06 a). |
| P4C2-13 (remarque) | **levé** | Condition (ii) lue d'avance (l. 356–358 : scores fermés sauf décision de Lazar inscrite avant toute lecture) ; risque de la condition (i) de P3 signalé (l. 358–359). Le texte tient quelle que soit la réponse de Lazar : une autre lecture serait un écart inscrit au texte scellé. |
| P4C2-14 (remarque) | **levé** | Le script v3 refuse les marqueurs de rédaction restants et toute ligne d'entropie ou de graine de trop, donc aussi dans le détail inséré ; le texte garde le nom `pilote4-gemini-organisme-v3.md`. Reste à faire au remplissage : citer dans le détail l'empreinte relue par chaque contre-lecture (P4C3-09). |
| P4C2-15 (conforme) | sans objet | — |

Le traitement de la contre-lecture 1 renvoie à la v2 (l. 513–515), non scellée mais citée par son empreinte entière
(l. 5–6) : la référence est fixe ; conforme.

## Constats

### P4C3-01 — mineur — Les appels de mutation de la v6.1 en génération notée disent la stagnation des scores de `test` : canal non déclaré

- **Fait, code.** En génération notée, la v6.1 ne tente sa mutation que si le dernier score de l'historique ne
  dépasse pas l'avant-dernier de plus de 0,01 (`principal.py` de `a9d8eb5`, l. 926–933 : `forcer_mutation` vient d'une
  clé que le noyau ne sert pas, P3 l. 196–199) ; ces scores sont ceux de `test`, rendus par le noyau dans `historique`
  (`archive.py` l. 229–234). La première génération où c'est possible est g002 (texte l. 179–183). Une mutation tentée
  a fait, en simulation, un appel de rôle `architecte_mutation_endogene` (série v8 : g003 de la v6.1 a 124 appels, dont
  un de ce rôle, contre 123 à la v5.3 ; journal v8 l. 60 et 66), et son successeur valide devient l'organisme de la
  génération suivante. Le retour arrière (v5.3 et v6.1, à partir de g002, écart de plus de 0,03) fait de même dépendre
  la mémoire des scores.
- **Fait, texte.** Ces faits sont lisibles avant le moment de lecture : pendant la course, session-depot consulte le
  journal des appels de l'unité en cours (texte l. 360–362 ; T2 l. 418–422 : « statuts, espèces, coûts, types de blocs ;
  aucun score »), qui porte aussi le rôle de chaque appel ; dès la fin, les journaux recopiés et l'extrait (nombre
  d'appels, coût et durée par génération) sont des pièces lisibles (T2 l. 422–428). T2 acceptait le « `role` de chaque
  appel » comme une valeur écrite par l'organisme (l. 428–432) parce que « le score de g0 n'a d'effet sur rien à g1 » ;
  à quatre générations ce n'est plus vrai. Le § Plan, point 3 (texte l. 362–368), déclare les canaux (a), (b), (c), mais
  pas celui-ci, qui porte un bit par génération sur les scores de `test` (une baisse ou une progression d'au plus 0,01).
- **Correction** (une phrase, au point 3, sans autre changement) : « (d) à partir de g002, un appel de rôle
  `architecte_mutation_endogene` dans une génération notée de la v6.1 — et l'appel, le coût, la durée et le
  changement d'organisme qu'il ajoute — dit que le dernier score de `test` n'a pas dépassé l'avant-dernier de plus de
  0,01 ; le retour arrière fait dépendre la mémoire des scores (v5.3 et v6.1) ; canal dit et accepté ; pendant la
  course, session-depot ne lit du journal de l'unité en cours que ce que T2 nomme (statuts, espèces, coûts, types de
  blocs), jamais les rôles ; personne ne compte les rôles des appels d'une génération notée avant le moment de
  lecture. » Les déclencheurs mécaniques du critère 1 (appels hors `OK`) restent lus dès la fin.

### P4C3-02 — mineur — Un `STOP` posé par une main humaine se lit, au `LANCEMENT.md`, comme celui du minuteur ; la liste d'arrêt écrit `SEGMENT=K`

- **Fait, lanceur.** Après tout arrêt sur `STOP` qui laisse un état de reprise, le lanceur écrit « segment K arrêté par
  STOP ; reprise attendue : SEGMENT=K+1 » (lanceur v6 l. 811–819), que `STOP` vienne du minuteur ou d'une main humaine ;
  seule la présence ou l'absence de la ligne « minuteur : STOP posé dans course/ à … » (l. 777–778) les distingue. Le
  segment suivant n'est accepté qu'avec `SEGMENT=K+1` (l. 214–215), `CLORE=1` compris.
- **Fait, texte.** La ligne « `STOP` posé par une main humaine » de la liste d'arrêt (l. 403) dit : « elle ne reprend
  que sur décision de Lazar (`SEGMENT=K`), ou se ferme sans reprise (`SEGMENT=K CLORE=1`) », alors que la ligne du
  minuteur (l. 404) et celle de la reprise refusée (l. 406) emploient K pour le segment arrêté et pour le segment
  relancé. Avec la notation de la l. 404, la commande juste est `SEGMENT=K+1` ; et la ligne du minuteur dit que
  session-depot lance le segment suivant sans attendre Lazar, sur la seule foi du `LANCEMENT.md`.
- **Correction.** L. 403 : « … elle ne reprend que sur décision de Lazar (`SEGMENT=K+1`, K étant le segment arrêté), ou
  se ferme sans reprise (`SEGMENT=K+1 CLORE=1`) ; le `LANCEMENT.md` porte alors « reprise attendue » comme pour le
  minuteur : session-depot, qui a posé ce `STOP`, ne lance pas le segment suivant sans le mot de Lazar ; un `STOP` du
  minuteur se reconnaît à la ligne « minuteur : STOP posé dans course/ à … (3400 s après le départ du lanceur) » ». La
  porte de la v6.1 accepte les deux (un `STOP` repris est un `STOP` repris) : à dire aussi l. 414 si c'est voulu.

### P4C3-03 — mineur — « Chaque refus sur un artefact » : plusieurs gardes nouvelles ne sont essayées que sur le cas sain (R5)

- **Noyau** (texte l. 262–265 : « … et chaque refus sur un artefact »). Trois refus de `reprendre()` n'ont pas d'essai
  sur un artefact (`tests/test_reprise_segments.py`, recherche des motifs) : le dernier événement n'est pas l'arrêt
  sur `STOP` (`boucle.py` l. 1037–1039 ; l'essai qui ajoute une ligne au journal déclenche la garde du nombre
  d'événements, l. 1035–1036, avant elle) ; ronde de génération en cours incohérente avec l'état (l. 1063–1064 ; seule
  la variante de conception est essayée) ; vue figée introuvable en mémoire partagée (l. 1065–1068 ; sans objet pour ce
  pilote). Les douze mutations ne les visent pas.
- **Lanceur** (§ Essais l. 443–447 et liste d'arrêt l. 405 : « verrou », « état de reprise »). Sans essai sur un
  artefact : verrou du segment 1 absent (lanceur v6 l. 209) ; autre course de ce nom partie dans un autre dossier
  (l. 211–213) ; dossier sans manifeste au segment K ≥ 2 (l. 208 ; `seg-sans-course` essaie le dossier absent, l. 206) ;
  état de reprise d'un autre arrêt ou d'un autre segment (l. 262–263 ; seul le compagnon faux est essayé,
  `seg-etat-altere`) ; état de plus mais non conforme, course alors fermée avec réserve (l. 820–822) ; code de retour du
  noyau autre que 0 et 9 au segment K ≥ 2 (fermeture, P4C3-07) ; numérotation des reprises seule, à arrêts justes
  (l. 341) ; condition du minuteur au segment K ≥ 2 (l. 769–771 : son seul essai est le cas sain `seg3-segment2`, où
  le `STOP` posé à échéance nulle n'a pas fait refuser la reprise).
- **Portée.** Ces gardes ne jouent que sur un état altéré ou un dossier déplacé, ou doublent un refus antérieur ; aucune
  ne change la course saine. Le texte, lui, affirme davantage que ce qui est essayé.
- **Correction** (texte seul) : l. 264 « … et chaque refus sur un artefact, sauf trois (dernier événement, ronde de
  génération incohérente, vue figée : lus dans le code, non essayés) » ; au § Essais, une phrase : « gardes du lanceur
  lues dans le code, non essayées : … (liste ci-dessus) ». Des artefacts pour elles au prochain noyau et au prochain
  lanceur, pas avant ce pilote.

### P4C3-04 — remarque — Les essais centraux de la reprise ne sont pas cités, et T2 permet de désélectionner les autres

- **Fait.** Le lanceur exige les 45 essais cités (`ESSAIS_CITES`, l. 168 : 29 de `b1c7f4b6` et 16 de la reprise), aucun
  échec, aucun saut, et « passés + désélectionnés = 169 » (l. 655–660 ; règle de T2 l. 388). Deux fonctions de la
  reprise, paramétrées, n'y sont pas : `test_course_en_segments_egale_la_course_continue` (5 cas, l'équivalence de la
  course en segments et de la course continue) et `test_reprise_refusee_si_le_lancement_differe` (7 cas). La variable
  `PYTEST_ARGS` n'est pas refusée en mode réel (l. 84) : une désélection de ces douze cas passerait, consignée
  « … désélectionnés » au `LANCEMENT.md`.
- **Correction** (texte seul) : au § Bornes, segments : « à chaque segment, `PYTEST_ARGS` reste vide ; session-depot
  vérifie au `LANCEMENT.md` « 169 passés, 0 sauté, 0 désélectionnés » ». Au prochain lanceur, citer les douze cas.

### P4C3-05 — remarque — À un code de retour non nul du noyau, le piège d'erreur du lanceur écrit une ligne fausse au `LANCEMENT.md`

- **Fait.** `set +e; wait "$PID"; CODE=$?; set -e` (lanceur v6 l. 787) : sous bash, le piège `ERR` (l. 227) se déclenche
  sur une commande en échec même sans `set -e` (essayé : bash 5.2.21). À une reprise refusée (code 9), le `LANCEMENT.md`
  porte donc « échec inattendu (code 9) à la ligne 787 … ; verrou … laissé (à examiner) », puis « reprise refusée par
  le noyau (code 9 …) », et le verrou du segment est retiré juste après (l. 806) :
  `simulation-lanceur-v6/LANCEMENT-simulation-v5-3-segments.md` l. 142–145. Le code est bien lu (9), le lanceur rend 3 ;
  la porte de la v6.1 ne lit pas ces lignes. Défaut ancien (la même ligne existe depuis le lanceur de T2), sans effet
  jusqu'ici parce que les courses réelles ont rendu 0.
- **Correction.** Une phrase à la ligne « reprise refusée par le noyau » de la liste d'arrêt (l. 406) : « la ligne
  « échec inattendu (code 9) … verrou laissé » que le piège d'erreur inscrit juste avant ne vaut pas : le verrou du
  segment est retiré ensuite ». Au prochain lanceur, `wait "$PID" || CODE=$?`.

### P4C3-06 — remarque — Borne de temps et cas attendu : deux précisions

- (a) **Borne** (l. 278–281 : 3 400 + 2 400 + 900 + 60 + 300 = 7 060 s, juste). Elle omet l'attente de 10 s après l'arrêt
  du groupe de l'organisme (`bac_a_sable.py`, `_lancer`, l. 288–292) et celle du fil du serveur, 5 s (`serveur.py`
  l. 71–72) : 7 075 s, marge de 125 s sous 7 200 s. Le dépôt (60 s) et la fermeture (300 s) sont des estimations, non
  des bornes du code (fermeture observée : 3 à 4 s au pilote 3). La borne suppose aussi un minuteur vivant : s'il meurt
  avant l'échéance (reste de P4C2-12), rien ne le dit et le segment court jusqu'à la fin de la course, au risque de la
  coupure. Le dire, avec ces deux chiffres ; accepter le risque, ou demander à session-depot de vérifier pendant le
  segment que l'identifiant de processus du minuteur, consigné, vit encore.
- (b) « au total, **du noyau** : ≈ 50 à 93 minutes » (l. 292) : ce sont les durées avec la préparation et la fermeture
  (193 + 2 653 + 120 + 3 = 2 969 s ; 196 + 3 218 + 2 160 + 4 = 5 578 s) ; le noyau seul fait ≈ 46 à 90 minutes. La
  conclusion (un ou deux segments par course) ne change pas.

### P4C3-07 — remarque — Au segment K ≥ 2, un code du noyau autre que 0 et 9 ferme la course

- **Fait.** Seuls le code 9 (reprise refusée) et le code 0 avec un état de plus (fin de segment) laissent la course
  ouverte (lanceur v6 l. 804–823) ; tout autre code — refus du noyau à sa construction (code 7, par exemple isolation
  indisponible), exception (code 1) — passe à l'étape 8a, qui ferme la course, alors que rien n'a pu tourner dans ce
  segment ; de même un état de plus non conforme (l. 820–822, fermeture avec réserve). Au segment 1, un refus avant le
  manifeste passe en 8b et permet une tentative de plus. La liste d'arrêt ne le dit pas.
- **Correction** : à la ligne « course arrêtée en cours » (l. 410) : « … ; au segment K ≥ 2, un code du noyau autre que
  0 et 9, ou un état de reprise de plus mais non conforme, ferme la course (étape 8a) : la v6.1 ne part pas ». Ces cas
  sont improbables : les essais du noyau, refaits à chaque segment avant le départ, exercent l'isolation et
  échoueraient vraisemblablement avant (refus du lanceur, course laissée ouverte).

### P4C3-08 — remarque — L'organisme de l'unité suivante n'est pas empreinté dans l'état de reprise

- **Fait.** L'état porte les lignées et le chemin de leur organisme (`boucle.py` l. 988), l'empreinte de l'index de
  l'archive et du manifeste, mais pas l'empreinte de l'organisme qui tournera à l'unité suivante (le successeur recopié
  sous `course/lignees/`) ; `reprendre()` ne vérifie que son existence (l. 1074–1076). Entre deux segments (des minutes,
  ou des heures si Lazar doit décider), ce dossier n'est gardé que par les droits (dossier du pilote 0700, à root).
- **Correction** : rien avant ce pilote (session-depot ne touche pas `course/`) ; au prochain noyau, consigner dans
  l'état l'empreinte d'arbre de l'organisme de chaque lignée active et la comparer à la reprise.

### P4C3-09 — remarque — Petits faits et formulations

- « dépense déjà faite par la course (lue dans son état de reprise, **le seul champ lu**) » (l. 273) : le lanceur lit
  trois champs de l'état (raison de l'arrêt, numéro de segment, dépense ; lanceur v6 l. 262–264) et compte les lignes de
  `course/evenements.jsonl` (l. 746, 770 : le minuteur du segment K ≥ 2 attend l'événement de reprise ; ce journal porte
  les scores, `boucle.py` l. 795, il n'en lit que le nombre de lignes) ; tout est mécanique. Écrire « trois champs
  mécaniques ; le nombre de lignes du journal des événements, pour le minuteur ».
- Ligne de mutation (l. 411) : à g003, un successeur invalide donne « sans successeur valide », ou « sans successeur
  valide après relance » si g003 était elle-même une relance (`boucle.py` l. 845–848).
- Phrase du critère 3 (l. 112) : « deux organismes » est faux si seule la v5.3 part ; ajouter « (un seul si la v6.1 ne
  part pas) ».
- « une course sans `STOP` est inchangée » (l. 96) : ses événements et son archive le sont ; son rapport porte deux clés
  de plus, `segments` et `reprises` (`boucle.py` l. 1145–1146), que l'extrait ne recopie pas (`CHAMPS_RAPPORT`).
- § Pièces : ne nomme ni le fichier de cause de la série v7 (`essais-lanceur-pilote4-v7.cause.txt`), ni les essais et
  le journal du script de scellement v2, ni les dérivations des batteries v1 à v5, ni les écarts du lanceur de P3 aux
  lanceurs v1 et v2 et du v1 au v2 ; tous sont au fichier d'empreintes (309 lignes justes). « et toutes les autres
  pièces du dossier » suffit.
- Chaque segment lit le registre des GO et celui des dépenses sur `origin/main` (lanceur v6 l. 523, 530) : dire
  « `git fetch origin main` avant chaque segment, sans changer la tête de la copie ».
- Les deux marqueurs de rédaction (entre doubles crochets, l. 7 et 539) sont refusés par le script : ils se remplissent
  à la main avant lui (la demande de contre-lecture dit qu'il les remplit ; ce n'est pas le cas, et le texte ne dit pas
  qui le fait). Le détail inséré cite l'empreinte relue par chaque contre-lecture (v1 `312c9993…`, v2 `8657fcd2…`, v3
  `efffb7e4…`), puisque le texte scellé gardera le nom de la v3 avec une autre empreinte.
- L'écart publié du lanceur v5 au v6 a pour en-tête une copie dans le dossier de travail de l'auteur
  (`/tmp/claude-0/…/scratchpad/pilote4/lanceur-v5/…`) ; son contenu est l'écart recalculé entre les pièces : sans effet.
- Formes des lignes de dépense datées `2026-10-25` (l. 338–340) : un segment peut partir un autre jour ; le lanceur ne lit
  pas la date.
- Batterie : la vérification `seg-segment2-stop-retire` est remplie par la note de l'essai 6 (reprise refusée), l'essai
  sain 7 n'ayant plus de `STOP` à retirer ; sans portée (le noyau refuse toute reprise avec `STOP` présent, essai
  `test_reprise_refusee_stop_present`).

### P4C3-10 — conforme — Ce que j'ai trouvé conforme

- **Empreintes** (recalculées sur disque) : texte `efffb7e4…`, v2 `8657fcd2…`, P3 `57c8535a…`, T2 `d2944654…`,
  contre-lectures 1 `3dd09acb…` et 2 `7c625fa6…` ; lanceurs v6 `50f9c496…`, v5 `565f5205…`, v4 `f335440c…` ;
  dérivations `1e958eeb…`, `d97e89b3…`, `a9d74961…`, `553eeb4c…` ; écarts `de55a332…`, `ebc39db9…` ; batteries v7
  `c3263af1…`, v6 `b4857c51…`, v5 `e216c39e…` ; journaux v8 `b5673d17…`, v7 `e049220b…`, v6 `fa734f52…` ; script de
  scellement v3 `aee63b20…` ; note du noyau `13624795…`, mutations `f2db1ec8…` (compagnons des six fichiers de la note
  justes) ; faits `325b9332…` et `609ccf1f…` (compagnons justes), extraits recopiés `f07e059a…`, `d357a6fe…`,
  `24cd458a…`, `ce66dce9…`, `LANCEMENT.md` `81626514…` et `b4f7abb2…` ; banque v3 `157a2b45…`, v2 `52beb637…`, v1
  `f1387a20…` ; `LISEZMOI-v5` `d346bac1…`, `-v6` `5a387a74…`, `EMPREINTES-banque-v3-v1` `2a661a33…` ; contre-lectures
  de la banque v2 `5ee8df41…`, v3 `da6b744c…`, v4 `ea2916af…`, v5 `0ea27fa1…` ; références `52def946…`, `912752ff…`,
  `556d6398…` ; demande de v6.2 `f1551187…` ; lanceur v2 de P3 `add695a9…`. Les 37 empreintes pleines et les 33
  préfixes cités par le texte sont tous retrouvés, sauf ceux des pièces non lues (§ en-tête).
- **Fichier d'empreintes des pièces** `EMPREINTES-pieces-pilote4-v4.txt` (`06552f74…`, compagnon juste) : 309 lignes sur
  309 justes ; il couvre toutes les pièces du dossier et de ses sous-dossiers, sauf lui-même et son compagnon.
- **Noyau.** Écart fourni appliqué aux fichiers d'avant : `boucle.py` et `cli.py` identiques à ceux de la copie
  `8e5e2f7b` ; empreintes « blob » `b76c9a3` → `c50d30a`, `b5dca5e` → `3ad4c18`, essais `042732e`, comme les en-têtes de
  l'écart ; empreinte d'arbre `61ddd638…` (17 fichiers), la même dans la copie de travail du pilote 4 ; 124 + 17 = 141
  fonctions d'essai anciennes, 28 cas nouveaux (169) ; suite complète « 169 passed in 233.29s » après la dernière
  modification du code (20:12:47 UTC → 20:15:35 UTC) ; mutations v2 faites sur le `boucle.py` publié (`8b594096…`), les
  douze détectées. Le comportement lu : `STOP` lu par `_doit_arreter` seulement (l. 862–872), avant chaque lignée d'une
  ronde (l. 887), chaque ronde de conception (l. 902) et chaque ronde de génération (l. 933) ; état écrit sous un nom
  neuf, scellé, protégé (l. 969–1001) ; ronde en cours gardée (ordre tiré, lignées faites) et continuée sans nouveau
  tirage (l. 880–893, 917, 960) ; graines : même entropie (comparée), même indice de lignée ; dépense et nombre
  d'appels relus de l'état, jamais recomptés ; refus avant toute écriture, l'événement de reprise venant en dernier
  (l. 1098) ; jamais deux reprises d'un même état (nombre d'événements) ; arrêt en conception sans génération notée
  (l. 927–931) ; course sans `STOP` : mêmes événements qu'avec `b1c7f4b6` (chemins comparés pas à pas). Champs comparés
  à la reprise (`CHAMPS_REPRISE`) : bornes, graine, banque, mission, code et commit, versions, isolation, espace,
  clés présentes, sources, question (sans son chemin), organismes imposés (famille, empreinte d'arbre) ; l'espace des
  organismes ne dépend que du chemin de la course (`bac_a_sable.espace_organismes`, gardé à la reprise) ; la question
  et l'archive n'ont pas d'état en mémoire (`question.py` l. 88–90 ; `archive.py`). Mes 28 essais passés.
- **Lanceurs.** v5 redérivé du v4 (37 remplacements) et v6 du v5 (3 remplacements), identiques octet pour octet ; les
  deux écarts publiés sont les écarts recalculés. Le v6 fait ce que dit le texte : segments et ordre (l. 186–224) ; un
  verrou par segment, celui du segment 1 gardé jusqu'à la fin ; même lanceur, même tête ; organisme et question du
  segment 1 revérifiés, jamais réécrits (l. 504–514) ; ligne de dépense « segment K » (l. 532–534) ; reste du GO ≥ 75 USD
  moins la dépense faite (l. 541–543) ; pièces de chaque essai dans `segment-K-tA/`, sortie standard fermée par segment ;
  `STOP` retiré avant la reprise (l. 747) ; `--reprendre` (l. 739) ; minuteur à 3 400 s du départ de chaque segment,
  posé au segment K ≥ 2 seulement après l'événement de reprise (l. 769–779) ; fin de segment sans fermeture ni poussée
  (l. 811–819) ; code 9 : course ouverte, rend 3 (l. 804–810) ; `CLORE=1` sans registre, test, essais ni course, avec
  `cd` vers le dépôt (l. 796–800) ; porte « v5.3 précédente » (l. 304–306, 338–342) ; 75 USD (l. 114). Variables sous
  `set -u` toutes définies sur chaque chemin (segment 1, K ≥ 2, `CLORE`, réel et simulation) ; dossier courant juste
  pour l'extrait dans les deux chemins ; aucun fichier réécrit hors du compagnon du `LANCEMENT.md`, réécrit à dessein.
- **Batteries et séries.** v6 redérivée de la v5 (9 remplacements) et v7 de la v6 (4), identiques. Série v8 : 218 cas
  sur 218, 20:43:13–20:54:02 UTC ; 162 − 4 + 60 cas nouveaux de segments = 218 ; mêmes noms de cas et même ordre que
  la série v7. Cause de la série v7 juste : avec `CLORE=1`, l'extrait se lançait hors du dépôt (« No module named
  'essaim_m3' »), d'où l'absence d'extrait et le refus de la porte pour une autre raison ; et la batterie v6 lisait
  la sortie du segment 1. Simulation des segments, relue dans les extraits : deux segments, `STOP` lu avant la
  ronde 2, reprise avec 6 appels et 0,088 USD relus, sortie de conception sans ronde, g000 à g003 ; trois segments,
  second arrêt après g000, 129 appels et 1,896 USD relus (6 + 123 ; 0,088 + 1,808), g001 à g003 au segment 3 ; appels
  par unité 6, 123, 129, 123, 123 comme la course continue ; fins « aucune lignée active ». Les frontières de segments de
  ces cas dépendent du minuteur (sondage à la seconde), leurs vérifications non.
- **Script de scellement v3** : documentation juste ; numpy ≥ 1.25 ; quatre marqueurs exactement, une fois chacun ;
  entropie par `secrets.randbits(128)`, enfants 0 et 1 de `SeedSequence(E).spawn(2)`, comme le lanceur les recalcule ;
  contre-lecture du texte exigée sous le nom `pilote4-gemini-organisme-v3-clN.md`, avec un compagnon au format
  « empreinte, deux espaces, nom » (celui de ce rapport l'est) ; refus d'écraser le fichier d'empreintes. Les marqueurs
  du texte relu sont là, chacun une fois (l. 7, 341, 346, 347, 506, 539), une seule ligne d'entropie, deux lignes de
  graine ; la ligne de GO porte les chevrons simples à dessein, que ni le script ni le lanceur ne prennent pour un
  marqueur.
- **Chiffres** : 6 × 25 + 3 × 145 + 300 = 885 s ; 3 400 + 2 400 + 900 + 60 + 300 = 7 060 s ; 3 × 607 + 832 = 2 653 s,
  3 × 751 + 965 = 3 218 s ; 15:37:44 → 15:40:57 = 193 s, 16:07:02 → 16:10:18 = 196 s ; 3 400 − 200 ≈ 3 200 s ≈ 53 min ;
  6 × 1 810 + 4 × 3 310 = 24 100 s ≈ 6,7 h, 3 segments de deux rondes et 4 d'une génération = 7 ; 2 × 75 = 150 ;
  (75 − 18) / 4 = 14,25 ; 185 − 30,23 − 150 = 4,77 ; 15,1161 + 15,1136 = 30,2297 ; 3 × 6,55 + 8,23 = 27,88 ;
  4 × 8,63 = 34,52 ; 60 recherches et 30 téléchargements ; ≈ 10 recherches web par course. Faits relus dans
  `faits-pilote3-v1/` : durées 661,06 / 838,03 s (v5.3), 610,83 / 864,09 s (v6), 750,91 / 831,59 s (M),
  607,0 / 964,55 s (S) ; coûts 6,7932 / 8,3229, 6,5495 / 8,5642, 6,6896 / 8,2273, 6,6672 / 8,6281 USD.
- **Objets et banque** : arbres v5.3 `6251ab21…` (22 fichiers) et v6.1 `ae331d1d…` (24 fichiers) recalculés ; v6.1
  l. 926–933 (stagnation, disjonction) et l. 1985–1990 (fin de conception), v5.3 l. 1799–1804 ; référence de
  provenance 0,8056 / 0,8333, oracle 0,8889 / 0,8056, catégories absentes du train 8 (4 et 4) et 14 (10 et 4) ;
  référence de paire 1,0 / 0,75 (longueur 1,0 / 0,75, mots des lignes propres 1,0 / 0,75, nombre de mots 1,0 sur
  `test`) ; les treize points de la demande de v6.2 sont ceux qu'énumère le texte (§ 2, points 1 à 13).
- **Cohérence.** Table de correspondance, liste d'arrêt et plan d'analyse disent la même chose des segments, du
  minuteur, de la porte et des 75 USD ; les noms d'essais cités par la liste d'arrêt existent dans la série v8 ou dans
  les essais du noyau. Ce qui reste au mot de Lazar est dit, sur la ligne de GO : objets et arbres, points ouverts de la
  v6.1, banque v3, question M, texte, lanceur et noyau, 4 générations, 6 rondes à 3 USD et 900 s, 75 USD par course tous
  segments compris, 60 recherches dont ≈ 10 web et leur coût, segments (minuteur, test et ligne de dépense par segment),
  185 USD pour le GO. Dans les trois cas soumis à Lazar le texte tient : v6.1 nommée et acceptée (ligne entière) ; seule
  la v5.3 (ligne sans la clause de la v6.1, refus de la v6.1 essayé, moment de lecture après la v5.3) ; une v6.x plus
  tard sous un texte à part.
