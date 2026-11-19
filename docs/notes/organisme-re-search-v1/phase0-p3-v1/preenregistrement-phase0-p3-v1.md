# Préenregistrement — phase 0 de P3 (panorama de candidats offerts au questionneur, monté sur l'instrument de P1), organisme d'idéation, v1

Gabarit suivi : `prereg/gabarit-preregistrement-v1.md` (8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e), sections dans son ordre, plus les sections propres à cette tâche (bloc gelé ; hors table ; calcul de puissance ; devis refait (non engagé) ; ce que la phase 0 ne dit pas ; écarts et choix ; ce qui a été vu avant scellement ; lancement).

- Auteur : modèle I (développeur unique de la phase 0 de P3, session du compte organisme).
- Date (UTC) : 2026-11-18 ; travail commencé à 2026-11-18T05:59:18Z, ce texte écrit à partir de 2026-11-18T06:06:31Z (`date -u`, jamais écrit à la main).
- Statut : **rien n'est exécuté sur la configuration de ce texte** ; **rien n'est adopté dans l'organisme** ; aucune dépense, aucune machine, aucun appel de modèle, aucun accès réseau. Aucune hypothèse ni revendication du programme n'est changée. Le devis refait ci-dessous **n'est pas engagé** : il reviendra à Lazar.
- Commit du code d'analyse : ce texte, `panorama_p3_v1.py`, `lanceur_phase0_p3_v1.py` et `test_phase0_p3_v1.py` (dossier `docs/notes/organisme-re-search-v1/phase0-p3-v1/`, R12) sont versés ensemble, sur la branche `lot/compte-organisme-v1` ; ce texte est scellé d'abord, son empreinte est ensuite posée dans le lanceur, puis le code et les essais sont scellés. Le lanceur écrit le commit exact au manifeste et refuse de partir si l'empreinte de ce texte n'est pas celle qu'il porte.
- **Code de P1 réemployé par import, sans modification** (dossier `docs/notes/organisme-re-search-v1/phase0-p1-p2-v1/`) : `mondes_reponses_p1p2_v1.py` (2c80a833e311b2983fbe6a31d401ac80e3aa03e8d7ccbcb4c3e515d577ebab04 : grammaire des lois, sondes, prédicats, répondeur), `questionneurs_p1_v2.py` (2870503014f301208258e0b4b2310c20b7d1713aadc9ac8d6911ed98f5cded3e : espace H, jeu, bissection, médoïde, rééchantillonnage double), `lanceur_phase0_p1p2_v2.py` (da4312e74d64f0898be4c3259486e61d0ff7357ff9d160a34cca4d345368c47c : gardes de préenregistrement, de code scellé, de fichier, de verdict de contre-lecture ; évaluation des lois de référence par l'évaluateur de l'organisme) et, par lui, `mesure_forme_p2_v1.py` (b3da53aa5dd665c386b9e62a46deb92d94ae418369f147e220e99421fe32b932, non utilisé ici). Le lanceur de P3 vérifie, avant tout calcul, leurs compagnons **et** ces empreintes ; un seul octet changé est un refus de partir.
- Documents qui font foi et pièces lues (empreintes recalculées à la rédaction) :
  - propositions `../propositions-conception-re-search-v1.md` (2b882f8d02d2953072c30a977cd5011eb36810b5f9083617c5d35de80d50f42e), section P3 et son devis, section 0, récapitulatif ;
  - contre-lecture `../contre-lecture-re-search-organisme-v1.md` (f81c778d2fa1c08ab8f56f452b407cbf9afb0eb2cef3a0ffa91129f241c90c24) : P-1 (P3 hors table, écart non déclaré), P-4 (trois issues, puissance avant devis), P-6 (pires cas qui ne sont pas des bornes ; prix plus proches pour argon) ;
  - lecture `../lecture-re-search-v1.md` (21d00c6dd5fdcc5c32bc397c1c1e5d4db62c6abaf20dd1fe93e622914546bbb2), section 2 (e) : conditions de protocole des deux interventions de l'article (réservoir : choix parmi quatre questions, sans référence ni leurre, ordre non rapporté ; panorama : solution incluse une fois parmi 20 à 42 candidats, un leurre de même famille, position non tirée, reconnaissance médiée par le répondeur) ;
  - dossier `../phase0-p1-p2-v1/` : préenregistrement v2 (bff8744edfb80201f0c97c58d54d8f409830707186613b8df2e96ecadd392d0a), code v1 et v2, verdict `verdict-phase0-p1-p2-v2.md` (471a4a4172a9285cc3e4676623341de6fdb3d65fa47363e27768de9ff42184a1) : P1 rendu « instrument discriminant » ;
  - source lue **seulement au lancement, par le lanceur**, empreinte vérifiée : course v67 `/home/user/ideation-organism/resultats/course-v67/poste-local-v1/boucle-reelle-v66.json` (21bc75f4d81825695b30b2b32f21feaa91322293f6c2c3161a28dc179ec6df71), lois plantées et cartes, pour la seule garde de disjonction ; évaluateur de l'organisme `orchestrator/pole/evaluateur_lois_v62.py` (26613fe72da7f049d5dd076aab51a3808221bf52686b9d0258a201c8b38b8632), lecture seule. Non ouverts pour cette tâche.
- Conditions à satisfaire : conditions de la mère (R-3186), P3 ; leur correspondance est donnée à la section « Conditions de la mère (R-3186) : où chacune est satisfaite ».
- Conventions : aucun nom de modèle de la famille du rédacteur ; proposeurs nommés comme dans l'analyse (argon, kimi).

## Bloc « effort et échantillonnage gelés »

Toute la configuration est gelée (tailles, seuils, niveaux, factices, prix du devis) ; le lanceur recalcule l'empreinte du JSON canonique de `bloc_effort(CONFIG)` et **refuse de partir si elle n'est pas écrite ici** :

**Empreinte du bloc « effort et échantillonnage gelés » : f14aca83fc354e49c096c178437d499150c1ff05ced14de31b90be47c9b41837**

```
{
 "p3": {
  "K": 8, "delta_equivalence": 0.05,
  "devis": {"appels_par_monde_et_proposeur": 4, "prix_usd_par_appel": {"argon": 0.20637, "kimi": 0.400484}, "reprises": 0.1},
  "factices_critere": ["hasard", "premier", "dernier", "reconnaisseur:1", "evitant:1", "famille"],
  "factices_kl": ["reconnaisseur:1", "hasard", "famille"],
  "factices_rapportes": ["reconnaisseur:0.15", "evitant:0.5"],
  "limite_lois_sans_leurre": 65536, "mondes": 1088, "mondes_kl": 200, "niveau": 0.975, "niveau_position": 0.995,
  "ordres": [1, 2], "points_de_carte": [0, 4, 8, 16], "politique_refus": "arret",
  "predicats_principaux": 42, "predicats_structurels": 51, "puissance": 0.8, "questions_T": 16,
  "rho_evitant": 0.5, "rho_min": 0.15, "seuil_signature_nat": 0.3,
  "sonde_questions": 2048, "sonde_score": 256, "taille_espace_H": 65536, "tirages_bootstrap": 10000
 },
 "proposeurs_reels": "aucun en phase 0 (questionneurs factices) ; réglages des proposeurs de la phase 1 (effort de raisonnement, température, plafond de jetons, rendu du panorama) à geler au manifeste de la phase 1, avant tout appel, sous un préenregistrement propre",
 "racine_graines": 20261118
}
```

(Ce bloc est recopié en mise en page resserrée ; l'empreinte porte sur le JSON canonique que le code calcule, clés triées.) Le lanceur exige aussi que `mondes` soit la taille rendue par le calcul de puissance (section « Calcul de puissance »), sinon refus.

## Hors table : P3 lève des indécidables, l'écart est déclaré (constat P-1)

La table de décision attache chaque essai à une ligne qui change. **P3 répond aux lignes C2 (les modèles reconnaissent-ils une bonne idée offerte mieux qu'ils ne la produisent ?) et C4 (des candidats extérieurs battent-ils le proposeur seul à coût égal ?), toutes deux restées indécidables.** P3 n'est donc pas ouvert par la règle fixée d'avance : **c'est un essai hors table, pour lever un indécidable, et cet écart est déclaré ici** (constat P-1 de la contre-lecture). Cette phase 0 ne porte que sur **C2**, et seulement sur la mesure : elle dit si l'instrument de reconnaissance retrouve des questionneurs factices de biais connu. C4 (phase 2 de la proposition : candidats extérieurs contre témoin à coût apparié) n'est ni éprouvé ni dimensionné ici. Ouvrir la voie, et toute phase payante, reste la décision de Lazar, sur le devis refait plus bas.

## Hypothèse

**H-P3 (validité de l'instrument de reconnaissance).** Sur des mondes plantés tirés dans la grammaire fermée de P1, quand on offre au questionneur, avant toute question, un panorama de K = 8 lois candidates — bras C : la loi du monde (forme vraie) à une position répartie d'avance ; bras B : le même panorama où la forme vraie est remplacée, à la même position, par un leurre apparié (même famille, même complexité, hypothèse distincte) — et qu'il choisit une carte de reconnaissance **sans aide** (aucune réponse du répondeur, aucun indice), l'écart apparié D = (taux de choix de la cible dans C) − (taux de choix de la cible, le leurre, dans B), lu par la règle gelée à trois issues, **retrouve des questionneurs factices de biais connu** : le bras « choix au hasard », « premier », « dernier » et « famille » au niveau du hasard ; le reconnaisseur parfait au-dessus ; l'évitant parfait en dessous ; et le biais de position de « premier » et « dernier » (et son absence ailleurs) est retrouvé par la part des choix par position. Aucun juge n'intervient : la vérité du monde planté seule (N-058). Renvoi : proposition P3, phase 0 ; lignes C2 (et C4, non éprouvée) de la table, hors table.

**Énoncé de l'article à éprouver plus tard (phase 1, non engagée)** : les modèles reconnaissent une bonne idée offerte mieux qu'ils ne la produisent (lecture, section 2 (e) : chez eux, la reconnaissance est médiée par le répondeur, la position de la ligne n'est pas tirée et le panorama fuit par construction). Dans notre cadre, la phase 1 dira, pour chaque proposeur, laquelle des trois issues tient.

Hypothèses de travail (déclarées) : la famille (type de la racine) et la complexité (nombre de nœuds typés) suffisent à apparier un leurre ; les remplisseurs d'une autre famille rendent la cible repérable par sa famille, ce qui est voulu (c'est le confondant que le leurre apparié neutralise, éprouvé par le factice « famille »).

## Prédiction chiffrée et signe attendu

Valeurs attendues par construction (K = 8, hasard 1/K = 0,125), par factice du critère :

| factice | taux C attendu | taux B attendu | D attendu | issue attendue | biais de position attendu |
|---|---|---|---|---|---|
| hasard (bras « choix au hasard ») | 0,125 | 0,125 | 0 | au niveau du hasard | aucun |
| premier | 0,125 exactement (plan) | 0,125 exactement | 0 exactement | au niveau du hasard | première position |
| dernier | 0,125 exactement | 0,125 exactement | 0 exactement | au niveau du hasard | dernière position |
| reconnaisseur:1 | 1 exactement | 0,125 | 0,875 | au-dessus du hasard | aucun |
| evitant:1 | 0 exactement | 0,125 | −0,125 | en dessous du hasard | — (non jugé) |
| famille (artefact) | 1 exactement | 1 exactement | 0 exactement | au niveau du hasard ; lecture sans leurre « au-dessus » | — (non jugé) |

Rapportés sans décision (puissance empirique à la taille retenue) : reconnaisseur:0,15 (D = 0,13125, issue attendue « au-dessus » avec une probabilité ≈ 0,80 au moins) ; evitant:0,5 (D = −0,0625, « en dessous », ≈ 0,80 au moins).

Confiance : ≈ 95 % que les cinq factices déterministes soient conformes (construction) ; **≈ 90 % pour le bras « choix au hasard »** : son issue « au niveau » est aléatoire ; sous l'hypothèse prudente de la taille (ordres parfaitement corrélés) sa probabilité est 0,80 ; ses deux ordres étant ici indépendants, elle est bien plus haute (simulation des essais : ≥ 0,95) ; et ≈ 97 % qu'aucun biais de position faux ne soit détecté pour le hasard et le reconnaisseur. Réfutation de H-P3 : un factice du critère dont l'issue, un écart exact, un taux exact ou le biais de position diffère de l'attente.

## Métrique

- **Monde** : une loi de l'espace H de P1 (65 536 lois tirées une fois dans la grammaire fermée, disjointes des lois plantées et des cartes de la course v67 par la signature prédictive, 0,30 nat, code de P1). 1 088 mondes tirés sans remise, parmi les lois qui ont un leurre apparié ; les lois écartées faute de leurre sont comptées et rapportées (limite d'arrêt : 65 536).
- **Famille et complexité** : famille = type de la racine ; complexité = nombre de nœuds typés de l'arbre. **Leurre apparié** : une loi de H de même famille et de même complexité que le monde, distincte de lui (divergence moyenne > 0,30 nat dans les deux sens sur la sonde de score), tirée par la graine dérivée de la loi. **Remplisseurs** : K − 1 = 7 lois de H d'une autre famille que le monde, distinctes entre elles, du monde et du leurre (même critère).
- **Plan des positions (réparti d'avance)** : 136 blocs de 8 mondes, chaque bloc une permutation de 0…7 tirée par la graine « p3/plan » ; tout préfixe de 8m mondes est équilibré. **Deux ordres de présentation** : ordre 1, le plan (la cible à la position p) ; ordre 2, le panorama renversé (la cible à 7 − p). Chaque position porte la cible exactement 136 fois dans chaque ordre (garde).
- **Panoramas appariés** : C et B ne diffèrent que par la position de la cible (forme vraie dans C, leurre dans B) ; la forme vraie n'est jamais dans B, le leurre jamais dans C.
- **Carte de reconnaissance sans aide** : avant toute question, le questionneur reçoit un état qui ne porte **que K et le panorama présenté** (lois copiées) et rend une position ; aucun répondeur n'existe à ce moment. Les factices qui simulent une reconnaissance (reconnaisseur, évitant, famille) reçoivent du banc une vérité simulée (position de la forme vraie dans C, famille du monde) : c'est leur biais connu, déclaré ; tout autre questionneur qui la demande est refusé. Chaque questionneur joue C et B dans les deux ordres : quatre cartes par monde.
- **Écart D** (métrique principale) : par monde, D_w = moyenne sur les deux ordres de [1(cible choisie dans C) − 1(cible choisie dans B)] ; D = moyenne des D_w. Intervalle : quantiles empiriques (méthode `inverted_cdf`) de 10 000 rééchantillonnages des mondes, au niveau **0,975** (correction de Bonferroni sur les deux proposeurs de la phase 1, appliquée dès la phase 0 pour juger l'instrument à son réglage d'usage). Rapportés : taux dans C et dans B avec intervalles ; « lecture sans leurre » (taux C − 1/K, même règle).
- **Biais de position** : part des choix à chaque position présentée, sur les quatre cartes par monde ; biais vers la première (resp. dernière) position détecté si la borne basse de sa part, intervalle au niveau **0,995** (10 000 rééchantillonnages des mondes), dépasse 1/K.
- **Recouvrement sur l'instrument de P1 (rapporté, sans décision)** : sur les 200 premiers mondes du plan (préfixe équilibré), ordre 1, la bissection de P1 pose T = 16 questions (répondeur exact, prédicats empiriques, ordre de présentation des prédicats tiré par graine) ; bras A (seul) : carte de P1 (médoïde) ; bras B et C : la carte de reconnaissance est gardée tant qu'elle est compatible avec les réponses, sinon carte de P1 ; KL(monde ‖ carte) à 0, 4, 8, 16 questions ; comparaisons C − B, C − A, B − A à T = 16 par le rééchantillonnage double de P1 (médianes et moyennes, 95 %), pour reconnaisseur:1, hasard et famille.
- Coût de la phase 0 : 0 USD.

## Seuil

- **Règle gelée à trois issues** (pour un questionneur ; intervalle [lo, hi] de D au niveau 0,975) : lo > 0 → **au-dessus du hasard** ; hi < 0 → **en dessous du hasard** ; −δ < lo et hi < δ avec **δ = 0,05** → **au niveau du hasard** ; sinon **non concluant** (défaut de puissance, jamais une quatrième conclusion).
- **Critère de validité (phase 0)** : chaque factice du critère conforme à toutes ses attentes du tableau de prédiction (issue ; D exactement 0 et intervalle de largeur nulle pour premier, dernier, famille ; taux C exactement 1 pour reconnaisseur:1 et famille, 0 pour evitant:1 ; lecture sans leurre « au-dessus » pour famille ; biais de première et de dernière position détecté ou non comme attendu pour hasard, premier, dernier, reconnaisseur:1). Conjonction, aucune correction supplémentaire.
- **Gardes** (elles priment ; chacune est un refus écrit, arrêt de P3) : plan équilibré ; chaque panorama conforme (taille, doublons, cible à sa place, C et B égaux ailleurs, forme vraie hors de B, leurre hors de C, leurre de même famille et complexité, remplisseurs d'une autre famille, distinction par la signature) ; carte sans aide (état réduit à K et au panorama ; vérité seulement aux factices déclarés) ; aucune carte hors panorama (règle « arrêt ») ; grammaire des prédicats de P1 inchangée ; lois sans leurre sous la limite.
- Taux d'erreur visés : 0,025 bilatéral par intervalle de D (0,05 sur la famille des deux proposeurs de la phase 1) ; 0,005 par intervalle de position ; puissance 0,80 par issue (section suivante).

## Calcul de puissance

Fait **avant tout devis**, par le code gelé (`taille_necessaire`, approximation normale de l'intervalle, niveau 0,975, z = 2,2414), sous une hypothèse **prudente** : les deux ordres d'un même monde sont parfaitement corrélés (l'unité est le monde ; le doublement des ordres ne fait rien gagner) ; indicatrices C et B indépendantes (une corrélation positive, comme celle d'un questionneur à biais de position, réduit la variance). Trois issues à distinguer, chacune rendue avec une probabilité au moins 0,80 quand elle est vraie :

| issue vraie | modèle | D | variance d'une unité | taille (mondes) |
|---|---|---|---|---|
| au niveau du hasard | p_C = p_B = 1/8 | 0 | 0,21875 | n ≥ 0,21875 · ((2,2414 + 1,2816) / 0,05)² = **1 085,98** |
| au-dessus | reconnaisseur ρ_min = 0,15 : p_C = 0,25625 | 0,13125 | 0,29996 | n ≥ 0,29996 · ((2,2414 + 0,8416) / 0,13125)² = 165,51 |
| en dessous | évitant ρ = 0,5 : p_C = 0,0625 | −0,0625 | 0,16797 | n ≥ 0,16797 · ((2,2414 + 0,8416) / 0,0625)² = 408,72 |

- **Taille nécessaire : 1 088 mondes par questionneur** (le maximum, 1 085,98, arrondi au multiple de 8 supérieur pour le plan), dimensionnée par l'issue « au niveau du hasard » ; **4 parties (cartes) par monde** (C et B × deux ordres), soit **4 352 cartes de reconnaissance par proposeur**, **8 704 appels** pour deux proposeurs. Variante optimiste rapportée (ordres indépendants) : 544 mondes, 2 176 appels par proposeur.
- Choix des effets (gelés ici, à rediscuter par Lazar avant la phase 1) : δ = 0,05 (40 % du hasard) ; ρ_min = 0,15 (effet de reconnaissance le plus petit qui vaille d'être vu) ; évitement ρ = 0,5 (moitié du hasard) ; l'écart « en dessous » doit dépasser δ (sinon les issues ne se séparent pas : refus écrit du code).
- Contrôle de l'approximation : par simulation (essai `test_puissance_controlee_par_simulation`, 600 répétitions à 1 088 mondes, ordres corrélés) chaque issue vraie est rendue au moins 75 % du temps, jamais l'issue opposée ; ordres indépendants, le hasard est « au niveau » au moins 95 % du temps.
- La phase 0 joue cette taille : elle vérifie que l'instrument rend les issues attendues **à la taille du devis**, et rapporte la puissance empirique sur reconnaisseur:0,15 et evitant:0,5.
- Le recouvrement à T = 16 (rapporté) n'est pas dimensionné : sa puissance se lira sur la dispersion rapportée par cette phase 0 et la phase 1 de P1 ; il n'entre pas dans le devis.

## Devis refait (non engagé)

Sur la taille de la puissance. Prix unitaires : seulement ceux des fichiers lus — coûts observés d'un appel de proposeur de la course v67, génération 1 et 2, tels que les propositions les citent (argon 0,20637 USD, `S1.M1.1.par_proposeur.argon.cout_proposeur_usd` ; kimi 0,400484 USD, `S1.M1.2.par_proposeur.kimi.cout_proposeur_usd`). **Unité différente** : un appel de carte de reconnaissance (un panorama de huit lois, une position en réponse) n'est pas un appel de proposeur ; **prix d'un appel de carte : à relever**. La contre-lecture (P-6) signale, pour argon seulement, des coûts plus bas par appel en S2a et S2b (0,060884 et 0,077161 USD) : non retenus pour le pire cas.

| poste | appels | prix unitaire et source | estimation | pire cas |
|---|---|---|---|---|
| phase 0 | 0 | — | 0 USD | 0 USD |
| phase 1, argon | 1 088 mondes × 4 cartes = 4 352 | 0,20637 USD (coût d'un appel de proposeur, course v67 ; prix d'un appel de carte à relever) | 898,12 USD | — |
| phase 1, kimi | 4 352 | 0,400484 USD (idem) | 1 742,91 USD | — |
| phase 1, total (taille prudente) | 8 704 | — | 2 641,03 USD | 8 704 appels au plus haut prix observé, plus 10 % de reprises : **3 834,39 USD** |
| variante optimiste (544 mondes) | 4 352 | idem | 1 320,51 USD | 1 917,20 USD |
| bras « choix au hasard », questionneurs factices | 0 | — | 0 USD | 0 USD |
| phase 2 (C4) | non dimensionnée | — | — | — |

Ce devis remplace celui de la proposition (phase 1 : 456 appels, pire cas 200,88 USD, sur 6 mondes sans puissance, constat P-4). Il n'est **pas engagé** : il revient à Lazar avec la lecture de cette phase 0 ; aucune dépense de P3 n'est faite ici. Les réglages des proposeurs (effort, température, plafond de jetons, rendu du panorama en texte) seront gelés au manifeste de la phase 1, sous son propre préenregistrement.

## Plan d'analyse

1. Sondes (questions 2 048, score 256) ; lois de référence de la course v67 évaluées par l'évaluateur de l'organisme (empreinte vérifiée) ; espace H de 65 536 lois disjointes (code de P1) ; contrôle de la grammaire des prédicats (51 colonnes, 42 empiriques).
2. Familles de H ; 1 088 mondes avec leurre apparié (graines « p3/mondes », « p3/leurre/<loi> ») ; plan (graine « p3/plan ») et sa garde ; remplisseurs (« p3/remplisseurs/<i> ») ; panoramas et leur garde.
3. Cartes de reconnaissance : chaque factice (six du critère, deux rapportés) × 1 088 mondes × {C, B} × {ordre 1, ordre 2} ; graine par carte « p3/carte/<questionneur>/<bras>/<ordre>/<i> ».
4. Par factice : trois issues (graine « p3/bootstrap/<questionneur> »), biais de position (« p3/bootstrap-position/<questionneur> »), conformité aux attentes gelées.
5. Recouvrement sur l'instrument de P1 (rapporté) : 200 premiers mondes, ordre 1 ; graines « p3/kl/partie/<i>/questionneur », « p3/kl/partie/<i>/ordre », « p3/kl/bootstrap/<questionneur>/<comparaison> ».
6. Calcul de puissance et devis recalculés et écrits dans la sortie.
- **Graines (R9)** : `numpy.random.SeedSequence(20261118, spawn_key=(k,))`, k = entier des 8 premiers octets du sha256 du nom de la tâche (fonction de P1). Le manifeste écrit la racine, la règle, la liste des tâches, la configuration et son empreinte, le bloc gelé et son empreinte, les versions (python, numpy, modules), les empreintes de ce texte, de la contre-lecture, du code de P3, du code de P1 réemployé, de l'évaluateur et de la source, le commit et l'état de l'arbre.
- **Comparaisons multiples** : une seule conjonction décisive (gardes, puis conformité des six factices) ; intervalles de D au niveau 0,975 (Bonferroni sur deux proposeurs) ; intervalles de position au niveau 0,995 ; tout le reste rapporté sans décision.

## Critères de lecture gelés

**P3, phase 0** (lecture proposée par le code, prononcée par un lecteur neuf, R13 ; les gardes priment) :

| gardes | issues et valeurs exactes des factices (hors position) | biais de position des factices | verdict |
|---|---|---|---|
| une au moins échoue (arrêt écrit) | — | — | **garde défaillante** : arrêt, audit du code, aucun devis soumis |
| tiennent | une au moins non conforme | — | **instrument de reconnaissance non discriminant (issues)** : arrêt, rapporté, aucun devis soumis |
| tiennent | conformes | un au moins non conforme | **biais de position non retrouvé** : arrêt, rapporté, aucun devis soumis |
| tiennent | conformes | conformes | **instrument de reconnaissance discriminant** : le devis refait de la phase 1 peut être soumis à Lazar (non engagé) |

- **Trois issues écrites d'avance pour la phase 1** (par proposeur, même règle, même niveau, mêmes δ et taille) : **reconnaissance au-dessus du hasard** (C2 tient dans notre cadre pour ce proposeur : il choisit la forme vraie offerte plus souvent que son leurre apparié) ; **au niveau du hasard** (équivalence à ±0,05 : il ne distingue pas la forme vraie du leurre) ; **en dessous du hasard** (il évite la forme vraie au profit du leurre) ; « non concluant » n'est pas une issue : c'est un défaut de puissance, rapporté tel quel. Rapporté aussi en phase 1 : l'écart est-il plus grand pour le plus faible des deux proposeurs (l'article l'affirme), et le biais de position de chacun.
- Audit de symétrie (R4), sans changer le verdict, motifs écrits : intervalle de D du bras « choix au hasard » de largeur nulle ; taux du hasard exactement 1/K dans C et dans B (trop propre) ; un factice du critère dont l'issue contredit l'attente (dans un sens comme dans l'autre). Action : relecture du code du plan, des panoramas et des cartes avant tout rapport.
- Les mesures rapportées (factices partiels, recouvrement sur l'instrument de P1, lecture sans leurre hors du factice famille, parts par position) ne changent pas le verdict.

## Liste d'arrêt

| condition | action |
|---|---|
| empreinte de ce texte ≠ celle qu'attend le lanceur, ou compagnon `.sha256` absent ou non conforme | refus de partir (code 2), rien écrit |
| empreinte du bloc gelé absente de ce texte | refus de partir (code 2), rien écrit |
| nombre de mondes ≠ taille rendue par le calcul de puissance gelé | refus de partir (code 2), rien écrit |
| contre-lecture absente, non scellée, ou verdict écrit autre que « scellable », ou qui ne cite pas l'empreinte de ce texte (« scellable après corrections » compris : des corrections exigent une v2 et un lanceur v2) | refus de partir (code 2), rien écrit |
| module de P3 sans compagnon conforme ; module de P1 sans compagnon conforme ou d'empreinte ≠ attendue | refus de partir (code 2), rien écrit |
| évaluateur de l'organisme ou source v67 absent ou d'empreinte inattendue | refus de partir (code 2), rien écrit |
| mode d'essai avec la configuration réelle ; dossier de sortie déjà présent (R12) | refus (code 2), rien écrit ; le lecteur R13 refuse toute sortie « essai » |
| plan non équilibré ; panorama non conforme ; leurre non apparié ; remplisseurs introuvables ; plus de 65 536 lois sans leurre | arrêt de P3, motif écrit (`arret`), verdict « garde défaillante » |
| carte hors panorama (règle « arrêt ») ; questionneur non déclaré qui lit la vérité ; état de carte avec une aide | arrêt de P3, motif écrit |
| grammaire des prédicats différente de celle de P1 ; loi de référence hors gabarit | arrêt de P3, motif écrit |
| verdict autre que « instrument de reconnaissance discriminant » | aucun devis soumis ; rapporté tel quel |
| tout refus de permission, de crochet ou de classifieur pendant le run | arrêt, rapport tel quel |

Aucun repli silencieux : chaque arrêt écrit son motif dans la sortie ; sortie, manifeste et journal des fichiers ouverts sont scellés.

## Conditions de la mère (R-3186) : où chacune est satisfaite

| condition | où |
|---|---|
| positions des candidats réparties d'avance (plan équilibré, graine dérivée) | `plan_positions`, `exiger_plan_equilibre` ; graine « p3/plan » ; essai `test_plan_equilibre_sain_et_artefacts` |
| questionneurs factices à biais de position connu (premier, dernier, hasard, reconnaisseur de la vraie forme) et l'instrument retrouve ce biais | `Premier`, `Dernier`, `Hasard`, `Reconnaisseur` (plus `Evitant`, `Famille`) ; `biais_de_position`, `ATTENTES_FACTICES` ; essai `test_factices_retrouves_sur_petits_mondes` |
| carte de reconnaissance sans aide | `jouer_carte` (état réduit à K et au panorama ; vérité seulement aux factices déclarés) ; essai `test_carte_sans_aide_saine_et_artefacts` |
| leurre apparié à la forme vraie (même famille, même complexité) | `famille`, `choisir_leurre`, `exiger_panorama` ; essais `test_leurre_apparie_meme_famille_et_distinct`, `test_sans_leurre_apparie_la_famille_passerait_pour_reconnaissance` |
| deux ordres de présentation et un bras « choix au hasard » | ordres 1 et 2 (miroir) dans `jouer_reconnaissance` ; factice `hasard` |
| trois issues écrites d'avance | `issue`, `trois_issues` ; section « Critères » ; essai `test_regle_trois_issues_sur_tableaux_synthetiques` |
| calcul de puissance avant tout devis, rendant la taille | `taille_necessaire` ; garde `exiger_puissance` ; section « Calcul de puissance » |
| devis refait sur cette taille, prix des fichiers lus ou « à relever » ; revient à Lazar ; aucune dépense ici | `devis` ; section « Devis refait (non engagé) » |
| P3 « hors table », écart déclaré | section « Hors table » ; clé `hors_table` de la sortie |
| R1, R4, R5, R6, R9, R12, N-058 | ce texte scellé avant toute exécution ; audit R4 ; chaque garde sur un cas sain et un artefact ; compagnons ; graines dérivées et manifeste ; fichiers neufs ; vérité du monde planté, aucun juge |

## Ce que la phase 0 ne dit pas

- Rien sur les proposeurs réels : aucun ne joue ; l'énoncé de l'article (reconnaître mieux que produire) n'est pas éprouvé ici, seulement l'instrument qui l'éprouvera.
- Rien sur la **découverte** : le bras C contient la vérité par construction ; C − B mesure la reconnaissance, jamais la production. La comparaison « reconnaître contre produire » demandera, en phase 1, de rapprocher D du recouvrement du bras A (seul) de P1 pour le même proposeur : ce rapprochement n'est pas préenregistré ici.
- Rien sur C4 (candidats extérieurs, témoin à coût apparié, phase 2) : non éprouvé, non dimensionné.
- Rien sur le rendu en texte d'un panorama pour un modèle (longueur, mise en forme, fuite par le texte) : la phase 1 devra le geler ; les factices choisissent une position sans lire de texte.
- Rien sur la boucle de production : aucun panorama contenant une loi vraie connue ni un témoin du pôle n'est jamais servi dans la boucle (propositions, section 0, point 3) ; rien n'est adopté ; la note de conception reste suspendue.
- Rien sur une composition de proposeurs (N-058).
- Le recouvrement à T = 16 est rapporté, sans décision ni puissance.
- Aucune dépense, aucune machine, aucun accès réseau.

## Écarts à la proposition et choix déclarés

1. **Métrique principale** : la proposition jugeait C2 sur le recouvrement à T = 16 (divergence) ; elle est jugée ici sur la carte de reconnaissance sans aide (conditions de la mère (R-3186)), le recouvrement étant rapporté. Raison : c'est la reconnaissance que l'énoncé vise, et la seule mesure dimensionnable avant la phase 1.
2. **Position répartie d'avance**, non tirée au hasard partie par partie (proposition : « position tirée au hasard ») : plan en blocs équilibrés, plus strict.
3. **Panorama de K = 8**, non 20 à 42 comme l'article : avec un hasard à 1/K, l'issue « en dessous » n'est séparable de la marge que si 1/K dépasse nettement δ ; à K = 20, |D−| ≤ 1/20 = δ. Choix déclaré, effet sur la comparabilité à l'article dit.
4. **Famille = type de la racine, complexité = nombre de nœuds typés** : lecture de « même famille, même complexité » dans notre grammaire ; le leurre peut avoir la même forme que le monde (mêmes types, autres paramètres) pourvu qu'il soit une hypothèse distincte (signature).
5. **Remplisseurs d'une autre famille** que le monde : rend la cible repérable par sa famille, à dessein, pour que le factice « famille » éprouve le leurre apparié.
6. **Bonferroni sur deux proposeurs dès la phase 0** : l'instrument est jugé à son réglage d'usage.
7. **Hypothèse prudente de la puissance** (ordres corrélés) : elle double presque la taille ; la variante optimiste est rapportée avec son devis.
8. **Mondes sans leurre** : écartés et comptés (sélection déclarée vers les familles peuplées).
9. **Questions du recouvrement** : la bissection de P1 pose les mêmes questions dans A, B et C (même graine), pour que seule la carte change.

## Ce qui a été vu avant scellement (déclaré, R1 et R4)

- Rien de la configuration de ce texte : ni l'espace H à 65 536 lois, ni les 1 088 mondes, ni la course v67 (empreinte seulement, recalculée par le lanceur au lancement).
- Le calcul de puissance et le devis : calculés par le code gelé sur les seuls paramètres de ce texte (aucune donnée) ; chiffres ci-dessus.
- **Petits mondes d'essai** seulement (racine 4242 ; H = 256 lois, sondes 512 et 128, 64 mondes, 2 000 rééchantillonnages ; aucune loi écartée faute de leurre) : hasard « non concluant » (D = 0,0938, [−0,0078 ; 0,1953] ; taux C 0,1953, B 0,1016) — attendu à 64 mondes, loin de la taille de la puissance ; premier et dernier : D = 0 exactement, taux 0,125, « au niveau », biais retrouvé ; reconnaisseur:1 : D = 0,8281 [0,7578 ; 0,8906], « au-dessus » ; evitant:1 : D = −0,125 [−0,1953 ; −0,0625], « en dessous » ; famille : taux C et B de 1, D = 0, « au niveau », lecture sans leurre « au-dessus » ; reconnaisseur:0,15 : D = 0,1641 [0,0781 ; 0,25], « au-dessus » ; evitant:0,5 : D = −0,0859 [−0,1719 ; −0,0078], « en dessous ». Sur ces petits mondes, le critère échoue donc par le seul bras « choix au hasard » (non concluant), comme il le doit sans puissance (essai `test_conformite_des_factices_et_lecture`). Aucun seuil n'a été changé après ces essais ; δ, ρ_min, ρ de l'évitant, K et les niveaux ont été fixés avant de les lancer.
- Remarque sur la construction : les factices déterministes (premier, dernier, famille) donnent des intervalles de largeur nulle par construction (plan équilibré, panoramas appariés) ; ce n'est pas un motif d'audit R4, qui ne porte que sur le bras « choix au hasard ».

## Lancement (après contre-lecture et versement, jamais avant)

`cd /home/user/controle-ia-travail/docs/notes/organisme-re-search-v1/phase0-p3-v1 && python3 -B lanceur_phase0_p3_v1.py --sortie <dossier neuf> --contre-lecture <rapport de contre-lecture scellé>` ; le lanceur porte l'empreinte attendue de ce texte et refuse de partir sinon, ou sans contre-lecture « scellable » de ce texte. Durée non mesurée à l'échelle (processeur seul ; la construction de H domine, comme pour P1, environ douze minutes). Le lancement lui-même est une décision à part ; ce texte ne l'engage pas.

## Contre-lecture

- **À faire, avant tout lancement** : par un sous-agent neuf, d'un autre modèle que le développeur, qui n'a écrit aucune pièce de cette tâche (R2), à qui l'on donnera explicitement à lire ce texte, `panorama_p3_v1.py`, `lanceur_phase0_p3_v1.py`, `test_phase0_p3_v1.py`, le code de P1 réemployé, la section P3 des propositions, les constats P-1, P-4 et P-6 de la contre-lecture et la section 2 (e) de la lecture.
- Le lanceur n'accepte qu'un rapport scellé dont le verdict écrit (titre « ## Verdict ») est « scellable » et qui cite l'empreinte de ce texte. Tout autre verdict arrête le lancement ; des corrections donneront une v2 de ce texte (nouveau nom, R12) et un lanceur v2.
- Le validateur `controle_ia.prereg` signale, à juste titre, que cette section ne porte pas encore les deux empreintes (texte relu et rapport) : elles n'existent qu'après la contre-lecture ; ce texte est donc scellé par `controle_ia.scellement` (compagnon), non par `sceller_prereg`, et c'est la garde du lanceur qui exige le rapport.
- Aucun rapport n'existe au scellement de ce texte : sans lui, le lancement est refusé (essai `test_vrai_preenregistrement_scelle_et_lancement_reel_refuse_sans_contre_lecture`).
