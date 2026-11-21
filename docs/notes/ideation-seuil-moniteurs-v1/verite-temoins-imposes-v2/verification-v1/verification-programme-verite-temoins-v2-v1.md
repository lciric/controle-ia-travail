# Vérification du programme de vérité des témoins, v2 (course « seuil et moniteurs ») — v1

Vérificateur du programme de vérité des témoins, modèle S. Écrit le 2026-11-21. Pièce de travail pour la mère seule : elle contient des valeurs refaites ; elle ne sort pas de ce dossier. Aucun appel, aucune clé, aucune dépense, aucun commit. Aucun refus de permission ni de garde.

## 0. Verdict

**Conforme, prêt à sceller.** Aucune correction exigée. Quatre réserves non bloquantes (§ 7) et deux points pour la mère (§ 8).

- 217 essais passent (annoncés : 217).
- Table v2 jouée deux fois chez moi : `cmp` muet, empreinte `11008999625bb5311927f17b2a1a85c2a7464b4f9e4390ba36e7f8659d67ab31`, égale à celle du livrable. Contre ma table v1 vérifiée, `diff` : exactement trois lignes (rang de T08 en entier, décalage de T09 arrondi à douze décimales, version). Aucune valeur, borne ou issue ne change.
- Les cinq réserves de ma vérification v1 et la remarque 10 sont levées (§ 1). Le contrôle de la dérive de F est juste et refait par une autre méthode sur huit cas (§ 3).
- Le défaut de la sortie factice v3 est celui de la factice, non du contrôle (§ 4).

## 1. Empreintes et rejeu

Livrable copié chez moi (`livrable-v2/`). `sha256sum -c` : les 15 lignes de la table d'empreintes `02b535a6…` (le « table `02b535a6…` » du mandat est la table d'empreintes ; la table de vérité est `11008999…`) et les 15 compagnons OK. Programme `bcd7fbac…`, essais `957b3717…`, rapport `c6af8545…`.

Essais : `…/.venv/bin/python -B -m pytest -q -p no:cacheprovider test_verite_temoins_imposes_v2.py` : **217 passed** en 144 s.

Rapport : aucun nom de modèle ni clé dans le livrable (hors `lectures/`) ; les seules occurrences de « claude » sont dans les chemins des en-têtes de différentiels et au § 7 du rapport (nom du répertoire de travail, « claude-0 »). Les étiquettes « modèle O » et « modèle S » sont des rôles.

Programme de contrôle chez moi : `essais_conventions_v2_v1.py`, `essais_tolerance_v2_v1.py`, `essais_v2b_v1.py`, `fabriquer_derive_v2.py`, et mes correspondances dans `derive/` ; mes sorties de rejeu de la table : `table2-a.json`, `table2-b.json`. (Un script plus long, `essais_v2_v1.py`, dont la mesure aléatoire de tolérance à n = 5 000 était trop lente en rationnels exacts, a été remplacé par les deux scripts ciblés ; ses sections courtes, n ≤ 3 000, donnent un pire écart de 7 × 10⁻¹⁵ à 7,8 × 10⁻¹⁶.)

## 2. Les cinq réserves et la remarque 10

| point | verdict | ce que j'ai fait |
|---|---|---|
| Remarque 10, écart type | levée | « moyenne plus k écarts types », n = 40, k = 5/2, sur N(0,1) : programme (couverture, taux moyen) pour n − 1 : (0,683435 ; 0,009010), pour n : (0,649369 ; 0,009708) ; simulation de 2 × 10⁶ échantillons à graine fixe : (0,683987 ; 0,009006) et (0,649805 ; 0,009703) : accord à 6 × 10⁻⁴ près (simulation). Nomination, sur la couverture (là où les conventions diffèrent de 0,034) : annonce = valeur n − 1 : `n_moins_1` ; annonce = valeur n : `n` ; annonce au milieu des deux, ou étrangère : `aucune`, statut au-delà de 0,001. Sur le taux moyen les deux conventions sont à 0,0007 et « les deux » accordent : exact et sans défaut. |
| `erreur_numerique` | levée | lot de quatre témoins : un témoin à `sigma` = 10⁴⁰⁰ rend `refuse/erreur_numerique`, le témoin à n = 5 001 rend `taille_au_dela_du_plafond`, les deux autres sont calculés ; les `comptes` nomment `ids_refuses = [GEANT, TROP]`. Le lot continue. |
| Plafond `N_MAX = 5000` | levé | n = 5 000 calculé en mode exact (valeur exacte de 20 002 caractères, instantané) ; n = 5 001 refusé. |
| « 0 » et « 0.0 » | levée | lois lues `mu = 0, sigma = 1` et `mu = 0.0, sigma = 1.00` : forme canonique égale ; témoin recalculé : mode `exact_rationnel`, borne 0 (en v1 : `flottant_borne`, 1,5 × 10⁻¹¹) ; `mu = 10⁻¹⁰` reste une autre loi. |
| `comptes` nomme les témoins | levée | `ids_ecarts_au_dela_de_0_001`, `ids_ecarts_indecis_a_la_borne`, `ids_desaccords_d_issue`, `ids_refuses`, triés ; vérifié sur mon lot. |
| Forme | levée | rang de T08 en entier, décalage de T09 arrondi (`diff` § 0) ; test d'en-tête. |
| Tolérance | acceptable, déclarée, non démontrée | § 2.1. |

Un point de fond sur l'accord d'issue : `accord_issue` vaut vrai si l'issue annoncée est celle de l'une OU l'autre convention ; la sortie donne aussi `accord_issue_par_convention`. Cela peut accorder une valeur lue selon n et une issue lue selon n − 1. Sans effet pour les témoins imposés (la règle n'y figure pas) ; point 8.2.

### 2.1 La tolérance max(10⁻¹², 2 × 10⁻¹⁵ × n)

Ce n'est pas une borne, et le rapport le dit. Je l'ai jugée à l'aide d'une mesure à moi, sur une autre grille que celle du développeur : pour n de 1 000 à 5 000, k − 1 entre 41 et 3n/4, p choisi pour que la répartition vaille environ 0,5 (là où l'erreur est la plus grande), p dyadique donc exact, contre la queue binomiale en rationnels :

| n | pire écart mesuré | tolérance déclarée | marge |
|---|---|---|---|
| 1 000 | 5,9 × 10⁻¹³ | 2,0 × 10⁻¹² | 3,4 |
| 2 000 | 9,4 × 10⁻¹³ | 4,0 × 10⁻¹² | 4,3 |
| 3 500 | 2,4 × 10⁻¹² | 7,0 × 10⁻¹² | 2,9 |
| 5 000 | 2,7 × 10⁻¹² | 1,0 × 10⁻¹¹ | 3,7 |

La marge est de 2,9 à 4,3 sur ma grille (le développeur annonce « au moins 3,6 » sur la sienne) : mince, mais la tolérance est une marge de sécurité sur une erreur d'évaluation de l'ordre de 10⁻¹² pour un enjeu de 10⁻³, soit neuf ordres de grandeur de réserve sur ce que le programme tranche. Les voies par petit k (récurrence de log C, somme compensée) tombent à 10⁻¹⁵ ; la voie de la bêta incomplète (k − 1 > 40) porte l'erreur résiduelle, qui n'est pas strictement linéaire en n (2,4 × 10⁻¹² à n = 3 500, k − 1 = 41). Je la juge raisonnable à condition de la garder « déclarée, non démontrée » (c'est le cas) ; elle ne fait basculer aucune issue de la table, dont les voies flottantes (n ≤ 300) gardent la tolérance de 10⁻¹² : la table est identique à l'octet près.

## 3. Le défaut des 4 300 chiffres

`texte_fraction` lève la limite de conversion le temps du rendu, la restaure dans un `finally` (vérifié : limite 4 300 avant et après, y compris quand le rendu échoue) et ne sert qu'au rendu. J'ai refait deux vérifications : (a) un entier de 5 000 chiffres lu par `json.loads` est toujours refusé (la limite reste active pour les entrées) ; (b) n = 5 000 rend sa valeur exacte (20 002 caractères) sans erreur. Verdict : **sûr, avec une réserve de précision** : la garantie « jamais pour la lecture d'une entrée » n'est pas tout à fait exacte à la lettre, car `canonique` (via `_normaliser`) appelle `texte_fraction` sur les nombres des lois d'entrée, donc sans limite. Elle ne crée pas de faille nouvelle : un rationnel d'entrée de plus de 4 300 chiffres ne peut venir que d'un flottant JSON à exposant (`1e5000`), dont la construction par `Fraction` coûte déjà davantage que son rendu (même comportement qu'en v1), et le calcul qui suit refuse proprement (`erreur_numerique`, vérifié au `sigma` = 10⁴⁰⁰). Le processus n'est pas multi-fil. Réserve 7.1.

## 4. Le contrôle de la dérive de F

Lecture du code (l. 1484-1580) : s est cerné par dichotomie sur P_F(X > s) = 1 %, la dérive translate de d = δ × écart type de F (convention de `decalage`), le taux après dérive P_F(X > s − d) est encadré (tolérance d'évaluation en plus) et comparé à 3 % ± 10⁻³ en valeur absolue : « dérive cohérente » si l'encadrement est dedans, « dérive incohérente : F écartée » s'il est dehors, `indecise_a_la_borne` s'il chevauche ; δ = 0 exact ; loi hors moteur, réseau, grappes, bloc mal formé, tranche sans 299, `controle` qui ne dit pas 3 % à 10⁻³ : refus codé dans le bloc, le lot continue ; sans `--correspondance` : `non_transmise`.

Refait par une autre méthode : `scipy.stats` (`isf`, `sf`), pour trois lois (Laplace d'échelle 2, Student à 5 degrés, normale N(0,25 ; 1)), un décalage juste et un faux chacun, plus deux frontières :

| cas | δ transmis | taux après dérive : scipy | programme | verdict attendu | verdict rendu |
|---|---|---|---|---|---|
| Laplace juste | 0,7768361992 | 0,030000000 | 0,029999999999 | cohérente | cohérente |
| Laplace faux | 0,7 | 0,026910986 | 0,026910985514 | incohérente | incohérente |
| Student juste | 0,7307121192 | 0,030000000 | 0,03 | cohérente | cohérente |
| Student faux (−0,03) | 0,7007121192 | 0,028603254 | 0,028603253975 | incohérente | incohérente |
| normale juste | 0,4455542659 | 0,030000000 | 0,030000000001 | cohérente | cohérente |
| normale fausse | 0,5 | 0,033898939 | 0,033898939123 | incohérente | incohérente |
| frontière haute (taux 0,031) | 0,4600521306 | 0,031000000 | 0,031000000001 | incohérente (écart de quelques 10⁻¹² au-delà) | incohérente |
| frontière basse (taux 0,029) | 0,4306499500 | 0,029000000 | 0,028999999997 | incohérente | incohérente |

Accord scipy-programme : 5 × 10⁻¹² au pire ; le « décalage qui triple » rendu pour information concorde (0,776836199212 pour Laplace, 0,730712119201 pour Student, 0,44555426589 pour la normale). Refus : loi de type `autre` : `loi_hors_moteur` ; `controle` à 5 % ± 1 % : `derive_controle_different` ; loi sur réseau : `derive_loi_non_continue`. L'indicateur `accord_avec_la_lecture_de_T09` vaut vrai quand l'entrée porte la lecture correspondante (Laplace juste) et faux sinon : il est informatif, comme le dit le rapport.

Une remarque sur le seuil : à 3 % la tolérance absolue de 10⁻³ revient à ± 0,0125 écart type environ pour δ ; un décalage arrondi à deux décimales (0,45) reste cohérent, à une seule décimale (0,4 ou 0,5) non.

## 5. La sortie factice v3 et la v4

Le constat du développeur est correct et le contrôle ne se trompe pas : la factice v3 transmet δ = 0,5 sous N(0,25 ; 1), qui donne un taux de 0,0339 (mon calcul : 0,033898939), à 0,0039 du but ; 0,5 est un arrondi de commodité, non le décalage qui triple. **C'est un défaut de la factice.** Pour la v4 : δ = 0,4455542659 (`NormalDist`, écrit « 0.4456 » dans la correspondance) : mon recalcul à δ = 0,4455542659 rend « cohérente » (0,030000000001) ; à 0,4456 le taux vaut environ 0,03 + φ(1,88) × 4,6 × 10⁻⁵ = 0,030003, ce qui recoupe le 0,030003111972 que le coordinateur me rapporte. Je n'ai pas rejoué la correspondance `7a997edb…` elle-même (je n'ai pas lu le dossier de la v4) : le recoupement est un calcul, non un rejeu.

## 6. Table

Rejeu ×2 : `cmp` muet, empreinte égale (§ 0). Égalité à la v1 hors des trois lignes : `diff` de mes deux tables, trois différences et aucune autre.

## 7. Réserves non bloquantes

1. La phrase « jamais pour la lecture d'une entrée » du rapport (§ 1, point 8) n'est pas exacte à la lettre : `_normaliser` rend les rationnels des lois d'entrée avec la limite levée ; sans conséquence (§ 3). À corriger dans une phrase d'erratum, ou à laisser.
2. Une entrée de fichier avec un entier JSON de plus de 4 300 chiffres lève encore une `ValueError` non attrapée dans `main` (trace, sortie 1) : arrêt franc et non silencieux ; même comportement qu'en v1.
3. La marge de la tolérance est de 2,9 à 4,3 sur ma grille : à garder « déclarée, non démontrée » ; ne pas l'écrire comme une borne.
4. `accord_issue` vrai si l'une des deux conventions accorde, indépendamment de la valeur (§ 2).

## 8. Points pour la mère

1. Rien ne manque avant le scellement ; les quatre réserves se règlent, si on le veut, par un erratum de classe B.
2. Pour « moyenne plus k écarts types » à l'usage de l'auteur : décider si l'issue annoncée doit suivre la même convention que la valeur. Aujourd'hui, l'une ou l'autre suffit (`accord_issue_par_convention` donne le détail). Décision de lecture, pas de calcul.
3. Le contrôle de dérive est prêt à lire la correspondance du programme de vérification v4 ; la tolérance absolue de 10⁻³ est un choix de la mère et se lit comme telle.

vérificateur du programme de vérité des témoins, modèle S
