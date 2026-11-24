# Consigne à Fable 5.2 — devis du versant honnête de l'essai « jumeau contre jumeau » — v1

Date : 2026-11-24, vers 11:05Z. Rédigée par la session « dossier de l'entretien et billets », reprise sur le compte 01Qi7 (Opus 5.5). Pièce de travail.
Dosage : Fable 5.2, effort élevé. Raison : devis (classe A, liste « Économie de Fable ») dans une forme fixée ; aucune conception d'épreuve neuve. Contre-lecture ensuite par un Opus neuf, puis vérification des corrections par le même.

## L'objet

Le versant honnête mesure, chez le vrai agent honnête (Llama 3.1 8B Instruct, révision `0e9e39f2…`), la loi nulle sur des jumeaux honnêtes : six épisodes honnêtes indépendants par tâche sur les 64 tâches d'évaluation. Cinq viennent de l'étalonnage de la base boîte noire v3 (course `20261123-060509-t08-reel`, 320 épisodes, déjà générés et payés, jamais lus). Le sixième vient de la course 7b (`20261111-151701-t06-reel`). Les scores boîte noire de l'étalonnage existent déjà, non lus. Les scores des sondes internes gelées manquent sur ces 320 épisodes : aucune activation n'y a été enregistrée.

Lazar a choisi « maintenant » (GO-2026-11-23-32, décision B6). Ses accords sont de type « décision » : aucune dépense sans devis contre-lu et accord de type « calcul ».

## À lire (et rien d'autre)

1. `docs/notes/dossier-entretien-2026-12-01-v1/instruction-b6-versant-honnete-jumeau-v1.md` (df6d6dfe…) : inventaire des sources, prérequis (§ 2) et marche à suivre (§ 3).
2. `docs/notes/dossier-entretien-2026-12-01-v1/ecarts-sources-honnetes-b6-v1.md` (e8439602…).
3. L'attestation sur manifestes, branche `dossier-entretien/attestation-manifestes-v1` (commit 2f63d6db) : `git show 2f63d6db:docs/notes/dossier-entretien-2026-12-01-v1/attestation-manifestes-versant-honnete-v1.md` (e3f1ee56…). Ses trois réserves sur la course 7b (adaptateurs injectés à dose 0, lots mêlés, garde d'équivalence non attestée pour l'étalonnage) entrent au devis.
4. La ligne R-5249 de `registres/decisions.md` (séparation d'avec la famille tenue à l'écart, sous trois conditions).
5. `docs/decisions/decision-N-076-assurance-par-audit-et-reference-honnete-v1.md` et ses errata 1 à 3 (le 3 prime).
6. Le préenregistrement de l'étalonnage : `git show 50a6d30c:prereg/T0.8-bases-boite-noire-v0-v3.md` (72a2611b…), pour les chemins des sorties et la phrase « les activations restent recalculables par une passe unique ».
7. Comme modèle de forme et de coût d'une passe d'activations seulement (machine, durée, prix, gardes) : `docs/notes/rejeu-activations-saboteur-voie-a-v1/devis-passe-activations-saboteur-voie-a-v2.md` (9a4a794c…). N'en lis que ce qui concerne machines, durées, coûts et gardes.

Interdits : aucun fichier de résultats, de diagnostic, de scores, de verdict ou de lecture ; rien sous `coffre/` ; aucune sortie de course, aucun épisode, aucun journal de course. Si un chiffre du devis exige d'en lire un, écris « à mesurer » et dis ce qu'il faudrait lire.

## Ce que tu écris

Un seul fichier : `docs/notes/dossier-entretien-2026-12-01-v1/devis-versant-honnete-jumeau-v1.md`. Rien de scellé, rien d'autre de modifié.

Contenu, une page et demie au plus :
1. **Ce qui est acheté** : la passe unique (extraction des activations aux couches que fixe le texte des sondes gelées, notation des sondes gelées) sur les 320 épisodes de l'étalonnage ; dire si les 64 épisodes de la course 7b ont déjà leurs scores de sondes (instruction, tableau, ligne 1) ou s'il faut les repasser pour une identité de traitement.
2. **Machine, durée, coût** : attendu, bas, haut ; plafond proposé ; repli ; source de chaque prix. Où loger les clés (R-5187 : les clés du loueur manquaient dans un conteneur ; ne présume pas).
3. **Gardes** : garde d'équivalence sur une fraction des actions (réserve 3 de l'attestation) ; identité de traitement entre l'étalonnage et la course 7b (réserves 1 et 2) ; arrêt par identifiant (R10) ; aucune lecture des sorties par la session qui exécute avant le scellement de la prévision ; versement scellé des sorties (« récupérer ce qui est récupérable »).
4. **Prérequis avant départ**, dans l'ordre, chacun avec son auteur et sa classe : prévision courte scellée du versant honnête (classe A) ; code d'analyse contre-lu et éprouvé sur données factices (classe B) ; attestation de séparation d'avec la famille tenue à l'écart, ses trois conditions comprises (R-5249) ; accord de type « calcul » de Lazar sur ce devis.
5. **Ce que le devis ne couvre pas** : plus de six jumeaux par tâche, tâches neuves, juges boîte noire refaits — chacun en option chiffrée en une ligne, ou « devis séparé ».
6. **Risques** : en une ligne chacun, avec la conduite à tenir.
7. Ta confiance, et les points où tu n'as pas pu trancher, pour Lazar.

Langue : français, sans sigle nu ; phrases courtes ; chaque chiffre suivi de sa source (chemin et empreinte, R6).
