# Vérification du brouillon 2 du troisième addendum d'écart de la course de l'étape B bis (apprentissage des sondes sur la tâche, T0.7) — v1

- **Vérificateur** : sous-agent neuf (règle R2). Je n'ai écrit ni l'addendum, ni ses brouillons, ni les quatre contre-lectures de
  la chaîne de lancement version 6, ni leur arbitrage, ni aucune pièce de la chaîne.
- **Date (UTC, `date -u`)** : 2026-11-18, de 05:21Z à 05:35Z environ. Commit lu : `244c4f7a72b732a09052e932655809b583586c2f`
  (le brouillon 2 et son dossier de preuve n'y sont pas encore versés : lus sur le disque).
- **Pièce vérifiée** : `brouillons/T0.7-etape-B-bis-v1/addendum-ecart-3-brouillon2.md`,
  `a57895d42d002f99a1278e76c88ee9034a5fd12c31eb6711dde4ab90826f42e1` (recalculée, égale à son compagnon).
- **Contre quoi** : la section A (points 1 à 10) de l'arbitrage
  `docs/notes/prealables-course-etape-b-bis-v1/arbitrage-contre-lecture-amorce-v6-v1.md`
  (`688abea5965a872b646148538f979be9dfd90d687c8eb73185eb092bcac150e3`, lu en entier) ; les quatre contre-lectures qu'il arbitre
  (« conformité » et « gardes » lues en entier ; « machine » et « adverse » lues pour tout ce qui touche le texte de
  l'addendum) ; le texte scellé `prereg/T0.7-etape-B-bis-v1.md` (`0ae6210f…`), son premier addendum (`f00eda8a…`) et son second
  addendum (`18baeac3…`), aux lignes citées ; `registres/decisions.md`, lignes R-3160, R-3170, R-3185, R-3188 (et R-3074, R-3146,
  R-3149, R-3162 par leur début) ; `registres/go.md`, lignes GO-2026-11-16-11, GO-2026-11-18-03, -04, -05.
- **Cloisonnement tenu** : rien d'ouvert sous `diag/`, `runs/` ni `donnees/` ; aucune branche de données ni de calcul ; aucun
  résultat de 7a, de 7b, de T0.6, de l'étape B, de l'étape B bis ni du premier test boîte blanche bis. Du registre partagé des
  sceaux, je n'ai lu que les deux premières colonnes (clé et heure) des lignes du 15 au 18 novembre. Du registre des arrêts,
  l. 133 à 135, je n'ai extrait par motif que les identifiants d'instance, les heures et le numéro du pilote ; un de mes motifs a
  rendu le début du nom de la garde qui a arrêté la marche du 16 novembre (déjà écrit dans le second addendum scellé, l. 61) ; je
  ne m'en sers pas. Du fichier de l'épreuve de niveau rejouée (données fabriquées), j'ai lu la graine, les paramètres, le coût et
  le niveau retenu. Aucune dépense, aucun appel au loueur ni à l'hébergeur, aucune clé lue, aucun commit, aucune poussée. Aucun
  clone : tout a été lu et rejoué dans le dépôt, sans rien y écrire que ce rapport et son compagnon.

## Verdict : « à corriger »

Les dix corrections de la section A de l'arbitrage sont **toutes faites**, exactes dans leurs chiffres, et aucune ne minimise.
Toutes les empreintes sont exactes. Les cinq passages remplacés sont uniques, et aucun seuil, critère de lecture, hypothèse ni
ligne de la liste d'arrêt n'est changé. **Aucun bloquant.**

Il reste **un majeur**, que ni les quatre contre-lectures ni l'arbitrage n'avaient vu, et que le brouillon 2 hérite de la lettre
de l'arbitrage (section A, point 9) : la phrase « plis […] inchangés : la règle de la liste d'arrêt, l. 180, n'est pas
déclenchée » est inexacte pour le **tirage des plis internes**, qui dépend de l'entropie changée. C'est une phrase à réécrire et
une lecture à déclarer, sans code neuf. S'y ajoutent sept mineurs, d'une phrase chacun.

### Liste exacte des corrections

**Majeur (à corriger avant le scellement)**

- **M1 — Plis internes et règle de la liste d'arrêt, l. 180.**
  - *Lieu* : brouillon 2, § 5, l. 295 (« Niveau, seuils, cellules, grille, plis et adversaires inchangés : la règle de la liste
    d'arrêt, l. 180, n'est pas déclenchée ») ; second addendum, § 5, l. 509 (« **plis** externes et internes », sous « Inchangés »),
    juste après les graines que TA-3 déclare changées.
  - *Fait* : le texte scellé, l. 116 (point 12 du plan), tire de l'entropie une graine par clé, dont `bbis/interne/<pli>` ; seuls
    « les plis externes prennent la graine `partition-taches` de 7b ». Le code le confirme : `src/controle_ia/t07bbis/marche_v4.py`,
    l. 60 (`CLES_FIXES`, clés `bbis/interne/e0` et `bbis/interne/e1`), l. 287 (`Graines(int(entropie))`), l. 363 (plis externes par
    la graine de 7b). L'entropie a changé à l'inscription de la seconde fiche (17 novembre, 11:05:29Z), donc **après** la marche
    du 16 novembre, qui avait lu les sorties de 7b sur la machine. Le tirage des plis internes — comme celui des apprentissages,
    des planchers, des réétiquetages et des tirages — n'est donc pas celui de la course arrêtée. La règle de la l. 180 du texte
    scellé vise un « changement […] des plis […] après la lecture de toute sortie de l'étape B, de 7b ou de T0.7 ».
  - *Portée* : la règle de construction des plis, leur nombre et les plis externes sont inchangés ; la course du 16 novembre n'a
    écrit aucun score, si bien que rien n'a pu être choisi d'après une lecture ; l'écart d'entropie lui-même est couvert par
    GO-2026-11-18-03 (1). Mais la phrase du § 5 affirme sans nuance « plis inchangés », et la lecture qui met le nouveau tirage
    hors de la règle de la l. 180 n'est déclarée nulle part. C'est de la même nature que les points 8 et 9 de l'arbitrage.
  - *Correction* (texte seul) : au § 5, remplacer la dernière phrase par une phrase de ce sens : « Niveau, seuils, cellules,
    grille, adversaires, règle de construction des plis et plis externes (graine `partition-taches` de 7b) inchangés. Le tirage
    des plis internes (clés `bbis/interne/e0`, `bbis/interne/e1`) et tous les tirages que l'entropie graine changent avec elle
    (TA-3), après la marche du 16 novembre, qui avait lu les sorties de 7b sans écrire de score. Lecture déclarée : la règle de
    la l. 180 vise un changement de la règle des plis, non le tirage que T, point 12, attache à l'entropie de la ligne
    `CODE-BBIS` en vigueur ; elle n'est pas déclenchée. Écart d'entropie couvert par GO-2026-11-18-03 (1) ; cette lecture est à
    faire couvrir avec le reste (§ 1). » Reporter le point au § 1 (pièce nommée par l'accord) et au § 7, point 2. Je ne tranche
    pas si GO-2026-11-18-03 (1) couvre déjà cette lecture : c'est à la mère de l'écrire.

**Mineurs (une phrase chacun ; à porter dans le même brouillon 3)**

- **m1 — Condition « sans bloquant » (§ 1, l. 60-62).** Le brouillon dit que la condition « le devient quand le lecteur neuf du
  brouillon 2 n'en relève plus », et ne dit pas comment se lève le second bloquant confirmé (machine, pilote de carte récent).
  Ce bloquant ne se lève pas par ce texte, mais par le feu version 4 (§ 4, point 9). Ajouter : « l'autre, de machine, se lève au
  feu version 4, qui exige un pilote de série 595 ou 580 (§ 4, point 9) ; l'accord ne vaut pas feu ».
- **m2 — Plafond de prix au lanceur et autorité de l'accord (§ 1, l. 65 et l. 73-74 ; § 3 ; § 7, point 2).** Le brouillon 1
  demandait l'accord de Lazar sur ce point ; le brouillon 2 le range dans l'accord de la mère, comme l'arbitrage le demande. Or
  GO-2026-11-18-05 laisse à Lazar « tout ce qu'un mot exprès de Lazar a déjà tranché autrement », et GO-2026-11-18-03 (3) est un
  mot exprès (« tenu hors du code » ; « le verdict dira que ce plafond tenait à un opérateur et non au code »). La garde du
  lanceur s'ajoute sans rien retirer, mais elle change la phrase que le verdict devait porter. Écrire au § 1 que ce point n'est
  pas couvert par l'accord de la mère seul : il est porté à Lazar par la mère dans son compte rendu, et reste en réserve au
  verdict tant que Lazar ne l'a pas dit. Je ne le classe pas plus haut : rien n'est caché, et le brouillon garde « dit à Lazar
  ici, pour qu'il le refuse ».
- **m3 — Clause d'antériorité, seconde moitié de la même ligne (raison de TA-4 et TA-5).** Le texte scellé, l. 93, dit aussi que
  le niveau est « inscrit avec la ligne `CODE-BBIS`, avant toute marche » et l'épreuve citée « avant toute exécution ». Le même
  fait (la marche du 16 novembre précède l'épreuve rejouée) touche ces deux membres de phrase. Les nommer avec la clause « lue
  avant toute ouverture de données de 7b ».
- **m4 — « n'est plus dans le dépôt » (TA-4, « nouveau », et raison « non vérifié par moi »).** Vérifié par moi (R11) : le
  fichier `registres/t07-etape-b-bis/epreuve-niveau-deux-plis-bbis-v1.json`, que la première fiche cite avec l'empreinte
  `641adeb5…`, est absent du disque et de l'index ; `git log --all` sur son chemin ne rend rien, mais le dépôt local est
  superficiel (140 commits) : l'histoire n'est pas prouvée. Écrire dans le « nouveau » « est absente du dépôt (disque et index ;
  histoire non vérifiée) » plutôt que « n'est plus », et retirer « non vérifié par moi » pour ce membre.
- **m5 — Préséance (§ 0, l. 42-43).** « le code qui apprend, note et écrit (les 63 fichiers de la fiche) » reprend l'équivalence
  que la raison de TA-2 vient de corriger : la marche importe aussi du code hors de la fiche. Écrire « le code neuf que la fiche
  cite (63 fichiers) ». La formule vient de l'arbitrage (section A, point 3) ; le défaut est le sien.
- **m6 — Heure du brouillon 2 (en-tête, l. 12-13).** « de 05:15Z à 05:45Z environ » : le fichier porte
  l'heure 05:20Z sur le disque, et ma vérification s'est achevée avant 05:45Z. Écrire l'heure réelle.
- **m7 — § 8 (fichiers à donner au contre-lecteur) et raison de TA-3.** Le § 8 ne nomme ni l'arbitrage, ni GO-2026-11-18-05,
  ni R-3170 et R-3188, ni les différences de la version 4 à la version 6. La raison de TA-3 garde « Aucun seuil, niveau, état
  ni issue n'en dépend », alors que l'entropie graine l'épreuve qui décide du niveau (TA-5 le dit) : écrire « le niveau, décidé
  par l'épreuve sous chacune des deux entropies, est 0,99 dans les deux cas ». Restent aussi, hors de la section A et laissés
  tels quels par choix déclaré du rédacteur, deux mineurs de la contre-lecture « conformité » : un des 34 essais du second
  addendum saute sur la machine (second addendum, l. 527) ; la coupure de 39,5 USD se lit avec les ≈ 5,99 USD déjà dépensés.

## Les dix corrections de la section A, une par une

| n° | correction demandée | faite ? | exacte ? | ma vérification |
|---|---|---|---|---|
| 1 | Clause d'antériorité de l'épreuve ; l. 24-25 ; point ajouté à l'accord | oui (§ 0, l. 35-38 ; paragraphe l. 211-217 ; § 1 ; § 7, point 2) | oui ; voir m3 | Texte scellé, l. 93, section « Seuil » (l. 87 à 95) : verbatim. Commit `d75587c8` daté 2026-11-17T11:03:40Z, qui ajoute le seul fichier de l'épreuve et son compagnon. Second addendum, l. 518 : marche de 17:58:00Z à 21:35:28Z. Épreuve : graine `bbis/epreuve-niveau` sous l'entropie `1490…2656`, données synthétiques (64 tâches, 800 directions, 1 000 jeux), niveau retenu 0,99. |
| 2 | Entropie : « ancien » étendu aux l. 507-508, « changée », deux valeurs, prédiction sans appui ; programme et sortie versés | oui (TA-3) | oui | « Ancien » : une fois dans le second addendum, de « (même entropie que la fiche » à « sans effet sur aucun état) ». Les deux valeurs sont celles des deux fiches et de GO-2026-11-18-03 (1). Parenthèses : +1 des deux côtés ; le texte reconstruit se lit sans rupture. Programme et sortie versés, compagnons conformes. |
| 3 | Préséance au § 0 | oui (l. 41-44) | oui ; voir m5 | Texte scellé, l. 5 (en-tête) et l. 227 (section « Code neuf », `scripts/lancer_bbis_v1.sh` et son amorce) : verbatim. |
| 4 | Écart net de la version 4 à la version 6 ; différences jointes ; « liste le code v4 » et « avec l'entropie » | oui (raison de TA-1, l. 109-119 ; TA-5 étendu) | oui | `diff` des amorces 4 et 5 : la seule ligne `MIN_ESSAIS=148` devient un commentaire et `MIN_ESSAIS=176` ; lanceurs : 16 lignes, des noms seulement. `MIN_ESSAIS=151` dans l'amorce 6 (l. 64). Les deux différences versées sont celles de `diff -u` rejoué, hors les deux lignes d'en-tête qui portent l'heure. R-3074 : « recompte », sans addendum. « liste le code v4 » : 0 occurrence après les remplacements. |
| 5 | Raison de TA-2 corrigée ; § 4 : code hors de la fiche sans garde ; geste B.4 | oui (l. 143-149 ; § 4, point 7) | oui | Fiche en vigueur : 63 fichiers, soit 22 sous `src/controle_ia/t07bbis/` (seul chemin de `src/`), 21 scripts, 20 essais. Je note que la première fiche citait 103 fichiers, dont le code réutilisé et `requirements-gpu.txt` : le manque de garde vient de la seconde fiche, non de la version 6. |
| 6 | § 4 : aucune garde ne compare la chaîne aux empreintes du § 6 ; « 64 caractères » au § 7 | oui (§ 4, point 8 ; § 7, point 5) | oui | Lanceur, l. 167 : `cut -c1-16`. Les « seize caractères » qui restent (§ 4, point 8, et § 6) décrivent ce que le lanceur imprime : exacts. |
| 7 | Accord : GO-2026-11-18-05 et R-3170 (8) cités ; qui accorde, sur quel texte ; pièce nommée ; condition « sans bloquant » | oui (Statut ; § 1 ; § 7, point 2) | oui ; voir m1 et m2 | Verbatim de GO-2026-11-18-04, de GO-2026-11-18-05 (mot et durée) et de R-3170 (8) : conformes aux registres. « l'accord de Lazar sur eux » retiré. La pièce est nommée telle qu'elle est (aucune fiche neuve). |
| 8 | Liste d'arrêt : lecture déclarée, sans changer la phrase scellée ; à faire couvrir | oui (§ 3, l. 231-235) | oui | Second addendum, l. 142 (bloc SA-5, l. 131 à 150) et l. 305 (bloc SA-15, l. 294 à 311) : verbatim. Les deux phrases sont présentes une fois avant et une fois après les remplacements. |
| 9 | Antériorité : heures de l'épreuve, de la fiche, du verdict de l'étape B ; course du 16 novembre ; phrase sur la l. 180 | oui (§ 5, l. 288-295) | heures exactes ; **phrase sur la l. 180 inexacte pour les plis internes (M1)** | 11:03:40Z (`d75587c8`) ; seconde ligne `CODE-BBIS` à 11:05:29Z ; commit `c098fb51` à 11:07:47Z ; clé `VERDICT-T07-ETAPE-B` à 2026-11-17T11:20:08Z, une occurrence. Registre des arrêts, l. 134 : instance 60953606 engagée à 17:25:30. Texte scellé, l. 180 : c'est bien la ligne « Changement d'une cellule […] ». |
| 10 | Pilote au § 4 | oui (§ 4, point 9) | oui | Aucune occurrence de `driver` dans `registre_bbis_v2.py` ni dans le lanceur version 6. Amorce, l. 102 : le motif ne lit que « CUDA Version: ». Registre des arrêts, l. 133 : instance 60952525, pilote 615.71.09. |

## Le brouillon touche-t-il un seuil, un critère, une hypothèse ou la liste d'arrêt ?

**Non.** Vérifié par le programme versé, rejoué, et par lecture :

- les cinq passages remplacés sont dans le second addendum seulement : le bloc « nouveau » de SA-8 (section « Code neuf » du
  texte scellé), le § 5 deux fois et le § 7 deux fois ;
- les 24 blocs SA autres que SA-8 sont inchangés, dont SA-4, SA-5, SA-15 et SA-19 ;
- le second addendum reconstruit ne diffère de l'original que sur 12 lignes de `diff`, toutes dans ces passages ;
- le niveau décisif reste 0,99 dans les deux fiches et dans l'épreuve rejouée.

Trois lectures sont déclarées sans changer la lettre : la clause d'antériorité de « Seuil », les deux phrases de la liste d'arrêt
(SA-5, SA-15), la préséance sur l'en-tête. Une quatrième manque : celle de la règle de la l. 180 pour le tirage des plis
internes (M1).

## Empreintes (toutes recalculées sur le disque)

Les 18 empreintes de 64 caractères du brouillon : 17 correspondent chacune à un fichier présent (texte scellé, deux addenda,
brouillon 1, arbitrage, programme, sortie, second addendum reconstruit, deux différences, amorces et lanceurs des versions 4 et
6, essais de la version 6, fiche en vigueur, épreuve rejouée) ; la dix-huitième, `641adeb5…9cbf`, est celle que la première fiche
donne à l'épreuve absente (lue dans `code-bbis-v1.json`). Les six empreintes courtes du dossier de preuve de la version 6
(`ca070374`, `83460ade`, `d48e74d3`, `8cbe0bc6`, `a3be1198`, `43298cc4`) sont exactes, et les compagnons de ce dossier sont tous
conformes. Les six pièces du dossier `preuve-addendum-3-brouillon2-v1/` et le brouillon 1 sont conformes à leurs compagnons.
Les deux entropies sont celles des deux fiches.

## Unicité des « anciens » (programme versé, rejoué)

`python brouillons/T0.7-etape-B-bis-v1/preuve-addendum-3-brouillon2-v1/controle-fragments-addendum-3-brouillon2-v1.py`, joué
depuis la racine avec l'environnement du dépôt : **code 0, « CONFORME »**, sortie identique ligne pour ligne à la partie « cas
sain » de la sortie versée ; le fichier reconstruit existe et est identique (rien n'a été réécrit). Chaque « ancien » : une fois
dans le second addendum, zéro fois dans le texte scellé et dans le premier addendum ; aucun chevauchement. Je n'ai pas rejoué les
trois artefacts (ils demandent une copie altérée) : j'ai lu le programme, et les trois refus annoncés découlent de ses lignes.
**Limite du programme** : pour un passage hors d'un bloc SA, il ne vérifie que le numéro de la section du second addendum (5 ou
7) ; cela suffit ici, ces deux sections ne remplaçant aucune ligne du texte scellé.

## Manque-t-il un écart ?

Un seul, de lecture : M1. Je n'ai trouvé aucun autre écart de la course au texte scellé et à ses deux addenda que les douze du
tableau de la contre-lecture « conformité », tous déclarés désormais. Autres mentions de l'entropie dans le second addendum
(l. 596 et l. 633, « entropie reprise ») : elles sont dans le compte rendu de sa contre-lecture (§ 11), histoire et non texte
en vigueur ; à dire d'un mot si la mère le veut.

## Limites

- Je n'ai pas relu les deux scripts de la version 6 ni rejoué leurs essais : ce n'est pas l'objet (les quatre contre-lectures
  et l'arbitrage l'ont fait) ; j'ai lu les lignes du lanceur et de l'amorce que le brouillon cite.
- « Jouée le 17 novembre » : je n'ai vérifié que l'heure du commit et le coût mural écrit dans l'épreuve (14 483 secondes, soit
  un départ au plus tard vers 07:02Z le 17 novembre) ; l'heure de départ n'est pas prouvée par moi.
- Je n'ai pas cherché l'heure de la première lecture des sorties de l'étape B (cloisonnement) : pour M1, seule la marche du
  16 novembre est établie comme lecture antérieure.
- La raison du changement d'entropie reste non vérifiée, comme le brouillon le dit.
- Les mesures du plancher sous Python 3.13 et 3.11 et le feu version 4 (section B de l'arbitrage) ne sont pas dans mon objet.
