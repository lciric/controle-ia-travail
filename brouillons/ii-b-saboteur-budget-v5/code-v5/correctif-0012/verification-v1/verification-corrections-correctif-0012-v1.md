# Vérification des corrections du correctif 0011 (correctif 0012) — v1

Écrite le 2026-11-21 par un vérificateur neuf (Claude Opus 5.5, côté saboteur), sous le mandat `registres/iib-reconception/mandat-verificateur-correctif-0012-v1.md` (f997001635d9…, vérifié). Pièce de classe B. Écart déclaré à GO-2026-11-21-84 (vérificateur Opus au lieu de Fable), repris du mandat.

## Verdict : conforme
Toutes les remarques de Fable sont traitées : les majeurs 1 et 2, et les mineurs 3 à 10. Les preuves rejouées sont justes. Les deux écarts déclarés sont acceptables. Le correctif 0012 ne touche aucun code de production. Il reste trois observations, non bloquantes ; aucune ne demande de correction (section « Observations »).

## Arbre
J'ai appliqué les correctifs 0011 (947e5a49…) puis 0012 (4cd18c1f…) sur la base 62356e2f (arbre ed9b0e48, recopié à l'identique). J'obtiens l'arbre 95e102f9 après le 0011 et l'arbre **bbcd9a84a77ac667ef6f9106b19afe29ffab041f** après le 0012, comme attendu. Le 0012 touche trois fichiers, tous sous `tests/`, et ne change rien sous `src/` ni sous `scripts/` (`sorties/rejeu-majeur-1-et-perimetre-v1.txt`).

## Remarque par remarque
- **Majeur 1, le nom `cf`.** Conforme.
  - « cf » n'est plus que le nom local de `verifier_config`.
  - Aucun code n'emploie `session_v5.cf`, ni ne l'importe ou le lit par `getattr`. Les seuls importeurs sont le lanceur de session et deux fichiers d'essais.
  - ruff et flake8 (règles F) ne relèvent rien.
  - La sous-commande `config`, jouée sans numpy, échoue avec « No module named 'numpy' » (code 1) sous `/usr/local/bin/python3` et sous `/usr/bin/python3`, avec `-I -S -B` et un environnement réduit.
  - La branche `surveillance` ne passe à `$SESSION` que `coupure-etalonnage` ; la garde de dépense, elle, passe par `$SESSION3`. L'essai neuf porte bien un artefact.
  - Rendus : `sorties/rejeu-config-sans-numpy-v1.txt` et `sorties/rejeu-majeur-1-et-perimetre-v1.txt`.
- **Majeur 2, le paramètre `carte`.** Conforme.
  - L'extrait de la preuve correspond au fichier : `lanceur_v5.py` (36c39fe3…) est identique à la base.
  - `_main` appelle `executer` sans `environnement` ni `carte`, et aucune option de la ligne de commande ne les remplace.
  - `carte_visible` n'a que deux signaux, `nvidia-smi` et torch, ce qui lève la réserve 5 de Fable.
  - Ma recherche indépendante ne trouve aucun `carte=False` ni aucun `CUDA_VISIBLE_DEVICES` sous `src/` et `scripts/`. Les clés `"carte"` qu'elle relève appartiennent à des dictionnaires sans rapport avec la garde.
  - L'assertion statique éprouve son détecteur sur sept artefacts et quatre cas sains.
  - Rendu : `sorties/rejeu-majeur-2-v1.txt`.
- **Écart du majeur 2 (dossier des moniteurs non lu) : acceptable.** Ce dossier n'existe pas dans l'arbre bbcd9a84, ce que j'ai vérifié par son seul nom. L'écart n'a donc aucun effet à ce commit.
- **Mineur 3 : écart acceptable.** Les essais 1 et 2 sont renommés « non-régression de la garde », et la documentation le dit. L'essai 4 reste celui qui échoue sans la correction.
- **Mineur 4 : conforme.** Le cas sain de même forme est ajouté : `phase_etalonnage` et `phase_course` avec `carte=False` seul, sous accord posé. Il passe.
- **Mineur 5 : conforme.** La variante appelle le `python3` trouvé sur `/usr/local/bin:/usr/bin:/bin`, et l'essai échoue sans repli si ce `python3` manque. La documentation est rectifiée.
- **Mineur 6 : conforme.** L'essai pose un environnement explicite (`PATH` du système, `LANG=C.UTF-8`) et décode en `encoding="utf-8"`.
- **Mineur 7 : conforme pour le code.** `PYTHONPATH` est posé et `PYTEST_ADDOPTS` est retiré. Je n'ai pas rejoué la vérification de la liste des paquets de la machine : sa source est sous `traces/`, qui m'est interdit. La réserve du développeur (48 paquets sur 72 non lus) reste ouverte.
- **Mineur 8 : conforme.** Toutes les variables `IIB_*` sont filtrées, ce que l'essai 2 vérifie. Le commentaire est rectifié, et l'hypothèse d'un `git` binaire autonome est écrite.
- **Mineur 9 : conforme.** Aucun 271 par défaut ne reste dans l'amorce, le lanceur de session, `session_v5` ni `lanceur_v5`. La répétition porte 275. Le 271 qui reste dans les ordres d'étalonnage (brouillons 3 à 8) est renvoyé à la mère ; ce renvoi est acceptable, car ces ordres sont hors du code (`sorties/rejeu-mineurs-9-10-v1.txt`).
- **Mineur 10 : conforme.** Les treize identifiants sont donnés et chacun existe une fois dans l'arbre. Le nombre de fonctions d'essai ne change pas entre 0011 et 0012 (24 dans les deux fichiers modifiés).

## Essais rejoués (arbre bbcd9a84, `PYTHONPATH=src`, sans `PYTEST_ADDOPTS`)
- Les quatre fichiers d'essais touchés (environnement de la machine, lanceur, distillateur de bout en bout, configuration) : **54 passed**, code 0 (`sorties/essais-fichiers-touches-verificateur-v1.txt`).
- La liste figée `scripts/tests-cibles-iib-v5-v5.txt` (f9ff477d…, 24 fichiers) : **275 passed in 469.21s**, code 0 (`sorties/liste-figee-verificateur-v1.txt`).

## Observations (non bloquantes)
1. **Mineur 5.** Sur le poste, le `python3` trouvé en tête du chemin est l'interpréteur des essais lui-même (3.13.18). La variante du système n'y ajoute donc rien de plus que la variante `-I -S -B`. Elle ne prend son sens que sur la machine.
2. **Majeur 2.** Si le dossier des moniteurs revenait dans l'arbre, `rglob` en énumérerait les noms avant le filtre, sans en lire le contenu. Il vaudrait mieux l'élaguer avant d'y descendre.
3. **Majeur 2.** Le détecteur s'en tient à la lettre de Fable : il cherche le littéral `carte=False`. Une forme comme `**{"carte": False}` lui échapperait. Aucune occurrence de cette forme n'existe aujourd'hui.
