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