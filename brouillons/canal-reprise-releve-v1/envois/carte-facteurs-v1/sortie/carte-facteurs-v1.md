# Carte des facteurs de conception de la v6.2.1 — v1

Écrite le 2026-10-26 à 06:41:54 UTC (heure lue sur `date -u` dans la commande qui écrit ce fichier) par un sous-agent neuf de la lignée conv-audit, sur le brief `LISEZMOI-brief-carte-facteurs-v1.md` (`d0d29df8dc60699cd9abf0f8c46d1057d00820828ffcfae14e8df6405fc80d7d`). L'auteur n'a écrit ni l'objet, ni ses textes, ni la boucle extérieure ; il n'a lu aucun résultat de course.

**Objet.** `organisme/` au commit `7ea32705c5437d91ed071dd95fb3209bb0b0035e` : la v6.2.1, 26 fichiers, empreinte d'arbre `4f13647a…` (vérifiée par conv-audit, non recalculée ici). Les 26 empreintes de fichiers ont été vérifiées contre `EMPREINTES-fournis-v1.txt`. Les numéros de ligne sont ceux de ces fichiers.

**Pièces sœurs.** Forme lisible par G5 : `carte-facteurs-v1.json` (`2aaedd08a719e93d2e18437377e9cc565dc4de230ef1af97b0a6e6ef807cec25`). Zones interdites : `zones-interdites-v1.md` et `zones-interdites-v1.json` (`0082519cc0ef2400c198c89a8504f52948e7abb9b7e35e113db9ba1319f0b342`). Méthode, doutes et table du brief : `LISEZMOI-carte-facteurs-v1.md`.

**Ce que la carte ne contient pas.** Aucun critère ni aucune stratégie de classement, aucun texte d'appel ni aucune consigne recopiés, aucun fait de course, aucun score, rien sur une tâche de la banque, aucune proposition de changement du code. Les consignes, les listes de mots et les seuils du routage sont désignés par fichier, fonction et lignes.

## 0. Comment lire la carte

1. **Entrée.** Une plage de lignes d'un fichier de `organisme/`, bornes comprises, avec la fonction la plus intérieure qui la contient toute (analyse `ast`) ; `<module>` hors de toute fonction.
2. **Appartenance.** Une ligne entière appartient à un facteur au plus, et jamais à la fois à un facteur et à une zone interdite.
3. **Lignes partagées.** Trois lignes portent deux facteurs. Elles n'appartiennent en entier à aucun facteur : chaque facteur y possède un segment (colonnes de caractères comptées à partir de 1, bornes comprises), et le reste de la ligne n'est à personne (§ 5).
4. **Segments interdits.** Trois lignes de F04 portent un segment gelé de la zone Z03 (§ 5).
5. **Points hors boucle.** Les seuils 0,01 et 0,03 sont des segments gelés dans les lignes de leur facteur (§ 4).
6. **Un facteur à la fois.** Une correction ne touche que les lignes et les segments d'un seul facteur, plus les fichiers d'accompagnement du § 6 du protocole. Pour F04 (« un élément du contrat ») et F07 (« une borne »), un seul élément ou une seule borne par correction.
7. **F09** (défaut de code nommé) n'a pas de lignes propres : son domaine est le reste du code (F09, ci-dessous).
8. **Valeurs.** Une valeur numérique ne désigne jamais un facteur : les mêmes valeurs reparaissent ailleurs pour d'autres grandeurs.
9. **Insertions** (proposition pour G5). Des lignes insérées entre les lignes n et n + 1 appartiennent au facteur X si n et n + 1 sont à X en entier, ou si l'une est à X en entier et l'autre libre (ni facteur, ni segment, ni zone) ; en tête ou en fin de fichier, la seule voisine compte ; sinon le bloc est refusé.

## 1. Vue d'ensemble

| facteur | nom | origine | fichiers et lignes |
|---|---|---|---|
| F01 | nombre minimal de rondes avant la déclaration de fin | liste du § 6 | `principal.py` 2102, 2104 (segment), 2106 |
| F02 | nombre de tâches d'entraînement du score interne | liste du § 6 | `principal.py` 31, 1932 |
| F03 | les deux seuils du critère de fin (un seul facteur, tranché par la carte) | liste du § 6 | `principal.py` 2103 (segment), 2104 (segment) |
| F04 | un élément du contrat de l'architecte | liste du § 6 | `principal.py` 1003–1016, 1018–1045, 1047–1053, 1099–1107 |
| F05 | la mutation en génération notée | liste du § 6 | `principal.py` 988–996, 997 (segment), 998 |
| F06 | le retour arrière | liste du § 6 | `memoire_isvd.py` 104, 118–121, 123–139, 240–248, 259–260 |
| F07 | une borne interne par tâche | liste du § 6 | `principal.py` 42, 1674, 1943 |
| F08 | le chemin de formulation de la moisson | liste du § 6 | `principal.py` 46, 782–783, 786, 796–799, 801–817, 820–825, 1234, 1892 |
| F09 | un défaut de code nommé | liste du § 6 | complément du code (voir F09) |
| F10 | nombre minimal d'exemplaires de mémoire de la branche « qualité » du critère de fin | hors liste, révélé par le code | `principal.py` 2103 (segment) |
| F11 | déclaration de fin forcée à la dernière ronde permise | hors liste, révélé par le code | `principal.py` 1798, 2105 |
| F12 | mutation en conception | hors liste, révélé par le code | `principal.py` 997 (segment) |
| F13 | castes des tâches (planification par mitose) ; porte aussi « appels par tâche » | hors liste du § 6 ; nommé au § 14 (castes, bornes internes) | `mitose_spectrale.py` 59–83, 85–86, 88–89, 91–92, 94–101 ; `principal.py` 1871–1876 |
| F14 | castes de la question ouverte | hors liste du § 6 ; nommé au § 14 (castes) | `mitose_spectrale.py` 104–123, 131–147 |
| F15 | forme de la règle de récompense interne (module initial, gabarit, replis) | hors liste du § 6 ; nommé au § 14 (forme, gabarit) | `politique_endogene.py` 3–6, 13–23, 26–32 ; `principal.py` 48–53, 957–964, 1055–1076 |
| F16 | garde de temps (part du temps alloué aux appels) | hors liste du § 6 ; « délais » du § 14 | `principal.py` 32, 2039–2040 |

## 2. Facteurs de la liste de départ (§ 6 du protocole)

### F01 — nombre minimal de rondes avant la déclaration de fin

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F01.1 | `principal.py` | `executer` | 2102 | — | indice de ronde r_idx tiré de ronde_conception (absente ou nulle : 1) ; lu aussi par F11 (l. 2105) |
| F01.2 | `principal.py` | `executer` | 2104 | 36–45 | minimum de rondes de la branche « convergence » |
| F01.3 | `principal.py` | `executer` | 2106 | — | disjonction de la déclaration : seule ligne où une condition de ronde peut valoir pour toutes les branches |

- **Bougent ensemble.** Le minimum de la branche « convergence » (F01.2) et l'indice de ronde qu'il compare (F01.1) : le minimum ne se lit que par cet indice, qui vaut 1 pour une `ronde_conception` absente ou nulle. La branche « qualité » (l. 2103) n'a aucune condition de ronde : par elle, une déclaration reste possible dès `r_idx = 1`. Un minimum qui vaudrait pour toute la déclaration ne peut se poser, sans toucher les segments de F03 et de F10, qu'à la ligne de la disjonction (F01.3) : c'est pourquoi cette ligne est à F01. Sur elle, F01 ne pose ou ne change qu'une condition de ronde ; G5 ne voit que la ligne, le contre-lecteur vérifie le reste.
- **Liens.** F11 lit le même indice (l. 2105) : changer F01.1 déplace aussi la dernière ronde de F11, et la pièce de périmètre le dit. Ce que vaut « deux rondes » dépend de la numérotation de `ronde_conception` par le noyau, que les pièces fournies ne donnent pas (LISEZMOI, D5).
- **Essais hérités.** `tests/test_emprunts_v5_3.py::test_v5_3_phase_conception_ecrit_fin_conception_json` (l. 190–227).

### F02 — nombre de tâches d'entraînement du score interne

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F02.1 | `principal.py` | `<module>` | 31 | — | N_VERIFICATIONS : nombre de tâches du score interne hors conception |
| F02.2 | `principal.py` | `executer` | 1932 | — | nb_verifs : 4 en conception, N_VERIFICATIONS sinon |

- **Bougent ensemble.** Le nombre en conception (4) et `N_VERIFICATIONS` hors conception : une seule expression (l. 1932) choisit l'un ou l'autre ; tous deux fixent le nombre d'appels `calibrateur_interne` (l. 1933–1947), donc le nombre de scores dont la moyenne est le score interne (l. 1953 ; moyenne l. 2029 et l. 2095–2099).
- **Hors du facteur.** Le choix des tâches (`_selection_stratifiee`, l. 1109–1125 : zone Z08) et la consigne servie (zone Z01).
- **Liens.** Le score interne est lu par F03 (l. 2103–2104), par la consigne de l'architecte (F04, l. 1005) et par la métrique proposée (l. 2120). La réserve d'appels hors tests de la mitose (F13, `mitose_spectrale.py` l. 68) couvre ces appels.
- **Essais hérités.** `tests/test_corrections_v1.py::test_c04_l_induction_voit_les_deux_familles` (l. 122–135).

### F03 — les deux seuils du critère de fin : un seul facteur

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F03.1 | `principal.py` | `executer` | 2103 | 32–58 | seuil de la branche « qualité » |
| F03.2 | `principal.py` | `executer` | 2104 | 51–77 | seuil de la branche « convergence » |

**Tranché : un seul facteur.** Raisons tirées du code :

1. Les deux seuils comparent la même grandeur, `score_interne_moyen` (l. 2095–2099), par le même opérateur.
2. Ce sont deux branches d'une seule disjonction (l. 2106), qui écrit un seul fichier, `fin_conception.json` (l. 2107–2118), sous la même étiquette de critère (l. 2108), quelle que soit la branche.
3. Le rôle de chacun dépend de l'autre. Tant que 0,65 reste sous 0,78, tout score qui passe 0,78 passe 0,65 : à partir de `r_idx = 2`, la branche à 0,78 n'ajoute rien, et elle ne décide qu'à `r_idx = 1` ; la branche à 0,65 ne décide qu'à partir de `r_idx = 2`. Porter l'un au-delà de l'autre change ce que fait l'autre : deux facteurs séparés ne seraient pas deux leviers indépendants.

Le minimum de rondes (F01) et le nombre minimal d'exemplaires (F10) tiennent sur les mêmes lignes mais comparent d'autres grandeurs (indice de ronde, taille de la mémoire), qui ne peuvent pas croiser un seuil de score : ils restent des facteurs à part, séparés par segments (§ 5).

- **Bougent ensemble.** 0,78 et 0,65.
- **Liens.** Le score vient de F02 (nombre de tâches) et de F15 (forme de la règle) ; sa valeur sans aucun score (l. 2098) n'est dans aucun facteur.
- **Essais hérités.** `tests/test_emprunts_v5_3.py::test_v5_3_phase_conception_ecrit_fin_conception_json` (l. 190–227). L'essai attend un score déclaré au moins égal au seuil de la branche « qualité » (l. 227).

### F04 — un élément du contrat de l'architecte

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F04.1 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 1003–1016 | — | consigne de l'architecte (segments gelés l. 1009 et 1011 : zone Z03) ; appel ; plafond de jetons (l. 1016) |
| F04.2 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 1018–1045 | — | fin de l'appel ; échec ; refus du code brut (C-17) ; objet JSON ; clés requises (segment gelé l. 1039 : zone Z03) ; filtre du nom ; bornes d'alpha (l. 1044) et de poids_brier (l. 1045) |
| F04.3 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 1047–1053 | — | poids_tsallis tiré de poids_brier ; en-tête du gabarit et constantes écrites (SEUIL_CASTE1, l. 1054, gelé : zone Z03) |
| F04.4 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 1099–1107 | — | contrôle du code du gabarit (seul appel du vérificateur, l. 1102) et issue |

Un seul élément par correction :

| élément | désignation | lignes de `principal.py` | précision |
|---|---|---|---|
| F04-a | plage d'alpha | 1008, 1011, 1039, 1044, 1051 | l. 1008, 1011 et 1039 en partie |
| F04-b | plage de poids_brier | 1009, 1011, 1039, 1045, 1047, 1052–1053 | l. 1009, 1011 et 1039 en partie, hors segments gelés |
| F04-c | ce que la consigne montre à l'architecte | 1004–1007 | — |
| F04-d | forme de la réponse demandée | 1010–1011 | l. 1011 hors segment gelé |
| F04-e | règles d'acceptation de la réponse | 1021–1022, 1024–1043, 1099–1107 | l. 1039 hors segment gelé |
| F04-f | plafond de jetons de l'appel | 1016 | — |
| F04-g | nom de la politique | 1011, 1043, 1050 | l. 1011 en partie |

- **Bougent ensemble, dans un élément.** La plage dite dans la consigne, la valeur d'exemple, la clé requise, la borne appliquée et la constante écrite par le gabarit : la consigne annonce la plage (l. 1008–1009), la borne l'applique (l. 1044–1045), l'exemple doit y tomber (l. 1011), le gabarit écrit la valeur bornée (l. 1051–1053). Pour `poids_brier`, `poids_tsallis` en découle (l. 1047 et 1053).
- **Gelé dans les lignes de F04.** Tout ce qui porte `seuil_confiance_caste1` : segments des l. 1009, 1011 et 1039, l. 1046 et l. 1054 (zone Z03). Ce paramètre du contrat est un seuil du routage de la règle qui choisit une classe (`_traiter_tache`, l. 1664, 1724, 1732), et le § 14 interdit d'écrire un tel seuil. Le rôle d'appel (l. 1017) est en zone Z10.
- **Hors de F04, mais contrainte.** Le vérificateur (`politique_endogene.py` : `verifier_proprete_stricte_recompense`, l. 95–148 ; `verifier_et_valider_code_politique`, l. 151–254) doit accepter le gabarit sur toute la plage bornée. La forme de la règle écrite par le gabarit est F15.
- **Rappels du § 14.** Jamais un contenu qui lie une récompense à un trait du texte d'une tâche ou à une classe. Une correction qui retirerait à la v6.2.1 sa réécriture de la règle la ferait sortir de la question de (b) : la pièce de correction le dit.
- **Essais hérités.** `tests/test_corrections_v5.py::test_c17_code_brut_refuse_sans_validation_ni_execution` (l. 281–299) ; `tests/test_corrections_v5.py::test_c17_json_fenced_toujours_accepte_par_le_gabarit` (l. 302–315) ; `tests/test_corrections_v5.py::test_c17_gabarit_aux_bornes_et_au_dela_accepte_et_valide_en_temps_borne` (l. 318–342) ; `tests/test_auto_architecte_v6.py::test_v6_auto_reecriture_effective_dans_successeur_sous_stagnation` (l. 77–109) ; `tests/test_auto_architecte_v6.py::test_v6_1_successeur_mute_s_importe_et_tourne_dans_processus_neuf` (l. 112–167) ; `tests/test_auto_architecte_v6.py::test_v6_rejet_mutation_reward_hacking_garde_politique_saine` (l. 170–212) ; `tests/test_auto_architecte_v6.py::test_v6_2_point_08_json_incomplet_refuse_et_seuils_routage_verifies` (l. 342–370).

### F05 — la mutation en génération notée

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F05.1 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 988–996 | — | historique ; mutation forcée par le contexte ; détection de stagnation (point hors boucle PHB-1, l. 994) |
| F05.2 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 997 | 38–88 | déclencheurs hors conception : mutation forcée, stagnation à partir de la génération 1 |
| F05.3 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 998 | — | sortie sans mutation |

- **Bougent ensemble.** Les trois déclencheurs hors conception, qui forment ensemble la partie hors conception de la condition (F05.2) : la mutation forcée par le contexte (`autoriser_mutation_code`, l. 989), la stagnation (l. 991–995 : les deux derniers scores de l'historique, entrées sans score écartées, l. 993 ; seuil 0,01, point hors boucle PHB-1) et la génération minimale (`generation >= 1`). La mutation forcée n'agit qu'hors conception, puisqu'en conception le premier terme de la condition est déjà vrai. Couper la mutation en génération notée demande les deux termes : d'où un seul segment.
- **Seuil 0,01.** Celui de la l. 994 appartient à F05 (§ 4).
- **Copies.** Le même test de stagnation est recopié dans la mitose (`mitose_spectrale.py` l. 73–76 et 115–118), avec sa propre valeur 0,01 : ces copies appartiennent à F13 et à F14 et sont indépendantes dans le code.
- **Liens.** L'appel de la mutation (l. 2028–2037) et l'assemblage du successeur (`_propager_successeur`, l. 1547–1595) ne sont dans aucun facteur ; le code muté passe par F04 (contrat) et F15 (forme). Même rappel du § 14 sur la question de (b).
- **Essais hérités.** `tests/test_auto_architecte_v6.py::test_v6_auto_reecriture_effective_dans_successeur_sous_stagnation` (l. 77–109).

### F06 — le retour arrière

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F06.1 | `memoire_isvd.py` | `mettre_a_jour_memoire_isvd` | 104 | — | archive généalogique lue |
| F06.2 | `memoire_isvd.py` | `mettre_a_jour_memoire_isvd` | 118–121 | — | scores du noyau reportés sur les entrées de l'archive |
| F06.3 | `memoire_isvd.py` | `mettre_a_jour_memoire_isvd` | 123–139 | — | retour arrière : condition (l. 125), meilleur ancêtre noté, écart (point hors boucle PHB-4, l. 132), restauration |
| F06.4 | `memoire_isvd.py` | `mettre_a_jour_memoire_isvd` | 240–248 | — | tenue de l'archive : génération ajoutée, exemplaires gardés par ancêtre (l. 246), profondeur (l. 248) |
| F06.5 | `memoire_isvd.py` | `mettre_a_jour_memoire_isvd` | 259–260 | — | drapeaux du retour arrière rendus dans l'état de mémoire |

- **Bougent ensemble.** L'écart au meilleur ancêtre (0,03, point hors boucle PHB-4), le choix du meilleur ancêtre noté (l. 129–131), les champs restaurés (l. 133–137), le report des scores du noyau sur l'archive (l. 118–121) et la tenue de l'archive (l. 240–248 : génération ajoutée, exemplaires gardés par ancêtre l. 246, profondeur l. 248) : le retour arrière ne restaure que depuis l'archive, et ses candidats sont les entrées notées de l'archive.
- **Interrupteur du mécanisme.** La condition de la l. 125.
- **Seuil 0,03.** Il appartient à F06 (§ 4).
- **Liens.** L'état restauré nourrit la mise à jour de la mémoire (l. 167–170, hors facteur) ; le résumé de mémoire servi dans les consignes le mentionne (l. 295, zone Z07) ; la table des scores par génération (l. 107–116) est lue aussi par le journal d'ablations (l. 141–165) ; ni l'une ni l'autre n'est dans un facteur.
- **Essais hérités.** `tests/test_emprunts_v5_3.py::test_v5_3_archive_genealogique_retour_arriere_sur_regression_score` (l. 107–130).

### F07 — une borne interne par tâche

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F07.1 | `principal.py` | `<module>` | 42 | — | MAX_TOKENS_TACHE |
| F07.2 | `principal.py` | `_traiter_tache` | 1674 | — | plafond de jetons d'un appel de tâche de test |
| F07.3 | `principal.py` | `executer` | 1943 | — | plafond de jetons d'un appel du calibrateur interne |

- **Une seule borne par tâche est une constante propre de l'organisme** : le plafond de jetons d'un appel de tâche, `MAX_TOKENS_TACHE` (l. 42), lu pour les tâches de test (l. 1674) et pour le calibrateur interne (l. 1943). Instance unique : F07-a.
- **Bougent ensemble.** La constante et ses deux lectures : les deux appels servent la même consigne (zone Z01 ; arguments l. 1699–1701 et 1936–1939) et passent par la même analyse (zone Z02).
- **Les autres bornes par tâche.** « Appels par tâche » est le nombre de castes recrutées (F13, `mitose_spectrale.py` l. 68–78) : mêmes lignes, donc un seul facteur, F13, avec la condition du § 14 sur les castes. « Délai par tâche » : le code n'en a pas ; la garde de temps est globale (F16).
- **Au-dessus.** Le plafond du noyau (`max_tokens_appel`, lu par `_plafond_tokens_effectif`, l. 192–197) borne la valeur : c'est une borne du noyau, pas de l'organisme.
- **Essais hérités.** aucun repéré.

### F08 — le chemin de formulation de la moisson

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F08.1 | `principal.py` | `<module>` | 46 | — | MAX_TOKENS_MOISSON_REQUETES (plafond de l'appel de formulation) |
| F08.2 | `principal.py` | `_executer_moisson` | 782–783 | — | listes que la formulation remplit |
| F08.3 | `principal.py` | `_executer_moisson` | 786 | — | condition de l'appel de formulation |
| F08.4 | `principal.py` | `_executer_moisson` | 796–799 | — | appel de formulation (son rôle, l. 800, est gelé : zone Z10) |
| F08.5 | `principal.py` | `_executer_moisson` | 801–817 | — | fin de l'appel ; lecture des requêtes et des références rendues |
| F08.6 | `principal.py` | `_executer_moisson` | 820–825 | — | complément par les requêtes de réserve (la liste, l. 88–99, est gelée : zone Z07) |
| F08.7 | `principal.py` | `_traiter_question_ouverte` | 1234 | — | formulation permise pour la question ouverte |
| F08.8 | `principal.py` | `executer` | 1892 | — | formulation permise pour la moisson des tâches (en conception seulement) |

- **Bougent ensemble.** La condition de l'appel (l. 786), les deux interrupteurs posés aux appels (`autoriser_appel_formulation` : moisson des tâches, en conception seulement, l. 1892 ; question ouverte, toujours, l. 1234), la lecture des requêtes et des références rendues (l. 804–817), le complément par la réserve (l. 820–825) et le plafond de jetons de l'appel (l. 46, lu l. 799) : ensemble, ils décident si les requêtes viennent d'un appel de modèle ou de la réserve, et dans quelles phases.
- **Gelé sur ce chemin.** La consigne de formulation et son exemple de format (zone Z06, l. 787–795), la liste de réserve (zone Z07, l. 88–99), le sujet fixe de la moisson des tâches (zone Z07, l. 1883), le rôle d'appel (zone Z10, l. 800). Les clés lues (l. 806 et 812) répondent à l'exemple de format gelé : les changer seules casse le chemin.
- **Hors du facteur.** Le nombre de recherches et de téléchargements (l. 784, 819, 832, 904–905) et les plafonds de la moisson (l. 34–40).
- **Essais hérités.** `tests/test_moissonneur_v5.py::test_v5_moisson_nominale_question_ouverte` (l. 203–237) ; `tests/test_moissonneur_v5.py::test_v5_moisson_sur_flux_taches_sans_fuite_de_test` (l. 308–333).

### F09 — un défaut de code nommé : forme de la déclaration

- **Domaine.** Les lignes de `principal.py`, `memoire_isvd.py`, `politique_endogene.py` et `mitose_spectrale.py` qui ne sont à aucun autre facteur (ni en entier, ni par segment) et dans aucune zone interdite :
  - `principal.py` : 1060 lignes en 62 plages : 1–13, 16–27, 33–41, 43–45, 47, 54–87, 100–250, 258–259, 282–312, 345–555, 557–588, 620–626, 628–632, 634–648, 669–670, 674–675, 682–683, 715–716, 754–781, 784–785, 818–819, 826–842, 844–879, 884–912, 914–927, 932, 947–952, 954–956, 965–966, 976–987, 999–1002, 1077–1078, 1097–1098, 1108, 1126–1127, 1133–1134, 1161–1162, 1194–1201, 1545–1597, 1611–1612, 1617–1618, 1628–1629, 1791–1797, 1799–1848, 1853–1870, 1877–1882, 1884–1891, 1893–1895, 1900–1912, 1919–1922, 1924–1928, 1930–1931, 1933–1935, 1940–1942, 1945–1953, 1958–1960, 2010–2038, 2041–2043, 2045, 2054–2076, 2078–2101, 2107–2184.
  - `memoire_isvd.py` : 231 lignes en 12 plages : 1–80, 83–84, 90–103, 105–117, 122, 140–185, 196–203, 205–226, 228–231, 233–239, 249–258, 261–284.
  - `politique_endogene.py` : 191 lignes en 9 plages : 1–2, 8, 11–12, 24–25, 33–34, 42–43, 53–84, 93–236, 251–254.
  - `mitose_spectrale.py` : 54 lignes en 3 plages : 1–42, 49–58, 102–103.
- **Sous l'exception « défaut du chemin des réponses » seulement,** les lignes de statut E de `zones-interdites-v1` (format, analyse de la réponse, délai) ; jamais une ligne R ni une ligne Z. Les essais, les documents et le manifeste suivent les règles des fichiers d'accompagnement (§ 6 du protocole).
- **Un défaut dans les lignes d'un autre facteur** se déclare sous ce facteur, avec son nom de défaut, et compte pour lui.
- **Forme de la déclaration** (dans la pièce de périmètre, avant le diff) :
  1. `facteur : F09 — défaut de code nommé` ; s'il y a lieu, `exception : défaut du chemin des réponses — format | analyse de la réponse | délai`.
  2. `nom du défaut` : un nom court, qui dit le défaut en termes de code.
  3. `lieu` : fichier, fonction, lignes au commit `7ea3270`, toutes dans le domaine (sous l'exception, dans des lignes E).
  4. `ce que fait le code` : le comportement tel qu'écrit, lu dans le code, sans fait de course.
  5. `pourquoi c'est un défaut` : la pièce de l'arbre que le code contredit (commentaire, docstring, `CONCEPTION.md`, un `CORRECTIONS-v*.md`, un essai hérité, le contrat du noyau tel que l'arbre le dit), ou une erreur Python atteinte par une entrée construite. Le verdict qui motive la correction se cite dans la pièce de correction, jamais dans un fichier de l'organisme.
  6. `ce qui change, ce qui ne change pas` : aucun paramètre d'un autre facteur, aucune ligne de zone interdite ; sous l'exception, aucune ligne R, et la déclaration que la règle qui choisit une classe ne change pas.
  7. `essais` : un cas sain et l'artefact (R5) dans `tests/test_corrections_v<N>.py` ; un essai hérité adapté seulement si la correction l'exige, avec sa raison.

## 3. Facteurs révélés par le code, hors de la liste (déclarés comme tels)

Critère d'ajout : un levier que la liste de départ ne couvre qu'en partie (F10, F11 et F12, détachés de F03, F01 et F05), ou que le § 14 nomme comme modifiable sans que le § 6 le liste (F13, F14, F15, F16). Les autres mécanismes vus dans le code ne sont pas érigés en facteurs (§ 6).

### F10 — nombre minimal d'exemplaires de mémoire de la branche « qualité »

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F10.1 | `principal.py` | `executer` | 2103 | 64–112 | nombre minimal d'exemplaires de mémoire de la branche « qualité » |

- **Pourquoi à part.** C'est la seconde condition de la branche à 0,78 : la taille de la mémoire après sa mise à jour (exemplaires retenus, `memoire_isvd.py` l. 238). Autre grandeur que le score (F03) et que la ronde (F01) ; même ligne que F03, séparée par segment (§ 5).
- **Essais hérités.** `tests/test_emprunts_v5_3.py::test_v5_3_phase_conception_ecrit_fin_conception_json` (l. 190–227).

### F11 — déclaration de fin forcée à la dernière ronde permise

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F11.1 | `principal.py` | `executer` | 1798 | — | rondes_conception_max lu du contexte |
| F11.2 | `principal.py` | `executer` | 2105 | — | déclaration à la dernière ronde permise |

- **Pourquoi à part.** Un maximum, lu de `rondes_conception_max`, n'est pas le minimum de F01. Il lit l'indice de ronde de F01 (l. 2102). Le terme `derniere_ronde` de la disjonction (l. 2106) est sur la ligne de F01 ; l'interrupteur de F11 est la l. 2105.
- **Essais hérités.** `tests/test_emprunts_v5_3.py::test_v5_3_phase_conception_ecrit_fin_conception_json` (l. 190–227).

### F12 — mutation en conception

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F12.1 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 997 | 13–33 | déclencheur en conception |

- **Pourquoi à part.** En conception, la mutation est tentée à chaque ronde : c'est un autre levier que la mutation en génération notée (F05), sur la même ligne, séparé par segment (§ 5). Même rappel du § 14 sur la question de (b).
- **Essais hérités.** `tests/test_corrections_v5.py::test_c17_gabarit_aux_bornes_et_au_dela_accepte_et_valide_en_temps_borne` (l. 318–342).

### F13 — castes des tâches ; « appels par tâche »

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F13.1 | `mitose_spectrale.py` | `planifier_castes_par_mitose` | 59–83 | — | espèces ; appels restants ; réserve hors tests (l. 68) ; budget par tâche (l. 69–70) ; pression d'exploration (point hors boucle PHB-2, l. 75) ; nombre de castes (l. 78) ; début de l'attribution |
| F13.2 | `mitose_spectrale.py` | `planifier_castes_par_mitose` | 85–86 | — | mode de la caste 1 ; condition suivante (noms de rôle gelés : zone Z10) |
| F13.3 | `mitose_spectrale.py` | `planifier_castes_par_mitose` | 88–89 | — | mode de la caste 2 ; condition suivante |
| F13.4 | `mitose_spectrale.py` | `planifier_castes_par_mitose` | 91–92 | — | mode de la caste 3 ; condition suivante |
| F13.5 | `mitose_spectrale.py` | `planifier_castes_par_mitose` | 94–101 | — | mode des castes suivantes ; castes rendues |
| F13.6 | `principal.py` | `executer` | 1871–1876 | — | appel de la planification : espèces, budget, nombre de tâches de test, historique |

- **Origine.** Le § 14 nomme « les castes, mais pas tant que HC-P4-06 est tenue sous un budget inchangé ». F13 porte aussi la borne « appels par tâche » du § 14 : le nombre de castes recrutées est le nombre maximal d'appels par tâche de test. La condition du § 14 vaut donc pour toute correction de F13.
- **Bougent ensemble.** La réserve d'appels hors tests (l. 68), les appels pour les tests et le budget par tâche (l. 69–70), la pression d'exploration (l. 72–76 ; 0,01, point hors boucle PHB-2), la cible et son plafond (l. 78) : ensemble, ils fixent le nombre de castes ; l'appel (`principal.py` l. 1871–1876) passe le nombre de tâches de test.
- **Gelé.** Les noms de rôle (l. 84, 87, 90 et 93 : zone Z10).
- **Liens.** La réserve couvre les appels hors tests (induction, F02, F08, F05 et F12) ; le routage et l'arrêt anticipé (zone Z02) décident combien des castes recrutées votent.
- **Essais hérités.** `tests/test_corrections_v5.py::test_c14_sans_sonde_comportement_inchange_toutes_les_castes_deliberent` (l. 97–117) ; `tests/test_corrections_v5.py::test_c14_une_seule_caste_aucun_arbitrage` (l. 120–128).

### F14 — castes de la question ouverte

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F14.1 | `mitose_spectrale.py` | `planifier_castes_question_ouverte` | 104–123 | — | espèces ; appels restants ; pression d'exploration (point hors boucle PHB-3, l. 117) ; nombre de castes (l. 120–122) |
| F14.2 | `mitose_spectrale.py` | `planifier_castes_question_ouverte` | 131–147 | — | attribution des rôles du catalogue (catalogue gelé : zone Z09) et des modes |

- **Origine.** Les castes du § 14, pour la question ouverte.
- **Bougent ensemble.** La cible (l. 120–122), la pression d'exploration (l. 114–118 ; 0,01, point hors boucle PHB-3) et l'attribution des rôles (l. 132–146).
- **Gelé.** Le catalogue des rôles et des axes (l. 124–130 : zone Z09).
- **Essais hérités.** `tests/test_question_ouverte_v4.py::test_v4_question_ouverte_nominale_ecrit_reponse_et_organisation` (l. 54–123).

### F15 — forme de la règle de récompense interne

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F15.1 | `politique_endogene.py` | `<module>` | 3–6 | — | nom, exposant et poids de la règle initiale |
| F15.2 | `politique_endogene.py` | `recompense_interne` | 13–23 | — | recompense_interne du module initial |
| F15.3 | `politique_endogene.py` | `code_objectif_sonde` | 26–32 | — | objectif de la sonde du module initial |
| F15.4 | `principal.py` | `<module>` | 48–53 | — | objectif de secours de la sonde |
| F15.5 | `principal.py` | `_calculer_score_bregman_tsallis` | 957–964 | — | appel de la règle pour le score interne, et son repli |
| F15.6 | `principal.py` | `_synthetiser_mutation_politique_endogene` | 1055–1076 | — | gabarit : recompense_interne et objectif de la sonde écrits dans le module muté |

- **Origine.** Le § 14 nomme « la règle de récompense interne : sa forme, les bornes de ses paramètres, son gabarit ».
- **Bougent ensemble.** La règle du module initial (`politique_endogene.py` l. 13–23) et celle du gabarit (`principal.py` l. 1057–1067) sont la même formule écrite deux fois : la première mutation acceptée remplace l'une par l'autre. L'objectif de la sonde (module initial, l. 26–32 ; secours, l. 48–53 ; gabarit, l. 1070–1076) reprend les poids de la règle (l. 5–6 ; dans le gabarit, les poids bornés par F04). Le repli du score (l. 957–964) remplace la règle quand elle échoue.
- **Contrainte hors facteur.** Le vérificateur doit accepter la forme (ancrages et propreté, `politique_endogene.py` l. 95–148).
- **Rappel du § 14.** Jamais un contenu qui lie une récompense à un trait du texte d'une tâche ou à une classe.
- **Essais hérités.** `tests/test_auto_architecte_v6.py::test_v6_verificateur_proprete_stricte_accepte_bregman_et_rejette_reward_hacking` (l. 13–26) ; `tests/test_auto_architecte_v6.py::test_v6_2_point_13_metrique_proposee_reflete_alpha_actif` (l. 384–404).

### F16 — garde de temps

| entrée | fichier | fonction | lignes | colonnes | désignation |
|---|---|---|---|---|---|
| F16.1 | `principal.py` | `<module>` | 32 | — | PART_TEMPS_APPELS |
| F16.2 | `principal.py` | `executer` | 2039–2040 | — | constat de la garde de temps (répète la valeur) |

- **Origine.** Les « délais » du § 14.
- **Bougent ensemble.** La part (l. 32) et le constat qui la répète (l. 2040). La constante est lue par `_temps_ok` (l. 112–116), par `_temps_suffisant_pour_moisson` (l. 119–129) et par `_faut_basculer` (l. 1609, zone Z02).
- **Pas les bornes du GO.** Le temps alloué vient du noyau (`temps_max_s`).
- **Essais hérités.** `tests/test_corrections_v1.py::test_c05_garde_de_temps_reponses_et_successeur_ecrits` (l. 139–154) ; `tests/test_moissonneur_v5.py::test_v5_garde_de_temps_bloque_la_moisson_tardive` (l. 349–371).

## 4. Seuils 0,01 et 0,03 : à quel facteur, et comment G5 les reconnaît

| point | valeur | facteur | fichier | ligne | fonction | colonnes | texte | désignation |
|---|---|---|---|---|---|---|---|---|
| PHB-1 | 0,01 | F05 | `principal.py` | 994 | `_synthetiser_mutation_politique_endogene` | 59–65 | `<= 0.01` | stagnation : déclencheur de la mutation en génération notée |
| PHB-2 | 0,01 | F13 | `mitose_spectrale.py` | 75 | `planifier_castes_par_mitose` | 59–65 | `<= 0.01` | stagnation : pression d'exploration des castes des tâches |
| PHB-3 | 0,01 | F14 | `mitose_spectrale.py` | 117 | `planifier_castes_question_ouverte` | 59–65 | `<= 0.01` | stagnation : pression d'exploration des castes de la question |
| PHB-4 | 0,03 | F06 | `memoire_isvd.py` | 132 | `mettre_a_jour_memoire_isvd` | 71–76 | `> 0.03` | écart au meilleur ancêtre qui déclenche le retour arrière |

- **0,01 (stagnation).** Trois occurrences, chacune dans les lignes de son facteur. Le texte du pilote rattache la stagnation à la mutation (`principal.py` l. 991–998) : PHB-1 (F05) est le point qui répond à « 0,01 (stagnation) ». PHB-2 (F13) et PHB-3 (F14) sont le même test, recopié avec la même valeur ; la carte les gèle aussi, par prudence, et Lazar dit si sa décision les couvre (LISEZMOI, D6).
- **0,03 (retour arrière).** PHB-4 (F06).
- **Pour G5.** Le segment couvre l'opérateur et la valeur. Un bloc qui en change un caractère est refusé dans une correction de la boucle : ces points ne changent que sur décision de Lazar, hors de la boucle, et cela compte pour une ronde (§ 6 du protocole). Le reste des lignes de leur facteur suit les règles du facteur.

## 5. Recouvrements déclarés et séparation proposée

**Lignes partagées entre deux facteurs** (aucune n'appartient en entier à un facteur) :

| fichier | ligne | fonction | segments (entrée : colonnes, texte) | reste de la ligne |
|---|---|---|---|---|
| `principal.py` | 997 | `_synthetiser_mutation_politique_endogene` | F12.1 : col. 13–33, `phase == "conception"` ; F05.2 : col. 38–88, `forcer_mutation or (generation >= 1 and stagnation)` | à aucun facteur |
| `principal.py` | 2103 | `executer` | F03.1 : col. 32–58, `score_interne_moyen >= 0.78` ; F10.1 : col. 64–112, `len(nouvel_etat_isvd.get("exemplaires", [])) >= 2` | à aucun facteur |
| `principal.py` | 2104 | `executer` | F01.2 : col. 36–45, `r_idx >= 2` ; F03.2 : col. 51–77, `score_interne_moyen >= 0.65` | à aucun facteur |

**Lignes de F04 qui portent un segment interdit** (zone Z03 ; le texte n'est pas recopié, c'est un texte d'appel ou une clé du seuil) :

| segment | zone | fichier | ligne | fonction | colonnes | ligne de | empreinte du segment | désignation |
|---|---|---|---|---|---|---|---|---|
| Z03.s1 | Z03 | `principal.py` | 1009 | `_synthetiser_mutation_politique_endogene` | 41–80 | F04 | `3111a29c1c0ea117…` | plage de seuil_confiance_caste1 dans la consigne de l'architecte |
| Z03.s2 | Z03 | `principal.py` | 1011 | `_synthetiser_mutation_politique_endogene` | 92–121 | F04 | `42d9ae99c6ab30b8…` | valeur d'exemple de seuil_confiance_caste1 dans la consigne de l'architecte |
| Z03.s3 | Z03 | `principal.py` | 1039 | `_synthetiser_mutation_politique_endogene` | 51–74 | F04 | `e5c646fa0e50cf31…` | clé seuil_confiance_caste1 parmi les clés requises |

**Séparation proposée : par segments.** Sur une ligne partagée, un bloc n'est accepté que si tous les caractères qu'il change tombent dans les segments du facteur déclaré ; le reste de la ligne (mots-clés, parenthèses, noms des variables) n'est à aucun facteur. Sur une ligne de F04 à segment interdit, aucun caractère du segment ne change. Les colonnes et les empreintes des segments sont dans les JSON.

**Si G5 ne lit que des lignes,** une ligne partagée est refusée à tout bloc : F03, F10 et F12 n'ont alors plus aucune ligne atteignable, F01 garde les l. 2102 et 2106, F05 les l. 988–996 et 998, et les trois lignes de F04 à segment interdit sont refusées. Repli possible : fusionner F01, F03, F10 et F11 en un facteur « règle de déclaration de fin » (l. 2102–2106), et F05 avec F12 en un facteur « déclencheur de la mutation » (l. 988–998). Ce serait s'écarter de la liste de départ (moins de facteurs, plus gros) ; le choix est à conv-audit (LISEZMOI, D1).

## 6. Ce qui n'est rangé dans aucun facteur

Ces mécanismes sont vus dans le code et laissés hors facteurs en v1 : ni le § 6 ni le § 14 ne les nomment comme leviers, et plusieurs nourrissent les consignes des tâches ou la règle de classe. Leurs lignes libres sont dans le domaine de F09 (défaut nommé seulement) ; une carte v2 peut les ériger.

- **Induction** : interrupteur l. 1911 ; appel l. 1919–1926 ; plafond `MAX_TOKENS_INDUCTION` (l. 43, lu l. 1922). Consigne et arguments : zone Z07.
- **Moisson des tâches, hors formulation** : interrupteur l. 1880 ; nombre de recherches et de téléchargements (l. 784, 819, 832, 904–905) ; plafonds (l. 34–40) ; `_moisson_ouverte` (l. 200–204).
- **Corpus d'archive** : `_charger_corpus_archive` (l. 284–310), appelé l. 1846.
- **Sondes sur les traits** : interrupteur l. 1901–1908 ; `_entrainer_et_predire_sondes_traits` (l. 463–647), hors des zones Z04 et Z10.
- **Mémoire ISVD** : `mettre_a_jour_memoire_isvd` (`memoire_isvd.py` l. 92–263) hors F06 et Z05 (dimension et rang, l. 96–97 ; exemplaires retenus, l. 238 ; troncature des textes, l. 201) ; `extraire_vecteur_koopman` (l. 8–29) ; `decomposer_jacobi_symetrique` (l. 32–78) ; chargement (`principal.py` l. 1834–1844) et mise à jour (l. 2066–2082, hors l. 2077).
- **Journal d'ablations** : `memoire_isvd.py` l. 141–165.
- **Contrôle de la règle mutée** : `politique_endogene.py` l. 55–254, hors des zones Z03 et Z05.
- **Parallélisme** : `PARALLELISME_MAX` (l. 33) ; la bascule elle-même est en zone Z02 (statut E, délai).
- **Successeur** : `_propager_successeur` (l. 1547–1595), appelé l. 2177–2182.
- **Métrique proposée** : l. 2120–2133.
- **Version** : `VERSION` (l. 27), hors facteur et hors fichiers d'accompagnement (LISEZMOI, D7).

## 7. Règle de lecture pour G5, en bref

1. Lire `carte-facteurs-v1.json` et `zones-interdites-v1.json` ; vérifier les empreintes de l'objet (`objet.sha256_fichiers`).
2. Un bloc dans une zone interdite (ligne entière ou segment) est refusé ; sous l'exception déclarée, un bloc ne peut toucher que des lignes E.
3. Un bloc hors des lignes et des segments du facteur déclaré est refusé ; un périmètre qui couvre deux facteurs est refusé.
4. Un bloc qui touche un point hors boucle est refusé.
5. Lignes insérées : § 0, point 9.
6. Fichiers d'accompagnement (manifeste, l. 3 et 5 ; `CORRECTIONS-v<N>.md` nouveau ; `tests/test_corrections_v<N>.py` nouveau ; essai hérité adapté avec sa raison) : § 6 du protocole. Un essai hérité qui lit les constantes de mots-clés est en zone Z05.
