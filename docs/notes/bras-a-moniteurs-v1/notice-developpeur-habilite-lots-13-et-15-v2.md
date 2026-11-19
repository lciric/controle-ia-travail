# Notice — développeur habilité côté moniteurs du bras A : extraction pour la base (lot 13) et tokeniseur de Qwen (lot 15) — version 2 du code

**En bref.**
- La version 2 applique les corrections de la contre-lecture (`contre-lecture-lots-13-et-15-bras-a-v1.md`, `73d4c58e…`), qui concluait « pas avant ». Aucun calcul ne change.
- Le rapport du tokeniseur est rendu **à l'octet** par la version 2 : `22073b32…` reste le rapport qui fait foi ; aucun rapport v2.
- 71 essais passent (68 sans le dossier du tokeniseur du juge). **Chaque garde des deux modules, retirée seule, fait échouer un essai** : 39 sur 39 pour l'extraction, 28 sur 28 pour le tokeniseur, avec ou sans le dossier du tokeniseur.
- La version 1 reste intacte ; ses essais l'éprouvent toujours.

Qui : développeur habilité côté moniteurs, session fille de la session mère `session_013QMayjsoZJFBUCqcnvD5h1`, le 19 novembre 2026. Rien ouvert sous `diag/`, `runs/`, `donnees/`, `docs/verdicts/` ; aucun résultat lu ; aucun poids chargé ; aucune dépense ; jamais la suite d'essais complète. Aucun outil refusé.

## 1. Fichiers

| rôle | chemin | empreinte |
|---|---|---|
| extraction, version 2 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/extraction_base_v2.py` | `d557c8396cf35acda5dfd21a8ad20cc146f337fd38f7db4cd10503d3fe7d2e0a` |
| ses essais | `tests/test_bras_a_v2_habilite_extraction_base_v2.py` | `acfa58ea452739e372ee4b114bf19a53edc7a90beebdf86ab3d9cda59046136a` |
| vérification du tokeniseur, version 2 | `src/controle_ia/organismes_discrets/bras_a_v2_habilite/verification_tokeniseur_qwen_v2.py` | `410b22e9888e9f221907aa757239c1b3100bde8f2ee2574bbdb182013a9e07d4` |
| ses essais | `tests/test_bras_a_v2_habilite_tokeniseur_qwen_v2.py` | `4e670c3c1c9d20408afa0d93be190f2a9e16f400ea6d611dc188f05f35bdf01d` |
| erratum de la notice v1 (scellé) | `docs/notes/bras-a-moniteurs-v1/notice-developpeur-habilite-lots-13-et-15-v1-erratum-1.md` | compagnon |

```
PYTHONPATH=src python -B -m pytest -q -p no:cacheprovider tests/test_bras_a_v2_habilite_tokeniseur_qwen_v2.py tests/test_bras_a_v2_habilite_extraction_base_v2.py
```
Dernière ligne : `68 passed, 3 skipped` ; `71 passed` avec `QWEN_TOKENISEUR_DOSSIER`.

## 2. Corrections, une par une

| correction du rapport | ce qui change |
|---|---|
| 1. Câblage de la garde de sortie (bloquant) | Essai du contre-lecteur recopié : `test_ecrire_refuse_et_n_ecrit_rien` (épisode manquant, ligne du témoin bénin, champ de plus : refus, rien d'écrit). Essai neuf : `test_extraire_appelle_la_garde_de_sortie` (un espion compte l'appel ; une garde qui refuse arrête l'extraction). Les deux appels, retirés, font échouer un essai. |
| 2. Gardes tautologiques | Tokeniseur : la garde « la balise seule ne se découpe pas comme la balise » est retirée ; la docstring dit que la balise peut se découper autrement selon ce qui la précède. Extraction : les trois gardes de constante deviennent des assertions marquées « hors R5 ». |
| 2 bis. Garde redondante | Extraction, garde de sortie : « 7 680 lignes » est impliquée par les gardes d'épisodes, de pas et de clés ; elle devient une assertion marquée « hors R5 ». |
| 3. Artefacts manquants | Un essai par garde : voir la table de la partie 3. Les gardes des jetons spéciaux ont un cas sain sur un tokeniseur jouet ; elles ne dépendent plus du vrai tokeniseur. |
| 4. Nom d'essai | `test_textes_du_temoin_benin_absents_de_la_sortie`. |
| Errata de la notice | Fichier d'erratum scellé ; la notice v1 n'est pas récrite. |

**Deux changements de plus, tirés des remarques du rapport.**
- **Dossier de sortie de l'extraction** (rapport, partie 2, « chemin réel de la base »). L'extraction reçoit la racine du dépôt (`--racine`) ; elle refuse un dossier de sortie hors de cette racine, ou dont le chemin relatif porte un fragment que la liste blanche de la base refuse. La docstring dit que la base se lance avec la racine des entrées égale à ce dossier.
- **Rapport déjà présent** (R12) : la vérification du tokeniseur refuse avant toute lecture, et non après.

**Ce qui n'est pas changé.** Le rendu du gabarit par le programme reste une réimplantation, que le contre-lecteur a trouvée égale à la bibliothèque du modèle. Le chemin de rendu réel est éprouvé au lot 14, qui emploie la bibliothèque elle-même.

## 3. Artefacts ajoutés

| module | garde | essai |
|---|---|---|
| tokeniseur | chiffre seul en plusieurs jetons | `test_decoupage_chiffre_seul_en_plusieurs_jetons_arrete` |
| | deux chiffres sur un même jeton | `test_decoupage_deux_chiffres_sur_un_meme_jeton_arrete` |
| | jeton de chiffre après la valeur | `test_decoupage_jeton_de_chiffre_apres_la_valeur_arrete` |
| | jetons des chiffres ≠ ceux du vocabulaire | `test_coherence_du_decoupage_et_du_recensement` |
| | jeton ajouté à deux identifiants | `test_recensement_jeton_ajoute_a_deux_identifiants_arrete` |
| | date posée dans le gabarit | `test_gabarit_date_posee_dans_le_gabarit_arrete` |
| | la réponse prolonge l'invite | `test_gabarit_reponse_qui_ne_prolonge_pas_l_invite_arrete` |
| | jetons spéciaux (neuf gardes) | `test_jetons_speciaux_cas_sain_sur_jouet` ; `test_jetons_speciaux_artefacts` (douze cas) |
| | rapport déjà présent | `test_rapport_deja_present_refuse_avant_toute_lecture` |
| | rapport identique à l'octet au rapport scellé | `test_vrai_tokeniseur_rapport_identique_a_l_octet` (avec le dossier du tokeniseur) |
| extraction | épisode sans ses champs ; sans identifiant de tâche | `test_episode_sans_ses_champs_arrete` |
| | épisode hors de 0 à 7 | `test_episode_hors_de_zero_a_sept_arrete` |
| | action ou texte hors format | `test_action_ou_texte_hors_format_arrete` |
| | sortie : condition, tâche, format | `test_garde_de_sortie_condition_tache_et_format` (sept cas) |
| | listes de noms | `test_listes_de_noms_de_la_configuration_du_bras` |
| | source absente ; condition hors format | `test_source_absente_et_condition_hors_format` |
| | configuration du bras sans compagnon ; altérée | `test_configuration_du_bras_sans_compagnon_ou_alteree` |
| | dossier de sortie | `test_dossier_de_sortie_sous_la_racine_et_sans_fragment_refuse` |

## 4. Épreuve par retrait

Dans une copie de `src/` et des essais, chaque `raise GardeArret` d'un module est neutralisé seul, puis le fichier d'essais du module est joué ; la copie est restaurée après chaque essai. Résultat : aucune garde ne survit, pour les deux modules. La méthode diffère un peu de celle du contre-lecteur (il remplace la condition par « faux » ; ici l'arrêt est retiré) : à refaire par lui pour la vérification courte.

## 5. Ce qui reste

- Vérification courte des corrections par le même contre-lecteur.
- Les deux remarques du rapport pour le lot 14 (balise imposée encodée avec le texte qui la précède ; chemin de rendu réel du gabarit éprouvé) seront traitées avec les corrections de la contre-lecture du lot 14, en une version 2 de ce module.
- Aux cases de 13.1, citer la version 2 : commit de la branche et empreintes de la table ci-dessus.
