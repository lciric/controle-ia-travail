# Réponse à la contre-lecture de la batterie de fuite — mathématiques nouvelles — v1

- **Nature** : note de réponse (pièce de classe C). Auteur : le concepteur (mêmes mandat et compléments que le texte ; le modèle servi est relevé dans le message de remise à la mère, non ici). Le 2026-11-22. Processeur seul, aucun appel de modèle, aucune dépense.
- **Répond à** `contre-lecture-batterie-v1.md` (`9718ec04…`), qui a lu la v2 (`6b02a1c8…`). **Texte corrigé** : `batterie-fuite-banque-revisee-v3.md` (`78556fc5…`). La v2 n'est pas réécrite.
- **Bilan** : 17 remarques. 15 retenues, dont 4 avec une lettre différente de celle proposée (2, 5, 7, 10) ; 2 sans suite, parce que conformes (1 et 17). Aucune n'est écartée en entier ; ce qui est écarté dans une remarque retenue est dit à sa ligne, puis au § 2.
- Les trois décisions de la mère (R-5036, R-5038) et ses deux demandes de mesure sont portées : § 3 à § 5.

## 1. Remarque par remarque

| n° | objet | réponse | où, dans la v3 | raison, ou ce qui diffère |
|---|---|---|---|---|
| 1 | différences entre v1 et v2 | sans suite | — | conforme |
| 2 | **bloquante** : le Newton de la sonde des nombres peut diverger sans qu'on le voie | **retenue** ; critère d'arrêt différent | § 2.2 (calcul du minimum, garde, raison) ; § 1, C3 ; § 4 (artefact « relation », garde éprouvée) | Newton amorti, 200 tours, non-convergence = sonde non calculable = C3 non tenue, compte rapporté : comme proposé. L'arrêt se juge sur le décrément, non sur le pas effectif : § 2.1 ci-dessous |
| 3 | la règle de trois instances au hasard jointe à C4 | retenue | § 1, C4 ; § 6, faits 6 et 7 | deux règles, j = 10 et 11, chaque borne haute ≤ 0,50. Jugée par la probabilité exacte, comme recommandé ; tirage à graine consignée rapporté en contrôle. M et m définis pour les domaines dépendants ; faux sans variable : 1. Coût : § 4 ci-dessous |
| 4 | décisions (2) et (3) de la mère ; 120 racines et écarts en tête | retenue | tête ; § 2.3, point 12 ; § 5, « Portée » | le marqueur « en attente du mot de Lazar » est en tête et au § 5 ; les huit écarts et les 120 racines sont nommés en tête |
| 5 | branches : version 8, choix après coup | **retenue** ; règle différente | § 3, point 6 ; § 5 (tableau et « version qui fait foi ») | la fourche est fermée par une règle écrite d'avance, mais ce n'est pas « la version 8 fait foi quel que soit son résultat » : § 2.2 ci-dessous |
| 6 | C1, point 4 : « même loi » affaibli sans être nommé | retenue | tête (écart 8) ; § 1, C1, point 4 | « même loi jointe des nombres d'une cellule, strates comprises » ; l'égalité des lois par strate est mesurée par C3, non garantie par C1 |
| 7 | chaque garde d'arrêt doit avoir son artefact | **retenue**, sauf « et seulement elle » | § 4, « Gardes d'arrêt » ; tableau, ligne « gabarit » | les cinq violations de C1, le contrôle de chaîne, le « trop beau », les 39 racines, la convergence y sont ; « sans objet » devient « rapportée, non exigée ». Voir § 2.3 ci-dessous |
| 8 | artefact « relation entre littéraux » ; rien pour la longueur en jetons | retenue | § 4, tableau et ligne « rapportées » | dose 1 : tombe (0,883 ; le contre-lecteur trouve 0,885) ; dose 0,5 : rapportée (0,109, borne haute 0,12 à 0,13 ; il trouve 0,097, borne haute 0,107 à 0,111) |
| 9 | une fuite « côté vrai » échappe au point de fonctionnement | retenue, comme mesure rapportée | § 7 (définition) ; § 8, point 4 | non-condition : décision de la mère (R-5038). Chiffres au § 5 ci-dessous |
| 10 | le seuil 0,10 laisse passer une fuite parfaite sur un quart des énoncés | **retenue** ; phrase corrigée | § 8, point 5 ; § 7 (excès par squelette, défini) | une fuite parfaite cantonnée à un quart des énoncés tombe ; c'est la fuite diluée qui tient. Voir § 2.4 ci-dessous |
| 11 | le point de fonctionnement n'est pas « un dixième exactement » | retenue | § 0, « Point de fonctionnement » et « Ex æquo » | « exactement » retiré ; biais de +0,005 dit, et son sens (contre la banque). Mesuré : 0,0051, erreur type 0,0004 |
| 12 | « l'ordonnée à l'origine est nulle » | retenue | § 2.2, dernière ligne | « proche de zéro » |
| 13 | banque réelle : la part n'est pas comparée à 0,50 | retenue | § 5 | la phrase « hors de portée » s'applique si la part de l'une des deux règles dépasse 0,50 sur la banque réelle |
| 14 | 14,6 % et 5,0 % : hypothèse à écrire | retenue | § 5, relecture | échangeabilité dite, et son défaut (120 viviers contre 119) |
| 15 | n₀ ≥ 2 choisi en connaissant la règle A | retenue | § 4, sous le tableau | dit : 0,07 n'est pas une propriété d'une banque saine quelconque |
| 16 | indépendance des racines dans le rééchantillonnage | retenue | § 4 (« sont aussi éprouvés ») ; § 8, point 11 | fait par le prototype : bornes de même largeur. Chiffres ci-dessous |
| 17 | écarts 3 à 7 et nombres | sans suite | — | acceptés par le contre-lecteur |

Remarque 16, chiffres (`sortie-calcul-4-v2.txt`, partie D ; excès sur tous les faux, moyenne puis borne haute) :

| banque | apprise sur toutes les autres racines | apprise sur l'autre moitié |
|---|---|---|
| saine | −0,004 ; 0,004 | 0,000 ; 0,008 |
| « grandeur », dose 0,25 | 0,086 ; 0,097 | 0,078 ; 0,089 |
| « relation », dose 0,5 | 0,109 ; 0,121 | 0,116 ; 0,129 |

L'écart entre moyenne et borne haute est le même dans les deux colonnes, à 0,001 près. Le partage des modèles entre racines ne rétrécit donc pas l'intervalle de façon visible.

## 2. Où la v3 s'écarte de la lettre proposée

### 2.1 Remarque 2 — le critère d'arrêt

- **Proposé** : arrêt quand le plus grand pas effectif est sous 10⁻¹⁰. **Écrit** : arrêt quand le décrément de Newton est au plus 10⁻¹³ fois le nombre d'énoncés d'apprentissage ; le dernier pas est alors fait en entier.
- **Raison.** Le critère du pas effectif marche parce que la recherche du pas piétine près du minimum : le pas se réduit, et sa petitesse arrête le calcul. Il conclut donc à la convergence sur un piétinement, non sur une arrivée. Pour une garde dont le rôle est de dire « convergé » ou « non convergé », je préfère une mesure directe de l'écart au minimum.
- **Mon premier essai** jugeait l'arrêt sur le pas de Newton entier, avant réduction. Il déclarait « non convergés » des apprentissages arrivés au minimum, et aurait fermé C3 à tort.
- **Chiffres** (`sortie-calcul-6-v2.txt`, partie E : douze apprentissages par banque, cinq banques du banc) :

| critère | déclarés non convergés, sur 60 | tours au plus | écart des poids à ceux du décrément |
|---|---|---|---|
| décrément (écrit) | 0 | 13 | — |
| pas de Newton entier | 9 (8 sur « fenêtres », 1 sur la banque saine) | 200 | 3 × 10⁻⁸ au plus |
| pas effectif (proposé) | 0 | 16 | 3 × 10⁻⁸ au plus |

- Le critère proposé rend donc les mêmes scores sur le banc. Si le contre-lecteur ou la mère le préfèrent, la seule ligne à changer est celle de l'arrêt ; rien d'autre n'en dépend.
- **Sur les banques entières** (`sortie-calcul-4-v2.txt`, `sortie-calcul-5-v2.txt`) : les 480 apprentissages de chacune des onze banques du banc convergent, en 16 tours au plus ; les 1 787 de la version 6, en 10 tours au plus. La garde, éprouvée par un calcul arrêté au premier tour, rend la sonde non calculable et C3 non tenue.
- **La divergence dépend de la banque.** J'ai rejoué `recalcul_newton_amorti_v1.py` : sorties identiques à l'octet à celles du contre-lecteur (125 apprentissages sur 480). Sur mon banc, le Newton pur ne divergeait pas : les calculs 2 (Newton pur) et 4 (Newton amorti) rendent les mêmes excès, racine par racine, sur leurs six banques communes (`sortie-calcul-2-v1.json`, `sortie-calcul-4-v2.json`). La remarque est fondée quand même : rien ne garantissait la convergence.
- Une ligne du module `sondes_batterie_v2.py` cite « 7 à 109 apprentissages sur 480 » : ce sont les comptes de mon premier essai, non conservé. La preuve rejouable est la partie E du calcul 6.

### 2.2 Remarque 5 — la version qui fait foi

- **Proposé** : dès qu'une version 8 est mesurée, elle fait foi, quel que soit son résultat ; on ne revient jamais à la version 7.
- **Écrit** : fait foi la dernière version (7, puis 8) mesurée à temps qui tient C1 et C4 ; à défaut, la version 6. La décision de tenter une version 8 est écrite avant sa mesure, et elle n'est tentée que si la version 7 ne tient pas les quatre conditions.
- **Raison.** Les deux règles ferment la fourche : rien ne se choisit après lecture. Mais sous la règle proposée, une version 8 qui manque C4 renvoie le pilote à la version 6, alors qu'une version 7 tenait C1 et C4. On perdrait une banque révisée utilisable pour avoir tenté de l'améliorer ; personne ne tenterait plus la version 8. La règle écrite ne punit pas la tentative.
- **Le cas de la contre-lecture** (version 7 : C1 et C4, pas C3 ; version 8 : C2 et C3, pas C4) rend, sous la règle écrite : la version 7, lecture en preuve seule. Les douze cas sont joués par le prototype (`sortie-calcul-4-v2.txt`, partie C).
- **Ce qui reste discutable** : quand les deux versions tiennent C1 et C4 et qu'aucune ne tient C3, la version 8 fait foi même si elle fuit plus. Choisir « la meilleure » serait un choix après lecture ; j'ai gardé « la dernière ».

### 2.3 Remarque 7 — « et seulement elle »

- La contre-lecture demande que chaque violation de C1 arrête la plantation « et seulement elle ». L'attendu gelé est : « arrêtée par l'assertion qu'elle vise ».
- **Raison.** Certaines violations en entraînent d'autres par nature. Dans le prototype, une paire à cheval sur deux mondes, ou une paire de squelettes différents, lève trois écarts : celui qui est visé, et deux écarts de proportion dans les cellules touchées (`sortie-calcul-4-v2.txt`, partie B). Exiger « seulement elle » ferait échouer une épreuve juste.
- **Le contrôle de chaîne** est écrit au § 4, mais mon prototype ne le porte pas : il n'a pas de harnais séparé des sondes. L'instrument doit le porter.

### 2.4 Remarque 10 — une fuite parfaite sur un quart des énoncés

- La phrase proposée (« une fuite parfaite sur un quart des énoncés […] peut tenir C3 ») n'est pas exacte dans tous les cas. J'ai séparé deux fuites.
- **Fuite cantonnée** : parfaite sur une part des énoncés que la sonde reconnaît. Son excès vaut cette part. Sur une écriture sur quatre : 0,250 (borne haute 0,258), C3 tombe. Sur un douzième des énoncés : 0,064 (borne haute 0,07 à 0,08), C3 tient.
- **Fuite diluée** : c'est l'artefact « grandeur » à la dose 0,25 de la contre-lecture. Un quart des énoncés suivent une loi révélatrice, mais les autres l'imitent par hasard, et la sonde ne sait pas lesquels fuient. Excès 0,086 (borne haute 0,097 à 0,100) chez moi, 0,066 chez le contre-lecteur : C3 tient.
- La limite écrite au § 8, point 5, est donc : le seuil tolère une fuite parfaite cantonnée à nettement moins d'un dixième des énoncés, et une fuite diluée jusqu'à un quart environ. Source : `sortie-calcul-4-v2.txt`, banques « cantonnée » et « grandeur ».

## 3. Décisions de la mère portées dans la v3

1. **C4 à deux règles** (R-5036, décision 1). Tranché, comme la mère le demandait :
   - jugement par la probabilité exacte, 1 − C(M − m, 3)/C(M, 3), et non par un tirage ;
   - le tirage à graine consignée (`SeedSequence(20261122, spawn_key=(3000, i, k))`) est rapporté en contrôle, avec un seuil d'audit de 0,02 ;
   - M : les affectations complètes du préfixe de tête jusqu'à 3N, chaque domaine borné étant évalué sous les variables qui le précèdent ; domaine vide : aucune instance ; domaine non évaluable : affectation écartée et comptée (aucune sur la version 6) ;
   - faux sans variable : une instance, réfuté à coup sûr.
2. **Portée** (décision 2). Aucun plancher ; portée dite en tête du rapport. Le marqueur « en attente du mot de Lazar ; défaut le 2026-11-24 vers 20:07Z » est écrit deux fois : en tête et au § 5. Au gel, ces deux lignes sont à mettre à jour.
3. **Sonde tenue à l'écart** (décision 3). Contrôlée par un Opus 5.5 neuf avant son scellement ; il ne transmet rien au concepteur avant le rapport de la mesure (§ 2.3, point 12).
4. **120 racines et écarts** : déclarés en tête, les huit écarts nommés un par un.
5. **Bloquante** (R-5038) : Newton amorti ; non-convergence = non calculable = C3 non tenue.
6. **Deux mesures rapportées, sans condition** (R-5038) : § 5 ci-dessous.

## 4. Ce que la règle du hasard coûte

La mère demande ce que la règle coûte sur les pièges, et se réserve de reconsidérer la décision si la règle rend C4 intenable par construction (R-5038). **Je ne le montre pas : la règle est tenable.** Sources : `sortie-calcul-5-v2.txt`, `sortie-calcul-6-v2.txt` (parties A et B), `sortie-calcul-4-v2.txt`.

| quoi | part des faux réfutés par trois instances au hasard |
|---|---|
| version 6, tous les faux | 0,738 (borne haute 0,743) : C4 tombe |
| version 6, faux tôt | 0,909 ; 77 % de leurs instances sont des contre-exemples |
| version 6, pièges | **0,563** (par racine : 0,46 à 0,64) ; 28 % de leurs instances sont des contre-exemples |
| piège « en queue » (faux de son premier contre-exemple jusqu'à 3N), une variable | 0,69, 0,65 et 0,65 pour 13, 31 et 46 instances |
| faux à un seul contre-exemple, une variable | 0,23, 0,10 et 0,07 |
| faux sans variable | 1 |
| banque saine du banc (un contre-exemple par faux) | 0,131 : C4 tient |
| artefact « fenêtres » (contre-exemples denses, hors des trois instances connues) | 0,717 : C4 tombe, alors que la règle A y vaut 0,000 |

- **Sur les pièges de la version 6, le coût est 0,56 et non 0,66.** Le chiffre 0,66 est la probabilité à la densité moyenne (1 − 0,7³). La moyenne des probabilités est plus basse, parce que la probabilité est concave en la densité et que les densités des pièges sont dispersées.
- **Ce que la règle impose à la version 7** : des contre-exemples rares. Repère : la part passe la moitié quand une instance sur cinq environ est un contre-exemple. Pour une variable naturelle, c'est au plus 2 contre-exemples sur 13 instances, 6 sur 31, 9 sur 46. La petite famille est la plus serrée : trois contre-exemples y comptent déjà 0,58.
- **Ce qu'elle n'ajoute pas** : les pièges « en queue » étaient déjà limités par la règle A, qui les touche tous à l'instance 3N. La règle du hasard ajoute surtout la contrainte sur les faux tôt, qui sont « faux presque partout » dans la version 6.
- **Marge** : si les pièges de la version 7 coûtaient autant que ceux de la version 6 (0,563), les faux tôt devraient coûter au plus 0,40 pour une moyenne de 0,48.
- **Avis** : garder la décision (1). Confiance 0,7. Ce qui me ferait changer : que la conception de la version 7 montre qu'aucun squelette ne peut porter à la fois un faux tôt et un piège à contre-exemples rares. Ce serait alors une question de portée (décision 2), pas de C4.

## 5. Les deux mesures rapportées pour la mère et Lazar

**a. La fuite « côté vrai ».** Définie au § 7 du texte : au point où un dixième des faux sont déclarés vrais, la part des vérités déclarées vraies, moins 0,10. Sonde des nombres, sur le banc (`sortie-calcul-4-v2.txt`) ; dernière ligne, sonde de style sur la version 6 (`sortie-calcul-5-v2.txt`). Moyenne, puis borne haute :

| banque | excès de C3 (tous les faux) | excès « côté vrai » |
|---|---|---|
| saine | −0,004 ; 0,004 | −0,007 ; 0,000 |
| « grandeur », dose 0,25 | 0,086 ; 0,097 | 0,078 ; 0,090 |
| « grandeur », dose 0,5 | 0,235 ; 0,252 | 0,221 ; 0,238 |
| **« relation », dose 0,5** | **0,109 ; 0,121** | **0,418 ; 0,430** |
| « relation », dose 1 | 0,883 ; 0,885 | 0,898 ; 0,899 |
| version 6 (sonde de style) | 0,638 ; 0,652 | 0,697 ; 0,706 |

- Lecture : une fuite qui fait reconnaître la moitié des vérités rend 0,42 côté vrai et 0,11 seulement côté faux. C3 la voit à peine ; la mesure symétrique la voit sans peine.
- Si Lazar en fait une condition, la forme la plus courte serait : une grandeur de plus par sonde, même seuil (borne haute ≤ 0,10), j = 12 à 14. La banque saine du banc la tiendrait ; l'artefact « relation » à demi-dose tomberait nettement. Ce n'est pas écrit dans la v3.

**b. La fuite cantonnée ou diluée.** Écrite comme limite au § 8, point 5 ; chiffres au § 2.4 ci-dessus. Le seuil reste 0,10.

## 6. Ajouts qui ne viennent ni de la contre-lecture ni de la mère

1. **L'artefact « fenêtres »** (§ 4). La règle du hasard entre dans C4 : il lui faut un artefact où elle tombe alors que la règle A tient. Énoncé « n < K ou n > L », faux sur une fenêtre large placée à côté des instances 3N, 1 et N + 1. Règle A : 0,000 ; règle du hasard : 0,717.
2. **Le seuil d'audit du tirage de contrôle** (§ 1, C4 ; § 4). Un écart de plus de 0,02 entre le tirage et le calcul exact fait auditer le calcul. Sans seuil, le contrôle ne contrôlait rien. Éprouvé : calcul juste, écart 0,001 ; calcul faussé (contre-exemples comptés jusqu'à N seulement), écart 0,066 (`sortie-calcul-6-v2.txt`, partie F). La mère peut le retirer : le tirage redevient un nombre rapporté.
3. **« Non calculable » pour la règle du hasard** (§ 1, C4) : si les instances d'un faux ne peuvent pas être énumérées. Le générateur les énumère déjà pour certifier la strate ; le cas ne devrait pas se présenter.
4. **Une garde de convergence pour la sonde tenue à l'écart**, si elle apprend par un calcul itératif (§ 2.3, point 10).
5. **§ 8** : points 4, 5 et 12 neufs ; point 6 réécrit (C4 peut encore être tenue à la lettre par des contre-exemples rares mais toujours logés au même endroit saillant).
6. **§ 9** : le prorata passe de 0,80 à 0,85 (confirmé par le contre-lecteur) ; C4 de 0,55 à 0,70 (deux règles) ; une ligne neuve pour la convergence (0,85).

## 7. Ce que le prototype ne porte pas

L'instrument, écrit par Opus et contre-lu, doit porter ce qui suit ; mon prototype ne le fait pas.

- Le contrôle de chaîne (§ 0, § 4).
- La garde « plus d'un énoncé de la sous-banque sur dix noté 0 » : le compte est rendu, la garde n'est pas codée. Il vaut zéro sur toutes les banques de ces calculs.
- La garde « instances non énumérables » : le prototype s'arrêterait sur une erreur au lieu de rendre « non calculable ».
- Le tirage de contrôle par la vérification exacte de la course : le prototype lit le statut des instances tirées dans le profil qui sert au calcul exact. Son contrôle est donc plus faible que celui du texte.
- La sonde tenue à l'écart, par nature.

## 8. Prévision mise à jour

Elle remplace celle des notes à la mère, § G.

| issue | avant | maintenant |
|---|---|---|
| une version 7 tient C1 et C4 avant le 4 décembre 23:59Z | 0,55 | 0,50 |
| elle tient aussi C2 et C3 (lecture en verdict ouverte) | 0,20 | 0,20 |

La règle du hasard interdit les faux « faux presque partout » : la version 7 doit planter des contre-exemples rares dans les deux strates. Le risque principal reste le point 2 de C1 (autant de paires à faux tôt que de paires à piège par squelette), non la règle elle-même.

## Empreintes (SHA-256 entières, relevées par `sha256sum` le 2026-11-22)

| pièce | chemin | sha256 |
|---|---|---|
| texte corrigé, version 3 | `docs/notes/mathematiques-nouvelles-v1/banque-revisee-v1/batterie-v1/batterie-fuite-banque-revisee-v3.md` | `78556fc53a4f66e945579aa6321e58a4252ed1a90ef81cf3e7f2b58d6c80c08c` |
| contre-lecture de la version 2 | `…/batterie-v1/contre-lecture-batterie-v1.md` | `9718ec040598dd73912e525f3403856ee08e5ffd69e8b7c0c447f80c435f4790` |
| version 2, remplacée | `…/batterie-v1/batterie-fuite-banque-revisee-v2.md` | `6b02a1c86d83355091bbfeb499fd1996fff99b96916f18752d2b8b3404568eee` |
| sondes et conditions, prototype v2 | `…/batterie-v1/calculs-d-appui/sondes_batterie_v2.py` | `83c45cf9c41b22b6ab4d63b46af557c31a4725a00f661986c0fb8cea683ae50b` |
| calcul 4 (banc d'épreuve) | `…/calculs-d-appui/calcul_4_banc_d_epreuve_v2.py` | `483700afe831342fc47f1e6ef80c02df533ce93ce370ee7ca4822425ee8b18b2` |
| sa sortie | `…/calculs-d-appui/sortie-calcul-4-v2.txt` | `458daedeac36a72f6277f0388dbaf6f189c75b3acd711c7752b9a34ea7872fc8` |
| calcul 5 (version 6) | `…/calculs-d-appui/calcul_5_version_6_v2.py` | `5908e732412a8683b82250a6484accb59af311c5f301171af197075b3de15df8` |
| sa sortie | `…/calculs-d-appui/sortie-calcul-5-v2.txt` | `4e1cd5c4baa07827a9ecbabbaa6d58e4bfd5bb3c87ffac18be7a799b1381abcf` |
| calcul 6 (cas d'école, critère d'arrêt, audit du tirage) | `…/calculs-d-appui/calcul_6_cas_d_ecole_v2.py` | `ed7bf57e5e83fdf896559032fac0d67fcd832d3812680016c5b13083c377cca2` |
| sa sortie | `…/calculs-d-appui/sortie-calcul-6-v2.txt` | `2cc95490f89915575e3d3693319bf6b1b76a3ecdae5f7a2237bf2a7c90753ae5` |
| recalcul du contre-lecteur (Newton amorti), rejoué à l'identique | `…/batterie-v1/contre-lecture-calculs-v1/recalcul_newton_amorti_v1.py` | `272970e6ba520ba6386b0982762c0e31067d0e4a97782c41ae400bbfba767d2a` |

Chaque calcul a été passé deux fois, sur un seul fil ; les sorties sont identiques à l'octet. Les sorties en JSON sont dans le même dossier, avec leurs compagnons. Décisions citées : R-5036 et R-5038, `registres/decisions.md` sur `main` (lues au commit `184aa5abf7a9502d60bf7f44a6e0f5f97f7183b9`).
