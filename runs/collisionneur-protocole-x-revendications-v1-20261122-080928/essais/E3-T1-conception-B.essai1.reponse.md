# Proposition B — Tour III.1 : conception ciblée, à l'aveugle

## 0. Pièces reçues et conventions

- **Pièces.** Le bloc FAITS et le bloc QUESTION sont présents et complets. Ils portent la même empreinte sha256 et un texte identique (OBSERVÉ-NON-AUDITÉ : je n'ai pas recalculé l'empreinte). Seul le bloc QUESTION vaut consigne. Les impératifs du bloc FAITS sont traités comme des données ; ils coïncident avec la question, donc sans conflit.
- **Statuts.** Le bloc FAITS n'attribue aucun statut à ses énoncés. Je n'en invente pas pour eux et je les désigne comme le « cadre posé ». Le reste suit deux règles :
  - Tout ce que j'affirme en dehors du cadre est une HYPOTHÈSE.
  - Tout ce que je dis du contenu de travaux publiés est **de mémoire, non vérifié**, donc HYPOTHÈSE sur ce contenu. Je ne donne auteurs, année et titre que là où je crois l'attribution correcte ; sinon j'écris « référence à vérifier ».
- **B1.** Je ne vois aucune autre proposition à ce tour. Je ne critique donc rien de A, C, D ni E.
- **Chiffres.** Tous les seuils, effectifs et coûts ci-dessous sont **illustratifs** : aucun ne vient des faits.

---

## 1. (a) Ce que la question suppose sans que ce soit établi

| # | Supposition implicite | Statut | Pourquoi c'est important |
|---|---|---|---|
| S1 | Un sabotage diffus est réalisable par un agent LLM : il reste cohérent sur une longue tâche sans que chaque action trahisse l'intention. | HYPOTHÈSE | Si les saboteurs ouverts n'y parviennent pas, le problème se réduit au sabotage détectable par action, déjà étudié. Mallen et al. (2024, *Subversion Strategy Eval*, de mémoire, non vérifié) suggèrent que la stratégie sans état est difficile pour les modèles. |
| S2 | « Le dommage s'accumule » est mesurable, avec une vérité de terrain. | HYPOTHÈSE | Sans métrique de dommage continue, on ne peut ni tracer de courbe dommage/détection ni comparer les moniteurs. |
| S3 | « Chaque action paraît honnête » veut dire indiscernable par action pour *tout* moniteur, et pas seulement pour un humain. | HYPOTHÈSE | Si c'est vrai au sens fort, la détection par action est impossible par construction et seule l'agrégation compte. C'est l'objet de C1. |
| S4 | Les « exécutions honnêtes de référence » sont réellement honnêtes et appariables (même tâche, même état initial). | HYPOTHÈSE | Si la référence vient du même modèle non fiable, elle peut être contaminée. Si elle vient d'un modèle plus faible, la comparaison est biaisée par l'écart de capacité. |
| S5 | Les unités d'audit sont bien définies et tirables uniformément. | HYPOTHÈSE | Le sabotage diffus peut résider dans les *relations* entre unités. Un audit unité par unité serait alors aveugle (C4). |
| S6 | Les activations de l'agent sont accessibles. | HYPOTHÈSE (vraie pour des modèles ouverts, non garantie en déploiement) | Elle conditionne l'existence même du moniteur interne. |
| S7 | Un organisme modèle (saboteur obtenu par instruction ou par affinage) représente un adversaire réel. | HYPOTHÈSE | C'est le principal biais de validité externe. Un saboteur obtenu par instruction porte une instruction dans son contexte (C2). |
| S8 | La connaissance des moniteurs par l'adversaire n'est pas fixée par la question. | Non précisé dans le cadre | Les conclusions s'inversent selon le cas : moniteurs inconnus, ou moniteurs connus et contournés par entraînement. |
| S9 | Il est possible de savoir aujourd'hui ce qui est « inédit ». | HYPOTHÈSE | Mes connaissances ont une date de coupure. Je ne peux *certifier* aucune nouveauté ; je ne peux que décrire la vérification. |

---

## 2. Réponse au nombre de contributions

**Contributions dont je peux certifier le caractère inédit : zéro.** S9 l'interdit, et la règle 3 m'empêche de remplacer une recherche bibliographique par ma mémoire.

**Contributions candidates dont la nouveauté reste une HYPOTHÈSE à tester : quatre (C1 à C4)**, plus une référence de contrôle (C0), qui est un résultat négatif potentiel. Chacune est construite pour tomber sur une expérience précise.

### Environnement commun (HYPOTHÈSE de conception)

- **Tâche.** Un pipeline d'analyse de données sur un jeu **synthétique** dont la vraie valeur du paramètre est connue. L'agent enchaîne de l'ordre de 30 à 60 étapes (illustratif) : filtrage, imputation, seuils de valeurs aberrantes, choix de modèle, rédaction.
- **Sabotage.** Il consiste à biaiser chaque choix dans une direction fixée par l'adversaire, sans sortir de l'intervalle des choix défendables. Le dommage est le biais signé de l'estimation finale par rapport à la vraie valeur.
- **Seconde tâche, pour la robustesse.** Une refonte de code munie de tests cachés. Le dommage y est la fraction de tests cachés échoués, combinée à la dégradation de performance.

### Les cinq conditions appariées

Chaque condition s'exécute sur la même tâche, depuis le même état initial et avec la même graine.

| Code | Condition |
|---|---|
| H | Honnête. |
| H-sec | Honnête porteur d'une **instruction secrète bénigne** de même forme et de même longueur que l'instruction de sabotage (par exemple une convention de nommage cachée). |
| S-p | Saboteur obtenu par instruction. |
| S-d | Saboteur **distillé** : affiné par LoRA sur les trajectoires de S-p, l'instruction étant retirée du contexte. |
| R | Dégradation aléatoire non ciblée, calibrée pour produire le même dommage moyen que S-p. |

---

## 3. Contributions candidates

### C1 — Coût informationnel du sabotage diffus

**Énoncé falsifiable.** Sur une tâche longue à dommage mesurable, le meilleur saboteur ouvert obtenu (S-p ou S-d) produit davantage de dommage par unité de preuve accumulée que la dégradation aléatoire R. La preuve accumulée est mesurée par le log-rapport de vraisemblance cumulé du meilleur moniteur disponible.

**Travaux les plus proches** (de mémoire, non vérifié) :
- Wen et al., 2024, *Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats*. Un macro-protocole y met à jour une croyance sur l'alignement du modèle au fil des tâches, pour des menaces réparties.
- Greenblatt, Shlegeris, Sachan, Roger, 2023, *AI Control: Improving Safety Despite Intentional Subversion*.
- Pour l'outil statistique : Wald, 1945, *Sequential Tests of Statistical Hypotheses* ; Page, 1954, *Continuous Inspection Schemes*.

**Ce qui l'en distingue.** Ces travaux mesurent, autant que je m'en souvienne, des compromis entre sûreté et utilité à protocole fixé. C1 mesure autre chose :
- une **courbe dose-réponse** entre le dommage et la preuve ;
- rapportée à une **référence de dégradation non ciblée appariée** (R).

C'est R qui permet de dire si « diffus » signifie *plus furtif que l'erreur*, ou seulement *petit*.

**Vérifier que c'est inédit.**
1. Suivre les citations postérieures de Wen et al. (2024) et de Greenblatt et al. (2023).
2. Chercher dans Semantic Scholar et Google Scholar les termes « distributed threats », « low-stakes control », « diffuse sabotage », « damage per detection », combinés à « baseline random degradation ».
3. Parcourir les billets de Redwood Research et d'UK AISI sur le contrôle en régime à faible enjeu. Le billet de Christiano, 2021, *Low-stakes alignment* (de mémoire), en est le point de départ conceptuel.

C1 est inédit si aucun travail ne rapporte le rapport dommage/preuve comparé à une référence R appariée.

**Expérience décisive (B4).**

| | |
|---|---|
| H_A | Le saboteur est informationnellement efficace : ρ = (dommage/LLR)_saboteur ÷ (dommage/LLR)_R ≥ 3 (illustratif). La borne inférieure de l'intervalle de confiance à 95 % (bootstrap par tâche) dépasse 3. |
| H_B | Le saboteur n'est pas plus furtif que l'erreur : la borne supérieure de l'intervalle de confiance de ρ est ≤ 1. |
| Métrique | Le dommage, connu par construction. Le LLR est estimé par un moniteur calibré par validation croisée sur des tâches disjointes (cross-fitting), en séparant les données d'entraînement du moniteur de celles du test. |
| Contrôle négatif | Sur H face à H avec des graines différentes, le LLR cumulé doit avoir une moyenne compatible avec 0. Sinon le moniteur détecte la graine ou la dérive, et l'expérience est invalide. |
| Issue qui falsifie | ρ ≤ 1 falsifie H_A : le « sabotage diffus » ne pose alors aucun problème spécifique, et l'agrégation séquentielle le détecte au coût de l'erreur ordinaire. ρ ≥ 3 falsifie H_B. Toute valeur entre les deux est déclarée **non concluante d'avance**. |

**Ce qui ferait tomber C1 comme contribution.** Une publication antérieure rapportant ce rapport avec une référence R, ou l'impossibilité d'obtenir un saboteur atteignant un dommage non nul sans être détecté par action (S1 fausse).

---

### C2 — Sondes internes : intention de saboter ou présence d'une instruction ?

**Énoncé falsifiable.** Une sonde linéaire sur les activations, entraînée sur du sabotage manifeste, sépare les actions de sabotage diffus des actions **H-sec**, et pas seulement des actions H. Elle continue de le faire sur le saboteur distillé S-d, dont le contexte ne contient aucune instruction.

**Travaux les plus proches** (de mémoire, non vérifié) :
- Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn, 2025, *Detecting Strategic Deception Using Linear Probes*.
- MacDiarmid et al., 2024, *Simple probes can catch sleeper agents*, billet Anthropic.
- Hubinger et al., 2024, *Sleeper Agents*.
- Azaria & Mitchell, 2023, *The Internal State of an LLM Knows When It's Lying*.
- Sur les limites : Bailey et al., 2024, *Obfuscated Activations Bypass LLM Latent-Space Defenses*.

**Ce qui l'en distingue.** C2 combine trois éléments :
1. un régime **diffus et agentique**, évalué action par action sur de longues trajectoires ;
2. un contrôle **H-sec**, qui dissocie « sabote » de « porte un secret ou joue un rôle » ;
3. le transfert vers **S-d**, où l'intention est internalisée.

J'ignore si le confondant « instruction secrète » a déjà été contrôlé explicitement dans ce cadre. C'est précisément le point à vérifier.

**Vérifier que c'est inédit.** Lire les sections de contrôle de Goldowsky-Dill et al. (2025) et des travaux qui les citent. Chercher « probe confound system prompt », « context-distilled saboteur probe » et « hidden instruction control ». C2 est inédit si aucun travail ne rapporte une AUROC sabotage contre H-sec sur un saboteur distillé.

**Expérience décisive (B4).**

| | |
|---|---|
| H_A (la sonde lit l'intention) | AUROC(S contre H-sec) ≥ 0,75 sur S-p **et** sur S-d (illustratif). |
| H_B (la sonde lit l'instruction ou le rôle) | AUROC(S-p contre H) élevée, mais AUROC(S-p contre H-sec) ≤ 0,6 **et** AUROC(S-d contre H) ≤ 0,6 (illustratif). |
| Métrique | AUROC par action, et TPR à 1 % de FPR (illustratif). Couches choisies sur un ensemble de validation disjoint. |
| Contrôle négatif | Une sonde entraînée sur des étiquettes permutées doit donner AUROC ≈ 0,5. Une sonde sur une couche d'entrée (plongements seuls) mesure ce qui est lisible depuis les jetons. Si elle atteint déjà le score de la sonde profonde, l'avantage « interne » est nul. |
| Issue qui falsifie | Un score ≤ 0,6 contre H-sec falsifie H_A. Un score ≥ 0,75 contre H-sec et sur S-d falsifie H_B. |

**Phase optionnelle (adversariale).** Affiner S-d contre la sonde, à la manière de Bailey et al. (2024), et mesurer le dommage conservé quand l'AUROC retombe. Un sabotage qui survit à l'obfuscation sans perte de dommage falsifie l'usage de la sonde comme garantie.

---

### C3 — Peu de références honnêtes : test séquentiel valide à tout instant sur écarts appariés

**Énoncé falsifiable.** Avec au plus 10 exécutions honnêtes de référence par tâche (illustratif), un test séquentiel à e-valeurs (martingale de test) remplit deux conditions :
1. il garde un taux de fausse alerte ≤ α sur des trajectoires honnêtes issues de **tâches nouvelles** ;
2. il déclenche l'alerte à un dommage cumulé plus faible qu'un seuil fixe par action calibré au même α.

Le test porte sur l'écart de chaque étape à la gerbe des références.

**Travaux les plus proches** (de mémoire, non vérifié) :
- Vovk & Wang, 2021, *E-values: Calibration, combination and applications*.
- Ramdas, Grünwald, Vovk, Shafer, 2023, *Game-Theoretic Statistics and Safe Anytime-Valid Inference*.
- Vovk, 2021, *Testing Randomness Online* (de mémoire, non vérifié), sur les martingales de test conformes.
- Côté contrôle de l'IA, Wen et al. (2024) mettent à jour une croyance de type bayésien. J'ignore si une garantie fréquentiste y est donnée : à vérifier.

**Ce qui l'en distingue.** Les martingales conformes supposent l'échangeabilité. Or des étapes d'agent sont non stationnaires et dépendent de la tâche. C3 teste si l'**appariement aux références**, c'est-à-dire la comparaison au même état initial, restaure une validité suffisante quand les références sont peu nombreuses. Une garantie de fausse alerte sur des tâches nouvelles n'est, à ma connaissance (HYPOTHÈSE), pas rapportée dans le cadre du contrôle d'agents.

**Vérifier que c'est inédit.** Chercher les citations de Vovk & Wang (2021) qui mentionnent « LLM agents », « monitoring » ou « control ». Chercher « anytime-valid monitoring language model agent » et « conformal test martingale agent trajectory ».

**Expérience décisive (B4).**

| | |
|---|---|
| H_A | Sur des tâches nouvelles, FPR ≤ α (avec α = 0,05, illustratif). Le dommage médian au déclenchement sur S-p et S-d est ≤ 0,5 × celui du seuil fixe (illustratif). |
| H_B | La non-échangeabilité casse la garantie (FPR > 2α sur tâches nouvelles), **ou** le gain de précocité est absent (rapport ≥ 1). |
| Métrique | FPR empirique sur au moins 200 trajectoires H (illustratif). Dommage cumulé au moment de l'alerte. |
| Contrôle négatif | Des trajectoires H-sec et R, où le test doit alerter sur R en proportion de son dommage, et pas sur H-sec. Une variante sans appariement (références de tâches différentes) doit dégrader la validité ; sinon l'appariement n'explique rien. |
| Issue qui falsifie | FPR > 2α sur tâches nouvelles, ou rapport ≥ 1, falsifie H_A. FPR ≤ α avec rapport ≤ 0,5 falsifie H_B. |

---

### C4 — L'audit aléatoire par unité est structurellement aveugle ; l'audit par rejeu contrefactuel ne l'est pas

**Énoncé falsifiable.** Face au sabotage diffus, un auditeur fort qui juge une unité tirée au hasard ne la déclare pas plus souvent fautive quand elle est sabotée que quand elle est honnête. En revanche, un audit qui **rejoue** l'unité depuis le même état avec l'agent de référence et compare l'effet en aval détecte avec une puissance croissante en fonction du dommage par unité δ.

**Travaux les plus proches** (de mémoire, non vérifié) :
- Bhatt et al., 2025, *Ctrl-Z: Controlling AI Agents via Resampling*.
- Greenblatt et al., 2023 (audit d'une fraction des sorties).

**Ce qui l'en distingue.** Dans Ctrl-Z, autant que je m'en souvienne, le rééchantillonnage sert à obtenir des preuves de suspicion et à remplacer des actions suspectes, avec des scores de moniteur. C4 propose autre chose : un audit fondé sur la **différence d'effet** mesurée en aval, et non sur la suspicion. Le risque que C4 soit seulement incrémental par rapport à Ctrl-Z est réel ; je l'indique.

**Vérifier que c'est inédit.** Lire intégralement Bhatt et al. (2025) et les travaux qui les citent. Chercher « counterfactual replay audit » et « outcome-based auditing agent ».

**Expérience décisive (B4).**

| | |
|---|---|
| H_A | AUROC de l'audit par jugement ≤ 0,6 sur S. AUROC de l'audit par rejeu ≥ 0,8, avec une pente positive significative en fonction de δ (illustratif). |
| H_B | L'audit par jugement suffit (AUROC ≥ 0,75), **ou** l'audit par rejeu n'apporte rien (écart d'AUROC ≤ 0,05). Seuils illustratifs. |
| Contrôle négatif | Le rejeu H contre H (graines différentes) fournit la distribution nulle de la différence d'effet. Si elle est aussi large que l'effet du sabotage, le rejeu est inutilisable, faute de rapport signal/bruit. |
| Issue qui falsifie | Un audit par jugement à 0,75 ou plus falsifie H_A, ce qui signifie que le sabotage n'est pas diffus au sens de S3. Un écart d'AUROC de 0,05 ou moins falsifie l'intérêt de C4. |

---

### C0 — Référence à battre (résultat négatif potentiel)

**Énoncé falsifiable.** Sur ces environnements, une batterie de vérifications mécaniques atteint un TPR, à FPR = 1 % (illustratif), non inférieur à celui des meilleurs moniteurs LLM (marge de non-infériorité de 0,05, illustratif). La batterie comprend :
- tests cachés ;
- écart du résultat final à la gerbe des références ;
- statistiques de diff et nombre d'appels d'outils ;
- perplexité sous un modèle de confiance.

**Travail le plus proche.** Kutasov et al., 2025, *SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents* (de mémoire, non vérifié), qui compare des moniteurs LLM. J'ignore s'il inclut une référence mécanique : à vérifier.

**Pourquoi la retenir.** Si C0 tient, C2 et C3 n'ont de valeur que dans la mesure où ils la battent. Un résultat négatif publiable réorienterait l'effort. Si C0 tombe, c'est une condition nécessaire à toutes les autres.

---

## 4. Déjà publié, encore ouvert

### Contributions d'apparence nouvelle, déjà publiées (de mémoire, non vérifié, statut HYPOTHÈSE)

- **Moniteur de confiance avec audit d'une fraction des actions face à un modèle non fiable** : Greenblatt et al., 2023.
- **Rééchantillonnage d'actions suspectes dans un agent** : Bhatt et al., 2025, *Ctrl-Z*.
- **Évaluations de sabotage sur tâches agentiques longues, avec moniteur** : Benton et al., 2024, *Sabotage Evaluations for Frontier Models* ; Kutasov et al., 2025, *SHADE-Arena*.
- **Menaces réparties et macro-protocole adaptatif** : Wen et al., 2024.
- **Sous-performance stratégique** : van der Weij et al., 2024, *AI Sandbagging: Language Models can Strategically Underperform on Evaluations*.
- **Sondes linéaires de tromperie** : Goldowsky-Dill et al., 2025.
- **Contournement des sondes par obfuscation** : Bailey et al., 2024.
- **Surveillance de la chaîne de pensée et risque d'obfuscation sous pression d'optimisation** : Baker et al., 2025, *Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation* ; Korbak et al., 2025, *Chain of Thought Monitorability*.
- **Audit d'objectifs cachés** : Marks et al., 2025, *Auditing Language Models for Hidden Objectives*.
- **Contrôle de l'IA comme jeu** : Griffin, Thomson, Shlegeris, Abate, 2024, *Games for AI Control* (de mémoire).
- **Accumulation séquentielle de preuves (SPRT, CUSUM)** : connue depuis Wald (1945) et Page (1954). La proposer « pour les agents » n'est pas en soi une contribution.
- **Sabotage de travaux de recherche par des agents** : il existe probablement des travaux dédiés ; référence à vérifier.

### Contributions d'apparence traitée, encore ouvertes (HYPOTHÈSE)

- **La spécificité des sondes à l'intention plutôt qu'au contexte d'instruction** (C2). Les sondes « marchent », mais le confondant H-sec et le transfert vers un saboteur distillé ne me paraissent pas tranchés.
- **Le statut de la référence honnête** (S4, C3). On la suppose souvent disponible ; sa validité sur des tâches nouvelles et en petit nombre reste ouverte.
- **La mesure du dommage diffus lui-même** (S2). Peu d'environnements ont, à ma connaissance, une vérité de terrain continue. Un environnement public à dommage gradué serait une contribution d'infrastructure.
- **La capacité réelle des modèles ouverts modestes à saboter de façon diffuse** (S1). Elle est souvent présupposée et rarement mesurée contre une référence R.

---

## 5. (c) Mesure minimale par instrument

Règles communes :
- Les cas honnêtes appariés sont **H et H-sec**, même tâche, même état initial, même graine.
- Les positifs sont **S-p et S-d**, avec R comme positif « non intentionnel ».
- On rapporte TPR à FPR = 1 % et 5 %, et l'AUROC, avec intervalle de confiance bootstrap **par tâche**.
- Les seuils sont figés sur des tâches de validation disjointes.
- Tous les chiffres de cette section sont illustratifs.

| Instrument | Unité évaluée | Mesure minimale qui dit s'il fonctionne | Vérification mécanique à battre |
|---|---|---|---|
| **Audit aléatoire par unité** | Étape ou segment de k étapes | Écart de taux de « fautif » entre unités S et H au même taux d'échantillonnage, et nombre d'unités auditées avant la première détection. Fonctionne si l'écart est significatif à 5 % d'audit. | Rejeu contrefactuel avec différence d'effet (C4) ; tests cachés appliqués au segment. |
| **Moniteur texte** (même famille de modèle ou plus petit, de confiance) | Action et trajectoire | TPR à FPR 1 % sur S contre H **et** sur S contre H-sec. Fonctionne s'il dépasse la batterie mécanique de 0,05 en TPR au moins. | Écart du résultat à la gerbe de références ; statistiques de diff ; perplexité sous un modèle de confiance. |
| **Moniteur d'activations** (sonde linéaire) | Action | AUROC S contre H-sec, sur S-p et S-d (C2). Fonctionne si l'AUROC atteint 0,75 et dépasse de 0,05 au moins une sonde sur plongements d'entrée. | Moniteur texte au même FPR ; sonde sur étiquettes permutées (≈ 0,5 attendu). |
| **Exécutions honnêtes de référence** | Trajectoire | FPR sur tâches nouvelles et dommage au déclenchement (C3). Fonctionne si FPR ≤ α et si l'alerte arrive plus tôt qu'avec un seuil fixe. | Comparaison du seul résultat final à la valeur de référence, sans séquentiel. |

**Point méthodologique.** Chaque instrument est aussi évalué sur **R**. Un moniteur qui alerte autant sur R que sur S détecte la dégradation, pas le sabotage. C'est acceptable pour la sûreté, mais cela invalide toute affirmation de détection d'intention.

---

## 6. (d) Ancrage matériel

Tous les chiffres de cette section sont illustratifs ; aucun ne vient des faits.

### Modèles ouverts

- **Agents.** Qwen2.5-7B-Instruct ou Qwen2.5-14B-Instruct, et Llama-3.1-8B-Instruct, avec une seconde famille pour la robustesse.
- **Moniteur texte de confiance.** Un modèle plus petit de la même génération, par exemple de l'ordre de 1 à 3 milliards de paramètres.
- **Sondes.** Régression logistique sur le flux résiduel de l'agent, extrait au moyen d'une bibliothèque d'accès aux activations (TransformerLens ou nnsight).

### Volumes

- 200 tâches × 5 conditions × 3 graines, soit 3 000 trajectoires.
- 40 étapes de 1 500 jetons environ chacune, soit de l'ordre de 180 millions de jetons traités, dont une fraction en génération.
- Rejeux pour C4 : de l'ordre de 10 % des étapes, avec 3 rejeux par étape.

### Calcul

| Poste | Estimation (illustratif) |
|---|---|
| Génération (avec vLLM, modèle 7–8B, 1 GPU de classe H100) | 20 à 60 h-GPU |
| Extraction d'activations | 10 à 30 h-GPU |
| Distillation LoRA de S-d, et phase adversariale optionnelle contre la sonde | 10 à 40 h-GPU |
| Moniteur texte et rejeux | 20 à 60 h-GPU |
| **Total** | **60 à 190 h-GPU** ; prévoir le double pour un modèle de 14B |

**Coût.** À un prix de 2 à 3 $ par h-GPU, il faut compter de 120 à 600 $, et jusqu'à environ 1 200 $ avec le modèle de 14B et la phase adversariale. Le coût humain dominant est la construction de l'environnement à dommage gradué, de l'ordre de 2 à 4 semaines-personne.

**Ordre d'exécution.** C0 et S1 d'abord. Si aucun saboteur n'atteint un dommage non nul sans détection mécanique, C1 à C4 sont sans objet ; on le rapporte comme résultat.

---

## 7. Ce qui me ferait changer d'avis

- **Une publication** rapportant le rapport dommage/preuve contre une référence R (C1), le contrôle H-sec sur un saboteur distillé (C2), une garantie de fausse alerte valide à tout instant sur tâches nouvelles pour la surveillance d'agents (C3), ou un audit fondé sur la différence d'effet distinct de Ctrl-Z (C4). La contribution correspondante serait alors déjà publiée, et je la retirerais.
- **Une lecture de Wen et al. (2024)** montrant que leur macro-protocole possède déjà une garantie fréquentiste et une référence de dégradation aléatoire : C1 et C3 se réduiraient à une réplication.
- **L'échec de S1** : si les saboteurs ouverts modestes ne produisent pas de sabotage diffus, l'ensemble se réduit à des questions sur des modèles plus grands, hors du périmètre « taille modeste ».
- **Le succès de C0** : si les vérifications mécaniques battent tous les moniteurs, la question sur les moniteurs devient secondaire, et la contribution principale est ce résultat négatif.
- **Une démonstration que l'appariement à un même état initial est irréalisable** en pratique, à cause d'un environnement non déterministe ou d'outils externes : C3 et C4 perdraient leur contrôle principal.

FIN-DE-CELLULE