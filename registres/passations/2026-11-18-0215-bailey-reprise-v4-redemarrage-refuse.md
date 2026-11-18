# Témoin de Bailey — reprise v4 : redémarrage de 61049303 refusé par Vast

Champs techniques seulement, aucune note lue.
- Poste de reprise v4 (Hetzner 176569589) : créé 01:57:45Z ; inventaire conforme (61049303 seule instance du témoin,
  arrêtée) à 02:02:06Z ; reprise lancée (`lanceur_v21 reprendre`) ; terminée à 02:12:14Z, code 3 ; poste détruit par
  identifiant ensuite (`registres/arrets.md`).
- `sortie-conduite-v15/reprise-v10/bilan-reprise-v10.json` (scellé) : `statut` « exited » ; `redemarrage.debut`
  1794967330.637 (≈ 02:02:10Z), durée 18,4 s ; alerte « redémarrage refusé (GardeArret) : instance gardée arrêtée ;
  nœud » ; `detruite` faux. Aucun transfert ; liste des répertoires du dossier de reprise : 0 entrée.
- La commande de démarrage de `vastai` n'a pas rendu la ligne de succès attendue. Relevé à 02:16Z : 61049303 `exited`,
  état voulu `stopped` ; la machine 146915 n'a **aucune offre** (recherche d'offres par `machine_id=146915`) : sa carte est
  vraisemblablement louée à un autre client ; une instance arrêtée ne redémarre qu'une fois sa carte libre (lecture de la
  session, non établie). Le disque de l'instance reste conservé (stockage facturé, 0,1528 USD/h).
- Dépense de la reprise : redémarrage refusé, aucune heure de carte.
Conséquence : les journaux de la première exécution de la confirmation ne sont pas transférés ; la relance (addendum 8,
plafond 1,40 USD/h) ne peut pas partir par le chemin scellé (`relance_seule()` exige les journaux de la reprise). Nœud
soumis à Lazar.
