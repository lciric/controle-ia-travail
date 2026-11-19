# Barreau 5 — conception C, « la validation hors de nous » (version 1)

- Rédigée le 2026-11-19 par un sous-agent concepteur (Claude Fable 5.2). Rien lancé sur carte, rien dépensé, rien commis. Je n'ai pas lu les conceptions A et B.
- Sources : le socle `…/barreau5-comprendre/00-socle-des-faits.md` et ses notes 02, 03, 05, 06 ; l'extrait du PDF versé `docs/sources/pdf/2610.12445v1.pdf` (« Caught in the Act », pages 9 et 26). Aucune valeur de résultat hors de l'apprentissage des sondes sur la tâche (étape B bis).
- Chiffres de puissance : `…/barreau5-concevoir/simulation-puissance-C-externe-v1.py` et `sortie-simulation-puissance-C-externe-v1.json` (loi inventée, aucune donnée du programme, graines par `SeedSequence`). Les coûts sont des ordres de grandeur tirés du socle, à refaire en devis.

## 0. La thèse de cette conception

Dans l'organisme à adaptateur, « un adaptateur est actif » et « la disposition à saboter est active » sont **la même variable par construction** : l'adaptateur imite toutes les actions du saboteur instruit, gonflées ou non. Aucun contraste pris à l'intérieur de cet organisme ne peut donc séparer la disposition de l'adaptateur. Le contraste « actions gonflées contre non gonflées » ne lit que l'**acte**, et une sonde de disposition parfaite y donnerait 0,5.

Il faut donc un plan à quatre cases, adaptateur présent ou absent, sabotage présent ou absent, avec plusieurs réalisations indépendantes par case. Trois cases existent. La quatrième, « adaptateur présent, aucun sabotage », n'a qu'un substitut : l'adaptateur témoin distillé d'une consigne bénigne, à la dose 1, sans intensité mesurée.

Un tiers n'acceptera la réponse que si quatre conditions tiennent :
1. la méthode a retrouvé une vérité plantée qu'elle ne connaissait pas ;
2. l'unité de la comparaison est l'adaptateur, et non l'action ;
3. un contraste à poids constants existe ;
4. le calcul est refait par une autre main sur une autre pile.

**Le banc actuel est valide pour borner la spécificité** : « un adaptateur sans sabotage allume la sonde » est déjà établi. **Il n'est pas valide, seul, pour conclure « la sonde lit le sabotage »**.

## 1. Ce que le plan tranche, contraste par contraste

| contraste | ce qu'il garde constant | explication rivale écartée | ce qu'il ne tranche pas |
|---|---|---|---|
| **K1.** Organisme contre épisodes de l'adaptateur témoin, sous la sonde apprise ; textes honnêtes relus sous l'adaptateur saboteur contre les mêmes sous le témoin, appariés par action (scores fermés, processeur) | un adaptateur des deux côtés ; le texte dans la version appariée | « n'importe quel adaptateur donne le même score » | l'intensité (témoin non remis à l'intensité du saboteur), la graine et les données de distillation (un adaptateur contre un) |
| **K2.** Saboteur instruit contre témoin instruit, sous le modèle nu, lus par la sonde apprise sur l'adaptateur ; variante à texte égal : mêmes jetons, seule la ligne de consigne change (relecture sur carte) | les poids (aucun adaptateur), la présence d'une consigne, le texte dans la variante | « la sonde ne lit que la trace de l'adaptateur », « elle lit la présence d'une consigne » | la part de la séparation sur l'organisme due au sabotage (existence, non proportion) ; le régime de consigne (Kumar, 2605.27958) reste une réserve |
| **K3.** K adaptateurs saboteurs contre K adaptateurs distillés de l'honnête, même recette, graines différentes, comparés à **intensité mesurée égale** (courbe « score en fonction de l'intensité » sur les témoins à quatre doses) ; la sonde n'est jamais jugée sur l'adaptateur qui l'a apprise | la recette, le rang, l'intensité ; la graine est moyennée | la graine, l'intensité, la trace générique du réglage fin (2609.36490, p. 6-7) | le texte en génération libre (d'où la version à texte constant) ; un seul mode de sabotage |
| **K4.** Intervention sans entraînement : retirer la direction de la sonde chez le saboteur, l'ajouter chez l'honnête à norme égale à celle du déplacement de l'adaptateur, génération libre, placebo de même norme | les poids, la tâche | « lisible donc lié causalement » (2610.22460 p. 8 ; 2607.25907, PDF non versé) | une sonde non linéaire ; un attaquant qui s'entraîne |
| **K5.** Organismes d'autrui à contraste interne : dénégation de son but propre contre dénégation honnête d'autres buts, **dans le même adaptateur** (2610.12445, p. 26, table 10) ; bascule par une ligne de consigne à poids constants (bird-labs : 0,997 contre 0,745, p. 9 et 26) | l'adaptateur, par construction d'une autre équipe | « notre méthode ne marche que sur notre organisme » ; biais de fabrication maison | rien sur notre mode (le coût gonflé) ni sur Llama-3.1-8B : c'est une validation de la **méthode** |
| **K6.** Organisme où le sabotage varie à poids constants, par une variable connue de l'oracle (saboteur à budget, bras A) | les poids, la graine, l'intensité | toutes les rivales liées à l'adaptateur | dépend d'une conception que je n'ai pas le droit de lire (§ 5, nœud 6) |

## 2. Les étapes, dans l'ordre

**Étape 1 — Épreuve à vérité connue de la règle de lecture.** Processeur, 0 USD, 1 à 2 jours de code et de contre-lecture. *Tient avant l'entretien.* Classe B, routine.
- Un générateur d'activations à loi inventée plante, au choix : une direction liée à l'adaptateur seul ; une direction liée à l'acte ; une direction liée à la disposition ; et deux pièges, un témoin d'intensité plus faible et l'adaptateur d'apprentissage laissé dans la comparaison.
- Le code de lecture des étapes 2 et 4, **le même fichier, même empreinte**, rend son verdict sans connaître le monde.
- Forme vérifiable par un tiers : le tiers tire lui-même le monde et la graine, garde l'empreinte de la vérité, reçoit le verdict, puis révèle.
- Double programmation : le code est réécrit par l'autre modèle (Opus 5.5) à partir du seul texte, et les deux doivent s'accorder à 10⁻⁶ près sur les scores fermés.

**Étape 2 — Lecture à quatre cases sur les scores fermés de l'étape B bis (K1).** Processeur, 0 USD, une demi-journée après scellement. *Tient avant l'entretien si le texte neuf est scellé vers le 24-25 novembre.* **Nœud** : réemploi de données versées et texte neuf (§ 5, nœud 1).
- Données : `origin/donnees/t07-etape-b-bis-v2`, groupes déjà notés (organisme, épisodes du témoin, textes honnêtes sous chaque adaptateur), colonne `cout` de `mesures-t06.npz` jointe par la clé.
- Méthode : aire et différence appariée par action, rééchantillonnage des tâches, niveau 99 % ; les deux ordres de calcul ; tendance du score avec l'excès déclaré.
- Géométrie, sur les poids seuls : part de la norme des poids de la sonde linéaire dans l'espace écrit par les matrices de sortie de l'attention de chaque adaptateur, contre des sous-espaces aléatoires de même rang.

**Étape 3 — Relecture sur une autre pile, groupes manquants, intensité (K2).** Carte, environ 1 heure, 2,5 à 4,6 USD (ordre du texte scellé pour une relecture sur instance à part). *Tient avant l'entretien si le GO vient avec l'étape 2.* **Nœud de dépense.**
- Autre pile : bibliothèque publique d'adaptateurs avec poids fusionnés, simple précision, autre type de carte. Elle rejoue les groupes de l'étape B bis par les sondes gardées. C'est la réponse à deux réserves : l'égalité des chemins de calcul comparée sur 8 épisodes sur 64, et la dose 0,25 instable (0,9357 contre 0,7929 selon l'ordre de calcul).
- Groupes neufs : témoin instruit et saboteur instruit sous les sondes de chaque dose, puis la variante à texte égal.
- Intensité : divergence de Kullback-Leibler et norme du déplacement à la couche lue, pour le saboteur aux quatre doses et pour le témoin.
- Les activations sont gardées et versées cette fois.

**Étape 4 — L'adaptateur comme unité (K3).** Carte, environ 25 à 40 USD pour 4 témoins distillés de l'honnête et 3 saboteurs de plus (extrapolé de 8,5 à 12,5 USD par témoin à quatre doses ; devis à faire), 1 à 2 jours en parallèle. *Ne tient pas avant l'entretien avec une marge honnête* : une forme réduite à 2 contre 2 n'a aucune puissance (§ 3). **Nœud de dépense et d'énoncé** : il touche la définition du témoin apparié de G1, brouillon N-074.
- Second volet : réapprendre la sonde avec des exemples « adaptateur actif, étiquette 0 » (décorrélation à l'apprentissage, Devbunova 2603.19426, PDF non versé), jugée sur des adaptateurs jamais vus.

**Étape 5 — Intervention sans entraînement (K4).** Carte, 4 conditions de 64 épisodes à environ 0,7 heure chacune, soit environ 3 heures et 3 à 5 USD. Après l'entretien, ou avec l'étape 3 si Lazar le veut. Elle respecte l'invariant « aucun score de moniteur dans l'entraînement de l'agent ».

**Étape 6 — Hors de nous au sens fort.** Après l'entretien, sur devis ; trois nœuds lourds.
- (a) Rejouer la règle sur les sept organismes publiés par l'institut britannique de sécurité de l'IA. Poids annoncés publics par la référence Cooney et al. 2606.12618, connue par citation seulement : **non vérifiée sur PDF**, licence et disponibilité des questions d'interrogatoire inconnues. Qwen3.6-27B demande une carte de 80 Go.
- (b) Attaquant informé par entraînement : un adaptateur honnête qui allume la sonde, un saboteur qui l'éteint. Cela bute sur l'invariant de N-053 ; à ranger dans le bras d'attaque de N-056.
- (c) Même recette sur une autre lignée de modèle de même taille.

**Avant l'entretien, sans rien lancer.** Citer 2610.12445 : le contraste à adaptateur constant est publié et faisable (p. 26), et la figure de tête de cet article porte elle-même la confusion (p. 1, deux organismes différents). Ne pas écrire que la séparation « comportement contre trace » est libre : zone peu cherchée, règle R8.

## 3. Puissance des contrastes décisifs

- **K1 et K2 (640 actions contre 640, 64 tâches).** Borne basse à 99 % au-dessus de 0,5, rééchantillonnage des tâches.
  - Tâches appariées : une aire de 0,55 est détectée dans 75 à 99 % des cas selon la corrélation dans la tâche (0 à 0,6) ; 0,57 dans 98 % et plus.
  - Tâches non appariées, corrélation 0,3 : il faut 0,60 pour 80 %.
  - La formule du socle (écart-type 0,019179, facteur relevé sur ses lignes) donne 0,59 à 95 % avec le plancher des directions aléatoires.
  - C'est trois à cinq fois plus fin que le contraste « gonflées contre non gonflées » (0,65 à 0,76).
- **K3 (permutation exacte, unité = adaptateur).** L'écart est compté en écarts-types entre graines.
  - 2 contre 2 : niveau le plus bas 0,167, puissance nulle à 5 %.
  - 3 contre 3 : niveau le plus bas 0,05 ; puissance 44 %, 78 % et 98 % pour un écart de 1,5, 2,5 et 4.
  - 4 contre 4 : 55 %, 90 % et 99,8 % à 5 % ; rien à 1 %.
  - 5 contre 5 : 30 %, 75 % et 99 % à 1 %.
  - L'écart-type entre graines n'a jamais été mesuré (inconnue 5 du socle). Le plan à 4 contre 4 est donc un pari sur un écart d'au moins 2,5.
- **Épreuve à vérité connue (4 adaptateurs par bras, 200 mondes par ligne).**
  - Monde « acte » : retrouvé 99,5 %. Monde « disposition » : 99,5 %.
  - Monde « adaptateur seul » : 93,5 %, soit 6,5 % de faux « au-delà », proche du niveau nominal.
  - **Piège de l'intensité** : un témoin à 90 % de l'intensité du saboteur donne 47,5 % de faux « au-delà » ; à 60 %, 99,5 %.
  - Piège de l'adaptateur d'apprentissage laissé dans la comparaison : 11,5 % de faux « au-delà » au lieu de 6,5 %.
  - Conséquence : K1 seul ne peut jamais conclure « sabotage ». K3 exige l'intensité mesurée et une courbe d'étalonnage, non un simple réglage de la dose à l'œil.

## 4. Ce que dit chaque issue

- **K1.** Organisme et témoin indiscernables (aire sous 0,55 à 0,60) : la sonde lit « un adaptateur », quel qu'il soit. C'est la réponse au barreau 5 côté spécificité, forte parce que le témoin n'est même pas remis à l'intensité. Organisme au-dessus du témoin : **aucune conclusion sur le sabotage** (intensité, graine) ; seulement « tous les adaptateurs ne se valent pas », et l'étape 4 devient nécessaire.
- **K2.** Séparation à poids nus, consigne des deux côtés et texte égal : la sonde apprise sur l'adaptateur porte une composante liée au sabotage, qui n'est ni l'adaptateur ni la présence d'une consigne. C'est une existence, pas une part. Pas de séparation : hors de l'adaptateur, ce que la sonde lisait au modèle nu était la consigne ou le texte.
- **K3.** Saboteurs au-dessus de la courbe des témoins, sur des adaptateurs jamais vus : « au-delà de l'adaptateur » tient à l'échelle de la recette. Saboteurs sur la courbe : la sonde lit l'intensité du réglage fin ; l'organisme à adaptateur n'est pas recevable comme famille de la porte G1 sans témoin, et la reconception est commandée par N-062.
- **K4.** Ajouter la direction chez l'honnête fait gonfler le coût, ou la retirer chez le saboteur fait cesser le sabotage, au-delà du placebo : lien causal, l'issue la plus difficile à récuser. Aucun effet : « lisible, non contrôlable », résultat attendu et déjà publié, qui ne dit rien contre la lecture.
- **K5.** La règle retrouve le contraste interne publié et classe « organisme contre modèle nu » comme confondu : la méthode est validée hors de notre main. Elle échoue : la règle est à revoir avant toute phrase du dossier.
- **Autre pile.** Écart au-delà de la tolérance scellée : toutes les lignes de l'étape B bis passent en réserve jusqu'à explication.

## 5. Nœuds de Lazar

1. **Réemploi des scores fermés de l'étape B bis** pour l'étape 2, par un texte neuf scellé et contre-lu : écart à un texte scellé et lecture neuve. Recommandé, confiance haute.
2. **Sort du texte scellé de validité de l'adaptateur et de l'accord de 30 USD** (échéance le 27 novembre). Je recommande de ne pas le jouer tel quel : il vise les sondes génériques, ne garde aucune activation, pose un témoin à un seul exemplaire, et son aiguillage est inconnu. Je recommande de demander un accord neuf pour l'étape 3 (5 USD au plus). Confiance moyenne.
3. **Dépenses** : étape 3 (environ 5 USD), étape 5 (environ 5 USD), étape 4 (25 à 40 USD, devis), étape 6 (devis).
4. **Définition du témoin apparié** : distillé de l'honnête, intensité mesurée, plusieurs graines, sonde jamais jugée sur son adaptateur. Elle écrit une partie du critère de G1 (brouillon N-074, choix A ou C en attente).
5. **Organismes d'une autre main et autre lignée de modèle** : la décision R-122, « aucun organisme d'une autre main en phase 0 », est à rouvrir ; changement de modèle ; vérification des licences.
6. **Question à faire porter par une session autorisée** : le saboteur à budget ou le bras A font-ils varier le sabotage à poids constants par une variable que l'oracle connaît ? Si oui, y inscrire le contraste à organisme constant, retiré au brouillon 4 du texte de lecture du barreau 8. Ce serait le meilleur banc pour ce barreau.
7. **Attaquant informé par entraînement** contre l'invariant de N-053 ; revendication éventuelle ; envoi de la trousse de revérification au statisticien externe (contact : tu envoies).

**Proposer avec recommandation** (défaut sous 48 heures) : couche et sonde lues à l'étape 3 (celles retenues par pli, plus la couche 15 partout) ; tolérance d'accord entre les piles.

**Routine** : étape 1, code, double programmation, simulations.
