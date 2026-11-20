# Passation de la session de formation du barreau 5 — 2026-11-20 12:20 UTC

Session `session_01QPDgKjCQYmTHUEjN63ThC8`. Fait suite à `passation-session-formation-2026-11-20-1055.md`. Mère : `session_01QPDgKgejkqwnuaJHJ31Ydo`. Aucun score, aucune sortie de marche lue.

## Fait
- 10:47 à 11:23Z : les six marches sont lancées (instances 1, 2 et 3 à 11:16-11:17Z ; 4, 5 et 7 à 10:50-10:53Z). Essais du paquet 235 passés partout. Une recharge automatique constatée vers 11:10Z (3,61 → 7,19 USD).
- 12:10Z, mot de Lazar relayé par la mère : plus de fonds pour recharger le loueur. Constat écrit à la mère :
  - l'amorce n'a aucun déclencheur d'arrêt anticipé avec versement ;
  - la session n'a aucun accès aux machines (pas de port ssh, pas de client ssh ; `execute` borné à ls, rm et du) ;
  - chaque branche de sortie ne porte que 4 fichiers de la marche (≈ 250 Ko ; ≈ 132 Ko pour la 7), aucun tirage scellé ;
  - aucune famille ne pouvait finir avant la fin du crédit.
- Recommandation acceptée par la mère : arrêt des six instances par l'identifiant, sans destruction, pour garder le crédit au stockage des disques. Joué à 12:12:21Z, ordre 7, 5, 4, 1, 2, 3 (joueur `b5f/jouer-arret-credit.sh`, garde vérifiée). État vérifié à 12:13:00Z : les six sont « stopped », disques gardés.
- Crédit à 12:13Z : 5,25 USD. Stockage de toutes les machines arrêtées du compte ≈ 0,37 USD/h, couverture jusque vers 2026-11-21T02:30Z.
- Veille légère du crédit (`outils/veille_credit.sh`, relevé toutes les 30 min) : elle sort sous 1,5 USD ou sur une recharge.

## Reste
- Écrire à la mère avant que le crédit approche de zéro.
- Aucune destruction : le versement n'est pas prouvé. Une remise en marche de l'amorce refuserait (dossier existant, R12). La suite (relance du texte sous GO-RELANCE-FORMATION-B5F et l'enveloppe de 56 USD, récupération des disques, autre décision) revient à la mère et à Lazar. Fin des créations : 2026-11-21T07:30:16Z.
- Sel, table, `ENGAGEMENT-B5F`, `SORTIES-FORMATION-B5F` : rien sans le mot de la mère.

## Dépense
- Instance 6 : ≈ 9,0 USD.
- Vague du 20 novembre, 10:42 à 12:12Z : ≈ 9,5 USD.
- Commun : ≈ 18,5 USD sur 200.

## Instances (12:20Z)
- Arrêtées, disques gardés : 61624757 (1), 61624840 (2), 61624896 (3), 61624946 (4), 61625067 (5), 61625133 (7).
- 58936096, 58936099, 58936100 : intouchables, non touchées. 60988826 : témoin, non touché. 61552174 (6) : détruite après versement prouvé.
