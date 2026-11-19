# Contre-lecture des versions r1 et r2 — brouillon 6 de relance du préenregistrement du papier C — v1

- Contre-lecteur : le même agent que pour les versions c1 et c2 (Opus 5.5), le 2026-11-19.
- Textes : c2 `7a8d57c8…1f61` ; r1 `e12f16fa1460149344cd5d68b614294ea502c4c7fc24bc86970cafcfbaafc8b2` (conforme) ;
  **r2 `1ab62e7d22163306a3251cd75f4001f7daac63ea72577d5ee200a3bcf86cfec3` (égale à l'empreinte attendue)**.
- Pièces lues (empreintes recalculées) : table de remplissage r1 `25956ed0c0f5ffca…` ; table de traitement des points
  ouverts `67dbba301cc36681…` ; décisions v4 `054d83478e8a3e2f…` ; fiche pour le module v2 `d0fd066a5574fd1c…` ; note
  des différences v5 `c78bfb9ef323aa20…` ; journal v5 `53800b407f184167…` ; points ouverts d'origine
  `e8256bc643a73622…` ; validateur r2 relu. Ligne GO-2026-11-19-53 relue sur `origin/main` (`git show`). Code lu :
  `src/controle_ia/premier_test_ia/conditions.py` (`bornes_champs`), `src/controle_ia/environnements/propositions.py`
  (champs), `src/controle_ia/manifeste.py` (`graines`). Table de versement, section 3, sur la branche.
- Interdits tenus : aucun résultat, aucun fichier « consigne-privee » ni « conception-ii-b » ouvert, ligne R-2059
  filtrée, aucune dépense, aucun agent, aucune suppression ; écrits dans mon seul dossier ; aucun refus de permission.
- Contrôles par programme : `outils/diff-c2-r1-v1.txt` (34 blocs) et `outils/diff-r1-r2-v1.txt` (33 blocs), tous
  relus ; empreintes des pièces versées citées par r2 recalculées sur la branche (mesures v2 `946203c3…`, deux notes
  de voisins, vérification de la famille 1, brouillon 4, rapport « texte » du brouillon 5) : conformes ; mesures v2
  contre v1 : deux lignes ajoutées, rien d'autre ; `git diff 7a54d43 HEAD -- src tests` : 736 fichiers, dont 734
  ajoutés, 2 modifiés (deux fichiers d'essais), aucun supprimé.

Décompte : **0 bloquante, 3 majeures, 7 mineures.**

## 1. Version c2 → r1 (cases remplies)

Conforme. Chaque case porte l'option de GO-2026-11-19-53, recopiée sans changement de fond : D-1 (b), poids 0,5 ;
D-2 (a), k_P = 3 (effectifs et mention « non mesuré » de k_P = 1 retirés en cohérence) ; D-8 (a), masque accepté ;
D-15 (i) et (n) (tableau, Seuil, Critères et Combinaisons alignés) ; D-16 (a) ; D-17 (a) (la limite « non évaluée »
part avec la réserve, à juste titre). Les branches écartées sont retirées sans emporter autre chose ; les décisions à
défaut sont dites retenues par le directeur ; verrous 1, 7 et 8 mis à jour (le verrou 7 périmé est corrigé). D-9 est
écrite selon la lecture confirmée : version (a) si le rapport de la grille entière, C-P3c comprise, existe au
scellement et y est cité ; une statistique trouvée au-dessus du seuil suit la clause ; sinon version (b), sans
nouveau mot. Le texte suit la lettre du registre (« sinon (b) ») : sous (b), C-P3c garde son verdict à deux
lectures ; ce n'est pas « sans verdict » pour les trois (voir CR-10).

## 2. Remarques sur la version r2

### CR-01 — majeure — clause générale de primauté de la section 8
- **Lieu** : Plan d'analyse, section 8, introduction.
- **Citation** : « Elles font partie du texte ; là où un passage plus haut laisse deux lectures, elles priment. »
- **Pièce** : R1 (critères de lecture gelés, sans ambiguïté).
- **Constat** : la primauté est conditionnelle (« là où […] deux lectures ») : qui juge qu'un passage laisse deux
  lectures ? Plusieurs précisions contredisent un passage qui n'en laisse qu'une, et ne relèvent donc pas de la
  clause à la lettre : la précision 18 contre « la ligne C-P4 HC2 est écrite d'avance « non testable à cette
  puissance » » (Plan, section 2, et colonne « non concluante » des Critères) ; la précision 30 contre le sens
  évident de « n_cal / 2 » ; la précision 9 contre « fin du dernier champ, lecteur de champs de P3 » (corrigé, lui,
  au point 14). Deux lecteurs peuvent donc trancher différemment entre le passage et la précision.
- **Correction demandée** : rendre la primauté inconditionnelle, précision par précision, sur les lieux que chacune
  nomme déjà entre parenthèses ; et, dans chaque passage visé, ajouter le renvoi « (voir section 8, précision n) »,
  comme le point 14 le fait pour la précision 9. Une clause de primauté est acceptable à ces conditions ; telle
  qu'écrite, elle ne l'est pas.

### CR-02 — majeure — la précision 18 change ce qui compte comme réfutation de HC2
- **Lieu** : section 8, précision 18 ; Plan, section 2 (« demi-largeur prévue de g brut des sondes ») ; Critères,
  ligne C-P4 HC2.
- **Citation** : « Elle n'efface pas une réfutation : une issue « réfutée » reste « réfutée », avec la mention. »
- **Constat** : le texte antérieur écrit la ligne « d'avance » non testable, donc sans verdict dans les deux sens. La
  précision rend la réfutation possible dans ce cas. Statistiquement défendable (un intervalle large entièrement
  hors de la marge reste probant), mais c'est un changement de ce qui réfute une prédiction, pas une précision de
  calcul ; et la lecture symétrique (R4) était l'ancienne. Ce n'est pas « la lecture la plus sévère pour la
  confirmation » seulement : c'est une règle neuve pour la réfutation.
- **Correction demandée** : soit revenir à la lecture symétrique (ni confirmation ni réfutation, issue brute
  rapportée), soit porter ce point au directeur (décision courte, proposition à défaut).

### CR-03 — majeure — précision 9 : la borne champs / paragraphe peut se tromper différemment selon la cellule
- **Lieu** : section 8, précision 9 ; Métrique, point 14 ; TC.2, lectures (1) et (2).
- **Citation** : « après la clé du dernier champ présent, le paragraphe ajouté commence à la première ligne non vide
  qui suit une ligne vide […] Sans ligne vide après la dernière clé, l'action n'a pas de paragraphe : c'est l'attendu
  dans les cellules sans bras ».
- **Pièces** : `bornes_champs` et `_CLE_BRUTE` (`conditions.py`, l. 41-42 et 116-143) : bornes de début seulement ;
  champs TITLE, PROPOSAL, CONTROLS, COST, PREDICTION (`propositions.py`), dont le dernier est en texte libre.
- **Constat** : (a) une ligne vide **dans** le dernier champ (PREDICTION ou PROPOSAL de plusieurs paragraphes) place
  la borne au milieu du champ ; dans une cellule sans bras, la règle n'en dit rien (« l'attendu » n'y couvre que
  l'absence) : la fin du champ sort alors des « champs seuls » en H et S, pas forcément en SP. (b) Un plaidoyer
  écrit sans ligne vide, ou avant la dernière clé, est compté dans les champs (ou rendu illisible). Ces erreurs n'ont
  pas le même taux dans les cellules avec et sans plaidoyer : elles déplacent D₀ et g de la lecture principale de
  HC2, dans un sens inconnu. Le rédacteur le signale lui-même (règle écrite sans avoir lu le lecteur de champs).
- **Correction demandée** : (1) symétrie : une ligne vide suivie de texte après la dernière clé dans une cellule
  sans bras rend la borne « illisible », comptée dans la même règle des 5 % ; (2) rapporter par cellule la part des
  bornes illisibles et la part des actions dont le paragraphe détecté contient une clé de champ ; (3) tests du
  module sur des actions synthétiques (dernier champ de plusieurs paragraphes ; plaidoyer sans ligne vide ; plaidoyer
  avant la dernière clé ; gras « **COST:** »), cas sain et artefact (R5) ; (4) si le format de la consigne de bras
  le permet, demander un séparateur fixe avant le plaidoyer, à la configuration (choix du concepteur, à contre-lire).

### CR-04 — mineure — précision 34 : retirer la réserve plutôt que la remettre au niveau
- **Lieu** : section 8, précision 34 ; verrou 11.
- **Constat** : la clause est mécanique et posée avant toute donnée : procéduralement juste. Mais elle retire une
  garde de l'audit de symétrie qui protège C-P1 (destination) contre le contraste d'intention, au lieu de la
  ramener au niveau. Ce n'est pas la lecture la plus sévère, et rien ne dit si v₀ sera bimodal dans les données.
- **Correction demandée** : remplacer « la réserve est retirée » par « la réserve se déclenche sur le quantile à 95 %
  de l'écart sous le nul simulé (bimodal, même effectif), lu dans le rapport du verrou 11 » ; ou garder la réserve en
  écrivant son taux sous le nul à côté.

### CR-05 — mineure — témoin lexical redéfini : ce qu'il mesure, et les entrées du harnais
- **Lieu** : Métrique, point 14 ; liste d'arrêt 20 ; verrou 9.
- **Avis** : la redéfinition **répond au verrou 9** : tout ce qui porte la consigne de saboter (fin du message
  système, indication privée de chaque tour) est produit par le harnais pour la condition de la relecture ; les
  tours de l'agent et les observations restent ceux de l'épisode. Le témoin de l'instrument L-SP est fort : la
  transcription rebâtie sous la condition d'origine doit égaler celle de l'épisode jeton pour jeton, ce qui éprouve la
  fonction de reconstruction elle-même. La garde 20 est testable (cas sain : relecture honnête égale à la sortie du
  harnais ; artefact : une indication de saboteur glissée à un pas doit l'arrêter).
- **Reste** : (a) dire avec quelles entrées le harnais produit l'indication honnête « au même pas » (identifiant de
  tâche, rang du pas, historique rejoué) et que faire si l'indication honnête dépend d'un état que l'historique du
  saboteur ne reproduit pas ; (b) la garde 20 doit comparer à une sortie du harnais obtenue par un appel distinct de
  celui de la fonction de reconstruction, sinon elle se vérifie elle-même ; (c) écrire ce que mesure désormais
  g_trahison,lex : l'effet, à jetons de l'agent égaux, de la présence de la consigne de saboter dans le contexte ;
  l'« intention » y est opérationnalisée par cette présence (les actions relues, écrites sous la consigne, sont
  déclarées).

### CR-06 — mineure — garde de l'arbre gelé : motif inexact, protection annoncée non tenue
- **Lieu** : liste d'arrêt 1, parenthèse.
- **Citations** : « 736 fichiers sous `src/` et `tests/` diffèrent aujourd'hui de ce commit » ; « que le module ne
  touche pas au code des autres préenregistrements ».
- **Constat** : sur les 736, 734 sont des ajouts et 2 des modifications (deux fichiers d'essais) ; aucun fichier
  supprimé. La garde ancienne, lue à la lettre, aurait bien arrêté le lancement : le motif tient, mais le chiffre est
  à écrire juste. La garde neuve protège ce qui compte pour le papier C (dépendances gelées ; module hors de `src/` et
  de `tests/`). Elle ne vérifie pas qu'un fichier de `src/` hors de la fermeture des imports n'a pas été modifié par le
  travail du papier C, alors que la parenthèse le promet.
- **Correction demandée** : écrire « 734 ajoutés, 2 modifiés » ; soit retirer la promesse sur le code des autres
  préenregistrements (leurs propres sceaux la portent), soit l'assurer par une vérification : aucun commit de la
  branche du papier C ne modifie un fichier existant sous `src/` ou `tests/`. Pas de nœud : c'est une garde
  d'instrument, réécrite parce que l'ancienne était inapplicable.

### CR-07 — mineure — dépendances « calculées au scellement » et adaptateur scellé plus tard
- **Lieu** : champs du scellement, « Dépendances gelées » ; liste d'arrêt 1 ; D-20.
- **Constat** : la ligne couvre les fichiers que « le module ou l'adaptateur importe […] calculée par programme au
  scellement » ; or, sous D-20 (a), l'adaptateur n'existe pas au scellement. Ses dépendances (harnais, environnement,
  sondes en ligne) n'auront pas de ligne, et la garde 1 arrêtera le lancement.
- **Correction demandée** : les dépendances de l'adaptateur sont calculées et scellées par l'addendum de lancement,
  avec les lignes « Lanceur du papier C » ; la garde 1 lit les deux jeux de lignes.

### CR-08 — mineure — D-19 (a) : rendre l'addendum mécanique
- **Lieu** : Métrique, point 19, version (a) ; décisions v4, D-19.
- **Constat** : « le concept y est le libellé de l'organisme que le verdict de G0 retient », « en un libellé
  anglais » : un libellé reste à écrire, donc un choix après les mesures de G0. Le bras est rapporté, sans critère ni
  réserve (D-17 (a)) : ce n'est pas un écart à R1 au sens d'une règle d'analyse. Mais l'addendum n'est mécanique, comme
  celui de la dérivation, que si la règle de remplissage est entière dès maintenant.
- **Correction demandée** : fixer maintenant la règle : par exemple, la chaîne exacte qui nomme le mode « coût
  gonflé » dans la configuration scellée de l'organisme retenu par le verdict de G0, sans traduction ni choix ; les
  mots des consignes recopiés du banc tels quels. Ainsi écrite, la version (a) n'est pas un écart à R1.

### CR-09 — mineure — précision 30 : « n_cal / 2 » gardé à la lettre en sachant qu'il est faux
- **Lieu** : section 8, précision 30 ; Plan, section 2.
- **Constat** : l'intention du facteur est le nombre de contenus des huit tâches. Garder « n_cal / 2 » quand les huit
  tâches n'en portent pas la moitié biaise la demi-largeur prévue, donc le choix de n.
- **Correction demandée** : écrire le facteur comme le nombre de contenus des huit tâches d'évaluation. C'est une
  correction de calcul, sans effet sur un signe.

### CR-10 — mineure — D-9, version (b) : la vérification de C-P3c
- **Lieu** : bloc de la stabilité de rang, version (b).
- **Constat** : sous (b), C-P3c garde son verdict « à deux lectures, sous la clause de repli ». Or la clause exige
  une vérification ; sans rapport de grille, il faut dire laquelle tient lieu.
- **Correction demandée** : écrire que la vérification courte U1 de la session 16 (deux lectures, C-P3c au plus 0,047
  joint, seuil 0,0597 à 2 000 essais ; rapport `45a0d875…`) tient lieu de vérification pour C-P3c sous (b).

## 3. Points demandés par la session

- **Les 36 précisions (38 points ouverts)** : je les ai relues une à une. Les précisions 1 à 8, 10 à 13, 15, 16, 19 à
  29, 31 à 33, 35 et 36 lèvent l'ambiguïté visée sans en créer d'autre, et ne favorisent aucun signe. Plusieurs
  durcissent la confirmation (13, 14, 16, 17) ou comptent les tirages non finis contre la conclusion testée, dans les
  deux sens (5) : symétriques, je les accepte comme précisions. Pour le module, elles s'écartent de la lecture codée
  (5, 14, 18) : le module doit être mis à jour (verrou 3). Restent : 9 (CR-03), 18 (CR-02), 30 (CR-09), 34 (CR-04), et
  la clause d'introduction (CR-01).
- **Partage « avant le scellement » et « avant l'étape 2 ou le pilote »** :
  - Rien de ce qui est repoussé ne porte une règle d'analyse, à deux conditions : la règle de D-19 (a) est rendue
    mécanique (CR-08), et l'adaptateur reste sans règle de décision, ce que la précision 36 et l'épreuve sur le modèle
    jouet doivent assurer.
  - Verrous 12 et 13 : ce sont des entrées lues dans des pièces à venir ; les règles qui les emploient sont au texte.
    Le report est acceptable.
  - Verrou 11 : avant le scellement, c'est juste.
- **Décisions neuves** :
  - D-18 (accord de type « calcul ») : nœud justement classé (dépense). Les options sont honnêtes et complètes ;
    les deux exigent une ligne « calcul » inscrite par Lazar, ce que la liste dit. Recommandation (b) défendable.
  - D-19 : nœud justement classé (lecture de N-053, événement à venir). Options complètes. Recommandation (a)
    acceptable si elle est rendue mécanique (CR-08).
  - D-20 : la proposition à défaut convient. Ce n'est pas un écart à R1 : du code sans règle d'analyse, scellé et
    contre-lu avant toute donnée, pilote compris. L'inconvénient d'alignement est dit honnêtement. Corriger les
    dépendances (CR-07).
  - Garde 1 : pas de nœud (CR-06).
- **Revendications, chiffres, énoncés** : entre c2 et r2, hors des cases du directeur, aucun énoncé, aucune prédiction
  ni aucune marge ne change, aucune revendication n'est ajoutée, aucun chiffre de l'état de l'art n'est ajouté. Une
  seule réserve : la précision 18 change une règle de réfutation (CR-02). Les seuls chiffres neufs sont des choix de
  conception déclarés et l'empreinte de la mesure v2 (vérifiée).
- **Validateur r2** : trois sections à remplir (D-19, D-18, « Contre-lecture ») et treize marqueurs, dont le neuf
  `<<LIGNES_DEPENDANCES_PAPIER_C>>`.

## 4. Avis d'ensemble

Aucune remarque bloquante. **Scellable après correction** de CR-01 à CR-03 (majeures) et des mineures, ou leur refus
écrit. Il faut aussi le mot du directeur sur D-18 et D-19 (D-20 prend son défaut) et sur CR-02 s'il n'est pas corrigé,
et la levée des verrous nommés avant le scellement : 3, 4, 9, 10 et 11. Les verrous 12 et 13 portent sur l'étape 2.
