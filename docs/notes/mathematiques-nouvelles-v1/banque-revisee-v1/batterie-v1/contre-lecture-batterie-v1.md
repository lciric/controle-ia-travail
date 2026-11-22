# Contre-lecture de la batterie de fuite de la banque révisée (mathématiques nouvelles) — v1

- Contre-lecteur : Opus 5.5, session neuve, auteur d'aucune des pièces lues. Le 2026-11-22. Processeur seul, aucun appel de modèle, aucune dépense. Règles appliquées : R1, R2, R4, R5 (CLAUDE.md, « Règles gelées »), classe A de « Allègement ».
- Pièce contre-lue : **`batterie-fuite-banque-revisee-v2.md`** (`6b02a1c86d83355091bbfeb499fd1996fff99b96916f18752d2b8b3404568eee`, commit `617155c0`), qui remplace la v1 (`428ddb6c…`, commit `f70c8b05`). Lues aussi : `notes-a-la-mere-batterie-v1.md` (`c7bd64e4…`) et son erratum 1 (`3fc75dc8…`), les calculs d'appui du concepteur, le mandat (`575f8c29…`), le rapprochement (`bd5c2af3…`), les deux jugements (`b1380fe3…`, `f82e0c8f…`) et l'erratum 1 du jugement Fable, la note du diagnostic (`da4d80f4…`), les lignes GO-2026-11-22-109, -115 et -121 de `registres/go.md` (sur `origin/main`).
- Cloisonnement : seules les racines d'épreuve 1000 à 1119 ont servi, sur un banc que j'ai reconstruit sans importer ni le code du concepteur ni le paquet de la version 6. Aucun fichier de clé, aucune banque réelle, aucune racine du générateur.

## Verdict

**Gelable après corrections.** Une remarque bloquante, neuf à corriger, sept mineures.

- Le texte est conforme au mandat et aux mots de Lazar ; les sept écarts du concepteur sont justifiés ; j'ai refait par mon propre code les deux épreuves clés (écart 1 : 0,90 contre 0,00 ; écart 2 : le bloc entier rend −0,10 sur une fuite grossière que le prorata voit à 0,13), et le calcul 14,6 % / 5,0 %.
- **Bloquant** : la sonde des nombres, telle qu'écrite (Newton pur, 50 pas, sans garde de convergence), diverge en silence sur une fuite réelle. Sur mon artefact « relation entre littéraux », 125 des 480 apprentissages ne convergent pas, et l'excès mesuré tombe de 0,885 à 0,248 ; une fuite plus faible passerait. C'est un repli silencieux (règle R5).
- La v2 ne diffère de la v1 que par ce que le concepteur annonce (contrôle par `diff`, remarque 1). Elle ne porte pas encore les trois décisions de la mère ni l'écart des 120 racines en tête (remarques 3 à 5).

## Remarques

### 1. Différences entre v1 et v2 — conforme, sans suite

`diff` des deux fichiers : titre ; ligne d'état (lecture tranchée, GO-2026-11-22-121, « en attente du mot de Lazar » retiré) ; ligne « remplace la v1 » ; renvoi aux notes « lue avec son erratum 1 » ; mention de GO-121 au seuil de C3 ; ligne de variante du § 5 retirée ; une ligne d'empreinte pour la v1 et la précision des commits du registre. Rien d'autre. GO-2026-11-22-121 au registre dit bien : option (i), rappel d'au plus 0,20 à fausses alarmes d'au plus 0,10. La correction demandée (mention et variante supprimées) est faite.

### 2. Bloquante — la sonde des nombres peut diverger sans qu'on le voie (§ 2.2, « Modèle »)

- Constat. La lettre impose un Newton pur, partant de zéro, 50 pas au plus, sans contrôle du pas, et ne dit rien du cas où il ne converge pas. Sur un artefact où la vérité se lit dans la proximité de deux littéraux (R = C − d, d de 1 à 5, pour les vérités ; lois marginales de A, C, R inchangées), le modèle du squelette « R != mod(A * n + C, PM) » ne converge dans aucun des apprentissages (poids jusqu'à 2 500, scores jusqu'à 80 000). Les scores de ce squelette deviennent du bruit, et l'excès mis en commun tombe de 0,885 (Newton amorti) à 0,248 (Newton pur) ; par racine, il va de −0,09 à 0,90. Le prototype du concepteur emploie le même algorithme.
- Pourquoi bloquant : une banque qui fuit par une relation nette fait diverger la sonde précisément parce que la séparation est forte ; plus la fuite est franche, plus la sonde risque de la manquer. C'est une garde qui se tait (R5).
- Correction : (a) Newton amorti : le pas est divisé par deux tant que la perte pénalisée ne baisse pas d'au moins 10⁻⁴ fois la pente ; 200 pas au plus ; arrêt quand le plus grand pas effectif est sous 10⁻¹⁰ ; (b) garde : un apprentissage qui n'a pas convergé, ou un poids ou un score non fini, rend la sonde non calculable pour les racines concernées, donc C3 non tenue ; le compte des non-convergences est rapporté ; (c) l'épreuve du § 4 ajoute l'artefact « relation » (remarque 8). Avec (a), la banque saine et « grandeur » donnent les mêmes valeurs qu'avant à 10⁻⁴ près (0 non-convergence sur 480 apprentissages dans les deux cas). Pièces : `contre-lecture-calculs-v1/recalcul_newton_amorti_v1.py` et sa sortie.

### 3. À corriger — décision (1) de la mère : la règle de trois instances au hasard jointe à C4

- La v2 juge C4 sur la seule règle A ; la règle du hasard n'est qu'au § 7, en description. Il faut l'écrire dans C4, avec son propre j (11) et son seuil (borne haute ≤ 0,50).
- Cohérence à régler : la mère dit « tirées au hasard, graine SeedSequence consignée » ; le § 7 la définit par une probabilité exacte, 1 − C(M − m, 3)/C(M, 3), sans tirage. Je recommande la probabilité exacte comme grandeur de décision : elle ne dépend d'aucune graine, elle a moins de variance, et on ne peut pas la viser. Si la mère tient au tirage, écrire la graine à la lettre (par exemple `SeedSequence(20261122, spawn_key=(3000, racine_index, rang_du_faux))`), le tirage sans remise parmi les M instances, et la vérification exacte de la course.
- À définir dans les deux cas : M quand une variable bornée a un domaine qui dépend des variables précédentes (instances = suites admissibles du préfixe jusqu'à 3N, domaines vides exclus) ; le traitement d'un faux sans variable (M = 1, m = 1 : réfuté).
- À dire à la mère : la règle du hasard est exigeante pour les pièges, dont les contre-exemples forment une queue (30 % des instances en moyenne sur la version 6, soit environ 0,66 de réfutation par trois instances). Tenir C4 obligera la version 7 à des contre-exemples rares. C'est le but de la décision, mais cela réduit les chances de la branche « version 7 ».

### 4. À corriger — décisions (2) et (3) de la mère, et écart des 120 racines, à écrire en tête

- (2) Pas de plancher de portée : ajouter au § 5 une ligne « la portée (familles, squelettes, gabarits écartés) est dite en tête du rapport », marquée « en attente du mot de Lazar, défaut sous 48 heures : aucun plancher ».
- (3) Le § 2.3, point 12, dit déjà « une session neuve, ni le concepteur ni l'auteur de la sonde ». Écrire « un Opus 5.5 neuf », et ajouter qu'il ne transmet rien au concepteur avant le rapport de la mesure (même interdit que le point 9).
- 120 racines : la mère accepte ; l'écart au « au moins 40 » des juges et du mandat doit figurer en tête du texte, pas seulement dans les notes. Plus largement, la tête renvoie aux notes pour les sept écarts : une ligne qui les nomme dans le texte gelé lui-même le rend lisible seul.

### 5. À corriger — branches : version 8 et choix après coup (§ 3.6 et § 5)

- Le tableau du § 5 ne parle que de la version 7, alors que le § 3.6 permet une version 8. Écrire « la dernière version mesurée avant le 2026-12-04T23:59Z » à la place de « version 7 ».
- Fourche à fermer : une version 7 qui tient C1 et C4 mais pas C2 ou C3, puis une version 8 qui tient C2 et C3 mais pas C4. Sans règle, on choisirait après coup la version la plus favorable. Proposition : la décision de tenter une version 8 est écrite avant sa mesure ; dès qu'elle est mesurée, c'est elle qui fait foi, quel que soit son résultat ; on ne revient jamais à la version 7.

### 6. À corriger — C1, point 4 : « même loi » est affaibli sans être nommé

- Le rapprochement et les juges demandent des « littéraux tirés de la même loi » pour les vérités et les faux. Le point 4 demande une seule procédure de tirage qui ne connaît pas la strate, la strate étant constatée après. Sous cette procédure, la loi des nombres sachant la strate n'est pas la même dès que la vérité dépend de la grandeur (énoncés à seuil) : la loi conditionnelle diffère par nature. Le texte le sait (§ 8.5 ; notes, § G) et confie ce point à la sonde des nombres.
- Correction : nommer ce point comme huitième écart (« même loi » lu comme « même procédure, strate constatée après » ; l'égalité des lois par strate est mesurée par C3, pas garantie par C1) ; et préciser « la même loi » de la dernière phrase du point 4 (« construction différente admise si elle donne la même loi ») : même loi jointe des nombres d'une cellule, avant la constatation de la strate.

### 7. À corriger — épreuve R5 : chaque garde d'arrêt doit avoir son artefact (§ 4)

R5 veut chaque garde testée sur un cas sain et sur un artefact. Le banc n'exerce que l'assertion « énoncé sans paire » de C1 (par l'artefact « gabarit »). Ajouter, chacune devant arrêter la plantation et seulement elle :
- une paire à cheval sur deux mondes ; une paire de squelettes différents ; une paire de textes identiques ; un squelette à deux paires à faux tôt et zéro à piège dans un monde ; une sous-banque qui sert un seul membre d'une paire ;
- le contrôle de chaîne du § 0 : une sonde à qui l'on passe l'identifiant ou la strate doit être arrêtée ;
- l'audit « trop beau » : une sonde aux étiquettes inversées (excès vers −0,10) doit le déclencher ;
- le plancher de 40 racines plantées : 39 plantées doivent rendre « aucune condition ne tient » ;
- la garde de convergence de la remarque 2.
Dans le tableau, la colonne C4 de l'artefact « gabarit » dit « sans objet » : écrire « rapportée, non exigée ».

### 8. À corriger — ajouter l'artefact « relation entre littéraux » ; la longueur en jetons n'en demande pas

- La sonde des nombres a des traits de couple (rapport, égalité). Aucun artefact ne les éprouve : « grandeur » est vu par les traits d'un seul littéral. Artefact proposé : pour les vérités, avec la probabilité « dose », R = C − d (d de 1 à 5), A en est déduit, lois marginales inchangées. Mes résultats (120 racines d'épreuve, Newton amorti) : dose 1, excès 0,885, borne haute 0,888, tombe ; dose 0,5, 0,097, borne haute 0,107 à 0,111, tombe à peine. Attendu à geler : dose 1 tombe par la sonde des nombres ; 0,5 rapportée.
- Longueur en jetons (0,646 au diagnostic) : le texte la range dans C1 (deux membres d'une paire ont le même squelette, donc le même nombre de jetons). C'est juste : un artefact de longueur casse le squelette commun et tombe par C1, comme « gabarit ». La longueur en caractères ne dépend plus que des chiffres, qui sont un trait de la sonde des nombres. Aucun artefact de plus n'est nécessaire.

### 9. À corriger — une fuite « côté vrai » échappe au point de fonctionnement choisi

- C3 regarde le haut du classement (« le plus faux ») à 10 % de fausses alarmes. Une fuite qui permet de reconnaître à coup sûr une partie des vérités, sans rien dire des faux, y est presque invisible : si la moitié des vérités se reconnaît, le rappel vaut 0,20 et l'excès 0,10, au bord du seuil (c'est ce que montre l'artefact « relation » à demi-dose). Or la lecture en verdict compte aussi les vérités reconnues.
- Sous C1 la sonde de style est aveugle, et l'aire de C2, qui verrait cette fuite, ne la voit plus.
- Correction minimale : rapporter, pour chaque sonde, le point symétrique (rappel des vérités à 10 % de faux déclarés vrais), sans effet. En faire une condition change la lettre de GO-115 et GO-121 : nœud pour Lazar, recommandation « rapporter seulement », confiance 0,6.

### 10. À corriger — le seuil 0,10 laisse passer une fuite parfaite sur un quart des énoncés ; à écrire au § 8

Mon artefact « grandeur » à dose 0,25 (un quart des énoncés portent une fuite parfaite) donne 0,066, borne haute 0,077 : il tient (le concepteur trouve 0,086, borne haute ≤ 0,100, par une construction proche). Une fuite totale limitée à quelques squelettes est diluée de la même façon. C'est la conséquence voulue d'un excès toléré de 0,10, mais le § 8 ne le dit qu'en termes d'« excès vrai ». Ajouter : « une fuite parfaite sur un quart des énoncés, ou sur un squelette sur dix, peut tenir C3 ; les excès par squelette (§ 7) sont là pour la voir, sans effet sur la décision ».

### 11. Mineure — le point de fonctionnement n'est pas « un dixième exactement » quand les scores sont continus (§ 0)

Avec des scores tous distincts, la 8ᵉ vérité forme un bloc pris à moitié, mais tous les faux classés entre la 7ᵉ et la 8ᵉ vérité sont comptés en entier : le rappel est celui du seuil placé à la 8ᵉ vérité. Biais d'une sonde sans information : +0,0053 en théorie (8/76 − 0,10), +0,0048 mesuré. Il joue contre la banque (prudent). Écrire une phrase qui le dit.

### 12. Mineure — « l'ordonnée à l'origine est nulle » (§ 2.2, dernière ligne)

Sous C1, chaque squelette a autant de vérités que de faux à l'apprentissage, donc l'ordonnée est proche de zéro, mais elle ne l'est pas exactement : la pénalité et les autres poids la déplacent. Écrire « proche de zéro ».

### 13. Mineure — relecture de la banque réelle : la valeur de la règle aveugle n'est pas comparée à 0,50 (§ 5)

La plage du minimum au maximum sur 120 racines peut contenir des valeurs au-dessus de 0,50. Une banque réelle à 0,55, dans la plage, ne ferme rien. Ajouter : « si la part de la banque réelle dépasse 0,50 (règle A ou règle du hasard), la phrase “hors de portée” s'applique aussi ».

### 14. Mineure — 14,6 % et 5,0 % : exact, sous une hypothèse à écrire

Vérifié : 6/(R + 1) vaut 0,1463 à 40 racines et 0,0496 à 120 ; ma simulation de trois valeurs indépendantes donne 0,143 et 0,047. Hypothèse : la banque réelle est échangeable avec les racines neuves. Elle l'est presque : sa sonde des nombres apprend sur 120 viviers, celle d'une racine neuve sur 119. Les ex æquo (part de la règle aveugle en 75ᵉ) rendent la borne prudente. Une phrase au § 5.

### 15. Mineure — banque saine du banc : n₀ ≥ 2 pour les faux tôt est choisi en connaissant la règle A

Ce choix rend la règle A presque muette sur la banque saine (0,07). C'est légitime pour un banc, mais le dire, pour qu'on ne lise pas 0,07 comme une propriété d'une banque saine quelconque.

### 16. Mineure — indépendance des racines dans le rééchantillonnage (§ 8.9)

Je n'ai pas chiffré l'effet. Proposition à faire par le code de la batterie : comparer la borne haute de la sonde des nombres sur la banque saine du banc avec celle d'une variante apprise sur des racines d'apprentissage disjointes (deux moitiés). Rapporté, sans effet.

### 17. Mineure — sur les écarts 3 à 7 et les nombres

- Écart 3 (seuil réglé sur les vérités notées) : juste ; il ne lit aucun faux, et le diagnostic montre que le seuil transporté donne des fausses alarmes de 0,05 à 0,16.
- Écart 4 (apprendre sur le vivier, noter sur la sous-banque) : juste.
- Écart 5 (tirage après le scellement de la sonde tenue à l'écart) : nécessaire.
- Écart 6 (trois valeurs relues) : juste, calcul vérifié (remarque 14).
- Écart 7 (chacune des neuf bornes) : plus strict que « la plus grande » ; il compte neuf épreuves, ce qui joue contre la banque. Accepté.
- Plancher 40, « non calculable » si plus d'un énoncé sur dix est noté zéro faute d'apprentissage, audit « trop beau » sous −0,03 : justes. À 120 racines, −0,03 est à environ 6 écarts-types d'une sonde sans information à scores continus, à 9 pour une sonde à scores liés par paire (sorties du calcul 1, que je retrouve).

## Écarts 1 et 2 refaits par mon code

Banc reconstruit d'après le § 4 (12 mondes, N de 4, 10 et 15, PM premier de 211 à 1999, quatre écritures, strates contrôlées par force brute sur [0 .. 3N] pour chaque énoncé), 120 racines d'épreuve 1000 à 1119, graines distinctes de celles du concepteur.

| banque | sonde des nombres par squelette, autres racines (lettre du § 2.2) | sonde commune dans la racine, traits résumés (façon diagnostic) | sonde commune dans la racine, traits dans l'ordre d'écriture |
|---|---|---|---|
| saine | 0,001 (borne haute 0,008) | −0,003 (0,005) | −0,009 (−0,001) |
| grandeur, dose 1 | **0,900 (0,900)** | **−0,001 (0,007)** | 0,076 (0,089) |
| grandeur, dose 0,5 | 0,211 (0,229) | 0,006 (0,014) | 0,025 (0,035) |
| grandeur, dose 0,25 | 0,066 (0,076) | −0,006 (0,002) | 0,000 (0,009) |

Excès moyen sur tous les faux, borne haute entre parenthèses. L'écart 1 est confirmé : une sonde commune ne voit pas une fuite dont le sens change avec l'écriture, même quand on lui donne les traits dans l'ordre ; la sonde par squelette la voit entière.

| sonde « squelette seul » (part de faux du squelette dans les autres racines) | prorata | bloc entier |
|---|---|---|
| banque saine | 0,000 | −0,100 |
| gabarit partiel (une écriture porte une vérité pour trois faux, les autres une pour une) | **0,134 (borne haute 0,140), tombe** | **−0,097, tient** |
| cas d'école (9 vérités et 45 faux au même score haut) | 0,40 | −0,10 |

L'écart 2 est confirmé : au bloc entier, une sonde grossière ne voit jamais rien, et sur une banque saine elle rendrait −0,10 partout, ce qui déclencherait à tort l'audit « trop beau » sous −0,03. Le prorata est la bonne règle.

## Les trois nœuds du concepteur

1. **C4 à la lettre** : la mère a joint la règle du hasard. Cohérent ; à écrire dans C4 (remarque 3), de préférence par la probabilité exacte.
2. **Plancher de portée** : aucun, portée dite en tête, en attente du mot de Lazar. Cohérent ; une ligne à ajouter (remarque 4). Je suis d'accord : un plancher ferait échouer une version 7 sans fuite.
3. **Contrôle de la sonde tenue à l'écart** : un Opus neuf. Cohérent avec § 2.3, point 12 ; préciser le modèle et l'interdit de transmission (remarque 4).

## Échappatoires examinées

- Contre-exemples à 3N − 1 pour tenir C4 à la lettre : fermé par la décision (1), si la règle du hasard est écrite dans C4.
- Fuite par la définition du monde : fermée, les deux membres d'une paire partagent le monde (C1, point 1).
- Fuite par la longueur : fermée par le squelette commun et le trait « nombre de chiffres ».
- Fuite par une relation nette entre littéraux : vue par la sonde des nombres, **seulement après la correction de la remarque 2**.
- Fuite diluée (un quart des énoncés, ou quelques squelettes) : passe, par construction du seuil (remarque 10).
- Fuite qui reconnaît les vérités : passe au bord du seuil (remarque 9).
- Choix entre versions 7 et 8 après lecture : à fermer (remarque 5).
- Fuite que ni la sonde des nombres ni la sonde tenue à l'écart ne lit (parité, divisibilité, chiffres) : c'est le rôle de la troisième sonde ; si elle est retirée, C3 repose sur une seule sonde utile (§ 8.6, déjà dit).

## Pièces (SHA-256 aux compagnons)

| pièce | chemin |
|---|---|
| cette contre-lecture | `docs/notes/mathematiques-nouvelles-v1/banque-revisee-v1/batterie-v1/contre-lecture-batterie-v1.md` |
| recalcul des écarts 1 et 2, relecture par la plage, cas d'école | `…/batterie-v1/contre-lecture-calculs-v1/recalcul_ecarts_1_2_v1.py` |
| sa sortie | `…/contre-lecture-calculs-v1/sortie-recalcul-ecarts-1-2-v1.txt` et `.json` |
| Newton amorti et compte des non-convergences | `…/contre-lecture-calculs-v1/recalcul_newton_amorti_v1.py` |
| sa sortie | `…/contre-lecture-calculs-v1/sortie-recalcul-newton-amorti-v1.txt` et `.json` |

Durée des calculs : environ dix minutes de processeur. La sortie texte du premier script porte un avertissement de dépassement numérique : c'est la divergence de la remarque 2, gardée telle quelle.
