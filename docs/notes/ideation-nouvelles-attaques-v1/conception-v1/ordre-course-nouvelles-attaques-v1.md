# Ordre de course — organisme d'idéation, « nouvelles attaques », trois générations — v1

- Auteur : rédacteur neuf, modèle F. Écrit le 2026-11-20 ; relevé de `date -u` : 01:01:43Z, après la lecture des pièces et avant l'écriture.
- Statut : **pièce de travail, non contre-lue.** Elle propose ; la mère la soumet. Processeur seul : aucun appel, aucune dépense, aucun lancement de l'organisme ni de l'orchestrateur.
- Mandat et complément : voir la question (`question-course-nouvelles-attaques-v1.md`, même dossier). Le complément prime : la course sert le bras d'attaque et vise des menaces inédites (`GO-2026-11-19-96`).
- Je n'ai pas lu le code de l'orchestrateur. Tout ce que je dis de la version 68 vient de son rapport de développeur (`docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/rapport-developpeur-orchestrateur-v68-v1.md`, `ad42b7229a8e37aae823b1041a3acf1db91ee4053f5fec61136b6fd178b59aa6`), de sa contre-lecture (`contre-lecture-orchestrateur-v68-v1.md`, `d2cfeac1a8d96a732c2cd9341aecc96a12778fff9b20ccfa0fef1edb2d47e325`) et de la fiche des quatre décisions, version 7 (`fiche-quatre-decisions-orchestrateur-v68-v7.md`, `5ddfae1887c14a950b1f05d274364930aeb50c216540ce881797f0acdb3f6bac`, contrôlée « Conforme », `522a3c46aa588b72cae3ff723451166337f2181c7600560e40af686a12725a09`), qui attend ton mot.

## 0. Verdict

1. **Aucune version existante de l'orchestrateur ne peut porter cette course en réel.** La version 68 sait jouer plusieurs générations sous un plafond de course, mais en moteur simulé seulement : elle refuse le moteur réel par construction. La course demande une version suivante (69), un lanceur neuf (11), un additif scellé et une configuration propre. C'est du travail sur processeur, sans dépense (§ 2).
2. **La course ne joue aucun test de mort** : une fiche est une idée, non une loi sur des données. Elle n'a donc besoin ni de l'interrupteur des tests de mort, ni de la machine jetable. Des quatre décisions de la fiche de la version 68, seule la deuxième la touche : ce qui est servi à la génération suivante (§ 5).
3. **Ce qui passe d'une génération à l'autre est ton nœud.** Je recommande un registre de toutes les fiches passées par le portier, sans verdict ni tri ; sans ton mot, rien n'est servi (§ 5).
4. **Rien n'est décidé par un juge.** Ce qui tranche, dans cette course, est l'épreuve des témoins plantés ; ce qui tranche une idée est une épreuve du bras, hors de cette course (§ 7, § 10).

## 1. Ce que la course est, et ce qu'elle n'est pas

Elle est une course de l'atelier d'idées (N-065, rôle 2, `docs/decisions/decision-N-065-v1.md`, `f820e90da0920d505d22bc7b33fad4906181d43bd5af7e79418a3c161a8a65c4`) : l'organisme reçoit la question scellée et rend des fiches d'idées. Elle sert le bras d'attaque : ses fiches disent contre quoi éprouver les moniteurs.

Elle n'est pas une course du bras. Aucune fiche n'est jouée contre un moniteur. Aucune fiche n'est une preuve. Aucune dépense ne part avant le devis contre-lu et ton accord de calcul (`GO-2026-11-19-94`).

## 2. La version de l'orchestrateur qui porte la course

**Ce qui existe.** La version 68 est contre-lue « Conforme ». Elle joue N générations, tient un plafond de dépense sur la course entière en réservant le plafond de chaque génération avant de la jouer, et écrit sur la ligne de chaque génération ce qu'elle a lu de la précédente. Son lanceur refuse le moteur réel dans tous les régimes, éteint compris, et n'épingle aucun additif (rapport du développeur, § 4, § 8 et § 9). Le lanceur de course en place (version 10) ne joue qu'une génération.

**Le régime dont la course a besoin** est celui que la version 68 appelle « éteint, sans étage » : trois générations, aucun étage de tests de mort, montant requis égal à trois fois le plafond d'une génération (rapport du développeur, § 5). Dans ce régime la version 68 ne sert rien ; seule la mémoire qui évite les redites passe, et elle n'est jamais montrée aux proposeurs.

**Ce qui manque, en code, pour qu'une course réelle parte** (à écrire par un développeur, sur mandat ; je ne l'écris pas) :

| n° | ce qui manque | d'où je le tiens |
|---|---|---|
| 1 | une version 69 qui lève le refus du moteur réel pour **ce seul régime**, nommé, et qui épingle l'additif | rapport du développeur, § 4 et § 9, point 3 ; fiche v7, « Ce qui manque encore » |
| 2 | un lanceur de course version 11 : épingle la version 69 ; bornes des relais, parts au pire et crédits comptés pour trois générations ; plafond du premier relais porté au montant requis ; ligne d'accord vérifiée au montant exact | rapport du développeur, § 9, point 2 |
| 3 | un additif scellé : le régime, ce qui est servi et à qui, le titre de la section servie, la règle quand il n'y a rien à servir | rapport du développeur, § 9, point 3 |
| 4 | une configuration de course propre : champs de fiche de la question, valeurs fermées des trois axes, refus d'un champ « comment faire » | question, § 5 ; fiche v7, verdict, point 4 (« elle fixera ses propres champs de fiche ») |
| 5 | le tirage des cases par génération : graine dérivée de celle de la course (règle R9), sans remise d'une génération à l'autre, famille tenue à l'écart exclue, garde de disjonction | N-049 ; **non vérifié** : j'ignore si l'orchestrateur sait servir des cases différentes à chaque génération |
| 6 | si tu retiens le registre servi (§ 5, option H1) : un lecteur du registre des fiches passées. La version 68 ne lit que la sélection scellée d'un étage de tests de mort, et il n'y en a pas ici | rapport du développeur, § 3, point 1 ; fiche v7, décision 2, option (b) : « il faudrait une version de plus » |
| 7 | le coût par espèce et par rôle écrit génération par génération au journal de la course | N-045 v2, point 2 ; **non vérifié** : le manifeste de fin de la course v9 le porte pour une génération |
| 8 | la garde « part de fiches au coffre » entre deux générations (§ 11) | proposition du rédacteur |

**Ce qui ne manque pas.** La machine jetable et l'essai du bac à sable réel : aucun script écrit par un modèle n'est exécuté. Le remplacement du mot « survit » demandé par ta décision R-3209, point 3 : il vise la sélection des tests de mort, que cette course ne joue pas.

**Ce que cela coûte en conception.** Zéro dollar d'appels d'interface ; du temps de sessions. Ordre de grandeur, d'après la version 68 (huit fichiers neufs écrits et essayés en une session de développeur, puis une contre-lecture) : quatre mandats et leurs quatre contre-lectures — la version 69 ; le lanceur 11 ; l'additif avec la configuration ; les témoins plantés, que la mère écrit. S'y ajoutent un essai à blanc de bout en bout en moteur simulé, et la mesure des consignes sans appel. Le point 6 ajoute un fichier et ses essais à la version 69. Ces sessions consomment la place du modèle F, déjà interrompue une fois par sa limite d'usage (note d'interruption, même dossier que la fiche, `c773d268…`, citée par la fiche v7).

**Les trois générations ne se jouent pas comme trois courses d'une génération.** Le lanceur 10 le permettrait, mais ce qui passerait d'une course à l'autre serait porté à la main : le code ne serait plus figé (N-044), et chaque course demanderait sa ligne.

## 3. Le déroulé

**Avant tout appel payant** (aucune dépense) : question contre-lue et scellée ; additif, configuration, version 69 et lanceur 11 contre-lus ; préenregistrement court scellé et contre-lu (§ 12) ; tirage des cases scellé ; témoins plantés écrits par la mère et scellés ; pièces servies attestées « aucune recette » par la mère ; essai à blanc de bout en bout en moteur simulé ; mesure des consignes sans appel.

**Deux lignes à part, avant la course** : la sonde de refus (chaque espèce reçoit la question ; une espèce qui refuse est retirée de tous les rôles, sans reformulation) ; l'épreuve réelle des témoins plantés (un témoin manqué : aucune course, aucune retouche sans version neuve et mot de la mère).

**Chaque génération** : proposition (chaque espèce reçoit chaque case de la génération) ; aiguillage par le portier (une fiche trop concrète va au coffre, comptée, jamais relue) ; juges croisés, pour information (§ 7) ; écriture de la ligne de la génération (cases servies, fiches rendues, fiches au coffre en compte, coût par espèce et par rôle, ce qui a été lu de la génération précédente) ; garde de budget de la course ; garde du coffre (§ 11).

**Après la troisième génération** : relecture « aucune recette » de toutes les fiches validées par la mère (R-607), attestée et scellée ; lecture d'antériorité (§ 9) ; lecture des mesures du § 6 ; puis le chemin du § 10. Les réponses brutes sont conservées (règle de Lazar R-3661, citée par le devis v2i).

## 4. Tâches fraîches à chaque génération (N-049)

N-049 (`docs/decisions/decision-N-049-v1.md`, `8a5bf5e57e2bb447467388acb572e032d1a6a578a868db1b7304263a1c9d4460`) veut qu'un organisme ne puisse s'adapter qu'à la famille, plus aux textes. Ici la tâche est la case.

- **Vivier** : les 120 cases de la question (§ 5 de la question).
- **Famille tenue à l'écart** : toutes les cases d'une valeur de l'axe « ce que le moniteur suppose », tirée par graine avant la course, soit 20 cases. Une famille entière, non des cases éparses : sinon ce qu'on appellerait généralisation ne serait qu'une interpolation (question du coffre v2, point 3). Elle n'est jamais servie dans cette course ; son identité est scellée. Son usage ultérieur est ta décision.
- **Tirage** : onze cases par génération, comme à la course v9, tirées sans remise parmi les 100 restantes, par une graine propre à chaque génération, dérivée de celle de la course (règle R9). Trente-trois cases servies ; soixante-sept restent en réserve.
- **Pièces servies** : la question scellée ; une pièce d'antériorité attestée « aucune recette » par la mère (la synthèse `rapports/fille-ideation-1-v1/synthese-anteriorite-pilier-attaque-v2b.md`, `b828d800913c8960d04b6822de8f10fc51ee573c660c84f6658ea6ba68796b8d`, ou une version neuve). Je n'ai lu de cette synthèse que son existence et son empreinte.

## 5. Ce qui passe d'une génération à l'autre

**Ce qui est déjà tranché.** Rien du juge n'est servi aux proposeurs : ni note, ni rang, ni sélection faite par un juge (`GO-2026-11-19-89`). Ce n'est pas une option.

**Ce qui reste ouvert**, et qui est ton nœud (ce qui est servi à un agent) :

- **H0 — rien n'est servi.** Seule la mémoire qui évite les redites passe, jamais montrée. Avantage : aucun code de lecture neuf ; aucun écart à aucune garde. Inconvénient : la génération 2 ne voit rien de la génération 1. Les trois générations sont alors trois tirages sur des cases différentes, dédoublonnés ; l'héritage se réduit à ne pas redire.
- **H1 — un registre sans verdict ni tri.** La génération suivante reçoit, pour **toutes** les fiches des générations passées que le portier a laissées passer, leurs trois champs fermés, leur nom et leur énoncé ramené à une ligne. Aucune note, aucun rang, aucune étiquette d'antériorité ; ordre tiré par graine ; taille bornée en octets, gelée à l'additif ; chaque ligne passée à la garde des étiquettes interdites ; aucune fiche du coffre. Le champ `filiation` d'une fiche nomme la fiche du registre dont elle part, ou « aucune ». Avantage : les proposeurs peuvent partir d'une idée passée ou s'en écarter ; l'usage de l'héritage laisse une trace comptable. C'est un registre des tentatives, non une archive de découvertes, comme la fiche v7 le rapporte de l'héritage ; et la seconde passe des courses d'idéation servait déjà aux proposeurs les fiches de la première (`rapports/fille-ideation-1-v1/devis-course-ideation-pilier-attaque-v2-v1.md`, `531849e3e4f55de3ae5f097033fdcb50bd209ac88670547b3060fb869b10eea3`, § 1). Inconvénient : du code neuf (§ 2, point 6) ; des consignes plus longues ; et servir toutes les fiches, c'est aussi servir les moins bonnes.

**Recommandation** : H1, confiance 0,6. Ce qui me ferait changer : que tu veuilles d'abord un mot unique pour tout l'organisme sur ce qui est servi (décision 2 de la fiche v7) ; ou que la mesure des consignes montre que le registre ne tient pas dans la borne.

**Défaut** : aucun. Sans ton mot, H0 : rien n'est servi.

## 6. Héritage récompensé, composition, coût dans le signal — comment la course les tient, code figé

N-044 (`docs/decisions/decision-N-044-v1.md`, `2b70bdac014d366d058a530680d016663b35ed73b8ca0cae9f2369206f5004bf`) sépare trois régimes de budget : conception, usage, re-conception. **Cette course est en régime d'usage** : le code et la composition sont figés avant le premier appel. Rien, dans la course, n'apprend ni ne se réécrit. Je dis donc pour chaque énoncé de N-045 v2 (`docs/decisions/decision-N-045-v2.md`, `c7b05e39de381cee1d5ec2276745a0310bd3cc0857a6be0e0fb14eeb5042261d`) ce qu'il devient ici, sans le gonfler.

- **L'héritage d'une génération est récompensé (point 5).** Les trois générations forment un seul épisode, K = 3, gelé. Le mérite de la génération 1 se lit sur ce que les générations 2 et 3 en font. Aucune décision ne se prend sur la génération 1 seule, hors les gardes d'arrêt. Mesures écrites d'avance, toutes calculées par programme sur des champs fermés, sans juge : part des fiches des générations 2 et 3 dont la `filiation` n'est pas « aucune » ; taux de redite d'une génération à l'autre (même classe, même case) ; nombre de classes distinctes couvertes ; part de fiches au coffre, en compte. Ce sont des **descriptions**. La course n'a pas de bras témoin : elle ne dit pas si hériter vaut mieux que trois tirages indépendants à coût égal. Cette comparaison est l'objet du plan de l'héritage, non de cette course ; un bras témoin doublerait la dépense (devis, § 8).
- **À qui va le signal.** À la conception suivante de l'organisme, par la lecture de l'épisode entier, que tu décides. Rien ne revient aux proposeurs pendant la course.
- **La composition est une variable apprise (point 1).** Dans la course, elle est figée. Ce qui s'apprend se lit après : fiches et coût par espèce et par rôle, génération par génération. Le choix de la composition se juge sur l'oracle du monde planté et le coût (N-058) ; l'oracle par espèce n'existe pas encore (devis de l'héritage v5, § 6). Je ne recommande donc aucune réduction sur preuve ; les compositions à trois et à deux espèces sont chiffrées au devis pour que tu puisses en décider.
- **Le coût entre dans le signal (point 2).** Le coût de chaque génération, par espèce et par rôle, est écrit au journal de la course et rapporté à côté des mesures. Il n'est pas servi aux proposeurs : code figé, ils n'ont rien à réallouer ; et tout ce qui est servi à un agent est ton nœud. La forme d'un score net n'est pas gelée ici : aucun critère de cette course n'en dépend.
- **La nécessité de la frontière est une sortie (point 3).** Rapportée : part du coût et des fiches par espèce.

## 7. Ce qui tranche

N-058 (`docs/decisions/decision-N-058-v1.md`, `854f2724864f1e45394e001f4aca7b0248753e5d2b0a66991e2ee8a7be87de9d`) : la composition se juge sur l'oracle du monde planté et le coût, jamais sur le verdict d'un juge.

- **L'oracle de cette course est l'épreuve des témoins plantés.** La mère écrit des témoins dont la bonne issue est connue d'avance : des fiches qui redisent une idée déjà publiée et vérifiée au dépôt (elles doivent être reconnues comme non inédites) ; des fiches hors périmètre (elles doivent être écartées) ; des fiches à la forme interdite, par exemple un champ « comment faire » rempli d'un texte inerte (le portier doit les envoyer au coffre). **Aucun témoin ne contient un procédé réel.** Un témoin manqué arrête la course avant qu'elle parte.
- **Les juges ne tranchent rien.** Leur classement n'est servi à personne ; il n'entre dans aucun critère, dans aucun choix d'espèce, dans aucun passage vers le bras. Il sert à deux choses : lire les témoins plantés, et donner à la mère un ordre de lecture.
- **Une idée n'est tranchée que hors de cette course**, par une épreuve du bras sur monde planté, sous préenregistrement (§ 10).

## 8. Code et régimes de budget figés après la conception (N-044)

- Après le scellement du préenregistrement court, plus rien ne change : version de l'orchestrateur, lanceur, additif, configuration, composition, tirage des cases, plafonds. Tout changement est une version neuve et une course neuve (règle R12).
- Régime d'usage : un plafond d'arrêt par génération, un plafond de course égal à trois fois ce plafond, réservé génération par génération ; la course s'arrête plutôt que de dépasser, même si la dépense réelle aurait tenu (rapport du développeur, § 8). Aucune réserve de re-conception n'est ouverte dans cette course.

## 9. Règle d'antériorité, écrite d'avance

**Ce qui est comparé.** L'idée d'une fiche : sa classe (les trois champs fermés) et son énoncé. La nouveauté se juge par classe de mécanisme, non par la surface du texte.

**Qui est lu.** Tous les témoins plantés, et les fiches que la mère retient après la relecture « aucune recette ». Les autres fiches sont « non lues ».

**Contre quelles sources**, dans cet ordre : (1) les questions v1 et v2 du pilier attaque et la question du coffre v2 ; (2) les synthèses d'antériorité déjà versées, dont `rapports/fille-ideation-1-v1/synthese-anteriorite-pilier-attaque-v2b.md` ; (3) le coffre, par un lecteur isolé qui ne rend qu'un oui ou un non par classe ; (4) l'état de l'art du dépôt et ses lectures sur PDF ; (5) la littérature, à un périmètre de recherche (bases, période, classes de requête) écrit et scellé **avant** toute lecture de fiche.

**Par qui.** Un lecteur neuf, qui n'a pas écrit la fiche ; jamais l'organisme qui l'a produite ; d'une autre famille que le proposeur si possible. Il ne voit ni le rang des juges, ni l'espèce du proposeur. Toute fiche qu'il dit sans antériorité passe à un second lecteur, d'une autre lignée, qui cherche à lui en trouver une.

**Les quatre étiquettes, et ce qu'on a le droit de dire.**

| étiquette | condition | ce qu'on dit |
|---|---|---|
| antériorité trouvée | une source nommée ; pour la littérature, lue sur PDF empreinté, page citée (règle R7) | « déjà décrite », avec la source |
| antériorité partielle | une source couvre une partie des champs | ce qui est couvert, ce qui ne l'est pas ; pas « inédite » |
| non tranchée | désaccord des deux lecteurs ; source non vérifiable sur PDF ; recherche inachevée | **la fiche n'est pas dite inédite** |
| aucune antériorité trouvée | les deux lecteurs, aux cinq sources, n'en trouvent pas | « inédite au périmètre vérifié le [date] », avec le périmètre |

**Symétrie** (règles R3 et R4). Le même effort de recherche pour toute fiche lue ; le périmètre ne s'élargit ni ne se resserre au vu d'un résultat. Une part de fiches « inédites » suspecte de propreté, très haute ou nulle, déclenche le même audit. Un lecteur qui manque un témoin d'antériorité planté voit toutes ses étiquettes annulées.

**Portée de l'étiquette.** Elle ordonne le travail du bras. Ce n'est pas une revendication du programme : toute phrase publique sur la nouveauté d'une menace reste ton nœud, après vérification (règles R7 et R8).

## 10. Le chemin d'une fiche validée vers le bras d'attaque

| étape | ce qui se passe | qui décide |
|---|---|---|
| 1 | pendant la course, le portier scelle au coffre toute fiche qui glisse vers le concret ; seuls des comptes sortent | le portier, par construction |
| 2 | relecture « aucune recette » de toutes les fiches validées (R-607), attestée et scellée ; ce qui glisse va au coffre | la mère |
| 3 | lecture d'antériorité (§ 9) | les lecteurs neufs ; la mère consigne |
| 4 | la mère te propose une liste de cartes : classe, énoncé, étiquette, rien d'autre | **toi** |
| 5 | les cartes retenues passent au bras par la mère. La session de l'attaquant informé ne lit jamais les sorties brutes de l'organisme | la mère transmet ce que tu as retenu |
| 6 | dans le bras : rien ne se construit ni ne se joue hors de ses trois scellements (règle scellée qui fait foi, familles aveugles, moniteurs gelés), de la revue de sécurité externe (R-611), d'un préenregistrement contre-lu et d'un accord sur devis | **toi** |
| 7 | rien ne revient à l'organisme : aucun score d'un moniteur du programme n'entre dans sa sélection ni dans ses consignes (N-053, point 5) | invariant |

**Aucune fiche n'entre dans une course du bras sans les étapes 1 à 6.**

**Une conséquence à connaître.** La mère conçoit les moniteurs, et elle lit toutes les fiches. Une carte qu'elle a lue est donc, pour la défense, un mode **vu** : elle ne peut pas fonder le mode tenu à l'écart (N-054), qui reste conçu par une instance qui n'a vu aucun moniteur. Je l'écris comme règle de la course : **aucune carte de cette course ne nourrit le mode tenu à l'écart.** Si tu veux qu'une part des fiches reste inconnue de la défense, il faut qu'un lecteur isolé, hors de la défense, fasse pour cette part la relecture « aucune recette » ; ce serait un écart à la lettre de `GO-2026-11-19-94` (« relecture […] par la mère »), donc ton mot.

## 11. Liste d'arrêt et gardes

Chaque garde s'éprouve sur un cas sain et sur un artefact avant la course (règle R5) ; aucun repli silencieux.

- Refus d'un classifieur de sûreté : le tour s'arrête, consigné tel quel, non relancé ; reformulation plus étroite sur ton mot seulement (R-609).
- Espèce qui refuse à la sonde : retirée de tous les rôles.
- Témoin planté manqué à l'épreuve : aucune course.
- Plafond d'une génération ou de la course atteint : arrêt avant le poste.
- **Garde du coffre** : si plus d'un quart des fiches d'une génération vont au coffre, la génération suivante ne part pas ; la question dérive vers le concret et se reformule. Le seuil est une proposition du rédacteur, à geler.
- Consigne plus longue que la borne mesurée : départ refusé.
- Clé dont le reste ne couvre pas sa part au pire : départ refusé (règle du lanceur, devis, § 6).

## 12. Ce qui se scelle avant la course

Un préenregistrement court (règle R1), contre-lu par un sous-agent neuf à qui l'on donne les fichiers à lire (règle R2) : la question scellée ; K = 3 ; la composition ; le tirage des cases et la famille tenue à l'écart ; ce qui est servi (H0 ou H1) ; les mesures du § 6, dites descriptives ; la règle d'antériorité et son périmètre de recherche ; les gardes du § 11 ; les plafonds. Il écrit au même rang « l'héritage ne laisse aucune trace » et son contraire, « aucune fiche n'est inédite » et son contraire (règle R3). Cette course ne passe aucune porte du programme : aucun verdict de porte n'est prononcé.

## 13. Réserves

1. Je n'ai pas lu le code. Les points 5 et 7 du § 2 sont à vérifier par le développeur avant d'écrire la version 69.
2. Les valeurs des trois axes viennent de pièces du dépôt, mais leur croisement est de moi. La mère peut les resserrer avant le scellement.
3. Onze cases par génération, vingt cases tenues à l'écart, le quart du coffre : valeurs du rédacteur, à geler à l'additif.
4. La lecture d'antériorité à deux lecteurs, sur PDF, est lourde. Elle ne porte que sur les fiches que la mère retient ; le devis ne la chiffre pas en dollars (§ 7 du devis).
5. La fiche v7 attend ton mot. Si tu tranches sa décision 2 pour tout l'organisme, le § 5 s'y aligne.
