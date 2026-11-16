# Consigne du lecteur B (verdict de l'étape B de T0.7) — rapport du rédacteur — v1

- **Statut** : rapport pour la session mère `session_016QhUrtmLyFWJP6Cy7rgfXH`, qui décide ; rien n'est décidé ici.
  Fichier neuf, scellé, non commité.
- **Rédacteur** : sous-agent neuf de la session mère (modèle B), rédacteur de la consigne du lecteur B ; travail du
  2026-11-16, de 12:06:55Z à 12:46:18Z (`date -u`, relevé au début et juste avant le sceau de ce rapport). Ni lecteur ni
  juge d'aucun verdict ; aucune donnée ni aucun résultat de 7a, de 7b ou de T0.7 ouvert.

## Verdict

1. **La consigne est écrite, vérifiée par programme et prête à être contre-lue** : la pièce à contre-lire est le
   **brouillon 2**, `consigne-lecteur-b-v1-brouillon2.md` (`6bcfa40005d8e194249568c98be6f855a39ac46792339bb6049895c892ecf421`).
   Le brouillon 1, demandé sous ce nom, existe et reste tel quel (scellé trop tôt, puis complété par un brouillon 2
   plutôt qu'écrasé : § 4 et § 10).
2. **Elle n'ajoute aucun critère** : 194 renvois au texte (fichier, ligne, citation exacte), tous retrouvés à leur ligne
   par programme ; aucun mot de la liste de contenu de la commande ; aucun nom de modèle.
3. **Six points demandent un mot de la mère avant le sceau** (§ 6 et § 7) : qui écrit la réserve R-BA1 ; pièces de
   l'étape A que le texte attend chez le lecteur et que la commande ne lui remet pas (`sondes-t07.json`) ; borne de la
   phrase gelée ; déclencheur « trop beau » ; audit de symétrie sur un jeu non décisif ; calcul de puissance.

## 1. Pièces produites (toutes dans ce dossier, scellées, compagnon égal, non commitées)

| pièce | empreinte | rôle |
|---|---|---|
| `consigne-lecteur-b-v1-brouillon2.md` | `6bcfa40005d8e194249568c98be6f855a39ac46792339bb6049895c892ecf421` | **la consigne à contre-lire** (958 lignes) |
| `consigne-lecteur-b-v1-brouillon1.md` | `44f0fd1e6c95a0ef833b63cb6d99e6b91bbe76a1e1b9892858ae3069254586f5` | premier jet, gardé (règle R12) |
| `rapport-redacteur-consigne-b-v1.md` | son compagnon | ce rapport |
| `verification_renvois_consigne_b_v1.py` | `db03961f32b67dc9a20f86dfbeadfedc153c671e5becac73cb545f2dcb20bc85` | pièce d'appui, non demandée : vérification par programme d'une version de la consigne (renvois, emplois, empreintes, noms, filtres) ; lecture seule |
| `verification-renvois-consigne-b-sortie-v2.txt` | `f571ea2aefe29140e155531367c45537d488a4ef78aa660b3dfa3b691e4b1b3e` | sortie sur le brouillon 2 : cas sain « CONFORME », code 0 ; cinq artefacts, code 1 chacun (règle R5) |
| `verification-renvois-consigne-b-sortie-v1.txt` | `6983e2ac15c4aa54444484c62565b9531b53308294647afaeb71344575f6c78d` | même sortie sur le brouillon 1 |

## 2. Pièces lues, avec leurs empreintes

**Procédure** (ce dossier), en entier : `commande-compte-3-phase-c-v3.md`
(`9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e`) ; `consigne-lecteur-a-v1.md`
(`b5abfa163dc26f5b21322280ffc3f005f3954e499e780d83276971deb92ed96f`) et sa contre-lecture,
`verification-courte-liste-v2-consigne-a-v1.md` (`f48db58adf154339a2e8ba61f9c8bf91923cab2caa092c9605de8b69a5708ba0`) ;
`verification-courte-commandes-v2-v3-v1.md` (`cb9757d53e1d4926e376d06a36391de341d8d1f62d48d7a59db1c47cb71f1b86`) ;
`calendrier-et-remise-phase-c-v3-v1.md` (`1dd534af0f75ac7a0ba454dc11a87ecf51631f5888a7d1f57d58dc714c2bad21`) ;
`preparation-phase-c-v3-mere-v1.md` (`31bfacd57c6d83d77dfb99a1a3c41a2543eb8e086d819ee24043deda6bdb8dd9` ; paru à 12:25Z,
lu alors : son § 1.4 confirme les contraintes que j'avais tirées de la commande).

**Textes scellés** :

| pièce | empreinte | ce que j'en ai lu |
|---|---|---|
| `prereg/T0.7-sondes-v0-v1.md` (ligne `SCELLEMENT-T07`) | `d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5` | l. 1 à 3 (titre, début du statut) ; l. 691-700 ; l. 914-1548 ; l. 1670-2039 ; l. 2091-2265 ; l. 2312-2411 ; l. 2466-2535 ; l. 2598-2660 ; l. 2671-2783 ; par recherche de mots : phrases isolées des l. 1549-1669, 2040-2090, 2412-2465 et 2662-2669, et courts fragments de dix lignes des l. 13-152 (noms de chemins interdits, affichés par le contrôle du filtre de contenu). **Non lu** : le reste des l. 4-690, l. 701-913, le reste des plages précédentes, l. 2784-3398 |
| `prereg/T0.7-sondes-v0-v1-addendum-cache-motifs-v1.md` | `8c377286f2fa9be7020416a1d25bbcebb8fad0944f14c508614519a6a0886dc8` | l. 1-140 et 251-391 |
| `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json` | `e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328` | toutes les clés |
| `prereg/T0.6-organismes-v0-v1.md` | `ef31feff9abb26d0d66c3c35f3c721ee7d054a63f880657535a5e4a47cbdf169` | l. 527-588, 763-772 ; titres |
| `prereg/T0.8-base-A-mots-et-cout-v1.md` | `72b067d5b3f8c0d7f257677dbc86ace6cd1917b07f7a96e2263b91647dc6205d` | l. 124-171 ; lignes isolées (13, 20, début de 51, 177, 205-206) ; titres |
| `docs/decisions/decision-N-063-v2.md` | `b2d9f03543802f82890c99eff77d4aab34ad532b50986b887c046906914b625b` | en entier |
| `prereg/T0.7-consigne-audit-fuites-v1.md` | `43102e80332cd138305604b7cffb2dc77a1584a7ad0b48584c7506ea377b3a5d` | l. 1-20, 110-124, 530-565, 629-704 ; fragments des l. 785 et 794 (même contrôle) ; titres |

**Code du module de T0.7** (pour l'aide « où les nombres sont écrits », section 5 de la consigne ; même geste que le
rédacteur de la consigne A) : au commit que cite la ligne `CODE-T07` (`c2fab6cc7267b76228a75dc3e2e08bc7aa038961` ;
`registres/code-t07/CODE-T07-v3.json`, `d3eaebfe1842f06c042e4cfffc2038f08973a544a8a10ccffa0c6109a566c218` ;
`src/controle_ia/t07/` de `main` égal à ce commit, vérifié par `git diff`) : `lecture_v4.py` (`42f60780…`, fonctions
`etape_b`, `lecture_planchers_p3`, `exiger_nombre_de_directions`, `reserves_plancher_figees`, et l'appel de
`creer_manifeste`) ; `lecture_v3.py` (`ac3666e4…`, `lecture_jeux_v3`) ; `lecture_v2.py` (`709b2feb…`, `ouvrir`) ;
`lecture_v1.py` (`62b34790…`, signatures et retours de cinq fonctions) ; `criteres_v1.py` (`12b999fe…`, constantes,
états, `entree_F`, `mention_dose`, `regles`, `issue_critere_3`) ; `plancher_v2.py` (`a0f80e68…`,
`comparer_difference_au_plancher`, `resume_pour_critere`) ; `plancher_v1.py` (`ac6e8263…`, `niveau_bonferroni`,
`predicteurs_triviaux`) ; `lectures_t07_v2.py` (`1f523c07…`, `lectures`) ; `lectures_t07_v1.py` (`01904d94…`,
`difference`, `placebo`, `_prediction_validite`, `reserves`) ; `registre_v1.py` (`e5023657…`, deux fonctions du
journal) ; `src/controle_ia/manifeste.py` (`1a5c7464…`, trois fonctions) ;
`src/controle_ia/premier_test_ia/statistiques.py` (`a8552575…`, `aire_simple` seule). Empreintes entières : section 5 de
la consigne.

**Registres** (clés, dates, chemins, empreintes seulement) : `registres/scellements-v1.md`
(`18e5fe518c6027a868a60bf89f6d3eac63ac65c717d2cc37105225b4a96cc517`, quinze lignes) ; trois lignes de
`registres/decisions.md` prises par leur clé (R-2718, R-2813, R-2971), plus un fragment de la ligne 2785, affiché par une
recherche (§ 10).

**Jamais ouvert** : aucun `diag/`, `runs/` ni `donnees/` de 7a ou de 7b ; aucun score ; `audit-fuites-t07.json` et
`verdict-P3-bis-v1-issue.json` (présence et compagnon seulement) ; aucun verdict de T0.6, de P3 ou de P3-bis ; rien de
la liste interdite de mon brief ; rien de l'étape B bis (ni son texte, ni son registre) ; `lecture-t07.json`,
`manifeste.json` du run de T0.7 et le fichier « mots et coût » n'existent pas sur `main` (constaté par leur nom).

## 3. Renvois au texte scellé : chacun vérifié (ligne et citation)

- **Table 3.2 de la consigne** : 194 renvois `Rnnn | fichier | ligne | citation` — T0.7 : 172 ; T0.6 : 9 ; consigne de
  l'audit : 5 ; base (A) de T0.8 : 4 ; N-063 v2 : 2 ; addendum : 2. Chaque citation est une sous-chaîne exacte de la
  ligne citée (contrôle 1 du script) ; chaque renvoi est employé dans le corps, aucun renvoi du corps n'est inconnu
  (contrôle 2). Sortie : `verification-renvois-consigne-b-sortie-v2.txt`.
- **Plages de lignes citées dans le corps** (hors table) : 58 plages éprouvées par programme, chacune par un ou deux
  mots-clés de son début et de sa fin, aucun absent. Liste (fichier, plage, mots-clés) :

| fichier | plages éprouvées |
|---|---|
| T0.7 | 1-913 (« ## En-tête ») ; 914-998 ; 1009-1063 ; 1065-1156 ; 1101-1106 (« égalité », « ligne L7c ») ; 1109-1111 ; 1124-1126 (« trois marques ») ; 1130-1131 ; 1158-1184 ; 1186-1254 ; 1226-1232 ; 1256-1312 ; 1272-1276 ; 1298-1312 ; 1373-1394 ; 1413-1416 ; 1459-1520 ; 1496-1497 ; 1507-1509 ; 1538-1543 ; 1670-1781 ; 1802-1811 ; 1813-1836 ; 1813-1815 ; 1816-1817 ; 1817-1828 ; 1829-1832 ; 1831-1832 ; 1832-1833 ; 1833-1836 ; 1837-1896 ; 1898-1942 ; 1903-1916 ; 1935-1938 ; 1944-2024 ; 2026-2037 ; 2174-2192 ; 2174-2178 ; 2194-2209 ; 2466-2507 ; 2509-2531 ; 2601-2660 ; 2668 ; 2679-2760 |
| T0.6 | 527-541 ; 573-585 ; 763-771 |
| base (A) de T0.8 | 124-141 |
| consigne de l'audit | 110-118 ; 122 ; 530-549 ; 642-647 ; 677-703 |
| addendum | 1-43 ; 83-96 ; 251-265 ; 267-299 |
| N-063 v2 | 1-26 |

- **Conséquence pour le sceau** : la consigne fait rejouer ce contrôle au lecteur (section 6.1 : une citation absente
  de sa ligne arrête, `piece-non-conforme`). **Après toute retouche de la consigne, rejouer le script avant de sceller**
  (`python3 -I -B verification_renvois_consigne_b_v1.py <racine> <consigne> [motif des noms de modèles]`, code 0).

## 4. Du brouillon 1 au brouillon 2 : neuf retouches

Le brouillon 1 a été scellé avant ma dernière relecture ; je ne l'ai pas écrasé (règle R12). Le brouillon 2 est le
brouillon 1 plus :

1. titre et puce « État du fichier » (brouillon 2, base citée par son empreinte) ;
2. note « Trois familles de noms » remise en lignes (forme seule) ;
3. plage « à parcourir sans étudier » : l. 1837-1896 au lieu de 1836-1896 (la l. 1836 finit la définition de F) ;
4. plages « à consulter » étendues : l. 2660 (accord au code, point 12 : T7-P10 de la tromperie et des enjeux) et
   l. 2668 (réserve CLC-07) ;
5. aide de la section 5 : domaines des valeurs que le module écrit (`entrees`, `sous_phrase_L1b`, `sous_phrase_L7`,
   `etat`), pour éviter un faux désaccord de forme ;
6. dérivation de Q : le défaut de P-064 nommé (clé `p064` de la configuration) ;
7. réserve R15 jugée par la condition de sa ligne sur l'extrait ; cas CLC-07 du texte (T7-P9 « non lue » sans R15)
   écrit comme désaccord non tranché ;
8. lignes L1b et L7 : la cellule entière recopiée, puis la phrase qui s'applique, seule (section 6.8 et section 12) ;
9. P3 : aucun nombre de P3 comparé de la main du lecteur.

## 5. Choix de rédaction

1. **Renvois, non recopie** : la consigne ne recopie pas les critères ; elle donne section, ligne et citation courte
   (brief de la mère). La consigne A et le plan de forme du préparateur recopiaient à l'octet. Une annexe « à l'octet »
   des l. 1898-1936 peut être ajoutée par programme si la mère la préfère.
2. **Plages de lecture** : le texte fait 754 Ko, avec des lignes de plus de 13 000 caractères ; la consigne dit quelles
   plages lire en entier (environ 100 Ko), lesquelles consulter (environ 92 Ko), lesquelles laisser.
3. **Interdits du message non recopiés** (la consigne A les recopiait) : la ligne du message nomme l'autre étape et des
   chemins que le filtre de contenu toucherait. La consigne dit qu'ils « valent en entier » et interdit, sans la nommer,
   toute écriture sur une autre étape ou lecture du programme. Zéro ligne touchée par `INTERDITS_CONTENU_B`.
4. **Liste fermée positive des pièces** (quatorze lignes) au lieu d'une liste de fragments de noms interdits (même
   raison) ; chemins de la consigne et du fichier « mots et coût » pris du message et de l'extrait, non écrits en dur.
5. **Trois passes** dans l'ordre du plan, point 8 : entrées P, A, Q, F dérivées avant toute lecture des sondes ; puis
   lectures décisives et ligne ; puis placebo, audit, validité, descriptif, effectifs, réserves.
6. **Le lecteur dérive lui-même** Q (du fichier « mots et coût »), F (du fichier d'audit), les états des sondes, de (i)
   et de (ii), puis la ligne, et compare à la ligne mécanique : **ligne ou sous-phrase différente : arrêt**
   `desaccord-ligne-mecanique` (repris de la consigne A). G et A ne viennent que du module (pièces non remises).
7. **Neuf codes d'arrêt**, dont deux neufs : `critere-inapplicable`, `ecart-au-texte` (valeur gelée, date, fermeture,
   liste d'arrêt, état de BA-L2).
8. **Fichier d'issue** à quatre clés (`etape`, `ligne`, `verdict`, `verdict_sha256`) : le texte n'en fixe pas pour ce
   verdict ; les sous-phrases et les réserves restent dans la prose.
9. **Sceau** : aucun compagnon écrit par le lecteur (le bloc C7 scelle les copies) ; son engagement est l'empreinte du
   verdict dans le fichier d'issue.
10. **Rapport final de quatre lignes** (R-V2) ; constat M4 de la contre-lecture de la consigne A réglé (ce que porte
    la ligne STATUT sur un refus).
11. **Symétrie R4** : forme gelée (déclencheurs de R7 et de R9, audit du fichier) jugée quel que soit le sens de la
    ligne ; ce qui paraît trop propre hors des déclencheurs gelés s'écrit en question, sans seuil neuf.
12. **Identifiants** : aucun nom de modèle ni identifiant servi ; le lecteur ne recopie pas les l. 1-913 du texte ni
    l'en-tête de la consigne de l'audit, qui en portent.
13. **Aide des clés** tirée du code au commit de `CODE-T07` ; « le fichier fait foi ».

## 6. Points où le texte scellé paraît ambigu pour un lecteur (je ne tranche pas)

| n° | où | ambiguïté | ce que fait le brouillon 2 |
|---|---|---|---|
| A1 | T0.7 l. 2183 | la réserve R-BA1 est écrite « à côté de toute phrase sur le critère 3 (par la session mère, dans le rapport du verdict […]) » : est-ce le lecteur qui la porte dans son verdict, ou la mère dans un rapport à part ? La commande remet pourtant la ligne dédiée de BA-L2 au lecteur | section 6.9, « lecture de cette consigne » : le lecteur recopie la ligne ; si elle dit « s'applique » avec le mot de Lazar, il marque « (réserve R-BA1) » après chaque phrase sur le critère 3 et recopie une fois la phrase gelée de BA-L2 ; sans mot de Lazar ou sans état : arrêt |
| A2 | T0.7 l. 1903-1916 | le texte ne borne pas la « phrase gelée » dans la cellule « lecture » (T0.6 écrivait « les phrases entre guillemets sont gelées ») ; les cellules mêlent phrases, consignes de rapport et renvois aux brouillons. La phrase que le module écrit n'est pas la cellule à l'octet : pour L4, le code (`criteres_v1.py`, `PHRASES`) ne porte pas les réserves de l'audit de P3 que le candidat 2 a jointes à la cellule | section 6.8 : cellule entière recopiée, `resultat.phrase` en regard, différence écrite, non tranchée |
| A3 | T0.7 l. 1928 | « effet observé « trop beau » (toutes les sondes au-dessus sur tous les jeux) » : « tous les jeux » n'est pas borné ; le code le juge sur les jeux décisifs. De même, l'ensemble des lectures que balaient « aire > 0,95 ou < 0,05 » et « quantile 0,95 d'un plancher > 0,70 » n'est pas borné (le code balaie lectures décisives, hors jugement et de validité, non les couples descriptifs) | section 7 : « trop beau » jugé sous les deux lectures, réserve écrite si l'une déclenche (sens prudent) ; pour les deux autres, le lecteur juge ce que le fichier porte et écrit tout désaccord avec le module |
| A4 | T0.7 l. 1924, 1928 | audit de symétrie sur un jeu **non décisif** : R7 le veut « avant tout verdict de G0 », R9 « avant tout verdict », et la l. 1924 dit qu'il « suit l'étape B, hors F » ; ni qui le fait, ni s'il précède le verdict B | section 7 : le lecteur ne le fait pas (aucune pièce) ; il écrit « audit dû, non fait par ce verdict », en question |
| A5 | T0.7 l. 2036 | la lecture d'un « non détecté à cette puissance » est définie par une aire minimale tirée du quantile et de la demi-largeur « lus au résultat » ; le texte ne dit pas si le verdict la calcule (formule de la l. 2030, à lire avec soin) | section 6.8 : calcul interdit, phrase recopiée, question écrite |
| A6 | base (A) de T0.8, l. 139 | « lecture prudente, à écrire telle quelle avec toute phrase sur le barreau 3 » : T0.7 ne la reprend pas ; le verdict B porte des phrases sur ce que la base dit des doses | section 6.9 : le lecteur n'écrit rien de sa main sur la base ; il ne recopie pas la phrase de T0.8 |
| A7 | addendum, l. 40-43 | la pièce se dit « brouillon 3, non scellé au sens d'un préenregistrement », sans ligne au registre ; le lecteur ne peut pas établir qu'elle est en vigueur | section 6.3 : il compare la ligne `CODE-T07` à la « Nouvelle ligne » de l'addendum et écrit l'écart sans le juger |

## 7. Ce que le texte attend du lecteur et que la commande ne lui remet pas

| pièce absente du bac (bloc C5) | ce que le texte en attend | effet dans la consigne |
|---|---|---|
| `diag/<run de T0.7>/sondes-t07.json` | l. 2659 : « le vrai motif est écrit dans `sondes-t07.json`, où le lecteur du verdict (R13) le lit » (défaut DF-05 de T7-P6) ; l. 1539 : effectifs « paires des jeux » ; sondes principales et règle d'ex aequo | « non remis », question ; motif de T7-P6 comparé aux lignes des jeux de l'extrait |
| `notation-t07.json`, rapport de la réextraction, `ouverture-t07.json` | l. 1518-1519 : paliers de la garde de la réextraction ; entrée G (garde d'identité) | paliers pris des réserves que le module recopie ; G prise du module seul |
| `diag/<run de 7b>/lecture-cout-t06.json` | l. 1539-1541 : table A de T0.6 | A prise du module seul (`resultat.table_A`) |
| journal et verdict en prose de P3-bis | G3 ; `verdict_sha256` | « non vérifiable depuis mes pièces » |

Le bloc C2 place déjà `sondes-t07.json` et son compagnon dans la racine de l'hôte, et son empreinte est la ligne
`SONDES-T07`. L'ajouter au bac demande une version nouvelle de la commande (bloc C5) et une retouche de la consigne
(liste des pièces, 29 lignes au bordereau, motif de T7-P6, effectifs). **Options** : (a) remettre telle quelle, le
lecteur écrit « non remis » — rapide, mais le verdict laisse ouverts DF-05 et les paires des jeux ; (b) version 4 de la
commande avec cette pièce — conforme à la lettre de la l. 2659, au prix d'une répétition du bloc C5. Constat de registre à
12:07Z (`registres/scellements-v1.md`, `18e5fe51…`) : lignes `-JD` et `-JA` présentes, aucune ligne `-JC` ni
`SCELLEMENT-CONCEPTS-T07`. Recommandation : (a), parce que la ligne `-JC` manque : le motif « jeu J-A ou J-C non scellé »
que le module écrirait pour T7-P6 est alors vrai, et la question de DF-05 tombe ; restent les paires des jeux, écrites
« non relevées » ; confiance 0,6.

## 8. Fichiers à donner au contre-lecteur de la consigne

Le contre-lecteur lit le texte scellé de T0.7 : il doit en avoir le droit, et il devient exclu des lecteurs de P3-bis.
Il n'est ni le lecteur B ni un lecteur d'une autre étape. Le rédacteur étant en modèle B, il est d'un autre modèle
(R-2813). Il ne lit aucune donnée ni aucun résultat.

1. `consigne-lecteur-b-v1-brouillon2.md` (`6bcfa400…`) : la pièce ; `consigne-lecteur-b-v1-brouillon1.md`
   (`44f0fd1e…`) pour le différentiel seulement.
2. Ce rapport ; `verification_renvois_consigne_b_v1.py` (`db03961f…`) et sa sortie v2 (`f571ea2a…`), à rejouer.
3. `commande-compte-3-phase-c-v3.md` (`9d788919…`) : § 0, § 2, blocs 1C, C5, C6, C7, F-C.
4. `consigne-lecteur-a-v1.md` (`b5abfa16…`) et `verification-courte-liste-v2-consigne-a-v1.md` (`f48db58a…`) ;
   `verification-courte-commandes-v2-v3-v1.md` (`cb9757d5…`, R-V2) ; `preparation-phase-c-v3-mere-v1.md`
   (`31bfacd5…`, § 1.4).
5. Les textes cités : `prereg/T0.7-sondes-v0-v1.md` (plages du § 3), son addendum, sa configuration ;
   `prereg/T0.6-organismes-v0-v1.md` ; `prereg/T0.8-base-A-mots-et-cout-v1.md` ; `docs/decisions/decision-N-063-v2.md` ;
   `prereg/T0.7-consigne-audit-fuites-v1.md`.
6. Pour la section 5 seulement : le code du module au commit `c2fab6cc…` (fichiers du § 2).

À lui demander : chaque « lecture de cette consigne » et chaque « choix de cette consigne » ; les sections 6.5 à 6.7
contre les l. 1459-1520 ; la section 4 contre les l. 1813-1836 ; les clés de la section 5 contre le code ; les
quatorze pièces contre le bloc C5 ; le motif des noms contre le bloc C7 ; les quatre lignes contre le bloc F-C.

## 9. Déclaration d'exclusion

Je suis un sous-agent neuf de la session mère `session_016QhUrtmLyFWJP6Cy7rgfXH`, modèle B, lancé le 2026-11-16 à
12:06Z pour écrire la consigne du lecteur B. J'ai lu le texte scellé de T0.7 (plages du § 2), son addendum, sa
configuration, le code de son module au commit de `CODE-T07`, des passages de T0.6, de la base (A) de T0.8, de la
consigne de l'audit des fuites, et la décision N-063 v2 (empreintes : § 2). **Je suis de ce fait exclu de tout rôle de
lecteur de P3-bis.** Par prudence, je me tiens aussi exclu du rôle de lecteur B, de la contre-lecture de ma propre
consigne et de l'analyse du verdict B. À inscrire par la mère à la liste « qui a lu quoi ».

## 10. Incidents de ma main, et ce que je n'ai pas fait

1. **Sceau trop tôt** : j'ai scellé le brouillon 1 avant ma dernière relecture. Je ne l'ai pas modifié ; le brouillon 2
   porte les retouches (§ 4). Deux fichiers au lieu d'un.
2. **Trois pièces d'appui non demandées** (script et deux sorties) : utiles au contre-lecteur et au sceau ; la mère
   peut les laisser hors du dépôt.
3. **Nombres de P3 lus dans des textes permis**, jamais dans un fichier de P3 : T0.7 l. 2028-2037 (« Puissance »),
   l. 1030, 1163 et 1912 (réserves de l'audit de P3) ; consigne A et T0.6 l. 564-571 (effet du témoin de P3, seuil de
   l'audit) ; base (A) de T0.8, l. 51, début de la ligne (une valeur de référence de la prédiction BA-P1).
4. **Identifiants de modèle vus, non recopiés** : en-têtes de T0.7 (l. 3, l. 693-695, mentions dans la section
   « Module ») et de la consigne de l'audit.
5. **Fragment hors sujet du registre des décisions** : une recherche de la convention des lettres de modèle a affiché
   environ 500 caractères de la ligne 2785 (un plafond et un cumul de dépense d'une autre tâche ; aucun résultat).
6. **Noms listés, rien d'ouvert** : `docs/verdicts/` (noms), `diag/20261114-001352-t07-lecture-reel/` (deux noms),
   nombre d'entrées de `runs/`.
7. **Identifiant de session** lu par son nom de variable, pour l'en-tête ; aucune valeur de clé, jamais `env` ni
   `printenv`.
8. **Non fait** : aucun commit, aucune poussée, aucun `git fetch`, aucun clone, aucun réseau, aucun appel payant, aucun
   `pytest`, aucun calcul lourd, aucun message à une autre session, aucun fichier existant modifié. La consigne n'est
   pas contre-lue (règle R2) : elle ne régit rien avant la contre-lecture et le sceau de la mère.
