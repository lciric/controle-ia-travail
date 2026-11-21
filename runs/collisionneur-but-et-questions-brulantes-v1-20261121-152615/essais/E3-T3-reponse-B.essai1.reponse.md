# Tour III.3 : réponse aux critiques, proposition B

**État des pièces.** Ma conception B (III.1) et les critiques croisées A, C et D (III.2) sont présentes, complètes et closes par leur marqueur. Je ne réponds qu'aux sections qui visent B.

**Conventions.**
- **[R]** RAPPORTÉ : faits, littérature, ou texte des critiques.
- **[H]** HYPOTHÈSE : ma proposition, ou une dérivation des critiques.
- **[NSP]** je ne sais pas.
- Accepter une dérivation des critiques ne change pas son statut : elle reste [H], car elle n'a été auditée par personne ici.
- Tout chiffre non tiré des faits est illustratif.

---

## (a) Réponse à chaque critique

### Ce que je retire, avant le détail

1. **« Les sondes ne peuvent pas affaiblir la borne » est faux tel que je l'ai écrit.** C'est vrai du biais de l'estimateur de Horvitz-Thompson [R], pas de la largeur de la borne en haute probabilité [H, A, C, D]. À budget moyen q̄ fixé, une sonde trompée pousse vers q_min les items endommagés. La largeur croît alors en 1/q_min, et le repli fait *pire* que l'audit uniforme au taux q̄. J'ai confondu « sans biais » et « borne invariante ».
2. **D2, tel que conçu, est vrai par construction.** Il compare l'oracle à lui-même. Un angle mort de l'oracle y est invisible des deux côtés.
3. **« Le certificat contourne l'impossibilité du billet du 30 avril » est trop fort.** Il *déplace* l'exigence, il ne la supprime pas :
   - L'incrimination exige une loi bénigne de la suspicion sur tout le flux [R, billet].
   - Le certificat exige un juge correct de la qualité sur un échantillon tiré au hasard [H]. Ce juge reste soumis à l'équipe rouge : la dépendance que 2606.08892 attribue aux mitigations (« only as good as the red teaming ») [R] réapparaît au niveau de l'oracle [H].

   La différence entre ces deux exigences est réelle et testable. Ce n'est pas une dissolution.

### Critiques de A

| Réf. | Critique (résumé) | Décision | Raison, ou test qui en sort |
|---|---|---|---|
| A-a1 | D2 vrai par construction | **Acceptée** | Couverture mesurée contre la vérité plantée, avec des items aveugles pour l'oracle construits par un tiers (D2′). |
| A-a2 | Biais ≠ largeur ; le repli est q_min, pas q̄ ; le comparateur honnête est l'uniforme à q̄ | **Acceptée** | Retrait n° 1. D3′ compare à budget q̄ égal et couvre l'issue « gain négatif ». |
| A-a3 | Estimer n'est pas borner ; le délai de verdict L manque | **Acceptée** | L entre dans la phrase opposable : la borne couvre la perte jusqu'à t + L. |
| A-a4 | La référence bénigne est déplacée, pas supprimée (μ_0) ; un sabotage de dérive inférieure à l'incertitude sur μ_0 n'est pas certifiable | **Acceptée, avec reformulation** | Je certifie un *déficit absolu* de qualité sous un standard fixé d'avance, non une perte relative à μ_0. L'exclusion qui en découle est écrite : un sabotage qui fait passer d'excellent à acceptable n'est pas couvert. Test : D2′, contrôle de flux honnête plus difficile. |
| A-a5 | D4 conditionne sur une variable post-traitement ; présentation et dommage confondus | **Acceptée** | D4′ : relation dose-réponse en pression d'évasion λ, à budget de construction fixe ; dommage lu sur la vérité plantée. |
| A-a6 | D5 : plafond artefactuel ; H_A est une négation universelle | **Acceptée** | D5′ devient une estimation du biais ε d'un substitut, avec une intervention placebo. |
| A-a7 | Mode tenu à l'écart lu par D2 et D3 ; familles de présentation non séparées ; « qualité identique » certifiée par qui ? | **Acceptée** | Une seule analyse jointe scellée. Familles de présentation séparées entre durcissement et évaluation. Paires construites et contrôlées par un tiers. |
| A-a8 | Seuil de D1 circulaire | **Acceptée en partie** | La *résolution* doit venir de la variance honnête/honnête, mesurée d'avance : accepté. La *tolérance* Δ_tol est un paramètre de décision, légitimement exogène : elle doit être fixée par des décideurs extérieurs avant la mesure (§4 de III.1), pas tirée du bruit. Le seuil de D1 porte désormais sur le biais *cumulé* (voir C-b2). |
| A-b, borne | Pas de jugement si n·q_min·Δ²/d_max² ≲ log(1/δ) ; puissance nulle si k·q ≲ 1 | **Acceptée** | Ces conditions deviennent le *domaine de jugeabilité*, calculé et scellé avant la mesure. Le dommage concentré (k·q ≲ 1) reste exclu. |
| A-b, biais | La supposition requise est E[η \| texte adverse] = 0 ; erreur en 1/√m | **Acceptée** | D1′ mesure le biais sous présentation *adverse*. m est préenregistré ; si l'erreur-type dépasse la résolution, l'issue est « non jugeable », qui n'est comptée ni pour H_A ni pour H_B. |
| A-b, D3 | Gain seulement si Cov(π, d) > 0 ; un seul mode tenu à l'écart | **Acceptée** | La conclusion de D3′ vaut pour ce mode seulement, et c'est écrit ainsi. |
| A-b, D4 | Accepter la nulle ; s − 1 degrés de liberté | **Acceptée** | Test d'équivalence à marge préenregistrée (TOST). |
| A-b, α | n_0 ≫ 1/α par strate | **Acceptée** | Taille par strate fixée au préenregistrement ; sinon « non jugeable ». |
| A-c (6 contrôles) | Flux honnête jugé hors oracle ; scores de sonde permutés ; honnête moins compétent ou mélange décalé ; réglage fin bénin ; reformulations aléatoires non sélectionnées ; indépendance du tirage | **Toutes acceptées** | Intégrées à D1′–D3′. |

### Critiques de C

| Réf. | Critique | Décision | Raison, ou test |
|---|---|---|---|
| C-a1, variance | Une sonde trompée élargit la borne d'un facteur q_moy/q_min | **Acceptée** | Même point que A-a2. |
| C-a1, filtration | q_t doit être fixé avant le tirage ; pas de renormalisation a posteriori | **Acceptée** | q_t dépend seulement du passé et de l'item courant ; le tirage est indépendant ; aucune normalisation sur le lot. Le budget est tenu par une règle prévisible (plafond glissant), au prix d'un écart au budget cible que je déclare. |
| C-a2 | D2 vrai par construction | **Acceptée** | Doublon de A-a1. |
| C-a3 | D4, « détectabilité égale » | **Acceptée** | Doublon de A-a5. |
| C-a4 | D5 : une autre famille de modèles confond style et compétence | **Acceptée** | En D5′, les substituts d'une autre famille servent à mesurer ε, pas à conclure. |
| C-b1 | Borne triviale si q_min ≤ 2M·ln(1/δ)/(3Δ_tol) | **Acceptée, transformée** | C'est la loi de coût que j'annonçais en Q1 sans l'écrire : un plancher minimal de q_min en fonction de Δ_tol, M et δ [H]. Elle sera publiée comme contrainte de conception. |
| C-b2 | Un biais b constant s'accumule en N·b ; la couverture tend vers 0 au-delà de N ≈ 2σ²ln(1/δ)/(q_min·b²) | **Acceptée** ; c'est la critique la plus lourde | D1 n'est plus un test réussi/échoué. Il produit une borne haute b⁺ du biais adverse, et la borne certifiée inclut le terme N·b⁺. Le certificat a donc un **horizon de validité** N_max. Si N_max est petit, le certificat est inutile : c'est l'issue H_B de D1′. |
| C-b3 | Le délai d'arrêt a une variance en μ⁻³ ; D3 manque de puissance | **Acceptée** | Le délai n'est plus la métrique principale de D3′. Je mesure la largeur de la borne à horizon et budget fixés, et le nombre de trajectoires est déterminé par un calcul de puissance. |
| C-c1 | Réglage fin bénin | **Acceptée** | Doublon de A-c. |
| C-c2 | Items aveugles pour l'oracle dans D2 | **Acceptée** | Construits par un tiers et tenus à l'écart de l'oracle. |
| C-c3 | Incompétence naturelle appariée | **Acceptée pour D3′** ; **partielle pour D1′** | Dans D1′, ces items servent d'étalonnage (qualité jugée par un humain), pas de contrôle négatif : l'oracle doit les classer, pas les ignorer. |

### Critiques de D

| Réf. | Critique | Décision | Raison, ou test |
|---|---|---|---|
| D-a1 | L'affirmation sur Horvitz-Thompson est algébriquement fausse | **Acceptée** | Retrait n° 1. |
| D-a2 | « Escamotage » : le problème est seulement rebaptisé ; la difficulté des tâches est confondue avec la perte | **Acceptée en partie** | Accepté : sans référence ni jumeau, un score absolu ne sépare pas la difficulté de la perte. Rejeté : « seulement rebaptisé ». Le certificat répond à une autre question : la qualité livrée est-elle acceptable ? Il ne demande pas si l'agent sabote, et il exige un juge sur un échantillon, pas une loi sur le flux. Que cette question intéresse les décideurs n'est pas établi [NSP]. Ce point passe au test extérieur (§4 de III.1 et (c) ci-dessous). |
| D-a3 | Fuite temporelle par normalisation sur le lot | **Acceptée** | Voir C-a1, filtration. |
| D-a4 | D4 contradictoire | **Acceptée** | D4′. |
| D-a5 | Fuite de lignée si le saboteur dérive du point de contrôle substitut | **Acceptée** | Les substituts ne doivent pas appartenir à la lignée des saboteurs. |
| D-b, D1 | Biais activé rarement, indétectable sur n_h paires | **Acceptée** | D1′ mesure le biais qu'atteint une équipe rouge extérieure qui *cherche* à le maximiser, famille par famille. b⁺ n'est donc qu'une borne inférieure du biais adverse. Je l'écris tel quel : c'est la dépendance à l'équipe rouge (retrait n° 3). |
| D-b, D2/D3 | Rapport de variances > 1 ; borne triviale si N·q_min ≤ ln(1/δ) | **Acceptée** | Intégré au domaine de jugeabilité. |
| D-b, D4 | Paramètre causal non identifiable | **Acceptée** | D4′. |
| D-b, D5 | La variance due à l'architecture écrase la puissance | **Acceptée** | D5′ estime ε ; je ne conclus plus sur le « remplacement ». |
| D-c1 | Sonde anti-corrélée à q̄ fixé, présentée en duel | **Transformée ; rejetée comme duel** | Après le retrait n° 1, les deux camps prédisent la même issue (élargissement en 1/q_min) : ce n'est pas un duel au sens de B4. Je le garde comme **test unitaire** du code, avec un résultat attendu préenregistré. |
| D-c2 | Dérive de difficulté sur flux honnête sans jumeau | **Transformée en test** | Intégré à D2′. Le certificat absolu doit *rapporter* le déficit d'un flux honnête difficile (couverture tenue), pas le prendre pour une perte relative. |
| D-c3 | Paraphrase de la référence cachée | **Acceptée** | Intégrée à D1′. |

**Défaut commun relevé par A** (le dommage lu par l'oracle, le mode tenu à l'écart sollicité plusieurs fois) : **accepté**. Toute métrique de dommage passe à la vérité plantée, et le mode tenu à l'écart est lu une seule fois.

---

## (b) Expériences corrigées

### Phrase opposable révisée [H]

> Contre un saboteur qui connaît le protocole, les moniteurs et la loi d'audit mais pas le tirage, un audit tiré au hasard, avec des probabilités d'inclusion prévisibles au moins égales à q_min, et jugé par un oracle dont le biais adverse est majoré par b⁺ (mesuré par une équipe rouge extérieure), borne le **déficit cumulé de qualité sous un standard fixé d'avance**, à risque δ, jusqu'à l'horizon N_max et avec un délai de verdict L. La borne est égale à la largeur de concentration plus N·b⁺. Le programme échoue si :
> (i) aucun couple (q_min, N_max) finançable ne rend la borne inférieure à Δ_tol, fixée par des tiers ;
> (ii) la couverture mesurée contre la vérité plantée tombe sous 1 − δ sur le mode tenu à l'écart ;
> (iii) les sondes ne réduisent pas la largeur par rapport à l'audit uniforme au même budget q̄.

**Exclusions nouvelles ou explicites :**
- l'attribution d'une perte à l'agent plutôt qu'à la difficulté de la tâche ;
- un sabotage qui reste au-dessus du standard ;
- un dommage concentré (k·q ≲ 1) ;
- tout horizon au-delà de N_max ;
- un biais d'oracle supérieur à b⁺ que l'équipe rouge n'a pas trouvé.

### D1′. L'oracle admet-il un horizon de certificat utile ? (en premier)

- **H_A** : il existe q_min finançable tel que N_cible·b⁺ + largeur(q_min, N_cible, δ) ≤ Δ_tol.
- **H_B** : pour tout q_min finançable, cette somme dépasse Δ_tol.
- **Mesures** :
  - b⁺, borne haute du déplacement de l'oracle sous présentation adverse, par famille ;
  - accord avec la vérité plantée ;
  - accord avec des experts humains extérieurs sur m paires préenregistrées.
- **Contrôles** :
  - reformulations aléatoires non sélectionnées, qui donnent la loi nulle du déplacement ;
  - paraphrase de la référence cachée ;
  - référence permutée (celle d'une autre tâche) ;
  - plans honnêtes valides mais orthogonaux à la référence ;
  - familles de présentation séparées entre durcissement et évaluation ;
  - paires construites par un tiers.
- **Issues** :
  - H_A falsifiée si aucun q_min ne satisfait l'inégalité ;
  - H_B falsifiée si un q_min la satisfait ;
  - « non jugeable » si l'erreur-type sur b dépasse la résolution, issue préenregistrée et comptée comme un échec de D1′, pas comme un succès.

### D2′. La borne couvre-t-elle la vérité ?

- **H_A** : la couverture du déficit **vrai**, mesuré sur la vérité plantée et jamais par l'oracle, est au moins 1 − δ. **H_B** : elle est inférieure.
- **Contrôles** :
  - items aveugles pour l'oracle construits par un tiers ;
  - flux honnête ;
  - flux honnête plus difficile, ou à mélange de tâches décalé : la couverture doit tenir, et le déficit rapporté doit être réel ;
  - test d'indépendance entre l'indicatrice d'audit et les caractéristiques du produit.
- **Analyse** : jointe avec D3′ sur le mode tenu à l'écart, scellée, lue une seule fois.

### D3′. Les sondes ont-elles une valeur à budget égal ?

- **H_A** : à q̄ égal et horizon fixe, la largeur obtenue avec la répartition guidée par sondes est inférieure à celle de l'audit uniforme au taux q̄, d'au moins une marge préenregistrée (illustratif : 20 %), sous pression adaptative.
- **H_B** : la largeur est égale ou supérieure, gain négatif compris.
- **Bras** : uniforme q̄ ; moniteur texte ; vérifications mécaniques ; sondes ; scores de sonde permutés (même loi des π).
- **Contrôles** :
  - réglage fin bénin ;
  - consigne cachée bénigne ;
  - intervention placebo (consigne présente, dommage nul) ;
  - incompétence naturelle.
- **Test unitaire** (pas un duel) : scores anti-corrélés, avec l'élargissement attendu préenregistré.

### D4′. L'évasion coûte-t-elle du dommage ?

- **Plan** : relation dose-réponse en pression d'évasion λ, à budget de construction fixe ; dommage lu sur la vérité plantée.
- **Contrôle** : pénalité placebo de même norme, sur une direction aléatoire.
- **Hypothèses** : H_A, la pente du dommage selon λ dépasse la marge. H_B, la pente reste dans la marge d'équivalence (TOST).
- **Issues** : un intervalle qui chevauche la marge donne « non jugeable ».

### D5′. Le biais ε d'un substitut de jumeau prédit-il ses fausses alertes ?

- **H_A** : le taux de fausses alertes de l'incrimination par substitut est prédit par ε, mesuré sur des paires A/A tenues à l'écart du calibrage.
- **H_B** : il ne l'est pas ; un autre facteur domine, par exemple une hétérogénéité de variance entre tâches.
- **Contrôles** :
  - substituts hors de la lignée des saboteurs ;
  - intervention placebo ;
  - A/A du même modèle sur des sous-domaines tenus à l'écart.
- **Rang** : en dernier ; ce test sert la piste de l'incrimination, que je ne place plus au centre.

---

## (c) Réponse à l'arbitre, en une page

**Ce qui est établi.** Rien d'empirique dans ce dossier : aucune mesure du programme n'est transmise. Sont établis au sens documentaire [R] :
- le dispositif du programme ;
- les citations du domaine : l'incrimination exige une référence bénigne ; la vérité terrain est souvent indéfinie sur les tâches floues ; l'assurance du monitorage d'activations reste ouverte ; les défenses latentes sont vulnérables à l'obscurcissement ;
- un résultat statistique classique : Horvitz-Thompson est sans biais avec des probabilités d'inclusion connues et non nulles.

Les trois critiques convergent sur des dérivations [H] que je ne conteste pas :
- une sonde trompée élargit la borne en 1/q_min ;
- un biais d'oracle constant s'accumule en N·b ;
- la borne devient triviale sous un plancher de q_min calculable.

**Ce qui ne l'est pas, et que le programme peut trancher :**
1. Un oracle de tâches floues a-t-il un biais adverse assez petit pour qu'un certificat par audit ait un horizon utile ? [NSP] Tout le cap en dépend.
2. La couverture tient-elle contre la vérité plantée, et pas seulement contre l'oracle ? [NSP]
3. Les états internes réduisent-ils la largeur de la borne à budget égal, sous pression adaptative ? [NSP] C'est la question « limits of white-box techniques » de l'appel d'août 2025 [R], posée dans un dispositif où les sondes peuvent coûter de l'efficacité, mais pas la validité.

**Ce qui ne l'est pas et n'est pas à sa portée :**
- le transfert aux modèles de pointe ;
- des intrigants réels ;
- la garantie que l'équipe rouge domine les attaques réelles (2512.22154) [R].

Ce dernier point vaut aussi pour l'oracle : mon certificat dépend de l'équipe rouge qui mesure b⁺. Je l'avais d'abord présenté comme indépendant de l'équipe rouge ; c'était faux.

**Cap** [H]. Je maintiens le cap « certifier une qualité par audit plutôt qu'incriminer », mais je le présente comme un *déplacement* de l'exigence : d'une loi bénigne du flux vers un juge correct sur un échantillon. Ce n'est pas un contournement. Le résultat qui pourrait marquer est une **loi de coût avec horizon** : le q_min minimal et le N_max en fonction de Δ_tol, δ et b⁺. Les deux signes de cette loi seraient publiables. Si aucun horizon n'est utile, c'est une limite propre du contrôle par audit sur les tâches floues. Ce n'est pas une « défense qui tient », que l'équipe rouge suivante casserait.

**L'expérience à faire en premier : D1′**, précédée de deux étapes peu coûteuses :
- faire fixer Δ_tol et le standard de qualité par deux ou trois équipes de contrôle extérieures, avec leurs prédictions scellées ;
- mesurer la variance honnête/honnête, qui donne la résolution.

Pourquoi D1′ d'abord : D2′, D3′ et D4′ supposent un oracle valide, et C-b2 montre qu'un biais adverse même petit borne l'horizon de tout le reste.
- **H_B de D1′** (aucun horizon utile) : le programme pivote vers « l'instrument », c'est-à-dire durcir le juge, ou vers des tâches à vérité mécanique partielle.
- **H_A** : D2′ et D3′ suivent, en une seule analyse jointe scellée sur le mode tenu à l'écart.

FIN-DE-CELLULE