# Contre-lecture des différences (lecture v3 → v4, passe v4 → v5) et troisième essai d'intégration de bout en bout — v1

Contre-lecteur : Claude Opus 5.5 (`claude-opus-5-5`), sous-agent neuf ; n'a écrit ni les codes, ni les essais, ni les notices, ni le texte ; auteur des deux contre-lectures précédentes (`contre-lecture-code-lecture-v1-v1.md`, `c5f12da0…cb85` ; `contre-lecture-code-lecture-v3-integration-v1.md`, `c07e5032…0228`).
Début : 2026-11-19T04:35:56Z ; fin : voir la dernière ligne.

## Empreintes des pièces (toutes égales à celles de la commande)
- texte, brouillon 13 : `7628ebfd8534bd44287e0a233a80339e6dde57db88fd0ada3df3c6a1b2305cd4` ; différence 12 → 13 faite par programme (mot à mot), lue en entier
- lecture v4 : `fda9bdb35d1924b09505b52129e9a4f7f8e941969c0959bc4364c4e7704c14b4` ; essais : `50d697625953fca3a42c93b5cdc0330b832d878da4a6e6d1115e07c0791a430f` ; notice : `e0e5ce6e3f8231ce393ab0fc2a5007c7abb5fd0151398c3654c332442d548df4`
- passe v5 : `a5eeef6203b558dbc0c1b58085d2dd4d13617a7c76e9aa374aa224304b19759f` ; essais : `c8cbfdbee7043f776106f7c46f242a2b4d577d0086c4d02273067441b80db0ff` ; notice : `e7591c562bee76cc50fce2a98d19d805a7e4879ceb3c4a0b05b9c4def1205558`
- différences `diff -u` lecture v3 → v4 (335 lignes) et passe v4 → v5 (76 lignes), lues en entier ; notices de la lecture v3 → v4 comparées par programme.

## 1. Essais (au premier plan, un fichier par commande)
- `tests/test_barreau8_moniteurs_lecture_v4.py` (04:36:01Z → 04:38:41Z) : `171 passed in 159.00s (0:02:38)`
- `tests/test_barreau8_moniteurs_passe_v5.py` (04:38:42Z → 04:40:08Z) : `103 passed in 85.05s (0:01:25)`
Dossiers temporaires supprimés.

## 2. Remarques N-1 à N-5 du second rapport

| remarque | état |
|---|---|
| N-1 tâche réduite à une classe | **réglée** (lecture v4 et texte, l. 391) : `_a0_taches_a_une_classe` rend la tâche et la classe qui lui reste, sans autre effet ; le motif d'échec est retiré ; la règle d'échec est « égalité des deux chemins non tenue, (a) ou (b) ». Vu en intégration : `tache-02`, classe restante 0, essai tenu, ligne L2. |
| N-2 notice | **réglée** (section « Ce qui a été éprouvé, et ce qui ne l'a pas été ») ; elle ne mentionne pas encore ce troisième essai (sans conséquence). |
| N-3 portée de la finitude | **presque réglée** : contrôle avant toute autre condition, sur les entrées des neuf noms et sur toutes les candidates au plancher, quelle que soit la classe, dans les deux codes ; **reste un écart de portée** (C-1 ci-dessous). |
| N-4 nom unique de la sonde décisive | **réglée** dans la passe v5 (`sum(x.nom == d.nom for x in sondes) == 1`) ; même portée que la lecture (l'index du fichier de la sonde). |
| N-5 audit non ouvert par l'intégration | **réglée** : audit ouvert par sa commande sur une livraison fabriquée par les montages des essais de la lecture (point 4). |

## 3. Ce qui est neuf
- **(a) Égalité des deux chemins** (texte l. 390). La lecture décisive (`ligne_de_production`), le placebo, la dose, les descriptifs, le bras de diagnostic et l'essai (plancher et égalité) lisent le tableau des scores par action par **la même fonction** `lire_scores_d_action` (ligne = champ `rang` de l'action, colonne de la direction, case du maximum). L'égalité est **exacte** (`lus == recalcules`, aucun écart permis), **jouée avant (i)** (`essai_de_la_chaine`, avant le premier tirage). Les bornes de l'essai viennent des **seuls champs `rang` et `jetons_notes`** (`_a0_bornes` : sommes cumulées dans l'ordre de `rang`), et les mêmes bornes servent à l'injection (ii) et à la permutation (iii). Une inégalité fait échouer l'essai **sans rejeu**, **rien d'autre n'est joué**, et la sortie ne porte que la sonde et le nombre d'actions inégales, **jamais un score**. (iii) suit la lettre : `permutation(n)` sur les actions de `H` notées rangées dans l'ordre des clés, l'action de rang k reçoit les scores de l'élément k. **Conforme.** Sur la livraison jouet saine : 59 actions comparées par sonde, 0 inégale.
- **(b) Nom de la course** : `exiger_meme_course` dans `ouvrir_lecture`, après la garde de réception, où la trace et l'extrait sont lus ensemble ; refus `[3]` (liste d'arrêt, ligne 3) ; inscrit aux conditions de départ. **Conforme** (texte l. 97, 168, 275, 410) ; vu en intégration (point 4).
- **(c) Finitude** : passe v5, contrôle sur les entrées des neuf noms **dans les trois index** (`for role in sorted(contenus)`), puis sur les candidates au plancher dans le fichier de plancher de chaque sonde. Lecture v4 : les neuf noms cherchés **dans les seuls index des fichiers des sondes** (`legeres`, `neuves`), **pas dans celui du fichier des planchers** ; candidates au plancher : même règle que la passe. Portée différente (C-1). Sans effet sur une livraison (la passe s'arrête la première), mais la lettre des deux codes diffère, et celle du texte (« toute entrée de l'index ») ne dit pas lequel.
- **(d) Nom unique de la sonde décisive** : les deux codes l'exigent dans l'index du fichier de la sonde, à la clé de la table. **Même chose.**
- **(e) Nom des couches 7 ou 23 en double** : les deux codes cherchent dans l'index du fichier de la sonde seulement (lecture : refus `[15]` ; passe : arrêt). **Même portée.** Le texte dit « dans l'index » sans dire lequel (phrase T-4).

## 4. Essai d'intégration (versions courantes)
Scripts : `/tmp/claude-0/-home-user-controle-ia-travail/ccd98af0-e97a-5c3c-8902-30e463468b85/scratchpad/cl-lecture/integration_v4_monde.py`, `…/integration_v4_cli.py`, `…/cli_jouet_v4.py`, `…/audit_v4.py` ; journaux `…/log-v4a-*.txt`, `…/log-audit-v4.txt`. Dossiers de travail supprimés.

**Monde avec une action sans jeton noté dans chaque condition** (même montage que le second essai : dépôt git d'essai portant une copie du paquet, jouet de la passe v5 plongé dans 24 couches, planchers rangés à l'envers, registre propre aux six clés ; 04:41:25Z → 04:46:08Z) :
1. Passe v5 : livraison écrite ; neuf sondes « lue » ; bordereau du code de la passe à chemins relatifs, module `passe_recalcul_v5` présent.
2. Par l'enveloppe à cadre réduit, en sous-processus : `modules`, `bordereau-code`, `reception` (tenue), `etats` (conforme), `puissance` réduite, tous en code 0. `python -m … lecture_sondes_v4 reception` (cadre du texte) : passe registre, texte et modules, puis refuse `[r2]` sur la taille des morceaux (30 000 contre 50 000 000, constante du texte), comme attendu.
3. **Artefact « nom de course différent »** (extrait des états `run_id` « 20261119-010203-course-autre », trace « 20261118-235959-course ») : `lecture` code 2, « REFUS [3] le nom de la course porté par la trace de la passe diffère de `run_id` de l'extrait des états … » ; aucune sortie écrite.
4. Même nom dans la trace et l'extrait (ligne des états remplacée dans le registre d'essai) : `lecture` code 0, « LECTURE ÉCRITE ET SCELLÉE ; lignes déclenchées : L2 », ligne `LECTURE-SONDES-IIB` **inscrite par la lecture**, dernière du registre. Égalité des deux chemins : 0 action inégale sur 59, pour chaque sonde. Essai de la chaîne tenu, sans rejeu (artefact positif au-dessus pour les trois sondes, bornes basses de D 0,175 à 0,266) ; `tache-02` nommée « classe restante 0 » pour la tromperie, **sans ligne d'échec**. Conditions de départ : « nom de la course : égal dans la trace de la passe et dans l'extrait des états ».
5. Seconde `lecture` : code 2, « REFUS [5] une sortie de la lecture existe déjà … ». `audit` : code 2, « REFUS [15] aucun déclencheur » (jouet sans déclencheur).

**Ouverture de l'audit par sa commande** (04:46:34Z → 04:46:46Z) : livraison fabriquée par les montages des essais de la lecture v4 (`Monde(sf, graine=1, effets=EFFET)`, `monter`), commandes `lecture` et `audit` jouées par l'enveloppe en sous-processus. `lecture` : code 0, L1, déclencheur d2 (« tromperie-difference_moyennes-c15 sur B100-contre-H : aire 0.9547… ») ; `audit` : code 0, « AUDIT MÉCANIQUE ÉCRIT … ; ligne AU-b », aucun défaut, production et états relus égaux. Le monde sans action vide n'a pas été rejoué : le monde ci-dessus porte une livraison saine, actions vides comprises, et l'égalité y tient.

## 5. Lacunes encore relevées par les développeurs
1. **L'égalité n'éprouve pas le champ `rang` lui-même** (r5 l'exige égal au rang dans le fichier ; un rang faux mais cohérent déplacerait les deux chemins ensemble). Mérite une phrase de limite, parce que le texte présente l'égalité comme l'épreuve de l'association des scores aux clés : « L'égalité des deux chemins n'éprouve pas le champ `rang` lui-même : la garde de réception r5 exige qu'il soit le rang de l'action dans l'ordre du fichier. »
2. **Après une inégalité, (i), (ii) et (iii) ne sont pas joués** : c'est ce que fait le code ; le texte dit seulement « sans rejeu ». Mérite une phrase : « Après une inégalité des deux chemins, ni (i), ni (ii), ni (iii) ne sont joués. »
3. **Le nom de la course n'est pas rejoué à l'audit** : la liste du contenu de l'audit est fermée et ne le porte pas ; la lecture n'a pu tourner que si les noms étaient égaux, et l'extrait et la trace relus par l'audit sont ceux des mêmes lignes de registre. Pas de phrase nécessaire ; si la session mère veut l'écrire : « L'audit ne rejoue pas le contrôle du nom de la course ; la lecture n'a tourné que s'il tenait. »
4. **Portée de la finitude** (C-1) : phrase : « … sur toute entrée qui porte le nom de l'une des neuf sondes nommées, dans l'index de chacun des trois fichiers de sondes et de planchers, … » ; correction de la lecture : chercher les neuf noms aussi dans l'index du fichier des planchers.
5. **Nom en double aux couches 7 et 23** : les deux codes cherchent dans l'index du fichier de la sonde ; phrase : « … un nom de sonde des couches 7 ou 23 qui paraît plus d'une fois dans l'index de son fichier … ».

## Remarques
- **C-1, MINEURE (code de la lecture)** — `regle_des_sondes_lues`, contrôle de finitude : les neuf noms ne sont cherchés que dans les index des fichiers `legeres` et `neuves` ; la passe v5 les cherche aussi dans l'index du fichier des planchers. Sans effet sur une livraison (si la passe a livré, aucune entrée de ces noms n'y est non finie), mais les deux codes n'appliquent pas la même règle. Correction : ajouter le rôle du fichier des planchers à la recherche des neuf noms (ou, si la session mère retient l'autre lecture, retirer ce rôle à la passe), avec la phrase T-1.
- **C-2, MINEURE (notice de la lecture v4)** — ne mentionne pas ce troisième essai (audit ouvert par sa commande ; nom de course éprouvé de bout en bout). Sans effet sur l'exécution.

## Conclusion
**Liste fermée des corrections** — aucune n'est bloquante ; l'interface entre les deux codes et la ligne de commande tiennent de bout en bout (réception, extrait, recette, refus du nom de course différent, lecture, inscription de sa ligne, refus de la seconde lecture, audit ouvert par sa commande) :
- **Code de la lecture** : C-1 (mineure). **Notice de la lecture** : C-2 (mineure).
- **Code de la passe** : aucune.
- **Phrases à porter au texte** (avant le scellement) :
  - T-1 : « La finitude … sur toute entrée qui porte le nom de l'une des neuf sondes nommées, dans l'index de chacun des trois fichiers de sondes et de planchers, … »
  - T-2 : « L'égalité des deux chemins n'éprouve pas le champ `rang` lui-même : la garde de réception r5 exige qu'il soit le rang de l'action dans l'ordre du fichier. »
  - T-3 : « Après une inégalité des deux chemins, ni (i), ni (ii), ni (iii) ne sont joués. »
  - T-4 : « … un nom de sonde des couches 7 ou 23 qui paraît plus d'une fois dans l'index de son fichier … »
Une fois C-1 faite (ou T-1 tranchée dans l'autre sens et la passe alignée) et les quatre phrases portées, je tiens les deux codes pour **conformes au texte et intégrés de bout en bout : prêts pour leurs lignes de registre une fois le texte scellé**.

## Refus d'outil
Aucun.

## Fichiers lus
Différence du texte 12 → 13 (par programme) ; différences des codes (par programme, en entier) ; notice de la lecture v4 (par différence avec la v3) ; essais : exécution seulement, et montages des essais de la lecture v4 (`fabriquer_sondes`, `Monde`, `monter`) et de la passe v5 (constantes, `ecrire_course`). Rien sous les chemins interdits ; aucun registre du dépôt ; aucun résultat.

Fin : 2026-11-19T04:47:55Z (`date -u`, prise juste avant le scellement).
