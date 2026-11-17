# Vérification adverse de l'addendum 7 — seconde passe (version corrigée, commit 0c373143) — v2

Workflow `reverifier-addendum-7-bailey` (run `wf_cf1c580a-4d0`), lancé par la session `session_01XJ6MgnEhQMZteN9F8a1BST` le 17 novembre 2026 ; deux sous-agents neufs ; cloisons : aucune note lue. Retours reproduits tels quels.

## Angle : application des corrections de la première vérification — bloquant : oui

Ne pas sceller l'addendum en l'état. Les treize corrections de la première vérification, sans compter les remarques facultatives, sont bien appliquées. Je l'ai vérifié par programme, en ramenant les espaces à un seul. Le texte de remplacement du § 6 est identique, de l'étape 2 jusqu'à « avec cette réserve. ». Sont repris mot pour mot et à la bonne place : le titre du § 2, le § 2.3, le § 2.4, l'ajout à la condition 2, l'exception du § 3, la dernière puce du § 3, K′, le lecteur de la confirmation, le refus de `valider`, l'échéance à 02:48Z et l'objet du GO (seule la majuscule change).

Contrôles qui passent :
- aucune phrase coupée, aucune liste ni numérotation cassée ;
- `82ef2fa0…` vérifiée, avec son `.sha256` ; `e573e4c7…` et `f1c2ca52…` vérifiées ;
- les essais complémentaires donnent 4 passés (relancés sans écrire dans le dépôt).

Pendant la vérification, la version lue a été commitée : 0c373143, empreinte e0a179cf…, arbre propre.

Deux textes de remplacement de l'angle « règle de lecture », justes chacun seul, créent ensemble deux contradictions nouvelles, l'une et l'autre bloquantes :
- (1) La voie « défaut du § 3 » ne peut pas se suivre avec le § 6. Elle exige une correction et des pièces refaites après la lecture. Le § 6 l'interdit (« Aucune pièce de l'étape 2 n'est faite après la lecture » ; délai de 24 h de l'étape 4 ; `lecture_v8` nommé pour la confirmation ; « défaut du § 3 » classé cause de non-lancement). Le lecteur choisit alors, verdict connu, si la confirmation corrigée est retenue.
- (2) Prise à la lettre, la liste des défauts comprend « la chute d'une garde nommée ». Or la relance a fini par la garde de dépense (§ 1). Un défaut est donc déjà ouvert sur un fait connu avant la lecture.

S'ajoutent un « à corriger » (l'échéance est dite « sans décision » alors que la condition 2 ouvre une ligne neuve discrétionnaire ; un poste lancé en retard n'est pas couvert) et des remarques sans conséquence. Aucune contradiction nouvelle entre le § 2.1 et le reste en dehors de ces points.

### 1. bloquant — § 3, l. 93-99 (exception « défaut technique ») ; § 3, l. 100-104 (`lecture_v8`) ; § 3, l. 116-119 (« lancée selon le § 6 ») ; § 6, l. 187 (étape 4, 24 h), l. 189 (« Aucune pièce de l'étape 2 n'est faite après la lecture »), l. 192 (« défaut du § 3 » parmi les causes de non-lancement) ; condition 2, l. 166-167

**Constat.** Contradiction nouvelle entre le § 3 et le § 6, née de deux textes de remplacement appliqués tels quels.

Ce que dit le § 3 : en cas de défaut, seul le code en cause est corrigé, par un addendum neuf écrit après la lecture. La confirmation « est alors lancée avec ce code selon cet addendum, quel que soit le verdict à 36 tours, si l'échéance le permet ; elle reste soumise à la règle du verdict retenu ».

Ce qui s'y oppose :
- Le § 6 interdit sans exception toute pièce de l'étape 2 après la lecture. Or un lanceur corrigé change `commit_code`, donc le manifeste v7, la conduite v15 et le poste v13, sous des noms neufs (R12).
- L'étape 4 impose un poste lancé au plus tard 24 h après le scellement du verdict. La condition 2 fait d'une échéance manquée pour ce motif « une décision postérieure à la lecture ».
- La confirmation est lue avec `lecture_v8` nommément, ce qui exclut un code de lecture corrigé.
- La dernière puce du § 3 ne définit « la confirmation » que comme la série « lancée selon le § 6 ». Elle déclare « jamais retenue » toute série « décidée après la lecture », sans réserver l'exception.
- Le § 6 range « défaut du § 3 » parmi les causes de non-lancement, alors que le § 3 veut qu'on lance.

Conséquence : après un défaut, une fois le verdict à 36 tours connu, on peut soutenir l'une ou l'autre lecture. Soit la confirmation corrigée est la confirmation et peut être retenue si K′ ≥ 71 (§ 3). Soit elle est hors du § 6, donc « décidée après la lecture » et jamais retenue, ou même interdite. Le verdict retenu dépend alors d'un choix fait verdict connu : c'est la porte que les bloquants 2 et 3 de la première vérification voulaient fermer.

**Correction.** (1) § 3, après « ne change rien d'autre, contre-lu (R2). », insérer : « Dans ce seul cas, les pièces de l'étape 2 que la correction touche (code, conduite, poste, manifeste et, si son objet doit citer l'addendum neuf, ligne de GO) sont refaites après la lecture sous des noms neufs (R12), contre-lues (R2) et scellées. Le délai de l'étape 4 du § 6 court du scellement de la dernière d'entre elles. Ce n'est pas une décision postérieure à la lecture, et la série ainsi lancée est « la confirmation ». Un défaut du code de lecture fait lire la confirmation avec le code corrigé que nomme cet addendum neuf. »
(2) Dernière puce du § 3 : remplacer « lancée selon le § 6 (et sa relance, l. 371) » par « lancée selon le § 6, ou, après un défaut du § 3, selon l'addendum qui le corrige (et sa relance, l. 371) ».
(3) § 6 : remplacer « Aucune pièce de l'étape 2 n'est faite après la lecture. » par « Aucune pièce de l'étape 2 n'est faite après la lecture, hors la correction d'un défaut du § 3. ».
(4) § 6 : dans la liste des causes, remplacer « défaut du § 3, » par « défaut du § 3 qui ne peut être corrigé avant l'échéance, ».
(5) Condition 2 : après « après le délai du § 6, étape 4 », ajouter « (compté, après un défaut du § 3, comme au § 3) ».

### 2. bloquant — § 3, l. 88-89 (« Ce défaut ne peut être que : la chute d'une garde nommée, … ») contre § 1, l. 10-11 (« a fini … par la garde de dépense … aucune garde tombée »)

**Constat.** La liste fermée des défauts, prise à la lettre, couvre un fait déjà connu avant la lecture.

Le § 1 dit que la relance « a fini le 15 novembre vers 11:52Z par la garde de dépense ». La liste d'arrêt du texte appelle cette garde « Dépense du poste … ≥ B − 2 USD : arrêt … ; run tronqué » ; c'est la fin normale d'un run au régime réduit. La nouvelle exception compte comme défaut technique « la chute d'une garde nommée », sans exclure les arrêts de dépense ni d'échéance.

Un lecteur peut donc établir dès la lecture à 36 tours un « défaut » qui n'en est pas un. La suite est alors une confirmation non lancée « avec ce code », un « code en cause » introuvable, un addendum neuf postérieur à la lecture et un retard, avec le risque « confirmation non lancée (défaut du § 3) ». Le « aucune garde tombée » du § 1 montre la convention de l'auteur, mais l'exception ne la reprend pas. L'ambiguïté porte sur la seule voie d'exception de la règle et n'est levée nulle part.

**Correction.** § 3 : remplacer « la chute d'une garde nommée, » par « la chute d'une garde nommée, hors les arrêts de dépense (B − 2) et d'échéance de la liste d'arrêt, qui tronquent un run sans défaut (la relance a fini ainsi, § 1), ».

### 3. à corriger — Condition 2, l. 165-167 (« au-delà, une ligne neuve ; … ou une ligne neuve refusée, est une décision postérieure à la lecture ») ; § 6, l. 191-192 (« échéance (condition 2) » parmi les causes « constatées sans décision ») ; étape 4, l. 187

**Constat.** (i) La condition 2 garde « au-delà, une ligne neuve ». Une échéance dépassée ouvre donc toujours une décision prise après la lecture : demander, puis accorder ou refuser la ligne. Le refus est classé écart, mais l'octroi prolonge la série sans aucune mention. « Échéance (condition 2) » ne peut donc jamais être une cause « constatée sans décision », comme le dit le § 6. Les deux textes, ajoutés séparément, ne s'accordent pas.
(ii) Un poste lancé plus de 24 h après le scellement, mais qui tient l'échéance, n'est couvert ni par l'ajout de la condition 2 (qui ne vise qu'une échéance manquée) ni par la phrase finale du § 6 (qui ne vise qu'une absence de lancement ou un arrêt). On ne sait pas si cette série est « lancée selon le § 6 », donc si elle peut être retenue.

**Correction.** Condition 2 : remplacer « au-delà, une ligne neuve ; » par « au-delà, la confirmation n'est pas lancée (« échéance »), sans ligne neuve ; », et retirer « , ou une ligne neuve refusée, » de la phrase ajoutée. (Autre voie : garder la ligne neuve, mais écrire que sa demande est faite sans attendre et qu'accordée ou refusée elle est rapportée « décidée après la lecture », et retirer alors « échéance (condition 2) » de la liste du § 6.)
Étape 4 : ajouter « ; un poste lancé après ce délai est un écart (nœud), et la série ainsi lancée est rapportée « décidée après la lecture » ».

### 4. remarque — § 3, l. 120-122 (empreintes de suffixe)

**Constat.** La remarque 4 de l'angle fidélité demandait « les empreintes de suffixe (écart 9) ». « Écart 9 » a été placé dans la parenthèse « (graines identiques, écart 9) », où il semble qualifier les graines et non les empreintes. Le texte, l. 344, parle bien des « empreintes de l'écart 9 ». Le sens reste devinable et la puce n'a aucun effet sur la lecture.

**Correction.** Écrire « les empreintes de suffixe (écart 9) de la confirmation diffèrent de celles de la relance (graines identiques), calculé et lu après … ».

### 5. remarque — § 1, l. 14 (« Le texte lit ce run comme un run tronqué de K′ = 36 tours »)

**Constat.** La remarque 6 a été appliquée au § 3, mais le § 1 écrit toujours K′ = 36 avant la lecture. La tension est légère, puisque le § 3 dit désormais que K′ est établi par la lecture.

**Correction.** Facultatif : « comme un run tronqué (36 tours complets au bilan ; K′ établi par la lecture) ».

### 6. remarque — § 2 bis, l. 76-80 ; § 5 (a), l. 147-148

**Constat.** Phrases du § 2 bis :
- La phrase « Hôte à t = 1 800 s qui croîtrait comme la relance, à 1,258 USD/h : arrêt à B − 2 vers 45 tours » est insérée avant la phrase identique qui définit la croissance (« ≈ 180 s par tour, mise à l'échelle 1 800/2 276 »). Il en résulte un doublon, et un renvoi qui précède sa définition.
- Rien de cassé, mais le § 2 bis dit maintenant 45 tours à 1,258 USD/h quand le § 5 (a) ne donne que 48 et 39. Le § 5 (a) n'est pas tenu de suivre, la correction étant facultative.
- La remarque 5 de l'angle fidélité (« plus 33 à 84,5 USD » non mis à jour) n'est pas reprise. Ce choix est permis et n'est pas annoncé comme repris.

**Correction.** Facultatif : fondre les deux phrases en « Hôte à t = 1 800 s qui croîtrait comme la relance (≈ 180 s par tour, mise à l'échelle 1 800/2 276) : arrêt à B − 2 vers 48 tours complets à 1,108 USD/h, vers 45 à 1,258 USD/h (c de la règle), vers 39 à 1,6 USD/h (régime réduit). » Reporter « ≈ 45 à 1,258 USD/h » au § 5 (a) si l'on veut l'accord.

### 7. remarque — Section « Contre-lecture », l. 203-213

**Constat.** Deux détails :
- La liste des remarques reprises omet « écart 9 » (remarque 4 de l'angle fidélité), qui a pourtant été reprise.
- « Échéance de création à ce taux » renvoie à 1,258 USD/h, alors que le § 6 donne désormais 02:48Z à 1,2576 USD/h.
Le paragraphe de la vérification adverse reste par ailleurs exact : trois bloquants, cinq « à corriger » et les remarques citées correspondent aux changements vérifiés. Le `.sha256` des essais complémentaires est commité (7a115fdf).

**Correction.** Facultatif : ajouter « écart 9 » aux remarques reprises, et écrire « échéance de création au taux relevé (1,2576 USD/h) ».

## Angle : adversaire (voies restantes après lecture du verdict à 36 tours) — bloquant : oui

À ne pas sceller en l'état : deux bloquants. Les voies que le texte corrigé ferme vraiment sont les suivantes. Le mot de lancement est reçu avant la lecture et vaut en bloc, sans modification. B = 85 est fixé, et le filtre comme la garde de 1 800 s sont figés dans les pièces contre-lues. Une tentative, une série ou une relecture décidée après la lecture n'est jamais retenue. Le défaut technique est borné à des causes mécaniques, sans aucune valeur de note. La règle K′ ≥ 71 est symétrique, quel que soit le verdict. Le contrôle du juge hors seuil est réglé. Les empreintes de suffixe ne sont lues qu'après les deux verdicts. « Mot retiré », « recharge suspendue » et « ligne non renouvelée » portent la réserve. Restent des voies qui permettent d'empêcher la confirmation sans cette réserve, sous l'apparence d'une cause technique. (1) Des causes classées « sans décision » dépendent en fait d'une décision prise après la lecture : crédit 9′ non tenu (crédit versé par Lazar, dépense des autres chantiers) ; « ligne de la liste d'arrêt », qui couvre « une condition de lancement manque » (condition 3, 4 ou 8 retirée, GO révoqué) ; échéance manquée parce que le scellement du verdict a été retardé après sa remise, l'étape 3 n'ayant aucune borne et le délai de 24 h courant du scellement. (2) Pendant et après le run : un compte vidé quand la carte n'a plus de fonds passe pour une « coupure de l'hôte » ; « sa relance (l. 371) » est ambiguë quand elle exige une conduite et un addendum neufs (le code ne relance pas après une coupure) ; la reprise de la lecture 38 n'a pas de délai ; refaire ou non la mise en place reste un choix. À corriger aussi : un seul lecteur par verdict, consigné, sur une commande fixée, avec un délai pour lancer celui de la confirmation, et aucun verdict retenu avant la clôture ; les 24 h d'offre, qui se heurtent à l'arrêt d'une heure prévu par 9′ ; le délai de l'addendum correctif ; la réserve, qui doit suivre le verdict dans la formule publique. Remarques : mot conditionnel, lecteur de la confirmation tenu loin des registres, location des offres par un autre chantier. Chaque correction est donnée mot pour mot ; aucune ne touche une hypothèse, un seuil ou un critère gelé. Je n'ai modifié ni créé aucun fichier. Je n'ai ouvert aucun fichier sous cloison. Fichiers lus : /home/user/controle-ia-travail/prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md (et son diff avec HEAD) ; /home/user/controle-ia-travail/docs/notes/reproduction-attaque-publiee-v1/verification-adverse-addendum-7-bailey-v1.md ; /home/user/controle-ia-travail/docs/notes/reproduction-attaque-publiee-v1/contre-lecture-addendum-7-confirmation-bailey-v1.md ; /home/user/controle-ia-travail/prereg/temoin-attaque-publiee-bailey-v1.md ; addenda 2 (lecture 38), 5 et 6 ; /home/user/controle-ia-travail/src/controle_ia/temoin_bailey/lanceur_v21.py (relance, reprise) ; /home/user/controle-ia-travail/runs/temoin-bailey-v1-20261111/poste-hetzner-v12.sh (attente d'offre).

### 1. bloquant — § 6, l. 191-193 (causes « constatées sans décision ») ; l. 181-183 (relevé « indicatif ») ; l. 186-187 (étapes 3 et 4) ; § 2.4, l. 64-65

**Constat.** Trois causes de la liste « sans décision » dépendent en fait d'une décision prise après la lecture. Elles laissent l'adversaire qui préfère le verdict à 36 tours empêcher la confirmation sans recevoir la réserve « décidé après la lecture ». Le premier bloquant de la vérification précédente est donc rouvert par une autre porte. (1) Crédit 9′ : le crédit du compte dépend des versements de Lazar et de la dépense des autres chantiers (addendum 6, § 1 et risque (b)). Ne pas créditer, ou laisser un autre chantier consommer, donne « crédit 9′ non tenu au relevé (§ 2.5) », sans réserve. Le relevé de l'étape 2 n'est qu'« indicatif » et n'a pas à tenir 9′. (2) « Une ligne de la liste d'arrêt » comprend la ligne « une condition de lancement manque » ([T] l. 362) et la ligne « modèle ou juge … sous conditions non acceptées » ([T] l. 364). Retirer après la lecture la condition 3, 4 ou 8, ou révoquer la ligne de GO (`verifier_non_revoque`), passe donc pour une ligne de la liste d'arrêt. Seuls « mot retiré » et « ligne de GO non renouvelée » sont nommés comme des décisions. (3) Échéance : le délai de 24 h court du scellement du verdict à 36 tours, et non de sa remise. L'étape 3 n'a aucune borne. On peut recevoir le verdict, retarder son scellement, puis lancer le poste dans les 24 h. La création tombe alors après la limite (vers le 28 novembre 02:48Z à 1,2576 USD/h) et l'absence de lancement est classée « échéance (condition 2) », sans réserve.

**Correction.** (a) § 6, étape 2, remplacer « et un relevé de crédit indicatif (c₀, o, S) ; le relevé de 9′ fait à l'étape 4 est consigné
     dans l'ordre de lancement sans nouveau mot ; » par « et un relevé de crédit (c₀, o, S) qui tient déjà 9′ (s'il ne la tient pas, la lecture attend qu'il la tienne) ; le relevé de 9′ fait à l'étape 4 est consigné
     dans l'ordre de lancement sans nouveau mot ; les conditions de lancement 3, 4 et 8 y sont constatées valoir pour cette série, et le mot de Lazar les couvre ; ». (b) Remplacer « 3. le verdict à 36 tours prononcé et scellé (R13) ;
4. crédit relevé (9′), poste lancé au plus tard 24 h après le scellement du verdict à 36 tours, création. » par « 3. le lecteur du verdict à 36 tours lancé au plus tard 24 h après la fin de l'étape 2 ; son verdict scellé tel qu'il est rendu, dans l'heure qui suit sa remise à la session (R13) ;
4. crédit relevé (9′), poste lancé au plus tard 24 h après la remise du verdict à 36 tours, création. ». (c) § 2.4, remplacer « lui-même au plus tard 24 h après le
   scellement du verdict à 36 tours (§ 6, étape 4) » par « lui-même au plus tard 24 h après la
   remise du verdict à 36 tours (§ 6, étape 4) ». (d) § 6, remplacer « Après la lecture, la confirmation ne manque que par une cause fixée ici et constatée sans décision :
aucune offre conforme (§ 2.4), crédit 9′ non tenu au relevé (§ 2.5), échéance (condition 2), défaut du § 3, ou une ligne
de la liste d'arrêt. » par « Après la lecture, la confirmation ne manque que par une cause fixée ici et constatée sans décision :
aucune offre conforme (§ 2.4), échéance (condition 2) alors que les délais des étapes 3 et 4 et du § 3 ont été tenus, défaut du § 3, ou une ligne
de la liste d'arrêt constatée par le code (garde, contrôle du juge, règle, dépense, échéance, erreur technique nommée), hors les lignes « une condition de lancement manque » et « modèle ou juge … sous conditions non acceptées ». Sont des décisions postérieures à la lecture, quelle que soit leur forme : un crédit 9′ non tenu au relevé de l'étape 4 alors qu'il l'était à l'étape 2 ; une condition de lancement retirée, révoquée ou contestée après la lecture, ligne de GO révoquée comprise ; une échéance manquée parce que la lecture, la remise ou le scellement du verdict à 36 tours, ou l'addendum du § 3, ont dépassé leur délai. »

### 2. bloquant — § 3, l. 116-117 (« et sa relance, l. 371 ») ; § 6, l. 194-195 (liste des décisions postérieures) ; [T] l. 363, 371 ; lanceur_v21 l. 1789-1792

**Constat.** Pendant et après le run, quatre voies restent ouvertes. (1) Compte vidé : si la carte n'a plus de fonds, la recharge échoue sans `billing_failed` (addendum 6, § 1). Vast coupe alors l'instance, ce que les addenda 5 et 6 ont classé « coupure de l'hôte », une ligne de la liste d'arrêt. Au-delà de 20 tours, on obtient un run tronqué, K′ ≤ 70, et le verdict à 36 tours est retenu sans réserve. Or les fonds de la carte dépendent de Lazar, et seule « recharge suspendue » est nommée comme une décision. (2) « Sa relance (l. 371) » est ambiguë. Après une coupure, `lanceur_v21` ne relance pas (« exécution principale morte sans état … pas de relance ; nœud »). La relance du texte exige alors une conduite et un addendum neufs, comme l'addendum 5. Le § 3 la dit à la fois « la confirmation » (sa relance) et « tentative décidée après la lecture » (jamais retenue). L'adversaire choisit la lecture selon le signe. (3) Reprise de la lecture 38 : quand le transfert n'a pas fait foi, la reprise est indispensable au verdict. Rien n'en fixe le délai, et elle demande peut-être un crédit versé par Lazar (série 3). La retarder au-delà de l'échéance, ou laisser Vast supprimer l'instance, donne « pas de verdict », et le verdict à 36 tours est retenu sans réserve. Ce cas n'est ni une « absence de lancement » ni un « arrêt ». (4) Mise en place tombée : « peut être refaite » ([T] l. 363 ; addendum 5, § 4, sur un nouveau mot). Le choix de la refaire se fait après la lecture, et le statut de la mise en place refaite n'est pas fixé.

**Correction.** (a) § 3, après « désigne la seule série de cet addendum, lancée selon le § 6 (et sa relance, l. 371). », insérer : « « Sa relance » est seulement celle que joue `lanceur_v21` dans la conduite v15, sur la même instance, sans pièce, mot ni addendum neufs. Une relance qui en demanderait (coupure de l'hôte, compte vidé : chemin de l'addendum 5) est une tentative décidée après la lecture. Une garde de mise en place tombée met fin à la série (« confirmation non courue (mise en place) ») ; une mise en place refaite (l. 363) est une tentative décidée après la lecture. La reprise de la lecture 38, quand le transfert de la conduite n'a pas fait foi, fait partie de la confirmation. Elle est lancée sans nouveau mot dans les 24 h qui suivent le constat, par des pièces qui ne font que cette reprise, contre-lues (R2), et ne lit aucune note. Une coupure de l'instance faute de crédit n'est pas, pour la règle du verdict retenu, une « coupure de l'hôte » de la liste d'arrêt. » (b) § 6, remplacer « (mot retiré, recharge suspendue, ligne de GO non renouvelée,
autre motif) » par « (mot retiré, recharge suspendue, compte vidé ou recharge non payée quelle qu'en soit la cause, crédit non versé pour une reprise, reprise de la lecture 38 non lancée dans son délai, lecteur de la confirmation non lancé dans son délai, ligne de GO non renouvelée ou révoquée,
autre motif) ».

### 3. à corriger — § 3, l. 84 et l. 100-104 (lecteurs)

**Constat.** Lecteurs : rien n'interdit de lancer plusieurs lecteurs neufs pour le même verdict, puis de garder celui qui convient. Rien ne fixe non plus la commande sur laquelle on constate un refus de `valider` ou une erreur d'exécution du code de lecture : un mauvais chemin fabrique un « défaut » ou un « pas de verdict ». Aucun délai ne borne le lancement du lecteur de la confirmation. Ne pas le lancer laisse le seul verdict à 36 tours, et rien ne dit qu'aucun verdict n'est retenu avant la clôture.

**Correction.** § 3, à la fin de la puce « Verdict de confirmation », ajouter : « Chaque verdict est demandé à un seul lecteur, dont le lancement (identifiant, heure, fichiers donnés) est consigné avant qu'il ne rende. Tout autre lecteur lancé pour le même verdict est rapporté, et le premier lancé fait foi. Un refus de `valider` ou de l'assemblage, ou une erreur d'exécution du code de lecture, n'est constaté que sur la commande consignée, rejouée une seconde fois à l'identique. Le lecteur de la confirmation est lancé au plus tard 24 h après le scellement des journaux de la conduite ou de la reprise. Aucun verdict n'est retenu pour l'étape 1, ni rapporté comme tel, avant que la confirmation soit close (verdict scellé, ou cause du § 6 constatée). »

### 4. à corriger — § 2.4, l. 64-65 ; addendum 6, 9′ (poste arrêté faute d'offre dans l'heure)

**Constat.** Le délai d'offre de 24 h se heurte à 9′. Le poste v12 attend lui-même 24 h (144 essais de 600 s), mais 9′ permet aussi de lancer le poste juste après le relevé puis de l'arrêter faute d'offre dans l'heure, « avant un nouveau relevé ». Un poste arrêté au bout d'une heure et jamais relancé peut être présenté comme « aucune offre conforme ». Le texte ne dit pas non plus de quel lancement partent les 24 h.

**Correction.** § 2.4, après « « confirmation non lancée », rapportée avec sa cause. », ajouter : « Les 24 h courent du premier lancement du poste. Si le poste est arrêté faute d'offre dans l'heure (9′), il est relancé après un nouveau relevé dans l'heure qui suit, jusqu'à la fin de ces 24 h. « Aucune offre conforme » n'est constatée que par les états poussés par le poste sur ces 24 h. Un poste arrêté et non relancé est une décision postérieure à la lecture (§ 6). »

### 5. à corriger — § 3, l. 93-96 (addendum correctif après un défaut)

**Constat.** En cas de défaut, rien ne borne le délai de l'addendum correctif. Le retarder fait manquer l'échéance, ce qui donne « confirmation non lancée (défaut du § 3) », sans réserve, alors que ce retard est une décision.

**Correction.** § 3, après « qu'il est écrit après cette lecture et ne change rien d'autre, contre-lu (R2). », insérer : « Cet addendum est scellé au plus tard 72 h après la remise du verdict à 36 tours, et le poste est lancé au plus tard 24 h après son scellement. Une échéance manquée faute de ces délais est une décision postérieure à la lecture (§ 6). »

### 6. à corriger — § 6, l. 195-196 (« Le verdict retenu reste alors celui à 36 tours, avec cette réserve. »)

**Constat.** Toute décision prise après la lecture pour empêcher la confirmation laisse encore retenu le verdict à 36 tours. Cette voie ne sert que l'adversaire qui préfère ce verdict. Elle ne lui coûte qu'une réserve, et rien n'oblige cette réserve à le suivre là où il sera cité (formule publique, papier).

**Correction.** Remplacer « Le verdict
retenu reste alors celui à 36 tours, avec cette réserve. » par « Le verdict
retenu reste alors celui à 36 tours, avec cette réserve, qui l'accompagne partout où il est cité, formule publique comprise : « confirmation engagée avant la lecture, non menée pour une décision postérieure à la lecture ». » (Variante plus forte, à soumettre à Lazar avant le scellement : dans ce cas, aucun verdict n'est retenu pour l'étape 1 sans nouvelle décision.)

### 7. remarque — § 6, étape 2, l. 184-185 (mot de Lazar)

**Constat.** Un mot donné avant la lecture mais assorti d'une condition sur le verdict (par exemple « go sauf si … ») n'est pas exclu. Il rouvrirait le choix selon le signe.

**Correction.** Après « une modification est un écart, par un addendum neuf scellé avant la lecture ; », ajouter « un mot assorti d'une condition (sur le verdict, une date ou un montant) vaut refus ; ».

### 8. remarque — § 3, l. 100-101 (lecteur de la confirmation)

**Constat.** « Ne reçoit » ne l'empêche pas de lire de lui-même les registres ou les passations où le verdict à 36 tours serait consigné.

**Correction.** Remplacer « et qui ne reçoit ni ce verdict ni son rapport avant d'avoir scellé le sien » par « et qui ne reçoit ni ne lit ce verdict, son rapport, ni aucun registre, passation ou note écrits après la remise de ce verdict, avant d'avoir scellé le sien (cloisons écrites dans sa consigne) ».

### 9. remarque — § 2.4 ; § 5 (b), (c)

**Constat.** Le compte est partagé avec d'autres chantiers. Un autre chantier peut louer les offres qui passent le filtre (seulement le Texas et l'Oregon au relevé) pendant la fenêtre de 24 h, ce qui donne « aucune offre conforme », ou élever o au point de vider le compte. Cette voie est peu probable, mais elle n'est pas fermée.

**Correction.** Au § 6, dans la puce de la demande du mot de lancement, ajouter : « la demande demande aussi qu'aucun autre chantier ne loue de carte sur ce compte de la remise du verdict à la fin du transfert de la confirmation ; une location de ce genre est une décision postérieure à la lecture ». 
