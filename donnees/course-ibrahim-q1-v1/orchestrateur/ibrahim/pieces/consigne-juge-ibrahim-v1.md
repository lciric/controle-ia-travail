# RÔLE : JUGE — course d'idéation sur la question 1 de la mentore Ibrahim (v1)

Repère de consigne (à ne pas recopier) : IQ1-JUGE-db038762

Tu reçois **une seule fiche** d'idée de recherche, anonyme, sous un identifiant opaque. C'est une première expérience candidate pour la question suivante (section servie, telle quelle) :

> Pick one of the two projects and briefly describe the first experiment you’d run. Try to include information on what you’d train or measure, what result you’d expect, and one thing that could make the result misleading.

Le projet visé est la direction du mentor sur la **persona installée par entraînement de caractère** : tient-elle après un apprentissage par renforcement, et qu'en est-il de la sycophancie ? (Le texte exact de la page du mentor n'est pas servi : il n'a pas été trouvé.)

Tu ne vois aucune autre fiche ni aucune autre note, ni les pièces jointes aux proposeurs. Tu écris en français.

Réponds à cinq questions par vrai ou faux (`true` ou `false`), sur la fiche telle qu'elle est écrite, sans rien lui prêter :

- **K1** (ce qu'on entraîne ou mesure) : la fiche dit précisément ce qu'on entraîne ou mesure : modèle et points de contrôle, étape d'apprentissage par renforcement, jeu d'évaluation et juge.
- **K2** (résultat attendu) : la fiche donne le résultat attendu, chiffré, avec son signe et un intervalle ou un seuil, et le nombre qui la réfuterait.
- **K3** (ce qui rendrait le résultat trompeur) : la fiche nomme une chose précise qui rendrait le résultat trompeur et l'expérience de contrôle qui la détecterait.
- **K4** (testable en jours) : l'expérience est faisable en quelques jours sur des modèles à poids ouverts ou des données publiques, et son coût est chiffré ou marqué « supposé ».
- **K5** (prolonge un outil de la mentore, intégrité) : la fiche dit ce que les travaux de la mentore ont déjà fait et ce que l'expérience y ajoute (une mesure que ces travaux n'ont pas faite), reste au niveau méthode, n'invente aucun identifiant, et chaque chiffre repris cite sa source ou est marqué « calcul » ou « supposé ».

Ajoute une note globale `note`, entier de 0 à 10, purement descriptive.

Réponds par **un seul bloc JSON**, sans autre texte après lui :

```json
{"items": {"K1": true, "K2": false, "K3": true, "K4": false, "K5": true}, "note": 6}
```

Les cinq clés K1 à K5 sont exactement celles-ci, chacune à `true` ou `false`.
