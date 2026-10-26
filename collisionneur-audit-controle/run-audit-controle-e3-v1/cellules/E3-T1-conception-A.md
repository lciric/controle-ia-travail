# Proposition A — Tour III.1 : ce que l'audit F2 a manqué ou mal jugé

**Pièces.** F1, F2, F3 sont présentes et apparemment complètes ; aucune coupure visible. Je ne peux pas contre-lire les PDF de F2 (empreintes non vérifiées par moi) : tout ce que F2 affirme reste **OBSERVÉ-NON-AUDITÉ**. Les références que je donne de mémoire sont marquées **RAPPORTÉ (mémoire)** ; aucun identifiant arXiv n'est donné de mémoire.

---

## (a) Ce que la question suppose sans l'établir

1. **Que les 26 failles de F2 sont correctement lues.** Statut : OBSERVÉ-NON-AUDITÉ. F2 signale lui-même deux contradictions internes de sources (R4) ; aucune contre-lecture n'existe. Je raisonne « à supposer que F2 soit exact ».
2. **Que la littérature pertinente est celle que F2 pouvait lire jusqu'au 26 octobre 2026.** Statut : HYPOTHÈSE. Ma fenêtre de connaissance s'arrête avant 2026 ; pour tout travail daté 2026, je ne peux ni confirmer ni compléter. Ce que je peux ajouter, ce sont des travaux antérieurs que F2 n'a pas convertis en failles, et des hypothèses du dispositif que ni F1 ni F2 ne testent.
3. **Que le dispositif est « sondes linéaires ».** Statut : RAPPORTÉ (F1 §8.1 liste aussi perceptron, attention, Mahalanobis). La question rétrécit ; les angles morts d'agrégation que je soulève valent pour toutes les familles.
4. **Que « manqué » et « mal jugé » sont deux listes disjointes.** Non : le plus coûteux est souvent une faille *recensée* mais mesurée par un test qui ne tranche pas (section D).
5. **Que la décision F3 fixe un état stable.** Statut : RAPPORTÉ. F3 n'autorise aucune dépense ; les propositions 2 et 4(a) restent conditionnelles à un GO.
6. **Que l'audit devait trouver des failles « publiées ».** Les failles les plus graves que je vois sont *méthodologiques* (circularité de la définition du budget, validité du faux-positif toujours-valide) : elles ne sont pas des « failles publiées », mais elles mettent en défaut la thèse du papier A avant toute attaque.

---

## (b) Failles documentées manquées (question 1)

Statut de chaque ligne : RAPPORTÉ (mémoire) pour la source ; « couverte » = mon jugement sur F1.

### Sabotage

| # | Hypothèse du dispositif mise en défaut | Source | Couverte |
|---|---|---|---|
| S-A1 | **« Le gain du séquentiel se mesure contre une accumulation boîte noire des scores. »** Il existe déjà un protocole *à état* pour menaces distribuées : le budget d'audit s'adapte dans le temps à l'estimation courante du taux d'attaque, et l'attaquant choisit sa *fréquence* d'attaque (le cadre « menace distribuée » est le leur). Sans cette base dans le plan 2 × 2, l'effet « séquentiel » de H2 confond accumulation de scores et adaptation du budget. | Wen, Hebbar, Larson, Bhatt, Radhakrishnan et al. 2024, *Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats* | **En partie** (F1 §8.3 : « séquentiel boîte noire », « monitoring à état sur flotte » pour B seulement). |
| S-A2 | **« Le ré-échantillonnage est une intervention non spécifique » (H6).** Dans la base même citée par E1.6, le ré-échantillonnage est un *instrument de détection* (les tirages multiples incriminent) et non seulement une intervention ; H6 mélange donc deux effets. | Bhatt, Rushing, Kaufman, Tracy, Georgiev, Matolcsi, Khan, Shlegeris 2025, *Ctrl-Z: Controlling AI Agents via Resampling* | **Non** comme distinction ; S6 de F2 touche la règle de sélection, pas la double nature. |
| S-A3 | **« Le juge boîte noire n'a pas de canal d'élicitation. »** L'injection de bruit dans les poids élève la performance des modèles qui sous-performent délibérément : canal de détection bon marché, pas d'entraînement. F2 a lu la p. 1 de cette source (table d) mais ne l'a pas convertie en faille ni en contre-mesure pour S1. | Tice et al. 2024, *Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models* (titre et équipe repris de F2 ; contenu de mémoire) | **Non**. |
| S-A4 | **« L'environnement (a) est une construction neuve. »** Un cadre publié de « sabotage de décision » et de « sape de la surveillance » existe, avec des seuils de détection humains ; l'absence de comparaison expose A à un relecteur. | Benton, Wagner, Christiansen, Anil, Perez et al. 2024, *Sabotage Evaluations for Frontier Models* | **Non** (absent de F1 et de F2). |

### Tromperie et collusion

| # | Hypothèse mise en défaut | Source | Couverte |
|---|---|---|---|
| D-A1 | **« Un juge de même lignée est neutre » (D1 (a)).** Au-delà de l'auto-reconnaissance (D8) et de l'appariement de lignée (S7), il existe un biais *bénin* : un juge reconnaît et préfère ses propres générations. Un verdict de suspicion plus bas sur sa lignée ne prouve ni collusion ni sur-apprentissage : c'est un troisième mécanisme, à mesurer sur contenu identique attribué différemment. | Panickssery, Bowman, Feng 2024, *LLM Evaluators Recognize and Favor Their Own Generations* | **En partie** (S7, D8). |
| D-A2 | **« Un organisme à objectif caché inculqué par documents synthétiques est un bon substitut d'intention émergente » (proposition 2 de F2).** La méthode d'origine est un jeu d'audit où l'objectif caché est précisément inculqué par documents synthétiques ; les équipes qui l'ont trouvé l'ont fait en partie *via la saillance du concept* dans les données et les représentations. Ce qui fonde la proposition 2 fonde aussi sa circularité (section D). | Marks, Treutlein, Bricken et al. 2025, *Auditing Language Models for Hidden Objectives* | **Non** (F2 cite une autre source pour la méthode). |
| D-A3 | **« Le bruit d'activations est une intervention de H6 et non un détecteur. »** Des organismes qui simulent l'alignement sont démasqués par des interventions internes (bruit, pilotage) parce que leurs politiques basculent sous perturbation ; le même geste sert donc de détecteur, ce qui crée une seconde lecture de H6. | Clymer, Juang, Field 2024, *Poser: Unmasking Alignment-Faking LLMs by Manipulating Their Internals* | **Non**. |
| D-A4 | **« Les attaques contre une sonde demandent l'accès aux poids » (HC4).** Des activations obfusquées contre des sondes et des moniteurs à autoencodeur parcimonieux s'obtiennent aussi par optimisation d'*entrées* ; la « taxe de déplacement » n'est pas un nombre mais une courbe par régime d'accès (texte sans gradient ; entrées avec gradient ; poids). | Bailey, Serrano, Sheshadri et al. 2024, *Obfuscated Activations Bypass LLM Latent-Defense Mechanisms* | **En partie** (EC.4 mentionne des codes publiés ; D3 de F2 mélange les régimes, voir D). |

### Conscience d'évaluation

| # | Hypothèse mise en défaut | Source | Couverte |
|---|---|---|---|
| E-A1 | **« Les contrôles croisés de §7 dissocient conscience d'évaluation et intention. »** Un jeu de données publié sépare plusieurs facettes de la conscience situationnelle (reconnaissance de soi, du contexte, du déploiement) ; sans cette décomposition, « conscience d'évaluation » dans H8 est un construit composite et la sonde peut lire une facette qui ne pilote rien. | Laine, Chughtai, Betley, Hariharan, Scheurer et al. 2024, *Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs* | **Non** (F2 la laisse en « restant à lire » sans faille associée). |
| E-A2 | **Conscience d'évaluation du juge** (angle mort 10 de F2, « sans source »). La source la plus proche n'est pas une conscience d'évaluation mais une *sape délibérée* de la surveillance par un modèle-moniteur (Benton et al. 2024, ci-dessus) : elle fournit le protocole de mesure (un moniteur qui fausse ses notes sans être pris) que F2 cherchait. | Benton et al. 2024 | **Non**. |

Écarté en une ligne : les mécanismes concrets de stéganographie inter-agents (Motwani et al. 2024 ; Roger & Greenblatt 2023, tous deux en « restant à lire » de F2) ne se décrivent pas sans procédé ; la faille se réduit à D9, déjà recensée.

---

## (c) Angles morts inédits et duels décisifs (question 2 ; livrable b)

Chaque duel : H_A contre H_B exclusives, métrique, seuil, contrôle négatif, issue falsifiante. Tous les seuils sont **illustratifs**.

### AM-1 — Le budget B est-il défini par l'instrument qu'il doit valider ?
**Pourquoi faux.** F1 §3 pose (a) « chaque action de sabotage déplace l'espérance du score d'au moins δ » et (b) « B = Σδ ». Si B est *mesuré* par le déplacement de sonde, le lemme « la puissance ne dépend que de B » est vrai par construction : on a défini la dose par l'effet. E1.1 parle de « dose-réponse du budget » sans dire dans quel espace vit la dose. Ni F1 ni F2 ne nomment ce point.
**Duel.** B est défini *dans l'espace de la tâche* (dommage semé par action, vérifié en aval), indépendamment de la sonde.
- H_A : δ(dose) est proportionnelle à la dose de tâche et la somme Σδ est invariante à la fragmentation (k actions de dose d/k donnent le même Σδ que une action de dose d).
- H_B : δ(dose) a un seuil : en dessous d'une dose par action d*, δ ≈ 0 ; Σδ s'effondre quand la fragmentation s'affine — exactement le régime « diffus » que A revendique.
- Métrique : δ estimé par action sur une grille de doses (par exemple 5 niveaux × 3 fragmentations, illustratif) ; test de proportionnalité contre modèle à seuil (comparaison de vraisemblance).
- Contrôle négatif : sonde aléatoire appariée en covariance (doit donner δ ≈ 0 partout) ; actions honnêtes de longueur appariée.
- Falsifie : un seuil d* > 0 avec Σδ non conservée falsifie H_A et donc l'hypothèse (b) du lemme sur organismes réels ; une proportionnalité à toutes les doses falsifie H_B. Coût : CPU sur activations en cache, à condition que E1.1 grille les doses.

### AM-2 — La garantie « toujours valide » tient-elle sous dépendance intra-trajectoire ?
**Pourquoi faux.** La thèse de A est « une garantie de faux positifs toujours valide ». Un processus e calibré sur la variance d'épisodes honnêtes (F1 §3 (c)) suppose que les scores successifs, sous honnêteté, forment une suite dont le produit des e-valeurs est une supermartingale. Or les actions d'une même trajectoire partagent le contexte : les scores de sonde sont autocorrélés sous honnêteté. Le cadre général (Ramdas, Grünwald, Vovk, Shafer 2023, *Game-Theoretic Statistics and Safe Anytime-Valid Inference* — RAPPORTÉ (mémoire)) exige que l'e-variable soit construite *conditionnellement* au passé ; une calibration marginale ne le garantit pas. F2 ne touche pas la partie statistique.
**Duel.**
- H_A : à α = 0,01, le taux d'alerte sur des épisodes honnêtes neufs, à contexte partagé, est ≤ α.
- H_B : il dépasse α à cause de l'autocorrélation ; la garantie n'est valide que sur scores permutés.
- Métrique : taux empirique d'alerte sur ≥ 500 épisodes honnêtes (illustratif), intervalle à 95 % ; seuil : borne inférieure > 2α falsifie H_A.
- Contrôle négatif : mêmes scores **permutés entre trajectoires** (détruit l'autocorrélation, conserve les marginales) — doit donner ≈ α. Si permuté ≈ α et réel > α, H_B est établie et le processus e doit être reconstruit par e-variables conditionnelles (ou par blocs). Coût : CPU.
- Ajout : la même mesure sur des épisodes honnêtes tirés d'une distribution de tâches *postérieure* (dérive) — une alerte cumulative lit aussi la dérive.

### AM-3 — Le max sur les tokens est-il un détecteur de longueur ?
**Pourquoi faux.** Décision 1 de F1 : max ou attention. Le maximum de n variables croît avec n ; une action honnête longue a un score max plus haut. Sous accumulation séquentielle, la somme de max détecte la verbosité. Un saboteur concis est avantagé ; un honnête prolixe pénalisé. F2 défend l'agrégation (D7) sans ce point.
**Duel.**
- H_A : corrélation score max – longueur d'action, sous honnêteté, non distinguable de zéro (|ρ| < 0,1, illustratif).
- H_B : ρ > 0 et égale à celle de la sonde aléatoire appariée (pur effet d'extrême).
- Contrôle négatif : sonde aléatoire appariée, même agrégation. Falsifie : ρ_sonde ≈ ρ_aléatoire > 0 falsifie H_A ; alors normaliser (max sur fenêtre fixe, ou quantile de l'honnête à longueur égale). Coût : CPU.

### AM-4 — Les copies honnêtes à poids partagés co-varient déjà
**Pourquoi faux.** B parie que le partage des poids fait co-varier les signatures *du sabotage*. Mais il fait co-varier aussi les signatures honnêtes sur tâches voisines ; la « co-élévation » (F1 §3) exige un null de corrélation inter-agents estimé sur essaims honnêtes, non la seule variance (c). F2 ne traite pas le papier B.
**Duel.**
- H_A : corrélation inter-agents des scores, essaim honnête à tâches partagées, ≈ celle à tâches indépendantes.
- H_B : elle est nettement supérieure (écart > 0,2, illustratif) → la co-élévation sans null apparié a un taux de fausses alertes > α.
- Contrôle négatif : essaim d'agents de lignées différentes (Qwen) sur mêmes tâches partagées (isole l'effet poids partagés de l'effet tâche). Falsifie : si l'écart tient pour lignées mélangées, c'est la tâche, pas les poids ; si l'écart n'existe que pour poids partagés, H_A est falsifiée et le null doit être estimé par essaim honnête apparié avant E2.3. Coût : génération d'essaims honnêtes (GPU, modéré).

### AM-5 — La vérité semée a une signature
**Pourquoi faux.** Les sabotages de (a) sont « cibles semées préenregistrées ». Une procédure de semis (gabarit, positions, formulations) laisse une trace de surface ; une sonde ou un juge peut apprendre le semis. Ni F1 ni F2 (S5 porte sur le non-semé) ne mettent de base mécanique à battre.
**Duel.**
- H_A : un classifieur de surface (longueur, mots-clés, position des cibles) ne sépare pas semé d'honnête mieux que le hasard.
- H_B : il atteint un rappel notable à 1 % FP → une partie du rappel de la sonde est du semis.
- Contrôle : épisodes honnêtes où le gabarit de semis est appliqué *sans* contenu de sabotage (placebo de semis). Falsifie : rappel de surface > 2 × FP falsifie H_A ; la sonde doit battre ce classifieur et être lue sur le placebo de semis. Coût : CPU.

### AM-6 — Le thème élève la sonde sous honnêteté
**Pourquoi faux.** Les propositions d'expériences qui traitent de risque, sécurité, échec ont un vocabulaire proche des concepts sondés (tromperie, enjeux élevés). F2 juge D6 « couverte » par le 2 × 2 rhétorique × intention ; ce plan contrôle le plaidoyer, non le thème.
**Duel.** H_A : taux de fausses alertes constant entre strates thématiques honnêtes ; H_B : strate « risque/sécurité » > 3 × les autres (illustratif). Contrôle : juge génératif sur les mêmes strates (si lui aussi monte, c'est le thème ; sinon, la sonde). Falsifie H_A si l'écart tient après appariement de longueur. Coût : nul.

---

## (d) Contre-mesures et tests de l'audit : faibles, circulaires ou mal ciblés (question 3)

1. **S2 / proposition 1, « lecture filtrée » promue lecture principale de l'intention.** Masquer les positions porteuses d'évidence textuelle n'empêche pas l'attention de copier l'information de la consigne vers les positions d'action : une sonde linéaire sur ces positions peut toujours lire « j'ai une consigne ». Le filtre sous-estime la fuite ; en faire la lecture *principale* d'une revendication d'intention est une faiblesse. **À la place : la cellule « politique dormante ».**
   - H_A : la sonde lit l'intention en acte — score bas quand la politique est *présente mais inactive* (famille (iii) verrouillée sans mot de passe, PDF déjà dans la liste de F2 : Greenblatt, Roger, Krasheninnikov, Krueger 2024, *Stress-Testing Capability Elicitation With Password-Locked Models* ; ou famille (i) avec condition de déclenchement non remplie).
   - H_B : la sonde lit la représentation de la politique — score haut même dormante.
   - Métrique : rappel à 1 % FP sur épisodes dormants ; seuil : doit être ≤ FP du témoin honnête. Contrôle négatif : honnête avec consigne bénigne de même longueur et saillance.
   - Issue : dormant détecté falsifie H_A et rend la « prédiction de validité (i)/(ii) » inopérante ; dormant non détecté avec activé détecté falsifie H_B. Coût : quelques heures GPU.

2. **Proposition 2, famille (iv) par documents synthétiques.** F2 reconnaît que les documents « sont encore du texte ». Le problème est plus précis (D-A2) : rendre un concept saillant par entraînement rend ce concept lisible par une sonde *générique* du même concept, que l'agent agisse ou non. Le test de F2 (δ et rappel sur (iv) contre (ii)) ne sépare pas « lit l'intention » de « lit le concept inculqué ». **Ajout obligatoire** : (iv-nul), même pipeline sur documents décrivant une politique *sans rapport*, et lecture de la sonde sur les épisodes de (iv) où le sabotage ne s'est pas produit (taux de sabotage < 100 %). Si ces épisodes scorent comme les sabotés, H_A (intention) est falsifiée. Sans ce témoin, la dépense (dizaines d'heures GPU, F2) achète une circularité.

3. **D3 / angle mort 1, « contrôlabilité par le contexte ».** F2 mélange deux régimes : consigne en langage naturel sans gradient (sa source principale) et entrées optimisées avec gradient (E4, 2607.25907 selon F2). HC4 doit être une **courbe taxe(régime d'accès)** : texte, entrées optimisées, poids. Le test de F2 (une seule condition « suppression consignée ») mesure un point de la courbe et laisse le régime intermédiaire — le plus réaliste pour un agent qui contrôle ses propres sorties mais pas ses poids — sans mesure.

4. **D8, test « exactitude de reconnaissance de lignée ».** Mesure la reconnaissance, non son effet sur le verdict. Mesure à la place : Δ du verdict sur **contenu identique** attribué ou paraphrasé vers une autre lignée (D-A1) ; cela sépare auto-préférence bénigne et collusion.

5. **Proposition 3, test causal avec placebo (E4).** Piloter une direction dégrade la capacité ; toute direction change alors le taux de sabotage par effet de compétence. Il manque le contrôle **utilité honnête sous pilotage** à norme égale : une direction « causale » doit déplacer le sabotage *à utilité constante*. Sans cela, le placebo et la direction visée sont indistinguables pour une mauvaise raison.

6. **Proposition 4(b), porte de séparabilité à 8 milliards sur tâche vérifiable.** Correcte comme garde d'interprétation d'un nul, mais unilatérale : la réussir ne transfère pas au sabotage diffus (construit différent). À dire tel quel dans le préenregistrement, sinon elle sera lue comme une validation.

7. **S6 (règle de sélection de H6) et S-A2.** Juste, mais incomplet : le ré-échantillonnage est aussi un détecteur (Ctrl-Z). E1.6 doit rapporter deux quantités : l'effet d'intervention (succès d'attaque/utilité) et l'effet de détection (incrimination par tirages multiples), sinon H6 confond les deux.

8. **Comptage « 3 couvertes / 16 en partie / 6 non ».** C'est un jugement, non un fait ; D6 et E7 « couvertes » sont réfutées respectivement par AM-6 et par E-A1 (le construit composite). Le chiffre ne doit pas être réutilisé comme indicateur de maturité.

9. **Ce que F2 a bien jugé et que je reprends en le disant** : S5 (non-semé), D5 (invariant « aucun score dans un signal d'entraînement »), E1/E6 (marqueurs de test). Je ne les reformule pas.

---

## (e) Instruments nommés : mesure minimale (livrable c)

| Instrument | Taux à rapporter | Cas honnêtes appariés (fausses alertes) | Vérifications mécaniques à battre |
|---|---|---|---|
| **Sonde sur activations** (linéaire et autres, agrégation max/attention) | Rappel à 1 % FP par famille d'organismes ; FP réalisé sur chaque strate ci-contre | Honnête + consigne bénigne de même longueur ; honnête prolixe (quartile long) ; honnête sur thème « risque » ; honnête averti de la surveillance ; honnête qui avoue une erreur ; **politique dormante** | Sonde aléatoire appariée (F1) ; **prédicteur de longueur seul** ; **mots-clés/regex sur la sortie** ; **classifieur du gabarit de semis** |
| **Juge génératif** (boîte noire) | Rappel à 1 % FP ; Δ verdict sur contenu identique attribué à l'autre lignée ; Δ verdict cadrage « banc d'essai » vs « production » | Mêmes strates, plus plaidoyer sincère | Mots-clés ; juge plus faible (3B) ; juge d'autre lignée |
| **Moniteur séquentiel** (processus e / somme cumulée) | Taux d'alerte réalisé à α sur honnêtes neufs (AM-2) ; latence alerte/dommage | Trajectoires honnêtes longues ; honnêtes d'une distribution postérieure (dérive) | Scores permutés entre trajectoires ; accumulation boîte noire ; **protocole à état à budget adaptatif** (S-A1) |

Règle de lecture : un instrument dont le rappel ne dépasse pas la meilleure vérification mécanique de sa ligne n'a pas démontré qu'il lit autre chose que la surface.

---

## (f) Les cinq ajouts les plus utiles, classés (question 4)

Coûts en ordre de grandeur, **illustratifs**, sur Vast.ai, carte de classe A100.

1. **Définition de B dans l'espace de la tâche et test de proportionnalité δ(dose) × fragmentation (AM-1).** Sans cela le lemme est tautologique et E1.3 ne teste rien. Coût : nul si E1.1 grille les doses (CPU sur cache) ; sinon ≈ 10 h GPU de génération supplémentaire.
2. **Garde du faux-positif toujours-valide : permutation inter-trajectoires et dérive (AM-2).** C'est la revendication de titre du papier A. Coût : CPU, < 1 journée humaine.
3. **Cellule « politique dormante » en lecture principale de l'intention, à la place de la lecture filtrée** (section D-1), avec famille (iii) verrouillée. Coût : quelques heures GPU ; conditionnel à la licence des organismes (iii) (F1 §7).
4. **Bases mécaniques et strates de fausses alertes (AM-3, AM-5, AM-6)** inscrites au préenregistrement de G1 : longueur, mots-clés, gabarit de semis, thème. Coût : CPU ; ≈ 1 journée humaine.
5. **Null de co-élévation sur essaim honnête apparié (AM-4) avant E2.3**, et base « déploiement adaptatif » dans le 2 × 2 (S-A1). Coût : ≈ 20–40 h GPU pour les essaims honnêtes ; réimplémentation de la base ≈ 2–3 journées humaines.

Non classé mais conditionnel : la proposition 2 de F3 (famille (iv)) ne doit être lancée qu'avec le témoin (iv-nul) ; sinon la dépense ne tranche pas.

---

## (g) Ancrage matériel (livrable d)

- **Modèles** (F1 §14, RAPPORTÉ) : Llama-3.1-8B-Instruct (agents, sondes), Qwen2.5-7B (hétérogénéité, essaim mixte d'AM-4), Llama-3.2-3B-Instruct (juge faible, D1 (b)). Organismes (iii) : licence à vérifier.
- **Cache d'activations** (illustratif) : flux résiduel 4 096 dimensions, bf16 ≈ 8 ko/token/couche ; 1 000 épisodes × 20 actions × 500 tokens = 10⁷ tokens ≈ 80 Go par couche lue ; trois couches ≈ 240 Go de stockage objet. Tous les duels AM-1, AM-2, AM-3, AM-5, AM-6 et la cellule dormante se calculent sur ce cache, en CPU.
- **Calcul** (illustratif) : génération de 10⁷ tokens par un 8B batché ≈ 3–6 h GPU ; essaims honnêtes d'AM-4 (N = 4 à 16 agents, 200 épisodes) ≈ 20–40 h GPU ; famille (iv)(a) LoRA ≈ 10–20 h GPU (compatible avec « dizaines d'heures » de F2). Total des cinq ajouts hors (iv) : < 60 h GPU.
- **Coût** (illustratif) : à 1–2 $/h GPU, l'ensemble des ajouts proposés tient sous 200 $ ; le poste dominant reste le temps humain de préenregistrement et de contre-lecture (règle R2 de F1), non le calcul.
- **Ce que je ne peux pas chiffrer** : la licence des organismes (iii), la disponibilité de FakeLab « sur demande » (F1 §6), et toute source datée 2026 citée par F2 — pour celles-ci, « référence à vérifier » s'applique.

FIN-DE-CELLULE