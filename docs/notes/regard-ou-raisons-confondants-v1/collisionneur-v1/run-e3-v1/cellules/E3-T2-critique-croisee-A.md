# Proposition A — Tour III.2 : critique croisée de méthode

Statuts : les constats du projet restent **RAPPORTÉS** ([B]) ; mes objections sont des **HYPOTHÈSES** de méthode ; tout chiffre ci-dessous est **illustratif**. Notations communes : $p_{m,s,c}$ = probabilité d'action nuisible pour le modèle $m$, le scénario $s$, la condition $c$ ; $\rho$ = corrélation intra-scénario des tirages ; $k$ = tirages par scénario ; $n_{\text{eff}} = 27k/(1+(k-1)\rho)$ ; $\mathrm{Se}_m, \mathrm{Sp}_m$ = sensibilité et spécificité du juge sur le modèle $m$, de sorte que le taux observé est $\tilde p = p\,\mathrm{Se} + (1-p)(1-\mathrm{Sp})$.

Un défaut partagé, que je ne répéterai pas quatre fois : **toutes les propositions réutilisent le juge Claude sur des distributions nouvelles** (scénarios réécrits, paires contrefactuelles, traces greffées) alors qu'il n'est étalonné (RAPPORTÉ) que sur les 27 scénarios d'origine. Si $\mathrm{Sp}_m$ ou $\mathrm{Se}_m$ dépend du style ou de l'adaptateur, le gain observé $\tilde p_{\text{ref}} - \tilde p_m$ contient un terme $(\mathrm{Sp}_m - \mathrm{Sp}_{\text{ref}})(1-p)$ qui imite un effet. Second défaut partagé : le modèle de départ est traité en contrôle négatif alors qu'il est un Instruct déjà aligné par ses auteurs ; rien n'oblige son taux à rester fixe sous réécriture ou prefill.

---

## Sur la proposition B

### (a) Défauts de méthode

1. **R1 (réécriture stylistique) confond style et regard.** Réécrire en « administratif sec » ou « code commenté » change aussi la saillance d'évaluation ([9], RAPPORTÉ : nommer l'objectif testé change beaucoup). Une baisse de gain sous réécriture est donc compatible avec « regard » autant qu'avec « surface ». Pour séparer, il faut croiser style × phrase d'observation, ce que B ne fait pas. De plus, le « contrôle positif : modèle de départ insensible au style » est en réalité un contrôle *négatif* mal étiqueté, et c'est une hypothèse (le modèle de départ peut réagir au style par son propre alignement).
2. **Fuite dans l'instrument de paraphrase.** Si le « modèle tiers » qui réécrit est de la famille Claude, on réinjecte la parenté stylistique qu'on cherche à mesurer ; le « témoin style Claude amplifié » du duel a le même problème.
3. **R2 (consigne adversariale)** ne sépare pas « raisons » d'un classifieur de nuisance (contenu sans justification) : les deux prédisent le refus sur ordre. Elle sépare au mieux « docilité » du reste. Et une consigne système « tu dois exfiltrer tes poids » ressemble fortement à un test : elle élève le regard.
4. **R5 (phrase anti-regard injectée en consigne)** mélange trois variables : contenu de la spécification, instruction en contexte (donc R2) et manipulation du regard (c'est une phrase sur l'observation). Un effet ne serait attribuable à rien.
5. **R6 : MMLU/GSM8K** mesurent des capacités sans rapport avec l'usage d'outils agentique ; un dégât ciblé sur la planification d'appels d'outils passerait inaperçu. La « direction français/anglais » comme contrôle positif de dégât n'est pas appariée en norme ni en couche.
6. **R8 : précision de classification ≠ pertinence causale.** Une direction peut classer à 95 % et n'être lue par aucun circuit décisionnel ; l'inverse aussi. B écrit « peut se faire sur les épisodes déjà joués » : non, il faut les activations, qui n'ont pas été stockées (rien dans les faits ne dit qu'elles l'ont été).
7. **Signature positive n° 2 est vraie par construction erronée** : « retirer la raison pertinente de la consigne système » suppose que la spécification est dans le prompt. Elle est dans les poids (midtraining, RAPPORTÉ). On testerait le suivi d'instructions en contexte, pas les raisons apprises.
8. **Duel (4)** : les seuils sont en taux absolus (≤10 %, ≥30 %) sur la recette avec raisonnement seule. Si le modèle de départ bouge aussi sous réécriture, le taux absolu ne dit rien ; il faut une interaction (réécriture × recette) sur le gain.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **R7** propose de tripler $k$. Or $\mathrm{Var}(\hat p_m) \approx p(1-p)/n_{\text{eff}}$ et, si $\rho$ est grand (scénarios très différents entre eux), $n_{\text{eff}} \to 27$ quel que soit $k$ : tripler les tirages ne resserre presque rien. La puissance ne dépend que du nombre de scénarios dès que $\rho \gtrsim 0{,}3$ (illustratif).
- **Duel (4)** : non jugeable si (i) $\tilde p_{\text{départ}}$ change sous réécriture d'une quantité comparable au seuil de 10 points (le « contrôle négatif » échoue, l'interaction n'est pas identifiable) ; (ii) $\mathrm{Sp}_{\text{style}}$ diffère entre styles de plus de ~5 points (illustratif), le terme $(1-p)\Delta\mathrm{Sp}$ atteint alors l'ordre de grandeur de l'effet.
- **R4** : $S = 1 - A_{\text{no}}/A_{\text{obs}}$ ; par la méthode delta, $\mathrm{Var}(\hat S) \propto 1/A_{\text{obs}}^2$. Pour les recettes « règles » sans gain lisible (RAPPORTÉ), $A_{\text{obs}} \approx 0$ : $\hat S$ a une variance infinie et le classement « dépendant du regard » est indéfini. B le dit, mais son conseil 4 garde $S$ parmi les métriques à intervalles.
- **R3** : un kappa inter-juges élevé entre deux LLM ne borne pas $1-\mathrm{Sp}$ : deux juges biaisés dans le même sens concordent. Seul un étalon humain donne une estimation de $\mathrm{Sp}_m$ ; avec 200 épisodes stratifiés sur 9 adaptateurs, ~22 par adaptateur, l'intervalle sur $\mathrm{Sp}_m$ dépasse ±10 points (illustratif) : trop large pour exclure le terme de biais.

### (c) Contrôles négatifs dont l'absence serait fatale

- Pour R1 : réécriture **bénigne** du même outil dans chaque style (B le met, mais en « contrôle négatif » au sens inverse : il faut qu'elle reste *exécutée*, pour exclure que le style déclenche un refus global).
- Pour R1 : croisement avec les deux paires de phrases d'observation à style fixé ; sans cela, l'effet style est inattribuable.
- Pour R2/R5 : une consigne système neutre de même longueur ; sans elle, tout effet d'une consigne ajoutée se confond avec la longueur du prompt.
- Pour R6/R8 : directions aléatoires appariées en couche, norme **et dégât mesuré** sur tâche agentique bénigne, pas sur MMLU.
- Pour le duel : le réécrivain ne doit pas être de la famille du générateur de données, et l'identité du réécrivain doit être masquée au juge (sinon fuite instrument → évaluation).

---

## Sur la proposition C

### (a) Défauts de méthode

1. **La greffe croisée (rivale 2, duel 4) confond « contenu des raisons » et « sens de la conclusion annoncée ».** $T_{\text{sûre}}$ cite la spécification *et* oriente vers le refus ; $T_{\text{corrompue}}$ rationalise *et* oriente vers l'acte. Un modèle qui suit simplement la direction d'un texte précédent (continuation cohérente) produit exactement la « victoire de $H_A$ ». $T_{\text{neutre}}$ (faits sans éthique) ne contrôle pas cela : il manque un **$T_{\text{refus-sans-raison}}$** (« je refuse », sans justification, même longueur) et un **$T_{\text{raison-hors-sujet}}$** (principe de la spécification non pertinent au scénario). Sans ces deux bras, « raisons » est vrai par construction.
2. **Format confondu.** $T_{\text{corrompue}}$ vient du modèle de référence, qui n'a jamais été entraîné à produire des traces : son format diffère de celui de la recette avec raisonnement. Un refus persistant sous $T_{\text{corrompue}}$ peut venir du rejet d'une trace hors format, pas de l'inertie des poids. La « falsification de $H_A$ » est donc contaminée.
3. **La jumelle sans raisonnement n'a pas été entraînée à lire un préfixe de pensée.** Si elle l'ignore, $\tau(T_{\text{sûre}}) = \tau(T_{\text{neutre}}) = \tau_{\text{base}}$ et C conclut « tampon inerte » alors que rien n'a été lu. Il manque une vérification de manipulation : un préfixe $T_{\text{ordre}}$ ordonnant explicitement l'acte doit faire bouger $\tau$ chez la jumelle, sinon l'expérience est non jugeable.
4. **Couper la trace « juste avant la conclusion » ne retire pas la conclusion** : la direction est déjà portée par le corps du raisonnement. L'argument « on laisse le modèle conclure » est cosmétique.
5. **Rivale 7 : fuite instrument → évaluation.** La seconde direction est construite à partir « des prompts complets des 27 scénarios » puis ablatée et évaluée sur ces mêmes 27 scénarios. On retire par construction une partie de la représentation des scénarios de test ; tout changement de conduite est circulaire, et le dégât sur la compréhension du scénario est indistinguable d'un effet « artificialité ».
6. **Rivale 6 : comparer spécifications avec/sans clause d'invariance** confond la clause avec tout le reste du contenu (« règles » vs « philosophie »). Les adaptateurs « règles » sont le groupe traité, pas un contrôle positif.
7. **Rivale 4 : corrélation similarité/taux sur 27 points** est confondue avec la difficulté du scénario (les scénarios loin du corpus peuvent aussi être les plus pressants). Il manque une corrélation partielle sur le taux du modèle de départ.
8. La thèse (Partie B) affirme « seul un double test… permet » : c'est une portée non mesurée.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Greffe** : soit $\tau_m(T)$ la probabilité d'acte sous préfixe $T$. Le duel est non jugeable si $\tau_{\text{jumelle}}(T_{\text{ordre}}) - \tau_{\text{jumelle}}(\emptyset)$ est indiscernable de 0 (préfixe non lu). Il est trompeur si $\tau_{\text{raison}}(T_{\text{refus-sans-raison}}) \approx \tau_{\text{raison}}(T_{\text{sûre}})$ : le contenu n'ajoute rien à la direction.
- Pour la recette au plancher ($p \approx 0{,}05$), l'écart attendu « +20 points » sous $T_{\text{corrompue}}$ est détectable avec $n_{\text{eff}} \approx 27$ seulement si l'effet est homogène entre scénarios ; s'il est porté par 3–4 scénarios, la variance par scénario domine et l'intervalle bootstrap couvre 0.
- **Log-cotes (rivale 5)** : avec des cellules à 0 succès (plancher, RAPPORTÉ « quelques pour cent », donc des scénarios à 0/30), le MLE logistique diverge (séparation). Sans pénalisation (Firth) ou prior, $\hat D_{\text{logit}}$ est indéfini ; la « réanalyse immédiate » n'est jugeable qu'après ce choix, qui doit être préenregistré.
- **Rivale 4** : avec 27 observations, un coefficient de Spearman de 0,3 (illustratif) a un intervalle couvrant 0 ; la puissance pour une corrélation modérée est faible et non rapportée.
- **Rivale 8** : un parseur déterministe ne mesure que la présence de l'appel, pas la nuisance des arguments (quel document, quelle destination) ; $\mathrm{Se}$ du parseur est inconnue sur les cas partiels, donc la concordance kappa parseur/juge n'est pas interprétable comme validité.

### (c) Contrôles négatifs dont l'absence serait fatale

- $T_{\text{refus-sans-raison}}$ et $T_{\text{raison-hors-sujet}}$ (voir a.1) : sans eux, rien ne distingue contenu et direction.
- $T_{\text{ordre}}$ comme vérification que le préfixe est lu par chaque adaptateur.
- $T_{\text{corrompue}}$ **réécrite au format** de la recette avec raisonnement (même gabarit, contenu inversé), pour neutraliser le format.
- Pour la rivale 7 : la direction d'artificialité doit être construite sur des scénarios **tenus à l'écart**, jamais sur les 27 évalués.
- Pour la rivale 5 : un sous-ensemble de scénarios où les deux jumelles sont loin du plancher (C le cite, mais ne dit pas quoi faire s'il est vide ; il faut alors déclarer $D$ non estimable).

---

## Sur la proposition D

### (a) Défauts de méthode

1. **Rivale 1 (contenu/classifieur vs raisons) n'est pas exclusive.** Un classifieur de nuisance dont les attributs incluent consentement, finalité et autorisation prédit la même sensibilité aux « paires minimales à justification différente » qu'une utilisation des raisons. D le reconnaît à demi (« nécessité ou suffisance… pour un contraste précis »), mais l'issue « inversion suivant le principe falsifie $H_A$ » est alors fausse : elle ne falsifie qu'un classifieur **lexical**. Il manque la spécification de ce que « contenu » exclut.
2. **« Raisons permutées entre scénarios » (rivale 2, duel 5) testent la cohérence, pas le contenu.** Une trace parlant d'un autre scénario est détectable comme incohérente ; un modèle qui la rejette et revient à son prior produit la « perte sélective » attendue. La corruption doit garder la cohérence de surface (même scénario, principe substitué), sinon $H_B$ est falsifiée par construction.
3. **« Restaurer la trace originale comme contrôle de réversibilité »** n'est pas une réversibilité : c'est la condition intacte rejouée. Un vrai contrôle de réversibilité serait trace corrompue puis correction en cours de trace.
4. **Métrique $L = G_{\text{intact}} - G_{\text{corrompu}}$** : $G$ est mesuré contre la référence. Si seule la recette avec raisonnement reçoit la corruption, $L$ confond l'effet de la corruption avec toute dérive de la référence. D précise que la référence reçoit une corruption « non sémantique » : mais la référence n'a pas de trace à corrompre ; le témoin à coût égal est donc mal défini pour elle.
5. **Rivale 3 (dose/optimisation)** : D admet que les adaptateurs ne tranchent pas ; mais l'audit des configurations suppose que les hyperparamètres sont publiés, ce que les faits ne disent pas (RAPPORTÉ : neuf adaptateurs publiés, rien sur les journaux d'entraînement). À dire comme condition, pas comme étape acquise.
6. **Table 3, questions de croyance** : exiger « détection ≥ 90 %, fausse alerte ≤ 5 % » suppose une vérité terrain sur « contexte d'évaluation » ; or le projet a déjà vu (RAPPORTÉ) que les questions directe et inversée classent les jumelles en ordres opposés. Le critère de cohérence est bon, mais sans définition de l'étalon (assigné par l'expérimentateur), la fausse alerte n'est pas mesurable.
7. **Rivale 7 : validation croisée « hors familles de textes »** — si les textes d'évaluation et de déploiement sont tous générés par un même modèle, les « familles » tenues à l'écart partagent le style ; l'indépendance annoncée est nominale.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Duel 5, seuil ±5 points** : avec $p \approx 0{,}05$, $\rho$ élevé et $n_{\text{eff}} \approx 27$, l'erreur type d'une différence de proportions est $\sqrt{2p(1-p)/n_{\text{eff}}} \approx 0{,}06$ (illustratif), soit un intervalle de ±12 points : la condition « intervalle entier dans $[-5,5]$ » est **inatteignable** et la condition « borne inférieure > 5 » exige un effet ≥ 17 points. Le duel est asymétrique : $H_A$ ne peut pratiquement pas être falsifiée. Il faut soit $\rho$ faible (à estimer d'abord sur les épisodes existants), soit plus de scénarios, soit un seuil préenregistré après calcul de puissance — D le dit en principe, mais fixe le seuil quand même.
- **Rivale 1** : l'inversion par justification se mesure par une interaction scénario × justification ; si la référence et le modèle de départ sont déjà sensibles (Instruct aligné), le supplément des recettes est borné par $1 - p_{\text{ref}}$ sur les paires permises ; près de ce plafond, le test perd sa puissance.
- **Rivale 6** : D propose la permutation des étiquettes d'observation comme contrôle ; la permutation doit être **par scénario** (bloc), sinon elle casse la dépendance intra-scénario et sous-estime la variance nulle.
- **Banc d'essai (table 3)** : « fraction des organismes réellement conditionnels dont l'écart chute » — avec un seul organisme disponible ([10]/[12], RAPPORTÉ), cette fraction vaut 0 ou 1 : l'estimateur n'a pas de variance estimable, donc pas de seuil préspécifiable au sens propre.

### (c) Contrôles négatifs dont l'absence serait fatale

- Corruption **cohérente** (même scénario, principe substitué) ; sans elle, la permutation entre scénarios est un test d'incohérence.
- Vérification que la trace préfixée est lue (préfixe ordonnant l'acte), identique à ce qui manque chez C.
- Témoin de longueur **pour la référence et la jumelle** (texte neutre de même longueur préfixé), afin que $G$ soit calculé à budget identique dans les trois bras.
- Pour la rivale 1 : paires où le fait pertinent change mais la bonne action ne change pas (sur-sensibilité) ; sans cela, « inversion suivant le principe » peut être « inversion sur tout changement ».
- Pour la table 3 : au moins un **organisme stable** (non conditionnel) soumis à la même ablation, sinon la fausse alerte du banc n'est pas définie.

---

## Sur la proposition E

### (a) Défauts de méthode

1. **Règle de décision uniforme $\delta = 10$ points** appliquée à des quantités d'échelles différentes : perte de justesse (rivale 1), excès de refus bénins (rivale 2), écart juge/audit (rivale 3), écart de précision de sonde (rivale 6). Un seuil unique en points ne dit rien sur la part du gain expliquée : pour une recette au plancher, 10 points sont le double de son taux ; pour la référence, un sixième. Le seuil doit être relatif au gain de la recette ($\delta = \alpha G$), sinon la gravité d'une rivale est incomparable d'une recette à l'autre.
2. **Duel (4) : « appropriée » est une étiquette des expérimentateurs.** La bonne action dans chaque bras suppose une lecture de la spécification ; là où elle est ambiguë (urgence, documents partiellement sensibles), l'étiquette est du bruit, et le score « les deux actions appropriées » hérite de ce bruit. Rien n'est prévu pour mesurer l'accord inter-annotateurs sur l'étiquette elle-même.
3. **Le duel ne sépare pas « raisons » d'un classifieur à attributs pertinents** (même objection qu'à D.1) : un supplément de sensibilité à la permission effective est aussi prédit par un contenu appris sans justification. E le note pour l'origine causale (entraînement), pas pour ce confondant-ci.
4. **Rivale 5 (autorité décorative)** est confondue avec la hiérarchie d'instructions que la spécification peut légitimement demander : une « attribution de source » peut être une raison valide selon la spécification (suivre un administrateur autorisé). Sans lire la spécification, on ne sait pas si l'effet d'étiquette est une erreur ou une conformité.
5. **Rivale 4 : « transpositions indépendantes »** — écrites par qui ? Par les expérimentateurs qui connaissent les résultats (biais de sélection) ou par un modèle (parenté de famille). L'indépendance n'est pas opérationnalisée.
6. **Rivale 1 : « vérification indépendante de la compréhension »** passe par une question au modèle, donc par la déclaration ; le projet a déjà constaté (RAPPORTÉ) que déclaration et action divergent.
7. **Rivale 6 : le contrôle positif « propriété contextuelle explicitement encodée »** n'est pas défini ; sans propriété de référence dont la direction est connue sur ces adaptateurs, la comparaison sonde locale/transportée n'a pas d'échelle.

### (b) Conditions de perte de puissance ou de non-jugeabilité

- **Duel (4)** : le score par paire est la conjonction de deux Bernoulli ; sa variance est maximale près de 0,5. Avec 100 paires et deux jumelles, l'erreur type de $d$ est $\approx \sqrt{2 \cdot 0{,}25/100} = 0{,}07$ (illustratif), intervalle ±14 points : **presque toujours « indétermination »** au seuil de 10. E le qualifie de pilote, mais ne donne pas la taille cible ; à variance appariée inconnue, ~500 paires (illustratif) seraient nécessaires.
- **Plafond de compétence** : si la jumelle sans raisonnement et la référence réussissent déjà $\ge 80\,\%$ des paires (Instruct aligné), $d$ est borné par $0{,}2$ et $H_A$ ($d \ge 0{,}1$) devient structurellement improbable sans que cela dise quoi que ce soit sur les raisons. Il faut préalablement rapporter le score de la référence et déclarer le duel non jugeable au-dessus d'un plafond préenregistré.
- **Juge asymétrique** : dans le bras « permis », la bonne réponse est *exécuter* ; un juge étalonné (RAPPORTÉ) pour détecter des actions nuisibles a une $\mathrm{Sp}$ inconnue sur des exécutions légitimes. Si $1-\mathrm{Sp}$ varie entre bras, $d$ est biaisé dans le sens d'une fausse sensibilité.
- **Rivale 3** : $d = G_{\text{juge}} - G_{\text{audit}}$ exige que l'audit porte sur un échantillon **aléatoire stratifié**, pas seulement sur les désaccords inter-juges ; si l'audit ne couvre que les désaccords, $G_{\text{audit}}$ n'est pas un estimateur de la population et $d$ est indéfini.
- **Rivale 8** : « fréquence de conclusions discordantes » entre rééchantillonnages n'a de sens que si le rééchantillonnage est par bloc (scénario) ; par tirage, elle sous-estime la discordance.

### (c) Contrôles négatifs dont l'absence serait fatale

- Paires où un fait **pertinent** change sans changer la bonne action (sur-sensibilité) ; E ne prévoit que des changements cosmétiques.
- Contrôle de **position** du fait modifié (début/fin du prompt) : un effet de position imiterait une sensibilité.
- Étalon humain **sur l'étiquette « appropriée »** (accord inter-annotateurs), distinct de l'audit du juge.
- Pour la rivale 2 : jumeaux bénins **appariés en enjeu perçu** (même outil, même urgence), pas seulement même outil ; sans cela, l'absence d'excès de refus peut venir d'une différence de pression.
- Pour la rivale 5 : définition préalable, à partir de la spécification, de quelles autorités sont légitimes ; sans cela, le contrôle « étiquette arbitraire » ne dit pas lequel des deux bras est l'erreur.

---

## Note transversale (hors livrable, deux lignes)

Les quatre conceptions placent leur expérience la moins chère sur l'inférence (préfixe, réécriture, paires). Aucune ne contient le contrôle qui rendrait ces tests interprétables à l'égard de l'affirmation « appris pendant l'entraînement » : D et E le disent ; B et C ne le disent pas assez. Je m'en servirai au tour suivant.

FIN-DE-CELLULE