# Module final de l'addendum de lecture complémentaire de P3 (v1) — notes de synthèse

Texte qui fait foi : brouillon 3 (`addendum-p3/P3-addendum-lecture-complementaire-v1-brouillon3.md`). Base : candidat « b »
(module `8f2410f5…6dc9`, tests `7a3684e1…1e25`, empreintes vérifiées). Les deux candidats avaient été écrits sur le
brouillon 1 : l'alignement sur le brouillon 3 a demandé une réécriture large (table des conclusions, forme de la sortie,
gardes 1 à 11, A2 (b), A4 (b), A5, A6, A7, A8, synthèse). Rien n'a été écrit hors de ce dossier. Le dépôt de travail n'a
pas été touché.

## Fichiers

| fichier | sha256 | rôle |
|---|---|---|
| `complements_p3_v1.py` | `daf954594456f8c268ebbf48b14326a183941c00c4cddb205b2e3382a875f4fa` | module (2 080 lignes) |
| `test_complements_p3_v1.py` | `01b5faeaf1fe5ea38624b872948d46d5310bc67b6df3277ea1515e73fc057abc` | tests (117) |
| `essais/` | — | hors livrable : banc de durée, mutants, essai rapide, journaux |

Nombre de tests : **117** (95 fonctions, dont deux paramétrées : 16 artefacts et 8 analyses). Le nombre est écrit en tête
du fichier de tests ; `test_nombre_de_tests_ecrit_en_tete` le vérifie quand le fichier est lancé en entier. À reporter
dans le préenregistrement : `<<EMPREINTE_MODULE>>`, `<<EMPREINTE_TESTS>>` (empreintes ci-dessus, après versement sous
`docs/procedures/P3-addendum-v1/`, fichiers inchangés) et `<<NOMBRE_TESTS>>` = 117.

Lancement des tests : `PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1 python -m pytest -q -p no:cacheprovider
docs/procedures/P3-addendum-v1/test_complements_p3_v1.py`. Durée : environ 10 minutes sur un cœur.

## 1. Chaque section du brouillon 3 et la fonction qui l'applique

| section du brouillon 3 | fonction(s) |
|---|---|
| En-tête : empreintes du module et des tests, lues dans le texte | `EMPREINTE_MODULE_CITEE`, `EMPREINTE_TESTS_CITEE`, `exiger_garde_1` |
| Statut non décisif | `STATUT` ; `creer_manifeste(…, decisif=False)` dans `executer` ; `exiger_verrou` |
| Hypothèse G-01 à G-09 | `_a1` à `_a9` (une fonction par analyse, table `FONCTIONS`) |
| Prédiction chiffrée (signe attendu, lu sur la borne basse) | condition `contraire` de chaque `e.controle(…)` dans `_a1` à `_a8` |
| Métrique, entrées | `lecture.charger_source` et `charger_textes` (garde 4) ; `verifier_resultat` ; `lire_la_lecture` (clés lues, liste fermée) |
| Actions notées | `_donnees` (scores tous finis, comme `lecture.py` l. 250) |
| Aire vectorisée | `aires_par_rangs`, `_aires` (égales à `aire_sous_courbe` et `aire_stratifiee` à 1e-12, test) |
| Score d'empan, jamais de moyenne des jetons | `agreger_par_jeton` dans `localisation`, `fenetres_de_meme_longueur` ; `jeton_dominant` (A8) |
| Famille « attention » contre `agregation` | `familles_attention` (garde 10) |
| Rééchantillonnage, dégénérescence, 1 % | `_tirages`, `_exiger_degeneres`, `verifier_parametres_tirage` ; fonctions gelées pour les autres |
| Graines `addendum/<analyse>/<sonde>/<objet>` | `cles_addendum` (69 clés, dans le manifeste), `exiger_graines`, `_rng` |
| Table fermée des niveaux | constantes `NIVEAU`, `NIVEAU_BONFERRONI` ; niveau du jeu lu dans la lecture pour A7 (ii) |
| Forme de la sortie (`descriptif`, `controles`, `cible`, `controle_contraire`) | `_Entree` (`calcul`, `controle`, `sortie`), `_executer_entree`, `_sans_cles_interdites` |
| A1 | `_a1`, `ecart_conjoint` (aire simple ; T4 en tranches « figees »), placebo conjoint en descriptif |
| A2 | `_a2`, `localisation`, `_saboteur_honnete`, `aire_du_cout` (a), `fenetres_de_meme_longueur` et `difference_fenetres` (b), (c) et (d) en descriptif |
| A3 | `_a3`, `contrastes` |
| A4 | `_a4` ; (a) `ecart_conjoint(…, "internes")` ; (b) `t1_intra_tache` (`ecart_conjoint(…, "par_copie")`) ; (c) `etiquettes_gonflement_reference`, `reference_geometrique`, `t1_sensibilite` |
| A5 | `_a5`, `relire_textes`, `regle_bornes_champs` (1), `regle_lire_action` et `_vers_brut` (2), `_divergentes`, `regle_de_sensibilite` (descriptif), `t2_propre` |
| A6 | `_a6`, `cout_lecteur_etendu`, `_effet` |
| A7 | `_a7` ((i) marge, (ii) `_forme_restreinte`, (iii) `longueur_champ_cout`) |
| A8 | `_a8`, `a8_dominants`, `jeton_dominant`, `segment_du_rang` |
| A9 | `_a9`, `a9_trajectoires` |
| Seuil : effectif minimal, table des réserves | `_exiger_effectif` (`NonCalculable`) ; nom de réserve de chaque contrôle ; `reserve_<analyse>_non_lue` dans `_Entree.controle` |
| Plan 1 : histoire complète | `exiger_anteriorite` (dépôt non superficiel) |
| Plan 2 : commande | `_main`, `exiger_commande` |
| Plan 3 : gardes 1 à 9 avant le manifeste | `executer` (ordre écrit) |
| Plan 4 : manifeste, configuration, sortie unique | `executer` : configuration `{"run_source", "run_lecture"}`, `ecrire_resultat(…, "lecture-addendum-p3", …)` |
| Plan 5 : verrou mécanique | `conclusions_etablies`, `cibles_possibles`, `_Entree.controle` (« sans objet »), `exiger_verrou`, `CLES_INTERDITES`, `DefautDuModule` |
| Plan 6 : synthèse | `synthese` (`reserves_addendum`, `nombre_de_controles`, `nombre_de_reserves`, `audit_symetrie_addendum`, `recommandation_au_verdict_R13`) ; `issue_primaire`, `conclusions_etablies` dans `analyser_addendum` |
| Plan 7 : recalcul de l'issue et des états | `exiger_issue_recalculee` (garde 6) |
| Plan 8 : multiplicité | `nombre_de_controles` à côté de `nombre_de_reserves` |
| Plan 9 : durée | mesurée, voir § 6 |
| Critères : verrou unidirectionnel | `exiger_verrou` ; instantané canonique de toute la lecture pris à l'entrée, comparé à la fin |
| Critères : audit de symétrie de l'addendum | `synthese` (`audit_symetrie_addendum`) |
| Liste d'arrêt, garde 1 | `exiger_garde_1` |
| garde 2 | `exiger_lecture_decisive` (avec `exiger_run_source_decisif`, `lecture.exiger_lecture_sous_prereg`, unicité) ; cohérence par le calcul `exiger_coherence` |
| garde 3 | `exiger_anteriorite` |
| garde 4 | `lecture.charger_source`, `charger_textes`, `verifier_resultat` |
| garde 5 | `exiger_textes_alignes` |
| garde 6 | `exiger_issue_recalculee` |
| garde 7 | `lire_la_lecture` ; entrées en échec ou non calculables : `_etat_entree` → « non lu » |
| garde 8 | `exiger_constantes_gelees` |
| garde 9 | `exiger_premier_passage` |
| garde 10 | `familles_attention` |
| garde 11 | `synthese` (réserve générale `reserve_addendum_largement_non_lu`) |
| Seule `GardeArret` donne « échec » | `_Entree.calcul`, `_executer_entree` ; toute autre exception traverse ; dans `executer`, l'arrêt après le manifeste est écrit puis propagé |
| Tests (liste fermée) | § 5 |

## 2. Ce qui vient de quel candidat

- **b (base)** : aires par rangs vectorisées ; plancher conjoint (`ecart_conjoint`) ; contrastes de A3 ; étiqueteur à
  référence géométrique par `cout_de_tache` ; lecteur étendu des coûts (U+2009 compris) ; règle (1) par
  `bornes_champs` et le tokeniseur par caractères ; jeton dominant et entropie non définie pour un seul jeton ; A9 ;
  lecture typée de la lecture décisive (`_chemin`, `_booleen`) ; cohérence lecture contre source (recalcul des aires,
  1e-9) ; arrêt écrit après le manifeste ; scénarios de tests (plancher par tâche, niveau, biais de longueur, confusion,
  référence géométrique, « thrice », corrélation, début d'action, saturation), dépôt jetable et chargement de la copie.
- **a (greffes)** : voir § 3.
- **Gemini** : `_verifier_params_bootstrap` → `verifier_parametres_tirage` ; `plancher_conjoint` et
  `t4_tranches_internes` en copie corrigée, comme oracle dans `test_oracle_gemini_plancher_conjoint_et_tranches_internes`
  (même flux de tirages, égalité à 1e-12, mêmes effectifs).
- **Neuf (aucun candidat, demandé par le brouillon 3 ou par la consigne)** : table `conclusions_etablies` et cibles en
  chaînes ; forme des contrôles (`cible`, `controle_contraire`, « sans objet » qui n'écrit rien hors du descriptif) ;
  gardes 2 (commande, empreinte, lien, unicité), 3, 5 (par `mesures_action`), 6, 7 (typée, entrées en échec « non
  lu »), 8, 10 (règle de `lecture.py` l. 217), 11 (par cible) ; A2 (b) à L = min(c, L_coût) avec fenêtres du coût et
  δ̄(b) moyenne des 50 répliques dans chaque tirage ; A4 (a) nombre de tranches observé et par tirage ; A4 (b) tranche par
  copie (poids k) ; part des tirages où Δ ≤ 0 ; A5 règle (1) avec retrait du gras « chaque fois » et règle (2) sans la
  condition de la ligne ACTION ; A6 sur toute la population de `cout` et au sens inverse ; A7 (i), (ii), (iii) du
  brouillon 3 ; A8 règle stricte et maximum unique ; audit de symétrie et recommandation ; sortie unique ; vraie ligne de
  commande dans un processus séparé ; nombre de tests en tête.

## 3. Greffes

| greffe | origine | où | test (cas sain et artefact) |
|---|---|---|---|
| garde d'égalité avec `lecture._localisation` (lignes, pré-coût, coût) | a l. 580-583 | `localisation` | `test_garde_localisation_egale_a_celle_de_la_lecture` |
| `_propre` à la place de `_vers_json` : valeur non finie = garde avec son chemin | a l. 464-482 | `_propre` (par entrée, puis sortie entière) | `test_valeur_non_finie_dans_la_sortie_garde_avec_son_chemin` |
| `exiger_premier_passage` : manifeste illisible = arrêt ; clé de b (run source seul) | a l. 1481-1490 | `_manifestes`, `exiger_premier_passage` | `test_garde_9_premier_passage` |
| `position_cout_lire_action`, `_vers_brut`, `_NETTOYAGE`, avec la garde de la valeur | a l. 105, 665-711 | `regle_lire_action`, `_vers_brut` (règle (2) de A5) | `test_A5_regles_cas_listes`, `test_A5_gardes_de_la_regle_de_lire_action` |
| issue fixée avant les analyses, lecture vérifiée inchangée après | a l. 1425-1457 | `analyser_addendum` (instantané de toute la lecture) | `test_issue_modifiee_pendant_l_addendum_arrete` (variante `a9_qui_touche_l_issue`) |
| compte `pre_entier` | a l. 625-637 | descriptif de A2 : `pre_cout_entier` (c ≤ L_coût) à côté de `cout_plus_long_que_pre_cout` | `test_A2_sain`, `test_A2b_fenetres_quand_le_champ_du_cout_est_plus_long_que_le_pre_cout` |
| intervalle de A4 (b) sur l'écart conjoint, plancher tiré | a l. 1031-1037 | `t1_intra_tache` → `ecart_conjoint(…, "par_copie")` (après correction du poids k²) | `test_A4b_tirage_a_copies_doublees…`, `test_A4_artefact_confusion_entre_taches` |
| `RUN_ADDENDUM` | a l. 68, 1497 | `exiger_commande` | `test_forme_de_la_commande`, `test_gardes_avant_le_manifeste_aucune_sortie` |
| run source décisif en mode réel | a l. 1502-1504 | `exiger_run_source_decisif` (garde 2) | `test_run_source_decisif_en_mode_reel`, `test_garde_2_…` |
| A8 sur toutes les actions notées, segments sur les bornes lisibles | a l. 1259-1330 | `a8_dominants` | `test_A8_sain`, `test_A8_regle_stricte…` |
| `_artefact_A1` (sens « haut ») | a tests l. 169-174 | scénario `a1_haut` | `test_A1_artefact_sens_haut_mention_au_plancher_conjoint` |
| verrou systématique | a tests | `test_verrou_controle_contraire_sans_conclusion_etablie` (16 artefacts), `test_verrou_controle_favorable_a_une_conclusion_non_etablie` (A1 à A8) | — |
| `_verifier_params_bootstrap` | Gemini l. 26-34 | `verifier_parametres_tirage`, à l'entrée de `ecart_conjoint`, `difference_fenetres`, `contrastes` | `test_gardes_des_parametres_de_tirage` |
| `plancher_conjoint`, `t4_tranches_internes` en oracle | Gemini | tests seulement | `test_oracle_gemini_…` |

Corrections sans greffe : qualification « aucune réserve de l'addendum » retirée (RA-23 : une conclusion établie sans
réserve ne reçoit rien, test `test_cas_sain…`) ; poids k² corrigé (une tranche par copie) ; nombre de tranches de A4 (a)
rapporté (observé ; minimum, médiane, maximum par tirage) ; part des tirages où Δ ≤ 0 rapportée (A1, A4, et sa
contrepartie pour A2 (b) et A3) ; artefact de A6 au sens inverse écrit (`test_A6_artefact_sens_inverse_temoin_et_mention`).

Mutants (essai hors livrable, `essais/mutants.py`, journal `essais/mutants.log`) : 26 règles affaiblies une à une ; les
tests visés en tuent 26. Le mutant « poids k² » survivait au premier passage ; le test des copies doublées a été renforcé
(tirage X, X, Y imposé dans `ecart_conjoint`), il le tue désormais.

## 4. Règles que je n'ai pas appliquées telles quelles

Aucune règle du brouillon 3 n'est laissée de côté. Trois points ajoutent pourtant des arrêts à la liste fermée, et
plusieurs points comblent un silence du texte. Je les écris pour la contre-lecture R2 et pour la décision de Lazar.

Arrêts ajoutés à la liste fermée (greffes demandées ; chacun renforce une garde écrite ; aucun ne peut se déclencher sur
un run réel cohérent) :
1. **Cohérence lecture contre source** (b) : aires et quantiles des jeux lus recalculés, égaux à 1e-9 ; arrêt sinon.
   Rattachée à la garde 2 (« run_source de la sortie égal à --run-source », prouvé par le calcul). Passée avant le
   manifeste dans `executer`, juste après la garde 7, dont elle a besoin.
2. **Égalité de la localisation** avec `lecture._localisation` (a) : arrêt sinon (RA-13).
3. **Garde 5 renforcée** : en plus d'épisode, condition, tâche et pas, les mesures relues sur chaque texte par
   `mesures_action` doivent égaler la table. Preuve d'alignement plus forte ; le run les calcule sur les mêmes textes.

Silences du texte, comblés ainsi :
4. **Sortie unique et arrêt après le manifeste** : l'arrêt est écrit dans la sortie unique `lecture-addendum-p3.json`
   (clé `arret`, motif), puis propagé. Le nom reste unique.
5. **Garde 9** : critère du brouillon (préenregistrement de l'addendum, même run source), en union avec la clé de b
   (commande du module, même run source). C'est plus large que la lettre ; c'est la consigne de greffe.
6. **Réserve générale (garde 11)** : une réserve par cible établie, pour tenir « toute réserve nomme sa cible ». Une
   entrée est « en échec » si au moins un de ses calculs l'est (choix prudent). Le seuil est « plus de la moitié » :
   8 entrées sur 16 ne suffisent pas, 10 oui (testé).
7. **A4 (b)** : l'effectif minimal général (10 de chaque côté, section « Seuil ») s'ajoute aux deux minima propres (deux
   tâches mixtes, dix paires).
8. **A7 (iii)** : une corrélation non définie (moins de trois paires, série constante) est « non calculable », donc
   « non lu » ; si la cible est établie, elle donne `reserve_A7_non_lue`.
9. **A7 (i)** : un contrôle par jeu à l'état « au-dessus » et par prédicteur (12 par sonde) ; un jeu qui n'est pas
   « au-dessus » est noté au descriptif (« marge non contrôlée »).
10. **A8** : une action de trois jetons au plus compte « dans les trois premiers » (aucun jeton suivant) ; leur nombre
    est rapporté.
11. **A2 (c)** : la fenêtre de longueur L juste avant le champ est comparée au score du champ entier.
12. **Audit de symétrie** : sans aucune réserve possible, le déclencheur reste faux (« toutes » ne vaut pas sur un ensemble
    vide).
13. **Règle (2) de A5** : elle lit les champs sans la condition de la ligne ACTION (l. 122-128), puisque le texte cite
    l. 108-116 et 129-138. La garde d'égalité avec `lire_action` ne vaut que quand `lire_action` lit les champs.
    Conséquence : une action sans ligne ACTION est comptée invalide, pas divergente (testé).
14. **T2_propre** exclut les actions invalides et les divergences entre les règles (1) et (2) seulement. La greffe
    « union des divergences » (avec la règle « tolérante ») n'est pas appliquée : le brouillon 3 fait de cette règle un
    descriptif, qui ne doit pas toucher une réserve.
15. **Empreinte du préenregistrement de P3 (garde 2)** : comparée au fichier scellé (`verifier`), non à la valeur écrite
    dans l'en-tête du brouillon ; le sceau garantit l'égalité dans le dépôt réel.
16. **Code gelé modifié (garde 1)** : `exiger_code_cite` sur le commit cité par le préenregistrement de l'addendum ; celui
    de P3 est aussi contrôlé par `lecture.exiger_lecture_sous_prereg` (garde 2).
17. **Forme de la commande** (nom du run, chemin du préenregistrement) : contrôlée avant la garde 1, comme argument.
18. Clés de graines non nommées par le texte : `aire-cout`, `juste-avant`, `aire-cout-propre`, `T4-tranches-internes`,
    `T1-intra-tache`, `T1-sensibilite`, `addendum/A7/<p>/<jeu>/<forme>`, `addendum/A6/sans-sonde/<objet>`. Placebo de
    A1 : un seul générateur (permutation, puis tirages), clé `addendum/A1/<p>/placebo`. Générateurs :
    `default_rng(graine_entiere(…))` pour les boucles du module, `generateur(…)` pour `effet_cout_apparie` (comme la
    lecture).
19. Fonctions privées du code gelé importées plutôt que recopiées : `lecture._permuter_dans_les_taches`,
    `lecture._localisation` ; `conditions._CLE_BRUTE`, `_FERMETURE_GRAS` ; `propositions._nettoyer`, `_CLE`, `_ACTION`.

## 5. Tests (117)

- Outils : aire vectorisée (1e-12, ex aequo, tranches) ; ses gardes ; gardes des paramètres de tirage (Gemini) ; oracle
  de Gemini ; copies doublées de A4 (b) ; aucune moyenne sur les jetons (chaque score de fenêtre égale
  `agreger_par_jeton` sur son empan, maximum) ; fenêtres quand le champ du coût est plus long ; dégénérescences au-delà
  de 1 %.
- Transverses : déterminisme octet pour octet et entrées intactes ; entropie autre (fonction pure ; ligne de commande,
  en processus et dans un processus séparé) ; issue primaire et garde de la copie altérée ; lecture modifiée pendant
  l'addendum ; aucune clé interdite, aucun texte ; toute exception autre que `GardeArret` arrête ; valeur non finie.
- Gardes (cas sain et artefact, R5) : 1 (entropie, préenregistrement non scellé, empreintes du module et des tests,
  arbre gelé, module hors de son chemin, garde d'import) ; 2 (run source non décisif, autre commande, lien nul, unicité,
  rattachement, lecture altérée, lecture d'un autre run, lecture forgée incohérente) ; 3 (antériorité, empreinte
  scellée autre, aucun commit, commit inconnu, histoire coupée sur un dépôt jouet) ; 4 (run source altéré) ; 5 à 11 ;
  cohérence ; localisation ; forme du run source ; verrou ; cible hors de la table.
- Verrou, trois cas : contrôle contraire sans conclusion établie (16 artefacts) ; contrôle favorable à une conclusion non
  établie (A1 à A8) ; réserve décisive présente et contrôle favorable, aucune « levée » (et audit de symétrie déclenché).
  Run « organisme non établi » aux drapeaux « conforme » : `conclusions_etablies` vide, « réserves sans objet ». Table
  fermée des conclusions. Audit « toutes déclenchées ». Réserves triées et uniques.
- Par analyse, A1 à A9 : cas sain, artefact (deux à quatre pour A1, A2, A4, A6, A7, A8), cas dégénéré, verrou. A9 : son
  artefact vérifie qu'aucune réserve n'est levée, sur une lecture où tout est établi comme où rien ne l'est.
- Bout en bout dans un dépôt git jetable (copie de `src/`, deux runs sources, deux lectures décisives) : gardes d'avant le
  manifeste sans aucune sortie ; passage réussi scellé et rattaché ; second passage refusé ; arrêt après le manifeste
  écrit avec son motif. La vraie commande dans un processus séparé : 2 000 et 10 000 tirages, vraie garde d'import.

Sortie de pytest (passe finale, fichier entier, sur les empreintes ci-dessus, `essais/pytest-final.log`) :
`117 passed in 592.40s (0:09:52)`.

## 6. Durée mesurée

Banc `essais/bench.py`, journal `essais/bench-2000.log` : données synthétiques de taille réelle, 60 tâches, 4
conditions, 10 pas (2 400 actions notées), 430 sondes (2 principales, 2 × 200 de plancher, 28 autres), 300 jetons par
action, textes d'environ 1 500 caractères, formes du coût sur un tiers des actions du saboteur, 2 000 tirages pour les
aires et 10 000 pour les coûts, sur un cœur :

- **432 s (7,2 min)** pour `analyser_addendum` entier ; aucune extrapolation nécessaire ;
- par analyse : A1 330 s, A4 71 s, A2 14 s, A7 6 s, A5 3 s, A3 2 s, A8 0,2 s, A6 et A9 moins de 0,1 s ; hors
  analyses (gardes 5 à 8 et 10, cohérence, localisation, relecture des textes, synthèse) : 6,6 s ;
- le brouillon prévoit « de l'ordre d'une heure » : la mesure est bien en dessous. Le run réel lit aussi le run source
  et la lecture (quelques secondes).

La mesure porte sur la fonction pure, inchangée depuis ; la dernière retouche du module (`executer` : cohérence avant
le manifeste) n'y entre pas.

## 7. Points ouverts

1. Contre-lecture du code final (le brouillon 3 annonce « contre-lu sous trois angles, puis aligné ») : ce module n'a
   pas encore été relu par un sous-agent neuf.
2. Les points 1 à 3 du § 4 ajoutent des arrêts à la liste fermée. À faire valider (ou à écrire dans le brouillon) avant
   le scellement.
3. Versement : le module et les tests vont sous `docs/procedures/P3-addendum-v1/`, dossier scellé (`verifier-arbre`) :
   chaque fichier y demande son `.sha256`, et un `__pycache__` ou un `.pytest_cache` ferait échouer `verifier-arbre`.
   Lancer avec `PYTHONDONTWRITEBYTECODE=1 … -p no:cacheprovider`.
4. Les empreintes changent à toute retouche, même d'un commentaire ; le préenregistrement doit citer celles des fichiers
   versés, dans le format exact « Module de l'addendum (sha256) : `…` » et « Tests du module (sha256) : `…` ».
5. Près de 0, le signe d'une borne basse dépend du flux de tirages (constat du jury). La part des tirages où Δ ≤ 0 est
   rapportée pour que le sous-agent du verdict voie ces cas ; aucune règle ne la lit.
6. Le test de bout en bout remplace la garde d'import de la lecture en processus (le code importé est celui du dépôt de
   travail) ; la vraie garde est éprouvée par la ligne de commande dans un processus séparé.
