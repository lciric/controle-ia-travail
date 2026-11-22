# Vérification de l'essaim v6 : conforme

Objet : le programme essaim v6 (90274147…), sur le moteur v8f (445fe2d3…). Aucun bloquant. Les 55 essais passent.

## Points vérifiés

- **Moteur :** le programme pointe sur la v8f et son empreinte est contrôlée au chargement (mutation prise).
- **Journal ancien :** `verifier` le lit avec `.get` et le signale « autre moteur » au lieu de tomber sur une `KeyError`. Les deux cas sont prouvés : clé `sha256_v8d` et clé `sha256_moteur` fausse.
- **Devis :** le devis régénéré par la v6 est identique, octet pour octet, au contenu de `devis-pilote-v6/`, et les empreintes de ce dossier tiennent. Totaux, sur la configuration à place « fin » :

| Cycles | Pire sans relance | Pire avec relances |
|---|---|---|
| 2 | 48,78 USD | 126,34 USD |
| 3 | 65,40 USD | 167,97 USD |
| 4 | 83,54 USD | 213,04 USD |

## Mutations, toutes prises

| Mutation | Essai qui la prend |
|---|---|
| E2, clé `place_iii3` non exigée | `test_v6_configuration_sans_place_iii3_refusee` |
| E3, empreinte du moteur non contrôlée au chargement | `test_empreinte_v8d_controlee` |
| E4, contrôle du moteur retiré de `verifier` | `test_v6_verifier_controle_l_empreinte_du_moteur[champ0]` |
| E4b, `.get` remis en accès direct | `test_v6_verifier_controle_l_empreinte_du_moteur[champ1]` |

## À savoir

- Le non-bloquant de la v5 reste ouvert : `place_iii3` n'agit pas sur la consigne finale. C'est le point ouvert pour Fable.
- Le pire sans relance ne tient sous le plafond dur de 64 USD qu'à 2 cycles.
- `git status` montre un dossier non suivi qui ne vient pas de moi : `docs/notes/demandes-fable-api-2026-11-22-v1/`.
