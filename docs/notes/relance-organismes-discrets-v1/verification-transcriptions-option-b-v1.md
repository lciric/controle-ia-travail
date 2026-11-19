# Vérification des deux transcriptions du mot de Lazar « option B, go aux deux mots » — v1

**Verdict : fidèles sous corrections listées.** Le mot, l'option B et les deux mots demandés sont rendus exactement, et rien de l'option B ne manque. Mais la décision version 4 ajoute deux définitions et assouplit la version 3 au point 5 (constats 1 à 3). L'archive se tait sur le repli de deuxième ligne et ferme une ligne de calcul que Lazar n'a pas fermée (constats 4 et 5).

- **Date (UTC, `date -u`)** : 2026-11-19T06:15:32Z. Vérificateur neuf : je n'ai écrit aucune des pièces lues.
- **Objets vérifiés** : l'archive sans exécution du texte scellé (`prereg/T0.7-organismes-discrets-v-a-v1-archive-sans-execution-v1.md`, `65e45b38cc285f10454630319d735d7170e427fcab10ef0f2ec2d25096d963aa`) et la décision sur la vérité du dommage, version 4 (`docs/decisions/decision-N-060-v4.md`, `e14779987cf61ae65f4690a0bbb94f373bd0e48f8cdeabb0bd2b31b99b1af241`). Les deux empreintes sont égales à leurs fichiers compagnons. Les deux fichiers viennent du commit `510056e3`.

## Ce qui a été vérifié et trouvé juste

- **Le mot, lu à la source.** Je l'ai lu par l'outil de lecture des événements de la session, en lecture seule. Dans la session `session_013QMaymFtcZwVwjxVAF3gmH`, l'événement `a5370baf-2d2e-4d4c-9c3b-fda7ce421d03` contient « option B, go aux deux mots ». Il a le rôle utilisateur, vient de la plate-forme web et a été créé à 2026-11-19T06:03:02.221Z. Le verbatim, l'événement et l'heure sont exacts dans les deux transcriptions. Les « deux mots » sont bien (i) et (ii) de la décision version 2.
- **Empreintes recalculées** (`sha256sum`), toutes égales à celles que citent les transcriptions et à leurs compagnons :

| pièce | empreinte |
|---|---|
| `prereg/T0.7-organismes-discrets-v-a-v1.md` | `06ab6a2f6e173bb1258f45ffeded7a419b05ecc2f59920666cea91aafcc7cf05` |
| `prereg/T0.7-organismes-discrets-v-a-v1-addendum-lecture-lot-de-huit-v1.md` | `bd6ae8dfdfcda18a9c7118ede4f1542fae71063521c442093f778a1cd4b0e4f3` |
| `prereg/T0.7-organismes-discrets-v-a-v1-addendum-2-pas-de-distillation-v1.md` | `4f9af3c5cfb3725eab81d1507dc2c116845d26b492a5fb07e7370a17f7439352` |
| `docs/notes/relance-organismes-discrets-v1/decision-bras-a-regle-du-controle-mal-place-v2.md` | `fb9e2445d5110ff5d7f87c34055dad505b8fbef9f8ed1f6cd553997290c3dac0` |
| `docs/notes/relance-organismes-discrets-v1/decision-bras-a-regle-du-controle-mal-place-v1.md` (lue, non citée par les transcriptions) | `181c848882317e4d07a9290a66d0e5ddeb5b86499f6a8dd3588e3abd523dfe1f` |
| `docs/notes/relance-organismes-discrets-v1/verification-grain-couverture-v1.md` | `8c981920b6e08597eca032d9f5927e460f67b7af52245c6eeee427207b1bc722` |
| `docs/notes/relance-organismes-discrets-v1/contre-lecture-addendum-3-brouillon1-v1.md` | `ce575acc543e51b8dbdba2f14eeccf1b3649bb2e7f0a8954599b2043c54f2974` |
| `docs/notes/relance-organismes-discrets-v1/seconde-contre-lecture-addendum-3-regle-du-controle-mal-place-v1.md` | `d398fe250979cdc93424c0de72b471705e73168a67cdfb1225b477494a37c138` |
| `prereg/T0.7-organismes-discrets-v-a-v1-addendum-3-objet-lu-et-epreuve-du-jumeau-deplace-v1-brouillon1.md` | `b921e7486ec79693398f0b3ca2a1e661096d2c4047f817087fdb8016116377dc` |
| `prereg/T0.7-organismes-discrets-v-a-v1-consigne-des-lecteurs-v1-brouillon1.md` | `43bf7d4065a1ed9e0975854577ad8b8a56028a196810721a6b8d5c677d4cf7c8` |
| `prereg/T0.7-organismes-discrets-v-a-v2-brouillon1.md` | `7c4b71275dd59e13f9666dee8df886592c4ef3ae6ebd7227159878b24d3c294c` |
| `docs/decisions/decision-N-060-v1.md`, `-v2.md`, `-v3.md` | `4a09c5f5…`, `06a7cb23…`, `2b448f696503112c4acebd3d56748e2c9d9931d9e597f1991e3f278e651c5591` |
| `registres/organismes-discrets-v-a-addenda-v2.md` | `cfd9ab6bbe18b4ef845cd7b6171b2d2df824c8373f0dc7b004bad98fe9533b1d` |
| `docs/notes/relance-organismes-discrets-v1/contre-lecture-preenregistrement-v2-brouillon1-v1.md` (lue, non citée par les transcriptions) | `ce250f0a039265413a2c829d53cc4399a6863a566f1887f55462b01e9244aaa2` |

- **Citations retrouvées mot pour mot** (recherche par programme) :
  - « pour un défaut d'instrument constaté avant toute donnée » (décision version 2) ;
  - le second mot entier, « une version nouvelle de la décision N-060 pour le bras A — appariement […] dans les verdicts » (décision version 2) ;
  - « défaut confirmé en partie : dommage non visé, cas nul attendu » (vérification, ligne 4) ;
  - la date de scellement du texte, 2026-11-17T11:26:12Z (`registres/scellements-v1.md`, ligne 21) ;
  - l'inscription des deux addenda au registre voisin, version 2.
- **Aucun écrasement (R12).** Le commit `510056e3` ajoute quatre fichiers. Il allonge le journal de la relance d'une seule entrée en fin (OD-074) ; ce journal n'a pas d'empreinte compagnon et aucune de ses lignes antérieures n'est touchée. Le texte scellé, ses deux addenda et la version 3 ont chacun un seul commit. La vérification de l'arbre (`python -m controle_ia.scellement verifier-arbre .`) ne trouve aucune empreinte en désaccord : ses 106 signalements sont des compagnons absents ou des formats de nom, aucun sur ces pièces ni sur les deux transcriptions.
- **Personnes et courriels.** Seul Lazar est nommé ; il n'y a aucun courriel.
- **Aucune donnée, aucune dépense.**
  - Le registre des dépenses, sur cette branche comme sur la branche principale, n'a aucune ligne sous la ligne de calcul du bras A.
  - Aucun dossier de course du bras A dans `runs/`. Les dossiers « organismes discrets » qui s'y trouvent sont ceux de l'organisme d'idéation et du collisionneur ; je ne les ai pas ouverts.
  - Ce que je n'ai pas pu vérifier : les comptes des loueurs (aucun appel fait).
- **Contradiction avec la version 3 hors du bras A** : aucune (« Partout ailleurs, la v3 reste la lecture en vigueur », v4, ligne 5).

## Manque : l'option B, élément par élément

| élément de l'option B (décision version 2) | où il est transcrit |
|---|---|
| refuser la règle dans l'addendum | archive, ligne 5 et ligne 15 (« Lazar l'a refusée ») |
| archiver sans exécution, « pour un défaut d'instrument constaté avant toute donnée » | archive, lignes 5, 10 et 12 |
| et non « résultat négatif d'instrument » : le verdict de la vérification est partiel | archive, ligne 16 |
| le préenregistrement neuf porte la question | archive, ligne 5 ; v4, ligne 5 |
| une réponse des lecteurs à deux champs | v4, point 2 |
| couverture de contenu seul et couverture appariée préenregistrées dès maintenant | v4, point 3 |
| le sens de « discret » écrit | v4, point 4 |
| second mot : appariement en variable principale ; deux couvertures rapportées ; « désappariement » dans les verdicts | v4, points 1 et 3 |
| la ligne de 27 USD reste inemployée | archive, ligne 20 (avec un ajout : constat 5) |

**Rien de l'option B n'est omis.**

## Constats

### À corriger

1. **Décision version 4, point 5 : « inchangé », mais l'ordre des épreuves est assoupli.**
   - Passage (ligne 23) : « **Repris de la v3, inchangé** : […] épreuves avant toute lecture décisive ».
   - La version 3, point 2, écrit : « Épreuves de l'oracle avant toute lecture d'un épisode saboté (R5) ».
   - Les deux ne sont pas équivalents. Le point 3 de la version 4 rend les deux couvertures « rapportées, non décisives ». La lettre nouvelle permettrait donc de lire les couvertures d'épisodes sabotés avant les épreuves de l'oracle de couverture.
   - Rien de l'option B ne porte ce changement.
   - Correction : reprendre mot pour mot « avant toute lecture d'un épisode saboté », ou déclarer le changement comme tel et le soumettre à Lazar.

2. **Décision version 4 : les cinq épreuves de la version 3, et d'autres nœuds, passent au rédacteur.**
   - Passage (ligne 27, sous « ne fixe pas ») : « épreuves exactes de l'appariement (dont la place des cinq épreuves de la v3, point 2, au regard des deux couvertures rapportées) […] ; ils se préenregistrent, se contre-lisent par un agent neuf (R2) et se scellent ».
   - La version 3 fixe ces cinq épreuves, dont le plan tronqué et l'ancre humaine. L'option B n'en dit rien.
   - La contre-lecture du texte neuf (`ce250f0a…`, ligne 97) range sous « Ce qui exige le mot de Lazar » : « (2) épreuve du plan tronqué abandonnée ; (3) ancre humaine tenue ou non par une personne ; (4) le désappariement réalise-t-il le mode « affaiblir les contrôles » de N-054, et peut-il nommer une dose candidate à la lecture interne (B3) ; (5) seuils ; (6) les deux lecteurs ».
   - Le mot de Lazar n'a tranché que le premier point de cette liste.
   - Écrite ainsi, la version 4 laisse ces points à un préenregistrement et une contre-lecture, sans le mot de Lazar. Le même texte dit pourtant les épreuves « reprises, inchangées ».
   - Correction :
     - (a) écrire que les cinq épreuves du point 2 de la version 3 restent celles de la couverture de contenu seul ;
     - (b) inscrire sous « ne fixe pas », comme nœuds de Lazar et non comme travail du rédacteur : l'abandon ou le remplacement d'une de ces épreuves (plan tronqué, ancre humaine), et si le désappariement réalise le mode « affaiblir les contrôles » et peut désigner une dose candidate à la lecture interne (lien avec la décision N-063 version 2) ;
     - (c) signaler aussi les seuils et les lecteurs, que la même liste range parmi les mots de Lazar.

3. **Décision version 4, points 2 et 3 : la « couverture appariée » reçoit une définition que l'option B ne donne pas, et « place » change de sens.**
   - Passages : « sa place (l'action qui le porte) » (ligne 20) ; « la couverture appariée (un contrôle de la référence ne compte que s'il est porté par une action jugée appariée) » (ligne 21).
   - L'option B nomme la couverture appariée sans la définir. Sa source est la seconde contre-lecture : « toutes deux tirées d'une réponse à deux champs » (ligne 254).
   - Dans cette source, le champ de place est la question de la place : « l'addendum peut poser la question de la place dans un champ séparé du statut » (décision version 2). Ses trois valeurs sont « sous une expérience qu'il peut vérifier ; sous une expérience qu'il ne peut pas vérifier ; général » (seconde contre-lecture, ligne 111).
   - La version 4 réduit la place à l'emplacement. Elle définit la couverture appariée par le verdict d'appariement de l'action, qui est la construction de la contre-lecture du texte neuf (ligne 100 : « ne compter couvert qu'un contrôle porté par une action jugée appariée »), et non par le champ de place.
   - Les deux constructions ne coïncident pas. Une action peut être jugée appariée dans son ensemble, par exemple quand des contrôles passe-partout « comptent comme répondant », alors qu'un contrôle de la référence qu'elle porte ne répond pas à sa proposition, ou l'inverse. L'option B ne choisit pas entre elles.
   - Correction, au choix :
     - écrire « couverture appariée, construite par le texte neuf (à partir du champ de place ou du jugement d'appariement de l'action) » et porter ce choix sous « ne fixe pas » ;
     - ou reprendre la lettre de la décision version 2 au point 2 : « la question de la place, dans un champ séparé du statut de contenu ».

4. **Archive et décision version 4 : silence sur le repli de deuxième ligne.**
   - Lazar a décidé ce repli, le choix adverse parmi plusieurs tirages honnêtes : il est « construit aussi, en parallèle du bras A ». Ligne de décision GO-2026-11-18-47, « go recos », `registres/go.md` de la branche principale, ligne 411. Son ancrage écrit est la section 9.2 du texte scellé.
   - Son brouillon `prereg/T0.7-organismes-discrets-repli-deuxieme-ligne-v1-brouillon1.md` (en-tête seul lu) cite comme documents qui font foi le texte archivé et ses deux addenda.
   - L'archive écrit : « Le texte scellé et ses deux addenda **ne s'exécutent plus** » (ligne 10). Cela emporte la section 9.2. Pourtant ni « Ce qui n'est pas archivé » ni « Ce que cette archive ne fait pas » ne nomment ce repli.
   - La version 4 (ligne 5), « pour le seul bras A […] (texte neuf, `prereg/T0.7-organismes-discrets-v-a-v2-*`) », ne dit pas si le repli relève d'elle ou de la version 3.
   - L'option B n'en décide rien.
   - Correction :
     - dans l'archive : « le repli de deuxième ligne décidé par Lazar (GO-2026-11-18-47) n'est pas visé ; son ancrage, la section 9.2 du texte archivé, tombe ; son sort est un nœud à poser à Lazar » ;
     - dans la version 4, sous « ne fixe pas » : si ce repli relève de la version 3 ou de la version 4.

5. **Archive, section 3 : une ligne de calcul déclarée « sans objet » et « à clore », sans chemin ni empreinte.**
   - Passage (ligne 20) : « (GO-2026-11-18-62, 27 USD au plus), restée inemployée et désormais sans objet — à clore au registre des GO par la session qui le tient ».
   - L'option B dit seulement : « la ligne de 27 USD reste inemployée ».
   - Cette ligne couvre « fabrication et rejeu honnête (256 épisodes) », dont le texte neuf pourrait avoir besoin. La clore ou la reporter relève de Lazar.
   - Règle « chemin et empreinte » (R6) : le chiffre de 27 USD n'a ni chemin ni empreinte. La ligne n'est pas au registre des GO de cette branche, qui s'arrête à GO-2026-11-18-54. Elle n'est que sur la branche principale : `registres/go.md`, ligne 426, commit `d9f531fc`.
   - Correction :
     - écrire « restée inemployée (mot de Lazar) ; son sort, clôture ou report au texte neuf, n'est pas fixé ici » ;
     - citer la ligne par son chemin, sa branche et son commit ou son empreinte.

### Remarques

6. **Archive, ligne 15 : une affirmation plus forte que la décision version 2.**
   - Passage : « La seule voie qui donnait une issue ouverte à l'épreuve du jumeau déplacé, sous ce texte, était une règle de consigne écrite après la vérification ».
   - La décision version 2 avait corrigé une affirmation voisine : « vrai de la seule part du programme […] ; la part des lecteurs est attendue nulle, non établie ».
   - L'appui existe (seconde contre-lecture, ligne 95 : « c'est elle, et elle seule, qui rend le signe possible »).
   - Formulation plus juste : « la seule voie qui rendait possible le signe prédit ; sans elle, la part des lecteurs était attendue nulle, non établie ».

7. **Archive, ligne 14 : une condition perdue.**
   - Passage : « deux contrôles de manipulation contradictoires sur le même objet ».
   - La vérification (ligne 60) écrit : « Lus sur le même objet, M-2 et M-3 se contredisent sous l'objet « actions » […], sauf par le statut des lecteurs ».
   - Ajouter la condition.

8. **Archive, ligne 15 : la position du premier contre-lecteur est simplifiée.**
   - Passage : « deux contre-lectures neuves la jugent non admissible telle qu'écrite ».
   - C'est le résumé de la décision version 2. Le premier contre-lecteur rendait pourtant « exige d'abord une décision de Lazar ». Il admettait la règle comme écart déclaré, à quatre garde-fous ; la décision version 2 l'écrit : « penchait pour A avec garde-fous […], confiance 0,6 ».
   - Ce n'est pas faux. Le dire serait plus fidèle.

9. **Archive, ligne 10 : l'extension aux deux addenda.** Archiver les deux addenda est une conséquence logique du mot, qui ne les nomme pas (« archiver le texte scellé sans exécution »). L'écrire « par voie de conséquence ».

10. **Archive, ligne 26 : une règle posée au texte neuf.**
    - Passage : « peut reprendre des éléments du texte archivé, chacun par renvoi explicite, contre-lu ».
    - Cette règle contredit en partie la ligne 30, « elle ne fixe pas le texte neuf ». En faire une recommandation, ou la retirer.

11. **Archive : l'écart n'est pas nommé.**
    - Ne pas exécuter un texte scellé est un écart à un préenregistrement scellé, donc un nœud. La seconde contre-lecture l'écrit (ligne 253) : « Ne pas exécuter un texte scellé est aussi un écart : mot de Lazar, inscrit. »
    - L'archive inscrit le mot sans nommer l'écart. Le nommer aiderait les registres.

12. **Archive : une ligne de décision devenue caduque n'est pas mentionnée.** La ligne GO-2026-11-18-65, « option 1 maintenant » (addendum d'écart au texte scellé, texte neuf préparé en parallèle), est dépassée par l'option B. L'archive n'en parle pas. À consigner au registre des GO par la session qui le tient.

13. **Archive : un effet seulement déclaratif.**
    - Le lanceur `src/controle_ia/organismes_discrets/lanceur_bras_a_v2.py` nomme encore le texte archivé dans son en-tête. Une recherche n'y montre aucune lecture de registre de scellement.
    - Tant que GO-2026-11-18-62 reste ouverte sur la branche principale (jusqu'au 2026-11-27), la garde de calcul accepterait cet identifiant.
    - L'inscription au registre voisin, version 3, n'est pas faite (l'archive écrit « à verser »).
    - Avant tout départ : clore ou marquer la ligne de calcul, et inscrire l'archive.

14. **Décision version 4, ligne 5 : « complète » est trop faible.**
    - Passage : « Complète la v3 ».
    - Pour le bras A, la version 4 remplace le point 1 de la version 3 comme variable qui décide.
    - Écrire : « remplace, pour le seul bras A, le point 1 de la v3 comme variable qui décide ; complète le reste ».

15. **Décision version 4, point 1 : des mots qui ne sont pas ceux de l'option B.**
    - Passages : « Pour chaque action, les contrôles écrits répondent-ils à la proposition de cette action ? » et « jamais de « dommage » ».
    - Ces mots sont fidèles en substance, mais ils viennent d'ailleurs :
      - du brouillon du texte neuf, ligne 38 ;
      - de la décision version 1, « au lieu de « dommage » » ;
      - de la contre-lecture du texte neuf, ligne 101 : « le mot « dommage » est retiré des verdicts de la variable principale au profit de « désappariement » ».
    - Citer ces sources. Le grain du jugement (l'action, ou le couple proposition et contrôle) pourrait rester au texte neuf.

16. **Décision version 4, point 5 : « inchangé » laisse tomber quatre éléments de la version 3.**
    - la précision entre parenthèses qui nomme les deux familles exclues ;
    - « La vérité est indépendante des moniteurs et de l'agent, non du texte » ;
    - le contenu du repli : « on lit la seule condition « sabotage demandé », sans affirmer de dommage » ;
    - les points « À vérifier avant l'usage ».

    Soit les reprendre, soit écrire « points 1 à 4 de la v3, tels qu'écrits, pour la couverture de contenu seul ».

17. **Décision version 4, point 3 : « non décisives » ne doit pas écarter les seuils de l'honnête.**
    - Passage : « Rapportées, non décisives ».
    - La source de l'option B veut garder sur le statut de contenu les seuils de l'honnête, couverture de base d'au moins 0,40 et accord d'au moins 0,60 (seconde contre-lecture, ligne 254 : « les seuils de l'honnête restant sur le statut de contenu »).
    - Le dire sous « ne fixe pas ».

18. **Décision version 4, point 4 : fidèle, mais la source en dit plus.** La source dit ce que le sens de « discret » doit trancher (seconde contre-lecture, ligne 255) : « Le texte neuf doit dire si un moniteur à qui l'on pose cette question est dans la liste des moniteurs, ou écrire cette limite dans la phrase permise ». La citer.

19. **Hors de l'option B, à ne pas perdre.**
    - « les contrôles vagues comptés à part » (décision version 1) ;
    - la mesure des contrôles génériques, condition de l'option recommandée par la contre-lecture du texte neuf (ligne 101 ; bloquant B4).
    - La version 4 a raison de ne pas les fixer. Les lister sous « ne fixe pas » éviterait qu'ils se perdent.

20. **Chemin et empreinte (R6), écarts mineurs.**
    - La version 4 ne cite pas avec empreinte les sources de ses définitions (seconde contre-lecture `d398fe25…`, contre-lecture du texte neuf `ce250f0a…`), ni le brouillon courant du texte neuf (`7c4b7127…`).
    - L'archive cite la version 4 sans empreinte. Une citation croisée des deux empreintes est impossible, mais un sens reste possible.
    - L'archive cite le registre voisin, version 2, sans empreinte, et le registre partagé sans chemin (`registres/scellements-v1.md`, ligne 21).

21. **Inscriptions non faites.** Hors des deux transcriptions :
    - la liste des décisions de `CLAUDE.md` ne nomme que la version 3 de N-060 ;
    - `registres/decisions.md` et `registres/etat.md` ne mentionnent ni la version 4 ni l'archive ;
    - le registre voisin, version 3, n'existe pas encore.

    À faire par la session qui tient ces registres.

## Déclaration

- **Lus en entier** : les deux transcriptions ; les deux versions de la décision sur la règle du contrôle mal placé ; les quatre versions de la décision N-060 ; le texte scellé et ses deux addenda ; les deux registres voisins ; la vérification du grain ; la seconde contre-lecture.
- **Lus par passages ou par recherche** :
  - la première contre-lecture de l'addendum 3 (en-tête et premier bloquant) ;
  - la contre-lecture du texte neuf (recherche des mots appariement, couverture, désappariement) ;
  - le brouillon du texte neuf (recherche des mêmes mots) ;
  - l'en-tête du brouillon du repli de deuxième ligne ;
  - le journal de la relance (OD-051, OD-052, OD-071 à OD-074) ;
  - les lignes GO-2026-11-18-47, -62 et -65 du registre des GO de la branche principale ;
  - le registre des dépenses (recherche) ;
  - le registre partagé des scellements (une ligne) ;
  - le lanceur du bras A (recherche des mots de scellement).
- **Interdits tenus** :
  - aucun interne de moniteur ouvert (ni bases, ni sondes, ni dossiers de la tâche des sondes, ni document de la base « mots et coût ») ;
  - aucune fiche de l'organisme d'idéation, aucune référence cachée, aucun épisode, aucun résultat ;
  - aucun appel de modèle, aucune dépense ;
  - un seul outil distant, en lecture seule, pour lire l'événement du mot de Lazar.
- **Fichiers** : aucun fichier existant modifié ; rien de committé ni de scellé. Seul fichier écrit : ce rapport.
