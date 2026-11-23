# Passation — développeur de la chaîne de lancement de T0.8 — 2026-11-23 06:25 UTC

Session `session_013QMaykVEGYEXUpWBeemUjb` (modèle Opus 5.5). Écrite sur le mot de Lazar `GO-2026-11-23-09` relayé par la
session mère. **Aucune machine, aucun serveur, aucune tâche planifiée actifs** (la seule tâche planifiée, reprise à
08:00Z, a été supprimée le 22 à 21:37Z quand la mère a levé l'économie). Rien ne tourne.

## Mandat

Développeur de la chaîne de lancement de T0.8 (bases boîte noire), mandat de la session mère
`session_013QMayjbmQUdDuDs2S3i3XD`. Consigne : `docs/procedures/t08-course-v1/consigne-chaine-de-lancement-t08-v3.md`
(`6f52c4db…`, branche `prep/t08-texte-complet-fable-v1`). Interdits tenus : aucune machine, aucun appel au loueur, aucune
dépense, aucun résultat ni verdict lu, aucune branche `calcul/…` ni `verdict/…` lue (un refus d'outil sur `calcul/t08-course-v1`
le 23 n'a été ni rejoué ni contourné), jamais de poussée vers `lciric/controle-ia`.

## Interlocuteurs

- Mère : `session_013QMayjbmQUdDuDs2S3i3XD` (ordres, décisions R-5123, R-5125, R-5131).
- Rédacteur de T0.8 : `session_013QMayo5SNVbiUW6hGnPrCo` (quota de Fable épuisé jusqu'au 29 novembre).
- Contre-lecteur de la chaîne : `session_013QMaymC2hofayrH8ySBw7N` ; contre-lecteurs Sonnet lancés par la mère.
- Développeur de l'alignement : `session_013QMaymaQLzKJsDBnmrEZ7q`.

## Fait (branches et commits, tous poussés)

| objet | branche | commit |
|---|---|---|
| chaîne v3 + r-9 (empreinte de `course-t08.json` exigée), contre-lue conforme | `t08/chaine-de-lancement-v1` | `d17bd6170` |
| commit C (code aligné + chaîne + scellement v4 + registre des accords de main) | `t08/chaine-de-lancement-v1` | `bd32f9a5c` |
| programme de scellement v4 (contre-lu conforme, Sonnet) ; v5 (mineures m-1, m-2, non contre-lue, hors de C) | `t08/scellement-v4` | `4c9c9b1b3` ; `eaea816b9` |
| fusion de C dans main + pièce des empreintes de C (46 fichiers) ; poussée sur main par la mère | `t08/fusion-vers-main` | `94ca2036b` |
| diagnostic de la tentative 1 (garde : téléchargement paresseux du clone partiel, 900 s) | `diag/t08-gardes-tentative-1-v1` | `603567e27` |
| C2 : `rev-list --missing=allow-promisor`, message d'arrêt des gardes ; EA `d020de2c…` ; contre-lu conforme avec mineures | `t08/correctif-clone-partiel-v1` | C2 `3c0f60f9f` ; pièces v2 `d596fc86b` |
| C3 : familles de clés `SCELLEMENT-T08[-V<n>]`, `CODE-T08[-V<n>]` (R-5131) ; EA inchangée | `t08/correctif-cles-registre-v1` | C3 `6735dd2e1` ; pièces v3 `1cff7cc0f` |

Essais au commit C3 : suite de T0.8 274 passés, 5 sautés ; essai de bout en bout code 0 (255 passés, 1 écarté sur la
machine simulée ; versement prouvé) ; P3 rejoué contre une copie du registre réel de main plus deux lignes v3 simulées :
code 0, lignes v3 retenues ; sans elles : arrêt.

## Pièces v3 préparées, non scellées (commit `1cff7cc0f`)

- pièce des empreintes au commit C3 : `docs/notes/t08-code-aligne-v1/empreintes-code-t08-6735dd2e-v1.md`, `7f8a7a92d0a45a892f157eb96613316a6eb04d73a3aa81ef7c83d05a7fc7519e` ;
- texte v3 : `prereg/T0.8-bases-boite-noire-v0-v3.md`, `72a2611b3eff8ef070ab6f12f1468213cb88a8f42729eb2e9edeea7fcb884918` ;
- marqueurs v3 : `prereg/T0.8-marqueurs-scellement-v3.json`, `b88734a5473c1fbfb45a42ef79038cca4e43a55dc77e9699f3c86c286597b62a` ;
- configuration v3 : `prereg/T0.8-configuration-course-v3.json`, `7973d240ec3059c3f51265f245b4b37353f7aa9352a99c074dc83429e052998a` ;
- liste de la branche d'entrée v3 : `docs/notes/t08-chaine-de-lancement-v1/correctif-cles-registre-v1/liste-branche-entree-v3.txt`, `2f095e69…` ;
- EA : `d020de2c9dc2d7083ab0a9fbfb03d429e1fb3ef00e3bbbf7aedfa420fea55df0`. Commandes : `…/correctif-cles-registre-v1/pieces-preparees-c3-v1.md`.

## Reste

- Contre-lecture (Sonnet, lancée par la mère) du différentiel C2 → C3 ; corrections éventuelles par moi, vérifiées par
  le même contre-lecteur.
- Côté mère : scellement du texte v3, lignes `SCELLEMENT-T08-V3` et `CODE-T08-V3` ; fusion de C3 dans la branche du code
  si elle doit être main ; P3 depuis un arbre au commit C3 ; P1 à P10 par l'exécutante ; relance.
- Le rapport de la chaîne (v3, `a65b8bc3…`) ne décrit pas encore C2 et C3 : les notes `diag-gardes-tentative-1-v1.md`,
  `correctif-clone-partiel-v1/pieces-preparees-c2-v1.md` et `correctif-cles-registre-v1/pieces-preparees-c3-v1.md` en tiennent lieu.

## Réserves

- Mineures de la contre-lecture de C2 en réserve écrite (comptage des blobs absents ; message du code 137) ; mineures m-1,
  m-2 du scellement v4 corrigées en v5, hors de C, non contre-lues.
- L'essai de bout en bout ne voit pas un coût proportionnel à la taille de l'histoire (son arbre ne porte que des fichiers
  sous les motifs d'extraction) ; l'essai `tests/test_t08_garde_clone_partiel_v1.py` le couvre.
- Les traces de l'instance de la tentative 1 (`calcul/t08-course-v1`) n'ont pas été lues par moi (cloisonnement).
- Nombres du rapport v3 (252, 265) dépassés : C2 et C3 donnent 271 et 274 essais de la suite, 255 sur la machine.

## Versé ici

`docs/notes/t08-chaine-de-lancement-v1/versement-2026-11-23-v1/` : journaux des essais (suites, bout en bout, scellement,
mesure, reproduction), rapports et journaux d'instance des sept essais de bout en bout, différentiels de travail, et
l'inventaire du bloc-notes (`inventaire-bloc-notes-v1.md` : ce qui n'est pas versé, copies régénérables du dépôt ou du jouet,
3,1 Go de clones d'essai). Aucun secret (recherche faite).

## Prochaine action exacte

Attendre le retour de la contre-lecture de C3 (`t08/correctif-cles-registre-v1`, `6735dd2e1`). Sur un constat : corriger
sur cette branche en un lot, rejouer `tests/test_t08_*.py` et l'essai de bout en bout
(`PYTHONPATH=src python3 -B scripts/essai_jouet_chaine_t08_v1.py --dossier <neuf> --horodatage 20261122-120000 --entropie 12345 --nom a`),
refaire les pièces v3 si le commit change, et répondre à la mère. Sans constat : rien, la mère scelle.
