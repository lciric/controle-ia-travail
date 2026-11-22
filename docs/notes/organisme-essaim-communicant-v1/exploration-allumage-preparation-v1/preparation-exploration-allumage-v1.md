# Préparation : avis de l'organisme sur la question « exploration au-delà du hasard, et naissance des idées nouvelles », avec et sans essaim — v1

Écrit le 2026-11-22T14:56:51Z par la session de l'organisme, pour la mère (message de 14:55Z). **Rien n'est lancé.**

## 0. La pièce, et un point bloquant
- **Source** : `docs/notes/exploration-idees-fable-v1/question-neutre-exploration-et-allumage-v2.md`, branche `claude/exploration-idees-fable-v1`, sha256 `3d4a1781…`, 3 188 octets.
- **Point bloquant** : le fichier mêle au corps de la question un en-tête de rédaction. La ligne 3 nomme la session fille et le test de devinette. Il n'a pas de section « à servir » marquée.
- **Il faut une version « servie »**, au corps seul, sans titre ni métadonnées, scellée, comme les autres questions servies (`…-servie-vN.md`). Je la forme par programme sur ton mot, ou tu me la donnes.

## 1. Voie sans essaim : une mini-passe aux neuf proposeurs
- **Forme** : une requête par proposeur, la question servie seule. Il n'y a ni groupes, ni préambule, ni consigne de longueur, sauf si tu en décides autrement. La garde de coupure se réduit alors à trois contrôles : fin normale, texte non vide, modèle servi.
- **Claude** (Opus 5.5, Fable 5.1, Opus 4.6, Sonnet 4.6) : par des sessions que tu crées, sur le kit de `passe-x-kit-abonnement-v1`, avec le même versement sans lecture. Coût API : 0. Le quota hebdomadaire de l'abonnement est en alerte.
- **API** : Argon, Carbon et Neon en flux, sous la garde Google v3 ; Kimi en flux ; Astra 6.2 par lots.
- **Code** : l'exécutant v4 est lié aux textes des groupes. Il faut une adaptation courte (lot 13), avec un texte unique et la garde réduite, puis sa vérification, soit environ 30 à 45 minutes.

| clé | requêtes | réservé au pire (6,05 par tentative, P4) | attendu réel |
|---|---|---|---|
| GEMINI_API_KEY | 3 (+ relance éventuelle) | 18,15 | environ 4 à 6, d'après la passe X (18,69 pour 3 modèles × 3 groupes, relances comprises) |
| KIMI_API_KEY | 1 | 6,05 | environ 0,1 |
| OPENAI_API_KEY_2, par lots | 1 | 1,93 au tarif des lots | environ 0,2 |
| Luc | 0 (Claude par l'abonnement) | 0 | 0 |
| **total API** | 5 | **26,13** | **environ 5** |

## 2. Voie avec essaim, Argon par étapes
- **Avis de Fable** : il est attendu de la session Fable qui tourne, sur le mandat `mandats-fable-abonnement-v1/mandat-fable-essaim-argon-par-etapes-v1.md` (`93bec410…`).
- **Devis préliminaire** pour le pilote P-std entier, 748 requêtes, sur GEMINI_API_KEY :
  - jusqu'au 30 novembre : 75 USD attendus, 150 au cas haut, 526 au pire ;
  - dès le 1er décembre : le double.
- **Recommandé, avant l'avis de Fable** :
  1. une fumée de six appels, environ 1 USD ;
  2. l'adaptateur Argon du lanceur et sa vérification ;
  3. un pilote au quart, environ 19 USD attendus en novembre, sous une borne d'arrêt de 60 USD.
- **Le service de la question à l'essaim** demande un préenregistrement court, au titre de R1, avant le pilote.

## 3. Ordre proposé
1. La version servie de la question.
2. La mini-passe sans essaim : le lot 13 vérifié, puis les sessions Claude que tu crées.
3. L'avis de Fable sur l'essaim, puis son devis calculé et contre-lu.
4. La fumée Argon, puis le pilote au quart.
