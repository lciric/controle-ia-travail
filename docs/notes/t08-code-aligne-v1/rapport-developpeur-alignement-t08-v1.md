# Rapport du développeur — alignement du code de T0.8 sur la pièce « mots et coût » inscrite — v1

- **Auteur** : développeur neuf (modèle A), session `session_013QMaymaQLzKJsDBnmrEZ7q`, lancé par la session mère `session_013QMayjbmQUdDuDs2S3i3XD`. Classe B (instrument).
- **Consignes** : `brouillons/t08-texte-complet-fable-v1/consigne-alignement-code-t08-v1.md` (`0e643d7e…5f3f`, commit `ec6312d9`), puis sa **version 2** (`consigne-alignement-code-t08-v2.md`, `0ffb2953…aa46`, commit `89ed1a93`), reçue en cours de travail ; empreintes vérifiées sur leurs compagnons ou par `git show`.
- **Branche** : `prep/t08-code-aligne-v1`, tirée de `main` à `82640390` (qui contient le commit de la pièce `da06bb57`). **Divergence de nom déclarée** : la v1 de la consigne disait `prep/t08-code-v2` ; l'ordre de la mère et la v2 disent `prep/t08-code-aligne-v1`, retenu.
- **Commits** : code aligné `<<COMMIT_CODE>>` (seuls `src/controle_ia/t08/` et `tests/test_t08_*` changent par rapport à `main`) ; pièces de ce rapport dans des commits suivants, sous `docs/notes/t08-code-aligne-v1/`.
- **Aucune dépense, aucune instance, aucun réseau hors `git`** ; aucun refus d'outil.

## 1. Ce que j'ai lu, ce que je n'ai pas ouvert

Lu : `CLAUDE.md` ; la tête de `registres/etat.md` (routine) ; les deux consignes ; du brouillon 11 de T0.8 l'en-tête, la « Métrique » (paragraphes M2, MC, score, en une passe, avec raisonnement), la section « Depuis le gel du 10 novembre » (« Code », « Gardes de code ») et la ligne de la table des marqueurs (le brouillon 12 n'a pas été ouvert : la v2 dit que sa section « Code » dit la même chose) ; le code au commit `453a71e1` (`src/controle_ia/t08/`, `tests/test_t08_*_v1.py`) ; de ses rapports, la commande et le bilan de l'essai de bout en bout et le banc de mutations `mutations-corrections-2-t08-v1.py` ; `scripts/mots_et_cout_t06_v3.py` (en-tête, modules gelés, partie « contrat lu par T0.8 ») ; son fichier d'inscription ; la seule ligne `CODE-MOTS-ET-COUT-T06` de `registres/scellements-v1.md` (le fichier entier n'est ouvert que par le lecteur de registre de T0.8 dans deux essais) ; `tokenizer.json` de la branche `donnees/tokeniseur-llama-3.1-8b-instruct-v1` par `git show` (`79e3e522…b2b4`, égal à son compagnon).

Pas ouverts : aucun fichier de `diag/`, `runs/`, `donnees/` d'une course réelle ; aucune branche `calcul/…` ni `verdict/…` ; rien de `docs/verdicts/` ; aucune pièce du saboteur, du bras A ni du bras d'attaque ; R-D15 et R-D16 dans les rapports de la pièce (non ouverts : leur contenu est repris dans la section « Code » du brouillon 11) ; aucune recherche récursive large (seules des listes de noms de `git ls-tree` sur la branche du tokeniseur, pour trouver le chemin de `tokenizer.json`).

## 2. Ce que fait l'alignement (fichier par fichier, par rapport à `453a71e1`)

| fichier | changement | raison |
|---|---|---|
| `src/controle_ia/t08/mots_et_cout_v1.py` | marqueur `CODE_MOTS_ET_COUT_T06` à cinq clés (`commit`, `fichier_inscription`, `sha256_inscription`, `module`, `sha256_module`), contrôlé par `exiger_forme_marqueur_piece` ; `verifier_inscription` joue (a) à (e) dans l'ordre de la consigne ; `charger_module_par_chemin` charge le module par son chemin, en exécutant les octets dont l'empreinte vient d'être vérifiée, sans `sys.path`, sans nom de module cherché, sans cache d'octets ; après chargement : `sys.path` inchangé et `GardeArret` de la pièce = celle du paquet, sinon arrêt ; tout échec rend `sys.path` et `sys.modules` tels qu'avant ; chemins hors de la racine refusés ; `charger_piece(mode, marqueur, racine, ligne)` ; `Piece.inscription` porte les contrôles faits. Pièce jouet, contrat, contrôle d'identité, fonctions de la pièce jouet : inchangés. | R-D15, R-D16 ; consigne § 2, points 1 à 3 |
| `src/controle_ia/t08/configuration_v1.py` | `exiger_marqueurs` délègue la forme de `CODE_MOTS_ET_COUT_T06` à `exiger_forme_marqueur_piece` | forme alignée |
| `src/controle_ia/t08/lecture_v1.py` | `_exiger_ligne_piece` (point (a)) remplace la comparaison « quatrième cellule = empreinte du module » dans l'étape (a) et le passage à blanc ; `passage_a_blanc_reel(..., racine_piece=None)` : avec le dépôt, joue en plus (b) à (e) et le chargement par chemin (aucune fonction de la pièce appelée) ; `executer_lecture` en mode réel lit la ligne au registre de la liste blanche et charge la pièce par `charger_piece`, et refuse une pièce passée qui n'a pas été chargée ainsi ; `r["entrees"]["piece_mots_et_cout"]` consigne les contrôles (`None` en jouet) | consigne § 2, point 1 ; une garde neuve (refus d'une pièce passée non contrôlée), plus stricte, ne change aucune étiquette ni seuil |
| `src/controle_ia/t08/essai_jouet_v1.py` | le registre factice cite un fichier d'inscription factice (`registres-factices/code-mots-et-cout-t06-jouet.json`) au lieu du module : forme du registre réel | fidélité de l'essai de bout en bout |
| `tests/test_t08_alignement_piece_v1.py` (neuf) | cas sain sur le dépôt (ligne réelle, inscription, module chargé par chemin, imports inchangés) ; artefacts (a) à (e), ordre des points, rien d'écrit, aucun module laissé ; chargeur (exécution qui casse, `sys.path` touché, autre `GardeArret`, contrat incomplet, enveloppe refusée hors du paquet, empreinte relue) ; chemins hors racine ; **contrat** : enveloppe et pièce inscrite, mêmes centres, états et scores, bases (A) et (B) | § 2, points 1, 2 et 4 |
| `tests/test_t08_tokeniseur_balise_v1.py` (neuf) | Q-4 sur le tokeniseur réel (§ 3 ci-dessous) | § 2, point 6 |
| `tests/test_t08_mots_et_cout_v1.py` | refus du jouet en mode réel par une inscription conforme | forme alignée |
| `tests/test_t08_entrees_rendu_v1.py`, `tests/test_t08_gardes_corrections_v1.py`, `tests/test_t08_lecture_course_v1.py` | marqueurs factices à la forme alignée ; artefacts neufs (forme d'avant, ligne qui cite le module, autre empreinte, autre chemin) ; passage à blanc avec `racine_piece` ; lecture réelle qui refuse une pièce non contrôlée | forme alignée, gardes neuves |

**Ce qui ne change pas, prouvé par programme** (`preuve-inchange-t08-v1.py`, sortie au § 4) : aucune constante en capitales changée ni retirée dans les quatre fichiers changés (cinq ajoutées dans `mots_et_cout_v1.py`, déclarées) ; seules les fonctions déclarées ci-dessus changent ; `VALEURS_GELEES_COURSE`, `VALEURS_GELEES_LECTURE` et `MARQUEURS` évalués aux deux commits : égaux ; `tables_v1.py` (phrases des tables D et F) inchangé à l'octet ; `src/controle_ia/bases/` égal à `main` (`sequentiel.py` à `35a09834…`) ; pièce et fichier d'inscription aux empreintes du brouillon 11. Pièce jouet : laissée où elle est (elle vit dans le module de l'enveloppe ; son emplacement ne gêne aucune vérification).

**Modules importés (consigne v2, constat M-6)** (`modules-importes-t08-v1.py`) : fermeture des imports du code de T0.8 et de la pièce (imports dynamiques par nom compris), 70 fichiers de `src/controle_ia/` ; tous **égaux à l'octet** à `453a71e1`, sauf les quatre fichiers alignés ci-dessus. Les quatre chemins exigés (`bases/`, `t06/cout.py`, `t06/test_croise.py`, `environnements/propositions.py`) : égaux à l'octet.

## 3. Arrêt à la balise sur le tokeniseur réel (Q-4) — constat déclaré

Avec le tokeniseur réel (`79e3e522…`), la balise se tokenise `<s|and|bag|ging|_conf|idence|>`.

1. **Tient** : balise précédée de 28 textes (rien, saut de ligne, espace, tabulation, texte, ponctuation, chiffres, fragments de la balise…) et suivie de chacune des 101 valeurs, avec trois fins : la génération s'arrête au jeton où la balise apparaît, la coupe est « balise », et le jeton suivant est celui de la valeur (8 484 cas). Balise écrite en jetons non canoniques : 3 000 découpages tirés parmi les **454 740** que permet le vocabulaire : même chose.
2. **Constat (ni corrigé, ni une règle changée)** : quand la balise est suivie, dans le même mot du prétokeniseur, d'un **saut de ligne** ou d'une **ponctuation** (`>\n`, `>\n\n`, `>.`, `>:`, `>"`, `>'`, `>-`, `` >` ``, `>(`, `>=`, `>%`, `><`, `>>`, `></`), le tokeniseur fusionne `>` avec ce caractère en **un seul jeton**. La détection **ne manque pas** la balise : elle la voit et arrête la génération à ce jeton ; mais la balise finit **dans** le jeton (état « à cheval ») ; le code rend alors une **anomalie sans score** (`ANOMALIE_A_CHEVAL`, code de `453a71e1`, inchangé) et **aucune valeur n'est lue au jeton suivant**. Suivie d'une espace, d'une tabulation, de `**`, d'un tiret long ou d'un chiffre : « balise », lecture normale. **Ce que je ne sais pas** : la fréquence de « `<sandbagging_confidence>` puis saut de ligne » dans la génération des juges ; le texte (brouillon 11, « Avec raisonnement ») ne nomme pas ce cas (« à cheval » n'y figure pas). **Nœud pour la mère et le rédacteur** : la règle d'une lecture « à cheval » (anomalie sans score aujourd'hui) est du code, non du texte.

## 4. Essais (nombres)

- Essais de T0.8 (`tests/test_t08_*_v1.py`, dix fichiers) : **166 réussis**, deux passes : `<<PASSES>>`. Avant l'alignement, au portage : 142 réussis (huit fichiers de `453a71e1`, sur `main`).
- Banc de mutations (`mutations-alignement-t08-v1.py`, sortie `mutations-alignement-t08-v1-sortie.txt`) : témoin sans mutation 166 réussis ; **38 mutations, 38 tuées** (les 21 du banc de `453a71e1`, toutes applicables, et 17 neuves A01 à A17), 0 survivante, 0 inapplicable. Deux réglages déclarés du banc : le conftest copié perd la ligne d'import du greffon des échecs connus (liste propre à la suite entière ; aucun essai de T0.8 n'y figure) ; le registre, l'inscription et le module de la pièce sont copiés, non liés (un lien sortirait de la racine, ce que la garde refuse). Deux premiers passages du banc rejetés : témoin en erreur (code 4) — le banc s'arrête désormais si le témoin échoue (garde ajoutée, R5).
- Essai de bout en bout sur le modèle jouet, deux fois (`H=20261122-190746`, `E=335478590226277757345460670410651332604`, commit `04b4edfa`) : codes 0 et 0 ; **53 fichiers** (52 à `453a71e1`, plus le fichier d'inscription factice) ; 7 exclus déclarés (manifestes et compagnons) ; **0 différent** ; `controle_tables_par_racine` vrai et vrai ; déterministe. Sortie `essai-bout-en-bout-alignement-t08-v1-sortie-b.json`, inventaire des fichiers des deux racines (noms et empreintes) `…-inventaire.txt` ; les racines (67 Mo de sorties factices) sont sorties de l'arbre, non versées.
- Suite du dépôt : `<<SUITE>>`.

## 5. Ce que je n'ai pas pu vérifier

- Le passage à blanc sur le registre réel complet et la lecture réelle de bout en bout : hors de la consigne (§ 5) ; `passage_a_blanc_reel(..., racine_piece=dépôt)` est prêt pour la mère.
- L'égalité « enveloppe = pièce » est éprouvée sur données factices seulement.
- Le tokeniseur du modèle de 3 milliards : non revérifié (le texte le dit déjà).
- Routine de reprise : `verifier-arbre` sur `main` rend 96 écarts préexistants (non traités ici) ; l'inventaire des instances est laissé à la mère.

## 6. Valeur du marqueur `COMMIT_CODE_T08`

`<<VALEUR>>`
