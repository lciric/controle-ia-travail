# Collisionneurs v8d, compte rendu 22 : mode essaim écrit (v9-essaim v1), en contre-lecture ; devis du pilote : nœud

22 novembre 2026, 06:12Z. Aucun appel.

**Code** (Opus 5.5, classe B), `docs/notes/collisionneur-v9/essaim-v1/` : `collisionneur_v9_essaim_v1.py` (c2db738c…), essais (0d997f28…, 24 passés, rejoués par moi), configuration du pilote (a7b783fc…, enveloppe vide : `lancer` refuse tant qu'elle n'est pas reportée du dossier isolé), rapport du développeur (3373b36f…). Importe la v8d telle quelle ; chaque appel passe par son `executer_cellule`. 13 mutations prises. Contre-lecture par un Opus neuf en cours.

**Devis du pilote** (question générale, cinq modèles, quatre cycles, enveloppe supposée 15 USD) : **63,58 USD au pire sans relance** (temps 0 : 8,17 ; temps 1 : 44,58 ; temps 2 : 10,84) ; 166,26 avec relances ; dépense mesurée bornée à 87,68 par les parts. **Au-dessus du plafond de 45 par dossier : nœud.** Cause : 30 appels (5 brouillons, 20 de cycle, 5 finaux), chacun au plafond de sortie de la v8d (la garde de Google interdit de le baisser), contre 15 en mode isolé.

**Conséquence de fond, à trancher par Fable (budget égal, classe A)** : avec une enveloppe égale au coût mesuré du mode isolé (~15 USD), les parts par agent (0,75 / 1,65 / 0,60 USD) laissent aux modèles chers un ou deux appels de cycle sur quatre ; beaucoup de tours seront sautés (journalisés « part épuisée »). Options : (a) moins de cycles (deux) ; (b) budget égal en mots de texte plutôt qu'en dollars ; (c) enveloppe plus large que l'isolé, déclarée ; (d) pilote tel quel pour mesurer.

**Choix du développeur à trancher** (détail dans le rapport) : part contrôlée sur le coût mesuré ; ordre séquentiel fixe par cycle (un agent voit ses prédécesseurs du même cycle) ; textes sans auteur sauf les salons ; limites non fixées par Fable (revue 400 mots, erratum 150, six textes ouverts par cycle, 3 000 mots par appel de cycle) ; **en-tête, consigne des cycles et consigne finale écrits par le développeur : à faire écrire par Fable**.
