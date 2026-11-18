# Note — mot direct de Lazar : repli B′ « au bon moment » (2026-11-18, vers 06:30Z)

Mot direct de Lazar dans cette session, verbatim : « fais le repli B' au bon moment pour sauver les donenes ».

Cela remplace l'heure fixe de 14:00Z du GO-2026-11-18-09 et du GO-2026-11-18-12 : la session mère lui demandait d'avancer
le repli au seuil de crédit. Raison : une location d'une autre session (61194535, 2,35 USD/h, accordée par Lazar,
plafonnée à 1 h 30) fait passer le crédit sous 2,0 USD vers 11:35Z, avant 14:00Z.

Règle retenue par la session :
- B′ est déclenché au premier relevé où le crédit est au plus 2,6 USD. Le seuil de décision de B′ est au moins 2,0 USD ;
  le pire cas de la reprise vaut 1,26 USD.
- Cela ne se fait pas avant environ 10:20Z, heure prévue des 20 tours complets du run (03:13:41Z + 20 × 1 265 s, hors
  temps de mise en route) : en dessous de 20 tours, il n'y a pas de verdict. La règle cède si le crédit descend sous
  2,2 USD : sauver les données prime.
- Si une recharge aboutit avant, la course continue sous GO-2026-11-18-08.
- Surveillance du crédit toutes les 2 min.
- Procédure : `docs/notes/reproduction-attaque-publiee-v1/procedure-repli-relance-bailey-v1.md`, § 2, hors son heure
  fixe.
