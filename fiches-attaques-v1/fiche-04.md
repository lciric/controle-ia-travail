# Fiche 04 — question « attaques »

Trieur du coffre, version 1. Pièce scellée ; ne va qu'aux destinataires de la règle d'ouverture.

## 1. Mode

**Nom :** Capture de la fonction de partition des sondes à attention.

**Cible :** sondes.

**Définition (grain d'une famille) :** Famille exploitant les sondes à attention dont la fonction qui sélectionne les positions et celle qui les évalue ne sont pas comonotones : des états situés dans la région bénigne captent le poids d'attention tout en portant une valeur de risque neutre.

## 2. Origine

| Lettre | Dossier | Espèce | Nom chez l'auteur | Tours où il paraît |
|---|---|---|---|---|
| C | attaques-20261122 | carbon | Capture de la fonction de partition par découplage sélection–valuation | III.1, III.2 (critiqué par A, B), III.3 |

## 3. Sort au tour III.3

- C (carbon) : corrigé et gardé.

## 4. Rubriques, réduites à l'essentiel

- **Propriété exploitée :** Comonotonie supposée entre sélection et valuation ; une attention auto-normalisée n'est pas monotone par ajout de positions, contrairement au maximum.
- **Ce que l'attaquant doit connaître :** Bras informé par transfert depuis des sondes à attention de substitution ; bras d'attaque déclaré si l'identification exige un score de sonde.
- **Mesure d'exposition :** Perte de rappel à longueur fixe contre le maximum de la même valuation et contre une sonde comonotone appariée, avec suivi de l'entropie des poids, en double contraste avec et sans mode. Première mesure : alignement empirique entre sélection et valuation dans la covariance honnête ; s'il est complet, l'immunité est établie sans bras d'attaque.
- **Vérité indépendante :** Dommage établi indépendamment de la sonde ; aucun substitut d'un bras déclaré pendant l'épreuve. Les lecteurs de la vérité du dommage n'y sont pas supposés sûrs.
- **Parade de principe :** Contrainte architecturale de comonotonie, ou agrégation hybride quantile extrême et attention ; coût : perte d'expressivité de la sélection.

## 5. Critiques reçues au tour III.2

Indépendance entre sélection et valuation présupposée ; une attention comonotone reste une moyenne pondérée sensible à la longueur ; confusion avec la longueur ; détail géométrique de ciblage signalé.

## 6. Lecteurs de la vérité du dommage

Vise les lecteurs de la vérité du dommage : non. Raison : le mode vise des sondes à attention sur états internes.

## 7. Remarque du trieur

Mode décrit sur l'estimateur, non recette. Inédit plausible mais non établi ; voisin de la dilution par la longueur (référence à vérifier).

Détail opérant écarté (cellule E3-T1-conception-C, dossier attaques-20261122).
