# Addendum 7 au préenregistrement du témoin de Bailey (`prereg/temoin-attaque-publiee-bailey-v1.md`, `fb6c2f34…`) — run de confirmation au régime complet (72 tours), décidé et lancé avant toute lecture ; les deux verdicts lus après sa clôture

16-17 novembre 2026, scellé après contre-lecture (R2). Session « attaquant informé » (`session_01XJ6MgnEhQMZteN9F8a1BST`),
branche `claude/compassionate-meitner-d4ryyk`. Brouillons archivés tels quels (R12) :
`brouillons/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation-brouillon1.md` et `…-brouillon2.md` (contre-lu) ;
états intermédiaires de ce fichier : commits `c44c6d65`, `0c373143` et `11954d70`. Le préenregistrement et ses addenda 1
à 6 restent tels quels ; en cas de conflit, le préenregistrement prime et l'écart est un nœud. **Écrit et scellé avant
toute lecture** : aucune note de sonde ni de juge du témoin n'a été lue, par aucune session.

## 1. Pourquoi
La relance seule (addenda 5 et 6) a fini le 15 novembre vers 11:47Z (instance détruite à 11:47:37Z,
`runs/temoin-bailey-v1-20261111/sortie-conduite-v13/poste-v5.json`) par la garde de dépense (D = 73,026 USD sur B = 75) :
**36 tours complets**, aucune autre garde tombée, transfert complet, instance détruite
(`runs/temoin-bailey-v1-20261111/sortie-conduite-v13/bilan-conduite-v5.json`, `3e992ff3…`). Dossier de lecture assemblé :
`runs/temoin-bailey-v1-20261111/lecture-assemblee-v1/` (45 fichiers scellés vérifiés le 16 novembre). Le texte lit ce run
comme un run tronqué (36 tours complets au bilan ; K′ établi par la lecture), au régime réduit (l. 165, 332, 338). Le
verdict n'est pas lancé.

Choix soumis à Lazar avant toute lecture (`registres/passations/2026-11-16-2354-bailey-choix-1-suspendu-question-ordre.md`,
`df9a3eda…`) ; mot de Lazar, verbatim : « go 2 puis 1 »
(`registres/passations/2026-11-16-2355-decision-lazar-bailey-2-puis-1.md`, `93494ff9…`) : un run neuf de 72 tours, au
régime publié, engagé avant la lecture du verdict à 36 tours.

**Ordre de lecture.** La session avait présenté à Lazar l'ordre « addendum scellé, verdict à 36 tours, puis lancement ».
La contre-lecture et deux vérifications adverses (section « Contre-lecture ») ont montré que toute lecture avant la fin
de la confirmation laisse des décisions (mot de lancement, crédit, délais, offre, relance, reprise, lecteurs) dépendre du
résultat lu. Choix de la session sous l'autonomie en cours (`GO-2026-11-16-04`, `GO-2026-11-17-01`), consigné
(`registres/passations/2026-11-17-0052-choix-session-bailey-lecture-apres-cloture.md`, `74df1fbf…`) et rapporté à Lazar
dans le message qui annonce le scellement : **aucune note n'est lue avant la clôture de la confirmation ; les deux
verdicts sont lus ensuite** (§ 3). C'est un écart à l'ordre que consignait la note du « go 2 puis 1 » ((i) addendum,
(ii) verdict à 36 tours, (iii) run neuf ; `93494ff9…`) ; il est soumis à Lazar avec la demande du mot de lancement
(condition 7). Lazar peut ordonner une lecture plus tôt : ce serait un écart à cet addendum, par un addendum neuf, scellé
avant cette lecture. Dès qu'une note ou un verdict du témoin est lu avant la clôture, par qui que ce soit (lecture
ordonnée, ou faite malgré le § 3), c'est consigné avec ce qui a été vu ; toute décision prise ensuite sur la confirmation
(fin, seconde tentative, relance, reprise, mise en place refaite, mot, crédit) est rapportée « décidée après une lecture », et le verdict retenu
porte cette réserve partout où il est cité.

**Lenteur de la relance** (champs techniques seulement) : tours 0 à 35 de 36,5 à 132,8 min
(`runs/temoin-bailey-v1-20261111/sortie-conduite-v13/principal-relance/transfert-1/sortie-durees-v3.jsonl`, `6c445f3e…`) :
croissance presque régulière des tours 0 à 29 (36,5 à 127,2 min), puis tours 30, 33, 34 et 35 plus courts (72,3 ; 66,8 ;
45,2 ; 46,8 min) ; 48,7 h pour 36 tours ; tours 0 et 1 : 2 187,1 et 2 365,6 s (moyenne 2 276,4 s). Tours 0 à 7 de la
première exécution de la série 3, sur une autre machine (Texas, machine 146915), 21,7 à 26,4 min, sans croissance sur ces
huit tours (`…/sortie-conduite-v11/reprise-v10-2/principal/transfert-1/sortie-durees-v3.jsonl`, `9ff59e4b…`) ; t du
pilote de la série 3 : 1 315,99 s (`…/sortie-conduite-v11/reprise-v10-2/pilote/transfert-1/sortie-durees-v3.jsonl`,
`2cac2458…`). Diagnostic en lecture seule du 15 novembre
(`runs/temoin-bailey-v1-20261111/diagnostic-hetzner-v1-sortie.txt`, `9a879463…`) : processus d'exécution à 576 % de
processeur, carte à 0 % ; ≈ 16 min entre la sauvegarde d'une sonde et celle des paramètres, ≈ 1 h 30 entre ces
paramètres et la sonde suivante : la partie lente est sur le processeur (lecture de la session, non établie :
l'entraînement de la sonde sur la banque qui grossit, ou une charge variable de l'hôte — charge moyenne 16,3 au
diagnostic ; tours 30, 33, 34 et 35 plus courts). La machine 146915 du Texas porte un AMD EPYC 7V12, 32 cœurs effectifs,
2,45 GHz ; relevés des offres : `runs/temoin-bailey-v1-20261111/releve-offres-processeur-20261117-0025.txt`
(`a902256b…` ; Texas, machine 146915, 1,2576 USD/h, et Oregon, machine 154960, 1,255 USD/h, carte et 110 Go de stockage
compris, même processeur) et `…/releve-offres-filtre-addendum-7-20261117-0051.txt` (`e99a2d92…` ; au filtre du § 2.4 :
deux offres, Texas 1,2816 USD/h (machine 146917, autre que la machine 146915 de la série 3, même processeur, durée de
tour non éprouvée) et Caroline du Nord 1,5505 USD/h (machine 151320, AMD EPYC 7763) ; ni la machine 146915 ni celle de
l'Oregon n'y figurent). Les offres changent d'un relevé à l'autre. Les caractéristiques du processeur de la machine de
la relance (Suède, offre 58516569, `offre-choisie-v12.json`, `972928bb…`) ne sont pas relevées : rien n'établit que le
filtre du § 2.4 l'aurait exclue.

## 2. Écarts : principe décidé par Lazar (« go 2 puis 1 ») ; B = 85 par son mot du 17 novembre (ligne de GO) ; crédit par la recharge automatique seule (lecture par la session de son mot du 17 novembre, acceptée ou refusée avec le mot de lancement) ; plafond de durée, seconde tentative (§ 2.3), filtre et modalités du § 2.5 : calcul de la session, soumis à Lazar avec la demande du mot de lancement (condition 7), qui les accepte ou les refuse en bloc, sans les modifier
1. **Run de confirmation (écart à R3, texte l. 69-71, à la liste d'arrêt, à l'addendum 4, § 2.2, et à l'addendum 5,
   § 4 : une série nouvelle après la relance, sur nouvelle décision de Lazar et par cet addendum).** Une série neuve,
   **décidée, scellée et lancée avant toute lecture** : ce qui la rend compatible avec l'objet de R3 (aucun résultat
   connu ne la motive : aucune note du témoin n'a été lue, et aucune ne l'est avant sa clôture, § 3). Tout du texte
   s'applique sans changement : hypothèse, prédictions, métriques, seuils, population, juge, modèle, bras, graines
   (pilote 1394228342, run principal 1865327867), critères de lecture gelés, liste d'arrêt (pilote, au plus une
   reprise ; règle ; run principal ; au plus une relance), audit de symétrie. La relance de la liste d'arrêt (l. 371)
   est jouée par la conduite sur la même instance quand le code le permet ; si l'instance est perdue, par le chemin de
   l'addendum 5 (relance seule : pièces neuves contre-lues (R2), mot de Lazar), sans nouvel addendum si le code ne
   change pas. Une mise en place tombée peut être refaite (l. 363 ; addendum 5, § 4 : conduite et script de poste neufs
   (R12), mot de Lazar ; même poste de dépense : D cumulée, même B). Dans tous ces cas, avant la clôture (§ 3). Code : celui de l'addendum 5, plus la garde du point 3.
2. **Poste neuf, B neuf (écart au texte, l. 249-251 et 374).** La série de confirmation est un poste neuf : D compte de
   zéro à sa première instance ; **B = 85 USD**, garde à B − 2. Pourquoi 85 : la règle donne K = 72 dès que
   c ≤ 1,6 USD/h (carte et stockage, borne du § 2.4), t ≤ 1 800 s (garde du § 2.3) et D ≤ 8,7 USD au calcul
   (`analyse_v3.nombre_de_tours(85, 8, 1.6, 1800)` : H = 41,9 h, K = 72 ; K = 71 tant que D ≤ 9,6 USD). La garde B − 2
   laisse ≈ 62 h de run à 1,258 USD/h, ≈ 49 h à 1,6 USD/h (≈ 70 h au taux carte seule de 1,11 USD/h, qui n'est pas le
   c de la règle). Au-delà de 1,6 USD/h, la règle peut donner K < 71 (c = 1,8, D = 5, t = 1 800 : K = 67), d'où la
   borne de coût du § 2.4. Les séries 1 à 3 et la relance gardent leur B = 75 et leur D (73,026 USD) ; la dépense
   cumulée du témoin devient au plus ≈ 73 + 84,5 USD.
3. **Garde neuve : durée de tour du pilote** (code `lanceur_v21`, `Conduite(t_max_pilote_s=1800)`) : après la règle,
   si t (moyenne des durées des tours 0 et 1 du pilote, la même que la règle) dépasse **1 800 s**, arrêt avant le run
   principal, transfert, destruction. Cette garde n'ouvre pas la reprise du pilote du texte (l. 243-245, 366 : elle se
   referait sur le même hôte) ; sa chute met fin à la tentative. **Une seconde tentative, une seule**, est permise sur
   une autre machine (celle de la première tentative exclue du choix d'offre), sur le mot de Lazar, avant la clôture
   (§ 3) : même poste (D cumulée, même B), pièces neuves (R12) qui ne diffèrent de celles de la première tentative que
   par les noms, l'instance antérieure ajoutée et l'exclusion de cette machine, contre-lues (R2). Son pilote et sa règle
   sont ceux de la seconde machine : t est celui de son pilote (écart au texte, l. 243-245 : « t se prend sur la
   première exécution du pilote qui a fini ses tours 0 et 1 », et l. 248 : règle « appliquée une fois »). Au calcul de
   sa règle, D ≈ 6 à 9 USD (jusqu'à ≈ 14 USD si un pilote a été repris pour une autre cause) : à c = 1,6 USD/h et
   t = 1 800 s, bornes des § 2.3 et 2.4, K = 72 tant que D ≤ 8,7 USD, 71 jusqu'à 9,6 USD, moins au-delà (D = 14 USD :
   K = 66, régime réduit, non retenu au § 3) ; sous ces bornes la marge est plus large. Seconde chute, ou pas de seconde
   tentative : « confirmation non courue (garde de durée du pilote) », avec t. Pourquoi 1 800 : entre le t du pilote de
   la série 3 (1 315,99 s ; 1 800 ≈ 1,368 × t) et le t qu'aurait eu la relance (2 276,4 s), que la garde aurait
   arrêtée. Perte en cas de chute : mise en place, contrôle du juge et trois tours de pilote (≈ 3 h, ≈ 3 à 5 USD sur un
   hôte comme celui de la relance), doublée si le pilote a été repris pour une autre cause ; aucune garde ne la borne
   avant la fin du pilote, hors B − 2.
4. **Filtre d'offre** (paramètre de lancement, déclaré) : celui du poste v12 (`poste-hetzner-v12.sh`, l. 143), plus
   `cpu_cores_effective >= 32`, `cpu_ghz >= 2.4`, et un coût, carte et 110 Go de stockage (grandeur `cout` du choix
   d'offre), d'au plus 1,6 USD/h ; offre la moins chère qui passe. Disque 110 Go. Ce filtre est une préférence : il
   n'est pas établi qu'il exclue la machine de la relance ; le contrôle est la garde du § 2.3. Aucune offre conforme
   dans les 24 h qui suivent le lancement du poste (états poussés par le poste) : rien ne tourne ; « confirmation non
   lancée (aucune offre) ».
5. **Crédit : la recharge automatique seule** (écart à la condition 9′ de l'addendum 6, qui exigeait un crédit couvrant
   20 tours ; mot de Lazar du 17 novembre, verbatim : « vast se recharge tout seul »,
   `registres/passations/2026-11-17-0052-lazar-bailey-recharge-seule.md`, `7f03f882…`). Avant la création : recharge
   automatique configurée (`has_billing` vrai, `autobill_threshold` > 0, `autobill_amount` > 0, `billing_failed` faux) et
   champ `credit` (non `balance`, qui vaut 0 au relevé de 00:51Z) au moins égal à `autobill_threshold` ; relevé (champs
   du compte rendus par `vastai show user`, heure ; dépense horaire des autres instances du compte) fait au lancement du
   poste, non repris pendant l'attente d'une offre, consigné dans l'ordre de lancement ; sinon aucune création tant
   qu'un nouveau relevé ne les tient pas ; « condition du § 2.5 non tenue » n'est constatée qu'à l'échéance de création
   (condition 2) ou sur le mot de Lazar. Aucun seuil de crédit au-delà. Surveillance sans valeur de garde : à chaque
   réveil, crédit, paiements et dépense des autres instances du compte ; alerte à Lazar sous 4 USD de crédit ou si
   `billing_failed` est vrai (l'alerte sur la dépense des autres instances de l'addendum 6 n'est pas reprise).

## 2 bis. Devis (demandé par le mot de Lazar du 16 novembre ; s'ajoute au devis v4, qu'il ne remplace pas)
Hors poste Hetzner. Hôte comme la machine 146915 du Texas (pilote t = 1 316 s ; tours 0 à 7 de 1 299 à 1 586 s, moyenne
1 411 s, sans croissance sur huit tours) : mise en place et contrôle du juge ≤ 0,75 h, pilote ≈ 1,1 h, 72 tours ≈ 28,2 h
(32,5 h avec la marge de 1,15) : ≈ 30 à 34 h, soit ≈ 38 à 43 USD à 1,258 USD/h (carte et stockage : le c de la règle ;
≈ 33 à 38 USD à 1,108 USD/h, carte seule, relevé de la session du 16 novembre, non consigné). Les machines autres que la
machine 146915 du Texas ont une durée de tour non éprouvée ; au relevé de 00:51Z, aucune des deux offres qui passent le
filtre n'est cette machine (la moins chère : machine 146917, 1,2816 USD/h, soit ≈ 38 à 44 USD pour 30 à 34 h). Hôte à
t = 1 800 s qui croîtrait comme la relance (pente de la relance sur les tours 0 à 29 : ≈ 180 s par tour, soit ≈ 143 s
par tour une fois mise à l'échelle 1 800/2 276) : arrêt à B − 2 vers 48 tours complets à 1,108 USD/h, vers 45 à
1,258 USD/h, vers 39 à 1,6 USD/h (régime réduit). Dépense maximale : B − 0,5 = 84,5 USD (seuil de secours), seconde
tentative du § 2.3 comprise. Dépense cumulée du témoin : 73,03 USD (séries 1 à 3 et relance) plus 38 à 84,5 USD. Tirage
sur la carte de Lazar : toute la dépense au-delà de la part du crédit située au-dessus du seuil de recharge de 5 USD
(≈ 1,5 USD au relevé de 00:51Z), par recharges de 5 USD (≈ une toutes les 4 h à 1,26 USD/h ; ≈ 8 à 9 recharges, soit
40 à 45 USD, pour 30 à 34 h ; 17 au pire, soit 85 USD), hors la dépense des autres chantiers du compte.

## 3. Lecture (fixée maintenant ; aucune note lue avant la clôture de la confirmation)
- **Aucune lecture avant la clôture.** Aucune note de sonde ni de juge du témoin (séries 1 à 3 : pilotes, première
  exécution et relance à 36 tours ; confirmation : pilotes, tentatives et exécutions ; journaux d'égalités compris)
  n'est lue, par aucune session ni aucun lecteur, avant la clôture de la confirmation, même là où le texte le
  permettrait plus tôt (l. 241-242, 371). Les gardes automatiques (l. 268-270) et le contrôle du juge de la mise en
  place (l. 231 : « ce n'est pas une lecture de résultat ») ne sont pas des lectures. Les décisions prises jusque-là
  (mot de lancement, crédit, offre, seconde tentative du § 2.3, relance de la l. 371, mise en place refaite (l. 363),
  reprise de la lecture 38) le sont donc sans connaître aucune note ni aucun verdict (seuls sont connus les champs que
  le texte laisse lire : durées, mémoire, nombre de pas, tours complets, nom et état des gardes, états des contrôles du
  juge) ; elles sont rapportées avec leur cause.
- **Clôture de la confirmation** : constatée par une note scellée de la session, qui ne cite que des champs techniques,
  dans l'un de ces cas : (i) les journaux de l'exécution qui porte le verdict sont transférés et scellés (run fini, ou
  tronqué par une ligne de la liste d'arrêt ; après la reprise de la lecture 38 s'il en faut une) ; (ii) la confirmation
  n'est pas lancée ou pas courue, cause nommée : refus exprès du mot de lancement, aucune offre (§ 2.4), condition du
  § 2.5 non tenue, échéance (condition 2), garde de mise en place non refaite (l. 363 ; addendum 5, § 4 : elle peut
  l'être avant la clôture, sur un nouveau mot de Lazar), contrôle du juge hors seuil (l. 365), garde de durée du pilote
  (§ 2.3), seconde chute du pilote, K < 20 à la règle, journaux perdus (reprise de la lecture 38 impossible), ou toute
  autre ligne de la liste d'arrêt qui laisse la série sans run principal lisible ; (iii) Lazar y met fin ; c'est rapporté
  comme sa décision, avec la réserve du § 1 si une lecture a précédé ; si un run est en cours, la note de clôture
  n'est écrite qu'après son arrêt, le transfert et le scellement de ses journaux (reprise de la lecture 38 comprise),
  ou le constat de leur perte. Quand la cause laisse une suite à la décision de
  Lazar (mot de lancement, seconde tentative du § 2.3, mise en place refaite, relance par le chemin de l'addendum 5,
  crédit d'une reprise, nouveau relevé du § 2.5, ligne neuve de la condition 2), la note de clôture cite le mot de Lazar
  qui y renonce, ou constate que l'échéance de la condition 2 est passée ; dans les autres cas, elle est écrite dès le
  constat (s'il y a eu relance par le chemin de l'addendum 5 : après l'assemblage, ou le constat de son refus). Après la clôture, rien n'est ajouté à la confirmation. La note de clôture nomme, pour chaque verdict à lire,
  le dossier donné au lecteur (pour la confirmation : la sortie de la conduite ; le dossier de reprise s'il y a eu
  reprise ; le dossier assemblé, fait avant la clôture, s'il y a eu relance par le chemin de l'addendum 5 ; un refus de
  cet assemblage est constaté avant la clôture, sans lecteur, par la puce « Refus ou erreur à la lecture ») et la
  commande ; ils ne changent plus. Avant la note de clôture, la commande est jouée telle quelle sur un dossier factice
  de même forme, construit par programme sans aucune pièce réelle (comme dans les essais du § 4) ; son issue est citée
  dans la note ; une commande qui y échoue est corrigée avant la clôture, sans aucun dossier réel.
- **Les deux verdicts**, après la clôture seulement : deux lecteurs neufs distincts (R13 : ni auteurs du
  préenregistrement ni de l'analyse), lancés ensemble dans les 24 h qui suivent la clôture, chacun avant que l'autre
  n'ait rendu (un lancement plus tardif est rapporté avec sa cause et ne change aucune règle) ; l'un sur
  `lecture-assemblee-v1` (verdict du texte pour les séries 1 à 3 et la relance ; K′ établi par cette lecture, 36 tours
  complets au bilan ; l. 332, 338) ; l'autre, si un run principal de la confirmation a ses journaux transférés et
  scellés (cas (i) ; cas (ii) ou (iii) après le début du run principal, lu comme un run interrompu, l. 338), sur le dossier que
  nomme la note de clôture. Mêmes critères gelés (`lecture_v8.valider`, `lire` avec
  `analyse_v3.graines()["reechantillonnage"]`, audit de symétrie). Chaque verdict est demandé à un seul lecteur, dont le
  lancement (heure, fichiers donnés, commande) est consigné avant qu'aucun des deux lecteurs n'ait rendu ; tout autre
  lecteur lancé pour le même verdict est rapporté, et le premier lancé fait foi. Aucun des deux lecteurs ne reçoit ni ne
  lit le verdict de l'autre, son rapport, son dossier de lecture, ni aucun registre, passation ou note écrits après la
  clôture, avant d'avoir scellé le sien (cloisons écrites dans sa consigne). Le chemin du rapport est fixé par la consigne. Chaque lecteur écrit et scelle lui-même son
  rapport ; il ne rend à la session que l'empreinte de ce rapport, ou la mention « refus ou erreur » avec le message du
  code (texte de la `GardeArret` ; pour toute autre exception, son type et la ligne du code, sans le contenu qu'elle
  cite), sans aucune valeur. Jusqu'à ce que chaque verdict attendu soit scellé, ou son absence
  constatée, aucune session n'ouvre un rapport, ne lit une note de sonde ou de juge du témoin (au sens de la première
  puce ; les l. 241-242 et 371 du texte ne jouent qu'ensuite), ni ne joue sur un dossier réel `valider`, `lire`, un code de lecture
  corrigé ou tout autre code qui lit ou rend une note : seuls les lecteurs le font (la conduite, la reprise de la
  lecture 38, l'assemblage d'une relance avant la clôture et les contrôles d'empreinte et de scellement, qui ne rendent
  aucune note, ne sont pas visés). Si une session apprend malgré cela un verdict ou une valeur de note avant
  ce moment (message d'un lecteur, fichier ouvert), c'est consigné avec ce qui a été vu ; toute décision prise ensuite
  sur l'autre lecture (remplacement d'un lecteur) est rapportée « décidée après une lecture », et le verdict retenu
  porte cette réserve. Un lecteur dont l'exécution finit sans empreinte ni mention est
  remplacé par un lecteur neuf, sur la même consigne (chemin de rapport neuf, R12), qui fait alors foi, même lancé
  après que l'autre a rendu ; un rapport que le premier aurait scellé n'est pas retenu et n'est pas un verdict rendu
  (« rendu » : empreinte rendue à la session) ; c'est rapporté. Une mention « refus ou erreur » rendue vaut constat de
  la seconde exécution, quelle qu'en soit la forme, même si le lecteur dit ne pas avoir rejoué, et n'ouvre aucun
  remplacement. K′ de la confirmation : nombre de tours complets de
  l'exécution qui porte son verdict (sa relance, s'il y en a une, l. 371).
- **Refus ou erreur à la lecture : règle mécanique, sans diagnostic.** Un état « pas de verdict » rendu par `valider`
  est une issue des critères gelés. Un refus levé par le code (`GardeArret` de `valider` ou de `lire`) ou une erreur
  d'exécution est constaté par le lecteur lui-même, qui ne joue que la commande consignée et la rejoue une seconde fois
  à l'identique avant de rien rendre, sans rien modifier entre les deux exécutions (code, dossier, commande,
  environnement), sans ouvrir aucune pièce du dossier ni modifier aucun fichier du dépôt hors son rapport ; son rapport
  donne les empreintes de l'arbre du code et du dossier à chaque exécution ; une seconde exécution faite après un
  changement vaut refus. Si la seconde exécution aboutit sans changement, il en fait son rapport et y dit le premier
  échec. Un refus ou
  une erreur à la seconde exécution : **« pas de verdict » pour ce run, quelle qu'en soit la cause** (pièce, code,
  assemblage, commande ou environnement), sans nœud, sans classement de la cause, sans correction ni nouvelle lecture
  retenue. Aucune décision ne dépend donc d'un diagnostic. La cause peut être étudiée et rapportée après que chaque
  verdict attendu est scellé, ou son absence constatée, sans effet sur aucun verdict ; toute lecture ultérieure de ce
  run, même après correction, est rapportée « exploratoire, non retenue ». Un refus de l'assemblage d'une relance passée
  par le chemin de l'addendum 5 est constaté avant la clôture, sans lecteur et sans lire aucune note : « pas de verdict » pour ce run,
  quelle qu'en soit la cause, sans correction (le nœud de l'addendum 5, § 5 (d) : « s'il refuse, le verdict n'est pas
  prononcé : nœud », et de l'addendum 6, § 5 (d) : « assemblage refusé : pas de verdict, nœud », est tranché ici) ; la note de clôture le dit et aucun lecteur n'est lancé pour ce run. Dès qu'un verdict a
  été rendu pour un run, aucune relecture de ce run n'est retenue.
- **Rapport** : les deux verdicts, côte à côte, chacun avec son K′ et son régime ; leur accord ou leur désaccord est
  rapporté tel quel ; aucune mise en commun des notes ; aucun verdict n'est ouvert par la session ni rapporté avant que
  chaque verdict attendu soit scellé, ou son absence constatée. **Verdict retenu pour l'étape 1** (nœud 5, option (c),
  inchangée ; formule publique « attaque publiée reproduite sur le banc des auteurs », au régime publié ou « sur
  K tours ») : si la confirmation compte K′ ≥ 71, son verdict, quel qu'il soit (« effet reproduit », « effet non
  reproduit » ou « non interprétable » ; un état « pas de verdict » n'est pas un verdict), est retenu, au régime publié ;
  le verdict à 36 tours reste rapporté comme la lecture prévue au régime réduit. Dans tous les autres cas (confirmation
  non lancée ou non courue, pas de run principal, pas de verdict, ou K′ ≤ 70, quelle qu'en soit la cause), le verdict
  retenu est celui à 36 tours ; si ce run est lui-même sans verdict, aucun verdict n'est retenu pour l'étape 1, quel
  que soit celui de la confirmation ; la confirmation est rapportée avec sa cause, selon la table des critères gelés
  (l. 329-338). Ce que vaut l'étape 1 pour le témoin de [Règle] ne change pas (l. 340 ; nœud 5, option (c)).
- Contrôle du juge hors seuil à la mise en place de la confirmation : pas de run, pas de verdict de confirmation
  (l. 365) ; il est rapporté à côté du verdict à 36 tours, comme réserve, sans le changer.
- **Après le lancement du premier lecteur** : aucune série, tentative, relance, reprise, ni relecture d'un run dont le
  verdict a été rendu, décidée ensuite n'est retenue pour l'étape 1 ; elle est rapportée à côté, avec la mention « décidée après la lecture », sans changer le verdict
  retenu. Aucune autre série sans nouvelle décision de Lazar et nouvel addendum. « La confirmation » désigne la seule
  série de cet addendum, seconde tentative du § 2.3, mise en place refaite (l. 363) et relance de la l. 371 comprises.
- Information, sans effet sur la lecture : le rapport donne le premier tour où les empreintes de suffixe (écart 9) de
  la confirmation diffèrent de celles de la relance (graines identiques), calculé et lu après le scellement des deux
  verdicts ; aucune comparaison de ces empreintes n'est faite avant.

## 4. Code, essais
`lanceur_v21` (= `lanceur_v20` plus la garde du § 2.3 ;
`75cf4049c61d81439989ad11f4f8370ef9c7b16a1257c881245f0efbd8dbaf02`), au commit
`873ab00ca5eaaaa00c84c9ae9f0bd53fef6435e5` ; instance (`instance_v16`), exécution (`execution_v4`), lecture
(`lecture_v8`), journaliseur, conventions, analyse : inchangés. Manifeste neuf `manifeste-local-v7.json`, écrit après
l'inscription de la ligne de GO (il porte son identifiant) : seules différences avec le v6 : `B` (85), `commit_code`,
`go_id`. Essais : `tests/test_temoin_bailey_condition6_v21.py` (`36573ae2…`) : les essais v20 rejoués, plus la garde
(sous le plafond : run principal ; plafond atteint : passe ; au-dessus : arrêt avant le run principal, instance
détruite ; sans plafond : rien ne change) ; avec `tests/test_temoin_bailey_reprise_relance_v1.py` : 227 passés, 1 sauté
(configurations publiques non fournies), sous `PYTHONPATH=src`. Essais complémentaires (M-9 de la contre-lecture) :
`tests/test_temoin_bailey_condition6_v21_complements.py` (`82ef2fa0…`, commit `c44c6d65` ; pilote repris pour une autre
cause, puis garde ; t non fini) : 4 passés. La valeur par défaut `t_max_pilote_s=None` désarme la garde : la conduite
v15 refuse de partir si la valeur n'est pas exactement 1 800, et l'ordre de lancement la consigne. Si la garde tombe, le
manifeste « règle » n'est pas écrit : B, R, D, c, t, H et K sont au bilan et dans le dossier `regle` transféré. Le
libellé d'arrêt du code (« … ; nœud ») se lit selon le § 2.3.

Pièces de lancement, écrites après l'inscription du GO (elles portent son identifiant), contre-lues (R2) et scellées
avant le lancement : conduite `lancer-conduite-v15.py` (il n'y a pas de v14) = `lancer-conduite-v13.py` sans
`relance_seule`, avec `lanceur_v21`, `t_max_pilote_s=1800`, aucune instance antérieure, le manifeste v7 et le GO neuf ;
poste `poste-hetzner-v13.sh` et son constructeur = le poste v12 avec la conduite v15, le filtre du § 2.4 et la garde du
commit `873ab00c`.

## 5. Risques déclarés
- (a) l'hypothèse « processeur » n'est pas établie ; la vitesse d'un hôte peut changer après le pilote, par croissance
  (relance, tours 0 à 29) ou par une charge variable de l'hôte (relance, tours 30, 33, 34 et 35 plus courts ; non
  établi). La garde B − 2 tronque alors le run : à t = 1 800 s avec la croissance de la relance, ≈ 48 tours à
  1,108 USD/h, ≈ 45 à 1,258 USD/h, ≈ 39 à 1,6 USD/h (régime réduit, lu si K′ ≥ 20). Inversement, la garde du § 2.3 peut
  arrêter un hôte lent au seul moment du pilote, ou un hôte stable entre 1 800 et ≈ 2 470 s à 1,258 USD/h (≈ 1 935 s à
  1,6 USD/h ; ≈ 2 800 s au taux carte seule de 1,108 USD/h) que la règle aurait laissé finir 72 tours : perte du § 2.3 ;
- (b) les offres qui passent le filtre changent d'heure en heure ; hors la machine 146915 du Texas (absente du relevé de
  00:51Z), leur durée de tour n'a pas été éprouvée ;
- (c) crédit par la recharge automatique seule : une recharge a déjà fait défaut dans la nuit du 12 au 13 novembre
  (addendum 6, § 1 : carte sans fonds, sans `billing_failed`). Si le compte se vide, Vast arrête l'instance : avant
  20 tours complets, erreur technique de la liste d'arrêt (une relance possible, § 2.1 ; sinon pas de verdict de
  confirmation) ; après, run tronqué (K′ ≤ 70 : le verdict retenu est celui à 36 tours). Une instance arrêtée sous solde
  négatif peut être supprimée par Vast avant la reprise (addendum 6) : journaux perdus, pas de verdict de confirmation.
  Le compte est partagé avec d'autres chantiers : leur dépense accélère le tirage sur la carte ;
- (d) graines identiques à celles du texte : la confirmation n'est pas un réplicat indépendant de la relance ; elle
  teste le même protocole au régime publié (choix de rester dans le texte : changer les graines serait un écart de plus) ;
- (e) délai : les deux verdicts ne sont lus qu'après la clôture (≈ 2 jours après le lancement ; davantage en cas de
  seconde tentative, de relance ou de reprise). Le dossier `lecture-assemblee-v1` reste dans le dépôt sans être lu : la
  cloison repose sur la discipline des sessions, comme depuis le début du témoin. Sur l'ordre de lecture, cet addendum
  remplace le brief `registres/passations/2026-11-15-1843-brief-lancement-session-neuve-temoin-bailey-choix-et-verdict.md`,
  la passation du même jour et la note `registres/passations/2026-11-16-2355-decision-lazar-bailey-2-puis-1.md`, qui
  placent le verdict à 36 tours après le scellement de l'addendum ; toute passation et tout brief écrits avant la clôture
  le disent en tête ;
- (f) le code de lecture n'a jamais été joué sur le dossier réel à 36 tours (cloison) : un refus ou une erreur à la
  lecture, quelle qu'en soit la cause, laisse ce run sans verdict (règle mécanique du § 3, choisie pour qu'aucune
  décision ne dépende d'un diagnostic fait après la clôture) ; si le run à 36 tours est sans verdict et la
  confirmation non retenue, l'étape 1 reste sans verdict retenu (§ 3).

## 6. Conditions de lancement et ordre
Celles du texte et de l'addendum 5, avec :
- condition 2 : une **ligne de GO neuve sur `main`** (mot de Lazar du 17 novembre,
  `registres/passations/2026-11-17-0008-decision-lazar-bailey-ligne-go-main.md`, `546aa0bc…`), de type « calcul »,
  d'identifiant `GO-AAAA-MM-JJ-NN`. Son objet cite le texte (`fb6c2f34`), le devis v4 (`f9c8c66e`) et cet addendum par
  son empreinte, et fixe « (B = 85, garde d'horloge à B − 2) » ; il ne porte aucune autre mention « (B = … ». Plafond
  90 USD ≥ B ; les 5 USD au-delà de B ne sont engagés par aucune conduite : ils couvrent l'écart entre le compte prudent
  et la facture, et une reprise éventuelle (lecture 38) après un arrêt à B − 2 ; toute dépense au-delà de B : nœud.
  Échéance 2026-11-30 : création au plus tard à l'échéance moins ((B − 0,5)/c + 1) h (`verifier_echeance`), soit vers
  le 27 novembre 17:44Z à c = 1,108 USD/h, avant le 28 novembre 02:48Z à c = 1,2576 USD/h ; au-delà : « confirmation non
  lancée (échéance) », sauf ligne neuve accordée par Lazar avant la clôture ;
- condition 5 : nœud 5, option (c), inchangée ;
- condition 7 : le mot direct de Lazar pour le lancement. Il accepte ou refuse en bloc la confirmation, les paramètres du
  § 2, l'ordre de lecture (§ 1) et les règles du § 3 (clôture, verdict retenu, refus ou erreur à la lecture), qui sont
  un choix de la session ; donné avant le scellement de cet addendum, il ne vaut que si les § 2 et 3 scellés sont
  identiques à ce qui a été porté à sa connaissance ; un mot assorti d'une condition ne vaut pas mot de lancement : la demande est renouvelée ;
  seul un refus exprès est une cause de clôture (§ 3) ;
- condition 9′ de l'addendum 6 : remplacée par le § 2.5.

Ordre, sans autre étape que les suites permises avant la clôture (§ 2.1, § 2.3) :
1. cet addendum contre-lu et scellé ;
2. la ligne de GO inscrite sur `main` ; les pièces de lancement écrites (conduite `lancer-conduite-v15.py`, poste
   `poste-hetzner-v13.sh` et son constructeur, manifeste v7), contre-lues (R2) par un lecteur neuf, puis scellées. Ce
   lecteur vérifie qu'elles ne diffèrent de la conduite v13, du poste v12 et du manifeste v6 que par ce que cet addendum
   nomme : `lanceur_v21`, `t_max_pilote_s=1800` exigé, aucune `relance_seule`, aucune instance antérieure, B = 85,
   filtre du § 2.4, garde du commit `873ab00c`, GO neuf et empreinte de cet addendum vérifiée dans son objet ; la demande
   du mot de lancement envoyée à Lazar, avec cet addendum (chemin, empreinte), les § 2 et 2 bis, l'ordre de lecture et
   la règle du verdict retenu (§ 3 : aucun verdict avant la clôture), les risques du § 5 et le tirage attendu sur la
   carte ; le mot de Lazar reçu ;
3. relevé du § 2.5, ordre de lancement, poste lancé, création ; conduite ; clôture (§ 3) ;
4. après la clôture seulement : les deux verdicts (§ 3), scellés ; rapport ; soumis à Lazar pour GO (R13).

Si la confirmation n'est pas lancée ou pas courue, le rapport le dit avec sa cause, et le verdict retenu est celui à
36 tours s'il en a un ; sinon aucun verdict n'est retenu pour l'étape 1 (§ 3).

## Contre-lecture
Rapport (R2) : `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-addendum-7-confirmation-bailey-v1.md`
(`f1c2ca523da96dbeb3e989248ebac21c36f5fad853730613a5d5183513e5372c`), contre-lecteur neuf, sur le brouillon 2 :
« scellable après corrections », aucun bloquant ; ses textes de remplacement sont repris (§ 1, § 2.1 à 2.4, § 2 bis,
§ 4, § 5 (a), condition 2), sauf ce que les points suivants changent.
Vérifications adverses, par des relecteurs neufs : première passe, trois angles
(`docs/notes/reproduction-attaque-publiee-v1/verification-adverse-addendum-7-bailey-v1.md`, `e573e4c7…`, sur le commit
`c44c6d65`) : trois bloquants de l'angle « règle de lecture » ; seconde passe, deux angles (`…-v2.md`, `70e4f7f2…`, sur
le commit `0c373143`) : quatre bloquants (deux contradictions nées de l'exception « défaut technique » : avec l'ordre du
§ 6 et avec la garde de dépense du § 1 ; causes de non-lancement dépendant d'une décision postérieure à la lecture ;
relance, reprise, compte vidé et mise en place) et, parmi les points à corriger, les lecteurs. Traitement : plutôt que
de fermer ces voies une à une, **l'ordre est changé** (§ 1, § 3, § 6 : aucune lecture avant la clôture ; les deux
verdicts ensuite), ce qui retire l'exception « défaut technique », les délais comptés depuis la lecture et la liste des
décisions « postérieures à la lecture » avant la clôture. Repris des deux passes : un seul lecteur par verdict,
lancement consigné, commande rejouée à l'identique ; lecteurs cloisonnés l'un de l'autre ; aucun verdict rapporté avant
les deux scellements ; relance de la l. 371 et reprise précisées ; K′ établi par la lecture ; empreintes de suffixe
(écart 9) lues après les verdicts ; provenance du taux de 1,108 USD/h ; devis et risques au taux carte et stockage ;
échéance exacte ; objet du GO sans autre « (B = … » ; mot conditionnel ; libellé d'arrêt ; essais complémentaires
scellés.
Passe finale, trois angles, sur le texte réécrit (`…-v3.md`, `eab770c9…`, sur le commit `11954d70`) : deux bloquants,
tous deux dans la phase de lecture, après la clôture (règle « refus ou erreur à la lecture » à deux lectures ; premier
verdict connu de la session avant que le sort du second soit fixé), corrigés par les textes de remplacement des
relecteurs (lecteurs lancés ensemble, qui scellent eux-mêmes ; dossier et commande nommés à la clôture ; nœud tranché
sans ouvrir aucun rapport ; statut du lecteur neuf), avec un choix de la session que le premier relecteur laissait à
l'auteur : un refus du code n'est corrigeable que s'il tient à un défaut du code ou de l'assemblage, jamais à la pièce
lue. Points « à corriger » et remarques des trois angles repris : périmètre de « aucune note » ; lecture anticipée ;
pièces anciennes remplacées sur l'ordre de lecture ; moment et auteur de la clôture ; mise en place refaite ; run arrêté
par Lazar ; rattachement de l'ordre de lecture et du § 3 au mot de lancement ; mot conditionnel ; machine 146915 et
relevé de 00:51Z ; champ `credit` ; pilote et règle de la seconde tentative ; bornes de D ; taux carte et stockage aux
§ 2.2 et § 5 (a) ; tours 30, 33, 34 et 35 ; pente ; tirage sur la carte ; heure de fin de la relance ; nuit du 12 au
13 novembre ; chemins complets ; empreintes des notes du 16 novembre ; commits intermédiaires ; lecture qui suit un refus et
définition de « la confirmation » ; dossier de lecture de l'autre lecteur ; champs techniques connus avant la clôture ;
lancement tardif des lecteurs et ordre du § 6 ; relevé et alerte du § 2.5 ; liste des bloquants de la seconde passe ;
`PYTHONPATH`. Aucun constat écarté.
Dernière vérification, différentielle, deux angles (`…-v4.md`,
`16e008d2adbd1babe312122be65da2588a5e9f6eaafe6049e2f2da07d33f37ce`, sur le commit `9c3613d6`) : un bloquant, vu par les
deux angles, dans le choix de la session de la passe finale. Classer un refus en « pièce » (pas de verdict) ou en
« code » (correction, puis lecteur neuf) demandait un diagnostic fait après la clôture, quand rien n'interdisait plus de
lire les notes du run en cause : une décision qui dépendrait d'un résultat lu. Traitement : plutôt que d'encadrer ce
diagnostic, **la règle devient mécanique** (§ 3, puce « Refus ou erreur à la lecture ») : un refus ou une erreur, rejoué
par le lecteur, vaut « pas de verdict » pour ce run quelle qu'en soit la cause, sans correction ni nouvelle lecture
retenue. Prix déclaré au § 5 (f). Ce choix retire, sans les appliquer, les textes proposés pour la dichotomie (angle
« application », points 1 à 4 et 6 (b) ; angle « phase de lecture », points 1 (second remplacement), 2, 3 (mention
« valeur de note vue » ; date du constat, sans objet faute de délai) et 8 (renvoi aux deux § 5 (d) retiré avec la
dichotomie, conséquence portée au § 5 (f))) ; il reprend leur objet : aucune session ne lit une note ni ne joue un code
de lecture sur un dossier réel avant que chaque verdict attendu soit scellé ou son absence constatée ; le lecteur
rejoue lui-même ; lecture ultérieure « exploratoire, non retenue ». Repris tels quels : chemin du rapport fixé par la
consigne ; message du code ; lecteur remplacé ; cas (iii) après l'arrêt et le transfert ; cas (ii) ou (iii) ; mise en
place refaite au même poste de dépense ; membre de phrase de la condition 7 rétabli ; traçabilité de cette section.
Repris avec adaptation à la règle mécanique : verdict appris par erreur (seul le remplacement d'un lecteur reste une
décision) ; run à 36 tours sans verdict (aucun verdict retenu pour l'étape 1, fixé maintenant, sans nœud) ; assemblage
refusé constaté avant la clôture ; parenthèse sur la lecture qui suit un refus retirée plutôt que remplacée (angle
« application », point 6 (a)).
Vérification de cette correction, deux angles (`…-v5.md`,
`831d04c2db476dbbdb75cd8b625219a77b898cae5acab7f2c0ea19411098ba77`, sur le commit `68c3edc1`) : la règle mécanique ferme
le bloquant v4 ; un bloquant neuf : entre ses deux exécutions, le lecteur pouvait ouvrir les notes, corriger le code ou
l'environnement, puis rendre une seconde exécution qui aboutit. Traitement : le lecteur ne joue que la commande
consignée, ne change rien entre ses deux exécutions, n'ouvre aucune pièce, et donne les empreintes de l'arbre du code et
du dossier à chaque exécution ; une seconde exécution après un changement vaut refus. Points « à corriger » : la
correction d'un assemblage refusé, que la session avait ajoutée (fenêtre, délai, renvoi inexact aux § 5 (d), en-tête du
§ 6, réserve du § 1), est **retirée** plutôt que bornée : un assemblage refusé vaut « pas de verdict », sans
correction, ce qui tranche le nœud des addenda 5 et 6, § 5 (d) ; l'assemblage du dossier à 36 tours a déjà abouti
(§ 1), et l'en-tête « Ordre, sans autre étape… » du § 6 reste juste, la règle n'ajoutant aucune étape ; la clôture
attend l'assemblage ou le constat de son refus. Repris : code visé par la cloison (un code qui lit ou rend une note ;
conduite, reprise, assemblage et contrôles d'empreinte exceptés) ; chemin de rapport neuf du lecteur remplacé et sens de
« rendu » ; mention « refus ou erreur » qui vaut constat, sans remplacement ; commande jouée sur un dossier factice avant
la clôture (remarque, reprise pour réduire le prix du § 5 (f)) ; mise en place refaite dans la réserve du § 1 ; phrase
du § 6 sur le verdict retenu. Aucun constat écarté.
