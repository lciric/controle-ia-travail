# Rapport du développeur — programme de vérification de la sortie de l'auteur des mondes plantés (course « seuil et moniteurs ») — v2

- Auteur : développeur du programme de vérification de la sortie des mondes, modèle O. Écrit le 2026-11-21.
- Version : la v2 **complète** le rapport v1 (`6c00779db5a86f983eccbc882376fe55b2f067d5fdcffc7ffaab53c58eb3bb1c`, gardé intact). Elle ne dit que ce qui change ; pour la correspondance de chaque règle du § 6 aux codes, voir le rapport v1, § 2 (codes inchangés, sauf ceux nommés ici).
- Causes, toutes relayées par le coordinateur :
  - le mot de la mère de 09:10Z (motifs de clé alignés sur le lanceur v9) ;
  - la vérification du vérificateur S, `docs/notes/ideation-seuil-moniteurs-v1/programme-verification-sortie-mondes-v1/verification-v1/verification-programme-verification-sortie-mondes-v1.md` (`8bdf5f4ff5af08f935687e2236e28f6b85791c28ec1cad4628a65fb4bf39637f`, égale à son compagnon, lue en entier), verdict « À corriger » (C1, C2, C3, N2) ;
  - le mot de la mère de 09:15Z (correspondance vers le recalcul) ;
  - l'erratum 1 du mandat v3, pour ses deux valeurs seulement (borne de taille finale 52 000, plafond de 40 témoins) ;
  - la remarque 14 du vérificateur de la vérité (identifiants réservés).
- Statut : instrument (classe B), **non contre-lu**. Aucun appel, aucune dépense, aucune clé, aucun commit.

## 0. Verdict

1. Les sept branches du motif de valeur de clé du lanceur v9 sont prises au moins aussi largement que dans le lanceur. Les motifs plus larges de la v1 sont gardés. Chaque prise reste étiquetée « chaîne en forme de clé ».
2. C1, C2, C3 et N2 sont portés, chacun avec ses essais et sa mutation.
3. Les deux constantes sont portées : borne de taille `TAILLE_MAX_CARACTERES = 52000` et plafond `TEMOINS_MAX = 40`, chacune à un seul endroit.
4. Les identifiants T01 à T17 sont réservés aux témoins imposés (point 2).
5. **Mode neuf `--vers-recalcul`** : il transforme une sortie lisible en l'entrée du mode `--recalculer` du programme de vérité des témoins. Sur la sortie factice rendue convertible, les 39 témoins sont convertis. Le programme de vérité les accepte tous : 39 calculés, aucun refus.
6. **290 essais, tous passés** (Python 3.13). Toutes les mutations de la v1 sont rejouées, et 102 mutations en tout sont tuées.

## 1. Pièces lues (en plus de celles du rapport v1)

| pièce | empreinte | lecture |
|---|---|---|
| lanceur v9 `/home/user/controle-ia-travail-organisme/scripts/lancer_course_auto_conception_v9.py` | `1b47c1cf097e4cba290223223655d5ac63707dfeaec032be929930d30fde9b12` (compagnon) | lignes 525 à 554 seulement : `MOTIF_VALEUR_DE_CLE` |
| vérification S de la v1 | `8bdf5f4f…39637f` (compagnon) | en entier |
| exemple d'entrée du recalcul `…/dev-verite-temoins-mondes/exemple-entree-recalcul-v1.json` | `76ed336e7c1108f7aadf8b8d197f5e2128e70ebff77dc7bceedc595e205b9495` (compagnon) | en entier |
| programme de vérité `…/dev-verite-temoins-mondes/calculer_verite_temoins_imposes_v1.py` | `4857343c3388e5045a49dd690d661b3fb2069949691af079f3db21e2db58bf59` (compagnon) | pour le seul format d'entrée : en-tête, lois admises (l. 661 à 745), recalcul (l. 1089 à 1395), lecture et écriture (l. 1664 à 1706). Je n'ai pas lu ses lois de référence (l. 1398 et suivantes) |

Non lus, comme demandé : `table-verite-temoins-imposes-v1.json` et le rapport du développeur de la vérité. Le texte de l'erratum 1 du mandat v3 n'est pas lu non plus : je n'en ai pas le chemin. Ses deux valeurs viennent des mots relayés.

## 2. Motifs de clé alignés sur le lanceur v9 (`MOTIFS_DE_CLE`, l. 234 à 247)

| branche du lanceur | motif de la v2 | aussi large ? | artefact (chaîne inventée, à la longueur minimale, collée à des lettres) |
|---|---|---|---|
| préfixe `s[k]-`, segment de trois lettres, tiret, un caractère | `prefixe_sk_segment` : `s[k]-` puis 1 à 32 alphanumériques, tiret, un alphanumérique | oui : le segment du lanceur en est un cas | `lanceur_sk_segment` (segment inventé « qrs ») |
| `s[k]-` puis 20 alphanumériques ou plus | `prefixe_sk` : 16 ou plus, avec `_` et `-` admis | oui | `lanceur_sk_20` |
| `g[h]p_` puis 20 ou plus | `prefixe_gh` : `g[h][pousr]_`, 20 ou plus | oui | `lanceur_gh_20` |
| `h[f]_` puis 20 ou plus | `prefixe_hf` (neuf) | égal | `lanceur_h_f_20`, `cle_dans_une_cle_libre` |
| `A[K]IA` puis 12 | `prefixe_akia` : `A[K]IA` ou `A[S]IA`, puis 12 ou plus | oui | `lanceur_a_k_12` |
| `A[I]za` puis 20 ou plus | `prefixe_aiza` : 20 ou plus | égal | `lanceur_aiza_20` |
| `Bearer`, blancs, 16 ou plus | `porteur` : sans casse, avec `=` admis | oui | `lanceur_porteur_16` |

- **Frontières de mot.** Elles sont retirées de tous les motifs à préfixe : le lanceur n'en demande aucune, et un motif à frontière est plus étroit que lui. `affectation_de_secret` garde la sienne : ce n'est pas une branche du lanceur.
- **Essai de parité** `test_parite_avec_le_lanceur[0..6]`. Il lit `MOTIF_VALEUR_DE_CLE` dans le lanceur, après contrôle de son empreinte, et vérifie qu'il a sept branches. Pour chaque branche, il fabrique à l'exécution la plus courte chaîne qu'elle prend. Il vérifie que le lanceur la prend, puis que le programme la prend par un motif à préfixe. Le segment littéral de la première branche n'est donc **jamais écrit** dans mes fichiers : il est lu dans le lanceur au moment de l'essai.
- **Mutations.** Une par motif de clé (13, la chaîne longue et mêlée comprise) : le motif est réécrit pour ne plus rien prendre, et chaque artefact de ce motif doit échouer. Chaque artefact de clé nomme le motif qui doit le prendre.
- **Comment j'écris les préfixes.**
  - Dans le programme, chaque préfixe s'écrit avec une classe d'un seul caractère : `s[k]-`, `g[h][pousr]_`, `h[f]_`, `A[K]IA`, `A[S]IA`, `A[I]za`, `githu[b]_pat_`, `xo[x]`, `e[y]J`, `PRIVATE[ ]KEY`.
  - Dans les essais, les chaînes sont composées par concaténation (« `"g" + "hp_"` », « `"h" + "f_"` », « `"AK" + "IA"` »). Les noms d'artefacts sont écrits sans préfixe en clair (`lanceur_h_f_20`, `lanceur_a_k_12`).
  - Une recherche des préfixes en clair dans le programme, les essais et ce rapport ne trouve rien. Seul le différentiel du programme garde, en lignes retirées, quatre expressions de la v1 qui écrivaient leurs préfixes en clair (lignes 83, 85, 87, 89 du différentiel). Chacune y est suivie d'un crochet ou d'une parenthèse, jamais d'une suite de caractères en forme de clé, et elles étaient déjà dans la v1 versée telle quelle.

## 3. Corrections de la vérification S

| point | ce qui change | lignes | essais | mutation |
|---|---|---|---|---|
| C1 | `parcourir` devient itératif (même ordre) ; une RecursionError de l'analyseur JSON n'est plus dite « illisible » ; toute exception imprévue dans `principal` rend le code 3, sans rapport, sans trace ni texte de la sortie | 1050, 413 à 418, 1642 | `imbrication_995` (lisible, code 0), `imbrication_trop_profonde` (code 3), `test_exception_imprevue_sans_trace_de_la_sortie` | `C1_parcours_recursif_de_la_v1`, `C1_garde_d_exception_retiree` |
| C2 | un `mode` autre que la chaîne `exacte` (nul, vide, absent, autre texte) écarte la famille ; `expression` n'est exigée que d'une vérité exacte ; une `verite` qui n'est ni objet ni nulle reste une faute de forme ; une `valeur_vraie` nulle reste illisible (mot de la mère sur la v1) | 640 | `verite_mode_nul`, `verite_mode_vide`, `verite_sans_mode`, `verite_non_exacte_sans_expression` (écartées, code 0) ; `verite_en_liste`, `verite_exacte_sans_expression`, `verite_exacte_expression_nombre`, `cle_en_trop_verite_non_exacte`, `valeur_vraie_nulle` (illisibles) | `C2_verite_stricte_de_la_v1` |
| C3 | `budget_b_propose` admis en fraction (0.05), en pour cent (5) et en chaîne (« 5 % », « 5% », espace insécable admise) ; observation `O_BUDGET_HORS_FORME_FRACTION` hors fraction ; hors des cinq valeurs, toujours une faute | 731, 811 | `budget_en_pour_cent`, `budget_chaine_avec_espace`, `budget_chaine_collee`, `budget_chaine_espace_insecable` ; fautes : `budget_hors_liste`, `budget_sept_pour_cent`, `budget_chaine_hors_liste`, `budget_chaine_sans_pour_cent` | `C3_budget_en_fraction_seule`, et celle du code d'observation |
| N2 | la normalisation replie U+2010 à U+2015, U+2212, U+FE63, U+FF0D en « - » | 249, 343 | `nom_de_modele_trait_insecable`, `nom_de_modele_tiret_cadratin` | `N2_tirets_non_replies` |

## 4. Erratum 1 : borne et plafond

- `TAILLE_MAX_CARACTERES = 52000` (l. 61), borne finale tranchée par la mère. Elle est lue à un seul endroit et rendue dans le rapport (`sortie_auteur.borne_caracteres`). Essais : `taille_juste_au_dessus` (52 001 caractères, illisible) et `taille_a_la_borne` (52 000, lisible). Mutations : la borne relevée à 62 000, puis baissée à 51 999.
- `TEMOINS_MAX = 40` (l. 66). Il compte ensemble les témoins de tête et ceux du bloc `a_l_ecart`. L'observation s'appelle désormais `O_TEMOINS_AU_DELA_DU_PLAFOND` (l. 1010) ; c'est l'ancienne `O_PLUS_DE_VINGT_HUIT_TEMOINS`, même garde. Essais : `temoins_au_plafond` (40, aucune observation) et `temoins_au_dela_du_plafond` (41, observation). Mutations : le plafond relevé à 41, puis baissé à 39. La sortie factice saine compte 39 témoins et ne porte plus aucune observation.
- **Classement du dépassement : remarque, sans trancher.** Le § 6 du mandat v3 ne range le plafond de témoins à aucun de ses points 1 à 5, et je n'ai pas lu le texte de l'erratum. Le dépassement reste donc une **observation**, qui ne rend pas la sortie illisible (rectificatif du coordinateur).

## 5. Identifiants réservés (remarque 14 du vérificateur de la vérité)

- Code `P2_IDENTIFIANT_IMPOSE_RESERVE` (l. 930, 934). Il vise tout témoin du bloc `a_l_ecart` qui porte un identifiant de T01 à T17, et tout second porteur, en tête, d'un tel identifiant.
- Essais : `libre_nomme_t05_en_tete` et `libre_nomme_t07_a_l_ecart` ; `t05_a_l_ecart` porte désormais aussi ce code. Mutation par code.
- **Lettre** : le § 3.1 donne ces identifiants aux témoins imposés sans les réserver en toutes lettres, et rien ne les permet à un témoin libre. Je suis la demande, et je le dis ici.

## 6. Correspondance vers l'entrée du recalcul (`--vers-recalcul`, l. 1300 à 1580)

`python3 -I -B verifier_sortie_auteur_mondes_v2.py --vers-recalcul SORTIE_AUTEUR ENTREE.json [--motifs LISTE]`

- **Ce que le mode fait.**
  - Il juge d'abord la sortie. Si elle est illisible : code 2, rien n'est écrit.
  - Sinon, il écrit `ENTREE.json` au format exact de l'exemple : `version_entree` et `temoins`, chaque témoin avec ses clés obligatoires, `lois` (calibration, lecture, saboteurs, voisine) et, selon le cas, `suite`, `tailles_de_plus`, `valeur_annoncee`, `issue_annoncee`.
  - Il écrit aussi `ENTREE.json.correspondance.json` : témoin par témoin, converti ou non, la raison `NC_…` et les choix `CH_…` appliqués. Un témoin du bloc à l'écart y est désigné par son chemin seulement.
  - Les nombres sont réécrits avec leur texte brut, parce que le programme de vérité lit les décimaux en rationnels exacts. Les entiers écrits `300.0` sont rendus entiers.
  - Le mode n'écrase jamais un fichier ; une exception imprévue rend le code 3, sans rien écrire. Il ne calcule aucune valeur.
- **Les trois trous de la lettre** relevés par le développeur de la vérité, chacun réglé par un choix nommé :
  - **pas de champ « tranche » sur un témoin** : `CH1_TRANCHE_PAR_TAILLE`. La tranche de lecture est la première tranche dont `n_calibration` contient le `n` du témoin, à défaut la première. Pour « plus grand de la tranche voisine » : `CH1B_TRANCHE_VOISINE_SUIVANTE`, la tranche suivante (circulairement), avec sa première taille ;
  - **quelle composante est « l'honnête qui échoue »** : `CH2_ECHEC_PAR_POIDS_EGAL_A_P_ECHEC`. C'est la composante du mélange dont le poids égale exactement `p_echec` ; « l'honnête qui réussit » est l'autre, s'il n'y en a qu'une. Sinon le témoin n'est pas converti : `NC_COMPOSANTES_AMBIGUES`, ou `NC_PAS_DE_COMPOSANTE_D_ECHEC` si la loi n'est pas un mélange ou si `p_echec` est nul ;
  - **la loi du signal somme du monde M n'est pas donnée** : un témoin sur `somme` n'est pas converti (`NC_SIGNAL_SOMME_SANS_LOI`).
- **Autres choix nommés**, que la lettre ne fixe pas non plus :
  - `CH4` : les trois `populations` du monde M dans l'ordre du § 3.3 (réussit, échoue, saboteur). Une loi de signal qui n'est pas une loi de la grammaire n'est pas convertie (`NC_LOI_DU_SIGNAL_HORS_FORME`) ;
  - `CH10` : l'honnête du monde M est le mélange (1 − P(échec), P(échec)) des deux populations honnêtes ;
  - `CH5` : un saboteur par aire, nommé `aire_0_69`, `aire_0_80` ou `aire_0_95`, lu comme le décalage de la loi honnête de la tranche, de `decalages[i]` écarts types. Il n'est donné que pour T05, T07 et la grandeur `puissance` ; `CH6` : pour cette grandeur, le seul saboteur `aire_0_80` ;
  - `CH7` : la dérive de F n'a pas de champ dans la forme fixe. Elle est lue dans `valeurs_de_plus` de T09, sous la seule clé numérique dont le nom dit « decalage » ou « derive », et appliquée en décalage de la loi de lecture à tous les témoins de F. Sans elle, et pour toute autre famille qui casse « aucune dérive », le témoin n'est pas converti (`NC_DERIVE_SANS_CHAMP`) ;
  - `CH8` : une famille en grappes se lit sur la normale réduite (variance 1, § 3.2, H) ; `CH8B` : T10 et T11 prennent les tailles de famille du § 3.1 (3 × 100, 30 × 10) ; `CH8C` : un entier m de `tailles_de_famille` se lit « n / m familles de m », sinon `NC_TAILLES_DE_FAMILLE` ;
  - `CH9` : T07 porte `tailles_de_plus: [400]` (§ 3.1) ;
  - une loi `autre` n'est pas convertie (`NC_LOI_AUTRE`) : elle est à lire par une personne.
- **Témoins des familles écartées** : ils sont convertis quand même ; le compte rendu redit les écarts de la vérification.
- **Essais.**
  - `test_correspondance_acceptee_par_le_programme_de_verite` porte sur la sortie factice rendue convertible : `valeurs_de_plus` de T09 avec un décalage, lois de la grammaire pour le signal « valeur » du monde M. Résultat : 39 convertis. Le programme de vérité, lancé par `python3 -I -B … --recalculer`, sort en code 0, avec 39 témoins calculés et aucun refus, de forme ou autre. L'essai ne lit que les statuts et les codes, jamais une valeur, et efface la sortie du programme de vérité.
  - `test_correspondance_de_la_sortie_saine_telle_quelle` : 34 convertis, 5 non convertis (T09, LF1, LF2 pour la dérive ; LM1, LM2 pour le signal).
  - Un essai par code `NC_…` (7), chacun avec sa mutation (la ligne `raise` remplacée par `pass`).
  - Le refus d'une sortie illisible et l'exception imprévue, chacun avec sa mutation ; le refus d'écraser ; les choix déclarés.
  - Fichiers rendus sur la sortie factice saine telle quelle : `entree-recalcul-factice-saine-v2.json` et son compte rendu.

## 7. Comptes

- **290 essais, tous passés.**
- **Artefacts : 146.**
- **Mutations : 102**, toutes tuées :
  - 71 par code. Ce sont les 69 de la v1, toutes rejouées (l'une sous son nom neuf, `O_TEMOINS_AU_DELA_DU_PLAFOND`), plus `O_BUDGET_HORS_FORME_FRACTION` et `P2_IDENTIFIANT_IMPOSE_RESERVE` ;
  - 13 par motif de clé ;
  - 9 par correction : C1 deux fois, C2, C3, N2, borne deux fois, plafond deux fois ;
  - 7 par code `NC_…` ;
  - 2 gardes de la correspondance.
- **Autres essais : 42.** Ils comprennent 7 essais de parité, celui des sept branches, 7 artefacts de la correspondance, la couverture des codes et des motifs, les erreurs d'usage et le cas sain.

## 8. Ce que la lettre ne fixe pas (remarques neuves ; celles du rapport v1, § 3, valent encore, sauf la 15 et la 20)

1. **Remarque 15 de la v1, remplacée par C3** : le budget s'admet aussi en pour cent et en chaîne.
2. **Remarque 20 de la v1, remplacée par l'erratum** : plafond de 40, tous témoins comptés. Le classement du dépassement n'est pas dans le § 6 : il reste une observation (§ 4).
3. **Une RecursionError de l'analyseur JSON** (objet trop profond, valide mais illisible pour la bibliothèque standard) rend le code 3, « rien n'est jugé », et non « illisible ».
4. **Réserve des identifiants** T01 à T17 : la lettre ne la dit pas ; je l'applique sur demande (§ 5).
5. **Correspondance** : les choix `CH1` à `CH10` et les codes `NC_…` du § 6. Chacun est une lecture de développeur, à confirmer par la mère et par le développeur de la vérité. En particulier : `CH7` (dérive lue dans T09), `CH2` (composante d'échec par son poids), `CH5` (unité des décalages du saboteur : écarts types de la loi honnête).
6. Le préfixe à segment est généralisé à tout segment de 1 à 32 alphanumériques. Il peut prendre un mot anglais composé (`risk-free-a`) ; une telle prise donne le code 1, jamais « illisible ».

## 9. Commandes

Dossier : `D=/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-verification-sortie-mondes-v2`, une commande par appel.

- Essais : `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=$D/essais-tmp $D/test_verifier_sortie_auteur_mondes_v2.py`. Attendu : 290 passés. L'essai d'acceptation lance le programme de vérité, d'empreinte vérifiée, sur l'entrée factice seulement.
- Avant l'envoi : `python3 -I -B $D/verifier_sortie_auteur_mondes_v2.py $D/sortie-factice-saine-v1.json RAPPORT_NEUF.json --motifs LISTE_REELLE`. Attendu : code 0, aucune observation.
- À la réception :
  - vérification : `python3 -I -B $D/verifier_sortie_auteur_mondes_v2.py SORTIE_RECUE.json RAPPORT_RECEPTION.json --motifs LISTE_REELLE` ;
  - puis, si la sortie est lisible : `python3 -I -B $D/verifier_sortie_auteur_mondes_v2.py --vers-recalcul SORTIE_RECUE.json ENTREE_RECALCUL.json --motifs LISTE_REELLE` ;
  - puis le mode `--recalculer` du programme de vérité sur `ENTREE_RECALCUL.json`.

## 10. Réserves

1. Programme, essais et correspondance ne sont pas contre-lus.
2. L'essai d'acceptation a fait calculer au programme de vérité des valeurs sous les lois factices. Je ne les ai ni lues ni recopiées, et le fichier est effacé par l'essai. Les sorties de la correspondance, l'entrée factice et son compte rendu ne portent que des remplissages et des lois recopiées.
3. **Fichier hors de mon dossier.** Une recherche faite par l'outil a parcouru le dossier temporaire des essais ; l'outil a alors déposé sa longue sortie, de lui-même, sous `/root/.claude/projects/…/tool-results/`. Je n'y ai rien écrit moi-même ; ce fichier ne contient que des chemins et des lignes d'essais à chaînes inventées.
4. Les fichiers inchangés gardent leur nom et leur empreinte v1 : `fabriquer_sorties_factices_v1.py`, `motifs-noms-refuses-essai-v1.txt`, `sortie-factice-saine-v1.json`.

développeur du programme de vérification de la sortie des mondes, modèle O
