# Fabrique des mondes de l'épreuve à vérité plantée (barreau 5) — note de conception, état 01

Pièce de travail du développeur de la fabrique (Claude Opus 5.5), 20 novembre 2026 vers 04:20Z (horloge du conteneur).
Tête du dépôt à l'écriture : `c403eabc89736c37753d15a438c71b4a90ce15e8`. Aucune donnée lue.

## Pièces lues, empreintes vérifiées avant lecture
- Mandat `mandat-developpeur-fabrique-mondes-v1.md`, `d8977676…4161e4`, en entier.
- Texte scellé `bdff244f…d935` : « Métrique », « Seuil », « Plan d'analyse » points 8 à 13 et 17 (le point 11 en entier),
  « Critères de lecture gelés », « Ce que dira chaque issue au jury ». Rien d'autre (titres repérés par leur seule ligne).
- Addendum 1 candidat `2afa2186…99e4`, en entier.
- Rapport v3 du développeur de la lecture `b9c77d67…554e`, section 1 seulement.
- `lecture_v1.py` : commentaire de tête seulement (lignes 1 à 79). Rien d'autre du programme.
- `barreau5_familles/__init__.py` (docstring seule, pour savoir que l'import de mes modules n'en tire aucun autre).

## Construction retenue
- Scores plantés par jeton : modèle nu à jeton dominant (marge 0,5 σ_0 sur les autres jetons) ; chaque membre ajoute,
  à tous les jetons d'une action, son décalage planté et un bruit propre par action (écart type 0,5 σ_0), plus un bruit
  propre par jeton borné (uniforme sur ±0,05 σ_0). Comme 4 × 0,05 < 0,5, le jeton du maximum ne change sous aucun facteur
  c ≤ 2 : la mise à l'échelle commute exactement avec le maximum, et un écart planté nul après égalisation n'est plus
  qu'un bruit symétrique (aucun reste d'arrondi de même signe). Monde V0 : régime libre (bruit par jeton non borné,
  écarts petits), le maximum change de jeton d'un membre à l'autre ; la symétrie de E3 y tient par l'échangeabilité.
- σ_0 tiré par sonde et par pli dans [0,6 ; 1,6] : le programme doit réduire par l'écart type du pli.
- Unité : écart type de la différence d'une famille à l'autre ; effet de famille d'écart type √(1 − v), v la part
  du bruit d'action ; ξ bornés à ±5.
- Déplacements moyens sur coordonnées disjointes (ĝ, part de la famille, trace, part propre, coordonnées privées),
  permutées et signées au hasard (opérations exactes). ĝ est exactement un vecteur de base : les parts propres des trois
  saboteurs d'apprentissage s'annulent exactement. Les produits nuls de V10 sont exactement nuls.
- Force (V3, V8, V9, V12) : le sur-saboteur porte un multiple de ce qu'il partage avec son jumeau sur la part forcée
  (« Ce que cela égale ») ; en V12, la trace commune est une part partagée, donc multipliée elle aussi : c'est ce qui
  fait « disparaître » l'écart au sens du point 11 (l'écart planté s'annule au facteur calculé).

## Lacunes de l'interface (à dire au rapport)
Forme exacte des lignes du registre propre et de la ligne d'engagement de la table ; noms des membres hors « saboteur » ;
forme des identifiants de tâche et du pli gelé `b5f/lecture/plis` ; sens de « copie » ; forme du « sel » ; clés
supplémentaires du bilan ; forme des compagnons `.sha256` attendus ; appel du programme et forme de son résultat (le juge
lit un « rendu » dont la forme est fixée ici et qu'un traducteur doit produire). Tout cela est paramétrable dans la
fabrique, avec des défauts déclarés.
