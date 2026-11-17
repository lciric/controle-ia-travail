# Confirmation de Bailey — instance arrêtée par Vast faute de crédit

Relevé de 17:14Z (champs techniques seulement, aucune note lue) :
- Vast : `credit` 0, `balance` −0,084 USD, `billing_failed` vrai (recharge automatique en échec depuis au moins 15:41Z ;
  alertes à Lazar à 15:41Z, 16:15Z, 16:46Z, 17:14Z).
- Instance 61049303 (machine 146915) : `exited` / `stopped`, arrêtée vers 17:12Z.
- Conduite (PID 7832 sur le poste 176451822, en marche) : run principal lancé 10:36:37Z ; sondages en échec depuis
  17:12:11Z (2 consécutifs à 17:13:12Z). Au bout de 30 sondages ou d'une heure, elle tient l'instance pour
  injoignable, arrête, tente le rapatriement ; instance arrêtée et transfert incomplet : **pas de destruction**
  (« reprise requise », `lanceur_v21._finir`).
- Poste Hetzner 176451822 : en marche ; non détruit (il poussera le bilan et la liste des répertoires).
- Tours complets du run principal : inconnus à ce stade (environ 16 à 18 attendus à ~1 400 s par tour) ; ils seront
  établis par le transfert.

Suite, recommandation consignée d'avance (mot du 17 novembre vers 09:45Z) : dès le retour du crédit (Lazar), reprise de
la lecture 38 pour transférer les journaux (pièces neuves contre-lues, R2) ; puis, si l'exécution compte moins de 20
tours complets, relance de la l. 371 dans `GO-2026-11-17-07` ; sinon, run tronqué lu au régime réduit (le verdict
retenu reste celui à 36 tours, § 3). Risque déclaré (§ 5 (c)) : Vast peut supprimer une instance arrêtée sous solde
négatif avant la reprise (journaux perdus : pas de verdict de confirmation). Aucune lecture de note avant la clôture.
