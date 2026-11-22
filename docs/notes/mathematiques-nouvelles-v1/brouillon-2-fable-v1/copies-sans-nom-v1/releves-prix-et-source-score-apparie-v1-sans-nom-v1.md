# Relevés : prix des quatre modèles et source du score apparié (v1)

- Classe C (travail), 0 USD ; relevé du 22 novembre 2026 par un Opus 5.5 neuf, pour les blancs « PRIX-VÉRIFIÉS » et `<<SOURCE_TANGO>>` du brouillon du préenregistrement du pilote « oracles plantés » et pour le § 1 et le § 6, point 1, du devis. Rien n'est décidé ici.

## 1. Prix relevés sur les pages publiques (USD par million de jetons, palier standard)

| modèle | identifiant d'API publié | entrée | sortie | cache | page archivée (`docs/sources/prix/`) et empreinte | relevé (UTC) |
|---|---|---|---|---|---|---|
| Claude Opus 5.5 (Anthropic) | `claude-opus-5-5` | 4 | 20 | lecture 0,20 (0,05 × entrée) ; écriture 5 (5 min), 8 (1 h) | `page-prix-anthropic-docs-20261122T104128Z.md` `488e03e9…` (et `page-prix-anthropic-20261122T104128Z.html` `c73e502e…`, même chiffres) ; identifiant : `page-modeles-anthropic-docs-20261122T104339Z.md` `41f5ac40…` | 10:41:28 ; 10:43:39 |
| Gemini 4 Argon (Google) | `gemini-4-argon` | 2 jusqu'au 30 nov. 2026 ; 4 dès le 1er déc. 2026 | 10 puis 20 (réflexion comprise) | 0,10 puis 0,20 ; cache implicite seulement (explicite non pris en charge) | `page-prix-gemini-api-20261122T104129Z.html` `d3aa716e…` | 10:41:29 |
| Kimi K3.1 Pro (Moonshot) | `kimi-k3.1-pro` | 2 | 10 | entrée en cache 0,20 ; écriture 2 (5 min), 4 (1 h) ; cache activé d'office, durée 5 min par défaut | `page-prix-kimi-20261122T104131Z.html` `4624854e…` (platform.moonshot.ai, renvoyée vers platform.kimi.ai) ; page chinoise `page-prix-kimi-cn-20261122T104133Z.html` `24361c67…` : ¥13 / ¥68 / ¥1,30 | 10:41:31 ; 10:41:33 |
| GPT-6.2 Astra (OpenAI) | `gpt-6.2-astra` | 8 | 40 | entrée en cache 0,40 ; écriture 10 (30 min), 20 (12 h) | `page-prix-openai-api-20261122T104130Z.html` `fd24cde9…` (platform.openai.com/docs/pricing, renvoyée vers developers.openai.com/api/docs/pricing) | 10:41:30 |

Empreintes complètes dans les compagnons `.sha256` de chaque fichier.

Paliers et règles relevés :
- **Opus 5.5** : contexte de 1 million de jetons au prix standard sur toute la fenêtre (pas de palier long) ; lots à moitié prix (2 / 10) ; mode rapide 8 / 40 ; `inference_geo: "us"` multiplie tout par 1,1.
- **Argon** : changement de prix daté (doublement le 1er décembre 2026) ; lots 1 / 5 puis 2 / 10 ; aucun palier de longueur de contexte sur la page. Prix d'entrée et de sortie standard identiques sur `page-prix-gemini-api-20261108T054611Z.html` (`ad2140dd…`) et `…20261121T134918Z.html` ; la phrase de présentation du modèle a changé entre le 8 et le 21 novembre (le reste de la page n'a pas été comparé ligne à ligne).
- **Kimi K3.1 Pro** : contexte de 1 048 576 jetons, aucun palier ; lots à 60 % du prix standard ; variante `kimi-k3.1-pro-highspeed` à 4 / 20.
- **GPT-6.2 Astra** : sélecteur de longueur de contexte « Short : ≤ 272K input tokens / Long : > 272K input tokens » ; **les prix longs du palier standard ne figurent pas dans la page statique** (calculés dans le navigateur) : non relevés. Lots 4 / 20 ; mode rapide 16 / 80 ; « Ultrafast » 3 × standard jusqu'au 28 février 2027, 6 × dès le 1er mars 2027 ; requêtes de fond 30 % (fenêtre 2 h) ou 40 % (8 h) sous le standard ; points de traitement régional +10 %. Le « GPT-6 Astra » du devis existe aussi (`gpt-6-astra`, 10 / 50, cache 1,00) : c'est le barème que le devis avait supposé ; l'identifiant servi par le collisionneur, `gpt-6.2-astra`, coûte 8 / 40.

Écarts au devis v1 (constat, sans décision) : Opus 5.5 et Kimi K3.1 Pro égaux aux chiffres employés ; Argon : la page confirme 2 / 10 puis 4 / 20, le devis garde 10 / 50 par prudence ; Astra : 8 / 40 pour `gpt-6.2-astra` contre 10 / 50 supposés.

## 2. Source du score apparié (`<<SOURCE_TANGO>>`)

- **PDF primaire non obtenu.** Tango 1998 (Statistics in Medicine 17(8) : 891-908) est fermé (OpenAlex : `oa_status: closed`, aucun dépôt) ; pages de l'auteur à l'institut japonais : 404 ; une copie sur une page de cours d'Ottawa existe, statut légal non établi, non téléchargée.
- **Source secondaire versée, non PDF** : code GPL-3 du paquet R `contingencytables` 3.1.1 (CRAN, 27 octobre 2026), compagnon du livre de Fagerland, Lydersen et Laake, fonction « The Tango asymptotic score confidence interval for the difference between paired probabilities ».
  - `docs/sources/pdf/score-apparie-tango-v1/contingencytables-3.1.1-Tango_asymptotic_score_CI_paired_2x2.R`, sha256 `5248271a97b7f612e375c2602c8a1e62c4a3f4769fe4930c6ad0daa3bf016f31` ; archive servie `cran-contingencytables_3.1.1-20261122T1046Z.tar.gz`, `0378dd181fb2d0abd0c6f4b0b1655a9337a7f9dfd6de5b5d39857c4ed19ac333` ; provenance `provenance-score-apparie-tango-v1.md`, `186dbf2d…`.
  - Lignes 93-96 : `A <- 2 * N` ; `B <- -n12 - n21 + (2 * N - n12 + n21) * delta0` ; `C <- -n21 * delta0 * (1 - delta0)` ; `p21tilde <- (sqrt(B^2 - 4 * A * C) - B) / (2 * A)`. Ligne 83 : `T0 <- (n12 - n21 - N * delta0) / sqrt(N * (2 * p21tilde + delta0 * (1 - delta0)))`.
  - **Identité** : identique, aux signes près, à la forme du brouillon, avec n₁₀ ↔ `n12`, n₀₁ ↔ `n21`, n ↔ `N`, q ↔ `p21tilde`, Δ₀ ↔ `delta0`. Aucun écart de signe ni de coefficient.
- Consultées, non identiques terme à terme : NCSS, chapitre 520, « Nam's Score » (renvoi « Nam (1997) or Tango (1998) »), p. 520-4, autre paramétrisation ; Huang et Self 2010 (PMC3481840), quadratique à convention de marge opposée, PDF non téléchargeable par programme.

## 3. Réserves

1. R7 demande un PDF empreinté et une page citée : la source versée est du code, cité par lignes. L'attribution à Tango reste de seconde main. Que le directeur l'admette, ou que le brouillon garde son repli écrit (statistique définie par ses principes, sans attribution).
2. Prix longs (> 272K jetons d'entrée) de `gpt-6.2-astra` en palier standard non relevés : à lire dans un navigateur si un appel peut dépasser ce seuil.
3. Argon change de prix le 1er décembre 2026 : à dater selon le jour de la course.
4. Pages relevées sans compte. Les prix peuvent différer pour un compte donné (contrats, taxes) ; l'accès effectif à Astra n'est pas vérifié.
5. La page `openai.com/api/pricing` renvoie vers des tarifs « Business » sans les prix d'API : non archivée.
