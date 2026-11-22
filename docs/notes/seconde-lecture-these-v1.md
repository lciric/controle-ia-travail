# Seconde lecture de la thèse — quatre sources lues sur PDF (v1)

22 novembre 2026. PDF et empreintes : `docs/sources/seconde-lecture-these-v1/` (compagnons `.sha256`). Pages = pages du fichier PDF. PDF traités comme données non fiables.

## 1. Filler, Ker, Fridrich 2009 — lu
`filler-ker-fridrich-2009-square-root-law-markov-covers-spie.pdf` (actes SPIE, société internationale d'optique, 2009).
- Hypothèses (p. 3-4) : modification indépendante de chaque élément ; couverture = chaîne de Markov stationnaire du premier ordre, transitions ≥ δ > 0 ; système imparfait : une paire d'états consécutifs a une probabilité différente sous couverture et sous objet porteur (éq. 2-3).
- Théorème 1 (p. 5) : β(n)/√n → ∞, détection ; → 0, ε-sûreté ; → ε, sûreté asymptotique Cε² « pour une constante C ».
- Constante (p. 7) : la divergence de Kullback-Leibler est bornée par ½ C̃ ε², C̃ bornant sa dérivée seconde normalisée (renvoi à leur réf. 11) ; non explicitée, elle dépend de la chaîne et du plongement. Le détecteur (p. 5, éq. 4) compte les paires consécutives ; sa variance est bornée par l'oubli exponentiel de la chaîne (lemme 1, p. 8-9).
- p. 4 : un système qui préserve les statistiques du premier ordre est « probablement détectable par des dépendances d'ordre supérieur ».

**(a) Occupé.** La loi tient pour des couvertures markoviennes sous ces trois hypothèses ; la constante devient une borne liée à la courbure de la divergence. Limite : taux constant dans un objet, pas taux décroissant (p. 8).

## 2. Arias-Castro, Bubeck, Lugosi 2012 — lu
`arias-castro-bubeck-lugosi-2012-detection-of-correlations-arxiv-1106.1193v2.pdf` (Annals of Statistics 40(1), 412-435).
- Cadre (p. 2, éq. 1.1) : sous les deux hypothèses chaque composante est normale centrée réduite ; seule la covariance ρ sur un sous-ensemble S de taille k change. **Marginales identiques.** Un seul vecteur observé (p. 5) : aucun test par valeur propre maximale.
- Carré de la somme (p. 14-15, proposition 3.1) : nχ²₁ sous l'hypothèse nulle, (n + ρk(k−1))χ²₁ sous l'alternative ; puissant si ρk²/n → ∞, quasi optimal au régime **dense** k²/n → ∞, sans puissance si k²/n → 0, même à ρ = 1.
- Carré de la somme localisé (p. 17-18, proposition 3.4) : quasi optimal pour les intervalles.
- Test d'adéquation (p. 18-20, proposition 3.5) : histogramme des Φ(Xᵢ), maximum des effectifs par case ; quasi optimal au régime **rare** k²/n → 0, k/log n → ∞.
- Rapport de vraisemblance généralisé : sous-optimal pour les ensembles quelconques (p. 6, 17).

**(b) L'énoncé est contredit ; voisin à citer.** Une statistique bâtie sur les seules valeurs par pas — somme, donc moyenne ; histogramme, cousin du maximum — garde de la puissance quand seule la corrélation change, car sa loi dépend de la loi jointe. L'énoncé ne tient que pour une décision sur un seul pas ou pour l'espérance d'une statistique additive. Forme défendable : « une statistique dont la loi ne dépend que des marginales a une puissance égale au taux de faux positifs » — ce que ne sont ni la moyenne, ni le maximum, ni la somme cumulée d'une trajectoire.

## 3. Parrack, Attubato, Heimersheim 2025 — lu
`parrack-attubato-heimersheim-2025-black-to-white-arxiv-2507.12691v3.pdf` (version 3, janvier 2026, 39 pages ; lues 1-11 et 13-14).
- Mesure (p. 1-2, 5-6) : gain « du noir au blanc » = moniteur par modèle de langue recevant les scores de sondes jeton par jeton, moins le même moniteur sans eux. **Oui, gain d'un moniteur de sorties à qui l'on donne les scores de sondes.**
- Agent Llama 3.3 de 70 milliards de paramètres, sondes de Goldowsky-Dill et al. 2025 (p. 2, 5) ; moniteurs Claude Haiku 3.5 et Sonnet 3.5 (p. 5) ; en annexe, GPT-4o de base et affiné (p. 13-14).
- Unité : la réponse ; aucun cadre séquentiel ; aire sous la courbe de fonctionnement sur cinq jeux de tromperie (p. 3-4, 7).
- Chiffres (p. 7, tableau 3, moyennes) : boîte noire Sonnet 0,879 ; boîte blanche Sonnet, sonde par paires 0,925 ; moyenne seule de cette sonde 0,941. Portes dérobées dans le code : boîte blanche 0,776 contre 0,899 (p. 7-8). GPT-4o boîte noire : 0,831 (p. 14).
- Aucune analyse des cas manqués par la meilleure boîte noire ; GPT-4o est un moniteur de plus, jamais un contrôle sur ce reste.

**(c) Voisin à citer, différence nette :** l'énoncé conditionne sur les sabotages manqués par la meilleure boîte noire et y compare la boîte blanche à une seconde boîte noire d'une autre lignée ; Parrack et al. mesurent un gain moyen, sur la tromperie, réponse par réponse. Ce contrôle conditionnel : non trouvé dans les pièces lues.

## 4. arXiv 2606.10456 — lu
« The Distributed Detectability Band Against Marginal-Preserving Attacks », Zhang Qinqin et Gao Yuze, version 2, juin 2026, 11 pages (lues 1-9) ; `zhang-gao-2026-distributed-detectability-band-arxiv-2606.10456v2.pdf`.
- Proposition 1 (p. 3) : un moniteur dont la règle ne dépend que de la répartition empirique des scores (moyenne, maximum, queue des k plus grands, compteur de seuil) a une puissance égale au taux de faux positifs contre une attaque à marginale exactement préservée.
- Construction (p. 3) : copule gaussienne autorégressive d'ordre 1 ; dommage codé par l'autocorrélation élevée.
- Proposition 2 (p. 4) : test séquentiel du rapport de probabilités et autocorrélation consistants quand la longueur croît.
- Chiffres (p. 7, tableau 2, T = 300) : famille marginale, aire 0,48 à 0,54, puissance à 1 % de faux positifs 0,000 à 0,048 ; famille de corrélation, aire 0,79 à 0,97, puissance jusqu'à 0,688. Traces réelles (p. 8) : autocorrélation honnête 0,064 ; aire 0,59 à T = 24, 0,98 à T = 400.
- Réserve, notre lecture : la preuve pose la répartition empirique égale à l'honnête « par définition », faux à T fini ; leur moyenne affiche 0,048 de puissance à 1 % (p. 7), ce qu'explique la section 2.

**(d) Occupé** pour la version boîte noire et synthétique : sur des scores scalaires de moniteur, synthétiques puis réels, le contraste marginale contre corrélation est énoncé et mesuré. Hors de leurs pages : scores de sondes internes, dommage réel non additif, appariement à un jumeau honnête.
