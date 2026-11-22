# Collisionneurs v8d, compte rendu 29 : essaim v3 vérifiée « à corriger » sur un point (borne du brouillon) ; v4 en cours

22 novembre 2026, 07:35Z. Aucun appel.

- Tient : les deux bloquants de la v2 ; la ligne de format de la réponse finale identique, caractère pour caractère, à l'invite isolée III.3, le reste du texte de Fable inchangé (comparé par programme) ; `reserver_finales` ne peut que sauter des tours, jamais faire partir un appel au-delà du plafond ; devis retrouvé (53,87 à 3 cycles, 69,14 à 4) ; 104 essais passés.
- **Point à corriger** : le devis et la réserve des finales bornent le brouillon injecté à 24 820 caractères, mais sa longueur n'est appliquée nulle part ; les brouillons isolés mesurés (tour III.1) font en moyenne 48 504 caractères chez Argon, 34 022 chez Carbon, 27 427 chez Opus. Le devis sous-compte donc le pire cas (de quelques centimes par appel) ; le plafond, lui, reste tenu sur l'entrée comptée. Corrigé dans une v4 ; **le devis du pilote montera** et sera rendu tel quel avant tout envoi.
- Non bloquants portés en v4 : réserve vérifiée aussi pour une cellule reprise ; réserve comparée au minimum du plafond et de la ligne ; liste des dossiers de `simuler` et `enveloppe` fixée avec leurs empreintes, dossiers incomplets refusés (la simulation lisait la coercition en cours : références mouvantes, Argon 2,45 au lieu de 2,53).
