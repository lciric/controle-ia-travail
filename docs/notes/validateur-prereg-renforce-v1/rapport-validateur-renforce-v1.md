# Validateur renforcé des préenregistrements — rapport v1

- **Pièce** : instrument (classe B), écrite par Opus 5.5 le 28 novembre 2026, à contre-lire par un autre modèle. Non commise par l'auteur.
- **Fichiers** : `src/controle_ia/prereg_renforce_v1.py` (module et ligne de commande), `tests/test_prereg_renforce_v1.py` (56 essais). Aucun fichier existant modifié.
- **Pourquoi** : le validateur de structure (`src/controle_ia/prereg.py`, fonction `problemes`) a laissé passer, le 28 novembre, deux brouillons qui citaient des empreintes sans fichier et des chemins absents ; sur 13 mutations de chaque brouillon il en voyait 2 (`docs/notes/premortem-prereg-v4-20261128-v1/lecteur-B/rendu-lecteur-B-v1.md`, § 1, témoin T2 (a)).
- **Emploi** : `PYTHONPATH=src python -m controle_ia.prereg_renforce_v1 [--racine R] [--mots-min N] FICHIER…` ; code de sortie 1 si un fichier a au moins un problème ; les avertissements ne changent pas le code. En bibliothèque : `problemes_renforces(chemin, racine=".", mots_min=30, index=None)` renvoie la liste des problèmes ; `verifier_renforce(...)` renvoie (problèmes, avertissements).

## 1. Ce que fait chaque contrôle, et ce qu'il ne fait pas

Les problèmes de `prereg.problemes` viennent d'abord, inchangés (sections, marqueurs, deux empreintes par contre-lecture). Les cinq contrôles suivent ; chaque message commence par sa lettre.

**Index des empreintes connues.** Construit une fois par appel (une fois pour tous les fichiers en ligne de commande) : (1) toutes les lignes au format de `sha256sum` (« empreinte, deux espaces ou espace-étoile, nom ») des fichiers `*.sha256` de l'arbre, hors `.git`, `.venv` et caches ; une ligne compte seulement si le fichier qu'elle désigne existe (le nom de la ligne, relatif au dossier du compagnon ; à défaut, pour un compagnon d'une ligne, le fichier dont il porte le nom) ; (2) à la première empreinte ou au premier préfixe non portés par un compagnon, l'empreinte SHA-256 de chaque fichier de `git ls-files --cached` (arbre de travail), hors fichiers gardés. Hors dépôt git, seuls les compagnons comptent. Sur le dépôt réel, l'index complet prend environ 7 secondes.

**(a) Empreintes complètes.** Toute chaîne de 64 caractères hexadécimaux minuscules, n'importe où dans le texte (non collée à une lettre ou un chiffre), doit être dans l'index. Un problème par empreinte distincte, avec la ligne de sa première citation.
- Ne vérifie pas que l'empreinte est celle **du fichier cité à côté** : une empreinte qui désigne un autre fichier du dépôt passe. Exemple réel : les deux brouillons donnent pour `src/controle_ia/prereg.py` l'empreinte `3b2e3ee5…`, qui est celle d'une copie archivée sous `docs/notes/echelle-conscience-eval/…/depot/src/controle_ia/prereg.py`, pas du fichier courant ; le contrôle (a) l'accepte.
- Ne vérifie pas qu'un compagnon est juste (c'est le rôle de `verifier-arbre`).
- Ne résout pas une version historique (« `registres/decisions.md` au commit `ec1d71b0…` », empreinte `ac9b2cdb…`) ni un fichier effacé de l'arbre courant (candidats intermédiaires) : ils sont signalés.
- Ne reconnaît pas les empreintes en majuscules ni coupées par une mise en forme.

**(b) Préfixes d'empreinte.** Toute chaîne de 8 à 63 caractères hexadécimaux minuscules, dont au moins un chiffre, suivie de « … » ou de « ... », doit être le début d'au moins une empreinte de l'index. Aucune : problème. Plusieurs : avertissement seulement.
- Un préfixe de commit git (`commit 9c1f4b1a…`) ou d'un objet extérieur au dépôt est signalé à tort ; le contrôle ne distingue pas un préfixe de commit d'un préfixe d'empreinte.
- Un préfixe sans chiffre (`deadbeefcafe…`) ou de moins de 8 caractères est ignoré.

**(c) Chemins du dépôt.** Tout contenu entre accents graves qui commence par `src/`, `docs/`, `prereg/`, `diag/`, `runs/`, `registres/`, `scripts/`, `tests/`, `brouillons/` ou `livrables/` : son premier mot (une commande avec arguments n'est lue que par son premier mot ; aucun fichier suivi du dépôt n'a d'espace dans son nom) doit exister, relativement à la racine. Un suffixe `:n` ou `:n1-n2` doit vérifier 1 ≤ n1 ≤ n2 ≤ nombre de lignes ; sur un dossier, c'est un problème. Un contenu qui porte `…`, `...`, `*`, `?`, `[`, `<`, `{` ou `$` est ignoré (motifs, gabarits, variables).
- Ne lit pas les chemins hors accents graves, ni les noms nus (`contre-lecture-r2-etages-1-2-v1.md`, cité seul par les deux brouillons), ni les dossiers hors de la liste (`donnees/`, `traces/`).
- Ne distingue pas un fichier promis (« sera écrit ») d'un fichier inventé : les deux sont signalés.
- Pour un fichier gardé, l'existence est vérifiée (simple consultation du disque) mais les lignes ne sont pas comptées : avertissement.

**(d) Sections trop courtes.** Chacune des huit sections de `prereg.SECTIONS` doit compter au moins N mots (paramètre `mots_min`, défaut 30) ; un mot est un morceau sans espace qui contient au moins une lettre ou un chiffre. Les sous-sections `###` comptent dans leur section.
- Ne juge pas le contenu : trente mots creux passent.

**(e) Contre-lectures.** Chaque entrée « Contre-lecture k » (puce `-`, `*` ou `+`, gras, titre `###` à `######`, ou ligne nue), à défaut d'entrée la section entière, doit (1) nommer un modèle de la liste `MODELES` — Fable, Opus, Sonnet, Haiku, Gemini, Carbon, Argon, Neon, Astra, GPT, Llama, Mistral, Qwen, DeepSeek, Grok —, mot entier, casse indifférente (`claude-opus-5-5` compte ; « Claude » seul ne suffit pas, il ne dit pas lequel) ; (2) citer au moins une empreinte résolue par (a).
- Ne vérifie pas que le modèle nommé est bien celui du relecteur (le nom peut désigner l'auteur), ni la règle de la session (Fable neuf pour les pièces délicates depuis GO-2026-11-28-06), ni que l'empreinte est celle du brouillon relu ou du rapport.
- Les entrées sont reconnues aussi quand elles commencent par `* **` (forme des deux brouillons, que le validateur de base ne découpe pas).

**Garde de lecture.** Aucun fichier gardé n'est ouvert, ni pour son empreinte, ni pour compter ses lignes, ni comme préenregistrement (refus par `GardeArret`) : `*.npz`, `*.npy`, `*.safetensors`, tout ce qui est sous `brouillons/g0-criteres-2-3-v1/consignes-privees-*` et `brouillons/ii-b-saboteur-budget-*`, tout nom qui commence par `P3-consignes-v1` (le préenregistrement scellé, ses brouillons et candidats ; `P3-bis-consignes-v1.md` n'est pas gardé), tout ce qui est sous `src/controle_ia/iib/`. Leurs compagnons `.sha256` sont lus. Sur le dépôt réel, 111 fichiers suivis sont sautés.

**Hors champ** (mutations du lecteur B que ce validateur ne voit pas) : un neuvième titre de niveau 2, le niveau des sous-sections, le retrait de mots imposés (`FILS_BLAS`, `SeedSequence`, `sdpa`), un seuil contradictoire. Aucun contrôle de cohérence chiffrée.

## 2. Épreuves (R5)

- 56 essais dans un faux dépôt temporaire (`git init`, fichiers, compagnons) ; aucun ne lit le vrai dépôt. Cas sain : aucun problème, aucun avertissement, code de sortie 0. Artefacts : au moins un par contrôle et par branche (empreinte inventée, compagnon orphelin, fichier ni suivi ni scellé, liste `sha256sum` à plusieurs lignes, hors dépôt git ; préfixe inconnu, en trois points, ambigu, ignoré ; chemin absent, lignes hors fichier sur quatre formes, suffixe sur un dossier, motifs ignorés, commande ; seuil de mots paramétré ; entrée sans modèle, modèle dans un identifiant, entrée sans empreinte résolue, section sans entrées, quatre formes d'entrée ; quatorze cas de la garde, aucun fichier gardé haché, préenregistrement gardé refusé, index partagé sans nouveau hachage).
- Mutations du lecteur B rejouées dans les essais : q1 (empreintes de la contre-lecture inventées), q2 (toutes inventées), q3 (chemins inexistants), q4 (sections réduites à un mot) ; chacune passe le validateur de base et est vue.
- Épreuve du validateur par ses propres essais : dix mutants du module (chaque contrôle éteint, ambiguïté de (b) passée en erreur, comptage de lignes éteint, garde éteinte, compagnon orphelin accepté) ; chacun fait échouer de 1 à 9 essais.
- Commande : `PYTHONPATH=src python -m pytest -q tests/test_prereg_renforce_v1.py tests/test_prereg.py` → 66 réussis.

## 3. Relevé informatif (aucun fichier relevé n'est modifié)

### 3.1 Les deux brouillons du 28 novembre

| brouillon | validateur de base | renforcé |
|---|---|---|
| `brouillons/prereg-v4-c-furtif-g1/G0-critere-3-additif-c-furtif-v1-brouillon-gemini-1.md` (`94913179…`) | aucun problème | 12 problèmes : 10 empreintes (a) sans fichier (`79e3e522…`, `dabd4336…`, `30d432f8…`, `94ca013c…`, `fe414af7…`, `374ad473…`, `29e4c210…`, `189fb0c0…`, `177c7b61…`, `59a2a571…`) ; (e) contre-lectures 1 et 2 sans modèle nommé |
| `brouillons/prereg-v4-c-furtif-g1/G1-architecture-h1-h2-v1-brouillon-gemini-1.md` (`887795c4…`) | aucun problème | 9 problèmes : 7 empreintes (a) sans fichier (`79e3e522…`, `94ca013c…`, `374ad473…`, `29e4c210…`, `189fb0c0…`, `177c7b61…`, `59a2a571…`) ; (e) contre-lectures 1 et 2 sans modèle nommé |

`59a2a571…` est l'empreinte donnée au rapport de la contre-épreuve 2 (`contre-epreuve-r2-volets-11-13-v1.md`) : aucun fichier du dépôt ne la porte. Les préfixes cités par G0 (`0065065b…`, `19dbc99e…`, `2263c5c4…`, `68ade33f…`, `76cdeace…`) se résolvent tous, et tous les chemins cités entre accents graves existent ; les chemins absents que relevait le lecteur B sont des noms nus, hors du champ de (c). Sur les 13 mutations du lecteur B, rejouées sur chaque brouillon et comparées au brouillon intact (numéros de ligne retirés), le renforcé en voit 7 au lieu de 2 : p5 (le nom `passe_recalcul_v6` change, le chemin n'existe plus), p6, p7, q1, q2, q3, q4.

### 3.2 Préenregistrements scellés de `prereg/`

Champ : les 183 fichiers `prereg/*.md` qui ont un compagnon (sur 187 ; trois non scellés `versant-honnete-jumeau-*`, et `prereg/P3-consignes-v1.md`, gardé, non ouvert). Beaucoup sont des additifs ou des brouillons qui n'ont pas les huit sections : 117 échouent déjà au validateur de base. Les comptes sont donc donnés deux fois.

| contrôle | 183 scellés : fichiers en échec (problèmes) | 66 qui passent le validateur de base : fichiers en échec (problèmes) |
|---|---|---|
| (a) empreinte sans fichier | 135 (2 458) | 55 (1 181) |
| (b) préfixe sans empreinte connue | 93 (641) | 35 (326) |
| (c) chemin absent ou lignes hors fichier | 115 (1 831) | 39 (929) |
| (d) section de moins de 30 mots | 19 (26) | 0 |
| (e) contre-lecture sans modèle ou sans empreinte résolue | 102 (263) : sans modèle 84, sans empreinte 68 | 34 (120) : sans modèle 33, sans empreinte 5 |
| un contrôle renforcé au moins | 174 | 65 |

Un seul fichier passe tout : `prereg/diagnostics-prealables-sondes-v1.md`. Aucun préfixe ambigu.

Trois exemples par contrôle (dans les 66, sauf (d)) :
- (a) `prereg/G0-critere-3-designation-course-v1.md`, ligne 3 : `051d0012…`, empreinte d'un candidat intermédiaire effacé de l'arbre ; `prereg/P3-addendum-lecture-complementaire-v1.md`, ligne 6 : `012bb5ba…` ; `prereg/P3-addendum2-audit-verdict-v1.md`, ligne 50 : `ac9b2cdb…`, empreinte de `registres/decisions.md` à un commit ancien.
- (b) `prereg/P3-bis-temoin-positif-v1.md`, ligne 310 : `e682abb0…` (cité après `git show`) ; `prereg/R1-addendum-relance-v4.md`, ligne 10 : `a5a61077…` ; `prereg/SPARKS-EXP7-NUL-addendum-1.md`, ligne 603 : `a51942b1…`.
- (c) `prereg/G0-critere-3-designation-course-v1.md`, ligne 15 : `brouillons/g0-criteres-2-3-v1/T0.6-organisme-consigne-cachee-dose-reponse-v1-candidat1.md` ; `prereg/P3-addendum-lecture-complementaire-v1.md`, ligne 5 : un brouillon de `brouillons/canal_gemini/…` absent ; `prereg/P3-bis-temoin-positif-v1.md`, ligne 359 : `scripts/p3bis_instance_v2.sh`.
- (d) `prereg/P-041-examen-final-v1.md` et `prereg/P-041-malleabilite-v1.md` : Contre-lecture de 23 mots ; `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-addendum-1-brouillon1.md` : Contre-lecture vide.
- (e) `prereg/G0-critere-3-designation-course-v1.md`, `prereg/P3-addendum-lecture-complementaire-v1.md`, `prereg/P3-addendum2-audit-verdict-v1.md` : contre-lecture 1 sans modèle nommé.

**Lecture.** Ces comptes ne disent pas que 174 préenregistrements sont faux : la règle de nommer le modèle date du 19 novembre, beaucoup d'empreintes et de chemins désignent des versions historiques, des candidats effacés, des fichiers promis ou des objets extérieurs (commits d'autres dépôts, fichiers de machines distantes). Ils disent que le contrôle, appliqué tel quel aux pièces anciennes, signalerait presque tout ; il est fait pour les pièces neuves, avant scellement.

## 4. Limites connues et pistes (non faites)

1. (a) n'apparie pas une empreinte au chemin cité à côté ; c'est le défaut le plus grave qui reste (une empreinte d'un autre fichier passe).
2. Versions historiques : on pourrait résoudre « `chemin` au commit `X` » par `git show X:chemin`.
3. (b) signale les préfixes de commit ; on pourrait accepter un préfixe qui désigne un objet git du dépôt.
4. (c) ignore les noms nus et les dossiers hors liste ; une convention pour les fichiers promis (marque écrite à côté du chemin) éviterait de les confondre avec des chemins inventés.
5. (e) ne sait pas qui est le relecteur : le modèle nommé peut être celui de l'auteur.
6. Le hachage de l'arbre de travail suit le contenu sur disque, pas celui du dernier commit.
