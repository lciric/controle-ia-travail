# session-depot → conv-audit — n° 274 — 2 novembre 2026, 13:38 UTC (heure relevée par `date -u`)

**Éléments pour A1-bis**, relevés par la session fille vers 13:45 UTC. Aucun appel n'a été fait et aucun relais n'a été lancé. Seuls les registres de **dépense** et le code ont été lus, jamais le contenu des sorties.

## 1. Espèces, telles qu'elles ont servi

| Espèce | Fournisseur, modèle servi (vérifié) | Chemin d'appel | Sortie maximale | Délai | Porte de plafond |
|---|---|---|---|---|---|
| Fable | Anthropic, `claude-fable-5-1` | `collisionneur_v8.appeler_anthropic` (kit Anthropic, flux, effort « high »), sans relais | 64 000 (128 000 en relance) | kit, 4 reprises | plafond de run du collisionneur ; barème supposé 10 / 50 USD par million |
| Opus | Anthropic, **`claude-opus-4-6`** (et non 5.5) | idem | idem | idem | idem ; barème supposé 15 / 75 |
| Astra | OpenAI, `gpt-6-astra` | `collisionneur_v8.appeler_openai` (chat/completions), sans relais | 32 000 (65 536 en relance) | 1 800 s, reprises sur 429 et 5xx | plafond de run ; barème supposé 10 / 50 ; jetons de raisonnement sans doute comptés deux fois (≈ +5 %, à corriger) |
| Kimi | Kimi, `kimi-k3.1-pro` | `commande_kimi_v2.py` vers `relais_kimi_v3.py`, port 8804 | proposeur 65 536 ; court 16 000 ; minimum 4 096 | commande 1 750 s ; amont 1 700 s ; silence 600 s | porte « environnement » + plafond cumulé du registre + plafond du relais |
| Argon (rappel) | Gemini, `gemini-4-argon` | `commande_argon_v56_nuit_v2.py`, port 8805 | 32 000 ; court 4 000 | 1 750 s | idem Kimi |

**Il n'existe aucune commande externe au format du pôle v56 pour Claude ni pour Astra.** Ce format demande `--registre`, `--plafond-cumule-usd`, `PLAFOND_SESSION_USD`, `ROLE_POLE` et le modèle servi en dernière ligne ; seules les fonctions du collisionneur existent. Il faut donc deux commandes neuves, par exemple sur le modèle de `commande_argon_v56_nuit_v2`, éprouvées hors réseau. Ports libres proposés : 8806 pour Claude, 8807 pour Astra.

## 2. Coût par appel réussi relevé (USD : nombre / moyenne / médiane / maximum)

**Collisionneur v8**, cellules de l'étage III, 4 runs ; entrée d'environ 27 000 à 87 000 jetons, sortie d'environ 5 000 :

| Espèce | Nombre | Moyenne | Médiane | Maximum |
|---|---|---|---|---|
| Fable | 12 | 1,936 | 1,775 | 2,861 |
| Opus 4.6 | 12 | 1,823 | 1,777 | 2,662 |
| Argon | 12 | 1,204 | 1,069 | 1,777 |
| Kimi | 12 | 0,298 | 0,286 | 0,383 |
| Astra | 12 | 0,932 | 0,899 | 1,518 |

Ce sont des barèmes supposés hauts : aucune facture n'a été relue.

**A1**, rôle « proposeur_ideation », entrée d'environ 2 000 jetons :

| Espèce | Nombre | Moyenne | Médiane | Maximum | Échecs |
|---|---|---|---|---|---|
| Argon | 526 | 0,062 | 0,054 | 0,799 | 1 |
| Kimi | 5 | 0,349 | 0,328 | 0,567 | 616 |

Kimi produit beaucoup de raisonnement : 56 270 jetons de sortie pour l'appel à 0,567 USD, et **10 à 25 min par appel**.

Pour Claude et Astra, aucune mesure n'existe sur ce rôle : les valeurs du v8 ne se transposent pas, car l'entrée y est 15 à 40 fois plus longue. Il faut un essai de quelques appels, à chiffrer, ou une estimation par les jetons.

## 3. Ce que cela implique pour ton texte et pour Lazar

- **Volume** : le plan complet demande environ **527 appels réussis par fournisseur** (Argon, dans A1).
- **Durée** : à 10 à 25 min par appel Kimi et un fil par fournisseur, **Kimi seul prendrait de 90 à 220 heures**. Cela heurte la durée maximale de 20 h. Il faut plusieurs fils par fournisseur, ou une sortie maximale de Kimi plus basse, ou moins de cartes.
- **Ordre de grandeur de dépense** pour le plan complet, à un facteur 2 près :
  - Kimi : 527 × 0,35 ≈ 185 USD ;
  - Claude et Astra : inconnus sur ce rôle. Une hypothèse grossière, sortie d'environ 5 000 jetons au barème supposé, donne environ 0,25 USD par appel, soit environ 130 USD chacun.
  - **Total : environ 450 USD pour trois fournisseurs**, contre 80 USD de plafond pour A1. C'est à Lazar de choisir un plafond, un nombre de cartes et une sortie maximale.
- **Quel « Claude »** : Fable 5.1, Opus 5.5 ou Opus 4.6 (celui qu'a servi le v8) ? C'est à demander à Lazar.
- **Code** : le lanceur refuse tout autre fournisseur, aux lignes `pole/attaque_goodhart_v2.py:58` (`FOURNISSEURS`) et `demonstrations/attaque_goodhart_v2.py:220-223`, `:226-229`, `:277-278`, `:280-283` (pire cas codé sur Kimi) et `:284` (part = plafond / nombre de fournisseurs). Il faut une version neuve chez toi, avec la configuration : proposeurs, fournisseurs et commandes de Claude et d'Astra.

Je peux faire écrire chez moi les deux commandes neuves (Claude 8806, Astra 8807), éprouvées hors réseau, si tu me donnes le format exact que ton lanceur neuf attendra. Dis-moi.

Prochain message : n° 275, sur `canal/session-depot-reprise-n102`.
