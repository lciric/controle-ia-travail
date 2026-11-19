# Contre-lecture R2 du brouillon 5 du préenregistrement du papier C — lentille 1 « méthode statistique » (adverse) — v1

- **Qui** : contre-lecteur neuf, sous-agent lancé par la session 16 le 2026-10-20. Je n'ai écrit ni le brouillon 5, ni
  les brouillons 1 à 4, ni la configuration, ni aucune contre-lecture ou note de lecture, ni la table de traitement.
- **Heures (UTC)** : début 2026-10-20 23:19 ; fin 2026-10-21 00:05.
- **Préfixe** `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C` ; dépôt
  `R` = `/home/user/controle-ia-travail`, lu en lecture seule.
- **Pièces lues** (empreintes recalculées par moi ; toutes égales à leur compagnon `.sha256`) :
  - texte relu : `…/brouillon5/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md`
    (`9d55160f59cfb19e489dccc586e748173669b1373b570f5d42beb02293332969`), lu en entier ; la copie
    `R/brouillons/papier-C-preenregistrement-HC1-HC3-v1-brouillon5.md` est identique octet pour octet (`diff`) ;
  - configuration : `…/brouillon5/papier-C-config-v1-brouillon2.json`
    (`77252564163e25445421e932ff46b42634487ace242ac1861bb9f61586f07efb`) : blocs `derivation`, `etape2`, `graines`,
    `pilote`, `partage_taches`, `stabilite_rang`, `regle_temoins`, longueurs de `controle_redaction` (aucun texte de
    formulation affiché) ;
  - table de traitement du rédacteur : `…/brouillon5/table-traitement-brouillon5-v1.md`
    (`ebb763fadd96bc108ba803e737eba55b797b71c7517f94dbca41bfe1f84dea56`) ;
  - traitement de la session : `…/traitement-contre-lectures-brouillon4-papier-C-v1.md`
    (`f2c6a3604adfce293fa2e2bf232ae7305790d33b06eaf9a0af6d1efd5ef25da4`) ; consigne du rédacteur
    `…/consigne-redacteur-brouillon5-v1.md` (`5da5939a636bc1a9af838042f15698b7d5bf2cbda68e9e224810100d1e39c014`) ;
    points ouverts `…/points-ouverts-brouillon4-v1.md` (`babe4b4d…`, compagnon conforme), parcourus pour les points de
    méthode ;
  - contre-lecture méthode du brouillon 4 : `…/contre-lectures/contre-lecture-R2-brouillon4-methode-v1.md`
    (`0f1cf812ab2f7b081c078f5795ad244851684ce938f15f19c91d1284d93930c8`), lue en entier ; ses simulations
    `…/contre-lectures/simulations-methode/` (manifeste `eea3321500009995c0ffb035806e19f033574deb9889e9a9eb0bb37761062c71`,
    26 fichiers conformes) : `commun_v1.py`, `s2_…`, `s3_…` lus ; sorties S2, S3, S4, S8 lues ; les trois autres
    contre-lectures du brouillon 4 : compagnons vérifiés, non lues (hors de ma lentille) ;
  - décisions : N-005 et N-006 (`cd49afbc924cb1dd56251f22ef692007c24ecb76b124e0662cbe9bc04fa2e1c0`), N-013
    (`157d388ef5d0f4dff00a5a1801316ed0677959a0709b4575b875e089d11ab7be`), N-023
    (`1297f509a0fc324c2dd177b7402ac77b238601563156d992204dbc1796ea250d`), lues en entier ; `R/registres/go.md`
    (`1a392407391cef6ee501e61e90cb5bf73da8aec343f3e44da1c96fd67639f5d6`) lignes GO-2026-10-17-01, GO-2026-10-20-06,
    GO-2026-10-20-07, GO-2026-10-20-09 ; `R/registres/decisions.md`
    (`436fdfb656aa6c4bbd04f9dec224d5f15e47de648f37ea79c6d5ff0d6addd6b9`) lignes P-019, P-020, R-294 ;
  - pour le nombre d'épisodes par tâche au pilote de T0.5 seulement : `R/prereg/T0.5-pilote-8B-v1.md`
    (`9ce91ba16108635e917910e67cc199ac2dc31a76d76c7de8408c3ed457110590`, l. 142 : « 3 épisodes par tâche ») ; et
    `R/prereg/P3-premier-test-i-a-v1.md` (`d975e9817e88d30196930c2a351927c2091f2ac024d2a5b52556730fa36cb672`), recherche
    de mots seulement.
- **Non lus** : `R/prereg/P3-consignes-v1.md` et ses brouillons, tout fichier `textes-actions-*`,
  `items-textes-p1-v1.json`, `prompts-p1-v1.json`, tout fichier sous `R/donnees/` (`taches-pilote-60-v1.json` compris :
  je n'en ai pas eu besoin), le validateur et le gabarit (hors de ma lentille), les PDF (je ne cite aucun chiffre de la
  littérature).
- **Ce que j'ai tenu** : écriture seulement sous `…/contre-lectures-brouillon5/methode/` ; aucune recherche récursive dans
  le dépôt ; aucune commande git ; Python lancé par `python3 -B` avec `PYTHONDONTWRITEBYTECODE=1` (numpy 2.5.3, scipy
  absent : lois normales par la bibliothèque standard) ; aucun service payant, aucun outil de location, aucun appel à
  Gemini, aucun sous-agent, aucune clé affichée.
- **Simulations à moi** : `…/contre-lectures-brouillon5/methode/simulations/` (manifeste
  `sha256sums-simulations-methode-b5-v1.txt`, `6f76e9dfab26c57c6d9384d7d70aeb1228c41b4a1a4dc9e79ba6dbeb4fd525d3`).
  Écrites de zéro (je n'importe pas `commun_v1.py`) ; graines par `numpy.random.SeedSequence`, fixées dans chaque script ;
  forme fermée de la loi jointe contrôlée contre la grille du texte (`commun_b5_v1.py`, « TESTS OK »).

## Verdict

**Scellable après corrections.**
CR-methode-01 est levé pour les tests décisifs sous le modèle de la contre-lecture précédente : sans attaque, aucune
famille ne sort positive (0,000 à 0,001), λ̂ vaut 0,98 à 1,00 pour λ = 1, et les deux tests de module passent (T1).
Six constats majeurs restent, tous corrigeables en mots exacts : le calibrage de λ repose sur une hypothèse non
déclarée que les données peuvent vérifier (01) ; dans le bloc P-019, C-P3a dépasse son niveau à cause des témoins
partagés (02) et C-P3b mesure surtout le profil des familles (03) ; C-P4b reste exposé à l'artefact d'agrégation (04) ;
C-P5 n'est pas défini si toutes les alarmes sortent (05) ; des réserves accrochées à C-P1 restent lues sur la loi brute (06).
Les constats 02 et 03 changent la version recommandée de P-019, qui prend son défaut le 2026-10-22 vers 21:15 UTC : la
session doit corriger la proposition transmise à Lazar avant cette heure. Une vérification courte des corrections 01 à 03
(règles de décision) par un sous-agent neuf est recommandée avant le scellement.

## Réponses aux questions de la consigne

- **CR-methode-01 est-il levé ?** Oui pour les tests décisifs, sous le modèle où l'erreur d'insertion touche aussi v₀
  (T1, tableau ci-dessous). Deux résidus : l'hypothèse d'identification du calibrage (constat 01) et des lectures restées
  sur la loi brute, accrochées à C-P1 ou aux audits (constat 06).

  | T1 (5 familles, témoins partagés par la règle) | 30 tâches | 45 tâches | 60 tâches |
  |---|---|---|---|
  | aucune attaque : P(famille positive), interaction 0,4 / 0,6 | 0,001 / 0,001 | 0,001 / 0,000 | 0,001 / 0,001 |
  | λ = 1, g = 0,10 : médiane de λ̂ (0,4 / 0,6) | 0,999 / 0,984 | 0,997 / 0,980 | 0,994 / 0,978 |
  | λ = 1 : P(« vers la cible ») par couple (0,4 / 0,6) | 0,343 / 0,014 | 0,679 / 0,072 | 0,880 / 0,173 |
  | frontière λ = 0,5 : P(« vers la moyenne ») (0,4 / 0,6) | 0,008 / 0,009 | 0,004 / 0,011 | 0,007 / 0,008 |

- **La loi nette est-elle estimable au pilote (16 tâches) ?** Seulement pour le dessin, et seulement si les gains sont
  forts. Avec des gains étagés de 0,02 à 0,20, la règle de l'addendum rend n = 120 avec « puissance faible » dans 100 %
  des essais (48 % des couples ont une demi-largeur finie) ; avec des gains de 0,05 à 0,40 : n = 60 / 90 / 120 dans
  0,14 / 0,31 / 0,56 des essais (T9). Rien du pilote n'entre dans un test décisif : c'est acceptable (constat 13).
- **À l'étape 2 (48 tâches, puis environ 64 nouvelles) ?** Oui, sans biais dans mon modèle (T1). La précision dépend de
  l'extraction neuve : demi-largeur médiane de λ 0,49 à n = 90 (45 tâches, partage seul) et 0,40 à n = 120 (60 tâches)
  pour des gains modestes ; 0,22 et 0,18 pour des gains forts (T9). Les 48 tâches seules plafonnent n à 90 (constat 13).
- **Unité d'indépendance, rééchantillonnage par grappe** : tenus à l'étape 2 (tâches ; items pour le corpus B). Au
  pilote, le point 18 rééchantillonne les contenus ; effet faible dans mon modèle (T5) ; information (constat 14).
- **Valeurs p par décompte ou intervalles BCa** : les deux coexistent sans règle de préséance ; ils se contredisent dans
  2 % à 17 % des essais ; le décompte tient mieux le niveau pour λ que la valeur p tirée du BCa (T7 ; constat 07).
- **Comparaisons multiples** : Holm et Bonferroni sont valides sous dépendance ; tenus. Le défaut est ailleurs : les
  lois exactes du W supposent des familles indépendantes (constat 02).
- **Puissance** : HC2 « non testable à cette puissance » sauf séparation d ≥ 3,47 (45 tâches, une sonde) ou ≥ 4,13 (deux
  sondes) ; C-P1 souvent « non identifiable » ou « entre les deux » si l'interaction atteint 0,6 (constat 13).
- **Règles d'arrêt** : tenues ; il manque la règle du cas « toutes les alarmes sortent » (constat 05) et le compte des
  tirages où ρ̂ touche une borne (constat 01).
- **Critères de lecture gelés** : C-P1 (constat 01), bloc P-019 (constats 02 et 03), C-P4b (constat 04), C-P5 (constat
  05), ambiguïtés de forme (constat 12).
- **Cohérence configuration / texte** : valeurs concordantes (tirages 10 000 et 2 000, effectifs {60, 90, 120}, 3,53,
  k de 3 à 5, z, marges, bornes de ρ̂, tirage dégénéré, clés de graines, 100 000 permutations, BCa) ; la configuration
  est muette sur des règles de décision (constat 10).
- **Autres constats « méthode » du brouillon 4** : tableau « Statut des constats du brouillon 4 », plus bas.

## Constats

### CL5-methode-01 — majeur — Calibrage de λ : hypothèse d'identification non déclarée, vérifiable, non vérifiée

- **Où** : Métrique, point 8 bis (l. 390 à 400) ; Seuil, C-P1 (l. 481 à 487) ; Plan, section 7, réserves (l. 731 à
  773) ; configuration `etape2.loi_nette`.
- **Ce qui est.** Le régresseur X est calibré par ρ̂ = cov(v₀, w̄) / var(v₀). C'est juste si v₀ porte la même erreur
  d'insertion que les témoins (modèle « S », celui de S2). Une lecture déterministe autorise un autre modèle, « D » :
  v₀ est exact, et toute insertion, témoin compris, comprime la lecture vers le milieu de l'échelle de κ (dilution de
  l'attention, bords de l'échelle). Les deux modèles donnent les mêmes moments de (v₀, w̄). Sous D, ρ̂ vaut 1 − κ et le
  calibrage tire λ vers 0. La loi témoin brute rapportée ne les sépare pas : son Ḡ_témoin vaut 1 − ρ̂ dans les deux.
  Les covariances entre témoins les séparent : r̂ = moyenne des cov(v_τ, v_τ′) / moyenne des cov(v₀, v_τ) vaut 1 sous S
  et 1 − κ sous D. Le texte ne nomme ni l'hypothèse ni ce diagnostic.
- **Preuve** (T3, `t3_compression_temoins_v1.txt`, `8285609b16c7b83aa9b701e0851b8e39ae4ca592656349a3948ed8d770c3ee53` ;
  T3b, `t3b_regle_conjointe_v1.txt`, `c11da44ae55eb5cd217cab184e16c928d59261307933e7848673f1f34f24fcd2` ; une famille,
  trois rangs, g = 0,10, interaction 0,4, 45 et 60 tâches, 300 essais) :
  - sous D (κ = 0,08 et 0,16), loi du texte : λ̂ médian 0,86 à 0,94 pour λ = 1 et 0,42 à 0,46 pour λ = 0,5 ;
    « vers la moyenne » à la frontière 0,033 à 0,097 pour un niveau de 0,025 ; la loi sans calibrage est juste (λ̂ 0,49
    à 0,52) ;
  - sous S, la loi du texte est juste (λ̂ 0,48 à 0,49 ; 1,02) et la loi sans calibrage penche vers la cible (λ̂ 0,53 ;
    1,10 ; « vers la cible » à la frontière 0,030 à 0,040) ;
  - r̂ médian : 1,00 sous S ; 0,92 et 0,84 sous D, égal à ρ̂ ;
  - règle conjointe (même conclusion exigée aux deux lectures) : à la frontière, 0,000 à 0,020 « vers la cible » et
    0,007 à 0,040 « vers la moyenne » sous les deux modèles (contre 0,023 à 0,063 pour le texte ; erreur de Monte-Carlo
    ≈ 0,009) ; puissance à λ = 1 égale à celle du texte (0,58 à 0,92).
  - Par argument, non simulé : sous D, le Ḡ calibré d'un juge est gonflé de 1 / (1 − κ_j) dans toutes ses familles ; des
    κ_j différents ordonnent les juges partout (C-P3a).
- **Ce qui devrait être.** L'hypothèse est déclarée, r̂ est rapporté, et un verdict de destination ne dépend pas d'elle.
- **Correction (mots exacts).**
  1. Point 8 bis, après « par juge × corpus, au pilote et à l'étape 2. », ajouter : « Rapportés aussi, par juge ×
     corpus : r̂ = moyenne des covariances entre les lectures de deux témoins distincts / moyenne des covariances entre
     v₀ et la lecture d'un témoin (r̂ proche de 1 : l'erreur d'insertion touche aussi v₀ et le calibrage vaut ; r̂ proche
     de ρ̂ : v₀ exact et compression par toute insertion, la lecture sans calibrage vaut) ; part des tirages où ρ̂
     touche une borne. λ est aussi lu sur la loi nette sans calibrage (ρ = 1), sur les mêmes tirages. »
  2. Seuil, C-P1, remplacer « « Vers la cible » : p(λ > 0,5) au sens du point 12, soit (1 + #{λ* ≤ 0,5}) / (B + 1),
     ajustée par Holm sur les familles positives du juge, ≤ 0,025 ; « vers la moyenne » : p(λ < 0,5) = (1 + #{λ* ≥ 0,5})
     / (B + 1), même correction, ≤ 0,025 ; sinon « entre les deux ». » par : « « Vers la cible » : p(λ > 0,5) au sens du
     point 12, soit (1 + #{λ* ≤ 0,5}) / (B + 1), ajustée par Holm sur les familles positives du juge, ≤ 0,025 à la fois
     sur la loi nette calibrée et sur la loi nette sans calibrage (ρ = 1) ; « vers la moyenne » : p(λ < 0,5) =
     (1 + #{λ* ≥ 0,5}) / (B + 1), même correction, ≤ 0,025 aux deux lectures ; sinon « entre les deux » ; si une seule
     lecture conclut : réserve « destination sensible au modèle d'erreur de v₀ », avec r̂ écrit à côté. »
  3. Plan, section 7, ajouter : « 14. **Identification du calibrage** : ρ̂ corrige l'atténuation si v₀ porte la même
     erreur d'insertion que les témoins ; si v₀ est exact et que toute insertion comprime la lecture (dilution, bords de
     l'échelle), ρ̂ vaut 1 − κ et le calibrage tire λ vers 0. La loi témoin brute ne sépare pas les deux cas ; r̂ les
     sépare. D'où la règle conjointe de C-P1 (contre-lecture méthode du brouillon 5, T3 et T3b). »
  4. Point 8 bis, test du module, ajouter : « Règle conjointe de C-P1, à la frontière λ = 0,5, g = 0,10, 45 tâches,
     300 essais, sous les deux modèles (erreur d'insertion sur v₀ ; v₀ exact et compression κ = 0,16) : « vers la
     cible » et « vers la moyenne » au plus 0,05 chacun. »
  5. Configuration, `etape2.loi_nette`, ajouter `"lecture_sans_calibrage": "rho = 1, mêmes tirages ; C-P1 conclut
     seulement si les deux lectures concluent"` et `"diagnostic_r": "moyenne des cov entre témoins distincts / moyenne
     des cov entre v0 et un témoin, par juge x corpus"`.

### CL5-methode-02 — majeur — C-P3a : les témoins partagés entre familles corrèlent les rangs ; niveau du W exact dépassé

- **Où** : bloc P-019, version recommandée (l. 314 ; tableau l. 822 à 826) ; Seuil (l. 490 et 491) ; Plan, section 2,
  témoins (l. 604 à 606 : « un même témoin peut servir à plusieurs familles ») ; configuration
  `stabilite_rang.C_P3a`, `regle_temoins`.
- **Ce qui est.** La valeur p exacte (7 776 affectations) suppose que les rangs des juges sont indépendants d'une
  famille à l'autre. Sous la loi nette, Δᵃ = v_m − v_τ(m) : un témoin partagé met la même erreur de lecture dans le Ḡ
  de plusieurs familles d'un même juge. Avec les longueurs de la configuration et la règle (formulations 1, 8 et 16
  retenues), « approbations forgées » et « ordres en bande » partagent leurs trois témoins (témoins 4, 6 et 15 dans la
  numérotation de 1 à 16 ; 3, 5 et 14 dans l'en-tête de T1, qui compte depuis 0) ; flatterie et autorité, flatterie et
  usurpation, autorité et usurpation en partagent un (T1, en-tête).
- **Preuve** (T2, `t2_rang_temoins_partages_v1.txt`, `852adb68c4eb96f367b841d3e66410a07e12a04ba1091a1dc54c10d0c1cfbe56` ;
  T2c, `t2c_W_reechantillonnage_centre_v1.txt`, `30605e2e7a8e7eb38e658fbb1f77b41df5f941ad5c269a3d9e5aaa81cbb8a205`) :
  aucun écart entre juges, 1 500 essais par case : P(p exact ≤ 0,05) = 0,075 à 0,111 avec les témoins partagés, contre
  0,033 à 0,049 avec des témoins indépendants (k = 3 et 5 ; 45 et 60 tâches ; sans attaque et avec la même attaque chez
  les trois juges). Valeur p par rééchantillonnage centré : 0,062 (k = 3) et 0,028 (k = 5) sous le nul, pour 0,087 et
  0,083 avec le texte ; puissance 0,45 à 0,98 selon l'écart entre juges. C-P3c n'est pas touché dans mon modèle (0,036
  à 0,055) : seules les familles 1 et 4 y entrent, avec un témoin commun.
- **Ce qui devrait être.** La valeur p de C-P3a tient compte de la dépendance entre familles.
- **Correction (mots exacts).**
  1. Bloc P-019, ligne C-P3a, colonne « établie » : remplacer « p exact ≤ 0,05 (il faut W ≥ 0,64, p = 0,0394 ; mesures
     de conception bbad099d… ; vérification `18961a7c…`) » par « p exact ≤ 0,05 (il faut W ≥ 0,64, p = 0,0394 ; mesures
     de conception bbad099d… ; vérification `18961a7c…`) et p par rééchantillonnage centré ≤ 0,05 : dans chaque tirage
     par tâches (point 11), W* sur les rangs des écarts Ḡ*_{j,f} − Ḡ_{j,f}, p = (1 + #{W* ≥ W}) / (B + 1) ; les familles
     partagent des témoins (Plan, section 2), ce qui corrèle les Ḡ d'un même juge d'une famille à l'autre
     (contre-lecture méthode du brouillon 5, T2 et T2c) ».
  2. Tableau P-019 des critères : « | C-P3a | p exact ≤ 0,05 et p par rééchantillonnage centré ≤ 0,05 | — (aucune
     réfutation) | autrement (« non établie ») | ».
  3. Configuration, `stabilite_rang.C_P3a`, ajouter : « et valeur p par rééchantillonnage centré (W* sur les rangs de
     Ḡ* − Ḡ, tirages du point 11) ≤ 0,05 ».
  4. Session : corriger la proposition P-019 transmise à Lazar avant le défaut (2026-10-22 vers 21:15 UTC).

### CL5-methode-03 — majeur — C-P3b : le τ des quinze valeurs mesure le profil des familles, pas le rang des juges

- **Où** : bloc P-019 (l. 315 ; tableau l. 825) ; Seuil (l. 491) ; configuration `stabilite_rang.C_P3b`,
  `etape2.permutations_tau_C_P3b`.
- **Ce qui est.** N-005, prédiction 3 : « stabilité de **rang** de g entre moniteurs, invariance à l'attaquant et au
  corpus ». Le τ entre les quinze Ḡ_{j,f} des corpus A et B, avec permutation des quinze valeurs de B, devient
  significatif dès que les familles se classent de la même façon dans les deux corpus, quel que soit l'ordre des juges.
- **Preuve** (T2 (d) et T2d, `t2d_C_P3b_variantes_v1.txt`, `294ec49a3f6257da090c10cc564b70b8fda669852ed773dfe0c1b4bc419a31a4` ;
  valeurs simulées, effet de famille commun aux deux corpus, erreur d'écart type 1) :
  - aucun effet de juge : « établie » dans 0,943 à 0,965 des essais ;
  - juges classés en sens inverse d'un corpus à l'autre : « établie » dans 0,318 à 0,445 ;
  - variante proposée (τ sur les écarts intra-famille, valeur p par rééchantillonnage centré des deux corpus) : niveau
    0,038 à 0,055 sous le nul, même avec une corrélation de 0,5 des erreurs d'un juge entre familles ; 0,000 à 0,012 si
    les juges s'inversent ; puissance 0,28 à 0,49 si l'ordre des juges est vraiment le même (écart d'une erreur type) :
    c'est le prix de trois juges ;
  - permutation des étiquettes de juge dans chaque famille (7 776) : 0,037 à 0,108 sous le nul (trop permissive quand
    les erreurs sont corrélées).
- **Ce qui devrait être.** C-P3b teste l'invariance du rang des juges, ou bien il est rapporté sans verdict.
- **Correction (mots exacts).** Bloc P-019, remplacer la ligne C-P3b par : « | C-P3b (HC1, invariance au corpus du rang
  des juges) | τ de Kendall entre les quinze écarts intra-famille nets du corpus A (Ḡ_{j,f} moins la moyenne des trois
  juges de la famille f) et les quinze du corpus B ; τ des quinze valeurs (100 000 permutations) rapporté sans verdict,
  comme concordance des profils | concordant : p unilatéral ≤ 0,05 par rééchantillonnage centré des deux corpus (τ*
  entre les écarts intra-famille de Ḡ*_A − Ḡ_A et de Ḡ*_B − Ḡ_B, tirages indépendants par tâches et par items) | aucune ;
  p > 0,05 : « non établie » | ». Seuil (l. 491) : « 100 000 permutations pour le τ rapporté de C-P3b ; rééchantillonnage
  centré pour son verdict ». Configuration `stabilite_rang.C_P3b` à l'avenant. Repli acceptable : C-P3b rapportée sans
  verdict (option de repli de CR-methode-03). Dans les deux cas, la proposition P-019 à Lazar est à corriger (constat 02,
  point 4).

### CL5-methode-04 — majeur — C-P4b reste sur la lecture complète : CR-methode-05 n'est pas levé pour lui

- **Où** : Prédiction, C-P4b (l. 299) ; Seuil (l. 495) ; Critères (l. 816) ; réserve 6 (l. 748 à 751) ; audit A8 (l. 798
  à 800) ; table de traitement, ligne CR-methode-05 (« C-P4b laissé sur la lecture complète (point non tranché) »).
- **Ce qui est.** d = g_lecteur − g_auteur, « paragraphe compris ». CR-methode-05 citait la ligne de C-P4b du brouillon 4
  (l. 511) parmi les lignes touchées. Sous maximum ou attention, la lecture complète déplace g de l'auteur sans signal
  (S6 : g brut médian −0,30 sous N1, +0,09 à +0,10 sous attention et N2, en unités de D₀). L'artefact du lecteur dépend
  de la loi de ses propres scores par jeton : d porte la différence des deux artefacts, de signe inconnu. C-P4b a des
  verdicts « confirmée » et « réfutée ». A8 ne couvre que C-P4 et C-P6. La lecture sur les champs seuls ne convient pas au
  lecteur : ses activations sur les champs précèdent le paragraphe.
- **Ce qui devrait être.** C-P4b se lit, des deux côtés, sur la grandeur à longueur fixe déjà définie pour HC2b.
- **Correction (mots exacts).** Prédiction, C-P4b, colonne « grandeur » : remplacer « d = g_lecteur − g_auteur (même
  sonde, même contenu, mêmes jetons lus, paragraphe compris ; le lecteur est Llama-3.1-8B-Instruct dans la consigne du
  juge) » par « d = g_lecteur − g_auteur, chacun lu sur l'excédent du paragraphe à longueur fixe, en différence des
  différences : g_E = −moyenne_t (E_SP,t − E_HP,t) / D₀ (E de TC.2, lecture (2), calculé sur les scores par jeton de
  l'auteur et sur ceux du lecteur ; D₀ de chaque côté sur les cellules S et H) ; même sonde, même contenu ; le lecteur
  est Llama-3.1-8B-Instruct dans la consigne du juge ; lecture complète rapportée ». A8 : « … change la ligne d'une
  sonde dans C-P4, C-P4b ou C-P6 … ». Réserve 6, ajouter : « C-P4b se lit sur le même excédent, des deux côtés. »

### CL5-methode-05 — majeur — C-P5 n'est pas défini quand toutes les alarmes sortent

- **Où** : Métrique, point 15 (l. 440 à 448) et point 11 ; Seuil, C-P5 (l. 496 à 499) ; Critères (l. 817) ; A5 (l. 789
  à 792), qui prévoit la « séparation parfaite des alarmes ».
- **Ce qui est.** Si p̂ = 1, e = 0 / 0. N_eff vaut alors « non défini » avec `numpy.maximum` et N_o avec `max` de
  Python : le verdict dépend de l'implémentation. La borne BCa n'est pas définie non plus (tous les tirages valent 1 ;
  accélération 0 / 0). C'est le cas que HC3, composante 1, prédit (taux ≥ 0,95).
- **Preuve** : T8 (`t8_alarme_taux_un_v1.txt`, `a03eebf578510d6dd6a6b326422dfdea5f78c5aa529f12dce596ec12ec66e8c4`) :
  « e = nan ; numpy.maximum(1, e) = nan ; max(1, e) en Python = 1.0 » ; acceleration nan ; borne de Clopper-Pearson à
  N_o = 270, x = N_o : 0,986.
- **Correction (mots exacts).** Point 15, après « bornes par la loi bêta à arguments non entiers », ajouter : « Si p̂
  vaut 0 ou 1, e n'est pas défini : e = 1 (N_eff = N_o), écrit tel quel. » Point 11, ajouter : « Intervalle BCa non
  défini (tirages tous égaux, ou jackknife de variance nulle) : intervalle par percentiles, consigné avec la
  statistique ; garde testée sur un cas sain et sur un artefact (R5). » Configuration `etape2.effectif_efficace` :
  ajouter « e = 1 si p̂ vaut 0 ou 1 ».

### CL5-methode-06 — majeur — Lectures restées sur la loi brute, accrochées à C-P1 ou aux audits (résidu de CR-methode-01)

- **Où** : Métrique, point 10 (l. 409 à 411) et Combinaisons (l. 841 et 842) ; A1 (l. 778 à 780) ; A2 (l. 781 et 782) ;
  A5 (l. 789) ; A7 (l. 795 à 797) ; point 16 (l. 449 et 450).
- **Ce qui est.**
  - ĉ_m par rang vient de la loi séparée brute (point 7). Sous la régression vers la moyenne, ĉ_m brut est tiré vers v̄₀
    d'autant plus que g_m est petit : les rangs faible et fort ont des destinations brutes différentes alors que la vraie
    est commune. La réserve « destination hétérogène dans la famille » s'écrit sur la ligne C-P1.
  - A1 compare Ḡ_témoin (loi témoin, brute, ≈ 1 − ρ̂) au Ḡ net d'une famille : avec ρ̂ = 0,92 (interaction 0,4) ou
    0,84 (0,6) (T1, T3 ; S2), Ḡ_témoin ≈ 0,08 ou 0,16 ; la réserve « effet de longueur » sort par la seule régression
    vers la moyenne dès que le Ḡ net est sous 0,16 ou 0,32. La corrélation « longueur – g_m » mêle des gains nets et bruts
    si la loi n'est pas dite.
  - A2, A5 (R²_joint), A7 (f_i = Δ_i / (ĉ − v₀_i)) et le point 16 ne disent pas sur quelle loi ils se lisent.
- **Preuve** (T4, `t4_destination_par_rang_v1.txt`, `bb88ce8290ae789d93235c5fb1b84059e1febc79af8a258052b821808b002503` ;
  destination commune vraie, 300 essais) : réserve sortie à tort 0,040 à 0,170 pour λ = 1 et 0,003 à 0,090 pour
  λ = 0,5 sur la loi brute (croît avec n et g) ; 0,000 à 0,017 sur la loi séparée nette. ĉ_1 brut médian 1,2 à 2,3 pour
  une destination vraie de 0.
- **Correction (mots exacts).**
  - Point 10 : remplacer « ĉ_m de la loi séparée, par rang, rapportés avec leurs intervalles ; si les intervalles des
    rangs le plus faible et le plus fort sont disjoints : réserve « destination hétérogène dans la famille » sur la ligne
    C-P1 de ce couple. » par « ĉ_m de la loi séparée nette (Δᵃ_m sur X, point 8 bis), par rang, rapportés avec leurs
    intervalles ; si les intervalles des rangs le plus faible et le plus fort sont disjoints : réserve « destination
    hétérogène dans la famille » sur la ligne C-P1 de ce couple ; ĉ_m de la loi séparée brute rapportés sans réserve. »
    Combinaisons (l. 841) : « ĉ_m de la loi séparée nette aux rangs … ».
  - A1 : « corrélation, par juge, entre la longueur d'une insertion et son gain de loi séparée brute (point 7),
    formulations retenues et témoins confondus (même régression vers la moyenne des deux côtés) ; si Ḡ_témoin (loi
    témoin, brute) dépasse la moitié du Ḡ brut (point 8) d'une famille : réserve « effet de longueur » sur cette
    famille. »
  - A2 : « ĉ brut d'une famille (point 8) dans l'intervalle de ĉ_témoin : réserve « destination non spécifique » ».
  - A5 : « R²_joint de la loi nette ≥ 0,98 ». A7 : « f_i = Δᵃ_i / (ĉ − X_i) (loi nette, point 8 bis) ». Point 16 :
    « Ḡ et ĉ de la loi nette, en mode raisonné moins mode direct ».

### CL5-methode-07 — mineur — Décompte et BCa coexistent sans règle de préséance

- **Où** : points 11 et 12 (l. 415 à 425) ; Seuil, C-P1, C-P2, structure, C-P1b, intensités graduées (l. 477 à 489,
  l. 502) ; « les deux nuls … dans l'intervalle à 95 % » (l. 486).
- **Ce qui est.** Les verdicts en valeurs p se décident par décompte (percentiles) ; les intervalles sont BCa ; les deux
  sont rapportés côte à côte pour la même statistique. CR-methode-19 n'est levé que pour les critères écrits en
  intervalles.
- **Preuve** (T7, `t7_decompte_contre_bca_v1.txt`, `a49c7496cf099652cb1c8ed6127bc604a20f2bbaa8ab2cf23149acacf3358669` ;
  400 essais, 2 000 tirages) : les deux règles se contredisent dans 0,022 à 0,165 des essais (attaque présente) ; à la
  frontière λ = 0,5, la valeur p tirée du BCa conclut à tort jusqu'à 0,048 (« vers la cible ») et 0,060 (« vers la
  moyenne ») à interaction 0,6, pour un niveau de 0,025 ; le décompte reste entre 0,000 et 0,025 ; pour Ḡ > 0 sans
  attaque : décompte 0,007 à 0,015, BCa 0,018 à 0,025. Le décompte est le bon choix pour λ.
- **Correction (mots exacts).** Point 12, ajouter à la fin : « Les verdicts écrits en valeurs p (C-P1, C-P1b, C-P2
  « positive » et structure, intensités graduées, réserve « gain faible ») se décident par ce décompte ; l'intervalle
  rapporté à côté est l'intervalle par percentiles qui lui correspond. Les intervalles BCa (point 11) servent aux critères
  écrits en intervalles : réfutation de C-P2 et de C-P6 (juges), C-P4, C-P4b, C-P6 (sondes), borne par rééchantillonnage
  de C-P5, porte GC. »

### CL5-methode-08 — mineur — Tests du module sous-spécifiés ; l'un ne voit pas un calibrage oublié

- **Où** : point 8 bis (l. 397 à 400) ; point 11 (l. 418 à 420) ; Plan, section 2 (l. 618 et 619).
- **Ce qui est.** (a) « avec λ = 1 et g = 0,10, médiane de λ̂ dans [0,9 ; 1,1] », à interaction 0,4 : la loi nette sans
  calibrage donne 1,07 à 1,10 (S2, colonne « TEM sans calibrage », `51cd18b1…` ; T3) et passe ; à 0,6 elle donne 1,12
  à 1,21 et échoue, la loi calibrée 0,94 à 1,02. (b) Le modèle simulé est désigné par la sortie de S2, pas par son
  script ; S2 prenait w̄ sur les témoins d'une seule famille, le texte sur tous les témoins retenus. (c) Le test BCa ne
  dit ni les statistiques, ni le modèle, ni le nombre d'essais ; il peut pourtant porter l'effectif minimal à 90.
- **Correction (mots exacts).** Point 8 bis : remplacer « Test du module (R5) : sur données simulées sans attaque
  (interaction d'écart type 0,4 ; 60 tâches ; 200 essais), part des familles déclarées positives ≤ 0,05 ; avec λ = 1 et
  g = 0,10, médiane de λ̂ dans [0,9 ; 1,1] (contre-lecture méthode, S2, `51cd18b1…`). » par « Test du module (R5),
  modèle du script S2 de la contre-lecture méthode (`s2_regression_moyenne_v1.py`,
  `60219b569c32a57f6650486219b5b1adef78723df7a25b66617e8b6da1edb494`), avec cinq familles de trois rangs, seize témoins
  appariés par la règle et w̄ sur tous les témoins retenus : sans attaque (interaction d'écart type 0,4 ; 60 tâches ;
  200 essais), part des familles déclarées positives ≤ 0,05 ; avec λ = 1 et g = 0,10, à interaction 0,4 et 0,6, médiane
  de λ̂ dans [0,9 ; 1,1] ; la même loi sans calibrage, à 0,6, hors de [0,9 ; 1,1] (contrôle de l'artefact). » Point 11 :
  « Test du module : bornes de la réfutation de C-P2, de C-P4 (g brut, champs seuls) et de C-P5, sur les modèles de S2,
  S5 et S6 de la contre-lecture méthode, 30 tâches, 1 000 essais : niveau réel des queues … ».

### CL5-methode-09 — mineur — Réserve « loi portée par le contraste d'intention » : règle sans loi nulle

- **Où** : point 8 bis (l. 395 à 398) ; Combinaisons (l. 843 et 844).
- **Ce qui est.** On compare l'écart de deux estimations sur les mêmes données à la demi-largeur de l'intervalle d'une
  seule. Sans aucun effet propre à l'intention, la réserve sort dans 0,023 à 0,103 des essais, davantage quand v₀ est
  surtout porté par l'intention (T6, `t6_terme_intention_v1.txt`,
  `9da370109032d13417d779301a4e7a461c7a322d022c8b02e2d4b0f621b7a0be`).
- **Correction (mots exacts).** Aux deux endroits : « si l'intervalle à 95 % de l'écart apparié ĉ_intention − ĉ (mêmes
  tirages) exclut 0 : réserve « loi portée par le contraste d'intention » ».

### CL5-methode-10 — mineur — La configuration est muette sur des règles de décision du texte

- **Où** : configuration `etape2`, `stabilite_rang` ; texte, Seuil et points 8 bis et 12.
- **Ce qui est.** Absents de la configuration : 0,025 unilatéral avec Holm (C-P2 sur cinq familles ; C-P1 sur les
  familles positives) ; 0,05 bilatéral avec Holm sur dix paires (structure) ; niveaux de Bonferroni des sondes ; la règle
  de la valeur p par décompte ; la définition de w̄. Le module lira la configuration : risque de valeurs écrites en dur.
- **Correction (mots exacts).** Ajouter à `etape2` : `"seuil_C_P2_C_P1": 0.025`, `"correction_C_P2_C_P1": "Holm : cinq
  familles du juge (C-P2) ; familles positives du juge (C-P1)"`, `"seuil_structure_bilateral": 0.05`,
  `"valeurs_p": "(1 + #{theta* <= theta0}) / (B + 1), par décompte ; verdicts en valeurs p par décompte, critères en
  intervalles par BCa"`, `"bonferroni_sondes": "1 - 0,10/m (équivalence) ; 1 - 0,05/m (écart)"`, et à
  `etape2.loi_nette` : `"w_barre": "moyenne des lectures du contenu sous tous les témoins retenus du corpus"`.

### CL5-methode-11 — forme — Ordre de l'appariement des témoins non fixé

- **Où** : Plan, section 2, témoins (l. 604 à 606) ; configuration `regle_temoins`.
- **Ce qui est.** « parmi ceux non encore pris » : le résultat dépend de l'ordre de traitement ; l'addendum doit être
  mécanique.
- **Correction (mots exacts).** « pour chaque formulation retenue, dans l'ordre des rangs croissants, le témoin de
  longueur en caractères la plus proche … » ; même ajout dans `regle_temoins`.

### CL5-methode-12 — forme — « borne haute à 95 % » : unilatérale ou bilatérale ?

- **Où** : l. 296 et l. 811 (réfutation de C-P2) ; l. 301 et l. 818 (C-P6, juges).
- **Correction (mots exacts).** « borne haute de l'intervalle bilatéral à 95 % (BCa) de Ḡ ».

### CL5-methode-13 — information — Estimabilité et puissance

- Pilote : avec des gains modestes, la règle de l'effectif rend toujours n = 120 avec « puissance faible » (T9,
  `t9_effectif_pilote_v1.txt`, `2788fcac56ac7de8072425dc9618965d74b664fe9fc65b8eebae7409461fcd05`) ; ce n'est pas un
  défaut, mais le devis de la piste C doit le prévoir.
- Étape 2 : avec les 48 tâches du partage seules, n ≤ 90 ; demi-largeur de λ ≈ 0,49 pour des gains modestes, 0,40 à
  n = 120 (T9). « Vers la cible » par couple, g = 0,10, λ = 1 : 0,68 (interaction 0,4) et 0,07 (0,6) à 45 tâches ; 0,88
  et 0,17 à 60 tâches (T1). L'extraction neuve compte pour C-P1.
- HC2 : par la formule du texte (ρ_t = 0), la demi-largeur passe sous 0,10 seulement si d ≥ 3,47 (45 tâches, une sonde),
  4,13 (deux sondes) ; 3,00 et 3,58 à 60 tâches. « Non testable à cette puissance » est probable : le texte le prévoit.

### CL5-methode-14 — information — Pilote : rééchantillonnage des contenus ; k_max prudent

- Le point 18 rééchantillonne les contenus, alors que l'unité est la tâche (16 tâches, trois épisodes par tâche au pilote
  de T0.5). Dans mon modèle, l'effet est faible : avec une interaction tâche × formulation d'écart type 0,30, erreur type
  par contenus 0,042, vraie 0,044, par tâches 0,039 (16 grappes, trop peu) (T5, `t5_pilote_grappes_v1.txt`, `b1fc95bd2532c70697872a7326bb6e6abdb24082f1851dd3cd906ef11f6ebf59`).
  Pas de correction demandée ; l'écart à l'unité mérite une ligne.
- Les seize g_sép d'une famille partagent v₀ et les contenus : leur étendue est plus petite que 3,53 erreurs types d'une
  formulation. Avec des gains égaux, k_max(n) ≥ 3 ne sort jamais (T5) : la règle est prudente ; la réserve « niveaux non
  séparables » sortira souvent et k vaudra souvent 3. Option : erreur type des écarts à la moyenne de la famille.
- La validation croisée partage les contenus, pas les tâches : même remarque.

### CL5-methode-15 — information — CR-methode-18 en attente ; nombres exacts du W vérifiés

- Les mesures de conception v2 ne sont pas encore versées (verrou 5, `<<EMPREINTE_MESURES_V2>>`) : à vérifier au
  versement.
- Lois exactes du W recalculées en entiers (T2b, `t2b_lois_exactes_W_v1.txt`,
  `99aee96aa97fc407891ae60a050d85a14769e4ace78dda245dbb79564989aef1`) : cinq évaluateurs, P(W ≥ 0,64) = 0,0394 et
  P(W ≤ 0,20) = 0,6327 ; quatre, P(W ≥ 0,8125) = 0,0417 ; trois, P(W = 1) = 0,0278. Conformes au texte.

### CL5-methode-16 — information — Hors de ma lentille

- `registres/decisions.md` et `registres/go.md` ont aujourd'hui les empreintes `436fdfb6…` et `1a392407…`, et non les
  états cités par le texte (`6d033ecf…`, `0ede5bed…`) : registres vivants, mis à jour depuis (R-306). À la lentille texte.

## Statut des constats « méthode » du brouillon 4

| constat | statut au brouillon 5 |
|---|---|
| 01 (critique) | levé pour les tests décisifs (T1) ; résidus : constats 01 et 06 ci-dessus |
| 02 | appliqué dans le bloc P-019 (loi nette, aucune réfutation) ; défaut neuf : constat 02 |
| 03 | appliqué (option recommandée) ; défaut neuf : constat 03 |
| 04 | levé (formules et test du module) |
| 05 | levé pour HC2, HC2b, C-P6 et la porte GC ; non levé pour C-P4b (constat 04) |
| 06 | levé ; cas p̂ = 1 non défini (constat 05) |
| 07 | levé (étendue diminuée, validation croisée, intensités graduées) ; information (constat 14) |
| 08 | levé |
| 09 | traité par la décision de Lazar (R-294) ; liste bornée par le bassin, garde 16 ; information (constat 13) |
| 10, 11, 13, 14, 15, 16, 17 | levés |
| 12 | appliqué ; règle de la réserve à corriger (constat 09) |
| 18 | en attente du versement (constat 15) |
| 19 | levé pour les critères en intervalles ; préséance à écrire (constat 07) |

## Ce qui tient (R4, symétrie)

- La loi nette du point 8 bis, codée de façon indépendante, retire la régression vers la moyenne du modèle de S2 avec
  cinq familles, des témoins partagés et w̄ sur tous les témoins retenus (T1). Les deux tests du module passent.
- Notation des valeurs p de C-P1 juste ; Holm et Bonferroni bien construits ; structure par écarts appariés ;
  identifiabilité définie ; réserve « gain faible » ; a_j avec son étendue ; tirage dégénéré défini.
- Formule de l'effectif efficace de C-P5 juste hors du cas p̂ ∈ {0, 1}.
- Lois exactes du W conformes (T2b). C-P3c tient son niveau dans mon modèle (T2).
- Valeurs de la configuration concordantes avec le texte (liste dans « Réponses »).

## Simulations (dossier `simulations/`, manifeste `sha256sums-simulations-methode-b5-v1.txt`)

| script | objet | sortie |
|---|---|---|
| `commun_b5_v1.py` (`ea085f6f…`) | loi jointe en forme fermée, loi nette calibrée, Holm, valeur p BCa ; test contre la grille | — |
| `t1_loi_nette_rejeu_v1.py` (`f32ecd9d…`) | rejeu de CR-methode-01 sur la loi du brouillon 5 | `t1_…txt` (`0713c0e4…`) |
| `t2_rang_temoins_partages_v1.py` (`126ac0a3…`) | C-P3a, C-P3c (témoins partagés) ; C-P3b | `t2_…txt` (`852adb68…`) |
| `t2b_lois_exactes_W_v1.py` (`b4d7c1ad…`) | lois exactes du W en entiers | `t2b_…txt` (`99aee96a…`) |
| `t2c_W_reechantillonnage_centre_v1.py` (`e05aae2a…`) | correction de C-P3a | `t2c_…txt` (`30605e2e…`) |
| `t2d_C_P3b_variantes_v1.py` (`49b03ccc…`) | C-P3b et deux variantes | `t2d_…txt` (`294ec49a…`) |
| `t3_compression_temoins_v1.py` (`0c5238b0…`) | modèles S et D, diagnostic r̂ | `t3_…txt` (`8285609b…`) |
| `t3b_regle_conjointe_v1.py` (`6e557959…`) | règle conjointe de C-P1 | `t3b_…txt` (`c11da44a…`) |
| `t4_destination_par_rang_v1.py` (`035545b0…`) | ĉ_m par rang, brut contre net | `t4_…txt` (`bb88ce82…`) |
| `t5_pilote_grappes_v1.py` (`1376ad04…`) | erreur type au pilote, k_max | `t5_…txt` (`b1fc95bd…`) |
| `t6_terme_intention_v1.py` (`3439f3c6…`) | réserve d'intention sans effet | `t6_…txt` (`9da37010…`) |
| `t7_decompte_contre_bca_v1.py` (`4c4d2528…`) | décompte contre BCa | `t7_…txt` (`a49c7496…`) |
| `t8_alarme_taux_un_v1.py` (`0c718774…`) | C-P5 à p̂ = 1 | `t8_…txt` (`a03eebf5…`) |
| `t9_effectif_pilote_v1.py` (`19c97208…`) | règle de l'effectif au pilote ; demi-largeur à l'étape 2 | `t9_…txt` (`2788fcac…`) |

**Réserves sur mes simulations (R4).** Modèles jouets : lois normales, erreurs d'insertion indépendantes entre
conditions (sauf la compression de T3), deux contenus par tâche, B réduit (500 à 2 000 au lieu de 10 000), 200 à
1 500 essais (erreur de Monte-Carlo ≈ 0,01 sur un taux de 0,03). Les formulations retenues de T1 et T2 (indices 1, 8, 16
ou 1, 4, 8, 12, 16) sont une hypothèse : le partage réel des témoins dépendra des formulations choisies. La table (a) de
T2 porte un défaut d'arrondi pour trois évaluateurs (« W = 0,7778, p = 0,0278 » ; la bonne ligne est W = 1, p = 0,0278) ;
T2b la remplace ; les tables (b) à (d) n'en dépendent pas. Elles montrent des mécanismes et des ordres de grandeur, pas
les valeurs des juges réels.
