# Contre-lecture (R2) — préenregistrement de l'idée 1.1, version 2, brouillon 2 (poids du nul) : contrôle du différentiel — v1

- Contre-lecteur : sous-agent neuf de la session mère. Je n'ai écrit ni ce brouillon, ni le brouillon 1, ni sa contre-lecture
  ([CL2]), ni la version 1, ni la preuve, ni la synthèse, ni les rendus des angles, ni le juge, ni les nuls v8 et v9.
- Date (UTC) : 2026-11-15, de 20:45 à 21:00 environ (`date -u`). Dépôt `/home/user/controle-ia-travail`, `main`, tête
  `eeee7230` (commit du brouillon 2, 20:44:28). Aucun commit, aucune poussée, aucun appel réseau ni payant ; brouillon non
  modifié.
- **Texte relu** : `docs/notes/organisme-idees-juge-v1/organisme-idee-1-1-poids-du-nul-v2-brouillon2.md`,
  `5a78dbe759421888f10cd5bcae57f4fa1ed03d0cef162944a9bd17ca98a9e6ae` (égale à son compagnon).
- Lu aussi : le brouillon 1 (`916985ce…0b55`, différentiel par `git diff --no-index --word-diff`) ; [CL2]
  (`d5e71f6c…c4b`) en entier ; le dossier `organisme-idee-1-1-poids-du-nul-v2-outils/` ; [R-PROJ] § 5 ; `selection_pari.py`
  (bibliothèque, `proba`, `valider_loi`, `_traj_moyennes_glissantes`) et `cycle.py` (l. 312 à 330) de la copie `94bfd92` ;
  `test_nul_v9.py` (en-tête, imports, classes) de la copie `a41b7b5` ; en-tête de `banc_tricheurs_v7.py` ; `src/controle_ia/prereg.py`.
- Rien lu sous `diag/`, `runs/` de 7a ou 7b, `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`,
  `docs/notes/bras-attaque/`. Pour retrouver les fichiers des empreintes citées, j'ai calculé l'empreinte des fichiers suivis
  par git, ces dossiers exclus (contenu jamais affiché).

## Verdict

**Scellable après corrections.** Deux majeurs, sept mineurs, tous textuels ; aucun ne touche la conception. Les six majeurs et
les quatorze mineurs de [CL2] sont levés dans le texte, à deux restes près : M6 est levé par une route dont une affirmation est
fausse (N2) ; la règle de réduction neuve, écrite pour M5, contredit la liste de ce qui n'est jamais réduit (N1).

## Ce qui tient (vérifié)

1. **Différentiel.** Chaque bloc changé correspond à une remarque de [CL2] ou à une précision de la mère annoncée (M3, M5, M6).
   Un seul changement n'est pas annoncé : la section « Citations obligatoires » dit maintenant « empreintes des quatre PDF
   recalculées par moi […], égales » au lieu de « reprises de [BANC-v2] ; PDF non rouverts ». Il est juste (les quatre
   empreintes sont égales, point 4), mais le statut dit « rien d'autre ne change » (n6). Aucun autre effet de bord : les
   indices de graines du brouillon 1 sont gardés (Hg prend `i_ligne` = 28, après H7) ; aucun seuil ni aucune prédiction hors
   de P2, P12 et P13 n'a bougé.
2. **Remarques de [CL2], une par une.**
   - M1 : I ⊂ {15 lignes V} à la « Métrique », en tête des prédictions, à l'étage 3 et aux « Comparaisons » ; lignes Q et H
     exclues de ρ, des gains réunis et de la décomposition ; mutation ajoutée. Levé.
   - M2 : ligne d'arrêt réécrite mot pour mot avec ses deux exceptions (Hg comprise) ; tirage bloc par bloc ; numérateur de
     W^reste sous gel = carte gelée ; « une promotion sous gel porte sur la carte gelée » écrit à la garantie et au bras 3 ;
     mutation ajoutée. Levé.
   - M3 : H7 séparé en terme projeté (dent, cellule de Holm) et juge complet (rapporté) ; Hs déclarée aveugle et sortie du
     verdict « trou atteint » ; Hg ajoutée ; écart de montage « urne » écrit ; critère de mort écrit. Levé (n1 sur le critère).
   - M4 : ρ⁺ et I⁺ définis selon le rapport ; mutation ajoutée. Levé (n3 sur deux cas de lecture).
   - M5 : estimation refaite (7 à 9 s ; 29 000 répétitions = 56,4 à 72,5 heures d'un cœur, soit 18,8 à 24,2 heures sur trois
     processus : juste) ; chronométrage à l'étape 0 ; D ≤ 32 heures ; règle de réduction ; borne de 48 heures (écart déclaré,
     plus dur que [CL2]). Levé, sauf N1.
   - M6 : route « à défaut » choisie, impossibilité de verser le fichier déclarée et vérifiée par moi (`git cat-file -t
     a41b7b5` échoue ; aucun `banc_tricheurs_v9.py` suivi). Levé en partie : N2.
   - m1 à m14 : tous portés à l'endroit dit. m14 : entrée « Contre-lecture 2 » reconnue par `prereg.ENTREE`.
3. **Comptes.** Holm : fatales dans la famille 6 + 5 + 4 + 4 + 3 = **22** ; copies 2 + 2 + 1 + 1 + 1 = **7** ; taille Q7 7,
   Q8 8, Hs 4, Hm 4, Hg 4, H7 1 = **28** ; **57 = 22 + 7 + 28**. Fatales **34 = 22 + 12** (Q9a, Q9b, hors de Holm).
   P2 **35 = 7 + 28**. Lignes : 22 + 7 = **29** ; `i_ligne` de 0 à 28. Exact.
4. **Seuils (annexe A).** Script et sortie versés, égaux à leurs compagnons (`91fd1d11…cecda`, `4e508c64…72f2`) ; le script
   et la sortie extraits du texte sont égaux, octet pour octet, aux fichiers versés ; rejoué par moi en `python -I` : sortie
   identique à l'octet. Le script du brouillon 1, extrait de [B1], redonne `d7408ee1…83f3`. À 57 cellules : tenue ≤ 29,
   non tenue ≥ 74 (pas le plus strict) ; ≤ 38 et ≥ 63 (pas le moins strict) ; dents 527 et 63 ; informativité 29. Justes.
5. **Empreintes (R6).** 40 empreintes entières dans le texte. 38 correspondent au fichier nommé (modules de `94bfd92` égaux
   aussi à `empreintes-copie-v1.txt`). Les deux autres sont déclarées : `a9f9594e…` (reprise de [SYN], fichier non rouvert,
   dans un dossier que je n'ouvre pas) et `d7408ee1…` (script du brouillon 1, recopié dans [B1], point 4).
6. **Validateur.** `controle_ia.prereg.problemes` sur le brouillon 2 : **0 problème**.
7. **Aucun identifiant de modèle** dans le texte (recherche sur les noms de familles et de fournisseurs : rien).
8. **Ligne Hg.** `valider_loi` de `94bfd92` accepte la carte telle qu'écrite (essai à sec, dimension 2, 3 issues ; types
   rencontrés : `melange`, `softmax`, `moyenne_glissante`) ; `lissage` n'est pas contrôlé par `valider_loi`, la valeur 0,5
   est donc à tenir par le banc. Hg n'est pas aveugle par l'argument de Hs : W^reste ne contient pas le monde
   `melange`([S1, S2]). Mais sa composante « fenêtre 5, lissage 0,5 » est exactement la fenêtre 5 du membre ordinaire
   `moyenne_glissante` de `BIBLIOTHEQUE_STANDARD` (maximum sur les fenêtres 5, 10, 20, 50) : à dire (n7).
9. **Règle de réduction : applicable sans lecture de résultat.** D se calcule sur les seuls temps ; l'ordre est fixé ; aucune
   cellule de Holm n'est touchée (les crans 2, 3 et 5 portent sur les lignes V, hors de Holm ; les cellules de Holm de J9-D40,
   J9-D et La-P sur Q7, Q8, Hs, Hm, Hg restent à 1 000) ; ni la principale, ni La, ni Ld, ni les dents. **Une seule
   exception : le cran 4 touche 12 cellules fatales (N1).** Deux précisions de forme (n2).
10. **Tirage bloc par bloc.** Un seul tirage par répétition, partagé par tous les bras ; sous gel, le journal du bloc b est
    écrit avant le tirage du bloc b. Les mêmes issues vont à tous les bras, à une précision près (n4).
11. **Critère de mort et cas sain, contre α et Holm.** « Au moins 20 sur 200 » : borne basse unilatérale à 95 % de 20/200 =
    0,067, au-dessus de la dent du jeu (0,05) ; cohérent dans le sens sûr. « Au plus 2 sur 200 » sous gel : plus dur que
    P12 (≤ 0,02) et que α ; sans risque de signe positif (R3), mais avec un risque de blocage à écrire (n1). Aucun des deux
    n'entre dans Holm : ce sont des essais du code, sur les graines `(97, k)`, distinctes de celles du jeu. Juste.

## Majeurs (ancien → nouveau)

**N1 — Le cran 4 de la règle de réduction réduit des cellules fatales, que la même section déclare « jamais réduites ».**
Q9a et Q9b portent 12 des 34 cellules fatales (« Cellules (comptes) » : 6 + 6 ; P1 : 34 = 22 + 12). Le cran 4 les met à 500
répétitions, et la phrase suivante dit « les cellules fatales (toutes à 1 000) ». Telle qu'écrite, la règle est inapplicable
dès le cran 4 : il faudrait choisir après le chronométrage.
- ancien : « 4. lignes Q9a et Q9b (protection, hors de Holm, rapportées) : 500 premières répétitions ; »
- nouveau : « 4. lignes Q9a et Q9b, bras à projection seulement (J9-P et La-P : 4 cellules rapportées, hors de Holm, non
  fatales) : 500 premières répétitions ; les 12 cellules fatales de ces lignes restent à 1 000 ; »
- ancien : « **Jamais réduits** : les 57 cellules de la famille de Holm et les cellules fatales (toutes à 1 000) ; »
- nouveau : « **Jamais réduits** : les 57 cellules de la famille de Holm et les 34 cellules fatales, celles de Q9a et Q9b
  comprises (toutes à 1 000) ; »

**N2 — La route « à défaut » du préalable 1 repose sur une affirmation fausse : les classes nommées emploient le banc
absent.** « Écarts », l. 586 et 587. `MembresNulV9`, `CertificatMorceaux` et `EvaluateurV9` emploient toutes `banc` :
constantes `K`, `DIM`, `ALPHA` (l. 57, lues sur le module absent), `banc.CALIBRAGE`, `banc.TIRAGES`, `banc.DELTA0`,
`banc.INSTANTS` (`_engagement`, l. 317 à 331), et les constructeurs `banc._par_sp`, `banc._si_seuil`, `banc._melange`
(l. 149 à 155, 179, 192, 252, 282 à 288, 340, 364). Les valeurs de ces constantes dans `banc_tricheurs_v9.py` sont inconnues.
(Indice, non une preuve : `banc_tricheurs_v7.py`, `ef016d25…cf12`, fixe K, DIM, TIRAGES, CALIBRAGE, ALPHA, DELTA0 = 3, 2,
200, 50, 0,05, 0,01 et INSTANTS = les huit instants par défaut.) Les essais réécrits ne sont donc pas des copies des
essais d'origine. De plus, la classe `TricheursParMorceaux` (monde W2 de l'attaque, tricheurs M01 à M07, loi neuve plantée)
n'est remplacée que par un seul essai du banc. Enfin, « Sinon : pas de jeu », placé après la phrase sur un versement futur,
peut se lire « sans versement, pas de jeu », ce qui contredit la route « à défaut ».
- ancien : « (K = 3, dimension 2, α = 0,05 écrits dans l'essai), d'après les »
- nouveau : « (K = 3, dimension 2, α = 0,05, 200 tirages, instants T₈, écrits dans l'essai ; mondes construits par les types
  de `lois_v1.py` (`par_sous_population`, `si_sinon`, `melange`) au lieu de `banc._par_sp`, `banc._si_seuil`,
  `banc._melange`), d'après les »
- ancien : « classes de `test_nul_v9.py` qui n'emploient pas ce banc : »
- nouveau : « classes de `test_nul_v9.py` qui n'en emploient que les constantes et les constructeurs de mondes (valeurs
  d'origine inconnues : les essais réécrits ne sont pas des copies, différentiel avec chaque essai d'origine écrit et lu par
  le contre-lecteur du code) : »
- ancien : « les essais d'origine sont rejoués en plus. Sinon : pas de jeu. »
- nouveau : « les essais d'origine sont rejoués en plus. Si (a), (b) ou (c) manque ou échoue : pas de jeu. La classe
  `TricheursParMorceaux` n'est pas réécrite ; l'essai du banc ci-dessus en tient lieu, et c'est une réserve du rapport. »

## Mineurs (ancien → nouveau)

- **n1 — Critère de mort et cas sain : plus durs que le jeu, sans le dire.** Sous gel, si le vrai taux valait 0,01, le cas
  sain « au plus 2 sur 200 » échouerait une fois sur trois (0,32) ; à 0,02 (permis par P12), trois fois sur quatre (0,76).
  Sans garde, un vrai taux de 0,07 passerait la dent du jeu, mais ferait survivre la mutation 93 fois sur 100. Dans ces deux
  zones, l'étape 0 bloquerait le jeu, alors que l'étage 7 a un verdict écrit. L'exploratoire (0,30 pour toutes les coupures
  sans garde ; 0 sur 13 000 sous gel) rend ce risque faible, mais le choix doit être écrit.
  - ancien : « niveau α ne garantit pas zéro ; exploratoire : 0 sur 13 000, [R-PROJ] § 5). »
  - nouveau : « niveau α ne garantit pas zéro ; exploratoire : 0 sur 13 000, [R-PROJ] § 5). Ces deux seuils sont plus durs
    que la dent du jeu (63 sur 1 000) et que P12 (≤ 0,02) : choix déclaré, fondé sur l'exploratoire (18 sur 60 pour toutes
    les coupures sans garde). Une survie (moins de 20) ou un cas sain manqué (3 ou plus) bloque le jeu, avec son compte
    inscrit à l'addendum, et ouvre un texte neuf ; jamais de seuil changé après coup. »
- **n2 — Chronométrage : sur quelles lignes, pour combien de processus.** La formule de D demande un temps par ligne et par
  bras, alors que le texte dit « 20 répétitions d'essai » sans dire les lignes. Elle divise par 3, alors que le jeu tourne
  avec « trois processus au plus ».
  - ancien : « Temps de chaque bras mesuré sur 20 répétitions d'essai (graines »
  - nouveau : « Temps de chaque bras mesuré sur 20 répétitions d'essai **de chacune des 29 lignes**, gel par bloc compris,
    le programme n'écrivant que des temps (graines »
  - ancien : « répétitions) / 3 processus. »
  - nouveau : « répétitions) / p, où p ≤ 3 est le nombre de processus inscrit à l'addendum. »
- **n3 — Lecture de ρ⁺ : deux cas non écrits.** L'ordre « le moins favorable » n'est pas écrit, ni le cas où I compte au
  moins 2 lignes et I⁺ moins de 2 (J9⁺ promeut plus que J9, donc I⁺ peut rétrécir).
  - ancien : « si J9⁺ change le verdict : **« sensible au certificat »**, et c'est le moins favorable des deux qui est
    retenu | »
  - nouveau : « si J9⁺ change le verdict : **« sensible au certificat »**, et c'est le moins favorable des deux qui est
    retenu (ordre, du plus au moins favorable : « regagne », « partiel », « ne regagne pas », « nuisible ») ; si I⁺ compte
    moins de 2 lignes alors que I en compte au moins 2 : « sensible au certificat », et la principale est lue « non
    tranché » (issue D) | »
- **n4 — Mêmes issues quels que soient les bras joués.** Sur Hs, Hm, Hg et H7 seulement, le tirage est entrelacé avec le gel.
  Il faut dire que la suite des appels au générateur est la même partout.
  - ancien : « les 200 issues fraîches sont tirées du monde, bloc par bloc, d'un générateur distinct ; la »
  - nouveau : « les 200 issues fraîches sont tirées du monde, bloc par bloc, d'un générateur distinct, par la même suite
    d'appels sur toutes les lignes, que des bras sous gel y soient joués ou non (les issues ne dépendent d'aucun bras) ; la »
- **n5 — P12 : la prédiction sur Hs n'a pas de réfutation.**
  - ancien : « Hm ou Hg : borne basse > 0,05 (le trou est atteint par une carte de la grammaire) | 0,6 | »
  - nouveau : « Hm ou Hg : borne basse > 0,05 (le trou est atteint par une carte de la grammaire) ; Hs, J9-P-nu complet :
    borne basse > 0,05 (défaut de W^reste, à auditer) | 0,6 | »
- **n6 — Statut : un changement non annoncé** (citations, point 1).
  - ancien : « et les précisions de la mère sur M3, M5 et M6 ; rien d'autre ne change. »
  - nouveau : « et les précisions de la mère sur M3, M5 et M6 ; seul autre changement : les empreintes des quatre PDF des
    citations sont recalculées (égales) au lieu d'être reprises. »
- **n7 — Hg : composante égale à un membre de W^reste.** À dire, pour la lecture d'un nul sur Hg.
  - ancien : « | garde P4, second type qui lit l'historique ([CL2] M3) ; jouée comme Hm | »
  - nouveau : « | garde P4, second type qui lit l'historique ([CL2] M3) ; jouée comme Hm ; sa composante « fenêtre 5,
    lissage 0,5 » est la fenêtre 5 du membre ordinaire `moyenne_glissante` de W^reste (Hg n'est pas aveugle : le monde n'est
    pas dans W^reste) ; `lissage` n'est pas contrôlé par `valider_loi`, le banc le vérifie | »

## Réponses aux questions posées par l'auteur

- **Holm à 57, P2 à 35** : exacts (point 3) ; seuils inchangés, rejoués (point 4).
- **Règle de réduction** : ordre et seuil de 32 heures applicables sans lecture ; aucune cellule de Holm, ni la principale, ni
  une primaire, ni une dent n'est touchée ; mais le cran 4 touche 12 cellules fatales (N1).
- **Cas sain « au plus 2 sur 200 »** : acceptable, plus dur que α et que P12 ; à écrire comme choix déclaré, avec sa
  conséquence (n1). L'écart à [CL2] (« 0 fois ») est justifié.
- **Essais réécrits du v9** : bloquants dans le texte ; suffisants comme préalable une fois N2 corrigé (constantes et
  constructeurs réécrits déclarés, différentiel lu, `TricheursParMorceaux` en réserve).
- **Hg et `valider_loi`** : acceptée (point 8).

## Fichiers produits

- Ce rapport et son compagnon `.sha256`. Mes essais (rejeu de l'annexe A, extraction du script, essai de `valider_loi` sur
  Hg et Hm à partir d'une copie du paquet `pole` de `94bfd92`, calculs binomiaux) sont restés dans le dossier de travail de
  la session, hors du dépôt. Aucun fichier du dépôt n'a été modifié.
