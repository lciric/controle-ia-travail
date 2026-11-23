# Correctif du clone partiel (tentative 1 de T0.8) : commit C2 et pièces préparées, non scellées — v1

Développeur de la chaîne de lancement, le 23 novembre 2026 ; demande de la session mère (R-5125, mot de Lazar
`GO-2026-11-23-05`). Branche `t08/correctif-clone-partiel-v1`. Diagnostic : `diag/t08-gardes-tentative-1-v1`,
`docs/notes/t08-chaine-de-lancement-v1/diag-gardes-tentative-1-v1.md`.

## Commit C2

`3c0f60f9f60626bcacbafa93b8ab3d5b644b7cec`, seul parent C (`bd32f9a5c`). Différentiel par rapport à C : six fichiers.
- `src/controle_ia/t08/entrees_v1.py` (`c743b8ed…`, compagnon neuf) : `rev-list --all --objects --missing=allow-promisor`,
  et son commentaire.
- `scripts/amorce_instance_t08_v1.sh` : un arrêt des gardes sans sortie donne son code et, à 124 ou 137, « délai de
  900 s dépassé ». **EA neuve : `d020de2c9dc2d7083ab0a9fbfb03d429e1fb3ef00e3bbbf7aedfa420fea55df0`.**
- `tests/test_t08_garde_clone_partiel_v1.py` (`3763ba63…`) : trois essais en clone partiel, hors de la liste figée.
  La liste (`5b6db29b…`) et le nombre attendu (255) ne changent pas.

## Mesure du risque résiduel (clone partiel réel de `main`, `--filter=blob:none`)

`mesure-clone-partiel-main-v1.txt` : 6 801 commits ; seconde passe (`git log --all --root --no-renames -m --name-only`)
**0,5 s** ; première passe corrigée (`rev-list --missing=allow-promisor`) 1,1 s, aucun objet téléchargé ; 51 160 blobs
absents, que l'ancienne garde allait chercher un par un. Bien en dessous de 300 s. (Mesure faite dans la session, réseau
de la session ; la machine de location est plus loin de GitHub, mais aucune des deux passes n'y fait de réseau.)

## Pièces préparées, non scellées (le scellement et la ligne `CODE-T08` sont faits par la session mère)

| pièce | chemin | sha256 | ce qui change |
|---|---|---|---|
| pièce des empreintes au commit C2 | `docs/notes/t08-code-aligne-v1/empreintes-code-t08-3c0f60f9-v1.md` | `b759e1e0148b91d43a08ac03879843052584ac579f94448a443ba433a8ec33b6` | 47 fichiers ; contre celle de C : l'amorce, `entrees_v1.py`, l'essai neuf |
| texte de T0.8, version 2 | `prereg/T0.8-bases-boite-noire-v0-v2.md` | `5334f479748dfd647949a48b944bb25901b4ae4d0b3acfdd12c75185737bc0a0` | la v1 scellée (`0855ae06…`) plus deux lignes : l'en-tête d'additif (R-5123, R-5125, `GO-2026-11-23-05`) et la valeur du marqueur `COMMIT_CODE_T08` (C2, pièce des empreintes neuve) |
| fichier des marqueurs, version 2 | `prereg/T0.8-marqueurs-scellement-v2.json` | (ci-dessous) | `COMMIT_CODE_T08` seul |
| configuration de la course, version 2 | `prereg/T0.8-configuration-course-v2.json` | (ci-dessous) | `marqueurs.COMMIT_CODE_T08` seul (programme de la configuration rejoué sur une copie scellée du texte v2) |
| liste de la branche d'entrée | `docs/notes/t08-chaine-de-lancement-v1/correctif-clone-partiel-v1/liste-branche-entree-v2.txt` | (ci-dessous) | 20 fichiers : ceux de `entree/t08-course-v1` (`9d679784`), texte et configuration en version 2 |

Contrôles faits sur le texte v2 : validateur `controle_ia.prereg.problemes` vide ; contrôle « à la place » du programme de
scellement v4 tenu (les marqueurs lus dans le texte égalent le fichier v2) ; `exiger_marqueurs` et
`exiger_marqueurs_au_texte` (joués par le programme de la configuration) tenus.

## Commandes, après le scellement du texte v2 (commit S2) et l'inscription de `CODE-T08` à C2

- Configuration (à réécrire sur le texte scellé ; elle doit égaler le fichier préparé) :
  `PYTHONPATH=src python3 -B scripts/ecrire_configuration_course_t08_v1.py --texte prereg/T0.8-bases-boite-noire-v0-v2.md --marqueurs prereg/T0.8-marqueurs-scellement-v2.json --go-admis GO-2026-11-10-12,GO-2026-11-22-79 --sortie prereg/T0.8-configuration-course-v2.json`
- Branche d'entrée (nom neuf, R12) : `python3 -I -B scripts/construire_branche_entree_t08_v1.py construire --depot . --branche entree/t08-course-v2 --commit-7b 55c3e3eb89a4650419f35999aaa4c54288275b0d --commit-code 3c0f60f9f60626bcacbafa93b8ab3d5b644b7cec --commit-texte <S2> --texte prereg/T0.8-bases-boite-noire-v0-v2.md --config prereg/T0.8-configuration-course-v2.json`
- Lanceur : `T08_PREREG=prereg/T0.8-bases-boite-noire-v0-v2.md T08_CONFIG=prereg/T0.8-configuration-course-v2.json T08_BRANCHE_ENTREE=entree/t08-course-v2 T08_BRANCHE_CODE=<branche qui porte C2> T08_AMORCE_SHA256=d020de2c9dc2d7083ab0a9fbfb03d429e1fb3ef00e3bbbf7aedfa420fea55df0`, depuis un clone au commit qui porte C2.
- Pièce des empreintes, rejeu : `python3 docs/notes/t08-code-aligne-v1/empreintes-code-t08-v3.py verifier docs/notes/t08-code-aligne-v1/empreintes-code-t08-3c0f60f9-v1.md` (code 0).

## Correction de la note de diagnostic

La note dit que l'essai de bout en bout « avait le mécanisme, sans l'échelle ». Plus exactement : son clone était partiel,
mais l'arbre de son code ne portait que des fichiers sous les motifs d'extraction, tous téléchargés à l'extraction ; aucun
blob ne manquait, la garde n'en allait chercher aucun (le compte d'objets de la garde est le même avant et après le
correctif : 1 842 au commit C, 1 844 au commit C2, deux fichiers de plus). Pour qu'il le voie, son arbre devrait porter
des fichiers hors des motifs ; ce n'est pas fait ici (le correctif reste minimal) ; l'essai neuf de la garde le couvre.

## Mineures de la contre-lecture du correctif (Sonnet, `contre-lecture/t08-correctif-gardes-v1`, `eeb7c8aa9`), en réserve écrite

C2 est gardé tel quel : chaque correction changerait le commit du code, donc toutes les pièces ci-dessus et les essais à
rejouer. Les deux mineures que la mère permet de corriger « si c'est en quelques lignes » sont mises en réserve :
- **2 — `objets_git` ne compte plus les blobs absents.** Les compter à part demanderait `--missing=print`, qui accepte
  aussi, sans les distinguer, les objets manquants **non** promis : la garde perdrait son arrêt sur ces objets. Le
  faire proprement (`--missing=print` puis contrôle de chaque objet absent contre les paquets promis) n'est pas « quelques
  lignes ». Conséquence : le nombre « objets git » du journal de l'instance compte les objets présents (commits, arbres,
  blobs extraits) ; il n'est lu par aucune règle.
- **3 — « délai de 900 s dépassé » s'affiche aussi au code 137.** Le code 137 vient ici du second signal de
  `timeout -k 10` (le programme n'a pas fini 10 s après la coupure) : c'est encore un dépassement du délai, mais le
  message gagnerait à dire « coupé par signal, code 137 ». Sans effet sur la conduite : l'arrêt, la consignation et la
  destruction sont les mêmes.
- **1 et 4** : le troisième essai éprouve git et non la garde (il établit la cause, c'est voulu ; les deux premiers
  éprouvent la garde) ; le temps total des gardes à l'échelle : voir la mesure ci-dessus (0,5 s et 1,1 s pour les deux
  passes de git, sur un clone partiel réel de `main`).
