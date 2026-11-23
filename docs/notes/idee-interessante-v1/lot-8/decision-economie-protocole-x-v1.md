# Règle d'économie du protocole X, lot 8 (v1)

Pièce de travail (classe C), écrite le 2026-11-23 vers 19:10Z par la session chef d'orchestre du lot 8 (branche `idees/lot-8-chef-d-orchestre-v1`), sur le mandat GO-2026-11-23-31 et le point 18 des messages du directeur (`lot-8/messages-directeur-lot-8-2026-11-23-v1.md`, 0a18a98e…). Mesure qualitative par unités de proposition renvoyée à un sous-agent (limite de l'abonnement atteinte à 18:5xZ, reprise après 23:10Z) : la règle ci-dessous tient sur les faits mesurés par programme et sur la lecture de la structure des réponses ; elle sera confirmée ou corrigée par un erratum quand la mesure par unités sera rendue.

## 1. Demande approfondie appliquée à la question « comment baisser la facture sans sacrifier la rigueur »

1. **Ce qu'un expert ferait et qui n'est pas demandé.** Il chercherait d'abord où va vraiment l'argent et le temps, au lieu de couper au jugé ; il traiterait le choix des modèles comme un problème de portefeuille (valeur marginale par dollar, corrélation des erreurs), pas comme un vote ; il décorrélerait les voix par la famille plutôt que par le nombre ; il garderait un bras témoin pour savoir si la matière première aide ou oriente ; il fixerait une règle d'arrêt séquentielle (on retire un modèle dès que sa valeur marginale mesurée tombe sous un seuil) plutôt qu'un choix fait une fois pour toutes.
2. **Données brutes.** Les appels déjà faits : usage en jetons et durée (`reponses-google-v1/appel-*.json`), prix versés (`docs/sources/prix/page-prix-gemini-api-20261122T104129Z.html`, `page-prix-anthropic-docs-20261122T104128Z.md`), les réponses elles-mêmes, les journaux du collisionneur (`registres/depenses.md`), et les arrêts techniques (Argon en RECITATION, 22 novembre ; limite de 5 h de l'abonnement atteinte ce soir).
3. **Méthodes et outils.** Recouvrement lexical par programme (termes longs, trigrammes, références auteur-année ; script `mesure/recouvrement_v1.py`, versé à côté) ; appariement par unités de proposition et note de qualité des unités propres (en cours) ; coût par réponse calculé sur l'usage ; valeur marginale par dollar = unités propres fortes / coût.
4. **Validation hors de nous.** Le registre des idées de la veille de cap (une idée propre à un modèle a-t-elle été retenue et éprouvée ?) ; le bras témoin du collisionneur ; à terme, la part des propositions qui passent une épreuve préenregistrée, par modèle d'origine.

**Critères que le directeur n'a pas nommés, retenus et appliqués :** décorrélation des erreurs (famille différente plutôt que second modèle de la même famille) ; fiabilité technique (taux d'arrêt RECITATION, coupures) ; taux de références douteuses ; rareté du quota (la limite de 5 h de l'abonnement et le quota de Fable sont aujourd'hui plus rares que les dollars de Google) ; latence ; neutralité (chaque voix en plus est une occasion de fuite d'orientation) ; traçabilité (tout appel journalisé, rejouable).

## 2. Faits mesurés : Argon, Carbon, Neon

Deux questions, mêmes invites aux trois (idées intéressantes v1 ; suivi homomorphisme v1, Argon à sa relance).

| Mesure | Question 1 | Question 2 |
|---|---|---|
| Mots (Argon / Carbon / Neon) | 6 432 / 4 554 / 5 334 | 3 669 / 3 132 / 2 837 |
| Jaccard des termes longs, Argon-Carbon / Argon-Neon / Carbon-Neon | 0,45 / 0,40 / 0,42 | 0,38 / 0,36 / 0,43 |
| Jaccard des références, mêmes paires | 0,33 / 0,18 / 0,18 | 0,29 / 0,16 / 0,36 |
| Références propres (Argon / Carbon / Neon) | 20 / 26 / 29 | 6 / 8 / 14 |
| Part de l'union des références perdue sans Argon / sans Neon / avec Carbon seul | 0,20 / 0,28 / 0,49 | 0,13 / 0,31 / 0,44 |
| Coût de la réponse, USD (Argon / Carbon / Neon) | ≈ 0,24 / 0,34 / 0,54 | ≈ 0,15 (+ 0,11 de l'arrêt RECITATION) / 0,22 / 0,75 |

Prix : Carbon 2 et 10 USD par million de jetons (entrée, sortie réflexion comprise) jusqu'au 30 novembre, 4 et 20 ensuite ; Neon 3 et 15 ; Argon lu par programme à 2 et 10 sur la même page (à confirmer à l'œil). Lecture de la structure (titres et propositions en gras des trois réponses de la question 2) : le squelette est commun parce que la question l'impose (même verdict liminaire — l'homomorphisme strict est rejeté —, mêmes outils d'alignement, même réserve sur un Noether discret, mêmes risques de fuite) ; chacun porte une ou deux propositions centrales propres (Argon : esquisses catégoriques et faisceaux cellulaires, conservation cohomologique, effacement lexical ; Neon : détection endogène dans un seul domaine, isolement de Swanson, correction des comparaisons multiples, transport non équilibré).

**Conclusion sur les faits.** Les trois ne sont pas redondants au mot près (recouvrement des termes 0,36 à 0,45 ; des références 0,16 à 0,36), mais ils le sont sur l'ossature, que dicte la question. Argon est le plus proche de Carbon (les deux plus forts recouvrements de références avec Carbon) et le moins fiable (un arrêt RECITATION sur deux appels de la question 2). Neon est le plus éloigné des deux autres (le plus de références propres, aux deux questions) mais coûte 1,6 à 3,4 fois Carbon. La redondance utile à réduire n'est donc pas d'abord entre modèles de Google : c'est la seconde voix de la même famille, quand une voix d'une autre famille (Fable, Opus) répond déjà.

## 3. Règle retenue (appliquée au lot 8, révisable sur mesure)

1. **Carbon : toujours, et lu à part** (souhait du directeur), à l'effort le plus haut admis (« high »), sur chaque question neutre retenue.
2. **Argon : retiré par défaut** des envois de fond (le plus redondant avec Carbon, le moins fiable). Il reste disponible pour des tâches de forme courtes ou une relance technique.
3. **Neon : sur les seules questions d'exploration ouverte** (brainstorm, signaux, objets nouveaux), pas sur les questions de méthode fermée ou de recensement ; et retiré pour la suite du lot si, sur ses deux premières réponses du lot, la mesure par unités ne trouve pas au moins deux unités propres notées « fortes » par réponse (règle d'arrêt séquentielle, consignée).
4. **Une seule version neutre par axe, servie à tous** ; pas de reformulation par modèle. Le nombre de questions est le premier levier (le coût est proportionnel à questions × modèles) : on regroupe tant qu'une réponse de 3 500 mots reste profonde ; la réflexion ne sature pas (Carbon 15 000 à 23 000 jetons, Neon jusqu'à 43 000, sous 65 536), donc le découpage se fait par axe de fond, pas par crainte de troncature.
5. **Voix de familles diverses avant voix multiples d'une même famille** : Carbon (Google), Opus 5.5 et Fable 5.2 (Anthropic) suffisent à la décorrélation ; Opus et Fable en effort maximal passent par des sessions de l'abonnement (mot du directeur relayé par la mère, 18:59Z) ; la clé RR_ANTHROPIC_API_KEY_LUC seulement en repli, dans le plafond de 30 USD.
6. **Contre-lecture groupée** : Fable contre-lit, en une passe par question, la réponse de Carbon et celle d'Opus ; Opus contre-lit celle de Fable (croisement) ; la mère juge. Pas de contre-lecture par réponse isolée.
7. **Collisionneur** : bras principal et bras témoin appariés (même moteur, mêmes tours, même plafond par bras), sinon la comparaison ne vaut rien ; l'économie se fait sur le nombre de tours et d'espèces fixé au devis, jamais sur l'appariement.
8. **Ce qui n'est jamais coupé** : la version neutre et son test de neutralité ; la demande d'une expérience décisive avec prédiction chiffrée et ce qui la réfuterait ; les journaux d'appel (réglage, usage, défaut) ; la règle « une panne technique n'est pas un résultat ».
9. **Mesure continue** : chaque réponse du lot reçoit, à la contre-lecture, le compte de ses unités propres fortes ; le rapport unités fortes par dollar, par modèle, est versé au registre des idées ; la règle est révisée sur ces chiffres au lot suivant.

## 4. Coût attendu du lot 8 sous cette règle

Pour cinq questions neutres plus la question déjà servie du point 16 : Carbon ≈ 6 × 0,35 ≈ 2,1 USD ; Neon sur trois ou quatre questions ≈ 2 à 3 USD ; total Google ≈ 4 à 5 USD, sous le plafond de 10 USD. Fable et Opus par l'abonnement : 0 USD ; en repli sur la clé LUC, pire cas compté à `max_tokens` (128 000 jetons de sortie de Fable ≈ 5,1 USD par appel), d'où au plus cinq appels de Fable en repli dans les 30 USD. Collisionneur : sur devis.
