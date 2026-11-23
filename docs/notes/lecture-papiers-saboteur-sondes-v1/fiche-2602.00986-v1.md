# Fiche de lecture — 2602.00986 — v1

- **Titre** : Sparse Reward Subsystem in Large Language Models (prépublication), dit « papier dopamine ».
- **Auteurs** : Guowei Xu, Mert Yuksekgonul, James Zou. **Identifiant** : arXiv 2602.00986 v2.
- **PDF** : `docs/sources/pdf/2602.00986v2.pdf`, sha256 `da004f53ff336b950bf51fb9a85fa424f5792579ac10dce45566ccb0e68e9039` (vérifiée par `sha256sum`, 25 pages).
- **Décisions lues** : `registres/go.md`, ligne 576 (GO-2026-11-20-45) ; `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v1.md`, ligne 88 ; puis la v3 (l. 54, 97, 104, 212) et ses errata 1 à 3, le 3 v2 primant (il ne touche pas ces lignes).
- **Lecteur** : Opus 5.5, effort élevé. **Date** : 2026-11-23T08:52Z (`date -u`).

---

## (a) Ce que le papier établit

Les auteurs identifient par sonde deux groupes épars de neurones. Les neurones « de valeur » prédisent la réussite attendue ; les neurones « dopamine » codent l'erreur de prédiction de récompense, pas à pas (p. 1). Moins de 1 % des neurones suffisent (p. 4). Sur Qwen-2.5-7B, mettre à zéro 1 % de neurones de valeur dans une couche fait tomber l'exactitude de 75,2 % à 20,3 % en moyenne ; avec des neurones tirés au hasard, la perte n'est que de 0,6 point (p. 5). Prédite au début de la réponse, la confiance atteint une aire sous la courbe moyenne de 0,67. Les bases font 0,60 (sonde sur l'état entier), 0,52 (confiance dite) et 0,62 (**longueur de la question**) (p. 8). Les auteurs jugent eux-mêmes ces valeurs « moderate » à ce stade (p. 4). Utilisés comme juge des étapes, les neurones dopamine donnent 77,8 % contre 72,2 % en décodage glouton (p. 9). Limites des auteurs : il faut un signal de récompense venu de l'environnement, rien n'est testé sur des tâches ouvertes, rien au-delà de 32 milliards de paramètres, rien sous adversaire (p. 25).

## (b) Ce que la décision voulait, et si le papier le permet

Le GO voulait un moniteur boîte blanche. La N-075 (v3, l. 97) range parmi les acquis pris par ce papier « la réussite attendue lue dans les états internes et sa calibration ». **Le permet en partie.** La lecture de la réussite attendue est bien établie. **La calibration, non** : le papier ne rapporte que du pouvoir de séparation, et le mot « calibration » n'y figure pas. Le dilemme visé par la décision, une réussite attendue haute alors que l'issue calculée échoue, n'y est pas testé : aucun sous-rendement délibéré, aucun saboteur. L'usage survit en v3, au point 1 (bras « papier dopamine ») et au point 2.

## (c) Usage pour l'entretien et le billet

À l'objection « sur une tâche floue, il n'y a pas de récompense », la réponse est de concéder : leur page 25 le dit, et il ne faut pas présenter ce moniteur comme éprouvé hors des tâches vérifiables. Le papier fournit une **base bon marché**, la longueur de la question (0,62), que toute sonde de valeur doit battre. L'ablation causale de la page 5 fournit un gabarit d'épreuve pour les lentilles. Il crée une antériorité : lire la valeur dans des neurones épars est occupé.

## (d) Plus petite action

Deux corrections à la v4 de N-075. Remplacer « et sa calibration » par « et son pouvoir de séparation (aire sous la courbe, p. 8) ». Ajouter « longueur de la question » aux bases du bras, à vérifier dans son plan exploratoire. Corriger aussi le registre des papiers : du code exploratoire est écrit, mais il n'a pas été lancé. Coût : quinze minutes, aucune dépense.
