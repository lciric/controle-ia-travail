# Contre-lecture (R2) — préenregistrement de la recombinaison bisociative à deux espaces, v2, brouillon 1 — v1

- Contre-lecteur : sous-agent neuf, Opus 5.5 (`claude-opus-5-5`), modèle différent de l'auteur (Sonnet 5.5). **Non-auteur** du brouillon, du recoupement, de la question, de l'avis d'Opus, de la synthèse, du code du pôle et de `trancher-recombinaison-v1`. Début `date -u` : 2026-10-30T00:48:03Z ; rédaction : 2026-10-30T00:53:13Z.
- Relus (SHA-256 recalculés, tous égaux à leur compagnon `.sha256`) : brouillon `c9077cfe136269c8cf1a5fa8192153fccf48962aba8e276ac2a7e4dad89288e7` ; recoupement `c76959a07f35024d8ea63be54ab7ea9ddc5170960b48112160860898ccf3ee0d` ; question `73a30ab7…` ; avis d'Opus `2331e70f…` ; synthèse `49dd3840…` ; pièce A `recombinaison.py` `71faad38…` ; dans `trancher-recombinaison/` : rapport B `72cff8a0…`, préenregistrement v1 `5335614b…`, `monde_v1.py` `af907b1d…`, `methodes_v1.py` `2f7a8b11…`, `mesures_v1.py` `0a1e3c38…`, `conditions_v1.py` `9246ecc6…`, `trancher_v1.py` `781335dd…`, résultats `daaef112ce5a402bda785c1206db222c8f94793afaf7c0ced910467b4bf4a624` ; lignes R-497 et R-500 de `registres/decisions.md` ; `prereg/gabarit-preregistrement-v1.md` ; `src/controle_ia/prereg.py`.
- Non lus (interdits) : `donnees/`, branches git, `prereg/P3-consignes-v1.md`, `diag/*/traces`. Aucun réseau, aucune dépense, aucun fichier existant modifié, rien scellé. Calculs de ma main marqués (M).
- Validateur (`problemes`, lecture seule) : les huit sections R1 et R2 sont présentes et non vides ; seul défaut signalé, attendu : « contre-lecture 1 sans ses deux empreintes ». Les marqueurs `[À GELER PAR LAZAR]` et `[À SCELLER]` ne sont **pas** vus par le validateur (il cherche « À REMPLIR »).

## Constats (ligne du brouillon ; défaut ; correction ; gravité)

**CB-01 — l. 29-35, 66, 212 ; circularité du monde v2.**
- Défaut : La vérité est « concept latent commun » (W3) et N lit le canal bruité de ce même concept : le générateur fabrique la proximité conceptuelle que l'objectif lit. P4 (N − N_β0) est donc acquis par construction dès que le canal est passable ; il ne prouve rien sur la valeur du concept, seulement que l'instrument voit le canal. Sur les mondes v1 (NR), il n'y a pas de circularité : κ y lit les étiquettes d'opérateur, la même information que d1 et b ; NR ne teste donc pas le concept, seulement la non-régression.
- Correction : (1) écrire que la ligne « ingrédient manquant : oui » vaut **sous W1-W3** seulement, et la renommer en conséquence ; (2) déclarer P4 comme contrôle de manipulation, pas comme preuve ; (3) **ajouter une condition « concepts inertes »** (le monde « plat » de la synthèse, D7 B, abandonné sans le dire) : concepts observés par le même canal mais latents indépendants de la vérité (vérité par opérateur latent comme en v1). Exigence : borne basse de Δ(N, N_β0) ≤ 0 et borne haute < δ_non. C'est le seul témoin où une forme sans valeur conceptuelle peut être prise en défaut.
- Gravité : **majeure**.

**CB-02 — l. 197-203, 208 ; adoption possible sans concept.**
- Défaut : A1 à A6 n'exigent pas Δ(N, N_β0) > 0. L'éloignement seul fait déjà +11,9 et +6,6 (B § 1), au-dessus de l'option (b). N peut donc être « adoptée » alors que le terme de concept n'apporte rien, ce que la recommandation l. 86 interdit (« plus les contrastes de détection »). A6 ne protège pas : la fuite retire aussi des paires valides à b.
- Correction : ajouter A7 « dans les deux, borne basse à 95 % de Δ(N, N_β0) > 0 » ; si A1 à A6 tiennent sans A7, le verdict est « l'éloignement suffit : N_β0 ou b_eloigne, pas N ».
- Gravité : **majeure**.

**CB-03 — l. 23, 135 ; l. 229 ; repli silencieux dans la pièce A.**
- Défaut : `tirage_glouton` (pièce A, l. 141-148) **attrape** `NonDefiniePositive`, saute le candidat, puis s'arrête sans rien dire. `ordre_glouton` de v1 borne aussi le pivot à 1e-300. Réutiliser ces fonctions « telles quelles » contredit la liste d'arrêt (« arrêt du bras et du run ; jamais de repli silencieux », R5). De plus, la garde l. 242 ne teste que `cholesky`.
- Correction : imposer un glouton nouveau, qui laisse remonter l'exception et compte les pivots ≤ 0 ; tester la garde **à travers** le glouton, sur `noyau_fautif` puis sur un noyau sain.
- Gravité : **majeure**.

**CB-04 — l. 181, 94, 212-214 ; puissance des règles gelées.**
- Défaut : Le chiffre « puissance 0,8 pour 3 points » vaut pour « borne basse > 0 », pas pour les règles écrites. (M) Avec un écart-type de 15,3 et 1 200 mondes, l'erreur type vaut 0,44. Une ligne « borne basse ≥ δ = 3 » a donc une puissance de 0,8 seulement si l'effet vrai atteint 3 + 2,8 × 0,44 = 4,2 points. Pour un effet vrai de 3 points, elle tombe à 2,5 %. Or P5 prédit +1 à +5 : par les prédictions mêmes de l'auteur, le « oui » est presque inatteignable. L'avis d'Opus écrivait d'ailleurs « ≥ +3 et bornes basses > 0 » : le durcissement n'est pas signalé. Même défaut pour A1 : si l'effet vrai égale θ_abs dans une condition, la conjonction donne au mieux 0,25.
- Correction : « oui » si l'estimation ≥ δ **et** la borne basse > 0 (Opus), ou garder « borne basse ≥ δ » mais écrire la puissance vraie. Dans les deux cas, tabuler P(verdict) pour les centres de P1 à P5 et pour les écarts-types 11 (« moyen », B § 1) et 15,3.
- Gravité : **majeure**.

**CB-05 — l. 100-101, 106, 166 ; générateur sous-spécifié, rareté appariée irréalisable telle qu'écrite.**
- Défaut : Les 10 concepts sont tous rattachés à un champ et portés par les opérateurs de groupe. Un pont conceptuel, un jumeau (« concept non moyeu tiré ») ou une greffe porte donc un concept que **beaucoup** d'articles du champ source portent aussi. Conséquences : (1) des vraies paires « par expansion », nombreuses et concentrées sur un même article, contraires à « 3 vrais ponts » ; (2) une fréquence documentaire de l'étiquette de pont souvent bien au-dessus de {2, 3, 4} ; (3) une fréquence **observée** qui ne peut pas être « tirée » : elle résulte de la couverture, des parasites et de la fuite.
- Correction : réserver un groupe de concepts de pont rares, non portés par les opérateurs de groupe ; fixer la loi du nombre **latent** de porteurs ({2, 3, 4}, même loi pour tous les statuts) ; mesurer la fréquence observée à la validation ; dire comment le monde INV attribue un concept aux groupes transversaux ; compter et rapporter les vraies paires par mécanisme, expansion comprise.
- Gravité : **majeure**.

**CB-06 — l. 122, 133 ; ordre des strates ambigu.**
- Défaut : Une paire de domaines observés donne jusqu'à 28 strates pour un budget de 12. Sauf monde pauvre, N prend alors la meilleure paire des 12 strates de plus fort score, en un seul passage. « Scores recalculés à chaque tour » est vide (aucune répulsion). Le rôle des 3 générations n'est pas dit : une remise à zéro du tour par génération de 4 tirerait 3 paires dans chacune des 4 meilleures strates, soit un autre bras.
- Correction : écrire « comme `_tour_des_strates` de v1 : un seul tour sur le budget de 12, sans remise à zéro par génération ; si moins de 12 strates sont non vides, second passage dans l'ordre décroissant des scores de strate recalculés sur les paires restantes ; départage par la graine du bras ». Dire que les générations n'ont aucun effet ici, pour tous les bras (N_dpp compris).
- Gravité : moyenne.

**CB-07 — l. 68, 195, 234 ; dénominateur 12 contre « mondes exclus ».**
- Défaut : Avec un dénominateur fixe, la précision est toujours définie : V0 (« ≤ 2 % ») et la ligne d'arrêt l. 234 sont vides de sens. De plus, d1c (étiquettes de concept seules) et N_filtre peuvent s'abstenir dans les mondes pauvres (« mal », SP) : la précision placebo en SP **baisse** alors mécaniquement, et A3 peut échouer pour une raison étrangère à N.
- Correction : définir « monde exclu » (par exemple moins de 12 paires valides, ou aucune vraie paire valide hors SP) ; rapporter `n_sortie` par bras ; calculer la précision placebo sur `n_sortie` ou interdire l'abstention (complément par tirage uniforme parmi les valides restantes, déclaré). En v1, toutes les sorties faisaient 12 (résultats `daaef112…`), donc le contrôle de reproduction l. 235 n'en est pas touché.
- Gravité : moyenne.

**CB-08 — l. 108, 212, 216, l. 53 contre l. 212 ; placebo de concepts.**
- Défaut : La permutation à l'intérieur d'un domaine observé garde, par construction, la composition en concepts de chaque domaine. Un gain de N_PC sur N_β0 peut donc venir de cette information de domaine légitime, et non d'un artefact ; la ligne l. 216 suspendrait alors les deux volets. Autre point : P6 annonce Δ(N, N_PC) ≥ δ, le tableau exige seulement > 0.
- Correction : choisir une seule exigence (« borne basse > 0 ») ; écrire le sens attendu de Δ(N_PC, N_β0) et sa raison ; ajouter un second placebo, une permutation globale entre articles qui conserve les fréquences d'étiquettes, comme témoin de l'information de domaine.
- Gravité : moyenne.

**CB-09 — l. 205-216 ; table de lecture non mécanique.**
- Défaut : Le tableau mêle les deux volets. Ses lignes se recouvrent et aucun ordre de priorité n'est donné. La ligne « A1 non tenue » n'est pas la négation d'A1 : un écart moyen < θ_abs avec une borne haute ≥ θ_abs tombe dans « indécis ». La sortie de l'audit R4 n'est pas écrite.
- Correction : deux tables, adoption puis ingrédient. Lignes exclusives et exhaustives, lues de haut en bas, la première qui s'applique décide : V0, puis audit, puis artefact, puis le reste. Renommer « A1 non tenue » en « N sous le seuil ». Écrire l'issue de l'audit : « artefact trouvé → non concluant et version nouvelle ; aucun artefact → la table s'applique ».
- Gravité : moyenne.

**CB-10 — l. 220 ; audit R4.**
- Défaut : (1) Les seuils sont asymétriques : un gain déclenche l'audit à 15 points, une perte à 10. (2) « N identique au bit près à N_β0 » est attendu dans V_concepts_absents et ne doit pas y déclencher l'audit. (3) La portée de l'identité, monde par monde ou sur l'ensemble, n'est pas dite.
- Correction : un seuil |Δ| ≥ 12 dans les deux sens (ou un autre chiffre unique) ; identité « sur toutes les mondes d'une condition », hors identités déclarées d'avance.
- Gravité : faible.

**CB-11 — l. 3, 22, 78, 88-92, 145, 170 ; marqueurs invisibles, gel incomplet.**
- Défaut : `sceller_prereg` ne bloque pas `[À GELER PAR LAZAR]`. Le gel n'a donc pas de garde mécanique, ce qui contredit R5 (aucun repli sur une recherche manuelle). Par ailleurs, δ, δ_non, −1, 0,30 et 18 sont aussi des seuils : « à geler avec le reste » ne dit pas par qui.
- Correction : remplacer chaque marqueur par le texte littéral « À REMPLIR » jusqu'au gel ; écrire que **tous** les seuils (θ_abs, θ_rel, δ, δ_non, non-régression, plafond, écart-type, seuils de validation) sont gelés par Lazar, ligne datée dans `registres/decisions.md`, sans défaut.
- Gravité : moyenne.

**CB-12 — l. 29-31, 50, 199 ; hypothèse et prédiction discordantes.**
- Défaut : H-B2 (i) affirme que N bat d1c et A2 exige une borne basse > 0, mais P3 annonce « + ou nul ». La même discordance avait été relevée chez Opus (recoupement § 5) et reste ici.
- Correction : P3 « + » (confiance 0,40) et « nul » nommé comme réfutation permise.
- Gravité : faible.

**CB-13 — l. 145, 100 ; une forme utile peut échouer pour une raison de générateur.**
- Défaut : Les concepts sont disjoints par champ. Deux articles proches (même champ) partagent donc souvent un concept avec κ ≈ 1, alors qu'un vrai pont n'en partage qu'un parmi plusieurs (κ ≈ 0,5, SUPPOSÉ). Avec e = 8,5, une paire proche pèse la moitié : N peut tirer des paires proches et perdre contre b_eloigne pour une cause de générateur. La même disjonction favorise N contre d1c par construction (d1c ignore la distance).
- Correction : rapporter avant les méthodes, sur les graines de validation, la loi de κ observé par classe (vrai pont, proche, faux pont, homonyme), sans seuil, pour ne pas régler le monde sur N. Écrire la dépendance d'A2 à cette disjonction dans « ce que ce test ne dit pas » ; ajouter une condition descriptive « concepts partagés entre champs ».
- Gravité : moyenne.

**CB-14 — l. 163, 165, 243 ; validation et gardes non mécaniques.**
- Défaut : (1) La « corrélation de rangs sur les latents » mêle deux indicatrices binaires : il faut nommer la statistique et l'ensemble de paires. (2) « Variation des cosinus ≥ 0,2 » ne dit ni quels cosinus ni quelle moyenne. (3) Le « détecteur de lecture des champs latents » n'est pas défini.
- Correction : écrire la formule exacte de (1) et (2). Pour (3), séparer les latents des observations dans la structure du monde : les bras ne reçoivent qu'une vue observée, et tout accès latent lève une exception. Tester ce garde sur le bras artefact et sur N.
- Gravité : moyenne.

**CB-15 — l. 180, l. 12, l. 17 ; chiffres et provenance (R6, R7).**
- Défaut : Le « environ 43 paires valides » (M) est faux. Les résultats `daaef112…` donnent directement 67,5 (« bien »), 60,5 (« moyen ») et 53,6 (SP) : 0,138 est une moyenne de 6/V, gonflée par l'inégalité de Jensen. L'empreinte du recoupement manque l. 12 (c'est `c76959a0…`) ; `registres/decisions.md` est cité sans empreinte, il faut citer le texte des lignes.
- Correction : citer le fichier de résultats et son empreinte, corriger le recoupement § 5 dans sa version suivante.
- Gravité : faible.

**CB-16 — l. 23, 135, 178 ; défaut D-b non suivi.**
- Défaut : Le défaut retenu est « factoriel par strate × déterminant », mais N_dpp n'est qu'un descriptif, sans croisement avec β (pas de N_dpp_β0).
- Correction : soit écrire que le factoriel est réduit à une ablation, et pourquoi ; soit ajouter N_dpp_β0 et lire Δ(N_dpp, N_dpp_β0) en secondaire.
- Gravité : faible.

**CB-17 — l. 181, 185, 232 ; coup d'œil sur la validation.**
- Défaut : Calculer l'écart-type de Δ(N, b) sur 200 mondes de validation montre aussi la moyenne avant les mondes de décision.
- Correction : le code ne rend que l'écart-type et les sorties de la grille. La moyenne de Δ(N, b) en validation est scellée, puis lue avec le verdict.
- Gravité : faible.

## Réponses aux questions (a) à (g)
- (a) Oui, le test peut échouer, mais une forme **sans concept** peut être adoptée (CB-02), et le volet « ingrédient » est en partie acquis par construction (CB-01). Une forme utile peut échouer pour une raison de générateur : CB-05, CB-07 et CB-13.
- (b) Le contraste N − N_β0 doit être **obligatoire** pour l'adoption (A7). Il manque le monde à concepts inertes et un placebo global. Les autres témoins et ablations suffisent.
- (c) Avec 1 200 mondes, l'erreur type vaut 0,44 (M). C'est assez pour « borne basse > 0 », pas pour « borne basse ≥ 3 » si l'effet vrai est de 3 points (CB-04).
- (d) La lecture n'est pas encore mécanique : CB-06, CB-07, CB-09, CB-10 et CB-14.
- (e) Liste d'arrêt et R4 : CB-03, CB-07, CB-10 et CB-17. Ajouter : précision placebo hors de [0 ; 1] ou bras de sortie vide sur plus de 2 % des mondes → arrêt.
- (f) Validateur : les sections R1 sont présentes. Il ne bloque pas les marqueurs propres au brouillon (CB-11).
- (g) Lazar gèle en une ligne datée : θ_abs, θ_rel, A7, δ, δ_non, la règle « estimation ≥ δ et borne basse > 0 » (ou la puissance vraie de « borne basse ≥ δ »), la non-régression, le plafond, l'écart-type de garde. Forme proposée : « A1 : dans M_bien **et** M_moyen, écart moyen Δ(N, b) ≥ θ_abs points, rapport des moyennes ≥ θ_rel, borne basse à 95 % de Δ(N, b) > 0 ; A7 : borne basse à 95 % de Δ(N, N_β0) > 0 dans les deux ». Chiffres en points de pourcentage, aucun défaut.

## Conclusion
**Non scellable** en l'état (CB-01 à CB-05 majeurs) ; scellable après corrections et gel de tous les seuils par Lazar, avec une nouvelle contre-lecture du brouillon 2 par un sous-agent neuf.
