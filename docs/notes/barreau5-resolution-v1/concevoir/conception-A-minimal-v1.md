# Barreau 5 — conception A, « le plus sûr avant l'entretien » (v1)

- Concepteur : Claude Fable 5.2, 19 novembre 2026. Rien lancé, rien dépensé, rien commis. Aucun refus d'outil.
- Sources : le socle `barreau5-comprendre/00-socle-des-faits.md` et ses notes 01 et 02. Seuls chiffres de résultat : ceux de l'apprentissage des sondes sur la tâche (étape B bis), déjà dans le socle.
- Simulation à loi inventée (aucune donnée du programme) : `barreau5-concevoir/puissance_conception_A_v1.py`, sortie `sortie-puissance-conception-A-v1.txt`.

## 0. Verdict en trois lignes

1. Le texte scellé de validité de l'adaptateur ne répond pas à ta question telle que le jury la posera : il ne vise que les sondes génériques, et la confusion mesurée est celle des sondes apprises sur la tâche. Je ne le joue pas en hâte ; je le garde intact et j'en sauve la seule pièce qui sert à tout, l'adaptateur honnête distillé.
2. Les scores fermés de l'étape B bis portent déjà, à 0 USD, un plan factoriel complet que personne n'a lu : état (adaptateur actif, modèle nu) croisé avec texte (saboteur, honnête), par action, sous la même sonde. Il contourne le plafond géométrique qui a rendu muette la différence « texte égal moins adaptateur seul ».
3. Ce plan a un défaut que j'ai trouvé en l'écrivant : son interaction est exactement confondue avec le chemin de calcul (deux cellules de l'ancien chemin, deux du neuf). Une relecture d'une demi-heure de carte, les quatre cellules par le même chemin, lève ce défaut. C'est la seule dépense que je recommande avant l'entretien.

## 1. Ce que le plan tranche, contraste par contraste

Notation : pour chaque dose, quatre groupes de 640 actions notés par la même sonde apprise — épisodes du saboteur sous son adaptateur ; textes honnêtes relus sous le même adaptateur ; textes du saboteur relus sous le modèle nu ; épisodes honnêtes sous le modèle nu.

| contraste | ce qu'il tient constant | rivale écartée | rivale qui reste |
|---|---|---|---|
| **A. Épisodes du saboteur contre textes honnêtes, sous le même adaptateur à la même dose** (jamais calculé) | l'adaptateur et sa dose | « la sonde ne lit que la présence de l'adaptateur » : sous cette rivale, l'aire vaut 0,5 | le texte ; l'adaptateur sur son propre texte contre un texte imposé ; le chemin de calcul |
| **B. Contraste A moins le même contraste sous le modèle nu** (textes du saboteur contre textes honnêtes, sans adaptateur) | en plus : ce que le texte seul donne à la sonde | « au-delà de l'adaptateur, elle ne lit que le texte » | propre texte contre texte imposé ; empreinte du réglage fin du mode « coût » ; chemin de calcul (confusion exacte, voir § 0.3) |
| **C. Tendance du score avec l'excès déclaré, dans les épisodes du saboteur à dose fixée** (tau de Kendall stratifié par tâche ; une seule série, donc à l'abri du chemin de calcul) | adaptateur, dose, tâche | présence de l'adaptateur | grandeur du nombre déclaré |
| **D. Tendance C moins la même tendance sur les mêmes textes relus sous le modèle nu**, et la tendance chez l'honnête | en plus : les jetons | grandeur du nombre lue dans le texte | un seul adaptateur |
| **E. Descriptifs sans seuil** : saboteur contre adaptateur témoin (épisodes, puis mêmes textes honnêtes en différence appariée) ; part de la direction de la sonde dans l'espace où écrivent les matrices de sortie de chaque adaptateur, comparée aux 800 directions du plancher ; norme des deux adaptateurs | — | rien : un contre un, intensités non égalisées | graine, données, intensité |

Le contraste « textes du saboteur sous le modèle nu contre l'honnête », lu comme soutien par un texte scellé et comme réserve par l'autre, devient ici un simple effet principal du texte : ni l'un ni l'autre. La question porte sur l'interaction.

**Ce que le plan ne tranche pas** : sabotage contre empreinte du réglage fin du mode « coût » (il faut l'adaptateur honnête distillé) ; la variabilité entre deux adaptateurs de même recette (unité expérimentale : un seul) ; un autre mode de sabotage ; les sondes génériques (objet du texte scellé).

## 2. Étapes dans l'ordre

| n° | étape | données | méthode | coût | durée | avant le 1er décembre ? |
|---|---|---|---|---|---|---|
| 0 | **Deux décisions prises avant toute lecture** (§ 5, nœuds 1 et 2) : sort des pièces payantes du texte scellé, fixé par une règle de date et non par un résultat | — | mot de Lazar | 0 | un jour | oui, et c'est la condition du reste : le texte scellé invalide toute pièce lancée « sur la foi d'une sortie » |
| 1 | **Lecture de l'aiguillage du texte scellé** par un agent autorisé : deux booléens, le nombre de sondes lues, rien d'autre | lecture scellée de l'étude des sondes génériques, branche du verdict | lecture de champs | 0 | une heure | oui (routine, cloisonnée) |
| 2 | **Texte neuf, court** : « validité de l'adaptateur pour les sondes apprises sur la tâche », à deux lectures déclarées d'avance (pas de piège de lecture unique) ; conçu par Fable, contre-lu par Opus | — | chaîne complète de classe décisive | 0 | 19 au 22 novembre | oui |
| 3 | **Lecture 1, au processeur** : contrastes A à E sur les scores fermés ; chaque ligne sous la sonde et sous sa jumelle du second ordre de calcul, une ligne n'est « tenue » que si les deux s'accordent | scores par action et poids de l'étape B bis ; colonne du coût jointe par clé ; fichiers des deux adaptateurs | aire de Mann-Whitney contre le plancher des 800 directions, rééchantillonnage des 64 tâches, niveau 99 % ; tau stratifié ; A et B rendus « sous réserve de chemin de calcul » aux doses 0,25 à 0,75 | 0 | code et contre-lecture 21-23, lecture 24, verdict par agent neuf 25 | oui |
| 4 | **Relecture homogène sur carte** : les quatre groupes, quatre doses, par le même chemin d'état imposé, notés par les sondes gardées ; puis **lecture 2** des contrastes A et B sans la réserve | adaptateurs, textes, poids des sondes ; code de relecture de l'étape B bis et fonction d'état imposé, existants | même programme de lecture | environ 0,5 heure de carte, 1 à 3 USD, plafond 5 | carte le 25 ou 26, lecture le 27 | oui si l'accord est donné à l'étape 0 ; sinon l'entretien se fait sur la lecture 1 |
| 5 | **Adaptateur honnête distillé**, pièce du texte scellé, jouée telle quelle si son code est inscrit avant le 25 novembre à 12:00Z ; sinon prolongation | recette scellée | texte scellé, sans écart de réglage | 8,5 à 12,5 USD, 7,5 heures | 25-26 novembre | incertain ; sa lecture, elle, est après l'entretien dans tous les cas |
| 6 | Relecture à texte constant du texte scellé, sa lecture unique, puis notation de l'adaptateur honnête par les sondes apprises (troisième lecture, texte neuf) | — | — | 2,5 à 4,6 USD, plus 1 à 3 | décembre | non |

**Le texte scellé peut-il être joué tel quel ?** Trois pièges, trois réponses. Lecture unique : je ne lis aucune de ses lignes gratuites avant ses deux courses ; ma lecture 1 n'ouvre aucun de ses fichiers. Aiguillage : inconnu jusqu'à l'étape 1 ; s'il ferme la lecture, le texte scellé est mort et la fabrication de l'adaptateur honnête passe sous le texte neuf (clause de repli à y écrire). Lancement tardif : addendum d'écart d'une page, qui déclare l'exposition du code aux verdicts lus et dit que le lancement applique tard la règle mécanique du 14 novembre, sans réglage changé.

## 3. Puissance des contrastes décisifs

Simulation : 64 tâches, 10 actions par épisode, corrélation de tâche 0,1 à 0,3 et d'épisode 0,1 à 0,5, plancher supposé à 0,56 (ceux de l'étape B bis vont de 0,52 à 0,57).

| contraste | plus petit effet détectable à 80 % | à comparer à |
|---|---|---|
| A (640 contre 640) | aire 0,62 à 0,68 au niveau 99 % ; 0,61 à 0,65 à 95 % | « dommage par action » déjà lu : 0,65 à 0,76 ; et un nul borne l'aire sous 0,60 à 0,65 environ |
| B (différence de deux aires) | 0,09 à 0,16 à 99 % | place disponible : 0,43 à 0,49 aux doses 0,25 et 0,5 (le texte y est presque muet), 0,12 à la dose 1. La différence lue par l'étape B bis n'avait que 0,001 à 0,075 de place |
| C (tau, 5 à 10 actions lisibles par tâche) | tau 0,13 à 0,19 à 99 % ; le texte scellé écrit 0,165 à 0,27 par une formule qu'il dit optimiste | corrélation de rang d'environ 0,2 : plus fin que le contraste en deux classes |
| D (différence de deux tau) | environ 0,15 à 0,25 (racine de deux fois C, moins l'appariement ; à chiffrer dans le texte) | — |

Limite dure : à la dose 1, B est marginal (place 0,12, seuil 0,09 à 0,16). Les doses 0,25 et 0,5 portent la décision, et ce sont celles que la réserve de chemin de calcul touche : d'où l'étape 4.

## 4. Ce que dit chaque issue

- **A non au-dessus du plancher, C non au-dessus** (issue que le nul du « dommage par action » rend plausible). « À adaptateur et dose fixés, la sonde apprise ne distingue pas les épisodes du saboteur de textes honnêtes relus sous le même adaptateur (aire au plus [borne haute]) et ne suit pas l'excès déclaré. Avec l'adaptateur seul à 0,93 à 0,999, ce que nous avons appris à lire est la présence de cet adaptateur, à cette puissance. La cause est de conception : l'étiquette d'apprentissage était confondue avec l'adaptateur. La sonde suivante s'apprend à adaptateur constant. » C'est une réponse ferme, et le jury peut la vérifier.
- **A au-dessus, B non.** « Sous adaptateur fixé, elle distingue le saboteur, mais pas plus que le texte seul ne le permet sans adaptateur : au-delà de l'adaptateur, elle lit le texte. »
- **A et B au-dessus (après la relecture homogène), ou C et D au-dessus.** « La présence de l'adaptateur n'explique pas toute la lecture : à adaptateur fixé, le score bouge avec l'épisode saboté au-delà du texte, ou croît avec l'excès au-delà des jetons. Non écarté : l'empreinte du réglage fin du mode "coût", l'adaptateur sur son propre texte, un seul adaptateur. Le contrôle qui l'écarterait est scellé depuis le 14 novembre et en fabrication. » Jamais « la sonde lit le sabotage ».
- **Sonde et jumelle du second ordre en désaccord** : « non tranché à cette dose, instabilité de l'apprentissage » (déjà connue à la dose 0,25).
- **Lecture 1 seule, sans la relecture homogène** : A et B dits « sous réserve de chemin de calcul » aux doses 0,25 à 0,75 ; un nul y reste lisible (un décalage de chemin qui annulerait pile un effet réel est peu plausible, à écrire tel quel), un positif ne l'est pas.

Validable hors de nous : texte scellé avant lecture, scores par action et programme publiés, tout se recalcule sur un portable ; le contraste « à adaptateur constant » a un précédent publié (« Caught in the Act », arXiv 2610.12445v1, p. 26, vérifié sur PDF par le critique), dont la figure d'appel porte elle-même la confusion que nous mesurons.

## 5. Nœuds de Lazar, propositions, routine

**Nœuds (arrêt, ton mot) :**
1. Texte neuf pour les sondes apprises : hypothèse de validité nouvelle, réemploi des scores fermés de l'étape B bis, sens du contraste « saboteur relu sous le modèle nu » (effet principal, ni soutien ni réserve). *Recommandation : oui ; confiance haute.*
2. À décider **avant** la lecture 1 : (a) adaptateur honnête joué sous le texte scellé si son code est inscrit avant le 25 novembre à 12:00Z, (b) prolongation de l'accord de 30 USD au 12 décembre pour le reste, (c) laisser échoir. *Recommandation : (a) avec (b) en filet ; confiance moyenne — le risque est le temps de code, que personne n'a compté.*
3. Rattacher la relecture homogène (plafond 5 USD) à l'accord de 30 USD, sous le texte neuf. *Recommandation : oui ; confiance haute, c'est le meilleur rapport du plan.*
4. Addendum d'écart au texte scellé (lancement tardif, exposition du code, script d'énumération des grilles s'il est introuvable).
5. Si l'aiguillage ferme la lecture : texte scellé abandonné, adaptateur honnête sous le texte neuf.
6. Phrase du dossier : elle ne peut dire plus que l'issue lue ; aucune revendication « comportement contre trace de l'adaptateur » (zone peu cherchée, règle anti-faux-trou).

**Proposer avec recommandation (défaut sous 48 heures)** : niveau 99 % par ligne, huit tests principaux ; règle « tenue seulement si les deux ordres de calcul s'accordent » ; descriptifs E sans seuil.

**Routine** : code de lecture et ses épreuves sur scores factices ; lecture de l'aiguillage par un agent autorisé ; versement des pièces absentes depuis la branche du quatrième compte ; calcul des normes d'adaptateur.
