# Plan du branchement — l'expérimentateur et l'étage des tests de mort sur la course principale d'auto-conception — v3

**Cette v3 porte les seize corrections de la contre-lecture de la v2** (`0b041dab3ba0db5e69318b6bca90b8af1aff2b3f0929898a855d5747cbe36889`, verdict « À corriger ») et les décisions que la mère a prises depuis. La v2 (`7cf3c78d…`) et la v1 (`0bb27bc0…`) restent telles quelles (règle R12). La table « correction → lieu » est au rapport joint.

Pièce de travail (classe C), non scellée. Elle planifie ; elle ne tranche rien. Processeur seul : aucun appel, aucune dépense, aucun code lancé, aucune écriture dans un dépôt.

- Auteur : planificateur du branchement de l'expérimentateur, modèle F.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 08:00:56Z, après les lectures, avant l'écriture.
- Lecture neuve : la contre-lecture, en entier ; `origin/main` au commit `e1103c83b858722da299e7438cc26f79d8e0b501` pour les deux registres et pour deux pièces de la course v9 (§ 7.3, D8).
- Ce texte ne porte aucun identifiant de modèle, aucun nom de clé, aucune méthode d'attaque, aucun contenu de carte.

Sigles : CL, la contre-lecture ; NC, la note de conception générale (`4f3ae86f…`), non contre-lue ; PM et DM, le plan du pilier mathématique et le devis de son pilote, sous la réserve de la mère dite à la v2 ; A69, C70, R68, F68, L10, NA, DH comme à la v1.

**Aucun prix n'a été relevé aujourd'hui.** Tous les montants sont des calculs à la main sur des valeurs lues.

## 0. En bref

1. **La note répond à D2** par une course appariée de l'organisme, avec et sans le mécanisme de la carte, sur des mondes à lois plantées scellés d'avance : sur un banc à proposeurs écrits par programme d'abord, avec de vrais proposeurs ensuite pour les seules cartes qui tiennent. C'est une proposition non contre-lue ; son nœud N1 reste à Lazar, sans défaut.
2. **Les quatre premiers pas de la note n'exigent aucune génération neuve.** Le pas 3 porte sur les seuls témoins ; les pas 1 et 4 portent sur les cartes de la course v9. La boucle à plusieurs générations (lots E5 et E6) sort du chemin critique, sauf si Lazar retient D8 (c) (§ 7.3).
3. **« 94 cartes » est une borne haute.** La porte commune ne vaut que pour les cartes qui n'ont pas déjà un texte scellé (NC, § 4.1) : les cartes des lignes 1 et 3 et de l'héritage en sortent. Leur nombre ne m'est pas connu.
4. **Treize lots** : E0 à E9, dont E2 et E3 récrits, plus C1, C2 et C3.
5. **Calendrier** : de 45 à 54 heures de code et de vérification ; de 23,5 à 59 heures de textes, estimation non revue, que je crois basse de 6 à 10 heures. Le chemin critique est le texte de la porte s'il approche sa borne haute, le code s'il reste à sa borne basse.
6. **Deux dépenses, deux lignes.**
   - *Ligne 1, la première dépense : la mesure de l'expérimentateur sur les seuls témoins.* Machine : 2, 4 ou 12 heures, soit de 0,15 à 3,36 USD aux deux tarifs relevés, et de 2,60 à 15,60 USD à la borne haute de 1,30 USD de l'heure. Appels : de 0,57 à 49 USD, lecteur témoin compris.
   - *Ligne 2, les cartes, après D8 et sur un second devis.* Machine : 7, 25 ou 48 heures, soit de 0,51 à 13,44 USD, et de 9,10 à 62,40 USD à 1,30 USD de l'heure. Appels : de 13 à 385 USD pour 94 cartes au plus, lecteur compris, traducteurs non chiffrés.
   - Le barreau 2 : de l'ordre de 590 USD par carte à cinq espèces, **de propositions seules, tiré d'un devis, hypothèse**, hors appels de l'étage.
7. **Quatorze décisions** : N1 à N7 posés par la note ; D1, D5, D6, D7 et D8 posées par ce plan ; D3 et D4 inscrites au registre (R-4394). D5 et D6 sont récrites ensemble ; D8 est récrite sur le modèle des exceptions accordées.

## 1. Ce qui existe

Le § 1 de la v1 et le § 1 de la v2 valent. S'y ajoute, lu ou rapporté depuis :

| pièce | source | état |
|---|---|---|
| contre-lecture du plan v2 | disque, `docs/notes/organisme-auto-conception-v1/plan-experimentateur-course-principale-v2/contre-lecture-v1/contre-lecture-plan-course-principale-v2-v1.md`, `0b041dab…`, égale à son compagnon | lue en entier |
| D3 et D4 | `registres/decisions.md`, R-4394 : « Mère : AC-1, rien de servi » | inscrites ; relu par moi |
| relevé du lot 0 du véhicule NA-1 | R-4411, `10ac79ec…` | rendu ; une dizaine de contradictions, deux bloquantes (routage par rôle, texte fixe d'un adaptateur) ; calendrier de NA-1 passé à 48 à 60 heures, départ le 25 ou le 26 (R-4415, R-4427) ; **non ouvert par moi** |
| ordre v4 de la course « seuil et moniteurs » | R-4425, `390af604…` | **scellé** ; une v5 est en contrôle (R-4432) ; non ouvert par moi |
| mandat de l'auteur des mondes plantés de cette course | R-4426 (`75f0acd3…`), puis R-4433 (`6774507c…`, devis `4f5dca99…`) | en contre-lecture ; auteur de la troisième lignée ; non ouvert par moi |
| erratum 1 du plan du pilier | R-4431, `1827b680…` | N6 prime ; l'empreinte des calculs y est corrigée ; aucune date promise ; non ouvert par moi |
| définition scellée de « mieux » | `4eae96bc…` ; lue par le contre-lecteur (CL, § 2, point 8) | cas A et B à seuils chiffrés ; cas C lisible sur plusieurs générations seulement |
| proposition des cartes à éprouver | `origin/main`, `docs/notes/organisme-auto-conception-v1/course-v2/proposition-cartes-a-eprouver-v9-v1.md`, `a2cd45ad…` | lue par ses titres et ses comptes seulement (§ 7.3) |
| lecture descriptive de la course v9 | `origin/main`, `docs/notes/organisme-auto-conception-v1/course-v2/lecture-course-v9-v1.md`, `0306adf7…` | lue par ses titres et sa ligne 99 seulement |

Une question du lot E0 a sa réponse : la course v67 a joué l'étage v57, par le tour fermé v64 (CL, § 2, point 4).

## 2. D2 confrontée au § 2.2 de la note

### 2.1 La réponse de la note

| | barreau 1, la course de banc | barreau 2, la course réelle appariée |
|---|---|---|
| l'organisme | un banc écrit par nous : proposeurs écrits par programme, fonctions de jugement, mondes à lois vraies et fausses plantées | l'organisme réel, vrais proposeurs, tests de mort réels dans la boucle |
| la carte y entre comme | un greffon : une fonction appelée une fois par génération, dans le bac, qui ne reçoit que ce que recevait le mécanisme remplacé, jamais la vérité | le même greffon, branché |
| bras, sur les mêmes graines | sans (le témoin) ; avec ; placebo de même forme ; bases bon marché du point de greffe, en liste fermée | avec et sans, mêmes mondes |
| issue | « invalide » si la carte fait promouvoir plus de lois fausses que le niveau annoncé ; **« sans gain » si son écart apparié au témoin, au placebo et à la base ne passe pas le seuil de son cas**, sur des familles de mondes tenues à l'écart ; sinon « tient au banc », qui n'est pas une adoption | « tient » ou « ne tient pas » |
| coût | du processeur ; l'expérimentateur se paie une fois par carte | de l'ordre de 590 USD par carte à cinq espèces, 90 à deux : **propositions seules, tiré du devis de l'héritage, hypothèse** (NC, § 2.2, point 4 ; R-4422) ; les appels de l'étage dans la boucle n'y sont pas |

Quatre règles (NC, § 2.1) : aucun agent n'écrit le critère de mort ; le code d'un agent rend une décision, jamais une mesure ; l'épreuve passe d'abord ses témoins plantés ; un mort reste mort.

### 2.2 Ce que la note règle des objections de la v1

Inchangé depuis la v2, § 2.2 : l'objet servi à l'étage est une fiche écrite par l'orchestrateur ; l'étage v5 sert à écrire et sceller le greffon ; le proposeur choisit un cas et une taille, jamais l'épreuve ; le pont ne remplit que des champs fermés à extrait cité ; l'oracle passe par le comparateur sans juge du palier 0b ; les bornes de 0,06 à 0,90 USD ne valent que pour un script de loi.

### 2.3 Ce que la note tranche

**Rien** : pièce de travail non contre-lue, recommandation (a) à 0,7 sur N1, sans défaut. Je tiens sa forme d'épreuve pour base de planification, parce que la mère me l'a demandé.

### 2.4 Ce qui reste ouvert

1. Le banc de la ligne 1 se rend-il greffable sans réécriture ? Non établi (NC, § 6).
2. L'étage v5 accepte-t-il la fiche écrite par l'orchestrateur ? « À confirmer sur le code. »
3. Le coût d'un greffon : de 0,08 à 4 USD, non mesuré, lecteur témoin non compris (§ 6.3).
4. La part des cartes par barreau et le nombre de cartes hors gabarit.
5. `numpy` dans le bac ; la durée d'une exécution nue.
6. **Où tourne le rejeu du barreau 1** (§ 3.2) : la note est ambiguë.
7. Les seuils de la définition scellée : les cas A et B en portent de chiffrés ; le cas C renvoie au seuil de B « à la dernière génération jouée », contre un placebo, et ne se lit donc que sur un banc à plusieurs générations (CL, § 2, point 8 ; je n'ai pas ouvert la pièce). Ce sont des tailles d'effet, à joindre au test exact des rangs signés. À écrire au texte de la porte.
8. La liste fermée des points de greffe, celle des bases, et les quatre mécanismes témoins : des formes, rien d'écrit.

### 2.5 Ce qui reste à Lazar

N1, N2, N3, N4 ; D1, D6 et D8.

## 3. Ce qui manque, après la note

### 3.1 Relecture du § 2 de la v1

| v1 | v3 |
|---|---|
| l'objet de l'épreuve, les données, l'oracle, les mondes | répondu en proposition (NC, § 2.2) ; manquent le banc greffable, les mondes, les mécanismes témoins, la table d'admission, le texte de la porte |
| sommet d'étage, enveloppe | inchangé, avec un paramètre : la forme d'épreuve ; la forme imposée du tour fermé reste la seule admise en réel tant qu'un additif n'en nomme pas d'autre (NC, § 3.1) |
| le pont | pont à extrait cité, deux traducteurs, gabarit « mécanisme » |
| classes d'issue | celles d'A69, plus les motifs « invalide » et « sans gain », plus les statuts « hors gabarit » et « non éprouvée (épreuve morte) » |
| boucle à plusieurs générations, lecture | hors du premier emploi ; requis au pas 5 de la note |
| récompense de l'héritage | l'issue par tentative et son coût, rien de plus fin ; rien de servi d'ici la lecture de l'épreuve de l'héritage (NC, § 2.5) |
| les juges | pour information, jamais un choix ni un repêchage |
| lanceur, additif, préenregistrement | **un lanceur de la série AC-1**, qui porte la table des épreuves ; un additif par épreuve ; un préenregistrement de la porte, si N3 l'accorde |
| le bac | trois lieux : le bac, la machine jetable, la mère ; ni clé ni vérité sur la machine ; inventaire et versement scellé avant destruction |
| mesures et gardes | plus les huit gardes de NC, § 2.6 |

**Le lanceur.** La note loge la table des épreuves « dans le lanceur de course 11 » (NC, § 3.1, point 6). L'additif scellé de la v69 fait du lanceur 11 celui du seul palier 1 : « Tout autre jeu d'options est refusé par le lanceur version 11 lui-même » (A69, § 7, point 5). Avec D3 inscrite, le lanceur de cette course prend un nom de la série AC-1 ; je propose `lancer_etage_auto_conception_ac_v1.py`, « lanceur AC-1 ». De même, la v69 refuse le moteur réel hors du palier 1 (A69, § 2, C3) : il faut à AC-1 son propre lanceur de l'orchestrateur, qui lève le refus pour son seul régime, comme NA-1 le fait pour le sien. À signaler à l'auteur de la note.

**Manques neufs** : un premier compte des cartes (D8) ; deux traducteurs de deux lignées, dont aucune n'est l'expérimentateur ; un modèle pour l'expérimentateur (N4).

### 3.2 Le lieu du rejeu du barreau 1 — question à l'auteur de la note

La note dit deux choses. Le rejeu du script scellé est « le seul code neuf du côté de la machine » (NC, § 3.1, point 2). Le banc et la vérité sont chez la mère, et l'issue se calcule « sur processeur » chez elle (NC, § 2.5, § 4.1 ; N6). Or le barreau 1 rejoue, à chaque génération du banc, du code écrit par un modèle, sur tous les mondes et tous les bras.

| lecture | ce qu'elle exige | ce qu'elle coûte |
|---|---|---|
| **(i) le rejeu chez la mère** | un bac local entre le greffon et la vérité, comme au palier 0a ; le dire au texte de la porte, avec N6 | aucune location ; du temps de processeur chez la mère, non mesuré |
| **(ii) le rejeu sur la machine jetable** | la vérité y monte, ce que N6 (a) interdit, ou le banc se coupe en deux : décisions du greffon sur la machine, mesure chez la mère, génération par génération | des heures de location en plus, non mesurées ; des allers et retours par génération |

**Je ne tranche pas.** La question va à l'auteur de la note, avant E3 et C1. Ma lecture provisoire, pour le devis seulement : (i), parce que N6 (a) a un défaut sous 48 heures et qu'elle seule le tient sans couper le banc. Le temps de ce rejeu est compté au § 6.2, comme une hypothèse nommée.

## 4. Les lots

### 4.1 E2 et E3 récrits

**E2 révisé — le pont à extrait cité et le gabarit « mécanisme ».**
- Contenu : la fiche à champs fermés d'une carte (point de greffe en liste fermée ; cas de la définition ; quantité, signe et taille de l'effet, sinon « lu au plus prudent ») ; le programme qui vérifie à l'octet chaque extrait cité ; la règle d'accord des deux traducteurs ; le statut « hors gabarit » ; le constructeur de la fiche servie à l'étage ; les gardes de l'entrée de l'expérimentateur.
- Dépend de : E0 ; N1 ; D8 ; **E3**, pour la liste fermée des points de greffe.
- Partage avec la course « seuil et moniteurs » : sa mise en forme fixe par deux traducteurs, telle que la porte son ordre v4 scellé (`390af604…`, R-4425). **Proposition, non un fait** : un seul programme de vérification d'extrait, deux gabarits. À adresser à ses rédacteurs.
- Avec le pilier mathématique : rien du pont.

**E3 révisé — le banc de course greffable, les mondes à lois plantées, les mécanismes témoins.**
- Contenu : le banc ; un point de greffe par étage du trajet d'une carte ; le générateur de mondes à lois vraies et fausses plantées, graines dérivées par monde et par course (règle R9), racine gardée avec la vérité ; les familles tenues à l'écart ; les bras ; les quatre mécanismes témoins et leur sort attendu ; le banc d'étalonnage, joué à 0 USD, qui scelle la table d'admission.
- Les témoins d'abord : aucune carte ne passe avant la table d'admission scellée ; un témoin « doit mourir » qui tient fait une épreuve morte, arrêt rapporté, jamais un repli.
- L'issue se calcule chez la mère ; le lieu du rejeu est la question du § 3.2.
- Dépend de : E0 ; N1 ; **le comparateur sans juge du palier 0b** ; **la lecture de la définition scellée** ; la réponse à la question du § 3.2.
- Partage avec la course « seuil et moniteurs » et avec le pilier. **Proposition** : un seul module « graines, disjonction, clé scellée, famille tenue à l'écart », plusieurs générateurs. Le mandat de l'auteur des mondes plantés de « seuil et moniteurs » est déjà en contre-lecture (R-4426, R-4433) : la proposition est à lui porter maintenant, sinon le module s'écrira deux fois. Le générateur du pilier est son lot B1 (PM).
- Heures : 8 à 15 (NC, § 3.3).

### 4.2 La table des lots

| lot | contenu | dépend de | partagé avec | premier emploi ? |
|---|---|---|---|---|
| E0 | relevé du code, sans écriture ; **il lit d'abord le relevé du lot 0 de NA-1** (`10ac79ec…`) et ne repose pas ses questions ; questions propres de la v1, moins la troisième, plus : le banc de la ligne 1 est-il greffable ; l'étage accepte-t-il la fiche écrite par l'orchestrateur ; `numpy` dans le bac | — | NA-1, lot 0 | oui |
| C1 | texte de la porte pour cet emploi : gabarit, banque de témoins, critères et seuils par cas, table d'admission (classe A) | N1, N3 ; E3 ; la réponse du § 3.2 | un texte par emploi | oui |
| E3 révisé | § 4.1 | E0 ; N1 ; comparateur du palier 0b ; définition scellée ; § 3.2 | pilier, « seuil et moniteurs » | oui |
| C2 | mesure hors machine, porte des lots, registre et garde « un mort reste mort » | E3 | les trois emplois | oui |
| E2 révisé | § 4.1 | E0 ; N1 ; D8 ; E3 | « seuil et moniteurs » | oui, pour la ligne 2 |
| E1 | sommet d'étage et enveloppe | E0 ; palier 0b | palier 1 : écrit une fois (D5) | oui, pour la ligne 1 |
| C3 | rejeu du script scellé ; paramètre de forme d'épreuve | E1 | les trois emplois | oui, pour la ligne 1 |
| E4 | la projection des classes dans les fichiers de la course ; C2 en a pris le cœur : compté 2,75 heures par prudence, sans doute 1 à 1,5 | C2 | palier 1 | oui, petit |
| E7 | mesures et export | C2 | forme de NA-1, lot 7 | oui |
| E8 | **lanceur AC-1** et lanceur de l'orchestrateur AC-1 : table des épreuves, épinglages, parts, machine déclarée, durée de location, attestation du bac, ligne d'accord | E1, C3 ; **C1**, pour la banque et la table d'admission ; **N4**, pour le rôle et sa part | A69, § 7, pour la liste ; NA-1, lot 8, pour les relais, à relire sur son relevé | oui, pour la ligne 1 |
| E9 | mise en route et essai du bac, inventaire et versement avant destruction, essai à blanc de bout en bout | E7, E8 | palier 1 ; NA-1, lot 9 | oui, pour la ligne 1 |
| E5 | course à plusieurs générations avec étage | E1, E2, E4 | base v68 | non, sauf D8 (c) |
| E6 | lecture du registre par la génération suivante | E4, E5 | NA-1, lot 5 | non ; D4 inscrite : rien de servi à la première course |

**Le régime du premier emploi est un régime neuf — proposition.** Pour les lignes 1 et 2, l'étage tourne sans génération de proposeurs : sur des témoins, puis sur des cartes archivées. Je l'appelais « étage seul » à la v2 comme un fait ; c'est une proposition. La note ne le nomme pas pour cette course. GO-2026-11-21-16 n'accorde l'étage seul qu'à la course « seuil et moniteurs ». Le lanceur v10 refuse « les tests de mort seuls » (L10, l. 14 à 16). Il lui faut donc son additif et le mot de Lazar : c'est D1, récrite pour le nommer (§ 7.2).

**Chemin critique, aux deux bornes de C1.** Le code jusqu'au premier dollar (E0, E1, C3, E8, E9) fait de 17,25 à 18,25 heures. Si C1 reste à sa borne basse (3,5 heures), c'est ce code qui est critique. Si C1 approche sa borne haute (39 heures, le rythme mesuré du texte du palier 0b), c'est le texte. E8 dépendant de C1, le lanceur ne se fige dans aucun cas avant la table d'admission.

**Ordre.** À 0 USD : E0 ; E3 et le brouillon de C1 ; C2 ; table d'admission scellée ; premier compte des cartes par la voie qui n'ouvre rien (D8, option (d)). Pour la ligne 1 : E1 et C3 ; E8 et E9 ; additif, devis, ligne, N4. Pour la ligne 2 : D8, E2, second devis. E5 et E6 après.

**Ce qui ne s'écrit pas deux fois** : comme à la v2, § 4.2, sous les deux propositions du § 4.1.

## 5. Le calendrier

Heures de session, sans appel.

| | v1 | v3 |
|---|---|---|
| code et vérification | 37,75 | **45 à 54** (E3 révisé 8 à 15 ; C2 2 à 3 ; C3 1 à 2) |
| dont premier emploi, sans E5 ni E6 | — | 36,5 à 45,5 |
| textes, hors porte | 20 | 20, **estimation non revue** |
| C1, texte de la porte | — | 3,5 à 39 |
| **textes** | 23 | **23,5 à 59** |
| **somme** | environ 61 | **68,5 à 113** |

**Les 20 heures de textes viennent de la v1, à dix lots et sans pont.** Elles ne comptent ni les consignes des deux traducteurs, ni le gabarit « mécanisme », ni le mandat et le programme du compte des cartes, ni un additif par épreuve, ni trois mandats de lot de plus, ni la question à l'auteur de la note et sa réponse. Mon supplément, hypothèse sans mesure : 6 à 10 heures. La borne basse de 23,5 est donc sans doute basse ; avec le supplément, 29,5 à 69, et la somme 74,5 à 123.

**L'ordre du compte et de la mesure — proposition, écart à la lettre de la note.** La note veut le compte des cartes avant tout devis (« sans ce compte, aucun devis », NC, § 4.1, pas 1). La mère a fait de la mesure sur les seuls témoins la première dépense (D6). Je propose de lire ainsi : le devis de la ligne 1 est borné par le nombre de témoins fois le plafond par greffon ; il ne dépend d'aucune carte et peut partir sans le compte. Le compte précède le devis de la ligne 2, sans exception. Si la mère veut la lettre de la note, la ligne 1 attend D8 ; l'option (d) de D8 rend un premier compte à 0 USD et lève alors l'attente.

**Horloge, au plus tôt, sous condition du mot de Lazar sur l'ordre des pilotes.**
- Table d'admission scellée, à 0 USD : trois à quatre jours après le mot sur N1.
- Ligne 1 : il faut en plus le sommet d'étage, les lanceurs AC-1, le bac, un additif, un devis contre-lu, une ligne, N4, et D1 pour le régime neuf. Pas avant le 28 novembre.
- Ligne 2, **une seconde dépense, sur un second devis** : le verdict d'une carte se calcule sur processeur, mais chaque carte coûte une session d'expérimentateur, un lecteur témoin et deux traductions. Après la mesure, après D8, après le compte.

**Ce que je ne peux pas dater** : les nœuds ; la lecture du palier 0b ; la place du modèle F, que NA-1 occupe désormais pour 48 à 60 heures (R-4415, R-4427), avec le pilier et la course « seuil et moniteurs ».

## 6. Le devis du bac et des appels

### 6.1 Ce qui est lu

| valeur | source | nature |
|---|---|---|
| 0,0675 à 0,0733 USD de l'heure | F68, décision 4 | relevé du 11 ou du 12 novembre, non revérifié |
| 0,28 USD de l'heure ; borne haute du programme 1,30 | DM, l. 15, sous la réserve de la mère | observé le 12 novembre ; borne écrite |
| course v67 : 14 tests en 45,5 minutes, soit 3,25 minutes par test | verdict de la v67 | mesuré |
| expérimentateur à la v67 : au plus 0,081 USD par test ; **lecteur témoin : au plus 0,061 USD par test** | NC, § 1 ; CL, § 2, point 5 | mesuré, appels de proposeur compris, pour un script de loi |
| plafond par défaut de la session du lecteur témoin : 0,10 USD, noté « supposé » | DH, § 5 | borne écrite dans le code |
| plafond d'une formalisation dans un autre brouillon : 4 USD par item | NC, § 2.2 | non mesuré |

### 6.2 Machine : deux lignes séparées

**Ligne 1 — la mesure sur les seuls témoins (première dépense).**

| cas | hypothèses | heures | à 0,0733 | à 0,28 | à 1,30 |
|---|---|---|---|---|---|
| bas | 4 témoins au rythme de la v67 ; une heure de mise en route et d'essai du bac | 2 | 0,15 | 0,56 | 2,60 |
| haut | 12 témoins, 9 minutes chacun ; deux heures de mise en route | 4 | 0,29 | 1,12 | 5,20 |
| pire | la durée maximale de cette ligne atteinte | 12 | 0,88 | 3,36 | 15,60 |

Plafond proposé : **5 USD, durée maximale 12 heures**. Il tient jusqu'à 0,41 USD de l'heure ; au-delà, le devis se refait.

**Ligne 2 — les cartes, après D8, second devis.**

| cas | hypothèses | heures | à 0,0733 | à 0,28 | à 1,30 |
|---|---|---|---|---|---|
| bas | 94 cartes au plus, au rythme de la v67 ; une heure de mise en route | 7 | 0,51 | 1,96 | 9,10 |
| haut | 94 cartes au plus, 9 minutes chacune ; 8 heures d'exécutions de mise au point ; 2 heures de mise en route | 25 | 1,83 | 7,00 | 32,50 |
| pire | la durée maximale atteinte | 48 | 3,52 | 13,44 | 62,40 |

Plafond proposé : **15 USD, durée maximale 48 heures**. Il tient jusqu'à 0,31 USD de l'heure. Les deux lignes font 20 USD au plus, contre 15 à la v2, qui les mêlait.

**Le rejeu du barreau 1 n'est dans aucun de ces cas.** Sous la lecture (i) du § 3.2, il ne loue rien : il prend du temps de processeur chez la mère, que rien ne mesure. Sous la lecture (ii), il ajoute des heures de location à la ligne 2, que rien ne mesure non plus, et la durée maximale de 48 heures peut ne pas suffire. Dans les deux cas, ce temps est à chiffrer par E3, sur le banc d'étalonnage, avant le devis de la ligne 2. Quatre et douze témoins, huit heures de mise au point, douze et quarante-huit heures de durée maximale sont mes hypothèses.

### 6.3 Appels : ce qui n'est mesuré nulle part

| poste | borne basse | borne haute | nature |
|---|---|---|---|
| un greffon, expérimentateur seul | 0,08 USD | 4 USD | relevé d'un script de loi ; plafond d'un autre brouillon |
| le lecteur témoin, par greffon | 0,061 USD | 0,10 USD | relevé de la v67 ; plafond par défaut « supposé » |
| **un greffon, lecteur compris** | **environ 0,14 USD** | **4,10 USD** | |
| ligne 1, 4 à 12 témoins | 0,57 USD | 49,20 USD | |
| ligne 2, 94 cartes au plus | 13,35 USD | 385,40 USD | moins les cartes hors gabarit et celles déjà sous un texte scellé |
| les deux traducteurs, deux appels par carte | — | — | **non chiffrés**, ni par la note ni ici |

**Le lecteur témoin.** L'étage v5, « sans un octet changé », sert la fiche à un lecteur témoin (A69, § 9, réserve 1 (c)). La v2 ne le comptait pas. Avec lui, la borne basse monte d'environ 75 %. Le retirer serait un écart à l'étage tel quel, à écrire à l'additif ; je ne le propose pas.

**Le barreau 2** : de l'ordre de 590 USD par carte à cinq espèces, 90 à deux. Ce sont dix générations de bras au prix du devis de l'héritage : propositions seules, hypothèse, hors appels de l'étage dans la boucle. Sur devis à part, après les issues du banc.

**Lecture.** La location reste négligeable devant les appels. La ligne 1 est petite et bornée ; elle donne le chiffre sans lequel aucun devis de la ligne 2 n'est honnête.

## 7. Les décisions

Aucun défaut pour une dépense. Aucune n'est prise ici.

### 7.1 Nœuds de Lazar posés par la note

Chacun est au format complet dans la note, § 6 ; je les condense.

| nœud | décision | recommandation de la note | défaut |
|---|---|---|---|
| N1 | ce qu'un test de mort éprouve sur une carte : (a) course appariée à deux barreaux, pont pour les cartes de la v9 ; (b) course réelle seulement ; (c) engagement écrit par le proposeur | (a), 0,7 | aucun |
| N2 | champs de fiche des courses suivantes, qui rouvre 3a : (a) trois champs fermés de plus ; (b) inchangés | (a) pour la suite, (b) pour les cartes de la v9 ; 0,65 | aucun |
| N3 | un seul texte scellé pour la porte commune, ou un texte par ligne | le texte unique pour les cartes sans texte scellé ; 0,6 | aucun |
| N4 | modèle et plafond de l'expérimentateur d'épreuve : (a) une autre lignée que le lecteur témoin, nommée par Lazar ; (b) attendre celui de la v67 ; (c) deux lignées partout | (a), 0,6 | aucun |
| N5 | règle de l'épreuve morte | (a), 0,65 | (a) sous 48 heures |
| N6 | où se calcule l'issue : (a) chez la mère ; (b) sur la machine | (a), 0,8 | (a) sous 48 heures |
| N7 | ordre au pilier mathématique | (a), les épreuves d'abord ; 0,75 | (a) sous 48 heures pour la conception |

- N1 : j'appuie (a) à 0,65, un cran sous la note.
- N4 : la mère recommande à Lazar un modèle du premier relais comme expérimentateur. **Ce n'est pas accordé.** E8 et le devis de la ligne 1 en dépendent ; la course « seuil et moniteurs » aussi (R-4432, R-4433).
- N6 : la question du § 3.2 s'y rattache.

### 7.2 Décisions posées par ce plan

**D1 — Étendre le régime « tests de mort réels » à la course principale, sous sa variante sans génération.**
- Décision : le régime s'étend-il à la course principale, et couvre-t-il un étage joué sans génération de proposeurs, sur des témoins puis sur des cartes archivées ?
- Enjeu : A69 lie l'allumage au seul palier 1 ; GO-2026-11-21-16 n'accorde l'étage seul qu'à la course « seuil et moniteurs » ; le lanceur v10 refuse « les tests de mort seuls ». Sans un mot qui nomme cette variante, les lignes 1 et 2 ne peuvent pas s'allumer.
- Options : (a) oui, variante nommée, sous un additif propre à AC-1 ; écriture en routine, allumage sur devis et ligne. Avantage : suit la priorité dite ; ouvre la mesure sur les témoins. Inconvénient : un régime de plus avant qu'aucun n'ait tourné. (b) oui pour la course à générations seulement, après le palier 1. Avantage : un seul régime neuf à la fois. Inconvénient : ferme les lignes 1 et 2, donc D6 (a). (c) non.
- Recommandation : (a), confiance 0,7. Aucun défaut.

**D3 — Nom de version : inscrite.** « AC-1 » (R-4394).

**D4 — Ce que lit la génération suivante : inscrite.** Rien de servi à la première course (R-4394). Sans objet au premier emploi, faute de génération suivante.

**D6 — La première dépense de ce branchement.**
- Décision : quelle dépense demande-t-on d'abord à Lazar pour cette course ?
- Enjeu : aucun coût de greffon n'est mesuré, à un facteur cinquante près ; sans cette mesure, tout devis des cartes est une fourchette de 13 à 385 USD.
- Options : (a) **la mesure de l'expérimentateur sur les seuls témoins**, sur la machine jetable : ligne 1 du § 6, bornée par le nombre de témoins fois le plafond par greffon. Avantage : petite, bornée, rend le premier chiffre réel et une première lecture de fidélité. Inconvénient : demande le sommet d'étage, le bac et N4 avant que le palier 1 n'ait tourné. (b) attendre la mesure du palier 1. Avantage : rien à écrire pour cette course d'ici là. Inconvénient : le palier 1 mesure un script de loi, non un greffon ; sa mesure ne se transpose pas. (c) un devis des cartes sur les bornes, avec un plafond d'arrêt. Avantage : une seule ligne. Inconvénient : dépense à l'aveugle, contre la note.
- Recommandation : (a), confiance 0,65. C'est la recommandation de la mère ; elle remplace celle de la v1. **Aucun défaut** : rien ne se loue ni ne s'appelle sans devis contre-lu et ligne de calcul.

**D5 — L'ordre des écritures et du premier allumage, accordé à D6.**
- Décision : dans quel ordre s'écrivent le socle commun, cette course, le palier 1 et NA-1, et laquelle s'allume d'abord ?
- Enjeu : le sommet d'étage, le rejeu et l'essai du bac servent au palier 1 et à cette course ; D6 (a) allume cette course avant le palier 1 ; la place du modèle F est unique.
- Options : (a) le socle commun (sommet d'étage paramétré pour plusieurs générations et pour la forme d'épreuve, rejeu, essai du bac) s'écrit d'abord et une fois, dans la v69 comme l'additif scellé le veut, AC-1 l'appelant sans le modifier ; le banc et la porte s'écrivent en même temps, à 0 USD ; **le premier allumage est la ligne 1 de cette course** ; le palier 1 s'allume ensuite sur le même socle, dès son préenregistrement court ; NA-1 sur l'autre file. Avantage : rien écrit deux fois ; cohérent avec D6 (a). Inconvénient : le socle est éprouvé d'abord par une forme d'épreuve neuve, non par la forme imposée déjà jouée. (b) le palier 1 s'allume d'abord, cette course ensuite : c'était l'option recommandée à la v1. Avantage : le socle est éprouvé sur la forme connue. Inconvénient : contredit D6 (a) ; ne vaut que si Lazar retient D6 (b). (c) le socle écrit pour cette course seule, le palier 1 le reprend plus tard. Avantage : suit la priorité à la lettre. Inconvénient : A69 à reprendre.
- Recommandation : (a), confiance 0,6. La v2 disait D5 « renforcée » : c'était faux, son option recommandée contredisait D6.
- Défaut sous 48 heures, **compté à partir de ce texte et non de celui de la v1** : (a), pour l'ordre des écritures seulement. Aucun allumage n'a de défaut.

**D7 — Le préenregistrement.**
- N2 et N3 en prennent une part : le texte des cartes de la v9 est celui de la porte (N3). Ce qui reste à décider ici : un préenregistrement neuf de la course pour les courses suivantes, à la place du v2 scellé qui écrit « pas de tests de mort » et « une seule génération », ou un additif à ce v2.
- Recommandation : un texte neuf, confiance 0,75 ; aucun défaut. Il n'est requis qu'au pas 5 de la note.

### 7.3 D8 — Le premier compte des cartes et leur passage aux traducteurs (nœud de Lazar)

- **Décision** : par quelle voie obtient-on le compte des cartes de la course v9 par nature (celles qui changent l'épreuve, une règle de l'orchestrateur, la conduite de modèles, celles hors gabarit), puis leur mise en forme fixe ?
- **Enjeu** : la note demande ce compte avant tout devis des cartes. Les cartes sont sous `archives-reponses-modeles/`. Les exceptions déjà accordées à ce dossier sont bornées : dans GO-2026-11-20-15 et GO-2026-11-20-28, **un agent neuf qui ne lit aucune carte** fait tourner un programme écrit ou contre-lu par la mère, qui ne rend que des identifiants, des comptes ou des noms de clés ; la mère n'y entre pas. Ce que la note demande va plus loin sur deux points, et je le dis :
  1. **Un compte de nature ne sort d'aucun programme seul** : dire qu'une carte change l'épreuve plutôt qu'une règle demande de lire son contenu.
  2. **Les deux traducteurs reçoivent chaque carte entière.** C'est une seconde lecture du même dossier, servie à des modèles de deux lignées, hors de la maison pour l'une au moins : **une seconde exception, et une dépense**.
- **Options.**
  - **(d) Un premier compte tiré des pièces déjà sur `main`, sans rouvrir le dossier.** Vérifié sur deux pièces, par leurs titres et leurs comptes seulement. La proposition `a2cd45ad…` range les 94 cartes : 2 exclues, 58 au plancher ou au-dessus en treize lignes après fusion, 34 sous le plancher. La lecture descriptive `0306adf7…`, l. 99, compte les modules nommés dans le champ `module_change` : treize modules, de 55 à 3 mentions, dont 42 pour les tests de mort, 34 pour les témoins plantés, 31 pour les proposeurs ; son § 4 regroupe les cartes. **Ce compte existe donc, à 0 USD, mais ce n'est pas celui de la note** : les mentions se recouvrent, « une mention n'est pas un changement », et aucune des deux pièces ne classe par barreau. Il sert de borne pour le devis de la ligne 2, pas de base pour passer une carte. Avantage : aucune exception, aucune dépense. Inconvénient : une borne, non un compte ; les cartes déjà sous un texte scellé restent à retrancher.
  - **(a) Le modèle accordé, étendu au moins possible.** Un agent neuf **qui ne lit aucune carte** fait tourner un programme contre-lu sur le fichier des cartes : il rend, par identifiant, les seules valeurs des champs fermés existants et la présence de mots d'une liste scellée d'avance dans `module_change`. Sorties : identifiants et comptes. La mère n'y entre pas. Avantage : reste dans le modèle de GO-15 et GO-28. Inconvénient : un compte par mots, plus fin que (d), encore loin d'un compte de nature.
  - **(b) Les deux traducteurs lisent les cartes entières** et rendent les fiches à champs fermés, à extrait cité vérifié par programme ; le compte de nature sort des fiches. Avantage : le seul compte que la note demande ; il sert aussi le pas 4. Inconvénient : seconde exception, plus large que toutes les précédentes ; dépense non chiffrée ; à ne demander qu'après la ligne 1 et sur un devis.
  - **(c) Ne passer aucune carte de la v9.** Avantage : rien ne s'ouvre. Inconvénient : **le premier emploi se réduit à la mesure sur les témoins** (ligne 1) ; la porte ne sert que les courses suivantes, donc E5 et E6 reviennent sur le chemin critique, avec N2, D7 et un texte neuf de la course ; aucune carte n'est éprouvée avant une génération neuve.
- **Recommandation** : (d) tout de suite, puis (a) avec le devis de la ligne 2, puis (b) seulement si Lazar l'accorde après la mesure ; confiance 0,6. La v2 recommandait un agent qui ouvre les cartes : je retire cette option, plus large que le modèle accordé.
- **Défaut** : aucun. (d) n'ouvre rien et ne dépense rien : c'est de la routine, et sa première lecture est faite ici ; un agent neuf peut la refaire en comptes propres sans mot de Lazar. (a), (b) et (c) sont le nœud : accès à un dossier fermé, ou dépense, ou abandon du premier emploi sur les cartes.

## 8. Le pilier mathématique

Sous la réserve de la mère sur PM et DM.

**Ce que ce plan lui emprunte.**
1. La règle stricte « une proposition qui meurt reste morte », avec la mort héritée par toute reformulation équivalente (PM, § 5, point 2 ; sa décision D-M5). **Proposition, adressée au rédacteur de C1, et que la note ne porte pas** : pour une carte d'auto-conception, tenir deux cartes de même fiche à champs fermés et de même greffon pour une seule tentative. Elle touche le compte des tentatives, et « même greffon » dépend de ce qu'écrit l'expérimentateur : à définir par empreinte du greffon scellé, ou à écarter.
2. Le tarif et la minuterie de sa machine à processeur (DM).
3. La forme « l'expérimentateur à modèle ne tue pas : mesuré, pas cru » (PM, § 5, point 3).

**Ce que ce plan lui doit** : le sommet d'étage paramétré (E1 et C3) ; C2 ; le module des graines et des clés, si la proposition du § 4.1 est retenue.

**Les trois écarts de la v2** entre le plan du pilier et la note sont exacts selon la contre-lecture. Deux sont traités par l'erratum 1 du plan du pilier (R-4431) : N6 prime, et l'empreinte des calculs est corrigée. Le troisième, les deux calendriers, attend le mot de Lazar sur l'ordre des pilotes.

## 9. Réserves du planificateur

1. **La note n'est pas contre-lue.** Deux de ses points sont à faire remonter à son auteur : le lieu du rejeu (§ 3.2) et la table des épreuves « dans le lanceur 11 » (§ 3.1).
2. **PM et DM** portent la réserve de la mère.
3. **Je n'ai ouvert** ni le relevé du lot 0 de NA-1, ni l'ordre v4 de « seuil et moniteurs », ni le mandat de ses mondes, ni la définition scellée, ni le banc de la ligne 1, ni le code du palier 0b, ni l'erratum du pilier. J'en tiens ce que disent le registre, la note et la contre-lecture.
4. **Des deux pièces de la course v9**, je n'ai lu que les titres, les lignes de compte et la ligne 99 ; aucun contenu de carte n'est repris ici. Je n'ai rien ouvert sous `archives-reponses-modeles/`.
5. **Les heures et les cas sont des estimations**, calculées à la main ; le nombre de témoins, les heures de mise au point et les durées maximales sont mes hypothèses.
6. **Le nombre de cartes déjà sous un texte scellé** ne m'est pas connu.

— planificateur du branchement de l'expérimentateur, modèle F
