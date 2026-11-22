# Contre-lecture de l'essaim v4 (classe B) — rendu v1

Objet : `collisionneur_v9_essaim_v4.py` (sha256 9ae76a54a1ca89f0…), essais v4 (590182258ab0299e…), configuration pilote v4 (c9c233b1fa4cc191…). Aucun appel, aucune clé, rien écrit dans le dépôt.

## Verdict : à corriger (un bloquant)

Les points (a), (b) et (c) tiennent. Le point (1) tient pour la réserve des finales, qui lit la longueur réelle du brouillon écrit. Il ne tient pas en entier pour le devis.

## Bloquant

1. **Borne d'un brouillon pas encore écrit : le plafond de relance est oublié** (`borne_brouillon`, ligne 921). La borne prend `MODELES[l]["max"] × CAR_SORTIE_MAX`. Mais un brouillon valide peut sortir de l'essai de relance, plafonné à `max_relance` (plan de `executer_cellule` dans le moteur v8d, ligne 1965). Astra : `max` vaut 8 000 et `max_relance` 32 000, donc la borne est de 36 000 caractères au lieu de 144 000. Fable : 147 000 au lieu de 192 000. Le devis compte donc encore moins que le pire réel, et l'écart fait passer le pilote à 3 cycles au-dessus du plafond dur (voir le devis plus bas).
   Correction proposée : `sortie = max(max(v.MODELES[l]["max"], v.MODELES[l]["max_relance"]) * v.CAR_SORTIE_MAX[...] for l in lettres)`. Ajouter un essai avec un brouillon d'Astra plus long que 36 000 caractères, qui doit tenir sous la borne du devis. Cette correction est faite dans une copie du bloc-notes : les 48 essais passent.

## Non-bloquants

- La garde « origine finie » d'un rejeu (ligne 1031, `etage3_fini(v, origine)`) fait double emploi : l'origine est déjà contrôlée parce qu'elle figure dans la liste. La mutation M-c5 n'est pas prise, et elle ne peut pas l'être.
- Le refus d'une balise dans `verifier` (ligne 1404) n'a aucun essai : la mutation P5 n'est pas prise. Ajouter un essai qui altère un texte publié.
- Le comptage des mots par `split()` ne borne pas les caractères des textes publiés. La borne de 7 caractères par mot (salons, prépublications, revues) n'est appliquée nulle part. C'est un défaut de même nature que celui du brouillon, en plus petit. Le plafond reste tenu sur l'entrée comptée.
- La v4 (programme, essais, configuration) n'a ni compagnons `.sha256` (R6) ni rapport de développeur v4.

## Corrections antérieures : elles tiennent

Le passage de v3 à v4 ne touche aucune de ces parties. Le motif des lettres de proposition reste insensible à la casse sur le mot seul et exige une capitale de A à E : « cette proposition a » n'est pas attrapé. Les noms de modèle sont gardés. Les balises `<<<`/`>>>`, y compris leurs formes NFKC, sont refusées à la publication, à l'injection et dans `verifier`. Le refus de `--faits` différent de `--question` est en place. Tout appel passe par `executer_cellule` de la v8d avec `--plafond-usd` (ligne 812), et aucun autre chemin réseau n'existe.

## Essais et mutations

48 essais passés sur la v4. Chaque mutation est une copie du programme dans le bloc-notes, lancée par `ESSAIM_MODULE` (`mutations.txt`). Mutations prises :

| Mutation | Point | Essai qui la prend |
|---|---|---|
| M1, borne de la v3 | (1) | `test_borne_du_brouillon_long` |
| M1b, brouillon écrit ignoré | (1) | `test_reserve_compte_le_brouillon_ecrit` |
| M1c, longueur écrite à zéro | (1) | `test_reserve_compte_le_brouillon_ecrit` |
| Ma, cellule reprise exclue | (a) | `test_reserve_verifiee_a_la_reprise_et_sous_la_ligne` |
| Mb, ligne ignorée | (b) | `test_reserve_verifiee_a_la_reprise_et_sous_la_ligne` |
| Mc1, empreinte ignorée | (c) | `test_isoles_avec_empreintes_et_etats` |
| Mc2, étage III ignoré | (c) | `test_enveloppe_par_modele` |
| Mc3, rejeu admis dans `enveloppe` | (c) | `test_isoles_avec_empreintes_et_etats` |
| Mc4, rejeu sans origine | (c) | `test_isoles_avec_empreintes_et_etats` |
| Mc6, `simuler` sans `--isoles` | (c) | `test_isoles_avec_empreintes_et_etats` |
| P1, lettre de proposition insensible à la casse | anonymat | `test_motif_proposition_sensible_a_la_lettre` |
| P2, motif de proposition retiré | anonymat | `test_noms_de_modele_signales_ou_refuses` |
| P3, sans NFKC | faux bloc | `test_chevrons_normalises_refuses` |
| P4, `--faits` différent de `--question` | faits | `test_faits_differents_de_la_question_refuses` |

Non prises : Mc5 (redondante) et P5 (sans essai).

## Devis du pilote (`devis`, question générale v2, sans réseau)

| | 3 cycles, v4 | 3 cycles, v4 corrigée (relance) | 4 cycles, v4 | 4 cycles, v4 corrigée (relance) |
|---|---|---|---|---|
| Pire sans relance | 62,30 | **65,39** | 79,67 | 83,54 |
| Pire avec relances | 161,78 | 167,96 | 205,29 | 213,02 |
| Finales seules, sans relance | 12,78 | 13,56 | 13,32 | 14,10 |
| Finales seules, avec relances | 33,20 | 34,74 | 34,41 | 35,96 |

Rappel de la v3 : 53,87 USD à 3 cycles et 69,14 USD à 4 cycles.

Comparaison au plafond dur de 64 USD :

- La v4 telle quelle passe sous 64 USD à 3 cycles sans relance, de 1,70 USD seulement.
- Une fois le bloquant corrigé, le pire sans relance dépasse 64 USD à 3 cycles comme à 4 cycles.
- Avec relances, le pire dépasse largement 64 USD dans tous les cas.

Le plafond dur reste tenu appel par appel, mais le pire complet ne tient sous 64 USD dans aucun cas.

## Simulation (`simuler`, coût attendu, références simulées)

| | 3 cycles | 4 cycles |
|---|---|---|
| Coût prévu total | 22,30 USD | 27,50 USD |
| Dont finales | 5,13 USD | 5,35 USD |
| Taux de tours sautés | 0 % | 20 % |

Aucun nombre de cycles ne « tient » : chaque modèle dépasse sa référence de 1,16 à 1,86 fois.

## Dossiers lus par `simuler`

Les sept dossiers dont l'étage III est fini, sans les rejeux d'Argon (marqués « non fini » par le programme), avec l'empreinte de leur `journal.jsonl` :

- `runs/collisionneur-anteriorite-pilier-v1-20261121-131029` : c2fae5127140e8d16b890d2e5ff0ee7fec91ece92f1f81e1055f7355cda1a2aa
- `runs/collisionneur-derive-de-regime-v2-20261121-131044` : 925043c94d95dd0284ca49bc411d66e2eeb73e30558c0c739712ee793a5962ad
- `runs/collisionneur-methodes-maths-v1-20261121-093850` : d779015eee3aeb1a82df2294c3f1bf05eb77d8015ed310e1c9f97ba5a1b27606
- `runs/collisionneur-percee-controle-securite-v1-20261121-114810` : 9f6d689380d224e053659ba75212000366327197b7ad96204f8f6294ee43a5c2
- `runs/collisionneur-protocole-x-coercition-v1-20261122-061053` : 0c6df11deea5453309ffe90701aae73701ca9eadd1bfdd2ba5662ac45f80d3fa
- `runs/collisionneur-question-de-recherche-fusionnee-v1-20261121-153256` : 22216d3f6c5e149c5f3847c8ccd07287786c282306be58bc4484cd397fbb04b8
- `runs/collisionneur-seuil-moniteurs-v1-20261121-063125` : 7b1cb98f8ec6c70d71905e33cd77302f86f3ed5babe38b52667568a170afdda3

Exclus parce que non finis : dopamine-v1-20261120-122457 et protocole-x-problematique-papier-v1-20261122-061053.
