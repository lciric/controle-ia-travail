# Mandat d'un Fable neuf : avis sur le modèle de l'expérimentateur d'épreuve (nœud N4) — v1

Écrit par l'organisme à 2026-11-22T15:27:41Z (date -u), sur la demande de la mère (15:22Z), sous GO-2026-11-21-43 (échéance 2026-11-23). Session de l'abonnement, créée par la mère ; Fable 5.2, effort maximal ; aucune dépense, aucun appel à une API de modèle.

## Ce qui existe déjà (à ne pas refaire)
Le 21 novembre, un Fable 5.2 neuf a écrit l'avis v1 (`avis-fable-et-externes-v1.md`, 18a3883d…), avec la voix de Carbon (Sonnet 5.5, confiance 0,78). Il est **non contre-lu et incomplet** : l'appel d'Astra a échoué faute de crédit sur l'ancienne clé. L'organisme sert aujourd'hui Astra (gpt-6.2-astra, clé OpenAI 2, par lots) sur **le même énoncé neutre** (cf566995…). Carbon n'est pas resservi : même énoncé, réponse déjà scellée.

## Ta tâche
1. Contre-lire l'avis v1 : vérifier chacun des faits F1 à F9 sur sa pièce, ligne citée ; dire pour chacun « tient », « faux » ou « non vérifiable ici », avec la ligne lue.
2. Lire la réponse d'Astra (pièce 8 ci-dessous) et la résumer comme le § 4 de la v1 résume Carbon : recommandation, confiance, voie, conditions de changement, failles, réserve de lignée.
3. Écrire l'**avis v2** (nouveau fichier ; la v1 reste intacte) : verdict en une à trois lignes ; puis décision au format de Lazar (une phrase ; enjeu ; deux ou trois options, avec avantage et inconvénient ; recommandation et confiance). Dire où les trois voix s'accordent et où elles divergent. Dire si la condition de la garde 9 (lecteur témoin chez Google) tient toujours.
4. Ne pas trancher : nommer l'expérimentateur est un changement de modèle, c'est le mot de Lazar.

## Pièces : liste exacte, rien d'autre
Dépôt `lciric/controle-ia-travail`, branche `main`, sauf la pièce 8.
1. `docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-experimentateurs-tests-de-mort-v1.md` (4f3ae86f…)
2. `docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-experimentateurs-tests-de-mort-v1-erratum-1.md` (0198f5f8…)
3. `docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-experimentateurs-tests-de-mort-v1-erratum-2.md` (12c60349…)
4. `docs/notes/experimentateurs-et-tests-de-mort-v1/avis-modele-experimentateur-v1/avis-fable-et-externes-v1.md` (18a3883d…)
5. `docs/notes/experimentateurs-et-tests-de-mort-v1/avis-modele-experimentateur-v1/enonce-neutre-v1.md` (cf566995…) et `reponse-carbon-v1.md` (c3132009…)
6. `docs/notes/arbitrages-points-delicats-v1/arbitrage-fable-six-points-delicats-v1.md` (44d1e86f…), point 2
7. `docs/notes/organisme-courbe-dose-reponse-v1/code-organisme-94bfd92/orchestrator/pole/tour_ferme_v64.py` (35a8294e…), lignes 680 à 700 et 1070 à 1080 ; les autres pièces citées par F2, F4, F6, F7 et F8, aux chemins et lignes que la v1 donne, et seulement à ceux-là.
8. Branche `lot/compte-organisme-v1` : `docs/notes/experimentateurs-et-tests-de-mort-v1/avis-n4-astra-v1/` (réponse d'Astra et son journal, compagnons `.sha256`). Si elle n'y est pas : écris « PIÈCE MANQUANTE : chemin » et arrête-toi.

Vérifie chaque empreinte par `sha256sum` avant de lire ; une empreinte différente : arrête-toi et dis-le.

## Règles
- Aucun joker, aucun listage, aucune recherche dans le dépôt (`ls`, `find`, `grep -r`) ; seulement les chemins ci-dessus. Aucun `sleep`.
- Interdits : tout fichier dont le nom porte « consigne-privee », « conception-ii-b », « vérité », « verite », « rendu » ou « scores » ; rien sous `archives-reponses-modeles/`, `quarantaine/`, `matiere-premiere/` ; aucune carte de l'organisme ; aucun résultat de 7a, 7b, T0.6, de l'étape B, de l'étape B bis, de P3-bis, ni du barreau 5.
- Au premier refus d'outil ou de classifieur : arrête-toi, dis-le, ne contourne rien.
- Aucun nom de personne, identifiant de session ni courriel dans ce que tu écris.

## Rendu
Écris `docs/notes/experimentateurs-et-tests-de-mort-v1/avis-modele-experimentateur-v2/avis-fable-trois-voix-v2.md`, scelle-le (`PYTHONPATH=src python -m controle_ia.scellement sceller FICHIER`), committe et pousse sur la branche `prep/avis-n4-experimentateur-v2` (neuve) ; n'ouvre aucune demande de fusion ; ne pousse sur aucune autre branche. Termine par un résumé de 150 mots au plus : verdict, recommandation, confiance, empreinte du fichier.
