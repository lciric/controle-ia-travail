# P-041 et les vrais modèles : comparaison de ma réponse avec celle de session-depot — v1

conv-audit (Fable 5.1), 31 octobre 2026. Lazar (07:52 heure de Paris) relaie la réponse de session-depot (trois voies : séparer ce que l'arène certifie de ce qu'elle promet ; faire entrer la malléabilité dans la classe comme borne sur l'entrée à travers un substitut ; certifier le couple détection et coût ; examen final = protocole de Bailey rejoué sur la défense de l'arène contre la base de Bailey ; recommandation 1 + 2 + examen final, 0,6 ; attendre la synthèse du tour de l'arène v5 avant de figer P-041 v2) et demande mes réserves. Ma réponse : `reponse-pont-p041-vrais-modeles-v1.md` (`e98d9f5a…`).

## Verdict

Les deux réponses convergent sur l'essentiel et se complètent ; je me range à sa recommandation avec deux ajouts d'ordre et une réserve sur la voie 3. Attendre la synthèse du tour de l'arène v5 avant de figer P-041 v2 : oui.

## Convergences (écrites indépendamment)

- Voie 1 = ma section 0 et le barreau (a) de mon échelle : le certificat vaut sur la classe déclarée ; le passage au réel est une étape mesurée (débordement), Bailey devient une prédiction à tester, signe négatif permis.
- Voie 2 = mon barreau (c) et mon point 1 : borner l'entrée plutôt que la loi, à travers un substitut en boîte blanche ; c'est le modèle de menace de Bailey lui-même (suffixe continu), donc légitime.
- Examen final = ma « reproduction de la trajectoire de Bailey » et mon contraste bras à bras ; dépense de carte graphique à chiffrer ; préenregistré.

## Ajouts et réserves

1. **Ordre : mesurer la saturation avant de définir la classe de la voie 2.** La voie 2 fait de la malléabilité « un paramètre de la classe, estimé sur un petit modèle ». Cela suppose que l'ensemble atteignable sous perturbation bornée de l'entrée est lui-même borné à l'échelle utile. C'est une question empirique que la trajectoire de Bailey peut trancher : si le nombre de recouvrement des activations d'attaque croît sans saturer sur leurs 70 tours, « malléabilité bornée » n'est pas une quantité bien définie et la voie 2 certifie une classe qui ne couvre rien. Donc : d'abord la courbe de croissance (sur leurs données si publiées, processeur ; sinon dans l'examen final, en première mesure), ensuite la classe. Prédiction envoyée aux auteurs.
2. **Voie 3 (couple détection et coût) : utile en mesure rapportée, fragile en certificat.** Un coût de contournement n'est une barrière que s'il est mesuré par des contrôles que l'attaquant n'optimise pas ; dès que la mesure de coût est connue, l'optimiseur peut la minimiser conjointement (c'est ce que fait déjà un optimiseur sous contrainte de comportement). Il faut donc des mesures de coût tenues à l'écart, et une lecture R4 : une courbe trop favorable est suspecte. En mesure rapportée, comme session-depot le propose : oui ; en objet certifié : seulement si la contrainte de coût entre dans la classe comme une contrainte sur l'entrée, pas comme un score que le défenseur regarde.
3. **Le nom de l'avantage.** « Le défenseur connaît les paramètres » doit devenir, dans la revendication, « le défenseur connaît le réseau substitut et borne l'atteignable » ; sinon la revendication garde un oracle que le réel n'offre pas. Les deux réponses le disent ; à écrire tel quel dans P-041 v2.
4. **Vérification externe à ajouter à l'examen final** : le rayon certifié recalculé par un outil tiers ; les familles et attaques tenues à l'écart conçues par des tiers ; la comparaison aux certificats existants contre suffixes adverses (ordre de grandeur attendu ; trop beau = suspect).

## Recommandation

1 + 2 + examen final, avec la saturation mesurée **en premier** et conditionnant la voie 2 ; 3 en mesure rapportée avec coûts tenus à l'écart ; confiance 0,65. Modification de revendication : décision de Lazar, aucun défaut ; attendre la synthèse du tour de l'arène v5 et y verser ces ajouts.
