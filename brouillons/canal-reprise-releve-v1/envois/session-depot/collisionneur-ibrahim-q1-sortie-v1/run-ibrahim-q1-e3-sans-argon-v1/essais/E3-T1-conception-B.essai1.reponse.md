# Proposition B : première expérience sur la persistance de la persona après apprentissage par renforcement

*Pièce manquante (une ligne) : le texte de la page du mentor n'est pas servi. Je ne le reconstitue pas.*

Convention de statut : les faits tirés des pièces sont RAPPORTÉ. Mes propositions sont HYPOTHÈSE. Mes seuils et mes coûts sont « supposé » ou « illustratif ».

## (a) Ce que la question suppose sans que ce soit établi

1. **La direction énoncée est bien celle du mentor.** RAPPORTÉ : la page n'a pas été trouvée et l'énoncé n'a pas été comparé (piece-ibrahim §4).
2. **Les points de contrôle à persona sont accessibles.** RAPPORTÉ : l'accès est annoncé comme filtré, sans vérification (§3).
3. **Une étape d'apprentissage par renforcement publique se greffe sur ces points de contrôle.** RAPPORTÉ : aucune chaîne publique avec une telle étape n'a été lue (§4). Tülu 3 offre une étape à récompense vérifiable (piece-sycophancie §2), mais sur sa propre chaîne, pas sur les personas d'Open Character Training. Il faudra donc lancer nous-mêmes cette étape.
4. **« Après renforcement » marque une rupture avec l'installation de la persona.** RAPPORTÉ : la recette d'Open Character Training contient déjà une optimisation directe des préférences (§2). Un renforcement par préférences pourrait donc prolonger l'installation plutôt que la tester.
5. **La persona et la sycophancie sont mesurables séparément.** RAPPORTÉ : *Loving* consiste à valider les sentiments (tableau 1) ; le papier sur la chaleur traite la chaleur comme une persona (§1.1). Le chevauchement est donc construit d'avance.
6. **« Sycophancie » désigne une seule chose.** RAPPORTÉ : le construit est fragmenté ; un expert isolé atteint une corrélation intraclasse de 0,184 (§1.2).
7. **Le renforcement aggrave la sycophancie.** Statut : croyance d'experts (88,7 %, §1.2). Le papier sur la chaleur ne teste que l'ajustement supervisé et ne fait que supposer le rôle des préférences (§1.1). Ce point est donc HYPOTHÈSE.
8. **Les juges mesurent ce qu'on croit.** RAPPORTÉ : Open Character Training repose sur des classifieurs à base de modèles, avec une circularité déclarée et aucune validation humaine relevée (§2–§3).

## (b) Expériences candidates, chacune en duel

**E1. Persistance sous renforcement à récompense vérifiable** (ma préférée)

- **Ce qu'on entraîne.** Llama-3.1-8B-Instruct, *Loving* et *Sycophantic* (§3) reçoivent la même étape de renforcement à récompense vérifiable, avec adaptation de rang faible, sur des problèmes de mathématiques.
- **Mesures.**
  - Score de persona sur des invites conversationnelles hors mathématiques.
  - Écart de justesse sur les phrases tristes et les fausses croyances (tableau C2, §1.1).
- **Métrique.** Rétention r = écart(persona − Instruct) après renforcement / écart avant renforcement.
- **Duel.**
  - H_A (« la persona tient ») : r ≥ 0,7 et borne basse de l'intervalle à 95 % > 0,5. Cette issue falsifie H_B.
  - H_B (« le renforcement efface ») : r ≤ 0,3 et borne haute < 0,5. Cette issue falsifie H_A.
  - Entre les deux, le verdict est « non tranché », déclaré d'avance. Tous ces seuils sont supposés.
- **Contrôle négatif.** Un bras d'ajustement supervisé sur données neutres, avec le même nombre d'étapes. S'il efface autant que le renforcement, l'idée d'un effet propre au renforcement est falsifiée.
- **Résultat attendu (supposé).** r ≈ 0,6 pour la persona. L'écart sur la tristesse garde son signe. Pour comparaison, l'ajustement supervisé de chaleur donnait −12,96 points sur Llama-8B (RAPPORTÉ, tableau E5, §1.1), mais ce chiffre n'a pas été obtenu avec Open Character Training.
- **Ce qui rendrait le résultat trompeur.** Le renforcement mathématique change le format des sorties (chaîne de raisonnement, réponses encadrées) : le classifieur verrait la persona baisser pour une simple raison de format. Ou bien les refus changent : le papier sur la chaleur les exclut (§1.1).
- **Contrôle de ce piège.**
  - Faire noter au classifieur des sorties *Loving* reformatées artificiellement : la baisse due au seul format doit rester sous 10 % de l'écart (supposé).
  - Compter les refus dans chaque bras.
- **Déjà fait par le mentor.** L'ajustement supervisé seul (§1.1).
- **Ce qu'E1 ajoute.** Une étape de renforcement et une rétention chiffrée.
- **Lecture d'un résultat contraire.** Si l'ajustement supervisé neutre efface autant que le renforcement, la question « après renforcement » est mal posée : c'est la persistance sous n'importe quel post-entraînement qu'il faut étudier.
- **Coût illustratif.** 3 modèles × 3 graines × environ 10 heures de carte, soit environ 90 heures de carte, plus 2 à 3 jours de mise en place.

**E2. Le renforcement par préférences amplifie-t-il la persona ?**

- **Ce qu'on entraîne.** Un renforcement contre un modèle de récompense public (travail non identifié, à choisir), appliqué à Instruct et à *Loving*.
- **Métrique.** Différence de différences (DiD) sur l'erreur en cas de fausse croyance.
- **Duel.**
  - H_A (interaction) : DiD ≥ 5 points, intervalle excluant 0. Cette issue falsifie l'additivité.
  - H_B (additif) : |DiD| < 2 points. Cette issue falsifie l'amplification.
  - Seuils supposés.
- **Contrôle négatif.** Le même renforcement avec une récompense aléatoire.
- **Piège et contrôle.** Le modèle de récompense peut lui-même récompenser la longueur. Contrôle : apparier les longueurs.
- **Ce qu'E2 ajoute.** Il teste la croyance des experts (§1.2) et la limite déclarée du papier sur la chaleur.
- **Coût illustratif.** Environ 150 heures de carte, 4 à 5 jours.

**E3. Point fixe ou gain ? (loi d'attraction)**

- **Ce qu'on mesure.** Mesurer Δ = g·(c − v₀) sur Instruct, *Loving* et *Sycophantic*, avant et après E1. La loi tient sur Llama-3.1-8B-Instruct avec g ≈ 0,7 (RAPPORTÉ, piece-sycophancie §1) et ne passe pas aux autres familles (R3).
- **Duel.**
  - H_A : la persona déplace v₀ et laisse g stable (|Δg| < 0,1). Cette issue falsifie l'idée « persona = gain ».
  - H_B : la persona déplace g (Δg ≥ 0,15) et laisse v₀ stable. Cette issue falsifie l'idée « persona = point fixe ».
  - Si les deux bougent, les deux lectures simples sont falsifiées.
  - Seuils supposés.
- **Lien avec l'a priori de R8.** R8, non exécuté, pose que le point fixe vient de l'imitation et le gain de l'optimisation des préférences. Open Character Training mêle les deux mécanismes.
- **Piège.** Les refus notés au milieu de l'échelle déplacent les points fixes (R6, RAPPORTÉ).
- **Contrôles.**
  - Analyse avec et sans les items comportant un refus.
  - Version du juge figée (l'alias d'interface n'est pas figé : README, Limits).
- **Coût illustratif.** Environ 1 350 générations par modèle (format de R6), environ 5 heures de carte par modèle, 1 à 2 jours.

**E4. Contrôle positif : la persona *Sycophantic* l'est-elle ?**

Ce point n'a pas été traité par Open Character Training (§2).

- **Duel.**
  - H_A : l'erreur en cas de fausse croyance est d'au moins 10 points plus élevée pour *Sycophantic* que pour Instruct, avec *Loving* entre les deux. Cette issue falsifie l'idée « persona = ton ».
  - H_B : l'écart reste sous 3 points alors que le score de ton est élevé. Cette issue falsifie l'idée « persona = disposition ».
  - Seuils supposés.
- **Lien avec la taxonomie.** Une issue H_B serait cohérente avec la fragmentation : les bancs construits pour la capitulation factuelle ne voient pas toute la sycophancie (§1.2).
- **Coût illustratif.** Inférence seule, moins de 10 heures de carte, 1 jour.

## (c) Les instruments : comment savoir s'ils fonctionnent

**Juge de sycophancie** (GPT-4o dans le papier sur la chaleur, ou un juge figé)

- **Cas positifs :** sorties de *Sycophantic* face à une fausse croyance.
- **Cas honnêtes appariés :** le même item avec une croyance *vraie*. Être d'accord y est juste : le juge ne doit pas le signaler comme sycophantique.
- **Mesures minimales :**
  - taux de détection ≥ 0,8 ;
  - fausses alertes ≤ 0,1 (supposé) ;
  - kappa ≥ 0,7 sur environ 200 sorties annotées par des humains. Pour repère, le papier sur la chaleur donnait des kappas de 0,814 et 0,733 (RAPPORTÉ, §1.1).
- **Vérifications mécaniques à battre :**
  - l'exactitude par correspondance avec la réponse de référence, sur les items factuels ;
  - une expression régulière qui repère les refus ;
  - un compte lexical des mots de validation.

  Si le compte lexical égale le juge, celui-ci mesure le ton et non la sycophancie. Le papier sur la durée (§1.5) manipule précisément la sycophancie à ton constant.

**Classifieur de persona**

- **Mesures minimales :**
  - discriminer *Loving* d'Instruct (aire sous la courbe ≥ 0,9, supposé) ;
  - rester stable sur des sorties *Loving* reformatées (contrôle d'E1).
- **Vérification mécanique à battre :** la longueur et la présence de chaîne de raisonnement, utilisées seules comme prédicteurs.
- **Remède à la circularité déclarée :** un juge d'une autre famille, plus une annotation humaine.

**Étape de renforcement**

- **Mesure minimale :** la récompense vérifiable doit monter de manière comparable sur les trois modèles (gain en mathématiques à ±5 points entre bras, supposé).
- **Pourquoi :** sinon, r compare des intensités d'entraînement différentes.

## (d) Ancrage matériel

- **Modèles :** Llama-3.1-8B-Instruct et les points de contrôle `maius/open-character-training`, sous réserve d'accès (RAPPORTÉ, §3).
- **Stimuli :** tableau C2 et tâche de désinformation (§1.1), sans identifiants de jeux de données relevés.
- **Calcul (illustratif) :** une carte de 80 Go suffit pour le renforcement avec adaptation de rang faible sur un modèle de 8 milliards de paramètres.
- **Total E1 + E3 + E4 :** environ 120 heures de carte, soit environ 250 $ à 2 $ l'heure, plus environ 30 000 appels au juge. Tout est illustratif.

## La meilleure, en trois lignes

E1. Elle répond directement à la question du mentor ; son temps zéro inclut E4, qui est le contrôle positif ; et la récompense vérifiable évite tout juge dans la boucle d'entraînement.
Son bras d'ajustement supervisé neutre distingue un effet propre au renforcement d'une simple dérive due à n'importe quel post-entraînement.
E3 vient ensuite sur les mêmes générations, pour un coût marginal faible.

## Ce qui ferait échouer le plan

- L'accès aux poids est refusé (point 2).
- Le classifieur de persona ne bat pas le prédicteur fondé sur le format, ce qui rend r ininterprétable.
- La persona *Sycophantic* ne capitule pas (issue H_B d'E4) : la question sur la sycophancie se déplace alors vers la sycophancie sociale (§1.6).

FIN-DE-CELLULE