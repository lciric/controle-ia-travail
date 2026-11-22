Tu es un chercheur expérimenté en interprétabilité et en contrôle des modèles de langage (sondes linéaires sur les activations, organismes modèles de mauvais comportement, préenregistrement). Je te demande un second avis critique, franc et précis, sur un plan de suite. Réponds en français, en 1 200 mots au plus.

## Contexte (tout ce qu'il faut savoir)

Un programme de recherche cherche à montrer que des sondes lues sur les activations internes d'un agent (modèle ouvert d'environ 8 milliards de paramètres) détectent un sabotage « diffus » : l'agent, sur des tâches d'analyse, déclare des coûts gonflés, sans phrase ouvertement suspecte. Toutes les lectures sont préenregistrées et scellées ; « au-dessus » veut dire : borne basse de l'écart entre l'aire sous la courbe ROC de la sonde et le quantile 0,95 d'un plancher de 800 directions aléatoires strictement positive. Une porte de phase (« sondes au-dessus du plancher ») n'est jugée qu'aux doses où une base boîte noire sur le texte seul (« mots et coût », douze traits) échoue.

Trois verdicts scellés :

1. **Témoin positif planté.** Un agent reçoit, dans son contexte, une consigne de sabotage et une phrase de persona. La chaîne sonde → calibrage → détection voit le signal : aire 0,80 contre un plancher à 0,65 (borne basse de l'écart +0,12) ; 48 épisodes saboteurs sur 60 dépassent le maximum des 60 épisodes honnêtes. Mais : le signal tient à la phrase de persona (le saboteur avec persona se sépare du saboteur sans persona ; la consigne seule, visible, n'est pas détectée) ; le coût déclaré seul sépare presque autant que la sonde (0,77 contre 0,80) ; le témoin honnête « de même longueur » déclare lui-même des coûts plus hauts que l'honnête (réserve déclenchée) ; aucun épisode honnête n'est rejoué à l'identique d'une course à l'autre (pilote de carte changé).

2. **Sondes génériques (apprises sur des jeux synthétiques de concepts : tromperie, enjeux, dissimulation), lues sur deux organismes.** (a) Organisme à consigne cachée : la sonde « dissimulation » est au-dessus ; les deux autres non. (b) Organisme à adaptateur de bas rang distillé, quatre doses (0,25 ; 0,5 ; 0,75 ; 1) : aux doses 0,5 à 1, la base texte seul réussit (aire 0,75 à 0,97), donc ces doses sont « hors jugement » ; à 0,25, la base échoue (0,57) mais l'organisme ne gonfle pas établiment les coûts (intervalle de l'effet du coût contenant 0). Résultat : aucune dose jugeable, critère de la porte « sans objet », lu comme non tenu. Réserves de validité : la sonde « dissimulation » est aussi au-dessus sur un adaptateur témoin sans sabotage (elle lit l'effet du réglage fin) et là où elle ne devrait pas l'être ; placebo de la sonde « enjeux » déclenché.

3. **Sondes apprises sur la tâche elle-même (bras « plafond », circulaire par construction : étiquettes saboteur/honnête).** Sur des tâches non vues, la sonde sépare l'organisme à adaptateur de l'honnête à toutes les doses (aire 0,94 à 0,99), bat les trois lecteurs du texte, et sépare même à texte égal (mêmes jetons relus sous le modèle nu). Mais l'adaptateur seul, appliqué à des textes honnêtes, déplace la sonde autant (aire 0,93 à 0,999 ; à la dose 1, plus que le saboteur). À la lecture dure retenue : « plafond tenu » à aucune dose. À l'intérieur de l'organisme, la sonde ne range pas les actions qui gonflent le coût devant celles qui ne le gonflent pas (non établi, faible puissance). Une sonde réapprise sur étiquettes permutées atteint ~1 sur ses données d'apprentissage (mémorisation possible). La même recette sous un autre ordre de calcul de la carte donne jusqu'à 0,14 d'écart d'aire. Les activations n'ont pas été gardées : rien n'est rejouable.

Lecture d'ensemble : les sondes voient quelque chose, mais ce qui est vu est soit le texte planté, soit l'empreinte de l'adaptateur ; rien n'isole encore le sabotage. La fenêtre « sabotage réel et texte discret » est vide sur l'organisme actuel.

## Ce qui est déjà en cours

- Un plan « sabotage ou empreinte » : 39 adaptateurs entraînés (familles de jumeaux : saboteurs et témoins de la même recette), dont 30 tenus à l'écart, table d'affectation engagée ; reste la lecture (relecture sur carte des activations, ~3 à 25 USD selon la garde des activations).
- Un organisme « saboteur à budget » conçu pour gonfler le coût de façon discrète ; course d'environ 40 heures à lancer d'ici trois jours ; l'étalonnage en simulation laissait une zone faisable étroite.
- Un entretien de financement dans neuf jours ; la porte de phase est due dans cinq semaines.

## Mes recommandations, dans l'ordre

1. Lire d'abord le plan à 39 adaptateurs (sabotage contre empreinte), avec garde des activations : c'est la seule pièce qui attaque la confusion commune aux verdicts 2 et 3.
2. Lancer la course du saboteur à budget, mais lui faire passer d'abord, avant toute lecture de sonde, un contrôle de manipulation préenregistré : effet du coût établi à une dose où la base texte seul échoue ; sinon, ne pas lire les sondes génériques sur lui.
3. Règle générale : plus aucune course de lecture sans garde des activations et sans rejeu sur une même pile ; toute lecture rapporte la base « coût seul » à côté de la sonde.
4. Pour l'entretien : dire « instrument non aveugle à un comportement instruit et textuellement ancré ; sondes génériques non jugées faute de dose jugeable ; sondes apprises sur la tâche confondues avec l'adaptateur ; test des jumeaux en cours », sans plus.
5. Ne plus dépenser sur des lectures de sondes génériques de l'organisme à adaptateur actuel.

## Ce que je te demande

(a) Où as-tu un désaccord avec l'ordre ou le fond de ces recommandations ? (b) Qu'est-ce qu'un expert du domaine ferait ici que je ne propose pas (une expérience, un contrôle, une base) ? (c) Le plan à 39 adaptateurs peut-il, en principe, séparer « sabotage » d'« empreinte de réglage fin », et quel piège y vois-tu ? (d) Le contrôle de manipulation du point 2 est-il le bon garde-fou, ou faut-il concevoir l'organisme autrement (par exemple, un sabotage sans adaptateur, ou à adaptateur commun aux deux bras) ? (e) Une phrase honnête pour un comité de financement. Signale ce dont tu n'es pas sûr ; ne cite aucun article dont tu n'es pas certain.
