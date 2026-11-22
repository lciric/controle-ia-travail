# Contre-lecture de la v8n (4bd86e65…), v5

**Verdict : à corriger (deux bloquants, simples).**

Essais : 537 passés, 11 sautés.

Sur le dossier cible (lu par programme, journal et composition seulement) :
- la composition de la v8n à six espèces redonne le sceau de especes.json ;
- l'ajout de Fable 5.1 prend la lettre G et laisse ce sceau intact ;
- l'étage III est fini : l'absence de III.1-A est acceptée ;
- dépense de 16,27 USD, ligne du run de 100 USD, script v8d, donc --reprise exigé.

Ce qui tient :
- seule G part ; les cellules d'origine sont sautées ;
- les contrôles précèdent toute écriture ;
- les pièces absentes de III.3 sont déclarées ;
- le plafond porte sur la dépense totale ;
- la commande verifier liste l'ajout à part.

## Bloquants

1. --rejuger-essai, --accepter-absence et --accepter-motif restent admis avec --espece-ajoutee (l. 3560-3603).
   - Un rejugement écrit une cellule d'origine, et une acceptation change le journal d'origine.
   - Correction : refuser ces trois options avec l'ajout, avant toute écriture, avec un essai.
2. Sans --ligne-usd, l'ajout dépense sur la ligne du run d'origine (l. 2365-2378 : il reste 83,73 USD sur la cible).
   - Correction : exiger --ligne-usd avec --espece-ajoutee, c'est-à-dire une ligne propre, sur GO.

## Non-bloquants

- Préambule à sept propositions : acceptable, puisque les absences de III.3 sont déclarées. Il serait mieux d'ajouter une ligne qui dit que la proposition G est ajoutée après coup.
- devis ne chiffre pas l'ajout : à chiffrer pour le GO (devis --espece-ajoutee), sinon utiliser devis-reprise.
- Même sans l'option, etat.md gagne une colonne et chaque essai le champ ajoutee_apres_coup (valeur faux). Aucun envoi ne change.
- Une absence d'une cellule de G ne peut pas être acceptée : une porte fermée sur G est sans issue.
- Deux contrôles de verifier n'ont pas d'essai : l'empreinte d'origine (N11) et une cellule de G hors de l'étage III (N13).

## Mutations

15 mutations, 13 prises ; survivantes : N11 et N13.
