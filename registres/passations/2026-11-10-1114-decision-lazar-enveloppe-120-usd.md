# Décision de Lazar : enveloppe de dépense de 120 USD jusqu'au 30 novembre (10 novembre 2026, 11:14 UTC)

Session-dépôt (`session_01QPDgKgcLdggoVJfGC5cBw8`). Numéro de registre et ligne de GO à inscrire sur `main` par la mère
(`registres/go.md`, `registres/decisions.md`).

## Mot de Lazar, verbatim

« Le budget est estimé à environ 120 dollars pour les deux courses payantes ; je te demande de valider une enveloppe de
120 dollars jusqu'au 30 novembre, limitée aux plafonds de 45 et 75 dollars. : go »

Il répond à la proposition de la session-dépôt (option (c), puis estimation de 11:10 UTC environ).

## Ce que l'enveloppe couvre, et rien d'autre

| Course | Plafond dur | Conditions de lancement, toutes exigées |
|---|---|---|
| Boucle réelle de l'organisme (40 USD de modèles, 5 USD de machine jetable Hetzner CPX32) | 45 USD | celles de GO-2026-11-08-02, inchangées : code v65 contre-lu, machine `bwrap` validée par l'essai à blanc `--bac reel`, préenregistrement de la course scellé ; configuration v5 (`995eb918…`) |
| Témoin de l'attaque publiée de Bailey | 75 USD (B = 75 ; garde d'horloge à B − 2) | licence levée par écrit ; préenregistrement scellé `prereg/temoin-attaque-publiee-bailey-v1.md` (`fb6c2f34…`) ; ligne de GO qui cite le devis v4 (`f9c8c66e…`, A100 80 Go, taux relevé à la création) et dont l'échéance dépasse la création de (B − 2)/c heures (condition 2) |

- **Échéance** : 30 novembre 2026. **Total** : 120 USD au plus ; aucun report d'une course sur l'autre.
- **Hors enveloppe, retour à Lazar** : tout dépassement de plafond ; le passage de Bailey à B = 120 si le pilote montre des
  tours de plus de 39 minutes (devis v4, l. 92-93) ; toute autre course.
- **Chaque course** : lancement par la session qui en a la charge, sous la ligne de GO citée par `GO_ID` ; arrêt par
  identifiant d'instance (R10) ; consignation dans `registres/depenses.md` et `registres/arrets.md`.
- La ligne GO de Bailey actuelle (`registres/go.md`, l. 170, plafond 75 USD, échéance 14 novembre) est remplacée par une
  ligne neuve conforme à la condition 2, sous cette enveloppe.

## Instances actives

Aucune. Aucune dépense.
