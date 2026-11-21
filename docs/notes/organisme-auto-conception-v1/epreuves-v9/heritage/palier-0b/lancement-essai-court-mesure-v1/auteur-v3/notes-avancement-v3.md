# Notes d'avancement — auteur v3 du lanceur et du gardien, palier 0b, essai court (au fil de l'eau)

- 2026-11-21 vers 17:12Z : erratum 2 (68faf068…3848) vérifié par `sha256sum` et lu ; vérification v2 et ses essais lus en entier.
- Pièces qui changent : `gardien-essai-court-v3.py` (corrections 1 et 2) et `demarrer-gardien-essai-court-v3.sh` (nom du gardien lancé, seul changement). Inchangées, copiées à l'octet dans ce dossier pour un rejeu autonome : `lancer-essai-court-v2.sh`, `demarrer-essai-court-v2.sh`, `verifier-commande-v2.py`, les deux extractions du complément.
- Essais à l'essai (17:14–17:15Z) : chef tué, descendant qui finit seul (garde continuée, fin quand tous absents) ; chef tué, descendant sous seuil de place factice (arrêt en mode descendants, témoin intact) ; orphelin de la vérification : « dossier NON figé » après 10 paires (n 53 puis 58), B arrêté par moi.
- Rejeu complet : `essais/rejouer-tout-v3.sh final` (base tirée de l'emplacement du script ; n'écrit que sous ce dossier).
