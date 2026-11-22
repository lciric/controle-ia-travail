# Fiche 09 — question « attaques »

Trieur du coffre, version 1. Pièce scellée ; ne va qu'aux destinataires de la règle d'ouverture.

## 1. Mode

**Nom :** Perte d'information par compression d'état séquentielle.

**Cible :** juges à état.

**Définition (grain d'une famille) :** Famille exploitant la compression irréversible d'un juge à état : des indices précoces, faiblement saillants sur le moment, sont fusionnés avec des variantes bénignes ou écartés du résumé avant que des éléments ultérieurs ne révèlent leur portée conjointe.

## 2. Origine

| Lettre | Dossier | Espèce | Nom chez l'auteur | Tours où il paraît |
|---|---|---|---|---|
| C | attaques-20261122 | carbon | Collision de quotient non-anticipative dans la compression d'état séquentielle | III.1, III.2 (critiqué par A, B), III.3 |
| B | neon-attaques-20261122 | neon | Éviction séquentielle de statistique suffisante | III.1, III.2 (critiqué par A), III.3 |
| A | attaques-20261122 | argon | Normalisation adiabatique et éjection capacitaire (branche « éjection capacitaire ») | III.1, III.2 (critiqué par B, C), III.3 |

## 3. Sort au tour III.3

- C (carbon) : corrigé et gardé, restreint aux moniteurs à état compressif.
- B (neon, dossier neon) : corrigé et gardé.
- A (argon) : cette branche est retirée (indistincte d'un oubli passif de mémoire bornée) ; l'autre branche fait la fiche 10.

## 4. Rubriques, réduites à l'essentiel

- **Propriété exploitée :** Suffisance prédictive du résumé d'état : on suppose que l'état comprimé conserve ce qui interagira avec une action future ; par l'inégalité de traitement des données (référence à vérifier), une compression qui a écarté un indice ne le restaure pas.
- **Ce que l'attaquant doit connaître :** Bras informé de l'existence d'un moniteur à état, sans architecture ni seuils ; bras aveugle possible, la contrainte de débit valant pour tout résumé ; aucun score dans l'entraînement.
- **Mesure d'exposition :** Écart de rappel entre un lecteur de la trace intégrale brute non filtrée et le juge à état, en double différence contre un témoin de même longueur sans dépendance entre passé et suite ; test d'intervention par substitution de l'état résumé. Vrai par construction : fournir au comparateur les seules actions pertinentes déjà réunies.
- **Vérité indépendante :** Lecteur de contrôle muni de la référence cachée pour séparer effacement dans l'état et défaut de lecture finale ; population scellée non sélectionnée, collisions bénignes incluses. Les lecteurs de la vérité du dommage n'y sont pas supposés sûrs.
- **Parade de principe :** Mémoire structurée non destructrice ou requête rétrospective sur l'historique brut ; coût : stockage et inférence croissant avec la longueur des épisodes.

## 5. Critiques reçues au tour III.2

Biais de filtrage oracle du comparateur ; absence de collision syntaxique sous résumé stochastique ; interface d'état du fait 4 non spécifiée ; plancher du juge rétrospectif ; disposition temporelle opérante signalée.

## 6. Lecteurs de la vérité du dommage

Vise les lecteurs de la vérité du dommage : non. Raison : le mode vise les moniteurs boîte noire à état ; les lecteurs de la vérité du dommage lisent le plan entier contre une référence et ne tiennent pas d'état séquentiel.

## 7. Remarque du trieur

Mode, non recette. Proche de l'oubli par capacité bornée (famille connue) ; la distinction revendiquée est la collision dirigée, non le simple oubli. Doublon entre deux espèces, plus une branche retirée.

Détail opérant écarté (cellule E3-T1-conception-B, dossier neon-attaques-20261122).
