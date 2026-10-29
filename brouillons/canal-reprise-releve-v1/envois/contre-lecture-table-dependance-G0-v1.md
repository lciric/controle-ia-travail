# Contre-lecture (R2) de la table de dépendance « critères de G0 → travaux », v1

**Déclaration.** Je n'ai écrit aucun des fichiers relus. Modèle : Sonnet (sous-agent neuf). Heure lue par `date -u` : 2026-10-29 10:20:23 UTC.
Interdits respectés : rien lu sous `donnees/`, `prereg/P3-consignes-v1.md`, `diag/*/traces` ; aucune commande git ; aucune dépense ; aucun fichier existant modifié.

**Empreintes des fichiers demandés** (`sha256sum`, la compagne `.sha256` de la table vérifiée : OK) :
- table `e2480618816d6bcbea77654fe805b82a8e1333cddc428ea1ce6c03e75e6fe4f5`
- avis sur le repli `62cc6fbf4793d477cd9ca22a168febe3abc5ee3887fcd78db4d31b891dc50aab` (compagne OK)
- grille (copie de travail) `320af9b0b367c08ddcb08d39979ca9c014157d14701b107369b760be48a76a34`
- brief v2 `9261932a11f29e8643175bc6e150d5455067f58a3cb1e57dca99e02cb17aa3b2` (lignes 100 à 249 lues)
- `registres/decisions.md` `b303e3ad…` (fichier vivant ; ligne 462 = N-027, empreinte de la ligne `7c7d82c9…`) ; `CLAUDE.md` `a2aabda8…`

**Fichiers lus en plus, pour lever les définitions que la table déclare introuvables** (empreintes tronquées à 16 caractères) :
note du moissonneur `87d36ce3336d63b3`, note du tour (c) `ad33007204aa0ecc`, programme de conception de l'organisme v2 `353515fffa33bb93`,
paramètres de la garde δ pour G1 `db6037507f23d1ee`, décision pilote couche 2 v5 `255a364e710cd713`, brouillon 4 de T0.7 `a292088ca6e7f593`,
passation du 28 octobre `b010b548340d2f9e` (tous sous `brouillons/` ou `registres/`, chemins dans le dépôt).

## Verdict d'ensemble
La règle de lecture (§4) est mécanique et sa table inverse est exacte (vérifiée ligne à ligne : 1 → W8-W13 + W18 ; 2 → W11 ; 3 → W13 ; 5 → W14, W15, W19 ; 7 → W18 ; 8 → W19, W20).
Le défaut est dans le **contenu des lignes**, pas dans la règle : plusieurs colonnes « dépend » et « sert » sont contraires au brief et à l'annexe B, et deux définitions que la table dit
introuvables existent dans le dépôt et la contredisent.

## Constats

**CT-01 — Cellules non tranchées scellées (W5, W21, C3, C4). Gravité : bloquant.**
Lignes 35 (« continue, à confirmer »), 51 (« non établi », « fermé par défaut »), 88-89. Les classes « à confirmer » et « non établi » n'existent pas au §2 ; la règle ne dit pas ce qu'elles font : le lecteur du repli devrait trancher.
Les définitions existent : moissonneur = pièce 5 de la conception v7 de la course d'idéation (note du moissonneur) ; tour (c) = variante « outils clôturés » de cette même course (note du tour (c)).
Correction : reclasser W5 et W21 avant scellement, sans cellule provisoire ; supprimer C3, C4 ou les réduire à une justification.

**CT-02 — W16 et C1 confondent « organisme » (pôle scientifique automatique) et organismes de T0.6 ; « sert 2 » et « sert 8 » inventés. Gravité : bloquant.**
Lignes 35 (W5), 46 (W16), 86 (C1). Le programme de conception v2 (l. 1) définit « l'organisme » comme le pôle scientifique automatique ; ce n'est pas la famille (i) ou (ii) du critère 2. L'argument « son entraînement éventuel appartient à E1.1 » n'a aucune source.
Le moissonneur est un outil des proposeurs d'idéation, ses résumés sont `non_opposable` (note du moissonneur § 3) : il ne sert pas le critère 8 ; sa première moisson réelle exige un GO et coûte des jetons (≈ 0,4 dollar par course, § 6), donc « sans dépense » (l. 35, 88) est faux.
Aucun fichier du pôle lu ne relie la course d'idéation à un critère de G0. Sous la règle 3, une ligne qui ne sert aucun critère de N ne dépense pas : la mention « sert 2 » ou « sert 8 » est ce qui lui donnerait le droit de dépenser.
Correction : « sert — » pour W5, W16 et W21 (sauf source écrite contraire), avec la conséquence dite à Lazar : sous le repli, la course ne dépense pas. Retirer l'argument de C1 « évite de perdre un mois » (raison d'utilité, non de dépendance).

**CT-03 — W10, W12 déclarées dépendre du critère 1 seul ; W11 traitée autrement. Gravité : bloquant.**
Lignes 40-42, 90 (C5). Le critère 3 se lit « sur (i) et (ii) » (brief l. 173, 194) ; le brouillon 4 de T0.7 lit T7-P1 à T7-P4, T7-P9 et T7-P10 sur (i-a) et (ii) (l. 73-74, 94). Or W10 (T7-P9, T7-P10) est « dépend 1 » tandis que W11, qui lit les mêmes activations de T0.6 (T7-P6 à P8), est « dépend 1, 2 » : même nature, classes opposées.
Annexe B de la grille : « 2 avant 3 ; 2 et 3 avant 4 ». W12 « run sur épisodes de T0.6 » sans dépendance à T0.6 contredit l'énoncé de N-029 que C5 invoque.
Preuve par l'absurde : la table inverse (l. 71-79) dit que, si le critère 2 est dans N (organismes absents), seule W11 se ferme ; W10 et W12, qui lisent ces organismes, continueraient et pourraient dépenser.
Correction : scinder W10 en W10a (entraînement sur données génériques, témoin lexical ; dépend 1) et W10b (lecture sur les épisodes de T0.6 ; dépend 1 et le produit de T0.6) ; faire dépendre W12 du même produit ; voir CT-04 pour la forme de cette dépendance.

**CT-04 — N figé au verdict : les chaînes 2 → 3 → 4 se bloquent pendant le report. Gravité : bloquant.**
§4 (l. 60) : « soit N l'ensemble des critères que le verdict ne déclare pas tenus ». Une fois CT-03 corrigé, W10b et W12 sont fermées tant que 2 est dans N, et 2 reste dans N toute la durée du report : les critères 3 et 4 ne peuvent plus progresser, la clause de report ne sert à rien. C'est sans doute la raison implicite de la classe actuelle de W10 et W12 ; il faut l'écrire, pas la cacher.
Correction à décider par Lazar (nœud : elle change la mécanique de la clause) : exprimer les dépendances comme des **produits scellés** (« verdict scellé de T0.6 existant », test mécanique M-0.5) et dire si N est réévalué à chaque verdict de critère scellé pendant le report, ou seulement au second verdict.

**CT-05 — Complétude (question a) : lignes manquantes. Gravité : bloquant (P4-instrument, pilote couche 2, garde δ), à corriger (le reste).**
Présents : T0.1 à T0.9 (W1, W2, W6, W7, W8, W9, W10-W12, W17-W18), G1 (W14, W22), papiers A, B, C (W19, W20, W25, W17, W18, W24), course d'idéation (W16), état de l'art (W2), moissonneur (W5), veille, collisionneur.
Absents, donc fermés par W26 : (1) **P4-instrument**, contrôle positif exigé avant toute sonde sur T0.6 (grille, critère 3 ; R-262 le met en tête du plan) : travail du critère 3 fermé par défaut ; (2) **pilote de la couche 2** (seize tâches de réserve, dépense sur devis) et **simulations de la garde δ** (rapports v1 à v5) : ni synthétiques au sens de W15 pour le pilote, ni exécution de G1 au sens de W22 ; (3) autres éléments du pôle en cours : orchestrateur, corpus primaire, porte PACE, pari de signe ; (4) addendum 2 de P3 (N-025) ; (5) phases 2 et 3 (T2.0 à T3.4, G2, G3) non nommées, couvertes seulement par W25 ; (6) message FakeLab (T0.2) et rédaction/soumission (brief § 12), qui sont des nœuds.
Correction : dresser la liste à partir de `registres/etat.md` et du brief (références T0.x, TC.x, T2.x, T3.x, numéros R/N/GO), pas à partir des noms de la demande ; porter l'identifiant de registre sur chaque ligne pour que « appartient à la ligne » ne soit pas un jugement.

**CT-06 — W15 et W22 : « couche 2 » mal définie ; dépendances sans source. Gravité : à corriger.**
Lignes 45, 52, 87 (C2). Dans le programme de conception v2 (§ 5), la couche 2 est une « banque avec sabotage : organismes T0.6, sondes T0.7, bases T0.8 », avec sa propre porte de sortie ; ce n'est pas « Couche 2 / G1 ». « Dépend 5 » et « sert 6 » (W15) n'ont aucune source ; la garde δ est écrite « pour le brouillon du préenregistrement de G1 » (paramètres de la garde δ), et plusieurs valeurs viennent « du fichier réel du pilote, remplies avant scellement » : le scellement de G1 dépend donc d'un produit du pilote, ce que W14 ignore (voir CT-07).
Correction : redéfinir W15 et W22 sur la définition du pôle ; ou les déclarer hors périmètre et les lister (CT-05).

**CT-07 — W14 (préenregistrement de G1) : dépend 5 seulement. Gravité : à corriger.**
Ligne 44 et C9 (l. 94). Annexe B : « 2 à 4 avant le scellement de 6 si G1 cite les instruments » ; le plan 2 × 2 de G1 (brief l. 214-217) est fait des sondes et des bases de T0.7 et T0.8, sur les mêmes épisodes. La table tranche à la place de Lazar un point que la grille laisse conditionnel. Conséquence : avec 2, 3, 4 dans N, W14 continue et peut sceller un préenregistrement de G1 qui cite des instruments non validés.
Correction : soit ajouter 2, 3, 4 à la colonne « dépend » de W14, soit porter le choix à Lazar comme décision écrite avant scellement de la table.

**CT-08 — Traitement inégal du critère 8 (W17, W19, W20, W2). Gravité : à corriger.**
C8 (l. 93) fait dépendre les papiers A et B du critère 8 au nom de R7 et de CLAUDE.md (aucun chiffre non vérifié dans un préenregistrement ou un papier), puis dit « le papier C est couvert par W17 » alors que W17 (préenregistrement du papier C) est « dépend — ». Même règle, deux traitements ; le brief fait de 2607.08066 la collision la plus sérieuse pour le papier C (T0.2, priorité 1).
Colonnes mortes : W19 et W20 « dépend 8, sert 8 » (si 8 est dans N, la ligne est fermée : « sert 8 » ne peut jamais jouer). W2 regroupe le contrôle de traçabilité, que l'annexe B place après les textes scellés des critères 6 et 7 : il ne peut pas être « dépend — ».
Correction : une règle unique pour la présence de chiffres dans un texte scellé, et W2 scindée (références ; traçabilité).

**CT-09 — Latitude laissée au lecteur du repli (question c). Gravité : à corriger.**
- l. 31 (W1) « sert : transversal » : valeur hors des critères numérotés ; la règle 3 ne dit pas si W1 dépense.
- l. 32 (W2) « reste de l'état de l'art » : défini par l'état, pas par la tâche.
- l. 36 (W6) « reprise éventuelle » : rejouer T0.3 après le verdict changerait la preuve du critère 5 (gel levé après le run, R-025).
- l. 39 (W9) « sert 2 (3, 4 : fournit leurs données) » : la parenthèse ne dit pas si 3 et 4 ouvrent un droit de dépenser.
- l. 21 « honnêtement » (définition de « dépend ») ; l. 25 « tant qu'il reste ouvert » ; §4 règle 3 vise les travaux « qui continuent » sans dire que les conditionnels ouverts qui servent N y sont inclus.
- l. 52-55 (W22 à W25) : « 1 à 6 », « 7 et suivants », « G1 » ne sont pas des critères de G0 (sans effet, ces lignes étant fermées, mais à nettoyer).
- « décisive » (clause) n'est défini nulle part ; voir CT-11.

**CT-10 — Taillage sur l'état (question d). Gravité : bloquant, porté par CT-02 et CT-03.**
La forme de la règle serait la même sans les travaux en cours. Les affectations de lignes ne le seraient pas : (i) toutes les pistes en cours ouvertes ont pour seule dépendance un critère déjà prouvé (1 pour W8-W10, W12 ; 5 pour W14, W15) alors que le brief, la grille et N-029 vont vers 2, 3, 4 ; (ii) les deux travaux en cours qui n'ont aucun lien écrit avec un critère reçoivent « sert 2 » et « sert 8 », donc un droit de dépenser ; (iii) les papiers A et B, hors du travail du jour, dépendent du critère 8, pas W17 ni W14 ; (iv) l'argument de C1 est une perte de temps, pas une dépendance ; (v) la réserve de la l. 101 constate elle-même que la table « laisse le travail courant presque intact ». Je ne prétends pas à l'intention ; l'effet est celui d'un taillage, ce qui déclenche l'audit de R4 : le corriger par CT-02, CT-03, CT-07.

**CT-11 — « Expérience décisive » (clause) et W18 / W13. Gravité : à corriger.**
La clause interdit toute expérience décisive de G1 et du papier C. W18 (pilote du papier C, ≈ 6 dollars) continue si 1 et 7 sont tenus ; la table ne dit pas s'il est « décisif ». W13 (P3, déjà jugé : verdict v2) dépend de 3 tout en étant une lecture de ce que le critère 3 demande (sondes au-dessus du plancher) : fermée précisément quand 3 est dans N, donc quand elle sert.
Correction : lister les travaux « décisifs » (W22 à W25, plus W18 si Lazar le veut) par numéro ; reclasser W13 (ou l'éclater en reprise de P3, addendum 2, P4-instrument).

**CT-12 — Application mécanique de la clause (question e) : ce qui manque. Gravité : à corriger (sauf CT-04).**
Avec les corrections ci-dessus, la clause (report unique au 31 janvier 2027, puis clôture, aucune expérience décisive) devient applicable. Il manque encore :
1. **Qui applique** la table et sous quelle forme (une feuille de repli scellée au jour du verdict : N, puis une ligne par travail : continue / fermé / dépense sur devis). La grille (Forme du verdict) fournit déjà la liste des états par critère, donc N est mécanique.
2. **Verdict interrompu** (liste d'arrêt de la grille : « un arrêt n'est pas une lecture ») : N n'existe pas ; la table et la clause se taisent.
3. **Clôture** au second verdict : quelles lignes cessent (toutes sauf W1, rapport de porte ?). La table n'a aucune règle de fin.
4. **Conflit clause / table** : la clause (2) dit « les travaux indépendants continuent » sans restriction de dépense ; la règle 3 de la table en ajoute une (l. 100 : « la clause prime »). Il faut en décider, pas en laisser le choix.
5. **Travaux nouveaux** entre le scellement et le verdict : W26 les ferme ; le pôle crée des versions chaque jour : prévoir la date limite d'une version 2 de la table.

**CT-13 — Remarques de forme. Gravité : remarque.**
- R-454 (`registres/decisions.md` l. 668) résume la table comme « 9 continuent (T0.1 à T0.5, …) » et « 22 travaux » ; la table classe T0.5 (W8) comme conditionnel, compte 25 travaux plus W26, et fait continuer collisionneur et moissonneur : corriger R-454 (nouvelle ligne, pas de réécriture).
- La phrase de provenance (« seule liste des travaux de la phase 0 ») est inexacte : W4, W5, W15, W16, W21 viennent de la demande ; C6 s'appuie sur le nul de P3.
- « Collisionneur » (W4) est défini par une hypothèse ; le registre le désigne comme « outil de Lazar, hors dépôt », employé sur des questions de décision, sous GO : « sert 8 » n'est pas établi.
- §4 dernier paragraphe : les droits de dépenser listés sont incomplets (4 donne aussi W8 ; 6 donne aussi W3) ; ajouter une seconde table inverse pour les droits de dépenser.

## Conclusion
**Non scellable.** Corrections exigées avant scellement : CT-01 (W5, W21 reclassées sans cellule provisoire), CT-02 (« sert » de W5, W16, W21 sur source écrite ou « — »), CT-03 (scinder W10, dépendances de W10b et W12 au produit de T0.6), CT-04 (décision de Lazar sur la forme des dépendances et la réévaluation de N pendant le report), CT-05 (lignes pour P4-instrument, pilote de la couche 2 et garde δ au minimum), puis audit R4 selon CT-10 ; CT-06 à CT-12 à traiter dans la même version v2, contre-lue à nouveau (R2).
