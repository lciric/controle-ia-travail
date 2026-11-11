# Mesure de `ATT` de T0.7 au commit C7 — v1 (EN COURS, rapport écrit au fil de l'eau)

Sous-agent neuf, mandat unique de la mère (2026-11-11) : mesurer la ligne d'essais `ATT` de T0.7 au commit C7 selon le § 11 bis
de l'ordre `docs/procedures/ordre-execution-etape-a-t07-v1-brouillon8.md` (`24dc8df6555bac03f2ffbe8440c3c1a7b9bf2aeaf9eab3c651306a6a73fc116e`,
compagnon vérifié). Décisions lues : R-2313 à R-2316 de `registres/decisions.md` (ces lignes seulement).

## 1. Repères vérifiés avant la mesure (2026-11-11, 05:41 à 05:45 UTC, `date -u`)

- Ordre brouillon 8 : empreinte égale au compagnon (`24dc8df6…`).
- C7 = `b4cd9953d199dd8f220f5162e5868c5b00fd392d` (R-2316).
- Script `scripts/etape_a_t07_variante_b_v4.sh` lu **au commit C7** (`git show C7:…`) : `4b17d1f05441f5206d9f4ac58fb5ccf2b755bd86c13bee622ccf3bc327df05c6`
  (égal à R-2313 et à la copie de l'arbre de travail ; **aucun compagnon `.sha256` du script sur disque**, R11 : vérifié par la liste de `scripts/`).
- Configuration v8 : `docs/notes/g0-deux-semaines-v1/t07-module-v2/plancher-v3-pieces-v1/configuration-t07-v8.json`,
  `e31c7a79dc1b68d561874d4d42d63b5eb950931f06075927f239c7ad971fb328` (égale au compagnon, et égale à l'objet de ce chemin à C7) ;
  chemin final prévu `prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json` **pas encore copié** : les chemins cités sont tirés du fichier
  sous `docs/notes/…` (écart déclaré, § 4).

## 2. Bac et méthode (commande de remesure du § 11 bis, tête à C7)

Bac neuf (vide à 05:45:28 UTC) : `/tmp/claude-0/-home-user/1cc16375-a2bd-54b9-a03f-27d43b6f26a6/scratchpad/agents/mesure-att-c7/`
(noté `<bac>`) ; clone `<bac>/d`. Chaque étape est un petit script du bac qui **source, telles quelles, les lignes du script v4 de C7**
(extraites par `sed -n` de la copie `4b17d1f0…`), avec un journal horodaté `<bac>/journal-mesure.txt`. Scripts et extraits (empreintes) :

| pièce du bac | rôle | sha256 |
|---|---|---|
| `etape2.sh` | clone, puis lignes 132-169 du v4 | `9d4c2d7219ea3cc555aa775beca2d99ee46356ef815998b79cd2a74add013d64` |
| `etape2-lignes-132-169.sh` | `REGISTRES`, `MOTIFS`, `NOMMES`, `CITES`, extraction partielle, `checkout`, gardes | `d0cdb9c623f849a03da211b2a004ed16adf05fe929c2bdc5f258236622331373` |
| `etape3a.sh` | lignes 171-181 (recopie des registres nommés), liste des chemins cités, sans recopie | `629318057d22827033b84ab480dcf810c375a422580c650b8b060e31b3cf31ac` |
| `etape3-lignes-171-181.sh` | `interdit`, `apporter`, boucle des registres | `18f68eb12cf957f89854aea5cda32a43a673c59ef38f32530a9dc7930ca9b343` |
| `etape3b.sh` | lignes 171-181 puis 182-198 (cités, périmètre, journaux des jeux) | `f5d208a0537a78f38c47228ebaee884f82b5bedaaeed4f7e62b0e26dc4ce2dce` |
| `etape3-lignes-182-198.sh` | fichiers cités, périmètre C-1, journaux, `src/` `tests/` inchangés | `02bf7a42c58888cd137869892a249da1e8027fdf0d89febe115f2061c4b4e064` |
| `motifs-extraction.txt` | les 38 lignes passées à `sparse-checkout set --no-cone --stdin` | `56041134cc67c00233540bea1428c4a2d327531d0a070a3e15edb1b7c3fa272a` |
| `cites-registres.txt` | 5 chemins cités par les registres (awk de la ligne 182) | `70ff1e79a07d37132d29cbaef5070e26086578e8c4ebcd7f7341049bed3db660` |

### Étape 2 (05:46:16 à 05:46:20 UTC)

- Commande de clone (depuis `<bac>`) : `git clone -q --filter=blob:none --no-checkout --single-branch --branch main https://github.com/lciric/controle-ia-travail.git d`
  (git 2.43.0 ; aucun jeton posé : le mandataire de la session porte l'accès). Vérifié : `remote.origin.promisor = true`,
  `partialclonefilter = blob:none`, refspec `+refs/heads/main:refs/remotes/origin/main` (seule `main`) ; 3 081 commits atteignables depuis C7.
- `origin/main` = **H = `5d6ef6f567dcee5f73ec71ee67ea4cdbb1a3403d`** (deux commits après C7 : `a84be34d` CODE-T07-v2, `5d6ef6f5` pièces du candidat 5).
- Configuration lue par la ligne 150 (`git show "$S7:$CONFIG"`), `S7 = C7`, `CONFIG` = le chemin sous `docs/notes/…` ; objet à C7 contrôlé égal à `e31c7a79…`.
- Lignes 162-169 jouées : extraction partielle, `git checkout -q b4cd9953…`, gardes « tête = S7 », « C7 ancêtre de S7 », `git diff --quiet C7 S7 -- src tests`,
  « S7 ancêtre de main » : **toutes passées** (« code conforme »). `S6` (`935262b1…`) absent du clone à branche unique : contrôle des exigences de paquets sauté (comme sur l'instance si `S6` n'est pas atteignable depuis `main`).
- Résultat : 2 281 fichiers extraits, 139 Mo ; 24 fichiers `tests/test_t07_*.py`.

### Étape 3 (05:47:00 à 05:47:38 UTC)

- Registres nommés depuis H : `registres/scellements-v1.md` (`a399031d21200e3ea28b06964592a601dc3f59e6851bc60311cb7cfa4e9dc392`) et
  `registres/go.md` (`b4fa7480c071e6e9b00ceb5d42506792db780ee72040b8daca786e8c535b74db`) recopiés avec leurs compagnons ;
  `registres/scellements-v1.md.ouvertures.md`, `registres/ouvertures-p3bis-v1.md`, `registres/prealables-p3bis-v1.md` : **absents de main** (journal du script) — rien de P3-bis n'est donc recopié.
- Chemins cités (5), **classés avant toute recopie** contre les interdits du script (ligne 171), les chemins de 7a (`20261109-070232-t06-reel`) et les
  interdits du mandat (dont P3-bis, l'étiqueteur, `mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`) : **aucun ne tombe dans un interdit** ; tous présents à H avec compagnon :
  `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon4.md`, `donnees/t07-jeux-synthetiques-v2/dissimulation-v2.jsonl`,
  `donnees/t07-jeux-synthetiques-v2/intention-autres-modes-v2.jsonl`, `prereg/T0.8-base-A-mots-et-cout-v1.md`, `registres/code-t07/CODE-T07-v2.json` (non suivi à C7, `d5eb0b66…`).
- `RUN6` : aucune course 7b ; tenu par l'identifiant du run de 7a pour que la ligne 183 écarte ses chemins (sans effet : aucun cité).
- Périmètre (C-1), `PERIMETRE=JD,JA` : `SCELLEMENT-JEUX-T07-JD` 1 ligne, `-JA` 1, `-JC` 0, `SCELLEMENT-CONCEPTS-T07` 0 : **conforme**, aucun arrêt ;
  journaux du script : un seul fichier, `donnees/t07-jeux-synthetiques-v2/journal-verification-v2.txt` (`58906bb4…`, conforme à son compagnon),
  commun aux deux jeux (même dossier ; compté « 1 » pour chacun).
- Contrôles : fichiers recopiés et fichiers cités par la configuration v8 (6 chemins : `diag/20261019-230011-p3-reel/sondes-figees.json`,
  `donnees/20261007-082440-t05-extraction/taches-entrainement.json`, `donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz`,
  `donnees/T0.7-faits-repe-v1/facts_true_false.csv`, `donnees/T0.7-models-under-pressure-v1/training/train.jsonl`,
  `runs/20261019-230011-p3-reel/manifeste.json`) **tous égaux à leurs compagnons** ; `src/` et `tests/` inchangés (ligne 197) ;
  arbre après l'étape 3 : ` M registres/scellements-v1.md` (registre de H ≠ C7), `?? registres/code-t07/CODE-T07-v2.json` et son compagnon.

### Étape 6 (lancée à 05:48:24 UTC)

- Liste : `sha256sum tests/test_t07_*.py` → 24 fichiers, `f030758e45861732947cbf00f27350f96bba65fce331f8bb51479e283a9e9e74`
  (locale vide : `LANG`, `LC_ALL`, `LC_COLLATE` non posées ; ordre du motif identique en locale C, contrôlé).
- Commande, depuis `<bac>/d` : `TZ=UTC PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src /home/user/controle-ia-travail/.venv/bin/python -m pytest -q -rsxX -p no:cacheprovider --color=no tests/test_t07_*.py --basetemp=<bac>/essais-tmp -o tmp_path_retention_policy=failed`
  (sortie `> <bac>/essais.txt 2> <bac>/essais.err`), puis `tail -n 1 | sed -E 's/ in [0-9.]+s.*$//'`.
- Interpréteur : **Python 3.13.16** (`/home/user/controle-ia-travail/.venv`), `numpy` 2.4.6, `scipy` 1.17.1, `pytest` 9.1.1, `torch` 2.14.1+cpu
  (égaux aux versions figées de `requirements-cpu.txt`) ; aucune installation éditable de `controle_ia` dans l'environnement (seul `PYTHONPATH=src` du clone).
- **Python 3.11** : `/usr/bin/python3.11` (3.11.17) est présent mais **sans les paquets** (`numpy` absent) ; aucun environnement 3.11 muni d'eux trouvé
  (dossiers d'environnements du bac à sable regardés : 3.13 seulement) : **pas de rejeu sous 3.11** ; rien installé (disque, mandat).

(suite écrite au fil de la mesure)
