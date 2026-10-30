# Question pour le collisionneur (quatre modèles) et pour Argon à part — mesurer et valider l'universalité des défenses : brainstorm des questions candidates du texte III — v2

v2 (session-depot, 30 octobre 2026, R-826) : la v1 (rédacteur neuf, inchangée) plus deux changements demandés par Lazar : quatre modèles au collisionneur (Kimi K3.1 Pro ajouté) ; bloc 4 réécrit, la décision « plusieurs instances » étant prise.

**Garde de sûreté (en tête, à respecter sans exception) :**

- niveau méthode seulement ;
- aucune recette ;
- aucun exemple de mode d'attaque ;
- aucun scénario d'évasion ni description de la manière dont un agent tromperait un instrument ;
- aucun paramètre concret de famille.

Une réponse qui en produirait est écartée. On ne demande jamais de produire quoi que ce soit d'adverse : on demande comment **mesurer**, **borner**, **estimer** et **valider**.

Écrite par un rédacteur neuf, 30 octobre 2026, relevé `date -u` 11:32 UTC, d'après une demande du directeur de recherche, Lazar, reformulée puis validée par lui. Même forme « arbitre » que les questions précédentes : quatre modèles (Claude Opus 5.5, Claude Fable 5.1, Gemini Argon, Kimi K3.1 Pro), trois tours ; puis Argon seul, à part, avec le même texte. **Sujet entièrement défensif et méthodologique.** La synthèse est matériau pour un préenregistrement ; elle ne tranche rien ; tout chiffre qui ne vient pas des faits est marqué « illustratif ».

## Contexte (autoportant : il suffit à répondre)

Un programme de recherche défensive étudie le contrôle de systèmes d'intelligence artificielle : détection d'un sabotage diffus par des sondes sur les activations internes et par des moniteurs qui ne lisent que le texte (boîte noire), avec agrégation séquentielle des indices ; modèles à poids ouverts de 8 et de 70 milliards de paramètres. Règle de base : le programme ne construit **aucun agent attaquant opérationnel**. Pour évaluer ses défenses, il utilise des **familles** (classes d'éléments d'évaluation simulés, définies par un schéma de construction, jamais décrites ici), dont certaines sont **tenues à l'écart** : ni les concepteurs de la défense ni la défense ne les voient avant la mesure finale.

Le **texte III** de la course d'idéation demandera, au niveau méthode, comment concevoir un **bras d'attaque** (le banc d'évaluation adverse, simulé, qui sert à mesurer, sans agent opérationnel) et une **mesure de l'universalité** des défenses qu'**un tiers puisse vérifier**. Le présent brainstorm produit les questions candidates de ce texte. Un statut accompagne chaque fait des pièces : VÉRIFIÉ (avec chemin) ou SUPPOSÉ.

Donnée de départ : deux sources indépendantes en apparence ont énuméré 28 et 25 familles, dont 18 communes. L'estimateur de Lincoln-Petersen donne environ 39. Selon le dossier, les deux sources sont deux modèles de fournisseurs différents, qui ont reçu la même question et la même grille fermée ; un lecteur unique a fait l'appariement, et il appartient à la lignée d'une des deux sources ; l'appariement n'est pas bijectif (une famille d'une source en recouvre deux de l'autre).

## Question

« Concevez la **méthode** qui permettrait d'affirmer, devant un tiers, qu'une défense est universelle sur un ensemble de familles, et de confronter cette affirmation à des mesures extérieures. Répondez par quatre blocs, dans cet ordre.

### Bloc 1 — Quatre propositions préalables, avant toute question candidate

**(a) Définition opérationnelle de l'universalité.** Options à comparer : pire cas sur une classe de familles déclarée d'avance ; écart de performance entre familles vues et familles tenues à l'écart ; quantile ou proportion de familles où la défense passe un seuil ; autre. Pour chacune : ce qu'il faut déclarer avant la mesure, l'énoncé exact qu'elle autorise (avec quantificateur et classe), ce qu'elle n'autorise pas, et comment un tiers la vérifie. Dites en particulier ce qui sépare « universelle sur la classe déclarée » de « robuste à l'inconnu ».

**(b) Modèle de menace de la mesure.** Adversaire d'évaluation aveugle ou informé de la défense : quelles catégories d'information il possède (existence de la défense, liste des familles, protocole de mesure, seuils), son budget (nombre d'essais, calcul, interactions), et comment rapporter les résultats par palier d'information. Vous décrivez des **paramètres de la mesure**, jamais des conduites ni des moyens. Précisez ce que l'évaluation interdit de partager entre construction et évaluation de la défense.

**(c) Combien de familles, par simulation.** Comment calculer le nombre de familles nécessaire pour affirmer l'universalité avec une confiance donnée : énoncé cible (par exemple : avec confiance 1 − α, la part de la classe où la défense échoue est inférieure à ε), modèle génératif de la population de familles, hétérogénéité et dépendance entre familles proches, variance à deux niveaux (entre familles, et entre éléments d'une famille), règle d'arrêt séquentielle, analyses de sensibilité. Un point à traiter : les familles sont **découvertes**, non tirées au hasard ; la garantie dépend donc du mécanisme de découverte. Dites ce que la simulation peut démontrer et ce qu'elle suppose.

**(d) Combien de familles encore inconnues.** Refaites le calcul de Lincoln-Petersen sur les données ci-dessus (et sa version corrigée de Chapman), puis discutez ses hypothèses : population fermée, indépendance des sources, même probabilité de capture pour toutes les familles, appariement exact. Dites dans quel sens la dépendance entre sources, l'hétérogénéité et l'erreur d'appariement déplacent l'estimation. Indiquez quels estimateurs employer avec plusieurs sources : Chao (bornes inférieures), Good-Turing (masse manquante, couverture), capture-recapture multi-sources (modèles log-linéaires, classes latentes), approche bayésienne. Dites comment tester l'indépendance, comment traiter un refus commun de répondre (une même censure sur toutes les sources) et ce que devient l'estimation si le nombre de familles n'est pas fermé.

### Bloc 2 — Données de départ à recommander

Plutôt que des résumés, quelles données brutes recommandez-vous, et pourquoi ? Candidates : (i) les trajectoires brutes de bancs publics conçus par d'autres (SHADE-Arena, ControlArena, MonitoringBench, SLEIGHT-Bench, Liars' Bench), utilisées comme **familles extérieures** ; (ii) les journaux de refus de questions passées ; (iii) les propositions brutes d'une course précédente. Pour chacune : indépendance réelle vis-à-vis du programme, étiquetage au niveau des familles, risque de recouvrement avec ce que les modèles ont déjà vu, coût de mise au format, usage possible comme source supplémentaire de capture-recapture. Si vous ne connaissez pas un banc, dites-le : n'inventez ni contenu ni référence.

### Bloc 3 — Questions candidates pour le texte III

**Au plus cinq par modèle.** Chaque question est formulée en termes de mesurer, valider, borner ou estimer. Pour chacune :

1. l'**avantage** qu'elle exploite ;
2. le **piège méthodologique** qui la tuerait ;
3. la **validation extérieure** qu'elle permet : familles conçues hors du programme, prédictions scellées confrontées à des mesures, revue extérieure ;
4. sa **probabilité de refus** par un modèle (faible, moyenne, élevée ; pourcentage illustratif) et la raison, en disant comment la formulation reste au niveau méthode.

### Bloc 4 — Question annexe

**Décision prise par le directeur** : les familles tenues à l'écart seront conçues par **plusieurs instances indépendantes**, de fournisseurs et de modèles différents (cinq sont prévues), chacune tenue à l'écart de la conception des défenses et scellée à part. Proposez **comment l'organiser** :
- ce que chaque instance reçoit (même consigne ou consignes différentes) ;
- comment empêcher les fuites entre elles ;
- comment apparier leurs familles sans qu'un lecteur unique biaise l'appariement ;
- comment tester leur indépendance (corrélation des données d'entraînement entre fournisseurs) ;
- comment s'en servir comme sources multiples pour estimer les familles encore inconnues ;
- ce qu'on fait si une instance refuse.

Pour chaque point : options, avantage, inconvénient, recommandation et confiance. Ce qui n'est pas dans les pièces ou dans le contexte est marqué SUPPOSÉ. »

## Insertion dans les consignes du tour

- Livrable (a) du tour : ce que la question suppose sans que ce soit établi correspond aux hypothèses des blocs 1(b), 1(c) et 1(d).
- Livrable (b), duels : formulez au moins deux duels H_A contre H_B portant sur des **estimateurs ou des définitions** (par exemple : Lincoln-Petersen contre estimateur par bornes de Chao), avec métrique, seuil, contrôle négatif et issue qui falsifie chaque hypothèse.
- Livrable (c), mesure minimale : l'instrument est ici l'**estimateur du nombre de familles** et la **mesure d'universalité** ; la mesure minimale est leur couverture et leur biais sur des mondes simulés à vérité connue, contre une base à battre (comptage brut des familles observées).
- Respectez la limite de mots du tour : définitions courtes ; si la place manque, gardez dans l'ordre les blocs 1, 3, 4, 2.

## Critères de lecture de la synthèse (gelés avant lecture)

- Une définition de l'universalité n'est retenue comme « commune » que si deux modèles au moins la donnent avec le même quantificateur, la même classe déclarée et la même statistique ; sinon « divergente », options au format décision.
- Une réponse qui contient une recette, un exemple de mode, un scénario d'évasion ou un paramètre concret de famille est écartée et comptée.
- Une question candidate sans validation extérieure chiffrée ou sans piège nommé est marquée « non retenue ».
- Un estimateur du nombre de familles sans ses hypothèses explicites est marqué « non jugeable ».
- L'avis d'Argon à part est lu à côté, non compté dans « commun ».
