# Collisionneur v9, mode essaim (v6) : rapport

Écrit à 2026-11-22T08:01:39Z (`date -u`). Classe B, Opus 5.5, session des collisionneurs. Aucun réseau, aucune clé, aucune course. Le pilote ne part qu'après le feu écrit de la mère.

- La v5 est vérifiée conforme par le même contre-lecteur (`verification-essaim-v5-opus-v1.md`) : bloquant de la v4 corrigé, passage au moteur v8e sans casse, 19 mutations prises.
- `collisionneur_v9_essaim_v6.py` (90274147…), copie de la v5 (f2593ce9…, intacte) par `fabriquer_essaim_v6_depuis_v5_v1.py` ; essais `test_collisionneur_v9_essaim_v6.py` : 55 passés ; configuration `configuration-pilote-essaim-v6.json` (`place_iii3` à null : refusée).

## Changements, et seulement ceux-là
1. Moteur **v8f** (445fe2d3…), vérifié conforme par son contre-lecteur (`../verification-corrections-collisionneur-v9-v8f-opus-v1.md`).
2. `verifier` lit sans erreur un journal plus ancien (clé `sha256_v8d`) et le dit « autre moteur » (non-bloquant 4).
3. Essais neufs, mutations E2 et E4 de la vérification désormais prises : configuration sans `place_iii3` refusée proprement (« clé place_iii3 absente ») ; empreinte du moteur contrôlée par `verifier` (deux cas).
4. Devis régénéré par la v6 (non-bloquant 2) : `devis-pilote-v6/`, chiffres identiques à la v5 : **48,78 / 65,40 / 83,54 USD** au pire sans relance à 2, 3 et 4 cycles (126,34 / 167,97 / 213,04 avec relances). Sous 64 USD : 2 cycles seulement.

Non porté : garde redondante de l'origine d'un rejeu (sans risque).

## Ouvert, pour Fable par la mère (inchangé)
`place_iii3` n'agit pas sur l'essaim : la finale ne garde que la ligne « Livrable », la même pour les deux places ; brouillons balisés, finales non. Appariement avec les jumeaux isolés de la v8d rompu. Incohérences de la consigne finale : `incoherences-consigne-finale-essaim-pour-fable-v1.md`.
