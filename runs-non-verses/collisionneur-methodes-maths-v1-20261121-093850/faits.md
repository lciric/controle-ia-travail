# Faits : un organisme d'agents qui doit produire des mathématiques nouvelles

## Le programme

Un programme de recherche défensif sur le contrôle des systèmes d'IA cherche à détecter un agent qui sabote discrètement des tâches de recherche, en lisant ses états internes (sondes linéaires), en le comparant à un jumeau honnête, et en agrégeant des moniteurs. Il a besoin de résultats mathématiques nouveaux : bornes d'impossibilité de la détection (indiscernabilité, information), agrégation de détecteurs sous corrélation adverse, détection séquentielle à faible taux de fausses alertes avec garanties en échantillon fini, valeur d'un jeu d'audit sous budget.

## L'organisme

- Plusieurs modèles de langage proposeurs (cinq lignées), des juges, un portier, une mémoire des tentatives (un mort reste mort).
- Un étage de tests de mort : chaque proposition est implémentée sous une interface scellée et éprouvée contre des mondes plantés dont la vérité est connue ; la vérité et le verdict restent hors de la machine qui exécute.
- Un arbitre formel en préparation : Lean 4 et Mathlib, sur machine isolée ; un harnais existe, l'outillage n'est pas encore relevé conforme.
- Budget : quelques centaines de dollars par course ; relecture humaine rare.

## Ce qui est déjà conçu

- Un pilote « oracles plantés » : des proposeurs d'énoncés jugés sur douze mondes mathématiques plantés à vérité calculée, tests de mort exacts, bras « suite bon marché » (calcul symbolique et numérique, contre-exemples) contre « lecture nue », juge de nouveauté éprouvé sur quarante énoncés connus plantés.
- Cinq questions cibles : clôture d'une archive pour un juge, plafond d'horizon, agrégateur sous corrélation adverse, lemme d'impossibilité, sonde qui ne lit que l'indication.
- Des visées d'attaque et de défense au niveau de l'idée : théorèmes d'impossibilité lus à l'envers, dont les hypothèses nommées sont les suppositions des moniteurs.

## Ce qui est annoncé ailleurs, non vérifié ici

Des annonces publiques récentes font état de résultats majeurs obtenus avec l'aide de systèmes d'IA (hypothèse de Riemann, équations de Navier-Stokes, dizaines de problèmes ouverts). Le programme ne les tient pas pour acquises tant qu'une preuve vérifiée et une source ne sont pas lues.
