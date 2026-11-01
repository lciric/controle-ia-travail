# Gel de la conception v5 — arène « mélange d'équilibre » — écrit AVANT tout calcul de la v5 (racines, diagnostic de la pureté, règle de choix de la variante, condition testable et garde, règles nouvelles, prédictions)

Rédacteur neuf Opus 5.5 (lignée conv-audit), 1er novembre 2026, relevé `date -u` : 2026-11-01T09:14:23Z juste avant l'écriture. Il n'a écrit aucun des brouillons 1 à 4, aucun des codes v1 à v4, aucune contre-lecture ni la vérification courte de ce pilote.

Ce fichier est écrit **avant** toute ligne de code v5, tout essai v5, tout diagnostic, tout pilote v5 et toute simulation v5. Il ne sera jamais rouvert. Le code v5 épinglera son empreinte et refusera de partir en mode diagnostic, essai, audit d'essai ou témoin si ce fichier manque, a changé, ou ne cite pas la racine demandée.

**Seules lectures faites avant ce gel** (déclarées) : les pièces v1 à v4 (textes, codes, journaux) ; la vérification courte `verification-arene-melange-v4-brouillon4.md` (`28ab322f…`) ; les décisions R-739, R-1031, R-1034 ; la question `question-convergence-defense-unique-v1.md` ; **les temps processeur par bras** du pilote v4 (`essai-pilote-arene-melange-v4-detection.json`, champs `cpu_trajectoire_s`, `cpu_final_s`, `cpu_tache_s` ; pour budgéter le calcul) — A 0,8 + 1,1 s, B 1,2 + 3,0 s, C1 5,2 s, C2 5,3 s, C3 4,8 s, D 5,7 + 6,1 s, B′ 7,1 + 8,1 s, C3′ 12,2 s, tâche 60,7 s. Aucune autre valeur du pilote v4 n'a été recalculée.

## 0. Nature des changements (déclarée)

Brouillon 5 écrit **après** la vérification courte du brouillon 4 (« gelable après corrections » : CM4-01 majeur, CM4-02 et CM4-03 moyens, CM4-04 à CM4-09 mineurs) et **après** la décision de Lazar du 1er novembre, 08:37 UTC (R-1034, point 5) : « go réécriture et correction » — à classe de fonctions égale, B′ s'effondre sur un seul moniteur (poids purs dans 58 à 71 % des tâches), pureté imposée par le jeu ; le jeu ne permet pas de distinguer « le tirage au hasard est inutile » de « la classe est en cause ». Tout ce qui suit est postérieur aux pilotes v3 et v4 ; rien ne lit une racine de décision. La question au collisionneur (`question-convergence-defense-unique-v1.md`, question 4) porte sur le même point : ce gel n'en préjuge pas la réponse ; si elle arrive, elle sera comparée à ce qui suit, sans changer aucune règle gelée ici.

## 1. Racines

### 1.1 Racines neuves de la v5 (toutes dans 20264001 à 20264999, bornes exclues ; aucune n'apparaît dans le dépôt hors de ce fichier, recherche faite à 09:10 UTC hors `donnees/` et hors `arene-extension-familles-v1/`)

| Racine | Usage (unique) |
|---|---|
| 20264601 / 20264602 | diagnostic de la pureté : échelle de classes, instances 0 à 15, deux δ (racine principale / racine des familles tenues) |
| 20264611 | jeux témoins à équilibre intérieur connu (contrôle préalable de chaque lancement, essais compris) |
| 20264621 / 20264622 | pilote v5 (24 instances × 2 δ) et audit d'essai v5 sur des tâches de ce pilote |
| 20264631 / 20264632 | réservées : reprise du pilote v5 seulement si une erreur de code oblige à le rejouer (non employées sauf déclaration au journal) |
| 20264641 / 20264642 | essais du code v5 et mesures de temps |
| 20264643 | essais du code v5 : « une autre racine change le résultat » |
| 20264651 | simulations du calcul de puissance v5 (décision rééchantillonnée, bandes S10, critère d'audit, P10, table de temps) |

Décision inchangée : **RACINE = 20261201, RACINE_TENUE = 20261202**, jamais employées hors décision autorisée par un préenregistrement scellé.

### 1.2 Racines refusées par garde en v5 (relevé complet des v1 à v4)

- toutes celles refusées en v4 : 20261101 ; 20261291 à 20261298 ; 20261301 ; 20261311 à 20261316 ; 20262291, 20262297, 20262313 ; 20269501, 20269502 ; 20269731, 20269732 ; 20269741, 20269742 ;
- **toutes les racines gelées de la v4** : 20264101, 20264102 (recalibrage) ; 20264201, 20264202 (pilote et audit d'essai v4) ; 20264211, 20264212 (réservées v4, non employées mais nommées) ; 20264301, 20264302, 20264303 (essais v4) ; 20264401 (puissance v4) ;
- les valeurs nommées par les essais v4 comme racines « non gelées » : 20264555, 20264777 ; les bornes de plage 20264001 et 20264999 ;
- **toute racine de 20265001 à 20265999** (plage d'une autre session) ;
- toute racine hors décision qui n'est pas listée au § 1.1.

Les graines personnelles de la vérification courte (« hors de toute racine du dépôt ») ne sont pas connues : non refusables nommément, déclaré.

## 2. Diagnostic de la pureté (point 1 de la consigne), protocole écrit avant tout calcul

**Hypothèse de mécanisme (avant calcul)** : la pureté de B′ vient de la **couverture** : un maxout à 9 unités entraîné contre la stratégie d'équilibre q de l'attaquant détecte à la fois toutes les attaques du support de q, parce que l'attaquant est attaché à K = 3 directions fixes (les composantes de la loi cible, contrainte de comportement δ) et qu'une seule fonction de la classe couvre ces directions avec un coût de seuil faible (croissance logarithmique du seuil d'un « ou ») ; le jeu complet (classe × attaques atteignables) a alors un point-selle dans la classe, et le jeu restreint aussi. Hypothèses concurrentes nommées : (b) quasi-égalités bruitées entre moniteurs « généralistes » (la pureté forcée tiendrait au bruit d'échantillonnage de G) ; (c) troncature à T = 8 et nombre de moniteurs passés ; (d) solveur ou projection sur le simplexe (déjà écartée en v4 : pureté forcée 17/17 et 14/14 ; re-vérifiée ici par les jeux témoins, § 3).

**Calcul** (code v5, mode `diagnostic`, racine 20264601 / 20264602, instances 0 à 15, δ = (1,4 ; 1,6), mode léger : trajectoires, puis meilleures réponses finales standard et renforcée) : bras A et B (classe linéaire u = 1 : B est le mélange, A la défense unique de même classe), puis pour chaque u de l'**échelle U = (2, 3, 5, 9)** : **B_u** (double oracle dont l'oracle rend des maxouts à u unités, code de bras 10), **D_u** (un seul maxout à u unités, réentraîné à chaque tour contre le mélange uniforme de toutes les attaques passées : A = D_1 ; code 11), **M_u** (« mode » : le moniteur de poids maximal de B_u déployé seul ; code 13). Mêmes codes de bras pour tous les u (nombres aléatoires communs entre u, déclaré).

**Mesures par tâche et par u** (toutes descriptives) : poids finaux de B_u ; pur (poids ≥ 1 − 10⁻⁹) ; plus petit poids maximal parmi les stratégies d'équilibre du défenseur du jeu restreint final (tolérance 10⁻⁹ : « pureté forcée » si ≥ 1 − 10⁻⁶) ; même quantité pour les ε-équilibres, ε ∈ {0,002 ; 0,005 ; 0,01} (fragilité de la pureté au bruit de G, hypothèse b) ; **gain du mélange dans le jeu restreint** = valeur du jeu − meilleur minimum de ligne pure ; dominance faible de la ligne de poids maximal (G[i*, j] ≥ G[i, j] − 0,005 pour toute ligne i et toute colonne j) ; poids maximal de p à chaque tour (pureté selon le nombre de moniteurs passés, hypothèse c) ; V(B_u), V(D_u), V(M_u).

**Règle de choix de la variante (écrite avant tout calcul ; seules les statistiques de pureté y entrent, aucune valeur de V ni aucun contraste)** : f_u(δ) = part des tâches où la pureté de B_u est forcée ; r_u(δ) = part des tâches où les poids de B_u sont purs. **u\* = le plus grand u de U tel que f_u(δ) ≤ 0,25 et r_u(δ) ≤ 0,5 aux deux δ.** Si aucun u de U ne satisfait la règle : u\* = 1 ; Q2 se confond alors avec la Table 1 (B contre A) ; le brouillon 5 propose de retirer Q2 (décision à Lazar, format décision), sans autre choix à la main. Après le diagnostic, **une seule ligne change** dans le code v5 : `UNITES_Q2_V5 = None` devient `UNITES_Q2_V5 = u*` ; les empreintes du code avant et après sont consignées au journal.

## 3. Condition testable « la pureté n'est pas imposée par le jeu » et garde R5

**Jeux témoins à équilibre intérieur connu (racine 20264611)** : loi propre N(0, I₆) ; M = 3 « modes » d'attaque : lois dont les K = 3 composantes ont la même moyenne r·v_m (r = 4, écarts-types 1), v_m = (cos 2πm/3, sin 2πm/3, 0, 0, 0, 0) (triangle équilatéral centré à l'origine). L'attaquant choisit un mode (meilleure réponse discrète : le mode de plus faible détection de la défense mixte courante, sur échantillons frais) ; le défenseur emploie l'oracle `entrainer` du code (« détection », u unités) contre la stratégie d'équilibre q de l'attaquant ; double oracle à partir d'un moniteur entraîné contre le mode 0 ; T = 6 tours ; matrice G sur échantillons frais ; programme linéaire `resoudre_jeu` ; `poids_max_min_equilibres`.

Faits analytiques (avant calcul) :
- **témoin sain (classe linéaire, u = 1)** : pour tout moniteur linéaire, Σ_m w·(r v_m) = 0, donc au moins un mode a w·μ ≤ 0 et une détection ≤ α (en population) : **aucun équilibre pur** ; le mélange uniforme des trois spécialistes vaut v\* = [Φ(r − z) + 2 Φ(−r/2 − z)] / 3, z = Φ⁻¹(1 − α), soit **0,318** à r = 4, α = 0,01 ;
- **témoin artefact (u = 3)** : un seul maxout à 3 unités (unités le long des v_m) détecte chaque mode à ≈ Φ(r − Φ⁻¹(1 − α/3)) ≈ 0,90 ≫ v\* : **point-selle, pureté forcée par le jeu**.

**Condition C-T (le chemin de calcul sait trouver un équilibre intérieur), tolérances gelées** : sur le témoin sain, (i) meilleur minimum de ligne pure ≤ 3α (le témoin est bien sans point-selle) ; (ii) poids finaux : poids maximal ≤ 0,5 et support ≥ 2 ; (iii) |valeur du jeu restreint − v\*| ≤ 0,05 ; (iv) pureté non forcée (plus petit poids maximal parmi les équilibres < 1 − 10⁻⁶). Sur le témoin artefact : la pureté forcée **doit être détectée**.

**Garde R5** : `controle_temoins` (appelée au début des modes diagnostic, essai, audit d'essai, décision et audit) arrête tout lancement si C-T échoue sur le témoin sain, ou si le témoin artefact n'est pas reconnu dégénéré ; `exiger_jeu_non_degenere` arrête sur un jeu restreint à pureté forcée là où elle est appelée (témoins). Essais : cas sain (code réel) ; artefacts : solveur remplacé par un solveur qui rend un sommet pur ; témoin artefact ; témoin rendu dégénéré par construction (trois modes identiques).

**Condition C-J (le jeu de la variante retenue n'impose pas la pureté)** : au diagnostic, f_{u\*}(δ) ≤ 0,25 aux deux δ (c'est la règle du § 2) ; au pilote v5, f_{u\*}(δ) ≤ 0,5 aux deux δ, sinon écrit et la question devient « non exercée (jeu dégénéré) ». À la décision, la Table 7 garde la règle v4 (« non exercée » si les poids de B_u sont purs sur plus de la moitié des tâches d'un δ) et recopie f_{u\*}(δ) : « non exercée, pureté imposée par le jeu » si f > 0,5, « non exercée, pureté du sommet du solveur » sinon.

## 4. Règles nouvelles de la v5, fixées avant tout calcul

1. **Q2 reposée à la classe F_{u\*}** : « à classe de fonctions égale (maxouts à u\* unités), le mélange d'équilibre B_u bat-il D_u (défense unique réentraînée de même classe) et, à moniteurs égaux, C3′_u (« ou » déterministe des moniteurs de B_u) ? ». **M_u** (mode) est descriptif (B_u − M_u : le tirage seul, à moniteurs égaux contre le meilleur d'entre eux ; CM3-02, point 4). B′ et C3′ de la v4 (9 unités) **sortent de la décision** (leur non-exercice est l'objet du diagnostic) ; leur code reste, inchangé (essai de continuité).
2. Bras de la décision v5 : A, B, C1, C2, C3, D (inchangés : Q1, Tables 1, 2, 5), B_u, D_u, C3′_u, M_u. Codes de bras 10, 11, 12, 13.
3. **S10** : k = 4 d'emblée (CM4-03 ; k = 3 a échoué à 16 bandes en v4) sur les 18 bandes (9 bras × 2 δ, M_u exclu) ; repli fixé d'avance : k = 5 si le taux simulé de fausse alerte dépasse 0,05.
4. **S17** : bras audités A, B, C3, D, B_u, D_u, C3′_u ; contrastes audités B − A, B − C3, B − D, B_u − D_u, B_u − C3′_u ; critère inchangé (m/2 = 0,01 ou changement de classe démontré à t(K − 1 ; 0,995)) ; repli inchangé (t(K − 1 ; 0,9995)). Audit d'essai v5 sur les instances 0 à 4 du pilote v5, aux deux δ.
5. **Table de temps (CM4-01)**, méthode fixée avant calcul : temps processeur par tâche du pilote v5 ; 20 000 tirages de 2N tâches avec remise (racine 20264651) ; mur = somme / (2 e) + plus longue tâche / e ; probabilité d'arrêt sur la garde = P(mur > délai), pour N ∈ {100, 80, 60}, délai ∈ {9 000 ; 12 600 ; 14 400 s}, e ∈ {0,51 ; 0,52} (mesurées sur machine partagée) et e ∈ {0,60 ; 0,67 ; 0,80 ; 0,90 ; 1,00}, plus un mélange à poids égaux des efficacités mesurées (pilote v3 0,80 ; pilote v4 0,52 ; audit v4 0,51 ; diagnostic, pilote et audit v5 mesurés ici). **Combinaison proposée** : la plus grande N dont la probabilité d'arrêt à e = 0,51 est ≤ 0,01 avec un délai de la liste, le plus court délai à égalité ; présentée au format décision (Lazar, ou conv-audit par délégation R-739). Probabilités des classes simulées aussi à N = 80 et N = 60. Même méthode pour le délai de l'audit (20 tâches).
6. **CM4-02** : la condition de lancement (charge < 0,5) est réécrite comme réduisant le risque sans l'éliminer ; conséquence d'un dépassement : « non concluant », une seule reprise complète. **CM4-03 à CM4-09** : corrections de texte (S10 k = 4 ; S8 de l'audit dans les listes ; précision sur le commit `f65feb1a` et R-1031 ; bornes de P10 sans hypothèse d'indépendance ; compagnon du brouillon 4 à créer par conv-audit ; essais sains hors de l'essai nommé ; arbre git propre avec d'autres sessions).
7. Rien d'autre ne change dans A, B, C1, C2, C3, D, B′, C3′ : même calcul, mêmes graines par bras (essai de continuité contre la v4, champ à champ sur une même racine). N = 100 et S18 = 0,10 restent ceux de R-739 tant que Lazar ne décide pas autrement.

## 5. Prédictions écrites avant tout calcul (confiance entre parenthèses)

**Diagnostic** (racine 20264601) :
| Quantité | Prédiction | Branche opposée |
|---|---|---|
| f_9 (pureté forcée de B_9) | > 0,5 à au moins un δ (0,75) | ≤ 0,5 aux deux δ |
| f_5 | > 0,25 à au moins un δ (0,6) | ≤ 0,25 aux deux δ |
| f_3 | > 0,25 à au moins un δ (0,5) | ≤ 0,25 aux deux δ |
| f_2 | ≤ 0,25 aux deux δ (0,6) | > 0,25 à un δ |
| r_u (part pure) croissante de u = 1 à u = 9 à chaque δ (au sens large) | (0,6) | non monotone |
| gain du mélange dans le jeu restreint, moyen, décroissant de u = 1 à u = 9 | (0,6) | non monotone |
| fragilité : parmi les tâches pures de B_9, part dont le plus petit poids maximal des 0,005-équilibres est < 0,9 | ≥ 0,5 (0,5) | < 0,5 |
| B_u − D_u (descriptif) | > +0,01 à u = 2 aux deux δ (0,55) ; \|·\| < 0,02 à u = 9 (0,8) | |
| B_u − M_u (descriptif) | \|·\| < 0,01 à u = 9 (0,8) ; > 0 à u = 2 (0,55) | |
| u\* | 2 (0,45) ; 3 (0,25) ; 5 (0,1) ; aucun, donc 1 (0,2) | |

**Jeux témoins** : sain : C-T tenue (0,9) ; artefact : pureté forcée détectée (0,85).

**Pilote v5** (racine 20264621, à u\*) : part pure de B_u ≤ 0,5 aux deux δ (0,7) ; f_{u\*} ≤ 0,5 aux deux δ (0,75) ; B_u − D_u > 0 aux deux δ (0,55) ; B_u − C3′_u : signe non prédit (0,5) ; Q1 : B − C3 et B − D < 0 (0,9), B − A > 0 (0,9) ; A : borne basse B2 de I3 − 0,7345 > 0 aux deux δ (0,7) ; temps par tâche (10 bras) 35 à 75 s (0,6) ; efficacité mesurée ≥ 0,85 si la charge est < 0,5 au lancement et qu'aucun autre calcul ne tourne (0,6). Audit d'essai v5 : aucun drapeau (i) (0,85). S10 à k = 4 : fausse alerte ≤ 0,05 (0,7). Critère d'audit : fausse alerte ≤ 0,05 (0,7).

## 6. Après le diagnostic et après le pilote v5

Aucune modification des règles fixées ici, hors la ligne `UNITES_Q2_V5` (§ 2) et les replis écrits d'avance (§ 4.3, § 4.4). Toute correction de code révélée par les essais, le diagnostic ou le pilote est consignée au journal avec sa raison et sa nouvelle empreinte ; une correction qui change un résultat du pilote oblige à le rejouer sur la racine réservée 20264631 / 20264632. Si u\* = 1, aucun pilote v5 n'est lancé à u = 1 sans décision de Lazar : le brouillon 5 présente alors la proposition de retrait de Q2.
