# Devis du collisionneur : question neutre groupée sur les questions du directeur du 24 novembre (brouillon v1)

- **Nature** : brouillon d'une pièce de classe A (devis). **Non scellé, non vérifié** : la vérification par programme et la contre-lecture sont à faire par un agent neuf, après le test de devinette. Aucun appel, aucune dépense ; rien n'est lancé sans le mot de Lazar.
- **Heure** : `2026-11-24T17:14Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`. Écart au dosage du mandat du dossier, qui prévoyait Fable 5.2 en effort moyen pour le devis : ordre de la mère, économie du quota de Fable.
- **Gabarit** : `docs/notes/protocole-x-boucle-organisme-controle-v1/devis-collisionneur-boucle-organisme-controle-v2.md` (bras, options A et B, méthode), et `docs/notes/service-collisionneur-modes-v8-v1/devis-service-collisionneur-modes-v8-v3.md` (voie de l'abonnement, marge du kit d'Opus).
- **Calcul** : `verif_devis_questions_directeur_v1.py` (`7d16c136aa5e2101d486970c9425940a7b7f4b7d5e617f87955ada412298689b`), dérivé de `verif_devis.py` (`d3fbc0e4…`) ; sortie `verif-devis-questions-directeur-v1-sortie.txt` (`3e868a76cb3736c8a2cfa419cc80ead54ea9eabdc64c52a9c675104f08c9f075`). Tous les chiffres ci-dessous en viennent.

## 0. Résumé

- **Deux bras appariés, étage III seul** (conception, critique croisée, réponse), trois espèces : Opus 5.5, Carbon, Neon. Neuf cellules par bras, dix-huit en tout.
  - **Bras principal** : faits `faits-neutres-questions-directeur-v1.md` (3 333 octets, 3 235 caractères normalisés, 563 mots) et question `question-neutre-groupee-questions-directeur-v1.md` (9 253 octets, 8 922 caractères, 1 479 mots).
  - **Bras témoin** : mêmes faits ; question `question-temoin-neutre-questions-directeur-v1.md` (2 702 octets, 2 608 caractères, 430 mots).
- **Garde de motifs** : vide sur les trois pièces et sur les dix-huit invitations assemblées (`garde-motifs-questions-directeur-v1.md`).
- **Option A, Opus par l'abonnement** (Carbon et Neon par l'interface payante de Google) : attendu avec pannes **10,81 USD** pour les deux bras ; haut avec deux coupures de Carbon par bras 19,39 ; pire sans relance 23,87 ; pire avec toutes relances 71,61. **Plafond proposé : 16 USD par bras, 32 en tout.**
- **Option B, Opus par l'interface payante d'Anthropic** : attendu avec pannes **14,55 USD** ; haut 23,72 ; pire sans relance 32,33 ; pire avec relances 88,52. **Plafond proposé : 18 USD par bras, 36 en tout.**
- **Recommandation** : option A si la voie de l'abonnement d'Opus est disponible le jour du service ; sinon option B. Jamais un panachage des deux voies entre les bras.

## 1. Bras, espèces et voies

| Lettre | Espèce | Identifiant | Voie | Dépense |
|---|---|---|---|---|
| A | Opus 5.5 | `claude-opus-5-5` | **option A** : abonnement (kit, session fille éphémère, voie de l'abonnement v6 sur le moteur révision 8m, comme le service v8, § 2 et § 9) ; **option B** : interface d'Anthropic, moteur révision 8d, `--cle-anthropic` | A : **sans dépense** (marge du kit comptée au plafond, coût nul) ; B : payante |
| B | Carbon | `gemini-4-carbon` | interface de Google, flux continu | **payante** |
| C | Neon | `gemini-4-neon` | interface de Google, flux continu | **payante** |

- Fable 5.2 n'est pas proposé : quota de l'abonnement épuisé jusqu'au 29 novembre 2026, 18:00 UTC (service v8, v3, l. 3), et réservé aux pièces décisives. Argon, Astra : retirés, comme au devis v2 de la boucle (décorrélation par famille d'abord, coût).
- **À 0 USD, hors du plafond** : la note de fin de dossier (Markdown et PDF), le test de devinette, la vérification du devis.

## 2. Réglages et garde commune des modèles de Google

Vérifiés par `verifier_reglages_google` de la garde commune v3 (`src/controle_ia/garde_google_v3.py`, `923679b5…`), mode flux, sur le corps produit par le moteur : **aucun problème** aux trois tours, pour les deux espèces.

| Espèce | Réflexion (explicite) | Plafond de sortie, premier envoi / relance | Provision de réflexion | Texte au-delà de la réflexion | Limite de mots par tour → jetons (rapport mesuré) | Conforme |
|---|---|---|---|---|---|---|
| Carbon | niveau « high » (le plus haut admis), aucun budget envoyé | 65 536 / 65 536 | 49 152 | **16 384 ≥ 16 000** | 3 500 → 14 700 ; 3 000 → 12 600 (4,2 jetons par mot) | oui |
| Neon | niveau « xhigh » (le plus haut admis), aucun budget envoyé | 65 536 / 65 536 | 32 768 | **32 768 ≥ 16 000** | 3 500 → 17 850 ; 3 000 → 15 300 (5,1 jetons par mot) | oui |
| Opus 5.5 | effort « high » | 64 000 (option B) ; 128 000, marge du kit (option A) | — | — | — | — |

- **Carbon en flux seulement** : hors flux, sa limite est 32 768, sous les 65 152 exigés (49 152 + 16 000) ; aucun repli par lot pour Carbon. Neon : lot permis (65 536 ≥ 48 768), non demandé.
- **Après la réponse** (règle de `CLAUDE.md`) : zéro jeton de pensée, fin en `MAX_TOKENS`, `SAFETY`, `RECITATION` ou texte vide = défaut journalisé (codes 9 et 10 du moteur), jamais une réponse.
- **Relances** : Carbon et Neon, plafonds égaux, donc relance identique puis dernier recours déclaré à un niveau plus bas (écart déjà accordé, R-4664) ; Opus, une relance par l'interface, aucune par la voie de l'abonnement.

## 3. Tarifs, avec leur source datée (USD par million de jetons, entrée / sortie, réflexion comprise)

| Espèce | Compté au devis | Facturé | Source |
|---|---|---|---|
| Opus 5.5 | 4 / 20 (option B ; marge du kit en option A) | 4 / 20 | `docs/sources/prix/page-prix-anthropic-docs-20261122T104128Z.md` (`488e03e9…`), relevée le 22 novembre 2026 à 10:41Z, l. 23 |
| Carbon | **4 / 20** (barème haut, par prudence) | 2 / 10 jusqu'au 30 novembre 2026, 4 / 20 dès le 1er décembre | `docs/sources/prix/page-prix-gemini-api-20261122T104129Z.html` (`d3aa716e…`), relevée le 22 novembre 2026 à 10:41Z, palier « Standard », l. 153-163 |
| Neon | 3 / 15 | 3 / 15 | même page, l. 635-643 |

Taux de panne observés (espérance des pannes = taux × pire) : Carbon 7/56, Neon 1/26, Opus 2/52, repris de `docs/notes/service-collisionneur-modes-v8-v1/calculs-v3/calcul_devis_v8_v3.py`, l. 19. Relevé des sorties et des pièces : `docs/notes/service-collisionneur-modes-v8-v1/calculs/releve-journaux-v2.json` (`52cd710f…`).

## 4. Cellule par cellule (USD)

Entrée en jetons ; sortie médiane / 90e centile en jetons. En option A, les cellules d'Opus coûtent 0 ; leur marge de kit (dernière colonne) n'entre que dans la pointe.

### 4.1 Bras principal

| Cellule | Espèce | Entrée attendue | Sortie | Attendu | Haut | Pire sans relance | Pire avec relances | Marge du kit (A) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| III.1 conception A | Opus | 6 427 | 20 722 / 28 181 | 0,44 | 0,59 | 1,30 | 2,61 | 2,58 |
| III.1 conception B | Carbon | 4 106 | 33 819 / 37 234 | 0,69 | 0,76 | 2,32 | 6,95 | — |
| III.1 conception C | Neon | 4 172 | 34 709 / 41 581 | 0,53 | 0,64 | 1,49 | 4,48 | — |
| III.2 critique A | Opus | 36 856 | 20 871 / 25 616 | 0,56 | 0,70 | 1,45 | 2,89 | 2,73 |
| III.2 critique B | Carbon | 20 389 | 43 090 / 50 275 | 0,94 | 1,10 | 2,43 | 7,30 | — |
| III.2 critique C | Neon | 20 166 | 42 520 / 46 942 | 0,70 | 0,79 | 1,59 | 4,77 | — |
| III.3 réponse A | Opus | 52 597 | 25 526 / 32 150 | 0,72 | 0,90 | 1,49 | 2,99 | 2,77 |
| III.3 réponse B | Carbon | 30 807 | 34 491 / 40 024 | 0,81 | 0,96 | 2,50 | 7,51 | — |
| III.3 réponse C | Neon | 32 076 | 37 488 / 41 430 | 0,66 | 0,74 | 1,62 | 4,87 | — |

### 4.2 Bras témoin

| Cellule | Espèce | Entrée attendue | Attendu | Haut | Pire sans relance | Pire avec relances | Marge du kit (A) |
|---|---|---:|---:|---:|---:|---:|---:|
| III.1 conception A | Opus | 3 699 | 0,43 | 0,58 | 1,29 | 2,59 | 2,57 |
| III.1 conception B | Carbon | 2 363 | 0,69 | 0,75 | 2,31 | 6,92 | — |
| III.1 conception C | Neon | 2 401 | 0,53 | 0,63 | 1,49 | 4,46 | — |
| III.2 critique A | Opus | 34 036 | 0,55 | 0,69 | 1,44 | 2,87 | 2,72 |
| III.2 critique B | Carbon | 18 620 | 0,94 | 1,09 | 2,42 | 7,27 | — |
| III.2 critique C | Neon | 18 392 | 0,69 | 0,78 | 1,58 | 4,75 | — |
| III.3 réponse A | Opus | 49 560 | 0,71 | 0,88 | 1,48 | 2,97 | 2,76 |
| III.3 réponse B | Carbon | 28 912 | 0,81 | 0,95 | 2,49 | 7,48 | — |
| III.3 réponse C | Neon | 30 138 | 0,65 | 0,73 | 1,62 | 4,85 | — |

Sorties : mêmes médianes et centiles qu'au bras principal (relevé par espèce et par tour).

## 5. Totaux (USD)

| Grandeur | A, principal / témoin | **A, deux bras** | B, principal / témoin | **B, deux bras** |
|---|---:|---:|---:|---:|
| Attendu hors pannes | 4,34 / 4,30 | 8,64 | 6,07 / 5,99 | 12,06 |
| **Attendu avec espérance de pannes** | 5,43 / 5,38 | **10,81** | 7,32 / 7,24 | **14,55** |
| Haut avec deux coupures de Carbon (III.1, III.2) | 9,73 / 9,67 | 19,39 | 11,91 / 11,82 | 23,72 |
| Pointe : dépense comptée avant + marge exigée | 10,81 / 10,75 (III.3 réponse A, marge du kit) | — | 12,80 / 12,70 (III.3 réponse C) | — |
| Pire sans relance (formule de la garde) | 11,96 / 11,91 | **23,87** | 16,21 / 16,12 | **32,33** |
| Pire avec toutes relances | 35,88 / 35,72 | 71,61 | 44,37 / 44,15 | 88,52 |
| **Plafond et ligne proposés** | **16 / 16** | **32** | **18 / 18** | **36** |
| Pour information : attendu avec pannes, Carbon au barème facturé jusqu'au 30 novembre | — | 8,37 | — | 12,12 |

- **Règle du plafond** (devis v2 de la boucle ; service v8, v3, § 7.6) : pointe du chemin haut à deux coupures de Carbon, plus deux coupures de Carbon de plus (2,50 et 2,49 au pire), arrondie à l'entier supérieur : A, 10,81 + 5,01 = 15,81, donc 16 ; B, 12,80 + 5,01 = 17,81, donc 18. Le pire avec toutes relances est hors d'atteinte : la ligne et le plafond refusent tout envoi dont le pire les dépasserait.
- **Devis natif du moteur** (commande `devis`, borne large de 7 caractères par mot, étage III, tout par l'interface) : 15,89 (principal) et 15,81 (témoin), 31,70 en tout ; borne de comparaison, non le devis.
- **Commande** : `--ligne-usd 16 --plafond-usd 16` par bras (A) ou `--ligne-usd 18 --plafond-usd 18` (B) ; `--plafond-usd` n'est pas scellé et vaut 40 par défaut : **toute commande le redonne**.

## 6. Conditions

1. **Avant tout envoi** : test de devinette par un lecteur neuf, score sous 0,50 pour chaque pièce ; vérification de ce devis par programme et contre-lecture (agent neuf, classe A) ; mot de Lazar sur l'option et le plafond (dépense : nœud).
2. **Appariement strict** : mêmes espèces, voie, réglages, plafond pour les deux bras.
3. **Arrêts** : garde de motifs (code 7), réglages de Google (code 1), comptage (code 8), plafond ou ligne (code 4, faux échec « jamais parti », nœud), gardes de réponse (codes 6, 9, 10). Toute panne technique a droit à une relance sur le même accord et entre au registre des idées comme faux échec.
4. **Fin de dossier** : note en Markdown et en PDF sur les propositions des deux bras (accords, désaccords, neuf ou fragile, références à vérifier, propositions retenues), transmise avec le compte rendu.

## 7. Réserves

- **Voie de l'abonnement non vue ici** : le script de la voie v6 et le moteur révision 8m sous cette voie vivent sur une branche de reprise que ce sous-agent n'a pas ouverte (interdits de lecture) ; le chiffrage de l'option A suit le service v8, v3 (marge du kit 4 / 20 sur 128 000 jetons, coût nul) sans l'avoir rejoué sur ce moteur. Le calcul est fait sur la révision 8d, dont les tours, consignes, préambule et motifs sont les mêmes (service v8, v3, § 2).
- **Disponibilité du quota d'Opus** ce jour-là : non vérifiée.
- **Ordre des envois** supposé séquentiel (tour par tour, lettre par lettre) pour la pointe. Si les trois cellules d'un tour partaient ensemble, la pointe du bras principal au tour III.3 serait la dépense comptée avant ce tour plus les trois marges : option A, (9,73 − 0,96 − 0,74) + (2,77 + 2,50 + 1,62) = 8,03 + 6,90 = 14,93 ; option B, (11,91 − 0,90 − 0,96 − 0,74) + (1,49 + 2,50 + 1,62) = 9,32 + 5,62 = 14,94 ; sous les plafonds proposés, mais sans coupure de Carbon de plus tolérée en option A (14,93 + 2,32 > 16), une seule en option B (14,94 + 2,43 ≤ 18) ; en envoi parallèle, la même règle (deux coupures de plus) donnerait 20 par bras dans les deux options (14,93 + 5,01 et 14,94 + 5,01) (calcul de l'auteur sur les chiffres de la sortie, **à refaire par programme par l'agent neuf**).
- **Prix de Carbon** compté au barème haut ; la facture réelle avant le 1er décembre serait plus basse (ligne d'information du § 5, où l'espérance des pannes reste au barème haut).
