# Écarts entre les entrées attendues par le code de lecture de la première course et les fichiers de la course v5 — v1

> EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce de travail (classe C), côté exposé, pour préparer un portage mécanique (demande de la mère, 2026-11-24 vers 16:09Z). Aucun code de portage écrit. Relevé fait sur les noms de fichiers, la structure des clés et les seules valeurs d'étiquette (noms de phase, d'oracle, de schéma, comptes de lignes) ; aucune valeur mesurée lue, aucune consigne privée ouverte.

- Code lu : `src/controle_ia/iib/lecture_v1.py` (`b8e904c0…`), scripts `scripts/lecture_iib_{1,2}_*_v1.py`, au commit de lancement `192a429e`. Course : `20261123-043944-iib-course-reel`, branche `essai/iib-explo-v8` (`3326499e`). Sorties d'évaluation sous `diag/20261122-202132-iib-reel/` (dossier de l'étalonnage, engagé par la course).
- Légende de la dernière colonne : **M** = correspondance mécanique (nom ou chemin seulement) ; **C** = choix à trancher (conception : Fable, ou mot de la mère/Lazar) ; **A** = entrée absente de la course, à produire ou à fixer.

## 1. Fichiers

| attendu par `lecture_v1` | dans la course v5 | nature |
|---|---|---|
| `diag/RUN/resume.json`, vérifié par `manifeste.verifier_resultat`, qui porte `resultat.empreintes` des fichiers lus (clés = chemins relatifs à la racine) | `diag/20261123-043944-iib-course-reel/resume.json` ; ses `resultat.empreintes` ont pour clés des chemins **relatifs au dossier de l'étalonnage** (`evaluation/oracles-evaluation-B100.json`, …), non à la racine | M (résolution des chemins à fixer) |
| `runs/RUN/manifeste.json` (config, graines) | `runs/20261123-043944-iib-course-reel/manifeste.json` | M |
| `donnees/RUN/oracle-iib.json`, clé `actions` (toutes phases, un oracle) | quatre fichiers `diag/20261122-202132-iib-reel/evaluation/oracles-evaluation-{H,B50,B100,TJ100}.json`, clé `lignes` (1 280 lignes par condition : 64 tâches × 10 pas × **deux oracles**, `oracle` ∈ {`N`, `P`}), schéma `oracle-iib-v5`, plus `oracle_de_la_regle` | M (concaténation) + C (filtre d'oracle, § 2) |
| `diag/RUN/episodes-iib.json`, `fiches[*]` (`uid`, `phase`, `actions`, `jetons` : nombre de jetons générés par action) | absent. Le plus proche : `diag/20261122-202132-iib-reel/evaluation/ids-evaluation-{c}.json` (clé `ids`, `evaluation-<c>/<tâche>` → 10 listes d'identifiants) et `ids-actions-evaluation-iib-v5.json` (les quatre conditions) | A + C (règle de compte des jetons : jusqu'au premier jeton de fin compris ou non, plafond de 400 ; la note v7, question 3, en donne une pour la passe) |
| `diag/RUN/acceptation-iib.json`, `exces_moyen_par_action_des_acceptes` (déclencheur (a) de l'audit R4 de la lecture (1)) | aucun fichier ni clé de ce nom ; les épisodes du maître et leurs sorties d'oracle sont dans `course-maitre-iib-v5.json`, `oracle-course-iib-v5.json`, `tours/` | A + C (grandeur à recalculer : sur quel oracle, quels épisodes acceptés) |
| `donnees/RUN/textes-actions-iib.jsonl` (`phase`, `episode`, `pas`, `texte`), lecture (2) seule | **absent de la course et de toute branche relevée** : la course ne verse que les identifiants de jetons. Les textes sont à rebâtir par décodage des identifiants avec le jetoniseur de la révision figée (note v7, questions 2 et 4 : décodage sans les jetons spéciaux) | A (jetoniseur à charger ; règle de décodage à fixer) |

## 2. Champs d'une action

| `lecture_v1` | v5 (`oracles-evaluation-*.json`, `lignes[*]`) | nature |
|---|---|---|
| filtre `phase.startswith("evaluation-")` | `phase` = `evaluation-<c>` | M |
| filtre `contexte == "reecrit"` (un seul oracle, à contexte réécrit) | pas de `contexte` ; `oracle` ∈ {`N` (contexte réécrit), `P` (contexte de l'agent)} ; l'additif 1 du texte des sondes veut les lectures « sous l'oracle que désigne la règle scellée » : filtre `oracle == oracle_de_la_regle` | C (lecture par l'oracle désigné : à écrire ; rapport de l'autre oracle à côté ou non) |
| `e` (eₜ, excès de l'action) | `exces` (flottant, ou `null` si non bornable) | C (nom seulement si `exces` de v5 est la même grandeur que eₜ de v1 ; sous [P], la conception v5, 10.6, dit que ce n'est pas une mesure de niveau) |
| `bornable` | `bornable` | M |
| `episode` (tâche), `pas` | `episode`, `pas` (0 à 9) | M |
| `cout_declare`, `cout_lisible` | `cout_declare`, `cout_lisible` (lecteur de la fenêtre commune, `lecture_cout_v5`) ; aussi `ancien_lecteur` (lecteur du champ entier de v1) | C (quel lecteur du coût tient lieu de celui de v1) |
| `formes` (dict) | `fenetre.formes` (sept clés) | M |

## 3. Configuration et graines

| `lecture_v1` | v5 | nature |
|---|---|---|
| `config.lecture_1` : `tirages`, `niveau`, `taches_min`, `audit_largeur_min`, `audit_effet_min`, `audit_echantillon` | **absent** de la configuration de la course v5 (aucune clé de lecture) | A + C (reprendre les valeurs de la configuration de la première course, à la lettre ? source à citer) |
| `config.lecture_2` : `tirages_aire`, `permutations`, `quantile_plancher`, `aire_min`, `quantile_honnete_exces`, `fausses_alarmes`, `tirages_taux`, `vocabulaire_max`, `seuil_sous`, `seuil_flagrant` ; `config.lecture_2_code.piece` (chemin et empreinte de `scripts/mots_et_cout_t06_v3.py`) ; `config.mode` | absents, sauf `mode` ; `config.pieces` ne cite pas la pièce « mots et coût » | A + C |
| `cf.TEXTE["regle"]["b"]` (borne de la règle v1, descriptifs de la lecture (1)) | règle v5 en deux jeux (conception v5, section 7) | C (descriptif seulement) |
| graines `iib/lecture-1/tirages`, `iib/lecture-1/audit`, `iib/lecture-2/plis`, `iib/lecture-2/tirages_aire`, `iib/lecture-2/permutations`, `iib/lecture-2/tirages_taux`, lues dans `manifeste.graines` | `manifeste.graines` ne porte qu'une clé (`course/iib/v5/manifeste`) ; l'entropie est dans `config.entropie` | A + C (dériver ces clés par `SeedSequence` de l'entropie de la course, R9 : règle de dérivation à écrire et consigner) |

## 4. Sorties et gardes en aval

- **Nom et dossier des sorties** : `ecrire` écrit sous `diag/RUN/` ; `RUN` = nom de la course (`20261123-043944-iib-course-reel`), dossier qui ne porte que `resume.json` : M (à confirmer).
- **Garde de la lecture (2)** : ligne du registre des décisions citant l'empreinte de la sortie (1) : inchangée ; la ligne est inscrite par la mère sur `main` (la session côté exposé ne pousse pas dans `registres/`).
- **Programme de l'extrait des états** : v3 lit `jeux` (dix clés), `etat_par_unite.unites` (trois), `phrase`, `lecture_1.{sha256, phrase}` ; un portage qui garde ces clés le laisse mécanique ; il reste à passer en v4 pour les trois lignes de scellement (additif 2, D-17).

## 5. Ce qui n'est pas mécanique, en une liste

1. Oracle lu : celui de `oracle_de_la_regle` seul, et ce qu'on fait de l'autre (rapporté ou non).
2. Équivalence `exces` (v5) ↔ `e` (v1), et lecteur du coût (fenêtre commune ou ancien lecteur).
3. Textes des actions : décodage des identifiants par le jetoniseur (règle, jetons spéciaux, coupe à la fin d'action).
4. Nombre de jetons par action.
5. Excès moyen par action des acceptés du maître (déclencheur (a) de l'audit).
6. Valeurs de configuration des lectures (1) et (2) et citation de la pièce « mots et coût » : reprises de la première course ou fixées à neuf.
7. Graines des lectures : dérivation depuis l'entropie de la course.
