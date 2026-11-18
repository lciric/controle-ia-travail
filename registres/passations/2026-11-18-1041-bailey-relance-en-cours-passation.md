# Passation — témoin de Bailey, relance de la confirmation en cours ; pièces 3 et 4 du bras d'attaque (2026-11-18, 10:41Z)

Session `session_01XJ6MgnEhQMZteN9F8a1BST` (attaquant informé), branche `claude/compassionate-meitner-d4ryyk`. Demande de
Lazar, relayée par la session mère à 10:42Z : tout committer et pousser, avec une passation à jour. La session mère
passe sur un autre compte ; la surveillance de cette session continue telle quelle.

## État de la course (champs techniques seulement)
- **Relance de la confirmation** : conduite v16, poste Hetzner v14 176575468, instance Vast 61170458 (étiquette
  `temoin-bailey-c6-845f37c35eba4a3d`, machine 146917, offre 59284715), c = 1,2194 USD/h, K = 72, K′ = 17.
  - `principal-relance` lancé à 03:13:41Z ; fin attendue vers 04:30Z le 19 novembre.
  - À 10:38Z : instance en marche (états réel et voulu « running ») ; aucune marque de fin ; aucune ligne d'arrêt.
- **Crédit Vast** : 42,02 USD à 10:38:47Z, billing_failed faux.
  - Recharges manuelles de Lazar : +24,97 USD vers 07:20Z et +19,96 USD vers 07:39Z (GO-2026-11-18-18 ; course sous
    GO-2026-11-18-08).
  - Besoin restant de la relance : environ 1,32 USD/h jusqu'à 04:30Z, soit environ 23 USD.
- **Règle de repli B′**, mot direct de Lazar « fais le repli B' au bon moment pour sauver les donenes » ; note
  `2026-11-18-0630-…`. Elle est armée en filet :
  - B′ part si le crédit retombe à 2,6 USD ou moins, ou sous 2,2 USD en toute heure, ou si 61170458 n'est plus en marche ;
  - procédure `docs/notes/reproduction-attaque-publiee-v1/procedure-repli-relance-bailey-v1.md`, § 2 ;
  - pièces de reprise v7 scellées (commit `978f1b05`), option B (pièces v6) en secours ;
  - GO-2026-11-18-09 et GO-2026-11-18-12.
- **Surveillance** : boucle shell `scratchpad/surveiller-credit.sh`, relevé toutes les 2 min, journal
  `scratchpad/journal-credit.txt`. Elle sort au seuil, à une recharge, si l'instance s'arrête, ou toutes les 115 min, et
  elle est réarmée à chaque sortie. Le bloc-notes n'est pas dans le dépôt : un redémarrage du conteneur l'a déjà arrêtée
  une fois (07:14Z), et elle a été réarmée.
- **Rappel programmé** : 14:00Z, contrôle de la relance et vérification que la surveillance tourne.

## Fait aujourd'hui depuis la passation de 03:01Z
- Relance : contrôles conformes. Débits relevés et expliqués : téléchargement unique du modèle 1,98 USD ; instances
  d'autres sessions, E5 et l'expérience 1 de « Raisons ou regard ? », signalées à la session mère.
- **Bras d'attaque, pièce 3** : catalogue des procédures publiées (échelon 3)
  - v1 scellé (`a267b724…`, commit `1844c9e3`), après contre-lecture 3 et vérification ; erratum d'heure à part ;
  - v2 scellé (commit `616242e4`) : question 4 tranchée par Lazar en (b), échelon à part (R-3185 de la session mère).
- **Bras d'attaque, pièce 4** : plan de vérification externe v1 (`d3991222…`) et projet de courriel v4 (`3f1121f5…`),
  scellés (commit `565a6513`) après contre-lecture 3 et vérification. Courriel non envoyable : 18 points « À décider »,
  11 « À remplir ». Résumé en clair envoyé à la session mère pour Lazar.
- **Repli** :
  - plan de sauvegarde ;
  - pièces de reprise v6 (option B, commit `51035c07`) et v7 (B′, commit `978f1b05`), contre-lues ;
  - procédure du repli ;
  - B′ décidée (GO-2026-11-18-12), puis « au bon moment » (mot direct), désarmée par les recharges et gardée en filet.

## Réserves
- B′ (contre-lecture C4) : le code figé ne vérifie pas la reconstitution d'état. Si elle échouait, la lecture rendrait
  « Non interprétable ».
- B (contre-lecture C7) : sans état reconstitué, la course serait non interprétable. C'est pourquoi B′ est préférée.
- Régime sobre jusqu'au 22 novembre (limites d'usage) : aucun sous-agent hors nécessité du repli.

## Prochaine action
Laisser la relance finir (vers 04:30Z le 19). Puis :
1. détruire le poste v14 par son identifiant dès `poste-fini-v14.json` ;
2. vérifier la destruction de 61170458 ;
3. faire la lecture de clôture selon l'addendum 7, § 3, avec les gabarits de clôture v4.

## Instances et serveurs actifs (relevé de 10:40Z)
- Vast : 61170458 (relance de Bailey, en marche) ; quatre instances arrêtées hors témoin (58936096, 58936099, 58936100,
  60988826).
- Hetzner : 176575468 (poste v14, en cours) ; 176187199 (sauvegarde, gardé jusqu'à la clôture).
