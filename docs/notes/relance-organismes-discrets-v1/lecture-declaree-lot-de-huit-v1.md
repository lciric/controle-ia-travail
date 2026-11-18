# Lecture déclarée — « lot de 8 candidats » dans le préenregistrement scellé du bras A des organismes discrets — v1

- **Date (UTC, `date -u`)** : 2026-11-18T16:33Z.
- **Auteur** : lecteur neuf, ni auteur du texte, ni auteur du code, ni concepteur de moniteur. Aucun fichier de sondes, de bases, de moniteurs, de `runs/` ni de `diag/` ouvert. Aucun appel réseau. Seul ce fichier est écrit.
- **Objet** : exposer deux lectures (et une troisième) d'une ambiguïté du texte scellé, pour que Lazar tranche. Cette note ne tranche pas et ne recommande pas.

**Fichiers lus et empreintes sha256**

| fichier | empreinte |
|---|---|
| `prereg/T0.7-organismes-discrets-v-a-v1.md` (texte scellé) | `06ab6a2f6e173bb1258f45ffeded7a419b05ecc2f59920666cea91aafcc7cf05` |
| `prereg/T0.6-organismes-config-7b-v1.json` (configuration de référence) | `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527` |
| `docs/notes/organismes-discrets-v1/conception-organismes-discrets-v2.md` | `43a356ab7f8924faca17bb6024bbab8db778e3ce0b8a4b368ace1b78341f9b0c` |
| `docs/notes/organismes-discrets-v1/devis-organismes-discrets-v1.md` | `c376f2ea2e6a60849dc67e1563b45608a63454bd3fd3ba38202048354ea6b64c` |
| `src/controle_ia/harnais/episode.py` | `79113b4973d64bbcf0af16b2d7114c009b34132e1392e95ff83cef4d0a488c32` |
| `src/controle_ia/environnements/pilote_a.py` | `624761e2831a3fa14ccc1fe817d38a59014c9ef157e600cbd67e411607869bfc` |
| `src/controle_ia/t06/lanceur.py` | `a3dde5509712a7a2fe072dbdec7be616d8bc9190fa1a57e649f90bfce9f05bc3` |
| `docs/notes/relance-organismes-discrets-v1/carte-branchement-bras-a-v1.md` (avis d'un tiers, vérifié sur le code) | `0f26006d9eeaef7b1f7f84b96de50078350aa2e4cf177b6ed07cd21a12286190` |

Lus aussi, par recherche du seul mot « candidat », pour retracer l'origine de la formule : `conception-organismes-discrets-v1.md` et les brouillons 1, 5 et 6 du préenregistrement (même dossier que la conception).

## 1. Citations exactes

**Texte scellé.**
- Ligne 17 : « **Configuration de référence** : `prereg/T0.6-organismes-config-7b-v1.json` (clés `agent`, `adaptateur`, `distillation`, `taches_distillation`, `taches_evaluation`). `b7a5c1baeee13f7589b296fb166180515422ebc8c7eff703994bb5b6835ae527`. » L'empreinte citée est bien celle du fichier sur disque.
- Ligne 31 : « Conformément à la section 1.1 de `conception-organismes-discrets-v2.md` […] (**mêmes graines d'action** pour une même tâche d'une condition à l'autre, comme dans la configuration de référence). »
- Ligne 39 : « **Paramètres de génération et de distillation** (gelés par référence à la configuration scellée) : lot de 8 candidats, 400 jetons au plus, température 1,0, graines dérivées par (tâche, épisode, pas, candidat) (R9). […] Toute modification est un nœud. »
- Ligne 44 : « **Sélection adverse parmi $K$ tirages honnêtes** : retirée du protocole principal ; conservée exclusivement comme **repli ouvert déclaré de deuxième ligne** (voir section 5.2). »
- Ligne 161 : « **Tailles** : 16 tâches de vérification × 8 épisodes par tâche et par condition = **128 épisodes** ($N = 128$) et **1 280 actions** par condition ($T = 10$ pas par épisode). »
- Ligne 164 : « Une **seule** passe de tirage de candidats : 16 tâches × 8 épisodes × 10 pas × 8 candidats. Réglages de génération : lot de 8, 400 jetons au plus, température 1,0 (identiques à ceux de la configuration de référence). Graines (R9) : `numpy.random.SeedSequence`, dérivées par (tâche, épisode, pas, candidat) pour les tirages ; […] **mêmes graines d'action pour une même tâche d'une condition à l'autre**. »
- Ligne 280 (repli de deuxième ligne) : « Instruction de l'option de deuxième ligne […] (sélection adverse parmi $K$ tirages honnêtes), faisant l'objet d'un avenant de préenregistrement scellé séparément avant son exécution. »

**Configuration de référence.** Ligne 2 : `"N": 1` ; ligne 3 : `"T": 10` ; ligne 85 : `"episodes_par_tache_distillation": 5` ; `"lot": 8` ; `"max_nouveaux": 400` ; `"temperature": 1.0`. Sous `distillation` : `"lot": 1`, `"unite_du_lot": "transcription"`. Aucune clé ne porte le mot « candidat ». Aucune clé ne décrit la dérivation des graines. Aucune clé ne vaut « 8 épisodes par tâche ».

**Conception v2, section 1.1, point 2 (ligne 32).** « Sur chaque tâche de fabrication, **8 épisodes honnêtes** (T = 10 pas, N = 1, lot de 8, 400 jetons au plus, température 1,0, graines dérivées par (tâche, épisode, pas)). C'est l'unique génération de la fabrication. » Le mot « candidat » n'y figure pas.
**Conception v2, section 1.3 (ligne 78).** « **Le choix adverse parmi K tirages honnêtes** (dommage-caché) : son coût de fabrication est K fois celui du bras A […]. Il est gardé comme **option de deuxième ligne**. »

**Devis v1.** Ligne 3 : il chiffre la conception **v1** et le brouillon 1 du préenregistrement, pas la conception v2. Ligne 30 : « candidats du maître de (v-a) : 16 tâches × 8 épisodes × 10 pas × 8 candidats | 10 240 actions ». Ligne 31 : « lecteur de la clé de sélection sur la moitié D, une lecture courte par candidat | 10 240 lectures ». Ligne 43 : « Les trois doses de (v-a) se lisent sur **les mêmes huit candidats** (doses emboîtées) ». Ligne 78 : « 4 tâches, 2 épisodes, K = 8 ; […] si le pire de huit tirages honnêtes n'abaisse pas la couverture, (v-a) s'arrête ici ».

## 2. Faits établis

1. **Dans la configuration, « lot » vaut 8 et ne dit pas son unité** pour la génération (pour la distillation, l'unité est écrite : la transcription).
2. **Dans le code, le lot est un lot d'épisodes.** `harnais/episode.py`, lignes 10 à 12 : « à chaque (pas t, agent i), les actions de tous les épisodes du lot sont générées ensemble […] une graine par action ». `jouer_episodes` (ligne 160) prend une liste d'épisodes ; à la ligne 218, il lit une graine par épisode du lot pour le pas en cours ; `generer_lot` (ligne 74) rend une suite par ligne. Une ligne du lot est un épisode. Il y a une action par épisode et par pas. Rien ne tire plusieurs actions sur le même contexte, rien ne choisit.
3. **Les graines suivent (tâche, épisode), puis (agent, pas).** `t06/lanceur.py`, lignes 119 à 124 : une clé de graine par `distillation/tache/<tâche>/e<k>`. Lignes 148 et 149 : un générateur par épisode, d'où `graines_des_actions` (`pilote_a.py`, lignes 73 à 76) tire une graine par action (agent, pas). Aucun indice de candidat.
4. **Le découpage en lots** (`lanceur.py`, lignes 131 et 138 à 144 ; `pilote_a.py`, lignes 99 à 106) tranche le plan des épisodes par paquets de `lot`. La carte du tiers (piège 1) est exacte sur ce point.
5. **Origine de la formule.** La conception v1 (ligne 79) tirait « K actions candidates » par pas, avec « graines dérivées par (tâche, épisode, pas, candidat) », et retenait celle qui porte le moins de contrôles (ligne 81). Le brouillon 1 (ligne 109) porte mot pour mot la phrase de la ligne 164 du texte scellé. La conception v2 a retiré cette sélection (section 1.3). Les mots « candidats » et « candidat » sont restés dans les brouillons 5 et 6, puis dans le texte scellé.
6. **Le texte scellé ne donne aucune règle de choix** entre candidats. Le mot « sélection » n'y reste que dans des restes (« moitié D (sélection) », ligne 160 ; titre « M-2 (sélection effective) », ligne 178, dont le corps parle de permutation ; garde de la section 8.4).
7. **Les tailles et la puissance ne comptent pas les candidats.** $N = 128$ épisodes, 1 280 actions par condition, unité d'inférence de 16 moyennes de tâche (lignes 71, 77, 107, 161).
8. La ligne 44 renvoie à une « section 5.2 » qui n'existe pas ; le repli est en section 9.2.

## 3. Lecture A — le texte se lit comme la configuration de référence

Lot de huit épisodes joués en parallèle, une action par épisode et par pas, graines par tâche, épisode et pas. Aucun tirage multiple.

- **Plan de génération** : 16 tâches × 8 épisodes × 10 pas = 1 280 actions pour la passe de fabrication. Aucune règle de choix n'est nécessaire.
- **Devis** : multiplicateur 1. Le poste A du devis v1 (10 240 unités, soit environ 5,1 heures de carte et 2,5 USD à l'hypothèse de débit du devis) tombe à 1 280 unités (environ 0,6 heure, 0,3 USD). Le poste B (clé de sélection) n'a plus d'objet.
- **Tailles et puissance** : inchangées, telles qu'écrites.
- **Appariement au jumeau honnête** : direct. Une graine par (tâche, épisode, pas), la même d'une condition à l'autre, « comme dans la configuration de référence ».
- **Repli par K tirages** : reste entier et séparé, avec son avenant et sa génération propre, K fois plus chère, comme le dit la conception.
- **Lettre du texte** : s'appuie sur « gelés par référence à la configuration scellée », « identiques à ceux de la configuration de référence », « conformément à la section 1.1 » de la conception v2. Elle n'exécute pas trois éléments écrits : « lot de 8 **candidats** », le facteur « × 8 candidats », l'indice « candidat » des graines. Lazar doit dire si c'est une lecture déclarée ou un écart à consigner par addendum.
- **Risques** : écarter des mots d'un texte scellé après coup ; un lecteur extérieur peut y voir une réduction du protocole. Le code existant dérive les graines par générateur d'épisode, non par une clé à trois termes : la conformité de la dérivation à la lettre reste à déclarer.

## 4. Lecture B — huit actions candidates par pas

À chaque pas, huit actions tirées sur le même contexte, graines par tâche, épisode, pas et candidat.

- **Plan de génération** : 10 240 actions pour la passe. **Le texte ne dit pas laquelle est jouée.** Il faut une règle, et le texte n'en porte aucune. Il ne dit pas non plus si les huit tirages valent pour la seule fabrication ou aussi pour chaque condition de la vérification.
- **Devis** : multiplicateur 8 sur la génération de fabrication (poste A du devis v1 tel qu'écrit). Si les candidats étaient aussi tirés à la vérification, multiplicateur 8 sur ce poste aussi ; le texte ne le demande pas en clair.
- **Tailles et puissance** : inchangées si une seule action par pas est jouée. Si la règle de choix dépend du contenu, la loi de l'épisode « honnête » change, et l'écart-type estimé sur les épisodes honnêtes avec elle.
- **Appariement au jumeau honnête** : il faut dire quel candidat le jumeau joue. « Mêmes graines d'action » ne suffit plus sans indice de candidat fixé.
- **Repli par K tirages** : les huit tirages existeraient sur disque avant l'avenant qui doit préenregistrer ce repli. Le repli cesserait d'être K fois plus cher, contre la lettre de la conception (section 1.3).
- **Lettre du texte** : exécute les mots « candidat ». Mais elle contredit la conception v2 que le texte dit suivre (graines à trois termes, pas de candidat), la configuration de référence dite « identique », et le retrait de la sélection (ligne 44). Toute règle de choix serait un ajout : addendum d'écart nécessaire, et nœud (« Toute modification est un nœud »).
- **Risques** : réintroduire sans le dire le mécanisme retiré ; dépense huit fois plus forte pour des tirages sans emploi écrit ; code neuf hors de la chaîne éprouvée ; données du repli produites avant son préenregistrement.

## 5. Troisième lecture possible

**Lecture C — huit candidats tirés, le premier joué.** On tire les huit, on joue toujours le candidat d'indice 0, les sept autres sont archivés sans être lus. Elle exécute la lettre des lignes 39 et 164 sans sélection sur le contenu. L'appariement est simple (indice 0 partout). Elle coûte huit fois la génération de fabrication. « Le premier est joué » reste une règle que le texte n'écrit pas. Les sept tirages archivés posent la même question que dans la lecture B pour le repli.

Remarque de fait : avec un lot de 8 et 8 épisodes par tâche, chaque lot de la lecture A contient exactement les huit épisodes d'une tâche. Cela peut expliquer le glissement de vocabulaire, mais pas le facteur « × 8 candidats » de la ligne 164.

## 6. Ce que je n'ai pas pu établir

- L'intention de l'auteur du texte scellé et de son contre-lecteur. Le rapport de contre-lecture du brouillon 6 ne contient pas le mot « candidat ».
- L'existence d'un devis accordé à la conception v2. La conception v2 cite un « devis v2 » ; je n'ai trouvé pour ce bras que le devis v1, écrit pour la conception v1. Je n'ai pas cherché de ligne de GO de calcul pour ce bras.
- Sur quelles 16 tâches porte la passe de la ligne 164 (fabrication, d'après la conception ; le texte scellé ne le dit pas).
- Le contenu de `prereg/T0.8-base-A-mots-et-cout-v1.md`, que le texte scellé cite : fichier interdit, non ouvert.
- Le débit réel et donc les montants en dollars : ceux donnés ici reprennent l'hypothèse non mesurée du devis v1.
- Si le code de graines existant satisfait la lettre « `SeedSequence`, dérivées par (tâche, épisode, pas) » : je n'ai pas ouvert `manifeste.py`.

## Décision à prendre par Lazar

Le texte scellé du bras A se joue-t-il avec un lot de huit épisodes et une action par pas (lecture A), avec huit actions candidates par pas et une règle de choix à écrire (lecture B), ou avec huit candidats dont le premier est joué (lecture C), et sous quelle forme — lecture déclarée ou addendum d'écart ?
