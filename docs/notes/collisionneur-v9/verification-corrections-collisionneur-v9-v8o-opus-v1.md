# Vérification des corrections de la v8n dans la v8o (81c1ca22…), v6

**Verdict : conforme. Aucun bloquant.**

Essais : 545 passés, 11 sautés.

**Corrections portées :**
- les trois options sont refusées avec l'ajout, avant toute écriture ;
- --ligne-usd est exigée ;
- la ligne « ajoutée après coup » est dans les invites de la proposition ajoutée ;
- devis --espece-ajoutee chiffre l'ajout (sans relance, puis avec relances au plafond de relance) ;
- les mutants N11 et N13 sont maintenant pris.

**Porte fermée sur une cellule de la proposition ajoutée : non bloquant.**
- Ce défaut est sans risque d'argent : rien ne part ensuite.
- Si l'arbitre veut une issue : une acceptation d'absence réservée aux cellules de la lettre ajoutée, journalisée.

**Non bloquant :** aucun essai ne fixe le chiffre exact du devis de l'ajout. Deux mutants survivent (O6, absences hors du compte ; O7, relance chiffrée au premier plafond). Les gardes à l'envoi tiennent ; ajouter un essai qui fixe le chiffre.

**Mutants : 22 rejoués, 20 pris.**
