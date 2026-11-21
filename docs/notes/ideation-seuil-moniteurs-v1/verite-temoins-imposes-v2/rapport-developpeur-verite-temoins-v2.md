# Rapport du développeur — programme de vérité des dix-sept témoins imposés, v2 (course « seuil et moniteurs »)

- Auteur : développeur du programme de vérité des témoins imposés, modèle O. Écrit le 2026-11-21.
- Objet : la v2 demandée par la mère, au titre de la classe B, avant le premier usage réel. Elle porte les sept points de la demande et le contrôle de la dérive de F, ajouté ensuite à la demande du vérificateur du programme de vérification. La v1 est vérifiée « Conforme, prêt à sceller » et scellée (ligne VERITE-TEMOINS-SEUIL-MONITEURS-V1, branche `verite-temoins/seuil-moniteurs-v1`, commit `564347db`) ; son fichier `calculer_verite_temoins_imposes_v1.py` (`4857343c…`) est intact dans le dossier v1. Ce rapport complète le rapport v1 (`d5385a77…`), qui reste la pièce à lire pour le moteur, les témoins et les remarques ; il ne dit que ce qui change.
- Statut : pièce de travail. La v2 attend la vérification du même vérificateur S, puis le scellement par la mère.
- Aucun appel, aucune dépense, aucune clé, aucune écriture dans un dépôt, aucun commit. Aucun refus de permission, de classifieur ni de garde. La table de vérité ne quitte pas ce dossier.

## 0. Verdict

1. Les sept points sont portés, ainsi que le contrôle de la dérive de F. Un défaut de plus, trouvé en éprouvant le plafond, est corrigé (§ 1, point 8).
2. **217 essais passent** (184 de la v1, adaptés, et 33 de plus), en 152 secondes, sous `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider test_verite_temoins_imposes_v2.py`.
3. **La table v2 est égale à la v1, sauf la forme du point 6.** Le différentiel `differentiel-table-v1-vers-v2.diff` porte trois lignes changées : le rang de T08 (entier), le décalage de T09 (arrondi à douze décimales), et la ligne `version_sortie` (v1 → v2). Aucune valeur vraie, aucune borne, aucune issue ne change.
4. **Rejeu.** La table v2, jouée deux fois, a `cmp` muet (`11008999…`). Le recalcul de l'exemple v2, joué deux fois, a `cmp` muet (`07b3124a…`). L'entrée factice v3 du programme de vérification, avec sa correspondance, jouée deux fois, a `cmp` muet (`bf6a583a…`).
5. **Sur l'entrée factice v3 dite « saine », le contrôle de dérive rend « dérive incohérente : F écartée »** : le décalage transmis n'est pas celui qui triple un taux de 1 % sous la loi transmise. C'est un constat sur la factice, non un défaut du programme ; il est à transmettre à qui écrit le programme de vérification (§ 3).

## 1. Les corrections, une par une

| point | ce qui change | lignes (programme v2) | essai | mutation de calcul |
|---|---|---|---|---|
| 1. Remarque 10, écart type | Pour « moyenne plus k écarts types », la valeur annoncée est comparée aux deux conventions (n − 1 et n). La sortie nomme `convention_qui_accorde` : `n_moins_1`, `n`, `les_deux`, `aucune` ou `indecise`. Le statut global vaut « en deçà » dès qu'une convention accorde. Les deux valeurs, leurs tenues et leurs issues sont rendues (`ecart_type_divise_par_n`), avec les puissances des deux conventions et l'accord d'issue par convention | 1287, 1458 | `test_ecart_type_deux_conventions_nommees` (760) | `deux_conventions_confondues` |
| 2. Dépassement | Une `ArithmeticError` (dont `OverflowError` et `ZeroDivisionError`), une `ValueError` ou une `RuntimeError` (non-convergence) levée sur un témoin devient un refus codé `erreur_numerique` de ce seul témoin, avec son type. Le lot continue | 1598 | `test_erreur_numerique_refusee_pour_ce_seul_temoin` (780) | `erreur_numerique_arrete_le_lot` |
| 3. Plafond de n | `N_MAX = 5000` (§ 2 bis), garde `taille_au_dela_du_plafond`, appliquée à n, à la tranche voisine, aux `tailles_de_plus` et à l'horizon du monde S | 58, 137 | `test_plafond_des_tailles` (800) | mutation de garde |
| 4. « 0 » et « 0.0 » | La forme canonique d'une loi réduit tout nombre (entier ou rationnel lu du JSON) à son rationnel. La même loi suit la même voie, exacte quand elle le permet | 442, 454 | `test_zero_et_zero_virgule_zero` (827) | `zero_et_zero_virgule_zero_separes` |
| 5. `comptes` | Ajout de `ids_ecarts_au_dela_de_0_001`, `ids_ecarts_indecis_a_la_borne`, `ids_desaccords_d_issue` et `ids_refuses`, triés | 1614 | `test_comptes_nomment_les_identifiants` (850) ; `test_recalcul_bout_en_bout_et_comparaison` | `comptes_sans_identifiants` |
| 6. Forme | Décalage de T09 arrondi ; rang de T08 en entier, lu du recalcul, qui rend lui aussi le rang en entier ; l'en-tête du test nomme les onze mutations de calcul de la v1 et les dix de la v2 | 1791, 1817 | `test_forme_de_la_table` (876), sur le JSON écrit ; `test_en_tete_compte_les_mutations` (882) | `rang_de_T08_en_rationnel`, `decalage_de_T09_non_arrondi` ; l'en-tête, texte d'essai, est contrôlé par son essai, sans mutation |
| 7. Tolérance | Resserrée, puis déclarée (§ 2) | 57, 62, 411-430 | `test_tolerance_juste` (910) | `pente_de_tolerance_nulle`, `petit_k_par_difference_de_log_gamma` |
| 8. Trouvé : rationnels de plus de 4 300 chiffres | Au-delà de n ≈ 2 150, le dénominateur exact 100^n dépasse la limite de 4 300 chiffres que Python impose à la conversion d'un entier en texte. Sans correction, un témoin à n = 5 000 serait sorti en refus « erreur numérique » alors qu'il se calcule. La limite est levée pour ce seul rendu, d'un rationnel calculé par le programme, jamais pour la lecture d'une entrée | 192 | `test_plafond_des_tailles` (cas sain au plafond) | `rationnel_exact_au_dela_de_4300_chiffres` |
| 9. Dérive de F | Contrôle de cohérence en mode recalcul (§ 3) | 1484-1580, 1920 | `test_derive_de_F_juste_fausse_et_hors_moteur` (939) ; six artefacts | `derive_dans_le_mauvais_sens` |

## 2. La tolérance (point 7)

**Mesure** (`lectures/mesurer_tolerance_v2.py`, `c1e256c7…`, sortie `mesure-tolerance-v2.txt`, `e4ace554…`). Erreur absolue de P(Bin(n, p) ≤ k) en flottants contre la valeur exacte en rationnels au même p, sur une grille : n de 200 à 5 000, k − 1 de 0 à n/2, dix valeurs de p. Même mesure pour la gamma incomplète à a = (n − 1)/2, contre une somme en décimaux à 60 chiffres.
- **v1** : la voie à petit k (k − 1 ≤ 40) calculait log C(n, j) par différence de log-gamma ; son erreur croît comme n log n et atteint 1,1 × 10⁻¹² à n = 2 000 (k − 1 = 5, p = 0,001). C'est le défaut que le vérificateur a vu.
- **Resserré** : log C(n, j) est calculé par récurrence, avec une somme compensée. L'erreur de cette voie tombe sous 6 × 10⁻¹⁴ jusqu'à 5 000. Pour k − 1 = 0 (la base, T05 et T07 de la table), le calcul redonne la v1 bit pour bit ; l'essai le vérifie.
- **Reste, voie de la bêta incomplète** (k − 1 > 40) : 4,9 × 10⁻¹³ à 1 000, 9,2 × 10⁻¹³ à 2 000, 2,8 × 10⁻¹² à 5 000. Gamma : sous 4 × 10⁻¹³.
- **Déclaré** : `tolerance_evaluation(n) = max(1e-12, 2e-15 × n)`, avec une marge d'au moins 3,6 sur la mesure jusqu'à `N_MAX`. Cette tolérance vaut 10⁻¹² jusqu'à n = 500 : les voies flottantes de la table (n ≤ 300) ne changent pas. Elle s'applique aux intégrales sur grille, aux sommes sur réseau (deux fois, par la sommation par parties), aux grappes (à leur taille totale) et à « moyenne plus k écarts types ». Elle est rendue dans la sortie du recalcul.
- La tolérance reste **déclarée, non démontrée** : une mesure sur grille n'est pas une borne.

## 2 bis. Le plafond (point 3)

`N_MAX = 5000`, pour quatre raisons :
1. Il dépasse les 2 000 que le mandat atteint, d'un facteur 2,5. Les témoins imposés vont de 200 à 1 000.
2. La tolérance déclarée est mesurée jusque-là.
3. Le coût des rationnels exacts, qui croît vite avec n, est éprouvé jusque-là dans les essais.
4. La même valeur borne l'horizon du monde S, dont la programmation dynamique exacte coûte de l'ordre de l'horizon au carré.

## 3. Le contrôle de la dérive de F (point 9)

**Appel.** `python3 -I -B calculer_verite_temoins_imposes_v2.py --recalculer TEMOINS_JSON SORTIE_JSON --correspondance CORRESPONDANCE_JSON`. Sans `--correspondance`, la sortie dit `derive_de_F : {"statut": "non_transmise"}`, jamais un silence.

**Entrée.** Le programme lit le bloc `derive_de_F` de la correspondance du programme de vérification v3. Sa forme est celle de `entree-recalcul-factice-saine-v3.json.correspondance.json` (`c35c4bc3…`, lue par chemin complet ; l'entrée factice elle-même, `bb571948…`, ne porte pas ces champs) :
- `valeur_transmise` : texte décimal, ou nombre ;
- `loi_de_la_tranche` : texte JSON d'une loi de la grammaire, ou objet ;
- `rang_de_la_cle` ;
- `tranche_associee_a_T09` : `n_calibration_contient_299` doit valoir vrai ;
- `controle`, facultatif : s'il est présent, il doit dire 3 % à 0,001 près ;
- `statut` : si ce n'est pas « lue », le contrôle n'est pas fait, et c'est dit.

**Calcul.** Sous la loi F de la tranche, s est le seuil dont le taux vrai est 1 % avant la dérive. La dérive translate la loi de d = δ × écart type de F, la convention du type `decalage`. Le taux vrai après la dérive est P_F(X > s − d), et il doit valoir 3 % avec une tolérance absolue de 10⁻³. Le calcul est encadré : s est cerné par dichotomie, la tolérance d'évaluation s'y ajoute. Seul δ = 0 se rend exact. Aucune autre loi du moteur ne donne ici un rationnel exact (par exemple, pour Laplace, le taux vaut 0,01 eᵈ).

**Sortie** (`derive_de_F` dans la sortie du recalcul) :
- le verdict : « dérive cohérente », « dérive incohérente : F écartée », ou `indecise_a_la_borne` si l'encadrement chevauche la tolérance ;
- le taux calculé avec sa borne ;
- le décalage transmis et, pour information, le décalage qui triple sous cette loi ;
- la loi, le rang et la tranche ;
- l'accord de la loi de lecture de T09 dans l'entrée avec la dérive transmise.

Une loi hors moteur, une loi sur réseau ou en grappes, ou un bloc mal formé donne un refus codé dans ce bloc ; le lot de témoins continue.

**Essais** (939) :
- décalage juste sous une normale (taux 3 %, « cohérente ») ;
- décalage juste sous Laplace, où δ = ln 3 / √2 donne exactement 3 % ;
- décalage faux, 0,5 (« incohérente : F écartée ») ;
- δ = 0 par la voie exacte ;
- loi hors moteur (`couple` : refus `loi_hors_moteur`, le lot continue) ;
- sans correspondance ;
- de bout en bout en ligne de commande, avec l'accord à T09.

Les six gardes neuves ont chacune leur artefact et leur mutation de garde. La mutation de calcul `derive_dans_le_mauvais_sens` est détectée.

**Sur la factice v3** : « dérive incohérente : F écartée » (`sortie-recalcul-factice-v3-avec-correspondance-v2.json`). La dérive transmise est bien celle de la lecture de T09 dans l'entrée (accord vrai), mais elle ne triple pas le taux sous la loi transmise.

## 4. Différentiels

| différentiel | sha256 | contenu |
|---|---|---|
| `differentiel-table-v1-vers-v2.diff` | `173d45ba…` | trois lignes changées : rang de T08, décalage de T09, version |
| `differentiel-programme-v1-vers-v2.diff` | `e7eb84b0…` | les neuf points du § 1 et l'en-tête |
| `differentiel-essais-v1-vers-v2.diff` | `5bf975a6…` | en-tête, chemin v2, deux adaptations (rang en entier, `comptes`), les artefacts, les essais et les mutations de la v2 |

## 5. Comptes

| famille d'essais | v1 | v2 |
|---|---|---|
| cas sains, table, accord avec la note, registre des gardes | 45 | 45 |
| artefacts refusés, un par garde | 64 | 71 |
| mutations de garde | 64 | 71 |
| mutations de calcul | 11 | 21 |
| essais des corrections de la v2 | — | 9 |
| **total** | **184** | **217** |

Toutes les mutations sont détectées. Gardes : 71, dont sept neuves (le plafond, et six pour le contrôle de dérive).

## 6. Réserves

1. La v2 n'est pas encore vérifiée.
2. La sortie du **recalcul** change de forme : comparaison à deux conventions pour « moyenne plus k écarts types », `rang_k_ieme_plus_grand` en entier hors de `quantites`, nouvelles clés de `comptes`, d'en-tête et `derive_de_F`. Le format d'**entrée** des témoins ne change pas et garde sa version `recalcul-temoins-seuil-et-moniteurs-v1`. La correspondance est un second fichier facultatif.
3. L'en-tête de la table garde `tolerance_evaluation_declaree: 1e-12`, qui reste juste pour la table (voies flottantes à n ≤ 300). La part qui croît avec n est déclarée dans le programme et dans la sortie du recalcul, pour que le différentiel reste réduit au point 6.
4. Le refus `erreur_numerique` couvre trois familles d'erreurs sous un même code ; le type de l'exception est dans la raison.
5. Le contrôle de dérive prend la translation de la loi entière, conformément au type `decalage` et à la lecture de T09 dans le rapport v1 (remarque 4). Une loi pour laquelle « moyenne décalée » ne serait pas une translation n'est pas prévue.
6. Un premier jeu des sorties v2, produit avant le contrôle de dérive, est rangé sans destruction sous `lectures/premier-jeu-avant-controle-de-derive/`. Sa table est égale à l'octet à la table finale. Ce n'est pas un livrable. `lectures/essai-table-v2-1.json` est un essai de même contenu.
7. Les remarques du rapport v1 valent encore, sauf la dixième, portée ici ; la cinquième réserve de la v1 (forme) est levée.

## 7. Fichiers et empreintes

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-verite-temoins-mondes-v2/`. Table : `table-empreintes-verite-temoins-v2.txt` ; un compagnon `.sha256` par fichier livré.

| fichier | sha256 |
|---|---|
| `calculer_verite_temoins_imposes_v2.py` | `bcd7fbacc38da278adb99be6417237fb66c00bfbebafcdca8afa20b261cbe9a3` |
| `test_verite_temoins_imposes_v2.py` | `957b37173311dc9d8852c9ca7596561d122e09aee32b76b5b6c349d9cd69678d` |
| `table-verite-temoins-imposes-v2.json` | `11008999625bb5311927f17b2a1a85c2a7464b4f9e4390ba36e7f8659d67ab31` |
| `table-verite-temoins-imposes-v2-rejeu.json` | `11008999625bb5311927f17b2a1a85c2a7464b4f9e4390ba36e7f8659d67ab31` |
| `differentiel-table-v1-vers-v2.diff` | `173d45ba4cd9d020740e92e224761b6c8486e293c1ba52dba0bb46bcaab6e590` |
| `differentiel-programme-v1-vers-v2.diff` | `e7eb84b00d6da672437370cba5f77cb13b0b0674726193e4bec46f1a3d21c65a` |
| `differentiel-essais-v1-vers-v2.diff` | `5bf975a68f39037468fabc075a518cbe7c42659a03f4a02108e9210991ff540a` |
| `exemple-entree-recalcul-v2.json` | `70ab2055032e8634d084e8d5cb664593dad3d62e9fd8cc26950d22231f0b808e` |
| `exemple-sortie-recalcul-v2.json` | `07b3124a9c757a62d601f42b19394a6d7a48e41debc7d8e003237a6dc5f0e118` |
| `exemple-sortie-recalcul-v2-rejeu.json` | `07b3124a9c757a62d601f42b19394a6d7a48e41debc7d8e003237a6dc5f0e118` |
| `sortie-recalcul-factice-v3-avec-correspondance-v2.json` | `bf6a583abba1c9a81b1e64eff813ed9d4e052ec6190f5db24c23e13b7b8b8202` |
| `sortie-recalcul-factice-v3-avec-correspondance-v2-rejeu.json` | `bf6a583abba1c9a81b1e64eff813ed9d4e052ec6190f5db24c23e13b7b8b8202` |
| `mesure-tolerance-v2.txt` | `e4ace55406e3cbf97468dd1490121d65e56aa3e2224b868922ca2d6cc20610a4` |
| `lectures/mesurer_tolerance_v2.py` | `c1e256c73ea52c0fd9d4dfbd56600635aafa431a87f4f81f1ad08a56d8a70541` |

développeur du programme de vérité des témoins imposés, modèle O
