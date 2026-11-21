# Décision N-075, version 3 — erratum 3 : les choix de Lazar sur les points 7 à 11 de la section 11, portés dans le texte par le concepteur

- **Ce que c'est.** Un erratum à `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3.md` (`5aed4bab1172b18148c086d90e63611bdd769d9ea7fb4a043e9e9d3178c947b5`), qui n'est pas modifiée (R12). La v3 se lit avec son erratum 1 (`c6efeccfafca415851c0e15ad64305b268c9521f7773e795af28d8d25424b0c1`), son erratum 2 (`b19852b47a90e902ee3fc5c0144ddac00f8665a565b43b1df2debacf58f7bb46`) et celui-ci. **Là où ils diffèrent, cet erratum prime.**
- **Un erratum, non une v4.** Les quatre choix arrêtés retiennent des options déjà écrites et vérifiées dans la v3 : ils changent le statut de vingt passages et n'ajoutent aucun énoncé qui n'y soit, alors qu'une v4 rouvrirait à une vérification entière un texte de 86 000 octets.
- **Le numéro 3.** Le mandat disait « erratum 2 ». Ce nom est pris : la session mère `session_01QPDgKgejkqwnuaJHJ31Ydo` a écrit et scellé un erratum 2 à 15:57 UTC (commit `466e3c815`), en disant qu'elle « consigne et n'arbitre pas », l'auteur de la v3 n'étant pas joignable sur son compte. Je ne l'écrase pas. Cet erratum reprend ses cinq choix sans en changer aucun, dit ce qu'il ne dit pas (passages remplacés, ce qui reste ouvert, ce qui devient un nœud, énoncés tels qu'ils se lisent) et en corrige trois points (section 6).
- **Source.** La ligne `GO-2026-11-21-61` de `registres/go.md` (`65815cfcbd2d0462d544793ee9eda9ee83128b74441ff1aa72980262f3916ce7` à ma lecture ; `c8d88f437cd255757e9a0119f57fa8a766df60080daaf3c913de4b0d08a43de0` au scellement, une ligne ajoutée entre-temps, `GO-2026-11-21-64`, qui ne touche pas ces points), mots de Lazar vers 15:00 UTC dans la session mère, recopiés en section 0.
- **Auteur et heure.** Claude Fable 5.2 (`claude-fable-5-2`), concepteur (R-3735), auteur de la v3 et de son erratum 1, sur mandat de la session mère `session_01Qi7Gr3eYmAhDEJzqLgWcv1` ; 21 novembre 2026, entre 15:58 et 16:13 UTC (`date -u`). Aucun appel payant, ni commit ni poussée. Ni la v3, ni ses errata 1 et 2, ni `CLAUDE.md`, ni le programme, ni les registres ne sont modifiés.
- **Statut.** Pièce décisive : à vérifier une fois, en passe courte, par le contre-lecteur d'un autre modèle (Opus 5.5), avant que la mère ne s'y appuie. Les points à regarder d'abord sont dits au relevé de méthode.
- **Portée.** Aucun critère de porte ne change, aucun énoncé d'hypothèse non plus, aucune dépense n'est ouverte. Une revendication est resserrée par le mot de Lazar (le lemme, point 10). Un énoncé de garantie est resserré (le plancher, point 11). Rien n'est déclaré « libre ».

## 0. Mots de Lazar, verbatim

Ligne `GO-2026-11-21-61`, colonne des mots. Deux phrases touchent les cinq points :

> alors qu'elle se mesure par des dommages plantés. : go

> je penche poiur ca, demande au collisionneur et organisme dans la demande fusionnee

Deux autres touchent ce qui en dépend (section 2) :

> que faire ? demande au collisionneur + protoocle x

> go collisionneur pour avoir une confinace pokus elevee

Lecture de la mère, à la même ligne (extrait) : « N-075 v3, section 11 : point 7 (a) ; point 8 (a) ; point 9, Lazar penche pour (b) (réentraînement permis en service, interdit restreint au banc), à soumettre au collisionneur et à l'organisme dans la question fusionnée ; point 10 (a) ; point 11 (a), q mesuré par dommages plantés, strate non mesurée à zéro. Boucle audit-recapture-réapprentissage contre N-060 v3 point 4 : collisionneur et protocole X. Campagne de dommages plantés par un tiers : collisionneur pour une confiance plus haute. »

L'erratum 2, écrit par la session qui a reçu les mots, en rapporte quatre de plus, que la ligne du registre ne porte pas : « Le contre-lecteur recommande (a), avec une confiance de 0,55. go » (point 7) ; « Fable recommande (a) à 0,8 go » (point 8) ; « (a) Resserrer la revendication au seul reste […] go » (point 10) ; « Fable recommande (a), avec une confiance de 0,75. : go » (point 11). Je les reprends de lui. **Le rattachement de chaque phrase à chaque point est la lecture de la mère, non la mienne.**

## 1. Ce qui est retenu

### Point 7, option (a) : la veille dégelée vit à côté des trois chantiers actifs

La veille, dégelée sans borne de zone (`GO-2026-11-21-51`, point 4), ne compte pas parmi les trois chantiers actifs. Elle vit à côté d'eux, comme la levée partielle de `GO-2026-11-21-50` (D-P4), et sert d'abord les lectures d'antériorité que demandent les décisions. L'inconvénient écrit dans la v3 demeure : c'est une quatrième file de travail de fait. Passages remplacés : R-1 à R-3. `CLAUDE.md` le porte déjà (« Allègement de la procédure », dernière puce, depuis le commit `466e3c815`).

### Point 8, option (a) : la règle à deux clés dans sa forme réécrite

L'énoncé de la section 4 de la v3, écrit « proposé », est **retenu** tel quel :

> **Alerte** : un regard reconnaît un motif **et** une preuve de dommage, rendue par l'oracle, est trouvée au même endroit (même épisode, même artefact). **Motif sans preuve de dommage** : l'épisode monte dans la file d'audit, ou le moniteur s'abstient ; **il n'entre jamais dans les témoins**. Les témoins ne viennent que d'honnêtes exogènes du régime (au banc, le jumeau honnête). **Preuve de dommage sans motif** : elle relève du plancher (point 1) et n'attend aucune seconde clé.

Trois suites.
1. La lettre de `GO-2026-11-21-51`, « nouveauté seule = mise à jour des témoins », n'est plus la règle, et « nouveauté » devient « motif reconnu par un regard ». L'écart à la lettre que la v3 proposait est accordé.
2. Le « tronc commun » de la v3, seul appliqué jusqu'ici, est contenu dans la forme retenue : celle-ci s'applique en entier. Là où la v3 écrit encore « signal » pour la première clé (l. 117), on lit « motif », au sens de sa section 1.
3. Un motif sans preuve de dommage ne déclenche aucune mise à jour des témoins. Refaire les témoins sur des honnêtes exogènes reste une correction de la liste de la section 1 de la v3 ; la règle ne dit pas ce qui la déclenche. C'est ma lecture de l'option (a), à vérifier.

Inchangé : la règle aiguille l'audit et ne donne pas une alerte plus sûre que le plancher ; rien n'est revendiqué ; elle ne s'applique pas au taux de fausses alertes d'une porte ; la file d'audit prioritaire s'ajoute à la part tirée au hasard sans la réduire. L'inconvénient écrit demeure : plus d'audits. Passages remplacés : R-4 à R-10.

### Point 10, option (a) : la revendication du lemme resserrée au seul reste

Le papier A ne revendique du lemme d'additivité que le reste nommé par la lecture des voisins (revendication 5) : **une borne inférieure de la probabilité d'alarme, valide à tout instant, qui ne dépend que du dommage total, hors du cadre gaussien et sous dépendance, avec le coût du report, sur des scores de sondes.** L'énoncé complet et ses conditions sont en section 4.2. Passages remplacés : R-11 à R-13.

Ce que le choix ne fait pas. Il ne déclare pas ce reste libre : il est « non trouvé » par une lecture non contre-lue (R8). Il ne le dit pas démontré : l'inconvénient écrit dans la v3 demeure, la revendication dépend d'une démonstration dans cette forme. Il ne déclenche pas le repli de N-004 (lemme présenté comme corollaire cité), qui reste disponible et reste un nœud.

### Point 11, option (a) : l'identification de l'oracle mesurée, et écrite dans toute garantie

**La probabilité q que l'oracle reconnaisse un dommage qu'il regarde se mesure par des dommages plantés par un tiers, strate par strate (genre et dose), par une borne exacte. Toute garantie porte le minimum de q sur les strates mesurées. Une strate non mesurée compte pour zéro : aucune borne n'y est écrite.** L'énoncé de garantie du plancher, tel qu'il se lit désormais, est en section 4.1. Passages remplacés : R-14 à R-18 ; ajouts : A-1 à A-3.

Deux suites.
1. « Toute garantie » comprend la table du seuil au taux d'audit de N-076 (sa section 7), qui emploie q : elle se lit avec le même q mesuré. N-076 n'est pas modifiée ici ; à porter à sa prochaine version ou par erratum.
2. Tant que rien n'est planté, le plancher ne s'écrit que sous condition : aucune borne chiffrée, au banc comme en service. C'est l'inconvénient écrit de l'option, accepté par le choix.

Ce que le choix ne fait pas : il ne décide pas la campagne de dommages plantés (qui plante, quelles strates, quel cloisonnement, quel prix). Elle reste à part et va au collisionneur (section 2).

## 2. Ce qui reste ouvert

### Le point 9 : l'asymétrie d'apprentissage du programme contre l'invariant de l'oracle

**Non tranché.** Le programme (l. 170) dit : « chaque détection silencieuse devient un exemple étiqueté pour réentraîner les sondes ». N-060 v3 (point 4) pose : « aucune sortie de l'oracle dans la sélection d'un agent ou d'un moniteur ». Lazar **penche pour (b)** : restreindre l'interdit de N-060 v3, point 4, au banc, et permettre le réentraînement en service. Un penchant n'est pas un mot : la question va au collisionneur et à l'organisme, dans la question fusionnée. La recommandation de l'auteur dans la v3 était (a), confiance 0,6 ; elle reste écrite, sans plus de poids.

**D'ici le mot de Lazar**, la règle en vigueur s'applique en entier : N-060 v3, point 4. Aucun texte neuf n'écrit un réapprentissage de sonde sur des verdicts de l'oracle (N-076, § 6.2), et la boucle ne vit que sur mondes plantés (N-076, section 13, point 3). Le texte à part qui écrit la recapture l'écrit comme une quantité rapportée.

Ce que le mot devra fixer si (b) est retenu, d'après les inconvénients déjà écrits : quels épisodes servent au réapprentissage et lesquels jugent le même moniteur, puisque la recapture ne le jugerait plus à l'aveugle ; l'exclusion du mode tenu à l'écart (N-054, N-062) ; l'accès des concepteurs de moniteurs aux verdicts par épisode, que le même point 4 leur ferme ; la précision (i) du point 2 de la section 11, qui interdit tout réglage de moniteur sur les épisodes audités ; et la forme de l'amendement de N-060, décision scellée.

### Ce qui dépend du collisionneur

1. **Le point 9**, ci-dessus : collisionneur et organisme, dans la question fusionnée.
2. **La boucle audit, recapture, réapprentissage contre N-060 v3, point 4** (N-076, § 6.2 et section 13, point 3) : collisionneur et protocole X. C'est le même invariant que le point 9, vu depuis la boucle ; les deux réponses se lisent ensemble.
3. **La campagne de dommages plantés par un tiers** (décision D-3 de la note sur la couverture de l'oracle) : collisionneur, « pour avoir une confiance plus élevée ». Le point 11 (a) fixe comment une garantie s'écrit ; il ne fixe ni le tiers, ni la grille des strates, ni le prix.

### Ce que la ligne du 21 novembre ne touche pas

Les points 1 à 5 de la section 11 de la v3 (le plancher dans la liste des bases de la porte de fin de phase 1 ; la recapture et l'invariant de l'oracle ; « corriger » par l'entraînement de l'agent ; la parenthèse sur les sources ; la référence honnête en service) ne sont pas nommés à `GO-2026-11-21-61`. Ils restent tels que la v3 les laisse. Savoir si un « go recos » plus large les couvre (`GO-2026-11-21-60`, `-63`) revient à la mère : je ne le tranche pas.

## 3. Ce qui devient un nœud

1. **Le point 9 reste un nœud, sans défaut.** L'option (b) modifierait une décision scellée en vigueur : elle demande le mot de Lazar et un texte neuf, contre-lu.
2. **Le lemme.** Trois issues sont des nœuds : la note mathématique ne démontre pas le reste dans cette forme (repli de N-004, ou reste plus étroit) ; une lecture trouve le reste occupé (la contre-lecture de la lecture des voisins, les chapitres 4 à 6 du rapport KfK 3935, le rapport de 1990, l'article de Zerrweck) ; un texte veut remettre dans la revendication ce qui est hors du reste.
3. **Le plancher.** La campagne de dommages plantés est un nœud (dépense et cloisonnement : devis et mot de Lazar), après le collisionneur. Écrire une borne chiffrée demande des strates mesurées ; en ajouter une est une mesure, sur devis. Écrire une borne dans une strate non mesurée n'est pas un nœud : c'est interdit.
4. **La règle à deux clés.** Pas de nœud. La file d'audit prioritaire coûte des audits : sa part se déclare dans le texte qui l'écrit, et toute mesure sur un modèle reste sur devis.
5. **La veille.** Pas de nœud.

## 4. Les énoncés tels qu'ils se lisent désormais

### 4.1 La garantie du plancher d'audit au hasard

Elle est **affirmée** par le programme, jamais **revendiquée** comme un apport : le plancher est publié (Zhu, Zuo, Sun, « Blindfold » ; Gans et Holden ; Podkopaev et Ramdas) et s'écrit comme une base nommée et citée.

> Contre une menace diffuse, la garantie du programme ne repose pas sur la reconnaissance de l'attaque. Elle repose sur un plancher : une part p des épisodes, tirée en secret et indépendamment de tout ce que l'agent observe et de tout score, jugée par un oracle exogène, sous plafond de dommage par épisode. Ce plancher borne le dommage cumulé avant l'alarme pour toute politique d'attaque dont le dommage tombe dans une strate où la reconnaissance de l'oracle est mesurée ; sur un horizon donné et contre un taux de dommage honnête de référence, exogène et valable dans le régime, dès que l'honnête produit aussi ce dommage. La probabilité q que l'oracle reconnaisse un dommage qu'il regarde n'est pas supposée : elle se mesure par des dommages plantés par un tiers, strate par strate (genre et dose), par une borne exacte. Toute garantie porte le minimum de q sur les strates mesurées, et nomme ces strates. **Une strate non mesurée compte pour zéro : aucune borne n'y est écrite.** Les sondes et les moniteurs sont l'accélérateur et l'aiguillage de ce plancher, non sa garantie.

Comment cela se lit.
- *Quand l'honnête ne commet jamais ce dommage* : le saboteur est pris au plus tard à son n-ième épisode endommagé avec probabilité 1 − (1 − p·q)^n, où q est le minimum sur les strates mesurées. Dans une strate non mesurée, q vaut zéro et la formule rend zéro : rien n'est garanti à un saboteur qui peut y placer son dommage.
- *Quand l'honnête le commet aussi* : inchangé (horizon, taux de référence, grille de mises, excès toléré écrits d'avance), avec le même q.
- *« Par une borne exacte »* : je le lis comme la borne inférieure de q dans chaque strate, au niveau de confiance déclaré, puis le minimum sur les strates (note sur la couverture de l'oracle, l. 36 et 129). Zéro manque sur 59 dommages plantés d'une strate laisse un taux de manque de 0,05 au plus, à 95 % (rejoué). Le niveau, et sa répartition entre les strates, s'écrivent dans le texte qui écrit la borne.
- *Aujourd'hui* : à ma connaissance, aucune strate n'est mesurée de cette façon. Les épreuves de l'oracle de N-060 v3 (point 2) sont des épreuves d'admission, non une mesure de q par strate. Aucune borne chiffrée du plancher ne s'écrit donc ; les nombres de la v3 (299, 1 497) restent des illustrations sous supposition.
- *Limites* : celles de la v3, plus une. Rien contre un coup unique ; rien hors de la couverture de l'oracle ; **rien dans une strate non mesurée** ; rien sous l'excès toléré ; rien sans horizon en régime d'excès ; rien sans référence honnête valable ; rien si l'oracle est trompé.

### 4.2 La revendication du lemme d'additivité

C'est la seule revendication que ces choix touchent.

> Le papier A ne revendique du lemme d'additivité que ceci : une borne inférieure de la probabilité d'alarme, valide à tout instant, qui ne dépend que du dommage total, hors du cadre gaussien et sous dépendance, avec le coût du report, sur des scores de sondes internes.

Conditions de lecture.
- *Le libellé* est celui du reste nommé par la lecture des voisins (revendication 5, l. 180 de la pièce `973bd0dd…`), repris au point 10 de la v3. « Dommage total » s'y lit dans le cadre du lemme : le budget total des déplacements du score de sonde, dont le dommage est une fonction croissante (programme, l. 55). Le lemme n'additionne pas le dommage lui-même, et aucun texte n'écrit qu'il porte la borne du plancher (N-076, section 7). C'est ma lecture, à préciser par la note mathématique.
- *Ne se revendiquent plus* : l'invariance à horizon fixe et la séparation avec le maximum (déjà sorties par la v3, citées comme publiées) ; et ce que la liste de `GO-2026-11-21-47` portait sans que le reste le nomme, le prix de la garantie et la détection avant le dommage, qui se mesurent, se rapportent et se citent. L'invariance entre agents ne reste revendiquée que comme partie du reste : la borne ne dépend que du total, donc pas de sa répartition entre agents, sous les conditions que la note mathématique lui met.
- *À établir* : la démonstration du reste dans cette forme, par une version de la note mathématique, contre-lue. Je n'ai pas vérifié ce que sa v3 du 6 octobre en porte déjà.
- *À citer* dans tout texte qui présente le lemme : Avenhaus et Jaech (1981), Zerrweck (1981) d'après le rapport KfK 3365, le rapport KfK 3935, Khosravi et Huo (2610.10597 v1), et les voisins de la section 8 de la v3.

### 4.3 La règle à deux clés

L'énoncé est celui de la section 1, point 8. Rien n'y est revendiqué : c'est une règle d'exploitation.

## 5. Passages remplacés et ajouts

Numéros de ligne de la v3. Chaque texte ancien y figure une seule fois (contrôle par programme) ; celui de R-11 figure une seule fois dans l'erratum 1.

**R-1 (l. 187).** Ancien : « Savoir si la veille dégelée compte parmi les trois chantiers actifs est renvoyé à Lazar (section 11, point 7). » Nouveau : « La veille dégelée vit à côté des trois chantiers actifs, comme la levée partielle de `GO-2026-11-21-50` (D-P4), au service d'abord des lectures d'antériorité que demandent les décisions ; elle ne compte pas parmi les trois (`GO-2026-11-21-61`, point 7 (a)). »

**R-2 (l. 227).** Ancien : « la place de la veille dégelée est en section 11, point 7. » Nouveau : « la veille dégelée vit à côté d'eux (`GO-2026-11-21-61`, point 7 (a)). »

**R-3 (l. 240, texte à reporter au § 16 du programme).** Ancien : « sa place parmi les chantiers suit le mot de Lazar (N-075, section 11, point 7). » Nouveau : « elle vit à côté des trois chantiers actifs, au service d'abord des lectures d'antériorité que demandent les décisions (`GO-2026-11-21-61`). »

**R-4 (l. 31).** Ancien : « **Un écart à la lettre, proposé et non appliqué.** » Nouveau : « **Un écart à la lettre, accordé par Lazar.** »

**R-5 (l. 31).** Ancien : « La lettre change seulement sur le mot de Lazar (section 11, point 8). » Nouveau : « La lettre change : le mot est donné à `GO-2026-11-21-61` (point 8 (a)), et la forme réécrite de la section 4 est retenue. »

**R-6 (l. 112).** Ancien : « **Énoncé proposé, réécrit (en attente du mot de Lazar, section 11, point 8).** » Nouveau : « **Énoncé retenu, réécrit (`GO-2026-11-21-61`, point 8 (a)).** »

**R-7 (l. 114, alinéa entier, de « **Écart à la lettre du mot de Lazar, proposé.** » à « Le reste attend le mot de Lazar. »).** Nouveau : « **Écart à la lettre du mot de Lazar, accordé** (`GO-2026-11-21-61`, point 8 (a)). « Nouveauté seule = mise à jour des témoins » (`GO-2026-11-21-51`) n'est plus la règle, et « nouveauté » devient « motif reconnu par un regard ». La forme réécrite ci-dessus s'applique en entier ; le tronc commun y est contenu. Un motif sans preuve de dommage ne déclenche aucune mise à jour des témoins. Refaire les témoins sur des honnêtes exogènes reste une correction de la liste de la section 1 ; cette règle ne dit pas ce qui la déclenche. »

**R-8 (l. 117).** Ancien : « « audit prioritaire » dans le tronc commun, et ce que le mot de Lazar fixera pour le reste (section 11, point 8). » Nouveau : « « audit prioritaire » : l'épisode monte dans la file d'audit, ou le moniteur s'abstient ; il n'entre jamais dans les témoins (`GO-2026-11-21-61`, point 8 (a)). »

**R-9 (l. 219, « Ne pas écrire »).** Ancien : « « nouveauté seule = mise à jour des témoins » sans dire que les témoins ne se refont que sur des honnêtes exogènes » Nouveau : « « nouveauté seule = mise à jour des témoins » comme règle du programme ; « alerte = nouveauté et preuve de dommage » là où la règle dit « motif et preuve de dommage » »

**R-10 (l. 236, texte à reporter au § 8 du programme).** Ancien : « la règle à deux clés dans la forme que fixera le mot de Lazar (N-075, section 11, point 8), hors du taux de fausses alertes d'une porte » Nouveau : « la règle à deux clés (motif reconnu par un regard et preuve de dommage au même endroit : alerte ; motif seul : audit prioritaire, jamais les témoins ; preuve de dommage sans motif : le plancher), règle d'exploitation qui aiguille l'audit, hors du taux de fausses alertes d'une porte »

**R-11 (l. 184, texte de l'erratum 1, correction C-3).** Ancien : « C'est la lecture de `GO-2026-11-21-47` ; la lecture des voisins la rend partiellement occupée, et seul le reste qu'elle nomme pourrait se revendiquer, dans la forme que fixera le mot de Lazar (section 11, point 10). » Nouveau : « C'était la lecture de `GO-2026-11-21-47`. La lecture des voisins la rend partiellement occupée, et Lazar resserre la revendication au seul reste qu'elle nomme (`GO-2026-11-21-61`, point 10 (a)) : une borne inférieure de la probabilité d'alarme, valide à tout instant, qui ne dépend que du dommage total, hors du cadre gaussien et sous dépendance, avec le coût du report, sur des scores de sondes. Ce qui figure dans la liste ci-dessus sans être dans ce reste (le prix de la garantie, la détection avant le dommage) ne se revendique plus : il se mesure, se rapporte et se cite. »

**R-12 (l. 191).** Ancien : « resserrer la revendication à ce reste, ou replier le lemme, est un nœud (section 11, point 10). » Nouveau : « Lazar resserre la revendication à ce reste (`GO-2026-11-21-61`, point 10 (a)) ; le reste lui-même n'est pas déclaré libre : il est « non trouvé » par une lecture non contre-lue (R8), et sa démonstration dans cette forme reste à établir. Replier le lemme (N-004) reste un nœud. »

**R-13 (l. 234, texte à reporter au § 3 du programme).** Ancien : « Le lemme n'est revendiqué que dans sa lecture valide à tout instant, sur des scores de sondes internes, dans la forme que fixera le mot de Lazar sur le verdict d'antériorité (N-075, section 11, point 10). » Nouveau : « Le lemme n'est revendiqué que dans ce reste : une borne inférieure de la probabilité d'alarme, valide à tout instant, qui ne dépend que du dommage total, hors du cadre gaussien et sous dépendance, avec le coût du report, sur des scores de sondes internes (N-075, `GO-2026-11-21-61`) ; le voisin valide à tout instant le plus proche est cité (Khosravi et Huo, 2610.10597 v1). »

**R-14 (l. 48).** Ancien : « (comment ce q se connaît est une option ouverte, section 11, point 11) » Nouveau : « (q se mesure par des dommages plantés, strate par strate, et une strate non mesurée compte pour zéro : alinéa « Identification de l'oracle, mesurée », ci-dessous) »

**R-15 (l. 45).** Ancien : « oracle exogène au sens de la section 1 ; et, dès que l'honnête » Nouveau : « oracle exogène au sens de la section 1, dont la probabilité q de reconnaître un dommage qu'il regarde est mesurée par des dommages plantés, strate par strate ; et, dès que l'honnête »

**R-16 (l. 59).** Ancien : « rien hors de la couverture de l'oracle ; un saboteur qui reste sous l'excès toléré » Nouveau : « rien hors de la couverture de l'oracle ; rien dans une strate de dommage où q n'est pas mesuré par des dommages plantés ; un saboteur qui reste sous l'excès toléré »

**R-17 (l. 235, texte à reporter au § 4 du programme).** Ancien : « aucune borne contre un coup unique, hors de la couverture de l'oracle, sous l'excès toléré, sans horizon, ni si l'oracle est trompé. » Nouveau : « la borne porte le minimum, sur les strates de dommage mesurées, de la probabilité que l'oracle reconnaisse un dommage qu'il regarde, mesurée par des dommages plantés par un tiers ; aucune borne contre un coup unique, hors de la couverture de l'oracle, dans une strate non mesurée, sous l'excès toléré, sans horizon, ni si l'oracle est trompé. »

**R-18 (l. 252).** Ancien : « **Les points 7 à 11 attendent un choix de Lazar. Ils sont écrits en options ; cette note n'en tranche aucun, et aucun n'a de défaut.** » Nouveau : « **Les points 7, 8, 10 et 11 sont tranchés par Lazar à `GO-2026-11-21-61` : 7 (a), 8 (a), 10 (a), 11 (a). Le point 9 n'est pas tranché : Lazar penche pour (b), et la question va au collisionneur et à l'organisme. Les options restent écrites ci-dessous pour mémoire ; ce qui est retenu se lit dans l'erratum 3.** »

**R-19 (l. 345).** Ancien : « Restent ouverts, en options, sans défaut : les points 7, 8, 9, 10 et 11 de la section 11 » Nouveau : « Reste ouvert, en options, sans défaut : le point 9 de la section 11 ; les points 7, 8, 10 et 11 sont tranchés (`GO-2026-11-21-61`) »

**R-20 (l. 264, et la ligne de l'erratum 1 et de l'erratum 2).** La ligne pour `CLAUDE.md` est remplacée par celle de `docs/decisions/ligne-claude-md-N-075-v1.md` (section 7).

**A-1 (section 1, vocabulaire, ajout).** « **Dommage planté** : un dommage connu, introduit exprès par un tiers dans un produit honnête, pour compter si l'oracle le reconnaît ; qui est ce tiers et ce qu'il voit relève de la campagne, non tranchée. **Strate** : un genre de dommage à une dose donnée. **Strate mesurée** : strate où des dommages plantés ont été jugés par l'oracle et où la borne exacte de q est écrite ; toute autre strate est non mesurée et compte pour zéro. »

**A-2 (section 2, alinéa ajouté après les deux régimes de la « Forme restreinte de la borne », l. 49).** « **Identification de l'oracle, mesurée** (`GO-2026-11-21-61`, point 11 (a)). q n'est pas supposé. Il se mesure par des dommages plantés par un tiers, strate par strate (genre et dose), par une borne exacte. Toute garantie porte le minimum de q sur les strates mesurées, et nomme ces strates. Une strate non mesurée compte pour zéro : aucune borne n'y est écrite. Tant que rien n'est planté, aucune borne chiffrée du plancher ne s'écrit ; les nombres de cette section restent des illustrations sous supposition. »

**A-3 (l. 219, « Ne pas écrire », ajout).** « une borne chiffrée du plancher sans les strates où q est mesuré et sans leur compte de dommages plantés ; une borne dans une strate non mesurée ; un q supposé écrit comme un q mesuré ; « le réapprentissage des sondes en service est permis », tant que le point 9 n'est pas tranché ».

**Lecture d'ensemble.** Partout ailleurs où la v3 et son erratum 1 disent les points 7, 8, 10 et 11 « ouverts », « en options », « proposés » ou « en attente du mot de Lazar » (l. 4, 249, 266, 301, 354, 356, 357, 359 ; erratum 1, « Portée »), on lit : tranchés à `GO-2026-11-21-61`. Les numéros de ligne de la table de la section 14 ne changent pas.

## 6. Ce que cet erratum corrige de l'erratum 2

1. **Le reste du lemme.** L'erratum 2 l'écrit sans « avec le coût du report ». Ces mots sont dans le reste nommé par la lecture des voisins et dans l'option (a) de la v3 (l. 257) : ils sont rendus (section 4.2).
2. **Le point 11.** L'erratum 2 omet « (genre et dose) », « par une borne exacte » et « aucune borne n'y est écrite », et ne dit pas que le choix ne décide pas la campagne : c'est rendu (section 1).
3. **Sa ligne pour `CLAUDE.md`**, inscrite au commit `466e3c815`. Trois défauts : « réentraînement en service ouvert » peut se lire « permis », alors que le point n'est pas tranché et que N-060 v3, point 4, s'applique ; « alerte = signal » garde le mot du tronc commun, quand la forme retenue dit « motif », et perd « jamais les témoins » ; la ligne perd « jamais revendiquée », « hors porte », « non en garantie », « dilemme plutôt que décorrélation » et « pince en trois objets », que portait la ligne de l'erratum 1 et qui viennent de la v3 et de `GO-2026-11-21-46`, `-51` et `-53`.

Le reste de l'erratum 2 est juste et n'est pas repris en défaut : les cinq choix, et « d'ici son mot, la règle en vigueur (N-060 v3, point 4) s'applique ».

## 7. Ligne pour `CLAUDE.md`

Dans un fichier à part, scellé : `docs/decisions/ligne-claude-md-N-075-v1.md`. Elle remplace celle que `CLAUDE.md` porte depuis le commit `466e3c815`. La mère l'inscrit ; je ne modifie pas `CLAUDE.md`.

## 8. Ce que cet erratum ne porte pas

- Les autres décisions de la ligne `GO-2026-11-21-61`. Deux d'entre elles touchent pourtant cette décision et demandent leur propre pièce : « auditer des actes plutôt que des issues : go » (l'unité de l'audit, quand N-075 dit « mesurer l'issue ») ; l'estimation de la part des attaques jamais vues (Li et al.) intégrée au système de contrôle (section 2 de la v3).
- La question fusionnée pour le collisionneur et l'organisme : je ne l'écris pas ici.
- Aucune modification de N-060 v3, de N-076, du programme ni d'un texte scellé.
- Une v4 : à écrire quand le point 9 sera tranché, pour réunir la v3 et ses trois errata en un texte.

## Relevé de méthode

Selon `docs/procedures/consigne-commune-methode-de-recherche-v1.md`.

**Chaîne de raisonnement.**
1. La ligne `GO-2026-11-21-61` est lue en entier (`registres/go.md`, `65815cfc…`) : 7 (a), 8 (a), 9 non tranché avec penchant pour (b), 10 (a), 11 (a).
2. La v3 est lue en entier (empreinte égale au compagnon), avec son erratum 1, sa vérification (`bbee97b1…`) et la contre-lecture de la v1 (`eaec091b…`) ; de N-076 (`49b664c1…`), l'en-tête, les sections 1, 6, 13 et 14, le début de la section 7, et son erratum 1.
3. Chaque option retenue est reprise du texte de l'option dans la v3 (l. 254 à 258) et de l'énoncé qu'elle désigne (l. 112 pour le point 8 ; l. 257 pour le point 10 ; l. 258 pour le point 11).
4. Le reste du lemme est confronté à sa source : lecture des voisins, revendication 5, l. 180 (seul passage que j'en ai ouvert) ; libellés égaux.
5. Le point 11 est confronté à la note sur la couverture de l'oracle (`659f4593…`), l. 36, 90, 129, 143, 160 et 189. Rejoué : `python3 -c "print(0.95**59, 0.95**58)"` rend 0,0485 et 0,0510.
6. Les textes anciens de R-1 à R-19, soit vingt textes (R-7 compté par les deux bornes de son alinéa) : un programme compte chacun une fois dans la v3 (R-11 : une fois dans l'erratum 1, zéro dans la v3).
7. L'erratum 2 n'était pas dans mon premier relevé du dossier (vers 15:58 UTC) ; je l'ai trouvé par la ligne R-4595 du registre des décisions, puis sur disque (16:00 UTC). L'arbre de travail a bougé pendant l'écriture. J'ai relu le registre des accords avant de sceller : une ligne de plus, `GO-2026-11-21-64`, sans effet sur ces points ; la ligne `GO-2026-11-21-61` n'a pas changé (comparaison par `git diff` depuis le début de la session : une insertion, aucune suppression).
8. Supposé : « le prix de la garantie » et « la détection avant le dommage » sont hors du reste, parce que son libellé ne les nomme pas.
9. Supposé : aucune strate n'est mesurée à ce jour par des dommages plantés par un tiers ; je n'ai ouvert aucun résultat.
10. Non vérifié : le rattachement des mots de Lazar aux points, repris de la mère.

**Objets de contrôle.** Le compteur de textes anciens : objet vrai, les vingt textes, attendu une fois chacun, rendu une fois chacun ; objet faux, « point 12 de la section 11 », absent par construction, attendu zéro, rendu zéro. La règle « une strate non mesurée compte pour zéro » : objet où « le plancher garantit » est faux, q = 0, attendu une probabilité de prise nulle après 10 000 épisodes, rendu 0,0 ; objet où c'est vrai, q = 1 et q = 0,2 à 1 % d'audit, attendu 299 et 1 497, rendu 299 et 1 497. Ce sont les contrôles d'un texte, non d'une mesure ; rien n'a été scellé avant.

**Premier pas non justifié.** Le pas 8 : ce qui sort de la revendication du lemme avec le resserrement. Ce qui le justifierait : le mot de Lazar sur cette lecture, ou la lecture des voisins contre-lue. Le deuxième : le libellé du reste vient d'une lecture d'antériorité non contre-lue. Le troisième : le pas 10.

**Mode d'échec affecté.** Sans objet : pièce d'auteur.

**Dérivation de l'énoncé seul.** Sans objet.

**Trouvaille de côté.** (1) La même pièce a été écrite deux fois à quelques minutes d'écart, par la session mère d'un compte, puis sur mandat de celle d'un autre : un relevé du dossier et du registre avant de commander une pièce l'aurait évité. (2) « Auditer des actes plutôt que des issues », accordé à la même ligne, touche le premier levier de N-075 et n'a pas de texte.

**Évaluateur et conseil.** Ce qui juge cette pièce : le contre-lecteur Opus 5.5, puis la mère, puis Lazar pour le point 9. Par où elle pourrait être bien jugée sans le mériter : elle recopie des options déjà vérifiées, ce qui se lit comme sûr, alors que trois phrases sont de moi et non de la v3. Conseil au contre-lecteur, mode « énoncé infidèle » : R-11 et la section 4.2 (ce qui sort de la revendication ; la lecture de « dommage total ») ; R-7 (ce qui déclenche la mise à jour des témoins) ; la section 4.1 (« borne exacte » lue comme borne inférieure de q, minimum sur les strates).

## Ce que je n'ai pas fait

- Aucun PDF ouvert, aucun préenregistrement, aucun résultat, aucun dossier ni fichier interdit par le mandat. N-060 v3 n'est ouverte qu'à ses lignes 25 à 34 ; la note mathématique v3, par recherche de mots ; la lecture des voisins, à sa revendication 5.
- Je n'ai pas vérifié qu'aucun texte en cours n'écrit déjà un réapprentissage de sonde sur des verdicts de l'oracle.
- `CLAUDE.md`, le programme, les registres, la v3 et ses errata 1 et 2 ne sont pas modifiés. Ni commit ni poussée.
