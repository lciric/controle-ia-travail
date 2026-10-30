# Préenregistrement — la recombinaison bisociative à deux espaces sur mondes synthétiques — v2 — BROUILLON 2, NON SCELLÉ

**Squelette à contre-lire (contre-lecture 2, R2) puis à geler par Lazar, puis à sceller avant tout code d'expérience (R1). Aucune méthode, aucun monde n'a été exécuté. Chaque seuil porte le marqueur littéral du validateur du dépôt (voir la section « Seuil ») : tant qu'il en reste un dans le texte, `sceller_prereg` refuse de sceller. C'est la garde mécanique du gel (R5). Aucun défaut ne s'applique à un seuil.**

- Auteur du brouillon 2 : sous-agent, Sonnet 5.5 (`claude-sonnet-5-5`). A relu le brouillon 1, son rapport de contre-lecture et les pièces ci-dessous. **Ne peut pas être contre-lecteur** de ce brouillon.
- Date (UTC), relevé `date -u` au début de la rédaction : 2026-10-30T01:07:10Z.
- Commit du code d'analyse : aucun code à ce jour. Le code s'écrit **après** scellement ; son empreinte et son commit sont consignés au manifeste de chaque run avant le premier monde (R9).
- Documents qui font foi (chemins relatifs à `brouillons/canal-reprise-releve-v1/envois/pole-scientifique-automatique-v1/` ; SHA-256 recalculés par l'auteur du brouillon 2 le 2026-10-30 ; « lu » = lu par lui, « cité » = repris d'une pièce, non relu) :
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
  - `registres/decisions.md`, lignes R-497 et R-500 (lues ; le fichier est vivant, son empreinte au moment de la lecture est `f25477ce99042ab0e03571d482e8e3686c0009719035029c97209a0d6b9fc282`, donc le **texte** des lignes est cité ci-dessous, pas seulement leur numéro) :
    - R-497 (2026-10-29, Lazar, 13:12 heure de Paris) : « le brainstorming sur la bisociativité (produit scalaire × déterminant : maximiser le volume du parallélépipède entre deux directions, minimiser leur proximité conceptuelle) : c'était dans l'organisme v6.3.2, ça s'est perdu ? » ; proposition (a) retenue par défaut : champ « concepts mobilisés » au gabarit de fiche + « test préenregistré v2 de la recombinaison à deux espaces (volume des domaines × proximité des concepts), Swanson en comparateur, stratifié en témoin, seuil gelé » ;
    - R-500 (2026-10-29, Lazar, 13:23 heure de Paris, mot direct) : « des parents loin en domaine mais proches en concept : oui, pardon, je me suis trompé » ; bisociation = **loin en domaine, proche en concept** ; signe de β positif.
- Chiffres : tous les chiffres de v1 renvoient à `resultats-trancher-recombinaison-v1.json` (`daaef112…`) ou au rapport B (`72cff8a0…`). Ce qui est calculé par l'auteur du brouillon 2 est marqué (M), avec sa formule. Ce qui n'est dans aucune pièce est marqué SUPPOSÉ (R7).
- Références de dimensionnement de v1, rappelées sans servir de preuve (extraits de `daaef112…`, précisions en part de 12 paires) : tirage stratifié (b) 0,2033 (« bien ») et 0,1273 (« moyen ») ; marche de Swanson (d1) +3,5 et +3,8 points sur (b) ; strates dissemblables d'abord (b_eloigne) +11,9 et +6,6 ; b_eloigne en monde inversé −11,6 ; plafond de l'oracle 0,750 et 0,487 (0,278 en « mal ») ; paires valides par monde 67,55 (« bien »), 60,50 (« moyen »), 54,09 (« mal »), 53,59 (monde sans pont) ; vraies paires par monde 12,30 / 12,16 ; vraies paires **valides** 9,52 (« bien »), 5,97 (« moyen »), 3,34 (« mal »).

### Ce qui change par rapport au brouillon 1 (constat CB-xx → où)

1. **CB-01** — circularité. Le monde sépare vérité et observation (`Latent` et `Obs`, accès latent interdit aux bras) ; les concepts de fond sont indépendants de la vérité ; un pont d'opérateur ne laisse une trace conceptuelle qu'avec une probabilité λ (couplage) ; **nouvelle condition `M_inertes`** (mêmes concepts observés, aucune vérité) où N doit échouer à battre N_β0 (contrôle A8) ; **P4 est un contrôle de manipulation**, dit comme tel ; le verdict « oui » est renommé et ne vaut que sous W1 à W4.
2. **CB-02** — condition d'adoption **A7** (borne basse de Δ(N, N_β0) > 0 dans les deux) ; verdict « l'éloignement suffit » si A1 tient sans A7.
3. **CB-03** — glouton **nouveau** qui laisse remonter `NonDefiniePositive` ; la pièce A (`tirage_glouton` attrape l'exception) et `ordre_glouton` de v1 (pivot borné à 1e-300) ne sont pas réutilisés tels quels ; garde testée **à travers** le glouton et par balayage statique.
4. **CB-04** — la règle de détection est écrite en **deux options** avec leur puissance réelle ; tableaux de P(verdict) aux centres de P1 à P5 pour les écarts-types 11 et 15,3 ; nombre de mondes qui donne 0,8.
5. **CB-05, CB-13** — générateur révisé : concepts rares réservés aux ponts, nombre latent d'émetteurs tiré dans {2, 3, 4} pour tous les statuts, vraies paires comptées par mécanisme (expansion comprise), monde inversé spécifié, proximité conceptuelle propre au champ **mesurée** (loi de κ par classe, avant les méthodes) et **neutralisée** dans une condition descriptive. Le brouillon 1 plantait 21 paires de ponts (6 de v1 et 5 statuts de 3 paires), soit 42 articles distincts dans un vivier de 40, sans dire comment : le nombre de ponts est ramené à 15 paires, soit 30 articles.
6. **CB-06** — algorithme de N écrit pas à pas (un seul passage sur le budget de 12, pas de remise à zéro par génération ; les générations n'ont aucun effet, pour tous les bras).
7. **CB-07** — « monde exclu » défini sur les paires valides (indépendant des bras), taux d'exclusion mesuré ; abstention interdite (complément déclaré, `n_complete` rapporté).
8. **CB-08** — placebo **hors domaine** `N_PCg` (permutation globale entre articles) ajouté à `N_PC` (permutation intra-domaine) ; une seule exigence par placebo ; sens attendu de Δ(N_PC, N_β0) écrit avec sa raison.
9. **CB-09, CB-10** — deux tables de lecture (adoption, puis ingrédient) à lignes exclusives lues de haut en bas ; issue de l'audit écrite ; un seul seuil d'audit pour les deux sens ; identités déclarées d'avance.
10. **CB-11** — chaque seuil est un marqueur littéral du validateur jusqu'au gel ; l'inventaire S1 à S13 donne, pour chacun, la recommandation de l'auteur et sa raison sur une ligne à part ; section finale « Ligne de gel pour Lazar ».
11. **CB-12** — P3 : signe « + » (confiance 0,40), « nul » nommé comme réfutation permise.
12. **CB-14** — statistiques de validation écrites par formule ; séparation `Latent` / `Obs` mécanique (exception `AccesLatent`), testée sur un bras artefact et sur N.
13. **CB-15** — chiffres de v1 repris de `daaef112…` ; 67,5 / 60,5 / 53,6 paires valides (le « environ 43 » du brouillon 1 et du recoupement § 5 était faux, gonflé par l'inégalité de Jensen sur une moyenne de 6 / V) ; empreinte du recoupement ajoutée ; texte de R-497 et R-500 cité.
14. **CB-16** — ajout de `N_dpp_β0` : le « factoriel » est (règle de sélection : strates sans déterminant ou déterminant sans strates) × (β actif ou non).
15. **CB-17** — le code de validation ne rend que l'écart-type de garde et les écarts relatifs de la grille ; la moyenne de Δ(N, b) en validation est écrite dans un fichier scellé et lue avec le verdict.
16. **Ajouts de l'auteur** (hors rapport, à contre-lire) : non-régression recommandée à −2 points sur 1 200 mondes (la marge −1 sur 600 mondes passe avec une probabilité de 0,17 à 0,36 si N égale b : S7) ; `M_couplage_faible` (dose-réponse) ; `M_palettes_communes` et `M_palettes_disjointes` (axe champ-concept) ; reproduction des témoins par des copies **gardées**.

### Nœuds ouverts avant scellement

1. **Seuils S1 à S13** : à geler par Lazar, aucun défaut (section « Seuil »).
2. Défauts de 48 h du recoupement, pris sauf mot contraire de Lazar (échéance au plus tôt 2026-11-01T00:42Z, à confirmer dans `registres/decisions.md` avant scellement) : q ≡ 1 dans le candidat (D-a) ; factoriel de la règle de sélection (D-b, précisé en N_dpp_β0) ; facteur de concept (κ + ε)^β avec ε = 0,05 (D-c) ; exposants a priori e = 8,5, β = 1, grille en diagnostic (D-d) ; 1 200 mondes de décision (D-g).
3. Paramètres de monde fixés par l'auteur du brouillon 2, SUPPOSÉS et à contre-lire en priorité : λ = 0,7 ; palettes de 4 concepts sur 10 ; 18 concepts rares ; nombre de ponts par statut ; loi {2, 3, 4} des émetteurs.
4. Contre-lecteur 2 : sous-agent neuf, à désigner (section « Contre-lecture »).

## Hypothèse

**H-B2 (hypothèse de travail de la question `73a30ab7…` et de R-497, signe levé par R-500).** Sur des mondes synthétiques à vérité plantée **à deux espaces** (un espace de domaines, un espace de concepts sous-jacents, séparés), tirer les paires à recombiner par un **score de paire produit**, *loin en domaine* ET *proche en concept*, avec sélection par strate, apporte plus de vrais ponts que :
- (i) le tirage stratifié (b), (ii) la forme corrigée de la v6.3 (a), (iii) la marche de Swanson par étiquette rare d'opérateur (d1) et par étiquette de concept (d1c) ;
- (iv) ses propres ablations qui retirent le concept (N_β0) ou ne l'emploient que comme **filtre** (N_filtre).

Lecture en deux volets, plus un contrôle, à ne pas confondre :
- **volet d'adoption** : N (forme commune, définie au plan d'analyse) est-elle meilleure que les témoins, sous contrôles, **et** son terme de concept apporte-t-il quelque chose (A7) ? ;
- **volet « ingrédient manquant, sous W1 à W4 »** : dans un monde où le concept observé porte de la vérité, la proximité conceptuelle **dans l'objectif** apporte-t-elle quelque chose que ni l'éloignement seul ni le filtre ne donnent ? La réponse ne vaut **que sous W1 à W4** : elle ne dit pas que le concept apporte dans un monde réel ;
- **contrôle de manipulation** (P4) : N − N_β0 > 0 dans les mondes où le concept porte de la vérité montre seulement que l'instrument voit le canal de concepts. Il ne prouve rien sur la valeur du concept.

Hypothèses de travail du monde (SUPPOSÉES ; elles encodent l'hypothèse ; l'avis d'Opus et B § 6 le disent) :
- (W1) les concepts existent comme variables latentes séparées du domaine ;
- (W2) leur observation passe par un canal à trois niveaux (couverture, parasites, fuite de domaine) ;
- (W3) la vérité est « champs différents ET pont latent commun non moyeu ET contraintes vraies compatibles », où le pont latent est soit un opérateur (greffe ou jumeau, comme en v1), soit un concept rare (pont conceptuel pur) ;
- (W4) un pont d'opérateur laisse une trace conceptuelle avec une probabilité λ (couplage), et les concepts de fond, qui ne font jamais la vérité, sont indépendants des opérateurs et des ponts.

Le prix de W1 à W4 est mesuré par la condition `M_inertes` (concepts observés de même loi, sans aucun lien avec la vérité), par la dose-réponse sur λ, par V_fuite, V_concepts_absents, la non-régression sur les mondes v1 et la validation du générateur.

Ce que ce test ne dit pas (B § 6, étendu) :
- rien sur la qualité des fiches fusionnées par un modèle ; rien sur les vraies fiches (préenregistrement distinct, lecture descriptive) ;
- A1 et A2 dépendent de la façon dont le générateur lie le concept au champ (axe palettes : 4 sur 10 en décision ; communes et disjointes en descriptif). Une paire proche (même champ) partage souvent un concept de fond avec κ ≈ 1, alors qu'un vrai pont n'en partage qu'un parmi plusieurs ; selon l'axe, cela favorise ou défavorise N par rapport à d1c, qui ignore la distance ;
- les concepts rares marquent les ponts plantés de **tout** statut (vrai, faux, proche) : la rareté sépare « planté » de « non planté », pas « vrai » de « faux ». Cela avantage d1c, N et N_filtre de la même façon, et c'est le même mécanisme que celui qui fait gagner d1 en v1 ;
- λ n'est pas calibré sur un corpus réel : il fixe la force de l'hypothèse. La dose-réponse (M_inertes, M_couplage_faible, M_bien) en montre la pente, pas la valeur réelle.

Antériorité (R8) : **la forme n'est pas revendiquée comme inédite**. Le principe « proche en mécanisme, loin en domaine » est probablement occupé (Gentner 1983 ; Hope et collaborateurs 2017 ; Berthold 2012 ; Chan et collaborateurs 2018 — de mémoire, non vérifié sur PDF, R7). Seule la forme et son test à vérité plantée sont en jeu ; vérification d'antériorité avant toute revendication.

## Prédiction chiffrée et signe attendu

Ordres de grandeur SUPPOSÉS, ancrés sur les références de v1 rappelées en tête : borne basse = marche de Swanson (+3,5 ; +3,8), borne haute = strates dissemblables d'abord (+11,9 ; +6,6). Chaque ligne donne ce qui compterait comme réfutation ; les lignes sont lues symétriquement (R3, R4). Les sigles S1 à S13 renvoient à la section « Seuil ».

| # | Contraste | Signe | Ordre de grandeur | Réfutation de la prédiction |
|---|---|---|---|---|
| P1 | N − b, « bien » | + | +4 à +12 points | borne haute à 95 % < θ_abs (S1) ; < 0 : N perd |
| P2 | N − b, « moyen » | + | +2 à +7 points | idem |
| P3 | N − d1c (« bien », « moyen ») | + (confiance 0,40) | +1 à +5 points | borne haute à 95 % ≤ 0 dans les deux : « Swanson guidé par concepts suffit » ; **un résultat nul est une réfutation permise de P3**, nommée comme telle |
| P4 | N − N_β0 en M_bien, M_moyen : **contrôle de manipulation** | + | +3 à +8 points | borne haute < δ_non (S6) dans les deux : l'instrument ne voit pas le canal. Dit comme tel : P4 positif ne prouve rien sur la valeur du concept |
| P5 | N − N_filtre (concept dans l'objectif contre filtre) | + | +1 à +5 points | borne haute < δ_non dans les deux : « le concept suffit comme filtre » |
| P6 | **M_inertes** : N − N_β0 | ≤ 0 | −3 à 0 point | borne basse à 95 % > 0 (artefact, audit R4) ; ou borne haute ≥ δ_non (instrument trop imprécis) |
| P7 | placebos : N sous le vrai score − N_PCg (permutation globale) ; N_PCg − N_β0 ; N_PC − N_β0 | + ; ≤ 0 ; ≥ 0 | > 0 ; −5 à 0 ; 0 à +3 | Δ(N, N_PCg) borne basse ≤ 0 : le gain n'est pas de l'information conceptuelle ; Δ(N_PCg, N_β0) borne basse à 99 % > 0 : artefact (audit R4). Δ(N_PC, N_β0) ≥ 0 n'est **pas** une réfutation : voir la note sous la table |
| P8 | monde sans pont (SP) : N − b, N − d1c, N − N_β0, précision placebo | 0 | 0 | intervalle à 99 % excluant 0 : artefact |
| P9 | vérité inversée : Δ_INV − Δ_bien (Δ = N − b) | − | −5 à −20 points | borne haute ≥ 0 : N ne cible pas l'éloignement |
| P10 | fuite de domaine ρ = 0,6 : Δ_V_fuite − Δ_bien | − | −1 à −6 points | borne haute ≥ 0 : l'avantage ne vient pas des concepts |
| P11 | non-régression (mondes v1) : N − b | ≥ marge S7 | ≥ 0 attendu | borne basse à 99 % < marge S7 |
| P12 | dose-réponse de Δ(N, N_β0) selon le couplage : M_inertes < M_couplage_faible < M_bien | croissante | pente > 0 | descriptive : une pente non croissante est rapportée, sans verdict |
| P13 | descriptives : N_dpp − N ; N_global − N ; N_dpp − N_dpp_β0 ; palettes communes / disjointes contre M_bien | voir note | voir note | aucune réfutation de verdict (diagnostic) |

Notes :
- **Sens attendu de Δ(N_PC, N_β0)** (permutation à l'intérieur d'un domaine observé) : ≥ 0, de 0 à +3 points. Raison : N_PC garde la composition en concepts de chaque domaine ; si les concepts de fond suivent partiellement les champs (palettes de 4 sur 10), cette information de domaine est légitime et peut donner un petit gain sur N_β0 sans aucun artefact. Seul N_PCg, qui détruit aussi l'information de domaine en conservant les fréquences d'étiquettes, sert de test d'artefact.
- **Décomposition** : Δ(N, N_PCg) = information de domaine + information d'article ; Δ(N_PC, N_PCg) est la part de domaine ; Δ(N, N_PC) est la part d'article. Les trois sont rapportées.
- P13 : N_dpp − N ≤ 0 attendu (−6 à 0) ; |N_dpp − N_global| ≤ 1 ; Δ(N_dpp, N_dpp_β0) ≥ 0 comme Δ(N, N_β0) ; palettes communes : attendu en baisse pour N (le concept de fond y est partagé entre champs) ; palettes disjointes : attendu en hausse. Les signes de ces deux dernières sont SUPPOSÉS et non réfutables.
- Justification de P9 (M) : sur v1, le diagnostic d'éloignement passe de +11,9 à −11,6, soit −23,5 (B § 7.2) ; N mêle éloignement et concept, d'où une chute plus faible.
- Confiance de l'auteur du brouillon 2 (SUPPOSÉ) : 0,55 sur P1, 0,40 sur P3, 0,50 sur P4. L'avis d'Opus donne 0,45 pour « bat d1 sur les mondes étendus ».
- **Conséquence des prédictions sur la lecture** : si l'effet vrai est celui du centre de P2 (+4,5 en « moyen »), le seuil +5 (S1) n'est franchi qu'avec une probabilité de 0,06 à 0,13 (table de puissance, section « Seuil »). Les prédictions de l'auteur disent donc que « N adoptée » est une issue minoritaire, et que « N sous le seuil » est la plus probable.

## Métrique

**Unité** : le monde. **Budget** : 12 paires, tirées **en un seul passage** sur les mêmes 40 candidats (8 domaines × 5 articles). Les « 3 générations de 4 paires » de B et de v1 n'ont **aucun effet** ici, pour tous les bras sans exception (N_dpp compris) : v1 faisait déjà un seul tour sur le budget de 12 (`_tour_des_strates`). Une paire acceptée n'est plus retirée.

**Vrai pont** (latent, jamais lu par une méthode) : champs différents (monde inversé : même champ, domaines différents), pont latent commun non moyeu (un opérateur latent commun, ou un concept rare latent commun ; **jamais** un concept de fond ni le concept moyeu), contraintes vraies compatibles. La vérité est une fonction du seul `Latent`, calculée une fois par monde pour toutes les paires ; la recette de plantation (statut « vrai », « faux », etc.) n'a pas d'autre rôle que de la rendre vraisemblable.

**Vraies paires par mécanisme**, comptées et rapportées par monde et par condition : greffe, jumeau, pont conceptuel direct (planté), **expansion** (toute vraie paire non plantée : en v1, 12,3 vraies paires par monde pour 6 plantées, `daaef112…`, parce que tous les porteurs d'un opérateur importé sont vrais).

**Mondes exclus.** Un monde est exclu **pour tous les bras à la fois** si, avant l'exécution des bras, il a moins de 12 paires valides, ou (hors SP) aucune vraie paire valide. La décision ne dépend d'aucune sortie de bras. Le taux d'exclusion de chaque condition est rapporté ; au-dessus du taux S11 dans une condition de décision : arrêt.

**Précision (primaire)** : π(X, m) = (nombre de vrais ponts parmi les 12 paires de X dans le monde m non exclu) / **12**. Si la règle d'un bras rend moins de 12 paires (abstention), la suite est **complétée** par un tirage uniforme sans remise parmi les paires valides restantes (graine du bras) ; ce complément est **déclaré** : `n_complete` est rapporté par bras et par condition, et la précision, y compris la précision placebo, garde le dénominateur 12. Aucun bras n'est noté sur moins de 12 paires. Un bras déclaré non applicable d'avance (d1c dans V_concepts_absents, dans NR_bien et NR_moyen où d1c ≡ d1) est exclu de la condition, non noté zéro.

**Estimateurs** : moyenne sur les mondes non exclus ; écart apparié Δ(X, Y ; condition) = moyenne sur m de [π(X, m) − π(Y, m)] ; rapport r(X, Y) = moyenne de π(X) / moyenne de π(Y). Écarts entre conditions (INV, V_fuite contre « bien ») : ensembles de mondes distincts, rééchantillonnage indépendant des deux.

**Intervalles** : percentiles de 2 000 rééchantillonnages des mondes (appariés pour un écart). « Borne basse à 95 % » = percentile 2,5 ; « borne haute à 95 % » = percentile 97,5 ; « borne basse (ou haute) à 99 % » = percentile 0,5 (ou 99,5). Niveau 95 % pour les contrastes décisifs et les contrôles de non-gain de N_PCg, M_inertes ; niveau 99 % pour les contrôles placebo (SP, N_PCg − N_β0) et la non-régression. Graine : spawn_key (code de condition, code de contraste, 99), voir § 7.

**Secondaires (descriptifs)** : rappel ; rappel par mécanisme ; pièges tirés par classe (moyeu d'opérateur, moyeu de concept, surface, faux pont, pont proche, émetteur de surface, parasite, autre — classes de `mesures_v1.classe_pont` étendues) ; strates distinctes par paire ; **articles distincts parmi les 12 paires** ; part de paires éloignées et conceptuellement proches (latent, et observé) ; précision placebo en SP (part des paires tirées qui appartiennent à un ensemble de 6 paires valides tirées au hasard, graine propre au monde, indépendante des bras, comme en v1) ; `n_complete`, nombre de vecteurs de concepts nuls et de pivots non positifs par bras ; fuite mesurée de la validation ; **loi de κ observé par classe de paire** (voir § 6).

## Seuil

**Tous les seuils de ce préenregistrement sont des marqueurs de gel. Lazar les gèle en une ligne datée dans `registres/decisions.md` (texte proposé : section finale « Ligne de gel pour Lazar »). Aucun défaut ne s'applique, ni à 48 heures ni autrement.** Pour chaque seuil : la valeur (marqueur), puis, sur une ligne à part, la recommandation de l'auteur, puis sa raison. Les points sont des points de pourcentage de précision (0,01 = 1 point). Sauf mention, les seuils portent sur les conditions de décision M_bien et M_moyen, notées « les deux ».

**S1 — θ_abs, écart absolu d'adoption, contraste N − b, dans les deux**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : +5 points.
- Raison : seuil de l'avis d'Opus ; la marche de Swanson seule (+3,5 ; +3,8) ne le franchit pas, l'éloignement seul (+11,9 ; +6,6) le franchit, ce que A7 interdit de lire comme adoption ; +12 (v1) est hors d'atteinte et critiqué par les trois modèles.
- Autres options (non recommandées) : (a) +12, sans seuil relatif (continuité avec v1 ; ×1,59 en « bien » et ×1,94 en « moyen » sur b de v1, (M) 12 / 20,3 et 12 / 12,7) ; (c) synthèse : ×1,3 et Δ(N, b) ≥ Δ(b_eloigne, b) − 2, soit +6,1 et +3,8 pour ×1,3, +9,9 et +4,6 pour l'autre terme (M, sur les chiffres de v1).

**S2 — θ_rel, rapport d'adoption r(N, b), dans les deux**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : ×1,25.
- Raison : avis d'Opus ; sur les moyennes de v1, ×1,25 équivaut à +5,1 en « bien » (M, 0,25 × 20,3) donc coïncide avec S1, et à +3,2 en « moyen » (M, 0,25 × 12,7), donc ne lie pas là.

**S3 — A7, contraste d'apport du concept à l'adoption : borne basse à 95 % de Δ(N, N_β0) strictement supérieure à ce seuil, dans les deux**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : 0 (c'est-à-dire borne basse > 0).
- Raison : A7 sert à empêcher qu'un gain dû à l'éloignement seul soit lu comme l'adoption de N (CB-02) ; son rôle est la détection d'un signe, la taille de l'apport est jugée par δ dans le volet ingrédient.

**S4 — règle de détection « le concept apporte »** (notée détecte(Δ, δ)), à choisir entre deux options écrites
- Valeur : À REMPLIR — à geler par Lazar.
- Option R-A : détecte(Δ, δ) = vrai si estimation de Δ ≥ δ **et** borne basse à 95 % de Δ > 0 (formulation de l'avis d'Opus : « ≥ +3 et bornes basses > 0 »).
- Option R-B : détecte(Δ, δ) = vrai si borne basse à 95 % de Δ ≥ δ (durcissement du brouillon 1, non signalé alors).
- Recommandation de l'auteur : R-A.
- Raison : à 1 200 mondes, R-A atteint la puissance 0,8 dès que l'effet vrai vaut δ + 0,27 à 0,44 point, R-B dès δ + 0,89 à 1,46 point ((M), voir la table de puissance) ; avec les prédictions P4 et P5 mêmes de l'auteur, R-B rend « oui » presque inatteignable (probabilité 0,0006 si P4 vaut +5,5 et P5 +3).

**S5 — δ, apport minimal du concept pour « détecte »**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : +3 points.
- Raison : avis d'Opus (la synthèse proposait 2) ; au centre de P4 (+5,5) la détection est certaine ; δ égale le centre de P5 (+3), de sorte que N − N_filtre est lu à la frontière : la puissance y est de 0,5 par construction.

**S6 — δ_non, borne haute à 95 % sous laquelle « le concept n'apporte pas »**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : +2 points.
- Raison : avis d'Opus et synthèse ; δ_non < δ laisse une zone « indécis » entre 2 et 3 et rend les lignes « oui » et « non » exclusives.

**S7 — non-régression sur les mondes v1 (NR_bien, NR_moyen) : borne basse à 99 % de Δ(N, b) supérieure ou égale à la marge, et nombre de mondes**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : marge −2 points, 1 200 mondes pour NR_bien et pour NR_moyen.
- Raison : la marge −1 de l'avis d'Opus sur 600 mondes n'est franchie, si N égale simplement b (effet vrai 0), qu'avec une probabilité de 0,17 (écart-type 15,3) à 0,36 (écart-type 11) ; la marge −2 sur 1 200 mondes la porte à 0,98 (15,3) et 1,00 (11) ; une non-régression qui échoue quand rien ne régresse ne mesure rien ((M), table de puissance).

**S8 — plafond de l'oracle : précision de l'oracle supérieure ou égale à ce seuil, en M_bien et en M_moyen**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : 0,30.
- Raison : avis d'Opus ; en v1 l'oracle faisait 0,750 et 0,487, soit de la marge ; 0,278 en « mal » serait sous le seuil, ce qui concorde avec le statut descriptif de M_mal.

**S9 — écart-type de garde : écart-type de Δ(N, b) par monde sur 200 mondes de validation de M_bien et sur 200 de M_moyen, séparément, inférieur ou égal à ce seuil**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : 18 points.
- Raison : (M) reconstitué sur v1 d'après les demi-largeurs à 95 % de `daaef112…` (écart-type = demi-largeur × √400 / 1,96) : 15,0 à 15,3 en « bien » (Δ(d1, b), Δ(b_eloigne, b), Δ(a, b)), 11,2 à 12,0 en « moyen » ; 18 est 18 % au-dessus du maximum de v1, soit environ 3,5 erreurs types d'un écart-type estimé sur 200 mondes (erreur relative 1 / √(2 × 199) ≈ 5 %).

**S10 — seuils de l'audit de symétrie (R4)**
- Valeur : À REMPLIR — à geler par Lazar.
- Recommandation de l'auteur : |Δ(N, b)| ≥ 12 points dans les **deux sens** (gain ou perte), en M_bien ou en M_moyen ; précision de N ≥ 0,9 fois celle de l'oracle.
- Raison : un seul chiffre pour les deux signes (CB-10) ; 12 est le seuil d'adoption de v1, qu'aucune forme n'a atteint, de sorte qu'un résultat plus grand est assez anormal pour être audité ; 0,9 de l'oracle est un quasi-plafond.

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

### Puissance des règles écrites (M ; approximation normale ; formules données)

Erreur type = écart-type apparié / √n, intervalle à 95 % = estimation ± 1,96 erreur type. Écarts-types : 15,3 (maximum de v1 en « bien », et valeur de la garde de l'avis d'Opus) et 11 (v1 « moyen »). Les écarts-types de Δ(N, N_β0) et de Δ(N, N_filtre) ne sont **pas connus** (N et ses ablations sont corrélées : ils sont probablement plus petits) ; les tables sont donc prudentes. n = 1 200 sauf mention.

Probabilité d'obtenir « détecte » (δ = 3) selon l'effet vrai μ ; R-A : P(estimation ≥ max(δ ; 1,96 erreur type)) ; R-B : P(estimation ≥ δ + 1,96 erreur type) :

| μ (points) | R-A, écart-type 11 | R-A, 15,3 | R-B, 11 | R-B, 15,3 |
|---|---|---|---|---|
| 1 | 0,00 | 0,00 | 0,00 | 0,00 |
| 3 (centre P5) | 0,50 | 0,50 | 0,02 | 0,02 |
| 4 | 1,00 | 0,99 | 0,88 | 0,62 |
| 5,5 (centre P4) | 1,00 | 1,00 | 1,00 | 1,00 |
| 8 (haut de P4) | 1,00 | 1,00 | 1,00 | 1,00 |

- Effet vrai donnant la puissance 0,8 à 1 200 mondes : R-A, δ + 0,84 erreur type = 3,27 (écart-type 11), 3,37 (15,3), 3,44 (18) ; R-B, δ + 2,80 erreur type = 3,89 ; 4,24 ; 4,46.
- Nombre de mondes pour la puissance 0,8 à l'effet attendu : R-A, (0,84 σ / (μ − δ))² ; R-B, (2,80 σ / (μ − δ))². Pour la puissance conjointe 0,8 sur **deux** conditions, remplacer 0,84 par 1,25 (0,894 par condition). Au centre de P4 (5,5) : R-A 14 (σ 11) à 27 (σ 15,3) mondes, conjoint 30 à 58 ; R-B 152 à 294, conjoint 199 à 385. À μ = 4 : R-A 86 à 166, conjoint 188 à 365 ; R-B 950 à 1 837, conjoint 1 245 à 2 409. Au centre de P5 (3) : **aucun nombre de mondes ne suffit** (μ = δ) ; à μ = 3,5 : R-A 343 à 663 (conjoint 754 à 1 459), R-B 3 799 à 7 349.
- **Probabilité de « oui »** (quatre détections : N_β0 et N_filtre, dans les deux conditions) : P4 = 5,5 et P5 = 3 : R-A 0,25, R-B 0,0006. P4 = 5,5 et P5 = 4 : R-A 0,98 à 1,00, R-B 0,38 à 0,78. P4 = 5,5 et P5 = 5 : R-A 1,00, R-B 0,99 à 1,00.
- 1 200 mondes suffisent donc pour N − N_β0 sous les prédictions de l'auteur (centre +5,5) avec R-A ou R-B ; ils ne suffisent pas pour N − N_filtre à son centre (+3) : P5 est une prédiction à la frontière de δ, ce qui est la vraie limite du test, pas le nombre de mondes.

Probabilité de franchir A1 (estimation ≥ θ_abs et borne basse > 0) par condition, n = 1 200, selon l'effet vrai μ (écart-type 11 pour « moyen », 15,3 pour « bien ») :

| μ | θ_abs = 3, σ 11 / 15,3 | θ_abs = 4 | θ_abs = 5 |
|---|---|---|---|
| 2 | 0,00 / 0,01 | 0,00 / 0,00 | 0,00 / 0,00 |
| 4 | 1,00 / 0,99 | 0,50 / 0,50 | 0,00 / 0,01 |
| 4,5 (centre P2) | 1,00 / 1,00 | 0,94 / 0,87 | **0,06 / 0,13** |
| 5 | 1,00 / 1,00 | 1,00 / 0,99 | 0,50 / 0,50 |
| 6 | 1,00 / 1,00 | 1,00 / 1,00 | 1,00 / 0,99 |
| 8 (centre P1) | 1,00 / 1,00 | 1,00 / 1,00 | 1,00 / 1,00 |

- Avec S1 = 5 et les centres de P1 (8, « bien ») et de P2 (4,5, « moyen »), la conjonction de A1 dans les deux a une probabilité de 0,06 (σ 11) à 0,13 (σ 15,3). Le **seuil**, non le nombre de mondes, décide de la lecture de P2 : aucun n ne permet la puissance 0,8 pour μ ≤ θ_abs. C'est le prix du choix de S1 ; il est dit ici pour que Lazar le voie. Un S1 plus bas (4 ou 3) laisse passer davantage de cas où l'éloignement seul suffit, ce que A7 doit alors arrêter seul.

Non-régression (borne basse à 99 % ≥ marge) :

| n, écart-type | marge −1, μ = 0 | marge −1, μ = +1 | marge −2, μ = 0 | marge −2, μ = +1 |
|---|---|---|---|---|
| 600, 11 | 0,36 | 0,97 | 0,97 | 1,00 |
| 600, 15,3 | 0,17 | 0,73 | 0,73 | 0,99 |
| 1 200, 11 | 0,72 | 1,00 | 1,00 | 1,00 |
| 1 200, 15,3 | 0,38 | 0,98 | 0,98 | 1,00 |

M_inertes : P(borne haute à 95 % de Δ(N, N_β0) < δ_non = 2 | μ = 0) = 0,995 (1 200 mondes, σ 15,3) et 0,89 (600 mondes, σ 15,3) ; faux positif (borne basse > 0 | μ = 0) = 0,025. D'où 1 200 mondes pour M_inertes. INV : l'erreur type de Δ_INV − Δ_bien (600 et 1 200 mondes, σ 15,3) est 0,77 ; P(borne haute < 0 | μ = −5) = 1,00, | μ = −3 : 0,98, | μ = −1 : 0,26 (bas de P10 : peu de puissance, dit).

**Taux d'erreur visés** : intervalles à 95 % (décisifs) et à 99 % (placebo, non-régression). Multiplicité : voir le plan d'analyse, § 8.

## Plan d'analyse

### 1. Générateur `monde_v2.py` (nouveau nom, R12 ; étend `monde_v1.py` `af907b1d…`)

Nombres SUPPOSÉS, repris de l'avis d'Opus § 3 sauf mention.

**G1 — Séparation vérité / observation.** Un monde est une paire (`Latent`, `Obs`). `Obs` contient, pour chaque article : le sac de mots de domaine, l'ensemble des étiquettes d'opérateur observées, l'ensemble des étiquettes de concept observées (noms disjoints de ceux des opérateurs : préfixes `op:` et `co:`), les contraintes observées, le domaine observé, l'aptitude q ; la matrice `cos` des cosinus de domaine ; les fréquences documentaires observées. `Latent` contient : champs, groupes d'opérateurs, opérateurs et moyeux, tous les concepts latents, contraintes vraies, ponts plantés et leur statut, **provenance des étiquettes** (vrai, homonyme, parasite, moyeu : ce sont des champs latents), vérité. Les bras reçoivent une vue en lecture seule de `Obs` ; `Latent` n'est lisible qu'avec un jeton de mesure que les bras n'ont pas ; tout accès sans jeton lève `AccesLatent`.

**G2 — Base de v1 conservée.** 8 domaines × 5 articles, 2, 3 ou 4 champs tirés par monde, 3 opérateurs par groupe, moyeu d'opérateur à 25 %, 3 greffes, 3 jumeaux, vecteur de domaine par fréquences brutes (cosinus validés 0,54 / 0,28 / 0,03, B § 5), q uniforme sur [0,5 ; 1,5] **indépendante de la vérité**, étiquette de domaine juste à 0,95. Canal d'observation des opérateurs et des contraintes : celui de v1 (couverture 0,90 / 0,70 / 0,45 ; parasites 0,05 / 0,15 / 0,30 ; homonymes 0,05 / 0,10 / 0,20 pour « bien », « moyen », « mal »).

**G3 — Concepts de fond.** 10 concepts de fond F0 à F9, plus un concept moyeu H présent dans 30 % des articles (tirage indépendant). Chaque champ reçoit une **palette** de 4 concepts de fond tirés sans remise parmi les 10 (paramètre `taille_palette` = 4) ; chaque article porte 1 concept de fond (probabilité 0,6) ou 2 (0,4), tirés uniformément dans la palette de son champ. Ce tirage est **indépendant des opérateurs de l'article, de ses ponts et de la vérité** : le brouillon 1 attribuait un concept à chaque opérateur de groupe et déclarait « opérateur commun non moyeu ⟹ concept commun », ce qui faisait fabriquer par le générateur ce que N lit.

**G4 — Concepts rares.** Une réserve de 18 concepts rares R0 à R17, jamais dans une palette. Un concept rare n'est tiré que pour un pont planté (G6) ; au plus 13 sont utilisés par monde.

**G5 — Loi de rareté et émetteurs de surface.** Pour chaque concept rare r utilisé, le nombre latent d'émetteurs L_r est tiré uniformément dans {2, 3, 4}, **par la même loi pour tous les statuts de pont** (vrai, faux, proche). Deux des émetteurs sont les articles du pont ; les L_r − 2 autres sont des **émetteurs de surface** : articles tirés uniformément parmi les 38 autres, dont le texte emploie un mot de surface du concept sans le porter (leur concept latent est inchangé) ; le lexique étiquette ce mot comme r avec la même couverture que les autres. Un émetteur de surface ne crée **aucune vraie paire** : il ne porte pas r latent. La fréquence documentaire **observée** de l'étiquette r résulte de L_r, de la couverture, des parasites et de la fuite : elle est **mesurée** (V5), non tirée.

**G6 — Ponts plantés** (30 articles distincts sur 40 ; paires listées avec leur statut dans le monde ordinaire) :
- (a) 3 greffes et 3 jumeaux de v1 (pont d'opérateur latent), vrais. Avec une probabilité λ chacun, le pont est **aussi** exprimé par un concept rare latent commun aux deux articles (et par L_r − 2 émetteurs de surface, G5). Si le pont n'est pas exprimé, aucune étiquette de concept ne le relie.
- (b) 3 ponts conceptuels purs : deux articles de champs différents, à opérateurs propres de **noms différents** (aucun opérateur commun), sous un même concept rare latent ; contraintes rendues compatibles ; vrais.
- (c) 2 faux ponts : deux articles de champs différents, concept rare latent commun, contraintes vraies incompatibles (un axe + contre −) ; faux.
- (d) 2 ponts proches : deux articles d'un même champ (domaines différents), concept rare latent commun, contraintes compatibles ; faux en monde ordinaire, vrais en INV.
- (e) 2 ponts de surface : deux articles de champs différents dont un mot est étiqueté par le lexique d'opérateurs comme le même opérateur (homonymie de v1), opérateurs latents différents, aucun concept rare commun ; faux.
Les « homonymes rares de concept » du brouillon 1 sont remplacés par les émetteurs de surface de G5, qui jouent ce rôle pour tous les statuts.

**G7 — Couplage λ.** λ = 0,7 dans toutes les conditions v2 sauf `M_couplage_faible` (λ = 0,3) ; sans objet en SP (aucun pont planté) et en NR (monde de v1). (b), (c), (d) portent toujours un concept rare ; seul (a) dépend de λ. SUPPOSÉ : ni 1 (circularité), ni 0 (aucune trace).

**G8 — Monde `M_inertes` (concepts inertes).** Même graine et mêmes latents (champs, opérateurs, contraintes, ponts, vérité) que le monde `M_bien` correspondant ; seule la **couche d'observation des concepts rares est remplacée par un miroir** : pour chaque concept rare r, l'ensemble des L_r articles qui l'émettent (articles du pont et émetteurs de surface) est remplacé par L_r articles tirés uniformément parmi les 40, indépendamment des ponts, des champs et de la vérité. Les concepts de fond, le moyeu, le canal d'observation, les fréquences documentaires et le nombre d'étiquettes par article sont de même loi. La vérité est inchangée (les ponts conceptuels purs deviennent invisibles). Ainsi la proximité conceptuelle observée y existe en même quantité et ne porte **aucune vérité** : c'est le seul monde où une forme sans valeur conceptuelle peut être prise en défaut (CB-01).

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
| N_filtre | ablation | tour stratifié (b) parmi les paires valides de strates éloignées (cosinus moyen ≤ médiane) qui partagent un concept (κ > 0) ; puis, si moins de 12, le reste en tour stratifié (b) |
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
- Grille diagnostique (non éligible) : e ∈ {1, 2, 4, 8, 16} × β ∈ {0,5 ; 1 ; 2 ; 4}, sur 200 mondes de validation « moyen » seuls, scellée avant les mondes de décision ; elle ne change ni N ni le verdict. **Sortie de la grille** : les seuls écarts de chaque case à la case (e = 8, β = 1) ; ni la précision de b ni Δ(N, b) ne sont imprimés (CB-17).

### 6. Conditions et validation du générateur

| Condition (code de graine) | Mondes | Définition |
|---|---|---|
| M_bien (1), M_moyen (2) | 1 200 chacune | niveaux bien et moyen du G9 ; λ = 0,7 ; palettes de 4 |
| M_mal (3) | 600 | niveau mal ; descriptive, abandonnée si le plafond de l'oracle < S8 |
| SP (4) | 600 | M_bien sans aucun pont planté ; vérité vide ; mesure : précision placebo |
| INV (5) | 600 | M_bien, monde inversé du G10 |
| V_fuite (6) | 600 | M_bien avec ρ = 0,6 |
| V_concepts_absents (7) | 600 | M_bien sans aucune étiquette de concept (κ = 0 déclaré ; N se réduit à N_β0 par la règle du § 3 : identité **déclarée d'avance**) |
| V_moyeu_conceptuel (8) | 600 | concept moyeu à 0,6 |
| V_surface (9) | 600 | 5 ponts de surface au lieu de 2 (36 articles de ponts sur 40) |
| NR_bien (10), NR_moyen (11) | 1 200 chacune (S7) | `monde_v1.py` inchangé, graine de monde = premier mot de `SeedSequence(...).generate_state(1)` passé à `random.Random` ; concept := étiquette d'opérateur ; d1c ≡ d1 |
| **M_inertes (12)** | 1 200 | monde miroir du G8 sur les graines de M_bien |
| M_couplage_faible (13) | 600 | M_bien avec λ = 0,3 ; descriptive (dose-réponse P12) |
| M_palettes_communes (14) | 600 | M_bien avec `taille_palette` = 10 (tous les champs partagent les 10 concepts : proximité conceptuelle neutre au champ) ; descriptive |
| M_palettes_disjointes (15) | 600 | M_bien avec palettes disjointes (10 concepts répartis entre champs, au moins 2 par champ : le monde du brouillon 1) ; descriptive |

**Validation du générateur, avant toute méthode, sur graines distinctes (300 mondes « bien », 300 « moyen », 100 jumelles) ; seuils S13.** Formules :
- **V1** cosinus moyens, par paire d'articles du même domaine / de domaines proches / éloignés, moyennés sur les mondes.
- **V2 — fuite de domaine** F = ρ_S(κ_obs, cos_obs) − ρ_S(κ_lat, cos_obs), où ρ_S est la corrélation de rangs de Spearman calculée sur les 780 paires d'articles de chaque monde, puis moyennée sur les mondes « bien » ; κ_lat est le cosinus des vecteurs de concepts **latents** (même pondération par la fréquence documentaire latente). Elle mesure l'excès de lien entre proximité conceptuelle et proximité de domaine introduit par le canal d'observation, au-delà de celui, légitime, des palettes. Loi nulle rapportée : F après permutation des vecteurs de concepts observés entre articles d'un même domaine observé.
- **V3 — queue** : sur les paires valides d'un monde, part de paires du même champ parmi les 10 % de plus fort κ_obs, moins la même part parmi les 10 % de plus fort κ_lat ; moyenne sur les mondes.
- **V4 — jumelles** : le monde est régénéré en échangeant les mots propres de deux domaines pour les articles de ponts, mêmes latents et même flux de graines pour les rôles 1 à 3. Concordance = part des couples (article, étiquette de concept observée) identiques entre le monde et sa jumelle, sur les articles de ponts ; variation des cosinus = moyenne de |cos_obs(monde) − cos_obs(jumelle)| sur les paires plantées. **Ce test ne vérifie que l'absence de couplage dans le code** (par construction des flux de graines, la concordance est attendue proche de 1) ; il ne dit rien du vocabulaire réel, qui relève du préenregistrement sur fiches réelles.
- **V5** rareté appariée : pour chaque statut (vrai conceptuel, vrai d'opérateur, faux, proche, surface), fréquence documentaire observée moyenne de l'étiquette de pont retenue sur les paires plantées valides ; écart maximal entre statuts.
- **V6** vraies paires valides par monde, plafond de l'oracle (S8).
- **V7 (rapport sans seuil, CB-13)** : loi de κ observé et de cos observé par classe de paire — vrai conceptuel direct, vrai d'opérateur avec trace conceptuelle, vrai d'opérateur sans trace, faux pont, pont proche, paire d'émetteur de surface, fond partagé entre champs, fond partagé dans un champ — moyenne et déciles. Rapportée **avant** les méthodes, pour ne pas régler le monde sur N.
- **V8 (rapport sans seuil)** : comptes de vraies paires par mécanisme (greffe, jumeau, pont conceptuel direct, expansion), taux d'exclusion, taux de régénération, nombre moyen de paires valides par monde et par condition (en v1 : 67,55 / 60,50 / 53,59).

### 7. Graines (R9)
- Deux racines entières, valeurs de l'auteur, scellées avec le document : RACINE_DECISION = 20261031000000 ; RACINE_VALIDATION = 20001231000000 (distincte de celle de v1 et de toute graine de validation de v1).
- Chaque tâche reçoit `numpy.random.SeedSequence(entropy=RACINE, spawn_key=(code_condition, indice_monde, code_rôle))` (numpy ≥ 1.25) ; une régénération (G11) ajoute le numéro de tentative comme quatrième élément.
- Codes de condition : M_bien 1, M_moyen 2, M_mal 3, SP 4, INV 5, V_fuite 6, V_concepts_absents 7, V_moyeu_conceptuel 8, V_surface 9, NR_bien 10, NR_moyen 11, M_inertes 12, M_couplage_faible 13, M_palettes_communes 14, M_palettes_disjointes 15.
- Codes de rôle : monde 0 ; observation des opérateurs 1 ; observation des concepts 2 ; contraintes 3 ; placebo N_PC 4 ; placebo de SP 5 ; placebo N_PCg 6 ; miroir de M_inertes 7 ; bras 10 + rang du bras dans la liste figée du § 4 (N = 10, …, N_grille = 30) ; rééchantillonnage 99, avec `indice_monde` remplacé par le code du contraste.
- Manifeste par run (`src/controle_ia/manifeste.py`) : configuration et empreinte, versions de Python et de numpy, racines et clés de dérivation, empreintes du code, commit.

### 8. Comparaisons, multiplicité, puissance
- Contrastes décisifs (95 %) en M_bien et M_moyen : C1 Δ(N, b) ; C2 Δ(N, a), Δ(N, d1), Δ(N, d1c) ; C3 Δ(N, N_β0) ; C4 Δ(N, N_filtre) ; C5 placebo hors domaine : Δ(N, N_PCg) (95 %) et Δ(N_PCg, N_β0) (99 %) ; **C6 M_inertes** : Δ(N, N_β0) (95 %) ; C7 SP (99 %, précision placebo) ; C8 INV ; C9 V_fuite ; C10 non-régression (99 %).
- Descriptifs (95 %) : N contre b_eloigne, N_aleat, N_global, N_dpp, N_fiches, N_q, N_rare, N_α0, N_PC, N_grille ; Δ(N_dpp, N_dpp_β0) ; Δ(N_PC, N_β0) ; Δ(N_PC, N_PCg) ; M_mal ; V_concepts_absents ; V_moyeu_conceptuel ; V_surface ; M_couplage_faible, M_palettes_communes, M_palettes_disjointes ; résultats par nombre de champs (2, 3, 4).
- Multiplicité : les règles d'adoption et de lecture sont des **conjonctions** (toutes les conditions doivent tenir), chacune à son niveau : pas de correction. Les contrôles à 99 % limitent les fausses alertes (M : quatre écarts indépendants, 3,9 % contre 18,5 % à 95 % ; trois écarts en SP : 3,0 %).
- Paires valides par monde : en v1, 67,55 / 60,50 / 53,59 (`daaef112…`) ; le budget de 12 en couvre environ le cinquième. À mesurer en v2, où l'étage commun s'élargit aux étiquettes de concept (en `M_inertes` et `M_palettes_communes`, nettement plus de paires valides, SUPPOSÉ ; rapporté par V8).
- Puissance : voir la section « Seuil ». Écart-type apparié de v1 : 15,0 à 15,3 (« bien »), 11,2 à 12,0 (« moyen ») (M). À 1 200 mondes : erreur type 0,44 (σ 15,3), demi-largeur 0,87 (95 %) et 1,14 (99 %). La garde S9 vérifie l'écart-type de Δ(N, b) en v2.
- Coût : processeur seul, aucune dépense ; temps de quelques heures en Python avec numpy (SUPPOSÉ ; v1 : 93 s pour 4 000 mondes sans noyau sur les paires ; 12 000 mondes de décision ici (somme du tableau du § 6), noyaux sur les paires pour N_dpp et N_dpp_β0).

### 9. Ordre d'exécution
Contre-lecture 2 → gel de S1 à S13 par Lazar (ligne datée) → remplacement des marqueurs et scellement → écriture du code → tests de gardes (liste d'arrêt) → validation du générateur (V1 à V8) → méthodes sur 200 mondes de validation de M_bien et de M_moyen : le code ne rend à la console que l'écart-type de Δ(N, b) et le drapeau de la garde S9 ; les moyennes de Δ(N, b) en validation et la grille sont écrites dans un fichier **scellé** (empreinte) non ouvert avant le verdict (CB-17) → mondes de décision → lecture par un sous-agent neuf (R13), qui ouvre alors le fichier de validation.

### 10. Hors périmètre
- Passage sur les vraies fiches de la course 2 : préenregistrement distinct, lecture **descriptive** (environ 20 paires par bras selon l'avis d'Opus ; 128 à 300 fusions par bras selon la synthèse pour un effet de +10 points), sans sélection sur le verdict (N-053, contenu non lu par l'auteur : SUPPOSÉ), précédé d'une mesure de séparabilité sur les paires de fiches réelles. Source des concepts sur fiches réelles (D-e) : décision séparée.
- Aucun appel de modèle, aucune fusion : la précision mesure le tirage, pas les filles (B § 6).

## Critères de lecture gelés

Un sous-agent neuf (ni auteur du présent préenregistrement ni de l'analyse, R13) applique ces tables telles qu'elles sont écrites. Les seuils S1 à S13 sont gelés avant scellement. « Les deux » = M_bien et M_moyen. Chaque table se lit **de haut en bas : la première ligne dont la condition est vraie décide** ; les conditions des lignes suivantes supposent les précédentes fausses, de sorte que les lignes sont exclusives et exhaustives (la dernière ligne est le complémentaire).

**Booléens** (X ∈ {M_bien, M_moyen} ; Δ(·, · ; X) = écart apparié dans X ; lb95, ub95 = bornes basse et haute à 95 % ; lb99 = borne basse à 99 %) :
- V0 = validation du générateur passée (V1 à V6) ∧ aucun arrêt de la liste ∧ taux d'exclusion de chaque condition de décision ≤ taux S11 ;
- perd(X) = ub95 Δ(N, b ; X) < 0 ;
- A1(X) = estimation de Δ(N, b ; X) ≥ θ_abs ∧ r(N, b ; X) ≥ θ_rel ∧ lb95 Δ(N, b ; X) > 0 ;
- A2(X) = lb95 Δ(N, a ; X) > 0 ∧ lb95 Δ(N, d1 ; X) > 0 ∧ lb95 Δ(N, d1c ; X) > 0 ;
- suffit_d1c(X) = ub95 Δ(N, d1c ; X) ≤ 0 ;
- A7(X) = lb95 Δ(N, N_β0 ; X) > seuil S3 ;
- A3 = dans SP, aucun des écarts N − b, N − d1c, N − N_β0 (précision placebo) n'a un intervalle à 99 % qui exclut 0 ;
- A4 = ub95 (Δ(N, b ; INV) − Δ(N, b ; M_bien)) < 0 ;
- A5 = lb99 Δ(N, b ; NR_bien) ≥ marge S7 ∧ lb99 Δ(N, b ; NR_moyen) ≥ marge S7 ;
- A6 = ub95 (Δ(N, b ; V_fuite) − Δ(N, b ; M_bien)) < 0 ;
- A8 = dans M_inertes, lb95 Δ(N, N_β0) ≤ 0 ∧ ub95 Δ(N, N_β0) < δ_non ;
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
| 7 | non (A7(M_bien) et A7(M_moyen)) | **« l'éloignement suffit : N_β0 ou b_eloigne, pas N »**, ou le terme de concept n'est pas démontré ; N non adoptée |
| 8 | A2(M_bien) et A2(M_moyen) | **N adoptée** (volet d'adoption) |
| 9 | tout autre cas | **indécis** |

### Table 2 — volet « ingrédient manquant, sous W1 à W4 »

| # | Condition de la ligne | Verdict |
|---|---|---|
| 0 | V0 non tenue | **non concluant** |
| 1 | un déclencheur d'audit est présent et l'audit n'est pas rendu | **non concluant** (audit en attente) |
| 2 | audit rendu, artefact trouvé | **non concluant** ; version nouvelle |
| 3 | gain_contrôle | **non** : un gain apparaît quand le concept est inerte ou permuté, donc il n'est pas celui de la valeur conceptuelle |
| 4 | N0(M_bien) et N0(M_moyen) | **non** : le terme de concept n'apporte rien |
| 5 | D0(M_bien) et D0(M_moyen) et NF(M_bien) et NF(M_moyen) | **non** au sens de la question : le concept **suffit comme filtre** ; son entrée dans l'objectif n'apporte rien de plus |
| 6 | D0 et DF et PG dans les deux, et A8 | **oui, sous W1 à W4** : dans un monde où la proximité conceptuelle observée porte de la vérité, et seulement là, la proximité conceptuelle dans l'objectif apporte plus que l'éloignement seul et que le filtre. Ce verdict ne dit rien du monde réel |
| 7 | tout autre cas | **indécis** |

Notes de lecture : la ligne 5 et la ligne 6 sont exclusives parce que δ_non < δ (NF suppose une estimation < δ, DF une estimation ≥ δ) ; les lignes 4 et 5 le sont parce que N0 suppose une estimation < δ_non < δ. Les deux tables sont indépendantes : « N adoptée » peut coexister avec « indécis » sur l'ingrédient.

Lecture secondaire, sans effet sur le verdict : la valeur du second espace est Δ(N, N_α0) ; la place du déterminant sur les paires est Δ(N_dpp, N_global), Δ(N_dpp, N) et Δ(N_dpp, N_dpp_β0) (P13) ; la valeur de q est Δ(N_q, N) ; la part d'information de domaine et d'article, Δ(N_PC, N_PCg) et Δ(N, N_PC) ; la pente selon le couplage (P12) ; l'axe palettes (M_palettes_communes, M_palettes_disjointes).

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
| Écart-type de Δ(N, b) sur les 200 mondes de validation > S9, en « bien » ou en « moyen » | arrêt ; nouvelle version avec plus de mondes |
| Taux de mondes exclus > S11 dans une condition de décision | arrêt |
| Taux de mondes régénérés après échec de plantation > S11 | arrêt |
| Bras de sortie vide avant complément sur plus de S11 des mondes ; précision (placebo comprise) hors de [0 ; 1] | arrêt |
| Écart de contrôle excluant 0 (SP, N_PCg, M_inertes) | audit R4 ; verdict « non concluant » tant que non rendu |
| Reproduction : moyennes de b, a, c, d1 sur NR_bien et NR_moyen hors de l'intervalle de B § 1 élargi de la marge S12 | arrêt : le code des témoins diffère de v1 |
| Appel de modèle, réseau ou dépense | arrêt (devis et GO exigés) |
| Lecture d'un résultat ou exécution d'une méthode avant scellement ; paramètre modifié après lecture ; ouverture du fichier de validation avant le verdict | arrêt et consignation de l'écart (R1) |
| numpy < 1.25 | arrêt (R9) |
| Contre-lecture 2 absente, ou marqueur de gel restant dans le texte | pas de scellement |
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

## Contre-lecture

- **Contre-lecture 1** : sous-agent neuf, Opus 5.5 (`claude-opus-5-5`), non-auteur du brouillon, du recoupement, de la question, de l'avis d'Opus, de la synthèse, du code du pôle et de `trancher-recombinaison-v1`. Brouillon relu : `preenregistrement-bisociation-deux-espaces-v2-brouillon1.md`, empreinte `c9077cfe136269c8cf1a5fa8192153fccf48962aba8e276ac2a7e4dad89288e7`. Rapport : `bisociation-deux-espaces-v1/contre-lecture-preenregistrement-bisociation-v2-brouillon1.md`, empreinte `a31096c000213127ff191bba54adb47247280ba452464b07a036f07b7be527c4` (relevé 2026-10-30T00:53:13Z). Conclusion du rapport : non scellable en l'état (CB-01 à CB-05 majeurs), scellable après corrections, gel de tous les seuils par Lazar et nouvelle contre-lecture. Ce brouillon 2 n'est **pas** la version relue.

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

  Réserves propres à ce brouillon 2, soumises à la contre-lecture 2 : (1) λ = 0,7, palettes de 4 sur 10, 18 concepts rares et nombre de ponts par statut sont des choix de l'auteur, sans source ; (2) les écarts-types de Δ(N, N_β0) et Δ(N, N_filtre) sont inconnus (tables de puissance prudentes) ; (3) la marge de non-régression recommandée (−2) diffère de l'avis d'Opus (−1) ; (4) l'algorithme de N prend, en un passage, les 12 strates de plus fort score : il est proche de N_global, ce que la lecture secondaire mesure ; (5) la recommandation de S1 rend « N adoptée » improbable aux prédictions de l'auteur (0,06 à 0,13), ce qui est dit et non corrigé.

- Contre-lecture 2 : À REMPLIR — sous-agent neuf à désigner (ni auteur de ce brouillon, ni du brouillon 1, ni de la contre-lecture 1, ni des pièces), de préférence d'un modèle différent de l'auteur (Sonnet 5.5) ; empreinte du brouillon 2 relu, chemin et empreinte de son rapport, traitement de chaque remarque. Fichiers à lui donner explicitement : ce brouillon ; `contre-lecture-preenregistrement-bisociation-v2-brouillon1.md` ; `preenregistrement-bisociation-deux-espaces-v2-brouillon1.md` ; `recoupement-bisociation-v1.md` ; la question, l'avis d'Opus, la synthèse ; les pièces de la liste « Documents qui font foi » ; `trancher-recombinaison/resultats-trancher-recombinaison-v1.json` ; `prereg/gabarit-preregistrement-v1.md` et `src/controle_ia/prereg.py`. Interdits à lui rappeler : ni `donnees/`, ni branche git, ni `prereg/P3-consignes-v1.md`, ni `diag/*/traces`. Questions prioritaires : (1) `M_inertes` est-il vraiment un monde où une forme sans valeur conceptuelle échoue, et sa vérité est-elle découplée de ce que N lit ? (2) les tables de puissance, les règles R-A et R-B et les recommandations de S1, S4, S7 ; (3) le générateur G1 à G12 : 30 articles, rareté, expansion, INV ; (4) N lit-il, même indirectement, un champ latent ? (5) l'axe palettes crée-t-il un avantage par construction pour N ou pour d1c ? (6) les deux tables de lecture sont-elles exclusives et exhaustives ?

## Ligne de gel pour Lazar

À dire par Lazar, après la contre-lecture 2 et la lecture des sections « Seuil » et « Critères de lecture gelés ». Texte exact de la ligne proposée, avec toutes les valeurs recommandées de l'auteur (un « go » suffit) :

> « Go, je gèle le préenregistrement de la recombinaison bisociative à deux espaces v2 aux valeurs recommandées : S1, θ_abs = +5 points ; S2, θ_rel = ×1,25 ; S3, A7 = borne basse à 95 % de N − N_β0 supérieure à 0, dans M_bien et M_moyen ; S4, règle de détection R-A (estimation ≥ δ et borne basse à 95 % > 0) ; S5, δ = +3 points ; S6, δ_non = +2 points sur la borne haute à 95 % ; S7, non-régression = borne basse à 99 % de N − b supérieure ou égale à −2 points, sur 1 200 mondes pour NR_bien et pour NR_moyen ; S8, plafond de l'oracle ≥ 0,30 ; S9, écart-type de garde ≤ 18 points ; S10, audit de symétrie à |écart| ≥ 12 points dans les deux sens et à précision de N ≥ 0,9 fois celle de l'oracle ; S11, arrêts en taux à 2 % (mondes exclus, mondes régénérés, bras vides) ; S12, marge de reproduction de 2 points ; S13, validation du générateur : cosinus moyens dans [0,51 ; 0,57], [0,25 ; 0,31] et [0,00 ; 0,06], fuite de domaine ≤ 0,10, excès de queue ≤ 0,10, jumelles à concordance ≥ 0,9 et variation de cosinus ≥ 0,2, rareté appariée à écart ≤ 0,5, vraies paires valides en « moyen » ≥ 6. Les défauts de 48 heures D-a à D-d et D-g restent tels quels (q ≡ 1, e = 8,5, β = 1, ε = 0,05, 1 200 mondes de décision). Date et heure : à consigner dans `registres/decisions.md`. »

Pour changer une valeur : dire le numéro et la nouvelle valeur (par exemple « S1 = +4 »), le reste suit. Au scellement, cette section est remplacée par la ligne effectivement dite, avec sa date, recopiée de `registres/decisions.md`, et chaque marqueur de la section « Seuil » est remplacé par la valeur gelée. La ligne du registre ne vaut qu'une fois la contre-lecture 2 faite et ses remarques traitées ; sinon le validateur du dépôt refuse de sceller.
