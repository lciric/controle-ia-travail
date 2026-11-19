# Vérification de la différence entre la commande v3 et la commande v4 de la tranche de l'ajustement de nos lentilles

**Verdict : à corriger, légèrement.** V-M1 est levé pour le trafic et la course figée, mais la correction introduit un défaut neuf (N-1, majeur
léger) : l'étape 8 exige « identifiant de machine égal à celui de l'offre », et le suivi ne le restitue pas. Les quatre mineurs et la remarque sur
l'outil du loueur sont levés. L'essai neuf discrimine.

- Lecteur : sous-agent neuf (R2), modèle Sonnet 5.5 (`claude-sonnet-5-5`) ; 2026-11-18, branche `claude/lentilles-b-beta-course-v1`, sommet `3c4bf45d`.
- Lu : `diff` v3/v4 ; vérification courte de la v3 ; devis v12 §§ 4-5 ; `releve_prix_h100_v3.py` (colonnes) ; `suivi_vast_v6.py` ; `tests/test_neuron_lens_etapes_b_beta_v4.py`.
- Exécuté : `pytest tests/test_neuron_lens_etapes_b_beta_v4.py` → 2 passés. Mutations sur copies sous le scratchpad (`…/scratchpad/mutv4`), rien dans le dépôt. Aucune machine, aucune clé, aucun appel au loueur.

## Point neuf
**N-1 (à corriger) — étape 8 de la v4 : « identifiant de machine égal à celui de l'offre retenue ».** `suivi_vast_v6.CHAMPS` = `id, label, actual_status,
cur_state, intended_status, dph_total, gpu_name, start_date, status_msg` : `machine_id` n'y est pas, et `filtrer` écarte tout le reste. Le contrôle
ne peut donc pas s'exécuter tel qu'écrit (même défaut que V-M1, déplacé). Le relevé, lui, écrit bien `machine_id` (colonne 3) et `id` (colonne 2, identifiant
de l'offre, qui n'est pas celui de l'instance). *Correction* : remplacer par des contrôles que le suivi rend (`dph_total` dans [1,85 ; 2,62], `gpu_name`
H100 SXM, et `dph_total` à moins de 0,05 USD du prix de l'offre au relevé, `actual_status`/`label` = `neuron-lens-b-beta`), en disant que l'identité de la
machine n'est pas relue (le trafic fait foi par le relevé dans l'heure) ; ou bien un suivi v7 (nouveau nom, scellé, essayé) qui ajoute `machine_id`.

## Points de la vérification de la v3
| point | statut | constat |
|---|---|---|
| V-M1 trafic (étapes 4, 8) | **levé, sauf N-1** | trafic lu sur l'offre du relevé, déclaré ; l'étape 8 ne relit plus le trafic de l'instance. |
| V-M1 course figée (étape 13) | **levé** | critère du devis § 4 (état poussé immobile 30 min avec journal muet) ; `logs <ID> 40` existe dans le suivi. Le devis § 5 garde `gpu_util`/`cpu_util` : écart déclaré dans le texte (« l'outil ne restitue pas l'usage de la carte »), cohérent avec le § 4. « Inchangé entre deux contrôles ≥ 30 min » équivaut à « muet » ; acceptable. |
| V-m1 essai discriminant | **levé** | voir ci-dessous. |
| V-m2 crédit | **levé** | < 1 USD → arrêt (devis § 5 : exact) ; plancher de l'étape B bis → message à la mère, montants donnés par elle. |
| V-m3 scellement, colonnes | **levé** | `python -m controle_ia.scellement sceller <tsv>` : forme correcte ; colonnes citées (`prix_avec_200_go`, `inet_up_cost_usd_go`, `inet_down_cost_usd_go`, `inet_up_mbit`, `verification`) : **toutes présentes** dans `COLONNES` du relevé, noms exacts ; colonnes d'options correctement écartées. |
| V-m4 durée restante | **levé** | D totale 91 374 s / 129 405 s inchangés, « moins le temps écoulé » dit. |
| outil du loueur absent | **levé** | `python3 -m venv /home/user/vastai-env && …/pip install -q vastai==1.11.0` : commande bien formée, chemin identique à celui des étapes 9 et 10, version identique à celle exigée ensuite. |

## L'essai v4 discrimine-t-il ?
Oui. Mutations sur copies : (1) chaque export lit la moyenne des deux moitiés au lieu de sa moitié → `[False]` (sommes distinctes) **échoue** ;
(2) sommes toujours égales → `[False]` **échoue** ; (3) moitiés écartées de 0,1 % seulement → passe : A2 compare des matrices en égalité exacte, donc tolérance nulle
(sans effet pour la course, à savoir). Le jumeau sain (`[False]`) et l'artefact (`[True]`) existent ; la somme détermine bien les matrices.
Réserve : la copie (1) et (2) ne touche que le cas distinct ; le cas égal est protégé par la comparaison directe de la dernière ligne de l'essai.

Empreintes : commande v3 `3dd57cc4…`, essai v4 `b44ed87a…` (préfixes).
