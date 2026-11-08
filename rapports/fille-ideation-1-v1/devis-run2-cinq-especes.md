# Devis final — second run, collisionneur v9, 5 espèces, étage III, question v2

Date : 8 novembre 2026 (mise à jour 15:00Z).
GO : **en attente du mot de Lazar** (ligne de GO à inscrire).
Session : `session_016QhUrujoj3FTuFNoYshNYB`.
Plafond cible : **≤ 30 USD** (directive de Lazar, R-1825).

## 1. Collisionneur

- **Version** : `collisionneur-v2.12-cinq-especes-opus55` (branche `outils/collisionneur-v9-v1`).
- **Empreinte du script** : `27e9ce40a64fbcd5cd981f9cc1731b1119829a506f8427857cc850cde91bd1d6`.
- **Espèces** : A = Fable 5.1, B = Opus 5.5, C = Argon, D = Kimi K3.1 Pro, E = GPT-6 Astra.
- **Étage** : III seul (3 tours, 5 cellules par tour, 15 cellules au total).
- **Question** : question v2 scellée telle quelle (`2dbad4b75d20fadc3147be9eff07f2e77c2f82fe4f609ab1c29388ab46c4bb42`). Une seule question pour les 5 espèces (le v9 sert un fichier unique `question-etage3.md`). La variante étroite R-609 n'est **pas déployée** (décision de la mère : reformuler un refus est un contournement). Un refus au run est définitif et rapporté comme donnée.
- **Import T1 depuis v2.6** : **impossible** (préambule v2.6 « trois espèces » ≠ préambule v9 « cinq espèces » ; prompts non identiques au byte près). Les 15 cellules partent de zéro.

## 2. Entrées scellées

| Entrée | Empreinte |
|---|---|
| Question v2 (`question-pilier-attaque-v2.md`) | `2dbad4b75d20fadc3147be9eff07f2e77c2f82fe4f609ab1c29388ab46c4bb42` |
| Faits v2 (`faits-pilier-attaque-v2.md`) | `5cb21f08…` |

## 3. Barème des modèles

| Espèce | Identifiant d'API | Fournisseur | Prix (entrée / sortie, USD/1M jetons) | Sortie max (jetons) | Statut du prix |
|---|---|---|---|---|---|
| A | `claude-fable-5-1` | Anthropic | 10,0 / 50,0 | 64 000 | barème haut |
| B | `claude-opus-5-5` | Anthropic | 4,0 / 20,0 | 64 000 | lu dans la documentation |
| C | `gemini-4-argon` | Google (Gemini) | 10,0 / 50,0 | 32 000 | barème haut |
| D | `kimi-k3.1-pro` | Moonshot (Kimi) | 2,0 / 10,0 | 32 000 | vérifié le 30 octobre |
| E | `gpt-6-astra` | OpenAI | 10,0 / 50,0 | 32 000 | barème haut (prix confirmé 10/50 par recherche web ; barème haut conservé car sortie max plafonnée à 32 000) |

Les prix marqués « barème haut » sont volontairement surestimés : le plafond se déclenche plus tôt.

## 4. Coût par cellule (pire cas, sans relance)

Formule : `coût = caractères_entrée / 3 / 1 000 000 × prix_entrée + jetons_sortie_max / 1 000 000 × prix_sortie`.

| Cellule | Modèle | Entrée (car.) | Sortie max (jet.) | Pire cas USD |
|---|---|---:|---:|---:|
| E3-T1-conception-A | claude-fable-5-1 | 44 466 | 64 000 | 3,35 |
| E3-T1-conception-B | claude-opus-5-5 | 44 466 | 64 000 | 1,34 |
| E3-T1-conception-C | gemini-4-argon | 44 466 | 32 000 | 1,75 |
| E3-T1-conception-D | kimi-k3.1-pro | 44 466 | 32 000 | 0,35 |
| E3-T1-conception-E | gpt-6-astra | 44 466 | 32 000 | 1,75 |
| **Sous-total E3-T1** | | | | **8,53** |
| E3-T2-critique-croisee-A | claude-fable-5-1 | 128 466 | 64 000 | 3,63 |
| E3-T2-critique-croisee-B | claude-opus-5-5 | 128 466 | 64 000 | 1,45 |
| E3-T2-critique-croisee-C | gemini-4-argon | 128 466 | 32 000 | 2,03 |
| E3-T2-critique-croisee-D | kimi-k3.1-pro | 128 466 | 32 000 | 0,41 |
| E3-T2-critique-croisee-E | gpt-6-astra | 128 466 | 32 000 | 2,03 |
| **Sous-total E3-T2** | | | | **9,54** |
| E3-T3-reponse-A | claude-fable-5-1 | 166 966 | 64 000 | 3,76 |
| E3-T3-reponse-B | claude-opus-5-5 | 166 966 | 64 000 | 1,50 |
| E3-T3-reponse-C | gemini-4-argon | 166 966 | 32 000 | 2,16 |
| E3-T3-reponse-D | kimi-k3.1-pro | 166 966 | 32 000 | 0,43 |
| E3-T3-reponse-E | gpt-6-astra | 166 966 | 32 000 | 2,16 |
| **Sous-total E3-T3** | | | | **10,00** |
| **Total étage III** | **15 cellules** | | | **28,08** |

### Coût par espèce (pire cas, sans relance)

| Espèce | Modèle | Total USD |
|---|---|---:|
| A | claude-fable-5-1 | 10,73 |
| B | claude-opus-5-5 | 4,29 |
| C | gemini-4-argon | 5,93 |
| D | kimi-k3.1-pro | 1,19 |
| E | gpt-6-astra | 5,93 |
| **Total** | | **28,08** |

### Marge de relance

Une relance (sortie vide ou coupée) peut ajouter jusqu'au double du pire cas de sa cellule. Si toutes les cellules nécessitent une relance (cas extrême), le pire cas absolu est **52,59 USD**.

## 5. Sonde garde v2

Avant le lancement du collisionneur, sonde garde refus-question v2 (`sonde_garde_refus_v2.py`, scratchpad de la session) sur les 5 espèces, avec la **question v2 scellée** (`2dbad4b7…`). Si une espèce refuse à la sonde, elle est retirée du run, pas reformulée. Coût estimé : **~0,02 USD** (négligeable ; 5 appels de 1 024 jetons max chacun).

## 6. Récapitulatif

| Poste | USD |
|---|---|
| Sonde garde v2, 5 espèces | 0,01 |
| Étage III, pire cas sans relance | 28,08 |
| **Total (sans relance)** | **28,09** |
| Coût attendu (ratio 0,40 du pire) | ~11,24 |
| **Plafond du script** | **30,00** |

## 7. Clés nécessaires

| Variable d'environnement | Fournisseur | Statut |
|---|---|---|
| `RR_ANTHROPIC_API_KEY_LUC` | Anthropic (A, B) | **présente** |
| `GEMINI_API_KEY` | Google Gemini (C) | **présente** |
| `KIMI_API_KEY` | Moonshot Kimi (D) | **présente** |
| `OPENAI_API_KEY` | OpenAI (E) | **présente** |
| `GEMINI_API_KEY_2` | réservée étiqueteur | présente, **interdite d'usage** |
| `RR_TYPESAFE_API_KEY` | TypeSafe (Jev, optionnel) | présente |

## 8. Infrastructure nécessaire

| Composant | Statut | Détail |
|---|---|---|
| API Anthropic | **opérationnel** | confirmé par le run v2.6 en cours |
| API Gemini (`generativelanguage.googleapis.com`) | **opérationnel** | confirmé par l'appel Argon point 5 |
| API OpenAI (`api.openai.com`) | **opérationnel** | `gpt-6-astra` accepte les requêtes (vérifié 14:48Z) ; crédit suffisant |
| Relais Kimi local (`127.0.0.1:8789`) | **opérationnel** | PID 6398, amont `api.moonshot.ai`, plafond 30 USD, démarré 15:00Z |
| Identifiant d'API d'Astra | **confirmé** | `gpt-6-astra` présent dans `GET /v1/models` (vérifié 14:35Z) |
| Prix d'Astra | **confirmé (barème haut)** | 10,0 / 50,0 USD/1M jetons (vérifié par recherche web, cohérent avec le barème haut) |
| Crédit OpenAI | **opérationnel** | `gpt-6-astra` accepte les requêtes (vérifié 14:48Z) ; crédit suffisant (pas d'erreur `insufficient_quota`) |
| Crédit Kimi | **opérationnel** | HTTP 200 sur `api.moonshot.ai` (vérifié 14:45Z ; `api.moonshot.cn` est la plateforme chinoise, clés non interchangeables) |

## 9. Ce qui manque

1. ~~**Relais Kimi**~~ : **fait** (15:00Z), PID 6398, opérationnel.
2. ~~**Vérification de l'identifiant d'API d'Astra**~~ : **fait** (14:35Z), `gpt-6-astra` confirmé dans `GET /v1/models`.
3. ~~**Vérification du prix d'Astra**~~ : **fait** (14:50Z), barème 10/50 confirmé par recherche web (barème haut conservé).
4. ~~**Vérification du crédit OpenAI**~~ : **fait** (14:48Z), `gpt-6-astra` accepte les requêtes.
5. ~~**Vérification du crédit Kimi**~~ : **fait** (14:45Z), HTTP 200 sur `api.moonshot.ai`. Clé valide.
6. ~~**Sonde garde v2**~~ : **fait** (15:00Z). 5/5 OK, aucun refus. Résultats dans `sonde-garde-refus-v2-resultats.json`. Note : la sonde (méta-question, 1 024 jetons) ne préjuge pas du comportement au collisionneur (prompt complet, 64 000 jetons). Opus 5.5 a accepté la sonde mais avait refusé T1 au v2.6.
7. **GO de Lazar** : en attente (la mère porte le devis et le nœud du refus à Lazar).

## 10. Compatibilité avec le plafond de 30 USD

Le pire cas sans relance (28,08 USD) est **sous le plafond de 30 USD**. Marge : 1,92 USD, soit 6,8 %. Cette marge couvre au plus une relance de Kimi (0,43 USD) ou une relance partielle d'une cellule bon marché. Une relance d'une cellule Fable (jusqu'à 3,76 USD) dépasse le plafond : le script doit être paramétré à `--plafond-usd 30` pour stopper avant débordement.

**Risque** : si une cellule de T1 échoue et doit être relancée (essai 2), la marge est consommée. Si deux cellules échouent, le plafond est atteint avant la fin de T3. Le v9 lance d'abord le tour le moins cher (T1, 8,53 USD), ce qui permet de détecter les problèmes tôt.

**Le cas attendu** est nettement sous le plafond. Les cellules réelles du run v2.6 étaient 30 à 60 % sous le pire cas (exemple : T2-A pire 3,63 USD, réel 1,19 USD ; T2-B pire 1,45 USD, réel 0,55 USD). Coût attendu (ratio moyen 0,40 du pire cas) : **~11 USD**.

## 11. Recommandations

- **Plafond du script** : `--plafond-usd 30` (au lieu du défaut 40 dans le v9).
- **Refus** : un refus d'un classifieur est définitif dans le run et rapporté comme donnée (décision de la mère). L'espèce refusante à la sonde est retirée du run, pas reformulée.
- **Avant lancement** :
  1. ~~Sonde garde v2 sur les 5 espèces avec la question v2 scellée.~~ Fait (5/5 OK).
  2. ~~Vérification de l'identifiant d'API d'Astra.~~ Fait.
  3. ~~Vérification du crédit OpenAI et Kimi.~~ Fait.
  4. ~~Démarrage du relais Kimi local.~~ Fait.
  5. ~~Mot de la mère sur le devis et la question.~~ Reçu (question v2 scellée, pas de variante étroite).
  6. **GO de Lazar** : en attente.
