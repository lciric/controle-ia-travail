# Préenregistrement — arène coévolutive synthétique : le mélange d'équilibre contre ses témoins, à nombre de paramètres égal (Q1) ; à classe de fonctions égale (Q2, réécrite, proposée au retrait) — v1 — BROUILLON 5 (non scellé)

**Statut : brouillon 5, non gelé ; deux décisions de Lazar attendues (D-Q2 : retrait de Q2 ; D-T : délai et N) ; vérification courte par un modèle autre qu'Opus ; puis gel des seuils par Lazar ; puis scellement ; puis calcul décisif.**

Identifiant : **PREREG-ARENE-MELANGE-EQUILIBRE-V1**. Tâche : piste 3 du brainstorm P-041 (« bras mélange contre défense unique » : un mélange d'équilibre de moniteurs passés répond-il à la non-convergence de la défense unique réentraînée de Bailey et collègues, arXiv `2412.09565` ?), décision de Lazar R-695, test (b), sur processeur ; brouillon 5 écrit après la vérification courte du brouillon 4 et la décision R-1034 point 5 (« go réécriture et correction »). Pilote de **mécanisme** : aucun modèle de langage, aucun texte ; « l'attaquant » est un choix de paramètres dans une famille bornée de lois synthétiques.

- Auteur du brouillon 5, du gel v5 et de son additif b, du code v5, des essais v5, du diagnostic, du pilote v5, de l'audit d'essai v5, du calcul de puissance v5, du journal v5 et du LISEZMOI v5 : rédacteur neuf Opus 5.5 (lignée conv-audit), 1er novembre 2026. Il n'a écrit aucun des brouillons 1 à 4, aucun des codes v1 à v4, aucune contre-lecture ni la vérification courte de ce pilote.
- Branche `canal/conv-audit-n04`. Date (UTC) : 2026-11-01, écrit entre 10:38 et 10:55 (relevés `date -u` au journal v5).
- Commit du code d'analyse : À REMPLIR au gel (commit qui contient `arene_melange_v5.py` à l'empreinte du bloc d'identité, le gel v5 et l'additif b). Aucun fichier v5 n'est committé à l'écriture (hors du droit de ce rédacteur) : seule l'empreinte du code fait foi pour le diagnostic, le pilote et l'audit d'essai v5 (manifestes) ; la décision exige un arbre propre (§ Plan 5).
- Documents qui font foi (chemin + empreinte ; dossier `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/` sauf mention) :
  - `…/p-041-pont-vers-les-vrais-modeles-v1/brainstorm-malleabilite-et-arene-v1.md` — `08360a9402ff81d7d9146ed833d60e687f1be4d9acd0be3ab2867403dda8eb10` ; `…/p-041-pont-vers-les-vrais-modeles-v1/reponse-pont-p041-vrais-modeles-v1.md` — `e98d9f5a0ccbf6a77675fc922b318eec67d4838acf3b1e0ea8657b79928155a3` ;
  - brouillon 4 `preenregistrement-arene-melange-equilibre-v1-brouillon4.md` — `305911b7ab1945d7607377ede9c8cbfcf2257834bca6d6aadcf7c19be41f8160` (sans compagnon `.sha256`, CM4-07) ; vérification courte `verification-arene-melange-v4-brouillon4.md` — `28ab322f9d2e6098562d127f20e98560c4b202ef737b75ff217dfe0c9c7672f2` ; contre-lecture 3 — `7ccc1460d6925fb1c743cb099a4490fcca2c7146c99ec4098e49234bb15dc236` ;
  - décisions **R-739** (31 octobre : Q2 gardée, δ recalibrés, S18 = 0,10, N = 100, délai 9 000 s), **R-1031** (brouillon 4 et gel v4 consignés), **R-1034 point 5** (Lazar, 1er novembre 08:37 UTC : « go réécriture et correction ») de `registres/decisions.md` ;
  - questions au collisionneur `question-convergence-defense-unique-v1.md` — `671c613bf491a03858e79a851d508f6bbeea9237e1d45810e728fb997a54b048` et sa v2 (R-1039, même dossier, vérifiée contre son compagnon) : ce texte ne les contredit pas et n'attend pas leurs réponses (§ Ce qui change) ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` — `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`.
- Pièces v5 (même dossier) :
  - `gel-conception-arene-melange-v5.md` — `b55689cbddb1699ac288deb1b8b808e4d9e5d9fe2f827e2b9e827bc56017d2a0` (racines, diagnostic, règle de choix de u, jeux témoins, règles nouvelles, prédictions ; écrit à 09:14 UTC **avant** toute ligne de code v5 et tout calcul) ; `gel-conception-arene-melange-v5b.md` (additif b) — `a91d29fd748f29d14f3c839594d434569d3a3f6284dac39e856711045601e391` (écrit à 09:24 UTC après les seuls jeux témoins, avant tout calcul sur l'arène) ; les deux empreintes sont épinglées dans le code ;
  - `arene_melange_v5.py` — bloc d'identité ; au diagnostic `1cdf4a58ad06630af39580be39c1d8ba48d2ca2a34befb92e10fd169899543a9` ; `essais/test_arene_melange_v5.py` — empreinte au LISEZMOI v5 ;
  - `diagnostic-purete-arene-melange-v5.json` — `19d9acfb01c324ff34777d7dfa3b50052ec6a27ef271a8fad351cf1bf209d367` (PID : `6998d3f4…`) ;
  - `essai-pilote-arene-melange-v5-detection.json` — `116084f83fc95d2c9de08a3af97f89667474ff3138d000cd93384fa648fbfab6` (PID : `2ad2727c…`) ;
  - `audit-essai-arene-melange-v5.json` — `2f1c3931c4d7c394632af871e95096021581b8e59e6a742c5d92d861fe78fa33` (PID : `28d551c0…`) ;
  - `calcul-puissance-arene-melange-v5.py` — `cb846327082b241c75296af26a58ae5515a517850a4eaf4513a72da7481ecdc1` ; sa sortie `calcul-puissance-arene-melange-v5-sortie.txt` — `78ff081970a139b814e9a1c57e5d723a88d3d90cb9519c41a7b683c730f9b423`, désignée **(M5)** ;
  - journal `journal-pilotes-arene-melange-v5.txt` et `LISEZMOI-arene-melange-v5.md` — empreintes au LISEZMOI.
- Codes v1 à v4 et leurs configurations : cités seulement abrégés (`6402dc6b…`, `6685585f…`, `8e1e651b…`, `1d7544e6…`, `88c87818…`, `02db9c91…`, `70c77fd5…`, `3fbb27fc…`), pour qu'aucun de ces codes, qui cherchent leurs empreintes complètes, ne puisse partir sur ce texte (essai).

Tout nombre de ce texte vient de (M5) (section citée, par exemple [M5 § 5a]), du diagnostic, du pilote v5, de l'audit d'essai v5, des jeux témoins, des gels v5, ou des pièces v4 citées ; ou est un marqueur de gel. **Aucune lecture n'a été faite sur la racine de décision RACINE = 20261201 ni sur RACINE_TENUE = 20261202.**

### Bloc d'identité (vérifié par le code ; à régénérer par `arene_melange_v5.py identite` si le code ou la configuration change)

- Identifiant : PREREG-ARENE-MELANGE-EQUILIBRE-V1
- Racines de décision : RACINE = 20261201 ; RACINE_TENUE = 20261202
- Code : `arene_melange_v5.py` — 71df9a49ba2594837cb38485a50de5b0f25fd210c9f56838f35fdf634c78d575
- Configuration (empreinte de la forme canonique) : 51c9922d7f974d2de3f28050293514aa53a8fb3d335ff71007d600f13ad9c3d1
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
 "echelle_unites": [
  2,
  3,
  5,
  9
 ],
 "entrainement": "detection",
 "eps_equilibres": [
  0.002,
  0.005,
  0.01
 ],
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
 "n_diagnostic": 16,
 "n_eval": 19998,
 "n_eval_tenue": 3999,
 "n_fpr": 20000,
 "n_instances": 100,
 "n_mc": 256,
 "n_mc_final": 512,
 "n_propre_entr": 2000,
 "n_tenue": 50,
 "part_forcee_max": 0.25,
 "part_pure_max": 0.5,
 "pas_bissection": 3,
 "plafond_cpu_tache_s": 600.0,
 "r_cible": 4.0,
 "schema_graines": "SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, role, ...)) ; bras commun 0, A 1, B 2, D 4, C1 5, C2 6, C3 7, B' 8, C3' 9, B_u 10, D_u 11, C3'_u 12, M_u 13 ; roles cible 0, propre 1, attaques d'entrainement 2, calibration 3, fausses alertes 4, Monte-Carlo 5, departs 6, evaluation 7, init maxout 8, lois tenues 9, echantillons tenus 10, final 11, cout 12, Dirichlet 13, courbe 14, attaquant independant 15 ; reechantillonnage (code_delta, code_contraste, 0, 0, 99) ; temoins (racine des temoins : (unites, cas, tour, role 16, ...))",
 "seuil_calibrage_bas": 0.1,
 "seuil_calibrage_haut": 0.03,
 "sigma_cible": 1.0,
 "sigma_max": 1.5,
 "sigma_min": 0.5,
 "tau": 0.25,
 "tau_selle": 0.01,
 "taux_departs_non_finis_max": 0.05,
 "taux_nonconv_max": 0.1,
 "temoin_modes": 3,
 "temoin_poids_max": 0.5,
 "temoin_pur_max_alpha": 3.0,
 "temoin_rayon": 4.0,
 "temoin_tol_valeur": 0.05,
 "temoin_tours": 6,
 "temoin_unites_artefact": 3,
 "tol_dominance": 0.005,
 "tol_fpr": 0.005,
 "unites_Bp": 9,
 "unites_u": 1
}
```
<!-- configuration-canonique-fin -->

## Résumé pour Lazar

1. **Réécriture du jeu : verdict.** Le diagnostic gelé (16 instances × 2 δ, racine neuve) montre que, dans ce monde, **aucune classe plus riche que la classe linéaire ne laisse au tirage quelque chose à gagner** : la règle écrite avant calcul rend **u\* = 1**. À u = 1, la question « à classe égale » **est déjà la Table 1** (B contre A, la défense unique de même classe). **Proposition : retirer Q2 et lire la Table 1 comme la comparaison à classe égale (linéaire)** — décision D-Q2 (§ Seuil, S16), nœud de Lazar.
2. **Pourquoi la pureté (diagnostic)** : par **couverture**. Le gain que le tirage peut apporter dans le jeu restreint (valeur du jeu − meilleur moniteur pur) vaut 0,049 / 0,074 à u = 1, 0,031 / 0,042 à u = 2, puis **0,005 à u = 3** et ≈ 0,001 à u = 5 et 9 : la rupture tombe exactement à **u = K = 3**, le nombre de directions auxquelles la contrainte de comportement attache l'attaquant. Dès qu'une seule fonction de la classe couvre ces directions, plusieurs moniteurs « généralistes » atteignent presque le plafond (jeu plat, aucune ligne dominante), et lequel reçoit le poids 1 est décidé par le bruit de G (fragilité 1,00). Ce n'est ni le solveur ni la projection sur le simplexe (témoin sain : poids 0,334 / 0,334 / 0,333).
3. **Condition testable et garde R5** (gel v5 § 3, additif b) : deux **jeux témoins à équilibre connu** passent avant tout lancement — **sain** (trois modes symétriques, classe linéaire : aucun moniteur pur ne détecte plus que α ; équilibre intérieur v\* = 0,318) : retrouvé (valeur 0,3182, poids maximal 0,334) ; **artefact** (même jeu, classe à 3 unités : point-selle) : reconnu dégénéré (gain du mélange 0,0026 ≤ τ = 0,01). **Le témoin artefact a réfuté le critère du gel v5** (« pureté forcée ») : il avait un point-selle sans pureté forcée ni rendue ; d'où l'additif b, écrit avant tout calcul sur l'arène : **jeu dégénéré = gain du mélange ≤ 0,01** (la pureté est recopiée, plus jugée).
4. **Le tirage n'est pas inutile en soi (descriptif, non opposable)** : à moniteurs égaux, tirer selon l'équilibre bat le meilleur moniteur du même ensemble de +0,041 / +0,059 à u = 2, +0,004 / +0,006 à u = 3, rien au-delà ; contre la défense unique de même classe, +0,065 / +0,078 à u = 2, +0,020 / +0,045 à u = 3, ≈ 0 à u ≥ 5. Le jeu des brouillons 3 et 4 (u = 9) ne pouvait pas distinguer ces deux régimes ; le diagnostic les sépare, mais la règle gelée n'a pas retenu u = 2 (5 tâches dégénérées sur 16 à δ 1,4 pour 4 permises).
5. **Pilote v5 (racine neuve, 24 instances × 2 δ, bras de la décision à u\* = 1 : A, B, C1, C2, C3, D)** : Q1 se réplique pour la troisième fois — B − C3 −0,176 / −0,132 ; B − D −0,224 / −0,167 (**Q1 réfutée**) ; B − A +0,112 / +0,122 (mécanisme exercé ; c'est aussi la comparaison à classe égale) ; A ne progresse pas (I1 −0,001 / −0,002) et revient au-delà du hasard (I3 − 0,7345 : +0,175 [B2 +0,113 ; +0,231] / +0,210 [+0,161 ; +0,252]) ; 0 non-convergence sur 1 248 ; V(A) 0,111 (11 α) et 0,061 (6 α).
6. **Temps (CM4-01, table chiffrée [M5 § 5a])** : 39,2 s de processeur par tâche (maximum 46,6 s) pour les 6 bras ; N = 100 : 7 849 s de processeur, 3 924 s de mur à efficacité 1 ; **9 000 s tiennent jusqu'à une efficacité de 0,44** (12 600 s : 0,31 ; 14 400 s : 0,27) ; à l'efficacité la plus basse mesurée (0,51) le mur médian vaut 7 786 s (87 % du délai), probabilité d'arrêt < 1/20 000. Efficacités mesurées : 0,80 (pilote v3), 0,518 (pilote v4), 0,509 (audit v4), 0,909 (diagnostic v5), 0,978 (pilote v5), 0,962 (audit v5). **Si Q2 est retirée, R-739 (N = 100, 9 000 s) tient** ; la règle du gel v5 propose ce couple ; je recommande 12 600 s pour la marge (décision D-T). Si Q2 est posée à u = 2 (option b), 65 à 75 s par tâche estimés : 9 000 s exigerait 0,72 à 0,83 d'efficacité, intenable. Décision + audit à l'efficacité 0,51 : 2,6 h ; à 1 : 1,3 h.
7. **Autres corrections** : CM4-02 condition de lancement réécrite (réduit le risque sans l'éliminer ; un dépassement = aucun résultat, une reprise, puis non concluant) ; CM4-03 **S10 k = 4** partout (k = 4 : fausse alerte simulée 0,010 sur 12 bandes) ; CM4-04 S8 de l'audit dans les listes ; CM4-05 ordre gel → code précisé ; CM4-06 bornes de P10 sans indépendance ; CM4-07 compagnons à créer par conv-audit ; CM4-08 et CM4-09 notés.
8. **Seuils** : S1–S3, S5–S7, S9–S17 à geler par Lazar avec recommandation (S16 = confirmation de u\* = 1 et D-Q2 ; S8 = D-T et délai de l'audit) ; **S4 (N = 100) et S18 (0,10) décidés** (R-739). Recommandations : S1 = S5 = S6 = S15 = 0,02 ; S10 k = 4 ; S11 = (1,4 ; 1,6) ; S17 = 10 tâches par δ, écart 0,01 ; délai de l'audit 5 400 s.
9. **Prédictions du gel v5 et de son additif** : 24 branches comptées, **17 tenues, 7 réfutées** (dont « u\* = 2 », « pureté forcée détectée sur le témoin artefact », monotonie stricte de la pureté et du gain sur l'échelle) ; 3 sans objet (bras B_u absents à u\* = 1).
10. **Essais** : v5 115 réussis ; v1 25 ; v2 44 et 1 échec connu (CM2-01) ; v3 57 ; v4 97. Validateur sur ce brouillon : « Seuil » et « Contre-lecture » à remplir (attendu).
11. **Portée** : tout résultat est local (monde gaussien, K = 3, classe d'oracle, δ, T) ; il ne réfute ni ne confirme la piste 3 sur de vrais moniteurs. **A est réentraîné contre le mélange uniforme de toutes les attaques passées** (meilleure réponse à l'historique, au sens du jeu fictif côté défenseur, déployée en dernier itéré) : les questions v1 et v2 au collisionneur le décrivent comme réentraîné contre la dernière attaque (écart signalé à conv-audit).

## Ce qui change par rapport au brouillon 4

### Réécriture du jeu (R-1034 point 5)

| Point | Brouillon 4 | Brouillon 5 | Origine |
|---|---|---|---|
| Diagnostic de la pureté | « pureté forcée par le jeu », non expliquée | **diagnostic gelé** sur une échelle de classes u ∈ (1, 2, 3, 5, 9) : couverture des K = 3 directions de l'attaquant ; ni le solveur ni la projection ; jeu plat, poids 1 décidé par le bruit (§ Prédiction A) | consigne, point 1 |
| Critère de dégénérescence | poids purs (≥ 1 − 10⁻⁹) ; pureté forcée (≥ 1 − 10⁻⁶) | **gain du mélange ≤ τ = 0,01** (additif b, après le témoin artefact) ; pureté et pureté forcée recopiées | gel v5 § 3, additif b |
| Condition testable et garde | — | **jeux témoins à équilibre connu** (sain : intérieur retrouvé ; artefact : dégénérescence reconnue) ; garde `controle_temoins` avant tout lancement ; essais sain et artefacts | consigne, point 1 ; R5 |
| Q2 | B′ (9 unités) contre D et C3′ ; « non exercée » prévue à 0,99 | Q2 reposée à la classe F_{u\*} choisie par règle gelée ; **u\* = 1** : Q2 se confond avec la Table 1 ; **retrait proposé** (D-Q2) ; options : Q2 à u = 2 par décision expresse, ou nouveau monde | gel v5 § 2, § 6 |
| Bras | A, B, C1, C2, C3, D, B′, C3′ | décision à u\* = 1 : **A, B, C1, C2, C3, D** (B′, C3′ sortis, code inchangé) ; B_u, D_u, C3′_u, M_u codés (codes 10 à 13), calculés seulement si u ≥ 2 | gel v5 § 4.1–4.2 |
| Table 1 | contrôle de plomberie | contrôle de plomberie **et** comparaison à classe égale (linéaire) | § Hypothèse |
| Table 7 | « non exercée » si poids purs > 1/2 | « non exercée (jeu dégénéré) » si gain ≤ 0,01 sur > 1/2 des tâches ; « non exercée (sommet du solveur) » si poids purs > 1/2 ; « **Q2 retirée** » à u\* = 1 | additif b § 2.4 |
| Racines | plage v4 | racines neuves 20264601 à 20264651 ; **toutes les racines de la v4** (et 20264555, 20264777, 20264001, 20264999) refusées jusque dans `gen` | consigne ; R9 |
| Questions au collisionneur | — | le témoin sain est un jeu à équilibre connu au sens de la question 4 de la v2 ; ce texte n'attend pas les réponses ; si elles arrivent, elles sont comparées au diagnostic sans changer aucune règle gelée | R-1034 (6), R-1039 (4) |

### Constats de la vérification courte (CM4-01 à CM4-09)

| Id | Constat de la vérification | Traitement au brouillon 5 | Où |
|---|---|---|---|
| CM4-01 (majeur) | options de temps non chiffrées contre l'efficacité mesurée ; N = 80 ne règle rien ; durée totale non additionnée ; renvoi du 0,52 | **Accepté** : table de temps chiffrée (M5 § 5a) — probabilité d'arrêt sur la garde pour N ∈ {100, 80, 60} × délai ∈ {9 000 ; 12 600 ; 14 400 s} × efficacité (0,51 ; 0,52 ; … ; 1) et au mélange des efficacités mesurées ; efficacité minimale par case ; « N = 80 à 9 000 s échoue à l'efficacité mesurée » écrit ; durée totale décision + audit à l'efficacité mesurée ; le 0,52 renvoyé au journal v4b (R5 : 2 912,4 / (2 812,4 × 2) = 0,518) ; combinaison proposée au format décision | S8 ; résumé point 6 ; décision D-T |
| CM4-02 (moyen) | la condition de lancement ne protège pas | **Accepté** : réécrite — réduit le risque sans l'éliminer (preuve : audit d'essai v4 lancé à charge 0,3, fini à 0,51) ; conséquence d'un dépassement (aucun résultat, une reprise complète, seconde interruption → non concluant) ; argument du délai long | § Plan 5 ; S8 |
| CM4-03 (moyen) | S10 : ligne « Recommandation » k = 3, valeur en vigueur k = 4 | **Accepté** : recommandation **k = 4** partout (résumé, S10, gel v5 § 4.3) ; en v5, k = 4 d'emblée, repli k = 5 fixé d'avance | S10 ; gel v5 § 4.3 |
| CM4-04 | S8 (délai de l'audit) absent des listes de gel | **Accepté** : S8 (délai de la décision et délai de l'audit) dans l'en-tête de « Seuil », dans « Rôles » et au résumé | Seuil ; Rôles ; résumé |
| CM4-05 | preuve de l'ordre gel → code écrite plus fort que les pièces ; texte CM3-08 périmé | **Accepté** : pour la v4, le commit `f65feb1a` contient **aussi** le premier état du code v4, les essais et le script de puissance ; l'antériorité du gel sur « toute ligne de code » repose sur le journal v4 (déclaration, plausible, non contredite) ; R-1031 a consigné le gel v4 (empreinte, racines, règle), sans l'heure ni les commits. Pour la v5 : gel écrit à 09:14:23 UTC (`date -u`), code commencé à 09:16:58 ; l'additif b à 09:23:52, après les seuls jeux témoins ; **aucun commit** (hors du droit de ce rédacteur) : l'ordre repose sur le journal v5, les empreintes épinglées dans le code (qui refuse de partir sans les deux fichiers) et les manifestes (empreintes du code et du gel dans chaque sortie) ; à committer par conv-audit | § Plan 6 ; Contre-lecture |
| CM4-06 | P10 « 0,990 » suppose les δ indépendants | **Accepté** : P10 rapportée avec ses deux bornes sans hypothèse d'indépendance (au moins le maximum des deux δ, au plus leur somme) et la valeur sous indépendance | P10 ; (M5) § 4b |
| CM4-07 | brouillon 4 sans compagnon `.sha256` | **Noté** : ce rédacteur n'écrit aucun compagnon (consigne) ; compagnons du brouillon 4 et du brouillon 5 à créer par conv-audit ; empreintes données dans le LISEZMOI v5 et ici | LISEZMOI v5 |
| CM4-08 | trois essais nommés sans leur cas sain dans la même fonction | **Accepté** : phrase ajoutée (v5 : `test_jeu_artefact`, `test_racines_essai_artefact`, `test_cli_diagnostic_refuse_autres_instances`) ; les essais neufs de la v5 (témoins, classe u, diagnostic) ont sain et artefacts dans la même fonction | Liste d'arrêt |
| CM4-09 | « arbre git propre » avec d'autres sessions | **Accepté** : note au § Plan 5 (fichiers non suivis d'autres sessions à committer ou à isoler par une copie de travail séparée au même commit, déclaré au journal) | § Plan 5 |

## Ce que l'expérience n'autorise pas

- **Rien sur les vrais modèles** ni sur les moniteurs d'activations réels : ni Llama, ni les sondes de Bailey et collègues, ni la boucle à 70 tours. Le monde est une famille de lois que nous avons écrite (`reponse-pont-p041-vrais-modeles-v1.md` § 0).
- **A n'est pas le protocole de Bailey** : même oracle « détection » que les autres bras, et **réentraîné contre le mélange uniforme de toutes les attaques passées** (meilleure réponse à l'historique, déployée en dernier itéré), pas contre la seule dernière attaque ; la non-convergence de A mesurée ici (Table 5) est une **analogie**, pas une reproduction. (Les questions v1 et v2 au collisionneur décrivent A comme réentraîné contre la dernière attaque : écart de description signalé à conv-audit, sans effet sur ce texte.)
- **Rien sur l'équilibre du jeu complet** : B et B_u sont des itérés du double oracle tronqué à 8 tours.
- **Q1 n'est pas « à capacité égale »** : B déploie 7 paramètres par requête, C3 et D les 63. Une réfutation de Q1 dit que la classe de fonctions déployée compte, pas que le tirage au hasard est inutile.
- **Q2 est posée à une seule classe, F_{u\*}**, choisie par une règle gelée sur la seule non-dégénérescence du jeu (diagnostic) : elle ne dit rien des classes plus riches (où le diagnostic montre le jeu dégénéré) ni de la classe de 9 unités des brouillons 3 et 4. Elle n'est pas « à paramètres égaux » : B_u stocke 7 + 56u paramètres, D_u 7u.
- **C3′_u n'est pas de même classe que B_u** (il déploie tous les moniteurs à la fois) : B_u − C3′_u compare deux usages des mêmes moniteurs.
- **B_u − D_u ne mesure pas le tirage seul** : B_u ajoute à D_u une sélection (maximin sur 9 moniteurs) et une distribution d'entraînement différente (q au lieu du mélange uniforme). **B_u − M_u** isole le tirage à moniteurs égaux contre le meilleur d'entre eux, mais reste descriptif.
- **« Q2 non exercée » n'est pas « le tirage au hasard est inutile »** : c'est un jeu dégénéré (gain du mélange ≤ 0,01) à cette classe, dans ce monde, à ces δ, à T = 8, contre un attaquant local.
- **Monde favorable au « ou » déterministe** : queues gaussiennes, moniteurs peu nombreux, attaquant attaché à K = 3 directions fixes (c'est ce qui rend le jeu dégénéré aux classes riches, diagnostic).
- Deux budgets seulement, choisis sur A seul en v4 ; A bas au budget haut.
- Aucune revendication d'antériorité ni de nouveauté (R8) ; références **SUPPOSÉ** sauf Bailey et collègues (lu sur PDF par session-depot, R-874, aucun chiffre repris).
- Aucun énoncé sur des moniteurs quadratiques, des réseaux profonds, d'autres dimensions, d'autres familles, ni un attaquant en boîte noire.
- (iii) est une **borne haute** de la valeur du jeu (l'attaquant est un optimiseur local), contrôlée par un attaquant indépendant (S17).
- Ni porte, ni dépense, ni modification de P-041.

## Portée d'une réfutation et d'une confirmation

- **Toute lecture est locale** : monde (gaussien, d = 6, K = 3), classe d'oracle du défenseur (linéaire pour A et B, maxout pour C3 et D), oracle « détection », δ ∈ {1,4 ; 1,6}, T = 8, attaquant local en boîte blanche.
- **Q1 réfutée** établit : dans ce monde, un « ou » déterministe des mêmes moniteurs linéaires et un maxout de même total font mieux que leur mélange d'équilibre. Elle ne réfute pas la piste 3.
- **Table 1 « mécanisme exercé »** établit, en plus du contrôle de plomberie : **à classe linéaire égale**, le mélange d'équilibre bat la défense unique réentraînée de même classe, dans ce monde. Elle ne dit pas si le tirage aide à une classe plus riche.
- **Le diagnostic (non opposable)** indique, sans le prouver : à u ≥ K = 3, le jeu restreint est dégénéré et la question du tirage y est vide ; à u = 2, le tirage garde un apport descriptif (+0,04 à +0,08). Une question confirmatoire sur l'échelle de classes demande un préenregistrement propre (option (a) de D-Q2, proposition pour une version suivante) ou l'option (b).
- **Si Q2 est posée à u = 2 (option b)** : « Q2 confirmée » établirait qu'à classe de 2 unités le mélange d'équilibre bat la défense unique de même classe et le « ou » de ses moniteurs ; « réfutée » le contraire ; « non exercée » que le jeu à u = 2 est dégénéré sur la décision malgré le diagnostic. Chaque lecture serait conditionnée par un choix fait après lecture du diagnostic (déclaré).
- **Aucune lecture ne réfute ni ne confirme la piste 3 sur de vrais moniteurs.** Au mieux, elle indique quelle classe de moniteurs tester ensuite (une classe qui ne couvre pas les directions que l'attaquant peut prendre).
- **Condition d'application (Table 5)** : si A progresse, Q1 ne dit rien d'une réponse à la non-convergence ; si A ne progresse pas, Q1 porte sur un monde où la défense unique ne converge pas, dans ce monde seulement. La forme (« cycle ») est lue contre la valeur nulle 0,7345, jamais sur I3 brut.

## Antériorité (toutes SUPPOSÉ sauf mention, non lues sur PDF pour ce texte)

Double oracle (McMahan, Gordon et Blum 2003) ; réponse stratégique à une population de politiques (Lanctot et collègues 2017) ; jeu fictif (Brown 1951 ; Robinson 1951) ; défenses randomisées contre attaques adverses (Pinot et collègues 2020). Bailey et collègues, arXiv `2412.09565v2`, lu sur PDF par session-depot (R-874) : seule l'idée de la boucle est reprise ; **aucun chiffre** de ce papier n'est repris (R7). Le jeu témoin (trois modes symétriques, classe linéaire) est un jeu à équilibre connu au sens de la question 4 de `question-convergence-defense-unique-v2.md` ; il est écrit avec le code de l'arène, sans bibliothèque extérieure.

## Hypothèse

Renvoi : brainstorm P-041 piste 3 (« la réponse correcte à une suite de meilleures réponses adverses est un mélange aux poids d'équilibre ») ; pistes 2, 4, 5 ; scores (i), (ii), (iii) de la fusion v3.

**Principe de l'oracle du défenseur (S13)**, inchangé depuis le brouillon 2 : l'oracle maximise le taux de détection lissé au seuil α, le même pour tous les bras ; A est donc une « défense unique réentraînée, même oracle », réentraînée contre le mélange uniforme de toutes les attaques passées, pas le protocole de Bailey.

**Historique déclaré** : Q2, B′, C3′ et les mesures de la condition d'application sont une bifurcation postérieure au pilote v2 (gel v3) ; les δ recalibrés, S18, N et le délai sont des choix postérieurs au pilote v3 (R-739, gel v4) ; **la réécriture de Q2** (classe F_u, diagnostic, jeux témoins, critère de dégénérescence) est postérieure au pilote v4 et à la vérification courte (R-1034 point 5, gel v5 et additif b) ; aucun n'a lu une racine de décision.

- **Q1 (hypothèse principale 1, inchangée)** : contre la meilleure réponse adverse finale, le mélange d'équilibre B bat chacun des témoins **à nombre de paramètres égal** — C1 (mêmes 9 moniteurs, poids uniformes), C2 (poids de Dirichlet), C3 (« ou » déterministe), D (maxout unique à 63 paramètres) — d'au moins m = S6, aux deux δ. H0 : pour au moins un témoin et un δ, non.
- **Q2 (hypothèse principale 2, réécrite ; proposée au retrait, décision D-Q2)** : à **classe de fonctions égale F_{u\*}** (maxouts à u\* unités), le mélange d'équilibre B_u bat D_u (défense unique réentraînée de même classe) et C3′_u (« ou » des moniteurs mêmes de B_u) d'au moins m = S6, aux deux δ ; u\* rendu par la règle gelée du diagnostic (gel v5 § 2, additif b § 2.3). **La règle a rendu u\* = 1** : à u = 1, B_u est B et D_u est A ; Q2 **se confond avec la Table 1** (B contre A, à classe linéaire égale). Aucun bras de Q2 séparé n'est calculé (branche écrite au gel v5 § 2 et § 6). Si Lazar retient l'option (b) de D-Q2 (Q2 à u = 2), l'énoncé ci-dessus vaut à u = 2, avec les Tables 6 et 7 telles qu'écrites, après un nouveau gel et un pilote sur la racine réservée.
- **Condition « la pureté n'est pas imposée par le jeu » (gel v5 § 3, additif b)** : (C-T) sur les jeux témoins à équilibre intérieur connu, le chemin de calcul retrouve l'équilibre intérieur (témoin sain) et reconnaît le jeu dégénéré (témoin artefact) — garde R5 avant tout lancement ; (C-J) le jeu restreint de la classe retenue n'est dégénéré (gain du mélange ≤ 0,01) que sur au plus un quart des tâches de diagnostic à chaque δ.
- **Condition d'application** : la défense unique A ne progresse pas d'un tour à l'autre (I1) ; forme lue sur l'écart de son taux de retours à la valeur nulle (I3 − 0,7345).
- **Contrôle de plomberie PC** : B bat A sur (iii) aux deux δ. **Lecture ajoutée (v5)** : c'est aussi la comparaison **à classe égale (linéaire)** du mélange d'équilibre et de la défense unique de même classe. **Non-régression** : Δ(B, A) sur (ii), tolérance S5, lecture sans seuil recopiée.
- **Hypothèses de travail** : oracle du défenseur approché (seuil gaussien et deux départs pour les maxouts) ; attaquant approché, contrôlé par un attaquant renforcé et par l'attaquant indépendant de S17 ; loi propre N(0, I) connue du code, pas des bras ; B et B_u itérés tronqués.

## Prédiction chiffrée et signe attendu

**La décision est une réplication de pilotes concluants** : les probabilités simulées ci-dessous sont **conditionnelles au pilote v5** pris pour vérité (24 instances) ; la décision peut encore surprendre, et toute surprise déclenche l'audit. Valeurs non opposables ; la décision se lit sur RACINE, jamais lue.

### A. Prédictions du gel v5 et de son additif, et leur sort

### Diagnostic de la pureté (gel v5 § 2, additif b ; racine 20264601 / 20264602, 16 instances × 2 δ, mode léger ; non opposable)

Fichier `diagnostic-purete-arene-melange-v5.json` (`19d9acfb01c324ff34777d7dfa3b50052ec6a27ef271a8fad351cf1bf209d367`), code au diagnostic `1cdf4a58ad06630af39580be39c1d8ba48d2ca2a34befb92e10fd169899543a9` (le code remis n'en diffère que par la ligne gelée `UNITES_Q2_V5` et la branche « u\* = 1 », § Plan 6 ; une tâche du diagnostic recalculée par le code remis est identique au bit). Mur 1 909,8 s, processeur 3 473,2 s (108,5 s par tâche de diagnostic : 6,4 s pour u = 1, puis 20,4 ; 22,4 ; 27,1 ; 32,2 s pour u = 2, 3, 5, 9), efficacité 0,91 ; 8 non-convergences sur 2 880 entraînements.

| u (unités par moniteur) | δ | jeux restreints dégénérés g_u (gain ≤ 0,01) | pureté forcée f_u | poids purs r_u | gain moyen du mélange dans le jeu restreint | B_u − D_u (erreur-type) | B_u − M_u (erreur-type) |
|---|---|---|---|---|---|---|---|
| 1 (B contre A) | 1,4 | 0,188 | 0,000 | 0,000 | 0,0492 | +0,108 (0,016) | — |
| 1 | 1,6 | 0,062 | 0,000 | 0,000 | 0,0742 | +0,118 (0,011) | — |
| 2 | 1,4 | **0,312** | 0,062 | 0,062 | 0,0305 | +0,065 (0,009) | +0,041 (0,010) |
| 2 | 1,6 | 0,062 | 0,000 | 0,000 | 0,0424 | +0,078 (0,015) | +0,059 (0,012) |
| 3 | 1,4 | 0,812 | 0,250 | 0,250 | 0,0049 | +0,020 (0,006) | +0,004 (0,002) |
| 3 | 1,6 | 0,812 | 0,250 | 0,375 | 0,0053 | +0,045 (0,013) | +0,006 (0,003) |
| 5 | 1,4 | 1,000 | 0,625 | 0,750 | 0,0007 | +0,001 (0,004) | −0,000 (0,001) |
| 5 | 1,6 | 1,000 | 0,562 | 0,625 | 0,0006 | +0,005 (0,005) | −0,000 (0,001) |
| 9 | 1,4 | 1,000 | 0,312 | 0,562 | 0,0011 | −0,000 (0,004) | +0,001 (0,001) |
| 9 | 1,6 | 1,000 | 0,438 | 0,500 | 0,0016 | +0,005 (0,005) | +0,001 (0,001) |

**Lecture du diagnostic (descriptive, non opposable)** :
1. **Pourquoi la pureté** : la cause est la **couverture**. Le gain que le tirage peut apporter dans le jeu restreint s'effondre entre u = 2 et u = 3 (de 0,03–0,04 à 0,005), soit exactement quand une seule fonction de la classe peut couvrir les **K = 3 directions** auxquelles la contrainte de comportement attache l'attaquant (les composantes de la loi cible) ; dès u ≥ 3, le jeu restreint est dégénéré dans 81 à 100 % des tâches. Le moniteur de poids maximal ne **domine** presque jamais les autres (dominance faible : 0 à 6 % des tâches) : le haut du jeu est **plat** — plusieurs moniteurs « généralistes » atteignent presque le plafond de la classe.
2. **Ce n'est ni le solveur ni la projection sur le simplexe** : sur le témoin sain, le même chemin de calcul rend (0,334 ; 0,334 ; 0,333) ; et parmi les tâches pures de B_9, **toutes** admettent des 0,005-équilibres de poids maximal < 0,9 (fragilité 1,00) : **lequel** des généralistes reçoit le poids 1 est décidé par le bruit d'échantillonnage de G, mais **que** le tirage ne gagne rien (gain ≤ 0,002) ne l'est pas.
3. **La pureté (rendue ou forcée) est le mauvais indicateur** : à u = 9, la pureté forcée ne touche que 31 et 44 % des tâches et la pureté rendue 56 et 50 %, alors que le jeu est dégénéré dans 100 % d'entre elles (c'est la leçon du témoin artefact, additif b).
4. **Le nombre de moniteurs passés n'en est pas la cause** : à u ≥ 3, p est déjà pur au tour 3 dans 44 à 94 % des tâches, et la pureté ne croît pas avec le nombre de moniteurs (à u = 9 : 75 et 94 % au tour 3, 44 et 69 % au tour 8).
5. **Le tirage n'est pas inutile en soi** (descriptif) : à moniteurs égaux, tirer selon l'équilibre bat le meilleur moniteur du même ensemble de +0,041 et +0,059 à u = 2, de +0,004 et +0,006 à u = 3, de rien au-delà (B_u − M_u) ; contre la défense unique de même classe, +0,065 et +0,078 à u = 2, +0,020 et +0,045 à u = 3, ≈ 0 au-delà (B_u − D_u). **Dans ce monde, le tirage aide tant que la classe ne couvre pas les directions de l'attaquant ; son apport tombe à zéro quand elle les couvre.** C'est ce que le jeu des brouillons 3 et 4 (u = 9) ne pouvait pas distinguer.
6. **Règle de choix (gel v5 § 2, additif b § 2.3)** : u\* = le plus grand u de (2, 3, 5, 9) tel que g_u ≤ 0,25 et r_u ≤ 0,5 aux deux δ. u = 2 échoue à δ 1,4 (5 tâches dégénérées sur 16 pour 4 permises) ; **u\* = 1**.

**Jeux témoins** (racine 20264611, recopiés dans chaque sortie) : sain : poids (0,334 ; 0,334 ; 0 ; 0 ; 0 ; 0 ; 0,333), valeur 0,3182 contre v\* = 0,3176, meilleur minimum de ligne pure 0,0001, gain 0,318 ; artefact : poids (0,952 ; 0,048), valeur 0,8901, meilleur minimum de ligne pure 0,8874, gain 0,0026, plus petit poids maximal parmi les équilibres 0,9516.

**Pilote v5** (racine 20264621 / 20264622, 24 instances × 2 δ, 6 bras, code `71df9a49…`, configuration `51c9922d…`) [M5 § 1, § 2, § 6] : V moyens δ 1,4 : A 0,1114 ; B 0,2230 ; C1 0,2092 ; C2 0,1991 ; C3 0,3988 ; D 0,4469 ; δ 1,6 : A 0,0614 ; B 0,1836 ; C1 0,1643 ; C2 0,1497 ; C3 0,3153 ; D 0,3504.

| Prédiction (gel v5 § 5 ; additif b § 2.5), confiance | Observé | Sort |
|---|---|---|
| f_9 > 0,5 à au moins un δ (0,75) | 0,312 ; 0,438 | **réfutée** (la pureté forcée n'est pas la bonne mesure : g_9 = 1,000) |
| f_5 > 0,25 à au moins un δ (0,6) | 0,625 ; 0,562 | tenue |
| f_3 > 0,25 à au moins un δ (0,5) | 0,250 ; 0,250 | **réfutée** (égalité au seuil) |
| f_2 ≤ 0,25 aux deux δ (0,6) | 0,062 ; 0,000 | tenue |
| r_u croissante de u = 1 à 9 à chaque δ (0,6) | 0 ; 0,06 ; 0,25 ; 0,75 ; 0,56 et 0 ; 0 ; 0,38 ; 0,62 ; 0,50 | **réfutée** (baisse de 5 à 9) |
| gain moyen décroissant de u = 1 à 9 (0,6) | 0,049 ; 0,031 ; 0,005 ; 0,0007 ; 0,0011 et 0,074 ; 0,042 ; 0,005 ; 0,0006 ; 0,0016 | **réfutée** (remontée de 5 à 9, au niveau du bruit) |
| fragilité ≥ 0,5 parmi les tâches pures de B_9 (0,5) | 1,00 ; 1,00 | tenue |
| B_2 − D_2 > +0,01 aux deux δ (0,55) | +0,065 ; +0,078 | tenue |
| \|B_9 − D_9\| < 0,02 (0,8) | −0,000 ; +0,005 | tenue |
| \|B_9 − M_9\| < 0,01 (0,8) | +0,001 ; +0,001 | tenue |
| B_2 − M_2 > 0 (0,55) | +0,041 ; +0,059 | tenue |
| u\* = 2 (0,45, la plus probable) | u\* = 1 | **réfutée** |
| g_9 > 0,5 à au moins un δ (0,8 ; additif b) | 1,000 ; 1,000 | tenue |
| g_2 ≤ 0,25 aux deux δ (0,5 ; additif b) | 0,312 ; 0,062 | **réfutée** |
| témoin sain : C-T tenue (0,9) | tenue | tenue |
| témoin artefact : pureté forcée détectée (0,85) | 0,9516 < 1 − 10⁻⁶ | **réfutée** (additif b) |
| pilote : Q1, B − C3 et B − D < 0 (0,9) | −0,176 ; −0,132 et −0,224 ; −0,167 | tenue |
| pilote : B − A > 0 (0,9) | +0,112 ; +0,122 | tenue |
| pilote : borne basse B2 de I3 − 0,7345 > 0 aux deux δ (0,7) | +0,113 ; +0,161 | tenue |
| temps par tâche 35 à 75 s (0,6) | 39,2 s (6 bras) | tenue |
| efficacité ≥ 0,85 si charge < 0,5 au lancement (0,6) | diagnostic lancé à 0,48 : 0,909 (pilote lancé à 0,80 : 0,978, condition non remplie) | tenue |
| audit d'essai v5 : aucun drapeau (i) (0,85) | aucun drapeau (i) ni (ii) | tenue |
| S10 à k = 4 : fausse alerte ≤ 0,05 (0,7) | 0,010 | tenue |
| critère d'audit : fausse alerte ≤ 0,05 (0,7) | 0,000 (écarts centrés) ; 0,001 (bruit doublé) | tenue |
| pilote : part pure de B_u ≤ 0,5 ; f_{u\*} ≤ 0,5 ; B_u − D_u > 0 | — | sans objet (u\* = 1 : aucun bras B_u) |

Bilan v5 : 24 branches comptées, **17 tenues, 7 réfutées**, 3 sans objet, 1 non prédite (signe de B_u − C3′_u). Aucune règle n'a été changée après le diagnostic ou le pilote ; la seule règle changée après un calcul (le critère de dégénérescence) l'a été par l'additif b, après les seuls jeux témoins et avant tout calcul sur l'arène. Les prédictions des gels v2 à v4 et leur sort sont aux brouillons 2 à 4.

### B. Prédictions pour la décision, par contraste et par δ (à u\* = 1, option (a) de D-Q2)

Classe prédite sous les valeurs recommandées (S1 = S5 = S6 = S15 = 0,02), estimation du pilote v5, probabilité simulée de la classe à N = 100 avec la règle réelle [M5 § 3, § 4], confiance (probabilité arrondie vers le bas à 0,05, plafonnée à 0,95), branche opposée (réfutation → audit, déclencheur 1). **Prédictions fermes : les signes, P1, P4, P5, P7 et P11.** Les classes de C1 (P2), C2 (P3) et la Table 2 (P6) ne sont pas prédites avec confiance. Mêmes lectures simulées à N = 80 et N = 60 : 1,000 pour les Tables 1, 4, 5 [M5 § 4a].

| # | Contraste | δ | Signe | Classe prédite | Pilote v5 : moyenne | Probabilité simulée | Confiance | Branche opposée |
|---|---|---|---|---|---|---|---|---|
| P1 | B − A (iii), plomberie et classe égale (linéaire) | 1,4 ; 1,6 | + | « mécanisme exercé » | +0,1116 ; +0,1222 | 1,000 | 0,95 | Table 1 ligne 5 ou 6 |
| P2 | B − C1 (iii) | 1,4 ; 1,6 | + | δ 1,4 « ≈ » ; δ 1,6 « B ≳ C1 » (non ferme) | +0,0137 ; +0,0193 | « ≈ » 0,934 ; « B ≳ X » 0,980 | — | signe contraire |
| P3 | B − C2 (iii) | 1,4 ; 1,6 | + | « B ≳ C2 » ; « B > C2 » (non ferme) | +0,0238 ; +0,0338 | 0,874 ; 0,932 | — | signe contraire |
| P4 | B − C3 (iii) | 1,4 ; 1,6 | − | « C3 > B » | −0,1758 ; −0,1317 | 1,000 | 0,95 | « B > C3 », « B ≳ C3 » |
| P5 | B − D (iii) | 1,4 ; 1,6 | − | « D > B » | −0,2239 ; −0,1668 | 1,000 | 0,95 | « B > D », « B ≳ D » |
| P6 | B − A (ii) | 1,4 ; 1,6 | − | Table 2 « régression avérée au-delà de la tolérance » (non ferme) | −0,0454 ; −0,0809 | 1,000 | — | borne basse B2 > 0 dans un δ |
| P7 | Q1 (Table 4) | — | — | « Q1 réfutée » (C3 et D) | — | 1,000 | 0,95 | « Q1 confirmée », « dépend de δ » |
| P10 | Q2 (Table 7) | — | — | « Q2 retirée » (par construction à u\* = 1) ; si option (b) : à prédire après le pilote à u = 2 | — | 1 par construction | — | — |
| P11 | Table 5 | 1,4 ; 1,6 | — | « A ne progresse pas, retours au-delà du hasard (cycle) » aux deux δ | I1 −0,0006 ; −0,0024 ; I3 − 0,7345 +0,175 ; +0,210 | 1,000 | 0,95 | « A progresse » ; une autre forme à un δ |

**Déclencheur 3 probable** (règle de Lazar, « mélange uniforme égal au mélange d'équilibre ») : à δ 1,4, Δ(B, C1) sort « ≈ » avec la probabilité 0,934 : l'audit de la classe de C1 dans la Table 3 est alors imposé ; il ne touche que cette classe.

Descriptives du pilote v5 (sans verdict) [M5 § 6] : (iii) par tour, A plat (0,088 → 0,084), B croissant (0,088 → 0,202), D croissant puis plat (0,087 → 0,407 dès le tour 4) ; nouveauté résiduelle au tour 8 : A 0,155, B 0,141, D 0,187 ; rétention de A au décalage 0 : 0,36 et 0,36 ; I2 de A +0,080 / +0,097 ; I3 − nul de B +0,02 / +0,02, de D −0,35 / −0,30 ; C1 − C2 +0,010 / +0,015 ; C3 − A +0,287 / +0,254 ; D − A +0,336 / +0,289 ; poids de B jamais purs, support moyen 3,5, jeu restreint de B jamais dégénéré (gain moyen 0,066 / 0,079) ; coût par contournement censuré à δ 1,4 : B 0,42, D 0,46 ; fausses alertes moyennes à 0,0003 de α au plus ; 0 non-convergence sur 1 248 ; 0 départ non fini sur 52 680, tous au statut 0 ; V standard − V renforcé ≤ 0,0015 en moyenne par bras.

**Lecture anticipée**, à ne pas confondre avec un résultat : si la décision réplique le pilote et que Q2 est retirée, (a) la défense unique (réentraînée contre l'historique, déployée en dernier itéré) ne progresse pas et ses attaques reviennent au-delà du hasard ; (b) à classe linéaire égale, un mélange d'équilibre la bat ; (c) un « ou » des mêmes moniteurs et un maxout de même total font beaucoup mieux (Q1 réfutée). Le diagnostic, non opposable, ajoute : le tirage aide tant que la classe ne couvre pas les directions de l'attaquant (u < K), plus au-delà.

## Métrique

Notations : une **tâche** = (δ, instance) ; les deux δ partagent la loi cible d'une instance. Taux de détection d'une défense mixte {(m_i, p_i)} sur une loi Q : Σ_i p_i × part des échantillons de Q dont le score dépasse le seuil t_i de m_i ; seuils calibrés au quantile 1 − α de 20 000 échantillons propres communs (α = S9).

- **(iii), principale, V(bras)** : après T tours (S12), défense figée ; deux meilleures réponses sous la contrainte distance ≤ δ et la boîte : **standard** (12 départs tirés + départ vers l'origine + attaques passées de la trajectoire — celles de B pour C1, C2, C3, celles de B_u pour C3′_u et M_u —, 512 échantillons de Monte-Carlo par composante, 100 itérations de programmation quadratique séquentielle par moindres carrés, SLSQP) et **renforcée** (48 départs, 200 itérations, plus la réponse standard) ; chacune évaluée sur 19 998 échantillons frais ; **V = la plus basse des deux détections**.
- **Écart apparié** Δ(X, Y) = moyenne sur les instances de V(X) − V(Y), à δ fixé.
- **Paramètres** stockés et **déployés par requête** (d = 6, un moniteur linéaire = 7 paramètres) : B 63 et 7 ; C1, C2 63 et 7 ; C3, D 63 et 63 ; **B_u** (7 + 8 × 7u) et ≤ 7u ; **D_u** 7u et 7u ; **C3′_u** (7 + 8 × 7u) et (7 + 8 × 7u) ; **M_u** 7u (ou 7 si le moniteur du tour 0 porte le poids maximal) et autant. À u\* = 1, aucun bras de la classe F_u n'est calculé (B_1 est B, D_1 est A) ; sous l'option (b) de D-Q2 (u = 2) : B_u 119 et ≤ 14 ; D_u 14 et 14 ; C3′_u 119 et 119.
- **(ii) familles tenues à l'écart** : 50 lois par tâche tirées de **RACINE_TENUE**, deux sous-familles ; 3 999 échantillons par loi ; score = moyenne des 50 taux. **(i) familles vues** : descriptif.
- **Courbe V(δ')** et **coût par contournement** (piste 5), **nouveauté résiduelle** (piste 4) : comme au brouillon 2 ; descriptifs.
- **Condition d'application** (A : verdict ; B, D, B_u, D_u : descriptif) : matrice H, ligne s = moniteur déployé au tour s (0 … T ; pour B et B_u, chaque moniteur un à un), colonne t = attaque du tour t (1 … T) ; **I1** (progrès) = moyenne de (iii) aux tours 5–8 moins aux tours 1–4 ; **I2** (baisse de détection des attaques passées : oubli ou saturation, non distingués) = moyenne sur t = 1 … 7 de H[t, t] − H[8, t], recopié sans verdict ; rétention par décalage ; **I3** (retours) = part des tours t ≥ 3 où le cosinus du déplacement de l'attaque avec celui d'une attaque d'un tour ≤ t − 2 dépasse celui avec l'attaque du tour t − 1 ; **valeur nulle de I3** sous échangeabilité = moyenne sur t = 3 … T de (t − 2)/(t − 1) = **0,7345** à T = 8 ; l'indicateur lu est **I3 − 0,7345**. Intervalles par rééchantillonnage des instances.
- **Équilibre du jeu restreint final de B et B_u (v5, descriptif, aucune graine)** : poids, pureté (un poids ≥ 1 − 10⁻⁹), plus petit poids maximal parmi les stratégies d'équilibre du défenseur (« pureté forcée » si ≥ 1 − 10⁻⁶), même quantité pour les ε-équilibres (ε = 0,002 ; 0,005 ; 0,01), **gain du mélange** = valeur du jeu restreint − meilleur minimum de ligne pure, **jeu dégénéré** si gain ≤ τ = 0,01 (additif b), dominance faible de la ligne de poids maximal ; B_u − D_u, B_u − C3′_u et B_u − M_u selon la pureté.
- **Contrôles** : fausses alertes de chaque défense finale sur 20 000 échantillons propres indépendants ; valeur du jeu restreint de B et B_u ; V standard − V renforcé ; contrastes sous chaque attaquant seul ; poids finaux de B, B_u, C2 (support, pureté, poids maximal, indice du moniteur de poids maximal) ; statuts de l'optimiseur, départs non finis, réponses à la limite ; entraînements non convergés ; jeux témoins (gel v5 § 3) recopiés dans chaque sortie.
- **Attaquant indépendant (S17)** : par bras audité (A, B, C3, D, B_u, D_u, C3′_u), optimiseur lourd (12 départs structurés, 100 départs tirés, attaques passées et finales, 1 024 échantillons, 300 itérations), puis stratégie d'évolution (1 + 12) sans gradient sur le taux dur, 400 générations, depuis la réponse lourde et depuis l'attaque finale standard. Choix source et choix audit réévalués sur un même échantillon frais (CM3-01). Pour A, à chaque tour, réponse renforcée contre le moniteur déployé ; I1 et I3 recalculés.
- **Intervalles** : rééchantillonnage apparié des instances, 20 000 tirages, quantiles linéaires 0,3125 %, 0,625 %, 1,25 %, 2,5 %, 5 % et symétriques ; graines `SeedSequence(entropy=racine, spawn_key=(code_delta, code, 0, 0, 99))`.

## Seuil

**Les seuils S1 à S3, S5 à S17 — dont S8 (délai de la décision, décision D-T, et délai de l'audit) et S16 (classe de Q2, décision D-Q2) — sont à geler par Lazar en une ligne datée de `registres/decisions.md`. Aucun défaut ne s'applique. S4 et S18 sont décidés (R-739) : choisis après lecture du pilote v3, sur délégation de Lazar, avec leur raison ; ils figurent dans la configuration.** S4, S7, S8 (interne), S9, S11, S12, S13, S14, S16, S17 et S18 sont des champs de la configuration : une valeur différente de celle du bloc de configuration change le code et l'identité (à régénérer). S1, S2, S3, S5, S6, S10, S15 sont des seuils de lecture appliqués par le lecteur R13.

### Décision D-Q2 (nœud de Lazar : modification d'hypothèse)

- **Décision** : que faire de Q2, la règle gelée du diagnostic n'ayant retenu aucune classe plus riche que la classe linéaire (u\* = 1) ?
- **Enjeu** : posée à 9 unités (brouillons 3 et 4), Q2 répète un jeu dégénéré ; le diagnostic montre que le tirage n'apporte quelque chose qu'à u < K = 3 ; à u = 1, Q2 est déjà la Table 1 ; un choix de u fait après lecture du diagnostic serait un degré de liberté du chercheur.
- **Options** :
  - **(a) retirer Q2** ; lire la Table 1 aussi comme la comparaison à classe égale (linéaire) ; recopier le diagnostic comme résultat descriptif ; proposer pour une version suivante une question propre sur l'échelle u ∈ {1, 2, 3} (racine neuve, prédiction de dose-réponse écrite d'avance). Avantage : aucune liberté prise après lecture ; décision plus courte (6 bras, 39 s par tâche ; R-739 tient). Inconvénient : aucune réponse confirmatoire au-delà de la classe linéaire dans cette décision.
  - **(b) poser Q2 à u = 2 par décision expresse.** Avantage : une question confirmatoire au-delà du linéaire, là où le diagnostic montre un apport (+0,065 / +0,078 contre D_2). Inconvénient : choix fait après lecture du diagnostic, contre la règle gelée (u = 2 a échoué à δ 1,4 : 5 jeux dégénérés sur 16 pour 4 permis) ; nouveau gel, pilote à u = 2 sur la racine réservée 20264631 / 20264632, nouvelle vérification ; temps × 1,7 environ (S8 à refaire : 14 400 s au moins, ou N = 80).
  - **(c) réécrire le monde** pour que le jeu soit intérieur à classe riche par construction (attaquant libre de sa direction à distance fixée, ou mélange calculé sur un ensemble de cibles plutôt que tâche par tâche). Avantage : question posable à 9 unités. Inconvénient : nouvelle conception, ce n'est plus le monde des Q1 et Table 5 ; plus d'une session.
- **Recommandation** : **(a)**, confiance 0,7.
- **Défaut sous 48 heures** : aucun (nœud : retrait ou modification d'hypothèse) ; sans décision, le brouillon reste non scellable (S16 à remplir).

### Décision D-T (CM4-01 ; Lazar, ou conv-audit par délégation R-739)

- **Décision** : délai externe de la décision et N.
- **Enjeu** : un dépassement du délai arrête le run sans aucun résultat écrit (une reprise, puis non concluant) ; la vérification courte a montré que 9 000 s ne tenaient pas à l'efficacité mesurée avec les 8 bras de la v4.
- **Table [M5 § 5a]** (option (a) de D-Q2, 6 bras, 39,24 s par tâche ; probabilité d'arrêt sur 20 000 tirages de 2N tâches, mur médian entre crochets) :

| N | délai | efficacité minimale | e = 0,51 | e = 0,52 | e = 0,67 | e = 1,00 | mélange des efficacités mesurées |
|---|---|---|---|---|---|---|---|
| 100 | 9 000 s | 0,44 | 0,000 [7 786] | 0,000 [7 636] | 0,000 [5 927] | 0,000 [3 971] | 0,000 |
| 100 | 12 600 s | 0,31 | 0,000 [7 786] | 0,000 [7 636] | 0,000 [5 926] | 0,000 [3 971] | 0,000 |
| 100 | 14 400 s | 0,27 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| 80 | 9 000 s | 0,35 | 0,000 [6 247] | 0,000 [6 127] | 0,000 [4 755] | 0,000 [3 186] | 0,000 |
| 60 | 9 000 s | 0,26 | 0,000 [4 708] | 0,000 [4 617] | 0,000 [3 583] | 0,000 [2 401] | 0,000 |

  Efficacités mesurées : pilote v3 0,80 ; pilote v4 0,518 (journal v4b, R5 : 2 912,4 / (2 812,4 × 2), et non (M4) § 5, qui donnait 0,16 et 0,41 par lancement de deux lancements simultanés) ; audit v4 0,509 ; diagnostic v5 0,909 ; pilote v5 0,978 ; audit v5 0,962. **Pour mémoire (brouillon 4, 8 bras, 60,7 s par tâche)** : N = 80 à 9 000 s exigeait 0,54 et échouait à 0,51–0,52 (mur 9 518 et 9 335 s), ce que le brouillon 4 ne disait pas. **Option (b) de D-Q2 (estimation, non mesurée)** : 65 à 75 s par tâche ; 9 000 s exigerait 0,72 à 0,83 ; 14 400 s, 0,45 à 0,52 ; N = 80 et 14 400 s, 0,36 à 0,42.
- **Options (sous (a))** : **(i) N = 100, 9 000 s** (R-739 ; proposition de la règle du gel v5 § 4.5) : tient jusqu'à 0,44 ; marge de 13 % à l'efficacité mesurée la plus basse ; une machine partagée par un autre calcul lourd pendant tout le run (deux lancements simultanés en v4 : 0,16 et 0,41 par lancement) le ferait échouer. **(ii) N = 100, 12 600 s** : tient jusqu'à 0,31 ; le délai n'est qu'un plafond, il ne coûte rien quand tout va bien ; inconvénient : une panne n'est constatée qu'au bout de 3 h 30. **(iii) N = 80, 9 000 s** : tient jusqu'à 0,35 ; lectures simulées inchangées (1,000) ; inconvénient : 20 % d'instances en moins, sans gain de temps nécessaire.
- **Recommandation** : **(ii) N = 100, 12 600 s**, confiance 0,65 ; écart déclaré à la proposition de la règle (i), pour la marge contre une machine partagée (CM4-02). Délai de l'audit : **5 400 s** (20 tâches à 86,9 s, maximum 109,2 s : 869 s de mur à efficacité 1 ; tient jusqu'à 0,16) [M5 § 5b]. Durée totale décision + audit : 1,3 h à efficacité 1, 2,6 h à 0,51.
- **Défaut sous 48 heures** : R-739 reste en vigueur (N = 100, 9 000 s), qui tient à l'efficacité mesurée sous l'option (a) ; sous l'option (b), la table est à refaire avant le gel.

**S1 — effet minimal du contrôle de plomberie, Δ(B, A) sur (iii)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02** (deux fois α), par principe.
- Raison : règle « moyenne ≥ S1 et borne basse B2 > 0 », par δ, N = 100 [M5 § 3a] : taille 0,000 sous effet nul ; 0,485 et 0,491 sous effet = S1 (règle de pertinence et de significativité, pas un test de « effet ≥ S1 ») ; puissance 0,980 et 1,000 à un effet de 0,03 ; pilote pris pour vérité 1,000.

**S2 — erreur de première espèce et corrections**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **5 % bilatéral par famille**, familles : Tables 1, 2 et 5 (Bonferroni sur 2 δ, B2) ; Q1, Table 3 (Bonferroni sur 8 tests, B8 ; équivalence au niveau 0,05/8 par côté, E8) ; Q2, Table 6, seulement sous l'option (b) de D-Q2 (Bonferroni sur 4 tests, B4 ; équivalence 0,05/4, E4).
- Raison : tailles avec la règle réelle (20 000 tirages, quantiles linéaires, 1 000 répétitions par scénario, N = 100 instances tirées du pilote v5, centrées puis décalées à la frontière) [M5 § 3b, § 3e] : Q1, P(« B > X » | Δ = +m) 0,001 à 0,005 (nominal 0,003) ; P(« X > B » | Δ = −m) 0,002 à 0,006 ; P(« ≈ » | Δ = ±m) 0,003 à 0,013 (nominal 0,006) ; Table 5, P(I1 haute < S15 | I1 = S15) 0,003 et 0,002 ; P(borne de I3 − nul du mauvais côté de 0 | I3 − nul = 0) 0,001 à **0,019** (nominal 0,00625). Erreur de simulation ≈ ±0,003. **Dépassement du nominal jusqu'à un facteur 2 (Q1) et 3 (I3 − nul à δ 1,4)** : déclaré ; aucune lecture prédite n'est près d'une frontière (C3 et D à 0,13–0,22 ; I3 − nul à +0,17–0,21).

**S3 — puissance visée**
- Valeur : À REMPLIR par Lazar.
- Recommandation : plomberie ≥ **0,9** à un effet de 0,03 par δ ; Table 3 : probabilité de la classe prédite ≥ **0,8** pour les prédictions fermes.
- Raison : plomberie 0,980 et 1,000 ; P1, P4, P5, P7, P11 : 1,000 [M5 § 3, § 4]. Limite : sous un écart nul sur (ii), « sans régression » ne sort qu'avec 0,797 à S5 = 0,02 [M5 § 3d].

**S4 — nombre d'instances N par valeur de δ — DÉCIDÉ (R-739)**
- Valeur : **N = 100** (200 tâches), décidée par conv-audit sur délégation de Lazar (R-739), **après** lecture du pilote v3 ; champ `n_instances` de la configuration. Révision possible par D-T (option iii) ou D-Q2 (option b).
- Raison : S3 tenue sous le pilote v5 ; lectures simulées identiques à N = 80 et 60 [M5 § 4a] ; temps : D-T.

**S5 — tolérance de non-régression sur (ii), Δ(B, A)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02 (= S1)**, par principe. **Lecture sans seuil** recopiée dans tous les cas.
- Raison : sous le pilote, « régression avérée » 1,000 ; taille de « régression avérée » à l'écart −S5 : 0,006 ; sous un écart nul, « sans régression » 0,797 [M5 § 3d].

**S6 — marge des contrastes de Q1 (Table 3) et, sous l'option (b), de Q2 (Table 6)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **m = 0,02 (= S1)**, par principe (fixé au gel v3). Équivalence bilatérale : un témoin équivaut à B si leur écart est démontré dans ]−0,02 ; +0,02[.

**S7 — λ des « ou » déterministes C3 (et C3′_u sous l'option (b))**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **8** (gel v2).

**S8 — plafonds de temps (CM4-01, CM4-04)**
- Valeur (décision) : À REMPLIR — **décision D-T** ci-dessus ; en vigueur (R-739) : `timeout 9000`. **600 s de processeur par tâche** (garde interne `plafond_cpu_tache_s`, configuration : maximum mesuré 46,6 s).
- Valeur (audit d'attaquant indépendant, 20 tâches) : À REMPLIR par Lazar ; recommandation **`timeout 5400`**.
- Raison : D-T et [M5 § 5].

**S9 — taux de fausses alertes α et tolérances**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **α = 0,01** ; garde |taux mesuré − α| ≤ 0,005 par défense finale ; déclencheur |moyenne d'un bras − α| > 0,001 dans un δ.
- Raison : pilote v5, écart des moyennes à α ≤ 0,0003 ; écart entre bras par tâche moyen 0,0014 et 0,0013, maximum 0,0026 [M5 § 6].

**S10 — déclencheur « trop beau / trop mauvais » (CM4-03)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **k = 4** : audit si la moyenne de V d'un bras dans un δ sort de la bande moyenne pilote ± 4 × écart-type par tâche du pilote × √(1/24 + 1/N) ; plus la règle de Lazar : moyenne de V(B) ≥ 0,99. (k = 4 d'emblée au gel v5 § 4.3, après l'échec de k = 3 à 16 bandes en v4 ; repli fixé d'avance k = 5 si le taux simulé dépasse 0,05 : non déclenché.)
- Raison : taux simulés de fausse alerte sur les 12 bandes (6 bras × 2 δ ; 5 000 paires pilote / décision tirées par tâches entières du pilote v5) : k = 4 **0,010** ; k = 5 0,003 ; k = 3 0,049 (pour mémoire) [M5 § 7].
- Bandes à N = 100 (k = 4) [M5 § 7] : δ 1,4 : A [0,0348 ; 0,1880] ; B [0,1822 ; 0,2638] ; C1 [0,1680 ; 0,2504] ; C2 [0,1554 ; 0,2429] ; C3 [0,3733 ; 0,4242] ; D [0,4282 ; 0,4655] ; δ 1,6 : A [0,0078 ; 0,1150] ; B [0,1558 ; 0,2114] ; C1 [0,1307 ; 0,1978] ; C2 [0,1041 ; 0,1954] ; C3 [0,2912 ; 0,3394] ; D [0,3332 ; 0,3676]. Si N change, la bande se recalcule par la même formule ; sous l'option (b) de D-Q2, bandes des bras de Q2 à calculer sur le pilote à u = 2.

**S11 — budgets de comportement δ**
- Valeur : À REMPLIR par Lazar (confirmation).
- Recommandation : **δ = (1,4 ; 1,6)**, rendus en v4 par la règle du gel v4 § 2 (A seul, 48 instances) ; inchangés en v5.
- Raison et réserves : au pilote v5, V(A) = 0,111 (11 α, au-dessus de 10 α) au δ bas et 0,061 (6 α) au δ haut ; au pilote v4, 0,082 et 0,036 ; instabilité du couple sous rééchantillonnage déclarée au brouillon 4 (33 %).

**S12 — nombre de tours T** : À REMPLIR par Lazar. Recommandation **T = 8**.

**S13 — oracle du défenseur (identique pour tous les bras)** : À REMPLIR par Lazar. Recommandation **« détection »** (principe, § Hypothèse).

**S14 — seuil de contournement relatif κ** : À REMPLIR par Lazar. Recommandation **κ = 0,5**, garde κ × base ≥ 2α (mesure descriptive).

**S15 — marge de la condition d'application (Table 5)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02 (= S1)**, par principe (gel v3).
- Raison : sous le pilote v5, ligne « cycle » aux deux δ 1,000 ; tailles 0,002 à 0,013 (I1) et 0,001 à 0,019 (I3 − nul) [M5 § 3e].

**S16 — classe de Q2 (u\*, gel v5 § 2, additif b § 2.3)**
- Valeur : À REMPLIR par Lazar (confirmation du résultat de la règle et **décision D-Q2**).
- Recommandation : **u\* = 1, rendu par la règle sans choix à la main** ; avec l'option (a) de D-Q2 (Q2 retirée). Champ `unites_u` de la configuration (= 1 dans le bloc d'identité). Sous l'option (b) : `unites_u = 2`, identité à régénérer, nouveau gel et pilote.
- Raison : diagnostic (§ Prédiction A) : g_u (jeux dégénérés) 0,188 / 0,062 à u = 1 ; **0,312** / 0,062 à u = 2 ; 0,812 / 0,812 à u = 3 ; 1,000 à u = 5 et 9 ; seuil 0,25 aux deux δ.

**S17 — audit d'attaquant indépendant (déclencheur 9)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **K = 10 tâches de la décision par δ** (instances 0 à 9, 20 tâches), bras A, B, C3, D (et B_u, D_u, C3′_u sous l'option (b)) ; contrastes audités B − A, B − C3, B − D (et B_u − D_u, B_u − C3′_u), et la Table 5 (I1, I3 de A) ; critère inchangé depuis le brouillon 4 : artefact si (i) |c̄| > m/2 = 0,01 (pour la Table 5, |écart moyen de I1| > S15/2), ou (ii) |c̄| > t(K − 1 ; 0,995) × erreur-type **et** classe recalculée différente ; aucun changement de signe seul ; repli fixé d'avance t(K − 1 ; 0,9995) si la fausse alerte simulée dépasse 0,05 (non déclenché).
- Raison : audit d'essai v5 (instances 0 à 4 du pilote v5, aux deux δ, 10 tâches ; essai de fonctionnement) : écarts moyens de −0,0012 à +0,0022 sur les paires, |écart de I1| ≤ 0,0005 ; aucun drapeau (i) ni (ii) ; classes et lignes de la Table 5 inchangées [M5 § 8]. Fausse alerte simulée du critère complet (8 tests : 3 paires et la Table 5, aux deux δ) : **0,000** (écarts centrés), 0,001 (bruit d'écart-type double) ; puissance contre un écart systématique de 0,010 : 0,753 (B − C3) et 0,715 (B − D) ; de 0,015 : 1,000 [M5 § 8b]. Réserves : bruit estimé sur 5 tâches par δ ; I3 de A changé par l'audit des tours dans une tâche par δ (±0,033 en moyenne), (iii) des tours abaissé dans 41 tours sur 80 (baisse moyenne 0,0012).

**S18 — garde de convergence des entraînements — DÉCIDÉ (R-739)**
- Valeur : **0,10** par tâche, décidée par conv-audit sur délégation de Lazar (R-739), **après** lecture du pilote v3 ; champ `taux_nonconv_max`. Au diagnostic, appliquée à la tâche de diagnostic entière (toutes classes), comme à une tâche ordinaire.
- Raison : pilote v5 : 0 non-convergence sur 1 248 ; diagnostic : 8 sur 2 880 ; pilote v4 : 3 sur 1 632 dont 2 dans une tâche.

## Plan d'analyse

### 1. Monde
Loi propre N(0, I_6). Loi cible d'une instance : 3 composantes, moyennes de norme 4 dans des directions tirées, écarts-types 1. Loi d'attaque : 3 composantes appariées, moyennes et écarts-types diagonaux dans la boîte (|μ| ≤ 5, σ ∈ [0,5 ; 1,5]). Contrainte de comportement : racine de la moyenne sur k du carré de la distance de Wasserstein d'ordre 2 entre composantes appariées ≤ δ. **Inchangé depuis le brouillon 2** : la réécriture de la v5 ne touche ni au monde ni à l'attaquant ; elle change la **classe** à laquelle Q2 est posée (diagnostic, § Hypothèse).

### 2. Bras
Tour 0 commun : moniteur linéaire M0 entraîné contre la loi cible (reproductibilité bit à bit vérifiée par garde). Puis, pour t = 1 … T, dans chaque bras à trajectoire : l'attaquant calcule une meilleure réponse contre la défense déployée ; le défenseur se met à jour.
- **A, défense unique réentraînée, même oracle** : déploie le dernier moniteur linéaire, entraîné contre le **mélange uniforme de toutes les attaques passées** (meilleure réponse à l'historique, dernier itéré déployé).
- **B, mélange d'équilibre linéaire** : double oracle tronqué ; p = stratégie d'équilibre du défenseur sur la matrice G ; q = stratégie d'équilibre de l'attaquant ; nouveau moniteur **linéaire** entraîné contre q. Défense finale : p sur la matrice 9 × 9.
- **D, unique** : un seul maxout à t + 1 unités au tour t (9 à la fin), entraîné contre le mélange uniforme de ses attaques passées.
- **C1, C2, C3** sur les 9 moniteurs mêmes de B après le tour T (poids uniformes ; Dirichlet (1, …, 1) ; « ou » déterministe standardisé, λ = S7, seuil recalibré à α).
- **B_u (v5)** : identique à B, mais l'oracle rend à chaque tour un **maxout à u\* unités** (S16) ; défense finale : p sur M0 et les 8 maxouts.
- **D_u (v5)** : un seul maxout à **u\* unités à tous les tours**, réentraîné contre le mélange uniforme de toutes les attaques passées (A est D_1).
- **C3′_u (v5)** : « ou » déterministe standardisé (`MoniteurOu`) des 9 moniteurs mêmes de B_u.
- **M_u (v5, descriptif)** : le moniteur de poids maximal de B_u, déployé seul.
B′ et C3′ (9 unités, brouillons 3 et 4) ne sont plus dans la décision ; leur code est inchangé (essai `test_bras_v4_inchanges`). Pour chaque bras, la défense finale est figée ; l'attaquant joue en dernier avec les attaques passées de sa trajectoire comme départs supplémentaires.

### 3. Graines (R9)
- **RACINE = 20261201**, **RACINE_TENUE = 20261202** (décision, jamais employées). Racines d'essai v5, toutes dans 20264001 à 20264999, écrites au gel v5 (§ 1.1) avant emploi : 20264601 / 20264602 (diagnostic) ; 20264611 (jeux témoins) ; 20264621 / 20264622 (pilote v5 et audit d'essai v5) ; 20264631 / 20264632 (réservées, **non employées**) ; 20264641 / 20264642 / 20264643 (essais du code) ; 20264651 (simulations du calcul de puissance).
- **Refusées par garde** (`exiger_racine_permise`, appelée dans `gen`) : 20261101 ; 20261291 à 20261298 ; 20261301 ; 20261311 à 20261316 ; 20262291, 20262297, 20262313 ; 20269501 / 02 ; 20269731 / 32 ; 20269741 / 42 ; **toutes les racines de la v4** (20264101 / 102, 20264201 / 202, 20264211 / 212, 20264301 / 302 / 303, 20264401) ; 20264555, 20264777 (nommées par les essais v4) ; 20264001, 20264999 ; toute racine de 20265001 à 20265999 ; toute racine hors décision non gelée.
- Chaque tirage : `numpy.random.SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, rôle, …))`, numpy ≥ 1.25 ; schéma dans la configuration (`schema_graines`). B_u, D_u, C3′_u, M_u ont les codes 10, 11, 12, 13. Garde de la racine de décision dans `gen`, re-vérifiée dans chaque processus de travail.

### 4. Comparaisons et multiplicité
- **Table 1** : Δ(B, A) sur (iii), B2. **Table 2** : Δ(B, A) sur (ii), B2. **Table 5** : I1 et I3 − 0,7345 de A, B2 ; I2 recopié.
- **Q1 (Tables 3 et 4)** : Δ(B, C1), Δ(B, C2), Δ(B, C3), Δ(B, D), 8 tests, B8 et E8. **Q2 (Tables 6 et 7)** : Δ(B_u, D_u), Δ(B_u, C3′_u), 4 tests, B4 et E4.
- « Confirmée » = intersection-union ; « réfutée » = union protégée par la correction.
- **Descriptives** : Δ(B_u, M_u) (le tirage seul), Δ(B_u, B), Δ(D_u, A), Δ(D_u, D), Δ(C3′_u, D_u), Δ(M_u, D_u), Δ(C1, C2), Δ(C3, A), Δ(D, A) ; (ii) de B − C3, B − D, B_u − D_u, B_u − C3′_u ; I1, I2, I3 − nul de B, D, B_u, D_u ; matrices H moyennes ; coût, courbes, nouveauté ; poids, gain du mélange, part dégénérée, pureté, pureté forcée, ε-équilibres, dominance, indice du moniteur dominant ; contrôles.

### 5. Ordre d'exécution, arrêt et reprise
(1) Essais du code ; (2) **arbre git propre** (CM4-09) : `creer_manifeste` arrête sur un arbre non propre ; d'autres sessions laissent des fichiers non suivis dans le dépôt (relevé à 09:36 UTC : 9 entrées, dont 3 d'autres sessions) : avant le lancement, conv-audit committe ou isole ces fichiers (par exemple une copie de travail séparée par `git worktree`, au même commit), déclaré au journal ; (3) une seule invocation `PYTHONPATH=src timeout <S8> python3 arene_melange_v5.py decision --prereg prereg/<nom>.md --instances 0:<N> --run-id <AAAAMMJJ-HHMMSS-arene-melange-v5> --processus 2` ; les jeux témoins passent d'abord (garde) ; PID et instants de départ des processus de travail écrits et scellés dans `runs/<run-id>/pids-travail.txt` ; (4) analyse écrite par le même processus (`analyse-arene.json`, scellé) ; (5) si le déclencheur 9 (ou un autre imposant l'audit) est présent, `arene_melange_v5.py audit --prereg … --source-run <run-id> --instances 0:10 --run-id <run-id>-audit --S1 … --S6 … --S15 …` (valeurs gelées), sous `timeout` (S8, délai de l'audit) ; les tâches de la décision sont reconstruites et vérifiées **au bit près** contre le run audité avant l'attaquant indépendant ; (6) lecture par un sous-agent neuf (R13), qui applique les tables ; `lire_tables` et `classes_sous_audit` sont des aides mécaniques, le texte scellé fait foi.

**Condition de lancement (CM4-02, réécrite)** : machine sans autre calcul lourd au lancement, charge moyenne sur une minute < 0,5 relevée par `uptime` et consignée. **Cette condition réduit le risque, elle ne l'élimine pas** : l'audit d'essai v4 a démarré à charge 0,3 sur 2 cœurs et a fini à l'efficacité 0,51 parce que d'autres sessions ont démarré pendant le calcul (journal v4b, R2) ; rien dans le code ne surveille la charge pendant le run. **Conséquence d'un dépassement du délai** : le signal TERM arrête le pool, aucun résultat n'est écrit (aucun point de reprise partiel) ; une seule reprise complète est permise (même code, mêmes racines, nouvel identifiant de run, après la commande `orphelins` saine) ; une seconde interruption externe rend la décision **non concluante**. C'est l'argument du délai long de S8 (table de temps, résumé point 6).

**Reprise après arrêt** : (a) arrêt de cause **externe** (signal, `timeout`, machine), aucun résultat écrit : le signal TERM est converti en arrêt du pool ; arrêt par PID de tout survivant consigné et garde « aucun orphelin ». **Aucune reprise tant que `arene_melange_v5.py orphelins --pids runs/<run-id>/pids-travail.txt` ne rend pas « aucun processus de travail consigné ne tourne »** (avec `--arreter` : arrêt par PID, jamais par motif de ligne de commande, R10). Puis **une** reprise complète ; seconde interruption externe → non concluant ; (b) arrêt par une garde interne : pas de reprise → non concluant, version nouvelle du préenregistrement ; (c) aucun point de reprise partiel (déclaré). Réserve : le processus `resource_tracker` de multiprocessing n'est pas consigné.

### 6. Historique de conception (déclaré ; aucune décision n'a lu une racine de décision)
1. Oracle du défenseur, seuil de contournement, bras C1–C3 : brouillon 2. 2. Bifurcation v3 (Q2, B′, C3′, condition d'application, marges par principe) : gel v3. 3. Après le pilote v3 : R-739 (Q2 gardée, recalibrage, S18, N, délai) ; gel v4 ; pour la v4, le commit `f65feb1a` contient le gel **et aussi** le premier état du code v4, les essais et le script de puissance : l'antériorité du gel sur « toute ligne de code v4 » repose sur le journal v4 (déclaration plausible, non contredite) ; R-1031 a consigné le gel v4 (empreinte, racines, règle), sans l'heure ni les commits (CM4-05).
4. **Après le pilote v4 et la vérification courte (R-1034 point 5)** : gel v5 écrit à 09:14:23 UTC (`date -u` juste avant), avant toute ligne de code v5 ; code v5 commencé à 09:16:58 par copie du code v4 ; premier calcul v5 : les jeux témoins (09:22) ; **additif b** écrit à 09:23:52 après les seuls témoins (le témoin artefact a montré que la pureté forcée ne voit pas un point-selle) ; diagnostic lancé à 09:28:29 (code `1cdf4a58…`), fini à 10:00:28 ; règle appliquée : u\* = 1 ; **une seule ligne de configuration changée** (`UNITES_Q2_V5 = None` → `1`, code `2fe61869…`) ; puis la **branche « u\* = 1 »** écrite au gel v5 § 2 et § 6 (bras de la décision et de l'audit selon la classe, Table 7 « Q2 retirée ») — aucun chemin de calcul d'un bras changé : une tâche du diagnostic recalculée par le code final est identique au bit, et l'essai `test_bras_v4_inchanges` passe ; deux essais corrigés (syntaxe ; garde S18 relâchée dans un essai à deux bras) ; code du pilote `71df9a49…` (10:07:56) ; pilote 10:08–10:24 ; audit d'essai 10:24–10:32 ; puissance 10:32–10:36. **Aucun commit** (hors du droit de ce rédacteur) : l'ordre repose sur ce journal, sur les empreintes du gel et de l'additif épinglées dans le code (qui refuse de partir sans eux) et sur les manifestes des sorties (empreintes du code et du gel). À committer par conv-audit.
5. **Après le pilote v5** : aucun changement de conception ni de code. Viennent du pilote v5 : les chiffres des prédictions pour la décision, les bandes S10, la table de temps, les tailles et probabilités simulées.

## Critères de lecture gelés

Un sous-agent neuf (R13) applique ces tables telles qu'écrites. Chaque table se lit **de haut en bas ; la première ligne vraie décide** ; la dernière est le complémentaire. Notations, pour un contraste ou un indicateur à δ fixé : est = moyenne ; qX = quantile X du rééchantillonnage ; **B2 = B4** = [q0,00625 ; q0,99375] ; **B8** = [q0,003125 ; q0,996875] ; **E8** = [q0,00625 ; q0,99375] ; **E4** = [q0,0125 ; q0,9875].

**V0** = aucune condition de la liste d'arrêt ∧ tâches exécutées = 2 × N ∧ racines du manifeste = RACINE et RACINE_TENUE ∧ empreintes du code, de la configuration et de la bibliothèque = celles du texte scellé ∧ jeux témoins passés (sortie recopiée) ∧ une seule invocation ayant écrit des résultats (au plus une reprise complète après arrêt externe consigné et commande `orphelins` saine).

**Déclencheurs d'audit (R4), symétriques** — un seul suffit ; l'effet bloquant de chacun est écrit :
1. **Contradiction de la branche prédite, dans les deux sens** (§ Prédiction B) : (a) classe du signe opposé au signe prédit ; (b) classe prédite « ≈ » et observée autre ; (c) plomberie observée en ligne 5 ou 6 ; (d) (ii) borne basse B2 > 0 dans un δ ; (e) Table 4 « Q1 confirmée » ou « dépend de δ » ; (f) Table 7 autre que la ligne prédite (P10) ; (g) Table 5 autre que « A ne progresse pas, retours au-delà du hasard (cycle) » à un δ. *Bloque* : la table contredite et la phrase de synthèse ; (c) bloque la Table 1.
2. **Trop beau / trop mauvais** (S10) : moyenne de V d'un bras dans un δ hors de sa bande ; ou moyenne de V(B) ≥ 0,99. *Bloque* : toutes les tables.
3. **Règle de Lazar** (« si le mélange uniforme égale le mélange d'équilibre, audit ») : Δ(B, C1) « ≈ » dans un δ ; ou V(B) = V(C1) au bit près sur une tâche ; ou poids finaux de B uniformes (10⁻⁶) sur une tâche. *Bloque* : la classe de C1 dans la Table 3 seulement.
4. **Mélange B dégénéré** : poids de B purs sur plus de la moitié des tâches d'un δ. *Bloque* : Tables 1, 3, 4. (Pour B_u, la dégénérescence n'est pas un déclencheur : elle rend Q2 « non exercée » par la Table 7.)
5. **Optimiseur** : moyenne de (V standard − V renforcé) > 0,01 pour un bras dans un δ ; ou un contraste des Tables 1, 3, 6 qui diffère de plus de 0,01 entre attaquant standard seul et renforcé seul. *Bloque* : toutes les tables.
6. **Jeu restreint** : moyenne de (valeur du jeu restreint − V) < −0,01 pour B ou B_u dans un δ. *Bloque* : Tables 1, 3, 4 (B) ou 6, 7 (B_u).
7. **Capacité non exercée** : V(D) = V(A) au bit près sur toutes les tâches d'un δ, ou V(D_u) = V(A) au bit près sur toutes les tâches d'un δ. *Bloque* : Tables 3, 4 (D) ; 6, 7 (D_u).
8. **Dérive des fausses alertes** : |moyenne des fausses alertes finales d'un bras − α| > 0,001 dans un δ. *Bloque* : toutes les tables.
9. **Conforme et trop propre (R4, CM3-04)** : l'une des lectures prédites fermes sort conforme (P1 ; P4, P5, P7 ; P8 si ferme ; P10 ; P11). *Effet* : audit d'attaquant indépendant (S17) sur les 20 tâches de la décision, **après** scellement de l'analyse et **avant** la phrase de synthèse ; pour P10, la part des jeux restreints dégénérés et la part de pureté forcée de B_u sont recopiées ; *bloque* la phrase de synthèse des tables concernées jusqu'au rapport.

**Contenu de l'audit** (tout déclencheur) : relecture du code par un sous-agent neuf ; audit d'attaquant indépendant sur les **tâches de la décision** (S17 ; jamais sur la racine d'essai) ; vérification que B et B_u déploient les poids du programme linéaire, C1 l'uniforme, C2 les poids de Dirichlet de sa graine, C3 et C3′_u le « ou » des moniteurs de leur source, M_u le moniteur de poids maximal de B_u. **Issue** : « artefact trouvé » si et seulement si le rapport scellé constate une erreur de code, un chemin non exercé (hors la dégénérescence de B_u, lue par la Table 7), ou le critère de S17 ((i) ou (ii)) ; sinon « pas d'artefact ».

### Table 1 — contrôle de plomberie, Δ(B, A) sur (iii)

| # | Condition | Verdict |
|---|---|---|
| 0 | V0 fausse | **non concluant** ; aucune lecture |
| 1 | un déclencheur qui bloque la Table 1 (1c, 2, 4, 5, 6 pour B, 8, 9 pour P1) est présent et l'audit n'est pas rendu | **non concluant (audit en attente)** |
| 2 | audit rendu, artefact trouvé | **non concluant** ; version nouvelle du préenregistrement |
| 3 | dans un δ, la moyenne de V est ≤ 2α pour tous les bras calculés (M_u excepté) | **non concluant** : jeu dégénéré |
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

Déclaré, non corrigé (inchangé depuis le brouillon 4) : la ligne 5 recouvre aussi « borne haute < 0 dans un δ, borne basse < −S5 » (régression démontrée, ampleur non tranchée) ; la lecture sans seuil recopiée le dit. Option pour Lazar, avant gel : ajouter entre 2 et 3 la ligne « borne haute < 0 dans au moins un δ → régression démontrée, ampleur non tranchée ».

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

### Table 5 — condition d'application (défense unique A), par δ, bornes B2, marge S15

| # | Condition | Lecture à ce δ |
|---|---|---|
| 1 | borne basse de I1 > S15 | **A progresse** |
| 2 | borne haute de I1 < S15 ∧ borne basse de (I3 − 0,7345) > 0 | **A ne progresse pas, retours au-delà du hasard (cycle)** |
| 3 | borne haute de I1 < S15 ∧ borne haute de (I3 − 0,7345) < 0 | **A ne progresse pas, sans retours au-delà du hasard** |
| 4 | borne haute de I1 < S15 | **A ne progresse pas, forme indéterminée** |
| 5 | sinon | **indéterminé** |

Verdict : « **condition d'application vérifiée** » si A ne progresse pas (lignes 2 à 4) aux deux δ ; « **non vérifiée** » si A progresse à au moins un δ ; « **indéterminée** » sinon. I2, I3 brut, sa valeur nulle et les matrices H sont recopiés sans verdict. Au δ haut, A est bas : « ne progresse pas » y discrimine peu, ce que la phrase de synthèse recopie. **A est réentraîné contre le mélange uniforme de toutes les attaques passées** (une meilleure réponse à l'historique, au sens du jeu fictif côté défenseur, déployée en dernier itéré), pas contre la seule dernière attaque.

### Table 6 — Q2 : classement de X ∈ {D_u, C3′_u} à chaque δ, Δ(B_u, X) sur (iii)

Mêmes classes que la Table 3, avec **B4** à la place de B8 et **E4** à la place de E8, marge m = S6.

### Table 7 — Q2 (« à classe F_u égale, B_u bat D_u ; à moniteurs égaux, B_u bat C3′_u ») — réécrite (additif b § 2.4)

Statut par δ, dans cet ordre : « **non exercée (jeu dégénéré : gain du mélange ≤ 0,01 sur plus de la moitié des tâches)** » si le jeu restreint final de B_u est dégénéré (gain du mélange = valeur du jeu restreint − meilleur minimum de ligne pure ≤ τ = 0,01) sur plus de la moitié des tâches de ce δ ; sinon « **non exercée (pureté du sommet du solveur)** » si les poids finaux de B_u sont purs (un poids ≥ 1 − 10⁻⁹) sur plus de la moitié des tâches de ce δ ; sinon comme la Table 4 sur les deux témoins.

| # | Condition | Verdict |
|---|---|---|
| 1 | « non exercée » (l'une ou l'autre forme) à au moins un δ | **Q2 non exercée (au moins un δ)** ; statuts par δ, classes de la Table 6, part dégénérée, part pure, part de pureté forcée et B_u − X selon la pureté recopiés |
| 2 | « tenue » aux deux δ | **Q2 confirmée** |
| 3 | « réfutée » aux deux δ | **Q2 réfutée** |
| 4 | « tenue » à un δ, « réfutée » à l'autre | **Q2 dépend de δ** |
| 5 | sinon | **Q2 non tranchée** |

Lecture obligée de la ligne 1 : « à la classe u\* dans ce monde, le tirage ne peut rien gagner d'utile dans le jeu restreint (ou le solveur rend un sommet pur) ; la décision ne dit pas si le tirage est utile à cette classe ». **B_u − M_u** (le tirage seul, à moniteurs égaux, contre le meilleur d'entre eux) est recopié sans verdict dans tous les cas.

**Phrase de synthèse** (écrite par le lecteur R13 en recopiant, sans rien omettre) : « Table 1 : … ; Table 2 : … (sans seuil : Δ(B, A) sur (ii) = est [B2] à chaque δ) ; Table 5 : … (par δ ; I1, I3 − 0,7345 et I2 de A avec intervalles) ; Table 3 : C1 …, C2 …, C3 …, D … (par δ, avec est [B8]) ; Table 4 : … ; Table 6 : D_u …, C3′_u … (par δ, avec est [B4]) ; B_u − M_u (descriptif) ; part dégénérée, part pure et part de pureté forcée de B_u par δ ; Table 7 : … ; déclencheurs : … ; issue des audits : … ; jeux témoins : … ; portée : résultat local au monde, à l'oracle, aux δ, à T et à la classe u\* ». Les classes des Tables 3 et 6 sont toujours recopiées.

## Liste d'arrêt

Chaque garde du code (90 sites `raise GardeArret`, chacun avec un motif unique) a un essai nommé qui la provoque par son motif (`pytest.raises(…, match=motif)`) et un cas sain ; `test_chaque_garde_a_son_essai` contrôle par l'arbre syntaxique que chaque site a une entrée et un essai nommé existant (il ne prouve pas à lui seul que l'essai provoque le motif). Trois essais nommés n'ont pas leur cas sain dans la même fonction (CM4-08) : `test_jeu_artefact` (le sain est dans `test_jeu_sain`), `test_racines_essai_artefact` (le sain dans `test_racines_essai_sain`), `test_cli_diagnostic_refuse_autres_instances` (le cas sain 0:16 n'est pas essayé : trop long ; le diagnostic réel l'a exercé). Fichier d'essais : `essais/test_arene_melange_v5.py` (115 essais ; R5).

| Condition | Action | Garde et essai (R5 : cas sain et artefact, motif vérifié) |
|---|---|---|
| Lancement en décision ou en audit sans préenregistrement scellé, conforme, identifié | pas de départ ; aucune graine de décision | `autoriser_decision`, `exiger_prereg_arene`, `exiger_identite_prereg` ; `test_prereg_scelle_refus_pour_la_bonne_raison`, `test_identite_prereg_sain_et_artefacts`, `test_decision_refusee_copie_brouillon5_pour_la_bonne_raison` (copie temporaire : sans compagnon → « absente » ; scellée → « scellé mais non conforme : Seuil ; Contre-lecture ») |
| **Jeux témoins : chemin de calcul incapable de retrouver l'équilibre intérieur connu, ou témoin dégénéré non reconnu (v5)** | **pas de départ (tous les modes)** | `controle_temoins`, `exiger_temoin_interieur`, `exiger_jeu_non_degenere` ; `test_temoins_sain_et_artefacts` (sain : code réel ; artefacts : solveur à sommet pur, trois modes identiques, tolérance serrée, garde rendue aveugle) |
| **Bras de la classe F_u sans u fixé ; décision sans u\* ; mode de tâche inconnu (v5)** | arrêt | `exiger_classe_u`, `_exiger_config_v5`, `executer` ; `test_classe_u_sain_et_artefacts` |
| **Diagnostic sur d'autres instances que 0:16 ; règle de u\* sur un nombre de δ différent (v5)** | arrêt | `main` (diagnostic), `choisir_unites` ; `test_cli_diagnostic_refuse_autres_instances`, `test_diagnostic_sain_et_choix_de_u` |
| Audit d'un run lancé sous un autre préenregistrement | arrêt | `exiger_meme_prereg` ; `test_exiger_meme_prereg` |
| Graine tirée d'une racine de décision sans autorisation ; processus de travail sans préenregistrement | arrêt | `gen`, `_travail` ; `test_gen_garde_racine_de_decision`, `test_travail_refuse_racine_de_decision_sans_prereg` |
| Racine des v1 à v4 (gelées v4 comprises), racine de la plage 20265001–20265999, racine non gelée, racine de décision hors décision, racine des tenues égale à la principale | arrêt | `exiger_racine_permise` (dans `gen`), `exiger_racines_essai` ; `test_racines_essai_sain`, `test_racines_essai_artefact`, `test_liste_des_racines_deja_employees_complete`, `test_cli_essai_refuse_racines_interdites` |
| Gel v5 ou additif b absent, modifié, ou gel ne citant pas la racine (diagnostic, essai, audit d'essai, témoins) | arrêt | `exiger_gel_v5` ; `test_gel_v5_sain_et_artefacts` |
| Configuration incohérente (δ, effectifs, κ, fractions, oracle, B′ sans maxout, audit, classe et échelle de Q2, parts de la règle, témoins, τ) | arrêt | `exiger_config` ; `test_config_sain_et_artefacts` |
| Fichier de sortie, fichier de PID ou dossier de run existant | arrêt (R12) | `_exiger_absent`, `_ecrire_nouveau`, `creer_manifeste` ; `test_cli_refuse_d_ecraser`, `test_lancer_consigne_pids_sans_orphelin` |
| Arbre git non propre au lancement de décision ou d'audit | arrêt | `creer_manifeste` (essais du dépôt) ; voir § Plan 5 (CM4-09) |
| Programme linéaire non résolu ; primal ≠ dual ; matrice invalide ; programme de non-unicité non résolu | arrêt | `resoudre_jeu`, `poids_max_min_equilibres` ; `test_jeu_sain`, `test_jeu_solveur_artefacts`, `test_jeu_artefact`, `test_equilibres_poids_max_min` |
| Poids de mélange invalides | arrêt | `exiger_poids` ; `test_poids_sain_et_artefact` |
| Loi d'attaque non finie, hors boîte, ou à distance > δ | arrêt | `exiger_admissible` ; `test_admissibilite_sain_et_artefact` |
| Échantillons non multiples de K | arrêt | `echantillonner` ; `test_echantillonnage_stratifie` |
| Moniteur non fini, non calibrable, non calibré | arrêt | `Moniteur` ; `test_moniteur_gardes` |
| « Ou » déterministe sur un moniteur non linéaire ou de variance nulle ; « ou » composite vide ou d'un membre presque constant | arrêt | `ou_deterministe`, `MoniteurOu` ; `test_ou_deterministe_sain_et_artefacts`, `test_ou_composite_sain_et_artefacts` |
| Maxout sans graine ; entraînement non fini ; oracle inconnu | arrêt | `entrainer` ; `test_entrainement_gardes` |
| Aucun départ fini ; part de départs non finis > 5 % | arrêt | `meilleure_reponse`, `exiger_departs_finis` ; `test_meilleure_reponse_departs_non_finis`, `test_garde_departs_finis` |
| Fausses alertes d'une défense finale hors de α ± 0,005 | arrêt | `exiger_fpr` ; `test_garde_fausses_alertes_sain_et_artefact` |
| Part d'entraînements non convergés > S18 = 0,10 dans une tâche (au diagnostic : sur la tâche entière, toutes classes) | arrêt | `exiger_convergence` ; `test_garde_convergence_et_identite_tour0` |
| Moniteur du tour 0 non reproductible bit à bit | arrêt | `exiger_meme_moniteur` ; idem |
| Temps processeur d'une tâche > 600 s | arrêt | `exiger_plafond` ; `test_plafond_de_temps_processeur` |
| Bras ou témoin inconnu | arrêt | `trajectoire`, `defense_temoin`, `construire_defenses` ; `test_bras_inconnus` |
| Lecture de la Table 5 ou jugement d'audit sans I3 (T < 3) | arrêt | `lire_tables`, `classes_sous_audit` ; `test_lire_tables_refuse_sans_I3`, `test_classes_sous_audit_sain_et_artefacts` |
| Audit : bras absent, tâche absente, V ou I1 reconstruit ≠ run audité au bit près, moins de deux tâches par δ, marges invalides, autres instances que 0:10 ; pilote audité étranger | arrêt | `auditer_tache`, `auditer`, `juger_audit`, `_bornes_marges`, `main`, `charger_pilote` ; `test_audit_sain_et_artefacts`, `test_juger_audit_sain_et_artefacts`, `test_bornes_marges_et_cli_audit`, `test_audit_essai_refuse_pilote_etranger` |
| Processus de travail consigné encore vivant à la fin d'un lancement ou avant une reprise | arrêt (R10) ; pas de reprise | `exiger_aucun_orphelin`, `arreter_par_pid`, commande `orphelins` ; `test_arret_par_pid_sain_et_artefact`, `test_lancer_consigne_pids_sans_orphelin`, `test_signal_term_arrete_le_pool_par_pid` |
| Signal TERM (dont `timeout`) | arrêt consigné, pool terminé, survivants arrêtés par PID | `lever_sur_term` dans `_lancer` ; `test_signal_term_arrete_le_pool_par_pid` |
| Ligne de base du coût trop basse | mesure « non définie », comptée | `cout_contournement` ; `test_cout_contournement_ligne_de_base_et_bissection` |
| Reproductibilité ; bras v2, v3 ou v4 modifiés | constat d'essai | `test_reproductibilite_bit_a_bit_et_temoins`, `test_ordre_des_bras_sans_effet`, `test_bras_v2_inchanges`, `test_bras_v3_inchanges`, `test_bras_v4_inchanges` |
| Tâches ≠ 2 × N ; invocations hors § Plan 5 ; paramètre changé après lecture | V0 fausse | contrôle du lecteur R13 |
| Appel de modèle, réseau, dépense | arrêt (devis et GO exigés) | — |
| Lecture d'un résultat de décision avant scellement | arrêt et consignation (R1) | — |
| numpy < 1.25 | arrêt (R9) | `exiger_numpy_minimal` (essais du dépôt) |
| Marqueur de gel restant, ou contre-lecture sans ses deux empreintes | pas de scellement | validateur `problemes` ; `test_brouillon5_non_conforme_au_validateur_et_identite_du_code` |
| Ligne de gel absente de `registres/decisions.md`, valeurs différentes du texte ; remarques non traitées | pas de scellement ; contrôle manuel pour S1, S2, S3, S5, S6, S10, S15 ; les champs de configuration sont comparés par le code | `exiger_identite_prereg` |

## Rôles

- Auteur : voir l'en-tête (rédacteur neuf Opus 5.5) ; n'a écrit ni les brouillons 1 à 4, ni les codes v1 à v4, ni aucune contre-lecture ou vérification.
- **Vérification courte du brouillon 5 (R2)** : un sous-agent neuf **d'un modèle autre qu'Opus**, qui n'a écrit ni ce texte ni le code ; fichiers à lui donner explicitement : ce brouillon, `arene_melange_v5.py`, `essais/test_arene_melange_v5.py`, `gel-conception-arene-melange-v5.md`, `gel-conception-arene-melange-v5b.md`, `diagnostic-purete-arene-melange-v5.json`, `essai-pilote-arene-melange-v5-detection.json`, `audit-essai-arene-melange-v5.json`, `calcul-puissance-arene-melange-v5.py` et sa sortie (M5), `journal-pilotes-arene-melange-v5.txt`, `LISEZMOI-arene-melange-v5.md`, la vérification courte du brouillon 4 et le brouillon 4. Points à juger en priorité : honnêteté de l'additif b (écrit après les témoins seuls) ; la règle de u\* et son application ; la branche « u\* = 1 » ajoutée au code après le diagnostic ; D-Q2 et D-T ; CM4-01 à CM4-09.
- Lecteur de porte (R13) : sous-agent neuf, ni auteur ni vérificateur ni analyste ; applique les Tables 1 à 7 ; verdict scellé puis soumis à Lazar.
- Lazar : tranche **D-Q2** (nœud) et **D-T** (ou conv-audit par délégation R-739) ; gèle S1 à S3, S5 à S17 — **dont S8 (délai de la décision et délai de l'audit) et S16** — (S4 et S18 décidés, R-739) ; donne le GO de l'exécution de décision (processeur, aucune dépense).

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf Sonnet 5.5 ; brouillon relu : `preenregistrement-arene-melange-equilibre-v1-brouillon1.md` `5129b8c26d384e92015142e6d80c1d29f922210975fc297ec487efab070284ce` ; rapport : `contre-lecture-arene-melange-v1-brouillon1.md` `3721865417495678475ab995d43a3e56dd1b3b1df7b147a218f6ce9b0bc5bd1f`. Traitement au brouillon 2.

- **Contre-lecture 2** — sous-agent neuf Sonnet 5.5 ; brouillon relu : `preenregistrement-arene-melange-equilibre-v1-brouillon2.md` `622e50d2ad961654b6daaa96d76a94f6dfd2d67188d9f7af199979359c0a1891` ; rapport : `contre-lecture-arene-melange-v2-brouillon2.md` `c6751de38ca84f716d424bc34dccd4103757423932204011a65136bd861cc427`. Traitement au brouillon 3.

- **Contre-lecture 3** — sous-agent neuf Sonnet 5.5 ; brouillon relu : `preenregistrement-arene-melange-equilibre-v1-brouillon3.md` `3ac8fe1fd1ee4cdb6ebc904a739f8098226703b02b6c0be428e2a572449dced0` ; rapport : `contre-lecture-arene-melange-v3-brouillon3.md` `7ccc1460d6925fb1c743cb099a4490fcca2c7146c99ec4098e49234bb15dc236`. Traitement au brouillon 4 (tableau CM3-01 à CM3-17), reconduit ; deux traitements « en partie » (CM3-08, CM3-10) achevés par CM4-05 et CM4-01.

- **Contre-lecture 4 (vérification courte du brouillon 4)** — sous-agent neuf Sonnet 5.5 ; brouillon relu : `preenregistrement-arene-melange-equilibre-v1-brouillon4.md` `305911b7ab1945d7607377ede9c8cbfcf2257834bca6d6aadcf7c19be41f8160` ; rapport : `verification-arene-melange-v4-brouillon4.md` `28ab322f9d2e6098562d127f20e98560c4b202ef737b75ff217dfe0c9c7672f2`. Verdict : « gelable après corrections » (0 bloquant, 1 majeur, 2 moyens, 6 mineurs). Traitement : tableau CM4-01 à CM4-09 (§ Ce qui change) ; plus la réécriture du jeu décidée par Lazar (R-1034 point 5).

- **Contre-lecture 5 (vérification courte du brouillon 5)** — À REMPLIR : sous-agent neuf d'un modèle autre qu'Opus (identifiant), empreinte de ce brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque.
