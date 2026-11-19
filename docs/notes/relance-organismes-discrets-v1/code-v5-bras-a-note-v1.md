# Code de l'instrument et de l'analyse du bras A des organismes discrets, version 5 — note du rédacteur — v1

**En bref.** La version 5 corrige le défaut bloquant B-1 et les dix défauts C-1 à C-10 de la contre-lecture du code de la version 4, traite dix des onze défauts mineurs (M-9 est documenté, non branché : voir sa ligne), porte les précisions des brouillons 19 et 20 et lit la livraison du côté habilité sous les noms de la version 8. Les cas que la note du brouillon 20 dit « en attente d'un arbitrage » ne sont pas codés comme des choix : six gardes nommées arrêtent, avec un message qui dit que le cas attend une décision. **Tant que les valeurs que le module habilité écrit pour déclarer son schéma de permutation ne sont pas transmises, la règle de discrétion s'arrête sur l'une de ces gardes** : c'est voulu. 256 essais passent.

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`), agent délégué par la session de relance. À contre-lire par un autre modèle (R-3735).
- **Texte suivi** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon20.md` (`b076e3f9…`), lu par recherches ciblées (liste en fin de note). Je n'ai lu aucun fichier « brouillon21 ».
- **Seule source sur le module habilité** : `reponses-du-developpeur-habilite-noms-comptes-rang-v1.md` (`54c8afb3…`). Le module n'est ni ouvert ni importé.
- **Heure** : 2026-11-19T15:45Z (`date -u`). Rien n'est committé ; aucun fichier existant n'est modifié.

## 1. Fichiers

Sous `src/controle_ia/organismes_discrets/` :

| module | ce qu'il est |
|---|---|
| `analyse_bras_a_v5.py` | neuf, entier ; n'importe pas la version 4 |
| `verdicts_bras_a_v5.py` | neuf, entier |
| `graines_bras_a_v5.py` | reprend tous les noms de `graines_bras_a_v4.py` (importé tel quel) ; ajoute le tirage à clé, remplace la porte de l'écart à R9 |
| `permutation_etiquettes_bras_a_v5.py` | neuf, entier |
| `reponses_lecteurs_v5.py` | copie de la version 4, une ligne de code changée (fermeture du bloc) |
| `mesures_bras_a_v5.py` | copie de la version 4, deux imports changés (types partagés avec les modules de la version 5) |
| `attentes_bras_a_v5.py` | neuf : arrêts nommés, dont les six cas en attente |
| `cloisonnement_bras_a_v5.py` | neuf : garde statique du cloisonnement |

**Restent et sont importés tels quels, sans version 5** : `instrument_appariement_v4.py`, `epreuves_couverture_bras_a_v3.py`, `fabrication_v3.py`, `graines_bras_a_v4.py` (la table des clés). Aucun défaut ne les touche. Leurs essais sont ceux de leur version.

Essais : `tests/test_{graines_bras_a,mesures_bras_a,analyse_bras_a,verdicts_bras_a,reponses_lecteurs,permutation_etiquettes_bras_a,cloisonnement_bras_a}_v5.py`. Les essais de la version 4 sont repris (aucun n'est perdu), et les essais neufs s'y ajoutent.

## 2. Essais

Commande exacte, lancée seule (jamais la suite entière) :

```
PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_{graines_bras_a,mesures_bras_a,analyse_bras_a,verdicts_bras_a,reponses_lecteurs,permutation_etiquettes_bras_a,cloisonnement_bras_a}_v5.py tests/test_epreuves_couverture_bras_a_v3.py
```

Résultat : **256 passés** (graines 102 ; mesures 8 ; analyse 45 ; verdicts 24 ; réponses 36 ; permutation 9 ; cloisonnement 28 ; épreuves de couverture, version 3 : 4). Toutes les données sont fabriquées dans l'essai. `tests/test_instrument_appariement_v4.py` n'a pas été relancé : son module ne change pas.

## 3. Défaut bloquant et défauts à corriger

`an` = `analyse_bras_a_v5`, `v` = `verdicts_bras_a_v5`, `g` = `graines_bras_a_v5`, `pe` = `permutation_etiquettes_bras_a_v5`.

| défaut | ce qui est fait | où | essai |
|---|---|---|---|
| **B-1** valeur p haute absente comptée pour 1 | Le code ne met plus jamais 1 de lui-même. Aire rendue, plancher sain et `valeur_p_haut` nulle : arrêt nommé « valeur p haute absente alors qu'elle est calculable », quelle que soit la valeur de la famille. Valeur de la famille absente, égale à 1 sans cause, ou autre que la valeur p haute : arrêt nommé | `an.cas_de_la_regle` | `test_b1_valeur_p_haute_absente_alors_que_l_aire_est_calculable_refusee` (scénario de la contre-lecture, avec et sans tirage dégénéré) ; `test_famille_de_holm_complete_et_valeur_1_seulement_avec_sa_cause` |
| **C-1** dénominateur du 1 %, rééchantillonnage tronqué | `tirages` compte les calculés ; `tirages + tirages_degeneres` doit valoir 2 000, sinon arrêt nommé. Seuil sur les demandés (20 passe, 21 non) | `an.exiger_coherence_des_comptes`, `an.intervalle_au_dela_de_un_pour_cent` | `test_c1_total_des_tirages_et_bord_du_un_pour_cent` |
| **C-2** garde de sortie qui se fie à un drapeau | La garde relit les dix-huit nombres, rejoue la règle et Holm, compare. Aucun drapeau n'est lu ; un champ de plus dans les détails est refusé | `an.exiger_resultat_de_discretion` | `test_c2_la_garde_de_sortie_ne_se_fie_a_aucun_drapeau` (onze retouches, dont celle de la contre-lecture) |
| **C-3** borne haute de C4 sous intervalle dégénéré | La borne à rapporter est « non calculable » dès que le cas est « intervalle dégénéré seul », même si un nombre est rendu ; les deux comptes de tirages sont rapportés | `an._details_d_un_moniteur` (`borne_haute_rapportee`), `v.rapport_c4` | `test_c3_borne_haute_non_calculable_sous_intervalle_degenere_meme_si_elle_est_rendue` |
| **C-4** borne ou valeur p basse absente | Refus nommé, plus de « indécis » sans motif | `an.cas_de_la_regle`, `an.exiger_coherence_des_comptes` | `test_c4_borne_haute_ou_valeur_p_basse_absente_sans_cause_refusee` |
| **C-5** fichier de l'étape (m) sous A15 ou A16 | L'analyse ne l'écrit plus. `v.ecrire_fichier_de_l_etape_m` exige une issue de la table A sans aucune ligne, le renvoi de la base « vérifié » et les effectifs conformes ; nom fixé, `etats-des-moniteurs-et-table-c-bras-a.json` | `v.ecrire_fichier_de_l_etape_m`, `an.exiger_fichier_de_l_etape_m` | `test_fichier_de_l_etape_m_ecrit_scelle_nomme_et_exige` |
| **C-6** garde statique contournable | Garde dans le code, par l'arbre syntaxique : fragments du nom du fichier (morceaux recollés compris), noms réservés, `import *` et accès indirects dans un programme qui importe l'analyse ; fichiers de commandes. Limites écrites en tête du module | `cloisonnement_bras_a_v5.exiger_cloisonnement_statique` | `tests/test_cloisonnement_bras_a_v5.py` : 24 modules plantés dans un dossier temporaire, dont les quatre contournements de la contre-lecture ; le code de la relance passe |
| **C-7** tirage sans clé | Les tirages de l'analyse reçoivent un tirage qui porte sa clé ; la clé est confrontée à l'usage au moment du tirage ; un générateur nu est refusé. L'aire conditionnelle exige la clé de son moniteur et de sa dose | `g.TirageAClef`, `g.tirage_de`, `g.generateur_pour` ; `an.intervalle_rapporte`, `an.percentiles_taches`, `an.page`, `an.tirages_des_taches`, `an.aire_conditionnelle` ; `pe.permutations_des_etiquettes` | `test_tirage_a_cle_et_garde_au_point_du_tirage` ; `test_tirages_de_l_analyse_refusent_un_generateur_sans_cle` ; `test_aire_conditionnelle_non_calculable_sans_arret_et_ses_gardes` |
| **C-8** schéma de permutation hors de la chaîne | Argument obligatoire, nommé, sans défaut, de `an.regle_de_discretion` ; confronté à `reglages.permutation` et `reglages.unite_de_la_permutation` de la livraison. Je ne tranche pas lequel | `pe.exiger_schema_de_la_livraison`, `an.exiger_reglages` | `test_attente_controle_des_reglages_et_schema_de_permutation_c8` ; `test_c8_schema_confronte_a_ce_que_la_livraison_declare` |
| **C-9** empreinte donnée par l'appelant | Le fichier des rangs doit répondre à son compagnon `.sha256` ; l'empreinte attendue est lue dans la pièce scellée du côté habilité (`scores_par_unite.sha256` de la sortie de la lecture commune), elle-même vérifiée par son compagnon | `an.lire_fichier_des_rangs`, `an.lire_la_sortie_scellee_de_la_lecture_commune` | `test_fichier_des_rangs_lu_sous_ses_gardes` |
| **C-10** dixième champ non contrôlé | Par moniteur, dose et pli, les valeurs de `rang` doivent être exactement un jeu de rangs moyens de 1 à n ; rien n'est converti | `an.exiger_rangs_dans_le_pli` | `test_c10_le_dixieme_champ_est_un_rang_moyen_dans_le_pli` (scores, rangs par pli et par condition, rangs sans égard au pli, décalés, mal partagés) |

## 4. Défauts mineurs

| défaut | ce qui est fait | où | essai |
|---|---|---|---|
| M-1 schéma libre dépendant de l'ordre reçu | places triées par (rang, étiquette) | `pe.permutations_des_etiquettes` | `test_m1_le_schema_libre_ne_depend_pas_de_l_ordre_des_episodes_recus` |
| M-2 porte de l'écart à R9 | la ligne de GO est lue dans le registre donné ; elle doit exister une fois et parler de R9 et des identifiants ; limite de la garde « table tirée de l'entropie du bras » écrite en tête du module et montrée par l'essai | `g.admettre_l_entropie_propre_de_la_table_des_identifiants`, `g.ligne_de_go` | `test_entropie_propre_de_la_table_des_identifiants_refusee_par_defaut` |
| M-3 dose ¼ absente | arrêt nommé | `an.lire_la_sortie_de_la_lecture_commune` | `test_doses_et_formes_hors_des_gardes_m3_m6` |
| M-4 valeurs p et comptes | les deux valeurs p sont confrontées aux formules du texte, à 1e-9 près | `an.exiger_coherence_des_comptes` | `test_m4_valeurs_p_confrontees_a_leurs_comptes_et_autres_coherences` |
| M-5 nombre gardé à côté de « non calculable » | le mot remplace le nombre | `an._rapport_de_la_dose_quart` | `test_attente_grandeurs_rapportees_a_la_dose_un_quart` |
| M-6 dose écrite en texte | toute forme inconnue arrête par une garde | `an._dose_de` | `test_doses_et_formes_hors_des_gardes_m3_m6` |
| M-7 journal de l'étape (g) | le constat porte le nom de l'épreuve jugée ; deux constats sur la même épreuve sont refusés ; `journal_avec_audit` refuse le moment de l'étape (g) | `v.constat_de_l_etape_g`, `v.journal_avec_l_etape_g` | `test_m7_le_constat_de_l_etape_g_nomme_l_epreuve_qu_il_juge` |
| M-8 origine des états de la table C | `ligne_table_c` et `rapport_c4` prennent le résultat de la règle et la dose | `v.ligne_table_c`, `v.rapport_c4` | `test_m8_la_table_c_ne_lit_pas_un_dictionnaire_d_etats_fait_a_la_main` |
| **M-9** `exiger_paires_gardees` sans appelant | **non branchée, à dessein** : le rééchantillonnage de l'aire conditionnelle tire des poids par tâche, et la garde sur ces poids serait vraie par construction. Dit en tête du module ; l'essai relie le tirage à la garde | `pe.exiger_paires_gardees` | `test_reechantillonnage_par_tache_garde_les_paires` |
| M-10 fermeture du bloc de code | blancs de bord tolérés (brouillon 20, 3.2) | `reponses_lecteurs_v5.retirer_le_bloc_de_code` | `test_m10_ligne_de_fermeture_du_bloc_de_code_blancs_de_bord_toleres` |
| M-11 troisième état du contrôle de l'adaptateur | le texte le nomme maintenant « pas au-dessus » ; le code garde ce nom ; l'essai le confronte au brouillon 20 | `v.ADAPTATEUR_PAS_AU_DESSUS` | `test_reserves_r_ba2_et_r_ba2b_telles_qu_ecrites` |

## 5. Précisions des brouillons 19 et 20, et forme de la version 8

- **Listes fermées** : dix-huit noms par moniteur et par dose, onze en sortie, neuf dans `reglages`, cinq dans `scores_par_unite` (`an.LISTES_FERMEES`).
- **`null`** veut dire « pas connu », jamais zéro. Des comptes à zéro là où ils devraient être nuls sont refusés.
- **Seuil du 1 %** : une **constante unique**, `an.DENOMINATEUR_DU_UN_POUR_CENT`, lue par une seule fonction. Elle vaut l'option (a) : strictement plus de 0,01 × les demandés, soit 21 sur 2 000. Passer à l'option (b) se fait en changeant cette seule valeur dans une version nouvelle du fichier ; l'essai montre les deux. La garde de sortie refuse un résultat calculé sous l'autre option.
- **Dose ¼** : chaque grandeur n'est dite « non calculable » que par ce qui la touche. Sous intervalle dégénéré, seule la borne haute l'est.
- **Fichier des rangs** : `rangs-par-unite-moniteurs-bras-a.jsonl`, dix champs dans l'ordre, le dixième `rang`.
- **Cloisonnement** : aucun module de la relance, hors `analyse_bras_a_v5.py`, ne nomme le fichier ni ne touche l'objet qui porte les rangs. La sortie de l'aire conditionnelle passe par `an.exiger_sortie_de_l_aire_conditionnelle` : aires, intervalle et comptes seulement.

## 6. Gardes « attend une décision »

Classe `attentes_bras_a_v5.EnAttenteDeDecision`. Aucune ne se lève par un réglage. Chacune a un essai sur un cas sain et sur un artefact.

| nom de la garde | quand elle arrête | point de la note du brouillon 20 | cas sain qui passe |
|---|---|---|---|
| tirages nuls sous permutations perdues | plus de 1 % de permutations perdues, couple de tirages `null` | 1, 2 | même cas avec les quatre comptes rendus : « indécis », 1 dans la famille |
| tirages nuls sous intervalle impossible | plancher rendu et sain, couple de tirages `null` | 1, 6 | moniteur aux quatre comptes rendus |
| valeur p pour la famille égale à 1 sous tirages dégénérés | plus de 1 % de tirages dégénérés, valeurs p `null`, 1 dans la famille (forme de la version 8, contraire à GO-2026-11-19-70) | 3, 5 | valeur p haute rendue et gardée dans la famille : « repère » ou « indécis » |
| grandeurs rapportées à la dose un quart | à la dose ¼, le module rend `null` une grandeur que le texte veut rapportée | 4 | les trois formes du texte, et la cause antérieure |
| liste fermée des noms rendus | un champ de plus ou de moins dans l'une quelconque des quatre listes | 8 | les quatre listes à la lettre |
| contrôle des réglages | un des quatre réglages chiffrés diffère du texte ; ou les valeurs qui déclarent le schéma de permutation ne sont pas connues | 10 | réglages du texte, déclarations données |

Dans chaque cas, la garde n'arrête que là où les lectures possibles divergent. Là où elles donnent le même résultat, le code continue.

## 7. Ce qui reste à écrire (hors de mon mandat)

- Les lots, le client des lecteurs, le lanceur, l'enchaînement de l'analyse.
- Dans cet enchaînement : appeler `exiger_cloisonnement_statique` sur `src/` et `scripts/` entiers. Mes essais ne la passent que sur des modules plantés et sur les programmes du paquet des organismes discrets.
- Donner à `regle_de_discretion` les déclarations du schéma, lues dans la configuration scellée, dès qu'elles sont transmises.
- Une version nouvelle après chaque arbitrage qui lève une garde de la partie 6.

## 8. Réserves

1. **Formes devinées.** Plusieurs formes de la version 8 ne sont pas transmises (voir le relevé des défauts, partie A). Là où j'ai dû en supposer une, un écart **arrête** ; il ne passe pas en silence. Le risque est un arrêt à tort à la première livraison réelle, non un verdict faux.
2. **Trois refus fermes que le texte ne commande pas mot pour mot** : valeurs p qui ne répondent pas à leurs comptes à 1e-9 près ; quantile de la borne haute autre que 1 − 0,05 ÷ 15 ; dose ¼ absente. Si le module arrondit ses nombres, les deux premiers arrêteront.
3. **Cas « intervalle dégénéré seul »** : je l'admets que `calculable` soit dit vrai ou faux, et que la borne soit rendue ou nulle, car la forme corrigée du module n'est pas connue. Le jugement, lui, ne dépend que des comptes et de la valeur p.
4. **La garde statique n'est pas une preuve.** Elle voit le code qu'on lui donne. La première barrière reste la règle « aucun agent n'ouvre le fichier ».
5. **Le tirage à clé arrête l'oubli, non la fraude** : Python ne cache rien.
6. Les essais de la statistique de la variable principale sont ceux de la version 4, repris : je ne les ai pas réécrits contre une seconde écriture neuve.

## 9. Fichiers ouverts

- Consignes : `CLAUDE.md`.
- Passation : `registres/passations/passation-relance-bras-a-2026-11-19-1500.md`, en entier.
- Notes, en entier : `contre-lecture-code-v4-bras-a-v1.md`, `preenregistrement-v2-brouillon20-note-v1.md`, `preenregistrement-v2-brouillon19-note-v1.md`, `reponses-du-developpeur-habilite-noms-comptes-rang-v1.md`, `defauts-du-texte-trouves-en-codant-v4.md`.
- Code de la version 4 : `analyse_bras_a_v4.py`, `graines_bras_a_v4.py`, `permutation_etiquettes_bras_a_v4.py` en entier ; `verdicts_bras_a_v4.py` (en-tête, table A, étape (g), table C, issues) ; `reponses_lecteurs_v4.py` (lignes 1 à 110) ; `mesures_bras_a_v4.py` (en-tête et imports) ; `instrument_appariement_v4.py` (imports, lignes 100 à 107) ; `epreuves_couverture_bras_a_v3.py` (imports). Aussi `src/controle_ia/gardes.py` (début) et `src/controle_ia/scellement.py` (signatures).
- Essais de la version 4 : `test_analyse_bras_a_v4.py` (lignes 1 à 34, 244 à 335, 600 à 997), `test_permutation_etiquettes_bras_a_v4.py` en entier, `test_verdicts_bras_a_v4.py` (lignes 1 à 30, 93 à 126, 232 à 262, 420 à 572), `test_graines_bras_a_v4.py` (dernier essai), `test_reponses_lecteurs_v4.py` (essai de la ligne d'ouverture). Les essais de mesures et le reste ont été repris par programme sans être relus.
- Brouillon 20, par recherches : conventions (lignes 143 à 146), 3.2 (phrase de la fermeture), 3.5 (b), 6.3 (g) (phrase de l'épreuve nommée), 6.9 (lignes 679 à 684, en entier), 7.4, 7.7 (troisième état), 8.4 (lignes des gardes de la discrétion, des rangs, du schéma et des graines), 12 (énoncés des options), 13.1 (cases « schéma de permutation » et « module »), 13.2 (ligne du lanceur de l'étape de discrétion).
- Registre des accords de `origin/main` : la seule ligne GO-2026-11-19-70.
- Liste des noms de fichiers du dossier `src/controle_ia/organismes_discrets/`.
- **Non ouverts** : aucun interne de moniteur, aucun module habilité, aucune notice ni contre-lecture du côté habilité, aucune fiche de l'organisme d'idéation, aucune réponse de lecteur, aucune clé. Aucun appel réseau, aucun appel de modèle, aucun sous-agent.
