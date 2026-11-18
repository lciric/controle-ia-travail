# Rapport du développeur — corrections du code du saboteur à budget (ii-b), v4

Développeur : Claude Opus 4.6, session `session_013QMaymotDCL6zt3is8m3xe`.
Branche : `prep/iib-code-v3`, depuis `main` (branche v2 `prep/iib-code-v2` gelée, non ancêtre).
Contre-lecture de référence : `docs/notes/barreau8-iib-v1/contre-lecture-ordre-et-devis-iib-v1.md` (empreinte `d398bf5c4a7902b3821eab5879dfad1176b17adb2e50658166324e01ece22193`, sur `main` commit `a49963340`).
Rapport du développeur v3 reste archivé sous son nom (R12).

## Méthode

Branche `prep/iib-code-v3` depuis la tête `e2fbb612` (commit des corrections VC3-01 à VC3-07 et de la présente livraison). Les quatre points O-M1, O-M4, O-M5 et O-M6 de la contre-lecture d'ordre sont traités ci-dessous, chacun avec le changement réel (fichier:ligne) ou le rapport demandé. Aucun fragment de la consigne privée dans ce rapport.

## O-M1 — la clé de la ligne de progrès des épreuves portait un mot interdit du filtre du relais

**Constat.** `progres(etape="epreuves", echec=…)` émettait une ligne contenant `echec=`, qui correspond au motif interdit `echec` du filtre du relais de l'amorce (`MOTIF_INTERDIT`). La ligne n'était donc jamais relayée à la surveillance.

**Changement.** `src/controle_ia/iib/lanceur_v1.py:292` : la clé `echec=` est remplacée par deux clés qui ne portent aucun mot interdit — `etat=passees` ou `etat=arret` selon le résultat de l'épreuve, et `epreuve=aucune` ou `epreuve=<identifiant>` pour le détail. La ligne passe désormais les deux filtres du relais (motif de progrès bien formé, aucun mot interdit).

**Essais.** Deux essais ajoutés dans `tests/test_iib_amorce_v1.py` :
- `test_sain_ligne_de_progres_epreuves_passe_les_deux_motifs_de_l_amorce` : vérifie que les deux variantes de la ligne neuve (`etat=passees` et `etat=arret`) passent `MOTIF_PROGRES` et ne contiennent aucun mot de `MOTIF_INTERDIT`, les deux motifs étant lus directement depuis le fichier de l'amorce.
- `test_artefact_ligne_de_progres_avec_mot_interdit_retenue` : vérifie que l'ancienne forme (`echec=aucun`) est bien retenue par `MOTIF_INTERDIT`.

## O-M4 — les fichiers par phase sous `donnees/` n'étaient jamais poussés (ignorés par git, absents de la liste de forçage)

**Constat.** Les fichiers par phase (`oracle-iib-*.json`, `ids-actions-iib-*.npz`, `textes-actions-iib-*.jsonl` et leurs empreintes) écrits dans `donnees/<run>/` n'étaient pas couverts par la liste de forçage `ajouter_legeres` de l'amorce. Comme `donnees/` est dans le `.gitignore`, ces fichiers restaient invisibles à `git status --porcelain` (sans `--ignored`) et au contrôle de fin de run.

**Changements.** Trois corrections dans `scripts/amorce_instance_iib_v1.sh` :

1. `ajouter_legeres` (`:261-265`) : six motifs par phase ajoutés à la boucle de forçage — `donnees/*/oracle-iib-*.json`, `donnees/*/oracle-iib-*.json.sha256`, `donnees/*/ids-actions-iib-*.npz`, `donnees/*/ids-actions-iib-*.npz.sha256`, `donnees/*/textes-actions-iib-*.jsonl`, `donnees/*/textes-actions-iib-*.jsonl.sha256`.

2. Contrôle de fin de run (`:442-448`) : `git status --porcelain` remplacé par `git status --porcelain --ignored` dans la vérification qu'aucun fichier ne reste hors du dépôt avant la fin normale. Un fichier ignoré restant déclenche une consignation de rattrapage, puis une fin anormale si le rattrapage échoue.

3. Les trois chemins de consignation (fin de run `:419-420`, arrêt consigné `:290-291` via `:347`, minuterie `:291` via `:302`) appellent tous `consigner_partiel` qui appelle `ajouter_legeres` : les fichiers par phase sont couverts dans les trois cas.

**Note sur le rapatriement et la suspension de destruction.** Le rapatriement des fichiers et la suspension de la destruction de l'instance en cas de fichier manquant relèvent de la session mère (pas de l'amorce). L'amorce fait sa part : les fichiers sont désormais poussés vers le dépôt distant, et tout oubli est détecté par le contrôle de fin. La suspension de la destruction en cas d'échec de la consignation est déjà présente : `fin_anormale` appelle `arreter_instance "fin anormale" 1`, qui en mode essai consigne l'arrêt et sort avec le code 1 (sans détruire).

**Essais.** Deux essais ajoutés dans `tests/test_iib_amorce_v1.py` :
- `test_sain_fichiers_par_phase_pousses_malgre_gitignore` : un bac à sable avec `donnees/` dans le `.gitignore` crée des fichiers par phase (via un faux python qui génère `oracle-iib-etalonnage.json`, `ids-actions-iib-etalonnage.npz`, `textes-actions-iib-etalonnage.jsonl` et leurs empreintes). Le run se termine normalement (code 0) et les fichiers par phase sont présents dans le dépôt distant (`git ls-tree`).
- `test_artefact_controle_de_fin_voit_les_fichiers_ignores` : un bac à sable avec `donnees/` dans le `.gitignore` crée un fichier orphelin (`fichier-orphelin-hors-patron.txt`) qui ne correspond à aucun motif de `ajouter_legeres`. Le run échoue (code ≠ 0), le journal porte une erreur de chaîne ou une fin anormale, et le marqueur de fin normale n'existe pas.

Le marqueur `--porcelain` a été ajouté à la liste `MARQUEURS` du diff borné (`test_difference_avec_la_v11_bornee_aux_changements_declares`) pour couvrir le passage de `--porcelain` à `--porcelain --ignored`.

## O-M5 — espace disque au moment du clonage : rapport

**Demande.** Rapporter ce que le code exige en espace disque au moment du clonage de l'instance.

**Rapport.** Le clonage de l'amorce (`scripts/amorce_instance_iib_v1.sh:226-238`) utilise un clonage partiel sans objets larges (`git clone --filter=blob:none --no-checkout`) suivi d'une extraction partielle (`sparse-checkout`). La liste des chemins extraits (`CHEMINS_CLONAGE`, `:206-225`) couvre : `.claude/`, `src/`, `tests/`, `scripts/`, `pyproject.toml`, `requirements-*.txt`, `prereg/`, une extraction de données de référence (`donnees/20261007-082440-t05-extraction/`), les registres (`registres/*.md`), les documents (`docs/*.md`, `docs/*.txt`, `docs/*.sha256`, `docs/notes/`, `docs/sources/invites-*/`), les brouillons du saboteur à budget (`brouillons/ii-b-saboteur-budget-v1/`), et les artefacts de runs précédents du saboteur à budget (`diag/*-iib-*/`, `runs/*-iib-*/`, `donnees/*-iib-*/`, `traces/iib-*/`).

L'espace disque effectif est la somme de :
- Le répertoire `.git` filtré (métadonnées seulement, pas de blobs non demandés) : variable selon le nombre de commits et d'objets d'arbre. Le code mesure et rapporte cette taille (`CL_GIT`, `:237`).
- L'arbre de travail extrait (les fichiers des chemins de `CHEMINS_CLONAGE` seulement) : le code mesure et rapporte cette taille (`CL_ARBRE`, `:237`).
- Le débit et la durée sont aussi rapportés (`:238`).

Le code ne fixe aucun seuil d'espace disque minimal en entrée — il ne vérifie pas l'espace libre avant le clonage. L'échec de clonage (`refus "clonage impossible"`, `:227`) est le seul garde-fou (le clonage échoue si le disque est plein). La taille réelle dépend de l'état du dépôt au moment du lancement. Aucune modification de code proposée : le code mesure et rapporte l'espace consommé, ce qui suffit à diagnostiquer un problème de disque après coup.

## O-M6 — temps calendaire pour la création : rapport

**Demande.** Rapporter ce que le code exige en temps calendaire pour la création de l'instance.

**Rapport.** Le code impose trois contraintes de temps calendaire :

1. **Fin du GO** (`FIN_GO_UTC_S`, `:128-129`) : un entier (secondes depuis l'époque Unix) lu depuis la variable d'environnement, obligatoire. L'échéance de la session est ramenée à cette valeur si elle la dépasse (`:150`).

2. **Échéance de la session** (`ECHEANCE_UTC_S`, `:148-149`) : un entier (secondes depuis l'époque Unix), obligatoire. Persistée dans `$R/iib-echeance.txt` (`:146-152`). La minuterie (`iib-minuterie.sh`) surveille cette échéance et arrête l'instance à son dépassement.

3. **Heure d'épuisement du plafond de dépense** (`DEPENSE_EPUISEE_UTC_S`, `:153-156`) : un entier, obligatoire. Si l'heure courante dépasse cette valeur au démarrage, un marqueur est posé (`:158-160`) et l'instance sera arrêtée.

4. **Calendrier de la configuration** (`:323-326`) : `session_v3.calendrier` lit la date de fin du GO depuis la configuration scellée et la compare à `FIN_GO_UTC_S` ; toute divergence est un refus.

Le code ne fixe pas de durée minimale de création ni de durée de session. Les trois variables (`FIN_GO_UTC_S`, `ECHEANCE_UTC_S`, `DEPENSE_EPUISEE_UTC_S`) sont toutes calculées par la session mère au moment de la création de l'instance, à partir du GO en vigueur et du plafond de dépense de la configuration. Le clonage est borné à 900 secondes par `timeout` (`:227`). Aucune modification de code proposée.

## Comptes

- Essais ciblés du saboteur à budget : 424 réussis sur 424 (13 fichiers d'essais).
- Répétition jouet : identique à l'octet (4 fichiers comparés, hors identifiants de run et horodatages de création ; entropie 20261114, deux runs `repa` et `repb`).
- Aucune fuite de fragment privé dans le code, les essais, les rapports ni les messages.
