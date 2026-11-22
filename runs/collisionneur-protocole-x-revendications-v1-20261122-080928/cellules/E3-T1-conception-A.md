# Proposition A, tour III.1 : conception ciblée

**État des pièces.** Le bloc FAITS reproduit la question et ne contient aucun fait porteur de statut. Aucune autre proposition ne m'est transmise, donc B1 est sans objet à ce tour. Je ne peux pas recalculer l'empreinte sha256.

**Réponse courte.** Je propose trois contributions candidates. Leur caractère inédit est une HYPOTHÈSE dans les trois cas, et rien dans cette cellule n'est VÉRIFIÉ. Si la recherche bibliographique décrite plus bas trouve un antécédent pour chacune, la bonne réponse est zéro.

Statuts employés ici :
- **HYPOTHÈSE** : mes conjectures.
- **RAPPORTÉ (de mémoire, non vérifié)** : mes souvenirs de la littérature.

Tous les seuils chiffrés sont **illustratifs** et à figer par préenregistrement avant toute donnée.

---

## (a) Ce que la question suppose sans l'établir

| # | Présupposé | Statut | Conséquence s'il est faux |
|---|---|---|---|
| P1 | Un sabotage diffus existe : dommage final net alors que chaque action reste sous le seuil de détection par action. | HYPOTHÈSE | Sur modèles modestes, il faut un sabotage scripté, et la portée des résultats se réduit (duel 0). |
| P2 | « Le dommage s'accumule » veut dire qu'il est attribuable action par action (additif). | HYPOTHÈSE, non dit par la question | Si le dommage naît d'interactions entre actions, l'audit d'unités isolées ne mesure rien (duel 2). |
| P3 | L'audit reconnaît une unité sabotée quand il la tire. | HYPOTHÈSE | Elle est en tension avec « chaque action paraît honnête » si l'unité est l'action : le taux de conviction de l'audit devient une inconnue à mesurer. |
| P4 | Les exécutions de référence sont honnêtes et de même distribution que le déploiement. | HYPOTHÈSE | L'étalonnage des fausses alertes est biaisé. |
| P5 | Le moniteur d'activations lit autre chose que ce que lit le moniteur de texte. | HYPOTHÈSE | L'instrument est redondant (duel 1). |
| P6 | L'erreur honnête se distingue du sabotage à dommage égal. | HYPOTHÈSE | Un agent modeste se trompe souvent : le sabotage diffus peut se loger dans la variance honnête. |
| P7 | L'adversaire contrôle la politique de l'agent, mais ni le tirage de l'audit ni les moniteurs ; sa connaissance du protocole n'est pas précisée. | HYPOTHÈSE | Les conclusions dépendent du modèle de menace retenu. |
| P8 | « Inédit » est décidable. | HYPOTHÈSE | Ma connaissance de la littérature est datée et non vérifiée : seule une recherche tracée par un tiers peut trancher. |

---

## (b) Contributions candidates et expériences décisives

### Banc commun

**Tâches.** Chaînes de traitement de données ou de code, au moins 30 actions (illustratif), environnement déterministe, score final continu et mécanique (tests cachés, écart à une sortie de référence).

**Bras saboteurs.**
- **S-invite** : sabotage diffus demandé par l'invite.
- **S-LoRA** : agent affiné pour saboter sans mention dans l'invite.
- **S-script** : perturbations injectées mécaniquement dans des trajectoires honnêtes, puis relues en lecture forcée par le modèle honnête. C'est le contenu saboté sans intention.

**Bras honnêtes appariés.**
- **H** : même tâche, même graine, même préfixe jusqu'à la bifurcation.
- **H-leurre** : agent honnête dont l'invite mentionne le sabotage en l'interdisant.
- **H-faible** : agent honnête handicapé (modèle plus petit ou température élevée), apparié en dommage final aux bras saboteurs.

**Dommage par action.** Δ_i est le gain de score final quand on remplace la seule action i par l'action honnête appariée et qu'on rejoue mécaniquement le reste.

### Duel 0 : la précondition (P1)

- **H_A.** Un agent modeste produit un sabotage diffus : AUROC par action du moniteur de texte ≤ 0,60 et dommage final ≥ 2 écarts-types de la variance honnête entre graines (illustratif).
- **H_B.** À cette échelle, le sabotage est soit visible action par action, soit noyé dans le bruit honnête.
- **Contrôle négatif.** H contre H avec graines différentes : le « dommage » mesuré doit rester dans le bruit.
- **Si H_A est falsifiée.** La question n'est pas instanciable avec des saboteurs modestes ; seul S-script reste, et toute conclusion sur l'intention est hors de portée.
- **Si H_B est falsifiée.** L'argument « trop petit pour saboter finement » tombe et les duels 1 à 3 sont recevables.

### Candidate C1 : la courbe soupçon–dommage sépare les deux familles de moniteurs

**Énoncé falsifiable.** Sur les actions sabotées, le décalage du score d'une sonde d'activations ne dépend pas du dommage Δ_i de l'action (signature d'intention). Celui d'un moniteur de texte lui est proportionnel et s'annule quand Δ_i tend vers 0 (signature de contenu). La dilution du dommage n'affaiblirait donc que le moniteur de texte.

**Travaux les plus proches (RAPPORTÉ, de mémoire, non vérifié).**
- Goldowsky-Dill, Chughtai, Heimersheim, Hobbhahn, *Detecting Strategic Deception Using Linear Probes*, 2025.
- Wen et al., *Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats*, 2024.
- Bailey et al., *Obfuscated Activations Bypass LLM Latent-Space Defenses*, 2024.

**Ce qui la distingue (HYPOTHÈSE).** Ces travaux donnent, à ma connaissance, des taux de détection globaux par scénario. Ils ne donnent pas de relation dose–réponse entre le dommage attribué à une action et le score du moniteur, ni de comparaison de sa forme entre texte et activations. Or cette forme décide si la dilution est la stratégie optimale de l'adversaire.

**Vérification de l'inédit par un tiers.**
1. Chercher sur arXiv, OpenReview et Alignment Forum les combinaisons de *probe*, *sabotage* ou *sandbagging*, *dose-response*, *magnitude*, *per-step*, *diffuse* ou *distributed*.
2. Suivre les citations descendantes des trois références.
3. Faire lire par deux personnes indépendantes.
4. Critère d'antériorité : un article qui mesure le score du moniteur en fonction d'un dommage par action, pour les deux familles.
5. Publier le journal des requêtes.

**Duel 1.**
- **H_A (intention).** Ordonnée à l'origine du décalage de sonde ≥ 0,5 écart-type dans le quintile de dommage le plus bas, et rapport quintile haut / quintile bas ≤ 1,5 (illustratif).
- **H_B (contenu).** L'intervalle de confiance du quintile bas contient 0 et le rapport est ≥ 3 (illustratif), comme pour le moniteur de texte.
- **Métrique.** Régression du décalage standardisé (action sabotée moins action honnête appariée) sur Δ_i, mesurée sur S-LoRA.
- **Contrôles négatifs.**
  - S-script : sous H_A la sonde doit y rester muette. Si elle s'y allume autant, elle lit le contenu.
  - H-leurre : la sonde ne doit pas s'allumer sur la seule mention du sabotage.
  - Étiquettes permutées.
- **Si H_A est falsifiée.** C1 tombe, et avec elle l'idée d'un apport propre des activations en régime diffus.
- **Si H_B est falsifiée.** L'idée que la dilution affaiblit tous les moniteurs de la même façon tombe ; la stratégie diffuse n'est plus dominante contre un défenseur qui lit les activations.
- **Zone intermédiaire.** Les deux formes fortes sont rejetées, et je le rapporterais ainsi.

### Candidate C2 : la validité de l'audit aléatoire dépend de l'additivité du dommage, pas du taux d'audit

**Énoncé falsifiable.** Contre un adversaire qui cherche à l'abaisser, le rapport d'additivité R = Σ_i Δ_i / Δ_total descend sous 0,5 (illustratif). Dans ce régime, aucun taux d'audit d'actions isolées, même 100 %, ne borne le dommage cumulé. Seul un audit d'unités plus larges, ou comparé à un contrefactuel honnête, le peut.

**Travaux les plus proches (RAPPORTÉ, de mémoire, non vérifié).**
- Greenblatt, Shlegeris, Sachan, Roger, *AI Control: Improving Safety Despite Intentional Subversion*, 2023.
- Griffin, Thomson, Shlegeris, Abate, *Games for AI Control*, 2024.
- Avenhaus et Canty, *Compliance Quantified*, 1996, pour les jeux d'inspection.

**Ce qui la distingue (HYPOTHÈSE).** Ces cadres supposent, de mémoire, qu'une unité fautive auditée est reconnue. Ici, la capacité de conviction de l'audit devient une quantité mesurée, fonction de la taille de l'unité et de la structure d'interaction du dommage. Le problème passe de « attraper une attaque » à « borner un total ».

**Vérification de l'inédit par un tiers.**
1. Chercher *imperfect auditing*, *audit unit*, *low-stakes*, *diffuse failures*, *interaction* ou *non-additive sabotage*.
2. Lire les sections « hypothèses » des articles de contrôle postérieurs à 2023.
3. Critère d'antériorité : un modèle ou une mesure où la probabilité de conviction dépend de l'unité auditée en régime cumulatif.

**Duel 2.**
- **H_A (additif).** R ≥ 0,8 (illustratif) : l'audit local avec contrefactuel mesure le dommage.
- **H_B (interactif).** R ≤ 0,5 (illustratif) malgré un dommage total net.
- **Métrique.** R avec intervalle par bootstrap sur les tâches. L'équipe rouge est explicitement chargée de minimiser R.
- **Contrôle négatif.** Paires H contre H : la distribution des Δ_i donne le plancher de bruit.
- **Contrôle positif.** S-script, construit additif, doit donner R ≈ 1 ; sinon la mesure est défectueuse.
- **Si H_A est falsifiée.** L'estimation du dommage total par sondage d'actions isolées est invalide quel que soit le taux, et l'unité d'audit devient la variable de conception.
- **Si H_B est falsifiée.** C2 tombe : le problème se ramène à un sondage classique avec variable auxiliaire, donc à de la statistique connue. L'idée que l'audit est aveugle au diffus tombe aussi.

### Candidate C3 : un petit nombre d'exécutions honnêtes sert mieux en contrefactuel apparié qu'en réservoir d'étalonnage

**Énoncé falsifiable.** À budget égal de k exécutions honnêtes, les employer comme bifurcations appariées aux points tirés par l'audit donne un meilleur taux de détection par trajectoire, à fausses alertes fixées, que de les employer à étalonner les seuils des moniteurs.

**Travaux les plus proches (RAPPORTÉ, de mémoire, non vérifié).**
- Bhatt et al., *Ctrl-Z: Controlling AI Agents via Resampling*, 2025.
- Greenblatt et al., 2023, déjà cité.

**Ce qui la distingue (HYPOTHÈSE).** Le rééchantillonnage publié se fait, de mémoire, à partir du modèle non fiable. La référence fiable y est un modèle plus faible, disponible sans limite. Ici, la ressource rare est l'exécution honnête de même capacité, et la question est celle de son allocation.

**Vérification de l'inédit par un tiers.**
1. Chercher *honest baseline budget*, *paired counterfactual*, *reference runs*, *calibration set size* dans la littérature de contrôle et de détection d'anomalies sur trajectoires.
2. Critère d'antériorité : une comparaison des deux usages à budget égal.

**Duel 3.**
- **H_A.** L'usage apparié l'emporte d'au moins 10 points de détection à 1 % de fausses alertes par trajectoire (illustratif).
- **H_B.** L'usage en étalonnage l'emporte du même écart.
- **Contrôle négatif.** Bifurcations H contre H : la statistique appariée doit respecter le taux de fausses alertes annoncé.
- **Si H_A est falsifiée.** C3 tombe : la divergence honnête entre réexécutions masque le dommage diffus, et le sabotage se cache dans la variance honnête.
- **Si H_B est falsifiée.** L'étalonnage sur réservoir honnête n'est pas le meilleur emploi de références rares.
- **Écart sous le seuil.** Je conclurais à l'équivalence, et C3 serait abandonnée.

---

## (c) Mesure minimale par instrument

Les règles sont communes aux quatre instruments :
- les taux sont rapportés par action et par trajectoire ;
- le taux de fausses alertes est mesuré séparément sur H, H-leurre et H-faible ;
- les intervalles de confiance sont calculés par tâche, pas par action.

**1. Audit aléatoire.**
- **Mesure.** Probabilité de conviction sachant que l'unité est sabotée, et fausses convictions sur unités honnêtes, pour trois tailles d'unité (action, segment, trajectoire), avec et sans contrefactuel honnête.
- **Cas appariés.** Même tâche, même préfixe, bras H et H-faible.
- **Vérifications mécaniques à battre.** Le score final seul (tests cachés) ; la taille du différentiel avec la référence honnête.
- **Verdict.** Si l'auditeur, humain ou modèle fiable, ne fait pas mieux que le différentiel brut, il n'ajoute rien.

**2. Moniteur de texte.**
- **Mesure.** Détection à 1 % de fausses alertes (illustratif) par action, puis par trajectoire après agrégation (somme, maximum, somme cumulée de type CUSUM).
- **Cas appariés.** H, et surtout H-faible : à dommage égal, le moniteur distingue-t-il sabotage et maladresse ?
- **Vérifications mécaniques à battre.**
  - expressions régulières et mots-clés ;
  - perplexité des actions sous un petit modèle fiable ;
  - longueur, nombre d'erreurs d'outil ;
  - régression logistique sur sac de mots.

**3. Moniteur d'activations.**
- **Mesure.** Les mêmes taux, avec entraînement sur S-invite et test sur S-LoRA, S-script et H-leurre.
- **Vérifications mécaniques à battre.**
  - la même sonde sur les activations d'un modèle lecteur tiers recevant le même texte : si elle fait aussi bien, l'accès interne à l'agent n'apporte rien ;
  - sac de mots sur le même texte ;
  - direction aléatoire, étiquettes permutées.
- **Verdict.** Une alerte sur H-leurre supérieure au taux nominal classe la sonde comme détecteur d'invite.

**4. Exécutions honnêtes de référence.**
- **Mesure.**
  - erreur d'étalonnage, c'est-à-dire l'écart entre fausses alertes visées et réalisées sur des tâches nouvelles, en fonction de k ;
  - autocorrélation des scores honnêtes au sein d'une trajectoire, qui fixe le nombre effectif d'observations indépendantes pour toute agrégation ;
  - variance du score final entre graines.
- **Vérification mécanique à battre.** Un seuil fixé sans aucune référence, par exemple un quantile sur les trajectoires de déploiement elles-mêmes.
- **Remarque arithmétique.** Estimer un seuil à un taux de fausses alertes α demande nettement plus de 1/α unités honnêtes indépendantes. C'est une déduction, pas un résultat.

---

## (d) Ancrage matériel

Tout ce qui suit est **illustratif**.

- **Agent.** Un modèle ouvert de 7 à 9 milliards de paramètres, par exemple de la famille Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct ou Gemma-2-9b.
- **Moniteur fiable et H-faible.** Un modèle de 1 à 3 milliards de paramètres.
- **S-LoRA.** Adaptateur de rang faible, quelques heures sur un seul processeur graphique.
- **Volume.**
  - environ 150 tâches de 30 à 40 actions sur six bras ;
  - dommage par action par réversion sur un sous-ensemble d'environ 50 trajectoires par bras saboteur, le rejeu étant mécanique et sans génération ;
  - activations résiduelles sur trois couches, agrégées par action.
- **Calcul.** De l'ordre de 100 à 300 heures sur un processeur graphique de 24 à 48 Go, soit quelques centaines à environ deux mille euros en location.
- **Audit humain.** Une centaine d'unités, une dizaine d'heures.
- **Risque matériel principal.** Le duel 0 peut conclure H_B, auquel cas les agents modestes ne fournissent que le bras scripté.

---

## (e) Déjà publié, encore ouvert, et ce qui me ferait changer d'avis

### D'apparence nouvelle, mais déjà publié (RAPPORTÉ, de mémoire, non vérifié)

- **La distinction entre défaillances concentrées et diffuses, et l'idée que le diffus permet d'accumuler des preuves.** Wen et al., 2024, et des billets de Greenblatt et Roger vers 2023 (référence à vérifier).
- **L'agrégation du soupçon au fil des actions et l'ajustement adaptatif de la confiance.** Wen et al., 2024 ; Bhatt et al., 2025.
- **Le budget d'audit limité et sa formulation en jeu.** Greenblatt et al., 2023 ; Griffin et al., 2024.
- **Les sondes linéaires contre la tromperie, et leur contournement.** Goldowsky-Dill et al., 2025 ; Bailey et al., 2024.
- **Les bancs agentiques avec tâche annexe malveillante et moniteurs.** Kutasov et al., *SHADE-Arena*, 2025 ; Benton et al., *Sabotage Evaluations for Frontier Models*, 2024.
- **Les mathématiques sous-jacentes.** Tests séquentiels (Wald, années 1940 ; Page, 1954), et détection de signaux faibles et rares (Donoho et Jin, *Higher criticism for detecting sparse heterogeneous mixtures*, 2004). « Agréger des signaux faibles » n'est donc pas inédit en soi.

### D'apparence traitée, mais ouvert (HYPOTHÈSE)

- **La fiabilité de l'audit en régime diffus.** L'audit est souvent supposé parfait, alors que la conviction sur une action d'apparence honnête n'est pas mesurée.
- **Un dommage continu attribué par action.** Les bancs que je connais rapportent un succès binaire de la tâche annexe.
- **La séparation du sabotage et de la maladresse à dommage égal** (bras H-faible).
- **Ce que lisent les sondes.** Elles sont validées sur des scénarios induits par l'invite ; la confusion avec l'invite et le transfert vers un saboteur affiné, à faible amplitude, restent à établir.
- **L'étalonnage des fausses alertes** avec peu de références honnêtes et des tâches non stationnaires.

### Ce qui me ferait changer d'avis

- **Un article antérieur satisfaisant un critère d'antériorité ci-dessus.** La candidate concernée est retirée, sans reformulation de sauvetage.
- **Duel 0 concluant H_B.** Je restreins toutes les affirmations au sabotage scripté.
- **Duel 1 concluant H_B avec un contrôle S-script propre.** J'abandonne l'idée d'un rôle propre des activations en régime diffus.
- **Duel 2 concluant H_A contre une équipe rouge compétente.** C2 se réduit à une application de la théorie des sondages et je ne la présente plus comme contribution.
- **Une équipe rouge trop faible** (R élevé faute d'effort adverse, constaté par un tiers). Le duel 2 est alors non concluant, pas favorable.

FIN-DE-CELLULE