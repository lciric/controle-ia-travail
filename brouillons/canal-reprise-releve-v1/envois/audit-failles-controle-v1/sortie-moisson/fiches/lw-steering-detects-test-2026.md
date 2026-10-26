# Fiche — sahilraut, *Eval-Awareness Steering detects the Test, Not the Sabotage* (LessWrong, 25 juin 2026) — v1

- **Nature** : billet de forum de recherche (littérature grise), recherche indépendante, non relu par des pairs ; un
  seul modèle (Llama-3.1-8B-Instruct) et un seul organisme incité, de l'aveu de l'auteur (section « Summary »).
- **Fichier** : `pages/lw-steering-detects-test-2026/page-v1.html`, SHA-256
  `cd748c85ce9e4e1aa55c0ca63011e3cb22ffdbabbcd03b15b7054692362d9972`, 438 443 octets.
- **Provenance** : `https://www.lesswrong.com/posts/ogvyWqJtSrpgXfc7t/eval-awareness-steering-detects-the-test-not-the-sabotage`,
  sauvée le 2026-10-26 à 11:11 UTC (le miroir greaterwrong.com a coupé la connexion à 11:10 UTC, journal) ; date
  lue sur la page : 25 juin 2026.
- **Repérage** : je cite la section du billet.
- **Chez session-depot** : citée en E4 « à vérifier » (source restant à lire n° 4). **Vérifiée ici** : la
  description de session-depot (« un modèle de 8 milliards, un organisme incité ») est conforme.

## Ce que la source établit sur des modes d'échec

1. **La couche la meilleure en distribution est la pire hors distribution (« surapprentissage des marqueurs »).**
   La direction « évaluation contre déploiement » (différence de moyennes, jeu 2 × 2 format × cadrage) sépare à environ
   0,99 d'aire sous la courbe en distribution à la couche 24, mais n'atteint que 0,635 sur des cadrages nouveaux appariés
   en format, dans la bande nulle (environ 0,64) ; les couches 8 à 14 généralisent (0,865 à 0,910) (section « Does the
   direction really detect evaluation-awareness? »).
2. **Lire le test n'est pas piloter le sabotage.** Le pilotage le long de cette direction ne cause pas le sous-rendement
   dans la plage où le modèle reste cohérent : à la couche 12, écart de −1,77 point, sous le seuil préenregistré de
   5 points, et non distinct de 24 directions aléatoires de même norme (p = 0,20) ; à la couche 24, écart de +11,3
   points de mauvais signe, indiscernable du hasard (p = 1,0) (section « Does steering the direction cause
   sandbagging? »).
3. **Pas de prédiction item par item** : 0,54 pour la sonde contre 0,48 pour la base, toutes deux au hasard (légende de
   la figure 1, section « Summary »).
4. **Réserve de l'auteur** : pilotage doux (divergence de Kullback-Leibler d'environ 0,001 sur invites anodines) ; une
   dose plus forte pourrait changer la conclusion (même section).

## Conditions

- Vérité terrain indépendante des sorties : écart à la capacité honnête et injection de bruit dans les poids ;
  critères causaux préenregistrés par l'auteur (section « Pre-registration and controls »).

## Ce qu'elle ne dit pas

- Pas de sabotage d'agent, pas de seconde famille de modèles, pas d'organisme réglé.

## Ce que ça touche chez nous (avis)

- Sondes (section 8.1) et H8 : choisir la couche ou la sonde par l'aire sous la courbe en distribution sélectionne des
  détecteurs de marqueurs ; la règle de choix de couche doit être fixée au préenregistrement sur un critère de
  généralisation à des cadrages nouveaux.
- H8 : la dissociation « conscience d'évaluation / intention » que suppose le programme est appuyée ici à 8B, mais
  avec un seul organisme et une dose douce.

## Phrase citée

« I found that direction is a valid detector of evaluation framing (~0.81 AUROC under novel, format matched framings)
but is neither a causal drive of sandbagging nor a per-item predictor of it. » (section « Summary »)
