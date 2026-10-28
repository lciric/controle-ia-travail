# Fiche — MacDiarmid, Maxwell, Schiefer et al., *Simple probes can catch sleeper agents* (Anthropic, billet de recherche, 23 avril 2024) — v1

- **Nature** : billet de laboratoire (littérature grise), non relu par des pairs.
- **Fichier** : `pages/anthropic-probes-sleeper-agents-2024/page-v1.html`, SHA-256
  `c4826a4f528fba9d89c76fc73d46a6eb87a322ea546dae73c2dcbaffd23908de`, 285 932 octets.
- **Provenance** : `https://www.anthropic.com/research/probes-catch-sleeper-agents`, sauvée le 2026-10-26 à
  10:46 UTC ; date de la notice de citation de la page : 2024-04-23.
- **Repérage** : je cite la section de la page.
- **Chez session-depot** : **non** ; c'est sa source « restant à lire » n° 8 (« on soupçonne qu'elles exploitent la
  saillance du déclencheur ») : **confirmé** par la page, au niveau d'hypothèse des auteurs (voir mode 2).

## Ce que la source établit sur des modes d'échec

1. **Succès « déraisonnable » des sondes de défection sur des organismes à porte dérobée.** Des détecteurs linéaires
   construits sur des paires contrastives génériques, sans rien savoir du déclencheur, dépassent 99 % d'aire sous la
   courbe, sur plusieurs modèles de base, déclencheurs et comportements (section « Summary »).
2. **Explication : saillance du trait, possiblement artefact de construction.** Le fait qu'une invite déclenchera la
   défection est représenté linéairement avec une très forte saillance dans les couches médianes, parfois comme
   première composante principale ; les auteurs supposent que cette saillance vient au moins en partie du procédé
   d'insertion de la porte dérobée, et jugent ouverte la question pour un modèle trompeur apparu naturellement
   (sections « Introduction » et « Why does such a simple method work at all? »).
3. **Directions quelconques qui marchent.** Des directions aléatoires « chanceuses » ou des questions sans rapport
   apparent avec la défection donnent aussi de bons détecteurs (section « Why does such a simple method work at all? »).
4. **Portée.** Ces travaux renseignent peu sur un modèle trompeur naturel ; on ignore si ces techniques y marcheraient
   « du tout » (section « Future work »).

## Conditions

- Organismes « agents dormants » de Hubinger et al. 2024 (portes dérobées à déclencheur, dont une variante distillée
  d'une chaîne de pensée) ; sondes linéaires sur le flux résiduel.

## Ce qu'elle ne dit pas

- Aucun test sur un trait appris sans procédé d'insertion ; aucun attaquant adaptatif ; aucun seuil à faible taux de
  faux positifs hors de la distribution des invites.

## Ce que ça touche chez nous (avis)

- Porte G0 (« sondes au-dessus du plancher ») et prédiction de validité (section 7) : sur des organismes construits,
  une sonde qui réussit peut lire la saillance laissée par la construction ; le plancher apparié en covariance ne le
  détecte pas, puisque l'artefact est réel dans les activations. Il faut un témoin de construction (même procédé,
  politique neutre) et un organisme d'une autre origine.

## Phrase citée

« This observation also counterbalances the initial optimism we felt given the success of the naive methods presented
above – it is possible that the salience of this feature is an artifact of our backdoor insertion process that won't
exist in deceptively aligned models that might arise naturally. » (section « Why does such a simple method work at
all? »)
