# Rapport du développeur : code des lectures du dommage et de la diffusion sur la course v5, version 1

> EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce du côté exposé : jamais transmise au côté des moniteurs ni à un concepteur de moniteur. Pièce de classe B (instrument) : à contre-lire par un autre modèle avant tout jeu sur la course réelle.

- **Développeur** : Claude Opus 5.5, sous-agent du côté exposé du barreau 8 (session `session_01Qi7Gr3KR5S1fcJtia9KMrT`).
- **Accord** : `GO-2026-11-24-37`. Aucune dépense, aucune machine, aucun appel de modèle.
- **Spécification suivie** : `docs/notes/barreau8-cote-expose-pieces-lecture-v1/specification-lectures-dommage-diffusion-course-v5-v1-brouillon3.md`, sha256 `acce24e76e17bffb2938616f2204d068a1f61d5e71938ce8a33e1e6a83a7407e` (constante `SPECIFICATION`, vérifiée à chaque lancement).
- **Arbre** : branche `barreau8/code-lectures-v5-cote-expose-v1`, tirée de `3326499e` ; spécification copiée au commit `03c2d9549`. Commits locaux seulement, rien de poussé.
- **Date** : 2026-11-24T18:02Z.

## 1. Fichiers neufs et empreintes

Aucun module antérieur n'est modifié (`git status` : sept fichiers neufs, plus leurs compagnons `.sha256` et ce rapport).

| fichier | rôle | sha256 |
|---|---|---|
| `src/controle_ia/iib/configuration_lectures_v5.py` | constantes (sections 5.1, 7.1, 8, 9, 12), `pour`, `exiger_specification`, `exiger_modules_d_origine` | `3c8232036bb84938ae3086e8ae9e8d565a68a2248e0d9ad64a2b5d34d9821c4f` |
| `src/controle_ia/iib/entrees_lectures_v5.py` | `ouvrir` (liste fermée), contrôles T0 et E0 à E10, jetoniseur, décodage, fidélité, présentation, graines | `8e1846c3e76fe7e3eb7ad355c2eb05808f7605f2bf42dcc5e42aa99d603d4adf` |
| `src/controle_ia/iib/lectures_v5.py` | appel du module d'origine, blocs rapportés, garde de l'audit, base « premier coût contre les suivants », citations | `0f48f8ec5dbf5afd76d85b950eb6c7b10077544c688a3d8f77a98b5ce82659ca` |
| `scripts/lecture_iib_1_dommage_v5.py` | lecture (1) | `11b41164372bde2f5cac573dba22325c75cc3352cd85cead4315832c9fd28367` |
| `scripts/lecture_iib_2_diffusion_v5.py` | lecture (2) | `15ffa52fe475c8619c9c4a3439c2fbb7aed83f75e6fb546f68d9882acd324e1e` |
| `scripts/lecture_iib_audit_r4_v5.py` | affichage de l'audit de symétrie, n'écrit rien | `92c5e0770e888245d6f76d542556d7adadb2329ff047dc10ce71fb147527a0f4` |
| `tests/test_lectures_iib_v5_v1.py` | essais de la section 14 (nom changé : écart 14) | `47c04f22516e7ae8a964a9b58641c154fbd4eb7a9f7ee660a0459eea643400bb` |

Bibliothèques : rien n'a été installé ; le `.venv` porte déjà numpy 2.4.6, scipy 1.17.1, torch 2.14.1, transformers 5.18.0, tokenizers 0.23.2 (celles de `requirements-cpu.txt`).

## 2. Commandes exactes de jeu (course réelle) — non jouées ici

Toutes depuis la racine de l'arbre de lecture (celle du code qui tourne, exigée en mode réel), arbre propre, avec le `.venv` du dépôt. `MAIN` : un arbre de `main` qui porte `registres/`. `JET` : un dossier qui ne contient que les quatre fichiers de `jetoniseur/` du commit `e5677bbf2696e9364da7f4bf191abcc5de16eabc` (par exemple `/tmp/claude-0/-home-user-controle-ia-travail/009b3d3c-f1bd-510b-b07f-b1a242cff477/scratchpad/jetoniseur-v1/jetoniseur`, extrait et vérifié : quatre empreintes égales aux références).

1. Lecture (1) :
   ```
   PYTHONPATH=src python scripts/lecture_iib_1_dommage_v5.py --racine . --run-id 20261123-043944-iib-course-reel \
       --etalonnage 20261122-202132-iib-reel --registre-sondes MAIN/registres/sondes-iib-v1.md
   ```
   Imprime chemins, empreintes et « audit R4 déclenché : oui/non ». Puis committer `diag/20261123-043944-iib-course-reel/lecture-iib-1-…-v1.json`, son compagnon et `runs/<AAAAMMJJ-HHMMSS>-iib-lecture-1-dommage-v5/` ; la session mère inscrit l'empreinte complète au registre des décisions.
2. Si l'audit s'est déclenché, affichage pour la relecture (rien d'écrit) :
   ```
   PYTHONPATH=src python scripts/lecture_iib_audit_r4_v5.py --racine . --run-id 20261123-043944-iib-course-reel \
       --etalonnage 20261122-202132-iib-reel --jetoniseur JET
   ```
   Puis la session mère inscrit la ligne qui porte l'empreinte, `AUDIT-R4-LECTURE-1-IIB` et `ISSUE=SANS-DEFAUT` ou `ISSUE=DEFAUT` (une seule issue et, pour `DEFAUT-AUTORISE`, un seul identifiant `GO-…` par ligne : voir l'écart 5).
3. Lecture (2) :
   ```
   PYTHONPATH=src python scripts/lecture_iib_2_diffusion_v5.py --racine . --run-id 20261123-043944-iib-course-reel \
       --etalonnage 20261122-202132-iib-reel --registre-decisions MAIN/registres/decisions.md \
       --registre-sondes MAIN/registres/sondes-iib-v1.md --jetoniseur JET
   ```
   Puis committer les deux sorties, leurs compagnons et le manifeste de la lecture.

Codes : 0 écrit et scellé ; 1 refus avant le manifeste, rien d'écrit ; 3 arrêt après le manifeste, seul `diag/<run de la lecture>/arret.json` écrit. Un refus « runs/… existe déjà » (deux lancements dans la même seconde) se relance une seconde plus tard.

## 3. Essais

- `PYTHONPATH=src python -m pytest -q tests/test_lectures_iib_v5_v1.py` : **153 passés** (environ 85 s). Matières : lignes construites à la main au schéma `oracle-iib-v5` ; une course jouet entière jouée par `lanceur_v5.executer` (étalonnage, conditions, course avec distillation et évaluation à 32 tâches, résumé et manifeste), dans un dépôt git jetable ; les gardes du jetoniseur réel sur les quatre fichiers tirés des objets du commit `e5677bbf` (essai sauté, et dit, si les objets manquent).
- Couverture de la table de la section 14 : chaque ligne a son cas sain et ses artefacts (T0 ; E0 à E9 ; spécification et modules ; configuration ; graines ; liste fermée ; présentation ; statistique (1) avec les quatre phrases ; blocs rapportés ; citations, chaîne exacte pour N et P, en-têtes produites par `designation_v5.designer` lui-même ; garde d'ordre ; garde de l'audit, dont « `DEFAUT` puis `SANS-DEFAUT` : refus » ; même course ; jetoniseur ; identifiants, dont l'essai rouge `len(tok)` contre `tok.vocab_size` ; décodage et fidélité, avec contrôle qu'aucun fichier n'est créé et que seule la clé (et le champ) est imprimée ; statistique (2) égale à l'appel direct ; base « premier coût » ; script d'audit, arbre inchangé ; forme lue par l'extrait, contrôles de `construire` recopiés ; écriture ; scripts, codes 0, 1 et 3 ; reproductibilité à l'octet sur deux copies ; fils de calcul).
- Essais antérieurs des modules importés (`test_iib_lectures_v1`, `configuration_v1`, `designation_v5`, `regle_v5`, `lecture_cout_v5`, `branches_v5`, `configuration_v5`, `jumeau_v5`) : **235 passés**.
- Suite entière (9 400 essais) : voir la section 7.

## 4. Écarts à la spécification proposés (lecture la plus stricte retenue)

1. **Fragment « sonde » contre la liste permise (section 12).** La liste fermée permet `registres/sondes-iib-v1.md` et les trois textes cités (`prereg/lecture-sondes-…`), que le fragment interdit `sonde` refuserait. Code : le seul fragment `sonde` est levé, et pour ces seuls chemins sous la racine des registres (registre : lignes de scellement seulement ; textes cités : empreinte seulement, et seulement pendant le contrôle T0). Tous les autres fragments restent interdits partout.
2. **D'où vient le mode avant T0.** La spécification ne le dit pas. Code : un script lancé en ligne de commande est toujours en mode réel ; le mode jouet n'existe que par l'argument `essais` de `main(...)`, appelé en mémoire par les essais (refusé en mode réel) ; le mode déclaré est exigé égal à celui de la configuration de la course (arrêt sinon). Le jetoniseur d'essai passe par le même argument.
3. **Citation de la lecture (1) quand *p* n'est pas calculable (10.1).** Lu à la lettre : `texte` est nul dès que `p_cite` est nul, quelle que soit la phrase (même « dommage agrégé vu », dont le corps n'emploie pas *p*). L'autre lecture (nul seulement pour « dommage non vu à cette puissance ») est à trancher par la session mère. En mode réel, l'effet minimal détectable est présent dès que la désignation a nommé N ou P ; *p* n'est nul que si l'excès moyen du maître n'est pas strictement positif.
4. **« Heures croissantes » (T0)** : lu strictement (deux heures égales refusées).
5. **Garde de l'audit (7.4)** : une ligne qui porte plus d'une issue `ISSUE=…`, ou une ligne `DEFAUT-AUTORISE` qui porte plus d'un identifiant `GO-…`, est refusée (la spécification ne dit rien de ces cas).
6. **Alias des graines (section 8).** Chaque lecture ne passe au module d'origine que les noms qu'elle lit (deux pour (1), quatre pour (2)), non les six ensemble : chaque lecture ne dérive que ses propres clés (table de la section 8).
7. **Script d'audit** : la spécification et les modules d'origine sont contrôlés à leurs empreintes avant la garde 1 (ajout).
8. **Ordre** : la forme de `--etalonnage` (E2) est contrôlée avant E0, parce que la liste fermée en a besoin.
9. **Clé `entrees`** : seulement les fichiers sous la racine de lecture (course, et la sortie de (1) pour (2)). Les registres sont dans `ordre_du_temps`, le jetoniseur dans `decodage`, la spécification et le code dans `lecture`.
10. **« Refus si l'une des trois sorties existe déjà » (7.4, point 4)** : lu comme les deux sorties de (2) et leurs compagnons.
11. **Durcissements sans effet sur un résultat** : lecture JSON stricte qui refuse aussi les nombres non finis écrits en clair (`1e999`) ; garde de fidélité qui compare aussi les types (booléen contre entier, nul) ; jetoniseur réel qui exige aussi le nom du modèle de l'agent, et la version chargée et la version installée de `transformers` et `tokenizers` ; signature `ouvrir(sorte, chemin, racines, lecture=…, cle=…)`, élargie pour porter la liste fermée.
12. **Lectures de fichiers hors de `ouvrir`**, faites par du code d'origine : la pièce inscrite et ses modules gelés (par `bases_textuelles_v1`, comme en v1), les compagnons `.sha256` (par `scellement.verifier`), le dossier du jetoniseur (par `AutoTokenizer`, après le contrôle de la liste fermée). Les fonctions d'origine ne reçoivent que des chemins déjà passés par `ouvrir`, et chaque JSON qu'elles ouvrent est d'abord relu strictement.
13. **Arrêt après le manifeste** : toute exception, et pas seulement `GardeArret`, écrit `arret.json` et rend le code 3 ; une interruption du clavier est relevée de nouveau après l'écriture.
14. **Nom du fichier d'essais : `tests/test_lectures_iib_v5_v1.py`, et non `tests/test_iib_lectures_v5.py` (section 14).** Le nom de la spécification changeait l'issue d'un essai antérieur, ce que la même section interdit. `tests/test_iib_lanceur_v5.py::test_amorce_v5_et_lanceur_de_session_v3_differences_bornees_aux_changements_declares` exige que la liste scellée de l'amorce (`scripts/tests-cibles-iib-v5-v6.txt`) soit égale à `tests/test_iib_*_v5.py` : l'essai passait en rouge, constaté sur la suite entière. Un nom en `test_iib_*_v1.py` aurait de même cassé `tests/test_iib_inventaires_v1.py::test_la_liste_ciblee_de_iib_existe_et_couvre_les_essais_de_iib`. Le nom retenu n'entre dans aucun motif lu par un essai antérieur. Les essais neufs n'ont pas changé.

## 5. Ce qui n'est pas éprouvé

- Rien n'a été joué sur la course réelle. Le jetoniseur réel n'a été éprouvé que pour ses gardes, sur aucun identifiant réel. La fidélité du décodage sur les 2 560 actions réelles reste la première épreuve de la lecture (2).
- La comparaison des versions de `transformers` et `tokenizers` avec le manifeste du run n'est pas jouée contre la valeur réelle, qui n'a pas été lue.
- La course jouet désigne l'oracle P. La voie N n'est éprouvée que sur des entrées construites (citations, présentation, statistique).

## 6. Ce que j'ai lu (registre « qui a lu quoi »)

- **Lu en entier** : `CLAUDE.md` (dans la consigne) ; la spécification scellée ; la pièce de structure `…/scratchpad/pour-fable/structure-sorties-course-v5-sans-valeur.txt` ; `scripts/extrait_iib_etats_lectures_cote_moniteurs_v3.py` de `origin/claude/iib-executante-v1` (`7eb8006d…`).
- **Code lu, en entier ou par passages** (arbre `3326499e`) : `iib/lecture_v1.py`, `iib/bases_textuelles_v1.py`, `iib/configuration_v1.py` (lignes 1 à 100), `iib/regle_v5.py`, `iib/lecture_cout_v5.py`, `iib/configuration_v5.py`, `iib/designation_v5.py`, `iib/branches_v5.py`, `manifeste.py`, `scellement.py`, `gardes.py` ; et par passages `iib/lanceur_v5.py`, `iib/jumeau_v5.py`, `iib/rapportes_v5.py`, `iib/oracle_v5.py`, `iib/tours_v1.py`, `iib/modele_v5.py`, `iib/jouet_v5.py`, `iib/versement_v5.py`, `t06/cout.py`, `t06/test_croise.py`, `harnais/formats.py`, `harnais/run_harnais_factice.py`, `scripts/lecture_iib_{1,2}_*_v1.py`, `.gitignore`.
- **Essais lus** : `tests/iib_v5_outils.py`, `tests/iib_distillation_v5_outils.py`, `tests/test_iib_distillation_bout_en_bout_v5.py`, `tests/test_iib_lectures_v1.py` (lignes 1 à 410), `tests/test_iib_lanceur_v5.py` (`_monde`).
- **Jetoniseur** : les quatre fichiers du commit `e5677bbf`, extraits dans `…/scratchpad/jetoniseur-v1/jetoniseur/` (ce dossier seul), empreintes vérifiées. Seuls `clean_up_tokenization_spaces`, `vocab_size` et `eos_token_id` en ont été lus par programme, et le jetoniseur a été chargé une fois pour en contrôler la taille et les fins.
- **Jamais ouvert** : aucune valeur des sorties de la course réelle (rien sous `diag/`, `donnees/` ni `runs/` de l'arbre, ni de l'arbre `course-v8`) ; aucune consigne privée ; rien sous `docs/verdicts/`. Toutes les sorties ouvertes pendant le développement sont celles de courses jouets fabriquées dans le bloc-notes ou dans les dossiers temporaires des essais.

## 7. Suite entière et comparaison avec la base

- `python -m pytest -q` en entier (9 400 essais) est trop lent en un seul processus (environ 3 % en 15 minutes). Il a été joué en quatre parts parallèles (fichiers triés, répartis un sur quatre) : **8 786 passés, 410 en échec, 200 sautés, 4 xfail** (total 9 400), avec le fichier d'essais encore sous son nom d'origine.
- Comparaison : les 54 fichiers qui portaient un échec ont été rejoués sur un arbre de la base `03c2d9549` (spécification seule, sans le code neuf). **408 des 410 échecs sont identiques sur la base**, donc antérieurs : amorces et scripts de T0.6 qui demandent des outils ou une machine, registres réels de `main`, inventaires, accords échus au 24 novembre. Les deux autres :
  1. `test_iib_lanceur_v5.py::test_amorce_v5_et_lanceur_de_session_v3_differences_bornees_aux_changements_declares`, causé par le nom du fichier d'essais ; corrigé par le changement de nom (écart 14), puis rejoué : passe.
  2. `test_iib_lectures_v1.py::test_garde_piece_chargee_a_l_empreinte_inscrite_sain_et_artefacts` dépend de l'ordre, sans rapport avec le code neuf. L'essai exige qu'aucun `scripts/__pycache__/mots_et_cout_t06_v3*` n'existe ; un essai joué avant lui dans la suite entière (`tests/test_mots_et_cout_t06_v3.py`) crée ce fichier. Reproduit sur la base : ces deux fichiers joués ensemble font échouer l'essai.
- Les inventaires qui échouent déjà sur la base (`test_cibles_invisibles_v1` à `v3`, `test_iib_inventaires_v1`, `test_depot_expurge_v7` à `v9`) ont été relus sur le code neuf : aucun des trois modules neufs n'y est désigné comme constructeur d'invite ou comme lecteur de la clé `cibles`, et aucun fichier neuf ne porte de fragment retiré par nom. Le garde-fou du dépôt sur les suppressions (`test_aucune_suppression_ailleurs_dans_le_code_v5`) passe sur les modules neufs.
- Bilan : **aucun essai antérieur ne change d'issue du fait du code neuf**.
