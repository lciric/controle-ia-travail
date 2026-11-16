# Contre-lecture de la consigne du lecteur B (brouillon 3) — tour 1 — v1

- **Pièce contre-lue** : `docs/procedures/lecture-7b-etape-b-compte-3-v1/consigne-lecteur-b-v1-brouillon3.md`
  (`12881d63d3cc5056b1246a3816da5d4a67d28970178085eca8c21d9bdd9cce85`, 1 015 lignes, égale à son compagnon), lecture entière.
- **Contre-lecteur** : sous-agent neuf (modèle C), règle R2 ; je n'ai écrit aucune pièce de la liste, aucun brouillon de la
  consigne, et je ne serai ni le lecteur B ni un lecteur d'une autre étape. Heures (`date -u`) : début 2026-11-16T13:57:23Z ;
  fin 2026-11-16T14:08:40Z (lue juste avant l'écriture de ce fichier).
- **Verdict : corrections** (1 majeure, 21 mineures dont 1 facultative ; plus 1 option de procédure laissée à la mère). La
  conception tient : aucun critère n'est ajouté, les 194 renvois, les 15 pièces, le motif des noms et les clés tirées du code
  sont exacts. Les corrections sont de précision (ordre des gestes, contradiction d'heure de fin, un code d'arrêt non
  mécanique, texte libre dans le rapport final, lecture prudente de la base (A) à recopier).

## 1. Pièces lues (empreintes recalculées)

- La pièce ; `consigne-lecteur-b-v1-brouillon2.md` (`6bcfa40005d8e194249568c98be6f855a39ac46792339bb6049895c892ecf421`, par
  différentiel) ; `rapport-redacteur-consigne-b-v1.md` (`5a0582d1535991e6499b641e0574d1c0e489c4fc72f3985b2948fd4de24d5bd7`,
  entier) ; `lecture-a-blanc-consigne-lecteur-b-brouillon3-v1.md`
  (`4b4e9af99696e93e1e4079a9e6c54b8b2ee638b8dd92d5589978638a89567841`, entière) ; `commande-compte-3-phase-c-v4-brouillon1.md`
  (blocs 1C, C0, C5, C6, C7, F-C, § 15) ; `consigne-lecteur-a-v1.md` (§ 13 seulement) ;
  `verification-courte-commandes-v2-v3-v1.md` (ligne R-V2) ; `preparation-phase-c-v3-mere-v1.md` (§ 1.4) ;
  `verification_renvois_consigne_b_v2.py` et sa sortie v3.
- Textes scellés, par plages : `prereg/T0.7-sondes-v0-v1.md` (l. 1065-1156, 1223-1236, 1256-1312, 1373-1394, 1413-1416,
  1459-1545, 1813-1836, 1898-1942, 1944-2024, 2174-2183, 2466-2480, 2609-2620, 2655-2671 ; recherches de mots ailleurs) ;
  addendum (l. 288-299) ; configuration (clés) ; `prereg/T0.8-base-A-mots-et-cout-v1.md` (l. 130-141) ;
  `prereg/T0.7-consigne-audit-fuites-v1.md` (titres, l. 118-124) ; `prereg/T0.6-organismes-v0-v1.md` et
  `docs/decisions/decision-N-063-v2.md` par le seul programme de renvois.
- Code au commit `c2fab6cc7267b76228a75dc3e2e08bc7aa038961` (`git show`) : `lecture_v1` à `lecture_v4`, `criteres_v1`,
  `plancher_v2`, `lectures_t07_v1`, `sondes_neuves_v1`, `controle_jeux_v1` (empreintes des douze fichiers de la section 5
  recalculées : égales).
- Registres : `registres/scellements-v1.md` et son journal (clés, dates, chemins seulement) ; une ligne de
  `registres/decisions.md` cherchée par sa clé (`R-2980`).

## 2. Contrôles demandés

1. **« Lecture » et « choix » de cette consigne** : onze marques relevées (l. 20-21, 556, 692, 715, 753, 763, 784, 801, 840, 899,
   966) ; chacune est fidèle au texte ou le dit ouvertement. Aucun critère ajouté. Deux arrêts de la consigne ne sont pas
   marqués « choix de cette consigne » alors qu'ils n'ont pas de point de la liste d'arrêt pour appui : l'égalité des 13 valeurs
   de la configuration et du manifeste (6.4, point 2) et les lignes lues par le module (6.4, point 4) : K20, K21.
2. **Sections 6.5 à 6.7 contre l. 1459-1520** : l'ordre est celui du plan (P, A, puis Q, puis F ; placebo et audit ; validité ;
   T7-P6, T7-P17, T7-P16, T7-P10, T7-P9 ; écart à la base ; phrase de M ; rapport). **Section 4 contre l. 1813-1836** : sept
   entrées, valeurs et domaines exacts. **Clés de la section 5** : confrontées au code (`etape_b`, `lecture_jeux_v3`,
   `comparer_difference_au_plancher`, `reserves`, `rejouer_controle_9`, `choisir_principale`, p6, `lire_jeux_et_phrases`,
   `controler_t07`) : aucune clé citée n'est absente ou d'une autre forme. Écarts relevés : K11 (passe 1 trop large), K13
   (motif de Q « illisible » non retrouvable à la lettre).
3. **Quinze pièces et bloc C5** : par le programme (contrôle 7 : 14 fichiers copiés, chemins égaux, 29 lignes au bordereau,
   extrait à part). Ce que la consigne fait lire dans `sondes-t07.json` est conforme aux l. 1539 (« paires des jeux », lecture
   de la consigne l. 2663 plausible) et 2659 (motif vrai de T7-P6, DF-05) ; les clés lues (`sondes_lues`,
   `principales_consignees`, `concepts`, `sondes_neuves.concepts.*`, `p6.etat`, `p6.paires_entrainement`,
   `controles_jeux.controle_9.jeux.*`, `phrases_concepts`) existent dans le code qui écrit le fichier. Ce qui est lu en
   comptes seulement : `paires_en_defaut`, `taches_sorties` ; rien du reste (`modes_temoin`, `directions`, `reglages` non lus).
4. **Motif des noms et quatre lignes** : le motif de la section 9 est égal, à l'octet, à celui du bloc C7 ; les douze noms de la
   consigne y répondent. Les quatre lignes sont celles que le bloc F-C relève (`STATUT`, `FICHIERS`, `DÉCLARATIONS`, `MESSAGE`).
   Règle R-V2 : les lignes `FICHIERS` ne portent que des noms ; les textes libres de `refus` et de `autre` sont le seul canal
   par lequel un nombre ou un morceau de pièce pourrait sortir : K3.
5. **Contrôle des renvois** : `verification_renvois_consigne_b_v2.py` rejoué sur la pièce : 194 citations retrouvées, 194
   renvois employés, 7 empreintes égales, 12 noms conformes, 29 lignes, 14 fichiers du bloc C5 égaux, aucune pièce de la table
   dans « Jamais remis » ; **code 0**. Rejoué aussi sur la pièce **avec les corrections K1 à K22 appliquées** (copie jetable) :
   **code 0**.
6. **Filtre de contenu** : aucune ligne touchée par `INTERDITS_CONTENU_B` ; aucun identifiant de modèle (motif passé en
   argument, non écrit ici) ; aucun marqueur à chevrons doubles ; les chevrons simples (`<ESPACE>`, `<PY>`, `<n>`) sont des
   noms de variables voulus.
7. **Lecture à blanc** : chaque point jugé au § 4.
8. **Neuf codes d'arrêt** : sept sont mécaniques. `critere-inapplicable` contient une clause de jugement (« condition d'une
   ligne que tes pièces ne permettent pas de juger et dont la ligne dépend ») : K2. `contradiction-consigne-texte` (« sur un
   point qui touche la ligne ») reste un jugement, repris de la consigne du lecteur A, laissé tel quel : remarque facultative.
   Aucun repli silencieux : les trois replis (P illisible pris du module, clé secondaire « non relevé », motif de T7-P6 de la
   pièce 15) sont écrits au verdict.
9. **Étape B bis, bras d'attaque, mode tenu à l'écart** : rien dans la consigne (recherche de mots : aucune occurrence). Le
   texte de T0.7 emploie « stratégie tenue à l'écart » (l. 1305, 1396) pour le bras de T7-P6 : autre chose que le mode tenu à
   l'écart de G1 ; la consigne ne lit pas la l. 1396 (hors de ses plages). Dans la pièce 15, `modes_temoin` et le champ `mode` de
   J-A ne sont pas lus (seuls les comptes de `taches_sorties`).

## 3. Jugement des ambiguïtés A1 à A7

- **A1 (R-BA1)** : lecture fidèle et prudente. La double marque (lecteur, puis session mère, T0.7 l. 2183) est admise, la
  consigne rappelle que le texte confie l'écriture à la session mère et que rien ne change (R112). Pas de correction. Réserve :
  la ligne dédiée de BA-L2 est un texte libre ; sa lecture mécanique demande des chaînes fixes (K17 à K19, et point pour la mère).
- **A2 (phrase gelée)** : la cellule entière à l'octet, `resultat.phrase` en regard, différence écrite non tranchée : la plus
  fidèle des lectures ; pas de correction.
- **A3 (« trop beau », balayages)** : lecture prudente (une lecture ou l'autre) ; mais « tous les jeux d'organisme lus » et les
  ensembles balayés pour R9 ne sont pas bornés. K15 les borne à ce que le module balaie ; K22 dit que la lecture large ne peut
  déclencher que si l'étroite le fait.
- **A4 (audit sur jeu non décisif)** : fidèle à T0.7 l. 1924 (« suit l'étape B, hors F ») ; « audit dû, non fait par ce verdict »,
  en question. Pas de correction.
- **A5 (puissance)** : calcul interdit, phrase recopiée, question : prudent et fidèle. Pas de correction.
- **A6 (lecture prudente de la base (A))** : **la consigne ne la recopie pas** (elle interdit seulement d'écrire « ne porte rien »
  ou « est flagrant » de sa main) : contraire à la préférence prudente de la mère et à T08A l. 139 (« à écrire telle quelle avec
  toute phrase sur le barreau 3 »). K16 la fait recopier une fois, avec rappel après toute phrase sur le critère 3.
- **A7 (addendum)** : comparaison de la ligne `CODE-T07` à la « Nouvelle ligne » : mécanique ; je l'ai refaite sur le registre
  (chemin et date égaux à l'addendum, l. 294). Pas de correction.
- Aucune des sept n'est un écart à un texte scellé qui demande le mot de Lazar.

## 4. Lecture à blanc : point par point

| point | jugé | pourquoi |
|---|---|---|
| B1 heure de fin | **retenu (majeur)** | l'en-tête du verdict veut l'heure de fin, la 6.10 la lit après le fichier d'issue, et le verdict ne se retouche plus : K1 |
| B2 recopie à la main | retenu, **option de la mère** | risque réel de faute de recopie sur des centaines de nombres, mais pas un écart au texte ; couples O1 et O2 ci-dessous |
| B3 textes libres du rapport final | retenu (mineur) | R-V2 : aucun nombre, aucune issue ; le jugement « cite un nombre » est fait au pire moment : K3 |
| m1 clé par sous-chaîne | retenu | `AUDIT-FUITES-T07` est contenue dans `CONSIGNE-AUDIT-FUITES-T07` : K6 |
| m2 « dix clés » | retenu | douze clés listées ; le texte (l. 2174-2178) en exige neuf à l'étape B, plus `SCELLEMENT-T07` permise : K5 |
| m3 ordre des gestes, code selon le cas | retenu | un script qui empreinte tout ouvre le fichier inattendu ; « ou » entre deux codes : K7 |
| m4 « jamais en entier » | retenu | les scripts de contrôle ouvrent les fichiers en entier : K8 |
| m5 message recopié | non retenu comme correction | un contrôle interne ne rattrape rien (le nom est fixé, R12) ; facultatif : faire écrire la copie par un script |
| m6 premier geste | non retenu | l'ordre « empreinte, lecture, copie » se déduit de 2, 6.0 et 11 ; facultatif |
| m7 lecture de ses propres fichiers | retenu | la 1 interdit tout fichier hors de `pieces/` : K9, K10 |
| m8 passe 1 trop large | retenu | `entrees.I`, `entrees.II`, `doses.etat_ii_par_dose_jugee`, `doses.ecart_a_la_base` portent des états et des aires de sondes : K11 |
| m9 journal avant dérivation de Q | retenu | la ligne `scores-t07/… (Q = …)` donne la valeur du module : K12 |
| m10 motif « introuvable » | retenu | le motif est un message du module : K13 |
| m11 forme des trois sections | retenu | K14 |
| m12 forme de la ligne de BA-L2 | retenu | K17 à K19 ; point pour la mère |
| m13 « trop beau » | retenu | K15, K22 |
| m14 « R9 », « R12 » sans préfixe | non retenu | la note « Trois familles de noms » et le mot « ligne » suffisent ; facultatif |
| m15 propreté suspecte | non retenu | question seule, sans seuil : c'est déjà dit ; fixer l'égalité exacte ajouterait une règle |
| m16 identifiants de modèle | non retenu comme correction | aucune garde sur le contenu au bloc C7 (noms seulement) : point pour la mère |
| m17 marqueur et puce | non retenu | voulus ; à réécrire au sceau |
| `critere-inapplicable` | retenu | K2 |
| A1 à A7 de la lecture à blanc | voir § 3 | A6 : désaccord avec la lecture à blanc (« une fois, section 3 » ne suffit pas) |

## 5. Corrections exactes (« ancien → nouveau »)

Chaque « ancien » figure **une seule fois** dans la pièce (vérifié par programme, 22 occurrences exactes). Les retours à la ligne
des « ancien » et « nouveau » sont des retours à la ligne du fichier. **K1 est majeure ; K22 est facultative ; les autres sont
mineures.**

**K1 (majeure, 6.10, heure de fin)**
- ancien : `seule fois. Heure de fin par `date -u`. Puis ton rapport final (section 14).`
- nouveau : `seule fois. L'heure de fin s'écrit dans l'en-tête du verdict (section 12, point 2) : tu la lis par `date -u` juste avant`⏎`d'écrire la version achevée du verdict en prose, jamais après le fichier d'issue (règle R12 : le verdict n'est plus retouché).`⏎`Puis ton rapport final (section 14).`

**K2 (13, code `critere-inapplicable`)**
- ancien : `, ligne mécanique hors des lignes L, condition d'une ligne que tes pièces ne permettent pas de juger et dont la ligne dépend (G et A, que tu prends du module comme la section 6.5 le dit, ne sont pas ce cas)`
- nouveau : `, ligne mécanique hors des lignes L (G et A, que tu prends du module comme la section 6.5 le dit, ne sont pas ce cas ; une condition que tes pièces ne permettent pas de juger s'écrit « non vérifiable depuis mes pièces » et, si la ligne en dépend, l'arrêt est `autre`)`

**K3 (14, textes libres du rapport final)**
- ancien : `` `<code>` est l'un des neuf codes de la section 13, seul. Deux exceptions : `refus` est suivi d'un tiret et du texte du ``⏎`refus, tel quel, **sauf** si ce texte cite un nombre, une issue ou le contenu d'une pièce : alors la ligne porte`⏎`` `arret refus` seul et le texte entier du refus va au fichier d'arrêt ; `autre` est suivi d'un tiret et d'un motif d'une ``⏎`ligne, sans nombre ni issue.`
- nouveau : `` `<code>` est l'un des neuf codes de la section 13, seul, sans aucun texte après lui : pour `refus` et pour `autre` aussi, la ``⏎`` ligne `STATUT` porte `arret refus` ou `arret autre` seul ; le texte entier du refus, ou le motif de `autre`, va au fichier ``⏎`d'arrêt.`

**K4 (2, pièce 9)**
- ancien : `§ 2.1 (à partir de l. 122)`
- nouveau : `§ 2.1 (l. 122-191)` (le § 2.2 commence l. 192 ; sans borne, la lecture « à partir de » atteint les annexes de l. 772 et suivantes, qui nomment des chemins interdits)

**K5 (6.3, point 2, « dix clés »)**
- ancien : `` `SCELLEMENT-P3BIS`, `VERDICT-P3BIS`, `ISSUE-MOTS-ET-COUT-T06` (clés de l'étape B : R109, l. 2174-2178 ; G1 : R169), ``
- nouveau : la même suite, avec, dans la parenthèse : `(clés de l'étape B : R109, l. 2174-2178 ; G1 : R169 ; ces dix`⏎`   clés, de `SCELLEMENT-T07` à `ISSUE-MOTS-ET-COUT-T06` dans l'ordre écrit ici, sont « les dix clés de l'étape B » du point 5 ;`⏎`   `SCELLEMENT-T07` est permise, non exigée, à l'étape B),`

**K6 (6.3, point 2, clé d'une ligne)**
- ancien : `` `LECTURE-T08-BASE-A` (R110) et `SCELLEMENT-T08-BASE-A`. Absente ou en double : arrêt `piece-non-conforme`. ``
- nouveau : le même texte, suivi de : `La clé d'une`⏎`   ligne est son premier champ entre barres (après le préfixe `<n>:` de l'extrait), comparé par égalité exacte, jamais par`⏎`   recherche d'une sous-chaîne (`AUDIT-FUITES-T07` est une sous-chaîne de `CONSIGNE-AUDIT-FUITES-T07`).`

**K7 (6.1, ordre et codes)**
- ancien : `` Écart : arrêt `piece-non-conforme` ou `fichier-interdit-recu`. ``
- nouveau : `Ordre : (1) les noms sous `<ESPACE>/pieces/`, comparés aux chemins du bordereau et à la liste fermée, sans ouvrir aucun`⏎`fichier ; (2) seulement ensuite, les empreintes. Un nom hors du bordereau ou de la liste fermée : arrêt`⏎`` `fichier-interdit-recu` (le fichier n'est pas ouvert) ; un fichier du bordereau manquant, une empreinte, un compagnon ou une ``⏎`citation différents : arrêt `piece-non-conforme`.`

**K8 (2, « Comment lire le texte scellé »)**
- ancien : `**Comment lire le texte scellé** : par plages de lignes (numéros de la section 3), jamais en entier d'un seul geste. Une`
- nouveau : `**Comment lire le texte scellé** : par plages de lignes (numéros de la section 3), jamais en entier d'un seul geste (les`⏎`scripts de contrôle des sections 6.1 et 6.5 ouvrent les fichiers en entier et n'en affichent que les plages et les écarts). Une`

**K9 (1, lectures permises)**
- ancien : `` ni aucun autre fichier ou dossier que `<ESPACE>/pieces/`, le ``
- nouveau : `` ni aucun autre fichier ou dossier que `<ESPACE>/pieces/`, les fichiers que tu as toi-même écrits dans `<ESPACE>/verdict-ferme/`, le ``

**K10 (6, scripts)**
- ancien : `ils ne lisent que tes pièces et n'écrivent que leur sortie,`
- nouveau : `ils ne lisent que tes pièces (et, pour l'empreinte du verdict, ce verdict) et n'écrivent que leur sortie,`

**K11 (6.5, clés lues à la première passe)**
- ancien : `` `resultat.entrees`, `p3bis`, `table_A`, `doses`, `fuites`, `bases`, `scores_ouverts`, `scores_ii_ouverts`, ``
- nouveau : `` `resultat.entrees` (sous-clés `G`, `P`, `A`, `Q` et `F` seules), `p3bis`, `table_A`, `doses` (hors `etat_ii_par_dose_jugee` et ``⏎`` `ecart_a_la_base`), `fuites`, `bases`, `scores_ouverts`, `scores_ii_ouverts`, ``

**K12 (6.3, point 6, journal)**
- ancien : `` 6. Journal : une seule ligne `OUVERTURE-T07 … etape-B/…` ; ``
- nouveau : `6. Journal (le script « controles » n'affiche de la ligne `scores-t07/…` que sa clé, sa date et son chemin ; ce qui suit`⏎`   « (Q = » n'est lu qu'en 6.5, point 6, après tes dérivations) : une seule ligne `OUVERTURE-T07 … etape-B/…` ;`

**K13 (6.5, point 4, motif de Q « illisible »)**
- ancien : `` et tu vérifies ce motif sur la pièce 12 si tu le peux ; motif introuvable dans la ``
- nouveau : `et tu vérifies sur la pièce 12, si tu le peux, que le fait que ce motif décrit (clé absente, dose manquante, valeur hors`⏎`   domaine, `null` interdit) est exact (le motif est un message du module, non une chaîne de la pièce) ; fait décrit non retrouvé dans la`

**K14 (5, forme de l'extrait)**
- ancien : `` (toutes les lignes du registre, chacune précédée de son numéro, `<n>:| CLÉ | date | ``
- nouveau : `` (toutes les lignes du registre, chacune précédée de son numéro ; les lignes des trois sections portent le même préfixe `<n>:`, `<n>:| CLÉ | date | ``

**K15 (7, point 1, ensembles balayés)**
- ancien : `de son plancher. Sous une ligne où aucun score n'est ouvert, tu écris que rien n'est à juger.`
- nouveau : `de son plancher. Les balayages « aire hors de [0,05 ; 0,95] » et « quantile 0,95 d'un plancher au-dessus de 0,70 » portent sur`⏎`   toute lecture écrite qui porte une aire contre un plancher : `jeux`, `jeux_hors_jugement`, et les lectures de validité T7-P3,`⏎`   T7-P4, T7-P6, T7-P9, T7-P15 et T7-P18 ; jamais `couples_figes_descriptif` ni `planchers_p3_descriptif` (lecture de cette`⏎`   consigne : l'ensemble que le module balaie, le texte ne le bornant pas). Sous une ligne où aucun score n'est ouvert, tu écris que rien n'est à juger.`

**K16 (6.9, lecture prudente de la base (A) ; A6)**
- ancien : `jamais de ta main qu'un texte « ne porte rien » ni qu'un organisme « est flagrant » ; tu recopies.`
- nouveau : le même texte, suivi de : `Dans tous les cas (BA-L2`⏎`qui s'applique ou non), tu recopies une fois, à la section « Verdict », la phrase « Lecture prudente » de T08A l. 139 (R143), à`⏎`l'octet et entre guillemets (les mots « ne porte rien » et « flagrant » y sont une citation, non ton propos), et tu écris`⏎`« (lecture prudente de T08A l. 139) » après toute phrase de ton verdict sur le critère 3 (lecture de cette consigne, sens`⏎`prudent : une réserve gelée de plus, qui ne change ni ligne ni issue).`

**K17 (6.9, premier cas de BA-L2)**
- ancien : `- la ligne dit que BA-L2 **ne s'applique pas** : tu l'écris une fois, à la section « Verdict » ;`
- nouveau : `- la ligne contient la chaîne « ne s'applique pas » (recherche de chaîne ; forme que la session mère fixe en écrivant la ligne`⏎`  dédiée) : BA-L2 **ne s'applique pas** : tu l'écris une fois, à la section « Verdict » ;`

**K18 (6.9, deuxième cas)**
- ancien : `- la ligne dit que BA-L2 **s'applique** et porte le mot de Lazar : la réserve R-BA1 accompagne chaque phrase de ton`
- nouveau : `- la ligne dit que BA-L2 **s'applique** et porte le mot de Lazar (elle contient la chaîne « mot de Lazar », et non « ne`⏎`  s'applique pas ») : la réserve R-BA1 accompagne chaque phrase de ton`

**K19 (6.9, troisième cas)**
- ancien : `- la ligne dit que BA-L2 s'applique **sans** mot de Lazar, ou ne dit pas l'état : arrêt `ecart-au-texte` (R110, R191).`
- nouveau : `- la ligne dit que BA-L2 s'applique **sans** mot de Lazar, ou ne contient aucune des deux chaînes : arrêt `ecart-au-texte` (R110, R191).`

**K20 (6.4, point 2, marque d'un choix)**
- ancien : `Toute autre inégalité est écrite clé par clé et laissée en question.`
- nouveau : `Toute autre inégalité est écrite clé par clé et laissée en question (choix de cette consigne, pour ce point : le texte ne`⏎`   fait pas de l'égalité de la configuration et du manifeste un point de sa liste d'arrêt).`

**K21 (6.4, point 4, marque d'un choix)**
- ancien : `` Écart : écrit ; s'il touche une clé de l'étape B : arrêt `ecart-au-texte`. ``
- nouveau : `` Écart : écrit ; s'il touche une clé de l'étape B : arrêt `ecart-au-texte` (choix de cette consigne). ``

**K22 (facultative, 7, point 2)**
- ancien : `(lecture de cette consigne, sens prudent ; une réserve ne change pas la ligne).`
- nouveau : `(lecture de cette consigne : l'une ou l'autre lecture suffit, la large ne pouvant déclencher que si l'étroite le fait ; une réserve ne change pas la ligne).`

### Option de la mère (B2) : verdict assemblé par programme

Non comptée dans les corrections. Elle évite les fautes de recopie à la main (plusieurs centaines de nombres, cellules « à
l'octet ») ; elle n'ajoute aucun critère. Les six noms ci-dessous répondent au motif du bloc C7 (vérifié).
- **O1** : ancien : `sondes qu'après avoir écrit la sortie de la première passe (choix de cette consigne).` ; nouveau : le même texte, suivi
  de : `Chaque script écrit aussi, dans `<ESPACE>/verdict-ferme/`, un bloc Markdown prêt à insérer (`verdict-T0.7-etape-B-v1-bloc-controles-v1.md`, `…-bloc-entrees-v1.md`, `…-bloc-decisives-v1.md`, `…-bloc-complements-v1.md`, noms complets) ; tes passages de prose sont dans `verdict-T0.7-etape-B-v1-prose-v1.md` ; le verdict en prose est assemblé par `verdict-T0.7-etape-B-v1-assemble-v1.py` (`<PY> -I -B`, heure de fin passée en argument, relevée par `date -u` juste avant), qui insère les blocs tels quels ; tu ne retapes de ta main aucun nombre, aucune empreinte, aucune cellule recopiée (choix de cette consigne).`
- **O2** : ancien : `` - `verdict-T0.7-etape-B-v1-complements-v1.py` et `verdict-T0.7-etape-B-v1-complements-sortie-v1.txt` ; `` ; nouveau : la même
  ligne, suivie d'une puce : `` - `verdict-T0.7-etape-B-v1-bloc-controles-v1.md`, `verdict-T0.7-etape-B-v1-bloc-entrees-v1.md`, `verdict-T0.7-etape-B-v1-bloc-decisives-v1.md`, `verdict-T0.7-etape-B-v1-bloc-complements-v1.md`, `verdict-T0.7-etape-B-v1-prose-v1.md` et `verdict-T0.7-etape-B-v1-assemble-v1.py` ; ``
- Sans l'option : le risque est celui d'un nombre mal recopié dans un verdict que seule l'empreinte de la prose engage.

### Remarques facultatives (aucune n'est exigée)

- 6.0 et 11 : faire écrire la copie du message par un script, avec contrôle des deux empreintes de la copie contre celles du
  bordereau et de la consigne (m5).
- Corps du texte : écrire « ligne R9 », « réserve R10 », « règle R12 » (m14).
- `contradiction-consigne-texte` : seul code resté jugé ; repris de la consigne du lecteur A.
- Après remplacement du jeton de la commande v4, rejouer `verification_renvois_consigne_b_v2.py` avec l'empreinte définitive.

## 6. Ce qui a été éprouvé sans écart (pour ne pas le rouvrir)

- 194 renvois et citations ; sept empreintes de l'en-tête ; douze empreintes de code de la section 5 ; la ligne `CODE-T07` du
  registre égale à la « Nouvelle ligne » de l'addendum ; plages de lignes citées pour R176, la réserve de M3 et le contrôle
  « égalité » ; clés de la configuration (13 valeurs gelées toutes présentes, `controle_aire` = « egalite », `p064` vrai).
- Les dates du registre actuel (`SCORES-T07` et `SONDES-T07` avant `VERDICT-P3BIS`) : la branche G3 de 6.3 ne servira pas ;
  les lignes `-JD` et `-JA` présentes, `-JC` absente : la branche « les deux présentes » de 6.7 point 3 ne servira pas non plus,
  le motif de T7-P6 s'accorde alors au registre.

## 7. Points pour la session mère

1. **Ligne dédiée de BA-L2** : la consigne ne peut la lire mécaniquement que si elle porte, selon le cas, « ne s'applique pas » ;
   ou « s'applique » et « mot de Lazar » (K17 à K19). À écrire ainsi, ou à faire corriger K17 à K19 avant le sceau.
2. **R-BA1** : le texte (l. 2183) la confie à la session mère ; la consigne la fait aussi marquer par le lecteur (admis par la
   préférence prudente, sans effet sur la ligne). La session mère écrit la sienne dans son rapport, comme le texte le dit.
3. **K16** : recopier la lecture prudente de T08A l. 139 au verdict ajoute une réserve gelée ; aucun mot de Lazar n'est requis
   (aucune ligne, aucune issue ne change).
4. **Option B2** : à décider (verdict assemblé par programme, ou recopie à la main du lecteur).
5. **Aucune garde de contenu au bloc C7** : seuls les noms de fichiers sont filtrés ; un identifiant de modèle ou un nom
   d'organisme venu du manifeste (`versions`, `reglages`) recopié dans le verdict ne serait vu par personne ; à vérifier à la
   lecture du verdict par la mère.
6. **À réécrire au sceau** : la puce « État du fichier » (brouillon 3, « non contre-lu »), la puce « Rédacteur » (qui ne
   décrit que le premier rédacteur), le jeton `EMPREINTE-COMMANDE-V4-A-REMPLIR`. Après ces réécritures et K1 à K22,
   rejouer le programme de renvois (code 0 exigé).
7. **Tour suivant** : une contre-lecture différentielle suffit (les couples ci-dessus ; la pièce n'est pas à refaire).
8. **Exclusions** : j'ai lu le texte scellé de T0.7 ; je suis exclu des lecteurs de P3-bis, de l'étape B et de B bis.

## 8. Déclaration et incidents de ma main

- Jamais ouverts : aucun fichier sous `diag/`, `runs/`, `donnees/` (ni `sondes-t07.json`, ni `lecture-t07.json`, ni
  `audit-fuites-t07.json`, ni scores, ni manifeste de run) ; aucun fichier de `docs/verdicts/` ; rien de l'étape B bis, du
  bras d'attaque ni du mode tenu à l'écart ; `registres/decisions.md` seulement par la clé `R-2980` (une ligne).
- Incidents : (1) une recherche de mots sur T0.7 et sur les textes cités (motifs de l'étape B bis et du bras d'attaque) a
  affiché le début (60 à 100 caractères) de lignes d'en-tête qui nomment ces chemins : noms seulement, rien ouvert. (2) Les
  commandes de lecture de code ont écrit des copies jetables dans mon dossier de travail (scratchpad), jamais dans le dépôt.
  (3) La liste du dossier des procédures a affiché des noms de fichiers du compte 3 : aucun nom de l'étape B bis. (4) Aucun
  commit, aucune poussée, aucun réseau, aucune dépense ; la pièce n'est pas modifiée.
