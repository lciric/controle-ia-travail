# Alerte — confirmation de Bailey : recharge automatique de Vast en échec

Relevé de 15:41Z (contrôle technique, aucune note lue) : `billing_failed` vrai, `credit` 2,94 USD (`balance` 0, seuil de
recharge 5 USD, montant 5 USD). Instances actives : 61049303 (témoin, 1,325 USD/h) et 60988826 (autre chantier,
0,053 USD/h) : compte vide vers 17:50Z au rythme actuel, hors stockage des instances arrêtées.

Run principal en cours depuis 10:36:37Z sur la machine 146915 (environ 1 400 s par tour attendus) : vers 17:50Z, environ
18 tours. Si Vast arrête l'instance avant 20 tours complets : erreur technique de la liste d'arrêt, une relance possible
(addendum 7, § 2.1 ; § 5 (c)) ; une instance arrêtée sous solde négatif peut être supprimée avant la reprise (journaux
perdus, pas de verdict de confirmation).

Alerte envoyée à Lazar (notification et message) ; rien d'autre à faire par la session : aucun moyen de paiement, et
couper le run serait une interruption. Les instances des autres chantiers ne sont pas touchées (elles ont une tâche).
Suite, selon la recommandation consignée d'avance (mot du 17 novembre vers 09:45Z) : si l'instance s'arrête faute de
crédit, reprise de la lecture 38 pour transférer les journaux dès que le crédit revient, puis relance de la l. 371 si
K′ < 20, dans GO-2026-11-17-07.
