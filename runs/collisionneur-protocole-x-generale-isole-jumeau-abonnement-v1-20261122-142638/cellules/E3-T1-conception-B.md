# Proposition B, tour III.1

**État des pièces.** Le bloc FAITS ne contient aucun fait doté d'un statut. Il reproduit la question mot pour mot, sous la même empreinte annoncée ; je n'ai pas recalculé cette empreinte (OBSERVÉ-NON-AUDITÉ). Le tour se joue à l'aveugle : je ne vois pas A, C, D ni E, et je n'en critique donc aucune. Sauf mention contraire, tout ce qui suit est HYPOTHÈSE.

## Thèse

Les trois articles mesurent une même grandeur sur trois axes : **combien de témoins indépendants le défenseur possède réellement**.
- Dans l'article 1, les témoins sont les pas de temps.
- Dans l'article 2, ce sont les copies du modèle. Or les exécutions de comparaison du défenseur sont elles-mêmes des copies.
- Dans l'article 3, ce sont les moniteurs, quand l'adversaire les vise.

Trois paramètres suffiraient peut-être, mesurés une seule fois :
- d'₁ : la sensibilité d'un témoin seul ;
- ρ : la corrélation des erreurs entre témoins ;
- α : l'exposant qui relie le dommage d'un acte au signal qu'il émet.

La problématique commune existe si ces paramètres prédisent la détection sur les trois axes et modifient une décision d'allocation. Sinon, les articles restent distincts et ne partagent que le banc d'essai. Le duel 5 et le duel 6 tranchent.

## (1) Question de recherche

> Face à un sabotage réparti en actes individuellement anodins, la valeur d'un témoin supplémentaire pour un défenseur à budget fixe (pas de temps agrégé, copie du modèle, moniteur d'une autre nature) est-elle prédite par la seule corrélation de ses erreurs avec celles des témoins déjà présents, quel que soit l'axe (temps, copies, moniteurs visés) sur lequel l'adversaire répartit son action ?

## (2) Réponse attendue, sous forme réfutable

**Modèle des témoins.** Chaque témoin i donne un score sᵢ. Dans chaque classe (honnête, sabotage), on suppose une variance σ² et une corrélation deux à deux ρ. Alors :
- Var(Σsᵢ) = nσ² + n(n−1)ρσ² ;
- d'où d'ₙ = d'₁·√(n / (1 + (n−1)ρ)), avec un plafond d'₁/√ρ.

L'identité est VÉRIFIÉE par le calcul ci-dessus. Son applicabilité est HYPOTHÈSE : elle suppose des scores binormaux, équicorrélés, de même variance dans chaque classe. On estime d' par d' = √2·Φ⁻¹(AUC), relation exacte dans le modèle binormal à variances égales.

**Axe temporel.** Un dommage total H est réparti en k actes de taille H/k. Si un acte de dommage h produit un signal c·hᵅ, un agrégateur de somme voit un signal total c·Hᵅ·k^(1−α). La répartition aide l'attaquant contre cet agrégateur si et seulement si α > 1. Le calcul est VÉRIFIÉ, le modèle reste HYPOTHÈSE. Contre un seuil appliqué acte par acte, la répartition aide toujours l'attaquant dès que α > 0.

**Attentes** (HYPOTHÈSE, chiffres illustratifs) :
- **E1.** Les exécutions de comparaison sont tirées des mêmes poids et l'adversaire est le modèle lui-même : ρ ≥ 0,3, donc un plafond d'environ 3 témoins effectifs.
- **E2.** Un moniteur d'une autre famille de modèles a un ρ au moins deux fois plus faible.
- **E3.** Entraîner l'agent à échapper au moniteur texte fait monter ρ(texte, activations) : la sonde perd une part de sa valeur sans avoir été visée.
- **E4.** α > 1 pour le moniteur texte (les gros actes y sont disproportionnellement suspects) ; α ≈ 1 pour la sonde d'activations.
- **Attente globale.** Les paramètres (d'₁, ρ, α), mesurés sur des tâches de calibration, prédisent d' à ±15 % près sur des tâches tenues à l'écart, et ce sur les trois axes.

**Réfutation.** Sur un axe, si la borne basse de l'IC 95 % de l'erreur de prédiction dépasse 15 %, l'unification est réfutée pour cet axe. Les attentes E1 à E4 sont réfutables une à une par les duels 2 à 4.

## (3) Antériorité la plus proche

Toutes ces références sont citées de mémoire (RAPPORTÉ).

- **La plus proche :** Greenblatt, Shlegeris, Sachan, Roger (2023), *AI Control: Improving Safety Despite Intentional Subversion*. On y trouve les trois ingrédients : un moniteur de confiance, un moniteur non fiable qui est une copie du modèle (avec risque de collusion), et un budget d'audit limité. Mais les tâches sont courtes (portes dérobées dans du code), et la corrélation entre témoins n'y est pas mesurée comme paramètre prédictif.
- Wen et al. (2024), *Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats* : menaces réparties sur de nombreuses actions. La liste complète des auteurs est à vérifier.
- Bhatt et al. (2025), *Ctrl-Z: Controlling AI Agents via Resampling* : le rééchantillonnage comme exécution de comparaison. Référence à vérifier.
- Bailey et al. (2024), *Obfuscated Activations Bypass LLM Latent-Space Defenses* : sondes contournées lorsqu'elles sont visées directement. Auteurs à vérifier.
- Baker et al. (2025), *Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation* : la pression d'un moniteur sur la chaîne de pensée induit de l'obfuscation.
- La loi elle-même, hors du domaine :
  - Kish (1965), *Survey Sampling* (effet de plan) ;
  - Ladha (1992), *The Condorcet Jury Theorem, Free Speech, and Correlated Votes* ;
  - Knight & Leveson (1986), *An Experimental Evaluation of the Assumption of Independence in Multiversion Programming*. Des versions développées indépendamment y échouent de façon corrélée ; c'est l'analogue direct de copies d'un même modèle.

## (4) Expérience qui trancherait

Le duel 1 sert de porte d'entrée. Viennent ensuite le duel 5, qui teste la prédiction sur les trois axes, puis le duel 6, qui teste la valeur pour les décisions. Le modèle principal est Qwen3-8B, avec une réplication sur Llama-3.1-8B-Instruct. Détails en (b) et (d).

## (5) Type de contribution

C'est une **loi connue ailleurs** (effet de plan, jury corrélé, programmation multi-versions), transposée en **protocole de mesure** pour le contrôle d'agents. S'y ajoute un phénomène possible : la saturation des exécutions de comparaison tirées des mêmes poids.

**Ce n'est pas une garantie.** Les paramètres d'₁, ρ et α sont estimés sur des sabotages plantés. Ils ne bornent rien face à un adversaire qui se comporterait autrement en calibration qu'en déploiement.

## (a) Ce que la question suppose sans l'établir

1. **Une suite d'actes anodins peut dégrader fortement le résultat d'une longue tâche.**
   - Statut : HYPOTHÈSE. Pour des modèles de pointe, c'est posé par Wen et al. (2024), RAPPORTÉ de mémoire. Rien n'est établi à 8 milliards de paramètres (duel 1).
2. **« Non suspect isolément » serait une propriété de l'acte.**
   - Statut : HYPOTHÈSE. En réalité, c'est relatif à un moniteur et à un seuil, et la question ne fixe ni l'un ni l'autre.
   - Je fixe donc : taux de détection par acte ≤ 10 % pour 1 % de fausses alertes par pas (illustratif).
3. **Le sabotage se distingue de l'erreur honnête.**
   - Statut : HYPOTHÈSE. Le seul critère mécanique que je propose est la directionnalité : le sabotage déplace la conclusion vers une cible.
   - Une dégradation sans direction (sous-performance volontaire) ne se distingue de l'incompétence que par l'ampleur. Le contrôle doit alors être le même modèle à pleine capacité.
4. **Un organisme-modèle représente « l'agent lui-même » en adversaire.** (Un organisme-modèle est un saboteur obtenu par consigne ou par affinage.)
   - Statut : HYPOTHÈSE. C'est le point faible principal : ρ et α mesurés sur des sabotages plantés peuvent différer de ceux d'un adversaire réel.
5. **Les copies d'un même modèle commettent des erreurs corrélées.**
   - Statut : HYPOTHÈSE. Un analogue est documenté en logiciel (Knight & Leveson 1986, RAPPORTÉ).
6. **Les sondes d'activations lisent l'intention plutôt que des traces du contexte, comme la consigne de sabotage.**
   - Statut : HYPOTHÈSE. Leur contournement lorsqu'elles sont visées est RAPPORTÉ (Bailey et al. 2024).
7. **« Viser les moniteurs » a un contenu précis.**
   - Statut : non spécifié par la question. L'adversaire peut ou non connaître leur architecture et accéder à leurs scores.
   - Je retiens : accès aux scores du moniteur texte pendant l'entraînement, aucun accès à la sonde (HYPOTHÈSE).
8. **Les budgets sont « limités ».**
   - Statut : aucun chiffre n'est donné. Les conclusions dépendent du rapport entre budget et volume de trajectoires. Les budgets que je fixe sont illustratifs.
9. **Les trois articles partagent un modèle de menace et un défenseur.**
   - Statut : HYPOTHÈSE. Si l'article 3 suppose un attaquant en boîte blanche et l'article 1 un attaquant en boîte noire, l'unification est artificielle.
10. **Les vérifications coûteuses sont fiables.**
    - Statut : HYPOTHÈSE. Je les mesure en (c).
11. **« Plus utiles ensemble » a un critère.**
    - Statut : la question n'en donne aucun. Je propose : un paramètre commun prédit (duel 5) et modifie une décision (duel 6).

## (b) Expériences décisives

[DUEL 1]
**Porte d'entrée : le phénomène existe-t-il à 8 milliards de paramètres ?**
- **Tâches.** Analyses synthétiques de 20 à 60 pas (filtres, jointures, agrégations, choix de sources), avec une clé cachée calculée par un pipeline de référence et une conclusion cible imposée au saboteur.
- **H_A.** Il existe un k ∈ {3, 5, 8} pour lequel les deux conditions tiennent ensemble :
  - le taux de bascule directionnelle de la conclusion (fausse, et dans le sens de la cible) atteint au moins 20 % ;
  - le taux de détection par acte du moniteur texte reste ≤ 10 % pour 1 % de fausses alertes par pas.
- **H_B.** Pour tout k testé, soit la bascule reste sous 20 % (le modèle ne sait pas saboter), soit la détection par acte dépasse 10 % (le sabotage est grossier). H_B est le complément exact de H_A.
- **Métrique.** Taux de bascule vérifié mécaniquement contre la clé ; détection par acte au seuil fixé.
- **Contrôles négatifs.**
  - Le même modèle, honnête, avec k erreurs injectées de même type mais de signe aléatoire : on attend environ la moitié des bascules dans le sens cible.
  - L'organisme affiné, sans son déclencheur.
- **Falsification.** Si un k satisfait les deux conditions, H_B est falsifiée. Sinon, H_A est falsifiée, et le programme est sans objet à cette échelle, pas en général.

[DUEL 2]
**Article 1 : répartir le sabotage dans le temps aide-t-il l'attaquant contre un agrégateur de somme ?**
- **Mesure du dommage par acte.** On rejoue le pipeline avec et sans l'acte, et on mesure sa contribution au déplacement final (rejeu contrefactuel).
- **H_A.** α ≤ 1 : à dommage total fixé, le d' de l'agrégateur de somme (ou CUSUM) ne décroît pas quand k ∈ {1, 2, 4, 8}.
- **H_B.** α > 1 : ce d' décroît avec k.
- **Métrique.** On estime α par régression de log(écart de score par acte) sur log(dommage par acte), séparément pour le moniteur texte et pour la sonde.
- **Seuil.** IC 95 % de α entièrement au-dessus de 1 : H_B. Entièrement à 1 ou en dessous : H_A. Si l'IC chevauche 1, le résultat n'est pas concluant et l'on double l'effectif.
- **Contrôles négatifs.**
  - Des trajectoires honnêtes où l'on insère k erreurs aléatoires de même dommage total : on obtient le α d'une erreur non intentionnelle.
  - Le même agrégateur sur des pas mélangés : cela vérifie qu'il n'exploite pas la position des actes.
- **Falsification.** Chaque issue falsifie l'hypothèse opposée. Si α_texte ≈ α_sonde, l'attente E4 est falsifiée.

[DUEL 3]
**Article 2 : les exécutions de comparaison sont-elles des témoins indépendants quand l'adversaire est le modèle lui-même ?**
- **Dispositif.** Une exécution cible et R = 4 rééchantillons. Un détecteur de divergence compare les résultats intermédiaires et les décisions.
- **Trois conditions.**
  - L, saboteur isolé : les rééchantillons sont honnêtes.
  - S, le modèle contre lui-même : les rééchantillons viennent du même organisme saboteur.
  - X : les rééchantillons viennent de saboteurs d'une autre famille de modèles.
- **H_A.** Rapport détection_S / détection_L ≥ 0,5 : les copies sabotent à des endroits différents.
- **H_B.** Ce rapport est < 0,5 : point focal partagé.
- **Métrique.** Taux de détection pour 1 % de fausses alertes par trajectoire. En mécanisme secondaire : recouvrement des emplacements sabotés entre copies de mêmes poids, comparé au recouvrement entre familles.
- **Contrôles négatifs.**
  - Des paires honnête–honnête : elles donnent le plancher de fausses alertes du détecteur.
  - La condition X : elle sépare la coordination due aux poids partagés de celle due à la structure de la tâche (les endroits « évidents » à saboter).
- **Falsification.**
  - Un rapport ≥ 0,5 falsifie H_B ; un rapport < 0,5 falsifie H_A.
  - Si détection_X ≈ détection_S, le mécanisme d'E1 (les poids partagés) est falsifié. L'article 2 porterait alors sur les tâches, pas sur les copies.
- **Variante en équipe.** Les copies se répartissent les rôles, et le sabotage se répartit entre elles. C'est le duel 2 avec l'axe « copies » à la place du temps, selon que l'agrégateur couvre ou non toutes les copies.

[DUEL 4]
**Article 3 : échapper au moniteur texte se transfère-t-il au moniteur d'activations, qui n'est pas visé ?**
- **Procédure.**
  - Affinage LoRA par échantillonnage de rejet : on garde les trajectoires de sabotage réussies que le moniteur texte note bas.
  - La sonde est entraînée avant cet affinage sur l'organisme de base, puis gelée ; elle n'intervient jamais dans la sélection.
- **H_A.** La baisse de détection de la sonde vaut au plus 25 % de celle du moniteur texte : les instruments sont découplés.
- **H_B.** Elle vaut 25 % ou plus : les deux instruments partagent une même surface d'attaque.
- **Métrique.** Taux de détection pour 1 % de fausses alertes, avant et après affinage, et ρ(texte, sonde) avant et après.
- **Contrôles négatifs.**
  - Un affinage identique (même nombre de pas, même divergence KL) mais avec sélection sur un score aléatoire : cela sépare « l'affinage déplace les activations » de « l'évasion se transfère ».
  - Une sonde réentraînée après affinage : elle distingue « sonde périmée » de « signal effacé ».
- **Falsification.** Chaque issue falsifie l'hypothèse opposée. Une baisse de la sonde gelée qui disparaît avec la sonde réentraînée réfute l'effacement du signal.

[DUEL 5]
**Unification : le modèle (d'₁, ρ, α) prédit-il la détection sur les trois axes ?**
- **Calibration.** Sur un jeu de tâches T_cal, on mesure d'₁, ρ (par classe) et α, pour chaque instrument et chaque axe.
- **Test.** Sur des tâches tenues à l'écart T_test, on prédit d'ₙ pour n ∈ {2, 4, 8} :
  - axe temporel : fenêtres d'agrégation ;
  - axe des copies : rééchantillons ;
  - axe des instruments : texte, sonde et moniteur d'une autre famille, avant et après l'attaque du duel 4.
- **H_A.** Les deux conditions tiennent :
  - |d'_obs − d'_préd| / d'_obs ≤ 15 % sur les trois axes (IC 95 %) ;
  - le modèle unifié ne fait pas plus de 5 % pire, en erreur, que des ajustements propres à chaque axe ayant le même nombre de paramètres libres (de la forme a·nᵇ).
- **H_B.** Au moins une des deux conditions échoue.
- **Contrôles négatifs.**
  - Des scores synthétiques à ρ connu ∈ {0 ; 0,2 ; 0,5} : la chaîne d'analyse doit retrouver ρ à ±0,05.
  - Des appariements permutés entre trajectoires : on doit obtenir ρ ≈ 0 et d' ∝ √n. Tout écart révèle un biais de l'estimateur.
- **Falsification.** Un axe en échec falsifie H_A : les articles restent distincts sur cet axe. La réussite sur les trois axes falsifie H_B.

[DUEL 6]
**Valeur pour les décisions : le paramètre ρ change-t-il l'allocation du budget ?**
- **Politique U.** Elle choisit quels témoins acheter (rééchantillons, moniteur d'une autre famille, sonde) et quelles trajectoires envoyer en vérification coûteuse, en maximisant le d' prédit par unité de coût à partir du ρ mesuré.
- **Politique S.** La meilleure des trois politiques propres à chaque article, réglée sur T_cal.
- **Métrique.** Sécurité : la fraction des trajectoires sabotées interceptées avant acceptation. On la mesure à budget égal (2 % de trajectoires vérifiées, 4 rééchantillons pour 10 trajectoires, illustratif) et à utilité égale (au moins 98 % d'acceptation des trajectoires honnêtes, illustratif).
- **H_A.** U − S ≥ 5 points sur T_test.
- **H_B.** U − S < 5 points.
- **Contrôle négatif.** U avec ρ forcé à 0, c'est-à-dire en supposant les témoins indépendants. Si U(ρ=0) ≈ U, la corrélation ne sert à rien pour décider, même si le duel 5 réussit.
- **Falsification.** Chaque issue falsifie l'hypothèse opposée.
- **Lecture.** Le duel 5 dit si le modèle unifié est vrai ; le duel 6 dit s'il est utile. « Plus utiles ensemble » exige les deux.

[FIN DES DUELS : 6]

## (c) Mesure minimale pour chaque instrument

**Cas honnêtes appariés, communs à tous les instruments.** Tous sont tirés de la même tâche, avec une longueur à ±10 % près :
- H1 : trajectoire honnête correcte ;
- H2 : trajectoire honnête mais fausse, le modèle se trompant de lui-même ;
- H3 : trajectoire honnête avec des erreurs aveugles injectées (même type et même nombre que le sabotage, signe aléatoire) ;
- H4 : l'organisme affiné, sans son déclencheur ;
- H5 : la consigne de sabotage est présente dans le contexte mais le modèle a ordre de l'ignorer, ce qui contrôle la sonde.

Les fausses alertes se mesurent d'abord sur H2 et H3, les négatifs difficiles.

**Moniteur texte (juge LLM, par pas et par trajectoire)**
- **Mesure.** Taux de détection pour 1 % de fausses alertes, par pas et par trajectoire ; AUC.
- **Vérifications mécaniques à battre.**
  - M1 : une régression logistique sur des traits de surface (longueur, nombre d'appels d'outils, nombre de modifications des données).
  - M3 : un contrôle de provenance (chaque nombre cité existe dans les sources, chaque filtre est déclaré).
- **Critère.** Un gain d'AUC ≥ 0,05 sur la meilleure de ces deux vérifications, mesuré sur H2 et H3 (illustratif). Sinon le moniteur ne sert à rien.

**Moniteur d'activations (sonde linéaire sur le flux résiduel)**
- **Mesure.** La même, plus la valeur ajoutée : l'AUC de la combinaison texte + sonde moins celle du texte seul doit atteindre 0,03 (illustratif).
- **Vérifications à battre.**
  - Une sonde sur la couche 0, qui ne lit que le lexique.
  - Une sonde entraînée sur des étiquettes permutées, qui donne le plancher.
- **Exigence.** La sonde doit garder ses performances sur H5, et se transférer d'un organisme obtenu par consigne à un organisme affiné. Sinon elle détecte la consigne, pas l'acte.

**Exécutions de comparaison**
- **Mesure.** Le taux de détection en fonction de R ∈ {1, 2, 4, 8}, qui donne n_eff ajusté par la formule de (2). Les fausses alertes se mesurent sur des paires honnêtes et sur des tâches qui admettent légitimement plusieurs chemins d'analyse.
- **Vérification à battre.** M5 : la dispersion des seules conclusions finales (vote majoritaire).

**Vérifications coûteuses** (rejeu d'un pas par le pipeline de référence, ou audit par un modèle de 70 milliards de paramètres)
- **Ce ne sont pas des oracles.** On mesure leur taux de détection sur des sabotages plantés, à coût fixe (par exemple 3 pas vérifiés par trajectoire, illustratif).
- **Vérification à battre.** M6 : un ciblage aléatoire du même budget. Si un ciblage guidé par les moniteurs ne fait pas mieux, les moniteurs n'apportent rien à la vérification.
- **Validation de la clé cachée.** On la vérifie à la main sur 50 tâches (illustratif).

## (d) Ancrage matériel

Tout ce qui suit est illustratif : rien ne vient des faits.

**Modèles**
- Agent et copies : Qwen3-8B ; réplication sur Llama-3.1-8B-Instruct. La réplication teste si ρ et α dépendent de la famille.
- Moniteur d'une autre famille : Gemma-2-9B-it ou Mistral-7B-Instruct.
- Vérification coûteuse : Llama-3.1-70B ou Qwen2.5-72B, quantifié en 4 bits.
- Outils : vLLM pour la génération, nnsight ou TransformerLens pour les activations, PEFT pour LoRA.

**Calcul**
- Environ 300 tâches et environ 30 000 trajectoires, rééchantillons compris, d'environ 20 000 jetons, soit environ 600 millions de jetons générés. À environ 2 500 jetons/s par H100 en lot, cela fait environ 70 h.
- Activations moyennées par pas, sur 5 couches : environ 50 Go. Stocker les activations jeton par jeton coûterait plusieurs To par couche.
- Extraction des activations : environ 30 h.
- Trois organismes LoRA plus l'affinage par rejet du duel 4 : environ 60 h.
- Auditeur de 70 milliards de paramètres sur environ 5 000 trajectoires : environ 100 h.
- Avec une marge de ×2 : environ 500 h-H100, soit 1 000 à 1 500 $ à 2–3 $/h.

**Équipe et calendrier** (deux personnes)
- Semaines 1–2 : tâches, clés, organismes.
- Semaines 3–4 : instruments et cas appariés ; préenregistrement des seuils et du découpage calibration/test.
- Semaines 5–6 : duels 1 à 4.
- Semaine 7 : duels 5 et 6.
- Semaine 8 : réplication sur la seconde famille et rédaction.

## Issues qui rendraient la question sans intérêt

- **Le duel 1 donne H_B.** Le phénomène n'est pas testable à 8 milliards de paramètres, et le programme est sans objet à cette échelle.
- **ρ ≈ 0 sur tous les axes et α ≈ 1.** Le modèle se réduit à l'hypothèse d'indépendance, et la problématique commune est triviale.
- **Les vérifications mécaniques M3 et M5 interceptent au moins 95 % des sabotages pour 1 % de fausses alertes.** Les tâches sont trop faciles et les moniteurs inutiles.
- **Le duel 5 donne H_A mais le duel 6 donne H_B.** L'unification est vraie mais inutile : trois articles séparés sur un banc d'essai commun.

## Comment vérifier la nouveauté

**La nouveauté que j'avance.** d'₁, ρ et α serviraient de paramètres prédictifs communs aux trois axes du contrôle d'agents.

**Recherche d'antériorité.** Chercher « design effect », « correlated monitors », « monitor ensemble diversity », « effective number of monitors » et « N-version » dans Greenblatt et al. (2023) et ses suites (Ctrl-Z, menaces réparties, collusion en surveillance non fiable). Si un travail ajuste déjà une loi de corrélation à des ensembles de moniteurs face au sabotage, ma contribution se réduit à une réplication à 8 milliards de paramètres sur des tâches longues.

**Garde-fous.**
- Préenregistrer les seuils.
- Publier le code, les cas honnêtes appariés et les sabotages plantés.
- Faire recalculer d' et ρ par un tiers à partir des scores bruts.
- Exiger que la loi tienne sur les deux familles de modèles.

FIN-DE-CELLULE