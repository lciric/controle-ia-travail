# Rapport du rédacteur — addendum 1 au préenregistrement scellé de la ligne 1, version 4 (erratum) — v1

Auteur : rédacteur neuf, modèle F. Date (`date -u`) : 2026-11-19, 22:21. Pièce de travail (classe C). Rien lancé, aucun résultat lu, aucune graine dérivée, rien écrit dans le dépôt, aucun commit, aucune poussée, aucun appel de modèle, aucune dépense, aucun réseau. Aucun refus d'outil. Rien touché sous `archives-reponses-modeles/`.

Mandat : `mandat-redacteur-addendum-ligne-1-v4-v1.md`, `447df1443aecc990629a9b5845a06c762a094414a092da40d2a39e146ceb5f16`, empreinte vérifiée avant de commencer (branche `lot/compte-organisme-v1`, commit lu `12535e60989af99b6cbb3fe7a2800844ae366dbb` ; mandat entré au commit `ebe691f82cf875166e023723b3957acdbfcff681`).

## Verdict

La version 4 est écrite, non scellée. Elle ne diffère de la version 3 que par les cinq corrections du contrôle `controle-differentiel-addendum-1-ligne-1-v3-v1.md` (`328322989b4d0eda7de480a666ed5599a26fe713ab16dc5d5a9fedf7000f17d5`, § 6) et par la tenue que ce contrôle décrit. La version 3 (`fb48a8ab9aeee1667c46a3d72dbf97d39343ecfb10227c652074d38f46ba55d5`) est intacte dans le dépôt (R12), empreinte relue après l'écriture.

## Fichiers rendus (bloc-notes `redacteur-addendum-ligne-1-v4/`)

| fichier | sha256 |
|---|---|
| `addendum-1-preenregistrement-ligne-1-effort-recherche-v5-v4.md` | `c29628a0dd209133545985cc334274462257314560c62c04259c5b31b1686e67` |
| `differentiel-addendum-1-ligne-1-v3-v4.diff` (`diff -u` de la version 3 du dépôt vers la version 4 ; 87 lignes) | `2798ad6b4c6e7b8cfa39592ccfe33b93a4c66c49914ad932eedd20a9e4a2d308` |
| `appliquer_corrections_addendum_ligne_1_v4.py` (programme de remplacement, lancé une fois) | `0fd2c351c3552bffc9a9c080e64412bf2d25a7522ce8fb485dc26874d1747531` |

Empreintes vérifiées par programme avant de citer : version 3 `fb48a8ab…`, son rapport `d2cc55dd…`, son différentiel `8c42ccc8…`, son mandat `ccd4b364…`, son programme `9d26722a…` (lu, non exécuté) ; contrôle `32832298…` (égale au commit `e8069af6d040616a2853f4ec4fc965809bd05706` et au commit lu) ; vérification de la version 2 `b0c09a4f…` ; version 2 `b5d76973…` (intacte).

## Les cinq corrections : faites à la lettre, par programme

Les textes exacts sont extraits par le programme de la section 6 du contrôle, sans recopie à la main ; chaque texte ancien a été trouvé exactement une fois dans la version 3 ; après application, chaque texte neuf est présent une seule fois et les textes anciens des corrections 1, 2 et 4 ont disparu (contrôles du programme).

1. § 6 : le paragraphe « Ajout de la mère […] par une configuration v3 » est remplacé en entier par le texte exact (configuration v3 non retenue ; ni configuration v3 ni code v3 ; contrôle de la garde A14 par lecture, sous l'option A comme sous l'option B).
2. § 6, « Conséquence pour la garde A14 » : la source d'heure est le fichier d'état du lanceur (`etat-lancement-ligne1-v2.json`, champ `debut`), le journal du lanceur n'étant lu qu'en complément ; heure consignée au registre pour une étape lancée à la main.
3. § 9, point 8 : texte exact ajouté après « le code ne change pas. » (copie et dossier d'empaquetage hors du dossier de sortie et hors de `code/` ; plafond du point 4 sur le total des deux versements).
4. En-tête, ligne de l'auteur : « je » et « cette version », hors de l'en-tête, du § 8 et des § 11 et suivants, désignent le rédacteur de la version 2 et la version 2.
5. En-tête : puce ajoutée après « Condition de la même ligne, recopiée telle quelle » (lecture de la condition de GO-2026-11-19-81 par la mère).

## Ce que le contrôle demande au rapport

- **Retrait de la configuration v3** : fait sur la décision de la mère (vers 22:10Z, d'après le mandat : ni configuration v3 ni code v3). La réserve du rapport du rédacteur de la version 3 sur cet ajout est donc levée : le code visé reste celui du § 5.1.
- **Source d'heure de la garde A14** : corrigée (correction 2). D'après le contrôle (§ 3), l'erreur venait de la correction 9 du contre-lecteur de la version 1, non du rédacteur de la version 2.
- **Lecture de GO-2026-11-19-81 par la mère** : écrite en tête (correction 5).
- **Décision 4** : toujours ouverte, sans défaut ; rien ne part avant elle (§ 6, inchangé).
- **Second ajout de la mère** (§ 9, point 8, versement de l'étalonnage pendant la course décisive) : gardé, conditionnel à l'option A, précisé par la correction 3.
- **Différentiel version 3 → version 4** : versé ; à faire contrôler par le même vérificateur (modèle O).

## Tenue de version, déclarée

Titre (« v4 ») ; phrase de statut (version 4, ne diffère de la version 3 que par les cinq corrections et la tenue ; l'histoire de la version 3 gardée dans une phrase au passé) ; ligne de l'auteur (mandat de la version 4 cité, troisième rédacteur) ; heure ; ligne « Contrôle du différentiel version 2 → version 3 » ajoutée en tête ; § 8 : ligne du contrôle remplie (chemin, empreinte, commit, verdict) et reformulée comme demandé, ligne « À PORTER » ajoutée pour le contrôle version 3 → version 4 ; § 11 : la seule phrase demandée, à la fin du paragraphe « Deux ajouts de la mère » ; § 12 neuf.

## Écarts et points à connaître

1. **Tenue de ma main, hors des textes imposés, à contrôler** : la phrase de statut ; la ligne de l'auteur ; la ligne du contrôle en tête ; le § 12 (dont le paragraphe « Raison du retrait »).
2. **Trois « cette version 3 » devenus « la version 3 »** (ligne de l'auteur, ligne « Vérification de la version 2 » de l'en-tête, table du § 8), et « Aucun des deux » devenu « Aucun des trois » dans la ligne de l'auteur. Le contrôle ne les nomme pas ; je les ai faits parce que, dans une version 4, ces mots auraient été faux ou ambigus, comme la version 3 avait fait de « Cette version 2 » au § 8. Si le vérificateur les refuse, ils se retirent sans toucher au reste.
3. Au § 12, je dis ce que les corrections 1 à 3 affirment du code **d'après le contrôle** : je n'ai rouvert aucun fichier du code.
4. Non retouché, parce que hors du mandat : au § 9, point 5, « le journal du lanceur sert au contrôle du § 6 » reste vrai seulement « en complément » depuis la correction 2 ; le fichier d'état du lanceur, lui, est versé par l'empaquetage (texte de la correction 2). Au § 11, « Tenue de version » et « Inchangé » restent tels quels, comme histoire de la version 3.
5. Restent « À PORTER » : chemin, empreinte, commit et heure du scellement (§ 6) ; contrôle du différentiel version 3 → version 4 (§ 8).
6. Les deux lignes d'en-tête du différentiel portent les chemins et les heures des fichiers (dépôt et bloc-notes), comme celui de la version 3 ; le corps fait foi.
