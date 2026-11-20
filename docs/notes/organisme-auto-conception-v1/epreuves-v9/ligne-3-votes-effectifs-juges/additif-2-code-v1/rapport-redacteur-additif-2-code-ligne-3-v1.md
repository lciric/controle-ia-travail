# Rapport du rédacteur — additif 2 (additif de code) de la ligne 3 — v1

Pièce de travail (classe C). Écrite le 2026-11-20 (temps universel), sous le mandat `mandat-redacteur-additif-de-code-ligne-3-v1.md` (`65f9873ca725df1cdfb2aeb69807c66cfcfb613b80f987662efb0791361fdf38`, égale à son compagnon). Les deux fichiers rendus n'existent que dans le bloc-notes. Rien n'est écrit dans le dépôt, rien n'est committé.

## Verdict

L'additif de code est écrit : `additif-2-code-preenregistrement-ligne-3-votes-effectifs-juges-v7-v1.md`, `656094057c4ea3ebdd08049883531180be1f91572600b03d0a8738734ee330ae`. Il nomme le code et ne change aucun critère, seuil, prédiction ni racine. Il reste à le sceller, par la mère, avant tout calcul de l'étage 1, chronométrage compris.

- **Commit du code** : `380db35647746e2c1eae44a85d0f2969d19113b6` (branche `lot/compte-organisme-v1`).
- **Empreintes** : les 18 fichiers nommés du dossier du code sont recalculés sur disque et égaux au rapport du développeur ; les 17 qui sont dans le commit du code ont, sur disque, le même identifiant git que dans le commit.
- **Racine décisive** : 2026111932, avec 2026111933 pour le rééchantillonnage ; 2026111931 pour le chronométrage.

## Sources, empreintes recalculées

| pièce | sha256 | contrôle |
|---|---|---|
| mandat | `65f9873c…1fdf38` | `sha256sum -c` du compagnon : OK |
| texte v7, `git show origin/main:…` après `git fetch origin main` (tête `40b16f8a8a23af3dba48319d4137f4cb972631c7`) | `4e3680d9915ef6e2fa33010fc9b7b2ef5575d74e58e982bfabdbdbcc3e99d5a0` | égale au mandat |
| additif 1 v2, même procédé, trouvé au chemin dit | `e1c1ee842219397a45b5a9a9336d05d873499b2a94bc8847f204b205141908b0` | égale au mandat ; commit de main qui le porte : `4bbd36765af028012221114b33fb7d39f9786c00` |
| addendum 1 de la ligne 1 v4, même procédé (forme) | `c29628a0dd209133545985cc334274462257314560c62c04259c5b31b1686e67` | aucune empreinte attendue dans le mandat |
| rapport du développeur, code v3 | `ae1fa1da825934ec2af942d2047825695804e526122e24038a7098a0f2ca9d9c` | égale au mandat |
| vérification du code v3 | `bd2773e29829ec9778aaaf2f3f4bb03796652f323f3bbb2c95e53ef24d6165f9` | égale au mandat |
| banc v2 | `ffc330839de048891bdbd323b8c19c04289386f9379492440a13e7df4c09b5b3` | égale à l'additif 1 |
| calcul de référence v2 et sa sortie | `802d4dd2…8dc6` ; `2cf1eba7…e724` | égales à l'additif 1 et aux constantes des essais |

Les 18 fichiers du code v3 et leurs empreintes entières sont au § 3 de l'additif : banc `09bfe0db…`, essais `28ad0e89…`, chronométrage `8cb61afb…`, contrôle `b4078e71…`, comparaison `4209748a…` et sa sortie `17ebe555…`, deux rapports de défauts `343f0f77…` et `586e6f45…`, quatre journaux de remplacement, quatre différentiels, rapport, vérification.

Contrôles faits : `sha256sum` sur chaque fichier nommé ; `git hash-object` sur les mêmes ; `git rev-parse 380db356:chemin` pour chacun ; `git rev-parse 380db356` ; `git merge-base --is-ancestor 380db356 lot/compte-organisme-v1` (oui) ; `git log -1` sur le seul fichier de la vérification.

## Ce que j'ai trouvé

1. **La vérification n'est pas dans le commit `380db356`.** Elle est dans le commit `53689f0d18bd7f3e9202bbca34f0e777eaf9a236`, postérieur de quatorze minutes. C'est l'ordre normal ; l'additif le dit et donne les deux commits.
2. **Le rapport du développeur v3 ne donne pas la commande de l'exécution décisive.** Il ne donne que la commande des essais. Les deux commandes (chronométrage, étage 1 décisif) sont dans l'en-tête des deux programmes, écrit par le développeur. L'additif les recopie de là et le déclare.
3. **L'autorisation des racines est l'additif lui-même, par chemin et empreinte.** Le code refuse les racines 2026111931 à 2026111933 sans un fichier dont l'empreinte égale celle donnée en argument. Il ne lit pas le contenu du fichier. L'empreinte de l'additif scellé ne peut pas être écrite dans l'additif : la commande la porte en argument (`HEX`), et la mère la compare au manifeste.
4. **Le champ `depot` du manifeste porte la tête du dépôt au lancement**, non le commit du code. L'identité du code tient à `programme_sha256`. L'additif le dit.

## Ce qui reste ouvert

1. **Contre-lecture de l'additif** (règle R2), si la mère la tient pour due avant le scellement : je ne l'ai pas commandée.
2. **Chemin scellé et empreinte** : à porter dans la commande par la mère. Le fichier scellé doit être celui-ci à l'octet, sinon l'empreinte change.
3. **Lieu de dépôt des sorties** de l'étage 1 et du chronométrage : fixé par aucun texte. Lecture du rédacteur, non éprouvée et non écrite comme règle : un dossier de sortie placé sous le dossier du code ferait dire « dossier du code non propre » au manifeste de l'exécution décisive, puisque le manifeste est construit après l'écriture du résultat.
4. **Contenu du dossier du code** : je n'ai lancé aucune commande de liste. Je n'ai donc pas vérifié qu'il ne contient que les fichiers nommés, ni qu'il ne contient pas `archives-reponses-modeles/`.
5. **Version de `numpy`** : écrite dans aucun rapport ; je ne l'ai pas relevée (aucun interpréteur lancé hors `python3 --version`, qui rend 3.13.18).
6. **Registre** : la clé ADDITIF-1-ORGANISME-V9-LIGNE-3 et R-4081 sont repris du mandat, non relus.
7. Rien n'a été rejoué : essais, contrôle des défauts et preuve d'égalité sont ceux du développeur et du vérificateur.

Aucun nœud de Lazar n'est ouvert par cet additif.

## Refus, écarts

- **Aucun refus de permission, de classifieur ou de garde.**
- Une commande a rendu une erreur de git, qui n'est pas un refus : `git rev-parse` sur le fichier de la vérification au commit `380db356` (« exists on disk, but not in '380db356' »). C'est le constat 1. Je l'ai relancée pour les quatre différentiels qu'elle n'avait pas rendus.
- Écart à la lettre du mandat : la commande de lancement vient de l'en-tête du code, non du rapport du développeur (constat 2).
- Aucun gabarit d'additif de code n'est nommé par l'en-tête du texte : la forme suit l'addendum de la ligne 1.
- Aucun calcul de l'étage 1, aucun lancement du banc, aucune graine dérivée, aucun appel de modèle, aucune dépense. Rien sous `archives-reponses-modeles/`, rien sous `/root/.claude/`.

Rédacteur neuf, modèle F.
