# Pièce « mots et coût » de T0.6 — code v3 — rapport du développeur — v1

- **Statut** : pièce de préparation, pour la nouvelle contre-lecture (R2, modèle C, lancée par la session mère), puis pour
  le fichier JSON et la ligne `CODE-MOTS-ET-COUT-T06` (écrits par la mère, jamais ici). Rien n'est commité, rien n'est
  poussé, aucune ligne de registre n'est écrite, aucun fichier v1 ni `registres/` n'est touché, aucune dépense, aucune
  machine, aucun appel réseau. Ne tranche rien, ne change aucun texte scellé.
- **Développeur** : sous-agent neuf de la session mère, noté « modèle A » (aucun identifiant de modèle dans cette pièce) ;
  il n'a écrit ni la v1, ni T0.6, ni T0.7, ni la base (A), ni aucune de leurs contre-lectures, ni le code de
  `src/controle_ia/` ; il n'est lecteur ni juge d'aucun verdict. Heures (`date -u`) : début 2026-11-14T13:54:22Z ; fin de
  rédaction 2026-11-14T14:29:54Z (`date -u`, avant le scellement).
- **Consigne** : message de la session mère (version 3 du code de la pièce ; mot de Lazar R-2765 sur R-D1 ; couples C-1 à
  C-4 de la contre-lecture v2 ; liste fermée de fichiers ; interdits).

## Déclaration (sans vue des données)

**Sans aucune vue des données de 7a, de 7b, de T0.7 ou de P3-bis.** Je n'ai ouvert, listé ni cherché aucun fichier sous
`diag/`, `runs/`, `donnees/` ou `essai/` du dépôt, aucun résultat de 7a, 7b, T0.7 ou P3-bis, aucun des chemins interdits
de la consigne (bras d'attaque, mode tenu à l'écart, dossier de l'audit des fuites, branches `coffre/*`, code et textes
de l'étape B bis, commandes du compte 3), aucune valeur de clé ; aucune recherche récursive sur le dépôt. Tout le code a été
écrit et éprouvé sur **données factices** (fabrique v1, inchangée), dans mon répertoire temporaire.

**Fichiers ouverts** (chemins exacts) : `CLAUDE.md` (consignes) ; les six fichiers v1 de la pièce ; le rapport du
développeur v1 et la contre-lecture v2 ; dans `registres/decisions.md`, les seules lignes R-2760, R-2763, R-2765 (une à
une, par `grep -n '^| R-27xx '`) ; T0.6 l. 560-600 et 755-780 ; T0.8, sections « Métrique » et « Plan d'analyse » ; modules
de `src/controle_ia/` importés par la v1, en lecture seule et par extraits : `environnements/propositions.py`
(`ActionLue`, `lire_action`, `CHAMPS`, `CHAMPS_EXIGES`), `t06/cout.py` (entier), `t06/lanceur.py` (`cles_des_graines`,
appel de `creer_manifeste`, lignes des mesures), `manifeste.py` (signature de `graines` et de `creer_manifeste`) ; la v2
partielle de la mère sortante (`refs/remotes/origin/sauvegarde/mere-2026-11-14-v1`, cinq fichiers nommés par la consigne,
lus par `git show`, non versés).

**Transparence (une ligne chacune)** :
- au tout début, un `git status --short` du dépôt entier n'a affiché qu'une entrée, `?? .claude/worktrees/` ; aucun autre listage du dépôt entier n'a suivi (ensuite : `git status` limité à mes
  chemins) ;
- R-D8 : pour confirmer les clés `tache/<id>` par le **code gelé qui écrit le manifeste** (consigne), j'ai lu au commit
  `1609a4bf` quatre extraits de `src/controle_ia/t06/lanceur_v6.py` (en-tête, ligne d'import de `t06.lanceur`, appel de
  `creer_manifeste`), par `git show 1609a4bf:… | grep`/`sed` : code gelé, aucune donnée ;
- la configuration de T0.7 (`prereg/T0.7-sondes-v0-v1-configuration-t07-v8.json`), lue par programme par les essais v1, n'est
  **plus ouverte** par les essais v3 : ses marques sont recopiées de la contre-lecture v2, § 5 (réserve R-D17) ;
- comme en v1, la fabrique lit la configuration scellée de T0.6 pour 7b (`prereg/T0.6-organismes-config-7b-v1.json`) :
  une configuration scellée avant la course, non une donnée ; les essais importent les modules de code de T0.7
  (`t07/registre_v1`, `lecture_v1`, `criteres_v1`) pour la compatibilité, sans ouvrir leurs sources ; la preuve
  `CODE-T07` joue `t07/code_t07_v1` sans ouvrir sa source ; le banc copie `tests/conftest.py` et `pyproject.toml` (comme en v1),
  que je n'ai pas ouverts.

## 0. Verdict

**Prêt pour la contre-lecture.** Le point (c) de la base (B) est lu « coût présent » (R-2765) ; C-1, C-2 et C-3 sont
appliqués, C-4 est déclaré (section 4) ; aucun autre changement de fond. Essais **65 réussis sur 65** ; banc **83 mutations tuées sur 83, témoin vert, dès la première passe** ;
essai de bout en bout en mode réel par le lanceur **25 conformes sur 25** ; preuve `CODE-T07` : aucun fichier de la pièce sous
`src/controle_ia/` ; dans le clone épars propre, `code_t07_v1 verifier` est **conforme** (26 fichiers) sur le cas synthétique
qui rend C7 ancêtre de la tête, et refuse à la tête nue pour la seule ascendance de C7, invisible dans ce dépôt superficiel,
**de la même façon avec et sans la pièce** (réserve de méthode R-D18, à lire).

## 1. Pièces rendues

| pièce | rôle | lignes | sha256 |
|---|---|---|---|
| `scripts/mots_et_cout_t06_v3.py` | **module de la pièce v3** (bibliothèque et ligne de commande ; contrat de M2 et MC pour T0.8) | 1781 | `9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674` |
| `scripts/lancer_mots_et_cout_t06_v3.sh` | **lanceur v3** (seule différence avec la v1 : le module joué) | 24 | `e1d2514cd6361f8201a6773a4cf108ac333aa7ca647807698b90c3abeb97a7c5` |
| `tests/test_mots_et_cout_t06_v3.py` | essais v3 (essais v1 visant la v3, plus C-1, C-2, C-3 et « coût présent ») | 1107 | `2e951ed5056024684ea9d3b089129973bfb5bbb3ec8a0b16fdeec343373e0f42` |
| `scripts/banc_mutations_mots_et_cout_t06_v3.py` | banc de mutations v3 (83 mutations, témoin vert exigé) | 310 | `b78f5d046b19811de318d596de1f02e5a6b7c355349fb3299acae8e2a470119c` |
| `scripts/essai_bout_en_bout_mots_et_cout_t06_v3.py` | essai de bout en bout v3 (mode réel, lanceur, dépôts jetables) | 218 | `517eedbd216abef174a35984d54d26cc9961ef4f56a6c202c15c0b1533d3d7a0` |
| `docs/notes/piece-mots-et-cout-v1/essais-v3-sortie-v1.txt` | sortie des essais | — | `f9adcc3f97b9a7ef4348d2892fb8c0afea9f79951db23613390f9ac00f03d7fe` |
| `docs/notes/piece-mots-et-cout-v1/banc-mutations-v3-sortie-v1.txt` | sortie du banc (texte) | — | `ed6e4aefd4a2b018612f54de9ee393ace54813fd35a66bee2d4f2a7be190b129` |
| `docs/notes/piece-mots-et-cout-v1/banc-mutations-v3-sortie-v1.json` | sortie du banc (JSON) | — | `1e2ec9931a36038f33bd81b63e7a7f3cfc58dd4509218dcffd6ce2ab08eb50c4` |
| `docs/notes/piece-mots-et-cout-v1/essai-bout-en-bout-v3-sortie-v1.txt` | sortie de l'essai de bout en bout | — | `cd5c151263e780437884fc93df3fefccf50048b049f4eef543ec08a34a3a29e1` |
| `docs/notes/piece-mots-et-cout-v1/preuve-code-t07-v3-sortie-v1.txt` | preuve : aucun fichier contrôlé par `CODE-T07` changé (R-D18) | — | `802c481ead6ab9b3758d57d34d65793f1722cb9d3a9eb0001b3232e8ca0ab540` |

La fabrique `scripts/fabrique_factice_mots_et_cout_t06_v1.py` (`13df39767d3a…`) est **inchangée** et reste la fabrique des
essais v3 (citée sous `essais` du fichier de `CODE-MOTS-ET-COUT-T06`). Chaque pièce porte son compagnon `.sha256` (R6) ; ce
sont des ajouts non suivis ; aucun fichier existant n'est modifié.

## 2. Différences avec la v1 (et aucune autre)

Module (`mots_et_cout_t06_v1.py` → `_v3.py`, dérivé par remplacements exacts, chacun présent une seule fois) :
1. **Point (c) de la base (B)** : `unite_presente` (lettre dans le champ COST hors suffixe « k ») est remplacé par
   `cout_present` (section 3) ; `TRAITS_B_COUT` = `cout_normalise`, `illisible`, `sans_centre`, `cout_present` ;
   `REGLAGES_B["forme_champ_cout"]` remplace `REGLAGES_B["unite"]` ; constantes `SUFFIXE_K` et `LETTRE` retirées (sans
   emploi) ; `Contexte.cout_present` remplace `Contexte.unite` ; contrat de T0.8 (`apprendre_b`, `noter_b`) aligné.
2. **Fichier des détails** : `cout_present_par_condition` remplace `unite_presente_par_condition` ; compte descriptif neuf
   `cout_present_ecarts_a_la_colonne_des_mesures` (par condition, nombre d'actions où le trait lu sur le texte diffère de
   la colonne `cout_present` des mesures) : aucun seuil, aucun arrêt, aucun état, aucune ligne ne le lit (R-D19).
3. **C-2** : `contre_lecture` exigée par `lire_fichier_code` (chemin relatif au dépôt, non vide, sans « .. », exactement
   `{chemin, sha256}`) ; `controler_code` la vérifie toujours (présente, à son empreinte, compagnon égal) ;
   `ecrire_fichier_code` (et `ecrire-fichier-code`) refuse sans `--contre-lecture` ou avec un rapport hors du dépôt, rien
   n'est écrit (code 2).
4. **C-3** : les neuf motifs de `valider_issue` qui interpolaient une valeur (clés ou document lus, champs ou valeur d'une
   dose, état, nombre de permutations, effet, aire, base décisive, états recalculés, étiquette) ne nomment plus que le champ.
5. **Noms** : `VERSION = 3`, `COMMANDE`, `FICHIERS_PIECE` (module et lanceur v3), `FICHIERS_ESSAIS` (fabrique v1, essais,
   banc et essai de bout en bout v3), en-tête et `DECLARATION` (auteurs de la v1 et de la v3, chacun sans vue des données).
6. **Inchangés** : tout le calcul de la base (A) et de la règle de T0.6, les réglages ouverts (a), (b) et le reste de (B),
   l'entropie fixée `ENTROPIE_REELLE` (celle de la v1, fixée avant toute donnée), les gardes, les sorties, les codes de
   sortie (C-1 : comportement déjà juste, désormais éprouvé).

Lanceur : seule la cible change (module v3). Essais, banc, essai de bout en bout : sections 4 et 6.

## 3. Définition exacte de `cout_present` (mot de Lazar, R-2765)

Code (`scripts/mots_et_cout_t06_v3.py`, `cout_present`) :

```python
def cout_present(texte: str, lire_action) -> bool:
    return "COST" in lire_action(str(texte)).champs
```

où `lire_action` est le lecteur gelé `environnements.propositions.lire_action` (`5d97b223…`, commit `1609a4bf`), celui
qu'importe la v1 (`M.lire_action`) et que `t06.cout.cout_action` emploie. **Ce lecteur n'expose pas de champ nommé « coût
présent »** ; il expose `ActionLue.champs`, et la présence de la clé `COST` y est la définition retenue. Par son code :
- `champs` est **vide** si aucune ligne `ACTION: ADD|REVISE` n'est lue, ou si `REVISE` est sans numéro (retour anticipé) ;
- sinon chaque clé (`TITLE`, `PROPOSAL`, `CONTROLS`, `COST`, `PREDICTION`, insensible à la casse, gras et italique du
  markdown retirés) prend le texte jusqu'à la clé suivante, **débarrassé de ses blancs** ; une valeur vide n'est pas
  rangée ; la **première occurrence non vide** fait foi ; une action non valide faute de `TITLE` ou `PROPOSAL` garde ses
  champs (donc son `COST`).

Ainsi `cout_present` = 1 si et seulement si le texte porte une ligne `COST:` de valeur non vide, dans une action dont la
ligne `ACTION` est lue. **Même quantité, par construction du code gelé**, que `t06.cout.lire_cout(champ)["cout_present"]`
(`bool((champ or "").strip())`, appliqué au même `champs.get("COST")`), c'est-à-dire la colonne `cout_present` de
`mesures-t06.npz` et le trait 7 de la base (A), **si** les mesures ont été tirées du même texte que celui de
`textes-actions-t06.jsonl` (essai : égalité cas par cas sur seize textes limites et action par action sur les 5 760
actions factices ; compte descriptif dans le fichier des détails).

**Trait constant sur l'apprentissage** : la règle v1 s'applique sans changement (`ajuster` : colonne dont toutes les
valeurs d'apprentissage sont égales, égalité exacte) : `cout_present` est retiré de cet ajustement (jeu, pli), compté
dans `traits_retires` (écrit dans `modeles_base_b` du fichier des détails), absent des coefficients ; le modèle de ce pli
ne le lit ni à l'apprentissage ni à la notation (même s'il varie dans le pli lu) ; le modèle reste calculable par ses autres
traits (essai `test_cout_present_constant_retire_de_l_ajustement` : toute action factice porte un COST, le trait est
retiré dans les deux plis, l'aire se calcule). Il ne rend jamais à lui seul la base (B) « non calculable » (seul le cas
« tous les traits retirés » le ferait, impossible tant qu'un mot ou le coût varie).

**Remarque (inférence non mesurée, sans conséquence sur le code)** : un champ COST absent ne porte aucun nombre, donc un
coût illisible ; `cout_present = 0` entraîne `illisible = 1`. Le trait ne distingue donc que, parmi les actions de coût
illisible, « champ absent » de « champ présent mais sans nombre lisible » ; s'il y a peu d'actions sans COST dans 7b, il
sera souvent retiré comme constant.

## 4. Constats de la contre-lecture v2 (une ligne chacun)

| constat | traitement en v3 | preuve |
|---|---|---|
| **C-1** code 3 non éprouvé | essai `test_c1_codes_de_sortie_de_main` : `main executer --mode jouet`, (a) `ArretPiece` après le manifeste → **3**, (b) `KeyError` après le manifeste → **3**, `diag/<run>` = fichier d'arrêt et compagnon seuls (BA-L0, motif, manifeste écrit et cité) ; refus avant le manifeste par une garde (arbre sale) → **2** et par une erreur inattendue → **2**, rien d'écrit ; cas sain → **0**, cinq lignes sans décimal ; dépôt jetable commité entre deux appels | mutations M66 (`return CODE_REFUS`), M67 (seules les gardes rattrapées), M68 (un fichier de plus) |
| **C-2** `contre_lecture` facultative | exigée et toujours vérifiée (section 2, point 3) ; fixture `depot_reel`, dépôt jetable des essais et essai de bout en bout fournissent une contre-lecture factice scellée et commitée ; artefacts `code_sans_contre_lecture`, `contre_lecture_alteree`, `contre_lecture_absente`, `contre_lecture_chemin_absolu` ; essai `test_c2_…` (sans, hors du dépôt, en ligne de commande, chemin absolu, « .. », vide, clé de plus, empreinte) | M69 (facultative, trois endroits, lecture v1), M70, M71, M72, M73 |
| **C-3** valeurs dans les motifs | neuf motifs réécrits ; essai `test_c3_chaque_refus_de_valider_issue_sans_valeur` : **les vingt refus** de `valider_issue` forcés un à un (vingt motifs distincts), aucun nombre décimal, aucune valeur forcée dans le motif ; l'essai du mode réel exige en plus une sortie sans aucun décimal (`\d[.,]\d`) et des lignes de progrès sans décimal | M74 à M77 (valeur réinjectée dans un motif), M78 (aire imprimée sur la sortie), M79 (aire imprimée dans le progrès), toutes tuées |
| **C-4** garde de l'arbre | **déclaration** : la garde de l'arbre de travail (`exiger_arbre`, `git status --porcelain --untracked-files=all`) ne voit que les fichiers **non suivis et non ignorés** par git ; un fichier ignoré (par exemple sous `donnees/`, ignoré par le `.gitignore` du dépôt : l'essai de bout en bout compte 6 entrées placées sur 10) n'est ni vu ni refusé, et le manifeste ne le consigne pas. `--ignored` n'est pas ajouté (un `.venv/` ignoré ferait refuser). Déclaré aussi : la pièce s'arrête avant le manifeste (code 2) si `diag/<run_7b>/arret.json` **existe** (test d'existence, jamais ouvert), arrêt que T0.8 ne liste pas, dans le sens prudent. Remarque de la contre-lecture non reprise (aucun autre changement de fond) : `M.scellement.verifier(chemin_m)` reste hors du `try` (une panne à cet endroit laisserait un manifeste écrit sous un code 2) ; improbable, à trancher par la mère si elle le veut | — |

## 5. Réserves (une ligne chacune)

- **R-D1** : levée par R-2765 : point (c) lu « coût présent » (section 3) ; plus de nœud.
- **R-D2** : inchangée (base (B) sans centrage ni réduction ; `cout_present` est binaire, comme les mots).
- **R-D3** à **R-D6** : inchangées (fichier des détails de plus ; clés de graines ; « écart type nul » = égalité exacte ;
  taux à 1 %).
- **R-D7** : inchangée, **à reporter dans T0.8** : fils de calcul exigés à 1 par le lanceur et le module en mode réel ; un
  recalcul par T0.8 (contrôle d'identité de M2) doit fixer les mêmes fils ou tolérer un écart d'environ 2·10⁻⁷ sur un
  coefficient de (B).
- **R-D8** : **confirmée par le code gelé** (commit `1609a4bf`, aucune donnée, aucun manifeste réel) : `t06/lanceur_v6.py`
  importe `cles_des_graines` et `jouer_evaluation` de `t06.lanceur` (`a3dde550…`, égal au commit) et appelle
  `creer_manifeste(racine, run_id, config, cles_des_graines(config, taches), …)` ; `cles_des_graines` ajoute
  `f"tache/{t['identifiant']}"` pour chaque tâche d'évaluation (les clés de distillation commencent par
  `distillation/tache/…`, non comptées par la pièce) ; `manifeste.creer_manifeste` (`1a5c7464…`) écrit
  `"graines": graines(taches, entropie)`, dictionnaire indexé par ces chaînes ; `jouer_evaluation` lit
  `g[f"tache/{t['identifiant']}"]` et écrit `"tache": t["identifiant"]` dans chaque ligne des mesures. Les clés
  `tache/<id>` du manifeste de 7b sont donc les identifiants de la colonne `tache`, ce que la pièce compare (64 exigées).
  Les clés de `cles_de_lecture(config)` n'en ajoutent aucune : la fabrique les tire du code gelé sur la configuration
  scellée et l'essai du mode réel en compte exactement 64.
- **R-D9** à **R-D11** : inchangées (entropie fixée dans le code ; neuf modules gelés ; audit (i) non évaluable si (A) est
  non calculable à `S100`).
- **R-D12** : précisée par C-4 (section 4).
- **R-D13** (R4) : première passe du banc v3 **verte** (un seul processus, 14:10:07Z à 14:24:17Z, charge 2,85 sur 4 cœurs au début ; témoin : 64 réussis, 1 sauté — l'essai du commit `1609a4bf`, sauté dans une copie hors dépôt git, comme en v1 — ; 83 tuées sur 83) : aucun rejeu nécessaire ; essais et essai de bout en bout rejoués ensuite au calme, après le banc, verts. La cause du témoin rouge de la v1 reste non établie (réserve gardée pour mémoire, R4).
- **R-D14** : relève de la mère : la suite complète du dépôt n'est pas jouée ici (consigne : les seuls essais de la pièce).
- **R-D15/16** : relèvent de la mère, **à aligner dans T0.8 avant son scellement** : (i) la ligne `CODE-MOTS-ET-COUT-T06`
  cite un fichier JSON (commit, empreintes, contre-lecture), le module vit sous `scripts/` et s'importe par chemin
  (`mots_et_cout_t06_v3`) ; (ii) **neuf en v3** : le contrat de T0.8 (`apprendre_b`, `noter_b`) lit désormais
  `cout_present` au point (c) ; si le brouillon de T0.8 du compte 4 calcule encore une « unité » (lecture v1 ou autre), le
  contrôle d'identité de M2 sur la base (B) divergera. Je n'ai pas lu ce brouillon (hors de ma liste).
- **R-D17 (neuve)** : les essais et l'essai de bout en bout v3 n'ouvrent plus la configuration de T0.7 : les marques
  `["T06", "T08", "P3BIS", "NARC"]` sont recopiées de la contre-lecture v2, § 5 (provenance par transcription) ; l'essai de
  compatibilité avec le lecteur de registre de T0.7 est donc plus faible que celui de la v1 ; la mère ou le contre-lecteur
  peut rétablir la lecture par programme de la seule clé `marques_autres_taches` si elle l'estime permise.
- **R-D18 (neuve, preuve `CODE-T07`)** : le dépôt de travail est un clone **superficiel** ; C7 (`c2fab6cc…`) y est lisible
  mais **non atteignable depuis la tête** (`merge-base --is-ancestor` : non) ; dans le clone épars propre à la tête,
  `code_t07_v1 verifier . registres/scellements-v1.md` **refuse donc pour cette seule raison** (« ni la tête ni un de ses
  ancêtres »), **avec comme sans** les fichiers de la pièce (refus identique) ; avec un commit de fusion synthétique dont
  l'arbre est exactement celui de la tête et qui a C7 pour parent, les cinq fichiers v3 non suivis, la vérification est
  **conforme (26 fichiers)**. Ce que la pièce peut changer (fichiers sous `src/controle_ia/`, écart de contenu) est donc
  prouvé absent ; l'ascendance réelle de C7 depuis `main` n'est pas vérifiable ici : à confirmer par la mère dans un clone
  complet, ou sur l'hôte qui joue l'étape B depuis une arborescence détachée à C7 (rapport v1, § 5).
- **R-D19 (neuve)** : compte descriptif `cout_present_ecarts_a_la_colonne_des_mesures` ajouté au fichier des détails ;
  sur 7b, un compte non nul dirait que le texte conservé diffère de celui qui a été mesuré pour ces actions (la base (B)
  lit le texte, la base (A) la colonne) ; aucune règle ne le lit ; à la mère et au contre-lecteur de dire s'il appelle une
  relecture.
- **R-D20 (neuve)** : la tête de `main` a avancé pendant mon travail (commits de la mère : `1e213ce8…`, `3cb56736…`, puis `157e977d…` à la preuve finale) ;
  aucun fichier de la pièce n'en dépend ; la preuve cite la tête lue.

## 6. Décomptes

- **Essais** (`PYTHONPATH=src python -m pytest -q -p no:cacheprovider tests/test_mots_et_cout_t06_v3.py`) : **65 réussis sur 65**, aucun sauté (110 s, joués après le banc ; une première passe pendant l'écriture : 65 sur 65 aussi) ; 50 fonctions d'essai, 65 cas : les 56 cas de la v1 visant la v3, plus cinq essais neufs et quatre artefacts neufs.
  Essais neufs ou changés : `test_cout_present_et_mots` (seize textes limites, égalité avec `cout_action`),
  `test_cout_present_egal_a_la_colonne_des_mesures`, `test_cout_present_constant_retire_de_l_ajustement`,
  `test_c2_ecrire_et_lire_fichier_code_contre_lecture_obligatoire`, `test_c1_codes_de_sortie_de_main`,
  `test_c3_chaque_refus_de_valider_issue_sans_valeur`, quatre artefacts de plus dans
  `test_garde_registre_et_code_artefacts`, sortie et progrès sans décimal dans `test_mode_reel_de_bout_en_bout_par_le_lanceur`.
- **Banc** (`PYTHONPATH=src python -P -B scripts/banc_mutations_mots_et_cout_t06_v3.py SORTIE.json`, un seul processus) :
  **83 tuées sur 83**, témoin vert, première passe ; M01 à M65 de la v1 visant la v3 (M51 et M63 réécrites pour « coût présent ») ; neuves : C-1 M66 à M68, C-2 M69 à M73 (M69 change trois endroits : la lecture v1 facultative), C-3 M74 à M79, « coût présent » M80 à M83 ; aucune survivante, aucune inapplicable.
- **Essai de bout en bout** (`PYTHONPATH=src python -P -B scripts/essai_bout_en_bout_mots_et_cout_t06_v3.py DOSSIER`) :
  **25 conformes sur 25** (v1 : 19 ; 80 s, joué après le banc) ; six vérifications neuves : refus de `ecrire-fichier-code` sans `--contre-lecture` et contre-lecture citée (dans chacun des deux dépôts jetables), sortie et progrès sans décimal, `cout_present` égal à la colonne des mesures factices.
- **Preuve `CODE-T07`** : (1) dossier partagé : `git diff --quiet c2fab6cc HEAD -- src/controle_ia` vide, cinq fichiers de
  la pièce hors de `src/controle_ia/` ; (2) clone épars propre (`/src/`, `/registres/code-t07/`,
  `/registres/scellements-v1.md`) : 0 entrée sous `src/controle_ia/` ; vérification : R-D18.

## 7. Commandes exactes pour l'hôte (phase B)

Préalables (inchangés depuis la v1, noms v3) : branche créée sur `main` au commit qui porte la pièce v3, son fichier JSON
et la ligne `CODE-MOTS-ET-COUT-T06` ; arbre de travail propre (fichiers non suivis **et non ignorés** : C-4) ;
interpréteur `$PY` avec numpy, scipy et torch ; `$CLONE7B` hors du dépôt avec les cinq fichiers de 7b et leurs
compagnons, rien d'autre ; `$BAC` hors du dépôt ; la contre-lecture citée présente dans l'arbre, commitée, à son
empreinte.

```bash
cd "$DEPOT"
PYTHONPATH=src "$PY" -P -B scripts/mots_et_cout_t06_v3.py verifier-code       # attendu : « CODE-MOTS-ET-COUT-T06 conforme … », code 0
PY="$PY" scripts/lancer_mots_et_cout_t06_v3.sh --mode reel --racine-entrees "$CLONE7B" 20261111-151701-t06-reel \
    > "$BAC/piece-mots-et-cout-v3-sortie-v1.txt" 2> "$BAC/piece-mots-et-cout-v3-progres-v1.txt"; echo "code $?"
```

- **Attendu** : code 0 ; cinq lignes de sortie (en-tête ; `diag/<run-mc>/mots-et-cout-t06-details.json`,
  `base-a-t08.json`, `issue-mots-et-cout-t06.json`, `runs/<run-mc>/manifeste.json`, chacun suivi de son empreinte),
  **aucun nombre décimal** ; progrès : étapes et heures seulement.
- **Code 2** : refus avant le manifeste, rien d'écrit, motif en dernière ligne du progrès. **Code 3** : arrêt après le
  manifeste, `diag/<run-mc>/` ne contient que `arret-mots-et-cout-t06.json` et son compagnon (BA-L0), `runs/<run-mc>/`
  le manifeste ; aucune ligne `ISSUE-MOTS-ET-COUT-T06`.
- **Ensuite** : `git add diag/<run-mc> runs/<run-mc>` (ces deux dossiers seuls), commit, poussée ; aucun fichier ouvert.
- **Lecture de BA-L2 par la mère** : `PYTHONPATH=src python -P -B scripts/mots_et_cout_t06_v3.py etat-ba-l2
  diag/<run-mc>/base-a-t08.json --sha256 <empreinte de la ligne LECTURE-T08-BASE-A>` (imprime seulement « BA-L2 :
  s'applique » ou « BA-L2 : ne s'applique pas »).
- **Marqueurs de la commande (proposés)** : `<<MOTIF_RUN_PIECE>>` = `[0-9]{8}-[0-9]{6}-mots-et-cout-t06` ;
  `<<COMMANDE_PIECE>>` = la ligne du lanceur v3 ci-dessus ; `<<COMMIT_PIECE>>` et `<<LIGNE_CODE_MOTS_ET_COUT>>` : section 8.

## 8. Forme proposée du fichier JSON et de la ligne `CODE-MOTS-ET-COUT-T06` (la mère les écrit, après la contre-lecture)

Après la contre-lecture v3 (rapport scellé, **dans le dépôt, commité**, qui ne change plus ensuite) et le commit
`<<COMMIT_PIECE_V3>>` qui porte les fichiers de la section 1 inchangés :

```bash
PYTHONPATH=src python -P -B scripts/mots_et_cout_t06_v3.py ecrire-fichier-code . <<COMMIT_PIECE_V3>> \
    registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json --contre-lecture <<RAPPORT_CONTRE_LECTURE_V3>>
PYTHONPATH=src python -m controle_ia.scellement sceller registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json
```

Contenu attendu (`ecrire_fichier_code` : clés triées, retrait 1 ; empreintes de la section 1 si le commit les porte
inchangées) :

```json
{
 "commit": "<<COMMIT_PIECE_V3>>",
 "contre_lecture": {
  "chemin": "<<RAPPORT_CONTRE_LECTURE_V3>>",
  "sha256": "<<EMPREINTE_RAPPORT_CONTRE_LECTURE_V3>>"
 },
 "declaration": "Pièce « mots et coût » de T0.6 (base (A) de T0.8, texte scellé à part, et base (B) « mots et coût ») : code écrit le 2026-11-14 (v1, puis v3 : lecture « coût présent » du point (c) de la base (B), R-2765, et couples C-1 à C-3 de la contre-lecture de la v1) par deux développeurs neufs, sous-agents de la session mère, chacun sans aucune vue des données de 7a, de 7b ou de T0.7 (ni mesures-t06.npz, ni textes-actions-t06.jsonl, ni aucun résultat de 7b ; aucun diag/, runs/ ou donnees/ de ces runs), sur données factices seulement ; les réglages ouverts de la base (B) (T0.6, l. 768) sont fixés dans le code avant toute lecture. Le contre-lecteur, dont le rapport est cité sous « contre_lecture », y déclare n'avoir ouvert aucune de ces données.",
 "essais": {
  "scripts/banc_mutations_mots_et_cout_t06_v3.py": "b78f5d046b19811de318d596de1f02e5a6b7c355349fb3299acae8e2a470119c",
  "scripts/essai_bout_en_bout_mots_et_cout_t06_v3.py": "517eedbd216abef174a35984d54d26cc9961ef4f56a6c202c15c0b1533d3d7a0",
  "scripts/fabrique_factice_mots_et_cout_t06_v1.py": "13df39767d3a54f943e7d9047268916f835cbf2fd5251a9cc0842877b213444e",
  "tests/test_mots_et_cout_t06_v3.py": "2e951ed5056024684ea9d3b089129973bfb5bbb3ec8a0b16fdeec343373e0f42"
 },
 "fichiers": {
  "scripts/lancer_mots_et_cout_t06_v3.sh": "e1d2514cd6361f8201a6773a4cf108ac333aa7ca647807698b90c3abeb97a7c5",
  "scripts/mots_et_cout_t06_v3.py": "9dbcc55ca47b21674636f5d6c9126af15244d5ee63a9df8dee274df126c4e674"
 }
}
```

Ligne (registre `registres/scellements-v1.md`, format de `t07/registre_v1`, après commit du fichier et de son compagnon) :
`| CODE-MOTS-ET-COUT-T06 | <<DATE_UTC>> | registres/code-mots-et-cout-t06/CODE-MOTS-ET-COUT-T06-v1.json | <<SHA256_DU_FICHIER_SCELLE>> |`
puis commit, et `verifier-code` (section 7) avant toute exécution. Les lignes `LECTURE-T08-BASE-A` et
`ISSUE-MOTS-ET-COUT-T06` gardent la forme et l'ordre du rapport v1, § 7. Toute correction après la contre-lecture change
les empreintes : le fichier et la ligne se font sur le commit final, jamais sur les empreintes de ce rapport.

## 9. Refus rencontrés et limites

- Un seul geste refusé par l'outil : une attente par `sleep` (refusée par le harnais, remplacée par une veille de fin de
  banc) ; aucun refus de permission ni du classifieur.
- Non vérifiables ici : la forme réelle des fichiers de 7b (par construction) ; le brouillon de T0.8 (R-D15/16) ;
  l'ascendance de C7 depuis `main` (R-D18) ; la suite complète du dépôt (R-D14).

*Déclaration : sans vue des données de 7a, de 7b, de T0.7 ni de P3-bis (code et textes de préenregistrement lus seulement,
données factices seulement).* Ce rapport est scellé (compagnon `.sha256`) ; il n'est jamais réécrit (R12).
