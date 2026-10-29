# Puissance de la garde appariée δ dans la fiche — v5 : finition, retenue e-BH simulée, k = 8 — rapport v5

Lignée conv-audit, 29 octobre 2026, 07:36 UTC (heure lue sur `date -u`). **Remplace la v4** (`rapport-puissance-garde-delta-v4.md`,
`21ec90dc…`, gardée, R12) après la contre-lecture `contre-lecture-garde-delta-v4.md` (`6a34e837…`, GD4-01 à 06) et la demande de
Lazar R-716 (retenue e-BH simulée, k = 8, d'après `parametres-garde-delta-pour-G1-v1.md`, `db603750…`). **Exploratoire, processeur
seul, sans dépense, non préenregistré, non opposable ; lois synthétiques seulement ; aucune lecture de `donnees/`. Aucune option
recommandée.**

Fichiers (dossier `simulation-puissance-garde-delta-v5/`, chacun avec `.sha256`) : script `simulation-puissance-garde-delta-v5.py`
(`7d1239e1…`) ; sept passages, chacun avec sa sortie, son journal et son manifeste écrit par le script (empreintes des sorties,
commande, graines, commit `7ff46b74…`, script « non suivi » au lancement) :

| passage | sortie | répétitions | durée* |
|---|---|---|---|
| principal : k = 1, 3, 8 ; 160, 300, 400, 650 unités ; K ∈ {10, 3} ; τ = 0,01 ; biais 0 et 0,0125 ; δ 0,05 et 0,075 ; seuils 160, 40, 320 ; lectures (A) et (B) | `-sortie-principale.json` `56e87d36…` | 2 000 | 411 s |
| variante τ = 0,10 (k = 8 ; 160, 400, 650 unités) | `-sortie-taux-0.10.json` `841e12d2…` | 2 000 | 170 s |
| variante deux fiches nulles (k = 8, τ = 0,01, biais 0) | `-sortie-fiches-nulles-2.json` `69edecf5…` | 2 000 | 186 s |
| effet d'unité logit σ = 1,0, avec lien coupé, k = 1, 3, 8 | `-sortie-effet-unite-1.0.json` `205ca165…` | 4 000 | 482 s |
| effet d'unité logit σ = 0,5, avec lien coupé, k = 1, 3, 8 | `-sortie-effet-unite-0.5.json` `9fcfec1c…` | 4 000 | 433 s |
| dispersion égale : bêta ρ = 0,17 des deux côtés, k = 1, 3, 8 | `-sortie-effet-beta-0.17.json` `25a83cc2…` | 4 000 | 233 s |
| rejeu de la commande principale v4 | `-sortie-rejeu-v4-principale.json` `afccad54…` | 4 000 | 1 261 s |

\* deux passages à la fois sur deux processeurs : durées gonflées (le passage principal v4 seul prenait 936 s). Aucun passage
n'a dépassé 25 minutes : 2 000 répétitions gardées. Vérifications : `essais-entrees-v5.py` → `essais-entrees-v5-sortie.json`
(`da775b9f…`) ; `verif-ebh-pole-v5.py` → `verif-ebh-pole-v5-sortie.json` (`7392098b…`) ; `comparer-v4-v5.py` →
`comparaison-v4-v5-sortie.json` (`15a08d26…`).

## 1. Réponse à la contre-lecture v4 et à R-716

| constat | réponse en v5 |
|---|---|
| **GD4-01** « l'effet d'unité ne touche presque pas la garde » | lecture retirée et réécrite (§ 3, lecture 5) ; mesure à dispersion égale (`--effet-unite-beta`) ; la colonne « garde » est dite : c'est le **minimum des k gardes** (`k_gardes`), la garde seule est donnée à côté |
| **GD4-02** lien garde-contraste non séparé, E[f_A] non écrit | cellules à effet : `moments_tires` (E[f_A], E[f_B], E[g], E[r_A], E[v], écarts-types, corrélation des probabilités de A entre honnêtes et sabotés de la même unité) ; par loi, `decomposition_effet_unite` (Var f = p₀(1 − p₀)/K + Var p·(1 − 1/K)) ; `--lien-coupe` ajoute la loi « lien coupé » ; l'alignement (même unité, même indice) est écrit « hypothèse la plus liée » |
| **GD4-03** souligné lu dans les CSV | un analyseur commun (`lire_nombre`, `lire_entier`) pour les champs CSV et toutes les options : souligné, inf, nan, hexadécimal, chiffres non ASCII, virgule décimale refusés ; les lignes 183-184 retirées (31 essais de refus, 2 essais sains) |
| **GD4-04** doublons par le nom seulement | doublons repérés par chemin résolu (`./`, lien symbolique) et par empreinte, entre garde et contraste aussi ; refus nommés (5 essais, 1 sain). Non fait : exiger la forme `fA,fB` ou `rA,rB` (la forme `ecarts` reste admise des deux côtés) |
| **GD4-05** git, manifeste | chaque code de retour de git est lu ; tout échec → « inconnu (motif) » : 10 cas à git simulé (hors dépôt, propriétaire douteux, sans commit, commit illisible, ls-files et status en échec, ignoré, modifié, propre, git absent) ; `--sortie` : le script écrit sortie, journal et manifeste, refuse d'écraser (R12) |
| **GD4-06** replis, erreurs brutes | refus nommés : `--ecarts ""`, virgule finale, fichier absent, dossier ; secours sans objet ; τ = 0 ; effet d'unité à p₀ ∈ {0 ; 1} ; identifiants non chaînes (nombre, true, null, vide, liste) ; motif JSON gardé (clé doublée, entier démesuré, NaN). Secours écrit seulement s'il sert, loi de secours nommée dans `lois` |
| **R-716** retenue e-BH simulée | `--lecture-ebh A,B`, `--m-fiches`, `--fiches-nulles` ; reproduit `Course.ajouter_trajectoire` puis `ebh_pondere` (§ 2) ; vérifié contre le pôle |
| **k = 8** | passage principal à k = 1, 3, 8 (§ 2) |
| identité v4 (point 8) | rejeu de la commande principale v4 : **216 cellules et les n₈₀, 5 795 champs, 0 différence**. Effet σ = 0,5 et 1,0 : 32 cellules communes chacune, 803 champs, une seule différence, l'option déclarée `--comparateurs` (1,3 contre 1,3,8). Champ v4 disparu : `reglages/contraste_synthetique_de_secours` (écrit seulement s'il sert, GD4-06) |

Essais d'entrées : 82 sur 82 conformes, 64 refus nommés, 0 erreur brute (script `7d1239e1…`).

**Retenue e-BH : ce qui est reproduit.** Chaque fiche porte la trajectoire du minimum de ses processus (comme `evaluer`) ; elle est
arrêtée au premier instant où ce minimum atteint −log(α_c/m) = log(m/α_c) et garde sinon sa valeur finale (`Course.ajouter_trajectoire`,
une génération, valeur héritée 1) ; la famille de m fiches à budgets α_c/m est lue par `ebh_pondere` (score log b + log e trié, k* le
plus grand k dont le score atteint −log k à 10⁻¹² près, ex æquo au bord compris). Vérification (`verif-ebh-pole-v5-sortie.json`) :
20 000 familles tirées (ex æquo, valeurs au bord, m > f) contre `ebh_pondere` : 0 différence ; 48 cellules, 3 840 suites, 21 360 fiches
relues par `evaluer` et `Course` sur les mêmes tirages rejoués : écart des trajectoires 3,6·10⁻¹⁵, des valeurs arrêtées 1,8·10⁻¹⁵,
0 suite à retenues différentes, parts des cellules identiques.

Hypothèses de la lecture (écrites en sortie) : modes indépendants et de même loi (mode 1 = tirage principal) ; en (B), les k fiches d'un
mode partagent le sujet ; fiches vraies : sujet honnête, écart de contraste +0,10 ; fiches nulles : écart 0, biais 0, sujet propre.

## 2. Résultats : fiche à k = 8 (τ = 0,01 ; sujet partagé ; 2 000 répétitions ; erreur type ≤ 0,011)

**(A)** une fiche par mode, m = 2, arrêt à 40 : part où la fiche du mode 1 est retenue par l'e-BH (entre parenthèses : première
atteinte de 40). **(B)** une fiche par (mode, comparateur), m = 16, arrêt à 320, retenue à 320/k* : part où **les 8 fiches du mode 1**
sont retenues (entre parenthèses : les 8 atteignent 320). Source : `-sortie-principale.json`, `ebh_A`, `ebh_B`.

| K, δ, biais | 160 unités | 300 | 400 | 650 |
|---|---|---|---|---|
| 10 ; 0,05 ; 0 | A 0,99 (0,98) · B 0,99 (0,05) | 1,00 · 1,00 | 1,00 · 1,00 | 1,00 · 1,00 |
| 10 ; 0,05 ; 0,0125 | A 0,76 (0,39) · B 0,80 (0,00) | 1,00 · 1,00 | 1,00 · 1,00 | 1,00 · 1,00 |
| 10 ; 0,075 ; 0 | A 0,99 (0,98) · B 0,99 (0,81) | 1,00 · 1,00 | 1,00 · 1,00 | 1,00 · 1,00 |
| 10 ; 0,075 ; 0,0125 | A 0,99 (0,98) · B 0,99 (0,79) | 1,00 · 1,00 | 1,00 · 1,00 | 1,00 · 1,00 |
| 3 ; 0,05 ; 0 | A 0,15 · B 0,15 | A 0,70 · B 0,68 | A 0,89 · B 0,88 | A 1,00 · B 1,00 |
| 3 ; 0,05 ; 0,0125 | A 0,04 · B 0,05 | A 0,67 · B 0,66 | A 0,90 · B 0,88 | A 1,00 · B 1,00 |
| 3 ; 0,075 ; 0 | A 0,17 · B 0,15 | A 0,68 · B 0,66 | A 0,90 · B 0,89 | A 1,00 · B 1,00 |
| 3 ; 0,075 ; 0,0125 | A 0,17 · B 0,15 | A 0,68 · B 0,67 | A 0,89 · B 0,88 | A 1,00 · B 1,00 |

Toutes les fiches vraies retenues (A : les deux modes ; B : les 16) : K = 3, δ = 0,05, biais 0 : 0,04 / 0,03 ; 0,51 / 0,46 ;
0,81 / 0,79 ; 0,99 / 0,99. À K = 3, le contraste limite : minimum des 8 contrastes au seuil 40 = 0,18 ; 0,67 ; 0,86 ; 0,995, minimum
des 8 gardes ≥ 0,92 (biais 0).

**Tailles minimales à écarts nuls** (garde, g = 0 à chaque unité) : δ = 0,05 : **111** (seuil 40), **161** (seuil 320), 144 (160) ;
δ = 0,075 : **75**, **108**, 97. Avec deux fiches nulles : (A) m = 4, seuil 80 : 128 et 86 ; (B) m = 18, seuil 360 : 163 et 110.

**Effet de k** (première atteinte de 160 par la fiche, biais 0) : K = 10, 160 unités : 0,88 / 0,76 / 0,59 (k = 1 / 3 / 8) ; K = 3,
400 unités : 0,94 / 0,84 / 0,70.

**Variante τ = 0,10** (`-sortie-taux-0.10.json`, k = 8, A · B) : K = 10, δ = 0,05 : 160 unités 0,56 · 0,61 (biais 0), 0,07 · 0,10
(0,0125) ; 400 unités 1,00 · 1,00 et 0,99 · 0,99. K = 3, δ = 0,05 : 400 unités 0,58 · 0,56 (biais 0), 0,16 · 0,13 (0,0125) ; 650 unités
0,96 · 0,95 et 0,53 · 0,49. K = 3, δ = 0,075, 650 unités : ≥ 0,99.

**Variante deux fiches nulles** (`-sortie-fiches-nulles-2.json`, k = 8, biais 0) : fiche nulle retenue dans 0 suite en (A), au plus
0,8 % des suites en (B) ; proportion moyenne de fausses découvertes ≤ 0,0005. Coût sur les vraies : K = 3, δ = 0,05, 400 unités :
A 0,89 → 0,81 ; B 0,88 → 0,87.

Artefacts (R5, garde seule) : frontière E[g] = δ au plus 0,8 fois la borne de Ville dans les six passages neufs ; tricheur ≤ 0,0005.

## 3. Effet d'unité : échelle, dispersion égale, lien (160 unités, δ = 0,05, seuil 160, biais 0, 4 000 répétitions)

**Échelle** (`decomposition_effet_unite`). En logit σ = 1, l'écart-type ajouté à p vaut 0,012 à p = 0,01 (σ·p(1 − p) = 0,0099),
0,091 à p = 0,10 et 0,208 à p = 0,50 (sabotés de A) ; corrélation intra-unité 0,015 ; 0,092 ; 0,17. Part ajoutée de la variance de f_A
(K = 10) : 0,12 à τ = 0,01, 0,45 à τ = 0,10 ; de r_A : 0,61. Espérance tenue : quadrature à 3·10⁻¹⁷ près ; E[f_A] tirés de 0,0099 à
0,0102 (τ = 0,01), |E[g]| ≤ 0,0004 dans toutes les cellules.

**Garde seule, k = 1** (σ = 0 : rejeu v4 ; logit 0,5 ; logit 1,0 ; bêta ρ = 0,17 des deux côtés, honnêtes et sabotés tirés à part) :

| loi | σ = 0 | logit 0,5 | logit 1,0 | bêta ρ = 0,17 |
|---|---|---|---|---|
| K = 10, τ = 0,01 | 0,89 | 0,89 | 0,88 | **0,77** |
| K = 10, τ = 0,10 | 0,46 | 0,42 | 0,36 | **0,30** |
| K = 3, τ = 0,01 | 0,65 | 0,65 | 0,65 | 0,61 |
| K = 3, τ = 0,10 | 0,19 | 0,19 | 0,18 | 0,16 |

Contraste k = 1 au même endroit (K = 10, τ = 0,01) : 0,985 ; 0,95 ; 0,82 ; 0,83 — la bêta et le logit σ = 1 ont presque la même
dispersion côté sabotés (ρ 0,17 contre 0,1735), d'où des contrastes voisins. Minimum des k gardes, logit 1,0, K = 10, τ = 0,10 :
garde seule 0,36, k = 3 : 0,18, k = 8 : 0,09.

**Lien garde-contraste** (fiche : lien tenu / lien coupé ; corrélation des p de A dans l'unité 0,75 à τ = 0,01, 0,88 à τ = 0,10,
0 coupé ; gardes et contrastes pris seuls voisins, écarts ≤ 0,02, tirages indépendants) :
K = 10, τ = 0,10 : k = 1 : 0,25 / 0,30 ; k = 3 : **0,07 / 0,13** ; k = 8 : 0,025 / 0,050. K = 10, τ = 0,01 : k = 3 : 0,49 / 0,49 ;
k = 8 : 0,32 / 0,34. K = 3, τ = 0,10, δ = 0,10, k = 8 : 0,018 / 0,034. À k = 8, K = 10, τ = 0,01, la fiche passe de 0,59 (σ = 0,
passage principal) à 0,32 (logit 1,0, lien tenu).

## 4. Lectures (sans recommandation ; sujet partagé)

1. **k = 8, τ = 0,01, K = 10** : la fiche passe à 300 unités dans les deux lectures et aux deux biais ; à 160 unités, seul le biais
   0,0125 à δ = 0,05 la retient (0,76 en A, 0,80 en B) ; δ = 0,075 tient (0,99).
2. **K = 3** : le contraste limite, garde comprise sans effet ; environ 0,88 à 0,90 à 400 unités, ≥ 0,99 à 650, mais « les deux modes »
   ou « les 16 fiches » à 400 unités : 0,78 à 0,81.
3. **(A) et (B), toutes fiches vraies** : retenues voisines (écarts ≤ 0,04, de signe variable). En (B), quand les 16 fiches sont vraies,
   le seuil effectif des retenues est 320/16 = 20 : la première atteinte de 320 est basse (0,05 à K = 10, 160 unités) et c'est la
   lecture de la valeur finale qui porte (B). Avec deux fiches nulles, (A) double son seuil (m 2 → 4) et perd plus que (B) (16 → 18).
4. La lecture e-BH sur la valeur finale ajoute jusqu'à 0,37 à la première atteinte (K = 10, δ = 0,05, biais 0,0125, 160 unités, A :
   0,39 → 0,76) ; elle n'ajoute presque rien là où le contraste limite (K = 3, k = 8 : au plus + 0,05).
5. **Lecture 3 réécrite.** La garde à δ = 0,05 est fragile au biais d'espérance du sujet et au bruit τ. L'effet d'unité en logit est
   petit près de τ = 0,01 **par construction** (écart-type ajouté ≈ σ·p(1 − p) = 0,01 à σ = 1, corrélation intra-unité 0,015) :
   « la garde ne bouge pas » vient de cette échelle, et du minimum des k gardes, que l'effet commun rend plus corrélées. À τ = 0,10 la
   garde seule baisse déjà (0,46 → 0,36). **À dispersion égale des deux côtés (ρ = 0,17), la garde seule baisse : 0,89 → 0,77
   (τ = 0,01), 0,46 → 0,30 (τ = 0,10)** ; le choix d'échelle décide donc de la lecture, et la surdispersion de f_A entre unités, mesurable
   au pilote, la tranchera. L'alignement « même unité, même indice » est l'hypothèse la plus liée : il retire jusqu'à 0,065 à la fiche
   (K = 10, τ = 0,10, k = 3), 0,02 à k = 8, τ = 0,01.
6. τ = 0,10 : la garde limite ; à K = 3, δ = 0,05, biais 0,0125, la fiche reste ≤ 0,53 à 650 unités.

## 5. Réserves

- Lois synthétiques ; seule la loi réelle par unité (pilote, lots C et J) fixera les chiffres « fiche ». Modes supposés indépendants et
  de même loi ; corrélation réelle des 8 comparateurs d'un mode inconnue (ici : sujet partagé seulement, B_j indépendants).
- Une génération, une famille utilisant tout α_c = 0,05 ; partage avec une autre famille non simulé (seuils plus hauts).
- Fiches nulles : contraste nul et garde vraie, sujet propre ; d'autres formes de fiches nulles non essayées.
- n₈₀ non calculés à k = 8 (`--sans-n80`, temps et mémoire) ; tailles minimales à écarts nuls seulement.
- Bêta : honnêtes et sabotés tirés à part (sans lien) ; seule la garde seule y sert de comparaison à dispersion égale.
- GD3-02 inchangé : un seul ensemble d'unités ; identifiants en JSON seulement. GD4-04 : la forme `ecarts` reste admise des deux côtés.
- Commit au lancement `7ff46b74…`, script non suivi par git (« ?? ») ; aucun commit fait ici.
- Non relu par une autre main (R2) : contre-lecture à demander.
