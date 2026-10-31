# Préenregistrement — arène coévolutive synthétique : le mélange d'équilibre contre ses témoins, à nombre de paramètres égal (Q1) et à classe de fonctions égale (Q2) — v1 — BROUILLON 3 (non scellé)

**Statut : brouillon 3, non gelé ; contre-lecture 3 par un modèle autre qu'Opus ; seuils à Lazar.**

Identifiant : **PREREG-ARENE-MELANGE-EQUILIBRE-V1**. Tâche : piste 3 du brainstorm P-041 (« bras mélange contre défense unique » : un mélange d'équilibre de moniteurs passés serait-il la réponse à la non-convergence de la défense unique réentraînée de Bailey et collègues, arXiv `2412.09565` ?), décision de Lazar R-695 (« gooo », 31 octobre 2026), test (b), sur processeur ; brouillon 3 écrit après la contre-lecture du brouillon 2. Pilote de **mécanisme** : aucun modèle de langage, aucun texte. « L'attaquant » est un choix de paramètres dans une famille bornée de lois synthétiques.

- Auteur : sous-agent neuf Opus 5.5 (lignée conv-audit), branche `canal/conv-audit-n04` ; il n'a écrit ni les brouillons 1 et 2, ni les codes v1 et v2, ni les contre-lectures.
- Date (UTC) : 2026-10-31, 11:30 (relevé `date -u`).
- Commit du code d'analyse : À REMPLIR au gel (commit qui contient `arene_melange_v3.py` à l'empreinte du bloc d'identité). Le code remis n'est pas committé par l'auteur ; le champ `commit` des manifestes de pilote désigne le HEAD du dépôt au lancement (`050cd4e4` pour le pilote v3 ; HEAD à l'écriture : `1460fe8f`), arbre qui **ne contient pas** le code exécuté (CM2-16) : seule l'empreinte du code fait foi pour les pilotes ; la décision exige un arbre propre.
- Documents qui font foi (chemin + empreinte) :
  - `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/p-041-pont-vers-les-vrais-modeles-v1/brainstorm-malleabilite-et-arene-v1.md` — `08360a9402ff81d7d9146ed833d60e687f1be4d9acd0be3ab2867403dda8eb10` ;
  - `…/p-041-pont-vers-les-vrais-modeles-v1/reponse-pont-p041-vrais-modeles-v1.md` — `e98d9f5a0ccbf6a77675fc922b318eec67d4838acf3b1e0ea8657b79928155a3` ;
  - `docs/notes/anteriorite-P-041-v1/idee-P-041-est-elle-bonne-fusion-v3.md` (branche `origin/main`) — `343617ca195316a0339a8864eccf62f42275f551ee9144c3eaa6047ff7c02345` ;
  - brouillon 1 — `5129b8c26d384e92015142e6d80c1d29f922210975fc297ec487efab070284ce` ; contre-lecture 1 — `3721865417495678475ab995d43a3e56dd1b3b1df7b147a218f6ce9b0bc5bd1f` ;
  - brouillon 2 `preenregistrement-arene-melange-equilibre-v1-brouillon2.md` — `622e50d2ad961654b6daaa96d76a94f6dfd2d67188d9f7af199979359c0a1891` ; contre-lecture 2 `contre-lecture-arene-melange-v2-brouillon2.md` — `c6751de38ca84f716d424bc34dccd4103757423932204011a65136bd861cc427` ;
  - gel v2 `gel-conception-arene-melange-v2.md` — `1628515a8cf2955f328e5785e5de3ec4279211bec73bea47e870413781292b83` ; calibrage des δ `calibrage-deltas-arene-melange-v2.json` — `f887e9c1051f40490e7c72c24fa74680f6b4e7818c0c9343d6e63a58c8ba933e` ; pilotes v2 `essai-pilote-arene-melange-v2-detection.json` — `121580c88d580fdd88460eb2352455121ce1c9680ba7e0e30a5f7e23ae4d166d`, `…-logistique.json` — `a948c85a0dc074559133bc29067f6ed4975a1c0818426773822e8b6b5ac70d01` ;
  - gabarit `prereg/gabarit-preregistrement-v1.md` — `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e`.
- Code et sorties v3 (dossier `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/arene-melange-equilibre-v1/`) :
  - `arene_melange_v3.py` — voir le bloc d'identité (le code de décision **refuse de partir** si son empreinte, celle de la configuration, celles des quatre fichiers de la bibliothèque et les versions de numpy et scipy n'apparaissent pas dans le texte scellé, ou si la configuration du texte diffère champ à champ) ;
  - `essais/test_arene_melange_v3.py` — `3fa646dbf132c813d924511c1e8fd7f190a2924049949d93c3b8003b17bc0051` ;
  - `gel-conception-arene-melange-v3.md` — `25035088a36742db86c3b6be818e5c97fabd8dd48c1f9e56934fce15e9f09506` (conception v3 et prédictions Q2 écrites **avant** toute exécution de B′) ;
  - `essai-pilote-arene-melange-v3-detection.json` — `e171e303330e47195757a9855a55181aea1bf1f75078fa9c6c7891033221427d` ; `essai-pilote-arene-melange-v3-pids.txt` — `4a767a82d99dda69d350f172f858430c1ddc70a5c1832a6497de4e5a91c94736` ;
  - `audit-essai-arene-melange-v3.json` — empreinte au LISEZMOI v3 et au journal ;
  - `calcul-puissance-arene-melange-v3.py` — empreinte au LISEZMOI v3 ; sa sortie `calcul-puissance-arene-melange-v3-sortie.txt` — `00a2234972c7bc0f0138a5c3e2c6b9fc1c6810b7c888b1b91342aecd10e434e5` (désignée **(M3)**) ;
  - `journal-pilotes-arene-melange-v3.txt` (commandes, horodatages, empreintes, ordre des étapes).
- Codes v1 et v2 et leurs configurations : cités seulement abrégés (`6402dc6b…`, `6685585f…`, `8e1e651b…`, `1d7544e6…`), pour qu'aucun des deux codes, qui cherchent leurs empreintes complètes, ne puisse partir sur ce texte (essai).

Tout nombre de ce texte vient de (M3) (section citée, par exemple [M3 § 3b]), du fichier de gel v3, du pilote v3, de l'audit d'essai, ou des fichiers v2 cités ; ou est un marqueur de gel. **Aucune lecture n'a été faite sur la racine de décision RACINE = 20261201 ni sur RACINE_TENUE = 20261202.**

### Bloc d'identité (vérifié par le code ; à régénérer par `arene_melange_v3.py identite` si le code ou la configuration change)

- Identifiant : PREREG-ARENE-MELANGE-EQUILIBRE-V1
- Racines de décision : RACINE = 20261201 ; RACINE_TENUE = 20261202
- Code : `arene_melange_v3.py` — 88c8781815007d92d5b0af17a7dc1995c00eae0773085c5a0ca35a1aafee4f0d
- Configuration (empreinte de la forme canonique) : 02db9c9183f4f601d9a77fd956f61f92de3bbafe31d78b809096743c6b15ac44
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
 "audit_critere": 0.05,
 "audit_departs": 100,
 "audit_es_generations": 400,
 "audit_es_lambda": 12,
 "audit_iter": 300,
 "audit_n_mc": 1024,
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
 "schema_graines": "SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, role, ...)) ; bras commun 0, A 1, B 2, D 4, C1 5, C2 6, C3 7, B' 8, C3' 9 ; roles cible 0, propre 1, attaques d'entrainement 2, calibration 3, fausses alertes 4, Monte-Carlo 5, departs 6, evaluation 7, init maxout 8, lois tenues 9, echantillons tenus 10, final 11, cout 12, Dirichlet 13, courbe 14, attaquant independant 15 ; reechantillonnage (code_delta, code_contraste, 0, 0, 99)",
 "seuil_calibrage_bas": 0.1,
 "seuil_calibrage_haut": 0.03,
 "sigma_cible": 1.0,
 "sigma_max": 1.5,
 "sigma_min": 0.5,
 "tau": 0.25,
 "taux_departs_non_finis_max": 0.05,
 "taux_nonconv_max": 0.05,
 "tol_fpr": 0.005,
 "unites_Bp": 9
}
```
<!-- configuration-canonique-fin -->

## Résumé pour Lazar

1. **Deux questions.** Q1 (celle du brouillon 2) : le mélange d'équilibre de moniteurs linéaires B bat-il ses témoins **à nombre de paramètres égal** (63) — C1, C2, C3, D ? B déploie 7 paramètres par requête, C3 et D les 63. Q2 (nouvelle, CM2-02) : **à classe de fonctions égale**, le mélange d'équilibre B′ (double oracle dont l'oracle rend des maxouts à 9 unités, la classe de D) bat-il D et C3′ (« ou » des moniteurs de B′) ? Q2 est une **bifurcation de conception postérieure au pilote v2**, décidée en routine par conv-audit, déclarée ; ses prédictions sont écrites avant toute exécution de B′ (gel v3).
2. **Condition d'application mesurée (CM2-03)** : au pilote v3, la défense unique A **ne progresse pas** (I1 = −0,001 aux deux δ) et **oublie** (I2 = +0,07 et +0,11 : le moniteur final détecte mal les attaques passées) ; les attaques reviennent vers d'anciennes dans 88 % et 93 % des tours. L'arène exhibe donc une non-convergence de la défense unique **analogue** à celle de Bailey (Table 5, prédite et tenue au pilote).
3. **Q1, pilote v3 (racine fraîche 20261311, 24 instances × 2 δ)** : réplique le v2. B − A = +0,104 / +0,118 ; B − C1 = +0,021 / +0,017 ; B − C2 = +0,030 / +0,035 ; B − C3 = −0,174 / −0,078 ; B − D = −0,223 / −0,104 [M3 § 2]. Q1 réfutée (C3 et D font mieux que B).
4. **Q2, pilote v3** : B′ − D = +0,001 / +0,009 ; B′ − C3′ = +0,008 / +0,029 ; B′ − B = +0,224 / +0,113 [M3 § 2]. **Ma prédiction Q2 (D ≥ B′ et C3′ ≥ B′) est réfutée** pour le signe ; surtout, les poids de B′ sont **purs dans 62 % et 54 % des tâches** (support moyen 1,4 et 1,8) : à classe de fonctions égale, l'équilibre du jeu restreint est presque pur, le tirage au hasard n'est presque pas exercé. Sous la règle gelée (Table 7, ligne « non exercée »), la décision lirait « Q2 non exercée » avec une probabilité simulée de 0,998 [M3 § 4]. Ce n'est pas corrigé après coup : c'est le résultat le plus informatif du pilote, déclaré.
5. **Marges par principe, sans pilote (CM2-04)** : m = S1 = 0,02 pour tous les témoins de Q1 et de Q2, équivalence bilatérale ; plus aucune marge ne dépend de B − A.
6. **Erreurs, mesurées avec le rééchantillonnage réel de la décision (CM2-07)**, 1 000 répétitions par scénario [M3 § 3] : plomberie, taille 0,000 sous effet nul ; Q1, tailles jusqu'à 0,008 (supériorité, nominal 0,003), 0,013 (« X > B ») et 0,017 (équivalence, nominal 0,006) ; Q2 jusqu'à 0,010, 0,015 et 0,026 (nominaux 0,006 et 0,013). Dépassements déclarés.
7. **Temps** [M3 § 5] : 57,0 s de processeur par tâche (8 bras) ; N = 100 → **120 min de mur sur 2 cœurs** (machine partagée, efficacité 0,80) ; N maximal sous 1 h 15 : 62. Recommandation : N = 100 sous `timeout 9000` ; option N = 60 sous `timeout 5400`.
8. **Dix-huit seuils** à geler (S1 à S18), aucun défaut. Nouveaux : S15 (marge de la condition d'application), S16 (unités de B′), S17 (audit d'attaquant indépendant), S18 (garde de convergence : 2 non-convergences sur 1 632 au pilote ; à 5 % par tâche, la décision s'arrêterait par garde avec une probabilité estimée de 0,16 ; recommandation 0,10).
9. **δ inchangés** (1,4 ; 1,8) ; A est près du plancher à δ 1,8 (1,5 α au pilote v2, 2,7 α au pilote v3, CM2-06) : la Table 1 à δ 1,8 mesure B contre un A presque nul. Option écrite : recalibrer sur ≥ 48 instances de la racine réservée 20261315 avant scellement — décision de Lazar.
10. **Portée** : tout résultat est local (monde gaussien, classe d'oracle, δ, T) ; il ne réfute ni ne confirme la piste 3 sur de vrais moniteurs (rubrique « Portée »).
11. Avant scellement : contre-lecture 3 par un modèle autre qu'Opus (R2), gel des seuils par Lazar, empreintes recalculées si une valeur change.

## Ce que l'expérience n'autorise pas

- **Rien sur les vrais modèles** ni sur les moniteurs d'activations réels : ni Llama, ni les sondes de Bailey et collègues, ni la boucle à 70 tours. Le monde est une famille de lois que nous avons écrite (`reponse-pont-p041-vrais-modeles-v1.md` § 0).
- **A n'est pas le protocole de Bailey** : même oracle « détection » que les autres bras ; tout énoncé est conditionnel à cet oracle. La non-convergence de A mesurée ici (Table 5) est une **analogie** de celle de Bailey, pas sa reproduction.
- **Rien sur l'équilibre du jeu complet** : B et B′ sont des itérés du double oracle tronqué à 8 tours ; écarts « valeur du jeu restreint − V » au pilote v3 : B +0,016 / +0,030 ; B′ +0,004 / +0,005 [M3 § 6].
- **Q1 n'est pas « à capacité égale »** : à nombre de paramètres égal (63), B déploie 1/9 des paramètres à chaque requête, C3 et D les déploient tous. Une réfutation de Q1 dit que la classe de fonctions déployée compte, pas que le tirage au hasard est inutile.
- **Q2 n'est pas « à paramètres égaux »** : B′ et D déploient la même classe (maxout à 9 unités, 63 paramètres par requête) ; B′ stocke 511 paramètres, D 63. B′ et C3′ ont les mêmes moniteurs et le même total (511). **Un maxout unique de 73 unités (même total que B′) n'est pas dans l'expérience** : lacune déclarée.
- **Monde favorable au « ou » déterministe** : queues gaussiennes, moniteurs peu nombreux ; rien sur des queues lourdes ni des dizaines de sondes.
- Deux budgets seulement, choisis sur A seul ; A près du plancher au budget haut (CM2-06).
- Aucune revendication d'antériorité ni de nouveauté (R8) ; références **SUPPOSÉ**.
- Aucun énoncé sur des moniteurs quadratiques, des réseaux profonds, d'autres dimensions, d'autres familles, ni un attaquant en boîte noire.
- (iii) est une **borne haute** de la valeur du jeu (l'attaquant est un optimiseur local), contrôlée par un attaquant indépendant (S17).
- Ni porte, ni dépense, ni modification de P-041 : pièce pour le tour 2 du collisionneur et la décision de Lazar sur P-041 v2.

## Portée d'une réfutation et d'une confirmation

- **Toute lecture est locale** : monde (gaussien, d = 6, K = 3), classe d'oracle du défenseur (linéaire pour B, maxout à 9 unités pour B′ et D), oracle « détection », δ ∈ {1,4 ; 1,8}, T = 8, attaquant local en boîte blanche.
- **Q1 réfutée** établit : dans ce monde, un « ou » déterministe des mêmes moniteurs linéaires et un maxout de même total font mieux que leur mélange d'équilibre. Elle **ne réfute pas** la piste 3 et ne dit rien du mélange à classe de fonctions égale.
- **Q2 réfutée** (B′ ne bat pas D ou C3′ d'au moins 0,02) établirait : à classe égale, dans ce monde, le tirage au hasard n'apporte pas d'effet d'intérêt. **Q2 confirmée** établirait : à classe égale, dans ce monde, le mélange d'équilibre bat le moniteur unique et l'agrégation déterministe. **Q2 non exercée** établit : à classe égale, l'équilibre du jeu restreint est presque pur ; la question du tirage au hasard ne se pose pas dans ce monde (ni pour, ni contre).
- **Aucune lecture ne réfute ni ne confirme la piste 3 sur de vrais moniteurs** (queues lourdes, dizaines de sondes, attaquants en boîte noire, oracle de régression). Au mieux, elle indique quelle classe de moniteurs tester ensuite.
- **Condition d'application (Table 5)** : si A progresse, la lecture de Q1 et Q2 ne dit rien de la réponse à une non-convergence (la condition n'y est pas réunie) ; si A ne progresse pas, Q1 et Q2 portent sur un monde où la défense unique ne converge pas, ce qui est la situation visée par la piste 3 — toujours dans ce monde seulement.

## Antériorité (toutes SUPPOSÉ, non lues sur PDF pour ce texte)

Double oracle (McMahan, Gordon et Blum 2003) ; réponse stratégique à une population de politiques (Lanctot et collègues 2017) ; défenses randomisées contre attaques adverses (Pinot et collègues 2020). Bailey et collègues, arXiv `2412.09565v2`, lu sur PDF par session-depot (R-874) : seule l'idée de la boucle est reprise (réentraînement d'un moniteur sur toutes les attaques passées, attaquant qui répond au dernier moniteur), avec un autre oracle ; **aucun chiffre** de ce papier n'est repris (R7). La convention de non-infériorité citée au brouillon 2 n'est plus employée (marges par principe).

## Hypothèse

Renvoi : brainstorm P-041 piste 3 (« la réponse correcte à une suite de meilleures réponses adverses est un mélange aux poids d'équilibre ») ; pistes 2, 4, 5 ; scores (i), (ii), (iii) de la fusion v3.

**Principe de l'oracle du défenseur (S13), énoncé avant toute observation de la v2** (l'oracle avait été changé au brouillon 1 après une observation sur une instance, archivée ; CM2-11). Le double oracle converge vers l'équilibre du jeu résolu si chaque oracle rend une meilleure réponse **pour le gain de ce jeu** (matrice G des taux de détection au seuil α). La régression logistique n'en est pas une ; elle n'exerce pas le chemin testé. L'oracle retenu maximise le taux de détection lissé au seuil α, **le même pour tous les bras**. A est donc une « défense unique réentraînée, même oracle », pas le protocole de Bailey ; tout est conditionnel à cet oracle. Sous l'oracle logistique, le pilote v2 montre que le mécanisme n'est pas exercé et que D > B aussi : le choix de l'oracle décide si la plomberie est exercée, pas le verdict de Q1 (CM2-02).

**Bifurcation v3 (déclarée)** : Q2, B′, C3′ et les mesures de la condition d'application sont ajoutés **après** la lecture du pilote v2 et de la contre-lecture 2 (gel v3, § 0) ; toutes les racines d'essai déjà employées sont refusées par garde ; les bras A, B, C1, C2, C3, D sont inchangés (essai `test_bras_v2_inchanges` : sorties identiques champ à champ au code v2 sur une même racine).

- **Q1 (hypothèse principale 1)** : contre la meilleure réponse adverse finale, le mélange d'équilibre B bat chacun des témoins **à nombre de paramètres égal** — C1 (mêmes 9 moniteurs, poids uniformes), C2 (poids de Dirichlet), C3 (« ou » déterministe), D (maxout unique à 63 paramètres) — d'au moins m = S6, aux deux δ. H0 : pour au moins un témoin et un δ, non.
- **Q2 (hypothèse principale 2)** : à classe de fonctions égale, le mélange d'équilibre B′ (maxouts à S16 unités) bat D (maxout unique de même classe, mêmes paramètres déployés par requête) et C3′ (« ou » déterministe des moniteurs mêmes de B′, même total) d'au moins m = S6, aux deux δ. H0 : pour au moins un témoin et un δ, non. Si les poids de B′ sont purs sur plus de la moitié des tâches d'un δ, Q2 est « non exercée » (R5, chemin non exercé).
- **Condition d'application** : la défense unique A ne progresse pas d'un tour à l'autre (I1) ; descriptif de sa forme (oubli I2, retours I3).
- **Questions qualifiantes** (Table 3) : C1, rôle des poids d'équilibre ; C2, poids d'équilibre contre poids quelconques ; C3, tirage au hasard contre agrégation déterministe des mêmes moniteurs linéaires ; D, mélange linéaire contre moniteur unique plus riche. C1 et C2 ne changent pas la Table 4, dont le verdict est porté par C3 et D ; « Q1 confirmée » exige pourtant les quatre.
- **Contrôle de plomberie PC** : B bat A sur (iii) aux deux δ.
- **Non-régression** : Δ(B, A) sur (ii), tolérance S5, lecture sans seuil recopiée.
- **Hypothèses de travail** : oracle du défenseur approché (approché aussi pour les maxouts de D et B′ : seuil gaussien, deux départs) ; attaquant approché, contrôlé par un attaquant renforcé et par l'attaquant indépendant de S17 ; loi propre N(0, I) connue du code, pas des bras ; B et B′ itérés tronqués.

## Prédiction chiffrée et signe attendu

**La décision est une réplication de pilotes concluants (CM2-09)** : les probabilités simulées ci-dessous sont **conditionnelles au pilote v3** pris pour vérité ; la décision peut encore surprendre (le pilote ne compte que 24 instances), et toute surprise déclenche l'audit. Valeurs non opposables ; la décision se lit sur RACINE, jamais lue.

### A. Prédictions des gels et leur sort

Gel v2 (avant le pilote v2) : 16 branches, 12 tenues, 4 réfutées (« B ≈ C1 à 0,01 près », « poids purs sous l'oracle logistique ») ; détail au brouillon 2. Gel v3 (`gel-conception-arene-melange-v3.md`, écrit à 10:24 UTC, avant toute exécution de B′ ; essais de B′ à partir de 10:29 UTC ; pilote v3 lancé à 10:39 UTC), sort au pilote v3 [M3 § 2, § 6] :

| Prédiction du gel v3 (avant) | Pilote v3, δ 1,4 ; δ 1,8 : moyenne [IC95] | Sort |
|---|---|---|
| B′ − D −, centre −0,03, dans [−0,10 ; +0,02] (0,60 ; 0,55) | +0,0009 [−0,0037 ; +0,0057] ; +0,0091 [+0,0043 ; +0,0138] | **réfutée** (signe) aux deux δ ; l'ordre de grandeur tient (\|·\| < 0,01) |
| B′ − C3′ −, centre −0,04 (0,70 ; 0,65) | +0,0084 [+0,0040 ; +0,0133] ; +0,0285 [+0,0225 ; +0,0353] | **réfutée** aux deux δ |
| B′ − B + (0,80) | +0,2241 ; +0,1133 | tenue |
| C3′ − D + (0,55) | −0,0075 [−0,0156 ; +0,0001] ; −0,0194 [−0,0281 ; −0,0112] | **réfutée** aux deux δ |
| Poids de B′ : part pure ≤ 0,5, support ≥ 2 (0,55) | part pure 0,62 ; 0,54 ; support 1,42 ; 1,79 | **réfutée** aux deux δ : Q2 « non exercée » au sens de la Table 7 |
| A, \|I1\| < 0,02 (0,75) | −0,0013 B2 [−0,0102 ; +0,0060] ; −0,0015 B2 [−0,0041 ; +0,0009] | tenue |
| A, I2 > 0,02 (0,65) | +0,0718 B2 [+0,0524 ; +0,0916] ; +0,1140 B2 [+0,0867 ; +0,1417] | tenue |
| Table 5 « A ne progresse pas, avec oubli » (0,5) | idem aux deux δ | tenue |
| B, D, B′ : I1 > 0 (0,8) | B +0,078 ; +0,075 ; D +0,158 ; +0,129 ; B′ +0,123 ; +0,110 | tenue |
| Q1 : signes du v2 (0,7 à 0,9) | B − A +0,104 ; +0,118 ; B − C1 +0,021 ; +0,017 ; B − C2 +0,030 ; +0,035 ; B − C3 −0,174 ; −0,078 ; B − D −0,223 ; −0,104 ; (ii) B − A −0,082 ; −0,094 | tenue (12 branches) |
| Temps : 45 à 70 s par tâche | moyenne 57,0 s, maximum 79,8 s | tenue (moyenne) |
| Lecture Q2 prédite « réfutée » (0,6) | sous la règle gelée : « non exercée » | **réfutée** |

Bilan v3 : 36 branches (hors temps et lecture), 28 tenues, 8 réfutées, **toutes du côté de Q2**. Raisonnement réfuté : j'attendais (§ 2.1 (d) du gel) que l'oracle de B′, entraîné contre une stratégie d'attaque concentrée, produise des moniteurs plus spécialisés que D ; en fait, à 9 unités, le moniteur entraîné contre l'équilibre de l'attaquant domine presque toujours les précédents dans le jeu restreint, et B′ se réduit à un maxout unique (poids maximal moyen 0,89 et 0,82) aussi bon que D. C3′ perd un peu contre B′ parce qu'il agrège aussi les moniteurs faibles des premiers tours et paie le resserrement du seuil.

### B. Prédictions pour la décision, par contraste et par δ

Classe prédite sous les valeurs recommandées (S1 = S5 = S6 = S15 = 0,02), estimation du pilote v3, probabilité simulée de la classe à N = 100 avec la règle réelle [M3 § 3, § 4], confiance (probabilité arrondie vers le bas à 0,05, plafonnée à 0,95), branche opposée (réfutation → audit, déclencheur 1). **Prédictions fermes : les signes, P4, P5, P6, P7, P8, P10 et P11. Les classes de C1 (P2) et C2 (P3) ne sont pas prédites avec confiance (CM2-13).**

| # | Contraste | δ | Signe | Classe prédite | Pilote v3 : moyenne | Probabilité simulée | Confiance | Branche opposée |
|---|---|---|---|---|---|---|---|---|
| P1 | B − A (iii), plomberie | 1,4 ; 1,8 | + | « mécanisme exercé » | +0,1036 ; +0,1176 | 1,000 | 0,95 | Table 1 ligne 5 ou 6 |
| P2 | B − C1 (iii) | 1,4 ; 1,8 | + | « B ≳ C1 » (non ferme) | +0,0208 ; +0,0166 | 0,985 ; 0,857 (« ≈ » 0,143 à δ 1,8) | — | signe contraire (« C1 ≳ B », « C1 > B ») |
| P3 | B − C2 (iii) | 1,4 ; 1,8 | + | « B > C2 » (non ferme) | +0,0304 ; +0,0354 | 0,994 ; 0,996 | — | signe contraire |
| P4 | B − C3 (iii) | 1,4 ; 1,8 | − | « C3 > B » | −0,1735 ; −0,0779 | 1,000 | 0,95 | « B > C3 », « B ≳ C3 » |
| P5 | B − D (iii) | 1,4 ; 1,8 | − | « D > B » | −0,2231 ; −0,1042 | 1,000 | 0,95 | « B > D », « B ≳ D » |
| P6 | B − A (ii) | 1,4 ; 1,8 | − | Table 2 « régression avérée au-delà de la tolérance » | −0,0819 ; −0,0937 | 1,000 | 0,95 | borne basse B2 > 0 dans un δ |
| P7 | Q1 (Table 4) | — | — | « Q1 réfutée » (C3 et D) | — | 1,000 | 0,95 | « Q1 confirmée », « Q1 dépend de δ » |
| P8 | B′ − D (iii) | 1,4 ; 1,8 | ≈ 0 | « ≈ » | +0,0009 ; +0,0091 | 1,000 ; 1,000 | 0,95 | « B′ > D » ou « D > B′ » |
| P9 | B′ − C3′ (iii) | 1,4 ; 1,8 | + | « ≈ » (δ 1,4) ; « B′ > C3′ » (δ 1,8) | +0,0084 ; +0,0285 | 1,000 ; 1,000 | 0,95 (signe) ; classes non fermes | « C3′ > B′ », « C3′ ≳ B′ » |
| P10 | Q2 (Table 7) | — | — | « Q2 non exercée (au moins un δ) » | part pure 0,62 ; 0,54 | 0,998 (« Q2 réfutée » 0,002) | 0,95 | « Q2 confirmée », « Q2 dépend de δ » ; « Q2 réfutée » (exercée) est aussi une surprise |
| P11 | Table 5 | 1,4 ; 1,8 | — | « A ne progresse pas, avec oubli » ; condition vérifiée | I1 −0,001 ; I2 +0,07 ; +0,11 | 1,000 | 0,95 | « A progresse » ; « sans oubli » |

Descriptives du pilote v3 (sans verdict) [M3 § 6] : (iii) par tour, A plat (0,079 → 0,073), B croissant (0,080 → 0,182), D et B′ croissants puis plats (≈ 0,35 dès le tour 4) ; nouveauté résiduelle au tour 8 de 0,135 (B′) à 0,187 (D) ; matrice H de A : chaque moniteur détecte bien l'attaque sur laquelle il vient d'être entraîné (rétention k = 0 : 0,35) mais mal la suivante (0,12 et 0,03) et de moins en moins les anciennes ; coût par contournement défini partout, censuré à δ 1,4 pour B 0,67, B′ 0,50, D 0,54, C3′ 0,25 ; fausses alertes moyennes à 0,0006 de α au plus ; 2 entraînements non convergés sur 1 632 ; 2 départs SLSQP sur 35 904 au statut 9 (limite d'itérations), une réponse à la limite.

**Lecture anticipée**, à ne pas confondre avec un résultat : si la décision réplique le pilote, (a) la défense unique ne converge pas et oublie ; (b) un mélange d'équilibre de moniteurs linéaires la bat, mais un « ou » de ces moniteurs et un maxout de même total font beaucoup mieux (Q1) ; (c) à classe de fonctions égale, le double oracle converge vers un équilibre presque pur, aussi bon que le maxout unique (B′ ≈ D) : **dans ce monde, ce qui guérit la non-convergence de la défense unique est la richesse de la classe déployée, pas le tirage au hasard** ; le tirage n'y est ni utile ni nuisible, il n'est presque pas employé. Conditionnel au monde, à l'oracle et aux budgets.

## Métrique

Notations : une **tâche** = (δ, instance) ; les deux δ partagent la loi cible d'une instance. Taux de détection d'une défense mixte {(m_i, p_i)} sur une loi Q : Σ_i p_i × part des échantillons de Q dont le score dépasse le seuil t_i de m_i ; seuils calibrés au quantile 1 − α de 20 000 échantillons propres communs (α = S9).

- **(iii), principale, V(bras)** : après T tours (S12), défense figée ; deux meilleures réponses sous la contrainte distance ≤ δ et la boîte : **standard** (12 départs tirés + départ vers l'origine + attaques passées de la trajectoire — celles de B pour C1, C2, C3, celles de B′ pour C3′ —, 512 échantillons de Monte-Carlo par composante, 100 itérations) et **renforcée** (48 départs, 200 itérations, plus la réponse standard) ; chacune évaluée sur 19 998 échantillons frais ; **V = la plus basse des deux détections** (biais d'au plus un écart d'échantillonnage, ≈ 0,001 à 0,003, en faveur de l'attaquant, pour tous les bras).
- **Écart apparié** Δ(X, Y) = moyenne sur les instances de V(X) − V(Y), à δ fixé.
- **Paramètres** : stockés (somme sur les moniteurs de la défense finale) et **déployés par requête** (maximum sur les moniteurs de poids non nul) : B 63 et 7 ; C1, C2 63 et 7 ; C3, D 63 et 63 ; B′ 511 et ≤ 63 ; C3′ 511 et 511.
- **(ii) familles tenues à l'écart** : 50 lois par tâche tirées de **RACINE_TENUE**, deux sous-familles ; 3 999 échantillons par loi ; score = moyenne des 50 taux.
- **(i) familles vues** : descriptif.
- **Courbe V(δ')** et **coût par contournement** (piste 5) : comme au brouillon 2 (seuil relatif κ = S14, garde de ligne de base κ × base ≥ 2α, censure, bissection en 3 pas) ; descriptifs.
- **Nouveauté résiduelle** (piste 4) : comme au brouillon 2.
- **Condition d'application** (A : verdict ; B, D, B′ : descriptif) : matrice H, ligne s = moniteur déployé au tour s (0 … T ; pour D, chaque moniteur de la trajectoire), colonne t = attaque du tour t (1 … T), taux sur les échantillons d'évaluation fixés de l'attaque ; **I1** (progrès) = moyenne de (iii) aux tours 5–8 moins aux tours 1–4 ; **I2** (oubli) = moyenne sur t = 1 … 7 de H[t, t] − H[8, t] ; rétention par décalage k = −1 … 3 ; **I3** (retours) = part des tours t ≥ 3 où le cosinus du déplacement de l'attaque avec celui d'une attaque d'un tour ≤ t − 2 dépasse celui avec l'attaque du tour t − 1. Intervalles par rééchantillonnage des instances.
- **Contrôles** : fausses alertes de chaque défense finale sur 20 000 échantillons propres indépendants ; valeur du jeu restreint de B et B′ ; V standard − V renforcé ; contrastes sous chaque attaquant seul ; poids finaux de B, B′, C2 (support, pureté, poids maximal) ; statuts SLSQP, départs non finis, réponses à la limite ; entraînements non convergés.
- **Attaquant indépendant (S17)** : SLSQP lourd (12 départs structurés — chaque composante, puis toutes, tirées vers l'origine de tout le budget, écarts-types 0,5 / 1 / 1,5 —, 100 départs tirés, attaques passées et finales, 1 024 échantillons, 300 itérations), puis stratégie d'évolution (1 + 12) sans gradient sur le taux dur, 400 générations, depuis la réponse lourde et depuis l'attaque finale standard ; V_audit = min(V, V_lourd, V_évolution × 2), chaque réponse évaluée sur 19 998 échantillons frais.
- **Intervalles** : rééchantillonnage apparié des instances, 20 000 tirages, quantiles linéaires 0,3125 %, 0,625 %, 1,25 %, 2,5 %, 5 % et symétriques ; graines `SeedSequence(entropy=racine, spawn_key=(code_delta, code, 0, 0, 99))` (codes 1–19 contrastes, 101–109 indicateurs).

## Seuil

**Tous les seuils sont à geler par Lazar en une ligne datée de `registres/decisions.md`. Aucun défaut ne s'applique.** Pour chacun : valeur (marqueur), recommandation, raison, source. S4, S7, S8 (interne), S9, S11, S12, S13, S14, S16, S17 (paramètres de l'attaquant et critère) et S18 sont des champs de la configuration : une valeur différente de celle du bloc de configuration change le code et l'identité (à régénérer). S1, S2, S3, S5, S6, S10, S15 sont des seuils de lecture appliqués par le lecteur R13.

**S1 — effet minimal du contrôle de plomberie, Δ(B, A) sur (iii)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02** (deux fois α).
- Raison : principe, non pilote (un gain de détection plus petit que deux fois le taux de fausses alertes est négligeable à ce point de fonctionnement). Règle « moyenne ≥ S1 et borne basse B2 > 0 », par δ, N = 100, rééchantillonnage réel : taille 0,000 sous effet nul ; 0,503 et 0,516 sous effet = S1 (règle de pertinence et de significativité, pas un test de « effet ≥ S1 ») ; puissance 0,977 et 1,000 à un effet de 0,03 [M3 § 3a].

**S2 — erreur de première espèce et corrections**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **5 % bilatéral par famille**, trois familles : Tables 1, 2 et 5 (Bonferroni sur 2 δ, B2) ; Q1, Table 3 (Bonferroni sur 8 tests, B8 ; équivalence au niveau 0,05/8 par côté, E8) ; Q2, Table 6 (Bonferroni sur 4 tests, B4 = [q0,00625 ; q0,99375] ; équivalence 0,05/4, E4 = [q0,0125 ; q0,9875]). Pas de correction entre Q1 et Q2 (deux questions distinctes) ; option : Bonferroni sur 12 tests.
- Raison : tailles **mesurées avec la règle réelle** (rééchantillonnage de 20 000 tirages, quantiles linéaires, 1 000 répétitions par scénario, N = 100 instances tirées du pilote v3, centrées puis décalées à la frontière) [M3 § 3b, § 3c, § 3e] : Q1, P(« B > X » | Δ = +m) 0,001 à 0,008 (nominal 0,003) ; P(« X > B » | Δ = −m) 0,003 à 0,013 ; P(« ≈ » | Δ = ±m) 0,004 à 0,017 (nominal 0,006) ; Q2, 0,005 à 0,008 ; 0,008 à 0,015 ; 0,005 à 0,026 (nominaux 0,006 et 0,013) ; Table 5, 0,002 à 0,009 (nominal 0,006). Erreur de simulation ≈ ±0,003 à 0,01. **Dépassement du nominal jusqu'à un facteur 2 à 4 dans quelques cellules** (percentiles d'un rééchantillonnage, un peu trop étroits sur des écarts asymétriques) : déclaré ; aucune lecture prédite n'est à la frontière (écarts de 0,08 à 0,22 pour C3 et D ; Q2 « ≈ » à 0,001–0,009 de zéro).

**S3 — puissance visée**
- Valeur : À REMPLIR par Lazar.
- Recommandation : plomberie ≥ **0,9** à un effet de 0,03 par δ ; Tables 3 et 6 : probabilité de la classe prédite ≥ **0,8** pour les prédictions fermes.
- Raison : plomberie 0,977 et 1,000 ; P4, P5, P8 : 1,000 ; P10 : 0,998 ; P11 : 1,000 [M3 § 3, § 4]. Limite : sous un écart nul sur (ii), « sans régression » sort avec 0,827 à S5 = 0,02 [M3 § 3d].

**S4 — nombre d'instances N par valeur de δ**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **N = 100** (200 tâches ; valeur du bloc de configuration).
- Raison : S3 tenue ; 190 min de processeur, **120 min de mur sur 2 cœurs** projetés [M3 § 5]. Option : **N = 60** (114 min de processeur, 72 min de mur ; classes inchangées sauf C2 « B > C2 » 0,92 et Q2 « non exercée » 0,971 [M3 § 3b, § 4]) ; elle change le champ `n_instances` (identité à régénérer).

**S5 — tolérance de non-régression sur (ii), Δ(B, A)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02 (= S1)**, par principe (symétrie avec S1). **Lecture sans seuil** recopiée dans tous les cas. Sous le pilote : « régression avérée » 1,000 [M3 § 3d].

**S6 — marge des contrastes de Q1 (Table 3) et de Q2 (Table 6)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **m = 0,02 (= S1) pour les quatre témoins de Q1 et les deux de Q2, aux deux δ**.
- Raison, sans pilote (CM2-04) : le même principe que S1 (un écart de détection inférieur à deux fois α est négligeable) ; fixé dans le gel v3 avant le pilote v3 ; il ne dépend plus de B − A (dont la valeur à δ 1,8 mesure surtout l'effondrement de A, CM2-06). Sens : **un témoin équivaut à B si leur écart est démontré dans ]−0,02 ; +0,02[** (équivalence bilatérale, deux tests unilatéraux) ; « B > X » exige une borne basse au-dessus de 0,02. La lecture sans seuil (estimation, intervalle B8 ou B4) de chaque contraste est recopiée dans la phrase de synthèse quelle que soit la classe.

**S7 — λ des « ou » déterministes C3 et C3′**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **8** (fixé au gel v2, avant les pilotes v2 ; le même pour C3′). log(9)/8 ≈ 0,27 écart-type au plus entre le score et λ fois le maximum des scores standardisés.

**S8 — plafond de temps**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **`timeout 9000` (2 h 30 de mur)** externe pour N = 100 (option N = 60 : `timeout 5400`), et **600 s de processeur par tâche** (garde interne `plafond_cpu_tache_s`) ; audit d'attaquant indépendant : `timeout 5400`.
- Raison : par tâche (8 bras) : moyenne 57,0 s, médiane 55,1 s, maximum 79,8 s ; efficacité mesurée 0,80 sur une machine partagée (charge moyenne ≈ 4 sur 2 cœurs pendant la session) [M3 § 5]. Audit : 229 s de processeur par tâche ; 10 tâches ≈ 19 min de processeur sur 2 cœurs, mais 614 s de mur mesurés pour 2 tâches en parallèle sur la machine chargée [M3 § 8] : projection de 19 à 51 min.

**S9 — taux de fausses alertes α et tolérances**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **α = 0,01** ; garde |taux mesuré − α| ≤ 0,005 par défense finale ; déclencheur |moyenne d'un bras − α| > 0,001 dans un δ.
- Raison : pilote v3, écart des moyennes à α ≤ 0,0006 ; écart entre bras par tâche moyen 0,0014 à 0,0017, maximum 0,0030 [M3 § 6]. Déclaré (CM2-12) : la garde tolère 50 % de α par défense ; pas de garde propre à l'écart entre bras d'une tâche (rapporté).

**S10 — déclencheur « trop beau / trop mauvais »**
- Valeur : À REMPLIR par Lazar.
- Recommandation : audit si la moyenne de V d'un bras dans un δ sort de la **bande moyenne pilote ± 5 × écart-type par tâche du pilote / √N** (règle écrite dans le gel v3 avant le pilote ; CM2-08). À N = 100 [M3 § 7] : δ 1,4 : A [0,0770 ; 0,1662] ; B [0,2034 ; 0,2469] ; C1 [0,1805 ; 0,2283] ; C2 [0,1676 ; 0,2220] ; C3 [0,3832 ; 0,4142] ; D [0,4384 ; 0,4583] ; B′ [0,4404 ; 0,4581] ; C3′ [0,4302 ; 0,4515] ; δ 1,8 : A [0,0084 ; 0,0456] ; B [0,1309 ; 0,1584] ; C1 [0,1137 ; 0,1424] ; C2 [0,0923 ; 0,1263] ; C3 [0,2048 ; 0,2403] ; D [0,2373 ; 0,2604] ; B′ [0,2472 ; 0,2687] ; C3′ [0,2163 ; 0,2427] ; plus la règle de Lazar : moyenne de V(B) ≥ 0,99. Si N change, la bande se recalcule par la même formule.

**S11 — budgets de comportement δ**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **δ = (1,4 ; 1,8)**, inchangés (règle `choisir_deltas` du v2, racine de calibrage 20261295, 12 instances).
- Raison et réserve (CM2-06) : au calibrage, V(A) = 0,034 à 1,8, choisi par franchissement d'un seuil bruité (1,6 : 0,035) ; aux pilotes, **A est près du plancher à δ 1,8** : 0,0154 (1,5 α, v2) et 0,0270 (2,7 α, v3) ; le critère « A pas au plancher » n'est donc pas tenu sur échantillon indépendant au pilote v2. **La Table 1 à δ 1,8 mesure B contre un A presque nul et ne démontre pas un « gain d'équilibre » à ce budget.** Aucune marge n'en hérite plus (S6 par principe). Ne pas changer δ sauf décision de Lazar ; option écrite : recalibrer avant scellement sur au moins 48 instances de la racine réservée 20261315 / 20261316 (`arene_melange_v3.py calibrage --instances 0:48`, environ 10 min), puis régénérer l'identité.

**S12 — nombre de tours T** : À REMPLIR par Lazar. Recommandation **T = 8** (nouveauté résiduelle de 1 au tour 1 à 0,135–0,187 au tour 8 [M3 § 6]).

**S13 — oracle du défenseur (identique pour tous les bras)** : À REMPLIR par Lazar. Recommandation **« détection »** (principe, § Hypothèse). Option « logistique » : au pilote v2, B − A = +0,003 et +0,0015, D > B : la Table 1 rendrait « mécanisme non démontré » et Q1 resterait réfutée (D > B aux deux oracles).

**S14 — seuil de contournement relatif κ** : À REMPLIR par Lazar. Recommandation **κ = 0,5**, garde κ × base ≥ 2α (mesure descriptive).

**S15 — marge de la condition d'application (Table 5)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,02 (= S1)**, par principe (gel v3).
- Raison : sous le pilote, « A ne progresse pas, avec oubli » 1,000 aux deux δ ; tailles 0,002 à 0,009 [M3 § 3e].

**S16 — unités de chaque moniteur de B′**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **9** (= T + 1, la classe du moniteur final de D ; gel v3).
- Raison : égalité de classe et de paramètres déployés par requête avec D. Option : un maxout unique de 73 unités (même total que B′) comme témoin supplémentaire — non implanté, coût élevé (lacune déclarée).

**S17 — audit d'attaquant indépendant (déclencheur 9)**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **10 tâches de la décision** (instances 0 à 4, aux deux δ), bras B, C3, D, B′, C3′ ; attaquant : 100 départs tirés + 12 structurés, 1 024 échantillons, 300 itérations, évolution (1 + 12) × 400 générations ; **critère d'artefact : dans un δ, la moyenne sur les tâches auditées de B − C3, B − D, B′ − D ou B′ − C3′ change de signe ou de plus de 0,05**.
- Raison : 0,05 est au-dessus du bruit apparié sur 5 tâches (même défense, deux attaquants : écarts de 0,000 à 0,005 au pilote [M3 § 8]) et sous les écarts qui portent Q1 (0,08 à 0,22). Réserve : pour Q2, les écarts sont de 0,001 à 0,03 ; un changement de signe y suffit à déclarer l'artefact, ce qui est voulu (R4, symétrie). Audit d'essai sur 2 tâches du pilote : changements de 0,000 à 0,005, aucun artefact.

**S18 — garde de convergence des entraînements**
- Valeur : À REMPLIR par Lazar.
- Recommandation : **0,10** par tâche (au plus 3 non-convergences sur 34 entraînements) ; le bloc de configuration porte encore **0,05**, valeur du brouillon 2 (changer le champ `taux_nonconv_max` régénère l'identité).
- Raison : au pilote v3, 2 non-convergences sur 1 632 (une dans deux tâches ; 0 sur 1 248 au pilote v2 : les maxouts de B′ sont nouveaux). À 0,05, 2 non-convergences dans une tâche arrêtent la décision ; probabilité estimée sur 200 tâches ≈ 0,16 (taux 0,0012 par entraînement, binomiale) ; à 0,10, ≈ 2 × 10⁻⁵. Une non-convergence est un entraînement arrêté à la limite d'itérations, dont le moniteur est employé ; la garde vise une dérive massive, pas un cas isolé.

## Plan d'analyse

### 1. Monde
Loi propre N(0, I_6). Loi cible d'une instance : 3 composantes, moyennes de norme 4 dans des directions tirées, écarts-types 1. Loi d'attaque : 3 composantes appariées, moyennes et écarts-types diagonaux dans la boîte (|μ| ≤ 5, σ ∈ [0,5 ; 1,5]). Contrainte de comportement : racine de la moyenne sur k du carré de la distance de Wasserstein d'ordre 2 entre composantes appariées ≤ δ.

### 2. Bras
Tour 0 commun : moniteur linéaire M0 entraîné contre la loi cible (reproductibilité bit à bit vérifiée par garde). Puis, pour t = 1 … T, dans chaque bras à trajectoire : l'attaquant calcule une meilleure réponse contre la défense déployée ; le défenseur se met à jour.
- **A, défense unique réentraînée, même oracle** : déploie le dernier moniteur linéaire, entraîné contre le mélange uniforme de toutes les attaques passées.
- **B, mélange d'équilibre linéaire** : double oracle tronqué ; p = stratégie d'équilibre du défenseur sur la matrice G ; q = stratégie d'équilibre de l'attaquant ; nouveau moniteur **linéaire** entraîné contre q. Défense finale : p sur la matrice 9 × 9.
- **B′, mélange d'équilibre à classe de D** : identique à B, mais l'oracle rend à chaque tour un **maxout à S16 = 9 unités** (graine d'initialisation du rôle 8, code de bras 8).
- **D, unique** : un seul maxout à t + 1 unités au tour t (9 à la fin), entraîné contre le mélange uniforme de ses attaques passées. Oracle à plusieurs unités approché (seuil gaussien, deux départs), le même pour les maxouts de B′.
- **C1, C2, C3** sur les 9 moniteurs mêmes de B après le tour T (poids uniformes ; Dirichlet (1, …, 1), graine `(code_delta, instance, 6, T + 1, 13)` ; « ou » déterministe standardisé, λ = S7, seuil recalibré à α).
- **C3′** sur les 9 moniteurs mêmes de B′ : z_i = (s_i − μ_i)/σ_i sur le propre de calibration, score log-somme-exp_i(λ z_i), seuil recalibré à α (`MoniteurOu` ; identique à C3 sur des moniteurs linéaires, essai).
Pour chaque bras, la défense finale est figée ; l'attaquant joue en dernier avec les attaques passées de sa trajectoire comme départs supplémentaires (celles de B pour C1, C2, C3 ; de B′ pour C3′).

### 3. Graines (R9)
- **RACINE = 20261201**, **RACINE_TENUE = 20261202** (décision, jamais employées). Racines d'essai v3, fixées avant leur première exécution et sans lien avec un résultat : 20261311 / 20261312 (pilote v3 et audit d'essai) ; 20261313 / 20261314 (essais du code, mesures de temps) ; 20261315 / 20261316 (réservées à l'option de recalibrage, non employées). **Refusées par garde** en v3 : 20261291 à 20261298 (brouillon 1 et v2) et 20269501 / 20269502 (diagnostics de la contre-lecture 2).
- Chaque tirage : `numpy.random.SeedSequence(entropy=racine, spawn_key=(code_delta, instance, code_bras, tour, rôle, …))`, numpy ≥ 1.25. Codes de bras : commun 0, A 1, B 2, D 4, C1 5, C2 6, C3 7, B′ 8, C3′ 9. Rôles : 0 à 14 comme au brouillon 2 ; 15 attaquant indépendant ; rééchantillonnage `(code_delta, code, 0, 0, 99)`. Le schéma est dans la configuration (`schema_graines`) ; le champ « graines » de `creer_manifeste` n'est pas employé (déclaré).
- Chaque bras tire ses graines de son propre code : l'ordre et la présence des autres bras ne changent aucun résultat (essai `test_ordre_des_bras_sans_effet`, y compris avec et sans B′).
- Garde de la racine de décision dans `gen`, re-vérifiée dans chaque processus de travail (y compris ceux de l'audit).

### 4. Comparaisons et multiplicité
- **Table 1** : Δ(B, A) sur (iii), B2. **Table 2** : Δ(B, A) sur (ii), B2. **Table 5** : I1 et I2 de A, B2.
- **Q1 (Tables 3 et 4)** : Δ(B, C1), Δ(B, C2), Δ(B, C3), Δ(B, D), 8 tests, B8 et E8.
- **Q2 (Tables 6 et 7)** : Δ(B′, D), Δ(B′, C3′), 4 tests, B4 et E4.
- « Confirmée » = intersection-union ; « réfutée » = union protégée par la correction.
- **Descriptives** : Δ(B′, B), Δ(C3′, C3), Δ(C3′, D), (ii) de B − C3, B − D, B′ − D, B′ − C3′ ; I1, I2, I3 de B, D, B′ ; matrices H moyennes ; coût, courbes, nouveauté ; poids ; contrôles.

### 5. Ordre d'exécution, arrêt et reprise
(1) Essais du code ; (2) une seule invocation `arene_melange_v3.py decision --prereg prereg/<nom>.md --instances 0:N --run-id <AAAAMMJJ-HHMMSS-arene-melange-v3>` sous `timeout` (S8), arbre git propre ; les PID et instants de départ des processus de travail sont écrits et scellés dans `runs/<run-id>/pids-travail.txt` ; (3) analyse écrite par le même processus (`analyse-arene.json`, scellé) ; (4) si le déclencheur 9 (ou un autre déclencheur imposant l'audit) est présent, `arene_melange_v3.py audit --prereg … --source-run <run-id> --instances 0:5 --run-id <run-id>-audit` (les tâches de la décision sont reconstruites et vérifiées **au bit près** contre le run audité avant l'attaquant indépendant) ; (5) lecture par un sous-agent neuf (R13), qui applique les tables ; `lire_tables` est une aide mécanique, le texte scellé fait foi.

**Reprise après arrêt (CM-12, CM2-14)** : (a) arrêt de cause **externe** (signal, `timeout`, machine), aucun résultat écrit : le signal TERM est converti en arrêt du pool, qui termine ses processus de travail ; puis arrêt par PID de tout survivant consigné et garde « aucun orphelin ». **Aucune reprise tant que `arene_melange_v3.py orphelins --pids runs/<run-id>/pids-travail.txt` ne rend pas « aucun processus de travail consigné ne tourne »** (avec `--arreter` : arrêt par PID, jamais par motif de ligne de commande, R10 ; l'instant de départ consigné protège contre un PID réemployé). Puis **une** reprise complète, même code, mêmes racines, nouvel identifiant de run ; seconde interruption externe → non concluant ; (b) arrêt par une garde interne : pas de reprise → non concluant, version nouvelle du préenregistrement ; (c) aucun point de reprise partiel (déclaré). Réserve : le processus `resource_tracker` de multiprocessing n'est pas consigné ; il se termine avec le processus principal.

### 6. Historique de conception (déclaré ; aucune décision n'a lu une racine de décision)
1. Oracle du défenseur, seuil de contournement, δ, bras C1–C3 : comme au brouillon 2 (§ Plan 6 du brouillon 2, archive `archive-observation-oracle-v1.json`).
2. **Bifurcation v3** (après le pilote v2 et la contre-lecture 2) : Q1 renommée « à nombre de paramètres égal » ; Q2, B′ et C3′ ajoutés ; mesures de la condition d'application ; marges par principe ; S10 par erreur-type ; déclencheur 9 et attaquant indépendant ; arrêt par PID. Conception et prédictions fixées dans `gel-conception-arene-melange-v3.md` (10:24 UTC) avant toute exécution de B′.
3. **Après le gel v3, avant le pilote v3** (journal) : deux corrections de plomberie révélées par les essais (garde de variance de `MoniteurOu` à 10⁻¹² au lieu de 0, un score constant laissant un écart-type d'arrondi ; rétention par décalage limitée aux décalages définis quand T < 4) et une accélération du calcul de C3′ et des maxouts (score et gradient en un seul produit matriciel, log-somme-exp groupée), sans changement de fonction (essais `test_bras_v2_inchanges`, `test_ou_composite_sain_et_artefacts`, `test_gradients`). Code du pilote = code remis (`88c87818…`).
4. **Après le pilote v3** : aucun changement de conception ni de code. Seuls les chiffres des prédictions pour la décision, les bandes S10 et les recommandations de S4, S8 et S18 viennent du pilote.

## Critères de lecture gelés

Un sous-agent neuf (R13) applique ces tables telles qu'écrites. Chaque table se lit **de haut en bas ; la première ligne vraie décide** ; la dernière est le complémentaire. Notations, pour un contraste ou un indicateur à δ fixé : est = moyenne ; qX = quantile X du rééchantillonnage ; **B2 = B4** = [q0,00625 ; q0,99375] ; **B8** = [q0,003125 ; q0,996875] ; **E8** = [q0,00625 ; q0,99375] ; **E4** = [q0,0125 ; q0,9875].

**V0** = aucune condition de la liste d'arrêt ∧ tâches exécutées = 2 × N ∧ racines du manifeste = RACINE et RACINE_TENUE ∧ empreintes du code, de la configuration et de la bibliothèque = celles du texte scellé ∧ une seule invocation ayant écrit des résultats (au plus une reprise complète après arrêt externe consigné et commande `orphelins` saine).

**Déclencheurs d'audit (R4), symétriques** — un seul suffit ; l'effet bloquant de chacun est écrit :
1. **Contradiction de la branche prédite, dans les deux sens** (§ Prédiction B) : (a) classe du signe opposé au signe prédit ; (b) classe prédite « ≈ » (P8, P9 à δ 1,4) et observée « B > X » ou « X > B » ; (c) plomberie observée en ligne 5 ou 6 ; (d) (ii) borne basse B2 > 0 dans un δ ; (e) Table 4 « Q1 confirmée » ou « dépend de δ » ; (f) Table 7 autre que « Q2 non exercée » ; (g) Table 5 autre que « A ne progresse pas, avec oubli » à un δ. *Bloque* : la table contredite et la phrase de synthèse ; (c) bloque la Table 1.
2. **Trop beau / trop mauvais** (S10) : moyenne de V d'un bras dans un δ hors de sa bande ; ou moyenne de V(B) ≥ 0,99. *Bloque* : toutes les tables.
3. **Règle de Lazar** (« si le mélange uniforme égale le mélange d'équilibre, audit ») : Δ(B, C1) « ≈ » dans un δ ; ou V(B) = V(C1) au bit près sur une tâche ; ou poids finaux de B uniformes (10⁻⁶) sur une tâche. *Bloque* : la classe de C1 dans la Table 3 seulement ; **ne bloque pas la Table 1** (CM2-04, CM2-10).
4. **Mélange B dégénéré** : poids de B purs sur plus de la moitié des tâches d'un δ. *Bloque* : Tables 1, 3, 4. (Pour B′, la pureté n'est pas un déclencheur : elle rend Q2 « non exercée » par la Table 7, comme prédit.)
5. **Optimiseur** : moyenne de (V standard − V renforcé) > 0,01 pour un bras dans un δ ; ou un contraste des Tables 1, 3, 6 qui diffère de plus de 0,01 entre attaquant standard seul et renforcé seul. *Bloque* : toutes les tables.
6. **Jeu restreint** : moyenne de (valeur du jeu restreint − V) < −0,01 pour B ou B′ dans un δ. *Bloque* : Tables 1, 3, 4 (B) ou 6, 7 (B′).
7. **Capacité non exercée** : V(D) = V(A) au bit près sur toutes les tâches d'un δ. *Bloque* : Tables 3, 4, 6, 7.
8. **Dérive des fausses alertes** : |moyenne des fausses alertes finales d'un bras − α| > 0,001 dans un δ. *Bloque* : toutes les tables.
9. **Conforme et trop propre (CM2-05)** : Table 4 « Q1 réfutée » portée par C3 ou D conformément à P4, P5 (probabilité simulée 1,000), ou Table 6 conforme à P8. *Effet* : audit d'attaquant indépendant (S17) sur les 10 tâches de la décision, **après** scellement de l'analyse et **avant** la phrase de synthèse ; *bloque* la phrase de synthèse des Tables 4 et 7, **pas** les Tables 1, 2 et 5.

**Contenu de l'audit** (tout déclencheur) : relecture du code par un sous-agent neuf ; audit d'attaquant indépendant sur les **tâches de la décision** (S17 ; jamais sur la racine d'essai, CM2-09) ; vérification que B et B′ déploient les poids du programme linéaire, C1 l'uniforme, C2 les poids de Dirichlet de sa graine, C3 et C3′ le « ou » des moniteurs de leur source. **Issue** : « artefact trouvé » si et seulement si le rapport scellé constate une erreur de code, un chemin non exercé (hors la pureté de B′, lue par la Table 7), ou le critère de S17 ; sinon « pas d'artefact ».

### Table 1 — contrôle de plomberie, Δ(B, A) sur (iii)

| # | Condition | Verdict |
|---|---|---|
| 0 | V0 fausse | **non concluant** ; aucune lecture |
| 1 | un déclencheur qui bloque la Table 1 (1c, 2, 4, 5, 6 pour B, 8) est présent et l'audit n'est pas rendu | **non concluant (audit en attente)** |
| 2 | audit rendu, artefact trouvé | **non concluant** ; version nouvelle du préenregistrement |
| 3 | dans un δ, la moyenne de V est ≤ 2α pour les huit bras | **non concluant** : jeu dégénéré |
| 4 | est ≥ S1 ∧ borne basse B2 > 0, aux deux δ | **mécanisme exercé** (B bat la défense unique ; à δ 1,8, contre un A presque nul) |
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
| 2 | borne haute de I1 < S15 ∧ borne basse de I2 > S15 | **A ne progresse pas, avec oubli** |
| 3 | borne haute de I1 < S15 ∧ borne haute de I2 < S15 | **A ne progresse pas, sans oubli** |
| 4 | borne haute de I1 < S15 | **A ne progresse pas, oubli indéterminé** |
| 5 | sinon | **indéterminé** |

Verdict : « **condition d'application vérifiée** » si A ne progresse pas (lignes 2 à 4) aux deux δ ; « **non vérifiée** » si A progresse à au moins un δ ; « **indéterminée** » sinon. I3 et les matrices H sont recopiés sans verdict.

### Table 6 — Q2 : classement de X ∈ {D, C3′} à chaque δ, Δ(B′, X) sur (iii)

Mêmes classes que la Table 3, avec **B4** à la place de B8 et **E4** à la place de E8, marge m = S6.

### Table 7 — Q2 (« à classe de fonctions égale, B′ bat D et C3′ »)

Statut par δ : « **non exercée (mélange B′ dégénéré)** » si les poids finaux de B′ sont purs (un poids ≥ 1 − 10⁻⁹) sur plus de la moitié des tâches de ce δ ; sinon comme la Table 4 sur les deux témoins.

| # | Condition | Verdict |
|---|---|---|
| 1 | « non exercée » à au moins un δ | **Q2 non exercée (au moins un δ)** ; statuts par δ et classes de la Table 6 recopiés |
| 2 | « tenue » aux deux δ | **Q2 confirmée** |
| 3 | « réfutée » aux deux δ | **Q2 réfutée** |
| 4 | « tenue » à un δ, « réfutée » à l'autre | **Q2 dépend de δ** |
| 5 | sinon | **Q2 non tranchée** |

**Phrase de synthèse** (écrite par le lecteur R13 en recopiant, sans rien omettre) : « Table 1 : … ; Table 2 : … (sans seuil : Δ(B, A) sur (ii) = est [B2] à chaque δ) ; Table 5 : … (par δ ; I1, I2 et I3 de A avec intervalles) ; Table 3 : C1 …, C2 …, C3 …, D … (par δ, avec est [B8]) ; Table 4 : … ; Table 6 : D …, C3′ … (par δ, avec est [B4]) ; part pure de B′ par δ ; Table 7 : … ; déclencheurs : … ; issue des audits : … ; portée : résultat local au monde, à l'oracle, aux δ et à T ». Les classes des Tables 3 et 6 sont toujours recopiées ; aucune lecture des Tables 4 et 7 ne masque un témoin.

## Liste d'arrêt

Chaque garde du code (62 sites `raise GardeArret`, chacun avec un motif unique) a un essai nommé qui la provoque par son motif (`pytest.raises(…, match=motif)`) et un cas sain ; `test_chaque_garde_a_son_essai` contrôle par l'arbre syntaxique que chaque site a une entrée et un essai nommé existant (il ne prouve pas à lui seul que l'essai provoque le motif, CM2-12). Fichier d'essais : `essais/test_arene_melange_v3.py`.

| Condition | Action | Garde et essai (R5 : cas sain et artefact, motif vérifié) |
|---|---|---|
| Lancement en décision ou en audit sans préenregistrement scellé, conforme, identifié | pas de départ ; aucune graine de décision | `autoriser_decision`, `exiger_prereg_arene`, `exiger_identite_prereg` ; `test_prereg_scelle_refus_pour_la_bonne_raison`, `test_identite_prereg_sain_et_artefacts`, `test_decision_refusee_copie_brouillon3_pour_la_bonne_raison` (copie temporaire : sans compagnon → « absente » ; scellée → « scellé mais non conforme : Seuil ; Contre-lecture », CM2-01) |
| Audit d'un run lancé sous un autre préenregistrement | arrêt | `exiger_meme_prereg` ; `test_exiger_meme_prereg` |
| Graine tirée d'une racine de décision sans autorisation ; processus de travail sans préenregistrement | arrêt | `gen`, `_travail` ; `test_gen_garde_racine_de_decision`, `test_travail_refuse_racine_de_decision_sans_prereg` |
| Hors décision : racine de décision, racine d'essai déjà employée, racine des tenues égale à la principale | arrêt | `exiger_racines_essai` ; `test_racines_essai_sain`, `test_racines_essai_artefact`, `test_cli_essai_refuse_racines_interdites` |
| Configuration incohérente (δ, effectifs, κ, fractions, oracle, B′ sans maxout, paramètres de l'attaquant indépendant) | arrêt | `exiger_config` ; `test_config_sain_et_artefacts` |
| Fichier de sortie, fichier de PID ou dossier de run existant | arrêt (R12) | `_exiger_absent`, `_ecrire_nouveau`, `creer_manifeste` ; `test_cli_refuse_d_ecraser`, `test_lancer_consigne_pids_sans_orphelin` |
| Arbre git non propre au lancement de décision ou d'audit | arrêt | `creer_manifeste` (essais du dépôt) |
| Programme linéaire non résolu ; primal ≠ dual ; matrice invalide | arrêt | `resoudre_jeu` ; `test_jeu_sain`, `test_jeu_solveur_artefacts`, `test_jeu_artefact` |
| Poids de mélange invalides | arrêt | `exiger_poids` ; `test_poids_sain_et_artefact` |
| Loi d'attaque non finie, hors boîte, ou à distance > δ | arrêt | `exiger_admissible` ; `test_admissibilite_sain_et_artefact` |
| Échantillons non multiples de K | arrêt | `echantillonner` ; `test_echantillonnage_stratifie` |
| Moniteur non fini, non calibrable, non calibré | arrêt | `Moniteur` ; `test_moniteur_gardes` |
| « Ou » déterministe sur un moniteur non linéaire ou de variance nulle ; « ou » composite vide ou de variance nulle | arrêt | `ou_deterministe`, `MoniteurOu` ; `test_ou_deterministe_sain_et_artefacts`, `test_ou_composite_sain_et_artefacts` |
| Maxout sans graine ; entraînement non fini ; oracle inconnu | arrêt | `entrainer` ; `test_entrainement_gardes` |
| Aucun départ fini ; part de départs non finis > 5 % (tâche, ou attaquant indépendant) | arrêt | `meilleure_reponse`, `exiger_departs_finis` ; `test_meilleure_reponse_departs_non_finis`, `test_garde_departs_finis` |
| Fausses alertes d'une défense finale hors de α ± 0,005 | arrêt | `exiger_fpr` ; `test_garde_fausses_alertes_sain_et_artefact` |
| Part d'entraînements non convergés > S18 dans une tâche | arrêt | `exiger_convergence` ; `test_garde_convergence_et_identite_tour0` |
| Moniteur du tour 0 non reproductible bit à bit | arrêt | `exiger_meme_moniteur` ; idem |
| Temps processeur d'une tâche > 600 s | arrêt | `exiger_plafond` ; `test_plafond_de_temps_processeur` |
| Bras ou témoin inconnu | arrêt | `trajectoire`, `defense_temoin`, `construire_defenses` ; `test_bras_inconnus` |
| Calibrage (option) sans δ satisfaisant la règle | arrêt | `choisir_deltas` ; `test_choisir_deltas` |
| Audit : bras absent, tâche absente, ou V reconstruit ≠ V du run audité au bit près ; pilote audité étranger | arrêt | `auditer_tache`, `auditer`, `charger_pilote` ; `test_audit_sain_et_artefacts`, `test_audit_essai_refuse_pilote_etranger` |
| Processus de travail consigné encore vivant à la fin d'un lancement ou avant une reprise | arrêt (R10) ; pas de reprise | `exiger_aucun_orphelin`, `arreter_par_pid`, commande `orphelins` ; `test_arret_par_pid_sain_et_artefact`, `test_lancer_consigne_pids_sans_orphelin`, `test_signal_term_arrete_le_pool_par_pid` |
| Signal TERM (dont `timeout`) | arrêt consigné, pool terminé, survivants arrêtés par PID | `lever_sur_term` (bibliothèque) dans `_lancer` ; `test_signal_term_arrete_le_pool_par_pid` |
| Ligne de base du coût trop basse | mesure « non définie », comptée | `cout_contournement` ; `test_cout_contournement_ligne_de_base_et_bissection` |
| Reproductibilité ; bras v2 modifiés | constat d'essai | `test_reproductibilite_bit_a_bit_et_temoins`, `test_ordre_des_bras_sans_effet`, `test_bras_v2_inchanges` |
| Tâches ≠ 2 × N ; invocations hors § Plan 5 ; paramètre changé après lecture | V0 fausse | contrôle du lecteur R13 |
| Appel de modèle, réseau, dépense | arrêt (devis et GO exigés) | — |
| Lecture d'un résultat de décision avant scellement | arrêt et consignation (R1) | — |
| numpy < 1.25 | arrêt (R9) | `exiger_numpy_minimal` (essais du dépôt) |
| Marqueur de gel restant, ou contre-lecture sans ses deux empreintes | pas de scellement | validateur `problemes` ; `test_brouillon3_non_conforme_au_validateur_et_identite_du_code` |
| Ligne de gel absente de `registres/decisions.md`, valeurs différentes du texte ; remarques de contre-lecture non traitées | pas de scellement ; contrôle manuel pour S1, S2, S3, S5, S6, S10, S15 ; les champs de configuration sont comparés par le code | `exiger_identite_prereg` |

## Rôles

- Auteur du brouillon 3 et du code v3 : sous-agent neuf Opus 5.5 (lignée conv-audit), qui n'a écrit ni les brouillons 1 et 2, ni les codes v1 et v2.
- Contre-lecteur du brouillon 3 (R2) : un sous-agent neuf **d'un modèle autre qu'Opus**, qui n'a écrit ni ce texte ni le code ; fichiers à lui donner explicitement : ce brouillon, `arene_melange_v3.py`, `essais/test_arene_melange_v3.py`, `gel-conception-arene-melange-v3.md`, `calcul-puissance-arene-melange-v3.py` et sa sortie, `essai-pilote-arene-melange-v3-detection.json`, `audit-essai-arene-melange-v3.json`, `journal-pilotes-arene-melange-v3.txt`, `LISEZMOI-arene-melange-v3.md`, la contre-lecture 2 et le brouillon 2. Points à juger en priorité : la bifurcation v3 et l'ordre « gel puis exécution » ; la définition de « classe de fonctions égale » (B′ contre D) et la lacune du maxout de 73 unités ; la ligne « non exercée » de la Table 7 et sa probabilité prédite ; les indicateurs I1, I2 de la Table 5 ; les tailles mesurées (S2) ; le déclencheur 9 et le critère de S17 ; S18.
- Lecteur de porte (R13) : sous-agent neuf, ni auteur ni contre-lecteur ni analyste ; applique les Tables 1 à 7 ; verdict scellé puis soumis à Lazar.
- Lazar : gèle S1 à S18 (et décide de l'option de recalibrage des δ) ; donne le GO de l'exécution de décision (processeur, aucune dépense).

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf Sonnet 5.5 ; brouillon relu : `preenregistrement-arene-melange-equilibre-v1-brouillon1.md` `5129b8c26d384e92015142e6d80c1d29f922210975fc297ec487efab070284ce` ; rapport : `contre-lecture-arene-melange-v1-brouillon1.md` `3721865417495678475ab995d43a3e56dd1b3b1df7b147a218f6ce9b0bc5bd1f`. Verdict : « présentable après corrections ». Traitement de CM-01 à CM-18 : au brouillon 2 (§ Contre-lecture, tableau), reconduit ici.

- **Contre-lecture 2** — sous-agent neuf Sonnet 5.5 ; brouillon relu : `preenregistrement-arene-melange-equilibre-v1-brouillon2.md` `622e50d2ad961654b6daaa96d76a94f6dfd2d67188d9f7af199979359c0a1891` ; rapport : `contre-lecture-arene-melange-v2-brouillon2.md` `c6751de38ca84f716d424bc34dccd4103757423932204011a65136bd861cc427`. Verdict : « présentable après corrections » (0 bloquant, 6 majeurs, 4 moyens, 6 mineurs). Traitement :

| Id | Traitement | Où dans ce brouillon |
|---|---|---|
| CM2-01 | **Accepté** : l'essai bâtit ses cas sur une copie temporaire (sans compagnon : refus par le scellement ; copie scellée : refus par non-conformité Seuil, Contre-lecture), indépendant de l'état du dossier ; décompte des essais au LISEZMOI v3. | § Liste d'arrêt ; `test_decision_refusee_copie_brouillon3_pour_la_bonne_raison` |
| CM2-02 | **Accepté, et étendu** : Q1 « à nombre de paramètres égal » (titre, résumé, Hypothèse), phrase « B déploie 1/9 des paramètres » ; « argument contre la piste 3 » retiré ; Q2 à classe de fonctions égale (B′, C3′) ajoutée par décision de routine, déclarée comme bifurcation postérieure au pilote, prédiction écrite avant ; S13 ne décide pas de Q1 (D > B aux deux oracles). Réserve : égalité de classe et de paramètres par requête, pas de total ; maxout de 73 unités absent (lacune). | Titre, Résumé 1, 4 ; § Hypothèse ; § N'autorise pas ; § Prédiction ; S13, S16 |
| CM2-03 | **Accepté** : mesure de la condition d'application (H, I1, I2, I3 ; Table 5) et rubrique « Portée ». Le pilote v3 montre que la condition **est** réunie (A ne progresse pas, oublie) : la remarque « l'arène n'exhibe pas de cycle » tenait à l'absence de mesure. | § Portée ; § Métrique ; Table 5 ; P11 |
| CM2-04 | **Accepté** : m = S1 = 0,02 par principe, fixé avant le pilote v3 ; énumération « ρ → classes » retirée ; équivalence bilatérale cohérente (« écart démontré dans ]−0,02 ; +0,02[ ») ; le déclencheur 3 ne bloque plus la Table 1. Conséquence déclarée : « Q1 confirmée » redevient atteignable en principe ; au pilote, C1 est « B ≳ C1 ». | S6 ; déclencheur 3 ; Table 1 |
| CM2-05 | **Accepté** : déclencheur 9 « conforme et trop propre » ; attaquant indépendant implanté (`attaquant_independant`, modes `audit` et `audit-essai`) ; 10 tâches de la décision ; critère « signe changé ou écart > 0,05 » ; B, C3, D, B′, C3′ ; essayé sur 2 tâches du pilote (aucun artefact). | Déclencheur 9 ; S17 ; § Métrique |
| CM2-06 | **Accepté, déclaré** : A à 1,5 α (v2) et 2,7 α (v3) au pilote à δ 1,8 ; ce que la Table 1 mesure alors est écrit ; δ inchangés ; option de recalibrage sur ≥ 48 instances de la racine réservée, décision de Lazar. | S11 ; Résumé 9 ; Table 1 ligne 4 |
| CM2-07 | **Accepté** : tailles et probabilités mesurées avec le rééchantillonnage réel (20 000 tirages, quantiles linéaires, 1 000 répétitions par scénario) ; dépassements du nominal déclarés. | S2 ; (M3) § 3 |
| CM2-08 | **Accepté** : S10 = moyenne pilote ± 5 × écart-type par tâche / √N. | S10 |
| CM2-09 | **Accepté** : « décision = réplication d'un pilote concluant ; probabilités conditionnelles au pilote » ; audit sur les tâches de la décision ; critère 0,05 au-dessus du bruit apparié. | § Prédiction (en-tête) ; contenu de l'audit ; S17 |
| CM2-10 | **Accepté** : déclencheur 3 sorti de la ligne 1 de la Table 1 ; effet bloquant de chaque déclencheur écrit. | Déclencheurs ; Table 1 |
| CM2-11 | **Accepté** : « énoncé avant toute observation de la v2 » avec la précision sur le brouillon 1. | § Hypothèse |
| CM2-12 | **Accepté** : formulation du contrôle d'exhaustivité corrigée ; tolérance de fausses alertes (50 % de α) et absence de garde entre bras déclarées. | § Liste d'arrêt ; S9 |
| CM2-13 | **Accepté** : seules les prédictions de signe et P4–P8, P10, P11 sont fermes ; C1 et C2 non prédites avec confiance. | § Prédiction B |
| CM2-14 | **Accepté** : PID et instants de départ consignés (scellés en décision) ; TERM converti en arrêt du pool ; arrêt par PID des survivants ; garde « aucun orphelin » et commande `orphelins`, condition d'une reprise. | § Plan 5 ; § Liste d'arrêt |
| CM2-15 | **Accepté** (déclaré) : biais d'optimisation possible en faveur de D (et des maxouts de B′, C3′) ; contrôlé par l'attaquant indépendant. | S17 ; § Hypothèse (hypothèses de travail) |
| CM2-16 | **Accepté** : un seul champ commit, à remplir au gel ; les commits des manifestes de pilote désignent un arbre sans le code (déclaré). | En-tête |
| CM2-17 | Constat positif ; reconduit (essais, reproductibilité, absence de fuite de la racine de décision). | — |

- **Contre-lecture 3** — À REMPLIR : sous-agent neuf d'un modèle autre qu'Opus (identifiant), empreinte de ce brouillon relu, chemin et empreinte de son rapport, traitement de chaque remarque (accepté, refusé et pourquoi).
