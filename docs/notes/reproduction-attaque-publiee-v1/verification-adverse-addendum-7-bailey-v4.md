# Vérification adverse de l'addendum 7 du témoin de Bailey — v4 (dernière vérification, différentielle)

Workflow `derniere-verification-addendum-7-bailey`, run `wf_3362de6e-1d2`, deux relecteurs neufs (ni auteurs de l'addendum
ni de ses corrections), sur `prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md` au commit `9c3613d6`.
Retours consignés tels quels depuis le journal du run (champ `result` de chaque relecteur) ; numéros de ligne : ceux du commit
`9c3613d6`. Cloisons tenues selon les deux relecteurs : aucune note ni journal technique ouvert, `valider` et `lire` non appelés.

## Angle « phase de lecture, cas par cas » — bloquant : oui

Ne pas sceller en l'état : un bloquant, cinq points à corriger, quatre remarques, tous dans la phase de lecture après la clôture. Fichier relu : /home/user/controle-ia-travail/prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md au commit 9c3613d6 ; les numéros de ligne sont ceux de ce commit, et chaque texte à remplacer y figure une seule fois.

**Le bloquant.** Après la clôture, la session peut lire les notes et jouer `valider` ou `lire` elle-même. Seuls les « rapports » et les « verdicts » lui sont fermés, et le texte (l. 241-242, 371) rouvre les notes dès la clôture. Devant un refus ou une erreur, elle connaîtrait donc le résultat avant de classer le nœud et de sceller, ou non, la correction sous 72 h : deux décisions qui changent le verdict retenu. Deux remplacements courts ferment la voie.

**Déroulé du § 3, cas par cas.**
- (1) 72 tours finis : règle claire. Clôture du cas (i), deux lecteurs lancés ensemble, verdict de la confirmation retenu si K′ ≥ 71.
- (2) Tronquée après une reprise : claire. La note de clôture nomme le dossier de reprise ; K′ ≤ 70 donne le verdict à 36 tours.
- (3) Non courue : claire, un seul lecteur. Rien n'est écrit si le run à 36 tours est lui-même sans verdict.
- (4) « Refus ou erreur » : c'est là que la règle manque. Outre le bloquant, quatre trous : qui rejoue la commande ; une erreur de la commande ou de son environnement ; le dossier assemblé, à la fois « pièce » et « assemblage » ; « ils ne changent plus » contre le nom neuf qu'impose R12.
- (5) Lecteur arrêté sans rien rendre : claire, aucune décision n'y connaît un résultat ; trois détails de forme.
- (6) Fin par Lazar pendant le run principal : la note est écrite « dès le constat », donc avant le transfert des journaux qu'elle doit nommer. Ordre à corriger, sans effet sur le verdict retenu tant que K′ ≤ 70.

**Messages du code.** Vérifiés à la lecture du code, sans rien exécuter : aucun message de `GardeArret` de `valider`, de `lire` ou de l'assemblage ne porte une valeur de note. Ils portent des noms de fichiers, de champs et de gardes. Seule voie étroite : une exception autre que `GardeArret` qui citerait un champ mal formé.

**Renvois et phrases.** Renvois du § 3 vérifiés justes : l. 231, 241-242, 268-270, 329-338, 340, 363, 365 et 371 du texte ; addendum 5, § 4 et § 5 (d) ; addendum 6, § 5 (d). Aucune phrase cassée.

**Cloisons.** Tenues : aucun journal de notes ni journal technique ouvert, `valider` et `lire` non appelés, aucune commande réseau, aucun fichier du dépôt créé ni modifié. Copie de travail hors dépôt : /tmp/claude-0/-home-user-controle-ia-travail/2cfa1854-671e-5aa7-83ff-79ac90ee7d37/scratchpad/addendum7-9c36.md. À signaler : la recherche des `raise` dans analyse_v3.py a affiché en contexte une ligne de constantes de la mention « trop beau » de l'audit (critère du texte, aucune valeur mesurée).

**Code lu.**
- /home/user/controle-ia-travail/src/controle_ia/temoin_bailey/lecture_v8.py (entier)
- /home/user/controle-ia-travail/src/controle_ia/temoin_bailey/lanceur_v21.py (l. 1-300 et 2600-2797)
- /home/user/controle-ia-travail/src/controle_ia/temoin_bailey/analyse_v3.py (lignes `raise`, `validite`, `graines`)
- /home/user/controle-ia-travail/src/controle_ia/scellement.py (lignes `raise`)

### 1. bloquant — § 3, l. 169-170 et l. 174-176 ; à rapprocher des l. 131-134 et 185-186 ; texte, l. 241-242 et 371

**Constat.** Après la clôture, rien n'interdit à la session de lire les notes ni de jouer le code elle-même. La première puce n'interdit les notes qu'« avant la clôture », et le texte (l. 241-242, 371) permet ensuite de les ouvrir. Les deux seules bornes écrites visent les « rapports » et les « verdicts » (l. 169-170, 185-186). Le cas « refus ou erreur » y pousse : les messages de `GardeArret` ne portent que des noms (constat 7). Pour dire si un refus de `lire` « tient à la pièce lue » ou « à un défaut du code », il faut donc regarder le journal des notes. De plus, la formule passive « constatés sur la commande consignée rejouée une seconde fois » laisse la session rejouer `valider` et `lire`, puis essayer la correction, sur le dossier réel. La session connaîtrait alors le résultat du run avant deux décisions qui changent le verdict retenu : le classement du nœud (« pas de verdict », ou correction) et le scellement de l'addendum dans les 72 h, ou son abandon. « Sans ouvrir aucun rapport » ne ferme donc pas la voie ; c'est le reste du texte de remplacement de la passe finale, pas un point déjà tranché. En passant : « la suite d'un refus ou d'une erreur soit close » (l. 170) et « chaque verdict attendu soit scellé, ou son absence constatée » (l. 186) ne disent pas la même chose, et « chaque lecteur lancé ait scellé le sien » ne peut pas se réaliser pour un lecteur remplacé.

**Correction proposée.** Remplacer « La session n'ouvre aucun rapport avant que chaque lecteur lancé ait scellé le sien, ou que la suite d'un refus ou d'une erreur soit close. » par « Jusqu'à ce que chaque verdict attendu soit scellé, ou son absence constatée, aucune session n'ouvre un rapport, ne lit une note de sonde ou de juge du témoin (au sens de la première puce ; les l. 241-242 et 371 du texte ne jouent qu'ensuite), ni ne joue `valider`, `lire` ou un code corrigé sur un dossier réel : seuls les lecteurs le font. » Remplacer « nœud, tranché sans ouvrir aucun rapport. » par « nœud, tranché sans ouvrir aucun rapport ni lire aucune note, sur le seul message du code, les noms, tailles et empreintes des fichiers et les champs techniques (un contrôle de forme par programme, qui ne rend aucune valeur de note, est permis) ; la correction ne s'essaie que sur des dossiers factices. »

### 2. à corriger — § 3, l. 152-155 et l. 176-179 ; § 5 (f), l. 251-252

**Constat.** L'alternative « pièce lue » ou « défaut du code ou de l'assemblage » laisse trois cas sans case. Aucun ne dépend d'un résultat, mais chacun décide si le run a un verdict, et tous sont probables à la première exécution réelle (§ 5 (f)). (a) Une erreur de la commande consignée ou de son environnement (module introuvable, chemin, mise en forme de la sortie). Aucun script de lecture n'existe sous `scripts/` ni à la racine de `runs/temoin-bailey-v1-20261111/` : la commande naîtra dans la note de clôture. Elle n'est ni « la pièce lue » ni « le code ou l'assemblage » ; à la lettre, elle finit en « pas de verdict » à 72 h. (b) Pour le run à 36 tours, la pièce lue est elle-même le produit de l'assemblage (`lecture-assemblee-v1`, `lanceur_v21.py` l. 2672-2752). Un manque dans ce dossier se range aussi bien sous « pièce non conforme » (pas de verdict) que sous « défaut de l'assemblage » (correction). (c) « Ils ne changent plus » (dossier et commande) contredit la correction : R12 impose un nom neuf au code corrigé, donc une commande neuve, et un défaut d'assemblage impose un dossier assemblé neuf.

**Correction proposée.** Remplacer « Ou bien le refus tient à la pièce lue (absente, altérée ou non conforme) » par « Ou bien le refus tient à la pièce lue (absente, altérée ou non conforme dans les transferts scellés d'origine) ». Remplacer « Ou bien il tient à un défaut du code ou de l'assemblage : » par « Ou bien il tient à un défaut du code, de l'assemblage (dossier assemblé compris), de la commande consignée ou de son environnement d'exécution : ». Remplacer « et la commande ; ils ne changent plus. » par « et la commande ; ils ne changent plus, sauf par l'addendum de correction de la puce « Refus ou erreur » (code, commande ou dossier assemblé de nom neuf, R12). »

### 3. à corriger — § 3, l. 168-169, 174-175, 179 et 181-182

**Constat.** Trois faits dont dépend la règle « refus ou erreur » ne sont attribués à personne. (a) Qui rejoue la commande « une seconde fois à l'identique » : le lecteur avant de rendre sa mention, ou la session ? (b) Rien n'est écrit si la seconde exécution aboutit (erreur passagère) : verdict du lecteur, ou refus ? (c) « Sans qu'aucune valeur de note ait été rendue » et « si une valeur de note a été rendue avant le refus » décident entre correction et « pas de verdict ». Seul le lecteur le sait, et il ne rend que la mention et le message du code. Le délai de 72 h court d'un « constat » sans heure tant qu'on ne sait pas qui constate. Avec `lire` tel qu'il est écrit (un seul retour, `lecture_v8.py` l. 769-772), aucune valeur ne sort avant une exception ; la règle doit quand même dire qui le déclare.

**Correction proposée.** Remplacer « constatés sur la commande consignée rejouée une seconde fois à l'identique, sans qu'aucune valeur de note ait été rendue : » par « constatés par le lecteur lui-même sur la commande consignée, qu'il rejoue une seconde fois à l'identique avant de rien rendre (si la seconde exécution aboutit, il en fait son rapport et y dit le premier échec), sans qu'aucune valeur de note lui ait été rendue ; le constat est daté du retour du lecteur : ». Remplacer « ou la mention « refus ou erreur » avec le message du code, sans aucune valeur. » par « ou la mention « refus ou erreur » avec le message du code et la mention « valeur de note vue : oui » ou « non », sans aucune valeur. »

### 4. à corriger — § 3, l. 190-193 ; § 6, l. 285-286

**Constat.** « Dans tous les autres cas […] le verdict retenu est celui à 36 tours » ne dit rien du cas où le run à 36 tours est lui-même sans verdict : refus tenant à la pièce, addendum non scellé sous 72 h, ou état « pas de verdict » rendu par `valider`. Le § 5 (f) déclare ce risque. Si la confirmation a alors un verdict au régime réduit (20 ≤ K′ ≤ 70), la lettre donne « aucun verdict retenu ». La formule publique « sur K tours » laisserait pourtant plaider pour celui de la confirmation, et ce débat aurait lieu les deux issues connues.

**Correction proposée.** Remplacer « le verdict retenu est celui à 36 tours ; la confirmation est rapportée » par « le verdict retenu est celui à 36 tours ; si ce run est lui-même sans verdict, aucun verdict n'est retenu pour l'étape 1, quel que soit celui de la confirmation, et c'est un nœud ; la confirmation est rapportée ». Si l'auteur préfère retenir alors le verdict de la confirmation au régime réduit, il l'écrit à la place ; l'une des deux règles doit être fixée avant le scellement.

### 5. à corriger — § 1, l. 33-36 ; § 3, l. 165-170

**Constat.** La réserve « décidée après une lecture » du § 1 ne vaut que pour une lecture faite « avant la clôture ». Après la clôture, rien n'est écrit si la session apprend un verdict avant que le sort de l'autre soit fixé. Trois façons probables : un lecteur qui met le verdict dans son message de retour au lieu de la seule empreinte (défaut courant d'un sous-agent), un rapport ouvert par erreur, un nom de fichier de rapport parlant choisi par le lecteur. Le nœud d'un refus, la correction ou le remplacement d'un lecteur seraient alors décidés verdict connu, sans trace.

**Correction proposée.** Après « (cloisons écrites dans sa consigne). » insérer « Le chemin du rapport est fixé par la consigne. » Après la phrase « La session n'ouvre aucun rapport […] » (ou son remplacement du constat 1), insérer « Si une session apprend malgré cela un verdict ou une valeur de note avant ce moment (message d'un lecteur, fichier ouvert), c'est consigné avec ce qui a été vu ; toute décision prise ensuite sur l'autre lecture (nœud, correction, remplacement) est rapportée « décidée après une lecture », et le verdict retenu porte cette réserve. »

### 6. à corriger — § 3, l. 147-152 et l. 160-162

**Constat.** Fin par Lazar pendant le run principal (cas (iii)) : l'ordre écrit ne tient pas. Le cas (iii) n'est pas de ceux qui attendent un mot : la note de clôture est donc écrite « dès le constat », avant l'arrêt de l'instance et le transfert des journaux. Or elle doit nommer le dossier donné au lecteur (sortie de la conduite, ou dossier de reprise si le transfert passe par une reprise). De plus, « après la clôture, rien n'est ajouté », et le second lecteur n'est lancé que si les journaux sont « transférés et scellés ». À la lettre, soit le run arrêté par Lazar n'est jamais lisible, soit le dossier nommé est faux. Sans effet sur le verdict retenu tant que K′ ≤ 70 ; cela change ce qui est lu et rapporté, et le départ des 24 h.

**Correction proposée.** Remplacer « (iii) Lazar y met fin ; c'est rapporté comme sa décision, avec la réserve du § 1 si une lecture a précédé. » par « (iii) Lazar y met fin ; c'est rapporté comme sa décision, avec la réserve du § 1 si une lecture a précédé ; si un run est en cours, la note de clôture n'est écrite qu'après son arrêt, le transfert et le scellement de ses journaux (reprise de la lecture 38 comprise), ou le constat de leur perte. »

### 7. remarque — § 3, l. 168-169 ; `lecture_v8.py`, `analyse_v3.py`, `scellement.py`, `lanceur_v21.py` l. 2672-2752

**Constat.** Vérifié dans le code, sans rien exécuter : aucun message de `GardeArret` levé par `valider`, `lire` ou `assembler_lecture` ne porte une valeur de note, un rappel, un taux du juge ni un compte de tours gagnés. Ils portent : un nom ou un chemin de fichier (`lecture_v8.py` l. 144, 157, 169, 177) ; un nom de champ (l. 274, 292) ; un texte fixe (l. 475, 517, 526, 546, 607, 639, 750) ; un nom de grandeur, de clé ou de garde et la constante 200 (`analyse_v3.py` l. 66, 69, 127, 135, 156, 184-186, 240-247) ; un chemin et douze caractères d'empreinte (`scellement.py` l. 81-87). `valider` ne lit aucune note. Les gardes rejouées par l'audit sont rattrapées (`lecture_v8.py` l. 718-719) et finissent dans le rapport, pas dans un refus. Aucune exception n'est conditionnée par le signe du résultat. Le message n'apprend que l'étape atteinte : un refus de `lire` suppose que `valider` a rendu un état nul, donc K′ ≥ 20 et gardes passées, des faits techniques. Reste une voie étroite hors `GardeArret` : une conversion comme `float(ev["note_juge"])` (l. 603) sur un champ mal formé donne une erreur dont le texte cite le contenu du champ.

**Correction proposée.** Facultatif. Dans la phrase « la mention « refus ou erreur » avec le message du code, sans aucune valeur », après « le message du code » insérer « (texte de la `GardeArret` ; pour toute autre exception, son type et la ligne du code, sans le contenu qu'elle cite) ».

### 8. remarque — § 3, l. 165-167 et l. 179-181

**Constat.** « Aucun des deux lecteurs » ne vise à la lettre que les deux premiers. Le lecteur neuf qui suit une correction est lancé quand le rapport de l'autre run est déjà scellé dans le dépôt, et il n'est pas dit sous les mêmes cloisons. Le lecteur remplacé l'est (« sur la même consigne ») ; le contre-lecteur de l'addendum de correction ne l'est pas non plus. Par ailleurs rien ne dit ce que vaut un nouveau refus de ce lecteur neuf : à la lettre la règle rejoue (nouveau nœud, nouveau délai), sans borne. La lecture étant mécanique, l'effet est faible.

**Correction proposée.** Remplacer « puis lecture par un lecteur neuf, qui fait foi pour ce run » par « puis lecture par un lecteur neuf, sous les mêmes cloisons (comme le contre-lecteur de l'addendum), qui fait foi pour ce run ; un nouveau refus ou une nouvelle erreur à cette lecture : « pas de verdict » pour ce run ». Si l'auteur préfère que la règle rejoue, il l'écrit avec sa borne.

### 9. remarque — § 3, l. 157-158, 163-165 et 169-171

**Constat.** Lecteur arrêté sans rien rendre : la règle est claire sur l'essentiel (remplacé, même consigne, le remplaçant fait foi) et aucune décision n'y connaît un résultat. Le code est déterministe (même dossier, même graine de rééchantillonnage) : le verdict ne dépend pas du lecteur. Trois détails. Rien ne dit qui constate l'arrêt ni à quoi on le reconnaît. Un rapport que le lecteur arrêté aurait déjà scellé reste dans le dépôt sans statut. Le remplaçant est forcément lancé après que l'autre lecteur a rendu son empreinte, ce que « chacun avant que l'autre n'ait rendu » et « consigné avant qu'aucun des deux lecteurs n'ait rendu » interdisent à la lettre.

**Correction proposée.** Remplacer « Un lecteur qui s'arrête sans rien rendre est remplacé par un lecteur neuf, sur la même consigne, qui fait alors foi ; c'est rapporté. » par « Un lecteur dont l'exécution finit sans empreinte ni mention est remplacé par un lecteur neuf, sur la même consigne, qui fait alors foi, même lancé après que l'autre a rendu ; un rapport que le premier aurait scellé n'est pas retenu ; c'est rapporté. »

### 10. remarque — § 3, l. 141-147, 153-155, 160-162 et 173-175

**Constat.** Deux cas de bord, sans effet sur le verdict retenu. (a) Un run principal interrompu avant 20 tours complets sans relance (seconde erreur, K recalculé sous 20, mot de relance non donné) a des journaux transférés et scellés, mais relève du cas (ii) (« sans run principal lisible »). La parenthèse « (cas (i) ; cas (iii) …) » laisse deux lectures sur le lancement d'un second lecteur ; c'est « pas de verdict » des deux façons. (b) La puce « Refus ou erreur » vise aussi un refus « de l'assemblage ». Or l'assemblage d'une relance passée par le chemin de l'addendum 5 est fait par la session avant la clôture : ni lecteur, ni rapport, ni délai de 72 h ne s'y appliquent tels quels, et la note de clôture ne peut pas nommer un dossier assemblé refusé. Aucun résultat n'est connu à ce moment.

**Correction proposée.** (a) Remplacer « (cas (i) ; cas (iii) après le début du run principal, lu comme un run interrompu, l. 338) » par « (cas (i) ; cas (ii) ou (iii) après le début du run principal, lu comme un run interrompu, l. 338) ». (b) Après « le dossier assemblé, fait avant la clôture, s'il y a eu relance par le chemin de l'addendum 5 » insérer « ; un refus de cet assemblage est tranché avant la clôture, par la règle de la puce « Refus ou erreur », sans lecteur ».

## Angle « application des constats de la passe finale » — bloquant : oui

Non scellable en l'état : un bloquant, six points à corriger, trois remarques. Le bloquant se corrige en deux remplacements courts, sans refonte.

**Application des 40 constats de la passe finale**
- 38 sont appliqués fidèlement, vérifiés par programme (textes de remplacement présents, anciennes formules absentes). Là où deux relecteurs proposaient deux textes pour le même point, l'auteur en a pris un ou les a fusionnés, sans perte.
- Le bloquant « refus ou erreur à la lecture » (premier angle, point 1) est appliqué avec le choix que le relecteur laissait à l'auteur ; ce choix est écrit dans la section « Contre-lecture ».
- Un constat est appliqué en partie (premier angle, point 3) : le membre de phrase « donné avant le scellement… » de la condition 7 a disparu sans raison écrite.
- Aucun constat n'est écarté, aucun n'est oublié.

**Le choix de l'auteur (puce « Refus ou erreur à la lecture »)**
- Il s'accorde avec « le premier lancé fait foi », avec le lecteur remplacé, avec la puce « Rapport », avec le § 5 (f) et avec la condition 7 du § 6.
- Il n'est pas écrit sans ambiguïté. Le classement « pièce » ou « code » décide si le run a un verdict, et il se fait après la clôture, quand l'interdit de lire les notes a cessé. L'aveugle n'est écrit que pour les rapports : la session, l'auteur de la correction ou son contre-lecteur peuvent ouvrir les notes du run en cause pour le diagnostic. C'est le bloquant (une décision qui dépendrait d'un résultat lu).
- Restent à écrire : trois cas sans branche (erreur d'exécution, dossier assemblé, commande consignée) ; le sens de « sans toucher à aucune condition de refus » quand le défaut est un refus levé à tort ; la commande, les cloisons et le second refus du lecteur neuf ; l'en-tête « sans autre étape » du § 6 ; deux formules des puces voisines.

**Phrases et renvois**
- Aucune phrase cassée.
- Tous les renvois ajoutés portent ce qu'on leur fait dire : l. 231, 241-242, 243-245, 248, 268-270, 363 du texte ; addendum 5, § 4 ; addendum 6, § 1. Les deux § 5 (d) ne parlent que de l'assemblage refusé (remarque).
- Empreintes revérifiées : `eab770c9…` (rapport de la passe finale), `df9a3eda…`, `93494ff9…`, `74df1fbf…`, `7f03f882…`, `546aa0bc…`, `3e992ff3…`. La destruction à 11:47:37Z et les machines 146915, 146917, 151320 et 154960 sont confirmées dans les pièces citées.

**Cloisons** : tenues. Aucune note ni journal technique ouvert, `valider` et `lire` non appelés, aucune commande réseau, aucun fichier du dépôt créé ni modifié ; les copies de travail sont hors dépôt.

Fichier relu : /home/user/controle-ia-travail/prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md au commit 9c3613d6 (`ba24eb3f…`, identique au disque). Rapport de la passe finale : /home/user/controle-ia-travail/docs/notes/reproduction-attaque-publiee-v1/verification-adverse-addendum-7-bailey-v3.md.

### 1. bloquant — § 3, l. 173-183 (« Refus ou erreur à la lecture »), surtout l. 175-176 et 181-182 ; avec l. 131-134 et l. 169-170

**Constat.** Le choix de l'auteur fait dépendre le sort d'un run d'un diagnostic : le refus « tient à la pièce lue » (pas de verdict) ou « à un défaut du code ou de l'assemblage » (correction, puis verdict qui fait foi). Ce diagnostic, l'addendum de correction et sa contre-lecture se font après la clôture. Or l'aveugle n'est écrit que pour les rapports (« tranché sans ouvrir aucun rapport », « La session n'ouvre aucun rapport »). L'interdit de lire les notes (l. 131-134) cesse à la clôture, et « sans qu'aucune valeur de note ait été rendue » ne vise que ce que le code a rendu au lecteur avant le refus. Rien n'empêche donc la session, l'auteur de la correction ou son contre-lecteur d'ouvrir le journal des notes du run en cause pour établir la cause, ni de jouer le code corrigé sur le dossier réel avant le lecteur neuf. Pour une erreur de `lire`, c'est le geste naturel : `assembler`, `audit` et `grandeurs_rapportees` de `lecture_v8` (l. 598-742) travaillent sur les notes. Le classement « pièce » ou « code » se ferait alors en connaissant les notes de ce run. Pour une confirmation à K′ ≥ 71, il décide si le verdict retenu est le sien ou celui à 36 tours. La voie est fermée du côté de l'autre verdict, pas du côté du run lui-même. Ce point naît du choix de l'auteur : dans le texte du premier relecteur, le classement était mécanique (un `GardeArret` ou non).

**Correction proposée.** Remplacer « nœud, tranché sans ouvrir aucun rapport. » par « nœud, tranché sans ouvrir aucun rapport ni lire aucune valeur de note : le diagnostic, la correction et sa contre-lecture se bornent au message du code, aux noms, tailles et empreintes des pièces, aux états et aux champs techniques (comme l. 370), et le code corrigé n'est joué sur le dossier réel que par le lecteur neuf. » Remplacer « ou si une valeur de note a été rendue avant le refus ou l'erreur » par « ou si une valeur de note de ce run a été rendue avant le refus ou l'erreur, ou lue, hors de l'exécution du code par un lecteur, avant que le lecteur neuf ait scellé son rapport ».

### 2. à corriger — § 3, l. 176-178 (« Ou bien le refus tient à la pièce lue… Ou bien il tient à un défaut du code ou de l'assemblage »)

**Constat.** La dichotomie laisse trois cas sans branche ; chacun se lit « pas de verdict » ou « correction ». (a) « Le refus tient… / il tient… » ne classe que le refus : l'erreur d'exécution, nommée dans la première et la dernière phrase, n'a pas de branche (erreur née d'une pièce mal formée, par exemple). (b) Le dossier assemblé est à la fois « la pièce lue » par le lecteur (`lecture-assemblee-v1`) et le produit de « l'assemblage » : un refus de `valider` sur un dossier assemblé non conforme relève des deux branches. (c) Un refus ou une erreur né de la commande consignée ou de son environnement (chemin, argument, `PYTHONPATH`) n'est ni la pièce ni le code. Or cette commande n'a pas pu être essayée sur le dossier réel (cloison, § 5 (f)) et « ne change plus » (l. 155). Le nœud est tranché à l'aveugle une fois le premier constat corrigé ; il reste à écrire la règle.

**Correction proposée.** Remplacer « Ou bien le refus tient à la pièce lue (absente, altérée ou non conforme) : » par « Ou bien le refus ou l'erreur tient aux pièces transférées et scellées (absentes, altérées ou non conformes) : ». Remplacer « Ou bien il tient à un défaut du code ou de l'assemblage : » par « Ou bien il tient à un défaut du code de lecture, de l'assemblage (dossier assemblé qui ne reproduit pas ces pièces) ou de la commande consignée : ». Si l'auteur préfère qu'un défaut de la commande vaille « pas de verdict », il l'écrit dans la première branche.

### 3. à corriger — § 3, l. 178 (« sans toucher à aucun critère gelé, seuil, garde ni condition de refus »)

**Constat.** Le texte du relecteur (« ni refus ») supposait qu'un refus ne se corrige jamais. Avec le choix de l'auteur, le défaut corrigeable est justement un refus levé à tort : la correction change le code qui décide ce refus. La phrase se lit alors de deux façons. Soit la correction est interdite dès que le défaut est dans le code d'un refus, et il ne reste de corrigeable que l'assemblage et les erreurs d'exécution. Soit elle est permise tant qu'aucun refus n'est desserré.

**Correction proposée.** Remplacer « sans toucher à aucun critère gelé, seuil, garde ni condition de refus, » par « sans toucher à aucun critère gelé, seuil ni garde, ni à aucune condition de refus autre que celle que le défaut fait lever à tort (elle continue de refuser une pièce absente, altérée ou non conforme), ».

### 4. à corriger — § 3, l. 155 (« ils ne changent plus ») ; l. 165-167 (cloisons des « deux lecteurs ») ; l. 179-181 (« puis lecture par un lecteur neuf »)

**Constat.** Trois points de la lecture après correction ne sont pas écrits. (a) La note de clôture fixe le dossier et la commande, qui « ne changent plus ». Or un code corrigé porte un nom neuf (R12), donc une commande neuve, et un défaut d'assemblage donne un dossier neuf. (b) Les cloisons visent « les deux lecteurs » ; le lecteur neuf n'a ni consigne ni cloisons écrites, alors que le lecteur remplacé a « la même consigne ». (c) Rien ne dit ce que vaut un second refus ou une seconde erreur après correction : nouveau nœud et nouveau délai de 72 h, ou « pas de verdict ». Le texte borne partout ailleurs à une seule reprise (l. 366, 371).

**Correction proposée.** Remplacer « puis lecture par un lecteur neuf, qui fait foi pour ce run » par « puis lecture par un lecteur neuf, sur la même consigne et les mêmes cloisons, avec le dossier et la commande que nomme cet addendum (seule exception à « ils ne changent plus »), qui fait foi pour ce run ». Après « ce n'est pas une relecture). » ajouter « Un second refus ou une seconde erreur pour le même run : « pas de verdict ». »

### 5. à corriger — § 6, l. 272 (« Ordre, sans autre étape que les suites permises avant la clôture (§ 2.1, § 2.3) »)

**Constat.** La phrase exclut à la lettre l'addendum de correction et la lecture par un lecteur neuf, qui viennent après la clôture. L'étape 4 renvoie bien au § 3, mais l'en-tête de la liste dit le contraire. C'est, en plus léger, la friction du premier bloquant de la seconde passe (exception « défaut technique » contre l'ordre du § 6). Le reste du § 6 s'accorde avec le choix de l'auteur : la condition 7 fait accepter en bloc la règle « refus ou erreur à la lecture », et la demande du mot de lancement porte les risques du § 5, donc le (f).

**Correction proposée.** Remplacer « Ordre, sans autre étape que les suites permises avant la clôture (§ 2.1, § 2.3) : » par « Ordre, sans autre étape que les suites permises avant la clôture (§ 2.1, § 2.3) et, après elle, la suite d'un refus ou d'une erreur à la lecture (§ 3) : ».

### 6. à corriger — § 3, l. 169-170 (« ou que la suite d'un refus ou d'une erreur soit close ») ; l. 197-198 (« la lecture qui suit un refus ou une erreur n'est pas une relecture »)

**Constat.** Deux formules reprises telles quelles des relecteurs ne suivent pas le choix de l'auteur. (a) La parenthèse de la puce « Après le lancement du premier lecteur » couvre aussi, à la lettre, une lecture faite après un refus tenant à la pièce, que la puce « Refus ou erreur » classe « pas de verdict ». Seul « le premier lancé fait foi » l'écarte. (b) « La suite d'un refus ou d'une erreur soit close » ne dit pas quand elle l'est : à l'addendum scellé, ou au rapport scellé du lecteur neuf. La puce « Rapport » (« chaque verdict attendu soit scellé, ou son absence constatée ») est plus stricte et l'emporte, mais les deux phrases doivent dire la même chose. Sinon la session peut soutenir qu'elle ouvre l'autre rapport dès l'addendum scellé, avant de lancer le lecteur neuf.

**Correction proposée.** (a) Remplacer « (la lecture qui suit un refus ou une erreur n'est pas une relecture) » par « (la lecture par un lecteur neuf, après l'addendum de correction de la puce « Refus ou erreur à la lecture », n'est pas une relecture) ». (b) Remplacer « ou que la suite d'un refus ou d'une erreur soit close » par « ou, après un refus ou une erreur, que le lecteur neuf ait scellé le sien ou que « pas de verdict » soit constaté pour ce run ».

### 7. à corriger — § 6, condition 7, l. 266-269 ; section « Contre-lecture », l. 308-313

**Constat.** C'est le seul constat de la passe finale appliqué en partie (angle « contre-lecture entière », point 3). Le texte de remplacement gardait « donné avant le scellement de cet addendum, il ne vaut que si les § 2 et 3 scellés sont identiques à ce qui a été porté à sa connaissance ; ». Ce membre de phrase, présent au commit 11954d70 pour le seul § 2 (l. 211-212), a disparu, sans raison écrite dans la section « Contre-lecture ». L'ordre du § 6 (demande envoyée avec l'empreinte de l'addendum scellé, puis mot reçu) le rend en partie redondant, mais un mot donné avant le scellement n'a plus de règle.

**Correction proposée.** Après « qui sont un choix de la session ; » réinsérer « donné avant le scellement de cet addendum, il ne vaut que si les § 2 et 3 scellés sont identiques à ce qui a été porté à sa connaissance ; ». À défaut, ajouter à la section « Contre-lecture » : « membre de phrase « donné avant le scellement… » de la condition 7 retiré : la demande part après le scellement, avec l'empreinte (§ 6, étape 2). »

### 8. remarque — § 3, l. 177 (renvoi aux addenda 5 et 6, § 5 (d)) ; § 5 (f), l. 251-252

**Constat.** Les renvois ajoutés portent ce qu'on leur fait dire : l. 231 (citation exacte), 241-242, 243-245 et 248 (citations exactes), 268-270 et 363 du texte ; addendum 5, § 4 (mise en place refaite par conduite et poste neufs, nouveau mot de Lazar) ; addendum 6, § 1 (carte sans fonds, `billing_failed` resté faux). Les deux § 5 (d) disent bien « assemblage refusé : pas de verdict, nœud », mais pour l'assemblage seulement et sans distinguer la cause ; l'addendum 6 y prévoit déjà qu'un défaut se corrige par addendum « avant toute lecture ». Placés après la seule branche « pièce », ils laissent croire que ces addenda ne visent qu'elle. Par ailleurs le § 5 (f) s'accorde avec le § 3 mais ne dit pas la conséquence : si le run à 36 tours reste sans verdict et que la confirmation n'est pas retenue, l'étape 1 n'a aucun verdict retenu (« dans tous les autres cas », l. 190-192).

**Correction proposée.** Remplacer « « pas de verdict » pour ce run (addendum 5, § 5 (d) ; addendum 6, § 5 (d)). » par « « pas de verdict » pour ce run (comme aux addenda 5 et 6, § 5 (d), pour l'assemblage refusé, dont ce texte tranche le nœud). » Au § 5 (f), remplacer « et pourrait laisser ce run sans verdict. » par « et pourrait laisser ce run sans verdict ; si la confirmation n'est pas retenue, l'étape 1 reste alors sans verdict retenu (§ 3). »

### 9. remarque — § 2.1, l. 70-71 (« conduite et poste neufs »)

**Constat.** La phrase ajoutée reprend l'addendum 5, § 4, où « poste » désigne le script du poste Hetzner. Dans cet addendum, « poste neuf » vient d'être défini au § 2.2 comme un poste de dépense où D repart de zéro. Une mise en place refaite pourrait donc se lire comme un poste de dépense neuf (D remis à zéro, B = 85 de nouveau). La seconde tentative du § 2.3 dit « même poste (D cumulée, même B) » ; la mise en place refaite ne le dit pas. L'effet sur K est faible, car une mise en place coûte peu.

**Correction proposée.** Remplacer « (l. 363 ; addendum 5, § 4 : conduite et poste neufs, mot de Lazar) » par « (l. 363 ; addendum 5, § 4 : conduite et script de poste neufs (R12), mot de Lazar ; même poste de dépense : D cumulée, même B) ».

### 10. remarque — Section « Contre-lecture », l. 298-313

**Constat.** Traçabilité. Aucun constat n'est écarté, et la section n'a donc aucune raison d'écart à porter ; le choix de l'auteur y est bien écrit (l. 306-308). Deux manques. (a) La liste « Points « à corriger » et remarques des trois angles repris » omet des points pourtant appliqués : lecture qui suit un refus et définition de « la confirmation » ; dossier de lecture de l'autre lecteur ; champs techniques connus avant la clôture ; lancement tardif et « sans autre étape » ; relevé et alerte du § 2.5 ; liste des bloquants de la seconde passe ; `PYTHONPATH`. (b) La phrase « Repris des deux passes : un seul lecteur par verdict, … essais complémentaires scellés. » du commit 11954d70 (l. 242-247) a été retirée sans qu'aucun constat le demande ; la trace de ce qui vient des deux premières passes est perdue.

**Correction proposée.** Après « commits intermédiaires » (l. 313), ajouter « ; lecture qui suit un refus et définition de « la confirmation » ; dossier de lecture de l'autre lecteur ; champs techniques connus avant la clôture ; lancement tardif des lecteurs et ordre du § 6 ; relevé et alerte du § 2.5 ; liste des bloquants de la seconde passe ; `PYTHONPATH`. Aucun constat écarté. » Rétablir, après « avant la clôture. » (l. 301), la phrase « Repris des deux passes : … essais complémentaires scellés. » du commit 11954d70.
