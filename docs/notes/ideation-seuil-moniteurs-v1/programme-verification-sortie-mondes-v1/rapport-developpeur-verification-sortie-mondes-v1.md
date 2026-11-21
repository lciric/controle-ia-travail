# Rapport du développeur — programme de vérification de la sortie de l'auteur des mondes plantés (course « seuil et moniteurs ») — v1

- Auteur : développeur du programme de vérification de la sortie des mondes, modèle O. Je n'ai écrit ni le mandat de l'auteur, ni sa contre-lecture, ni le programme de vérité des témoins. Écrit le 2026-11-21.
- Statut : instrument (classe B), **non contre-lu** : il attend le vérificateur S avant l'envoi. Aucun appel, aucune dépense, aucune clé lue ni nommée, aucune écriture dans un dépôt, aucun commit. Aucun refus de permission, de classifieur ni de garde.
- Mon mandat : `docs/notes/ideation-seuil-moniteurs-v1/mandat-developpeur-verification-sortie-auteur-mondes-v1.md` (`76c3c6c0209366868bb86e4865e2478daa77297fdff89c976bb8f5741f2f64df`, égal à son compagnon).

## 0. Verdict

1. Le programme `verifier_sortie_auteur_mondes_v1.py` (`8fbd70f7a0a7ffceba703530d0a230a920b44a1e39fc67e76b429556cf2d34c2`, bibliothèque standard seule) juge les points 1, 2, 3 et 5 du § 6 du mandat de l'auteur v3, dans cet ordre, et rend un JSON trié : un verdict par point (`tenu`, `manque`, `non_juge`), un verdict d'ensemble (`lisible` ou `illisible`), la liste des familles ou mondes **écartés** avec leurs raisons, et des observations qui ne décident de rien.
2. Il ne recalcule aucune valeur vraie (le point 4 reste au programme scellé de vérité) et n'en porte aucune : ni de la note, ni des témoins imposés (ni valeur, ni sorte, ni issue). De la table des témoins imposés, il ne porte que les définitions des règles recopiées du § 3.1.
3. Il ne nomme aucune famille tenue à l'écart : dans le rapport, elle s'appelle `a_l_ecart[i]`. Le rapport ne recopie aucun texte de la sortie : codes, chemins faits de clés connues (une clé libre s'écrit `*`), identifiants des témoins imposés, identifiants des familles visibles.
4. **Essais** : 195, tous passés sous Python 3.13.18 : 110 artefacts, 16 essais d'ensemble (cas sain, écarts, ordre des points, formes admises, non-recopie, commande du mandat, six erreurs d'usage, couverture), 69 mutations (une par garde, toutes tuées).
5. **Une contradiction de la lettre**, à trancher par la mère (remarque 20) : la borne de vingt-huit témoins ne peut pas tenir avec la complétude du point 2 ; il en faut au moins vingt-neuf en tête.

## 1. Pièces lues

| pièce | chemin | empreinte | lecture |
|---|---|---|---|
| mon mandat | `/home/user/controle-ia-travail-organisme/docs/notes/ideation-seuil-moniteurs-v1/mandat-developpeur-verification-sortie-auteur-mondes-v1.md` | `76c3c6c0…2f64df` (compagnon) | en entier |
| mandat de l'auteur v3 | `…/mandat-mondes-plantes-v3/mandat-auteur-mondes-plantes-seuil-et-moniteurs-v3.md` | `816313cb…05dbe9` (compagnon) | en entier |
| pièce de scellement du mandat v3 | `origin/main:prereg/ideation-seuil-moniteurs-v1/scellement-mandat-auteur-mondes-plantes-v3-v1.md` (après `fetch origin main`, `git show` redirigé) | `391c089e80c498e7d36ddc51c45b50e0447345ad360397a94c845f71cb5b347a` (compagnon sur `origin/main`) | en entier ; la ligne du mandat v3 y porte `816313cb…`, égale |
| rapport du rédacteur v3 (D-M16 à D-M18) | `…/mandat-mondes-plantes-v3/rapport-redacteur-mandat-mondes-plantes-v3.md` | `6a706f4c…576251` (compagnon) | en entier |
| rapport du rédacteur v2 (D-M11 à D-M18) | `…/mandat-mondes-plantes-v2/rapport-redacteur-mandat-mondes-plantes-v2.md` | `b4b1fdbb…7cb7698e` (compagnon) | en entier |

Mes copies de lecture (`lecture-scellement-mandat-v3.md` et son compagnon d'origine) sont dans mon dossier et sont **hors de la table d'empreintes** et hors versement.

## 2. Chaque règle du § 6, sa ligne de code, son essai

Lignes du programme à l'empreinte ci-dessus. « Code » : le code écrit dans le rapport JSON. Chaque code a au moins un artefact (`test_artefact[...]`) et une mutation (`test_mutation[CODE]`) qui neutralise toutes ses lignes et fait échouer ses artefacts.

### Point 1 — Forme (manqué : « illisible », code de sortie 2)

| règle du § 6, point 1 (et § 4) | code | lignes | artefacts |
|---|---|---|---|
| analyse JSON stricte | `P1_JSON_INVALIDE` | 403, 406 | `commentaire`, `virgule_finale` |
| — clé répétée dans un objet | `P1_CLE_DUPLIQUEE` | 393 (crochet 268) | `cle_dupliquee` |
| — NaN, Infinity, nombre hors des flottants | `P1_NOMBRE_NON_FINI` | 396 (250, 264) | `nan`, `infini` |
| — UTF-8 (§ 4.1) | `P1_UTF8` | 381 | `utf8` |
| un seul objet, sans texte avant ni après, sans bloc de code (§ 4.1) | `P1_TEXTE_AUTOUR_DE_L_OBJET` | 385, 401 | `texte_avant`, `bloc_de_code`, `texte_apres`, `marque_d_ordre` |
| — l'objet est un objet | `P1_PAS_UN_OBJET` | 409 | `pas_un_objet` |
| taille : 40 000 caractères au plus | `P1_TAILLE` | 388 (garde de lecture : 376) | `taille` |
| clés du premier niveau dans l'ordre, `temoins` avant `familles` | `P1_ORDRE_DES_CLES` | 706 | `ordre_des_cles` |
| aucune clé en trop, à aucun niveau, hors des objets à clés libres | `P1_CLE_EN_TROP` | 417, 702 | `cle_en_trop_temoin`, `cle_en_trop_famille_marquee`, `cle_en_trop_premier_niveau` |
| — clé exigée absente (§ 4.2, remarque 3) | `P1_CLE_MANQUANTE` | 420, 704 | `cle_manquante_temoin`, `cle_manquante_premier_niveau` |
| `version_forme` (§ 4.1) | `P1_VERSION_FORME` | 708 | `version_forme` |
| champs fermés valides | `P1_CHAMP_FERME_INVALIDE` | 425, 502, 508, 683 | `sorte_inconnue`, `apostrophe_typographique`, `structure_inconnue`, `marque_a_l_ecart_fausse` |
| — types (nombre JSON, texte, booléen, liste, entier) | `P1_TYPE_INVALIDE` | 430–488, 522, 538, 570–686, 711–814 | `n_en_texte`, `valeur_vraie_en_texte`, `k_non_entier` |
| — `signal` nul hors du monde M, dit sur le monde M | `P1_SIGNAL_INCOHERENT` | 585, 587 | `signal_nul_sur_m`, `signal_hors_m` |
| — `valeurs_de_plus` permise pour T05, T07, T09, T12 à T17 et les libres seulement | `P1_VALEURS_DE_PLUS_NON_PERMISES` | 599 | `valeurs_de_plus_t01` |
| — `valeurs_de_plus` : objet de nombres nommés | `P1_VALEURS_DE_PLUS_NON_NUMERIQUES` | 602 | `valeurs_de_plus_texte` |
| — `id` de famille : une lettre | `P1_IDENTIFIANT_DE_FAMILLE` | 629 | `identifiant_de_famille` |
| — `p_echec` : `null` hors de C et I | `P1_P_ECHEC_HORS_C_ET_I` | 639 | `p_echec_sur_a`, `p_echec_a_l_ecart` |
| — trois tranches | `P1_TRANCHES_PAS_TROIS` | 643 | `deux_tranches` |
| — trois décalages | `P1_DECALAGES_PAS_TROIS` | 671 | `deux_decalages` |
| — trois populations du monde M | `P1_POPULATIONS_PAS_TROIS` | 738 | `deux_populations` |
| — budget b parmi 1 %, 5 %, 10 %, 20 %, 30 % | `P1_BUDGET_HORS_LISTE` | 753 | `budget_hors_liste`, `budget_en_pourcent` |
| — un seul objet `{"temoins": …}` à part dans `a_l_ecart` | `P1_A_L_ECART_OBJET_TEMOINS_EN_DOUBLE` | 765 | `deux_objets_temoins` |
| lois dans la grammaire fermée (§ 4.2) | `P1_LOI_HORS_GRAMMAIRE` | 494, 506, 515, 531, 552 | `loi_inconnue`, `melange_boiteux`, `couple_a_trois_marges` |
| — loi `autre` avec sa `definition` | `P1_DEFINITION_MANQUANTE` | 527 | `autre_sans_definition` |
| règles dans la grammaire fermée (§ 4.3) | `P1_REGLE_HORS_GRAMMAIRE` | 559 | `regle_inconnue` |
| les sept suppositions à la lettre | `P1_SUPPOSITION_HORS_LISTE` | 459, 784 | `supposition_accentuee`, `supposition_de_table` |
| — sans doublon | `P1_SUPPOSITION_EN_DOUBLE` | 461 | `supposition_en_double` |

### Point 2 — Complétude (manqué : « illisible », code 2), et les écarts (jamais « illisible »)

| règle du § 6, point 2 | code | lignes | artefacts |
|---|---|---|---|
| les dix-sept témoins imposés (en tête, hors du bloc `a_l_ecart`) | `P2_TEMOIN_IMPOSE_ABSENT` | 868 | `t05_absent`, `t05_a_l_ecart` |
| — identifiants de témoins uniques (remarque 11) | `P2_IDENTIFIANT_DE_TEMOIN_EN_DOUBLE` | 863 | `temoin_en_double` |
| les familles A à I | `P2_FAMILLE_IMPOSEE_ABSENTE` | 879 | `famille_g_absente` |
| — une famille imposée ne va pas dans `a_l_ecart` | `P2_FAMILLE_IMPOSEE_A_L_ECART` | 881 | `famille_g_a_l_ecart` |
| — identifiants de familles uniques ; S et M réservés (remarque 11) | `P2_IDENTIFIANT_DE_FAMILLE_EN_DOUBLE`, `P2_IDENTIFIANT_DE_FAMILLE_RESERVE` | 873, 876 | `famille_en_double`, `famille_nommee_m` |
| P(échec) donné pour C et I | `P2_P_ECHEC_ABSENT` | 884 | `p_echec_de_c_nul` |
| les mondes S et M | (assurés par le point 1 : clés et objets exigés) | 696–757 | `cle_manquante_premier_niveau` |
| une famille tenue à l'écart ou deux | `P2_NOMBRE_DE_FAMILLES_A_L_ECART` | 886 | `aucune_famille_a_l_ecart`, `trois_familles_a_l_ecart` |
| un `de_marge` au moins | `P2_AUCUN_TEMOIN_DE_MARGE` | 888 | `aucun_de_marge` |
| — chaque témoin rattaché à un monde présent dans son bloc (remarque 11) | `P2_TEMOIN_RATTACHE_A_UN_MONDE_ABSENT` | 892, 895 | `temoin_sur_monde_z`, `temoin_a_l_ecart_sur_a` |
| **écart** : famille ou monde présent sans vérité exacte (§ 3.2 ; D-M18) | `E_VERITE_NON_EXACTE` | 903, 920 | `verite_approchee_e`, `verite_nulle_g`, `verite_approchee_s`, `verite_approchee_a_l_ecart` |
| **écart** : famille ou monde M sans témoin `doit_mourir` | `E_SANS_TEMOIN_DOIT_MOURIR` | 905, 915 | `b_sans_doit_mourir`, `m_sans_doit_mourir` |
| **écart** : famille ou monde M sans témoin `doit_tenir` | `E_SANS_TEMOIN_DOIT_TENIR` | 907, 917 | `d_sans_doit_tenir`, `a_l_ecart_sans_doit_tenir` |

Les essais d'écart vérifient que la sortie reste « lisible », code 0, point 2 tenu ; de plus `test_famille_sans_verite_exacte_ecartee_sans_rendre_illisible` et `test_famille_libre_sans_temoins_ecartee_sans_rendre_illisible`.

### Point 3 — Cohérence (manqué : sortie lisible, mais refusée en l'état, code 1)

| règle du § 6, point 3 | code | lignes | artefacts |
|---|---|---|---|
| la `table` redit les champs `suppositions_cassees` (familles, tenues à l'écart comprises, et variante du monde S ; `aucune` pour une famille saine) | `P3_TABLE_NE_REDIT_PAS` | 1027 | `table_sans_b`, `table_sans_s`, `table_a_en_trop` |
| — une ligne par couple | `P3_TABLE_LIGNE_EN_DOUBLE` | 1022 | `table_ligne_en_double` |
| — aucune ligne hors des familles et de la variante S | `P3_TABLE_MONDE_INCONNU` | 1019 | `table_monde_z`, `table_monde_m` |
| chaque famille cassée a son jumeau sain (objet non vide) | `P3_JUMEAU_SAIN_ABSENT` | 1031 | `jumeau_nul`, `jumeau_vide` |
| une famille `hors_table` ne casse aucune des sept | `P3_HORS_TABLE_CASSE_UNE_DES_SEPT` | 1033 | `hors_table_qui_casse` |
| le bloc `interface` ne porte ni loi… | `P3_INTERFACE_PORTE_UNE_LOI` | 1043 | `interface_loi_normale`, `interface_arrondis` |
| … ni paramètre… | `P3_INTERFACE_PORTE_UN_PARAMETRE` | 1045 | `interface_sigma` |
| … ni nom de famille (§ 4.2) | `P3_INTERFACE_NOMME_UNE_FAMILLE` | 1047 | `interface_famille_b`, `interface_nom_de_b` |
| rien hors du bloc `a_l_ecart` ne nomme une famille tenue à l'écart | `P3_FAMILLE_A_L_ECART_NOMMEE_HORS_DE_SON_BLOC` | 1072 (parcours 1060–1070) | `a_l_ecart_dans_remarque`, `nom_a_l_ecart_dans_remarque`, `temoin_a_l_ecart_en_tete`, `cle_libre_a_l_ecart` |

### Point 5 — Motifs (manqué : sortie refusée en l'état, code 1 ; code 2 si elle est aussi illisible)

| règle du § 6, point 5 | code | lignes | artefacts |
|---|---|---|---|
| aucun nom de modèle ou de fournisseur (liste lue du fichier de motifs) | `P5_NOM_DE_MODELE_OU_DE_FOURNISSEUR` | 1094 (chargement 1184) | `nom_de_modele`, `nom_de_modele_echappe` (échappement `\u`), `nom_de_fournisseur_en_cle` (dans une clé libre), `nom_de_modele_sortie_illisible` (texte brut) |
| aucune chaîne qui ressemble à une clé | `P5_CHAINE_DE_FORME_DE_CLE` | 1097, 1099 | `cle_a_prefixe`, `longue_chaine_melangee`, `bloc_de_cle_privee` |

### Ordre et verdict d'ensemble

- Lignes 1117–1124 : le point 1 d'abord ; s'il est manqué, les points 2 et 3 sont `non_juge` ; le point 5 est toujours jugé (sur les chaînes et les clés décodées, ou sur le texte brut si l'analyse échoue). Essais : `test_point_1_manque_laisse_2_et_3_non_juges`, `test_point_2_manque_laisse_3_juge`.
- Lignes 1138–1139 : « illisible » si le point 1 ou le point 2 est manqué (lettre du § 6).
- Codes de sortie : 0 lisible et tout tenu ; 1 lisible, point 3 ou 5 manqué ; 2 illisible ; 3 erreur d'usage ou de lecture, aucun rapport (sortie ou motifs absents, motifs vides ou invalides, arguments faux, rapport existant : on n'écrase jamais). Six essais `test_erreur_*`.

### Observations (ne décident de rien, ne changent pas le code de sortie)

Dix-sept codes `O_…`, lignes 469–964, chacun avec son artefact et sa mutation : quatre décimales (`O_PROBABILITE_A_MOINS_DE_QUATRE_DECIMALES`), poids d'un mélange, trente mots, une ligne pour `limite_monde_M`, dix remarques, écarts des témoins imposés à la définition de leur règle, `valeurs_de_plus` absentes, sorte et issue discordantes, `morte_sans_gain` hors T05 et T07 (D-M16), plus de vingt-huit témoins en tête, plus de deux familles libres, monde M sans témoin à portée conditionnelle, P(échec) différent entre C et I ou hors de [0,02 ; 0,10], drapeau `imposee` incohérent, jumeau sur famille saine, mention possible d'une famille dans `non_calcule`.

### Autres sorties du rapport

`hors_table` (familles à rapporter à part), `a_lire_par_une_personne_type_autre` (familles qui emploient une loi `autre`, § 4.2), `lignes_de_table_des_familles_a_l_ecart` (indices à détacher avec le bloc), `forme_du_bloc_a_l_ecart`, `comptes`, empreintes de la sortie, du programme et du fichier de motifs.

## 3. Ce que la lettre ne fixe pas (remarques)

1. **Blancs** autour de l'objet admis (espace, tabulation, saut de ligne) ; marque d'ordre des octets refusée comme texte avant l'objet.
2. **Taille** comptée en caractères du texte décodé, fichier entier. Garde de lecture à 1 000 000 octets.
3. Une **clé exigée absente** est une faute de forme, comme une clé en trop. L'ordre des clés n'est imposé qu'au premier niveau.
4. **Vérité non exacte** : un `verite.mode` autre que `exacte`, ou `verite` nulle, rend la famille (ou le monde S) **écartée**, non illisible. Je lis ainsi le § 6, point 2 et D-M18, qui priment sur « seule valeur admise » du § 4.2. Inversement, une `valeur_vraie` nulle est une faute de forme (lettre : « nombre »), qui rend la sortie illisible.
5. Une famille « sans vérité exacte » dite **seulement en prose dans `non_calcule`** ne peut pas être reconnue sûrement : observation `O_MENTION_POSSIBLE_DANS_NON_CALCULE`, à lire.
6. **`non_calcule`** : éléments texte, ou objets à clés libres (la forme n'est pas fixée).
7. **Bloc `a_l_ecart`** : deux lectures admises de « et, sous la clé `temoins`, leurs témoins » (dans chaque famille ; ou un objet `{"temoins": […]}` à part). « Marquées `tenue_a_l_ecart` » : clé `tenue_a_l_ecart: true` admise dans ce bloc seulement ; dans `familles`, c'est une clé en trop.
8. **Table et famille tenue à l'écart** : le § 4.2 exige ses lignes dans `table`, le § 6, point 3 interdit de la nommer hors du bloc. Ces lignes sont exemptées et rendues par indice, pour être détachées avec le bloc.
9. **Variante du monde S dans la table** : `monde` vaut `S`, ou `S` suivi d'un signe qui n'est pas une lettre (`S_derive`). Une ligne pour M, ou pour un monde inconnu, est refusée au point 3.
10. **Désignation d'une famille** (points 2 et 3) : égalité exacte d'une chaîne ou d'une clé avec l'identifiant ; « famille X », « familles X et Y », « monde X » ; ou le `nom` (quatre caractères au moins, sans casse ni accents). Une description sans nom n'est pas reconnue. « les K actions » n'est pas une désignation (essai : cas sain).
11. Identifiants : une lettre `[A-Za-z]` pour une famille ; `S` et `M` réservés ; identifiants uniques. Fautes de complétude, non de forme.
12. **Interface** : mots de loi de la grammaire et noms de paramètres. « échelle », « poids », « corrélation » peuvent donner un faux positif (point 3, pas « illisible »).
13. **Loi `autre`** : `definition` admise au niveau de la loi ou dans `parametres`. **Couple gaussien** : `rho` dans `parametres`, ou `dependance` objet `{"type": "gaussienne", "rho": …}`.
14. **Bornes numériques** non jugées (sigma positif, taux dans ]0, 1[) ; `k` entier au moins 1 jugé ; un entier écrit `300.0` est admis.
15. **Budget b** : fraction (0,01 … 0,30) ; `5` (pour cent) refusé.
16. **Quatre décimales** (§ 4.1, non listé au § 6, point 1 ; réserve 3 du rapport v2) : observation non bloquante, sur `valeur_vraie`, `risque_ou_niveau`, `p_echec`, les taux du monde S, `aire_gamma_propose`, `taux_parmi_ceux_qui_echouent`. Lu sur le texte brut de chaque nombre. Trente mots, dix remarques, une ligne : observations aussi.
17. **Témoins imposés** : le point 2 ne demande que leur présence. Leurs écarts à la définition de leur règle (monde, n, règle, garantie, risque, grandeur, population, portée, suppositions) sont des observations. Ni le n de T12 et T13, ni le risque des garanties « en moyenne » ne sont comparés.
18. **Points 3 et 5 manqués** : la sortie reste « lisible » à la lettre ; le code 1 la dit refusée en l'état. La mère décide d'un second essai.
19. Point 5 : motifs de clé génériques, intégrés au programme ; une empreinte hexadécimale en minuscules n'est pas signalée.
20. **Vingt-huit témoins : la lettre se contredit.** Aucun témoin imposé ne porte sur B, D, E, G ni sur le monde M ; un seul sur F (T09) et un seul sur I (T17). Le point 2 exige un `doit_mourir` et un `doit_tenir` pour chacun : au moins 2 × 4 + 2 + 1 + 1 = 12 témoins libres en tête, soit **29 au moins** avec les 17 imposés, au-delà des 28 du § 3.1. L'observation compte donc les seuls témoins en tête, et toute sortie complète la portera. Les témoins du bloc `a_l_ecart` ne sont pas comptés. **À trancher par la mère** ; le programme ne bloque pas.
21. **Deux familles libres** : la lettre ne dit pas si les familles tenues à l'écart en font partie. Observation si les familles libres visibles et celles du bloc `a_l_ecart` dépassent deux ensemble.
22. Le **`de_marge`** se compte sur tous les témoins, ceux du bloc `a_l_ecart` compris.

## 4. Commandes

Dossier : `D=/tmp/claude-0/-home-user-controle-ia-travail/16eb2a62-e29a-56e1-a702-f48557a5876c/scratchpad/dev-verification-sortie-mondes` (à remplacer par le chemin du versement).

**Avant l'envoi**, une commande par appel :

1. Essais : `/home/user/controle-ia-travail/.venv/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=$D/essais-tmp $D/test_verifier_sortie_auteur_mondes_v1.py`. Attendu : 195 essais passés.
2. Poser la liste réelle des noms refusés (de la mère, hors de mes pièces) et rejouer sur la sortie factice : `python3 -I -B $D/verifier_sortie_auteur_mondes_v1.py $D/sortie-factice-saine-v1.json RAPPORT_NEUF.json --motifs LISTE_REELLE`. Attendu : code 0, `lisible`, une seule observation (`O_PLUS_DE_VINGT_HUIT_TEMOINS`). Le rapport `RAPPORT_NEUF.json` ne doit pas exister.

**À la réception** : `python3 -I -B $D/verifier_sortie_auteur_mondes_v1.py SORTIE_RECUE.json RAPPORT_RECEPTION.json --motifs LISTE_REELLE`. Code 0 : lisible, tout tenu ; 1 : lisible, refusée en l'état (point 3 ou 5), à lire ; 2 : illisible, c'est ce code qui ouvre un second essai payé ; 3 : rien n'est jugé, aucun rapport. Lire ensuite `ecartes`, `hors_table`, `a_lire_par_une_personne_type_autre`, `lignes_de_table_des_familles_a_l_ecart` et `observations`.

Sans `--motifs`, le programme lit `motifs-noms-refuses-essai-v1.txt` posé à côté de lui : trois noms **fictifs**, pour les seuls essais.

## 5. Réserves

1. Programme et essais non contre-lus : le vérificateur S les lira avant l'envoi.
2. La détection d'un nom ou d'une loi dans du texte libre (points 3 et 5) est par motifs : elle peut manquer une désignation détournée ou se tromper sur un mot courant (remarques 10, 12, 19).
3. La sortie factice est faite de remplissages de forme : toutes les valeurs vraies valent 0,4321, tous les témoins imposés sont `de_marge`. Elle n'éprouve rien du point 4.
4. Les mutations retirent chaque garde en entier ; une garde affaiblie sans être retirée n'est pas éprouvée.

développeur du programme de vérification de la sortie des mondes, modèle O
