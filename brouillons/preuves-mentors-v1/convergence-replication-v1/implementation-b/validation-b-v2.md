# Validation de l'implémentation B, version 2 — v2

**Verdict : validation RÉUSSIE.** Sur la course originale (racine 20266201), écart absolu maximal entre ma sortie et l'analyse de référence : **0** sur 32 contrastes (16 par budget ; moyenne, écart-type, dix quantiles ; exigence ≤ 1e-9). Classes, verdicts et déclencheurs : **identiques** à ceux calculés sur les nombres de la référence et conformes au § 12.1 de la spécification v2. Les cas du § 12.3 (artefact, cas sain, décalages, seuil de trois tâches) rendent ce qu'attend la spécification.

Implémentation : `implementation_b_v2.py (implementation-b-v2)` · modèle : Claude Sonnet 5.5 (identifiant claude-sonnet-5-5), famille Claude, d'Anthropic · interpréteur `/home/claude/controle-ia-travail/.venv/bin/python` · Python 3.13.18 · numpy 2.4.6 · analyse complète en 0.789 s · validation complète en 96.7 s.

## Conditions de réussite

| Condition | Résultat |
|---|---|
| Empreintes des trois entrées conformes (spécification v2, résultats et analyse de la course originale) | oui |
| Règle D : trois vecteurs d'essai, gardes sur les six entiers, cas sain | oui |
| Générateur : indices des deux vecteurs d'essai du § 5.5 | oui |
| Entiers de plus de 2^63 : lecture, comparaison et écriture exactes | oui |
| Statistiques des 16 contrastes × 2 budgets à 1e-9 près | oui |
| Tableau de contrôle du § 12.1 (10 lignes lues dans la spécification v2) | oui |
| Classes (tables A, B, B′, C) identiques entre ma sortie et les nombres de la référence | oui |
| Verdicts (§ 9, § 10.1, après déclencheurs) et déclencheurs TR1 à TR4 identiques | oui |
| Écarts réduits z des quatre contrastes primaires concordants à 1e-9 | oui |
| Classes, contrôles et verdicts du § 9 conformes au texte du § 12.1 | oui |
| § 12.3 (a) : original contre lui-même → écart nul, TR2, quinze comptes à 200, arrêt, code 3 | oui |
| § 12.3 (b) à (e) : cas sain, R3 +0,06, R3 −0,03, trois tâches / deux tâches | oui |
| Suite d'essais (pytest) sans échec ni erreur | oui |

## Entrées (empreintes SHA-256)

- specification_v2 : `specification-statistique-decisive-v2.md` — `977dd9092cbd3715bd2cc9b5d5839f276242ad3f9df6302d383555f2b2ff511a` (conforme à l'empreinte épinglée : True)
- resultats_originaux : `resultats-regles-defense.json` — `d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b` (conforme à l'empreinte épinglée : True)
- analyse_de_reference_A : `analyse-regles-defense.json` — `18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42` (conforme à l'empreinte épinglée : True)
- Sortie de B sur la course originale : `sortie-b-originale-v2.json` — `11582b6db4aaec236952ef28756d72c1cdf7b46fa6f2587d85aa02d64af95d1d` (racine 20266201 ; code de sortie 3 ; lecture autorisée : False — attendu : l'original contre lui-même est l'artefact du § 12.3 (a))

## Le § 0 de la spécification v2, point par point

| # | Point | Dans B v1, puis dans B v2 | Détail |
|---|---|---|---|
| 1 | Contrôles T2, T3, T5, T6 : par budget ou globalement | déjà ainsi en v1 | états par budget, déclenché si au moins un budget ; v2 écrit en plus la marque de frontière globale |
| 2 | Ligne 2 de « HR1 répliquée ? » inatteignable | déjà ainsi en v1 pour la ligne ; changé en v2 pour la garde | ligne gardée mot pour mot ; v2 ajoute une alarme interne (code 2) si la ligne était atteinte par le chemin complet, et des essais |
| 3 | Deux issues globales (brute / après déclencheurs) | déjà ainsi en v1 | v2 ajoute la mention « V0 : non évaluée par B », « sous réserve de V0 » et la marque de frontière des issues |
| 4 | Frontière numérique : quelles comparaisons comptent | changé en v2 (partiellement déjà ainsi) | v1 : tables et contrôles T2/T5/T6 sans court-circuit, mais T4 (cos_moyen) non marqué, déclencheurs non marqués (TR1 en `any` à court-circuit), verdicts sans héritage des contrôles ni des déclencheurs ; v2 : tout cela est marqué et hérité sur le chemin de décision |
| 5 | Champs de E2 non vérifiés | changé en v2 | liste fermée de vérifications, chacune un arrêt (v1 : avertissements) |
| 6 | Nom du fichier compagnon | changé en v2 | v1 acceptait aussi `<fichier sans extension>.sha256` et ne faisait qu'avertir sur un nom de base différent ; v2 : `<fichier>.sha256` seul, une ligne exacte, empreinte et nom de base vérifiés (arrêt) |
| 7 | Résultats originaux sans compagnon | déjà ainsi en v1 | empreinte épinglée ; v2 précise : compagnon vérifié s'il existe, sinon empreinte épinglée, sinon arrêt ; variantes : `--empreinte-e1` |
| 8 | V0 et discordance A/B | changé en v2 | v1 : options `--plomberie-fausse` et `--discordance-ab` ; v2 : plus d'option de discordance, elle est calculée depuis E5 ; V0 non évaluée par B |
| 9 | Forme de E1 : « contient » | changé en v2 | v1 lisait « au moins » pour `resultat` mais exigeait exactement trois clés au premier niveau ; v2 : clés supplémentaires permises partout sauf dans `regles` |
| 10 | Arrêt sans sortie et auto-essai du § 12 : codes de sortie | changé en v2 | v1 : codes 0, 2, 3, 4 et discordance A/B hors du chemin d'analyse ; v2 : codes 0, 2, 3 seulement (sortie déjà existante = 2) et discordance A/B → 3 |
| 11 | T5 : première condition unilatérale, seconde bilatérale | déjà ainsi en v1 | v2 rend les deux conditions explicites dans la sortie (`a_unilaterale_declenche`, `b_bilaterale_declenche`) |
| 12 | « À 1e-12 près » pour [0 ; 1] | déjà ainsi en v1 | v2 écrit les bornes explicitement (−1e-12 ; float('1.000000000001')), égales à 1.0 + 1e-12 |
| 13 | Champs documentés non utilisés | changé en v2 | gardes neuves : `delta` (v1 : avertissement), `config_sha256` identique et épinglé, `lam` et `reference` ; `par_tour.exploitabilite` jamais exigé |
| 14 | L'analyse de A ne contient pas ses contrôles de santé | déjà ainsi en v1 | B ne lit pas les états de A ; classes, verdicts et déclencheurs « de A » sont calculés avec les contrôles recalculés depuis E1 |
| 15 | Seuil de T3 | déjà ainsi en v1 (même valeur) | v2 : constante hexadécimale `0x1.fffffff768fa1p-1` ; égale à 1.0 - 1e-9 et à float('0.999999999') |
| CL-10 | « Graines neuves » : seuil et mesures | changé en v2 | v1 : plus de 10 tâches, V seule, par variante ; v2 : plus de 2 tâches, V, X̄ et (ii), quinze comptes |
| — | Environnement | changé en v2 | interpréteur du dépôt, numpy 2.4.6 (validation et emploi) |

## Vecteurs d'essai

Règle D (§ 4) — H, ρ calculé, résultat :

- `d82dea33…` : ρ = 11786724493248295725 ; ρ_t = 9136419304016434890 → identiques aux attendus ; les gardes rejettent ce vecteur (interdit comme racine) : True
- `00000000…` : ρ = 15793235383387715774 ; ρ_t = 12390638538380655177 → identiques aux attendus ; les gardes rejettent ce vecteur (interdit comme racine) : True
- `ffffffff…` : ρ = 10168828190493638947 ; ρ_t = 4616211851522120706 → identiques aux attendus ; les gardes rejettent ce vecteur (interdit comme racine) : True
- Cas sain : la règle D appliquée à l'empreinte du préenregistrement original rend (11786724493248295725, 9136419304016434890), différent de (20266201, 20266202) : True.

Générateur (§ 5.5), racine 20266201 :

- clé (1, 203, 0, 0, 99) : forme (20000, 100), int64 ; ligne 0, dix premiers = [80, 79, 39, 86, 45, 87, 54, 22, 58, 80] ; dernière ligne, cinq derniers = [56, 63, 4, 66, 85] → conformes
- clé (2, 200, 0, 0, 99) : forme (20000, 100), int64 ; ligne 0, dix premiers = [73, 34, 66, 88, 64, 92, 23, 55, 84, 31] ; dernière ligne, cinq derniers = [10, 38, 20, 60, 51] → conformes

Entiers de 64 bits (§ 12.4) : 18446744073709551557 lu exactement : True ; son voisin est distinct comme entier (True) mais serait confondu en binaire64 (True) ; écrit en chaîne exacte : True.
Constantes : seuil de T3 `0x1.fffffff768fa1p-1` = 1.0 − 1e-9 : True ; = float('0.999999999') : True ; borne haute [0 ; 1] = 1.0 + 1e-12 : True ; G = 2.

## Tableau de contrôle du § 12.1 (10 lignes lues dans le texte de la spécification v2)

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

Niveau « arrêt » : les cinq contrastes dont une discordance arrête la lecture ; « alerte » : les onze autres.

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

Écart maximal absolu : tous contrastes **0** ; contrastes à arrêt 0 ; contrastes à alerte 0. Écart A/B maximal sur les z des quatre contrastes primaires : 0. Classes comparées : 25, différences : 0 ; éléments à la frontière : 0.

## Classes (première condition vraie ; budget 1 / budget 2)

- Table A (Δ(R3, R2) sur V) : ligne 2, « HR1 confirmée » — conforme au § 12.1 : True
- Table B (détection V) :
  - R0 : ≈ / ≈ — conforme : True
  - R1 : R2 ≳ R1 / ? — conforme : True
  - R3 : R3 > R2 / R3 > R2 — conforme : True
  - R4 : R4 ≳ R2 / R4 ≳ R2 — conforme : True
- Table B′ (exploitabilité moyenne X̄) :
  - R0 : ≈ / ≈ — conforme : True
  - R1 : R2 > R1 / R2 ≳ R1 — conforme : True
  - R3 : R3 > R2 / R3 > R2 — conforme : True
  - R4 : R4 ≳ R2 / R4 ≳ R2 — conforme : True
- Table C (détection (ii), numéro de ligne) :
  - R0 : 4 / 4 — conforme : True
  - R1 : 4 / 4 — conforme : True
  - R3 : 1 / 1 — conforme : True
  - R4 : 4 / 4 — conforme : True

## Contrôles de santé et verdicts du § 9

- T2 non déclenché : True ; T3 non déclenché : True (tâches à poids pur : [0, 0]) ; T4 non déclenché : True (tâches à cosinus moyen ≥ 0,999 : [5, 2], attendu 5 et 2)
- T5 non déclenché : True (plus grand écart standard − renforcé : 0.000387, attendu 0,00039 ; plus grand écart de contraste : 0.000427, attendu 0,00043) ; T6 non déclenché : True (plus grand écart à α : 0.000186, attendu 0,00019)
- Le mélange bat l'historique (HR1) : **HR1 confirmée** ; réentraîner vaut mieux que ne rien faire (HR0) : **réfutée** ; la régularisation ne nuit pas (HR3) : **confirmée** ; oublier coûte (HR2, descriptif) : **non tranchée** — conformes au § 12.1 : True.

## Gardes de la réplication : cas sain et artefact (§ 12.3)

- (a) artefact, l'original contre lui-même : écart g des quatre contrastes primaires [0.0, 0.0, 0.0, 0.0] (tous nuls : True) ; TR2 déclenché : True ; 15 comptes « graines neuves », tous égaux à 200 : True ; arrêt « graines non neuves » : True ; code de sortie 3 ; lecture autorisée : False ; issue brute : « non jugeable (plomberie) » → conforme : True
- (b) cas sain (+1e-6 ; R3 en plus +0,01) : plus grand compte 0 ; TR1 False ; TR2 False ; arrêt False ; code 0 → True
- (c) R3 +0,06 : TR1 déclenché True, z de R3 {'(R3, V, c=1)': 7.5003599048323135, '(R3, V, c=2)': 9.93858210839576} (positifs) → True
- (d) R3 −0,03 borné à 0 : TR1 déclenché True, z de R3 {'(R3, V, c=1)': -3.750179952416155, '(R3, V, c=2)': -4.969291054197875} (négatifs) → True
- (e) une variante (R1), trois tâches gardent leur V original : compte 3, arrêt True, code 3 → True ; deux tâches : compte 2, arrêt False, code 0 → True

## Suite d'essais (§ 12.2, 12.3, 12.4, 12.5, mutations)

- 560 essais lancés avec `/home/claude/controle-ia-travail/.venv/bin/python` : 560 passés, 0 échoués, 0 en erreur, 0 ignorés ; durée 91.567 s.
  - constantes, générateur, quantiles, lecture, CLI et divers : 16 essais, 0 échecs
  - § 12.1 course originale : 9 essais, 0 échecs
  - § 12.2 branches des tables, verdicts, contrôles, déclencheurs, issues : 241 essais, 0 échecs
  - § 12.3 gardes de la réplication (a) à (e) et comparaison A/B : 52 essais, 0 échecs
  - § 12.4 entiers de 64 bits et règle D : 34 essais, 0 échecs
  - § 12.5 gardes d'entrée, cas sain et artefact : 187 essais, 0 échecs
  - essais rattachés aux mutations de B v1 et aux exigences neuves : 21 essais, 0 échecs
- Campagne de mutations : 150/150 détectées : 140 dès la première version de la suite ; les 10 survivantes de ce premier passage (M12, M41, M42, M52, M66, M106, M139, M142, M143, M146) ont reçu des essais « mut » et sont détectées par la suite finale ; aucune mutation équivalente conservée.

## Marges aux seuils

Plus petite distance entre une quantité comparée et son seuil, sur les comparaisons évaluées pour chaque classe (frontière numérique : 1e-9). Les six plus petites :

- table_B/R1/budget 2 : 4.761e-05
- table_Bprime/R1/budget 1 : 1.068e-04
- table_Bprime/R4/budget 2 : 9.172e-04
- table_Bprime/R1/budget 2 : 9.569e-04
- table_B/R1/budget 1 : 1.158e-03
- table_Bprime/R4/budget 1 : 2.812e-03

Classes marquées à la frontière : aucune.

## Recoupements hors contrat de la spécification (informatif)

72 comparaisons de champs de l'analyse de référence qui ne font pas partie du contrat (moyennes par variante, cosinus moyens par tâche de R4, part de tâches à poids pur de R3, contrastes standard seul / renforcé seul). Écart maximal absolu : **1.11e-16**.

## Table de correspondance « élément du § 11.1 → clé JSON »

| Élément | Clé(s) JSON |
|---|---|
| Verdict d'ensemble : lecture autorisée ; motifs d'arrêt (§ 11.1) | `lecture_autorisee`, `motifs_arret`, `code_de_sortie` |
| Empreinte H ; racines ρ, ρ_t en chaînes décimales | `H`, `racines.rho`, `racines.rho_t`, `racine_de_reechantillonnage` |
| Contrastes de chaque budget, indexés par libellé (§ 5.7) | `resultat."1"|"2".contrastes_contre_R2.<libellé>.{moyenne, ecart_type, n, quantiles, zeros_exacts}` |
| Intervalles B2, B8, E8 | `intervalles."1"|"2".<libellé>.{B2, B8, E8}` |
| Classes des Tables A, B, B′, C avec leurs marques de frontière | `classes.table_A`, `classes.table_B.<R0|R1|R3|R4>."1"|"2"`, `classes.table_Bprime…`, `classes.table_C…` (clés `ligne`, `classe`, `frontiere`, `frontiere_propre`, `heritee_de`, `marge_min_au_seuil`, `comparaisons_a_la_frontiere`) ; liste : `classes_a_la_frontiere` |
| Contrôles T2 à T6 : valeurs comparées et état, par budget | `sante."1"|"2".<T2…T6>.{declenche, frontiere, …valeurs}` ; moyennes de V : `sante."c".moyennes_V` |
| Contrôles : état global (au moins un budget) et marque globale | `sante.etat_global.<T2…T6>`, `sante.frontiere_globale.<T2…T6>` |
| Verdicts du § 9 (course originale) | `verdicts_regles_originales.{HR1, HR0, HR3, HR2}.verdict` |
| Verdicts bruts du § 10.1 | `verdicts_bruts_replication.{HR1, HR0, HR3, lois_tenues_ii, HR2}.{ligne, verdict, frontiere}` ; classes κ : `kappa_R0_V`, `kappa_prime_R4_V`, `lignes_C_R0_ii` |
| g_π, σ_π, z_π | `ecart_de_replication.contrastes_primaires."(R3, V, c=1)"….{g, sigma, z, est_rep, s_rep, est_or, s_or}` |
| État de TR1 à TR4 (avec marques) et « au moins un » | `declencheurs_audit.{TR1, TR2, TR3, TR4, au_moins_un}.{declenche, frontiere}` |
| Verdicts après l'effet du § 10.2 | `verdicts_apres_declencheurs.{HR1, HR0, HR3, lois_tenues_ii}.{verdict, frontiere}` |
| Les quinze comptes « graines neuves » (§ 10.3) | `comptes_graines_neuves.comptes.<R0|R1|R2|R3|R4>.<V_iii_final|exploitabilite_moyenne_tours|ii_final>` ; `comptes_graines_neuves.arret_graines_non_neuves` |
| Deux issues globales (§ 10.4) et mention de V0 | `issues_globales.brute`, `issues_globales.apres_declencheurs` (clés `ligne`, `issue`, `frontiere`, `V0`, `sous_reserve_de_V0`) ; `issues_globales.V0` = « V0 : non évaluée par B » |
| Résultat de la comparaison A/B (§ 11.2) | `comparaison_A_B.{evaluee, discordance_a_arret, motifs, alertes_de_discordance, detail_par_contraste, z_pi, classes, verdicts_et_declencheurs, concordance}` |
| Empreintes de tous les fichiers lus | `empreintes_fichiers[].{role, fichier, sha256}` ; ordre des lectures : `ordre_des_lectures` |
| Versions (Python, numpy) | `meta_non_deterministe.versions.{python, numpy, implementation}` |
| Valeur de toute option de ligne de commande employée | `options.{mode, plomberie_fausse_V0, empreinte_E1_imposee_en_ligne_de_commande}` |
| Valeurs lues dans E2 (réplication) | `manifeste_E2.{run_id, lambda, reference, n_instances, config_sha256, prereg_sha256}` |

## Commande exacte pour la course (chemins à compléter par la session principale)

```
/home/claude/controle-ia-travail/.venv/bin/python \
  /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/implementation_b_v2.py replication \
  --resultats <RACINE_DEPOT>/diag/<run>/resultats-regles-defense.json \
  --manifeste <RACINE_DEPOT>/runs/<run>/manifeste.json \
  --prereg <RACINE_DEPOT>/prereg/preregistrement-replication-regles-defense-convergence-v1.md \
  --analyse-A <RACINE_DEPOT>/diag/<run>/analyse-regles-defense.json \
  --analyse-originale /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/analyse-regles-defense.json \
  --resultats-originaux /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/resultats-regles-defense.json \
  --sortie /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/sortie-b-replication-v2.json
```

Aucune option ne peut changer un seuil, sauter une vérification ou forcer une racine. Seule option qui touche une ligne du § 10.4 : `--plomberie-fausse` (défaut neutre : non ; sa valeur est écrite dans `options.plomberie_fausse_V0`). Sortie : code 0 (lecture autorisée), 2 (arrêt d'entrée, aucune sortie) ou 3 (arrêt de contrôle, sortie écrite, `lecture_autorisee: false`).

## Ce que cette validation ne couvre pas

- Le mode `replication` de bout en bout (règle D sur un texte scellé, E2, E3, E5, compagnons) n'est essayé que sur des pièces synthétiques construites à partir de la course originale ; aucune donnée de la réplication n'existe encore.
- Les sorties des essais (b) à (e) sont obtenues sans E5 (A n'a pas calculé ces variantes) : la discordance A/B n'y est pas évaluée (elle l'est sur la course originale contre sa propre analyse, et sur des analyses synthétiques altérées dans les essais).
- Les contrôles de santé de A ne sont pas dans l'analyse de la course : leur confrontation est limitée aux champs voisins (recoupements hors contrat) et au texte du § 12.1.
- La campagne de mutations est un contrôle de la suite d'essais, pas une preuve de justesse ; son code vit hors du dossier livré.

## Ambiguïtés restantes (lecture prudente retenue dans chaque cas)

- Présence de `temps` dans `resultat` : le § 3 écrit « `resultat` contient `temps` et `resultats` », le tableau « Emploi de chaque champ » écrit « `temps` … présence non exigée ». Lecture prudente retenue (celle qui arrête) : `temps` est exigé.
- Contenu admis d'un compagnon : le § 3 dit « une seule ligne non vide » puis « une fin de ligne ». Lecture prudente : le fichier est exactement `<64 hexadécimaux minuscules>␣␣<nom de base>\n` (ni ligne vide en plus, ni retour chariot, ni dossier dans le nom).
- Marques de frontière héritées : « toute classe, tout contrôle, tout déclencheur qui y entre » est lu comme « examiné sur le chemin de décision du verdict (lignes examinées jusqu'à la première vraie comprise) » ; lecture prudente puisqu'une marque ne fait que tolérer une divergence (donc plus étroite = plus d'arrêts). Pour HR3 original et réplication, T4 entre quand la ligne qui le teste est examinée.
- Comparaison A/B des contrastes de concordance exigée : n et zéros exacts identiques sont exigés EN PLUS des douze écarts à ε près (lecture prudente ; le § 11.2 ne cite que la moyenne, l'écart-type et les dix quantiles).
- « Égale au bit » du § 10.3 : lu comme égalité des 64 bits (0.0 et −0.0 seraient distincts ; le § 10.3 écrit aussi « égalité de binaires64 »).
- « Arrêt » de la ligne 1 du § 10.4 : lu comme tout arrêt de contrôle de B (graines non neuves, discordance A/B de niveau arrêt) ; les alertes (11 autres contrastes) n'y entrent pas.
- Le § 11.2 compare « verdicts bruts » ; B compare aussi les verdicts du § 9, les verdicts après déclencheurs et HR2 recopié (plus strict).
- Si E1 d'un essai porte des racines ≠ (20266201, 20266202), c'est un arrêt d'entrée ; en réplication, E1 doit porter (ρ, ρ_t) de la règle D.
- E5 : les champs `run_id` et `manifeste_sha256` du premier niveau de l'analyse sont exigés ; en mode essai (pas de E2) `manifeste_sha256` est comparé à celui de E1.
- Une marque de frontière sur un élément ne fait que tolérer une différence A/B ; la valeur « retenue » est celle de A, mais B ne remplace pas ses propres classes : il écrit les deux.
- T3 : la comparaison du plus grand poids à 0x1.fffffff768fa1p-1 porte sur une valeur brute de E1 (exclue de la marque, § 8) ; B écrit seulement à titre d'information le nombre de tâches à moins de ε de ce seuil, sans marque.
- Contrastes de concordance exigée : « z_π(A) − z_π(B) ≤ 1e-9 » est appliqué aux quatre contrastes primaires, ce qui est plus étroit que la tolérance sur la moyenne (un écart de 5e-10 sur la moyenne d'un contraste primaire déplace z_π de plus de 1e-9 : arrêt).
- Mode `essai` (pièces de la course originale ou de ses variantes) : sous-commande de B hors du contrat du § 3, utilisée pour le § 12 ; elle impose les racines de la course originale et ne peut pas servir pour la réplication (E3 et E2 y sont refusés).

## Fichiers ouverts pendant tout le travail (lecture ou exécution)

- /home/claude/controle-ia-travail/CLAUDE.md (consignes permanentes du dépôt, fournies par l'outil dans le contexte de la session ; non ouvert par une commande)
- /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/consigne-implementation-b-v2.md (lu)
- /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/specification-statistique-decisive-v2.md (lu en entier ; empreinte vérifiée)
- /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/specification-statistique-decisive-v1.md (v1, lu lors du travail précédent)
- /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/resultats-regles-defense.json (lu ; empreinte vérifiée)
- /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/entrees/analyse-regles-defense.json (lu ; empreinte vérifiée)
- /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/implementation_b.py (v1, lu, non modifié)
- /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/test_implementation_b.py (v1, lu, non modifié)
- /home/claude/controle-ia-travail/brouillons/preuves-mentors-v1/convergence-replication-v1/implementation-b/validation-b-v1.md, validation-b-v1.json, sortie-b-originale-v1.json (v1, lus, non modifiés)
- /home/claude/controle-ia-travail/.venv/bin/python (exécution) ; pytest 9.1.1 et numpy 2.4.6 de ce même environnement (importés par l'exécution)
- /tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/mut/mutations.py (mon script de mutations de la v1, lu pour l'adapter)
- /tmp/claude-0/-home-claude/730d0294-0b2b-55ca-8b32-49f2d3ec072d/scratchpad/v2/ (mes brouillons : part1-3.py, tpart1-4.py, mutations2.py, run/, mutw/ ; supprimés à la fin)
- Listage (ls) des dossiers …/convergence-replication-v1/, …/implementation-b/ et du dossier temporaire de la session (noms seulement ; aucun fichier étranger à ce travail n'a été ouvert)
- /tmp/pytest-of-root/ et dossiers temporaires créés par les essais et la campagne de mutations (écrits par les essais eux-mêmes, supprimés à la fin)

## Modèle

Claude Sonnet 5.5 (identifiant claude-sonnet-5-5), famille Claude, d'Anthropic.

