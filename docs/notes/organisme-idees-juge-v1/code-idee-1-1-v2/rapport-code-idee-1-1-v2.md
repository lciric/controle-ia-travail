# Rapport du développeur — code de l'idée 1.1, version 2 (corrections de la contre-lecture `contre-lecture-code-idee-1-1-v1.md`, `8def0cf5ea2f5c92ead9e116ae8a6c20249a3b3e7f3334b23994903907c50b99`)

- Auteur : le développeur du code v1 (rapport v1 `c970a897…`) ; je n'ai écrit ni le texte, ni la contre-lecture.
- Date (UTC) : 2026-11-15, de 23:10 à 23:23 ; tête `57956b23`.
- Ce que je n'ai pas fait :
  - aucun fichier v1 modifié (R12) ;
  - aucun commit, aucun appel réseau, aucun appel payant ;
  - **ni jeu, ni étape 0, ni lecture** lancés ;
  - aucun résultat lu ;
  - rien sous `diag/`, `runs/` ni `donnees/`.

## 1. Fichiers neufs (scellés)

Chaque fichier v2 est son fichier v1, plus les couples « ancien → nouveau » et l'ajout de fin déclarés dans `couples-v1-vers-v2.json`. L'essai `tests/test_organisme_idees_juge_idee_1_1_differentiel_v2.py` vérifie trois choses pour chacun des 13 fichiers :
- le fichier v1 est intact ;
- chaque ancien est présent une seule fois ;
- le fichier v2 est égal octet pour octet à v1 + différentiel.

Fichiers touchés : le banc (m3), la lecture (M3, m1, m4 à m7), l'étape 0 (E1, m9 à m11), l'exécution (M1, M2, m2, m8), les trois scripts, et les cinq fichiers d'essais. Les mutations ne changent que par leurs imports. Modules **inchangés** et toujours employés : `vue_v9_v1`, `nul_limite_v1`, `morceaux_par_coupe_v1`, les trois copies du code de la course, `projection_bras_v1`, `juge_v1`, `lois_v1`.

J'ai vérifié la fermeture des imports des trois scripts v2 : aucun module v1 touché n'est importé, et aucun fichier importé ne manque à `FICHIERS_GELES`. Les fichiers v1 touchés y restent, comme sources de l'essai du différentiel.

| fichier | sha256 |
|---|---|
| `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v2/couples-v1-vers-v2.json` | `17f06db023316d599c4be3301fbaff8cae9fe1932c226bf9e307e2e7bfb38813` |
| `scripts/etape0_idee_1_1_v2.py` | `4bf6f4d9e651864313e275a8f558b827b738d7c593a30e66e3f4e1709474c1d2` |
| `scripts/jouer_idee_1_1_v2.py` | `e1537e8eba34c56d89291765e393c8b209a5d807ca058eeb10e886f05b941e09` |
| `scripts/lire_idee_1_1_v2.py` | `973faf2bb0b44c56c2eab159d1d568f8ac853966b4e46488c601cae66be06bc5` |
| `src/controle_ia/organisme_idees_juge/banc_idee_1_1_v2.py` | `c3d77494885b8f51ea0a6858490242cbb9a993f4cbb8b6bc14511717673e27ea` |
| `src/controle_ia/organisme_idees_juge/etape0_idee_1_1_v2.py` | `2a3a9a89d7e9d59c9bfedfb2f64dd045470e51bd90badb645a8069a446fc6955` |
| `src/controle_ia/organisme_idees_juge/execution_idee_1_1_v2.py` | `36cce99ff05c968962527e6c85ff8e0a5d2701bf740bdb20e176bc0cb0a93ec9` |
| `src/controle_ia/organisme_idees_juge/lecture_idee_1_1_v2.py` | `7246d6eb5dccf4b25b2a7a972113a7493a4292f15f06dfd52ef0369572a44b5c` |
| `src/controle_ia/organisme_idees_juge/mutations_idee_1_1_v2.py` | `a71c97deaee78f96571aa1067b7619b56e9e24b6cd3e07d85aa6ea66224bc49b` |
| `tests/test_organisme_idees_juge_idee_1_1_banc_v2.py` | `bdc30ab359e78e0935090a19f3d5733ffd56121c9c71ff5e90a8b7581954a96c` |
| `tests/test_organisme_idees_juge_idee_1_1_differentiel_v2.py` | `3fbbdd2aba2a646c559b5e92b9d02b9de1f68b0665ed74ba9e32b4f403f8bdf4` |
| `tests/test_organisme_idees_juge_idee_1_1_execution_v2.py` | `c769bd4803a14c7b8337e8a01ad5a811abc41d7b48982c32558df83f00fde552` |
| `tests/test_organisme_idees_juge_idee_1_1_gardes_v2.py` | `f530a63188d07d3174a24e1b866c9f48007b715b4ad73526355bbec534a8887f` |
| `tests/test_organisme_idees_juge_idee_1_1_lecture_v2.py` | `b11f565521317d6752e9237397a2d120bf17fee1b7a1f64d9a2f0875e8f10817` |
| `tests/test_organisme_idees_juge_idee_1_1_projection_v2.py` | `6e53851ec4794d00f30d275a6a04f10aef72489c65cd6bce40085879b597631a` |

## 2. Essais

**259 passés, 0 échec** : les 117 essais v1, inchangés, et les 142 essais v2. Un processus, `nice -n 10`, sans variable `GIT_*`, 4 min 03. Un seul échec au premier passage :
- `ESSAIS` du lanceur v2 incluait les essais v1 ;
- c'est corrigé par un couple déclaré : le lanceur ne rejoue que les essais v2 ;
- les trois fichiers concernés ont été rejoués : 55 passés.

Les 142 essais v2 se répartissent ainsi : copies v2 des 117 essais v1, plus 25 neufs, dont l'essai du différentiel (14 cas). Le banc de mutations v2 compte 17 mutations, toutes tuées, 17 cas sains passés.

## 3. Correction par correction

| point | correction (fichier v2) | essai sain / artefact |
|---|---|---|
| **M1** | `execution.verifier_addendum_du_manifeste`, appelée par `lire_idee_1_1_v2.py` avant toute lecture : l'addendum inscrit au manifeste est relu, son empreinte est égale à celle du manifeste, chaque fichier gelé est revérifié par `lire_addendum`, et le bloc programme est égal à celui du manifeste ; sinon la lecture est refusée | `test_m1_la_lecture_relit_l_addendum_du_manifeste` (sain ; artefacts : sans addendum, empreinte différente, programme différent, fichier gelé modifié) |
| **M2** | `lire_addendum` compare **fichier par fichier** le champ `fichiers_geles` du fichier d'étape 0 aux empreintes de l'addendum, avec la même liste exigée ; l'empreinte du texte (`resultat.preenregistrement.sha256`) doit être égale à `3ffe1739…` | `test_m2_etape0_liee_au_code_gele_fichier_par_fichier` (autre code, liste incomplète, autre texte) |
| **M3** | `lecture.lire_v2` : verdicts de la v1 inchangés, plus les rapportés de la « Métrique » ; aucun ne porte de verdict. Détail ci-dessous | `test_lecture_v2_rapportes_de_la_metrique`, `test_strates_…`, `test_mcnemar_exact` |
| m1 | quantité fatale absente → `GardeArret` | `test_m1_quantite_fatale_absente_refusee` |
| m2 | clés `resultat`, `fichiers_geles`, `bloquants`, `jeu_permis`, `preenregistrement`, `chronometrage` exigées ; `jeu_permis` doit valoir `True` | dans `test_m2_…` (trois artefacts) |
| m3 | `probas_finies` exige la stricte positivité ; plus de plancher au numérateur gelé ni à celui de H7 (la loi est vérifiée, jamais plafonnée) | `test_m3_probabilite_de_carte_non_positive_refusee` |
| m4 | garde P4 : trois lectures rendues à part, dans `lectures`, sans priorité ; liste des cellules avec gel non tenues **ou non jugeables** | essai de lecture v2 |
| m5 | part des écarts résiduels > 2·10⁻³ sur J9, La et Ld | `test_m5_ecart_residuel_sur_j9_la_ld` |
| m6 | déclaré, sans changement de calcul : un secondaire réduit voit I recalculé sur ses seules premières répétitions (`declaration_m6` dans la sortie) | — |
| m7 | P5 peut valoir « partielle » (2 ou 3 lignes) ; P12 est lue sur ses réfutations écrites, partie par partie | essai de lecture v2 |
| m8 | reprise : `exiger_depot_propre_sauf_run` tolère les seuls `runs/<run>/` et `diag/organisme-idees-juge-v1/<run>/` du run repris ; tout autre changement refuse la reprise ; départ neuf inchangé (`exiger_depot_propre`) | `test_m8_reprise_tolere_les_seuls_dossiers_du_run` (sain ; artefacts : fichier étranger, dossier d'un autre run) |
| m9, m10, comptes non écrits | `etape0.declarations()`, inscrites au fichier d'étape 0 et imprimées dans le bloc programme de l'addendum : clés `(98, r, 0/1)` et `(97, k, …, 0/1)` ; empreintes des trois fichiers d'EP, dont `essai_projection_cas_v1.py` ; comptes de E9, ED, EP, des deux mutations, de Hn | `test_declarations_m9_m10` |
| m11 | déclaré dans le même bloc : le lanceur ne rejoue pas les comptes de H7 et de Hn ; ils valent pour le code gelé par M2 | — |
| **E1** | le lanceur v2 rejoue E0, E9, EP et ED (`etape0.essais_d_egalite`) **après** l'addendum et les contrôles, **avant** le jeu, comme l'étape 2 du texte ; tout essai manqué arrête avant le jeu ; les résultats sont inscrits au manifeste. **Plus d'écart d'ordre** | `test_e1_essais_d_egalite_manques_arretent` |

Détail de M3 :
- gains secondaires **contre J9⁺** (I⁺ recalculé) ;
- ρ **par strate** pour J9-P, La et Ld. L'appartenance des lignes V aux strates est la constante `STRATES_TEXTE`, écrite d'après le texte avant le jeu (voir § 5) ;
- **intervalles** de la décomposition du prix, sur les mêmes rééchantillons pour La et Ld ;
- **McNemar** exact par ligne V, sur 11 paires ;
- pour chaque (ligne, bras) : taux, **intervalle bilatéral** de Clopper-Pearson, log W **maximal et médian**.

Autre changement déclaré : le nom du run de la v2 est `idee-1-1-poids-du-nul-v2`. Le lanceur refuse un run antérieur de l'un ou l'autre nom.

## 4. E2 et E3 (pour le directeur ; rien n'est changé)

- **E2**
  - Phrase du texte (« Proximité avec le vrai juge ») : « J8 est calculé par le code du juge de la copie `94bfd92` (`nul_filles_v2.evaluer_v2`, `nul_v8.membres_archive_v8`). J9 par le **code original** [V9] : […] évaluation par `nul_v9.evaluer_v9` ([CL] M2). »
  - Ce que fait le code (v1 et v2) : le jeu n'appelle pas `evaluer_v2` ni `evaluer_v9`. Il rejoue d'abord leurs gardes : empreinte de l'engagement, lien des tirages, plan d'exécution, forme des issues, instants. Il appelle ensuite, dans l'ordre de `evaluer_sur_issues`, leurs fonctions internes : `sp.calibrer`, `sp.trajectoire_numerateur`, `sp.trajectoires`, `nf.valeurs_ajustees`, `nul_v9.detail_morceaux_groupe`, sans arrondi. Les membres communs sont partagés entre les bras après une vérification d'égalité.
  - Où l'égalité avec `evaluer_v2` et `evaluer_v9`, à 6 décimales et pour la promotion, est éprouvée : par essai ; par E9, sur deux répétitions de chacune des 29 lignes jugeables ; et désormais par E9 rejoué par le lanceur avant le jeu.
- **E3**
  - Phrase du texte (bras 5, J9-Dc) : « Sans coût de plus : les bornes par coupe sont déjà calculées. »
  - Ce que fait le code : le jumeau est évalué par le code du v9. J9-Dc fait **un second appel** au solveur, avec la copie renommée `detail_morceaux_par_coupe` : de 1 à 3 s par répétition dans mes mesures jouets, chronométrées dans le groupe « jumeau ». Aucun critère n'en dépend.

## 5. Lectures neuves déclarées (v2)

- **Strates de ρ (`STRATES_TEXTE`)** : « sur une partition du bras » si l'effet neuf de la ligne est posé sur une partition de la classe du bras.

  | bras | sur une partition | hors des partitions |
  |---|---|---|
  | J9-P | V2, V3, V4, V5 | V1 |
  | La | V5 | V1 à V4 |
  | Ld | V2, V4, V5 | V1, V3 |

  Ce tableau est ma lecture du texte, à confirmer par la mère.
- **Règle des strates** : une strate sans ligne informative est rendue « sans objet » ; un rééchantillon sans ligne informative dans la strate est écarté et compté ; les quantiles sont ceux de Bonferroni des primaires.
- **Décomposition du prix** : intervalle percentile à 95 %.
- **McNemar** : bilatéral exact ; les 11 paires sont listées dans `PAIRES_MCNEMAR`.

## 6. Étape 0, version 2 (à lancer par la mère, après relecture du différentiel)

```
cd /home/user/controle-ia-travail && .venv/bin/python -I -B scripts/etape0_idee_1_1_v2.py --travail /tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/etape0-travail-v2 --processus 3
```

- Sortie scellée : `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v2/etape0-v1/etape0-idee-1-1-v2.json`.
- La commande imprime aussi le bloc programme de l'addendum, avec ses déclarations.
- Les lignes d'empreintes s'obtiennent par `--lister-empreintes`.
- Durée estimée inchangée : environ 1 h, jusqu'à 1 h 30 si la machine est chargée.
- Lancer **après** le commit des v2 : l'étape 0 inscrit les empreintes des fichiers gelés, et M2 refusera toute différence avec l'addendum.
- Ensuite le jeu : `python -I -B scripts/jouer_idee_1_1_v2.py --addendum CHEMIN`. Il rejoue d'abord les essais, les mutations et E0 à ED, ce qui ajoute environ 15 minutes.

## 7. Ce qui n'est pas éprouvé

- L'étape 0 entière.
- Le jeu.
- La lecture sur des données réelles.
- La reprise après un vrai arrêt de machine : seuls le contrôle du dépôt et le saut des tranches scellées sont éprouvés.
- La contre-lecture du différentiel v1 → v2.
