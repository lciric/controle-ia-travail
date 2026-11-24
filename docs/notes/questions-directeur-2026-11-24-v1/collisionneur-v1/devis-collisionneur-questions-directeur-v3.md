# Devis du collisionneur : question neutre groupée sur les questions du directeur du 24 novembre (v3)

- **Nature** : pièce de classe A (devis), **non scellée**. Aucun appel, aucune dépense ; rien n'est lancé sans le mot de Lazar (dépense : nœud).
- **Heure** : `2026-11-24T17:51:50Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, auteur des devis v1 et v2, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`. Écart au dosage du mandat (Fable 5.2 en effort moyen) sur l'ordre de la mère : économie du quota de Fable.
- **Remplace** le devis v2 (`devis-collisionneur-questions-directeur-v2.md`, gardé tel quel), qui portait la question groupée v2 et le témoin v1. Ce devis porte les textes admis au test de devinette v5 (`test-neutralite-devinette-questions-directeur-v5.md`, `106bddaeb4bf00b7d3b71372c38175d59252833c7820a1d2f6b6fd405a8de68e` : « aucune pièce ni partie n'atteint 0,50 »), sur la demande de la vérification v2 (`verification-devis-questions-directeur-v2.md`, `54995675584b920062ce94674eecbe4cd0dc8406f97fbf32acc407d9bd36f854`, réserve 6).
- **Calcul** : `verif_devis_questions_directeur_v5.py` (`6db299897a3bf37354cfa6441ffef099b0511b397a922c6f2aea1e230a2dbc0e`) ; sortie `verif-devis-questions-directeur-v5-sortie.txt` (`c9cc34a49435ca15eab41507cdb6185bbaf8c647259d2473d2411d83e752e959`), code 0, rejouée à l'identique par la vérification v2. **Tous les chiffres ci-dessous en sont tirés** (tableaux des § 4 et 5 produits par programme depuis cette sortie). Moteur `collisionneur_v9_v8d.py` (`b7803838…`), garde commune `garde_google_v3.py` (`923679b5…`), relevé `releve-journaux-v2.json` (`52cd710f…`).

## 0. Résumé

- **Deux bras appariés, étage III seul** (conception, critique croisée, réponse), trois espèces : Opus 5.5, Carbon, Neon ; neuf cellules par bras, dix-huit en tout.
  - **Bras principal** : faits `faits-neutres-questions-directeur-v1.md` (`7926025c…`, 3 333 octets, 3 235 caractères normalisés, 563 mots) et question `question-neutre-groupee-questions-directeur-v5.md` (`6b3f041923e802a9212c0aeb23a6bb89b7d855f1c280fb0faff08db1f3bb4110`, 9 486 octets, 9 150 caractères, 1 529 mots).
  - **Bras témoin** : mêmes faits ; question `question-temoin-neutre-questions-directeur-v2.md` (`4a5a0aef549169a05d8086ed9863a2e3314486b3d5a97afbccc7fd339af4616d`, 2 740 octets, 2 646 caractères, 438 mots).
- **Garde de motifs** : vide sur les trois pièces et les dix-huit invitations (`garde-motifs-questions-directeur-v5.md`).
- **Option A, Opus par l'abonnement** (sans dépense ; Carbon et Neon par l'interface payante de Google) : attendu avec pannes **10,81 USD** pour les deux bras ; pire sans relance **23,87**. **Plafond : 16 USD par bras (32 en tout) si l'envoi en séquence par la voie de l'abonnement est attesté avant le service ; sinon 20 par bras (40).**
- **Option B, Opus par l'interface payante d'Anthropic** : attendu avec pannes **14,56 USD** ; pire sans relance **32,33**. **Plafond : 18 USD par bras, 36 en tout** (le moteur révision 8d envoie une cellule à la fois, vérifié dans son code par la vérification v1, § 5).
- **Chaque commande redonne le plafond** : `--plafond-usd` n'est pas scellé et vaut 40 par défaut ; toute commande, première ou reprise, porte `--ligne-usd` et `--plafond-usd` au plafond retenu.
- **Recommandation** : option A si la voie de l'abonnement est disponible et son envoi en séquence attesté ; sinon option A à 20 par bras, ou option B à 18 par bras. Jamais un panachage des voies entre les bras.

## 1. Bras, espèces et voies

| Lettre | Espèce | Identifiant | Voie | Dépense |
|---|---|---|---|---|
| A | Opus 5.5 | `claude-opus-5-5` | **option A** : abonnement (kit, session fille éphémère ; voie de l'abonnement v6 sur le moteur révision 8m, comme le service v8, version 3, § 2 et § 9) ; **option B** : interface d'Anthropic, moteur révision 8d, `--cle-anthropic` | A : **sans dépense** (marge du kit comptée dans la pointe, coût nul) ; B : payante |
| B | Carbon | `gemini-4-carbon` | interface de Google, flux continu, jamais en lot | **payante** |
| C | Neon | `gemini-4-neon` | interface de Google, flux continu | **payante** |

Fable 5.2 n'est pas proposé (quota de l'abonnement épuisé jusqu'au 29 novembre 2026, 18:00 UTC ; réservé aux pièces décisives). À 0 USD, hors du plafond : la note de fin de dossier, les tests de devinette, les vérifications.

## 2. Réglages des modèles de Google (règles de `CLAUDE.md`)

Vérifiés par la garde commune v3 (`verifier_reglages_google`, mode flux) sur le corps produit par le moteur, aux trois tours : **aucun problème** ; la vérification v1 (§ 3) a refusé dix artefacts sur dix par deux règles indépendantes.

| Espèce | Réflexion (explicite) | Plafond de sortie, premier envoi / relance | Provision de réflexion | Texte au-delà de la réflexion | Limite de mots par tour → jetons | Conforme |
|---|---|---|---|---|---|---|
| Carbon | niveau « high », le plus haut admis ; aucun budget | 65 536 / 65 536 | 49 152 | **16 384 ≥ 16 000** | 3 500 → 14 700 ; 3 000 → 12 600 | oui |
| Neon | niveau « xhigh », le plus haut admis ; aucun budget | 65 536 / 65 536 | 32 768 | **32 768 ≥ 16 000** | 3 500 → 17 850 ; 3 000 → 15 300 | oui |
| Opus 5.5 | effort « high » | 64 000 (B) ; 128 000, marge du kit (A) | — | — | — | — |

Après la réponse : zéro jeton de pensée, fin en `MAX_TOKENS`, `SAFETY`, `RECITATION` ou texte vide = défaut journalisé (codes 9 et 10), jamais une réponse. Relances : Carbon et Neon, relance identique puis dernier recours déclaré à un niveau plus bas (écart accordé, R-4664) ; Opus, une relance par l'interface, aucune par la voie de l'abonnement.

## 3. Tarifs (USD par million de jetons, entrée / sortie, réflexion comprise), relevés le 24 novembre 2026

| Espèce | Compté au devis | Facturé | Source relevée |
|---|---|---|---|
| Carbon | **4 / 20** (barème haut, par prudence) | 2 / 10 jusqu'au 30 novembre 2026 ; 4 / 20 dès le 1er décembre | page de tarifs de Google (`https://ai.google.dev/gemini-api/docs/pricing`), relevée à **17:19:00Z** : `releve-sources-tarifs-20261124T1719Z-v1/page-prix-gemini-api-20261124T171900Z.md.txt` (`3d7b87d69e839c4b969a0d953ff29f4b8f4ce5e5771f37fb95beb01459c2cfcc`), section « Gemini 4 Carbon », onglet « Standard », l. 127-128 et 134-135 |
| Neon | 3 / 15 | 3 / 15 | même copie, section « Gemini 4 Neon », onglet « Standard », l. 609 et 615 |
| Opus 5.5 | 4 / 20 (B ; marge du kit en A) | 4 / 20 | page de tarifs d'Anthropic (`platform.claude.com/docs/en/about-claude/pricing.md`), relevée à **17:19:21Z** par la vérification v1 : empreinte identique à la copie versée `docs/sources/prix/page-prix-anthropic-docs-20261122T104128Z.md` (`488e03e9…`), l. 23 |

Sortie maximale synchrone de 65 536 jetons pour Carbon et Neon : pages des modèles relevées à 17:20:51Z, même sous-dossier (`c880e69c…`, `b841dd32…`). Taux de panne (espérance des pannes = taux × pire) : Carbon 7/56, Neon 1/26, Opus 2/52 (`docs/notes/service-collisionneur-modes-v8-v1/calculs-v3/calcul_devis_v8_v3.py`, l. 19).

## 4. Cellule par cellule (USD)

En option A, les cellules d'Opus coûtent 0 ; leur marge de kit n'entre que dans la pointe. Les sorties sont les médianes et 90e centiles du relevé, par espèce et par tour.

### 4.1 Bras principal (question v5)

| Cellule | Espèce | Entrée attendue (jetons) | Sortie médiane / 90e centile (jetons) | Attendu | Haut | Pire sans relance | Pire avec relances | Marge du kit (option A) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| III.1 conception A | Opus | 6 525 | 20 722 / 28 181 | 0,44 | 0,59 | 1,30 | 2,61 | 2,58 |
| III.1 conception B | Carbon | 4 169 | 33 819 / 37 234 | 0,69 | 0,76 | 2,32 | 6,95 | — |
| III.1 conception C | Neon | 4 236 | 34 709 / 41 581 | 0,53 | 0,64 | 1,49 | 4,48 | — |
| III.2 critique A | Opus | 36 957 | 20 871 / 25 616 | 0,57 | 0,70 | 1,45 | 2,90 | 2,73 |
| III.2 critique B | Carbon | 20 452 | 43 090 / 50 275 | 0,94 | 1,10 | 2,43 | 7,30 | — |
| III.2 critique C | Neon | 20 230 | 42 520 / 46 942 | 0,70 | 0,79 | 1,59 | 4,77 | — |
| III.3 réponse A | Opus | 52 707 | 25 526 / 32 150 | 0,72 | 0,90 | 1,49 | 2,99 | 2,77 |
| III.3 réponse B | Carbon | 30 875 | 34 491 / 40 024 | 0,81 | 0,96 | 2,50 | 7,51 | — |
| III.3 réponse C | Neon | 32 146 | 37 488 / 41 430 | 0,66 | 0,74 | 1,62 | 4,87 | — |

### 4.2 Bras témoin (question v2)

| Cellule | Espèce | Entrée attendue (jetons) | Sortie médiane / 90e centile (jetons) | Attendu | Haut | Pire sans relance | Pire avec relances | Marge du kit (option A) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| III.1 conception A | Opus | 3 715 | 20 722 / 28 181 | 0,43 | 0,58 | 1,29 | 2,59 | 2,57 |
| III.1 conception B | Carbon | 2 374 | 33 819 / 37 234 | 0,69 | 0,75 | 2,31 | 6,92 | — |
| III.1 conception C | Neon | 2 412 | 34 709 / 41 581 | 0,53 | 0,63 | 1,49 | 4,46 | — |
| III.2 critique A | Opus | 34 053 | 20 871 / 25 616 | 0,55 | 0,69 | 1,44 | 2,87 | 2,72 |
| III.2 critique B | Carbon | 18 630 | 43 090 / 50 275 | 0,94 | 1,09 | 2,42 | 7,27 | — |
| III.2 critique C | Neon | 18 402 | 42 520 / 46 942 | 0,69 | 0,78 | 1,58 | 4,75 | — |
| III.3 réponse A | Opus | 49 578 | 25 526 / 32 150 | 0,71 | 0,88 | 1,48 | 2,97 | 2,76 |
| III.3 réponse B | Carbon | 28 924 | 34 491 / 40 024 | 0,81 | 0,95 | 2,49 | 7,48 | — |
| III.3 réponse C | Neon | 30 149 | 37 488 / 41 430 | 0,65 | 0,73 | 1,62 | 4,85 | — |

## 5. Totaux (USD)

| Grandeur | A, principal / témoin | **A, deux bras** | B, principal / témoin | **B, deux bras** |
|---|---:|---:|---:|---:|
| Attendu hors pannes | 4,34 / 4,30 | 8,64 | 6,07 / 5,99 | 12,06 |
| **Attendu avec espérance de pannes** | 5,43 / 5,38 | **10,81** | 7,32 / 7,24 | **14,56** |
| Information : attendu avec pannes, Carbon au taux prudent 13/79 | 5,72 / 5,67 | 11,39 | 7,61 / 7,52 | 15,13 |
| Information : attendu avec pannes, Carbon au barème facturé jusqu'au 30 novembre | — | 8,37 | — | 12,12 |
| Haut avec deux coupures de Carbon (III.1, III.2) | 9,73 / 9,67 | 19,39 | 11,91 / 11,82 | 23,73 |
| Pointe en séquence | 10,81 / 10,75 (III.3 réponse A, marge du kit) | — | 12,80 / 12,70 (III.3 réponse C) | — |
| Pointe en parallèle, tour par tour | 14,94 / 14,86 (lot III.3) | — | 14,94 / 14,85 (lot III.3) | — |
| **Pire sans relance** (formule de la garde) | 11,96 / 11,91 | **23,87** | 16,21 / 16,12 | **32,33** |
| Pire avec toutes relances (hors d'atteinte sous le plafond) | 35,89 / 35,72 | 71,61 | 44,38 / 44,15 | 88,53 |
| Plafond en séquence | 16 / 16 | 32 | **18 / 18** | **36** |
| Plafond en parallèle | 20 / 20 | 40 | 20 / 20 | 40 |
| **Plafond et ligne proposés, par bras** | **16 si l'envoi en séquence est attesté, sinon 20** | **32 ou 40** | **18** | **36** |

- **Règle du plafond** : pointe du chemin haut à deux coupures de Carbon, plus deux coupures de Carbon de plus (2,50 et 2,49 au pire), arrondie à l'entier supérieur.
- **Modèle parallèle** : les trois cellules d'un tour partent ensemble ; la marge du lot est la somme des marges ; la relance d'une cellule coupée part seule, après le lot.
- **Devis natif du moteur** (commande `devis`, borne large, tout par l'interface) : 15,90 (principal) et 15,81 (témoin) ; borne de comparaison, non le devis.
- **Chaque commande redonne le plafond** : `--ligne-usd N --plafond-usd N` (N = 16, 18 ou 20 selon l'option), à chaque lancement et à chaque reprise ; une reprise au-delà demande un nouveau mot de Lazar.

## 6. Conditions

1. **Avant tout envoi** : vérification de ce devis v3 contre la sortie v5 (vérificateur de la v2, classe A) ; attestation de l'ordre d'envoi de la voie de l'abonnement si l'option A à 16 est choisie ; mot de Lazar sur l'option et le plafond.
2. **Appariement strict** : mêmes espèces, voie, réglages et plafond pour les deux bras.
3. **Arrêts** : garde de motifs (code 7), réglages de Google (code 1), comptage (code 8), plafond ou ligne (code 4 : faux échec « jamais parti », nœud), gardes de réponse (codes 6, 9, 10). Toute panne technique a droit à une relance sur le même accord et entre au registre des idées comme faux échec.
4. **Fin de dossier** : note en Markdown et en PDF sur les propositions des deux bras, transmise avec le compte rendu.

## 7. Réserves (celles de la vérification v2, § 4)

1. **Texte de Carbon non garanti** : sous un niveau de réflexion, la réflexion n'est pas bornée, et le plafond de sortie de Google la comprend. Les 16 384 jetons de texte reposent sur la provision de 49 152, qui est une hypothèse. Un arrêt en `MAX_TOKENS` sans texte est un défaut journalisé (code 9), suivi d'une relance. Marge mince : 1 684 jetons à 3 500 mots.
2. **Le pire compte deux fois la provision** (plafond plus provision, alors que la provision est dans le plafond) : prudence voulue par le moteur ; le pire réel d'un envoi de Carbon est d'environ 1,4 USD, non 2,4.
3. **Dernier recours de relance au niveau inférieur** : dérogation au niveau le plus haut admis, accordée (R-4664).
4. **Voie de l'abonnement non vue** (moteur révision 8m) : l'ordre de ses envois n'est pas attesté ; d'où le plafond conditionnel de l'option A. La disponibilité du quota d'Opus ce jour-là n'est pas vérifiée.
5. **Sorties tirées d'une autre question** : les sorties attendues viennent des journaux du service v8. La question v5, de 1 529 mots, est plus longue que celles de ce relevé ; la limite de mots borne le texte de chaque tour, non la réflexion.
6. **Prix de Carbon compté au barème haut** : la facture avant le 1er décembre serait plus basse (ligne d'information du § 5, où l'espérance des pannes reste au barème haut).
