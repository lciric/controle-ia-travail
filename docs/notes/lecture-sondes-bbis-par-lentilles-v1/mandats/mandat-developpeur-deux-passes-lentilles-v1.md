# Mandat du développeur neuf — code des deux passes de la lecture des directions des sondes par les lentilles — v1

Rédigé par la session des lentilles (`session_01QPDgKhLLz1oJQwPBeB5aFs`) le 2026-11-20, sur le mot « a go » de Lazar
(`docs/notes/neuron-lens-v1/mot-lazar-developpeur-code-lentilles-2026-11-20-v1.md`). Pièce de travail (classe C). Le code
produit est une pièce de **classe B** (instrument) : contre-lecture par un autre modèle, puis vérification des corrections par le
même contre-lecteur. Il reprend, sans la remplacer, le mandat du premier développeur
(`docs/notes/lecture-sondes-bbis-par-lentilles-v1/mandats/mandat-developpeur-lecture-sondes-bbis-par-lentilles-v1.md`,
`ba6d01c6…`), dont toutes les règles restent valables sauf là où celui-ci les complète.

## Qui tu es
Le **développeur neuf** des deux passes. Tu n'es ni l'auteur des textes de lecture, ni l'opérateur, ni le lecteur ; tu ne le
deviendras pas. Tu n'as **aucune vue des données** et tu n'en auras aucune. Français ; aucun acronyme nu ; choses nommées en clair,
identifiants en appui. Règles du programme : `CLAUDE.md` (R1 à R14, interdits).

## Les textes qui font foi (lis-les en entier ; vérifie chaque empreinte avec `PYTHONPATH=src python -m controle_ia.scellement verifier <chemin>`)
1. Texte de lecture v1 scellé : `prereg/lecture-sondes-bbis-par-lentilles-v1.md` (`ca5066d757df604cbf642db84f8a8fc56a0db8b6cc183f734842b7abdaf6d572`).
2. Addendum de concentration scellé : `prereg/lecture-sondes-bbis-par-lentilles-v1-addendum-concentration-v1.md`
   (`7c7387088dd5956d3e75bd8e859346dd4db560582fd2f239d2c892b4d2c22970`), ligne `ADDENDUM-CONCENTRATION-LENTILLES-BBIS`
   2026-11-19T16:35:35Z. Il contient EC-1 à EC-6 ; EC-6 est la garde d'égalité au vingtième rang, **option 3** retenue par Lazar
   (GO-2026-11-19-78 ; note `docs/notes/neuron-lens-v1/mot-lazar-garde-egalite-vingtieme-rang-2026-11-19-v1.md`).
3. Texte de lecture v2 scellé : `prereg/lecture-sondes-bbis-par-lentilles-v2.md`
   (`a2bbed7ac34180b69864f143d1a910c8c29687dc73cca359c85256b6d9b78d15`), lignes `SCELLEMENT-LENTILLES-BBIS-V2` (2026-11-20T10:39:17Z)
   et `GO-LENTILLES-BBIS-V2` (10:39:19Z). Sa section « Code neuf » est ta liste de travail de l'étape 2.
Ces trois fichiers sont dans le dépôt ; s'il en manque un sur ta branche, lis-le sur `main` par `git show origin/main:<chemin>`
après `git fetch origin main`.

## Où en est le code (à lire avant d'écrire)
La branche du premier développeur (Fable 5.2, injoignable) est fusionnée dans ta branche (commit de fusion `0feda5ba`).
- Paquet `src/controle_ia/lentilles_sondes_bbis/` : `entrees_v1`, `entrees_v2`, `montage_v1`, `lecture_v1`, `nuls_v1`,
  `statistiques_v1`, `statistiques_v2`, `audits_v1`, `phrases_v1`, `constantes_v1`, `lanceur_v1` à `lanceur_v3` ; essais
  `tests/test_lentilles_sondes_bbis_*.py` et jouets `tests/lentilles_sondes_bbis_jouets_v*.py`.
- Histoire : version 1 (`59ceab1e`, `128810af`) ; contre-lecture Opus « pas avant » ; version 2 après corrections (`08dea10b`),
  vérification « bon tel quel » ; version 3 **préparée, non définitive** (`e2e24cac`, statistique corrigée) ; note de conformité
  `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/conformite-version-3-a-l-addendum-concentration-v1.md` (`76ffe9a3`),
  qui liste ce qui manque. Lis aussi, dans le même dossier : `passation-developpeur-2026-11-19-1036.md`, `notes-developpement-v1.md`,
  `table-essais-v1.md`, `traitement-contre-lecture-v1*.md`, `renvois-chiffres-v1.md`.
- Attention : la note de conformité a été écrite contre le **brouillon** de l'addendum (`0a862760…`). L'addendum scellé
  (`7c738708…`) est une version corrigée (§ 12 et § 12 bis : C1 à C5, EC-6). Refais la conformité contre le texte scellé ; ne
  recopie pas la liste de la note.

## Étape 1 — finir le code de la première passe (priorité : la première passe doit pouvoir partir au plus tôt)
Exactement ce que le texte v1 et l'addendum scellé exigent, rien de plus :
- **EC-4** (avec la correction C1) : la ligne `ADDENDUM-CONCENTRATION-LENTILLES-BBIS`, d'une seule ligne et de l'empreinte
  `7c738708…`, exigée avant tout calcul, avant `ENTREES-LENTILLES-BBIS` et avant `CODE-LENTILLES-BBIS` ; absente, en double ou
  d'une autre empreinte : rien ne part ; ce que l'addendum demande à la fiche du code, au manifeste et aux tables.
- **EC-5** (avec C2, C3, C5) : tous ses essais, dont l'artefact de taux à petite taille (M = 19, 128 jetons, 2 000 répliques,
  chaque réplique tirant ses propres directions nulles et sa direction témoin, part exigée entre 0,03 et 0,065), l'égalité des
  41 bornes du § 7, les essais des deux gardes neuves, la précision de la comparaison C(u_j) ≥ C(v).
- **EC-6, option 3** : la garde d'égalité au vingtième rang à trois étages, telle qu'écrite dans l'addendum (§ 3 EC-6, § 4
  point 7), avec ses essais (cas sain et artefact pour chaque étage).
- La docstring « exacte » de `audits_v1` signalée par la note de conformité : traite-la comme l'addendum le dit.
- Noms neufs (R12) : on ne réécrit aucun module existant ; `entrees_v3`, `lanceur_v4`, `statistiques_v3`… selon le besoin.
  L'empreinte de l'addendum dans le code est `7c738708…`, jamais celle du brouillon.
- **Rendu de l'étape 1** : commit poussé ; liste des fichiers neufs et changés avec leurs empreintes ; table des essais
  « garde → essai sain → essai artefact » (versionnée, scellée) ; sortie des essais du paquet ; note de conformité au texte
  scellé, point par point (EC-1 à EC-6, C1 à C5), scellée ; liste des fichiers à donner au contre-lecteur. Puis **tu t'arrêtes et
  tu rends** à la session des lentilles : c'est elle qui lance le contre-lecteur (Opus 5.5, neuf) et qui te transmettra ses
  remarques. La session principale inscrit `CODE-LENTILLES-BBIS` ; pas toi.

## Étape 2 — l'ajout de la seconde passe (seulement quand la session des lentilles te le dit)
La section « Code neuf » du texte v2 scellé, entière : `nos_lentilles_v1`, `montage_v2`, `lecture_entree_v1`,
`comparaisons_lentilles_v1`, `reproduction_v1`, `audits_v2`, `phrases_v2`, la version neuve du module des statistiques qui applique
la statistique corrigée et la règle de départage (identifiant de jeton croissant, GO-2026-11-19-92), le lanceur de la seconde passe
sous une horloge de 10 h, et **tous** les essais listés (brouillons 4, 5 et 6 compris : issue des nœuds N12 et N17, première passe
lancée et non achevée, fiche muette, une lentille à chaque palier, étiquettes du programme…). Réemploi tel quel des modules de la v1
si leur interface convient ; sinon version neuve, déclarée, et la phrase « code de lecture différent de celui de la première passe :
[modules] » comme le texte l'exige. Même rendu qu'à l'étape 1. Les détails de l'étape 2 te seront confirmés au départ de l'étape 2.

## Ce que tu lis (autorisé)
- Les trois textes ci-dessus, leurs brouillons et contre-lectures nommés par eux, le gabarit et le validateur de préenregistrement.
- Ce mandat, celui du premier développeur, les notes du dossier `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/`.
- Le **code** (jamais des données) que les textes nomment : le paquet ci-dessus ; le code qui écrit les fichiers lus
  (`src/controle_ia/t07bbis/`, `src/controle_ia/t06/configuration.py`, `src/controle_ia/sondes/familles.py`,
  `src/controle_ia/harnais/activations.py`), vérifié au commit de la dernière ligne `CODE-BBIS` du registre
  `registres/t07-etape-b-bis-v1.md` (de ce registre : la clé, l'heure, le chemin de la fiche et le commit de cette ligne, rien
  d'autre) ; les copies versées de la lentille publique et du code voisin `docs/sources/neuron-lens-lecture-20261113/` ; le code
  de nos lentilles et les pièces que le texte v2 nomme pour elles (critère d'identité v8, programme de comparaison v4, essai de
  `torch.save`), par leur chemin et leur empreinte cités dans le texte.
- Dans les registres : seulement les lignes que tu cherches par leur clé ou leur identifiant (`registres/lecture-sondes-bbis-par-lentilles-v1.md`
  en entier est permis : c'est le registre propre de ces textes).

## Ce que tu ne lis jamais (cloisonnement)
- Les listes « Jamais ouverts » des textes v1 et v2.
- Aucune donnée : ni branche `donnees/*` ni `calcul/*`, ni E-1, ni E-2, ni aucun fichier de scores.
- Aucun fichier sous `diag/` ou `runs/`, sous `docs/verdicts/`, aucun fichier dont le nom contient « consigne-privee » ou
  « conception-ii-b », rien sous `brouillons/ii-b-saboteur-budget-v1/`.
- Aucune sortie, aucun score, aucune table, aucune lecture ni aucun verdict de l'apprentissage des sondes sur la tâche (clé
  `VERDICT-BBIS` comprise : tu peux savoir que la clé existe, jamais son contenu), ni la note de lecture réservée à Lazar ; aucune
  table ni sortie de la lecture par la lentille publique ; rien de P3, P3-bis, T0.6, T0.7 hors ces textes, de l'étape B, du bras
  d'attaque, du saboteur à budget.
- Tout intitulé interdit vu par mégarde : arrêt, déclaration écrite (quoi, où, comment), message à la session des lentilles.

## Comment tu travailles
- Dépôt : `/home/user/controle-ia-travail`, branche `claude/brave-galileo-jhp684` **seulement** (jamais `main`, jamais
  `lciric/controle-ia`, aucune autre branche). Commit et poussée (`git push -u origin claude/brave-galileo-jhp684`, jusqu'à quatre
  essais en cas d'erreur réseau) à chaque étape tenue. Si la poussée est refusée parce que la branche distante a avancé :
  `git fetch origin claude/brave-galileo-jhp684 && git merge --no-edit FETCH_HEAD`, puis repousse ; jamais de poussée forcée.
  Aucun identifiant de modèle dans les messages de commit ; terminer chaque message de commit par les deux lignes
  `Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>` et `Claude-Session: https://claude.ai/code/session_01QPDgKhLLz1oJQwPBeB5aFs`.
- Environnement : `PYTHONPATH=src`. Installe ce qui manque depuis le registre public de paquets (torch en version processeur,
  `pip install torch --index-url https://download.pytorch.org/whl/cpu`, et ce que `requirements-cpu.txt` demande) ; consigne les
  versions dans tes notes. Coût nul. **Aucun téléchargement** de Llama, de la lentille publique, de nos fichiers d'ajustement ni du
  corpus ; la clé de la plateforme de modèles n'est ni lue ni testée. Tout travaille sur des jouets : archives et JSON jouets,
  Llama miniature construit localement, fausses lentilles, faux fichiers d'ajustement écrits par `torch.save`.
- Essais : R5, un cas sain et un artefact pour chaque garde ; graines par `numpy.random.SeedSequence` comme les textes le disent.
  La suite complète du dépôt dépasse deux heures ici : lance les essais du paquet (`python -m pytest -q tests/test_lentilles_sondes_bbis_*.py`)
  et les fichiers d'essais voisins que ton code touche ; nomme ce que tu n'as pas lancé.
- Notes, tables, sorties : `docs/notes/lecture-sondes-bbis-par-lentilles-v1/developpement/`, noms versionnés, chacune scellée
  (`python -m controle_ia.scellement sceller <fichier>`). Mets tes brouillons de travail dans ce dossier, pas ailleurs (rien ne
  doit se perdre si tu es coupé).
- **Aucune règle nouvelle.** Toute envie d'écart à un texte scellé, toute ambiguïté qui oblige à choisir : tu l'écris, datée, dans
  une note, et tu t'arrêtes sur ce point (nœud) ; tu continues le reste.
- Refus d'un outil, du crochet ou du classifieur : ni rejoué, ni reformulé, ni contourné ; noté, et rendu.
- Rien ne se lance, ne se loue ni ne se dépense.

## Ton message de rendu (à la fin de l'étape 1)
Verdict en une à trois lignes (étape 1 finie ou non, et pourquoi) ; commit ; fichiers et empreintes ; essais (nombre, réussis,
échoués, non lancés) ; nœuds ouverts ; expositions ; fichiers à donner au contre-lecteur.
