# Devis — atelier d'idées sur les bassins étroits et profonds, trois générations — v3

Écrit par le préparateur (Claude Opus 5.5) le 13 novembre 2026 (reprise à 15:35 UTC, `date -u`). **Remplace la v2**
(`23077e8b…`, gardée, R12) après la génération 1 du lanceur v2, close en défaut au contrôle (`operation-g1-v1.md`,
`3beef39e…`). **Aucune dépense engagée par ce devis.** Ligne **GO-2026-11-13-03** (60 USD ; par course 12 Claude + 8 hors
Claude ; échéance 2026-11-30). Lanceur `scripts/lancer_course_ideation_bassins_etroits_v3.py`.

## 1. Ce qui est déjà dépensé (cumul de départ)

| Run | Fournisseur | USD | Source |
|---|---|---|---|
| `20261113-152926-course-ideation-bassins-etroits-v2-g1` (lanceur v2, génération 1, 1ʳᵉ course) | Argon (contrôle externe) | **0,275477** | `sortie-controle/tentative-1.json` scellée, lue par le v3 (`cout_externe_usd`) |
| idem | Claude | 0,00 | tentative : `cout_claude_usd` 0,0 ; relais : 0 appel relayé |
| **Cumul de départ** | | **0,275477** | lu par la garde de cumul du v3 (essai `test_run_reel_du_v2_reconnu`) |

## 2. Plafonds et attendus par génération (inchangés depuis la v2)

| | Plafond (pire cas) | Attendu |
|---|---|---|
| Part Claude (contrôles 0,4 ; proposeurs 2 × 2,0 × 2 passes ; juge Opus 1,5) | 9,9 (total transmis 12,0) | ≈ 2,1 (calcul) |
| Part hors Claude (contrôle externe 1,7 ; passes d'Argon 1,3 + 1,9 ; juge Argon 2,5 ; contrôle court du bras 0,6) | 8,0 | ≈ 3,4 (calcul) |
| **Génération** | **17,9** (borne du GO 20) | **≈ 7 retenu (5 à 9)** |

Le contrôle d'Argon (consigne de contrôle entière, ≈ 33 200 jetons) se repaie à chaque course : ≈ 0,28 USD (mesuré le
13 novembre).

## 3. Le reste de la ligne

| | Attendu | Pire cas par les plafonds | Borne de la garde de cumul |
|---|---|---|---|
| Génération 1, seconde course (la dernière permise) | ≈ 7 | 17,9 | 0,28 + 20 ≤ 60 |
| Génération 2 | ≈ 7 | 17,9 | relevé + 20 ≤ 60 |
| Génération 3 | ≈ 7 | 17,9 | relevé + 20 ≤ 60 |
| **Total de la ligne, cumul de départ compris** | **≈ 21,3 (16,3 à 27,3)** | **54,0** (0,28 + 3 × 17,9) | **60** |

**Garde de cumul** (inchangée) : dépense relevée de toutes les courses et de tous les bras, v2 compris, plus 20 (course) ou
3,1 (bras) ≤ 60 ; dépense illisible = plafond entier. **Relance** (neuve) : une génération se relance **une fois** si la
course précédente a fini proprement, sans aucune fiche, avec une dépense relevée lisible (comptée) ; jamais après des
fiches ; deux courses par génération au plus. Pire cas si chaque génération use ses deux courses en défaut au contrôle :
≈ 6 × 0,28 ≈ 1,7 USD de plus, sous la borne.

## 4. Durée

Inchangée : course 1 à 2 heures (détachée sous un superviseur ; la même commande, relancée, dit « en marche », clôt, ou
signale un orchestrateur orphelin, code 4) ; bras 5 à 30 minutes ; trois générations ≈ 4 à 6 heures de calcul, un à deux jours
écoulés avec les lectures.

## 5. Réserves

- **Cause du défaut** : établie sans dépense par l'épreuve contre un faux amont local (rapport v3) ; le v3 transmet un
  environnement par liste de noms permis et un HOME neuf. La preuve porte sur l'en-tête que le kit envoie ; l'épreuve réelle
  reste la course elle-même (le premier contrôle Claude coûte au plus 0,2 USD par modèle).
- Fable 5.1 sans précédent mesuré en proposeur ; sonde de la garde refus-question recommandée (≈ 0,003 USD, à part).
- Bras impossible au-delà de ≈ 14 400 caractères par fiche en moyenne (garde du juge), refusé avant tout appel du bras.
- Témoins écrits par le modèle d'un proposeur et d'un juge (Opus 5.5).

## 6. Préalables

Bac à sable actif (R-2536) ; recoupement et son attestation de relecture (présents, `eecd98fa…`, `e6076698…`, selon
l'opérateur) ; relais Claude (`--modeles-permis claude-opus-5-5,claude-fable-5-1`, plafond 12) et Gemini v2 ; règle de
permission et épingle du **v3** (génération 1 seulement) ; vérification courte du v3.
