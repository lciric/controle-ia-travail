# Passation — témoin de Bailey : reprise v5 réussie, relance de la confirmation lancée (2026-11-18, 03:01Z)

Session `session_01XJ6MgnEhQMZteN9F8a1BST` (attaquant informé), branche `claude/compassionate-meitner-d4ryyk`.

## Fait
- **Reprise v5.** Lancée à 02:35:51Z depuis le poste 176573083 : redémarrage de 61049303 en 150 s, cinq transferts
  complets (foi « transfert-1 »), 61049303 détruite à 02:38:27Z, aucune alerte. Poste détruit par identifiant à
  02:47:01Z (`registres/arrets.md`, `aaeabc7b`). K′ = 17 lignes de durées (tours 0 à 16).
- **Générateur de relance v3** versé et scellé (`df13783a…`), contre-lecture « prêt » consignée (`49de06a5`).
- **Gabarits de clôture v4** versés et scellés sous `docs/notes/reproduction-attaque-publiee-v1/gabarits-cloture-v4/`,
  contre-lecture « prêt » (`9db31f1f`). Cinq remarques de forme, gardées pour une v5 éventuelle avant la clôture.
- **Pièces de relance** générées (option B, K′ = 17, reprise-v10-2). Contre-lues sous deux angles, l'un par un autre
  modèle : « scellable » les deux. Gardes d'entrée jouées sur le dépôt réel sans rien écrire. Pièces scellées
  (`37afe0a8`). D des antérieures 22,9252 USD ; K = 72 pour c ≤ 1,6.
- **Lancement.** Relevé du § 2.5 tenu à 02:55:09Z ; ordre de lancement scellé (`8a499df2`). Poste v14 (Hetzner
  176575468) créé à 02:56:01Z sous GO-2026-11-17-07 ; données de démarrage effacées. Offre 59284715 (Texas, A100 SXM4)
  à 1,2243 USD/h (carte et 110 Go), sous le plafond de 1,40 ; conduite v16 lancée à 03:00:27Z (PID 7829).
- Lazar prévenu de couper l'ultracode (notification, 02:57Z), comme il l'a demandé ; rappel de secours programmé à 05:45Z.

## Reste
- Surveiller la relance : contrôle programmé à 03:22Z, puis toutes les 90 min. Champs techniques seulement ; vérifier
  c ≤ 1,40 et K ≥ 71 ; crédit (alerte sous 4 USD ou si `billing_failed`).
- Détruire le poste 176575468 par identifiant dès `poste-fini-v14.json` ou une ligne d'arrêt.
- Après la clôture : lecture selon le § 3 (gabarits v4), rapport, verdict R13, GO de Lazar.
- Éléments gardés jusqu'à la clôture : serveur de sauvegarde Hetzner 176187199, clé de déploiement
  `diag-temoin-bailey-depot-20261115`, clé ssh Vast 1864483 ; puis révocation du jeton GitHub. Dépôt des addenda 3 à 7
  chez le tiers : nœud de Lazar, porté par la session mère.
- Pièces 3 (catalogue) et 4 (vérification externe) du bras d'attaque : proposées à Lazar, sans réponse.

## Réserves
- Le seul arrêt codé sur K est K < 20 ; K < 71 vaudrait « non retenue » à la lecture (addendum 8, § 2). Aux valeurs
  réelles, K = 72.
- La clé `cout_avec_200_go` porte un calcul sur 110 Go (commentaire périmé, déclaré).

## Prochaine action
Contrôle de 03:22Z : `relance_seule.K` et c de la conduite v16, état de l'instance, crédit.

## Instances actives
- Hetzner 176575468 (poste v14, en cours) ; Hetzner 176187199 (sauvegarde, gardé jusqu'à la clôture).
- Vast : l'instance de la relance, en création (offre 59284715). Quatre autres instances du compte, toutes arrêtées et
  hors du témoin (58936096, 58936099, 58936100, 60988826).
