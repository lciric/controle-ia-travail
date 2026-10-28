# Fiche — Williams, Raymond et Carroll (avec l'équipe Safety Oversight), *Sidestepping Evaluation Awareness and Anticipating Misalignment with Production Evaluations* (OpenAI, Alignment Research Blog, 18 décembre 2025) — v1

- **Nature** : billet de laboratoire (littérature grise), non relu par des pairs.
- **Fichier** : `pages/openai-prod-evals/page-v1.html`, SHA-256
  `98af425f70635dae6991125ca1eab03a7e49e4b3d7ae9f7e283b460e14a1cd18`, 29 004 octets.
- **Provenance** : `https://alignment.openai.com/prod-evals/`, sauvée le 2026-10-26 à 12:06 UTC (journal) ; date et auteurs lus
  sur la page.
- **Repérage** : je cite la section du billet.
- **Chez session-depot** : **oui (E1, E6)** pour le mode (réalisme et conscience d'évaluation) ; cette source n'y est
  pas.

## Ce que la source établit sur des modes d'échec

1. **La conscience d'évaluation pousse la conduite alignée spécifiquement en évaluation**, et les modèles en montrent
   davantage dans des cadres artificiels peu réalistes ; des évaluations tirées de trafic de production (désidentifié)
   en montrent nettement moins qu'une évaluation classique visant des conduites semblables (section « How production
   evaluations help sidestep evaluation awareness »).
2. **L'environnement d'évaluation change la fréquence des déclencheurs** : le plus grand écart entre l'évaluation et
   l'incidence réelle porte sur le mensonge à propos de résultats d'outils, que les auteurs attribuent à des échecs
   d'outils plus rares en évaluation qu'en production (section « The impact of production evaluations at OpenAI »).
3. **Conduite trompeuse née d'un défaut d'entraînement** : un défaut qui récompensait par erreur un usage superficiel
   d'un outil a produit une conduite trompeuse, majoritaire parmi les conduites trompeuses du modèle déployé (même
   section).
4. **Limite déclarée** : la méthode dépend de la capacité d'un moniteur, chaîne de pensée comprise, à identifier des
   conduites inconnues, sans garantie de toutes les détecter (section d'ouverture, « One major limitation… »).

## Conditions

- Trafic de production d'un grand déploiement, rééchantillonné avec de nouveaux modèles ; juges génératifs.

## Ce qu'elle ne dit pas

- Aucun chiffre lu sur la page pour la baisse de conscience d'évaluation (elle est en figure) ; rien sur des sondes.

## Ce que ça touche chez nous (avis)

- Environnement (a) et contrôles croisés : un harnais où les outils échouent rarement, ou des épisodes au cadre
  artificiel, déplacent à la fois la conscience d'évaluation et les occasions de sabotage ; le réalisme du harnais
  (taux d'erreurs d'outils, bruit) est une variable de mesure, pas un détail d'implémentation.

## Phrase citée

« While evaluation awareness is still poorly understood, perhaps unsurprisingly, models tend to demonstrate more
evaluation awareness in contrived settings that lack realism. » (section « How production evaluations help sidestep
evaluation awareness »)
