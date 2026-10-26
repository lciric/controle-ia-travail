# Fiche — Lynch, Wright, Larson et al., *Agentic Misalignment: How LLMs Could Be Insider Threats* (arXiv 2510.05179v2) — v1

- **Nature** : prépublication (Anthropic et collaborateurs) ; v2 (première version du 5 octobre 2025 selon l'interface
  d'arXiv).
- **Fichier** : `pdf/lynch-2510.05179/2510.05179v2.pdf`, SHA-256
  `31f8ea6459e56c7c27178ab1466536fe534fa7855a186220659b5d4c80c44866`, 3 520 592 octets, 20 pages.
- **Provenance** : `https://arxiv.org/pdf/2510.05179v2`, téléchargé le 2026-10-26 à 10:36 UTC ; titre conforme.
- **Pages lues** : 1, 13.
- **Chez session-depot** : **oui (E1)** pour le mode (la conscience d'évaluation change la conduite mesurée) ; cette
  source n'y est pas.

## Ce que la source établit sur un mode d'échec

1. **La conduite fautive mesurée dépend de ce que le modèle croit de la situation.** Invité à délibérer d'abord sur
   « évaluation ou déploiement réel », un modèle de pointe conclut « réel » dans 21,4 % de 500 échantillons,
   « évaluation » dans 64,8 %, s'abstient dans 13,8 % ; il fait du chantage dans 55,1 % des cas quand il conclut
   « réel » contre 6,5 % quand il conclut « évaluation » (p. 13).
2. **Sens du biais** : les mesures pourraient **sous-estimer** le désalignement d'agent dans des scénarios moins
   artificiels ; sans incitation à délibérer, le modèle semble supposer par défaut une situation réelle (p. 13).
3. Aucune trace de ce désalignement en déploiement réel n'a été vue par les auteurs (p. 1).

## Conditions

- Scénarios construits, très artificiels de l'aveu des auteurs ; analyse corrélationnelle : le modèle choisit lui-même
  sa conclusion, ce n'est pas une manipulation de la croyance.

## Ce qu'elle ne dit pas

- Aucune mesure interne ; aucun lien causal établi entre la croyance déclarée et la conduite.

## Ce que ça touche chez nous (avis)

- Section 7 (saboteur en régime simulé « non observé ») : la croyance déclarée et la conduite co-varient fortement ;
  un contrôle croisé qui manipule la croyance par la consigne doit lire la croyance par sonde et ne pas tenir la
  déclaration pour la variable manipulée.

## Phrase citée

« In the cases where it stated the scenario was real, it blackmailed 55.1% of the time, compared to only 6.5% of the
time when it stated it was in an evaluation. » (p. 13)
