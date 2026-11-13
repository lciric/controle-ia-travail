# Consigne — vérification courte du brouillon 4 « validité de l'adaptateur » — v1

Écrite le 2026-11-13T21:24:57Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, Claude Opus 5.5, **auteur du brouillon 4**). Lot : plan multi-comptes (`3b1bda25…`), lot « compte 4 », tâche 1. Aucune dépense, aucune publication, aucun changement de revendication.

## 0. Interdits permanents (recopiés du brief du compte 4, section 6, sans changement)

- Aucune dépense ni machine louée sans ligne de GO inscrite **et** mot de Lazar.
- Aucune valeur de clé : jamais `env`, `printenv`, `set` sans argument, `export -p`, `/proc/*/environ`.
- Jamais `diag/*/lecture-sondes-t06.json`, la lecture B de 7a, `donnees/lecture-b-7a-quarantaine-v1`, `donnees/mesure-unanime-v15-sortie-v1`, `essai/t06-explo-v3`, aucun `diag/` ni `runs/` de 7a ou 7b, l'étiqueteur, `scripts/extraire_mesures_epreuve_t06_v1.py`, la branche `calcul/p3bis-reel-v2`.
- Jamais `donnees/bras-attaque*`, `donnees/mode-tenu-a-l-ecart*`, `docs/notes/bras-attaque/`, `registres/index-bras-attaque*`, `anteriorite-bras-informe*`, ni la branche `claude/compassionate-meitner-d4ryyk`.
- Aucune recherche récursive qui traverse ces chemins : pas de `ls registres`, pas de `find` ni de `grep -r` larges ; fichiers nommés seulement.
- Jamais d'heure écrite à la main (`date -u` dans la même commande). Jamais de `git fetch` sans refspec.
- Garde des secrets à 0 avant chaque commit (sans objet ici : tu ne commites rien).
- Jamais toucher les instances Vast 58936096, 58936099, 58936100, 60480302, 60541314 ni les serveurs Hetzner `poste-temoin-bailey-*` ; aucun appel au loueur.
- Ne jamais contourner, reformuler ni confier à une autre session un refus de permission, du crochet ou d'un classifieur : arrêt, rapport à la mère.
- Rien de publié, aucun contact extérieur (tu rédiges, Lazar envoie).

**Ajoutés pour cette contre-lecture.**
- Lecture seule, sauf les deux fichiers du § 5. Aucune écriture git (ni `add`, ni `commit`, ni `push`, ni `checkout`, ni `fetch`), aucun appel réseau, aucune recherche sur la toile, aucun sous-agent.
- **Aucun fichier de `registres/`** (la mère n'en a nommé aucun pour ce lot) ; **aucun fichier de P3-bis** (procédure du rendez-vous, consigne du lecteur, verdict, tout `docs/verdicts/verdict-P3-bis*`) ; **rien de `donnees/`, `diag/`, `runs/`**.
- Pas de `verifier-arbre` ; `PYTHONPATH=src python3 -m controle_ia.scellement verifier <fichier>` sur fichiers nommés seulement.
- Dans un fichier nommé, `grep -n`, `sed -n` ou l'outil de lecture sur ce seul fichier ; jamais `grep -r`, `find`, `ls -R`, `git grep`.
- Aucune lecture de sonde, de score ni de résultat d'aucune course (tu lis des textes et du code, rien d'autre).

- **Exception d'écriture** : pour le point 1, tu peux écrire dans le seul dossier `/tmp/claude-0/-home-user-controle-ia-travail/0bb788a7-74e8-52db-b35a-9747a8f95b86/scratchpad/verification-b4/` (brouillon rejoué) ; nulle part ailleurs hors des fichiers du § 4.

## 1. Qui tu es

Vérificateur **neuf**, sous-agent de la session du compte 4. Tu n'as écrit ni ce texte, ni ses brouillons, ni ses couples, ni T0.7, ni son module. Ton modèle doit être différent de celui de l'auteur du brouillon 4 (Claude Opus 5.5, `claude-opus-5-5`) : écris ton identifiant de modèle en tête. Si tu lis T0.7 scellé, tu en deviens lecteur et tu es exclu ensuite de tout rôle de lecteur ou d'hôte du verdict de P3-bis et des verdicts de l'étape B de T0.7, de T0.8, du contrôle de l'adaptateur et du barreau 6. Français ; aucun sigle non développé.

## 2. Objet

Le brouillon 4 est écrit **par couples** « ancien » → « nouveau » appliqués au brouillon 3 : les 21 couples mécaniques de la contre-lecture 2, tels qu'écrits, puis 63 couples de l'auteur (`A4-01` à `A4-42`, `A4-M01` à `A4-M21`). Deux traitements y sont appliqués **à titre provisoire**, en attente d'une réponse : CLVA2-01 et CLVA2-10 (règle (a) de T0.7, décision de la mère) et CLVA2-11 (pièce HD après le verdict de P3-bis, créée si et seulement si l'issue est « vu », mot de Lazar). Un marqueur `<<COMMIT_C7_T07>>` est laissé exprès (mot de la mère : le commit C7 va changer, R-2593). Tu vérifies que le brouillon 4 fait ce que disent la contre-lecture 2 et ses couples, sans défaut neuf. Tu ne tranches pas les deux traitements provisoires ; tu dis s'ils sont écrits de façon cohérente avec le reste du texte.

## 3. Fichiers (vérifie chaque empreinte avant lecture)

| rôle | chemin | sha256 |
|---|---|---|
| brouillon 3 (base) | `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon3.md` | `defd8ef05038e703c24733f6a5f88a1153daf5f44d2b8cae14950a5643e875fd` |
| **brouillon 4** | `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon4.md` | `417d6aee9a86d56f3478b57da30cb8d1af47493ff79ba69858f2167b8ad15f42` |
| couples appliqués | `brouillons/validite-adaptateur-v1/candidat1-pieces/couples-brouillon4-v2.json` | `ce1a747aff59abbc58052f1531a3a1f7f0c881571472bc560262aa38ba498070` |
| générateur des couples | `brouillons/validite-adaptateur-v1/candidat1-pieces/faire-couples-brouillon4-v2.py` | `57402cc05000575aa1c7fa3753311caa4510b05e8ced6774fd51f376d4a7a37a` |
| script d'application | `brouillons/validite-adaptateur-v1/candidat1-pieces/appliquer-couples-vadapt-v2.py` | `933f0ebe4b97aa9aa5987a30e3f1898487c9dd6a241db71b2df2c2b67c978b71` |
| sortie de l'application | `brouillons/validite-adaptateur-v1/candidat1-pieces/sortie-application-couples-brouillon4-v2.json` | `67942f7cd5543cf65ec134581fc58fa64dc91647e1ce62afd196c1c31d3a9f3e` |
| puissance et devis de l'auteur | `brouillons/validite-adaptateur-v1/candidat1-pieces/puissance-devis-brouillon4-v1.py` et `sortie-puissance-devis-brouillon4-v1.txt` | `8eab925bec756e7d0c48dcf79bf494adfe7451d62d79dd20fba8e6cb9177a0ee`, `4c528a3f6c16094787047a4f915d5c5e909c1abbc64af2fcdd03327e930465aa` |
| confirmation des champs au commit C7 | `brouillons/validite-adaptateur-v1/candidat1-pieces/confirmation-champs-t07-c7-v1.md` | `f91452ed3e34a83b7c1c33c0cd74219b9340a2bcfb9beea805e4509910b9f2e7` |
| contre-lecture 2 (rapport et script) | `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon3-cl2.md`, `…-cl2-calcul.py` | `11f7242b9dbada3fdc9f6e2c0a707eef3f0d2b51783e425545d78ec43d2bccee`, `26437692aacc32fb1522025e37cf0dd6b14059415167491d0de9bedbd057d945` |
| erratum de T0.7 | `docs/notes/g0-deux-semaines-v1/t07-module-v2/erratum-concordance-adaptateur-t07-scelle-v1.md` | `f593676248698b985f842f30f403e0036b1faa556335d1b1bcb7ed7a08080aea` |
| T0.7 scellé (par lignes citées et `grep -n` dans ce seul fichier) | `prereg/T0.7-sondes-v0-v1.md` | `d7d180eccbbce8ff2e370f82957543c28f1e564c872f981c7ada403949baade5` |
| module de T0.7 (fichiers nommés) | `src/controle_ia/t07/<nom>.py` sur l'arbre ; égal au commit C7 `b4cd9953` (pièce de confirmation) | — |
| validateur | `src/controle_ia/prereg.py` | `3b2e3ee56463f30ffd3c549e7fe480fea574c707581bcf30098bf38f4980c306` |

## 4. Ce que tu vérifies

1. **Rejeu mécanique** : `python3 -I brouillons/validite-adaptateur-v1/candidat1-pieces/appliquer-couples-vadapt-v2.py <brouillon 3> defd8ef0…(entier) <couples v2> ce1a747a…(entier) /tmp/claude-0/-home-user-controle-ia-travail/0bb788a7-74e8-52db-b35a-9747a8f95b86/scratchpad/verification-b4/brouillon4-rejoue.md COMMIT_C7_T07` : l'empreinte de la sortie est-elle `417d6aee…` ? Les 21 premiers couples sont-ils, à l'octet, ceux du bloc JSON de la section 3 du rapport de la contre-lecture 2 ?
2. **Couples de l'auteur**, un par un (`A4-*`) : chacun traite-t-il bien le constat qu'il dit traiter (table de la section « Contre-lecture » du brouillon 4) ? Les 21 marques `A4-M*` suivent-elles la table de correspondance du rapport de la contre-lecture 2 (CLVA2-09) ? Les chiffres (puissance, devis) sont-ils ceux de la sortie du script de l'auteur ? Un couple introduit-il une erreur, une contradiction avec une autre section, un renvoi faux à T0.7 scellé (ligne citée qui ne dit pas ce qu'on lui fait dire) ?
3. **Règle (a)** : la formulation des sections « Métrique » et « Seuil » est-elle fidèle à T0.7 scellé (l. 1258) et à `plancher_v2.comparer_difference_au_plancher` ? L'analogue `Dτ` de VA-2 est-il écrit sans ambiguïté et déclaré non simulé ?
4. **Pièce HD** (plan, points 2 et 3 ; « Calcul et dépense » ; « Liste d'arrêt » ; annexe A ; en-tête) : la règle de lancement « si et seulement si `issue` vaut « vu » » est-elle cohérente avec G-1, avec l'engagement de la pièce R, avec la liste d'arrêt et avec l'annexe A ? Une phrase du texte suppose-t-elle encore HD jouée pendant 7b ?
5. **Résidus** : un passage du brouillon 4 contredit-il encore T0.7 scellé, l'erratum ou le module (200 directions, plancher de P3, `lecture_v2` au lieu de `lecture_v4`, commit `8ae9fc44` hors des passages historiques) ?
6. **Forme** : `PYTHONPATH=src python3 -c "from controle_ia.prereg import problemes; print(problemes('brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon4.md'))"` doit rendre le seul marqueur `<<COMMIT_C7_T07>>`.

**Gravité** : bloquant (empêche le scellement une fois les deux réponses données et le marqueur rempli), majeur (à corriger avant), mineur.

## 5. Ce que tu rends

Un rapport, `prereg/contre-lectures/validite-adaptateur-preenregistrement-v1-brouillon4-verification-courte-v1.md`, scellé par `PYTHONPATH=src python3 -m controle_ia.scellement sceller <fichier>`, puis vérifié. Sections : **0. Identité** (modèle, heures `date -u`, fichiers lus et empreintes) ; **1. Verdict** (trois lignes au plus : « conforme », « conforme après les corrections listées » ou « non conforme » ; nombres par gravité) ; **2. Constats** (`VB4-01`… ; gravité ; endroit ; preuve ; correction, en couple exact « ancien » → « nouveau » sur le brouillon 4 quand elle est mécanique, « ancien » présent une seule fois) ; **3. Couples** (bloc JSON des seules corrections mécaniques) ; **4. Limites**. Rien d'autre n'est écrit.

Ton dernier message : verdict en trois lignes, nombres de constats, chemin et empreinte du rapport, ton identifiant de modèle.
