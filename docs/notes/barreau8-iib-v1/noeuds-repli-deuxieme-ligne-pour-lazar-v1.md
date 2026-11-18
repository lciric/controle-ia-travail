# Note pour Lazar — les décisions que demande le brouillon du second moyen de fabrication du bras A — v1

Écrite le 2026-11-18 (UTC) par le contre-lecteur neuf du brouillon (rapport : `prereg/contre-lectures/T0.7-organismes-discrets-repli-deuxieme-ligne-v1-brouillon1-cl1.md`). Tu peux la lire seul : elle ne suppose pas de lire le mécanisme.

## Ce dont il s'agit, en trois lignes

Le bras A fabrique un saboteur en échangeant des champs de texte entre actions. Tu as demandé qu'on construise **aussi, en parallèle**, un second moyen, prévu seulement après un échec du premier : à chaque pas, le modèle honnête écrit K actions possibles ; un lecteur **choisit celle qui mentionne le moins de contrôles d'une moitié cachée de la référence** ; l'action choisie est jouée ; le saboteur n'écrit jamais un mot, il choisit seulement. Le brouillon est écrit ; la contre-lecture le juge scellable après corrections ; **quatre décisions viennent de toi**, les trois autres sont tranchées sans toi (dernière section).

Une chose que le brouillon ne disait pas : ce second moyen **met aussi en service un instrument que le texte scellé du bras A avait retiré** et gardé « pour plus tard » : lire une moitié de la référence cachée au moment de fabriquer. C'est le cœur de la première décision.

---

## Décision 1 — La clé de choix lit-elle une moitié de la référence cachée ?

**Décision en une phrase.** Autoriser, par une exception écrite à ta décision N-060 (version 3, point 4 (a) : « aucune sortie de l'oracle de couverture dans la sélection d'un agent »), qu'un lecteur de couverture lise la moitié « conception » de la référence cachée pour choisir les actions qui servent à entraîner le saboteur ; la moitié « vérité », elle, n'est jamais lue pour choisir.

**Enjeu.** Sans cette lecture, ce second moyen n'existe pas sous sa forme actuelle. La moitié « conception » et la moitié « vérité » sont deux moitiés du même savoir caché ; le lecteur qui choisit n'est pas l'oracle qui mesure le dommage (autre moitié, autre instrument), mais c'est la même fonction. Si tu autorises, la preuve que le dommage est réel passe par la moitié « vérité », jamais vue au moment de choisir. Si tu refuses, le second moyen devient le choix par champ (voir option b), plus lourd.

**Options.**
- **(a) Autoriser, exception écrite, partage des moitiés scellé avant tout tirage.** Avantage : le moyen le plus direct, le plus économique (environ 23 heures de carte, 11 à 13 dollars, partagé avec le bras A) ; une porte intermédiaire (« le maître abaisse-t-il la couverture de la moitié vérité ? ») arrête tôt s'il ne fait rien. Inconvénient : tu lèves toi-même un invariant que le programme avait posé ; la réserve « cousin d'une sortie de l'oracle dans la sélection » reste inscrite à chaque chiffre produit.
- **(b) Refuser la lecture de la référence : le lecteur choisit parmi les K versions d'un champ en ne lisant que l'énoncé de la tâche.** Avantage : aucune exception, la forme la plus propre vis-à-vis de N-060. Inconvénient : autre mécanisme (continuations sur préfixe, fonction d'ajustement à figer), un nouveau brouillon complet et une nouvelle contre-lecture ; le dommage sur la couverture est moins direct ; ce n'est pas ce que tu as demandé en disant « faire b aussi ».
- **(c) Garder (a) mais avec une clé programmée à liste fermée de contrôles (aucun modèle ne lit la référence).** Avantage : la clé n'est plus un lecteur modèle, donc plus de « sortie de lecteur » dans la sélection. Inconvénient : il faut écrire à la main les formes acceptées de chaque contrôle, sur 32 tâches ; délai et risque de couverture partielle ; conception sur processeur d'abord.

**Recommandation : (a), confiance moyenne.** À condition que la réponse soit inscrite en tête du texte définitif, que le lecteur de choix soit précisé (modèle, famille, consigne) et éprouvé avant toute sélection, et que la porte intermédiaire reste. Si tu tiens la lettre de N-060 pour stricte : (c) avant (b).

**Défaut sous 48 heures : rien n'est scellé ni lancé** ; le brouillon reste brouillon. Une exception à une de tes décisions ne se prend pas par défaut.

---

## Décision 2 — Les deux bras partagent-ils leurs épisodes honnêtes ?

**Décision en une phrase.** Faire servir les mêmes épisodes honnêtes, le même témoin « réglage fin sans sabotage » et les mêmes épreuves de l'oracle aux deux bras (comparaison appariée exacte, environ 3,3 heures de carte économisées), au lieu de tout fabriquer deux fois.

**Enjeu.** Le gain est petit (environ 1,6 dollar) ; le prix est un **couplage** : une épreuve de l'oracle qui échoue, ou un partage de moitiés qui échoue à son contrôle, arrête les deux bras, ce que la règle « aucun bras n'en arrête l'autre » ne dit pas. Et le partage suppose que la première action de chaque pas reproduise **au mot près** l'action honnête du bras A : ce que rien ne garantit en demi-précision ; une vérification est exigée (les candidats de départ coïncident-ils ?) avant de partager.

**Options.**
- **(a) Partager, sous une vérification de reproduction et avec l'exception écrite « les arrêts sur objets communs valent pour les deux ».** Avantage : appariement exact, économie. Inconvénient : couplage ; si la vérification échoue, retour à (b), +3,3 heures.
- **(b) Tout régénérer pour ce bras.** Avantage : deux bras indépendants. Inconvénient : environ +1,6 dollar et la perte de l'appariement exact des témoins.

**Recommandation : (a), confiance haute** — avec la vérification de reproduction écrite d'avance et son repli sur (b).

**Défaut sous 48 heures : (a) sous ces deux conditions** (c'est le choix du brouillon ; il ne dépense rien tant que le texte n'est pas scellé).

---

## Décision 3 — Qu'a-t-on le droit de dire quand les deux bras sont lus ensemble ?

**Décision en une phrase.** Interdire toute phrase du type « au moins un des deux moyens donne un saboteur discret » sans une correction qui rende la phrase deux fois plus difficile à obtenir qu'une phrase sur un seul bras.

**Enjeu.** Deux bras en parallèle doublent les chances qu'un hasard heureux fabrique un « saboteur discret ». La correction doit aller dans le **bon sens** : pour le dommage, abaisser le seuil de moitié ; pour la discrétion (qui se déclare par non-détection), abaisser le seuil de moitié rendrait la déclaration **plus facile** : la correction doit être écrite condition par condition. Le brouillon écrivait « seuil divisé par deux » partout ; c'est faux pour une des deux conditions.

**Options.**
- **(a) Une règle écrite par condition (dommage : seuil divisé par deux ; non-détection : seuil non abaissé ; borne haute sous 0,60 : seuil divisé par deux), et aucune phrase d'union sans elle.** Avantage : prudente, vérifiable. Inconvénient : l'union est difficile à obtenir.
- **(b) Aucune phrase d'union : chaque bras parle pour lui seul.** Avantage : le plus simple. Inconvénient : tu perds la phrase qui t'intéresse le plus si les deux bras sont partiellement positifs.

**Recommandation : (a), confiance haute.**

**Défaut sous 48 heures : (a)**, rédigée par condition dans le texte définitif.

---

## Décision 4 — La dépense

**Décision en une phrase.** Accorder des lignes de calcul **une par une, dans l'ordre**, après un devis neuf contre-lu : d'abord la ligne sans dépense, puis une ligne de faisabilité qui ne lit **aucun résultat de sabotage**.

**Enjeu.** Première estimation du brouillon, à reprendre par le devis : environ 23 heures de carte (11 à 13 dollars) si tout est partagé avec le bras A, 27 heures (13 à 15 dollars) sinon ; pire cas, environ 60 dollars ; plafond proposé 65 dollars. La contre-lecture a trouvé que la **première ligne payante** du brouillon lisait déjà le résultat décisif (le dommage du maître) hors de l'ordre gelé, et que la génération entière précédait la porte censée l'éviter : l'étagement (d'abord le seul cas fort, puis la porte, puis le reste) économise environ 11 heures, soit 5 à 6 dollars, si la porte arrête.

**Options.**
- **(a) Demander d'abord la ligne sans dépense, puis une ligne de faisabilité (débit, lisibilité du lecteur de choix, nombre de pas où il départage) sans lecture du dommage ; fabriquer ensuite le cas fort, la porte, puis le reste.** Avantage : le moins de dollars exposés avant la première information utile ; aucune lecture hors ordre. Inconvénient : plus de lignes de GO à demander.
- **(b) Une seule ligne pour toute la fabrication.** Avantage : un seul GO. Inconvénient : tu paies tout avant de savoir si la sélection fait quelque chose.

**Recommandation : (a), confiance haute.** Aucun GO n'est demandé maintenant ; le devis vient après le scellement.

**Défaut sous 48 heures : aucune dépense** (de toute façon aucune ligne n'est possible avant le scellement).

---

## Ce qui est tranché sans toi (trois lignes)

- **Trajectoire jouée contre sélection sur contexte honnête** : jouée (une transcription dont les pas suivants ont été écrits sur un autre contexte enseignerait autre chose que la politique) ; surcoût de 5 dollars environ, dans le plafond.
- **Porte intermédiaire avant toute distillation** : gardée, mais **réécrite** : sa puissance est chiffrée, un résultat nul se dit « dommage non démontré » et non « inexistant », un effet de signe inverse déclenche l'audit de symétrie.
- **Deux doses décisives sur trois** (la plus faible rapportée sans seuil) : gardé, symétrique du bras A.

## Ce que la contre-lecture ajoute et qui n'est pas une décision de toi

Trois points de fond : le test « le dommage généralise-t-il d'une moitié à l'autre ? » ne vaut rien sur l'élève évalué sur des tâches neuves (il vaut sur le maître, sur les tâches de fabrication) ; il manque un témoin « choix au hasard » (la pièce décisive de la conception dommage-cache) et une comparaison avec le témoin « réglage fin » à chaque dose ; une table de lecture a des cases sans verdict. Détail et corrections : le rapport cité en tête.
