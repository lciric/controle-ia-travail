# Fiche — captures d'écran du papier ASIS&T 2025, doi 10.1002/pra2.1298 — v1

conv-audit, 31 octobre 2026, ≈ 11:45 UTC. **24 captures d'écran** transmises par Lazar (12:43 heure de Paris), du lecteur en ligne de Wiley (`asistdl.onlinelibrary.wiley.com/doi/epdf/10.1002/pra2.1298`), pages 1 à 9 sur 10, scellées une à une (`capture-01.png` à `capture-24.png`). **Ce n'est pas un PDF empreinté** : rien de ce qui suit n'est opposable (R7) tant que le PDF n'est pas versé. Le titre exact et les noms complets des auteurs n'apparaissent pas dans les captures (initiales A.J.Y., S.Y., Z.S.X., Z.Y., D.S. ; financement NSFC n° 724B2015 et Jiangsu KYCX25_0133) : à relever sur la page de titre.

## Ce que dit le papier (d'après les captures ; pages du volume 799 à 807)

- **Objet** : un cadre « human-aware AI » qui prédit des « changements de paradigme » en joignant un **graphe de connaissances du domaine** (sciences de la vie ; PubMed et OpenAlex ; entités extraites par un ensemble de quatre modèles BERT, relations par PubMedBERT, Hetionet, primeKG) et un **espace collaboration–compétition des chercheurs** (cosignature = collaboration ; recouvrement d'entités sans cosignature = compétition, mesure c(s_i, s_j)), dans un réseau hybride d'ordre supérieur traité par un réseau de neurones convolutif sur graphe (p. 800 à 803).
- **Critère des paires de thèmes candidates** (p. 804) : distance de connaissance d_K grande (> θ_K, « nouveauté »), **distance sociale d_S petite** (< θ_S, « potentiel de collaboration », plus court chemin moyen entre chercheurs des deux thèmes), **densité d'experts** ρ élevée dans les deux thèmes (> θ_ρ). Thèmes par K-moyennes sur les plongements.
- **Temps** : réseaux par tranches, plongements avec décroissance exponentielle, puis un LSTM entraîné sur des « changements de paradigme historiques » (découvertes primées par un Nobel reliant des champs disparates) comme **exemples positifs**, qui sort une probabilité de changement à t + Δt (p. 805).
- **Validation déclarée** : « s'aligne sur des jalons historiques » (Nobel) ; limites reconnues : biais des bases, cosignature comme seule mesure sociale, erreurs d'extraction, sciences de la vie seulement, continuité supposée (p. 806–807).

## Pertinence pour le programme (à éprouver)

1. **Antériorité d'E1′ (base de ponts)** : leur critère « distance de connaissance grande + distance sociale petite + densité d'experts » est un **voisin direct** de notre profil « trou à structure commune » (communication faible + structure commune forte). Différences à écrire : nous mesurons la **structure commune** (objet, méthode), eux la distance de plongement ; ils ajoutent un **canal social** que notre E1′ n'a pas ; leur « densité d'experts » ressemble à notre témoin « popularité ».
2. **Témoin ou covariable** : la distance sociale (cosignature) peut entrer dans E1′ comme **témoin supplémentaire** ou covariable déclarée ; à décider (DE-n).
3. **Ce qu'ils ne font pas** (d'après les captures) : aucune épreuve prospective scellée, aucune rétrodiction inversée, aucun témoin « distance seule » ou « popularité seule » rapporté, positifs choisis après coup (Nobel) — exactement ce que nos garde-fous de R-878 visent. Zone « prédiction de ponts avec contrôle de rétrodiction et témoins » : **non occupée par ce papier**, à vérifier ailleurs (R8).
4. **Course 2 et bras méta** : le canal social est absent de nos bras ; piste à noter pour la génération 2.

À faire : verser le PDF (Wiley ; peut-être derrière un mur) ; titre et auteurs exacts ; lecture vérifiée page par page par un lecteur neuf avant toute citation.
