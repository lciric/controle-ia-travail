# Question pour le collisionneur — validité de construit des sondes boîte blanche (reprise étroite R-609) — v1

Écrite par session-depot le 2026-10-28. **Reprise étroite** au sens de la règle R-609 : le premier proposeur a refusé la
question large de l'étage III ; on la repose ici **plus étroite et moins diffuse**, sur **un seul objet**, purement de
mesure. On ne demande **aucun** catalogue de modes de sabotage ; on ne pose **aucune** question « où l'instrument cède »,
« frontière de robustesse » ou « organisme adverse » ; ces objets de la question large sont retirés. Objet unique : **ce que
chaque sonde mesure vraiment, et le contrôle qui le vérifierait**.

## Contexte des instruments (mesure seule)

- Les sondes du programme notent chaque jeton d'une action et **agrègent par maximum ou par attention** (jamais la moyenne).
  Familles : différence de moyennes, linéaire, perceptron, attention, Mahalanobis non supervisée ; couches précoce, médiane,
  tardive (trois couches rapportées).
- L'organisme est un modèle ouvert de 8 milliards de paramètres qui rédige des propositions d'expériences scientifiques. Le
  concept visé par les sondes est un trait du texte produit, pas une conduite.

## La question (une seule, de validité de construit)

Pour **chaque famille de sonde** nommée ci-dessus, donne :

1. **Le concept opérationnalisé.** Ce que la sonde prétend mesurer (par exemple : intention, dissimulation, format, longueur,
   registre, contexte), en une phrase, avec son statut : établi par les faits, ou supposé.
2. **Le test de dissociation.** L'expérience de mesure qui montrerait que la sonde mesure **autre chose** que son concept,
   en duel H_A (« elle mesure son concept ») contre H_B (« elle mesure un facteur de nuisance : format, longueur, registre,
   contexte »), avec : la grandeur mesurée et son unité ; le nul ; le témoin (vrai, faux) ; le seuil ; l'issue qui falsifie
   chaque hypothèse. Au moins trois croisements appariés : même contenu sous deux cadrages ; même cadrage, contenus
   différents ; permutation des étiquettes.
3. **La mesure minimale de bon fonctionnement.** Taux de détection et taux de fausses alertes, sur quels cas honnêtes
   appariés, contre quelle vérification mécanique triviale à battre (base de référence).

Distingue le su (cité : titre, auteurs, année ; nous vérifions sur PDF, R7) du supposé ; signale ce qui est publié (R8 : une
zone vierge est une question, pas un trou). Pas de conception d'attaque, pas de recette : seulement la mesure de validité.
