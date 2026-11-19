# Contre-lecture R2 du brouillon 6 du papier C — lentille « vérification courte de méthode » (adverse) — v1

- **Qui** : relecteur neuf, sous-agent lancé par la session 16. Je n'ai écrit ni les brouillons 1 à 6, ni leur
  configuration, ni aucune contre-lecture, note de voisins, projet de traitement ou traitement du papier C.
- **Heures (UTC)** : début 2026-10-21 01:07 ; fin vers 01:50.
- **Préfixe** `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/papier-C` ; dépôt
  `R` = `/home/user/controle-ia-travail`, lu en lecture seule.
- **Consigne** : `…/consigne-contre-lectures-brouillon6-v1.md`
  (`08c1acdbd115521425ac50b2699ddbeeed2a2d5b37e6157255e5ff214e4c2899`, égale à son compagnon). Partie commune et lentille
  « vérification courte de méthode » seulement.
- **Pièces** (empreintes recalculées par moi ; toutes égales à leur compagnon `.sha256`) :
  - texte relu : `…/brouillon6/papier-C-preenregistrement-HC1-HC3-v1-brouillon6.md`
    (`fadc74c3b40b6e6aee9035f5a9566288d17d60b8403b57863721c2ee57554d00`) : en-tête, verrous, Prédiction (bloc P-021),
    Métrique (points 8 bis à 12), Seuil, réserve 15, Critères de lecture ;
  - configuration `…/brouillon6/papier-C-config-v1-brouillon3.json` (`85173b22defe2c55844f23691028233a13746394324d0c598d3a66fb4f68820d`) :
    `stabilite_rang`, `etape2.loi_nette`, `regle_temoins`, longueurs de `controle_redaction` (égales à celles de la
    configuration brouillon 2, vérifié par script ; aucun texte de formulation lu ni affiché) ;
  - table `…/brouillon6/table-traitement-brouillon6-v1.md` (`74b5ae16e322b74340f793253af9387680ba370512fe5e9b8477a742d4d2f370`),
    lignes CL5-01 à CL5-03, CL5-08 ; sortie `…/brouillon6/problemes-brouillon6-v1.txt` (`335116c0…`, conforme) ; outils
    `…/brouillon6/travail/` : compagnons vérifiés, non lus (hors de ma lentille) ;
  - traitement `…/traitement-contre-lectures-brouillon5-papier-C-v1.md` (`08ca42ae7bd70a08a3695aca66ba0d16ee175da1771ba2c37ed6eda20cceb00e`) ;
    projet `…/traitement-brouillon5/traitement-contre-lectures-brouillon5-papier-C-projet-v1.md`
    (`c65aa83acb830c765b9bc4cee7f600d45708771eef12de0502237a4234d42d25`), sections 1.2, 3 et 6.3 ;
  - rapport méthode du brouillon 5 `…/contre-lectures-brouillon5/methode/contre-lecture-R2-brouillon5-methode-v1.md`
    (`0c492f02…`, conforme), lu en entier ; ses simulations (manifeste `sha256sums-simulations-methode-b5-v1.txt`,
    28 fichiers conformes, avant et après mes calculs) : `commun_b5_v1.py`, `t1`, `t2`, `t2c`, `t2d`, `t3`, `t3b` lus ;
  - registre `R/registres/decisions.md` (`6005137f…`, état lu à 01:15 UTC), ligne P-021 seulement.
- **Non lus** : `R/prereg/P3-consignes-v1.md`, tout fichier `textes-actions-*`, `items-textes-p1-v1.json`,
  `prompts-p1-v1.json`, rien sous `R/donnees/`, `R/runs/`, `R/diag/`, `R/traces/` ; aucune recherche récursive.
- **Ce que j'ai tenu** : écriture seulement sous `…/contre-lectures-brouillon6/methode-courte/` ; aucun réseau ; aucune
  commande git ; aucun sous-agent ; aucune dépense ; aucune clé ; `python3 -B` avec `PYTHONDONTWRITEBYTECODE=1`
  (numpy 2.5.3 ; aucun `__pycache__` créé, ni chez moi ni dans le dossier du brouillon 5). Les scripts du brouillon 5
  sont importés, jamais modifiés.
- **Simulations** : `…/contre-lectures-brouillon6/methode-courte/simulations/`, manifeste
  `sha256sums-simulations-methode-courte-b6-v1.txt` (`368f3ec867c05991ce4069c2854dc17aa61a508cb8e2462b18764654cb975bed`,
  61 lignes : 4 scripts, 3 listes de cases, 54 sorties). Graines par `numpy.random.SeedSequence`, base 20261021, dérivées
  par case.

## Verdict

**Scellable après corrections.**
Dans le modèle de la contre-lecture méthode du brouillon 5, rejoué avec un vrai rééchantillonnage par grappes, les trois
règles de l'option (A) de P-021 tiennent leur niveau pour k = 3 et k = 5, 45 et 60 tâches (aux deux lectures : C-P3a
0,012 à 0,042, C-P3b 0,030 à 0,048, C-P3c 0,019 à 0,053 ; erreur de Monte-Carlo ≈ 0,004 à 0,005). La règle conjointe de
C-P1 tient aussi, y compris quand un même juge porte les deux erreurs (0,000 à 0,028).
Mais l'extension « deux lectures » aux statistiques de rang ne protège pas quand les juges n'ont pas le même modèle
d'erreur (erreur sur v₀ chez l'un, compression chez l'autre) : les deux lectures ordonnent alors les juges dans le même
sens sans aucun écart vrai, et C-P3a et C-P3b sortent « établie » à tort dans 0,081 à 0,136 et 0,070 à 0,125 des essais
à g = 0,20 (constat 01). Une troisième lecture, calibrée par ρ̂/r̂ à partir du diagnostic déjà écrit, ramène les deux
règles à 0,008 à 0,043, pour une perte de puissance de 0,02 à 0,03. La clause de repli n'est pas applicable telle
qu'écrite : elle ne fixe ni le modèle, ni le nul, ni la grille, ni le nombre d'essais (constat 02).

## Réponses aux questions de la consigne

**Option (A) de P-021, niveau réel sous le nul, vrai rééchantillonnage** (U1 ; R = 2 000 essais par case, B = 1 000
tirages par grappes, mêmes tirages pour les trois juges et les cinq familles d'un corpus ; témoins appariés par la
`regle_temoins` de la configuration brouillon 3 ; corpus B : 30 items ; erreur de Monte-Carlo ≈ 0,004 à 0,005 pour un
taux de 0,03 à 0,05, ≈ 0,006 à 0,011 au-delà). Taux de « établie » aux deux lectures (règle du brouillon 6) ; entre
parenthèses, la lecture calibrée seule.

| scénario (nul : même gain vrai chez les trois juges) | C-P3a, k = 3 (45 / 60 tâches) | C-P3a, k = 5 (45 / 60) | C-P3b, k = 3 | C-P3b, k = 5 | C-P3c, 4 év. (k = 3 / 5, 45 tâches) |
|---|---|---|---|---|---|
| N0 aucune attaque, modèle S | 0,036 / 0,035 | 0,042 / 0,033 | 0,043 / 0,046 | 0,048 / 0,038 | 0,053 / 0,046 |
| N1 même attaque (g 0,10), S | 0,025 / 0,024 | 0,018 / 0,022 | 0,032 / 0,041 | 0,035 / 0,035 | 0,042 / 0,041 |
| N2 même attaque, S, erreurs différentes | 0,023 / 0,019 | 0,012 / 0,014 | 0,035 / 0,038 | 0,035 / 0,038 | 0,030 / 0,027 |
| N3 même attaque, D, κ 0,04 / 0,10 / 0,16 | 0,018 / 0,019 (cal. seule 0,067 / 0,078) | 0,023 / 0,018 (0,071 / 0,073) | 0,040 / 0,040 (0,071 / 0,064) | 0,036 / 0,030 (0,074 / 0,070) | 0,026 / 0,019 |
| N4 mécanismes différents d'un juge à l'autre, g 0,10 | 0,045 / 0,046 | 0,057 / 0,059 | 0,048 / 0,051 | 0,059 / 0,058 | 0,042 / 0,040 |
| **N5 comme N4, g 0,20** | **0,081 / 0,105** | **0,099 / 0,136** | **0,070 / 0,086** | **0,122 / 0,125** | 0,044 / 0,043 |

- La valeur p exacte seule dépasse son niveau partout (0,056 à 0,172 dans N0 à N3 ; 0,088 à 0,119 sans attaque ;
  davantage dans N4 et N5), comme T2 l'avait montré. Dans toutes les cases, le taux de la conjonction « exact et centré » est égal à celui du centré seul : la loi
  exacte ne mord jamais ; elle ne coûte rien non plus (constat 05).
- C-P3c à trois évaluateurs (sans P-020, W = 1), aux deux lectures : 0,011 à 0,037 dans toutes les cases.
- Puissance (S, gains vrais 0,07 / 0,10 / 0,13 entre juges, scénario P3) aux deux lectures : C-P3a 0,338 et 0,436
  (k = 3 ; 45 et 60 tâches), 0,451 et 0,571 (k = 5) ; C-P3b 0,342, 0,378, 0,522, 0,566 ; ± 0,011. Écarts 0,04 / 0,10 /
  0,16 (P6) : C-P3a 0,850 à 0,958, C-P3b 0,905 à 0,979. Les centrés seuls à 45 tâches (0,444 et 0,576 à la lecture
  calibrée) retrouvent T2c (0,448 et 0,657, 400 essais). La puissance de C-P3c n'est pas informative dans mon modèle
  (ses deux gains d'écart y sont du bruit pur).

**Clause de repli mécanique** : non applicable telle qu'écrite (constat 02). Lue au plus strict (modèle S de T1 et T2 ;
modèles S et D de T3 appliqués aux trois juges ensemble), elle ne se déclenche pour aucune règle : maximum 0,053 ± 0,005
(C-P3c, N0), sous 0,05 + 2 × 0,005. Lue comme couvrant les modèles S et D de T3 juge par juge, elle se déclenche pour
C-P3a et C-P3b (N5) et, à k = 5, aux limites pour N4 (0,059 ± 0,005).

**Lecture conjointe de C-P1 (CL5-01)** (U2 ; un juge, cinq familles, k = 3, 15 couples par essai, sans Holm ni
condition de famille positive, la lecture la plus sévère pour le niveau ; R = 1 000, B = 1 000) :

| modèle (frontière λ = 0,5) | calibrée : cible / moyenne | sans calibrage : cible / moyenne | **conjointe** : cible / moyenne |
|---|---|---|---|
| S, σ 0,4, g 0,10, 45 tâches (test du module) | 0,014 / 0,024 | 0,027 / 0,015 | 0,014 / 0,015 |
| D, κ 0,16, g 0,10, 45 tâches (test du module) | 0,003 / **0,071** | 0,017 / 0,023 | 0,003 / 0,023 |
| S, σ 0,4, 60 tâches | 0,020 / 0,024 | 0,038 / 0,013 | 0,020 / 0,013 |
| D, κ 0,16, 60 tâches | 0,004 / **0,086** | 0,020 / 0,026 | 0,004 / 0,026 |
| S, σ 0,6, g 0,20, 60 tâches | 0,026 / 0,027 | **0,117** / 0,004 | 0,026 / 0,004 |
| D, κ 0,16, g 0,20, 60 tâches | 0,001 / **0,243** | 0,028 / 0,028 | 0,001 / 0,028 |
| mélange dans un juge (s₀ 0,4 ; κ 0,08), g 0,10, 45 tâches | 0,006 / 0,044 | 0,026 / 0,014 | 0,006 / 0,014 |
| mélange dans un juge (s₀ 0,5 ; κ 0,16), g 0,20, 60 tâches | 0,001 / **0,235** | **0,128** / 0,003 | 0,001 / 0,003 |

Erreurs de Monte-Carlo 0,000 à 0,004. Puissance à λ = 1, g 0,10, 45 tâches : 0,826 (S) et 0,609 (D), égale à celle de la
lecture calibrée seule. La règle tient dans tous les modèles, y compris le mélange dans un même juge : la lecture
calibrée vaut (1 − κ) λ et la lecture sans calibrage λ / a (a = var(T) / (var(T) + s₀²)) ; elles encadrent toujours λ.
Le test du module tel qu'écrit ne voit pas une implémentation qui oublierait le calibrage (constat 03).

## Constats

### CB6-methode-courte-01 — majeur — « Deux lectures » : pas de protection quand les juges n'ont pas le même modèle d'erreur

- **Où** : bloc P-021, paragraphe « Deux lectures » (Prédiction, l. 554 à 557) ; Critères de lecture, l. 1262 et 1263 ;
  Seuil, C-P3a, C-P3b, C-P3c (l. 841 à 844) ; réserve 15 (l. 1195 à 1198) ; configuration `stabilite_rang.deux_lectures`.
- **Ce qui est.** Le texte étend aux statistiques de rang la règle conjointe de C-P1, « non simulée ». Sous un modèle
  d'erreur commun à tous les juges, elle protège (N2, N3). Mais chaque juge a son propre facteur : sans calibrage, Ḡ vaut
  a_j g ; calibré, g / (1 − κ_j). Si un juge a surtout une erreur sur v₀ (a_j < 1, κ_j = 0) et un autre surtout une
  compression (a = 1, κ > 0), les deux lectures placent le second au-dessus du premier, dans toutes les familles et dans
  les deux corpus. Ce facteur propre au juge suffit à produire une stabilité de rang qui n'existe pas. Le rapport du
  brouillon 5 le disait déjà par argument (CL5-01 : « des κ_j différents ordonnent les juges partout (C-P3a) ») ;
  l'extension ne le couvre pas.
- **Preuve** : U1, scénarios N4 et N5 (juge 1 : erreur sur v₀ d'écart type 0,6 ; juge 2 : erreur 0,4 et compression
  0,08 ; juge 3 : compression 0,16). À g = 0,20, aux deux lectures : C-P3a 0,081 à 0,136, C-P3b 0,070 à 0,125
  (`sorties_u1/u1_N5_k3_T45.txt`, `d7a020b2…` ; `u1_N5_k5_T60.txt`, `2fc8bfec…`). À g = 0,10 : 0,045 à 0,059. Le biais
  croît avec g, donc avec l'effet que HC1 prédit. C-P3c tient (0,040 à 0,047) : deux évaluateurs seulement portent Ḡ.
- **Ce qui devrait être.** Une lecture juste sous le modèle d'erreur de chaque juge. Le diagnostic r̂ du point 8 bis la
  donne. Sous le modèle général (erreur s₀ sur v₀, compression κ), ρ̂ = (1 − κ) a et r̂ = 1 − κ, donc ρ̂ / r̂ = a :
  calibrer par ρ̂/r̂ retire l'atténuation sans ajouter l'inflation, sous S (r̂ = 1), sous D (r̂ = ρ̂) et sous leur mélange.
  Vérifié (U3, R = 1 000, B = 1 000, ρ̂ et r̂ recalculés dans chaque tirage) : ρ̂/r̂ médian 0,843 / 0,924 / 1,000 pour des
  valeurs vraies de 0,84 / 0,92 / 1. Aux trois lectures, C-P3a vaut 0,008 à 0,025 et C-P3b 0,019 à 0,043 dans N1, N2, N3,
  N4 et N5 (± 0,003 à 0,006 ; `sorties_u3/u3_N5_k5_T60.txt`, `93b70c6d…`). La lecture ρ̂/r̂ seule vaut 0,024 à 0,065.
  Puissance (P3, 45 tâches) : C-P3a 0,318 (k = 3) et 0,422 (k = 5), contre 0,334 et 0,451 aux deux lectures ; C-P3b 0,307
  et 0,510, contre 0,329 et 0,532.
- **Correction (mots exacts).** C'est un changement du contenu de l'option (A) de P-021, encore en attente :
  la session le transmet comme correction de P-021 avant son défaut, par une ligne nouvelle du registre (R12), comme
  P-021 a remplacé P-019. Si la correction n'est pas retenue, la clause de repli réécrite (constat 02) s'applique :
  C-P3a et C-P3b rapportées sans verdict.
  1. Bloc P-021, remplacer le paragraphe « **Deux lectures.** Pour leurs composantes en Ḡ (C-P3a ; C-P3b ; Ḡ nets des
     familles 1 et 4 dans C-P3c), les trois statistiques sont calculées sur la loi nette calibrée et sur la loi nette sans
     calibrage (ρ = 1, mêmes tirages) ; « établie » seulement si les deux lectures concluent (extension aux statistiques de
     rang de la règle conjointe de C-P1 ; réserve 15 ; non simulée, d'où la clause qui suit). » par : « **Trois
     lectures.** Pour leurs composantes en Ḡ (C-P3a ; C-P3b ; Ḡ nets des familles 1 et 4 dans C-P3c), les trois
     statistiques sont calculées sur la loi nette calibrée, sur la loi nette sans calibrage (ρ = 1) et sur la loi nette
     calibrée par ρ̂/r̂ (X_i = v̄₀ + (ρ̂/r̂)(v₀_i − v̄₀), ρ̂/r̂ borné à [0,05 ; 1], ρ̂ et r̂ du point 8 bis recalculés dans
     chaque tirage), mêmes tirages ; « établie » seulement si les trois lectures concluent. Les deux premières ne
     suffisent pas quand les juges n'ont pas le même modèle d'erreur : sans écart vrai, elles ordonnent alors les juges
     dans le même sens (vérification courte de méthode du brouillon 6, U1 : C-P3a 0,081 à 0,136 et C-P3b 0,070 à 0,125
     sous le nul à g = 0,20) ; la troisième est juste sous l'erreur sur v₀, sous la compression et sous leur mélange
     (U3 : 0,008 à 0,043 aux trois lectures ; réserve 15). »
  2. Critères de lecture, remplacer « Les trois, pour leurs composantes en Ḡ, aux deux lectures de la loi nette
     (calibrée ; sans calibrage, ρ = 1) : « établie » seulement si les deux concluent ; » par « Les trois, pour leurs
     composantes en Ḡ, aux trois lectures de la loi nette (calibrée ; sans calibrage, ρ = 1 ; calibrée par ρ̂/r̂) :
     « établie » seulement si les trois concluent ; ».
  3. Seuil, ligne C-P3a, C-P3b, C-P3c : « deux lectures de la loi nette » devient « trois lectures de la loi nette (bloc
     P-021) ». En-tête « Ce que change le brouillon 6 » : « les trois aux deux lectures de la loi nette » devient « les
     trois aux trois lectures de la loi nette (calibrée, sans calibrage, calibrée par ρ̂/r̂) ».
  4. Réserve 15, ajouter : « Sous le modèle général (erreur sur v₀ et compression), ρ̂ = (1 − κ) a et r̂ = 1 − κ :
     ρ̂/r̂ estime a, l'atténuation seule. Pour C-P1, les lectures calibrée et sans calibrage encadrent λ dans ce modèle
     (U2) ; pour les statistiques de rang, qui comparent des juges dont les modèles peuvent différer, la lecture par
     ρ̂/r̂ est ajoutée (bloc P-021). La correction suppose une compression linéaire vers le milieu de l'échelle ; une
     autre forme n'est pas couverte. »
  5. Configuration, `stabilite_rang` : remplacer la clé `deux_lectures` par `trois_lectures` : « pour leurs composantes
     en Ḡ, C-P3a, C-P3b et C-P3c sont calculées sur la loi nette calibrée, sur la loi nette sans calibrage (rho = 1) et
     sur la loi nette calibrée par rho/r (rho/r borné à [0,05 ; 1], recalculé dans chaque tirage), mêmes tirages ;
     « établie » seulement si les trois lectures concluent » ; `lecture_recommandee` : « aux deux lectures » devient
     « aux trois lectures » ; `etape2.loi_nette`, ajouter `"lecture_rho_sur_r": "X = v0bar + (rho/r)(v0 - v0bar), rho/r
     borné à [0,05 ; 1], recalculé dans chaque tirage ; statistiques de rang seulement"`.
  6. Point 8 bis, test du module, ajouter : « Statistiques de rang, trois lectures : scénario où les juges ont des
     modèles d'erreur différents (erreur sur v₀ d'écart type 0,6 ; erreur 0,4 et compression 0,08 ; compression 0,16),
     même gain vrai g = 0,20, k = 5, 60 tâches, 1 000 essais : C-P3a et C-P3b « établie » au plus 0,06 chacun ; aux deux
     premières lectures seules, au-dessus de 0,10 (contrôle de l'artefact). »

### CB6-methode-courte-02 — majeur — Clause de repli : non mécanique telle qu'écrite

- **Où** : bloc P-021, « Clause de repli mécanique » (l. 559 à 562) ; configuration `stabilite_rang.clause_repli` ;
  registre, ligne P-021.
- **Ce qui est.** « un niveau réel sous le nul au-dessus de 0,05 plus deux erreurs de Monte-Carlo, dans le modèle de la
  contre-lecture méthode du brouillon 5 rejoué avec un vrai rééchantillonnage ». Restent ouverts : (a) « le modèle » : la
  contre-lecture du brouillon 5 en a plusieurs (S de T1 et T2 ; S et D de T3, chacun pour un juge ; T2d sans données) ;
  le cas qui fait échouer la règle (constat 01) combine S et D d'un juge à l'autre ; (b) « le nul » des statistiques de
  rang : avec ou sans attaque, et à quel g ; (c) la grille (k, nombre de tâches, σ, κ) et la règle de lecture sur cette
  grille (une case suffit-elle ?) ; (d) le nombre d'essais, donc l'erreur de Monte-Carlo, et le taux où elle se calcule
  (observé ou 0,05) ; (e) « l'une de ces règles » : la conjonction aux deux lectures, ou une lecture seule ? La lecture
  calibrée seule dépasse sous N3 (0,067 à 0,078) alors que la conjonction tient. Selon la lecture choisie, mes résultats
  déclenchent la clause pour C-P3a et C-P3b, ou ne la déclenchent pour rien.
- **Correction (mots exacts).** Remplacer la clause par : « **Clause de repli mécanique.** Si la vérification courte de
  méthode d'avant le scellement (sous-agent neuf ; contre-lecture 8) trouve, pour C-P3a, C-P3b ou C-P3c telle qu'écrite
  (toutes ses lectures jointes), un taux de « établie » au-dessus de 0,05 + 2 × √(0,05 × 0,95 / R) (R essais de la case,
  au moins 1 000) dans au moins une case de la grille qui suit, cette statistique est rapportée sans verdict, écrit tel
  quel, sans nouveau nœud. Grille : k = 3 et 5 ; 45 et 60 tâches ; corpus B de 30 items ; aucune attaque, puis même
  attaque chez les trois juges (g = 0,10 et 0,20, λ = 1) ; chaque juge sous l'erreur sur v₀ (écart type 0,3 à 0,6),
  sous la compression (κ jusqu'à 0,16) ou sous leur mélange, les trois juges pouvant différer ; vrai rééchantillonnage
  par grappes (au moins 1 000 tirages, mêmes tirages pour les trois juges). Résultat cité avec le chemin et l'empreinte
  du rapport. » Même texte dans `stabilite_rang.clause_repli`.
  Application à ce rapport : au texte actuel (deux lectures), la clause réécrite se déclenche pour C-P3a et C-P3b
  (N5 ; 0,05 + 2 × 0,0049 = 0,060) et pas pour C-P3c (maximum 0,053 ± 0,005). Avec la correction du constat 01, elle ne
  se déclenche pour aucune (U3, cases N1 à N5 couvertes : 0,043 ± 0,006 au plus ; cases N0 et le détail de N2 et N3 couverts
  seulement par U1 : à refaire en entier par la contre-lecture qui suit le brouillon 7, si le constat 01 est appliqué).

### CB6-methode-courte-03 — mineur — Test du module de la règle conjointe de C-P1 : il ne voit pas un calibrage oublié

- **Où** : point 8 bis, phrase « Règle conjointe de C-P1, à la frontière λ = 0,5, g = 0,10, 45 tâches, 300 essais, sous
  les deux modèles (…) : « vers la cible » et « vers la moyenne » au plus 0,05 chacun. »
- **Ce qui est.** La règle juste passe (U2 : 0,015 / 0,023 au plus). Mais une implémentation qui ne garderait que la
  lecture sans calibrage passe aussi (0,027 / 0,015 sous S ; 0,017 / 0,023 sous D). Une implémentation qui ne garderait
  que la lecture calibrée échoue sous D (0,071 ± 0,002 par couple), mais à 300 essais elle peut passer. L'unité du taux
  (couple, famille, avec ou sans Holm) n'est pas dite. R5 demande un essai sur artefact.
- **Correction (mots exacts).** Après « au plus 0,05 chacun », ajouter : « (taux par couple juge × famille, sans Holm) ;
  contrôles de l'artefact, 60 tâches, g = 0,20, 300 essais : sous le modèle v₀ exact et compression κ = 0,16, la
  lecture calibrée seule donne « vers la moyenne » au-dessus de 0,10 ; sous le modèle erreur sur v₀ d'écart type 0,6,
  la lecture sans calibrage seule donne « vers la cible » au-dessus de 0,08 ; la règle conjointe reste au plus 0,05 dans
  les deux (vérification courte de méthode du brouillon 6, U2 : 0,243, 0,117, puis 0,028 au plus) ».

### CB6-methode-courte-04 — majeur (processus) — La contre-lecture 8 décrite au texte couvre plus que cette vérification

- **Où** : verrou 6 (l. 184 à 188) ; projet, section 6.3, point 1 (v) à (viii).
- **Ce qui est.** Le texte annonce que la contre-lecture 8 couvre aussi C-P4b sur l'excédent des deux côtés, les moitiés
  par tâches et leur mise à l'échelle, l'ajout aux « Combinaisons » sur ĉ brut, et le style des deux plaidoyers sous la
  différence des différences. Ma consigne limite ma lentille à CL5-01 à CL5-03. Ces quatre points ne sont pas vérifiés ici.
- **Correction.** Session : confier les points (v) à (viii) à un sous-agent neuf avant le scellement, ou écrire au
  verrou 6 : « contre-lecture 8 : vérification courte de méthode de CL5-01 à CL5-03 (rapport `<<CHEMIN_RAPPORT_CL8>>`) ;
  points (v) à (viii) du projet, section 6.3 : contre-lecture `<<…>>` ».

### CB6-methode-courte-05 — information — Loi exacte de C-P3a : elle ne mord jamais

Dans les 32 cases de U1, le taux de « établie » de la conjonction est égal à celui du rééchantillonnage centré seul, à
chaque lecture. La valeur p exacte seule dépasse son niveau (0,056 à 0,172 dans N0 à N3). La garder ne coûte rien et ne protège de
rien ; aucune correction demandée.

### CB6-methode-courte-06 — forme — Deux précisions d'écriture

- C-P3b, colonne « établie » : la formule de la valeur p n'est pas écrite. Ajouter : « p = (1 + #{τ* ≥ τ}) / (B + 1) ».
- Configuration `stabilite_rang.C_P3a` : « valeur p exacte (7 776 affectations) ; et valeur p par rééchantillonnage
  centré (…) ≤ 0,05 » ne dit pas le seuil de la valeur p exacte. Écrire : « valeur p exacte (7 776 affectations) ≤ 0,05 ;
  et valeur p par rééchantillonnage centré (…) ≤ 0,05 ».

### CB6-methode-courte-07 — information — Ce qui tient (R4, symétrie)

- C-P3a corrigée : 0,012 à 0,042 aux deux lectures sous le nul dans le modèle de la contre-lecture du brouillon 5
  (N0 à N3), k = 3 et 5, 45 et 60 tâches, avec un vrai rééchantillonnage (le 0,062 de T2c à k = 3 venait de 400 essais : 0,038 à 0,040 ici, à
  2 000 essais). C-P3b corrigée, avec un vrai rééchantillonnage (tâches pour A, items pour B) au lieu de la loi des erreurs
  connue : 0,030 à 0,048 aux deux lectures. C-P3c, aux deux lectures : 0,019 à 0,053 à quatre évaluateurs,
  0,011 à 0,032 à trois.
- La règle conjointe de C-P1 : juste sous S, D et leur mélange dans un même juge, sans perte de puissance par rapport à
  la lecture calibrée seule.

## Simulations (dossier `simulations/`, manifeste `sha256sums-simulations-methode-courte-b6-v1.txt`, `368f3ec8…`)

| script | objet | sorties |
|---|---|---|
| `commun_cb6_v1.py` (`592d69d9…`) | modèle général (s₀, σ, κ par juge), appariement de la configuration brouillon 3, C-P3a, C-P3b, C-P3c ; importe sans les modifier `commun_b5_v1.py` et `t2_…py` du brouillon 5 | — |
| `u1_rang_vrai_reechantillonnage_v1.py` (`2bd74646…`) | option (A) de P-021, 8 scénarios × k × tâches, R = 2 000, B = 1 000 | `sorties_u1/` (32 fichiers) |
| `u2_regle_conjointe_CP1_v1.py` (`fcc9839a…`) | règle conjointe de C-P1, test du module, artefacts, mélange dans un juge, puissance ; R = 1 000 | `sorties_u2/` (10 fichiers) |
| `u3_lecture_rho_sur_r_v1.py` (`9cd78cee…`) | troisième lecture ρ̂/r̂ (correction du constat 01) ; R = 1 000 | `sorties_u3/` (12 fichiers) |

**Réserves sur mes simulations (R4).** Modèles jouets : lois normales, deux contenus par tâche, compression linéaire
vers le milieu de l'échelle, gains égaux d'un juge à l'autre sous le nul, profil de famille fixe. B = 1 000 au lieu de
10 000. Les formulations retenues (indices 1, 8, 16 ou 1, 4, 8, 12, 16) sont une hypothèse ; le partage réel des témoins
dépendra du choix au pilote. Corpus B simulé (30 items, moyenne 4,5, écart type 1,4) : le corpus réel n'a pas été lu.
Pour C-P3c, les deux gains d'écart sont du bruit pur, sans facteur propre au juge : si ces gains portent aussi un tel
facteur, C-P3c peut être touchée ; non simulé. U3 ne couvre pas toute la grille du constat 02 (N0 absent ; N2 et N3 sur
une case chacun). Les erreurs de Monte-Carlo de U2 sont calculées entre essais sur la moyenne de 15 couples corrélés.
