# Puissance de la garde appariée δ dans la fiche — v7 : dispersion en échelle bêta, K_s ≠ K_h — rapport v7

Lignée conv-audit, 29 octobre 2026, 12:24 UTC (heure lue sur `date -u`). **Complète la v6** (`rapport-puissance-garde-delta-v6.md`, `ae13d5be…`, gardée, R12) sur ses
réserves 2 et 3 (« doutes 1 et 2 » de la commande ; la réserve 4, combinaison des effets de A et des B, reste ouverte) ; **rien d'autre ne change**. **Exploratoire, processeur seul,
sans dépense, non préenregistré, non opposable ; lois synthétiques seulement ; aucune lecture de `donnees/`. Aucune option recommandée. Non relu par une autre main (R2) :
contre-lecture à demander.**

Fichiers (dossier `simulation-puissance-garde-delta-v7/`, chacun avec son empreinte compagnon `.sha256`) : script `simulation-puissance-garde-delta-v7.py` (`027954d8…`, fabriqué depuis la v6
`355f61d1…` par quinze remplacements exacts), huit passages (chacun avec sa sortie, son journal et son manifeste, écrits par le script), les tableaux (`tableaux-v7.md`, produit par
`tableaux-v7.py` à partir des sorties : les tableaux de ce rapport en sont copiés tels quels), les vérifications, et le manifeste d'ensemble `manifeste-puissance-garde-delta-v7.json`, assemblé
par `assembler-manifeste-v7.py` depuis les manifestes par passage (graines, versions, empreintes).

| passage | rôle | répétitions | durée* | commit au lancement | sortie (empreinte) |
| --- | --- | --- | --- | --- | --- |
| `-sortie-logit-0.json` | (i) dispersion nulle, K_h ∈ {10, 5} × K_s ∈ {10, 5, 3}, 288 unités | 2000 | 45,1 s | `9cd6aad3…` | `0507d087…` |
| `-sortie-logit-0.5.json` | (i) échelle logit (v6), σ = 0,5 | 2000 | 57,7 s | `b7acafcf…` | `4de0a079…` |
| `-sortie-logit-1.0.json` | (i) échelle logit (v6), σ = 1,0 | 2000 | 57,6 s | `b7acafcf…` | `b9a2abb8…` |
| `-sortie-beta-0.5.json` | (ii) échelle bêta, κ de σ = 0,5 | 2000 | 70,4 s | `a2de116b…` | `34d35b9e…` |
| `-sortie-beta-1.0.json` | (ii) échelle bêta, κ de σ = 1,0 | 2000 | 84,6 s | `a2de116b…` | `bff030a5…` |
| `-sortie-n80-beta-1.0.json` | (iii) n80 en bêta, κ de σ = 1,0, (10, 10) et (5, 5) | 2000 | 151,6 s | `9cd6aad3…` | `9ae2b3aa…` |
| `-sortie-rejeu-v6-principale.json` | (iv) rejeu, par le script v7, de la commande principale v6 | 2000 | 200,4 s | `a2de116b…` | `639513d0…` |
| `-sortie-rejeu-v6-dispersion-1.0-independante.json` | (iv) rejeu de la commande v6 « dispersion σ = 1,0 indépendante » | 2000 | 151,9 s | `9cd6aad3…` | `9075254d…` |

\* deux passages à la fois sur deux processeurs. **Aucun passage n'a dépassé 25 minutes (le plus long : 200 s) : 2 000 répétitions gardées partout.** Durée totale : environ 14 minutes en deux
voies. Vérifications : `verif-correspondance-beta-v7.py` → `verif-correspondance-beta-v7-sortie.json` ; `verif-identite-v6-v7.py` → `verif-identite-v6-v7-sortie.json` ;
`comparer-v6-v7.py` → `comparaison-v6-v7-rejeux-sortie.json` et `comparaison-v6-v7-cellules-communes-sortie.json` ; `verif-ebh-pole-v7.py` → `verif-ebh-pole-v7-sortie.json` ;
`essais-entrees-v7.py` → `essais-entrees-v7-sortie.json`. Python 3.13.18, numpy 2.5.3 (une seule version pour les huit passages) ; graine maîtresse 20261029, dérivation
`SeedSequence([graine, sha256(étiquette)])` (R9), graines dérivées par cellule dans chaque manifeste.

## 1. Constat → réponse pour les doutes 1 et 2

Vocabulaire : « e-BH » : règle de Benjamini-Hochberg sur les e-valeurs (richesses des paris) du pôle, à budgets α_c/m ; « fiche » : minimum des 8 gardes et des 8 contrastes d'un mode ;
K_h et K_s : exécutions honnêtes et sabotées par unité ; « biais δ/4 » : décalage de 0,0125 de l'espérance du sujet honnête ; p_B : probabilité par unité du comparateur B_j (f_B côté
honnête, espérance τ = 0,01 ; r_B côté saboté, espérance 0,40).

| doute | constat (v6) | réponse en v7 |
|---|---|---|
| **1. Dispersion en échelle bêta** (demandée par la contre-lecture GD5, non simulée en v6 : la décision relayée fixait le logit) | En logit, à σ égal des deux côtés, l'écart-type ajouté vaut 0,012 sur f_B et 0,20 sur r_B : l'échelle charge le contraste, pas la garde ; la perte de la fiche à K ≤ 5 vient des contrastes ; on ne sait pas si la **garde** perd quand la dispersion touche f_B | **Option `--echelle-dispersion logit|beta`** (défaut `logit`, identique à la v6 : § 4). En `beta`, f_B ~ Bêta(τκ, (1 − τ)κ) et r_B ~ Bêta(r_Bκ, (1 − r_B)κ) par unité et par comparateur, **κ commune aux deux côtés**, fixée pour que l'écart-type de r_B égale celui de la v6 au σ de référence (correspondance exacte au § 2, vérifiée par simulation, T3). La corrélation intra-unité ρ_b = Var/(p₀(1 − p₀)) est alors la même des deux côtés ; l'écart-type de f_B devient **0,023** (σ = 0,5) et **0,041** (σ = 1,0), contre 0,005 et 0,012 en logit (× 4,4 et × 3,3). **Résultat (T1) : le minimum des 8 gardes reste ≥ 0,995 dans toutes les cellules bêta (1,000 à K_h = 10) ; la fiche en bêta est, cellule pour cellule, à ≤ 0,03 de la fiche en logit au même σ (dans l'erreur type) ; n80 de la garde en bêta ≤ 8 unités au-dessus du logit (T2).** La garde ne perd pas ; la perte reste celle des contrastes |
| **2. K_s = K_h supposé** | Les décisions ne fixent que K_h ; la perte à K ≤ 5 vient des contrastes, donc de K_s | **Option `--K-s`** (produit cartésien avec `--K` ; `--K-sabotes` apparié gardé, les deux ensemble refusés). Passé : K_h ∈ {10, 5} × K_s ∈ {10, 5, 3} (la paire (5, 10), K_s > K_h, en plus). **Résultat (T1, T1bis) : la fiche dépend de K_s et presque pas de K_h.** À K_s = 10, la fiche vaut ≥ 0,986 dans les 20 cellules (K_h 10 ou 5, cinq lois, deux biais) ; à K_s = 5 : 0,971 à 0,975 sans dispersion, 0,934 à 0,946 à σ = 0,5, 0,796 à 0,822 à σ = 1,0, que K_h vaille 10 ou 5 ; à K_s = 3 : 0,626 à 0,649, puis 0,555 à 0,588, puis 0,410 à 0,441. Le minimum des 8 gardes reste ≥ 0,995 partout (1,000 à K_h = 10 ; 0,995 à 1,000 à K_h = 5) |

## 2. Correspondance logit → bêta (doute 1), exacte et vérifiée

Pour σ donné (`--effet-unite-comparateurs`), la v6 tire p_B = sigmoïde(logit p₀ + c + σu), u ~ N(0, 1), à espérance tenue (E[p_B] = p₀ exactement, par quadrature de Gauss-Hermite à 200
nœuds, `moments_logit`). La v7 en échelle bêta pose :

- ρ_b = Var_logit(r_B, σ) / (r_B(1 − r_B)), avec r_B = 0,40 et Var_logit lue par la **même** quadrature ; κ = (1 − ρ_b)/ρ_b ;
- f_B ~ Bêta(τκ, (1 − τ)κ), r_B ~ Bêta(r_Bκ, (1 − r_B)κ) : espérances τ et r_B **exactes** ; Var[p] = ρ_b p₀(1 − p₀) des deux côtés (corrélation intra-unité égale) ;
- écart-type de r_B **égal** à celui de la v6 au même σ (par construction) ; écart-type de f_B = √(ρ_b τ(1 − τ)).

| σ de référence | ρ_b | κ | f_B : (a, b) | r_B : (a, b) | écart-type r_B, logit = bêta | écart-type f_B, logit → bêta |
|---|---|---|---|---|---|---|
| 0,5 | 0,0540 | 17,519 | (0,175 ; 17,34) | (7,01 ; 10,51) | 0,1138 | 0,0052 → 0,0231 (× 4,41) |
| 1,0 | 0,1696 | 4,895 | (0,0490 ; 4,846) | (1,958 ; 2,937) | 0,2018 | 0,0123 → 0,0410 (× 3,33) |

(`verif-correspondance-beta-v7-sortie.json`, `d6dcb8ee…` : correspondance exacte retrouvée par le script à 10⁻¹² près ; en simulation sur 4 000 × 100 × 8 cases, espérances tenues à moins de
2 erreurs types, écarts-types de p_B à moins de 2 % des valeurs attendues des deux côtés et des deux échelles, moment d'ordre 3 de r_B à moins de 2 % de la valeur exacte de la bêta,
corrélation nulle entre comparateurs et entre honnêtes et sabotés en bêta, variances de g et de v conformes à la décomposition écrite ; refus nommés : bêta avec corrélation, paramètres
bêta hors échelle bêta, échelle inconnue ; `conforme: true`.) T3 retrouve ces écarts-types dans les cellules des passages (288 unités).

**Choix à déclarer** : la κ est fixée sur le côté saboté (r_B). L'autre lecture (κ fixée sur f_B) donnerait une dispersion **moindre** des deux côtés (écart-type de r_B 0,059 au lieu de
0,20 à σ = 1,0) et ne répondrait pas à la question posée (la garde perd-elle quand f_B se disperse ?). La forme Bêta(0,049 ; 4,85) de f_B à σ = 1,0 est extrême : la plupart des
unités ont p_B ≈ 0, quelques unes une p_B élevée. C'est un scénario de contrainte, pas une estimation (réserve 1).

**Ce qui n'est pas dans l'échelle bêta** : la corrélation ρ entre comparateurs (refusée) et le lien tenu entre les honnêtes et les sabotés d'une même unité (tirés à part, comme
`--effet-unite-beta` pour A en v5) ; une copule gaussienne par `scipy.special.betaincinv` aurait gardé les deux, mais coûte 11 s par tirage de 2 000 × 8 × 288 valeurs (mesuré) : écartée.
En v6, ρ = 0,17 et le lien pesaient au plus 0,034 et 0,05 sur la fiche (lectures 4 et T6).

## 3. Tableau principal : 288 unités, k = 8, τ = 0,01, δ = 0,05, lecture (A) m = 2, α_c = 0,05, 2 000 répétitions

#### T1. Puissance à 288 unités aux paramètres décidés (k = 8, τ = 0,01, δ = 0,05, α_c = 0,05, lecture (A) m = 2, seuil 40) : fiche, gardes, contrastes

Source : `-sortie-logit-0.json`, `-sortie-logit-0.5.json`, `-sortie-logit-1.0.json`, `-sortie-beta-0.5.json`, `-sortie-beta-1.0.json` ; fiche : `ebh_A.retenues_fiches_du_sujet` (fiche du mode 1 retenue par l'e-BH, m = 2, arrêt à 40) ; gardes et contrastes : bloc `40.0`, `k_gardes.part` et `k_contrastes.part` (le minimum des 8 atteint 40) ; `garde_seule.part` : une garde ; 2000 répétitions, erreur type ≤ 0,011

| dispersion | K_h | K_s | biais | fiche | minimum des 8 gardes | minimum des 8 contrastes | 1 garde |
| --- | --- | --- | --- | --- | --- | --- | --- |
| nulle (σ = 0, les deux échelles) | 10 | 10 | 0 | 1,000 | 1,000 | 1,000 | 1,000 |
| nulle (σ = 0, les deux échelles) | 10 | 10 | 0,0125 | 1,000 | 1,000 | 1,000 | 1,000 |
| nulle (σ = 0, les deux échelles) | 10 | 5 | 0 | 0,971 | 1,000 | 0,958 | 1,000 |
| nulle (σ = 0, les deux échelles) | 10 | 5 | 0,0125 | 0,975 | 1,000 | 0,965 | 1,000 |
| nulle (σ = 0, les deux échelles) | 10 | 3 | 0 | 0,649 | 1,000 | 0,621 | 1,000 |
| nulle (σ = 0, les deux échelles) | 10 | 3 | 0,0125 | 0,647 | 1,000 | 0,618 | 1,000 |
| nulle (σ = 0, les deux échelles) | 5 | 5 | 0 | 0,975 | 1,000 | 0,967 | 1,000 |
| nulle (σ = 0, les deux échelles) | 5 | 5 | 0,0125 | 0,971 | 0,996 | 0,958 | 0,998 |
| nulle (σ = 0, les deux échelles) | 5 | 3 | 0 | 0,626 | 1,000 | 0,604 | 1,000 |
| nulle (σ = 0, les deux échelles) | 5 | 3 | 0,0125 | 0,630 | 0,999 | 0,603 | 1,000 |
| nulle (σ = 0, les deux échelles) | 5 | 10 | 0 | 1,000 | 1,000 | 1,000 | 1,000 |
| nulle (σ = 0, les deux échelles) | 5 | 10 | 0,0125 | 1,000 | 0,996 | 1,000 | 0,999 |
| logit σ = 0,5 | 10 | 10 | 0 | 1,000 | 1,000 | 1,000 | 1,000 |
| logit σ = 0,5 | 10 | 10 | 0,0125 | 1,000 | 1,000 | 1,000 | 1,000 |
| logit σ = 0,5 | 10 | 5 | 0 | 0,943 | 1,000 | 0,922 | 1,000 |
| logit σ = 0,5 | 10 | 5 | 0,0125 | 0,934 | 1,000 | 0,915 | 1,000 |
| logit σ = 0,5 | 10 | 3 | 0 | 0,576 | 1,000 | 0,536 | 1,000 |
| logit σ = 0,5 | 10 | 3 | 0,0125 | 0,558 | 1,000 | 0,528 | 1,000 |
| logit σ = 0,5 | 5 | 5 | 0 | 0,936 | 1,000 | 0,921 | 1,000 |
| logit σ = 0,5 | 5 | 5 | 0,0125 | 0,946 | 0,998 | 0,932 | 0,999 |
| logit σ = 0,5 | 5 | 3 | 0 | 0,584 | 1,000 | 0,556 | 1,000 |
| logit σ = 0,5 | 5 | 3 | 0,0125 | 0,564 | 0,997 | 0,537 | 1,000 |
| logit σ = 0,5 | 5 | 10 | 0 | 1,000 | 1,000 | 1,000 | 1,000 |
| logit σ = 0,5 | 5 | 10 | 0,0125 | 0,999 | 0,997 | 1,000 | 0,999 |
| logit σ = 1,0 | 10 | 10 | 0 | 0,993 | 1,000 | 0,987 | 1,000 |
| logit σ = 1,0 | 10 | 10 | 0,0125 | 0,986 | 1,000 | 0,984 | 1,000 |
| logit σ = 1,0 | 10 | 5 | 0 | 0,810 | 1,000 | 0,775 | 1,000 |
| logit σ = 1,0 | 10 | 5 | 0,0125 | 0,798 | 1,000 | 0,764 | 1,000 |
| logit σ = 1,0 | 10 | 3 | 0 | 0,418 | 1,000 | 0,399 | 1,000 |
| logit σ = 1,0 | 10 | 3 | 0,0125 | 0,417 | 1,000 | 0,396 | 1,000 |
| logit σ = 1,0 | 5 | 5 | 0 | 0,822 | 1,000 | 0,793 | 1,000 |
| logit σ = 1,0 | 5 | 5 | 0,0125 | 0,796 | 0,998 | 0,767 | 0,999 |
| logit σ = 1,0 | 5 | 3 | 0 | 0,433 | 1,000 | 0,409 | 1,000 |
| logit σ = 1,0 | 5 | 3 | 0,0125 | 0,410 | 0,997 | 0,399 | 0,999 |
| logit σ = 1,0 | 5 | 10 | 0 | 0,990 | 1,000 | 0,984 | 1,000 |
| logit σ = 1,0 | 5 | 10 | 0,0125 | 0,988 | 1,000 | 0,982 | 1,000 |
| bêta (κ de σ = 0,5) | 10 | 10 | 0 | 1,000 | 1,000 | 1,000 | 1,000 |
| bêta (κ de σ = 0,5) | 10 | 10 | 0,0125 | 1,000 | 1,000 | 1,000 | 1,000 |
| bêta (κ de σ = 0,5) | 10 | 5 | 0 | 0,941 | 1,000 | 0,925 | 1,000 |
| bêta (κ de σ = 0,5) | 10 | 5 | 0,0125 | 0,935 | 1,000 | 0,918 | 1,000 |
| bêta (κ de σ = 0,5) | 10 | 3 | 0 | 0,555 | 1,000 | 0,528 | 1,000 |
| bêta (κ de σ = 0,5) | 10 | 3 | 0,0125 | 0,580 | 1,000 | 0,544 | 1,000 |
| bêta (κ de σ = 0,5) | 5 | 5 | 0 | 0,939 | 1,000 | 0,921 | 1,000 |
| bêta (κ de σ = 0,5) | 5 | 5 | 0,0125 | 0,946 | 0,997 | 0,930 | 1,000 |
| bêta (κ de σ = 0,5) | 5 | 3 | 0 | 0,588 | 1,000 | 0,561 | 1,000 |
| bêta (κ de σ = 0,5) | 5 | 3 | 0,0125 | 0,583 | 0,999 | 0,558 | 1,000 |
| bêta (κ de σ = 0,5) | 5 | 10 | 0 | 1,000 | 1,000 | 1,000 | 1,000 |
| bêta (κ de σ = 0,5) | 5 | 10 | 0,0125 | 1,000 | 0,998 | 1,000 | 1,000 |
| bêta (κ de σ = 1,0) | 10 | 10 | 0 | 0,989 | 1,000 | 0,984 | 1,000 |
| bêta (κ de σ = 1,0) | 10 | 10 | 0,0125 | 0,993 | 1,000 | 0,989 | 1,000 |
| bêta (κ de σ = 1,0) | 10 | 5 | 0 | 0,804 | 1,000 | 0,771 | 1,000 |
| bêta (κ de σ = 1,0) | 10 | 5 | 0,0125 | 0,799 | 1,000 | 0,759 | 1,000 |
| bêta (κ de σ = 1,0) | 10 | 3 | 0 | 0,440 | 1,000 | 0,408 | 1,000 |
| bêta (κ de σ = 1,0) | 10 | 3 | 0,0125 | 0,441 | 1,000 | 0,419 | 1,000 |
| bêta (κ de σ = 1,0) | 5 | 5 | 0 | 0,813 | 1,000 | 0,779 | 1,000 |
| bêta (κ de σ = 1,0) | 5 | 5 | 0,0125 | 0,796 | 0,997 | 0,760 | 0,999 |
| bêta (κ de σ = 1,0) | 5 | 3 | 0 | 0,410 | 1,000 | 0,389 | 1,000 |
| bêta (κ de σ = 1,0) | 5 | 3 | 0,0125 | 0,417 | 0,995 | 0,409 | 0,999 |
| bêta (κ de σ = 1,0) | 5 | 10 | 0 | 0,990 | 1,000 | 0,987 | 1,000 |
| bêta (κ de σ = 1,0) | 5 | 10 | 0,0125 | 0,990 | 0,997 | 0,985 | 0,999 |

σ = 0 : aucune dispersion, les deux échelles coïncident (une seule ligne). Logit : écart-type σ de l'effet d'unité en logit, espérance tenue, indépendant entre comparateurs (v6). Bêta : f_B ~ Bêta(τκ, (1 − τ)κ), r_B ~ Bêta(r_Bκ, (1 − r_B)κ), κ telle que l'écart-type de r_B égale celui de la v6 au σ indiqué (T3) ; honnêtes et sabotés tirés à part. (5, 10) : K_s > K_h, hors de la demande, donné en plus.

#### T1bis. Résumé de T1 : fiche retenue, étendue (minimum – maximum) sur K_h ∈ {10, 5} et biais ∈ {0 ; 0,0125}, par K_s

Source : T1

| dispersion | K_s = 10 | K_s = 5 | K_s = 3 |
| --- | --- | --- | --- |
| nulle (σ = 0, les deux échelles) | 1,000 – 1,000 | 0,971 – 0,975 | 0,626 – 0,649 |
| logit σ = 0,5 | 0,999 – 1,000 | 0,934 – 0,946 | 0,558 – 0,584 |
| logit σ = 1,0 | 0,986 – 0,993 | 0,796 – 0,822 | 0,410 – 0,433 |
| bêta (κ de σ = 0,5) | 1,000 – 1,000 | 0,935 – 0,946 | 0,555 – 0,588 |
| bêta (κ de σ = 1,0) | 0,989 – 0,993 | 0,796 – 0,813 | 0,410 – 0,441 |

La fiche dépend de K_s (contrastes) et presque pas de K_h (gardes) : lire T1.

**Hypothèses de ce tableau (à citer avec le chiffre)** : k = 8 comparateurs dont chacun a sa garde et son contraste dans le minimum de la fiche ; τ = 0,01 ; δ = 0,05 ; α_c = 0,05 entier
(famille seule) ; lecture (A) : 2 modes indépendants et de même loi, m = 2, arrêt à 40, une génération ; 288 unités honnêtes et 288 sabotées (jumeaux, lien tenu pour A et pour les
comparateurs en logit ; comparateurs tirés à part en bêta) ; sujet A sans dispersion par unité (binomial) ; comparateurs B_j binomiaux (σ = 0), à dispersion logit σ à espérance tenue,
ou bêta de κ correspondante ; biais 0 ou δ/4 du sujet honnête ; aucune fiche nulle ; 2 000 répétitions, erreur type ≤ 0,011 ; graine 20261029. Les cellules (10, 10) et (5, 5) de
`logit-0` sont, champ pour champ, celles de la sortie principale v6 à 288 unités (§ 4).

Lecture en trois lignes : la garde tient partout (minimum des 8 gardes ≥ 0,995, et 1,000 à K_h = 10), en logit comme en bêta ; la fiche ne dépend que de K_s : ≥ 0,986 à K_s = 10 dans les
vingt cellules, 0,80 à 0,98 à K_s = 5, 0,41 à 0,65 à K_s = 3 ; les deux échelles donnent la même fiche à ≤ 0,03 près (dans le bruit : l'erreur type d'une différence est 0,016).

## 4. Identité avec la v6 et contrôle de la simulation

- **Rejeu de la commande principale v6** par le script v7 (`--K 10,5,3`, 160 à 400 unités, avec n80) : 989 champs communs, 24 cellules, **0 différence** ; champs propres à la v7 : 5, tous
  dans `reglages` (`echelle_dispersion`, `K_s`, `paires_K_h_K_s`). **Rejeu de la commande v6 « dispersion σ = 1,0 indépendante »** (le chemin de code modifié) : 1 475 champs communs,
  24 cellules, **0 différence**, mêmes 5 champs propres (`comparaison-v6-v7-rejeux-sortie.json`, `31256e5a…`, `conforme: true`). Le champ `/reglages/sortie` est exclu : différent par
  construction.
- **Cellules communes** : `logit-0` contre la sortie principale v6, 4 cellules (K_h = K_s ∈ {10, 5}, 288 unités, deux biais), 148 champs, **0 différence** ; `beta-1.0` contre `n80-beta-1.0`,
  4 cellules, 204 champs, **0 différence** (`comparaison-v6-v7-cellules-communes-sortie.json`, `3158c691…`).
- **Au niveau de `cellule(…)`** (`verif-identite-v6-v7-sortie.json`, `6c6105a2…`) : 9 cellules d'essai (dispersion nulle ; logit σ = 1 avec ρ = 0,17 ; lien coupé ; effet sur A ; effet bêta sur
  A ; fiches nulles ; K_s ≠ K_h par le constructeur ; lectures (A) et (B)), 685 champs, **0 différence**, mêmes noms de loi ; témoin négatif (R5) : la même comparaison entre la v7 en
  bêta et la v6 en logit trouve 12 différences et des noms de loi distincts (`_beta`) ; les six paires (K_h, K_s) donnent six noms distincts, identiques entre v6 et v7.
- **Retenue e-BH contre le pôle** (`verif-ebh-pole-v7-sortie.json`, `5fb86178…`, `pari_apparie.py` `ec6c2cf6…`, lecture seule) : 20 000 familles contre `ebh_pondere`, 0 différence ; 72
  cellules (dont 23 en échelle bêta et 40 à K_s ≠ K_h), 144 lectures, 5 760 suites, 34 680 fiches relues par `evaluer` et `Course` : 0 différence d'atteinte, de retenue ou de part ;
  écart maximal des trajectoires et des valeurs arrêtées 1,8·10⁻¹⁵ ; `conforme: true`.
- **Essais d'entrées** (`essais-entrees-v7-sortie.json`, `181152b1…`) : 125 essais, **125 conformes**, 92 refus nommés, 0 erreur brute : les 104 essais de la v6 repris tels quels, plus 21
  essais v7 : bêta sans σ ou avec σ = 0 (refus « sans objet »), échelle inconnue ou en majuscules (refus), bêta avec corrélation entre comparateurs (refus « non traitée »), bêta avec
  `--lien-coupe` sans effet sur A (refus), bêta avec effet sur A et `--lien-coupe` (accepté : le lien coupé porte sur A), bêta avec `--effet-unite-beta` (refus « croisement »), bêta avec
  fiches nulles et lectures (A) et (B) (accepté, loi nulle nommée `_beta`), `--K-s 5,3` (deux lois nommées), `--K 10,5 --K-s 10,5,3` (six lois, six cellules), `--K-s` avec `--K-sabotes`
  (refus), `--K-s` souligné, nul, virgule finale, doublé, paire doublée (refus nommés), `--K-sabotes` seul (comportement v6 gardé), `--K-s` avec fichiers réels (secours sur la première
  paire).
- **Artefacts de la garde** (R5, T4) : frontière E[g] = δ au plus 0,22 fois la borne de Ville, tricheur à 0, dans les huit passages (cellules bêta comprises).
- **Manifeste d'ensemble** : huit passages, commit et état git du manifeste de chaque passage égaux à ceux de sa sortie, empreintes recomptées, aucune divergence ; trois commits au
  lancement (le dépôt reçoit des commits d'autres sessions pendant les passages, comme en v6, T5). Le script est « non suivi ».

## 5. Autres tableaux

#### T2. n80 : unités honnêtes pour que le minimum des 8 gardes atteigne le seuil avec une part de 0,8 (comparateurs seuls, sans fiche), K_s = K_h

Source : v7 : `-sortie-n80-beta-1.0.json` (9ae2b3aa…) ; v6 (lues, non recalculées) : `simulation-puissance-garde-delta-v6-sortie-principale.json` (40f36288…), `simulation-puissance-garde-delta-v6-sortie-n80-dispersion-0.5.json` (bede32e0…), `simulation-puissance-garde-delta-v6-sortie-n80-dispersion-1.0.json` (d0bb686a…) ; `lois.*.n_pour_puissance_0_8_k_gardes` ; dichotomie, 2 000 répétitions, incertitude de graine jusqu'à ≈ 6 %

| dispersion | source | K_h = K_s | biais | seuil 40 | seuil 160 |
| --- | --- | --- | --- | --- | --- |
| nulle | v6 | 10 | 0 | 128 | 168 |
| nulle | v6 | 10 | 0,0125 | 184 | 236 |
| nulle | v6 | 5 | 0 | 136 | 176 |
| nulle | v6 | 5 | 0,0125 | 208 | 264 |
| logit σ = 0,5 | v6 | 10 | 0 | 128 | 168 |
| logit σ = 0,5 | v6 | 10 | 0,0125 | 184 | 236 |
| logit σ = 0,5 | v6 | 5 | 0 | 140 | 176 |
| logit σ = 0,5 | v6 | 5 | 0,0125 | 204 | 264 |
| logit σ = 1,0 | v6 | 10 | 0 | 132 | 168 |
| logit σ = 1,0 | v6 | 10 | 0,0125 | 184 | 236 |
| logit σ = 1,0 | v6 | 5 | 0 | 140 | 180 |
| logit σ = 1,0 | v6 | 5 | 0,0125 | 204 | 264 |
| bêta (κ de σ = 1,0) | v7 | 10 | 0 | 136 | 172 |
| bêta (κ de σ = 1,0) | v7 | 10 | 0,0125 | 192 | 244 |
| bêta (κ de σ = 1,0) | v7 | 5 | 0 | 144 | 180 |
| bêta (κ de σ = 1,0) | v7 | 5 | 0,0125 | 212 | 272 |

La garde est tirée avec le sujet A commun aux 8 comparateurs ; la dispersion est celle des comparateurs B_j.

Lecture : en bêta à σ = 1,0, n80 monte de 4 à 8 unités au plus sur le logit (sous l'incertitude de graine de 6 %) ; au seuil 40 (lecture (A)), n80 ≤ 212 : max(288 ; n80) = 288 partout ;
au seuil 160 (référence), n80 ≤ 272 < 288.

#### T3. Correspondance logit → bêta : κ, corrélation intra-unité et écarts-types de p_B, attendus (décomposition écrite par le script) et tirés (288 unités, biais 0)

Source : `lois.*.decomposition_effet_unite` et `cellules.*.moments_tires` des sorties de dispersion

| dispersion | K_h | K_s | κ | ρ intra-unité f_B | ρ intra-unité r_B | E[f_B] tiré | E[r_B] tiré | écart-type p_B honnêtes attendu | tiré | écart-type p_B sabotés attendu | tiré |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| logit σ = 0,5 | 10 | 10 | — | 0,0028 | 0,0540 | 0,010 | 0,400 | 0,0052 | 0,0052 | 0,1138 | 0,1138 |
| logit σ = 0,5 | 5 | 3 | — | 0,0028 | 0,0540 | 0,010 | 0,400 | 0,0052 | 0,0052 | 0,1138 | 0,1139 |
| logit σ = 1,0 | 10 | 10 | — | 0,0153 | 0,1696 | 0,010 | 0,400 | 0,0123 | 0,0123 | 0,2018 | 0,2017 |
| logit σ = 1,0 | 5 | 3 | — | 0,0153 | 0,1696 | 0,010 | 0,400 | 0,0123 | 0,0123 | 0,2018 | 0,2018 |
| bêta (κ de σ = 0,5) | 10 | 10 | 17,519 | 0,0540 | 0,0540 | 0,010 | 0,400 | 0,0231 | 0,0232 | 0,1138 | 0,1139 |
| bêta (κ de σ = 0,5) | 5 | 3 | 17,519 | 0,0540 | 0,0540 | 0,010 | 0,400 | 0,0231 | 0,0231 | 0,1138 | 0,1138 |
| bêta (κ de σ = 1,0) | 10 | 10 | 4,895 | 0,1696 | 0,1696 | 0,010 | 0,400 | 0,0410 | 0,0410 | 0,2018 | 0,2019 |
| bêta (κ de σ = 1,0) | 5 | 3 | 4,895 | 0,1696 | 0,1696 | 0,010 | 0,400 | 0,0410 | 0,0411 | 0,2018 | 0,2018 |

E[f_B] visé 0,010, E[r_B] visé 0,400. Logit : la corrélation intra-unité diffère des deux côtés (le logit charge r_B) ; bêta : κ commune, même corrélation intra-unité des deux côtés, écart-type de r_B égal à celui du logit au même σ, écart-type de f_B 3 à 4 fois plus grand.

#### T4. Artefacts de la garde (R5), toutes cellules de tous les passages

Source : tous les passages, blocs `frontiere_part`, `frontiere_borne_ville`, `tricheur_part`

| passage | cellules | frontière / borne de Ville (max) | tricheur (max) |
| --- | --- | --- | --- |
| `logit-0` | 12 | 0,02 | 0,000 |
| `logit-0.5` | 12 | 0,06 | 0,000 |
| `logit-1.0` | 12 | 0,04 | 0,000 |
| `beta-0.5` | 12 | 0,06 | 0,000 |
| `beta-1.0` | 12 | 0,04 | 0,000 |
| `n80-beta-1.0` | 4 | 0,04 | 0,000 |
| `rejeu-v6-principale` | 24 | 0,22 | 0,000 |
| `rejeu-v6-dispersion-1.0-independante` | 24 | 0,16 | 0,000 |

Frontière E[g] = δ : doit rester sous la borne de Ville 1/seuil (rapport ≤ 1) ; tricheur E[g] = 2δ : doit rester ≈ 0.

#### T5. Passages : répétitions, durée, commit au lancement, état du script (lus dans le manifeste de chaque passage), empreinte de la sortie

Source : `manifeste-simulation-puissance-garde-delta-v7-sortie-*.json`, comparés aux champs `commit` et `etat_du_script` de chaque sortie

| passage | répétitions | durée (s) | commit au lancement | état du script | sortie = manifeste | sortie |
| --- | --- | --- | --- | --- | --- | --- |
| `logit-0` | 2000 | 45,1 | `9cd6aad314ce` | non suivi (??) | oui | `0507d087…` |
| `logit-0.5` | 2000 | 57,7 | `b7acafcfd7c8` | non suivi (??) | oui | `4de0a079…` |
| `logit-1.0` | 2000 | 57,6 | `b7acafcfd7c8` | non suivi (??) | oui | `b9a2abb8…` |
| `beta-0.5` | 2000 | 70,4 | `a2de116b4e48` | non suivi (??) | oui | `34d35b9e…` |
| `beta-1.0` | 2000 | 84,6 | `a2de116b4e48` | non suivi (??) | oui | `bff030a5…` |
| `n80-beta-1.0` | 2000 | 151,6 | `9cd6aad314ce` | non suivi (??) | oui | `9ae2b3aa…` |
| `rejeu-v6-principale` | 2000 | 200,4 | `a2de116b4e48` | non suivi (??) | oui | `639513d0…` |
| `rejeu-v6-dispersion-1.0-independante` | 2000 | 151,9 | `9cd6aad314ce` | non suivi (??) | oui | `9075254d…` |

## 6. Ce que cela change à la phrase du brouillon 4 de G1

Phrase actuelle : « K_h = 10, n_h ≥ 288 tient sous les lois essayées ; K_h = 5 n'est sûr que sans dispersion ».

Ce que la v7 établit (lois synthétiques, 288 unités, k = 8, τ = 0,01, δ = 0,05, lecture (A) m = 2, α_c = 0,05, biais ≤ δ/4, 2 000 répétitions) :

1. **La première moitié tient et s'étend à l'échelle bêta** : à K_h = K_s = 10, la fiche vaut ≥ 0,986 sous les cinq lois (nulle, logit σ ≤ 1,0, bêta de κ correspondante), et la garde
   elle-même (minimum des 8) vaut 1,000 partout ; n80 de la garde ≤ 244 < 288 au seuil 160 et ≤ 192 au seuil 40, même en bêta.
2. **La seconde moitié vise le mauvais K** : ce qui n'est sûr que sans dispersion, c'est **K_s = 5** (0,97 sans dispersion, 0,93 à 0,95 à σ = 0,5, 0,80 à 0,82 à σ = 1,0, que K_h vaille 10 ou 5),
   et non K_h = 5 : à K_h = 5 avec K_s = 10, la fiche vaut ≥ 0,988 sous les cinq lois et le minimum des 8 gardes ≥ 0,996. La dispersion de f_B, même portée à un écart-type de 0,041
   (bêta, κ de σ = 1,0), ne fait pas perdre la garde ; à τ = 0,01 et δ = 0,05, la dérive δ domine la variance de g.
3. **Phrase proposée** (sans recommandation sur le choix des valeurs) : « K_s = 10, n ≥ 288 tient sous les lois essayées (dispersion nulle, logit σ ≤ 1,0, bêta à corrélation intra-unité
   égale des deux côtés jusqu'à 0,17, biais ≤ δ/4), que K_h vaille 10 ou 5 ; K_s = 5 n'est sûr que sans dispersion (0,97) et tombe à 0,80 à σ = 1,0 ; la garde ne perd sous aucune de
   ces lois (minimum des 8 gardes ≥ 0,995, n80 ≤ 272 au seuil 160). » Les décisions R-416, R-435 et R-446 ne fixent que K_h : **fixer K_s est un point à trancher par Lazar** (modification
   de paramètre du programme : hors de ma main), la v7 ne le décide pas.

## 7. Doutes restants

1. **Lois synthétiques ; σ et κ sont des scénarios**, pas des estimations (P-9 : f_A non lue avant G1 ; la surdispersion de f_B et de r_B sera mesurée au pilote). La forme Bêta(0,049 ; 4,85)
   de f_B à κ de σ = 1,0 est extrême (réserve 1 de la v6, inchangée).
2. **κ fixée sur r_B** (§ 2) : un autre appariement (sur f_B) donne moins de dispersion des deux côtés et une fiche au moins aussi bonne ; non passé.
3. **Échelle bêta sans corrélation entre comparateurs ni lien honnêtes-sabotés** (tirés à part) ; la copule gaussienne qui les garderait coûte 11 s par tirage ; en v6 ces deux
   facteurs pesaient ≤ 0,034 et ≤ 0,05 sur la fiche, dans le sens favorable.
4. **Réserve 4 de la v6 inchangée** : effets de A et des B tirés indépendamment, combinaison non simulée ; sujet A sans dispersion dans tous les passages de la v7.
5. **K_s > K_h** : une seule paire (5, 10). K_h = 3 (sous le plancher) non repassé en v7 (v6, T1).
6. **Réserves 5 à 10 de la v6 inchangées** (deux modes, une génération, α_c entier ; fiches nulles non repassées en v7 ; biais a priori ; n80 sur la garde seule ; GD3-02 ; forme `ecarts`).
7. **Git** : le script lit le commit et l'état par `git rev-parse`, `git ls-files`, `git status` (lecture seule, comme en v6, GD4-05) ; je n'ai lancé aucune commande git moi-même ; le
   script est « non suivi » ; trois commits au lancement pour huit passages (T5).
8. **Environnement** : Python 3.13.18, numpy 2.5.3 ; scipy non utilisé.
9. **Non relu par une autre main (R2)** : contre-lecture à demander ; points à regarder en premier : la correspondance κ (§ 2, `parametres_beta_comparateurs`), le tirage bêta dans
   `tirer`, le produit cartésien `--K-s`, et la lecture « c'est K_s, pas K_h » (§ 6).
