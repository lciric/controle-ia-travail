# Fiche — Gao, *From Probe Scores to Alarm Policies: Operational Validity of Activation Monitors for Language-Model Agents* (DAI 2026 ; arXiv 2610.04575v1, 3 octobre 2026) — v1

- **Source déjà tenue par le programme** : `pdf-main/2610.04575v1.pdf`, SHA-256
  `ef50ec541464c3ee8e3f2fda9251684668238377575b2530341319f474dce12c` (préfixe contrôlé le 2026-10-26 à 11:25 UTC ;
  valeur complète dans `provenance-niveau2-lot4-v1.md`) ; non retéléchargée.
- **Pages lues** : 1–2.
- **Chez session-depot** : **non**.

## Ce que la source établit sur un mode d'échec

1. **L'aire sous la courbe et l'alarme à seuil sont deux estimandes différentes.** Un moniteur peut bien classer et
   être inutilisable au taux de fausses alarmes que la politique d'alarme peut se permettre (p. 1).
2. **Unité de risque** : quand une tâche contient plusieurs occasions d'alarme, l'aire sous la courbe et le taux de faux
   positifs par ligne n'identifient pas le risque « au moins une alarme » par tâche ou trajectoire (p. 1).
3. **Chiffres** : des moniteurs joints activations-observables atteignent 0,957 et 0,935 d'aire sous la courbe, mais
   leurs taux de détection verrouillés à 5 % et 10 % ne sont que de 0,642/0,742 et 0,719/0,782 ; sur AgentDojo, un
   moniteur à 0,922 ne détecte aucun des 38 cas positifs au point de fonctionnement verrouillé à 5 %, et des seuils
   prévus pour 10 % de fausses alarmes en réalisent 18,7 à 20,0 % en test ; sur un autre banc, 23 négatifs
   d'étalonnage indépendants ne suffisent pas à certifier même un contrôleur à 10 % (p. 1).
4. **Seuil certifié** : il exige assez d'unités négatives indépendantes, une règle sûre en cas d'égalité, et un
   transport vers le déploiement (p. 1).

## Conditions

- Agent Qwen2.5-7B sous injection d'invite (AgentDojo), autres bancs ; un auteur ; atelier ou conférence DAI 2026
  (p. 1).

## Ce qu'elle ne dit pas

- Rien sur la tromperie ou le sabotage diffus ; rien sur les processus e.

## Ce que ça touche chez nous (avis)

- Critère de G1 (rappel à 1 % de faux positifs) et agrégation séquentielle : le taux de faux positifs doit être défini
  et étalonné à l'unité où l'alarme coûte (épisode, trajectoire, essaim), sur assez de négatifs indépendants ; un
  rappel « par action » ne se transporte pas à l'épisode.

## Phrase citée

« A monitor can therefore rank examples well while being unusable at the false-alarm rate that the alarm policy can
afford. » (p. 1)
