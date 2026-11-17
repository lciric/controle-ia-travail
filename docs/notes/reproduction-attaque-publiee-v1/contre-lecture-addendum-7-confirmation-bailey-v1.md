# Contre-lecture (R2) de l'addendum 7 du témoin de Bailey — run de confirmation au régime complet — v1

17 novembre 2026. Contre-lecteur neuf : sous-agent lancé par la session `session_01XJ6MgnEhQMZteN9F8a1BST`. Je n'ai
écrit aucune des pièces relues. Ne se réécrit pas (R12).

## Verdict

**Scellable après corrections.** Aucun bloquant. Quatre constats majeurs (M-1 à M-4), qui touchent la protection
contre un run qui viserait un signe (R3, R4) et la règle de lecture du § 3. Textes de remplacement donnés mot pour mot.
Ils ne changent ni hypothèse, ni prédiction, ni métrique, ni seuil, ni critère de lecture gelé du texte.

Pièce relue : `brouillons/temoin-attaque-publiee-bailey-v1-addendum-7-run-de-confirmation-brouillon2.md`
(`674d8f1465bfbf0bfbdc1facfd2350aebe91d044533e8d21de15c83e12f452da`), notée [A7] ; les numéros de ligne renvoient à ce
fichier. Texte : `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3`,
empreinte vérifiée), noté [T].

## Ce que j'ai lu, fait, et pas lu

- Lu : [A7] ; [T] en entier ; addenda 1 à 6 (1 à 4 parcourus sur les séries, B et les conditions ; 5 et 6 en entier) ;
  notes `registres/passations/2026-11-15-1843-passation-…`, `2026-11-16-1224-…`, `2026-11-16-2353-…`, `2026-11-16-2354-…`,
  `2026-11-16-2355-decision-lazar-bailey-2-puis-1.md` (`93494ff9…`) et, parce qu'elle porte un mot de Lazar sur la
  ligne de GO de cet addendum, `2026-11-17-0008-decision-lazar-bailey-ligne-go-main.md` (`546aa0bc…`) ; note du nœud 5
  et décision `2026-11-10-1240-decision-lazar-noeud5-lecture-b2.md` ; `conception-continuation-relance-v2.md`
  (`6651a07f…`) ; devis v4 (§ 4, totaux) ; `diagnostic-hetzner-v1-sortie.txt` (`9a879463…`) ; les trois journaux de
  durées, **champs `tour` et `duree_s` seulement** (`6c445f3e…`, `9ff59e4b…`, et le pilote `2cac2458…`) ; la règle de la
  série 3 (`manifeste-v3-regle.json`, champ `regle_tours`) ; les offres choisies v11 et v12 (`23281d5b…`, `972928bb…`) ;
  `poste-hetzner-v12.sh` (`0990ff20…`, filtre) ; lignes GO-2026-11-10-10 et GO-2026-11-11-01 de `registres/go.md` sur
  `origin/main` ; `lanceur_v21.py` (différence avec `lanceur_v20.py`, `verifier_go`, `b_de_l_objet`, `verifier_echeance`,
  la conduite autour de la garde), `analyse_v3.nombre_de_tours` ; les essais v21.
- Fait : empreintes de `lanceur_v21.py` (`75cf4049…`) et des essais (`36573ae2…`) égales à celles de [A7], et égales au
  commit `873ab00c` ; essais `-k test_v21_` : 5 passés ; les deux fichiers d'essais en entier : **227 passés, 1 sauté**
  (5 min 33 s), comme [A7] l. 71 ; la ligne de GO proposée passée à `ligne_go`, `b_de_l_objet` et `verifier_go` ; la règle
  recalculée avec `nombre_de_tours` (calculs au § « Chiffres »). Rien de modifié, rien de commité, aucune commande réseau.
- **Pas lu** : aucune note de sonde ni de juge, aucun `notes-v3.jsonl` ni `technique-v3.jsonl`, aucune des pièces des
  cloisons ; `lecture_v8.lire` et `valider` non appelés.

## Chiffres refaits

| Grandeur | [A7] | Recalcul | Source |
|---|---|---|---|
| K à B = 85, c = 1,6, t = 1 800, D = 8 | ≈ 72,8 → 72 | H = 41,875 h ; K = 72 | `nombre_de_tours(85, 8, 1.6, 1800)` |
| Borne de D pour K = 72 (c = 1,6, t = 1 800) | « D ≤ 8 » | K = 72 si D ≤ 8,76 ; K = 71 si D ≤ 9,68 ; K = 70 à D = 9,7 | même fonction |
| K si c dépasse 1,6 (t = 1 800) | non dit | c = 1,7, D = 8 : 68 ; c = 1,8, D = 5 : 67 ; c = 2,0, D = 5 : 60 ; c = 2,07, D = 8 : 56 | même fonction |
| t du pilote de la série 3 | 1 315,99 s | (1 322,93 + 1 309,05)/2 = 1 315,99 s | `2cac2458…` ; `manifeste-v3-regle.json` |
| 1 800 / 1 315,99 | « 1,37 × » | 1,368 (1,37 × 1 315,99 = 1 802,9) | — |
| Tours 0 et 1 de la relance | 2 187 et 2 340 s | **2 187,1 et 2 365,6 s** ; leur moyenne, ce que la garde compare : 2 276,4 s | `6c445f3e…` |
| Seuil de crédit | 13,5 h | 0,75 + 1,5 + 20 × 1 800 × 1,15 / 3 600 = 0,75 + 1,5 + 11,5 = **13,75 h** | — |
| S à c₀ ≤ 1,7, o = 0,11 | ≥ 25 USD | 13,5 h : 24,4 ; 13,75 h : 24,9 ; donc 25 USD tient | — |
| Durée attendue, hôte comme le Texas | non dite | tours 0 à 7 : 1 299,5 à 1 586,2 s, moyenne 1 411,5 s ; 72 tours ≈ 28,2 h (32,5 h avec 1,15) ; avec mise en place et pilote ≈ 30 à 34 h, ≈ 33 à 38 USD à 1,108 USD/h | `9ff59e4b…` |
| Hôte à t = 1 800 s qui croîtrait comme la relance | « tronque » | pente de la relance (tours 0 à 29) ≈ 180 s par tour, mise à l'échelle 1 800/2 276 : arrêt à B − 2 vers 48 tours complets à 1,108 USD/h, vers 39 à 1,6 USD/h ; 20 premiers tours ≈ 17,3 h (contre 11,5 h au calcul du crédit) | `6c445f3e…` |
| Hôte stable que la règle laisserait finir | non dit | K = 72 tant que t ≤ ≈ 2 786 s à c = 1,108 et D = 4 | `nombre_de_tours` |
| Dernière création permise par l'échéance du 30 novembre | non dite | `verifier_echeance` (B − 0,5, marge 1 h, fin de jour à Paris) : 27 novembre ≈ 17:44Z à c = 1,108 ; 27 novembre ≈ 23:35Z à c = 1,2 ; 28 novembre ≈ 17:11Z à c = 1,6 | `lanceur_v21.py` |

Lenteur de la relance, champs techniques : tours 0 à 29 de 2 187 à 7 629 s, croissance presque régulière ; puis tours 30,
33, 34 et 35 nettement plus courts (4 340 ; 4 007 ; 2 710 ; 2 805 s), les tours 31 et 32 longs (7 891 ; 7 970 s). Le
tour 34, sur une banque plus grande que celle du tour 29, dure 2,8 fois moins. Le diagnostic montre une charge moyenne de
l'hôte de 16,3 pour un processus à 5,76 cœurs. Ces deux faits s'accordent mal avec « l'entraînement de la sonde sur la
banque qui grossit » comme cause seule, et suggèrent, sans l'établir, une charge variable de l'hôte.

## Constats

### M-1 — majeur — le lancement reste décidé après la lecture du verdict à 36 tours (R3, R4)
- Lignes : [A7] l. 29-31 (« engagée quel que soit le verdict »), l. 72-76, l. 87-95.
- Preuve : l'ordre « 2 puis 1 » protège la décision de principe et la règle de lecture, scellées avant la lecture. Mais
  trois actes qui conditionnent le lancement restent placés, ou laissés, après la lecture : la ligne de GO (l. 88-89 :
  aucun moment fixé ; le mot de Lazar du 17 novembre la permet dès le scellement de cet addendum), les pièces de
  lancement (l. 72-76 : « écrites après l'inscription du GO », sans moment fixé par rapport à la lecture), et le mot de
  lancement (condition 7, l. 90). La note `2026-11-17-0008` le dit : la ligne « ne vaut pas mot de lancement ». Un mot
  de lancement donné, ou refusé, après la lecture rend le run suspect de viser un signe. Le risque est accru par le
  risque (d) (l. 84-85) : mêmes graines, même code ; les premiers tours de la confirmation peuvent reproduire ceux de la
  relance. Qui a lu le verdict à 36 tours sait donc déjà une partie de l'issue de la confirmation.
- Correction : tout ce qui peut précéder la lecture la précède, et un non-lancement est rapporté avec sa cause. Texte
  du § 6 ci-dessous.

### M-2 — majeur — rien n'est fixé pour une confirmation qui ne court pas ; la garde du pilote croise la reprise du texte
- Lignes : [A7] l. 40-43, l. 61 ; [T] l. 243-245 et l. 366 (« Garde tombée … au pilote : une seule reprise entière du
  pilote »).
- Preuve : la garde de durée est une garde qui tombe au pilote. À la lettre de [T] l. 366, sa chute ouvre une reprise
  entière du pilote. Le code ne la fait pas : `lanceur_v21.py`, l. 1781-1784, rend l'arrêt après la règle, sans
  `pilote-reprise`. Une reprise sur le même hôte serait d'ailleurs inutile. [A7] ne dit pas que la garde n'ouvre pas
  cette reprise. Après la chute, [A7] écrit « nœud ». Ce nœud se tranche après la lecture à 36 tours : Lazar déciderait
  alors, en connaissant le verdict, de tenter ou non un autre hôte. Même trou pour « aucune offre en 24 h », le crédit
  insuffisant, l'échéance passée et un contrôle du juge hors seuil à la mise en place neuve. Dans ce dernier cas, rien
  n'est dit non plus de son effet sur le verdict à 36 tours.
- Correction : texte du § 2.3 ci-dessous. La garde n'ouvre pas la reprise du texte ; sa chute met fin à la série ; une
  autre tentative passe par une décision et un addendum neufs, qui disent qu'ils viennent après la lecture. Si
  l'auteur préfère fixer dès maintenant une seconde tentative sur une autre machine (même poste, même B, D cumulée),
  c'est un écart de plus, à soumettre à Lazar **avant** le scellement. Ce serait plus utile scientifiquement, mais ce
  n'est pas dans le « go 2 puis 1 ».

### M-3 — majeur — la règle de lecture du § 3 a quatre trous ; un mot contredit le nœud 5
- Lignes : [A7] l. 56-60 ; [T] l. 329-338 et l. 340 ; décision du nœud 5, option (c).
- Preuve :
  (a) « le verdict du témoin » (l. 58, 60) : [T] l. 340 met hors du texte ce que vaut un verdict pour le témoin de
  [Règle]. Lazar a tranché le nœud 5 par l'option (c) : le run de Bailey ne tient pas seul le témoin, il est
  l'« étape 1 ». Le mot de [A7] semble trancher un sujet scellé ailleurs (addendum 2 de la règle du bras).
  (b) K′ ≥ 71 avec « non interprétable » (P2 ou P3 non tenue, garde de fin de run) : [A7] ne dit pas si ce verdict
  devient « le verdict au régime publié » à la place du verdict à 36 tours.
  (c) « régime réduit si K′ ≥ 20 ; pas de verdict sinon » (l. 59-60) est faux pour certaines issues de [T]. La
  « sonde orientée » tombée au pilote vaut « non interprétable », pas « pas de verdict ». P2 ou P3 non tenue à
  20 ≤ K′ ≤ 70 vaut « non interprétable », pas « régime réduit ».
  (d) K′ n'est pas rattaché à l'exécution qui porte le verdict : il faut viser la relance de la confirmation, s'il y en
  a une ([T] l. 371).
  La règle ne dépend d'aucun résultat, et elle est fidèle aux régimes de [T] l. 331-332 (K′ ≥ 71 publié, 20 à 70
  réduit). Il faut seulement la resserrer.
- Correction : texte du § 3 ci-dessous. Le verdict retenu pour l'étape 1 est l'issue de la confirmation, **quelle
  qu'elle soit**, dès que K′ ≥ 71 ; sinon c'est celle à 36 tours. Cette règle est la plus simple et la plus symétrique.
  L'autre règle possible, ne retenir la confirmation que si elle est interprétable, ne vise pas un signe, mais rend le
  choix dépendant d'une issue. Si l'auteur la préfère, il l'écrit avant le scellement.

### M-4 — majeur — le taux c n'est pas borné : la règle peut prévoir un run au régime réduit
- Lignes : [A7] l. 37-39, l. 44-45 ; `poste-hetzner-v12.sh` l. 132 et 143 (aucune borne de prix).
- Preuve : K = 72 n'est garanti qu'à c ≤ 1,6 USD/h, t ≤ 1 800 s et D ≤ 8,76 USD. Le filtre prend « l'offre la moins chère
  qui passe », sans plafond. Les nouvelles bornes de processeur réduisent l'offre, et l'addendum 6 relève des taux
  jusqu'à 2,07 USD/h sur le compte. Exemples : c = 1,8, D = 5 → K = 67 ; c = 2,0 → K = 60. Une confirmation prévue au
  régime réduit dépense jusqu'à 85 USD sans pouvoir atteindre son objet.
- Correction : borne de coût dans le filtre (texte du § 2.4 ci-dessous), et bornes exactes de D dans le § 2.2. L'autre
  voie, un arrêt si la règle donne K < 71, change la liste d'arrêt et n'est pas recommandée.

### M-5 — moyen — chiffres et sources
- l. 19-21 : tour 1 de la relance = 2 365,6 s, pas 2 340 (même erreur l. 42-43). La « croissance presque régulière »
  vaut pour les tours 0 à 29, pas pour 30 à 35. Le minimum du Texas est 21,7 min, pas 21,6.
- l. 42 : « 1,37 × » ; exact : 1 800 = 1,368 × 1 315,99.
- l. 47-48 : 0,75 + 1,5 + 11,5 = 13,75 h, pas 13,5. Le seuil de 25 USD tient quand même (24,9 USD à 13,75 h).
- l. 25-26 : « AMD EPYC 7V12, 32 cœurs effectifs, 2,45 GHz », « louable le 16 novembre », « 1,108 USD/h » : aucune pièce
  citée (R6). Je n'en ai trouvé aucune dans le dépôt. L'offre v11 (`23281d5b…`) donne Texas, 59431043, 1,196 USD/h le
  12 novembre, sans caractéristiques de processeur.
- l. 44-45 : rien n'établit que la machine de la relance (Suède, offre 58516569, `offre-choisie-v12.json`, `972928bb…`)
  aurait échoué au nouveau filtre : ses caractéristiques de processeur ne sont pas relevées. Le filtre est donc une
  préférence, pas un contrôle prouvé. Il faut le dire ; la garde du pilote en est le vrai contrôle.
- l. 37 : « (72 000 × (85 − 10 − 8) / (23 × 1,6 × 1 800) ≈ 72,8 » ouvre une parenthèse sans la fermer.
- Correction : textes du § 1 et des § 2.2 à 2.5 ci-dessous. Pour les caractéristiques du Texas : citer la pièce du relevé
  (chemin, empreinte), ou écrire « relevé de la session, non consigné ».

### M-6 — moyen — pas de devis, alors que le mot de Lazar en demande un
- Lignes : [A7] l. 94 (« devis v4 … prolongé par l'addendum 7 ») ; note `2026-11-16-2355` : « après une ligne de GO …,
  **un devis** et le crédit Vast suffisant ».
- Preuve : le devis v4 chiffre un poste à B = 75 ou 120 sur d'autres hypothèses de durée. [A7] ne donne ni la durée ni
  la dépense attendues de la confirmation, ni la dépense cumulée du témoin (≈ 73 + jusqu'à 84,5 USD, contre un total de
  120 USD au devis v4), ni le tirage attendu sur la carte (demandé par l'addendum 6, § 6, pour le mot de lancement).
- Correction : § 2 bis ci-dessous. `verifier_go` exige que l'objet cite le devis v4 (`f9c8c66e`) : le § 2 bis s'y ajoute
  sans le remplacer.

### M-7 — moyen — « perte bornée » et risque (a) trop optimistes
- Lignes : [A7] l. 43 ; l. 80-81.
- Preuve : la garde n'agit qu'après la règle, donc après les trois tours du pilote, et après sa reprise s'il a été
  repris pour une autre cause. Sur un hôte comme celui de la relance, le pilote seul dure ≈ 2 h (2 187 + 2 366 + 2 519 s).
  Avec la mise en place et le juge : ≈ 3 h, ≈ 3 à 5 USD. Aucune garde ne borne cette perte avant la fin du pilote, sauf
  B − 2. Le risque (a) ne nomme que la croissance. Or les tours 30 à 35 montrent une vitesse qui change dans les deux
  sens, ce qui arrive avec une charge variable de l'hôte. Le plafond de 1 800 s :
  - peut arrêter à tort un hôte lent au seul moment du pilote, ou un hôte stable entre 1 800 et ≈ 2 700 s que la règle
    aurait laissé finir 72 tours ;
  - peut laisser passer un hôte qui ralentit ensuite (vers 48 ou 39 tours, voir les chiffres).
  Ces deux risques sont acceptables. Le choix de 1 800 s, entre 1 316 (Texas) et 2 276 (relance), est défendable, mais
  ils doivent être écrits.
- Correction : textes du § 2.3 et du risque (a) ci-dessous.

### M-8 — moyen — écarts et rattachements à compléter
- l. 28 : le titre attribue au « go 2 puis 1 » des choix qu'il ne contient pas. Le mot de Lazar engage un run neuf de
  72 tours, et la réponse de la session nommait un « court pilote de durée ». B = 85 a le mot exprès du 17 novembre (ligne
  de GO). Le plafond de 1 800 s, le filtre et le seuil de crédit sont des calculs de la session, à soumettre à Lazar avec
  la demande du mot de lancement, comme l'addendum 6 l'a fait pour 9′.
- l. 29-31 : écart aussi à l'addendum 4, § 2.2, et à l'addendum 5, § 4 (« aucune autre série sans nouvelle décision de
  Lazar et nouvel addendum ») : la condition est remplie, mais il faut le dire.
- Non nommés : l'échéance (dernière création possible, voir les chiffres) ; la condition 5 (nœud 5, option (c),
  inchangée) ; la mise en place refaite (contrôle du juge sous la graine du pilote : ce n'est pas une lecture, comme
  l'addendum 5, risque (b)) ; le plafond de 90 USD pour B = 85. [T] l. 249 définit B comme le plafond de la ligne de GO ;
  la lecture 30 de l'addendum 1 lit B dans l'objet, mais les 5 USD au-delà de B doivent dire ce qu'ils couvrent.
- Correction : textes du § 2 (titre) et du § 6 ci-dessous.

### M-9 — mineur — code `lanceur_v21` : conforme ; deux compléments
- Différence avec la v20 : minimale. Un champ `t_max_pilote_s` (défaut `None`), une garde de quatre lignes, le nom du
  module veilleur et deux messages ; rien d'autre.
- Placement : juste après la règle et le contrôle K < 20, avant l'écriture du manifeste « règle » et le run principal.
  C'est le bon endroit : t est celui de la règle, et la garde passe sur la première exécution du pilote qui a fini ses
  tours 0 et 1.
- `not t <= plafond` fait tomber la garde sur une valeur non finie. Le message ne porte qu'une durée, jamais une note. Le
  transfert et la destruction passent par `_finir`.
- Essais (R5) : cas sain (plafond + 1, égal) et artefact (plafond − 1 : arrêt, aucun principal, instance détruite) ;
  sans plafond, rien ne change. C'est le minimum de R5, et il est tenu.
- Manques :
  (i) `t_max_pilote_s=None` désarme la garde **en silence**. La conduite v15 doit refuser de partir si la valeur n'est
  pas exactement 1 800, et l'ordre de lancement ou le bilan doit la consigner. [A7] l. 67-68 (« seules différences : B,
  commit_code, go_id ») ne la met nulle part.
  (ii) Essais à ajouter, sans nouvel addendum s'ils ne changent pas le code : le chemin « pilote repris pour une autre
  cause, puis garde » ; t non fini.
  (iii) Quand la garde tombe, le manifeste « règle » n'est pas écrit : les valeurs B, R, D, c, t, H et K ne vivent que
  dans le bilan et dans le dossier `regle` transféré. À dire au rapport.
- Correction : phrase ajoutée au § 4 (ci-dessous) ; la contre-lecture des pièces vérifie (i).

### M-10 — mineur — ligne de GO proposée
- Épreuve : la ligne l. 93-95, passée telle quelle à `ligne_go`, donne type « calcul », plafond « 90 USD », échéance
  « 2026-11-30 ». `b_de_l_objet` lit B = 85,0 (une seule valeur entre parenthèses). `verifier_go(go, 85)` passe : le texte
  `fb6c2f34` et le devis `f9c8c66e` sont cités, et le plafond 90 ≥ 85. `verifier_go(go, 90)` refuse, comme il faut.
- À régler :
  - les marques à remplir (`1x`, `NN`, « empreinte au scellement ») : l'identifiant doit avoir la forme
    `GO-AAAA-MM-JJ-NN` que la garde de calcul exige ;
  - `verifier_go` ne contrôle pas la citation de l'addendum 7 : la conduite v15 devrait vérifier son empreinte dans
    l'objet ;
  - l'échéance impose une création au plus tard le 27 novembre vers 17:44Z (à c = 1,108).

### M-11 — mineur — dépendance des deux runs et lecteurs
- Le risque (d) est bien déclaré. Deux précisions :
  - le lecteur de la confirmation n'est pas celui du verdict à 36 tours ;
  - si l'auteur le souhaite, ajouter une grandeur rapportée hors critère, sans note : le premier tour où les empreintes
    de suffixe (écart 9) de la confirmation diffèrent de celles de la relance, lu après les deux verdicts. Elle dirait si
    la confirmation a d'abord rejoué la même trajectoire. C'est facultatif : une grandeur de plus doit être déclarée avant
    le scellement, ou pas du tout.

### M-12 — constat sans correction — question 6
Aucun résultat n'a été lu par [A7] : il ne lit que des durées, des taux et l'état des gardes, que [T] permet (l. 239-241,
« On n'en lit que : la durée de chaque tour… »). Aucune hypothèse, prédiction, métrique, population, aucun seuil ni
critère de lecture gelé n'est changé. La garde neuve ajoute un arrêt sur t, pas un seuil de métrique.

## Textes de remplacement, mot pour mot

**§ 1, l. 19-21, remplacer de « **Lenteur de la relance** » à « sans croissance (`9ff59e4b…`). » par :**
> **Lenteur de la relance** (champs techniques seulement) : tours 0 à 35 de 36,5 à 132,8 min
> (`principal-relance/transfert-1/sortie-durees-v3.jsonl`, `6c445f3e…`) : croissance presque régulière des tours 0 à 29
> (36,5 à 127,2 min), puis tours 30, 33, 34 et 35 plus courts (72,3 ; 66,8 ; 45,2 ; 46,8 min) ; 48,7 h pour 36 tours ;
> tours 0 et 1 : 2 187,1 et 2 365,6 s (moyenne 2 276,4 s). Tours 0 à 7 de la première exécution de la série 3, sur une
> autre machine (Texas, offre 59431043), 21,7 à 26,4 min, sans croissance sur ces huit tours (`9ff59e4b…`) ; t du
> pilote de la série 3 : 1 315,99 s (`pilote/transfert-1/sortie-durees-v3.jsonl`, `2cac2458…`).

**§ 1, l. 25-26, remplacer de « la partie lente est sur le processeur » à « 1,108 USD/h). » par :**
> la partie lente est sur le processeur (lecture de la session, non établie : l'entraînement de la sonde sur la banque
> qui grossit, ou une charge variable de l'hôte — charge moyenne 16,3 au diagnostic ; tours 30 à 35 plus courts). La
> machine du Texas (AMD EPYC 7V12, 32 cœurs effectifs, 2,45 GHz) est louable le 16 novembre (offre 59431043,
> 1,108 USD/h) : [pièce du relevé, chemin et empreinte ; à défaut : « relevé de la session, non consigné »]. Les
> caractéristiques du processeur de la machine de la relance (Suède, offre 58516569, `offre-choisie-v12.json`,
> `972928bb…`) ne sont pas relevées : rien n'établit que le filtre du § 2.4 l'aurait exclue.

**§ 2, titre, l. 28, remplacer par :**
> ## 2. Écarts : principe décidé par Lazar (« go 2 puis 1 ») ; B = 85 par son mot du 17 novembre (ligne de GO) ; plafond de durée, filtre et crédit : calcul de la session, soumis à Lazar avec la demande du mot de lancement (condition 7), dont le mot les accepte

**§ 2.1, l. 29, remplacer « (écart à R3 et à la liste d'arrêt : une série nouvelle après la relance) » par :**
> (écart à R3, [T] l. 69-71, à la liste d'arrêt, et à l'addendum 4, § 2.2, et à l'addendum 5, § 4 : une série nouvelle après la relance, sur nouvelle décision de Lazar et par cet addendum)

**§ 2.2, l. 35-39, remplacer le point entier par :**
> 2. **Poste neuf, B neuf (écart au texte, l. 249-251 et 374).** La série de confirmation est un poste neuf : D compte de
>    zéro à sa première instance ; **B = 85 USD**, garde à B − 2. Pourquoi 85 : la règle donne K = 72 dès que
>    c ≤ 1,6 USD/h (carte et stockage, borne du § 2.4), t ≤ 1 800 s (garde du § 2.3) et D ≤ 8,7 USD au calcul
>    (`analyse_v3.nombre_de_tours(85, 8, 1.6, 1800)` : H = 41,9 h, K = 72 ; K = 71 tant que D ≤ 9,6 USD). La garde B − 2
>    laisse ≈ 70 h de run à 1,11 USD/h. Au-delà de 1,6 USD/h, la règle peut donner K < 71 (c = 1,8, D = 5, t = 1 800 :
>    K = 67), d'où la borne de coût du § 2.4. Les séries 1 à 3 et la relance gardent leur B = 75 et leur D
>    (73,026 USD) ; la dépense cumulée du témoin devient au plus ≈ 73 + 84,5 USD.

**§ 2.3, l. 40-43, remplacer le point entier par :**
> 3. **Garde neuve : durée de tour du pilote** (code `lanceur_v21`, `Conduite(t_max_pilote_s=1800)`) : après la règle,
>    si t (moyenne des durées des tours 0 et 1 du pilote, la même que la règle) dépasse **1 800 s**, arrêt avant le run
>    principal, transfert, destruction. Cette garde n'ouvre pas la reprise du pilote du texte (l. 243-245, 366 : elle se
>    referait sur le même hôte) ; sa chute met fin à la série de confirmation, rapportée « confirmation non courue
>    (garde de durée du pilote) », avec t. Aucune nouvelle tentative sans nouvelle décision de Lazar et nouvel addendum,
>    qui diraient qu'ils sont postérieurs à la lecture du verdict à 36 tours. Pourquoi 1 800 : entre le t du pilote de la
>    série 3 (1 315,99 s ; 1 800 ≈ 1,368 × t) et le t qu'aurait eu la relance (2 276,4 s), que la garde aurait arrêtée.
>    Perte en cas de chute : mise en place, contrôle du juge et trois tours de pilote (≈ 3 h, ≈ 3 à 5 USD sur un hôte
>    comme celui de la relance), doublée si le pilote a été repris pour une autre cause ; aucune garde ne la borne avant
>    la fin du pilote, hors B − 2.

**§ 2.4, l. 44-45, remplacer le point entier par :**
> 4. **Filtre d'offre** (paramètre de lancement, déclaré) : celui du poste v12 (`poste-hetzner-v12.sh`, l. 143), plus
>    `cpu_cores_effective >= 32`, `cpu_ghz >= 2.4`, et un coût, carte et 110 Go de stockage (grandeur `cout` du choix
>    d'offre), d'au plus 1,6 USD/h ; offre la moins chère qui passe. Disque 110 Go. Ce filtre est une préférence : il
>    n'est pas établi qu'il exclue la machine de la relance ; le contrôle est la garde du § 2.3. Aucune offre conforme
>    en 24 h : rien ne tourne ; « confirmation non lancée », rapportée avec sa cause.

**§ 2.5, l. 46-48, remplacer le point entier par :**
> 5. **Crédit (comme la condition 9′ de l'addendum 6)** : avant la création, crédit ≥ S = 14 h × (max(1,7 ; c₀) + o) et
>    ≥ 25 USD, recharge automatique configurée ; 14 h ≥ mise en place ≤ 0,75 h + pilote ≤ 1,5 h + 20 tours × 1 800 s
>    × 1,15 = 11,5 h (total 13,75 h) ; relevé consigné dans l'ordre de lancement. Un hôte à t = 1 800 s qui croîtrait
>    comme la relance mettrait ≈ 17,3 h pour ses 20 premiers tours : la recharge automatique couvre l'écart (risque (c)).

**Ajouter après le § 2 :**
> ## 2 bis. Devis (demandé par le mot de Lazar du 16 novembre ; s'ajoute au devis v4, qu'il ne remplace pas)
> Hors poste Hetzner. Hôte comme celui du Texas (pilote t = 1 316 s ; tours 0 à 7 de 1 299 à 1 586 s, moyenne 1 411 s,
> sans croissance sur huit tours) : mise en place et contrôle du juge ≤ 0,75 h, pilote ≈ 1,1 h, 72 tours ≈ 28,2 h
> (32,5 h avec la marge de 1,15) : ≈ 30 à 34 h, ≈ 33 à 38 USD à 1,108 USD/h. Hôte à t = 1 800 s qui croîtrait comme la
> relance (≈ 180 s par tour, mise à l'échelle 1 800/2 276) : arrêt à B − 2 vers 48 tours complets à 1,108 USD/h, vers
> 39 à 1,6 USD/h (régime réduit). Dépense maximale : B − 0,5 = 84,5 USD (seuil de secours). Dépense cumulée du témoin :
> 73,03 USD (séries 1 à 3 et relance) plus 33 à 84,5 USD. Tirage sur la carte : la dépense moins le crédit initial, par
> recharges de 5 USD (≈ une toutes les 3 à 4,5 h selon le taux).

**§ 3, l. 50-61, remplacer la section entière par :**
> ## 3. Lecture (fixée maintenant, avant toute lecture)
> - **Verdict à 36 tours** (étape « 1 » de Lazar) : prononcé d'abord, par un lecteur neuf (R13), sur
>   `lecture-assemblee-v1`, avec les critères gelés ; c'est le verdict du texte pour les séries 1 à 3 et la relance
>   (K′ = 36, l. 332, 338). Il ne change ni la décision de lancer la confirmation, ni ses pièces, ni sa lecture. Seule
>   exception, fixée maintenant : si cette lecture établit un défaut technique d'un code que la confirmation emploie
>   (lanceur, instance, exécution, journaliseur, lecture), la confirmation n'est pas lancée avec ce code ; nœud ; toute
>   correction passe par un addendum neuf, qui dit qu'il est écrit après cette lecture.
> - **Verdict de confirmation** : par un lecteur neuf (R13), qui n'est pas celui du verdict à 36 tours, sur la sortie de
>   la conduite de confirmation, avec les mêmes critères gelés (`lecture_v8.valider`, `lire` avec
>   `analyse_v3.graines()["reechantillonnage"]`, audit de symétrie). K′ y désigne le nombre de tours complets de
>   l'exécution qui porte le verdict de la confirmation (sa relance, s'il y en a une, l. 371).
> - **Rapport** : les deux verdicts, côte à côte, chacun avec son K′ et son régime ; leur accord ou leur désaccord est
>   rapporté tel quel ; aucune mise en commun des notes. **Verdict retenu pour l'étape 1** (nœud 5, option (c),
>   inchangée ; formule publique « attaque publiée reproduite sur le banc des auteurs », au régime publié ou « sur
>   K tours ») : si la confirmation compte K′ ≥ 71, son verdict, quel qu'il soit (« effet reproduit », « effet non
>   reproduit » ou « non interprétable »), est retenu, au régime publié ; le verdict à 36 tours reste rapporté comme la
>   lecture prévue au régime réduit. Dans tous les autres cas (confirmation non lancée ou non courue, pas de run
>   principal, pas de verdict, ou K′ ≤ 70, quelle qu'en soit la cause), le verdict retenu est celui à 36 tours ; la
>   confirmation est rapportée avec sa cause, selon la table des critères gelés (l. 329-338). Ce que vaut l'étape 1 pour
>   le témoin de [Règle] ne change pas (l. 340 ; nœud 5, option (c)).
> - Contrôle du juge hors seuil à la mise en place de la confirmation : pas de run, pas de verdict de confirmation
>   (l. 365) ; il est rapporté à côté du verdict à 36 tours, comme réserve, sans le changer.
> - Aucune autre série sans nouvelle décision de Lazar et nouvel addendum.

**§ 4, l. 72, après « 227 passés, 1 sauté (configurations publiques non fournies). », insérer :**
> La valeur par défaut `t_max_pilote_s=None` désarme la garde : la conduite v15 refuse de partir si la valeur n'est pas
> exactement 1 800, et l'ordre de lancement la consigne. Si la garde tombe, le manifeste « règle » n'est pas écrit :
> B, R, D, c, t, H et K sont au bilan et dans le dossier `regle` transféré.

**§ 5, risque (a), l. 80-81, remplacer par :**
> - (a) l'hypothèse « processeur » n'est pas établie ; la vitesse d'un hôte peut changer après le pilote, par croissance
>   (relance, tours 0 à 29) ou par une charge variable de l'hôte (relance, tours 30 à 35 plus courts ; non établi). La
>   garde B − 2 tronque alors le run : à t = 1 800 s avec la croissance de la relance, ≈ 48 tours à 1,108 USD/h, ≈ 39 à
>   1,6 USD/h (régime réduit, lu si K′ ≥ 20). Inversement, la garde du § 2.3 peut arrêter un hôte lent au seul moment du
>   pilote, ou un hôte stable entre 1 800 et ≈ 2 700 s que la règle aurait laissé finir 72 tours : perte du § 2.3,
>   confirmation non courue ;

**§ 6, l. 87-95, remplacer la section entière par :**
> ## 6. Conditions de lancement et ordre
> Celles du texte et de l'addendum 5, avec :
> - condition 2 : une **ligne de GO neuve sur `main`** (mot de Lazar du 17 novembre,
>   `registres/passations/2026-11-17-0008-decision-lazar-bailey-ligne-go-main.md`, `546aa0bc…`), de type « calcul »,
>   d'identifiant `GO-AAAA-MM-JJ-NN`. Son objet cite le texte (`fb6c2f34`), le devis v4 (`f9c8c66e`) et cet addendum par
>   son empreinte, et fixe « (B = 85, garde d'horloge à B − 2) ». Plafond 90 USD ≥ B ; les 5 USD au-delà de B couvrent
>   [à nommer]. Échéance 2026-11-30 : création au plus tard à l'échéance moins ((B − 0,5)/c + 1) h (`verifier_echeance`),
>   soit le 27 novembre vers 17:44Z à c = 1,108 USD/h ; au-delà, une ligne neuve ;
> - condition 5 : nœud 5, option (c), inchangée ;
> - condition 7 : le mot direct de Lazar pour le lancement ;
> - condition 9′ : le § 2.5.
>
> Ordre, sans autre étape :
> 1. cet addendum contre-lu et scellé ;
> 2. **avant la lecture du verdict à 36 tours** :
>    - la ligne de GO inscrite sur `main` ;
>    - les pièces de lancement écrites (conduite `lancer-conduite-v15.py`, poste `poste-hetzner-v13.sh` et son
>      constructeur, manifeste v7). Elles sont contre-lues (R2) par un lecteur neuf, puis scellées. Ce lecteur vérifie
>      qu'elles ne diffèrent de la conduite v13, du poste v12 et du manifeste v6 que par ce que cet addendum nomme :
>      `lanceur_v21`, `t_max_pilote_s=1800` exigé, aucune `relance_seule`, aucune instance antérieure, B = 85, filtre
>      du § 2.4, garde du commit `873ab00c`, GO neuf et empreinte de cet addendum vérifiée dans son objet ;
>    - la demande du mot de lancement (condition 7) envoyée à Lazar, avec le § 2 bis, les risques du § 5 et le tirage
>      attendu sur la carte ;
> 3. le verdict à 36 tours prononcé et scellé (R13) ;
> 4. crédit relevé (9′), mot de Lazar reçu, création.
>
> Si une pièce de l'étape 2 ne peut être faite avant la lecture, elle est faite après, et le rapport le dit. Si la
> confirmation n'est pas lancée (mot non donné, aucune offre, crédit, échéance, défaut du § 3), le rapport du témoin le
> dit avec sa cause, et le verdict retenu reste celui à 36 tours.

## Réponses aux six questions

1. L'ordre « 2 puis 1 » protège la décision de principe et la règle de lecture. Il ne protège pas le lancement : M-1
   et M-2 corrigés, il le fait. La règle du § 3 ne dépend d'aucun résultat et elle est fidèle à [T] l. 331-332. Elle
   doit être resserrée : quel verdict compte à K′ ≥ 71 « non interprétable », quelles issues ont K′ < 71, quelle
   exécution porte K′, et le mot « verdict du témoin » (M-3).
2. Écarts : série neuve, poste neuf, B = 85, garde du pilote, filtre et crédit sont nommés. Leur rattachement au mot de
   Lazar est trop large (M-8). Manquent : l'échéance, la condition 5, la mise en place refaite, le plafond 90 contre
   B = 85, la reprise du pilote croisée par la garde (M-2) et la borne de taux (M-4). D d'un poste neuf est nommé (§ 2.2).
   Les graines identiques et la dépendance des deux runs sont déclarées (d) ; voir M-11.
3. B = 85 est exact (K = 72, H = 41,9 h), sous c ≤ 1,6 et D ≤ 8,76. Le t de 1 315,99 s est exact. Le tour 1 de la relance
   est faux (2 365,6 s, pas 2 340). 13,5 h vaut en fait 13,75 h. Sur un hôte comme le Texas : ≈ 30 à 34 h,
   ≈ 33 à 38 USD. Le plafond de 1 800 s se défend, mais ses deux erreurs possibles doivent être écrites (M-5, M-7).
4. Garde : la différence avec la v20 est minimale, la garde est au bon endroit et les essais suffisent à R5. Deux
   compléments : refus de `None` à la conduite, et deux essais de plus (M-9).
5. La ligne de GO proposée passe `verifier_go` et `b_de_l_objet`, une fois les marques remplies. L'ordre a un trou :
   rien n'est placé avant ou après la lecture, sauf l'addendum et la création (M-1). La contre-lecture des pièces est
   dite (l. 72-73). Il faut dire ce qu'elle vérifie, et la placer avant la lecture si possible.
6. Aucun résultat lu ; aucune hypothèse, métrique ni seuil changé (M-12).
