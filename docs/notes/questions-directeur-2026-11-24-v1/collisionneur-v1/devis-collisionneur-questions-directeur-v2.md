# Devis du collisionneur : question neutre groupée sur les questions du directeur du 24 novembre (v2)

- **Nature** : pièce de classe A (devis), **non scellée**. Aucun appel, aucune dépense ; rien n'est lancé sans le mot de Lazar.
- **Heure** : `2026-11-24T17:29Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, auteur du brouillon v1, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`. Écart au dosage du mandat (Fable 5.2 en effort moyen), sur l'ordre de la mère : économie du quota de Fable.
- **Remplace** le brouillon v1 (`devis-collisionneur-questions-directeur-v1-brouillon.md`, gardé tel quel). Deux changements, et seulement ceux-là :
  1. le bras principal porte la question groupée **v2** (`question-neutre-groupee-questions-directeur-v2.md`, `11657f18…`), retouchée après le test de devinette ; faits et question témoin v1 inchangés ;
  2. les corrections de la vérification (`verification-devis-questions-directeur-v1.md`, `c09b631e09637eba9a5a633ab0e3ffc9ca1c962e0c6dea0acba3a002ffffdd60`) : plafond de l'option A à 16 par bras **seulement si l'envoi en séquence est attesté**, sinon 20 ; option B à 18 ; pointe parallèle calculée par programme ; réserves 1, 2 et 4 de la vérification reprises.
- **Calcul** : `verif_devis_questions_directeur_v2.py` (`a482e71730761ddddfa482b117f0188dddc336925be55f414253b0e19218044a`), copie de la v1 (`7d16c136…`) dont les changements sont listés dans sa docstring ; sortie `verif-devis-questions-directeur-v2-sortie.txt` (`e224b79209d64a544b3678675f143cfb590db6c8a8e1db4ccee91687240634fa`), code 0. Tous les chiffres ci-dessous en viennent.
- **Gabarits** : devis v2 de la boucle (`docs/notes/protocole-x-boucle-organisme-controle-v1/devis-collisionneur-boucle-organisme-controle-v2.md`) ; devis du service v8, version 3 (`docs/notes/service-collisionneur-modes-v8-v1/devis-service-collisionneur-modes-v8-v3.md`).

## 0. Résumé

- **Deux bras appariés, étage III seul** (conception, critique croisée, réponse), trois espèces : Opus 5.5, Carbon, Neon. Neuf cellules par bras, dix-huit en tout.
  - **Bras principal** : faits `faits-neutres-questions-directeur-v1.md` (3 333 octets, 3 235 caractères normalisés, 563 mots) et question `question-neutre-groupee-questions-directeur-v2.md` (9 314 octets, 8 980 caractères, 1 489 mots).
  - **Bras témoin** : mêmes faits ; question `question-temoin-neutre-questions-directeur-v1.md` (2 702 octets, 2 608 caractères, 430 mots).
- **Garde de motifs** : vide sur les trois pièces et les dix-huit invitations (`garde-motifs-questions-directeur-v2.md`).
- **Option A, Opus par l'abonnement** (Carbon et Neon par l'interface payante de Google) : attendu avec pannes **10,81 USD** pour les deux bras (11,38 au taux de panne de Carbon le plus prudent) ; haut à deux coupures de Carbon par bras 19,39 ; pire sans relance 23,87 ; pire avec toutes relances 71,61. **Plafond : 16 USD par bras (32 en tout) si l'envoi en séquence par la voie de l'abonnement est attesté avant le service ; sinon 20 par bras (40).**
- **Option B, Opus par l'interface payante d'Anthropic** : attendu avec pannes **14,55 USD** (15,13 au taux prudent) ; haut 23,72 ; pire sans relance 32,33 ; pire avec relances 88,53. **Plafond : 18 USD par bras, 36 en tout** (le moteur révision 8d envoie en séquence, vérification § 5).
- **Recommandation** : option A si la voie de l'abonnement est disponible et que son envoi en séquence est attesté ; sinon option A à 20 par bras ou option B à 18 par bras. Jamais un panachage des voies entre les bras.

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

Tarifs **relus à leur source le 24 novembre 2026** par la vérification (§ 2) : Google à 17:19:00Z, copie `releve-sources-tarifs-20261124T1719Z-v1/page-prix-gemini-api-20261124T171900Z.md.txt` (`3d7b87d6…`) ; Anthropic à 17:19:21Z, empreinte identique à la copie du 22 novembre. Concordent.

Taux de panne observés (espérance des pannes = taux × pire) : Carbon 7/56, Neon 1/26, Opus 2/52, repris de `docs/notes/service-collisionneur-modes-v8-v1/calculs-v3/calcul_devis_v8_v3.py`, l. 19. Relevé des sorties et des pièces : `docs/notes/service-collisionneur-modes-v8-v1/calculs/releve-journaux-v2.json` (`52cd710f…`).

## 4. Cellule par cellule (USD)

Entrée en jetons ; sortie médiane / 90e centile en jetons. En option A, les cellules d'Opus coûtent 0 ; leur marge de kit (dernière colonne) n'entre que dans la pointe.

### 4.1 Bras principal (question v2)

| Cellule | Espèce | Entrée attendue | Sortie | Attendu | Haut | Pire sans relance | Pire avec relances | Marge du kit (A) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| III.1 conception A | Opus | 6 452 | 20 722 / 28 181 | 0,44 | 0,59 | 1,30 | 2,61 | 2,58 |
| III.1 conception B | Carbon | 4 122 | 33 819 / 37 234 | 0,69 | 0,76 | 2,32 | 6,95 | — |
| III.1 conception C | Neon | 4 188 | 34 709 / 41 581 | 0,53 | 0,64 | 1,49 | 4,48 | — |
| III.2 critique A | Opus | 36 881 | 20 871 / 25 616 | 0,56 | 0,70 | 1,45 | 2,89 | 2,73 |
| III.2 critique B | Carbon | 20 405 | 43 090 / 50 275 | 0,94 | 1,10 | 2,43 | 7,30 | — |
| III.2 critique C | Neon | 20 182 | 42 520 / 46 942 | 0,70 | 0,79 | 1,59 | 4,77 | — |
| III.3 réponse A | Opus | 52 625 | 25 526 / 32 150 | 0,72 | 0,90 | 1,49 | 2,99 | 2,77 |
| III.3 réponse B | Carbon | 30 824 | 34 491 / 40 024 | 0,81 | 0,96 | 2,50 | 7,51 | — |
| III.3 réponse C | Neon | 32 094 | 37 488 / 41 430 | 0,66 | 0,74 | 1,62 | 4,87 | — |

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
| Attendu avec pannes, Carbon au taux prudent 13/79 (information) | 5,71 / 5,67 | 11,38 | 7,60 / 7,52 | 15,13 |
| Haut avec deux coupures de Carbon (III.1, III.2) | 9,73 / 9,67 | 19,39 | 11,91 / 11,82 | 23,72 |
| Pointe en séquence (lieu) | 10,81 / 10,75 (III.3 réponse A, marge du kit) | — | 12,80 / 12,70 (III.3 réponse C) | — |
| Pointe en parallèle, tour par tour (lieu) | 14,94 / 14,86 (lot III.3) | — | 14,94 / 14,85 (lot III.3) | — |
| Pire sans relance (formule de la garde) | 11,96 / 11,91 | **23,87** | 16,21 / 16,12 | **32,33** |
| Pire avec toutes relances | 35,89 / 35,72 | 71,61 | 44,38 / 44,15 | 88,53 |
| Plafond en séquence | 16 / 16 | 32 | **18 / 18** | **36** |
| Plafond en parallèle | 20 / 20 | 40 | 20 / 20 | 40 |
| **Plafond et ligne proposés** | **16 si séquence attestée, sinon 20** | **32 ou 40** | **18** | **36** |
| Information : attendu avec pannes, Carbon au barème facturé jusqu'au 30 novembre | — | 8,37 | — | 12,12 |

- **Règle du plafond** (devis v2 de la boucle ; service v8, v3, § 7.6) : pointe du chemin haut à deux coupures de Carbon, plus deux coupures de Carbon de plus (2,50 et 2,49 au pire), arrondie à l'entier supérieur. En séquence : A, 10,81 + 5,01 → 16 ; B, 12,80 + 5,01 → 18. En parallèle : 14,94 + 5,01 → 20 dans les deux options.
- **Modèle parallèle** (vérification, § 5) : les trois cellules d'un tour partent ensemble ; la marge du lot est la somme des marges (pire de chaque envoi, ou marge du kit pour Opus par l'abonnement) ; la relance d'une cellule coupée part seule, après le lot. Les pointes parallèles calculées par le script v2 sont celles de la vérification (14,93, 14,86, 14,94, 14,85 ; écart d'un millième au bras principal, venu de la question v2).
- **Séquence** : le moteur révision 8d envoie une cellule à la fois (`lancer_etage`, vérification § 5), d'où 18 en option B. Pour l'option A, la voie de l'abonnement (révision 8m) n'a été vue ni par l'auteur ni par le vérificateur : **attester son ordre d'envoi avant le service**, sinon 20.
- **Devis natif du moteur** (commande `devis`, borne large, étage III, tout par l'interface) : 15,89 (principal) et 15,81 (témoin) ; borne de comparaison, non le devis.
- **Commande** : `--ligne-usd` et `--plafond-usd` au plafond retenu, par bras ; `--plafond-usd` n'est pas scellé et vaut 40 par défaut : **toute commande le redonne**.

## 6. Conditions

1. **Avant tout envoi** : test de devinette de la question v2 par un **lecteur neuf** (score sous 0,50 pour chaque partie) ; vérification de ce devis v2 par le même vérificateur (classe A : contre-lecture, puis vérification des corrections) ; attestation de l'ordre d'envoi de la voie de l'abonnement si l'option A à 16 est choisie ; mot de Lazar sur l'option et le plafond (dépense : nœud).
2. **Appariement strict** : mêmes espèces, voie, réglages, plafond pour les deux bras.
3. **Arrêts** : garde de motifs (code 7), réglages de Google (code 1), comptage (code 8), plafond ou ligne (code 4, faux échec « jamais parti », nœud), gardes de réponse (codes 6, 9, 10). Toute panne technique a droit à une relance sur le même accord et entre au registre des idées comme faux échec.
4. **Fin de dossier** : note en Markdown et en PDF sur les propositions des deux bras, transmise avec le compte rendu.

## 7. Réserves

- **Réflexion non bornée** (vérification, réserve 1) : le plafond de sortie de Google comprend la réflexion, et aucun budget n'est envoyé sous un niveau de réflexion. Les 16 384 jetons de texte de Carbon reposent sur la provision de 49 152, qui est une hypothèse, non une borne. Si la réflexion la dépasse, la réponse finit en `MAX_TOKENS` : défaut journalisé (code 9), relance identique, puis dernier recours. La marge est de 1 684 jetons sur 3 500 mots.
- **Pire prudent** (réserve 2) : le pire compte plafond plus provision au prix de sortie, alors que la provision est dans le plafond. Le pire réel d'un envoi de Carbon est d'environ 1,4 USD, non 2,4 : prudence voulue par le moteur, gardée.
- **Taux de pannes** (réserve 4) : au taux de Carbon le plus prudent du relevé (13 non valides sur 79), l'attendu avec pannes monte de 0,57 USD (ligne d'information du § 5) ; les plafonds ne changent pas.
- **Dernier recours au niveau inférieur** (réserve 3) : écart déclaré et accordé (R-4664), non revérifié ici.
- **Sorties tirées d'une autre question** : les sorties attendues viennent des journaux du service v8.
- **Voie de l'abonnement non vue** : son chiffrage suit le service v8, v3 (marge du kit 4 / 20 sur 128 000 jetons, coût nul), sans rejeu sur la révision 8m. La disponibilité du quota d'Opus ce jour-là n'est pas vérifiée.
- **Prix de Carbon** compté au barème haut ; la facture avant le 1er décembre serait plus basse.
