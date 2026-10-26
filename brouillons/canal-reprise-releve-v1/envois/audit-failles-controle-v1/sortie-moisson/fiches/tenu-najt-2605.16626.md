# Fiche — Najt, Toft, Tracy, Roger et Benton, *SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors* (arXiv 2605.16626v2, 19 mai 2026) — v1

- **Source déjà tenue par le programme** : `pdf-main/2605.16626v2.pdf`, SHA-256
  `1ba418227095eeea98881f61a606c9974f4f3a8758d6a6292c6a9cd8bbd76751` (préfixe contrôlé le 2026-10-26 à 11:25 UTC ;
  valeur complète dans `provenance-niveau2-lot3-v1.md`) ; non retéléchargée.
- **Pages lues** : 1.
- **Chez session-depot** : **non** (voisin de D10 et de S4).

## Ce que la source établit sur un mode d'échec

1. **Un moniteur de pointe manque la moitié des attaques construites** : sur 40 attaques de 11 catégories (transcriptions
   synthétiques d'un agent de code qui poursuit en secret un objectif nuisible), 20 ne sont jamais attrapées par un
   moniteur de pointe avec réflexion étendue sur 10 essais à 1 % de faux positifs ; taux d'attrapage global de 32 %
   (p. 1).
2. **Familles d'évasion identifiées** par les auteurs (je ne les détaille pas) ; des moniteurs « agents de code » et des
   consignes de moniteur ciblées améliorent l'attrapage pour certaines familles (p. 1).

## Conditions

- Transcriptions **synthétiques** écrites pour évader ; moniteurs génératifs ; tâches de code à fort privilège.

## Ce qu'elle ne dit pas

- Rien sur des moniteurs d'activations ; les attaques ne sont pas produites par l'agent surveillé lui-même.

## Ce que ça touche chez nous (avis)

- Bases boîte noire et papier C : un banc d'attaques écrites à la main pour évader est la mesure de robustesse qui
  manque aux juges de EC.1 ; et pour H1, il borne ce qu'un juge génératif de 3 à 8 milliards peut attraper.

## Phrase citée

« We find that 20 of 40 attacks are never caught by an Opus 4.6 monitor with extended thinking across 10 trials at a 1%
false-positive rate, while the overall catch rate is 32%. » (p. 1)
