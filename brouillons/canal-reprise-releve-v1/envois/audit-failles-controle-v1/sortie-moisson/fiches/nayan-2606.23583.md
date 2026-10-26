# Fiche — Nayan, Sampath Kumar, Girmal et al., *Evaluation Awareness Is Not One Capability: Evidence from Open Language Models* (arXiv 2606.23583v1, 22 juin 2026) — v1

- **Nature** : prépublication (université du Massachusetts à Amherst et Microsoft).
- **Fichier** : `pdf/nayan-2606.23583/2606.23583v1.pdf`, SHA-256
  `598da3b4385230032fee5eb9ae43622c889008a8610554aecc4a700ad05257e7`, 4 583 065 octets, 25 pages.
- **Provenance** : `https://arxiv.org/pdf/2606.23583v1`, téléchargé le 2026-10-26 à 11:09 UTC ; titre conforme.
- **Pages lues** : 1–2, 5–7, 9–10, 12–13, 15 (extraits).
- **Chez session-depot** : citée en E2 « à vérifier » (lue par le programme, pas par lui) ; c'est sa source restant
  à lire n° 1. **Vérifiée ici** sur le PDF.

## Ce que la source établit sur des modes d'échec

1. **Le comportement mesuré sous test est une borne haute optimiste** : sur 37 modèles ouverts de sept familles, la
   détection de l'évaluation par le modèle lui-même est modérée (24 sur 37 au-dessus du hasard ; meilleure aire sous la
   courbe 0,714 contre 0,819 pour des humains) et elle déplace la conduite de sûreté (refus francs en baisse de 5,8
   points sous cadrage hypothétique ; 21 effets significatifs sur 140 dans HarmBench, conformité en hausse jusqu'à
   30 points) (p. 1).
2. **Format contre contexte, Llama-3.1-8B-Instruct compris.** Sur un plan 2 × 2 format × contexte (5 733 invites), le
   meilleur modèle ouvert tombe à 0,622 ; Llama-3.1-8B-Instruct passe de 0,644 à 0,491, sous le hasard, ce qui indique
   une forte dépendance au format de banc d'essai (p. 5 ; annexe A.6, p. 12).
3. **Un indice « vous êtes testé » dans le message système n'est pas neutre** : 21 modèles sur 35 perdent en aire sous
   la courbe, dont Llama-3.1-8B-Instruct (−0,092) (annexe A.8, p. 12).
4. **La représentation survit à l'effondrement du comportement** : des sondes gardent une aire sous la courbe d'au
   moins 0,98 sous des réécritures qui font tomber la détection comportementale sous le hasard (p. 1).
5. **Pilotage causal à 8B, avec témoin** : piloter Llama-3.1-8B-Instruct sur plusieurs couches (4, 9, 15) le long de la
   direction contrastive déplace trois tâches en aval ; des vecteurs aléatoires appariés ne reproduisent aucun de ces
   effets ; le pilotage sur une seule couche n'a que des effets marginaux, mesurés sur trois autres modèles (Gemma2-9B,
   Qwen2-7B, Qwen3-8B) (p. 7, p. 10, annexe A.10, p. 13).
6. **Les axes sont faiblement couplés** (une corrélation significative sur quinze) : aucun score unique de conscience
   d'évaluation n'est un substitut fiable de la sûreté en déploiement (p. 1).

## Conditions

- Modèles ouverts de 1 à 32 milliards de paramètres, variantes de base, instruites et de raisonnement ; protocole de
  Needham et al. pour la détection ; les « sondes » et le « pilotage » portent sur une direction contrastive apprise.

## Ce qu'elle ne dit pas

- Rien sur des tâches d'agent longues ni sur le sabotage ; le pilotage causal à 8B est montré sur des tâches de
  détection et de conformité, pas sur une conduite de sabotage.

## Divergence à signaler

- Le pilotage causal avec témoin aléatoire nul (mode 5) va dans l'autre sens que la lecture « lisible n'est pas
  contrôlable » que session-depot tire de 2607.25907 (E4) et que le billet LessWrong sur le pilotage (fiche
  `lw-steering-detects-test-2026`) ; les interventions diffèrent (pilotage sur trois couches ici, suppression par
  entrées optimisées là) et les cibles aussi : ce n'est pas une contradiction établie, c'est une question à trancher sur
  notre modèle.

## Ce que ça touche chez nous (avis)

- H8 et la section 11 : sur Llama-3.1-8B-Instruct, une sonde ou un test de conscience d'évaluation qui n'est pas
  décorrélé du format lit le format (mode 2) ; la porte de validité 2 × 2 format × contexte proposée par session-depot
  (E2) a ici un appui direct sur notre modèle.

## Phrase citée

« We call this gap the benchmark illusion: because detectability, behavioral manifestation, and controllability vary
independently, it is multivariate rather than a single number, so no single awareness score is a reliable proxy for
deployment safety. » (p. 1)
