# Rapport du rédacteur — addendum 1 au préenregistrement scellé de la ligne 1, version 3 (erratum) — v1

Auteur : rédacteur neuf, modèle F. Date (`date -u`) : 2026-11-19, 22:10. Pièce de travail (classe C). Rien lancé, aucun résultat lu, aucune graine dérivée, rien écrit dans le dépôt, aucun commit, aucune poussée, aucun appel de modèle, aucune dépense. Aucun refus d'outil. Rien touché sous `archives-reponses-modeles/`.

Mandat : `mandat-redacteur-addendum-ligne-1-v3-v1.md`, `ccd4b3648e2f5b48debb9ae5b501ea88736476442dcb4c4ac25766805c3abc2d`, empreinte vérifiée avant de commencer (branche `lot/compte-organisme-v1`, commit `53ec6e1a8d1bbab034dc77c90926debc6fd21f02`). Un mot du coordinateur reçu en cours de travail : deux ajouts de la mère, hors des quatre corrections (voir plus bas).

## Verdict

La version 3 est écrite, non scellée : les quatre corrections de la vérification `b0c09a4f…` sont appliquées à la lettre, par programme, chaque texte ancien trouvé une seule fois ; les textes neufs sont extraits par ce programme de la section 6 de la vérification, non recopiés à la main. Deux ajouts de la mère s'y trouvent en plus, conditionnés à l'option A de la décision 4 : le vérificateur ne les a pas vus, et l'un des deux porte une réserve de ma part.

## Fichiers rendus (bloc-notes `redacteur-addendum-ligne-1-v3/`)

| fichier | sha256 |
|---|---|
| `addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v3.md` | `fb48a8ab9aeee1667c46a3d72dbf97d39343ecfb10227c652074d38f46ba55d5` |
| `differentiel-addendum-1-ligne-1-v2-v3.diff` (`diff -u` de la version 2 du dépôt vers la version 3) | `8c42ccc88910048cd666e98474ea61224eb17779a15f514be6561b779f7b3740` |
| `appliquer_corrections_v3.py` (programme de remplacement) | `9d26722ae7ca1e70d5a90f468a28515e8d242baa72b134a4985379508396de71` |

Empreintes vérifiées avant de citer : version 2 `b5d76973…` (intacte), son rapport `999d6446…`, son mandat `fa449b92…`, vérification `b0c09a4f…`, attestations `7565e0ba…` et `56d7e2f6…` (commit `6f0957a7…`).

## Les quatre corrections

1. § 5.4, table : les deux lignes d'en-tête en double retirées ; les deux « À PORTER par la mère » remplacés par les deux textes exacts (attestation du développeur, avec la limite des 18 passes de mutation ; attestation du vérificateur).
2. § 5.4, « État de ces conditions », dernière puce : remplacée par le texte exact ((iii) et (v) tenues, sources, limite des 18 passes).
3. § 6 : texte exact ajouté après « L'étalonnage ne part pas avant le scellement de cet addendum. ».
4. § 7, réserve 6 : fin remplacée par le texte exact (programme de l'audit de symétrie avant le lancement de la course décisive, empreinte dans le mot de Lazar).

## Deux ajouts de la mère, hors des quatre corrections

Reçus du coordinateur, décidés par la mère vers 22:04Z, écrits comme valables seulement si Lazar choisit l'option A de la décision 4, et comme tombant sous l'option B :
- § 9, point 8 : versement de l'étalonnage pendant la course décisive (copie du dossier scellé, sous-commande `empaqueter` du lanceur v2 sur la copie, poussée ; aucun fichier ouvert ; code inchangé ; commit, noms, tailles, empreintes notés).
- § 6, après le paragraphe sur la garde A14 : configuration v3 (la v2 plus un seul champ, l'heure du scellement de l'addendum), empreinte au registre avant le départ, vérification par le même contre-lecteur du code, cas sain et artefact de A14 rejoués ; repli écrit (lecture du journal du lanceur après la chaîne).

**Réserve sur le second ajout.** D'après ma lecture du code v2, le lanceur lit le fichier nommé `configuration_ligne1_v2.json` (chemin fixe, `CHEMIN_CONFIGURATION`), compare les dérivations au seul champ `preenregistrement.horodatage_scellement`, et ne lit aucune ligne de registre. Une configuration v3 d'un nom neuf (R12) avec un champ neuf ne serait donc ni lue ni employée par le code v2 sans un changement de code, et « le lanceur la vérifie contre cette ligne » n'existe pas dans le code. Changer la valeur de `horodatage_scellement` plutôt qu'ajouter un champ ferait mentir ce champ sur le préenregistrement. J'ai écrit l'ajout tel que transmis, avec une phrase de limite de ma main qui le dit et qui fait valoir le repli tant que la vérification de la v3 n'est pas rendue « conforme ». C'est à la mère de dire si un code v3 est nécessaire ; si oui, c'est un changement du code visé par l'addendum (§ 5.1), donc plus qu'un erratum.

**Conséquence pour la vérification.** Le vérificateur acceptait un simple contrôle du différentiel pour les quatre corrections seulement. Les deux ajouts sont de la matière neuve : ils sont à lire pour eux-mêmes. Je l'ai écrit dans l'addendum (§ 8 et § 11).

## Tenue de version, déclarée

Titre (« v3 ») ; phrase de statut ; ligne de l'auteur (mandat v3 cité, deux rédacteurs du même modèle distingués) ; heure ; ligne « Vérification de la version 2 » en tête ; au § 8, « Cette version 2 » devenu « La version 2 », la vérification portée dans la table, une ligne « À PORTER » pour le contrôle du différentiel ; un § 11 neuf (différentiel version 2 → version 3, pièces lues). Tout le reste est identique au caractère près (voir le différentiel).

## Écarts et points à connaître

1. Le § 11 et la phrase de limite du § 6 sont de ma main, hors des textes exacts ; je les tiens pour de la tenue et de la prudence, mais ils sont à contrôler.
2. La condition de GO-2026-11-19-81, recopiée telle quelle en tête, dit « l'addendum v2 scellé » : c'est la version 3 qui serait scellée. À la mère de dire si la lettre du GO couvre l'erratum ou s'il faut un mot.
3. Non retouché, parce que hors des quatre corrections : au § 5.4, « Préalable (mandat de cette version) » et « État de ces conditions à l'écriture » parlent de la version 2 ; au § 7, réserve 4, « pendant l'écriture de cette version » aussi ; le § 1 décrit les lectures du rédacteur de la version 2 à son commit. Le § 11 le dit.
4. Restent « À PORTER » : chemin, empreinte, commit et heure du scellement (§ 6) ; contrôle du différentiel (§ 8).
5. Le rapport du rédacteur v2 (« Trouvé en chemin », point 1) reste dépassé sur les attestations, comme la vérification le note.
6. Pour la limite du § 6, j'ai lu en partie `code/lancer_ligne1_v2.py`, une ligne de `code/etalonnage_ligne1_v2.py` et les noms des champs de la configuration v2 : lecture seule, rien exécuté du banc.
