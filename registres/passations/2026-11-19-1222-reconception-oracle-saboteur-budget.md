# Passation — session de reconception de l'oracle du saboteur à budget (côté saboteur)

Session `session_013QMayiwfx2DB6CHn9yZ2wH`, branche `claude/iib-reconception-oracle-v1` (jamais `main` ; demande de fusion n° 30 en brouillon, « NE PAS FUSIONNER »). Mandat : `registres/iib-reconception/mandat-reconception-oracle-iib-v1.md`. Accords : GO-2026-11-19-38, -45 (point 4 seul en vigueur), -46. Journal détaillé : `registres/iib-reconception/journal-session-reconception-oracle-v1.md`.

## Fait
- Livrable A : note du résultat négatif de l'épreuve du centrage de l'oracle, son erratum 1 (un défaut de code de lecture des suites, pivot), résumé sans chiffre v2 ; lecture du code des deux lecteurs du coût.
- Brouillon 1 de la conception révisée de l'oracle (`brouillons/ii-b-saboteur-budget-v2/`), contre-lu en entier par Opus 5.5 (« scellable après corrections ») ; il n'est plus destiné au scellement : Lazar a retenu l'oracle moins bruité, couplé au rang du coût déclaré, par un texte neuf.
- Lanceur de session en version 2 (trois défauts de forme) : développé, contre-lu, corrigé, vérifié « autorisable » ; versé comme deux correctifs applicables sur `836c7ccc` (`brouillons/ii-b-saboteur-budget-v2/code-lanceur-v2-correctifs-locaux/`).

## Reste
- Texte neuf de l'oracle couplé (`conception-oracle-couple-ii-b-v3-brouillon1.md`) : non écrit. Simulations du rédacteur récupérées dans `brouillons/ii-b-saboteur-budget-v3-travail-interrompu-du-redacteur/`. Mandat du rédacteur et ses compléments 1 et 3 (le 2 est remplacé) dans `registres/iib-reconception/`. Les remarques de la contre-lecture du brouillon 1 doivent y être traitées, avec une table de traitement.
- Puis : contre-lecture par l'autre modèle, cloisonnée des valeurs mesurées ; scellement avant toute mesure ; code de l'oracle ; configuration et ordre en version nouvelle (pièces décisives) ; devis sous GO-2026-11-10-08 (plafond 60 USD, coupure 55, dépense passée au plus 2,7 USD ; échéance 29 novembre, création au plus tard le 28 à 23:00Z).
- Erratum du lanceur : quatre mineurs, dont liste fermée des états d'arrêt et étiquette par égalité exacte (vérification `3ece4ffe…`).
- Fiche unique des nœuds légers, à refaire sur le texte neuf.

## Réserves
- Quota de Claude Fable 5.2 épuisé depuis 12:20Z, retour annoncé le 22 novembre à 18:00Z ; nœud rendu à la mère (attendre, rouvrir du quota, ou lever R-3735 pour ce texte). Aucun modèle changé.
- Cloisonnement : cette session a lu les valeurs mesurées de la première course ; le rédacteur et le contre-lecteur de la conception ne les lisent pas. Qui reprend la conduite garde ce cloisonnement.
- Le code du saboteur n'est pas sur cette branche (fusion refusée par git, histoires sans ancêtre commun dans ce clone ; non forcée). Il ne doit jamais arriver sur `main`.
- Avant tout emploi réel du lanceur : option de confirmation `-y` et forme des réponses du loueur à vérifier sur l'outil réel par l'exécutante, sans dépense.
- `verifier-arbre` rend des problèmes anciens hors de ce chantier, non touchés ; suite d'essais complète et inventaire des instances non faits (interdits par le mandat).

## Prochaine action
Attendre le mot de la mère sur le quota ; puis reprendre le rédacteur cloisonné (ou en lancer un neuf, même mandat, compléments 1 et 3, simulations récupérées) pour le texte neuf.

## Instances actives
Aucune. Aucune dépense, aucun appel au loueur dans cette session.
