# Préenregistrement — arène coévolutive synthétique : le mélange d'équilibre contre ses témoins à capacité égale — v1 — BROUILLON 2 (non scellé)

Identifiant : **PREREG-ARENE-MELANGE-EQUILIBRE-V1**. Tâche : piste 3 du brainstorm P-041 (décision de Lazar R-695, « gooo », 31 octobre 2026, `registres/decisions.md` ligne R-695), test (b), sur processeur ; brouillon 2 écrit après la contre-lecture du brouillon 1 (R-697). Pilote de **mécanisme** : aucun modèle de langage, aucun texte, aucune entrée de modèle. « L'attaquant » est un choix de paramètres dans une famille bornée de lois synthétiques.

- Auteur : sous-agent neuf Opus 5.5 (lignée conv-audit), branche `canal/conv-audit-n04` ; il n'a écrit ni le brouillon 1 ni le code v1.
- Date (UTC) : 2026-10-31, 09:50 (relevé `date -u`).
- Commit du code d'analyse : À REMPLIR au gel (commit qui contient `arene_melange_v2.py` à l'empreinte ci-dessous ; HEAD au moment du brouillon : `c7f5d3aa`, commits posés par l'agent parent ; le code remis n'est pas committé par l'auteur).
- Documents qui font foi (chemin + empreinte) :
  - `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/p-041-pont-vers-les-vrais-modeles-v1/brainstorm-malleabilite-et-arene-v1.md` — `08360a9402ff81d7d9146ed833d60e687f1be4d9acd0be3ab2867403dda8eb10` (pistes 2, 3, 4, 5) ;
  - `…/p-041-pont-vers-les-vrais-modeles-v1/reponse-pont-p041-vrais-modeles-v1.md` — `e98d9f5a0ccbf6a77675fc922b318eec67d4838acf3b1e0ea8657b79928155a3` ;
  - `docs/notes/anteriorite-P-041-v1/idee-P-041-est-elle-bonne-fusion-v3.md` (branche `origin/main`) — `343617ca195316a0339a8864eccf62f42275f551ee9144c3eaa6047ff7c02345` (trois scores (i), (ii), (iii)) ;
  - brouillon 1 : `preenregistrement-arene-melange-equilibre-v1-brouillon1.md` — `5129b8c26d384e92015142e6d80c1d29f922210975fc297ec487efab070284ce` ; sa contre-lecture `contre-lecture-arene-melange-v1-brouillon1.md` — `3721865417495678475ab995d43a3e56dd1b3b1df7b147a218f6ce9b0bc5bd1f` ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` — `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` ; bibliothèque : voir le bloc d'identité.
- Code et sorties de ce dossier (`brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/`) :
  - `arene_melange_v2.py` — `8e1e651b4be3e6fea6bf6bdf0fc00a19d479aa818323461fbf550582dfdb46bb` (le code de décision **refuse de partir** si cette empreinte, celle de la configuration, celles des quatre fichiers de la bibliothèque et les versions de numpy et scipy n'apparaissent pas dans le texte scellé, ou si la configuration du texte diffère de celle du code champ à champ) ;
  - `essais/test_arene_melange_v2.py` — `074aa9ff53f7d8d55b3cc922bf511a0b23af8dbf04ddd1d246df1a18e7b2f44d` ;
  - `calcul-puissance-arene-melange-v2.py` — `0991184bd899c82a192c052b44944e84eeee1858dd8526b0381d038ca0843efc` ; sa sortie `calcul-puissance-arene-melange-v2-sortie.txt` — `9cf0eaeb764524ad1b337009f4de551a7339fe05fb80405d3e006f6855a72c38` (désignée **(M)** ci-dessous) ;
  - `gel-conception-arene-melange-v2.md` — `1628515a8cf2955f328e5785e5de3ec4279211bec73bea47e870413781292b83` (conception et prédictions écrites **avant** les pilotes) ;
  - `calibrage-deltas-arene-melange-v2.json` — `f887e9c1051f40490e7c72c24fa74680f6b4e7818c0c9343d6e63a58c8ba933e` (choix des δ, racine de calibrage) ;
  - `essai-pilote-arene-melange-v2-detection.json` — `121580c88d580fdd88460eb2352455121ce1c9680ba7e0e30a5f7e23ae4d166d` ;
  - `essai-pilote-arene-melange-v2-logistique.json` — `a948c85a0dc074559133bc29067f6ed4975a1c0818426773822e8b6b5ac70d01` ;
  - `archive-observation-oracle-v1.py` — `4338d3558d25a1ae188c9067ba7281a403a17b1db22c6c8691cff5068a988def` ; sa sortie `archive-observation-oracle-v1.json` — `0b52cac34b83aa04bca918cf0384d3bd5f3dd0a2154fd39957e17a95d4a65bc4` ;
  - `journal-pilotes-arene-melange-v2.txt` — `fcaa40f8e9099915e6d56eccc0de42deec2ce432a87ef4ad87862e361c1a2391` (commandes, horodatages, empreintes, ordre des étapes).
- Code v1 et `CONFIG_V1` (brouillon 1) : cités seulement abrégés (`6402dc6b…`, `6685585f…`), pour que le code v1, qui cherche ses empreintes complètes, ne puisse pas partir sur ce texte.

Tout nombre de ce texte vient de (M) (section citée entre crochets, par exemple [M § 2]), du fichier de gel, du calibrage, de l'archive ou du journal, ou est un marqueur de gel (valeur laissée à Lazar). **Aucune lecture n'a été faite sur la racine de décision RACINE = 20261201 ni sur RACINE_TENUE = 20261202.**

### Bloc d'identité (vérifié par le code ; à régénérer par `arene_melange_v2.py identite` si le code ou la configuration change)

- Identifiant : PREREG-ARENE-MELANGE-EQUILIBRE-V1
- Racines de décision : RACINE = 20261201 ; RACINE_TENUE = 20261202
- Code : `arene_melange_v2.py` — 8e1e651b4be3e6fea6bf6bdf0fc00a19d479aa818323461fbf550582dfdb46bb
- Configuration (empreinte de la forme canonique) : 1d7544e652ee6ab782577c5731127c7338844ef3d39844d86842688ddb2031a3
- Bibliothèque `src/controle_ia/gardes.py` — a83c48ceba4877a2e226c3fd43669b464152f18169bb082e9b1c48ed92179439
- Bibliothèque `src/controle_ia/prereg.py` — 3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306
- Bibliothèque `src/controle_ia/scellement.py` — 93beeb1c8aae75463afc98e76ffb330b1e4f26be9c08ae8fee539a2df6a94ef2
- Bibliothèque `src/controle_ia/manifeste.py` — 1a5c7464523e224ca29d62ab70d83f9e7043d9bde3000ef1a4adc9ed74c8188d
- Versions : numpy 2.5.3 ; scipy 1.18.1 ; Python 3.13.18

<!-- configuration-canonique-debut -->
```json
{
 "K": 3,
 "T": 8,
 "alpha": 0.01,
 "boite_mu": 5.0,
 "d": 6,
 "deltas": [
  1.4,
  1.8
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
 "n_calibrage": 12,
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
 "schema_graines": "SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, role, ...)) ; bras commun 0, A 1, B 2, D 4, C1 5, C2 6, C3 7 ; roles cible 0, propre 1, attaques d'entrainement 2, calibration 3, fausses alertes 4, Monte-Carlo 5, departs 6, evaluation 7, init maxout 8, lois tenues 9, echantillons tenus 10, final 11, cout 12, Dirichlet 13, courbe 14 ; reechantillonnage (code_delta, code_contraste, 0, 0, 99)",
 "seuil_calibrage_bas": 0.1,
 "seuil_calibrage_haut": 0.03,
 "sigma_cible": 1.0,
 "sigma_max": 1.5,
 "sigma_min": 0.5,
 "tau": 0.25,
 "taux_departs_non_finis_max": 0.05,
 "taux_nonconv_max": 0.05,
 "tol_fpr": 0.005
}
```
<!-- configuration-canonique-fin -->

## Résumé pour Lazar

1. **Question (hypothèse principale)** : dans une arène synthétique où l'attaquant joue en dernier, le mélange d'équilibre B (double oracle tronqué à 8 tours) bat-il des témoins **à capacité égale** construits sur ses neuf moniteurs mêmes — poids uniformes (C1), poids aléatoires (C2), « ou » déterministe (C3) — et un moniteur unique à paramètres égaux (D) ? « B bat A » (A : défense unique réentraînée, **même oracle**, ce n'est pas le protocole de Bailey) n'est plus qu'un contrôle de plomberie.
2. **Oracle « détection »** retenu par principe (le double oracle exige une meilleure réponse au gain du jeu). Pilote logistique complet : B ≈ A (+0,003 ; +0,0015) : sous la régression, le mécanisme n'est pas exercé [M § 11].
3. **δ = (1,4 ; 1,8)** par une règle écrite avant, sur A seul, sur une racine de calibrage distincte (A détecte ≥ 10α à 1,4, ≥ 3α à 1,8).
4. **Pilote** (racine fraîche 20261293, 24 instances × 2 δ) [M § 2] : B − A = +0,13 aux deux δ ; B − C1 = +0,025 / +0,018 ; B − C2 = +0,036 / +0,037 ; B − C3 = −0,19 / −0,08 ; B − D = −0,24 / −0,11 ; B − A sur (ii) = −0,06 / −0,07.
5. **Prédiction** : plomberie tenue ; **hypothèse principale réfutée** (C3 et D font mieux que B aux deux δ) ; poids d'équilibre ≈ poids uniformes à la marge recommandée ; régression sur (ii). Ma prédiction écrite avant le pilote « B ≈ C1 à 0,01 près » a été **réfutée par le pilote** (+0,02), déclarée.
6. **Erreurs** [M § 3, § 5] : plomberie, taille par δ 0,000 sous « aucun effet » et 0,49–0,50 sous « effet = S1 » (règle de pertinence et de significativité, pas un test de « effet ≥ S1 ») ; Table 3 corrigée de Bonferroni sur 8 tests, tailles mesurées à la frontière ≤ 0,007 (supériorité) et ≤ 0,013 (équivalence).
7. **Temps** [M § 8] : 30,0 s de processeur par tâche (6 bras) ; N = 100 → **52 min de mur sur 2 cœurs** (cible ≤ 1 h 15 tenue ; N maximal 143 au temps moyen, 121 au temps maximal).
8. **Quatorze seuils** à geler (S1 à S14), aucun défaut ne s'applique. Un choix décide la classe de C1 et C2 : ρ (S6) ; le verdict de l'hypothèse principale n'en dépend pas [M § 7].
9. Rien sur les vrais modèles : un résultat ici dit seulement ce que le mécanisme fait dans une famille bornée connue, sous l'oracle « détection ».
10. Avant scellement : contre-lecture 2 par un autre modèle (R2), gel des seuils par Lazar, empreintes recalculées si une valeur change.

## Ce que l'expérience n'autorise pas

- **Rien sur les vrais modèles** ni sur les moniteurs d'activations réels : ni sur Llama, ni sur les sondes de Bailey et collègues, ni sur la boucle à 70 tours. Le monde est une famille de lois que nous avons écrite (`reponse-pont-p041-vrais-modeles-v1.md` § 0).
- **A n'est pas le protocole de Bailey** : il partage l'oracle « détection » des autres bras ; tout énoncé est **conditionnel à cet oracle** (sous l'oracle logistique, le mécanisme n'est pas exercé [M § 11]).
- **Rien sur l'équilibre du jeu complet** : B est un itéré du double oracle tronqué à 8 tours ; écart « valeur du jeu restreint − V(B) » au pilote : +0,015 et +0,025 [M § 9].
- **D n'est pas « la capacité »** : même nombre de paramètres, mais autre famille de fonctions, agrégation déterministe et trajectoire propre.
- **Monde favorable au « ou » déterministe** : queues gaussiennes et neuf moniteurs linéaires, où partager le budget de fausses alertes entre moniteurs coûte peu ; rien sur des moniteurs à queues lourdes ni sur des dizaines de sondes.
- Deux budgets seulement, choisis sur A seul (A tenu à ≥ 10α ; A presque contourné mais au-dessus du plancher) : rien au-delà.
- Aucune revendication d'antériorité ni de nouveauté : la zone « mélange d'équilibre de moniteurs contre attaquant adaptatif » n'est pas vérifiée (R8) ; références **SUPPOSÉ**.
- Aucun énoncé sur les moniteurs quadratiques, les réseaux profonds, d'autres dimensions, d'autres familles ou un attaquant en boîte noire.
- (iii) est une **borne haute** de la valeur du jeu (l'attaquant est un optimiseur local).
- Ni porte, ni dépense, ni modification de P-041 : le résultat est une pièce pour le tour 2 du collisionneur et pour la décision de Lazar sur P-041 v2.

## Antériorité (toutes SUPPOSÉ, non lues sur PDF pour ce texte)

Double oracle (McMahan, Gordon et Blum 2003) ; réponse stratégique à une population de politiques (Lanctot et collègues 2017) ; défenses randomisées contre attaques adverses (Pinot et collègues 2020). Bailey et collègues, arXiv `2412.09565v2`, lu sur PDF par session-depot (R-874) : seule l'idée de la boucle est reprise (réentraînement d'un moniteur sur toutes les attaques passées, attaquant qui répond au dernier moniteur), avec un autre oracle ; **aucun chiffre** de ce papier n'est repris (R7). La convention de non-infériorité « garder au moins la moitié de l'effet de la référence » citée en S6 est une pratique usuelle des essais cliniques, SUPPOSÉ, non vérifiée sur source pour ce texte.

## Hypothèse

Renvoi : brainstorm P-041 piste 3 (« la réponse correcte à une suite de meilleures réponses adverses est un mélange aux poids d'équilibre ») ; piste 2 (famille paramétrée par la perte de comportement δ que l'attaquant accepte) ; piste 4 (nouveauté résiduelle) ; piste 5 (coût par contournement). Scores de la fusion v3 de P-041 : (i) familles vues, (ii) familles tenues à l'écart, (iii) générateur adaptatif contre la défense figée, l'attaquant jouant en dernier.

**Principe de l'oracle du défenseur (S13), énoncé avant toute observation.** Le double oracle converge vers l'équilibre du jeu résolu à condition que chaque oracle rende une meilleure réponse **pour le gain de ce jeu**. Le gain est ici la matrice G des taux de détection au seuil de fausses alertes α. La régression logistique minimise une perte logarithmique moyenne ; elle ne maximise pas la détection à α ; ce n'est pas une meilleure réponse au gain. Un oracle qui n'en est pas une n'exerce pas le chemin testé (le mélange) et rend la comparaison muette (même logique que R5, « chemin non exercé »). L'oracle retenu maximise donc le taux de détection lissé au seuil α, **le même pour tous les bras**. Conséquence de portée : A est une « **défense unique réentraînée, même oracle** », **ce n'est pas le protocole de Bailey et collègues** (leurs sondes sont entraînées par régression) ; toutes les hypothèses ci-dessous sont **conditionnelles à cet oracle**. L'observation qui a précédé ce choix au brouillon 1 est en note (§ Plan 6) ; le fait qui la remplace est le pilote logistique complet (§ Prédiction, P-L1, P-L2).

- **HP (hypothèse principale)** : contre la meilleure réponse adverse finale (l'attaquant joue en dernier contre la défense figée après T tours), le mélange d'équilibre B **bat chacun des témoins à capacité égale** — C1 (mêmes 9 moniteurs, poids uniformes), C2 (mêmes moniteurs, poids aléatoires), C3 (« ou » déterministe des mêmes moniteurs), D (moniteur unique maxout à 63 paramètres comme B) — d'un effet d'intérêt (marge S6), aux deux valeurs de δ.
- **H0 de HP** : pour au moins un témoin et un δ, B ne le bat pas d'un effet d'intérêt (« X > B », « ≈ », « X ≳ B », « B ≳ X » ou « ? »).
- **Questions qualifiantes**, une par témoin, lues dans la Table 3 et toujours recopiées : C1, rôle des **poids d'équilibre** à moniteurs identiques ; C2, poids d'équilibre contre **poids quelconques** ; C3, **tirage au hasard** contre **agrégation déterministe** des mêmes moniteurs ; D, mélange contre un **moniteur unique plus riche** (paramètres égaux, autre famille de fonctions, trajectoire propre ; ce n'est pas « la capacité » au sens fonctionnel, CM-03).
- **Contrôle de plomberie PC** (ancienne H1, CM-02) : B bat A (défense unique réentraînée, même oracle) sur (iii), aux deux δ. Attendu ; il dit seulement que le mécanisme « mélange » est exercé. Son échec est une surprise et déclenche l'audit (R4, symétrie).
- **Non-régression** : Δ(B, A) sur (ii) (familles tenues à l'écart), lue avec une tolérance S5 et sans seuil.
- **Hypothèses de travail** : (a) l'oracle du défenseur (plusieurs départs déterministes) est une meilleure réponse approchée, la même pour tous les bras ; il est approché pour D (seuil gaussien, deux départs : biais défavorable à D, CM-16) ; (b) l'oracle de l'attaquant (SLSQP sous contrainte, départs tirés) est une meilleure réponse approchée, contrôlée par un attaquant final renforcé ; (iii) est une borne haute de la valeur du jeu ; (c) la loi propre est N(0, I) et connue du code, pas des bras, qui ne voient que des échantillons ; (d) B est un itéré du double oracle **tronqué à T = 8 tours**, pas l'équilibre du jeu complet (CM-11).

## Prédiction chiffrée et signe attendu

Toutes les valeurs viennent des pilotes sur la **racine d'essai fraîche** (20261293 / 20261294 ; 24 instances × 2 δ ; (M) et fichiers cités). Elles ne sont pas opposables : la décision se lit sur RACINE, jamais lue.

### A. Prédictions écrites avant les pilotes (`gel-conception-arene-melange-v2.md`) et leur sort sur les pilotes

| Prédiction du gel (avant) | Pilote | Sort |
|---|---|---|
| P-L1 : oracle logistique, poids de B purs sur plus de la moitié des tâches de chaque δ (prédiction de la contre-lecture, adoptée) | parts pures 0,29 (δ 1,4) et 0,12 (δ 1,8) ; support moyen 2,04 et 2,46 (contre 3,83 et 4,00 sous l'oracle détection) [M § 11, § 9] | **réfutée** aux deux δ (mélange presque dégénéré, pas pur) |
| P-L2 : oracle logistique, \|B − A\| < 0,02 sur (iii) | +0,0030 IC95 [+0,0015 ; +0,0047] ; +0,0015 IC95 [+0,0005 ; +0,0030] [M § 11] | **tenue** : sous la régression, le mécanisme n'est pas exercé |
| B − A + aux deux δ | +0,1345 ; +0,1276 [M § 2] | tenue |
| B − C1 ≈ 0 (\|moyenne\| < 0,01) aux deux δ | +0,0246 IC95 [+0,0159 ; +0,0345] ; +0,0184 IC95 [+0,0106 ; +0,0263] [M § 2] | **réfutée** aux deux δ : les poids d'équilibre battent les poids uniformes d'environ 0,02 (la mesure de la contre-lecture, +0,005 sur trois tâches, était imprécise) ; identique sous chaque attaquant seul [M § 9] |
| B − C2 + aux deux δ | +0,0357 ; +0,0367 | tenue |
| B − C3 − aux deux δ | −0,1932 ; −0,0807 | tenue |
| B − D − aux deux δ | −0,2354 ; −0,1118 | tenue |
| B − A sur (ii) − aux deux δ | −0,0612 ; −0,0694 | tenue |

Bilan : 16 branches (2 logistiques × 2 δ, 6 contrastes × 2 δ), 12 tenues, 4 réfutées (P-L1 et B − C1, aux deux δ). Conséquence pour S13 : choisir l'oracle « logistique » mène, au vu de son pilote, à une Table 1 « mécanisme non démontré » (B − A ≈ +0,003 < S1) : la décision ne dirait rien du mélange.

### B. Prédictions pour la décision, par contraste et par δ (deux branches)

Pour chaque ligne : le signe prédit, la classe prédite sous les valeurs recommandées (S1 = S5 = 0,02 ; S6 : ρ = 0,25), l'estimation pilote, la probabilité simulée de la classe prédite à N = 100 (pilote pris pour vérité, [M § 3, § 5, § 6, § 7]), la confiance de l'auteur (probabilité simulée, arrondie vers le bas à 0,05 et plafonnée à 0,95 pour l'incertitude de modèle : le pilote ne compte que 24 instances), et la **branche opposée**, qui réfute la prédiction et déclenche l'audit (R4, déclencheur 1).

| # | Contraste | δ | Signe | Classe prédite | Pilote : moyenne [IC95] | Probabilité simulée | Confiance | Branche opposée (réfutation → audit) |
|---|---|---|---|---|---|---|---|---|
| P1 | B − A (iii), plomberie | 1,4 | + | « mécanisme exercé » (ligne 4) | +0,1345 [+0,1150 ; +0,1524] | 1,000 | 0,95 | Table 1 ligne 5 (le mélange perd) ou 6 (non démontré) |
| P1 | idem | 1,8 | + | idem | +0,1276 [+0,1217 ; +0,1327] | 1,000 | 0,95 | idem |
| P2 | B − C1 (iii) | 1,4 | + | « ≈ » | +0,0246 [+0,0159 ; +0,0345] | 0,882 (« B ≳ C1 » 0,118) | 0,85 | « B > C1 » (les poids d'équilibre apportent plus du quart du gain du mécanisme) ; « C1 ≳ B » ou « C1 > B » (signe contraire) |
| P2 | idem | 1,8 | + | « ≈ » | +0,0184 [+0,0106 ; +0,0263] | 1,000 | 0,95 | idem |
| P3 | B − C2 (iii) | 1,4 | + | « B ≳ C2 » | +0,0357 [+0,0259 ; +0,0463] | 0,983 (« B > C2 » 0,016) | 0,95 | « C2 ≳ B » ou « C2 > B » (des poids quelconques font aussi bien) |
| P3 | idem | 1,8 | + | « B ≳ C2 » | +0,0367 [+0,0262 ; +0,0473] | 0,842 (« B > C2 » 0,158) | 0,80 | idem |
| P4 | B − C3 (iii) | 1,4 | − | « C3 > B » | −0,1932 [−0,2104 ; −0,1742] | 1,000 | 0,95 | « B > C3 » ou « B ≳ C3 » (le tirage au hasard paie contre l'agrégation déterministe) |
| P4 | idem | 1,8 | − | « C3 > B » | −0,0807 [−0,0874 ; −0,0739] | 1,000 | 0,95 | idem |
| P5 | B − D (iii) | 1,4 | − | « D > B » | −0,2354 [−0,2434 ; −0,2275] | 1,000 | 0,95 | « B > D » ou « B ≳ D » (le mélange bat le moniteur unique à paramètres égaux) |
| P5 | idem | 1,8 | − | « D > B » | −0,1118 [−0,1186 ; −0,1050] | 1,000 | 0,95 | idem |
| P6 | B − A (ii) | 1,4 et 1,8 | − | Table 2 « régression avérée au-delà de la tolérance » | −0,0612 [−0,0880 ; −0,0320] ; −0,0694 [−0,0937 ; −0,0439] | 1,000 | 0,95 | borne basse B2 > 0 dans un δ (B améliore (ii)) |
| P7 | HP (Table 4) | — | — | « HP réfutée » (statut « réfutée, un témoin fait mieux » aux deux δ : C3 et D) | — | 1,000 pour ρ = 0,10, 0,25 et 0,50 | 0,95 | « HP confirmée », « HP dépend de δ » |

Classe de C1 et C2 selon ρ (S6), à N = 100 [M § 5] : ρ = 0,10 → B − C1 « B > C1 » 0,993 (δ 1,4) et 0,550 (δ 1,8, sinon « B ≳ C1 ») ; B − C2 « B > C2 » 1,000 aux deux δ ; ρ = 0,50 → « ≈ » pour C1 et C2 aux deux δ (1,000). Les classes de C3 et D (« X > B », 1,000) et le verdict de la Table 4 ne dépendent pas de ρ.

Descriptives (sans verdict) [M § 9] : coût par contournement défini dans 100 % des tâches pour tous les bras ; part censurée parmi les définies à δ 1,4 : A 0,00, B 0,75, C1 0,12, C2 0,21, C3 0,08, D 0,46 ; à δ 1,8 : 0,00 pour tous ; médiane des fractions non censurées à δ 1,8 : A 0,531, B 0,875, C1 0,750, C2 0,719, C3 0,781, D 0,781 ; aucune courbe non monotone. Courbe V(δ') moyenne à δ 1,8 (δ' = 0 ; 0,25 ; 0,5 ; 0,75 ; 1 × δ) : A 0,468 0,359 0,232 0,095 0,015 ; B 0,385 0,338 0,282 0,219 0,143 ; C3 0,889 0,771 0,629 0,450 0,224 ; D 0,897 0,782 0,642 0,474 0,255. Nouveauté résiduelle décroissante dans A, B, D (tour 8 : 0,149 ; 0,164 ; 0,179). (iii) par tour : A plat (0,061 → 0,056), B croissant (0,060 → 0,169), D croissant (0,061 → 0,356). Écart « valeur du jeu restreint − V(B) » : +0,015 ; +0,025 (positif attendu).

**Lecture anticipée**, à ne pas confondre avec un résultat : si ces prédictions tiennent, le mélange d'équilibre bat la défense unique réentraînée (même oracle), et ses poids d'équilibre battent des poids uniformes ou quelconques sur les mêmes moniteurs d'environ 0,02 à 0,04 ; mais une agrégation **déterministe** des mêmes neuf moniteurs (« ou ») et un moniteur unique maxout à paramètres égaux font beaucoup mieux (de 0,08 à 0,24), et le gain sur (iii) se paie d'environ 0,06 à 0,07 sur (ii) (alors que C3 et D gagnent sur (ii) : B − C3 et B − D ≈ −0,45 [M § 2]). Ce serait un argument **contre** la piste 3 comme méthode propre dans ce monde : l'avantage revient à l'agrégation déterministe, pas au tirage au hasard. Conditionnel à l'oracle « détection » et à un monde favorable au « ou » déterministe.

## Métrique

Notations : une **tâche** = (δ, instance) ; une instance fixe la loi cible ; les deux δ partagent la loi cible d'une instance (appariement entre δ). Taux de détection d'une défense mixte {(m_i, p_i)} sur une loi Q : Σ_i p_i × part des échantillons de Q dont le score dépasse le seuil t_i de m_i ; seuil calibré au quantile 1 − α des scores de 20 000 échantillons propres communs aux bras d'une tâche (α = S9).

- **(iii), principale, V(bras)** : après T tours (S12), défense figée ; l'attaquant calcule deux meilleures réponses sous la contrainte distance ≤ δ et la boîte : **standard** (12 départs tirés + départ « tiré vers l'origine » + les attaques passées de la trajectoire — celles de B pour C1, C2, C3 —, 512 échantillons de Monte-Carlo par composante, 100 itérations) et **renforcée** (48 départs, 200 itérations, plus la réponse standard) ; chacune est évaluée sur 19 998 échantillons frais ; **V = la plus basse des deux détections**. Le minimum de deux estimations fraîches biaise V d'au plus un écart d'échantillonnage (≈ 0,001 à 0,003) en faveur de l'attaquant, pour tous les bras (déclaré, CM-17). Unité : proportion dans [0 ; 1].
- **Écart apparié** Δ(X, Y) = moyenne sur les instances de V(X) − V(Y), à δ fixé.
- **(ii) familles tenues à l'écart** : 50 lois par tâche tirées de **RACINE_TENUE**, deux sous-familles alternées (déplacement aléatoire dans la boule de comportement, rayon tiré entre 0,5 δ et δ ; tout le budget sur une composante tirée vers l'origine, échelles tirées) ; 3 999 échantillons par loi ; score = moyenne des 50 taux. Rapporté aussi par sous-famille ; courbe par tour pour A, B, D.
- **(i) familles vues** : moyenne des taux de la défense finale sur les attaques de la trajectoire (descriptif).
- **Courbe V(δ')** (piste 5, sans censure) : détection de la cible non modifiée (δ' = 0, **ligne de base**), puis de la meilleure réponse (3 départs tirés + départ vers l'origine + attaques passées et finales projetées) à δ' = 0,25 δ, 0,5 δ, 0,75 δ, puis V à δ' = δ. Mélange de forces d'attaquant (courbe plus faible que la finale) : déclaré.
- **Coût par contournement** (piste 5) : seuil **relatif** κ × ligne de base (κ = S14). **Garde de ligne de base** : si κ × base < 2α, mesure « non définie » pour ce bras et cette tâche (comptée, jamais remplacée). Sinon : premier point de la courbe sous le seuil ; **censuré à 1** si aucun ; puis bissection en 3 pas dans l'intervalle qui l'encadre (résolution δ/32). Rapporté par bras et par δ : part définie, part censurée parmi les définies, médiane des fractions non censurées, nombre de tâches à courbe non monotone (hausse de plus de α entre points consécutifs). Aucune moyenne mêlant censurées et non censurées n'est interprétée (CM-10).
- **Nouveauté résiduelle** (piste 4, bras à trajectoire) : au tour t, norme du résidu du déplacement θ_t − θ* après projection orthogonale sur l'espace des déplacements des tours 1 à t − 1, divisée par la norme du déplacement (dimension des paramètres 36 ≫ T = 8).
- **Contrôles** : fausses alertes de chaque défense finale sur 20 000 échantillons propres indépendants (moyenne par bras, écart à α, écart entre bras par tâche) ; valeur du jeu restreint de B et son écart à V(B) ; V standard − V renforcé par bras ; contrastes sous chaque attaquant seul ; poids finaux de B et de C2 (support, pureté, égalité à l'uniforme) ; attaquant : départs, départs non finis, statuts SLSQP, itérations maximales, réponses à la limite d'itérations (CM-09) ; entraînements non convergés.
- **Intervalles** : rééchantillonnage apparié des instances, 20 000 tirages, quantiles (percentiles) 0,3125 %, 0,625 %, 1,25 %, 2,5 %, 5 % et symétriques ; graines `SeedSequence(entropy=racine, spawn_key=(code_delta, code_contraste, 0, 0, 99))`. Usage par table : § Critères.

## Seuil

**Tous les seuils sont à geler par Lazar en une ligne datée de `registres/decisions.md`. Aucun défaut ne s'applique.** Pour chacun : la valeur (marqueur), la recommandation de l'auteur, sa raison, la source. Les seuils S4, S7, S8 (interne), S9, S11, S12, S13 et S14 sont des champs de la configuration : toute valeur différente de la recommandation change le code et la configuration, donc leurs empreintes et le bloc d'identité (à régénérer). S1, S2, S3, S5, S6 et S10 sont des seuils de lecture, appliqués par le lecteur R13.

**S1 — effet minimal du contrôle de plomberie, Δ(B, A) sur (iii)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02** (deux fois α).
- Raison : un gain de détection plus petit que deux fois le taux de fausses alertes est négligeable à ce point de fonctionnement ; principe, non pilote. Règle « moyenne ≥ S1 et borne basse B2 > 0 » (pertinence et significativité), par δ, à N = 100 : puissance 0,977 (δ 1,4) et 1,000 (δ 1,8) à un effet vrai de 0,03 ; taille 0,000 sous « aucun effet » ; 0,491 et 0,501 sous « effet vrai = S1 » (à effet égal à S1, la règle confirme une fois sur deux : ce n'est pas un test de « effet ≥ S1 ») [M § 3]. Option : 0 (signe seul ; taille par δ 0,008 et 0,010 [M § 3]).

**S2 — erreur de première espèce et corrections**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **5 % bilatéral par famille** ; Tables 1 et 2 : Bonferroni sur les 2 δ (bornes B2) ; Table 3 : Bonferroni sur les 8 tests (4 témoins × 2 δ, bornes B8), équivalence par deux tests unilatéraux au niveau 0,05/8 (intervalle E8).
- Raison : la taille se lit **par δ et sous chaque hypothèse nulle** (CM-05), pas sous le double nul. Plomberie : voir S1. Table 3, tailles mesurées à la frontière de la marge, N = 100, ρ = 0,25 : P(« B > X » | Δ = +m) 0,002 à 0,003 ; P(« X > B » | Δ = −m) 0,002 à 0,007 ; P(« ≈ » | Δ = +m) 0,005 à 0,013 (nominal 0,006 ; dépassement jusqu'à 0,013 pour B − C1 à δ 1,4, approximation de Student sur 24 instances : déclaré) [M § 5]. « HP confirmée » est une intersection-union (taille au plus celle du test le plus défavorable) ; « HP réfutée » est une union, protégée par la correction.

**S3 — puissance visée**
- Valeur : À REMPLIR par Lazar.
- Recommandation : plomberie ≥ **0,9** à un effet vrai de 0,03 par δ ; Table 3 : probabilité de la classe prédite ≥ **0,8** par contraste et par δ sous le pilote.
- Raison : à N = 100 : plomberie 0,977 et 1,000 [M § 3] ; Table 3 (ρ = 0,25) : C1 0,882 et 1,000 ; C2 0,983 et 0,842 ; C3 et D 1,000 [M § 5]. Limite déclarée : sous un écart vrai nul sur (ii), « sans régression » ne sort qu'avec une probabilité de 0,491 à S5 = 0,02 [M § 6] (écart-type de (ii) par instance ≈ 0,07) ; sous le pilote, « régression avérée » sort avec 1,000.

**S4 — nombre d'instances N par valeur de δ**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **N = 100** (200 tâches).
- Raison : S3 tenue ; temps projeté 100,0 min de processeur, 52,1 min de mur sur 2 cœurs [M § 8]. Autres options : N = 60 (31,3 min ; C1 « ≈ » 0,652 à δ 1,4 ; C2 « B ≳ C2 » 0,988 et 0,925) ; N = 150 (78,2 min, au-delà de 1 h 15) [M § 5, § 8].

**S5 — tolérance de non-régression sur (ii), Δ(B, A)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02 (= S1)**.
- Raison, indépendante du pilote : symétrie avec S1 — même principe (2α) ; la table ne peut pas tolérer sur (ii) un recul plus grand que l'effet minimal qu'elle cherche sur (iii). Sous le pilote : « régression avérée » 1,000 [M § 6]. Options : 0,01 (= S1/2, plus strict ; sous le pilote : avérée 1,000) ; 0,05 (marge de non-infériorité usuelle de 5 points pour une proportion ; sous le pilote : avérée 0,731, non exclue 0,269 : lecture instable) [M § 6]. **Lecture sans seuil** recopiée dans tous les cas (signe, estimation, intervalle B2).

**S6 — marges relatives des contrastes principaux (Table 3)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **ρ = 0,25**, plancher S1/2 = 0,01 : m(δ) = max(ρ × moyenne pilote de Δ(B, A) à δ ; 0,01), arrondie au millième → **m(1,4) = 0,034 ; m(1,8) = 0,032** (valeurs gelées ; non arrondies 0,0336 et 0,0319 [M § 4]).
- Raison : « un témoin équivaut à B s'il garde au moins les trois quarts du gain du mécanisme (B sur A) » ; plus strict que la convention usuelle de non-infériorité (garder la moitié de l'effet de la référence, SUPPOSÉ) parce que les contrastes sont ici précis et bon marché. Marge relative (CM-04) : elle suit l'effet du mécanisme à chaque budget au lieu d'une valeur absolue. La grille ρ = 0,10 / 0,25 / 0,50 a été écrite avant tout résultat de pilote (horodatage du script de puissance, journal étape 7) ; **la recommandation 0,25, elle, est écrite après la lecture du pilote** : déclaré. **Choix qui décide la classe de C1 et C2** (donc le déclencheur de Lazar « B ≈ C1 ») : ρ = 0,10 → « B > C1 » et « B > C2 » probables ; ρ = 0,25 → « ≈ » pour C1, « B ≳ C2 » ; ρ = 0,50 → « ≈ » pour C1 et C2 [M § 5]. Le verdict de la Table 4 n'en dépend pas [M § 7]. La lecture sans seuil de B − C1 et B − C2 (estimation et intervalle B8) est recopiée dans la phrase de synthèse quelle que soit la valeur.

**S7 — λ du « ou » déterministe C3**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **8**.
- Raison : fixé au gel, avant les pilotes ; log(9)/8 ≈ 0,27 écart-type au plus entre le score de C3 et λ fois le maximum des scores standardisés (essai `test_ou_deterministe_sain_et_artefacts`) ; la contre-lecture a trouvé λ = 4 et λ = 8 voisins.

**S8 — plafond de temps**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **`timeout 4500` (1 h 15 de mur)** externe pour l'exécution de décision (deux processus d'un fil chacun), et **600 s de processeur par tâche** (garde interne `plafond_cpu_tache_s`).
- Raison : temps mesuré par tâche (6 bras) : moyenne 30,00 s, médiane 29,64 s, maximum 35,68 s ; projeté à N = 100 : 52,1 min ; N maximal sous 1 h 15 : 143 au temps moyen, 121 au temps maximal [M § 8].

**S9 — taux de fausses alertes α et tolérances**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **α = 0,01** ; garde d'arrêt |taux mesuré − α| ≤ 0,005 par défense finale ; déclencheur d'audit |moyenne d'un bras − α| > 0,001 dans un δ.
- Raison : point de fonctionnement usuel des moniteurs ; au pilote, fausses alertes finales de 0,0080 à 0,0131, écart à α des moyennes par bras ≤ 0,0003, écart entre bras par tâche moyen 0,0014 à 0,0016 [M § 1, § 9] ; 0,001 vaut environ dix fois l'erreur-type de la moyenne d'un bras à N = 100.

**S10 — déclencheur « trop beau / trop mauvais », calibré sur le pilote**
- Valeur : À REMPLIR par Lazar.
- Recommandation : audit si la moyenne de V d'un bras dans un δ sort de la plage [minimum ; maximum] des V par tâche du pilote : δ 1,4 : A [0,0034 ; 0,2468] ; B [0,1681 ; 0,2743] ; C1 [0,1281 ; 0,2501] ; C2 [0,1077 ; 0,2515] ; C3 [0,2988 ; 0,4549] ; D [0,4033 ; 0,4773] ; δ 1,8 : A [0,0004 ; 0,0839] ; B [0,1072 ; 0,1778] ; C1 [0,0881 ; 0,1662] ; C2 [0,0638 ; 0,1633] ; C3 [0,1887 ; 0,2669] ; D [0,2068 ; 0,2893] [M § 10] ; plus la règle de Lazar : moyenne de V(B) ≥ 0,99.
- Raison : symétrique (les deux sens), calibré (CM-07) : une moyenne sur 100 tâches hors de la plage de 24 valeurs individuelles signale une anomalie grossière ; la règle « V(B) ≥ 0,99 » est gardée bien qu'inatteignable ici.

**S11 — budgets de comportement δ**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **δ = (1,4 ; 1,8)**, par la règle `choisir_deltas` écrite avant son exécution : grille 0,6 à 2,4, 12 instances, racine de calibrage 20261295, bras A seul ; δ_haut = plus grand δ où V(A) moyen ≥ 3α (A pas au plancher), δ_bas = plus grand δ < δ_haut où V(A) moyen ≥ 10α (A pas presque entièrement contourné).
- Raison : critère sur A seul (CM-04) ; V(A) au calibrage : 0,131 à 1,4 ; 0,035 à 1,6 ; 0,034 à 1,8 ; 0,010 à 2,0 (`calibrage-deltas-arene-melange-v2.json`) ; au pilote : V(A) 0,0764 et 0,0154, V(B) 0,2109 et 0,1430 : aucun bras au plancher, contrairement à δ = 2,4 au brouillon 1. Changer la règle après ce calibrage serait un changement de conception.

**S12 — nombre de tours T**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **T = 8**.
- Raison : nouveauté résiduelle de 1,000 au tour 1 à 0,149–0,179 au tour 8 [M § 9] ; T ≪ dimension des paramètres (36).

**S13 — oracle du défenseur (identique pour tous les bras)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **« détection »**.
- Raison : principe (§ Hypothèse), énoncé avant l'observation. Option « logistique » : au pilote logistique, B − A = +0,003 et +0,0015, support du mélange 2,0 à 2,5 [M § 11] : la Table 1 rendrait « mécanisme non démontré » et la décision ne dirait rien du mélange.

**S14 — seuil de contournement relatif κ**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **κ = 0,5** (contourné si la détection tombe à la moitié de celle de la cible non modifiée), garde de ligne de base κ × base ≥ 2α.
- Raison : principe (§ Plan 6, point 2) ; fixé au gel avant les pilotes. Au pilote : mesure définie dans 100 % des tâches ; parts censurées par δ en § Prédiction [M § 9]. Mesure descriptive, sans verdict.

## Plan d'analyse

### 1. Monde
Loi propre N(0, I_6). Loi cible d'une instance : 3 composantes, moyennes de norme r = 4 dans des directions tirées (graine de l'instance), écarts-types 1. Loi d'attaque : 3 composantes appariées aux composantes cibles, moyennes et écarts-types diagonaux dans la boîte (|μ| ≤ 5, σ ∈ [0,5 ; 1,5]). **Contrainte de comportement** : distance = racine de la moyenne sur k du carré de la distance de Wasserstein d'ordre 2 entre composantes appariées (pour des gaussiennes diagonales : ‖μ_k − μ*_k‖² + ‖σ_k − σ*_k‖²) ≤ δ ; borne haute de la distance de Wasserstein entre mélanges, exacte, lisse et lisible.

### 2. Bras
Tour 0 commun : moniteur linéaire M0 entraîné contre la loi cible (graine commune ; reproductibilité bit à bit vérifiée par garde à chaque tâche). Puis, pour t = 1 … T, dans chaque bras à trajectoire : l'attaquant calcule une meilleure réponse contre la défense déployée ; le défenseur se met à jour.
- **A, défense unique réentraînée, même oracle** : déploie le dernier moniteur ; met à jour par un moniteur linéaire entraîné (oracle S13) contre le mélange uniforme de toutes les attaques passées (loi cible comprise).
- **B, mélange d'équilibre (double oracle tronqué à T tours)** : matrice de gains G (moniteur i × attaque j, taux évalués sur des échantillons fixés par attaque) ; déploie p = stratégie d'équilibre du défenseur (programme linéaire, HiGHS) ; après la nouvelle attaque, q = stratégie d'équilibre de l'attaquant sur la matrice élargie ; nouveau moniteur linéaire entraîné contre le mélange q ; ligne ajoutée. Défense finale : p sur la matrice 9 × 9 après le tour T. B est un **itéré tronqué**, pas l'équilibre du jeu complet : l'écart « valeur du jeu restreint − V(B) » est rapporté par δ.
- **D, unique à paramètres égaux** : déploie un seul moniteur maxout à t + 1 unités au tour t (T + 1 = 9 unités à la fin, autant de paramètres que le mélange final de B : vérifié par essai) ; entraîné contre le mélange uniforme de ses attaques passées. Oracle à plusieurs unités : seuil gaussien approché (exact pour un moniteur linéaire seulement) et deux départs : biais **défavorable à D**, déclaré (CM-16).
- **C1, C2, C3, témoins « finale seulement »** sur les 9 moniteurs mêmes de B après le tour T (aucune trajectoire, aucune attaque nouvelle) : C1 poids 1/9 ; C2 poids tirés d'une loi de Dirichlet de paramètres (1, …, 1) (graine `(code_delta, instance, 6, T + 1, 13)`) ; C3 « ou » déterministe : pour chaque moniteur, z_i = (s_i − μ_i)/σ_i (moyenne et écart-type du score sur les 20 000 échantillons propres de calibration), score log-somme-exp_i(λ z_i) avec λ = S7, seuil recalibré à α ; même nombre de paramètres (63) que B et D.
Pour chaque bras, la défense finale est figée ; l'attaquant joue en dernier (§ Métrique) avec les attaques passées de sa trajectoire comme départs supplémentaires (celles de B pour C1, C2, C3).

### 3. Graines (R9)
- **RACINE = 20261201** (décision), **RACINE_TENUE = 20261202** (familles tenues à l'écart de la décision). Racines d'essai, toutes fixées avant leur première exécution et sans lien avec un résultat : 20261293 / 20261294 (pilote v2, oracle détection et oracle logistique) ; 20261295 / 20261296 (calibrage des δ, bras A seul) ; 20261297 / 20261298 (essais du code, mesures de temps). Les racines du brouillon 1 (20261291 / 20261292), sur lesquelles la conception a été choisie, sont refusées par garde en v2.
- Chaque tirage : `numpy.random.SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, rôle, …))`, numpy ≥ 1.25. Codes de bras : commun 0, A 1, B 2, D 4, C1 5, C2 6, C3 7 (le code 3 de l'ancien bras C n'est pas réemployé). Rôles : cible 0 ; propre d'entraînement 1 (commun aux bras) ; attaques d'entraînement 2 ; calibration 3 (commune) ; fausses alertes 4 (commune) ; Monte-Carlo de l'attaquant 5 ; départs 6 ; évaluation 7 ; initialisation du maxout 8 ; lois tenues 9 et leurs échantillons 10 (racine tenue) ; final 11 (sous-clés 1 à 6) ; coût 12 ; Dirichlet 13 ; courbe 14 ; rééchantillonnage `(code_delta, code_contraste, 0, 0, 99)`. Le schéma est écrit dans la configuration (`schema_graines`) donc dans le manifeste ; le champ « graines » que `creer_manifeste` ajoute de lui-même n'est pas employé par le code (noté au manifeste, CM-14).
- Chaque bras tire ses graines de son propre code : l'ordre et la présence des autres bras ne changent aucun résultat (essai `test_ordre_des_bras_sans_effet`).
- Garde de la racine de décision **dans `gen`** (CM-15) : toute graine tirée de RACINE ou RACINE_TENUE exige une autorisation posée par `autoriser_decision` (préenregistrement scellé, conforme, identifié), y compris dans chaque processus de travail, qui la re-vérifie.

### 4. Comparaisons et multiplicité
- **Contrôle de plomberie** (Table 1) : Δ(B, A) sur (iii) aux deux δ ; règle « pertinence et significativité » (moyenne ≥ S1 et borne basse > 0), bornes Bonferroni sur 2 δ (quantiles 0,625 % et 99,375 %).
- **Non-régression** (Table 2) : Δ(B, A) sur (ii), bornes Bonferroni sur 2 δ.
- **Hypothèse principale** (Tables 3 et 4) : Δ(B, C1), Δ(B, C2), Δ(B, C3), Δ(B, D) sur (iii), aux deux δ : 8 tests. Bornes Bonferroni sur 8 tests (quantiles 0,3125 % et 99,6875 %) pour « B > X », « X > B », « B ≳ X », « X ≳ B » ; équivalence par deux tests unilatéraux au niveau 0,05/8 (intervalle de quantiles 0,625 % et 99,375 %). « HP confirmée » est une intersection-union (aucune correction nécessaire, la correction la rend prudente) ; « HP réfutée » est une union, protégée par la correction.
- **Descriptives** (sans verdict) : Δ(B, C3) et Δ(B, D) sur (ii) ; Δ(C3, A), Δ(D, A), Δ(C1, C2) sur (iii) ; Δ(B, A) sur (i) ; coût par contournement et courbe V(δ') par bras ; nouveauté résiduelle ; courbes par tour de (ii) et (iii) ; sous-familles de (ii) ; poids de B et de C2 ; contrôles de l'attaquant et de l'optimiseur.

### 5. Ordre d'exécution, arrêt et reprise
(1) Essais du code (`python3 -m pytest -q …/essais/test_arene_melange_v2.py`) ; (2) une seule invocation `arene_melange_v2.py decision --prereg prereg/<nom>.md --instances 0:N --run-id <AAAAMMJJ-HHMMSS-arene-melange-v2>` sous `timeout` (S8), arbre git propre ; (3) analyse écrite par le même processus (`analyse-arene.json`, scellé par `ecrire_resultat`) ; (4) lecture par un sous-agent neuf (R13), qui applique les tables ci-dessous ; `lire_tables` du code est une aide mécanique, le texte scellé fait foi en cas d'écart.

**Reprise après arrêt (CM-12)** : (a) arrêt de cause **externe** (signal, `timeout`, machine), aucun résultat écrit : **une** reprise complète, même code, mêmes racines, nouvel identifiant de run ; le premier manifeste reste en place et est cité par le second ; une seconde interruption externe → non concluant ; (b) arrêt par une **garde interne** (`GardeArret`) : pas de reprise (le calcul est déterministe, la garde se redéclencherait) → non concluant, version nouvelle du préenregistrement avec la cause ; (c) aucun point de reprise partiel : `pool.map` perd les tâches finies, c'est déclaré et accepté (temps projeté sous la moitié du plafond).

### 6. Historique de conception (déclaré ; aucune décision n'a lu une racine de décision)
1. **Oracle du défenseur.** Le principe (S13, § Hypothèse) est premier. Note sur l'observation qui a précédé le changement au brouillon 1 : sur l'instance 0 de la racine d'essai du brouillon 1, δ = 1,6, l'oracle logistique donnait des poids purs et B ≈ A ; trois exécutions d'une tâche avaient été faites avec des versions intermédiaires du code (oracle logistique, oracle « détection », variante logistique), non conservées. L'observation est désormais **archivée par reproduction** avec le code v1 remis (`archive-observation-oracle-v1.py`, sortie `archive-observation-oracle-v1.json`, empreintes ci-dessus) sur les quatre combinaisons oracle × seuil essayées : sous l'oracle logistique, V(B) = 0,0702 contre V(A) = 0,0689, poids de B purs ; sous l'oracle « détection », V(B) = 0,1962 contre 0,0640 ; la combinaison « détection, seuil 0,10 » est identique bit à bit (hors temps) à la tâche du pilote v2 du brouillon 1. La valeur « 0,070 contre 0,069 » du brouillon 1, lue avec un code non conservé, n'est opposable que par cette reproduction (R6). Une instance ne fait pas un fait : celui qui la remplace est le **pilote logistique complet** sur la racine fraîche (§ Prédiction, P-L1, P-L2).
2. **Seuil de contournement.** Brouillon 1 : 0,5 puis 0,10 (absolu), fixé après avoir vu le contournement gratuit de B sur la même instance (archivé : avec le seuil 0,5, coût de B = 0,031 de δ ; avec 0,10, B, C et D censurés à 1 sur cette instance). Principe (avant toute observation de la v2) : un seuil absolu peut être au-dessus de la détection de la cible non modifiée, et le coût est alors nul par définition ; le seuil doit donc être **relatif** à cette ligne de base (κ = S14), avec une **garde** : κ × ligne de base ≥ 2α, sinon la mesure est « non définie » pour ce bras et cette tâche (comptée, rapportée par δ, jamais remplacée). La courbe V(δ') sur une grille de budgets (sans censure) est rapportée à côté.
3. **δ.** Brouillon 1 : (1,6 ; 2,4), 2,4 au plancher pour A. v2 : règle écrite dans le code (`choisir_deltas`) avant son exécution, appliquée sur une racine de calibrage distincte, critère sur A seul (S11).
4. **Bras.** Ancien bras C (mélange uniforme de moniteurs entraînés comme A, trajectoire propre) retiré : il mêlait l'effet des poids et celui des moniteurs ; remplacé par C1 (mêmes moniteurs que B, poids uniformes). Ajout de C2 et C3 (CM-03).
5. **Plus aucun changement de conception** depuis `gel-conception-arene-melange-v2.md` (empreinte ci-dessus, consignée au journal avant les pilotes) : le code des pilotes est le code remis (empreinte identique), les seuils recommandés et les prédictions chiffrées sont les seules choses tirées des pilotes.
6. Pilotes du brouillon 1 (`essai-pilote-racine-essai-v1.json`, `…-v2.json`) : conservés, non employés pour la puissance de la v2.

## Critères de lecture gelés

Un sous-agent neuf (R13) applique ces tables telles qu'écrites. Chaque table se lit **de haut en bas ; la première ligne vraie décide** ; la dernière est le complémentaire. Notations, pour un contraste à δ fixé : est = moyenne des écarts appariés ; qX = quantile X du rééchantillonnage (20 000 tirages) ; **B2** = [q0,00625 ; q0,99375] (Bonferroni sur 2 δ) ; **B8** = [q0,003125 ; q0,996875] (Bonferroni sur 8 tests) ; **E8** = [q0,00625 ; q0,99375] (intervalle de l'équivalence au niveau 0,05/8 par côté).

**V0** = aucune condition de la liste d'arrêt ∧ nombre de tâches exécutées = 2 × N (S4) ∧ racines du manifeste = RACINE et RACINE_TENUE ∧ empreintes du code, de la configuration et de la bibliothèque = celles du texte scellé ∧ une seule invocation ayant écrit des résultats (au plus une reprise complète après un arrêt externe consigné, § Plan 5).

**Déclencheurs d'audit (R4), symétriques** — un seul déclencheur suffit :
1. **Contradiction de la branche prédite, dans les deux sens** : le § Prédiction B donne pour chaque contraste un signe et une classe prédits. Déclenchent l'audit : (a) une classe observée du signe opposé au signe prédit (prédit + : « X > B » ou « X ≳ B » ; prédit − : « B > X » ou « B ≳ X ») ; (b) une classe prédite « ≈ » et observée « B > X » ou « X > B » ; (c) la plomberie prédite « mécanisme exercé » et observée autrement (Table 1 ligne 5 ou 6 : « H1 réfutée » déclenche le même audit que « trop beau ») ; (d) (ii) prédit négatif et borne basse B2 > 0 dans un δ ; (e) Table 4 prédite « HP réfutée » et observée « HP confirmée » ou « HP dépend de δ ».
2. **Trop beau / trop mauvais, calibré** (S10) : pour un bras et un δ, la moyenne de V en décision hors de la plage [minimum ; maximum] des V par tâche du pilote (§ Seuil, S10) ; plus la règle de Lazar : moyenne de V(B) ≥ 0,99 dans un δ.
3. **Règle de Lazar** (« si le mélange uniforme égale le mélange d'équilibre, audit ») : Δ(B, C1) classé « ≈ » dans un δ ; ou V(B) = V(C1) au bit près sur une tâche ; ou poids finaux de B égaux à l'uniforme (à 10⁻⁶) sur une tâche.
4. **Mélange dégénéré** : poids finaux de B purs (un poids ≥ 1 − 10⁻⁹) sur plus de la moitié des tâches d'un δ.
5. **Optimiseur** : moyenne de (V standard − V renforcé) > 0,01 pour un bras dans un δ ; ou un contraste des Tables 1 et 3 qui diffère de plus de 0,01 entre attaquant standard seul et attaquant renforcé seul.
6. **Jeu restreint** : moyenne de (valeur du jeu restreint de B − V(B)) < −0,01 dans un δ.
7. **Capacité non exercée** : V(D) = V(A) au bit près sur toutes les tâches d'un δ.
8. **Dérive des fausses alertes** (CM-17) : |moyenne des fausses alertes finales d'un bras − α| > 0,001 dans un δ (dix fois l'erreur-type attendue à N = 100).

**Contenu de l'audit** : relecture du code par un sous-agent neuf ; rejeu de 10 tâches sur RACINE_ESSAI (20261293) avec un attaquant quatre fois plus fort (départs et itérations) ; vérification que B déploie les poids du programme linéaire, C1 l'uniforme, C2 les poids de Dirichlet de sa graine, C3 le « ou » des moniteurs de B ; journal des poids. **Issue** : « artefact trouvé » si et seulement si le rapport scellé constate une erreur de code, un chemin non exercé, ou un contraste des Tables 1 à 3 qui change de plus de 0,01 sous l'attaquant renforcé ; sinon « pas d'artefact ».

### Table 1 — contrôle de plomberie, Δ(B, A) sur (iii)

| # | Condition | Verdict |
|---|---|---|
| 0 | V0 fausse | **non concluant** ; aucune lecture |
| 1 | un déclencheur d'audit est présent et l'audit n'est pas rendu | **non concluant (audit en attente)** |
| 2 | audit rendu, artefact trouvé | **non concluant** ; version nouvelle du préenregistrement |
| 3 | dans un δ, la moyenne de V est ≤ 2α pour les six bras | **non concluant** : jeu dégénéré |
| 4 | est ≥ S1 ∧ borne basse B2 > 0, aux deux δ | **mécanisme exercé** (B bat la défense unique) |
| 5 | borne haute B2 < 0 dans au moins un δ | **le mélange perd contre la défense unique** (au moins un δ) |
| 6 | sinon | **mécanisme non démontré** (gain sous S1 ou imprécis dans au moins un δ) |

Les Tables 2 à 4 se lisent si la Table 1 rend la ligne 4, 5 ou 6 (lignes 0 à 3 : le run ne dit rien). Motif : la plomberie n'est plus la question ; un mélange qui ne bat pas A reste comparable à ses témoins, et la phrase de synthèse recopie toujours la Table 1. Les lignes 5 et 6 contredisent la prédiction : elles ont déclenché l'audit (déclencheur 1), donc elles ne se lisent qu'après un audit rendu « pas d'artefact ».

### Table 2 — non-régression sur (ii), Δ(B, A) (bornes B2) ; lecture sans seuil rapportée à côté

| # | Condition | Lecture |
|---|---|---|
| 1 | borne haute < −S5 dans au moins un δ | **régression avérée au-delà de la tolérance** |
| 2 | borne basse > −S5 aux deux δ ∧ borne haute < 0 dans au moins un δ | **régression démontrée, sous la tolérance** |
| 3 | borne basse > 0 aux deux δ | **amélioration sur (ii)** |
| 4 | borne basse > −S5 aux deux δ | **sans régression à S5 près** |
| 5 | sinon | **régression non exclue (imprécis)** |

**Lecture sans seuil**, recopiée dans tous les cas : signe, estimation et intervalle B2 de Δ(B, A) sur (ii) à chaque δ.

### Table 3 — classement de chaque témoin X ∈ {C1, C2, C3, D} à chaque δ, Δ(B, X) sur (iii)

Marge m(δ) = S6 (une valeur par δ, § Seuil). Dans cet ordre, la première condition vraie :

| Classe | Condition | Sens |
|---|---|---|
| « B > X » | borne basse B8 > m(δ) | B bat X d'un effet d'intérêt |
| « X > B » | borne haute B8 < −m(δ) | X bat B d'un effet d'intérêt |
| « ≈ » | E8 ⊂ ]−m(δ) ; +m(δ)[ | équivalents à la marge près |
| « B ≳ X » | borne basse B8 > 0 | B meilleur, effet d'intérêt non démontré |
| « X ≳ B » | borne haute B8 < 0 | X meilleur, effet d'intérêt non démontré |
| « ? » | sinon | non tranché (imprécis) |

Sens de chaque témoin : C1 = rôle des **poids d'équilibre** à moniteurs identiques ; C2 = poids d'équilibre contre **poids quelconques** ; C3 = **tirage au hasard** contre **agrégation déterministe** des mêmes moniteurs ; D = mélange contre **un moniteur unique plus riche** (paramètres égaux, autre famille de fonctions, trajectoire propre).

### Table 4 — hypothèse principale HP (« B bat les témoins à capacité égale »)

Statut à chaque δ, dans cet ordre : « tenue » si les quatre témoins sont « B > X » ; « réfutée (un témoin fait mieux) » si un témoin au moins est « X > B » ; « réfutée (équivalence) » si un témoin au moins est « ≈ » ; « non tranchée » sinon.

| # | Condition | Verdict |
|---|---|---|
| 1 | « tenue » aux deux δ | **HP confirmée** |
| 2 | « réfutée » (l'une ou l'autre forme) aux deux δ | **HP réfutée** |
| 3 | « tenue » à un δ, « réfutée » à l'autre | **HP dépend de δ** |
| 4 | sinon | **HP non tranchée** |

**Phrase de synthèse** (écrite par le lecteur R13 en recopiant, sans rien omettre) : « Table 1 : … ; Table 2 : … (sans seuil : Δ(B, A) sur (ii) = est [B2] à δ_bas, est [B2] à δ_haut) ; Table 3 : C1 δ_bas …, δ_haut … ; C2 … ; C3 … ; D … ; Table 4 : … (statut par δ) ; déclencheurs d'audit : … ; issue de l'audit : … ». Les huit classes de la Table 3 sont toujours recopiées : aucune lecture de la Table 4 ne masque un témoin. Les mesures descriptives sont rapportées avec leur intervalle, sans verdict.

## Liste d'arrêt

Chaque garde du code (52 sites `raise GardeArret`, chacun avec un motif unique) a un essai qui la provoque par son motif et un cas sain ; l'essai `test_chaque_garde_a_son_essai` vérifie mécaniquement, par l'arbre syntaxique du code, qu'aucune garde n'est sans essai (CM-08). Fichier d'essais : `essais/test_arene_melange_v2.py`.

| Condition | Action | Garde et essai (R5 : cas sain et artefact, motif vérifié) |
|---|---|---|
| Lancement en décision sans préenregistrement scellé, conforme, identifié (identifiant, RACINE, RACINE_TENUE, configuration canonique champ à champ, empreintes de la configuration, du code et des quatre fichiers de la bibliothèque, versions de numpy et scipy, N) | pas de départ ; aucune graine de décision | `autoriser_decision`, `exiger_prereg_arene`, `exiger_identite_prereg` ; `test_prereg_scelle_refus_pour_la_bonne_raison` (compagnon absent : motif « empreinte compagnon … absente » ; compagnon altéré : « ≠ scellée » ; scellé non conforme : « scellé mais non conforme » ; autre expérience : « sans l'identifiant » ; sain : autorisation posée), `test_identite_prereg_sain_et_artefacts` (dix artefacts, un par motif), `test_decision_refusee_brouillon2_pour_la_bonne_raison` |
| Graine tirée d'une racine de décision sans autorisation (appel direct compris) ; processus de travail sans préenregistrement | arrêt | `gen`, `_travail` ; `test_gen_garde_racine_de_decision`, `test_travail_refuse_racine_de_decision_sans_prereg` |
| Hors décision : racine de décision, racine du brouillon 1, ou racine des tenues égale à la principale | arrêt | `exiger_racines_essai` ; `test_racines_essai_sain`, `test_racines_essai_artefact`, `test_cli_essai_refuse_racines_interdites` |
| Configuration incohérente (δ non fixés ou non croissants, effectifs non multiples de K, κ hors ]0 ; 1[, fractions de courbe invalides, oracle inconnu) | arrêt | `exiger_config` ; `test_config_sain_et_artefacts` |
| Fichier de sortie existant ou apparu pendant l'exécution (essai, calibrage) ; dossier de run existant (décision) | arrêt (R12) | `_exiger_absent`, `_ecrire_nouveau` ; `test_cli_refuse_d_ecraser` ; `creer_manifeste` (essais du dépôt) |
| Arbre git non propre au lancement de décision | arrêt | `creer_manifeste` (essais du dépôt `tests/test_manifeste.py`) |
| Programme linéaire non résolu ; valeurs primale et duale différentes de plus de 10⁻⁷ ; matrice de gains non finie, hors [0 ; 1] ou non bidimensionnelle | arrêt | `resoudre_jeu` ; `test_jeu_sain`, `test_jeu_solveur_artefacts` (solveur simulé en échec, valeur duale décalée), `test_jeu_artefact` |
| Poids de mélange négatifs, non finis ou de somme ≠ 1 | arrêt | `exiger_poids` ; `test_poids_sain_et_artefact` |
| Loi d'attaque non finie, hors de la boîte, ou à distance > δ après projection | arrêt | `exiger_admissible` ; `test_admissibilite_sain_et_artefact` (trois motifs) |
| Nombre d'échantillons non multiple de K | arrêt | `echantillonner` ; `test_echantillonnage_stratifie` |
| Paramètres de moniteur non finis ; scores propres non finis ; variance nulle ; moniteur non calibré | arrêt | `Moniteur` ; `test_moniteur_gardes` (quatre motifs) |
| « Ou » déterministe sur un moniteur non linéaire, ou score propre de variance nulle | arrêt | `ou_deterministe` ; `test_ou_deterministe_sain_et_artefacts` |
| Maxout sans graine ; entraînement logistique ou par détection non fini ; oracle inconnu | arrêt | `entrainer` ; `test_entrainement_gardes` (optimiseur simulé non fini) |
| Aucun départ de l'attaquant au point fini (une réponse) ; part de départs non finis > 5 % dans une tâche | arrêt | `meilleure_reponse`, `exiger_departs_finis` ; `test_meilleure_reponse_departs_non_finis` (un sur deux : compté, point rendu ; tous : arrêt), `test_garde_departs_finis` |
| Taux de fausses alertes d'une défense finale hors de α ± 0,005 (S9) | arrêt | `exiger_fpr` ; `test_garde_fausses_alertes_sain_et_artefact` |
| Part d'entraînements non convergés > 5 % dans une tâche | arrêt | `exiger_convergence` ; `test_garde_convergence_et_identite_tour0` |
| Moniteur du tour 0 non reproductible bit à bit | arrêt | `exiger_meme_moniteur` ; `test_garde_convergence_et_identite_tour0` |
| Temps processeur d'une tâche > 600 s (S8) | arrêt | `exiger_plafond` ; `test_plafond_de_temps_processeur` |
| Bras ou témoin inconnu | arrêt | `trajectoire`, `defense_temoin`, `executer_tache` ; `test_bras_inconnus` |
| Calibrage sans δ satisfaisant la règle | arrêt (pas de pilote) | `choisir_deltas` ; `test_choisir_deltas` |
| Ligne de base du coût trop basse (κ × base < 2α) | mesure « non définie » pour ce bras et cette tâche, comptée et rapportée par δ ; jamais remplacée | `cout_contournement` ; `test_cout_contournement_ligne_de_base_et_bissection` |
| Temps de mur total > S8 | arrêt par `timeout` externe, consigné ; reprise selon § Plan 5 (a) ; **contrôle externe non couvert par les essais du code** | — |
| Reproductibilité : deux exécutions d'une même tâche diffèrent hors temps mesurés | constat d'essai (pas une garde d'exécution) | `test_reproductibilite_bit_a_bit_et_temoins`, `test_ordre_des_bras_sans_effet` |
| Nombre de tâches ≠ 2 × N ; plusieurs invocations hors § Plan 5 (a) ; paramètre changé après une lecture | V0 fausse ; non concluant | contrôle du lecteur R13 (manifeste unique, horodatage) |
| Appel de modèle, réseau, dépense | arrêt (devis et GO exigés) | — |
| Lecture d'un résultat de décision avant scellement | arrêt et consignation (R1) | — |
| numpy < 1.25 | arrêt (R9) | `exiger_numpy_minimal` (essais du dépôt) |
| Marqueur de gel restant, ou contre-lecture sans ses deux empreintes | pas de scellement | validateur `problemes` ; `test_brouillon2_non_conforme_au_validateur_et_identite_du_code` |
| Ligne de gel absente de `registres/decisions.md`, ou valeurs différentes du texte ; remarques de contre-lecture non traitées | pas de scellement ; contrôle manuel pour S1, S2, S3, S5, S6, S10 (seuils de lecture) ; les seuils qui sont des champs de configuration (S4, S7, S8 interne, S9, S11, S12, S13, S14) sont comparés **par le code** au bloc de configuration | `exiger_identite_prereg` |

## Rôles

- Auteur du brouillon 2 et du code v2 : sous-agent neuf Opus 5.5 (lignée conv-audit), qui n'a écrit ni le brouillon 1 ni le code v1.
- Contre-lecteur du brouillon 2 (R2) : un sous-agent neuf **d'un autre modèle**, qui n'a écrit ni ce texte ni le code ; fichiers à lui donner explicitement : ce brouillon, `arene_melange_v2.py`, `essais/test_arene_melange_v2.py`, `calcul-puissance-arene-melange-v2.py` et sa sortie, `gel-conception-arene-melange-v2.md`, `journal-pilotes-arene-melange-v2.txt`, `calibrage-deltas-arene-melange-v2.json`, les deux pilotes v2, `archive-observation-oracle-v1.py` et sa sortie, `LISEZMOI-arene-melange-v2.md`, la contre-lecture du brouillon 1, le brainstorm. Points à juger en priorité : la règle de choix des δ et son application ; les marges relatives (S6) et la correction de Bonferroni ; la prédiction à deux branches ; l'ordre « principe puis observation » de S13 ; le « ou » déterministe C3 comme témoin.
- Lecteur de porte (R13) : sous-agent neuf, ni auteur ni contre-lecteur ni analyste ; applique les Tables 1 à 4 ; son verdict est scellé puis soumis à Lazar.
- Lazar : gèle S1 à S14 ; donne le GO de l'exécution de décision (processeur, aucune dépense).

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf Sonnet 5.5 ; brouillon relu : `preenregistrement-arene-melange-equilibre-v1-brouillon1.md` `5129b8c26d384e92015142e6d80c1d29f922210975fc297ec487efab070284ce` ; rapport : `contre-lecture-arene-melange-v1-brouillon1.md` `3721865417495678475ab995d43a3e56dd1b3b1df7b147a218f6ce9b0bc5bd1f`. Verdict : « présentable après corrections ». Traitement de chaque remarque :

| Id | Traitement | Où dans ce brouillon |
|---|---|---|
| CM-01 | **Accepté**, six conditions : (1) les trois exécutions intermédiaires et les quatre combinaisons oracle × seuil sont déclarées ; l'observation est archivée par reproduction (`archive-observation-oracle-v1.json`) ; (2) principe d'abord, observation en note ; (3) portée conditionnelle à l'oracle, A renommé « défense unique réentraînée, même oracle » (ce n'est pas le protocole de Bailey) ; (4) pilote logistique complet, 48 tâches, prédiction signée avant ; (5) tout recalculé sur la racine fraîche 20261293 / 20261294 ; (6) gel avant les pilotes, aucun changement après. Même traitement pour le seuil de contournement (relatif, garde de ligne de base, courbe). | § Hypothèse (S13), § Plan 6, § Prédiction P-L1 et P-L2, S13, S14 |
| CM-02 | **Accepté** : B > A devient un contrôle de plomberie (Table 1) ; l'hypothèse principale est « B bat les témoins à capacité égale » (Tables 3 et 4) ; la synthèse recopie toujours les huit classes. | § Hypothèse, § Critères |
| CM-03 | **Accepté** : témoins C1, C2, C3 sur les neuf moniteurs mêmes de B, en plus de D ; prédictions signées par contraste et par δ ; ancien C retiré (remplacé par C1). | § Plan 2, § Prédiction |
| CM-04 | **Accepté** : δ par une règle écrite avant, sur A seul, sur une racine de calibrage distincte ; marges relatives (fraction ρ de l'effet de plomberie du pilote, plancher S1/2) ; « B > X » exige une borne basse au-dessus de la marge, non de zéro. | S6, S11, Table 3 |
| CM-05 | **Accepté** : taille par δ et sous chaque hypothèse nulle (e = 0 ; e = S1) ; règle nommée « pertinence et significativité ». | Résumé, S2 |
| CM-06 | **Accepté** : S5 recommandé par principe (S5 = S1, symétrie) ; lecture sans seuil recopiée ; « pas un gain net » et « choix sensible » retirés ; ligne « régression démontrée sous la tolérance » ajoutée. | S5, Table 2 |
| CM-07 | **Accepté** : déclencheur sur toute contradiction de la branche prédite, dans les deux sens (plomberie comprise) ; « trop beau / trop mauvais » calibré sur la plage du pilote par bras et par δ ; règle « V(B) ≥ 0,99 » gardée. | § Critères, S10 |
| CM-08 | **Accepté** : 52 gardes, chacune avec un essai qui la provoque par son motif et un cas sain ; contrôle mécanique d'exhaustivité ; essais du scellement sans compagnon, compagnon altéré, non conforme, autre expérience. | § Liste d'arrêt |
| CM-09 | **Accepté** : statut et itérations de chaque départ SLSQP consignés ; départs non finis comptés, garde à 5 % par tâche ; réponses à la limite d'itérations comptées. | § Métrique (contrôles), § Liste d'arrêt |
| CM-10 | **Accepté** : seuil relatif κ, garde de ligne de base, parts censurées et non définies rapportées par δ et par bras, courbe V(δ'), non-monotonie comptée, bissection dans l'encadrement. | § Métrique, S14 |
| CM-11 | **Accepté** : « itéré tronqué » écrit, écart du jeu restreint rapporté par δ ; équilibres non uniques : déclaration (sommet de HiGHS à version de scipy fixée), pas de règle de choix. | § Plan 2, § Métrique |
| CM-12 | **Accepté** : règle de reprise (cause externe : une reprise ; garde interne : non concluant). | § Plan 5 |
| CM-13 | **Accepté** : tables réécrites, complémentaires, sans masquage ; essai d'exhaustivité sur 2 000 configurations ; motif écrit de l'ordre de lecture. | § Critères |
| CM-14 | **Accepté, en partie déclaré** : configuration canonique imprimée dans le texte et comparée champ à champ ; empreintes de la bibliothèque et versions vérifiées ; N comparé à `--instances` ; schéma des graines dans la configuration. Le champ « graines » ajouté par `creer_manifeste` ne peut pas être retiré sans modifier la bibliothèque : déclaré non employé. | Bloc d'identité, § Plan 3 |
| CM-15 | **Accepté** : garde dans `gen`, autorisation re-vérifiée dans chaque processus. | § Plan 3 |
| CM-16 | **Accepté** (déclaré) : biais défavorable à D. | § Plan 2 |
| CM-17 | **Accepté** : commit à remplir au gel (HEAD à l'écriture noté) ; V = minimum de deux estimations déclaré ; écart de fausses alertes entre bras rapporté et déclencheur de dérive à 0,001 ; confiances tirées des probabilités simulées, plafonnées à 0,95. | En-tête, § Métrique, § Critères, § Prédiction |
| CM-18 | Constat positif ; reproductibilité et absence de fuite de la racine de décision reconduites en v2 (essais). | — |

- **Contre-lecture 2** — À REMPLIR : sous-agent neuf d'un autre modèle (identifiant), empreinte de ce brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque (accepté, refusé et pourquoi).
