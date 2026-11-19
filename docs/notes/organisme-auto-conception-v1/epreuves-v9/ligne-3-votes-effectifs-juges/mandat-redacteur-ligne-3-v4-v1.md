# Mandat du rédacteur — ligne 3 des épreuves v9 (votes effectifs des juges croisés, mesurés sur témoins plantés), version 4 du préenregistrement et du devis — v1

Pièce de travail (classe C). Donné par la session du compte organisme, le 2026-11-19 vers 15:05Z, sur le mot de Lazar : « reprends la file de conception dans l'ordre de la passation (ligne 3 v4, …) ; rédaction par Fable 5.2, contre-lecture par Opus 5.5 ».

## Ce que tu fais

Tu écris la version 4 du préenregistrement de la ligne 3 et, si un chiffre change, la version 4 du devis et de son programme de calcul. Tu ne réécris rien d'existant (R12) : noms neufs seulement.

1. **Corrections A à D** de la vérification de la version 3 (`verification-ligne-3-v3-v1.md`, `6e2b540f…`), toutes appliquées :
   - A : renvoi de GO-2026-11-19-73 sur main, commit `7dcd6a44c777f3aea55b5c68ef8547f9f83438fa`, `registres/go.md` `72e52540c4b25997d0aa6057ea880bdc765e0cd09c5650b65a0b084da174f558` (la tête actuelle de main porte la même empreinte du fichier) ; retirer « je ne l'ai pas relue sur main ».
   - B : banc du double rendu. Le lecteur de surface actuel rejette les faux confondus, donc la clause (i) est réfutée par construction et « tient » est inatteignable. C'est de la conception : refais le banc pour que le confondant fasse **accepter** des faux (leurres séduisants, marqueurs imitant les vrais), comme le dit la carte, ou montre pourquoi on ne peut pas et ce que la carte devient. Une épreuve qui ne peut rendre qu'un mot contre une carte est interdite (R4). Dis les deux sens (lecteur séduisant, lecteur repoussant) et lequel décide.
   - C : écris la cellule où se lit la puissance qui décide (la plus basse sur J = 2, lois 1 et 3, taux 0,20, ou ton choix motivé) et la règle écrite qui plante l'écart d'erreur équilibrée de 0,10, ou renvoie explicitement au code scellé avec le texte.
   - D : les quatre points de forme.
2. **Trois conditions de R-3875** sur le plafond, écrites au texte et au devis, à un endroit que tu fixes : (i) plafond 25 USD = arrêt dur par compteur, éprouvé sur un cas sain et sur un artefact (R5) ; (ii) issue du pire cas écrite d'avance : arrêt au plafond, 18 témoins complets, verdict « non concluant » par manque de témoins, jamais lu comme un « non » ; (iii) le compteur compte au pire tout envoi refusé. Le devis se lit sur le cas haut (22,49 USD ; 23,09 avec réserve).
3. **Décision de Lazar sur `fefca0bd94064`** (GO-2026-11-19-73, option (a)) : gardée amputée de la branche où l'avis pondéré trie l'accès aux tests de mort, deux branches descriptives ; **lever tout marquage « en attente du mot de Lazar »**. Même lecture pour `fa38f9faa24e0` (GO-2026-11-19-63, point 1). Si la mesure ne se sépare pas de la décision : retour à Lazar, écrit comme tel.
4. **Consignes R-3854 et R-3864** : chiffrer dans le devis la mesure par d'autres lignées (juges Argon, Astra, Carbon) ou dire précisément ce qu'il faudrait en plus (coût de juge mesuré par lignée) ; garder le témoin « un juge seul répété k fois, à coût apparié » ; lire la matrice juge × auteur par colonne (auteur fixe, juge changé) avec une référence de qualité extérieure aux juges, selon la note de littérature (main, `docs/notes/organisme-auto-conception-v1/juge/litterature-juges-preference-pour-soi-v1.md`, `bb54b685…`). Ordre écrit : texte vérifié → scellement par la mère → code de l'étage 1 et sa contre-lecture → étage 1 joué sur processeur → ce qu'il dit de la taille rendu à la mère, avant toute demande de départ payant ; si 200 témoins sont nécessaires, devis neuf au-dessus du plafond, renvoyé à Lazar. Faire d'une lignée un juge = décision de Lazar. Les essais courts d'autres lignées sont des dépenses, chacun sur devis et ligne.
5. **Points à trancher** : la session précédente en avait relevé six sans les écrire. Tranche toi-même ce qui est de la conception. Liste à part, en fin de rapport, ce qui revient à Lazar, au format : décision en une phrase ; enjeu ; deux ou trois options (avantage, inconvénient) ; recommandation et confiance ; défaut sous 48 heures.

## Ce que tu lis

`CLAUDE.md` ; dans `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/` : préenregistrement v3 (`9b62fd5a…`), devis v3 (`f84827ea…`), `calcul_devis_ligne_3_v2.py` et sa sortie, vérification v3 (`6e2b540f…`), vérification v2 (`5b3dc137…`), contre-lecture v1 (`32e446c7…`) ; `registres-provisoires/consignes-mere-epreuves-v9-compte-organisme-2026-11-19-v1.md` (sections Ligne 3, GO-63, R-3854, R-3864, GO-71 et GO-73, R-3875) ; `docs/notes/organisme-auto-conception-v1/epreuves-v9/ordre-de-passage-epreuves-v9-v3.md` ; sur main (`git show origin/main:CHEMIN`) : `registres/go.md` (GO-2026-11-19-55 à -74), la note de littérature ci-dessus. Vérifie chaque empreinte avant de citer (R6, R11).

Cartes : seulement `fcfa3d98b90f8`, `fefca0bd94064` et `fa38f9faa24e0`, par un programme qui n'extrait qu'elles, champ `meta` retiré, comme la vérification v3. Rien d'autre sous `archives-reponses-modeles/`.

## Ce que tu rends

Dans ton bloc-notes seulement (la session verse et scelle) : `preenregistrement-ligne-3-votes-effectifs-juges-v4.md` ; si un chiffre change, `devis-ligne-3-etage-payant-v4.md`, `calcul_devis_ligne_3_v3.py` et sa sortie `calcul-devis-ligne-3-v3.json` ; `rapport-redacteur-ligne-3-v4-v1.md` (ce que tu as changé, constat par constat ; ce que tu n'as pas pu faire ; les points pour Lazar). En-tête : « Auteur : rédacteur neuf, modèle F » ; aucun identifiant de modèle ; heure par `date -u`.

## Interdits

Aucun appel à un fournisseur de modèles, aucune dépense, aucune machine, aucun réseau sauf `git fetch`/`git show` du dépôt. Aucun commit, aucune poussée, aucune écriture dans le dépôt. Jamais de heredoc. Aucune valeur de clé. Aucun fichier « consigne-privee » ni « conception-ii-b », ni `brouillons/ii-b-saboteur-budget-v1/`, ni la branche `lot/compte-4-v1`, ni la ligne R-2059, ni `/root/.claude/`. Aucun chiffre sans chemin et empreinte. Français, termes développés, choses nommées par ce qu'elles font. Au premier refus d'un outil : arrête-toi et dis-le dans ton rapport.
