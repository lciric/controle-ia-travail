# Vérification adverse de l'addendum 7 du témoin de Bailey — v5 (vérification de la correction « règle mécanique »)

Workflow `verification-correction-addendum-7-bailey`, run `wf_ca11fb6e-43c`, deux relecteurs neufs, sur
`prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md` au commit `68c3edc1` (différence
`9c3613d6..68c3edc1`). Retours consignés tels quels depuis le journal du run ; numéros de ligne : ceux du commit `68c3edc1`.

## Angle « règle mécanique » — bloquant : oui

Il reste un bloquant. La règle mécanique ferme bien le bloquant du rapport v4 : après la clôture, aucune décision ne dépend plus du classement de la cause (« pièce » ou « code »). Aucune session ne lit de note ni ne joue de code avant que chaque verdict attendu soit scellé ou son absence constatée, et toute lecture ultérieure est « exploratoire, non retenue ». La même voie se rouvre pourtant chez le lecteur : entre ses deux exécutions, rien ne lui interdit d'ouvrir les notes de son dossier, de corriger le code ou l'environnement, puis de rendre la seconde exécution qui aboutit. Les règles du dépôt classent même le code en « routine », et un sous-agent qui rencontre une erreur cherche d'abord à la corriger. On aurait donc une correction retenue, décidée après une lecture, sans addendum ni contre-lecture (R2).

Déroulé des cas : refus à 36 tours → pas de verdict ; la confirmation est retenue si K′ ≥ 71, sinon aucun verdict n'est retenu pour l'étape 1. Refus à la confirmation → le verdict à 36 tours est retenu. Les deux refusés → aucun verdict retenu ; c'est cohérent avec la puce « Rapport » et le § 5 (f). Erreur passagère → le rapport de la seconde exécution est retenu, ce qui n'est légitime que si rien n'a changé entre les deux exécutions (le code est déterministe).

Cohérence : la puce « Après le lancement du premier lecteur » et la condition 7 tiennent. La voie « assemblage refusé avant la clôture » ne lit aucun résultat, mais quatre points y manquent : délai, place dans la clôture et dans l'ordre du § 6, second lecteur sans dossier, phrase « Aucune décision ne dépend d'un diagnostic » contredite. Trois autres points à corriger : la cloison interdit à la lettre l'assemblage et la vérification des empreintes ; « verdict rendu » est ambigu pour un lecteur remplacé, et le chemin du rapport entre en collision ; une mention « refus ou erreur » non conforme n'a pas de règle.

Cloisons tenues : aucun fichier sous runs/ ouvert, valider et lire non appelés, rien modifié. Copie de travail numérotée, hors dépôt : /tmp/claude-0/-home-user-controle-ia-travail/2cfa1854-671e-5aa7-83ff-79ac90ee7d37/scratchpad/a7.txt

### 1. bloquant — § 3, l. 184-186 (puce « Refus ou erreur à la lecture ») ; avec l. 168-170 (cloisons des lecteurs) et l. 173-176

**Constat.** Avec la règle mécanique, la seule voie qui sauve un run après un premier échec est « la seconde exécution aboutit ». Or « à l'identique » ne vise que la commande consignée. Rien n'interdit au lecteur, entre ses deux exécutions, d'ouvrir les pièces de son propre dossier (ses cloisons ne visent que l'autre verdict), de modifier le code de lecture, le dossier ou l'environnement, ni de jouer d'autre code que la commande consignée. Les consignes du dépôt rangent d'ailleurs le code dans la « routine ». Comme valider et lire sont déterministes (même dossier, même graine), une seconde exécution qui aboutit après un refus suppose presque toujours un changement. Ce serait une correction retenue, décidée par le lecteur après avoir vu les notes, sans addendum ni contre-lecture (R2). C'est exactement la voie que la règle prétend fermer (« sans correction »), et elle peut changer le verdict retenu (verdict au lieu de « pas de verdict », ou une autre valeur si le code touché calcule).

**Correction proposée.** Remplacer « qui rejoue la commande consignée une seconde fois à l'identique avant de rien rendre ; » (l. 185-186) par « qui ne joue que la commande consignée et la rejoue une seconde fois à l'identique avant de rien rendre, sans rien modifier entre les deux exécutions (code, dossier, commande, environnement), ni ouvrir aucune pièce du dossier, ni modifier aucun fichier du dépôt hors son rapport ; son rapport donne les empreintes de l'arbre du code et du dossier à chaque exécution, et une seconde exécution faite après un changement est un refus ; »

### 2. à corriger — § 3, l. 141-142 (cas (i)), l. 153-154 (« dès le constat »), l. 163-165 (second lecteur), l. 189 et l. 191-194 ; § 6, l. 287 ; « Contre-lecture », l. 353-354

**Constat.** La voie « refus de l'assemblage » se décide avant la clôture, sans aucune note lue, donc hors du critère central. Mais elle est mal raccordée, sur quatre points. (a) Elle repose sur un diagnostic (« s'il tient au code d'assemblage »), ce que contredit à la lettre « Aucune décision ne dépend donc d'un diagnostic » (l. 189), et ce diagnostic n'a pas de borne. (b) L'addendum de correction n'a pas de délai. Il ne figure ni parmi les suites qui retardent la note de clôture (l. 150-152), ni dans l'en-tête du § 6. Le cas (i) se constate dès que les journaux sont transférés et scellés, donc avant l'assemblage, et la note est écrite « dès le constat » : la clôture peut tomber avant l'assemblage qu'elle doit nommer. Et rien ne dit qui décide d'attendre la correction ou de clore. (c) Si l'assemblage reste refusé, la puce « Les deux verdicts » lance quand même le second lecteur (« journaux transférés et scellés »), alors qu'aucun dossier n'est nommé. (d) La section « Contre-lecture » affirme que l'en-tête du § 6 n'a pas à changer, alors que cette étape se place avant la clôture et ne relève ni du § 2.1 ni du § 2.3.

**Correction proposée.** l. 189 : remplacer « Aucune décision ne dépend donc d'un diagnostic. » par « Aucune décision prise après la clôture ne dépend donc d'un diagnostic. » — l. 192-194 : remplacer « s'il tient au code d'assemblage, ce code peut être corrigé avant la clôture par un addendum neuf, contre-lu (R2), comme à l'addendum 6, § 5 (d) (« avant toute lecture ») ; sinon ce run n'a pas de verdict, et la note de clôture le dit. » par « le diagnostic se borne au message du code, aux noms, tailles et empreintes des pièces et aux champs techniques (comme l. 370 du texte), et toute correction ne s'essaie que sur des dossiers factices ; s'il tient au code d'assemblage, ce code peut être corrigé par un addendum neuf, contre-lu (R2), comme à l'addendum 6, § 5 (d) (« avant toute lecture »), scellé au plus tard 72 h après le constat du refus, et la note de clôture attend ce scellement et l'assemblage neuf, ou ce délai ; sinon, ou sans addendum scellé dans ce délai, ce run n'a pas de verdict, la note de clôture le dit et aucun lecteur n'est lancé pour lui. » — l. 287 : remplacer « Ordre, sans autre étape que les suites permises avant la clôture (§ 2.1, § 2.3) : » par « Ordre, sans autre étape que les suites permises avant la clôture (§ 2.1, § 2.3 ; § 3 : assemblage refusé) : » — l. 353-354 : remplacer « L'en-tête « Ordre, sans autre étape… » du § 6 reste tel quel : la règle mécanique n'ajoute aucune étape après la clôture. » par « L'en-tête « Ordre, sans autre étape… » du § 6 nomme l'assemblage refusé, seule étape ajoutée, avant la clôture ; la règle mécanique n'ajoute aucune étape après elle. »

### 3. à corriger — § 3, l. 175-176

**Constat.** « ni ne joue `valider`, `lire` ou un autre code sur un dossier réel : seuls les lecteurs le font » vaut « jusqu'à ce que chaque verdict attendu soit scellé », donc aussi avant la clôture. Prise à la lettre, la phrase interdit à la session l'assemblage d'une relance passée par le chemin de l'addendum 5 (l. 156, l. 191-194), la reprise de la lecture 38 et même la vérification des empreintes de la routine de reprise (`verifier-arbre .`). Elle se heurte ainsi à la voie de l'assemblage que la même puce ouvre, et chaque session du chantier l'enfreindrait en commençant.

**Correction proposée.** Remplacer « ni ne joue `valider`, `lire` ou un autre code sur un dossier réel : seuls les lecteurs le font. » par « ni ne joue `valider`, `lire` ou un autre code qui lit ou rend une note sur un dossier réel (la vérification des empreintes, la conduite, la reprise de la lecture 38 et l'assemblage fait avant la clôture exceptés, qui ne rendent aucune note) : seuls les lecteurs le font. »

### 4. à corriger — § 3, l. 170 (chemin du rapport), l. 179-181 (lecteur remplacé) et l. 194-195 (« Dès qu'un verdict a été rendu »)

**Constat.** Deux trous dans le remplacement. (a) Le remplaçant travaille « sur la même consigne », donc avec le même chemin de rapport (l. 170). Si le premier lecteur a scellé un rapport avant de s'arrêter, le remplaçant tombe sur un fichier existant : il doit l'écraser (contraire à R12), échouer (ce qui, par la règle mécanique, vaut « pas de verdict »), ou l'ouvrir. (b) « Un rapport que le premier aurait scellé n'est pas retenu » se heurte à « Dès qu'un verdict a été rendu pour un run, aucune relecture de ce run n'est retenue », car un rapport scellé peut se lire comme un « verdict rendu ». Si les deux rapports diffèrent (le remplaçant a reçu un refus, le premier avait un verdict), le choix de la règle qui prime ne se ferait qu'une fois les rapports ouverts : une décision prise après une lecture.

**Correction proposée.** Remplacer « remplacé par un lecteur neuf, sur la même consigne, qui fait alors foi, même lancé après que l'autre a rendu ; un rapport que le premier aurait scellé n'est pas retenu ; c'est rapporté. » par « remplacé par un lecteur neuf, sur la même consigne (chemin de rapport neuf, R12), qui fait alors foi, même lancé après que l'autre a rendu ; un rapport que le premier aurait scellé n'est pas retenu et n'est pas un verdict rendu au sens de la puce « Refus ou erreur à la lecture » (« rendu » : empreinte rendue à la session) ; c'est rapporté. »

### 5. à corriger — § 3, l. 171-173 et l. 179-181

**Constat.** Le remplacement ne vise que l'exécution « sans empreinte ni mention ». Rien n'est écrit pour une mention « refus ou erreur » non conforme : le lecteur dit n'avoir joué qu'une fois, ou rend une mention sans le message prévu. La session devrait alors choisir entre accepter la mention (pas de verdict) et lancer un remplaçant (verdict possible). Ce choix change le verdict retenu et n'a pas de règle. Il se fait sans note lue, sauf si un verdict a été appris par erreur, cas où seule une réserve s'applique. Mieux vaut le rendre mécanique.

**Correction proposée.** Après « un rapport que le premier aurait scellé n'est pas retenu » (et son complément du constat précédent), insérer « ; une mention « refus ou erreur » rendue vaut constat de la seconde exécution, quelle qu'en soit la forme, même si le lecteur dit ne pas avoir rejoué, et n'ouvre aucun remplacement ».

### 6. remarque — § 3, l. 154-158 (commande nommée à la clôture) ; § 5 (f), l. 263-266

**Constat.** Avec la règle mécanique, une faute dans la commande consignée (chemin, argument, PYTHONPATH) fait perdre le verdict du run, sans recours. Or cette commande, écrite dans la note de clôture, n'a jamais été jouée (cloison). Le prix est déclaré au § 5 (f), mais on peut le réduire sans aucune lecture : jouer cette commande sur un dossier factice. Le texte ne l'interdit pas, puisque la cloison ne vise que les dossiers réels.

**Correction proposée.** Après « et la commande ; ils ne changent plus. » (l. 158), ajouter « Avant la note de clôture, la commande est jouée telle quelle sur un dossier factice de même forme (essais du § 4), sans aucun dossier réel ; son résultat est cité dans la note. »

## Angle « application des constats du rapport v4 » — bloquant : non

Scellable après quatre corrections courtes. Rien n'est bloquant. Le critère central tient : avec la règle mécanique (un refus ou une erreur rejoués par le lecteur donnent « pas de verdict », sans nœud, sans correction ni nouvelle lecture retenue), aucune décision qui change le verdict retenu ne dépend plus d'une note ou d'un verdict lus après la clôture. La seule décision qui reste après la clôture est le remplacement d'un lecteur, qui est imposé, et dont le code est déterministe.

Ce qui a été vérifié par programme, sur le texte normalisé du commit 68c3edc1 :
- chacun des 15 textes insérés y figure une seule fois ;
- aucun ancien texte retiré ne subsiste (« nœud, tranché », « 72 h », « lecteur neuf, qui fait foi », « ou que la suite », « n'est pas une relecture », « @@ ») ;
- la phrase « Repris des deux passes… » est identique à celle du commit 11954d70 ;
- aucune phrase n'est cassée ;
- l'empreinte du rapport v4 (16e008d2adbd1babe312122be65da2588a5e9f6eaafe6049e2f2da07d33f37ce) est celle du compagnon .sha256, du fichier sur disque et du fichier au commit 68c3edc1.

Renvois vérifiés justes :
- texte, l. 231, 241-242, 268-270, 329-338, 332, 338, 340, 363, 365 et 371 ;
- addendum 5, § 4 (conduite et poste neufs, mot de Lazar) ;
- addendum 6, § 5 (d) : la citation « avant toute lecture » est exacte, mais voir le constat 2.

Sort des 20 constats du rapport v4 :

Angle « phase de lecture » :
- 1 : premier remplacement appliqué, mais « un code corrigé » est devenu « un autre code », ce qui crée une contradiction (constat 1 ci-dessous) ; second remplacement retiré, et c'est dit.
- 2 : retiré, c'est dit ; son objet est repris par « quelle qu'en soit la cause ».
- 3 : appliqué en partie. Le lecteur rejoue lui-même ; la seconde exécution qui aboutit est traitée ; la mention « valeur de note vue » est retirée et c'est dit. « Constat daté du retour du lecteur » est retiré sans que ce soit dit (sans objet, faute de délai).
- 4 : appliqué, mais « et c'est un nœud » est retiré alors que la section le dit repris « tel quel ».
- 5 : première insertion mot pour mot ; la seconde est adaptée (liste réduite au remplacement d'un lecteur), alors que la section la dit reprise « telle quelle ».
- 6, 7 et 9 : appliqués mot pour mot.
- 8 : retiré, c'est dit.
- 10 : le (a) est appliqué mot pour mot. Le (b) est appliqué et élargi : un assemblage refusé devient corrigeable par addendum. Cet élargissement est une matière nouvelle, présentée comme reprise « telle quelle » (constat 2).

Angle « application » :
- 1 à 4 : retirés, c'est dit.
- 5 : non appliqué, raison donnée. Elle est exacte pour l'après-clôture mais oublie la correction d'assemblage, ajoutée avant la clôture et absente des § 2.1 et 2.3 (constat 4).
- 6 (a) : la parenthèse est retirée au lieu d'être remplacée, alors que la section la range parmi les reprises « telles quelles ».
- 6 (b) : retiré, c'est dit ; son objet est atteint par la formule du constat 1 du premier angle.
- 7, 9 et 10 : appliqués mot pour mot ; pour le 10, liste et phrase rétablie.
- 8 : la première partie est sans objet (la phrase a disparu) ; la seconde est appliquée en substance au § 5 (f). Le point n'est nommé nulle part dans la section.

La section « Contre-lecture » est donc exacte sur ce qui est retiré, mais « Repris tels quels » est inexact pour quatre éléments, et « Aucun autre constat écarté » laisse le point 8 de l'angle « application » sans trace (constat 5).

Cloisons tenues : aucun fichier sous runs/ ouvert, valider et lire non appelés, ni registres/etat.md ni les dossiers interdits ouverts, aucune commande réseau, aucun fichier du dépôt créé ni modifié. Les copies de travail sont hors dépôt, dans /tmp/claude-0/-home-user-controle-ia-travail/2cfa1854-671e-5aa7-83ff-79ac90ee7d37/scratchpad/.

### 1. à corriger — § 3, l. 175-176

**Constat.** « ni ne joue `valider`, `lire` ou un autre code sur un dossier réel : seuls les lecteurs le font » interdit, à la lettre et jusqu'au scellement des verdicts, tout code que la session joue sur un dossier réel. Or le texte en demande plusieurs avant la clôture : la conduite, le scellement des journaux exigé par le cas (i) de la clôture (l. 141), l'assemblage d'une relance par le chemin de l'addendum 5 (l. 156, 192) et la vérification d'arbre de la routine de reprise. Le relecteur v4 avait écrit « un code corrigé » ; l'élargissement à « un autre code » rend le § 3 contradictoire avec lui-même et rend la clôture (i) irréalisable à la lettre. Ce qu'il faut interdire, c'est un code qui lit une note.

**Correction proposée.** Remplacer « ni ne joue `valider`, `lire` ou un autre code sur un dossier réel : seuls les lecteurs le font. » par « ni ne joue sur un dossier réel `valider`, `lire`, un code de lecture corrigé ou tout autre code qui lit une note : seuls les lecteurs le font (la conduite, l'assemblage d'une relance avant la clôture et les contrôles d'empreinte et de scellement, qui ne lisent aucune note, ne sont pas visés). »

### 2. à corriger — § 3, l. 153-154 et l. 191-194

**Constat.** La correction d'un assemblage refusé avant la clôture est une matière nouvelle (elle vient du point 10 (b), « phase de lecture », qui ne demandait que de trancher ce refus avant la clôture). Trois manques, sans résultat connu (rien n'est lu avant la clôture), mais qui décident si la relance a un verdict. (a) Fenêtre : hors des suites laissées à Lazar, la note de clôture « est écrite dès le constat » du cas (i), journaux transférés et scellés, et « après la clôture, rien n'est ajouté ». Rien n'ouvre donc de fenêtre à l'assemblage, ni à un addendum de correction et sa contre-lecture. (b) Aucune borne de durée, et rien sur un second refus après correction : à la lettre, la clôture peut être repoussée sans fin. (c) « Comme à l'addendum 6, § 5 (d) » est inexact. Ce § 5 (d) prévoit la correction d'un défaut que révèle l'essai sur processeur, et dit « Reprise impossible ou assemblage refusé : pas de verdict, nœud » ; l'addendum 5, § 5 (d), dit de même « s'il refuse, le verdict n'est pas prononcé : nœud ». Permettre d'avance la correction d'un refus réel est un écart à ces deux textes, à nommer comme tel. Le classement « tient au code d'assemblage » ou « sinon » reste un diagnostic, mais il se fait avant toute lecture : il est admissible, à condition d'être borné.

**Correction proposée.** (1) Remplacer « dans les autres cas, elle est écrite dès le constat. » par « dans les autres cas, elle est écrite dès le constat (s'il y a eu relance par le chemin de l'addendum 5 : après l'assemblage, ou, s'il est refusé, après l'assemblage refait par le code corrigé ou le constat que ce run n'a pas de verdict). » (2) Remplacer « s'il tient au code d'assemblage, ce code peut être corrigé avant la clôture par un addendum neuf, contre-lu (R2), comme à l'addendum 6, § 5 (d) (« avant toute lecture ») ; sinon ce run n'a pas de verdict, et la note de clôture le dit. » par « s'il tient au code d'assemblage, ce code peut être corrigé avant la clôture par un addendum neuf, contre-lu (R2) et scellé au plus tard 72 h après le refus (écart aux addenda 5 et 6, § 5 (d), qui en font un nœud ; correction « avant toute lecture », comme au § 5 (d) de l'addendum 6) ; sinon, ou si l'assemblage refait refuse encore, ce run n'a pas de verdict, et la note de clôture le dit. » La borne de 72 h est au choix de l'auteur, mais une borne doit être écrite avant le scellement.

### 3. à corriger — § 1, l. 34-35

**Constat.** La réserve « décidée après une lecture » énumère les décisions qu'elle couvre : « (fin, seconde tentative, relance, reprise, mot, crédit) ». La correction d'un assemblage refusé (§ 3, l. 191-194) décide si la relance a un verdict, donc si la confirmation est retenue à K′ ≥ 71. Elle n'y figure pas, pas plus que la mise en place refaite. Si une note est lue avant la clôture, sur ordre ou par faute, cette décision pourrait être prise résultat connu sans porter la réserve. C'est la seule voie, après correction, où une décision qui change le verdict retenu pourrait suivre une lecture sans trace.

**Correction proposée.** Remplacer « (fin, seconde tentative, relance, reprise, mot, crédit) » par « (fin, seconde tentative, relance, reprise, mise en place refaite, correction d'un assemblage refusé, mot, crédit) ».

### 4. à corriger — § 6, l. 287 ; Contre-lecture, l. 353-354

**Constat.** Le point 5 de l'angle « application » est écarté au motif que « la règle mécanique n'ajoute aucune étape après la clôture ». Ce motif vaut pour l'après-clôture. Mais l'en-tête « sans autre étape que les suites permises avant la clôture (§ 2.1, § 2.3) » exclut aussi, à la lettre, l'addendum de correction d'un assemblage refusé : c'est une suite avant la clôture, introduite au § 3, qui n'est ni au § 2.1 ni au § 2.3. L'en-tête et le § 3 se contredisent, et la raison donnée dans la section est incomplète.

**Correction proposée.** Remplacer « Ordre, sans autre étape que les suites permises avant la clôture (§ 2.1, § 2.3) : » par « Ordre, sans autre étape que les suites permises avant la clôture (§ 2.1, § 2.3 et, au § 3, la correction d'un assemblage refusé) : ». Remplacer « L'en-tête « Ordre, sans autre étape… » du § 6 reste tel quel : la règle mécanique n'ajoute aucune étape après la clôture. » par « L'en-tête « Ordre, sans autre étape… » du § 6 ne reçoit pas le texte proposé (la règle mécanique n'ajoute aucune étape après la clôture) ; il nomme la correction d'un assemblage refusé, seule suite ajoutée avant la clôture. »

### 5. remarque — Contre-lecture, l. 349-353

**Constat.** Traçabilité. « Repris tels quels » est inexact pour quatre éléments : (a) « verdict appris par erreur » : la liste des décisions est réduite au remplacement d'un lecteur ; (b) « run à 36 tours sans verdict » : « et c'est un nœud », du point 4 de l'angle « phase de lecture », est retiré. Le retrait est sain pour le critère central (pas de nœud tranché avec les deux issues connues), mais il n'est pas dit ; (c) « assemblage refusé tranché avant la clôture » : élargi en une correction par addendum (constat 2) ; (d) « parenthèse… retirée » : le point 6 (a) de l'angle « application » proposait un texte de remplacement, pas un retrait. Restent sans trace le point 8 de l'angle « application » (renvoi aux deux § 5 (d) retiré avec la dichotomie, conséquence au § 5 (f) appliquée en substance) et, au point 3 de l'angle « phase de lecture », la date du constat (sans objet, faute de délai). « Aucun autre constat écarté » reste exact une fois ces adaptations écrites.

**Correction proposée.** Remplacer « Repris tels quels : chemin du rapport fixé par la consigne ; verdict appris par erreur ; run à 36 tours sans verdict (aucun verdict retenu pour l'étape 1, fixé maintenant) ; message du code ; lecteur remplacé ; cas (iii) après l'arrêt et le transfert ; cas (ii) ou (iii) ; assemblage refusé tranché avant la clôture ; mise en place refaite au même poste de dépense ; membre de phrase de la condition 7 rétabli ; parenthèse sur la lecture qui suit un refus retirée ; traçabilité de cette section. » par « Repris tels quels : chemin du rapport fixé par la consigne ; message du code ; lecteur remplacé ; cas (iii) après l'arrêt et le transfert ; cas (ii) ou (iii) ; mise en place refaite au même poste de dépense ; membre de phrase de la condition 7 rétabli ; traçabilité de cette section. Repris avec adaptation à la règle mécanique : verdict appris par erreur (seul le remplacement d'un lecteur reste une décision) ; run à 36 tours sans verdict (aucun verdict retenu pour l'étape 1, fixé maintenant, sans nœud) ; assemblage refusé tranché avant la clôture, et corrigeable par addendum avant elle (écart aux addenda 5 et 6, § 5 (d)) ; parenthèse sur la lecture qui suit un refus retirée plutôt que remplacée (angle « application », point 6 (a)) ; renvoi aux deux § 5 (d) retiré avec la dichotomie, conséquence portée au § 5 (f) (angle « application », point 8) ; date du constat sans objet, aucun délai ne restant (angle « phase de lecture », point 3). » Si le constat 1 ci-dessus est appliqué, ajouter : « « un code corrigé » élargi à « tout autre code qui lit une note » (angle « phase de lecture », point 1). »

### 6. remarque — § 6, l. 300-301

**Constat.** « le verdict retenu est celui à 36 tours (§ 3) » ne reprend pas la règle nouvelle du § 3 (l. 204-205) : si ce run est lui-même sans verdict, aucun verdict n'est retenu pour l'étape 1. Le renvoi au § 3 sauve le sens, mais c'est la seule phrase du texte qui l'énonce sans réserve.

**Correction proposée.** Remplacer « et le verdict retenu est celui à 36 tours (§ 3). » par « et le verdict retenu est celui à 36 tours s'il en a un ; sinon aucun verdict n'est retenu pour l'étape 1 (§ 3). »
