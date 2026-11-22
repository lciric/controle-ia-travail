# Journal des accès du monteur de l'oracle, cycle 1 du scellement 2, relance — v1

- Classe C. Tenu par le monteur relancé (`session_01XJ6MgmSDBZpPAuXLe3diix`) ; scellé à la fin de la session.
- Chaque ligne : heure (UTC, `date -u`), chemin (objet git), empreinte sha256 (16 premiers signes), motif.
- Accès au coffre inscrit avant le premier geste : `registres/decisions.md`, R-4919, sur `main`.

## Avant le coffre

| heure | chemin | empreinte | motif |
|---|---|---|---|
| 14:37 | `becfd076:docs/notes/attaquant-informe-v1/course-brouillon17-v1/mandat-monteur-oracle-relance-v3.md` ; `docs/procedures/mandat-monteur-oracle-scellement-2-v2.md` (en entier) | `2d81401a54808257`, `c6f090c02bfc2cd6` | mandat |
| 14:38 | `origin/main:registres/decisions.md`, recherche de « Accès au coffre du bras d'attaque » et de mon identifiant ; lignes rendues : R-4638, R-4641 (accès, sans contenu), R-4919 | — | vérifier la ligne d'accès avant tout geste |

## Coffre et pièces de la famille du cycle 1

| heure | chemin | empreinte | motif |
|---|---|---|---|
| 14:39 | `donnees/bras-attaque-oracle-scellement-2-cycle-1-v1/` : noms et tailles | tête `c05c604df3794528` | inventaire |
| 14:40 | les 19 sceaux compagnons du dossier, vérifiés par `sha256sum -c` | tous conformes | empreintes avant lecture |
| 14:40 | `journal-acces-v1.md` (en entier) | `c67877f58af0619d` | travail du prédécesseur ; trouvé non scellé |
| 14:40 | `piece-1-…-v1.md`, `piece-2-…-v1.md`, `piece-3-…-v1.md`, `piece-4-…-v1.md`, `piece-5-…-v1.md` (en entier) | `c5f000943140b75b`, `758e404a4327f5a3`, `10e1f85ac7802623`, `7583d5ff11668be5`, `c46daeae33d116be` | idem |
| 14:40 | `message-mere-proposition-lecteurs-v1.md`, `-v2.md`, `constat-lecture-humaine-et-conservation-fournisseurs-v1.md` (en entier) ; pages de `sources-conditions-fournisseurs-v1/` : sceaux seuls, non ouvertes | `162738588e5c8436`, `ffc82cb9362d6879`, `f892fc6caaeb98e0` | idem |
| 14:40 | `message-mere-oracle-mode-connu-faisabilite-v1.md`, `message-mere-forme-des-questions-v12-v1.md`, `message-mere-attestations-voie-envoi-v13-v1.md` (en entier) | `bfb639a108b401ef`, `fd3dbb42bf2b90e4`, `6a8234f420dbe1b3` | idem |
| 14:41 | `controle_agent_p1_v1.py`, `oracle_famille_1_v1.py` (en entier) ; `test_oracle_famille_1_v1.py` (noms des tests et en-tête) | `42a2a0437473546f`, `43c4c8f1de288781`, `216c2f3213ce5044` | idem |
| 14:43 | `f4c479c5:donnees/bras-attaque-scellement-2-v1/piece-3-famille-aveugle-1-verite-du-dommage-v2.md` (en entier) | `2a7416a823c406a1` | spécification de l'oracle (mandat v2, section 3, obligatoire) |
| 14:43 | `origin/claude/scellement-2-familles-aveugles-v1` : liste des noms de fichiers et des commits (sans contenu) | — | repérer les versions qui font foi |
| 14:46 | `claude/scellement-2-contre-lecture-v1:…/piece-7-verification-des-corrections-v1.md` et son erratum 1 (en entier) ; `piece-7-contre-lecture-v1.md` : empreinte seule, non ouverte | `8be9063c0982ce24`, `aa10a1db0f9ff512`, `e0fbe36598b4f8c7` | conditions de la contre-lecture et nœuds restants |
| 14:46 | tests du dossier lancés (46 réussis) | — | état du code repris |

Non lus : la pièce 2 de la famille (texte du mode) et ses pièces 4 et 5 (la pièce 4 v2 n'a pas été ouverte : le plan
monté du prédécesseur en dit assez pour l'état repris), la contre-lecture `piece-7-contre-lecture-v1.md`, la pièce 1
de la famille et ses errata, tout moniteur, la branche `claude/scellement-2-famille-reserve-cycle-2-v1`,
`registres/etat.md`, les passations du programme, les lignes R-604 à R-610.

## Textes du banc fermé, hors coffre

| heure | chemin | empreinte | motif |
|---|---|---|---|
| 14:41 | course, brouillon 17 (`claude/loving-lamport-7ol5ws`) : titres, puis sections D6, D7 ter, D8, « Champs ouverts et nœuds », et les lignes de la liste d'arrêt qui touchent l'oracle (par recherche) | `cf5d35d8472137d3` | mandat v3, section 2, point 2 |
| 14:42 | répétition générale, brouillon 9 (`claude/prereg-course-banc-ferme-v1`) : en-tête, table des différences (champ R-5), champs et réserves | `a58cab35cf4914a4` | idem |
| 14:42 | pièce de sécurité v16 (`claude/piece-securite-banc-ferme-v1`) : titres, sections 3.5 et 6 | `b8bcda60ead6f58f` | idem |
| 14:42 | audit des lignées (`main`) : en-tête, « Lignée du juge », « Liste d'exclusion proposée », « Incertitudes » ; sa vérification : « Verdict », « Liste finale », et des lignes trouvées par recherche (exclusion, Mistral) | `596b5a73453b97ed`, `8718c80bee53da35` | liste d'exclusion seulement |
| 14:43 | fichiers de tâches du banc (`taches-evaluation.json`, `taches-entrainement.json`) : par programme, noms de clés, comptes par partie de la référence, forme des identifiants, comptes de descriptions qui portent un mot d'issue ; **aucun texte affiché** | `76cdeace861d2fff`, `8d20a698d76baa8a` | nœud de la règle des questions |
| 14:45 | `origin/main:registres/decisions.md` (lignes R-4668, R-4674, R-4676, R-4678, R-4679, R-4683, R-4779, et lignes après R-4679 trouvées par mots) ; `origin/main:registres/go.md` (lignes trouvées par mots : lecture humaine, oracle, lecteurs, GO-2026-11-21-61, -66, -75, -76, -84, -85 et quelques lignes du 22 rendues par la recherche) | — | état des nœuds du prédécesseur |
| 14:48 | `origin/main:CLAUDE.md`, lignes 50 à 100 (règles permanentes ajoutées depuis cette branche) | — | règle des appels aux modèles de Google |
| 14:47 | environnement de la session (outil `get_environment`) : noms des variables seulement | — | lieu d'envoi |

## Après les premières pièces

| heure | chemin | empreinte | motif |
|---|---|---|---|
| 14:54–14:56 | `sources-conditions-fournisseurs-v1/` (5 pages) : texte extrait par programme, recherche des citations du constat et de quelques mots (conservation, revue humaine, stockage) ; passages autour des mots rendus | `ad9f490a…`, `b2c1aa50…`, `e1bda710…`, `1edd80fc…` (non ouverte), `361792f0…` | champ n° 18 : vérifier chaque citation mot pour mot |
| 14:58 | course, brouillon 17 : recherche par programme de l'identifiant de l'ancienne session et de R-4638 et R-4679 dans le texte entier ; fragments rendus des lignes 35, 44, 82, 136, 151, 225, 561, 720 (dont 35, 44, 82 et 720 hors des sections désignées, fragments de moins de 250 signes, sans autre lecture) ; même recherche, sans résultat, dans la répétition et la pièce de sécurité | `cf5d35d8…`, `a58cab35…`, `b8bcda60…` | lieu d'envoi : remplacements exacts |

Note : la recherche du 14:38 a rendu la ligne R-4641, qui nomme la famille de réserve du cycle 2 par une empreinte
(`a944acdd`), sans contenu ; je n'en ai rien ouvert. Les lignes du registre des GO rendues par recherche portaient sur
d'autres chantiers (organisme, bras A, saboteur) ; aucune ne portait de contenu de moniteur. La recherche du 14:45
dans `registres/decisions.md` a aussi rendu R-4703, ligne sur une course de lecture des sondes (« aboutie », coût,
empreintes) : je la consigne comme accès à une ligne de registre d'un moniteur, **sans aucune valeur, aucun seuil,
aucun résultat** ; je n'ai rien ouvert de ce qu'elle cite.

Scellé le 2026-11-22 à 15:00 UTC (`date -u`), avec la passation `relance-passation-2026-11-22-1500.md`. Fin du journal v1.
