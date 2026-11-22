# Relecture par Claude Fable 5.2 (appel direct à l'interface d'Anthropic)

- Outil : `controle_ia.relecture_fable_api_v5` (empreinte du module 052ea1e2c66f8b80b1724db9f0c5afb27a48cc01eac2e1e5210658ca8423bdb8)
- Modèle demandé : `claude-fable-5-2` ; modèle servi : `claude-fable-5-2` ; identifiant du message : `msg_011ChHtkJxWdQGZ6CbCiTH6h`
- Heure (UTC) : 2026-11-22T11:37:30Z
- Réglages : effort `max`, réflexion adaptative à affichage « omitted » (texte de la réflexion ni demandé ni écrit), `max_tokens` 128000, aucune relance, aucun repli vers un autre modèle, budget de tâche 96000 jetons (bêta `task-budgets-2026-03-13` ; cible indicative vue par le modèle, pas une borne : seul `max_tokens` arrête)
- Entrées :
  - consigne : `docs/notes/demandes-fable-api-2026-11-22-v1/consigne-demande-approfondie-v1.md` — sha256 8263a1b41f0c2050f3715f5df01b0a6d70846840af0e41a3fa19f275ce3c55b2 (compagnon : vérifié)
  - correction : `docs/notes/demandes-fable-api-2026-11-22-v1/demande-27-erratum-interne-et-programme-v3-v1.md` — sha256 9e265f9840b818621d8a16280aba1ba96b66cff3cc10185cde5da244fb86edda (compagnon : vérifié)
  - correction : `docs/programme-controle-ia-v2.md` — sha256 2fd63badb5afea48f48d3ca501ae3b027c4094a8b176508488a41a22e45aa18c (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-9/relecture-fable-api.md` — sha256 48d4d72e5f1cbcdea6a60fea309e80f4e5f319e30389540acc7aa422bd560e52 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-22/relecture-fable-api.md` — sha256 22c5652113797a399d1d1df7fc8d4d6b100bcf04bd655118d51238c5ef3d7b64 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-4/relecture-fable-api.md` — sha256 cf55c7e073a1b99d2229bd08a96eb29e63878477379311b49227c5c5b6950344 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-8/relecture-fable-api.md` — sha256 d81a74d3c62220488d873a5d102dafc126b6d7f985777ec55723e9dc4fd6e9b5 (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/note-problematiques-programme-v1-sans-nom-v1.md` — sha256 4f2316edfdccc67bf60235a8cde7f8e43861c1261ea8c73708059faa0a7ef119 (compagnon : vérifié)
  - remarques : `docs/notes/recherche-exhaustive-transposition-v2.md` — sha256 2395ea20a570afd7b206bec4adec56664604a500902c68cf68eed87358ae9b8d (compagnon : vérifié)
  - remarques : `docs/notes/demandes-fable-api-2026-11-22-v1/copies-sans-nom-v1/table-revendications-en-vigueur-v1-sans-nom-v1.md` — sha256 02453d1d92fc589150cf6e27bed56a996aea8a3de86d8580629ecc8cb8e7cddc (compagnon : vérifié)
- Empreinte de l'invite envoyée : d17941720529511cc14e8d048c86c74923926e93c36ed6db61687fb659e1215a
- Jetons : entrée 98656, sortie 36607 (dont réflexion 25792), écriture de cache 0, lecture de cache 0 ; raison d'arrêt `end_turn`
- Coût compté : 2.253528 USD (base : usage ; tarif 8 / 40 USD par million de jetons d'entrée / de sortie)

---
# Demande 27 — erratum interne et version 3 du programme : réponse approfondie

**Conclusion d'abord.** Les deux pièces sont écrites ci-dessous : un erratum de 31 entrées (réponse 4 : 8 ; réponse 8 : 6 ; note des problématiques : 10 ; section 3 du programme : 7, par renvoi) et une version 3 en 19 différences. Trois limites : quatre des douze phrases de la réponse 22 ne figurent dans aucune des quatre pièces visées ; plusieurs textes NOUVEAU portent une hypothèse que les simulations n'ont pas encore tranchée ; la copie des ANCIEN est faite à la main, sans contrôle par programme. Confiance d'ensemble : 0,7.

**Réserves.**
- Je n'ai lu aucun PDF. Toute antériorité a le statut « rapporté, non vérifié sur PDF ». Je ne confirme aucun identifiant arXiv de 2026.
- Je n'ai ni le texte de N-003 (connu par la table et la réponse 22), ni la note de lecture sur la stéganographie. Ses deux phrases me sont connues par le résumé de la note des problématiques.
- Les réponses 4, 8, 9 et 22 viennent du même modèle que celle-ci : mon accord avec elles n'est pas une confirmation indépendante.
- Empreintes non recalculées. Je ne nomme que les auteurs des travaux cités.
- Convention de marquage : tout ANCIEN est un FAIT RAPPORTÉ (copie des pièces jointes) ; tout NOUVEAU est une PROPOSITION ; toute raison est un FAIT RAPPORTÉ des réponses 9 et 22, sauf mention HYPOTHÈSE.

## 1. Ce qu'un expert ferait et qui n'est pas demandé

Toutes les puces sont des PROPOSITIONS.
- **Appliquer les différences par programme.** Chaque ANCIEN doit être trouvé exactement une fois, puis la version 3 entière relue pour ses renvois orphelins (phase 0, « simulation du lemme » ; section 15, « co-auteur pour le lemme »).
- **Chercher les 24 phrases dans tout le dépôt**, non dans quatre pièces : préenregistrements, table des revendications, recherche exhaustive.
- **Corriger aussi les sources de l'erratum.** La réponse 9 écrit « inexact » sans la borne de N-003, ce que la réponse 22 corrige.
- **Simuler avant de sceller** toute phrase neuve qui contient une hypothèse.

## 2. Données brutes de départ

- Les fichiers à empreinte eux-mêmes, octet par octet, et non leur copie dans l'invite.
- Le texte de N-003 et les deux phrases de la note de lecture sur la stéganographie.
- Les pages citées de Ker 2010 (p. 7 et 11) et d'Avenhaus et Jaech 1981 (p. 25, 30 et 31).

## 3. Méthodes et outils

- Recherche de chaîne exacte avec compte égal à un, puis application à blanc et comparaison des versions 2 et 3.
- Contre-lecture par une instance qui n'a rien écrit ici.
- Trois simulations de la réponse 22 : franchissement séquentiel, copule à marginales préservées, carré de la somme.

## 4. Ce qui vérifie hors du directeur et de Claude

- Le programme d'application : son issue ne dépend d'aucun avis.
- Un spécialiste de stéganalyse et un statisticien des garanties nucléaires, sur les seuls textes NOUVEAU.
- Les auteurs de arXiv 2606.10456, sur la réserve à longueur finie.

## Demande reformulée

« Écris l'erratum et les différences de sorte qu'un programme puisse les appliquer (ANCIEN exact et unique). Dis pour chaque phrase des réponses 9 et 22 où elle se trouve, ou qu'elle est hors des quatre pièces. Signale tout NOUVEAU qui repose sur une hypothèse non simulée. Dis ce que la version 3 ne reporte pas. »

---

# Pièce 1 — Erratum interne

## Réponse 4

**E4-1.** ANCIEN : « La stéganographie et la comptabilité des matières prédisent une loi : le dommage indétectable croît comme la racine de l'horizon si la référence honnête est connue, puis linéairement si elle est estimée. »
NOUVEAU : « La stéganographie et la comptabilité des matières donnent un modèle nul : pour des pas indépendants et une référence de m pas, le dommage indétectable est d'ordre √(n + n²/m) ; il n'est linéaire qu'à référence bornée ou fautive (Ker 2010). »
Raison : forme exacte rapportée (réponse 9, phrase 1). Même correction dans la question Q1 : « croît-il comme la racine de l'horizon tant que la référence honnête est connue, puis linéairement dès qu'elle est estimée ».

**E4-2.** ANCIEN : « Ces lois supposent une couverture ou une valeur comptable connue. »
NOUVEAU : « Ker 2010 traite la référence estimée ; reste non trouvée, dans les pièces lues, leur mesure sur des scores de sondes d'agents. »
Raison : réponse 9, phrase 2.

**E4-3.** ANCIEN : « Personne ne l'a relevé. »
NOUVEAU : « Non relevé dans les pièces lues à cette date ; Khilar 2026 transpose la loi au suivi des usages. »
Raison : zone vierge affirmée sans recherche (réponse 9, phrase 3).

**E4-4.** ANCIEN : « la bascule entre les deux régimes se situe entre m et m divisé par le taux d'audit ; »
NOUVEAU : « à unités égales, la transition est en n ≈ m par construction (Ker 2010, corollaire 1) ; ce n'est pas une prévision ; »
Raison : rien ne fonde la division par le taux d'audit (réponse 9, phrase 4). Même correction pour « le point de bascule (m ou m divisé par le taux d'audit) ».

**E4-5.** ANCIEN : « l'exposant du bruit honnête dépasse un demi, parce que les trajectoires réelles sont dépendantes et les tâches hétérogènes ; »
NOUVEAU : « l'exposant reste un demi sous dépendance courte, qui gonfle la constante (Filler, Ker et Fridrich 2009) ; seule une dérive le long de la tâche le change ; l'hétérogénéité entre tâches ajoute un terme linéaire ; »
Raison : réponse 9, phrase 5.

**E4-6.** ANCIEN : « La loi de la référence passe de règle interne à résultat mesuré (candidate R1 de la demande 2). »
NOUVEAU : « La règle de la référence est l'application du corollaire 1 de Ker 2010 ; rien n'y est revendiqué. »
Raison : réponse 9, phrase 6.

**E4-7.** ANCIEN : « **Les deux issues ferment quelque chose.** »
NOUVEAU : « Deux issues ferment quelque chose si le plan a la puissance de les séparer ; sinon l'issue est indéterminée. »
Raison : réponse 22, phrase 10.

**E4-8.** ANCIEN : « La sonde change [la constante, non l'exposant] ; la taille de la référence fixe l'horizon défendable. »
NOUVEAU : « Prévision scellée, non constat : la sonde change la constante, non l'exposant. La taille de la référence fixe l'horizon défendable (Ker 2010, corollaire 1). »
Raison : réponse 9, phrases 12 et 6.

## Réponse 8

**E8-1.** ANCIEN : « La loi héritée dit que le dommage caché croît comme la racine de l'horizon, puis linéairement, avec une constante fixée par la détectabilité par action. »
NOUVEAU : « Le modèle nul hérité dit que le dommage caché est d'ordre √(n + n²/m), avec une constante propre au moniteur. »
Raison : réponse 9, phrase 1.

**E8-2.** ANCIEN : « la puissance ne peut venir que d'une relation entre mâchoires. »
NOUVEAU : « à marginales préservées, l'espérance des statistiques additives est inchangée ; une statistique de relation entre mâchoires est le test efficace, non le seul puissant. »
Raison : lettre du théorème inexacte (réponse 9, phrase 8).

**E8-3.** ANCIEN : « « Ce qu'un saboteur diffus peut cacher croît avec l'horizon selon une loi dont l'exposant dépend de la référence honnête et dont la constante dépend des moniteurs. » »
NOUVEAU : la thèse retenue, écrite en D3 de la pièce 2.
Raison : la loi est le modèle nul cité, non la thèse. Même correction pour « la loi héritée en thèse ».

**E8-4.** ANCIEN : « À fausse alerte jointe α, sur les sabotages que la meilleure boîte noire manque, la boîte blanche en rattrape une part c strictement supérieure à ce que rattrapent, au même budget, une seconde boîte noire d'une autre lignée et la sonde aléatoire appariée. »
NOUVEAU : « À taux total de fausses alertes égal, l'union "meilleure boîte noire et sonde" rattrape plus de sabotages diffus que l'union "meilleure boîte noire et seconde boîte noire d'une autre lignée" ; même épreuve pour la sonde aléatoire appariée. »
Raison : conditionner sur les manqués avantage tout moniteur peu corrélé au premier (réponse 22).

**E8-5.** ANCIEN : « L'horizon du gain est borné [FAIT RAPPORTÉ, N-076] : pas de gain au-delà de n = m. »
NOUVEAU : « L'horizon est borné : aucune conclusion au-delà de n = m (N-076, application du corollaire 1 de Ker 2010), m et n comptés dans la même unité. »
Raison : réponse 9, phrase 6.

**E8-6.** ANCIEN : « **Deux issues publiables.** »
NOUVEAU : « Deux issues publiables si la puissance du plan est calculée ; sinon une troisième, indéterminée. »
Raison : réponse 22, phrase 10.

## Note des problématiques (version 1)

**EN-1.** ANCIEN : « *Théorème négatif* : **contredit** par Arias-Castro, Bubeck et Lugosi 2012 »
NOUVEAU : « *Théorème négatif* : inexact dans la lettre de la version 2 du programme, que N-003 avait bornée, et contredit dans cette lettre par Arias-Castro, Bubeck et Lugosi 2012 »
Raison : réponse 22, phrase 8.

**EN-2.** ANCIEN : « Seule forme défendable : une statistique dont la *loi* ne dépend que des marginales est aveugle »
NOUVEAU : « Formes défendables : celle de N-003 (attaque qui préserve le multi-ensemble des scores, statistiques symétriques) et l'espérance inchangée des statistiques additives »
Raison : retrait excessif signalé par la réponse 22.

**EN-3.** ANCIEN : « Rien n'est tranché : c'est ta décision 1 (section 4). »
NOUVEAU : « Tranché le 22 novembre : cette thèse est retenue ; les décisions 1, 2 et 3 de la section 4 sont closes. »
Raison : mot du directeur.

**EN-4.** ANCIEN : « Revendication resserrée au seul reste : une borne inférieure de la probabilité d'alarme, valide à tout instant, fonction du seul dommage total »
NOUVEAU : « Retiré comme résultat le 22 novembre, reste compris ; gardé mentionné comme énoncé occupé hors du contrôle de l'intelligence artificielle ; la forme séquentielle devient une question »
Raison : modification de revendication accordée. Même correction pour « revendication resserrée, à démontrer (erratum 3 v2) ».

**EN-5.** ANCIEN : « théorème retiré comme résultat (recommandé) »
NOUVEAU : « théorème retiré comme résultat (décidé), gardé mentionné »
Raison : mot du directeur.

**EN-6.** ANCIEN : « candidate, rang 1 (réponse 9) »
NOUVEAU : « retenue le 22 novembre »
Raison : mot du directeur.

**EN-7.** ANCIEN : « *Complémentarité* (la boîte blanche rattrape-t-elle, parmi les manqués de la meilleure boîte noire, plus qu'une seconde boîte noire d'une autre lignée ?) : **non trouvée** dans les pièces lues. »
NOUVEAU : « *Complémentarité* (à taux total de fausses alertes égal, l'union de la meilleure boîte noire et de la sonde rattrape-t-elle plus que son union avec une seconde boîte noire d'une autre lignée ?) : non trouvée, 13 pages lues sur 39 chez le parent le plus proche. »
Raison : réponse 22, phrase 9, et énoncé à taux total égal.

**EN-8.** ANCIEN : « La garantie de fausses alertes reste. »
NOUVEAU : « La garantie de fausses alertes reste, sous une référence honnête de taille m déclarée, pour un horizon au plus m. »
Raison : réponse 22, phrase 4.

**EN-9.** ANCIEN : « en vigueur comme protocole ; candidate comme mesure »
NOUVEAU : « en vigueur comme protocole, application du corollaire 1 de Ker 2010 ; rien n'est revendiqué »
Raison : réponse 9, phrase 6.

**EN-10.** ANCIEN : « La recherche exhaustive d'antériorité sur la transposition, que tu as demandée ; aucun verdict n'en est versé dans les pièces que j'ai lues. »
NOUVEAU : « La recherche exhaustive est rendue (version 2) : la loi en racine est déjà transposée au suivi des usages (Khilar 2026) ; "premier à transposer" ne s'écrit pas ; quatre arbres de citations restent à parcourir. »
Raison : pièce versée depuis.

## Section 3 du programme, version 2

Sept entrées, dont l'ANCIEN et le NOUVEAU sont écrits une seule fois, dans la pièce 2.

| Entrée | Différence | Raison |
|---|---|---|
| EP-1 | D5 | La thèse n'est plus celle du titre. |
| EP-2 | D6 | Le lemme n'est plus candidat. |
| EP-3 | D7 | Réponse 9, phrase 11. |
| EP-4 | D8 | Réponse 9, phrase 7 ; réponse 22, phrase 8. |
| EP-5 | D9 | Réponse 9, phrase 9. |
| EP-6 | D10 | Réponse 22, phrase 10. |
| EP-7 | D11 | Réponse 22, phrase 7. |

## Phrases hors des quatre pièces

- Réponse 22, phrases 1, 2, 11 et 12 : elles sont dans la recherche exhaustive (section 5) et dans la table des revendications, non corrigées ici.
- Réponse 22, phrases 3, 5 et 6 : elles sont dans les sections 5 et 10 du programme, corrigées par D13, D18 et D16.
- Réponse 9, phrase 10 (« trois planchers ») : la note la range déjà en limite déclarée ; rien à corriger.

---

# Pièce 2 — Programme, version 3, en différences

**D1.** ANCIEN : « **Programme de recherche — v2 — 4 octobre 2026** (remplace la v1 du 14 septembre 2026) »
NOUVEAU : « **Programme de recherche — v3 — 22 novembre 2026** (remplace la v2 du 4 octobre 2026 ; seuls changent la thèse du papier A, le statut du lemme et du théorème négatif, H1, H2, H3, E1.3, E3.1 et le premier critère de succès) »

**D2.** ANCIEN : « — le même objet mathématique dans le temps (A) et entre agents (B). »
NOUVEAU : « — le même objet mathématique dans le temps (A) et entre agents (B). *(Retirée comme colonne vertébrale par la version 3 : voir section 3.)* »

**D3.** ANCIEN : « La fragmentation détruit la preuve externe, pas la preuve interne : l'accumulation séquentielle de scores de sondes détecte, avec une garantie de faux positifs toujours valide, ce que le max par action rate. »
NOUVEAU : « Les lois de la dissimulation répartie (Ker 2007 et 2010 ; Avenhaus et Jaech 1981), déjà transposées au suivi des usages contre l'extraction (Khilar 2026), donnent un modèle nul du dommage qu'un saboteur diffus peut cacher. Le papier mesure, sur des scores de sondes d'agents qui sabotent, où ce nul tient et quels termes s'y ajoutent ; puis ce que l'accès interne rattrape et qu'une seconde boîte noire ne rattrape pas. »

**D4.** ANCIEN : « H1, H2, L, T, H6, Tr, H8 »
NOUVEAU : « H1, H2, Bi, Q, H6, Tr, H8 ; L et T mentionnés, non revendiqués »

**D5.** ANCIEN : « ## 3. Thèse centrale : additivité interne, lemme et théorème négatif »
NOUVEAU : « ## 3. Thèse centrale : loi héritée comme modèle nul, bilan mesuré, complémentarité

**Thèse (papier A, retenue le 22 novembre 2026).** Celle de la section 2.

**Modèle nul.** Pour des pas indépendants et une référence honnête de m pas, comptés dans la même unité que les n pas surveillés, le dommage caché est d'ordre √(n + n²/m) ; il n'est linéaire qu'à référence bornée ou fautive (Ker 2010). Forme à ajuster : budget caché au carré ≈ z²·(σ²·n^(2H) + σ²·n²/m + τ²·n²). L'écart au nul est le résultat.

**Second axe.** La complémentarité avec une seconde boîte noire, à taux total de fausses alertes égal (H1).

**Citations obligatoires de la thèse.** Ker 2007 ; Ker 2010 ; Avenhaus et Jaech 1981 ; Khilar 2026 (arXiv 2610.13083).

**Statut de ce qui suit.** L'additivité interne, le lemme et le théorème ne sont plus des résultats ; ils restent mentionnés, chacun à son statut. »

**D6.** ANCIEN : « **Lemme (candidat, papier A).** »
NOUVEAU : « **Lemme d'additivité (mentionné, non revendiqué).** Énoncé occupé hors du contrôle de l'intelligence artificielle : l'indifférence de la somme à la répartition, à taille fixe (Avenhaus et Jaech 1981 ; Ker 2006). Ancienne lettre, pour mémoire : »

**D7.** ANCIEN : « Énoncé : pour un processus e de mélange au risque α, la puissance de détection ne dépend que de B et de la variance — pas de la répartition du sabotage sur les agents ni sur les pas de temps. »
NOUVEAU : « Ancien énoncé, non revendiqué : la puissance ne dépendrait que de B et de la variance. Établi et cité : à taille fixe, la puissance de la somme ne dépend pas de la répartition. Pour un processus e, question ouverte : l'étalement est-il le cas le moins favorable au défenseur ? Une simulation à budget égal (sabotage tôt, tard, étalé) la tranche avant toute phrase. »

**D8.** ANCIEN : « **Théorème négatif (papiers A et B).** Si le dommage passe par la **corrélation** à marginale préservée, toute statistique fondée sur les marginales (max, moyenne, somme cumulée) a une puissance égale au taux de faux positifs ; il faut un agrégateur d'**autocorrélation** (dans le temps) ou de **co-élévation** (entre agents). »
NOUVEAU : « **Théorème négatif (mentionné, non revendiqué ; papiers A et B).** La lettre de la version 2 (« toute statistique fondée sur les marginales a une puissance égale au taux de faux positifs ») est inexacte. N-003 l'a bornée : vraie quand l'attaque préserve le multi-ensemble des scores, pour les statistiques symétriques ; fausse quand elle ne préserve que les marginales par coordonnée. Arias-Castro, Bubeck et Lugosi 2012 la contredisent : le carré de la somme garde de la puissance en régime dense. Énoncé exact, élémentaire et cité : à marginales préservées, l'espérance des statistiques additives est inchangée ; le test efficace est du second ordre (autocovariance dans le temps, co-élévation entre agents). »

**D9.** ANCIEN : « C'est le même objet mathématique dans les deux papiers : l'indexation agnostique (section 4) n'est pas une commodité de rédaction, le mode d'échec et sa parade se transposent tous les deux. »
NOUVEAU : « L'unité du temps et de l'espace est héritée (Avenhaus et Jaech 1981) ; l'indexation agnostique (section 4) est une commodité de rédaction citée, non un apport. »

**D10.** ANCIEN : « Si oui, le lemme s'applique ; sinon, le théorème négatif dicte l'agrégateur. Les deux issues sont publiables. »
NOUVEAU : « Question Q : déplace-t-il la position des scores, leur dépendance, ou les deux ? Elle se lit par un test de position et un test de dépendance, étalonnés sur des substituts par permutation des pas. Aucune issue n'est dite publiable avant le calcul de puissance du plan ; une issue indéterminée est possible. »

**D11.** ANCIEN : « arXiv 2606.10456 occupe la version boîte noire et synthétique du contraste marginale/corrélation (provenance douteuse, preuves élémentaires). Différenciation : vraies activations de modèle, invariance au budget total, indexation unifiée temps/agents. »
NOUVEAU : « Zhang et Gao 2026 (arXiv 2606.10456) occupent le contraste en boîte noire, sur scores synthétiques puis sur traces réelles où l'attaque est fabriquée sur les scores. Réserve : limite à longueur finie, notre lecture, à vérifier en rejouant leur tableau 2. Aucune différenciation n'est revendiquée. Question : que déplacent, sur des scores de sondes, des attaques jouées par de vrais agents ? »

**D12.** ANCIEN : « Revendicable : la mesure spécifique diffus/flou ; le gain blanc-sur-noir en général est établi. »
NOUVEAU : « Revendicable : la mesure spécifique diffus/flou ; le gain blanc-sur-noir en général est établi (parent à citer avec son indice contraire : Parrack, Attubato et Heimersheim 2025). Complément, second axe de la thèse : à taux total de fausses alertes égal, l'union « meilleure boîte noire et sonde » rattrape plus de sabotages diffus que l'union « meilleure boîte noire et seconde boîte noire d'une autre lignée ». »

**D13.** ANCIEN : « le rappel croît avec l'horizon. Revendicable : l'application aux sondes internes ; le squelette séquentiel boîte noire existe. »
NOUVEAU : « à déplacement par acte fixé, le rappel suit le modèle nul hérité en n et m ; la garantie vaut sous une référence honnête de taille m déclarée, pour n au plus m (application du corollaire 1 de Ker 2010) ; l'écart au nul est le résultat. Le squelette séquentiel boîte noire existe. »

**D14.** ANCIEN : « **L — lemme d'additivité** (0,75). Section 3. »
NOUVEAU : « **L — lemme d'additivité** (mentionné, non revendiqué ; la note 0,75 est caduque). Section 3. »

**D15.** ANCIEN : « **T — théorème négatif** (compté avec L ; la version boîte noire synthétique est occupée, à vérifier). Section 3. »
NOUVEAU : « **T — théorème négatif** (mentionné, non revendiqué ; lettre inexacte, bornée par N-003). Section 3.
- **Bi — bilan mesuré contre le modèle nul** (chance d'un contenu propre : 0,5, jugement). Section 3.
- **Q — position ou dépendance** (question ; non calibrée). Section 3. »

**D16.** ANCIEN : « À budget de sabotage constant, la courbe boîte blanche domine la boîte noire et décroît plus doucement avec N. »
NOUVEAU : « À budget et nombre total d'actions fixés, la somme globale est prédite plate en N et le maximum décroissant (Avenhaus et Jaech 1981) ; la sonde change la constante, non la pente : prévision, non constat. »

**D17.** ANCIEN : « **E1.3** Lemme sur données réelles : la puissance ne dépend-elle que du budget total quand la fragmentation varie ? Test de la condition δ > 0. »
NOUVEAU : « **E1.3** Bilan sur données réelles : essai « jumeau contre jumeau », surface du seuil d'alarme honnête en n et m ajustée au modèle nul, après calcul de puissance ; simulation du franchissement séquentiel ; test de la condition δ > 0. »

**D18.** ANCIEN : « — le cœur vierge. »
NOUVEAU : « — base obligatoire : la somme globale ; gain revendiqué sur les seuls sabotages qui déplacent la dépendance. »

**D19.** ANCIEN : « (1) Lemme et théorème négatif démontrés et testés sur activations réelles, avec le plan 2 × 2 (A) ; »
NOUVEAU : « (1) Bilan mesuré contre le modèle nul hérité et complémentarité à taux total de fausses alertes égal, sur activations réelles, avec le plan 2 × 2 (A) ; »

**Notes sur ces différences.**
- [HYPOTHÈSE] D5, D7 et D16 reprennent la forme nulle, l'inégalité d'étalement et la somme plate de mes réponses 9 et 22, dérivées de ma main et non simulées.
- [FAIT RAPPORTÉ] La version 3 ne reporte aucune décision postérieure au 4 octobre hors de la demande. La marge asymétrique H6, retirée par N-077, y figure encore.

---

## Décisions qui reviennent au directeur

**Décision 1 — Sceller les textes NOUVEAU maintenant, ou après le contrôle par programme et les simulations.**
- *Enjeu.* Trois différences portent une hypothèse non simulée ; l'unicité des ANCIEN n'est vérifiée qu'à la lecture.
- *Option a : contrôle par programme tout de suite, scellement provisoire, D7 et D16 marqués « sous simulation ».* Avantage : plus de phrase fautive en circulation. Inconvénient : deux scellements.
- *Option b : tout sceller maintenant.* Avantage : une passe. Inconvénient : risque de sceller une phrase réfutable, comme le 22 novembre.
- *Option c : attendre les simulations.* Avantage : texte sûr. Inconvénient : la version 2 reste citable.
- *Recommandation.* Option a. Confiance : 0,75.

**Décision 2 — Arrêter la liste des citations obligatoires de la thèse.**
- *Enjeu.* D5 n'inscrit que les quatre sources de ta formulation.
- *Option a : les quatre seules.* Avantage : conforme à ton mot. Inconvénient : les sources de la dépendance courte, du théorème borné et de la complémentarité restent facultatives.
- *Option b : ajouter Ker 2006 ; Filler, Ker et Fridrich 2009 ; Arias-Castro, Bubeck et Lugosi 2012 ; Zhang et Gao 2026 ; Parrack, Attubato et Heimersheim 2025.* Avantage : chaque phrase corrigée a sa source obligatoire. Inconvénient : liste longue, non vérifiée sur PDF de ma part.
- *Recommandation.* Option b, après la lecture ciblée déjà accordée. Confiance : 0,65.

**Décision 3 — Fixer le périmètre de la version 3.**
- *Enjeu.* Elle garde des énoncés que des décisions ont retirés (H6, bascule de H8, « application aux sondes »).
- *Option a : version 3 limitée à cette demande, avec une phrase d'en-tête renvoyant à la table des revendications, version 2.* Avantage : conforme à « rien d'autre ne change ». Inconvénient : programme et table divergent.
- *Option b : version 4 qui reporte toutes les décisions.* Avantage : un seul texte qui fait foi. Inconvénient : chantier, à faire après le collisionneur.
- *Recommandation.* Option a maintenant, option b avec la table version 2. Confiance : 0,7.

**Décision 4 — Étendre l'erratum aux pièces hors périmètre.**
- *Enjeu.* Quatre phrases de la réponse 22 vivent dans la recherche exhaustive et la table ; la réponse 9 porte elle-même une phrase corrigée.
- *Option a : second erratum court sur ces trois pièces.* Avantage : les 24 phrases sont toutes traitées. Inconvénient : une pièce de plus.
- *Option b : laisser à la table version 2.* Avantage : aucun travail. Inconvénient : deux phrases « autorisées » fautives restent citables.
- *Recommandation.* Option a. Confiance : 0,7.

FIN DE LA RÉPONSE
