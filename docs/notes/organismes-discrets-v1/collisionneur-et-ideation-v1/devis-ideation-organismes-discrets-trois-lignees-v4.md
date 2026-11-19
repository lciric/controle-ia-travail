# Devis — organisme d'idéation sur les organismes discrets, trois courses jumelles (Carbon, Astra, Argon) — v4

**Statut : version 4, écrite le 2026-11-18 par la session de relance `session_01XJ6MgpChR1JWSMBxSQcf3c` après la contre-lecture R2 de la v3 (`contre-lecture-devis-trois-lignees-v3-v1.md`, lecteur neuf Opus 5.5 : « à corriger — 1 bloquant, 4 significatifs, 9 mineurs ») et la contre-lecture R2 du lanceur v8 (`contre-lecture-lanceur-v8-v1.md`) ; toutes deux intégrées ci-dessous (section 8). La v3 (`devis-ideation-organismes-discrets-trois-lignees-v3.md`) reste archivée sans modification (R12). Aucune dépense faite par lui.**
Remplace le devis v2 (`devis-collisionneur-ideation-organismes-discrets-v2.md`, `e8f8b581…`, archivé sans modification) pour la seule part « organisme d'idéation » ; la part « collisionneur » du v2 est consommée (7,86 USD, R-3072).

## 0. Mots de Lazar qui fixent ce devis (18 novembre 2026, session de relance)
- « relance l'organisme d'idéation sur les organismes discrets » ;
- « remplace un claude par gemini carbon et oublie pas astra de gpt » ;
- « go option A » : proposeurs Opus 5.5, Carbon, Astra, Argon ; juge interne Opus 5.5 ; juges externes différés Carbon, Astra, Argon ;
- « lance autonomie 24h » ; « go depenses go recos par anticipation ».

## 1. Pourquoi trois courses
L'orchestrateur épinglé (`lciric/ideation-organism`, commit `a41b7b50`, arbre `ee84d6ec…`) n'admet **qu'une lignée externe par course** au moteur réel (`verifier_commande_externe_reelle`, `demonstrations/ideation_v2.py`, v50-v51) et seuls des modèles Claude tiennent les rôles internes. La composition A tient donc en **trois courses jumelles** : mêmes pièces (question v3 `2f7acf36…`, faits v3 `5e2e9dd8…`, témoins v1 `1c6eef38…`), même graine de base, Opus 5.5 en proposeur et juge internes, une lignée externe par course (proposeur externe et juge externe différé).

## 2. Lanceur et plafonds (par course)
Lanceur : `scripts/lancer_course_ideation_organismes_discrets_v8.py` (dérivé du lanceur « Regard ou raisons » v1, `3b2dcb11…`). Plafonds de session transmis à l'orchestrateur :

| rôle | plafond (USD) |
|---|---|
| proposeur interne Opus 5.5 | 2,0 |
| juge interne Opus 5.5 | 2,0 |
| contrôle Claude (défaut de l'orchestrateur) | 0,2 |
| **total Claude transmis** | **6,0** (somme 4,2) |
| contrôle externe | 1,7 |
| proposeur externe (lignée) | 1,5 |
| juge externe différé (déclaré, jamais joué ici) | 2,5 |
| contrôle du bras (défaut) | 0,2 |
| **total externe transmis** | **6,5** (somme 5,9) |
| **plafond d'une course** (compté si la dépense est illisible) | **9,2** = 6,0 + 1,7 + 1,5 |

Une seule relance par lignée, seulement après une course finie proprement, sans fiche, à relevé lisible **d'au plus 2,1 USD** (`PLAFOND_RELANCE_USD` du lanceur v8 : arrêt au contrôle ; au-delà, la lignée n'est pas rejouée, nœud). Le 2,1 est hérité de la course modèle à deux contrôles Claude ; avec un seul contrôle ici le chiffre dérivé est 1,9 : la borne est prudente.

## 3. Attendu et pire cas

| poste | attendu (USD) | pire cas (USD) | source |
|---|---|---|---|
| Claude (Opus 5.5 : un proposeur, un juge, une passe), par course | 2,5 | 6,0 | course « Regard ou raisons » g1 : 5,08 USD avec deux proposeurs Claude, un juge et une seconde passe (devis v2 § 2) ; ici moitié moins de rôles, une passe |
| externe (contrôle + proposeur), par course | 1,0 | 3,2 | course v67 : Argon 0,86 USD proposeur (devis v2 § 2) ; Astra et Carbon tenus pour équivalents, prix d'enveloppe haut |
| **une course** | **3,5** | **9,2** | |
| **trois courses** | **10,5** | **27,6** | |
| relances (au plus une par lignée, défaut au contrôle) | 0 | 6,3 | 3 × 2,1 |
| **total de la ligne** | **≈ 10,5** | **≈ 34** | borne du lanceur : 34 USD |

**Prix unitaires.** Opus 5.5 : comptés par le relais Claude (`pole/relais_reel.py`) et par le kit d'agent ; la page publique de l'éditeur lue par un agent le 18 novembre donne 4 / 20 USD par million de jetons d'entrée / sortie (lecture non empreintée : information, non opposable). Gemini Argon et Carbon : les enveloppes comptent **8,3 / 41,5** (bornes hautes héritées de l'enveloppe v5 ; la borne d'entrée 8,3 avait été lue par Lazar sur sa console pour Argon, R-718 ; Carbon reprend la même borne par prudence) ; la page publique du fournisseur, lue par un agent le 18 novembre sans empreinte, affiche 2 / 10 jusqu'au 30 novembre 2026 : la dépense réelle de Gemini sera **inférieure** au coût compté. GPT-6 Astra : **10 / 50 USD, lus sur la page officielle le 14 novembre 2026** (palier standard, contexte ≤ 272 000 jetons d'entrée ; entrée en cache 1,00) : `docs/notes/organisme-conception-propre-v1/prix-astra-v2.md` (`bf211a07…`), page versée `docs/sources/tarifs-openai-v1/developers-openai-com-api-docs-pricing-2026-11-14.html` (`099c9496…`), R-2677 ; le compté égale le réel (l'entrée en cache comptée au prix plein est la seule borne haute) ; les gardes de taille gardent toute consigne sous 272 000 jetons. Dépense réelle à rapprocher des consoles par Lazar.

## 4. Relais (lancés avant, clés par nom, `scripts/lancer_relais_local_v1.py`)
| relais | script | port | bornes |
|---|---|---|---|
| Claude | `pole/relais_reel.py` du clone (`1b90b020…`) | 8787 | `--plafond-usd 22` (trois courses × 6 + trois contrôles de relance) ; modèles permis : `claude-opus-5-5` seul |
| Gemini v2 | `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py` (`2b0043bc…`) | 8788 | `--max-appels 24` ; modèles permis : `gemini-4-argon`, `gemini-4-carbon` |
| compatible OpenAI | `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py` (`67f36951…`) | 8790 | `--amont https://api.openai.com --variable-cle OPENAI_API_KEY --modeles-permis gpt-6-astra --plafond-usd 8 --prix-entree 10 --prix-sortie 50 --prix-cache 1 --max-appels 12` (`--prix-cache` obligatoire pour ce relais) |

Les relais tiennent leurs propres plafonds en plus de ceux de l'orchestrateur et des commandes ; le relais Gemini n'a pas de plafond en dollars (nombre d'appels seulement) : sa borne est celle des commandes (plafond de session) et de l'orchestrateur. Aucune clé ne transite par le lanceur, l'orchestrateur ni les commandes. **Aucun autre client n'appelle ces relais** pendant les courses (règle d'emploi) ; à chaque clôture, le journal de chaque relais est rapproché du relevé du lanceur et l'écart, s'il existe, est inscrit au registre des dépenses.

## 5. Plafond demandé et budget du jour
**34 USD** (pire cas de la ligne, borne du lanceur), échéance **2026-11-22**, hors de GO-2026-11-17-06 (reste ≈ 8,59 USD, périmètre « Argon seul, aucun Claude »). Attendu ≈ 10,5 USD.

**Budget du jour (R-3124)** : 100 euros de sortie d'argent pour la journée du 18 novembre (heure de Paris, recharge du loueur comprise), 100 euros neufs le lendemain ; **la session mère arbitre l'ordre des lignes** (règle de circulation des GO, R-3169 de la mère). D'après la contre-lecture de la v3, environ 23 euros étaient déjà sortis le 18 novembre à 04:00Z et la mère a prévu environ 77,5 USD pour d'autres lignes : le **pire cas de 34 USD ne tient pas dans la journée du 18 novembre à côté de ces lignes ; l'attendu de 10,5 USD non plus sans arbitrage**. Ce devis ne garde pas le budget du jour par du code (aucune garde n'existe pour cela) : il propose à la mère trois issues, par ordre de préférence de la session : (a) jouer **une lignée par jour** à partir du 18 ou du 19 novembre (plafond d'une course 9,2 USD, relance comprise 11,3), Carbon d'abord ; (b) jouer les trois lignées le 19 novembre sur le budget neuf ; (c) jouer les trois le 18 novembre si l'arbitrage des autres lignes le permet. Dans tous les cas la ligne de GO porte le plafond entier de 34 USD et l'échéance du 22 novembre ; l'ordre et les jours sont ceux que la mère fixe.

**Hors de cette ligne** : le bras du juge externe différé (trois juges, après attestation de lecture de Lazar) : de l'ordre de 2,5 + 0,2 USD par lignée, ≈ 8,1 USD au pire pour les trois ; il fera l'objet d'un devis et d'une ligne à part.

## 6. Préalables avant le premier appel
1. Contre-lectures R2 faites : devis v3 et lanceur v8 par deux lecteurs neufs Opus 5.5 (la session autrice est Fable 5.1 : autre modèle) ; corrections de la section 8 appliquées ; essais : lanceur v8 (231 cas), commandes v3e (98) et Astra (50), lanceur de relais (16), tous passés ; pièces scellées (compagnons R6).
2. Ligne de GO inscrite au registre sur `main` **par la session mère**, sur le mot exprès de Lazar portant sur ce devis (montant 34 USD, forme des trois courses), avec l'empreinte de ce devis v4.
3. Relais lancés et vérifiés par leur route d'état (`/relais/etat`) ; clés présentes par leur nom seulement (`RR_ANTHROPIC_API_KEY_RIGAUD`, `GEMINI_API_KEY`, `OPENAI_API_KEY`), exigées par le lanceur de relais (préfixe `!`).
4. Commandes exactes écrites avant le lancement : `commandes-exactes-trois-lignees-v2.md` (même dossier).
5. Dossier de run commité et poussé aussitôt après chaque lancement (C3) ; copies scellées de la sortie dans le dépôt à la clôture ; dépense inscrite au registre sous la ligne.

## 7. Risque accepté et dit d'avance : le modèle servi de Carbon
Le noyau n'admet comme modèle servi que l'identifiant exact ou un suffixe de date strict ; Carbon n'a jamais été appelé par le programme. Si Carbon rend un autre identifiant, le noyau refuse dès l'appel de contrôle externe, joué avant toute dépense Claude : la course s'arrête au coût de ce seul appel (au plus 1,7 USD, ≈ 0,1 attendu) et la relance de la lignée ne serait pas jouée (elle reproduirait le refus) : nœud. Carbon est joué en premier pour lever ce doute au plus tôt. Astra : égalité exacte des trois côtés déjà observée par le collisionneur v8 (`modele_servi` « gpt-6-astra »).

## 8. Corrections apportées par la v4 (contre-lectures de la v3 et du lanceur v8)
| constat | gravité | traitement |
|---|---|---|
| pire cas non confronté au budget du jour | bloquant | section 5 : budget du jour, trois issues, arbitrage de la mère |
| prix d'Astra dit « supposé » alors qu'il est lu et scellé (R-2677) | significatif | section 3 ; commande Astra, enveloppe et lanceur corrigés |
| relance non bornée (une lignée pouvait coûter 18,4 USD) | significatif | `PLAFOND_RELANCE_USD = 2,1` ajouté au lanceur v8, avec essais |
| appels par les relais hors du lanceur non comptés | significatif | section 4 : interdits ; journaux rapprochés à chaque clôture |
| même modèle que l'autrice | significatif | autrice Fable 5.1, lecteurs Opus 5.5 : autre modèle |
| `--prix-cache` obligatoire pour le relais compatible OpenAI | mineur | section 4 et commandes exactes v2 |
| 2,1 contre 1,9 ; R-718 attribué à Carbon ; prix lus sans empreinte ; devis sans compagnon ; relais Gemini sans plafond en dollars ; relais Claude à 20 | mineurs | sections 2, 3, 4 ; devis v4 scellé ; relais Claude à 22 |
| modèle servi de Carbon jamais observé | significatif (lanceur) | section 7 |
| nom listé absent n'empêchait pas le départ du relais | mineur (lanceur de relais) | préfixe `!` : nom exigé |
