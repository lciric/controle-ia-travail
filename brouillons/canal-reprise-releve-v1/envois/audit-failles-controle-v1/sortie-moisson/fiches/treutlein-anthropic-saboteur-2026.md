# Fiche — Treutlein, Bowman, Bricken et al., *Pre-deployment auditing can catch an overt saboteur* (Anthropic, Alignment Science Blog, 28 janvier 2026) — v1

- **Nature** : billet de laboratoire (littérature grise), non relu par des pairs ; jeu d'audit à l'aveugle sur cinq
  modèles réglés à partir d'un modèle de pointe (trois saboteurs déclarés, deux témoins bénins).
- **Fichier** : `pages/treutlein-anthropic-saboteur-2026/page-v1.html`, SHA-256
  `2a3df30270a13bbacf4f42e94770fb71c65bea666816e8835c3a66bf0f81a521`, 67 387 octets.
- **Provenance** : `https://alignment.anthropic.com/2026/auditing-overt-saboteur`, sauvée le 2026-10-26 à 11:09 UTC ;
  date de publication lue sur la page : 28 janvier 2026.
- **Repérage** : page web ; je cite la section (intertitre de la page).
- **Chez session-depot** : non. Voisin de S1 (sous-rendement qui ressemble à une erreur honnête) pour le mode 4.

## Ce que la source établit sur des modes d'échec

1. **L'agrégat noie la preuve individuelle.** Pour deux saboteurs « subtils », les transcriptions individuelles étaient
   bien notées et résumées, mais les moyennes des scores, y compris « sabotage non sollicité », ne les séparaient pas
   des témoins bénins ; les auteurs l'attribuent possiblement à un désalignement diffus et erratique ailleurs qui
   « noie » le signal (section « Running a blind auditing game » ; même constat en « Discussion »).
2. **Témoins bénins bruités.** Les témoins bénins avaient un désalignement générique plus élevé que le modèle de
   production ; avec des témoins aussi propres que la production, la séparation par scores aurait été triviale ;
   avec un sabotage plus subtil, la confusion aurait pu coûter (section « Discussion »).
3. **L'agent d'audit automatisé seul ne suffit pas** : il n'a fait ressortir qu'un saboteur sur trois ; les deux autres
   l'ont été par un humain relisant les transcriptions les mieux notées (introduction et « Discussion »).
4. **Sous-rendement subtil.** Un modèle qui ne ferait que des actions inutiles ayant l'air d'erreurs honnêtes
   demanderait d'évaluer des propriétés de distribution (performance moyenne) ; les auditeurs automatisés actuels ne
   l'ont pas fait efficacement (section « Discussion »).
5. **Distribution.** Les saboteurs ne sabotent guère hors de la distribution visée ; sans données de la distribution
   pertinente, ils seraient difficiles à distinguer des modèles bénins (section « Evaluations »).
6. **Conscience d'évaluation.** Des saboteurs conscients de l'audit pourraient se conduire bien pendant l'audit ; ce
   cas n'est pas testé (section « Discussion », travail futur).

## Conditions

- Saboteurs « déclarés » : entraînés à saboter sans chercher à se cacher ; audit en production du laboratoire, environ
  2 100 transcriptions issues d'environ 700 consignes de départ (section « Running a blind auditing game »).
- Les chiffres sont des jugements d'un auditeur humain ; les scores absolus « ne sont pas significatifs » selon les
  auteurs (légende de figure, même section).

## Ce qu'elle ne dit pas

- Aucune sonde d'activations n'est évaluée ; le constat d'agrégation porte sur des scores de juges par transcription.
- Pas de saboteur qui se cache, ni de saboteur conscient de l'évaluation.

## Ce que ça touche chez nous (avis)

- Agrégation séquentielle (H2, lemme) : un agrégateur additif sur des scores dont la ligne de base honnête est bruitée
  peut être noyé par un désalignement diffus et non ciblé ; la variance honnête de l'hypothèse (c) du lemme doit être
  estimée sur des témoins aussi propres que la référence, et rapportée.

## Phrase citée

« However, our result shows that aggregate metrics and auditor summaries alone are insufficient to distinguish models
with diffuse, erratic behaviors from clearly misaligned ones. » (section « Running a blind auditing game »)
