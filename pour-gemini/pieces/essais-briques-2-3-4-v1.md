# Essais des briques 2, 3 et 4 de la méta-conception (organisme v6.2.1) — v1

Rédigé le 2026-10-26T18:11:09Z (heure lue sur `date -u`). Lignée conv-audit, sous-agent, travail sur processeur seulement.
Entrées en lecture seule : `fournis/rapport-meta-conception.md` (empreinte `96d12112c8d8d7e376943fa42fc0a4d6faed52b7ed09ae9ecac981c65949c6cf`) et `fournis/organisme/` (27 fichiers, empreintes dans `manifeste-essais-v1.json` ; intacts après les runs, aucun fichier compilé écrit).
Fonctions de l'organisme et de la caste 1 : copies exactes extraites du source par l'arbre syntaxique (empreinte de chaque segment consignée), jamais importées. Python 3.13.17, numpy 2.5.3, scipy 1.18.1, `python3 -I -B`. Graines : `numpy.random.SeedSequence(entropy=20261026, spawn_key=(tâche, …))`, détail par fichier de résultats. Relance complète : `sh lancer_tout_v1.sh`. Une seconde relance donne des résultats identiques hors champs d'heure et de durée (les 7 fichiers).

## Verdict

- Brique 2 : le noyau du rapport n'est pas semi-défini positif (1 000 jeux en violation sur 1 000 ; sa diagonale est nulle, donc sa trace aussi). Sinkhorn-Knopp plus γI ne le répare qu'à γ ≥ 0,37, et le noyau réparé repousse alors exactement les paires qu'il devait favoriser. L'égalité « trace = 1 − ⟨d,d⟩² » est fausse : la trace vaut 14 + ⟨d,d⟩². Le correctif (similarité de domaine dans le noyau, qualité à part, partage d'opérateur réintroduit après tirage) donne 0,89 à 0,94 de paires de domaines différents et 99,5 à 100 % d'ensembles bisociatifs.
- Brique 3 : la répulsion actuelle ne voit aucun pivot. Ses 6 termes sont les 6 premiers, par ordre alphabétique, de 35 jetons présents dans les 5 textes : mots-outils, clé du gabarit, mots de la question. Un pivot n'y entre qu'à f ≥ ⌊0,75 n⌋/n et en l'absence de 6 mots-outils omniprésents. Le graphe de ligne coûte bien en d_B² (pente 2,007). Il est dominé par une exemption appuyée sur une fréquence de fond.
- Brique 4 : le score de fertilité a un biais de verbosité (×2,5 à ponts constants). La normalisation réduit ce biais sans l'annuler. Le filtre de contradictions est parfait sur un lexique propre, mais garde 34 % de fusions contradictoires dès qu'on ajoute un bruit réaliste.

## 0. Faits de code relevés avant les essais

| Fait | Preuve |
|---|---|
| `_score_pertinence_texte` n'existe pas dans le code v6.2.1 fourni : la question de Lazar et le rapport décrivent un tri qui n'est pas là. | 0 occurrence dans les fichiers `.py` de `fournis/organisme/` (recherche sur tout le répertoire) |
| `mitose_spectrale.py` ne contient ni Cholesky ni log-déterminant. La « capacité » vaut n / (1 + (n − 1) s̄) · log(1 + SNR), où s̄ est la similarité quadratique moyenne hors diagonale. « La décomposition de Cholesky existante de mitose_spectrale.py » sur laquelle le plan du rapport s'appuie n'existe pas. | `mitose_spectrale.py` l. 31-42 ; 0 occurrence de `cholesky` dans les `.py` |
| La « répulsion d'Onsager » n'est qu'une phrase de consigne envoyée aux castes 3 et 4 (« Termes deja satures… ne repete pas les arguments deja acquis »). Elle ne touche jamais le tirage d'articles. La liste affichée dans le rapport, calculée sur 5 textes, l'est après la boucle et n'est injectée nulle part. | `principal.py` l. 1252-1268, 1399, 1431 |
| `decomposer_jacobi_symetrique` renvoie \|λ\| triées, donc perd le signe. À son plafond par défaut de 120 rotations, elle ne converge pas à 20×20 (résidu relatif médian 0,046). À 16×16, matrice de type mémoire, l'erreur sur σ1/σ6 reste ≤ 0,51 %, et le 60,9 du protocole P1 n'est donc pas en cause. Dans les essais : 5 000 rotations, signe restitué par le quotient de Rayleigh, résidu ≤ 1,9e-10, écart au calcul de référence d'algèbre linéaire ≤ 4,4e-15. | [instrument], [b2-psd] |
| L'expression des jetons de l'organisme est en ASCII seulement : un mot accentué est coupé en fragments (« bilinéaire » → « bilin », « aire » ; « chaîne » → « cha »). L'extraction de la caste 1 (`\b[a-z]{4,}\b`) élimine au contraire tout mot accentué. | [b3-gen18] ; copie de `extraire_termes` |

## 1. Brique 2 — noyau de tirage

### Essai 1 : semi-définie positivité de la forme du rapport

Méthode. 1 000 jeux de n = 20 couples (d_i, o_i) unitaires tirés uniformément sur la sphère de dimension 16, q_i uniforme sur [0,5 ; 1,5]. Le noyau est assemblé sous la forme exacte L_ij = q_i q_j ⟨o_i,o_j⟩² (1 − ⟨d_i,d_j⟩²), puis décomposé par la copie de la fonction de Jacobi de l'organisme. Violation si λ_min < −10⁻⁸.

| Mesure | Valeur |
|---|---|
| Jeux en violation | **1 000 / 1 000** (de même à 120 rotations : un quotient de Rayleigh négatif suffit à le certifier) |
| λ_min | médiane −0,715 (de −1,414 à −0,366) ; λ_min/λ_max médiane −0,545 |
| Valeurs propres négatives par matrice | 10 à 13 sur 20 (médiane 11) |
| \|diagonale\| max ; \|trace\| max | 2,3e-15 ; 7,0e-15 |
| Mineurs principaux 2×2 négatifs | 189 380 / 190 000 (les autres ont L_ij < 10⁻⁶) |

Pourquoi. ⟨d_i,d_i⟩ = 1 annule la diagonale de M = J − C∘C, donc celle de L, donc sa trace. Une matrice symétrique non nulle de trace nulle a une valeur propre négative. Le théorème du produit de Schur exige deux facteurs semi-définis positifs, et M ne l'est pas. La note de la consigne (« K∘M n'est pas forcément indéfini ») est juste en général, mais ici K = (O∘O) a une diagonale unité et M une diagonale nulle : l'indéfinition est certaine dès que L ≠ 0. Conséquences : P({i}) ∝ L_ii = 0 pour tout singleton, P({i,j}) ∝ −L_ij² < 0 pour toute paire. Aucun tirage n'est défini. Cholesky échoue dans 200 corpus sur 200, en version gloutonne incrémentale comme en version de la bibliothèque d'algèbre linéaire [b2-tirages].

Sinkhorn-Knopp (5 itérations) puis + γI. Écart à la bistochasticité après 5 itérations : 2,9e-4 en médiane. La version symétrisée D L D est une congruence, elle conserve l'inertie : λ_min reste négatif (médiane −0,484). Violations : 1 000 / 1 000 pour γ ∈ {10⁻⁶ ; 10⁻³ ; 10⁻² ; 10⁻¹}. Le γ minimal requis vaut 0,37 à 0,66 (médiane 0,48), soit la moitié d'une somme de ligne, et non une régularisation « de Tikhonov ». À ce γ, la diagonale est constante : la qualité disparaît, et l'effet sur la sélection s'inverse (essai 3).

**Affirmation « garanti semi-défini positif par produit de Schur » : réfutée (1 000 / 1 000 violations).**

### Essai 2 : forme « trace » de la caste 2

Pour d unitaire, P = I − d dᵀ est un projecteur (P² = P à 5,6e-16), donc P^{1/2} = P et Tr(P_i P_j) = D − 2 + ⟨d_i,d_j⟩².

| Mesure (190 000 paires, D = 16) | Valeur |
|---|---|
| \|T − (14 + c²)\| max, racine exacte P^{1/2} = P | **3,6e-15** |
| idem, racine numérique (décomposition propre ; Jacobi de l'organisme sur 20 jeux) | 6,5e-8 ; 3,7e-8. L'erreur est en racine de la précision machine, à cause de la valeur propre nulle de P. |
| \|T − (1 − c²)\| min | **13,0** |
| Plage de T ; corrélation de Pearson T / c² | [14,000 ; 14,732] ; 1,0000000000000 (≥ 0,99999999999998) |
| Semi-définie positivité de ⟨o,o⟩·T | 0 / 1 000 violations ; λ_min ≥ 0,288 |

**Égalité « Tr[…] = 1 − ⟨d,d⟩² » : réfutée. La trace vaut 14 + ⟨d,d⟩².** La forme trace est bien semi-définie positive. Sa dépendance au domaine n'est que de 1/14 (de 14 à 15), et elle va dans le mauvais sens pour la lecture « affinité » du rapport : plus les domaines se ressemblent, plus le terme est grand, alors que (1 − c²) diminue. Dans un processus déterminantal, son terme dominant 14·⟨o_i,o_j⟩ est une similarité, donc une répulsion. Elle écarte les paires qui partagent un opérateur : 5,5 à 16 % d'ensembles bisociatifs contre 33,5 à 71,5 % au hasard (essai 3).

### Essai 3 : correctif et comparaison

Corpus synthétiques. n = 20 articles, 5 domaines, 8 opérateurs. d_i et o_i sont le prototype de leur étiquette plus un bruit isotrope (norme ≈ 0,6), en dimension 16. Trois configurations : étiquettes uniformes et indépendantes ; « hubs » (domaines inégaux, opérateurs selon une loi de Zipf d'exposant 1,2) ; « corrélée » (chaque domaine a un opérateur maison avec probabilité 0,6). 200 corpus par configuration. Sélection gloutonne du déterminant maximal, k = 4, départage au premier indice. Correctif : L = diag(q)(S + 10⁻³ I)diag(q), S_ij = ⟨d_i,d_j⟩². Mesures : « domaines » = part des 6 paires de domaines différents ; « bisoc » = ensembles contenant une paire même opérateur ET domaines différents (l'association visée) ; « q » = qualité moyenne. Les méthodes c3 à c5 utilisent les étiquettes d'opérateur, supposées extraites.

| Méthode | domaines (unif. / hubs / corr.) | bisoc (unif. / hubs / corr.) | q |
|---|---|---|---|
| hasard | 0,793 / 0,744 / 0,790 | 0,500 / 0,715 / 0,335 | 0,99-1,02 |
| tri par qualité (analogue d'un tri séparable) | 0,812 / 0,738 / 0,794 | 0,490 / 0,675 / 0,305 | 1,37-1,38 |
| a1 rapport, déterminant signé | 0,848 / 0,794 / 0,810 | 0,930 / 0,935 / 0,705 | 1,12-1,13 |
| a2 rapport, \|det\| (code de la caste 1) | 0,849 / 0,821 / 0,655 | 0,975 / 0,985 / 0,735 | 1,14-1,16 |
| a3 rapport réparé (Sinkhorn + γ minimal) | 0,726 / 0,615 / 0,808 | **0,000 / 0,060 / 0,005** | 0,99-1,00 |
| b forme trace | 0,828 / 0,734 / 0,854 | **0,055 / 0,160 / 0,050** | 1,33-1,36 |
| c1 correctif | **0,947 / 0,896 / 0,929** | 0,585 / 0,770 / 0,415 | 1,35-1,37 |
| c3 correctif, partage dans q (q·(1 + partenaires bisociatifs)) | 0,945 / 0,906 / 0,921 | 0,915 / 0,985 / 0,870 | 1,27-1,29 |
| c4 correctif conditionné à un opérateur-pivot | 0,894 / 0,843 / 0,728 | 1,000 / 0,995 / 0,975 | 1,10-1,20 |
| c5 correctif, paire garantie après tirage | **0,936 / 0,891 / 0,922** | **1,000 / 1,000 / 0,995** | 1,32-1,35 |

Erreurs-types : ≤ 0,021 sur « domaines », ≤ 0,035 sur « bisoc ». Une paire bisociative existe dans 200, 200 et 199 corpus.

Lecture dans les deux sens.
- En glouton, la forme du rapport favorise le partage d'opérateur entre domaines (bisoc 0,705 à 0,985), mais par accident algébrique. Avec une diagonale nulle, le déterminant à 3 éléments vaut 2·L_ab·L_ac·L_bc et récompense un triangle d'affinités. Ce n'est pas un processus déterminantal : Cholesky échoue (200 / 200), 17 à 25 % des sous-ensembles de taille 4 ont un déterminant négatif, et aucun tirage n'existe. Dès qu'on le rend semi-défini positif, il fait l'inverse (bisoc 0,000 à 0,060). Sur le critère P2 du rapport (paires ⟨d,d⟩ < 0,25 et ⟨o,o⟩ > 0,5), a2 obtient 0,48 / 0,55 / 0,34 et le correctif c1 seulement 0,13 / 0,20 / 0,08.
- Le correctif donne la meilleure diversité de domaines à qualité conservée. Le partage d'opérateur n'y est ni favorisé ni détruit : c1 vaut 0,585 / 0,770 / 0,415 contre 0,500 / 0,715 / 0,335 au hasard. Un processus déterminantal ne sait que repousser : par l'inégalité de Hadamard, det(L_S) ≤ Π L_ii, et toute similarité hors diagonale fait baisser la probabilité. L'attraction voulue sur l'opérateur ne peut donc pas être mise dans le noyau. **Il faut la réintroduire après tirage (c5)** : bisoc 0,995 à 1,000 pour un coût de 0,005 à 0,011 en diversité et de 0,008 à 0,039 en qualité. Dans q (c3), c'est moins sûr, car un score unaire ne garantit pas la paire. Le conditionnement (c4) coûte en diversité (0,728 en configuration corrélée) et en qualité.

Dégénérescence (tirage exact de taille 4, loi P(S) = det(L_S)/Σ sur les 4 845 sous-ensembles ; 20 corpus par configuration ; 50 tirages, une graine chacun) [b2-degen] :

| Noyau (configuration uniforme ; entre parenthèses, plage sur les 3 configurations) | prob. modale (moy.) | distincts / 50 (moy. ; min) | domaines E[·] | bisoc E[·] | rang(q, inclusion) |
|---|---|---|---|---|---|
| c1 correctif, sans Sinkhorn ni γ | 0,0025 | 49,15 ; 46 | 0,839 (0,778-0,846) | 0,491 | **0,96** (0,95-0,97) |
| c1 + γ = 10⁻³·λ_max | 0,0025 | 49,15 ; 46 | 0,838 | 0,491 | 0,96 |
| Sinkhorn sur S seul + γ | 0,0041 | 49,35 ; 48 | 0,862 (0,827-0,868) | 0,497 | **0,83** (0,77-0,83) |
| Sinkhorn sur L entier + γ | 0,0013 | 49,75 ; 49 | 0,865 | 0,512 | **0,03** (0,03-0,05) |
| b forme trace | 0,0028 | 49,25 ; 47 | 0,798 | 0,337 | 0,96 |
| a réparé (Sinkhorn + γ minimal) | 0,00025 | 49,55 ; 48 | 0,797 | 0,416 | 0,04 |
| rapport brut ; Sinkhorn + γ = 10⁻³ | indéfini (17-25 % ; 11-17 % de déterminants négatifs) | — | — | — | — |
| forme trace + Sinkhorn | Sinkhorn impossible (entrées négatives, ⟨o,o⟩ non carré) | — | — | — | — |
| référence uniforme | 0,0002 | 49,75 attendu | 0,799 | 0,474 | — |

- Aucune dégénérescence du tirage exact à n = 20, avec ou sans Sinkhorn + γI. On obtient 44 à 50 ensembles distincts sur 50 graines (moyennes 48,6 à 49,9) pour une probabilité modale ≤ 0,013. Pourtant les 3 premières valeurs propres portent 53 à 71 % de la trace : la dominance spectrale invoquée par la caste 3 est réelle, mais elle n'entraîne pas d'effondrement.
- Le glouton que le rapport implante est déterministe : 1 ensemble distinct sur 50 permutations de l'ordre du corpus, avec ou sans Sinkhorn + γI (1,05 à 1,1 pour « a réparé », par quasi-égalités). Sinkhorn + γI n'y change rien.
- γ augmente le nombre effectif d'ensembles en uniformisant. Pour γ de 0 à 10·λ_max, la diversité attendue passe de 0,839 à 0,796, soit la valeur uniforme 0,799 ; la diversité est perdue, pas gagnée.
- Sinkhorn sur L entier efface q : à convergence exactement, puisque l'échelonnement bistochastique de diag(q) K diag(q) est celui de K ; après 5 itérations, la corrélation de rang passe de 0,96 à 0,03. Sinkhorn sur S seul garde q (0,77 à 0,83) et gagne 0,02 à 0,05 de diversité. **S'il faut Sinkhorn, c'est sur S seulement.**

## 2. Brique 3 — répulsion et pivots de Swanson

### Seuil d'entrée du pivot

`termes_satures` = jetons de fréquence documentaire ≥ max(2, ⌊0,75 n⌋), triés par (−fréquence, ordre alphabétique), 6 premiers. Le seuil réel vaut ⌊0,75 n⌋/n : 60 % à n = 5, 70 % à n = 10, 75 % à n = 20.

Corpus : textes A et C sur deux vocabulaires disjoints (60 mots chacun, loi de Zipf), pivot B dans m des n textes en alternance A/C, k mots-outils présents dans tous les textes (plus 20 mots-outils à probabilité 0,5 quand k > 0). 200 graines par cellule. Probabilité que B soit dans `termes_satures` [b3-synth] :

| n (seuil) | k = 0 | k = 3 | k = 6 | k = 12 |
|---|---|---|---|---|
| 5 (3/5) | f = 0,6 : 0,73 à 1,00 ; f ≥ 0,8 : 1,00 | f = 0,6 : 0,00-0,07 ; 0,8 : 0,77-0,97 ; 1 : 1,00 | 0 pour f < 1 ; f = 1 : 0,98-1,00 | 0 pour f < 1 ; f = 1 : 1,00 (« calcium ») / **0,00** (« magnesium ») |
| 10 (7/10) | 0 pour f ≤ 0,6 ; **1,00 dès f = 0,7** | f = 0,7 : 0,73-0,89 ; ≥ 0,8 : 0,97-1,00 | 0 pour f < 1 ; f = 1 : 1,00 | 0 pour f < 1 ; f = 1 : 1,00 / **0,00** |
| 20 (15/20) | 0 pour f ≤ 0,7 ; **1,00 dès f = 0,75** | idem k = 0 | 0 pour f < 1 ; f = 1 : 1,00 | 0 pour f < 1 ; f = 1 : 1,00 / **0,00** |

Le pivot entre dès f ≥ ⌊0,75 n⌋/n tant que moins de 6 jetons le précèdent. Avec 6 mots-outils omniprésents ou plus, il n'entre jamais pour f < 1. À f = 1, il n'entre que si l'ordre alphabétique le place parmi les 6 premiers ex aequo : « calcium » oui, « magnesium » non avec 12 mots-outils. Le plafond de 6 et les mots-outils protègent donc le pivot, par accident.

### Cas réel : la liste du rapport (gen18)

Les 5 textes des castes, reconstruits depuis le rapport (corps + ligne de vote JSON pour les castes 2 à 5), redonnent **exactement** capacité 3,618972, gain 0,723794, similarité 0,305903 et les 6 termes [b3-gen18]. Il y a 35 jetons présents dans les 5 textes, 67 dans 4 et 93 dans 3 : 195 candidats pour 6 places. **Les 6 termes du rapport sont les 6 premiers, par ordre alphabétique, des 35 ex aequo.**

| Jeton | Nature |
|---|---|
| aux, dans | mots-outils |
| confiance | clé JSON imposée par le gabarit de consigne. Les autres mots du gabarit présents partout (« incertitude », « position », « raisonnement ») sont coupés par l'ordre alphabétique. |
| cholesky | mot de la question |
| article, bruit | vocabulaire du sujet (« bruit » vient en partie de « bruitée » coupé par l'accent) |

Les 35 ex aequo se répartissent ainsi : 15 mots-outils ou nombres, 9 mots de la question (dont « ponts », « swanson », « tirage »), 4 clés du gabarit, 1 fragment d'accent, 6 autres mots du sujet. **Aucun pivot.** Les 5 textes répondent à la même question : il n'y a pas de littératures A et C disjointes, la notion de pivot de Swanson ne s'applique pas. Les listes réellement injectées dans les consignes étaient, pour la caste 3 (2 textes), ['100', '200', '256', '_score_pertinence_texte', 'aire', 'amalgam'] : 3 nombres, un nom de fonction, 2 fragments d'accents. Pour la caste 4 (3 textes) : ['100', '256', '_score_pertinence_texte', 'article', 'aux', 'avec'].

### Remèdes

Vérité terrain : pivot B (à garder), hub générique H présent dans 90 % des textes des deux domaines (à repousser), mots-outils (à ignorer). 200 graines par cellule. « paire-pont bloquée » signifie qu'une paire (B, mot de domaine) est repoussée, ce qui bloque le pont lui-même. Pour (c), la « rétention » stricte compte aussi les paires (B, mot-outil) et (B, H), qui ne bloquent pas de pont.

| Remède (k = 12 mots-outils, f = 0,8) | rétention de B | paire-pont bloquée | H repoussé | part de mots-outils dans la liste | liste vide | unités comptées |
|---|---|---|---|---|---|---|
| base (organisme) n = 5 ; n = 20 | 1,00 ; 1,00 | 0 ; 0 | 0,00 ; 0,00 | **1,00 ; 1,00** | 0 ; 0 | 239 ; 954 jetons |
| (a) liste d'arrêt | **0,00 ; 0,00** | 1,00 ; 1,00 | 0,95 ; 0,99 | 0 ; 0 | 0 ; 0 | idem |
| (b) exemption des ponts entre groupes contrastés (τ = 0,5, 0,7 ou 0,9 : identiques) | 1,00 ; 1,00 | 0 ; 0 | **0,01 ; 0,00** | 0 ; 0 | 0,00 ; **1,00** | + bissection spectrale |
| (b+) idem, et seulement si la fréquence de fond est ≤ 0,1 | **1,00 ; 1,00** | 0 ; 0 | **0,96 ; 0,99** | 0 ; 0 | 0,00 ; 0,01 | + corpus de fond (300 textes) |
| (c) paires co-occurrentes, brutes | 1,00 ; 1,00 | 0 ; 0 | 0,44 ; 0,14 | **1,00 ; 1,00** | 0 ; 0 | 5 638 ; 22 401 paires |
| (c) paires co-occurrentes, après liste d'arrêt | 0,34 ; 0,46 | 0 ; 0 | 0,80 ; 0,54 | 0 ; 0 | 0,00 ; 0,47 | 1 618 ; 6 447 paires |

- Sans mots-outils (k = 0) et à f ≥ seuil, la base et (a) détruisent B dans 57 à 100 % des cas (100 % dès f = 0,8). C'est le seul régime où l'affirmation du rapport est vraie.
- (b) garde B mais exempte aussi H : un pivot et un hub générique ont la même distribution dans un corpus à deux domaines, et aucune règle interne au corpus ne les sépare. La répulsion est vidée (liste vide 100 % pour n ≥ 10). Sur les textes réels, le contraste vaut 0,47 < τ : rien n'est exempté et (b) se comporte comme (a). La marge est mince (0,47 contre τ = 0,5) : la bissection retient la bipartition de contraste maximal, alors que la moyenne sur toutes les bipartitions vaut 0,08.
- Seul (b+), avec une référence externe, garde B et repousse H.
- (c) ne bloque aucune paire-pont pour n ≥ 10. **À n = 5 et f = 1 (5 textes, le régime réel de la question ouverte), il en bloque dans 78 à 79 % des corpus** : un mot de A présent dans les 3 textes A atteint le seuil 3/5. Il perd H quand H est seul fréquent (liste vide 100 % à f = 0,6 pour n ≥ 10, après liste d'arrêt). Sur les textes réels, les 6 paires repoussées sont toutes ('article', x), encore par ordre alphabétique.

Coût du graphe de ligne [b3-synth] : sur 28 corpus (longueurs 30 à 240, d_B de 45 à 642), le comptage explicite des arêtes passant par B est égal à C(d_B, 2) dans 28 cas sur 28. La pente log-log est **2,007**. Le graphe de ligne complet compte 0,88 à 17,7 millions d'arêtes pour 20 textes synthétiques, et **2,21·10⁸** pour les 5 textes réels [b3-gen18] (1 191 jetons, 334 406 paires distinctes, 707 455 arêtes par jeton présent partout). La version par bigrammes orientés coûte d_entrée·d_sortie (≤ 324 ici), mais sur les textes réels ses paires saturées sont des artefacts : ('confiance', 'incertitude'), ('cat', 'goriel'), ('cha', 'raisonnement').

## 3. Brique 4 — fusion « pushout »

### Biais de verbosité du score de fertilité

Fonctions `extraire_termes` et `pushout_conceptuel` copiées à l'identique du code de la caste 1 [b4].

Ponts constants (p ponts plantés 3 fois dans chaque texte, V mots propres par texte) :

| p | score original, V = 2 → V ≥ 30 − p (plafond des 30 termes) | score normalisé, idem |
|---|---|---|
| 1 | 1,61 → 4,08 (×2,53) | 0,322 → 0,069 (×0,21) |
| 3 | 4,83 → 12,02 (**×2,49**) | 0,690 → 0,211 (×0,31) |
| 8 | 12,88 → 30,45 (×2,37) | 1,073 → 0,586 (×0,55) |

Population réaliste : 2 000 paires, p vrai de 0 à 6, longueurs de 10 à 150 jetons par texte, 30 % de vocabulaire général partagé, donc des ponts fortuits.

| Score | corr. de rang avec p vrai | avec la verbosité | partielle verbosité \| p | partielle p \| verbosité |
|---|---|---|---|---|
| original | 0,837 | 0,274 | **0,534** | 0,877 |
| normalisé \|ponts\|/\|union\|·log(1 + \|diff. sym.\|) | **0,872** | 0,153 | **0,351** | 0,886 |
| \|ponts\| seul | 0,857 | 0,228 | 0,477 | 0,885 |

Dans les strates de p, la corrélation avec la verbosité vaut 0,50 à 0,61 pour l'original et 0,22 à 0,45 pour le normalisé. Le résidu vient des ponts fortuits, qui croissent avec la longueur : 1,53, 2,34 puis 3,20 ponts en moyenne selon la tranche. **Le biais est établi. La normalisation le réduit sans l'annuler, et l'inverse à ponts strictement constants.** Corriger le résidu demanderait de comparer le recouvrement à son attendu sous hasard, ou de pondérer les ponts par leur rareté de fond. Ce n'est pas testé ici.

### Filtre de compatibilité des contraintes

Filtre minimal. Quatre axes (linéaire / non linéaire, stationnaire / transitoire, discret / continu, convexe / non convexe), formes françaises et anglaises, expression Unicode, formes négatives masquées avant de chercher les positives. Il y a contradiction si un texte vaut + et l'autre − sur un même axe ; un texte portant les deux marqueurs vaut « ± » et n'est pas compté. Corpus : 200 corpus de 20 textes (10 A, 10 C), valeur plantée +, − ou ∅ par axe (probabilités 0,3 / 0,3 / 0,4), d'où environ 56 % de paires contradictoires. Bruits : paraphrase hors lexique, mention du marqueur contraire hors affirmation, homographe « continue ». Les fusions candidates sont les paires A×C d'interface non vide selon `pushout_conceptuel`.

| Régime (paraphrase, mention contraire, homographe) | candidates | contradictoires acceptées sans filtre | avec filtre | précision | rappel | rejets à tort |
|---|---|---|---|---|---|---|
| propre (0 ; 0 ; 0) | 11 593 | 57,4 % | **0,0 %** | 1,000 | 1,000 | 0,0 % |
| réaliste (0,15 ; 0,15 ; 0,10) | 11 676 | 55,9 % | **34,4 %** | 0,938 | 0,608 | 5,1 % |
| bruité (0,30 ; 0,30 ; 0,20) | 11 726 | 56,3 % | **48,1 %** | 0,817 | 0,354 | 10,2 % |

Par construction, la part de contradictions *détectées* parmi les fusions acceptées est de 0 % avec filtre ; sans filtre, elle vaut 57,4 %, 36,3 % ou 24,4 % selon le régime. Par ailleurs, **65 à 67 % des fusions candidates n'ont aucun des ponts plantés dans leur interface** : la condition « B = O_A ∩ O_C non vide » est remplie par les mots du gabarit et les marqueurs eux-mêmes.

## 4. Verdicts par affirmation

| Code | Affirmation (source) | Verdict | Chiffre |
|---|---|---|---|
| F1 | `principal.py` trie par `_score_pertinence_texte` (question, rapport) | réfutée | 0 occurrence |
| F2 | `mitose_spectrale.py` calcule 0,5 log det(I + SNR G) par Cholesky ; « décomposition de Cholesky existante » (question, rapport) | réfutée | l. 31-42 : approximation n/(1 + (n − 1) s̄) ; 0 Cholesky |
| A1 | L = q q ⟨o,o⟩²(1 − ⟨d,d⟩²) garanti semi-défini positif par produit de Schur (rapport, castes 2 et 5) | **réfutée** | 1 000 / 1 000 ; λ_min médiane −0,715 ; diagonale nulle |
| A2 | Tr[(I − d_i d_iᵀ)^{1/2}(I − d_j d_jᵀ)^{1/2}] = 1 − ⟨d_i,d_j⟩² (caste 2) | **réfutée** | = 14 + ⟨d,d⟩² à 3,6e-15 ; écart ≥ 13,0 |
| A3 | La forme trace est semi-définie positive (caste 2) | établie | 0 / 1 000 ; λ_min ≥ 0,288 |
| A4 | La forme trace couple similarité d'opérateur et orthogonalité de domaine (caste 2) | réfutée | bisoc 0,055 / 0,160 / 0,050 contre 0,500 / 0,715 / 0,335 au hasard |
| A5 | 5 itérations de Sinkhorn-Knopp + γI rendent le noyau du rapport utilisable (rapport) | réfutée | violations 1 000 / 1 000 pour γ ≤ 0,1 ; γ min 0,37-0,66 ; réparé : bisoc 0,000-0,060 |
| A6 | Un processus déterminantal dégénère en top-k à n ≈ 20 (caste 3) ; Sinkhorn + γI l'évite (rapport) | réfutée (les deux) | tirage exact : 48,6-49,9 distincts / 50 avec ou sans ; glouton : 1 / 50 avec ou sans |
| A7 | Sinkhorn-Knopp neutralise les hubs sans détruire la définie-positivité (caste 4) | partielle | inertie conservée (congruence) ; sur L entier, q effacé (rang 0,96 → 0,03) ; sur S seul, q gardé (0,77-0,83), diversité +0,02 à +0,05 |
| A8 | Correctif : similarité de domaine dans S, qualité à part → domaines éloignés (consigne) | établie | domaines 0,896-0,947 contre 0,744-0,793 ; q 1,35-1,37 |
| A9 | Le correctif perd le partage d'opérateur (consigne) | partielle | au niveau du hasard (0,415-0,770 contre 0,335-0,715) ; après tirage : 0,995-1,000 |
| B1 | La répulsion actuelle détruit les pivots B en les traitant comme termes saturés (castes 2 et 5) | partielle → réfutée pour l'organisme réel | liste réelle : 0 pivot ; pivot listé seulement si f ≥ ⌊0,75 n⌋/n et < 6 mots-outils omniprésents |
| B2 | La répulsion sur le graphe de ligne préserve les pivots (castes 2 et 5) | partielle | paire-pont bloquée 0 % pour n ≥ 10, 78-79 % à n = 5, f = 1 ; hub perdu |
| B3 | Un pivot de degré d_B génère C(d_B, 2) = O(d_B²) arêtes du graphe de ligne (caste 4) | établie | 28 / 28 égalités ; pente 2,007 ; 2,21·10⁸ arêtes sur gen18 |
| B4 | … et sature la matrice de Cholesky en O(d_max⁶) (caste 4) | non testée | aucune factorisation de Cholesky du graphe de ligne dans le code |
| R1 | Remède (a), liste d'arrêt (consigne) | partielle | liste nettoyée (mots-outils 1,00 → 0) mais pivot exposé (rétention 0,00 dès f = 0,8 ; 0,43-0,45 au seuil exact à n = 5) |
| R2 | Remède (b), exemption des ponts entre domaines contrastés (consigne) | partielle | rétention 1,00 mais hub repoussé 0,00-0,01, liste vide 100 % (n ≥ 10) |
| R3 | Remède (b+), exemption avec fréquence de fond (ajouté) | établie | rétention 1,00 ; hub 0,95-0,99 ; mots-outils 0 |
| C1 | Le score \|ponts\|·log(\|A\| + \|B\| + 1) mesure la fertilité (caste 1) | réfutée (biaisé) | ×2,49 à ponts constants (p = 3) ; partielle verbosité 0,534 |
| C2 | Version normalisée \|ponts\|/\|union\|·log(1 + \|diff. sym.\|) corrige le biais (consigne) | partielle | partielle 0,534 → 0,351 ; rang avec p vrai 0,837 → 0,872 ; inversion à ponts constants (×0,31) |
| C3 | Le filtre de compatibilité garantit que le pushout ne fusionne pas des formalismes incompatibles (castes 4 et 5) | partielle | 57,4 % → 0,0 % (propre) ; 55,9 % → 34,4 % (réaliste) ; 56,3 % → 48,1 % (bruité) |
| C4 | Une interface B = O_A ∩ O_C non vide signale un pont opératoire (castes 2 et 5) | réfutée | 65-67 % des interfaces sans aucun pont planté |

## 5. Réserves

- Tout est synthétique, sauf les 5 textes de gen18, reconstruits exactement. Les taux absolus (bisoc, contradictions) dépendent des paramètres des générateurs, documentés dans chaque fichier de résultats ; les comparaisons entre méthodes, à corpus et graines égaux, sont la partie transposable.
- Les méthodes c3 à c5 utilisent les étiquettes d'opérateur. En pratique il faudrait les extraire, et c'est la limite que le rapport reconnaît lui-même pour les résumés de moins de 150 mots.
- J'ai défini moi-même le remède (b) : groupes par bissection spectrale, contraste = 1 − sim_inter/sim_intra. Une première définition, 1 − cos des centroïdes sur le vocabulaire privé des candidats, donnait 0,95, puis 0,77, sur des textes de même sujet : elle a été rejetée avant les runs finaux. Le seuil τ n'est étalonné que sur deux situations (deux domaines disjoints ; gen18 à 0,47), et la marge sur gen18 est mince. (b+) suppose un corpus de fond. L'archive de l'organisme pourrait en tenir lieu, ce qui n'est pas vérifié.
- Le filtre de contradictions est évalué sur un lexique que j'ai écrit et sur des bruits que j'ai choisis. Son rappel réel sur des résumés moissonnés est inconnu (affirmation C3 indécise sur ce point).
- Résultats « trop propres » à auditer (R4) : 1 000 / 1 000 en A1 et 0 / 1 000 en A3 sont des conséquences algébriques exactes (diagonale nulle ; produit de Schur de facteurs semi-définis positifs), pas des coïncidences d'échantillon. 28 / 28 en B3 est une identité de comptage. Le 0,0 % du filtre propre tient à un lexique planté identique à celui du détecteur.

## 6. Fichiers et empreintes

| Code | Fichier (sous `sortie/`) | SHA-256 |
|---|---|---|
| [b2-psd] | `resultats-b2-psd-trace-v1.json` | `57f816234f81becb3a1fd74403fa7126b83d004824aa2dac15fc389ffb172170` |
| [b2-tirages] | `resultats-b2-tirages-v1.json` | `abc28160eeed51048f274983995ac694eb3761a1005d036fb3356e810d595ccb` |
| [b2-degen] | `resultats-b2-degenerescence-v1.json` | `6d97d6a3607735d6e6aabfc0839ba42554409f87619cbce34f98afa3b0bf0a83` |
| [b3-gen18] | `resultats-b3-gen18-v1.json` | `cb9f6a8c33d8f0e0de2c360becd5e42792b8115eef6b2b87aa41fd24b0889306` |
| [b3-synth] | `resultats-b3-synthetique-v1.json` | `d81dde06b69b5846fccb5b40527ff6381febc2f50d050c6ccc07f4878d6c9ce6` |
| [b4] | `resultats-b4-v1.json` | `a60706696d26013faccb05261defa06f127d0d6a139efc36d28ffe3a7b4c6db2` |
| [instrument] | `resultats-instrument-jacobi-v1.json` | `b3675a120e18192002a6098db248534ade8203db4cc96e8643a4cc4379db684b` |
| manifeste | `manifeste-essais-v1.json` (versions, graines, empreintes des fournis et du code) | `ec1277af235eb6b99a766c4ca286cc3169942b919fe3818648e338209fbf4c9a` |

Code : `commun_v1.py`, `corpus_articles_v1.py`, `textes_v1.py`, `essai_b2_psd_trace_v1.py`, `essai_b2_tirages_v1.py`, `essai_b2_degenerescence_v1.py`, `essai_b3_gen18_v1.py`, `essai_b3_synthetique_v1.py`, `essai_b4_v1.py`, `essai_instrument_jacobi_v1.py`, `manifeste_v1.py`, `lancer_tout_v1.sh`. Chaque fichier a son compagnon `.sha256`.

## 7. Génération 0 — survit / éliminée / indécise

- F1 — tri de `principal.py` par `_score_pertinence_texte` : **éliminée** (fonction absente).
- F2 — capacité par log-déterminant et Cholesky existante dans `mitose_spectrale.py` : **éliminée** (ni l'un ni l'autre dans le code).
- A1 — noyau du rapport garanti semi-défini positif par produit de Schur : **éliminée** (1 000 / 1 000 violations).
- A2 — égalité « trace = 1 − ⟨d,d⟩² » : **éliminée** (trace = 14 + ⟨d,d⟩²).
- A3 — forme trace semi-définie positive : **survit** (0 / 1 000).
- A4 — forme trace au service du couplage d'opérateur entre domaines : **éliminée** (bisoc 0,05-0,16 contre 0,34-0,72 au hasard).
- A5 — Sinkhorn-Knopp (5 itérations) + γI répare le noyau du rapport : **éliminée** (γ ≥ 0,37 requis, et l'effet s'inverse).
- A6 — dégénérescence en top-k à n ≈ 20, évitée par Sinkhorn + γI : **éliminée** (48,6-49,9 distincts / 50 en tirage exact ; glouton déterministe dans tous les cas).
- A7 — Sinkhorn-Knopp sans dommage : **survit sur S seul, éliminée sur L entier** (q effacé, rang 0,96 → 0,03).
- A8 — correctif « similarité de domaine dans S, qualité à part » : **survit** (diversité 0,896-0,947, qualité conservée).
- A9 — partage d'opérateur à réintroduire hors du noyau, après tirage : **survit** (bisoc 0,995-1,000, diversité 0,891-0,936).
- B1 — la répulsion actuelle détruit les pivots : **éliminée** telle qu'énoncée pour l'organisme (0 pivot dans la liste réelle) ; sa version conditionnelle, « un pivot sans concurrent est listé dès f ≥ ⌊0,75 n⌋/n », **survit**.
- B2 — le graphe de ligne préserve les pivots : **indécise** (vraie pour n ≥ 10, fausse à n = 5 et f = 1 : 78-79 %) ; comme remède retenu, **éliminée** (dominé par b+).
- B3 — coût en C(d_B, 2) = O(d_B²) : **survit** (pente 2,007).
- B4 — saturation de Cholesky en O(d_max⁶) : **indécise** (non testée).
- R1 — liste d'arrêt seule : **éliminée** comme remède (expose le pivot) ; **survit** comme premier étage.
- R2 — exemption des ponts entre domaines contrastés, seule : **éliminée** (exempte aussi le hub, vide la liste).
- R3 — exemption avec fréquence de fond : **survit** (rétention 1,00, hub 0,95-0,99).
- C1 — score de fertilité de la caste 1 : **éliminée** (biais de verbosité ×2,49).
- C2 — score normalisé : **indécise** (meilleur, partielle 0,351, mais biais résiduel non nul).
- C3 — le filtre de compatibilité garantit l'absence de contradiction : **éliminée** comme garantie (34,4 % restants en régime réaliste) ; le filtre minimal comme réducteur : **indécise** (rappel réel sur résumés inconnu).
- C4 — interface non vide = pont opératoire : **éliminée** (65-67 % d'interfaces sans pont réel).
