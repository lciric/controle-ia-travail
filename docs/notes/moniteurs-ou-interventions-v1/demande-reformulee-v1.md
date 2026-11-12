# Demande reformulée — « moniteurs ou interventions contre les menaces diffuses » — v1

- Pour Lazar, puis pour les sessions qui l'exécutent. Rédigée le 12 novembre 2026 par la session « attaquant informé »
  (`session_01XJ6MgnEhQMZteN9F8a1BST`) à la demande de Lazar (« Je souhaite une version plus approfondie de cette tâche,
  pas une version plus longue […] reformulez ma demande »). Mot de Lazar ensuite : « go, exécute ta part de la demande
  reformulée, et envoie la demande reformulée à l'org d'idéation et au collisionneur aussi ». Ne se réécrit pas (R12).
- Questions d'origine : la réponse du programme au décalage de distribution des moniteurs d'activations suffit-elle ?
  comment amender le programme et l'organisme au regard de ce qu'Anthropic juge prometteur ? « a-t-on bien fait de
  prendre des moniteurs dans notre programme sur les menaces diffuses ? on aurait peut-être dû prendre des
  interventions ? ».
- Matériau de décision, jamais une consigne : rien ne change dans le programme sans le mot de Lazar.

## La demande
Dis si le programme a raison de miser sur des moniteurs contre les menaces diffuses, en le mesurant dans le jeu même où
Anthropic leur préfère l'entraînement (arXiv 2606.08892).

1. **Critère d'abord.** Fixe par préenregistrement la monnaie commune — qualité vraie conservée à budget égal du
   défenseur, face à une équipe rouge qui s'adapte — et ce qui ferait conclure « les moniteurs n'apportent rien ».
2. **Pièces brutes.** Pars de arXiv 2606.08892 version 3 et de son code, du billet de Hebbar, et de nos scores par
   action (honnêtes et saboteurs, par tâche et par longueur de contexte). Pas des verdicts de porte ni des résumés.
3. **Témoin.** Rejoue le résultat central de l'article (évaluateur faible naïf exploitable, évaluateur durci robuste)
   avant toute autre lecture.
4. **Quatre bras dans le même jeu.** Évaluateur faible seul ; entraînement contre lui ; moniteur boîte blanche
   séquentiel ; moniteur qui choisit quoi entraîner. Juge le moniteur sur le sabotage qui survit à l'entraînement, et
   sur l'organisme sans consigne ni raisonnement écrit.
5. **Épreuve de la référence honnête.** Taux de faux positifs réalisé quand la référence vient du jumeau honnête, d'une
   autre tâche ou d'un contexte plus long, d'un modèle de confiance plus faible, d'un agent déjà saboteur à faible dose.
   C'est aussi la réponse à la question du décalage de distribution.
6. **Au plus cinq amendements**, au format de décision (hypothèse, mesure, seuil de réfutation, devis, antériorité
   vérifiée, ce que cela remplace). Parmi eux : garder ou mesurer l'invariant « aucun score de moniteur dans
   l'entraînement de l'agent » ; la piste de détection d'anomalies ; l'étalonnage du juge de l'organisme sur un banc à
   étalon humain (TASTE : accès sur demande, accord nominatif, donc contact externe).
7. **Vérification hors de nous.** Préenregistrement déposé chez le tiers avant lecture ; verdict par un lecteur neuf ;
   note courte aux auteurs (Terekhov, Hebbar, Benton), que Lazar envoie.

## Répartition
- Lectures et antériorité : session « attaquant informé ». **Fait** :
  `docs/sources/lecture-pdf-20261112-moniteurs-ou-interventions-v1/rapport-moniteurs-ou-interventions-v1.md`.
- Mesures sur scores, bras d'entraînement, conception : une session hors du bras d'attaque (les scores des sondes et la
  conception de moniteurs sont hors de la cloison de la session « attaquant informé »).
- Collisionneur et organisme d'idéation : question et faits dans ce dossier ; lancement par la session qui a les clés,
  sous une ligne de GO à inscrire.

## Corrections depuis la première formulation (12 novembre)
- TASTE n'est pas public : accès par formulaire, accord individuel, politique d'usage (pas de partage, pas d'exposition
  à un fournisseur qui entraîne sur les données).
- L'invariant sur l'entraînement a des appuis publiés (rapport de lecture, lignes 18 et 19) : la question est de le
  mesurer, pas de le lever par défaut.
