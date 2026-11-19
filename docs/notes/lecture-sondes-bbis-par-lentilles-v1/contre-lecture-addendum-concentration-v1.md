# Contre-lecture de l'addendum « concentration » de la lecture des sondes par la lentille publique — v1

- **Contre-lecteur** : agent neuf, sous-agent de la session mère, modèle servi **Opus 5.5** (`claude-opus-5-5`). Il n'a écrit ni le
  texte scellé, ni l'addendum, ni le code, ni la contre-lecture du code ; il ne sera ni développeur, ni opérateur, ni lecteur de cette
  lecture. L'auteur de l'addendum est sur Fable 5.2 : la contre-lecture est faite par un autre modèle.
- **Date (UTC)** : 2026-11-19 ; premières lectures avant 12:29:50 (première heure relevée) ; programmes joués de 12:29 à 13:47 ; rapport
  écrit ensuite.
- **Pièce contre-lue** (classe A : addendum d'écart à un texte scellé ; mot de Lazar GO-2026-11-19-47, R-3771, ligne relue dans
  `registres/go.md` de la branche principale) : `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`, branche
  `claude/brave-galileo-jhp684`, commit `6de58b8cab4b1500dcae887bb73a40864bea7a4b`, lue dans un arbre détaché du bloc-notes ;
  `0a862760025caf11ff66578dc47c53143ee480c173a733920b9f4b9425d59546`, recalculée, égale au mandat et à son compagnon (« l'addendum »).
- **Six pièces de l'addendum** (`prereg/pieces-lecture-sondes-bbis-par-lentilles-v1/`), empreintes recalculées, égales au mandat et à
  leurs compagnons : programme des bornes `0f31484b…` et sa sortie `39a410e4…` ; calcul dans le modèle gaussien `39e73833…` et sa
  sortie `3dbd64f3…` ; simulation `78e115da…` et sa sortie `4ee7b11e…`.
- **Textes de référence, empreintes recalculées** : texte scellé `prereg/lecture-sondes-bbis-par-lentilles-v1.md`, branche principale
  (tête `15d1df0058582e7d82c5ad97f1a49ea1680c30fd`), `ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572` (« le texte ») ;
  rapport de la contre-lecture du code `679eb7232eed0c154743348102cccd40c05b8f38b1f730eeb21b24f171af155d` (§ 5 et fiche de décision) ;
  sortie du banc de ce contre-lecteur `0101c9aaaca97b5e1fc9a17e3230ae0b5f1806131a19ca452147e4799df62d4e` ; code préparé du
  développeur, commit `e2e24cacb87df4d31b487b7a81461a5208a928fa` : `statistiques_v2.py`
  `b6c291e304da5b974d4b1b484dd05cfe2a0ee819aff69abc62dde348dccd6f49`, et, pour la conformité, `statistiques_v1.py`, `audits_v1.py`,
  `lanceur_v3.py` et les noms des essais ; note `traitement-contre-lecture-v1-complement-1.md`
  `8b34c66ea0372c9ed7d4c48ab153ccd513c90649a30160b39451d19257dd24c5`.
- **Pièces du contre-lecteur** : dossier `docs/notes/lecture-sondes-bbis-par-lentilles-v1/contre-lecture-addendum-concentration-outils-v1/`,
  à côté de ce rapport (programmes, sorties, commandes et entropies ; chaque fichier scellé avec son compagnon ; liste au § 11).
  Données synthétiques seulement.

## Conclusion

**Scellable après ces couples exacts** : les cinq couples obligatoires C1 à C5 du § 9, et la condition de nommage du § 8 (le brouillon
garde un nom de brouillon et son empreinte ; la version porte le nom final). Les couples F1 à F3 sont facultatifs.

1. **Option 2, et seulement elle** : oui. Les trois passages corrigés du texte sont les seuls où une direction nulle entre dans sa propre
   référence ; direction lue, témoins, z des tables, familles, pôles, seuils, nuls, graines et bornes sont inchangés. Les ajouts (deux
   arrêts, une clé de registre, des essais, la règle du quantile écrite) sont des corollaires de procédure qui ne changent aucune valeur.
2. **§ 6 (d) et (e)** : le développement est juste ; je le refais et trouve le même terme, au même signe. Calculée par moi, la
   prédiction au premier ordre rend −4,5 et −4,0 /M sur les deux miniatures de l'auteur, contre −4,6 et −4,4 /M mesurés par lui. Ma
   simulation jointe appariée sur cinq lois neuves à jetons corrélés donne quinze différences négatives, stables une fois multipliées
   par M (ordre 1/M), à moins de 0,6/M de la prédiction. **Le signe tient** (conservateur). **La taille tient au niveau 0,05** : de
   −0,1 % à −0,5 % à 89 498 jetons et M = 2 000 dans mes lois, ce qui encadre les −0,23 % de l'auteur. **Elle grandit aux niveaux
   stricts** : de l'ordre de −1 % à −3 % au niveau 0,001, celui du libellé « concentrée » ; la simulation le confirme (terme multiplié
   par 1,8 à 2,8 quand le niveau passe de 0,05 à 1/80 ou 1/160). L'addendum ne le dit pas assez : C4.
3. **Bornes** : inchangées. Les 41 sont retrouvées par un calcul indépendant (loi bêta-binomiale en fractions exactes), à la valeur et au
   risque près ; risque de sortie d'une calibration saine de 1,28 à 1,87 × 10⁻⁴, confirmé.
4. **Simulation rejouée à une entropie neuve** : témoins à p ≤ 0,05 sous la statistique corrigée de 0,0495 à 0,0502 (l'auteur : 0,0497
   à 0,0500) ; moyenne des deux courses 0,04987 ± 0,00007, soit −0,2 % en relatif, au sens et à la taille du résidu prédit. La
   sur-dispersion d'environ 5 % ne se retrouve pas dans des mondes neufs (0,989 et 0,999), sans être exclue (borne haute à 95 % ≈ 6 %).
5. **Codabilité** : les cinq points et l'arrêt sont codables sans choix, à deux précisions près (C3, C5). Le code préparé est conforme
   aux cinq points et à l'arrêt, vérifié contre un calcul direct ; il ne l'est pas encore, comme attendu, à la clé de registre ni aux
   essais neufs (C1, C2).
6. **Points ouverts** : clé neuve à ratifier, placée aussi avant `CODE-LENTILLES-BBIS` (C1) ; ligne `CODE-LENTILLES-BBIS` pas encore
   inscrite ; seuil de 10⁻¹⁰ justifié par une identité exacte ; sur-dispersion ni établie ni exclue, sans conséquence pour les bornes.
7. **Expositions** : sans effet sur la règle du préenregistrement scellé.
8. **Règles** : les essais des gardes neuves manquent en partie (C2) ; le brouillon occupe le nom final (§ 8).

Hors du champ, à porter à la mère (§ 10) : le brouillon 2 de la version 2 du texte (qui ajoute nos lentilles), sur la même branche,
garde la phrase d'origine (« u_j compris : écart déclaré, négligeable à M = 2 000 », ligne 944) ; scellé ainsi, il reprendrait le biais.

## 1. La correction est l'option 2, et seulement elle

- **Option 2 de la fiche** (rapport, § 5) : « pour C(u_j), moyenne et écart type des M − 1 autres, par formule exacte ; pour P(u_j),
  quantile 0,99 des M − 1 autres, tiré des statistiques d'ordre du jeton ; familles inchangées ; inchangé pour v et les témoins ».
  EC-1 (concentration) et EC-2 (part) l'écrivent ; EC-3 en tire la calibration (témoins jugés comme v, bornes inchangées) ; la ligne du
  mot de Lazar dit la même chose.
- **Citations « avant »** : égales au texte, lignes 336-337 (EC-1), 338-339 (EC-2), 460-468 (EC-3, deux passages) ; les lignes citées
  par EC-4 (374-382, 628-633) et EC-5 (637-643) sont justes.
- **Rien d'autre ne bouge** : j'ai relu « Métrique » (points 1 à 9), « Seuil », « Plan d'analyse » (points 1 à 10), « Critères de lecture
  gelés », « Liste d'arrêt », « Données gardées », « Lignes de registre », « Code neuf », et cherché dans tout le texte « exacte »,
  « négligeable », « compris » et « quantile ». Les seuls passages où une direction nulle entre dans sa propre référence, ou qui
  appellent la loi du compte « exacte », sont les trois que l'addendum corrige. Les pôles (cosinus maximal, rang parmi les maxima nuls),
  les familles (comptes dans les vingt premiers jetons bruts), le jeton de début, les rangs empiriques et les z des tables de v n'ont
  pas de référence qui contienne la direction jugée : ils sont inchangés à juste titre. Les résumés des nuls gardés (« Données
  gardées » : moyenne, écart type et quantile 0,99 par jeton) restent ceux des M directions.
- **Ajouts, et leur nature** : (i) la règle du quantile (interpolation linéaire, rang 0,99 × (n − 1)) n'était pas écrite dans le texte ;
  c'est celle du code déjà contre-lu (`torch.quantile`, mode linéaire ; convention écrite dans les tables : « 0,99, interpolation
  linéaire ») ; elle ne change aucune valeur de v ; (ii) deux arrêts (variance des autres à 10⁻¹⁰ près ; moins de trois directions),
  de sens sévère, sans effet sur une lecture saine (§ 6, point 5) ; (iii) une clé de registre et des essais. Aucun ne touche la direction
  lue, les témoins, le z des tables, les familles, les pôles ni les seuils.
- **Mot changé** : la loi bêta-binomiale cesse d'être dite « exacte » et devient la « loi de référence, approchée » ; c'est vrai (§ 3), et
  aucune borne ne change.

## 2. § 6 (d) et (e) : le terme de couplage, refait

### 2.1 Développement

Soit, à un jeton, la référence des M − 1 autres nulles : moyenne m, écart type de population s ; une nulle u_j y a le z noté z. Ajouter
v, de score b, avec ζ = (b − m)/s, donne m' = m + (b − m)/M et s'² = s²·(M − 1)/M·(1 + ζ²/M), d'où

z' = (z − ζ/M) / √((1 − 1/M)(1 + ζ²/M)) = z − [z(ζ² − 1)/2 + ζ]/M + O(1/M²).

C'est le terme de l'addendum, au même signe : les nulles corrigées (sans v) sont plus hautes que dans le schéma exact de
δ = [z(ζ² − 1)/2 + ζ]/M. Pour une nulle au seuil, z ≈ c ; si ζ suit une loi normale de moyenne ρc et de variance 1 − ρ², alors
E[δ] = c·[ρ²(c² − 1)/2 + ρ]/M : le crochet de l'addendum est l'**écart relatif du z** (δ/c), non celui de la part. La part des valeurs p
au seuil bouge de −h(c)·E[δ], h étant le hasard de la concentration au seuil (voisin de c pour une queue gaussienne) : l'écart relatif
de la part vaut environ c·h fois le crochet (F1). La fenêtre anti-conservatrice (ρ entre −2/(c² − 1) et 0) et sa borne sont justes : le
minimum, atteint en ρ = −1/(c² − 1), vaut −c/(2(c² − 1)M) sur le z, soit ≈ (c² + 1)/(2(c² − 1)M) sur la part ; moins de 0,03 % à
M = 2 000.

Hors du modèle à une seule corrélation, la variation relative de la part, multipliée par M, vaut au premier ordre
−h(q)·E[q(ζ_t² − 1)/2 + ζ_t | C(v) = q], où q est le quantile de la concentration au niveau, et t le jeton où culmine une nulle au seuil
(indépendant de v). Je la calcule par Monte-Carlo, M infini : c'est la « prédiction » ci-dessous.

### 2.2 Prédiction contre mesure

- **Miniatures de l'auteur** (monde reconstruit par son programme, mêmes clés ; tirages à moi) : prédit −4,46/M (largeur 32) et
  −4,01/M (largeur 128) ; mesuré par l'auteur −4,6, −4,7, −4,7, −4,3 et −4,4, −4,4, −4,2, −4,8. Le § 6 (d) explique le § 6 (e).
- **Simulation jointe appariée à moi** (lois inventées, scores gaussiens corrélés entre jetons ; 128 jetons ; même schéma que la partie A
  de l'auteur : statistique corrigée contre schéma exact, sur les mêmes tirages ; entropie neuve ; 100 000 à 400 000 répliques ;
  niveau 0,05) ; différence relative multipliée par M :

| loi (corrélation entre jetons) | M = 39 | M = 79 | M = 159 | prédit au premier ordre |
|---|---|---|---|---|
| indépendants | −1,17 ± 0,10 | −1,13 ± 0,20 | −0,48 ± 0,44 | −0,55, plus le terme des lois (−1,1 ; −0,6 ; −0,3) |
| équicorrélés à 0,3 | −4,66 ± 0,11 | −4,22 ± 0,23 | −3,63 ± 0,44 | −4,18 |
| équicorrélés à 0,6 | −6,72 ± 0,12 | −6,64 ± 0,24 | −6,14 ± 0,48 | −6,44 |
| deux blocs de signes opposés (± 0,3) | −3,38 ± 0,11 | −3,40 ± 0,23 | −3,59 ± 0,46 | −3,26 |
| huit facteurs, charges de signes mêlés | −2,48 ± 0,10 | −2,34 ± 0,22 | −2,51 ± 0,45 | −1,95 |

  Quinze différences sur quinze négatives ; le produit par M est stable de M = 39 à M = 159 : ordre 1/M, conservateur.
- **Niveaux plus stricts** (même simulation, niveau k/(M + 1) avec k = 1) : équicorrélés à 0,6 : −14,1 ± 0,4 /M au niveau 1/80 et
  −18,9 ± 1,3 /M au niveau 1/160, contre −6,5 et −6,7 au niveau 0,05 ; deux blocs (± 0,3) : −6,0 ± 0,3 et −6,6 ± 1,0, contre −3,3 et
  −3,4. La prédiction au premier ordre (−17,3 ; −23,0 ; −6,8 ; −8,6) surestime d'environ un cinquième à ces niveaux, au même signe.

### 2.3 Taille à la taille du texte

Prédiction au premier ordre à 89 498 jetons, M = 2 000, niveau 0,05 : indépendants 0,000 % ; équicorrélés à 0,1, 0,3, 0,6, 0,9 :
−0,14 %, −0,38 %, −0,40 %, −0,43 % ; deux blocs (± 0,3 ; ± 0,6) : −0,29 %, −0,47 % ; huit et deux facteurs : −0,20 %, −0,35 %.
**Les −0,23 % de l'auteur sont du bon ordre au niveau 0,05** (−0,1 % à −0,5 % dans ces lois). À 8 192 jetons, aux niveaux 0,05,
0,01 et 0,001 : équicorrélés à 0,3 : −0,28 %, −0,69 %, −1,21 % ; deux blocs (± 0,6) : −0,44 %, −1,12 %, −2,74 % ; équicorrélés à
0,9 : −0,40 %, −1,28 %, −2,87 % (premier ordre, qui surestime d'environ un cinquième aux niveaux stricts). **Au niveau du libellé
« concentrée » (p ≤ 0,001 sous le nul isotrope), le résidu est donc de l'ordre de −1 % à −3 %**, toujours conservateur ; en valeur
absolue, 0,00097 à 0,00099 au lieu de 0,001. Les corrélations de la lentille réelle restent inconnues : ce sont des lois inventées.

### 2.4 Signe

Conservateur dans les quatre lois de l'auteur (et dans les mondes neufs de mon rejeu, § 4), dans mes cinq lois jointes et dans mes dix
lois prédites (nul pour des jetons indépendants à 89 498 jetons). Deux sources de sens contraire, petites : (i) la fenêtre des
corrélations faiblement négatives, bornée sous 0,03 % ; (ii) la norme fixée par la normalisation (un champ de scores de dimension
effective D : sachant v extrême à un jeton, la variance aux autres jetons baisse d'environ c²/D), d'effet ≈ +h·c³/(2D)/M sur la part,
soit ≈ +0,004 % à D = 4 096 et M = 2 000. Plus D est petit, plus cet effet grandit, mais les corrélations aussi : il joue pleinement dans
les miniatures de largeur 32, dont le bilan reste conservateur, et il est compris dans ma prédiction pour ces miniatures, qui rejoint
la mesure.

### 2.5 Ce qui en suit pour le point ouvert 1

Le fait donné à Lazar est à corriger, comme l'auteur le dit : « différence d'ordre 1/M² » vaut pour la loi de chaque statistique ; pour
la valeur p, il reste un terme d'ordre 1/M, conservateur, d'environ −0,1 % à −0,5 % au niveau 0,05 et jusqu'à quelques pour cent au
niveau 0,001 dans les lois essayées. La décision n'en change pas de sens (le biais anti-conservateur est retiré ; l'erreur restante va
vers « non distincte du nul » ; l'option 3 resterait la voie exacte). Recommandation à la mère : le dire à Lazar en une ligne de
réserve, sans demande de mot neuf.

## 3. Bornes de calibration

- **Programme de l'auteur rejoué** : sortie identique à la sienne, ligne de commande exceptée. **Calcul indépendant** (loi
  bêta-binomiale (n ; 100 ; 1 901) par récurrence en fractions exactes pour n = 200 et 1 000, somme sur 1 à 40 jeux, définitions de
  q_bas et q_haut du texte) : **41 bornes sur 41 égales** ; risques égaux à quatre chiffres. Exemples : un jeu de 1 000 [23, 85],
  1,829 × 10⁻⁴ ; un jeu de 200 [1, 24], 1,282 × 10⁻⁴ ; 13 jeux [89, 176], 1,559 × 10⁻⁴ ; 29 jeux [228, 357], 1,865 × 10⁻⁴ (le plus
  haut) ; 40 jeux [326, 478], 1,796 × 10⁻⁴. **Risque de sortie d'une calibration saine : 1,28 à 1,87 × 10⁻⁴**, confirmé.
- **Inchangées, et pourquoi** : sachant les nulles, le compte est binomial (n ; π) ; il est bêta-binomial (100 ; 1 901) quand la
  concentration d'un témoin et celles des M nulles sont indépendantes et de même loi ; sous la statistique corrigée, la moyenne de π
  vaut 100/2 001 au résidu du § 2 près, et la dispersion est celle de la référence à l'erreur des simulations près (§ 4). La loi reste
  la bonne référence ; ses bornes gardent règle et valeurs.
- **Sensibilité que j'ajoute** (même moyenne, variance du compte gonflée) : + 5 % : risque jusqu'à 2,66 × 10⁻⁴ ; + 10 % : jusqu'à
  3,67 × 10⁻⁴ ; combinée à une part déplacée (× 0,98 et variance × 1,10) : jusqu'à 6,84 × 10⁻⁴ (40 jeux) ; (× 0,97 et × 1,10) :
  1,23 × 10⁻³ (40 jeux). La phrase de l'addendum (« sous 0,1 % dans tous les cas plausibles ») tient, hormis ce dernier cas extrême.
- Deux phrases du § 7 de l'addendum sont à reprendre, sans effet sur une borne : « si et seulement si » (F2) et la borne de réunion
  (F3).

## 4. Simulation rejouée à une entropie neuve

Programme de l'auteur (`78e115da…`), la seule ligne de l'entropie changée (entropie tirée par moi ; les mondes des miniatures sont donc
neufs aussi) ; parties A et B à la taille déclarée ; 4 602 s ; sortie `sortie-rejeu-simulation.txt`.

- **Partie B, témoins à p ≤ 0,05 sous la statistique corrigée** (1 000 témoins par jeu, 2 000 jeux par scénario ; gaussien, structuré
  de largeur 128, de largeur 512, queues lourdes) : 0,05021, 0,04952, 0,04986, 0,04993 (± 0,00019) pour 0,04998 attendu ; chez l'auteur
  0,04976, 0,05001, 0,04972, 0,04996. La fourchette « 0,0497 à 0,0500 » tient pour sa course ; la mienne va de 0,0495 à 0,0502, à
  l'erreur de simulation près (l'écart le plus grand, 0,04952, est à 2,4 erreurs types, une fois sur huit). Les deux courses ensemble :
  0,04987 ± 0,00007, soit −0,2 % en relatif (à 1,6 erreur type de la référence) : du sens et de la taille du résidu de couplage prédit.
  Sous la statistique d'origine : 0,05348, 0,05179, 0,05212, 0,05451.
- **Sur-dispersion** (variance du compte, n = 1 000, rapportée à celle de la référence ; erreur type ≈ 0,038 chacune) : ma course
  0,991, 0,989, 0,999, 0,968 ; celle de l'auteur 0,935, 1,047, 1,057, 1,026. Les ≈ 5 % des miniatures structurées de l'auteur ne se
  retrouvent pas dans des mondes neufs (0,989 et 0,999). Les deux courses ensemble : 1,002 ± 0,013 sur les huit scénarios ; 1,023 ±
  0,019 sur les quatre structurés. **Une sur-dispersion de 5 % n'est ni établie ni exclue** (borne haute à 95 % ≈ 1,06 dans les
  miniatures structurées) ; elle n'est pas soutenue ; si elle existait, le risque de sortie d'une calibration saine monterait à
  2,7 × 10⁻⁴ au plus (§ 3).
- **Sorties des bornes** sous la statistique corrigée : 0 sur 8 000 jeux de 1 000 et 0 sur 8 000 jeux de 200 (chez l'auteur : 0 et 2) ;
  ensemble, 2 sorties sur 16 000 jeux de 200 pour ≈ 2 attendues. Hors de l'intervalle à 1 % par côté (n = 1 000) : 0,0145 à 0,0190 pour
  0,0177 attendu.
- **Partie A** (différence appariée corrigée − exacte au niveau 0,05, relative, multipliée par M) : largeur 32 : −4,8, −4,9, −5,0, −5,2 ;
  largeur 128 : −4,2, −4,0, −3,8, −3,6 (chez l'auteur −4,6 à −4,7 et −4,2 à −4,8) ; gaussien et queues lourdes négatifs aussi, toutes
  lignes. Le résidu d'environ −4,5/M des miniatures se retrouve dans des mondes neufs.
- **Part au-dessus du nul** : part moyenne des nulles sans elles-mêmes moins celle des témoins : −0,00017, −0,00003, −0,00005, −0,00016
  (± 0,00014 à 0,00018) ; taux des témoins à p ≤ 0,05 : 0,041 à 0,044, conservateur par les égalités, comme chez l'auteur.
- **Les trois statistiques que le programme nomme** (« v1 », « corrigée », « exacte ») sont calculées comme il le dit. Pour la statistique
  « exacte », chacune des M + 1 directions est jugée avec elle-même ; la même transformée croissante la ramène au jugement sans elle-même
  contre les M autres : le schéma est donc exact par échangeabilité. La partie B et le calcul des parts (statistiques d'ordre des M − 1
  autres, obtenues en décalant d'un cran au-dessus du rang retiré) sont justes.

## 5. Codabilité, et conformité du code préparé

| point de l'addendum (§ 4) | codable sans choix ? | code préparé (`e2e24cac`) |
|---|---|---|
| 1. quantile 0,99 des M − 1 autres, interpolation linéaire, rang 0,99 × 1 998 | oui | conforme : `quantiles_sans_soi`, rang 0,99 × (M − 2), décalage des statistiques d'ordre ; égal à un calcul direct, égalités comprises (écart nul sur les mêmes couples jeton-direction) |
| 2. v et témoins sur les M directions | oui | conforme : `resumer_nul` garde moyenne, écart type et quantile des M ; `p_temoins` et `z_scores` de la version 1, inchangés |
| 3. z des tables sur les M | oui | conforme : `lecture_signe` de la version 1, inchangée |
| 4. bornes inchangées | oui | conforme : `audits_v1` (loi bêta-binomiale du texte, mêmes définitions) ; l'essai des 41 valeurs manque |
| 5. repli, nul des signes, pôles, familles, jeton de début | oui | conforme : `lanceur_v3` appelle `resumer_nul` de la version 2 pour le nul isotrope partagé (l. 560), le nul des signes (l. 584) et le repli par direction (l. 656) ; familles calculées comme avant ; pôles par la version 1 |
| 6. arrêt (variance des autres ≤ 10⁻¹⁰ fois celle des M ; moins de trois directions) | oui | conforme : `concentrations_sans_soi` |
| EC-1, « calcul en double précision » | pas tout à fait : la précision de la comparaison C(u_j) ≥ C(v) n'est pas dite | le code calcule en double, rend C(u_j) en simple précision et compare en simple ; à écrire (C5) |
| EC-4, clé de registre | oui | pas encore : aucune vérification de la clé ; le manifeste ne cite pas l'addendum (C1) |
| EC-5, essais | pas tout à fait : l'essai du taux ne dit pas si chaque réplique tire ses nuls (C3) ; deux gardes neuves sans essai (C2) | pas encore : l'essai du taux (M = 19, 128 jetons, 2 000 répliques, [0,03 ; 0,065]) et celui des 41 bornes manquent ; l'essai de taux du développeur est autre (M = 200) |

Vérifications à moi, sur les fonctions extraites du commit (aucune donnée) : concentrations et parts de `resumer_nul` contre un calcul
direct, direction par direction, sur les M − 1 autres, en six configurations (M = 3, 5, 19, 101, 101, 40 ; deux avec beaucoup
d'égalités et deux directions identiques) : écart des concentrations ≤ 4,8 × 10⁻⁷ (simple précision) ; quantiles sans soi égaux ;
parts égales quand les vingt premiers jetons sont les mêmes. Un écart de part paraît seulement quand des égalités tombent au vingtième
rang : il vient du départage des vingt premiers (`topk` contre un tri stable), qui préexiste dans le texte et dans le code de la
version 1 (§ 10). Statistique d'origine strictement plus petite : vraie dans les six cas. Arrêts : deux directions : arrêt ; jeton
constant sur les autres : arrêt ; autres dispersés à 10⁻⁶ autour de 1 en simple précision : arrêt (rapport ≈ 10⁻¹³) ; à 10⁻³ : pas
d'arrêt.

## 6. Points ouverts du § 9 de l'addendum

1. **Ordre 1/M²** : confirmé en partie, comme l'auteur le dit (§ 2) ; C4 écrit la dépendance au niveau.
2. **Voie exacte** : juste ; aucune proposition.
3. **Ligne `CODE-LENTILLES-BBIS`** : **pas encore inscrite**. Le registre propre de la branche principale ne porte que
   `ABSENCE-VERDICT-LENTILLES-BBIS` et `SCELLEMENT-LENTILLES-BBIS` (clés seules lues) ; il n'existe pas sur les deux autres branches.
   La première ligne `CODE-` citera donc le code corrigé ; la question de forme tombe si la clé de l'addendum la précède (C1).
4. **Clé neuve** : à ratifier, avec C1 : avant `CODE-LENTILLES-BBIS` aussi (le code doit suivre un addendum scellé, et sa fiche en
   porter l'empreinte), vérifiée par le code avant toute requête ou ouverture, essayée (C2).
5. **Seuil de 10⁻¹⁰** : justifié. Identité exacte : variance des autres / variance des M = (M/(M − 1))·(1 − d²/(M − 1)), d étant le z
   de la nulle jugée avec elle-même. Le rapport ne descend sous 10⁻¹⁰ que si d² ≥ (M − 1)(1 − 10⁻¹⁰ environ), c'est-à-dire une nulle
   seule contre M − 1 valeurs égales à 10⁻⁵ près de l'écart type du jeton : cas dégénéré. Pour d ≤ 20, le rapport dépasse 0,80. L'erreur
   d'arrondi de la formule en double précision est d'environ 10⁻¹⁶ × M ≈ 2 × 10⁻¹³, bien sous le seuil. Le seuil sépare le zéro
   numérique de toute configuration non dégénérée ; il ne peut pas arrêter à tort sur des scores réels.
6. **Sur-dispersion** : ni établie ni exclue ; non reproduite à l'entropie neuve ; sans conséquence pour les bornes (§ 3 et § 4). Le
   point peut être fermé tel quel.

## 7. Expositions déclarées par l'auteur

- **Deux essais courts vus avant la course à la taille déclarée** : la règle du préenregistrement scellé porte sur les résultats de
  l'expérience, ici la lecture des sondes réelles, que personne n'a ouverte. Ces essais portent sur des données synthétiques d'une
  simulation d'appui, non décisive ; aucune borne, aucun seuil, aucun libellé n'en dépend (les bornes viennent du calcul exact). Seuls
  en dépendent la seconde largeur de la miniature (déclarée) et l'intervalle [0,03 ; 0,065] d'un essai de code. Mes lois neuves et le
  rejeu à une entropie neuve, dans des mondes neufs, ôtent tout doute sur le choix des miniatures.
- **Note et code du développeur lus après les formules** : risque que le texte suive le code. Les six hypothèses reprises sont la
  lecture directe de l'option 2 de la fiche, écrite avant le code, et de la ligne du mot de Lazar ; aucune ne change une valeur ;
  l'addendum les fixe comme ses propres décisions (« le texte décide, le code suit »). Sans effet sur la règle ; l'auteur n'est ni le
  développeur ni l'opérateur.

## 8. Règles

- **Préenregistrement scellé avant toute lecture (R1)** : l'addendum est scellé avant `ENTREES-LENTILLES-BBIS`, et, avec C1, avant
  `CODE-LENTILLES-BBIS`. Aucune sonde lue. Tenue.
- **Symétrie des audits (R4)** : la valeur « propre » de la statistique corrigée (5,13 % au banc) a été auditée par l'auteur, qui y a
  trouvé le terme de couplage ; mon rejeu et mes lois neuves sont l'audit symétrique. Tenue.
- **Gardes essayées sur un cas sain et sur un artefact (R5)** : l'arrêt sur la variance des autres a son essai ; l'arrêt « moins de
  trois directions » et la garde de la clé neuve n'en ont pas dans EC-5 (C2) ; les 41 bornes en ont un. À compléter.
- **Chiffres de l'état de l'art (R7)** : aucun. Chaque chiffre renvoie à un fichier et une empreinte (compagnons vérifiés).
- **Versions dans les noms (R12)** : programmes et module neufs sous des noms neufs : tenu. Mais le brouillon occupe le nom final
  (`…-addendum-concentration-v1.md`). Condition : la mère garde ce brouillon sous un nom de brouillon (par exemple
  `…-addendum-concentration-v1-brouillon1.md`, même empreinte `0a862760…`) et écrit la version, couples appliqués et statut mis à jour,
  sous le nom final ; aucun fichier scellé n'est écrasé.
- **Graines (R9)** : clés neuves propres à l'addendum, entropie du texte, déclarées : tenu.

## 9. Couples exacts

Texte « avant » copié de l'addendum (`0a862760…`), retours à la ligne compris ; chacun y paraît une seule fois (vérifié par programme).

**C1** (EC-4, obligatoire : ordre de la clé, vérification par le code, empreinte citée).

Avant :

```
Ajout : une clé neuve du registre propre, **`ADDENDUM-CONCENTRATION-LENTILLES-BBIS`** (version scellée de cet addendum), inscrite après
sa contre-lecture, **avant `ENTREES-LENTILLES-BBIS`** et avant toute exécution du calcul du point 6. La ligne `CODE-LENTILLES-BBIS` cite
un code qui applique l'addendum (fiche et empreintes du code corrigé). « Liste d'arrêt », ajout : `ADDENDUM-CONCENTRATION-LENTILLES-BBIS`
absente, ou inscrite après `ENTREES-LENTILLES-BBIS` : rien ne part ; nœud.
```

Après :

```
Ajout : une clé neuve du registre propre, **`ADDENDUM-CONCENTRATION-LENTILLES-BBIS`** (version scellée de cet addendum), inscrite après
sa contre-lecture, **avant `CODE-LENTILLES-BBIS` et avant `ENTREES-LENTILLES-BBIS`**, donc avant toute exécution du calcul du point 6.
La ligne `CODE-LENTILLES-BBIS` cite un code qui applique l'addendum (fiche et empreintes du code corrigé) ; la fiche porte le chemin et
l'empreinte de l'addendum scellé ; le code les compare à la ligne `ADDENDUM-CONCENTRATION-LENTILLES-BBIS` avant toute requête ou
ouverture, et le manifeste et les tables les citent à côté de l'empreinte du texte. « Liste d'arrêt », ajout :
`ADDENDUM-CONCENTRATION-LENTILLES-BBIS` absente, en plusieurs lignes, inscrite après `CODE-LENTILLES-BBIS` ou après
`ENTREES-LENTILLES-BBIS`, ou d'une autre empreinte que celle que porte la fiche du code : rien ne part ; nœud.
```

**C2** (EC-5, obligatoire : essais des deux gardes neuves).

Avant :

```
- **arrêt** : variance des autres nulle pour un jeton (jeton constant sur les autres) : arrêt ;
```

Après :

```
- **arrêt** : variance des autres nulle pour un jeton (jeton constant sur les autres) : arrêt ; deux directions nulles : arrêt ; cas
  sain : trois directions de scores distincts : pas d'arrêt ;
- **clé de l'addendum** (registre jouet) : une seule ligne `ADDENDUM-CONCENTRATION-LENTILLES-BBIS`, inscrite avant
  `CODE-LENTILLES-BBIS` et avant `ENTREES-LENTILLES-BBIS`, de l'empreinte que porte la fiche : accepté ; ligne absente, en deux lignes,
  inscrite après `CODE-LENTILLES-BBIS` ou après `ENTREES-LENTILLES-BBIS`, ou d'une autre empreinte : refus ;
```

**C3** (EC-5, obligatoire : l'essai du taux tire ses nuls par réplique ; avec un seul jeu de 19 nulles pour les 2 000 témoins, la part
suivrait la loi bêta (1 ; 19), d'écart type ≈ 0,048, et l'intervalle échouerait au hasard).

Avant :

```
  simulation, partie A) : un essai à 2 000 répliques exige une part entre 0,03 et 0,065 ;
```

Après :

```
  simulation, partie A) : un essai à 2 000 répliques, **chaque réplique tirant ses propres 19 directions nulles et sa direction
  témoin**, exige une part entre 0,03 et 0,065 ;
```

**C4** (§ 6 (g), obligatoire : le résidu dépend du niveau ; c'est le fait que la mère portera à Lazar).

Avant :

```
**inconnues ici** : ≈ −0,2 % dans les miniatures ; l'estimation au premier ordre de (d) va jusqu'à quelques pour cent pour des jetons
fortement corrélés.
```

Après :

```
**inconnues ici** : ≈ −0,2 % dans les miniatures, au niveau 0,05 ; l'estimation au premier ordre de (d) va jusqu'à quelques pour cent
pour des jetons fortement corrélés. Le terme **grandit aux niveaux plus stricts** : la contre-lecture l'estime, dans des lois
gaussiennes inventées à jetons corrélés, de −0,1 % à −0,5 % au niveau 0,05 (89 498 jetons, M = 2 000) et de l'ordre de −1 % à −3 % au
niveau 0,001 du libellé « concentrée » (8 192 jetons) ; toujours conservateur. Ce n'est pas une mesure sur la lentille réelle.
```

**C5** (EC-1, obligatoire : précision de la comparaison, pour que le code n'ait rien à choisir ; c'est ce que fait le code préparé).

Avant :

```
Calcul en double précision. Si, pour un jeton,
```

Après :

```
Calcul en double précision ; C(u_j) est ensuite rendu en simple précision, comme C(v), et la comparaison C(u_j) ≥ C(v) se fait en
simple précision (une égalité compte contre v). Si, pour un jeton,
```

**F1** (§ 6 (d), facultatif : le crochet est un écart relatif du z, non de la part).

Avant :

```
d'une
part relative ≈ [ρ²(c² − 1)/2 + ρ]/M :
```

Après :

```
d'un
écart relatif de leur z ≈ [ρ²(c² − 1)/2 + ρ]/M (sur la part des valeurs p au seuil, l'écart relatif est environ c·h fois plus grand,
h étant le hasard de la concentration au seuil, voisin de c) :
```

**F2** (§ 7, facultatif : un mélange de lois binomiales n'est fixé que par les n premiers moments de sa loi de mélange ; « seulement
si » est faux).

Avant :

```
Il est bêta-binomial (n ; 100 ; 1 901) si et seulement si π
```

Après :

```
Il est bêta-binomial (n ; 100 ; 1 901) si π
```

**F3** (§ 7, facultatif : avec le repli par direction, la calibration du nul partagé s'ajoute, ses lectures étant « remplacées »).

Avant :

```
au plus douze
calibrations (trois couches, deux lentilles, deux nuls) : au plus 2,2 × 10⁻³ par borne de réunion.
```

Après :

```
au plus douze
calibrations qui portent des libellés (trois couches, deux lentilles, deux nuls ; avec le repli par direction, celle du nul partagé,
dont les lectures sont alors « remplacées », s'y ajoute : dix-huit au plus, 3,4 × 10⁻³) : au plus 2,2 × 10⁻³ par borne de réunion.
```

## 10. Hors du champ de l'addendum, à porter à la mère

- **Version 2 du texte, en brouillon** : `prereg/lecture-sondes-bbis-par-lentilles-v2-brouillon2.md` (branche
  `claude/brave-galileo-jhp684` ; lecture par la lentille publique et par nos lentilles), ligne 944 : « compris : écart déclaré,
  négligeable à M = 2 000 ». Elle garde la statistique d'origine ; scellée ainsi, elle reprendrait le biais pour toutes ses lentilles.
  La correction est à y porter avant son scellement ; la mère dit si le mot de Lazar (GO-2026-11-19-47, donné pour le texte v1) la
  couvre. Lu par une recherche d'une ligne seulement.
- **Départage des vingt premiers jetons** : le texte ne dit pas comment départager deux jetons de même score au vingtième rang ; le code
  laisse `topk` décider. Préexistant, hors de l'addendum ; improbable sur 89 498 jetons en simple précision, possible si deux jetons
  gardés ont la même ligne de sortie.
- **Essai « artefact » d'EC-5** : « la statistique du texte d'origine rend des concentrations strictement plus petites » n'est vrai que si
  le maximum du z de la nulle est positif (pour un maximum négatif, c'est la statistique corrigée qui est la plus petite). Toujours vrai à
  la taille réelle et dans mes jouets ; à garder en tête pour un jouet à très peu de jetons.

## 11. Ce que j'ai fait, lu et produit

- **Actions** : `git fetch` des branches `claude/brave-galileo-jhp684`, `claude/lentilles-bbis-developpeur-v1` et principale ; un arbre
  détaché du commit `6de58b8c` dans le bloc-notes ; extraction de cinq fichiers du code préparé (`controle_ia/__init__.py`,
  `controle_ia/gardes.py`, et `__init__`, `constantes_v1`, `statistiques_v1`, `statistiques_v2` du paquet de la lecture) dans le
  bloc-notes pour les éprouver ; programmes au processeur ; aucun modèle chargé, aucune machine, aucune dépense, aucun commit, aucun
  push. Aucun refus d'outil.
- **Lu** : l'addendum en entier ; le texte scellé, sections « Métrique » à « Liste d'arrêt », « Données gardées », « Lignes de registre »,
  « Code neuf », plus une recherche de mots dans tout le texte ; le rapport, § 5 et fiche ; la sortie du banc ; les six pièces ; la note
  du développeur ; `statistiques_v2.py`, des passages de `statistiques_v1.py`, `audits_v1.py`, `lanceur_v3.py`, les noms des essais ;
  la ligne GO-2026-11-19-47 de `registres/go.md` ; les clés seules du registre propre de la lecture ; une ligne du brouillon 2 de la
  version 2, par recherche, et ses trois premières lignes (titre, auteur). **Jamais ouverts** : aucune sonde, aucun score, aucune
  table, aucune lecture, aucun verdict, rien sous `docs/verdicts/`, aucune branche de données ou de calcul, aucun fichier dont le nom
  porte « consigne-privee » ou « conception-ii-b ».
- **Pièces** (dossier `contre-lecture-addendum-concentration-outils-v1/`, à côté de ce rapport ; empreinte complète dans chaque
  compagnon ; commandes, entropies et versions dans `commandes-v1.txt`) :
  - commandes : `commandes-v1.txt` `0f53cb73…` ;
  - bornes : `bornes_independantes.py` `c8b037aa…`, sortie `87afee7b…` ; `risque_combine.py` `d250fa54…`, sortie `e71f1ee4…` ;
    rejeux des programmes de l'auteur : `sortie-rejeu-bornes.txt` `6b132d19…`, `sortie-rejeu-validite.txt` `d94f93a8…` ;
  - couplage : `couplage_contre_lecteur.py` `9cd93c13…`, sorties `sortie-couplage-J-T128.txt` `b13e1010…`,
    `sortie-couplage-P-T128.txt` `74db6faa…`, `sortie-couplage-P-grandT.txt` `50c30ebe…`, `sortie-couplage-P-extremes.txt`
    `81bbac1f…` ; `couplage_niveaux_contre_lecteur.py` `3375f176…`, sortie `725b6fa0…` ; `prediction_niveaux_contre_lecteur.py`
    `339624b2…`, sortie `7b4c9bc7…` ; `prediction_miniature_auteur.py` `8eb2a4b5…`, sortie `ae10b23a…` ;
  - rejeu de la simulation : `simulation_rejeu_entropie_neuve.py` `eb72eae9…` (le programme de l'auteur, la seule ligne de l'entropie
    changée), sortie `sortie-rejeu-simulation.txt` `bb720415…` ;
  - code préparé : `verif_code_dev.py` `0177b0af…`, sortie `05d2f1ea…` ; `diag_egalites.py` `f8b500c9…`, sortie `d8adbaf1…`.
