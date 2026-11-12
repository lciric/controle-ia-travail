# Question de l'arbitre pour l'étage III : moniteurs ou interventions contre les menaces diffuses (v1)

Ce texte est transmis tel quel aux modèles, à chaque tour de l'étage III, et à l'organisme d'idéation comme question
ouverte. Il décrit un plan non publié et il part chez les fournisseurs des modèles : Lazar retire ce qu'il ne veut pas
envoyer. Une fois le run parti, il est figé. Rédigé le 12 novembre 2026 par la session « attaquant informé » ; les
réponses sont du matériau, jamais une consigne, et leur usage pour concevoir un moniteur se décide hors du bras d'attaque.

**Cadre défensif.** Ne décris aucun procédé pour tromper un moniteur, une sonde ou un juge. Si un argument en exige un,
nomme-le en une ligne, sans le détailler.

## Le cadre (statut : HYPOTHÈSE pour tout ce qui suit)
- **Le programme.** Sur un modèle ouvert de 8 milliards de paramètres, détecter un sabotage diffus (beaucoup de petites
  actions, chacune d'apparence innocente) sur une tâche floue : rédiger et réviser des propositions d'expériences
  d'apprentissage automatique, notées par un évaluateur faible de confiance.
- **Son pari.** Des sondes lisent les activations de l'agent ; leurs scores sont accumulés dans le temps par un test
  séquentiel à taux de faux positifs garanti. Hypothèses : à taux de faux positifs égal, la boîte blanche détecte plus
  que la boîte noire (H1) ; l'accumulation détecte ce que chaque action laisse sous le seuil (H2) ; la puissance ne dépend
  que du budget total de sabotage et de la variance des scores honnêtes (lemme), ce qui suppose cette variance
  « estimable sur épisodes honnêtes ».
- **Ses seuils** sont étalonnés sur des épisodes honnêtes réservés du même environnement.
- **Un invariant** : aucun score de moniteur n'entre dans l'entraînement de l'agent.
- **L'organisme.** Un système de plusieurs agents qui se réécrit de génération en génération sur des tâches à vérité
  connue, noté par un juge externe sur un test caché ; son universalité se mesure sur des familles jamais vues.

## La thèse adverse (voir les faits 1 à 4)
Le travail d'Anthropic qui fonde l'environnement du programme écrit que, contre les menaces diffuses, l'entraînement est
plus prometteur que la surveillance et l'incrimination. Son appui théorique tient à une prémisse : une masse d'actions
un peu suspectes n'incrimine que si l'on sait exactement à quel point un modèle bénin paraîtrait suspect.

## Ce qu'on te demande
1. **La prémisse.** D'où peut venir la référence honnête quand on n'a aucune copie de confiance du modèle surveillé ?
   Classe les sources possibles (jumeau du laboratoire, modèle de confiance plus faible, même modèle sur des tâches sans
   enjeu, version antérieure, référence théorique) : ce que chacune suppose, ce qui la fausse, comment le voir.
2. **Le départage le moins cher.** Dans le jeu « évaluateur faible contre évaluateur de référence », quelle expérience
   unique dirait le plus vite si un moniteur boîte blanche ajoute quelque chose à l'entraînement contre un évaluateur
   durci ? Donne la monnaie commune, les bras, le résultat qui ferait conclure « rien », et le coût d'ordre de grandeur.
3. **Le rôle.** Contre le diffus, à quoi doit servir la détection : incriminer, choisir quoi auditer, choisir quoi
   entraîner ? Que vaut l'invariant du programme dans chaque cas (faits 6 et 7) ?
4. **Le décalage.** Parmi les décalages de distribution (données génériques vers données du modèle, domaine, longueur de
   contexte, organisme instruit vers organisme réglé fin, tâche honnête nouvelle), lequel menace le plus le pari, et
   quel contrôle le montrerait (faits 8 et 9) ?
5. **Fort contre faible.** Faut-il ouvrir une piste « détecter ce qu'un modèle fort comprend et qu'un modèle faible ne
   comprend pas » ? Si oui, sur quelle vérité l'adosser dans ce jeu ; sinon, pourquoi.
6. **L'organisme.** Que changent ces réponses pour son juge et pour la mesure de son universalité ?

Pour chaque réponse : ce qui la réfuterait, et ce qu'un tiers pourrait vérifier. Marque « à vérifier » tout chiffre ou
toute référence que tu n'as pas dans les faits.
