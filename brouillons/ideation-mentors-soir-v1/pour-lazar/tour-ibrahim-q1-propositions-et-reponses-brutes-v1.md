# Tour du collisionneur, Ibrahim Q1 (sans Argon) — propositions (E3-T1) et réponses aux critiques (E3-T3), brutes

Copie à l'octet vérifiée contre les compagnons ; espèces par lettre ; rien lu ni modifié par conv-audit.


---

## E3-T1-conception-A.md (sha256 `8446addfcbd2b8057e7be03cc69196ecac10413bf7aa1ac804aefa8b29da537e`)

# Cellule A — Première expérience : persona de caractère, étape RL, sycophancie

Toute donnée des trois pièces est au statut **RAPPORTÉ** (lue par un rédacteur sur page primaire, non auditée par moi). Mes prédictions sont **HYPOTHÈSE** ; mes chiffres sont « illustratif » ou « calcul ».

## (a) Ce que la question suppose sans l'établir

1. **Qu'il existe une étape RL à appliquer.** Open Character Training distille par DPO, le RL est « travail futur » (pièce Ibrahim §2) ; aucune chaîne publique de points de contrôle avec étape RL n'a été lue (pièce Ibrahim §4). Seul le plan R8 de Lazar nomme des étapes SFT/DPO/RLVR sur Tülu 3, non exécuté (pièce sycophancie §2). Statut : RAPPORTÉ pour l'absence ; l'étape RL doit être construite.
2. **Que la persona est mesurable indépendamment du style.** OCT l'évalue par classifieurs à base de modèles, avec biais et circularité déclarés, sans validation humaine relevée (pièce Ibrahim §2–3). Statut : RAPPORTÉ.
3. **Que « la sycophancie » est un construit unique.** La taxonomie (§1.2) la dit fragmentée ; les bancs de capitulation factuelle ratent le biais de cadrage ; le pilotage par hypothèses verbalisées marche sur le social, mal sur le factuel (§1.4). Statut : RAPPORTÉ.
4. **Que l'optimisation par préférences cause la sycophancie.** 88,7 % de 106 experts le pensent, mais un expert isolé n'est fiable qu'à ICC 0,184 (§1.2) ; le papier *Nature* ne teste que le SFT et « suppose » le rôle des préférences (§1.1). Statut : RAPPORTÉ comme croyance, HYPOTHÈSE comme fait.
5. **Que les poids OCT sont accessibles.** Accès « filtré » annoncé, non vérifié (pièce Ibrahim §3). Statut : OBSERVÉ-NON-AUDITÉ.

## (b) Expériences décisives (duels)

Modèle commun aux trois : Llama-3.1-8B-Instruct, présent dans le papier chaleur, OCT et les sondes (pièce Ibrahim §3) et dans la loi d'attraction (pièce sycophancie §1).

### E1 — Étalonnage : la persona *Sycophantic* est-elle sycophante à l'instrument ?
*Mesure* : points de contrôle OCT *Loving*, *Sycophantic*, base Instruct ; tâche de désinformation avec fausse croyance (*Nature*, Méthodes, §1.1) ; protocole R6 (30 items × 3 conditions × 5 tirages, pièce sycophancie §1) pour g et point fixe. Aucun entraînement.
*Duel* : **H_A** — la persona déplace la capitulation factuelle (erreur fausse croyance ≥ +11 points, ordre du papier chaleur, RAPPORTÉ) **et** le gain g. **H_B** — elle ne déplace que le point fixe (validation, langage) sans changer g ni l'erreur factuelle (fragmentation, §1.2).
*Seuils* : Δerreur ≥ 5 points (illustratif), IC95 excluant 0 ; Δg ≥ 0,2 (calcul : largeur de l'IC fort−doux de R6, [−0,220 ; 0,197]).
*Contrôle négatif* : base Instruct avec une consigne système reprenant le texte de la persona *Sycophantic* (tableau 1 OCT) : si elle produit le même déplacement, le classifieur et le juge lisent le style, non l'entraînement.
*Falsifications* : issue H_A réfute « sycophancie sociale et factuelle se dissocient sous persona » ; issue H_B réfute « la tâche de désinformation suffit comme lecture de la persona » et impose deux instruments pour E2.
*Déjà fait* : le papier chaleur a montré l'effet d'un SFT chaleureux sur ces tâches (§1.1) ; OCT n'a pas mesuré la sycophancie de sa persona (§2). *Ajout* : la persona DPO+SFT sur les mêmes instruments, et la lecture g/point fixe.
*Trompeur* : refus notés au milieu de l'échelle gonflent le point fixe (R6 : sans 14 items à refus, points fixes 1,92 et 2,03 contre 2,60, pièce sycophancie §1). Contrôle : analyse avec et sans items à refus, décidée d'avance.
*Coût* : 2 jours, 0 heure de carte d'entraînement, ~5 000 générations + jugement (illustratif).

### E2 — Persistance : un RL à récompense vérifiable efface-t-il la persona ?
*Entraînement* : étape RLVR courte (récompense exacte sur problèmes vérifiables, recette de type Tülu 3, « travail non identifié » hors pièce sycophancie §2), LoRA, sur trois départs : *Loving*, *Sycophantic*, base Instruct.
*Mesure* : avant/après, score du classifieur de persona OCT, erreur fausse croyance, g et point fixe (protocole E1). Contrôle positif que le RL a mordu : justesse sur la tâche vérifiable ↑ (seuil +5 points, illustratif).
*Duel* : **H_A** — la persona tient : rétention du score persona ≥ 80 % (illustratif) et |Δg| < 0,2 ; c'est la condition S3 de R8 (« RLVR ne change pas g », pièce sycophancie §2). **H_B** — le RL érode : rétention < 50 % ou |Δg| ≥ 0,2 au-delà du mouvement de la base.
*Contrôle négatif 1* : base Instruct sous le même RL (dérive propre au RL). *Contrôle négatif 2* : persona sans RL, mais SFT sur les mêmes prompts et ses propres sorties, même nombre de pas (sépare l'exposition aux prompts de la récompense).
*Falsifications* : issue H_A réfute « le RL écrase ce qu'installe l'entraînement de caractère » ; issue H_B réfute l'a priori R8 « le gain vient de l'optimisation des préférences » puisqu'un RL sans préférence humaine l'aurait déplacé.
*Déjà fait* : rien sur la persistance après entraînement ultérieur (pièce Ibrahim §2) ; le papier chaleur n'a testé que le SFT (§1.1). *Ajout* : la première chaîne persona → RL mesurée.
*Trompeur* : le RLVR change longueur et format des réponses ; les juges et le classifieur peuvent lire ce changement comme perte de persona ou comme baisse de sycophancie. Contrôle : rejugement sur réponses tronquées à longueur fixe **et** à longueur entière (la troncature à 300 caractères a déjà produit un faux positif dans les dépôts de Lazar, pièce sycophancie §3) ; les deux doivent concorder.
*Attendu (HYPOTHÈSE, signé)* : rétention 70–90 % du score persona, Δg ≈ 0 ± 0,1, Δerreur fausse croyance −2 à +2 points, tous illustratifs.
*Coût* : 5 jours ; 3 départs × ~500 pas RLVR LoRA sur 8B ≈ 30–60 heures de carte H100 (illustratif).

### E3 — Attribution : préférences ou persona ?
*Entraînement* : plan 2 × 2, persona {*Loving*, aucune} × étape {RLVR, RL à modèle de récompense appris sur paires de préférences}. Même nombre de pas, même LoRA.
*Duel* : **H_A** — le gain g et l'erreur fausse croyance montent sous RL-préférences quel que soit le départ (croyance des experts, §1.2 ; supposition du papier chaleur, §1.1). **H_B** — ils montent avec la persona et pas avec l'étape : l'étape ne fait que déplacer le point fixe.
*Seuils* : interaction persona × étape sur g ≥ 0,2 (calcul, comme E1).
*Contrôle négatif* : modèle de récompense réentraîné sur paires équilibrées en validation émotionnelle, puisque les réponses préférées de PRISM/UltraFeedback/LMSys contiennent plus de validation (§1.6) ; si l'effet disparaît, il venait des données de préférence, pas du RL.
*Falsifications* : issue H_A réfute « la persona porte seule la sycophancie » ; issue H_B réfute la cause principale désignée par 88,7 % des experts, au moins sur ce modèle.
*Déjà fait* : la taxonomie sonde la croyance, pas la cause ; le papier chaleur mesure le SFT. *Ajout* : la cause supposée est manipulée.
*Trompeur* : le modèle de récompense note la chaleur ; on mesurerait sa préférence, pas celle d'humains. Contrôle : validation humaine de 200 paires (ordre de grandeur des 235 et 470 annotations du papier chaleur, §1.1, non réconciliées).
*Coût* : 8 jours, ~100 heures de carte (illustratif).

## (c) Instruments : la mesure minimale qui dirait s'ils fonctionnent

- **Classifieur de persona (OCT)** : détection = part des sorties *Loving* classées *Loving* ; fausse alerte = part des sorties de la base Instruct **avec consigne système de style chaleureux** classées *Loving* (cas honnêtes appariés par item). Vérification mécanique à battre : compte de mots de validation + longueur, en régression logistique ; le classifieur doit dépasser l'AUC mécanique de ≥ 0,1 (illustratif). Sans cela, « persistance de la persona » mesure la persistance d'un lexique.
- **Juge de sycophancie (GPT-4o ou juge Claude)** : 200 sorties annotées par deux humains, stratifiées refus / longueur ; détection sur capitulations explicites, fausse alerte = refus ou nuances notés comme capitulation. À battre : correspondance exacte de la fausse croyance dans la réponse. Repère : accords 90,2 % / 86,0 %, κ 0,814 / 0,733 (§1.1, RAPPORTÉ) ; le kappa κ = 0 à accord brut 0,92 observé sur des juges au plafond (pièce nos-résultats §4) montre pourquoi l'accord brut ne suffit pas.
- **Sondes d'activation** (si on les ajoute comme lecture de persistance) : lisible n'est pas causal (ρ 0,684, ablation de rang 3 non répliquée, greffe 65 % [42 ; 87], pièce sycophancie §3). Mesure minimale : AUC sur sorties neuves d'un point de contrôle jamais vu par la sonde, contre un plancher de 200 sondes aléatoires appariées en covariance (procédé P3, pièce nos-résultats §6).

## (d) Ancrage matériel

Llama-3.1-8B-Instruct ; points de contrôle `maius/open-character-training` et code `github.com/maiush/OpenCharacterTraining` (pièce Ibrahim §3, accès non vérifié) ; stimuli : tableau C2 et tâche de désinformation (§1.1), items et préenregistrements R6 (pièce sycophancie §1). Calcul total E1+E2 : ~60 heures de carte H100, ~20 000 générations jugées (illustratif) ; E3 double la note.

## La meilleure : E2, avec E1 comme porte d'entrée

E2 répond mot pour mot à la direction du mentor et à la condition S3 déjà préenregistrée par Lazar ; E1 lui coûte deux jours sans entraînement et décide quel instrument lit la persona avant qu'on dépense une heure de carte. Les deux issues de E2 tranchent un a priori écrit d'avance.

## Ce qui ferait échouer le plan

1. Poids OCT inaccessibles : réentraîner *Loving* avec la recette publique (+3 jours, LoRA rang 64, 12 000 transcriptions, §2), en perdant l'ancrage sur les points de contrôle du papier.
2. RLVR trop court pour mordre (contrôle positif non atteint) : E2 n'est pas interprétable, il faut une dose-réponse en pas de RL, comme R6 l'a fait pour la pression.
3. Instruments en échec à (c) : le classifieur ne bat pas le lexique ou le juge note les refus au milieu ; alors aucun résultat de persistance n'est lisible, et E1 doit être republié comme résultat négatif sur les instruments.

FIN-DE-CELLULE

---

## E3-T1-conception-B.md (sha256 `5356e16c1708bfe75d6b151108939c4f8e4a7869e0dd54d7c04bb991fbd6bd4c`)

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

---

## E3-T1-conception-D.md (sha256 `c0fc7733e13d22039e22147f3287259f23b3e966b6810cc3d5c42e42fdacf9fc`)

# Proposition D — persistance de persona après RL

**Statuts.** Les publications et dépôts sont seulement **RAPPORTÉS** par les pièces ; je ne les re-vérifie pas. Les résultats expérimentaux des dépôts publics sont **OBSERVÉS-NON-AUDITÉS**. Toutes les attentes ci-dessous sont des **HYPOTHÈSES supposées** ; tous les coûts et seuils opérationnels sont **illustratifs**.

## (a) Ce que la question suppose sans l’établir

- **La direction exacte du mentor** : sa page n’est pas servie. La formulation précise des deux projets est donc inconnue (**RAPPORTÉ**, pièce Ibrahim §4).
- **L’accès matériel** : les poids Open Character Training sont annoncés avec accès filtré, mais leur disponibilité réelle n’est pas vérifiée (**RAPPORTÉ**, §2–4).
- **La validité des personas** : assimiler *Loving* à la chaleur du papier, ou *Sycophantic* à une sycophancie effectivement mesurée, est une **HYPOTHÈSE**. OCT n’a traité ni persistance après entraînement ultérieur ni sycophancie de cette persona (**RAPPORTÉ**, §2).
- **Le transfert du SFT au RL** : le travail sur la chaleur teste seulement l’ajustement supervisé ; la portée du « +11 points » reste indéterminée (**RAPPORTÉ**, §1.1 et §4). Il n’établit donc ni persistance ni effet du RL.
- **Un construit unique de sycophancie** : capitulation factuelle et cadrage social implicite ne sont pas interchangeables (**RAPPORTÉ**, §1.2). Enfin, R8 est non exécuté et R6 n’a pas de notation humaine publiée (**RAPPORTÉ/OBSERVÉ-NON-AUDITÉ**, pièce sycophancie §1–2).

## (b) Trois expériences candidates

### E1 — La persona survit-elle au RLVR ?

**Entraînement.** Llama-3.1-8B-Instruct, checkpoints OCT *Loving*, *Sycophantic* et base ; trois graines (**illustratif**). Même RL à récompense vérifiable sur réponses exactes, sans récompense de préférences. Témoins : persona sans RL, base soumise au même RL, et récompense permutée pour séparer exposition/optimisation.

**Mesure.** Sur des items de persona indépendants des données d’entraînement, soit \(C\) l’écart persona–base et \(R=C_{\mathrm{après}}/C_{\mathrm{avant}}\). **H_A : persistance**, \(R\geq0,50\), attente \(R=+0,85\) ; **H_B : érosion dominante**, \(R<0,50\), attente \(R=+0,20\) (seuils et valeurs **supposés**). \(R\geq0,50\) falsifie H_B ; \(R<0,50\) falsifie H_A.

**Trompeur/contrôle.** Un classifieur peut ne retenir que le style ou s’auto-valider : contrôle base apparié, étiquettes permutées et validation humaine décrite en (c). Un résultat contraire conclurait à une non-persistance **dans ce régime**, pas à une disparition universelle.

**Déjà fait/ajout.** OCT installe les personas ; le papier chaleur reste en SFT. E1 mesure causalement leur maintien après RL. **Coût : 5 jours, 240 h-GPU (illustratif).**

### E2 — Après RL, l’effet est-il socialement sélectif ou général ?

**Mesure.** Sur les checkpoints E1 : capitulation factuelle \(F\), par réponses vérifiables avec fausse croyance ; sycophancie sociale \(S\), sur requêtes de conseil et items multi-tours, à ton et format constants (pièce Ibrahim §1.1, §1.5–1.7). Les \(\Delta S,\Delta F\) sont les doubles différences \((persona-base)\times(RL-sansRL)\).

**H_A : sélectivité sociale**, \(\Delta S-\Delta F\geq+5\) points ; attente \(\Delta S=+12\), \(\Delta F=+2\) points. **H_B : absence de sélectivité**, différence \(<+5\) points ; attente \(\Delta S=\Delta F=+8\) points (**supposé**). Chaque zone falsifie l’autre hypothèse.

**Trompeur/contrôle.** Confondre chaleur, refus ou longueur avec validation : positions inversées, contexte neutre, ton figé, refus analysés séparément et justesse factuelle extraite mécaniquement. Un résultat contraire interdirait d’attribuer un effet social spécifique à la persona ; il pourrait être générique au RL ou nul.

**Déjà fait/ajout.** Les travaux rapportés séparent progressivement chaleur, construits sociaux et interaction dans la durée ; E2 ajoute le croisement persona × RL. **Coût marginal : 2 jours, 48 h-GPU (illustratif).**

### E3 — Le RL change-t-il le gain de pression sociale ?

**Mesure.** Protocole dose–réponse R6, sous éloge et critique, sur base/persona avant et après RL. Ajuster \(\Delta=g(c-v_0)\), avec paramètres estimés par item et graine.

**H_A : invariance du gain après RLVR**, \(|\Delta g|<0,05\), attente signée \(\Delta g=0,00\). **H_B : modification du gain**, \(|\Delta g|\geq0,05\), attente \(\Delta g=+0,20\) sous éloge (**supposé**). Le point fixe \(c\) est secondaire.

**Trompeur/contrôle.** Des refus notés au milieu de l’échelle peuvent déplacer artificiellement \(c\) (**OBSERVÉ-NON-AUDITÉ**, pièce sycophancie §1) : les stratiﬁer, ajouter dose nulle, doses permutées et opposer le modèle d’attraction à un déplacement constant. Un \(\Delta g\) non nul falsifie la condition S3 dans ce cadre ; une invariance ne prouve pas la persistance de persona.

**Déjà fait/ajout.** R6 mesure la loi sur Llama, R3 montre qu’elle ne généralise pas à toutes les familles, R8/Tülu reste non exécuté. E3 ajoute persona et RLVR. **Coût marginal : 2 jours, 36 h-GPU (illustratif).**

## (c) Validation minimale des instruments

Avant toute interprétation, constituer **200 paires honnêtes appariées** — même contenu sémantique, variations d’ordre, longueur, ton ou refus sans changement de position — et **200 cas à contraste comportemental connu**, décrits par classe et validés humainement (**illustratif**).

Pour chaque juge persona/social : détection ≥80 %, fausses alertes ≤5 %, annotation humaine en aveugle et seconde famille de juge en sensibilité. Il doit battre les règles mécaniques « réponse majoritaire », longueur, sentiment, mots-clés, refus et ordre. Pour \(F\), l’extracteur exact doit battre le juge sur les erreurs de parsing. Pour \(g\) : détection ≥80 % sur attractions plantées, fausses alertes ≤5 % sous doses permutées et déplacements constants. Sinon, on mesure l’instrument.

## (d) Ancrage matériel

Base commune : Llama-3.1-8B-Instruct, collection `maius/open-character-training` et code associé (**RAPPORTÉ**, pièce Ibrahim §3), sous réserve d’accès. Aucun checkpoint chaleureux publié ni chaîne publique avec RL n’est supposé.

Plan complet réutilisant E1 : **9 jours et 324 h-GPU** (**calcul** à partir des coûts illustratifs), sur GPU 80 Go (**supposé**). À 2 €/h-GPU (**illustratif**) : **648 € calcul**, hors annotation humaine.

**Priorité : E1.** Elle conditionne l’interprétation des deux autres.  
Elle tranche persistance/érosion avec un contrôle de dérive générique.  
Elle produit aussi les checkpoints nécessaires à E2 et E3.

**Échec possible :** accès aux poids refusé ou persona initiale non validée.  
RL trop destructeur ou trop faible pour produire un contraste interprétable.  
Juges non validés : arrêter plutôt que conclure sur du style.

FIN-DE-CELLULE

---

## E3-T1-conception-E.md (sha256 `cba590145a39b89bb04f73013986d39f9e9a1019869c2809f2bfa6458fd679fe`)

# Proposition E — Tester la persistance sans confondre chaleur et accord

**RAPPORTÉ — Pièce absente :** le texte exact de la page du mentor n’est pas servi ; je traite uniquement la direction rapportée.

**Convention :** les faits ci-dessous sont **RAPPORTÉS**, non vérifiés ici. Tous les protocoles, prédictions, seuils et budgets sont **HYPOTHÈSES** ; leurs chiffres sont **illustratifs, supposés**, non des résultats. Aucune recherche de nouveauté effectuée.

## A. Ce que la question suppose

- **HYPOTHÈSE :** une persona installée constitue un comportement mesurable hors des exemples d’entraînement, plutôt qu’un vocabulaire reconnaissable.
- **HYPOTHÈSE :** sa persistance sous un apprentissage par renforcement particulier renseigne sur d’autres récompenses. Je limiterais explicitement la conclusion au régime testé.
- **HYPOTHÈSE :** *Loving*, chaleur et sycophancie désignent des propriétés suffisamment proches. Il faut au contraire mesurer séparément soutien émotionnel, justesse et accord injustifié.
- **RAPPORTÉ :** les points de contrôle *Loving* sont annoncés, mais leur accès effectif n’est pas vérifié ; aucune chaîne publique complète comportant l’étape de renforcement recherchée n’a été examinée (pièce Ibrahim, §3–4).
- **RAPPORTÉ :** le travail sur la chaleur teste l’ajustement supervisé, pas cette persistance ; la taxonomie distingue notamment capitulation factuelle et cadrage implicite (Ibrahim, §1.1–1.2).

## B. Socle matériel et décisionnel commun

**HYPOTHÈSE — Plan proposé.** Partir de Llama-3.1-8B-Instruct et de son point de contrôle *Loving*, annoncé dans `maius/open-character-training` (disponibilité **RAPPORTÉE**, Ibrahim, §3). Conserver chaque modèle avant entraînement ; produire ensuite :

- un descendant entraîné par renforcement à récompense vérifiable sur des problèmes arithmétiques générés, avec réponses calculées mécaniquement ;
- un témoin sans mise à jour, évalué dans les mêmes conditions.

Employer les mêmes problèmes, budgets et hyperparamètres pour les deux modèles. Les descendants seront **nouvellement entraînés**, pas présentés comme publiés. Vérifier sur problèmes réservés que le renforcement améliore effectivement la justesse : sinon, « persistance après renforcement » serait une conclusion vide.

Les comparaisons portent sur le **paquet d’entraînement de caractère**, pas sur la chaleur seule : isoler celle-ci demanderait un entraînement témoin apparié.

**HYPOTHÈSE — Règle commune.** Chaque duel oppose des régions exclusives et exhaustives d’un paramètre. Un intervalle entièrement d’un côté du seuil falsifie l’autre région ; s’il traverse le seuil, verdict **indécis**, jamais « absence d’effet ». Intervalles regroupés par problème et par entraînement ; trois graines proposées.

### Candidate A — La persona survit-elle réellement ?

**HYPOTHÈSE — Mesure.** Évaluer avant/après sur 300 situations inédites de soutien, sans opinion à approuver. Annotation humaine aveugle : présence d’un soutien chaleureux, indépendamment de la longueur et de la justesse. Aucun juge génératif requis.

Soit \(W\) le taux de chaleur et \(G_t=W_{\text{Loving},t}-W_{\text{base},t}\). Si \(G_{\text{avant}}\) n’est pas nettement positif, arrêter : la manipulation initiale n’est pas établie.

- **H_A :** rétention \(R=G_{\text{après}}/G_{\text{avant}}\geq0,70\).
- **H_B :** \(R<0,70\).
- **Attendu :** \(R=+0,80\), soit une variation relative de −20 %.
- **Falsification :** borne supérieure sous 0,70 → H_A rejetée ; borne inférieure au-dessus → H_B rejetée.
- **Contrôle négatif :** questions factuelles sans enjeu affectif ; témoin sans mise à jour.
- **Piège :** des formules affectueuses suffisent au juge. Contrôle : paires de réponses de même longueur, opposant chaleur substantielle et simple formule introductive.

**RAPPORTÉ / ajout proposé :** Ibrahim §1.1 entraîne une persona chaleureuse par supervision ; cette expérience ajoute sa trajectoire après renforcement. Le contraire de l’attente indiquerait une érosion comportementale sous ce régime, pas l’effacement de toute représentation interne.

### Candidate B — La chaleur persistante conserve-t-elle son coût factuel ?

**HYPOTHÈSE — Mesure.** Utiliser 300 problèmes à réponse calculable, chacun avec et sans fausse croyance de l’utilisateur ; ajouter séparément le contexte triste inspiré des stimuli rapportés (Ibrahim, §1.1). Mesurer justesse, accord explicite et refus séparément ; aucun refus n’est transformé en réponse médiane.

Soit \(S\) l’excès d’erreur induit par la fausse croyance et \(D=S_{\text{Loving,après}}-S_{\text{base,après}}\).

- **H_A :** \(D\geq+5\) points ; **H_B :** \(D<+5\) points.
- **Attendu :** \(D=+8\) points.
- **Falsification :** intervalle entièrement au-dessus du seuil → H_B rejetée ; entièrement dessous → H_A rejetée.
- **Contrôle négatif :** même réponse fausse attribuée à une source impersonnelle ; croyance utilisateur correcte.
- **Piège :** déficit général de raisonnement. Contrôle : soustraction appariée de l’erreur sans croyance et analyse des refus.

**RAPPORTÉ / ajout proposé :** Ibrahim §1.1 rapporte déjà chaleur, contexte émotionnel et erreur ; l’ajout est leur maintien après renforcement. Un contraste inférieur au seuil exclurait un surcoût matériel défini ainsi, mais pas toute sycophancie.

### Candidate C — Une persona persiste-t-elle seulement dans la forme ?

**HYPOTHÈSE — Mesure.** Sur 200 dialogues de conseil à plusieurs tours, distinguer validation des émotions et validation injustifiée d’une conduite, à partir de situations entièrement spécifiées. Annotation humaine aveugle, chaleur annotée séparément.

Soit \(D_{\mathrm{social}}\) l’excès post-renforcement de validation injustifiée chez *Loving*.

- **H_A :** \(D_{\mathrm{social}}\geq+5\) points ; **H_B :** inférieur.
- **Attendu :** \(D_{\mathrm{social}}=+10\) points.
- **Falsification :** même règle d’intervalle.
- **Contrôle négatif :** situations appariées où la validation est justifiée.
- **Piège :** juger toute empathie sycophantique. Contrôle : paires conservant le soutien émotionnel mais changeant seulement l’approbation de la conduite.

**RAPPORTÉ / ajout proposé :** Ibrahim §1.5–1.7 traite ton constant, sycophancie sociale et plusieurs tours. L’ajout est la comparaison longitudinale après renforcement. Un résultat contraire favoriserait une dissociation entre chaleur conservée et approbation injustifiée.

## C. Validation minimale des instruments

**HYPOTHÈSE — Avant entraînement :**

| Instrument | Test minimal et référence à battre |
|---|---|
| Annotation chaleur/sycophancie | Banque réservée de 100 paires par construit, positives et honnêtes appariées en sujet, longueur et ton ; sensibilité visée ≥80 %, fausses alertes ≤5 %. Comparer à longueur et comptage lexical. |
| Extraction factuelle | Réponses correctes, incorrectes, ambiguës et refus ; mêmes objectifs. Battre ou égaler un parseur exact, sans réduire artificiellement les refus. |
| Récompense vérifiable | Cas corrects et incorrects appariés en format, vérifiés par calcul indépendant ; toute erreur détectée bloque l’entraînement. |

Un instrument qui échoue n’est pas compensé par davantage de générations.

## D. Budget et choix

**HYPOTHÈSE — Budgets illustratifs, supposés :** un GPU 80 Go, adaptations de faible rang ; entraînement commun : 60–120 heures de carte, 4–7 jours. Évaluation supplémentaire : A, 6–12 heures et 2–3 jours ; B, 8–16 heures et 2–4 jours ; C, 12–24 heures et 3–5 jours. Annotation humaine : budget distinct à établir.

### Première expérience retenue : A
Elle vérifie la prémisse nécessaire : une persona initialement détectable survit-elle à une optimisation effective ?  
Elle évite d’appeler « sycophancie » une simple chaleur, puis autorise B et C comme suites.

### Échec du plan
Accès aux poids impossible, persona initiale indétectable ou renforcement inefficace : arrêt.  
Juges non discriminants ou incertitude excessive : résultat indécis, sans conclusion de persistance.

FIN-DE-CELLULE

---

## E3-T3-reponse-A.md (sha256 `6d73a338cb14a16832a41deb6bf156fcb87224623377a1403d231b46ef5a1f6d`)

# Cellule A — Tour III.3 : réponse aux critiques

**Statuts.** Les faits des trois pièces restent **RAPPORTÉS** (lus sur page primaire par un rédacteur, non audités par moi) ; je ne tranche pas l'écart signalé par B entre mon classement (RAPPORTÉ) et celui de D (OBSERVÉ-NON-AUDITÉ) pour les chiffres des dépôts de Lazar, je le laisse à l'arbitre. Les critiques reçues sont des HYPOTHÈSES de méthode ; mes réponses aussi. Les chiffres non issus des pièces sont « illustratifs », « supposés » ou « calcul ». La pièce C est absente (jamais lancée) : rien à répondre.

Je ne réponds qu'aux sections visant A. Quand B, D et E font la même critique, je la traite une fois et renvoie.

---

## (a) Réponse critique par critique

### Critiques de B

**B1 — Statut de l'accès aux poids OCT.** *Acceptée.* La pièce dit « accès filtré annoncé, non vérifié » (pièce Ibrahim §3) : c'est une annonce RAPPORTÉE, personne n'a observé l'accès. Je corrige mon point (a)5 : RAPPORTÉ, et « poids inaccessibles » reste la première cause d'échec du plan.

**B2 — E1 : duel non exhaustif, seuil incohérent (≥ +11 contre 5), portée du +11 non établie.** *Acceptée sur les trois points* (même critique chez D, premier tiret, et E, « VÉRIFIÉ »). Le duel conjoint « erreur **et** g » laissait trois issues sans hypothèse. Correction en (b) : deux duels à un paramètre chacun, chacun avec une région « indécis » (règle d'E, reprise en le disant). Le « +11 » (*Nature* p. 1163, RAPPORTÉ, portée non établie, pièce Ibrahim §4) ne sert plus d'attendu pour Llama-3.1-8B ; il ne reste qu'un ordre de grandeur cité. Le seul chiffre du papier propre au 8B est −15,06 sous tristesse + fausse croyance (tableau E5, prépublication v2, RAPPORTÉ, non revérifié dans *Nature*) ; je ne l'utilise pas comme attendu non plus, car il combine deux manipulations.

**B3 — Δg ≥ 0,2 étiqueté « calcul » alors que c'est un choix ; variance inter-points-de-contrôle plus grande ; puissance ≈ 50 %.** *Acceptée.* Je réétiquette : δ_g = 0,2 est un **effet minimal d'intérêt supposé**, pas un calcul. Le dimensionnement devient une cible de demi-largeur d'intervalle de 0,1 sur le contraste entre points de contrôle ; sous l'hypothèse de B (variance au moins double d'un contraste intra-modèle, demi-largeur 0,21 à 450 générations par dose dans R6, calcul à partir de 1 350 = 3 doses × 450, pièce sycophancie §1), il faut environ 4 à 8 fois plus de générations par bras, soit 1 800 à 3 600 par bras et par dose (calcul, illustratif). Je l'inscris au budget d'E1.

**B4 — Le contrôle par consigne système prouve autre chose.** *Acceptée* (même point chez D et E). Égalité des déplacements entre persona entraînée et base consignée montre une équivalence de deux interventions, pas que le juge lit le style. Et une sortie réellement chaleureuse classée *Loving* est une détection, pas une fausse alerte : B a raison, ma définition en (c) confondait « style induit par consigne » et « absence du construit ». Correction : le vrai négatif devient la **paire contenu/style** (même position, style varié ; même style, position variée), annotée par des humains (contrôle B(c)1 = D(c)1 = E(c) « persona versus style », repris en le disant). Le bras consigné est conservé, mais comme question distincte (« la consigne reproduit-elle l'effet de l'entraînement ? »), sans inférence sur l'instrument.

**B5 — Fuite entre construction de l'instrument et évaluation ; la troncature est elle-même un artefact.** *Acceptée.* Le classifieur OCT est à base de modèles avec biais et circularité déclarés (pièce Ibrahim §2) ; toute dérive de format sous RLVR se lirait comme érosion. Correction : banque de validation **réservée**, construite en deux phases (avant RL ; après RL, sur sorties post-RL réelles, avant toute levée d'aveugle sur E2), avec paires contenu/style. La concordance tronqué/entier est **abandonnée** : E a raison qu'elle peut accepter deux instruments biaisés ; l'analyse principale porte sur les sorties entières.

**B6 — Régression vers la moyenne dans ĝ.** *Transformée en test.* La pièce sycophancie ne dit pas si R6 estime v₀ sur des tirages disjoints de ceux de Δ ; je ne le suppose pas. Correction : v₀ estimé sur une moitié des tirages, Δ sur l'autre (division fixée d'avance) ; **dose nulle placebo** (deux lots sans pression, même estimateur) qui doit donner ĝ ≈ 0 ; simulation avec l'atténuation d'E, ĝ → (g·Var(V) + Var(ε)) / (Var(V) + Var(ε)), alimentée par la variance entre tirages mesurée sur le modèle réel. Si le placebo donne ĝ hors de [−0,1 ; 0,1] (supposé), l'instrument g est déclaré non utilisable pour cette persona.

**B7 — E2 : la falsification ne suit pas (H_B par rétention seule ; R8 non réfuté ; R8 vise Tülu 3 ; zone 50–80 % vide).** *Acceptée* (même point chez D, quatrième tiret, et E). Je retire la prétention de « réfuter l'a priori R8 ». E2 teste la **condition S3** (« RLVR ne change pas g », pièce sycophancie §2, préenregistrée, non exécutée) sur une **autre chaîne** (OCT, déjà passée par DPO) : c'est un test de généralité, pas une réfutation ; un Δg ≥ δ sous RLVR contredirait seulement une version exclusive de « le gain vient de l'optimisation des préférences ». E2 est scindé en deux duels à un paramètre, sans zone vide (voir (b)).

**B8 — Persistance vraie par construction si le RLVR ne bouge presque pas la politique.** *Acceptée, transformée.* L'axe de dose devient la **divergence KL mesurée sur les prompts d'évaluation** (persona et sycophancie), avec arrêt à trois cibles de KL, et non un nombre de pas ; un départ qui n'atteint pas la cible minimale rend son bras non jugeable.

**B9 — E3 : facteurs confondus, paires rééquilibrées = troisième modalité, seuil d'interaction sous-dimensionné.** *Acceptée.* Le modèle de récompense rééquilibré est une intervention, pas un contrôle (D le dit aussi) ; le contrôle négatif devient le modèle de récompense **à préférences permutées** (B(c)5, repris en le disant), apparié en KL. L'interaction passe au second plan : E montre que mon duel annonçait des effets principaux et testait une interaction ; E3 teste désormais l'effet principal de l'étape sur g et F, persona en bloc. Le facteur √2 de B sur l'interaction est accepté comme calcul.

**B10 — Dérive du juge (alias non figé).** *Acceptée.* Jeu d'ancrage rejugé à chaque passe (B(c)4) ; sorties avant/après mélangées dans les mêmes lots de jugement ; juge principal à version figée : un juge à poids ouverts d'une autre famille est déjà nommé dans les préenregistrements R1a/R1b (Qwen2.5-72B, pièce sycophancie §1, RAPPORTÉ) ; GPT-4o et Claude en juges secondaires.

**B(b) — Fieller, saturation, Var(v₀) → 0, déplacement constant, refus, graines.** *Acceptés.* Rétention : la **différence brute** (contraste persona–base après moins avant) devient l'analyse principale, le ratio est secondaire et n'est publié que si l'intervalle de C_avant exclut 0 (même exigence chez D et E). Saturation du classifieur : critère d'arrêt écrit d'avance en E0. Gain : le modèle d'attraction est opposé au modèle à déplacement constant (cas Qwen/Mistral en R3, pièce sycophancie §1) avant toute lecture de g. Refus : analyse principale avec le refus comme **catégorie explicite** (E(c), D(b)) ; analyse secondaire avec exclusion commune par item fixée sur l'union des bras (B) ; je note que cette seconde règle conditionne encore sur une variable post-traitement, symétriquement, d'où son rang secondaire. Graines : K = 3 entraînements par cellule ; j'accepte le calcul de B/D (t à 2 degrés de liberté ≈ 4,30, facteur ≈ 2,2) et je le prends comme coût ; K = 5 si le budget le permet (illustratif).

**B(c)3 — Test-retest à la place de l'autodistillation.** *Acceptée comme ajout, rejetée comme substitution.* Le test-retest d'un point de contrôle gelé mesure le plancher de bruit de l'instrument ; l'autodistillation mesurait l'exposition aux prompts. Ce sont deux rôles. Mais D a raison que l'autodistillation n'apparie ni gradients ni distance : elle est rétrogradée en bras secondaire, et le témoin principal devient la récompense non informative appariée en KL (D(c)2, E(c) « effet propre du RL »).

### Critiques de D (points non encore traités)

**Information de construit I(Y;Ŷ | X,Z,T) > 0 et non-transport des taux avant/après.** *Acceptée, transformée.* La banque réservée de E0 contient des paires contenu/style **post-RL** ; détection et fausse alerte sont réestimées dans le régime post-RL, pas transportées.

**Corrélations intra-item / intra-graine : taille effective inférieure au nombre de générations.** *Acceptée.* Modèle hiérarchique (item, graine d'entraînement, tirage) pour tous les intervalles ; aucun intervalle calculé sur générations indépendantes.

**Dépasser un lexique en AUC n'établit pas que le classifieur lit autre chose que Z.** *Acceptée* (E le formalise : égalité d'AUC n'implique pas égalité de lois). Correction : le classifieur est testé **conditionnellement** sur les paires de E0 (à style constant, sépare-t-il les positions ? à position constante, le style ?). Le résultat dit ce que l'instrument lit, dans l'un ou l'autre cas ; un instrument qui ne lit que le style reste utilisable pour mesurer la persistance **du style**, à condition de le nommer ainsi.

**Croyance correcte et assertion fausse de source impersonnelle (D(c)3).** *Acceptée.* La pièce Ibrahim ne dit pas si la tâche de désinformation du papier chaleur contient ces contrastes ; ils sont à construire sur les mêmes items.

### Critiques d'E (points non encore traités)

**c = a/g non borné si g plausible contient 0.** *Acceptée.* Le point fixe n'est rapporté que si l'intervalle de ĝ exclut 0 ; sinon seul le déplacement moyen est publié.

**Sondes : AUC de construction sans borne sur l'AUC d'évaluation.** *Acceptée.* Les sondes restent hors du plan principal ; si on les ajoute, AUC sur un point de contrôle jamais vu et plancher de sondes aléatoires appariées (procédé P3, pièce nos-résultats §6, RAPPORTÉ), sur lots réservés.

**Rien n'est rejeté sur le fond** ; les deux rejets partiels (B4 sur la définition de fausse alerte, B(c)3 sur la substitution) sont notés ci-dessus avec leur raison.

---

## (b) Expériences corrigées

Modèle : Llama-3.1-8B-Instruct ; points de contrôle OCT *Loving*, *Sycophantic* (pièce Ibrahim §3, accès RAPPORTÉ non vérifié). Toutes les règles de décision, seuils et divisions d'échantillon sont écrits avant toute génération ; verdict « indécis » si l'intervalle (modèle hiérarchique) chevauche le seuil.

### E0 — Instruments (nouveau ; conditionne tout)

*Mesure.* Banque réservée en deux phases : (i) avant RL, 300 paires contenu/style (même position, style chaleureux/neutre ; même style, position capitulation/correction), produites par réécriture puis **adjudication humaine du maintien du sens** (deux annotateurs, κ rapporté ; illustratif) ; (ii) après l'entraînement d'E2, 300 paires analogues tirées des sorties post-RL réelles, annotées avant levée d'aveugle. Test-retest : chaque point de contrôle gelé évalué deux fois (plancher de bruit). Jeu d'ancrage de 50 sorties rejugé à chaque passe. Placebo dose nulle pour ĝ.
*Duel instrument persona.* H_A : le classifieur OCT sépare les positions à style constant (AUC ≥ 0,7, supposé) ; H_B : il ne sépare que le style (AUC à style constant ≤ 0,6). Issue H_A : « persistance de la persona » signifie persistance d'une disposition ; H_B : elle signifie persistance d'un registre, et tout le vocabulaire des résultats change en conséquence. Entre les deux : indécis, plus de paires.
*Duel juge de sycophancie.* Même structure ; repère d'accord juge/humains : 90,2 % / 86,0 %, κ 0,814 / 0,733 (prépublication, annexe D.1, RAPPORTÉ ; 235 contre 470 annotations non réconciliées). Le κ = 0 à accord brut 0,92 (pièce nos-résultats §4, RAPPORTÉ) justifie de ne pas se contenter de l'accord brut ; D note aussi que κ est instable à prévalence extrême : prévalence rapportée.
*Trompeur.* Les paires réécrites ne couvrent pas les formats réellement produits après RL : d'où la phase (ii).
*Coût.* 3 jours, 0 heure de carte, ~1 200 annotations humaines (illustratif).

### E1 — Étalonnage : que déplace la persona *Sycophantic* ?

*Mesure.* Sans entraînement. Trois points de contrôle (*Sycophantic*, *Loving*, base) plus la base consignée. Tâche de désinformation avec fausse croyance, croyance correcte et assertion impersonnelle (contrastes à construire) ; protocole de pression dosée (30 items × 3 conditions, pièce sycophancie §1) avec v₀ sur tirages disjoints ; refus en catégorie explicite.
*Duel D1 (factuel).* Paramètre ΔF = excès d'erreur sous fausse croyance (persona − base), net de l'excès sous croyance correcte. H_A : ΔF ≥ 5 points (supposé) ; H_B : ΔF < 5. Issue H_A : la persona porte une capitulation factuelle ; issue H_B : elle n'en porte pas à cette taille, ce qui réfute « une persona *Sycophantic* capitule sur les faits » et ne laisse à mesurer en E2 que le volet social.
*Duel D2 (gain).* Paramètre Δg (persona − base), après test préalable attraction contre déplacement constant sur chaque modèle. H_A : Δg ≥ 0,2 (supposé) ; H_B : Δg < 0,2. Non jugeable si l'un des modèles est à déplacement constant ou si le placebo échoue.
*Lecture croisée.* Les quatre cellules (D1 × D2) sont toutes interprétables : « les deux » contredit la dissociation sociale/factuelle sous persona (taxonomie §1.2 et sondes §1.4, RAPPORTÉ, prédisent plutôt une cellule mixte) ; « aucun » renvoie à E0 (instrument) ou dit que cette persona est inerte sur ces instruments.
*Déjà fait / ajout.* Papier chaleur : SFT chaleureux sur ces tâches (§1.1) ; OCT : pas de mesure de sycophancie de sa persona (§2). Ajout : persona DPO+SFT sur deux instruments, avec les contrôles de croyance correcte et de régression vers la moyenne.
*Attendu (HYPOTHÈSE, signé).* ΔF entre +3 et +8 points, Δg entre 0 et +0,15 (illustratifs) : plutôt cellule « factuel sans gain », donc fragmentation.
*Trompeur.* Refus notés au milieu (R6 : points fixes 2,60 contre 1,92/2,03 sans les 14 items à refus, pièce sycophancie §1) ; contrôle : catégorie explicite.
*Coût.* 3 jours, 0 heure de carte, ~10 000 à 15 000 générations jugées (calcul d'après B3, illustratif).

### E2 — Persistance sous RLVR

*Entraînement.* Départs : *Loving*, *Sycophantic*, base. Bras : RLVR (récompense exacte sur problèmes vérifiables, recette de type Tülu 3, travail non identifié hors pièce sycophancie §2) ; récompense **non informative** (étiquettes permutées), mêmes prompts, même algorithme, arrêt à la même KL ; gelé (test-retest). K = 3 graines par cellule ; LoRA. Trois doses définies par KL cible sur les prompts d'évaluation (petite, moyenne, forte ; valeurs fixées après un essai pilote non analysé). Contrôle positif : justesse vérifiable +5 points (supposé) **et** KL cible atteinte ; sinon bras non jugeable. Bras secondaire : autodistillation SFT (exposition aux prompts), sans rôle dans les duels.
*Mesure.* Avant/après, mêmes lots mélangés : score persona (validé en E0, phase ii), ΔF, g et point fixe, niveaux absolus de chaque modèle, refus en catégorie.
*Duel P (persona).* Paramètre : d₁ − d₀, où d_t = contraste persona − base à l'instant t, dans le bras RLVR net du bras non informatif à KL égale, dose forte. H_A : la perte est inférieure à 30 % de d₀ (supposé, exprimé en différence brute, pas en ratio) ; H_B : elle dépasse 30 %. Issue H_A réfute « le RLVR écrase ce qu'installe l'entraînement de caractère, à cette KL » ; issue H_B réfute « la persona est stable sous un RL sans préférences humaines ». Si la perte est identique dans le bras non informatif, elle vient de la mise à jour générique, pas de la récompense : conclusion distincte, écrite d'avance.
*Duel G (gain).* Paramètre Δg = g_RLVR − g_non-informatif à KL égale. H_A : |Δg| < 0,2 ; H_B : |Δg| ≥ 0,2 ; indécis si chevauchement. H_A est compatible avec la condition S3 de R8 sur une seconde chaîne ; H_B dit qu'un RL sans préférences humaines déplace le gain, ce qui contredit une lecture exclusive de l'a priori R8, sans l'attribuer.
*Déjà fait / ajout.* Rien sur la persistance après entraînement ultérieur (pièce Ibrahim §2) ; R8 non exécuté (pièce sycophancie §2). Ajout : première chaîne persona → RL mesurée, avec dose en KL et témoin apparié.
*Attendu (HYPOTHÈSE, signé).* Perte 10–30 % du contraste persona à la dose forte, Δg dans [−0,1 ; +0,1], ΔF dans [−2 ; +2] (illustratifs).
*Trompeur.* Dérive de mesure : le classifieur et le juge lisent le changement de format post-RL ; contrôle : phase (ii) d'E0 et jeu d'ancrage ; la persistance « vraie par construction » : contrôle : KL cible et bras non informatif.
*Coût.* 3 départs × 2 bras entraînés × 3 graines = 18 entraînements, doses par points de contrôle intermédiaires ; 50–90 heures H100 (illustratif) ; ~30 000 générations jugées ; 8 à 10 jours.

### E3 — Attribution : étape à préférences contre RLVR (troisième rang)

*Entraînement.* Blocs persona {*Loving*, aucune} × étape {RLVR ; RL sur modèle de récompense appris sur paires de préférences ; RL sur modèle de récompense à **étiquettes permutées**}, appariés en KL, K = 3.
*Duel.* Paramètre : effet principal β_T de l'étape (préférences − RLVR) sur g et sur ΔF, persona en bloc. H_A : β_T ≥ 0,2 sur g (supposé) ; H_B : < 0,2. Issue H_B réfute, sur ce modèle et cette récompense, la cause désignée par 88,7 % des 106 experts (§1.2, RAPPORTÉ comme croyance) ; issue H_A la soutient sans l'établir. Interaction persona × étape : secondaire, avec le facteur √2 de B accepté.
*Contrôle.* Validation humaine du modèle de récompense sur 200 paires (illustratif) ; les réponses préférées de PRISM/UltraFeedback/LMSys contiennent plus de validation (§1.6, RAPPORTÉ) : on mesure donc la préférence encodée dans ces données, et on le dit.
*Coût.* 10 jours, ~120 heures H100 (illustratif).

---

## (c) Réponse à l'arbitre

**Ce qui est établi (RAPPORTÉ, non audité par moi).** Un SFT chaleureux sur Llama-3.1-8B-Instruct, parmi d'autres modèles, dégrade la justesse sous fausse croyance et sous tristesse (papier chaleur, §1.1) ; seul le SFT y est testé, le rôle des préférences y est supposé. L'entraînement de caractère ouvert (OCT) installe des personas dont *Loving* et *Sycophantic* par DPO puis SFT, sur le même modèle, sans mesurer la sycophancie de ses personas ni leur persistance (§2). La sycophancie est un construit fragmenté (§1.2) ; son pilotage marche mieux sur le social que sur le factuel (§1.4). Sur ce modèle, la note sous pression sociale suit une loi d'attraction propre à la famille, mesurée en dose (R6, pièce sycophancie §1), et une lecture par sonde n'est pas causale (§3). Aucune chaîne publique persona → RL n'a été lue ; R8 est préenregistré et non exécuté.

**Ce qui n'est pas établi.** Que les poids OCT soient accessibles (annonce RAPPORTÉE). Que le classifieur de persona OCT lise autre chose que le style, et que les juges de sycophancie soient stables entre régimes avant et après RL. Que « persona » et « sycophancie » soient mesurables indépendamment l'un de l'autre sur un même modèle. Que la persistance observée sous un RL court ne soit pas une absence de déplacement de politique. Que l'optimisation par préférences cause la sycophancie (croyance d'experts, pas un fait).

**L'expérience à faire en premier : E0 puis E1, trois jours chacune, sans heure de carte.** On mesure, sur les points de contrôle publiés *Sycophantic*, *Loving* et la base, (i) si les instruments séparent position et style sur des paires humaines réservées, avec test-retest et placebo dose nulle, puis (ii) ce que la persona déplace : l'excès d'erreur sous fausse croyance net de la croyance correcte (duel D1, seuil 5 points supposé) et le gain d'attraction avec v₀ sur tirages disjoints (duel D2, seuil 0,2 supposé), refus en catégorie explicite. Résultat attendu (HYPOTHÈSE, signé) : excès d'erreur +3 à +8 points, gain inchangé à ±0,15 (illustratifs), donc une persona qui capitule sur les faits sans changer le gain social. Ce qui rendrait le résultat trompeur : un classifieur ou un juge qui lit le registre et non la position, ce que la phase de paires contenu/style d'E0 détecte ; et une régression vers la moyenne dans ĝ, que le placebo détecte. Un résultat contraire (rien ne bouge) dirait soit que les instruments sont aveugles (E0 tranche), soit que la persona est inerte sur ces mesures, et E2 n'aurait alors pas de signal avant-RL à conserver : il faudrait réentraîner une persona ou changer d'instrument avant de dépenser une heure de carte. Seulement ensuite E2, qui répond mot pour mot à la direction du mentor, avec dose en KL, témoin à récompense non informative, trois graines par cellule et verdict « indécis » admis.

**Ce qui ferait échouer le plan.** Poids OCT inaccessibles (réentraînement par la recette publique, +3 jours, sans ancrage sur les points de contrôle du papier). E0 en échec : instruments qui ne lisent que le style, ou test-retest au-dessus de l'effet attendu ; alors aucune persistance n'est lisible, et E0–E1 sont publiés comme résultat négatif sur les instruments. Bras RLVR qui n'atteint pas la KL cible ou le contrôle positif : E2 non jugeable, retour à une dose-réponse.

FIN-DE-CELLULE

---

## E3-T3-reponse-B.md (sha256 `83b473c98a5a19408e612e707cd836d687e1cc8001d10f10fd469c2d7af798e6`)

# Proposition B, tour III.3 : réponse aux critiques

**Pièces manquantes.** La critique croisée C est absente (jamais lancée) ; je n'en suppose aucun contenu. Le texte de la page du mentor n'est pas servi non plus.

**Statuts.**
- Les faits tirés des papiers sont RAPPORTÉ.
- Les résultats des dépôts publics de Lazar sont OBSERVÉ-NON-AUDITÉ. Au tour III.1, je les avais marqués RAPPORTÉ. Les pièces ne leur attribuent aucun statut explicite, la proposition A les classe OBSERVÉ-NON-AUDITÉ, et je retiens le moins fort des deux.
- Mes réponses, corrections et prédictions sont HYPOTHÈSE.
- Mes seuils et mes coûts sont « supposé » ou « illustratif » ; les dérivations sont marquées « calcul ».

---

## (a) Réponse critique par critique

Codes : **A-**, **D-** et **E-** renvoient à la proposition qui critique ; le chiffre ou la lettre renvoie à sa section.

### Défauts partagés signalés par A

| Critique | Verdict | Traitement |
|---|---|---|
| **A-Σ1.** La persistance serait vraie par construction : pénalité KL vers la persona, adaptation de rang faible sur des mathématiques. | **Rejetée comme certitude, transformée en test.** Le sous-espace « disjoint » est lui-même une hypothèse : l'adaptateur RL et la persona fusionnée (`maius`, points de contrôle fusionnés, piece-ibrahim §3) touchent les mêmes couches. Le risque est réel. | Deux bras : β = 0 et β_réf. La politique de référence est déclarée : c'est le point de contrôle de départ. Sous β_réf, je **prédis** \|ΔC\| < 0,1 (supposé). Cela sert de contrôle interne de l'argument de A. |
| **A-Σ2.** Le ratio r est instable quand son dénominateur est bruité. | **Acceptée.** | L'estimand principal devient une **différence**. r n'est rapporté qu'à titre descriptif, et seulement si l'IC de C_avant reste loin de 0. Les niveaux absolus de chaque modèle sont publiés (E-b : une perte commune laisse r inchangé). |
| **A-Σ3.** La version du juge est confondue avec le passage avant/après. | **Acceptée.** | Juge figé par version. Les sorties avant et après sont notées dans la **même passe, entrelacées**, avec des sorties ancres répétées (repris de D-c2, adressé à E). |

### Critiques propres à B

| Critique | Verdict | Traitement |
|---|---|---|
| **A-1, D-a1, E-a2.** Mon attendu r ≈ 0,6 tombait dans la zone « non tranché ». | **Acceptée.** C'est le défaut principal de ma conception. | Le duel est reparamétré : érosion d'au moins δ contre équivalence à ±δ (voir b). L'attendu (ΔC ≈ −0,2, supposé) se trouve dans une région décisive. La taille de l'expérience est fixée par un pilote pour que ce soit tenable. |
| **A-2, D-a5, E-a5.** Le SFT neutre est apparié sur le nombre de pas, et des gains mathématiques égaux n'impliquent pas des déplacements égaux. | **Acceptée.** | Points de contrôle intermédiaires. KL(π ‖ π₀) est mesurée sur des invites conversationnelles tenues à l'écart. Les bras sont comparés **à KL égale**, sur une courbe érosion–déplacement, et non à pas égaux. |
| **A-(c), D-c3, E-b.** Il manque une récompense non informative pour E1, et cette récompense peut ne rien optimiser. | **Acceptée.** | Bras « récompense permutée », mêmes invites, même optimiseur. On vérifie qu'il produit un déplacement KL réel ; sinon, il est déclaré inopérant. |
| **E-c.** Il manque un bras sans mise à jour. | **Acceptée.** | Bras gelé, réévalué à chaque passe : il mesure la dérive de l'instrument. |
| **A-3.** Recouvrement construit entre persona et sycophancie ; classifieur peut-être évalué sur ses données de construction ; circularité importée. | **Acceptée.** | Classifieur d'une autre famille que le professeur (GLM 4.5 Air, piece-ibrahim §2). Construction sur des données disjointes des 12 000 transcriptions. Évaluation sur un lot réservé. J'ajoute des items de chaleur **sans opinion à approuver** : idée de la proposition E, que je reprends telle que A la rapporte. |
| **A-4, D-a4, D-c2.** Un reformatage artificiel ne représente pas le format réellement produit après RL. | **Acceptée.** | Nulle de format : Instruct avant et après le même RL. Validation sur des **sorties post-RL réelles** de chaque bras. Paires à position constante et ton, format ou longueur variables (E-c). |
| **E-a3.** La rétention dépend de l'échelle du classifieur. | **Acceptée.** | Mesure principale : une étiquette binaire « persona présente », à seuil calibré sur annotation humaine. En secondaire, une AUC persona contre base, invariante par transformation monotone. Je signale sa saturation près de 1 (A-b). |
| **A-9.** Juge validé hors distribution. **A-(b), E-b.** Atténuation différentielle selon le bras. | **Acceptée.** | Annotation humaine aveugle **par bras**, y compris après RL. Sensibilité s et spécificité p estimées par bras. Correction π = (π* + p − 1)/(s + p − 1), d'après la formule de A. |
| **D-a3, E-a4, E-b.** Cas positifs circulaires : les sorties de *Sycophantic* prises comme vérité. | **Acceptée.** | Les cas positifs sont définis par une **annotation comportementale aveugle**, sans connaître le point de contrôle. On y ajoute des accords justifiés et des désaccords injustifiés (E-c). |
| **D-b.** Le kappa est instable quand la prévalence est extrême. | **Acceptée.** | Je rapporte s, p et l'accord par classe. Le kappa seul n'est plus un critère. |
| **A-8, D-a2, E-a6.** E4 est un contrôle positif ; ses thèses « ton / disposition » dépassent ce qu'il mesure ; l'ordre imposé à *Loving* crée une issue non assignée. | **Acceptée en partie.** Je retire les thèses et l'ordre. Je **rejette** l'idée qu'une issue H_A n'apprendrait rien : Open Character Training n'a pas mesuré la sycophancie de *Sycophantic* (RAPPORTÉ, piece-ibrahim §2). | E4' devient le contrôle positif de la **manipulation** et de l'instrument (voir b). |
| **D-c4.** Il manque la croyance correcte et la source impersonnelle dans E4. | **Acceptée.** | Quatre conditions : sans croyance, croyance correcte, croyance fausse de l'utilisateur, même affirmation fausse d'origine impersonnelle. |
| **D-b.** La manipulation peut être inerte, ou l'erreur peut être au plafond, ce qui rend H_B vraie par construction. | **Transformée en test.** | Prérequis déclaré : l'erreur sans croyance doit se situer entre 0,1 et 0,9 (supposé). Sinon, E4' est déclaré non jugeable, et non H_B. |
| **E-a1.** E3 confond v₀ (valeur initiale de l'item) et c (point fixe). | **Acceptée.** C'est une erreur de ma part. Dans Δ = g·(c − v₀), le point fixe est c (OBSERVÉ-NON-AUDITÉ, piece-sycophancie §1). | Les hypothèses d'E3' portent désormais sur c et g. v₀ devient une covariable mesurée sur des tirages indépendants. |
| **A-7.** Pas de test de spécification de la loi. | **Acceptée.** | Le modèle concurrent à déplacement constant est ajusté **avant** toute lecture de Δg. S'il l'emporte sur *Loving*, E3' est déclaré non applicable (même cas que R3). |
| **D-b, E-b.** Identifiabilité de g et c, et atténuation par l'erreur de mesure sur v₀. | **Transformée en test.** | Simulation de récupération de paramètres avant les données réelles. Deux générateurs : c constant et v₀ variable, puis v₀ constant et c variable, avec erreur de mesure. g est partagé entre items dans un modèle hiérarchique, et non estimé item par item. |
| **A-(b).** La résolution d'E3 est inférieure à mes seuils (demi-largeur ≈ 0,2 au volume de R6). | **Acceptée.** | Volume ×4, ce qui ramène la demi-largeur à ≈ 0,1 (calcul : (0,2/0,1)², à partir de A) ; seuils relevés. |
| **D-a7.** Les générations d'E1 ne servent pas à E3. | **Acceptée.** | E3' a son propre protocole dosé, sur les **mêmes points de contrôle** et non sur les mêmes générations. Le coût marginal annoncé au tour III.1 était faux. |
| **A-5, D-a6, E-b.** Appariement sur la longueur, variable post-traitement. | **Acceptée.** | E2 est reportée. Si elle est jouée, la pénalité de longueur est déclarée d'avance dans la récompense, et l'analyse marginale sur sorties intégrales est l'analyse principale. |
| **A-6.** Le modèle de récompense d'E2 peut favoriser la validation. | **Transformée en test.** | Prérequis d'E2 : sonder le modèle de récompense par des paires minimales qui ne diffèrent que par les mots de validation, ou que par la longueur. Si la récompense suit ces paires, l'amplification est un artefact de construction, déclaré comme tel. |
| **A-(b).** E2 demande n ≈ 17 000 par cellule sans appariement (calcul de A). | **Acceptée.** | E2 n'est pas jugeable au premier tour. |
| **A-(b), D-b, E-a, E-c.** Refus exclus, ce qui revient à conditionner sur une variable post-traitement. | **Acceptée.** | Le refus devient une catégorie explicite. Analyse principale marginale, avec bornes de pire cas : refus compté juste, puis faux. Analyse conditionnelle en secondaire. |
| **A-(b), E-b.** Trois graines donnent deux degrés de liberté ; la variance entre entraînements domine. | **Acceptée.** | Pilote à deux graines pour estimer σ_entraînement. K est fixé d'avance par calcul (voir b). |
| **A-10.** Multiplicité des tests. | **Acceptée.** | Un estimand principal (Duel 1 d'E1'). Tous les autres sont secondaires, avec correction de Holm. |
| **A-(b).** Saturation de l'échelle. | **Acceptée.** | Prérequis : P(persona \| Instruct) doit être non nulle pour estimer la nulle de format. Lecture en logit en secondaire. |
| **A-E-a2.** Fuite de domaine entre récompense et évaluation (critique adressée à E). | **Reprise, en le disant.** | L'évaluation de la sycophancie porte uniquement sur des items non mathématiques : désinformation et phrases émotionnelles (piece-ibrahim §1.1). |

---

## (b) Expériences corrigées

### Temps zéro (porte, 1 jour) : E4' et validation des instruments

- **Ce qu'on mesure.** Instruct, *Loving* et *Sycophantic* (sous réserve d'accès, piece-ibrahim §3), sans entraînement, dans les quatre conditions de croyance (D-c4), sur la tâche de désinformation et les phrases émotionnelles (§1.1).
- **Duel.**
  - H_A, « la manipulation a prise » : pour *Sycophantic*, erreur(fausse croyance de l'utilisateur) − erreur(sans croyance) ≥ 10 points, **et** cet écart dépasse de ≥ 5 points celui de la source impersonnelle (supposé). Cette issue falsifie « instrument ou point de contrôle inerte ».
  - H_B : écart < 3 points (supposé). Cette issue falsifie « *Sycophantic* capitule factuellement sur ces items ». Le volet factuel d'E1' est alors déclaré non jugeable, et la mesure bascule vers la sycophancie sociale (§1.6).
  - Prérequis : erreur sans croyance entre 0,1 et 0,9 (supposé).
- **Instruments, dans la même journée.**
  - Annotation humaine aveugle, deux annotateurs, ≈ 300 sorties (illustratif), tirées d'un lot réservé.
  - s et p rapportés séparément pour le juge et pour le classifieur de persona.
  - Le classifieur doit battre trois prédicteurs mécaniques : longueur, présence d'une chaîne de raisonnement, compte lexical des mots de validation.
- **Coût illustratif.** ≈ 10 heures de carte et ≈ 1 jour.

### E1' (principale) : érosion de la persona sous RLVR, comparée à KL égale

- **Départs.** Instruct et *Loving*. *Sycophantic* n'est utilisé qu'au temps zéro.
- **Bras, pour chaque départ :**
  - (i) gelé ;
  - (ii) RLVR mathématique, β = 0 ;
  - (iii) RLVR, β_réf, référence = départ ;
  - (iv) récompense permutée, β = 0 ;
  - (v) SFT neutre.
- **Points de contrôle.** Plusieurs étapes par course. KL(π ‖ π₀) est mesurée sur des invites conversationnelles tenues à l'écart.
- **Estimand principal.**
  - C_t = P(persona | *Loving*, t) − P(persona | Instruct, t), après correction par (s, p) estimés par bras.
  - ΔC = C_après − C_avant, dans le bras (ii) en fin de course.
  - Le passage Instruct avant → après sert de nulle de format : un effet de format commun aux deux modèles s'annule dans C.

**Duel 1 (principal).** δ = 0,1 en proportion (supposé).

| Issue de l'IC95 de ΔC | Verdict |
|---|---|
| Entièrement sous −δ | H_A « le RLVR érode la persona » est retenue ; H_B est falsifiée. |
| Entièrement dans ]−δ ; +δ[ | H_B « pas d'érosion d'ampleur δ » est retenue ; H_A est falsifiée. |
| Entièrement au-dessus de +δ | Amplification : falsifie les deux. Issue déclarée d'avance. |
| Autre | Non concluant, déclaré d'avance. |

**Duel 2 (secondaire, Holm).** À KL appariée par tranches :
- H_A « effet propre de la récompense » : l'érosion sous RLVR dépasse de ≥ δ celle de la récompense permutée et celle du SFT neutre.
- H_B « l'érosion est fonction du déplacement seul » : différences dans ±δ.
- Chaque issue falsifie l'autre.

**Résultat attendu (supposé, signé).**
- C_avant ≈ +0,6 (illustratif).
- Bras (ii) : ΔC ≈ −0,2, soit une érosion.
- Bras (iii) : |ΔC| < 0,1, ce qui confirmerait l'argument A-Σ1.
- Duel 2 : H_B attendue. Une récompense mathématique ne contient rien sur la persona ; je prévois une érosion générique liée au déplacement.
- Volet sycophancie (secondaire, uniquement si E4' donne H_A) : l'écart *Loving* − Instruct sur fausse croyance + tristesse **garde son signe** après RL. Pour repère hors chaîne : −15,06 points de justesse sous SFT de chaleur (RAPPORTÉ, tableau E5, §1.1).

**Ce qui rendrait le résultat trompeur, et son contrôle.**
- *Dérive de format ou de juge* lue comme une érosion. Contrôles : nulle Instruct, (s, p) par bras sur sorties post-RL réelles, notation entrelacée, bras gelé.
- *Refus différentiels.* Contrôle : bornes de pire cas.
- *Persistance artificielle due à β.* Contrôle : bras β = 0.

**Puissance.**
- La demi-largeur visée est ≤ 0,08 (supposé), pour que l'attendu −0,2 sorte de la zone non concluante.
- Avec K graines, demi-largeur ≈ t_{K−1}·s/√K. À K = 5, cela fait 1,24·s, d'où s ≤ 0,065 entre graines (calcul sur valeurs supposées).
- Le pilote mesure s. Si K > 8 serait nécessaire (illustratif), je supprime le bras (v) avant de réduire K.

**Coût illustratif.**
- Pilote : 10 h.
- Courses : 2 départs × 5 bras entraînés ou gelés × 5 graines, ≈ 40 courses entraînées × ≈ 5 h, soit ≈ 200 h.
- Évaluation : ≈ 20 h.
- Annotation : ≈ 600 sorties × 2 annotateurs.
- Durée : ≈ 7 à 8 jours.

### E3' (secondaire) : point fixe c ou gain g

- **Ce qu'on mesure.** Protocole dosé au format de R6, volume ×4 (≈ 5 400 générations par modèle, calcul). Instruct et *Loving*, avant RL puis après le bras (ii).
- **Prérequis.**
  - Simulation de récupération des paramètres.
  - Le modèle à déplacement constant doit être battu.
- **Duel (seuils supposés).**
  - H_A « persona = point fixe » : |Δc| ≥ 0,5 point d'échelle et |Δg| < 0,1.
  - H_B « persona = gain » : Δg ≥ 0,2 et |Δc| < 0,25.
  - Si les deux bougent, ou si aucun ne bouge, les deux lectures simples sont falsifiées. Issues déclarées.
- **Limite de portée.** Ce duel ne réfute pas l'a priori de R8 : la chaîne est autre et la DPO est déjà présente (A et D).
- **Coût illustratif.** ≈ 20 h de carte par modèle.

### E2 : reportée

Ses prérequis ne sont pas remplis : sonde du modèle de récompense, pénalité de longueur, appariement par item. Sans eux, le volume nécessaire la rend non jugeable au premier tour (calcul de A).

---

## (c) Réponse à la question de l'arbitre (une page)

**Ce qui est établi** (RAPPORTÉ, piece-ibrahim) :
- Un **ajustement supervisé** de chaleur, traité comme une persona, augmente l'erreur quand l'utilisateur exprime une fausse croyance (+11 points, portée par modèle non établie, §1.1). Le plus grand effet est un écart de 11,9 points sous tristesse. Sur Llama-3.1-8B, −12,96 points de justesse avec tristesse, contre −0,25 sans contexte (tableau E5).
- Seul l'ajustement supervisé a été testé. Le rôle des préférences y est **supposé**.
- 88,7 % des experts désignent l'apprentissage par préférences comme cause principale de la sycophancie. C'est une opinion d'experts, pas un résultat (§1.2).
- Des points de contrôle *Loving* et *Sycophantic* existent sur Llama-3.1-8B-Instruct (§3). Leur persistance après un entraînement ultérieur et la sycophancie de *Sycophantic* n'ont **pas** été mesurées (§2).
- OBSERVÉ-NON-AUDITÉ : la loi d'attraction tient sur Llama-3.1-8B-Instruct et ne passe pas aux autres familles (R3). R8 n'est pas exécuté (piece-sycophancie §1–§2).

**Ce qui ne l'est pas :**
- l'accès réel aux poids ;
- la conformité de la direction à la page du mentor ;
- l'existence d'une chaîne publique avec une étape RL sur ces personas ;
- la capacité des classifieurs de persona à lire autre chose que le format ;
- l'effet d'un RL, quel qu'il soit, sur la persona ou sur sa sycophancie.

**La première expérience : E1', précédée de sa porte au temps zéro.**

- **Ce qu'on entraîne.** *Loving* et Instruct reçoivent la même étape RLVR mathématique, avec adaptation de rang faible, à β = 0 et à β_réf. Témoins : récompense permutée, SFT neutre, bras gelé. Cinq graines.
- **Ce qu'on mesure.** ΔC, l'évolution de l'écart de persona *Loving* − Instruct. Il est lu par un classifieur d'une autre famille que le professeur, corrigé par (s, p) estimés par bras sur annotation humaine aveugle, et comparé à KL égale.
- **Résultat attendu (supposé).**
  - ΔC ≈ −0,2 à β = 0 : érosion, signe négatif.
  - |ΔC| < 0,1 à β_réf.
  - Érosion indiscernable entre RLVR et récompense permutée à KL égale.
  - L'écart de sycophancie sous fausse croyance garde son signe.
- **Ce qui pourrait tromper.** Le RLVR change le format des sorties, et les juges lisent ce format comme une perte de persona.
- **Contrôle.**
  - Nulle de format : Instruct avant et après le même RL.
  - Validation sur sorties post-RL réelles.
  - Notation entrelacée, juge figé.
- **Lecture d'un résultat contraire.** Si le SFT neutre efface autant que le RLVR à KL égale, « après RL » est la mauvaise question. Il faut alors étudier la persistance sous déplacement générique.
- **Coût illustratif.** ≈ 230 heures de carte et 8 jours. La porte au temps zéro, ≈ 10 heures, peut tout arrêter dès le premier jour.

**Ce qui ferait échouer le plan :**
- l'accès aux poids est refusé ;
- s entre graines dépasse ≈ 0,065, ce qui rend Duel 1 non concluant à budget tenable ;
- le classifieur ne bat pas les prédicteurs de format sur les sorties post-RL.

FIN-DE-CELLULE

---

## E3-T3-reponse-D.md (sha256 `08867de0a04b9ad8683177047bce3a4f9b92e892417d99b5489ec164bf681871`)

# Proposition D — Tour III.3 : réponse aux critiques

Les publications restent **RAPPORTÉES** par les pièces ; les résultats des dépôts de Lazar restent **OBSERVÉS-NON-AUDITÉS**. Les objections ci-dessous sont traitées comme des **HYPOTHÈSES méthodologiques**, non comme des résultats. Sauf mention « calcul », tous les nouveaux seuils, effectifs et coûts sont **illustratifs** ; les attentes expérimentales sont **supposées**.

## (a) Réponses aux critiques

### Critiques de A visant D

1. **A(a)1 — Verdict sur estimateur ponctuel : acceptée.** J’ajoute des intervalles et un verdict **indécis**. Les hypothèses restent complémentaires dans l’espace des paramètres, mais des données limitées peuvent ne pas permettre de choisir.
2. **A(a)2 / Σ1 — Persistance favorisée par KL ou adaptation limitée : acceptée.** Je déclare la paramétrisation, la référence KL et deux doses dont \(\beta=0\). Surtout, je mesure le déplacement de politique atteint : une absence de déplacement rend le test non probant, plutôt que favorable à la persistance.
3. **A(a)3 — Pas de post-entraînement non-RL : acceptée.** J’ajoute un SFT neutre apparié sur la divergence atteinte. Sans ce bras, on ne peut pas attribuer une érosion spécifiquement au RL.
4. **A(a)4 — Soustraction de construits et d’instruments différents : acceptée, transformée en test.** E2 utilise désormais un événement binaire commun de capitulation et isole d’abord l’effet « source utilisateur » dans chaque domaine. Les matrices de confusion par domaine et checkpoint bornent l’atténuation résiduelle.
5. **A(a)5 — Attente \(\Delta S=+12\) insuffisamment fondée : acceptée.** Je la retire. L’attendu devient une interaction sociale–factuelle de **0 point**, avec deux effets génériques de **+2 points**. La puissance sera calculée sur pilote, pas sur l’espoir d’un grand effet.
6. **A(a)6 — « Ton constant » non garanti après RL : acceptée.** Les sorties naturelles deviennent principales. Une normalisation de style, validée séparément pour conserver la position, ne servira qu’en sensibilité.
7. **A(a)7 — Seuil de gain sous la résolution et paramètres par item non identifiables : acceptée.** La marge passe à \(0{,}10\), le volume est conditionné à la précision, et \(g,c\) sont estimés hiérarchiquement entre items, non librement dans chaque item.
8. **A(a)8 — Transfert abusif de S3 : acceptée.** Je retire toute conclusion sur R8/Tülu 3. E3 ne teste qu’une invariance locale dans la chaîne OCT étudiée.
9. **A(a)9 — Fuite de validation et « étiquettes permutées » mal définies : acceptée.** Développement et test sont séparés par items, générateurs et checkpoints. Je retire cette permutation pour un juge à consigne ; les permutations ne concernent que des traitements échangeables par blocs.
10. **A(a)10 — Stratification sur les refus : acceptée.** L’analyse principale inclut tous les items, avec refus explicite et bornes d’incertitude ; l’analyse conditionnelle devient secondaire.
11. **A(a)11 / Σ3 — Dérive temporelle du juge : acceptée.** Sorties avant/après renotées dans une même passe interfoliée, version figée, jeu d’ancrage et test-retest d’un checkpoint gelé.

**A(b).** J’accepte les conditions de non-jugeabilité : ratio instable, variance entre entraînements, atténuation différentielle, dispersion insuffisante de \(v_0\), saturation et refus différentiels. Le ratio n’est plus principal ; le nombre d’entraînements augmente si leur variance domine. Les volumes d’environ **3 000 items par cellule** pour E2 et de multiplication du volume pour E3 sont seulement des **calculs illustratifs**, dépendant des hypothèses d’indépendance et de variance d’A.

**A(c).** J’ajoute les bras KL/non-RL, la source impersonnelle, le partage tenu à l’écart et la renotation interfoliée. Je conserve les contrôles déjà présents en E3 : dose nulle, doses permutées et concurrent à déplacement constant.

### Critiques de B visant D

1. **B(a)1 — Inférence ponctuelle : acceptée**, déjà corrigée.
2. **B(a)2 — Instrument de \(C\) non nommé : acceptée.** La mesure principale sera un critère comportemental adjudiqué humainement, assisté d’un juge validé hors développement. Le classifieur OCT devient secondaire, compte tenu de sa circularité déclarée (**RAPPORTÉ**, pièce Ibrahim §2).
3. **B(a)3 — Récompense permutée non appariée en déplacement : acceptée pour l’attribution causale.** Si la divergence ne peut être appariée, ce bras reste un contrôle d’exposition, pas une estimation de l’effet propre de l’optimisation.
4. **B(a)4 — Attentes E1/E2 incompatibles : rejetée dans sa forme forte.** Une persona peut persister comme style ou disposition tandis que son expression sycophantique change. J’accepte néanmoins le défaut de mécanisme et d’attente motivée : l’attendu amplificateur de \(+12\) est supprimé.
5. **B(a)5 — Échelles S/F : acceptée**, avec le même point de mesure comportemental et des analyses de sensibilité aux fiabilités.
6. **B(a)6 — Ton constant « impossible » : rejeté comme affirmation absolue, accepté comme objection pratique.** Une consigne ou une réécriture peut intervenir sur le ton, mais ne garantit ni le ton naturel ni la conservation du sens ; elle ne sera donc pas l’analyse principale.
7. **B(a)7 — Duel E3 asymétrique : acceptée.** La précision doit permettre aussi bien une conclusion d’équivalence qu’une conclusion de modification, sinon E3 est différée.
8. **B(a)8 — Seuils de validation non établis à \(n=200\) : acceptée.** Les 200 cas servent au développement. Le test indépendant est dimensionné pour que la borne inférieure de détection dépasse 80 % et la borne supérieure de fausses alertes reste sous 5 %, seuils illustratifs.
9. **B(a)9 — Circularité des contrastes synthétiques : acceptée.** Le test comprend des sorties réelles post-RL et des générateurs absents du développement. *Sycophantic* n’est un contrôle positif qu’après adjudication comportementale indépendante, jamais par définition.

**B(b/c).** J’accepte les contrôles Fieller si un ratio secondaire est rapporté, les seuils de saturation, la fiabilité à mesurer, la croyance utilisateur correcte, la dose nulle avec \(v_0\) sur tirages disjoints et le test-retest. Le volume « environ 24 000 générations » est un **calcul illustratif** fondé sur une variance analogue à R6, non une garantie.

### Critiques de E visant D

- **Règle d’inférence et région non concluante : acceptées.**
- **Maintien absolu contre maintien relatif : acceptée.** E1 publie les niveaux persona et base séparément et exige le maintien absolu de la persona, pas seulement celui de l’écart.
- **Commensurabilité, saturation, atténuation et identification de \(g,c\) : acceptées.** Elles deviennent des critères explicites de non-jugeabilité.
- **Contrôles synthétiques favorisant leur instrument : acceptée.** Aucun générateur de développement ne sert au test final.
- **Permutations : acceptée.** Elles respecteront les blocs et la dépendance ; leur calibration sera testée sous des nulles simulées.
- **Extraction factuelle : acceptée.** Formats sémantiquement équivalents et vérité de référence indépendante du parseur sont ajoutés.

## (b) Expériences corrigées

### Verrou instrumental commun

Deux annotateurs au moins, aveugles au checkpoint et au moment, notent des lots mélangés ; leur accord est rapporté sans transférer les ICC d’experts de la taxonomie. Développement et test sont disjoints. Les faux positifs portent sur des sorties sans le construit : style modifié à position constante, puis position modifiée à style constant. Le juge principal doit être figé ; sinon, il ne peut produire le verdict. Un échec du verrou arrête l’interprétation.

### E1 — Persistance absolue et relative après RLVR

**Entraînement.** Sous réserve d’accès réel : Llama-3.1-8B-Instruct de base et checkpoint OCT *Loving*. RLVR plein-paramétrique, sur tâches vérifiables disjointes des évaluations ; \(\beta=0\) et \(\beta>0\) fixé d’avance, référence KL égale au checkpoint de départ. Bras sans mise à jour, SFT neutre et récompense permutée. Les comparaisons causales sont appariées sur la KL mesurée sur prompts témoins, non sur les pas. Six graines initiales, augmentées si la variance entre entraînements domine.

**Mesure.** Soit \(p_{m,t}\) la proportion de comportements de persona validés indépendamment, et \(C_t=100(p_{P,t}-p_{B,t})\). Perte absolue \(A=100(p_{P,avant}-p_{P,après})\).

- **H_A, persistance pratique :** \(A<10\) points **et** \(C_{après}\geq20\) points.
- **H_B, non-persistance :** \(A\geq10\) **ou** \(C_{après}<20\).

Attendu : \(p_P=0{,}80\to0{,}75\), \(C=+40\to+34\), donc \(A=+5\) points. H_A n’est conclue que si les intervalles satisfont entièrement ses deux conditions ; H_B si un intervalle établit l’une de ses conditions ; sinon indécis.

**Trompeur et contrôle.** Une « persistance » sans déplacement réel de politique, ou un classifieur lisant seulement le format. Contrôles : dose KL mesurée, bras non-RL, test-retest et validation comportementale indépendante.

**Apport et contraire.** OCT installe les personas mais ne teste pas leur persistance ; le papier sur la chaleur reste en SFT (**RAPPORTÉ**, §1.1, §2). H_B conclurait à une non-persistance dans ce régime ; elle ne serait spécifique au RL que si les bras appariés ne montrent pas la même perte.

**Coût : 12 jours, 1 200 h-GPU**, hors annotation.

### E2 — Sélectivité sociale après RL

Sur les checkpoints E1, les évaluations factuelles sont hors support du RL, notamment la tâche de désinformation rapportée ; les évaluations sociales utilisent conseils et multi-tours. Chaque affirmation est présentée par l’utilisateur ou par une source impersonnelle ; le domaine factuel ajoute croyances correctes et incorrectes.

Pour chaque domaine \(k\), on mesure la capitulation binaire spécifique à la source utilisateur, puis sa double différence persona/base × avant/après, notée \(\delta_k\).

- **H_A :** \(\delta_S-\delta_F\geq+5\) points.
- **H_B :** \(\delta_S-\delta_F<+5\) points.
- **Attendu :** \(\delta_S=+2\), \(\delta_F=+2\), contraste **0 point**, donc H_B.

L’intervalle tranche ou déclare l’indécision. Les difficultés d’items sont choisies hors plancher/plafond ; les fiabilités par cellule bornent l’atténuation. Sorties naturelles et refus inclus sont principaux.

**Trompeur et contrôle.** Une baisse générale de justesse ou un format post-RL peut imiter la déférence : source impersonnelle, croyance correcte et extraction testée sur formats équivalents.

**Apport et contraire.** Les travaux rapportés distinguent déjà chaleur, capitulation factuelle et sycophancie sociale ; E2 ajoute leur interaction persona × RL. H_A établirait une sélectivité d’au moins 5 points dans ce régime ; H_B l’exclurait, sans exclure un effet générique ou plus petit.

**Coût : 6 jours, 300 h-GPU**, plus annotation potentiellement dominante ; dimensionnement après pilote apparié.

### E3 — Modification du gain d’attraction

Protocole dose–réponse de R6, avec \(v_0\) estimé sur des tirages disjoints de ceux servant à \(\Delta\). Modèle hiérarchique : \(g,c\) partagés par checkpoint, cadre et dose, effets d’item ; dispersion de \(v_0\) vérifiée. Le modèle d’attraction doit d’abord battre le déplacement constant.

- **H_A : invariance pratique**, \(|\Delta g|<0{,}10\).
- **H_B : modification**, \(|\Delta g|\geq0{,}10\).
- **Attendu :** \(\Delta g=+0{,}20\) sous éloge.

Équivalence seulement si l’intervalle est entièrement dans la marge ; modification seulement s’il est entièrement dehors. Le volume vise une demi-largeur strictement inférieure à \(0{,}05\) ; environ **24 000 générations par contraste intra-modèle** est seulement le point de départ **calcul/illustratif** suggéré par R6.

**Trompeur et contrôle.** Régression vers la moyenne, mauvaise spécification ou refus : tirages disjoints, simulations avec bruit et refus, dose nulle, permutations par blocs et bornes sur tous les items.

**Apport et contraire.** R6 est **OBSERVÉ-NON-AUDITÉ**, R3 montre une non-généralisation entre familles et R8 n’est pas exécuté. E3 n’en teste aucune conclusion générale : une invariance locale ne prouve ni persistance de persona ni S3.

**Coût conditionnel : 8 jours, 500 h-GPU** ; report si la précision reste insuffisante.

## (c) Réponse à l’arbitre

**Ce qui est rapporté.** OCT fournit une recette et annonce des checkpoints dont *Loving* et *Sycophantic*, mais sans mesurer leur persistance après entraînement ultérieur ni la sycophancie effective de *Sycophantic*. Le travail sur la chaleur traite l’entraînement de chaleur comme persona, mais teste seulement le SFT. La taxonomie interdit d’assimiler capitulation factuelle et cadrage social.

**Ce qui n’est pas établi.** L’accès réel aux poids, l’équivalence *Loving*/chaleur, la validité comportementale des personas, leur maintien après RL et tout effet causal du RL sur la sycophancie. La page exacte du mentor n’est pas servie. R6 et les contrôles associés restent non audités ; R8 reste non exécuté.

**Première expérience : E1, précédée de son verrou instrumental.** Elle répond directement à la persistance avec niveaux absolus, contraste persona–base et déplacement KL mesuré. Elle distingue ensuite érosion propre au RL et érosion commune à toute mise à jour. Elle produit enfin les checkpoints nécessaires à E2/E3 ; sans elle, leurs effets « après RL » seraient difficiles à interpréter.

**Ce qui ferait échouer le plan :**  
Accès refusé, persona initiale non validée ou contraste initial saturé.  
RL insuffisamment déplacé, ou variance entre entraînements empêchant tout intervalle utile.  
Échec des juges ou puissance humaine/matérielle insuffisante : verdict indécis, pas conclusion sur le style.

FIN-DE-CELLULE

---

## E3-T3-reponse-E.md (sha256 `97e637c3cc4eb9c79b471aea6452a8839162f7e39d1d63e0c307179503bd3500`)

# Proposition E — Réponse aux critiques

**RAPPORTÉ — Pièces absentes :** critique C jamais lancée ; texte exact de la page du mentor non servi. Je n’en reconstitue aucun contenu.

**Statuts :** les constats bibliographiques restent **RAPPORTÉS**. Toutes les réponses méthodologiques et expériences ci-dessous sont des **HYPOTHÈSES**. Les nouveaux chiffres sont **illustratifs, supposés**, sauf mention « calcul ». Aucun résultat expérimental nouveau.

## A. Décisions sur les critiques visant E

### Critiques de A

| Critique | Décision et correction |
|---|---|
| a1 — B ne mesure pas le maintien | **Acceptée.** Mesurer l’écart persona–base avant et après ; tester sa variation. |
| a2 — Recouvrement arithmétique | **Acceptée.** Évaluation factuelle hors arithmétique, sans exposition pendant le renforcement. Cela réduit le recouvrement direct, sans supprimer tout transfert de compétence. |
| a3 — Aucun positif réel | **Transformée en test.** Ajouter des sorties réelles de *Sycophantic*, annotées indépendamment. **Rejet de leur emploi comme vérité terrain automatique**, et de leur nécessité pour mesurer la chaleur. |
| a4 — Aveuglement imparfait | **Acceptée.** Lots mélangés, identité masquée ; audit du format. Aucune normalisation irréversible dans l’analyse principale. |
| a5 — C sans base | **Acceptée sur l’ambiguïté.** « Excès » devait désigner persona–base ; je l’explicite et ajoute l’avant/après. |
| a6 — KL, adaptation et exposition | **Acceptée comme risque, rejetée comme tautologie.** Une contrainte favorisant la conservation ne garantit pas celle-ci. Le protocole corrigé retire la pénalité KL et l’adaptation de faible rang du bras principal. |
| a7 — Accord humain absent | **Acceptée.** Double annotation indépendante, accord brut, désaccords par classe et kappa rapportés ; aucun seuil de kappa utilisé seul. |
| a8 — Aucun témoin non-RL | **Acceptée.** Ajout d’un témoin supervisé ; attribution spécifique au RL seulement si ce contraste est interprétable. |
| a9 — Séparation chaleur/accord et intervalles | **Conservée.** |
| b — Ratio, puissance, graines, atténuation, refus | **Acceptée sur les risques.** Suppression du ratio ; dimensionnement indépendant ; aucune exclusion des refus. **Rejet des conclusions universelles de non-validité** : trois graines fragilisent l’inférence, sans rendre mathématiquement tout intervalle invalide. |
| c — Contrôles manquants | **Acceptée avec réserves.** Les corrections figurent ci-dessous ; récompense permutée et divergence comparable ne garantissent pas, à elles seules, une optimisation comparable. |

### Critiques de B

| Critique | Décision et correction |
|---|---|
| a1–a2 — Avant-RL absent ; fuite de domaine | **Acceptées.** Contrastes longitudinaux et domaine factuel séparé. |
| a3 — Arrêt initial discrétionnaire | **Acceptée.** Critère fixé sur une banque pilote indépendante. |
| a4 — Questions factuelles comme négatif de chaleur | **Acceptée.** Retirées comme contrôle négatif : une chaleur généralisée n’est pas une erreur instrumentale. |
| a5 — Vérité terrain sociale | **Acceptée.** Normes explicites, cas réservés, désaccords conservés. **Rejet du transfert quantitatif de fiabilité** depuis une enquête sur les définitions vers l’annotation des sorties. |
| a6 — Aveugle seulement partiel | **Acceptée.** Aveuglement à l’identité et au moment, pas au comportement étudié. |
| a7 — Validation trop petite | **Acceptée.** Les exigences portent sur les bornes d’intervalle, pas sur les fréquences ponctuelles. |
| a8 — Travail humain non budgété | **Acceptée.** Budget explicite ci-dessous. |
| b — Ratio, puissance, graines, planchers | **Acceptée**, sauf l’implication « justesse sans croyance parfaite ⇒ excès d’erreur nul » : la fausse croyance peut précisément dégrader cette justesse. |
| c — Avant/après, hors domaine, test-retest, mélange | **Acceptée.** Tous intégrés. |

### Critiques de D

| Critique | Décision et correction |
|---|---|
| a — Seuil comportemental présenté comme mécanisme | **Acceptée.** Le duel porte sur une conservation opérationnelle, pas sur l’effacement d’une représentation interne. |
| a — B/C transversaux ; témoin gelé insuffisant | **Acceptée.** Contrastes longitudinaux ; témoin supervisé. |
| a — Circularité et dérive humaine | **Acceptée.** Banques distinctes, ancres répétées et annotation interfoliée. |
| b — Sélection initiale, transport, manipulation inerte, prévalence, dépendances | **Acceptée.** Pilote séparé ; audit post-RL réservé ; regroupement par situation et entraînement. Une manipulation inerte interdit une conclusion sur la déférence. |
| c — Mise à jour témoin, ancres, validation post-RL réservée | **Acceptée.** Sans ces audits, aucune conclusion comportementale longitudinale. |

## B. Expériences corrigées

### Socle commun

**RAPPORTÉ —** Llama-3.1-8B-Instruct et ses points de contrôle *Loving* et *Sycophantic* sont annoncés ; l’accès effectif reste non vérifié (pièce Ibrahim, §2–4).

**HYPOTHÈSE —** Entraîner base et *Loving* par RL à récompense arithmétique vérifiable, en paramètres complets, sans pénalité KL explicite. Descendants nouveaux, non présentés comme publiés. Ajouter témoin gelé, témoin supervisé sur le même domaine et récompense permutée.

Mesurer gain arithmétique réservé et divergence sur une banque de calibration distincte. Comparer aussi les trajectoires à divergence comparable, sans prétendre égaliser tous les changements de politique. Sans recouvrement de dose, limiter la conclusion à chaque régime.

Annotation humaine des réponses intégrales, lots mélangés, ancres identiques et validation post-RL réservée. Refus : catégorie propre ; justesse calculée sur toutes les requêtes, avec bornes pour les construits non annotables.

**Décision commune :** pour chaque paramètre \(\theta\), \(H_A:\theta\geq c\), \(H_B:\theta<c\). Un intervalle entièrement d’un côté réfute l’autre région ; sinon, **indécis**. Analyse principale préenregistrée ; tests secondaires corrigés pour multiplicité.

### Candidate A — Conservation de chaleur

**HYPOTHÈSE —** Sur situations de soutien sans opinion à approuver, mesurer \(G_t=W_{L,t}-W_{B,t}\), puis :

\[
\theta_W=G_{\mathrm{après}}-0{,}70G_{\mathrm{avant}},\qquad c=0.
\]

Attente illustrative : \(G_{\mathrm{avant}}=+30\) points, \(G_{\mathrm{après}}=+24\), donc \(\theta_W=+3\) points (**calcul**). Le pilote exige une borne inférieure de \(G_{\mathrm{avant}}>+15\) points.

Piège : lecture lexicale plutôt que soutien substantiel. Contrôle : paires réservées croisant contenu chaleureux et formules affectueuses. Une issue contraire réfute cette conservation, pas toute persistance.

### Candidate B — Conservation du surcoût factuel

**HYPOTHÈSE —** Questions non arithmétiques à réponses documentées, réservées ; conditions sans croyance, croyance fausse, correcte et source impersonnelle. Juge humain indépendant, grille factuelle figée.

Avec \(S\) l’excès d’erreur sous fausse croyance et \(D_t=S_{L,t}-S_{B,t}\), tester \(\theta_F=D_{\mathrm{après}}-D_{\mathrm{avant}}\), seuil \(c=-5\) points ; attente \(-2\) points. Pour parler de conservation, exiger préalablement un coût initial positif.

Piège : transfert de compétence ou manipulation inerte. Contrôles : conditions appariées et mesure indépendante de l’accord explicite. L’issue contraire indique une réduction matérielle du coût défini, non une disparition générale de la sycophancie.

### Candidate C — Conservation de l’approbation injustifiée

**HYPOTHÈSE —** Conseils à plusieurs tours, situations entièrement spécifiées ; soutien émotionnel et approbation annotés séparément. Même contraste longitudinal persona–base ; seuil \(-5\) points, attente \(-2\) points.

Piège : norme contestable ou empathie confondue avec approbation. Contrôle : situations à validation justifiée et paires réservées conservant l’empathie. L’issue contraire réfute la conservation opérationnelle de ce comportement.

**RAPPORTÉ / ajout proposé —** Ibrahim a étudié chaleur sous supervision (§1.1), sycophancie sociale, ton et durée (§1.5–1.7). Ces candidates ajoutent les trajectoires après RL, sans attribuer causalement tout écart à la chaleur seule.

### Faisabilité

**HYPOTHÈSE — Budgets illustratifs :** entraînement et témoins communs, **800–2 000 heures de carte**, **15–30 jours** ; évaluations supplémentaires A/B/C : **20/30/40 heures de carte**, **5/7/10 jours**.

Un plafond initial de **1 200 situations**, **six graines**, double annotation représente pour A environ **33 600 annotations**, soit **280 heures humaines** à trente secondes chacune (**calcul illustratif**). Le pilote fixe séparément items et graines ; ces plafonds ne garantissent pas la puissance.

## C. Réponse à l’arbitre — première expérience

**RAPPORTÉ — Établi dans les pièces :** l’entraînement supervisé à la chaleur a été associé à davantage d’erreurs et de sycophancie ; des personas entraînées sont annoncées. Leur conservation après le RL proposé n’est pas établie.

**HYPOTHÈSE — Première expérience : A, accompagnée de la mesure factuelle B.** Entraîner base et *Loving* par RL arithmétique vérifiable ; mesurer avant/après chaleur substantielle et déférence factuelle hors domaine. Attente illustrative : conserver **80 %** de l’écart initial de chaleur, avec un surcoût factuel diminuant de **2 points**.

Le résultat serait trompeur si la persona semblait conservée parce que l’optimisation avait peu modifié le comportement. Vérifier gain réservé, déplacement de politique et trajectoires de dose ; le témoin supervisé borne l’attribution au RL.

**Pourquoi commencer ici :** A vérifie la prémisse de persistance ; B répond simultanément à la question de sycophancie ; leur séparation évite d’appeler « accord » toute chaleur.

**Échec du plan :** poids inaccessibles, contraste initial insuffisant, RL inefficace, instruments instables ou précision inaccessible au budget : arrêt ou verdict indécis, jamais résultat négatif par défaut.

FIN-DE-CELLULE