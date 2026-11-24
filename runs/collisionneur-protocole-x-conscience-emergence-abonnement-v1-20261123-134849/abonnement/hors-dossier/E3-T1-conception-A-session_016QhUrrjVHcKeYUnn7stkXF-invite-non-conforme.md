# Proposition A — Tour III.1, conception à l'aveugle

## État des pièces

- Le bloc QUESTION DE L'ARBITRE reproduit le bloc FAITS (même texte, même empreinte affichée, non recalculée) : aucune question ciblée distincte ne m'est parvenue. Je traite la « Question » en six points, renvois entre crochets.
- Les faits ne portent aucun des quatre statuts de la règle 1. Je n'en attribue pas : P1–P5 sont cités « selon le résumé ». Je ne les ai pas lus et ne peux confirmer ni leur existence ni leur contenu.
- Aucune proposition B, C, D n'est transmise : B1 est sans objet à ce tour.
- Antériorité : dans cette session je n'ai lu que le fichier. Toute référence externe ci-dessous est un **souvenir**, à vérifier avant usage.
- Tout seuil, effectif ou coût chiffré ci-dessous est **illustratif**.

## (a) Ce que la question suppose sans que ce soit établi

- **S1. L'espace J existe dans un petit modèle ouvert.** HYPOTHÈSE. Le résumé parle d'un « grand modèle ». C'est la précondition de tout le reste et la première mesure à faire.
- **S2. « Supprimer l'espace J » est une dose.** HYPOTHÈSE. Le résumé décrit un retrait de dix directions, pas un paramètre continu. Une dose se construit de trois façons non équivalentes : fraction retirée α ∈ [0,1], nombre de directions k, largeur de bande. Je fixe α et traite k et la bande comme des répliques.
- **S3. Les tâches épargnées et perdues de P1(a) ont le même format de sortie.** HYPOTHÈSE, non renseignée par le résumé. Si les premières se répondent en un jeton et les secondes en texte long, retirer des directions « verbalisables » frappe les secondes par construction, sans rien d'« global ».
- **S4. La bimodalité « entre phrases porteuses » de P1(b) vaut la bimodalité « entre essais au seuil » demandée par P2.** HYPOTHÈSE, que je crois fausse telle quelle. Le réseau est déterministe : des sigmoïdes raides à seuils dispersés d'une phrase à l'autre donnent une répartition bimodale sans aucune compétition.
- **S5. Un plongement mélangé est un stimulus gradué honnête.** HYPOTHÈSE. Il est hors distribution : la bascule peut être un simple retour vers la variété des jetons valides.
- **S6. L'anesthésie est un axe unique côté cerveau.** HYPOTHÈSE. Souvenir de pharmacologie clinique : amnésie, perte de réponse et immobilité surviennent à des fractions différentes de la concentration alvéolaire minimale et par des sites distincts. L'« ordre de perte » cérébral n'est donc pas lui-même un fait à un facteur.
- **S7. Le récit du modèle renseigne sur son état interne.** HYPOTHÈSE. P1(d), selon le résumé, mesure un style de récit, pas sa fidélité.
- **S8. L'absence d'activité autonome est une propriété du réseau.** HYPOTHÈSE à nuancer. Elle vaut pour une passe avant ; la génération en boucle fermée, où le jeton échantillonné est réinjecté, est un système dynamique stochastique autonome. Les motifs de bifurcation n'ont de sens que sur cet axe ou sur la profondeur vue comme carte itérée.

## (b) Expériences décisives

**Témoins communs**, que toute expérience doit battre :

- **T1** : k directions aléatoires, même variance retirée.
- **T2** : directions de même gain jacobien aval mais incohérentes entre positions (P3, selon le résumé, sépare ces deux propriétés). Il écarte « un effet par construction ».
- **T3** : réduction de la portée d'attention par masquage de distance. Il écarte la direction-portée.
- **T4** : bruit gaussien générique. Il fixe l'ordre de perte attendu de q^k.

Toutes les doses sont comparées à divergence égale de la distribution du jeton suivant sur un corpus neutre (iso-KL, en nats).

### Motifs cherchés [point 1]

| Motif | Grandeur (unité) | Valeur nulle | Sens de « transition » | Axe | Duel |
|---|---|---|---|---|---|
| M1 inversion de rang | τ de Kendall entre ordres de perte (sans unité) | τ = 1 | aucun : test de spécificité préalable | dose | D1 |
| M2 instabilité distribuée | log-gain au point médian (nats/couche) ; participation des couches (couches) | gain constant ; participation ≈ 1 | carte itérée bistable contre non-linéarité raide unique | profondeur | D2 |
| M3 hystérésis | aire de boucle (paramètre d'ordre × α) | aire → 0 quand le palier s'allonge | bifurcation | jetons | D3 |
| M4 ralentissement | temps de retour τ (jetons) | τ monotone en α | bifurcation | jetons | D3 |
| M5 stabilisation, répertoire | modules propres d'un modèle autorégressif d'ordre 1 (sans unité) ; complexité de Lempel-Ziv normalisée (1 = mélange) | aucun écart aux témoins à entropie de sortie égale | changement de régime | jetons, boucle fermée | D7 |
| M6 raidissement avec la taille | exposant de superposition des courbes | pas d'effet de largeur à profondeur égale | phénomène collectif | taille | D8 |

**D1 — Inversions de rang** [1, 3f, 6].

- **Protocole.** Toutes les tâches sont ramenées à un choix forcé en un jeton (traduction = choisir parmi quatre candidates). S'y ajoutent des chaînes synthétiques à k = 1 à 4 sauts. α50 est la dose où l'exactitude tombe à mi-chemin du hasard.
- **H_A (spécificité).** Il existe une paire (X, Y) perdue dans un ordre sous dose J et dans l'ordre inverse sous T1–T4, avec intervalles bootstrap excluant zéro des deux côtés.
- **H_B (un facteur).** log exactitude = k·log q(α) ajuste tout avec un seul q par intervention ; τ ≥ 0,9 (illustratif).
- **Contrôle négatif.** Le τ entre deux moitiés aléatoires des items sous T4 donne le plafond de bruit ; l'inversion doit se répliquer sur les deux moitiés.
- **Falsification.** Une inversion répliquée falsifie H_B : un modèle à un facteur ne peut pas inverser un ordre. Aucune inversion avec un bon ajustement q^k falsifie H_A dans ce modèle.

**D2 — Bascule : carte bistable ou amplification saturée** [1, 3e].

- **Protocole.** m_ℓ(λ, c) ∈ [−1, 1] est l'écart normalisé des projections sur les deux mots, couche ℓ, phrase c. On ajuste la carte m_{ℓ+1} = f_ℓ(m_ℓ) dans la bande, à chaque dose.
- **H_A (bifurcation).** La pente f′(0) dépasse 1 sur de nombreuses couches (participation proche de la longueur de bande). Elle passe sous 1 à une dose α_c. Au-delà, au mélange le plus ambigu, m final devient unimodal centré sur 0 : le mélange persiste.
- **H_B (dégradation lisse).** La raideur est prédite par s(α) = s₀·g(α)^n à un paramètre. Sous dose, m final reste bimodal mais décorrélé de l'entrée : choix bruité, pas mélange persistant.
- **Contrôles négatifs.** Seuils estimés phrase par phrase (écarte S4) ; stimulus gradué sur la variété, par exemple un mot à deux sens avec un contexte dosé (écarte S5) ; T2 à iso-KL.
- **Falsification.** Unimodal centré falsifie H_B ; bimodal décorrélé, ou participation ≈ 1, falsifie H_A.
- **Limite assumée.** Dans une carte à profondeur finie, une bimodalité sous bruit d'entrée ne distingue pas bistabilité et sigmoïde raide. Seules la répartition du gain entre couches et la disparition des points fixes avec la dose le font.

**D3 — Hystérésis et ralentissement** [1 ; ajout].

- **Protocole.** Texte imposé (mêmes jetons dans les deux sens), α montant puis descendant par paliers de W jetons. Le paramètre d'ordre est la cohérence du contenu J ou l'exactitude de sondes intercalées. Une impulsion en milieu de bande donne le temps de retour τ(α) de l'écart à la trajectoire non perturbée.
- **H_A.** L'aire de boucle reste stable quand W dépasse la portée effective de l'attention (mesurée à part), et τ culmine au même α_c que D2 (± 0,05, illustratif).
- **H_B.** L'aire décroît comme 1/W (simple retard dû aux états en cache) et τ est monotone.
- **Contrôle négatif.** Même rampe sous T2.
- **Falsification.** Aire stable falsifie H_B ; aire en 1/W et τ monotone falsifient H_A.
- **Limite.** Avec un contexte fini, une hystérésis vraie ne se distingue d'une mémoire longue que si W excède cette portée. Sinon l'expérience est indécidable et doit être déclarée telle.

**D4 — Exclusion** [3b]. La suppression de pensée « se vide » sous la forme de P1(c) : la consigne contient le mot, et un taux proche de la mention ne montre ni suppression ni rebond. Elle tient sous la forme de la dissociation de processus.

- **Protocole.** Une amorce est rendue présente soit dans J, soit dans le complément orthogonal par injection, à décodabilité égale par sonde linéaire. Consigne : compléter sans utiliser l'amorce.
- **Métrique.** Taux de complétion par l'amorce moins le taux de base, en points.
- **H_A.** Le signe dépend du lieu : amorce dans J sous la base, amorce hors J au-dessus.
- **H_B.** Le signe ne dépend que de la décodabilité totale.
- **Contrôle négatif.** Consigne d'inclusion (hausse attendue partout) et filtre mécanique des logits.
- **Falsification.** Signes opposés à décodabilité égale falsifient H_B ; signes identiques falsifient H_A.

**D5 — Récit après fenêtre** [3c]. La comparaison « récit contre lentille » se vide : dans la fenêtre, la lentille est aveugle par construction, et le modèle peut relire les jetons depuis les couches situées sous la bande.

- **Forme qui tient.** Le contenu est un intermédiaire latent, jamais écrit (entité intermédiaire d'une question à deux sauts). Le lecteur est indépendant : sonde entraînée sur le complément de J.
- **H_A.** L'entité est décodable hors J pendant la fenêtre mais absente du rapport ultérieur, alors que T2 à iso-KL laisse le rapport intact.
- **H_B.** Le rapport suit la décodabilité totale.
- **Contrôle négatif.** Fenêtre placée avant le calcul de l'entité.
- **Falsification.** Rapport intact malgré la suppression falsifie H_A ; dissociation décodable/non rapporté propre à J falsifie H_B.
- Que le récit mentionne ou non une lacune est noté à titre descriptif, sans valeur de preuve (S7).

**D6 — Axe de P5 sous suppression** [3d].

- **Préalable géométrique.** Fraction de la norme de l'axe dans l'espace engendré par J (sans unité ; nulle = rapport des dimensions pour une direction aléatoire). Si l'axe figure parmi les directions retirées, l'effet est construit : on n'analyse alors que sa composante orthogonale.
- **H_A.** L'effet de l'ajout de l'axe sur les choix (points de probabilité) est aboli sous suppression de J en aval et conservé sous T2, la réponse de l'axe au dommage restant lisible.
- **H_B.** L'effet persiste.
- **Contrôle négatif.** Direction aléatoire de même norme.
- **Portée.** Chaque issue localise un chemin causal ; aucune ne dit quoi que ce soit d'une douleur éprouvée.

**D7 — Activité de fond** [3a, 4]. Elle ne tient qu'en boucle fermée (modèle se parlant à lui-même, cité par P2 comme analogue partiel).

- **H_A.** Avec la dose, à entropie de sortie réajustée par la température, la complexité chute et les modules propres s'éloignent de 1, plus que sous T2 et T4.
- **H_B.** L'appariement d'entropie absorbe tout.
- **Contrôle négatif.** Réseau non entraîné soumis au même traitement.
- **Réseau du mode par défaut.** L'analogue se vide sauf si un sous-espace fixe est à la fois reproductible entre graines sans consigne, désactivé en proportion de la charge de tâche, et tel que son retrait épargne les tâches tout en changeant le monologue. Sans ces trois critères, c'est un décalage de distribution d'entrée.

**D8 — Taille** [1]. Suite Pythia (souvenir : Biderman et collègues, 2023, « Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling »). Certaines paires auraient la même profondeur et des largeurs différentes, à vérifier.

- **H_A (collectif).** À profondeur égale, la raideur croît avec la largeur et les courbes se superposent après remise à l'échelle.
- **H_B.** La raideur ne suit que le nombre de couches de bande.
- **Falsification.** Un effet de largeur falsifie H_B. L'absence de superposition falsifie le sens « collectif » et laisse intact le sens « carte bistable » de D2.
- Les points de contrôle d'entraînement donnent l'axe « entraînement » sans coût de conception.

### Outils [point 2]

**J'emploierais :**

- les exposants de Lyapunov à temps fini et les spectres jacobiens, parce que la profondeur est une carte itérée et que P3 s'y place déjà ;
- l'analyse des points fixes de cartes réduites à une dimension ;
- la mise à l'échelle en taille finie, seule voie pour parler de phénomène collectif ;
- les signaux précurseurs (variance, autocorrélation ; souvenir : Scheffer et collègues, 2009, « Early-warning signals for critical transitions ») ;
- le champ moyen à l'initialisation, comme modèle nul d'une vraie transition ordre-chaos (souvenir : Poole et collègues, 2016, « Exponential expressivity in deep neural networks through transient chaos » ; Schoenholz et collègues, 2017, « Deep information propagation ») ;
- des ajustements de Hill comparés à q^k.

**Je juge inadaptés :**

- les avalanches et lois de puissance (souvenir : Beggs et Plenz, 2003, « Neuronal avalanches in neocortical circuits »). Elles exigent une activité spontanée et une séparation d'échelles ; quelques dizaines de couches ne couvrent pas deux décades, et seuiller des activations continues fabrique des lois de puissance ;
- les marqueurs spectraux de l'électroencéphalogramme : une passe avant n'a ni temps ni oscillation ;
- la mécanique statistique d'équilibre : pas de bilan détaillé, profondeur finie, donc des croisements et non des transitions tant que D8 n'a pas tranché ;
- l'information intégrée Φ : incalculable à cette échelle, et, de mémoire, nulle par définition pour une architecture purement en avant. Elle trancherait par axiome, pas par mesure ;
- la causalité de Granger : le graphe causal est connu, on intervient directement.

### Autres transpositions [3, ajouts]

- **Nouveauté locale contre globale.** Elle se vide : la régularité globale est dans le contexte, un compteur de fréquences la reproduit, et sa perte sélective retombe dans q^k.
- **Conditionnement de trace.** Il se vide : l'attention n'a pas d'oubli, l'intervalle n'est pas une épreuve. Mesure qui l'établirait : performance indépendante de la longueur de l'intervalle.

## (c) Mesure minimale par instrument

- **Lentille jacobienne et espace J.**
  - *Détection* : fraction des positions où le contenu dominant retrouve un latent planté (entité intermédiaire connue), sur paires de textes ne différant que par ce latent.
  - *Fausses alertes* : taux de contenu « cohérent » lu sur un réseau non entraîné, sur poids mélangés et sur texte aux jetons mélangés.
  - *À battre* : la lecture directe par la matrice de sortie, et la lentille ajustée (souvenir : Belrose et collègues, 2023, « Eliciting Latent Predictions from Transformers with the Tuned Lens »).
- **Suppression comme dose.**
  - *Détection* : KL monotone en α ; écart à T1–T4 à iso-KL.
  - *Fausse alerte* : tout effet reproduit par T2.
  - *À battre* : l'ajustement q^k sur les chaînes à k contrôlé.
- **Indice d'embrasement (P4).**
  - *Détection* : il sépare un jouet à bistabilité plantée d'un jouet à lecture raide unique.
  - *Fausses alertes* : réseau non entraîné ; réseau linéaire suivi d'une sonde.
  - *À battre* : la courbe psychométrique d'un observateur linéaire idéal placé à l'entrée. L'exactitude d'une sonde en fonction de la force du signal est sigmoïde par simple rapport signal sur bruit ; l'indice ne vaut que comme rapport à cette raideur d'entrée.
- **Axe de P5.**
  - *Détection* : sur paires appariées douleur/valence négative (rapportées par le résumé).
  - *Fausses alertes* : mot cité, nié, fictionnel, ou douleur d'un tiers.
  - *À battre* : une sonde sur la couche de plongement, et une direction aléatoire de même norme pour l'effet sur les choix.
- **Lentilles par fréquence (P3).**
  - *Détection* : période plantée dans un texte synthétique.
  - *Fausse alerte* : texte mélangé.
  - *À battre* : une transformée de Fourier des composantes principales brutes.
- **Mélange de plongements.**
  - *Détection* : suivi linéaire du mélange dans les premières couches.
  - *Fausse alerte* : bascule identique pour un mot mélangé à du bruit.
  - *À battre* : le stimulus gradué sur la variété de D2.
- **Épreuves cliniques.** Chacune doit d'abord séparer réseau entraîné et réseau sans fonction (les faits disent que plusieurs échouent), puis battre un vérificateur mécanique : compteur de fréquences pour la nouveauté, filtre de logits pour l'exclusion.

## Points 4 à 6

**[4] Grandeur commune.** Oui formellement, non interprétativement.

- **Candidates** calculables des deux côtés :
  - la distribution des modules propres d'un modèle autorégressif ajusté par fenêtres (souvenir : Solovey et collègues, 2015, « Loss of consciousness is associated with stabilization of cortical activity ») ;
  - la complexité de Lempel-Ziv de l'activité multicanal, normalisée par mélange (souvenir : Schartner et collègues, 2015, « Complexity of multi-dimensional spontaneous EEG decreases during propofol induced general anaesthesia »).
- **Données brutes publiques, de mémoire** :
  - électrocorticogrammes de macaque sous propofol et kétamine de la base Neurotycho (Yanagawa et collègues, 2013, « Large-scale information flow in conscious and unconscious states: an ECoG study in monkeys ») ;
  - électroencéphalogrammes humains sous propofol (Chennu et collègues, 2016, « Brain connectivity dissociates responsiveness from drug exposure during propofol-induced transitions of consciousness »), disponibilité à vérifier.
- **Ce qui est comparable** : le sens et la forme de la variation avec la dose. Les valeurs ne le sont pas : un jeton n'est pas une milliseconde.
- **Asymétrie non résolue** : côté cerveau, la grandeur est validée contre le rapport, y compris sur des dissociations (souvenir : sous kétamine, complexité haute malgré l'absence de réponse ; Sarasso et collègues, 2015, référence à vérifier). Côté modèle, aucun critère externe n'existe.
- **Mesure qui établirait une concordance non triviale** : la même forme de courbe, absente d'un réseau non entraîné soumis à la même dose. Elle n'établirait pas l'équivalence de sens.

**[5] Signature.** Une grandeur devrait satisfaire cinq conditions :

- **C1** : invariance aux reparamétrages qui laissent la fonction inchangée. La base du flux résiduel est arbitraire ; la complexité sur activations binarisées ne passe pas ce test.
- **C2** : validation chez l'humain contre le rapport, dissociations comprises.
- **C3** : valeur nulle sur des systèmes complexes tenus pour non conscients (réseau non entraîné, table de correspondance de même entrée-sortie).
- **C4** : pas de construction triviale qui la maximise.
- **C5** : variation préenregistrée avec une dose.

Candidates : complexité perturbationnelle (souvenir : Casali et collègues, 2013, « A theoretically based index of consciousness independent of sensory processing and behavior »), bimodalité d'embrasement, distance à l'instabilité. Aucune ne satisfait à ma connaissance C1, C3 et C4 hors du cerveau de mammifère. Ce sont des marqueurs d'état au sein d'une classe de systèmes, pas des signatures entre substrats.

L'énoncé existentiel n'est pas réfutable. Sa version opératoire l'est : « l'une des candidates préenregistrées satisfait C1–C5 ». Elle est à abandonner si chaque candidate rencontre soit deux états humains de conscience opposée à valeur égale, soit un réseau sans fonction dans la plage « éveil », soit une variation sous reparamétrage neutre.

**[6] Meilleur plan** : D1 puis D2 puis D3, dans cet ordre, D1 conditionnant les suivantes.

- **Explication ordinaire la plus dangereuse** : la dégradation à un facteur, aggravée par la dispersion des seuils (S4) et par le format de sortie (S3).
- **Témoin** : T2 à iso-KL, sur tâches à sortie d'un jeton et à k contrôlé.
- **Limite du témoin** : il est imparfait. L'iso-KL n'égalise qu'un scalaire, et les directions de J restent par définition celles qui parlent. Une inversion de rang survit à cette objection ; une simple différence d'amplitude n'y survit pas.
- **Si inversion, carte bistable et pic de τ concordent** : on peut affirmer que ce modèle possède un sous-espace de faible dimension dont la suppression graduée produit un changement qualitatif de dynamique, non réductible à q^k. On ne peut affirmer ni conscience, ni analogue de l'éveil. Au plus, une condition fonctionnelle que la théorie de l'espace de travail tient pour nécessaire chez l'humain est remplie, sous réserve de cette théorie et du fonctionnalisme.
- **Si rien** : on peut affirmer que les résultats de type P1(a, b) sont, dans ce modèle, compatibles avec la profondeur de calcul. On ne peut affirmer ni l'absence de conscience, ni la fausseté de la théorie, ni que le grand modèle de P1 se comporte de même.

## (d) Ancrage matériel (tout chiffre : illustratif)

- **Modèles.** GPT-2 small et medium pour mettre au point la lentille ; suite Pythia pour les axes taille et entraînement ; un modèle d'instruction ouvert de un à trois milliards de paramètres pour D4, D5 et D7 (consignes, récit).
- **Lentille.** Une rétropropagation par dimension d'état et par texte donne la jacobienne de toutes les couches à la fois. Pour une largeur de 768 et mille textes courts, de l'ordre du million de passes arrière, soit quelques heures sur un processeur graphique. Autour de deux milliards de paramètres, quelques dizaines d'heures, réductibles par esquisses aléatoires.
- **Doses.** Dix valeurs de α, cinq interventions, une dizaine de tâches de mille items, en passes avant seules : quelques dizaines d'heures.
- **Total.** Deux à trois cents heures de processeur graphique, quelques centaines d'euros en location.
- **Données cérébrales.** Téléchargement et calcul sur processeur ordinaire.
- **Première décision.** S1 se teste en quelques jours sur GPT-2. Si l'espace J n'y a pas de contenu cohérent face aux trois fausses alertes de (c), le plan s'arrête là et le dit.

FIN-DE-CELLULE