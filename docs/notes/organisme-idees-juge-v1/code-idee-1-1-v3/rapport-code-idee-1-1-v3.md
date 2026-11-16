# Rapport du développeur — code de l'idée 1.1, version 3 (corrections de la vérification du différentiel v1 → v2, `verification-differentiel-code-idee-1-1-v2.md`, `549e459743cba457bc140f0b4c48c21c386fd7a2a3576a81a315d0ea6038ad91`)

- Auteur : le développeur des versions 1 et 2 ; je n'ai écrit ni le texte ni les contre-lectures.
- Date (UTC) : 2026-11-15, de 23:35 à 23:50, tête `c817619c`.
- Ce que je n'ai pas fait :
  - aucun fichier v1 ou v2 modifié (R12) ;
  - aucun commit, aucun appel réseau, aucun appel payant ;
  - ni jeu, ni étape 0, ni lecture d'une sortie de jeu ;
  - rien sous `diag/`, `runs/` ni `donnees/`.
- L'essai de bout en bout joue une répétition de chacune des 30 lignes sous une **racine d'essai**, distincte de l'empreinte du texte. Il écrit seulement dans un dossier temporaire d'essai.

## 1. Méthode et fichiers neufs (scellés)

- Chaque v3 est son v2, plus les couples « ancien → nouveau » et l'ajout de fin déclarés dans `code-idee-1-1-v3/couples-v2-vers-v3.json`.
- `tests/test_organisme_idees_juge_idee_1_1_differentiel_v3.py` éprouve les 12 fichiers : v2 intact, chaque ancien présent une seule fois, v3 égal octet pour octet.
- Fichiers touchés : la lecture (N1, format, n2 à n5), les mutations, l'étape 0, l'exécution (imports et fichiers gelés), les trois scripts (n1 dans le lanceur), et les cinq fichiers d'essais.
- `test_…projection_v3.py` est une copie sans couple de la v2 : même empreinte.
- **Le banc reste `banc_idee_1_1_v2.py`, inchangé.**
- Fermeture des imports des scripts v3, vérifiée : aucun fichier importé hors de `FICHIERS_GELES` ; aucun module v1 ou v2 touché n'est importé. La liste gèle aussi les sources v2 de l'essai d'égalité, le JSON des couples et les sept essais v3. Le lanceur ne rejoue que ces sept essais.
- Nom du run v3 : `idee-1-1-poids-du-nul-v3`. Le lanceur refuse un run antérieur de l'une des trois versions.

| fichier | sha256 |
|---|---|
| `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v3/couples-v2-vers-v3.json` | `d4ec2946f9f8c96973a9d200763436ba7f751384093c381513a60b8762f79f60` |
| `scripts/etape0_idee_1_1_v3.py` | `7eedd01a40805e677f7174cc6d966d33400d2d9b2d3a482c8ed158245398513d` |
| `scripts/jouer_idee_1_1_v3.py` | `ea89c708e653e1c4ff7b878b306080cd1b7b78a8e5669d8db0bbc55a2db5c834` |
| `scripts/lire_idee_1_1_v3.py` | `533e8c729eda1444432202f68147d42f2b2f4c8d8697c683f985e53ce35d23e0` |
| `src/controle_ia/organisme_idees_juge/etape0_idee_1_1_v3.py` | `a28611d2d708d40ce847691f8a53763885779819b4d8c6028e267346eaa562e1` |
| `src/controle_ia/organisme_idees_juge/execution_idee_1_1_v3.py` | `047113faf307ffd5cb318a95770cc5ae83c2e3c12b489d1f3ab61cd0cf65b2e2` |
| `src/controle_ia/organisme_idees_juge/lecture_idee_1_1_v3.py` | `fa8b27beb87e70db21bd779e632ac93dd82015847f1e494d5a353e4190fb3103` |
| `src/controle_ia/organisme_idees_juge/mutations_idee_1_1_v3.py` | `6288c54d473658d5bb2b81bfb7a47675c5e1fcc5026ca0881ee2fcbee671accd` |
| `tests/test_organisme_idees_juge_idee_1_1_banc_v3.py` | `7e269b3b9e845a2ee362966ca096c991b1c3e8b36b7c12d422b527f84eae580c` |
| `tests/test_organisme_idees_juge_idee_1_1_bout_en_bout_v3.py` | `436e3a874418a8c76653de6419d3cf7d737f1872c01e10210f28d1fb509ae673` |
| `tests/test_organisme_idees_juge_idee_1_1_differentiel_v3.py` | `c0a1cd5706867d81507947322d4d5d0f55e74a25c700965e4ff2794ab0cc2b32` |
| `tests/test_organisme_idees_juge_idee_1_1_execution_v3.py` | `d424a19b900f796d431b261e303a1f67eec8d20c426cceb4957b1cf6b9f7fc88` |
| `tests/test_organisme_idees_juge_idee_1_1_gardes_v3.py` | `27d17ecd6670175b27aae3bd2a2dc447d3c9aa192523423183e472499fdce062` |
| `tests/test_organisme_idees_juge_idee_1_1_lecture_v3.py` | `5b6b0680bcdb768acdce0c39eab75a9ad4ae8a5b0598dae103575bebf07850c8` |
| `tests/test_organisme_idees_juge_idee_1_1_projection_v3.py` | `6e53851ec4794d00f30d275a6a04f10aef72489c65cd6bce40085879b597631a` |

## 2. Essais

**408 passés, 0 échec** : 117 v1, 142 v2 et 149 v3, tous inchangés depuis leur rendu. Un processus, `nice -n 10`, sans variable `GIT_*`, 8 min 10.

Un seul échec au premier passage : l'essai v2 recopié attendait la décomposition sans les champs `ecartes` et `niveau` ajoutés par n4. Je l'ai corrigé par un couple déclaré, puis rejoué.

Sur les 149 essais v3 :
- 12 sont l'essai d'égalité ;
- 2 sont l'essai de bout en bout ;
- 6 sont neufs dans le fichier de lecture ;
- le reste reprend les essais v2.

Le banc de mutations v3 compte 17 mutations, toutes tuées, et 17 cas sains passés.

## 3. Corrections

| point | code v3 | essai |
|---|---|---|
| **N1** | `_lw_rep` lit `A2.log_w_200`, la seule lecture d'A2 (« lu à 200 »). L'enregistrement synthétique des essais suit maintenant le banc : A2 sans `max` ; La et Ld avec leurs écarts résiduels | `test_n1_a2_lu_a_200_dans_les_rapportes` ; **bout en bout** (ci-dessous) |
| **Bout en bout** | une répétition **produite par `jouer_repetition`** pour chacune des 30 lignes, tous les bras, racine d'essai. Les enregistrements sont recopiés à 100 répétitions par ligne. Seules les valeurs `promue` sont réglées par un motif synthétique, pour franchir chaque étage ; tout autre champ est celui du banc. La chaîne : tranches scellées ; `charger_sortie` ; `verifier_format` ; `lire_v3`, avec les étages 1 à 3 franchis et les 18 rubriques présentes, dont tous les rapportés ; écriture scellée de `lecture.json` ; relecture | `test_lecture_de_bout_en_bout_sur_enregistrements_du_banc`, `test_format_reel_de_chaque_ligne_accepte` |
| **Format en `GardeArret`** | `verifier_format` contrôle, par sorte de ligne, chaque champ et sous-champ lu. Les groupes réductibles doivent former un préfixe. Les répétitions doivent être dans l'ordre. `lire_v3` vérifie le format d'abord, puis rend toute `KeyError`, `TypeError`, `IndexError`, `ValueError` ou `AttributeError` résiduelle en `GardeArret`, avec son message | `test_format_inattendu_rend_une_garde_avec_message` (champ, sous-champ, ordre, ligne absente), `test_erreur_imprevue_rendue_en_garde` |
| n1 | `"version_lanceur": 3` dans le lanceur v3 | relu |
| n2 | règle « au moins une ligne informative par strate » déclarée ; arrêt avec message si tous les rééchantillons sont écartés | `test_n2_n4_reechantillons_tous_ecartes_arretent` |
| n3 | J9-D et J9-D40 contre J9⁺ ajoutés aux paires de McNemar, soit 13 paires | essai de lecture (compte des paires) |
| n4 | décomposition : rééchantillons écartés comptés, niveau de 95 % déclaré dans la sortie, arrêt avec message si tout est écarté | idem n2 |
| n5 | `rho_plus_primaires` : ρ⁺ de J9-P, La et Ld, rapporté par un appel à part. Le verdict principal reste lu sur `rho_plus`, inchangé | bout en bout (rubrique présente) |
| m4, artefact | trou atteint et dent de H7 manquée ensemble : les trois lectures sont rendues séparément | `test_m4_artefact_dent_manquee_et_trou_ensemble` |
| m7, artefact | P5 « partielle » avec 2 lignes informatives ; une partie de P12 réfutée, d'où « toutes vraies » faux | `test_m7_artefacts_p5_partielle_et_p12_refutee` |
| Lectures à déclarer | `LECTURES_DECLAREES` de la lecture v3 : tableau des strates, règle des strates (n2), niveau de la décomposition (n4), paires de McNemar (n3), ρ⁺ des primaires (n5), m6. Elles sont jointes à `lecture.json`. `etape0.declarations_v3()` les ajoute aux déclarations v2 (m9 à m11, comptes non écrits) dans le fichier d'étape 0 et dans le **bloc d'addendum** imprimé | `test_declarations_m9_m10` (v3) |

Ce que l'essai de bout en bout montre, et ce qu'il ne montre pas :
- Il établit qu'aucun autre désaccord de format entre banc et lecture ne reste, pour des enregistrements **sans réduction**.
- Les formats réduits ne sont éprouvés que par `verifier_format` : groupes absents en suffixe, sur des données synthétiques.
- Aucun chiffre de l'essai n'est lu.

## 4. E2 et E3 (pour le directeur ; rien n'est changé)

Le texte et le comportement du code sont ceux du rapport v2, § 4.

- **E2** — phrase du texte : « J8 est calculé par le code du juge de la copie `94bfd92` (`nul_filles_v2.evaluer_v2`, `nul_v8.membres_archive_v8`). J9 par le **code original** [V9] : […] évaluation par `nul_v9.evaluer_v9` ». Le code rejoue les gardes de ces fonctions, puis appelle leurs fonctions internes dans leur ordre, sans arrondi.
- **E3** — phrase du texte : « Sans coût de plus : les bornes par coupe sont déjà calculées ». Le code fait un second appel au solveur pour J9-Dc.

## 5. Étape 0, version 3 (à lancer par la mère, après le commit des v3)

```
cd /home/user/controle-ia-travail && .venv/bin/python -I -B scripts/etape0_idee_1_1_v3.py --travail /tmp/claude-0/-home-user-controle-ia-travail/78897fa0-2926-5bf2-a108-3e893bc2db62/scratchpad/etape0-travail-v3 --processus 3
```

- Sortie scellée : `docs/notes/organisme-idees-juge-v1/code-idee-1-1-v3/etape0-v1/etape0-idee-1-1-v3.json`. La commande imprime aussi le bloc programme et toutes les déclarations ; les lignes d'empreintes s'obtiennent par `--lister-empreintes`.
- Durée estimée : environ 1 h, de 1 h à 1 h 30 sous charge.
- Jeu ensuite : `python -I -B scripts/jouer_idee_1_1_v3.py --addendum CHEMIN`.
- Lecture ensuite : `python -I -B scripts/lire_idee_1_1_v3.py diag/organisme-idees-juge-v1/<RUN_ID>`.

## 6. Non éprouvé

- L'étape 0 entière.
- Le jeu.
- La lecture d'une vraie sortie de jeu, et des enregistrements réels sous réduction.
- La reprise après un vrai arrêt de machine.
- La relecture du différentiel v2 → v3 par un sous-agent neuf.
