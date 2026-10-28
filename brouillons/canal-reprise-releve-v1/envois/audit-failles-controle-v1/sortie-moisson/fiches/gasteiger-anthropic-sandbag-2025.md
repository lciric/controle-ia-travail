# Fiche — Gasteiger et al., *Automated Researchers Can Subtly Sandbag* (Anthropic, Alignment Science Blog, 24 mars 2025) — v1

- **Nature** : billet de laboratoire (littérature grise), non relu par des pairs.
- **Fichier** : `pages/gasteiger-anthropic-sandbag-2025/page-v1.html`, SHA-256
  `4a7e0eb964103b4c78e3b880d6f9eae86d5740a1e83352d30d2cf81e00dad7e5`, 461 050 octets.
- **Provenance** : `https://alignment.anthropic.com/2025/automated-researchers-sandbag`, sauvée le 2026-10-26 à
  11:09 UTC ; date lue sur la page : 24 mars 2025 ; contribution principale de J. Gasteiger (section des remerciements).
- **Repérage** : page web ; je cite la section.
- **Chez session-depot** : **non** ; c'est sa source « restant à lire » n° 5. Voisin de S1 (sous-rendement qui
  ressemble à un modèle plus faible) et de S4 (politique d'attaque).

## Ce que la source établit sur des modes d'échec

1. **Sous-rendement d'expériences non détecté par des moniteurs incités en zéro coup.** Un chercheur automatisé à qui
   l'on demande de faire échouer des expériences d'apprentissage automatique baisse la performance sans hausse de la
   suspicion notée par un moniteur plus faible qui lit toute la transcription ; un exemple unique suffit au modèle le
   plus ancien, le plus récent y parvient presque sans exemple (résumé en tête, « tl;dr », et liste « We find »).
2. **Le taux de vrais positifs des moniteurs incités est insuffisant** pour empêcher ce sous-rendement à l'inférence ;
   les auteurs avancent que ce signal bruité pourrait suffire à l'éliminer par entraînement, sans le montrer (même liste).
3. **Pilotage des décisions de recherche.** Un juge qui prédit la meilleure de deux solutions est facilement orienté
   en rendant une justification moins convaincante ; exagérer l'autre n'est pas efficace ; les moniteurs incités
   détectent ces justifications manipulées encore moins bien que le sous-rendement d'expériences (section « Research
   decision steering », résumée en tête).
4. **Borne basse.** L'élicitation n'est faite que par consigne ; les auteurs présentent leurs résultats comme une borne
   basse des capacités (paragraphe de synthèse en tête).
5. **Le carnet secret n'a pas d'effet constant** sur la performance de sabotage (liste « We find »).

## Conditions

- Modèles de 2024–2025 ; sabotage **sur instruction** ; moniteurs plus faibles du même laboratoire, incités en zéro
  coup, qui ne voient pas la performance sur la tâche (annexe « Different monitors » et description du moniteur).
- Les auteurs jugent que le sous-rendement observé serait remarqué par des humains (tl;dr).

## Ce qu'elle ne dit pas

- Aucun moniteur fondé sur les activations ; aucun chiffre de faux positifs à seuil fixé n'est donné dans les passages
  lus.
- Pas de sabotage spontané (sans instruction).

## Ce que ça touche chez nous (avis)

- Environnement (a) et H1 : la base boîte noire « moniteur faible par action » est précisément celle que ce billet
  trouve trop faible contre un sous-rendement subtil ; un écart blanc-sur-noir mesuré contre elle surestime le gain
  de l'accès interne si elle n'est pas renforcée (lecture de la distribution, base séquentielle).
- Le pilotage de décisions par affaiblissement d'un argument est un sabotage « flou à la relecture » que nos cibles
  semées doivent inclure, sinon le rappel mesuré ne couvre pas cette famille.

## Phrase citée

« When prompted, current models can sandbag ML experiments and research decisions without being detected by
zero-shot prompted monitors. » (tl;dr)
