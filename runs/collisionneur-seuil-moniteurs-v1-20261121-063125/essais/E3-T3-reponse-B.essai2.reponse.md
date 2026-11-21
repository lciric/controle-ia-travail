# Proposition B — Tour III.3 : réponse aux critiques

**Pièces reçues.** Ma conception III.1 et les critiques croisées de A, C, D et E sont présentes, complètes, et chacune se termine par sa marque de fin. Je ne réponds qu'aux sections « Sur la proposition B ». S'y ajoute le préambule de D : il réfute directement une phrase de ma P3, et je m'en sers en le disant (B1).

**Statuts.**
- **RAPPORTÉ** : faits, ou affirmation d'une pièce critique.
- **VÉRIFIÉ** : calcul que j'ai refait ici.
- **HYPOTHÈSE** : tout le reste, y compris toutes mes propositions corrigées.

Aucun résultat d'expérience n'est revendiqué. Aucun identifiant arXiv n'est donné de mémoire.

---

## (a) Décision sur chaque critique

### Bloc 1 — Validité et nature de l'e-processus P3 (et de E2)

| Réf. | Critique (RAPPORTÉ) | Décision | Raison, correction ou test |
|---|---|---|---|
| A-a1, A-a2, C-c (invite), E-c2 | P3 teste « agent = jumeau », pas « agent honnête ». Une consigne cachée ou un affinage fait rejeter le nul sans sabotage. | **Acceptée** | Le nul exact de P3 est l'identité de politique conditionnellement au préfixe. Mon contrôle positif à température modifiée le montrait déjà. **Correction de lecteur** (P3', HYPOTHÈSE) : les K+1 candidats (pas de l'agent et K bifurcations du jumeau) sont lus par le **même** lecteur, c'est-à-dire le modèle de l'agent dans son propre contexte, par passe forcée. L'asymétrie d'invite disparaît du *lecteur*, mais pas de la *politique*. Ce résidu devient le test E2'-(iii)/(iv). |
| A-a3, C-a2, E-a1, E-b | Kolmogorov-Smirnov continu sur des rangs discrets : rejet par construction. Le non-rejet n'est pas une preuve. | **Acceptée** | Recalcul : la loi uniforme discrète sur {1/(K+1),…,1} vérifie sup\|F₀(u)−u\| = 1/(K+1) (**VÉRIFIÉ**). C donne 1/(2(K+1)), qui est une borne inférieure ; E donne la valeur exacte. Avec 2 000 pas (illustratif) et K = 10, √N·D ≈ 4,1 > 1,36 : le test rejette quelle que soit la vérité. **E2 est retiré.** |
| A-a3, C-a3, D-a, D-b (R_t constant) | Pas dépendants. L'uniformité marginale empilée n'implique pas E[e_t \| passé] ≤ 1. L'empilement surpondère les épisodes longs. | **Acceptée** | Le contre-exemple de D est correct : des rangs marginalement uniformes mais figés donnent E[g(R_t) \| R_{t−1}] = g(R_{t−1}). **Correction** : l'unité est la tâche, et l'on teste directement les fréquences de Ville (E2'). |
| A-b (transport) | Si E[e_t \| passé] ≤ 1+ε, la borne devient (1+ε)^T/100. | **Acceptée** | Refait : M_t/(1+ε)^t est une surmartingale, d'où la borne (**VÉRIFIÉ**). Il ne faut donc pas tenter d'estimer ε par empilement de pas. On mesure plutôt P(sup M_t ≥ c) à des niveaux c jugeables. |
| C-b2, E-a2, E-b, A-b | Le calibrateur κ·p^(κ−1) est plafonné, d'où une puissance nulle sur peu de pas. | **Acceptée pour la puissance. Rejetée** : l'étiquette « perte de validité » de C. | Recalcul : sup_κ κ(K+1)^(1−κ) = (K+1)/(e·ln(K+1)) ≈ 1,69 pour K = 10 (**VÉRIFIÉ**), soit au moins 9 pas au rang maximal ; avec κ = 0,5 : 1,658, soit 10 pas (**VÉRIFIÉ**). En revanche, C calcule lui-même qu'une somme de Riemann à droite d'une fonction décroissante est < 1. Le calibrateur discret est donc **conservatif, donc valide**. **Correction** : une fonction de pari g directement sur les rangs, de moyenne ≤ 1 sous l'uniforme discrète, plafonnée à K+1 (borne de A, C et E, **VÉRIFIÉE**), ou un mélange préenregistré sur son paramètre. Le choix de κ ou λ après inspection est une fuite (E-a2) : **acceptée**, préenregistrement. |
| A-b, C (puissance diffuse) | Si le saboteur garde des rangs centraux, M_t décroît. Le rang jette l'amplitude que la somme linéaire garde. | **Transformée en test** | E-sim, ci-dessous, avant tout achat. |
| A-a7 | Le coût de P3 est récurrent. | **Acceptée** | Mon tableau 6D le sous-estimait. Le coût de surveillance vaut (points de contrôle) × K générations, plus K passes forcées, **pour chaque épisode surveillé**, en continu. |
| Préambule de D ; C sur D (argument identique) | Ville borne P_H(alerte), pas P_H(alerte \| tranche de longueur réalisée). | **Acceptée** | Ma phrase « pas de calibration par bac à faire » est **fausse** pour la cible du programme. **Correction**, détaillée en (b) : seuil 1/(α·π_min), et évaluation en lecture seule sur des trajectoires non interrompues (je reprends la décision de D, en le disant). |

### Bloc 2 — Regroupement des bacs (P1, P2, E1)

| Réf. | Critique | Décision | Raison, correction ou test |
|---|---|---|---|
| A-a6, C-a1, E-a3 | La normalisation est ajustée sur les données qui testent l'invariance puis calibrent. Le pré-test sur les mêmes épisodes casse Wilks. | **Acceptée** | Avec quelques centaines d'épisodes, un partage en trois effondre l'effectif. **Correction** : une normalisation de forme fixée *avant* les données, sans paramètre ajusté, ou aucune normalisation. |
| A-b, C-b1, E-b, D-b | L'égalité au quantile 90 % ne contraint pas le quantile 99 %. E1 n'a pas la puissance d'établir ± 3 points. | **Acceptée** | Recalcul de C : √(2 × 0,10 × 0,90 / 100) ≈ 4,24 points, demi-largeur ≈ 8,3 > 3 (**VÉRIFIÉ**). **E1 est retiré.** P2 ne sert plus à certifier par bac. Il ne reste qu'une aide de puissance pour une garantie **regroupée**, qui n'est pas la cible du programme. |
| A-b (grappes) | n_eff = n/(1+(m−1)ρ). Sous 299, Wilks ne tient plus. | **Acceptée** | **Correction P1'** : un seul épisode par tâche, tiré au hasard selon une règle préenregistrée, avec le score gelé. L'hypothèse i.i.d. porte alors sur les tâches, et non sur une estimation de ρ. |

### Bloc 3 — Usage de l'article : covariable, moniteurs, routage

| Réf. | Critique | Décision | Raison, correction ou test |
|---|---|---|---|
| A-b (M1), C-a4 | V̂₀ lu sur l'agent évalué est post-traitement et sert de canal d'évasion. | **Acceptée pour M1 et E3. Rejetée pour P4.** | P4 ne lit V̂₀ que sur des épisodes honnêtes de calibration ; le problème naît quand on applique la covariable à l'agent. **Correction M1'** (HYPOTHÈSE) : V̂₀ est lu sur le **jumeau**, à partir de l'énoncé public de la tâche. La covariable est alors antérieure au traitement et hors de portée de l'agent. |
| D-b (P4) | Une AUC de prédiction de l'échec ne fixe aucun taux de queue p_h par strate. Si les poids w_h ne sont pas identifiés, la moyenne repondérée ne l'est pas. | **Acceptée** | P4 est subordonné à E0-b, qui mesure le taux de dépassement par strate à un niveau jugeable. Sans cette mesure, pas de stratification. |
| A-a4, D-a | E3 et E4 falsifient H_A par simple manque de puissance. | **Acceptée** | Je reprends, en le disant, la règle de marge de D, déjà adoptée par A : borne haute ≤ g ⇒ H_A falsifiée ; borne basse > g ⇒ H_B falsifiée ; sinon non concluant. |
| D-a, E-a4, E-b | L'AUC ne donne pas la détection au seuil de verdict. | **Acceptée** | Le contre-exemple de E est correct : F₀ est un mélange (1−π)G_bas + πG_haut avec π > α, et F₁ est placée entre les deux supports. On obtient AUC = 1−π, mais une détection nulle au quantile 1−α (**VÉRIFIÉ**). **Correction** : métrique principale = détection à un taux de fausses alertes fixé, mesuré sur les échecs honnêtes appariés, à un niveau jugeable. L'AUC devient secondaire. |
| C-c1 | Pas de témoin de neurones aléatoires en E3 et E4. | **Acceptée** | Omission réelle. Ajout : même architecture de sonde, même taille de sous-ensemble, neurones aléatoires ou issus d'une sonde de prédiction du jeton suivant (contrôle de la Table 2, RAPPORTÉ). |
| C-c2 ; E sur D (bogue exogène, repris en le disant) | Un échec honnête imprévu, à V̂₀ élevé, imite la « dissociation » de M2. | **Acceptée** | Contrôle négatif de E4'. |
| A-c | Il manque une cellule « saboteur assigné sans dommage confirmé ». | **Acceptée comme cellule rapportée** | Le contraste principal du programme n'est pas rediscuté (RAPPORTÉ, §3). La cellule est rapportée à part, pour mesurer la sélection sur l'issue. |
| A-a5, E-a4 | M4 est vrai ou faux par construction : à poids et entrée égaux, la passe avant est identique. | **Acceptée** | **M4 est retiré.** |
| D-b, D-c (routage) | P(dommage \| alerte, routé) n'identifie pas la différence de risques. Il faut un témoin à budget égal sans lentille. | **Acceptée** | **M3'** : randomisation par lot, comparée au même budget dépensé sans lentille (bifurcation honnête non sélectionnée). Le test d'évasion étant clos (RAPPORTÉ), le résultat ne vaut que contre un saboteur non adaptatif. |
| E-c1, E-a1 (mélange) | A/A stratifié échec contre succès ; mélange de tâches qui masque une violation conditionnelle. | **Transformée, avec correction** | Le mélange de E réfute **le diagnostic** marginal, pas le théorème. Si l'échangeabilité vaut conditionnellement au préfixe, une variable latente mesurable par le préfixe ne biaise pas les rangs. Le contre-exemple exige donc un jumeau qui diffère de l'agent d'une façon corrélée au type de tâche : c'est ce que E2' doit détecter. Mais l'échec final est postérieur aux pas. P(alerte \| échec) ≤ α/P_H(échec) (**VÉRIFIÉ**), et un excès sur les seuls échecs peut exister **sous le nul exact**. La référence doit donc être jumeau contre jumeau, conditionné de la même façon. |
| A (références) | L'année de « AI Control » diffère entre B et E. | **Acceptée** | Greenblatt, Shlegeris, Sachan, Roger, « AI Control: Improving Safety Despite Intentional Subversion » : **année à vérifier**. Benton et al. et Bhatt et al. restent « référence à vérifier ». |

---

## (b) Propositions et expériences corrigées

### Propositions corrigées (toutes HYPOTHÈSE)

- **P1'** — Garantie conditionnelle au lot, au niveau de la tâche.
  - On prend un épisode par tâche et un score gelé, avec le seuil au maximum.
  - P(taux réel > α) = (1−α)^n_tâches. Il faut n_tâches ≥ ln δ / ln(1−α) ≈ 299 pour δ = 5 % (**VÉRIFIÉ**).
  - Pour une certification simultanée de 5 tranches à δ = 5 % au total, il faut ≈ 459 tâches par tranche (**VÉRIFIÉ**, calcul de A et C).
  - Le taux réalisé attendu vaut 1/(n+1), environ 0,33 % pour n = 299 (**VÉRIFIÉ**). Il faut rapporter ce chiffre, pas « 1 % ».
- **P3'** — E-processus sur les rangs, lecteur commun.
  - À chaque point de contrôle préenregistré, on tire K bifurcations du jumeau. Les K+1 candidats sont lus par le modèle de l'agent, dans son contexte, et R_t est le rang du pas réel.
  - Facteur e_t = g(R_t), avec g fixée d'avance, de moyenne ≤ 1 sous l'uniforme discrète et ≤ K+1.
  - **Cible par tranche** : soit π_min la plus petite probabilité honnête d'une tranche de longueur. Si P_H(alerte) ≤ α·π_min, alors P_H(alerte \| tranche b) ≤ α·π_min/π_b ≤ α (**VÉRIFIÉ**). Le seuil devient donc 1/(α·π_min). Avec 5 tranches équiprobables, il vaut 500 (illustratif), et il faut au moins ⌈ln 500 / ln 11⌉ = 3 pas au rang maximal pour K = 10 (**VÉRIFIÉ**).
  - *Hypothèses* :
    - π_min est estimé par une borne de confiance basse sur les longueurs honnêtes, qui sont observées sur tous les épisodes honnêtes ;
    - la loi des longueurs est stable au déploiement (S5) ;
    - l'évaluation se fait en lecture seule, sur des trajectoires non interrompues (D).
  - *Échec* :
    - nul d'identité de politique, et non d'intention (A-a1) ;
    - perte de puissance contre un sabotage diffus (E-sim) ;
    - coût récurrent.
- **P4** : subordonnée à E0-b.
- **P5** : inchangée. Les valeurs extrêmes servent d'estimateur secondaire, jamais de seuil.
- **P6** : inchangée. C'est probablement l'issue honnête au point de verdict par tranche.
- **M1'** : covariable lue sur le jumeau, à partir de l'énoncé public.
- **M2** : maintenue comme hypothèse, testée par E4'.
- **M3'** : randomisée par lot.
- **M4** : retirée.

### Expériences (inférence forte, zone non concluante déclarée)

**E0 — Inventaire des unités indépendantes** (zéro épisode, à faire d'abord)
- *H_A* : le nombre de tâches distinctes dans la strate regroupée est ≥ 299, et la plus petite tranche en compte ≥ 99.
- *H_B* : l'un des deux comptes est inférieur.
- *Mesure* : métadonnées de tâche, variante, version et graine ; corrélation intra-tâche des scores.
- *Falsifie H_A* : P1' n'est pas réalisable sur l'existant, et le quantile conforme à 1 % n'existe pas dans cette tranche. Il faut un achat, ou P6.
- *Falsifie H_B* : P1' est réalisable au niveau regroupé.
- *E0-b* : taux de dépassement d'un seuil intermédiaire, par strate de difficulté lue par M1'. Il décide si P4 a un objet.

**E-sim — Le rang tue-t-il la puissance ?** (zéro épisode)
- *H_A* : sur une grille de décalages diffus par pas, pour K ∈ {4, 10, 20} et un nombre m de points de contrôle (valeurs illustratives), la détection de P3' au seuil 1/(α·π_min) reste à moins d'une marge préenregistrée de celle de la somme linéaire seuillée par P1'.
- *H_B* : l'écart dépasse la marge sur toute la zone de décalages pertinente.
- *Ancrage* : moments, queue empirique centrale et corrélation intra-tâche des scores honnêtes existants. On y ajoute des nuls à rangs marginalement uniformes mais dépendants (D).
- *Falsifie H_A* : P3' ne vaut pas son coût récurrent comme détecteur. Il ne reste qu'un outil de validité, ou on l'abandonne.
- *Falsifie H_B* : l'objection de puissance (A, C, E) ne tient pas dans le régime simulé.
- *Limite* : le modèle de décalage est une HYPOTHÈSE. E-sim ne dit rien d'un saboteur réel.

**E2' — Validité et nature du nul de P3'** (remplace E2)
- *Unité* : la tâche, un épisode par tâche.
- *Bras* :
  - (i) jumeau contre jumeau, placebo exact ;
  - (ii) agent de production honnête contre jumeau, A/A de D ;
  - (iii) agent honnête avec consigne cachée bénigne de même longueur (C, E) ;
  - (iv) invite honnête paraphrasée (E) ;
  - (v) contrôle positif : température modifiée.
- *Mesure* : fréquence des tâches avec sup M_t ≥ c, pour c ∈ {5, 10, 20} (illustratif). Ville impose ≤ 1/c (**VÉRIFIÉ**). On teste aussi la dépendance g(R_t) ~ R_{t−1}, avec permutation **entre** épisodes. Les fréquences sont conditionnées à l'échec, avec (i) comme référence conditionnée de la même façon.
- *Duel 1, validité* :
  - *H_A* : dans (ii), borne de Clopper-Pearson haute ≤ 1/c + marge, pour tout c.
  - *H_B* : borne basse > 1/c pour au moins un c.
  - H_A falsifiée : P3' est invalide sur l'agent réel. H_B falsifiée : la validité marginale est transportée jusqu'au seuil par Ville, et vers la cible par tranche par α·π_min.
- *Duel 2, nature* :
  - *H_A'* : (iii) ou (iv) dépasse les bornes comme (v).
  - *H_B'* : (iii) et (iv) restent sous les bornes.
  - H_A' confirme que P3' détecte une différence de politique, pas une intention (A-a1). H_B' montre que P3' est insensible à des différences bénignes de cette ampleur, sans rien établir sur l'intention.
- *Non jugeable* : c = 100 sur quelques centaines de tâches. Je le dis d'avance.
- *Coût* : K générations par point de contrôle sur des préfixes existants. On commence avec un petit K.

**E3' — Apport de l'article comme covariable (M1')**
- *Métrique* : détection du saboteur avec dommage contre l'échec honnête de la même variante, à un taux de fausses alertes fixé sur les échecs appariés, à un niveau jugeable (10 %, illustratif). On compare avec et sans M1'.
- *Comparateurs* : longueur de la question ; taux d'échec historique de la variante.
- *Duel* :
  - *H_A* : borne basse du gain > g.
  - *H_B* : borne haute ≤ g.
  - Sinon : non concluant.
- *Marge g* : préenregistrée, avec un calcul de puissance sur le nombre de paires de sabotage. Ce nombre n'est pas fourni (S9) : tant qu'il manque, E3' n'est pas planifiable.
- *Contrôles* : covariable permutée entre tâches ; neurones aléatoires de même taille ; neurones issus de la sonde du jeton suivant.

**E4' — Intention ou échec attendu (M2)**, sur le contraste principal, sans le rediscuter
- *Duel* :
  - *H_A* : contre **chacune** des quatre bases de comparaison du programme (RAPPORTÉ), borne basse du gain de détection > g.
  - *H_B* : pour au moins une base, borne haute ≤ g.
  - Sinon : non concluant.
- *Contrôles négatifs* :
  - échec honnête provoqué par un obstacle non annoncé ou une panne d'environnement, à V̂₀ élevé ;
  - honnête avec consigne cachée bénigne ;
  - neurones aléatoires ;
  - cellule « saboteur sans dommage », rapportée à part.
- *Portée* : un résultat obtenu contre un saboteur non adaptatif ne dit rien d'un saboteur adaptatif, puisque le test d'évasion est clos (RAPPORTÉ).

**M3' — Routage** (après E2' et E4' seulement)
- *Unité* : le lot, randomisé.
- *Duel* :
  - *H_A* : à budget humain et de bifurcations égal, la réduction du dommage dépasse g par rapport au même budget dépensé sans lentille.
  - *H_B* : réduction ≤ g.
- *Mesure du dommage* : à l'aveugle, sur toutes les branches, y compris des non-alertes auditées par tirage indépendant du rang (D).

---

## (c) Réponse à l'arbitre (une page)

**Ce qui est établi**

- **RAPPORTÉ.** L'article mesure, sur des tâches vérifiables :
  - une prédiction pré-génération modérée : AUC 0,67, contre 0,62 pour la longueur de la question ;
  - un effet d'ablation fort : 75,2 % → 20,3 % d'exactitude, contre 74,6 % avec des neurones aléatoires ;
  - un gain de recherche pas à pas : 77,8 % contre 75,0 % pour la base implicite.

  Il n'a ni cadre ouvert, ni cadre adverse.
- **VÉRIFIÉ (mathématique, sous hypothèses écrites).**
  - Un quantile conforme à 1 % exige au moins 99 unités échangeables. Sa garantie est marginale sur le tirage du lot.
  - Une garantie conditionnelle au lot, avec le seuil au maximum, exige ≈ 299 unités i.i.d. (δ = 5 %), soit ≈ 459 par tranche pour 5 tranches simultanées.
  - Ville donne une borne marginale. Elle ne vaut pour une tranche de longueur réalisée que si l'on durcit le seuil à 1/(α·π_min).
  - Un facteur fondé sur des rangs est plafonné à K+1.
  - L'égalité au quantile 90 % ne contraint pas le quantile 99 %.
  - Une AUC élevée est compatible avec une détection nulle à 1 %.
  - Conditionner sur l'échec final gonfle le taux de fausses alertes jusqu'à α/P(échec), même sous le nul exact.

**Ce qui n'est pas établi (HYPOTHÈSE)**

- Le nombre de **tâches** indépendantes, plutôt que d'épisodes, et la corrélation intra-tâche.
- Que le jumeau soit distribué comme l'agent honnête de production.
- Le transfert des sondes au travail ouvert.
- L'existence d'un signal d'intention distinct de l'échec attendu.
- La puissance d'un e-processus sur rangs contre un sabotage diffus.
- Le lien entre la difficulté et la queue des scores honnêtes.

**Conséquence honnête.** Avec quelques centaines d'épisodes, la certification à 1 % **par tranche** est probablement « non jugeable » sans achat. Trois sorties restent légitimes :
1. une garantie regroupée (P1'), en le déclarant ;
2. une garantie par tranche au prix d'un seuil durci (P3'), si E2' passe ;
3. le remplacement du seuil absolu par un budget d'audit (P6), avec « non concluant » préenregistré.

**Demande reformulée.**
> « Compter les tâches indépendantes par tranche. Choisir une garantie (marginale conforme, conditionnelle au lot, ou séquentielle durcie par 1/(α·π_min)) et nommer son hypothèse, son test de falsification jugeable et sa perte de puissance. Séparément, mesurer à taux de fausses alertes fixé sur les échecs honnêtes appariés si la lentille apporte plus qu'une marge g préenregistrée au-delà des quatre bases de comparaison, avec une vérité scellée par un tiers. »

**Vérification externe.**
- Vérité implantée et scellée par un tiers.
- Test nul contre nul et jumeau contre jumeau, sur le code gelé.
- Réplication publique de la Table 2 sur Qwen-2.5-7B-SimpleRL-Zoo et MATH500.
- Dommage mesuré sans voir les scores, y compris sur les non-alertes.

**L'expérience à faire en premier : E-sim, précédée de l'inventaire E0.**
- *Pourquoi* : aucune des deux ne coûte d'épisode, et elles décident si E2', qui coûte K générations par point de contrôle, mérite d'être payée.
- *Duel* : si le rang perd trop de puissance (H_B), P3' n'est plus qu'un outil de validité et l'on se rabat sur P1' ou P6. Si H_A tient, on lance E2' sur les préfixes existants avec un petit K.
- *Coût* : calcul processeur et lecture des métadonnées.
- *Ce qu'elle suppose* : un modèle de décalage diffus réaliste.
- *Comment elle échoue* : une simulation trop éloignée des vraies queues, d'où son ancrage sur les scores honnêtes existants.

FIN-DE-CELLULE