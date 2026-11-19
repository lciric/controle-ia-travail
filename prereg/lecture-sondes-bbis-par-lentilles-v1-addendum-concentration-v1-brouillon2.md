# Addendum d'écart déclaré au préenregistrement descriptif scellé « lecture, par la lentille publique côté sortie, des directions des sondes apprises sur la tâche (étape B bis de T0.7) » — les directions nulles sont jugées sans elles-mêmes (valeur p de concentration et valeur p de la part au-dessus du nul) — v1

- **Auteur** : rédacteur neuf, sous-agent de la session mère, modèle servi **Fable 5.2** (`claude-fable-5-2`). Il n'a écrit ni le
  texte scellé, ni son code, ni la contre-lecture du code, ni aucune pièce de l'apprentissage des sondes sur la tâche ; il ne sera ni
  développeur, ni opérateur, ni lecteur de cette lecture.
- **Date (UTC, `date -u`)** : 2026-11-19. Lecture des pièces à partir de 11:38:42 ; programmes écrits et joués de 11:43 à 12:20 ;
  session interrompue puis relancée par la mère (mot de Lazar rapporté par elle, R-3792) ; texte écrit à partir de 12:21:09.
- **Décision** : mot « go » de Lazar, **option 2** de la fiche de décision du rapport de contre-lecture du code, inscrit en
  **GO-2026-11-19-47** et **R-3771** (références données par la mère ; l'auteur n'a ouvert aucun registre).
- **Règle de scellement** : ce texte est un **brouillon candidat**, scellé comme brouillon par son auteur. Il est **contre-lu par un
  agent neuf sur Opus 5.5** (R2 ; fichiers à lui donner : § 11), puis scellé par la mère, puis inscrit au registre propre
  `registres/lecture-sondes-bbis-par-lentilles-v1.md` sous la clé **`ADDENDUM-CONCENTRATION-LENTILLES-BBIS`** (heure, chemin,
  empreinte), **avant toute lecture d'une sonde réelle**, c'est-à-dire avant la ligne `ENTREES-LENTILLES-BBIS` et avant toute exécution
  du calcul (texte scellé, plan, point 6). Tant que cette ligne manque, rien ne part.
- **Texte scellé visé** : `prereg/lecture-sondes-bbis-par-lentilles-v1.md`,
  `ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572`, lu sur la branche principale (tête
  `505c64ffff9a7a8032a10cecad5f00d57cfce4ea`), empreinte recalculée et égale. Il est noté « le texte » ci-dessous.
- **Pièces citées (chemin et empreinte, branche principale, empreintes recalculées par l'auteur)** :
  - rapport de la contre-lecture du code, `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lecture-code-lentille-publique-v1.md`,
    `679eb7232eed0c154743348102cccd40c05b8f38b1f730eeb21b24f171af155d` (« le rapport ») ;
  - outils scellés du contre-lecteur du code, dossier `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lecture-outils-v1/` :
    banc `banc_contre_lecteur_v1.py`, `5045f1142bef0a85388df1d081e15edfc7e49e0c47f16aeabde0a0d37f895142` ; sa sortie
    `sortie-banc-contre-lecteur-v1.txt`, `0101c9aaaca97b5e1fc9a17e3230ae0b5f1806131a19ca452147e4799df62d4e` ; programme du risque
    `risque_calibration_v2.py`, `f289aa0304c0713970291b65df9754a2db9b43fc7a06865a8aa68f672cc5bb62` ; sa sortie
    `sortie-risque-calibration-v2.txt`, `170b6cfca11a14bbf53707189735baa0f2c3403a9fa4ad76f09674e4ca2db349` ;
  - programme des bornes du texte, `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/bornes_calibration_beta_binomiale_v1.py`,
    `a8763c96a3f945e680700f121c800d0d636f129aa3fb64ee71f23f97b01b675e`, et sa sortie
    `sortie-bornes-calibration-beta-binomiale-v1.txt`, `61bf13cd5e0c706c9e1bf0ede6b15b0b7dff7ae6af6006dbe36b759185330e5a` ;
  - note du développeur et module préparé (branche `claude/lentilles-bbis-developpeur-v1`, commit
    `e2e24cacb87df4d31b487b7a81461a5208a928fa`, lus sur l'autorisation de la mère, **après** que l'auteur a écrit ses formules) :
    `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/traitement-contre-lecture-v1-complement-1.md`,
    `8b34c66ea0372c9ed7d4c48ab153ccd513c90649a30160b39451d19257dd24c5` ;
    `src/controle_ia/lentilles_sondes_bbis/statistiques_v2.py`, `b6c291e304da5b974d4b1b484dd05cfe2a0ee819aff69abc62dde348dccd6f49`.
- **Pièces neuves de cet addendum** (dossier `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/`, noms neufs, R12 ; aucune donnée,
  aucun poids, aucune sonde, aucune lentille) :
  - programme des bornes `bornes_calibration_statistique_corrigee_v2.py`,
    `0f31484b5e2c0fe98a584d8011bede8734fca62eae1f2b6d36d17638638ed34c` ; sortie
    `sortie-bornes-calibration-statistique-corrigee-v2.txt`, `39a410e46c4cd938e082a6d9ed3bdcc8b9a0b7365e80ad9efcd5de60b53d540e` ;
  - calcul exact dans le modèle gaussien `validite_gaussienne_statistique_corrigee_v2.py`,
    `39e7383391993f96e2ae850dc93f53a91b2111b512f9fb23f9d062d4a2e5ff3d` ; sortie
    `sortie-validite-gaussienne-statistique-corrigee-v2.txt`, `3dbd64f3906e58058309f190d2495234a7aa2594d675d58683d804939b5de3be` ;
  - simulation sur données synthétiques `simulation_statistique_corrigee_v2.py`,
    `78e115daf97d94305880eb69b3f5d0de665d5e38847a5a2c013118e7cd56f7c4` ; sortie
    `sortie-simulation-statistique-corrigee-v2.txt`, `4ee7b11e7d5b2c4c5ff25d79a7b0b769005110ae8618cf83012ee8dcfb69955e`.
- **Statut** : **version corrigée après la contre-lecture `715ddfa7…`**, à vérifier par le même contre-lecteur, puis à sceller par
  la mère ; ce statut remplace, pour l'état de la pièce, les mots « brouillon candidat » de la règle de scellement ci-dessus. Le
  brouillon contre-lu est archivé sans changement d'un octet sous
  `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1-brouillon1.md`,
  `0a862760025caf11ff66578dc47c53143ee480c173a733920b9f4b9425d59546`. La contre-lecture (contre-lecteur neuf, Opus 5.5 ; conclusion :
  « Scellable après ces couples exacts ») :
  `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lecture-addendum-concentration-v1.md`,
  `715ddfa7fb65352126f21c773e9f4ad9359d25cc5a57d1a2816d4018111bf106`, branche principale. Les cinq couples obligatoires C1 à C5 et les
  trois couples facultatifs F1 à F3 de son § 9 sont appliqués à la lettre ; **un point d'écart neuf, EC-6 (garde d'égalité au
  vingtième rang), est ajouté hors de cette contre-lecture et soumis à Lazar avant le scellement** (§ 9, point 7) ; détail au § 12.
  Corrections portées par un rédacteur sur Fable 5.2 de la session des lentilles (`session_013QMaykLXtozHttcSQ4ke1s`), sans mémoire
  du brouillon 1, qu'il a lu comme une pièce. Aucune dépense, aucune machine, aucun modèle chargé, aucune sonde réelle lue.

## 0. Le texte scellé n'est pas remplacé

Le texte reste scellé et inchangé. Cet addendum ne change que les passages nommés au § 3 ; partout ailleurs le texte fait foi. Là où
l'addendum et le texte se contredisent sur ces passages, l'addendum prime. **Le texte décide, le code suit** : le code est accordé à
l'addendum scellé, jamais l'inverse.

## 1. La correction, en deux lignes

Pour chaque direction nulle u_j, la moyenne et l'écart type qui donnent sa **concentration**, et le quantile 0,99 qui donne sa **part
au-dessus du nul**, se calculent sur les **M − 1 autres directions nulles du même nul, sans elle-même**.
La direction lue, les directions témoins, les comptes de familles, les pôles et les bornes de calibration ne changent pas.

## 2. Déclaration de l'écart

- **Ce que le texte dit** (« Métrique », point 6, lignes 336-337) : la concentration de chaque direction nulle est calculée avec la
  moyenne et l'écart type des M directions nulles, elle-même comprise, « écart déclaré, négligeable à M = 2 000 ».
- **Ce qui a été trouvé** : cet écart n'est pas négligeable. Au banc du contre-lecteur du code — **matrices aléatoires seulement**,
  taille du texte (89 498 jetons, largeur 4 096, M = 2 000), sept scénarios, huit répétitions de 2 000 témoins chacun — la part des
  témoins à p ≤ 0,05 vaut **5,71 %** en moyenne (0,0571 ; de 0,0555 à 0,0585 selon le scénario) au lieu de 5 % (100/2 001), et
  **5,13 %** quand chaque direction nulle est jugée sans elle-même, sur les mêmes tirages. Chiffres : sortie du banc,
  `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lecture-outils-v1/sortie-banc-contre-lecteur-v1.txt`,
  `0101c9aaaca97b5e1fc9a17e3230ae0b5f1806131a19ca452147e4799df62d4e` (moyenne des sept lignes « seuil 0.05000 » recalculée par
  l'auteur : 0,05706 et 0,05130) ; rapport, § 5, `679eb7232eed0c154743348102cccd40c05b8f38b1f730eeb21b24f171af155d`.
- **Mécanisme** : une direction nulle comprise dans sa propre moyenne et son propre écart type voit son plus grand z rétréci, alors
  que la direction lue ne l'est pas. La relation est exacte (§ 3, EC-1) : z sans elle-même = d · √(M/(M − 1)) / √(1 − d²/(M − 1)), d
  étant le z avec elle-même ; pour d ≈ 4,5 et M = 2 000, d est plus petit de 0,53 %. Le même mécanisme joue sur la part : une
  direction nulle dépasse le quantile 0,99 qui la comprend à 20 rangs sur 2 000 (1,00 %), une direction fraîche à 1,049 %.
- **Sens** : anti-conservateur. Les valeurs p du texte sont un peu trop petites, pour les directions réelles comme pour les témoins ;
  la calibration du texte pouvait sortir de ses bornes à tort (rapport, § 5 : probabilité 0,159 pour quarante jeux de 200 témoins à
  la part 0,0571).
- **Antériorité** : **aucune sonde réelle n'a été lue**, par personne, selon le rapport et selon la mère ; le biais a été vu sur des
  matrices aléatoires seulement. L'auteur n'a ouvert aucune sonde, aucune table, aucun score, aucun registre (§ 10).
- **Décision** : option 2 de la fiche du rapport, par le mot de Lazar (GO-2026-11-19-47, R-3771).

## 3. Les écarts : texte avant, texte après

### EC-1 — « Métrique », point 6, concentration (texte, lignes 336-337)

Avant :

> - **concentration** C(v) = max_t z_t ; p = (1 + #{j : C(u_j) ≥ C(v)}) / (M + 1), C(u_j) calculé avec les mêmes m_t et s_t (u_j
>   compris : écart déclaré, négligeable à M = 2 000) ;

Après :

> - **concentration** C(v) = max_t z_t ; p = (1 + #{j : C(u_j) ≥ C(v)}) / (M + 1). **Pour chaque direction nulle u_j,
>   C(u_j) = max_t z_t^(−j)(u_j), avec z_t^(−j)(u_j) = (a_t(u_j) − m_t^(−j)) / s_t^(−j), où m_t^(−j) et s_t^(−j) sont la moyenne et
>   l'écart type de a_t sur les M − 1 autres directions nulles du même nul, u_j exclue.** L'écart type est celui de population
>   (diviseur M − 1 pour M − 1 valeurs), comme s_t l'est pour M valeurs (diviseur M). C(v) reste calculé avec m_t et s_t, sur les M
>   directions nulles ;

Formules exactes, que le code peut employer (identités algébriques ; la définition ci-dessus fait foi), avec m_t et s_t sur les M
directions et d = (a_t(u_j) − m_t) / s_t :

- m_t^(−j) = (M·m_t − a_t(u_j)) / (M − 1) ;
- (s_t^(−j))² = (M·s_t² − (a_t(u_j) − m_t)²·M/(M − 1)) / (M − 1) ;
- z_t^(−j)(u_j) = d · √(M/(M − 1)) / √(1 − d²/(M − 1)) : fonction croissante de d, la même pour tous les jetons ; donc
  C(u_j) = φ(max_t d), φ(d) = d · √(M/(M − 1)) / √(1 − d²/(M − 1)).

Calcul en double précision ; C(u_j) est ensuite rendu en simple précision, comme C(v), et la comparaison C(u_j) ≥ C(v) se fait en
simple précision (une égalité compte contre v). Si, pour un jeton, la variance des M − 1 autres est nulle ou ne dépasse pas 10⁻¹⁰ fois la variance des M :
**arrêt** (z non fini ; ligne « valeur non finie dans une lecture ou un nul » de la « Liste d'arrêt », de sens sévère).

### EC-2 — « Métrique », point 6, part au-dessus du nul (texte, lignes 338-339)

Avant :

> - **part au-dessus du nul** P(v) : part des vingt premiers jetons dont le score dépasse le quantile 0,99 des M scores nuls du même
>   jeton ; p de même forme ;

Après :

> - **part au-dessus du nul** P(v) : part des vingt premiers jetons dont le score dépasse le quantile 0,99 des M scores nuls du même
>   jeton ; p de même forme, **où, pour chaque direction nulle u_j, P(u_j) est la part de ses vingt premiers jetons (par score) dont le
>   score dépasse le quantile 0,99 des M − 1 scores des autres directions nulles au même jeton, u_j exclue**. Quantile par
>   **interpolation linéaire** : sur n valeurs triées x_0 ≤ … ≤ x_{n−1}, rang fractionnaire h = 0,99 × (n − 1), valeur
>   x_⌊h⌋ + (h − ⌊h⌋)·(x_{⌊h⌋+1} − x_⌊h⌋). Pour v et les témoins, n = M = 2 000 (h = 1 979,01) ; pour une direction nulle,
>   n = M − 1 = 1 999 (h = 1 978,02) ;

Les vingt premiers jetons de u_j restent ses vingt plus grands scores bruts ; « dépasse » reste strict.

### EC-3 — « Plan d'analyse », point 6, calibration (texte, lignes 460-468)

Avant (deux passages de la même puce) :

> leurs p de concentration sont calculés contre les M directions nulles

> sous la loi exacte du compte quand les témoins d'un jeu partagent ses M directions nulles : pour un jeu de n témoins, la loi
> bêta-binomiale (n ; 100 ; M − 99 = 1 901) ; pour plusieurs jeux mis en commun (un jeu de 200 par vecteur), la somme de lois
> bêta-binomiales indépendantes ; bornes calculées par le code et écrites (par exemple [23, 85] pour un jeu de 1 000 ; [1, 24] pour un
> jeu de 200 ; [12, 53] pour trois jeux de 200 ; [26, 79] pour cinq jeux de 200)

Après :

> leurs p de concentration sont calculés contre les M directions nulles, **chaque témoin jugé comme la direction lue (m_t et s_t des M
> directions nulles), chaque direction nulle jugée sans elle-même (« Métrique », point 6, corrigé par l'addendum)**

> sous la **loi de référence** du compte quand les témoins d'un jeu partagent ses M directions nulles : pour un jeu de n témoins, la loi
> bêta-binomiale (n ; 100 ; M − 99 = 1 901) ; pour plusieurs jeux mis en commun (un jeu de 200 par vecteur), la somme de lois
> bêta-binomiales indépendantes ; **cette loi est approchée, non exacte (addendum, § 7)** ; bornes calculées par le code et écrites,
> **égales à celles du programme `bornes_calibration_statistique_corrigee_v2.py` de l'addendum** (par exemple [23, 85] pour un jeu de
> 1 000 ; [1, 24] pour un jeu de 200 ; [12, 53] pour trois jeux de 200 ; [26, 79] pour cinq jeux de 200)

Le reste de la puce (nombres de témoins, mise en commun, part attendue 100/2 001, définition de q_bas et q_haut, niveau 10⁻⁴ par côté,
borne basse déclarée lâche pour n < 600) est inchangé. **Les bornes ne changent pas de valeur.**

### EC-4 — « Plan d'analyse », point 1, et « Lignes de registre » (texte, lignes 374-382 et 628-633)

Ajout : une clé neuve du registre propre, **`ADDENDUM-CONCENTRATION-LENTILLES-BBIS`** (version scellée de cet addendum), inscrite après
sa contre-lecture, **avant `CODE-LENTILLES-BBIS` et avant `ENTREES-LENTILLES-BBIS`**, donc avant toute exécution du calcul du point 6.
La ligne `CODE-LENTILLES-BBIS` cite un code qui applique l'addendum (fiche et empreintes du code corrigé) ; la fiche porte le chemin et
l'empreinte de l'addendum scellé ; le code les compare à la ligne `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` avant toute requête ou
ouverture, et le manifeste et les tables les citent à côté de l'empreinte du texte. « Liste d'arrêt », ajout :
`ADDENDUM-CONCENTRATION-LENTILLES-BBIS` absente, en plusieurs lignes, inscrite après `CODE-LENTILLES-BBIS` ou après
`ENTREES-LENTILLES-BBIS`, ou d'une autre empreinte que celle que porte la fiche du code : rien ne part ; nœud.

### EC-5 — « Code neuf » (texte, lignes 637-643 et essais « nuls et statistiques »)

Ajout : le module des statistiques porte la correction sous un nom neuf (R12). Essais ajoutés (R5, cas sain et artefact) :

- **cas sain** : concentration et part de chaque direction nulle égales à un calcul direct, direction par direction, sur les M − 1
  autres (moyenne, écart type de population, quantile par interpolation linéaire sur M − 1 valeurs) ;
- **artefact** : la statistique du texte d'origine (direction nulle comprise) rend des concentrations strictement plus petites ;
  l'essai le voit ;
- **artefact de taux, à petite taille** : sur des scores gaussiens indépendants, M = 19 directions nulles, 128 jetons, la part des
  témoins à p ≤ 0,05 vaut environ 0,045 sous la statistique corrigée et environ 0,47 sous celle du texte d'origine (sortie de la
  simulation, partie A) : un essai à 2 000 répliques, **chaque réplique tirant ses propres 19 directions nulles et sa direction
  témoin**, exige une part entre 0,03 et 0,065 ;
- **arrêt** : variance des autres nulle pour un jeton (jeton constant sur les autres) : arrêt ; deux directions nulles : arrêt ; cas
  sain : trois directions de scores distincts : pas d'arrêt ;
- **clé de l'addendum** (registre jouet) : une seule ligne `ADDENDUM-CONCENTRATION-LENTILLES-BBIS`, inscrite avant
  `CODE-LENTILLES-BBIS` et avant `ENTREES-LENTILLES-BBIS`, de l'empreinte que porte la fiche : accepté ; ligne absente, en deux lignes,
  inscrite après `CODE-LENTILLES-BBIS` ou après `ENTREES-LENTILLES-BBIS`, ou d'une autre empreinte : refus ;
- inchangé : « bornes recalculées égales aux exemples du plan » ; ajouté : égales aux 41 bornes du § 7.

### EC-6 — « Métrique », point 6, vingt premiers jetons, et « Liste d'arrêt » (texte, lignes 334-335, 338-339 et 345 ; table des lignes 527 et suivantes) : garde d'égalité au vingtième rang — point d'écart neuf, soumis à Lazar avant le scellement

**Ce point n'était pas dans le brouillon contre-lu.** Il vient du § 10 de la contre-lecture (« hors du champ, à porter à la mère ») et
de son § 5 ; il est écrit ici comme un écart neuf, que le contre-lecteur vérifie et que Lazar tranche (§ 9, point 7).

- **Ce que le texte dit** : les vingt premiers jetons d'une direction sont ses vingt plus grands scores (k = 20) ; la part au-dessus
  du nul, les comptes de familles, le jeton de début et les comparaisons appariées en dépendent. **Le texte ne dit pas quel jeton
  garder quand le vingtième et le vingt-et-unième score sont égaux.**
- **Ce qui a été trouvé** : le code laisse alors la fonction de tri (`topk`) décider, sans le dire. Le contre-lecteur l'a vu sur des
  jouets à scores arrondis : un écart de part ne paraît que lorsque des égalités tombent au vingtième rang, et il vient du seul choix
  des vingt premiers (les quantiles sans soi sont égaux à un calcul direct, écart nul, et les parts sont égales dès que les vingt
  premiers sont les mêmes : `diag_egalites.py`, `f8b500c9a285958807cf8fcbb3b6683c392d57b95b96cbc207f4b719ab397c7f`, sortie
  `sortie-diag-egalites.txt`, `d8adbaf1af32ff70c42e79df7e65ae833b04f40bcce0ef5b2b7cf39e47618690`, dossier
  `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lecture-addendum-concentration-outils-v1/`, branche principale). Le défaut **préexiste** à la correction de cet addendum (texte et code de la version 1). Aucune sonde réelle
  n'a été lue.
- **Pourquoi une garde et non une règle** : départager (par exemple par l'identifiant du jeton) changerait la définition des vingt
  premiers jetons du texte scellé ; cette règle est écrite dans la version 2 du texte, en brouillon. Sous le texte scellé, l'addendum
  ajoute seulement une garde : **aucun choix n'est fait en silence** (R5).

Ajout (« Métrique », point 6, à la suite de la puce des vingt premiers jetons ; et deux lignes de la « Liste d'arrêt ») :

> **Garde d'égalité au vingtième rang.** Pour chaque liste de vingt premiers jetons, le code relève les vingt-et-un plus grandes
> valeurs. Il y a **égalité au vingtième rang** quand la vingtième et la vingt-et-unième sont égales, par égalité exacte, dans la
> précision où la liste est classée (simple précision). Une égalité ailleurs dans le classement ne compte pas.
>
> (i) **Direction lue** (chaque vecteur, chaque signe, chaque lentille, lentille des logits comprise ; chaque liste qui entre dans
> une table ou une comparaison : vingt premiers par score, vingt premiers par z sous le nul isotrope, listes du témoin de couche) :
> une égalité au vingtième rang **arrête le calcul**, avant toute écriture de table, avec le message nommé **« égalité de score au
> vingtième rang d'une direction lue »**, qui donne la cellule, le pli, le rôle, le vecteur, le signe, la lentille, la couche, la
> liste, les deux identifiants de jeton et la valeur commune ; nœud.
>
> (ii) **Direction nulle** (nul isotrope partagé, nul isotrope refait par direction, nul des signes ; liste par score) : une
> égalité au vingtième rang n'arrête pas à elle seule ; la direction nulle est **marquée**. Pour chaque statistique S qui dépend des
> vingt premiers jetons (part au-dessus du nul ; compte de chaque famille), le code rend, à côté de p, deux bornes :
> p_bas = (1 + #{j non marquée : S(u_j) ≥ S(v)}) / (M + 1) et p_haut = p_bas + (nombre de directions marquées) / (M + 1). Le libellé
> (« Seuil ») est calculé deux fois, avec p_bas sous les deux nuls puis avec p_haut sous les deux nuls. **Libellés égaux** : le
> calcul continue, le libellé est celui-là (il ne dépend d'aucun départage, la règle des libellés étant monotone en p), et le nombre
> de directions marquées, p_bas et p_haut sont écrits dans les tables. **Libellés différents** : arrêt, avec le message nommé
> **« égalité au vingtième rang d'une direction nulle, décisive pour un libellé »**, qui donne la direction lue, la lentille, le nul,
> la statistique, p_bas, p_haut et le nombre de directions marquées ; nœud. Sans direction marquée, p_bas = p = p_haut : rien ne change.
>
> (iii) **Direction témoin** : le compte de calibration ne porte que sur les p de concentration (plan, point 6), où les vingt
> premiers jetons n'entrent pas : pas d'arrêt ; le nombre de témoins à égalité au vingtième rang est écrit par (couche, lentille,
> nul). La concentration, les pôles et les bornes de calibration ne sont pas concernés : aucun n'emploie les vingt premiers jetons.

> « Liste d'arrêt », deux lignes ajoutées : | égalité de score au vingtième rang d'une direction lue | arrêt ; nœud | et
> | égalité au vingtième rang d'une direction nulle, décisive pour un libellé | arrêt ; nœud |.

**Portée, et sa raison.** La garde couvre les trois sortes de directions, mais n'arrête pas de la même façon. Une égalité sur la
direction lue change la liste montrée, sa part, ses familles et ses comparaisons : arrêt. Une égalité sur une direction nulle change
aussi la statistique, par la part ou le compte de cette nulle, donc la valeur p de v d'au plus 1/(M + 1) par nulle marquée : la
garde la compte, borne son effet, et n'arrête que si elle peut changer un libellé. Une égalité sur un témoin ne change aucun compte
du texte : elle est écrite. **Arrêter sur toute direction nulle ou témoin n'est pas recommandé** : la lecture s'arrêterait presque
à coup sûr (ci-dessous), pour un effet qui, le plus souvent, ne change rien.

**Probabilité, ordre de grandeur** (calcul de l'auteur de ce point ; données synthétiques ; **non contre-lu**). Le contre-lecteur
juge l'égalité « improbable sur 89 498 jetons en simple précision, possible si deux jetons gardés ont la même ligne de sortie »
(§ 10) ; ses jouets à scores arrondis n'en donnent pas la fréquence à la taille réelle. Dans un modèle simple (89 498 scores
indépendants de loi normale, arrondis en simple précision ; vingtième et vingt-et-unième rangs tirés par leurs statistiques d'ordre ;
méthode contrôlée contre un tirage direct à un pas d'arrondi de 10⁻³ : 0,0362 contre 0,0364), la fréquence d'une égalité au vingtième
rang est de **7,0 × 10⁻⁶ par direction** (28 sur 4 000 000 ; ± 1,3 × 10⁻⁶) pour des scores centrés ; 3,2 × 10⁻⁵ si la moyenne des
scores vaut dix écarts types, 2,8 × 10⁻⁴ si elle en vaut cent (l'arrondi pèse plus quand les scores sont grands devant leur
dispersion). Soit, pour des scores centrés : rare pour une direction lue ; 0,014 direction marquée attendue par jeu de 2 000
directions nulles ; mais **1,4 égalité attendue sur les ≈ 195 000 lectures du calcul** (texte, plan, point 6), c'est-à-dire au moins
une avec une probabilité d'environ 0,74 (1 − e^(−1,36)), et davantage si les scores ne sont pas centrés (6 et 54 égalités attendues
aux deux autres lignes). Si deux jetons gardés ont la même ligne de sortie, leurs scores sont égaux pour toute direction : ils
occupent les rangs vingt et vingt-et-un environ une fois sur 89 498 par direction, soit ≈ 2 égalités attendues de plus sur 195 000
lectures par paire de tels jetons (ordre de grandeur, rangs tenus pour équiprobables). **Ce ne sont pas des mesures sur la lentille
réelle** : les scores réels ne sont ni indépendants ni gaussiens. Programme et sortie, hors du dépôt à l'écriture (bloc-notes de la
session des lentilles, dossier `piece-egalites/`), que la mère verse sous `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/`
avant le scellement, mêmes empreintes : `frequence_egalite_vingtieme_rang_v1.py`,
`b1d0d47439be89d7380aa81c08f08ae83b0f92053b3dbefda27810e6be97d5b2` ; `sortie-frequence-egalite-vingtieme-rang-v1.txt`,
`26f4abba8e5816165b5cb01bdba969ff90af570791578967ac6c7d666cc02e74` (entropie du texte, clés neuves
`lentilles-bbis/addendum-concentration-v1/egalite-vingtieme-rang/…`, R9).

**Essais** (R5 ; écrits par le développeur du code, non par l'auteur de ce point ; cas sain et artefact pour chaque étage) :

- **cas sain** : scores tous distincts : aucun arrêt, aucune direction marquée, p_bas = p = p_haut ; égalités placées ailleurs
  (rangs 5 et 6 ; rangs 21 et 22) dans une direction lue : aucun arrêt ;
- **artefact, direction lue** : lentille jouet dont deux jetons ont la même ligne de sortie, direction choisie pour qu'ils tiennent
  les rangs 20 et 21 : arrêt, message (i), les deux identifiants rendus ; la garde appliquée aux scores de la direction de signe
  opposé, où ces deux jetons sont en queue de classement : pas d'égalité au vingtième rang ; une égalité de z aux rangs 20 et 21
  de la liste par z : arrêt ;
- **direction nulle, cas sain** : une direction nulle à égalité au vingtième rang, libellé égal aux deux bornes : pas d'arrêt, une
  direction marquée écrite, p_haut − p_bas = 1/(M + 1) ;
- **direction nulle, artefact** : jouet à M = 99 où, pour une famille, p_bas = 0,01 sous les deux nuls et p_haut = 0,02 sous l'un
  d'eux (une direction marquée ; libellé « sur-représentée » à une borne seulement) : arrêt, message (ii) ;
- **témoin** : un témoin à égalité au vingtième rang : pas d'arrêt, compte écrit, compte de calibration inchangé ;
- **liste de moins de vingt-et-un jetons** (jouets seulement) : pas de vingt-et-unième valeur : garde sans objet, écrit.

## 4. Ce que le code fait

Cinq décisions, une ligne chacune, plus l'arrêt ; le développeur ne choisit rien.

1. **Quantile 0,99 des M − 1 autres** : interpolation linéaire, la même règle que pour les M directions, appliquée aux 1 999 valeurs
   (rang fractionnaire 0,99 × 1 998 = 1 978,02).
2. **Direction lue et directions témoins** : elles gardent la moyenne, l'écart type et le quantile calculés sur les **M** directions
   nulles ; seules les directions nulles sont jugées sans elles-mêmes (option 2 du rapport : « inchangé pour v et les témoins »).
3. **z des tables** (vingt premiers jetons, z sous chaque nul, classement par z, rang empirique parmi les M scores nuls) : inchangé,
   calculé sur les **M** directions nulles.
4. **Bornes de calibration** : valeurs inchangées ; loi de référence bêta-binomiale (n ; 100 ; 1 901) par jeu, somme de lois
   indépendantes pour des jeux mis en commun, q_bas le plus grand entier tel que P(X < q_bas) ≤ 10⁻⁴, q_haut le plus petit tel que
   P(X > q_haut) ≤ 10⁻⁴ ; les 41 valeurs sont au § 7.
5. **Repli par direction et pôles** : le nul isotrope refait par direction (garde du rapport à ε) et ses 200 témoins par vecteur
   suivent **la même règle** que le nul partagé (directions nulles sans elles-mêmes, témoins sur les M) ; le nul des signes aussi ; les
   **pôles sont inchangés** (cosinus maximal, rang parmi les maxima nuls : ni moyenne, ni écart type, ni quantile) ; les comptes de
   familles et le jeton de début aussi.
6. **Arrêt** : variance des M − 1 autres nulle, ou au plus 10⁻¹⁰ fois celle des M, pour un jeton : arrêt ; moins de trois directions
   nulles : arrêt (sans objet à M = 2 000 ; utile aux essais jouets).
7. **Garde d'égalité au vingtième rang** (ajout de la version corrigée, EC-6, soumis à Lazar) : direction lue : arrêt nommé ;
   direction nulle : marquée, p_bas et p_haut rendus, arrêt nommé si le libellé diffère entre les deux ; témoin : compté et écrit.
   Sans égalité, aucune valeur ne change.

**Les six hypothèses du développeur** (note `traitement-contre-lecture-v1-complement-1.md`, § 3, `8b34c66e…`) sont **toutes
reprises, sans écart** : (1) interpolation linéaire sur 1 999 valeurs ; (2) écart type de population ; (3) direction lue, témoins et z
des tables sur les M directions ; (4) familles et pôles inchangés, repli par direction sous la même règle ; (5) bornes de calibration
inchangées : `audits_v1` les porte déjà, aucun `audits_v2` n'est demandé par l'addendum ; (6) arrêt sur variance des autres nulle à
10⁻¹⁰ près, ou moins de trois directions. Les formules de `statistiques_v2.py` (`b6c291e3…`, `concentrations_sans_soi`) sont celles de
EC-1. L'auteur n'a ni joué ni contre-lu ce code : sa revérification revient au contre-lecteur du code. La note rapporte un banc à
taille réelle sur matrices aléatoires (5,15 % et 4,90 % de témoins à p ≤ 0,05 après correction, 6,05 % et 5,80 % avant) : chiffres
rapportés par la note, **non vérifiés par l'auteur**, qui n'a pas ouvert la sortie de ce banc.

## 5. Ce qui ne change pas

Directions lues, lecture, rapport à ε, les deux nuls et leurs graines, M = 2 000, z et vingt premiers jetons de la direction lue,
familles, jeton de début, pôles, comparaisons appariées, « Seuil » (niveaux des libellés, attendu par le seul hasard), « Critères de
lecture gelés », phrases gelées, audits de symétrie, nombres de témoins, bornes de calibration, montage, entrées, cloisonnement, coût
(0 USD, au processeur). Le coût de calcul ajouté est une passe sur le tableau des scores nuls et les statistiques d'ordre des vingt
premiers jetons de chaque direction nulle.

## 6. Validité approchée de la statistique corrigée

**Verdict** : l'ordre 1/M² annoncé par la fiche de décision tient pour les **lois de chaque statistique** ; pour la **valeur p**, il
tient quand les jetons sont indépendants ; quand les scores des jetons sont corrélés, il reste un terme d'ordre **1/M**, de signe
**conservateur** (valeurs p un peu trop grandes), mesuré ci-dessous. C'est plus faible que ce que la fiche annonçait : point ouvert
n° 1 du § 9.

**(a) Le schéma exact, pour repère.** Sous le nul, la direction lue v et les M directions nulles sont M + 1 tirages échangeables. Si
chaque direction était jugée contre les M autres (v contre les M nulles ; chaque nulle contre les M − 1 autres nulles **et v**), les
M + 1 concentrations seraient échangeables et la valeur p serait exacte : P(p ≤ k/(M + 1)) = k/(M + 1), sans égalités. La simulation
le retrouve (colonne « exacte » : 0,0496 à 0,0504 pour 0,05).

**(b) Ce que fait la statistique corrigée.** v est jugée contre M directions ; chaque nulle contre M − 1 (v n'y est pas). Par
indépendance, la concentration corrigée de u_j a **exactement** la loi de la concentration d'une direction fraîche jugée contre M − 1
directions ; celle de v, la loi d'une direction fraîche jugée contre M. Les deux lois ne diffèrent que par la taille du jeu de
référence, M − 1 contre M. Une loi qui dépend de cette taille n par un développement en 1/n (L_n = L_∞ + A/n + …) donne
L_M − L_{M−1} = −A/(M(M − 1)) + … : **ordre 1/M²**. La statistique du texte d'origine, elle, différait à l'ordre 1/M.

**(c) Calcul exact dans le modèle gaussien** (jetons indépendants, scores gaussiens ; programme
`validite_gaussienne_statistique_corrigee_v2.py`, sortie `3dbd64f3…`). Le z d'un jeton suit √((M + 1)/(M − 1)) × Student(M − 1) pour
v, √(M/(M − 2)) × Student(M − 2) pour une direction nulle jugée sans elle-même. À la taille du texte (89 498 jetons), en tenant les
concentrations nulles pour indépendantes :

| niveau | nominal | texte d'origine | statistique corrigée | écart relatif de la corrigée |
|---|---|---|---|---|
| p ≤ 0,05 | 0,049975 | 0,057819 | 0,049972874 | −4,3 × 10⁻⁵ (= −171/M²) |
| p ≤ 0,01 | 0,009995 | 0,012072 | 0,009994457 | −5,5 × 10⁻⁵ (= −218/M²) |
| p ≤ 0,001 | 0,001000 | 0,001283 | 0,000999429 | −7,1 × 10⁻⁵ (= −284/M²) |

Pour M de 250 à 16 000, l'écart relatif de la corrigée multiplié par M² reste entre −166 et −172 : c'est bien un ordre 1/M². Le modèle
rend 5,78 % pour le texte d'origine, à côté des 5,71 % du banc. **Avec M = 2 000 : la part des p ≤ 0,05 passe de 0,049975 à
0,049973 ; l'écart est conservateur et cent fois sous la résolution d'une valeur p (1/2 001).** Pour la part au-dessus du nul, avec
des scores de loi uniforme : une direction lue dépasse le quantile de n autres avec la probabilité 0,01 + 0,98/(n + 1), soit
0,010489755 (n = M) contre 0,010490000 (n = M − 1) : écart 0,98/(M(M + 1)) = 2,4 × 10⁻⁷, contre 0,010000 avec elle-même.

**(d) Le terme de couplage, que (b) et (c) ne voient pas.** Dans le schéma exact, v entre dans la moyenne et l'écart type de chaque
nulle ; dans la statistique corrigée, non. Ajouter v à la référence de u_j change son z au jeton t, au premier ordre, de
−[z·(ζ² − 1)/2 + ζ]/M, où ζ est le z de v au même jeton. En moyenne sur v ce terme est nul (d'où l'ordre 1/M² des lois). Mais la
valeur p compare u_j à v quand v est extrême : si le jeton où u_j culmine est corrélé (corrélation ρ) au jeton où v culmine, à la
hauteur c, ζ vaut environ ρ·c et le terme ne s'annule plus. Les nulles corrigées sont alors plus hautes que dans le schéma exact, d'un
écart relatif de leur z ≈ [ρ²(c² − 1)/2 + ρ]/M (sur la part des valeurs p au seuil, l'écart relatif est environ c·h fois plus grand,
h étant le hasard de la concentration au seuil, voisin de c) : **valeurs p plus grandes, sens conservateur**, pour toute corrélation positive ou forte. Le
terme ne peut devenir anti-conservateur que pour une corrélation faiblement négative (entre −2/(c² − 1) et 0), et alors d'au plus
≈ (c² + 1)/(2(c² − 1)·M) en relatif sur la part : moins de 0,03 % à M = 2 000. Ce calcul est un **développement au premier ordre, non
un théorème**.

**(e) Mesure du couplage par simulation jointe** (données synthétiques ; § 8 ; sortie `4ee7b11e…`, partie A : 128 jetons, différence
appariée entre la statistique corrigée et le schéma exact, sur les mêmes tirages, niveau 0,05) :

| scénario | M = 19 | M = 39 | M = 79 | M = 159 | lecture |
|---|---|---|---|---|---|
| scores gaussiens indépendants | −0,00551 ± 0,00011 | −0,00167 ± 0,00008 | −0,00073 ± 0,00008 | −0,00020 ± 0,00009 | proche de (c) : −0,0053, −0,0014, −0,0004, −0,0001 ; reste entre 0 et −0,6/M en relatif (un jeton commun sur 128) |
| queues lourdes (Student à 5 degrés) | −0,00253 ± 0,00008 | −0,00062 ± 0,00006 | −0,00023 ± 0,00006 | −0,00021 ± 0,00006 | même ordre |
| miniature structurée, largeur 32 | −0,01200 ± 0,00013 | −0,00597 ± 0,00010 | −0,00298 ± 0,00010 | −0,00136 ± 0,00010 | **ordre 1/M** : −4,6, −4,7, −4,7, −4,3 /M en relatif |
| miniature structurée, largeur 128 | −0,01160 ± 0,00012 | −0,00561 ± 0,00009 | −0,00265 ± 0,00009 | −0,00152 ± 0,00010 | **ordre 1/M** : −4,4, −4,4, −4,2, −4,8 /M en relatif |

Sur les mêmes tirages, la statistique du texte d'origine s'écarte de +56 à +180/M en relatif (parts de 0,068 à 0,53 pour 0,05).
Toutes les différences mesurées de la statistique corrigée sont **négatives** (conservatrices). Dans la miniature structurée (lignes
de la matrice de sortie à direction commune, donc jetons corrélés), le résidu vaut ≈ −4,5/M : **douze fois plus petit que le biais
corrigé, et de sens opposé**. Porté à M = 2 000, il ferait −0,23 % en relatif (0,04986 au lieu de 0,04998).

**(f) À la taille M = 2 000** (partie B de la simulation : 1 024 jetons, 2 000 jeux de 1 000 témoins par scénario), part des témoins à
p ≤ 0,05 sous la statistique corrigée : 0,04976, 0,05001, 0,04972, 0,04996 (± 0,00019 chacune) pour 0,049975 attendu ; sous le texte
d'origine : 0,05303, 0,05196, 0,05210, 0,05459. La statistique corrigée est au niveau nominal à l'erreur près ; le résidu de couplage
attendu (≈ 0,0001) est sous cette erreur.

**(g) Ce que cela donne pour la lecture réelle.** À M = 2 000 : résidu des lois de −4 × 10⁻⁵ à −7 × 10⁻⁵ en relatif, négligeable ;
résidu de couplage conservateur, d'une taille qui dépend des corrélations entre les scores des jetons de la lentille réelle,
**inconnues ici** : ≈ −0,2 % dans les miniatures, au niveau 0,05 ; l'estimation au premier ordre de (d) va jusqu'à quelques pour cent
pour des jetons fortement corrélés. Le terme **grandit aux niveaux plus stricts** : la contre-lecture l'estime, dans des lois
gaussiennes inventées à jetons corrélés, de −0,1 % à −0,5 % au niveau 0,05 (89 498 jetons, M = 2 000) et de l'ordre de −1 % à −3 % au
niveau 0,001 du libellé « concentrée » (8 192 jetons) ; toujours conservateur. Ce n'est pas une mesure sur la lentille réelle. Le banc du contre-lecteur du code (0,0513, dont l'auteur estime l'erreur type à ≈ 0,0009 sur 56 jeux) ne le résout
pas. **Sens de l'erreur restante : la lecture penche très légèrement vers « non distincte du nul », jamais vers « se distingue »** (au
terme anti-conservateur borné de (d) près). La calibration du texte mesure cette part même (les témoins sont jugés comme v) : un
résidu plus fort qu'attendu se verrait dans les comptes, écrits dans les tables.

**Part au-dessus du nul** : sous la statistique corrigée, la part moyenne des directions nulles égale celle des témoins (écarts
+0,00004, −0,00006, −0,00016, +0,00005, ± 0,00014 à 0,00018) ; sous le texte d'origine elle est plus basse de 0,005 à 0,024. La part
des témoins à p ≤ 0,05 reste sous 0,05 (0,041 à 0,045) : la statistique ne prend que 21 valeurs, les égalités rendent sa valeur p
conservatrice, avant comme après la correction.

## 7. Bornes de calibration sous la statistique corrigée, et risque de sortie

**Loi du compte.** Sachant les M directions nulles d'un jeu, ses n témoins sont indépendants : le compte des p ≤ 0,05 suit **exactement**
une loi binomiale (n ; π), π étant la probabilité qu'un témoin dépasse la 100ᵉ plus grande concentration nulle du jeu. Le compte est
donc un **mélange de lois binomiales**, avant comme après la correction. Il est bêta-binomial (n ; 100 ; 1 901) si π
suit la loi bêta (100 ; 1 901), ce qui est vrai quand la concentration d'un témoin et les M concentrations nulles sont indépendantes
et de même loi. Le texte appelait cette loi « exacte » : elle ne l'était pas sous sa statistique (moyenne de π ≈ 0,057). Sous la
statistique corrigée elle **n'est pas exacte non plus, mais approchée à l'ordre du § 6** : moyenne de π égale à 100/2 001 au résidu
près, dispersion mesurée ci-dessous. **Rien ne la remplace** : elle devient la « loi de référence, approchée », et les bornes gardent
leur règle et leurs valeurs.

**Contrôle par simulation** (partie B, M = 2 000, 2 000 jeux par scénario ; référence : moyenne 49,975 et variance 71,17 pour
n = 1 000 ; 9,995 et 10,44 pour n = 200) :

| scénario | n = 1 000 : variance / référence | hors de l'intervalle à 1 % par côté (attendu 0,0177) | n = 200 : variance / référence | hors (attendu 0,0116) |
|---|---|---|---|---|
| gaussien | 0,935 | 0,0145 | 0,959 | 0,0105 |
| structuré, largeur 128 | 1,047 | 0,0235 | 0,983 | 0,0095 |
| structuré, largeur 512 | 1,057 | 0,0190 | 1,047 | 0,0145 |
| queues lourdes | 1,026 | 0,0200 | 1,047 | 0,0150 |

(erreur type du rapport des variances ≈ 0,04 ; des fréquences ≈ 0,003). La loi de référence décrit le compte à l'erreur de la
simulation près ; une sur-dispersion de l'ordre de 5 % dans les scénarios structurés n'est ni établie ni exclue. Sorties des bornes
du texte sur 8 000 jeux de 1 000 témoins : 0 ; sur 8 000 jeux de 200 : 2 (attendu ≈ 1). La simulation ne peut pas vérifier un risque de
10⁻⁴ ; elle vérifie la moyenne, la dispersion et les queues à 1 %.

**Bornes recalculées** (programme neuf `bornes_calibration_statistique_corrigee_v2.py`, sortie `39a410e4…` ; il retrouve les quatre
exemples du texte et les quatre bornes du rapport) : nul isotrope partagé, un jeu de 1 000 témoins : **[23, 85]**, risque de sortie
1,83 × 10⁻⁴. Jeux de 200 témoins mis en commun (nul des signes ; nul isotrope refait par direction), par nombre k de vecteurs de la
couche, bornes et risque de sortie sous la loi de référence :

1 : [1, 24] (1,28e-04) ; 2 : [6, 39] (1,72e-04) ; 3 : [12, 53] (1,59e-04) ; 4 : [18, 66] (1,33e-04) ; 5 : [26, 79] (1,78e-04) ;
6 : [33, 92] (1,43e-04) ; 7 : [41, 104] (1,76e-04) ; 8 : [48, 116] (1,51e-04) ; 9 : [56, 128] (1,58e-04) ; 10 : [64, 140] (1,57e-04) ;
11 : [72, 152] (1,51e-04) ; 12 : [81, 164] (1,72e-04) ; 13 : [89, 176] (1,56e-04) ; 14 : [97, 187] (1,62e-04) ;
15 : [106, 199] (1,70e-04) ; 16 : [114, 210] (1,70e-04) ; 17 : [123, 222] (1,73e-04) ; 18 : [131, 233] (1,68e-04) ;
19 : [140, 245] (1,66e-04) ; 20 : [149, 256] (1,85e-04) ; 21 : [157, 267] (1,75e-04) ; 22 : [166, 279] (1,68e-04) ;
23 : [175, 290] (1,81e-04) ; 24 : [183, 301] (1,68e-04) ; 25 : [192, 312] (1,78e-04) ; 26 : [201, 323] (1,86e-04) ;
27 : [210, 335] (1,74e-04) ; 28 : [219, 346] (1,81e-04) ; 29 : [228, 357] (1,87e-04) ; 30 : [236, 368] (1,69e-04) ;
31 : [245, 379] (1,73e-04) ; 32 : [254, 390] (1,76e-04) ; 33 : [263, 401] (1,79e-04) ; 34 : [272, 412] (1,80e-04) ;
35 : [281, 423] (1,82e-04) ; 36 : [290, 434] (1,82e-04) ; 37 : [299, 445] (1,82e-04) ; 38 : [308, 456] (1,82e-04) ;
39 : [317, 467] (1,81e-04) ; 40 : [326, 478] (1,80e-04).

**Risque de sortie attendu** (probabilité qu'une calibration saine sorte de ses bornes) : sous la loi de référence, entre
1,28 × 10⁻⁴ et **1,87 × 10⁻⁴** par calibration (au plus 2 × 10⁻⁴ par construction) ; pour une lecture entière, au plus douze
calibrations qui portent des libellés (trois couches, deux lentilles, deux nuls ; avec le repli par direction, celle du nul partagé,
dont les lectures sont alors « remplacées », s'y ajoute : dix-huit au plus, 3,4 × 10⁻³) : au plus 2,2 × 10⁻³ par borne de réunion. Sensibilité, si la part vraie
s'écarte de 100/2 001 (même dispersion, moyenne déplacée) :

| part vraie | un jeu de 1 000 | 6 jeux de 200 | 13 jeux | 20 jeux | 40 jeux |
|---|---|---|---|---|---|
| référence (0,049975) | 1,83e-04 | 1,43e-04 | 1,56e-04 | 1,85e-04 | 1,80e-04 |
| résidu des lois, × (1 − 10⁻⁴) | 1,83e-04 | 1,43e-04 | 1,56e-04 | 1,85e-04 | 1,80e-04 |
| couplage conservateur, × 0,99 | 1,88e-04 | 1,48e-04 | 1,71e-04 | 2,15e-04 | 2,25e-04 |
| × 0,98 | 2,03e-04 | 1,66e-04 | 2,18e-04 | 3,03e-04 | 3,93e-04 |
| × 0,95 | 3,13e-04 | 3,10e-04 | 6,30e-04 | 1,17e-03 | 2,67e-03 |
| × 0,90 | 8,30e-04 | 1,09e-03 | 3,79e-03 | 9,48e-03 | 3,70e-02 |
| 0,0513 (banc, sans elle-même, lecture pessimiste) | 2,15e-04 | 1,92e-04 | 2,67e-04 | 3,84e-04 | 6,69e-04 |
| 0,0571 (texte d'origine, pour mémoire) | 1,75e-03 | 3,30e-03 | 1,37e-02 | 3,59e-02 | 1,59e-01 |

Lecture : avec la correction, le risque de perdre à tort une couche reste sous 0,1 % dans tous les cas plausibles (résidu jusqu'à
−2 %, ou part du banc), contre jusqu'à 16 % sous le texte d'origine. Une sortie rend « non calculables » les tables de cette couche,
de cette lentille et de ce nul (« Liste d'arrêt », inchangée) : la garde échoue du côté sûr.

## 8. Simulation : plan, graines, ce que l'auteur a vu

- **Statut** : simulation d'appui, **descriptive, non décisive** ; aucune porte, aucun libellé, aucune borne n'en dépend (les bornes
  viennent du calcul exact). Données synthétiques seulement, au processeur de la session (quatre processus, 1 980 s).
- **Graines (R9)** : `numpy.random.SeedSequence(entropy=E, spawn_key=(entier des 8 premiers octets du SHA-256 de la clé,))`, PCG64, E
  = entropie du texte (`207246359357165180107189867815730235805`) ; **clés neuves**, propres à l'addendum, jamais employées par la
  lecture : `lentilles-bbis/addendum-concentration-v1/simulation-A/<scénario>/M<M>/bloc<i>` (i de 0 à 7),
  `…/simulation-B/<scénario>/bloc<i>` (i de 0 à 15), `…/monde/structure-<D>/<A|B>`.
- **Ordre, déclaré** : l'auteur a joué deux essais courts (échelles 0,01 et 0,002) pour éprouver le programme, **et en a vu les
  chiffres**, avant la course à la taille déclarée ; après le premier, il a ajouté une seconde largeur à la miniature structurée
  (32 et 128 en partie A, 128 et 512 en partie B) pour voir si le résidu dépendait de la largeur. La course rendue est la seule à la
  taille déclarée ; aucune n'a été rejouée ni écartée. Le programme des bornes a été rejoué une fois, après l'ajout de lignes de
  sensibilité (parts × 0,99 à × 0,90), une fois le terme de couplage vu : les bornes elles-mêmes n'ont pas changé.
- **Limite** : les miniatures (128 ou 1 024 jetons, largeur 32 à 512) n'imitent la lentille réelle qu'en structure ; la taille du
  résidu de couplage sur les scores réels n'est pas mesurée ici. Elle le sera, sans rien ouvrir de plus, par les comptes de calibration
  du calcul.

## 9. Points ouverts avant le scellement

1. **L'ordre 1/M² ne tient qu'en partie** (§ 6) : la fiche de décision annonçait une « différence d'ordre 1/M² » ; l'auteur trouve
   cet ordre pour les lois, et un résidu de couplage d'ordre 1/M, conservateur, quand les jetons sont corrélés. La décision (option 2)
   n'en est pas changée dans son sens : le biais anti-conservateur est retiré et l'erreur restante est du côté sûr. Mais c'est un fait
   donné au directeur qui est corrigé : la mère dit si Lazar doit en être informé avant le scellement. À contre-lire en priorité : le
   développement du § 6 (d) et le signe.
2. **Voie exacte, non retenue, signalée** : le schéma échangeable du § 6 (a) (chaque nulle jugée avec v comprise) serait exact, mais
   coûte une passe sur les scores nuls par direction lue et par témoin ; l'option 3 de la fiche (jeu séparé) l'est aussi. Hors de la
   décision ; aucune proposition.
3. **Ligne `CODE-LENTILLES-BBIS`** : l'auteur ignore si elle est déjà inscrite (aucun registre ouvert). Si elle l'est avec un code
   d'avant la correction, la mère choisit la forme (ligne neuve qui cite le code corrigé), et le dit.
4. **Clé neuve du registre propre** (EC-4) : ajout de procédure, au-delà des trois sections nommées par le mandat ; à ratifier ou
   retirer par la mère.
5. **Seuil de 10⁻¹⁰ de l'arrêt** (§ 4, ligne 6) : repris du développeur, sans autre appui.
6. **Sur-dispersion possible du compte** (§ 7) : ≈ 5 % dans les scénarios structurés, à une erreur type et demie ; non établie.
7. **Garde d'égalité au vingtième rang (EC-6) : point d'écart neuf, soumis à Lazar avant le scellement** (écart à un texte scellé :
   nœud, sans défaut ; rien n'est scellé avant son mot).
   - **Décision** : dire ce que fait le code, sous le texte scellé, quand le vingtième et le vingt-et-unième score d'une direction
     sont égaux, et pour quelles directions il s'arrête.
   - **Enjeu** : sans garde, la fonction de tri choisit en silence un des deux jetons ; la part, les familles et les listes montrées
     en dépendent. Avec une garde trop large, la lecture s'arrête presque à coup sûr.
   - **Option 1 — direction lue seulement** : arrêt nommé sur la direction lue ; rien sur les directions nulles ni les témoins.
     Avantage : la plus simple ; arrêt rare (≈ 7 × 10⁻⁶ par direction lue dans le modèle simple de EC-6). Inconvénient : une égalité
     sur une direction nulle reste tranchée en silence par le tri, et peut déplacer une valeur p de 1/2 001.
   - **Option 2 — arrêt sur toute direction, nulles et témoins compris**. Avantage : aucune égalité ne passe. Inconvénient : sur
     ≈ 195 000 lectures, au moins une égalité est attendue avec une probabilité de l'ordre de 0,7 ou plus dans le même modèle ; la
     lecture s'arrêterait donc le plus souvent, et il faudrait alors une règle de départage, donc un second écart au texte scellé.
   - **Option 3 — garde à trois étages, celle écrite en EC-6** : direction lue : arrêt nommé ; direction nulle : marquée, comptée,
     effet borné par p_bas et p_haut, arrêt nommé seulement si le libellé en dépend ; témoin : compté et écrit. Avantage : rien n'est
     tranché en silence, aucun libellé ne dépend d'un départage, et la lecture ne s'arrête que si l'égalité compte. Inconvénient :
     deux colonnes de plus dans les tables et quelques lignes de code et d'essais de plus que l'option 1.
   - **Recommandation** : option 3 ; confiance moyenne à bonne (environ 0,75). L'incertitude porte sur la fréquence réelle des
     égalités, estimée dans un modèle simple et non mesurée sur la lentille. Si Lazar retient l'option 1 ou l'option 2, EC-6 et la
     ligne 7 du § 4 sont repris avant le scellement.
   - **Lien avec la version 2 du texte** : son brouillon 3 écrit une règle de départage (score décroissant, puis identifiant de jeton
     croissant). Sous l'option 3, une première lecture menée à son terme n'a aucune égalité au vingtième rang sur une direction lue,
     et aucun de ses libellés ne dépend du départage des directions nulles : la règle de la version 2 ne peut donc changer ni une
     liste de direction lue ni un libellé de cette première lecture.

## 10. Expositions, et ce que l'auteur a lu

- **Lu** : le texte scellé, lignes 1 à 82, 131 à 195, 303 à 560 et 626 à 674 (en-tête, vocabulaire, hypothèse, prédiction, métrique,
  seuil, plan, critères, liste d'arrêt, lignes de registre, code neuf) ; **non lues** : « Ce que l'auteur savait », « Entrées exactes,
  et ce qui n'est jamais ouvert » et la fin du texte. Le rapport de la contre-lecture du code, en entier. Des outils du
  contre-lecteur : le banc, sa sortie, le programme du risque et sa sortie. Le programme des bornes du texte et sa sortie. La note du
  développeur et `statistiques_v2.py` (commit `e2e24cac`), sur l'autorisation de la mère. Les **titres seulement** (18 lignes, par
  `grep`) du premier addendum d'écart de l'apprentissage des sondes sur la tâche, pour la forme d'un addendum. Trois messages de la
  mère (cinq points du développeur ; six hypothèses ; reprise).
- **Jamais ouverts** : aucun fichier de la liste « jamais ouverts » du texte ; aucune sortie, aucun score, aucune table, aucune
  lecture, aucun verdict de l'apprentissage des sondes sur la tâche ; aucune table de la lecture par lentille ; aucune branche
  `donnees/*` ni `calcul/*` ; aucun `diag/` ni `runs/` ; aucun registre ; rien d'autre de la branche du développeur.
- **Vu par des listes de noms seulement** : les noms de fichiers de `prereg/` et de deux dossiers de `docs/notes/` dans l'arbre de
  travail (dont deux brouillons « v2 » de ce texte, non ouverts).
- **Actions** : deux `git fetch` en lecture (branche principale, branche du développeur) ; aucun commit, aucun push, aucune machine,
  aucune dépense, aucun modèle chargé, aucun fichier existant modifié. Fichiers créés : cet addendum, les six pièces du dossier
  `prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/`, leurs empreintes compagnons.
- **Refus d'outil** : aucun refus de permission. Une limite de session a interrompu le travail ; reprise sur le message de la mère.
- **Arbre de travail** : la session est sur la branche `claude/brave-galileo-jhp684`, où le texte scellé et le dossier des pièces ne
  sont pas ; l'addendum et ses pièces y sont posés comme fichiers neufs, non suivis ; la mère les verse sur la branche qu'elle choisit.

## 11. Fichiers à donner au contre-lecteur (R2)

Cet addendum ; le texte scellé (`ca5066d7…`), sections « Métrique », « Seuil », « Plan d'analyse », « Liste d'arrêt » ; le rapport
(`679eb723…`), § 5 ; la sortie du banc (`0101c9aa…`) ; les six pièces neuves (programmes et sorties, empreintes en tête) ; la note du
développeur (`8b34c66e…`), § 3, et `statistiques_v2.py` (`b6c291e3…`). À vérifier d'abord : les lignes citées du texte (avant) ; les
formules de EC-1 ; la règle du quantile de EC-2 ; le § 6 (d) et (e) ; les 41 bornes contre un calcul indépendant ; que le programme de
simulation calcule bien les trois statistiques qu'il nomme.

## 12. Version corrigée après la contre-lecture : ce qui a changé depuis le brouillon 1

Fabriquée par programme à partir du brouillon 1 (`0a862760…`) : remplacements exacts, chaque texte « avant » trouvé une fois et une
seule ; les couples sont extraits par programme du § 9 de la contre-lecture (`715ddfa7…`) ; contrôle par `diff` contre le brouillon 1.

| changement | où | nature |
|---|---|---|
| statut | en-tête, puce « Statut » | version corrigée, à vérifier par le même contre-lecteur, puis à sceller par la mère |
| **C1** (obligatoire) | § 3, EC-4 | clé de l'addendum avant `CODE-LENTILLES-BBIS` aussi ; fiche du code, vérification par le code, manifeste et tables ; « Liste d'arrêt » étendue |
| **C2** (obligatoire) | § 3, EC-5, puce « arrêt », et puce neuve « clé de l'addendum » | essais des deux gardes neuves (moins de trois directions ; clé de registre) |
| **C3** (obligatoire) | § 3, EC-5, puce « artefact de taux » | chaque réplique tire ses 19 directions nulles et sa direction témoin |
| **C4** (obligatoire) | § 6 (g) | le résidu de couplage grandit aux niveaux stricts ; chiffres de la contre-lecture |
| **C5** (obligatoire) | § 3, EC-1, sous les formules | précision de la comparaison C(u_j) ≥ C(v) |
| **F1** (facultatif, pris) | § 6 (d) | le crochet est un écart relatif du z, non de la part : erreur de fait corrigée |
| **F2** (facultatif, pris) | § 7, « Loi du compte » | « si et seulement si » était faux : « si » |
| **F3** (facultatif, pris) | § 7, « Risque de sortie attendu » | calibration du nul partagé ajoutée au compte en cas de repli par direction |
| **EC-6** (neuf, hors contre-lecture) | § 3, après EC-5 ; § 4, ligne 7 ; § 9, point 7 | garde d'égalité au vingtième rang ; soumis à Lazar |
| ce § 12 | fin | ajouté |

- **Pourquoi les trois couples facultatifs sont pris** : chacun retire une phrase que le contre-lecteur a montrée fausse ou
  incomplète (F1 : grandeur mal nommée ; F2 : équivalence fausse ; F3 : compte de calibrations incomplet), aucun ne change une borne,
  une valeur ni une règle ; un texte scellé ne garde pas une erreur connue. Le rédacteur des corrections a relu les trois : F2 par le
  raisonnement (un mélange de lois binomiales de taille n n'est fixé que par les n premiers moments de la loi de mélange) ; F3 par le
  compte (douze fois 1,87 × 10⁻⁴ = 2,2 × 10⁻³ ; dix-huit fois : 3,4 × 10⁻³) ; F1 sur le développement du § 2.1 de la contre-lecture,
  non refait.
- **Aucun couple ne s'est trouvé inapplicable** : les huit textes « avant » paraissent une fois chacun dans le brouillon 1.
- **Points ouverts du § 9 après la contre-lecture** (son § 6) : 1 : confirmé en partie, C4 l'écrit ; la contre-lecture recommande une
  ligne de réserve à Lazar, sans demande de mot neuf ; 2 : aucune proposition ; 3 : la ligne `CODE-LENTILLES-BBIS` n'est pas encore
  inscrite (relevé du contre-lecteur), la question de forme tombe avec C1 ; 4 : clé à ratifier par la mère, avec C1 ; 5 : seuil de
  10⁻¹⁰ justifié par une identité exacte (contre-lecture, § 6, point 5) ; 6 : ni établie ni exclue, non reproduite à une entropie
  neuve, sans conséquence pour les bornes ; 7 : neuf, à Lazar. Les points 1 à 6 gardent leurs mots du brouillon 1.
- **Hors de cet addendum** (contre-lecture, § 10) : la correction de la statistique et une règle de départage sont portées dans le
  brouillon 3 de la version 2 du texte ; l'essai « artefact » de EC-5 (« concentrations strictement plus petites ») ne vaut que si le
  plus grand z de la nulle est positif : à garder en tête pour un jouet à très peu de jetons, sans changement ici.
- **Ce que le rédacteur des corrections a lu** : le brouillon 1 en entier ; la contre-lecture en entier ; de ses outils,
  `diag_egalites.py`, sa sortie et la ligne de commande qui la produit ; du texte scellé (`ca5066d7…`, branche principale), les
  lignes 330 à 348, 360 à 382, 456 à 470, 525 à 552 et 626 à 674 ; du brouillon 2 de la version 2 du texte, les passages de la
  statistique, des vingt premiers jetons et de la calibration. **Jamais ouverts** : aucune sonde, aucun score, aucune table, aucune
  lecture, aucun verdict de l'apprentissage des sondes sur la tâche, aucune branche `donnees/*` ni `calcul/*`, aucun registre.
  Aucune machine, aucune dépense, aucun modèle chargé, aucun commit, aucun push ; un programme sur données synthétiques, au
  processeur (EC-6).
- **À donner au contre-lecteur pour la vérification** : cette version ; le brouillon 1 (`0a862760…`) ; sa contre-lecture
  (`715ddfa7…`) ; pour EC-6 : le texte scellé, lignes 334 à 345, « Seuil » et « Liste d'arrêt » ; `diag_egalites.py` et sa sortie ;
  le programme `frequence_egalite_vingtieme_rang_v1.py` et sa sortie. À vérifier d'abord : que les huit couples sont appliqués à la
  lettre et que rien d'autre n'a changé hors des endroits de la table ; pour EC-6 : la monotonie de la règle des libellés en p, la
  formule de p_bas et p_haut, et l'ordre de grandeur de la fréquence.
