# Table d'empreintes — planificateur du plan v4 de la course principale

SHA-256 recalculées par le planificateur du plan v4, modèle F, le 2026-11-21. Les tables v1 à v3 valent toujours pour ce qu'elles portent ; celle-ci n'ajoute que le neuf.

## Pièces rendues à la v4

| pièce | empreinte |
|---|---|
| `plan-experimentateur-tests-de-mort-course-principale-v4.md` | `ebb4cb47707e30929b535c8f65249f3f55abe831386e1fcaf5cf69cffcecc14f` |
| `differentiel-plan-v3-v4.md` | `d6440df2bed22f82b593d39905184610cc6733a241ac5204a77203eae01fd5dd` |
| `rapport-planificateur-v4.md` | `29e18ef8d436c9be67a3003f6b3452ecc4bb0b09472b1a31a2c45842f93b3512` |
| `calculs_plan_v4.py` | `6560afffad364ef8b13e73bd41a1f284e1b373c494fec7e5d27fc124b290b962` |
| `calculs-plan-v4-sortie.txt` | `1f26453325d1733375d0a51d3bb128662a80cc30f54610c750ba3ee057e7a315` |
| `calculs-plan-v4-passe-2.txt` (seconde passe, égale à l'octet) | `1f26453325d1733375d0a51d3bb128662a80cc30f54610c750ba3ee057e7a315` |

Cette table a son propre compagnon ; son empreinte est au message de remise.

## Pièces qui font foi, lues

| pièce | chemin | empreinte | lecture |
|---|---|---|---|
| mandat | disque de `/home/user/controle-ia-travail-organisme/`, `docs/notes/organisme-auto-conception-v1/mandat-planificateur-plan-v4-course-principale-v1.md` | `1bf2d874d2c575dbdc62641a088d0abdea6d9ea3d3cc18f4cfebd0b51184234d`, égale à son compagnon | en entier |
| plan v3 | même disque, `docs/notes/organisme-auto-conception-v1/plan-experimentateur-course-principale-v3/plan-experimentateur-tests-de-mort-course-principale-v3.md` | `f6476c4f5a135f4d551d66958eb30d3a1319ae3bf230c64a08fbdef602599a69` | en entier |
| rapport v3 | même dossier, `rapport-planificateur-v3.md` | `6655e40dab7470ef2c87ac487212f6d3f44fc5a2300d1f298960b2dfebbbac8e` | en entier |
| table v3 | même dossier, `table-empreintes-planificateur-v3.md` | `fd0a1f6244933bb16954d3dfcdfb6358e59d3544fdfd4eeb7b2fc15b7259852c` | en entier |
| différentiel v2 → v3 | même dossier, `differentiel-plan-v2-v3.md` | `4e4bbfc7031ba9ab67f7591464bfab87fe3414af8b21fbd7c1778647198deb89` | en entier |
| contrôle du plan v3 | même dossier, `controle-v1/controle-plan-course-principale-v3-v1.md` | `864159fa8f0dd6d972d8c73bf6f0df4085a02d435c5dab0f2179c477ce16fdeb` | en entier |
| rapport du compte des cartes | même disque, `docs/notes/organisme-auto-conception-v1/compte-cartes-v9-v1/rapport-compte-cartes-v9-v1.md` | `9e410b09760bc2e29ec32eddf0c5bf52971176a0b914accc8c0c0d595d267c3b` | en entier |
| sortie du compte des cartes | même dossier, `compte-cartes-v9-depuis-main-v1.json` | `9515bae3527398bc61016444f00530d664a0085b80072632fd82baee33295e74` | en entier |
| note de conception | `origin/main`, `docs/notes/experimentateurs-et-tests-de-mort-v1/conception-branchement-experimentateurs-tests-de-mort-v1.md` ; copie `lu-note-conception.md` | `4f3ae86fe2ffa8c8abeeef95a2c574e723b731db11bb3b20d65d0ab534f11298` | en entier |
| erratum 1 de la note | `origin/main`, même dossier, `…-v1-erratum-1.md` ; copie `lu-erratum-1-note.md` | `0198f5f8dc6d12e34d0beaa6493e761211ef1d613c9306dc651b432afb8f44d7` | en entier |
| erratum 2 de la note | `origin/main`, commit `8b527dd57df107512e51ab2c4fbe1a55b476bb85`, même dossier, `…-v1-erratum-2.md` ; copie `lu-erratum-2-note.md` | `12c6034978e7475e007147df632327537b6a4a32c458ceef5e7d51b4aa3127de`, égale à son compagnon tiré du même commit | en entier |
| additif scellé de la v69, v4 | `origin/main`, `prereg/organisme-auto-conception-v9/orchestrateur-v69/additif-interrupteurs-orchestrateur-v69-v4.md` ; copie `lu-additif-v69-v4.md` ; même empreinte sur le disque, `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v69/` | `cb352811f0202aa530fa4fd94de1d7ed4e6a8d589584c06c24c915e3c73bb578` | en entier |
| `registres/go.md` | `origin/main`, commit `aea06e6383b1a5ebb6936170e8b29b5faaa83e16` ; copie `lecture-go-origin-main-v4.md` | `ec9baf4f0651c831c64cacef408027e179e96ea547133bb32de22be24f51be3d` | l. 488 à 492, 546, 559, 612 à 617 ; débuts des l. 618 à 621 |
| `registres/decisions.md` | même commit ; copie `lecture-registre-origin-main-v4.md` | `0d1f19d10e3f6c447166166a5c9098fb9b66a5ac88ef3df1bcfa35f1febd29ec` | l. 4269, 4560 à 4580 ; extraits des l. 4087 et 4291 |
| lecture descriptive de la course v9 | `origin/main`, `docs/notes/organisme-auto-conception-v1/course-v2/lecture-course-v9-v1.md` ; copie `lu-lecture-course-v9-v1.md` | `0306adf74d321cfa933e047adff28324092787f870a2bf97bafd9d52bd5ffddb` | l. 99 seule |

Les copies de lecture (`lu-…`, `lecture-…`) sont exclues du versement.

## Citées par d'autres pièces seulement, non ouvertes, empreinte non recalculée

| pièce | début d'empreinte | source |
|---|---|---|
| plans v1 et v2 | `0bb27bc0…`, `7cf3c78d…` | plan v3 |
| contre-lecture du plan v2 | `0b041dab…` | plan v3 |
| proposition des cartes à éprouver | `a2cd45ad…` | rapport du compte des cartes |
| configuration scellée de la course v9 | `3f662ee8…` | note de conception, § 1 |
| ordre de passage des épreuves v3 | `b19f550b…` | note de conception, § 1 |
| définition scellée de l'amélioration considérable | `4eae96bc…` | note de conception, § 2.2 |
| devis de l'héritage v5 | `30c87fa6…` | erratum 1, § 2 |
| relevé du lot 0 de NA-1 ; ordre v4 et mandat des mondes de « seuil et moniteurs » ; erratum 1 du plan du pilier | `10ac79ec…` ; `390af604…`, `6774507c…` ; `1827b680…` | registre |
