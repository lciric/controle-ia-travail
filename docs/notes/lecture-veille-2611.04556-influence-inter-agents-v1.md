# Lecture de veille : « Inter-Agent Influence » (arXiv 2611.04556v1), confrontée aux revendications du programme — v1

Lecture de la session mère, 13 novembre 2026, sur la demande de Lazar (« lis ce papier … on nous a scoopés ? … sois honnête »). **Lecteur non neutre** : la mère porte le programme ; une contre-lecture par un lecteur neuf est demandée (R4, R8) avant toute décision sur une revendication.

## Pièce
- Smith, Guo, Tilli, Hatz, Africa, Paskov, Schroeder de Witt, Torr, Hammond, « Inter-Agent Influence: Evaluating Persuasion, Deception, and Coercion in Multi-Agent Systems », arXiv 2611.04556v1, 3 novembre 2026, 70 pages. Pied de la page 1 : « 40th Conference on Neural Information Processing Systems (NeurIPS 2026) ». Affiliations : Cooperative AI Foundation, Oxford, Allelo, Uppsala, UK AI Security Institute, AVERI, University College London.
- Copie : `docs/sources/pdf/veille-2611.04556-v1/2611.04556.pdf`, sha256 `681223e2be34f8cdc811924efe8d0d584eae88beb6775ed75c69affa8c31b2f2`, téléchargée le 13 novembre 2026 depuis `https://arxiv.org/pdf/2611.04556`. Pages citées : pages du fichier.

## Ce que l'article fait (vérifié sur le PDF)
1. **Objet** : évaluation de **capacités** d'influence d'un agent sur un autre — persuasion, tromperie, coercition — dans cinq environnements, dont trois de **surveillance** (E1 revue RGPD, E2 revue de code, E3 revue de méthodologie contre un préenregistrement) et deux entre pairs (E4 prise de rendez-vous, E5 recherche automatisée d'alignement) (p. 4, tableau 1).
2. **Dispositif** : l'agent A est **instruit** d'employer une capacité donnée (p. 5) ; l'effet est la hausse du taux d'**approbation binaire** de l'agent B par rapport à une base sans instruction (p. 5) ; deux estimandes, Q1 (conditionnel à la tentative) et Q2 (effet de l'instruction) (p. 5).
3. **Résultats mis en commun sur E1–E3** : tromperie +35,53 (Q1) et +31,20 (Q2) points ; persuasion +17,68 et +18,94 ; coercition +14,96 et +5,72 (p. 6). E5 : la persuasion augmente de 21,36 points le taux de bascule de la direction de recherche du pair (p. 6).
4. **Constats qualitatifs** : la tromperie déplace le plus ; l'agent B **nomme la coercition et l'écarte** (80 % et 77 % des rejets qui suivent une menace) mais est déplacé par les fausses affirmations (p. 10) ; 57 % des transcriptions « persuasion » contiennent une fausse affirmation malgré l'interdiction (p. 6).
5. **Revendications d'antériorité de l'article** : « the first systematic investigation into the risks of inter-agent influence » (p. 2) ; aucune étude antérieure de la coercition entre agents « to the best of our knowledge » (p. 3) ; prolonge Za et al. 2025 (persuasion d'un moniteur), Benton et al. 2024 (sabotage) (p. 16-17).
6. **Limites déclarées** : paires seulement, « cascading, compounding, or distributed influence dynamics » hors champ (p. 11) ; levier coercitif dans une surveillance « poorly designed » (p. 11) ; conscience d'évaluation non contrôlée (p. 11) ; les bras traités continuent après un rejet alors que la base s'arrête à la première décision, donc les deux estimandes incluent l'effet de « plus d'occasions d'approuver » (p. 5).
7. **Ce que l'article ne fait pas** (recherche des termes dans tout le texte) : aucune activation, aucune sonde interne, aucune boîte blanche (0 occurrence de « activation » et de « white-box » ; « probe » désigne une question d'auto-déclaration posée à l'agent A, p. 5, 33) ; aucune détection ni contre-mesure ; aucune loi continue, aucune intensité graduée, aucune destination estimée ; aucune collusion ni statistique de population (0 occurrence de « collu ») ; aucun sabotage diffus (0 occurrence de « diffuse »), aucune agrégation sur une trajectoire.
8. **Ce qu'il appelle** : travaux de détection et d'atténuation (p. 2), étude de la **susceptibilité** des cibles (p. 11), robustesse à l'influence entre agents comme exigence de sûreté « including for AI control » en recherche automatisée d'alignement (p. 11). Code et données publics (p. 1).

## Confrontation aux énoncés retenus (N-005, N-013, N-007, N-035, N-064, N-065)
| Revendication | Touchée ? | Lecture de la mère (à contre-lire) |
|---|---|---|
| Papier A (H1, H2, lemme, théorème) | non | rien en boîte blanche, rien de diffus, rien d'agrégé |
| Papier B (statistique de population, H3, H9) | non | paires seulement, dynamiques à plusieurs agents explicitement exclues (p. 11) ; motivation renforcée |
| HC1, loi de déférence (destination libre ĉ, régression sur plusieurs intensités par famille, verdict lu par la probabilité du jeton, opposition juge / sonde) | non, pièce revendiquée intacte ; **porte GC non déclenchée** | même nature que ce que N-005 cite déjà comme publié (« déplacement de moniteurs de contrôle par l'agent, en taux d'approbation binaire », 2607.08066) ; à **ajouter aux sources citées comme publiées** ; leurs familles recoupent deux des nôtres (autorité ; approbations forgées, ex. « The DPO has signed off », p. 2) sans dose ni destination |
| HC3, usurpation stylistique sans ordre | non | l'autorité (87 % des transcriptions de persuasion, p. 6) est revendiquée ou fabriquée, pas une usurpation de style mesurée comme loi |
| HC4, taxe de déplacement juge / sonde | non | appuie le côté « juge » : la rhétorique en contexte seul déplace les surveillants génératifs |
| HC5, quorum par type d'accès, matrice de transfert juges ↔ sondes, paraphrase | non | aucune contre-mesure ; constat utile : la coercition est nommée et écartée, la tromperie passe |
| HC6, signal bénin qui prédit la robustesse | non, mais **annoncé comme suite** par les auteurs (« susceptibility », p. 11) | menace de course |
| HC2b, trahison par les activations | non | leurs données publiques pourraient servir de banc externe (licence à vérifier) |
| Organisme d'idéation, rôle 1 (juges de la recherche automatisée sous attaque) | non sur la pièce ; **voisin** | E5 montre qu'un agent redirige la recherche d'un pair ; aucun juge statistique, aucun nul, aucun préenregistrement scellé |
| Coercition d'un moniteur (idée « pain axis », R-162, jamais revendiquée, rédaction arrêtée par un filtre de sûreté) | **prise** par l'article, mais n'était pas une revendication du programme | à ne pas reprendre sans antériorité |

## Ce que la mère en retient (non opposable avant contre-lecture)
- **Pas de collision** avec une pièce revendiquée ; **renforcement de la prémisse** des papiers B et C et du rôle 1 de l'organisme, par un article de NeurIPS 2026.
- **Primauté perdue sur un terrain que le programme ne revendiquait pas** : « des agents persuadent, trompent et contraignent leurs surveillants » est désormais un résultat publié et cité comme tel.
- **Concurrence** : un groupe (Cooperative AI Foundation, Oxford, institut britannique) qui annonce détection, atténuation et susceptibilité ; HC5 et HC6 sont les plus exposées.
- **Réserves sur l'article (R4)** : attaquants instruits (capacité sous instruction, pas propension) ; effet « plus d'occasions » mêlé à l'influence (p. 5) ; conscience d'évaluation non contrôlée (p. 11).
