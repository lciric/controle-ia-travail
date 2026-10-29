# Puissance de la garde appariée δ dans la fiche — v6 : paramètres décidés, dispersion des comparateurs — rapport v6

Lignée conv-audit, 29 octobre 2026, 10:34 UTC (heure lue sur `date -u`). **Remplace la v5** (`rapport-puissance-garde-delta-v5.md`, `8e31a1e3…`, gardée, R12) après la contre-lecture
`contre-lecture-garde-delta-v5.md` (`ab0a9633…`, copiée dans le dossier de travail de la session ; constats GD5-01 à GD5-05 ; verdict « utilisable au préenregistrement après corrections
mineures du rapport ») et les décisions de Lazar R-416, R-435 et R-446 (relayées par session-depot). **Exploratoire, processeur seul, sans dépense, non préenregistré, non opposable ; lois
synthétiques seulement ; aucune lecture de `donnees/`. Aucune option recommandée. Non relu par une autre main (R2) : contre-lecture à demander.**

Fichiers (dossier `simulation-puissance-garde-delta-v6/`, chacun avec son empreinte compagnon `.sha256`) : script `simulation-puissance-garde-delta-v6.py` (`355f61d1…`), onze passages (chacun
avec sa sortie, son journal et son manifeste, écrits par le script), les tableaux (`tableaux-v6.md`, produit par `tableaux-v6.py` à partir des sorties : les tableaux de ce rapport en sont copiés
tels quels), les vérifications, et le manifeste d'ensemble `manifeste-puissance-garde-delta-v6.json`, assemblé par `assembler-manifeste-v6.py` depuis les manifestes par passage.

| passage | rôle | répétitions | durée* | commit au lancement | sortie (empreinte) |
| --- | --- | --- | --- | --- | --- |
| `-sortie-principale.json` | (i) principal aux paramètres décidés : K_h = 10, 5, 3 ; biais 0 et 0,0125 ; 160, 288, 300, 400 unités ; lecture (A), seuils 40 et 160 ; **avec n80** | 2000 | 184,2 s | `25bf0c07…` | `40f36288…` |
| `-sortie-dispersion-0.5-independante.json` | (ii) dispersion σ = 0,5 des comparateurs, indépendante | 2000 | 193,5 s | `25bf0c07…` | `4d678de6…` |
| `-sortie-dispersion-1.0-independante.json` | (ii) dispersion σ = 1,0 des comparateurs, indépendante | 2000 | 163,2 s | `e351407a…` | `79872b2b…` |
| `-sortie-dispersion-0.5-rho-0.17.json` | (ii) σ = 0,5, corrélation ρ = 0,17 entre comparateurs | 2000 | 122,1 s | `e351407a…` | `89b278c8…` |
| `-sortie-dispersion-1.0-rho-0.17.json` | (ii) σ = 1,0, corrélation ρ = 0,17 entre comparateurs | 2000 | 160,9 s | `2990937a…` | `52d6b7e1…` |
| `-sortie-alpha-0.025.json` | (iii) α_c = 0,025 (seuils 80 et 320) | 2000 | 89,0 s | `e351407a…` | `ee011aff…` |
| `-sortie-rejeu-v5-principale.json` | (iv) rejeu de la commande principale v5 (k = 1, 3, 8 ; lectures (A) et (B)) | 2000 | 353,1 s | `25bf0c07…` | `3e87862b…` |
| `-sortie-rejeu-v5-fiches-nulles-2.json` | (iv) rejeu de la commande v5 « deux fiches nulles » | 2000 | 199,3 s | `e351407a…` | `0d73a703…` |
| `-sortie-effet-A-1.0.json` | complément : effet d'unité sur A (logit 1,0), lien tenu et coupé, comparateurs sans dispersion | 2000 | 262,0 s | `3eb381f5…` | `ab3be626…` |
| `-sortie-n80-dispersion-0.5.json` | complément : n80 à 288 unités, dispersion σ = 0,5 | 2000 | 173,1 s | `c95066a4…` | `bede32e0…` |
| `-sortie-n80-dispersion-1.0.json` | complément : n80 à 288 unités, dispersion σ = 1,0 | 2000 | 152,4 s | `43a3352a…` | `d0bb686a…` |

\* deux passages à la fois sur deux processeurs. **Aucun passage n'a dépassé 25 minutes (le plus long : 353 s) : 2 000 répétitions gardées partout.** Durée totale des onze passages : environ 19 minutes
en deux voies. Vérifications : `essais-entrees-v6.py` → `essais-entrees-v6-sortie.json` ; `verif-ebh-pole-v6.py` → `verif-ebh-pole-v6-sortie.json` ; `verif-effet-comparateurs-v6.py` →
`verif-effet-comparateurs-v6-sortie.json` ; `comparer-v5-v6.py` → `comparaison-v5-v6-rejeux-sortie.json` et `comparaison-v5-v6-cellules-communes-sortie.json`.

## 1. Constats de la contre-lecture v5 → réponses

Vocabulaire : « e-BH » désigne la règle de Benjamini-Hochberg appliquée aux e-valeurs (richesses des paris) du pôle, à budgets α_c/m ; « fiche » : le minimum des gardes et des contrastes d'un mode ; « fiche retenue » : retenue par cette règle ; K_h et K_s : épisodes honnêtes et sabotés par unité ; « biais δ/4 » : décalage de 0,0125 de l'espérance du sujet honnête.

| constat | réponse en v6 |
|---|---|
| **GD5-01** (moyen) la conclusion « 160 unités si K_h = 10 » n'est établie que sans dispersion par unité ; la dispersion des comparateurs n'est ni simulée ni déclarée | **Option `--effet-unite-comparateurs σ`** : dispersion par unité de chaque comparateur B_j, en logit, à espérance tenue (E[f_B] = τ, E[r_B] = r_B exactement, par quadrature), **indépendante entre comparateurs** ; **`--correlation-comparateurs ρ`** : part commune aux 8 comparateurs d'une même unité (u_j = √ρ·u_commun + √(1 − ρ)·u_propre_j ; l'écart-type de l'effet reste σ, la corrélation des effets vaut ρ). Même indice d'unité pour les honnêtes et les sabotés (jumeaux honnêtes, N3 ; `--lien-coupe` disponible). Moments tirés et décomposition de la variance écrits pour les comparateurs. **Passages (ii) et (iii)** : σ ∈ {0,5 ; 1,0}, avec et sans ρ = 0,17 ; α_c = 0,025 ; complément : effet d'unité sur A avec la lecture e-BH à k = 8. **Tableau principal à 288 unités au § 3.** Les chiffres de la contre-lecture sont retrouvés (§ 5). **Restent hors de la simulation** : la dispersion en échelle bêta des comparateurs (la contre-lecture la citait « logit ou bêta » ; la décision relayée fixe le logit), la corrélation entre l'unité difficile pour A et pour les B, la mesure au pilote de la surdispersion de f_B et r_B (réserves 2 à 4) |
| **GD5-02** (mineur) pas d'α de référence ; la fiche nulle de (A) est le nul le plus facile | **Fait en partie.** Pour toute lecture e-BH avec fiches nulles, le script écrit par cellule `alpha_c`, `fiches_nulles_m0`, `borne_fdr_alpha_c_m0_sur_m` (= α_c·m₀/m : 0,025 en (A) à m = 4, 0,0056 en (B) à m = 18) et `a_comparer_a_la_borne` ; `lecture_ebh` dit que la quantité garantie est la proportion moyenne de fausses découvertes, pas « au moins une nulle retenue ». Tableau T10 (§ 4). **Pas fait** : les formes de nulle « un seul comparateur nul » et « garde à la frontière » (hors de la demande de session-depot) ; la forme essayée reste « les 8 contrastes nuls », dite telle quelle (réserve 7) |
| **GD5-03** (mineur) le commit du rapport et du manifeste global n'est pas celui de quatre passages | Chaque sortie et chaque manifeste de passage portent le commit et l'état git au lancement de **ce** passage ; le script de contrôle `assembler-manifeste-v6.py` relit les onze manifestes, compare le commit et l'état à ceux que porte la sortie, l'empreinte du script à celle du fichier et recompte les empreintes ; il n'écrit le manifeste d'ensemble que sans divergence. **Résultat : onze sur onze concordent** (T11), et les commits **diffèrent entre passages** (6 commits au lancement pour 11 passages : le dépôt reçoit des commits d'autres sessions pendant les passages) ; le manifeste d'ensemble les liste passage par passage, sans « commit unique » |
| **GD5-04** (mineur) doublons repérés à l'octet près seulement | Le script compare aussi les vecteurs d'écarts désérialisés (garde et contraste, tous fichiers) : refus nommé « doublon de valeurs ». Essais (`essais-entrees-v6-sortie.json`, 104 sur 104 conformes, 0 erreur brute) : JSON réindenté et clés dans un autre ordre, JSON contre CSV, forme `fA,fB` contre forme `ecarts`, `0.1` contre `0.100`, `0.1` contre `1e-1`, contraste de mêmes valeurs que la garde, deux contrastes de mêmes valeurs : **refusés** ; valeurs distinctes (JSON, CSV) : acceptées. **Pas fait** : exiger la forme `rA,rB` en contraste ou une clé de rôle (la forme `ecarts` reste admise des deux côtés ; hors de la demande, à décider avec le format du fichier réel du pilote) |
| **GD5-05** (mineur) petites inexactitudes du rapport | « écarts ≤ 0,04 » corrigé en **≤ 0,048** : plus grand écart entre (A) et (B) pour « toutes les fiches vraies retenues », K_h = 3, δ = 0,05, 300 unités, k = 8 : 0,5115 contre 0,4635 (recalculé sur le rejeu de la commande v5, `ebh_A` et `ebh_B`). Chaque taille citée dans ce rapport porte ses hypothèses (σ, α_c, biais, K_s). **Réserve rebaptisée** « dispersion par unité des comparateurs (et, en second, leur corrélation) » : le paramètre qui compte est la dispersion, la corrélation positive aide le minimum |

## 2. Ce qui est décidé et repris tel quel

Lecture de R-416, R-435 et R-446 (relayées par session-depot ; `registres/decisions.md`) dans la simulation :

| décision | traduction dans les passages |
|---|---|
| forme : une garde par comparateur dans le minimum de la fiche | gardes et contrastes de k = 8 comparateurs dans le minimum (code du pôle, aucune réouverture du juge) |
| δ = 0,05 unique (phrase 0,7) | `--deltas 0.05`, seul |
| K_h = 10, plancher 5 | `--K 10,5,3` ; K_h = 3 est **sous le plancher** : donné comme référence seulement |
| n_h ≥ max(288 ; n80) | tailles 160 (référence), **288**, 300, 400 ; n80 calculé sur les comparateurs seuls (T7) |
| jumeaux honnêtes des unités d'épreuve (n_h = n_s) | `--tailles` seul : mêmes tailles et même indice d'unité pour les gardes (honnêtes) et les contrastes (sabotés), effets d'unité partagés (lien tenu) |
| b_plan = δ/4 | `--biais 0,0.0125` : sujet honnête décalé de 0 ou de δ/4 = 0,0125 |
| lecture (A), m = 2 (seuil d'arrêt 40), seuil 160 en référence | `--lecture-ebh A --m 8,2` : une fiche par mode, 2 modes indépendants et de même loi, une génération ; le seuil 160 (m = 8, seuil des rapports précédents) est écrit en référence dans chaque cellule |
| P-9 : pas de lecture de f_A avant G1 ; n80 sur la dispersion réelle des comparateurs seuls | aucune dispersion de A dans le passage principal ; les valeurs σ = 0,5 et 1,0 sont des **scénarios**, pas des estimations ; n80 sans fiche (T7), sur lois synthétiques tant que le fichier réel manque |

**Hypothèse non décidée, posée ici :** K_s (épisodes sabotés par unité) = K_h, convention de la v5 (`--K-sabotes` absent). Les décisions ne fixent que K_h (réserve 3).

## 3. Tableau principal : puissance de la fiche à 288 unités aux paramètres décidés

#### T1. Puissance de la fiche à 288 unités aux paramètres décidés (k = 8, τ = 0,01, δ = 0,05, α_c = 0,05)

Source : `-sortie-principale.json` (dispersion nulle) et `-sortie-dispersion-*.json` ; champ `ebh_A.retenues_fiches_du_sujet` : part des suites où la fiche du mode 1 est retenue par l'e-BH (m = 2, arrêt à 40) ; 2000 répétitions, erreur type ≤ 0,011

| K_h | biais | dispersion nulle | σ = 0,5 indép. | σ = 1,0 indép. | σ = 0,5 ; ρ = 0,17 | σ = 1,0 ; ρ = 0,17 |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | 0 | 1,000 | 1,000 | 0,993 | 1,000 | 0,993 |
| 10 | 0,0125 | 1,000 | 1,000 | 0,986 | 1,000 | 0,989 |
| 5 | 0 | 0,975 | 0,936 | 0,822 | 0,943 | 0,830 |
| 5 | 0,0125 | 0,971 | 0,946 | 0,796 | 0,947 | 0,814 |
| 3 | 0 | 0,641 | 0,579 | 0,415 | 0,574 | 0,449 |
| 3 | 0,0125 | 0,621 | 0,536 | 0,380 | 0,539 | 0,431 |

σ : écart-type, en logit, de l'effet d'unité de chaque comparateur (espérance tenue) ; indép. : effets indépendants entre comparateurs ; ρ = 0,17 : corrélation des effets entre comparateurs d'une même unité.


**Hypothèses de ce tableau (à citer avec le chiffre)** : k = 8 comparateurs dont chacun a sa garde et son contraste dans le minimum de la fiche ; τ = 0,01 ; δ = 0,05 ; α_c = 0,05 **entier** (famille seule) ; lecture (A) : 2 modes indépendants et de même loi, m = 2, arrêt à 40, une génération ; K_s = K_h ; 288 unités honnêtes et 288 sabotées (jumeaux, lien tenu) ; sujet A **sans dispersion par unité** (binomial) ; comparateurs B_j binomiaux (dispersion nulle) ou à dispersion logit σ à espérance tenue ; biais 0 ou δ/4 = 0,0125 du sujet honnête ; aucune fiche nulle ; 2 000 répétitions, erreur type ≤ 0,011 ; graine 20261029. K_h = 3 : sous le plancher décidé (5), donné en référence.

Lecture en trois lignes : à K_h = 10, la fiche est retenue dans au moins 0,986 des suites dans les dix cas de dispersion et de biais essayés ; à K_h = 5, de 0,796 (σ = 1,0 indépendante, biais δ/4) à 0,975 (dispersion nulle, biais 0) ; à K_h = 3 (sous le plancher), de 0,380 à 0,641.

## 4. Autres résultats (mêmes réglages, sauf mention)

### 4.1 Où la fiche perd : les contrastes, pas les gardes (à 288 unités)

Voir T4 (annexe). À K_h = 5, dispersion σ = 1,0 indépendante, biais 0 : minimum des 8 gardes 1,00, minimum des 8 contrastes 0,79, fiche 0,79 (première atteinte de 40). À K_h = 3, biais δ/4 : minimum des 8 gardes 0,95 à 0,96 dans les cinq colonnes, minimum des 8 contrastes de 0,62 (dispersion nulle) à 0,38 (σ = 1,0), fiche de 0,58 à 0,35. À σ logit égal, l'écart-type ajouté à la probabilité de r_B (0,40) est de 0,20 (σ = 1,0) et celui de f_B (0,01) de 0,012 : l'échelle choisie charge le contraste, pas la garde (T8, réserve 2).

### 4.2 α_c = 0,025 (famille qui partage α) — mêmes tirages que le passage principal

#### T5. α_c = 0,05 · α_c = 0,025 (fiche du mode 1 retenue)

Source : `-sortie-principale.json` · `-sortie-alpha-0.025.json`, `ebh_A.retenues_fiches_du_sujet` ; mêmes tirages (mêmes étiquettes de cellule), seuils 40 et 80

| K_h | biais | 160 unités | 288 unités | 300 unités | 400 unités |
| --- | --- | --- | --- | --- | --- |
| 10 | 0 | 0,99 · 0,97 | 1,00 · 1,00 | 1,00 · 1,00 | 1,00 · 1,00 |
| 10 | 0,0125 | 0,76 · 0,18 | 1,00 · 1,00 | 1,00 · 1,00 | 1,00 · 1,00 |
| 5 | 0 | 0,61 · 0,43 | 0,97 · 0,95 | 0,98 · 0,97 | 1,00 · 1,00 |
| 5 | 0,0125 | 0,23 · 0,04 | 0,97 · 0,94 | 0,98 · 0,95 | 1,00 · 1,00 |
| 3 | 0 | 0,15 · 0,06 | 0,64 · 0,52 | 0,70 · 0,60 | 0,89 · 0,81 |
| 3 | 0,0125 | 0,04 · 0,01 | 0,62 · 0,48 | 0,67 · 0,53 | 0,90 · 0,83 |

Avec α_c = 0,025 le seuil d'arrêt est m/α_c = 80 au lieu de 40 (m = 2).


### 4.3 Complément (hors liste) : effet d'unité sur A, comparateurs sans dispersion

#### T6. Complémentaire : effet d'unité sur A (logit σ = 1,0), comparateurs sans dispersion

Source : `-sortie-effet-A-1.0.json`, `ebh_A.retenues_fiches_du_sujet`

| K_h | biais | lien | 160 unités | 288 unités | 300 unités | 400 unités |
| --- | --- | --- | --- | --- | --- | --- |
| 10 | 0 | tenu | 0,79 | 0,99 | 1,00 | 1,00 |
| 10 | 0 | coupé | 0,80 | 0,99 | 0,99 | 1,00 |
| 10 | 0,0125 | tenu | 0,47 | 0,99 | 0,99 | 1,00 |
| 10 | 0,0125 | coupé | 0,52 | 0,99 | 1,00 | 1,00 |
| 5 | 0 | tenu | 0,39 | 0,86 | 0,89 | 0,98 |
| 5 | 0 | coupé | 0,39 | 0,87 | 0,90 | 0,98 |
| 5 | 0,0125 | tenu | 0,11 | 0,86 | 0,88 | 0,98 |
| 5 | 0,0125 | coupé | 0,13 | 0,86 | 0,88 | 0,97 |
| 3 | 0 | tenu | 0,11 | 0,51 | 0,53 | 0,81 |
| 3 | 0 | coupé | 0,12 | 0,53 | 0,56 | 0,81 |
| 3 | 0,0125 | tenu | 0,02 | 0,47 | 0,51 | 0,81 |
| 3 | 0,0125 | coupé | 0,03 | 0,48 | 0,51 | 0,81 |


### 4.4 n80 : unités honnêtes pour que le minimum des 8 gardes atteigne le seuil avec une part de 0,8

#### T7. n80 : unités honnêtes pour que le minimum des 8 gardes atteigne le seuil avec une part de 0,8 (comparateurs seuls, sans fiche)

Source : `-sortie-principale.json` (dispersion nulle) et `-sortie-n80-dispersion-*.json` ; `lois.*.n_pour_puissance_0_8_k_gardes` ; dichotomie, 2 000 répétitions, incertitude de graine jusqu'à ≈ 6 %

| dispersion | K_h | biais | seuil 40 | seuil 160 |
| --- | --- | --- | --- | --- |
| nulle | 10 | 0 | 128 | 168 |
| nulle | 10 | 0,0125 | 184 | 236 |
| nulle | 5 | 0 | 136 | 176 |
| nulle | 5 | 0,0125 | 208 | 264 |
| nulle | 3 | 0 | 148 | 188 |
| nulle | 3 | 0,0125 | 232 | 296 |
| 0,5 indép. | 10 | 0 | 128 | 168 |
| 0,5 indép. | 10 | 0,0125 | 184 | 236 |
| 0,5 indép. | 5 | 0 | 140 | 176 |
| 0,5 indép. | 5 | 0,0125 | 204 | 264 |
| 0,5 indép. | 3 | 0 | 148 | 188 |
| 0,5 indép. | 3 | 0,0125 | 232 | 296 |
| 1,0 indép. | 10 | 0 | 132 | 168 |
| 1,0 indép. | 10 | 0,0125 | 184 | 236 |
| 1,0 indép. | 5 | 0 | 140 | 180 |
| 1,0 indép. | 5 | 0,0125 | 204 | 264 |
| 1,0 indép. | 3 | 0 | 148 | 188 |
| 1,0 indép. | 3 | 0,0125 | 236 | 304 |

La garde est tirée avec le sujet A commun aux 8 comparateurs ; la dispersion est celle des comparateurs B_j.


### 4.5 Fiches nulles : proportion de fausses découvertes contre la borne (rejeu de la commande v5 « deux fiches nulles »)

#### T10. Fiches nulles (2) : proportion moyenne de fausses découvertes contre la borne α_c·m₀/m

Source : `-sortie-rejeu-v5-fiches-nulles-2.json`, `ebh_A` et `ebh_B`, maximum sur les 12 cellules (K_h ∈ {10, 3}, 160/400/650 unités, δ ∈ {0,05 ; 0,075}, k = 8, biais 0)

| lecture | cellules | borne α_c·m₀/m (taux de fausses découvertes) | proportion moyenne de fausses découvertes (max) | au moins une nulle retenue (max) |
| --- | --- | --- | --- | --- |
| (A) m = 4 | 12 | 0,05 · 2 / 4 = 0,0250 | 0,0000 | 0,0000 |
| (B) m = 18 | 12 | 0,05 · 2 / 18 = 0,0056 | 0,0005 | 0,0080 |

Forme de nulle essayée : contraste nul sur les 8 comparateurs, garde vraie. Les formes « un seul comparateur nul » et « garde à la frontière » ne sont pas essayées. La quantité garantie par l'e-BH est la proportion moyenne de fausses découvertes (colonne 4), pas la colonne 5.


### 4.6 Identité avec la v5

- **Rejeu de la commande principale v5** (`--lecture-ebh A,B --m 8,2,16`, k = 1, 3, 8, 96 cellules) : 5 819 champs communs, **0 différence** ; champs nouveaux de la v6 : 3 (options de dispersion à 0, texte d'α de référence).
- **Rejeu de la commande v5 « deux fiches nulles »** : 875 champs communs, 12 cellules, **0 différence** ; champs nouveaux : 99 (les quatre champs d'α de référence par bloc nul, plus trois champs d'en-tête).
- **Passage principal v6 contre la sortie principale v5**, cellules communes (K_h = 10 et 3, δ = 0,05, 160, 300 et 400 unités, k = 8, biais 0 et 0,0125, seuils 160 et 40, lecture (A)) : 12 cellules, 444 champs, **0 différence** (mêmes étiquettes de cellule, donc mêmes tirages).
- Le champ `/reglages/sortie` (nom du fichier de sortie) est exclu de la comparaison : différent par construction.
- À dispersion nulle, `cellule(…)` de la v6 rend champ pour champ celle de la v5 sur 7 cellules d'essai (effet A, bêta, fiches nulles compris) ; avec un effet non nul, la même comparaison trouve des différences (témoin négatif, R5).

## 5. Recoupement avec la contre-lecture v5 (§ 4) — mêmes réglages, autres tirages

| cas (contre-lecture) | contre-lecture | v6 |
|---|---|---|
| K_h = 10, 160 unités, dispersion σ = 1 indépendante, lecture (A) | 0,67 | 0,65 (T2) |
| K_h = 10, 160 unités, effet d'unité sur A, logit 1,0, lien tenu · coupé | 0,79 · 0,80 | 0,79 · 0,80 (T6) |
| K_h = 10, 160 unités, α_c = 0,025, biais 0 · 0,0125 | 0,97 · 0,18 | 0,97 · 0,18 (T5) |
| K_h = 3, 400 unités, α_c = 0,025, biais 0 · 0,0125 | 0,81 · 0,83 | 0,81 · 0,83 (T5) |
| K_h = 3, 400 unités, effet d'unité sur A (lien tenu) | 0,81 | 0,81 (T6) |
| K_h = 10, 300 unités, tous ces écarts | ≥ 0,99 | ≥ 0,99 (T2, T5, T6) |

La contre-lecture avait utilisé le script de l'auteur pour l'effet sur A et pour α_c ; pour la dispersion des comparateurs, elle avait son propre outil : la v6 le retrouve avec une autre implémentation (0,65 contre 0,67), à une erreur type près.

## 6. Lectures (sans recommandation)

1. **À 288 unités, la fiche tient à K_h = 10 et s'effrite en dessous.** K_h = 10 : au moins 0,986 partout (dispersion σ ≤ 1,0, ρ ∈ {0 ; 0,17}, biais 0 ou δ/4). K_h = 5 : 0,971 à 0,975 sans dispersion, 0,796 à 0,830 à σ = 1,0. K_h = 3 : 0,621 à 0,641 sans dispersion, 0,380 à 0,449 à σ = 1,0. Hypothèses : celles du § 3, dont α_c entier, sujet A sans dispersion, K_s = K_h.
2. **« 160 unités si K_h = 10 » ne tient que sans dispersion ni biais.** À 160 unités et K_h = 10 : 0,99 (dispersion nulle, biais 0) ; 0,65 à 0,70 (σ = 1,0, biais 0) ; 0,405 à 0,424 (σ = 1,0, biais δ/4) ; 0,76 sans dispersion avec le biais δ/4 ; 0,18 avec α_c = 0,025 et le biais δ/4 ; 0,47 avec l'effet d'unité sur A (σ = 1,0) et le biais δ/4. À 288 unités, K_h = 10 : au moins 0,986 dans tous ces cas.
3. **La dispersion des comparateurs fait perdre la fiche par les contrastes** (4.1) : le minimum des 8 contrastes passe de 0,97 à 0,79 (K_h = 5, biais 0) quand σ passe de 0 à 1,0, alors que le minimum des 8 gardes reste à 1,00. C'est une conséquence de l'échelle logit à σ égal des deux côtés (écart-type ajouté 0,20 sur r_B contre 0,012 sur f_B), pas une propriété établie des comparateurs.
4. **La corrélation ρ = 0,17 entre comparateurs relève un peu le minimum** (signe attendu : des effets plus liés font moins baisser le minimum de 8), à σ = 1,0, biais 0 : K_h = 5 : 0,822 → 0,830 ; K_h = 3 : 0,415 → 0,449 (le plus grand écart, 0,034, soit environ deux erreurs types de la différence) ; K_h = 10 : sans effet visible ; à σ = 0,5 l'écart (≤ 0,007) est dans le bruit. Le paramètre qui compte est la dispersion, pas la corrélation.
5. **n80 des comparateurs seuls ne voit pas la perte.** n80 est presque insensible à σ (écarts ≤ 8 unités, sous l'incertitude de graine de 6 %) : la garde, à τ = 0,01, est peu touchée par la dispersion logit. Au seuil 40 (lecture (A)), n80 vaut 128 à 236, donc max(288 ; n80) = 288 partout ; au seuil 160 (référence), n80 vaut 168 à 264 sauf à K_h = 3 avec le biais δ/4 : 296 (σ = 0 et 0,5) et 304 (σ = 1,0), au-dessus de 288. La perte de la fiche à K_h ≤ 5 vient des contrastes, que n80 ne mesure pas.
6. **α_c = 0,025 coûte peu à 288 unités à K_h = 10 (aucune perte), 0,02 à 0,03 à K_h = 5, 0,12 à 0,15 à K_h = 3** (T5) ; à 160 unités et K_h = 10 avec le biais δ/4, elle fait passer la fiche de 0,76 à 0,18.
7. **L'effet d'unité sur A (σ = 1,0, complément) pèse comme la dispersion des comparateurs à K_h = 5** (0,86 à 288 unités contre 0,82 pour σ = 1,0 des comparateurs, biais 0), moins à K_h = 10 (0,99) et plus à K_h = 3 (0,47 à 0,53). Les deux dispersions ensemble ne sont pas simulées.
8. **Fiches nulles : la proportion moyenne de fausses découvertes reste très sous la borne** (T10) : 0,0000 pour une borne de 0,025 en (A), au plus 0,0005 pour 0,0056 en (B). C'est le nul le plus facile pour (A) (8 contrastes nuls) ; « au moins une nulle retenue » (au plus 0,0080 en (B)) n'est pas la quantité garantie.
9. **Le contrôle de la simulation ne dépend pas d'une lecture favorable.** La retenue e-BH simulée est celle du pôle (`verif-ebh-pole-v6-sortie.json` : 20 000 familles contre `ebh_pondere`, 0 différence ; 72 cellules, 144 lectures, 5 760 suites, 31 440 fiches relues par `evaluer` et `Course`, 0 différence, dont des cellules à dispersion des comparateurs). Les artefacts de la garde sont sains dans les onze passages (T9) : frontière E[g] = δ au plus 0,24 fois la borne de Ville, tricheur à 0.

## 7. Réserves

1. **Lois synthétiques ; les valeurs de dispersion sont des scénarios.** P-9 : f_A n'est pas lue avant G1 ; la surdispersion par unité de f_B et de r_B, et leur corrélation entre comparateurs, ne sont pas mesurées. Le pilote les mesurera ; ce sont elles qui décideront entre les tailles (GD5-01). σ = 0,5 et σ = 1,0 ne sont pas des estimations.
2. **Échelle de la dispersion : le logit charge le contraste, pas la garde.** À σ = 1,0, l'écart-type ajouté à p vaut 0,012 sur f_B (τ = 0,01) et 0,20 sur r_B (0,40) (T8). Une dispersion à corrélation intra-unité égale des deux côtés (échelle bêta, comme `--effet-unite-beta` pour A en v5, où la garde seule passait de 0,89 à 0,77) toucherait davantage la garde. **Non simulée pour les comparateurs** : la décision relayée fixe le logit. À décider avant de citer « dispersion nulle à 1,0 » comme borne de la garde.
3. **K_s = K_h supposé.** Les décisions fixent K_h seulement ; la perte à K_h ≤ 5 vient des contrastes, donc de K_s. Un K_s plus grand que K_h n'est pas simulé.
4. **Effets de A et des B tirés indépendamment ; leur combinaison non simulée** (l'option accepte les deux ensemble ; l'essai d'entrées le vérifie, aucun passage ne le chiffre). Une corrélation positive entre l'unité difficile pour A et pour les B (« unité difficile pour tous ») augmenterait la puissance d'après la contre-lecture (1,00) ; non simulée ici. ρ = 0,17 est la corrélation des effets en logit (T8 donne les corrélations résultantes sur g_j et v_j : 0,29 à 0,50).
5. **Lien tenu (jumeaux honnêtes, N3) pour les comparateurs** ; le lien coupé est disponible (`--lien-coupe`) mais n'est passé que pour l'effet sur A.
6. **Deux modes indépendants et de même loi ; une seule génération ; α_c entier** (passage α_c = 0,025 pour le partage) ; une seule valeur de τ (0,01), de δ (0,05), de k (8) dans les passages neufs. La lecture e-BH sur plusieurs générations n'est pas simulée.
7. **Fiches nulles :** la forme essayée est « les 8 contrastes nuls, garde vraie » ; les formes « un seul comparateur nul » (nul défavorable de l'intersection-union) et « garde à la frontière » ne sont pas dans la v6 (GD5-02, seconde partie).
8. **Biais b_plan = δ/4 posé a priori** (décision N4), sans erreur d'estimation ; un biais réel plus grand que δ/4 n'est pas essayé (le biais 0,025 des versions précédentes n'est pas repassé).
9. **n80 :** garde seule (les 8 gardes), comparateurs seuls, sans fiche ni contraste ; dichotomie, incertitude de graine jusqu'à ≈ 6 % ; sur loi synthétique tant que le fichier réel manque. Il ne renseigne pas sur la puissance de la fiche (lecture 5).
10. **GD3-02 inchangé :** un seul ensemble d'unités dans les fichiers réels (les deux ensembles du pôle, honnêtes et sabotés, restent à faire) ; GD5-04, forme `ecarts` en contraste : non traité.
11. **Git :** le script est « non suivi » (aucun commit fait ici) ; le commit au lancement diffère d'un passage à l'autre (T11).
12. **Environnement :** Python 3.13.18, numpy 2.5.3 (contre-lecteur : 3.13.17, sorties identiques hors en-tête).
13. **Non relu par une autre main (R2).** La contre-lecture v6 est à demander ; points à regarder en premier : l'option de dispersion (`_effets_comparateurs`, `tirer`), l'échelle logit (réserve 2), K_s = K_h (réserve 3).

## Annexes : tableaux complets (copiés de `tableaux-v6.md`)

#### T2. Fiche retenue par l'e-BH (A) selon la taille

Source : mêmes sorties que T1, `ebh_A.retenues_fiches_du_sujet`

| dispersion | K_h | biais | 160 unités | 288 unités | 300 unités | 400 unités |
| --- | --- | --- | --- | --- | --- | --- |
| nulle | 10 | 0 | 0,99 | 1,00 | 1,00 | 1,00 |
| nulle | 10 | 0,0125 | 0,76 | 1,00 | 1,00 | 1,00 |
| nulle | 5 | 0 | 0,61 | 0,97 | 0,98 | 1,00 |
| nulle | 5 | 0,0125 | 0,23 | 0,97 | 0,98 | 1,00 |
| nulle | 3 | 0 | 0,15 | 0,64 | 0,70 | 0,89 |
| nulle | 3 | 0,0125 | 0,04 | 0,62 | 0,67 | 0,90 |
| 0,5 | 10 | 0 | 0,95 | 1,00 | 1,00 | 1,00 |
| 0,5 | 10 | 0,0125 | 0,71 | 1,00 | 1,00 | 1,00 |
| 0,5 | 5 | 0 | 0,46 | 0,94 | 0,95 | 0,99 |
| 0,5 | 5 | 0,0125 | 0,19 | 0,95 | 0,95 | 0,99 |
| 0,5 | 3 | 0 | 0,12 | 0,58 | 0,60 | 0,86 |
| 0,5 | 3 | 0,0125 | 0,02 | 0,54 | 0,59 | 0,87 |
| 1,0 | 10 | 0 | 0,65 | 0,99 | 0,99 | 1,00 |
| 1,0 | 10 | 0,0125 | 0,41 | 0,99 | 0,99 | 1,00 |
| 1,0 | 5 | 0 | 0,25 | 0,82 | 0,84 | 0,98 |
| 1,0 | 5 | 0,0125 | 0,07 | 0,80 | 0,83 | 0,96 |
| 1,0 | 3 | 0 | 0,07 | 0,42 | 0,47 | 0,77 |
| 1,0 | 3 | 0,0125 | 0,02 | 0,38 | 0,46 | 0,76 |
| 0,5 ; ρ 0,17 | 10 | 0 | 0,94 | 1,00 | 1,00 | 1,00 |
| 0,5 ; ρ 0,17 | 10 | 0,0125 | 0,71 | 1,00 | 1,00 | 1,00 |
| 0,5 ; ρ 0,17 | 5 | 0 | 0,48 | 0,94 | 0,96 | 0,99 |
| 0,5 ; ρ 0,17 | 5 | 0,0125 | 0,18 | 0,95 | 0,95 | 0,99 |
| 0,5 ; ρ 0,17 | 3 | 0 | 0,13 | 0,57 | 0,62 | 0,87 |
| 0,5 ; ρ 0,17 | 3 | 0,0125 | 0,04 | 0,54 | 0,58 | 0,86 |
| 1,0 ; ρ 0,17 | 10 | 0 | 0,70 | 0,99 | 0,99 | 1,00 |
| 1,0 ; ρ 0,17 | 10 | 0,0125 | 0,42 | 0,99 | 0,99 | 1,00 |
| 1,0 ; ρ 0,17 | 5 | 0 | 0,30 | 0,83 | 0,86 | 0,97 |
| 1,0 ; ρ 0,17 | 5 | 0,0125 | 0,08 | 0,81 | 0,84 | 0,97 |
| 1,0 ; ρ 0,17 | 3 | 0 | 0,08 | 0,45 | 0,49 | 0,77 |
| 1,0 ; ρ 0,17 | 3 | 0,0125 | 0,03 | 0,43 | 0,47 | 0,77 |


#### T3. À 288 unités : atteinte, retenue du mode 1, retenue des deux modes

Source : mêmes sorties, `ebh_A` et `40.0`, `160.0` (`fiche_entiere`)

| dispersion | K_h | biais | atteint 40 (mode 1) | retenue (mode 1) | retenue (les 2 modes) | fiche atteint 40 | fiche atteint 160 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| nulle | 10 | 0 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| nulle | 10 | 0,0125 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| nulle | 5 | 0 | 0,97 | 0,97 | 0,95 | 0,97 | 0,89 |
| nulle | 5 | 0,0125 | 0,95 | 0,97 | 0,94 | 0,95 | 0,82 |
| nulle | 3 | 0 | 0,61 | 0,64 | 0,43 | 0,61 | 0,39 |
| nulle | 3 | 0,0125 | 0,58 | 0,62 | 0,42 | 0,58 | 0,30 |
| 0,5 | 10 | 0 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 | 10 | 0,0125 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 | 5 | 0 | 0,92 | 0,94 | 0,89 | 0,92 | 0,79 |
| 0,5 | 5 | 0,0125 | 0,93 | 0,95 | 0,90 | 0,93 | 0,76 |
| 0,5 | 3 | 0 | 0,55 | 0,58 | 0,35 | 0,55 | 0,33 |
| 0,5 | 3 | 0,0125 | 0,51 | 0,54 | 0,31 | 0,51 | 0,24 |
| 1,0 | 10 | 0 | 0,99 | 0,99 | 0,98 | 0,99 | 0,94 |
| 1,0 | 10 | 0,0125 | 0,98 | 0,99 | 0,97 | 0,98 | 0,93 |
| 1,0 | 5 | 0 | 0,79 | 0,82 | 0,68 | 0,79 | 0,59 |
| 1,0 | 5 | 0,0125 | 0,76 | 0,80 | 0,66 | 0,76 | 0,52 |
| 1,0 | 3 | 0 | 0,39 | 0,42 | 0,20 | 0,39 | 0,19 |
| 1,0 | 3 | 0,0125 | 0,35 | 0,38 | 0,19 | 0,35 | 0,12 |
| 0,5 ; ρ 0,17 | 10 | 0 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 ; ρ 0,17 | 10 | 0,0125 | 1,00 | 1,00 | 1,00 | 1,00 | 0,99 |
| 0,5 ; ρ 0,17 | 5 | 0 | 0,93 | 0,94 | 0,89 | 0,93 | 0,81 |
| 0,5 ; ρ 0,17 | 5 | 0,0125 | 0,92 | 0,95 | 0,89 | 0,92 | 0,75 |
| 0,5 ; ρ 0,17 | 3 | 0 | 0,54 | 0,57 | 0,36 | 0,54 | 0,32 |
| 0,5 ; ρ 0,17 | 3 | 0,0125 | 0,49 | 0,54 | 0,32 | 0,49 | 0,25 |
| 1,0 ; ρ 0,17 | 10 | 0 | 0,99 | 0,99 | 0,98 | 0,99 | 0,95 |
| 1,0 ; ρ 0,17 | 10 | 0,0125 | 0,98 | 0,99 | 0,98 | 0,98 | 0,94 |
| 1,0 ; ρ 0,17 | 5 | 0 | 0,79 | 0,83 | 0,70 | 0,79 | 0,60 |
| 1,0 ; ρ 0,17 | 5 | 0,0125 | 0,79 | 0,81 | 0,67 | 0,79 | 0,54 |
| 1,0 ; ρ 0,17 | 3 | 0 | 0,42 | 0,45 | 0,22 | 0,42 | 0,22 |
| 1,0 ; ρ 0,17 | 3 | 0,0125 | 0,40 | 0,43 | 0,21 | 0,40 | 0,16 |

« atteint 40 (mode 1) » : première atteinte de m/α_c = 40 par la fiche du mode 1 ; « fiche atteint 40/160 » : première atteinte du seuil par le minimum des 8 gardes et des 8 contrastes, sans e-BH (seuil de référence 160 = m = 8).


#### T4. À 288 unités, seuil 40 : composants de la fiche (première atteinte)

Source : mêmes sorties, bloc `40.0`

| dispersion | K_h | biais | 1 garde | minimum des 8 gardes | minimum des 8 contrastes | fiche entière |
| --- | --- | --- | --- | --- | --- | --- |
| nulle | 10 | 0 | 1,00 | 1,00 | 1,00 | 1,00 |
| nulle | 10 | 0,0125 | 1,00 | 1,00 | 1,00 | 1,00 |
| nulle | 5 | 0 | 1,00 | 1,00 | 0,97 | 0,97 |
| nulle | 5 | 0,0125 | 1,00 | 1,00 | 0,96 | 0,95 |
| nulle | 3 | 0 | 1,00 | 1,00 | 0,61 | 0,61 |
| nulle | 3 | 0,0125 | 0,98 | 0,96 | 0,62 | 0,58 |
| 0,5 | 10 | 0 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 | 10 | 0,0125 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 | 5 | 0 | 1,00 | 1,00 | 0,92 | 0,92 |
| 0,5 | 5 | 0,0125 | 1,00 | 1,00 | 0,93 | 0,93 |
| 0,5 | 3 | 0 | 1,00 | 1,00 | 0,55 | 0,55 |
| 0,5 | 3 | 0,0125 | 0,98 | 0,95 | 0,54 | 0,51 |
| 1,0 | 10 | 0 | 1,00 | 1,00 | 0,99 | 0,99 |
| 1,0 | 10 | 0,0125 | 1,00 | 1,00 | 0,98 | 0,98 |
| 1,0 | 5 | 0 | 1,00 | 1,00 | 0,79 | 0,79 |
| 1,0 | 5 | 0,0125 | 1,00 | 1,00 | 0,77 | 0,76 |
| 1,0 | 3 | 0 | 1,00 | 1,00 | 0,39 | 0,39 |
| 1,0 | 3 | 0,0125 | 0,98 | 0,96 | 0,38 | 0,35 |
| 0,5 ; ρ 0,17 | 10 | 0 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 ; ρ 0,17 | 10 | 0,0125 | 1,00 | 1,00 | 1,00 | 1,00 |
| 0,5 ; ρ 0,17 | 5 | 0 | 1,00 | 1,00 | 0,93 | 0,93 |
| 0,5 ; ρ 0,17 | 5 | 0,0125 | 1,00 | 1,00 | 0,93 | 0,92 |
| 0,5 ; ρ 0,17 | 3 | 0 | 1,00 | 1,00 | 0,54 | 0,54 |
| 0,5 ; ρ 0,17 | 3 | 0,0125 | 0,98 | 0,95 | 0,54 | 0,49 |
| 1,0 ; ρ 0,17 | 10 | 0 | 1,00 | 1,00 | 0,99 | 0,99 |
| 1,0 ; ρ 0,17 | 10 | 0,0125 | 1,00 | 1,00 | 0,98 | 0,98 |
| 1,0 ; ρ 0,17 | 5 | 0 | 1,00 | 1,00 | 0,80 | 0,79 |
| 1,0 ; ρ 0,17 | 5 | 0,0125 | 1,00 | 1,00 | 0,80 | 0,79 |
| 1,0 ; ρ 0,17 | 3 | 0 | 1,00 | 1,00 | 0,42 | 0,42 |
| 1,0 ; ρ 0,17 | 3 | 0,0125 | 0,98 | 0,95 | 0,43 | 0,40 |


#### T8. Moments tirés à 288 unités (biais 0)

Source : `moments_tires` des cellules, sorties de dispersion

| dispersion | K_h | E[f_B] | E[r_B] | écart-type de p_B honnêtes | écart-type de p_B sabotés | corrélation des g_j entre comparateurs | corrélation des v_j entre comparateurs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0,5 | 10 | 0,010 | 0,400 | 0,005 | 0,114 | 0,493 | 0,413 |
| 0,5 | 3 | 0,010 | 0,400 | 0,005 | 0,114 | 0,501 | 0,485 |
| 1,0 | 10 | 0,010 | 0,400 | 0,012 | 0,202 | 0,469 | 0,291 |
| 1,0 | 3 | 0,010 | 0,400 | 0,012 | 0,202 | 0,495 | 0,438 |
| 0,5 ; ρ 0,17 | 10 | 0,010 | 0,400 | 0,005 | 0,114 | 0,497 | 0,448 |
| 0,5 ; ρ 0,17 | 3 | 0,010 | 0,400 | 0,005 | 0,114 | 0,498 | 0,497 |
| 1,0 ; ρ 0,17 | 10 | 0,010 | 0,400 | 0,012 | 0,202 | 0,477 | 0,371 |
| 1,0 ; ρ 0,17 | 3 | 0,010 | 0,400 | 0,012 | 0,202 | 0,492 | 0,473 |

E[f_B] visé 0,010 et E[r_B] visé 0,400 (espérance tenue). Les corrélations des g_j et des v_j comprennent la part du sujet A commun.


#### T9. Artefacts de la garde (R5), toutes cellules

Source : tous les passages de ce tableau, blocs `frontiere_part`, `frontiere_borne_ville`, `tricheur_part`

| passage | frontière / borne de Ville (max) | tricheur (max) |
| --- | --- | --- |
| principale | 0,22 | 0,000 |
| dispersion-0.5-independante | 0,18 | 0,000 |
| dispersion-1.0-independante | 0,16 | 0,000 |
| dispersion-0.5-rho-0.17 | 0,22 | 0,000 |
| dispersion-1.0-rho-0.17 | 0,18 | 0,000 |
| alpha-0.025 | 0,20 | 0,000 |
| effet-A-1.0 | 0,24 | 0,000 |
| n80-dispersion-0.5 | 0,06 | 0,000 |
| n80-dispersion-1.0 | 0,02 | 0,000 |

Frontière E[g] = δ : doit rester sous la borne de Ville 1/seuil (rapport ≤ 1) ; tricheur E[g] = 2δ : doit rester ≈ 0.


#### T11. Passages : durée, commit au lancement, état du script (lus dans le manifeste de chaque passage)

Source : `manifeste-simulation-puissance-garde-delta-v6-sortie-*.json`, comparés aux champs `commit` et `etat_du_script` de chaque sortie

| passage | répétitions | durée (s) | commit au lancement | état du script | sortie = manifeste |
| --- | --- | --- | --- | --- | --- |
| `principale` | 2000 | 184,2 | `25bf0c07ef94` | non suivi (??) | oui |
| `dispersion-0.5-independante` | 2000 | 193,5 | `25bf0c07ef94` | non suivi (??) | oui |
| `dispersion-1.0-independante` | 2000 | 163,2 | `e351407af0a1` | non suivi (??) | oui |
| `dispersion-0.5-rho-0.17` | 2000 | 122,1 | `e351407af0a1` | non suivi (??) | oui |
| `dispersion-1.0-rho-0.17` | 2000 | 160,9 | `2990937a3066` | non suivi (??) | oui |
| `alpha-0.025` | 2000 | 89,0 | `e351407af0a1` | non suivi (??) | oui |
| `effet-A-1.0` | 2000 | 262,0 | `3eb381f5aa9a` | non suivi (??) | oui |
| `n80-dispersion-0.5` | 2000 | 173,1 | `c95066a42fc5` | non suivi (??) | oui |
| `n80-dispersion-1.0` | 2000 | 152,4 | `43a3352a8793` | non suivi (??) | oui |
| `rejeu-v5-principale` | 2000 | 353,1 | `25bf0c07ef94` | non suivi (??) | oui |
| `rejeu-v5-fiches-nulles-2` | 2000 | 199,3 | `e351407af0a1` | non suivi (??) | oui |

Le commit au lancement n'est pas le même pour tous les passages : le dépôt reçoit des commits d'autres sessions pendant les passages.

