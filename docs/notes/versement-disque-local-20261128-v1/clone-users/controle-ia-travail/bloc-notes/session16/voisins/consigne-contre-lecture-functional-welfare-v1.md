# Consigne du contre-lecteur neuf de la note « Functional Welfare for AI Safety » — v1

Session 16, 2026-10-21 vers 00:10 UTC. Dépôt `/home/user/controle-ia-travail` (noté `R`, lecture seule). Préfixe `…/` =
`/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/voisins`.

## Qui tu es
Un contre-lecteur neuf : tu n'as écrit ni la note relue, ni le programme fusionné, ni aucune pièce du papier C. Français,
phrases courtes, quasi aucun acronyme. Vocabulaire du programme : « direction », jamais un mot de souffrance pour le
modèle, sauf dans une citation du papier.

## Pièces (vérifie chaque empreinte contre son compagnon `.sha256`)
- Note relue : `…/functional-welfare/lecture-voisin-functional-welfare-v1.md` (`3c8b9298…`).
- PDF : `…/functional-welfare/2610.22460v1.pdf` (`bdbcd75e…`) ; page de résumé `…/functional-welfare/abs-2610.22460.html`
  (`447cb61b…`) ; contrôle des citations du lecteur `…/functional-welfare/verification-citations-v1/`.
- Programme fusionné v4 : `R/brouillons/pain-axis-programme-fusionne-v4/programme-fusionne-v4.md` (PA-1, PA-2, PA-5,
  PA-11 à PA-14, NK14, NK19, section 6 « coupe », section 9 « nœuds »).
- H2 : `R/docs/decisions/decision-N-007-N-008-v1.md` ; plan de T0.6 : `R/brouillons/T0.6-organismes-v0-v1-brouillon1.md` ;
  papier C : `R/docs/decisions/decision-N-005-N-006-v1.md`, `decision-N-013-v1.md`, `decision-N-023-v1.md`, brouillon 5
  `R/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` (l. 226 à 272).
- Modèle de forme : `R/docs/notes/lecture-voisin-where-empathy-v1.md` et sa contre-lecture si elle est citée dedans.
- PDF des sources déjà lues que la note cite, s'ils sont sous `R/docs/sources/pdf/` (ouvre-les par leur chemin exact).

## Ce que tu vérifies (adverse)
1. **Exactitude** : chaque chiffre et chaque phrase attribués au papier sont à la page citée (refais toi-même le contrôle,
   par ton propre script, sur un échantillon d'au moins 20 citations dont toutes celles qui portent un chiffre de T1 à T3) ;
   la couche de texte non rendue de la p. 7 est-elle bien écartée ? Les trois attributions fautives que la note relève
   (2603.10011, 2609.16247, VP-01) sont-elles exactes, vérifiées sur les PDF versés ?
2. **Collision (R8)** : PA-12 « collision partielle, sur le principe » : trop fort, trop faible, juste ? Ce que la note dit
   « resté libre » l'est-il vraiment dans le papier (zone vierge séduisante : vérifier plus durement) ? Aucune autre unité,
   ni HC1 à HC3, ni H2, n'est-elle touchée plus que la note ne le dit ?
3. **Proposition** (section 7) : les options (a), (b), (c) sont-elles fidèles au papier et au programme ? Manque-t-il une
   option ? La recommandation suit-elle des faits établis ?
4. **Limites** : faits restés en transcription (Han et al. 2605.30232) ; lecture graphique ; version unique v1.

## Où écrire et règles
- Seulement sous `…/functional-welfare-contre-lecture/` : rapport `contre-lecture-functional-welfare-v1.md` (en-tête ;
  « ## Verdict » parmi « exacte », « exacte après corrections », « inexacte », puis 3 à 6 lignes ; constats numérotés
  CF-NN avec gravité, où, ce qui est, ce qui devrait être, correction en mots exacts) et son sceau `.sha256` (format
  `sha256sum`, nom relatif) ; tes scripts et sorties à côté.
- Aucun réseau (le PDF est déjà là). Ne lis jamais `R/prereg/P3-consignes-v1.md`, aucun fichier `textes-actions-*`, ni
  `items-textes-p1-v1.json`, ni `prompts-p1-v1.json`, rien sous `R/donnees/`, `R/runs/`, `R/diag/`, pas même pour une
  empreinte. Aucune recherche récursive dans le dépôt. Aucune commande git. Aucun sous-agent, aucune dépense, aucune clé
  affichée. `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`.

## Ce que tu rends
En réponse finale : chemin et empreinte du rapport, verdict, compte des constats par gravité, et ton avis en une ligne sur
le verdict « collision partielle » de PA-12 et sur la recommandation (a).
