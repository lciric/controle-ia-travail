# Pièce qui scelle le manifeste d'ouverture du rejeu du juge de sélection (critères v7) — v1

Écrite et scellée par la session mère (`session_01XJ6Mgr8BN6UanALsQatc5E`) le 2026-11-20T06:13:34Z (`date -u`), à partir du brouillon du contre-lecteur des critères (`9499d832…`, commit 40ad4636 de `lot/compte-organisme-v1`), qu'elle a relu en entier. Les trois fichiers sont copiés à l'octet dans `prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/`.

**Contrôles rejoués par la mère avant le scellement** : `valider_manifeste` (programme d'assemblage `2f5640da…`) passe, et les seize clés égalent `CLES_MANIFESTE` ; `valider_configuration` du masque (`07ed8725…`) et du lecteur par programme (`de99117b…`) passent ; les deux identifiants X6 égalent, par programme, la clé `extraction.identifiants_par_classe.a_corriger` de la sortie `f5c7cc1c…` ; les heures de R-4097, R-4102 et R-4128 sont exactes.

**Écarts du brouillon, tranchés par la mère.**
1. Les dix `champs` de la configuration A sont égaux, dans l'ordre, à la clé `champs_fiche` de la configuration de la course v9 elle-même (`runs/20261119-094145-course-auto-conception-v9/configuration-orchestrateur.json`, `lot/compte-organisme-v1`), vérifié par programme. L'écart de source est levé.
2. `formules` = « non vérifié » seul : la consigne du proposeur v2 (`a7c34a7a…`) n'impose que cette formule (l. 32, règle 6). « prédit » n'y décrit que le champ `cout` (l. 59), sans être une formule imposée. Valeur gardée, conforme au rapport v7, § 5 (« au moins « non vérifié » »).
3. `intertitres` = `[]` : le format de la réponse n'impose que des champs. Valeur gardée.
4. « La réserve du § 4 » visée par la mère est celle du message de l'organisme du 2026-11-20 vers 05:23Z, § 4 : les lecteurs liront dans les critères le signal par famille du rejeu v2, et pourraient se corriger d'eux-mêmes dans l'autre sens. C'est l'amorçage par le signal du rejeu v2, écrit au point 6 ci-dessous ; il entre dans la proposition.
5. Les deux identifiants X6, recopiés dans le brouillon, sont contrôlés par programme (voir plus haut).

## 1. Les pièces scellées

| pièce | chemin | sha256 |
|---|---|---|
| manifeste | `prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/manifeste-rejeu-v1.json` | `a81d30d35c3dad56405e536b901218982b16e2b5f6f82b77b2d84581974d49dd` |
| configuration A du masque | `prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/configuration-a-masque-v1.json` | `8a8548d1444bfe3ab85396b3913c2d1b018a32541e9a283bd3f9b517a6332ce4` |
| configuration B du lecteur par programme | `prereg/organisme-auto-conception-v9/juge-selection/rejeu-v1/configuration-b-lecteur-v1.json` | `b44371d235292623e2c51fdd31a68bbabae5402774d5e99860b5a6b90ebdaa6a` |
| critères v7 scellés | `prereg/organisme-auto-conception-v9/juge-selection/criteres-choix-cartes-v9-v7.md` | `6af793a27f6bce4b5fe05aa18b5c6c33aed8d10a284d081fd24a0640434a316f` |
| note v7 scellée | même dossier | `bbd71b7c998866ec249556fe7803015c54aac4081dffc4e5084588819bc98a26` |
| programme d'assemblage | `juge-selection/criteres-v5/assemblage_selection_v4_v2.py` | `2f5640daaeae042d16fb22486a5994a41f0eb26b6e9f190c7984a38bfa5afdf6` |
| masque | `juge-selection/criteres-v4/masque_style_cartes_v1.py` | `07ed87256ba6f2ca510dfd462733190566343ed09e485cb1b638e0314780823e` |
| lecteur par programme | `juge-selection/criteres-v5/lecteur_par_programme_cartes_v2.py` | `de99117bb125108ae94a65cc630af304a15c3ce00ebc3036b9c2eca8e969c204` |
| garde de `lignee_reconnue` | `docs/notes/organisme-auto-conception-v9-mere/juge-selection-manifeste-v1/garde_lignee_reconnue_v2.py` | `635e9160e0bf03cd70a25cd0532e638203c8bc621c502313e5f2491b4ba76585` |

## 2. Décision qui fixe les valeurs

**GO-2026-11-20-10, point O2** (`registres/go.md` sur `main`, ligne 541), mot pour mot :

> « Juge, critères v7 : en tête (1) et (3) ; décision 1 (a) ; 2 (a) ; 3 (b) au rejeu et (a) en course ; 4 (b) ; 5 (a) au rejeu ; huit confirmations telles qu'écrites. »

Mot de Lazar, vers 04:44Z : « O2 recos ».

## 3. Justification de chaque valeur (règle M1 : ici, non dans le manifeste)

| clé | valeur | justification |
|---|---|---|
| `identifiant_course` | `auto-conception-course-v9-2026-11-19-v1` | critères § 9, point 1 (« à défaut, le nom du dossier d'archive ») ; nom pris dans la statistique de famille, § 2, point 1, sans ouvrir le dossier. Il fixe tous les tirages : il ne change plus après ce scellement |
| `usage` | `rejeu` | O2, décision 1 (a) |
| `ligne_accord` | `GO-2026-11-20-10` | O2 ; le programme ne la lit que pour l'usage « course » |
| `criteres_sha256` | `6af793a2…` | critères v7 scellés |
| `nombre_vise` | `9` | critères § 6 (à défaut de charge connue) ; confirmation 6, telle qu'écrite |
| `veto_par_titulaire` | `selon_titulaires` | O2, décision 2 (a) : trois cartes à trois titulaires au plus |
| `suppleantes` | `6` | O2, décision 2 (a) ; critères § 8 |
| `filtre_veto` | `famille` | O2, décision 2 (a) |
| `plafond_veto` | `nombre_vise` | O2, décision 2 (a) ; consigne R-3876 |
| `regime_items` | `ajoutables_oui` | O2, décision 4 (b) ; orthographe de `REGIMES` dans le programme |
| `seuil_accord` | `0.75` | confirmation 5, telle qu'écrite |
| `lignee_reconnue_declaree` | `true` | O2, décision 3 (b), au rejeu |
| `emploie_lectures_v2` | `false` | critères, annexe B : lectures neuves |
| `familles` | `prop-opus` et `prop-fable` dans la même famille ; `prop-argon`, `prop-astra` et `prop-carbon` chacun dans la sienne | critères, annexe B, l. 373. Étiquettes de la configuration de la course v9, clé `proposeurs` (réponses `35cc9bcf…`). Les noms de familles sont libres, seule l'égalité compte |
| `hors_choix` | `[]` | voir le point 4 |
| `cartes_attendues` | `94` | voir le point 4 |

**Configuration A du masque.**
- `champs` : les dix champs de la consigne du proposeur v2 (`course-v2/consigne-proposeur-auto-conception-v2.md`, `a7c34a7a…`, l. 43-44 et 50-61), dans leur ordre : `titre`, `axe`, `module_change`, `mecanisme`, `plus_proche_voisin`, `ce_qui_distingue`, `epreuve_monde_plante`, `cout`, `ce_qui_la_refuterait`, `limites`.
- `plafond` : `mediane` (décision 5 (a), au rejeu).
- `formules` : `non vérifié`. La consigne l'impose (règle 6) et les critères le nomment en annexe B.
- `intertitres` : `[]`. La consigne n'impose aucun intertitre.
- `seuil_formule_recitee` 0,2 et `minimum_formule_recitee` 3 (confirmation 8).
- `hors_choix` : `[]`.

**Configuration B du lecteur par programme.**
- `champ_refutation` : `ce_qui_la_refuterait`.
- `champs_voie` : `titre`, puis `mecanisme`.
- `hors_choix` : `[]`.

Les trois champs de B figurent dans A.

**Contrôles par les programmes qui liront ces fichiers.**
- `valider_manifeste` passe. Les seize clés sont égales à `CLES_MANIFESTE`.
- `valider_configuration` du masque et `valider_configuration` du lecteur passent.
- Sortie : `sortie-valider-manifeste-v1.txt`.

## 4. Le cas X6

- **Règle**, R-4097 (2026-11-20T05:19:29Z) : seule une fiche `niveau_methode` reçoit un passeport ; les autres vont au journal sous « retenues », sans contenu. X6 désigne les deux fiches de ce journal, toutes deux `a_corriger`.
- **Complément**, R-4102 (05:30:14Z) : le journal a été écrit par l'aiguilleur v54. Une fiche non lancée n'a ni passeport ni place au journal.
- **Vérification close**, R-4128 (06:05:00Z) : `fiches.json` (`ba65c411…`) porte 94 clés, et aucune des deux retenues n'y est. L'extraction est `f5c7cc1c…`.
- **Les deux identifiants X6** : `f640bf1e40418` et `f9a7c8311d714`. Ils sont tirés par programme de la seule clé `extraction.identifiants_par_classe.a_corriger` de `sortie-extraction-x6-v2.json`.
- **D'où** `hors_choix` = `[]` partout : le masque refuse un identifiant absent du fichier (l. 110-112). Et `cartes_attendues` = 94. Les deux cartes X6 sont hors du choix par construction : elles n'ont pas de passeport et ne sont pas dans le fichier.

## 5. La garde de `lignee_reconnue`

La garde `garde_lignee_reconnue_v2.py` (`635e9160…`) est jouée sur chaque lecture déposée, **avant `assembler`**. Elle refuse toute valeur qui n'est ni une clé de `familles` de ce manifeste, ni « aucune », dans les cartes comme dans le veto. Une lecture refusée est à refaire.

## 6. Réserves de la table (`a41a2c7c…`), au vu de R-4128

1. **`hors_choix` et les 94 cartes : levée.** Les deux cartes X6 sont hors du fichier (R-4128). Le rejeu porte sur ses 94 cartes.
2. **Les étiquettes `prop-…` : levée quant à la source.** Elles viennent de la configuration de la course v9. Leur égalité avec `meta` → `proposeur` n'est pas vue sur le fichier, mais elle est contrôlée par refus, sans repli silencieux : l'assemblage et la statistique de famille refusent une étiquette hors de leur table.
3. **`identifiant_course` fixe tous les tirages : ouverte, comme règle.** Il est scellé ici et ne se refait pas après une lecture.
4. **La graphie de `lignee_reconnue` (« Gestes », point 3) : levée** par la garde v2, à condition qu'elle soit jouée sur chaque lecture avant `assembler`.

Restent ouverts aussi, hors de la table :
- l'amorçage par le signal du rejeu v2, que lisent les lecteurs dans les critères (K3 le leur dit) ;
- l'amorçage que la décision 3 (b) accepte.

Tous deux sont à porter dans la proposition.

## 7. Ordre des gestes (critères, annexe C)

1. Scellement de ce manifeste, de A et de B.
2. Le masque.
3. Le lecteur par programme, deux fois : `fiches`, puis `masque`.
4. Les deux lecteurs, sur la consigne v3 (`85efbd70…`).
5. La garde, sur chaque lecture.
6. La table des espèces, par programme.
7. `assembler`.
8. `gardes`, avec les deux sorties du lecteur par programme.
9. La statistique de famille scellée, avec sa correspondance.
10. La proposition, puis sa contre-lecture.

*Scellé par la mère.*
