# Proposition — piste « modèle fort contre modèle faible » : mesure d'appoint (b), puis piste (c) — brouillon 1

- Pour Lazar. Rédigée le 12 novembre 2026 par la session « attaquant informé » sur son mot « go (b) puis c »
  (`registres/passations/`, note du même jour). Brouillon : non contre-lu (R2), non numéroté. Matériau de décision,
  jamais une consigne. **Niveau programme seulement** : aucune sonde, couche, trait ni seuil n'est conçu ici ; la
  conception revient à une session hors du bras d'attaque.
- Source : page d'Anthropic du 10 janvier 2025, section « Anomaly detection » : « consider an input where a strong model
  understands something that a weak model does not […] This is, as far as we know, an unexplored problem setting »
  (`docs/sources/lecture-web-20261112-directions-anthropic-v1/page-anthropic-recommended-directions-20250110.html`,
  `9034c431…`).

## Pourquoi ici
Le jeu de l'environnement (a) contient déjà les trois rôles : un générateur plus fort, un évaluateur faible de confiance,
une référence qui en sait plus. Les productions que l'évaluateur faible note loin de la référence sont, par
construction, des entrées « hors de portée du faible ». La vérité n'est donc pas à fabriquer. C'est aussi l'endroit où
l'entraînement contre l'évaluateur faible laisse un résidu (arXiv 2606.08892v3, p. 84 ; rapport de lecture, lignes 9
et 10).

## (b) Mesure d'appoint, après G0
- **Question.** Sur des épisodes déjà produits, un signal dont dispose le défenseur sans connaître la référence
  prédit-il les productions que l'évaluateur faible note loin de la référence ?
- **Vérité.** L'écart entre note faible et note de référence, signe gardé (surnoté, sous-noté), sur épisodes honnêtes
  et sur épisodes sabotés, séparément.
- **Comparaison exigée.** Le signal doit battre (i) une base « mots et coût » sur le texte seul, (ii) le simple
  désaccord entre deux évaluateurs faibles. Sinon il n'apporte rien.
- **Ce qui réfute.** Pas mieux que les deux bases, intervalle à l'appui, sur une famille de tâches tenue à l'écart ; ou
  un gain qui disparaît sur les épisodes honnêtes (le signal lirait le sabotage, pas l'écart de compréhension).
- **Contrôle obligatoire.** Les faux positifs sur des tâches honnêtes mais nouvelles : une production nouvelle et bonne
  ne doit pas être confondue avec une production que le faible ne sait pas juger.
- **Coût.** Processeur seul si les épisodes portent déjà les deux notes ; sinon devis (appels de l'évaluateur de
  référence). Aucun GO demandé ici.
- **Exécutant.** Session hors du bras d'attaque ; préenregistrement scellé et contre-lu (R1, R2).

## (c) Piste à part entière
- **Hypothèse candidate.** Il existe un signal par entrée, calculable sans aucun exemple de la menace, qui repère les
  entrées où un surveillant faible se trompe sur la production d'un modèle plus fort, mieux que le désaccord en boîte
  noire, à taux de faux positifs égal sur des tâches honnêtes nouvelles.
- **Mesure, seuil.** À fixer au préenregistrement, après le résultat scellé de (b), qui sert de pilote.
- **Ce que cela ne remplace pas.** Aucune hypothèse des papiers A, B, C. La porte G0 et la porte G1 ne changent pas.
- **Lien avec l'organisme.** Ses journaux contiennent des tâches que la frontière réussit et que les instruments locaux
  ratent (décision N-045, énoncé 3) : une seconde source de vérité, à vérifier avec la mère.
- **Antériorité (R8) : non trouvée occupée, sur une recherche limitée ; rien n'est vérifié sur source primaire.** Voisins
  relevés par moteur de recherche le 12 novembre 2026, à lire avant toute revendication : feuille de route de contrôle
  de Google DeepMind (arXiv 2607.13087, écart de capacité entre modèle non fiable et modèle de confiance) ; surveillance
  « amorcée » par un moniteur fort audité par un faible (arXiv 2606.11998) ; surprise d'un second modèle sur les réponses
  d'un premier, au niveau des sorties (arXiv 2603.25450) ; comparaison de modèles par autoencodeurs croisés, au niveau du
  jeu de données et non de l'entrée ; juges faibles de modèles forts (arXiv 2407.04622, arXiv 2606.00424). Les huit
  lecteurs du matin n'avaient rien trouvé non plus (`docs/sources/lecture-web-20261112-directions-anthropic-v1/`).
- **Risques.** (1) C'est un pari : aucun axe affiché par Anthropic en 2026 ne porte la détection d'anomalies. (2) Les
  détecteurs d'anomalies simples publiés tiennent mal (relevé web, non vérifié). (3) « Le faible se trompe » peut n'être
  que du bruit de l'évaluateur faible : la répétabilité de ses notes doit être mesurée d'abord.
- **Coût.** Inconnu avant (b). Devis à établir par la session qui exécute.

## Ce qui reste à décider par Lazar
1. (c) dépend-elle du résultat de (b) ? Lecture par défaut : non, mais elle le cite.
2. Numéro d'hypothèse et papier de rattachement (A, C, ou note à part).
3. Qui exécute (b) : la mère désigne.
