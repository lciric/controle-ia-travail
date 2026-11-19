# Mot d'ouverture de la ligne 1 de l'organisme : les quatre objets, chemins et empreintes entières — v1

Pièce de travail (classe C) de la session mère `session_01XJ6Mgr8BN6UanALsQatc5E`, écrite le 19 novembre 2026 vers 23:45Z par programme : chaque empreinte est recalculée sur l'objet git ou sur le fichier de `main`, puis comparée au préfixe donné par la session de l'organisme. Elle sert le mot unique de Lazar prévu par `GO-2026-11-19-85` (décision 4, option A).

Branche de l'organisme : `lot/compte-organisme-v1`, tête `c41ca058e919f60d86f0be328798517af3602122` ; commit du code v2 : `14abb83052da2037ed39002716ecf97e2a99a6c4`. Préfixe des chemins de la branche : `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/`. Depuis le commit du code v2, aucun fichier de `code/` ni de `code-v2/` n'est modifié ni supprimé ; dix fichiers sont ajoutés (attestations, vérification, programme de l'audit et ses essais, avec leurs compagnons).

## 1. L'addendum 1 scellé et son erratum scellé (sur `main`)

| objet | chemin | sha256 | clé et heure du scellement |
|---|---|---|---|
| addendum 1 | `prereg/organisme-auto-conception-v9/addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v4.md` | `c29628a0dd209133545985cc334274462257314560c62c04259c5b31b1686e67` | `ADDENDUM-1-ORGANISME-V9-LIGNE-1`, 2026-11-19T22:25:03Z |
| erratum 1 v3 | `prereg/organisme-auto-conception-v9/erratum-1-addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v4-v3.md` | `ab98317d5e809d53eb5af88f17dd1f4e3683a16a1a21c699c9823538f84f1bd4` | `ERRATUM-1-ADDENDUM-1-ORGANISME-V9-LIGNE-1`, 2026-11-19T23:39:59Z |

## 2. Le code v2 et sa vérification (branche de l'organisme)

| objet | chemin sous le préfixe | sha256 |
|---|---|---|
| configuration v2 | `code/configuration_ligne1_v2.json` | `81f58ce5ca0a492ef231fa175303a21dfb21383a096fa71911b917923cc34f15` |
| commande de lancement v2 | `code-v2/commande-lancement-banc-a-ligne1-v2.md` | `f03dd49e051de8ea2fb1ca9861435b541cba8ffa801e005281553987f31a4298` |
| vérification des corrections du code v2 | `code-v2/verification-corrections-banc-a-ligne-1-v2-v1.md` | `6acbf7a6b04064993f82a639067158edf1d605b844be7fbbb5fd687e48297e5b` |

## 3. Les attestations sur les graines

| objet | chemin sous le préfixe | sha256 |
|---|---|---|
| attestation du développeur | `code-v2/attestation-graines-developpeur-banc-a-v2-v1.md` | `7565e0bae853fe5e30d447ae93d3a4b38c9a04466b13fd462a2ecc25d4377f15` |
| attestation du vérificateur | `code-v2/attestation-graines-verificateur-banc-a-v2-v1.md` | `56d7e2f6d52da254fee2998fa66f3c55c466ba0df1c713f64567a8fe8037e8e2` |

## 4. Le programme de l'audit de symétrie, contre-lu et inscrit

| objet | chemin sous le préfixe | sha256 |
|---|---|---|
| programme | `code/audit_symetrie_ligne1_v1.py` | `ca000bba3fe7399adecfcf5c93fd162dcf52524e4951683f3ecd93105047eef7` |
| essais | `code/essais/test_audit_symetrie_ligne1_v1.py` | `18031e62feae966a2eb6fd1788df1c481db156a803e4272e277736a1cf85c9f3` |
| contre-lecture | `code-audit-v1/contre-lecture-programme-audit-symetrie-ligne-1-v1-v1.md` | `037409baad6f6a685498aa5989807821558a5d3a866848e1ab732a95dd97c4ec` |

Inscription : clés `CODE-AUDIT-SYMETRIE-ORGANISME-V9-LIGNE-1` et `ESSAIS-AUDIT-SYMETRIE-ORGANISME-V9-LIGNE-1` de `registres/scellements-v1.md`, 2026-11-19T22:56:43Z.

## 5. Ce que le mot ouvre, et les rappels de la session de l'organisme

- Le mot ouvre la chaîne « étalonnage, puis course décisive », d'un trait ; les portes l'arrêtent seules.
- Lancement par la commande v2 ; journal en ajout.
- L'étalonnage est versé par copie, sans lecture, pendant la course décisive.
- Le contrôle de A14 se fait par le fichier d'état du lanceur, contre 2026-11-19T22:25:03Z (heure du scellement de l'addendum).
- L'audit de symétrie tourne sous le même Python (3.13) et le même numpy que l'étalonnage.
- Aucune dépense : la course tourne sur processeur, environ une heure sur quatre processus.
