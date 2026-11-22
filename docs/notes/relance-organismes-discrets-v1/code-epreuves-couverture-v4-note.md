# Code des épreuves de la couverture du bras A, version 4 — note

- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), agent du code délégué par la session de relance. Date : 2026-11-22. Branche `claude/pensive-bardeen-1fv7hw`. Processeur seul ; aucun réseau, aucune clé, aucune dépense, aucun commit.
- **Texte** : `prereg/T0.7-organismes-discrets-v-a-v2-brouillon47.md`, `f59f6b4ed2b1198c3781badf83692d593ed4ade0df5baa9f0e4ea8b1827a6cb9` (lignes 655, 713, 817 à 820, 1171, 1467). Le code suit le texte ; le texte n'est pas changé.
- **Contre-lecture appliquée** : `docs/notes/relance-organismes-discrets-v1/contre-lecture-instrument-bras-a-v1.md`, `b2f36f0a1e6ce1c48be6a44a8d847aab6200219350cfa60ede99d5c68f4d0dce` (E-M1, E-M2, E-m1 à E-m5, I-m1).
- **Version 3 inchangée** : `epreuves_couverture_bras_a_v3.py` `c4e8b5b5…71211`, ses essais `530265b0…ed3b6` (R12).

## Fichiers neufs

| fichier | empreinte sha256 |
|---|---|
| `src/controle_ia/organismes_discrets/epreuves_couverture_bras_a_v4.py` | `9502437b27ffb6c0dd44047046d1e1e3bbad6aa27111bcf26317354f4b8e7e74` |
| `tests/test_epreuves_couverture_bras_a_v4.py` | `9254ddcf4b16f532f423bfd4234cf1ea19aaef6349fa0aec88915eddc5f43ecb` |
| `tests/test_instrument_appariement_v4_brouillon47.py` | `cef492580ce70de2f107043cf16fed5adfb1e40120557337f0aa32659ce8e591` |

## Changements, ligne du texte, essais (sain / artefact / écart v3 → v4)

- **E-M1, plan tronqué** (ligne 819 : « la seconde grandeur se compte sur les contrôles qui ont au moins un extrait connu ») : `grandeurs_du_plan_tronque` divise par le nombre de contrôles à extrait connu (rendu sous `controles_a_extrait_connu`). Plan sans aucun tel contrôle : part `None`, non définie, comptée (le texte est muet ; lecture prudente de la contre-lecture et de la ligne 1171, « jamais remplacé par une valeur ») — **point ouvert au texte**. Garde neuve : plus de contrôles à extraits connus que la référence n'en a → arrêt. Essais : `test_e_m1_denominateur_des_controles_a_extrait_connu_et_ecart_v3` (un perdu, un seul contrôle à extrait connu sur trois : v3 0,333…, v4 1,0 ; `{}` et listes vides → `None` ; gardes), `test_extrait_a_cheval_sur_les_rangs_4_et_5_est_perdu`.
- **E-M2, dose flagrante** (ligne 820 : « vérifié dans le plan de l'artefact et dans aucune de ses parties non remplacées ») : `parties_non_remplacees` (neuve) coupe le **texte du plan** (`artefacts_v1.texte_du_plan`) hors des cœurs des valeurs de `CONTROLS` (ce que `remplacer_les_controles` remplace), séparateurs compris ; `comptes_de_la_dose_flagrante` y cherche l'extrait. Essais : `test_e_m2_extrait_a_cheval_hors_des_champs_remplaces_et_ecart_v3` (sonde de la contre-lecture `hausse de K0 … TITLE: Expérience 1` : v3 `(1, 3)`, v4 `(0, 3)` ; à cheval entre partie gardée et valeur remplacée : reste `(1, 3)`, lettre du texte), `test_parties_non_remplacees_du_plan`. L'argument est maintenant le plan de l'artefact (actions non vides ; une action vide arrête par `texte_du_plan`).
- **E-m1** (même ligne 820, première condition) : la lecture donnée doit être celle du plan de l'artefact — statut strict recalculé par `reponses_lecteurs_v5.statut_strict_couverture`, présents égaux, sinon arrêt. Essai : `test_e_m1_lecture_qui_n_est_pas_celle_de_l_artefact` (lecture du plan source : v3 `(1, 3)` sans arrêt, v4 arrêt ; lecture de l'artefact : sain).
- **E-m2** (3.3, règle de la lecture) : « retrouvé » (plan tronqué) passe par `statut_strict_couverture` (24 caractères ou champ court `TITLE`, `PROPOSAL`, `CONTROLS`) ; « dans une partie non remplacée » : 24 caractères dans une partie, ou, plus court, valeur entière d'un `TITLE` ou `PROPOSAL` (la valeur entière d'un `CONTROLS` est remplacée). Extrait connu vide : arrêt (la v3 le comptait « perdu »). Essais : `test_e_m2_plan_tronque_extrait_court_sous_la_regle_de_la_lecture` (titre court retrouvé par hasard : v3 non perdu, v4 perdu ; titre entier gardé : sain ; vide : arrêt), `test_e_m2_dose_flagrante_extrait_court_sous_la_regle_de_la_lecture` (valeur entière courte d'un `CONTROLS` remplacé, sous-chaîne d'une proposition : v3 0, v4 1 ; titre entier : 0).
- **E-m3** (ligne 713 : « dans la liste triée de tous les mots ») : `mots_des_autres_taches` rend `sorted(mots)`. L'ordre de tri n'est pas dit au texte (pris : points de code, `sorted` de Python) — **point ouvert au texte** (une demi-phrase). Change les mots tirés sous une clé donnée, pour la dose flagrante **et** pour le texte sans rapport du lot honnête de l'appariement (même fonction). Essai : `test_e_m3_liste_triee_et_ecart_v3` (même multiensemble, ordre différent, doublons gardés).
- **E-m4** : import de `reponses_lecteurs_v5` ; essais par `reponses_lecteurs_v5` et `analyse_bras_a_v13.spearman`.
- **E-m5** : les quatre cas manquants ont leurs essais (ci-dessus).
- **I-m1** : `tests/test_instrument_appariement_v4_brouillon47.py` lit les consignes dans le brouillon 47 et la case « consignes figées » (ligne 1467) par programme : empreintes `98a9bd34…c9248` et `ecf590ea…1816`, égales ; artefacts (un caractère, consigne échangée) refusés. Module inchangé.

Inchangés : retrait, référence d'une autre tâche, `plan_tronque`, `remplacer_les_controles`, `texte_tire`, `plan_a_dose_flagrante` (l'empreinte d'un artefact de retrait est essayée égale à celle de la v3).

## Essais de la v3 repris, remplacés

Repris tels quels (statuts par v5) : retrait, référence d'une autre tâche, construction du plan tronqué, dose flagrante et texte sans rapport. **Remplacés, déclarés** : (1) `part_des_controles_perdus == 1/3` devient `1/2` (E-M1 ; même entrée) ; (2) `mots[:3] == ["Entraîner", "le", "modèle"]` devient `mots == sorted(mots)` (E-m3). Le fichier d'essais de la v3 reste vrai pour la v3 et passe.

## Campagne de mutations (script hors dépôt, dans le dossier temporaire de la session ; module muté en place puis restauré, empreinte revérifiée égale)

18 mutants sur `grandeurs_du_plan_tronque`, `comptes_de_la_dose_flagrante` et leurs aides (`_retrouve`, `parties_non_remplacees`, `_dans_une_partie`) et le tri : **17 tués**. Survivant déclaré : M17 (seuil 24 → 1 dans la branche des extraits de 24 caractères ou plus de `_dans_une_partie`) — **équivalent** : la branche n'est atteinte que si l'extrait normalisé compte déjà au moins 24 caractères. M11 (séparateur oublié dans les positions) survivait au premier passage : essai renforcé (bords de chaque partie), tué.

```
TUÉ M1 dénominateur v3 (n_controles) · TUÉ M2 sans extrait connu → 0.0 · TUÉ M3 a_extrait = tous les contrôles
TUÉ M4 garde len > n retirée · TUÉ M5 _retrouve sous-chaîne nue · TUÉ M6 extrait connu vide admis · TUÉ M7 any → all
TUÉ M8 garde E-m1 retirée · TUÉ M9 parties par action (v3) · TUÉ M10 coupe sur la valeur brute
TUÉ M11 séparateur oublié · TUÉ M12 dernière partie oubliée · TUÉ M13 court : CONTROLS admis
TUÉ M14 court : sous-chaîne nue · TUÉ M15 dénominateur = présents · TUÉ M16 tombé inversé
SURVIT M17 seuil 24 → 1 (équivalent) · TUÉ M18 mots non triés (v3)
17/18 tués ; module restauré, empreinte 9502437b27ffb6c0dd44047046d1e1e3bbad6aa27111bcf26317354f4b8e7e74
```

## Commandes et sorties

```
$ PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_epreuves_couverture_bras_a_v4.py
12 passed in 0.93s
$ PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_epreuves_couverture_bras_a_v3.py
4 passed in 0.82s
$ PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_instrument_appariement_v4_brouillon47.py
1 passed in 0.13s
$ PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider tests/test_instrument_appariement_v4.py
25 passed in 6.19s
```

## Restes ouverts

- Au texte : part des perdus d'un plan sans contrôle à extrait connu (ici non définie, comptée) ; ordre du tri de la liste des mots (ici points de code) ; la case « commit » doit nommer `epreuves_couverture_bras_a_v4.py` et la présente note.
- `comptes_de_la_dose_flagrante` tient pour remplacée toute valeur non vide de `CONTROLS` de l'artefact, relue par `empan_valeur` sur l'artefact : un mot tiré qui ferait naître une clé en début de ligne déplacerait l'empan (impossible avec des mots joints par une espace sur la ligne de la clé ; non essayé).
- Le module des lots (`lots_bras_a_v1.py`, non ouvert) appelle la v3 : son passage à la v4 n'est pas fait ici. Un `brouillon48` est apparu dans l'arbre pendant le travail (non ouvert).

## Ce que j'ai ouvert

CLAUDE.md (consignes de session) ; la contre-lecture en entier ; du brouillon 47, lignes 655, 713, 817 à 820, 1467 et le relevé `grep` de quelques mots (dont 1171) ; `epreuves_couverture_bras_a_v3.py` et ses essais en entier ; `tests/test_instrument_appariement_v4.py` (lignes 1 à 40, 468 à 478, noms des fonctions) ; `instrument_appariement_v4.py` (`consignes_du_texte`, `empreinte_consigne`, `exiger_consigne_figee`, `valeur_champ`) ; `reponses_lecteurs_v5.py` (`statut_strict_couverture`, `_valeurs_entieres`, champs du champ court, noms des fonctions) ; `artefacts_v1.py` (lignes 62 à 155) ; `fabrication_v3.py` (`_CLE`, `empan_valeur`, `decouper_texte`) ; `analyse_bras_a_v13.spearman`. Aucun chemin cloisonné ; une recherche récursive dans `src/` a été refusée par la garde de la session et non refaite.
