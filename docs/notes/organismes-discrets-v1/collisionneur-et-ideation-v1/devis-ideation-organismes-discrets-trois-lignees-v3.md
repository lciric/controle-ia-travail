# Devis — organisme d'idéation sur les organismes discrets, trois courses jumelles (Carbon, Astra, Argon) — v3

**Statut : écrit le 2026-11-18 vers 04:05 UTC (`date -u`) par la session de relance `session_01XJ6MgpChR1JWSMBxSQcf3c` ; contre-lecture R2 demandée à un sous-agent neuf. Aucune dépense faite par lui.**
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

Une seule relance par lignée, seulement après une course finie proprement, sans fiche, à relevé lisible (au pire une tentative en défaut au contrôle ≈ 2,1 USD avant la relance).

## 3. Attendu et pire cas

| poste | attendu (USD) | pire cas (USD) | source |
|---|---|---|---|
| Claude (Opus 5.5 : un proposeur, un juge, une passe), par course | 2,5 | 6,0 | course « Regard ou raisons » g1 : 5,08 USD avec deux proposeurs Claude, un juge et une seconde passe (devis v2 § 2) ; ici moitié moins de rôles, une passe |
| externe (contrôle + proposeur), par course | 1,0 | 3,2 | course v67 : Argon 0,86 USD proposeur (devis v2 § 2) ; Astra et Carbon tenus pour équivalents, prix d'enveloppe haut |
| **une course** | **3,5** | **9,2** | |
| **trois courses** | **10,5** | **27,6** | |
| relances (au plus une par lignée, défaut au contrôle) | 0 | 6,3 | 3 × 2,1 |
| **total de la ligne** | **≈ 10,5** | **≈ 34** | borne du lanceur : 34 USD |

**Prix unitaires.** Opus 5.5 : 4 / 20 USD par million de jetons d'entrée / sortie (page publique des tarifs de l'éditeur, lue le 18 novembre 2026 ; comptés par le relais Claude). Gemini Argon et Carbon : la page publique des tarifs affiche 2 / 10 jusqu'au 30 novembre 2026 (lecture automatique du 18 novembre) ; les enveloppes comptent **8,3 / 41,5** (bornes hautes héritées de l'enveloppe v5, borne d'entrée lue par Lazar sur sa console, R-718) : la dépense réelle de Gemini sera **inférieure** au coût compté. GPT-6 Astra : **10 / 50, SUPPOSÉS** (page des tarifs refusée à la lecture automatique ; barème volontairement haut du collisionneur v8) : même sens, dépense réelle attendue inférieure au compté. Dépense réelle à rapprocher des consoles par Lazar.

## 4. Relais (lancés avant, clés par nom, `scripts/lancer_relais_local_v1.py`)
| relais | script | port | bornes |
|---|---|---|---|
| Claude | `pole/relais_reel.py` du clone (`1b90b020…`) | 8787 | `--plafond-usd 20` (trois courses × 6, marge) ; modèles permis : `claude-opus-5-5` seul |
| Gemini v2 | `docs/notes/ideation-organisme-v1/argon-recherche-v1/relais_gemini_v2.py` (`2b0043bc…`) | 8788 | `--max-appels 24` ; modèles permis : `gemini-4-argon`, `gemini-4-carbon` |
| compatible OpenAI | `docs/notes/ideation-organisme-v1/relais-kimi-v1/relais_kimi_v4.py` (`67f36951…`) | 8790 | `--amont https://api.openai.com --variable-cle OPENAI_API_KEY --modeles-permis gpt-6-astra --plafond-usd 8 --prix-entree 10 --prix-sortie 50 --max-appels 12` |

Les relais tiennent leurs propres plafonds en plus de ceux de l'orchestrateur et des commandes ; aucune clé ne transite par le lanceur, l'orchestrateur ni les commandes.

## 5. Plafond demandé
**34 USD** (pire cas de la ligne, borne du lanceur), échéance **2026-11-22** (celle de GO-2026-11-17-06), hors de GO-2026-11-17-06 (reste ≈ 8,59 USD, périmètre « Argon seul, aucun Claude »). Budget du jour de Lazar : 100 euros (R-3124) ; attendu ≈ 10,5 USD.

## 6. Préalables avant le premier appel
1. Contre-lecture R2 de ce devis, du lanceur v8 et de ses essais, des commandes v3e et Astra v1 et de leurs essais (sous-agents neufs, d'un autre modèle).
2. Ligne de GO inscrite au registre sur le mot de Lazar (« go depenses go recos par anticipation »), avec le plafond ci-dessus.
3. Relais lancés et vérifiés par leur route d'état (`/relais/etat`) ; clés présentes par leur nom seulement (`RR_ANTHROPIC_API_KEY_RIGAUD`, `GEMINI_API_KEY`, `OPENAI_API_KEY`).
4. Commandes exactes écrites avant le lancement (modèle : `docs/notes/regard-ou-raisons-confondants-v1/organisme-v1/commandes-exactes-v1.md`).
5. Dossier de run commité et poussé aussitôt après chaque lancement (C3) ; copies scellées de la sortie dans le dépôt à la clôture ; dépense inscrite au registre sous la ligne.
