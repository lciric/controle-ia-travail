# Validation de l'implémentation B sur la course originale — v1

**Verdict : validation RÉUSSIE.** Écart maximal absolu entre ma sortie et l'analyse de référence : **0** sur 32 contrastes (16 par budget, chacun : moyenne, écart-type, dix quantiles ; exigence ≤ 1e-9). Classes et verdicts : **identiques** à ceux de la référence et à ceux écrits dans le § 12 de la spécification.

Implémentation : `implementation_b.py (implementation-b-v1)` · Python 3.13.18 · numpy 2.5.3 · analyse en 0.818 s (validation complète : 0.992 s).

## Conditions de réussite

| Condition | Résultat |
|---|---|
| Empreintes des trois entrées conformes | oui |
| Règle D : trois vecteurs d'essai, gardes sur les six entiers, cas sain | oui |
| Générateur : indices des deux vecteurs d'essai du § 5.5 | oui |
| Statistiques des 16 contrastes × 2 budgets à 1e-9 près | oui |
| Tableau de contrôle du § 12 (10 lignes lues dans la spécification) | oui |
| Classes (tables A, B, B′, C) identiques entre ma sortie et les nombres de la référence | oui |
| Verdicts identiques entre ma sortie et les nombres de la référence | oui |
| Écarts réduits z des quatre contrastes primaires concordants à 1e-9 | oui |
| Classes, contrôles, verdicts et auto-essai conformes au texte du § 12 | oui |

## Entrées (empreintes SHA-256)

- specification : `specification-statistique-decisive-v1.md` — `2a1ad6d356ab60d44aebbf8d92ee9ba932bd24f925ae4fb86538545e0706e0e5` (attendu : `2a1ad6d3…`)
- resultats_originaux : `resultats-regles-defense.json` — `d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b` (attendu : identique : True)
- analyse_de_reference_A : `analyse-regles-defense.json` — `18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42` (attendu : identique : True)
- Sortie de B : `sortie-b-originale-v1.json` — `336bc6d3425fcc1194473953b93a3c40c2d4adbcecd8853f8820bec452508f8c` (racine 20266201)

## Vecteurs d'essai

Règle D (§ 4) — H, ρ calculé, ρ attendu, résultat :

- `d82dea33…` : ρ = 11786724493248295725 ; ρ_t = 9136419304016434890 → identiques aux attendus ; les gardes rejettent bien ce vecteur (interdit comme racine) : True
- `00000000…` : ρ = 15793235383387715774 ; ρ_t = 12390638538380655177 → identiques aux attendus ; les gardes rejettent bien ce vecteur (interdit comme racine) : True
- `ffffffff…` : ρ = 10168828190493638947 ; ρ_t = 4616211851522120706 → identiques aux attendus ; les gardes rejettent bien ce vecteur (interdit comme racine) : True
- Cas sain : la règle D appliquée à l'empreinte du préenregistrement original rend (11786724493248295725, 9136419304016434890), différent de (20266201, 20266202) : True.

Générateur (§ 5.5), racine 20266201 :

- clé (1, 203, 0, 0, 99) : forme (20000, 100), int64 ; ligne 0, dix premiers = [80, 79, 39, 86, 45, 87, 54, 22, 58, 80] ; dernière ligne, cinq derniers = [56, 63, 4, 66, 85] → conformes
- clé (2, 200, 0, 0, 99) : forme (20000, 100), int64 ; ligne 0, dix premiers = [73, 34, 66, 88, 64, 92, 23, 55, 84, 31] ; dernière ligne, cinq derniers = [10, 38, 20, 60, 51] → conformes

## Tableau de contrôle du § 12 (10 lignes lues dans le texte de la spécification)

| Budget | Contraste | Écart max. absolu (moyenne, écart-type, 4 quantiles) | Conforme |
|---|---|---|---|
| 1 | R3 - R2 (V_iii_final) | 0 | oui |
| 1 | R0 - R2 (V_iii_final) | 0 | oui |
| 1 | R4[moyenne,λ=0.3] - R2 (V_iii_final) | 0 | oui |
| 1 | R0 - R2 (ii_final) | 0 | oui |
| 1 | R1 - R2 (exploitabilite_moyenne_tours) | 0 | oui |
| 2 | R3 - R2 (V_iii_final) | 0 | oui |
| 2 | R0 - R2 (V_iii_final) | 0 | oui |
| 2 | R4[moyenne,λ=0.3] - R2 (V_iii_final) | 0 | oui |
| 2 | R0 - R2 (ii_final) | 0 | oui |
| 2 | R1 - R2 (exploitabilite_moyenne_tours) | 0 | oui |

## Concordance avec l'analyse de référence, contraste par contraste

Niveau « arrêt » : les cinq contrastes dont une discordance arrête la lecture ; « alerte » : les onze autres. Colonne « n / zéros » : nombre d'instances et nombre de différences exactement nulles, identiques à la référence.

| Budget | Contraste | Niveau | Écart max. absolu | n / zéros |
|---|---|---|---|---|
| 1 | R0 - R2 (V_iii_final) | arrêt | 0 | oui |
| 1 | R1 - R2 (V_iii_final) | alerte | 0 | oui |
| 1 | R3 - R2 (V_iii_final) | arrêt | 0 | oui |
| 1 | R4[moyenne,λ=0.3] - R2 (V_iii_final) | arrêt | 0 | oui |
| 1 | R0 - R2 (ii_final) | arrêt | 0 | oui |
| 1 | R1 - R2 (ii_final) | alerte | 0 | oui |
| 1 | R3 - R2 (ii_final) | alerte | 0 | oui |
| 1 | R4[moyenne,λ=0.3] - R2 (ii_final) | alerte | 0 | oui |
| 1 | R0 - R2 (exploitabilite_finale) | alerte | 0 | oui |
| 1 | R1 - R2 (exploitabilite_finale) | alerte | 0 | oui |
| 1 | R3 - R2 (exploitabilite_finale) | alerte | 0 | oui |
| 1 | R4[moyenne,λ=0.3] - R2 (exploitabilite_finale) | alerte | 0 | oui |
| 1 | R0 - R2 (exploitabilite_moyenne_tours) | alerte | 0 | oui |
| 1 | R1 - R2 (exploitabilite_moyenne_tours) | arrêt | 0 | oui |
| 1 | R3 - R2 (exploitabilite_moyenne_tours) | alerte | 0 | oui |
| 1 | R4[moyenne,λ=0.3] - R2 (exploitabilite_moyenne_tours) | alerte | 0 | oui |
| 2 | R0 - R2 (V_iii_final) | arrêt | 0 | oui |
| 2 | R1 - R2 (V_iii_final) | alerte | 0 | oui |
| 2 | R3 - R2 (V_iii_final) | arrêt | 0 | oui |
| 2 | R4[moyenne,λ=0.3] - R2 (V_iii_final) | arrêt | 0 | oui |
| 2 | R0 - R2 (ii_final) | arrêt | 0 | oui |
| 2 | R1 - R2 (ii_final) | alerte | 0 | oui |
| 2 | R3 - R2 (ii_final) | alerte | 0 | oui |
| 2 | R4[moyenne,λ=0.3] - R2 (ii_final) | alerte | 0 | oui |
| 2 | R0 - R2 (exploitabilite_finale) | alerte | 0 | oui |
| 2 | R1 - R2 (exploitabilite_finale) | alerte | 0 | oui |
| 2 | R3 - R2 (exploitabilite_finale) | alerte | 0 | oui |
| 2 | R4[moyenne,λ=0.3] - R2 (exploitabilite_finale) | alerte | 0 | oui |
| 2 | R0 - R2 (exploitabilite_moyenne_tours) | alerte | 0 | oui |
| 2 | R1 - R2 (exploitabilite_moyenne_tours) | arrêt | 0 | oui |
| 2 | R3 - R2 (exploitabilite_moyenne_tours) | alerte | 0 | oui |
| 2 | R4[moyenne,λ=0.3] - R2 (exploitabilite_moyenne_tours) | alerte | 0 | oui |

Écart maximal absolu : tous contrastes **0** ; contrastes à arrêt 0 ; contrastes à alerte 0. Écarts réduits z des quatre contrastes primaires : écart A/B maximal 0.

## Classes (première condition vraie ; budget 1 / budget 2)

- Table A (Δ(R3, R2) sur V, détection finale) : ligne 2, « HR1 confirmée » — conforme au § 12 : True
- Table B (détection V) :
  - R0 : ≈ / ≈ — conforme au § 12 : True
  - R1 : R2 ≳ R1 / ? — conforme au § 12 : True
  - R3 : R3 > R2 / R3 > R2 — conforme au § 12 : True
  - R4 : R4 ≳ R2 / R4 ≳ R2 — conforme au § 12 : True
- Table B′ (exploitabilité moyenne X̄) :
  - R0 : ≈ / ≈ — conforme au § 12 : True
  - R1 : R2 > R1 / R2 ≳ R1 — conforme au § 12 : True
  - R3 : R3 > R2 / R3 > R2 — conforme au § 12 : True
  - R4 : R4 ≳ R2 / R4 ≳ R2 — conforme au § 12 : True
- Table C (détection sur les lois tenues à l'écart, ligne) :
  - R0 : 4 / 4 — conforme au § 12 : True
  - R1 : 4 / 4 — conforme au § 12 : True
  - R3 : 1 / 1 — conforme au § 12 : True
  - R4 : 4 / 4 — conforme au § 12 : True
- Comparaison avec les classes calculées sur les nombres de la référence : 25 classes comparées, différences : 0 ; classes à la frontière numérique : 0.

## Contrôles de santé (budget 1 / budget 2)

- T2 (résultat trop beau ou jeu trop mauvais) non déclenché : True
- T3 (mélange dégénéré) non déclenché : True ; tâches à poids pur : [0, 0]
- T4 (régularisation dégénérée) non déclenché : True ; tâches à cosinus moyen ≥ 0,999 : [5, 2] (attendu : 5 et 2)
- T5 (écart entre les deux optimiseurs) non déclenché : True ; plus grand écart standard − renforcé : 0.000387 (attendu : 0,00039) ; plus grand écart de contraste : 0.000427 (attendu : 0,00043)
- T6 (dérive du taux de fausses alertes) non déclenché : True ; plus grand écart à α : 0.000186 (attendu : 0,00019)

## Verdicts de la course originale (§ 9)

- Le mélange bat l'historique (HR1) : **HR1 confirmée**
- Réentraîner vaut mieux que ne rien faire (HR0) : **réfutée**
- La régularisation ne nuit pas (HR3) : **confirmée**
- Oublier coûte (HR2, descriptif) : **non tranchée**
- Conformes au § 12 : True ; identiques aux verdicts calculés sur les nombres de la référence : True.

## Essai des gardes de la réplication « contre elle-même » (§ 12, cas artefact)

- g des quatre contrastes primaires : [0.0, 0.0, 0.0, 0.0] → tous nuls : True
- TR2 (résultat trop propre) déclenché : True
- Comptes « graines neuves » : {'R0': 200, 'R1': 200, 'R2': 200, 'R3': 200, 'R4': 200} → tous égaux à 200 : True
- Arrêt « graines non neuves » déclenché : True
- Conforme au § 12 : True. Code de sortie de la commande `analyser` dans ce cas : 3 (sortie écrite, lecture non autorisée).

## Marges aux seuils (ce qui rend les classes robustes au calcul numérique)

Plus petite distance entre une quantité comparée et son seuil, sur les comparaisons effectivement évaluées pour chaque classe (seuil de frontière numérique : 1e-9). Les six plus petites :

- table_B/R1/budget 2 : 4.761e-05
- table_Bprime/R1/budget 1 : 1.068e-04
- table_Bprime/R4/budget 2 : 9.172e-04
- table_Bprime/R1/budget 2 : 9.569e-04
- table_B/R1/budget 1 : 1.158e-03
- table_Bprime/R4/budget 1 : 2.812e-03

Classes marquées à la frontière : aucune.

## Recoupements hors contrat de la spécification (informatif)

72 comparaisons de champs de l'analyse de référence qui ne font pas partie du contrat (moyennes par variante, écart standard − renforcé, cosinus moyens par tâche de R4, part de tâches à poids pur de R3, contrastes « V standard seul / renforcé seul »). Écart maximal absolu : **1.11e-16**.

## Ce que cette validation ne couvre pas

- Le mode réplication (règle D appliquée au texte scellé, manifeste, fichiers compagnons, concordance des racines) n'a pas de données réelles à ce stade ; il est essayé par les tests unitaires sur des pièces synthétiques (`test_implementation_b.py`).
- Les contrôles de santé de la référence A ne sont pas dans l'analyse de la course : ils sont confrontés au texte du § 12 et aux champs voisins de l'analyse (recoupements ci-dessus), pas à des états écrits par A.
- La concordance des écarts réduits z est établie ici sur le cas où A et B portent sur les mêmes résultats (essai contre elle-même).

