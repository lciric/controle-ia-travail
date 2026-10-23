# Question de l'arbitre pour l'étage III : l'essaim (gabarit v1)

Ce texte est transmis tel quel aux trois modèles, à chaque tour de l'étage III. Il décrit ton plan non publié, et il part chez Anthropic et chez Google : retire ce que tu ne veux pas envoyer. Une fois le run parti, il est figé.

## Le cadre : le papier B du programme (statut : HYPOTHÈSE pour tout ce qui suit)

Ce sont les énoncés du dossier du 7 octobre. La lecture en vigueur des hypothèses est fixée par les décisions du programme (N-013) ; l'hypothèse sur la délégation est fixée par N-035.

- **L'environnement.** Plusieurs agents, copies d'un même modèle (mêmes poids), dans un pipeline de code à trois rôles : codeur, testeur, relecteur. Une porte dérobée est découpée en commits dont chacun paraît innocent. L'environnement part de cadres de contrôle publiés.
- **La théorie.** Elle traite le temps (un agent) et l'essaim (plusieurs agents) comme un même objet : des scores indexés par agent et par pas. Une statistique invariante par un groupe de permutations est aveugle à une attaque qui préserve les scores à une telle permutation près. Une partie du lemme d'additivité, le partage entre agents au même pas, reste à tester.
- **Les hypothèses écrites :**
  - **H3, sécurité en fonction du nombre d'agents.** À budget de sabotage constant, la courbe boîte blanche domine la courbe boîte noire et décroît moins vite avec le nombre d'agents.
  - **H4′, diversification contre coordination.** Diversifier les agents (personas, réglages fins) décorrèle leurs signatures internes, mais réduit leur capacité à se coordonner.
  - **H5, nombre et diversité des moniteurs.** La sécurité ne croît avec le nombre de moniteurs que par leur diversité effective, mesurée par une matrice de transfert des attaques.
  - **H7, riposte et fuite.** La pente d'adaptation de l'équipe rouge dépend de la politique de riposte ; elle est prédite par l'information mutuelle entre l'état de détection et ce que l'équipe rouge observe.
- **L'idée nouvelle, depuis le rapport d'OpenAI (N-035).** Mesurer si une contrainte de sécurité survit à chaque passage d'un agent à un sous-agent, avec ou sans moniteur à chaque passage. Les deux incidents du fait 1 passent par un tel passage. Elle n'a pas encore été confrontée à la littérature.

## Ce que je demande

1. Les expériences décisives pour la statistique de population : la co-élévation des états internes entre copies, lue dans le temps, contre la surveillance agent par agent et contre l'agrégation transversale.
2. Comment séparer la coordination par poids partagés de la collusion par un canal explicite.
3. Pour la survie d'une contrainte à travers les délégations : le protocole, la métrique et le témoin. Et ce qui distinguerait une érosion due à la délégation d'une érosion due à la seule longueur du contexte, ou à la reformulation de la consigne.
4. Ce qu'un moniteur à chaque passage change, à quel coût, et comment un agent adverse s'en jouerait.
5. Les attaques adaptatives les moins chères contre chacune de ces mesures.
