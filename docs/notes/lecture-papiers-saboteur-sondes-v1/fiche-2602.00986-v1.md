# Fiche de lecture — 2602.00986 — v1

- **Titre** : Sparse Reward Subsystem in Large Language Models (prépublication), dit « papier dopamine ».
- **Auteurs** : Guowei Xu, Mert Yuksekgonul, James Zou. **Identifiant** : arXiv 2602.00986 v2.
- **PDF** : `docs/sources/pdf/2602.00986v2.pdf`, sha256 `da004f53ff336b950bf51fb9a85fa424f5792579ac10dce45566ccb0e68e9039` (vérifiée par `sha256sum`, 25 pages).
- **Décisions lues** : `registres/go.md`, ligne 576 (GO-2026-11-20-45) ; `docs/decisions/decision-N-075-issue-plancher-et-deux-regards-v1.md`, ligne 88 ; puis la v3 (l. 54, 97, 104, 212) et ses errata 1 à 3, le 3 v2 primant (il ne touche pas ces lignes).
- **Lecteur** : Opus 5.5, effort élevé. **Date** : 2026-11-23T08:52Z (`date -u`).

---

## (a) Ce que le papier établit

Deux groupes épars de neurones, trouvés par sonde : « de valeur », qui prédisent la réussite attendue, et « dopamine », qui codent l'erreur de prédiction de récompense pas à pas (p. 1). Moins de 1 % des neurones suffisent (p. 4). Sur Qwen-2.5-7B, mettre à zéro 1 % de neurones de valeur dans une couche fait tomber l'exactitude de 75,2 % à 20,3 % en moyenne ; avec des neurones tirés au hasard, la perte n'est que de 0,6 point (p. 5). Confiance prédite avant la réponse : aire sous la courbe moyenne 0,67, contre 0,60 (sonde sur l'état entier), 0,52 (confiance dite) et 0,62 (**longueur de la question**) (p. 8) ; valeurs dites « moderate » (p. 4). Utilisés comme juge des étapes, les neurones dopamine donnent 77,8 % contre 72,2 % en décodage glouton (p. 9). Limites : récompense de l'environnement requise, rien sur tâches ouvertes, au-delà de 32 milliards de paramètres ni sous adversaire (p. 25).

## (b) Ce que la décision voulait, et si le papier le permet

Le GO voulait un moniteur boîte blanche ; la N-075 (v3, l. 97) attribue à ce papier « la réussite attendue lue dans les états internes et sa calibration ». **Le permet en partie.** La lecture de la réussite attendue est bien établie. **La calibration, non** : le papier ne rapporte que du pouvoir de séparation, et le mot « calibration » n'y figure pas. Le dilemme visé (réussite attendue haute, issue calculée en échec) n'y est pas testé : aucun saboteur. L'usage survit en v3, au point 1 (bras « papier dopamine ») et au point 2.

## (c) Usage pour l'entretien et le billet

Objection « sur une tâche floue, pas de récompense » : concéder, leur page 25 le dit ; ne pas présenter ce moniteur comme éprouvé hors des tâches vérifiables. **Base bon marché** : la longueur de la question (0,62), à battre par toute sonde de valeur. L'ablation de la page 5 est un gabarit d'épreuve pour les lentilles. Antériorité : la valeur lue dans des neurones épars est occupée.

## (d) Plus petite action

Deux corrections à la v4 de N-075. Remplacer « et sa calibration » par « et son pouvoir de séparation (aire sous la courbe, p. 8) ». Ajouter « longueur de la question » aux bases du bras, à vérifier dans son plan exploratoire. Au registre des papiers : du code exploratoire est écrit, non lancé. Quinze minutes, aucune dépense.
