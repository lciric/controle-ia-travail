# Pièce de périmètre — ronde 1 élaguée de la boucle extérieure du pilote 4 — v1

Écrite avant le diff par le sous-agent neuf de la lignée conv-audit (analyste et correcteur de la ronde 1 élaguée), sur
le brief `BRIEF-ronde-1-elaguee-v1.md`. Objet : la v6.2.1 (« la Fusée »), commit `7ea32705c5437d91ed071dd95fb3209bb0b0035e`,
arbre `4f13647a7070b3941b660d60c428620df6b4e0e31cea1d2c63d71b8606e6214d`, 26 fichiers ; numéros de ligne au commit de
l'objet (identiques à `fournis/objet/`, empreintes vérifiées).

## Facteur

**F01 — nombre minimal de rondes avant la déclaration de fin** (`carte-facteurs-v2.json`, `facteurs[0]`), un seul
facteur, une seule entrée changée :

| entrée | fichier | fonction | lignes | colonnes | texte d'origine du segment | sha256 du segment |
|---|---|---|---|---|---|---|
| F01.3 | `principal.py` | `executer` | 2106 | 16–71 | `critere_qualite or critere_convergence or derniere_ronde` | `afbd1e24219df40130381ddfab202e6a321af0c4f485df768d734323bf0f92a2` (recalculé, égal à la carte) |

Forme du changement : celle du champ `regle_d_ajout` de F01.3 — le texte nouveau du segment est une conjonction (`and`)
dont un opérande est la disjonction d'origine, identique à l'arbre près, et l'autre une condition de ronde qui ne lit que
`r_idx` avec une constante entière : `(critere_qualite or critere_convergence or derniere_ronde) and r_idx >= 3`. Les
colonnes 1 à 15 (`            if `) et le deux-points final ne changent pas. F01.2 (l. 2104, `r_idx >= 2`) ne change pas.

## Fichiers d'accompagnement (liste close du protocole, § 6, point 2 ; carte, champ `accompagnement`)

- `principal.py` l. 27 (`VERSION`), avec `manifeste.json` l. 3 (version) et l. 5 (description, sans fait de course, sans
  fiche, sans verdict, sans score) : version 6.2.2.
- `CORRECTIONS-v6.md`, nouveau : le changement de code seulement (quoi, où).
- `tests/test_corrections_v6.py`, nouveau : cas sains et artefact (R5).
- Essai hérité adapté, parce que la correction l'exige : `tests/test_emprunts_v5_3.py`,
  `test_v5_3_phase_conception_ecrit_fin_conception_json` (l. 190–227, essai hérité de F01 dans la carte ; hors Z05 et
  Z13), l. 209–210 seulement (`ronde_conception` et `rondes_conception_max` du contexte). Raison : l'essai attend une
  déclaration de fin à la ronde 1 (`ronde_conception` 0, lu comme 1), que la correction retire par construction.

## Ce que le périmètre ne touche pas

Aucune ligne ni aucun segment de zone interdite (Z01 à Z14) ; aucun point hors boucle (PHB-1 à PHB-4) ; aucune autre
entrée de F01 ni d'un autre facteur ; aucune liaison nouvelle de nom (règle des noms N0, N1, N1b) ; aucune forme
interdite (N2) ; une lecture nouvelle de `r_idx` dans `executer` (NG-164 : `lecture_nouvelle_refusee` faux ; lecture
permise par `regle_d_ajout`). Aucun score, aucune valeur tirée des lectures, aucun identifiant de tâche, aucun critère ni
aucune stratégie de classement n'entre dans l'organisme.

Horodatage : écrit le 2026-10-26 17:11:17 UTC (heure lue sur `date -u` dans la commande qui écrit cette ligne), avant tout diff.
