# Contre-lecture du registre d'hypothèses de conception v2, du protocole v1 et des briefs d'agents v1 de la boucle extérieure du pilote 4 — rapport v1

## En-tête

- **Contre-lecteur** : sous-agent neuf (`claude-opus-5-5`), lancé par conv-audit le 26 octobre 2026. Je n'ai écrit ni les
  textes relus, ni aucune pièce fournie, ni le brief.
- **Heure** : rapport écrit le 2026-10-26 à 04:26:21 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne). Mon heure de
  début n'est consignée par aucune commande d'écriture (écart 3).
- **Brief** : `/home/claude/canal-conv-audit-n04/brouillons/canal-reprise-releve-v1/envois/boucle-exterieure-pilote4-v1/BRIEF-contre-lecture-boucle-exterieure-v1.md`,
  `33ea90d46c78ebc714346dad7efb566137bd6c799ea0245214e4b087acdf1a57`, vérifiée avant lecture : égale ; compagnon juste.
- **Textes relus** (`/var/tmp/boucle-exterieure-pilote4-v2/sortie/`), empreintes vérifiées par `sha256sum -c` de leurs
  compagnons avant toute lecture, toutes égales à celles de la demande :
  - `registre-hypotheses-conception-pilote4-v2.md`, `3881fa16070be8824f9b4d7987a432dc23ad34d31df7a3d971ffbc65ab433623` (560 lignes) ;
  - `protocole-boucle-exterieure-pilote4-v1.md`, `23e4e1ba07b04f43021a39cc66cc41711c0244649597a0bb420b04d488b090a4` (379 lignes) ;
  - `brief-agents-fin-de-course-v1.md`, `b5f61890ac40b3f232f6b92a4f1c6d15742e2e19bf845798525f6d1c209bbdfd` (222 lignes) ;
  - `LISEZMOI-sortie-v2.md`, `4c312a5aa7dbcf28da0703b5f4bdcf87c4f01b50544fea07fd43d95306e46a0b` (92 lignes).
- **Ce qui fait foi** : `LISEZMOI-brief-v2.md`, `bb472681e1bd1216ad2e3b4ea4364d8b07f6b23c5fabbd52673eaa117f47a661` (égale
  au préfixe du brief) ; `fournis/` : douze fichiers sur douze conformes à `EMPREINTES-fournis-v1.txt` (`7b5c6821…`), dont
  le texte du pilote `pilote4-gemini-organisme-v4.md`, `782b858c…` (égal), qui prime.
- **Fait transmis par conv-audit, que je n'ai pas vérifié** (aucun dossier de course ouvert) : la première course
  (v6.2.1) est partie à 03:51 UTC ; son dossier s'appelle `pilote4-gemini-v6-2-v1-tentative2` (suffixe ajouté par le
  lanceur après un refus avant le manifeste).
- **Conventions** : les numéros de lignes sont ceux des fichiers nommés. « Registre », « protocole », « briefs »,
  « LISEZMOI » désignent les quatre textes relus ; « texte v4 », le texte du pilote ; « P4v3 », sa v3 ; « (A) », « (B) »,
  « (C) », la sortie du script, le relevé mécanique, le code de l'objet (registre § 0.1). Ce rapport ne contient aucun
  score, aucun critère ni aucune stratégie de classement des tâches.

## Lu, exécuté, non ouvert

- **Lu en entier** : le brief ; les quatre textes ; `LISEZMOI-brief-v2.md` ; `fournis/brief-boucle-exterieure-v1.md` ; le
  texte v4 ; la contre-lecture 7 (`pilote4-gemini-organisme-v4-cl7.md`) ; le registre v1 ; le brief du script de
  lecture ; les deux synthèses du collisionneur ; les hypothèses du pilote décisif (b).
- **Lu en partie** : P4v3 (l. 110–244 et 380–439, et les lignes trouvées par `grep`) ; le relevé v7 des mots de Lazar
  (en-tête, puis les lignes de 00:49 à 03:48 par `grep`) ; le dessin de la primitive d'expérience (l. 1–20) ; la question
  « agents sur le noyau » (l. 1–25).
- **Exécuté** : `sha256sum` et `sha256sum -c` ; `ls`, `wc`, `grep` dans les deux dossiers nommés ; `python3 -I -c` (nombres
  sans aucun score, aucun fichier écrit) ; un essai de `diff` sur deux arbres inventés, sous mon dossier de sortie
  (`essai-diff-ru-v1.log`, `251f543e5df638672d7bb780256d6ddbbe733f1272bdd336904e4a935992666e`, compagnon juste) ; `date -u`.
- **Non ouvert** : aucun fichier de banque, aucune archive fermée, aucun dossier de course, aucun extrait ni journal
  d'appels, aucun code d'organisme, aucun script du pilote. Aucun `git`, aucun sous-agent, aucun réseau, aucune clé.

## Verdict

**Utilisable après corrections.**

Aucun constat bloquant ; onze à corriger avant usage (CLB-01 à CLB-11) ; huit mineurs (CLB-12 à CLB-19). Le cœur tient :
les deux fiches que visait la contre-lecture 7 sont « indécidables par ce pilote », avec ce qu'il faudrait pour les
trancher ; les nulles existent ; le calendrier de Holm est juste ; la retenue de lecture est écrite partout. Ce qui manque
relève de l'exécution : un relevé mécanique qui n'existe pas encore ; le nom réel du dossier de la première course ; des
gardes qui ne voient pas tout (fichiers nouveaux d'une correction, facteurs, contenu interdit) ; deux chemins par
lesquels les deux courses se rencontrent ; quatre règles qui contredisent le texte v4 ou le registre lui-même
(CLB-03, 04, 09, 11) ; et un effort de correction que rien n'égalise entre les deux objets avant le pilote décisif (b).

Ordre proposé : pousser telles quelles les quatre pièces relues, avec leurs empreintes, avant la fin de la première
course (texte v4, l. 155–156) ; écrire leurs versions corrigées (noms nouveaux, R12) avant l'ouverture de la lecture,
sans lire aucun fait ni score de course ; faire relire l'écart.

## Décidabilité, fiche par fiche (point 1 du brief)

| fiche | objet | se tranche par | état |
|---|---|---|---|
| HC-P4-01 | les deux | relevé (B) : ronde de la déclaration de fin | décidable si (B) existe (CLB-02) |
| HC-P4-02 | les deux | — | « indécidable par ce pilote », avec ce qu'il faudrait (classes d'au moins 26 et 16 tâches) : conforme à P4C7-01 |
| HC-P4-03 | v6.2.1 | (B) : appels de mutation, successeur valide ayant tourné | décidable si (B) porte ces champs |
| HC-P4-04 | v6.2.1 | (B), score de `test` rendu (absent de la sortie prévue), opération (2) | aujourd'hui « non observable » ; CLB-03 |
| HC-P4-05 | les deux | comme HC-P4-04 | comme HC-P4-04 ; énoncé sur les scores, CLB-03 |
| HC-P4-06 | v6.2.1 | (B) : castes, rôles des appels | décidable si (B) les porte |
| HC-P4-07 | les deux | (B) : coûts, durées, statuts, segments | décidable si (B) existe |
| HC-P4-08 | les deux | nombre de tâches sans réponse (absent de la sortie prévue) | « non observable » tant que le script ne le rend pas ; CLB-04 |
| HC-P4-09 | les deux | (B) : recherches par ronde | décidable si (B) les compte par ronde |
| HC-P4-10 | comparaison | — | « indécidable par ce pilote », avec ce qu'il faudrait (pilote décisif (b)) : conforme à P4C7-02 |
| HC-P4-11, HC-P4-12 | chaque course | sortie du script, test (iii) | décidables par la sortie seule ; mais l'agent n'y arrive qu'après l'étape 3 des briefs, qui lit (B) |

Ni le libellé (ii) ni les scores sur les catégories absentes du train ne fondent une fiche (registre l. 68–73 et
518–521) : conforme.

## Constats

### CLB-01 — à corriger avant usage — Le nom de la première course n'est pas celui de son dossier

- **Où** : registre l. 166 et l. 38 (`lecture-<nom de course>-v1`) ; protocole l. 228 (§ 9), l. 40 et 85–88 (noms en
  `<course>`) ; briefs l. 12 (exemple de `<course>`), 46, 48, 99–100, 124.
- **Ce qui ne va pas** : les trois textes prennent `pilote4-gemini-v6-2-v1` pour nom de la course et, par l'exemple des
  briefs, pour valeur de `<course>` dans tous les noms de fichiers du dossier de lecture. Le dossier réel s'appelle
  `pilote4-gemini-v6-2-v1-tentative2`. Aucun texte ne prévoit une nouvelle tentative (la seule permise sans Lazar après un
  refus avant le manifeste, P4v3 l. 357–358). Trois suites : on ne sait pas si `<course>` est le nom du texte ou celui du
  dossier ; si le script nomme sa sortie d'après le dossier, `lecture/lecture-<course>-v1.md` ne la trouve pas, et la
  renommer casse son compagnon, qui porte le nom nu ; si un dossier au nom simple reste de la tentative refusée,
  l'assemblage peut le prendre.
- **Correction** : écrire au protocole (§ 3 et § 9) et au mode d'emploi des briefs que `<course>` est le nom exact du
  dossier que session-depot a poussé pour la course qui a tourné ; que les sorties du script et du relevé gardent les noms
  que leurs auteurs leur donnent, jamais renommées ; que le dossier se choisit par l'identité du § 9 (commit, arbre,
  nombre de fichiers, graine du manifeste), non par son nom ; qu'un dossier de tentative refusée n'est jamais lu.

### CLB-02 — à corriger avant usage — Le relevé mécanique (B) n'existe pas, et toute la boucle en dépend

- **Où** : registre l. 41–44 et lignes « Entrées » des fiches HC-P4-01, 03, 06, 07, 09 (en partie 04, 05, 08) ; protocole
  l. 88–107 et l. 375 ; briefs l. 48–50 ; LISEZMOI l. 30 (choix 1), l. 60 et l. 62.
- **Ce qui ne va pas** : cinq fiches ne se tranchent que par (B), trois en partie. L'étape 3 de chaque agent (fin de la
  course) se lit aussi dans (B) : sans lui, tout agent s'arrête, avant même les fiches de `test_final`. Or (B) n'a ni
  auteur désigné, ni script, ni essai (R5), ni nom fixé (« proposé »). Ces fiches ne sont donc aujourd'hui ni tranchées
  par la sortie du script, ni déclarées « indécidables par ce pilote » (point 1 de mon brief). Leur lecture de (B) repose
  sur le choix 1 du LISEZMOI : le point 4 du brief v2 (« les agents ne voient que la sortie du script de lecture ») lu au
  sens du texte v4, point 3 (« du script de lecture, ils ne voient que la sortie »). Cette lecture est défendable — le
  texte v4, qui prime, n'interdit aux agents que textes de tâches, vérités et clés (l. 383–385), et le brief v1 nommait
  les faits mécaniques —, mais elle n'est pas tranchée.
- **Correction** : avant l'ouverture, conv-audit tranche le choix 1. Si oui : auteur du script du relevé désigné ; nom et
  champs fixés ; essai sur un cas sain (pièces de simulation de la série v13) et sur un artefact (champ de texte planté) ;
  script et sortie empreintés ; une phrase qui dit que le relevé d'une course est produit et poussé sans être affiché sous
  la retenue (il porte des bits sur les scores de `test`, registre l. 179–181). Si non : ces fiches deviennent
  « indécidables par ce pilote », avec ce qu'il faudrait (un relevé), et l'étape 3 des briefs lit la fin de la course dans
  une autre pièce de session-depot.

### CLB-03 — à corriger avant usage — Opération (2), HC-P4-04 et HC-P4-05 : comparaisons hors de la levée, permises par défaut, corrections suspendues au bruit

- **Où** : registre l. 100–105 (opération (2)), l. 285–300 (HC-P4-04), l. 307–310 et 319–328 (HC-P4-05), l. 157–159
  (§ 0.6) ; briefs l. 18 et 74–77 ; LISEZMOI l. 35 (choix 6) et l. 61 ; texte v4 l. 385, 387–389 et 425–430.
- **Ce qui ne va pas** :
  - (a) Le texte v4 ne lève l'interdit que pour deux comparaisons (un score et sa référence ; les générations 0 et 3
    d'une même course) et garde « aucune autre différence calculée » (l. 429–430) ; les agents en restent tenus
    (l. 387–389) et ne changent pas ses règles (l. 385). L'opération (2) calcule d'autres différences sur `test`
    (génération 1 moins génération 0, génération 2 moins génération 1, meilleur ancêtre moins dernier score). Le registre
    la permet sauf refus de conv-audit : le défaut va contre le texte qui prime, et une pièce de la boucle ne peut pas
    élargir sa levée.
  - (b) L'énoncé de HC-P4-05 (« la condition se présente au moins une fois ») porte sur la trajectoire des scores de
    `test`, non sur le code : son verdict est lui-même une comparaison de générations autres que 0 et 3.
  - (c) Les conséquences « tenue → correction candidate » (l. 294–298 et 324–326) suspendent une proposition de relance
    payante à un événement de bruit ; le registre le dit : une non-hausse a une chance d'environ une sur deux à chaque
    génération (l. 295–296, illustratif). C'est ce que le § 0.6 du registre interdit (« aucune correction de la ronde
    suivante n'est motivée par un score seul »), et c'est une règle de décision sur des scores au-delà des quatre tests
    du point 4 bis (point 2 de mon brief).
- **Correction** : « non permise » par défaut (registre § 0.2 ; briefs l. 18) ; une permission demanderait une version
  nouvelle du texte du pilote ou un mot de Lazar. Si elle est donnée : réduire HC-P4-04 et HC-P4-05 à la conformité du
  code (l'appel de mutation, ou la restauration, a lieu si et seulement si la condition du code est remplie), déclarées
  descriptives quant aux scores ; rapporter la survenue de la condition comme un fait, sans verdict. Si les deux seuils
  méritent correction (seuil sous le poids d'une tâche, registre l. 148–153), le soumettre comme un point de conception a
  priori, indépendant de ce que la course montre.

### CLB-04 — à corriger avant usage — Le registre fait recopier des valeurs de `test_final` qu'il interdit

- **Où** : registre l. 449–451 (b et c : « on les cite comme des comptes ») et l. 387–388 (nombre de tâches sans réponse
  « rapporté », cellules de `test_final` comprises) ; contre registre l. 106–107 et 496–497, protocole l. 144 et 356
  (« compte »), briefs l. 66 ; gardes G3 et G8 (protocole l. 265 et 270). De plus, briefs l. 116–118 (comparer une valeur
  p brute à 0,05) contre registre l. 100–105 et briefs l. 74–77.
- **Ce qui ne va pas** : un analyste qui suit HC-P4-11 ou HC-P4-08 rend une pièce que G3 et G8 refuseraient. L'étape 6 de
  l'analyste lui fait, en plus, comparer une valeur p de `test_final` à un seuil, opération absente des seules permises.
- **Correction** : pour `test_final`, coordonnées et libellés seulement. Le sens d'un rejet, « aucune tâche sans réponse »
  ou non, et « non-rejet final » ou « en attente de la lecture finale » deviennent des libellés que le script écrit
  lui-même : à demander dans la version nouvelle du script (LISEZMOI, point 3.6), à la place de b, c et des comptes.

### CLB-05 — à corriger avant usage — Les deux courses se rencontrent par le journal et par la lecture finale de Holm

- **Où** : protocole l. 139–141 (un seul journal pour la boucle), l. 110–112 (sa dernière version dans chaque dossier de
  lecture), l. 153 (verdicts au journal), l. 330–333 (§ 13), l. 86–87 et l. 76 ; briefs l. 98–100 et 145–146 ; registre
  l. 502 ; LISEZMOI l. 63.
- **Ce qui ne va pas** :
  - (a) Le journal, unique pour les deux objets, porte les verdicts de chaque course, libellés (iii) compris. Les agents
    de la v5.3 liront ceux de la v6.2.1 ; l'analyste neuf du § 13 lira ceux de la v5.3. C'est le chemin vers la
    comparaison que P4C7-02 ferme ; contraire au registre (« aucune pièce ne cite un nombre ou un verdict de l'autre
    course ») et à la liste interdite (« pendant la lecture d'une course : la sortie de l'autre course »).
  - (b) Le § 13 redit les verdicts finals « à partir du seul fichier de la v6.2.1 ». Ce fichier n'existe que si une
    version nouvelle du script rend un fichier par course sans les valeurs p de l'autre (LISEZMOI, point 3.6 : « à
    demander »), sous un nom nouveau : le script refuse d'écraser (R12 ; brief du script, l. 73–75) et le § 3 ne nomme que
    `-v1`. Sinon, la lecture finale met les deux courses dans une même sortie.
- **Correction** : un journal par objet, ou, dans le dossier de lecture, un extrait empreinté réduit aux entrées de
  l'objet ; G6 appliqué à ce qui est servi. Au § 3 et au § 13 : nom et version de la sortie finale, un fichier par course,
  sans aucune valeur de l'autre course ; le § 13 ne s'applique qu'une fois cette version écrite et essayée.

### CLB-06 — à corriger avant usage — « Un facteur à la fois » : la garde ne voit pas les fichiers nouveaux et ne connaît pas les facteurs

- **Où** : briefs l. 171–172 (`diff -ru`), l. 153–154, l. 199 et 207–211 ; protocole l. 175–186 (§ 6), l. 168 et l. 267
  (G5).
- **Ce qui ne va pas** :
  - (a) `diff -ru` sans `-N` n'écrit, pour un fichier nouveau, qu'une ligne « Only in … », sans son contenu (essai :
    `essai-diff-ru-v1.log`). La liste d'accompagnement ajoute des fichiers nouveaux (`CORRECTIONS-v<N>.md`,
    `tests/test_corrections_v<N>.py`) : leur contenu échappe au contre-lecteur, qui ne lit que le diff, au script G5, qui en
    compare les blocs, et au contrôle « l'écart entre les deux commits est le diff transmis » (protocole l. 185–186).
  - (b) Le périmètre est déclaré « avant » le diff, mais rendu dans la même pièce : rien n'en prouve l'ordre. G5 compare
    le diff à un périmètre que le correcteur peut élargir ; l'artefact de G5 (seuil de stagnation et seuil du retour
    arrière) passe si le périmètre déclaré couvre les deux.
  - (c) « Les deux seuils du critère de fin, comptés ensemble » (protocole l. 168 ; registre l. 214) est une définition :
    deux paramètres comptés pour un facteur.
- **Correction** : `diff -ruN` ; une pièce de périmètre rendue et empreintée avant l'écriture du diff ; une carte
  « facteur → fichiers, fonctions, plages de lignes », écrite d'avance par conv-audit depuis la liste du § 6 et lue par
  le script G5 ; un artefact de G5 de plus (périmètre déclaré qui couvre deux facteurs : refusé). Faire confirmer (c)
  (LISEZMOI, choix 23).

### CLB-07 — à corriger avant usage — Contenu interdit du correcteur : vérifiable par un tiers en partie seulement, et jamais essayé

- **Où** : protocole l. 350–360 (§ 14), l. 265–266 (G3, G4) et l. 270 (G8) ; briefs l. 155–157 et 207–211.
- **Ce qui ne va pas** (point 5 de mon brief : la garde est-elle vérifiable par un tiers, et par quoi ?) :
  - connaissance d'une tâche : oui, par construction (le correcteur ne reçoit aucune donnée par tâche : la sortie du
    script n'a que des agrégats, le relevé aucun texte), et G4 cherche noms interdits, marqueurs et chaînes tirées de (A) ;
  - valeur de `test_final` : en partie, par marqueurs (G3, G8) et par G4 ; une valeur transformée (un seuil choisi
    d'après une cellule) ne se détecte pas ;
  - critère ou stratégie de classement : seulement par la lecture du contre-lecteur (partie B, étape 4). Aucun contrôle
    mécanique, et aucun essai sur un artefact (R5) : aucun dossier d'audit ne présente au contre-lecteur une correction
    interdite.
- **Correction** : une liste close des zones du code de l'objet que le correcteur ne touche pas (consignes des rôles qui
  répondent aux tâches, analyse de la réponse qui fixe une classe, constantes de mots-clés C-16, …), sauf un « défaut du
  chemin des réponses » déclaré et revu à part (protocole l. 359–360) ; écrite par conv-audit depuis le code, lue par le
  script G5. Et un essai R5 : un diff synthétique qui porte un contenu interdit de la liste du § 14 (choisi par l'auteur
  de l'essai, gardé hors des pièces de la boucle) doit être refusé par G5 et par le contre-lecteur.

### CLB-08 — à corriger avant usage — Audit des agents : faisable, mais pas aveugle tel qu'écrit

- **Où** : protocole l. 278–297 (§ 12.1), l. 110–112 et l. 157 (journal), l. 264 (G2) ; briefs l. 22, 46–47, 79–80,
  98–100 et 104–106 ; registre l. 360–361 ; texte v4 l. 459–460 et 472–473 ; `LISEZMOI-brief-v2.md` l. 12–13.
- **Ce qui ne va pas** :
  - (a) Le dossier d'audit porte le journal, qui consigne les audits et les lectures réelles (protocole l. 157) : il dit
    à l'agent où il en est.
  - (b) Tiré d'une course simulée, son relevé portera des coûts et des durées de simulateur : la série v13 relit
    1,9544 dollars après 130 appels (texte v4 l. 472–473) et a fait ses 229 cas en moins de 11 minutes (l. 459–460), quand
    le registre annonce environ 30 à 55 dollars par course (l. 360–361, illustratif).
  - (c) L'analyste s'arrête à tout écart d'identité (briefs l. 104–106). Une course de la série v13 porte
    vraisemblablement d'autres graines que celles du texte (tirées à son scellement, vers 03:00 UTC, après la série) ; et
    une sortie calculée sur une banque synthétique passe par les empreintes surchargées « réservées aux essais » du
    script, que sa sortie montre peut-être.
  - (d) G2 accepte tout fichier d'ouverture « qui cite une décision » : un dossier d'audit doit en porter une fausse, que
    ni l'agent ni G2 ne distinguent d'une vraie.
  - Le brief promet un dossier « indiscernable d'un dossier réel » (briefs l. 79) ; le protocole ne dit pas comment.
- **Faisabilité** : oui, avec ce que le script produit (ses essais construisent déjà banque et dossiers synthétiques) et
  les pièces de la série v13, à condition de forger identité, coûts, durées, journal et ouverture, puis de refaire
  manifeste et compagnons.
- **Famille de l'agent qui « casse exprès »** : conforme — paramètre laissé à Lazar, sans valeur par défaut (protocole
  l. 312–315 et 373 ; briefs l. 20 et 190 ; LISEZMOI l. 72).
- **Correction** : écrire au § 12.1 comment un dossier d'audit est construit (identité de l'objet réel ; coûts et durées
  plausibles ; journal et ouverture de même forme qu'un dossier réel ; manifeste et compagnons refaits ; sortie du script
  sans trace de la surcharge) ; liste d'audit gardée par conv-audit seul. Pour G2 : l'ouverture cite une référence
  vérifiable (ligne du registre des décisions ou message du canal, avec empreinte), contrôlée par conv-audit avant
  l'assemblage. Dire que la mesure de l'audit est l'accord avec les verdicts attendus écrits par conv-audit : elle éprouve
  aussi sa propre lecture du registre.

### CLB-09 — à corriger avant usage — La « ronde d'isolement » ne peut rien attribuer

- **Où** : registre l. 463–466 (HC-P4-11 ; HC-P4-12 par renvoi, l. 475–476), l. 458–460 et l. 160–162.
- **Ce qui ne va pas** : attribuer un changement à un mécanisme demande de comparer la course d'isolement à celle qui a
  montré le changement ; le registre l'interdit (« jamais par la différence entre deux rondes »), et, à une graine, un
  non-rejet ne montre pas une absence d'effet (l. 458–460). La conséquence proposerait une relance payante qui ne peut
  pas répondre à sa question.
- **Correction** : l'attribution est « indécidable par ce pilote » ; ce qu'il faudrait : plusieurs graines avec et sans
  le mécanisme, sous un texte nouveau qui fixe test et seuil (comme le pilote décisif (b)). Retirer la ronde d'isolement
  des conséquences, ou ne la garder que si son propre texte fixe un test décidable.

### CLB-10 — à corriger avant usage — Symétrie : rien n'égalise l'effort de correction des deux objets avant le pilote décisif (b)

- **Où** : protocole l. 213–217 (§ 8) et l. 191–195 (§ 7) ; registre, fiches HC-P4-03, 04 et 06 (v6.2.1 seule) ;
  `hypotheses-pilote-decisif-b-v1.md` l. 19–21.
- **Ce qui ne va pas** : trois fiches ne concernent que la v6.2.1 ; une seule correction est propre à la v5.3 (décalage
  d'indice, HC-P4-01) ; la règle d'arrêt (§ 7, point 2) arrête plus tôt l'objet qui a le moins de leviers. Les versions
  corrigées entrent dans (b), qui compare les deux objets. Un effort de correction inégal penche la comparaison vers
  l'objet le plus corrigé : la boucle viserait un signe par sa forme (R3), sans qu'aucune fiche le vise.
- **Correction** : un point à soumettre à Lazar, écrit au § 8 et au § 16 : (b) prend les objets tels que livrés ; ou les
  deux objets reçoivent le même nombre de rondes de boucle, et l'inégalité de leurs leviers est déclarée au texte de (b)
  avant son scellement.

### CLB-11 — à corriger avant usage — Le document de correction entre dans l'arbre de l'organisme

- **Où** : protocole l. 178–181 (§ 6) et l. 218–220 (§ 8) ; briefs l. 169–170 ; registre l. 179–181 ; texte v4
  l. 379–381.
- **Ce qui ne va pas** : « rien de la boucle n'est servi à un organisme ni à Gemini : ni le registre, ni les verdicts, ni
  les motifs des corrections » (protocole l. 218–219) ; mais le `CORRECTIONS-v<N>.md` nouveau entre dans `organisme/` et
  « ne cite que des faits mécaniques » : ce sont des motifs. Ces faits portent des bits sur les scores de `test`
  (registre § 0.8), que le texte v4 ne laisse servir à un organisme que sur décision de Lazar (l. 379–381). Si un rôle de
  l'organisme lit son propre arbre (non vérifié), le motif lui est servi.
- **Correction** : le document de l'arbre ne décrit que le changement de code (quoi, où), sans fait de course, fiche ni
  verdict ; les motifs restent dans les pièces de la boucle ; G4 vérifie qu'il ne porte aucun fait de course.

### CLB-12 — mineur — Le correcteur lit toute la sortie du script

- **Où** : briefs l. 145–146 et 150–152 ; protocole l. 65 ; texte v4 l. 378–379.
- **Ce qui ne va pas** : le correcteur ne peut fonder une correction que sur un verdict de l'analyste ou un libellé (iii),
  mais reçoit toutes les valeurs de `test_final`. Le texte v4 (02:17) laisse les agents lire la sortie : ce n'est pas une
  infraction. Mais le correcteur tient le rôle de concepteur, celui de Gemini, à qui le texte refuse les scores de
  `test_final` ; une valeur vue peut orienter un choix sans laisser de trace.
- **Correction** : retirer `lecture/` de ce que lit le correcteur.

### CLB-13 — mineur — L'aveugle de la partie A ne tient qu'à une consigne

- **Où** : briefs l. 16–17, 194–197 et 199 ; protocole l. 127–131.
- **Ce qui ne va pas** : le brief du contre-lecteur porte dès le départ les chemins des pièces de l'analyste et du
  correcteur. L'empreinte de la partie A prouve l'ordre d'écriture, pas l'ignorance (synthèse « lecture du pilote »,
  point 5).
- **Correction** : conv-audit ne donne ces chemins, ou ne copie ces pièces, qu'après avoir reçu la partie A et consigné
  son empreinte.

### CLB-14 — mineur — « Rejet trop propre » : non défini, à un seul sens, et un adjectif que les briefs interdisent

- **Où** : registre l. 466–467 ; briefs l. 119–121, 66 et 69.
- **Ce qui ne va pas** : aucun critère écrit d'avance ; l'exemple ne donne qu'un sens ; l'appliquer oblige à juger des
  comptes de `test_final`.
- **Correction** : tout rejet de (iii), quel qu'en soit le sens, reçoit le même audit (R4) ; retirer « trop propre ».

### CLB-15 — mineur — Le code de l'objet est une entrée de fiches que l'analyste n'ouvre pas

- **Où** : registre l. 281, 314, 340–341 et 346 ; briefs l. 100 et 194 ; protocole l. 64, 66 et 108–109.
- **Ce qui ne va pas** : HC-P4-04, 05 et 06 nomment le code de l'objet parmi leurs entrées ; l'analyste « n'ouvre pas
  `objet/` », la partie A du contre-lecteur non plus.
- **Correction** : donner `objet/` en lecture à l'analyste et à la partie A, ou retirer le code des entrées de ces fiches
  (le registre cite déjà les lignes).

### CLB-16 — mineur — Petites inexactitudes de texte et de chemins

- (a) Protocole l. 70–72 : « l'archive fermée et tout ce qui en est tiré » couvre, à la lettre, (A) et (B), tirés de
  l'archive ; écrire « hors (A) et (B) ».
- (b) Briefs l. 167 et 171 (`objet/organisme/`) contre protocole l. 108–109 (`objet/` est la copie, avec
  `objet/EMPREINTE-ARBRE.txt` à côté, qui changerait une empreinte d'arbre calculée sur `objet/`) : un seul chemin.
- (c) Protocole l. 356 interdit au correcteur d'écrire un « libellé » de `test_final`, alors que l. 124 et briefs l. 179
  lui font citer le verdict qui motive sa correction, qui peut être un libellé (iii) : écrire « jamais dans les fichiers de
  l'organisme ; dans la pièce de correction, la cellule et son libellé seulement ».
- (d) Registre l. 519–520 : « à ces tailles, tout intervalle couvre toute référence » n'est pas vrai en général (un
  intervalle peut rester sous une référence haute) ; écrire que ces intervalles sont trop larges pour rien séparer
  (illustratif).
- (e) Protocole l. 268 : le motif de G6 (les deux noms de course dans une même pièce) frappe aussi le journal et le
  tableau d'identité ; borner sa portée aux pièces de verdicts.
- (f) L'empreinte attendue de `MANIFESTE-DOSSIER-v1.txt` n'est pas un champ des briefs (l. 10–20 et 44–45) : un dossier
  altéré avec son manifeste passe la vérification ; ajouter ce champ.

### CLB-17 — mineur — Table « v1 → v2 » et écarts : omissions

- **Où** : registre l. 214, 490–493, 547 et 559 ; LISEZMOI l. 52 et 76–82 ; `brief-boucle-exterieure-v1.md` l. 70–71.
- **Ce qui ne va pas** : (a) HC-P4-01 est dite « inchangée en substance » alors que la v2 ajoute « comptés comme un seul
  facteur » (déclaré seulement au choix 23) ; (b) la ligne « § 2 » de la table ne dit pas l'ordre nouveau en trois
  groupes ; (c) non déclarés : des chemins relatifs à un « dossier de lecture » assemblé par conv-audit, au lieu des
  « chemins relatifs à un dossier de course » du brief v1 (point 3), et un journal unique pour les deux objets (CLB-05).
- **Correction** : compléter la table et le LISEZMOI dans leurs versions nouvelles.

### CLB-18 — mineur — Une phrase du registre donne au correcteur un fait de structure de la banque

- **Où** : registre l. 479–480 (HC-P4-12) et l. 31 ; briefs l. 145 (le correcteur lit le registre).
- **Ce qui ne va pas** : la phrase sur le canal des paires ne sert à aucun test ; le registre dit ne rien contenir qui
  puisse être utilement servi à un organisme, et le correcteur, qui écrit l'organisme, le lit.
- **Correction** : retirer la phrase (P4v3 la porte pour qui doit la connaître).

### CLB-19 — mineur — Multiplicité d'une ronde à l'autre

- **Où** : protocole l. 335–336 et § 7.
- **Ce qui ne va pas** : chaque relance a sa propre famille de tests ; sur trois rondes, jusqu'à six tests (iii) par
  objet s'enchaînent par les décisions de la boucle, sans contrôle d'ensemble ni mention de ce fait.
- **Correction** : le dire dans chaque texte de relance et dans ce que conv-audit transmet à Lazar.

## Ce que j'ai trouvé conforme

- **Empreintes et identités** : les quatre textes et leurs compagnons (format « empreinte, deux espaces, nom nu ») ; les
  31 chaînes hexadécimales et graines que citent les quatre textes se retrouvent toutes dans les pièces fournies ou
  égalent une empreinte calculée ; le tableau d'identité du protocole (l. 228–229 : commits, arbres, nombres de fichiers,
  graines) concorde avec le texte v4 (l. 202–203, 239–240, 360–361) et P4v3 (l. 117–118).
- **Nombres refaits sans aucun score** (bibliothèque standard) : z = 2,2414 ; bornes basses maximales 0,7818 et 0,7049,
  au meilleur partage (18 et 18 ; 12 et 12) ; tailles de classe minimales 26, 21 et 16, et « jamais » pour 1,0 ; valeurs
  p exactes du registre § 0.5 pour des comptes hypothétiques (illustratif) ; 1/48 − 1/72 = 1/144. Calendrier de Holm
  juste (registre l. 79–85) : sous 0,0125, un rejet le reste ; au-dessus de 0,05, un non-rejet le reste ; entre les
  deux, en attente.
- **P4C7-01** : aucune fiche ne tire de verdict de (ii) (registre l. 68–73) ; HC-P4-02 « indécidable par ce pilote »,
  avec ce qu'il faudrait ; un « au-dessus » est un signal de défaut (registre l. 239–240 ; G7).
- **P4C7-02** : HC-P4-10 « indécidable par ce pilote », renvoyée au pilote décisif (b) ; aucune fiche ne compare les deux
  objets ; agents tenus par l'interdit (registre l. 95–99 ; protocole l. 207–209), hors les deux chemins de CLB-05.
- **Symétrie** : une nulle par famille (HC-P4-11 et 12) et ce que son non-rejet implique ; une règle écrite d'avance pour
  « tenue » et pour « éliminée » (ou rejet et non-rejet) dans chaque fiche ; aucune fiche ne vise un signe ; relance
  « pour voir si les scores bougent » refusée (protocole l. 253).
- **Retenue et moments** : aucune lecture avant l'ouverture transmise par conv-audit, fiches mécaniques comprises
  (registre l. 173–184 ; protocole l. 36–46) ; jamais pendant une course ni entre deux segments (protocole l. 33–35 ; G1) ;
  texte nouveau poussé avant toute lecture si des graines sont ajoutées (protocole l. 47–49).
- **Qui voit quoi** : liste interdite complète (secret, clés, archive, journaux et extraits bruts, `LANCEMENT.md`, réponse
  à la question, réponses du collisionneur) ; rien du registre ni des verdicts servi à un organisme (protocole l. 218–220,
  § 15), hors CLB-11 ; `test_final` jamais servi.
- **Correcteur** : ses interdits (§ 14) reprennent ceux du brief et y ajoutent les constantes de mots-clés et les bornes
  du GO.
- **Suites** : une relance est une course nouvelle, avec texte versionné et contre-lu, lanceur dérivé et essayé, lignes
  de GO et de dépense, mot direct de Lazar dans la session de session-depot, aucune dépense par défaut (protocole
  l. 239–253) ; des graines de plus restent une décision de Lazar (l. 251–252) ; arrêt à trois rondes par objet (ronde 1 =
  course du pilote 4 : lecture prudente, déclarée), à un plafond que Lazar fixera, sur la liste d'arrêt, sur son mot.
- **Gardes** : les quatre que demandait le brief v1 y sont (G1, G3, G4, G5), plus G2, G6, G7 et G8, chacune avec un cas
  sain et un artefact.
- **Sources** : lignes de code citées (`principal.py`, `memoire_isvd.py`, `mitose_spectrale.py`), canaux (b) et (d),
  exception du retour arrière et critère de fin de la v5.3 conformes au texte v4 (l. 307–320) et à P4v3 (l. 135–184 et
  397–409) ; résumé de (b) fidèle (HC-P4-10) ; renvois aux synthèses justes (« lecture du pilote », points 6 et 7 ;
  « neuron explorer », point 4 et décision 2).
- **Auteur** : choix faits seul, points ouverts et écarts déclarés (LISEZMOI § 2 à 5), hors CLB-17 ; heures écrites par
  `date -u` ; textes finis à 03:58 et 03:59 UTC, quelques minutes après le départ transmis de la première course ; l'auteur
  dit n'avoir lu aucun fait de course.

## Ce que je n'ai pas pu vérifier

- Le script de lecture et sa sortie (non fournis) : nom de sa sortie (dossier ou course), empreintes qu'il affiche, mode
  « Holm sur deux », présence du score de `test` rendu, de b et c, du nombre de tâches sans réponse ; ses essais.
- Le dossier de la course (`pilote4-gemini-v6-2-v1-tentative2`), sa liste fermée, son extrait : quels champs de (B)
  existent vraiment (critère écrit, « a tourné », motifs de refus, castes, restauration, recherches par ronde) ; l'existence
  d'un dossier de la tentative refusée ; le nom qu'attend la porte « v6.2 précédente » de la v5.3 (hors de cette relecture).
- Le code des objets : si un rôle de l'organisme lit son propre arbre (CLB-11) ; si `objet/` porte un texte de tâche (par
  exemple l'exemple de format, `principal.py` l. 794) ; si une mutation forcée ou une génération au score nul peuvent
  rompre l'équivalence de HC-P4-04 sans défaut de code.
- Le script `releve_appels_simulation_v3.py`, cité comme base de (B).
- La poussée des pièces sur le canal et son heure par rapport à la fin de la première course (sans `git`).
- Les mots de Lazar après 03:48, absents des pièces fournies ; l'heure de départ de la première course (fait transmis).

## Écarts déclarés

1. J'ai écrit un fichier temporaire (la liste des chaînes hexadécimales citées par les quatre textes ; aucun score) dans
   le dossier de travail de ma session (`/tmp/claude-0/…/scratchpad/hex-cites.txt`), hors du seul dossier permis ; je
   l'ai effacé aussitôt. Pour vérifier l'effacement, j'ai listé les noms de ce dossier ; je n'y ai ouvert aucun fichier.
2. J'ai listé les noms du dossier du brief et lu le compagnon du brief, pour vérifier son empreinte ; rien d'autre dans
   ce dossier.
3. Mon heure de début n'est consignée par aucune commande d'écriture.
4. Pièce de plus, sous le dossier permis : `essai-diff-ru-v1.log` et son compagnon (essai sur deux arbres inventés,
   effacés ensuite).
5. Python lancé en mode isolé, sans écrire de fichier, pour refaire des nombres sans aucun score.
