# Différences entre le brouillon 1 et le brouillon 2 du préenregistrement de l'étude par simulation des formulations du contraste à témoin apparié de la porte de fin de phase 1 (G1) — v1

- Écrit par le rédacteur du brouillon 2 (Claude Fable 5.2, `claude-fable-5-2`), le 18 novembre 2026 vers 22:15 UTC.
- Brouillon 1 : `prereg/formulation-g1-simulation-v1-brouillon1.md` — `5b3b981bca7239a170846140db9245c2989f81e02d1910842daabb6023a1422f` (inchangé).
- Contre-lecture 1 : `prereg/contre-lectures/formulation-g1-simulation-v1-brouillon1-cl1.md` — `ffa60e0b9255feb0e178ccfb137d2db23168c5c44dae8d864b8ddbce3969ffb8`.
- Brouillon 2 : `prereg/formulation-g1-simulation-v1-brouillon2.md` — `96cd0fa3342b9feb601be4aa46aa13bda53ae3b89284c1ce0f9329cf21b83af3`.
- Aucune simulation complète n'a tourné ; aucune issue n'a été lue. `prereg.problemes` sur le brouillon 2 : aucune remarque.

## 1. Fichiers : ancien, nouveau, décompte des lignes changées

Choix (R12) : **fichiers neufs** pour tout fichier de code ou d'essais qui change ; les fichiers de la v1 restent tels quels, scellés, et leurs 59 essais réussissent toujours. Le décompte est celui de `diff ancien nouveau` : lignes retirées (−), lignes ajoutées (+).

| ancien (empreinte) | nouveau (empreinte) | − | + |
|---|---|---|---|
| `prereg/formulation-g1-simulation-v1-brouillon1.md` (`5b3b981bca7239a170846140db9245c2989f81e02d1910842daabb6023a1422f`) | `prereg/formulation-g1-simulation-v1-brouillon2.md` (`96cd0fa3342b9feb601be4aa46aa13bda53ae3b89284c1ce0f9329cf21b83af3`) | 78 | 164 |
| `src/controle_ia/formulation_g1/statistiques_v1.py` (`543461cdcbdb3f5a4eaac1f5791540e19c207d56777a6ee8b105d0ff9c2b69a7`) | `statistiques_v2.py` (`cf6dc8cb5207309b48709ab042f65b22485063a821851db4eeb0d27a255f6cdf`) | 4 | 28 |
| `mondes_v1.py` (`d0fa9f5a2e1e45c9829208aea5cc7ef179225d3ce0e067398cdb94034fa034c8`) | `mondes_v2.py` (`12234cbd032db6c757c3d0aad16423467edad4fceab86b45afc27f2c1f1450e5`) | 18 | 79 |
| `simulation_v1.py` (`f8106a7ce1da040aefd1f733b46031b9b55484afeb478da7b23d4e22583ad6d4`) | `simulation_v2.py` (`62381e96fe4fd1abe9b2727ab191a64acd2d6f1e2e72ec3cf32bfacb9ca1f1a4`) | 63 | 117 |
| `lecture_v1.py` (`e1537be1268df9ee8aed3d293921c0b798b9cf3133cda50ff297503cadc69184`) | `lecture_v2.py` (`64cddf016f6e6f704ac546a66ab95c3ad1b70b8f57b28df24c860da851676eb4`) | 53 | 263 |
| `__init__.py` (`bb0aaef73d9ea295aab8385ce8e755858690ebdb9c88dc4f0c500dc6ae3772da`) | inchangé (son texte nomme encore les modules de la v1 ; le changer romprait son sceau) | 0 | 0 |
| `tests/test_formulation_g1_statistiques_v1.py` (`6879158a7280677f4ec511d83f1ef983982cfec1f07677d536a27ee229ad64b5`) | `test_formulation_g1_statistiques_v2.py` (`6b799cdaa7c15a018e64dffb03d8b7588730067c7d1100af5989a8ba1fe4057d`) | 2 | 36 |
| `test_formulation_g1_gardes_v1.py` (`f191516b661d78bc5005a6b092c5ec5a796dc897b5fa9ad4ba5b379ae3ab01d7`) | `test_formulation_g1_gardes_v2.py` (`cff1c8c3a167cb3c7945864801893dec5942580058171d64f11b4d22317e7516`) | 12 | 110 |
| `test_formulation_g1_mondes_plantes_v1.py` (`92586db16e18ef1839bfc0e49909891c94f20e0c61c5196fce4ccb198c7c09da`) | `test_formulation_g1_mondes_plantes_v2.py` (`dc446a865640c6e14ab5e909a405694dd0818deddfd89ac6453cc75d2231fc84`) | 4 | 12 |
| `test_formulation_g1_regle_v1.py` (`d4e7557e09cccb8e375b8a7167fd73bbfc9ac8b86b309d91a62d308972d8b83d`) | `test_formulation_g1_regle_v2.py` (`180e90754e65d13ab5ecb80b8346e965a6774a11486f6556e51bf7b1a6ecc1e5`) | 51 | 278 |

Essais rejoués le 18 novembre 2026 à 22:12 UTC (`.venv/bin/python -B -m pytest -q -p no:cacheprovider`, `PYTHONPATH=src`, dossier temporaire hors du dépôt) : **95 réussis** sur les quatre fichiers de la v2 ; **59 réussis** sur les quatre fichiers de la v1.

## 2. Chaque changement, rattaché à sa remarque

### Bloquants

| remarque | changement de texte (section du brouillon 2) | changement de code | essais (fichier de la v2) |
|---|---|---|---|
| **B-1** la règle penche vers A | couple « faux positifs sur l'avance véhiculaire » (« Métrique »), appliqué tel quel ; couple « couverture de puissance » (« Métrique »), tel quel ; couple « Ce que l'issue vaut », tel quel ; en plus : les deux classes de désaccord définies à « Hypothèse », leur dénombrement à « Métrique », la section « Choix de fond remis à Lazar » (sans recommandation), la première ligne de la table de la règle (« sous le plafond ») | `lecture_v2.classe_de_regle` (le couple, plus l'option « grille d'avant l'essai ») ; `indicateurs` range par classe de règle et rend `desaccords` ; `tables_de_desaccord` (une ligne par monde, pour la note) | `regle` : `test_classe_de_regle_quatre_cas_et_frontiere`, `test_indicateurs_couverture_sous_le_plafond_et_desaccords_hors_regle`, `test_tables_de_desaccord` |
| **B-2** changements faits après l'essai | couple « Puis : la règle est jouée une seconde fois… », appliqué (devenu le point 1 de la liste des rejeux) ; couple P6 « non probante », tel quel ; couple de la déclaration 3 : la phrase sur P4 est écrite avec « le rédacteur du brouillon 2 ne peut pas le dire » — il n'a pas écrit le brouillon 1, qui n'a qu'une version scellée ; P4 est donc traitée comme non probante | `NON_TRANCHE_APRES_ESSAI` ; `indicateurs(…, avant_essai=True)` ; `verdict` le vérifie avant l'effectif ; `mondes_v2.SABOTAGE_AJOUTE_APRES_ESSAI` | `regle` : `test_grille_d_avant_l_essai`, `test_dependances_de_l_issue` (cas 1), `test_ordre_des_dependances` |

### Majeurs

| remarque | changement de texte | changement de code | essais |
|---|---|---|---|
| **M-1** calibrage honnête | couple du tableau de la grille, tel quel ; couple de la définition de E, tel quel ; hypothèse de travail (7) ; écarts-types du seuil sous le tableau ; calcul exact (d) ; mondes plantés à 4 000 épisodes | `Monde.calibrage_honnete` sans défaut (0 refusé) ; la grille l'écrit à 10 fois les tâches ; variantes « calibrage honnête à 16 fois » et « sur 300 » ; `NOMBRE_ATTENDU` ; contrôle V4 à 4 000 épisodes (ajout) | `gardes` : `test_grille_calibrage_honnete_a_l_echelle_de_n055`, `test_calibrage_honnete_sans_defaut` ; `mondes_plantes` : `test_calibrage_quarante_sur_quatre_mille_un` |
| **M-2** le pari | hypothèse de travail (2) : ni le couple préféré ni le repli, mais leur réunion — grille de mises de D-S6 mise en œuvre comme lecture qui décide (couple préféré), conception non remise et garde de D-S4 absente, donc issue dite conditionnelle (repli) ; couple de « Métrique », tel quel | `statistiques_v2.pari_sur_grille` ; `simulation_v2` : lecture « pari » sur la grille, la mise prévisible devient « pari_previsible » ; `verdict` : issue différente sous elle → « dépend de la statistique » ; contrôle V3 pour les deux paris | `statistiques` : trois essais `test_pari_sur_grille_*` ; `regle` : `test_dependances_de_l_issue` (cas 4 et 5) ; `gardes` : `test_structure_des_sorties` |
| **M-3** trois comparateurs | couple de l'hypothèse de travail (1), appliqué, avec les valeurs fixées (parts 0,9 et 0,75 ; 0,6 et 0,4 ; corrélation 0,7) ; ligne « comparateurs » du tableau ; « Ce que l'étude ne dit pas » | `Monde.bases_blanches`, `correlation_bases`, `correlations()` ; `simulation_v2._lot` à plusieurs comparateurs sous intersection-union ; deux variantes ; `NON_TRANCHE_COMPARATEURS` | `gardes` : `test_trois_comparateurs_intersection_union`, `test_correlations_des_moniteurs` ; `regle` : `test_dependances_de_l_issue` (cas 6 et 7) |
| **M-4** budgets du témoin | couple de B1, tel quel ; paragraphe « Budgets d'épisodes du témoin, dits » ; ligne « épisodes du témoin lus par la garde » du tableau ; **ajout du rédacteur** : sixième rejeu de la règle | `Monde.episodes_garde` ; variantes « garde sur 300 épisodes » et « budget de témoin égal » ; `NON_TRANCHE_BUDGET` (ajout) | `gardes` : `test_garde_lue_sur_une_partie_des_episodes`, `test_garde_partielle_refusee_avec_reechantillonnage` ; `regle` : `test_dependances_de_l_issue` (cas 8 et 9) |
| **M-5** niveau | couple « rejouée au niveau 0,05 », tel quel ; hypothèse de travail (3) | `NON_TRANCHE_NIVEAU` ; `verdict` | `regle` : `test_dependances_de_l_issue` (cas 3), `test_ordre_des_dependances` |
| **M-6** audits de symétrie | paragraphe « Audit de symétrie » : « entièrement codé » ; « huit » corrigé en douze ; ligne « alerte trop beau » de « Seuil » | `alertes_de_symetrie` : alerte « option retenue à sa meilleure valeur », alerte « trop beau » (avec un plancher d'une demi-répétition, ajout : un compte entier ne peut pas approcher l'exact de plus près) | `regle` : `test_alertes_de_symetrie_sain_et_artefacts` |

### Mineurs

| remarque | changement |
|---|---|
| **m-1** | en-tête : commits `b6285a4e1` (code de la v1) et `80fb3e1d4` (essais) ; tête à l'écriture du brouillon 2 |
| **m-2** | P2 : réfutation étendue à l'empreinte 0,8 (couple tel quel) ; codée dans `predictions` |
| **m-3** | P6 : réfutation à 10 % (couple tel quel) ; P6 se lit sur la variante « calibrage honnête sur 300 », puisque le bloc principal calibre à l'échelle de D-S9 |
| **m-4** | couple tel quel (P1 à P8) ; `lecture_v2.predictions` ; essai `test_predictions_codees` (cas sain, bascule de chaque clause, monde absent) |
| **m-5** | seuil de validité = niveau + trois erreurs de Monte-Carlo : 0,036 au niveau 0,025, 0,065 au niveau 0,05 (`SEUILS_FAUX_POSITIFS`) ; note sur le maximum de 54 mondes ; les réponses écrites des mondes plantés gardent 0,065 (`BORNE_MONDES_PLANTES`) ; essai `test_seuil_de_validite_suit_le_niveau` |
| **m-6** | ligne « bruit d'épisode » du tableau ; texte de `simulation_v2._calibrage` |
| **m-7** | `exiger_duree` (contrôlée à chaque monde rendu ; arrêt des processus fils par leurs poignées), `exiger_repetitions_completes`, `exiger_mondes_complets` ; validation manquée : trois artefacts et le cas sain ; essais `test_duree_maximale`, `test_repetitions_minimales`, `test_mondes_complets`, `test_validation_saine_et_manquee` ; ligne de la liste d'arrêt réécrite |
| **m-8** | « Ce que l'étude ne dit pas » |
| **m-9** | note sous le message ; « le plan est joint » au lieu de « le plan et le code » |
| **m-10** | monde « PL3 d'origine, seuils calibrés sur 300 épisodes », rapporté, non bloquant (`rapporte` dans `controles_validation`) ; non joué avant scellement |

### Ajouts du rédacteur du brouillon 2, au-delà des couples (à contre-lire)

1. Sixième rejeu de la règle, à budgets du témoin égalisés (`NON_TRANCHE_BUDGET`) — tiré de M-4.
2. Prédiction P8 (bruit du seuil à l'échelle de D-S9, lecture « student »), écrite par ordre de grandeur avant toute simulation — tirée du point (g) de la contre-lecture.
3. Contrôle de théorie V4 à 4 000 épisodes (40/4 001) — tiré de M-1.
4. Clause de réfutation de P7 alignée sur son énoncé (« aucun monde où les deux options dépassent 50 % »), relevée en codant m-4.
5. Plancher d'une demi-répétition dans l'alerte « trop beau » — tiré de M-6.
6. Paragraphe « Ce que la règle peut encore devoir à sa construction, dit d'avance ».
7. Section « Points portés à Lazar par la contre-lecture 1 » (reprise de la section 7 du rapport).

## 3. Ce qui n'est pas appliqué, et pourquoi

- **Garde de D-S4 du pari du programme** (M-2) : N-055 n'en donne que le nom (« appariée bloquante (δ) + absolue rapportée + e-valeur du minimum + calibrage dimensionné par les jumeaux ») ; sa définition est dans la conception du pari (v2, `9c39a73d…`), qui n'est pas dans les pièces remises au rédacteur et qu'il n'a pas cherchée. L'inventer aurait mis dans l'étude une statistique qui n'est celle de personne.
- **Fidélité de la grille de mises** (M-2) : mise en œuvre d'après la seule ligne D-S6 de N-055 (capital moyen sur quatre mises fixes) ; à confronter à la conception par la session mère.
- **Unité de D-S9** (M-1) : prise à la tâche (10 × tâches épisodes) ; à confirmer.
- **Phrase sur P4** (B-2) : le rédacteur ne peut pas dire si P4 existait avant l'essai ; elle est traitée comme non probante.
- **Bloc principal à trois comparateurs** (M-3) : la liste de N-056 n'est simulée qu'en variante (72 mondes) ; la passer au bloc principal triplerait le plan et demanderait des valeurs des bases que rien ne fixe.

## 4. Décision qui n'est pas au rédacteur

Refuser un gain réel quand la boîte blanche sonne sur le véhicule au-delà de 5 %, ou laisser passer une avance du véhicule sous 5 % : écrit comme décision de Lazar à la section « Choix de fond remis à Lazar » du brouillon 2, deux options, avantage et inconvénient de chacune, **sans recommandation**, sans défaut sous 48 heures.
