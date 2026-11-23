# Correctif des clés du registre (second défaut de chaîne, préalable P3) : commit C3 et pièces préparées, non scellées — v1

Développeur de la chaîne de lancement, le 23 novembre 2026 ; décision R-5131 de la session mère, sous le mot de Lazar
`GO-2026-11-23-05`. Branche `t08/correctif-cles-registre-v1`.

## Commit C3

`6735dd2e1b30c2615802b78c290e24a80863b18d`, seul parent C2 (`3c0f60f9f`). Différentiel par rapport à C2 :
- `src/controle_ia/t08/entrees_v1.py` (`e76bc494…`) : familles de clés `SCELLEMENT-T08[-V<n>]` et `CODE-T08[-V<n>]`
  (`lignes_famille`, `exiger_ligne_famille`) ; une ligne `CODE-T08-V<n>` dont la quatrième cellule est le commit
  (40 caractères) est lue comme `CODE-T08` (elle tombait jusqu'ici en ligne « d'une autre forme ») ; une clé qui commence
  par `SCELLEMENT-T08-V` ou `CODE-T08-V` sans la forme exacte (`-V<n>`, n ≥ 1 sans zéro de tête) arrête ; les autres clés
  (`SCELLEMENT-T08-BASE-A`…) ne sont pas de la famille.
- `src/controle_ia/t08/lecture_v1.py` (`75966a84…`, compagnon neuf) : `controles_texte_et_registre` exige une seule ligne
  de chaque famille qui correspond (empreinte du texte passé ; commit du marqueur), ni zéro ni deux ; les deux lignes
  retenues sont rendues avec leur clé (`cle`) ; antériorité inchangée, portée sur ces deux lignes. Cette fonction sert au
  passage à blanc (P3) et à la lecture.
- `tests/test_t08_cles_famille_v1.py` (`30a1aa29…`) : cas sains v1 seul ; v1 et v2, la v2 seule correspond ; v1, v2, v3,
  la v3 seule correspond (et la ligne `SCELLEMENT-T08-BASE-A` présente) ; antériorité de la ligne retenue ; artefacts :
  deux lignes qui correspondent (pour chaque famille), aucune (pour chaque famille), clés `SCELLEMENT-T08-VX`,
  `CODE-T08-V0`, `CODE-T08-V02`, famille absente. Hors de la liste figée (inchangée, 255 essais).

**Où ces clés sont lues** (relevé sur C2) : seulement `entrees_v1.py` (lecture du registre) et `lecture_v1.py`
(`controles_texte_et_registre`). Le lanceur ne les cite qu'en commentaire ; l'amorce, `course_v1.py`, les deux
programmes de configuration et la garde de calcul (`.claude/hooks/garde_calcul.py`) ne les lisent pas ; le programme de
scellement ne les nomme que dans son texte d'aide. **L'amorce ne change pas : EA reste
`d020de2c9dc2d7083ab0a9fbfb03d429e1fb3ef00e3bbbf7aedfa420fea55df0`.**

## Passage à blanc (P3) rejoué de bout en bout

Code au commit C3 ; registre : copie du registre réel de `main` (lignes `SCELLEMENT-T08`, `CODE-T08`,
`SCELLEMENT-T08-V2`, `CODE-T08-V2`, `SCELLEMENT-T08-BASE-A`), plus deux lignes v3 simulées (`registre-simule-v3-v1.txt`) ;
texte v3 scellé sur une copie ; configuration v3 écrite par son programme ; pièce « mots et coût » du dépôt.
- Cas sain : **code 0** ; lignes retenues `SCELLEMENT-T08-V3` et `CODE-T08-V3` ; aucune ligne mal formée lue
  (`passage-a-blanc-v123-sortie-v1.json`).
- Artefact : le même registre sans les lignes v3 : **code 1**, « famille SCELLEMENT-T08 (['SCELLEMENT-T08',
  'SCELLEMENT-T08-V2']) : aucune ligne à l'empreinte du préenregistrement passé … : autre texte scellé : arrêt »
  (`passage-a-blanc-sans-v3-arret-v1.txt`).

## Pièces préparées, non scellées

| pièce | chemin | sha256 |
|---|---|---|
| pièce des empreintes au commit C3 (48 fichiers ; contre celle de C2 : `entrees_v1.py`, `lecture_v1.py`, l'essai neuf) | `docs/notes/t08-code-aligne-v1/empreintes-code-t08-6735dd2e-v1.md` | `7f8a7a92d0a45a892f157eb96613316a6eb04d73a3aa81ef7c83d05a7fc7519e` |
| texte de T0.8, version 3 (la v2 scellée, `5334f479…`, plus un additif v3 qui cite R-5131 et `GO-2026-11-23-05`, et le marqueur `COMMIT_CODE_T08` = C3) | `prereg/T0.8-bases-boite-noire-v0-v3.md` | `72a2611b3eff8ef070ab6f12f1468213cb88a8f42729eb2e9edeea7fcb884918` |
| marqueurs, version 3 (`COMMIT_CODE_T08` seul change) | `prereg/T0.8-marqueurs-scellement-v3.json` | `b88734a5473c1fbfb45a42ef79038cca4e43a55dc77e9699f3c86c286597b62a` |
| configuration de la course, version 3 (`marqueurs.COMMIT_CODE_T08` seul change contre la v2 de `main`) | `prereg/T0.8-configuration-course-v3.json` | `7973d240ec3059c3f51265f245b4b37353f7aa9352a99c074dc83429e052998a` |
| liste de la branche d'entrée v3 (20 fichiers ; texte et configuration en v3) | `docs/notes/t08-chaine-de-lancement-v1/correctif-cles-registre-v1/liste-branche-entree-v3.txt` | `2f095e69084c5614cb0194ac7aefc5892d87eb2ed6e10107642e5597108547a3` |

Contrôles sur le texte v3 : validateur vide ; `exiger_marqueurs` et `exiger_marqueurs_au_texte` (par le programme de la
configuration, sur une copie scellée) tenus ; passage à blanc ci-dessus.

## Commandes, après le scellement du texte v3 (S3) et l'inscription de `SCELLEMENT-T08-V3` et `CODE-T08-V3` (C3)

- Configuration : `PYTHONPATH=src python3 -B scripts/ecrire_configuration_course_t08_v1.py --texte prereg/T0.8-bases-boite-noire-v0-v3.md --marqueurs prereg/T0.8-marqueurs-scellement-v3.json --go-admis GO-2026-11-10-12,GO-2026-11-22-79 --sortie prereg/T0.8-configuration-course-v3.json` (elle doit égaler le fichier préparé).
- Branche d'entrée : `python3 -I -B scripts/construire_branche_entree_t08_v1.py construire --depot . --branche entree/t08-course-v3 --commit-7b 55c3e3eb89a4650419f35999aaa4c54288275b0d --commit-code 6735dd2e1b30c2615802b78c290e24a80863b18d --commit-texte <S3> --texte prereg/T0.8-bases-boite-noire-v0-v3.md --config prereg/T0.8-configuration-course-v3.json`.
- P3 : `PYTHONPATH=src python3 -m controle_ia.t08.passage_a_blanc_v1 --config prereg/T0.8-configuration-course-v3.json --registre registres/scellements-v1.md --prereg prereg/T0.8-bases-boite-noire-v0-v3.md --racine-piece .`, **depuis un arbre au commit C3** (le code de C2 lit encore les clés exactes).
- Lanceur : `T08_PREREG=prereg/T0.8-bases-boite-noire-v0-v3.md T08_CONFIG=prereg/T0.8-configuration-course-v3.json T08_BRANCHE_ENTREE=entree/t08-course-v3 T08_BRANCHE_CODE=<branche qui porte C3> T08_AMORCE_SHA256=d020de2c9dc2d7083ab0a9fbfb03d429e1fb3ef00e3bbbf7aedfa420fea55df0`.
- Pièce des empreintes : `python3 docs/notes/t08-code-aligne-v1/empreintes-code-t08-v3.py verifier docs/notes/t08-code-aligne-v1/empreintes-code-t08-6735dd2e-v1.md` (code 0).
