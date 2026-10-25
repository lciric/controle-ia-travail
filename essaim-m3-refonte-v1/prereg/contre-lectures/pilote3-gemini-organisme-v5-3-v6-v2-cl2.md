# Contre-lecture 2 du préenregistrement du troisième pilote (Gemini v5.3 puis v6) — `pilote3-gemini-organisme-v5-3-v6-v2.md`, lanceur v2 et essais v3

- **Contre-lecteur** : sous-agent neuf (`claude-opus-5-5`), lancé par conv-audit. Je n'ai écrit aucune pièce de ce pilote, ni T2, ni la
  contre-lecture 1.
- **Date** : 25 octobre 2026, de 15:00:04 à ≈ 15:20 UTC (heures lues sur `date -u`).
- **Méthode** :
  - lecture seule des fichiers listés, par leur chemin exact ;
  - aucune recherche récursive, aucune commande git, aucun sous-agent ;
  - rien d'exécuté : ni lanceur, ni essai, ni code d'organisme, ni interpréteur ;
  - commandes lancées : `date -u`, `sha256sum`, `wc`, `sed -n` (lecture de lignes, affichage exact par `l`, filtres
    d'adresses) et `diff` entre extraits obtenus par `sed -n`.
- **Stabilité** : empreintes refaites à 15:16 UTC, toutes inchangées. Les numéros de ligne cités sont ceux des versions
  ci-dessous.

## Fichiers lus (sha256)

Racine : `/home/claude/pilote3-v53-v6/essaim-m3-refonte-v1/prereg/`. « pièces » = `pieces-pilote3-gemini-v5-3-v6/`.

| fichier | lu | sha256 |
|---|---|---|
| `pilote3-gemini-organisme-v5-3-v6-v2.md` (texte contre-lu) | entier | `184299c2fa3d347ff9f8c73148387222689c123dbe9f17ec9595b5472a22feea` |
| `contre-lectures/pilote3-gemini-organisme-v5-3-v6-v1-cl1.md` | entier | `25c996efb6d7045f9506f436ecc489e3a70d48abbf6af9dc7232bded82bbae30` |
| pièces / `diff-lanceur-pilote3-v1-vers-v2.txt` | entier | `51f06e5096d8f51796a3c652e554d0867e69e9f378f95f48cb64957a63b95f4c` |
| pièces / `lancer_pilote3_gemini_v5_3_v6_v2.sh` | entier | `add695a90683b59fe9c3a06f0fb7ff70ae46c4067c490c9850988852c814ec76` |
| pièces / `essais_lanceur_pilote3_v5_3_v6_v3.sh` | entier | `14bc0535534bc5c7350102c4d13786ecd40cb3802cb980eb1e4715b53d116aa9` |
| pièces / `essais-lanceur-pilote3-v5-3-v6-v3.log` | entier | `4c4e68ae27b53d337fde1fd1d9335df8584caa8070ca3fea751a85dbcd6019c3` |
| pièces / `essais-lanceur-pilote3-v5-3-v6-v2.log` | `diff` avec le v3, lignes « ÉCHEC » et bilan | `96c22ebf8170d6974ebdcf6e63746a5378f5e557c9d41cde1a4dfa394baf8189` |
| pièces / `sceller_pilote3_v2.py` | entier | `c7fe17ca772270e6b942cb97932473db90541c57644729727e00220b7fc678a3` |
| pièces / `recherche-autoriser-mutation-code-noyau-v1.txt` | entier | `8838d9fc1fddec4b782dbbe2d3f74d8f205bd9cb47d8ccb96b53d1f79010c5bc` |
| `pilote2-gemini-organisme-v5-2-v2.md` (T2) | l. 263–266, 288–291, 360–368, 379, 397, 408–409, 428–432, 527–557 | `d294465429094e5099cb5facdad95e2b806aa8953640b57bcab99998396c066b` |

## Verdict

**Scellable après corrections.**

- Aucun constat majeur : 4 mineurs et 5 remarques.
- Les deux constats majeurs de la contre-lecture 1 sont traités, dans le texte comme dans le lanceur. La porte
  « v5.3 précédente » est mécanique, conforme à la liste close de T2 et essayée.
- Les corrections demandées ici sont mineures. Au sens du texte (l. 45–47), elles n'arrêtent pas le pilote.

## Vérifié et conforme

### Empreintes

Toutes celles que le texte cite pour les fichiers de ma liste sont égales à celles que j'ai calculées :

- texte de T2 `d2944654…` ;
- contre-lecture 1 `25c996ef…` ;
- lanceur v2 `add695a9…` ;
- écart `51f06e50…` ;
- essais v3 `14bc0535…` et leur journal `4c4e68ae…` ;
- journal v2 `96c22ebf…` ;
- script de scellement v2 `c7fe17ca…` ;
- recherche `8838d9fc…`.

### P3C1-01 (porte « v5.3 précédente ») : traité

- **Même code.** J'ai comparé par `diff` le code de l'étape (0 bis) (l. 213–269) à celui de l'étape (0) (l. 293–351).
  - Ils sont identiques, sauf les paramètres et les messages. Les paramètres sont : la course `v5-3` (au lieu de
    `maieutique`), le nom de l'en-tête `pilote3-gemini-v5-3-maieutique-v1`, le lanceur (nom et `SHA_LANCEUR` de ce
    lanceur), la lignée `gemini-organisme-v5-3` et `GO-2026-10-25-02`.
  - Les lignes des statuts, du seuil de 20 %, de Fable, des générations invalidées, de la fin et des arrêts sont
    identiques.
  - La comparaison de la graine avec le texte est déplacée à l'étape (2), seul endroit où le texte est vérifié
    (l. 415–418).
- **Exécution.** L'étape (0 bis) tourne toujours pour la v6 en réel (condition l. 204). Elle est placée avant l'étape
  (0). Ses refus passent par `refus` : le dossier est créé et le refus consigné.
- **Refus en réel**, chacun essayé :
  - variable non définie (l. 205), essai `reel-v6-sans-precedente` ;
  - v5.3 d'une autre copie (l. 210), essai `reel-v6-precedente-hors-dossier`. Les chemins comparés sont résolus par
    `pwd -P` : un lien vers une autre copie est refusé aussi ;
  - autre nom (l. 211), essai `reel-v6-precedente-nom` ;
  - v5.3 simulée (en-tête « (reel, tentative N) » et manifeste `reel`, l. 225–226 et 254–256), essai
    `reel-v6-precedente-simulee`.
- **Graine de la v5.3.**
  - Elle doit être un entier (l. 268), sinon refus : essai `v53-graine-vide`.
  - Elle doit être égale, exactement, à la ligne « graine de la course v5-3 » du texte (l. 416). Ce contrôle a
    toujours lieu en réel, puisque `PREREG` y est exigé. Essais : `sain-v6-graine-v53` et `v53-graine-autre`.
- **Ligne de dépense de la v6.** L'empreinte de la v5.3 est contrôlée (l. 448–450) en plus de celle de M
  (l. 445–447). Essais : `sain-v6` (ligne portant les deux) et `v6-depense-sans-empreinte-v53`.
- **Texte.** La table (l. 80) dit : pour une issue de la v5.3, « la v6 ne part pas ». La liste d'arrêt a sa ligne
  (l. 322). Le § Essais liste 21 artefacts de la v5.3 et 23 de M : ce sont les 21 et 23 cas du journal v3.

### P3C1-02 (ligne du GO) : traité

- La l. 52–54 décrit exactement le contrôle du lanceur (l. 441).
- **Ligne d'extension.** J'ai pris la l. 57, sans indentation ni accents graves, et lui ai appliqué les quatre filtres
  de la l. 441 (émulés par `sed -n`) : elle passe pour la v5.3 (`6251ab21`) comme pour la v6 (`940c59c3`). Une seule
  ligne sert donc aux deux courses. La ligne de R-440, sans empreinte, ne passe pas, et n'a pas à passer.
- **Lignes de dépense** (l. 62–63). Chacune passe les filtres des l. 444–450 pour sa course : nom, GO,
  `5ae4e801423bbef0` et, pour la v6, le champ de la v5.3. La ligne de la v5.3 ne porte pas le nom de la v6.
- La forme suit celle de T2 (l. 288–291). La ligne `registre_go` du manifeste est dite (l. 58–60).

### Les onze autres constats de la contre-lecture 1

| constat | traitement vérifié |
|---|---|
| P3C1-03 | oui : règle de procédure (l. 97–102), plus stricte que la correction proposée (après la fin de S et de l'épreuve de l'étape 1) ; « sans artefact » est dit (l. 387–388) |
| P3C1-04 | oui : R-439 et R-440 cités (l. 33–44, mots conformes à ceux de la contre-lecture 1) ; S finie ; « arrête » et « prêtes » définis (l. 45–49). Voir P3C2-06 pour « prêtes » |
| P3C1-05 | oui : canal dit et accepté (l. 293–296) ; citation l. 101–113 (l. 207) |
| P3C1-06 | oui : pièce de recherche citée avec son empreinte ; elle dit 33 fichiers `.py` et aucune ligne (la recherche porte sur les seuls fichiers `.py`) |
| P3C1-07 | oui dans le texte (l. 161–165) ; heures non vérifiables (rapport hors de ma liste) |
| P3C1-08 | oui : (i) à (iv), l. 223–232 ; pour les nombres d'appels, voir P3C2-01 |
| P3C1-09 | oui : l. 87 et 283–289 |
| P3C1-10 | en partie : gardes valant par identité des lignes dites (l. 382–388) ; pièces citées avec leur empreinte (l. 398–406) ; relecture des champs : voir P3C2-01 |
| P3C1-11 | oui : texte aligné sur le lanceur (l. 113–123) ; égalité exacte (lanceur l. 349–350) ; essai `m-graine-vide` |
| P3C1-12 | oui, sauf deux citations de lignes : voir P3C2-09 |
| P3C1-13 | oui : statut de l'erratum (l. 19–22) ; garde de numpy (script l. 14–15) ; tests de dépense imputés (l. 64–65) |

### Lanceur v2 et écart v1 → v2

- **L'écart est fidèle à la v2.** Son côté ajouté est identique aux lignes 3–8, 32–34, 198–271, 349–350, 415–418 et
  447–449 du lanceur v2 (`diff` vide). Il compte 92 lignes ajoutées et 5 retirées, ce qui donne 661 lignes pour la v1.
- **Les renvois de la contre-lecture 1 tombent juste.** Ses numéros de ligne de la v1, décalés selon l'écart, tombent
  sur les mêmes lignes de la v2 : 49, 53, 55, 59, 107–120, 193–272, 210–213, 268–270, 328, 333, 355–367, 500, 597 et
  605.
- **Aucune variable indéfinie.** `SHA_LANCEUR` (l. 183), `RACINE_PILOTES` (l. 133), `GO_ID` (l. 103), `PY` (l. 67),
  `refus` et `note` (l. 179–180) sont tous définis avant l'étape (0 bis). `EMP_V53` est remis à vide (l. 203).
  `GRAINE_V53_MANIFESTE` est lu sous `:-` (l. 415). Aucune variable ne viole `set -u`.
- **Ordre des étapes.** Il est conforme au texte (plan, point 1). Je n'ai trouvé aucun refus manquant.
- **Effet sur la course v5.3.** Une seule ligne change pour elle : l'égalité exacte de la graine M (l. 349–350).
  - T2 l. 408 s'écrit exactement « `   graine de la course maieutique = 3970427751169333427` », sans caractère final
    (affichage par `sed -n l`).
  - Le cas `sain-v5-3` a franchi ce contrôle avec le vrai T2. Le programme d'essais vérifie l'empreinte de T2 dans les
    trois copies (l. 35–37).

### Texte v2 et lanceur v2 : compatibilité mécanique

- **Lignes de graines** (l. 280–281). Elles ont la forme « `   graine de la course v5-3 = <<GRAINE_V53>>` », sans
  caractère final. Une fois scellées, elles satisfont les motifs des l. 408 et 416 du lanceur.
- **Entropie.** Une seule occurrence de « entropie E = » (l. 276).
- **Marqueurs.** Il y en a exactement quatre, chacun une fois. Ce sont ceux qu'attend le script (l. 19–25).
- **Lanceur.** Son empreinte est citée en entier (l. 393).
- **Renvois à T2 vérifiés** : l. 263–265 (≈ 123 et ≈ 129 appels), 288–291, 365 (cité par R-439), 408, 428–432,
  527–557.

### Essais v3

- **Total.** 122 cas conformes sur 122. Le décompte du programme donne 122 :
  3 + 14 + 22 + 21 + 1 + 5 + 4 + 8 + 3 + 2 + 5 + 7 + 5 + 6 + 6 + 2 + 3 + 5.
- **Nouvelles gardes.** Chacune a un cas sain et un artefact (R5) :

  | garde | cas sain | artefacts |
  |---|---|---|
  | variable définie, dossier présent | `sain-v6` | `reel-v6-sans-precedente`, `v53-absente` |
  | même copie, nom (en réel) | franchis par `reel-v6-precedente-simulee`, refusé plus loin | `reel-v6-precedente-hors-dossier`, `reel-v6-precedente-nom` |
  | empreintes | `sain-v6` | `v53-sans-empreintes`, `v53-empreintes-alterees` |
  | liste close | « v5.3 saine » | 15 artefacts, plus `reel-v6-precedente-simulee` |
  | graine entière, puis égale au texte | `sain-v6-graine-v53` | `v53-graine-vide`, `v53-graine-autre` |
  | dépense de la v6 | `sain-v6` | `v6-depense-sans-empreinte-v53` |
  | graine M en égalité exacte | `sain-v5-3-graine-m` | `m-graine-autre`, `m-graine-vide` |

- **Cas en échec en v2 : une erreur d'attente de l'essai.**
  - Entre les journaux v2 et v3, seul ce cas change ; le reste ne diffère que par le chemin `essais-v2` → `essais-v3`.
  - En v2, le cas tournait pour la v6 en réel. Le lanceur l'a refusé à l'étape (0 bis) : « PRECEDENTE_V53 non
    défini », code 2. C'est l'ordre voulu (commentaire l. 198 ; texte, plan, point 1). L'essai attendait, lui, le refus
    de l'étape (0).
  - En v3, le cas passe à la course v5-3. Le cas v6 de la porte est `reel-v6-sans-precedente`.

### Script de scellement v2

- Il refuse numpy < 1.25 (l. 14–15).
- Il exige l'ensemble exact des quatre marqueurs, chacun une fois.
- Il dérive les graines comme le lanceur : enfant 0 pour la v5-3, enfant 1 pour la v6.
- Il refuse un fichier d'empreintes déjà existant (R12). Voir P3C2-03.

### Courses finies

Le pilote 3 ne touche ni M ni S :

- il ne fait que lire le dossier de M (`sha256sum -c`, `grep`, lecture de l'extrait) ;
- il n'écrit que dans sa propre copie, sous des marqueurs, une espace des organismes et des branches aux noms du pilote 3 ;
- le texte laisse T2 seul en vigueur pour M et S (l. 18–19).

## Constats

### P3C2-01 — mineur — Une partie des champs « relus par la contre-lecture 2 » ne l'est pas : aucune pièce de ma liste ne les porte

- **Lieu** : texte l. 7–9, 190–191, 226–227, 238–240, 333 et 349–356 ; table l. 423 (P3C1-10).
- **Constat** :
  - **Relus et conformes** : le nombre d'essais (122 sur 122) et l'explication du cas en échec en v2.
  - **Non relus** :
    - les nombres d'appels en simulation : pour la v5.3 et la v6, 123 appels à g000 et 129 à g001, tous `OK` ; pour la
      M de référence et la « v5.3 saine », g000 {"OK": 123} et g001 {"OK": 129} ;
    - l'absence d'appel de rôle `architecte_mutation_endogene` dans les journaux de la v6 ;
    - les versions de l'interpréteur.
  - **Pourquoi.** Le journal v3 ne porte pas ces valeurs : le programme d'essais ne cherche que le début des lignes
    (« ; v5.3 saine : g000 et g001 OK », l. 147 ; « ; M saine : … », l. 134 et 149). Elles viennent de
    `simulation-lanceur-v2/`, que le texte cite sans chemin de fichier ni empreinte.
  - **Conséquence.** La phrase « les champs remplis après la contre-lecture 1 (nombres d'appels en simulation,
    essais) le sont par elle » est fausse pour les nombres d'appels. Ces nombres ne commandent aucune porte : ils ne
    servent qu'à un ordre de grandeur non opposable, et l'inertie de V6-01 repose sur la lecture du code.
- **Correction** : deux possibilités.
  - Citer les fichiers exacts qui portent ces valeurs, avec chemin et empreinte : le `LANCEMENT.md` et l'extrait du cas
    sain v6, les journaux des appels de la v6. Écrire ensuite « non relus par la contre-lecture 2 (pièces hors de sa
    liste) ».
  - Ou les faire relire avant le scellement.

### P3C2-02 — mineur — Le texte décrit mal ce que lit la contre-lecture 2, et nomme encore les essais v2

- **Lieu** : texte l. 433–434 ; table l. 414.
- **Constat** :
  - La l. 433–434 annonce une contre-lecture 2 faite « sur cette v2, le lanceur v2, son écart à la v1 et le journal
    des essais v2 ».
  - Or les essais de référence sont les v3 (122 sur 122). Le journal v2 (121 sur 122) n'est qu'une pièce gardée.
  - La table (l. 414) renvoie, elle aussi, aux « essais v2 ».
- **Correction** :
  - écrire ce que j'ai lu (en-tête de ce rapport) et citer le chemin de ce rapport ;
  - dans la table, écrire « essais v2, repris en v3 (122 sur 122) ».

### P3C2-03 — mineur — Le script de scellement empreinte les contre-lectures présentes, sans exiger qu'elles le soient

- **Lieu** : `sceller_pilote3_v2.py` l. 31–32 ; texte l. 407.
- **Constat** :
  - La l. 32 prend tout fichier `pilote3-gemini-organisme-v5-3-v6-*` du dossier des contre-lectures.
  - Si on le lance avant que ce rapport et son compagnon existent, ou avec un nom erroné, il scelle sans eux et sans le
    dire. C'est un repli silencieux (R5). Le texte annonce pourtant « le fichier d'empreintes de toutes les pièces et
    des contre-lectures de ce texte ».
  - Les compagnons des contre-lectures ne sont pas vérifiés non plus.
- **Correction**, au choix :
  - **sans nouvelle pièce** :
    - avant le scellement, faire `sha256sum -c` des compagnons des deux contre-lectures ;
    - après, vérifier que `EMPREINTES-pilote3-gemini-v5-3-v6-v1.txt` porte bien les quatre fichiers ;
    - consigner les deux sorties dans le message de départ ;
  - **ou** un `sceller_pilote3_v3.py` (R12) qui refuse s'il manque l'un de ces quatre fichiers, ou si un compagnon ne
    se vérifie pas.

### P3C2-04 — mineur — Des faits sans pièce (R6)

- **Lieu** : texte l. 108–111 (fin de S) ; l. 343–346 (première série d'essais de la v1).
- **Constat** :
  - **Faits de S.** Pour M, le texte cite ses sources : canal n° 49 et ligne de 14:19 UTC de `registres/depenses.md`.
    Pour S, il ne cite rien : fin à 14:49:09 UTC, code 0, 15,30 USD, statuts d'appels, empreintes `21f30373…`. Ce
    sont pourtant ces faits qui fondent l'ordre « pilote 3 après S ».
  - **Série remplacée.** « 17 sur 94 » et « 36 essais du noyau en échec » renvoient à un journal remplacé (écart à
    R12, déclaré). Plus aucune pièce ne porte ces chiffres.
  - Je n'ai pu vérifier aucun de ces faits : registres, canal et dossiers des courses sont hors de ma liste.
- **Correction** :
  - citer la source des faits de S : message du canal (numéro, heure), ligne de `registres/depenses.md`, ou
    `LANCEMENT.md` de S avec son empreinte ;
  - pour la série remplacée, écrire : « journal remplacé ; chiffres sans pièce, non opposables ».

### P3C2-05 — remarque — Une ligne de T2 dit l'inverse de la liste close : « les plafonds ne bloquent pas S »

- **Lieu** : T2 l. 544, reprise par la liste d'arrêt (texte l. 315) ; texte l. 135–137 ; lanceur l. 261–262 ; essai
  `v53-plafond-total`.
- **Constat** :
  - **La contradiction.** Lue avec S = v6, la ligne de T2 dit qu'un plafond de la v5.3 ne bloque pas la v6. Or la
    liste close refuse une v5.3 arrêtée au plafond total (« arrêt de la course : ['plafond total atteint'] ») : le
    lanceur le fait, et l'essai le montre.
  - **Déjà réglée.** Le texte tranche en faveur du refus : il prévaut sur T2 (l. 18) et vise « toute autre issue »
    (l. 136). Mais la table ne traduit que « S ne part pas », et session-depot lira seule la liste d'arrêt.
  - **Héritée.** La même tension existe dans T2, dont la porte de S refusait un arrêt au plafond total. T2 est scellé :
    on n'y touche pas.
- **Correction** : ajouter une ligne à la table : « les plafonds ne bloquent pas S » (T2 l. 544) : sans objet pour le
  pilote 3 ; un arrêt de la v5.3 au plafond total, ou une génération non `OK`, arrête la v6 (liste close).

### P3C2-06 — remarque — La suite des opérations entre la v5.3 et la v6 n'est écrite nulle part d'un seul tenant

- **Lieu** : texte l. 47–49, 55–56, 60–63 et 322 ; table l. 415.
- **Constat** :
  - **« Prêtes ».** La définition exige les « lignes de dépense poussées sur `main` ». Or la ligne de la v6 ne peut
    s'écrire qu'après la fin de la v5.3.
  - **Récupération avant la v6.** Seule la table (l. 415) dit « récupérées avant chaque course ». Le corps du texte ne
    demande pas de refaire `git fetch origin main` dans la copie avant la v6.
  - **Dossier de la v5.3.** Il doit rester en place, dans le dossier des pilotes de cette copie, jusqu'au départ de la
    v6.
  - **Conséquence d'un oubli.** Une ligne de dépense de la v6 sans l'empreinte de la v5.3 relève de la l. 322
    (« Lazar décide »), et non d'une nouvelle tentative. La v6 attendrait donc le retour de Lazar.
- **Correction** :
  - ajouter une phrase : « Avant la v6 : écrire la ligne de dépense de la v6 (forme l. 63 ; les 16 premiers caractères
    viennent de `EMPREINTES-pilote-v1.txt.sha256` de la v5.3), la pousser sur `main`, puis faire
    `git fetch origin main` dans la copie du pilote 3 ; laisser le dossier de la v5.3 en place ; `PRECEDENTE_V53` = ce
    dossier » ;
  - dans « prêtes », écrire « la ligne de dépense de la v5.3 (celle de la v6 après la fin de la v5.3) ».

### P3C2-07 — remarque — Des branches des deux portes n'ont pas d'artefact ; elles valent par identité des lignes

- **Lieu** : lanceur l. 215–217, 231–234, 245–246 et 254–256, et leurs jumelles de l'étape (0) ; essais v3
  l. 264–290.
- **Constat** :
  - **Héritées de T2** (comme P3C1-11 pour M), ces branches n'ont pas d'artefact :
    - empreintes sans `LANCEMENT.md` ou sans extrait ;
    - extrait illisible ;
    - « aucun appel au journal » ;
    - en réel, un en-tête « reel » avec un manifeste `reel` ou `go_id` autre.
  - **Propre à la v5.3.** Le nom `…-tentativeN` de la v5.3 n'est pas essayé en réel.
  - **Depuis les essais v3.** L'étape (0) n'est plus essayée en réel pour la course v6, puisque l'étape (0 bis) refuse
    avant elle.
  - **Pourquoi c'est sans conséquence.** Le code de l'étape (0 bis) est celui de l'étape (0), aux paramètres et aux
    messages près (vérifié par `diff`). Et l'étape (0) ne dépend pas de la course.
- **Correction** : aucune avant le scellement. Le dire au § Essais, à la suite des « gardes communes non rejouées ».

### P3C2-08 — remarque — Le lanceur ne vérifie pas que les deux empreintes de la dépense de la v6 sont sur la même ligne

- **Lieu** : lanceur l. 445–450 ; texte l. 63 et 134–135.
- **Constat** :
  - **Ce que fait le lanceur.** Il cherche une ligne qui nomme la v6, le GO et l'empreinte de M. Puis, séparément, une
    ligne qui nomme la v6, le GO et l'empreinte de la v5.3. Deux lignes distinctes passeraient donc.
  - **Ce que dit le texte.** Il prescrit une seule ligne qui porte les deux empreintes.
  - **Conséquence.** Le lanceur est seulement plus permissif que le texte. La forme du texte passe : je l'ai vérifié
    par filtre `sed -n` sur la l. 63.
- **Correction** : aucune au lanceur, qu'il ne faut pas changer maintenant. Facultatif : écrire au texte « au moins une
  ligne portant les deux ».

### P3C2-09 — remarque — Deux citations de lignes des objets diffèrent de la contre-lecture 1

- **Lieu** : texte l. 197–198 (« `principal.py` l. 724 de la v5.3 et l. 725 de la v6 ») ; l. 208
  (« `mitose_spectrale.py`, l. 73–75 et 115–117 »).
- **Constat** :
  - Pour `principal.py`, la contre-lecture 1 écrit (P3C1-12) : « en v6, ce sont les l. 724–725 […] ; en v5.3, une
    ligne plus haut ». Cela donne v5.3 l. 723–724 et v6 l. 724–725.
  - Pour la mitose, elle écrit « l. 73–76 et 115–118 » (gardes aux l. 73 et 115).
  - Les fichiers des objets sont hors de ma liste : je n'ai pas vérifié.
- **Correction** : vérifier sur les fichiers, puis aligner les citations.

## Non vérifié (hors de ma liste, ou exécution interdite)

- **Lanceur v1** (`5a56d854…`). Je n'ai vérifié ni le côté retiré de l'écart, ni l'absence d'autre changement de même
  longueur. Seuls sont établis : le côté ajouté égal à la v2, et la cohérence des numéros de ligne.
- **Programme d'essais v2** (`4c7af35a…`). « À un cas près » n'est pas vérifié octet pour octet. Le `diff` des
  journaux le confirme indirectement.
- **Autres pièces du pilote 3** : `deriver_lanceur_pilote3_v2.py`, essais v1 et leur journal,
  `sceller_pilote3_v1.py`, `simulation-lanceur-v1/` et `simulation-lanceur-v2/`, rapport de vérification des objets
  (heures, exécutions).
- **Code des objets et du noyau** : `cli.py`, `bac_a_sable.py`, `archive.py`, outil d'extraction ; valeur par défaut de
  `autoriser_mutation_code` dans `principal.py` de la v6.
- **Registres et canal** : `go.md`, `depenses.md`, `decisions.md` (R-439, R-440, ligne `GO-2026-10-25-02`), messages du
  canal.
- **Courses M et S** : dossiers, empreintes (`5ae4e801…`, `21f30373…`), heures, coûts. Pour la graine, seul est vérifié
  que la ligne de T2 a la forme exacte ; que le manifeste réel de M porte `3970427751169333427` ne l'est pas.
- **Noms des champs du manifeste réel** (`reel`, `go_id`, `entropie_seed_sequence`). Je les suppose les mêmes que ceux
  qui ont servi en réel à la porte de S de T2.
- **Comportements du noyau** : forme d'un crédit épuisé dans l'extrait réel ; lecture de la première ligne du GO.
- **Graines d'essai** `13729193726644583001` et `1541481317522987174` : non recalculées, l'exécution étant interdite. Le
  lanceur les a recalculées et acceptées dans les cas sains.

## Décompte

- 9 constats : 0 majeur, 4 mineurs (P3C2-01 à P3C2-04), 5 remarques (P3C2-05 à P3C2-09).
- Au sens de la l. 45–47 du texte, aucun constat de cette contre-lecture n'arrête le pilote. Les corrections mineures
  peuvent se faire sans nouvelle relecture.
- **Ordre à tenir** : faire les corrections ; vérifier ce rapport par son compagnon `.sha256` (écrit avec lui) ; puis
  sceller (voir P3C2-03).
