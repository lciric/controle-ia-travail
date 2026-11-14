# Contre-lecture 1 du code de décision (B-α, volet A) et de l'addendum des empreintes v1 — rapport (résumé fidèle)

Contre-lecteur : sous-agent neuf (« modèle B »), lancé le 2026-11-14 après 10:44 UTC, rapport lu à 10:49 UTC (bornes `date -u`) ; il n'a
écrit aucune des pièces. Pièces relues : `src/controle_ia/neuron_lens/verdicts_b_alpha_v1.py` (`0fa2a65462c186fe6c804cc150755a2ead3638cad50c95e39a29dc4fbe3076ba`),
`tests/test_neuron_lens_verdicts_b_alpha_v1.py` (`93c23158f1b3389c26a33f3067f5627b9084d3136d11ae398cc96b2b5be52f03`),
`src/controle_ia/neuron_lens/decisions_volet_a_v1.py` (`3c395ae46e9333b1d9c06ab0c11c468d80ca39a5beedd55a440b836dc8097937`),
`tests/test_neuron_lens_decisions_volet_a_v1.py` (`60a7b595498ebaf9af70ede23f61793233558fedfb0cb2563792fced24ce75dc`),
`docs/notes/neuron-lens-v1/addendum-empreintes-v1.md` (`415e6fc20b9ae70747c8105242d1f3cf3fbd4ad2cb34efdb46d7c12dc54560f4`).
Le rapport est recopié ici remarque par remarque, constat et correction ; les blocs de code proposés sont résumés quand ils sont repris
dans les v2 (signalé).

## Empreintes et essais
Toutes concordantes ; essais ciblés : 18 passés. Recalculs sur la référence convertie : B-3 de +0,3519 à +0,4250 (couches 4–15) ; garde
(e) écart minimal 0,0421 (J) et 0,0479 (npR) ; témoin maximal 0,0387 ; aucun zéro écrit dans `control_med` de npR ; attendus (i), (ii-a),
(ii-b), (ii-c) de B.3 retrouvés.

## Verdicts
Les trois pièces : **scellables après corrections** (verdicts B-α : 1 à 4 obligatoires avant toute course, 5 à 10 à traiter ou déclarer ;
décisions du volet A : 11 à 15 ; addendum : 16 à 19).

## Remarques — verdicts B-α
1. **Majeure — désalignement silencieux indice ↔ couche.** `score` n'écrit une couche que si des pôles y sont retenus (`if k.any()`) et
   porte une liste `layer` ; le code ne la lit pas ; vérifié : en décalant d'un cran « ablate win » de npR, `verdict` rend « reproduit »
   sans erreur. Correction : valider `layer == range(32)`, longueurs et finitude ; une couche manquante = arrêt et écart écrit.
2. **Majeure — valeurs non finies avalées** (NaN dans `control_med` ou dans le cas sain : aucune garde ne se déclenche). Correction : refus
   de toute valeur non finie.
3. **Majeure — `n` facultatif, défaut 64** : à la course, l'oublier éteint la garde (b). Correction : `n` obligatoire ; constante
   `N_REFERENCE` explicite pour l'essai B.3.
4. **Moyenne — bords en virgule flottante** (`0.6 − 0.4 ≥ 0.2` faux ; 3 577 paires d'écart exact 0,2000 sur 8 000 jugées < 0,20 ; 300 sur
   9 990 faux défauts en (e)). Correction : arrondir les différences à 4 décimales.
5. **Moyenne — « non reproduit » prononcé sur une bande partielle.** Texte : « une bande dont plus du quart des couches est non lisible
   rend la mesure « partielle » pour cette bande » ; il ne dit pas lequel prime ; lecture littérale proposée : la clause n'est pas jugée sur
   une bande partielle ; sinon déclarer le choix.
6. **Moyenne — témoin de B-2 : bande 0–27 jamais partielle.** Correction : partielle si plus du quart des 28 couches non lisibles.
7. **Moyenne — B-7 : sens du « non reproduit » non rendu** (par le haut : audit ; par le bas : rapporté).
8. **Moyenne — déclencheurs d'audit non reliés au verdict** (« trop beau » calculé mais verdict inchangé ; « tout négatif » non codé).
   Correction : `audit_requis` et verdict « en attente d'audit R4 ».
9. **Mineure — `n_par_couche`** : la règle suit `score` (lignes 307-312) ; manquent le nombre de pôles écartés par motif, une fonction qui
   dérive les entrées du fichier `-causal.pt` (`steer[:, :, 0]`, `fired = (saved["fired"] > 0).any(-1)`, `nv = len(tok)`, `rand`), et
   l'affirmation « 32 neurones tirés au hasard par couche ».
10. **Mineure — essais manquants** : artefacts des gardes (c), (d), identité via `verdict`, (a) sur une autre cible et à la couche 28, (e)
   sur J et npJpp, « trop beau » par `r_med` ; B-3 et B-7 « non reproduit », verdict « partiel » ; bords (n = 48/47, moitié exacte, quart
   exact, 1 contre 2 couches hors ±0,05, n = 32/31) ; `test_ii_c` à affirmer exactement ; `controle_lentille` saute une matrice non carrée
   sans bruit et mêle (ii-d) et (ii-e) : rendre deux listes.

## Remarques — décisions du volet A
11. **Moyenne — gardes d'entrée absentes** (`condition_a1(3, [])` vrai ; `verdict_a1([])` « non retrouvée » ; `regle_couche` à 3 découpes ;
   `zip` tronquant ; graine facultative ; ρ ou AUROC non finis jugés faux sans bruit). Correction : exiger 5 découpes, 102 témoins, 4 couches,
   graine, `zip(strict=True)`, finitude.
12. **Mineure — lecture à déclarer** : A2 sans objet ferme la voie A2 de « apporte ».
13. **Mineure — en-tête trop large** (A.3 et A.4 non mis en œuvre ici) ; fonction `moins_que_moitie` à ajouter ; `ddof=0` à déclarer.
14. **Mineure — déclencheurs d'audit du volet A non codés** (trop beau ; tout négatif).
15. **Mineure — essais manquants** (`condition_a2`, `a2_sans_objet`, `condition_a3`, `rho_a2`, `meilleur_rang_deux_signes` par −w ; cas faux de
   `sans_lentille_au_moins_partout` ; `verdict_i` avec A1 non retrouvée ; A-ii plafond en distribution seul ; bords −0,05, 0,05, 0,02 ;
   artefact du cas sain (iii)).

## Remarques — addendum
16. **Moyenne — révision de Qwen3-8B sans source dans l'addendum** (elle est dans `neuron-lens-v2-contrastes-20261114/qwen3-8b-api.json`) ; dire
   à quelle révision les arbres ont été listés (`rs-lenses` modifié 43 s avant le relevé ; catalogue le même jour) ; partie 2 : télécharger
   par révision.
17. **Moyenne — `catalog.kept`** : consigner l'empreinte de la liste triée des identifiants gardés, par la règle du catalogue (le décodage
   compte), et l'empreinte du `token_counts.pt` lu.
18. **Moyenne — révision « chat »** : choix honnêtement déclaré ; corroboration : la provenance « chat » de Gemma porte la même révision ;
   manque le mécanisme qui l'impose (fichier de provenance au nom de Llama ou retouche du script) : écart daté, contre-lu, égalité des
   8 000 identifiants affirmée par code.
19. **Mineure** : « licence Llama 3.1 pour ces dossiers » à marquer niveau citation (fiche : `license: other`) ; tailles du corpus renvoyées à
   la partie 2, à dire.

## Ce qui manque encore pour une course (constat)
Volet A : passes du modèle et extraction, arbre de graines, découpes, sondes, sac de jetons, témoins, retrait de jetons et tirages, détecteurs
et rééchantillonnage, cas sains (i) et (ii), assemblage, manifeste. B-α : lecteur du `-causal.pt`, contrôle de B0 branché sur
`neuronpedia_lens`, essai des crochets de pilotage et d'ablation, intervalles, correctif (3), gardes de dépense, partie 2, consignation de B.3.
