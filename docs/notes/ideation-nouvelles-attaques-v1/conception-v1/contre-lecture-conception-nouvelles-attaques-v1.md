# Contre-lecture — conception de la course « nouvelles attaques », pièces v1 — v1

- Contre-lecteur, modèle O. Écrite le 2026-11-20 ; relevé de `date -u` : 01:34:20Z, après les lectures et avant l'écriture. Contre-lecteur neuf : je n'ai écrit ni le mandat du rédacteur ni les pièces.
- Mandat : `docs/notes/ideation-nouvelles-attaques-v1/conception-v1/mandat-contre-lecteur-conception-nouvelles-attaques-v2.md` (`d80edb6c6bdd1e4b0c9eb2de5283e059a177d71b2a213d59d2ae9eb9bd36d858`, vérifiée contre son compagnon), sur GO-2026-11-20-06.
- Processeur seul. Aucun appel à un fournisseur de modèles, aucune dépense, aucune écriture dans le dépôt, aucun commit. Réseau : un seul `git fetch origin main` (tête `6f7cd0f8b8a9556499f32642f674ddba7d520c06`). Aucune commande sur un chemin sous `archives-reponses-modeles/`, aucune commande de liste. **Aucun refus d'outil ni de classifieur.**

## 0. Verdict

**Conforme après corrections.** Vingt et une corrections, au § 3, chacune avec son texte de remplacement.

1. **Aucune recette** dans aucune pièce. Une phrase de la question invite à décrire comment la menace serait plantée dans un monde : correction préventive C16.
2. La question est **neuve et distincte** des trois questions scellées, et le complément 1 est porté en entier. Trois défauts de la règle d'antériorité : la « classe » de mécanisme se confond avec la case servie (C10) ; le choix des fiches lues n'est pas écrit d'avance (C12) ; les travaux du dépôt sur l'évasion des moniteurs manquent aux sources (C14).
3. Ce que l'ordre de course dit de la version 68 est juste au regard des pièces. Mais **GO-2026-11-20-05**, postérieur aux pièces, en change cinq endroits (C1 à C9, § 2) :
   - par 1a, la version suivante et le lanceur 11 sont pris par le palier 1 ;
   - par 2b, ce qui passe d'une génération à l'autre n'est plus un choix entre rien et un registre ;
   - D2 et D3 se récrivent.
4. Le **devis** se rejoue à l'octet, deux fois, et chaque source est vérifiée par son empreinte. Deux erreurs :
   - le troisième relais est présent dans les trois compositions, à 199,65 USD (C17) ;
   - le reste du premier relais est de 162,56 USD et non de 162,57, l'épreuve des témoins de la v9 ayant coûté 0,980399 sur cette clé au lieu des 0,97 estimés (C18).

   L'alerte sur le crédit reste juste dans son sens : la clé ne couvre ni 450 ni 195 USD.
5. Les décisions sont au format, sauf une : le défaut de D6 porte sur une dépense (C20).
6. **Aucun identifiant de modèle** dans les six pièces.

## 1. Empreintes vérifiées

Toutes égales aux valeurs du mandat et à leurs compagnons (`sha256sum -c`, lancé par `env -C`) :

| pièce | empreinte |
|---|---|
| question v1 | `dfa2fdf19a8dd043b9d52fe50758cb718aade34e3a40b9697e8cbdeca148d44f` |
| ordre de course v1 | `d47f70800ec4412b65c583d15977cd72cbe96f22fda0ff475be966f1b4133f36` |
| devis v1 | `638492f1cc65151c0528ed62f5d13849d4629336a65b80d1db1ba054e61c6268` |
| programme de calcul v1 | `7fdde8e53d00237dc1c4fdc12301a4f0faf30286a4d7957cdc1f1c36cc35cbf0` |
| sortie du calcul v1 | `216cfbfceb026c7d83e153182232ee6f95a680cefd60e54bfaa0a1193b4ba3e4` |
| rapport du rédacteur v1 | `61a35c2bfa92b3e311c25cfc1a9291725e796c4e61d17acfb67b50fdf6a30969` |

Les pièces qui font foi, recalculées et égales aux empreintes qu'elles portent :
- le mandat du rédacteur, `8fd94f6f…`, et son complément 1, `226ea152…` ;
- N-044 `2b70bdac…`, N-045 v2 `c7b05e39…`, N-049 `8a5bf5e5…`, N-058 `854f2724…`, N-065 `f820e90d…` ;
- les trois questions : `29870ac9…`, `2dbad4b7…`, `7d22b64e…` ;
- la fiche v7, `5ddfae18…`, et le rapport du développeur de la version 68, `ad42b722…` ;
- la contre-lecture de la version 68, `d2cfeac1…`, vérifiée par son empreinte seulement.

Sources du devis :
- S1 `30c87fa6…`, S3 `a8c033cd…` et sa sortie `1f43d531…`, S4 `531849e3…` ;
- la synthèse v2b, `b828d800…` ;
- au commit `af32512da` : `registres/depenses.md`, `43cad7c0…`, et `registres/go.md`, `7fce4374…`.

Sur `main` (`6f7cd0f8`) :
- `registres/go.md` : `685e67d0ab11c65ea75a17c34d03740feeaac8951f73fd878d2800a70cf160a6`, lignes GO-2026-11-19-19 à -21, -89, -94 à -96 et GO-2026-11-20-05 et -06 lues ;
- `registres/decisions.md` : `011051dfbeaa4b09b2cd7e96f529b4ab155ba0862a810d4b65c774c8a4b02583`, R-606 à R-611 lues, plus R-3237 et R-4035, que les pièces citent ;
- `registres/depenses.md` : `a6d50ecad8a5c11e349b288989d3bda7237237c6e5037220ba11b2becb2d72f7`.

## 2. Les six vérifications du mandat

### 2.1 Aucune recette

Chaque phrase des quatre pièces est relue. Aucune ne contient de procédé, d'étape, de réglage, d'exemple joué, de texte d'instruction ou de code. Les valeurs des trois axes sont des hypothèses de moniteur, des menaces du programme et des étages de lecture, toutes abstraites. Le témoin « champ comment faire » est un texte inerte (ordre, § 7).

Une seule phrase invite au concret : le point 2 de la question servie, et la glose du champ `mesurable_sur_monde_plante`. Demander « ce qu'un monde planté devrait contenir » pour une menace pousse le proposeur à décrire comment la menace y serait produite. La correction C16 est préventive, mais obligatoire au sens du mandat.

### 2.2 Question neuve et complément porté

La table du § 1 de la question sépare bien l'objet de chacune des trois questions scellées. Pour le coffre, elle sous-dit deux emprunts, et C10 en tient compte :
- la question reprend aussi sa taxonomie, l'axe « ce que le moniteur suppose » ;
- ses fiches ressemblent au gabarit de carte de menace du coffre.

Le complément est porté en entier :
- l'inédit est dit en tête, avec l'étiquette bornée « inédite au périmètre vérifié le [date] » ;
- la règle d'antériorité est écrite d'avance, avec ses sources, ses lecteurs et l'issue « non tranchée, non dite inédite » ; elle tient R3, R7 et R8 ;
- le chemin vers le bras est écrit, avec la relecture « aucune recette », les trois scellements et R-611 ;
- qui décide est dit (ordre, § 10).

Quatre défauts restent :
1. **La classe se confond avec la case** (C10). Une fiche est dite porter « une classe (les trois champs fermés) ». Ces champs sont ceux de la case servie : toutes les fiches d'une case partagent donc leur classe. La condition 2 jugerait alors l'inédit par la case seule, contre l'intention même que la question emprunte au coffre, la nouveauté par classe de mécanisme.
2. **Le choix des fiches lues n'est pas écrit d'avance** (C12). Seules « les fiches que la mère retient » sont lues pour l'antériorité, et rien ne dit comment elle retient. Les juges lui donnent un ordre de lecture : un choix non écrit d'avance ouvre la porte à une sélection par le rang des juges, contre R3 et R4, et la lettre de N-058 sur les juges ne le borne pas.
3. **L'effort n'est pas le même des deux côtés** (C13). La symétrie dit « le même effort pour toute fiche lue », mais seul le côté « sans antériorité » passe à un second lecteur. Le contrôle d'une antériorité trouvée n'est pas écrit.
4. **Une source manque** (C14). Les travaux du dépôt sur l'évasion et la corruption des moniteurs ne sont pas parmi les sources de l'antériorité : le collisionneur « évasion et moniteurs », les quatre familles d'évasion (R-606, R-610, R-611) et l'attaque de Goodhart (N-065, rôle 1). La règle R8 veut une vérification plus dure.

Une cinquième correction, C15, tient au tirage et non à l'antériorité : la famille tenue à l'écart pourrait tomber sur « autre, à nommer », qui n'est pas une famille de mécanisme.

### 2.3 L'ordre de course

L'ordre tient les décisions qui font foi :
- **N-044** : régime d'usage, code et composition figés, aucune réserve de re-conception.
- **N-045 v2** : K = 3, gelé ; coût par espèce et par rôle au journal ; nécessité de la frontière rapportée ; aucune réduction sans preuve. La lecture du point 2 est déclarée : le coût n'est servi à personne, faute de score servi (GO-89) et parce que le code est figé. C'est défendable, et dit.
- **N-049** : la case comme tâche, tirée par une graine dérivée (R9), sans remise, et une famille entière tenue à l'écart.
- **N-058 et GO-89** : rien du juge n'est servi ; les juges ne tranchent rien.

Ce qu'il dit de la version 68 est juste au regard du rapport du développeur et de la fiche v7 :
- le moteur réel est refusé dans tous les régimes, éteint compris ;
- aucun additif n'est épinglé ;
- le plafond de course est réservé génération par génération ;
- le montant requis vaut N × S17.

Un point était faux avant même GO-2026-11-20-05 : l'ordre prend le « lanceur 11 » pour la course. Or le rapport du développeur, § 9, point 2, le définit comme le lanceur du régime « tests de mort seuls, sans lecture ».

Défauts propres à l'ordre :
- deux mesures de l'héritage sont fixées par construction (C11) : la redite « même case » est impossible entre générations, et le nombre de cases couvertes est fixé par le tirage ;
- le contrôle de la fiche v7 est cité sans chemin, contre R6 (C21).

Ce que GO-2026-11-20-05 change est au § 2 ci-dessous.

### 2.4 Le devis

**Rejeu.** J'ai copié le programme dans mon dossier et l'ai joué deux fois (`python3 -B`, Python 3.13.18). Les deux sorties sont égales à l'octet à la sortie versée (`cmp` muet les deux fois).

**Sources.** S1 à S6 sont vérifiées par empreinte, et leurs chiffres relus aux lignes citées :
- S1 : coûts par rôle et tentatives 94, 56 et 38 ;
- S2, ligne 536 : 72,502472 et 36,457056 ;
- S3, § 1 à § 4 : 55,94 ; 137,81 ; 140, 135 et 120 ; 6,05 ; 199,03 ; 66,55 ;
- S5 : 150, 5 et 6 ;
- S6 : N × S17.

**Cas.** Bas, haut, pire, plafond et ligne sont cohérents entre le texte, la table et la sortie :
- 72,51, 137,81 et 150 par génération ;
- 217,53, 413,43 et 450 sur la course ;
- 218,72 et 419,43 de total, 456 de plafond total ;
- les mêmes enchaînements pour trois et deux espèces, et les seuils au cas haut sont tous lancés.

L'écart d'un centime de S1 est dit.

Erreurs :
- **Le troisième relais (C17).** Il porte le proposeur de l'espèce 2 : sa dépense à la v9, 4,74571 en S2, est le coût de ce rôle en S1, et S3, § 3, lui donne 11 × 6,05 = 66,55. L'espèce 2 est dans les trois compositions, et le relais vaut 199,65 partout, non « à relever ». La colonne « ce qu'il tient » est aussi incomplète. Le premier relais porte, en plus de l'aiguilleur et d'un juge, les proposeurs des espèces 3 et 4 : 36,457056 = 7,43 + 17,58 + 4,59 + 6,86. Le deuxième porte, en plus d'un juge, ceux des espèces 1 et 5 : 31,299704 = 4,17 + 24,72 + 2,41.
- **Le crédit du premier relais (C18).** Le net de 199,03 de S3 comptait l'épreuve des témoins à 0,97 estimé. Elle a coûté 0,980399 sur cette clé (S2, ligne 532, même fichier, même empreinte). Le reste vaut 200 − 0,000108 − 0,980399 − 36,457056 = **162,562437**, donc 162,56. Les manques valent 287,44 et 32,44, et la composition à deux espèces reste couverte. Au registre de `main` relu ce jour, aucune ligne postérieure ne porte sur cette clé. La dispense des deux autres clés (R-3237) a été posée par la mère pour une course : elle est à redire pour celle-ci.
- **Le repère S4 (C19).** Les 8,42 USD sont la séquence complète de la fille 2 sur la question v1 : sonde, course et bras, dont environ 3,80 de tentatives avortées. Ce n'est pas « une course d'une génération ». Le repère n'entre dans aucun total.

### 2.5 Les décisions pour Lazar

D1 et D7 sont au format, sans défaut pour une dépense ; D2 est sans défaut pour ce qui est servi ; D4 et D5 portent un défaut sous 48 heures, légitime. Restent deux décisions :
- **D6, les juges.** Le défaut sous 48 heures « (a), juges joués » porte sur une part de la dépense : 27,81 USD au cas bas. C'est contraire au mandat (C20).
- **D3.** Son défaut est mal formé, et l'option « attendre ton mot sur la fiche v7 » est caduque. D3 se récrit en entier (C9).

### 2.6 Identifiants de modèle

Recherche, insensible à la casse, des noms d'espèces et de fournisseurs connus du dépôt dans les six pièces : aucun. Seuls apparaissent `CLAUDE.md`, un nom de fichier, et la chaîne « claude-0 » du chemin de bloc-notes, un faux positif. Ce document n'en contient aucun non plus : les espèces sont dites par leur numéro.

## 3. Ce que GO-2026-11-20-05 change aux pièces

GO-2026-11-20-05 est le mot de Lazar vers 01:14Z ; les pièces datent de 01:01Z. Lazar a pris 2b contre la recommandation (a) de la fiche v7 (R-4035).

- **1a, à la version qui portera la course.** 1a donne la version suivante de l'orchestrateur, le lanceur version 11 et leur additif au seul régime « tests de mort sans rien servir, palier 1 de l'héritage ». L'ordre de course et le rapport nomment pourtant « version 69 » et « lanceur 11 » comme le véhicule de la course. Ils ne peuvent plus l'être, et le régime de la course n'est pas couvert par la routine de 1a. La course demande une version ultérieure et un lanceur qui suit le 11, numéros fixés par leurs mandats, et un mot d'activation de principe à part. La fiche v7 l'écrit sous l'option (a) de sa décision 1 : « les lignes qui demandent la lecture attendent une seconde décision ». D3 se récrit en ce sens (C9), et son option « attendre ton mot sur les quatre décisions de la fiche v7 » tombe.
- **2b, à D2 et à ce qui est servi.** Lazar fixe une seule règle pour l'organisme : la génération suivante lit ce que sert le registre des tentatives, toutes les tentatives et leur classe d'issue, ce qui demande une version de plus. La divergence GO-89 / GO-76 est tranchée du côté de la lecture de l'héritage : ni verdict de juge, ni sélection des survivantes. L'ordre l'avait prévu (§ 5, ce qui ferait changer la recommandation ; réserve 5) : le § 5 s'aligne. En conséquence :
  - D2 n'est plus le choix « H0 ou H1 », et son défaut « sans ton mot, H0 » irait contre 2b ;
  - le point 6 du § 2 n'est plus conditionnel ;
  - le régime de la course n'est plus « éteint, sans étage » mais « lecture sans étage », un régime que la version 68 refuse par construction (rapport du développeur, § 4).

  Reste un nœud neuf : la forme du registre dans une course qui n'exécute aucune épreuve. Sa seule issue est l'aiguillage du portier. Ce portier est un modèle, et ce qui est au coffre ne se relit jamais (R-607). Faut-il servir le compte des tentatives au coffre ? C'est le nouveau D2 (C6, C9).
- **3a et 4b** ne changent rien. La course fixe ses propres champs (fiche v7, verdict, point 4) et ne loue aucune machine. Le point 2 du verdict de l'ordre (« seule la deuxième la touche ») devient faux, car 1a la touche aussi (C2).

## 4. Corrections

Elles s'appliquent à texte exact, par l'outil `scripts/remplacer_texte_exact_v1.py`, sous des noms de version neufs (R12). « Ancien » est copié des pièces v1 ; « nouveau » le remplace.

### Ordre de course

**C1 — § 0, point 1 (1a).**
- Ancien : `La course demande une version suivante (69), un lanceur neuf (11), un additif scellé et une configuration propre. C'est du travail sur processeur, sans dépense (§ 2).`
- Nouveau : `Ton mot GO-2026-11-20-05 (1a) réserve la version suivante de l'orchestrateur, le lanceur version 11 et leur additif au seul régime du palier 1 de l'héritage ; ton mot 2b demande une version de plus pour la lecture du registre des tentatives. La course demande donc une version ultérieure de l'orchestrateur, un lanceur qui suit le 11, un additif scellé et une configuration propre, numéros fixés par leurs mandats. C'est du travail sur processeur, sans dépense (§ 2).`

**C2 — § 0, point 2.**
- Ancien : `Des quatre décisions de la fiche de la version 68, seule la deuxième la touche : ce qui est servi à la génération suivante (§ 5).`
- Nouveau : `Des quatre décisions de la fiche de la version 68, tranchées par GO-2026-11-20-05, deux la touchent : la première (1a), qui prend la version suivante et le lanceur 11 pour le palier 1 de l'héritage (§ 2), et la deuxième (2b), ce qui est servi à la génération suivante (§ 5). 3a et 4b ne la touchent pas.`

**C3 — § 0, point 3.**
- Ancien : `3. **Ce qui passe d'une génération à l'autre est ton nœud.** Je recommande un registre de toutes les fiches passées par le portier, sans verdict ni tri ; sans ton mot, rien n'est servi (§ 5).`
- Nouveau : `3. **Ce qui passe d'une génération à l'autre est fixé par ton mot 2b** : le registre de toutes les tentatives et de leur classe d'issue, sans verdict ni tri. Reste ton nœud : sa forme dans une course sans épreuve exécutée, où la seule issue est l'aiguillage du portier (§ 5).`

**C4 — § 2, le régime.**
- Ancien : `**Le régime dont la course a besoin** est celui que la version 68 appelle « éteint, sans étage » : trois générations, aucun étage de tests de mort, montant requis égal à trois fois le plafond d'une génération (rapport du développeur, § 5). Dans ce régime la version 68 ne sert rien ; seule la mémoire qui évite les redites passe, et elle n'est jamais montrée aux proposeurs.`
- Nouveau : `**Le régime dont la course a besoin** n'existe dans aucune version : trois générations, aucun étage de tests de mort, montant requis égal à trois fois le plafond d'une génération (le régime « éteint, sans étage » de la version 68, rapport du développeur, § 5), **plus** la lecture du registre des tentatives que ton mot 2b demande. La version 68 refuse la lecture sans étage (rapport du développeur, § 4) ; la version suivante, sous ton mot 1a, ne vaudra que pour le palier 1 de l'héritage. La mémoire qui évite les redites passe aussi, jamais montrée aux proposeurs.`

**C5 — § 2, la table des manques et ses renvois.**
- Point 1. Ancien : `| 1 | une version 69 qui lève le refus du moteur réel pour **ce seul régime**, nommé, et qui épingle l'additif |`. Nouveau : `| 1 | une version de l'orchestrateur postérieure à celle du palier 1 (GO-2026-11-20-05, 1a), qui lève le refus du moteur réel et de la lecture sans étage pour **ce seul régime**, nommé, et qui épingle l'additif |`.
- Point 2. Ancien : `| 2 | un lanceur de course version 11 : épingle la version 69 ;`. Nouveau : `| 2 | un lanceur de course postérieur au lanceur 11, que ton mot 1a réserve au palier 1 : épingle la version du point 1 ;`.
- Point 6. Ancien : `| 6 | si tu retiens le registre servi (§ 5, option H1) : un lecteur du registre des fiches passées. La version 68 ne lit que la sélection scellée d'un étage de tests de mort, et il n'y en a pas ici |`. Nouveau : `| 6 | un lecteur du registre des tentatives (ton mot 2b, § 5), qui sert toutes les tentatives et leur classe d'issue sous la forme que tu retiens en D2. La version 68 ne lit que la sélection scellée d'un étage de tests de mort, et il n'y en a pas ici |`.
- Coût de la conception. Ancien : `la version 69 ; le lanceur 11 ;`. Nouveau : `la version du point 1 ; son lanceur ;`.
- Ancien : `Le point 6 ajoute un fichier et ses essais à la version 69.`. Nouveau : `Le point 6 ajoute un fichier et ses essais à cette version ; il peut reprendre le lecteur du registre que ton mot 2b demande pour l'héritage, s'il est écrit d'abord.`.
- § 3. Ancien : `additif, configuration, version 69 et lanceur 11 contre-lus`. Nouveau : `additif, configuration, version et lanceur du § 2 contre-lus`.
- § 13, réserve 1. Ancien : `avant d'écrire la version 69.`. Nouveau : `avant d'écrire la version du § 2, point 1.`.

**C6 — § 5 (2b).** Remplacer tout le texte qui va de `**Ce qui reste ouvert**, et qui est ton nœud` jusqu'à `**Défaut** : aucun. Sans ton mot, H0 : rien n'est servi.` inclus. Le texte nouveau :

> **Ce que ton mot 2b fixe** (GO-2026-11-20-05, donné après l'écriture de la v1 de cette pièce). La génération suivante lit ce que sert le registre des tentatives : toutes les tentatives et leur classe d'issue, sans verdict de juge ni sélection des survivantes. C'est une seule règle pour l'organisme, et cette course s'y aligne.
>
> **Ce qui reste ouvert**, et qui est ton nœud (ce qui est servi à un agent) : la forme de ce registre dans une course qui n'exécute aucune épreuve. Sa seule issue est l'aiguillage du portier, « passée » ou « au coffre ». Le portier est un modèle : son aiguillage n'est pas une épreuve exécutée. Ce qui est au coffre n'est jamais relu (R-607).
>
> - **(a) Le registre entier.** Pour chaque tentative passée par le portier : ses trois champs fermés, son nom, son énoncé ramené à une ligne, et la classe d'issue « passée ». Pour les tentatives au coffre : leur seul compte par case, classe « au coffre », sans nom ni énoncé. Aucune note, aucun rang, aucune étiquette d'antériorité ; ordre tiré par graine ; taille bornée en octets, gelée à l'additif ; chaque ligne passée à la garde des étiquettes interdites. Avantage : la lettre de 2b, sans rien relire du coffre. Inconvénient : le compte du coffre dit aux proposeurs où la question a glissé vers le concret.
> - **(b) Le registre sans les comptes du coffre.** Les mêmes lignes pour les tentatives passées ; rien du coffre, même en compte. Avantage : rien du coffre n'est servi. Inconvénient : toutes les tentatives ne sont pas servies, un écart à la lettre de 2b.
>
> Dans les deux formes, le champ `filiation` d'une fiche nomme la fiche du registre dont elle part, ou « aucune » : l'usage de l'héritage laisse une trace comptable. C'est un registre des tentatives, non une archive de découvertes, comme la fiche v7 le rapporte de l'héritage. La seconde passe des courses d'idéation servait déjà aux proposeurs les fiches de la première (`rapports/fille-ideation-1-v1/devis-course-ideation-pilier-attaque-v2-v1.md`, `531849e3e4f55de3ae5f097033fdcb50bd209ac88670547b3060fb869b10eea3`, § 1). Coût commun aux deux formes : le lecteur du registre (§ 2, point 6) et des consignes plus longues.
>
> **Recommandation** : (a), confiance 0,55. Ce qui me ferait changer : que la mère juge, à l'épreuve des témoins, que le compte du coffre pousse les proposeurs vers la forme interdite ; ou que la mesure des consignes montre que le registre ne tient pas dans la borne.
>
> **Défaut** : aucun. Sans ton mot sur la forme, la course ne part pas : ne rien servir irait contre ton mot 2b.

**C7 — § 12.**
- Ancien : `ce qui est servi (H0 ou H1)`.
- Nouveau : `ce qui est servi (le registre de ton mot 2b, sous la forme retenue en D2)`.

**C8 — § 13, réserve 5.**
- Ancien : `5. La fiche v7 attend ton mot. Si tu tranches sa décision 2 pour tout l'organisme, le § 5 s'y aligne.`
- Nouveau : `5. Ton mot GO-2026-11-20-05 (1a, 2b, 3a, 4b) a tranché la fiche v7 après l'écriture de la v1 de ces pièces ; les § 0, § 2, § 5 et § 12 s'y alignent.`

**C10 — Classe de mécanisme et case** (question, § 2 et § 5 ; ordre, § 9).
- Question, § 2. Ancien : `Une fiche porte **une idée** : une classe (les trois champs fermés du § 5) et un énoncé d'une à trois phrases.`. Nouveau : `Une fiche porte **une idée** : sa case (les trois champs fermés du § 5, égaux à ceux de la case servie), sa classe de mécanisme (ce que l'idée met en défaut, lu dans son énoncé) et un énoncé d'une à trois phrases.`.
- Question, § 2, condition 2. Ancien : `2. sa classe est absente du coffre, ce qu'un lecteur isolé dit par oui ou par non, sans rien en sortir d'autre ;`. Nouveau : `2. aucune fiche du coffre ne porte sa classe de mécanisme, ce qu'un lecteur isolé dit par oui ou par non, sans rien en sortir d'autre ;`.
- Question, § 5, champs. Ancien : `` `ce_que_le_moniteur_suppose` (fermé) ; `menace_du_programme` (fermé) ; `etage_de_lecture` (fermé) ; ``. Nouveau : `` `ce_que_le_moniteur_suppose`, `menace_du_programme`, `etage_de_lecture` (fermés, égaux à ceux de la case servie ; une fiche qui en diffère est refusée par le portier et comptée) ; ``.
- Ordre, § 9. Ancien : `**Ce qui est comparé.** L'idée d'une fiche : sa classe (les trois champs fermés) et son énoncé. La nouveauté se juge par classe de mécanisme, non par la surface du texte.`. Nouveau : `**Ce qui est comparé.** L'idée d'une fiche : sa case (les trois champs fermés, égaux à ceux de la case servie), sa classe de mécanisme (ce que l'idée met en défaut, lu dans son énoncé) et son énoncé. La nouveauté se juge par classe de mécanisme, non par la surface du texte ni par la case seule : toutes les fiches d'une case partagent ses trois champs.`.
- Question, § 1, dernière cellule de la ligne du coffre. Ancien : `elle reprend de cette question une seule chose, le jugement de la nouveauté **par classe de mécanisme** et non par la surface du texte`. Nouveau : `elle reprend de cette question sa taxonomie (l'axe « ce que le moniteur suppose ») et le jugement de la nouveauté **par classe de mécanisme**, non par la surface du texte ; ses fiches ressemblent aux cartes de menace du coffre, mais ses proposeurs ne lisent pas le coffre`.

**C11 — § 6, mesures fixées par construction.**
- Ancien : `part des fiches des générations 2 et 3 dont la `filiation` n'est pas « aucune » ; taux de redite d'une génération à l'autre (même classe, même case) ; nombre de classes distinctes couvertes ; part de fiches au coffre, en compte. Ce sont des **descriptions**.`
- Nouveau : `part des fiches des générations 2 et 3 dont la `filiation` n'est pas « aucune » ; nombre de fiches parentes distinctes, et part de la plus citée ; part de fiches au coffre, en compte. Les cases étant tirées sans remise, une redite « même case » d'une génération à l'autre est impossible, et le nombre de cases couvertes est fixé par le tirage : ces deux grandeurs sont rapportées comme contrôles du tirage, non comme mesures de l'héritage. Ce sont des **descriptions**.`

**C12 — § 9, qui est lu.**
- Ancien : `**Qui est lu.** Tous les témoins plantés, et les fiches que la mère retient après la relecture « aucune recette ». Les autres fiches sont « non lues ».`
- Nouveau : `**Qui est lu.** Tous les témoins plantés, et toutes les fiches qui passent la relecture « aucune recette ». Si leur nombre dépasse une borne gelée au préenregistrement court, la part lue est tirée parmi elles par graine (règle R9), jamais par le rang des juges ni par un choix de la mère. Les autres fiches sont « non lues ».`
- Renvois : à l'ordre, § 13, réserve 4, `Elle ne porte que sur les fiches que la mère retient ;` devient `Elle ne porte que sur les fiches lues au sens du § 9 ;`. Au devis, § 7, point 2, `pour les fiches que la mère retient.` devient `pour les fiches lues au sens de l'ordre de course, § 9.`.

**C13 — § 9, symétrie.**
- Ancien : `**Symétrie** (règles R3 et R4). Le même effort de recherche pour toute fiche lue ; le périmètre ne s'élargit ni ne se resserre au vu d'un résultat.`
- Nouveau : `**Symétrie** (règles R3 et R4). Le même effort de recherche, au même périmètre, pour toute fiche lue par le premier lecteur. Le second lecteur lit toute fiche dite sans antériorité (règle R8) et vérifie, sur le PDF et à la page citée, toute antériorité dite trouvée ou partielle : les deux étiquettes sont contrôlées. Le périmètre ne s'élargit ni ne se resserre au vu d'un résultat.`

**C14 — Sources internes de l'antériorité** (ordre, § 9 ; question, § 2).
- Ordre, § 9. Ancien : `(2) les synthèses d'antériorité déjà versées, dont `rapports/fille-ideation-1-v1/synthese-anteriorite-pilier-attaque-v2b.md` ;`. Nouveau : `(2) les synthèses d'antériorité déjà versées, dont `rapports/fille-ideation-1-v1/synthese-anteriorite-pilier-attaque-v2b.md` ; (2 bis) les travaux du dépôt sur l'évasion et la corruption des moniteurs déjà versés — tours du collisionneur « évasion et moniteurs » et document des quatre familles d'évasion (R-606, R-610, R-611), attaque de Goodhart (N-065, rôle 1) —, lus par un lecteur isolé qui ne rend qu'un oui ou un non par classe là où ces pièces sont cloisonnées ;`.
- Ordre, § 9, table des étiquettes. Ancien : `les deux lecteurs, aux cinq sources, n'en trouvent pas`. Nouveau : `les deux lecteurs, à toutes les sources de la liste, n'en trouvent pas`.
- Question, § 2, condition 1. Ancien : `1. son idée est absente des questions v1 et v2 du pilier attaque, de la question du coffre, et des synthèses d'antériorité déjà versées ;`. Nouveau : `1. son idée est absente des questions v1 et v2 du pilier attaque, de la question du coffre, des synthèses d'antériorité déjà versées et des travaux du dépôt sur l'évasion et la corruption des moniteurs (R-606, R-610, R-611 ; N-065, rôle 1) ;`.
- Rapport, § 4, point 2. Ancien : `à deux lecteurs, cinq sources.`. Nouveau : `à deux lecteurs, aux sources de l'ordre de course, § 9.`.

**C15 — § 4, famille tenue à l'écart.**
- Ancien : `toutes les cases d'une valeur de l'axe « ce que le moniteur suppose », tirée par graine avant la course, soit 20 cases.`
- Nouveau : `toutes les cases d'une valeur de l'axe « ce que le moniteur suppose », tirée par graine avant la course parmi les cinq valeurs nommées (jamais « autre, à nommer », qui n'est pas une famille de mécanisme), soit 20 cases.`

**C21 — En-tête de l'ordre (R6).**
- Ancien : `contrôlée « Conforme », `522a3c46aa588b72cae3ff723451166337f2181c7600560e40af686a12725a09`), qui attend ton mot.`
- Nouveau : `contrôlée « Conforme », contrôle `522a3c46aa588b72cae3ff723451166337f2181c7600560e40af686a12725a09`, R-4035 sur `main`), sur laquelle tu as donné ton mot après l'écriture de la v1 de ces pièces (GO-2026-11-20-05 : 1a, 2b, 3a, 4b).`

### Question

**C16 — § 4, point 2, et § 5, champ `mesurable_sur_monde_plante` (aucune recette, préventive).**
- § 4. Ancien : `> 2. dis ce qu'un monde planté devrait contenir pour que la question « le moniteur la voit-il ? » reçoive une réponse calculée par un oracle, et quelle grandeur on y lirait ;`. Nouveau : `> 2. dis ce qu'un monde planté devrait permettre d'observer et de compter pour que la question « le moniteur la voit-il ? » reçoive une réponse calculée par un oracle, et quelle grandeur on y lirait, sans dire comment la menace y serait produite ou plantée ;`.
- § 5. Ancien : `(ce que le monde contient, la grandeur lue, l'oracle)`. Nouveau : `(ce que le monde permet d'observer et de compter, la grandeur lue, l'oracle ; jamais comment la menace y serait produite)`.

C10 et C14 touchent aussi la question.

### Devis, programme et sortie

**C17 — § 3, relais, et programme.** Remplacer la table « Par relais, sur la course », de la ligne `| relais | ce qu'il tient | cinq espèces | trois espèces | deux espèces |` jusqu'à la ligne `| troisième | un proposeur seul | 199,65 | à relever | à relever |` incluses, par :

```
| relais | ce qu'il tient | cinq espèces | trois espèces | deux espèces |
|---|---|---|---|---|
| premier | l'aiguilleur, le juge de l'espèce 3 et les proposeurs des espèces 3 et 4 (à trois espèces : de l'espèce 3 ; à deux : aucun) | 450 | 195 | 150 |
| deuxième | le juge de l'espèce 1 et les proposeurs des espèces 1 et 5 (à trois et à deux espèces : de l'espèce 1) | 450 | 195 | 150 |
| troisième | le proposeur de l'espèce 2 seul, présent dans les trois compositions | 199,65 | 199,65 | 199,65 |

Répartition lue à la course v9 : 36,457056 USD sur la première clé (S2) = 7,43 + 17,58 + 4,59 + 6,86 (S1) ; 31,299704 sur la deuxième = 4,17 + 24,72 + 2,41 ; 4,74571 sur la troisième = 4,75 ; parts au pire de S3, § 3. Le troisième relais vaut 11 × 6,05 × 3 au compte de S3 ; à trois et à deux espèces, le plafond dur de la proposition (55 ou 40 USD par génération) le coupe avant.
```

Dans le programme, nouvelle version et nouveau nom, sa sortie de même :
- Ancien : `                ) if nom == "A" else "sans objet ou a relever",`
- Nouveau : `                ),`

**C18 — § 6 et renvois : le crédit du premier relais.**
- Devis, § 6. Ancien : `Le devis v2i comptait 199,03 USD nets sur cette clé avant la course v9 (S3, § 3) ; la course v9 y a dépensé 36,457056 USD (S2). Il resterait **162,57 USD**, sous réserve de toute dépense postérieure, que je n'ai pas relevée.`. Nouveau : `Le devis v2i comptait 199,03 USD nets sur cette clé avant la course v9 (S3, § 3), l'épreuve des témoins y étant estimée à 0,97. Elle y a coûté 0,980399 USD (S2, ligne 532), après la vérification de la clé, 0,000108 (S2, ligne 528) ; la course v9 y a dépensé 36,457056 USD (S2, ligne 536). Il resterait **162,56 USD** (200 − 0,000108 − 0,980399 − 36,457056 = 162,562437). Aucune ligne postérieure sur cette clé au registre des dépenses de `main` relu le 2026-11-20 (commit `6f7cd0f8`, `a6d50ecad8a5c11e349b288989d3bda7237237c6e5037220ba11b2becb2d72f7`) ; le relevé du jour du devis final prime.`.
- Devis, table du § 6. `| cinq espèces | 450 | non | 287,43 |` devient `| cinq espèces | 450 | non | 287,44 |`, et `| trois espèces | 195 | non | 32,43 |` devient `| trois espèces | 195 | non | 32,44 |`.
- Devis, fin du § 6. Ancien : `Les crédits des deux autres relais étaient illisibles et sous dispense au devis v2i ; je ne les ai pas relevés.`. Nouveau : `Les crédits des deux autres relais étaient illisibles et sous dispense au devis v2i ; je ne les ai pas relevés. Cette dispense (R-3237 : départ permis, arrêt au premier refus pour crédit) a été posée par la mère pour une course : qu'elle vaille pour celle-ci est à redire au devis final.`.
- Devis, § 0, point 3 : `environ 162,57 USD` devient `environ 162,56 USD`. Devis, § 9 : `d'au moins 287,43 USD` devient `d'au moins 287,44 USD`, et `manque encore de 32,43 USD` devient `manque encore de 32,44 USD`.
- Rapport : `d'au moins 287,43 USD` (D1) devient `d'au moins 287,44 USD`, et `environ 162,57 USD` (D7) devient `environ 162,56 USD`.
- Programme, nouvelle version. Ancien : `V2I_CREDIT_NET_RELAIS_1_AVANT_V9_USD = D("199.03")`. Nouveau, sur trois lignes : `V2I_CREDIT_NET_RELAIS_1_AVANT_V9_USD = D("199.03")  # estimation de S3, rapportee seulement`, puis `DEPENSE_VERIFICATION_CLE_RELAIS_1_USD = D("0.000108")  # S2, ligne 528`, puis `DEPENSE_EPREUVE_V9_CLE_RELAIS_1_USD = D("0.980399")  # S2, ligne 532`.
- Programme, même version. Ancien : `    credit_reste = V2I_CREDIT_NET_RELAIS_1_AVANT_V9_USD - V9_PART_CLE_RELAIS_1_USD`. Nouveau : `    credit_reste = (V2I_CREDIT_DECLARE_RELAIS_1_USD - DEPENSE_VERIFICATION_CLE_RELAIS_1_USD - DEPENSE_EPREUVE_V9_CLE_RELAIS_1_USD - V9_PART_CLE_RELAIS_1_USD)`. Attendu : reste `162.562437`, manques `287.44`, `32.44` et `0.00`.

La nouvelle sortie se joue deux fois et se compare à l'octet. Le devis cite ses nouvelles empreintes.

**C19 — § 1, ligne S4.**
- Ancien : `course d'idéation sur le pilier attaque : 8,42 USD réels pour une course d'une génération, plafond 20 ; sonde de refus ≈ 0,005 pour trois modèles`
- Nouveau : `8,42 USD réels pour la séquence complète d'une course d'idéation d'une génération sur la question v1 du pilier attaque (sonde, course et bras, dont ≈ 3,80 de tentatives avortées) ; plafond 20 de la course sur la question v2 ; sonde de refus ≈ 0,005 pour trois modèles`
- La colonne du chemin de S4 cite aussi le § 3.2.

**C9, suite — renvois du devis à 2b.**
- § 2. Ancien : `une case et, si tu le retiens, un registre borné.`. Nouveau : `une case et, aux générations 2 et 3, le registre borné que ton mot GO-2026-11-20-05 (2b) fait servir.`.
- § 7, point 3. Ancien : `(ordre de course, § 5, option H1)`. Nouveau : `(ton mot 2b ; ordre de course, § 5)`.

### Rapport du rédacteur

**C9 — § 1, § 4, D2, D3 et § 6 (1a et 2b).**
- § 1, point 3. Ancien : `3. **La course est portée par une version 69 de l'orchestrateur, qui reste à écrire.** La version 68 ne joue plusieurs générations qu'en moteur simulé. Il manque aussi un lanceur version 11, un additif scellé et une configuration propre.`. Nouveau : `3. **La course est portée par une version de l'orchestrateur postérieure à celle que ton mot GO-2026-11-20-05 (1a) réserve au palier 1 de l'héritage, et qui lit le registre des tentatives (2b) ; elle reste à écrire.** La version 68 ne joue plusieurs générations qu'en moteur simulé. Il manque aussi un lanceur qui suit le 11, un additif scellé et une configuration propre.`.
- § 4, point 5. Ancien : `5. **Héritage : un registre sans verdict ni tri**, recommandé, sur ton mot ; sinon rien.`. Nouveau : `5. **Héritage : le registre des tentatives de ton mot 2b**, sans verdict ni tri ; sa forme dans cette course est D2.`.
- D2. Remplacer tout le texte qui va de `### D2 — Ce que la génération suivante lit` jusqu'à `**Recommandation.** H1, confiance 0,6. **Défaut.** Aucun ; sans ton mot, H0.` inclus. Le texte nouveau :

  > ### D2 — La forme du registre servi, sous ton mot 2b
  > **Décision.** Dans cette course, qui n'exécute aucune épreuve, le registre des tentatives de ton mot 2b sert-il aussi le compte des tentatives au coffre ?
  > **Enjeu.** Ton mot 2b (GO-2026-11-20-05) fixe la règle : toutes les tentatives et leur classe d'issue, sans verdict ni tri. Ici la seule issue est l'aiguillage du portier, un modèle ; ce qui est au coffre n'est jamais relu (R-607). Ce qui est servi à un agent reste ton nœud.
  > **Options.** (a) le registre entier : les tentatives passées avec leurs champs fermés, leur nom et leur énoncé ramené à une ligne, et celles du coffre en compte par case seulement. C'est la lettre de 2b, mais le compte dit où la question a glissé vers le concret. (b) le même registre sans les comptes du coffre : rien du coffre n'est servi, mais c'est un écart à la lettre de 2b.
  > **Recommandation.** (a), confiance 0,55. **Défaut.** Aucun : ce qui est servi à un agent est un nœud ; sans ton mot, la course ne part pas.

- D3. Remplacer tout le texte qui va de `### D3 — Préparer le véhicule` jusqu'à `**Recommandation.** (a), confiance 0,7. **Défaut.** Écrire le code, éteint, est de la routine ; l'allumage n'a pas de défaut.` inclus. Le texte nouveau :

  > ### D3 — Le véhicule de la course
  > **Décision.** Donnes-tu le mot d'activation de principe d'un régime de plus, « trois générations, sans étage de tests de mort, lecture du registre des tentatives », qui fait écrire en routine la version de l'orchestrateur, le lanceur et l'additif qui le portent ?
  > **Enjeu.** Ton mot GO-2026-11-20-05 (1a) réserve la version suivante de l'orchestrateur, le lanceur version 11 et leur additif au seul palier 1 de l'héritage, tests de mort sans rien servir ; 2b demande une version de plus pour la lecture du registre. Aucune version prévue ne porte cette course : la version 68 refuse la lecture sans étage et le moteur réel. L'allumage reste soumis au devis et à une ligne d'accord qui nomme ce régime.
  > **Options.** (a) oui, pour ce seul régime, écrit après la version du palier 1 et sur elle, numéros fixés par les mandats : la course peut partir dès ton accord de calcul ; cela prend de la place du modèle F. (b) attendre la lecture du palier 1 de l'héritage : une base éprouvée en réel, mais la course attend un résultat qui ne la concerne pas. (c) trois courses d'une génération par le lanceur en place, le registre porté à la main : rien à écrire, mais le code n'est plus figé (N-044) et il faut trois lignes ; je ne la recommande pas.
  > **Recommandation.** (a), confiance 0,7. **Défaut sous 48 heures.** Aucun pour l'allumage, qui est un nœud ; écrire le code éteint, sans dépense, reste de la routine.

- § 6. Ancien : `puis, si D3 est (a) : mandats de la version 69, du lanceur 11, de l'additif et de la configuration ;`. Nouveau : `puis, si D3 est (a) : mandats de la version de l'orchestrateur et du lanceur du régime de la course (après ceux du palier 1, ton mot 1a), de l'additif et de la configuration ;`.

**C20 — D6, défaut (dépense).**
- Ancien : `**Recommandation.** (a), confiance 0,55. **Défaut sous 48 heures.** (a).`
- Nouveau : `**Recommandation.** (a), confiance 0,55. **Défaut.** Aucun : les juges sont une part de la dépense de D1 et se tranchent avec elle.`

Les recommandations et les confiances de C6 et de C9 (D2, forme (a), 0,55) sont du contre-lecteur, parce que l'option ancienne est tombée. Le rédacteur peut les changer en disant pourquoi. Celle de D3 reste celle du rédacteur.

## 5. Réserves

1. **Le code de l'orchestrateur n'est pas lu**, ni par le rédacteur ni par moi. Ce qui est dit de la version 68 vient du rapport du développeur et de la fiche v7. Les points 5 et 7 du § 2 de l'ordre restent « non vérifiés ».
2. **La répartition des relais par espèce (C17) est une lecture.** Je la tire de l'égalité des dépenses par clé de S2 avec les coûts par rôle de S1, et des parts de S3, § 3. Aucune pièce ne l'écrit telle quelle. Le lanceur de la course la recoupera.
3. **Un écart possible du rédacteur, déclaré par lui.** Deux commandes `find` récursives ont pu traverser un dossier `archives-reponses-modeles/` (rapport du rédacteur, § 7, point 2). Rien n'en a été lu selon lui. C'est un écart possible à un interdit de son mandat, à porter à la mère ; il ne touche pas le contenu des pièces. Le rédacteur n'a lu les contre-lectures de la version 68 et de la fiche v1 que par leur empreinte, quand son mandat les lui donnait à lire (rapport, § 7, point 3) ; il le dit.
4. **La lecture du point 2 de N-045 v2 est défendable, mais elle est une lecture.** Le coût n'est servi à personne, faute de score servi (GO-89), et parce que le code est figé. Le préenregistrement court pourra l'écrire, avec « score net : sans objet ».
5. **Les corrections C1 à C9 suivent un mot de Lazar postérieur aux pièces.** Elles ne disent pas que le rédacteur s'est trompé à 01:01Z ; elles alignent les pièces.

## 6. Refus

Aucun refus d'outil ni de classifieur pendant cette contre-lecture.

— contre-lecteur, modèle O
