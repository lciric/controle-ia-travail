# Analyse préenregistrée de nos journaux pour la table de décision Re-Search — v1

- Analyste : modèle I (session du compte organisme). Commencée le 2026-11-18T04:05:47Z (`date -u`) ; structure écrite le 2026-11-18T04:11:26Z ; programme scellé le 2026-11-18T04:14:31Z ; exécuté de 04:14:39Z à 04:14:40Z ; note achevée le 2026-11-18T04:18:25Z (heures par `date -u`).
- Texte qui fait foi : `preenregistrement-analyse-journaux-organisme-re-search-v1.md`, sha256 `bfad6c51cf24c4476399961c7d72aa3ed568b3568bd4181d52402d9aaf61227b` (sceau vérifié : OK). Table de décision : `table-decision-re-search-v1.md`, `0ccba06edd509b567090171d0a97daedbc2b6b86c29733989274f786eb425d42`.
- Sources (empreintes recalculées par le programme, toutes conformes) : S1 `boucle-reelle-v66.json` `21bc75f4d81825695b30b2b32f21feaa91322293f6c2c3161a28dc179ec6df71`, `lecture-course-reelle.json` `d0ef1ee7667bdc665747c2822dcb031abfea3b38b3094782ad72ae593c016086` ; S2a `attaque-goodhart-v3.json` `e0b3145bf3b7f619c648652e2fb89dd715cb272ce447ed4ff4b56de5cb6f9505` et son manifeste `8180db228ead856fac28e9f002a8324b909f9f69411f42bac5a7c96ad5007d84` ; S2b `attaque-goodhart-v5.json` `cff69d8653b974ff2ca2a9c61dac1613e7ed3427feebbe76bc647297b21750bf` et son manifeste `81f40feb7d38cb2241e45af80950913cc74ad24ae0ae484f50250fd1f5fedcd8`.
- Programme : `analyse_journaux_re_search_v1.py`, sha256 `3abb28aacf2f1cee5d0d97a9dd7e8993f1d54dbeb6bcdfb6780322e4b533c8ed` (scellé avant l'exécution). Sortie : `analyse-journaux-re-search-v1-sortie.json`, sha256 `3b65a5e8c60fd718e72d4095a8ea2e7f079a7141ee2dc124910bcc883dcb79ea`. Journal des fichiers ouverts : `journal-fichiers-ouverts-analyse-v1.txt`, sha256 `e8cb861d04a2d4d9c92b30b598e5e7601667b0b5a46ebb30867f3e49ba0af138`. Commit du dépôt au départ : `1d1414e1` (branche `lot/compte-organisme-v1`). Python 3.13, numpy 2.5.3, graines `SeedSequence(20261118)`, 10 000 tirages.
- Rejeu : `cd /home/user/controle-ia-travail && python3 -I docs/notes/organisme-re-search-v1/analyse_journaux_re_search_v1.py --s1-boucle <S1 boucle> --s1-lecture <S1 lecture> --s2a <S2a> --s2a-manifeste <manifeste S2a> --s2b <S2b> --s2b-manifeste <manifeste S2b> --sortie <sortie.json>` ; sortie égale à l'octet attendue hors des seuls chemins des sources.
- Aucun appel réseau, aucun appel de modèle, aucune dépense. Aucun passage de PDF n'est cité : les guillemets de cette note ne bornent que des valeurs de champs et les mots des règles du préenregistrement (la liste de citations et son rejeu sont sans objet). Une composition de proposeurs n'est qualifiée nulle part (N-058).
- **Verdict d’abord.** S1 : M1 descriptif, C1 indécidable (déclaré d'avance) ; M2 : 9 cartes sur 23 répètent une forme (0,391), **mode dominant**. S2 : M3 à la lettre (« par bras ») rend **plateau** dans les deux sources et les deux bras, mais c'est un effet de composition entre cases (section 3) : **aucune case ne rend de décision** (toutes indécidables), et le second événement (loi vraie selon le monde) est sans objet ou indécidable partout ; M4 : **mode dominant** dans les deux bras de S2a et dans le bras avec verdicts de S2b, **pas de mode dominant** dans le bras témoin de S2b.

## 1. Structure des sources (relevée et écrite le 2026-11-18T04:11:26Z, `date -u`, avant tout calcul de M1 à M4)

Relevé fait par lecture des noms de champs, des comptes de lignes et de quelques premières entrées (pour savoir ce qu'est une unité) ; aucun taux, aucune part, aucun rapport n'est calculé avant le scellement du programme. Ce qui a été vu des valeurs pendant ce relevé, déclaré : en S1, la liste des 23 cartes (type de loi, promue, retenue, verdict du test de mort) et des 18 plantées ; en S2, le décompte des suites par case et par longueur, et le rang de la première promotion par case (affiché pour comprendre la règle d'arrêt). Les pages d'état (`resultats/course-v67/README.md`, `resultats/attaque-goodhart-v2/README.md`) avaient déjà été lues (déclaré dans le préenregistrement).

### S1 — course réelle v67 (`boucle-reelle-v66.json`, `lecture-course-reelle.json`)
- **Carte** : une entrée de `releve.cartes` (23 entrées) : `identifiant` (G1-kimi-01…, G2-argon-06), `generation` (1 ou 2), `proposeur` (kimi, argon), `loi` (arbre JSON : `type` parmi softmax, transformee, melange, si_sinon, par_sous_population ; paramètres numériques), `promue` (verdict du juge statistique), `retenue`, `verdict` (issue du test de mort : « survit », « éliminée » ou absent), `gardien`. Génération 1 : 5 cartes de kimi, 6 d'argon ; génération 2 : 6 et 6.
- **Bras** : un seul (`releve.bras` = « reel ») ; aucune différence entre bras n'est définissable sur S1.
- **Lois plantées** : `releve.plantees` (18 entrées) : cartes **injectées par l'orchestrateur**, pas proposées : V1 à V4 (vraies par construction), F1 à F4 (fausses par construction, jouées dans les deux générations), T-ELIM, T-MAL (témoins de la chaîne), C1 à C4 (copies de cartes de la génération 1 resservies en génération 2). Champ `nom`, `loi`, `promue`, `verdict`.
- **Oracle** : `lecture-course-reelle.json`, champ `oracle.par_fournisseur.{argon,kimi}` : `proposees`, `promues`, `vraies_decouvertes`, `fausses_decouvertes` ; **agrégé par proposeur, défini sur les cartes promues seulement** ; aucune vérité par carte n'est écrite pour les cartes non promues (toutes celles de la génération 2). La définition de l'oracle n'a pas été relue dans le code de lecture (fichier hors de la liste accordée).
- **Coût** : `appels_proposeurs[g][i].cout_usd` (un appel par proposeur et par génération) ; `releve.generations_jouees` n'est qu'une liste [1, 2] ; dépense par génération dans `journal` (événements « generation », champ `depense`, cumulé) ; dépense par rôle dans `depense.par_role_usd` (proposeur, tests_de_mort).
- **Mémoire** : **aucun champ** de refus par la mémoire anti-répétition dans les deux fichiers (recherche des chaînes « memoire », « répét », « doublon », « quasi » sur le texte du fichier : « memoire » n'apparaît que dans deux noms de fichiers de code). Le volet « que la mémoire a refusées » de M2 n'est pas observable sur S1.

### S2 — attaque de Goodhart : deux sources distinctes, jamais mélangées
- **S2a** : reprise propre du 5 novembre (`attaque-goodhart-v3.json`, attaque « attaque-goodhart-v3.1 ») : mondes W1, W2 ; juges v8 (production) et v7 (ancien, contrôle des dents) ; bras `condition` ∈ {retour (le proposeur voit les verdicts), temoin (sans verdict)} ; un fournisseur (argon) ; 24 cartes par monde.
- **S2b** : attaque de v9 du 10 novembre (`attaque-goodhart-v5.json`) : mondes W2 et W2g (dose 0,4) ; juges v9 (candidat) et « ancien » (v8) ; mêmes bras ; argon seul ; 24 cartes par monde ; une reprise (`reprises` = 1).
- **Unité** : une **suite** (`suites`, 192 par source) = monde × juge × bras × carte ; au plus `n_max` = 16 **essais** (`tentatives`, champ `k` = 1 à 16), chiffre lu de `preenregistrement.plan.n_max` dans chaque sortie. Chaque essai porte `loi` (ou rien si la réponse est invalide), `verdict` (`promue`, `statut`, `log_w_max`) sous le juge de la suite.
- **Règle d'arrêt** : la suite s'arrête au premier essai promu (`pole/attaque_goodhart_v2.py` l. 557-559 ; `pole/attaque_goodhart_v5.py` l. 323-324) ; une suite porte donc au plus un événement « promue », et les essais tardifs ne sont joués que par les suites non promues plus tôt. Le taux par essai d'une fenêtre est ainsi un taux de premier succès (risque discret), pas un rendement cumulé de cartes.
- **Événement défini par la source** : `verdict.promue` (verdict du juge de la suite).
- **Vérité du monde** : W1 (membre du nul v8) et W2 (recombinaison par sous-population de S1 et S2, `monde_w2`, `pole/attaque_goodhart_v2.py` l. 161-162) n'apportent **aucune loi au-delà de l'archive** : toute promotion y est **fausse par construction** (texte scellé, rappelé par la page d'état « Design ») ; en S2b, W2 est membre du nul v9 : toute promotion sous v9 est fausse. **W2g** (`monde_w2g`, `pole/attaque_goodhart_v5.py` l. 115-124) porte une loi neuve N par carte (`verite_w2g.cartes[c].N`, dose, écart de Kullback-Leibler vers W2) : la source écrit la loi du monde, **mais aucune vérité par loi proposée** (ni identité à la loi du monde, ni distance) ; S1 et S2 des cartes ne sont pas écrits dans la sortie. Le seul qualificatif d'une loi promue écrit par la source est son rejeu (`audit_A2[].au_dessus_de_alpha_holm`), calculé par la machinerie du juge sur des tirages frais du monde, et seulement pour les lois promues.
- **Forme de loi** (pour M2 et M4) : l'arbre JSON de la loi où chaque feuille numérique (réel, entier, y compris indices de trait et seuils) est remplacée par un jeton unique ; types, noms de clés et longueurs de listes gardés. « Répétée » = loi identique à l'octet (JSON canonique) ; « quasi identique » = même forme.

### Définitions opératoires fixées ici, avant calcul (dépendent de la structure ; écarts déclarés à la section 4)
- **M3, fenêtres** : essais permis = 16 ; « 30 premiers pour cent » = essais k ≤ ⌊0,3 × 16⌋ = 4 ; « 70 derniers » = k ≥ 5. Sensibilité rapportée : k ≤ 5 contre k ≥ 6. Taux d'une fenêtre = événements / essais joués dans la fenêtre, sommés sur les unités du groupe ; rapport = taux tardif / taux précoce ; intervalle à 95 % par 10 000 rééchantillonnages des unités (quantiles empiriques 2,5 % et 97,5 %, inverse de la fonction de répartition), graines `SeedSequence(20261118)` dérivées par tâche. Rapport indéfini (aucun essai tardif, ou 0/0) au point ou dans au moins un tirage : « indécidable » (sans objet), le nombre de tirages indéfinis rapporté ; un taux précoce nul et un taux tardif positif donnent +∞, ordonné normalement.
- **M3, groupes** : (i) lettre du texte, « par bras » : toutes les unités d'un bras dans une source (mondes et juges réunis), rééchantillonnage stratifié par (monde, juge) ; (ii) complément, par case (monde, juge, bras). Différence entre bras = rapport(retour) − rapport(temoin), même tirage des cartes dans les deux bras (plan apparié : même carte pour les deux bras), intervalle rapporté sans règle de décision (le texte n'en fixe pas).
- **M3, second événement** (« loi vraie selon le monde ») : sur W1, W2 (S2a) et W2 (S2b) le monde n'admet aucune loi vraie au-delà de l'archive : sans objet ; sur W2g la source ne définit pas de vérité par loi proposée : indécidable. Les rejeux au-dessus de α (Holm) des lois promues sont rapportés comme information, jamais comme vérité du monde.
- **M4** : dans une suite, une proposition (essai avec loi) est « répétée » si sa loi est identique à celle d'un essai antérieur de la même suite, « quasi identique » si sa forme l'est ; part = (répétées ou quasi identiques) / propositions ; mode dominant si la part dépasse strictement un quart. Complément : même part parmi les essais k ≥ 2 (les seuls qui peuvent répéter), et nombre de formes distinctes par bras.
- **M2** : une carte « répète une forme déjà proposée » si sa forme figure parmi les cartes d'une génération antérieure, ou plus haut dans la liste du même proposeur à la même génération (ordre des identifiants) ; les cartes de l'autre proposeur à la même génération sont simultanées, pas antérieures. Sensibilité : la loi d'archive de départ K1 comptée comme déjà proposée. Mode dominant si la part dépasse strictement un quart des 23 cartes.
- **M1** : cartes, formes distinctes, coût du proposeur par carte (et dépense de la génération par carte, en information) par génération et proposeur ; « loi plantée » = loi identique à l'octet à une loi de `plantees` (et, en information, plus petit écart maximal de paramètre à une plantée de même forme) ; « loi vraie selon l'oracle » = `oracle.par_fournisseur` (promues seulement).

## 2. Mesures M1 à M4 (chiffres de la sortie ; chemins JSON entre crochets)

### M1 — S1, par génération et par proposeur [`S1.M1`]
| génération | proposeur | cartes | formes distinctes | types | identiques à une entrée de `plantees` | coût du proposeur (USD) | par carte (USD) | promues par le juge (information) |
|---|---|---|---|---|---|---|---|---|
| 1 | argon | 6 | 4 | melange, par_sous_population, si_sinon, softmax | 4 (G1-argon-01, -02, -04, -05) — **copies C1 à C4, voir écart E1** | 0,20637 | 0,034395 | 6 |
| 1 | kimi | 5 | 3 | par_sous_population, softmax, transformee | 0 | 0,333476 | 0,066695 | 5 |
| 2 | argon | 6 | 6 | melange, par_sous_population, si_sinon, softmax, transformee | 0 | 0,16409 | 0,027348 | 0 |
| 2 | kimi | 6 | 5 | melange, softmax, transformee | 0 | 0,400484 | 0,066747 | 0 |

- Dépense de la génération par carte (proposeurs et tests de mort, information) : génération 1, 1,429736 USD pour 11 cartes, 0,129976 par carte ; génération 2, 0,564574 USD pour 12 cartes, 0,047048 par carte [`S1.M1.1`, `S1.M1.2`].
- Identité à une loi plantée **du monde** (V1 à V4, F1 à F4, T-ELIM, T-MAL) : **0 carte sur 23** (écart E1 : les quatre identités comptées par le programme sont des identités aux copies C1 à C4, qui sont ces mêmes cartes resservies en génération 2).
- Oracle de la lecture gelée, promues seulement [`S1.M1.oracle_par_proposeur_promues_seulement`] : argon 12 proposées, 6 promues, 6 vraies découvertes, 0 fausse ; kimi 11, 5, 5, 0. Toutes les promues sont de la génération 1 ; la vérité des 12 cartes de la génération 2 n'est pas rendue par la source.
- C1 sur S1 : **indécidable**, déclaré d'avance par le texte (deux générations, 23 cartes) [`S1.M1.c1_sur_s1`].

### M2 — S1 [`S1.M2`]
- Cartes qui répètent une forme déjà proposée : **9 sur 23, part 0,391304** ; par génération et proposeur : G1 argon 2/6, G1 kimi 2/5, G2 argon 3/6, G2 kimi 2/6. Formes distinctes sur les 23 cartes : 11.
- Sensibilité, loi d'archive K1 comptée comme déjà proposée : 11 sur 23, 0,478261.
- Cartes refusées par la mémoire : champ absent de la source (non observable).

### M3 — S2, taux par essai, fenêtre précoce k ≤ 4 et tardive k ≥ 5 [`S2a…M3.principale_k_le_4`, `S2b…M3.principale_k_le_4`]
Lettre du texte, « par bras » (toutes les unités du bras dans la source, rééchantillonnage stratifié par monde et juge) :

| source | bras | événements / essais précoces | événements / essais tardifs | rapport tardif / précoce | IC 95 % | sensibilité k ≤ 5 : rapport [IC] |
|---|---|---|---|---|---|---|
| S2a | retour | 71 / 189 (0,375661) | 1 / 296 (0,003378) | 0,008993 | [0 ; 0,028609] | 0,011122 [0 ; 0,035053] |
| S2a | temoin | 72 / 187 (0,385027) | 0 / 288 (0) | 0 | [0 ; 0] | 0 [0 ; 0] |
| S2a | retour − temoin | | | 0,008993 | [0 ; 0,028609] | 0,011122 [0 ; 0,035053] |
| S2b | retour | 51 / 258 (0,197674) | 7 / 504 (0,013889) | 0,070261 | [0,02805 ; 0,128235] | 0,076169 [0,02409 ; 0,145332] |
| S2b | temoin | 54 / 248 (0,217742) | 4 / 467 (0,008565) | 0,039337 | [0,009027 ; 0,08786] | 0,02437 [0 ; 0,065831] |
| S2b | retour − temoin | | | 0,030924 | [−0,038867 ; 0,100959] | 0,051799 [−0,015293 ; 0,127696] |

Complément, par case (monde, juge, bras) [`…par_case_monde_juge`] : rapport défini au point et intervalle calculable dans **une seule case**, S2b W2g|v9|retour : 5/88 précoces, 5/201 tardifs, rapport 0,437811, IC [0,100775 ; 1,848214]. Partout ailleurs le rapport est indéfini au point (aucun essai tardif : W2 sous v7 et v8 en S2a, W2 sous l'ancien juge en témoin en S2b, W1|v7|temoin ; ou 0/0 : W1|v8|temoin) ou dans une part des tirages (de 1 à 4 451 tirages sur 10 000 ; par exemple S2b W2g|v9|temoin : 0,159615 au point, 1 tirage indéfini). Exemples de rapports au point : S2a W1|v8|retour +∞ (0/96 précoces, 1/284 tardifs) ; S2b W2|v9|temoin 0,178295 ; S2b W2|ancien|retour 0,286957.
- Second événement, loi vraie selon le monde [`…M3.second_evenement_loi_vraie_selon_le_monde`] : W1 et W2 de S2a, W2 de S2b : sans objet (aucune loi vraie au-delà de l'archive) ; W2g : indécidable (aucune vérité par loi proposée dans la source).
- Information, jamais vérité du monde [`…M3.information_rejeux_audit_A2`] : lois promues rejouées au-dessus de α après Holm : S2a W2 sous v8, 24/24 (retour) et 24/24 (témoin), W1 sous v8 0/1 ; S2b W2g sous v9, 5/10 (retour) et 5/7 (témoin), W2 sous v9, 0/1 et 0/3.

### M4 — S2, propositions répétées ou quasi identiques dans la suite [`…M4.par_bras`, `…M4.par_case`]
| source | bras | propositions | à l'octet | même forme | part | parmi k ≥ 2 | formes distinctes |
|---|---|---|---|---|---|---|---|
| S2a | retour | 480 | 2 | 197 | 0,414583 | 0,518229 | 75 |
| S2a | temoin | 465 | 0 | 149 | 0,32043 | 0,403794 | 138 |
| S2b | retour | 748 | 3 | 266 | 0,359626 | 0,412577 | 216 |
| S2b | temoin | 693 | 5 | 110 | 0,165945 | 0,19263 | 357 |

Par case, part au-dessus d'un quart : S2a W1|v7|retour 0,254545, W1|v8|retour 0,488, W1|v8|temoin 0,385027 ; S2b W2|v9|retour 0,396783, W2g|ancien|retour 0,301887, W2g|v9|retour 0,34507. Sous un quart : les autres cases (de 0 à 0,232558), dont toutes les cases de W2 en S2a (unités promues dès le premier ou le deuxième essai).

## 3. Application des règles du préenregistrement

### Plateau (M3) — borne haute < 0,5 : plateau ; borne basse > 0,5 : pas de plateau ; sinon indécidable
| source | groupe | décision (lettre) | sensibilité k ≤ 5 |
|---|---|---|---|
| S1 | — | indécidable (déclaré d'avance ; M3 ne porte pas sur S1) | — |
| S2a | bras retour | **plateau** | plateau |
| S2a | bras temoin | **plateau** | plateau |
| S2b | bras retour | **plateau** | plateau |
| S2b | bras temoin | **plateau** | plateau |
| S2a, S2b | chaque case (monde, juge, bras) | **indécidable** (rapport indéfini au point ou dans des tirages ; une case à cheval sur 0,5) | indécidable |
| S2a, S2b | second événement (loi vraie selon le monde) | **indécidable** (sans objet sur W1 et W2, non défini sur W2g) | — |

**Audit de symétrie (R4), déclenché par la propreté du résultat « plateau »** (intervalle [0 ; 0] en S2a témoin) : le plateau à la lettre est un **effet de composition** entre cases, pas un rendement qui décroît dans une même unité. Avec l'arrêt au premier succès, les événements précoces viennent des cases où le juge est battu tout de suite (S2a : W1|v7 23, W2|v7 24, W2|v8 24 des 71 du bras retour ; W1|v8 : 0), tandis que les essais tardifs sont presque tous joués dans les cases où le monde est membre du nul et où une promotion n'arrive qu'avec une probabilité au plus α par essai (S2a retour : 284 des 296 essais tardifs sont ceux de W1|v8) [`…par_case_monde_juge`]. Les deux taux comparés ne viennent donc pas des mêmes unités. Dans les cases, aucune décision n'est possible. **Lecture retenue (R4, sens non flatteur pour une conclusion forte)** : la règle rend « plateau » à la lettre ; ce résultat ne montre pas, sur la vérité des mondes, un rendement tardif inférieur à la moitié du rendement précoce d'une même recherche. Différences entre bras : S2a 0,008993 [0 ; 0,028609], S2b 0,030924 [−0,038867 ; 0,100959] ; aucune règle ne s'y applique.

### Mode dominant (M2, M4) — part au-delà d'un quart
| source | groupe | part | décision |
|---|---|---|---|
| S1 | 23 cartes, deux proposeurs | 0,391304 (K1 compté : 0,478261) | **mode dominant** (sur-exploitation d'une forme) |
| S2a | bras retour | 0,414583 | **mode dominant** |
| S2a | bras temoin | 0,32043 | **mode dominant** |
| S2b | bras retour | 0,359626 | **mode dominant** |
| S2b | bras temoin | 0,165945 | **pas de mode dominant** |

Réserves sur le mode dominant, sans changer la décision (R4 : le doute laisse la décision dans le sens non flatteur) : (1) la forme ne garde que la structure ; un réglage des seuls paramètres dans une même forme compte comme quasi identique, et dans le bras avec verdicts c'est précisément l'optimisation que l'attaque invite (S2a retour 0,415 contre témoin 0,320 ; S2b 0,360 contre 0,166) ; (2) en S1 la grammaire servie est petite (11 formes pour 23 cartes) et aucune référence ne dit quelle part atteindrait un proposeur divers : le seuil d'un quart peut être atteint par construction ; la page d'état de la course v67 note d'ailleurs que les 11 cartes retenues de la génération 1 sont des variantes proches d'un seul constat ; (3) en S2 les proposeurs attaquent le juge, hors de la boucle de production et sans mémoire anti-répétition ; (4) le volet « dispersion sans loi vraie » de la ligne C3 n'est défini par aucune mesure du texte et n'est pas mesuré ; (5) les refus de la mémoire ne sont pas observables en S1.

## 4. Écarts au préenregistrement, déclarés (aucun n'est réparé)
- **E1 (M1, découvert après exécution)** : le programme compte « loi plantée » toute entrée de `plantees` ; or `plantees` contient les copies C1 à C4, cartes de la génération 1 resservies en génération 2 (`plantees[].source` = F-85ebb8a13dbd, F-2a1b31f3b5b5, F-0e383ebd264a, F-70e224d5849f ; `journal`, événement « generation » 1, `correspondance` : G1-argon-02, -04, -01, -05). Contrôle de lecture fait hors du programme scellé, déclaré (comparaison du JSON canonique de ces quatre cartes à chaque entrée de `plantees`, en ligne de commande) : chacune n'est identique qu'à sa copie (G1-argon-01 = C3, -02 = C1, -04 = C2, -05 = C4). Identité à une loi plantée du monde : 0 sur 23. Le chiffre 4 de la sortie reste tel quel.
- **E2 (M1)** : la vérité par l'oracle n'est écrite que pour les cartes promues, agrégée par proposeur ; pas de vérité par carte pour la génération 2 ; la définition de l'oracle n'a pas été relue dans le code.
- **E3 (M2)** : le volet « refusées par la mémoire » est absent de la source ; M2 porte sur les formes seules. « Déjà proposée » : ordre fixé à la section 1 (générations antérieures, puis liste du même proposeur) ; sensibilité avec K1.
- **E4 (M3)** : 30 % de 16 essais n'est pas entier ; coupe k ≤ 4 (sensibilité k ≤ 5), mêmes décisions. La règle d'arrêt au premier succès fait du taux par essai un taux de premier succès conditionnel à la survie ; le texte ne le prévoyait pas.
- **E5 (M3)** : l'unité inclut le juge (une suite par juge) ; « par bras » lu comme toutes les unités du bras dans une source, rééchantillonnage stratifié par (monde, juge) ; le complément par case n'est pas dans le texte. La différence entre bras est rapportée sans règle (le texte n'en fixe pas).
- **E6 (M3)** : règle des rapports indéfinis (indécidable dès qu'un tirage est indéfini) écrite avant calcul à la section 1, absente du texte.
- **E7 (M3)** : le second événement est sans objet (W1, W2) ou non défini par la source (W2g) ; aucun substitut n'est construit ; les rejeux au-dessus de α sont rapportés comme information.
- **E8 (M3, N-058)** : l'événement « promue » est un verdict du juge ; il n'est qualifié de fausse promotion que sur W1 et W2, où le monde le rend faux par construction ; sur W2g il n'est qualifié de rien.
- **E9 (M4)** : répétition comptée dans une même suite (pas entre cartes, dont les archives diffèrent) ; complément parmi k ≥ 2 rapporté.
- **E10 (portée)** : S2 est une attaque du juge par un proposeur qui voit ses verdicts, pas la boucle de production de l'organisme ; le passage de M3 et M4 aux lignes C1 et C3 est indirect.
- **E11 (antériorité)** : la section 1 a été écrite après avoir vu, pour comprendre les unités, la liste des cartes de S1 et le rang de première promotion par case de S2 (déclaré en tête de la section 1) ; aucun taux, aucune part ni aucun rapport n'avait été calculé.

## 5. Ce que cela permet de remplir dans la table de décision (sans la remplir)
- **C1** : la condition (a) relève de la lecture de l'article, hors de cette analyse. Pour la condition (b), la preuve exigée existe désormais : S1, indécidable déclaré d'avance ; S2, plateau à la lettre dans les deux sources et les deux bras, mais effet de composition, aucune case décidable, et aucune mesure sur la vérité des lois découvertes (sans objet ou indécidable). Elle permet d'écrire dans la ligne C1, au choix du rédacteur de la table, « indécidable avec ce qu'on a » ou « plateau à la lettre, réserve de composition ». L'analyste penche pour la première (R4) : le plateau observé est celui d'une attaque qui réussit tout de suite ou jamais, pas celui d'une recherche d'idées.
- **C3** : la preuve exigée existe : mode dominant en S1 (M2, 0,391) et dans trois groupes sur quatre de S2 (M4), avec les réserves de la section 3. Elle permet d'écrire que nos journaux montrent un mode dominant de répétition de formes, au sens du seuil d'un quart. Ce que la ligne propose alors (un réglage de la mémoire ou des bras mesuré sur monde planté) resterait un essai proposé, sur devis, pas une adoption : la note de conception de la suite est suspendue par la mère.

## 6. Incidents
- Les chemins des sources S2 et des essais, écrits dans la sortie et dans le journal des fichiers ouverts, contiennent le nom du dossier temporaire de la session (`/tmp/claude-0/…`) : nom de dossier, pas un nom ni un identifiant de modèle ; laissé tel quel parce que la condition de la mère exige les chemins.
- E1 (copies C1 à C4 comptées comme lois plantées) est un défaut de définition du programme, vu après exécution ; non réparé, déclaré.
- Avant scellement, une clé de la sortie a été renommée dans le programme (`formes_distinctes_toutes_cartes`) ; l'essai sain a été rejoué après ce changement (`sain2.json`), puis le programme scellé sans autre modification.
- Essais R5 : cas sain sur sources fabriquées (valeurs attendues calculées à la main et retrouvées : rapport 9/14 = 0,642857, parts M4 20/23 et 31/34, M2 1/4 sans K1 et 2/4 avec) ; décisions « plateau » et « pas de plateau » sur unités fabriquées ; artefacts : empreinte attendue fausse, refus (code 2, aucune sortie écrite) ; empreintes réelles attendues sur fichiers fabriqués, refus (code 2, aucune sortie).
- S2b porte une reprise (`reprises` = 1, l'appel échoué rejoué) ; l'essai compte comme joué, comme dans la lecture gelée.
- Aucun accès réseau, aucune dépense, aucun appel de modèle ; aucune course interrompue lue ; aucun refus de permission, de crochet ou de classifieur rencontré.
