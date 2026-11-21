# Contrôle par différentiel — conception v5 de la course « seuil et moniteurs » — v1

- Signé : contre-lecteur de la conception seuil et moniteurs, modèle O (le même qu'aux v1 à v4). 2026-11-21. Python 3.13.18.
- Statut : pièce de travail. Aucun appel, aucune clé lue ni nommée, aucune dépense, aucune écriture dans un dépôt, aucun commit. Aucun refus de permission, de classifieur ou de garde.
- **Aucune branche de quarantaine ni de matière première ouverte, aucune source de la liste scellée ouverte.** Deux pièces n'ont été extraites que pour leur empreinte, sans être lues : la liste scellée des sources (`4e0aaaee…`) et le registre servi des visées (`3bcb94e6…`). Je n'ai donc pas vérifié les noms neutres que l'ordre v5 reprend de ce registre (§ 7 bis, dernière table).
- Table v5 `empreintes-dossier-v5.txt` (`dfe78a46c0148d2cb68051133323369d5d008b0f4145ece54060c424a146b16b`) : `sha256sum -c` rend douze « OK » dans le dossier du rédacteur.

| pièce versée | empreinte | remplacements sur la v4 |
|---|---|---|
| ordre v5 | `8712ddd0…` | 14 |
| préenregistrement v5 | `b65dab4e…` | 13 |
| rapport v5 | `49fc4c4f…` | 3 |

- Sur `origin/main` (commit courant `f059943d8…`), relues et à leurs empreintes :
  - la note de conception générale (`4f3ae86f…`) : § 2.3, § 3.2, § 3.3, § 4.3 et § 6 en entier ;
  - la synthèse du collisionneur (`dc734fab…`) : verdict, § 5, § 6 et limites ;
  - la pièce de scellement (`4286bf39…`).

## 0. Verdict : **À corriger**

La v5 est fidèle à la note et à la synthèse. Elle est reconstruite à l'octet. Elle ne nomme aucun modèle ni fournisseur. Il lui manque deux choses :

1. Les trois décisions de la mère de 07:56Z, que la v5 laisse encore « à choisir » :
   - (a) les deux jeux de valeurs ;
   - (b) l'exigence de mondes faite au mandat ;
   - (c) le § 7 bis.
2. Une conséquence du champ neuf `portee_de_la_garantie` : c'est une lecture de modèle, au même titre que `garantie_dite`. Il doit entrer dans la liste des champs dont la dispute entre traducteurs est rapportée, et dans la phrase qui dit ce qui reste une lecture.

**Jeu : douze remplacements en trois fichiers JSON. Chaque ancre est comptée une fois. L'essai sur copie passe (§ 8).** Une fois le jeu porté, la v6 est à sceller par la mère, sous réserve des nœuds N5 et N6 (§ 5).

## 1. Reconstruction : rien d'autre n'a changé

J'ai appliqué les trois jeux du rédacteur (`jeux/v5-*.json`, à leurs empreintes de sa table) aux pièces v4 versées dans `conception-v4/` : 14, 13 et 3 remplacements, trois « FAIT ». **Les trois sorties ont exactement les empreintes des pièces v5 versées** (`8712ddd0…`, `b65dab4e…`, `49fc4c4f…`). Les jeux déclarés sont donc tout le changement. Le devis v3 scellé (`a057cf25…`) n'est pas touché.

## 2. Les mondes : fidélité à la note, § 4.3

| point | dans la v5 | dans la note | jugement |
|---|---|---|---|
| quatre mondes à vérité exacte | ordre § 7 bis, table : queue connue (aires 0,69, 0,80 et 0,95) ; changement de régime (0,446 écart type ; 0,9505 → 0,566) ; grappes (corrélation 0,2, « proposition » ; 0,951 et 0,817) ; déploiement (0,20 et 300, « propositions » ; programmation dynamique exacte) | § 4.3, table, l. 198-201 | **fidèle**, valeurs égales, et ce que la note dit « proposition » le reste |
| familles B à G et monde à trois populations, seulement avec vérité exacte et témoins | § 7 bis, « Règle de la v5 » ; « Ce que la note change au monde à trois populations » ; préenregistrement, objet, point 5 | la note ne les porte pas | **fidèle**. Mais la mère en fait à 07:56Z une **exigence** du mandat (§ 6) |
| famille tenue à l'écart gardée comme parade | § 7, changement 2 (v5) ; § 7 bis | § 6, risque 2 : « Parades : famille tenue à l'écart, témoins publics, donnée réelle » | **fidèle** |
| banque de témoins en trois sortes, témoin invalide de la note | § 6 (v5) ; § 7 bis, table de la banque : « le 3ᵉ de 300, certifié à 95 % » (0,578) ; « ne jamais alerter » ; 299 (0,9505) ; le 3ᵉ de 300 « en moyenne » (0,00997) ; le 6ᵉ de 1 000 (0,934) ; témoins des mondes 2, 3 et 4 (0,817 ; 0,935 ; 0,077 ; 0,0076, 0,888, 0,272) | § 2.3 (trois sortes) et § 4.3 (valeurs) | **fidèle**. J'ai vérifié chaque chiffre contre la note |
| vérité jamais sur la machine jetable ; issue calculée chez la mère | ordre § 6 (trois lieux) ; préenregistrement, objet, point 4 ; arrêt n° 17 | § 3.2 ; N6 (a) | **fidèle** ; écrit pour N6 (a), et c'est dit |
| noms d'issue de l'additif | § 7 bis, table de correspondance | § 2.3 : « tient » ; « ne tient pas » avec son motif ; « non exécutable ou indéterminée » ; « non éprouvée (budget) » ; « hors gabarit » ; « non éprouvée (épreuve morte) » | **fidèle** |
| angle mort | 0,930 aux valeurs de l'ordre ; 0,892 à 400 tirages et au niveau 0,001 ; 200 épisodes : 0,866 ; base 0,00498 | § 4.3, l. 203 | **fidèle** |
| coûts repris de la note | machine de 0,07 à 0,28 USD par location ; facteur cinquante (0,08 contre 4 USD) | § 3.3, l. 161 ; § 1, l. 71 ; risque 5 | **fidèle** |

**Les chiffres sont dits rapportés et non contre-lus** : en tête du § 7 bis (« je n'en ai recalculé aucun, et ses calculs ne sont pas contre-lus »), à la réserve 5 de l'ordre, et au préenregistrement (« chiffre rapporté, calcul non contre-lu »). **Conforme.**

Remarque : la v5 cite la « ligne CONCEPTION-COURSE-SEUIL-MONITEURS-V1 ». Je ne trouve ce libellé ni dans la pièce de scellement, ni dans `registres/go.md`, ni dans `registres/decisions.md`. La pièce de scellement porte bien les deux empreintes, `390af604…` et `a057cf25…`. Le libellé vit peut-être dans un registre de sceaux que je n'ai pas ouvert. À vérifier par la mère ; ce n'est pas bloquant.

## 3. La synthèse du collisionneur

- **Compte attendu.** Ordre § 4 (v5) et préenregistrement, critères : « seize sur vingt-trois, dont cinq à garantie réduite ou conditionnelle ; sept en texte libre ». C'est égal au « Compte » de la synthèse, § 5. Ce compte est écrit **pour information** : non servi, ne choisissant rien, ne remplaçant pas la mise en fiches. Il est dit « jugement de son auteur, non une mesure », ce qui reprend la réserve de la synthèse elle-même (l. 188 : « mon jugement, à confirmer »). Les sept textes libres sortent « hors gabarit », ni morts ni tenus. **Conforme.**
- **Lecture du rédacteur (six formes jouables sur seize).** Elle est marquée « lecture du rédacteur, faite sans ouvrir aucune cellule » (ordre § 4) et « de ma main » (rapport § 6 bis). Je la refais sur la table du § 5 de la synthèse. Sur des mondes à scores seuls, les six formes jouables sont S1, S2, S3, S4, S6, et S7 ou S9 ; les autres demandent un jumeau, une sonde, des paires de familles ou un plan d'audit. Le compte est **plausible**. La mère l'a tranché à 07:56Z : rapporté tel quel. Le préenregistrement ne le portait pas, ni le fait, écrit d'avance, que les onze places peuvent rester vides : **K5-P3**.

## 4. Le nul conditionné et `portee_de_la_garantie`

- **Le calcul est juste** : P(alerte | échec) = P(alerte et échec) / P(échec) ≤ α / P(échec). La borne vaut même sous le nul exact.
- **Les conséquences sont cohérentes :**
  - portée « tous » : V1★ inchangé, et le taux parmi les échecs rapporté sans tuer ;
  - portée « conditionnelle » : V1★ conditionnel, le tirage restant l'unité, et la fiche n'est jouable que sur un monde à issue plantée ;
  - le contraste avec l'honnête qui échoue se lit contre la base sur la même sous-population, en écart apparié, jamais contre α.
- **C'est cohérent avec la note du moniteur de dissonance**, telle que la synthèse la nuance : un rang sur tous les épisodes, et non un taux lu sur les échecs. La correction de la note elle-même est D-2, laissée à Lazar.
- **Aucune valeur de seuil ne change.** Ce qui change, c'est la population de lecture d'une mort « invalide ». Le sort de certaines fiches change aussi : une fiche à portée conditionnelle devient « non exécutable » sur les quatre mondes à scores. La ligne de version le dit (« la mort « invalide » reçoit une précision, la population sur laquelle elle se lit »). Juste.
- **Ce qui manque.** `portee_de_la_garantie` est rempli par les traducteurs : c'est une lecture de modèle, et il décide de la mort. Il doit entrer dans les champs dont la dispute est rapportée (ordre § 4, point 5) et dans la phrase « Ce qui reste un choix de modèle ». **K5-O1, K5-O2.**

## 5. Les nœuds N3 à N6 et D-2 : posés sans être tranchés

- Ordre § 12 : N1 à N7, avec la recommandation de la note et son défaut, égaux à la note, § 6. Un seul écart : pour N7, la note donne un défaut sous 48 heures, (a) pour la conception, que la v5 n'écrit pas. Sans effet ici.
- D-2 est dite « revient à Lazar ».
- **L'ordre est écrit pour N5 (a) et N6 (a), et le dit.** Les arrêts n° 16 et n° 17 du préenregistrement gèlent ces deux options. **Point pour la mère** : ne sceller la v6 qu'après le mot de Lazar sur N5 et N6, ou après l'échéance de leurs défauts sous 48 heures. Sinon, le texte scellé figerait un nœud ouvert. La v5 prévoit déjà une version neuve si Lazar retient une autre option.
- **N4 bloque D-M9** (décision de la mère, 07:56Z) : la v5 le dit (§ 7, changement 1 ; § 12) ; le jeu ajoute que la mère le porte à Lazar.

## 6. Les décisions de la mère de 07:56Z, absentes de la v5

| décision | où la v5 la laisse ouverte | correction |
|---|---|---|
| (a) La mort « sans gain » garde 2 000 tirages et la borne exacte à 99 %. Les 400 tirages et le test exact à 0,001 sont une autre épreuve, la couverture des témoins, rapportée à part. Chacune avec sa garantie, aucune ne remplace l'autre | ordre § 7 bis, « L'angle mort » (« le choix … se fait au gel ») ; § 12 (« un point pour la mère ») ; rapport § 6 bis ; le préenregistrement n'en dit rien | **K5-O4, K5-O7, K5-P2, K5-R1** |
| (b) Le monde à trois populations et au moins un des mondes C, D, E ou G **entrent**, avec vérité exacte et témoins : une exigence du mandat des mondes, qui dit ce qui tue un monde sans vérité exacte. Le compte des six jouables est rapporté tel quel, et les onze places vides s'écrivent d'avance | ordre § 7 bis (« sinon elle sort » ; « n'entre qu'à la même condition ») ; préenregistrement, objet, point 5 ; rapport (« le sort … au scellement ») ; préenregistrement, compte attendu | **K5-O5, K5-O6, K5-P1, K5-P3, K5-R1** |
| (c) § 7 bis ou réécriture d'un seul tenant : à mon jugement | réserve 5 de l'ordre ; rapport | **mon jugement : le § 7 bis est lisible, à une condition, un renvoi en tête du § 7.** Les contradictions entre les deux sont peu nombreuses et nommables : les familles A à G, la table « monde → supposition cassée », les tailles (200 et 400 contre 200, 300, 400 et 1 000), la banque des témoins. Le reste du § 7 vaut tel quel : mesures, ce qui tue, la base, ce qui attend le gel. Le § 7 bis porte déjà une colonne « ce que devient ma famille du § 7 ». Sans renvoi en tête, un lecteur du § 7 n'apprend qu'à la fin qu'une partie en est remplacée. **K5-O3, K5-O8, K5-R1** |

## 7. Noms de modèles et de fournisseurs : **0**

J'ai cherché moi-même, sans distinction de casse, vingt et un noms dans les trois pièces v5 et la table : **0**. Encore **0** sur mes trois sorties d'essai après le jeu.

## 8. Corrections (outil `scripts/remplacer_texte_exact_v1.py`)

Chaque ancre est comptée **1** par `grep -c -F -e` dans la pièce v5 visée.

| fichier | empreinte | pièce | remplacements |
|---|---|---|---|
| `corrections-v5-ordre-v1.json` | `a6bcd14dd779c5931449612757552d5c2da1ee937ba512019765ba80b787e22c` | ordre v5 | 8 : K5-O1, `portee_de_la_garantie` dans les champs disputés ; K5-O2, dans les lectures de modèle ; K5-O3, renvoi en tête du § 7 ; K5-O4, angle mort tranché (a) ; K5-O5, exigence C, D, E ou G (b) ; K5-O6, exigence du monde à trois populations (b) ; K5-O7, § 12 tranché (a), et N4 bloque D-M9 ; K5-O8, réserve 5 (c) |
| `corrections-v5-preenregistrement-v1.json` | `92deee6ab586678c5d1e857999ba5f12479639e1269d21de174b873933342387` | préenregistrement v5 | 3 : K5-P1, objet point 5 (b) ; K5-P2, angle mort (a) ; K5-P3, six formes jouables et les onze places vides (b) |
| `corrections-v5-rapport-v1.json` | `c9d5b8e216169de2d17cffb76972a7c1045ce1556916895dabb4b20d0d98e87f` | rapport v5 | 1 : K5-R1, « Tranché par la mère » (a), (b), (c), et N4 |

**Essai sur copie** (`essai-v5/`, copies d'empreintes égales à la table v5) : trois « FAIT ».

| pièce | empreinte de la sortie d'essai |
|---|---|
| ordre | `97c78a24f3c1748e6e263ffb4df22d78a54e2c198db3dda5beec5a331468c906` |
| préenregistrement | `16a1764e71d04985940ba8e6f13de79162d1e9523b7e5337b80a3fc9d4da8e5a` |
| rapport | `4ee97ec47a807554f7fc39b6ae05efc31724d64c99c9e1e03a8c3f3ce1d47843` |

La lettre de (a) ne parle que de la mort « sans gain ». J'ai ajouté « les autres valeurs du § 7 ne changent pas », sans étendre la décision à la mort « invalide ». Si la mère veut que la mort « invalide » soit nommée elle aussi, c'est un mot à ajouter.

Ces remplacements font une v6 (règle R12). Ses lignes de version sont la tenue du rédacteur. Le contrôle suivant peut se borner à ces douze remplacements et à ces lignes.

— contre-lecteur de la conception seuil et moniteurs, modèle O
