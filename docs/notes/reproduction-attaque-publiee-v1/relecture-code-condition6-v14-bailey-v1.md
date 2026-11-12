# Relecture du code v14 du témoin de Bailey (lanceur_v14, instance_v13) — message d'erreur d'une exécution morte avant tout tour

- **Qui** : relecteur neuf (règle R2), sous-agent qui n'a écrit aucune des pièces relues.
- **Quand** : 12 novembre 2026 (soir, UTC).
- **Commit lu** : `4821ad7ef562748be092ec00ae6665795ae1a886`. Pendant la relecture, la branche a avancé à `1f15e43e`
  (addendum 3 en brouillon, scripts de lancement) ; `git diff 4821ad7e` est vide pour tous les fichiers relus ci-dessous.
- **Routine de reprise** : non exécutée (consigne). Aucune instance, aucun appel réseau, aucun `git push`, aucun fichier
  cloisonné ouvert.

Fichiers lus (SHA-256) :

| Fichier | Empreinte |
|---|---|
| `src/controle_ia/temoin_bailey/instance_v13.py` | `62686ac11dbba382b97cd16c94f5280570f783d9329f8dcb3a7fc78776d20032` |
| `src/controle_ia/temoin_bailey/instance_v12.py` | `de46698656b56cc52389c6150af50da7d4aa6ac5120e78561bc2db1b6155086d` |
| `src/controle_ia/temoin_bailey/lanceur_v14.py` | `02e9816a64160cea5a38f2c4cb10612d94f9ee6a8712c6da59684528f32fc101` |
| `src/controle_ia/temoin_bailey/lanceur_v13.py` | `9257266f31d1f6f915b24db5dc66d5e9a7c7404b517c8980294de83241181185` |
| `src/controle_ia/temoin_bailey/execution_v3.py` | `279f1f4f6e04fad67db457831abdba712d16feb15571c24173988af9a1a58a5f` |
| `src/controle_ia/temoin_bailey/lecture_v8.py` (passages) | `1657a492d7229a9f3cd37c2094a012cf2cb629d8e7e6b91632895586e9d9a00a` |
| `src/controle_ia/temoin_bailey/conventions_v3.py` (passages) | `51c2fa26a4e61038b14c97825618e2006be9572c9f82d67a2d5e26bea2bbca86` |
| `src/controle_ia/temoin_bailey/analyse_v3.py` (`garde_fin_de_run`) | `c28c6821629a6d4eec657c376a3df2d5361de2e46c4441361f43e0e8f423f2ca` |
| `tests/test_temoin_bailey_condition6_v14.py` | `6f4809a5f8107d77df59aaeaa95297e134c7861da322cf12808a4e68325d7ba9` |
| `prereg/temoin-attaque-publiee-bailey-v1.md` (écart 2, Pilote, Gardes, Ce qui sort, Liste d'arrêt) | `fb6c2f34355d98ba08798cab1a4964a03b41eedf57d687454663f01c9646f2c3` |
| `prereg/temoin-attaque-publiee-bailey-v1-addendum-2-condition6-arret-autonome.md` (passages) | `f79459c712a0f12ecbf55c9ea787f67032031e9672e6db002b84725286c96e13` |
| `registres/passations/2026-11-12-1545-temoin-bailey-pilote-seconde-chute-noeud.md` | `21f0fc4d48a135a9a016e81d9a4ce91aed948952d91a5517d39f1dd609dec72b` |
| `registres/passations/2026-11-12-1720-decision-lazar-bailey-option-a-v14.md` | `df3833a9d773d6b7b5daf36d1662a547cc24b90bfc0204ce7b4ef00fc5c32be2` |
| `docs/notes/reproduction-attaque-publiee-v1/contre-lecture-3-prereg-temoin-bailey-v1.md` (l. 83-93 : ordre de `train_harmful.py`) | `30147d3cbd7df65f9d033ffb3dc848dc953e00345f30c96098d1860071114231` |

Essais : `PYTHONPATH=src python -m pytest -q tests/test_temoin_bailey_condition6_v14.py` : **146 passés, 1 échoué**
(`test_v13_P2_processus_reels_veilleur_arrete_autre_pid_jamais_signale`), 157,6 s. Le même essai seul : 1 échec sur 6.

## Verdict

**Conforme après corrections.** Aucune fuite trouvée dans le cas qui a motivé la v14 (mort à l'import ou à la
composition de Hydra). Mais la garantie écrite (« aucune note, aucun texte… ») n'est pas tenue par la condition seule
(R-2), et le filtre retire justement les lignes qui diraient la cause (R-1). Le défaut `signal` est réel et bien corrigé.

## Points

### R-1 — à corriger (prioritaire, avant l'addendum 3) — filtre excessif : il retire les lignes qui nomment la cause

`instance_v13.py` l. 216 et l. 234. Le motif `-?\d+\.\d+` retire toute ligne qui contient un nombre décimal. Or sur
l'instance, Python vit dans `/root/venv` (`lanceur_v14.py` l. 1057) : **chaque cadre de trace d'une bibliothèque**
porte `/root/venv/lib/python3.11/site-packages/…`, donc il est retiré. Essai fait sur un message type :
- retirées : `File ".../python3.11/site-packages/sparsify/__init__.py", line 3` (l'hypothèse de tête de la note
  `2026-11-12-1545`, addendum 2 l. 43) ; `ImportError: cannot import name 'X' from 'transformers' (/…/python3.11/…)` ;
  `torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.96 GiB…` ; tout numéro de version ;
- gardées : `ModuleNotFoundError: No module named 'triton'`, `OSError: [Errno 28] No space left on device`, les cadres
  de `train_harmful.py`.

Le fichier dirait souvent le type de l'erreur, rarement d'où elle vient. Or la condition d'écriture garantit déjà
qu'aucune note n'existe (sous R-2). Le filtre est une défense en profondeur ; il ne doit pas détruire le diagnostic.

Correction proposée : remplacer la valeur sur place au lieu de retirer la ligne, et ne pas toucher aux chemins ni aux
versions collées à un mot. Par exemple :
`_VALEURS = re.compile(r"(?<![\w./-])-?\d+\.\d+(?![\w.])|\d{13,}")`, `l = _VALEURS.sub("‹valeur›", l)`, et pour
`tensor(` couper la ligne à partir de `tensor(` (`l[:l.find("tensor(")] + "‹tenseur retiré›"`). Garder la limite de 300
caractères appliquée **après** le filtre (c'est déjà l'ordre, à garder). Ajouter un essai sur des lignes de trace réelles
(chemin `python3.11`, `ImportError … (/root/venv/lib/python3.11/…)`, mémoire de carte) : il aurait montré le défaut.

### R-2 — à corriger — la condition ne garantit pas, à elle seule, qu'aucune note ni aucun texte n'existe

`instance_v13.py` l. 239-249 (et docstring l. 6-9). Ce que vaut chaque terme :
- `surv.demarrage is None` (l. 596-598) veut dire seulement : **moins d'octets reçus sur la sortie standard que la
  longueur de la configuration attendue**. Ce n'est pas « le script n'a pas passé la l. 173 ». Si le script imprime une
  configuration **différente et plus courte** et que rien d'autre ne sort sur la sortie standard, la garde n'est jamais
  décidée, l'enfant n'est pas arrêté, et il continue : chargement du modèle, sonde initiale, tour 0 (générations,
  notes, juge). La barre de progression (`tqdm`) et les avertissements vont sur la sortie d'erreur. Une mort à ce
  moment écrit le fichier. Le filtre retire les nombres, pas un texte sans chiffre (une ligne de génération imprimée
  par un avertissement ou une exception, par exemple).
- `complets == 0` ne prouve pas l'absence de tour : `tours_complets_instance` rend 0 si un journal manque ou est
  illisible (`lecture_v8.py` l. 350-353), et une dernière ligne coupée des gardes du lanceur retire tous les tours (A-1).
- code de retour non nul : rien à redire (un enfant tué par la dépense ou l'échéance a un code négatif ; c'est voulu).

Cas limites demandés :
- mort après une génération mais avant l'impression de la configuration : impossible dans l'ordre du script public
  (impression l. 173 avant toute construction, contre-lecture 3 l. 85-86 ; `execution_v3.py` ne fait qu'importer, semer
  et composer avant) **si** la configuration imprimée est la bonne. Possible seulement dans le cas « configuration plus
  courte » ci-dessus ;
- configuration imprimée en morceaux : sans effet (le tampon s'accumule, l. 597) ; une mort au milieu de l'impression
  donne `None`, et rien n'a été construit ;
- `surv.demarrage` à `None` alors que des tours ont commencé : seulement dans le cas « configuration plus courte » ;
- sortie d'erreur du juge ou d'une bibliothèque qui imprime des textes : le juge et la génération viennent après la
  l. 173 ; même réserve.

Correction proposée (deux lignes, garantie stricte) : n'écrire que si le texte reçu est un **préfixe** de la
configuration attendue (vide compris), ce qui prouve que l'enfant n'a pas fini l'impression de la l. 173 :
`and surv.attendu.startswith(surv.tampon)` (passer `surv` ou ce booléen à `ecrire_erreur_demarrage`). Ce n'exclut aucun
cas utile : si autre chose sortait avant la configuration, la garde de démarrage tomberait de toute façon. En plus, à peu
de frais : exiger `journal/notes-v3.jsonl` absent ou vide et les dossiers `sondes/` et `params/` vides. Essais : un
artefact « configuration plus courte, puis texte sur la sortie d'erreur, puis mort » (pas de fichier) et un cas sain
« moitié de la configuration, puis mort » (fichier écrit).

### R-3 — à préciser (addendum 3) — portée : morts après la configuration et garde de démarrage tombée

La v14 ne fait rien sortir si l'enfant meurt **après** avoir imprimé la bonne configuration et avant le tour 0
(chargement du modèle, mémoire de carte, disque, sonde initiale), ni quand la garde de démarrage tombe. Or la liste
d'arrêt (préenregistrement l. 370) promet, pour la garde de démarrage tombée, un « diagnostic borné au nom de la garde,
au message d'erreur… ». C'est un choix défendable (après la l. 173, des activations et des notes peuvent exister), mais
l'addendum 3 doit l'écrire : « le message ne sort pas pour une mort après l'impression de la configuration ». L'étendre
(par exemple sous la condition « journal des notes absent, sondes et paramètres vides ») serait un nouvel
élargissement de la liste fermée : nœud, à Lazar.

### R-4 — à préciser (addendum 3), et filtre à compléter — ce que le message peut contenir

Avant la l. 173, la sortie d'erreur peut porter : la ligne de Hydra « Error executing job with overrides: [...] »
(graine, K, chemins), et des fragments de configuration dans un refus de surcharge. Le texte (l. 316-317) dit que « la
configuration que le script imprime au démarrage n'en sort pas, seule son empreinte ». Ce n'est pas une fuite de note,
mais c'est un écart à la lettre : l'addendum 3 doit dire que le message peut contenir les surcharges et des morceaux de
configuration. Par prudence, et pour pas cher, ajouter au filtre un motif de jeton (`hf_[A-Za-z0-9]{20,}`) et de longues
suites alphanumériques (`[A-Za-z0-9_-]{40,}`, hors chemins) : le jeton Hugging Face est sur l'instance
(`/root/.cache/huggingface/token`) ; aucune bibliothèque connue ne l'imprime, mais rien ne l'empêche.

### R-5 — à préciser — le défaut `signal` : réel, ancien, corrigé ; deux masquages inoffensifs restent

- **Réel** : en Python, toute affectation dans une fonction (ici l'affectation annotée `signal: list[str] = []`,
  `instance_v12.py` dans `executer`) rend le nom local dans **toute** la fonction, dès la compilation. L'appel
  `os.kill(proc.pid, signal.SIGTERM)`, plus haut, lève donc `UnboundLocalError`. Reproduit sur `instance_v12.executer`
  avec un enfant qui imprime une fausse configuration : `UnboundLocalError: cannot access local variable 'signal'`.
- **Ancien** : la même ligne est dans `instance_v7`, `v8`, `v10`, `v11`, `v12`. Depuis la v7, les trois arrêts internes
  d'une exécution (garde de démarrage tombée, dépense B − 2, échéance) faisaient planter `executer` sans ligne `ETAT` ni
  état écrit, en laissant l'enfant vivre ; seuls le chien de garde et les veilleurs protégeaient. Le run du 12 novembre
  ne passait pas par ce chemin (l'enfant est mort seul). Les relectures v7 à v12 et leurs essais ne l'ont pas vu : à
  rapporter à Lazar (règle R4).
- **Correction complète** dans `executer` (`instance_v13.py` l. 740-748 ; plus aucun usage du nom local `signal`
  dans cette fonction). Analyse de syntaxe sur `instance_v13.py`, `lanceur_v14.py`, `lecture_v8.py`, `execution_v3.py`,
  `journaliseur_v3.py` : aucun autre masquage d'un module **utilisé** dans la même fonction. Restent deux masquages
  sans effet : `reconstituer_etat` (l. 790) et `main` (l. 1375), qui n'emploient pas le module `signal`. Les renommer
  `signaux` (même piège au prochain ajout).
- Essai manquant : l'arrêt de l'enfant par la dépense et par l'échéance (seule la garde de démarrage tombée passe par
  `os.kill` dans les essais v14). Ce même essai, avec un enfant qui n'imprime rien, doit écrire le fichier d'erreur
  (code négatif, garde non décidée).

### R-6 — à corriger — essais (R5) incomplets

`tests/test_temoin_bailey_condition6_v14.py` l. 3286-3376. Les huit essais couvrent le cas sain (mort à l'import), trois
artefacts (configuration imprimée, configuration fausse, code nul), le filtre, l'écriture sans sortie d'erreur, le
transfert et les modules. Manquent :
1. les branches `complets != 0` et `code_retour is None` de `ecrire_erreur_demarrage` (un appel direct suffit :
   `(…, 1, None, 1)` et `(…, None, None, 0)` → `False`, pas de fichier) ;
2. les deux essais de R-2 (configuration partielle ; configuration plus courte) ;
3. l'essai de R-5 (arrêt par la dépense ou l'échéance, enfant muet) ;
4. un essai du filtre sur des lignes de trace réelles (R-1) ;
5. une lecture (`lecture_v8.valider`, ou au moins `dossier_de_foi`, `journaux_scelles` et `garde_fin_de_run`) sur un
   dossier d'étape qui porte `erreur-demarrage-v1.txt` (voir R-8) ;
6. un artefact d'écriture qui échoue (dossier en lecture seule) : `False`, état écrit quand même.

### R-7 — à corriger (essai) — l'essai instable : confirmé, cause établie, pas grave pour la production

Confirmé : 1 échec dans le passage complet, 1 échec sur 6 en isolé (l. 3190 : `processus_vivant(pid)` encore vrai).
Cause établie par une sonde (40 cas sur 40) : après `SIGTERM`, `/proc/<pid>/cmdline` devient vide pendant que le
processus finit sa sortie (`State: R`), **avant** qu'il soit récoltable. `identite_veilleur_arret` (`lanceur_v14.py`
l. 973-991) lit alors « fini » ; `_arreter_veilleurs_precedents` (l. 2145-2186) note « arrêté par son PID » ; l'essai
appelle aussitôt `processus_vivant`, qui interroge `Popen.poll()` : pas encore fini. En production, c'est bénin : un
processus dont la mémoire est rendue n'exécute plus de code et ne peut plus appeler l'API. Correction : dans l'essai,
attente bornée (5 s) de `not la.processus_vivant(pid)` ; ou, dans `_arreter_veilleurs_precedents`, pour un veilleur
suivi par un `Popen`, `p.wait(timeout=5)` après l'identité devenue non vraie.

### R-8 — constat (aucune correction) — effets de bord sur la lecture, la reprise, le chien, l'état reconstitué

- **Transfert** : `transferer` (l. 1223) accepte `instance_v13.SORTANTS`, soit `cv.SORTANTS` plus le seul
  `erreur-demarrage-v1.txt` (essai l. 3369 ; `sortie-erreur-instance.log` refusé, l. 3367-3368).
- **Garde de fin de run** : elle exige l'égalité exacte `set(empreintes_instance) == set(NOMS_JOURNAUX)`
  (`analyse_v3.py` l. 429). Un dossier qui porte le fichier d'erreur la ferait tomber. Elle n'est appelée que si K′ ≥ 1
  (`lecture_v8.py` l. 579-584). Le fichier n'existe que si l'instance a compté 0 tour complet, par la même fonction
  (`k_prime(tours_journal(…))`) sur les mêmes journaux. Si les transferts diffèrent, la garde tombe déjà. Pas de
  conflit aujourd'hui ; fragile si l'une des deux règles change (d'où l'essai R-6, point 5).
- **Lecture** : `dossier_de_foi`, `journaux_scelles` (appelé avec les noms des empreintes), `_execution` acceptent un
  nom de plus ; la clé `erreur_demarrage` de l'état est ignorée.
- **Chien de garde, reprise, état reconstitué** : ils appellent la même fonction `empreintes` (l. 767-774, `SORTANTS`) ;
  `reconstituer_etat` n'écrit jamais le fichier ; une exécution arrêtée par le chien avant la fin d'`executer` n'a pas de
  fichier (limite naturelle) ; `empreintes --si-absent` garde les empreintes prises avant l'arrêt.
- **Archive envoyée** : aucun import nouveau dans `instance_v13` (`re` déjà importé) ; `CHEMINS_ARCHIVE` passe à
  `instance_v13.py` (essai l. 3372-3376).

### R-9 — constat (aucune correction) — le diff du lanceur

Le diff normalisé (`sed instance_v12→instance_v13, lanceur_v13→lanceur_v14`) ne montre que : docstring v14, import de
`SORTANTS`, commentaire de `VEILLEUR_MODULE`, liste fermée du transfert (l. 1223). Le diff brut ajoute
`INSTANCE_MODULE`, `CHEMINS_ARCHIVE` et son commentaire, deux mentions `lanceur_v14` dans des messages (l. 899,
l. 1765). Les mentions `instance_v12` et `lanceur_v13` qui restent (l. 13-14, 41, 593) sont dans des docstrings
historiques : correct. Rien d'autre. Détail : la ligne d'import l. 254 dépasse 120 caractères et place `SORTANTS` hors de
l'ordre alphabétique (cosmétique).

### R-10 — à préciser (hors du champ de la v14) — garde de démarrage jamais décidée : pas de délai

Si l'enfant reste bloqué avant l'impression (ou imprime moins que la configuration attendue), rien ne l'arrête avant
la dépense B − 2 ou l'échéance (désormais effectives grâce à R-5) ou le chien de garde. Un délai borné (quelques
minutes, la garde tombe « en quelques secondes » selon la contre-lecture 3 l. 87) éviterait de payer une carte à
attendre. Proposition pour une version suivante, pas pour la v14.

### Petits points (à préciser)

- `_ecrire_texte` (l. 252-258) n'efface pas son temporaire en cas d'erreur, à la différence d'`_ecrire_json` (Q-4).
  Le temporaire est hors de la liste fermée : jamais transféré. Aligner sur `_ecrire_json` par cohérence.
- La ligne `ETAT` d'`executer` (l. 1394-1397) ne porte pas `erreur_demarrage` : la conduite ne sait qu'au transfert
  qu'un message existe. L'ajouter aiderait le bilan (aucun risque : c'est un booléen).
- Coupe à 20 000 octets (l. 236) : la première ligne gardée peut être tronquée au début ; sans conséquence.
- `str.splitlines` coupe aussi sur `\r` : les barres de progression ne font pas de lignes géantes ; bien.
