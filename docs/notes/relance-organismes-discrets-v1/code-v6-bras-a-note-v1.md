# Code de l'instrument et de l'analyse du bras A des organismes discrets, version 6 — note du rédacteur — v1

**En bref.** La version 6 porte les quatre défauts à corriger et les neuf mineurs de la contre-lecture du code de la version 5, et la règle de discrétion est récrite sur la table des formes du brouillon 24. Aucun défaut n'est écarté ; deux sont traités autrement que la correction proposée (C-4, lecture d'un dossier ; M-3, fichier de l'étape (m)), et je dis pourquoi. Tout ce qui attend Lazar est un **choix nommé, obligatoire, sans valeur par défaut**, lu dans un fichier scellé : cinq choix, aucune valeur retenue par le code. 277 essais passent.

- **Rédacteur** : Claude Fable 5.2 (`claude-fable-5-2`). À contre-lire par un autre modèle (R-3735).
- **Texte suivi** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon24.md` (`12609c04…`), par recherches ciblées. Le mandat est passé du brouillon 22 au 23 puis au 24 pendant l'écriture ; le code suit le 24.
- **Seule source sur le module habilité** : les réponses du développeur habilité (`54c8afb3…`). Le module n'est ni ouvert ni importé.
- **Heure** : 2026-11-19T16:40Z (`date -u`). Rien n'est committé ; aucun fichier existant n'est modifié.

## 1. Fichiers

Sous `src/controle_ia/organismes_discrets/` :

| module | ce qu'il est |
|---|---|
| `analyse_bras_a_v6.py` | statistique de la version 5, inchangée ; règle de discrétion récrite |
| `verdicts_bras_a_v6.py` | tables de la version 5 ; issue d'un arrêt ; fichier de l'étape (m) et ses constats |
| `arrets_bras_a_v6.py` | neuf : l'événement « arrêt de la lecture de la discrétion » et ses listes fermées |
| `configuration_bras_a_v6.py` | neuf : la configuration scellée, cinq choix nommés et chaînes du module |
| `graines_bras_a_v6.py` | reprend la table des clés de la version 4 ; tirage à clé, lignes d'accord |
| `permutation_etiquettes_bras_a_v6.py` | schéma confronté à la configuration scellée |
| `cloisonnement_bras_a_v6.py` | garde statique |
| `mesures_bras_a_v6.py` | copie de la version 5, un import changé |

**Restent et sont importés tels quels** : `reponses_lecteurs_v5.py`, `instrument_appariement_v4.py`, `epreuves_couverture_bras_a_v3.py`, `fabrication_v3.py`, `graines_bras_a_v4.py` (table des clés). Aucun module de la version 6 n'importe l'analyse, les graines ni les verdicts de la version 5.

Essais : `tests/test_{graines_bras_a,mesures_bras_a,analyse_bras_a,verdicts_bras_a,permutation_etiquettes_bras_a,cloisonnement_bras_a}_v6.py`, et leur aide `tests/aide_bras_a_v6.py`.

## 2. Essais

Commande exacte, lancée seule :

```
PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_{graines_bras_a,mesures_bras_a,analyse_bras_a,verdicts_bras_a,permutation_etiquettes_bras_a,cloisonnement_bras_a}_v6.py tests/test_reponses_lecteurs_v5.py tests/test_epreuves_couverture_bras_a_v3.py
```

Résultat : **277 passés**. Fichiers de la version 6 : 237 (graines 103 ; mesures 9 ; analyse 46 ; verdicts 26 ; permutation 9 ; garde statique 44). Réponses des lecteurs, version 5, module resté : 36. Épreuves de couverture, version 3 : 4.

L'essai `test_la_garde_passee_sur_src_et_scripts_du_depot` exige que les quatre programmes autorisés répondent à leur empreinte compagnon : il ne passe qu'une fois les fichiers scellés.

## 3. Les cinq choix nommés

Fichier scellé lu par `configuration_bras_a_v6.lire_la_configuration_scellee`. Un choix absent, vide ou approchant est refusé ; sans ce fichier, la règle de discrétion ne se lit pas.

| choix | valeurs | où il joue | essai |
|---|---|---|---|
| schéma de permutation (point 17) | libre par épisode ; échange dans chaque paire | `permutation.exiger_schema_de_la_livraison` | `test_reglages_rendus_un_essai_par_artefact` |
| seuil de 1 % (fiche 9) | sur les tirages demandés ; sur les tirages calculés | `analyse.intervalle_au_dela_de_un_pour_cent`, seul endroit | `test_seuil_du_un_pour_cent_choix_nomme_un_essai_par_option` |
| intervalle impossible (fiche 10) | comme un intervalle dégénéré ; indécis d'office ; anomalie | `analyse.juger_une_lecture` | `test_intervalle_impossible_choix_nomme_un_essai_par_redaction` |
| moniteur appris non ajustable (fiche 11) | aire non calculable ; anomalie ; module corrigé | `analyse.juger_une_lecture` | `test_moniteur_appris_non_ajustable_choix_nomme_un_essai_par_redaction` |
| issue d'un arrêt (fiche 12) | ligne d'arrêt de la course ; discrétion non lue ; non lue en distinguant les étapes | `verdicts.issues`, `verdicts.table_a_apres_un_arret` | `test_issue_d_un_arret_un_essai_par_valeur_du_choix` |

Le seuil de 1 % a un défaut écrit dans la fiche 9 ; le code n'en a pas : la configuration doit le nommer. **Aucun arrêt « attend une décision » ne reste** : les six de la version 5 sont devenus des refus écrits au texte, des choix nommés, ou des grandeurs « non rendues ».

## 4. Contre-lecture du code de la version 5

`an` = `analyse_bras_a_v6`, `v` = `verdicts_bras_a_v6`, `g` = `graines_bras_a_v6`, `cl` = `cloisonnement_bras_a_v6`.

| défaut | ce qui est fait | où | essai |
|---|---|---|---|
| **C-1** règle non liée à la pièce scellée | La règle prend le chemin de la pièce scellée et celui de la configuration scellée ; le résultat porte les deux empreintes ; la garde de sortie relit les deux fichiers, rejoue la règle et exige l'égalité du résultat entier. La retouche cohérente de l'essai d'attaque est refusée | `an.regle_de_discretion`, `an.exiger_resultat_de_discretion` | `test_la_regle_se_lit_sur_deux_fichiers_scelles_et_sa_garde_de_sortie_les_relit` |
| **C-2** déclarations du schéma données par l'appelant | Plus d'argument, plus de table, plus de défaut : les déclarations sont lues dans la configuration scellée | `configuration_bras_a_v6`, `permutation.exiger_schema_de_la_livraison` | `test_schema_confronte_a_ce_que_la_livraison_declare_d_apres_la_configuration_scellee` |
| **C-3** trois réglages non lus | Statistique de l'agrégateur, doses de la famille, dose pour information : contrôlés contre la configuration ; un artefact chacun | `an._exiger_reglages` | `test_reglages_rendus_un_essai_par_artefact` |
| **C-4** garde statique | Autorisation par chemin exact et par empreinte compagnon ; exclusion par préfixe de chemin exact ; noms recollés par `join`, `%`, `format`, chaîne retournée ; fichiers `.mk`, `.zsh`, `.ipynb`, `Makefile` et réglages. **Lecture d'un dossier : signalée, non refusée** (voir plus bas) | `cl.violations_de_la_garde_statique`, `cl.listages_a_relire` | `tests/test_cloisonnement_bras_a_v6.py` |
| **M-1** jeton, tirage réemployé | Seules les deux fabriques inscrivent un tirage au registre ; un tirage fait avec le jeton ou par `object.__new__` est refusé ; un tirage ne sert qu'une fois ; la garde statique refuse le jeton et le constructeur hors du module des graines | `g.generateur_pour`, `cl` | `test_m1_un_tirage_ne_se_fabrique_que_par_ses_fabriques_et_ne_sert_qu_une_fois` |
| **M-2** porte de l'écart à R9 | Registre du dépôt, non donné par l'appelant ; phrase d'accord à la lettre ; un mot de refus ferme la porte | `g.ligne_d_accord` | `test_entropie_propre_de_la_table_des_identifiants_refusee_par_defaut` |
| **M-3** étape (m) tenue à l'écriture seulement | L'écriture prend le journal de la table A et le lit elle-même ; un second fichier scellé porte les constats ; la lecture l'exige. Un fichier de l'étape (m) écrit à la main est refusé | `v.ecrire_fichier_de_l_etape_m`, `an.exiger_fichier_de_l_etape_m` | `test_fichier_de_l_etape_m_ecrit_avec_ses_constats_et_exige_a_la_lecture` |
| **M-4** pièce scellée, formes non reconnues | `lignes` et `champs` d'une forme non reconnue arrêtent ; la pièce donnée à l'étape (n) doit être celle des constats de l'étape (m) | `an.lire_fichier_des_rangs` | `test_fichier_des_rangs_lu_sous_ses_gardes` |
| **M-5** dose ¼ et `calculable` | Une seule table des formes pour les quatre doses | `an.ranger_une_lecture` | `test_ecarts_de_structure_arretent_a_toute_dose_et_sont_ranges_a_l_etape_m` |
| **M-6** issue d'une livraison refusée | Événement nommé ; issue par le choix nommé, trois valeurs, aucune retenue | `arrets_bras_a_v6`, `v.issues` | `test_issue_d_un_arret_un_essai_par_valeur_du_choix`, `test_issue_d_un_arret_artefacts` |
| **M-7** essais manquants | Retouche cohérente ; `glob`, `join`, autorisation, exclusions ; garde passée sur `src/` et `scripts/` ; secondes écritures neuves de la statistique | — | `test_statistique_de_la_variable_principale_contre_des_secondes_ecritures_neuves`, et les précédents |
| **M-8** mélange de versions | `mesures_bras_a_v6` ; la garde statique refuse la porte de l'écart à R9 d'une version antérieure des graines ; `LONGUEUR_MIN` égale dans les deux versions | `cl` | `test_m8_la_chaine_de_la_version_6_n_importe_pas_l_analyse_de_la_version_5` |
| **M-9** comptes à virgule | Un compte entier écrit `2000.0` se lit comme l'entier ; `1999.5` arrête | `an._compte_lu` | même essai que M-5 |

**Deux écarts à la correction proposée.**
- **C-4, lecture d'un dossier.** La contre-lecture proposait de signaler `glob`, `iterdir` et leurs voisins, « ou bien d'écrire cette limite en clair ». Refuser ces appels arrêterait à tort : sur le dépôt, huit programmes sans rapport lisent à bon droit un dossier de fichiers de lignes JSON. J'ai donc fait les deux moitiés sans la garde : `listages_a_relire` les liste sans arrêter, et la limite (e) de l'en-tête dit que le fichier des rangs doit être rangé dans un dossier qu'aucun lanceur ne parcourt.
- **M-3, fichier de l'étape (m).** La contre-lecture proposait d'y écrire l'issue de la table A, le renvoi de la base et l'empreinte de la pièce. Les conventions du texte disent « trois champs et eux seuls ». J'ai gardé les trois champs et mis les constats dans un second fichier scellé, `constats-de-l-etape-m-bras-a.json`. Le texte ne le nomme pas : c'est au relevé des défauts.

## 5. Essais d'attaque repris

| pièce de la contre-lecture | où elle est reprise |
|---|---|
| `attaques_regle_v1.py` (37 cas) | `tests/test_analyse_bras_a_v6.py` : structure, grandeurs exigées, famille, seuil, réglages, deux fichiers scellés |
| `attaques_fichiers_v1.py` | fichier de l'étape (m) écrit à la main ; issue de la table A fabriquée ; pièce aux formes non reconnues ; rangs |
| `attaques_cloisonnement_v1.py` (16 modules) | `test_les_seize_modules_de_l_essai_d_attaque_de_la_version_5` : 13 refusés, 1 témoin sain, 1 signalé, 1 limite écrite |
| `attaques_graines_v1.py` | jeton, `object.__new__`, réemploi, ligne qui refuse |
| `garde_sur_le_depot_v1.py` | `test_la_garde_passee_sur_src_et_scripts_du_depot` |

Trois cas de l'essai d'attaque changent de sens sous le brouillon 24, et l'essai le dit : le couple de tirages nul au cas C est admis ; la forme de la version 8 sous « tirages dégénérés » est refusée (et « non rendue » à la dose ¼) ; un motif quelconque au cas B est refusé, puisqu'il doit être dans sa liste fermée.

## 6. Notes des brouillons 22 à 24, point par point

| point | fait |
|---|---|
| 1. cas reconnu aux comptes, ordre B, C, E, D, A ; `motif` nomme le cas | `an.ranger_une_lecture` |
| 2. deux sortes d'écart | structure : arrêt à toute dose ; grandeur exigée nulle : arrêt aux doses de la famille, « non rendue » à la dose ¼ |
| 3. arrêt = événement nommé ; issue par choix | `arrets_bras_a_v6`, `v.issues` ; l'événement ne nomme aucune ligne de table |
| 4. valeur de la famille, égalité exacte | `==`, sans tolérance ; essai à une unité du dernier chiffre |
| 5. cas E, trois rédactions | un choix, un essai par valeur ; (c) lève le même événement |
| 6. motif « non ajustable », trois rédactions | un choix, un essai par valeur ; (a) et (c) codés de même ; nombre de lectures rapporté |
| 7. seuil en un seul endroit | un choix, un essai par option |
| 8. « non rendue » ; borne « non calculable » aux cas D et E | `an.juger_une_lecture`, `v.rapport_c4` |
| 9. couples nuls admis | les deux au cas B ; les tirages aux cas C et E |
| 10. listes fermées, vingt lectures, réglages | un artefact par réglage |
| 11. chaînes inconnues | toutes dans la configuration scellée ; aucune devinée |
| 12. empreinte du fichier des rangs | prise dans la pièce scellée |
| 13. `effectifs`, `exclues` | aucune règle ne les lit ; rapportés tels que rendus, comme les aires de l'agrégateur |
| 14. cas et motif des vingt lectures rapportés | `resultat["cas_et_motifs"]` |
| 15. sortie du programme qui refuse | cinq éléments, chacun pris dans une liste fermée ; essai sur onze refus |
| 16. étape de l'événement | (m) pour la sortie de la lecture commune, dose ¼ comprise ; (n) pour le fichier des rangs |

## 7. Ce qui est commun aux trois rédactions de l'issue

- L'arrêt est **consigné** : fichier scellé dans le dossier des arrêts, avec le constat et l'empreinte de la livraison.
- **Une livraison refusée n'est pas relue** : la règle la refuse si son arrêt est consigné.
- **Une livraison refaite n'est lue que sur une ligne de GO** du registre du dépôt, qui porte la phrase d'accord.
- Aucun état n'est dit après un arrêt : la règle ne rend rien.

Le versement de la livraison elle-même revient à l'enchaînement.

## 8. Ce qui reste à écrire (hors de mon mandat)

- Les lots, le client des lecteurs, le lanceur, l'enchaînement de l'analyse.
- Dans cet enchaînement : écrire et sceller la configuration ; appeler la garde statique sur `src` et `scripts` ; ne tirer d'un arrêt que son constat ; verser la livraison refusée.
- Une version nouvelle si le texte scellé retire des rédactions : le code les porte toutes aujourd'hui.

## 9. Réserves

1. **Contrôles que la liste de 6.9 ne nomme pas.** Valeurs p confrontées à leurs comptes ; entrée hors de sa place ; nombre hors de 0 à 1 ; borne rendue sans son quantile. Chacun est une cause d'arrêt de plus, dont l'issue est celle de la fiche 12. À inscrire au texte ou à retirer du code (relevé, partie A).
2. **Formes supposées.** `scores_par_unite.lignes` est lu comme un entier et `.champs` comme une liste : toute autre forme arrête. Le quantile nul est admis quand la borne est nulle.
3. **Provenance.** La pièce scellée et la configuration sont des fichiers dont le chemin vient de l'enchaînement. Le code vérifie leur compagnon et lie leurs empreintes au résultat et aux constats ; qu'elles soient les bonnes tient à leur inscription au registre.
4. **Ligne de GO d'une livraison refaite.** La phrase est de moi ; rien ne lie la ligne à une livraison donnée, et « une seule fois » n'est pas compté.
5. **Registre du dépôt.** Les lignes d'accord se lisent dans `registres/go.md` de l'arbre de travail, qui peut être en retard sur la branche principale.
6. **Un tirage ne sert qu'une fois.** Chaque intervalle d'un même lot rejoue donc la clé du lot : mêmes tâches tirées pour toutes les grandeurs. Le texte ne le dit pas.
7. **La garde statique n'est pas une preuve**, et le tirage à clé arrête l'oubli, non la fraude.
8. **Référence déplacée trois fois** pendant l'écriture. Je n'ai lu des brouillons 23 et 24 que 6.9 (« Ce que vaut cet arrêt », définition unique), les lignes de 8.4 et les notes.

## 10. Fichiers ouverts pour la version 6

- `docs/notes/relance-organismes-discrets-v1/` : `contre-lecture-code-v5-bras-a-v1.md` en entier ; les cinq programmes et leurs sorties sous `contre-lecture-code-v5-pieces/` ; les notes des brouillons 22 (en entier), 23 (en entier) et 24 (début et partie 6) ; `decisions-bras-a-brouillon22-v1.md` ; `verification-corrections-brouillon22-bras-a-v1.md` en entier.
- Brouillon 22 : conventions (ligne 155), 6.9 (lignes 693 à 713), 7.2 (ligne A17), 7.5, 8.4 (lignes 928 à 938), 6.3 (m) et (n).
- Brouillon 23 : 6.9 (lignes 703 à 711 et ligne du cas E), 8.4 (lignes 944 à 950).
- Brouillon 24 : 6.9 (lignes 711 à 721), 8.4 (lignes 959 et 960).
- Mes fichiers de la version 5 et leurs essais ; `src/controle_ia/scellement.py` (fonction `sceller`) ; `tests/conftest.py` (début).
- Par programme, pour la garde statique : `src/` et `scripts/`, chemins interdits élagués avant tout parcours ; seuls des comptes et des noms de fichier ont été affichés.
- **Non ouverts** : aucun interne de moniteur, aucun module habilité, aucune notice ni contre-lecture du côté habilité, aucune fiche de l'organisme d'idéation, aucune réponse de lecteur, aucune clé. Le registre des accords n'a pas été lu (les essais en fabriquent un). Aucun appel réseau ni de modèle, aucun sous-agent.
