# Estimation de la durée et de la mémoire maximale de la lecture de l'apprentissage des sondes sur la tâche (étape B bis de T0.7) — v1

Écrite le 2026-11-18 par un sous-agent neuf (Opus 5.5), sous les règles communes `registres/t07-etape-b-bis/lecture-v1/regles-communes-agents-lecture-bbis-v1.md`. Objet : borner la durée et la mémoire maximale du programme de lecture `src/controle_ia/t07bbis/lecture_v5.py` quand il tournera sur les données réelles (processeur, 4 cœurs, 16 Go, sans mémoire d'échange, fils de calcul à 1). **Rien de réel n'a été lu ni joué** : ni le module ni sa garde sur des fichiers réels ou sur l'histoire réelle du dépôt ; aucun fichier sous `diag/`, `donnees/`, `runs/`, `docs/verdicts/`, ni dans le dossier de montage de la lecture. Toutes les durées et mémoires ci-dessous sont celles de **jouets fabriqués** ; ce ne sont pas des mesures de l'expérience.

## Verdict

- **Durée** : estimation centrale **≈ 3 minutes** (≈ 1 min avant le seuil, ≈ 2 min après) ; borne haute prudente **≈ 35 minutes**. La borne haute tient sous une heure avec une marge d'environ 25 minutes.
- **Mémoire maximale** (taille résidente) : estimation centrale **≈ 1,1 Go** ; borne haute prudente **≈ 2,5 Go**. Sur 16 Go, la marge est large (plus de 13 Go).
- **Seuil** (ligne `BBIS LECTURE ENTREES OUVERTES`) : il tombe après les seules gardes de registre et les commandes git d'antériorité ; dans l'estimation centrale, ≈ 25 à 35 % de la durée totale est avant lui, **≈ 65 à 75 % après lui** (≈ 2 minutes de calcul exposé à une coupure) ; dans la borne haute, presque tout le surplus tombe après le seuil.
- **Aucune écriture partielle** : confirmé par lecture du code (section 5). Toute coupure après le seuil perd la lecture entière.

## 1. Tailles retenues (texte scellé et code)

Du texte scellé `prereg/T0.7-etape-B-bis-v1.md` (plan, points 4 à 10 et 13 ; « Données gardées ») et de `commun_v1.py` :
- 64 tâches, deux plis de 32 tâches ; 640 actions par condition, soit 10 actions par (condition, tâche) (garde `exiger_effectifs`), ≈ 320 actions par groupe et par pli ; 9 conditions dans les mesures (≈ 5 760 actions).
- 5 sources plafond (P-instruit, P-S25 à P-S100) × 2 plis ; 10 cellules (5 plafond, 5 transferts).
- 800 directions de plancher par sonde et par pli (`N_DIRECTIONS`) ; 100 sondes du nul de réétiquetage (`N_REETIQUETAGES` ; 50 dans la variante r1, que je ne connais pas et n'ai pas cherché à connaître : j'ai mesuré le cas le plus cher, 100) ; 2 000 tirages par ligne (`N_TIRAGES`) ; niveau décisif 0,99.
- Groupes notés par source (`validation_imbriquee_v1.plan_de_notation`) : P-instruit, 16 groupes avec plancher, 6 avec nul ; P-S25 à P-S75, 6 groupes avec plancher plus 3 groupes « sans le champ du coût » (second plancher de 800 lignes), 2 avec nul ; P-S100, 8 groupes plus 3. Scores en double précision (`apprentissage_carte_v1.scores`, `np.float64`).

## 2. Inventaire de ce qui coûte (lecture du code)

**Avant le seuil** (`lire`, lignes 1452-1491, et `main`) : import du module (≈ 2 s) ; `adaptateur_retenu` (lecture d'une ligne de registre, empreinte du module de la pièce, un `git show`) ; `lire_lignes`, `verifier_lignes` (empreintes de quelques petits fichiers cités) ; `exiger_ordre_propre` et, si l'exception du quatrième addendum s'ouvre, `preuve_entree_conjointe` (une quinzaine de commandes git ponctuelles : `cat-file`, `rev-list -n 1`, `show`, `ls-tree`, `merge-base`) ; **`anteriorite_etape_b`** : un `git log --all -S` (recherche de chaîne dans l'histoire d'un fichier) et deux `git log --all --diff-filter=A` sur un motif de chemin. Ces trois parcours de toute l'histoire dominent l'avant-seuil.

**Après le seuil**, dans l'ordre du code :
1. Issue de P3-bis, audit des fuites, `sondes-bbis.json`, fiche du code, manifeste de 7b, `lecture-cout-t06.json`, `mesures-t06.npz` et `textes-actions-t06.jsonl` (empreintes recalculées, boucle Python sur ≈ 5 760 actions) : quelques secondes.
2. `charger_tableaux` : empreinte et `np.load` de tous les fichiers de scores ; tout est gardé en mémoire **en même temps**, ≈ 240 Mo en double précision au total (jouet à la taille réelle : 237,7 Mo, 598 tableaux) ; la plus grosse pièce est une matrice directions × actions (800 × 320, 2 Mo). `verifier_deux_premieres` : poids des sondes, négligeable.
3. **Lecteurs du texte** (`lecteurs_texte`), 10 (source, pli) : base « mots et coût » (A) et (B), 2 apprentissages (L-BFGS-B, au plus 1 000 itérations, 15 000 évaluations) ; **classifieur lexical** (`lex_pli`) : 4 pénalités × 4 plis internes + 1 apprentissage final = 17 apprentissages logistiques creux (unigrammes et bigrammes, L-BFGS-B, au plus 1 000 itérations), soit **170 apprentissages lexicaux** ; notation de tous les groupes « O ». C'est le premier poste en durée, et le seul dont le coût dépend des données (nombre d'itérations).
4. Contrôle d'égalité de MC (`aires_controle_mc`) : 4 doses × 2 bases × 2 plis = 16 apprentissages sur ≈ 1 280 actions.
5. **Cellules** (`lignes_cellule`) : par cellule, des « règles (a) » à 801 lignes (sonde + 800 directions) : 10 par cellule plafond de (ii) (D, TE, MU, ART, RF, SC, SC_TE, A_T, DOM, DOM-H), 4 pour P-instruit, 4 par transfert vers (ii), 2 pour T-S100-instruit, soit ≈ 62 ; un nul de réétiquetage par cellule (100 jeux d'une ligne) ; des différences appariées (MC, LEX, ENC, DD) ; le contrôle de l'intervalle propre par `intervalle_aire_moyenne` (boucle Python de 2 000 × 2 aires) dans chaque D. Noyau : `comparaisons` (lignes × 32 × 32) puis `plancher_v2.aires_tirees`, par lots de 25 directions, `W (2 000 × 32) @ C (32 × 32)`. Complexité d'une règle (a) ≈ 801 × 2 000 × 32² × 2 opérations par pli, indépendante des valeurs.
6. Dispersion entre ordres de calcul, BB-P6 (jeux d'une ligne), états, issue, réserves, audit : négligeable.
7. Écriture : `creer_manifeste` (un `git status --porcelain --untracked-files=all`, empreinte du texte scellé), sérialisation JSON (≈ 0,1 Mo dans le jouet), scellement, ligne au journal des ouvertures.

**Aucune matrice directions × actions × tirages n'est jamais formée** : la plus grande matrice transitoire est (801 × 2 000) en double précision (12,8 Mo), plus un lot (25 × 2 000 × 32) de 12,8 Mo et les comparaisons (801 × 32 × 32, 6,6 Mo par pli).

## 3. Mesures sur jouets fabriqués

Méthode : la chaîne jouet de bout en bout (`tests/test_t07bbis_bout_en_bout_v1.py`, `tests/aide_t07bbis_jouet_v1.py`) fixe le nombre de tâches et d'actions par la course jouet de T0.6 (6 tâches) ; seuls directions, réétiquetages et tirages se règlent (`essai`). La taille réelle ne s'y fabrique pas sans réécrire la chaîne. J'ai donc écrit un pilote hors du dépôt (`…/scratchpad/estimation/jouet_taille.py`, supprimé après) qui **fabrique** des mesures (9 conditions, coûts, champs de T0.8, textes de 140 à 200 mots), des tableaux de scores de mêmes noms, formes et types que ceux de la marche, les écrit en morceaux de moins de 90 Mo, puis rejoue **la partie de `lire` après le seuil avec les fonctions mêmes du module** : `charger_tableaux` (sur les fichiers fabriqués), `lecteurs_texte`, `aires_controle_mc`, `ContexteLecture`, `Assembleur`, `lignes_cellule` pour les 10 cellules (contrôle de l'intervalle compris), `issue_complete`, `dispersion_ordres`, `audit_r4`, `bbp6`, sérialisation. Fils de calcul à 1, mémoire virtuelle bornée à 8 Go, un cœur, machine partagée avec un autre agent. Mémoire : `resource.getrusage` (`/usr/bin/time` absent). Toutes les lignes de toutes les cellules sont sorties calculables (aucun raccourci par « non calculable »).

| Taille (tâches, actions par tâche, directions, nul, tirages) | Octets des scores | Lecteurs du texte | Cellules (10) | Après chargement, total | Taille résidente maximale |
|---|---|---|---|---|---|
| 16, 4, 50, 10, 200 | 1,9 Mo | 5,1 s | 0,9 s | 6,2 s | 557 Mo |
| 32, 5, 200, 25, 500 | 15,5 Mo | 13,1 s | 2,8 s | 16,2 s | 601 Mo |
| **64, 10, 800, 100, 2 000 (réelle), repli de MC** | 237,7 Mo | 55,2 s | 47,5 s | **104 s** | **1 047 Mo** |
| **64, 10, 800, 100, 2 000 (réelle), code de la pièce** | 237,7 Mo | 55,8 s | 47,2 s | **104 s** | **1 049 Mo** |

À la taille réelle : chargement et empreintes des scores 0,5 s ; contrôle d'égalité de MC 0,8 à 1,4 s ; par cellule, 3,4 s (P-instruit), ≈ 7 s (chaque P-S_d), ≈ 3,5 s (chaque transfert vers (ii)), 2,2 s (T-S100-instruit). La taille résidente de base (≈ 550 Mo) vient de l'import de torch, que la lecture réelle fait aussi (`lecteurs_texte` → `validation_imbriquee_v1` → `apprentissage_carte_v1` → `import torch`).

Noyau du classifieur lexical (`noyau_lex.py`, textes fabriqués à vocabulaire de Zipf sur 20 000 mots, 640 textes de 160 à 280 mots, ≈ 104 000 termes) : 0,4 à 0,6 s par apprentissage ; ≈ 4,4 ms par évaluation de l'objectif ; un apprentissage poussé au plafond de 1 000 itérations coûterait ≈ 1 200 évaluations, soit ≈ 5 s.

Avant le seuil, proxies sur ce dépôt (9 352 commits, 647 références ; motifs **inexistants**, rien de la garde n'est joué) : `git log --all -S` restreint à un fichier ≈ 12 s ; `git log --all --diff-filter=A` sur un motif de chemin ≈ 22 s (le code en lance deux) ; import du module ≈ 2 s ; `git status --untracked-files=all` 0,07 s.

## 4. Bornes

**Durée**
- Centrale : avant le seuil ≈ 2 s + 12 s + 2 × 22 s + quelques secondes de git ponctuel ≈ **1 min** ; après le seuil ≈ 5 s d'entrées + 1 s de chargement + 55 s de lecteurs du texte + 1 s de contrôle de MC + 48 s de cellules + quelques secondes d'écriture ≈ **2 min** ; total **≈ 3 min**.
- Borne haute prudente (cumul de pires cas, chacun peu probable) : 170 apprentissages lexicaux tous au plafond de 1 000 itérations sur un vocabulaire réel plus riche (≈ 6 s chacun) ≈ 17 min ; 36 apprentissages de MC au plafond de leur solveur ≈ 5 min ; cellules et chargement ralentis d'un facteur 2 par l'autre agent et un disque plus lent ≈ 2 min ; parcours git de l'avant-seuil × 3 (histoire plus longue ou cache froid) ≈ 3 min ; marge de 50 % sur le reste ≈ 8 min ; **≈ 35 min**. Le coût des cellules ne dépend pas des valeurs (formes fixées par le texte) : il ne peut pas dériver ; seuls les apprentissages des lecteurs du texte en dépendent.

**Mémoire maximale**
- Centrale : ≈ 550 Mo (interpréteur, numpy, scipy, torch) + ≈ 240 Mo de scores gardés ensemble + mesures et textes (dizaines de Mo) + transitoires de calcul (< 100 Mo) ≈ **1,1 Go** (mesuré 1,05 Go sur le jouet réel, qui portait en plus ses propres structures de fabrication).
- Borne haute prudente : × 2 pour la fragmentation de l'allocateur, des textes réels plus longs, des matrices lexicales plus grandes et un double transitoire au chargement (`np.array(z[nom])` copie chaque tableau) ≈ **2,5 Go**. Aucun chemin du code ne forme de matrice qui croisse avec le produit directions × actions × tirages.

## 5. Seuil et écritures partielles (lecture du code)

- La ligne `BBIS LECTURE ENTREES OUVERTES` est imprimée (`lire`, l. 1491) juste après `anteriorite_etape_b` et la construction de la liste blanche, avant la première ouverture d'une entrée (`issue_p3bis`). Tout ce qui précède est garde de registre, empreintes de petits fichiers et commandes git ; aucun calcul lourd.
- **Aucun résultat partiel n'est écrit** : `lire` assemble tout dans un dictionnaire en mémoire et le rend ; `main` écrit ensuite, en une fois, le manifeste de la lecture puis `diag/<run-lecture>/lecture-bbis.json` (`ecrire_lecture`), puis seulement la ligne `OUVERTURE-BBIS` au journal des ouvertures (`journaliser_ouverture`). Le seul signe laissé par une coupure après le seuil est la ligne imprimée sur la sortie : le journal des ouvertures n'en garde **aucune trace** (à journaliser par l'opérateur, par exemple en gardant la sortie du processus dans un fichier).

## 6. Ce que la mesure ne couvre pas

- Les données réelles : nombre d'itérations des apprentissages lexicaux et de MC sur les vrais textes (borné ci-dessus par les plafonds des solveurs, non mesuré) ; taille réelle du vocabulaire.
- Les commandes git de l'avant-seuil et de la preuve d'entrée conjointe sur l'**arbre de lecture** (histoire et références propres, non ouvertes) : seulement des proxies sur ce dépôt, motifs inexistants.
- La lecture disque des vrais fichiers depuis l'arbre de lecture, l'import des modules gelés de la pièce (`verifier_modules_geles`), `lire_table_A`, la vérification des deux premières directions (poids réels).
- La variante r1 (50 réétiquetages, linéaire seule) : moins chère que le cas mesuré.
- Le coût d'une contention plus forte que celle observée, et tout redémarrage de la machine (rien ne survit à une coupure, section 5).

## 7. Ce qui pourrait faire exploser l'une ou l'autre — et ce qui ferait perdre la lecture sans exploser

- Explosion de mémoire : aucun chemin trouvé ; la seule croissance est linéaire dans les fichiers de scores (≈ 240 Mo). Une source qui écrirait des matrices bien plus grandes que le texte ne le prévoit se verrait déjà au poids des fichiers (morceaux de moins de 95 Mo).
- Explosion de durée : seulement les apprentissages des lecteurs du texte (plafonnés : un non-convergé rend « non calculable », sans boucle) et les parcours git `--all` sur une histoire très longue (avant le seuil, donc sans perte).
- **Hors mandat, signalé parce qu'il fait perdre la lecture après le seuil** : toute `GardeArret` levée entre le seuil et l'écriture remonte à `main`, qui imprime `BBIS LECTURE ARRET` et sort en code 2 **sans rien écrire** ; en particulier `creer_manifeste` (appelé seulement à l'écriture, après tout le calcul) refuse un arbre de travail non propre, **fichiers non suivis compris** (`git status --porcelain --untracked-files=all`), et un dossier `runs/<run-lecture>` déjà présent. L'arbre de lecture doit donc être propre au lancement et le rester pendant les ≈ 2 minutes de calcul (aucun fichier créé dedans par un autre agent).

## 8. Fichiers ouverts

- Code et textes : `lecture_v5.py`, `plis_v1.py`, `commun_v1.py`, `adversaires_texte_v1.py`, `lien_mots_et_cout_v1.py`, `validation_imbriquee_v1.py` (en partie), `marche_v4.py` (en partie), `validation_imbriquee_v4.py` (en-têtes), `apprentissage_carte_v1.py` (en-têtes), `t07/plancher_v2.py`, `t06/test_croise.py`, `sondes/evaluation.py`, `sondes/temoins.py`, `t06/cout.py`, `manifeste.py`, `gardes.py` (extraits), `scripts/mots_et_cout_t06_v3.py` (code, exécuté sur données fabriquées), `prereg/T0.7-etape-B-bis-v1.md` (plan, puissance, données gardées, calcul), les deux fichiers d'essai et l'aide jouet, les règles communes.
- **Aucun fichier de résultat ni de données réelles** n'a été ouvert, ni par la chaîne ni à l'œil ; aucun registre d'état, de décisions ou de passation.
- Dossier temporaire `/tmp/claude-0/-home-user-controle-ia-travail/1829cd11-38fd-5ef8-9688-6827f39023bc/scratchpad/estimation/` : supprimé à la fin.
