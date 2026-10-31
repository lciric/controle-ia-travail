# Contre-lecture (R2) — préenregistrement « arène : mélange d'équilibre contre ses témoins à capacité égale » v1, brouillon 2 — brouillon 1 de la contre-lecture

- Auteur : sous-agent Sonnet 5.5 neuf (autre modèle que l'auteur Opus 5.5 du brouillon 2 et du code v2). Il n'a écrit ni le préenregistrement, ni le code, ni les essais, ni le calcul de puissance, ni la contre-lecture du brouillon 1.
- Date (UTC) : 2026-10-31, 10:07 (relevé `date -u`). Branche `canal/conv-audit-n04`.
- Texte relu : `preenregistrement-arene-melange-equilibre-v1-brouillon2.md`, empreinte `622e50d2ad961654b6daaa96d76a94f6dfd2d67188d9f7af199979359c0a1891` (conforme à son compagnon `.sha256` et au LISEZMOI).
- Empreinte de ce rapport : à calculer par l'agent parent (aucun compagnon écrit par moi, consigne).
- Rien modifié dans le dépôt hors ce rapport. Rien lu sous `donnees/`. Aucune graine tirée de RACINE = 20261201 ni de RACINE_TENUE = 20261202. Mes diagnostics (scripts dans `/tmp/cm2_diag/`, hors dépôt : `attaquant_alt.py` `088d2388…`, `lp.py` `27e6fa68…`, `motifs.py` `02cf2a8e…`, `taille_boot.py` `db3eb7a8…`) emploient la racine d'essai neuve **20269501 / 20269502**, jamais utilisée ailleurs (recherche dans le dépôt : aucune occurrence).

## 0. Verdict

**Présentable après corrections.** Aucun constat bloquant ; six majeurs, quatre moyens, six mineurs (§ 3), un constat positif.

Le code est sain et la plomberie tient (essais, reproductibilité de la puissance, programme linéaire, attaquant). La réfutation prédite **n'est pas un artefact de l'attaquant ni de l'équité des fausses alertes** : j'ai opposé aux défenses finales de B, C1, C3, D (et A) un attaquant beaucoup plus lourd et une stratégie d'évolution sans gradient, sur racine neuve ; ils ne font pas mieux que l'attaquant du code, sauf un écart de 0,02 sur D dans une tâche, qui joue en faveur de D mais ne change aucun signe (§ 2.5).

Ce qui doit changer touche **ce que la réfutation veut dire** et quelques énoncés faux ou fragiles du texte : (i) l'hypothèse principale « B bat des témoins à capacité égale » est, dans cette arène, presque assurée d'échouer par construction (B ne dispose que de moniteurs linéaires tirés un à un, C3 et D disposent des neuf moniteurs à la fois ou d'une famille plus riche), et le texte l'appelle « capacité égale » et en tire un « argument contre la piste 3 » que rien ne justifie ; (ii) l'arène ne montre pas la non-convergence de Bailey que le mélange est censé guérir ; (iii) S6 (ρ = 0,25) recrée le défaut « choisir en connaissant la réponse » que la contre-lecture 1 avait fait retirer pour S5 ; (iv) l'audit R4 ne se déclenche que sur surprise, alors que la réfutation à 1,000 est justement le résultat « trop propre » ; (v) δ_haut = 1,8 laisse A à 1,5 α au pilote, ce que le texte dit ne pas être ; (vi) un essai du code est rouge à la remise. Aucune correction ne demande de toucher à la racine de décision ; les corrections de texte n'exigent pas de nouveau pilote ; une seule (CM2-01) change un fichier d'essais (donc son empreinte ligne 16).

## 1. Ce que j'ai fait (traçabilité)

- `sha256sum -c` sur tous les compagnons du dossier : conformes (22 fichiers). Empreintes citées par le texte (bibliothèque `gardes.py`, `prereg.py`, `scellement.py`, `manifeste.py`, gabarit, brainstorm, réponse pont) : conformes. `arene_melange_v2.py identite` imprime le bloc du texte (lignes 30-38, configuration) à l'identique.
- `python -m pytest -q -p no:cacheprovider essais/test_arene_melange_v2.py` (`PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src`) : **44 réussis, 1 échec**, 20,8 s : `test_decision_refusee_brouillon2_pour_la_bonne_raison` (CM2-01). Essais v1 (`essais/test_arene_melange_v1.py`) : **25 réussis**, 4,8 s. Aucun `__pycache__` créé.
- `calcul-puissance-arene-melange-v2.py` rejoué sur les deux pilotes : sortie **identique** à (M) (une ligne vide finale près), 23 s.
- Validateur `problemes` (via `python -I`, `PYTHONPATH=src`) : refuse le brouillon pour « Seuil » et « Contre-lecture » seulement, comme annoncé. Le marqueur « À REMPLIR » de la ligne 7 (commit) sera refusé après remplissage des deux sections (règle « hors des sections exigées »), c'est voulu.
- Transcription des chiffres du texte vers (M), le gel, le journal : tous les nombres que j'ai recoupés (résumé 4 à 7, P1 à P7, S1, S3, S4 à S6, S8 à S11, descriptives, courbes, plages S10, parts censurées) sont conformes. Aucun écart de transcription trouvé.
- Programme linéaire : 300 matrices aléatoires (dont un cinquième à valeurs arrondies, équilibres non uniques) : conditions d'équilibre vérifiées (`min_j pG ≥ v`, `max_i Gq ≤ v`), valeur au moins égale à la borne par force brute ; orientation (lignes = moniteurs qui maximisent) conforme à `trajectoire`.
- Racines : les trois fichiers de pilote et de calibrage portent chacun dans leur manifeste et dans chaque résultat leurs racines (20261293/4 ; 20261295/6), jamais 20261201/2 ni 20261291/2. `20261201` n'apparaît qu'une fois dans le code (la constante `RACINE`).
- Ordre des étapes : les horodatages de fichiers (CET, UTC + 1) concordent avec le journal : code 09:15 UTC, gel 09:16 UTC (avant le pilote 09:16:56), script de puissance 09:18 UTC (avant la fin du premier pilote à 09:29). Je n'ai pas de moyen de prouver au-delà du journal et des `mtime`.

## 2. Réponses aux points demandés

### 2.1 CM-01 à CM-17

| Id | Sort | Où dans le brouillon 2 | Réserve |
|---|---|---|---|
| CM-01 | traité | principe l. 142 ; archive l. 314 ; A renommé l. 110, 124, 290 ; pilote logistique complet l. 159-160 ; racine fraîche l. 153, 297 ; gel `gel-conception-arene-melange-v2.md` | « énoncé avant toute observation » inexact chronologiquement (CM2-11) |
| CM-02 | traité | B − A en contrôle de plomberie l. 147, 303 ; HP l. 144 | le remplaçant pose le problème CM2-02 |
| CM-03 | traité | C1, C2, C3 sur les neuf moniteurs mêmes de B l. 146, 293 ; D déclaré « pas la capacité » l. 126, 146 | « capacité égale » reste le titre (CM2-02) |
| CM-04 | **traité en partie** | δ par règle sur A seul l. 265 ; marges relatives l. 240 ; « B > X » exige une borne basse au-dessus de la marge l. 371 | δ_haut : A à 1,5 α au pilote (CM2-06) ; marge fondée sur B − A à A quasi nul (CM2-04) |
| CM-05 | traité (taille à revoir) | résumé l. 115 ; S1, S2 l. 216, 221 ; règle nommée | tailles mesurées avec des bornes de Student, pas avec la règle de décision (CM2-07) |
| CM-06 | traité | S5 = S1 par principe l. 235 ; lecture sans seuil l. 236, 363 ; ligne « démontrée sous la tolérance » l. 358 | S5 liste encore la lecture au pilote de chaque option (l. 236), sans conséquence ici ; le même défaut revient sur S6 (CM2-04) |
| CM-07 | **traité en partie** | déclencheurs dans les deux sens l. 327-335 ; plages calibrées l. 260 | audit seulement sur surprise (CM2-05) ; S10 pratiquement inerte (CM2-08) |
| CM-08 | traité, un essai rouge | 52 gardes, un essai par motif l. 395 ; scellement refusé pour la bonne raison l. 399 | essai rouge (CM2-01) ; l'adverbe « mécaniquement » est trop fort (CM2-12) |
| CM-09 | traité | statuts, itérations, départs non finis comptés, garde à 5 % l. 206, 412 | — |
| CM-10 | traité | κ relatif, garde de ligne de base, parts par δ, courbe l. 203-204, 281 | mesure non comparable d'un bras à l'autre (ligne de base propre), sans verdict : acceptable |
| CM-11 | traité | « itéré tronqué » l. 291 ; écart rapporté l. 191, 206 ; équilibres non uniques : déclaration | — |
| CM-12 | traité | règle de reprise l. 311 | arrêt par `timeout` et processus orphelins (CM2-14) |
| CM-13 | traité | Tables 1 à 4 réécrites l. 339-391 ; motif l. 351 ; essai d'exhaustivité (2 000 configurations) | — |
| CM-14 | traité | configuration canonique imprimée et comparée champ à champ l. 40-106 ; empreintes de la bibliothèque ; N comparé à `--instances` | seuils de lecture (S1, S2, S3, S5, S6, S10) contrôlés à la main seulement : déclaré l. 427 |
| CM-15 | traité | garde dans `gen`, re-vérifiée dans chaque processus l. 300 | — |
| CM-16 | traité (déclaré) | l. 149, 292 | — |
| CM-17 | traité | commit « À REMPLIR au gel » l. 7 ; minimum de deux estimations déclaré l. 199 ; déclencheur de fausses alertes l. 335 | confiances (CM2-13) ; trois commits différents cités (CM2-16) |

Aucun constat non traité.

### 2.2 Correction du code

- **Programme linéaire** : correct (§ 1). `resoudre_jeu` vérifie primal et dual à 1e-7, statuts, matrice dans [0 ; 1]. Équilibres non uniques : sommet HiGHS, déclaré.
- **Double oracle de B** (`trajectoire`, l. 817-851) : meilleure réponse de l'attaquant contre p ; colonne ajoutée à G ; q de l'attaquant sur la matrice élargie ; nouveau moniteur entraîné contre q ; ligne ajoutée ; défense finale = p sur G 9 × 9. Cohérent avec le texte (l. 291). Valeur du jeu restreint − V(B) = +0,015 / +0,025 au pilote (positif attendu, B itéré tronqué).
- **Attaquant (joue en dernier, convergé)** : SLSQP, 12 départs tirés plus un vers l'origine plus les attaques passées ; statut 0 dans 100 % des 52 218 départs du pilote, 83 itérations au plus pour une limite de 100 [M § 9]. Mon contrôle indépendant (§ 2.5) confirme.
- **Témoins** : C1 poids 1/9, C2 Dirichlet (graine dérivée, rôle 13), C3 « ou » déterministe, tous construits dans `defense_temoin` à partir de `etat_B["moniteurs"]`, les mêmes objets que ceux de B ; essai `test_reproductibilite_bit_a_bit_et_temoins` : 63 paramètres déployés pour B, C1, C2, C3, D, poids de C1 et de C2 vérifiés, C3 à poids [1,0]. Seuils recalibrés à α sur le même `Xcal` ; fausses alertes mesurées sur un `Xfpr` indépendant, moyennes par bras à 0,0003 de α au plus. Pas de fuite d'information : la standardisation de C3 n'emploie que le propre de calibration.
- **D** : maxout à t + 1 unités au tour t ; oracle approché (seuil gaussien, deux départs) : biais défavorable à D, déclaré ; il n'empêche pas D de battre B de 0,11 à 0,24, donc il ne peut pas fonder la réfutation.
- **Oracle « détection »** : gradients vérifiés (`test_gradients`, `check_grad`), départs déterministes, meilleur départ retenu, même oracle pour tous les bras.
- **Graines (R9)** : `SeedSequence(entropy=racine, spawn_key=…)` dans `gen`, garde numpy ≥ 1.25 ; clés par code de bras, tour, rôle ; la clé de rééchantillonnage `(code_delta, code_contraste, 0, 0, 99)` ne peut pas entrer en collision avec une clé de tâche (aucune tâche n'emploie le rôle 99) ; test d'indépendance à l'ordre des bras.
- **Racines refusées** : `exiger_racines_essai` (décision, brouillon 1, racine des tenues distincte) ; `gen` refuse RACINE et RACINE_TENUE sans autorisation posée par `autoriser_decision` ; `_travail` re-vérifie. Essais pour chaque motif.
- **Gardes (R5)** : j'ai recoupé le dictionnaire `MOTIFS` (52 entrées) avec le corps des essais nommés : chaque motif figure littéralement dans l'essai qui lui est attribué (49 dans le corps, 3 dans le décorateur `parametrize`). Les essais montrent en général un cas sain puis un artefact. Réserves : CM2-12.

### 2.3 Plan d'analyse et seuils S1 à S14

- **Cohérence texte / code** : `lire_tables` applique les lignes des Tables 1 à 4 telles qu'écrites (ordre, quantiles B2/B8/E8, « ≈ » après « B > X » et « X > B »). Exhaustivité testée sur 2 000 configurations. Pas d'écart trouvé.
- **S1 (0,02)** : principe 2 α, sans pilote. Règle « moyenne ≥ S1 et borne basse B2 > 0 » : puissance et tailles correctes en lecture, c'est une règle de pertinence et de significativité (nommée ainsi). Enjeu nul au vu du pilote (+0,13).
- **S5 (0,02 = S1)** : par principe ; lecture sans seuil recopiée. Acceptable. (Sa puissance sous écart nul est 0,49 : limite déclarée.)
- **S6 (ρ = 0,25)** : voir CM2-04, majeur.
- **S2, taille** : voir CM2-07.
- **S3, S4, S8, S9, S12, S14** : cohérents avec (M). S8 : 52,1 min de mur projeté pour 75 min de plafond.
- **S7 (λ = 8)** : log 9 / 8 ≈ 0,27 écart-type vérifié par l'essai du « ou » (`s ≤ 8 max z + log 3` pour trois moniteurs, borne analogue pour neuf).
- **S10** : voir CM2-08.
- **S11** : voir CM2-06.
- **S13** : principe d'abord, bien. Un fait en renforce la portée que le texte ne tire pas : sous l'oracle logistique, D vaut 0,45 / 0,26 contre 0,034 / 0,008 pour B [M § 11], donc « D > B » vaut **aux deux oracles** ; le choix de l'oracle décide si la plomberie est exercée, pas le verdict de HP. À écrire (CM2-02).
- **Erreurs de première espèce** : « HP confirmée » = intersection-union (taille ≤ celle du test le plus défavorable) ; « HP réfutée » = union protégée par Bonferroni. Logique correcte. Taille chiffrée à revoir (CM2-07).

### 2.4 R4 (symétrie), la réfutation à 1,000

- Faits : B − C3 < 0 et B − D < 0 dans **24 instances sur 24** aux deux δ (maxima par instance : −0,073 et −0,193 à δ 1,4 ; −0,052 et −0,064 à δ 1,8). Le pilote logistique donne le même signe (D 0,45 contre B 0,034). L'écart attaquant standard / attaquant renforcé est au plus 0,013 par tâche (C3) et ne change aucun contraste de plus de 0,002 [M § 9].
- Artefact d'attaquant : exclu à mon niveau (§ 2.5).
- Artefact de fausses alertes : exclu (moyennes à 0,0003 de α, écart entre bras par tâche 0,0014 à 0,0016). Le maximum observé est 0,0131 (C3, une tâche), assez pour déplacer V de quelques millièmes, pas de 0,08 à 0,24.
- Artefact de capacité ou d'information : pas d'information inégale. **La capacité est inégale en un sens que le texte appelle « égal »** : voir CM2-02. C'est la cause principale et elle est structurelle, pas un défaut de code.
- Ce que le texte ne fait pas : la symétrie R4 s'applique aux surprises, pas à un résultat prévu et propre. Voir CM2-05.

### 2.5 Attaquant indépendant (diagnostic, racine neuve 20269501 / 20269502, non opposable)

Défenses finales construites avec le code v2 (`Contexte`, `trajectoire`, `defense_temoin`) puis attaquées par : (0) l'attaquant du texte (standard) ; (1) un attaquant lourd (250 départs tirés, 21 départs structurés « composantes vers l'origine, écart-type 0,5 / 1 / 1,5 », attaques passées, 1 024 échantillons de Monte-Carlo, 300 itérations) ; (2) une stratégie d'évolution (1 + 12) sur le taux dur, depuis (1) et depuis (0), 1 500 générations. V évalué sur 19 998 échantillons frais. Trois tâches (instance 0 à δ 1,4 ; instances 0 et 1 à δ 1,8). Colonnes : standard / lourd / évolution depuis lourd / évolution depuis standard.

| Tâche | A | B | C1 | C3 | D |
|---|---|---|---|---|---|
| i0, δ 1,4 | .235 / .236 / .235 / .241 | .270 / .271 / .270 / .272 | .269 / .272 / .270 / .271 | .390 / .390 / .390 / .397 | .459 / .459 / .458 / .461 |
| i0, δ 1,8 | .114 / .117 / .117 / .117 | .160 / .161 / .159 / .163 | .164 / .166 / .164 / .167 | .234 / .234 / .234 / .238 | **.309 / .289** / .290 / .316 |
| i1, δ 1,8 | .0006 / .0004 / .0007 / .0007 | .098 / .101 / .100 / .101 | .118 / .120 / .120 / .122 | .182 / .185 / .191 / .192 | .230 / .236 / .236 / .243 |

Lecture : aucune méthode ne trouve une détection plus basse que le standard, sauf D (instance 0, δ 1,8 : −0,020 pour l'attaquant lourd) et B (−0,001 pour l'évolution). Le biais d'optimisation joue donc **en faveur de D** (V(D) légèrement surestimé), de 0,02 au plus sur trois tâches, contre un écart B − D de 0,11 à ce δ. Le contrôle « renforcé » du texte (même optimiseur, plus de départs) a un maximum de +0,011 pour D [M § 9] : cohérent. Dans la tâche i1, A est à 0,0006 à δ 1,8 : A au plancher (CM2-06).

## 3. Constats

Classement : bloquant 0, majeur 6, moyen 4, mineur 6.

### Majeurs

**CM2-01 — Un essai du code est rouge à la remise ; le test du refus de scellement dépend de l'état du dossier** (majeur)
- Où : `essais/test_arene_melange_v2.py` l. 308-316 (`test_decision_refusee_brouillon2_pour_la_bonne_raison`) ; prereg l. 16 (empreinte du fichier d'essais), l. 399 ; LISEZMOI (« 45 essais »).
- Constat : le test suppose que le brouillon 2 n'a pas de compagnon `.sha256` (« Le brouillon 2 n'a pas de compagnon », l. 309). Le compagnon existe (écrit à 09:52 UTC), le refus vient maintenant de « scellé mais non conforme : Seuil ; Contre-lecture » : 44 réussis, 1 échec. C'est exactement le défaut que CM-08 signalait en v1 (un essai qui ne teste plus ce que dit son nom parce que l'état du dossier a changé). Il échouera aussi après scellement. Le cas « compagnon absent, motif précis » est pourtant couvert correctement dans `test_prereg_scelle_refus_pour_la_bonne_raison`, sur des fichiers temporaires.
- Correction : bâtir ce test sur une copie temporaire du brouillon sans compagnon (ou le supprimer, le cas étant déjà couvert), ajouter un cas « copie du brouillon avec compagnon : refus par non-conformité (Seuil, Contre-lecture) » ; recalculer l'empreinte du fichier d'essais (l. 16) ; corriger « 45 essais ».

**CM2-02 — L'hypothèse principale est presque assurée d'échouer par construction ; « capacité égale » désigne un nombre de paramètres, pas une capacité** (majeur)
- Où : titre (l. 1) ; résumé 1 (l. 110) ; HP (l. 144) ; « Lecture anticipée » (l. 193) ; Plan 2 (l. 291-293) ; « n'autorise pas » (l. 123-132).
- Constat :
  1. B ne manie que des moniteurs **linéaires**, tirés **un seul à la fois** : à chaque requête il déploie 7 paramètres sur 63. C3 est le « ou » des neuf mêmes moniteurs (63 paramètres actifs à chaque décision), D un maxout à neuf unités. Pour des moniteurs fixes et une même fausse alerte α, la détection d'un mélange est une moyenne des détections de ses moniteurs, donc au plus la meilleure d'entre elles ; un « ou » dont le seuil par moniteur est resserré ne perd que si ce resserrement coûte plus que la moyenne. Avec des queues gaussiennes et des décalages de 2 à 4 écarts-types, il coûte peu (le texte le reconnaît l. 127). La victoire de C3 et de D est donc la conséquence attendue de la **classe de fonctions**, pas un test du **tirage au hasard**.
  2. Les données le montrent : B − C3 et B − D < 0 sur 24 instances sur 24 aux deux δ ; sous l'oracle logistique, tous les bras linéaires (A, B, C1, C2, C3) sont à 0,007-0,034 et D (maxout) à 0,45 / 0,26 [M § 11].
  3. La comparaison informative (« à classe de fonctions égale, le mélange d'équilibre bat-il le déterministe ? », par exemple un double oracle dont l'oracle rend des moniteurs maxout, contre un maxout unique de même total) n'est pas dans l'expérience. C'est une lacune de conception, que le texte ne nomme pas.
  4. L. 193 conclut que ce serait « un argument **contre** la piste 3 comme méthode propre dans ce monde » : trop fort. Ce qui serait établi : dans une arène gaussienne, avec une classe d'oracle linéaire, un « ou » déterministe des mêmes moniteurs et un maxout de mêmes paramètres font mieux qu'un mélange d'équilibre de ces moniteurs. Rien sur le mélange à classe de fonctions égale.
- Correction :
  - titre, résumé 1, l. 144 : « à nombre de paramètres égal » à la place de « à capacité égale », avec la phrase « B déploie 1/9 des paramètres à chaque requête, C3 et D les déploient tous » ;
  - supprimer ou reformuler l. 193 ; ajouter à « n'autorise pas » : « rien sur un mélange de moniteurs de même classe de fonctions que le témoin déterministe ; ce bras n'est pas dans l'expérience (lacune déclarée) » ;
  - écrire que HP est réfutée aux deux oracles (le pilote logistique donne D > B), donc que S13 ne décide pas de HP, seulement de la plomberie.

**CM2-03 — La portée pour le programme n'est pas écrite : l'arène ne reproduit pas la non-convergence de Bailey** (majeur)
- Où : « n'autorise pas » (l. 121-132) ; résumé 9 (l. 118) ; l. 193.
- Constat : le mélange d'équilibre est proposé comme réponse à une défense unique réentraînée qui ne converge pas. Dans l'arène, A est « plat » (détection par tour 0,061 → 0,056, [M § 9]) : l'attaquant gagne toujours contre le dernier moniteur, sans oscillation mesurée (aucune mesure d'un cycle n'est prévue : la mesure (i) est descriptive). B > A est donc la seule trace du mécanisme, et c'est la plomberie, pas la question. Une réfutation de HP ne peut pas dire que le mélange d'équilibre n'est pas la réponse à la non-convergence de Bailey, et le texte ne le dit pas assez nettement ; l. 193 le suggère.
- Correction : ajouter une rubrique « Portée d'une réfutation et d'une confirmation » : une réfutation établit un résultat négatif local (monde, classe d'oracle, δ, T) ; elle ne réfute ni la piste 3 ni l'usage du mélange sur de vrais moniteurs ; elle indique au mieux de tester un mélange de moniteurs plus riches. Ajouter « cette arène n'exhibe pas de cycle de la défense unique : la condition d'application de la piste 3 n'y est pas vérifiée ».

**CM2-04 — S6 : ρ recommandé après le pilote, avec la liste des classes selon ρ exposée à Lazar ; marge ancrée sur un contraste à A quasi nul** (majeur)
- Où : S6 (l. 238-241) ; Table 3 (l. 365-378) ; déclencheur 3 (l. 330) ; Table 1 ligne 1 (l. 344).
- Constat :
  1. Le texte déclare que la recommandation 0,25 est écrite après la lecture du pilote et que la grille l'a été avant : honnête. Mais S6 énumère ensuite, pour chaque ρ, la classe de C1 et C2 (« ρ = 0,10 → B > C1 et B > C2 probables ; 0,25 → ≈ pour C1 ; 0,50 → ≈ pour les deux »). C'est le défaut que CM-06 avait fait retirer pour S5 (« Lazar fixe en sachant la réponse »).
  2. ρ = 0,25 fixe la marge à 0,034 / 0,032 alors que l'effet pilote B − C1 est de 0,0246 / 0,0184 : « B > C1 » est impossible par construction, « HP confirmée » aussi (elle exige quatre « B > X »). La marge est donc une décision sur la confirmabilité de HP, prise avec le pilote sous les yeux.
  3. Une marge relative à B − A est instable : à δ 1,8, A est à 1,5 α (CM2-06), B − A = 0,128 mesure l'effondrement de A, pas un « gain du mécanisme ».
  4. La phrase « un témoin équivaut à B s'il garde au moins les trois quarts du gain » décrit une non-infériorité unilatérale ; la Table 3 teste une équivalence bilatérale ]−m ; +m[.
  5. La classe prédite pour C1 est « ≈ » (probabilité 0,88 / 1,000), ce qui déclenche **à coup sûr** la règle de Lazar (déclencheur 3) ; or la Table 1 ligne 1 rend « non concluant (audit en attente) » tant que l'audit n'est pas rendu : la lecture de la plomberie est subordonnée à un audit **prédit** (aggravé par CM2-10).
- Correction :
  - fixer la marge par un principe sans pilote (par exemple m = S1 = 0,02 pour les quatre témoins, ou ρ fixé avant lecture et motivé indépendamment) et retirer de S6 l'énumération « ρ → classes » ;
  - dire que C1 et C2 sont des questions qualifiantes dont la classe ne change pas la Table 4 par C3 et D, mais que « HP confirmée » est hors d'atteinte avec ce ρ ;
  - corriger la phrase de non-infériorité ou passer à une équivalence unilatérale cohérente ;
  - dissocier : un audit déclenché par la seule règle de Lazar (déclencheur 3) ne bloque pas la lecture de la Table 1.

**CM2-05 — R4 : l'audit ne se déclenche que sur surprise ; le résultat prévu et « trop propre » n'en déclenche aucun** (majeur)
- Où : déclencheurs 1 à 8 (l. 327-335) ; contenu de l'audit (l. 337) ; S10 (l. 258-261).
- Constat : R4 demande le même audit pour un résultat suspect de propreté « positif ou négatif ». Ici huit contrastes sont prédits à 1,000 et 24 instances sur 24 vont dans le sens prévu ; si la décision réplique, **aucun déclencheur ne tire**, sauf le déclencheur 3 (C1 ≈, prédit) dont le contenu de l'audit (rejeu de 10 tâches de RACINE_ESSAI avec un attaquant quatre fois plus fort) ne porte pas sur les tâches de la décision et ne vise pas C3 et D, les deux bras qui portent la réfutation. Le seul contrôle d'attaquant propre à ces deux bras est « V standard − V renforcé », même famille d'optimiseur. Mon contrôle indépendant (§ 2.5) n'a pas trouvé d'artefact, mais c'est précisément ce que l'audit du texte devrait établir sur les tâches de la décision.
- Correction : ajouter un déclencheur « résultat conforme à la prédiction avec P7 simulée = 1,000 et HP réfutée par C3 ou D » qui impose, après scellement et avant la phrase de synthèse, un contrôle d'attaquant indépendant (départs structurés, plus de départs, optimiseur sans gradient) sur au moins 10 tâches de la décision pour C3, D, B, avec critère d'artefact « un contraste B − C3 ou B − D change de signe ou de plus de 0,05 » ; préciser que l'audit tourne sur les tâches de la décision et non sur RACINE_ESSAI.

**CM2-06 — S11 : A est à 1,5 α au pilote à δ_haut = 1,8, contrairement à ce que dit le texte** (majeur)
- Où : S11 (l. 263-266, « aucun bras au plancher ») ; résumé 3 (l. 112) ; S10 (l. 260).
- Constat : la règle choisit le plus grand δ avec V(A) ≥ 3 α = 0,03. Au calibrage (12 instances), V(A, 1,8) = 0,034 (erreur-type 0,012) ; V(A, 1,6) = 0,0352 ; la suite n'est pas monotone et la règle prend le maximum : sélection par franchissement de seuil bruité. Au pilote frais (24 instances), V(A, 1,8) = 0,0154 (erreur-type 0,0045) et A est ≤ 0,03 dans **20 tâches sur 24**, ≤ 0,02 dans 19 ; dans mon diagnostic, A vaut 0,0006 dans une tâche. Le critère du texte (« A pas au plancher ») n'est donc pas tenu sur échantillon indépendant, et l'affirmation « aucun bras au plancher, contrairement à δ = 2,4 au brouillon 1 » est fausse pour A à δ_haut. C'est le défaut CM-04 de la v1, réduit mais présent. B, C1, C2, C3, D sont, eux, bien au-dessus du plancher à ce δ, et aucun verdict de HP n'en dépend.
- Correction : écrire que A est à 1,5 α au pilote à δ 1,8, que Table 1 à δ 1,8 mesure B contre un A presque nul et ne démontre pas un « gain d'équilibre » à ce budget, et que la marge de S6 en hérite (CM2-04). Ne pas changer δ (changement de conception après pilote) sauf décision explicite de Lazar ; sinon, option : recalibrer sur au moins 48 instances d'une racine neuve avant scellement.

### Moyens

**CM2-07 — Les tailles de la Table 3 sont mesurées avec des bornes de Student, la décision emploie des quantiles de rééchantillonnage** (moyen)
- Où : S2 (l. 221) ; résumé 6 (l. 115) ; (M) § 5 ; `calcul-puissance-arene-melange-v2.py` l. 74-80, 205-212.
- Constat : le texte annonce des tailles ≤ 0,007 (supériorité) et ≤ 0,013 (équivalence) et déclare « approximation de Student ». Mais les quantiles 0,3125 % et 99,6875 % d'un rééchantillonnage de 100 valeurs sont plus étroits qu'un intervalle de Student et plus variables. Contrôle (`taille_boot.py` : centrage du pilote, Δ = ±m, N = 100, 20 000 tirages, règle exacte de `analyser`, 150 répétitions par cellule, B − C1 et B − C2 aux deux δ) : P(« X > B » | Δ = −m) = 0,013 ; 0,020 ; 0,007 ; 0,000, soit 0,010 en moyenne contre 0,003 nominal et 0,002-0,007 pour Student ; P(« B > X » | Δ = +m) : 0 ; 0 ; 0 ; 0,007 ; P(« ≈ » | Δ = +m) : 0 ; 0,007 ; 0,007 ; 0. Bruit de simulation de l'ordre de ± 0,01 par cellule : indicatif, non concluant, mais la taille de la règle réelle n'est pas démontrée.
- Correction : mesurer les tailles avec le rééchantillonnage de la décision (au moins 1 000 répétitions par cellule) ou écrire « tailles sous bornes de Student ; la règle réelle n'est pas évaluée ». L'effet sur le verdict est nul (écarts de 0,08 à 0,24), mais S2 est un seuil affiché.

**CM2-08 — S10 ne peut quasiment jamais se déclencher** (moyen)
- Où : S10 (l. 258-261) ; déclencheur 2 (l. 329).
- Constat : la plage [minimum ; maximum] de 24 valeurs par tâche est comparée à la **moyenne de 100 tâches** : un écart-type de moyenne d'environ 0,005 contre une plage de ± 0,05 ; la moyenne ne sort de la plage que pour une anomalie grossière. C'est le défaut que CM-07 reprochait à « V(B) ≥ 0,99 » (déclencheur inatteignable), déplacé.
- Correction : bande fondée sur l'erreur-type de la moyenne de décision (moyenne du pilote ± 5 × écart-type par tâche / √N), par bras et par δ ; ou comparer la moyenne de décision à l'intervalle de rééchantillonnage du pilote élargi.

**CM2-09 — La décision réplique un pilote qui a déjà répondu ; l'audit prévu tourne sur la racine d'essai** (moyen)
- Où : en-tête de la section « Prédiction » (l. 153) ; S6, S10, S11 (valeurs tirées du pilote) ; l. 337.
- Constat : le pilote donne, sur 24 instances, les huit signes de HP avec des intervalles très étroits ; les seuils recommandés et les « prédictions » de la Table B sont tirés de lui. Le run de décision est une réplication (sur 200 tâches) dont la valeur d'information sur HP est faible ; cela n'invalide rien (R1 est respecté pour la racine de décision) mais le texte devrait le dire, car la phrase « Elles ne sont pas opposables » (l. 153) laisse croire que la décision peut encore surprendre. L'audit « rejeu de 10 tâches sur RACINE_ESSAI » (l. 337) ne dit rien sur la décision ; sur 10 tâches, le critère « un contraste change de plus de 0,01 » a un bruit comparable au critère lui-même pour B − C1.
- Correction : écrire « décision = réplication d'un pilote concluant ; les probabilités simulées sont conditionnelles à ce pilote » ; faire porter l'audit sur des tâches de la décision (CM2-05) ; relever le critère d'artefact au-dessus du bruit apparié à 10 tâches.

**CM2-10 — Une règle de Lazar prédite subordonne la plomberie à un audit** (moyen)
- Où : déclencheur 3 (l. 330) ; Table 1 ligne 1 (l. 344) ; l. 351.
- Constat : voir CM2-04 point 5. Sous la valeur recommandée de S6, la prédiction « C1 ≈ B » rend le déclencheur 3 presque certain ; la Table 1 ligne 1 impose « non concluant (audit en attente) » ; la Table 1 se lit avant toute autre. Le verdict sera donc « non concluant » jusqu'à l'audit dans le cas **prévu**.
- Correction : exempter explicitement le déclencheur 3 de la ligne 1 (l'audit de la règle de Lazar bloque la lecture de la Table 3 pour C1, pas celle de la Table 1), ou le retirer de la liste des déclencheurs bloquants.

### Mineurs

**CM2-11 — « Énoncé avant toute observation » inexact** (mineur) : l. 142. Le brouillon 1 a changé l'oracle **après** une observation sur une instance (archivée l. 314) ; le gel dit « avant toute observation de la v2 » (précision exacte). Écrire la même précision l. 142.

**CM2-12 — La couverture mécanique des gardes est déclarative ; la tolérance de fausses alertes est lâche** (mineur) : l. 395 (« vérifie mécaniquement ») : `test_chaque_garde_a_son_essai` prouve qu'une entrée de `MOTIFS` et un essai nommé existent pour chaque site, pas que l'essai nommé provoque le motif (j'ai vérifié séparément que c'est le cas, § 2.2). Reformuler. La garde `exiger_fpr` tolère |FPR − α| ≤ 0,005 (50 % de α) par défense ; la dérive est surveillée seulement sur la moyenne (déclencheur 8). Pas de garde propre aux écarts entre bras par tâche (maximum observé 0,0032). Acceptable, à déclarer.

**CM2-13 — Probabilités simulées et confiances conditionnelles au pilote** (mineur) : l. 172-187. Les classes de C1 et C2 sont à la frontière de la marge (0,0246 contre 0,034 ; 0,0367 contre 0,032) ; l'erreur d'estimation du pilote (erreur-type de 0,005 à 0,008) n'est pas propagée, et la marge elle-même dépend du pilote. « B ≳ C2 » à δ 1,8 (0,842) est une prédiction de pièce à pile ou face. Les confiances plafonnées à 0,95 couvrent HP, pas ces classes. Dire que les classes de C1 et C2 ne sont pas prédites avec confiance ; ne garder comme prédictions fermes que les signes et P4, P5, P7.

**CM2-14 — Arrêt par `timeout` et R10** (mineur) : S8 (l. 250), l. 311 et 420. `timeout` envoie un signal au processus lancé, pas aux processus de travail du pool `spawn` ; R10 demande des arrêts par PID ou identifiant. Prévoir la collecte des PID enfants et leur arrêt, et en faire une condition d'une « reprise complète » (pas de reprise tant qu'un orphelin tourne).

**CM2-15 — Attaquant moins fort sur D que sur les autres bras** (mineur) : § 2.5. Le biais d'optimisation joue en faveur de D (jusqu'à 0,02 sur une tâche), par construction du paysage (somme de neuf sigmoïdes d'un maxout). Sans effet sur les signes. À déclarer à côté de CM-16, avec le contrôle indépendant de CM2-05.

**CM2-16 — Trois commits différents cités, mesures non rattachées à un commit du code** (mineur) : l. 7 (`c7f5d3aa`), journal (`a01c9287`), (M) (`c187a609`). Le code remis n'est pas committé par l'auteur : le champ `commit` des manifestes de pilote désigne un arbre sans le code. Sans conséquence pour la décision (arbre propre exigé), à clarifier au gel.

### Positif

**CM2-17** : essais 44/45 puis 25/25 ; puissance rejouée à l'identique ; programme linéaire validé sur 300 matrices ; attaquant confirmé par trois méthodes indépendantes (§ 2.5) ; transcription des chiffres sans écart ; aucune fuite de la racine de décision (racines des fichiers, garde dans `gen`) ; déclaration honnête des prédictions réfutées (B ≈ C1, L1) ; ordre des étapes cohérent avec les `mtime`.

## 4. R3 et symétrie

- **R3** : tenu. Les prédictions écrites sont négatives (réfutation de HP) ; aucun run ne vise un signe positif. Réserve : le choix de ρ après le pilote (CM2-04) est une marge de manœuvre d'analyse ; elle va dans le sens défavorable à la piste (« ≈ » à la place de « B > C1 »), donc ce n'est pas une visée positive, mais c'est une décision prise en connaissant la réponse.
- **R4** : voir CM2-05, CM2-08, CM2-10.

## 5. Portée : ce que vaut une réfutation ici

Ce que le préenregistrement peut revendiquer, si les corrections sont faites :
- dans une arène gaussienne de dimension 6 à trois composantes, avec des moniteurs linéaires entraînés pour maximiser la détection à α = 0,01 (oracle « détection »), à deux budgets (1,4 ; 1,8), huit tours : le double oracle tronqué B bat la défense unique réentraînée A (plomberie, au budget haut contre un A déjà à 1,5 α) ; ses poids d'équilibre battent des poids uniformes ou aléatoires d'environ 0,02 à 0,04 (qualifiant) ; un « ou » déterministe des mêmes moniteurs et un maxout de mêmes paramètres font nettement mieux (0,08 à 0,24), sans artefact d'attaquant détecté ;
- ce résultat est négatif **pour cette classe de mélange**, avec cette classe d'oracle, dans ce monde favorable au « ou ».

Ce qu'il ne peut pas revendiquer :
- que le mélange d'équilibre n'est pas une réponse à la non-convergence de Bailey (cette non-convergence n'est pas exhibée, CM2-03) ;
- que le mélange est inutile à classe de fonctions égale (bras absent, CM2-02) ;
- quoi que ce soit sur de vrais moniteurs (queues lourdes, dizaines de sondes, attaquants en boîte noire) ;
- que la réfutation est robuste à d'autres budgets que les deux choisis sur A seul, dont un presque au plancher de A (CM2-06).

La phrase honnête pour Lazar : « dans cette arène, le gain qu'un mélange d'équilibre de moniteurs linéaires apporte sur une défense unique est dépassé par ce qu'apporte le simple fait d'agréger les mêmes moniteurs de manière déterministe ; on ne sait pas encore si le tirage au hasard apporte quelque chose à classe de fonctions égale. »

## 6. Corrections demandées, dans l'ordre

Avant présentation à Lazar :
1. CM2-02, CM2-03 : titre, résumé, l. 144, l. 193, rubrique de portée.
2. CM2-04, CM2-10 : S6 sans énumération des classes par ρ, marge par principe ou ρ fixé indépendamment, déclencheur 3 sorti de la ligne 1.
3. CM2-06 : corriger S11 (A à 1,5 α), déclarer ; décision de Lazar sur un éventuel recalibrage.
4. CM2-05, CM2-08, CM2-09 : audit sur les tâches de la décision, déclencheur « résultat conforme et propre », S10 par erreur-type.
5. CM2-07 : mesurer ou déclarer les tailles de la règle réelle.

Avant scellement :
6. CM2-01 : test à réécrire, empreinte l. 16, « 45 essais ».
7. CM2-11 à CM2-16 : mineurs.
8. Remplir S1 à S14 (gel de Lazar), la section « Contre-lecture » (entrée 2 avec les deux empreintes : brouillon relu `622e50d2…` et le présent rapport), le commit (l. 7), régénérer le bloc d'identité si une valeur de configuration change.

## 7. Limites de cette contre-lecture

- Je n'ai pas relu les antériorités (toutes « SUPPOSÉ ») ni utilisé de réseau.
- Mes attaquants indépendants portent sur trois tâches d'une racine neuve : ils n'établissent pas un niveau, ils cherchent un artefact ; le résultat « aucun artefact » ne vaut que dans l'ordre de grandeur (0,003, 0,02 pour D).
- La mesure de taille bootstrap (150 répétitions par cellule) est bruitée (± 0,01) ; elle montre que la taille réelle n'est pas démontrée, pas qu'elle est mauvaise.
- L'argument de CM2-02 (le « ou » domine la moyenne pour des moniteurs fixes en queues gaussiennes) est un raisonnement, étayé par l'accord des signes sur 24 instances et par le pilote logistique ; je n'ai pas fait tourner le bras « mélange de maxout » qui le testerait.
- Je n'ai lu de `controle_ia` que `prereg.py` et l'usage de `gardes.py`, `scellement.py`, `manifeste.py` par le code.
- Le brouillon n'est pas scellé et ne doit pas l'être avant le traitement de chaque remarque (accepté, refusé et pourquoi) dans l'entrée « Contre-lecture 2 ».
