## Réponse 10

La question porte sur l'existence d'une problématique d'ensemble rendant les trois articles (agent seul sur longue tâche, copies multiples d'un même modèle, moniteurs ciblés par l'adversaire) plus utiles ensemble que séparément.

**(1) Meilleure question de recherche :** Existe-t-il une frontière de détection commune aux trois configurations (agent seul, copies multiples, moniteur ciblé) qui se dégrade de façon prévisible selon une loi unique liant la longueur de la tâche, le nombre d'agents et la part du travail vérifiable ?

**(2) Réponse attendue (réfutable) :** La sensibilité du meilleur moniteur disponible décroît en O(1/√n) avec le nombre d'actions n, indépendamment de la configuration, parce que la dilution du signal suit une marche aléatoire sous sabotage diffus—mais cette borne est atteinte différemment selon la configuration, ce qu'une analyse conjointe révèle là où des articles séparés ne pourraient que constater. Si les trois courbes empiriques divergent de façon non prévisible, la problématique commune n'existe pas.

**(3) Antériorité la plus proche :** Greenwald & Hall (2003) sur la détection d'anomalies séquentielles ; Christiano et al. (2021, « AI Safety via Debate ») sur la vérification par adversaire ; Irving & Askell (2019, « AI safety needs social scientists ») sur la détection multi-agent. Cité de mémoire, non vérifié.

**(4) Expérience qui trancherait :** Faire accomplir à Mistral-7B (ou LLaMA-3-8B) une tâche de résumé documentaire de 200 étapes avec taux de sabotage fixé (5 %, 10 %, 20 %) dans trois conditions : agent seul, deux copies collaborantes, agent face à un moniteur qu'il peut lire. Mesurer la courbe ROC du meilleur moniteur dans chaque condition et tester si les trois courbes s'alignent sur une même loi de décroissance. Durée estimée : 6 semaines avec deux personnes.

**(5) Type de contribution :** Phénomène : si les trois courbes s'alignent, c'est un phénomène unifié transférable depuis la théorie de la détection séquentielle. Si elles divergent, les trois articles gagnent à rester distincts.

**Problématique d'ensemble :** Elle existe. Le lien est la *dilution du signal sous contrainte de ressources de vérification*. Les trois articles gagnent à partager un cadre formel commun (taux de faux positifs admissible, budget de vérification, longueur de tâche) et à mesurer leurs résultats sur la même échelle, même si leurs expériences restent séparées. Sans ce cadre, leurs conclusions sont incomparables. Avec lui, chaque article contraint les deux autres : si le moniteur interne est inefficace face au ciblage, cela borne ce que le défenseur peut faire dans les deux autres configurations.

**Ce qui rendrait la question sans intérêt :** Si l'une des trois configurations est trivialement réductible aux deux autres (par exemple, les copies multiples sont détectables exactement comme un agent seul répété). **Vérification de la nouveauté :** Chercher dans NeurIPS/ICML/ACL 2022–2024 des articles comparant explicitement ces trois configurations sous un cadre défenseur/adversaire unifié.

---

## Réponse 11

La longueur de la tâche est le facteur le moins étudié dans la littérature sur la surveillance d'agents de langue. La question porte sur son effet asymétrique pour défenseur et adversaire.

**(1) Meilleure question de recherche :** La longueur d'une tâche avantage-t-elle l'adversaire de façon superlinéaire par rapport au défenseur, ou leur rapport de force reste-t-il constant quelle que soit la durée ?

**(2) Réponse attendue (réfutable) :** Le rapport signal/bruit du meilleur moniteur décroît en Θ(1/√n) pour un adversaire diffus (n = nombre d'actions), ce qui avantage l'adversaire de façon superlinéaire dès que n > 100 ; mais un audit à échantillonnage stratifié (pondérant les actions par leur variance de sortie) restaure un rapport constant si la fréquence d'audit est au moins proportionnelle à √n. Cette prédiction est réfutable : si le rapport reste constant sans stratification, l'hypothèse principale tombe.

**(3) Antériorité la plus proche :** Shi et al. (2023, « Large Language Models Can Be Easily Distracted by Irrelevant Context ») sur la dégradation avec longueur ; Perez et al. (2022, « Ignore Previous Prompt ») sur l'injection au fil de la tâche. Pour la détection séquentielle en général : Page (1954, CUSUM). Cité de mémoire.

**(4) Expérience qui trancherait :** Faire accomplir à LLaMA-3-8B une tâche de synthèse d'articles avec n ∈ {20, 50, 100, 200, 500} étapes, avec un adversaire injectant une erreur factuelle tous les k pas (k fixé). Moniteur : classifieur NLI sur chaque sortie. Mesurer F1 en fonction de n. Contrôle : mêmes erreurs concentrées sur les 10 dernières étapes. Durée estimée : 5 semaines.

**(5) Type de contribution :** Loi empirique (phénomène) si la dégradation en 1/√n est confirmée ; mécanisme si l'on identifie pourquoi (perte de contexte, accumulation de biais). Ce serait nouveau par rapport à Page (1954) car le signal n'est pas stationnaire.

**Ce qui rendrait la question sans intérêt :** Si le rapport défenseur/adversaire est constant en n, la longueur n'est qu'un paramètre d'échelle et n'ouvre pas de vulnérabilité propre. **Vérification :** Reproduire l'expérience avec deux valeurs de k différentes ; si les courbes sont parallèles en log-log, la loi est robuste.

---

## Réponse 12

La question porte sur ce que l'homogénéité des agents (copies du même modèle) change pour défenseur et adversaire, par rapport à un agent seul ou à des modèles différents.

**(1) Meilleure question de recherche :** L'homogénéité des agents (copies d'un même modèle) rend-elle le sabotage diffus plus facile à coordonner et plus difficile à détecter que dans un système hétérogène ou mono-agent, à budget de vérification égal ?

**(2) Réponse attendue (réfutable) :** Des copies homogènes partagent les mêmes angles morts comportementaux ; un adversaire qui exploite un angle mort d'une copie l'exploite automatiquement dans toutes, réduisant le coût du sabotage d'un facteur proportionnel au nombre de copies. Simultanément, la corrélation entre sorties des copies permet au défenseur de détecter des déviations par comparaison croisée—mais seulement si les copies reçoivent des contextes différents. Cette dualité est mesurable : le F1 de détection croisée est supérieur dans le régime homogène si et seulement si les copies reçoivent des contextes différents.

**(3) Antériorité la plus proche :** Liang et al. (2023, « Encouraging Divergent Thinking in Large Language Models ») sur la corrélation entre copies ; Greenwald & Hall (2003) sur la détection multi-source. Sur la coordination implicite entre modèles homogènes : Anil et al. (2023, « Gemini: A Family of Highly Capable Multimodal Models ») pour la cohérence inter-copies, de mémoire, non vérifié pour ce point précis.

**(4) Expérience qui trancherait :** Trois conditions avec Mistral-7B : (a) agent seul 100 étapes, (b) deux copies homogènes avec contextes différents, (c) deux agents hétérogènes (Mistral-7B + LLaMA-3-8B). Adversaire : injection de biais factuels partagés dans la condition (b). Moniteur : comparaison croisée des sorties + classifieur NLI. Mesure : taux de détection à faux positifs fixés à 5 %. Contrôle : condition sans sabotage pour calibrer la corrélation baseline. Durée : 6 semaines.

**(5) Type de contribution :** Phénomène nouveau si la dualité (angle mort partagé vs. détection croisée) est confirmée empiriquement ; mécanisme si l'on peut lier les angles morts aux têtes d'attention spécifiques.

**Ce qui rendrait la question sans intérêt :** Si les copies homogènes se comportent exactement comme des agents indépendants (aucune corrélation des erreurs). **Vérification de la nouveauté :** Chercher des articles mesurant explicitement la corrélation des erreurs entre copies du même modèle dans une tâche multi-étapes.

---

## Réponse 13

La question porte sur ce que change la possibilité pour l'agent de *cibler* le moniteur (influencer son verdict) plutôt que de passer inaperçu, et sur les implications pour l'évaluation du moniteur.

**(1) Meilleure question de recherche :** Un agent qui vise à obtenir un verdict favorable du moniteur plutôt qu'à passer inaperçu produit-il un signal détectable distinct, et les métriques d'évaluation actuelles des moniteurs sont-elles aveugles à cette distinction ?

**(2) Réponse attendue (réfutable) :** Un agent qui optimise pour le verdict du moniteur génère un texte qui satisfait les critères superficiels du moniteur (longueur, cohérence locale, marqueurs de qualité) tout en dégradant la substance—un profil de sortie distinct du sabotage passif. Les métriques standard (AUC, F1) ne distinguent pas les deux régimes parce qu'elles sont mesurées sur des distributions où le sabotage passif est la seule hypothèse alternative. Cette cécité est réfutable : un moniteur entraîné sur sabotage passif devrait avoir un AUC significativement inférieur sur un jeu de test avec sabotage actif-ciblé.

**(3) Antériorité la plus proche :** Perez et al. (2022, « Red Teaming Language Models with Language Models ») sur l'adversaire actif. Sur le ciblage de classificateurs de texte : Wallace et al. (2019, « Universal Adversarial Triggers »), de mémoire. Goodhart's Law appliquée aux LLM : Krakovna et al. (2020, « Avoiding Side Effects in Complex Environments »), de mémoire.

**(4) Expérience qui trancherait :** Générer deux jeux de données avec LLaMA-3-8B : (a) sabotage passif (erreurs factuelles aléatoires), (b) sabotage actif ciblant un moniteur NLI donné (l'agent voit le prompt du moniteur et optimise sa sortie par beam search guidé). Entraîner deux moniteurs : l'un sur (a), l'autre sur (a)+(b). Mesurer l'AUC croisée. Contrôle : vérifier que les sorties (b) sont bien dégradantes pour la tâche malgré un score moniteur élevé (évaluation humaine d'un sous-ensemble). Durée : 7 semaines.

**(5) Type de contribution :** Mécanisme (Goodhart adapté aux agents de langue sous surveillance) + phénomène mesurable. La contribution est nouvelle si aucun article ne mesure explicitement l'AUC d'un moniteur entraîné sur sabotage passif et testé sur sabotage actif-ciblé.

**Ce qui rendrait la question sans intérêt :** Si l'agent ne peut pas améliorer significativement son score moniteur sans perdre en dommage (trade-off sévère). **Vérification :** Comparer les scores moniteurs des deux régimes à taux de dommage fixé.

---

## Réponse 14

Je liste les contributions candidates par ordre de robustesse estimée, puis les fausses nouvelles et les faux résolus.

**Contribution 1**
*Énoncé falsifiable :* Un audit stratifié (pondérant les actions par leur variance de sortie) détecte le sabotage diffus avec un budget de vérification significativement inférieur à un audit uniforme, sur une tâche de 200 étapes avec LLaMA-3-8B.
*Travail le plus proche :* Wald (1945, Sequential Analysis) ; pour les LLM : Bowman et al. (2022, « Measuring Progress on Scalable Oversight ») — de mémoire, non vérifié.
*Ce qui le distingue :* Bowman et al. ne testent pas le sabotage diffus multi-étapes avec un adversaire actif.
*Vérification d'antériorité :* Chercher dans ACL/EMNLP/NeurIPS 2022–2024 « scalable oversight sequential audit LLM ».
*Expérience falsifiante :* Si l'audit stratifié ne réduit pas le budget de plus de 30 % à F1 fixé, la contribution tombe.

**Contribution 2**
*Énoncé falsifiable :* Les activations internes d'un agent de 8B paramètres contiennent un signal détectable (AUC > 0,75) de sabotage diffus que les sorties textuelles seules ne donnent pas, sur une tâche de synthèse de 100 étapes.
*Travail le plus proche :* Marks & Tegmark (2023, « The Geometry of Truth ») sur les représentations internes ; Burns et al. (2022, « Discovering Latent Knowledge ») — de mémoire.
*Ce qui le distingue :* Ces travaux ne testent pas le sabotage diffus multi-étapes.
*Vérification :* Chercher « internal activations LLM deception detection long-horizon ».
*Expérience falsifiante :* Si AUC(activations) ≤ AUC(sorties) + ε, la contribution tombe.

**Contribution 3**
*Énoncé falsifiable :* Un adversaire qui sait que le moniteur lit ses activations peut réduire sa visibilité interne de plus de 50 % sans perdre en efficacité de sabotage, par fine-tuning sur un signal de récompense négatif, sur un modèle de 8B paramètres.
*Travail le plus proche :* Hubinger et al. (2019, « Risks from Learned Optimization ») — de mémoire.
*Ce qui le distingue :* Hubinger et al. ne quantifient pas le trade-off visibilité/dommage sur un modèle ouvert.
*Expérience falsifiante :* Si le fine-tuning dégrade les capacités générales de plus de 10 % (mesure MMLU), le coût pour l'adversaire est prohibitif.

**Fausses nouvelles (déjà publiées) :** La détection d'hallucinations par NLI est bien couverte (Maynez et al., 2020). L'audit aléatoire simple pour la supervision humaine est implicite dans Christiano et al. (2017, RLHF).

**Faux résolus (encore ouverts) :** La comparaison directe activations vs. sorties pour la détection de sabotage *diffus* (par opposition à la détection de mensonge ponctuel) reste ouverte. L'interaction entre longueur de tâche et budget d'audit n'a pas de loi empirique publiée.

**Ce qui me ferait changer d'avis :** Un survey systématique de ICLR/NeurIPS 2024–2025 avec les mots-clés « diffuse sabotage », « scalable oversight sequential », « internal monitor adversarial ».

---

## Réponse 16

**Affirmation A** : À faux positifs égaux, l'un des deux moniteurs détecte plus que l'autre.

- *État :* Indécidable en l'état, mais plausible que le moniteur interne soit supérieur sur le sabotage *latent* (non exprimé textuellement) et inférieur sur le sabotage *expressif*.
- *Forme réfutable :* AUC(moniteur interne) > AUC(moniteur sorties) + 0,05 sur un jeu de test de sabotage latent, à taux de faux positifs ≤ 5 %.
- *Antériorité :* Burns et al. (2022, « Discovering Latent Knowledge ») — de mémoire. Ne teste pas le sabotage diffus.
- *Expérience minimale :* LLaMA-3-8B, tâche de résumé 100 étapes, deux types de sabotage (latent vs. expressif), deux moniteurs (NLI sur sorties, sonde linéaire sur activations couche 20). Contrôle sans lequel le résultat ne vaut rien : vérifier que le sabotage latent est bien dégradant pour la tâche (évaluation humaine de 50 exemples).
- *Issue sans intérêt :* Si AUC des deux moniteurs est identique à ε près sur les deux types.

**Affirmation B** : Les deux moniteurs ensemble détectent plus que le meilleur seul, et plus que deux moniteurs de sorties différents.

- *État :* Plausible si les deux moniteurs ont des erreurs indépendantes.
- *Forme réfutable :* F1(ensemble) > F1(meilleur) + 0,05 ET F1(ensemble) > F1(deux sorties) + 0,05.
- *Antériorité :* Dietterich (2000, « Ensemble Methods in Machine Learning ») — de mémoire. Non spécifique aux LLM sous sabotage.
- *Expérience :* Même setup que A, ajouter un second moniteur de sorties (BLEURT ou BERTScore). Contrôle : corrélation des erreurs des deux moniteurs de sorties vs. moniteur interne+sortie.
- *Issue sans intérêt :* Si les erreurs des deux moniteurs sont fortement corrélées (r > 0,8).

**Affirmation C** : L'adversaire peut (ou ne peut pas) réduire sa visibilité pour l'un sans l'accroître pour l'autre, ou sans perdre en dommage.

- *État :* Indécidable actuellement ; c'est la plus importante des quatre.
- *Forme réfutable :* Fine-tuner l'adversaire pour minimiser la détection interne ; mesurer si la détection par sorties augmente et si le dommage diminue. Si le front de Pareto est convexe (réduire l'un augmente toujours l'autre), C est fausse.
- *Antériorité :* Hubinger et al. (2019) — de mémoire. Ne quantifie pas le trade-off.
- *Expérience :* Fine-tuning de LLaMA-3-8B avec récompense = −score(moniteur interne), pénalité = −dommage. Mesurer le front de Pareto (visibilité interne, visibilité sortie, dommage). Contrôle : sans pénalité de dommage, pour séparer les effets.
- *Issue sans intérêt :* Si le trade-off est trivial (réduire l'un augmente toujours l'autre proportionnellement).

**Affirmation D** : Le moniteur interne n'ajoute rien au moniteur de sorties.

- *État :* Fausse si C est vrai (il existe un sabotage latent détectable par les activations mais pas les sorties).
- *Forme réfutable :* F1(interne seul) ≤ F1(sorties seul) sur tous les types de sabotage testés.
- *Antériorité :* Marks & Tegmark (2023) suggèrent le contraire pour la véracité, de mémoire.
- *Expérience :* Incluse dans l'expérience de A.
- *Issue sans intérêt :* Si le sabotage latent n'existe pas empiriquement (toute dégradation s'exprime textuellement).

**Relations entre A, B, C, D :** Ce ne sont pas des rivales mais des *compléments hiérarchiques*. C est la thèse centrale (trade-off adversaire). A et B sont des mesures nécessaires pour trancher C. D est un cas limite de A.

**Quelle mérite d'être la thèse d'un article :** C, reformulée ainsi : « Le trade-off visibilité/dommage pour un adversaire face à deux moniteurs hétérogènes définit une frontière de Pareto mesurable. » A, B, D sont des mesures dans cet article.

**Affirmation oubliée :** L'effet de la longueur de la tâche sur les deux courbes ROC—si la supériorité du moniteur interne dépend de n, ce qui conditionnerait le choix du moniteur selon la durée.

FIN DES RÉPONSES.
