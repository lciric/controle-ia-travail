# Préenregistrement — réplication sur graine neuve de la course de convergence des règles de défense (mélange d'équilibre, défense figée, historique) — v1 — BROUILLON 1 (non scellable : champs à remplir)

**Statut** : brouillon 1, écrit le 1er novembre 2026 (≈ 21:45 UTC) par un sous-agent neuf (Claude Opus 5.5) qui n'a écrit ni le code de la course (v2), ni l'arène v4, ni le préenregistrement original, ni sa lecture, ni son audit. Rien n'est décidé, scellé ni commité. Champs restant à remplir (marqués en capitales pour le validateur) : le code v3 et son empreinte (bloc d'identité à régénérer par le code), le commit, l'empreinte de l'implémentation indépendante B, la décision sur N (recommandation écrite), la contre-lecture. Le validateur `controle_ia.prereg` refuse ce texte tant qu'un marqueur reste : c'est voulu.

Pièces d'appui, dans le même dossier : `etat-des-lieux-v1.md` (ce qu'est la course, où sont le code et la statistique, ce qu'ont appliqué la lecture et l'audit, réserves) et `specification-statistique-decisive-v1.md` (statistique, classes, verdicts et règles de cette réplication en langage mathématique, avec vecteurs d'essai vérifiés sur la course originale ; ci-après « la spécification »).

- Identifiant : **PREREG-REPLICATION-REGLES-DEFENSE-V1**
- Auteur : sous-agent neuf (Claude Opus 5.5), brouillon 1 ; aucun autre rôle dans cette chaîne.
- Date (UTC) : 2026-11-01, brouillon 1 ≈ 21:45 UTC.
- Commit du code d'analyse : À REMPLIR — commit qui contient `arene_regles_defense_v3.py` à l'empreinte du bloc d'identité et `test_arene_regles_defense_v3.py`.
- Documents qui font foi (chemin + empreinte) :
  - préenregistrement scellé de la course originale `prereg/preregistrement-regles-defense-convergence-v1.md` — `d82dea3388684dd369520b4f394c53b9e5f71159b9c056a6f739ef32c73d025d` (monde, règles, mesures, tables A et B dont ce texte reprend les classes) ;
  - code de la course originale `docs/notes/convergence-defense-v1/regles-defense-v1/arene_regles_defense_v2.py` — `9f0dcf5e0d10fe93dd19c318f076728d62b64734161dc72b40a812a817340da3` (référence du diff v2 → v3) ; essais `test_arene_regles_defense_v2.py` — `78d979ab76bbe4b3ad6b55be77bf2b745a4457940eb9cb4c16a3ee87ef324b81` ;
  - gel v2 `docs/notes/convergence-defense-v1/regles-defense-v1/gel-regles-defense-v2.md` — `9977d7df7f87f081f3c89709c6f36ab2c3861cb06c972dffbabe0e777e9910f3` (définition des règles, inchangée) ;
  - arène v4 `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/arene_melange_v4.py` — `70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61` (copie suivie par git, identique au bit au fichier `donnees/argon-seul-convergence-v1/arene_melange_v4.py` chargé par la course originale) ;
  - résultats de la course originale `diag/20261101-160323-regles-defense-convergence/resultats-regles-defense.json` — `d07ece476cc1f33b6179c6395ec486e944a170dc6d4f77bae42b153038d5f93b` ; analyse `…/analyse-regles-defense.json` — `18b801123040c28894ccd2601f8da93b1ed8bc87d015b3db1b1603a91e680e42` ; manifeste `runs/20261101-160323-regles-defense-convergence/manifeste.json` — `36db58cfac9bfc4cf199ca5cdf74ac17ea24afab84b95ffd0aac945b922a6720` ;
  - lecture préenregistrée originale `lecture-course-regles-defense-v1.md` — `24081eed65cebd8dd01d6e17ec76c5a6433d171da68ccbaa50657421cd7c4a23` ; audit « trop beau » — `7e81d094868e0d9cd2c03b73b5ca80cd0cd028b717a8085e027182fb57bd9966` ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` — `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` ;
  - spécification `brouillons/preuves-mentors-v1/convergence-replication-v1/specification-statistique-decisive-v1.md` — À REMPLIR (empreinte de la version contre-lue ; aucune empreinte compagnon n'est écrite par l'auteur du brouillon).

### Bloc d'identité (à régénérer par `arene_regles_defense_v3.py identite` ; vérifié par le code à la décision)

- Identifiant : PREREG-REPLICATION-REGLES-DEFENSE-V1
- Racines : RACINES_REPLICATION = règle D (dérivées de l'empreinte SHA-256 de ce texte scellé ; jamais écrites dans ce texte ; § Plan 3)
- Code : `arene_regles_defense_v3.py` — À REMPLIR
- Code de la course originale (référence du diff) : `arene_regles_defense_v2.py` — 9f0dcf5e0d10fe93dd19c318f076728d62b64734161dc72b40a812a817340da3
- Arène v4 : `arene_melange_v4.py` — 70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61
- Gel : `gel-regles-defense-v2.md` — 9977d7df7f87f081f3c89709c6f36ab2c3861cb06c972dffbabe0e777e9910f3
- Configuration (empreinte de la forme canonique) : 3fbb27fc0824b7a9d13a0036c975c43e00e4dc7ece9f0231dfca7c0234785098 (identique à la course originale si N = 100, § Seuil S-N)
- Bibliothèque `src/controle_ia/gardes.py` — a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439
- Bibliothèque `src/controle_ia/prereg.py` — 3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306
- Bibliothèque `src/controle_ia/scellement.py` — 93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2
- Bibliothèque `src/controle_ia/manifeste.py` — 1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d
- Versions : numpy 2.4.6 ; scipy 1.17.1 ; Python 3.13.18
- Implémentation indépendante B : chemin et empreinte — À REMPLIR (scellée avant la création du manifeste de la course)

<!-- configuration-canonique-debut -->
```json
{
 "K": 3,
 "T": 8,
 "alpha": 0.01,
 "audit_critere": 0.01,
 "audit_departs": 100,
 "audit_es_generations": 400,
 "audit_es_lambda": 12,
 "audit_iter": 300,
 "audit_k": 10,
 "audit_n_mc": 1024,
 "audit_quantile_t": 0.995,
 "boite_mu": 5.0,
 "d": 6,
 "deltas": [
  1.4,
  1.6
 ],
 "departs": 4,
 "departs_cout": 3,
 "departs_entr": 8,
 "departs_final": 12,
 "departs_renforce": 48,
 "entrainement": "detection",
 "fractions_courbe": [
  0.25,
  0.5,
  0.75
 ],
 "grille_calibrage": [
  0.6,
  0.8,
  1.0,
  1.2,
  1.4,
  1.6,
  1.8,
  2.0,
  2.4
 ],
 "iter_entr": 300,
 "iter_max": 100,
 "iter_renforce": 200,
 "kappa_contournement": 0.5,
 "l2": 0.001,
 "lambda_ou": 8.0,
 "n_attaque_entr": 2001,
 "n_cal": 20000,
 "n_calibrage": 48,
 "n_eval": 19998,
 "n_eval_tenue": 3999,
 "n_fpr": 20000,
 "n_instances": 100,
 "n_mc": 256,
 "n_mc_final": 512,
 "n_propre_entr": 2000,
 "n_tenue": 50,
 "pas_bissection": 3,
 "plafond_cpu_tache_s": 600.0,
 "r_cible": 4.0,
 "schema_graines": "SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, role, ...)) ; bras commun 0, A 1, B 2, D 4, C1 5, C2 6, C3 7, B' 8, C3' 9 ; roles cible 0, propre 1, attaques d'entrainement 2, calibration 3, fausses alertes 4, Monte-Carlo 5, departs 6, evaluation 7, init maxout 8, lois tenues 9, echantillons tenus 10, final 11, cout 12, Dirichlet 13, courbe 14, attaquant independant 15 ; reechantillonnage (code_delta, code_contraste, 0, 0, 99)",
 "seuil_calibrage_bas": 0.1,
 "seuil_calibrage_haut": 0.03,
 "sigma_cible": 1.0,
 "sigma_max": 1.5,
 "sigma_min": 0.5,
 "tau": 0.25,
 "taux_departs_non_finis_max": 0.05,
 "taux_nonconv_max": 0.1,
 "tol_fpr": 0.005,
 "unites_Bp": 9
}
```
<!-- configuration-canonique-fin -->

Réglages de R4 (inchangés de la course originale, vérifiés par le code à la décision) :

- LAMBDA_RETENU = 0.3
- REFERENCE_RETENUE = moyenne

Codes de graine des règles (inchangés) : R0 20, R1 21, R2 1, R3 2, R4 24 ; rangs à l'analyse : R0 0, R1 1, R2 2, R3 3, R4 4.

## Résumé pour Lazar

1. **Ce qu'on refait** : exactement la course du 1er novembre (même monde synthétique, mêmes cinq règles, même configuration au bit, même N, même code à la seule exception des racines), sur une **graine neuve que personne ne choisit** : elle est dérivée de l'empreinte de ce texte une fois scellé (règle D, § Plan 3). Le but est de montrer qu'aucun des deux constats présentés aux mentors ne tient à la graine de la course originale.
2. **Les deux constats testés** : (a) **« le mélange bat l'historique »** (HR1) : la défense qui tire au hasard, aux poids d'équilibre, parmi ses moniteurs passés détecte mieux, face à un attaquant qui répond en dernier, que le moniteur unique réentraîné sur toutes les attaques passées : +0,10 et +0,12 de détection à la course originale ; (b) **« ne rien faire fait aussi bien »** (réfutation de HR0) : le moniteur initial jamais réentraîné est équivalent, à 0,02 près, au moniteur réentraîné sur l'historique. En secondaire : la régularisation vers le passé ne nuit pas (HR3), et la défense figée détecte mieux les lois tenues à l'écart.
3. **Ce qui comptera comme réplication** : (a) un écart d'au moins **+0,05** aux deux budgets avec un intervalle B2 au-dessus de zéro ; (b) la même classe qu'à l'original, « équivalentes à 0,02 près » (ou en faveur de la défense figée), aux deux budgets. Probabilités calculées d'avance si la course originale dit vrai : ≈ 1 pour (a), ≈ 0,90 pour (b) (≈ 0,85 en tenant compte de l'incertitude de l'original).
4. **Garde-fous** : la statistique est recodée par un **autre agent qui ne voit pas le code**, d'après la spécification ; les deux calculs doivent concorder à 10⁻⁹ près, sinon arrêt. Un résultat **plus beau** que l'original déclenche le même audit qu'un résultat plus faible (règle de symétrie). Un contrôle vérifie que les graines sont bien neuves.
5. **Coût** : processeur seul, **0 USD**, ≈ 28 min de mur sur les 2 cœurs de cette machine (1 693 s à l'original), `timeout 3600`.
6. **Ce que la réplication ne dit pas** : rien sur la capacité déployée (le mélange déploie jusqu'à 9 moniteurs contre 1), rien sur un attaquant plus fort que l'attaquant local, rien sur d'autres budgets ou d'autres mondes (§ suivant). Ce sont les attaques suivantes d'un mentor ; elles demandent d'autres courses.
7. **À trancher par toi** : N (recommandation : 100, la même configuration au bit ; § Seuil S-N) et le GO de la course.

## Ce que l'expérience n'autorise pas

- **Rien au-delà de la robustesse à la graine.** Même monde (d = 6, K = 3, T = 8), mêmes deux budgets δ (1,4 ; 1,6) **choisis à l'origine sur la seule règle historique**, même oracle, même attaquant local, même λ* : une réplication réussie dit « ce n'est pas la graine », pas « c'est général ».
- **Capacité déployée** : R3 déploie un mélange aléatoire de jusqu'à 9 moniteurs linéaires (63 paramètres ; 7 par requête), R2 un seul (7). HR1 compare un mélange d'équilibre à un hyperplan pur ; qu'un mélange d'équilibre batte une stratégie pure face à un attaquant qui joue en dernier est attendu du théorème du minimax sans point-selle pur (le texte original appelle HR1 « plomberie »). Au pilote de l'arène v4 (non opposable), des combinaisons déterministes des mêmes moniteurs faisaient nettement mieux que le mélange. Aucune phrase « le mélange est la bonne façon d'employer plusieurs moniteurs » n'est autorisée.
- **Attaquant** : V est la meilleure de deux réponses du **même** optimiseur local ; contre un mélange, l'objectif de l'attaquant est plus multimodal et l'optimiseur local pourrait y être plus faible que contre un hyperplan, ce qui gonflerait HR1. L'attaquant indépendant de l'arène v4 n'est pas branché ici ; la sérialisation des défenses finales (§ Plan 2, changement C10) permet de l'appliquer ensuite **sans rejouer la course**, dans un préenregistrement séparé (recommandé).
- **HR0** : « ≈ » veut dire « pas d'avantage de plus de m = 0,02 » (≈ 17 % du niveau de V au δ 1,4, ≈ 30 % au δ 1,6), pas « aucune différence » ; la défense figée est M0 (entraîné contre la cible seule), pas le meilleur moniteur figé ; l'équivalence peut refléter un plancher de la classe linéaire dans ce monde (audit original, § 3).
- **Deux budgets, une seule famille de cibles** : les deux budgets partagent la loi cible de chaque instance (corrélation entre budgets du contraste R3 − R2 : 0,45 ; R0 − R2 : 0,20 à l'original) ; « aux deux budgets » n'est pas deux réplications indépendantes.
- Rien sur les vrais modèles ni sur des moniteurs d'activations réels. Aucune revendication d'antériorité ni de nouveauté (R8). Aucune porte, aucune dépense, aucune modification du programme.

## Hypothèse

Renvoi : préenregistrement scellé de la course originale (`d82dea33…`), hypothèses HR1, HR0, HR3 ; lecture (`24081eed…`) et audit (`7e81d094…`) ; verdicts finals consignés en R-976 (session-depot) : HR1 confirmée, HR0 réfutée, HR3 confirmée, HR2 non tranchée. Monde, règles, oracle, attaquant, mesures : ceux de la course originale, sans changement (§ Plan 1).

- **HRép1 (primaire) — « le mélange bat l'historique » tient sur graine neuve** : Δ(R3, R2) = moyenne sur les instances de V(R3) − V(R2) est d'au moins τ = **+0,05** à chaque budget, avec la borne basse de B2 strictement positive (signe et taille). Réfutation : signe inversé démontré (borne haute B2 < 0) ou effet démontré inférieur à 0,05 (borne haute B2 < 0,05) à un budget.
- **HRép0 (primaire) — « ne rien faire fait aussi bien » tient sur graine neuve** : à chaque budget, la classe de Δ(R0, R2) sur V par la Table B originale est « ≈ » (équivalentes à m = 0,02 près) ou en faveur de la défense figée (« R0 ≳ R2 », « R0 > R2 »). Réfutation : à un budget, le réentraînement l'emporte de façon démontrée (« R2 > R0 » ou « R2 ≳ R0 »).
- **HRép3 (secondaire) — « la régularisation ne nuit pas » tient** : à chaque budget, classe de Δ(R4, R2) sur V « R4 > R2 », « R4 ≳ R2 » ou « ≈ », dégénérescence S12 non déclenchée. Réfutation : « R2 > R4 » ou « R2 ≳ R4 » à un budget.
- **HRép-ii (secondaire) — la défense figée détecte mieux les lois tenues à l'écart** : Table C ligne 4 (borne basse B8 de Δ(R0, R2) sur (ii) > 0) aux deux budgets. Réfutation : régression démontrée (lignes 1 à 3) à un budget.
- **Descriptifs (recopiés, sans verdict de réplication)** : HR2 (« oublier coûte » : D̄(R1, R2) sur X̄, Table B′) — son verdict original « non tranchée » et sa fragilité à la parité de T (audit, § 5) rendent une réplication de verdict sans objet ; les autres classes des Tables B, B′, C, la Table D, R3′, le coût.
- **Hypothèses de travail** : le code v3 calcule exactement ce que calculait le code v2 (vérifié avant la course par un essai de non-régression au bit sur deux tâches de la course originale et par un essai de diff restreint, § Plan 2) ; l'implémentation B suit la spécification (vérifié sur la course originale, écart ≤ 10⁻⁹) ; la variabilité de la réplication est celle d'un rééchantillonnage de la course originale (base du calcul de puissance).

## Prédiction chiffrée et signe attendu

Les prédictions sont, **par construction**, tirées de la course originale (c'est l'objet d'une réplication) ; les probabilités viennent d'un calcul de puissance déclaré (§ Seuil S-N). Confiance = probabilité subjective arrondie.

| # | Contraste | Budget | Signe | Classe ou issue prédite | Ordre de grandeur | Confiance | Ce qui réfute |
|---|---|---|---|---|---|---|---|
| PR1 | Δ(R3, R2) sur V (HRép1) | 1,4 ; 1,6 | + | « répliquée » (est ≥ 0,05 ∧ bas(B2) > 0 aux deux) | +0,09 à +0,13 (original +0,1045 ; +0,1236) | 0,95 | haut(B2) < 0 ou haut(B2) < 0,05 à un budget |
| PR0 | Δ(R0, R2) sur V (HRép0) | 1,4 ; 1,6 | ≈ 0 | « ≈ » aux deux budgets (ou en faveur de R0) | entre −0,009 et +0,012 (original +0,0024 ; +0,0037) | 0,85 | « R2 > R0 » ou « R2 ≳ R0 » à un budget |
| PR3 | Δ(R4, R2) sur V (HRép3) | 1,4 ; 1,6 | ≥ 0 | « R4 ≳ R2 » ou « ≈ » ; S12 non déclenché | 0 à +0,03 (original +0,0202 ; +0,0142) | 0,9 | « R2 > R4 » ou « R2 ≳ R4 » à un budget |
| PRii | Δ(R0, R2) sur (ii) | 1,4 ; 1,6 | + | Table C ligne 4 aux deux | +0,03 à +0,08 (original +0,0516 ; +0,0600) | 0,9 | lignes 1 à 3 à un budget |
| PRz | écarts de réplication z_π des quatre contrastes primaires | — | — | aucun \|z_π\| > 2,4977 (TR1 non déclenché) | \|z_π\| ≈ 0 à 2 | 0,9 | TR1 déclenché (audit, pas une réfutation) |
| PRs | contrôles de santé T2 à T6 | 1,4 ; 1,6 | — | aucun déclenché ; fausses alertes à α ± 0,001 | comme l'original | 0,95 | un contrôle déclenché (non jugeable) |
| PR2 | D̄(R1, R2) sur X̄ (descriptif) | 1,4 ; 1,6 | + | recopiée | +0,01 à +0,03 | 0,8 (signe) | — (aucun verdict) |

**Déclaré.** (1) Les consignes de la tâche proposaient « HR1 : écart ≥ +0,05 avec intervalle à 95 % excluant 0 » et « HR0 : intervalle de l'écart fixe − réentraînée contenant 0 ou en faveur de la fixe ». Ce brouillon garde le seuil de taille +0,05 (qui est aussi l'ordre de grandeur de P1 dans le texte original) mais prend l'intervalle **B2** de l'original (98,75 % bilatéral, plus strict que 95 %) pour la comparabilité ; pour HR0, « intervalle contenant 0 » seul ferait passer une réplication imprécise pour une réussite (absence de preuve), alors que l'original a conclu par **équivalence** (E8 dans ]−0,02 ; +0,02[) : la réplication exige la même classe ; la classe « ? » (imprécise) donne « non jugeable ». (2) L'auteur a vu tous les résultats de la course originale (résultats bruts, analyse, lecture, audit) ; aucune racine de la réplication n'existe encore (elle dépend de l'empreinte finale de ce texte) ; aucune exécution du jeu n'a été faite pour ce brouillon. (3) Les probabilités de PR1 et PR0 viennent d'un rééchantillonnage des 100 instances originales (§ Seuil S-N), non d'une course.

## Métrique

Celles de la course originale (texte scellé `d82dea33…`, § Métrique), sans changement ; définitions mathématiques complètes dans la spécification (§ 1 à 5) :
- **V** = détection finale de la défense figée après T = 8 tours, la plus basse des réponses standard et renforcée de l'attaquant, sur 19 998 échantillons frais ; **(ii)** = détection moyenne sur 50 lois tenues à l'écart ; **X̄** = moyenne sur les tours de 1 − (iii)_t.
- **Contraste apparié** à budget fixé : est = moyenne sur les 100 instances (triées par instance) de la différence « variante − R2 » ; écart-type de l'échantillon (dénominateur n − 1).
- **Intervalles** : rééchantillonnage apparié des instances, B = 20 000 tirages, générateur `SeedSequence(entropy=ρ, spawn_key=(code_budget, 200 + 100 × code_mesure + rang, 0, 0, 99))` avec ρ la racine principale de la règle D, quantiles linéaires (type 7) aux dix niveaux 0,3125 % … 99,6875 % ; B2 = [q0,00625 ; q0,99375] ; B8 = [q0,003125 ; q0,996875] ; E8 = [q0,00625 ; q0,99375] (spécification § 2, § 5).
- **Écart de réplication** (neuf) : pour chacun des quatre contrastes primaires π (R3 − R2 et R0 − R2 sur V, deux budgets), g_π = est_réplication − est_original, σ_π = √(s_rép²/100 + s_orig²/100), z_π = g_π / σ_π ; est_orig et s_orig lus dans l'analyse originale `18b80112…` (spécification § 10.2).
- **Graines neuves** (neuf) : pour chaque variante, nombre de tâches où V de la réplication est égal au bit à V de l'original à la même tâche (spécification § 10.3).

## Seuil

Tous les seuils de la course originale sont **repris sans changement** (S1 m = 0,02 ; S5 = 0,02 ; S9 α = 0,01, garde ± 0,005, déclencheur 0,001 ; S10 trop beau / trop mauvais ; S12 = 0,999 sur plus de la moitié des tâches ; bornes B2, B8, E8). Les bornes de l'original sont gardées **telles quelles**, sans recalcul de la multiplicité pour la famille plus petite de la réplication (conservateur ; déclaré). Réserve héritée : B2 a les quantiles d'un Bonferroni à quatre tests (commentaire de l'arène v4, l. 159–161), plus large que nécessaire pour deux budgets.

**Seuils neufs** :
- **τ = 0,05** — taille minimale de Δ(R3, R2) pour « HR1 répliquée » ; posé par principe à environ la moitié de l'effet original (+0,10 ; +0,12) et égal à l'ordre de grandeur de P1 dans le texte original.
- **z* = 2,497705474412374** (quantile 0,99375 de la loi normale) — déclencheur TR1 : Bonferroni à 5 % bilatéral sur les quatre contrastes primaires.
- **0,001** — déclencheur TR2 « trop propre » (les quatre |g_π| sous 0,001 ; probabilité ≈ 2,5 × 10⁻⁴ avec des graines indépendantes).
- **10 tâches sur 200** (5 %) — arrêt « graines non neuves » (attendu ≈ 0,07 tâche par variante par hasard : V est un multiple de 1/19 998 d'écart-type ≈ 0,06 entre tâches).
- **ε = 10⁻⁹** — concordance des implémentations A et B (spécification § 11).
- **S8 : `timeout 3600`** (deux fois la durée observée), 2 processus, 600 s de processeur par tâche (garde interne inchangée).

**S-N — nombre d'instances par budget** — Valeur : **À REMPLIR (décision de Lazar ; recommandation : N = 100)**.
- Décision : combien d'instances par budget pour la réplication.
- Enjeu : la puissance de HRép0 (la classe « ≈ » de l'original est à 1,5 à 1,7 erreur-type de sa frontière) contre l'identité de configuration avec l'original.
- Option (a) **N = 100** : configuration identique au bit à l'original (`3fbb27fc…`), réplication directe, ≈ 28 min ; P(HRép1 répliquée) ≈ 1,00 ; P(HRép0 répliquée) ≈ 0,90 si l'original dit vrai (≈ 0,85 en comptant l'incertitude de l'original), « non jugeable » ≈ 0,10. Inconvénient : une chance sur dix que HR0 reste imprécise.
- Option (b) **N = 200** : P(HRép0 répliquée) ≈ 0,999 (approximation normale), ≈ 57 min ; inconvénient : le champ `n_instances` change, donc l'empreinte de configuration ; ce n'est plus la course originale au bit (seulement à la taille près) ; instances 0 à 199.
- **Recommandation : (a), confiance 0,6** — l'argument présenté aux mentors est « même course, au bit près, seule la graine change » ; la limite de puissance de HR0 est celle de la course originale elle-même et sera déclarée. Défaut sous 48 heures : (a) ; mais la course de cette nuit exige le mot de Lazar (GO), qui peut porter les deux.

**Calcul de puissance (déclaré)** — rééchantillonnage, 20 000 fois, de 100 instances parmi les 100 de la course originale (les mêmes instances aux deux budgets, pour garder la corrélation entre budgets), différences par tâche décalées selon le scénario, bornes par approximation normale (z = 2,4977 pour B2 et E8, 2,7344 pour B8) ; graine de calcul sans lien avec la course (`SeedSequence(314159, (1,))`) ; script de l'auteur dans son dossier temporaire, non versé.

| Scénario (vérité supposée) | HRép1 répliquée | HRép1 non jugeable | HRép0 répliquée | HRép0 non jugeable | HRép0 non répliquée | HRép3 répliquée |
|---|---|---|---|---|---|---|
| celle de la course originale | 1,000 | 0,000 | 0,903 | 0,096 | 0,000 | 1,000 |
| effet de HR1 réduit de moitié (+0,052 ; +0,062) | 0,655 | 0,342 | — | — | — | — |
| effet de HR1 = +0,06 aux deux budgets | 0,955 | 0,045 | — | — | — | — |
| vrai Δ(R0, R2) = −0,01 (le réentraînement aide un peu) | — | — | 0,317 | 0,147 | 0,535 | — |
| vrai Δ(R0, R2) = −0,02 (= −m) | — | — | 0,000 | 0,000 | 0,999 | — |

## Plan d'analyse

### 1. Monde, règles, mesures
Ceux de la course originale, inchangés : configuration `3fbb27fc…` (si N = 100), cinq variantes R0 (défense figée), R1 (dernière attaque), R2 (historique), R3 (mélange d'équilibre), R4 (régularisation, λ* = 0,3, référence « moyenne ») ; T = 8 ; δ = (1,4 ; 1,6) ; oracle « détection » ; finale « légère » de l'arène v4 plus (ii) finale et (i) sur les attaques vues ; codes de graine 20, 21, 1, 2, 24.

### 2. Code v3 (à écrire par un sous-agent neuf ; liste fermée de changements par rapport à v2 `9f0dcf5e…`)
Fichier `docs/notes/convergence-defense-v1/regles-defense-v1/arene_regles_defense_v3.py`, copie de v2, **avec ces seuls changements** :
- **C1** en-tête : ce qui change et pourquoi (texte) ;
- **C2** `VERSION = "arene_regles_defense_v3"` ; `IDENTIFIANT_PREREG = "PREREG-REPLICATION-REGLES-DEFENSE-V1"` ;
- **C3** chemin de l'arène v4 = la copie suivie par git (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/arene_melange_v4.py`), empreinte épinglée inchangée `70c77fd5…` (comportement identique : les fonctions employées ne dépendent pas de l'emplacement du fichier) ;
- **C4** racines : fonction neuve de dérivation par la règle D (spécification § 4) ; les racines dérivées remplacent les racines de décision ; 20266201 et 20266202 rejoignent les racines employées (refusées) ; gardes de la règle D ;
- **C5** `exiger_racine_permise_regles` : une racine dérivée exige l'autorisation par le texte scellé (comme une racine de décision en v2) ;
- **C6** `exiger_identite_prereg_regles` : identifiant neuf ; exige la ligne « RACINES_REPLICATION = règle D » à la place de « RACINE_DECISION = … » ; exige aussi l'empreinte du code v2 ;
- **C7** `autoriser_decision_regles` : dérive et pose les racines après `exiger_prereg_scelle` ;
- **C8** `_travail` : dans chaque processus de travail, l'autorisation dérive les racines du même texte et vérifie leur égalité avec celles de la tâche ;
- **C9** `main`, mode `decision` : vérification du gel v2 par son empreinte seule (il ne peut pas citer des racines dérivées d'un texte postérieur ; la règle est dans ce texte scellé) ; manifeste : racines (entiers et chaînes), « règle D », empreinte du code v2 ; course et analyse sur les racines dérivées (`analyser_regles(res, ρ)`) ;
- **C10** sérialisation, **sortie seulement** : pour chaque variante, la défense finale (pour chaque moniteur : W, b, seuil t, échelle e, poids), les attaques de la trajectoire et les deux attaques finales (par l'option `rendre_attaques` de `phase_finale`, qui ne change aucun calcul) ; la loi cible par tâche ;
- **C11** `bloc_identite` : identifiant, ligne de la règle D, empreinte du code v2 ; **C12** `__all__` ;
- **rien d'autre** : règles, oracle, attaquant, lois tenues, finale, `analyser_regles`, `_boot`, `MESURES_CONTRASTE`, compteurs, gardes, mode `essai` et ses racines d'essai v2 (employées par des essais seulement) restent identiques.

Essais `test_arene_regles_defense_v3.py` : les 25 essais de v2 adaptés, plus **E1** règle D (les trois vecteurs d'essai de la spécification § 4 ; gardes saines et artefacts : racines égales, racine dans l'ensemble interdit, racine égale à un vecteur d'essai) ; **E2** 20266201 et 20266202 refusées ; **E3** identité v3 (sain ; artefacts : identifiant v2, ligne de la règle D absente, empreinte du code v2 absente) ; **E4** décision refusée sans texte scellé ; **E5** diff restreint : par l'arbre syntaxique, chaque fonction et classe de niveau module de v2 et v3 est identique, sauf celles des changements C1 à C12 ; **E6 (lent)** non-régression au bit : v3 rejoue les tâches (δ 1,4 ; instances 0 et 1) de la course originale sur ses racines d'origine (autorisation posée par l'essai seulement ; aucune information neuve : résultats déjà scellés et lus) et rend au bit, pour les cinq variantes, `V_iii_final`, `V_iii_standard`, `V_iii_renforce`, `exploitabilite_moyenne_tours`, `ii_final`, `fpr_final`, `par_tour.iii`, `par_tour.ii`, `poids_finaux` de `resultats-regles-defense.json` (`d07ece47…`) ; **E7** la sérialisation ne change aucune valeur (une tâche, petite configuration, avec et sans).

### 3. Graines (R9) — règle D
(ρ, ρ_t) = les deux premiers mots de 64 bits de `numpy.random.SeedSequence(entropy=int(H, 16))`, H = empreinte SHA-256 de ce texte scellé (spécification § 4 ; vecteurs d'essai : l'empreinte du texte original `d82dea33…` donne (11786724493248295725, 9136419304016434890), jamais employés). ρ est la racine principale (jeu et rééchantillonnage), ρ_t celle des lois tenues à l'écart. Toute modification du texte change H, donc les racines : **un texte modifié est une course nouvelle** (R12). Aucun tirage n'est fait sur une racine dérivée d'un texte non scellé ; le code refuse de dériver d'un texte non scellé ; personne n'applique la règle D à un brouillon (seuls les trois vecteurs d'essai de la spécification sont calculés à la main) ; une seule version scellée de ce texte sera lancée, et toute autre version scellée est consignée avec son empreinte, ce qui rend visible toute tentative de choisir la graine en rescellant. Schéma de dérivation des tirages inchangé : `SeedSequence(entropy=ρ, spawn_key=(code_budget, instance, code_règle, tour, rôle, …))`.

### 4. Implémentation indépendante B
Écrite par un agent neuf qui ne voit **ni** le code v2, **ni** le code v3, **ni** l'arène, à partir de la seule spécification ; validée sur la course originale (spécification § 12 : écart ≤ 10⁻⁹ sur les 16 contrastes × 2 budgets, classes et verdicts originaux retrouvés, gardes de réplication déclenchées sur la course contre elle-même) ; rapport de validation et code **scellés avant la création du manifeste** de la course ; plus modifiés ensuite.

### 5. Ordre d'exécution, commandes, durée (2 cœurs de cette machine)
0. **Préparation** (dans `/home/claude/controle-ia-travail`, aucune ref `donnees/*`, aucun `git fetch` sans refspec) : rapatrier depuis la branche déjà récupérée `origin/canal/session-depot-reprise-n67` les fichiers absents de cet arbre : `docs/notes/convergence-defense-v1/`, `prereg/preregistrement-regles-defense-convergence-v1.md` et son compagnon, `diag/20261101-160323-regles-defense-convergence/`, `runs/20261101-160323-regles-defense-convergence/` (par exemple `git checkout origin/canal/session-depot-reprise-n67 -- <ces chemins>`) ; vérifier leurs empreintes (`PYTHONPATH=src .venv/bin/python -m controle_ia.scellement verifier <fichiers>`).
1. **Essais du code v3** (≈ 1 min, dont ≈ 35 s de processeur pour E6) :
   `cd /home/claude/controle-ia-travail/docs/notes/convergence-defense-v1/regles-defense-v1 && PYTHONPATH=/home/claude/controle-ia-travail/src OMP_NUM_THREADS=1 REGLES_ESSAIS_LENTS=1 /home/claude/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider test_arene_regles_defense_v3.py` ; journal et empreinte consignés.
2. **Bloc d'identité** : `… /home/claude/controle-ia-travail/.venv/bin/python -B arene_regles_defense_v3.py identite`, recopié tel quel dans ce texte.
3. **Implémentation B** écrite, validée, scellée (§ 4).
4. **Contre-lecture** (R2) puis **scellement** de ce texte sous `prereg/preregistrement-replication-regles-defense-convergence-v1.md` (`controle_ia.prereg.sceller_prereg`) ; commit (le manifeste exige un arbre propre) ; **GO de Lazar** consigné ; charge relevée par `uptime` et consignée ; aucune autre charge lourde sur la machine.
5. **La course — une seule invocation** (≈ 28 min de mur ; 1 692,7 s à l'original ; plafond 60 min) :
   `cd /home/claude/controle-ia-travail && PYTHONPATH=src OMP_NUM_THREADS=1 timeout 3600 .venv/bin/python -B docs/notes/convergence-defense-v1/regles-defense-v1/arene_regles_defense_v3.py decision --prereg prereg/preregistrement-replication-regles-defense-convergence-v1.md --instances 0:100 --run-id "$(date -u +%Y%m%d-%H%M%S)-replication-regles-defense" --lambda 0.3 --reference moyenne --processus 2`
   Sorties scellées : `runs/<run-id>/manifeste.json`, `runs/<run-id>/pids-travail.txt`, `diag/<run-id>/resultats-regles-defense.json`, `diag/<run-id>/analyse-regles-defense.json` (implémentation A).
6. **Implémentation B** sur la course (secondes) puis **comparaison A/B** (spécification § 11) ; discordance → arrêt.
7. **Lecture** par un sous-agent neuf (R13) : critères gelés ci-dessous ; audit si un déclencheur l'exige ; verdict scellé ; soumis à Lazar.

### 6. Comparaisons et multiplicité
Deux primaires (HRép1, HRép0), chacune aux deux budgets (intersection : « répliquée » exige les deux budgets) ; deux secondaires (HRép3, HRép-ii), lues à part, sans effet sur l'issue globale ; descriptifs recopiés. Bornes de l'original gardées (B2 pour HRép1 ; B8 et E8 pour HRép0, HRép3 ; B8 pour HRép-ii). Déclencheur d'écart de réplication corrigé par Bonferroni sur les quatre contrastes primaires.

### 7. Reprise après arrêt
Arrêt externe (`timeout`, signal) : arrêt par PID des processus consignés (R10), `orphelins --pids runs/<run-id>/pids-travail.txt` sain, puis **une** reprise complète : même code, même texte scellé (donc mêmes racines), nouvel identifiant de run ; seconde interruption → « non jugeable (plomberie) ». Arrêt par garde interne → « non jugeable », version nouvelle (nouveau texte, nouvelles racines). Aucun point de reprise partiel.

### 8. Historique de conception (déclaré)
1. Demande de conv-audit (1er novembre 2026, R-1075 : « go » de Lazar sur le dossier de preuves pour les mentors), premier sous-agent coupé par une panne de crédits (R-1076), relance. 2. Lecture des pièces de la branche n67 (préenregistrement scellé, code v2 lu en entier, lecture, audit, gel v2, formalisation, LISEZMOI v1 et v2, lecture vérifiée de l'avis d'Argon seul) et de la copie suivie de l'arène v4 pour les parties des racines, des quantiles, de l'attaquant, du contexte et de la finale ; rien sous `donnees/`. 3. Recodification de la statistique depuis la spécification écrite, sans importer le code : écart 0,0 avec l'analyse scellée, classes et verdicts originaux retrouvés. 4. Calcul de puissance par rééchantillonnage des instances originales. 5. Ce brouillon 1. Aucune exécution du jeu, aucune racine de réplication dérivée.

## Critères de lecture gelés

Un sous-agent neuf (R13) applique ces règles telles qu'écrites, dans l'ordre ; la première ligne vraie décide. Notations et définitions : spécification § 2, § 5, § 7, § 8, § 10 (copiées ici) ; « budget » = δ 1,4 (code 1) ou δ 1,6 (code 2).

**V0 de la réplication** = (a) aucune condition de la liste d'arrêt ; (b) 200 tâches, instances 0 à 99 à chaque budget, sans doublon, cinq variantes aux noms exacts ; (c) racines du manifeste et de chacune des 200 tâches = règle D appliquée à l'empreinte de ce texte scellé (recalculée par le lecteur et par B), différentes de 20266201 et 20266202 ; (d) empreintes du code v3, de l'arène v4, du gel v2, de la configuration et de la bibliothèque = celles du bloc d'identité, versions conformes ; (e) λ = 0,3 et référence « moyenne » (commande, manifeste, chaque tâche) ; (f) une seule invocation ayant écrit des résultats (au plus une reprise complète consignée) ; (g) essais du code v3 passés avant la course, dont E5 et E6 (journal consigné) ; (h) implémentation B scellée avant la création du manifeste et validée sur la course originale ; (i) concordance A/B (spécification § 11) ; (j) contrôle « graines neuves » passé (aucune variante avec plus de 10 tâches égales au bit à l'original).

**Contrôles de santé** (spécification § 7, seuils de l'original) : T2 trop beau / trop mauvais ; T3 mélange dégénéré (bloque HRép1) ; T4 dégénérescence de R4, S12 (bloque HRép3 seulement) ; T5 optimiseur ; T6 dérive des fausses alertes. T2, T5, T6 bloquent toutes les lectures.

### Table R1 — HRép1, « le mélange bat l'historique » tient-il ? (Δ(R3, R2) sur V, bornes B2, par budget c : est_c, bas_c, haut_c)

| # | Condition | Verdict brut |
|---|---|---|
| 0 | V0 fausse | **non jugeable (plomberie)** ; aucune lecture |
| 1 | T2, T3, T5 ou T6 déclenché | **non jugeable (santé)** |
| 2 | il existe un budget où la moyenne de V ≤ 2α pour chacune des cinq variantes | **non jugeable (jeu dégénéré)** |
| 3 | aux deux budgets : est_c ≥ 0,05 ∧ bas_c > 0 | **répliquée** |
| 4 | à au moins un budget : haut_c < 0 | **non répliquée (signe inversé)** |
| 5 | à au moins un budget : haut_c < 0,05 | **non répliquée (effet démontré inférieur à 0,05)** |
| 6 | sinon | **non jugeable (imprécis)** |

### Table R0 — HRép0, « ne rien faire fait aussi bien » tient-il ? (classe κ_c de Δ(R0, R2) sur V par la Table B originale, B8 et E8, m = 0,02)

Table B originale (première condition vraie) : bas(B8) > m → « R0 > R2 » ; haut(B8) < −m → « R2 > R0 » ; bas(E8) > −m ∧ haut(E8) < m → « ≈ » ; bas(B8) > 0 → « R0 ≳ R2 » ; haut(B8) < 0 → « R2 ≳ R0 » ; sinon « ? ».

| # | Condition | Verdict brut |
|---|---|---|
| 0 | V0 fausse | **non jugeable (plomberie)** |
| 1 | T2, T5 ou T6 déclenché | **non jugeable (santé)** |
| 2 | à au moins un budget : κ_c = « R2 > R0 » | **non répliquée (le réentraînement l'emporte d'un effet d'intérêt)** |
| 3 | à au moins un budget : κ_c = « R2 ≳ R0 » | **non répliquée (le réentraînement l'emporte, effet démontré non nul)** |
| 4 | aux deux budgets : κ_c ∈ {« ≈ », « R0 ≳ R2 », « R0 > R2 »} | **répliquée** |
| 5 | sinon (« ? » à un budget) | **non jugeable (imprécis)** |

### Table R3 — HRép3, secondaire (classe κ′_c de Δ(R4, R2) sur V par la Table B)

| # | Condition | Verdict brut |
|---|---|---|
| 0 | V0 fausse | non jugeable (plomberie) |
| 1 | T2, T5 ou T6 | non jugeable (santé) |
| 2 | T4 (S12) à au moins un budget | sans verdict (R4 ≈ défense figée), classe de R0 recopiée à côté |
| 3 | à au moins un budget : κ′_c ∈ {« R2 > R4 », « R2 ≳ R4 »} | non répliquée |
| 4 | aux deux budgets : κ′_c ∈ {« R4 > R2 », « R4 ≳ R2 », « ≈ »} | répliquée |
| 5 | sinon | non jugeable (imprécis) |

### Table Rii — HRép-ii, secondaire (ligne ℓ_c de la Table C originale pour Δ(R0, R2) sur (ii), bornes B8, S5 = 0,02)

Table C originale : 1 haut < −S5 ; 2 haut < 0 ∧ bas > −S5 ; 3 haut < 0 ; 4 bas > 0 ; 5 bas > −S5 ; 6 sinon.

| # | Condition | Verdict brut |
|---|---|---|
| 0 | V0 fausse | non jugeable (plomberie) |
| 1 | T2, T5 ou T6 | non jugeable (santé) |
| 2 | aux deux budgets : ℓ_c = 4 | répliquée |
| 3 | à au moins un budget : ℓ_c ∈ {1, 2, 3} | non répliquée (signe inversé) |
| 4 | sinon | non jugeable (imprécis) |

### Déclencheurs d'audit (R4), symétriques — un seul suffit

- **TR1 — écart de réplication, dans les deux sens** : |z_π| > z* = 2,497705474412374 pour au moins un des quatre contrastes primaires. **Un résultat plus beau que l'original (écart vers le haut pour R3 − R2, ou vers la défense figée pour R0 − R2) déclenche exactement comme un résultat plus faible.**
- **TR2 — trop propre** : |g_π| < 0,001 pour les quatre contrastes primaires.
- **TR3 — défense figée plus belle que l'original** : κ_c ∈ {« R0 > R2 », « R0 ≳ R2 »} à au moins un budget (l'original rendait « ≈ » aux deux).
- **TR4 — non-réplication** : verdict brut de HRép1 ou de HRép0 « non répliquée (…) ».

**Effet** : tant que le rapport d'audit n'est pas scellé, les verdicts de HRép1, HRép0, HRép3 et HRép-ii sont « non jugeable (audit en attente) ». Rapport « pas d'artefact » → verdicts bruts rétablis, avec la mention « après audit » ; « artefact trouvé » → « non jugeable (artefact) », version nouvelle.

**Contenu de l'audit** (sous-agent neuf, ni auteur de ce texte, ni du code v3, ni de B, ni lecteur) : (1) recalculer la règle D sur l'empreinte du texte scellé et la comparer aux racines du manifeste et des 200 tâches ; (2) recompter les égalités au bit avec la course originale pour V, X̄ et (ii), toutes variantes ; (3) rejouer E5 (diff restreint) et E6 (non-régression au bit) ; (4) rejouer deux tâches de la réplication (δ 1,4 ; instances 0 et 1) dans un processus neuf et vérifier l'égalité au bit avec le fichier de résultats ; (5) pour HR0 : relecture du code de R0 et du compteur d'entraînements (zéro entraînement, M0 déployé) ; pour HR1 : poids de R3 issus du programme linéaire, part pure, support ; (6) recalculer A et B. **Issue** : « artefact trouvé » si erreur de code, chemin non exercé, graines non neuves ou discordance ; sinon « pas d'artefact ». Option, hors verdict : attaquant indépendant de l'arène v4 sur les défenses finales sérialisées (C10), dans un préenregistrement séparé.

### Issue globale (première ligne vraie)

| # | Condition | Issue |
|---|---|---|
| 1 | V0 fausse, condition d'arrêt, ou discordance A/B | **non jugeable (plomberie)** |
| 2 | HRép1 ou HRép0 « non jugeable (audit en attente) » | **en attente d'audit** |
| 3 | HRép1 ou HRép0 « non jugeable (artefact) » | **non jugeable (artefact)** |
| 4 | HRép1 « non répliquée (…) » | **échec de réplication du résultat positif** |
| 5 | HRép1 « répliquée » ∧ HRép0 « répliquée » | **réplication réussie** |
| 6 | HRép1 « répliquée » ∧ HRép0 « non répliquée (…) » | **réplication partielle : le mélange tient, l'équivalence de la défense figée ne tient pas** |
| 7 | HRép1 « répliquée » ∧ HRép0 « non jugeable (…) » | **réplication partielle : le mélange tient, l'équivalence de la défense figée reste imprécise** |
| 8 | sinon | **non jugeable** |

### Issues écrites d'avance (phrases à reprendre telles quelles, chiffres remplis par le lecteur)

- **Réplication réussie** : « Sur une graine neuve que personne n'a choisie — dérivée de l'empreinte du texte scellé —, le mélange d'équilibre reste plus détecteur que la défense réentraînée sur l'historique (+a et +b, B2 [ … ]) et ne rien faire reste équivalent à réentraîner sur l'historique à 0,02 près (classes … ) ; la statistique, recodée par un agent qui n'a pas vu le code, concorde à 10⁻⁹. Les deux constats de la course du 1er novembre ne tiennent pas à sa graine. Portée inchangée : monde synthétique de l'arène v4, deux budgets, huit tours, attaquant local ; la capacité déployée et la force de l'attaquant restent à tester. »
- **Réplication partielle, équivalence non tenue** : « Le mélange d'équilibre bat toujours l'historique (+a, +b) ; en revanche, sur cette graine, réentraîner sur l'historique fait mieux que ne rien faire (classe … , est … ) : la phrase « ne rien faire fait aussi bien » ne sera plus présentée ; on rapporte les deux courses et leur écart. »
- **Réplication partielle, équivalence imprécise** : « Le mélange d'équilibre bat toujours l'historique ; la seconde course ne tranche pas l'équivalence de la défense figée (classe « ? » au budget … ) : cette phrase reste celle d'une seule course, avec sa marge de 0,02. »
- **Échec de réplication du résultat positif** (après un audit « pas d'artefact ») : « Sur une graine neuve, l'avantage du mélange d'équilibre ne se retrouve pas à la taille de 0,05 (ou s'inverse) : le seul résultat positif du programme ne tient pas à la réplication ; il n'est pas présenté comme acquis ; l'écart entre les deux courses devient l'objet d'une enquête. »
- **En attente d'audit** : « La réplication a déclenché l'audit de symétrie (motif : … ) ; aucune phrase sur la réplication avant le rapport scellé. »
- **Non jugeable (plomberie, santé, artefact)** : « La réplication n'a pas pu être lue (motif : … ) ; aucune phrase sur la réplication ; reprise selon la liste d'arrêt. »
- Secondaires, à ajouter après la phrase principale : « La régularisation vers le passé ne nuit toujours pas (classes … ) / ne tient pas (… ) » ; « La défense figée détecte toujours mieux les lois tenues à l'écart (+…, +…) / ne le fait plus (… ) ».

**Phrase de synthèse** (lecteur R13, sans rien omettre) : « Réplication de la course de convergence sur racines dérivées (règle D, ρ = …, ρ_t = …) : V0 … ; santé : T2 … T6 … ; HRép1 : Δ(R3, R2) +… [B2 … ; … ] et +… [ … ] → … ; HRép0 : Δ(R0, R2) +… [B8 …] [E8 …], classe … et … → … ; écarts de réplication z : … ; déclencheurs TR1 à TR4 : … ; audit : … ; HRép3 : … ; HRép-ii : … ; HR2 (descriptif) : … ; concordance A/B : écart maximal … ; graines neuves : comptes … ; issue globale : … ; portée : robustesse à la graine seulement. »

## Liste d'arrêt

| Condition | Action | Garde ou essai |
|---|---|---|
| Lancement sans texte scellé, conforme, identifié (identifiant v3, ligne de la règle D, empreintes du code v3 et v2, de l'arène v4, du gel v2, de la configuration, de la bibliothèque, versions, N, λ*, référence) | pas de départ ; aucune racine dérivée | `autoriser_decision_regles`, `exiger_identite_prereg_regles` ; E3, E4 |
| Racines dérivées égales entre elles, dans l'ensemble interdit, ou égales à un vecteur d'essai | arrêt, aucun repli | règle D ; E1 |
| Racines 20266201 ou 20266202 demandées hors de l'essai E6 | arrêt | `exiger_racine_permise_regles` ; E2 |
| Arène v4 absente ou d'empreinte ≠ `70c77fd5…` ; gel v2 ≠ `9977d7df…` | pas de chargement / arrêt | `charger_arene_v4`, `exiger_gel_regles` |
| Code v3 ≠ empreinte du bloc ; différence avec v2 hors de C1 à C12 ; essai E6 non passé | pas de départ | E5, E6 |
| Implémentation B non scellée avant le manifeste, ou non validée sur la course originale | pas de lecture | V0 (h) |
| Arbre git non propre ; fichier de sortie existant | pas de départ (R12) | `creer_manifeste`, `_exiger_absent` |
| Gardes de l'arène et du code v2, inchangées : processeur d'une tâche > 600 s ; fausses alertes d'une défense finale hors α ± 0,005 ; entraînements non convergés > 0,10 par tâche ; départs non finis > 5 % ; moniteur du tour 0 non reproductible ; programme linéaire non résolu ; loi inadmissible ; moniteur non fini ; R0 modifié | arrêt | gardes et essais repris de v2 |
| `timeout 3600` atteint ou signal | arrêt par PID (R10), `orphelins` sain, une reprise complète au plus | `_lancer`, `arreter_par_pid`, `exiger_aucun_orphelin` |
| Graines non neuves : plus de 10 tâches égales au bit à l'original pour une variante | arrêt ; « non jugeable (artefact) » | spécification § 10.3 |
| Discordance A/B > 10⁻⁹ sur un contraste décisif ou secondaire, ou classe différente hors frontière numérique | arrêt ; aucune lecture ; diagnostic par un sous-agent neuf ; toute correction après lecture = écart au préenregistrement (nœud de Lazar) | spécification § 11 |
| Lecture d'un résultat de la réplication avant scellement de ce texte et de B | arrêt et consignation (R1) | — |
| Modification de ce texte après scellement | interdite (R12) ; nouveau texte = nouvelles racines = nouvelle course | règle D |
| Appel de modèle, réseau, dépense | arrêt (devis et GO exigés) | — |
| `git fetch` sans refspec explicite ; lecture d'une ref `donnees/*` | interdit (quarantaine) | — |
| Marqueur de gabarit restant ; contre-lecture sans ses deux empreintes | pas de scellement | `controle_ia.prereg.problemes` |

## Rôles

- Auteur du brouillon 1, de l'état des lieux et de la spécification : sous-agent neuf (Claude Opus 5.5).
- Code v3 et essais : sous-agent neuf, qui n'écrit pas B.
- Implémentation B : agent neuf, qui ne voit que la spécification (et les formats de fichiers qu'elle décrit), ni v2, ni v3, ni l'arène.
- Contre-lecture (R2) : sous-agent neuf ; fichiers à lui donner : ce brouillon, `specification-statistique-decisive-v1.md`, `etat-des-lieux-v1.md`, le préenregistrement original scellé, la lecture et l'audit originaux, `arene_regles_defense_v2.py`, `arene_regles_defense_v3.py` et ses essais, `gel-regles-defense-v2.md`, la copie suivie de `arene_melange_v4.py`. Points à juger en priorité : que la règle D est bien imprévisible pour l'auteur et non réessayable ; que le diff C1 à C12 ne touche à aucun calcul ; que les Tables R1 et R0 lisent bien « réplique » au sens de l'original (et pas plus faible) ; que la symétrie des déclencheurs est réelle ; que la spécification suffit à recoder la statistique sans le code.
- Lecteur R13 : sous-agent neuf ; applique les tables ; verdict scellé, soumis à Lazar.
- Auditeur (si un déclencheur l'exige) : sous-agent neuf.
- Lazar : décision S-N ; GO de la course (processeur, 0 USD, ≈ 28 min).

## Contre-lecture

À REMPLIR — sous-agent neuf (identifiant), empreinte du brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque (accepté, refusé et pourquoi).
