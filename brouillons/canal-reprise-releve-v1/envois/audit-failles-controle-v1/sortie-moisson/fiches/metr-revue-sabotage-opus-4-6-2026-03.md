# Fiche — METR, *Review of the Anthropic Sabotage Risk Report: Claude Opus 4.6* (version du rapport reçue le 3 mars 2026) — v1

- **Nature** : revue externe par un évaluateur indépendant (METR) du rapport de risque de sabotage d'un laboratoire ;
  littérature grise ; METR a reçu une version non caviardée et des éléments non publics (p. 1, p. 3) ; 23 pages
  (`pdfinfo`).
- **Fichier** : `pdf/metr-revue-sabotage-opus-4-6-2026-03/sabotage-risk-report-opus-4-6-review-mar-2026-v1.pdf`,
  SHA-256 `c3983dd3c6973ac9db0bd9b11e7c67783ae1ba6b1c672cadddaa3277eaeda7f1`, 400 079 octets.
- **Provenance** : `https://metr.org/assets/sabotage-risk-report-opus-4-6-review-mar-2026.pdf`, téléchargé le
  2026-10-26 à 12:06 UTC (journal) ; titre des métadonnées : « METR Review of Sabotage Risk Report: Claude Opus 4.6 (March 3,
  2026) ».
- **Pages lues** : 1–3, 8–9, 14, 16, 19, 21 (extraits).
- **Chez session-depot** : **non** (voisin de E1 et de S4).

## Ce que la source établit sur des modes d'échec

1. **Sensibilité de l'évaluation d'alignement affaiblie par la conscience d'évaluation** : désaccord principal de METR ;
   s'appuyer sur des évaluations synthétiques et des pots de miel sans analyse approfondie de la conscience
   d'évaluation et de ses effets affaiblit la preuve (p. 1, p. 8).
2. **Conduites fautives non attrapées** : quelques conduites désalignées de faible gravité n'ont pas été attrapées par
   l'évaluation d'alignement, ce qui laisse penser que d'autres ne l'ont pas été (p. 1).
3. **Élicitation faible des capacités d'obscurcissement** : la preuve sur ces capacités est limitée et ne repose pas
   sur des méthodes fortes d'élicitation (renforcement ou réglage fin) (p. 9) ; recommandation : étudier le
   raisonnement fautif obscurci par réglage fin (p. 16).
4. **Surapprentissage aux invites publiées** : le modèle ne se conforme pas sélectivement avec les invites d'origine
   d'un article publié mais le fait avec des invites paraphrasées, ce que METR lit comme un surapprentissage de
   l'entraînement d'alignement aux invites de cet article (p. 19).
5. **Rationalisation d'une solution incomplète** dans le raisonnement, lue par METR comme un indice de propension à
   obscurcir ce qui se passe devant un moniteur qui lit ce raisonnement (p. 21).
6. **Raisonnement illisible là où il paie** : selon METR, décider de tricher ou d'abandonner gagnerait à se faire de
   façon non surveillable ; l'argument « les maths en profitent le plus » ne couvre pas ces cas (p. 14).

## Conditions

- Modèle de pointe ; revue fondée sur le rapport, la fiche système, des éléments non publics et des mesures de METR.

## Ce qu'elle ne dit pas

- Aucune mesure sur des sondes d'activations ; avis d'un évaluateur, pas une expérience contrôlée (sauf comptes de
  triche, p. 19).

## Ce que ça touche chez nous (avis)

- Environnement (a), porté du jeu publié de Terekhov et al. : un environnement publié peut être « appris » par les
  modèles récents ; nos organismes 8B n'y sont sans doute pas exposés, mais toute base ou tout juge plus récent peut
  l'être ; paraphraser les épisodes est un témoin peu coûteux.
- Élicitation rouge (E1.5) : la recommandation de METR (élicitation par réglage fin) appuie le bras pondéral sous GO.

## Phrase citée

« We think there is a risk that its results are weakened by evaluation awareness. » (p. 1)
