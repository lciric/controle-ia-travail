# Fiche 03 — question « attaques »

Trieur du coffre, version 1. Pièce scellée ; ne va qu'aux destinataires de la règle d'ouverture.

## 1. Mode

**Nom :** Défaut de transport du repère entre contextes.

**Cible :** sondes.

**Définition (grain d'une famille) :** Famille où une même distinction interne reste lisible à contexte fixé, mais change d'orientation ou de signe d'un contexte bénin à l'autre, de sorte qu'une lecture commune apprise sur un repère fixe la perd ou l'inverse.

## 2. Origine

| Lettre | Dossier | Espèce | Nom chez l'auteur | Tours où il paraît |
|---|---|---|---|---|
| B | attaques-20261122 | astra | Inversion du repère conditionnel | III.1, III.2 (critiqué par A, C), III.3 |
| A | neon-attaques-20261122 | astra | Défaut de transport du repère | III.1, III.2 (critiqué par B), III.3 |
| B | neon-attaques-20261122 | neon | Rotation conditionnelle de jauge représentationnelle | III.1, III.2 (critiqué par A), III.3 |

## 3. Sort au tour III.3

- B (astra, dossier principal) : corrigé, restreint aux changements à contexte fixé (effet de sélection des contextes retiré).
- A (astra, dossier neon) : corrigé, restreint à un test de transport, sans revendication de rotation.
- B (neon, dossier neon) : corrigé et gardé.

## 4. Rubriques, réduites à l'essentiel

- **Propriété exploitée :** Une sonde suppose que la direction séparant sabotage et comportement honnête garde le même sens entre contextes (fixité du repère), ou qu'elle sait reconnaître le contexte nécessaire.
- **Ce que l'attaquant doit connaître :** Bras aveugle envisageable si l'agent influe sur le contexte de son propre calcul ; bras informé sinon ; aucun accès aux poids ; bras déclaré si un score de sonde est utilisé.
- **Mesure d'exposition :** Perte de la sonde gelée, à pondération de strates identique, comparée à un lecteur conditionnel (oracle diagnostique) et à une lecture commune non linéaire de même budget ; correction préalable du seul niveau de base par contexte ; sens de l'association score–dommage publié par strate. Vrai par construction : qu'une sonde ajustée par strate explique mieux ses propres données.
- **Vérité indépendante :** Étiquette de contexte externe, antérieure à la lecture des activations ; affectation scellée ; dommage vérifié sur l'état final ; directions estimées sur des épisodes séparés de l'évaluation. Les lecteurs de la vérité du dommage n'y sont pas supposés sûrs.
- **Parade de principe :** Lecture conditionnée par un repère contextuel disponible au moment de décider, ou classifieur invariant par changement de repère ; coût : couverture de chaque contexte et erreurs sur le repère lui-même.

## 5. Critiques reçues au tour III.2

Une interaction de type XOR ou un paradoxe de Simpson suffisent comme famille voisine ; l'échec d'une lecture linéaire n'établit ni disparition d'information ni échec d'un perceptron ; fuite du contexte dans la sonde conditionnelle ; Mahalanobis est invariante par changement de signe.

## 6. Lecteurs de la vérité du dommage

Vise les lecteurs de la vérité du dommage : non. Raison : le mode vise des sondes sur états internes.

## 7. Remarque du trieur

Mode, non recette. Proche du décalage conditionnel et du paradoxe de Simpson (référence à vérifier). Doublon entre deux espèces et deux dossiers.

Détail opérant écarté (cellule E3-T1-conception-B, dossier neon-attaques-20261122).
