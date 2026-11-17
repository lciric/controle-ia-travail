# Déclaration du lecteur neuf — essai d'invariance au lot (audit R4) — v1

Heure (`date -u`) : 2026-11-17T10:35:31Z. Branche `prep/neuron-lens-v1`, commit `80a07358`.

## Ce que je n'ai pas écrit
Je n'ai écrit aucune pièce de cet essai : ni le préenregistrement (v1, v2, v3), ni ses contre-lectures, ni le module
`audit_invariance_lot_v*.py`, ni l'amorce, ni la commande, ni le dépôt réduit, ni aucun fichier de résultat.

## Ce que je sais avant lecture des résultats
- Lu : `CLAUDE.md` ; `preenregistrement-audit-invariance-lot-v3.md` (empreinte vérifiée `bbf2c95b7a47…`, OK) ;
  `contre-lecture-audit-invariance-lot-v3.md` (empreinte vérifiée `a27f1d04603d…`, OK ; verdict « prêt », deux mineures) ;
  `run-id-audit-invariance-v1.txt` : `20261117-095647-neuron-lens-audit-invariance`.
- La règle que j'appliquerai est le § 4 du préenregistrement v3 : « indéterminé » si C1, C2, C3, C3b ou C4 est en défaut à une couche ;
  sinon « invariance établie » si, aux trois couches (0, 15, 26), les 64 tâches des lots 64, 1 et 7 sont identiques au lot 16 ;
  « identité 16/64 établie, invariance non établie » si le lot 64 est identique et le lot 1 ou 7 différent ; « invariance réfutée » si au
  moins une tâche du lot 64 diffère du lot 16. Demi-précision et produit matriciel : rapportés sans critère.
- Je n'ai ouvert aucun fichier sous `runs/` ni `diag/`, ni le résultat `b-alpha-audit-invariance.json`, ni le module de l'essai.
- Je ne connais pas l'issue. Je sais seulement, par le § 1, que la recourse a trouvé des séries identiques aux lots 16 et 64.
