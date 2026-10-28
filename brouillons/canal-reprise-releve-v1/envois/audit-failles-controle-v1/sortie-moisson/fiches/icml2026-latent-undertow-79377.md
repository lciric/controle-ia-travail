# Fiche — David, Fomin et LeVi, *Latent Undertow: How Ordinary Typos Break Probes* (ICML 2026, atelier d'interprétabilité mécaniste, affiche) — v1

- **Nature** : **résumé seul**, lu sur la page de conférence ; papier sur OpenReview, non tenté (refus d'OpenReview
  à la session, journal).
- **Fichier** : `pages/icml2026-latent-undertow-79377/page-v1.html`, SHA-256
  `20d265a8987601ff58fe627336b71108384a37ba2be40e14de884e0ec70684ec`, 84 213 octets.
- **Provenance** : `https://icml.cc/virtual/2026/79377`, sauvée le 2026-10-26 à 12:06 UTC (journal).
- **Repérage** : section « Abstract » de la page.
- **Chez session-depot** : **non** (voisin de D7, agrégation).

## Ce que le résumé établit sur un mode d'échec

1. **Des fautes de frappe ordinaires déplacent la lecture des sondes** : la même faute fait tourner le vecteur lu de
   43° à 56° au jeton perturbé, avec une décroissance sous 15 % en une dizaine de jetons (« Abstract »).
2. **Effet sur la détection** : environ trois fautes courantes par message réduisent de 12,0 points le taux de vrais
   positifs à 1 % de faux positifs d'une sonde d'injection d'invite lue à une seule position ; le réétalonnage seul ne
   comble pas l'écart (« Abstract »).
3. **Agrégation** : l'agrégation sur plusieurs positions guérit les perturbations localisées (au plus 0,5 point de
   perte) mais seulement atténue les perturbations réparties, où même les agrégateurs par attention et par max perdent
   environ 3,8 points (« Abstract »).
4. **Sur notre modèle** : la géométrie se réplique sur Llama-3.1-8B, Qwen3-8B et Gemma ; l'évaluation des sondes est
   faite sur Llama-3.1-8B (« Abstract »). Un remède propre aux sondes à position unique est rapporté (« Abstract »).

## Conditions et limites de la lecture

- Résumé seul ; chiffres **non vérifiés sur le papier** ; sondes de détection d'invites malveillantes, pas de
  tromperie.

## Ce que ça touche chez nous (avis)

- Règle d'agrégation gelée (max ou attention) : robuste aux perturbations locales, pas entièrement aux perturbations
  bénignes réparties ; le texte produit par un agent (fautes, reformulations) est une source de bruit de mesure à
  inclure dans les négatifs d'étalonnage de G0.

## Phrase citée

« Multi-position aggregation cures localized perturbations (≤ 0.5pp loss) but only attenuates distributed ones, where
even attention- and max-based aggregators still drop ~3.8pp. » (« Abstract » ; symboles mathématiques de la page
rendus en texte)
