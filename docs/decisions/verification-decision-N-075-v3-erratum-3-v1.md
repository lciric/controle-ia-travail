# Vérification courte — erratum 3 de la décision N-075 v3, et ligne pour `CLAUDE.md` (v1)

- **Vérificateur.** Claude Opus 5.5 (`claude-opus-5-5`), agent neuf : je n'ai écrit ni la décision, ni ses errata, ni la ligne. Classe A, une passe courte. 21 novembre 2026, vers 16:15 UTC (`date -u`).
- **Pièces vérifiées** (empreintes recalculées, égales à celles du mandat) : `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v3-erratum-3.md` (`d51863d24a3798641ce6fd7665ff8db89bd6089f52d643e4a5bccb42a2aef3fd`), lu en entier ; `docs/decisions/ligne-claude-md-N-075-v1.md` (`d59158e40cd4285ab8ee62ebff616e4f25d8cc7901a09c4474cee7384b3f173f`), lu en entier.
- **Références lues.** `registres/go.md`, ligne `GO-2026-11-21-61` en entier ; la v3 (`5aed4bab…`, égale à son compagnon) aux lignes citées par l'erratum 3 et en sections 1, 4 et 11 ; ses errata 1 et 2 en entier ; `docs/decisions/verification-decision-N-075-v3-v1.md` ; la ligne N-075 actuelle de `CLAUDE.md` ; la lecture des voisins (`973bd0dd…`), revendication 5 (l. 176-181) ; la note sur la couverture de l'oracle (`659f4593…`), l. 34, 36, 85, 90, 129, 143, 160, 189 ; le programme, l. 50-58 ; N-076, § 6.2 et section 13.
- **Non ouverts** : aucun PDF, préenregistrement ni résultat ; rien des dossiers et fichiers interdits par le mandat. Aucun fichier existant modifié ; ni commit ni poussée.

## Verdict

**À corriger : cinq corrections, petites, de lettre.** Les cinq choix de Lazar sont portés exactement ; l'erratum 3 et l'erratum 2 ne se contredisent que là où l'erratum 3 corrige l'erratum 2, et la primauté est dite ; l'énoncé du plancher porte « strate non mesurée = zéro » et « aucune borne chiffrée tant que rien n'est planté » ; la ligne pour `CLAUDE.md` est juste et ne lit pas « permis » ce qui est ouvert. Restent : l'« Énoncé retenu » de la v3 (l. 45) qui garde une borne « pour toute politique dont l'oracle voit le dommage » (C-1) ; deux phrases sur ce qui sort de la revendication du lemme qui en disent un peu plus que le choix (C-2, C-3) ; une phrase sur la recapture qui resserre un point que l'erratum dit laisser tel quel (C-4) ; un compte de signes (C-5). Après ces remplacements, les deux pièces sont prêtes sans nouvelle vérification.

## 1. Les choix de Lazar

| point | ligne du GO | erratum 3 | état |
|---|---|---|---|
| 7 | (a) | veille à côté des trois chantiers, au service d'abord des lectures d'antériorité (§ 1 ; R-1 à R-3) | **exact** ; reprend l'option (a) de la v3 (l. 254) |
| 8 | (a) | forme réécrite retenue (§ 1 ; R-4 à R-10) | **exact** ; énoncé recopié de la v3, l. 112 |
| 9 | penche pour (b), collisionneur et organisme, question fusionnée | non tranché, penchant (b), N-060 v3 point 4 en vigueur (§ 2, § 3 ; R-18, R-19, A-3) | **exact** ; nulle part lu comme permis |
| 10 | (a) | revendication resserrée au seul reste (§ 1, § 4.2 ; R-11 à R-13) | **exact** ; libellé égal à la revendication 5 de la lecture des voisins (l. 180), mot pour mot, « avec le coût du report » compris |
| 11 | (a), q par dommages plantés, strate non mesurée à zéro | § 1, § 4.1 ; R-14 à R-17, A-1 à A-3 | **exact** ; énoncé recopié de l'option (a) de la v3 (l. 258) ; la campagne reste à part |

Textes anciens de R-1 à R-19 recomptés par programme : chacun une fois dans la v3 (R-7 par ses deux bornes), R-11 une fois dans l'erratum 1 et zéro dans la v3. Rien de plus que les choix, à une exception près (C-4) ; rien de moins.

## 2. Erratum 3 contre erratum 2

Aucune contradiction sur les cinq choix. Les trois différences sont des corrections que l'erratum 3 nomme (§ 6) et justes à la source : « avec le coût du report » est dans le reste (lecture des voisins, l. 180) ; « (genre et dose) », « par une borne exacte » et « aucune borne n'y est écrite » sont dans l'option (a) de la v3 (l. 258) ; la ligne du commit `466e3c815` disait « signal » et « réentraînement en service ouvert ». La primauté est dite deux fois : en tête (« Là où ils diffèrent, cet erratum prime ») et dans la ligne pour `CLAUDE.md` (« le 3 prime »).

## 3. Les trois phrases signalées

- **Ce qui sort de la revendication du lemme** (R-11, § 4.2). Sortir « le prix de la garantie » et « la détection avant le dommage » est fidèle à « au seul reste » : le libellé ne les nomme pas. Mais « se cite » leur prête une source publiée : la v3 en donne une pour la détection avant le dommage, sous sa forme classique (rapport KfK 3935, l. 191), aucune pour le prix de la garantie. Ils sortent parce que le reste ne les nomme pas, non parce qu'ils seraient occupés (R8). D'où C-2. L'invariance entre agents gardée « comme partie du reste » est une lecture du concepteur, non nommée par le libellé ni par le mot de Lazar ; elle doit se dire telle. D'où C-3. La lecture de « dommage total » comme budget des déplacements du score est juste à la source (programme, l. 55) et déjà marquée « ma lecture ».
- **Ce qui déclenche la mise à jour des témoins** (R-7, § 1, point 8, suite 3). **Conforme.** L'option (a) énumère les issues : motif et dommage, alerte ; motif seul, audit prioritaire ; dommage seul, plancher. Un motif seul n'a donc pas d'autre suite, et l'option (c), qui gardait la nouveauté comme déclencheur, n'est pas retenue. « Refaire les témoins sur des honnêtes exogènes » est bien dans la liste « Corriger » de la section 1 de la v3 (l. 36), sans déclencheur fixé.
- **« Par une borne exacte »** (§ 4.1). **Conforme** à la source : « borne exacte par strate, puis minimum sur les strates » (note sur la couverture de l'oracle, l. 36 ; l. 129). Chiffre rejoué : `0.95**59` = 0,0485 et `0.95**58` = 0,0510 ; la phrase « 0,05 au plus, à 95 % » est juste. Remarque sans correction : le minimum des bornes inférieures par strate est une borne inférieure valide du minimum de q au niveau de chaque strate, sans partage du niveau (seule la strate du vrai minimum doit tenir) ; « sa répartition entre les strates » n'est donc nécessaire que pour des bornes simultanées par strate.

## 4. L'énoncé du plancher

§ 4.1, A-1, A-2, A-3, R-16 et R-17 portent : q mesuré, jamais supposé ; minimum sur les strates mesurées, nommées ; strate non mesurée = zéro, aucune borne écrite ; aucune borne chiffrée tant que rien n'est planté, au banc comme en service ; 299 et 1 497 en illustrations sous supposition ; plancher affirmé, jamais revendiqué. **Un défaut** : l'« Énoncé retenu » de la section 2 de la v3 (l. 45), que R-15 complète sans le restreindre, dit encore que le plancher borne le dommage « pour toute politique d'attaque dont l'oracle voit le dommage » : une strate que l'oracle voit sans y être mesuré y reste couverte, contre le § 4.1 et le point 11 (a). La limite de R-16 (l. 59) le rattrape, mais deux énoncés retenus diffèrent. D'où C-1 (texte ancien compté une fois dans la v3).

## 5. La ligne pour `CLAUDE.md`

598 signes mesurés par programme (sans le chevron) : sous 600. Chaque segment se retrouve dans la v3 et l'erratum 3, et les GO cités sont les bons. Le point 9 est écrit « non tranché, N-060 v3 tient » : rien n'y est lu « permis ». Style conforme aux autres lignes (sujet, GO, énoncés en raccourci, chemin, primauté de l'erratum). Ce qu'elle perd (« oracle exogène », « hors porte », les trois noms cités, « 1981 cité », « prioritaire ») est dit dans la pièce et reste dans la décision. **Un défaut de lettre** : la ligne actuelle de `CLAUDE.md` mesure 549 signes, non 548 (programme ; égale à celle de l'erratum 2). D'où C-5.

## 6. Corrections exactes

Chaque texte ancien est compté une fois dans son fichier, par programme.

**C-1 — erratum 3, § 5 : un remplacement de plus, et le compte de tête.**
- Insérer, juste avant « **R-16 (l. 59).** », l'alinéa : « **R-15 bis (l. 45).** Ancien : « pour toute politique d'attaque dont l'oracle voit le dommage » Nouveau : « pour toute politique d'attaque dont le dommage tombe dans une strate où la reconnaissance de l'oracle est mesurée (une strate non mesurée compte pour zéro) » »
- Ancien (en-tête) : « ils changent le statut de vingt passages » Nouveau : « ils changent le statut de vingt et un passages »

**C-2 — erratum 3, « se cite » sans source.**
- Ancien (R-11, nouveau texte) : « ne se revendique plus : il se mesure, se rapporte et se cite. » Nouveau : « ne se revendique plus : il se mesure et se rapporte, et se cite là où une source le porte (pour la détection avant le dommage, sous sa forme classique, le rapport KfK 3935) ; il sort parce que le reste ne le nomme pas, non parce qu'il serait occupé. »
- Ancien (§ 4.2) : « le prix de la garantie et la détection avant le dommage, qui se mesurent, se rapportent et se citent. » Nouveau : « le prix de la garantie et la détection avant le dommage, qui se mesurent et se rapportent, et se citent là où une source les porte (la détection avant le dommage, sous sa forme classique : rapport KfK 3935) ; ils sortent parce que le reste ne les nomme pas, non parce qu'ils seraient occupés. »

**C-3 — erratum 3, § 4.2, invariance entre agents.**
- Ancien : « sous les conditions que la note mathématique lui met. » Nouveau : « sous les conditions que la note mathématique lui met. C'est ma lecture du reste, non un mot de Lazar : si la note mathématique ne l'établit pas, l'invariance entre agents sort de la revendication. »

**C-4 — erratum 3, § 2, recapture.**
- Ancien : « Le texte à part qui écrit la recapture l'écrit comme une quantité rapportée. » Nouveau : « Le texte à part qui écrit la recapture l'écrit comme une quantité rapportée ; la suite d'une annonce relève du point 2 de la section 11 de la v3, que cet erratum laisse tel quel (à confirmer). »

**C-5 — ligne pour `CLAUDE.md`, compte de la ligne remplacée.**
- Ancien : « (548 signes) » Nouveau : « (549 signes) »

## Relevé de méthode

**Chaîne.** (1) Empreintes recalculées. (2) Ligne `GO-2026-11-21-61` lue en entier, confrontée au § 0 et au § 1. (3) Textes anciens de R-1 à R-19 recomptés par programme dans la v3 et l'erratum 1. (4) Reste du lemme confronté à la lecture des voisins, l. 180 : égal. (5) « Borne exacte » confrontée à la note sur l'oracle, l. 36 et 129 ; chiffre rejoué. (6) « Refaire les témoins » confronté à la section 1 de la v3, l. 36, et aux options (a) et (c), l. 255. (7) § 2 confronté à N-076, § 6.2 et section 13, point 3, et à la v3, section 11, point 2. (8) Ligne mesurée (598) ; ligne actuelle de `CLAUDE.md` mesurée (549), égale à celle de l'erratum 2.

**Objets de contrôle.** Compteur des ancres : chaque texte ancien de C-1 à C-5 rendu une fois ; objet faux, « vingt » dans l'erratum 3, rendu trois fois, donc non retenu seul comme ancre. Longueur : la ligne de l'erratum 2 et celle de `CLAUDE.md` rendues égales, 549.

**Premier pas non justifié.** Le reste du lemme et l'état « partiellement occupé » viennent d'une lecture des voisins non contre-lue ; je vérifie la fidélité à cette pièce, non sa justesse. Le rattachement des phrases de Lazar aux points vient de la mère ; je ne l'ai pas vérifié autrement que par la ligne du registre.

**Trouvaille de côté.** La v3 (l. 258) écrit 0,0511 pour `0.95**58`, qui vaut 0,05105 : 0,0510 à l'arrondi, comme l'écrivent la vérification de la v3 et l'erratum 3. Sans effet sur aucun énoncé ; à reprendre dans la v4.
