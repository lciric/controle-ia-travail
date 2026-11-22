# Vérification de la correction de la v8m, v4

**Verdict : conforme.**

- Le code de la v8m n'a pas changé (empreinte 420394f9…).
- Le seul ajout de test_collisionneur_v9_v8m_v2.py est l'essai demandé (réponse vide finie en end_turn, sous --effort-max : aucun rejeu, aucune déclaration).
- Essais : 519 passés, 11 sautés.
- Le mutant J3 (rejeu aussi sur end_turn) fait échouer exactement cet essai ; sans mutant, tout passe.
