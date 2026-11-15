# État des corrections v3 (brouillon 6, code v3) — EN COURS, v1

**Déclaration** : arrêt propre demandé par la mère (changement de compte de Lazar). Même développeur que
`corrections-controle-attention-v1.md` ; commande R-2919 après `contre-lecture-brouillon5-et-code-v2-v1.md` (`93b0724d…`).
Processeur seul, aucune machine, aucun appel payant ; rien sous `diag/`, `donnees/`, `docs/verdicts/` ; aucun fichier existant
modifié (R12). Date (UTC) : 2026-11-15. Branche `prep/t07bbis-code-v1` : code et brouillon 6 au commit `6c346a03` (parent
`b57a5f47`, poussé) ; cette note et la sortie des essais : commit suivant. **Le rapport `corrections-controle-attention-v2.md`
n'est pas écrit** (brouillon dans le bloc-notes, perdu avec lui).

## Fait et reste, par point de la demande

1. **M2, voie (b)** — FAIT. `validation_imbriquee_v3` : sonde de contrôle en échec (3 ou 300 époques, déterminisme compris) →
   arrêt (erreur de chaîne) ; couple tiré à la fin de l'apprentissage parmi les sondes finales finies, même ordre trié, même
   graine `bbis/egalite-carte` (égal à la v1 si toutes finies) ; aucun → arrêt ; aucune clé `sans_objet`. `marche_v3`,
   `scripts/amorce_bbis_v3.sh`, `scripts/lancer_bbis_v3.sh`. Brouillon 6 : couples c2 (point 5), c5 (liste d'arrêt), c7, c10.
2. **M1** — FAIT. `lecture_v2` : R-PILE (phrase du brouillon), point (7) de la section D, lecture de `controle_carte_processeur`
   (« sans objet », absent, non numérique, > 10⁻⁴, déterminisme absent → arrêt de la lecture). Liste de la fiche
   `fichiers-fiche-code-bbis-v3.txt` : 103 chemins (`b8fb095b…`). Couple c8.
3. **m1** — FAIT. `scripts/repetition_carte_bbis_v3.py` (lot neuf `ac.LotCarte(seqs, appareil)`, égalité au premier lot écrite,
   pic mémoire carte), amorce et lanceur de la répétition v3 ; branche de sortie `calcul/t07bbis-repetition-v4`, absente à
   distance (`git ls-remote` : 0).
4. **m8 et m3** — FAIT. Règle de lecture écrite avant la passe au texte (c4) et au script (`lecture_de_la_passe`, au fichier de
   sortie et au résumé de l'amorce) : compte si chaque famille ≤ 10⁻⁴ et égalités au bit près, sinon code 9 ; ≤ 10⁻⁵ pour
   chaque famille : sans nœud ; entre les deux : nœud écrit à la mère.
5. **m2** — FAIT. `MIN_ESSAIS=115` = passés de l'arbre de l'instance simulé (115 passés, 24 sautés).
6. **m4 à m7, m9** — FAIT. m4 : listes d'actions comparées à la v1 ; m5 : c1 ; m6 : c3, c6 ; m7 : `dd67802d…` en c4, c6 ;
   m9 : suffixe unique v4 (branche, traces, dossier de l'instance, étiquette).
7. **Incident** — FAIT. `conftest.py` neuf à la racine : retire `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_COMMON_DIR`,
   `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES` et `GIT_CONFIG*` dès l'import ; preuve
   `tests/test_essais_git_propres_bbis_v1.py` (sous `GIT_DIR` vers un témoin, rien ne bouge ; artefact : sans garde, il bouge).

**Reste** : le rapport `corrections-controle-attention-v2.md` (différentiel par fichier : 64 couples sur huit fichiers, dans
`tests/aide_t07bbis_differentiels_v3.py`) ; la contre-épreuve complète des autres essais du dépôt sous la garde (ci-dessous).

## Essais (sortie : `essais-sortie-corrections-controle-attention-v2.txt`)

- Suite de B bis au commit `6c346a03` : **183 passés**, 0 échec, 0 sauté (155 avant ; 28 neufs : 17 + 8 + 3), 2050 s.
- Arbre de l'instance simulé (motifs de l'amorce v3 ; 336 fichiers, identiques au bit près au commit `6c346a03`) :
  **115 passés, 24 sautés** (sautés nommés : chaîne de T0.6 et pièce « mots et coût » absentes de l'extraction) ; minimum 115.
- Autres fichiers d'essais qui lancent git (75 fichiers, 4058 essais), sous la garde : **incomplet** (69 %, borne de temps) ;
  9 échecs vus ; contre-épreuve sur quatre fichiers : mêmes 4 échecs avec et sans la garde (arbre de travail hors du chemin du
  dépôt principal, état vivant des autres sessions), et les 5 premiers échecs passent seuls dans les deux cas. Aucun échec
  attribué à la garde ; 4 échecs (trois fichiers « ideation ») non contre-éprouvés.

## Réserves

1. `conftest.py` de la racine vaut pour tous les essais du dépôt et retire aussi les `GIT_CONFIG*` de la session (réglages réseau
   de git) ; contre-épreuve complète non faite.
2. Tirage déplacé à la fin de l'apprentissage : autre tirage que la v1 si une sonde finale n'est pas finie ; après un arrêt de
   débit, aucun contrôle (aucun score écrit) ; lot du contrôle construit sur la carte en fin d'apprentissage.
3. « ≤ 10⁻⁵ pour chaque famille » lu sur l'écart du contrôle de chaque famille (linéaire à 300, attention à 3).
4. R-PILE compte la sonde finale d'ENC à réglage « attention- » (interprétation).
5. Suffixe v4 pour la passe, fichiers en v3 ; `memoire_carte_max_octets` est un pic, pas la taille du seul second lot.
6. Non éprouvé sans carte : écart à 3 époques sur la carte, égalité de deux lots construits sur la carte, déterminisme dans la
   marche, amorces et lanceurs v3 jamais joués sur une machine.

## Empreintes (commit `6c346a03`)

- brouillon 6 : `bf1be58e4be262b180e5ea952cafd7948942ff450614c901e97318500d874935`
- `pieces/couples-brouillon6-v1.py` : `b61ed1d32d5fef1b821eac4d6effe3b8d136f7498e126c5ef796fb05c0e03a57`
- `code/fichiers-fiche-code-bbis-v3.txt` : `b8fb095bf44dc855868e1b48cef6005222af6888b00a9df2f60fccc36ded7d5d`
- `src/controle_ia/t07bbis/validation_imbriquee_v3.py` : `71bffa5bf26c2b182bb81ebfb920c1246b6c9784b2332ff1304f0ff3c24890eb`
- `src/controle_ia/t07bbis/marche_v3.py` : `7009b34d46c33ed8fa4a5045d4ad93816c0948fd6dc165cb8f74e493b98f03f5`
- `src/controle_ia/t07bbis/lecture_v2.py` : `154795f4ecfa3273a7a5cec91c6975cd34e558d14647bb8a1cb1ef4968972aca`
- `scripts/amorce_bbis_v3.sh` : `18e2f2052efdca0d9d447738c3c4f1099302f7134b9518b59eea78ba563695dd`
- `scripts/lancer_bbis_v3.sh` : `dc26ea01a06bfb9eac3fc4f9f1b9b3bb86490d61d9e8f5deb54bcb180b17ee68`
- `scripts/repetition_carte_bbis_v3.py` : `355b313319d01f8a3f77cdd7603fd43b75ae1599bc079e03d9f93cf24f07e289`
- `scripts/amorce_repetition_bbis_v3.sh` : `cb489ebec9206afe2105512b2cda33f5265bbd8e4eb080a6521dc01d11348f48`
- `scripts/lancer_repetition_bbis_v3.sh` : `5bd32c146e0798b51a0a58753687fef75e0207b37a2e5949b0bddc39c80a758b`
- `conftest.py` : `8fe7cc46c35c13daf8dd87b34102522211024b8e9a2941ad9daeb8d3f8f44427`
- `tests/test_essais_git_propres_bbis_v1.py` : `e87f1bb983489dfb7316a68b46a9288f698df578b6dfe6a4d30c27b199e5962e`
