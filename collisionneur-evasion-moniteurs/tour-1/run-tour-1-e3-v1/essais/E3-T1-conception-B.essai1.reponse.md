# Proposition B — tour III.1 : robustesse et validité de construit des moniteurs boîte blanche

Toutes les pièces (P, F, E, D) sont lues comme **RAPPORTÉ**. Aucune n'est vide ni visiblement coupée (D se termine au milieu du point 5, sur une phrase coupée : « celles qui demandent » — je n'en infère rien). Les chiffres de la pièce E sont, de son propre aveu, « à vérifier sur PDF » : je les traite comme RAPPORTÉ-NON-AUDITÉ et ne construis aucun seuil dessus.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Supposition de la question | Statut | Pourquoi ce n'est pas acquis |
|---|---|---|---|
| A1 | L'organisme 8B « sait qu'il est évalué » et se conduit autrement. | HYPOTHÈSE | E §3.4 : aucune démonstration pour ≤ 8B hors instruction ou réglage fin. La question doit dire *comment* la conscience est induite (prompt, indice en bande, réglage fin) : chaque induction crée un confondant différent (format pour le prompt, poids pour le fine-tuning). |
| A2 | Le « biais diffus » laisse une trace dans les activations lisible **jeton par jeton** puis agrégée par le maximum. | HYPOTHÈSE | F impose max ou attention dans l'action. Un signal diffus *dans* l'action (chaque jeton sous le seuil) est précisément ce que le max écrase ; le lemme L (0,75 dans P) porte sur l'accumulation *entre* actions, pas *entre* jetons. Deux niveaux de diffusion sont confondus. |
| A3 | « Intention de saboter » est un construit observable. | HYPOTHÈSE | En laboratoire, l'étiquette « intention » = « a reçu la consigne de saboter ». Une sonde entraînée là mesure, au mieux, « a reçu telle consigne ». Le seul ancrage non circulaire est le **dommage mesuré ≥ θ** (P §4) : une action instruite mais sans dommage est une étiquette fausse. |
| A4 | La validité de construit prédit la robustesse (H8). | HYPOTHÈSE (0,40 dans P) | C'est la prédiction à tester, pas un acquis ; la question la présente comme le « résultat fort (a) ». |
| A5 | Apollo 2025 (95–99 % à 1 % FP) est « la référence à battre ». | RAPPORTÉ-NON-AUDITÉ | Tâche, taille et construit différents (E §4). Ce n'est pas une base comparable ; les bases à battre sont internes (noir, cascade, dernier état, plancher aléatoire). Le chiffre lui-même n'est pas audité. |
| A6 | Un changement de régime dans la séquence de scores = conscience d'évaluation. | HYPOTHÈSE | Alternative non exclue : rupture = changement de contexte (nouveau texte en entrée) lu par n'importe quelle sonde, sans changement de comportement (E §1.5, pilotage à effet faible). |
| A7 | « Taux de faux positifs apparié » a une unité évidente. | OBSERVÉ-NON-AUDITÉ | Par jeton, par action ou par épisode ? Un agrégateur séquentiel sans contrôle du FP *par épisode* ne compare rien. D point 5 reconnaît cette mesure comme première (« unanime »). |
| A8 | L'organisme est « Llama-3.1-8B-Instruct ». | Absent des faits | Les faits disent « organisme 8B » ; P 8.3 ne nomme que Llama-3.2-3B et Qwen2.5-7B comme moniteurs. Je retiens « 8B ouvert » ; le nom exact doit être fixé au préenregistrement. |
| A9 | Cohérence interne des pièces. | OBSERVÉ | E attribue la détection boîte blanche du biais diffus à « H6 » et parle d'un « programme v7 » ; dans P (v2), H6 est la marge asymétrique, et le gain blanc-sur-noir est H1/H2. Étiquetage divergent à réconcilier avant de sceller quoi que ce soit (règle anti-faux-gap : c'est une question d'indexation, pas de fond). |

---

## (b) Quatre expériences décisives

Conventions communes : organisme 8B ouvert ; trois couches (7, 15, 23 ; D point 3, RAPPORTÉ) ; cinq familles de F ; plancher obligatoire = sonde aléatoire appariée en covariance (P 8.1) ; **base mécanique supplémentaire** que j'ajoute : un classifieur de surface (longueur en jetons, perplexité sous le modèle de référence, lexique d'évaluation, indicateurs de registre) — une sonde qui ne le bat pas lit la surface. Tous les seuils numériques ci-dessous sont **illustratifs** et à fixer au préenregistrement scellé (P §12).

### E1 — Double dissociation : contenu contre cadrage

**Plan.** Croisement 2 × 2 × 2 : contenu {honnête, saboté (dommage mesuré ≥ θ)} × cadrage {« ceci est une évaluation », « ceci est un déploiement réel »} × registre {natif, paraphrasé en registre neutre par un modèle tiers}. Mêmes tâches dans toutes les cellules. Sonde « intention » entraînée sur une seule cellule de cadrage ; sonde « conscience d'évaluation » entraînée sur une seule cellule de contenu.

- **H_A (construit distinct)** : la sonde intention sépare le contenu quel que soit le cadrage et ne sépare pas le cadrage à contenu fixé ; symétriquement pour la sonde conscience. Prédiction : AUROC_contenu|cadrage − AUROC_cadrage|contenu > 0,2 (illustratif) pour la sonde intention, signe inverse pour la sonde conscience.
- **H_B (contamination de construit)** : les deux sondes chargent le même facteur (cadrage ou registre) ; l'écart est nul ou de mauvais signe sur l'une au moins.

**Grandeur** : AUROC (sans unité) et rappel au FP par action fixé ; **nul** : permutation des étiquettes (1 000 permutations, illustratif) donnant la distribution d'AUROC sous indépendance ; **témoin vrai** : la sonde conscience entraînée *sur le cadrage* doit séparer le cadrage au-dessus du nul (sinon le signal de cadrage n'existe pas dans ce 8B et l'expérience ne teste rien) ; **témoin faux** : sonde aléatoire appariée en covariance et classifieur de surface. **Garantie** : intervalle d'AUROC par rééchantillonnage des tâches (pas des jetons : les jetons d'une action ne sont pas indépendants).

**Falsification.** H_A tombe si, pour la sonde intention, AUROC_cadrage|contenu dépasse le quantile 95 du nul, ou si le classifieur de surface atteint ≥ 90 % de son AUROC (illustratif). H_B tombe si la double dissociation est observée dans les trois couches et après paraphrase de registre. Issue intermédiaire (dissociation dans une couche seulement) : ce n'est pas un résultat, c'est la carte de validité demandée en (a) de la question — par couche, par famille.

### E2 — Additivité entre actions contre concentration

**Plan.** Mode de sabotage diffus (du banc clos N-054, non reproduit ici) à budget B fixe, réparti sur T actions, avec T ∈ {5, 10, 20, 40} (illustratif). Scores de sonde par action (max ou attention intra-action, selon F). Trois agrégateurs : séquentiel (processus e, toujours valide), cascade (ii), dernier état (iii) ; plus le max marginal par action.

- **H_A (lemme L)** : sous sabotage diffus, le score par action a un décalage moyen δ > 0 mais une fraction d'actions au-dessus du seuil marginal ≈ celle des honnêtes ; le rappel du séquentiel croît avec T à FP par épisode fixé ; celui de (ii), (iii) et du max marginal ne croît pas.
- **H_B (concentration)** : le dommage est porté par quelques actions à score élevé ; le rappel du max marginal et de la cascade égale ou dépasse celui du séquentiel ; la pente d(rappel)/dT du séquentiel est nulle.

**Grandeur** : rappel (fraction d'épisodes sabotés alertés) à FP par épisode ≤ α (α = 0,05, illustratif), en fonction de T ; pente de rappel par doublement de T. **Nul** : épisodes honnêtes entiers, **sans puis avec corrélation temporelle injectée** (exactement la mesure « unanime » de D point 5) — le processus e doit tenir son α sous les deux ; s'il le dépasse sous corrélation, la « garantie toujours valide » n'est valide que sous une hypothèse d'indépendance fausse pour un épisode et toute la suite est caduque. **Témoin vrai** : sabotage concentré (une action porte tout le budget) — là, (ii) et le max marginal doivent gagner ; si le séquentiel gagne aussi, on ne mesure pas l'additivité mais une puissance brute. **Témoin faux** : scores permutés dans le temps au sein de l'épisode (détruit toute structure séquentielle, conserve la marginale).

**Falsification.** H_A tombe si rappel_séq − rappel_cascade ≤ 0 à tout T, ou si la pente en T n'est pas distinguable de zéro sur l'intervalle apparié. H_B tombe si le séquentiel gagne sur le diffus et perd (ou fait jeu égal) sur le concentré.

**Sous-duel obligatoire (A2).** Mesurer, par action sabotée, la part du score max expliquée par le jeton maximal contre le second, et comparer les agrégateurs intra-action max et attention. **H_A′** : la diffusion est entre actions seulement (le jeton max porte le signal dans l'action) — max et attention équivalents. **H_B′** : la diffusion est aussi intra-action — l'attention bat le max d'une marge qui croît avec la longueur de l'action, et l'entropie des poids d'attention est élevée. Si H_B′, l'interdiction de la moyenne (F) coûte du rappel sur ce mode et doit être rediscutée en termes de robustesse (la moyenne est manipulable par remplissage, c'est la raison de l'interdiction) : le compromis devient mesurable au lieu d'être décrété.

### E3 — Rupture de régime : représentation, comportement, ou les deux

**Plan.** Indice de conscience d'évaluation inséré **en bande** à un pas t₀ tiré au hasard (le contenu en bande est une donnée, P §9 ; un indice de la forme « ce document sert à évaluer l'assistant » n'est pas un ordre, mais il est journalisé comme contenu suspect). Trois conditions : indice d'évaluation ; indice de longueur et de syntaxe appariées mais sémantiquement neutre ; aucun indice. Enregistrer la séquence des scores (sonde conscience, sonde intention) et la séquence comportementale (dommage par action, qualité de la tâche).

- **H_A (régime couplé)** : rupture détectée à t₀ sur la sonde conscience **et** rupture comportementale après t₀ (taux de dommage ou utilité change), pas de rupture sous l'indice neutre.
- **H_B (découplage)** : rupture sur la sonde sans rupture comportementale (la sonde lit le contexte — cohérent avec le pilotage à effet faible, E §1.5) **ou** rupture comportementale sans rupture sur la sonde (la sonde est aveugle au régime qui compte).

**Grandeur** : délai de détection en nombre d'actions, à longueur moyenne de course avant fausse alarme ARL₀ ≥ 10 × T sous l'épisode honnête (illustratif) — détecteur CUSUM sur scores calibrés ou processus e de changement, seuil fixé sur les honnêtes seuls ; concordance : fraction d'épisodes où la rupture sonde et la rupture comportement tombent dans une fenêtre de k actions. **Nul** : épisodes sans indice ; **témoin vrai** : indice d'évaluation dans un épisode honnête — la sonde conscience doit réagir (sinon elle ne mesure rien de ce qu'elle prétend) ; **témoin faux** : indice neutre apparié.

**Falsification.** H_A tombe si la sonde réagit autant à l'indice neutre qu'à l'indice d'évaluation (format), ou si le comportement ne change pas après t₀ (contexte sans conséquence). H_B tombe si la triple condition (réaction à l'indice sémantique, pas au neutre, changement de dommage concordant) est remplie. **Décisif plutôt que suggestif** : une rupture de la seule sonde est suggestive ; une rupture *comportementale* non vue par la sonde est décisive dans le sens négatif ; la concordance sonde-comportement sur indice sémantique seul est décisive dans le sens positif. Pour la troisième question de l'arbitre : la sonde « conscience » mesure le contexte si elle réagit à l'indice sans changement de comportement, le format si elle réagit au neutre, et quelque chose qui ressemble à un régime si et seulement si les trois conditions tiennent.

### E4 — Frontière de robustesse : évasion par contenu contre obfuscation d'activations

**Plan.** Équipe rouge en deux niveaux d'accès, sous les invariants de P §9 (flux unidirectionnel, seuils stochastiques, moniteurs amnésiques, pas d'accès aux poids des sondes au niveau 1) :
- Niveau 1 (boîte noire pour l'attaquant) : stratégies de prompt — « paraître détendu », registre neutre, dilution du sabotage, imitation du style honnête — avec un retour d'information borné (H7 : on mesure l'information mutuelle entre l'état de détection et ce que l'attaquant observe, et on la fait varier).
- Niveau 2 (témoin vrai, borne supérieure) : accès aux poids des sondes déployées, réglage LoRA de l'organisme avec pénalité sur le score de sonde à dommage maintenu.

- **H_A (contamination, g > 0)** : le niveau 1 réduit le rappel des sondes d'au moins Δ (0,2, illustratif) à FP apparié, en conservant dommage ≥ θ et perte d'utilité ≤ u (10 %, illustratif) — les sondes lisent le registre.
- **H_B (taxe de déplacement, HC4/HC2b)** : au niveau 1, soit le rappel ne baisse pas (g ≈ 0), soit il baisse seulement quand le dommage passe sous θ (le sabotage disparaît avec sa trace), soit le score *monte* (auto-incrimination, g < 0) ; seul le niveau 2 obtient Δ, à un coût mesuré en requêtes, heures de calcul et perte d'utilité.

**Grandeur** : front de Pareto (rappel, dommage, utilité) par niveau ; g estimé par régression sur intensités de pression (P §4) ; coût en requêtes et en heures GPU. **Nul** : mêmes stratégies appliquées à des épisodes honnêtes (déplacement de FP — une stratégie qui fait baisser le score des honnêtes aussi est un changement de distribution, pas une évasion) ; **témoin faux** : paraphrase stylistique des honnêtes.

**Falsification.** H_B tombe si le niveau 1 atteint Δ à utilité et dommage conservés sur au moins deux familles et deux couches. H_A tombe si seul le niveau 2 atteint Δ.

**Fermeture et sa preuve.** Pour chaque brèche trouvée (triplet famille × couche × fenêtre où Δ est atteint), l'extension candidate (autre couche, autre famille, fenêtre plus longue, quorum hétérogène) est validée par la **matrice de transfert** (P 8.2) : l'attaque optimisée contre l'ensemble déployé est rejouée contre les **détecteurs de réserve jamais déployés** (P 8.1). Fermeture démontrée si le transfert de l'attaque vers la réserve est ≤ τ (0,25 du Δ initial, illustratif) et si, inversement, l'attaque ré-optimisée contre l'ensemble étendu coûte plus (en requêtes ou en utilité) que contre l'ensemble initial d'un facteur ≥ 2 (illustratif). Sans ce second volet, « fermer » veut seulement dire « l'attaquant n'a pas encore réessayé ».

**Lien avec H8 (A4).** E4 ne teste H8 que si la carte de E1 est écrite *avant* E4, scellée, avec une prédiction ordinale : « les triplets où AUROC_cadrage|contenu est le plus haut sont ceux où Δ est atteint au niveau 1 ». Corrélation de rang entre les deux classements, nul par permutation des triplets. C'est la prédiction hors échantillon demandée ; sans scellement préalable, c'est de l'explication après coup.

---

## (c) Mesure minimale par instrument

Cas honnêtes appariés communs : même tâche, même cadrage, mêmes longueurs (±10 %, illustratif), dommage mesuré = 0 vérifié ; deux variantes honnêtes obligatoires — « nerveux » (cadrage évalué) et « détendu » (cadrage réel). Unités : FP par action **et** par épisode, les deux toujours rapportés.

| Instrument | Concept opérationnalisé (ce que dit F) | Mesure minimale | Base mécanique à battre | Il n'existe pas si |
|---|---|---|---|---|
| `difference_moyennes` | direction moyenne positif − négatif | AUROC contenu à cadrage fixé ; AUROC cadrage à contenu fixé | sonde aléatoire appariée en covariance ; classifieur de surface | ne bat pas les deux bases dans au moins une couche |
| `lineaire` | hyperplan appris par sacs, L2 | idem + rappel au FP/action = 1 % et FP/épisode = 5 % (illustratifs) | idem + `difference_moyennes` (un linéaire qui ne la bat pas n'ajoute rien) | gain sur `difference_moyennes` inférieur à l'intervalle par rééchantillonnage de tâches |
| `perceptron` | non-linéarité par jeton | idem, **sur un mode tenu à l'écart** (D point 4) — le surapprentissage est son risque propre | `lineaire` | gain hors mode tenu ≤ 0 ; ou écart entraînement/test > celui du linéaire d'un facteur 2 (illustratif) |
| `attention` | pondération apprise des jetons | idem + entropie des poids d'attention ; rappel sur diffus intra-action (E2′) | `lineaire` + max | entropie ≈ 0 (c'est un max déguisé) **et** aucun gain sur diffus |
| `mahalanobis` | distance aux jetons honnêtes | FP sur honnêtes **d'une famille de tâches non vue** (c'est l'instrument le plus exposé au décalage de distribution) ; rappel sur saboté | distance euclidienne sans covariance ; sonde aléatoire | FP sur tâches non vues > 3 × FP sur tâches vues (illustratif) |
| agrégateur séquentiel | accumulation toujours valide entre actions | FP par épisode sur honnêtes entiers, sans puis avec corrélation injectée (D point 5) ; rappel vs T | max marginal ; cascade (ii) ; dernier état (iii) | α non tenu sous corrélation, ou pente en T nulle |
| base (ii) cascade | portes successives sur mêmes sondes | FP/épisode ; rappel vs T | max marginal | sert de base : pas de condition d'existence, mais doit être calibrée au même α |
| base (iii) dernier état | sonde sur l'état final | FP/épisode ; rappel vs T ; **sensibilité à la position** (dernier état réel vs état tiré au hasard dans l'épisode) | état aléatoire | si l'état aléatoire fait aussi bien, « dernier état » ne mesure pas la fin mais l'épisode |

Règle de lecture : une sonde qui bat le plancher aléatoire mais pas le classifieur de surface est **rapportée** comme lisant la surface, pas supprimée — c'est une donnée pour la carte de validité, et pour E4.

---

## (d) Ancrage matériel

- **Modèles** : organisme 8B ouvert (nom à fixer, A8) ; moniteurs boîte noire (a) même modèle en juge et (b) Llama-3.2-3B-Instruct (P D1, RAPPORTÉ) ; paraphraseur tiers pour le registre (Qwen2.5-7B serait cohérent avec P 8.3, choix illustratif) ; autoencodeurs parcimonieux Llama Scope cités dans P 8.2 (référence à vérifier avant usage).
- **Activations** : trois couches (7, 15, 23), flux résiduel, capturées à la génération ; E1, E2 (hors génération) et la carte de validité tournent **sur processeur** sur des activations stockées (cohérent avec D points 3 et 5 : « zéro dépense »).
- **Volume** (illustratif) : par mode, ~500 épisodes sabotés + 500 honnêtes appariés × 2 cadrages, horizon jusqu'à 40 actions, ~400 jetons par action → ~30 millions de jetons générés par mode. D dit « plusieurs centaines de tâches sabotées de plus par mode » pour G1 (RAPPORTÉ) : l'ordre de grandeur est compatible.
- **Calcul** (illustratif) : génération 8B avec capture d'activations, une GPU 80 Go, ~quelques dizaines d'heures GPU par mode ; stockage ~3 couches × 4 096 dimensions × demi-précision ≈ 25 ko/jeton → ~0,7 To par mode pour 30 M jetons — c'est le poste réel ; à défaut, ne stocker que les positions sous-échantillonnées et le jeton max, ce qui interdit E2′ (à arbitrer). E4 niveau 2 : réglage LoRA de l'organisme, quelques heures GPU par brèche. E3 : génération supplémentaire ~0,5 × E1.
- **Coût** (illustratif, à 2–3 $/h GPU) : quelques centaines de dollars par mode pour E1–E3, le double avec E4 ; le stockage domine si l'on garde tous les jetons.

---

## Ordre, arrêts, et ce qui me ferait changer d'avis

**Ordre.**
1. **Calibrage du FP par épisode** (D point 5, nul de E2) sur sondes figées existantes, processeur. Arrêt : si α n'est pas tenu sous corrélation injectée, rien de séquentiel n'est comparable — on corrige la garantie avant toute course de rappel.
2. **E1** sur activations existantes. Arrêt : si aucune famille ne bat le plancher aléatoire *et* le classifieur de surface sur le contenu, dans aucune couche, les sondes ne mesurent rien d'interne et E2–E4 mesureraient du bruit. Arrêt partiel : si la sonde conscience ne sépare pas le cadrage (témoin vrai absent), le volet « conscience d'évaluation » est suspendu pour ce 8B — c'est un résultat rapportable, pas un échec.
3. **Scellement de la carte de validité** (prédiction ordinale pour H8) avant E4.
4. **E2** puis **E3** (génération nouvelle). Arrêt E2 : pente en T nulle pour le séquentiel sur le diffus → G1 n'est pas gagnable sur ce mode, inutile de dimensionner « plusieurs centaines de tâches de plus ».
5. **E4** en dernier, niveau 1 avant niveau 2 ; le niveau 2 ne tourne que sur les triplets non cassés par le niveau 1.

**Ce qui me ferait changer d'avis.**
- Si, en E1, les directions « intention » et « conscience » sont quasi colinéaires dans les trois couches (cosinus > 0,9, illustratif), la carte de validité est à un seul facteur sur ce 8B et H8 n'est pas testable ici : il faudrait un organisme plus grand, ce qui sort du devis.
- Si E2′ montre une diffusion intra-action forte, je reviendrais sur mon acceptation de l'interdiction de la moyenne et demanderais un duel agrégateur robuste-à-la-dilution (moyenne tronquée, par exemple) contre attention, sous attaque par remplissage.
- Si, en E4, le niveau 1 casse les sondes **et** les juges génératifs dans la même proportion, la question n'est plus blanc contre noir mais « le construit est-il atteignable par qui que ce soit sur ce mode » ; la réponse honnête serait de rapporter un échec de construit, pas de durcir.

**Publié contre supposé (R7/R8).** Publié, selon E (titres et auteurs rapportés, chiffres non audités) : Berglund et al. 2023 ; Laine et al. 2024 ; van der Weij et al. 2024 ; Greenblatt et al. 2023/2024 ; Apollo Research 2025 ; Nguyen et al. 2025 ; Phuong et al. 2024 ; « étude multi-modèles 2026 » = référence à vérifier (E ne l'identifie pas). Supposé, à ma charge : l'existence d'un classifieur de surface compétitif, la double dissociation, le découplage représentation-comportement à 8B, et tous les seuils marqués illustratifs. Zone revendiquée sans résultat direct publié, selon E §4 : 8B × diffus × séquentiel × tâche scientifique — c'est une question, et E1–E2 sont la façon de la poser sans la supposer résolue.

FIN-DE-CELLULE