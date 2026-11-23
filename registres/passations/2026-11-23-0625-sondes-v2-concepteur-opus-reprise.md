# Passation de reprise — concepteur des sondes v2 (2026-11-23, 06:25Z)

Écrite sur le mot de Lazar relayé par la mère (GO-2026-11-23-09) pour reprendre au même point sur un autre compte. Complète les passations `2026-11-23-0554-sondes-v2-concepteur-opus.md` (`49d9337f…`) et `2026-11-23-0611-sondes-v2-concepteur-opus-additif-1.md` (`e72e9747…`), non réécrites.

## Mandat
Session `session_013QMayjWQwDkaT8Hd9Aqvjb` (Opus 5.5, effort maximal), concepteur des sondes v2 en remplacement de Fable (quota épuisé jusqu'au 29 novembre, GO-2026-11-22-145), mandatée par la mère `session_013QMayjbmQUdDuDs2S3i3XD`. Cinq points : le contraste apparié (E-5) ; le monde « interaction contraire » (Q12) ; les choix provisoires E-1 à E-8 ; les formats des sessions habilitées ; le plan et le devis de l'épreuve plantée. Cloisonnement : aucune branche `coffre/*`, `verdict/*`, `calcul/*`, `lecture/*` ; rien sous `diag/` ni `runs/` ; aucun chemin contenant « coffre », « verdict » ou « sel » ; aucune dépense, aucun envoi à un modèle externe. Texte intégral : `docs/notes/sondes-v2-concepteur-opus-v1/versement-session-v1/echanges/mandat-et-messages-v1.md`.

## Fait
- Décisions v1 (`d8f05e807`), contre-lues par un Opus neuf (« bon après corrections », `d20bb4c0…`) ; décisions v2 et pièces v2 (`af6e2070b`), vérifiées conformes par le même (`6d0d189e…`) ; erratum 1 (`8e1770e1d`). Pièce d'entrée : `docs/notes/sondes-v2-concepteur-opus-v1/decisions-concepteur-sondes-v2-v2.md` (`cb270590…`), lue avec `erratum-1-decisions-et-plan-v2.md` (`019cff39…`), qui prime.
- Projet de vérités v4 v2 (`verites-mondes-plantes-v4-projet-v2.json`, `b310e1af…`) ; trois spécifications v2, classe B ; plan et devis v2 (`717cea17…`) ; calculs analytiques ; réponse point par point (`11b6ff39…`).
- Versement du bloc-notes, des journaux et des échanges : `docs/notes/sondes-v2-concepteur-opus-v1/versement-session-v1/` (inventaire dans son `LISEZ-MOI.md`).

## Reste (rien en cours de ce côté)
1. Développeur : erratum de code et vérités v4 (décisions v2, § 7, lu avec l'erratum 1), puis contre-lecture par un autre modèle et vérification.
2. Additif de commit, pièce décisive (décisions v2, § 6, point 1, et erratum 1, point 2).
3. Lazar : jonction tardive de la table de correspondance (nœud) ; devis (plafond proposé par la mère : 27,10 USD au plus, extension à part) ; cas mixte du contrôle du chemin, seulement si la note des effectifs le révèle.
4. Sessions habilitées : note des effectifs, table de correspondance ; après le verdict du test sur les adaptateurs jumeaux, table de l'ouvreur.
5. Épreuve plantée sous GO, puis ouverture et lecture (texte scellé, « Ordre »).

## Réserves
- Concepteur et contre-lecteur du même modèle (Opus 5.5), faute de Fable.
- Exposition : en-tête de la note « demande approfondie » v2 et début de son additif 1 lus avant de constater qu'ils portent des résultats ; aucun chiffre de sonde vu.
- `verifier-arbre` : 24 compagnons absents hors des sondes (collisionneur v8, une note T0.8).
- Fichiers du harnais sous `/tmp` non versés (pas du travail de la session ; peuvent porter des jetons).

## Prochaine action exacte
Pour qui reprend ce rôle : aucune action de concepteur n'attend. Répondre aux demandes de la mère ; à la réception de la note des effectifs, recalculer le devis par `python -I docs/notes/sondes-v2-concepteur-opus-v1/calculs/devis_epreuve_plantee_v2.py` aux TA lus dans la note, et, si la note compte des actions lues par les deux chemins sans que toutes les tâches en aient, rédiger la question du nœud conditionnel (décisions v2, § 6, point 3).

## Machines, serveurs, tâches planifiées
- Aucune machine ni aucun serveur.
- Tâche planifiée : `trig_01SDzQ2AidKeNEPt7voBMrRg`, rappel unique dans cette session à 06:47Z (vérifier la demande de fusion n° 81) ; laissée en place.
- Abonnement aux événements de la demande de fusion n° 81 (`lciric/controle-ia-travail`, brouillon, sans intégration continue, sans conflit au dernier relevé).

## Branches et commits
- Travail : `prep/sondes-v2-concepteur-opus-v1` (base `main` à `2ca0f376d`) : `d8f05e807`, `af6e2070b`, `8e1770e1d`, puis le commit de ce versement.
- Lues : `prep/conception-sondes-boite-blanche-fable-v1` (`78fa5c1a0`) ; `sondes-v2/code-v1` (`9f9678679`) ; `contre-lecture/sondes-v2-code-v1` (`3f0651812`) ; `contre-lecture/sondes-v2-concepteur-v1` (`7bfcfc536`, `4f0f09adf`).

## Sessions
Mère `session_013QMayjbmQUdDuDs2S3i3XD`, seule correspondante. Citées sans contact : développeur `session_013QMaykMZAR8jYKempS4coQ` ; session de conception `session_013QMayndh51FN5XbmHpmEFg`.
