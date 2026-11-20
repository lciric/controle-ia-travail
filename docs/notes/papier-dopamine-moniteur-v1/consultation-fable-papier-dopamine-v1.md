# Consultation — comment le programme peut se servir du papier « dopamine » (v1)

- **Date** : 20 novembre 2026, 11:51 UTC (relevée par `date -u`). **Auteur** : Claude Fable 5.2, sous-agent consulté sur le mandat ci-dessous. Pièce de classe C. Aucune dépense, aucun appel payant, aucun commit, aucune recherche en ligne. Rien lu sous les dossiers cloisonnés.
- **Papier** : Xu, Yuksekgonul, Zou, « Sparse Reward Subsystem in Large Language Models », arXiv 2602.00986v2, 11 mai 2026, prépublication non relue (p. 1). **Lu en entier, 25 pages** : texte extrait page par page ; pages 5, 7, 21, 24 et 25 relues en image pour les figures ; figures des pages 6, 20, 22 et 23 lues par leur légende et leurs axes seulement ; pages 10 à 17 (références), longues listes d'auteurs survolées.
- **Pages citées** : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 17, 19, 20, 21, 22, 23, 24, 25.

**Fichiers lus (sha256)**

| Fichier | Empreinte |
|---|---|
| `docs/notes/papier-dopamine-moniteur-v1/mandat-fable-papier-dopamine-v1.md` | `6ed83437efbae6a2748736c4534c6fb0f750acf93c074b6fd5cbc45aa3b4f53e` |
| `docs/sources/pdf/2602.00986v2.pdf` | `da004f53ff336b950bf51fb9a85fa424f5792579ac10dce45566ccb0e68e9039` |
| `CLAUDE.md` | `4689ca3e03da5a12379ba83b1da4d636b34cba30295e23fa0c462ca242f37683` |
| `docs/programme-controle-ia-v2.md` | `2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c` |
| `docs/etat-de-l-art-controle-ia-v1.md` (sections 0 à 6) | `a7d6846d14758c13639eccb2daeb47722085636a6601aa159e4132ab71d570ce` |
| `docs/notes/lecture-voisin-neuron-lens-v1.md` (sections 1, 5, 6) | `12c8f673e41411683b112d5a218a2a88d6493fb91a60338393134aba0bf2a44e` |
| `docs/notes/neuron-lens-v1/decision-entree-lentilles-programme-v1.md` | `6aaf54e7a701554dd8e05f495961b4ff2e97a58662072ee008d702f73bb5b4bd` |
| `docs/decisions/decision-N-026-v1.md` (bras « moyenne ») | `85bd40235f3668c66adffc2ff18139ff1a0c402f3aaa24cca70db0217f755bf0` |
| `docs/decisions/decision-N-029-v1.md` (référence boîte noire) | `084e30523c0a0349cb1daf0dcf804f6c9d38c10d4f8bceed23c787fa507f34e4` |
| `docs/decisions/decision-N-034-v1.md` (honnête sous revers) | `97e33e971a8fd01cdb8ff233f25dd9c0f1fd169e9889fca9a343ecd2aa3d5993` |
| `docs/decisions/decision-N-053-v1.md` (audit défensif) | `2204256d744288be2708578c0fdc8c44c62a29b70b2727ed7e31ec142d1cdeae` |
| `docs/decisions/decision-N-056-v1.md` (lignes sur les couches et les bases seulement) | `3592c1e977e8c38c0c883231d090d92cef4b7602fd91a9b303f9e5352ee46f2d` |
| `docs/decisions/decision-N-061-v1.md` (ressources publiques) | `b2ae441720665ed49f131e18fb7612d0d1c2a4e0cc7a0e18a301178fe5b2df54` |
| `docs/decisions/decision-N-063-v2.md` (base « mots et coût ») | `b2d9f03543802f82890c99eff77d4aab34ad532b50986b887c046906914b625b` |

Tout chiffre ci-dessous est une affirmation des auteurs, lue sur le PDF à la page citée ; aucun n'est une mesure du programme.

---

## Verdict

Le papier ne donne pas un moniteur de sabotage. Il donne une lecture interne de la **réussite que le modèle attend de lui-même**, et une lecture de la **surprise à chaque étape**. Mon jugement : cette lecture sert au programme d'abord comme **témoin de construit et base de comparaison** que toute sonde d'intention doit battre, ensuite comme **covariable** qui réduit le bruit des scores honnêtes, et seulement en troisième lieu, sous une hypothèse à tester, comme moniteur. L'habillage « neurones » et « parcimonie » ne sert pas. Confiance moyenne, de l'ordre de 60 %, tant que rien n'est mesuré sur notre modèle.

---

## Ce que le papier établit, et ce qu'il n'établit pas

**Ce qu'il fait.** Il entraîne un petit perceptron à deux couches sur l'état caché d'une couche pour prédire la réussite finale, par un objectif de différence temporelle (p. 3-4). Il élague ensuite les coordonnées d'entrée dont les poids ont la plus petite norme, et regarde si la prédiction tient (p. 4). Il appelle « neurones de valeur » les coordonnées qui restent. Il refait la même chose pour l'erreur de prédiction par paragraphe, estimée par des continuations tirées au hasard depuis chaque frontière de paragraphe, et appelle « neurones dopamine » les coordonnées retenues (p. 6).

**Ce qui tient à la lecture.**
- Avant toute génération, la prédiction de réussite est modeste : aire sous la courbe moyenne de 0,67 sur quatre modèles et deux jeux ; sur Llama-3.1-8B, notre modèle, 0,69 sur MATH500 et 0,66 sur ARC (tableau 3, p. 8).
- À la fin de la réponse, elle est meilleure : « mostly stable above 0.8 » sur Minerva Math, Llama-3.1-8B-Instruct compris (p. 24, figure 11 p. 25).
- La surprise par étape est lue faiblement : corrélation de rang entre 0,1 et 0,4 environ, irrégulière d'un taux d'élagage à l'autre (figure 4, p. 7, lue sur le graphique), sur deux modèles Qwen réglés par renforcement sur des mathématiques, un seul jeu (p. 7).

**Ce qui ne tient pas, ou pas encore.**
1. **« Moins de 1 % des neurones » n'est pas ce qui est mesuré.** La grille d'élagage s'arrête à 0,99 (tableau 8, p. 20) : le point le plus parcimonieux garde 1 %, pas moins.
2. **Concentré ou redondant ?** Le papier montre qu'un petit ensemble de coordonnées *suffit*. Il ne montre pas qu'un ensemble de même taille tiré au hasard, avec une sonde réentraînée, échoue. Ce témoin manque pour les courbes d'élagage ; le hasard n'apparaît que pour le recouvrement entre jeux (p. 5-6, p. 20) et pour l'ablation (p. 5). Or l'annexe A va contre la thèse : une sonde entraînée sur la seule récompense finale retient d'autres coordonnées, dont l'ablation fait beaucoup moins de dégâts (66,4 % contre 20,3 % d'exactitude en moyenne, tableau 5, p. 19). Deux sondes qui prédisent la même chose à partir de coordonnées différentes, c'est la signature d'une information répandue.
3. **L'ablation prouve la nécessité, pas la spécificité.** Mettre à zéro 1 % des coordonnées « de valeur » d'une couche fait tomber l'exactitude de 75,2 % à 20,3 % en moyenne, et à 1,2 % en couche 5 (tableau 2, p. 5). Les témoins sont le hasard, la norme des poids, Wanda et une sonde de prédiction du jeton suivant. Aucun n'est apparié sur la taille ou la variance des activations, la mise à zéro sort le modèle de son régime, et seule l'exactitude en mathématiques est mesurée. Un modèle qui s'effondre à 1,2 % est probablement cassé en général. Les auteurs citent eux-mêmes le travail sur les poids massifs (référence 35, p. 14).
4. **« Neurone » veut dire coordonnée de l'état caché** (« input dimension matches the dimensionality of the LLM's l-th layer hidden states », p. 3), alors que le témoin « norme des poids » vise la projection de sortie du perceptron du modèle (p. 5). L'objet n'est pas celui des catalogues de neurones.
5. **La surprise par étape repose sur peu.** Les étapes où la surprise est faible sont écartées à l'entraînement et à l'évaluation (seuil 0,3, p. 6) : la corrélation ne vaut que sur les grandes surprises. Le nombre de continuations par frontière n'est pas donné dans les réglages (p. 19-20). L'exemple montré est un seul neurone, le 1517 de la couche 5 (p. 7, 22, 24), alors que les courbes portent sur les couches 15 à 22 (p. 7). Le lien entre les deux familles de neurones est une figure, pour ce seul neurone, après ablation de 20 % et non de 1 % (p. 24).
6. **Le gain en recherche guidée est fragile.** 72,2 % sans guidage, 72,2 % au hasard, 77,8 % avec la sonde (tableau 4, p. 9), sur le sous-ensemble de validation, trois graines, sans intervalle ni effectif. Remarque d'arithmétique de ma part, pas un fait du papier : ces trois valeurs et celle de la base intermédiaire (75,0 %) sont des multiples de 1/36, pas de 1/300 ; si l'effectif est petit, l'écart tient à un ou deux problèmes.
7. **La lecture interne ne bat pas nettement le texte.** La seule longueur de la question atteint 0,62 en moyenne et dépasse la sonde sur le plus petit modèle ; sur Llama-3.1-8B et MATH500, demander sa confiance au modèle donne 0,69, autant que la sonde (tableau 3, p. 8). Le taux d'élagage retenu est « optimal », sans dire sur quelles données il est choisi (p. 8).
8. **Une seule graine** (p. 19-20). **Transfert entre modèles** limité à deux réglages de la même base (p. 6). **Aucune adresse de code** dans les 25 pages.
9. **Rien sur la surveillance.** Aucune occurrence de tromperie, de sabotage, de retenue volontaire ni d'adversaire, sauf l'appel final à étudier la robustesse « under adversarial settings » (p. 25). Les auteurs reconnaissent que la méthode exige un signal de récompense et n'a pas été essayée sur des tâches ouvertes (p. 25) : c'est exactement le terrain du programme, « flou à la relecture, vérifiable en aval ».

---

## (1) Ce qu'un expert ferait, et que tu ne demandes pas

1. **Poser la question de construit avant la question d'usage.** La valeur du papier est définie sous la politique du modèle lui-même : l'espérance de réussite s'il continue comme il fait (équation 1, p. 2). Pour un saboteur, cette espérance est basse *parce qu'il sabote*. Pour un honnête sur une tâche dure, elle est basse aussi. Une sonde de valeur risque donc de lire « ça va mal finir », pas « je le fais exprès ». L'expert écrirait trois prédictions concurrentes, avec leur signe, avant toute lecture :
   - *lecture de la difficulté* : avant génération, le score ne bouge pas avec la dose de sabotage ; pas de détection, mais une bonne covariable ;
   - *lecture de l'issue attendue* : le score baisse avec la dose, et baisse autant chez l'honnête en difficulté ; détection apparente, fausses alertes sur les tâches dures et sous revers (réserve « dérive de l'honnête sous revers », N-034) ;
   - *dissociation* : chez l'honnête, une erreur est une surprise négative (le creux de la figure 3, p. 7-8) ; chez le saboteur, le dommage est attendu, donc sans surprise. La signature d'intention serait alors « dommage sans surprise », et non un score élevé.
2. **Reproduire avant de construire.** Rejouer sur Llama-3.1-8B-Instruct un chiffre du tableau 3 et la lecture en fin de réponse. Sans cela, tout le reste est bâti sur une prépublication à une graine.
3. **Ajouter les témoins qui manquent au papier** : sous-ensemble aléatoire de même taille avec sonde réentraînée ; ablation par la moyenne et par rééchantillonnage ; témoin apparié en norme d'activation ; sonde linéaire à côté du perceptron ; plusieurs graines ; choix du taux d'élagage emboîté.
4. **Rendre l'instrument conforme au programme avant de le juger.** La sonde de surprise du papier normalise chaque coordonnée sur *toute* la réponse, puis fait la **moyenne** sur les jetons du paragraphe (p. 22). C'est doublement inutilisable chez nous : la moyenne sur les jetons est interdite en production (N-026), et une normalisation qui lit la fin de la réponse ne peut pas tourner en ligne. Il faut une variante à maximum ou à attention, normalisée sur un étalonnage honnête gelé, et garder la recette d'origine comme bras de diagnostic seulement.
5. **Séparer trois emplois** (moniteur, base, covariable) et écrire pour chacun le critère gelé qui le retient ou l'écarte.
6. **Chercher l'antériorité là où l'idée est séduisante** (R8) : la littérature sur la retenue volontaire de capacité est le lieu naturel de « le modèle sait qu'il peut, et ne fait pas ». Je ne l'ai pas cherchée.

## (2) Les données brutes dont il partirait

Pas les tableaux ni les courbes du papier, et pas nos scores de sondes déjà agrégés. Mais :

- **Les activations par jeton** de Llama-3.1-8B-Instruct, flux résiduel en sortie de bloc, aux couches du papier (2 à 4 pour la valeur, p. 4 ; milieu de réseau pour la surprise, p. 7) et aux couches du programme (7, 15, 23, N-056), à trois positions : fin de la consigne, chaque frontière d'action, fin de l'épisode. Sur des épisodes honnêtes, sur leurs jumeaux sabotés à chaque dose, et sur une famille d'organismes que la sonde n'a jamais vue.
- **Le texte brut de chaque action**, pour le prédicteur sur les traits du texte (N-029).
- **La vérité de l'issue**, par épisode et si possible par action : cibles semées, vérification différée, note de rubrique. C'est la « récompense » que la méthode exige.
- **Les continuations brutes** tirées depuis chaque frontière d'action, avec leur nombre et l'erreur type de l'estimation de valeur. Le papier ne donne pas ce nombre ; nous devons le fixer et le consigner.
- **Les jeux publics du papier** (MATH500, ARC, Minerva Math), avec des réponses régénérées par nous, puisque ni le code ni les activations des auteurs ne sont accessibles depuis le PDF.
- **Les poids des sondes et la liste des coordonnées retenues, par graine.**

À vérifier sur disque avant tout devis (R11) : si les activations par jeton des épisodes déjà joués existent aux bonnes couches et positions, une partie se fait sans processeur graphique. Les relire reste une lecture nouvelle, donc un préenregistrement (R1).

## (3) Les méthodes et les outils précis

- **Extraction** : crochets du harnais maison ou de TransformerLens sur la sortie de bloc ; numérotation des couches alignée sur celle des sondes existantes.
- **Sondes** : réplique exacte du papier pour la comparaison (perceptron à deux couches, 1024 unités cachées pour la valeur et 32 pour la surprise, AdamW, pas de 1e-4, 100 époques, facteur d'escompte 1 − 1e-5, p. 19), et, à côté, régression logistique et différence de moyennes, seules lisibles par une lentille. Objectif de différence temporelle contre régression sur l'issue finale (annexe A, p. 19).
- **Parcimonie** : chemin de régularisation L1 avec réentraînement après sélection, validation croisée emboîtée ; cent tirages de sous-ensembles aléatoires de même taille pour avoir une distribution nulle ; stabilité de la sélection entre graines, comparée au nul hypergéométrique que le papier dérive (p. 20).
- **Agrégation** : maximum sur les jetons de l'action ou sonde à attention ; jamais de moyenne hors bras de diagnostic nommé (N-026).
- **Mesure** : rappel à 1 % de faux positifs avec intervalle par rééchantillonnage des épisodes entiers ; plancher aléatoire apparié en covariance (programme, section 8.1) ; comparaison appariée aux bases ; lecture avec les positions porteuses d'évidence textuelle masquées (N-053, point 1).
- **Plan de construit** : honnête ou saboteur, croisé avec tâche facile ou dure ; jumeau honnête ; bras « revers » (N-034) ; dose-réponse.
- **Séquentiel** : le même processus à garantie toujours valide que pour les autres sondes, sur le score brut et sur le score dont on a retiré la part expliquée par la valeur attendue.
- **Lecture par lentille** : direction linéaire de la sonde de valeur lue par la lentille publique de Llama 3.1 8B Instruct, avec direction aléatoire appariée et artefact voulu (note de lecture, section 5, usage a1).
- **Graines** par `SeedSequence`, manifeste par course (R9).

## (4) Ce qui, hors de toi et de moi, vérifierait le résultat

1. **Un chiffre publié, rejoué sur des données publiques.** Sur Llama-3.1-8B et MATH500 : sonde 0,69, sonde linéaire de référence 0,64, confiance demandée 0,69, longueur de la question 0,63 (tableau 3, p. 8) ; en fin de réponse, plus de 0,8 sur Minerva Math (p. 24-25). Si notre chaîne ne retombe pas dans l'intervalle, c'est elle ou le papier qui est en cause, et on le sait avant d'avoir touché un épisode du programme.
2. **Une vérité plantée et un placebo.** La chaîne doit retrouver un signal que nous avons mis nous-mêmes, et rendre le hasard sur des issues permutées (R5).
3. **Des données tenues à l'écart** : famille d'organismes jamais vue par la sonde, tâches fraîches (N-049), jeu final lu une seule fois (N-050), et le mode de sabotage tenu à l'écart, que je ne connais pas et qui doit le rester.
4. **Des organismes construits par d'autres** : ceux de l'institut britannique sur la retenue volontaire (programme, section 7, famille iii) sont le cas public le plus proche de « peut et ne fait pas ». Le registre les dit disponibles à 70 milliards de paramètres seulement : changement de modèle, donc nœud.
5. **Des tiers dans la chaîne** : contre-lecture du préenregistrement par un autre modèle, verdict par un sous-agent neuf (R2, R13) ; le code des auteurs s'il est publié (les contacter est un nœud : je rédige, tu envoies) ; toute réplication indépendante du papier, que je n'ai pas cherchée.
6. **Le temps** : prédictions signées scellées avant lecture.

---

## Ta demande, reformulée

> Sur Llama-3.1-8B-Instruct et sur les épisodes du programme, la lecture interne de la réussite attendue et celle de la surprise par étape, telles que Xu, Yuksekgonul et Zou les définissent, apportent-elles, à 1 % de faux positifs, une détection du sabotage diffus au-delà de trois bases : le prédicteur sur les traits du texte, la confiance demandée au modèle, et nos sondes d'intention ? Lisent-elles l'intention de saboter, ou seulement l'échec attendu ? Répondre en partant des activations brutes et de la vérité de l'issue, après avoir rejoué sur notre modèle un chiffre publié du papier, avec des prédictions signées scellées avant lecture, un plancher aléatoire apparié, les témoins que le papier n'a pas, et une famille d'organismes tenue à l'écart. Dire, pour chacun des trois emplois possibles (moniteur, base de comparaison, covariable), s'il est retenu, sur quel critère gelé, et à quel coût.

---

## Réponse à la demande reformulée

### Ce qui sert comme base de comparaison — l'emploi que je recommande en premier

**Une « sonde de réussite attendue », entraînée sur des épisodes honnêtes seulement, sans aucun exemple de sabotage.** Elle a trois qualités que nos sondes d'intention n'ont pas ensemble.
- Elle respecte l'anti-circularité par construction (programme, section 7) : son étiquette est l'issue, pas le sabotage.
- Elle joue pour les sondes le rôle que la base « mots et coût » joue pour le texte (N-063) : si une sonde d'intention ne détecte pas mieux qu'elle, c'est que la sonde d'intention lit « ça se passe mal », et la revendication d'intention tombe. C'est un test direct de H8.
- Elle se compare à la confiance demandée au modèle, base boîte noire gratuite que le papier fournit lui-même et qui l'égale sur notre modèle (tableau 3, p. 8). Tant que la lecture interne ne bat pas la question posée, elle ne porte aucun gain de l'accès interne (H1).

### Ce qui sert comme covariable

**Retirer du score de chaque sonde la part expliquée par la réussite attendue.** La puissance du test séquentiel dépend de la variance des scores honnêtes (hypothèse (c) du lemme, programme, section 3). La difficulté de la tâche est une source évidente de cette variance. Si la sonde de valeur la capte, la soustraire resserre les scores honnêtes et augmente le rappel à faux positifs égaux, sans rien demander au saboteur. C'est aussi une parade à la dérive de l'honnête sous revers. Prédiction à sceller : la variance honnête baisse ; si elle ne baisse pas, l'emploi est abandonné.

### Ce qui pourrait servir comme moniteur boîte blanche, sous condition

1. **La dissociation « dommage sans surprise ».** C'est la seule voie par laquelle ce papier peut toucher l'intention. Elle a un défaut de fond : il faut connaître le dommage pour constater l'absence de surprise, donc elle sert à l'audit, après coup, pour trier l'erreur de l'intention, et pas comme alarme en ligne. Elle s'appuie en outre sur la partie la plus faible du papier (corrélation de 0,1 à 0,4, modèles réglés par renforcement, jamais Llama). Je la classe en bras exploratoire.
2. **Le score de valeur brut comme trait de plus** dans le panel de sondes, à côté des concepts existants. Emploi légitime seulement si la lecture « issue attendue » se confirme *et* si le trait survit au plan honnête ou saboteur croisé avec facile ou dur. Je m'attends à ce qu'il n'y survive pas.
3. **Avertissement sur les couches 2 à 4.** À cette profondeur, à la dernière position de la consigne, une sonde lit surtout la surface de la question, et le papier montre que la longueur seule fait presque aussi bien (p. 8). Un tel trait est une base boîte noire déguisée. Il doit passer la lecture à positions masquées avant d'être appelé interne.

### Un emploi hors moniteur que le papier suggère sans le voir

**Les continuations tirées depuis chaque frontière d'action comme mesure du dommage par action.** La différence entre la valeur estimée sous la politique honnête et sous la politique de l'organisme, au même préfixe, chiffre ce que chaque action sabotée coûte. C'est la quantité que le lemme appelle budget de sabotage, et dont l'expérience E1.3 a besoin quand la fragmentation varie. Ce n'est pas un moniteur, c'est un instrument de vérité, et il est cher : un lot de continuations par action et par épisode. Sur devis seulement, et seulement si la vérité de l'issue se calcule par programme sur une continuation.

### La jonction avec la lecture par lentille neuronale

Ta directive demande aussi la lentille parmi les moniteurs. La note de lecture du 13 novembre conclut qu'elle est un instrument d'audit, pas un moniteur, et je ne vois rien dans ce papier qui change cela. La jonction utile est celle-ci : lire par la lentille la direction linéaire de la sonde de réussite attendue. Si elle « fait dire » des mots de difficulté ou de format, la sonde lit la surface ; sinon, on a un soupçon de moins, sans blanchiment. Deux précautions : le perceptron du papier n'a pas de direction unique, il faut la variante linéaire ; et les « neurones » du papier sont des coordonnées du flux, pas les neurones des catalogues, dont les descriptions publiques ne s'appliquent donc pas.

### Ce qui ne sert pas

- **La thèse de parcimonie et le vocabulaire « neurones de valeur », « neurones dopamine ».** Non établie contre la lecture redondante, et sans valeur de sécurité : une sonde qui lit peu de coordonnées n'est pas plus robuste, elle offre une cible plus étroite.
- **La sonde de surprise telle que publiée** : moyenne sur les jetons et normalisation sur la réponse entière (p. 22).
- **Le guidage de la génération par la sonde** (p. 8-9). Chez nous, ce serait faire entrer un score de moniteur dans la sélection des actions de l'agent : interdit par l'invariant de N-053, point 5, hors bras d'attaque déclaré.
- **Le neurone 1517 de la couche 5 et tout indice de coordonnée** : ils appartiennent à un modèle Qwen réglé par renforcement.
- **Les chiffres d'ablation comme preuve de spécificité**, et l'analogie avec les neurosciences comme argument.

### Limites du papier qui pèsent sur nous

Signal de récompense binaire et vérifiable exigé, tâches ouvertes non essayées (p. 25) ; preuve de la surprise par étape absente sur Llama ; une graine ; aucun adversaire ; aucun code ; lecture avant génération à peine au-dessus du texte. Ce sont des limites de ce papier, pas des trous du champ (R8).

### Risques d'antériorité et de collision

- **Zone revendiquée trouvée occupée : aucune**, sur les 25 pages. Le papier ne traite ni surveillance, ni sabotage, ni agrégation séquentielle, ni corruption du moniteur.
- **Voisins à lire avant toute phrase du type « la valeur interne détecte la retenue »** : la sonde linéaire de réussite sur la question seule (référence 9, arXiv 2509.10625, p. 10) ; la difficulté perçue lue dans les états cachés (référence 51, arXiv 2509.12886, p. 17) ; les neurones associés aux hallucinations (référence 18, arXiv 2512.01797, p. 11) ; les récompenses tirées des états cachés (référence 23, arXiv 2505.12225, p. 13) ; les sondes parcimonieuses sur neurones (référence 24, p. 13-14). Aucun n'est dans l'état de l'art v1. Côté contrôle, le gain de l'accès interne sur la retenue volontaire et les jeux d'audit de l'institut britannique y sont déjà (état de l'art, section 2.1, niveau transcription) : la dissociation « sait mais ne fait pas » y est probablement explorée. C'est une question à vérifier sur PDF, pas une zone libre.
- **« Le score de sonde comme série temporelle »** est déjà dans les revendications interdites (état de l'art, section 5) ; la surprise par étape en est un cas de plus, à citer.
- **Papier C.** Les auteurs notent qu'on pourrait supprimer ou amplifier ces signaux pour contourner des mécanismes de sécurité (p. 25). Pour nous, c'est une question de mesure défensive à ranger sous la taxe de déplacement (HC4) : le déplacement d'une sonde parcimonieuse coûte-t-il moins que celui d'une sonde dense ? Je ne détaille pas plus.
- **Collision interne** : ajouter cette sonde à une liste scellée, lire d'autres couches que 7, 15 et 23, ou toucher les épisodes déjà joués sans texte nouveau, sont des nœuds (N-061, point 4 ; N-056 ; R1).

---

## Décision à te poser

**Décision : faire entrer la lecture de la réussite attendue dans le programme, et à quel titre.**
- **Enjeu** : un témoin de construit de plus pour H8 et un gain possible de puissance, contre un chantier de plus alors que trois sont actifs.
- **Option a — base et covariable, en bras rapporté.** Rejouer d'abord un chiffre du papier sur notre modèle ; puis une sonde de réussite attendue sur épisodes honnêtes, comme base que les sondes d'intention doivent battre et comme covariable ; lecture de sa direction par la lentille publique. Elle ne sert pas de critère et n'entre dans aucune liste scellée. Avantage : sert la question du programme, coût faible, se range sous le chantier « saboteur et sondes, lentilles comprises ». Inconvénient : des passages du modèle, donc un devis.
- **Option b — a, plus le bras exploratoire « dommage sans surprise » et la mesure du dommage par continuations.** Avantage : seule voie vers l'intention, et un instrument pour le lemme. Inconvénient : cher, appuyé sur la partie la plus faible du papier.
- **Option c — citer seulement.** Le papier entre à la veille comme voisin lu ; rien n'est construit. Avantage : aucun coût. Inconvénient : ta directive du 20 novembre n'est pas suivie.
- **Recommandation : a**, confiance moyenne. Je ne recommande pas d'en faire un moniteur revendiqué avant que le plan honnête ou saboteur croisé avec facile ou dur ait parlé.
- **Défaut sous 48 heures** : c.

Dans tous les cas : préenregistrement conçu, contre-lu par un autre modèle, scellé avant toute lecture ; devis avant tout calcul.

## Ce que je n'ai pas fait

- Aucune recherche d'antériorité en ligne : les voisins ci-dessus viennent de la bibliographie du papier et de l'état de l'art v1.
- Aucune vérification sur disque de ce que le harnais journalise (couches, positions) : la part faisable sans processeur graphique reste à établir.
- Les figures des pages 6, 20, 22 et 23 n'ont pas été relues en image.
- La décision N-056 n'a été lue que par ses lignes sur les couches et les bases, pour ne rien apprendre du mode tenu à l'écart.
