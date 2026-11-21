# Rapport du développeur — code de commande de la relecture, version 2 (additif 1 v2 au devis du barreau 5) — v1

- **Nature** : rapport d'une pièce de classe B (code). Écrit par Claude Fable 5.2, développeur, agent neuf, le 21 novembre 2026. Mandat : `mandat-developpeur-commande-lecture-v2-v1.md` (`7c52ca65dd0e616bff12bfe86727b0796b6b33b4fa3dc97cefcc0f866d1542af`, vérifié contre son compagnon). Pièce qui commande : additif 1, version 2, au devis (`c3120d3ade40f31f26a225cd2bf7c3520c7ba0a314e2b554832229d67c8e120c`, vérifié).
- **Verdict** : le montage du § 3 de l'additif se code sans toucher un fichier existant et rend la commande de la version 1 à l'octet, pour les deux pièces. Je ne le juge pas plus risqué qu'un code de lecture neuf : pas de nœud levé de mon côté. Cinq écarts à l'additif, nommés au § 6. Reste à faire par d'autres : contre-lecture par un autre modèle, puis essais du paquet entier au commit de commande.
- Aucune dépense, aucune commande au loueur, aucun appel réseau, aucune clé lue ni affichée, rien poussé, aucun commit dans `/home/user/controle-ia-travail`.

## 1. Commit de commande et liste fermée

- Arbre : `…/scratchpad/arbre-commande`, branche locale `course/barreau5-commande-lecture-v2`.
- **Commit de commande : `76c608b61d52549d4e0dceb9d07be0c5bea273f8`**. Son parent, `d532ed0ff…`, ne porte que le fichier d'épreuves, commis avant le code ; lui-même a pour parent le commit du code de lecture figé `c76e79169eee337ce66c7d88f62d039e853eebfc`.
- `git diff --name-status c76e7916 HEAD` : trois lignes, toutes « A ». Aucun fichier existant modifié. Arbre de travail propre après les essais.

| fichier ajouté (liste fermée, écrite dans le module : `LISTE_FERMEE`) | sha256 |
|---|---|
| `scripts/lancer_b5f_lecture_v2.sh` | `c07fc1244860aa9795b3c5b610ddc78115f58c818ecb25b9aa2fcfae87aabcbf` |
| `src/controle_ia/barreau5_familles/commande_lecture_v2.py` | `c6c5d11c04f337c789c7f5a289d5190f51772b4ff96893499a8a5d07bc565ef0` |
| `tests/test_commande_lecture_v2.py` | `535e719526e292e66daf7ea35969eee0166f9dadcebe7eff20897aa6908ac01e` |

## 2. Ce que fait le code

- **Garde du stockage** : `exiger_offre_lecture_v2`, plafond par pièce (`PLAFOND_STOCKAGE_USD_H` : « decisif » 0,12 ; « repetition » 0,08), même formule (`storage_cost` × disque / 730), mêmes autres bornes lues dans `relecture_v1.OFFRE_LECTURE`.
- **Corps recomposé** : `corps_recompose` reprend les lignes 1049 à 1099 de `relecture_v1.py` à deux remplacements près (stockage ; garde de l'arbre de la session remplacée par (d), (b), (c)). Les fonctions et constantes de la version 1 sont importées, non copiées.
- **(a)** `relecture_v1.exiger_code_du_commit`, inchangée. **(b)** `exiger_session_au_commit_de_commande`. **(c)** `exiger_commande_issue_du_code_fige`. **(d)** `commit_de_commande_cite`.
- **Entrée unique** : `commande_de_creation_v2` refuse tout plan autre que « decisif », puis refuse d'être jouée depuis un autre arbre que celui de la session, puis joue le corps. Le lanceur ne porte que « commande decisif … » et renvoie toute autre sous-commande au lanceur de la version 1, depuis l'arbre figé.

## 3. Format de la colonne de référence de `GO-LECTURE-B5F`, lu par (d)

Lu à la lettre, en entier (`fullmatch`), dans la colonne de référence rendue par `engagement_v1.lignes_du_registre` :

    <nom de la session de lecture> ; additif 1 v2 au devis sha256 <64 signes hexadécimaux minuscules> ; commande de lecture v2, commit <40 signes>, vérifiée sha256 <64 signes>

suivi au plus de « ; <texte libre> ». Le nom de la session est exigé non vide. Les chaînes « additif 1 v2 au devis » et « commande de lecture v2 » n'y figurent qu'une fois chacune. L'empreinte de l'additif doit être `c3120d3a…120c`. L'empreinte après « vérifiée » est celle du rapport de vérification du code : seule sa forme est lue. Ni barre verticale ni saut de ligne.

Exemple (pour le commit de commande d'aujourd'hui ; l'empreinte du rapport de vérification est à venir, notée ici par des zéros) :

    session de lecture session_XXXX ; additif 1 v2 au devis sha256 c3120d3ade40f31f26a225cd2bf7c3520c7ba0a314e2b554832229d67c8e120c ; commande de lecture v2, commit 76c608b61d52549d4e0dceb9d07be0c5bea273f8, vérifiée sha256 0000000000000000000000000000000000000000000000000000000000000000

Si la contre-lecture demande une correction du code, le commit de commande change, et la citation avec lui.

## 4. Épreuves du § 3.4 : nom, ce qu'elle prouve, rouge puis verte

Rouge d'abord : le fichier d'épreuves a été joué avant que le module existe (import en échec, `sortie-01-epreuves-avant-le-code-rouge.txt`) et commis seul. Puis, le code écrit, **21 mutations, une par garde**, chacune portée dans le module ou le lanceur, tout le fichier rejoué, fichier rendu à l'octet (empreintes vérifiées). Chacune a rendu au moins un essai rouge ; relevé complet : `sortie-03-mutations.txt` et `.json`. Verte : 111 essais passés au commit de commande.

| épreuve du § 3.4 | essais | ce qu'elle prouve | mutation vue rouge |
|---|---|---|---|
| Stockage, sain | `test_stockage_decisif_cas_sains_offre_du_releve_et_frontiere`, `test_stockage_par_le_corps_recompose` | offre 32744970 (0,24) acceptée ; 0,2920 rend 0,12 juste et passe | M19 (formule à 720) ; M01 |
| Stockage, artefacts | `test_stockage_decisif_artefacts_refuses` (0,2921 ; 0,30 ; 0,32) | refus au-dessus de 0,12 | M01 (plafond à 0,14) |
| Stockage, témoin | `test_stockage_temoin_la_version_1_refuse_l_offre_du_releve` | la borne de 0,08 mord encore en version 1 | M17 |
| Portée, entrée | `test_portee_l_entree_de_la_version_2_refuse_la_repetition` | « repetition » refusée à l'entrée | M03 |
| Portée, corps | `test_portee_repetition_par_le_corps_recompose_…` | 0,40 refusé, 0,19 accepté à 150 Go | M02 (répétition à 0,12) |
| Portée, constantes | `test_portee_les_constantes_…_a_0_08` | version 1 et formation à 0,08 | M02 |
| Égalité à l'octet | `test_egalite_a_l_octet_…[decisif]`, `[repetition]` | même commande que la version 1, deux pièces | M18 (branche répétition infidèle : seul `[repetition]` rougit) |
| Rien d'autre ne change | `test_difference_fermee_…`, `test_les_noms_du_corps_…`, `test_memes_autres_bornes_…` (30 cas), `test_les_autres_gardes_…` (15 cas) | différence de source fermée à deux blocs ; mêmes objets ; mêmes refus | M04, M18 |
| (a) | `test_a_marche_dont_l_arbre_gele_differe`, `test_a_marche_qui_porte_le_module_neuf` | marche au code changé ou portant le module : refus | M04 |
| (b) | `test_b_arbre_de_session_autre_…`, `test_b_arbre_de_travail_change`, `test_b_fichier_non_suivi_sous_src` | les trois clauses, une à une | M05, M06, M07 |
| (c) | `test_c_…_modifie_supprime_ou_ajoute_hors_liste` (4 cas), `test_c_…_sans_le_module_ou_sans_le_lanceur`, `test_c_…_ne_descend_pas_…` | modifié, supprimé, hors liste, incomplet, sans ascendance : refus | M09, M10, M11, M08 |
| (d) | `test_d_…_sans_la_citation`, `test_d_…_autre_empreinte_…`, `test_d_citation_d_un_autre_commit`, `test_d_format_…_lu_a_la_lettre` (15 artefacts) | citation absente, autre additif, autre commit, format faux : refus | M14, M12, M13, M15 |
| Montage complet, sain | `test_montage_complet_cas_sain`, `test_lanceur_…_cas_sain_et_refus` | commande rendue, en processus et par le lanceur joué depuis l'arbre de commande | M16, M20 |
| Les deux arbres | `test_les_deux_arbres_verifier_de_la_version_1` | « verifier » v1 acceptée depuis l'arbre figé, refusée depuis le commit de commande (constat C2) | artefact vu rouge par construction : c'est la version 1 qui refuse |
| Registre | `test_registre_a_la_forme_d_aujourd_hui_…`, `test_registre_corrige_par_la_voie_c_…`, `test_registre_corrige_plus_une_cle_inventee_refuse` | les trois objets de la voie (c), mêmes réponses en version 1 et 2 | M18 pour l'objet 2 ; les deux autres sont des refus de la version 1 |
| Registre réel | `test_registre_propre_reel_…` (joué sur demande, § 5) | idem sur le registre propre réel | — |
| Aucune substitution | `test_aucune_substitution_dans_le_module_neuf`, `…_l_epreuve_voit_une_substitution` (12 artefacts), `test_les_modules_figes_ne_sont_pas_alteres_…` | aucune affectation d'attribut ; l'épreuve voit douze formes de substitution | M17 |
| Lanceur | `test_lanceur_…_refuse_toute_autre_sous_commande` (15 cas), `test_texte_du_lanceur_…` | seule « commande » sort du code figé | M21 |
| Module joué (ajout, § 6) | `test_entree_le_module_joue_…` | l'entrée refuse un module joué hors de l'arbre de la session | M16 |

## 5. Comptes d'essais (au commit de commande, `sortie-05-essais-au-commit-de-commande.txt`)

| fichier | résultat |
|---|---|
| `tests/test_commande_lecture_v2.py` | 111 passés, 1 sauté (le registre réel, sans sa variable) |
| le même, registre réel seul (`B5F_REGISTRE_PROPRE_REEL` = la pièce `registre-propre-main-25236c16.md`) | 1 passé |
| `tests/test_barreau5_familles_relecture_v1.py` | 24 passés |
| `tests/test_lancer_b5f_lecture_v1.py` | 43 passés |
| `tests/test_barreau5_familles_engagement_v1.py` | 23 passés |

**Registre réel, par le corps recomposé et par la version 1, mêmes réponses** (`sortie-02-registre-propre-reel.txt`) : état d'avant la voie (c), reconstitué et vérifié à `c4aeced7…fe63` : refus, « registre propre, ligne 13 : clé ENGAGEMENT-RECREATION-3-B5F inconnue », pour les deux pièces. Copie corrigée : lecteur passé, six clés ; la relecture décisive s'arrête à « engagement absent » (la ligne `ENGAGEMENT-B5F` n'y est pas encore), la répétition à la garde du code du commit (le commit `c76e7916` n'est pas dans le dépôt d'essai). Copie corrigée plus une clé inventée : refus à la ligne 20. Le registre de main d'aujourd'hui (avec `SORTIES-FORMATION-B5F`) répond comme la copie corrigée.

## 6. Écarts à l'additif, nommés

1. **Un second objet privé récrit.** L'additif dit que `_montrer` est la seule fonction privée du corps. Le corps emploie aussi le motif privé `_RUN_LECTURE` (ligne 1061). Je l'ai récrit dans le module, à l'identique, non importé ; un essai compare les deux motifs.
2. **Une garde ajoutée à l'entrée, non demandée.** `exiger_module_joue_depuis` : le module joué doit être celui de l'arbre que vérifie (b). Sans elle, (b) et (c) pourraient porter sur un arbre propre pendant que le code joué vient d'un autre. Elle ne desserre rien ; elle peut bloquer si le lanceur est joué avec une `RACINE` autre que son propre arbre. Au contre-lecteur de dire s'il la garde.
3. **(c) exige aussi la présence du module et du lanceur** parmi les fichiers ajoutés, en plus de « rien hors liste ». Plus strict que la lettre.
4. **Le corps, pour « repetition », prend la tête de la session comme commit de commande.** L'additif veut les deux branches dans le corps et le refus à l'entrée, sans dire ce que devient (d) pour la répétition. C'est la garde plus faible que décrit son § 3.3 ; elle n'est atteinte par aucune entrée (ni le module, ni le lanceur), seulement par les essais.
5. **Format de (d)** : j'ai fixé « vérifiée sha256 <64 signes> » (l'additif écrit « vérifiée [empreinte du rapport] ») et exigé un nom de session non vide en tête.

Hors additif, à signaler :
- **Lignes d'attribution des commits.** Le mandat demande des messages « sans identifiant de modèle ». Le corps des deux messages n'en porte pas, mais j'ai gardé en pied les deux lignes d'attribution que porte chaque commit du dépôt (`Co-Authored-By`, `Claude-Session`), dont l'une nomme le modèle. Si la mère les veut ôtées, le commit de commande change d'identifiant.
- **Pièce sans compagnon.** `registre-propre-main-25236c16.md` n'a pas de compagnon `.sha256` dans le dossier des pièces. Empreinte relevée : `41f5ec1485b5c60c00448c5f341ad6ca3876ffb5c3c6c64b3bc43183eecfffd4`. Je l'ai employée en lecture seule ; son contenu se recoupe par l'empreinte `c4aeced7…` de l'état reconstitué.
- **Périmètre.** Deux sorties d'outil trop longues ont été rangées par l'outil sous `/root/.claude/…` ; je ne les ai pas ouvertes, j'ai relu les pièces par leur chemin. Une commande `ls` a listé les noms de la racine de l'arbre de commande (dont `brouillons`, `diag`, `donnees`, `runs`) : noms seulement, rien d'ouvert. `harnais/validation_reelle.py` n'a pas été ouvert : sa constante `CHEMINS_GELES` est importée, comme le fait la version 1. Les essais copient le texte scellé et la configuration scellée dans le dépôt d'essai sans les lire, comme ceux de la version 1.
- **Offre du relevé.** Je n'ai pas le relevé (hors liste) : l'offre 32744970 des essais est bâtie des chiffres du § 1 de l'additif ; la mémoire de la carte (81 920 Mo) est une valeur d'essai.

## 7. Ce que je n'ai pas fait

- Les essais du paquet entier au commit de commande (893 au dernier relevé du registre) : seuls les quatre fichiers du mandat ont été joués.
- Aucune exécution sur le dépôt réel avec un vrai commit de marche : la ligne `GO-LECTURE-B5F` n'existe pas encore ; le montage n'est éprouvé que sur des dépôts d'essai.
- `registres/go.md` de l'arbre de commande n'a pas été mis à jour (réserve 2 du scellement) : c'est à la session ; un essai montre que ce fichier peut changer dans l'arbre de travail sans faire refuser (b).
- Le pas 4 de l'additif (prix d'une recherche à 300 Go) reste supposé : rien dans ce code ne le vérifie, comme l'additif l'a décidé.

## 8. Pour le contre-lecteur

Par où ce code pourrait être jugé bon sans le mériter : l'égalité à l'octet est prouvée sur un dépôt d'essai, non sur le dépôt réel ; l'essai de différence fermée compare des sources, il ne dit rien des fonctions (b), (c), (d) elles-mêmes, que seuls leurs artefacts éprouvent ; (b) ne voit pas un fichier non suivi sous `scripts/` (clause reprise telle quelle de la version 1). Pièces du bloc-notes : `mutations.py`, `sortie-01` à `sortie-05`, `empreintes-avant-mutations.txt`.
