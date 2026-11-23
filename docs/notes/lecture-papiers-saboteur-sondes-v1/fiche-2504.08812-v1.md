# Fiche de lecture — 2504.08812 v1 — « Mechanistic Anomaly Detection for "Quirky" Language Models »

- **Auteurs** : David O. Johnston, Arkajyoti Chakraborty, Nora Belrose (EleutherAI, Santa Cruz) ; arXiv 2504.08812 v1.
- **PDF** : `docs/sources/pdf/adjudant-opus-independant-v1/2504.08812v1.pdf`, sha256 `d8e3fb690110088f8300e1d97d75214517c6100e2c2a233c8bd64022fb20f46a` (recalculée, concorde avec le registre, R11).
- **Décision lue** : `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v1.md`, l. 87 (point 2, contre-indices à la pince) et l. 155 ; usage vérifié dans la v3 en vigueur (l. 96, corrigée ; l. 169 ; l. 217, « à citer quand le point est abordé »), non touché par ses errata 1 à 3.
- **Lecteur** : Claude Opus 5.5, effort élevé. **Date** : 2026-11-23T08:46:50Z.

---

**(a) Ce que le papier établit.** Détection d'anomalie sur les états internes, apprise sur des exemples faciles et sains, éprouvée sur des modèles affinés pour suivre une heuristique fautive quand le nom « Bob » paraît : Llama 3.1 8B et Mistral 7B (p. 3 du PDF). « No detector is effective across all models and tasks » (p. 1). Sur Llama, hors arithmétique, l'aire sous la courbe moyenne est partout sous 0,8, souvent près du hasard (p. 6). Les jeux faciles pour un détecteur le sont pour les autres ; corrélation des performances : 0,97 entre distance de Mahalanobis et facteur local d'aberration sur activations, 0,99 avec la distance L0 d'un autoencodeur creux, 0,60 avec un détecteur sur attributions (p. 7 ; figure p. 9 : 0,966, 0,989, 0,596). Joindre naïvement attributions et activations n'apporte rien (p. 8). Les anomalies sont des heuristiques fautives, « rather than intentional deception » (p. 2).

**(b) Ce que voulait la décision.** Un contre-indice : deux regards sur activations tombent ensemble. **Le permet en partie** : la v3 le dit exactement (corrélation de performances entre jeux et couches, non de pannes sous une même attaque). Il n'y a ni attaquant ni saboteur. Le fait de la page 8 soutient en plus l'énoncé « deux alertes réunies ne créent pas de puissance », que la décision ne lui attache pas.

**(c) Usage.** Pour l'entretien, objection « pourquoi pas une détection d'anomalie sans exemple d'attaque ? » : réponse honnête, faible et inégale selon le modèle, mesurée sur des modèles de 7 et 8 milliards de paramètres. Il fournit une base nommée, la distance de Mahalanobis sur activations, à mettre à côté des sondes non supervisées du programme, et l'épreuve « la seconde mâchoire est-elle une autre nature de trait ? » (attributions contre activations).

**(d) Plus petite action.** Ajouter la page 8 (non-gain de la jonction) à la citation de Johnston au point 2 de la prochaine version de N-075, et la page 2 (pas de tromperie voulue) partout où il sert de contre-indice. Coût : un quart d'heure, aucune dépense.
