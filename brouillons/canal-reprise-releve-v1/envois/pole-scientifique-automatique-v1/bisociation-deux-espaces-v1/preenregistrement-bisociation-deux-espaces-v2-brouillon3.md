# Préenregistrement — la recombinaison bisociative à deux espaces sur mondes synthétiques — v2 — BROUILLON 3, NON SCELLÉ

**Squelette à contre-lire (contre-lecture 3, voir « Nœuds ouverts »), puis à geler par Lazar, puis à sceller avant tout code d'expérience (R1). Aucune méthode, aucun monde n'a été exécuté, et aucune simulation du monde v2 n'a été faite : les seules grandeurs calculées sont des probabilités par approximation normale (script cité en tête, sans aucun tirage aléatoire). Chaque seuil et chaque paramètre de monde porte le marqueur littéral du validateur du dépôt (sections « Seuil » et « Contre-lecture », entrée « Contre-lecture 3 ») : tant qu'il en reste un dans le texte, `sceller_prereg` refuse de sceller. Ce que le validateur ne contrôle pas est dit dans la liste d'arrêt et à la fin du texte. Aucun défaut ne s'applique à un seuil ni à un paramètre de monde.**

- Auteur du brouillon 3 : sous-agent, Sonnet 5.5 (`claude-sonnet-5-5`), même modèle que l'auteur du brouillon 2. A relu le brouillon 2 et la contre-lecture 2 en entier, ainsi que les pièces ci-dessous. **Ne peut pas être contre-lecteur** de ce brouillon.
- Date (UTC), relevé `date -u` : début de la rédaction 2026-10-30T01:26:09Z ; fin de la rédaction 2026-10-30T01:47:35Z.
- Non lus (interdits) : `donnees/`, `prereg/P3-consignes-v1.md`, `diag/*/traces`. Aucune commande git, aucune branche, aucun réseau, aucune dépense, aucun fichier existant modifié, rien scellé. Fichiers neufs écrits : ce brouillon, le script de puissance et sa sortie (listés ci-dessous).
- Commit du code d'analyse : aucun code à ce jour. Le code s'écrit **après** scellement ; son empreinte et son commit sont consignés au manifeste de chaque run avant le premier monde (R9).
- Documents qui font foi (chemins relatifs à `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/` ; SHA-256 recalculés par l'auteur du brouillon 3 le 2026-10-30, tous égaux à ceux du brouillon 2 ; « lu » = lu par l'auteur du brouillon 2, d'après son relevé ; « cité » = repris d'une pièce, non relu). L'auteur du brouillon 3 a lu en entier le brouillon 2 et la contre-lecture 2, et lu en plus : les agrégats de `resultats-trancher-recombinaison-v1.json` (écarts appariés), `methodes_v1.py` l. 76-160, `recoupement-bisociation-v1.md` § 3 et § 7, `avis-opus-neuf-bisociation-v1.md` l. 115-184, `synthese-collisionneur-bisociation-v1.md` (recherche de D7), `src/controle_ia/prereg.py` en entier, et les lignes R-497, R-500, R-529 à R-532 de `registres/decisions.md` :
  - `bisociation-deux-espaces-v1/preenregistrement-bisociation-deux-espaces-v2-brouillon2.md` `36427069b1e8a91c2841d55add9787e8bfbc12daf1c6dd12e7efc75d2b293d91` (**brouillon relu par la contre-lecture 2**, lu en entier) ;
  - `bisociation-deux-espaces-v1/contre-lecture-preenregistrement-bisociation-v2-brouillon2.md` `71382fd9141965ced6604a671256508f37bec0e5cb36a91f8cd186b96677fb3b` (lue en entier ; constats CB2-01 à CB2-09 ; contre-lecteur Opus 5.5) ;
  - `bisociation-deux-espaces-v1/calcul-puissance-bisociation-v2-brouillon3-v1.py` `a6ffbe2c48fe903faea9de816126a3c394b1f3090d7fb4e2696f65832cccbc12` et sa sortie `bisociation-deux-espaces-v1/calcul-puissance-bisociation-v2-brouillon3-v1-sortie.txt` `d9d6c8e8b85752a97a3d294785c416ef9bf8662cddf9ea0d6d6fc492e505f532` (écrits pour ce brouillon ; **source des probabilités marquées (M)** de la section « Seuil »)
  - `bisociation-deux-espaces-v1/preenregistrement-bisociation-deux-espaces-v2-brouillon1.md` `c9077cfe136269c8cf1a5fa8192153fccf48962aba8e276ac2a7e4dad89288e7` (lu, en entier) ;
  - `bisociation-deux-espaces-v1/contre-lecture-preenregistrement-bisociation-v2-brouillon1.md` `a31096c000213127ff191bba54adb47247280ba452464b07a036f07b7be527c4` (lu, en entier ; constats CB-01 à CB-17) ;
  - `bisociation-deux-espaces-v1/recoupement-bisociation-v1.md` `c76959a07f35024d8ea63be54ab7ea9ddc5170960b48112160860898ccf3ee0d` (lu, en entier) ;
  - `bisociation-deux-espaces-v1/question-bisociation-deux-espaces-v1.md` `73a30ab727445969b7ecb8300ba0fef5efd7dfcf9c59cd93943d6ce77e1c4cc3` (lu) ; `bisociation-deux-espaces-v1/avis-opus-neuf-bisociation-v1.md` `2331e70f5fb02530982d535447c88aedade769facd661d882a27e386b57ae3e1` (lu, en entier) ;
  - `bisociation-deux-espaces-v1/entrees/synthese-collisionneur-bisociation-v1.md` `49dd38406b865eae742793045472cac3385e29ef3f3cf1921841df4d94361fb0` (lu en partie : décisions D6 à D9 ; les cellules sous `donnees/` ne sont pas lues) ;
  - `orchestrateur-pole-v7/pole/recombinaison.py` `71faad38644c77ae2cc21f23bfb1011c48fe674a08e542983819425ee47bd3d0` (pièce A ; lu aux lignes 1 à 200 : `cholesky`, `tirage_glouton` et `noyau_fautif` y sont) ;
  - `trancher-recombinaison/trancher-recombinaison-v1.md` `72cff8a067641cab173f3b6fbba32976a64989ded279d078ec4da432a582e4bf` (pièce B, « B » ci-dessous ; lu en entier) ;
  - `trancher-recombinaison/resultats-trancher-recombinaison-v1.json` `daaef112ce5a402bda785c1206db222c8f94793afaf7c0ced910467b4bf4a624` (lu par extraction de ses agrégats ; **source des chiffres de v1** de ce document) ;
  - `trancher-recombinaison/monde_v1.py` `af907b1d5d779dfc1c4353503d31059f20d031a4b4324fea3ca775ad6a6bc98c`, `methodes_v1.py` `2f7a8b1192a79d5bed64fb48f9a5db6f1df6bf86e3a2296eafca75493f2790dd`, `mesures_v1.py` `0a1e3c3806ae892a526fa6a21bcf07217e6f41118244a7cdd01a2f8ad9f8a82e`, `conditions_v1.py` `9246ecc6a4a71f8a701600a0c55c549d622423496a436f2f708b0d9ffe53af35`, `trancher_v1.py` `781335dda51954f5d4ac1ab25ce0ce850a421d8c0c2346ae8284fddc8a6609e0` (tous lus) ;
  - `trancher-recombinaison/preenregistrement-trancher-recombinaison-v1.md` `5335614b2b8b38deb50408c4755401242e5a8436f82b1f9e8be48e57f9dd2985` (cité, non relu) ;
  - `prereg/gabarit-preregistrement-v1.md` `8cad43714b562e28238a92200d6315b1769d8bdf7e9f0a8d72dfe2bc9b37700e` et `src/controle_ia/prereg.py` `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` (lus) ;
  - `registres/decisions.md`, lignes R-497 et R-500 (lues ; le fichier est vivant : empreinte `f25477ce99042ab0e03571d482e8e3686c0009719035029c97209a0d6b9fc282` à la lecture de l'auteur du brouillon 2, `4cd1bf9798cc4c750c75ebb5f76b4bd709af9dcac7f5a5917d41d5ead3333529` à l'assemblage du brouillon 3, le 2026-10-30 (empreinte d'un fichier vivant : elle peut avoir changé depuis) ; le **texte** des lignes est donc cité ci-dessous, pas seulement leur numéro) :
    - R-497 (2026-10-29, Lazar, 13:12 heure de Paris) : « le brainstorming sur la bisociativité (produit scalaire × déterminant : maximiser le volume du parallélépipède entre deux directions, minimiser leur proximité conceptuelle) : c'était dans l'organisme v6.3.2, ça s'est perdu ? » ; proposition (a) retenue par défaut : champ « concepts mobilisés » au gabarit de fiche + « test préenregistré v2 de la recombinaison à deux espaces (volume des domaines × proximité des concepts), Swanson en comparateur, stratifié en témoin, seuil gelé » ;
    - R-500 (2026-10-29, Lazar, 13:23 heure de Paris, mot direct) : « des parents loin en domaine mais proches en concept : oui, pardon, je me suis trompé » ; bisociation = **loin en domaine, proche en concept** ; signe de β positif.
- Chiffres : tous les chiffres de v1 renvoient à `resultats-trancher-recombinaison-v1.json` (`daaef112…`) ou au rapport B (`72cff8a0…`). Ce qui est calculé par l'auteur est marqué (M), avec sa formule ; ce qui l'est par script renvoie au script et à sa sortie (empreintes ci-dessus). Ce qui n'est dans aucune pièce est marqué SUPPOSÉ (R7).
- Références de dimensionnement de v1, rappelées sans servir de preuve (extraits de `daaef112…`, précisions en part de 12 paires) : tirage stratifié (b) 0,2033 (« bien ») et 0,1273 (« moyen ») ; marche de Swanson (d1) +3,5 et +3,8 points sur (b) ; strates dissemblables d'abord (b_eloigne) +11,9 et +6,6 ; b_eloigne en monde inversé −11,6 ; plafond de l'oracle 0,750 et 0,487 (0,278 en « mal ») ; paires valides par monde 67,55 (« bien »), 60,50 (« moyen »), 54,09 (« mal »), 53,59 (monde sans pont) ; vraies paires par monde 12,30 / 12,16 ; vraies paires **valides** 9,52 (« bien »), 5,97 (« moyen »), 3,34 (« mal »). Écarts appariés sur le stratifié b, extraits de `daaef112…` par l'auteur du brouillon 3 (M : moyenne des écarts appariés, « bien » / « moyen ») : forme corrigée v6.3 (a) −4,79 / −2,21 ; uniforme (c) −5,23 / −2,06 ; marche de Swanson (d1) +3,52 / +3,77 ; strates dissemblables d'abord (b_eloigne) +11,90 / +6,60 ; oracle +54,65 / +35,98.

### Ce qui change par rapport au brouillon 2 (constat CB2-xx → où)

La liste des changements du brouillon 2 par rapport au brouillon 1 reste dans le brouillon 2 (empreinte ci-dessus) et dans le tableau de la section « Contre-lecture » ; elle n'est pas répétée.

1. **CB2-01 (majeure)** — la circularité est réduite, pas levée. (a) Nouvelle **condition de jugeabilité J(X) = borne basse à 95 % de Δ(d1c, c ; X) > 0** (S14), indépendante de la forme de N : elle sépare « canal inexploitable dans ce monde » de « la forme ne sait pas l'exploiter ». Table 2 : nouvelle ligne 4 avant « le terme de concept n'apporte rien ». Table 1 : la même condition précède la lecture de A7 (lignes 8 et 9). (b) « N adoptée » devient « **N adoptée, sous W1 à W4** » (Table 1 ligne 10). (c) G8 : graine du monde inerte réécrite et cohérente avec le code de condition 12 du § 7 (rôles 0 à 3 avec le code 1, miroir avec le code 12 et le rôle 7) ; écart apparié Δ(N, N_β0 ; M_bien) − Δ(N, N_β0 ; M_inertes) rapporté, monde à monde. (d) La phrase qui faisait de `M_inertes` « le seul monde » où une forme sans valeur conceptuelle est prise en défaut est corrigée : c'est un contrôle de spécificité, nécessaire mais faible. (e) A7 et P4 sont dits être **le même contraste** (rôles différents).
2. **CB2-02 (majeure)** — prédictions rendues cohérentes (section « Prédiction ») : tableau Δ(X, b) pour b_eloigne, N_β0, d1, d1c, a, c ; **P1 et P2 recalés** pour que P1 ≈ Δ(N_β0, b) + P4 tienne ; **P14 (N − d1) et P15 (N − a)** ajoutées ; nouvelle ligne de lecture « **Swanson par opérateur suffit** » (suffit_d1, Table 1 ligne 7) ; puissance d'A2 tabulée ; probabilité d'adoption recalculée par script. Conséquence à lire en premier : l'adoption à 0,03-0,04 de la contre-lecture 2 venait de centres incompatibles avec P4 ; avec la chaîne ancrée sur v1, elle est de l'ordre de 0,9 ; elle tombe à 0 si l'éloignement seul perd plus de 1,5 point sur b en « moyen ».
3. **CB2-03 (moyenne)** — concepts de fond : nombre de concepts de fond par article rendu paramètre (S16c, recommandation : exactement 2, ce qui neutralise le κ = 1 sur un seul concept de fond), J, **N_filtre renforcé** (même information pondérée que d1c : étiquette de concept partagée la plus rare de fréquence observée ≤ φ, S16f), classe « fond partagé entre champs » mesurée, V7 « lu mais ne change rien ».
4. **CB2-04 (majeure, nœud de décision)** — **paramètres de monde au gel** : S16a à S16f (λ, palettes, concepts de fond par article, loi des émetteurs, ponts par statut, seuil φ), et **S15 (nombre de mondes par condition)**. Ponts par statut recommandés 3 / 3 / 3 (purs, faux, proches) + 3 de surface : 18 paires, 36 articles sur 40 ; V_surface : 2 faux, 2 proches, 5 de surface (36 articles). Les 18 concepts rares restent un choix d'auteur (au plus 15 utilisés).
5. **CB2-05 (faible)** — SP est dit contrôle de plomberie (espérance identique pour tout bras à 12 paires valides distinctes ; A3 échoue avec la probabilité 0,03 quel que soit n) et n'est plus compté parmi les contrôles d'artefact (ce sont `M_inertes` et N_PCg).
6. **CB2-06 (faible)** — S9 : **extension automatique** du nombre de mondes, n' = min(4 800 ; ⌈n × (σ̂ / 15,3)²⌉) au-delà du seuil, au lieu de l'arrêt (qui révélait un grand effet avant le verdict).
7. **CB2-07 (faible)** — S10 : note écrite ; avec les centres recalés de P1, le seuil 12 est franchi presque à coup sûr en « bien » : l'audit est quasi certain si la prédiction se réalise (dit, non corrigé).
8. **CB2-08 (faible)** — nombres de mondes de R-A à μ = 5,5 corrigés : 32 et 61 (conjoint 42 et 80).
9. **CB2-09 (faible)** — § 5 « sortie de la grille » : **non imprimée** ; codes de contraste de la graine 99 énumérés (§ 7) ; le texte ne dit plus que le validateur contrôle la ligne de gel ou le traitement des remarques : il ne le fait pas (voir « Liste d'arrêt » et « Ligne de gel »).
10. **Recommandations de seuils de la contre-lecture 2** écrites comme recommandations (S1 à S16), avec la table de puissance de la contre-lecture et son recalcul (section « Seuil »).
11. **Ajouts de l'auteur du brouillon 3, hors rapport (à contre-lire)** : J aussi dans la Table 1 ; S14, S15, S16 comme éléments de gel ; φ (S16f) ; P14 et P15 ; recalage de P3 ; codes de contraste ; tests R5 de l'extension de S9 et de la graine du monde inerte ; script de puissance et sa sortie ; ligne de gel complète.

### Nœuds ouverts avant scellement

1. **Seuils S1 à S14, nombre de mondes S15 et paramètres de monde S16** : à geler par Lazar, aucun défaut (section « Seuil »). La ligne de gel complète est en fin de texte.
2. **Défauts de 48 h du recoupement**, pris sauf mot contraire de Lazar (échéance au plus tôt 2026-11-01T00:42Z, à confirmer dans `registres/decisions.md` avant scellement) : q ≡ 1 dans le candidat (D-a) ; D-b lu ainsi : **N (score de paire, un passage par strates, sans déterminant) est le candidat éligible ; le déterminant sur les paires (N_dpp, N_dpp_β0) est une ablation descriptive, jamais éligible** ; facteur de concept (κ + ε)^β avec ε = 0,05 (D-c) ; exposants a priori e = 8,5, β = 1, grille en diagnostic (D-d). **D-g (1 200 mondes de décision) est remplacé par S15** : le gel de S15 prime sur le défaut.
3. **Contre-lecture 3** : les ajouts listés au point 11 ci-dessus et le recalage des prédictions n'ont été relus par personne. Recommandation de l'auteur : une contre-lecture 3 ciblée (sous-agent neuf, de préférence d'un autre modèle que Sonnet 5.5), ou, si Lazar la juge superflue, le dire en une phrase dans la ligne de gel : c'est alors un écart à R2, à consigner.
4. **Choix d'auteur non gelés par Lazar** (scellés avec le texte) : 10 concepts de fond, concept moyeu à 30 %, 18 concepts rares, niveaux du canal des concepts, loi de q.
5. **Réserve à lire avant le gel** : la probabilité d'adoption dépend presque uniquement de l'avance de l'éloignement seul (N_β0) sur b en « moyen » (section « Prédiction », conséquence), non des seuils ; v1 est la seule donnée (+6,60), et rien ne dit qu'elle se transpose au monde v2.

## Hypothèse

**H-B2 (hypothèse de travail de la question `73a30ab7…` et de R-497, signe levé par R-500).** Sur des mondes synthétiques à vérité plantée **à deux espaces** (un espace de domaines, un espace de concepts sous-jacents, séparés), tirer les paires à recombiner par un **score de paire produit**, *loin en domaine* ET *proche en concept*, avec sélection par strate, apporte plus de vrais ponts que :
- (i) le tirage stratifié (b), (ii) la forme corrigée de la v6.3 (a), (iii) la marche de Swanson par étiquette rare d'opérateur (d1) et par étiquette de concept (d1c) ;
- (iv) ses propres ablations qui retirent le concept (N_β0) ou ne l'emploient que comme **filtre** (N_filtre).

Lecture en deux volets, plus un contrôle et une condition de jugeabilité, à ne pas confondre :
- **volet d'adoption** : N (forme commune, définie au plan d'analyse) est-elle meilleure que les témoins, sous contrôles, **et** son terme de concept apporte-t-il quelque chose (A7), **dans un monde jugeable (J)**, et **sous W1 à W4** ? ;
- **volet « ingrédient manquant, sous W1 à W4 »** : dans un monde où le concept observé porte de la vérité, la proximité conceptuelle **dans l'objectif** apporte-t-elle quelque chose que ni l'éloignement seul ni le filtre ne donnent ? La réponse ne vaut **que sous W1 à W4** : elle ne dit pas que le concept apporte dans un monde réel ;
- **contrôle de manipulation** (P4) : N − N_β0 > 0 dans les mondes où le concept porte de la vérité montre seulement que l'instrument voit le canal de concepts. Il ne prouve rien sur la valeur du concept. **A7 est le même contraste que P4** (borne basse à 95 % de Δ(N, N_β0) > seuil S3) ; il a deux rôles, condition de l'adoption et contrôle de manipulation, et l'adoption est donc toujours lue « sous W1 à W4 » (CB2-01) ;
- **condition de jugeabilité J** : le canal observé porte de la vérité exploitable, jugé **sans N** par le contraste d1c − c (borne basse à 95 % > seuil S14). Sans elle, l'échec de N à battre N_β0 ne distingue pas « le canal est inexploitable dans ce monde » de « la forme ne sait pas l'exploiter ». J remplace la condition de jugeabilité de la synthèse (D7, B : Z_oracle − Z₀ ≥ δ), qui n'avait pas été reprise.

Hypothèses de travail du monde (SUPPOSÉES ; elles encodent l'hypothèse ; l'avis d'Opus et B § 6 le disent) :
- (W1) les concepts existent comme variables latentes séparées du domaine ;
- (W2) leur observation passe par un canal à trois niveaux (couverture, parasites, fuite de domaine) ;
- (W3) la vérité est « champs différents ET pont latent commun non moyeu ET contraintes vraies compatibles », où le pont latent est soit un opérateur (greffe ou jumeau, comme en v1), soit un concept rare (pont conceptuel pur) ;
- (W4) un pont d'opérateur laisse une trace conceptuelle avec une probabilité λ (couplage), et les concepts de fond, qui ne font jamais la vérité, sont indépendants des opérateurs et des ponts.

Le prix de W1 à W4 est mesuré par la condition `M_inertes` (concepts observés de même loi, sans aucun lien avec la vérité), par la dose-réponse sur λ, par V_fuite, V_concepts_absents, la non-régression sur les mondes v1 et la validation du générateur.

Ce que ce test ne dit pas (B § 6, étendu) :
- rien sur la qualité des fiches fusionnées par un modèle ; rien sur les vraies fiches (préenregistrement distinct, lecture descriptive) ;
- A1 et A2 dépendent de la façon dont le générateur lie le concept au champ (axe palettes : S16b en décision ; communes et disjointes en descriptif). Une paire proche (même champ) partage souvent un concept de fond avec κ ≈ 1, alors qu'un vrai pont n'en partage qu'un parmi plusieurs ; selon l'axe, cela favorise ou défavorise N par rapport à d1c, qui ignore la distance ;
- les concepts rares marquent les ponts plantés de **tout** statut (vrai, faux, proche) : la rareté sépare « planté » de « non planté », pas « vrai » de « faux ». Cela avantage d1c, N et N_filtre de la même façon, et c'est le même mécanisme que celui qui fait gagner d1 en v1 ;
- λ n'est pas calibré sur un corpus réel : il fixe la force de l'hypothèse. La dose-réponse (M_inertes, M_couplage_faible, M_bien) en montre la pente, pas la valeur réelle ;
- **`M_inertes` est un contrôle de spécificité nécessaire mais faible (CB2-01)** : un bras qui suit κ y perd presque à coup sûr, parce que les concepts rares tirés au hasard créent des paires leurres éloignées à fort κ. A8 ne prend donc en défaut que les gains tirés de lois que le miroir conserve (nombre d'étiquettes par article, fréquences documentaires, palettes liées aux champs, concepts de fond). Il ne prouve pas l'absence de toute autre source de gain ; N_PCg, SP et les bras artefacts de la liste d'arrêt contrôlent chacun un autre défaut ;
- **la jugeabilité J ne garantit pas que le monde ressemble à un corpus réel** : elle garantit seulement que, dans ce monde, un bras simple qui lit les étiquettes de concept bat le tirage uniforme. Si J échoue, aucune lecture négative sur le concept n'est permise (Tables 1 et 2) ;
- **concepts de fond** : avec des vecteurs normés, deux articles de champs différents qui ne portent qu'un même concept de fond ont κ = 1, plus que tout vrai pont (κ ≈ 0,68 d'après la contre-lecture 2, ordre de grandeur sans simulation). Cela peut faire échouer P4 pour une raison de générateur. La neutralisation (G3) combine S16c, J, N_filtre renforcé et la mesure de la classe « fond partagé » ; elle ne la supprime pas, et son effet n'est pas mesuré avant les mondes de décision.

Antériorité (R8) : **la forme n'est pas revendiquée comme inédite**. Le principe « proche en mécanisme, loin en domaine » est probablement occupé (Gentner 1983 ; Hope et collaborateurs 2017 ; Berthold 2012 ; Chan et collaborateurs 2018 — de mémoire, non vérifié sur PDF, R7). Seule la forme et son test à vérité plantée sont en jeu ; vérification d'antériorité avant toute revendication.

## Prédiction chiffrée et signe attendu

Ordres de grandeur SUPPOSÉS, **ancrés sur les écarts appariés de v1** (`daaef112…`, « bien » / « moyen », en points sur le stratifié b) : strates dissemblables d'abord (b_eloigne) +11,90 / +6,60 ; marche de Swanson (d1) +3,52 / +3,77 ; forme corrigée v6.3 (a) −4,79 / −2,21 ; uniforme (c) −5,23 / −2,06. Chaque ligne donne ce qui compterait comme réfutation ; les lignes sont lues symétriquement (R3, R4). Les sigles S1 à S16 renvoient à la section « Seuil ».

**Chaîne de cohérence (CB2-02).** Les écarts appariés s'ajoutent : pour deux bras quelconques, Δ(N, X) = Δ(N, b) − Δ(X, b), et Δ(N, b) = Δ(N, N_β0) + Δ(N_β0, b) exactement (linéarité de la moyenne appariée). Le brouillon 2 donnait P4 = +3 à +8 et P2 = +2 à +7, soit Δ(N_β0, b) ≈ 4,5 − 5,5 = −1 en « moyen » à leurs centres, sans le dire, alors que l'éloignement seul fait +6,60 en v1. Les prédictions ci-dessous sont recalées pour que la chaîne tienne ; les fourchettes de P1 à P3, P14 et P15 sont des sommes de fourchettes (bas + bas, haut + haut), donc volontairement larges.

| Bras X | Δ(X, b) en v1 (« bien » / « moyen ») | Prédiction v2 « bien » | Prédiction v2 « moyen » | Raison (SUPPOSÉ) |
|---|---|---|---|---|
| b_eloigne | +11,90 / +6,60 | +9 à +14 | +5 à +8 | même règle qu'en v1 (strates de cosinus moyen ≤ médiane d'abord) ; l'étage commun élargi aux étiquettes de concept peut déplacer cet écart dans les deux sens : centre de v1, fourchette élargie |
| N_β0 | — | +8 à +14 (centre +11,9) | +4 à +9 (centre +6,6) | éloignement seul, par score continu puis strates : même information que b_eloigne ; centre pris égal à celui de b_eloigne, écart attendu −2 à +2 |
| d1 | +3,52 / +3,77 | +2 à +5 (centre +3,5) | +2 à +5 (centre +3,8) | marche par étiquette d'opérateur, inchangée ; les ponts d'opérateur sont ceux de v1 |
| d1c | — | +2 à +6 (centre +4) | +2 à +6 (centre +4) | même marche sur les étiquettes de concept ; les concepts rares marquent des ponts de tout statut et des émetteurs de surface (G5) : pas mieux que d1 par construction |
| a | −4,79 / −2,21 | −6 à −3 (centre −4,8) | −4 à −1 (centre −2,2) | inchangé : la forme corrigée v6.3 perd contre b |
| c | −5,23 / −2,06 | −6 à −3 | −4 à −1 | inchangé : tirage uniforme |

| # | Contraste | Signe | Ordre de grandeur | Réfutation de la prédiction |
|---|---|---|---|---|
| P1 | N − b, « bien » | + | **+11 à +22 (centre +17,4)** = Δ(N_β0, b) (+8 à +14) + P4 (+3 à +8) | borne haute à 95 % < θ_abs (S1) ; < 0 : N perd |
| P2 | N − b, « moyen » | + | **+7 à +17 (centre +12,1)** = Δ(N_β0, b) (+4 à +9) + P4 (+3 à +8) | idem |
| P3 | N − d1c (« bien », « moyen ») | + (confiance 0,40) | « bien » +5 à +20 (centre +13) ; « moyen » +1 à +15 (centre +8) | borne haute à 95 % ≤ 0 dans les deux : « Swanson guidé par concepts suffit » (Table 1 ligne 6) ; **un résultat nul est une réfutation permise de P3**, nommée comme telle |
| P4 | N − N_β0 en M_bien, M_moyen : **contrôle de manipulation = A7** | + | +3 à +8 points (centre +5,5) | borne haute < δ_non (S6) dans les deux : l'instrument ne voit pas le canal. Dit comme tel : P4 positif ne prouve rien sur la valeur du concept |
| P5 | N − N_filtre (concept dans l'objectif contre filtre **renforcé**) | + | +1 à +5 (centre +3, conservé faute d'élément ; peut baisser avec le filtre renforcé) | borne haute < δ_non dans les deux : « le concept suffit comme filtre » |
| P6 | **M_inertes** : N − N_β0 | ≤ 0 | −3 à 0 point | borne basse à 95 % > 0 (artefact, audit R4) ; ou borne haute ≥ δ_non (instrument trop imprécis) |
| P7 | placebos : N sous le vrai score − N_PCg (permutation globale) ; N_PCg − N_β0 ; N_PC − N_β0 | + ; ≤ 0 ; ≥ 0 | > 0 ; −5 à 0 ; 0 à +3 | Δ(N, N_PCg) borne basse ≤ 0 : le gain n'est pas de l'information conceptuelle ; Δ(N_PCg, N_β0) borne basse à 99 % > 0 : artefact (audit R4). Δ(N_PC, N_β0) ≥ 0 n'est **pas** une réfutation : voir la note sous la table |
| P8 | monde sans pont (SP, **contrôle de plomberie**) : N − b, N − d1c, N − N_β0, précision placebo | 0 | 0 | intervalle à 99 % excluant 0 : erreur de code ou probabilité 0,03 (A3) |
| P9 | vérité inversée : Δ_INV − Δ_bien (Δ = N − b) | − | −5 à −20 points | borne haute ≥ 0 : N ne cible pas l'éloignement |
| P10 | fuite de domaine ρ = 0,6 : Δ_V_fuite − Δ_bien | − | −1 à −6 points | borne haute ≥ 0 : l'avantage ne vient pas des concepts |
| P11 | non-régression (mondes v1) : N − b | ≥ marge S7 | ≥ 0 attendu | borne basse à 99 % < marge S7 |
| P12 | dose-réponse de Δ(N, N_β0) selon le couplage : M_inertes < M_couplage_faible < M_bien | croissante | pente > 0 | descriptive : une pente non croissante est rapportée, sans verdict |
| P13 | descriptives : N_dpp − N ; N_global − N ; N_dpp − N_dpp_β0 ; palettes communes / disjointes contre M_bien | voir note | voir note | aucune réfutation de verdict (diagnostic) |
| P14 | N − d1 (« bien », « moyen ») | + | « bien » +6 à +20 (centre +14) ; « moyen » +2 à +15 (centre +8) | borne haute à 95 % ≤ 0 dans les deux : « Swanson par opérateur suffit » (Table 1 ligne 7) |
| P15 | N − a (« bien », « moyen ») | + | « bien » +14 à +28 (centre +22) ; « moyen » +8 à +21 (centre +14) | borne haute à 95 % ≤ 0 : N ne bat pas une forme que v1 a réfutée → audit R4 |

Notes :
- **Sens attendu de Δ(N_PC, N_β0)** (permutation à l'intérieur d'un domaine observé) : ≥ 0, de 0 à +3 points. Raison : N_PC garde la composition en concepts de chaque domaine ; si les concepts de fond suivent partiellement les champs (palettes de 4 sur 10), cette information de domaine est légitime et peut donner un petit gain sur N_β0 sans aucun artefact. Seul N_PCg, qui détruit aussi l'information de domaine en conservant les fréquences d'étiquettes, sert de test d'artefact.
- **Décomposition** : Δ(N, N_PCg) = information de domaine + information d'article ; Δ(N_PC, N_PCg) est la part de domaine ; Δ(N, N_PC) est la part d'article. Les trois sont rapportées.
- P13 : N_dpp − N ≤ 0 attendu (−6 à 0) ; |N_dpp − N_global| ≤ 1 ; Δ(N_dpp, N_dpp_β0) ≥ 0 comme Δ(N, N_β0) ; palettes communes : attendu en baisse pour N (le concept de fond y est partagé entre champs) ; palettes disjointes : attendu en hausse. Les signes de ces deux dernières sont SUPPOSÉS et non réfutables.
- Justification de P9 (M) : sur v1, le diagnostic d'éloignement passe de +11,9 à −11,6, soit −23,5 (B § 7.2) ; N mêle éloignement et concept, d'où une chute plus faible.
- Confiances de l'auteur du brouillon 2 (SUPPOSÉ), **conservées sans recalibrage** : 0,55 sur P1, 0,40 sur P3, 0,50 sur P4. L'avis d'Opus donne 0,45 pour « bat d1 sur les mondes étendus ».
- **Conséquence des prédictions sur la lecture (CB2-02, recalculée par script, section « Seuil »).** Aux valeurs recommandées (n = 2 400), « N adoptée » a une probabilité d'environ **0,91 (σ « moyen » 11) à 0,89 (15,3)** si l'éloignement seul garde en v2 l'avance qu'il a en v1 (centres ci-dessus) ; d'environ **0,80 / 0,52** avec les centres implicites du brouillon 2 (Δ(N_β0, b) = +2,5 « bien » et −1 « moyen », donc Δ(N, d1 ; « moyen ») = +0,7) ; de **0,03 / 0,04** avec les seuils et le nombre de mondes du brouillon 2 (contre-lecture 2). L'adoption dépend d'**une seule quantité** : l'avance de N_β0 sur b en « moyen ». Sous −1,5 point elle est impossible (A1 et A2 contre d1 échouent) ; à −1 point elle vaut 0,48 / 0,18 ; à partir de −0,5 point elle vaut 0,9 (script § 13). La prédiction de l'auteur est donc que l'éloignement seul garde son avance de v1 ; c'est elle, non le choix des seuils, qui rend « N adoptée » probable. **Rien ne dit qu'elle se transpose** : l'étage commun élargi aux étiquettes de concept peut la réduire.
- **P5 et le filtre renforcé** : à P5 = +3 la probabilité de « oui » est de 0,91 / 0,87 ; à P5 = +2,5 elle est de 0,24 ; à P5 ≤ +2 elle est de 0,00 et le verdict tombe en « indécis » (zone entre δ_non et δ), puis en « non : le filtre suffit » si P5 descend sous δ_non (script § 6). Le centre de P5 est conservé faute d'élément ; le filtre renforcé pousse P5 vers le bas.
- **Audit de symétrie et P1** : avec le centre recalé de P1 (+17,4 en « bien »), le déclencheur |Δ(N, b)| ≥ 12 de S10 est franchi presque à coup sûr si la prédiction se réalise (voir S10).

## Métrique

**Unité** : le monde. **Budget** : 12 paires, tirées **en un seul passage** sur les mêmes 40 candidats (8 domaines × 5 articles). Les « 3 générations de 4 paires » de B et de v1 n'ont **aucun effet** ici, pour tous les bras sans exception (N_dpp compris) : v1 faisait déjà un seul tour sur le budget de 12 (`_tour_des_strates`). Une paire acceptée n'est plus retirée.

**Vrai pont** (latent, jamais lu par une méthode) : champs différents (monde inversé : même champ, domaines différents), pont latent commun non moyeu (un opérateur latent commun, ou un concept rare latent commun ; **jamais** un concept de fond ni le concept moyeu), contraintes vraies compatibles. La vérité est une fonction du seul `Latent`, calculée une fois par monde pour toutes les paires ; la recette de plantation (statut « vrai », « faux », etc.) n'a pas d'autre rôle que de la rendre vraisemblable.

**Vraies paires par mécanisme**, comptées et rapportées par monde et par condition : greffe, jumeau, pont conceptuel direct (planté), **expansion** (toute vraie paire non plantée : en v1, 12,3 vraies paires par monde pour 6 plantées, `daaef112…`, parce que tous les porteurs d'un opérateur importé sont vrais).

**Mondes exclus.** Un monde est exclu **pour tous les bras à la fois** si, avant l'exécution des bras, il a moins de 12 paires valides, ou (hors SP) aucune vraie paire valide. La décision ne dépend d'aucune sortie de bras. Le taux d'exclusion de chaque condition est rapporté ; au-dessus du taux S11 dans une condition de décision : arrêt.

**Précision (primaire)** : π(X, m) = (nombre de vrais ponts parmi les 12 paires de X dans le monde m non exclu) / **12**. Si la règle d'un bras rend moins de 12 paires (abstention), la suite est **complétée** par un tirage uniforme sans remise parmi les paires valides restantes (graine du bras) ; ce complément est **déclaré** : `n_complete` est rapporté par bras et par condition, et la précision, y compris la précision placebo, garde le dénominateur 12. Aucun bras n'est noté sur moins de 12 paires. Un bras déclaré non applicable d'avance (d1c dans V_concepts_absents, dans NR_bien et NR_moyen où d1c ≡ d1) est exclu de la condition, non noté zéro.

**Estimateurs** : moyenne sur les mondes non exclus ; écart apparié Δ(X, Y ; condition) = moyenne sur m de [π(X, m) − π(Y, m)] ; rapport r(X, Y) = moyenne de π(X) / moyenne de π(Y). Écarts entre conditions (INV, V_fuite contre « bien ») : ensembles de mondes distincts, rééchantillonnage indépendant des deux.

**Intervalles** : percentiles de 2 000 rééchantillonnages des mondes (appariés pour un écart). « Borne basse à 95 % » = percentile 2,5 ; « borne haute à 95 % » = percentile 97,5 ; « borne basse (ou haute) à 99 % » = percentile 0,5 (ou 99,5). Niveau 95 % pour les contrastes décisifs et les contrôles de non-gain de N_PCg, M_inertes ; niveau 99 % pour les contrôles placebo (SP, N_PCg − N_β0) et la non-régression. Graine : spawn_key (code de condition, code de contraste, 99), voir § 7.

**Secondaires (descriptifs)** : rappel ; rappel par mécanisme ; pièges tirés par classe (moyeu d'opérateur, moyeu de concept, surface, faux pont, pont proche, émetteur de surface, parasite, **fond partagé entre champs**, autre — classes de `mesures_v1.classe_pont` étendues) ; strates distinctes par paire ; **articles distincts parmi les 12 paires** ; part de paires éloignées et conceptuellement proches (latent, et observé) ; précision placebo en SP (part des paires tirées qui appartiennent à un ensemble de 6 paires valides tirées au hasard, graine propre au monde, indépendante des bras, comme en v1 ; **contrôle de plomberie seulement** : son espérance est la même, 6 / V, pour tout bras qui rend 12 paires valides distinctes, donc la différence vraie entre bras est nulle par construction, voir A3) ; `n_complete`, nombre de vecteurs de concepts nuls et de pivots non positifs par bras ; fuite mesurée de la validation ; écart apparié Δ(N, N_β0 ; M_bien) − Δ(N, N_β0 ; M_inertes), monde à monde (G8) ; **loi de κ observé par classe de paire** (voir § 6).

## Seuil

**Tous les seuils et tous les paramètres de monde de ce préenregistrement sont des marqueurs de gel. Lazar les gèle en une ligne datée dans `registres/decisions.md` (texte proposé : section finale « Ligne de gel pour Lazar »). Aucun défaut ne s'applique, ni à 48 heures ni autrement.** Pour chaque seuil : la valeur (marqueur), puis, sur une ligne à part, la recommandation de l'auteur (elle reprend les valeurs recommandées par la contre-lecture 2), puis sa raison. Une recommandation est une recommandation : le texte ne la lit pas comme une valeur. Les points sont des points de pourcentage de précision (0,01 = 1 point). Sauf mention, les seuils portent sur les conditions de décision M_bien et M_moyen, notées « les deux ».

**S1 — θ_abs, écart absolu d'adoption, contraste N − b, dans les deux**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : +4 points.
- Raison : les seuils absolus sont des effets minimaux d'intérêt, et les contrôles (A7, A8, N_PCg) sont plus sensibles que le seuil de détection (contre-lecture 2). +4 reste au-dessus de la marche de Swanson seule en v1 (+3,52 ; +3,77) ; l'éloignement seul (+11,90 ; +6,60) le franchit, ce que A7 (S3) interdit de lire comme adoption. Avec +5 et les centres du brouillon 2, A1 en « moyen » avait 0,06 / 0,13 de probabilité à n = 1 200 (reproduit) ; avec +4, 0,99 / 0,95 à n = 2 400 pour un effet vrai de 4,5 (M, script § 1-2). Avec les centres recalés de P1 et P2 (+17,4 ; +12,1), S1 ne lie pas ; il lie si l'éloignement seul s'effondre.
- Autres options (non recommandées) : (a) +5 (brouillon 2 ; avis d'Opus) ; (b) +12, sans seuil relatif (continuité avec v1 ; ×1,59 en « bien » et ×1,94 en « moyen » sur b de v1, (M) 12 / 20,3 et 12 / 12,7) ; (c) synthèse : ×1,3 et Δ(N, b) ≥ Δ(b_eloigne, b) − 2, soit +6,1 et +3,8 pour ×1,3, +9,9 et +4,6 pour l'autre terme (M, sur les chiffres de v1).

**S2 — θ_rel, rapport d'adoption r(N, b), dans les deux**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : ×1,20.
- Raison : ne lie que si b dépasse 20 % de plus que sa propre moyenne ; sur les moyennes de b de v1 (20,33 et 12,73 points, `daaef112…`), ×1,20 équivaut à +4,07 en « bien » (M, 0,20 × 20,33 ; proche de S1) et +2,55 en « moyen » (M, 0,20 × 12,73 ; ne lie pas). La moyenne de b en v2 est inconnue : l'équivalent en points est rapporté avec les résultats, non gelé.

**S3 — A7, contraste d'apport du concept à l'adoption : borne basse à 95 % de Δ(N, N_β0) strictement supérieure à ce seuil, dans les deux**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : 0 (c'est-à-dire borne basse > 0).
- Raison : A7 sert à empêcher qu'un gain dû à l'éloignement seul soit lu comme l'adoption de N (CB-02) ; son rôle est la détection d'un signe, la taille de l'apport est jugée par δ dans le volet ingrédient. Rappel : c'est le même contraste que P4 (contrôle de manipulation) ; l'adoption est donc lue sous W1 à W4.

**S4 — règle de détection « le concept apporte »** (notée détecte(Δ, δ)), à choisir entre deux options écrites
- Valeur : À REMPLIR — à geler par Lazar.
- Option R-A : détecte(Δ, δ) = vrai si estimation de Δ ≥ δ **et** borne basse à 95 % de Δ > 0 (formulation de l'avis d'Opus : « ≥ +3 et bornes basses > 0 »).
- Option R-B : détecte(Δ, δ) = vrai si borne basse à 95 % de Δ ≥ δ (durcissement du brouillon 1, non signalé alors).
- Recommandation de l'auteur : R-A.
- Raison : à 2 400 mondes, R-A atteint la puissance 0,8 dès que l'effet vrai vaut δ + 0,19 à 0,26 point (2,69 pour σ 11 ; 2,76 pour σ 15,3), R-B dès δ + 0,63 à 0,88 point (3,13 ; 3,38) ((M), script § 3) ; avec les prédictions P4 = +5,5 et P5 = +3 de l'auteur, « oui » a la probabilité 0,91 / 0,87 sous R-A et 0,21 / 0,13 sous R-B (script § 6).

**S5 — δ, apport minimal du concept pour « détecte »**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : +2,5 points.
- Raison : la contre-lecture 2 (le brouillon 2 recommandait +3, l'avis d'Opus +3, la synthèse +2). À +3, δ égalait le centre de P5 (+3) et la puissance de N − N_filtre y était de 0,5 par construction ; à +2,5, elle est de 0,99 / 0,95 par condition à n = 2 400 (script § 3) et la détection de N − N_β0 (centre +5,5) reste certaine.

**S6 — δ_non, borne haute à 95 % sous laquelle « le concept n'apporte pas »**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : +1,5 point.
- Raison : la contre-lecture 2 (le brouillon 2 recommandait +2). δ_non < δ laisse une zone « indécis » entre 1,5 et 2,5 et rend les lignes « oui » et « non » exclusives. A8 (`M_inertes`) passe avec la probabilité 0,975 à effet nul et prend en défaut un gain parasite de 1 point avec 0,89 (σ 15,3) à 0,99 (σ 11) à n = 2 400, 0,96 pour σ = 13 (script § 8).

**S7 — non-régression sur les mondes v1 (NR_bien, NR_moyen) : borne basse à 99 % de Δ(N, b) supérieure ou égale à la marge, et nombre de mondes**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : marge −2 points, 1 200 mondes pour NR_bien et pour NR_moyen.
- Raison : la marge −1 de l'avis d'Opus sur 600 mondes n'est franchie, si N égale simplement b (effet vrai 0), qu'avec la probabilité 0,16 (σ 15,3) à 0,36 (σ 11) ; la marge −2 sur 1 200 mondes la porte à 0,97 (15,3) et 1,00 (11) ; une non-régression qui échoue quand rien ne régresse ne mesure rien ((M), script § 9 ; le brouillon 2 donnait 0,17 et 0,98, soit 0,01 de plus, à l'arrondi près).

**S8 — plafond de l'oracle : précision de l'oracle supérieure ou égale à ce seuil, en M_bien et en M_moyen**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : 0,30.
- Raison : avis d'Opus ; en v1 l'oracle faisait 0,750 et 0,487, soit de la marge ; 0,278 en « mal » serait sous le seuil, ce qui concorde avec le statut descriptif de M_mal.

**S9 — écart-type de garde et action : écart-type de Δ(N, b) par monde sur 200 mondes de validation de M_bien et sur 200 de M_moyen, séparément ; au-delà du seuil, le nombre de mondes de décision de la condition est étendu (il n'y a pas d'arrêt)**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : seuil 18 points ; action : **extension automatique** du nombre de mondes de la condition concernée à n' = min(4 800 ; ⌈n × (σ̂ / 15,3)²⌉), où n est le nombre de S15 et σ̂ l'écart-type estimé ; n' est calculé et consigné au manifeste **avant** le premier monde de décision ; si σ̂ ≤ seuil, n est inchangé ; si n' atteint le plafond de 4 800, la condition s'exécute au plafond et l'erreur type atteinte est rapportée, sans arrêt. `M_inertes` prend le n' de M_bien (il en reprend les graines).
- Raison : (M) reconstitué sur v1 d'après les demi-largeurs à 95 % de `daaef112…` (écart-type = demi-largeur × √400 / 1,96) : 15,0 à 15,3 en « bien » (Δ(d1, b), Δ(b_eloigne, b), Δ(a, b)), 11,2 à 12,0 en « moyen » ; 18 est 18 % au-dessus du maximum de v1, soit environ 3,5 erreurs types d'un écart-type estimé sur 200 mondes (erreur relative 1 / √(2 × 199) = 0,050, script § 14). **L'arrêt du brouillon 2 est abandonné (CB2-06)** : l'écart-type de Δ(X, b) croît avec l'effet (22,7 pour l'oracle en « bien », contre-lecture 2), donc un N fort pouvait franchir le seuil et arrêter le run, révélant un grand effet avant le verdict. L'extension ne lit que σ̂ ; la moyenne de Δ(N, b) en validation reste dans le fichier scellé. Exemples (script § 14) : σ̂ = 18 donne n' = 3 322 ; 20 donne 4 101 ; à partir de 21,64, le plafond 4 800.

**S10 — seuils de l'audit de symétrie (R4)**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : |Δ(N, b)| ≥ 12 points dans les **deux sens** (gain ou perte), en M_bien ou en M_moyen ; précision de N ≥ 0,9 fois celle de l'oracle.
- Raison : un seul chiffre pour les deux signes (CB-10) ; 12 est le seuil d'adoption de v1, qu'aucune forme n'a atteint en v1, de sorte qu'un résultat plus grand est assez anormal pour être audité ; 0,9 de l'oracle est un quasi-plafond. **Note (CB2-07)** : b_eloigne seul faisait +11,90 en « bien » en v1, et le centre recalé de P1 est +17,4 : un résultat conforme à la prédiction franchit ce seuil, donc **l'audit est quasi certain en « bien » si la prédiction se réalise** ; ce n'est pas une anomalie (R4 : un résultat conforme mais énorme est audité comme un résultat suspect), c'est le coût d'une prédiction forte. L'audit est une relecture de code et un test de permutation, pas un arrêt.
- Autre option (non recommandée) : relever le seuil à 20 points ; le déclencheur « précision de N ≥ 0,9 × oracle » reste.

**S11 — seuils d'arrêt en taux**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : 2 % pour chacun de trois taux : mondes exclus par condition de décision ; mondes régénérés après échec de plantation ; mondes où un bras rend une sortie vide avant complément.
- Raison : valeur du brouillon 1 pour le premier taux, étendue aux deux autres (CB-07) ; au-delà, la population mesurée n'est plus celle du plan.

**S12 — marge de reproduction des témoins de v1**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : 2 points de chaque côté de l'intervalle à 95 % du tableau de B § 1 pour b, a, c et d1 en NR_bien et NR_moyen.
- Raison : valeur du brouillon 1 ; les graines de v2 sont celles de `SeedSequence`, pas celles de `random.Random(entier)` de v1 : on s'attend à une variation d'échantillonnage (erreur type de la précision moyenne de b : 0,34 point à 1 200 mondes, contre 0,58 à 400, (M), d'après la demi-largeur 0,0115 de l'intervalle de b en « bien » dans `daaef112…`, soit un écart-type de 11,7 points) mais pas à un écart de code.

**S13 — seuils de validation du générateur (§ 6), sur graines distinctes (300 mondes « bien », 300 « moyen », 100 jumelles)**
- V1 cosinus moyens, même domaine / proches / éloignés ; valeur : À REMPLIR — à geler par Lazar. Recommandation : [0,51 ; 0,57], [0,25 ; 0,31], [0,00 ; 0,06]. Raison : référence de v1 0,54 / 0,28 / 0,03 (B § 5) ± 0,03.
- V2 fuite de domaine F (formule au § 6) en « bien » ; valeur : À REMPLIR — à geler par Lazar. Recommandation : F ≤ 0,10. Raison : avis d'Opus (« fuite ≤ 10 points en bien ») ; reprise sans changement.
- V3 queue (formule au § 6) ; valeur : À REMPLIR — à geler par Lazar. Recommandation : excès ≤ 0,10. Raison : brouillon 1, sans élément pour en changer.
- V4 jumelles (formules au § 6) ; valeur : À REMPLIR — à geler par Lazar. Recommandation : concordance des étiquettes de concept ≥ 0,9 et variation moyenne des cosinus de domaine ≥ 0,2. Raison : brouillon 1 ; seuil de l'avis d'Opus pour la concordance (0,8) relevé à 0,9 parce que le test porte ici sur un générateur et non sur des annotateurs.
- V5 rareté appariée ; valeur : À REMPLIR — à geler par Lazar. Recommandation : écart entre statuts de la fréquence documentaire observée moyenne de l'étiquette de pont ≤ 0,5. Raison : brouillon 1.
- V6 vraies paires valides par monde en « moyen », en moyenne ; valeur : À REMPLIR — à geler par Lazar. Recommandation : ≥ 6. Raison : brouillon 1 ; v1 faisait 5,97 (`daaef112…`), donc le seuil est à la limite de v1, et v2 ajoute des ponts conceptuels visibles par le canal, donc l'attendu est au-dessus.

**S14 — J, condition de jugeabilité : borne basse à 95 % de Δ(d1c, c) strictement supérieure à ce seuil, en M_bien et en M_moyen (J(M_bien) et J(M_moyen))**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : 0 (borne basse > 0).
- Raison : J ne dépend pas de la forme de N (d1c et c sont des témoins) et sépare « canal inexploitable dans ce monde » de « N ne sait pas l'exploiter » (CB2-01). Ordre de grandeur favorable en v1 : d1 − c = +8,75 « bien » et +5,83 « moyen » (M, 3,52 + 5,23 et 3,77 + 2,06, `daaef112…`). Puissance (script § 11, n = 2 400) : un effet vrai de 1,5 point ou plus est détecté avec la probabilité 1,00 ; de 1 point, 0,89 / 0,80 (conjonction des deux conditions, σ « moyen » 11 / 15,3) ; de 0,5 point, 0,22 / 0,13 ; à effet nul, J passe à tort avec 0,02 par condition. Un seuil plus haut (par exemple 1 point) exclut aussi les canaux à peine exploitables ; non recommandé, faute de repère.

**S15 — nombre de mondes par condition (hors NR, fixé par S7), avant extension éventuelle par S9**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : **2 400** pour M_bien, M_moyen et M_inertes ; **600** pour SP, INV et V_fuite ; **600** pour chacune des sept conditions descriptives (M_mal, V_concepts_absents, V_moyeu_conceptuel, V_surface, M_couplage_faible, M_palettes_communes, M_palettes_disjointes). Total : 11 400 mondes de décision (dont NR 2 400) et 4 200 descriptifs, soit 15 600 ; 22 800 au plus avec l'extension de S9 à 4 800 pour les trois grandes conditions.
- Raison : même puissance pour M_bien, M_moyen et M_inertes (A8 : 0,975 à effet nul) ; processeur seul, aucune dépense ; SP reste à 600 parce que la puissance n'y joue pas (la différence vraie y est nulle par construction, CB2-05) ; INV et V_fuite à 600 : A4 et A6 détectent un effet de −3 points avec 0,99 (σ 15,3, M_bien à 2 400, script § 10). Ce gel **remplace** le défaut D-g (1 200 mondes). Options : 1 200 (n du brouillon 2 : adoption 0,49 / 0,26 aux centres du brouillon 2, script § 12) ; 4 800 (plafond de S9).

**S16 — paramètres de monde** (CB2-04 : ils fixent la force de l'hypothèse ; en modifier un est une modification de la force d'une hypothèse, donc un nœud de décision ; aucun n'a de source dans une pièce)

- **S16a — λ, probabilité qu'un pont d'opérateur laisse une trace conceptuelle (G6, G7), et λ_faible de M_couplage_faible.**
  - Valeur : À REMPLIR — à geler par Lazar.
  - Recommandation de l'auteur : λ = 0,7 ; λ_faible = 0,3.
  - Raison : ni 1 (circularité : le pont d'opérateur serait toujours visible dans les concepts) ni 0 (aucune trace) ; la dose-réponse M_inertes (0) < M_couplage_faible (0,3) < M_bien (0,7) en montre la pente (P12). Aucune source : c'est un choix de force de l'hypothèse.
- **S16b — taille de la palette de concepts de fond par champ (G3).**
  - Valeur : À REMPLIR — à geler par Lazar.
  - Recommandation de l'auteur : 4 concepts sur 10.
  - Raison : deux palettes de 4 sur 10 se recouvrent de 1,6 concept en moyenne (contre-lecture 2) : le concept de fond suit partiellement le champ sans l'identifier ; les conditions M_palettes_communes (10 sur 10) et M_palettes_disjointes encadrent ce choix en descriptif. Aucune source.
- **S16c — nombre de concepts de fond par article (G3).**
  - Valeur : À REMPLIR — à geler par Lazar.
  - Recommandation de l'auteur : exactement 2 (tirés dans la palette du champ de l'article).
  - Raison : neutralise le κ = 1 sur un seul concept de fond (CB2-03) : un article à deux fonds qui n'en partage qu'un avec un autre a κ voisin de 0,5 (vecteurs normés, selon les poids), non 1 ; le cas κ = 1 exige de partager les deux. Contrepartie : le κ des vrais ponts baisse aussi, de façon non mesurée (aucune simulation faite). Option : 1 ou 2, probabilités 0,6 et 0,4 (brouillon 2) ; elle laisse le cas κ = 1 sur un seul fond ouvert, que J et N_filtre atténuent sans le supprimer.
- **S16d — loi du nombre latent d'émetteurs L_r d'un concept rare (G5).**
  - Valeur : À REMPLIR — à geler par Lazar.
  - Recommandation de l'auteur : uniforme sur {2, 3, 4}, **la même pour tous les statuts de pont**.
  - Raison : la même loi pour les vrais, les faux et les proches évite que la rareté sépare « vrai » de « faux » (CB-05) ; 4 = L_r maximal, ce qui fixe le seuil φ de S16f. Aucune source.
- **S16e — nombre de ponts par statut (G6) et variante de V_surface.**
  - Valeur : À REMPLIR — à geler par Lazar.
  - Recommandation de l'auteur : (a) 3 greffes et 3 jumeaux ; (b) 3 ponts conceptuels purs ; (c) 3 faux ponts ; (d) 3 ponts proches ; (e) 3 ponts de surface : 6 + 12 = 18 paires, **36 articles sur 40**. Dans V_surface : (c) 2, (d) 2, (e) 5, soit 6 + 3 + 2 + 2 + 5 = 18 paires, 36 articles.
  - Raison : ce sont les comptes de l'avis d'Opus ; la réduction à 2 / 2 / 2 du brouillon 2 (30 articles) n'était pas imposée par le vivier et rendait le canal plus informatif (moins de leurres). Les 18 concepts rares restent un choix d'auteur : 6 + 3 + 3 + 3 = 15 au plus sont utilisés. Garde de configuration : 2 × nombre de paires de ponts ≤ 36, et concepts rares requis ≤ 18.
- **S16f — φ, fréquence documentaire observée maximale de l'étiquette de concept partagée pour le palier 1 de N_filtre (§ 4).**
  - Valeur : À REMPLIR — à geler par Lazar.
  - Recommandation de l'auteur : φ = 4.
  - Raison : 4 est le L_r maximal de S16d ; N_filtre retient ainsi les paires dont l'étiquette partagée la plus rare est aussi rare qu'un concept rare planté, la même information pondérée que d1c (CB2-03). Choix **prudent pour N** : un filtre fort rend P5 plus difficile, ce qui va dans le sens contraire d'une faveur faite à N (R4). Il lit la loi des émetteurs du générateur ; c'est dit.

Valeurs du texte non gelées par Lazar, scellées avec lui : 10 concepts de fond, concept moyeu à 30 %, 18 concepts rares, niveaux (c ; p_par ; ρ) du canal des concepts, deux mots de surface par concept, loi de q (choix de l'auteur ou de l'avis d'Opus, non remis en cause par la contre-lecture 2).

### Puissance des règles écrites (M ; approximation normale ; formules et script)

Source de toutes les probabilités marquées (M) : `bisociation-deux-espaces-v1/calcul-puissance-bisociation-v2-brouillon3-v1.py` (empreinte en tête), sortie `…-sortie.txt` (empreinte en tête) ; section citée par « script § k ». Aucun tirage aléatoire, aucun monde simulé.

**Calcul.** Un écart apparié moyen sur n mondes est pris de loi normale N(μ, s²), s = σ / √n. σ = 15,3 points en « bien » (maximum de v1) et 11 ou 15,3 en « moyen » (v1 : 11,2 à 12,0) ; les écarts-types de Δ(N, N_β0) et Δ(N, N_filtre) ne sont **pas connus** (N et ses ablations sont corrélées : probablement plus petits), donc les tables sont prudentes. Φ est la fonction de répartition normale. Intervalle à 95 % = estimation ± 1,96 s ; à 99 % ± 2,576 s. Les facteurs d'une conjonction sont traités comme indépendants (approximation).
- A1 (une condition) : P(estimation ≥ max(θ_abs ; (θ_rel − 1) × b̄ ; 1,96 s)) = 1 − Φ((t − μ) / s). Exemple : « moyen », σ 11, n 2 400 : s = 11 / √2 400 = 0,2245 ; t = 4 ; μ = 4,5 ; z = (4 − 4,5) / 0,2245 = −2,227 ; P = Φ(2,227) = 0,987.
- Borne basse à 95 % > 0 (A2, A7, J) : P = 1 − Φ(1,96 − μ / s). Exemple : N − d1 en « moyen », μ = 0,7, σ 11, n 2 400 : 1,96 − 0,7 / 0,2245 = −1,158 ; P = 0,877.
- détecte, R-A : P(estimation ≥ max(δ ; 1,96 s)) ; R-B : P(estimation ≥ δ + 1,96 s). N0, NF : P(estimation < δ_non − 1,96 s).
- A8 (`M_inertes`) : borne basse ≤ 0 **et** borne haute < δ_non, soit estimation < min(1,96 s ; δ_non − 1,96 s) (événements emboîtés, non indépendants). Exemple : μ = 0, n 2 400, σ 15,3 : s = 0,3123 ; min(0,612 ; 0,888) = 0,612 ; P = Φ(1,96) = 0,975.
- Non-régression : P(estimation ≥ marge + 2,576 s). Exemple : n 1 200, σ 15,3, marge −2, μ = 0 : s = 0,4417 ; z = (−2 + 1,138) / 0,4417 = −1,952 ; P = Φ(1,952) = 0,9746, soit 0,97.
- Nombre de mondes pour la puissance 0,8 sur « borne basse > 0 » : n = ((1,96 + 0,84) σ / μ)² ; conjoint sur deux conditions (0,894 par condition, z = 1,25) : (1,96 + 1,25). Sur « estimation ≥ δ » : n = (0,84 σ / (μ − δ))² ; on retient le plus grand des deux.

Probabilité de « détecte » (δ = 2,5), n = 2 400, selon l'effet vrai μ (script § 3) :

| μ (points) | R-A, σ 11 | R-A, σ 15,3 | R-B, σ 11 | R-B, σ 15,3 |
|---|---|---|---|---|
| 2 | 0,01 | 0,05 | 0,00 | 0,00 |
| 2,5 | 0,50 | 0,50 | 0,02 | 0,02 |
| 3 (centre P5) | 0,99 | 0,95 | 0,61 | 0,36 |
| 3,5 | 1,00 | 1,00 | 0,99 | 0,89 |
| 4 | 1,00 | 1,00 | 1,00 | 1,00 |
| 5,5 (centre P4) et au-delà | 1,00 | 1,00 | 1,00 | 1,00 |

- Effet vrai donnant la puissance 0,8 à 2 400 mondes : R-A, δ + 0,84 s = 2,69 (σ 11), 2,76 (15,3), 2,81 (18) ; R-B, δ + 2,80 s = 3,13 ; 3,38 ; 3,53.
- Nombre de mondes pour la puissance 0,8 (R-A, δ = 2,5 ; script § 4) : à μ = 5,5, **32** (σ 11) et **61** (σ 15,3), conjoint **42** et **80** (la borne basse > 0 lie, non δ : la formule du brouillon 2, qui ne retenait que δ, donnait 14 / 27 et 30 / 58, CB2-08) ; à μ = 4 : 60 et 115, conjoint 85 et 164 ; à μ = 3,5 : 86 et 166, conjoint 191 et 368 ; au centre de P5 (3) : 343 et 664, conjoint 761 et 1 471 ; à μ = δ = 2,5 : aucun nombre de mondes ne suffit. Sous R-B, au centre de P5 : (2,80 σ / 0,5)² = 3 800 et 7 340 (M).

Probabilité de franchir A1 par condition, n = 2 400, θ_abs = 4, θ_rel = ×1,20 (seuil effectif 4,07 en « bien », 4,00 en « moyen » sur les moyennes de b de v1), selon l'effet vrai μ (script § 1) :

| μ | « moyen », σ 11 | « moyen », σ 15,3 | « bien », σ 15,3 |
|---|---|---|---|
| 3 | 0,00 | 0,00 | 0,00 |
| 4 | 0,50 | 0,50 | 0,42 |
| 4,5 (centre de P2 du brouillon 2) | 0,99 | 0,95 | 0,92 |
| 5 | 1,00 | 1,00 | 1,00 |
| 6 et au-delà (dont les centres recalés 12,1 « moyen » et 17,4 « bien ») | 1,00 | 1,00 | 1,00 |

Reproduction des valeurs du brouillon 2 (n = 1 200, θ_abs = 5, ×1,25) : à μ = 4,5 en « moyen », 0,06 (σ 11) et 0,13 (σ 15,3) (script § 2).

**A2 : borne basse à 95 % de N − d1 > 0 en « moyen »** (CB2-02), selon μ = effet vrai sur N − d1 (script § 5) :

| μ | n = 1 200, σ 11 / 15,3 | n = 2 400, σ 11 / 15,3 | n = 4 800, σ 11 / 15,3 |
|---|---|---|---|
| 0,7 (centres implicites du brouillon 2 : 4,5 − 3,8) | 0,60 / 0,35 | 0,88 / 0,61 | 0,99 / 0,89 |
| 1,5 | 1,00 / 0,92 | 1,00 / 1,00 | 1,00 / 1,00 |
| 8,3 (centre recalé : 12,1 − 3,8) | 1,00 / 1,00 | 1,00 / 1,00 | 1,00 / 1,00 |

Pour la puissance 0,8 sur ce seul contraste à μ = 0,7 : 1 939 (σ 11) et 3 750 (σ 15,3) mondes.

**Probabilités de « oui » et de « non » (Table 2 de lecture)** (n = 2 400, R-A, δ = 2,5, δ_non = 1,5 ; script § 6, § 7). « oui » = D0 et DF dans les deux, A8 ; PG et J supposés tenus ; le facteur 0,99² du dernier test vient des deux tests à 99 % de Δ(N_PCg, N_β0) à vrai effet ≤ 0.

| P4 | P5 | « oui » R-A, σ 11 / 15,3 | avec le facteur N_PCg | « oui » R-B, σ 11 / 15,3 |
|---|---|---|---|---|
| 5,5 | 3 | 0,91 / 0,87 | 0,89 / 0,85 | 0,21 / 0,13 |
| 5,5 | 4 | 0,97 / 0,97 | 0,96 / 0,96 | 0,97 / 0,97 |
| 5,5 | 2,5 | 0,24 / 0,24 | 0,24 / 0,24 | 0,00 / 0,00 |
| 5,5 | 2 | 0,00 / 0,00 | 0,00 / 0,00 | 0,00 / 0,00 |
| 3 | 3 | 0,85 / 0,78 | 0,83 / 0,76 | 0,05 / 0,02 |

« non » (N0 dans les deux, c'est-à-dire borne haute < 1,5) selon l'effet vrai de N − N_β0 : μ = 0 : 1,00 ; 0,5 : 0,89 / 0,80 ; 1 : 0,22 / 0,13 ; 1,5 et au-delà : 0,00. Entre les deux, le verdict est « indécis ».

**`M_inertes` (A8)**, probabilité que A8 tienne selon le gain parasite μ (script § 8) :

| n | μ = 0 | μ = 0,5, σ 11 / 15,3 | μ = 1, σ 11 / 13 / 15,3 | μ = 1,5 |
|---|---|---|---|---|
| 2 400 | 0,975 | 0,39 / 0,64 | 0,01 / 0,04 / 0,11 | 0,00 |
| 1 200 | 0,98 (σ 11 et 13) ; 0,92 (σ 15,3) | 0,65 / 0,62 | 0,12 / 0,24 / 0,20 | 0,00 |

Prise en défaut d'un gain parasite de 1 point à n = 2 400 : 0,99 (σ 11), 0,96 (σ 13), 0,89 (σ 15,3).

**Non-régression** (borne basse à 99 % ≥ marge, une condition ; script § 9) :

| n, σ | marge −1, μ = 0 | marge −1, μ = +1 | marge −2, μ = 0 | marge −2, μ = +1 |
|---|---|---|---|---|
| 600, 11 | 0,36 | 0,97 | 0,97 | 1,00 |
| 600, 15,3 | 0,16 | 0,73 | 0,73 | 0,99 |
| 1 200, 11 | 0,72 | 1,00 | 1,00 | 1,00 |
| 1 200, 15,3 | 0,38 | 0,97 | 0,97 | 1,00 |

**INV et V_fuite** (A4, A6 ; INV ou V_fuite à 600 mondes contre M_bien à 2 400, σ 15,3 ; script § 10) : erreur type de la différence 0,70 (0,77 avec M_bien à 1 200) ; P(borne haute < 0) vaut 0,30 pour μ = −1 (bas de P10 : peu de puissance, dit), 0,99 pour −3, 1,00 pour −5.

**J** (script § 11) : voir S14.

**Probabilité de « N adoptée »** (Table 1 ligne 10), produit des facteurs A1, A2 (contre d1, a, d1c), A7, A3, A4, A5, A6, A8, absence de gain_contrôle, J, traités comme indépendants (script § 12 ; § 13) :

| scénario de centres | n | σ « moyen » 11 / 15,3 |
|---|---|---|
| **recalés (V)** : N_β0 − b = +11,9 « bien », +6,6 « moyen » | 2 400 | **0,91 / 0,89** |
| recalés (V) | 1 200 | 0,86 / 0,84 |
| implicites du brouillon 2 (L) : Δ(N, b) = 8 et 4,5, Δ(N, d1 ; « moyen ») = +0,7 ; produit A1 × A2-d1 × A8 × A3 × A5 seul | 2 400 | 0,80 / 0,52 |
| (L) | 1 200 | 0,49 / 0,26 |
| (L), seuils et n du brouillon 2 (θ 5, ×1,25, δ_non 2) | 1 200 | 0,03 / 0,04 |

J est supposée tenue dans ces lignes (Δ(d1c, c) = +3 points, d1c à +4 sur b : script § 11, § 12), sauf dans les lignes (L), qui reprennent le produit de la contre-lecture 2, lequel n'a pas de facteur J.

Sensibilité (script § 13) : l'avance vraie de N_β0 sur b en « moyen » (« bien » fixé au centre recalé, P4 = +5,5, n = 2 400) : −2 ou −1,5 : 0,00 / 0,00 ; −1 : 0,48 / 0,18 ; −0,5 : 0,91 / 0,77 ; 0 et au-delà : 0,91 / 0,89.

**Extension de S9** (script § 14) : n' vaut 2 400 pour σ̂ ≤ 15,3, 3 322 pour 18, 4 101 pour 20, 4 800 à partir de 21,64. Coût de calcul : processeur seul.

**Table de contrôle : table de puissance de la contre-lecture 2 et recalcul de l'auteur du brouillon 3** (même approximation normale ; script, sections indiquées)

| Quantité (valeurs recommandées, sauf mention) | Contre-lecture 2 | Recalcul (script) | Écart ou remarque |
|---|---|---|---|
| A1 en « moyen », μ = 4,5, θ_abs 4, n 2 400, σ 11 / 15,3 | 0,99 / 0,95 | 0,99 / 0,95 (0,987 ; 0,945) § 1 | égal |
| « oui » sous R-A (δ 2,5), P4 = 5,5, P5 = 3, n 2 400 | 0,91 / 0,87 | 0,91 / 0,87 § 6 | égal ; 0,89 / 0,85 avec les deux tests N_PCg |
| « non » à effet vrai 0 | 1,00 | 1,00 § 7 | égal |
| adoption, centres de l'auteur (brouillon 2), n 2 400 | 0,79 / 0,53 | 0,80 / 0,52 § 12 (A1 × A2-d1 × A8 × A3 × A5) | arrondis, ≤ 0,01 |
| mondes pour 0,8 sur A2 contre d1 (μ = 0,7) | 1 936 / 3 745 | 1 939 / 3 750 § 5 | z = 2,8016 au lieu de 2,80 |
| `M_inertes` à effet nul, n 2 400 | 0,97 | 0,975 § 8 | égal |
| `M_inertes`, gain parasite de 1 point, n 2 400 (n 1 200) | 0,96 (0,76) | 0,96 (0,76) pour σ = 13 ; 0,89 à 0,99 pour σ 15,3 à 11 § 8 | la contre-lecture a pris σ ≈ 13 pour Δ(N, N_β0) ; il est inconnu : la plage est écrite |
| adoption aux seuils recommandés, n 1 200, centres du brouillon 2 | 0,48 / 0,26 | 0,49 / 0,26 § 12 | arrondi |
| « oui » aux seuils recommandés, n 1 200 | 0,74 / 0,68 | 0,76 / 0,70 § 6 bis | la contre-lecture multiplie deux probabilités emboîtées (A8 = 0,90) ; exact : 0,92 (A8 = 0,924) |
| A8 à effet nul, n 1 200, δ_non 1,5, σ 15,3 | 0,90 | 0,92 § 8 | idem (événements emboîtés) |
| valeurs du brouillon 2 (n 1 200, θ 5, ×1,25, δ 3, δ_non 2) : adoption ; « oui » | 0,03 / 0,04 ; 0,24 | 0,03 / 0,04 ; 0,24 § 12, § 6 bis | égal |
| nombre de mondes, R-A, μ = 5,5 (conjoint) | 32 / 61 (42 / 80) | 32 / 61 (42 / 80) § 4 | égal |
| non-régression, 1 200 mondes, marge −2, μ = 0, σ 15,3 | 0,98 (brouillon 2) | 0,97 (0,974) § 9 | 0,01 |
| marge −1, 600 mondes, μ = 0, σ 15,3 | 0,17 (brouillon 2) | 0,16 § 9 | 0,01 |

Aucun écart n'est supérieur à 0,02 ; les deux seuls vrais écarts de méthode sont l'emboîtement de A8 et le σ de Δ(N, N_β0). **Réserve** : la table de la contre-lecture et son recalcul ne valent que sous les centres de l'auteur du brouillon 2 ; sous les centres recalés (ancrés sur v1), les probabilités d'adoption sont différentes (0,91 / 0,89) et la valeur recommandée de S1 ne lie plus, voir ci-dessus.

**Taux d'erreur visés** : intervalles à 95 % (décisifs) et à 99 % (placebo, non-régression). Multiplicité : voir le plan d'analyse, § 8.

## Plan d'analyse

### 1. Générateur `monde_v2.py` (nouveau nom, R12 ; étend `monde_v1.py` `af907b1d…`)

Nombres SUPPOSÉS, repris de l'avis d'Opus § 3 sauf mention. Les paramètres S16a à S16f sont gelés par Lazar : ils sont désignés ici par leur nom, jamais par une valeur.

**G1 — Séparation vérité / observation.** Un monde est une paire (`Latent`, `Obs`). `Obs` contient, pour chaque article : le sac de mots de domaine, l'ensemble des étiquettes d'opérateur observées, l'ensemble des étiquettes de concept observées (noms disjoints de ceux des opérateurs : préfixes `op:` et `co:`), les contraintes observées, le domaine observé, l'aptitude q ; la matrice `cos` des cosinus de domaine ; les fréquences documentaires observées. `Latent` contient : champs, groupes d'opérateurs, opérateurs et moyeux, tous les concepts latents, contraintes vraies, ponts plantés et leur statut, **provenance des étiquettes** (vrai, homonyme, parasite, moyeu : ce sont des champs latents), vérité. Les bras reçoivent une vue en lecture seule de `Obs` ; `Latent` n'est lisible qu'avec un jeton de mesure que les bras n'ont pas ; tout accès sans jeton lève `AccesLatent`.

**G2 — Base de v1 conservée.** 8 domaines × 5 articles, 2, 3 ou 4 champs tirés par monde, 3 opérateurs par groupe, moyeu d'opérateur à 25 %, 3 greffes, 3 jumeaux, vecteur de domaine par fréquences brutes (cosinus validés 0,54 / 0,28 / 0,03, B § 5), q uniforme sur [0,5 ; 1,5] **indépendante de la vérité**, étiquette de domaine juste à 0,95. Canal d'observation des opérateurs et des contraintes : celui de v1 (couverture 0,90 / 0,70 / 0,45 ; parasites 0,05 / 0,15 / 0,30 ; homonymes 0,05 / 0,10 / 0,20 pour « bien », « moyen », « mal »).

**G3 — Concepts de fond.** 10 concepts de fond F0 à F9, plus un concept moyeu H présent dans 30 % des articles (tirage indépendant). Chaque champ reçoit une **palette** de `taille_palette` concepts de fond tirés sans remise parmi les 10 (S16b) ; chaque article porte `nb_fonds` concepts de fond (S16c) tirés uniformément dans la palette de son champ. Ce tirage est **indépendant des opérateurs de l'article, de ses ponts et de la vérité** : le brouillon 1 attribuait un concept à chaque opérateur de groupe et déclarait « opérateur commun non moyeu ⟹ concept commun », ce qui faisait fabriquer par le générateur ce que N lit. **Neutralisation du κ = 1 sur un seul concept de fond (CB2-03).** Avec des vecteurs normés, deux articles de champs différents qui ne portent qu'un même concept de fond ont κ = 1, plus que tout vrai pont (κ ≈ 0,68 d'après la contre-lecture 2, ordre de grandeur sans simulation) ; avec deux concepts de fond par article (recommandation S16c), ce cas tombe à κ voisin de 0,5 et le cas κ = 1 exige de partager les deux. La neutralisation repose sur quatre dispositifs, dont aucun n'est réglé sur N : S16c ; la condition de jugeabilité J (S14), qui requalifie en « non concluant » un échec dû à un canal inexploitable ; N_filtre renforcé (S16f, § 4) ; la classe « fond partagé entre champs » mesurée parmi les 12 paires de chaque bras (Métrique). Elle ne supprime pas le défaut et son effet n'est pas mesuré avant les mondes de décision.

**G4 — Concepts rares.** Une réserve de 18 concepts rares R0 à R17, jamais dans une palette. Un concept rare n'est tiré que pour un pont planté (G6) ; au plus 6 + n_b + n_c + n_d sont utilisés par monde (15 aux comptes recommandés de S16e, donc la réserve suffit). Garde de configuration : 6 + n_b + n_c + n_d ≤ 18.

**G5 — Loi de rareté et émetteurs de surface.** Pour chaque concept rare r utilisé, le nombre latent d'émetteurs L_r est tiré selon la loi S16d, **la même pour tous les statuts de pont** (vrai, faux, proche). Deux des émetteurs sont les articles du pont ; les L_r − 2 autres sont des **émetteurs de surface** : articles tirés uniformément parmi les 38 autres, dont le texte emploie un mot de surface du concept sans le porter (leur concept latent est inchangé) ; le lexique étiquette ce mot comme r avec la même couverture que les autres. Un émetteur de surface ne crée **aucune vraie paire** : il ne porte pas r latent. La fréquence documentaire **observée** de l'étiquette r résulte de L_r, de la couverture, des parasites et de la fuite : elle est **mesurée** (V5), non tirée.

**G6 — Ponts plantés** (au plus 36 articles distincts sur 40 ; paires listées avec leur statut dans le monde ordinaire ; comptes n_b à n_e de S16e, recommandés 3 / 3 / 3 / 3) :
- (a) 3 greffes et 3 jumeaux de v1 (pont d'opérateur latent), vrais. Avec une probabilité λ (S16a) chacun, le pont est **aussi** exprimé par un concept rare latent commun aux deux articles (et par L_r − 2 émetteurs de surface, G5). Si le pont n'est pas exprimé, aucune étiquette de concept ne le relie.
- (b) n_b ponts conceptuels purs : deux articles de champs différents, à opérateurs propres de **noms différents** (aucun opérateur commun), sous un même concept rare latent ; contraintes rendues compatibles ; vrais.
- (c) n_c faux ponts : deux articles de champs différents, concept rare latent commun, contraintes vraies incompatibles (un axe + contre −) ; faux.
- (d) n_d ponts proches : deux articles d'un même champ (domaines différents), concept rare latent commun, contraintes compatibles ; faux en monde ordinaire, vrais en INV.
- (e) n_e ponts de surface : deux articles de champs différents dont un mot est étiqueté par le lexique d'opérateurs comme le même opérateur (homonymie de v1), opérateurs latents différents, aucun concept rare commun ; faux.
Les « homonymes rares de concept » du brouillon 1 sont remplacés par les émetteurs de surface de G5, qui jouent ce rôle pour tous les statuts. Aux comptes recommandés : 6 + 12 = 18 paires, 36 articles ; dans V_surface : (c) 2, (d) 2, (e) 5, soit 18 paires et 36 articles (S16e). Garde de configuration : 2 × (nombre de paires de ponts) ≤ 36.

**G7 — Couplage λ.** λ (S16a) dans toutes les conditions v2 sauf `M_couplage_faible` (λ_faible, S16a) ; sans objet en SP (aucun pont planté) et en NR (monde de v1). (b), (c), (d) portent toujours un concept rare ; seul (a) dépend de λ. SUPPOSÉ : ni 1 (circularité), ni 0 (aucune trace).

**G8 — Monde `M_inertes` (concepts inertes).** Pour chaque indice de monde m, mêmes latents (champs, opérateurs, contraintes, ponts, vérité) que le monde `M_bien` d'indice m : les **rôles 0 à 3 sont dérivés avec le code de condition 1** (celui de M_bien) et l'indice m, de sorte que les latents et l'observation des opérateurs, des concepts de fond, du moyeu et des contraintes sont égaux bit à bit à ceux de M_bien (CB2-01) ; seule la **couche d'observation des concepts rares est remplacée par un miroir**, dérivé avec le **code de condition 12 et le rôle 7** : pour chaque concept rare r, l'ensemble des L_r articles qui l'émettent (articles du pont et émetteurs de surface) est remplacé par L_r articles tirés uniformément parmi les 40, indépendamment des ponts, des champs et de la vérité. Les bras et les placebos d'un monde de M_inertes tirent avec le code de condition 12 (§ 7). Le canal d'observation, les fréquences documentaires et le nombre d'étiquettes par article y sont de même loi que dans M_bien. La vérité est inchangée (les ponts conceptuels purs deviennent invisibles). Ainsi la proximité conceptuelle observée y existe en même quantité et ne porte **aucune vérité**. **Portée, corrigée (CB2-01)** : c'est un contrôle de spécificité, **nécessaire mais faible**. Un bras qui suit κ y perd presque à coup sûr (les concepts rares tirés au hasard créent des paires leurres éloignées à fort κ) ; A8 ne prend donc en défaut que les gains tirés de lois que le miroir conserve (nombre d'étiquettes, fréquences, palettes liées aux champs, concepts de fond). Ce n'est pas « le seul monde » où une forme sans valeur conceptuelle peut être prise en défaut (la phrase du brouillon 2 est retirée) : N_PCg, SP et les bras artefacts contrôlent d'autres défauts. **Rapporté** (descriptif, sans verdict) : l'écart apparié Δ(N, N_β0 ; M_bien) − Δ(N, N_β0 ; M_inertes), monde à monde, sur des latents identiques.

**G9 — Canal d'observation des concepts.** Pour chaque concept émis (fond, moyeu, rare, y compris par un émetteur de surface) : (i) couverture : avec la probabilité c le mot est étiqueté, sinon il retombe dans le sac de domaine (fuite lexicale vers le vecteur de domaine, mesurée par F) ; (ii) fuite de domaine ρ : une étiquette couverte est remplacée, avec la probabilité ρ, par le concept de fond dominant du domaine de l'article (le plus fréquent parmi les articles du domaine, départage par indice) ; (iii) parasites : avec la probabilité p_par, l'article reçoit une étiquette supplémentaire tirée uniformément parmi les 28 concepts (fond et rares). Niveaux (c ; p_par ; ρ) : « bien » (0,85 ; 0,05 ; 0,05) ; « moyen » (0,65 ; 0,15 ; 0,15) ; « mal » (0,45 ; 0,30 ; 0,30). Deux mots de surface par concept, **indépendants du domaine**.

**G10 — Monde inversé INV.** Miroir exact de M_bien : la relation « éloignés / proches » est échangée pour tous les statuts. Les groupes d'opérateurs sont transversaux aux champs (miroir de v1) ; les **palettes de concepts de fond sont attachées aux groupes d'opérateurs transversaux**, non aux champs (symétrique de M, où elles sont attachées aux champs) ; les ponts (a) et (b), ainsi que (c) et (e), relient des domaines du même champ ; les ponts (d) deviennent des « ponts éloignés compatibles » (champs différents, concept rare commun, contraintes compatibles) et sont **faux**. Les concepts rares, la loi des émetteurs, λ et le canal sont ceux de M_bien. Vérité : même champ, domaines différents, pont latent commun non moyeu, contraintes compatibles.

**G11 — Échec de plantation.** Si un pont ne peut pas être planté après 1 000 essais, le monde est régénéré avec la tentative suivante (spawn_key étendue d'un compteur de tentative) ; le taux de régénération est rapporté et soumis à S11. Aucun pont n'est omis en silence.

**G12 — Étage de vérité unique.** La vérité est calculée par une seule fonction `vrai(i, j)` sur `Latent` ; la recette de plantation n'est pas relue. Les comptes par mécanisme (greffe, jumeau, pont conceptuel direct, expansion) sont dérivés de cette fonction et du registre des ponts plantés.

### 2. Étage commun (identique pour tous les bras)
Une paire est valide si : domaines observés différents ; filtre de compatibilité des contraintes **observées** passé ; partage d'**au moins une étiquette observée (opérateur ou concept)**. Le pont retenu est l'étiquette partagée la plus rare (fréquence documentaire observée ; départage par nom). Tous les bras voient les mêmes observations (R4).

### 3. Quantités du candidat
- cos_ij : cosinus observé des vecteurs de domaine (`cos` de v1).
- Vecteur de concepts de l'article i : étiquettes de concept **observées**, poids log(40 / fréquence documentaire observée), norme 1. κ_ij = produit scalaire, dans [0, 1]. **Vecteur nul : κ = 0, déclaré, compté et rapporté** (jamais NaN, jamais de repli silencieux, R5). Sur les mondes NR (v1), « concept » := étiquette d'opérateur observée (dit explicitement : ni Opus ni la synthèse ne disent comment N tourne sans concepts).
- Score de paire s_ij = (1 − cos_ij²)^e × (κ_ij + ε)^β × [q_i q_j seulement dans N_q].
- Strate : paire de domaines observés. Score de strate = plus fort s_ij de ses paires restantes.

### 4. Bras
Liste figée, dans cet ordre (le rang sert aux graines, § 7) : N, b, a, d1, d1c, c, b_eloigne, oracle, N_β0, N_α0, N_filtre, N_aleat, N_global, N_dpp, N_dpp_β0, N_fiches, N_q, N_rare, N_PC, N_PCg, N_grille.

| Code | Rôle | Définition |
|---|---|---|
| **N** | **candidat, forme commune retenue** | score s_ij, q ≡ 1, e = 8,5 ; β = 1 ; ε = 0,05 (a priori, § 5), **algorithme ci-dessous**. Aucun déterminant. |
| b | témoin | tirage stratifié de v1 (`stratifie`) |
| a | témoin | forme corrigée v6.3 de v1 (`corrige`, avec q), par la copie **gardée** de `ordre_glouton` (ci-dessous) |
| d1 | témoin | marche de Swanson par étiquette rare d'opérateur (v1) |
| d1c | témoin | même marche sur les étiquettes de concept (loi exacte, tirage sans remise parmi les paires valides) |
| c | référence | tirage uniforme parmi les paires valides |
| b_eloigne | témoin de référence | strates de cosinus moyen ≤ médiane d'abord (`stratifie_eloigne` de v1, observé) |
| oracle | plafond | vraies paires valides d'abord |
| N_β0 | ablation | β = 0 : domaine seul, même algorithme |
| N_α0 | ablation | e = 0 : concept seul, même algorithme |
| N_filtre | ablation, **renforcée (CB2-03)** | tour stratifié (b) servi par paliers, chaque palier en tours de strates jusqu'à 12 paires : (1) paires valides des strates éloignées (cosinus moyen observé ≤ médiane, comme `stratifie_eloigne`) dont l'étiquette de concept partagée la plus rare a une fréquence documentaire observée ≤ φ (S16f), c'est-à-dire la même information pondérée que d1c ; (2) si moins de 12, paires valides des strates éloignées qui partagent un concept (κ > 0) ; (3) si moins de 12, toutes les paires valides. Le nombre de paires prises à chaque palier est rapporté par monde |
| N_aleat | ablation | ordre des strates aléatoire (rebattu à chaque passage), meilleure paire par s_ij dans la strate |
| N_global | ablation | les 12 plus forts s_ij, sans strates (égalités par la graine du bras) |
| N_dpp | ablation, forme (O3) de l'avis d'Opus | ensemble de base = paires valides ; qualité de la paire = s_ij de N ; répulsion S^D ⊙ S^C et noyau L = diag(√s)(S^D ⊙ S^C)diag(√s) + γI, γ = 10⁻³, avec S^D(P, P') = (cos_ik cos_jl + cos_il cos_jk) / √((1 + cos_ij²)(1 + cos_kl²)) pour P = (i, j), P' = (k, l), et S^C(P, P') = ⟨ψ_P, ψ_P'⟩, ψ_P = (c̃_i ⊙ c̃_j) normé, ou le vecteur propre à la paire si elle ne partage aucun concept ; glouton `glouton_paires` (ci-dessous) ; **seule la règle de sélection diffère de N** |
| N_dpp_β0 | ablation (CB-16) | N_dpp avec β = 0 dans la qualité et S^C ≡ 1 : domaine seul, même glouton |
| N_fiches | ablation, option ⊙ de la question | noyau sur les fiches S_ij = cos_ij² · κ_ij², q ≡ 1, γ = 10⁻³, même chaîne que (a) (glouton gardé) |
| N_q | ablation, candidat d'Opus | N avec le facteur q_i q_j |
| N_rare | ablation, facteur de C | κ remplacé par la rareté de l'étiquette partagée la plus rare : log(40 / fréquence) / log(20) |
| N_PC | placebo intra-domaine | N sous le score permuté (§ 4 bis), permutation des vecteurs de concepts entre articles d'un **même domaine observé** |
| N_PCg | placebo hors domaine | N sous le score permuté, permutation des vecteurs de concepts entre **tous** les articles (fréquences d'étiquettes conservées) |
| N_grille | diagnostic | N réglé sur la grille du § 5 (non éligible) |

**Algorithme de N** (CB-06), comme `_tour_des_strates` de v1 :
1. Calculer s_ij pour toutes les paires valides.
2. Strates = paires non ordonnées de domaines observés contenant au moins une paire valide restante. Score de strate = plus fort s_ij de ses paires restantes.
3. **Passage** : trier les strates par score décroissant (égalités : ordre tiré par la graine du bras) ; dans chaque strate, accepter la paire de plus fort s_ij (égalités : tirage par la graine du bras) ; s'arrêter dès que 12 paires sont acceptées.
4. Si moins de 12 paires après le passage et s'il reste des paires valides : nouveau passage, **scores de strate recalculés sur les paires restantes**, même règle ; et ainsi de suite.
5. Un passage ne contient jamais deux paires d'une même strate. Une paire de domaines observés donne jusqu'à 28 strates pour 12 places : sauf monde pauvre, N prend la meilleure paire des 12 strates de plus fort score en un seul passage ; la « répulsion » entre paires est donc la seule séparation par strate.
6. Les générations n'ont aucun effet, pour tous les bras.

**§ 4 bis — placebos de concepts.** `placebo_score(monde, rng, portee)` permute les vecteurs de concepts entre articles : `portee` = « domaine observé » (N_PC, graine de rôle 4) ou « global » (N_PCg, graine de rôle 6) ; fréquences d'étiquettes conservées ; la permutation s'applique à tout vecteur ou graphe de concepts **utilisé pour classer ou tirer** par N ; l'étage commun garde les vraies étiquettes, donc les paires valides sont inchangées. Une même permutation par monde et par portée. d1c garde ses vraies étiquettes.

**Glouton nouveau `glouton_paires` (CB-03).** Cholesky incrémentale (Chen, Zhang et Zhou 2018, de mémoire, R7) : à chaque pas, calculer le pivot d_i² de chaque candidat restant ; choisir le plus grand ; si le pivot choisi est ≤ 10⁻¹² × max(diagonale), **lever `NonDefiniePositive`** (pas de saut du candidat, pas de sortie anticipée). Compter et rapporter le nombre de candidats à pivot ≤ 0 par monde. Avant le glouton, la décomposition de **tout** le noyau est faite par `cholesky` de la pièce A (qui lève). Le code des bras ne contient **aucun** `except` (ni `NonDefiniePositive`, ni générique) autour de ces appels : balayage statique (liste d'arrêt). `tirage_glouton` de la pièce A (qui attrape l'exception, saute le candidat et s'arrête sans rien dire) et `ordre_glouton` de v1 (pivot borné à 1e-300) **ne sont pas réutilisés tels quels**. Pour (a), a_q1 et N_fiches : copie gardée de `ordre_glouton`, numériquement identique tant que le pivot choisi reste > 0, qui lève sinon ; identité avec la version de v1 vérifiée sur 50 mondes (même ordre).

### 5. Hyperparamètres
- A priori (défaut D-d du recoupement, voir les nœuds ouverts) : e = 8,5 (règle : une paire à cos 0,28 pèse la moitié d'une paire à cos 0 ; (M) 8,49, accord avec l'exposant ≈ 17 de B et C et avec α = 8 d'Opus) ; β = 1 ; ε = 0,05 (règle : une paire sans concept partagé pèse environ le dixième d'une paire de κ = 0,5, (M) 0,09) ; γ = 10⁻³.
- Grille diagnostique (non éligible) : e ∈ {1, 2, 4, 8, 16} × β ∈ {0,5 ; 1 ; 2 ; 4}, sur 200 mondes de validation « moyen » seuls, scellée avant les mondes de décision ; elle ne change ni N ni le verdict. **Sortie de la grille** : les seuls écarts de chaque case à la case (e = 8, β = 1), écrits dans le fichier scellé du § 9 et **non imprimés** (CB2-09, qui relevait la contradiction avec le § 9) ; ni la précision de b ni Δ(N, b) ne sont imprimés (CB-17).

### 6. Conditions et validation du générateur

Les nombres de mondes sont ceux de S15 (hors NR : S7) ; ceux de M_bien et M_moyen sont étendus par S9 s'il y a lieu ; M_inertes prend celui de M_bien. Les paramètres de monde sont ceux de S16.

| Condition (code de graine) | Mondes | Définition |
|---|---|---|
| M_bien (1), M_moyen (2) | S15, S9 | niveaux bien et moyen du G9 ; paramètres S16 |
| M_mal (3) | S15 | niveau mal ; descriptive, abandonnée si le plafond de l'oracle < S8 |
| SP (4) | S15 | M_bien sans aucun pont planté ; vérité vide ; mesure : précision placebo (**contrôle de plomberie**, A3) |
| INV (5) | S15 | M_bien, monde inversé du G10 |
| V_fuite (6) | S15 | M_bien avec ρ = 0,6 |
| V_concepts_absents (7) | S15 | M_bien sans aucune étiquette de concept (κ = 0 déclaré ; N se réduit à N_β0 par la règle du § 3 : identité **déclarée d'avance** ; d1c non applicable) |
| V_moyeu_conceptuel (8) | S15 | concept moyeu à 0,6 |
| V_surface (9) | S15 | ponts de surface portés à n_e' et (c), (d) ramenés à n_c', n_d' (S16e : 36 articles de ponts) |
| NR_bien (10), NR_moyen (11) | S7 | `monde_v1.py` inchangé, graine de monde = premier mot de `SeedSequence(...).generate_state(1)` passé à `random.Random` ; concept := étiquette d'opérateur ; d1c ≡ d1 |
| **M_inertes (12)** | = n de M_bien | monde miroir du G8 sur les graines de M_bien (rôles 0 à 3 sous le code 1, miroir sous le code 12) |
| M_couplage_faible (13) | S15 | M_bien avec λ_faible (S16a) ; descriptive (dose-réponse P12) |
| M_palettes_communes (14) | S15 | M_bien avec `taille_palette` = 10 (tous les champs partagent les 10 concepts : proximité conceptuelle neutre au champ) ; descriptive |
| M_palettes_disjointes (15) | S15 | M_bien avec palettes disjointes (10 concepts répartis entre champs, au moins 2 par champ : le monde du brouillon 1) ; descriptive |

**Validation du générateur, avant toute méthode, sur graines distinctes (300 mondes « bien », 300 « moyen », 100 jumelles) ; seuils S13.** Formules :
- **V1** cosinus moyens, par paire d'articles du même domaine / de domaines proches / éloignés, moyennés sur les mondes.
- **V2 — fuite de domaine** F = ρ_S(κ_obs, cos_obs) − ρ_S(κ_lat, cos_obs), où ρ_S est la corrélation de rangs de Spearman calculée sur les 780 paires d'articles de chaque monde, puis moyennée sur les mondes « bien » ; κ_lat est le cosinus des vecteurs de concepts **latents** (même pondération par la fréquence documentaire latente). Elle mesure l'excès de lien entre proximité conceptuelle et proximité de domaine introduit par le canal d'observation, au-delà de celui, légitime, des palettes. Loi nulle rapportée : F après permutation des vecteurs de concepts observés entre articles d'un même domaine observé.
- **V3 — queue** : sur les paires valides d'un monde, part de paires du même champ parmi les 10 % de plus fort κ_obs, moins la même part parmi les 10 % de plus fort κ_lat ; moyenne sur les mondes.
- **V4 — jumelles** : le monde est régénéré en échangeant les mots propres de deux domaines pour les articles de ponts, mêmes latents et même flux de graines pour les rôles 1 à 3. Concordance = part des couples (article, étiquette de concept observée) identiques entre le monde et sa jumelle, sur les articles de ponts ; variation des cosinus = moyenne de |cos_obs(monde) − cos_obs(jumelle)| sur les paires plantées. **Ce test ne vérifie que l'absence de couplage dans le code** (par construction des flux de graines, la concordance est attendue proche de 1) ; il ne dit rien du vocabulaire réel, qui relève du préenregistrement sur fiches réelles.
- **V5** rareté appariée : pour chaque statut (vrai conceptuel, vrai d'opérateur, faux, proche, surface), fréquence documentaire observée moyenne de l'étiquette de pont retenue sur les paires plantées valides ; écart maximal entre statuts.
- **V6** vraies paires valides par monde, plafond de l'oracle (S8).
- **V7 (rapport sans seuil, CB-13)** : loi de κ observé et de cos observé par classe de paire — vrai conceptuel direct, vrai d'opérateur avec trace conceptuelle, vrai d'opérateur sans trace, faux pont, pont proche, paire d'émetteur de surface, fond partagé entre champs, fond partagé dans un champ — moyenne et déciles. Rapportée **avant** les méthodes, pour ne pas régler le monde sur N. **V7 est lu mais ne change rien** : aucun paramètre de monde n'est modifié après sa lecture ; si la loi de κ montre un monde mal réglé (par exemple des paires de fond partagé qui dominent les paires valides, ou un recouvrement des lois de κ entre vrai et faux pont), la conséquence est une version nouvelle du préenregistrement (R12), non un réglage (CB2-03).
- **V8 (rapport sans seuil)** : comptes de vraies paires par mécanisme (greffe, jumeau, pont conceptuel direct, expansion), taux d'exclusion, taux de régénération, nombre moyen de paires valides par monde et par condition (en v1 : 67,55 / 60,50 / 53,59).

### 7. Graines (R9)

- Chaque tâche reçoit `numpy.random.SeedSequence(entropy=RACINE, spawn_key=(code_condition, indice_monde, code_rôle))` (numpy ≥ 1.25) ; une régénération (G11) ajoute le numéro de tentative comme quatrième élément.
- Codes de condition : M_bien 1, M_moyen 2, M_mal 3, SP 4, INV 5, V_fuite 6, V_concepts_absents 7, V_moyeu_conceptuel 8, V_surface 9, NR_bien 10, NR_moyen 11, M_inertes 12, M_couplage_faible 13, M_palettes_communes 14, M_palettes_disjointes 15.
- Codes de rôle : monde 0 ; observation des opérateurs 1 ; observation des concepts 2 ; contraintes 3 ; placebo N_PC 4 ; placebo de SP 5 ; placebo N_PCg 6 ; miroir de M_inertes 7 ; bras 10 + rang du bras dans la liste figée du § 4 (N = 10, …, N_grille = 30) ; rééchantillonnage 99, avec `indice_monde` remplacé par le code du contraste.
- **Graines de `M_inertes` (CB2-01)** : pour l'indice de monde m (code de condition 12), les rôles 0 à 3 sont dérivés avec `spawn_key = (1, m, rôle)` (code de M_bien) ; le miroir avec `(12, m, 7)` ; les bras et placebos avec `(12, m, 10 + rang)`, `(12, m, 4)` et `(12, m, 6)`. Les indices m vont de 0 au nombre de mondes de M_bien moins un (extension de S9 comprise). Essai R5 : latents égaux à ceux de M_bien d'indice m (cas sain) ; code de condition 12 mis par erreur aux rôles 0 à 3, latents différents (artefact, détecté).
- **Rééchantillonnage (rôle 99) : codes de contraste (CB2-09).** `spawn_key = (code_condition, code_contraste, 99)` ; pour un écart entre deux ensembles de mondes distincts (14, 15), un second flux `(code_condition, code_contraste, 99, 1)` rééchantillonne le second ensemble ; pour un écart apparié par l'indice de monde (10), un seul flux sert aux deux. Le code de condition est celui où le contraste est calculé (celui de la première condition nommée pour 10, 14 et 15 : 12, 5, 6).
  - Décisifs : 1 Δ(N, b) ; 2 Δ(N, a) ; 3 Δ(N, d1) ; 4 Δ(N, d1c) ; 5 Δ(N, N_β0) ; 6 Δ(N, N_filtre) ; 7 Δ(N, N_PCg) ; 8 Δ(N_PCg, N_β0) ; 9 Δ(d1c, c) (J) ; 10 écart apparié Δ(N, N_β0 ; M_bien) − Δ(N, N_β0 ; M_inertes) ; 11 SP : N − b ; 12 SP : N − d1c ; 13 SP : N − N_β0 ; 14 Δ(N, b ; INV) − Δ(N, b ; M_bien) ; 15 Δ(N, b ; V_fuite) − Δ(N, b ; M_bien).
  - Descriptifs : 20 N − b_eloigne ; 21 N − N_aleat ; 22 N − N_global ; 23 N − N_dpp ; 24 N − N_fiches ; 25 N − N_q ; 26 N − N_rare ; 27 N − N_α0 ; 28 N − N_PC ; 29 N_dpp − N_dpp_β0 ; 30 N_PC − N_β0 ; 31 N_PC − N_PCg ; 32 N_dpp − N_global ; 33 b_eloigne − b ; 34 N_β0 − b ; 35 d1 − b ; 36 d1c − b ; 37 a − b ; 38 c − b ; 40 + rang du bras : précision moyenne d'un bras. Les contrastes 33 à 38 donnent la chaîne de cohérence de la section « Prédiction ».

- Manifeste par run (`src/controle_ia/manifeste.py`) : configuration et empreinte, versions de Python et de numpy, racines et clés de dérivation, empreintes du code, nombres de mondes (S15 et n' de S9), commit.

### 8. Comparaisons, multiplicité, puissance
- Contrastes décisifs (95 %) en M_bien et M_moyen : C1 Δ(N, b) ; C2 Δ(N, a), Δ(N, d1), Δ(N, d1c) ; C3 Δ(N, N_β0) ; C4 Δ(N, N_filtre) ; C5 placebo hors domaine : Δ(N, N_PCg) (95 %) et Δ(N_PCg, N_β0) (99 %) ; **C6 M_inertes** : Δ(N, N_β0) (95 %) ; **C7 jugeabilité** : Δ(d1c, c) (95 %) ; C8 SP (99 %, contrôle de plomberie) ; C9 INV ; C10 V_fuite ; C11 non-régression (99 %).
- Descriptifs (95 %) : N contre b_eloigne, N_aleat, N_global, N_dpp, N_fiches, N_q, N_rare, N_α0, N_PC, N_grille ; Δ(N_dpp, N_dpp_β0) ; Δ(N_PC, N_β0) ; Δ(N_PC, N_PCg) ; écart apparié M_bien − M_inertes ; chaîne de cohérence (contrastes 33 à 38) ; M_mal ; V_concepts_absents ; V_moyeu_conceptuel ; V_surface ; M_couplage_faible, M_palettes_communes, M_palettes_disjointes ; résultats par nombre de champs (2, 3, 4).
- Multiplicité : les règles d'adoption et de lecture sont des **conjonctions** (toutes les conditions doivent tenir), chacune à son niveau : pas de correction. Les contrôles à 99 % limitent les fausses alertes (M : quatre écarts indépendants, 3,9 % contre 18,5 % à 95 % ; trois écarts en SP : 3,0 %).

- Paires valides par monde : en v1, 67,55 / 60,50 / 53,59 (`daaef112…`) ; le budget de 12 en couvre environ le cinquième. À mesurer en v2, où l'étage commun s'élargit aux étiquettes de concept (en `M_inertes` et `M_palettes_communes`, nettement plus de paires valides, SUPPOSÉ ; rapporté par V8).
- Puissance : voir la section « Seuil ». Écart-type apparié de v1 : 15,0 à 15,3 (« bien »), 11,2 à 12,0 (« moyen ») (M). À 2 400 mondes : erreur type 0,31 (σ 15,3), demi-largeur 0,61 (95 %) et 0,80 (99 %) (script § 0 ; à 1 200 : 0,44, 0,87 et 1,14). La garde S9 vérifie l'écart-type de Δ(N, b) en v2 et étend le nombre de mondes, sans arrêt.
- Coût : processeur seul, aucune dépense ; temps de quelques heures en Python avec numpy (SUPPOSÉ ; v1 : 93 s pour 4 000 mondes sans noyau sur les paires ; ici 15 600 mondes aux valeurs recommandées de S15 et S7, 22 800 au plus avec l'extension de S9, noyaux sur les paires pour N_dpp et N_dpp_β0).

### 9. Ordre d'exécution
Contre-lecture 2 (faite) puis 3 si demandée → gel de S1 à S16 par Lazar (ligne datée dans `registres/decisions.md`) → remplacement des marqueurs et scellement → écriture du code → tests de gardes (liste d'arrêt) → validation du générateur (V1 à V8) → méthodes sur 200 mondes de validation de M_bien et de M_moyen : la console ne reçoit que l'écart-type σ̂ de Δ(N, b), le drapeau de S9 et le nombre de mondes n' qui en résulte (consigné au manifeste avant le premier monde de décision) ; les moyennes de Δ(N, b) en validation et la grille sont écrites dans un fichier **scellé** (empreinte), non ouvert avant le verdict (CB-17) → mondes de décision (n' compris) → lecture par un sous-agent neuf (R13), qui ouvre alors le fichier de validation.

### 10. Hors périmètre
- Passage sur les vraies fiches de la course 2 : préenregistrement distinct, lecture **descriptive** (environ 20 paires par bras selon l'avis d'Opus ; 128 à 300 fusions par bras selon la synthèse pour un effet de +10 points), sans sélection sur le verdict (N-053, contenu non lu par l'auteur : SUPPOSÉ), précédé d'une mesure de séparabilité sur les paires de fiches réelles. Source des concepts sur fiches réelles (D-e) : décision séparée.
- Aucun appel de modèle, aucune fusion : la précision mesure le tirage, pas les filles (B § 6).

## Critères de lecture gelés

Un sous-agent neuf (ni auteur du présent préenregistrement ni de l'analyse, R13) applique ces tables telles qu'elles sont écrites. Les seuils S1 à S16 sont gelés avant scellement. « Les deux » = M_bien et M_moyen. Chaque table se lit **de haut en bas : la première ligne dont la condition est vraie décide** ; les conditions des lignes suivantes supposent les précédentes fausses, de sorte que les lignes sont exclusives et exhaustives (la dernière ligne est le complémentaire).

**Booléens** (X ∈ {M_bien, M_moyen} ; Δ(·, · ; X) = écart apparié dans X ; lb95, ub95 = bornes basse et haute à 95 % ; lb99 = borne basse à 99 %) :
- V0 = validation du générateur passée (V1 à V6) ∧ aucun arrêt de la liste ∧ taux d'exclusion de chaque condition de décision ≤ taux S11 ∧ nombre de mondes exécuté de chaque condition = son nombre gelé (S15, S7) ou n' (S9) ;
- perd(X) = ub95 Δ(N, b ; X) < 0 ;
- A1(X) = estimation de Δ(N, b ; X) ≥ θ_abs ∧ r(N, b ; X) ≥ θ_rel ∧ lb95 Δ(N, b ; X) > 0 ;
- A2(X) = lb95 Δ(N, a ; X) > 0 ∧ lb95 Δ(N, d1 ; X) > 0 ∧ lb95 Δ(N, d1c ; X) > 0 ;
- suffit_d1c(X) = ub95 Δ(N, d1c ; X) ≤ 0 ; **suffit_d1(X) = ub95 Δ(N, d1 ; X) ≤ 0** (CB2-02, symétrique de suffit_d1c : sans elle, ub95 Δ(N, d1) ≤ 0 tombait dans « indécis ») ;
- A7(X) = lb95 Δ(N, N_β0 ; X) > seuil S3 (même contraste que P4) ;
- **J(X) = lb95 Δ(d1c, c ; X) > seuil S14** (canal jugeable : un bras simple qui lit les étiquettes de concept bat le tirage uniforme, sans N) ;
- A3 = dans SP, aucun des écarts N − b, N − d1c, N − N_β0 (précision placebo) n'a un intervalle à 99 % qui exclut 0 (contrôle de plomberie : fausse alerte de probabilité 0,03) ;
- A4 = ub95 (Δ(N, b ; INV) − Δ(N, b ; M_bien)) < 0 ;
- A5 = lb99 Δ(N, b ; NR_bien) ≥ marge S7 ∧ lb99 Δ(N, b ; NR_moyen) ≥ marge S7 ;
- A6 = ub95 (Δ(N, b ; V_fuite) − Δ(N, b ; M_bien)) < 0 ;
- A8 = dans M_inertes, lb95 Δ(N, N_β0) ≤ 0 ∧ ub95 Δ(N, N_β0) < δ_non (contrôle de spécificité, nécessaire mais faible) ;
- détecte(Δ, δ) : selon la règle S4 (R-A ou R-B) ;
- N0(X) = ub95 Δ(N, N_β0 ; X) < δ_non ; NF(X) = ub95 Δ(N, N_filtre ; X) < δ_non ;
- D0(X) = détecte(Δ(N, N_β0 ; X), δ) ; DF(X) = détecte(Δ(N, N_filtre ; X), δ) ;
- PG(X) = lb95 Δ(N, N_PCg ; X) > 0 ;
- gain_contrôle = (lb99 Δ(N_PCg, N_β0 ; X) > 0 pour au moins un X) ∨ (lb95 Δ(N, N_β0) > 0 dans M_inertes).

**Audit de symétrie (R4)**, déclenché par un résultat trop propre **ou** trop mauvais, un seul seuil pour les deux sens (S10) :
- |Δ(N, b ; X)| ≥ seuil S10 pour au moins un X ;
- précision de N ≥ (rapport S10) × précision de l'oracle dans une condition de décision ;
- N identique au bit près à N_global, N_β0 ou à un témoin **sur tous les mondes d'une condition**, hors identités déclarées d'avance (N ≡ N_β0 dans V_concepts_absents ; d1c ≡ d1 dans NR_bien et NR_moyen) ;
- un écart de contrôle excluant 0 : A3 en défaut, gain_contrôle ;
- fuite mesurée F exactement nulle (à 10⁻¹² près) ; concordance des étiquettes avec la vérité > 0,99.

Contenu de l'audit : relecture du code par un sous-agent neuf pour vérifier qu'aucune méthode ne lit un champ latent (lecture, exception `AccesLatent`, balayage statique) ; relance sur les graines de validation (RACINE_VALIDATION) ; test de permutation. **Issue** : « artefact trouvé » → verdict **non concluant** et version nouvelle du préenregistrement (R12) ; « aucun artefact » → les tables ci-dessous s'appliquent telles quelles, le rapport d'audit étant scellé.

### Table 1 — volet d'adoption

| # | Condition de la ligne | Verdict |
|---|---|---|
| 0 | V0 non tenue | **non concluant** ; aucune lecture des contrastes |
| 1 | un déclencheur d'audit est présent et l'audit n'est pas rendu | **non concluant** (audit en attente) |
| 2 | audit rendu, artefact trouvé | **non concluant** ; version nouvelle |
| 3 | perd(M_bien) ou perd(M_moyen) | **N perd contre le stratifié** ; N non adoptée |
| 4 | non (A1(M_bien) et A1(M_moyen)) | **N sous le seuil** ; N non adoptée |
| 5 | A3, A4, A5, A6 ou A8 non tenue, ou gain_contrôle | **contrôle en défaut** ; N non adoptée |
| 6 | suffit_d1c(M_bien) et suffit_d1c(M_moyen) | **« Swanson guidé par concepts suffit »** (issue permise) ; N non adoptée |
| 7 | suffit_d1(M_bien) et suffit_d1(M_moyen) | **« Swanson par opérateur suffit »** (issue permise) ; N non adoptée |
| 8 | non (J(M_bien) et J(M_moyen)) | **non concluant : canal non jugeable** ; aucune lecture du terme de concept ; N non adoptée à ce stade |
| 9 | non (A7(M_bien) et A7(M_moyen)) | **« l'éloignement suffit : N_β0 ou b_eloigne, pas N »**, ou le terme de concept n'est pas démontré, **le canal étant jugeable** ; N non adoptée |
| 10 | A2(M_bien) et A2(M_moyen) | **N adoptée, sous W1 à W4** (volet d'adoption ; le concept observé porte de la vérité par construction du monde) |
| 11 | tout autre cas | **indécis** |

### Table 2 — volet « ingrédient manquant, sous W1 à W4 »

| # | Condition de la ligne | Verdict |
|---|---|---|
| 0 | V0 non tenue | **non concluant** |
| 1 | un déclencheur d'audit est présent et l'audit n'est pas rendu | **non concluant** (audit en attente) |
| 2 | audit rendu, artefact trouvé | **non concluant** ; version nouvelle |
| 3 | gain_contrôle | **non** : un gain apparaît quand le concept est inerte ou permuté, donc il n'est pas celui de la valeur conceptuelle |
| 4 | non (J(M_bien) et J(M_moyen)) | **non concluant : canal non jugeable** (CB2-01) : un échec de N ne se lit pas comme « le concept n'apporte rien » |
| 5 | N0(M_bien) et N0(M_moyen) | **non** : le terme de concept n'apporte rien, **le canal étant jugeable** |
| 6 | D0(M_bien) et D0(M_moyen) et NF(M_bien) et NF(M_moyen) | **non** au sens de la question : le concept **suffit comme filtre** ; son entrée dans l'objectif n'apporte rien de plus |
| 7 | D0 et DF et PG dans les deux, et A8 | **oui, sous W1 à W4** : dans un monde où la proximité conceptuelle observée porte de la vérité, et seulement là, la proximité conceptuelle dans l'objectif apporte plus que l'éloignement seul et que le filtre. Ce verdict ne dit rien du monde réel |
| 8 | tout autre cas | **indécis** |

Notes de lecture : dans la Table 1, les lignes 6 et 7 se lisent dans cet ordre ; la ligne 8 (J) précède la ligne 9 (A7) parce qu'un échec de A7 n'a de sens que si le canal est jugeable. Dans la Table 2, les lignes 5 et 6 sont exclusives parce que N0 suppose une estimation < δ_non < δ et D0 une estimation ≥ δ ; les lignes 6 et 7 le sont parce que NF suppose une estimation < δ_non et DF une estimation ≥ δ. Les deux tables sont indépendantes : « N adoptée » peut coexister avec « indécis » sur l'ingrédient. Une valeur de N − N_filtre entre δ_non et δ donne « indécis ».

Lecture secondaire, sans effet sur le verdict : la valeur du second espace est Δ(N, N_α0) ; la place du déterminant sur les paires est Δ(N_dpp, N_global), Δ(N_dpp, N) et Δ(N_dpp, N_dpp_β0) (P13) ; la valeur de q est Δ(N_q, N) ; la part d'information de domaine et d'article, Δ(N_PC, N_PCg) et Δ(N, N_PC) ; la pente selon le couplage (P12) ; l'axe palettes (M_palettes_communes, M_palettes_disjointes) ; la chaîne de cohérence de la section « Prédiction » (contrastes 33 à 38 du § 7) ; l'écart apparié Δ(N, N_β0 ; M_bien) − Δ(N, N_β0 ; M_inertes) ; la part des 12 paires de chaque bras dont le seul concept partagé est un concept de fond.

Aucune lecture avant scellement ; rien de ces tables ne change après lecture ; toute déviation est écrite comme telle (R1). Le verdict est scellé puis soumis à Lazar pour GO (R13).

## Liste d'arrêt

| Condition | Action |
|---|---|
| Validation du générateur ratée (V1 à V6, plafond de l'oracle S8) | arrêt avant toute méthode ; correction par une nouvelle version du préenregistrement (R12) |
| Noyau non défini positif ou pivot choisi ≤ 0, détecté par `cholesky` du noyau entier ou par `glouton_paires` / la copie gardée (N_dpp, N_dpp_β0, N_fiches, a) | arrêt du bras et du run ; **jamais de repli silencieux** (R5) ; consigné |
| Balayage statique : un `except` (spécifique ou générique) autour d'un appel à `cholesky`, `glouton_paires` ou à la copie gardée dans le code des bras | arrêt : le code est refusé |
| NaN, division par zéro ou κ hors [0, 1] (tolérance 10⁻⁹) dans un score | arrêt |
| Vecteur de concepts nul non compté | arrêt |
| Accès d'un bras à `Latent` (`AccesLatent`) | arrêt du run ; audit R4 |
| Plafond de l'oracle < S8 en M_bien ou en M_moyen | arrêt : monde non jugeable |
| Écart-type σ̂ de Δ(N, b) sur les 200 mondes de validation > seuil S9, en « bien » ou en « moyen » | **pas d'arrêt** (CB2-06) : extension du nombre de mondes de la condition à n' (S9), calculée et consignée avant le premier monde de décision ; au plafond de 4 800 : exécution au plafond, erreur type atteinte rapportée |
| Nombre de mondes exécuté d'une condition différent de son nombre gelé (S15, S7) ou de n' (S9) | arrêt |
| Taux de mondes exclus > S11 dans une condition de décision | arrêt |
| Taux de mondes régénérés après échec de plantation > S11 | arrêt |
| Bras de sortie vide avant complément sur plus de S11 des mondes ; précision (placebo comprise) hors de [0 ; 1] | arrêt |
| Configuration de monde hors garde (S16e) : 2 × nombre de paires de ponts > 36, ou concepts rares requis > 18 | arrêt |
| Latents d'un monde de M_inertes différents de ceux du monde de M_bien de même indice (comparaison bit à bit) | arrêt |
| Écart de contrôle excluant 0 (SP, N_PCg, M_inertes) | audit R4 ; verdict « non concluant » tant que non rendu (SP : fausse alerte de probabilité 0,03, CB2-05) |
| Reproduction : moyennes de b, a, c, d1 sur NR_bien et NR_moyen hors de l'intervalle de B § 1 élargi de la marge S12 | arrêt : le code des témoins diffère de v1 |
| Appel de modèle, réseau ou dépense | arrêt (devis et GO exigés) |
| Lecture d'un résultat ou exécution d'une méthode avant scellement ; paramètre modifié après lecture ; ouverture du fichier de validation avant le verdict | arrêt et consignation de l'écart (R1) |
| numpy < 1.25 | arrêt (R9) |
| Marqueur de gel restant dans le texte, ou entrée « Contre-lecture k » sans ses deux empreintes | pas de scellement (**contrôlé** par le validateur `problemes`) |
| **Ligne de gel absente de `registres/decisions.md`, ou valeurs de la ligne différentes de celles du texte ; remarques de contre-lecture non traitées ; contre-lecture 3 ni faite ni déclarée superflue** | pas de scellement ; **contrôle manuel : le validateur ne vérifie ni la ligne de gel ni le traitement des remarques** (CB2-09) |
| Empreinte du code différente entre deux sessions d'un même run | arrêt |

**Gardes testées sur un cas sain et sur un artefact (R5)** avant les mondes de décision :
- **noyau non défini positif à travers le glouton** (CB-03) : `noyau_fautif` de la pièce A injecté dans `glouton_paires` doit lever `NonDefiniePositive` (et non rendre une sélection partielle) ; cas sain : noyau de la forme corrigée, sélection de 12 ; même essai sur la copie gardée de `ordre_glouton` ;
- **balayage statique** : un module de bras contenant `except NonDefiniePositive` est refusé ; cas sain : le module livré passe ;
- **bras qui lit la vérité** : un bras artefact qui demande `Latent` doit lever `AccesLatent` ; un bras artefact qui reçoit le jeton de mesure (score = indicatrice du vrai pont) doit enregistrer un gain proche du plafond **et** déclencher l'audit (précision ≥ 0,9 × oracle) ; cas sain : N s'exécute sans exception ;
- vecteur de concepts nul : κ = 0 compté et rapporté ; cas sain : monde jouet à la main à réponse connue ;
- abstention : un bras qui rend 8 paires est complété par 4 paires uniformes et `n_complete` = 4 ; cas sain : un bras qui rend 12 ;
- monde exclu : un monde construit avec 11 paires valides est exclu pour tous les bras ; cas sain : 12 paires valides ;
- échec de plantation : un paramétrage qui rend le pont (d) impossible provoque une régénération comptée, puis l'arrêt au-dessus du taux S11 ; cas sain : paramètres de décision ;
- monde jouet dont la précision des 12 paires est calculée à la main (vérification des estimateurs, du complément et des intervalles) ;
- reproduction de v1 : copies gardées de `ordre_glouton` identiques à la version de v1 sur 50 mondes.
- **extension de S9** (CB2-06) : σ̂ synthétique ≤ seuil, n' = n (cas sain) ; σ̂ = 20, n' = ⌈n × (20 / 15,3)²⌉ = 4 101 pour n = 2 400 ; σ̂ = 25, plafond de 4 800 atteint, rapporté, **sans arrêt** (artefact) ;
- **graine du monde inerte** (CB2-01) : latents de M_inertes d'indice m égaux à ceux de M_bien d'indice m, miroir différent (cas sain) ; code de condition 12 mis par erreur aux rôles 0 à 3 : latents différents, détecté (artefact) ;
- **garde de configuration S16e** : 18 paires et 15 concepts rares passent (cas sain) ; 19 paires de ponts, ou 7 / 4 / 4 / 4 ponts, sont refusés (artefact) ;
- **N_filtre** : monde jouet à réponse connue, paires aux fréquences ≤ φ au palier 1 prises d'abord (cas sain) ; monde où aucune paire ne passe le palier 1, passage déclaré aux paliers 2 puis 3 avec les nombres par palier rapportés (artefact : aucun repli silencieux) ;
- **jugeabilité J** : monde jouet où d1c bat c de façon connue, J vraie (cas sain) ; monde sans étiquette de concept (V_concepts_absents), d1c non applicable et J non calculée, déclarées (artefact).

## Contre-lecture

- **Contre-lecture 1** : sous-agent neuf, Opus 5.5 (`claude-opus-5-5`), non-auteur du brouillon, du recoupement, de la question, de l'avis d'Opus, de la synthèse, du code du pôle et de `trancher-recombinaison-v1`. Brouillon relu : `preenregistrement-bisociation-deux-espaces-v2-brouillon1.md`, empreinte `c9077cfe136269c8cf1a5fa8192153fccf48962aba8e276ac2a7e4dad89288e7`. Rapport : `bisociation-deux-espaces-v1/contre-lecture-preenregistrement-bisociation-v2-brouillon1.md`, empreinte `a31096c000213127ff191bba54adb47247280ba452464b07a036f07b7be527c4` (relevé 2026-10-30T00:53:13Z). Conclusion du rapport : non scellable en l'état (CB-01 à CB-05 majeurs), scellable après corrections, gel de tous les seuils par Lazar et nouvelle contre-lecture. Ni le brouillon 2 ni le brouillon 3 ne sont la version relue.

  Traitement de chaque remarque (accepté, refusé et pourquoi) :

  | Constat | Gravité | Traitement | Où |
  |---|---|---|---|
  | CB-01 circularité | majeure | accepté en entier : séparation vérité / observation, concepts de fond indépendants, λ, `M_inertes`, A8, P4 en contrôle de manipulation, verdict « oui, sous W1 à W4 » | Hypothèse ; G1 à G8 ; Table 2 |
  | CB-02 adoption sans concept | majeure | accepté : A7 et ligne 7 de la Table 1 | S3 ; Table 1 |
  | CB-03 repli silencieux | majeure | accepté : glouton nouveau, copie gardée, balayage statique, essais R5 à travers le glouton | § 4 ; liste d'arrêt |
  | CB-04 puissance des règles | majeure | accepté : deux options R-A et R-B avec leur puissance, tables aux centres de P1 à P5, σ 11 et 15,3, nombre de mondes | S4 ; section Seuil |
  | CB-05 générateur sous-spécifié | majeure | accepté : concepts rares réservés, loi {2, 3, 4} des émetteurs, comptes par mécanisme, INV spécifié, 30 articles sur 40 | G3 à G12 |
  | CB-06 ordre des strates | moyenne | accepté : algorithme de N pas à pas ; générations sans effet | § 4 ; Métrique |
  | CB-07 dénominateur et exclusions | moyenne | accepté : monde exclu défini sur les paires valides, complément déclaré, `n_complete` ; le contrôle de reproduction est inchangé car en v1 toutes les sorties faisaient 12 (11,995 en « mal ») | Métrique ; S11 |
  | CB-08 placebo de concepts | moyenne | accepté : une exigence par placebo, sens attendu de Δ(N_PC, N_β0) écrit, N_PCg ajouté | P7 ; § 4 bis ; Table 2 |
  | CB-09 table non mécanique | moyenne | accepté : deux tables à lignes exclusives et ordre de priorité, « N sous le seuil », issue de l'audit | Critères de lecture gelés |
  | CB-10 audit R4 | faible | accepté : un seuil pour les deux sens (S10), identités déclarées, portée « sur tous les mondes d'une condition » | S10 ; audit |
  | CB-11 marqueurs invisibles | moyenne | accepté : marqueur littéral du validateur à chaque seuil, tous les seuils gelés par Lazar en une ligne datée, sans défaut | Seuil ; Ligne de gel |
  | CB-12 P3 | faible | accepté : « + », confiance 0,40, « nul » nommé réfutation permise | P3 |
  | CB-13 échec pour raison de générateur | moyenne | accepté avec réserve : loi de κ par classe rapportée avant les méthodes (V7), dépendance écrite dans « ce que ce test ne dit pas », trois points sur l'axe palettes. Réserve : le sens du biais de N selon cet axe n'est pas connu avant mesure | Hypothèse ; V7 ; § 6 |
  | CB-14 validation non mécanique | moyenne | accepté : formules de F, de la queue et des jumelles ; séparation `Latent` / `Obs` par exception. Réserve : le test des jumelles ne vérifie que l'absence de couplage dans le code (dit au § 6) | § 1 G1 ; § 6 |
  | CB-15 chiffres et provenance | faible | accepté : chiffres de `daaef112…` ; recoupement § 5 à corriger dans sa version suivante (non modifié ici) ; texte de R-497 et R-500 cité | En-tête ; Seuil |
  | CB-16 factoriel | faible | accepté par l'ajout de N_dpp_β0 | § 4 ; P13 |
  | CB-17 coup d'œil sur la validation | faible | accepté : seule la garde S9 est imprimée ; moyennes et grille dans un fichier scellé, ouvert avec le verdict | § 5 ; § 9 |
  | (e) du rapport : précision hors [0 ; 1], bras vide > 2 % | — | accepté | Liste d'arrêt |
  | (g) du rapport : forme de la ligne de gel | — | accepté et étendue à S1 à S13 | Ligne de gel |

- **Contre-lecture 2** : sous-agent neuf, Opus 5.5 (`claude-opus-5-5`), modèle différent de l'auteur (Sonnet 5.5), **non-auteur** des brouillons 1 et 2, de la contre-lecture 1, du recoupement, de la question, de l'avis d'Opus, de la synthèse, du code du pôle et de `trancher-recombinaison-v1` (début 2026-10-30T01:13:22Z ; rédaction 2026-10-30T01:23:49Z). Brouillon relu : `preenregistrement-bisociation-deux-espaces-v2-brouillon2.md`, empreinte `36427069b1e8a91c2841d55add9787e8bfbc12daf1c6dd12e7efc75d2b293d91`. Rapport : `bisociation-deux-espaces-v1/contre-lecture-preenregistrement-bisociation-v2-brouillon2.md`, empreinte `71382fd9141965ced6604a671256508f37bec0e5cb36a91f8cd186b96677fb3b`. Conclusion du rapport : **scellable après corrections puis gel** (CB2-01, CB2-02 et CB2-04 avant le gel ; les autres sont mécaniques). Ce brouillon 3 n'est **pas** la version relue.

  Traitement de chaque remarque :

  | Constat | Gravité | Traitement | Où |
  |---|---|---|---|
  | CB2-01 circularité réduite, pas levée | majeure | accepté en entier : condition de jugeabilité J (S14) ; « N adoptée, sous W1 à W4 » ; graine du monde inerte cohérente avec le code 12 ; écart apparié M_bien − M_inertes rapporté ; phrase sur « le seul monde » corrigée ; J aussi dans la Table 1 (ajout de l'auteur) | Hypothèse ; G8 ; § 7 ; Tables 1 et 2 |
  | CB2-02 prédictions incohérentes, puissance d'adoption surestimée | majeure | accepté en entier : chaîne de cohérence, P1 et P2 recalés, P14 et P15, ligne suffit_d1, puissance d'A2 tabulée. **Réserve** : le recalage ancre les centres sur v1 (b_eloigne) et fait passer « N adoptée » de 0,03-0,04 à ≈ 0,9 ; il repose sur une seule donnée | Prédiction ; Table 1 ligne 7 ; Seuil |
  | CB2-03 une forme utile peut échouer pour une raison de générateur | moyenne | accepté avec réserve : J, N_filtre sur la même information pondérée (φ = S16f), V7 lu sans effet, classe « fond partagé » ; S16c (2 fonds par article) est une recommandation de l'auteur, effet non simulé | G3 ; § 4 ; V7 |
  | CB2-04 paramètres de monde sans source et hors gel | majeure (nœud) | accepté en entier : S16a à S16f et S15 au gel ; ponts 3 / 3 / 3 + 3 de surface (36 articles) ; V_surface à 2 / 2 / 5 | Seuil S15, S16 ; G4 à G7 |
  | CB2-05 le placebo sans pont ne contrôle que la plomberie | faible | accepté : SP dit contrôle de plomberie, A3 de fausse alerte 0,03, hors des contrôles d'artefact | Métrique ; Critères ; Liste d'arrêt |
  | CB2-06 S9, arrêt corrélé à la taille de l'effet | faible | accepté : extension automatique à n' = min(4 800 ; ⌈n (σ̂ / 15,3)²⌉), sans arrêt | S9 ; Liste d'arrêt |
  | CB2-07 S10 | faible | accepté : écrit ; avec P1 recalé, l'audit est quasi certain en « bien » (dit, non corrigé ; option 20 points) | S10 |
  | CB2-08 nombres de mondes de R-A | faible | accepté : 32 / 61 (conjoint 42 / 80), par script | Puissance |
  | CB2-09 divers | faible | accepté : « non imprimée » ; codes de contraste énumérés (§ 7) ; le validateur ne contrôle pas la ligne de gel, dit et ajouté à la liste d'arrêt | § 5 ; § 7 ; Liste d'arrêt ; Ligne de gel |
  | (d) tables de lecture | — | accepté : J et suffit_d1 ajoutées ; notes d'exclusivité conservées (courtes) | Critères |
  | (e) ligne de gel incomplète | — | accepté : paramètres de monde, nombre de mondes par condition, action de S9, lecture de D-b, remarque sur le validateur | Ligne de gel |
  | (f) choix d'auteur | — | accepté : λ, palettes, loi des émetteurs, comptes par statut au gel ; 18 rares laissés à l'auteur | S16 |
  | Recommandation de seuils pour Lazar | — | écrite comme recommandations (S1 à S16) ; table de puissance recalculée par l'auteur du brouillon 3, écarts ≤ 0,02 | Seuil |

  Réserves propres à ce brouillon 3, soumises à la contre-lecture 3 : (1) P1, P2, P3, P14 et P15 sont recalées sur v1 par l'auteur : le recalage fait de « N adoptée » une issue probable, sur une seule donnée qui peut ne pas se transposer ; (2) S16c (exactement 2 concepts de fond) et S16f (φ = 4) sont des choix de l'auteur du brouillon 3, leur effet n'est pas simulé ; φ lit la loi des émetteurs du générateur ; (3) l'adoption exige désormais J (ajout de l'auteur) ; (4) les probabilités traitent les facteurs d'une conjonction comme indépendants et ignorent l'écart-type de Δ(N, N_β0) et de Δ(N, N_filtre) (inconnus) ; (5) avec P1 recalé, l'audit de S10 est quasi certain en « bien » ; (6) l'extension de S9 ne lit que σ̂, mais σ̂ croît avec l'effet : la fuite est limitée à un nombre de mondes ; (7) la table de la contre-lecture 2 est vérifiée sous ses propres centres, qui ne sont plus ceux du brouillon 3.

- Contre-lecture 3 : À REMPLIR — sous-agent neuf à désigner (ni auteur de ce brouillon, ni du brouillon 2, ni de la contre-lecture 2, ni des pièces), de préférence d'un modèle différent de l'auteur (Sonnet 5.5), **ciblée sur les ajouts de l'auteur du brouillon 3** (nœuds ouverts 3) ; empreinte du brouillon 3 relu, chemin et empreinte de son rapport, traitement de chaque remarque. Ou, si Lazar la juge superflue, une phrase de lui dans la ligne de gel, recopiée ici (écart à R2, consigné). Fichiers à lui donner explicitement : ce brouillon ; la contre-lecture 2 ; le brouillon 2 ; `calcul-puissance-bisociation-v2-brouillon3-v1.py` et sa sortie ; `resultats-trancher-recombinaison-v1.json` ; `prereg/gabarit-preregistrement-v1.md` et `src/controle_ia/prereg.py`. Interdits à lui rappeler : ni `donnees/`, ni branche git, ni `prereg/P3-consignes-v1.md`, ni `diag/*/traces`. Questions prioritaires : (1) la chaîne de cohérence et les centres recalés de P1 à P3, P14, P15 ; (2) J, dans la Table 1 comme dans la Table 2 ; (3) S16c et S16f ; (4) N_filtre renforcé ; (5) les graines de `M_inertes` ; (6) les tables de puissance.

## Ligne de gel pour Lazar

À dire par Lazar, après la lecture des sections « Seuil » (en particulier S16, la réserve des nœuds ouverts 5 et le recalage des prédictions) et « Critères de lecture gelés ». Texte exact de la ligne proposée, avec toutes les valeurs recommandées (un « go » suffit) :

> « Go, je gèle le préenregistrement de la recombinaison bisociative à deux espaces v2 aux valeurs recommandées. **Seuils** : S1, θ_abs = +4 points ; S2, θ_rel = ×1,20 ; S3, A7 = borne basse à 95 % de N − N_β0 supérieure à 0, dans M_bien et M_moyen ; S4, règle de détection R-A (estimation ≥ δ et borne basse à 95 % > 0) ; S5, δ = +2,5 points ; S6, δ_non = +1,5 point sur la borne haute à 95 % ; S7, non-régression = borne basse à 99 % de N − b supérieure ou égale à −2 points, sur 1 200 mondes pour NR_bien et pour NR_moyen ; S8, plafond de l'oracle ≥ 0,30 ; S9, écart-type de garde 18 points, **sans arrêt** : au-delà, le nombre de mondes de la condition passe à min(4 800 ; ⌈n × (σ̂ / 15,3)²⌉), M_inertes reprenant celui de M_bien ; S10, audit de symétrie à |écart| ≥ 12 points dans les deux sens et à précision de N ≥ 0,9 fois celle de l'oracle ; S11, arrêts en taux à 2 % (mondes exclus, mondes régénérés, bras vides) ; S12, marge de reproduction de 2 points ; S13, validation du générateur : cosinus moyens dans [0,51 ; 0,57], [0,25 ; 0,31] et [0,00 ; 0,06], fuite de domaine ≤ 0,10, excès de queue ≤ 0,10, jumelles à concordance ≥ 0,9 et variation de cosinus ≥ 0,2, rareté appariée à écart ≤ 0,5, vraies paires valides en « moyen » ≥ 6 ; S14, jugeabilité J = borne basse à 95 % de d1c − c supérieure à 0, dans M_bien et M_moyen. **Nombre de mondes (S15)** : 2 400 pour M_bien, M_moyen et le monde inerte M_inertes ; 600 pour le monde sans pont, INV et V_fuite ; 600 pour chacune des sept conditions descriptives (M_mal, V_concepts_absents, V_moyeu_conceptuel, V_surface, M_couplage_faible, M_palettes_communes, M_palettes_disjointes). **Paramètres de monde (S16)** : λ = 0,7 et λ_faible = 0,3 ; palettes de 4 concepts de fond sur 10 ; exactement 2 concepts de fond par article ; nombre d'émetteurs latents d'un concept rare uniforme sur {2, 3, 4}, le même pour tous les statuts de pont ; ponts : 3 greffes, 3 jumeaux, 3 conceptuels purs, 3 faux, 3 proches et 3 de surface (18 paires, 36 articles sur 40), et dans V_surface 2 faux, 2 proches et 5 de surface (36 articles) ; seuil de rareté du filtre φ = 4. **Lecture de D-b** : N (score de paire, un passage par strates, sans déterminant) est le candidat éligible ; le déterminant sur les paires (N_dpp, N_dpp_β0) est une ablation descriptive, jamais éligible. Les autres défauts de 48 heures D-a, D-c et D-d restent tels quels (q ≡ 1, ε = 0,05, e = 8,5, β = 1) ; D-g (1 200 mondes) est remplacé par S15. Les choix d'auteur non gelés (10 concepts de fond, moyeu à 30 %, 18 concepts rares, niveaux du canal) sont scellés avec le texte. **Contre-lecture 3** : demandée, ciblée sur les ajouts de l'auteur du brouillon 3 ; le scellement attend son rapport. Date et heure : à consigner dans `registres/decisions.md`. »

Pour changer une valeur : dire le numéro et la nouvelle valeur (par exemple « S1 = +5 », « S16c = 1 ou 2 concepts de fond », « contre-lecture 3 non demandée »), le reste suit. Au scellement, cette section est remplacée par la ligne effectivement dite, avec sa date, recopiée de `registres/decisions.md`, et chaque marqueur des sections « Seuil » et « Contre-lecture » est remplacé par la valeur gelée ou par le rapport de la contre-lecture 3.

**Ce que le validateur du dépôt (`src/controle_ia/prereg.py`, fonction `problemes`) contrôle, et ce qu'il ne contrôle pas (CB2-09).** Il vérifie la présence des huit sections exigées, l'absence du marqueur de gel dans le texte, l'absence de marqueurs de gabarit, et deux empreintes de 64 caractères par entrée « Contre-lecture k ». Il **ne vérifie pas** que la ligne de gel est consignée dans `registres/decisions.md`, que ses valeurs sont celles du texte, ni que les remarques de la contre-lecture sont traitées : ces trois contrôles sont manuels, avant `sceller_prereg`, et figurent dans la liste d'arrêt.

