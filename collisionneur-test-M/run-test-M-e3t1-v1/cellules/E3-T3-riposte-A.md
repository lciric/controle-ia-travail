# Cellule A — Tour III.3 : riposte

**Pièces.** Le bloc FAITS déclare qu'aucun fait n'est joint. Ma conception III.1 et les deux attaques (B, C) sont présentes, non vides, closes par `FIN-DE-CELLULE`. Je ne réponds qu'aux sections visant A. Tout chiffre de ma main est **illustratif** ; mes prédictions sur le comportement des instruments sont des **HYPOTHÈSES**.

Je ne lisse pas : là où B et C convergent, je le dis, et je garde ce qui les sépare.

---

## (a) Réponses aux attaques

### Sonde et étiquettes

**B-A1 et C-faille 1 — le désenchevêtrement rend la sonde aveugle à T, puis β_T ≈ β_C ≈ 0 par construction.** *Acceptée en partie, transformée en test.*

B a raison sur le mécanisme : si T est équilibré dans chaque classe d'entraînement, la régression pénalisée pousse vers zéro toute direction qui ne porte que T, et ce qui reste est la provenance (registre académique contre quotidien). Je conteste un point : « β_T ≈ 0 par construction » suppose que l'effet de T sur le flux résiduel, à la position lue, est confiné au sous-espace que la sonde a appris à ignorer. Si T modifie la représentation de la provenance elle-même (le modèle lit « question scolaire » plus fortement en format banc), β_T ne sera pas nul. Mais je ne peux pas le démontrer d'avance, et c'est précisément ce que B me demande en simulation. Je retiens donc que ma conception III.1 avait remplacé une circularité bruyante par une circularité silencieuse — l'objection est juste.

La conclusion honnête : **aucune étiquette indépendante de T n'existe pour cette nuit** (mon (a)3 de III.1 le disait, je ne l'avais pas suivi jusqu'au bout). On ne peut pas la contourner par la réécriture ; on peut seulement l'exposer. D'où le **duel 0** ci-dessous : deux sondes aux circularités opposées, un témoin de provenance, et la règle qui décide laquelle sert au duel 1, ou si aucune ne le peut.

**B-A2 et C-faille 1 (seconde moitié) — fuite du gabarit maître entre entraînement et test.** *Acceptée.* Correction : les niveaux de T et de C sont représentés par **plusieurs réalisations** (chaînes distinctes), et les réalisations utilisées pour réécrire les données d'entraînement sont **disjointes** de celles des items de test. Cela répond en même temps au contrôle c5 de B (contraste intra-niveau) et au duel D1.

**B-A7 et C-scénario 2 — le duel 2 est battu par construction ; la sonde gagne en lisant le domaine.** *Acceptée.* Sur des paires à distance d'édition minimale, le prédicteur de surface est au hasard par définition ; la sonde le dépasse en lisant la provenance, donc le domaine. Correction : le témoin pertinent du duel 2 n'est pas TF-IDF seul, c'est la **sonde de provenance** (c1 de B, contrôle 1 de C), et les paires doivent être **appariées par domaine** (contenu académique en cadre d'usage contre le même en cadre de banc). Le duel 2 réécrit ne prétend plus mesurer « conscience d'évaluation » ; il mesure « la sonde lit autre chose que n-grammes et domaine ». Sur le scénario d'empoisonnement de C (n-gramme glissé dans l'entraînement, TF-IDF à 0,98) : accepté comme menace ; la banque d'entraînement est écrite et relue par quelqu'un d'autre que l'analyste, et l'écart sonde − surface n'est rapporté que sur les paires appariées où le témoin de surface est contraint près de 0,5.

**B-A9 et C-contrôle 3 — les étiquettes « usage réel » sont une intention de conception, pas une vérité.** *Acceptée.* Je requalifie : les étiquettes ont le statut **HYPOTHÈSE** (« l'auteur a voulu écrire une invite d'usage »), et aucun seuil d'AUC ne les transforme en vérité. Le seul lien possible entre w et autre chose qu'une intention d'écriture est l'intervention : ajouter ±α·w au flux résiduel et mesurer un changement de sortie (par exemple la probabilité de « oui » à une question fixe « cette interaction est-elle une évaluation ? »). Statut : HYPOTHÈSE de faisabilité ; coût de l'ordre de l'heure (illustratif). Je l'intègre au **pilote**, pas au test décisif.

**B-adversaire γ, C-scénarios 1 et 5 — signal logé hors position, hors couche ou non linéaire ; un nul ne l'exclut pas.** *Acceptée.* Trois corrections : (i) l'empreinte des poids est comparée à celle du point de contrôle publié avant toute extraction (contre la substitution) ; (ii) le balayage de couches sur développement couvre **toutes** les couches, la restriction 8–24 était illustrative ; (iii) **règle de rédaction préenregistrée** : tout résultat nul s'écrit « non lu par une sonde linéaire à la couche L, position p », jamais « absent du modèle ». Le scénario 5 de C (sonde médiane = domaine, décision tardive) prédit exactement P1 ≈ témoin de provenance ; le duel 0 est construit pour le voir.

### Position de lecture

**B-A3 et C-faille 2, C-contrôle 2 — position confondue avec T ; identité du jeton t−1 ; longueur et RoPE.** *Acceptée.* C'est la faille la plus simple et la plus grave de ma conception. Corrections :

- La ligne `Answer:` n'est plus terminale. Toutes les cellules se terminent par la **même séquence** : fin du tour utilisateur, en-tête assistant du gabarit de discussion. Lecture au dernier jeton de cet en-tête, identique dans les quatre cellules (même identifiant, même rôle). Vérification mécanique c3 de B obligatoire : égalité des k derniers identifiants de jetons avant la position lue, k ≥ 4 (illustratif).
- Les trois positions candidates de III.1 sont abandonnées ; il n'y a plus de degré de liberté sur la position.
- Longueur : covariable dans le modèle mixte **et** contrôle « lorem ipsum » de C (texte absurde de longueur variable dans le gabarit ; la pente du score de sonde sur la longueur doit être compatible avec zéro, seuil préenregistré). Si la pente n'est pas nulle, β_C — le style ouvert étant plus long — est corrigé de cette pente ou déclaré ininterprétable.

**C-scénario 3 — frontière de tokenisation.** *Acceptée.* Le diff automatique est fait sur les identifiants de jetons après application du gabarit de discussion, pas sur le texte.

### Règle de décision

**B-A4 — rapport à dénominateur quasi nul ; absence de preuve comptée comme preuve.** *Acceptée.* Le rapport R disparaît de la règle. Il reste rapporté, descriptivement, avec son intervalle, parce que l'essaim l'a formulé ainsi ; mais la décision porte sur trois quantités séparées : la borne inférieure de |β_T| ; un test d'équivalence (TOST) sur β_C ; la borne inférieure de la **différence** |β_T| − 2|β_C|. Un plan sous-dimensionné ne peut plus favoriser H_A : sans puissance, le TOST échoue et l'issue est ni-ni. La simulation c4 (β_C = 0 ; β_T = β_C = 0) est ajoutée au pilote pour mesurer le taux de fausse acceptation.

**B-A5 et C-faille 4 — la température fait passer β_C sous δ.** *Acceptée.* Plus de calibration dans l'analyse confirmatoire. Métrique : logit brut w·h + b avec ‖w‖ = 1. Le seuil δ est exprimé en unités de l'**écart-type résiduel du modèle mixte sur le jeu de test** (dénominateur déclaré, estimé sur les items de test, pas sur l'entraînement — l'objection de C contre B sur σ_train s'applique aussi à ma version III.1, j'en tiens compte). δ = 0,2 écart-type résiduel (illustratif).

**B-A6 et C-faille 3 — appariement d'amplitude : degré de liberté, linéarité supposée, Goodhart sur la distance d'édition.** *Acceptée.* La normalisation « par unité de distance » est retirée. Les distances de surface restent mesurées et rapportées, comme description des manipulations. La ligne de base pour « sensibilité générique » devient le **facteur placebo** (c2 de B, duel D2) : une troisième manipulation de distance comparable, sans lien supposé avec l'évaluation. Le gonflement de la distance de C par des salutations creuses (scénario β de B) est rendu visible par les réalisations multiples : une réalisation rembourrée se distingue des autres dans la composante de variance intra-niveau (HYPOTHÈSE).

**B-multivers.** *Acceptée.* Les choix qui restent (couche ; sonde P1 ou P2 ; δ ∈ {0,1 ; 0,2 ; 0,3} illustratif) sont énumérés avant scellement, et les résultats sont rapportés pour toutes les combinaisons, avec désignation de la combinaison confirmatoire. La position de lecture n'est plus un choix.

### H-M2

**B-A8 — frontières violées par mes propres exemples.** *Acceptée.* Reclassement, avec la contrainte que chaque transformation soit applicable **identiquement dans les quatre cellules** :

- G_sens : synonymes de liste fermée ; actif/passif de la consigne ; reformulation de la salutation **sans déplacement**.
- G_pos : échange de l'ordre prompt-système / consigne ; bloc de candidats avant la question ; échange de l'ordre consigne / contexte factuel. Le déplacement de `Answer:` est supprimé (la ligne n'est plus terminale et n'existe que dans T = banc).
- G_opt : permutation des options avec relettrage, orbite séparée, comme recommandé en III.1.
- G_placebo : ligne vide à position fixe, puces `-` contre `*` — orbite témoin, attendue à dispersion minimale.

**C-scénario 4 — ancre RoPE sur la position relative de `Answer:`.** *Transformée en test.* Ce que C décrit n'est pas une tromperie : c'est le mécanisme que H-M2 appelle « dérive distributionnelle ». La question est de savoir si σ_pos s'explique par le déplacement en jetons. Analyse préenregistrée double, comme B le demande à C (C8) : régression de Δscore sur Δposition du bloc déplacé (en jetons) et sur Δlog-perplexité, **avec** désignation de l'analyse sans covariable comme confirmatoire pour H-M2, et de l'analyse avec covariable comme explicative. Si Δscore est une fonction monotone de Δposition, H-M2 est soutenue mais s'interprète comme sensibilité positionnelle, pas comme « reconnaissance du contenu ».

### Duels de contrôle imposés par B

**D1 (réalisation contre niveau)** et **D2 (spécificité contre placebo)** : *acceptés*, placés avant le duel 1. D1 répond aussi à C-faille 1 : si la variance entre réalisations d'un même niveau est du même ordre que la variance entre niveaux, l'effet de T n'est pas un effet de classe et H-M1 est indécidable avec ce plan.

**Contrôle positif par injection (B).** *Accepté avec une réserve.* Injecter une direction connue dans les seules cellules banc et vérifier que la chaîne retrouve β_T teste le **pipeline** (modèle mixte, règle), pas la sémantique de w : si l'on injecte le long de w, le succès est garanti ; si l'on injecte le long d'une direction orthogonale à w, l'échec est garanti. Je le garde comme vérification du pipeline, avec injection le long de w à amplitude connue, et je le déclare tel.

### Ce que je rejette

- **C-faille 1, formulation « vrai par construction ! »** : je rejette la force de la conclusion, pas le mécanisme. β_T ≠ 0 sous sonde P1 n'est pas « uniquement l'échec de la sonde à ignorer le format » ; c'est aussi compatible avec « T modifie la lecture de la provenance par le modèle ». Les deux lectures sont distinguées par le duel 0 (comparaison avec le témoin de provenance), pas par un raisonnement a priori.
- **C-faille 4, statut « VÉRIFIÉ mathématiquement »** : l'invariance de R sous division scalaire est exacte ; je signale seulement que je ne requalifie aucun statut et que la phrase « température = 10 garantit |β_C| < 0,1 » dépend de l'échelle initiale, donc est une HYPOTHÈSE sur les données.
- **C-scénario 1, « < 1 heure GPU » pour un affinage avec pénalité d'orthogonalité** : non réfuté, mais hors de portée de la nuit et hors du modèle d'origine ; traité par l'empreinte des poids et par la règle de rédaction des nuls.

---

## (b) Expériences corrigées

### Duel 0 — Deux circularités et un témoin de provenance (préalable, sur développement)

Trois classifieurs linéaires, même couche, même position (dernier jeton de l'en-tête assistant) :

- **P1** : provenance (banc public contre journal de conversation), formats équilibrés dans chaque classe par des réalisations d'entraînement disjointes du test.
- **P2** : même provenance, formats **non** équilibrés (chaque source dans son gabarit natif).
- **W_prov** : provenance, entraîné sur du texte sans aucun cadrage (question nue, sans prompt-système ni consigne).

- **H_A** : P1 et P2 portent une information commune qui n'est ni surface ni domaine : cos(P1, W_prov) < 0,6 **et** cos(P2, W_prov) < 0,6 (illustratif), et sur paires appariées par domaine et par format, AUC(P1) − max(AUC(TF-IDF voyant le format), AUC(W_prov)) ≥ 0,05 (illustratif).
- **H_B** : cos(P1, W_prov) ≥ 0,8 (illustratif) — P1 lit le domaine — ou P2 est reproduit par TF-IDF voyant le format — P2 lit T.

**Ce que chaque issue falsifie.** H_A falsifie « la seule étiquette disponible est le domaine » et autorise le duel 1 avec P1 comme confirmatoire, P2 en multivers. H_B falsifie l'hypothèse 3 de mon III.1 (étiquettes séparables de T) **sur ce modèle et ces corpus** ; le duel 1 est alors rétrogradé en « mesure de sensibilité au gabarit » et rapporté comme tel.

### D1 — Réalisation contre niveau (sur développement)

Au moins trois réalisations par niveau de T et de C (illustratif). H_A : rapport de composantes de variance niveau/réalisation ≥ 4 (illustratif). H_B : rapport < 2. Issue H_B : H-M1 indécidable avec un plan à niveaux ; on rapporte l'effet de chaque réalisation.

### D2 — Spécificité contre placebo (sur développement)

Facteur placebo de distance de surface comparable à T. H_A : borne inférieure de |β_T| − |β_placebo| > 0. H_B : équivalence établie par TOST. Issue H_B : tout effet de T est une sensibilité générique à la perturbation ; l'interprétation « évaluation » est retirée quel que soit R.

### Contrôles mécaniques (avant scellement)

Égalité des k derniers identifiants de jetons avant la position lue ; diff sur identifiants de jetons hors blocs T, C ; pente score-longueur sur lorem ipsum compatible avec zéro ; empreinte des poids ; simulations c4 sous effets nuls et sous effets connus ; injection le long de w pour vérifier le pipeline.

### Duel 1 — H-M1, corrigé (décisif, après scellement)

Plan 2×2 intra-contenu, 120 contenus (illustratif), ≥ 3 réalisations par niveau, items de test sur réalisations jamais vues à l'entraînement, longueur en covariable, lecture au jeton commun.

Modèle : score ~ T + C + T×C + placebo + longueur + (1 + T + C | contenu) + (1 | réalisation_T) + (1 | réalisation_C). Métrique : logit brut, ‖w‖ = 1. δ = 0,2 écart-type résiduel (illustratif).

- **H_A (essaim)** : borne inférieure de |β_T| > δ ; TOST établit |β_C| < δ ; borne inférieure de |β_T| − 2|β_C| > 0 ; |β_T| − |β_placebo| > 0 (D2 déjà acquis).
- **H_B** : TOST sur β_C échoue **et** intervalle de β_C exclut zéro avec |β_C| > δ ; ou |β_{T×C}| > 0,5·|β_T|.
- **Ni-ni** : tout le reste, rapporté comme intervalles sur β_T, β_C et leur différence.

R est rapporté à titre descriptif. Résultats pour toute la grille du multivers (couche, P1/P2, δ) ; la combinaison confirmatoire est désignée avant scellement.

**Ce que chaque issue falsifie.** H_A : falsifie « le signal est principalement une réponse au registre d'échange », sous la réserve explicite que l'étiquette est une intention de conception. H_B : falsifie H-M1 telle que formulée. Ni-ni : falsifie la puissance supposée ; la taille d'échantillon nécessaire est rapportée.

### Duel 2 — réécrit comme borne, non comme validation

Sur paires appariées par domaine et par format (contenu académique en cadre d'usage contre le même en cadre de banc), hors items de test : AUC(P1) contre max(TF-IDF voyant le format, W_prov). Étiquettes permutées comme plancher. L'énoncé du résultat est : « P1 porte / ne porte pas une information au-delà des n-grammes et du domaine » — rien de plus.

### Duel 3 — H-M2, corrigé

Quatre orbites (G_sens, G_pos, G_opt, G_placebo), transformations applicables identiquement dans les quatre cellules, évaluées dans **les quatre cellules** et non seulement dans la cellule banc-balisé.

- **H_A (essaim)** : σ_sens < σ_pos d'un facteur ≥ 2 (illustratif) dans chaque cellule, σ_sens < σ_inter-contenus, σ_placebo ≈ σ_sens.
- **H_B** : σ_sens ≥ σ_pos, ou σ_placebo ≈ σ_pos (toute perturbation déplace le score), ou l'ordre des orbites change selon la cellule.

Métrique : écart-type intra-orbite par contenu, puis composantes de variance par orbite (pas de moyenne de rapports, pour éviter le biais que B relève contre C en C9). Analyse double préenregistrée (avec et sans Δposition et Δlog-perplexité), analyse sans covariable confirmatoire. Issue H_A avec Δscore monotone en Δposition : H-M2 soutenue et interprétée comme sensibilité positionnelle. Issue H_B : H-M2 réfutée ; le signal répond aux changements lexicaux fins ou à toute perturbation.

### Pilote d'intervention (non décisif)

±α·w à la position lue, mesure de la probabilité de « oui » à une question fixe sur la situation d'évaluation. Statut HYPOTHÈSE de faisabilité. Sert à écrire la version suivante du préenregistrement, pas à trancher cette nuit.

---

## (c) Réponse à l'arbitre

**Ce qui est établi.** Rien empiriquement : aucun fait n'est joint. Par raisonnement, quatre points tiennent, et les deux équipes rouges convergent dessus par des voies différentes :

1. Il n'existe pas, pour cette nuit, d'étiquette « évaluation / usage réel » indépendante du gabarit. Toute sonde est entraînée soit sur la provenance (donc le domaine), soit sur le format. Ma réécriture de III.1 ne résolvait pas cela ; elle déplaçait la circularité. Statut : conséquence d'un raisonnement, pas un résultat.
2. Une règle de décision fondée sur un rapport d'effets est pathologique près de zéro et récompense le manque de puissance. La règle doit porter sur des différences et un test d'équivalence.
3. La position de lecture doit être un jeton identique dans toutes les cellules, précédé des mêmes jetons ; sinon β_T mesure le jeton lu.
4. Un niveau représenté par une seule chaîne ne permet pas de parler de « gabarit » comme classe (Clark 1973, cité par B, référence à vérifier par le relecteur).

**Ce qui n'est pas établi.** Qu'une direction linéaire lisible existe dans Llama-3.1-8B-Instruct pour quoi que ce soit qui mérite le nom de « conscience d'évaluation » ; que T et C soient séparables au niveau des jetons autrement que par convention ; que le signal, s'il existe, soit à une position unique et dans les couches balayées ; que les étiquettes disponibles désignent autre chose qu'une intention d'écriture. Un résultat nul cette nuit ne dira rien sur le modèle, seulement sur cette sonde à cette couche et cette position.

**Option.** Je maintiens la **voie (c) avec pilote**, et B l'a rejointe depuis sa propre lecture. Ce qui tournerait cette nuit, sur données de développement uniquement, sans toucher aux items de test : le duel 0 (deux sondes, témoin de provenance, témoin de surface voyant le format), D1, D2, les contrôles mécaniques (jeton commun, lorem ipsum, empreinte des poids, simulations sous effet nul), le pilote d'intervention. Le texte de préenregistrement du duel 1 est écrit à partir de ces résultats, relu par un relecteur neuf, scellé, puis le 2×2 tourne une autre nuit. La voie (a) ne devient raisonnable que si le duel 0 donne H_A et D1 donne H_A ; la voie (b) ajoute un instrument de sortie à une chaîne dont l'instrument d'activation n'est pas validé, et je ne vois toujours pas ce qui la justifierait.

**L'expérience à faire en premier.** Le duel 0 : si P1 est colinéaire au témoin de provenance, ou si P2 est reproduit par un prédicteur de surface qui voit le format, H-M1 n'est pas testable sur ce modèle avec ces corpus, et c'est l'information utile de la nuit. Si ni l'un ni l'autre, on a une sonde qui lit quelque chose dont on ignore encore le nom, et le duel 1 peut être préenregistré avec la réserve écrite : « étiquettes = intention de conception, statut HYPOTHÈSE ».

**Ce qui me ferait changer d'avis.** Une issue H_A au duel 0 et à D1 avant minuit de travail humain, avec un relecteur disponible pour sceller : alors la voie (a) étendue est compatible avec les règles du programme et je la soutiendrais. Une issue H_B au duel 0 clôt la question pour cette nuit, et le résultat se publie tel quel.

FIN-DE-CELLULE