# Contrôle du différentiel — ligne 3 des épreuves v9, préenregistrement et devis version 7 (erratum), sur les quatre corrections de la vérification de la version 6 — v1

- **Contrôleur** : l'agent du modèle O qui a écrit la vérification de la version 6 (`verification-ligne-3-v6-v1.md`, `cbaf44de72b3dff7bd133be33a288a6a171776e72b94fc194f866faa05e8f9c1`) ; je n'ai écrit aucune version du texte ni du devis (règle R2 ; règle de l'allègement : vérification des corrections par le même contre-lecteur).
- **Mandat** : reprise sur GO-2026-11-19-84 (main, commit `45653e962…`, ligne relue : « Les travaux arrêtés reprennent. Aucune dépense. »).
- **Heure** (`date -u`) : 2026-11-19T22:46:58Z (relevée en cours de travail). Processeur seul ; aucun appel de modèle, aucune dépense ; réseau : `git fetch origin lot/compte-organisme-v1 main` et des `git show`. Aucune écriture dans le dépôt : les pièces sont tirées du commit `5e51b0b15bad4d62c296a392618279ae257547b5` par `git show` vers mon bloc-notes ; l'arbre de travail n'est pas touché.
- **Aucune commande sur un chemin sous `archives-reponses-modeles/`** ; aucune carte ouverte. Aucun outil n'a refusé.

## 1. Empreintes (recalculées sur le contenu au commit `5e51b0b1`, égales à leur compagnon et aux préfixes donnés)

| pièce | empreinte |
|---|---|
| préenregistrement v7 | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` |
| `differentiel-preenregistrement-ligne-3-v6-v7.diff` | `ef9ab82fb6a245306dd41978931729aa1b60ebcbc1537bd8c77a3873ff12791a` |
| devis v7 | `382ea448db3ba8f5d69df1f3566165d1028ad8aceddfc8c538c522b838f58270` |
| `differentiel-devis-ligne-3-v6-v7.diff` | `4861ef69a171fc92b64841f3055ab736c16afd9e5d3760a25dc0730d2fef3a61` |
| `rapport-redacteur-ligne-3-v7-v1.md` | `b5c3bcd5b3b39d1ff356c651eff8139ab8b5909ca91860bfafd154739ce64a4e` |
| `appliquer_corrections_ligne_3_v7.py` | `fc2fb615d3b3db71e0cd3366e1a7a5f2451c986463119b4ad807d83ca11c2c8d` |
| `tenue_version_ligne_3_v7.py` | `405884433557a5f4a74bd9fb9ed0ddc455cb5192aefbe5508aeee7bfde398571` |
| `mandat-redacteur-ligne-3-v7-v1.md` | `70568050074f1ec4fc0be614317452b6d0bd8b7cdc815b6949e65c45c57234da` |
| références : préenregistrement v6 / devis v6 (même commit) | `b040d24c…` / `34e87d90…`, inchangés |

## 2. Différentiels versés

Recalculés par moi (`diff -U0` sur les fichiers v6 et v7 du commit) : **égaux à l'octet** aux deux fichiers versés (hors les deux lignes d'en-tête de nom). Préenregistrement : 12 morceaux ; devis : 4 morceaux, comme le rapport le dit.

## 3. Les quatre corrections, à la lettre

Contrôle par programme (`lettre_v7.py`, dans mon bloc-notes) : les textes anciens et neufs sont tirés du § 10 de ma vérification, sans recopie ; chacun est compté dans la v6 et la v7.

| correction | remplacement | ancien en v6 | neuf en v6 | neuf en v7 | ancien en v7 |
|---|---|---|---|---|---|
| 1 | (3), liste fermée entière | 1 | 0 | 1 | 0 |
| 1 | annexe A, « … et au rapport de la garde), » | 1 | 0 | 1 | 0 |
| 2 | ajout en fin de puce « Repli », après « et d'ici là la garde ne tourne pas. » | — | 0 | 1 (ancre + texte, contigus) | — |
| 3 | (5), journal créé vide ; absent ou illisible | 1 | 0 | 1 | 1, contenu dans le neuf (le neuf prolonge l'ancien) |
| 3 | liste d'arrêt, artefact « journal des rejeux absent ou illisible » | 1 | 0 | 1 | 1, contenu dans le neuf |
| 4 | en-tête, provenance (R-3917, R-3934, commit, empreinte) | 1 | 0 | 1 | 0 |
| 4 | (4), « selon le mandat de la version 6, point 2, condition (4) » | 1 | 0 | 1 | 0 |

Sept remplacements, tous à la lettre et à leur place, sans écart ; c'est le compte du rapport (« 7 remplacements de correction »). La lecture mot à mot du différentiel ne montre, dans ces morceaux, rien d'autre que ces textes.

## 4. Tenue de version déclarée

Les 12 morceaux du préenregistrement correspondent aux 18 lignes de la table « Différentiel avec la version 6 » : titre ; statut (version 6 mise au passé, vérification de la version 7 « sur lui seul ») ; auteur et date ; mandats (« la version 6 », correction 4, puce du mandat v7) ; documents (vérification v6 citée comme faite, `registres/decisions.md` relu) ; empreintes recalculées, devis v7, « non lus » ; garde (3), (4), (5), repli (corrections et « vérificateurs des versions 6 et 7 ») ; ordre des gestes (1) ; liste d'arrêt ; « Contre-lecture » (vérification v6 faite, table des quatre corrections, tenue nommée, version 7 à vérifier, demande de la version 6 gardée pour mémoire) ; annexe A ; différentiel. Le résumé de ma vérification à « Contre-lecture » est fidèle (24 et 16 morceaux, corrections, écart jugé juste, rejeu à l'octet, empreinte des cartes non vérifiée, devis v6 propre). **Rien d'autre ne change** : aucun montant, appel, hypothèse, seuil, critère ni règle de lecture.

## 5. Devis v7

Trois lignes changent sur 263 (titre ; statut ; § 7, point 1), plus la section « Différentiel avec la version 6 ». Comptage par programme (`chiffres_devis.py`) des nombres hors empreintes, hors section de différentiel : seuls changent des numéros de version et de nom de fichier (« 7 » ajouté, « v6 » cité comme remplacé) ; **aucun montant, aucun nombre d'appels, aucun plafond ne change** (16,52 ; 22,49 ; 44,38 USD intacts). Le statut cite le devis v6 par son empreinte juste et ma vérification par la sienne. Renvoi seul : conforme au mandat v7 et à la décision de la mère de garder le devis v7.

## 6. Observations, sans correction

- Le rapport nomme les deux outils `outils/appliquer_v7.py` et `outils/tenue_v7.py` ; ils sont versés sous d'autres noms (`appliquer_corrections_ligne_3_v7.py`, `tenue_version_ligne_3_v7.py`), avec les mêmes empreintes. L'outil d'application refuse tout dossier sous `archives-reponses-modeles/` ; je ne l'ai pas lancé.
- Le texte v7 dit « version 7 entre 22:35 et 22:38 » et le rapport « de 22:35 à 22:40 » : compatibles (texte fini, puis rapport).
- « Version 7, à vérifier. Par un agent neuf du modèle O » : le contrôle est fait par le vérificateur de la version 6, ce qui est la règle de l'allègement elle-même. La mère peut le noter au scellement ; aucun texte à changer.
- Le mot d'acceptation de la mère (vers 22:28Z) n'a pas d'autre source écrite que le rapport à la session ; le texte le dit tel quel.

## Verdict

**Scellable tel quel** (préenregistrement v7 et devis v7).
