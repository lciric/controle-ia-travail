# Table d'empreintes — planificateur du plan v5 de la course principale

SHA-256 recalculées par le planificateur, modèle F, le 2026-11-21. La table v4 (`3c1c7578d08225c05067e0da9335c4ebc1dd3e85063e7dc77d08fc203beda0ee`) vaut toujours pour ce qu'elle porte ; celle-ci n'ajoute que le neuf.

## Pièces rendues à la v5

| pièce | empreinte |
|---|---|
| `plan-experimentateur-tests-de-mort-course-principale-v5.md` | `ff18bacd1372dc5bb410ff739966b8a70d614bfffa14be73502a4e639a888a07` |
| `differentiel-plan-v4-v5.md` | `3b1d55f711c7c7529f3cedf5bacb00f4966cdfc023072735811fc142b2ff2c5c` |
| `rapport-planificateur-v5.md` | `8e903b01fabf31b32be8b3e4c02a89300c4ffd20ab5cd616707740da066ea560` |
| `calculs_plan_v5.py` | `2fffea8e837bf09f1ed9b9f42966f709bd5bc76997182a8242ef8504734a0db7` |
| `calculs-plan-v5-sortie.txt` | `415d5448f6348b23eef28272675442cd9cdb8a2b723ac4d64678c5deee286426` |
| `calculs-plan-v5-passe-2.txt` (seconde passe, égale à l'octet) | `415d5448f6348b23eef28272675442cd9cdb8a2b723ac4d64678c5deee286426` |

Cette table a son propre compagnon ; son empreinte est au message de remise.

## Pièces de la v4, inchangées

| pièce | empreinte |
|---|---|
| plan v4 | `ebb4cb47707e30929b535c8f65249f3f55abe831386e1fcaf5cf69cffcecc14f` |
| rapport v4 | `29e18ef8d436c9be67a3003f6b3452ecc4bb0b09472b1a31a2c45842f93b3512` |
| différentiel v3 → v4 | `d6440df2bed22f82b593d39905184610cc6733a241ac5204a77203eae01fd5dd` |
| `calculs_plan_v4.py` | `6560afffad364ef8b13e73bd41a1f284e1b373c494fec7e5d27fc124b290b962` |
| `calculs-plan-v4-sortie.txt` | `1f26453325d1733375d0a51d3bb128662a80cc30f54610c750ba3ee057e7a315` |

## Pièces neuves lues

| pièce | chemin | empreinte | lecture |
|---|---|---|---|
| vérification du plan v4 | disque de `/home/user/controle-ia-travail-organisme/`, `docs/notes/organisme-auto-conception-v1/plan-experimentateur-course-principale-v4/verification-v1/verification-plan-course-principale-v4-v1.md` | `804a6675ea350fbe30835e40f7d538be1f731240c159f01c887da33567f57dbb` | en entier |
| plan v1 | même disque, `docs/notes/organisme-auto-conception-v1/plan-experimentateur-course-principale-v1/plan-experimentateur-tests-de-mort-course-principale-v1.md` | `0bb27bc0a1f262daa41ad1f7746c34a2d423a90354e834d6f6874eee1f80d8e7` | lignes de lots et d'heures seulement (l. 128 à 137, 162 à 171, et les lignes qui portent « heures ») |

## Citée, non ouverte, empreinte non recalculée

| pièce | empreinte dite | source |
|---|---|---|
| configuration scellée des juges, `configuration-course-auto-conception-v5.json`, clé `champs_fiche` | `3f662ee80e12db7af79428c0bd2b0efe7e560a6a36c440c322343003fe2cc4f8` | relevé de la mère ; vérification du plan v4, « Pièces » et § 4.1 |

Exclu du versement : `lu-diff-v4-v5.txt`, le différentiel ligne à ligne des deux plans, fait pour contrôler que rien d'autre n'a changé.
