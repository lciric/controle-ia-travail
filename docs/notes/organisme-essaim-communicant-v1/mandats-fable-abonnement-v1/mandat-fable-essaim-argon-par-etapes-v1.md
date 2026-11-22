# Mandat à Fable (session de l'abonnement) — l'essai en essaim de l'organisme, avec Argon, par étapes — v1

Écrit le 2026-11-22T14:33:44Z par la session de l'organisme, sur la demande de Lazar relayée par la mère. Fable rend un avis écrit. **Il n'envoie aucun appel payant.**

## Question
Lazar veut faire l'essai en essaim de l'organisme avec **Argon** (gemini-4-argon) comme modèle, et non avec Kimi. Comment le conduire par étapes ? Il faut dire quel pilote, de quelle taille, avec quels réglages, sous quelles bornes d'arrêt et avec quelles mesures, avant le pilote entier.

## Ce qui existe (à lire, par chemin exact, sur la branche `lot/compte-organisme-v1` du dépôt de travail)
1. `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v5/rapport-devis-instruments-essaim-v5.md` : le pilote P-std, 748 requêtes, son lanceur v3 et ses gardes. Il est écrit pour Kimi (`max_tokens` 24 001).
2. `docs/notes/organisme-essaim-communicant-v1/devis-et-instruments-v5/a-faire-avant-preenregistrement-pilote-v2.md` : la liste des points à faire avant le préenregistrement.
3. Sur `main` : `src/controle_ia/garde_google_v3.py`. Elle impose la réflexion au plus haut admis et 16 000 jetons de texte au moins, avec une sortie de 65 536 au plus en flux.
4. Sur `main` : `docs/notes/demandes-fable-api-2026-11-22-v1/reponse-10/relecture-fable-api.md` (`f41a63d5…`). C'est ta réponse sur le critère de la comparaison entre l'essaim et l'isolé (pièces 1 et 2, décision 2 sur les cellules d'Argon jouées sans réflexion). Elle **ne tranche pas** le pilote Argon par étapes.

## Devis préliminaire de l'organisme (calcul à la main, non vérifié)
Hypothèses par requête : entrée de 10 000 jetons en attendu, 20 000 en haut ; sortie, réflexion comprise, de 8 000 en attendu, 16 000 en haut et 65 536 au pire.

| tarif d'Argon | attendu | haut | pire |
|---|---|---|---|
| jusqu'au 30 novembre (2 / 10 USD le million) | 75 | 150 | 526 |
| dès le 1er décembre (4 / 20) | 150 | 299 | 1 052 |

## Options
- (a) Pilote entier tout de suite, sous une borne d'arrêt par course.
- (b) **Recommandée par l'organisme** (confiance 0,6), en trois temps :
  1. une fumée Argon de six appels ;
  2. un adaptateur Argon pour le lanceur, en flux sous la garde v3, et sa vérification ;
  3. un pilote réduit au quart, environ 187 requêtes et environ 19 USD attendus en novembre, sous une borne de 60 USD ; puis le pilote entier si le quart est sain.
- (c) Un pilote à réflexion réduite (repli au budget, prévu par la garde v3), moins cher mais moins comparable.

## Ce que Fable rend
1. Son choix entre (a), (b) et (c), ou une autre forme, avec ses raisons et sa confiance.
2. La taille de chaque étape, les bornes d'arrêt et les critères de passage d'une étape à l'autre, chiffrés.
3. Les réglages d'Argon : niveau de réflexion, sortie, budget de repli éventuel, mode « flux ».
4. Les mesures et les gardes à ajouter au lanceur pour Argon : coupure, défaut Google, coût au pire.
5. Ce qui doit être préenregistré avant le pilote : hypothèse, seuil, plan d'analyse.
6. Ce qu'il ne sait pas et qui demande une mesure.

## Règles
- Langue : français.
- Pas d'appel payant, aucune clé.
- Lire seulement les pièces citées.
- Marquer [FAIT RAPPORTÉ], [HYPOTHÈSE] ou [PROPOSITION].
