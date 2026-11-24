# Vérification des corrections du code de la lecture des sondes v6 (barreau 8) — Sonnet 5.5

## En-tête

- **Qui** : Claude Sonnet 5.5, même contre-lecteur que pour `contre-lecture-conformite-lecture-v6-sonnet-v1.md` (non touché). Vérification des corrections seulement, pas une nouvelle contre-lecture entière.
- **Quand** : 2026-11-24, après 14:30Z. Branche `barreau8/code-lecture-sondes-v6-v1`, tête `eb2d3ac0` (diff lu : `746e80cf..eb2d3ac0` sur `src/`, `tests/` et la notice v7). Arbre de travail propre avant et après.
- **Empreintes lues** (`sha256sum`) :
  - `lecture_sondes_v6.py` : `8b39af4b760c1a621093a31616214d0ff7802212322a020cb67cba2f9a16570a` ;
  - `lectures_descriptives_additif_1_v1.py` : `1135731ce34a929287610316b929a4075c200f6d89bbbcd00a08189efa18420b` ;
  - `tests/test_barreau8_moniteurs_lecture_v6.py` : `505d1e3fed63f4aa7b5453cd2da7ca376355728daf8ac9449c9f734c6d452586`.
- **Cloisonnement** : même que la première fois. Mutations sur une copie de `src/` de mon bloc-notes ; aucun fichier du dépôt modifié.

## Essais

`PYTHONPATH=src .venv/bin/python -m pytest -q tests/test_barreau8_moniteurs_lecture_v6.py -p no:cacheprovider` : **`150 passed in 193.13s`**. Attendu : 150.

## Constat par constat

| # | constat | état | lieu et vérification |
|---|---|---|---|
| 1 | cascade : actions sans rang honnête non comptées | **porté** | `lectures_descriptives_additif_1_v1.py` `ld2`, début : `actions_sans_rang_honnete_cascade` et son détail par condition, dans `episodes`. Le compte est `notees & isnan(rangs_honnetes(...)[0])` : il ne dépend que des rangs de pas et des tâches. Essai `test_ld2_actions_sans_rang_honnete_comptees_…` : valeurs attendues 3 et `{H: 1, S: 1, J: 1}` établies à la main. Mutant « compte forcé à 0 » : tué. |
| 2 | différences de rappels sans parts d'alertes de h ni n, k | **porté** | `ld2` : chaque ligne de différence porte `part_d_alertes_h` et `n_et_k_de_h` des deux lectures comparées (`maximum` et la base), tirés de la ligne de rappel (sixième élément du tuple `etat_lecture`) ; `_difference_de_rappels` lit `a[:5]`, inchangé pour le calcul. Écrits avant la branche « seuil au plafond », donc aussi sous « non définis ». Essai sur les clés. Mutant « parts retirées » : tué. |
| 3 | rang de « postérieure » non éprouvé seul | **porté** | Essai `refus("rang-seul-anterieur", …)` : ligne `CODE-LECTURE` datée après l'additif 2 mais placée avant lui dans le fichier ; refus attendu `23`. Mutant N3 (rang ignoré) : **tué**. |
| 4 | O-2 et O-4 non éprouvés | **porté** | `ARTEFACTS_ORDRE` : deux artefacts de plus. Mutants « O-2 non requis » (M4) et « O-4 non requis » : **tués**. |
| 5 | ex aequo non éprouvés | **porté** | `test_ld_ex_aequo_pour_moitie_valeurs_a_la_main` : aire intra-tâche 5/6 et rangs honnêtes 0,5 et 0,75, valeurs calculées à la main (je les ai refaites : justes). Mutants N8 (`<` en `<=`) et N9 (ex aequo à 0) : **tués**. |
| 6 | « dernier état » non éprouvé | **porté** | `test_ld_dernier_etat_prend_le_plus_grand_rang_de_pas_note` : dernière action la plus basse, puis dernier pas non noté. Mutant N20 (`argmin`) : **tué**. |
| 7 | bornes du marquage R4 ; D-15 déclarée « écart » avec tout « oui » | **porté** | `test_ld_marquage_r4_aux_bornes` (0,96, 0,951 et 0,04 marquées ; 0,95, 0,94, 0,05, 0,06 non ; rappel 1 marqué, 0,99 non). Mutants N11 (seuil haut 0,99) et N11b (seuil bas 0,01) : **tués**. Artefact `ecart-declare-tout-oui` ajouté à l'essai D-15 : mutant P1 (comparaison au verdict déclaré retirée) : **tué**. |
| 10 | structure des rôles (s3), (s6), (s7), (s8) non rejouée | **porté** | `lecture_sondes_v6.py` `forme_depuis_table` : (s3) dose de p égale à celle de j ; (s6) h à dose 0 ; (s7) sabotées à un même adaptateur et à dose strictement positive ; (s8) adaptateur de j porté par aucune autre condition. Refus code 20. Je les ai relues contre la lettre de l'additif 1 : conformes. Cinq artefacts ajoutés ; cinq mutants (un par condition, s7 en deux) : **tués**. **La vraie table neuve est acceptée** : `forme_depuis_table(exiger_table_neuve(table réelle))` rend les conditions `H, B50, B100, TJ100`, p = `B100` ; `exiger_pieces_d14` sur les vraies pièces rend ses cinq clés ; l'essai sur la vraie table passe. |
| 11 | brouillon 1 du rapport v5 accepté | **porté en partie** | Code : `SHAS_RAPPORTS_CONFORMITE_ANTERIEURS` = `fa9158fb…` et `44aaa3da…` ; refus à la lecture du bordereau et à son écriture. J'ai recalculé : `44aaa3da…` est bien l'empreinte du brouillon 1 sur disque. Essais : le côté lecture est éprouvé (mutant « contrôle retiré à la lecture » tué par `test_refus_de_tourner`). **Restent non éprouvés** : le côté écriture (`ecrire_bordereau_du_code`, mutant « contrôle retiré » survivant) et la valeur du second empreinte (mutant « tuple tronqué » survivant) ; la boucle ajoutée à `test_bordereau_du_code_ecrit_puis_verifie` ne les prouve pas, car le refus y vient déjà du contrôle d'empreinte du fichier cité (même code `5`, message non vérifié). Sans effet sur la conformité du code ; trou d'essai mineur. |
| 12 | chemin de la table neuve non épinglé | **porté** | `Pieces.table_neuve` ; `lire_la_table` refuse (20) un bordereau qui cite la table ailleurs, `ecrire_bordereau_du_code` aussi ; valeur égale au chemin de M-4 et à celui du dépôt (vérifié). Essai `test_chemin_de_la_table_neuve_epingle` (refus, puis cas sain). Mutant « épinglage retiré » : **tué**. La notice v7 (étape 5, ligne `[20]`) le dit. |

Les remarques 8, 9, 13 à 17 : laissées ou portées à la session mère, comme la pièce de corrections le dit ; je n'ai rien à y reprendre (elles n'étaient pas des écarts de lettre).

## Rejeu des mutants survivants (copie de `src/` de mon bloc-notes, sur le code corrigé)

| mutant | avant | après |
|---|---|---|
| N3 rang de « postérieure » ignoré | survivait | tué |
| M4 O-2 non requis (et O-4, variante) | survivait | tués |
| N8 `<` en `<=` (rang honnête) | survivait | tué |
| N9 ex aequo à 0 (aire intra-tâche) | survivait | tué |
| N11 seuil du marquage 0,99 (et 0,01) | survivait | tués |
| N20 dernier état en `argmin` | survivait | tué |
| P1 verdict déclaré D-15 non comparé | survivait | tué |

Les sept sont tués. (N23 et P15 étaient équivalents ou sans effet observable : non rejoués.) Les mutants nouveaux sur les corrections : 11 sur 12 tués (le douzième : constat 11, écriture).

## Rien d'autre n'est cassé

- Les 145 essais d'avant passent encore (150 au total) ; la vraie table neuve passe la nouvelle structure des rôles ; le chemin épinglé est celui du dépôt ; les comptes `actions_sans_rang_honnete_cascade` et les parts d'alertes sur les lignes de différence sont des champs ajoutés, sans effet sur un état, un déclencheur ni le verdict (bloc `descriptif_additif_1` seulement ; l'essai de la sortie décisive identique à l'octet passe).
- Le diff de `src/` ne contient pas d'autre changement que ceux de la pièce de corrections (je l'ai lu en entier : 23 lignes pour la lecture, 16 pour les lectures descriptives).
- La notice v7 dit les trois changements (rapport v5 « scellé ou brouillon 1 », chemin de M-4, structure des rôles (s1) à (s8) en `[20]`) ; pas d'autre phrase changée.

## Verdict

**Conforme.** Sept constats mineurs et trois remarques portées (une, la 11, en partie : côté écriture et valeur du second empreinte sans essai propre, non bloquant) ; aucun défaut neuf.
