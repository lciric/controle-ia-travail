# Contre-lecture de l'additif 5 (additif de code de la mesure « portée à 200 » de la ligne 3), version 1 — v1

Pièce de travail (classe C) sur une pièce décisive, contre-lue par un autre modèle que le rédacteur (règle R2). Écrite le 2026-11-20 sur le mandat `mandat-contre-lecteur-additif-5-code-portee-200-v1.md` (`4e6ac7597c9b9766a140f49149f33fb7b835c914f7c2b5839b6e677e9a38bbf1`, égale à son compagnon). Règle d'aveugle tenue : aucune mesure de l'étage 1 ouverte, rien sous `…/execution-etage-1-v1/`, `…/verdict-etage-1-v1/` ni `prereg/organisme-auto-conception-v9/ligne-3/verdict-etage-1/`. Aucun lancement du banc ni du chronométrage, aucune graine dérivée, aucune écriture dans le dépôt, aucun commit, aucun appel de modèle.

Pièce contre-lue : `LIGNE/additif-3-portee-200-v1/additif-5-code-preenregistrement-ligne-3-portee-200-v1.md`, `d1b237d602d68b488510ff0ba94f9519481984554ae6627807ce43f1a1c4233d` (LIGNE = `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-3-votes-effectifs-juges/`).

## Verdict : À corriger

Trois corrections de fond (1 à 3), et trois corrections de nom qui en découlent (4 à 6), parce qu'une version neuve prend un nom neuf (règle R12) et que `CHEMIN` est écrit dans le texte. Rien ne touche une règle, un seuil, une prédiction, une lecture, une racine ou une empreinte de la table. Le code, les racines, les deux commandes et l'interpréteur sont justes ; les fautes sont dans les deux blancs et dans une attribution à l'additif 2.

## 1. Empreintes

- Pièces qui font foi, chacune égale à son compagnon (`sha256sum -c` : OK) : l'additif 5 (`d1b237d6…`) ; le rapport de son rédacteur (`de001c345042034067d6586bf153dfda7e220e377e17e08756713eadaad4f95e`) ; le mandat du rédacteur (`8a669690…`) ; la contre-lecture du code (`ab19b31a…`) ; le rapport du développeur (`117b7686…`, égal au § 2.4). Additif 3 v3 (`71b7a876…`) et additif 2 v3 (`f5562d20…`) tirés de `origin/main` par `git show` redirigé, égaux à leurs compagnons tirés de même.
- Les quatorze fichiers de `LIGNE/code-portee-200-v4/` : `sha256sum -c` de leurs quatorze compagnons, quatorze « OK » ; empreintes recalculées sur disque, chacune présente dans le texte de l'additif à l'octet près (le banc et le chronométrage deux fois, au § 2.1 et au § 9 ; les douze autres une fois). Les quatre copies du v3 sont égales à l'additif 2, § 3.1 et § 3.2.
- Commit `af19ff8d` = `af19ff8dbb0e1c990f7bb97f7e5a77a332dca14c` (`git rev-parse`), ancêtre de la tête de `lot/compte-organisme-v1` (`git merge-base --is-ancestor` : vrai). Banc et chronométrage tirés de ce commit par `git show af19ff8d:CHEMIN > FICHIER` : `79865552dd666ea697a817c520d6f50337a9634cd8efe8a7b26d08a280ab4de7` et `6b9d2cbfd9bbf638d30c0d314531de510d85a4a2b28c8da40100ec8c7be51b90`, égales à la table. Pour l'ensemble des fichiers suivis du dossier : `git diff --quiet af19ff8d -- LIGNE/code-portee-200-v4` rend 0 (disque égal au commit).
- Le dossier du code n'est pas encore sur `origin/main` (tête lue après `git fetch`) : la recopie par la mère reste à faire, comme l'additif le dit.

## 2. Fidélité au § 5 de l'additif 3

Tenue. L'additif ne fait que nommer : dossier, commit, quatorze empreintes, les trois racines du § 2 de l'additif 3 avec leurs clés (2 ; 12) et `.spawn(210)`, les deux commandes du gabarit complétées, l'interpréteur. Racines refusées (2026111931 à 2026111937), racine des essais (2026111930) : égales à l'additif 3, § 2, et au code (`RACINES_TOUJOURS_REFUSEES`, `TACHES_PERMISES_PAR_RACINE_PORTEE_200`, `NOMBRE_CELLULES_PORTEE_200`). Le contrôle du manifeste du § 4 reprend celui de l'additif 3, § 6, point 3, sans rien en retirer. Les § 6 et § 7 ne font que redire la garde, la réserve du `.gitignore` et les points laissés à la mère et à l'agent qui prononce par la contre-lecture du code. Aucune règle, aucun seuil, aucune prédiction, aucune lecture ne change. Le seul ajout à la lettre des commandes (les deux `env -u`) est déclaré.

## 3. Les commandes

Complètes et exactes ; lançables telles quelles une fois `HEX` porté (voir le § 5 pour `HEX` et le commit).

- Syntaxe : `env -C DOSSIER_DU_CODE -u … -u … PYTHONDONTWRITEBYTECODE=1 python3 -B …` est valide pour GNU `env` (coreutils 9.4 sur cette machine) ; `-C` place le dossier courant dans le dossier du code, comme le gabarit le veut.
- Arguments : ceux de `main` du banc (`--portee-200`, `--autorisation-additif`, `--empreinte-additif`, `--sortie`, tous requis) et du chronométrage (`--autorisation-additif`, `--empreinte-additif`, `--manifeste`). Hors essai, la configuration est la constante `CONFIGURATION_PORTEE_200` (le banc refuse toute autre).
- `CHEMIN` absolu : nécessaire, `verifier_autorisation` ouvre le chemin tel quel depuis le dossier du code. Le chemin proposé est absent de `origin/main` (libre).
- **Les deux `env -u` : à garder.** Raison lue au code : le chronométrage charge le banc (`charger_banc`, l. 97) avant d'appeler `verifier_variables_de_chemin_non_posees` (l. 106) ; si `BANC_LIGNE_3_CHEMIN` était posée, un fichier étranger serait exécuté à l'import, et le refus lui-même viendrait de ce fichier. Les `-u` retirent la variable avant l'interpréteur ; le refus du code reste un second filet. Au banc, le contrôle (l. 2038) précède toute dérivation ; les `-u` y sont sans effet sur un lancement juste.
- **Dossiers de sortie : justes.** `LIGNE/execution-portee-200-v1/chronometrage` et `…/mesure` sont hors du dossier du code (frères de `code-portee-200-v4/`), absents (`stat` : absent sur disque ; absent de `origin/main`), et aucun composant de leur chemin n'est `archives-reponses-modeles` (LIGNE n'en porte pas sur `origin/main`). Le chronométrage crée `execution-portee-200-v1/chronometrage` avec ses parents (`mkdir(parents=True, exist_ok=False)`), puis la mesure crée `…/mesure`, absent ; la garde de la mesure borne `git status --porcelain` au dossier du code, que ce premier dossier non suivi ne touche pas (additif, § 6, point 3 : juste).
- **Chronométrage à `--repliques-echantillon` par défaut** (20, l. 94) : juste, l'additif dit « aucun autre argument ».
- Sorties et compagnons : `ecrire_json_exclusif` écrit chaque JSON et son `.sha256` ; noms égaux au § 4.

## 4. L'interpréteur

`python3` = `/usr/local/bin/python3` (`command -v python3`), Python 3.13.18 (`python3 --version`), **numpy 2.5.3** (`python3 -m pip show numpy`, relevé par moi). Le Python de l'environnement du dépôt porte numpy 2.4.6 (`.venv/bin/python -m pip show numpy`). Le choix est juste : c'est la lettre du gabarit (additif 3, § 5 ; additif 2, § 6) et l'interpréteur sous lequel la contre-lecture du code a rejoué les 157 essais. La raison 3 du § 5 attribue toutefois à l'additif 2 ce qu'il ne dit pas (correction 3).

Remarque, sans correction : `python3` se résout par le `PATH` du lanceur. Lancer d'un interpréteur de commandes où l'environnement du dépôt n'est pas activé ; la mère compare `versions.executable` et `versions.numpy` du manifeste à ce paragraphe, comme l'additif le dit.

## 5. Les deux blancs

- **Le commit de `main`** : un blanc juste, à une condition que l'additif ne dit pas. Un commit ne peut porter son propre identifiant : le versement du dossier sur `main` doit être un commit antérieur à l'écriture de ce blanc et au commit qui scelle l'additif. « La mère le recopie sur `main` au scellement » laisse croire à un seul commit (correction 2).
- **`HEX` ne peut pas être écrit dans l'additif.** Écrire l'empreinte dans le fichier change le fichier, donc son empreinte ; l'additif le dit lui-même à la ligne suivante (« Un fichier ne porte pas sa propre empreinte »), mais l'appelle un blanc « à écrire par la mère au scellement ». L'additif 2, § 6, dit juste : « elle n'est pas écrite ici ». `HEX` se lit dans le compagnon scellé et se porte dans les commandes au lancement (correction 1).
- Il n'y a donc qu'**un** blanc à écrire dans le texte, le commit de `main`. Rien d'autre à écrire par la mère.

## 6. Corrections (chaque « Ancien » compté une fois par `grep -c -F -e` dans `d1b237d6…`)

**Correction 1 (§ 4, `HEX`).**
Ancien : « - `HEX` = **à écrire par la mère au scellement** : l'empreinte sha256 de cet additif scellé, celle de son compagnon. Un fichier ne porte pas sa propre empreinte. »
Neuf : « - `HEX` = l'empreinte sha256 de cet additif scellé, celle de son compagnon, **qui n'est pas écrite ici** : un fichier ne porte pas sa propre empreinte. La mère la lit dans le compagnon scellé et la porte dans les deux commandes au lancement, sans rien écrire dans ce fichier. »

**Correction 2 (§ 2, commit de `main`).**
Ancien : « Commit de `main` qui porte le dossier : **à écrire par la mère au scellement** (je ne peux pas le connaître). »
Neuf : « Commit de `main` qui porte le dossier : **à écrire par la mère au scellement** (je ne peux pas le connaître). C'est le commit du versement du dossier sur `main`, fait avant que ce blanc soit écrit, donc avant le commit qui scelle cet additif ; c'est le seul blanc de cet additif. »

**Correction 3 (§ 5, raison 3).**
Ancien : « 3. l'additif 2, § 6, relève 2.5.3 comme version de numpy de l'environnement de l'étage 1 ; garder le même interpréteur écarte une différence de version de numpy entre la mesure à 100 et la mesure à 200, que l'audit de symétrie de l'additif 3 compare cellule par cellule. Je n'ai pas lu le manifeste de l'étage 1 (règle d'aveugle) : ce point est à relire par l'agent qui prononce. »
Neuf : « 3. l'additif 2, § 6, donne 2.5.3 comme la version de numpy relevée par le contre-lecteur dans l'environnement des essais et de la vérification du code de l'étage 1, non comme celle de l'exécution de l'étage 1 ; si l'étage 1 a tourné sous ce même interpréteur, le garder écarte une différence de version de numpy entre la mesure à 100 et la mesure à 200, que l'audit de symétrie de l'additif 3 compare cellule par cellule. Je n'ai pas lu le manifeste de l'étage 1 (règle d'aveugle) : sa version de numpy est à relire sur ce manifeste par l'agent qui prononce. »

**Correction 4 (titre).**
Ancien : « racines autorisées, commandes de lancement — v1 »
Neuf : « racines autorisées, commandes de lancement — v2 »

**Correction 5 (ligne de statut).**
Ancien : « **Statut : version 1, non scellée. »
Neuf : « **Statut : version 2, non scellée. »
et, à la fin de cette même ligne, après « (`8a669690ac1c43b46d0c6bae9b02ce208783a9bd2b397b557de0ca7399d0d291`, égale à son compagnon). », la phrase : « Version 2, même jour : elle porte à la lettre les corrections 1 à 6 de la contre-lecture `contre-lecture-additif-5-code-portee-200-v1.md` (empreinte de son compagnon) sur la version 1 (`d1b237d602d68b488510ff0ba94f9519481984554ae6627807ce43f1a1c4233d`), au § 2, au § 4, au § 5, au titre et à cette ligne ; rien d'autre ne change. » (l'empreinte entre parenthèses est celle du compagnon de la présente pièce, recopiée par le rédacteur ; elle ne peut pas figurer ici).

**Correction 6 (§ 4, `CHEMIN`).**
Ancien : « /prereg/organisme-auto-conception-v9/additif-5-code-preenregistrement-ligne-3-portee-200-v1.md` — le chemin **absolu** »
Neuf : « /prereg/organisme-auto-conception-v9/additif-5-code-preenregistrement-ligne-3-portee-200-v2.md` — le chemin **absolu** »
(La version 2 se nomme `additif-5-code-preenregistrement-ligne-3-portee-200-v2.md` et se scelle sous ce nom ; si la mère scelle sous un autre nom, `CHEMIN` doit le suivre.)

Après ces corrections : contrôle du différentiel v1 → v2 par le même contre-lecteur, puis scellement par la mère.

## 7. Écarts au mandat, déclarés

- Une commande `awk` avec un programme en ligne, pour compter chaque empreinte de la table dans le texte de l'additif : cela s'approche de l'interdit « code en ligne passé à un interpréteur » ; écart, déclaré. Le résultat a été recoupé à l'œil, empreinte par empreinte.
- Un appel `sha256sum` avec une option fausse (`--output`), refusé par l'outil lui-même, sans effet.
- Gestes de contrôle hors de la liste du mandat, chacun sur un seul chemin nommé : `git fetch origin main` ; `git diff --quiet af19ff8d --` borné au dossier du code (code de sortie seul, aucune liste rendue) ; `git merge-base --is-ancestor` ; quatre `git cat-file` sur `origin/main` (dossier de sortie, chemin de l'additif, dossier du code, `archives-reponses-modeles` sous LIGNE) ; `stat` sur le parent des sorties ; `git rev-parse --abbrev-ref HEAD` ; `printenv PATH` ; `env --version` ; cinq recherches `grep` et six décomptes `grep -c -F -e`, chacun borné à un seul fichier nommé (banc v4, chronométrage, additif 5).
- Les additifs 2 et 3 et les deux programmes tirés du commit sont copiés dans un sous-dossier `lus/` de mon dossier.
- Aucun refus de permission, de classifieur ni de garde.

## 8. Pièces lues

| pièce | sha256 | lecture |
|---|---|---|
| mandat du contre-lecteur | `4e6ac7597c9b9766a140f49149f33fb7b835c914f7c2b5839b6e677e9a38bbf1` | en entier |
| additif 5, version 1 | `d1b237d602d68b488510ff0ba94f9519481984554ae6627807ce43f1a1c4233d` | en entier |
| rapport du rédacteur | `de001c345042034067d6586bf153dfda7e220e377e17e08756713eadaad4f95e` | en entier |
| mandat du rédacteur | `8a669690ac1c43b46d0c6bae9b02ce208783a9bd2b397b557de0ca7399d0d291` | en entier |
| additif 3, version 3 (`origin/main`) | `71b7a876398cdcc133f006c01ff7eb644e8f2c69be79e90be50088bd26492807` | en entier |
| additif 2, version 3 (`origin/main`) | `f5562d206bc56bfa1ebf2ff88abcdd6fcc93ececb6abd513d05611c6c4e5f25a` | en entier |
| contre-lecture du code | `ab19b31a1597f471b1ac057dbe92638bf29dd1a422c83af26ffe3dc6f613d2fd` | en entier |
| rapport du développeur | `117b768697de68e768cc4f2b463f50abb0abbf189a6dc59e2e6083ac9a078090` | empreinte seule |
| `chronometrer_portee_200_ligne_3_v1.py` | `6b9d2cbfd9bbf638d30c0d314531de510d85a4a2b28c8da40100ec8c7be51b90` | en entier |
| `banc_juges_scriptes_ligne_3_v4.py` | `79865552dd666ea697a817c520d6f50337a9634cd8efe8a7b26d08a280ab4de7` | l. 1 à 249 ; `ecrire_json_exclusif` ; l. 1740 à 2051 (manifeste, mode « portée à 200 », gardes, `main`) |

Les autres fichiers du code : empreintes seules.

Contre-lecteur neuf, modèle O.
