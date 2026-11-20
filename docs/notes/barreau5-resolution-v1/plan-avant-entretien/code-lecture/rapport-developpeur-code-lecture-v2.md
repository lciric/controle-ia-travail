# Rapport du développeur du code de lecture du barreau 5 (plan « sabotage ou empreinte de l'adaptateur ») — v2

Écrit le 20 novembre 2026 par le développeur du code de lecture (Claude Opus 5.5, sous-agent de la session mère `session_01XJ6Mgr8BN6UanALsQatc5E`). Pièce d'instrument (classe B). Mandat `mandat-developpeur-code-lecture-v1.md` (`fffe5bd785705d54035c9a29cae6beef4ba8fedf0d4eca0ec17834b1dd48460b`, vérifiée) ; texte scellé `prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1.md` (`bdff244f1377e795b84f71518bb5e58fb1600fff8afee383d8f70c10d3f5d935`) ; contre-lecture v2 `contre-lecture-code-lecture-v2.md` (`f2f81f32efa1bb05cb138e5e5825f91467548b9efd2c17ede390c29e9893e680`, commit `cfa21a5b4`, lue en entier, avec ses outils). Le rapport v1 (`a140273f…`) n'est pas modifié (R12). Aucune donnée : modèle jouet et fichiers fabriqués seulement ; rien de `diag/` ; aucun réseau, aucune dépense, aucun commit (les commits intermédiaires sont ceux de la mère).

## En bref

- **L'amorce de l'instance de lecture est écrite** (`scripts/amorce_b5f_lecture_v1.sh`, fichier neuf), avec, côté session, la commande de création imprimée par le lanceur, la commande de destruction après preuve du versement et le contenu de la ligne `SCORES-B5F`. Essais neufs : blocs de l'amorce (50) et amorce entière à blanc (4), cas sain et artefacts.
- **Les corrections de la contre-lecture sont appliquées** : les quatre majeurs (M-1 à M-4) ; sur les huit mineurs, cinq corrigés (m-1, m-3, m-4, m-5, m-8), deux déclarés avec leur motif (m-6, m-7), un laissé tel quel pour l'additif (m-2) ; un essai neuf pour chacune des six mutations manquées (C1, C2, C3, C4, C5, C7), et un essai rapide pour C8 (m-8).
- **Essais** : [ESSAIS] **Mutations v2** : [MUTATIONS]
- **Trois points ne sont pas corrigés**, comme demandé : le niveau d'une issue sous huit familles, la tâche sans coût lisible chez un seul membre, la valeur de « [borne] » dans la phrase E (section 5).

## 1. L'amorce de l'instance de lecture

Écrite sur le modèle de `scripts/amorce_b5f_formation_v1.sh`, lue sans être modifiée (même découpage en blocs `# >>> nom` … `# <<< nom` joués par les essais, même minuterie par l'identifiant, même versement par un index séparé et `commit-tree`, même preuve par l'inventaire poussé et relu, mêmes essais local et à blanc). Ce que reçoit l'instance (point 7, deuxième tiret ; point 8) : le dépôt au commit de la marche, en extraction partielle nommée (code, les trois fichiers d'essais de la lecture, l'amorce et le lanceur de la lecture, la configuration scellée de la course de confirmation, le texte scellé, le registre propre, les seules tâches d'évaluation, les invites, et les adaptateurs existants cités) ; et, dans un clone à part, le seul dossier des entrées de lecture à leur commit. **Jamais** : `docs/notes`, `diag`, `runs`, `brouillons`, une marche de formation, la branche de la formation (clone à une branche ; toute référence qui la nomme : refus), la table, un coût d'un adaptateur tenu à l'écart.

Ce que le texte exige de l'instance, et où l'amorce le tient :

| exigence | où |
|---|---|
| un seul commit des adaptateurs tenus à l'écart | amorce, bloc `entrees` (`verifier_entrees`) : tête = `ENTREES_COMMIT` ; chaque fichier du dossier `entrees-de-lecture-b5f/` ajouté par ce seul commit (`diff-tree --root`, statut « A » pour tous, rien de modifié ni de retiré) ; aucun autre fichier extrait ; aucune référence à la branche de la formation. Côté session, `commande_de_creation` exige ce commit sur la branche distante des entrées |
| dans l'ordre des noms opaques | `relecture_v1.exiger_entrees` (changé, section 2) : noms `X-01` à `X-NN` sans trou (les noms de `engagement_v1.noms_opaques` sont contigus sur les adaptateurs présents) ; l'arbre d'un commit range ses fichiers par nom |
| fichiers réduits aux seuls tenseurs | `relecture_v1.exiger_tenseurs_seuls` (neuf) : en-tête `safetensors` lu sans charger les tenseurs ; aucune clé `__metadata__` ; seules des matrices `.A` et `.B` |
| minuterie qui ne détruit qu'après versement prouvé | bloc `minuterie` : à l'échéance d'arrêt plus un quart d'heure, DELETE par l'identifiant seulement si le témoin du versement final existe ; sinon état « stopped », disque gardé, signal pour la mère. Le témoin (bloc `preuve`, `temoin_final`) n'est écrit que si la marche est menée au bout, les sorties prouvées (inventaire poussé et relu au commit distant, chaque fichier à sa taille et à son empreinte) et les activations gardées versées |
| aucun score ni résumé dans les journaux | la marche n'imprime que des étapes, des comptes et l'empreinte de l'inventaire ; l'amorce n'écrit que des codes, des comptes, des commits et le contenu de `SCORES-B5F` ; le seul chemin par lequel un nombre tiré d'une sonde pouvait sortir (message du contrôle carte-processeur en échec) est fermé (m-3, section 3) ; les clés ne sont citées que par leur nom (essai à blanc : aucune valeur dans le journal, la sortie ni les fichiers poussés) |
| versement des fichiers fermés et ligne `SCORES-B5F` | bloc `versement` : liste blanche (`permis`), fichiers fermés, poids, inventaires, manifeste, résultats et traces d'abord, puis les activations gardées (règle « une_sur_dix ») par lots de 900 Mo au plus ; le contenu de `SCORES-B5F` (« commit <40> ; inventaire sha256 <64> ») est écrit au journal pour la mère, qui le recontrôle par `lancer_b5f_lecture_v1.sh scores` avant de l'inscrire |

Choix déclarés de l'amorce (sans texte qui les tranche) : disque de 150 Go pour la répétition générale (300 Go pour la relecture, devis, § 3) ; aucun versement pendant la marche (les fichiers fermés n'existent qu'à sa fin ; la marche est bornée par `timeout`, la minuterie veille à part ; attente par `wait` du seul processus lancé) ; règles de garde « trois_couches » et « couche_15 » : les activations vont sur le volume accordé (nœud 4), que l'amorce ne connaît pas, donc aucune destruction par la minuterie et un signal pour la mère ; deux aides réservées à l'essai à blanc (`B5F_VERSEMENT_S`, `B5F_MINUTERIE_UNE_FOIS`), refusées hors de lui. Rien n'est jamais supprimé.

Côté session (`relecture_v1`, sous-commandes de `lancer_b5f_lecture_v1.sh`) : `commande` imprime la création (bornes du devis sur l'offre, échéance d'arrêt au prix de l'offre, registre au commit de la marche avec « maintenant » pour instant de création, code du commit égal à celui de `CODE-LECTURE-B5F`, texte scellé, amorce telle qu'au commit en base64, adaptateurs existants présents au commit avec leur empreinte, arbre extrait propre (m-5), commit des entrées sur leur branche distante, garde de calcul) ; `detruire` imprime la destruction par l'identifiant après preuve de l'étiquette et du versement ; `verifier-destruction` ; `scores`.

Une faute de mon essai, corrigée : le premier passage de l'amorce entière à blanc échouait (2 sur 4) parce que l'essai cherchait la clé factice de l'instance dans le journal du faux `curl`, qui consigne ses propres arguments ; la clé y est par construction (en-tête d'autorisation). L'essai la cherche désormais partout ailleurs, et dans ce journal hors de l'en-tête d'autorisation : 4 sur 4.

## 2. Ce qui change dans les modules déjà rendus (commit `8c1d69188`)

Le contre-lecteur verra ces différences à la vérification. Aucun nom de fichier ne change : le code n'est pas figé (`CODE-LECTURE-B5F` n'est pas inscrite).

**`src/controle_ia/barreau5_familles/relecture_v1.py`**, pour l'amorce :
- `exiger_entrees` : après la vérification des compagnons, refus si les noms opaques ne sont pas `X-01` à `X-NN` sans trou, et `exiger_tenseurs_seuls` sur chaque adaptateur tenu à l'écart et d'apprentissage ;
- neuves : `exiger_tenseurs_seuls` ; `exiger_adaptateur_existant` (empreinte de 64 signes hexadécimaux exigée, chemin du dépôt sans « .. », hors de `docs`, `diag`, `runs`, sans `b5f-formation`) ; `exiger_config_lecture` l'appelle pour les adaptateurs de la répétition et les points d'ancrage, et refuse un nom de répétition en double ;
- section neuve « côté session » : constantes (`AMORCE`, `IMAGE`, `DEPOT_URL`, `BRANCHE_ENTREES`, `DOSSIER_ENTREES`, `ENTREES_DE_LA_MARCHE`, `PIECES_LECTURE`, `OFFRE_LECTURE`), `piece_lecture`, `exiger_offre_lecture`, `echeance_arret_lecture_s`, `exiger_code_du_commit`, `commande_de_creation`, `commande_de_destruction`, `ligne_scores`, `activations_gardees`, `precharger` ; `_session` reçoit les sous-commandes `commande`, `detruire`, `verifier-destruction`, `scores`, `gardees`, `precharger` ;
- pour m-5 : `motifs_de_l_amorce`, `_extrait`, `exiger_arbre_extrait_propre`, appelée par `verifier_avant_creation` (qui rend `arbre_extrait`) et par `commande_de_creation`.

**`src/controle_ia/barreau5_familles/lecture_v1.py`**, pour la contre-lecture : `lire` (M-1), `descriptifs` (paramètre `non_lu`), `audit_symetrie` (paramètre `lu`, clé `sondes_lues`), `phrases` (m-1, diagnostic « non lu »), constante `NON_LU`, `manipulation` (M-2), `exiger_arbre` (M-3, clé `compagnons`), `issue` (m-4) ; docstring du module.

**`src/controle_ia/barreau5_familles/sondes_v1.py`** : `controle_carte` relève la garde sans nombre (m-3).

**`scripts/lancer_b5f_lecture_v1.sh`** : en-tête (l'amorce est écrite, emportée par « commande », jamais jouée par le lanceur) ; sous-commandes `commande`, `detruire`, `verifier-destruction`, `scores` ; liste des refus.

**Essais** (noms gardés) : `tests/test_barreau5_familles_lecture_v1.py` (+12 essais, un étendu), `tests/test_barreau5_familles_sondes_v1.py` (+2), `tests/test_barreau5_familles_relecture_v1.py` (+3, pour l'amorce), `tests/test_lancer_b5f_lecture_v1.py` (refus étendus ; essais de la session, +2 pour la contre-lecture). Neufs : `tests/test_amorce_b5f_lecture_v1.py`, `tests/test_amorce_b5f_lecture_entiere_v1.py`.

## 3. Traitement des constats de la contre-lecture

Lignes : celles des fichiers dans l'état rendu ici. Chaque correction est défaite une à une par une mutation (K01 à K16, section 6) : l'essai cité l'attrape.

| constat | fichier | lignes | essai qui l'attrape |
|---|---|---|---|
| M-1, sondes lues sous « non interprétable » | `lecture_v1.py` | [L-M1] | `test_non_interpretable_rien_n_est_lu_des_sondes` (K01) |
| M-2, famille sans sur-saboteur dans M1 | `lecture_v1.py` | [L-M2] | `test_famille_sans_sur_saboteur_absente_de_toutes_les_epreuves`, étendu à M1 et M3 (neuf familles, seuil 1) (K02) |
| M-3, la table sous un nom de compagnon | `lecture_v1.py` | [L-M3] | `test_compagnon_orphelin_ou_faux_dans_l_arbre_de_lecture_refus` : cas sain, `table.sha256`, `scores/notes.sha256`, compagnon d'un autre contenu (K03, K04) |
| M-4, garde du code au commit sans essai | `lecture_v1.py` (inchangée) | [L-M4a] | `test_code_de_lecture_au_commit_cas_sains_et_artefacts` : trois cas sains, quatre artefacts, recette du sondage S4 (K15) |
| M-4, `verifier_avant_creation` | `relecture_v1.py` | [L-M4b] | `tests/test_lancer_b5f_lecture_v1.py::test_verifier_avant_creation_cas_sain_et_artefacts` : cas sain, commit illisible, registre sans épreuve, registre absent, marche orpheline, arbre de travail changé (K16, S02) |
| M-4, ouvreur sur la branche de la formation | `lecture_v1.py` (inchangés) | [L-M4c] | `test_preparer_depuis_une_branche_de_formation_fabriquee` : une marche, une famille, trois membres ; cas sain (coûts, marque des milliers, part non éditable, écritures, empreintes) ; copie `-x1` sans ligne de relance ; ligne de relance et première copie seule ; résultat « absente » ; ligne d'une autre copie (K12, K13, K14) |
| C1 | — (code juste) | — | `test_probabilites_rapportees_exactes_sur_un_cas_ecrit_a_la_main` (5/1024 et 1021/1024) |
| C2 | — | — | `test_petits_ecarts_sans_separation_apprise_etablie_issue_n` |
| C3 | — | — | `test_grand_ecart_negatif_sans_contraire_issue_n` |
| C4 | — | — | `test_epreuve_inscrite_apres_les_scores_refus` |
| C5 | — | — | `test_ouverture_d_une_autre_table_que_l_engagement_refus` |
| C7 | — | — | `test_manipulation_sur_les_seules_taches_communes` |
| m-1, niveau de 95 % dans la phrase ; « au plus » | `lecture_v1.py` | [L-m1] | `test_phrase_au_niveau_de_95_et_au_plus_au_niveau_de_e3` (K05, K06) |
| m-2, « [borne] » de la phrase E | non corrigé | — | question à l'additif (section 5) |
| m-3, écart mesuré écrit | `sondes_v1.py` | [L-m3] | `tests/test_barreau5_familles_sondes_v1.py::test_controle_carte_processeur_en_echec_sans_nombre_ecrit` (K07) |
| m-4, « niveau non atteignable » sous six familles de M1 ou M3 | `lecture_v1.py` | [L-m4] | `test_manipulation_sous_six_familles_motif_niveau_non_atteignable` (K11) |
| m-5, garde de l'arbre jouée côté session | `relecture_v1.py` | [L-m5] | `tests/test_lancer_b5f_lecture_v1.py::test_arbre_extrait_au_commit_sans_table_ni_ligne_de_la_formation` : table et ligne de coût dans un dossier extrait (refus, par `verifier` et par `commande`), la même table hors des motifs (acceptée), règles des motifs (K08, K09, K10) |
| m-6, instant de « création » | déclaré | — | voir ci-dessous |
| m-7, « chaque étape écrite avant la suivante » | déclaré | — | voir ci-dessous |
| m-8 (C8 vue par le seul jouet) | — | — | `tests/test_barreau5_familles_sondes_v1.py::test_sonde_d_un_pli_ne_note_que_les_taches_de_son_pli` |

Ce que font les corrections, précisément :
- **M-1.** Si la manipulation n'est pas établie : `c_separation_apprise` et `d_epreuves` valent `None` ; le diagnostic vaut `{"mot": "non lu", "motif": "manipulation non établie : rien n'est lu des sondes"}` ; les descriptifs sont calculés sur `ch` sans aucune notation (restent intensités, référence honnête du coût, écritures ; couches et comparaison portent ce motif ; aucun point d'ancrage) ; l'audit reste calculé, son déclencheur (iii), qui ne se juge que sur la séparation apprise, vaut `None` (« non lu ») et ne déclenche rien ; `sondes_lues` dit l'état ; la phrase du diagnostic dit « Diagnostic non lu ». Le chargement de l'arbre, ses gardes (série manquante, sonde du diagnostic absente) et les statuts « echec » des sondes restent : ce sont des gardes de la liste d'arrêt, sans aucun score. Sous six familles de E3 (point 13, issue N), la manipulation n'est jamais établie (M3 ne compte que des familles de E3), donc rien n'y est lu non plus.
- **M-2.** La différence de M1 (et de M3) n'est prise que pour une famille dont la table porte le jumeau et le sur-saboteur (point 17).
- **M-3.** Dans `exiger_arbre`, tout fichier `.sha256` de l'arbre doit être le compagnon d'un fichier inventorié ou de l'inventaire, et passer `scellement.verifier` ; sinon refus.
- **m-1.** La phrase de S, D et C se termine par « (au niveau de 95 %) » quand l'issue porte ce niveau ; « au plus » est l'erreur par sens du niveau propre de E3 (0,025 à sept familles, 0,005 sinon), même quand l'issue est à 95 % par M1.
- **m-3.** `controle_carte` relève une `GardeArret` qui ne porte que la sonde, le pli et « écart au-dessus de la tolérance », sans le message gelé (contexte supprimé).
- **m-4.** Le motif de NI dit « M1, niveau non atteignable : cinq familles » ; l'issue reste NI (le choix entre NI et N dans ce cas est laissé à l'additif).
- **m-5.** `exiger_arbre_extrait_propre` lit les motifs d'extraction dans l'amorce du commit de la marche, extrait au commit (par `git archive`, dans un dossier temporaire) les fichiers qu'ils prennent et les adaptateurs existants cités, et y joue `exiger_arbre_de_lecture_propre` (table par l'empreinte engagée et par sa forme, ligne de la formation d'une famille tenue à l'écart, marche de formation). La garde des références git reste celle de l'instance (son clone ne porte qu'une branche).

Déclarations motivées :
- **m-6.** Sur l'amorce : le commit de la marche est fixé dans la commande de création (`COMMIT`) ; `commande` lit le registre à ce commit avec « maintenant » pour instant de création, avant d'imprimer, et exige `ENGAGEMENT-B5F` antérieure ; le registre d'un commit fixé ne change plus, et l'instance le relit au même commit au début de la marche. La garde du point 9 tient donc à l'instant de la création, pourvu que la session joue la commande imprimée sans en changer le commit (l'échéance d'arrêt court depuis l'impression).
- **m-7.** Les étapes (b) à (g) sont calculées dans l'ordre, chacune sur les seules entrées des étapes précédentes, et le résultat est écrit une fois, scellé, à l'étape (h) : écrire chaque étape à part laisserait des fichiers non scellés après un refus en cours de lecture. Le fond (rien des sondes avant l'étape (b) établie) est tenu par M-1.

Les questions 1 et 3 de la contre-lecture sont réglées par la mère (formats des lignes fixés par ce code ; point 13 avant « non interprétable ») : rien n'est changé pour elles.

## 4. Ce qu'il faudra pour la course de lecture

- **Son commit.** La marche part d'un commit `COMMIT` d'une branche de code `BRANCHE_CODE` du dépôt de travail (clone à une seule branche, au commit). Ce commit : descend du commit cité par `CODE-LECTURE-B5F` et porte le même arbre gelé (`CHEMINS_GELES`) ; porte le registre propre avec, dans cet ordre, `SCELLEMENT-B5F`, `CODE-FORMATION-B5F`, `GO-FORMATION-B5F`, la relance s'il y en a une, `SORTIES-FORMATION-B5F`, `ENGAGEMENT-B5F` (après les sorties et la relance, avant la création), `CODE-LECTURE-B5F`, `EPREUVE-B5F` (même empreinte du programme), `GO-LECTURE-B5F` (égale à l'accord de la commande), et ni `SCORES-B5F`, ni `OUVERTURE-B5F`, ni `LECTURE-B5F`, ni `VERDICT-B5F` ; porte le texte scellé, la configuration scellée de la course de confirmation, l'amorce et le lanceur de la lecture, les trois fichiers d'essais, `tests/conftest.py`, les tâches d'évaluation et leur compagnon, les invites, et les adaptateurs existants à leurs chemins ; ce qu'il en extrait passe `exiger_arbre_extrait_propre`. La branche de la course de formation (`course/barreau5-formation-v1`) ne porte pas le code de lecture : la course de lecture part d'une autre branche, qui le porte.
- **Son plancher d'essais : 137** (`MIN_ESSAIS` de l'amorce) = 95 (`tests/test_barreau5_familles_lecture_v1.py`) + 18 (`…_sondes_v1.py`) + 24 (`…_relecture_v1.py`). `tests/test_amorce_b5f_lecture_v1.py` exige l'égalité avec le compte collecté : tout essai ajouté à ces trois fichiers se reporte dans l'amorce au même commit.
- **Ses motifs.** Les trois fichiers, nommés (amorce, bloc `motifs`, et l'étape 5), jamais le motif `tests/test_barreau5_familles_*.py` : l'instance de lecture n'extrait pas les essais de la formation, et ce motif, joué sur un commit qui porte le code de lecture, ferait échouer l'essai du plancher de la formation (`test_texte_plancher_d_essais_egal_au_nombre_d_essais_du_paquet` : le compte n'y serait plus 235). Rien n'est touché côté formation ; une relance de la formation doit, elle aussi, partir d'un commit sans le code de lecture.
- **Ses entrées.** Branche `donnees/barreau5-familles-jumelles-v1-entrees-de-lecture` sur le dépôt distant ; dossier `entrees-de-lecture-b5f/`, écrit par `engagement_v1.preparer_entrees_de_lecture` (adaptateurs tenus à l'écart `X-NN.safetensors`, adaptateurs d'apprentissage `A<k>-<membre>.safetensors`, épisodes `A<k>-saboteur-evaluation.jsonl`, chacun avec son compagnon), ajouté en entier par un seul commit `ENTREES_COMMIT`, qui n'ajoute rien d'autre (je recommande une branche sans histoire, d'un seul commit : un commit parent qui porterait déjà le dossier, ou un fichier hors du dossier, est refusé). Aucune ligne de cette branche ne vient de la branche de la formation.
- **Ses adaptateurs existants** (points d'ancrage du plan décisif, ou les quatre adaptateurs de la répétition, donnés par la mère) : une liste `{nom, chemin, sha256}`, chemins présents au commit de la marche ; une empreinte absente ou illisible est refusée (configuration, commande, amorce).
- **Le reste.** Branche de sortie `donnees/barreau5-familles-jumelles-v1-lecture` (répétition : `…-repetition`) absente du dépôt distant ; offre A100 SXM4 80 Go dans les bornes du devis, disque de 300 Go (répétition : 150) ; ligne d'accord dans `registres/go.md` pour la garde de calcul ; `GH_TOKEN` et `HF_TOKEN` passés par leur nom ; après la marche, `lancer_b5f_lecture_v1.sh scores` puis l'inscription de `SCORES-B5F` par la mère ; pour une règle de garde autre que « une_sur_dix », le versement des activations sur le volume avant toute destruction (nœud 4).

## 5. Trois points laissés tels quels, pour l'additif

Le texte ne les tranche pas ; un additif écrit par Fable les fixera. Le code n'y est pas touché.
1. **Niveau d'une issue sous huit familles** (question 2 de la contre-lecture) : le code prend le plus faible de M1, M3 et des épreuves que l'issue affirme (S : E1, E2a, E2b, E3 ; D et C : E3). Lié : m-4, le choix de NI ou de N quand M1 ou M3 a moins de six familles (le motif le dit désormais ; l'issue reste NI).
2. **Tâche sans coût lisible chez un seul membre** (question 4) : le code garde la tâche aux autres membres (chaque membre sur les tâches communes où il a au moins un coût lisible).
3. **« [borne] » de la phrase E** (m-2, cinquième question) : le code écrit le plus grand écart signé de E3, jamais négatif, mais qui peut être minuscule.

## 6. Essais et mutations

Commande (copie de travail du dépôt, temporaires sous `/dev/shm`) : `TMPDIR=/dev/shm PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src .venv/bin/python -B -m pytest -q -p no:cacheprovider --basetemp=/dev/shm/<nom> <fichiers>`.

[RESULTATS-ESSAIS]

Mutations : `outils-developpeur-code-lecture-v1/mutations-code-lecture-v2.py`, même procédé qu'en v1 (copie de travail unique ; témoins sans mutation exigés verts ; « attrapée » si pytest rend 1 ; chaque « avant » trouvé une fois exactement). Sortie : `outils-developpeur-code-lecture-v1/sortie-mutations-code-lecture-v2.md`.

[RESULTATS-MUTATIONS]

Syntaxe : les fichiers Python changés compilent sous Python 3.11.18 (`verifier-syntaxe-v1.py`), l'amorce et le lanceur sous `bash -n`.

## 7. Ce qui menace le gel à H+30 h

1. `lecture_v1.py` change (M-1, M-2, M-3, m-1, m-4) : l'empreinte que portera `CODE-LECTURE-B5F` est celle de l'état final ; l'additif (section 5), s'il change le code, la change encore : l'épreuve à vérité plantée se joue après le dernier changement.
2. L'additif doit précéder la seconde programmation et l'épreuve à vérité plantée.
3. L'amorce n'est contre-lue par personne ; m-6 s'y juge.
4. La branche des entrées (un seul commit, sans histoire) et son commit doivent exister sur le dépôt distant avant la commande de création ; la convention est la mienne.
5. Le plancher de 137 essais est lié aux trois fichiers ; une relance de la formation depuis un commit qui porte le code de lecture ferait échouer l'essai du plancher de la formation.
6. `exiger_arbre_extrait_propre` n'a jamais été jouée sur le dépôt réel (je ne lis pas ses dossiers) : la première fois sera le `verifier` de la mère ; un JSON extrait qui porterait « famille : T0x » avec « membre » ou « cout » l'arrêterait : à jouer tôt, sans dépense.

## 8. Fichiers

[FICHIERS]
