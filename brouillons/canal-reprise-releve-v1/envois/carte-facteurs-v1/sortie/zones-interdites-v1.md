# Zones interdites de la v6.2.1 — v1

Écrite le 2026-10-26 à 06:42:49 UTC (heure lue sur `date -u` dans la commande qui écrit ce fichier) par un sous-agent neuf de la lignée conv-audit, sur le brief `LISEZMOI-brief-carte-facteurs-v1.md` (`d0d29df8dc60699cd9abf0f8c46d1057d00820828ffcfae14e8df6405fc80d7d`). L'auteur n'a écrit ni l'objet, ni ses textes, ni la boucle extérieure ; il n'a lu aucun résultat de course.

**Objet.** `organisme/` au commit `7ea32705c5437d91ed071dd95fb3209bb0b0035e` (v6.2.1, 26 fichiers ; empreintes de fichiers vérifiées ; empreinte d'arbre `4f13647a…` non recalculée ici). Numéros de ligne : ceux de ces fichiers.

**Pièces sœurs.** Forme lisible par G5 : `zones-interdites-v1.json` (`0082519cc0ef2400c198c89a8504f52948e7abb9b7e35e113db9ba1319f0b342`). Carte des facteurs : `carte-facteurs-v1.md` (`47fa6100ae32ec7a0879b14397a3ee4dc5731a98958acd920a9f279110346d2e`) et `carte-facteurs-v1.json` (`2aaedd08a719e93d2e18437377e9cc565dc4de230ef1af97b0a6e6ef807cec25`). Méthode, doutes et table du brief : `LISEZMOI-carte-facteurs-v1.md`.

**Ce que la liste ne contient pas.** Aucun critère ni aucune stratégie de classement, aucune règle, aucun seuil, aucune liste de mots, aucune consigne, aucun exemple : les parties du code sont désignées par fichier, fonction et lignes, jamais recopiées. Aucun fait de course, aucun score, rien sur une tâche de la banque, aucune proposition de changement du code.

## 0. Lecture

1. **Liste close.** Onze zones, Z01 à Z11 ; rien d'autre n'est zone interdite. Une ligne de code hors zone et hors facteur n'est atteignable que par F09 (défaut de code nommé) ; hors des modules de code, les fichiers d'accompagnement suivent le § 6 du protocole.
2. **Statuts.** `Z` : interdit, sans exception. `R` : porte la règle qui choisit une classe ; interdit, sans exception. `E` : chemin des réponses hors de cette règle ; interdit, sauf sous l'exception « défaut du chemin des réponses », déclarée dans la pièce de périmètre et revue à part par le contre-lecteur, qui le dit dans son verdict ; le type est donné (format, analyse de la réponse, délai).
3. **Zones et facteurs.** Disjoints ligne à ligne ; une zone l'emporte toujours. Trois segments de la zone Z03 tiennent dans des lignes du facteur F04 (§ 3).
4. **Origine.** Chaque zone dit si elle vient de la liste de départ du § 14 ou d'un ajout depuis le code ; chaque ajout porte sa raison.

## 1. Vue d'ensemble

| zone | nom | origine | statuts | fichiers et lignes |
|---|---|---|---|---|
| Z01 | Consignes des rôles qui répondent aux tâches | liste de départ du § 14 | E, Z | `principal.py` 1163–1190, 1191–1192, 1193, 1699–1701, 1741–1742, 1747–1754, 1936–1939 ; `mitose_spectrale.py` 43–48 |
| Z02 | Analyse de la réponse du modèle qui fixe une classe, et règle qui choisit la classe | liste de départ du § 14, complétée depuis le code | E, R | `principal.py` 313–344, 649–660, 661, 662–668, 671–673, 676–681, 684–689, 690–707, 708–709, 710, 711–714, 1598–1610, 1613–1616, 1630–1647, 1648–1672, 1673, 1675–1697, 1698, 1702–1712, 1713–1740, 1743–1744, 1745–1746, 1755–1765, 1766–1772, 1773–1774, 1775–1782, 1783–1788, 1790, 1961–1962, 1963–1972, 1973, 1974–1983, 1984–1986, 1987, 1988–2001, 2002–2009, 2044 |
| Z03 | Seuils du routage de la règle de classe | ajout depuis le code | R | `politique_endogene.py` 7, 44–52, 85–92, 240–250 ; `principal.py` 1046, 1054, 1088–1096, 1619–1627 |
| Z04 | Sonde : convention de classe et droit de vote | ajout depuis le code | R | `principal.py` 589–619, 633 |
| Z05 | Constantes de mots-clés de C-16 et ce qui les lit | liste de départ du § 14 | Z | `memoire_isvd.py` 81–82, 85–89, 186–195, 204, 227, 232 ; `principal.py` 14–15, 967–975, 1079–1087, 2077 ; `politique_endogene.py` 9–10, 35–41, 237–239 ; `tests/test_auto_architecte_v6.py` 302–312 ; `tests/test_corrections_v5.py` 205–215, 218–243, 246–250 ; `tests/test_emprunts_v5_3.py` 133–150 |
| Z06 | Exemple de format (principal.py l. 794) et consigne de formulation de la moisson | liste de départ du § 14 | Z | `principal.py` 787–795 |
| Z07 | Tout texte d'appel servi à un modèle pour une tâche | liste de départ du § 14, complétée depuis le code | Z | `principal.py` 28–29, 88–99, 251–257, 260–281, 880–883, 928–931, 933–946, 953, 1128–1132, 1135–1160, 1789, 1849–1852, 1883, 1896–1899, 1913–1918, 1929, 1954–1957 ; `memoire_isvd.py` 285–302 |
| Z08 | Exemples à vérité et leur choix | ajout depuis le code | Z | `principal.py` 30, 1109–1125 ; `metrique/attaques.json` 1–62 |
| Z09 | Chemin de la question ouverte | ajout depuis le code | Z | `principal.py` 717–753, 1202–1233, 1235–1544, 2046–2053 ; `mitose_spectrale.py` 124–130 |
| Z10 | Identifiants des appels (rôles) | ajout depuis le code | Z | `principal.py` 556, 627, 800, 843, 913, 1017, 1923, 1944 ; `mitose_spectrale.py` 84, 87, 90, 93 |
| Z11 | Instruments et documents de l'arbre | ajout depuis le code | Z | `metrique/calculer.py` 1–60 ; `metrique/definition.md` 1–15 ; `metrique/__init__.py` 1 ; `CONCEPTION.md` 1–162 ; `CORRECTIONS-v1.md` 1–57 ; `CORRECTIONS-v2.md` 1–25 ; `CORRECTIONS-v3.md` 1–16 ; `CORRECTIONS-v4.md` 1–23 ; `CORRECTIONS-v5.md` 1–53 ; `manifeste.json` 2, 4 |

## 2. Les zones

### Z01 — Consignes des rôles qui répondent aux tâches (liste de départ)

**Raison.** Le texte servi aux castes (tâches de test) et au calibrateur interne (tâches d'entraînement), composé par `_construire_prompt_evaluation_tache` : contexte, mémoire, règles induites, extrait de moisson, contrainte orthogonale, énoncé, étiquettes autorisées, consigne de choix, forme de réponse. Les lignes qui en choisissent les arguments, et les termes saturés qu'on y sert, en font partie. Seule la forme de réponse demandée (l. 1191–1192) est de statut E (format).

| entrée | fichier | fonction | lignes | statut | désignation |
|---|---|---|---|---|---|
| Z01.1 | `principal.py` | `_construire_prompt_evaluation_tache` | 1163–1190 | Z | consigne de tâche servie aux castes et au calibrateur interne |
| Z01.2 | `principal.py` | `_construire_prompt_evaluation_tache` | 1191–1192 | E (format) | forme de réponse demandée |
| Z01.3 | `principal.py` | `_construire_prompt_evaluation_tache` | 1193 | Z | fin de la consigne |
| Z01.4 | `principal.py` | `_traiter_tache` | 1699–1701 | Z | arguments qui composent la consigne de la caste 1 |
| Z01.5 | `principal.py` | `_traiter_tache` | 1741–1742 | Z | termes saturés servis dans la consigne orthogonale |
| Z01.6 | `principal.py` | `_traiter_tache` | 1747–1754 | Z | arguments qui composent la consigne orthogonale |
| Z01.7 | `principal.py` | `executer` | 1936–1939 | Z | arguments qui composent la consigne du calibrateur interne |
| Z01.8 | `mitose_spectrale.py` | `calculer_capacite_shannon_gram` | 43–48 | Z | choix des termes saturés que les consignes servent |

### Z02 — Analyse de la réponse du modèle qui fixe une classe, et règle qui choisit la classe (liste de départ, complétée)

**Raison.** Le chemin d'une réponse de modèle jusqu'à l'étiquette et la confiance écrites dans `reponses_test.json` : réception, repérage et décodage, analyse, seuils du routage lus, votes, arbitrage, arrêt anticipé, agrégation, ordre des tâches, écriture. La liste de départ en nomme l'analyse ; le reste du chemin y est ajouté parce qu'il porte la règle qui choisit la classe ou parce qu'il est le « format » et le « délai » de l'exception. Frontière R/E : § 4. La l. 1674 (plafond de jetons d'un appel de tâche) n'en est pas : elle est au facteur F07.

| entrée | fichier | fonction | lignes | statut | désignation |
|---|---|---|---|---|---|
| Z02.1 | `principal.py` | `_enregistrer_appel` | 313–344 | E (analyse) | réception d'une réponse : statut, texte retenu, journal |
| Z02.2 | `principal.py` | `_extraire_json_candidat` | 649–660 | E (analyse) | repérage des objets JSON d'une réponse |
| Z02.3 | `principal.py` | `_extraire_json_candidat` | 661 | R | ordre de préférence entre plusieurs objets JSON d'une même réponse |
| Z02.4 | `principal.py` | `_extraire_json_candidat` | 662–668 | E (analyse) | décodage de l'objet |
| Z02.5 | `principal.py` | `_normaliser` | 671–673 | E (analyse) | normalisation des chaînes comparées (étiquettes, familles, vérités) |
| Z02.6 | `principal.py` | `_confiance_finie` | 676–681 | E (analyse) | décodage d'un nombre fini |
| Z02.7 | `principal.py` | `_parser_decision_tache` | 684–689 | E (analyse) | entrée de l'analyse de la réponse d'une tâche |
| Z02.8 | `principal.py` | `_parser_decision_tache` | 690–707 | R | champs qui portent l'étiquette et la confiance ; rapprochement avec les étiquettes autorisées ; confiance lue hors objet ; valeur par défaut et bornes de la confiance |
| Z02.9 | `principal.py` | `_parser_decision_tache` | 708–709 | E (analyse) | constat rendu |
| Z02.10 | `principal.py` | `_parser_decision_tache` | 710 | R | validité du vote |
| Z02.11 | `principal.py` | `_parser_decision_tache` | 711–714 | E (analyse) | sortie de l'analyse |
| Z02.12 | `principal.py` | `_faut_basculer` | 1598–1610 | E (délai) | décision de passer les tâches de test en parallèle |
| Z02.13 | `principal.py` | `_ecrire_reponses` | 1613–1616 | E (format) | écriture atomique de reponses_test.json |
| Z02.14 | `principal.py` | `_traiter_tache` | 1630–1647 | E (analyse) | entrée de _traiter_tache ; sortie vide sans étiquette ou sans caste |
| Z02.15 | `principal.py` | `_traiter_tache` | 1648–1672 | R | seuils du routage lus, avec leurs replis ; urnes des votes |
| Z02.16 | `principal.py` | `_traiter_tache` | 1673 | E (analyse) | textes de la tâche |
| Z02.17 | `principal.py` | `_traiter_tache` | 1675–1697 | R | vote de la sonde ; caste 1 et son état |
| Z02.18 | `principal.py` | `_traiter_tache` | 1698 | E (délai) | temps et budget avant l'appel de la caste 1 |
| Z02.19 | `principal.py` | `_traiter_tache` | 1702–1712 | E (analyse) | appel de la caste 1, réception, analyse |
| Z02.20 | `principal.py` | `_traiter_tache` | 1713–1740 | R | vote de la caste 1 ; accord, discorde, besoin d'arbitrage |
| Z02.21 | `principal.py` | `_traiter_tache` | 1743–1744 | R | castes supplémentaires appelées |
| Z02.22 | `principal.py` | `_traiter_tache` | 1745–1746 | E (délai) | temps et budget avant chaque caste supplémentaire |
| Z02.23 | `principal.py` | `_traiter_tache` | 1755–1765 | E (analyse) | appel d'une caste supplémentaire, réception, analyse |
| Z02.24 | `principal.py` | `_traiter_tache` | 1766–1772 | R | votes supplémentaires ; arrêt anticipé |
| Z02.25 | `principal.py` | `_traiter_tache` | 1773–1774 | E (analyse) | textes rendus |
| Z02.26 | `principal.py` | `_traiter_tache` | 1775–1782 | R | agrégation : étiquette retenue et confiance finale |
| Z02.27 | `principal.py` | `_traiter_tache` | 1783–1788 | E (format) | détails rendus |
| Z02.28 | `principal.py` | `_traiter_tache` | 1790 | E (format) | sortie |
| Z02.29 | `principal.py` | `executer` | 1961–1962 | E (format) | résultats des tâches |
| Z02.30 | `principal.py` | `_recevoir` | 1963–1972 | E (format) | _recevoir : réponse rangée et écrite |
| Z02.31 | `principal.py` | `executer` | 1973 | E (format) | ligne vide entre les deux fonctions internes |
| Z02.32 | `principal.py` | `_une` | 1974–1983 | E (délai) | _une : appel de _traiter_tache |
| Z02.33 | `principal.py` | `_une` | 1984–1986 | R | données de la sonde servies à la règle (C-15 : exactitude de validation seule) |
| Z02.34 | `principal.py` | `_une` | 1987 | E (délai) | _une : fin |
| Z02.35 | `principal.py` | `executer` | 1988–2001 | E (délai) | tâches de test en séquence, puis en parallèle |
| Z02.36 | `principal.py` | `executer` | 2002–2009 | E (format) | réponses rassemblées |
| Z02.37 | `principal.py` | `executer` | 2044 | E (format) | écriture finale des réponses |

### Z03 — Seuils du routage de la règle de classe (ajout depuis le code)

**Raison.** `_traiter_tache` lit ces seuils (l. 1650–1669) et décide par eux du vote de la sonde, de l'accord précoce et de l'arbitrage (l. 1686, 1689, 1723–1724, 1728, 1732). Le § 14 interdit d'écrire « tout seuil […] qui intervient dans le choix d'une classe ». `seuil_confiance_caste1` est aussi un paramètre du contrat de l'architecte : ses parts du contrat (l. 1046, l. 1054 et les segments du § 3) sont gelées pour cette raison ; le reste du contrat reste au facteur F04 (LISEZMOI, D2).

| entrée | fichier | fonction | lignes | statut | désignation |
|---|---|---|---|---|---|
| Z03.1 | `politique_endogene.py` | `<module>` | 7 | R | SEUIL_CASTE1 du module initial |
| Z03.2 | `politique_endogene.py` | `seuils_routage` | 44–52 | R | seuils_routage du module initial |
| Z03.3 | `politique_endogene.py` | `<module>` | 85–92 | R | clés requises des seuils de routage |
| Z03.4 | `politique_endogene.py` | `verifier_et_valider_code_politique` | 240–250 | R | contrôle des seuils de routage d'un module candidat |
| Z03.5 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 1046 | R | borne de seuil_confiance_caste1 dans le contrat |
| Z03.6 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 1054 | R | gabarit : SEUIL_CASTE1 |
| Z03.7 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 1088–1096 | R | gabarit : seuils_routage |
| Z03.8 | `principal.py` | `_lire_seuil_verifie` | 1619–1627 | R | _lire_seuil_verifie : bornes et replis des seuils lus |

### Z04 — Sonde : convention de classe et droit de vote (ajout depuis le code)

**Raison.** L. 589–619 : l'exactitude de validation de la sonde se calcule avec la convention qui fait d'une probabilité une étiquette, et elle décide si la sonde vote (C-15). L. 633 : bornes des probabilités de la sonde qui deviennent des votes (l. 1686–1693). Le reste de `_entrainer_et_predire_sondes_traits` n'est dans aucune zone (rôles d'appel : Z10).

| entrée | fichier | fonction | lignes | statut | désignation |
|---|---|---|---|---|---|
| Z04.1 | `principal.py` | `_entrainer_et_predire_sondes_traits` | 589–619 | R | exactitude de validation de la sonde et droit de vote (C-15) |
| Z04.2 | `principal.py` | `_entrainer_et_predire_sondes_traits` | 633 | R | bornes des probabilités de la sonde qui deviennent des votes |

### Z05 — Constantes de mots-clés de C-16 et ce qui les lit (liste de départ)

**Raison.** Liste de départ : constantes `memoire_isvd.py` l. 81–82 et ce qui les lit. Lecteurs retenus, directs ou par le détecteur : le détecteur, la pondération des traces, les drapeaux rangés et relus, l'import, l'expression du gabarit, le branchement de la pondération, la copie du module initial et sa pondération, l'essai de la pondération par le vérificateur, et les essais hérités qui les lisent. Le résumé de mémoire montre le drapeau (`memoire_isvd.py` l. 298, dans Z07).

| entrée | fichier | fonction | lignes | statut | désignation |
|---|---|---|---|---|---|
| Z05.1 | `memoire_isvd.py` | `<module>` | 81–82 | Z | constantes de mots-clés (C-16) |
| Z05.2 | `memoire_isvd.py` | `_detecter_confirmation_multi_familles` | 85–89 | Z | détecteur qui les lit |
| Z05.3 | `memoire_isvd.py` | `mettre_a_jour_memoire_isvd` | 186–195 | Z | pondération des traces par le détecteur ou par ponderer_trace_memoire |
| Z05.4 | `memoire_isvd.py` | `mettre_a_jour_memoire_isvd` | 204 | Z | drapeau du détecteur rangé |
| Z05.5 | `memoire_isvd.py` | `mettre_a_jour_memoire_isvd` | 227 | Z | drapeau relu ou recalculé par le détecteur |
| Z05.6 | `memoire_isvd.py` | `mettre_a_jour_memoire_isvd` | 232 | Z | drapeau rangé dans l'exemplaire |
| Z05.7 | `principal.py` | `<module>` | 14–15 | Z | import des constantes |
| Z05.8 | `principal.py` | `_expression_mots_cles` | 967–975 | Z | _expression_mots_cles |
| Z05.9 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 1079–1087 | Z | gabarit : ponderer_trace_memoire |
| Z05.10 | `principal.py` | `executer` | 2077 | Z | branchement de la pondération sur la mise à jour de la mémoire |
| Z05.11 | `politique_endogene.py` | `<module>` | 9–10 | Z | copie des constantes dans le module initial |
| Z05.12 | `politique_endogene.py` | `ponderer_trace_memoire` | 35–41 | Z | ponderer_trace_memoire du module initial |
| Z05.13 | `politique_endogene.py` | `verifier_et_valider_code_politique` | 237–239 | Z | essai de ponderer_trace_memoire par le vérificateur |
| Z05.14 | `tests/test_auto_architecte_v6.py` | `test_v6_2_point_05_unification_mots_cles_multi_familles` | 302–312 | Z | essai hérité qui lit les constantes |
| Z05.15 | `tests/test_corrections_v5.py` | `_mots_des_affectations` | 205–215 | Z | aide d'essai qui lit les mots des affectations |
| Z05.16 | `tests/test_corrections_v5.py` | `test_c16_mots_cles_une_seule_source_module_initial_et_gabarit` | 218–243 | Z | essai de C-16 (une seule source) |
| Z05.17 | `tests/test_corrections_v5.py` | `test_c16_mot_cle_invalide_refuse_par_le_gabarit` | 246–250 | Z | essai de C-16 (mot invalide refusé) |
| Z05.18 | `tests/test_emprunts_v5_3.py` | `test_v5_3_journal_ablations_et_confirmation_multi_familles` | 133–150 | Z | essai hérité qui lit le drapeau du détecteur |

### Z06 — Exemple de format (`principal.py` l. 794) et consigne de formulation de la moisson (liste de départ)

**Raison.** Liste de départ. L'exemple de format est une chaîne écrite sur deux lignes : il commence l. 793. La consigne entière (l. 787–795) est un texte d'appel dont la sortie choisit les documents servis ensuite dans les consignes des tâches.

| entrée | fichier | fonction | lignes | statut | désignation |
|---|---|---|---|---|---|
| Z06.1 | `principal.py` | `_executer_moisson` | 787–795 | Z | consigne de formulation de la moisson, dont l'exemple de format (l. 793–794) |

### Z07 — Tout texte d'appel servi à un modèle pour une tâche (liste de départ, complétée)

**Raison.** Le texte que le code écrit dans les consignes des tâches : directement (consigne d'induction et ses arguments ; balises et bloc de moisson ; repli d'archive) ; par la mémoire (traces versées à la mémoire, dont celle du calibrateur, qui porte la vérité de la tâche ; résumé de mémoire servi dans les consignes) ; par la moisson (requêtes de réserve, de même nature que l'exemple de format de Z06 ; sujet fixe de la moisson des tâches ; assainissement et choix des passages de ce qui est servi).

| entrée | fichier | fonction | lignes | statut | désignation |
|---|---|---|---|---|---|
| Z07.1 | `principal.py` | `<module>` | 28–29 | Z | balises du bloc de moisson servi dans les consignes |
| Z07.2 | `principal.py` | `<module>` | 88–99 | Z | requêtes de réserve |
| Z07.3 | `principal.py` | `_sanitiser_donnee_externe` | 251–257 | Z | assainissement du texte extérieur servi |
| Z07.4 | `principal.py` | `_extraire_passages_denses_document` | 260–281 | Z | choix des passages d'un document servi |
| Z07.5 | `principal.py` | `_executer_moisson` | 880–883 | Z | trace d'une notice, versée à la mémoire |
| Z07.6 | `principal.py` | `_executer_moisson` | 928–931 | Z | trace d'un document, versée à la mémoire |
| Z07.7 | `principal.py` | `_executer_moisson` | 933–946 | Z | bloc de corpus servi dans les consignes |
| Z07.8 | `principal.py` | `_executer_moisson` | 953 | Z | assemblage du bloc de corpus |
| Z07.9 | `principal.py` | `_bloc_moisson_borne` | 1128–1132 | Z | _bloc_moisson_borne |
| Z07.10 | `principal.py` | `_construire_prompt_induction_entrainement` | 1135–1160 | Z | consigne d'induction (exemples à vérité) |
| Z07.11 | `principal.py` | `_traiter_tache` | 1789 | Z | trace d'une tâche de test, versée à la mémoire |
| Z07.12 | `principal.py` | `executer` | 1849–1852 | Z | trace du corpus d'archive, versée à la mémoire |
| Z07.13 | `principal.py` | `executer` | 1883 | Z | sujet fixe de la moisson des tâches |
| Z07.14 | `principal.py` | `executer` | 1896–1899 | Z | repli d'archive servi dans les consignes |
| Z07.15 | `principal.py` | `executer` | 1913–1918 | Z | arguments qui composent la consigne d'induction |
| Z07.16 | `principal.py` | `executer` | 1929 | Z | trace des règles induites, versée à la mémoire |
| Z07.17 | `principal.py` | `executer` | 1954–1957 | Z | trace du calibrateur interne, avec la vérité de la tâche, versée à la mémoire |
| Z07.18 | `memoire_isvd.py` | `resumer_memoire_pour_prompt` | 285–302 | Z | résumé de mémoire servi dans les consignes |

### Z08 — Exemples à vérité et leur choix (ajout depuis le code)

**Raison.** « Tout exemple » (§ 14) : le nombre et le choix des tâches d'entraînement montrées avec leur vérité dans la consigne d'induction (`_selection_stratifiee` choisit aussi les tâches du calibrateur interne et le pli de validation de la sonde) ; les tâches d'attaque de la métrique (textes, étiquettes, vérités, au vocabulaire de la banque depuis C-11).

| entrée | fichier | fonction | lignes | statut | désignation |
|---|---|---|---|---|---|
| Z08.1 | `principal.py` | `<module>` | 30 | Z | N_EXEMPLES_INDUCTION |
| Z08.2 | `principal.py` | `_selection_stratifiee` | 1109–1125 | Z | _selection_stratifiee : choix des tâches d'entraînement montrées avec leur vérité |
| Z08.3 | `metrique/attaques.json` | `(fichier entier)` | 1–62 | Z | tâches d'attaque : textes, étiquettes, vérités |

### Z09 — Chemin de la question ouverte (ajout depuis le code)

**Raison.** Consignes servies aux castes et à l'arbitre, analyse de leurs réponses, thèse retenue, réponse écrite et sa forme de repli, catalogue des rôles et des axes servis aux castes. Ce sont des textes d'appel servis à des modèles ; le § 14 interdit au correcteur d'écrire quoi que ce soit sur les questions ou leurs réponses ; aucun facteur du § 6 ne vise ce chemin. La l. 1234 (facteur F08) en est exceptée.

| entrée | fichier | fonction | lignes | statut | désignation |
|---|---|---|---|---|---|
| Z09.1 | `principal.py` | `_parser_contribution_question_ouverte` | 717–753 | Z | analyse des réponses des castes de la question |
| Z09.2 | `principal.py` | `_traiter_question_ouverte` | 1202–1233 | Z | question ouverte : début (moisson, castes) |
| Z09.3 | `principal.py` | `_traiter_question_ouverte` | 1235–1544 | Z | question ouverte : consignes, délibération, thèse retenue, réponse écrite |
| Z09.4 | `principal.py` | `executer` | 2046–2053 | Z | réponse de repli à la question |
| Z09.5 | `mitose_spectrale.py` | `planifier_castes_question_ouverte` | 124–130 | Z | catalogue des rôles et des axes servis aux castes de la question |

### Z10 — Identifiants des appels (ajout depuis le code)

**Raison.** Chaque appel est nommé par son rôle dans le journal du noyau ; le texte du pilote nomme le rôle de l'architecte dans sa liste d'arrêt (texte v4, l. 327), et des essais lisent les rôles. Changer un nom changerait l'identité d'appels lus hors de l'organisme. Le rôle de la validation de la sonde (l. 593) est dans Z04 ; les rôles de la question sont dans Z09.

| entrée | fichier | fonction | lignes | statut | désignation |
|---|---|---|---|---|---|
| Z10.1 | `principal.py` | `_entrainer_et_predire_sondes_traits` | 556 | Z | rôle d'appel d'un entraînement de sonde |
| Z10.2 | `principal.py` | `_entrainer_et_predire_sondes_traits` | 627 | Z | rôle d'appel d'une prédiction de sonde (celui de la validation, l. 593, est dans Z04) |
| Z10.3 | `principal.py` | `_executer_moisson` | 800 | Z | rôle d'appel de la formulation |
| Z10.4 | `principal.py` | `_executer_moisson` | 843 | Z | rôle d'appel d'une recherche |
| Z10.5 | `principal.py` | `_executer_moisson` | 913 | Z | rôle d'appel d'un téléchargement |
| Z10.6 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 1017 | Z | rôle d'appel de l'architecte |
| Z10.7 | `principal.py` | `executer` | 1923 | Z | rôle d'appel de l'induction |
| Z10.8 | `principal.py` | `executer` | 1944 | Z | rôle d'appel du calibrateur interne |
| Z10.9 | `mitose_spectrale.py` | `planifier_castes_par_mitose` | 84 | Z | rôle de la caste 1 |
| Z10.10 | `mitose_spectrale.py` | `planifier_castes_par_mitose` | 87 | Z | rôle de la caste 2 |
| Z10.11 | `mitose_spectrale.py` | `planifier_castes_par_mitose` | 90 | Z | rôle de la caste 3 |
| Z10.12 | `mitose_spectrale.py` | `planifier_castes_par_mitose` | 93 | Z | rôle des castes suivantes |

### Z11 — Instruments et documents de l'arbre (ajout depuis le code)

**Raison.** `metrique/` : la métrique externe, que le noyau applique aux sorties d'un organisme (`metrique/definition.md` l. 3) et que le code de l'organisme ne lit pas ; ce n'est pas un levier de l'organisme (ses tâches d'attaque sont dans Z08). `CONCEPTION.md` et `CORRECTIONS-v1.md` à `CORRECTIONS-v5.md` : hors des fichiers d'accompagnement du § 6 (seul un `CORRECTIONS-v<N>.md` nouveau y est), et R12. `manifeste.json` l. 2 et 4 : nom et point d'entrée, contrat du noyau ; les l. 3 et 5 (version, description) sont des fichiers d'accompagnement.

| entrée | fichier | fonction | lignes | statut | désignation |
|---|---|---|---|---|---|
| Z11.1 | `metrique/calculer.py` | `(fichier entier)` | 1–60 | Z | métrique externe |
| Z11.2 | `metrique/definition.md` | `(fichier entier)` | 1–15 | Z | définition de la métrique externe |
| Z11.3 | `metrique/__init__.py` | `(fichier entier)` | 1 | Z | sous-paquet de la métrique |
| Z11.4 | `CONCEPTION.md` | `(fichier entier)` | 1–162 | Z | conception |
| Z11.5 | `CORRECTIONS-v1.md` | `(fichier entier)` | 1–57 | Z | corrections antérieures |
| Z11.6 | `CORRECTIONS-v2.md` | `(fichier entier)` | 1–25 | Z | corrections antérieures |
| Z11.7 | `CORRECTIONS-v3.md` | `(fichier entier)` | 1–16 | Z | corrections antérieures |
| Z11.8 | `CORRECTIONS-v4.md` | `(fichier entier)` | 1–23 | Z | corrections antérieures |
| Z11.9 | `CORRECTIONS-v5.md` | `(fichier entier)` | 1–53 | Z | corrections antérieures |
| Z11.10 | `manifeste.json` | — | 2 | Z | nom (contrat du noyau) |
| Z11.11 | `manifeste.json` | — | 4 | Z | point d'entrée (contrat du noyau) |

## 3. Segments interdits dans des lignes de facteur

Le texte de ces segments n'est pas recopié (texte d'appel, ou clé du seuil) ; colonnes et empreinte suffisent à G5. Sur ces lignes, le reste appartient au facteur F04.

| segment | zone | fichier | ligne | fonction | colonnes | ligne de | empreinte du segment | désignation |
|---|---|---|---|---|---|---|---|---|
| Z03.s1 | Z03 | `principal.py` | 1009 | `_synthetiser_mutation_politique_endogene` | 41–80 | F04 | `3111a29c1c0ea117…` | plage de seuil_confiance_caste1 dans la consigne de l'architecte |
| Z03.s2 | Z03 | `principal.py` | 1011 | `_synthetiser_mutation_politique_endogene` | 92–121 | F04 | `42d9ae99c6ab30b8…` | valeur d'exemple de seuil_confiance_caste1 dans la consigne de l'architecte |
| Z03.s3 | Z03 | `principal.py` | 1039 | `_synthetiser_mutation_politique_endogene` | 51–74 | F04 | `e5c646fa0e50cf31…` | clé seuil_confiance_caste1 parmi les clés requises |

## 4. Frontière de l'exception « défaut du chemin des réponses »

**Ce qui porte la règle qui choisit une classe (R).** Ce qui décide de ce qui compte comme la réponse d'un modèle et de la façon de combiner les réponses : les champs lus pour l'étiquette et la confiance, le rapprochement avec les étiquettes autorisées, la validité d'un vote, la confiance lue hors de l'objet, la valeur par défaut et les bornes de la confiance, l'ordre de préférence entre plusieurs objets d'une même réponse ; les seuils du routage et leurs replis ; le vote de la sonde ; les votes des castes, l'accord, la discorde et l'arbitrage, les castes appelées, l'arrêt anticipé ; l'agrégation ; les données de la sonde servies à la règle. S'y ajoutent les zones Z03 et Z04, de statut R.

**Ce qui n'en est pas (E).** Ce qui trouve et lit ce que le modèle a écrit, ou règle le temps : réception d'une réponse, repérage et décodage des objets JSON, décodage des nombres, normalisation des chaînes comparées, entrées et sorties des fonctions, mécanique des appels, contrôles de temps et de budget avant un appel, ordre séquentiel ou parallèle des tâches, écriture du fichier des réponses, forme de réponse demandée dans la consigne.

| entrée | fonction | lignes de `principal.py` | R ou E | type | désignation |
|---|---|---|---|---|---|
| Z01.2 | `_construire_prompt_evaluation_tache` | 1191–1192 | E | format | forme de réponse demandée |
| Z02.1 | `_enregistrer_appel` | 313–344 | E | analyse | réception d'une réponse : statut, texte retenu, journal |
| Z02.2 | `_extraire_json_candidat` | 649–660 | E | analyse | repérage des objets JSON d'une réponse |
| Z02.3 | `_extraire_json_candidat` | 661 | R | — | ordre de préférence entre plusieurs objets JSON d'une même réponse |
| Z02.4 | `_extraire_json_candidat` | 662–668 | E | analyse | décodage de l'objet |
| Z02.5 | `_normaliser` | 671–673 | E | analyse | normalisation des chaînes comparées (étiquettes, familles, vérités) |
| Z02.6 | `_confiance_finie` | 676–681 | E | analyse | décodage d'un nombre fini |
| Z02.7 | `_parser_decision_tache` | 684–689 | E | analyse | entrée de l'analyse de la réponse d'une tâche |
| Z02.8 | `_parser_decision_tache` | 690–707 | R | — | champs qui portent l'étiquette et la confiance ; rapprochement avec les étiquettes autorisées ; confiance lue hors objet ; valeur par défaut et bornes de la confiance |
| Z02.9 | `_parser_decision_tache` | 708–709 | E | analyse | constat rendu |
| Z02.10 | `_parser_decision_tache` | 710 | R | — | validité du vote |
| Z02.11 | `_parser_decision_tache` | 711–714 | E | analyse | sortie de l'analyse |
| Z02.12 | `_faut_basculer` | 1598–1610 | E | délai | décision de passer les tâches de test en parallèle |
| Z02.13 | `_ecrire_reponses` | 1613–1616 | E | format | écriture atomique de reponses_test.json |
| Z02.14 | `_traiter_tache` | 1630–1647 | E | analyse | entrée de _traiter_tache ; sortie vide sans étiquette ou sans caste |
| Z02.15 | `_traiter_tache` | 1648–1672 | R | — | seuils du routage lus, avec leurs replis ; urnes des votes |
| Z02.16 | `_traiter_tache` | 1673 | E | analyse | textes de la tâche |
| Z02.17 | `_traiter_tache` | 1675–1697 | R | — | vote de la sonde ; caste 1 et son état |
| Z02.18 | `_traiter_tache` | 1698 | E | délai | temps et budget avant l'appel de la caste 1 |
| Z02.19 | `_traiter_tache` | 1702–1712 | E | analyse | appel de la caste 1, réception, analyse |
| Z02.20 | `_traiter_tache` | 1713–1740 | R | — | vote de la caste 1 ; accord, discorde, besoin d'arbitrage |
| Z02.21 | `_traiter_tache` | 1743–1744 | R | — | castes supplémentaires appelées |
| Z02.22 | `_traiter_tache` | 1745–1746 | E | délai | temps et budget avant chaque caste supplémentaire |
| Z02.23 | `_traiter_tache` | 1755–1765 | E | analyse | appel d'une caste supplémentaire, réception, analyse |
| Z02.24 | `_traiter_tache` | 1766–1772 | R | — | votes supplémentaires ; arrêt anticipé |
| Z02.25 | `_traiter_tache` | 1773–1774 | E | analyse | textes rendus |
| Z02.26 | `_traiter_tache` | 1775–1782 | R | — | agrégation : étiquette retenue et confiance finale |
| Z02.27 | `_traiter_tache` | 1783–1788 | E | format | détails rendus |
| Z02.28 | `_traiter_tache` | 1790 | E | format | sortie |
| Z02.29 | `executer` | 1961–1962 | E | format | résultats des tâches |
| Z02.30 | `_recevoir` | 1963–1972 | E | format | _recevoir : réponse rangée et écrite |
| Z02.31 | `executer` | 1973 | E | format | ligne vide entre les deux fonctions internes |
| Z02.32 | `_une` | 1974–1983 | E | délai | _une : appel de _traiter_tache |
| Z02.33 | `_une` | 1984–1986 | R | — | données de la sonde servies à la règle (C-15 : exactitude de validation seule) |
| Z02.34 | `_une` | 1987 | E | délai | _une : fin |
| Z02.35 | `executer` | 1988–2001 | E | délai | tâches de test en séquence, puis en parallèle |
| Z02.36 | `executer` | 2002–2009 | E | format | réponses rassemblées |
| Z02.37 | `executer` | 2044 | E | format | écriture finale des réponses |

- **Jamais sous l'exception :** une ligne R ou Z ; une source nouvelle d'étiquette ou de poids ; un changement de ce qui est retenu pour une réponse que le code lit déjà.
- **Lignes E qui servent aussi ailleurs.** `_normaliser` (l. 671–673) sert au score interne (l. 1951), à la sonde (l. 603, 623) et au routage (l. 694, 1680, 1722, 1728) ; `_extraire_json_candidat` (l. 649–668) sert à la formulation (l. 805, F08), à l'architecte (l. 1037, F04) et à la question (l. 718, Z09) ; `_confiance_finie` (l. 676–681) sert à la sonde, à l'architecte (l. 1040) et aux seuils du routage (l. 1623) ; `_enregistrer_appel` (l. 313–344) sert à tous les appels. Un défaut corrigé là sous l'exception touche aussi ces chemins : la pièce de périmètre le dit, et le contre-lecteur le revoit.

## 5. Points d'attention

- Les ajouts depuis le code (Z03, Z04, Z08, Z09, Z10, Z11, et le complément de Z02 et de Z07) sont des choix de cette pièce, chacun avec sa raison ; ils sont à confirmer par la contre-lecture (LISEZMOI, D3).
- `seuil_confiance_caste1` : gelé bien que le § 14 ouvre « le contrat de l'architecte » (LISEZMOI, D2).
- Rôles d'appel : la spécification du relevé mécanique n'est pas dans les pièces fournies (LISEZMOI, D4).
