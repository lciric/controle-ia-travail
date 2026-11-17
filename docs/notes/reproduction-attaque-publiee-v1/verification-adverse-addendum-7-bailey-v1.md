# Vérification adverse de l'addendum 7 (version à sceller, commit c44c6d65) — trois relecteurs indépendants — v1

Workflow `verifier-addendum-7-bailey` (run `wf_2d396cf7-130`), lancé par la session `session_01XJ6MgnEhQMZteN9F8a1BST` le 17 novembre 2026 ; trois sous-agents neufs, un angle chacun ; cloisons : aucune note lue. Retours reproduits tels quels.

## Angle : fidélité — bloquant : non

Fidélité tenue : l'addendum peut être scellé en l'état. J'ai comparé mot à mot, en ramenant les espaces à un seul, les 13 textes de remplacement du rapport (section « Textes de remplacement, mot pour mot ») avec prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md, et j'ai fait le diff complet avec le brouillon 2 (empreinte 674d8f14…, celle que cite le rapport ; empreinte du rapport f1c2ca52…, égale à son fichier compagnon et à celle que cite l'addendum).

Dix textes sur treize sont repris à l'identique et à la bonne place : § 1 (lenteur), titre du § 2, § 2.1 à 2.5, § 3, l'insertion du § 4 juste après « non fournies). » et le § 5 (a). Les trois autres ne diffèrent que par les compléments annoncés dans la section « Contre-lecture ».
- § 1 : la marque « [pièce du relevé…] » est remplacée par le relevé, `releve-offres-processeur-20261117-0025.txt`, dont l'empreinte a902256b… est vérifiée.
- § 2 bis : ajout de « (carte seule), ≈ 38 à 43 USD à 1,258 USD/h ».
- § 6 : « [à nommer] » est remplacé par l'emploi des 5 USD, et l'échéance à 1,258 USD/h est ajoutée (28 novembre 02:50Z, recalculée : exacte).

Ajouts hors des textes du rapport, tous annoncés : la puce « Information » du § 3 et la phrase « Essais complémentaires » du § 4.

Contrôles négatifs :
- Aucune autre modification, en dehors de l'en-tête (titre et ligne d'état), ce qui est normal pour un scellement.
- Aucune section manquante ni dupliquée : 1, 2, 2 bis, 3, 4, 5, 6, Contre-lecture.
- Aucune phrase coupée.
- Aucune marque restante : ni [à nommer], ni [pièce…], ni « […] », ni @@, ni « brouillon 2 », ni « À venir ».

Textes du brouillon disparus, tous à cause d'un remplacement prévu par le rapport et non par erreur : la proposition de ligne de GO (§ 6, section entière remplacée), « nœud » après la chute de la garde, et le numéro de machine 146915 au § 1.

Restent six points, aucun bloquant :
- un « à corriger » : le fichier d'essais complémentaires est cité sans empreinte ni résultat (R6) ;
- cinq remarques.

Aucun fichier modifié.

### 1. à corriger — 117-118

**Constat.** Le nouveau fichier d'essais, tests/test_temoin_bailey_condition6_v21_complements.py, est cité sans empreinte, sans fichier compagnon .sha256 et sans résultat (nombre d'essais passés). Les deux autres fichiers d'essais cités ont, eux, leur empreinte et leur fichier compagnon.

**Preuve.** ls tests/ : test_temoin_bailey_condition6_v21.py.sha256 et test_temoin_bailey_reprise_relance_v1.py.sha256 existent ; aucun test_temoin_bailey_condition6_v21_complements.py.sha256. Fichier commité dans c44c6d65. L. 117 de l'addendum : « Essais complémentaires (M-9 de la contre-lecture) : `tests/test_temoin_bailey_condition6_v21_complements.py` (pilote repris pour une autre cause, puis garde ; t non fini). » La v21 du lanceur est inchangée (75cf4049…), donc aucun nouvel addendum n'est requis pour ce code.

**Correction.** Avant le scellement : sceller le fichier d'essais (fichier compagnon .sha256), citer son empreinte abrégée et le résultat de l'exécution (par exemple « n passés »).

### 2. remarque — 28-31

**Constat.** La pièce citée au § 1 ne prouve pas tout ce qu'elle accompagne. Elle donne le coût de l'offre avec 110 Go de stockage (1,2576) et le processeur, mais ni le taux de 1,108 USD/h pour la carte seule ni la date du 16 novembre.

**Preuve.** Le relevé (a902256b…) est daté du 2026-11-17T00:25:54Z et sa seule ligne utile sur cette offre dit « offre 59431043 machine 146915 Texas, US cout_110Go 1.2576 AMD EPYC 7V12 … coeurs_effectifs 32.0 GHz 2.45 » ; aucun prix pour la carte seule. Or le texte dit : « louable le 16 novembre (offre 59431043, 1,108 USD/h) : relevé … : offre 59431043 à 1,2576 USD/h carte et 110 Go de stockage compris (1,108 USD/h la carte seule) ».

**Correction.** Facultatif : écrire « (1,108 USD/h la carte seule, relevé de la session du 16 novembre, non consigné) » ou citer la pièce qui porte ce taux, et préciser que le relevé est du 17 novembre à 00:25Z.

### 3. remarque — 31 ; 59-63 ; 70 ; 131

**Constat.** Hors de l'angle fidélité, mais visible dans le complément de la session. Selon le relevé cité, la règle « offre la moins chère qui passe » choisirait aujourd'hui la machine de l'Oregon (154960, 1,255 USD/h), pas celle du Texas (1,2576 USD/h). Le devis (« Hôte comme celui du Texas ») et le risque (b) ne le disent pas.

**Preuve.** Relevé : « offre 57349463 machine 154960 Oregon, US cout_110Go 1.255 … coeurs_effectifs 32.0 GHz 2.45 », avant « offre 59431043 … 1.2576 ». Les deux passent le filtre du § 2.4 (au moins 32 cœurs, au moins 2,4 GHz, au plus 1,6 USD/h). Risque (b) : « une autre machine qui passe le filtre n'a pas été éprouvée ».

**Correction.** Facultatif : une phrase au risque (b) ou au § 2 bis : « au relevé du 17 novembre, l'offre retenue serait celle de l'Oregon (même processeur, non éprouvée) ».

### 4. remarque — 102-103

**Constat.** La grandeur facultative suggérée par la contre-lecture (M-11) est reprise sans deux précisions. Le moment de la lecture (« lu après les deux verdicts ») n'y est pas. La définition des empreintes de suffixe (« écart 9 ») non plus.

**Preuve.** Rapport, M-11 : « le premier tour où les empreintes de suffixe (écart 9) de la confirmation diffèrent de celles de la relance, lu après les deux verdicts ». Addendum : « Information, sans effet sur la lecture : le rapport donne le premier tour où les empreintes de suffixe de la confirmation diffèrent de celles de la relance (graines identiques). »

**Correction.** Facultatif, mais à faire avant le scellement si on le fait : ajouter « (écart 9), lu après les deux verdicts ».

### 5. remarque — 76

**Constat.** Dans le devis, la dépense cumulée n'est pas mise à jour avec le taux carte et stockage ajouté juste au-dessus. Elle reste « plus 33 à 84,5 USD », alors que le bas de la fourchette serait 38 USD à 1,258 USD/h.

**Preuve.** L. 72 : « ≈ 38 à 43 USD à 1,258 USD/h (carte et stockage…) » ; l. 75-76 : « Dépense cumulée du témoin : 73,03 USD (séries 1 à 3 et relance) plus 33 à 84,5 USD ».

**Correction.** Facultatif : « plus 33 (carte seule) ou 38 (carte et stockage) à 84,5 USD ».

### 6. remarque — 1-7 ; 36 ; 145

**Constat.** Trois écarts mineurs, ni annoncés ni contraires au rapport. (1) L'en-tête est réécrit pour le scellement : « — brouillon 2 » retiré du titre ; la ligne d'état devient « scellé après contre-lecture (R2) » avec les deux brouillons archivés. (2) Au § 6, l'ordre des mots change : « le 27 novembre vers 17:44Z » devient « vers le 27 novembre 17:44Z ». (3) Le § 2.1 reprend mot pour mot la notation « [T] » du rapport, qui n'est pas définie dans l'addendum, lequel désigne ailleurs le texte par « l. » seul.

**Preuve.** Diff entre le brouillon 2 et la version à sceller, l. 1, 3-5 et 145 ; texte du rapport pour le § 6 : « soit le 27 novembre vers 17:44Z à c = 1,108 USD/h » ; addendum l. 36 : « écart à R3, [T] l. 69-71 ». La ligne 69 du texte porte bien le paragraphe R3. Échéances recalculées : 84,5/1,108 + 1 = 77,26 h, soit le 27 novembre 17:44Z ; 84,5/1,258 + 1 = 68,17 h, soit le 28 novembre 02:50Z (fin de jour à Paris = 30 novembre 23:00Z) : exactes.

**Correction.** Aucune nécessaire. Facultatif : nommer « en-tête » parmi les changements de la section « Contre-lecture ».

## Angle : règle de lecture et ordre (R3, R4, R1) — bloquant : oui

Il ne faut pas sceller l'addendum en l'état (prereg/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation.md), car il ne protège pas contre un run qui viserait un signe. La règle du verdict retenu (§ 3) est symétrique, fixée d'avance et fidèle aux l. 329-338 et au nœud 5. En revanche, trois sorties restent ouvertes après la lecture du verdict à 36 tours.

(a) Le mot de lancement, qui accepte aussi les paramètres du § 2, n'est reçu qu'à l'étape 4, donc après la lecture. « Mot non donné » est une cause admise de non-lancement, et toute l'étape 2 peut glisser après la lecture. Cela contredit le § 2.1 (« engagée quel que soit le verdict ») et rouvre M-1.

(b) Une tentative décidée après la lecture, par exemple après une chute de la garde de durée du pilote, peut prendre le nom de « confirmation » et devenir le verdict retenu si K′ ≥ 71.

(c) L'exception « défaut technique » n'est pas bornée. Elle peut naître de la mention « trop laid », lue sur R_att et J, donc d'un résultat négatif. Elle mène à une correction décidée verdict connu, sans statut fixé, et laisse ouverte une relecture des 36 tours par un code corrigé.

Le reste est à corriger ou à noter :
- délai de 24 h et échéance sans point de départ ;
- empreintes de suffixe sans borne de lecture, alors que M-11 en donnait une ;
- K′ = 36 écrit avant la lecture ;
- lecteur de la confirmation non tenu à l'écart du premier verdict.

Les corrections mot pour mot sont données pour chaque constat. Aucune ne touche une hypothèse, un seuil ou un critère gelé.

### 1. bloquant — § 6, l. 160-167 (étape 4 « mot de Lazar reçu » ; « Si une pièce de l'étape 2 ne peut être faite avant la lecture, elle est faite après » ; « mot non donné ») ; § 2, titre l. 35 (« dont le mot les accepte ») ; contre § 2.1 l. 38 (« engagée quel que soit le verdict à 36 tours »)

**Constat.** Le lancement n'est pas fixé avant la lecture. Le mot de lancement (condition 7) n'est reçu qu'à l'étape 4, donc après le verdict à 36 tours. Ce mot accepte aussi les paramètres du § 2 (plafond de 1 800 s, filtre, crédit), qui restent ainsi ouverts jusqu'après la lecture. Le dernier paragraphe fait de « mot non donné » une cause admise de non-lancement, sans autre effet que de retenir le verdict à 36 tours. Il laisse aussi glisser toute l'étape 2 après la lecture, avec pour seule obligation de le dire. Cela contredit le § 2.1, qui fonde la compatibilité avec R3 sur un engagement indépendant du verdict. Cela rouvre exactement le risque M-1 : sur un « effet reproduit » à 36 tours, on ne lance pas, et ce verdict est retenu ; sur un « non reproduit », on lance, et si K′ ≥ 71 c'est la confirmation qui est retenue. C'est un run qui viserait un signe. Le risque (d) aggrave le défaut : mêmes graines, donc qui a lu les 36 tours connaît en partie la trajectoire de la confirmation. Le crédit et l'échéance sont aussi en partie à la discrétion de Lazar après la lecture : recharge, ligne de GO à renouveler (« au-delà, une ligne neuve »). Enfin, l'addendum 6, § 6, veut que la demande cite le relevé 9′, qui n'existe qu'à l'étape 4.

**Preuve.** Addendum 7, l. 163 : « 4. crédit relevé (9′), mot de Lazar reçu, création » ; l. 165-167 : « Si une pièce de l'étape 2 ne peut être faite avant la lecture, elle est faite après […] Si la confirmation n'est pas lancée (mot non donné, aucune offre, crédit, échéance, défaut du § 3) […] le verdict retenu reste celui à 36 tours » ; l. 38 : « elle est engagée quel que soit le verdict à 36 tours » ; note 2026-11-17-0008 : la ligne de GO « ne vaut pas mot de lancement » ; [T] l. 69-71 ; addendum 6, l. 78-79.

**Correction.** (1) § 2, titre, remplacer « dont le mot les accepte » par : « dont le mot, reçu avant la lecture du verdict à 36 tours (§ 6, étape 2), les accepte ou les refuse en bloc, sans les modifier ».
(2) § 6, remplacer de « 2. **avant la lecture du verdict à 36 tours** : » jusqu'à la fin de la section par :
« 2. **avant la lecture du verdict à 36 tours, qui attend que tout ce point soit fait** :
   - la ligne de GO inscrite sur `main` ;
   - les pièces de lancement écrites (conduite `lancer-conduite-v15.py`, poste `poste-hetzner-v13.sh` et son
     constructeur, manifeste v7). Elles sont contre-lues (R2) par un lecteur neuf, puis scellées. Ce lecteur vérifie
     qu'elles ne diffèrent de la conduite v13, du poste v12 et du manifeste v6 que par ce que cet addendum nomme :
     `lanceur_v21`, `t_max_pilote_s=1800` exigé, aucune `relance_seule`, aucune instance antérieure, B = 85, filtre
     du § 2.4, garde du commit `873ab00c`, GO neuf et empreinte de cet addendum vérifiée dans son objet ;
   - la demande du mot de lancement (condition 7) envoyée à Lazar, avec le § 2 bis, les risques du § 5, le tirage
     attendu sur la carte et un relevé de crédit indicatif (c₀, o, S) ; le relevé de 9′ fait à l'étape 4 est consigné
     dans l'ordre de lancement sans nouveau mot ;
   - **le mot de Lazar reçu** : il accepte ou refuse en bloc la confirmation et les paramètres du § 2 tels que scellés ;
     une modification est un écart, par un addendum neuf scellé avant la lecture ;
3. le verdict à 36 tours prononcé et scellé (R13) ;
4. crédit relevé (9′), poste lancé au plus tard 24 h après le scellement du verdict à 36 tours, création.

Aucune pièce de l'étape 2 n'est faite après la lecture. Si l'une ne peut être faite, ou si le mot est refusé, avant la
lecture : « confirmation non lancée », rapportée avec sa cause et la mention « avant la lecture » ; le verdict retenu est
celui à 36 tours. Après la lecture, la confirmation ne manque que par une cause fixée ici et constatée sans décision :
aucune offre conforme (§ 2.4), crédit 9′ non tenu au relevé (§ 2.5), échéance (condition 2), défaut du § 3, ou une ligne
de la liste d'arrêt. Le rapport du témoin le dit avec sa cause, et le verdict retenu reste celui à 36 tours. Toute autre
absence de lancement ou tout arrêt décidé après la lecture (mot retiré, recharge suspendue, ligne de GO non renouvelée,
autre motif) est un écart à cet addendum : nœud ; rapporté « décidé après la lecture du verdict à 36 tours ». Le verdict
retenu reste alors celui à 36 tours, avec cette réserve. »

### 2. bloquant — § 2.3, l. 53-54 ; § 3, l. 101 (« Aucune autre série sans nouvelle décision de Lazar et nouvel addendum ») ; règle du verdict retenu, l. 92-97

**Constat.** Une tentative décidée après la lecture peut devenir le verdict retenu. Après une chute de la garde de durée du pilote, ou toute fin de série, une nouvelle tentative passe par « décision de Lazar et nouvel addendum » postérieurs à la lecture. Rien n'interdit à cet addendum de l'appeler « la confirmation », et la règle du § 3 retient « la confirmation » dès que K′ ≥ 71. Un hôte lent au pilote est plausible : la machine de la relance aurait fait tomber la garde. Lazar déciderait alors, verdict connu, de retenter ou non sur un autre hôte. Si la retentative atteint 71 tours, son verdict remplace celui à 36 tours. La règle du verdict retenu dépend donc d'une décision prise sur le signe. Le texte exige qu'un nouvel addendum « dise » qu'il est postérieur à la lecture, mais n'attache aucun effet à cette mention.

**Preuve.** Addendum 7, l. 53-54 : « Aucune nouvelle tentative sans nouvelle décision de Lazar et nouvel addendum, qui diraient qu'ils sont postérieurs à la lecture du verdict à 36 tours » ; l. 92-95 : « si la confirmation compte K′ ≥ 71, son verdict, quel qu'il soit […] est retenu » ; § 1, l. 20-23 : t de la relance 2 276,4 s > 1 800 ; contre-lecture, M-2 : « Lazar déciderait alors, en connaissant le verdict, de tenter ou non un autre hôte ».

**Correction.** (1) § 2.3, remplacer « Aucune nouvelle tentative sans nouvelle décision de Lazar et nouvel addendum, qui diraient qu'ils sont postérieurs à la lecture du verdict à 36 tours. » par : « Aucune nouvelle tentative sans nouvelle décision de Lazar et nouvel addendum, qui diraient qu'ils sont postérieurs à la lecture du verdict à 36 tours ; une telle tentative n'est jamais retenue pour l'étape 1 par la règle du § 3 : son verdict, s'il y en a un, est rapporté à côté, avec la mention « décidée après la lecture ». »
(2) § 3, remplacer « - Aucune autre série sans nouvelle décision de Lazar et nouvel addendum. » par : « - Aucune autre série sans nouvelle décision de Lazar et nouvel addendum. « La confirmation », dans la règle du verdict retenu, désigne la seule série de cet addendum, lancée selon le § 6 (et sa relance, l. 371). Une série, une tentative ou une relecture décidée après la lecture du verdict à 36 tours n'est jamais retenue pour l'étape 1 ; elle est rapportée à côté, avec la mention « décidée après la lecture », sans changer le verdict retenu. » (Autre voie, qui exige un mot de Lazar avant le scellement : fixer dès maintenant une seconde tentative sur une autre machine après une chute de la garde du § 2.3, même poste, même B, D cumulée. C'est l'option ouverte par M-2.)

### 3. bloquant — § 3, l. 82-85 (exception « défaut technique établi par la lecture à 36 tours »)

**Constat.** L'exception n'est pas bornée et peut servir de porte de sortie liée au signe. (i) Rien ne définit « défaut technique », ni ce qui l'établit. Le texte dit qu'un suffixe non appliqué donnerait « effet non reproduit », signalé seulement par la mention « trop laid » de l'audit, une condition lue sur R_att et J. Un lecteur peut donc tirer un « défaut d'exécution » d'un motif de notes, et seulement quand l'issue est négative. (ii) Une fois le défaut établi : nœud, puis correction par un addendum postérieur à la lecture. La relance de la confirmation dépend alors d'une décision prise verdict connu. Rien ne dit si cette confirmation corrigée reste éligible au verdict retenu. (iii) Pour un défaut du code de lecture, le sort du verdict à 36 tours n'est pas fixé. Une relecture avec un code corrigé, faite après avoir vu l'issue, est une analyse post hoc qui pourrait devenir le verdict retenu. Cela heurte R1 et [T] l. 334.

**Preuve.** Addendum 7, l. 82-85 : « si cette lecture établit un défaut technique d'un code que la confirmation emploie (lanceur, instance, exécution, journaliseur, lecture), la confirmation n'est pas lancée avec ce code ; nœud ; toute correction passe par un addendum neuf » ; [T] l. 300-304 : « Un suffixe non appliqué donnerait un rappel R_att haut et un taux J bas, donc « effet non reproduit », signalé seulement par la mention « trop laid » de l'audit » ; [T] l. 351-353 : la mention « à examiner » « n'ouvre pas d'autre examen » ; [T] l. 334.

**Correction.** § 3, remplacer de « Seule exception, fixée maintenant : » à « qui dit qu'il est écrit après cette lecture. » par :
« Seule exception, fixée maintenant : un défaut technique d'un code que la confirmation emploie (lanceur, instance,
exécution, journaliseur, lecture), établi par cette lecture sans aucune valeur de note. Ce défaut ne peut être que :
la chute d'une garde nommée, un refus de `lecture_v8.valider` ou de l'assemblage, une erreur d'exécution du code de
lecture, ou l'échec de l'un des trois contrôles de l'audit de symétrie ([T] l. 342-346), le contrôle en cause étant
nommé. Ne sont pas un défaut : la mention « à examiner » ([T] l. 347-353), toute valeur ou tout motif de R_att, R_def,
R_std, J, P1, P2 ou P3, et l'issue du verdict. Ce qui précède vaut quelle que soit l'issue à 36 tours. En cas de
défaut, la confirmation n'est pas lancée avec ce code. Seul le code en cause est corrigé, par un addendum neuf qui dit
qu'il est écrit après cette lecture et ne change rien d'autre, contre-lu (R2). La confirmation est alors lancée avec ce
code selon cet addendum, quel que soit le verdict à 36 tours, si l'échéance le permet ; elle reste soumise à la règle
du verdict retenu. Sinon : « confirmation non lancée (défaut du § 3) ». Toute autre suite est décidée après la lecture
(§ 6). Un défaut du code de lecture laisse le verdict à 36 tours tel qu'il a été prononcé et scellé : aucune relecture
de la relance par un code corrigé n'est retenue pour l'étape 1 ; elle est rapportée à côté, avec la mention « décidée
après la lecture ». »

### 4. à corriger — § 2.4, l. 62-63 (« Aucune offre conforme en 24 h ») ; § 6, condition 2, l. 144-146 (échéance)

**Constat.** Le délai de 24 h n'a pas de point de départ. Le moment du lancement du poste après la lecture est donc libre. Laisser filer le temps jusqu'à l'échéance (création au plus tard vers le 27 novembre) produit une « confirmation non lancée (échéance) » sans décision explicite. C'est une sortie discrétionnaire qui passe pour une cause technique.

**Preuve.** l. 62-63 : « Aucune offre conforme en 24 h : rien ne tourne ; « confirmation non lancée » » ; l. 144-146 : « création au plus tard à l'échéance moins ((B − 0,5)/c + 1) h […] au-delà, une ligne neuve ».

**Correction.** § 2.4, remplacer « Aucune offre conforme en 24 h : » par : « Aucune offre conforme dans les 24 h qui suivent le lancement du poste, lui-même au plus tard 24 h après le scellement du verdict à 36 tours (§ 6, étape 4) : ». Dans la condition 2, après « au-delà, une ligne neuve », ajouter : « ; une échéance manquée parce que le poste a été lancé après le délai du § 6, étape 4, ou une ligne neuve refusée, est une décision postérieure à la lecture (§ 6) ». 

### 5. à corriger — § 3, l. 102-103 (information sur les empreintes de suffixe)

**Constat.** La contre-lecture (M-11) proposait cette grandeur « lue après les deux verdicts ». Le texte scellé a perdu cette borne. Si l'on compare les empreintes pendant le run de confirmation (celles de la relance sont transférées), on sait dès les premiers tours que la confirmation rejoue la trajectoire de la relance, donc une partie de son issue, au moment où des décisions restent possibles (crédit, recharge, arrêt).

**Preuve.** Addendum 7, l. 102-103 : « le rapport donne le premier tour où les empreintes de suffixe de la confirmation diffèrent de celles de la relance (graines identiques) » ; contre-lecture, M-11 : « lu après les deux verdicts ».

**Correction.** Remplacer « le rapport donne le premier tour où les empreintes de suffixe de la confirmation diffèrent de celles de la relance (graines identiques). » par : « le rapport donne le premier tour où les empreintes de suffixe de la confirmation diffèrent de celles de la relance (graines identiques), calculé et lu après le scellement des deux verdicts ; aucune comparaison de ces empreintes n'est faite pendant la confirmation. »

### 6. remarque — § 3, l. 81-82 (« K′ = 36, l. 332, 338 »)

**Constat.** Le texte fixe K′ = 36 avant la lecture, d'après le bilan technique. Or K′ est établi par la lecture (`valider`, garde de fin de run, tours complets). Écrire 36 préjuge du travail du lecteur R13. La règle du verdict retenu est inchangée tant que K′ ≤ 70.

**Preuve.** l. 81-82 : « c'est le verdict du texte pour les séries 1 à 3 et la relance (K′ = 36, l. 332, 338) » ; [T] l. 258-260 et 307.

**Correction.** Remplacer « (K′ = 36, l. 332, 338) » par « (K′ établi par cette lecture, 36 tours complets au bilan ; l. 332, 338) ».

### 7. remarque — § 3, l. 86 (lecteur de la confirmation)

**Constat.** Le lecteur de la confirmation est distinct du premier, mais rien ne l'empêche de connaître le verdict à 36 tours avant de prononcer. Les critères sont mécaniques, mais l'audit de symétrie (R4) comporte des jugements (défaut, « à examiner »).

**Preuve.** l. 86 : « par un lecteur neuf (R13), qui n'est pas celui du verdict à 36 tours ».

**Correction.** Après « qui n'est pas celui du verdict à 36 tours », insérer « et qui ne reçoit ni ce verdict ni son rapport avant d'avoir scellé le sien ».

### 8. remarque — § 3, l. 95-97 (« K′ ≤ 70 … le verdict retenu est celui à 36 tours »)

**Constat.** Une confirmation de K′ compris entre 37 et 70 tours, plus longue que la relance, n'est jamais retenue. Le choix est fixé d'avance, ne dépend d'aucune issue et reste fidèle aux régimes de [T] l. 331-332 : il est symétrique. Il est seulement coûteux en information. Pour le reste, la règle couvre sans ambiguïté K′ ≥ 71 (quel que soit le verdict), K′ ≤ 70, non interprétable, pas de run principal, sonde orientée, P2 et P3, relance de la confirmation (l. 371), garde du pilote, absence d'offre, crédit, échéance et contrôle du juge. La seule réserve est le croisement « K′ ≥ 71 sans verdict » (refus de `valider` ou de l'assemblage) : le texte l'envoie à « pas de verdict », donc aux 36 tours, ce qui se tient.

**Preuve.** l. 92-100 ; [T] l. 329-338.

**Correction.** Aucune ; à garder tel quel. Facultatif, pour lever le croisement : après « quel qu'il soit (« effet reproduit », « effet non reproduit » ou « non interprétable ») », insérer « (un refus de `valider` ou de l'assemblage n'est pas un verdict : « pas de verdict ») ».

## Angle : chiffres et code — bloquant : non

J'ai refait les chiffres de l'addendum 7 avec le code et les pièces : tous tiennent, et rien n'empêche de le sceller. Il reste une correction de provenance, sur le taux « 1,108 USD/h la carte seule », et cinq remarques.

**Règle du nombre de tours.** `nombre_de_tours(85, 8, 1.6, 1800)` donne H = 41,875 h et K = 72. La borne exacte est D ≤ 8,76 pour K = 72 (le texte écrit 8,7, valeur prudente) et D ≤ 9,68 pour K = 71 (le texte écrit 9,6). À D = 9,7, K = 70. Avec c = 1,8, D = 5 et t = 1 800 : K = 67, comme écrit. Pour un hôte stable à c = 1,108 et D = 4, K reste à 72 jusqu'à t = 2 786 s (« ≈ 2 700 » dans le texte).

**Durées** (champs `tour` et `duree_s` seulement), tous concordants :
- Relance (`6c445f3e…`) : 36,5 à 132,8 min ; tours 0 à 29 jusqu'à 127,2 min ; tours 30, 33, 34 et 35 à 72,3, 66,8, 45,2 et 46,8 min ; 48,7 h au total.
- Tours 0 et 1 de la relance : 2 187,1 et 2 365,6 s, moyenne 2 276,4 s.
- Texas, tours 0 à 7 (`9ff59e4b…`) : 21,7 à 26,4 min, moyenne 1 411,5 s.
- Pilote de la série 3 (`2cac2458…`) : t = 1 315,99 s, et 1 800 = 1,368 × t.
- 72 tours au Texas : 28,2 h, 32,5 h avec la marge de 1,15.
- Hôte à t = 1 800 s qui croîtrait comme la relance : 20 premiers tours en 17,3 h.

**Devis (§ 2 bis).** 30 à 34 h ; 33 à 38 USD à 1,108 USD/h et 38 à 43 USD à 1,258 USD/h. Une recharge de 5 USD toutes les 3,1 à 4,5 h. Arrêt à B − 2 vers 48 à 49 tours à 1,108 et vers 39 à 1,6 : concordant.

**Crédit (§ 2.5).** 0,75 + 1,5 + 11,5 = 13,75 h ≤ 14 h. S = 14 × (1,7 + 0,11) = 25,3 USD, donc ≥ 25 USD.

**Échéance de création** (fin de jour à Paris, 22:59:59Z) : 27 novembre 17:44:10Z à c = 1,108 (exact) ; 28 novembre 02:49:47Z à c = 1,258 et 02:48:30Z à 1,2576. Le « vers 02:50Z » du texte arrondit donc une date limite vers le haut.

**Dépense de la relance.** D = 73,026 USD (`bilan-conduite-v5.json`, champ `depense` seul).

**Ligne de GO (§ 6).** Elle passe `ligne_go`, `b_de_l_objet` (B = 85) et `verifier_go` à 85 ; `verifier_go` refuse à 90 et à 75, comme il faut.

**Différence entre lanceur_v21 et lanceur_v20.** Seulement la docstring, `VEILLEUR_MODULE`, deux messages, le champ `t_max_pilote_s=None` et une garde de quatre lignes. La garde est placée après la règle et après le contrôle K < 20, avant le manifeste « règle » ; tout arrêt passe par `_finir`.

**Essais.** La commande demandée donne 9 passés, 221 désélectionnés, en 95 s. La paire v21 + reprise_relance compte 228 essais, ce qui s'accorde avec « 227 passés, 1 sauté ».

**Empreintes vérifiées** : 75cf4049 (identique au commit 873ab00c et au `.sha256`), 36573ae2, fb6c2f34, f9c8c66e (devis v4), f1c2ca52 (contre-lecture), 674d8f14 (brouillon 2), 546aa0bc, 9a879463, 972928bb, a902256b, 6c445f3e, 9ff59e4b, 2cac2458, 3e992ff3 (bilan).

**Correction de provenance** (à faire, non bloquante) : le taux « 1,108 USD/h la carte seule » et la date « louable le 16 novembre » sont rattachés au relevé `a902256b…`, qui ne les contient pas.

**Remarques :**
- Le code prend pour c le taux carte et stockage de l'instance (`dph_total`), jamais 1,108 : les chiffres donnés à 1,108 sont optimistes. Par exemple, l'arrêt à B − 2 tomberait vers 45 tours à 1,258.
- Au relevé, le filtre choisirait l'Oregon (1,255), et non le Texas.
- Les essais complémentaires n'ont ni empreinte ni `.sha256`, et ne sont pas dans le commit `873ab00c`.
- Le message d'arrêt du code finit par « ; nœud », alors que le § 2.3 dit que la chute met fin à la série.
- L'objet de la ligne de GO ne doit porter aucune autre parenthèse « (B = … ».

Je n'ai rien modifié dans le dépôt et je n'ai lu aucune pièce sous cloison.

### 1. à corriger — § 1, l. 30-31 (et § 2 bis l. 72, § 5 (a), § 6 l. 145)

**Constat.** Le taux « 1,108 USD/h la carte seule » et « louable le 16 novembre » sont rattachés au relevé `a902256b…`, qui ne les contient pas (R6).

**Preuve.** `runs/temoin-bailey-v1-20261111/releve-offres-processeur-20261117-0025.txt` (sha256 a902256be46b…, vérifiée) daté du 2026-11-17T00:25:54Z ne donne que `cout_110Go` (Texas 1.2576, Oregon 1.255, etc.), sans `dph_total` ni prix de la carte seule. Aucune autre pièce du dépôt (recherche de « 1,108 / 1.108 ») ne porte ce chiffre. L'offre v11 (`23281d5b…`) donne pour le Texas dph_total 1,196 le 12 novembre.

**Correction.** Écrire « 1,108 USD/h la carte seule : relevé de la session, non consigné » (forme admise par M-5), ou consigner une pièce scellée qui porte `dph_total` et `storage_cost` de l'offre 59431043. Mettre le 17 novembre pour la date du relevé, ou dire que le 16 novembre n'a pas de pièce.

### 2. remarque — § 2 bis, § 5 (a), § 6 (échéance)

**Constat.** Le code ne voit jamais le taux « carte seule » 1,108 : c est lu sur l'instance (`taux_horaire` : `dph_total`), et § 2.2 et § 2.4 définissent c comme le taux carte et stockage. Les chiffres donnés à 1,108 sont donc optimistes.

**Preuve.** `lanceur_v21.py` l. 430-431 (`dph_total` de `show instance`) et l. 1682-1691 (c relevé, puis passé à `verifier_echeance`). À c = 1,258, l'arrêt à B − 2 d'un hôte à t = 1 800 s qui croît comme la relance tombe vers 45 tours, et non 48 (simulation : pente 180,5 s par tour mise à l'échelle 1 800/2 276,4, soit 142,8 s ; 49 tours à 1,108, 45 à 46 à 1,258, 39 à 1,6). La date de l'échéance prise à 1,108 est plus précoce : elle reste donc prudente.

**Correction.** Facultatif : donner aussi « ≈ 45 tours à 1,258 USD/h » au § 5 (a) et au § 2 bis, ou dire que 1,108 n'est qu'un plancher qui n'est pas le c de la règle.

### 3. remarque — § 6, l. 145

**Constat.** « vers le 28 novembre 02:50Z à c = 1,258 » arrondit vers le haut une date limite. La limite exacte tombe avant 02:50Z.

**Preuve.** `echeance_epoch("2026-11-30")` donne 2026-11-30 22:59:59Z. `verifier_echeance` (B = 85, marge 0,5, transfert 3 600 s) : 2026-11-27 17:44:10Z à c = 1,108 (exact) ; 2026-11-28 02:49:47Z à c = 1,258 ; 02:48:30Z à c = 1,2576 (le taux relevé). Contrôlé : la garde passe 1 s avant la limite et tombe 60 s après.

**Correction.** Écrire « avant le 28 novembre 02:48Z à c = 1,2576 USD/h (relevé) », ou garder la seule date à 1,108, qui est la plus précoce.

### 4. remarque — § 2 bis, l. 70 ; § 2.4

**Constat.** Au relevé, le filtre « offre la moins chère qui passe » choisirait l'Oregon (offre 57349463, 1,255) et non le Texas (1,2576). Le devis « hôte comme celui du Texas » vaut pour un hôte dont la durée n'a pas été mesurée (même processeur).

**Preuve.** Relevé `a902256b…` : Oregon cout_110Go 1.255, Texas 1.2576, même AMD EPYC 7V12 à 32 cœurs effectifs et 2,45 GHz. Les autres offres sont exclues par les cœurs, la fréquence ou la borne de 1,6.

**Correction.** Une demi-phrase au § 2 bis ou au risque (b) : « au relevé, l'offre retenue serait celle de l'Oregon, même processeur, durée non éprouvée ».

### 5. remarque — § 4, l. 117-118

**Constat.** Les essais complémentaires sont cités sans empreinte, et ils ne sont pas dans le commit `873ab00c` cité pour le code.

**Preuve.** `tests/test_temoin_bailey_condition6_v21_complements.py` : sha256 82ef2fa0a9ef…, aucun `.sha256` compagnon, ajouté au commit c44c6d65 (HEAD). Le commit 873ab00c contient `lanceur_v21.py` (75cf4049…, vérifiée) et `test_..._v21.py` (36573ae2…, vérifiée).

**Correction.** Ajouter « (`82ef2fa0…`, commit c44c6d65) », et sceller le fichier avec un `.sha256` (R6).

### 6. remarque — § 2.3 ; lanceur_v21.py l. 1782-1783

**Constat.** Le message d'arrêt du code finit par « ; nœud », alors que § 2.3 dit que la chute met fin à la série (« confirmation non courue (garde de durée du pilote) »). L'écart ne porte que sur le libellé ; le comportement est conforme (arrêt avant le principal, `_finir`, aucune reprise).

**Preuve.** `bilan["arret"] = f"durée de tour du pilote au-delà du plafond (… s > … s) : arrêt avant le run principal ; nœud"`.

**Correction.** Aucune au code (il est scellé). Le rapport traduit ce libellé selon le § 2.3 ; on peut le dire en une demi-phrase au § 4.

### 7. remarque — § 6, condition 2

**Constat.** La ligne de GO décrite au § 6 passe les gardes. Une condition reste non écrite : l'objet ne doit porter aucune autre parenthèse « (B = … », par exemple un rappel du B = 75 des séries 1 à 3.

**Preuve.** Ligne construite selon le § 6 (`GO-2026-11-17-02`, calcul, objet citant l'empreinte de l'addendum, `fb6c2f34`, `f9c8c66e`, « (B = 85, garde d'horloge à B − 2) », 90 USD, 2026-11-30). Résultats : `ligne_go` lit le type « calcul », le plafond « 90 USD » et l'échéance « 2026-11-30 » ; `b_de_l_objet` = 85,0 ; `verifier_go(go, 85)` passe ; `verifier_go` à 90 ou à 75 refuse ; `verifier_non_revoque` passe. La forme du brouillon 2 (« … prolongé par l'addendum 7 (B = 85 … ») passe aussi. Avec un « (B = 75) » de plus dans l'objet : refus « ne fixe pas B de façon unique ». L'identifiant `GO-AAAA-MM-JJ-NN` suit la forme exigée par `.claude/hooks/garde_calcul.py` l. 52-53.

**Correction.** Facultatif : « l'objet ne porte aucune autre mention « (B = … » ».
