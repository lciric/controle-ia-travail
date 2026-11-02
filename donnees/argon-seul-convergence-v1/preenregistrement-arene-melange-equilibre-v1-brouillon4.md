# Préenregistrement — arène coévolutive synthétique : le mélange d'équilibre contre ses témoins, à nombre de paramètres égal (Q1), à classe de fonctions égale contre D et à moniteurs égaux contre C3′ (Q2) — v1 — BROUILLON 4 (non scellé)

**Statut : brouillon 4, non gelé ; vérification courte par un modèle autre qu'Opus ; puis gel des seuils par Lazar ; puis scellement ; puis calcul décisif.**

Identifiant : **PREREG-ARENE-MELANGE-EQUILIBRE-V1**. Tâche : piste 3 du brainstorm P-041 (« bras mélange contre défense unique » : un mélange d'équilibre de moniteurs passés répond-il à la non-convergence de la défense unique réentraînée de Bailey et collègues, arXiv `2412.09565` ?), décision de Lazar R-695, test (b), sur processeur ; brouillon 4 écrit après la contre-lecture 3 et la décision R-739. Pilote de **mécanisme** : aucun modèle de langage, aucun texte ; « l'attaquant » est un choix de paramètres dans une famille bornée de lois synthétiques.

- Auteurs : code v4, gel v4, calibrage et pilote v4 : rédacteur neuf Opus 5.5 (lignée conv-audit), coupé par la limite d'usage le 31 octobre vers 13:45 UTC ; **ce brouillon 4**, l'audit d'essai v4, l'assemblage du pilote, la sortie de puissance v4 et le LISEZMOI v4 : rédacteur de reprise Opus (lignée conv-audit), 1er novembre 2026. Aucun des deux n'a écrit les brouillons 1 à 3, les codes v1 à v3 ou une contre-lecture de ce pilote.
- Branche `canal/conv-audit-n04`. Date (UTC) : 2026-11-01, 08:02 (relevé `date -u`).
- Commit du code d'analyse : À REMPLIR au gel (commit qui contient `arene_melange_v4.py` à l'empreinte du bloc d'identité). Le code v4 au calibrage (`dcc3e0b9…`) est au commit `c34a06d7` et le code du pilote (`70c77fd5…`, celui du bloc d'identité) au commit `fd37ceb3`, commits de conv-audit ; le champ `commit` des manifestes de pilote (`0cd84636`) désigne un arbre qui ne contient pas le code exécuté : seule l'empreinte du code fait foi pour les pilotes ; la décision exige un arbre propre.
- Documents qui font foi (chemin + empreinte ; dossier `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/` sauf mention) :
  - `…/p-041-pont-vers-les-vrais-modeles-v1/brainstorm-malleabilite-et-arene-v1.md` — `08360a9402ff81d7d9146ed833d60e687f1be4d9acd0be3ab2867403dda8eb10` ; `…/p-041-pont-vers-les-vrais-modeles-v1/reponse-pont-p041-vrais-modeles-v1.md` — `e98d9f5a0ccbf6a77675fc922b318eec67d4838acf3b1e0ea8657b79928155a3` ;
  - brouillon 1 — `5129b8c26d384e92015142e6d80c1d29f922210975fc297ec487efab070284ce` ; contre-lecture 1 — `3721865417495678475ab995d43a3e56dd1b3b1df7b147a218f6ce9b0bc5bd1f` ; brouillon 2 — `622e50d2ad961654b6daaa96d76a94f6dfd2d67188d9f7af199979359c0a1891` ; contre-lecture 2 — `c6751de38ca84f716d424bc34dccd4103757423932204011a65136bd861cc427` ;
  - brouillon 3 `preenregistrement-arene-melange-equilibre-v1-brouillon3.md` — `3ac8fe1fd1ee4cdb6ebc904a739f8098226703b02b6c0be428e2a572449dced0` ; contre-lecture 3 `contre-lecture-arene-melange-v3-brouillon3.md` — `7ccc1460d6925fb1c743cb099a4490fcca2c7146c99ec4098e49234bb15dc236` ; gel v3 — `25035088a36742db86c3b6be818e5c97fabd8dd48c1f9e56934fce15e9f09506` ; sortie de puissance v3 **(M3)** — `00a2234972c7bc0f0138a5c3e2c6b9fc1c6810b7c888b1b91342aecd10e434e5` ; pilote v3 — `e171e303330e47195757a9855a55181aea1bf1f75078fa9c6c7891033221427d` ;
  - décision **R-739** de `registres/decisions.md` (Lazar, 31 octobre 12:02 UTC : « tranche-les » ; conv-audit tranche Q2 gardée, δ recalibrés, S18 = 0,10, N = 100, délai externe 9 000 s) ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` — `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`.
- Code et sorties v4 (même dossier) :
  - `gel-conception-arene-melange-v4.md` — `9e1f25aeaf1c992e96f8d2d66acab7ca9028d498720461cbccaa87f38d23568d` (racines neuves, règle de recalibrage, règles nouvelles, prédictions du pilote v4, écrits **avant** tout calcul v4 ; empreinte épinglée dans le code) ;
  - `arene_melange_v4.py` — bloc d'identité ; `essais/test_arene_melange_v4.py` — `2adcf876a09a23d151182a0edeccb5e5a7338a004bed7490f9f3a24dcc1013c0` ;
  - `calibrage-deltas-arene-melange-v4.json` — `622c3bb448650c6ce07405534c8ea5defba3a89dcea8481ccd2c23156a70eb31` ;
  - pilote v4 en deux lancements : `essai-pilote-arene-melange-v4-detection-instances-00-05.json` — `963441f8456436bb046c26c851a5c794ddfdd1967d6d5f3dcdcd670e6b858bcc`, `…-instances-05-24.json` — `11b31596bb360a00e35be191900f966ff71599d0f18757a4af7153901cf76171` ; leur union `essai-pilote-arene-melange-v4-detection.json` — `4d1fb23f0c72de79270609fa6516020f71611e54210dc1a02059c3c67db36b8e` (script `assembler-pilote-arene-melange-v4.py` — `406db1c3de37f4d76df809ffdf26231b7fcfaf0659e9296563cbd720fbfb0832`) ;
  - `audit-essai-arene-melange-v4.json` — `528b5cd4f68b48812895a39ecd7b249cd3e9dffdb888f14e6244486dc3102ead` (instances 0 à 4 du pilote, aux deux δ : 10 tâches) ;
  - `calcul-puissance-arene-melange-v4.py` — `cf5543a76842a81f77fd381e9f08dd7ef876aa1ddc289a5cf06f3edf5a538031` ; sa sortie `calcul-puissance-arene-melange-v4-sortie.txt` — `45a7fe3b56d80f571ffbaf02203fe1c9993d7aa162a1e0161aeed289decb8428`, désignée **(M4)** ;
  - journaux `journal-pilotes-arene-melange-v4.txt` — `a69e4ceff41f78773517c778ca30c9caf456a8078db46cb2f4db37519643b218` (code, calibrage, lancement du pilote) et `journal-pilotes-arene-melange-v4b.txt` (suite) — empreinte au LISEZMOI v4.
- Codes v1 à v3 et leurs configurations : cités seulement abrégés (`6402dc6b…`, `6685585f…`, `8e1e651b…`, `1d7544e6…`, `88c87818…`, `02db9c91…`), pour qu'aucun de ces codes, qui cherchent leurs empreintes complètes, ne puisse partir sur ce texte (essai).

Tout nombre de ce texte vient de (M4) (section citée, par exemple [M4 § 3b]), du calibrage v4, du pilote v4, de l'audit d'essai v4, du gel v4, ou des pièces v3 citées ; ou est un marqueur de gel. **Aucune lecture n'a été faite sur la racine de décision RACINE = 20261201 ni sur RACINE_TENUE = 20261202.**

### Bloc d'identité (vérifié par le code ; à régénérer par `arene_melange_v4.py identite` si le code ou la configuration change)

- Identifiant : PREREG-ARENE-MELANGE-EQUILIBRE-V1
- Racines de décision : RACINE = 20261201 ; RACINE_TENUE = 20261202
- Code : `arene_melange_v4.py` — 70c77fd5c0ec72b63ae4c10e1e6b2fc423aacfedce9a4a0792869d92c5a2ae61
- Configuration (empreinte de la forme canonique) : 3fbb27fc0824b7a9d13a0036c975c43e00e4dc7ece9f0231dfca7c0234785098
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

## Résumé pour Lazar

1. **Deux questions, inchangées.** Q1 : le mélange d'équilibre de moniteurs linéaires B bat-il ses témoins **à nombre de paramètres égal** (63) — C1, C2, C3, D ? Q2 : à **classe de fonctions égale**, le mélange d'équilibre B′ (maxouts à 9 unités) bat-il D (même classe, mêmes paramètres déployés par requête) et, **à moniteurs égaux**, C3′ (« ou » déterministe des moniteurs mêmes de B′ ; 511 paramètres déployés par requête, pas la même classe : CM3-07) ?
2. **Décisions R-739 appliquées** (Lazar a délégué, conv-audit a tranché ; choix **postérieurs** à la lecture du pilote v3) : Q2 gardée, lecture réécrite ; δ recalibrés sur 48 instances d'une racine neuve (20264101) par la règle écrite d'avance sur le seul bras A → **δ = (1,4 ; 1,6)** (au lieu de 1,4 ; 1,8) ; **S18 = 0,10, N = 100, délai externe 9 000 s**.
3. **Calibrage (A seul, 48 instances, moyenne de V(A) et erreur-type)** : 0,6 : 0,372 (0,018) ; 0,8 : 0,312 (0,018) ; 1,0 : 0,233 (0,019) ; 1,2 : 0,161 (0,016) ; 1,4 : 0,102 (0,013) ; 1,6 : 0,056 (0,011) ; 1,8 : 0,026 (0,006) ; 2,0 : 0,007 (0,002) ; 2,4 : 0,001 (0,0004). Le couple dépend de deux franchissements bruités (1,4 est à 0,15 erreur-type au-dessus de 10α ; 1,8 à 0,7 erreur-type sous 3α) : sous rééchantillonnage des instances, (1,2 ; 1,6) sort 43 %, (1,4 ; 1,6) 33 %, (1,4 ; 1,8) 23 %. Règle appliquée telle qu'écrite.
4. **Pilote v4 (racine neuve 20264201, 24 instances × 2 δ, 8 bras)** : Q1 réplique la v3 — B − A +0,128 / +0,139 ; B − C1 +0,020 / +0,021 ; B − C2 +0,040 / +0,036 ; B − C3 −0,194 / −0,144 ; B − D −0,234 / −0,180 : **Q1 réfutée** (C3 et D font mieux que B). Q2 — B′ − D +0,002 / +0,004 ; B′ − C3′ +0,007 / +0,011 ; poids de B′ **purs dans 71 % et 58 % des tâches** : **Q2 « non exercée »** sous la règle gelée.
5. **Ce que veut dire « Q2 non exercée » (R-739, CM3-02)** : à classe de 9 unités, le jeu restreint a presque toujours un équilibre pur — et cette pureté est **forcée par le jeu** (sur toutes les tâches pures, le plus petit poids maximal parmi les stratégies d'équilibre du défenseur vaut 1) — et B′ ≈ D. C'est un **plafond de la classe de moniteurs** dans ce monde : il ne prouve pas que le tirage au hasard est inutile. Le moniteur qui porte le poids pur n'est **pas** le dernier entraîné : moniteur du tour 2, 3 ou 4 dans 14 tâches pures sur 17 (δ 1,4) et 12 sur 14 (δ 1,6), le dernier dans 2 et 1. À classe linéaire, tirer au hasard parmi les mêmes moniteurs bat A (C1 − A ≈ +0,11), mais la richesse de la classe fait beaucoup plus (D − A +0,36 / +0,32) : le tirage s'y comporte en substitut partiel de capacité.
6. **Condition d'application (CM3-03)** : A ne progresse pas (I1 +0,002 / −0,001) ; son taux de retours I3 vaut 0,90 et 0,94 contre une **valeur nulle de 0,735** (déplacements échangeables) : écart +0,17 [B2 +0,10 ; +0,23] et +0,21 [+0,16 ; +0,25] : **retours au-delà du hasard** (Table 5, ligne « cycle »). B est à la valeur nulle (+0,00 / +0,02) ; D et B′ nettement dessous (−0,23 à −0,38). A reste bas au δ haut (V(A) 0,036 au pilote, 3,6 α) : la Table 5 y discrimine peu.
7. **Audit indépendant réécrit (CM3-01, CM3-04)** : 10 tâches de la décision **par δ** (20), A compris ; artefact si |écart moyen| > 0,01 (moitié de la marge) **ou** changement de classe démontré (écart > t × erreur-type). Audit d'essai v4 (5 tâches par δ du pilote) : aucun drapeau (i) ni (ii) ; écarts moyens |c̄| ≤ 0,0011, écart maximal par tâche 0,0097 ; aucune classe ni ligne de la Table 5 changée sur l'analyse du pilote entier [M4 § 8]. Taux de fausse alerte simulé du critère : 0,002 avec les écarts d'essai centrés, 0,011 avec un bruit d'écart-type double ; repli non déclenché ; puissance contre un écart systématique de 0,010 sur B′ − D : 0,76, de 0,015 : 1,00. [M4 § 8b].
8. **S10 corrigé (CM3-05)** : bande = moyenne pilote ± 3 × écart-type × √(1/24 + 1/N) (Bonferroni sur 16 bandes) ; fausse alerte simulée sur les 16 bandes : règle v3 0,323 ; k = 3 **0,095** (> 0,05) ; d'où le **repli k = 4**, fixé au gel v4 avant le pilote : 0,025. [M4 § 7].
9. **Temps** : 60,7 s de processeur par tâche (maximum 87,3 s) [M4 § 5] ; N = 100 → 202 min de processeur, **101 min de mur sur 2 cœurs à efficacité 1** (67 % du délai de 9 000 s). Le délai tient si l'efficacité (temps processeur / (mur × 2)) dépasse **0,67**. Mesurée dans cette session sur une machine partagée par d'autres sessions : 0,52 (pilote v4, deux lancements simultanés) et 0,51 (audit d'essai), soit ≈ 3 h 15 de mur : **le délai serait dépassé** et le run perdu entier (aucun point de reprise partiel) ; au pilote v3, 0,80 (126 min, 84 % du délai). **Condition de lancement écrite : machine sans autre calcul lourd** ; à défaut, option pour Lazar : N = 80 (81 min à efficacité 1) ou `timeout 12600`. Audit de la décision (20 tâches) : 40 min à efficacité 1, 79 min à 0,51.
10. **Seuils** : S1–S17 à geler par Lazar (recommandations inchangées sauf S10, S11, S17) ; S4 (N = 100), S8 (9 000 s) et S18 (0,10) sont **décidés** (R-739). Portée : tout résultat est local (monde gaussien, classe d'oracle, δ, T) ; il ne réfute ni ne confirme la piste 3 sur de vrais moniteurs.
11. Avant scellement : vérification courte par un modèle autre qu'Opus, gel des seuils par Lazar, empreintes recalculées si une valeur change.

## Ce qui change par rapport au brouillon 3

| Point | Brouillon 3 | Brouillon 4 | Origine |
|---|---|---|---|
| δ | (1,4 ; 1,8), calibrage v2 sur 12 instances | **(1,4 ; 1,6)**, recalibrés sur 48 instances de la racine neuve 20264101 / 20264102, bras A seul, règle écrite au gel v4 avant tout calcul ; une seule ligne de code changée (`DELTAS_V4`) | R-739 (2), CM3-16, CM2-06 |
| S18 | recommandation 0,10, configuration à 0,05 | **0,10 décidé** ; dans la configuration dès le premier calcul v4 (plus de rupture de chaîne d'empreinte, CM3-09) | R-739 (3) |
| N, délai | recommandations | **N = 100, `timeout 9000` décidés** ; projection de temps refaite (CM3-10) | R-739 (3) |
| Lecture de Q2 | « la question du tirage ne se pose pas » ; « le dernier moniteur domine » | plafond de la classe de moniteurs ; explication contredite retirée ; indice du moniteur dominant ; pureté forcée par le jeu (programme linéaire de non-unicité) ; B′ − D et B′ − C3′ selon la pureté ; ce que la décision pourra et ne pourra pas conclure | R-739 (1), CM3-02 |
| Titre, C3′ | « à classe de fonctions égale… bat D et C3′ » | « à classe égale contre D, **à moniteurs égaux** contre C3′ » ; dilution de C3′ déclarée | CM3-07 |
| I3 | sans valeur nulle | **valeur nulle 0,7345** (échangeabilité) ; I3 − nul lu avec son intervalle ; Table 5 réécrite (« cycle » = retours au-delà du hasard) ; I2 renommé « baisse de détection des attaques passées (oubli ou saturation) », recopié sans verdict ; H et I2 de B et B′ par moniteur | CM3-03 |
| Audit S17 | 5 tâches (instances 0 à 4), B, C3, D, B′, C3′ ; artefact = signe changé ou écart > 0,05 | **10 tâches par δ** (instances 0 à 9, 20 tâches) ; **A ajouté** (B − A, tours de A pour la Table 5) ; choix source et choix audit réévalués sur un même échantillon frais ; artefact = écart > m/2 = 0,01 ou changement de classe démontré ; taux de fausse alerte simulé, repli fixé d'avance | CM3-01, CM3-04, CM3-11 |
| Déclencheur 9 | P4, P5, P8 | **P1, P4, P5, P8, P10, P11** ; contrôle de non-unicité des équilibres pour P10 | CM3-04 |
| S10 | ± 5 é.-t./√N (≈ 36 % de fausses alertes sur 16 bandes) | ± 3 × é.-t. × √(1/24 + 1/N) ; taux simulé ; repli k = 4 fixé d'avance | CM3-05 |
| P10 | 0,998 | probabilité conditionnelle au pilote **et** avec son incertitude (loi bêta) | CM3-06 |
| Preuve de l'ordre | déclarations | gel v4 dans un commit de conv-audit (`f65feb1a`, 12:51 UTC) avant le code du calibrage (`c34a06d7`, 12:57 UTC) et avant le calibrage (13:05 UTC) ; empreinte du gel épinglée dans le code, qui refuse de partir sans lui | CM3-08 |
| Pureté | texte « ≥ », code « > » | « ≥ 1 − 10⁻⁹ » dans les deux | CM3-12 (c) |
| `MoniteurOu` | garde de variance absolue 10⁻¹² | garde relative : écart-type > 10⁻⁶ × max(1, \|moyenne\|) | CM3-15 |
| Racines | — | neuves, plage 20264001 à 20264999, gelées avant emploi ; toutes les racines déjà employées (brouillons 1 à 3, codes v1 à v3, contre-lectures 2 et 3) et la plage 20265001 à 20265999 d'une autre session refusées jusque dans `gen` | consigne, R9 |
| Témoins nouveaux | — | **aucun** : maxout unique de 73 unités non ajouté (diagnostic non opposable de la contre-lecture 3 : ne change rien ; coût) ; témoin « mode » et « ou » restreint au support de B′ laissés en options à Lazar | CM3-02, CM3-07 |
| Bras | — | A, B, C1, C2, C3, D, B′, C3′ calculent exactement comme en v3 (essai `test_bras_v3_inchanges`, champ à champ sur une même racine) | gel v4 § 3.9 |

## Ce que l'expérience n'autorise pas

- **Rien sur les vrais modèles** ni sur les moniteurs d'activations réels : ni Llama, ni les sondes de Bailey et collègues, ni la boucle à 70 tours. Le monde est une famille de lois que nous avons écrite (`reponse-pont-p041-vrais-modeles-v1.md` § 0).
- **A n'est pas le protocole de Bailey** : même oracle « détection » que les autres bras ; la non-convergence de A mesurée ici (Table 5) est une **analogie**, pas une reproduction.
- **Rien sur l'équilibre du jeu complet** : B et B′ sont des itérés du double oracle tronqué à 8 tours ; écarts « valeur du jeu restreint − V » au pilote v4 : B +0,019 / +0,024 ; B′ +0,004 / +0,004 [M4 § 6].
- **Q1 n'est pas « à capacité égale »** : B déploie 7 paramètres par requête, C3 et D les 63. Une réfutation de Q1 dit que la classe de fonctions déployée compte, pas que le tirage au hasard est inutile.
- **Q2 n'est pas « à paramètres égaux »** : B′ et D déploient la même classe (maxout à 9 unités, ≤ 63 paramètres par requête) ; B′ stocke 511 paramètres, D 63. **C3′ n'est pas de même classe que B′** (511 paramètres déployés par requête) : B′ − C3′ compare deux usages des mêmes moniteurs ; C3′ agrège aussi les moniteurs faibles des premiers tours et paie un seuil resserré (dilution).
- **B′ − D ne mesure pas le tirage seul** : B′ ajoute à D une sélection (maximin sur 9 moniteurs) et une distribution d'entraînement différente (stratégie d'équilibre de l'attaquant au lieu du mélange uniforme des attaques passées).
- **« Q2 non exercée » n'est pas « le tirage au hasard est inutile »** : c'est un plafond de la classe de moniteurs à 9 unités dans ce monde, à ces δ, à T = 8, contre un attaquant local.
- **Monde favorable au « ou » déterministe** : queues gaussiennes, moniteurs peu nombreux.
- Deux budgets seulement, choisis sur A seul ; A bas au budget haut (3,6 α au pilote).
- Aucune revendication d'antériorité ni de nouveauté (R8) ; références **SUPPOSÉ** sauf Bailey et collègues (lu sur PDF par session-depot, R-874, aucun chiffre repris).
- Aucun énoncé sur des moniteurs quadratiques, des réseaux profonds, d'autres dimensions, d'autres familles, ni un attaquant en boîte noire.
- (iii) est une **borne haute** de la valeur du jeu (l'attaquant est un optimiseur local), contrôlée par un attaquant indépendant (S17).
- Ni porte, ni dépense, ni modification de P-041.

## Portée d'une réfutation et d'une confirmation

- **Toute lecture est locale** : monde (gaussien, d = 6, K = 3), classe d'oracle du défenseur (linéaire pour B, maxout à 9 unités pour B′ et D), oracle « détection », δ ∈ {1,4 ; 1,6}, T = 8, attaquant local en boîte blanche.
- **Q1 réfutée** établit : dans ce monde, un « ou » déterministe des mêmes moniteurs linéaires et un maxout de même total font mieux que leur mélange d'équilibre. Elle ne réfute pas la piste 3 et ne dit rien du mélange à classe égale.
- **Q2 non exercée** (prédite) établit seulement : à classe de 9 unités, dans ce monde, l'équilibre du jeu restreint est presque toujours pur (pureté forcée par le jeu, pas un artefact du solveur), et B′ et D sont équivalents à 0,02 près ; le mélange atteint le **plafond de la classe**. Elle **ne pourra pas conclure** que le tirage au hasard est inutile, ni qu'il serait utile à une classe plus pauvre, ni qu'il le serait sur de vrais moniteurs. Elle **pourra** dire : à classe linéaire, le tirage est un substitut partiel de capacité (Table 1, C1 − A descriptif) ; à classe riche, la question du tirage est bornée par un plafond que ce monde atteint dès le tour 4.
- **Q2 réfutée** (B′ ne bat pas D ou C3′ d'au moins 0,02, avec un mélange exercé) établirait : à classe égale, dans ce monde, le tirage au hasard n'apporte pas d'effet d'intérêt. **Q2 confirmée** établirait le contraire. Les deux sont des surprises (déclencheur 1f).
- **Maxout unique de 73 unités** (même total que B′) : non ajouté. Le diagnostic de la contre-lecture 3 (racine 20269731 / 32, 8 instances par δ, non opposable) donne D73 − D = +0,003 / −0,001 et D73 − B′ = −0,002 / +0,003 : il ne change aucune lecture. Raisons de ne pas l'ajouter : diagnostic non opposable mais sans signal ; coût d'au moins un doublement du temps par tâche, hors du délai de 9 000 s décidé. Lacune déclarée.
- **Aucune lecture ne réfute ni ne confirme la piste 3 sur de vrais moniteurs.** Au mieux, elle indique quelle classe de moniteurs tester ensuite.
- **Condition d'application (Table 5)** : si A progresse, Q1 et Q2 ne disent rien d'une réponse à la non-convergence ; si A ne progresse pas, Q1 et Q2 portent sur un monde où la défense unique ne converge pas, dans ce monde seulement. La forme (« cycle » : retours au-delà du hasard) est lue contre la valeur nulle 0,735, jamais sur I3 brut.

## Antériorité (toutes SUPPOSÉ sauf mention, non lues sur PDF pour ce texte)

Double oracle (McMahan, Gordon et Blum 2003) ; réponse stratégique à une population de politiques (Lanctot et collègues 2017) ; défenses randomisées contre attaques adverses (Pinot et collègues 2020). Bailey et collègues, arXiv `2412.09565v2`, lu sur PDF par session-depot (R-874) : seule l'idée de la boucle est reprise ; **aucun chiffre** de ce papier n'est repris (R7).

## Hypothèse

Renvoi : brainstorm P-041 piste 3 (« la réponse correcte à une suite de meilleures réponses adverses est un mélange aux poids d'équilibre ») ; pistes 2, 4, 5 ; scores (i), (ii), (iii) de la fusion v3.

**Principe de l'oracle du défenseur (S13)**, inchangé depuis le brouillon 2 : l'oracle maximise le taux de détection lissé au seuil α, le même pour tous les bras ; A est donc une « défense unique réentraînée, même oracle », pas le protocole de Bailey.

**Historique déclaré** : Q2, B′, C3′ et les mesures de la condition d'application sont une bifurcation postérieure au pilote v2 (gel v3) ; les δ recalibrés, S18, N et le délai sont des choix postérieurs au pilote v3 (R-739, gel v4) ; aucun n'a lu une racine de décision.

- **Q1 (hypothèse principale 1)** : contre la meilleure réponse adverse finale, le mélange d'équilibre B bat chacun des témoins **à nombre de paramètres égal** — C1 (mêmes 9 moniteurs, poids uniformes), C2 (poids de Dirichlet), C3 (« ou » déterministe), D (maxout unique à 63 paramètres) — d'au moins m = S6, aux deux δ. H0 : pour au moins un témoin et un δ, non.
- **Q2 (hypothèse principale 2)** : le mélange d'équilibre B′ (maxouts à S16 unités) bat D (même classe, mêmes paramètres déployés par requête) et C3′ (« ou » des moniteurs mêmes de B′) d'au moins m = S6, aux deux δ. H0 : pour au moins un témoin et un δ, non. Si les poids de B′ sont purs (un poids ≥ 1 − 10⁻⁹) sur plus de la moitié des tâches d'un δ, Q2 est « non exercée » à ce δ (R5, chemin non exercé), lue comme un plafond de la classe (§ Portée).
- **Condition d'application** : la défense unique A ne progresse pas d'un tour à l'autre (I1) ; forme lue sur l'écart de son taux de retours à la valeur nulle (I3 − 0,7345).
- **Contrôle de plomberie PC** : B bat A sur (iii) aux deux δ. **Non-régression** : Δ(B, A) sur (ii), tolérance S5, lecture sans seuil recopiée.
- **Hypothèses de travail** : oracle du défenseur approché (seuil gaussien et deux départs pour les maxouts de D et B′) ; attaquant approché, contrôlé par un attaquant renforcé et par l'attaquant indépendant de S17 ; loi propre N(0, I) connue du code, pas des bras ; B et B′ itérés tronqués.

## Prédiction chiffrée et signe attendu

**La décision est une réplication de pilotes concluants** : les probabilités simulées ci-dessous sont **conditionnelles au pilote v4** pris pour vérité (24 instances) ; la décision peut encore surprendre, et toute surprise déclenche l'audit. Valeurs non opposables ; la décision se lit sur RACINE, jamais lue.

### A. Prédictions du gel v4 et leur sort au pilote v4

Gel v4 (`gel-conception-arene-melange-v4.md`, § 4, écrit à 12:43 UTC le 31 octobre, avant le calibrage et le pilote ; δ_bas, δ_haut = ceux que rendrait la règle) ; pilote v4 [M4 § 2, § 6] :

| Prédiction du gel v4 (avant) | Pilote v4, δ 1,4 ; δ 1,6 : moyenne [IC95, intervalle de confiance à 95 %] ou bornes B2 | Sort |
|---|---|---|
| V(A) ≥ 10α au δ bas (0,6) ; ≥ 3α au δ haut (0,5) | 0,0816 ; 0,0359 | **réfutée** au δ bas (8,2 α ; le calibrage donnait 0,102 ± 0,013) ; tenue au δ haut |
| B − A (iii) + (0,9) | +0,1283 [+0,1077 ; +0,1470] ; +0,1387 [+0,1272 ; +0,1493] | tenue |
| B − C1, B − C2 (iii) + (0,7) | B − C1 +0,0202 ; +0,0205 ; B − C2 +0,0402 ; +0,0356 | tenue |
| B − C3, B − D (iii) − (0,9) | B − C3 −0,1935 ; −0,1443 ; B − D −0,2341 ; −0,1795 | tenue |
| B − A (ii) − (0,8) | −0,0538 [−0,0784 ; −0,0274] ; −0,0580 [−0,0893 ; −0,0233] | tenue (signe) |
| \|B′ − D\| < 0,02 (0,8) | +0,0024 [−0,0043 ; +0,0085] ; +0,0042 [−0,0001 ; +0,0088] | tenue |
| B′ − C3′ + (0,7) | +0,0072 [+0,0015 ; +0,0127] ; +0,0114 [+0,0072 ; +0,0160] | tenue |
| part pure de B′ > 0,5 à au moins un δ (0,7) | 0,708 ; 0,583 | tenue |
| pureté forcée ≥ 0,8 parmi les tâches pures (0,7) | 1,000 (17/17) ; 1,000 (14/14) | tenue |
| A : \|I1\| < 0,02 (0,75) | +0,0020 B2 [−0,0029 ; +0,0069] ; −0,0005 B2 [−0,0046 ; +0,0034] | tenue |
| A : borne basse B2 de I3 − 0,7345 > 0 (0,7) | +0,1683 B2 [+0,0988 ; +0,2308] ; +0,2099 B2 [+0,1613 ; +0,2516] | tenue |
| D : I3 − 0,7345 < 0 (0,7) | −0,2831 ; −0,3804 | tenue |
| Temps par tâche 45 à 75 s (0,7) | moyenne 60,7 s, maximum 87,3 s | tenue (moyenne) |
| Audit d'essai : aucun drapeau (i) (0,9) | aucun drapeau (i) ni (ii) (10 tâches, 5 par δ) | tenue |
| Fausse alerte de S10 à k = 3 ≤ 0,05 (0,6) | 0,095 | **réfutée** ; repli k = 4 appliqué (0,025) |
| Fausse alerte de l'audit ≤ 0,05 (0,7) | 0,002 (écarts centrés) ; 0,011 (bruit doublé) | tenue |

Bilan v4 : 31 branches (hors lecture), **29 tenues, 2 réfutées** : V(A) ≥ 10α au δ bas (0,082 au pilote contre 0,102 ± 0,013 au calibrage : écart compatible avec le bruit de 24 instances ; δ_bas est à 0,15 erreur-type au-dessus de 10α) et fausse alerte de S10 à k = 3 (0,095 > 0,05 ; repli k = 4 appliqué par la règle écrite d'avance). Aucune règle n'a été changée après le pilote v4. Les prédictions des gels v2 et v3 et leur sort sont aux brouillons 2 et 3 (les 8 branches réfutées du gel v3 étaient toutes du côté de Q2 ; décompte corrigé, CM3-12 (b) : 26 tenues et 8 réfutées sur 34 branches, hors temps et lecture ; la clause « support ≥ 2 » non comptée à part). L'explication donnée au brouillon 3 de la pureté de B′ (« le moniteur entraîné contre l'équilibre de l'attaquant domine presque toujours les précédents ») est **retirée** : contredite au pilote v3 (contre-lecture 3) et au pilote v4 (indice du moniteur de poids maximal, résumé point 5).

### B. Prédictions pour la décision, par contraste et par δ

Classe prédite sous les valeurs recommandées (S1 = S5 = S6 = S15 = 0,02), estimation du pilote v4, probabilité simulée de la classe à N = 100 avec la règle réelle [M4 § 3, § 4], confiance (probabilité arrondie vers le bas à 0,05, plafonnée à 0,95), branche opposée (réfutation → audit, déclencheur 1). **Prédictions fermes : les signes, P1, P4, P5, P7, P8, P10 et P11.** Les classes de C1 (P2), C2 (P3), C3′ (P9) et la Table 2 (P6) ne sont pas prédites avec confiance.

| # | Contraste | δ | Signe | Classe prédite | Pilote v4 : moyenne | Probabilité simulée | Confiance | Branche opposée |
|---|---|---|---|---|---|---|---|---|
| P1 | B − A (iii), plomberie | 1,4 ; 1,6 | + | « mécanisme exercé » | +0,1283 ; +0,1387 | 1,000 | 0,95 | Table 1 ligne 5 ou 6 |
| P2 | B − C1 (iii) | 1,4 ; 1,6 | + | « B ≳ C1 » (non ferme) | +0,0202 ; +0,0205 | 0,990 ; 0,990 (« ≈ » 0,010 ; 0,003) | — | signe contraire (« C1 ≳ B », « C1 > B ») |
| P3 | B − C2 (iii) | 1,4 ; 1,6 | + | « B > C2 » (non ferme) | +0,0402 ; +0,0356 | 1,000 ; 1,000 | — | signe contraire |
| P4 | B − C3 (iii) | 1,4 ; 1,6 | − | « C3 > B » | −0,1935 ; −0,1443 | 1,000 | 0,95 | « B > C3 », « B ≳ C3 » |
| P5 | B − D (iii) | 1,4 ; 1,6 | − | « D > B » | −0,2341 ; −0,1795 | 1,000 | 0,95 | « B > D », « B ≳ D » |
| P6 | B − A (ii) | 1,4 ; 1,6 | − | Table 2 « régression avérée au-delà de la tolérance » (non ferme : à 24 instances, le pilote lit « imprécis ») | −0,0538 ; −0,0580 | 1,000 | — | borne basse B2 > 0 dans un δ |
| P7 | Q1 (Table 4) | — | — | « Q1 réfutée » (C3 et D) | — | 1,000 | 0,95 | « Q1 confirmée », « Q1 dépend de δ » |
| P8 | B′ − D (iii) | 1,4 ; 1,6 | ≈ 0 | « ≈ » | +0,0024 ; +0,0042 | 1,000 ; 1,000 | 0,95 | « B′ > D » ou « D > B′ » |
| P9 | B′ − C3′ (iii) | 1,4 ; 1,6 | + | « ≈ » (classe non ferme) | +0,0072 ; +0,0114 | 1,000 ; 1,000 | 0,95 (signe) | « C3′ > B′ », « C3′ ≳ B′ » |
| P10 | Q2 (Table 7) | — | — | « Q2 non exercée (au moins un δ) » | part pure 0,708 ; 0,583 | 1,000 conditionnel au pilote ; **0,990 avec son incertitude** (loi bêta, puis binomiale à N = 100 : δ 1,4 0,961 ; δ 1,6 0,748) [M4 § 4b] | 0,95 | « Q2 confirmée », « Q2 dépend de δ » ; « Q2 réfutée » (exercée) est aussi une surprise |
| P11 | Table 5 | 1,4 ; 1,6 | — | « A ne progresse pas, retours au-delà du hasard (cycle) » aux deux δ ; condition vérifiée | I1 +0,0020 ; −0,0005 ; I3 − 0,7345 +0,168 ; +0,210 | 1,000 | 0,95 | « A progresse » ; une autre forme à un δ |

Descriptives du pilote v4 (sans verdict) [M4 § 6] : (iii) par tour, A plat (0,072 → 0,066), B croissant (0,072 → 0,189), D et B′ croissants puis plats (≈ 0,40 dès le tour 4 ; plafond de la classe de 9 unités) ; nouveauté résiduelle au tour 8 de 0,151 (B′) à 0,199 (D) ; matrice H de A : rétention au décalage 0 de 0,37, au décalage 1 de 0,24 et 0,23 ; C1 − C2 +0,020 / +0,015 ; C3 − A +0,322 / +0,283 ; D − A +0,362 / +0,318 ; C1 − A (dérivé : B − A moins B − C1) ≈ +0,108 / +0,118 ; B′ − D selon la pureté : tâches pures +0,0021 (erreur-type 0,0034, n = 17) / +0,0038 (0,0036, n = 14), tâches à mélange réel +0,0031 (0,0084, n = 7) / +0,0047 (0,0026, n = 10) ; B′ − C3′ : pures +0,0107 / +0,0129, à mélange −0,0014 / +0,0093 ; indice du moniteur de poids maximal de B′ sur les tâches pures : tour 2 (4 ; 7), 3 (7 ; 0), 4 (3 ; 5), 5 (0 ; 1), 6 (1 ; 0), 8 (2 ; 1) ; poids de B jamais purs (support moyen 3,7 et 3,8) ; coût par contournement censuré à δ 1,4 pour B 0,46, D 0,38, B′ 0,38, C3′ 0,29 ; fausses alertes moyennes à 0,0002 de α au plus ; 3 entraînements non convergés sur 1 632 (au plus 2 dans une tâche) ; 0 départ non fini sur 69 918, tous au statut 0, aucune réponse à la limite ; V standard − V renforcé ≤ 0,0011 en moyenne par bras [M4 § 6].

**Lecture anticipée**, à ne pas confondre avec un résultat : si la décision réplique le pilote, (a) la défense unique ne progresse pas et ses attaques reviennent vers d'anciennes au-delà du hasard ; (b) un mélange d'équilibre de moniteurs linéaires la bat, mais un « ou » de ces moniteurs et un maxout de même total font beaucoup mieux (Q1 réfutée) ; (c) à classe de 9 unités, l'équilibre du jeu restreint est presque toujours pur et B′ ≈ D : le mélange atteint le plafond de la classe ; **la décision ne dira pas** si le tirage serait utile sous ce plafond (classe plus pauvre) ni hors de ce monde. Le tirage est un substitut partiel de capacité à classe linéaire (C1 − A, descriptif) ; la richesse de la classe guérit davantage (D − A). Conditionnel au monde, à l'oracle et aux budgets.

## Métrique

Notations : une **tâche** = (δ, instance) ; les deux δ partagent la loi cible d'une instance. Taux de détection d'une défense mixte {(m_i, p_i)} sur une loi Q : Σ_i p_i × part des échantillons de Q dont le score dépasse le seuil t_i de m_i ; seuils calibrés au quantile 1 − α de 20 000 échantillons propres communs (α = S9).

- **(iii), principale, V(bras)** : après T tours (S12), défense figée ; deux meilleures réponses sous la contrainte distance ≤ δ et la boîte : **standard** (12 départs tirés + départ vers l'origine + attaques passées de la trajectoire — celles de B pour C1, C2, C3, celles de B′ pour C3′ —, 512 échantillons de Monte-Carlo par composante, 100 itérations de programmation quadratique séquentielle par moindres carrés, SLSQP) et **renforcée** (48 départs, 200 itérations, plus la réponse standard) ; chacune évaluée sur 19 998 échantillons frais ; **V = la plus basse des deux détections**.
- **Écart apparié** Δ(X, Y) = moyenne sur les instances de V(X) − V(Y), à δ fixé.
- **Paramètres** : stockés et **déployés par requête** : B 63 et 7 ; C1, C2 63 et 7 ; C3, D 63 et 63 ; B′ 511 et ≤ 63 ; C3′ 511 et 511.
- **(ii) familles tenues à l'écart** : 50 lois par tâche tirées de **RACINE_TENUE**, deux sous-familles ; 3 999 échantillons par loi ; score = moyenne des 50 taux. **(i) familles vues** : descriptif.
- **Courbe V(δ')** et **coût par contournement** (piste 5), **nouveauté résiduelle** (piste 4) : comme au brouillon 2 ; descriptifs.
- **Condition d'application** (A : verdict ; B, D, B′ : descriptif) : matrice H, ligne s = moniteur déployé au tour s (0 … T ; pour B et B′, chaque moniteur un à un, pas la défense mixte), colonne t = attaque du tour t (1 … T) ; **I1** (progrès) = moyenne de (iii) aux tours 5–8 moins aux tours 1–4 ; **I2** (baisse de détection des attaques passées : oubli ou saturation, non distingués) = moyenne sur t = 1 … 7 de H[t, t] − H[8, t], recopié sans verdict ; rétention par décalage ; **I3** (retours) = part des tours t ≥ 3 où le cosinus du déplacement de l'attaque avec celui d'une attaque d'un tour ≤ t − 2 dépasse celui avec l'attaque du tour t − 1 ; **valeur nulle de I3** sous échangeabilité des déplacements = moyenne sur t = 3 … T de (t − 2)/(t − 1) = **0,7345** à T = 8 (simulation, 20 000 tirages de vecteurs gaussiens à 36 coordonnées : 0,7329 (erreur-type 0,0012) [M4 § 9]) ; l'indicateur lu est **I3 − 0,7345**. Intervalles par rééchantillonnage des instances.
- **Contrôles** : fausses alertes de chaque défense finale sur 20 000 échantillons propres indépendants ; valeur du jeu restreint de B et B′ ; V standard − V renforcé ; contrastes sous chaque attaquant seul ; poids finaux de B, B′, C2 (support, pureté, poids maximal, indice du moniteur de poids maximal) ; **plus petit poids maximal parmi toutes les stratégies d'équilibre du défenseur** du jeu restreint final (programme linéaire ; « pureté forcée » si ≥ 1 − 10⁻⁶) ; B′ − D et B′ − C3′ selon la pureté (tâches pures, tâches à mélange réel) ; statuts de l'optimiseur, départs non finis, réponses à la limite ; entraînements non convergés.
- **Attaquant indépendant (S17)** : par bras audité (A, B, C3, D, B′, C3′), optimiseur lourd (12 départs structurés, 100 départs tirés, attaques passées et finales, 1 024 échantillons, 300 itérations), puis stratégie d'évolution (1 + 12) sans gradient sur le taux dur, 400 générations, depuis la réponse lourde et depuis l'attaque finale standard. **Choix source** = la meilleure des deux réponses de la décision (standard, renforcée) ; **choix audit** = la meilleure du choix source et des trois réponses indépendantes (selon leurs évaluations propres ; égalité : le choix source est gardé) ; les deux choix sont **réévalués sur un même échantillon frais** de 19 998 points (graine commune : écart nul au bit si le choix ne change pas), ce qui retire le biais de sélection du minimum (CM3-01, point 3). Pour A, à chaque tour t, réponse renforcée contre le moniteur déployé au tour t ; (iii) audité du tour = minimum de (iii) du tour et de cette réponse sur un échantillon frais ; I1 et I3 recalculés.
- **Intervalles** : rééchantillonnage apparié des instances, 20 000 tirages, quantiles linéaires 0,3125 %, 0,625 %, 1,25 %, 2,5 %, 5 % et symétriques ; graines `SeedSequence(entropy=racine, spawn_key=(code_delta, code, 0, 0, 99))`.

## Seuil

**Les seuils S1 à S3, S5 à S7, S9 à S17 sont à geler par Lazar en une ligne datée de `registres/decisions.md`. Aucun défaut ne s'applique. S4, S8 et S18 sont décidés (R-739) : choisis après lecture du pilote v3, sur délégation de Lazar, avec leur raison ; ils figurent dans la configuration (S4, S18) ou la commande (S8).** S4, S7, S8 (interne), S9, S11, S12, S13, S14, S16, S17 et S18 sont des champs de la configuration : une valeur différente de celle du bloc de configuration change le code et l'identité (à régénérer). S1, S2, S3, S5, S6, S10, S15 sont des seuils de lecture appliqués par le lecteur R13.

**S1 — effet minimal du contrôle de plomberie, Δ(B, A) sur (iii)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02** (deux fois α), par principe.
- Raison : règle « moyenne ≥ S1 et borne basse B2 > 0 », par δ, N = 100, rééchantillonnage réel [M4 § 3a] : taille 0,000 sous effet nul ; 0,499 et 0,483 sous effet = S1 (règle de pertinence et de significativité, pas un test de « effet ≥ S1 ») ; puissance 0,976 et 1,000 à un effet de 0,03 ; pilote pris pour vérité 1,000.

**S2 — erreur de première espèce et corrections**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **5 % bilatéral par famille**, trois familles : Tables 1, 2 et 5 (Bonferroni sur 2 δ, B2) ; Q1, Table 3 (Bonferroni sur 8 tests, B8 ; équivalence au niveau 0,05/8 par côté, E8) ; Q2, Table 6 (Bonferroni sur 4 tests, B4 ; équivalence 0,05/4, E4). Pas de correction entre Q1 et Q2.
- Raison : tailles mesurées avec la règle réelle (20 000 tirages, quantiles linéaires, 1 000 répétitions par scénario, N = 100 instances tirées du pilote v4, centrées puis décalées à la frontière) [M4 § 3b, § 3c, § 3e] : Q1, P(« B > X » | Δ = +m) 0,001 à 0,005 (nominal 0,003) ; P(« X > B » | Δ = −m) 0,002 à 0,006 ; P(« ≈ » | Δ = ±m) 0,004 à 0,015 (nominal 0,006) ; Q2, 0,005 à 0,014 ; 0,004 à 0,015 (nominal 0,00625) ; « ≈ » 0,006 à 0,024 (nominal 0,0125) ; Table 5, P(I1 haute < S15 | I1 = S15) 0,013 et 0,006, P(borne de I3 − nul du mauvais côté de 0 | I3 − nul = 0) 0,001 à 0,011 (nominal 0,00625). Erreur de simulation ≈ ±0,003. **Dépassement du nominal jusqu'à un facteur 2 à 2,5 dans quelques cellules** (percentiles d'un rééchantillonnage un peu étroits) : déclaré ; aucune lecture prédite n'est près d'une frontière (C3 et D à 0,14–0,23 ; B′ − D à 0,002–0,004 de zéro ; B′ − C3′ à 0,007–0,011, E4 haute 0,0135 et 0,0168 < 0,02).

**S3 — puissance visée**
- Valeur : À REMPLIR par Lazar.
- Recommandation : plomberie ≥ **0,9** à un effet de 0,03 par δ ; Tables 3 et 6 : probabilité de la classe prédite ≥ **0,8** pour les prédictions fermes.
- Raison : plomberie 0,976 et 1,000 ; P4, P5, P8 : 1,000 ; P10 : 1,000 conditionnel, 0,990 avec l'incertitude du pilote ; P11 : 1,000 [M4 § 3, § 4]. Limite : sous un écart nul sur (ii), « sans régression » (borne basse > −S5 aux deux δ) ne sort qu'avec 0,400 à S5 = 0,02 [M4 § 3d].

**S4 — nombre d'instances N par valeur de δ — DÉCIDÉ (R-739)**
- Valeur : **N = 100** (200 tâches), décidée par conv-audit sur délégation de Lazar (R-739), **après** lecture du pilote v3 ; champ `n_instances` de la configuration.
- Raison : S3 tenue sous le pilote ; la décision est une réplication scellée ; tailles et probabilités ci-dessus à N = 100 ; temps : 202 min de processeur, 101 min de mur à efficacité 1 (S8).

**S5 — tolérance de non-régression sur (ii), Δ(B, A)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02 (= S1)**, par principe. **Lecture sans seuil** recopiée dans tous les cas.
- Raison : sous le pilote, « régression avérée » 1,000 ; taille de « régression avérée » à l'écart −S5 : 0,016 ; sous un écart nul, « sans régression » 0,400 [M4 § 3d].

**S6 — marge des contrastes de Q1 (Table 3) et de Q2 (Table 6)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **m = 0,02 (= S1) pour les quatre témoins de Q1 et les deux de Q2, aux deux δ**, par principe (fixé au gel v3, avant le pilote v3). Équivalence bilatérale : un témoin équivaut à B si leur écart est démontré dans ]−0,02 ; +0,02[.

**S7 — λ des « ou » déterministes C3 et C3′**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **8** (gel v2).

**S8 — plafond de temps — DÉCIDÉ (R-739) pour la décision**
- Valeur : **`timeout 9000`** (2 h 30 de mur) externe pour la décision à N = 100, décidé par conv-audit sur délégation de Lazar (R-739), **après** lecture du pilote v3 ; **600 s de processeur par tâche** (garde interne `plafond_cpu_tache_s`, configuration). Audit d'attaquant indépendant (20 tâches) : `timeout` à geler par Lazar — À REMPLIR ; recommandation **`timeout 5400`** (20 tâches à 241,5 s de processeur en moyenne, maximum 287,1 s : 40 min à efficacité 1, tient jusqu'à une efficacité de 0,45).
- Raison et risque : par tâche (8 bras) : moyenne 60,7 s, médiane 59,6 s, maximum 87,3 s ≪ 600 s ; décision : 12 136 s de processeur, 6 068 s de mur à efficacité 1 (67 % de 9 000 s) ; **efficacité minimale pour tenir : 0,67**. Efficacités mesurées : 0,80 (pilote v3) ; 0,52 (pilote v4 : deux lancements simultanés, quatre processus sur deux cœurs, charge 9 à 11) ; 0,51 (audit d'essai v4, charge 3 à 6 due à d'autres sessions) [M4 § 5, § 8]. À 0,65 le run dure 9 335 s et serait coupé. **Réserve (divergence non résolue avec R-739)** : 9 000 s ne tient que sur une machine sans autre calcul lourd ; le texte en fait une condition de lancement (§ Plan 5 : charge moyenne sur une minute < 0,5 relevée par `uptime` juste avant le lancement, consignée). Si Lazar préfère ne pas dépendre de cette condition : N = 80 (fait tenir 9 000 s jusqu'à une efficacité de 0,54 ; probabilités des classes non simulées à N = 80 ; champ `n_instances`, identité à régénérer) ou `timeout 12600` (recommandation de la contre-lecture 3). Durée totale décision + audit : 2 h 20 à efficacité 1.

**S9 — taux de fausses alertes α et tolérances**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **α = 0,01** ; garde |taux mesuré − α| ≤ 0,005 par défense finale ; déclencheur |moyenne d'un bras − α| > 0,001 dans un δ.
- Raison : pilote v4, écart des moyennes à α ≤ 0,0002 ; écart entre bras par tâche moyen 0,0016, maximum 0,0031 [M4 § 6].

**S10 — déclencheur « trop beau / trop mauvais » (règle réécrite, CM3-05)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : audit si la moyenne de V d'un bras dans un δ sort de la **bande moyenne pilote ± k × écart-type par tâche du pilote × √(1/n_pilote + 1/N)**, n_pilote = 24, **k = 3** (Bonferroni sur 16 bandes à 5 % : Φ⁻¹(1 − 0,05/32) ≈ 2,95, arrondi ; règle et repli « k = 4 si le taux simulé dépasse 0,05 » fixés au gel v4 avant le pilote) ; plus la règle de Lazar : moyenne de V(B) ≥ 0,99.
- Raison : taux simulés de fausse alerte sur les 16 bandes (5 000 paires pilote / décision tirées par tâches entières du pilote v4) : règle v3 (± 5 é.-t./√N, centrée sur le pilote) **0,323** ; v4 k = 3 **0,095** ; v4 k = 4 **0,025** [M4 § 7]. Le taux à k = 3 dépasse 0,05 (les 16 bandes sont corrélées par tâche et l'écart-type du pilote est lui-même estimé sur 24 tâches) : **repli k = 4**, appliqué par la règle du gel v4 § 3.4, écrite avant le pilote.
- Bandes à N = 100 (k = 4) [M4 § 7] : δ 1,4 : A [0,0274 ; 0,1359] ; B [0,1824 ; 0,2374] ; C1 [0,1616 ; 0,2177] ; C2 [0,1340 ; 0,2054] ; C3 [0,3803 ; 0,4264] ; D [0,4289 ; 0,4591] ; B′ [0,4299 ; 0,4629] ; C3′ [0,4213 ; 0,4571] ; δ 1,6 : A [−0,0012 ; 0,0730] ; B [0,1565 ; 0,1927] ; C1 [0,1319 ; 0,1764] ; C2 [0,1113 ; 0,1667] ; C3 [0,3009 ; 0,3369] ; D [0,3406 ; 0,3676] ; B′ [0,3443 ; 0,3722] ; C3′ [0,3279 ; 0,3658]. Si N change, la bande se recalcule par la même formule.

**S11 — budgets de comportement δ — recalibrés (R-739)**
- Valeur : À REMPLIR par Lazar (confirmation du résultat de la règle).
- Recommandation : **δ = (1,4 ; 1,6)**, rendus par la règle du gel v4 § 2 (A seul, 48 instances, racine 20264101 / 20264102), sans choix à la main.
- Raison et réserves : moyennes de V(A) au calibrage, avec erreur-type : 1,2 : 0,1614 (0,0159) ; **1,4 : 0,1019 (0,0131)** ; **1,6 : 0,0563 (0,0107)** ; 1,8 : 0,0256 (0,0060) ; 2,0 : 0,0072 (0,0022) (grille complète au résumé, point 3). Le couple dépend de deux franchissements bruités ; sous 2 000 rééchantillonnages des instances : (1,2 ; 1,6) 0,43 ; (1,4 ; 1,6) 0,33 ; (1,4 ; 1,8) 0,23 (descriptif, sans effet sur le choix). Au pilote v4 (24 instances d'une autre racine), V(A) = 0,082 au δ bas (sous 10α) et 0,036 au δ haut (3,6 α) : A reste bas au δ haut ; la Table 1 à 1,6 mesure B contre un A faible, mais plus contre un A presque nul (2,7 α à 1,8 au pilote v3).

**S12 — nombre de tours T** : À REMPLIR par Lazar. Recommandation **T = 8**.

**S13 — oracle du défenseur (identique pour tous les bras)** : À REMPLIR par Lazar. Recommandation **« détection »** (principe, § Hypothèse).

**S14 — seuil de contournement relatif κ** : À REMPLIR par Lazar. Recommandation **κ = 0,5**, garde κ × base ≥ 2α (mesure descriptive).

**S15 — marge de la condition d'application (Table 5)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02 (= S1)**, par principe (gel v3).
- Raison : sous le pilote, ligne « cycle » aux deux δ 1,000 ; tailles 0,006 à 0,013 (I1) et 0,001 à 0,011 (I3 − nul) [M4 § 3e].

**S16 — unités de chaque moniteur de B′**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **9** (= T + 1, la classe du moniteur final de D ; gel v3). Options non implantées (décision de Lazar) : témoin « mode » (moniteur de poids maximal de B′ déployé seul) ; « ou » restreint au support de B′ ; maxout unique de 73 unités (§ Portée) ; nouvelle conception à moins d'unités (où le mélange serait exercé) : nouveau gel, nouveau pilote, racine neuve.

**S17 — audit d'attaquant indépendant (déclencheur 9) — critère réécrit (CM3-01, CM3-04)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **K = 10 tâches de la décision par δ** (instances 0 à 9, aux deux δ : 20 tâches), bras **A**, B, C3, D, B′, C3′ ; attaquant comme au § Métrique ; contrastes audités **B − A** (Table 1), B − C3, B − D (Table 3), B′ − D, B′ − C3′ (Table 6), et la Table 5 (I1, I3 de A). Pour chaque contraste et chaque δ : c_i = contraste sur les choix audit réévalués − contraste sur les choix source réévalués ; c̄ = moyenne sur les K tâches ; ES = écart-type / √K. **Artefact** si (i) |c̄| > **m/2 = 0,01** (écart pratique ; pour la Table 5, |écart moyen de I1| > S15/2 = 0,01), **ou** (ii) |c̄| > t(K − 1 ; 0,995) × ES **et** la classe du contraste dans sa table, recalculée en décalant l'estimation et toutes ses bornes de c̄, diffère de la classe lue (pour la Table 5 : ligne recalculée avec I1 et I3 − nul décalés de leurs écarts moyens, l'un des deux écarts dépassant t × ES). **Aucun changement de signe ne compte à lui seul.** Repli fixé au gel v4 avant tout calcul : si le taux simulé de fausse alerte dépasse 0,05, le multiplicateur de (ii) passe à t(K − 1 ; 0,9995), rien d'autre.
- Raison : audit d'essai v4 (5 tâches par δ du pilote, essai de fonctionnement, CM3-11) : écarts moyens de −0,0011 à +0,0010, erreur-type ≤ 0,0027, écart maximal par tâche 0,0097 ; aucun drapeau [M4 § 8]. Taux de fausse alerte du critère complet (12 tests : 5 contrastes et la Table 5, aux deux δ), décision simulée (N = 100 tirées du pilote) et audit simulé (K = 10 écarts par δ tirés parmi ceux de l'essai) : **0,002** (écarts centrés), 0,011 (bruit gaussien d'écart-type double) ; repli non déclenché ; puissance contre un écart systématique ajouté à B′ − D aux deux δ : 0,000 à 0,005, **0,762 à 0,010**, 1,000 à 0,015 ; à B − C3 : 0,749 à 0,010, 1,000 à 0,015 [M4 § 8b]. Réserves : bruit estimé sur 5 tâches par δ seulement ; la partie I3 de l'audit de la Table 5 n'a pas changé I3 sur les 10 tâches d'essai (la réponse renforcée part de l'attaque du tour et en reste proche) : contrôle faible de la forme, fort de I1 ((iii) abaissé dans 48 tours sur 80, baisse moyenne 0,0013).

**S18 — garde de convergence des entraînements — DÉCIDÉ (R-739)**
- Valeur : **0,10** par tâche (au plus 3 non-convergences sur 34 entraînements), décidée par conv-audit sur délégation de Lazar (R-739), **après** lecture du pilote v3 ; champ `taux_nonconv_max`, présent dès le premier calcul v4 (pilote, essais et calcul de puissance v4 ont tourné à 0,10 : pas de rupture de chaîne d'empreinte).
- Raison : au pilote v3, 2 non-convergences sur 1 632 ; à 0,05, deux non-convergences dans une même tâche arrêtent la décision, probabilité estimée ≈ 0,16 sur 200 tâches (chiffre fragile dans les deux sens : 2 événements, CM3-09) ; la garde vise une dérive massive, pas un cas isolé (un entraînement arrêté à la limite d'itérations reste employé). Pilote v4 : 3 non-convergences sur 1 632 entraînements, dont **2 dans une même tâche** (2/34 = 0,059) : à 0,05 le pilote v4 lui-même se serait arrêté ; à 0,10 il passe [M4 § 6].

## Plan d'analyse

### 1. Monde
Loi propre N(0, I_6). Loi cible d'une instance : 3 composantes, moyennes de norme 4 dans des directions tirées, écarts-types 1. Loi d'attaque : 3 composantes appariées, moyennes et écarts-types diagonaux dans la boîte (|μ| ≤ 5, σ ∈ [0,5 ; 1,5]). Contrainte de comportement : racine de la moyenne sur k du carré de la distance de Wasserstein d'ordre 2 entre composantes appariées ≤ δ.

### 2. Bras
Tour 0 commun : moniteur linéaire M0 entraîné contre la loi cible (reproductibilité bit à bit vérifiée par garde). Puis, pour t = 1 … T, dans chaque bras à trajectoire : l'attaquant calcule une meilleure réponse contre la défense déployée ; le défenseur se met à jour.
- **A, défense unique réentraînée, même oracle** : déploie le dernier moniteur linéaire, entraîné contre le mélange uniforme de toutes les attaques passées.
- **B, mélange d'équilibre linéaire** : double oracle tronqué ; p = stratégie d'équilibre du défenseur sur la matrice G ; q = stratégie d'équilibre de l'attaquant ; nouveau moniteur **linéaire** entraîné contre q. Défense finale : p sur la matrice 9 × 9.
- **B′, mélange d'équilibre à classe de D** : identique à B, mais l'oracle rend à chaque tour un **maxout à S16 = 9 unités**.
- **D, unique** : un seul maxout à t + 1 unités au tour t (9 à la fin), entraîné contre le mélange uniforme de ses attaques passées.
- **C1, C2, C3** sur les 9 moniteurs mêmes de B après le tour T (poids uniformes ; Dirichlet (1, …, 1) ; « ou » déterministe standardisé, λ = S7, seuil recalibré à α). **C3′** sur les 9 moniteurs mêmes de B′ (`MoniteurOu`).
Pour chaque bras, la défense finale est figée ; l'attaquant joue en dernier avec les attaques passées de sa trajectoire comme départs supplémentaires.

### 3. Graines (R9)
- **RACINE = 20261201**, **RACINE_TENUE = 20261202** (décision, jamais employées). Racines d'essai v4, toutes dans la plage 20264001 à 20264999, écrites au gel v4 (§ 1.1) avant emploi : 20264101 / 20264102 (recalibrage) ; 20264201 / 20264202 (pilote v4 et audit d'essai) ; 20264211 / 20264212 (réservées à une reprise du pilote, **non employées**) ; 20264301 / 20264302 / 20264303 (essais du code) ; 20264401 (simulations du calcul de puissance).
- **Refusées par garde** (`exiger_racine_permise`, appelée dans `gen`) : 20261101 ; 20261291 à 20261298 ; 20261301 ; 20261311 à 20261316 ; 20262291, 20262297, 20262313 ; 20269501 / 02 ; 20269731 / 32 ; 20269741 / 42 ; toute racine de 20265001 à 20265999 (autre session) ; toute racine hors décision non gelée.
- Chaque tirage : `numpy.random.SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, rôle, …))`, numpy ≥ 1.25 ; schéma dans la configuration (`schema_graines`). Chaque bras tire de son propre code (essai `test_ordre_des_bras_sans_effet`). Garde de la racine de décision dans `gen`, re-vérifiée dans chaque processus de travail.

### 4. Comparaisons et multiplicité
- **Table 1** : Δ(B, A) sur (iii), B2. **Table 2** : Δ(B, A) sur (ii), B2. **Table 5** : I1 et I3 − 0,7345 de A, B2 ; I2 recopié.
- **Q1 (Tables 3 et 4)** : Δ(B, C1), Δ(B, C2), Δ(B, C3), Δ(B, D), 8 tests, B8 et E8. **Q2 (Tables 6 et 7)** : Δ(B′, D), Δ(B′, C3′), 4 tests, B4 et E4.
- « Confirmée » = intersection-union ; « réfutée » = union protégée par la correction.
- **Descriptives** : Δ(B′, B), Δ(C3′, C3), Δ(C3′, D), Δ(C1, C2), Δ(C3, A), Δ(D, A) ; (ii) de B − C3, B − D, B′ − D, B′ − C3′ ; I1, I2, I3 − nul de B, D, B′ ; matrices H moyennes ; coût, courbes, nouveauté ; poids, pureté forcée, indice du moniteur dominant, B′ − D et B′ − C3′ selon la pureté ; contrôles.

### 5. Ordre d'exécution, arrêt et reprise
(1) Essais du code ; (2) une seule invocation `PYTHONPATH=src timeout 9000 python3 arene_melange_v4.py decision --prereg prereg/<nom>.md --instances 0:100 --run-id <AAAAMMJJ-HHMMSS-arene-melange-v4> --processus 2`, arbre git propre, sur une machine sans autre calcul lourd (charge moyenne sur une minute < 0,5 relevée par `uptime` juste avant le lancement et consignée ; S8) ; PID et instants de départ des processus de travail écrits et scellés dans `runs/<run-id>/pids-travail.txt` ; (3) analyse écrite par le même processus (`analyse-arene.json`, scellé) ; (4) si le déclencheur 9 (ou un autre imposant l'audit) est présent, `arene_melange_v4.py audit --prereg … --source-run <run-id> --instances 0:10 --run-id <run-id>-audit --S1 … --S6 … --S15 …` (valeurs gelées), sous `timeout` (S8) ; les tâches de la décision sont reconstruites et vérifiées **au bit près** contre le run audité avant l'attaquant indépendant ; (5) lecture par un sous-agent neuf (R13), qui applique les tables ; `lire_tables` et `classes_sous_audit` sont des aides mécaniques, le texte scellé fait foi.

**Reprise après arrêt** : (a) arrêt de cause **externe** (signal, `timeout`, machine), aucun résultat écrit : le signal TERM est converti en arrêt du pool ; arrêt par PID de tout survivant consigné et garde « aucun orphelin ». **Aucune reprise tant que `arene_melange_v4.py orphelins --pids runs/<run-id>/pids-travail.txt` ne rend pas « aucun processus de travail consigné ne tourne »** (avec `--arreter` : arrêt par PID, jamais par motif de ligne de commande, R10). Puis **une** reprise complète, même code, mêmes racines, nouvel identifiant de run ; seconde interruption externe → non concluant ; (b) arrêt par une garde interne : pas de reprise → non concluant, version nouvelle du préenregistrement ; (c) aucun point de reprise partiel (déclaré). Réserve : le processus `resource_tracker` de multiprocessing n'est pas consigné.

### 6. Historique de conception (déclaré ; aucune décision n'a lu une racine de décision)
1. Oracle du défenseur, seuil de contournement, bras C1–C3 : brouillon 2. 2. Bifurcation v3 (Q2, B′, C3′, condition d'application, marges par principe) : gel v3, avant toute exécution de B′.
3. **Après le pilote v3 et la contre-lecture 3** : décisions R-739 (Q2 gardée, recalibrage, S18, N, délai) ; gel v4 écrit à 12:43–12:44 UTC le 31 octobre, avant toute ligne de code v4 (journal v4) et présent au commit `f65feb1a` (12:51 UTC) ; code v4 au calibrage `dcc3e0b9…` (commit `c34a06d7`, 12:57 UTC) ; calibrage 13:05–13:41 UTC ; une seule ligne changée (`DELTAS_V4`, diff vérifié) → code du pilote `70c77fd5…` ; pilote 13:43 UTC.
4. **Après le pilote v4** : aucun changement de conception ni de code. Viennent du pilote v4 : les chiffres des prédictions pour la décision, les bandes S10 (et le choix de k par la règle écrite), le temps projeté, les tailles et probabilités simulées. L'audit d'essai v4 et la sortie de puissance v4 ont été produits par le rédacteur de reprise, avec le code et le calcul de puissance laissés tels quels.

## Critères de lecture gelés

Un sous-agent neuf (R13) applique ces tables telles qu'écrites. Chaque table se lit **de haut en bas ; la première ligne vraie décide** ; la dernière est le complémentaire. Notations, pour un contraste ou un indicateur à δ fixé : est = moyenne ; qX = quantile X du rééchantillonnage ; **B2 = B4** = [q0,00625 ; q0,99375] ; **B8** = [q0,003125 ; q0,996875] ; **E8** = [q0,00625 ; q0,99375] ; **E4** = [q0,0125 ; q0,9875].

**V0** = aucune condition de la liste d'arrêt ∧ tâches exécutées = 2 × N ∧ racines du manifeste = RACINE et RACINE_TENUE ∧ empreintes du code, de la configuration et de la bibliothèque = celles du texte scellé ∧ une seule invocation ayant écrit des résultats (au plus une reprise complète après arrêt externe consigné et commande `orphelins` saine).

**Déclencheurs d'audit (R4), symétriques** — un seul suffit ; l'effet bloquant de chacun est écrit :
1. **Contradiction de la branche prédite, dans les deux sens** (§ Prédiction B) : (a) classe du signe opposé au signe prédit ; (b) classe prédite « ≈ » (P8) et observée « B′ > D » ou « D > B′ » ; (c) plomberie observée en ligne 5 ou 6 ; (d) (ii) borne basse B2 > 0 dans un δ ; (e) Table 4 « Q1 confirmée » ou « dépend de δ » ; (f) Table 7 autre que « Q2 non exercée » ; (g) Table 5 autre que « A ne progresse pas, retours au-delà du hasard (cycle) » à un δ. *Bloque* : la table contredite et la phrase de synthèse ; (c) bloque la Table 1.
2. **Trop beau / trop mauvais** (S10) : moyenne de V d'un bras dans un δ hors de sa bande ; ou moyenne de V(B) ≥ 0,99. *Bloque* : toutes les tables.
3. **Règle de Lazar** (« si le mélange uniforme égale le mélange d'équilibre, audit ») : Δ(B, C1) « ≈ » dans un δ ; ou V(B) = V(C1) au bit près sur une tâche ; ou poids finaux de B uniformes (10⁻⁶) sur une tâche. *Bloque* : la classe de C1 dans la Table 3 seulement.
4. **Mélange B dégénéré** : poids de B purs sur plus de la moitié des tâches d'un δ. *Bloque* : Tables 1, 3, 4. (Pour B′, la pureté n'est pas un déclencheur : elle rend Q2 « non exercée » par la Table 7.)
5. **Optimiseur** : moyenne de (V standard − V renforcé) > 0,01 pour un bras dans un δ ; ou un contraste des Tables 1, 3, 6 qui diffère de plus de 0,01 entre attaquant standard seul et renforcé seul. *Bloque* : toutes les tables.
6. **Jeu restreint** : moyenne de (valeur du jeu restreint − V) < −0,01 pour B ou B′ dans un δ. *Bloque* : Tables 1, 3, 4 (B) ou 6, 7 (B′).
7. **Capacité non exercée** : V(D) = V(A) au bit près sur toutes les tâches d'un δ. *Bloque* : Tables 3, 4, 6, 7.
8. **Dérive des fausses alertes** : |moyenne des fausses alertes finales d'un bras − α| > 0,001 dans un δ. *Bloque* : toutes les tables.
9. **Conforme et trop propre (R4, CM3-04)** : l'une des lectures prédites fermes sort conforme — Table 1 « mécanisme exercé » (P1) ; Table 4 « Q1 réfutée » portée par C3 ou D (P4, P5, P7) ; Table 6 « ≈ » pour B′ − D (P8) ; Table 7 « Q2 non exercée » (P10) ; Table 5 « condition d'application vérifiée », ligne « cycle » aux deux δ (P11). *Effet* : audit d'attaquant indépendant (S17) sur les 20 tâches de la décision, **après** scellement de l'analyse et **avant** la phrase de synthèse, plus, pour P10, le contrôle de non-unicité (part des tâches pures de B′ dont la pureté est forcée, recopiée) ; *bloque* la phrase de synthèse des Tables 1, 4, 5 et 7 (selon la prédiction conforme) jusqu'au rapport.

**Contenu de l'audit** (tout déclencheur) : relecture du code par un sous-agent neuf ; audit d'attaquant indépendant sur les **tâches de la décision** (S17 ; jamais sur la racine d'essai) ; vérification que B et B′ déploient les poids du programme linéaire, C1 l'uniforme, C2 les poids de Dirichlet de sa graine, C3 et C3′ le « ou » des moniteurs de leur source. **Issue** : « artefact trouvé » si et seulement si le rapport scellé constate une erreur de code, un chemin non exercé (hors la pureté de B′, lue par la Table 7), ou le critère de S17 ((i) ou (ii)) ; sinon « pas d'artefact ».

### Table 1 — contrôle de plomberie, Δ(B, A) sur (iii)

| # | Condition | Verdict |
|---|---|---|
| 0 | V0 fausse | **non concluant** ; aucune lecture |
| 1 | un déclencheur qui bloque la Table 1 (1c, 2, 4, 5, 6 pour B, 8, 9 pour P1) est présent et l'audit n'est pas rendu | **non concluant (audit en attente)** |
| 2 | audit rendu, artefact trouvé | **non concluant** ; version nouvelle du préenregistrement |
| 3 | dans un δ, la moyenne de V est ≤ 2α pour les huit bras | **non concluant** : jeu dégénéré |
| 4 | est ≥ S1 ∧ borne basse B2 > 0, aux deux δ | **mécanisme exercé** (B bat la défense unique ; au δ haut, contre un A faible) |
| 5 | borne haute B2 < 0 dans au moins un δ | **le mélange perd contre la défense unique** |
| 6 | sinon | **mécanisme non démontré** |

Les Tables 2 à 7 se lisent si la Table 1 rend la ligne 4, 5 ou 6. Une table bloquée par un déclencheur se lit « en attente d'audit » jusqu'au rapport, puis comme écrite si « pas d'artefact ».

### Table 2 — non-régression sur (ii), Δ(B, A) (bornes B2) ; lecture sans seuil rapportée à côté

| # | Condition | Lecture |
|---|---|---|
| 1 | borne haute < −S5 dans au moins un δ | **régression avérée au-delà de la tolérance** |
| 2 | borne basse > −S5 aux deux δ ∧ borne haute < 0 dans au moins un δ | **régression démontrée, sous la tolérance** |
| 3 | borne basse > 0 aux deux δ | **amélioration sur (ii)** |
| 4 | borne basse > −S5 aux deux δ | **sans régression à S5 près** |
| 5 | sinon | **régression non exclue (imprécis)** |

Déclaré, non corrigé (ce serait changer une règle de lecture après le pilote v4) : la ligne 5 recouvre aussi le cas « borne haute < 0 dans un δ, borne basse < −S5 » (régression démontrée, ampleur non tranchée), qui est celui du pilote v4 ; la lecture sans seuil recopiée le dit. Option pour Lazar, avant gel : ajouter entre 2 et 3 la ligne « borne haute < 0 dans au moins un δ → régression démontrée, ampleur non tranchée ».

### Table 3 — Q1 : classement de chaque témoin X ∈ {C1, C2, C3, D} à chaque δ, Δ(B, X) sur (iii)

| Classe | Condition (marge m = S6) | Sens |
|---|---|---|
| « B > X » | borne basse B8 > m | B bat X d'un effet d'intérêt |
| « X > B » | borne haute B8 < −m | X bat B d'un effet d'intérêt |
| « ≈ » | E8 ⊂ ]−m ; +m[ | équivalents à la marge près |
| « B ≳ X » | borne basse B8 > 0 | B meilleur, effet d'intérêt non démontré |
| « X ≳ B » | borne haute B8 < 0 | X meilleur, effet d'intérêt non démontré |
| « ? » | sinon | non tranché |

### Table 4 — Q1 (« B bat ses témoins à nombre de paramètres égal »)

Statut par δ : « tenue » si les quatre témoins sont « B > X » ; « réfutée (un témoin fait mieux) » si un témoin au moins est « X > B » ; « réfutée (équivalence) » si un témoin au moins est « ≈ » ; « non tranchée » sinon.

| # | Condition | Verdict |
|---|---|---|
| 1 | « tenue » aux deux δ | **Q1 confirmée** |
| 2 | « réfutée » (l'une ou l'autre forme) aux deux δ | **Q1 réfutée** |
| 3 | « tenue » à un δ, « réfutée » à l'autre | **Q1 dépend de δ** |
| 4 | sinon | **Q1 non tranchée** |

### Table 5 — condition d'application (défense unique A), par δ, bornes B2, marge S15 (réécrite, CM3-03)

| # | Condition | Lecture à ce δ |
|---|---|---|
| 1 | borne basse de I1 > S15 | **A progresse** |
| 2 | borne haute de I1 < S15 ∧ borne basse de (I3 − 0,7345) > 0 | **A ne progresse pas, retours au-delà du hasard (cycle)** |
| 3 | borne haute de I1 < S15 ∧ borne haute de (I3 − 0,7345) < 0 | **A ne progresse pas, sans retours au-delà du hasard** |
| 4 | borne haute de I1 < S15 | **A ne progresse pas, forme indéterminée** |
| 5 | sinon | **indéterminé** |

Verdict : « **condition d'application vérifiée** » si A ne progresse pas (lignes 2 à 4) aux deux δ ; « **non vérifiée** » si A progresse à au moins un δ ; « **indéterminée** » sinon. I2 (baisse de détection des attaques passées : oubli ou saturation), I3 brut, sa valeur nulle et les matrices H sont recopiés sans verdict. Au δ haut, A est bas (3,6 α au pilote) : « ne progresse pas » y discrimine peu, ce que la phrase de synthèse recopie.

### Table 6 — Q2 : classement de X ∈ {D, C3′} à chaque δ, Δ(B′, X) sur (iii)

Mêmes classes que la Table 3, avec **B4** à la place de B8 et **E4** à la place de E8, marge m = S6.

### Table 7 — Q2 (« à classe égale, B′ bat D ; à moniteurs égaux, B′ bat C3′ »)

Statut par δ : « **non exercée (mélange B′ dégénéré)** » si les poids finaux de B′ sont purs (un poids ≥ 1 − 10⁻⁹) sur plus de la moitié des tâches de ce δ ; sinon comme la Table 4 sur les deux témoins.

| # | Condition | Verdict |
|---|---|---|
| 1 | « non exercée » à au moins un δ | **Q2 non exercée (au moins un δ)** ; statuts par δ, classes de la Table 6, part pure, part de pureté forcée et B′ − D selon la pureté recopiés |
| 2 | « tenue » aux deux δ | **Q2 confirmée** |
| 3 | « réfutée » aux deux δ | **Q2 réfutée** |
| 4 | « tenue » à un δ, « réfutée » à l'autre | **Q2 dépend de δ** |
| 5 | sinon | **Q2 non tranchée** |

Lecture obligée de la ligne 1 (R-739) : « à classe de 9 unités, le mélange d'équilibre atteint le plafond de la classe ; la décision ne dit pas si le tirage au hasard est utile » (§ Portée).

**Phrase de synthèse** (écrite par le lecteur R13 en recopiant, sans rien omettre) : « Table 1 : … ; Table 2 : … (sans seuil : Δ(B, A) sur (ii) = est [B2] à chaque δ) ; Table 5 : … (par δ ; I1, I3 − 0,7345 et I2 de A avec intervalles) ; Table 3 : C1 …, C2 …, C3 …, D … (par δ, avec est [B8]) ; Table 4 : … ; Table 6 : D …, C3′ … (par δ, avec est [B4]) ; part pure de B′ par δ, part de pureté forcée ; Table 7 : … ; déclencheurs : … ; issue des audits : … ; portée : résultat local au monde, à l'oracle, aux δ et à T ». Les classes des Tables 3 et 6 sont toujours recopiées.

## Liste d'arrêt

Chaque garde du code (78 sites `raise GardeArret`, chacun avec un motif unique) a un essai nommé qui la provoque par son motif (`pytest.raises(…, match=motif)`) et un cas sain ; `test_chaque_garde_a_son_essai` contrôle par l'arbre syntaxique que chaque site a une entrée et un essai nommé existant (il ne prouve pas à lui seul que l'essai provoque le motif). Fichier d'essais : `essais/test_arene_melange_v4.py` (97 essais ; R5).

| Condition | Action | Garde et essai (R5 : cas sain et artefact, motif vérifié) |
|---|---|---|
| Lancement en décision ou en audit sans préenregistrement scellé, conforme, identifié | pas de départ ; aucune graine de décision | `autoriser_decision`, `exiger_prereg_arene`, `exiger_identite_prereg` ; `test_prereg_scelle_refus_pour_la_bonne_raison`, `test_identite_prereg_sain_et_artefacts`, `test_decision_refusee_copie_brouillon4_pour_la_bonne_raison` (copie temporaire : sans compagnon → « absente » ; scellée → « scellé mais non conforme : Seuil ; Contre-lecture ») |
| Audit d'un run lancé sous un autre préenregistrement | arrêt | `exiger_meme_prereg` ; `test_exiger_meme_prereg` |
| Graine tirée d'une racine de décision sans autorisation ; processus de travail sans préenregistrement | arrêt | `gen`, `_travail` ; `test_gen_garde_racine_de_decision`, `test_travail_refuse_racine_de_decision_sans_prereg` |
| Racine déjà employée, racine de la plage 20265001–20265999, racine non gelée, racine de décision hors décision, racine des tenues égale à la principale | arrêt | `exiger_racine_permise` (dans `gen`), `exiger_racines_essai` ; `test_racines_essai_sain`, `test_racines_essai_artefact`, `test_liste_des_racines_deja_employees_complete`, `test_cli_essai_refuse_racines_interdites` |
| Gel v4 absent, modifié, ou ne citant pas la racine (calibrage, essai, audit d'essai) | arrêt | `exiger_gel_v4` ; `test_gel_v4_sain_et_artefacts` |
| Calibrage sur d'autres instances que 0:48 ; aucun δ ne satisfait la règle | arrêt | `main` (calibrage), `choisir_deltas` ; `test_cli_calibrage_refuse_autres_instances`, `test_choisir_deltas` |
| Configuration incohérente (δ, effectifs, κ, fractions, oracle, B′ sans maxout, paramètres et critère de l'audit) | arrêt | `exiger_config` ; `test_config_sain_et_artefacts` |
| Fichier de sortie, fichier de PID ou dossier de run existant | arrêt (R12) | `_exiger_absent`, `_ecrire_nouveau`, `creer_manifeste` ; `test_cli_refuse_d_ecraser`, `test_lancer_consigne_pids_sans_orphelin` |
| Arbre git non propre au lancement de décision ou d'audit | arrêt | `creer_manifeste` (essais du dépôt) |
| Programme linéaire non résolu ; primal ≠ dual ; matrice invalide ; programme de non-unicité non résolu | arrêt | `resoudre_jeu`, `poids_max_min_equilibres` ; `test_jeu_sain`, `test_jeu_solveur_artefacts`, `test_jeu_artefact`, `test_equilibres_poids_max_min` |
| Poids de mélange invalides | arrêt | `exiger_poids` ; `test_poids_sain_et_artefact` |
| Loi d'attaque non finie, hors boîte, ou à distance > δ | arrêt | `exiger_admissible` ; `test_admissibilite_sain_et_artefact` |
| Échantillons non multiples de K | arrêt | `echantillonner` ; `test_echantillonnage_stratifie` |
| Moniteur non fini, non calibrable, non calibré | arrêt | `Moniteur` ; `test_moniteur_gardes` |
| « Ou » déterministe sur un moniteur non linéaire ou de variance nulle ; « ou » composite vide ou d'un membre presque constant (écart-type ≤ 10⁻⁶ × max(1, \|moyenne\|)) | arrêt | `ou_deterministe`, `MoniteurOu` ; `test_ou_deterministe_sain_et_artefacts`, `test_ou_composite_sain_et_artefacts` |
| Maxout sans graine ; entraînement non fini ; oracle inconnu | arrêt | `entrainer` ; `test_entrainement_gardes` |
| Aucun départ fini ; part de départs non finis > 5 % | arrêt | `meilleure_reponse`, `exiger_departs_finis` ; `test_meilleure_reponse_departs_non_finis`, `test_garde_departs_finis` |
| Fausses alertes d'une défense finale hors de α ± 0,005 | arrêt | `exiger_fpr` ; `test_garde_fausses_alertes_sain_et_artefact` |
| Part d'entraînements non convergés > S18 = 0,10 dans une tâche | arrêt | `exiger_convergence` ; `test_garde_convergence_et_identite_tour0` |
| Moniteur du tour 0 non reproductible bit à bit | arrêt | `exiger_meme_moniteur` ; idem |
| Temps processeur d'une tâche > 600 s | arrêt | `exiger_plafond` ; `test_plafond_de_temps_processeur` |
| Bras ou témoin inconnu | arrêt | `trajectoire`, `defense_temoin`, `construire_defenses` ; `test_bras_inconnus` |
| Lecture de la Table 5 ou jugement d'audit sans I3 (T < 3) | arrêt | `lire_tables`, `classes_sous_audit` ; `test_lire_tables_refuse_sans_I3`, `test_classes_sous_audit_sain_et_artefacts` |
| Audit : bras absent, tâche absente, V ou I1 reconstruit ≠ run audité au bit près, moins de deux tâches par δ, marges invalides, autres instances que 0:10 ; pilote audité étranger | arrêt | `auditer_tache`, `auditer`, `juger_audit`, `_bornes_marges`, `main`, `charger_pilote` ; `test_audit_sain_et_artefacts`, `test_juger_audit_sain_et_artefacts`, `test_bornes_marges_et_cli_audit`, `test_audit_essai_refuse_pilote_etranger` |
| Processus de travail consigné encore vivant à la fin d'un lancement ou avant une reprise | arrêt (R10) ; pas de reprise | `exiger_aucun_orphelin`, `arreter_par_pid`, commande `orphelins` ; `test_arret_par_pid_sain_et_artefact`, `test_lancer_consigne_pids_sans_orphelin`, `test_signal_term_arrete_le_pool_par_pid` |
| Signal TERM (dont `timeout`) | arrêt consigné, pool terminé, survivants arrêtés par PID | `lever_sur_term` dans `_lancer` ; `test_signal_term_arrete_le_pool_par_pid` |
| Ligne de base du coût trop basse | mesure « non définie », comptée | `cout_contournement` ; `test_cout_contournement_ligne_de_base_et_bissection` |
| Reproductibilité ; bras v2 ou v3 modifiés | constat d'essai | `test_reproductibilite_bit_a_bit_et_temoins`, `test_ordre_des_bras_sans_effet`, `test_bras_v2_inchanges`, `test_bras_v3_inchanges` |
| Tâches ≠ 2 × N ; invocations hors § Plan 5 ; paramètre changé après lecture | V0 fausse | contrôle du lecteur R13 |
| Appel de modèle, réseau, dépense | arrêt (devis et GO exigés) | — |
| Lecture d'un résultat de décision avant scellement | arrêt et consignation (R1) | — |
| numpy < 1.25 | arrêt (R9) | `exiger_numpy_minimal` (essais du dépôt) |
| Marqueur de gel restant, ou contre-lecture sans ses deux empreintes | pas de scellement | validateur `problemes` ; `test_brouillon4_non_conforme_au_validateur_et_identite_du_code` |
| Ligne de gel absente de `registres/decisions.md`, valeurs différentes du texte ; remarques non traitées | pas de scellement ; contrôle manuel pour S1, S2, S3, S5, S6, S10, S15 ; les champs de configuration sont comparés par le code | `exiger_identite_prereg` |

## Rôles

- Auteurs : voir l'en-tête (code v4 et gel v4 : rédacteur Opus coupé ; brouillon 4 : rédacteur de reprise Opus). Aucun n'a écrit les brouillons 1 à 3, les codes v1 à v3 ni une contre-lecture.
- **Vérification courte du brouillon 4 (R2)** : un sous-agent neuf **d'un modèle autre qu'Opus**, qui n'a écrit ni ce texte ni le code ; fichiers à lui donner explicitement : ce brouillon, `arene_melange_v4.py`, `essais/test_arene_melange_v4.py`, `gel-conception-arene-melange-v4.md`, `calibrage-deltas-arene-melange-v4.json`, `calcul-puissance-arene-melange-v4.py` et sa sortie (M4), `essai-pilote-arene-melange-v4-detection.json` (et ses deux parties), `audit-essai-arene-melange-v4.json`, les deux journaux v4, `LISEZMOI-arene-melange-v4.md`, la contre-lecture 3 et le brouillon 3. Points à juger en priorité : traitement de CM3-01 à CM3-16 (tableau ci-dessous) ; application de R-739 ; critère S17 et son taux de fausse alerte ; S10 ; Table 5 réécrite ; lecture de Q2 ; temps.
- Lecteur de porte (R13) : sous-agent neuf, ni auteur ni vérificateur ni analyste ; applique les Tables 1 à 7 ; verdict scellé puis soumis à Lazar.
- Lazar : gèle S1 à S3, S5 à S7, S9 à S17 (S4, S8 et S18 décidés, R-739) ; donne le GO de l'exécution de décision (processeur, aucune dépense).

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf Sonnet 5.5 ; brouillon relu : `preenregistrement-arene-melange-equilibre-v1-brouillon1.md` `5129b8c26d384e92015142e6d80c1d29f922210975fc297ec487efab070284ce` ; rapport : `contre-lecture-arene-melange-v1-brouillon1.md` `3721865417495678475ab995d43a3e56dd1b3b1df7b147a218f6ce9b0bc5bd1f`. Traitement au brouillon 2.

- **Contre-lecture 2** — sous-agent neuf Sonnet 5.5 ; brouillon relu : `preenregistrement-arene-melange-equilibre-v1-brouillon2.md` `622e50d2ad961654b6daaa96d76a94f6dfd2d67188d9f7af199979359c0a1891` ; rapport : `contre-lecture-arene-melange-v2-brouillon2.md` `c6751de38ca84f716d424bc34dccd4103757423932204011a65136bd861cc427`. Traitement au brouillon 3 (tableau CM2-01 à CM2-17), reconduit.

- **Contre-lecture 3** — sous-agent neuf Sonnet 5.5 ; brouillon relu : `preenregistrement-arene-melange-equilibre-v1-brouillon3.md` `3ac8fe1fd1ee4cdb6ebc904a739f8098226703b02b6c0be428e2a572449dced0` ; rapport : `contre-lecture-arene-melange-v3-brouillon3.md` `7ccc1460d6925fb1c743cb099a4490fcca2c7146c99ec4098e49234bb15dc236`. Verdict : « présentable après corrections » (0 bloquant, 4 majeurs, 7 moyens, 5 mineurs). Traitement :

| Id | Traitement | Où dans ce brouillon (et code) |
|---|---|---|
| CM3-01 | **Accepté** : critère réécrit — écart pratique m/2 = 0,01 ou changement de classe démontré (t(K − 1 ; 0,995) × erreur-type) ; aucun changement de signe seul ; choix source et audit réévalués sur un même échantillon frais (biais du minimum retiré) ; 10 tâches par δ ; taux de fausse alerte simulé, repli fixé d'avance. | S17 ; § Métrique ; `juger_audit`, `classes_sous_audit`, `auditer_tache` ; (M4) § 8b |
| CM3-02 | **Accepté** (R-739 (1)) : explication « le dernier moniteur domine » retirée (contredite aussi au pilote v4) ; « plafond de la classe », non « tirage inutile » ; ce que la décision pourra et ne pourra pas conclure ; B′ − D et B′ − C3′ selon la pureté ; indice du moniteur dominant ; pureté forcée par programme linéaire ; B′ − D ne mesure pas le tirage seul. Témoin « mode » : option pour Lazar, non ajouté. | Résumé 5 ; § N'autorise pas ; § Portée ; Table 7 ; § Métrique |
| CM3-03 | **Accepté** : valeur nulle 0,7345 ; I3 − nul ; Table 5 réécrite ; I2 renommé et recopié sans verdict ; H et I2 de B et B′ par moniteur ; A bas au δ haut écrit. | Table 5 ; § Métrique ; Résumé 6 |
| CM3-04 | **Accepté** : A et B − A dans l'audit ; contrôle des tours de A (Table 5) ; déclencheur 9 étendu à P1, P10, P11 ; contrôle de non-unicité pour P10. | Déclencheur 9 ; S17 ; `BRAS_AUDIT`, `PAIRES_AUDIT`, `auditer_tours_A` |
| CM3-05 | **Accepté** : k × é.-t. × √(1/24 + 1/N), k = 3, repli k = 4 ; taux simulé. | S10 ; (M4) § 7 |
| CM3-06 | **Accepté** : P10 rapportée conditionnelle au pilote et avec son incertitude (loi bêta). | P10 ; (M4) § 4b |
| CM3-07 | **Accepté** : titre et Q2 « à moniteurs égaux contre C3′ » ; dilution déclarée ; « ou » restreint au support de B′ : option pour Lazar. | Titre ; Résumé 1 ; § N'autorise pas ; S16 |
| CM3-08 | **Accepté** : gel v4 avant tout calcul, attesté par les commits de conv-audit `f65feb1a` (gel), `c34a06d7` (code du calibrage) et par l'empreinte épinglée dans le code, qui refuse de partir sans le gel. Consignation dans `registres/decisions.md` : à faire par conv-audit (hors du droit d'écriture de ce rédacteur). | § Plan 6 ; journal v4b |
| CM3-09 | **Résolu par R-739 (3)** : S18 = 0,10 décidé ; présent dans la configuration dès le premier calcul v4 : pas de rupture de chaîne. | S18 |
| CM3-10 | **Traité** : délai 9 000 s décidé (R-739) ; projection refaite ; durée totale décision + audit écrite ; condition de lancement (machine sans autre calcul lourd). Écart à la recommandation de la contre-lecture (`timeout 12600`) : R-739 a tranché 9 000 s. | S8 ; § Plan 5 |
| CM3-11 | **Accepté** : audit d'essai v4 sur 5 tâches par δ, présenté comme essai de fonctionnement et base du bruit simulé, non comme contrôle. | S17 ; (M4) § 8 |
| CM3-12 | **Accepté** : (a) chiffres de taille recopiés de (M4) ; (b) décompte v3 corrigé (26 tenues, 8 réfutées sur 34) ; (c) pureté « ≥ » dans le code (`SEUIL_PURETE`) ; (d) « ≈ 0, signe opposé » écrit quand c'est le cas. | § Prédiction A ; code |
| CM3-13 | **Noté** au LISEZMOI v4 (compagnons des essais en chemin relatif, à vérifier depuis `essais/`). | LISEZMOI v4 |
| CM3-14 | Rien à faire (déclaré). | § Plan 5 |
| CM3-15 | **Accepté** : garde relative de variance de `MoniteurOu`. | Liste d'arrêt ; code |
| CM3-16 | **Traité par le recalibrage** (R-739 (2)) ; A reste bas au δ haut (3,6 α au pilote), écrit. | S11 ; Table 5 |
| CM3-17 | Constat positif ; reconduit. | — |

- **Contre-lecture 4 (vérification courte du brouillon 4)** — À REMPLIR : sous-agent neuf d'un modèle autre qu'Opus (identifiant), empreinte de ce brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque.
