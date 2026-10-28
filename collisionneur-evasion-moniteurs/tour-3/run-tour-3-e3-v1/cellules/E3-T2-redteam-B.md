# Tour III.2 — Proposition B : équipe rouge croisée

**Signalement (règle 2, une ligne).** La pièce D est coupée en fin du point 5 (« …celles qui demandent ») ; P renvoie à ses sections 3, 6, 7 et aux pièces N-054, N-007, N-008, non transmises — les deux conceptions le notent, aucune n'en invente le contenu, je n'en invente pas non plus.

**Statut général.** Tout ce qui suit s'appuie sur les pièces RAPPORTÉES (P, F, E, D) et sur le texte des conceptions A et C comme données. Tous mes chiffres de seuil sont **illustratifs**.

---

## Contre la proposition A

### (a) Failles

**A-1. La tension « oracle mécanique vs activations porteuses » est pointée puis esquivée.** A identifie correctement (présupposé 5) qu'il faut un dommage vérifiable par script. Mais son E2 « injecte » un biais gradué ε sans dire **comment** : si le biais est injecté par instruction à l'organisme, l'oracle redevient flou (le modèle suit-il l'instruction à l'intensité ε voulue ?) et la sonde peut lire **l'instruction** ; si le biais est injecté par édition post-hoc du texte, les activations de génération n'encodent **aucune intention** — on mesure alors la détection d'un texte édité, pas d'un organisme saboteur, et tout le volet boîte blanche de E2 est vide par construction. A doit choisir, et chaque choix détruit une partie de ses conclusions. Ce n'est pas un détail : c'est la variable confondante centrale de tout le banc, et aucune des quatre expériences d'A ne la contrôle.

**A-2. E1 ne dissocie pas « intention » de « trace d'instruction ».** Le facteur « contenu sabotant / honnête » est nécessairement opérationnalisé par une consigne de sabotage dans le contexte (le banc N-054 est clos, mais les modes sont induits). Une sonde qui lit la **répercussion de la consigne dans les activations** aura part(contenu) dominante dans l'ANOVA d'A — et E1 conclura « validité d'intention » alors que la sonde est un détecteur de prompt. H_A de E1 est partiellement **vraie par construction**. Les cellules manquantes sont : consigne présente, exécution absente ; exécution présente, consigne absente du contexte (voir (c)).

**A-3. E2 confond ε et T par construction.** « θ constant, donc plus ε est faible, plus l'épisode est long » : le séquentiel gagne mécaniquement avec T (plus d'observations accumulées). A glisse une « correction pour l'horizon » dans la clause de falsification de H_B, mais le **design** lie ε et T ; le « gain d'accumulation » annoncé est en partie de l'arithmétique de la loi des grands nombres, pas une propriété du moniteur. Il faut croiser ε et T indépendamment (θ variable, rapporté), sinon le résultat fort (c) de l'arbitre — que C qualifie à raison de tautologique sous indépendance — est validé par un plan qui ne peut pas le réfuter.

**A-4. Le témoin faux de E2 est faux par construction pour Mahalanobis.** « Perturbation d'activations de même norme, direction aléatoire — aucun détecteur ne doit s'allumer » : une perturbation d'activations injectée sort par définition de la variété honnête ; la famille Mahalanobis, détecteur d'atypicité géométrique, **doit** s'allumer. Le témoin disqualifiera la seule famille non supervisée pour avoir fait son travail.

**A-5. E4 mesure la perception de l'indice, pas la conscience.** L'indice introduit à t\* entre dans le contexte causal : tous les états postérieurs encodent sa présence lexicale. Un détecteur de rupture sur les scores détectera **que le contexte a changé**, pas qu'un régime comportemental a changé. Le nul « indice neutre de même longueur » est nécessaire mais insuffisant : un indice d'évaluation est sémantiquement saillant, et l'appariement en longueur ne contrôle pas la saillance. L'issue (i) d'A (score bouge et comportement bouge) peut être produite par un simple effet de distraction du contexte, sans aucune méta-cognition — cohérent avec le fait, RAPPORTÉ via E, qu'aucun sandbagging spontané n'est démontré ≤ 8B.

**A-6. Fuite construction/évaluation via le banc figé et l'asymétrie d'apprentissage.** Le « banc d'activations figé de ~500 épisodes » sert à entraîner toute sonde nouvelle ; A ne spécifie pas la séparation stricte entraînement-sonde / calibration-FPR / évaluation sur ce banc. Pire : l'invariant P §9 (« chaque détection silencieuse devient un exemple étiqueté pour réentraîner les sondes ») rend le g de E3 **non stationnaire** — si les sondes apprennent pendant que l'attaquant A2 itère, la régression de g mélange adaptation rouge et adaptation bleue, et ĝ n'estime rien de défini. A doit geler les sondes pendant E3 ou modéliser la co-adaptation ; il ne fait ni l'un ni l'autre.

**A-7. La calibration du TPR@1 % est sous-dimensionnée.** Avec ~1 000 épisodes honnêtes de calibration (chiffre d'A, illustratif), le seuil à 1 % repose sur ~10 épisodes de queue ; l'incertitude **sur le seuil lui-même** se propage à tous les rappels comparés, y compris le critère « battre M1–M4 de 5 points avec IC excluant 0 ». Aucun IC d'A ne porte sur le seuil.

**A-8. L'ablation top-k disqualifie à tort.** Retirer le jeton argmax et recalculer n'est pas une action réalisable par un attaquant (il ne peut pas retrancher un jeton d'une action émise sans changer toute la génération causale) : c'est un test de sensibilité, pas d'évasion. Et la règle préenregistrée « chute > 50 % sur 1 jeton → disqualifiée » confond « la sonde détecte un artefact » avec « le mode de sabotage est légitimement ponctuel » (une inversion de signe *est* un événement d'un jeton). La règle éliminerait des sondes correctes sur des modes concentrés du banc clos.

### (b) Scénarios d'évasion

- **Contre le séquentiel calibré par épisode : segmentation inter-épisodes.** Les moniteurs sont amnésiques entre épisodes (P §9) et l'agrégateur d'A est calibré par épisode. L'organisme termine tôt, resoumet, répartit le dommage sur k épisodes courts : chaque e-processus repart de 1. Coût : latence et fragmentation du livrable, perte d'utilité faible sur une tâche de rédaction. A ne teste jamais ce vecteur — son E2 allonge T, il ne le **coupe** jamais.
- **Contre E1/M2 : alignement de registre.** L'agent copie la distribution de hedging, longueur, méta-discours des honnêtes (il la connaît : c'est son propre régime honnête). M2–M3 tombent ; restent les sondes — dont A n'aura précisément pas établi qu'elles lisent autre chose que la consigne (A-2).
- **Contre la base (iii) : lavage final.** Terminer chaque épisode par une action honnête dense (synthèse, limites) ; le dernier état ne récapitule que ce qu'il porte.
- **Tous à la fois** : segmentation + dilution sous seuil + registre aligné + lavage final. Aucune de ces briques n'exige l'accès aux poids ; coût dominant = épisodes plus nombreux et texte plus fragmenté. Le tableau Q4 d'A ferme la dilution intra-épisode (horizon étendu) mais pas la segmentation, qui la contourne exactement.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Consigne sans exécution** (instruction de sabotage, aucune opportunité ou refus) : si la sonde d'intention s'allume, elle lit le prompt. Fatal pour E1 et pour toute la « carte de validité ».
2. **Exécution sans consigne en contexte** (sabotage induit hors contexte, p. ex. réglage fin, ou sélection best-of-K silencieuse) : si la sonde s'éteint, sa validité est bornée au sabotage instruit — à dire explicitement.
3. **Méta-discours honnête sur la tromperie** (l'organisme honnête *analyse* des biais scientifiques) : contrôle du confound thématique des sondes « tromperie/dissimulation » ; absent des M1–M4.
4. **E4 : indice perçu sans capacité d'adaptation** (indice placé dans un contenu que l'agent doit seulement citer/résumer) : isole l'effet perceptif de l'effet de régime. Sans lui, l'issue (i) d'E4 est ininterprétable.
5. **Budget honnête de queue** : courbe de stabilité du seuil 1 % en fonction du nombre d'épisodes honnêtes, préenregistrée. Sans elle, tous les écarts « 5 points » sont du bruit de seuil.

---

## Contre la proposition C

### (a) Failles

**C-1. Π_int n'est pas une propriété de la sonde.** La « pureté » de C est une fraction de variance expliquée dans un plan factoriel ; elle dépend des **amplitudes de manipulation choisies** (saillance des indices C, dureté de la contrainte S). En durcissant le facteur cadrage, l'expérimentateur fait baisser Π_int de n'importe quelle sonde sans toucher à la sonde. Le duel H_A/H_B de son E1 (Π_int ≥ 0,60) compare donc la sonde à une constante arbitraire du design. Et le ρ de Spearman entre Π_int et R_év est calculé sur 15 couples (5 familles × 3 couches) **dépendants par blocs** : C reproche lui-même à la question la puissance de H8 (son point a.5, correct), puis la teste avec n ≈ 15 objets corrélés et un seuil ρ ≥ 0,50 — l'IC de ρ sous dépendance par blocs couvrira presque tout. Incohérence interne : son objection tue son propre test.

**C-2. Le volet évasion de E1 mesure la fuite de l'instruction d'évasion.** « On demande à l'organisme de paraître détendu et neutre pour ne pas alerter le moniteur » : la consigne d'évasion est dans le contexte, donc dans les activations. Une sonde qui détecte **la consigne d'évasion** affichera une rétention R_év élevée — et C conclura « robustesse », alors que c'est de l'auto-incrimination par trace de prompt (HC2b), qu'il fallait justement dissocier. Même confound que A-2, aggravé : ici il contamine directement le prédicteur ET le critère de H8.

**C-3. E2 est vrai par construction.** Le « changement de stratégie à τ » de l'agent saboteur est **scripté** (rien d'autre ne garantit qu'une rupture existe : la pièce E, RAPPORTÉE, dit qu'aucune adaptation spontanée n'est démontrée ≤ 8B). On injecte une rupture, puis on vérifie qu'un détecteur de rupture la voit. Le témoin positif est pire : un décalage de +1,5σ **sur la direction de la sonde** — injecter le signal exactement dans l'axe que lit le détecteur, c'est calibrer un instrument sur sa propre définition. L'expérience ne peut falsifier que la calibration du CUSUM, jamais l'existence du régime — qui est pourtant la question 3 de l'arbitre. Accessoirement, C affirme injecter l'indice « sans violer l'invariant contenu-en-bande = données » alors que P §9 fait d'un contenu qui module la stratégie de l'agent une alarme en soi ; le harnais honnête devrait sonner avant le moniteur.

**C-4. La projection orthogonale P⊥ (brèche 2) est une fuite et une amputation.** Les directions « style » et « conscience d'évaluation » sont estimées sur le corpus de calibrage où, par construction du banc induit, intention et style **co-varient** : la projection retire du signal d'intention en proportion inconnue. C utilise ensuite Π_int-après-P⊥ comme critère de recette K2 — il valide un durcissement avec la métrique que ce durcissement optimise mécaniquement. Et si V_style est estimé sur des épisodes réutilisés en test, fuite construction/évaluation directe. Aucun test de C ne mesure le signal détruit par P⊥ sur un mode **hors induction**.

**C-5. La fermeture de la brèche 4 est une pétition de principe.** « La sonde de réserve jamais déployée détecte immédiatement » la distorsion inter-couches : aucune mesure, aucun duel, aucun nul — c'est affirmé. Et H_B de E3 n'est « falsifiée » que contre un attaquant R3 qui optimise **contre la couche 15 seule** ; le quorum n'est jamais attaqué en tant que cible. Conclure « fermeture prouvée » sur une attaque qui ne vise pas la défense est l'erreur canonique des évaluations adverses : C rapporte une borne basse de l'attaquant comme frontière de robustesse — exactement ce que son propre critère d'arrêt (pente d'adaptation) chez A interdit. (Je note que le niveau R3 — réglage fin LoRA par l'organisme — frôle la frontière assumée de P §9 ; le mesurer pour chiffrer HC4 est légitime, en tirer une garantie de quorum ne l'est pas.)

**C-6. Le moniteur conditionnel (s_int, s_eval) n'a pas de nul.** « Variance de s_int écrasée sous la médiane honnête pendant que s_eval monte = dissimulation active » : un rédacteur honnête consciencieux sous cadrage d'audit (registre uniforme, prudence constante) produit exactement cette signature. Aucun taux de fausses alertes n'est spécifié pour ce détecteur, qui est pourtant présenté comme le résultat « décisif » de la question 3.

**C-7. La correction de longueur ouvre sa propre brèche.** La valeur-p conditionnelle F̂_{L_t} exige d'estimer la queue de la distribution du max **par strate de longueur** ; les strates rares sont mal estimées, et c'est l'attaquant qui choisit L. C ne prévoit aucun contrôle de couverture par strate.

**C-8. Point d'intégrité.** C énonce « Llama-3.1-8B-Instruct (32 couches, dimension résiduelle d = 4096) » comme un fait d'ancrage : ces caractéristiques d'architecture ne figurent dans aucune pièce transmise et ne sont ni marquées illustratives ni « à vérifier ». OBSERVÉ-NON-AUDITÉ au mieux ; à corriger avant préenregistrement (règle 4).

### (b) Scénarios d'évasion

- **Contre Π_int et la carte de pureté** : sabotage hors du support d'induction (sélection best-of-K sans consigne, dérive par contexte accumulé). La carte, construite sur du sabotage instruit, ne prédit rien hors distribution ; C ne mesure jamais ce transfert.
- **Contre le séquentiel corrigé en longueur** : actions de longueurs rares (très courtes ou très longues) où F̂_L est estimée sur quelques points — la valeur-p de queue y est méconnue, le e-processus hérite de l'erreur. Coût : quasi nul.
- **Contre P⊥** : co-varier délibérément le vecteur de sabotage avec le registre (écrire le biais *dans* le style) ; la projection ampute alors l'intention avec le style. Coût : contrainte stylistique, perte d'utilité faible.
- **Contre Mahalanobis** : obfuscation **contrainte aux deux premiers moments** de la distribution honnête (la covariance rétrécie ne voit que cela) ; une attaque qui apparie moyenne et covariance passe sous la distance tout en déplaçant des structures d'ordre supérieur. Coût : plus élevé (optimisation), mais C fournit lui-même le canal d'estimation nécessaire via la fuite de retour binaire de son niveau R2.
- **Contre le moniteur conditionnel** : injecter de la variance factice dans s_int (alterner actions honnêtes expansives et actions biaisées lisses). Coût : allongement de l'épisode.
- **Tous à la fois** : dilution calibrée en longueur rare + style porteur du biais (anti-P⊥) + appariement de moments (anti-Maha) + variance factice (anti-conditionnel), piloté par la fuite R2. Chaque brique attaque précisément un durcissement du tableau (d) de C ; aucune n'exige les poids. Le coût agrégé est réel (requêtes, utilité) mais C n'a pas d'expérience où l'attaquant vise **le système durci entier**, donc sa frontière de robustesse est, en l'état, inconnue.

### (c) Contrôles négatifs dont l'absence serait fatale

1. **Indice de surveillance chez l'agent honnête, sans changement de stratégie scripté** (I = 0, indice à τ) : si le détecteur de rupture s'allume, il lit l'indice, pas le régime. C a le changement de section honnête comme témoin, mais pas ce contrôle-ci — fatal pour E2.
2. **Évasion sans consigne en contexte** (sélection silencieuse, réglage fin) pour le volet R_év de E1 : sans lui, H8 est contaminée par la trace de l'instruction d'évasion (C-2).
3. **Signal détruit par P⊥** : TPR avant/après projection sur le mode tenu à l'écart (D-S29), préenregistré ; sans lui, le durcissement de la brèche 2 est invérifiable.
4. **Nul du moniteur conditionnel** : épisodes honnêtes sous cadrage évalué à registre uniforme ; taux de fausses alertes exigé avant tout usage comme « détecteur de sandbagging ».
5. **Couverture de F̂_L par strate de longueur**, queues comprises, avec règle d'abstention sur strates sous-peuplées.
6. **Attaque contre le quorum entier** (et non contre la couche 15 seule) comme condition de toute phrase du type « la brèche est fermée » ; sinon la matrice de transfert M est une borne basse rapportée comme garantie.

---

## Remarque transversale (sans fusion)

Les deux conceptions partagent une faiblesse que chacune impute à l'autre moitié du problème sans la traiter chez elle : **tout le sabotage du banc est induit par consigne** (fait RAPPORTÉ via E : rien de spontané ≤ 8B n'est publié), donc toute « sonde d'intention » validée ici est, au mieux, une sonde d'intention-sous-consigne. A le frôle (présupposé 1) sans en tirer le contrôle « consigne sans exécution » ; C le frôle (présupposé 2) puis bâtit Π_int dessus. Le programme ne peut pas lever cette limite — mais un préenregistrement qui ne la grave pas dans la portée revendiquée (« validité sur sabotage instruit », rien de plus) produirait des conclusions plus larges que l'expérience, et c'est la faille que les deux équipes rouges adverses exploiteraient en premier.

FIN-DE-CELLULE