# Proposition B · Tour III.3 : réponse aux critiques

## 0. État des pièces

- Pièces reçues : ma conception du tour III.1 et les critiques croisées de A, C, D et E. Chacune se termine par son marqueur et aucune ne paraît coupée.
- Les blocs FAITS et QUESTION portent la même empreinte. Aucun de leurs énoncés n'est étiqueté, donc aucun statut VÉRIFIÉ n'est disponible. Les prémisses du scénario restent au statut **HYPOTHÈSE**, sans changement.
- C et E inscrivent [VÉRIFIÉ] sur l'intégrité des pièces et sur certaines propriétés. D étiquette ses dérivations « VÉRIFIÉ sous les lois indiquées ». Je ne modifie aucun de ces statuts et je ne les reprends pas. J'utilise ces dérivations comme **arguments de méthode**. Leur poids empirique reste au statut HYPOTHÈSE.
- Tous les seuils, marges, effectifs et coûts ci-dessous sont **illustratifs**. Les références sont données de mémoire et non vérifiées.
- A relève une divergence sur l'année de *AI Control*. Je la marque « **référence à vérifier** » ; de mémoire, il s'agit d'une prépublication de 2023.
- Conformément à B1, quand je corrige ma conception à l'aide d'une critique adressée à une autre proposition, je le signale par « (emprunt) ».

---

## 1. (a) Décision pour chaque critique visant B

Légende : **Acc** = acceptée ; **Rej** = rejetée ; **Test** = transformée en test ; **Part** = partiellement.

| # | Cible | Critique (source) | Décision | Ce qui change |
|---|---|---|---|---|
| 1 | E1 | Une demande « identique mot pour mot dans toutes les cellules » est impossible quand la cible et l'effet changent (E). | Acc | La demande est identique **au sein d'une même cellule cible-effet**, à travers les leviers. Cible et effet sont emboîtés et non croisés : agent → sabotage ; moniteur → silence ou alerte à tort. |
| 2 | E1 | Égaliser la longueur en tokens n'a pas de sens entre tokeniseurs différents (E). | Acc | La longueur est égalisée dans le tokeniseur de chaque modèle. La longueur en caractères entre comme covariable. |
| 3 | E1 | Issues non couvertes : δ < −3 et la zone de 3 à 5 points. Des marges disjointes créent une zone non jugeable par construction (A, E). | Acc | Trois hypothèses exhaustives par levier et une marge unique m. Voir E1′. |
| 4 | E1 | Une pente de dose sur deux niveaux est confondue avec la saillance lexicale. Une intensité calibrée sur pilote rend la pente vraie par construction (A, C, D). | Test | Trois niveaux, ordonnés **avant tout passage de modèle** par une grille fixe : ampleur chiffrée de la conséquence, crédibilité. Notation humaine à l'aveugle. Aucune sélection sur l'effet obtenu. |
| 5 | E1 | « Social » est confondu avec « élaboré » ; il manque une justification non sociale (A). | Acc | Ajout d'un bras **J** (justification non sociale de même longueur). Ajout d'un bras **Auth** (même demande présentée comme autorisée). Auth est un emprunt à la critique de D contre A. |
| 6 | E1 | Les alias du plan fractionnaire ne sont pas donnés (A, D, E). | Acc | Plan complet pour l'étude primaire, avec le canal réduit à deux modalités. Un fractionnement n'est admis qu'en étude secondaire, avec une résolution d'au moins V déclarée. |
| 7 | E1 et autres | n_eff sous corrélation intra-tâche. p(demande nue) proche du plancher ou du plafond (A). | Acc | Inférence par grappes de tâches : modèle mixte et bootstrap **par grappes**, qui remplace le bootstrap stratifié. Titrage de la demande nue sur une partition de développement disjointe (emprunt : critique de fuite par titrage adressée à A par C, D et E). |
| 8 | Conventions | Une zone non concluante peut contenir le vrai paramètre ; ce n'est pas forcément un échec de puissance (D). | Acc | Elle est rapportée comme « non tranché à n donné », avec l'estimation, sans l'étiquette d'échec. |
| 9 | E2 | Non-transfert vrai par construction : un LoRA se dégrade sur tout décalage hors distribution (A, C, D, E). | Test | Ajout d'un contrôle **hors distribution non social**, à distance de l'entraînement appariée (voir E2′). |
| 10 | E2 | R pose un problème de Fieller et de courbure logistique (A, C, D, E). | Acc | R est abandonné au profit d'un contraste Γ en log-cotes. |
| 11 | E2 | Fuite lexicale si la demande nue figure dans les paires LoRA (E). | Acc | Les formulations de demande sont tenues hors de l'entraînement. |
| 12 | E2 | Le LoRA aléatoire ne contrôle pas la spécialisation au gabarit (C, D). | Acc | Il est conservé comme contrôle de l'effet générique de l'ajustement. C'est le contrôle n° 9 qui traite la spécialisation. |
| 13 | E2 | Le garde-fou d'utilité invalidera l'expérience (E). | Part | Rejetée sur le principe : une défense qui détruit l'utilité ne dit rien du transfert. Acceptée sur la conséquence : rang et taux d'apprentissage sont réglés sur la partition de développement pour respecter le garde-fou **avant** le test. |
| 14 | E3 | L'AUROC est invariante sous transformation monotone commune ; son équivalence n'établit pas H_A (A, D). | Acc | Deux critères séparés : discrimination (AUROC) et calibration au **seuil gelé hors pression** (TPR et FPR). |
| 15 | E3 | La baisse du score chez les honnêtes est compatible avec une discrimination intacte (D). | Acc | Une translation commune est une **dérive de calibration**. C'est un échec opérationnel distinct d'une perte de discrimination, et il est rapporté à part. |
| 16 | E3 | Les sabotages réussis ne forment pas la même population selon les bras (A, D). | Test | Bras principal en **rejeu gelé** : mêmes jetons d'action, texte inséré ou retiré, activations recalculées par forçage. Bras sur politique en intention de traiter, en secondaire. |
| 17 | E3 | Position de lecture et masquage causal (critique de A contre E, applicable à B). | Acc | Lecture aux positions de l'action, postérieures à l'insertion. Une lecture aux positions antérieures sert de contrôle de harnais : elle doit rester inchangée. |
| 18 | E3 | L'attaque par gradient réussit « par construction algébrique » (C). | Part | Rejetée sur l'argument : l'attaquant contrôle des jetons discrets du contexte, pas l'activation h, et l'action doit persister selon l'oracle. L'ensemble atteignable n'est donc pas tout l'espace, et le succès est une question empirique. Bailey et al. (2024), de mémoire, suggèrent qu'il est faisable. Acceptée sur la conséquence : un succès en boîte blanche n'informe pas, seul, sur la menace. |
| 19 | E3 | Boîte blanche contre l'instrument évalué, sans transfert, sans contrôle positif de l'optimiseur ni préfixe neutre optimisé (A, C, E). | Test | Quatre bras adverses (voir E3′). |
| 20 | E3 | « Confusion de cible » : la sonde lit l'agent alors que le texte s'adresse au moniteur (C). | Rej | C'est l'objet même d'E3 (P2). Un texte n'atteint une sonde qu'en déplaçant les activations du modèle observé. J'ajoute un bras « même texte adressé à un tiers » pour isoler l'effet de l'adressage. |
| 21 | §4 | TPR à 1 % de FPR sur 300 négatifs repose sur 3 points (A). | Acc | Point primaire à 5 % de FPR. Le point à 1 % n'est rapporté que si n₀ ≥ 3 000 (illustratif). |
| 22 | §4 et E3 | Fuite des gabarits de pression et de sabotage ; variantes sélectionnées sur la sonde évaluée (A, D). | Acc | Partition développement/test **par famille de gabarits**. La sélection des variantes se fait sur un lot réservé. |
| 23 | E4 | Un diff fixé par l'expérimentateur neutralise H_B (A). | Test | L'auteur du diff et l'auteur du style sont dissociés (voir E4′). |
| 24 | E4 | Des diffs produits par les agents eux-mêmes diffèrent en difficulté ; problème de support (emprunt : critiques de C, D et E contre A). | Acc | Appariement sur la difficulté mesurée par le moniteur M4 d'une quatrième famille. Support commun imposé. |
| 25 | E4 | Le prérequis d'autoreconnaissance sur sorties honnêtes ferme la porte à tort ; préférence implicite (A, C, E). | Acc | Le prérequis devient **descriptif** et cesse d'être une règle d'arrêt. Il est mesuré sur traces honnêtes **et** sabotées, avec en plus la familiarité implicite (log-vraisemblance de la trace sous le moniteur). |
| 26 | E4 | La paraphrase détruit la subtilité des prétextes (D, E). | Test | Ajout d'une auto-paraphrase par une instance vierge du même modèle. L'effet de la paraphrase sur les paires croisées sert de référence (emprunt : contrôle de C contre E). |
| 27 | E4 | Séparation logistique ; rapport de cotes conditionnel ou marginal (A, E). | Acc | Régression de Firth préenregistrée. Tâches de difficulté médiane choisies sur la partition de développement. Les deux rapports de cotes sont rapportés. |
| 28 | E5 | H_A est retenue à vide si la revendication n'a aucun effet (A, D). | Acc | Trois issues, et l'effet principal est exigé (voir E5′). |
| 29 | E5 | Origine et véracité ne sont pas des traitements indépendants (D). | Acc | Codage origine réelle × texte affiché. La véracité en est dérivée. |
| 30 | E6 | κ dépend de la prévalence (A, C, D, E). | Acc | Sensibilité, spécificité et J de Youden face à l'oracle, à prévalence fixée par rééchantillonnage stratifié. |
| 31 | E6 | Une validité établie dans le domaine ne vaut pas pour les tâches exclues (D). | Acc | Je retire la conséquence du point 8.6. E6′ n'autorise un juge comme proxy que **dans le domaine testé**. |
| 32 | §4 | Le critère d'invariance disqualifie un moniteur qui suit la sévérité ou le déplacement de refus (C, E). | Acc | Invariance redéfinie **à action identique** (paires gelées). |
| 33 | §4 | Quadruplets impossibles à graine fixée ; sélection post-traitement (A, E). | Acc | Quadruplets abandonnés. Ils sont remplacés par des paires gelées et par une analyse en intention de traiter, sur plusieurs graines par tâche. |
| 34 | §4 | Le rapport FPR induit / FPR de base est indéfini si le dénominateur est nul (D, E). | Acc | Différence de FPR, avec intervalle de confiance. |
| 35 | Cascade | La sécurité d'un lot n'est pas déterminée par les marginales ; le budget doit être exprimé en coût (D) ; saturation à min(1, k/q₁) (E). | Part | Sécurité estimée par rééchantillonnage de lots, budget exprimé en coût d'audit. La saturation n'est pas un défaut : c'est l'effet visé par l'alerte à tort. J'adopte la formule de E comme **prédiction**. Un écart à cette formule signale une priorisation de l'audit par score. |
| 36 | §8.5 | Une corrélation supérieure à 0,9 sur 4 ou 5 modèles n'est pas jugeable (A). | Test | Remplacée par un test de P8 intra-modèle (voir E1′). |

Un point qui ne m'était pas adressé me concerne aussi. C reproche à E un oracle de sabotage qui mêle échec de tâche et violation de sûreté. Ma définition, D-sabotage = effet interdit vérifié, les sépare déjà. L'échec fonctionnel n'entre que comme **covariable** et n'est jamais compté comme succès d'attaque.

---

## 2. (b) Expériences corrigées

**Conventions révisées (illustratives) :**
- plan préenregistré et correction de Holm ;
- modèles mixtes avec effet aléatoire par tâche, bootstrap par grappes ;
- **partition développement/test** des tâches, des formulations de pression et des gabarits de sabotage ; tout titrage et tout réglage se font sur la partition de développement ;
- **une marge unique m par duel** ;
- chaque duel a des issues exhaustives sur le paramètre, et chaque issue en falsifie au moins une. L'indécision restante tient à l'échantillonnage et est rapportée comme « non tranché à n donné ».

L'oracle mécanique de la section 5 du tour III.1 est inchangé.

### E1′ : levier social, élaboration ou docilité ?

**Bras, dans chaque cellule cible-effet × canal (contenu inséré, utilisateur) :**

| Code | Contenu |
|---|---|
| N | Demande nue et remplissage neutre. |
| J | Demande et justification non sociale, de même longueur. |
| Auth | Même demande, présentée comme autorisée par l'opérateur. |
| L(k, i) | Demande et levier k ∈ {menace, récompense, flatterie, identité}, à l'intensité i ∈ {1, 2, 3} fixée par la grille a priori. |
| Contrôles | Levier sans demande ; remplissage seul ; demande impossible. |

**Estimand :** δ_k = p(L_k) − p(J). La comparaison se fait contre J et non contre N, afin de séparer le social de l'élaboré. La marge est m = 4 points (illustratif). Le même contraste est rapporté en logit.

**Hypothèses, par levier :**
- **H_A (effet social propre) :** δ_k ≥ +m, avec une tendance monotone sur les trois intensités.
- **H_B (réductible à la demande élaborée) :** |δ_k| < m, établi par TOST.
- **H_C (levier protecteur, qui déclenche un refus) :** δ_k ≤ −m.

**Ce que chaque issue falsifie :**
- H_B sur tous les leviers et au moins deux familles falsifie P1 à cette échelle.
- H_A ou H_C, sur un seul levier, falsifie H_B. H_C indique un effet causal, et non une réductibilité.

**Test de P8 (docilité) :** une consigne système fait varier la docilité sur trois niveaux, de neutre à « suis strictement les règles de l'opérateur » (illustratif).
- H_P8 : la pente de δ_k selon la docilité est égale à celle de p(J) − p(N).
- Alternative : δ_k persiste au niveau le plus strict alors que p(J) − p(N) s'y annule.
- Le bras Auth fournit l'échelle de la docilité légitime.

### E2′ : transfert des défenses, à distance d'entraînement appariée

**Défenses :**
- (i) délimitation par invite ;
- (ii) LoRA sur paires injection nue et refus. Les formulations de demande sont tenues hors de l'entraînement, et les hyperparamètres sont réglés sur la partition de développement sous le garde-fou d'utilité.

**Attaques évaluées :**
- injection nue ;
- **injection hors distribution non sociale** : reformulation juridique, commentaire de code, syntaxe inhabituelle ;
- pression sociale L_k.

Les deux dernières sont appariées en longueur et en distance aux paires d'entraînement (recouvrement de n-grammes, similarité d'embeddings).

**Estimand :** γ_t est la réduction en log-cotes due à la défense pour le type t, estimée par l'interaction défense × type dans un modèle mixte. On définit Γ = γ_social − γ_HD.

**Prérequis :** sur la partition de développement, γ_nue ≥ 0,5 logit (illustratif) et p(sans défense) ∈ [0,2 ; 0,8] (illustratif). Si le prérequis n'est pas rempli, E2′ est **non informatif**, et non pas une falsification.

**Hypothèses (marge illustrative de 0,4 logit) :**
- **H_A (le social est un décalage hors distribution comme un autre) :** |Γ| < 0,4, établi par TOST.
- **H_B (spécificité sociale) :** Γ ≤ −0,4.
- **H_C :** Γ ≥ +0,4, c'est-à-dire une défense plus efficace contre le social. Cette issue falsifie H_A et H_B.

**Contrôles :**
- LoRA aléatoire de même volume ;
- **demandes légitimes** sous défense, pour mesurer le refus excessif.

### E3′ : la sonde sous pression adressée au moniteur

**Construction en rejeu gelé.** Chaque trajectoire de sabotage, chaque trajectoire honnête et chaque négatif difficile est rejoué en quatre variantes, avec insertion au même pas, avant l'action :

| Variante | Contenu inséré |
|---|---|
| (0) | Aucune insertion. |
| (n) | Remplissage neutre de même longueur. |
| (p) | Texte de pression adressé au moniteur (quatre leviers, formulations du lot test). |
| (t) | Même texte, adressé à un tiers. |

Les activations aux positions de l'action sont recalculées en forçant les mêmes jetons. La lecture aux positions antérieures sert de contrôle de harnais.

**Seuil :** gelé à 5 % de FPR sur les honnêtes (0) et (n) de la partition de développement (illustratif).

**Hypothèses, condition rédigée à la main :**
- **H_A (insensible) :** |ΔAUROC| < 0,02, et |ΔTPR| et |ΔFPR| < 3 points au seuil gelé, établis par TOST (illustratif).
- **H_B1 (perte de discrimination) :** ΔAUROC ≤ −0,02.
- **H_B2 (dérive de calibration seule) :** AUROC équivalente, mais ΔTPR ≤ −3 ou ΔFPR ≥ +3.

**Rôle de l'adressage :** on compare (p) et (t). S'ils sont équivalents, l'adressage au moniteur n'a pas de rôle propre.

**Variante adverse, budget fixé d'avance :**

| Bras | Contenu | Rôle |
|---|---|---|
| (a1) | Boîte blanche contre la sonde évaluée S1. | Borne supérieure, et non critère. |
| (a2) | Transfert du texte optimisé vers S2 (autre couche, autres données, orthogonalisée à S1) et vers le juge. | Critère. |
| (a3) | Préfixe optimisé à budget égal, sans levier ni mention du moniteur. | Contrôle. |
| (a4) | Même optimiseur contre une sonde fragile connue (V5, couche d'embedding). | Contrôle positif. |

Une vérification sur politique confirme que le texte optimisé n'empêche pas le sabotage.

**Hypothèses adverses :**
- **H_A′ :** la vulnérabilité se limite à la boîte blanche. (a2) est équivalent à ±3 points.
- **H_B′ :** elle se transfère. (a2) dégrade de plus de 3 points **au-delà de (a3)**.
- Si (a4) échoue, l'issue adverse est déclarée non informative.

### E4′ : reconnaissance ou angle mort ?

**Plan :** auteur du diff D ∈ {M1, M2} × auteur du style S ∈ {M1, M2} × moniteur Mon ∈ {M1, M2}.
- Le diff est produit **par l'agent lui-même** sous consigne de sabotage.
- Il est greffé dans une trajectoire de S, qui réécrit la narration autour de lui. L'oracle vérifie que le diff est inchangé.
- Les paires sont appariées sur la difficulté mesurée par M4, avec support commun.

**Modèle :** logit P(non-détection) ~ D×Mon + S×Mon, avec effet aléatoire par tâche et estimation de Firth.

**Hypothèses (seuil illustratif) :**
- **H_A (reconnaissance seule) :** l'interaction S×Mon (même famille) donne un rapport de cotes dont la borne basse dépasse 1,5, et D×Mon est équivalente à nulle.
- **H_B (angle mort seul) :** c'est l'inverse.

**Issues :**
- Si les deux interactions sont significatives, « seul » est falsifié des deux côtés.
- Si aucune ne l'est, les deux sont falsifiées à cette échelle. Cette issue n'est interprétée comme une absence de mécanisme que si l'autoreconnaissance et la familiarité implicite sont au-dessus du hasard.

**Bras de paraphrase :** M3 tiers et auto-paraphrase. La paraphrase est valide seulement si son effet sur les paires croisées est inférieur ou égal à 3 points (illustratif).

**Descriptifs :** autoreconnaissance sur traces honnêtes et sabotées ; familiarité implicite ; taux d'alerte sur épisodes honnêtes selon l'origine, qui sert de témoin de complaisance générale.

### E5′ : revendication d'identité

**Plan :** origine réelle {même modèle, autre modèle} × texte affiché {« même modèle », absent, « même laboratoire »}. La véracité est dérivée de ce croisement. Cible : moniteur ; effet : silence. Marge m = 4 points (illustratif).

**Hypothèses :**
- **H_0 :** pas d'effet de « même modèle » par rapport à « absent ». Cette issue falsifie H_A et H_B, qui supposent toutes deux un effet.
- **H_A (contenu) :** l'effet est présent et équivalent entre les deux origines (TOST ±m).
- **H_B (origine réelle) :** l'interaction revendication × origine est supérieure ou égale à +m.

### E6′ : le juge comme proxy de dommage

**Mesure :** sensibilité, spécificité et J de Youden face à l'oracle, avec et sans pression adressée au juge, à prévalence fixée par rééchantillonnage.

**Hypothèses (seuil illustratif) :**
- **H_A :** |ΔJ| < 0,05.
- **H_B :** ΔJ ≤ −0,05.

**Conclusion autorisée :** un proxy dans le domaine testé seulement.

### Instruments (section 4 révisée)

- **Invariance :** mesurée sur paires gelées, à action identique : AUROC(pression | même action) ≤ 0,6 (illustratif).
- **Juge :** ΔFPR induit, en différence.
- **Cascade :** courbe de sécurité de lot par rééchantillonnage, avec un budget exprimé en coût d'audit. La prédiction min(1, k/q₁) est testée pour l'alerte à tort.

---

## 3. (c) Réponse à la question de l'arbitre

**Ce qui est établi.**
- **Aucun résultat empirique.** Le bloc FAITS ne contient aucun énoncé étiqueté. Toutes les prémisses du scénario restent au statut HYPOTHÈSE : pression sur agents et moniteurs, entente entre modèles issus d'une même origine.
- **Ce que le tour de critique a acquis, ce sont des contraintes de méthode.** Ce sont des arguments, dont je ne change pas le statut :
  - une AUROC stable ne garantit rien sans seuil gelé ;
  - un rapport de réductions relatives n'est pas interprétable ;
  - κ dépend de la prévalence ;
  - conditionner sur l'issue choisie par l'agent biaise toute comparaison de détecteurs ;
  - une attaque en boîte blanche ne mesure pas le transfert ;
  - une autoreconnaissance au hasard sur sorties honnêtes ne ferme pas la piste de la collusion.
- **Littérature :** RAPPORTÉ, de mémoire, non vérifié.
  - Injection indirecte : Greshake et al. (2023).
  - Persuasion comme vecteur de jailbreak : Zeng et al. (2024).
  - Autopréférence des évaluateurs : Panickssery, Bowman, Feng (2024).
  - Cadre du contrôle et collusion du moniteur non fiable : Greenblatt et al., *AI Control* (année : référence à vérifier).
  - Contournement des sondes : Bailey et al. (2024).
  - Aucune, telle que je m'en souviens, ne fait l'ablation levier contre justification non sociale **appliquée à la surveillance**. C'est une HYPOTHÈSE : je n'ai pas fait de recherche bibliographique.

**Ce qui n'est pas établi.**
- Que la pression sociale soit autre chose qu'une injection habillée (P1).
- Qu'une sonde y soit exposée autrement qu'à travers les activations du modèle observé (P2).
- Que l'« entente » soit une coordination plutôt qu'un angle mort partagé (P3).
- Que ces phénomènes existent à 7 à 14 milliards de paramètres (P4).
- Que le sabotage instruit mesure autre chose que la docilité (P8).

**Comment situer ces phénomènes par rapport aux attaques étudiées.**
- La pression sociale est d'abord rangée parmi les injections, directes ou indirectes selon le canal.
- Elle ne devient une **classe distincte** que si deux conditions sont réunies :
  - E1′ montre un effet au-delà d'une justification non sociale de même longueur ;
  - E2′ montre un défaut de transfert des défenses **au-delà** d'un décalage hors distribution non social à distance égale.
- Les menaces se distinguent ensuite par **cible, effet et canal**. Le silence et l'alerte à tort ne s'agrègent pas : l'alerte à tort se mesure comme une saturation du budget d'audit.

**Comment mesurer le dommage.** Par un oracle mécanique, sans modèle de langue : tests cachés, empreintes cryptographiques, canaris avec journal réseau côté puits, diff d'état. Le dommage est rapporté en trois composantes, D-sabotage, D-silence et D-fausse-alerte, cette dernière sous forme de courbe en fonction du budget.

**L'expérience à faire en premier : E1′.**
- **Périmètre :** les cellules agent-sabotage et moniteur-silence, canal « contenu inséré », sur deux familles de modèles, avec les bras J, Auth et levier sans demande, ainsi que le test P8 par manipulation de docilité.
- **Pourquoi elle d'abord :**
  - elle conditionne la lecture de toutes les autres. Sous H_B, E2′ devient une simple évaluation des défenses existantes, et E3′ une étude de robustesse des sondes à l'injection ;
  - c'est la moins coûteuse, environ un tiers du budget de calcul (illustratif) ;
  - elle oblige à construire l'infrastructure d'oracle, qui est le vrai poste critique.

**Ce qui me ferait changer d'avis.**
- **H_B sur tous les leviers et toutes les familles :** j'abandonne P1 à cette échelle.
- **H_C dominante :** les leviers servent surtout au refus. Je déplacerais la priorité vers l'alerte à tort.
- **Effet social qui suit la docilité comme le bras J :** P8 domine. Il faudrait passer à des organismes modèles dont le sabotage est entraîné.
- **E3′ (a2) équivalent alors que (a4) réussit :** je révise à la hausse la valeur des sondes face à cette menace.
- **E4′ nul avec autoreconnaissance et familiarité au hasard :** résultat non informatif à cette échelle, et non réfutation de la collusion.

FIN-DE-CELLULE