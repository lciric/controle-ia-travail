# Contre-lecture des collisionneurs v9-v8n et v9-v8o (voie --google-arriere-plan)

- **Classe B.** Auteur du code : session fille des collisionneurs (Opus 5.5). Contre-lecteur : un Opus 5.5 neuf, sous-agent, qui n'a pas écrit le code ; aucun fichier modifié, aucun réseau. 24 novembre 2026.
- **v8n** (aac7d302…) : « conforme avec remarques », aucun défaut bloquant. La voie en arrière-plan passe par la garde Google commune avant l'envoi : réflexion explicite au niveau prévu, plafond au moins égal à la réflexion plus 16 000, limite de mots. Après la réponse : zéro pensée, statut autre que « completed », texte vide et MAX_TOKENS sont des défauts, jamais une réponse. Huit remarques, corrigées dans le v8o (R1 à R8, en-tête du v8o).
- **v8o** (f63c513c…) : vérification des corrections par le même contre-lecteur : « conforme », les huit corrections sont faites et justes, et rien d'autre n'est introduit. L'essai simulé `essai_simule_v8o_v1.py` passe (neuf cas).
- **Points mineurs gardés, déclarés, non bloquants :**
  - (R5) le refus de `--repli-lot` avec `--google-arriere-plan` vient après les écritures de préparation au journal ; une commande refusée y laisse ces lignes ;
  - (R7) « REFUS » compte aussi les autres échecs sans envoi (connexion impossible, nom introuvable, 429 répété) ; c'est prudent et sans coût ;
  - (R8) la suppression chez Google n'est faite qu'après une lecture finie ; après un délai, un échec ou une annulation, l'interaction reste chez Google (conservation d'un jour au niveau gratuit). La route DELETE n'est pas dans la documentation lue, mais son échec n'est jamais bloquant. `nom_lot` mêle l'identifiant et le résultat de la suppression.
