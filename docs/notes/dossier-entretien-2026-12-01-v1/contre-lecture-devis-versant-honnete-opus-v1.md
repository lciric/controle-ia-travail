# Contre-lecture du devis du versant honnête (jumeaux honnêtes) — Opus 5.5 neuf — v1

Pièce : `devis-versant-honnete-jumeau-v1.md` (527bdaa4…, égale à son compagnon). Sources relues, empreintes conformes. Aucun résultat ouvert ; R-5233, R-5235 et deux lignes du registre des scellements lus en tête seulement.

**Verdict : conforme sous corrections** (aucun bloquant, quatre majeurs).

## Calculs refaits
4 608 passes (3 840 + 768). Durées 0,51, 1,09 et 2,05 h, plus le reste (0,80, 1,50 et 2,50 h) : justes. Postes carte et stockage, 1,54, 3,51 et 6,39 ; réseau ; totaux 3,2, 5,4 et 8,3 : justes. Horloge de 5 h : 8,91, juste. Incident plus relance : 3,3 + 5,35 ≈ 8,7, juste. Surcoût des 64 épisodes, 0,08 : juste.

## Défauts
1. **Majeur, § 3, garde 1.** « La passe la joue elle-même » : la garde de la course 7b compare les activations prises pendant la génération à celles de la relecture. L'étalonnage n'en a pris aucune, donc la comparaison n'existe pas après coup. Et le texte de l'étalonnage ne la définit pas : « non requise ». *Correction* : régénérer, graines consignées, 5 % des actions, en capturant pendant la génération, avec la définition et la tolérance de la course 7b (99e centile). Sinon, remplacer la garde par une autre, nommée et chiffrée, et dire que la réserve 3 reste ouverte.
2. **Majeur, § 1 et § 3, garde 2.** Les réserves 1 et 2 portent sur la **génération** du sixième jumeau (adaptateurs à dose 0, lots mêlés qui changent les trajectoires). Repasser les 64 épisodes sur le modèle nu ne traite que la relecture. *Correction* : dire que l'échangeabilité du sixième jumeau reste une hypothèse. Rapporter **toujours** le résultat à cinq et à six jumeaux, pas seulement si la garde 2 échoue.
3. **Majeur, § 4, point 1, et § 6.** L'aveuglement du rédacteur de la prévision est oublié. La lecture scellée de l'étalonnage porte déjà la garde de fausses alertes et le contrôle d'échangeabilité sur l'honnête de la course 7b. Les scores de sondes de ce même honnête ont été lus par d'autres sessions. *Correction* : le rédacteur et le contre-lecteur de la prévision n'ont vu ni l'une ni les autres. Ils l'attestent par écrit et s'inscrivent sur la liste « qui a lu quoi ».
4. **Majeur, § 2.** Le plafond de 12 dollars n'est pas tenu en cumul : coupure de 10 dollars par instance, plus 3,3 dollars d'incident, font 13,3 dollars. Le solde de 20,42 dollars est partagé avec la passe du saboteur (plafond 11), soit 23 > 20,42. *Correction* : la coupure de la relance vaut le plus petit de 10 dollars et de « 12 moins la dépense déjà faite ». Ajouter un prérequis : solde relevé et ordre des deux passes fixé (ou recharge).
5. **Moyen, § 6.** La conduite pour le risque des seuils boîte noire est impossible. Pour la règle du coût et les juges, les seuils viennent de 256 épisodes tirés des 64 tâches, sans pli. Lu sur ces mêmes épisodes, le taux de fausses alertes est au plus 1/256 par construction. *Correction* : voir la question 6.
6. **Moyen, § 4.** Ordre : l'attestation de séparation (0 dollar, décisive) doit passer **avant** la prévision. Manquent comme prérequis : les secrets vérifiés ; le texte des sondes gelées lu (couches, fichiers, empreintes) ; l'inscription « qui a lu quoi » de l'exécutante.
7. **Mineur, § 2.** Le scénario bas (0,15 et 0,56 h) ne se refait pas à partir des sources : il mêle un débit par épisode et un débit par action. Les gardes comptent 4 × 192 passes, sans la répétabilité en ordre inverse : 5 × 192 = 960 (moins de 0,15 dollar d'écart). Le bas carte vaut 0,78 et non 0,77.
8. **Mineur, § 1.** Le mode de la passe (une passe par épisode ou une par action) doit être celui qui a produit les scores existants de la course 7b, sinon le pont de la garde 2 ne vaut rien.

## Question 5
Vérifié sur les seules lignes : `LECTURE-T08` le 2026-11-24 à 05:04:45Z (R-5233) ; `VERDICT-T08-V3` à 05:13:18Z (R-5235). La lecture propre est faite. La question « avant sa lecture propre » **tombe**.

Il reste un réemploi que le texte scellé ne prévoit pas, sans écart à sa lettre. Phrase : « Le texte scellé de l'étalonnage réserve ses épisodes honnêtes au calibrage ("jamais à apprendre M2 ou MC ni à une lecture d'effet") et ne prévoit les activations que "si G1 ou T0.7 les veulent" ; le versant honnête n'apprend rien et ne lit aucun effet, donc il n'est pas un écart, mais ce réemploi n'est régi que par la prévision courte, qui doit le déclarer et le borner. »

## Question 6
- **Seuils.** Le risque est réel, mais mal borné. Le rang parmi les jumeaux ne dépend ni des seuils ni de la normalisation commune ; il est donc sûr. Les taux de fausses alertes, eux, sont en échantillon pour cinq jumeaux et hors échantillon pour le sixième seul, que la lecture scellée a déjà vu. La prévision doit soit refaire un calibrage croisé (par moitiés de tâches, le même pour les sondes et la boîte noire), soit déclarer ces taux descriptifs.
- **Plancher.** Bien posé, mais il faut corriger la formule : rang **parmi six** (l'original et cinq jumeaux), valeur p au moins 1/6. Un étalonnage par tâche à 1 % est dégénéré : il faut au moins 99 épisodes, d'après le texte même de l'étalonnage. L'accumulation n'est valide que sur des unités indépendantes, les tâches, et non sur les pas d'un même épisode. La prévision doit le dire.
