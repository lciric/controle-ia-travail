# Fiche — Xu et Wu, *Attacking the Oversight, Not the Mission: Backdoor Evasion Against Activation-Based Monitors in Reasoning Agents* (NeurIPS 2026, atelier « Agents in the Wild », affiche) — v1

- **Nature** : **résumé seul**, lu sur la page de conférence ; papier sur OpenReview, non tenté (refus d'OpenReview
  à la session, journal).
- **Fichier** : `pages/neurips2026-attacking-oversight-168158/page-v1.html`, SHA-256
  `fd9570ec27172c639b4c2625c8929b440166c680a2cdf941f0aece0a8eba39e1`, 92 754 octets.
- **Provenance** : `https://neurips.cc/virtual/2026/168158`, sauvée le 2026-10-26 à 11:10 UTC.
- **Repérage** : section « Abstract » de la page.
- **Chez session-depot** : source restant à lire n° 3 (« à vérifier ») ; **sa lecture d'après la page de conférence
  est conforme au résumé** ; papier non lu ici non plus.

## Ce que le résumé établit (mode d'échec et contre-indice)

1. **Évasion réelle mais localisée** : un réglage fin adverse contre une sonde linéaire qui lit l'état interne d'une
   porte dérobée dans un raisonneur à trajectoire latente continue fait tomber la séparabilité **seulement** à la
   position latente visée par la perte ; une sonde neuve lue ailleurs dans la trajectoire retrouve entièrement le
   signal (« destruction sans déplacement ») (« Abstract »).
2. **Aucune évasion détectable** contre un modèle de même capacité à chaîne de pensée explicite, à toute intensité
   (« Abstract »).
3. **Hétérogénéité déclarée** : l'étendue de la baisse s'élargit à l'échelle intermédiaire et le succès de l'attaque
   dépend de la graine à la plus grande ; les auteurs en tirent une borne à la généralisation d'un résultat de sondage
   à une seule échelle (« Abstract »).

## Conditions et limites de la lecture

- Résumé seul ; modèles « raisonneurs récurrents continus » entraînés par les auteurs ; tailles non données dans le
  résumé ; trois graines.

## Ce que ça touche chez nous (avis)

- Hypothèse Tr et règle d'agrégation : contre-indice symétrique (R4) aux évasions d'agrégation (D7 de session-depot) ;
  lire sur plusieurs positions et couches avec une sonde de réserve neuve borne l'évasion localisée ; résultat à ne pas
  transposer à une seule échelle (les auteurs le disent).

## Phrase citée

« Across a full λgrid and three seeds, the attack produces real but narrowly localized evasion: separability collapses
only at the exact latent position the loss term targets, is fully recovered by a fresh monitor probing anywhere else in
the (redundant, untouched) trajectory, and never rises elsewhere – destruction without relocation. » (« Abstract »)
