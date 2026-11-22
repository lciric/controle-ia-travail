# État des deux dossiers « conscience et anesthésie » à la pause (v1)

Écrit à 2026-11-22T17:02:58Z. Classe C. Ordre de Lazar relayé par la mère (16:57Z) : pause jusqu'à la réinitialisation de l'usage hebdomadaire de l'abonnement (vers le 29 novembre, 02:00Z) ; aucune cellule neuve, aucune vague neuve. Accord : GO-2026-11-22-78 (50 USD par dossier, échéance le 30 novembre ; relance sur le mot GO-2026-11-22-96). Moteur v8m par `voie_abonnement_v5.py` (effort xhigh), `vague_abonnement_v1.sh`.

## Dossier 1, question neutre
`runs/collisionneur-protocole-x-conscience-anesthesie-neutre-abonnement-v1-20261122-153110`
- Premier tour (conception) : Fable (abonnement, versé), Argon, Astra, Carbon (deuxième essai, le premier coupé en flux et compté au pire), Neon : cinq cellules écrites, sceaux vérifiés.
- En suspens : Opus du premier tour (kit E3-T1-conception-B, branche `kits-abonnement/conscience-anesthesie-neutre-abonnement-B-v1`, texte servi cffbe283…). Session fille session_013QMaynL98qjZuujME9m8nv créée à 16:51Z, interrompue par la mère : sa réponse n'est pas versée. À la reprise : session neuve, ou recueil v6 de celle-ci si son premier tour est complet.
- Puis tours deux (critique croisée) et trois (réponse) entiers.
- Dépense : 4,18 USD sur 50 (journal). Un refus avant envoi (passage par l'interface de lot refusé par la règle du plafond large, rien envoyé, option retirée).
- Dernière vague : arrêt code 2 (porte fermée, kit d'Opus en attente), 17:02:38Z.

## Dossier 2, version 3 avec réserve
`runs/collisionneur-protocole-x-conscience-anesthesie-v3-reserve-abonnement-v1-20261122-153110`
- Premier tour : Fable (abonnement, versé), Astra, Carbon (deuxième essai, OK, 0,73 USD) : trois cellules écrites, sceaux vérifiés. Argon : refus RECITATION, définitif ; absence acceptée par l'arbitre (GO-2026-11-22-97), à passer par `--accepter-absence E3-T1-conception-C` à la reprise.
- En suspens : Neon du premier tour (jamais envoyé : la vague a été arrêtée par PID 1105 à 16:59:23Z, juste après la sortie de Carbon, sur l'ordre de pause) ; Opus (kit B, branche `kits-abonnement/conscience-anesthesie-v3-reserve-abonnement-B-v1`, texte servi 0ed87c51…), session fille session_013QMaynhPZnMWENZdeWwtDn interrompue par la mère, non versée.
- Puis tours deux et trois.
- Dépense : 3,61 USD sur 50 (journal). Le tableau `etat.md` est périmé (arrêt avant sa régénération : il montre Carbon « interrompu », 2,89 USD) ; le journal fait foi, la prochaine commande le régénère.

## Commande de reprise (rien d'autre à changer)
`bash docs/notes/collisionneur-v9/reprise-v8d-v1/vague_abonnement_v1.sh v8m DOSSIER DOSSIER/question-etage3.md GO-2026-11-22-78 xhigh 50 --fable --opus --argon --astra --carbon --neon --sortie-max --reprise` ; pour le dossier 2, ajouter `--accepter-absence E3-T1-conception-C`. Ne pas passer `--repli-lot` (refusé par la règle du plafond large pour Carbon).
