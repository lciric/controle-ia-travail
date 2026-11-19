# Contre-lecture du correctif du lanceur de session du saboteur à budget : contrôle « aucune tâche commune » (commit f9a8aaeb), v1

Contre-lecteur neuf (n'a écrit ni ce code ni ses essais), du côté du saboteur à budget (barreau 8), exclu de tout rôle côté sondes. Le 19 novembre 2026.

Objet : commit `f9a8aaeb91cf165c6d318f8782d1e8581c5eb105`, branche `prep/iib-code-v4` (identique à `origin/prep/iib-code-v4`), parent `ec3b0329cd59db676007bd6c9ea3f0c36cf3ce95`. Lu dans l'arbre de travail propre `/tmp/claude-0/-home-user-controle-ia-travail/7344498a-9e3b-55a8-9388-941e130beae8/scratchpad/wt-iib-v4` (rien n'y a été modifié ni committé ; `git status` vide avant et après).

## Conclusion

**AUTORISABLE** : le commit peut porter le commit de lancement. Deux réserves mineures, non bloquantes, plus bas (motif vide quand une tâche n'a pas d'identifiant ; doublons et énoncés vides acceptés par le lanceur mais refusés par la course, écart antérieur au correctif et inatteignable en mode réel).

## Verdicts

1. **Empreinte et périmètre de la différence : conforme.** `git diff ec3b0329..f9a8aaeb | sha256sum` = `faa7f33feeded870266624c236d926948027f0f4f82977d4cb98ad7861f7cb08`, 185 lignes. Trois fichiers seulement (`git diff --name-status`) : `scripts/lancer_iib_v1.sh` modifié, `scripts/tests-cibles-iib-v2.txt` neuf, `tests/test_iib_taches_v2.py` neuf (13 essais). Le module partagé `src/controle_ia/environnements/pilote_a.py` et la répétition jouet `src/controle_ia/iib/jouet_v1.py` sont inchangés.

2. **Lecture en ligne du lanceur équivalente à `charger_taches`, refus sinon : conforme (deux réserves mineures).** Éprouvé en extrayant la lecture en ligne du lanceur corrigé et en la jouant, cas par cas, contre `charger_taches` de la course sur des fichiers scellés fabriqués (17 cas) :
   - forme « résultat » (`resultat.taches`), forme plate (`taches`), et les deux clés présentes avec des contenus différents : mêmes tâches lues des deux côtés (`resultat.taches` prime) ;
   - `resultat` présent mais pas un objet (liste, chaîne, nul) : la course lève une exception, le lanceur refuse avec le motif nommé ; aucune divergence ;
   - `resultat` présent sans `taches` alors que `taches` existe au premier niveau (et de même `resultat` nul avec `taches` au premier niveau) : la course lève `KeyError: 'taches'` (ou une erreur de type) sans se replier sur le premier niveau ; le lanceur refuse lui aussi, sans repli. Ils ne doivent pas diverger, et ne divergent pas ;
   - fichier qui n'est pas un objet (liste au premier niveau, liste contenant la chaîne « resultat », chaîne, nul) : refus des deux côtés ;
   - liste vide (forme résultat ou plate) : le lanceur refuse (code 2, sans `lancement.txt`) ; `charger_taches` rend une liste vide, que la course refuserait ensuite par ses comptes de tâches. Le lanceur est plus strict, comme demandé ;
   - tâche sans `identifiant`, tâche qui n'est pas un objet, identifiant non hachable : refus des deux côtés. **Réserve mineure** : côté lanceur, le refus (code 2, sans `lancement.txt`) porte un motif vide, « contrôle « aucune tâche commune » refusé () », la trace Python allant sur la sortie d'erreur ; refus tenu, motif non nommé ;
   - **doublons d'identifiant dans un même fichier, énoncé vide** : le lanceur accepte (lecture par ensemble), la course refuse (`GardeArret` dans `charger_taches`, avant tout calcul mais après la création de l'instance). **Réserve mineure, non bloquante** : écart déjà présent avant le correctif (le lanceur d'avant lisait aussi par ensemble), hors de la consigne (même clé de lecture que la course), et inatteignable en mode réel : la validation de la configuration (`iib/configuration_v1.py`, lignes 325 à 327) exige les empreintes des deux fichiers réels (`8d20a698…`, `76cdeace…`), et l'essai neuf vérifie par le chargeur de la course 32 et 64 identifiants uniques, aucun commun.
   - Détail de forme : le motif écrit « liste des tâches de évaluation » (l'élision est impossible dans le texte entre apostrophes simples du lanceur) ; cosmétique.

3. **Rien d'autre ne change dans le comportement du lanceur : conforme.** Les seuls changements de comportement sont dans le contrôle lui-même : la forme `resultat.taches` est lue, la liste vide est refusée (le lanceur d'avant acceptait une liste plate vide), le libellé du refus change. Le format de `lancement.txt`, les codes de sortie (2 sur tout refus) et la suite du parcours sont inchangés. L'ancien libellé « tâche(s) de réserve dans l'évaluation » (`git grep` au parent et au commit, hors dossiers interdits) n'apparaissait que dans `scripts/lancer_iib_v1.sh` au parent ; aucun essai, ni l'amorce, ni aucun autre script ne le citait (les autres occurrences de la tournure sont dans des documents et dans le message d'arrêt du code de la course, `iib/lanceur_v1.py` ligne 88, non touché). L'empreinte du lanceur n'est écrite en dur nulle part (parent `5e968357…`, corrigé `3279e3dc…`).

4. **Les 13 essais neufs attrapent le défaut : conforme.** Rejoués sans toucher l'arbre, sur une copie du lanceur d'avant (`git show ec3b0329:scripts/lancer_iib_v1.sh`, empreinte `5e968357ec806bbe1eaa70558495083de27e217128e2208f4c45f8db948fa56b`) dans un dossier à moi, un greffon d'essai pointant `test_iib_scripts_v1.LANCEUR` sur cette copie : **11 échecs, 2 réussites**, comme annoncé. Lecture des échecs :
   - 4 attrapent le défaut de comportement : forme réelle saine, formes mêlées, les deux fichiers réels (refusés par `KeyError: 'taches'`) ; liste plate vide acceptée (« CONTRÔLES CONFORMES ») ;
   - 6 attrapent un refus par plantage, sans motif nommé (« … () : aucune création ») : clé absente, `resultat` sans `taches`, liste vide de forme réelle, `taches` qui n'est pas une liste, liste au premier niveau, tâche commune en forme réelle (que le lanceur d'avant ne pouvait pas détecter) ;
   - 1 échoue sur le seul libellé : tâche commune en forme plate, que le lanceur d'avant refusait déjà correctement (« communes r0 »).
   - Les 2 réussites : la forme plate du jouet (saine des deux côtés) et l'essai des fichiers réels par le chargeur de la course (indépendant du lanceur).
   Sur le lanceur corrigé : **13 réussites**.

5. **Suites ciblées : conforme.** Suite v2 (`scripts/tests-cibles-iib-v2.txt`, 14 fichiers) au commit corrigé : `469 passed in 146.40s (0:02:26)`. Suite v1 seule (`scripts/tests-cibles-iib-v1.txt`, 13 fichiers, celle que joue l'amorce) : `456 passed in 135.71s (0:02:15)` ; la liste v1 passe intégralement au commit corrigé, et cette ligne satisfait le motif de l'amorce pour 456 essais attendus.

6. **Amorce inchangée, rien de ce qu'elle vérifie n'est rompu : conforme.** `scripts/amorce_instance_iib_v1.sh` : même objet au parent et au commit (`b6d9ffe4…`), empreinte `5d78e7e4b6466fd61fac423ec4dd1d9a3fb87d97c4ad99f345b624ac97beb433`. Elle joue la liste v1 d'empreinte écrite en dur `847676eff87f20c8aa5d7b1a1b401a7dd025c71c57d190ec0ba9c306f397e3b6` : liste inchangée, empreinte recalculée égale. Le nombre attendu (456) est tenu (point 5). La liste v2 et les essais neufs ne sont pas joués sur l'instance (l'amorce joue la v1), ce qui est voulu : le contrôle corrigé s'exécute sur la machine de lancement, pas sur l'instance.

## Remarques hors des six points (aucune bloquante)

- Le lanceur est corrigé sous son nom v1, alors que la liste et les essais reçoivent un nom v2. Le lanceur n'a encore servi à aucune course et aucune empreinte ne l'épingle ; à consigner par la session mère si la règle des versions dans les noms doit s'appliquer ici.
- L'en-tête du lanceur cite toujours les seuls essais `tests/test_iib_scripts_v1.py` ; les essais neufs n'y sont pas nommés. Cosmétique.

## Empreintes relevées

- `scripts/lancer_iib_v1.sh` au commit : `3279e3dcc631519e574c2011f9f143d956d3b668c729a176cd8efc0e99dece8f` ; au parent : `5e968357ec806bbe1eaa70558495083de27e217128e2208f4c45f8db948fa56b`.
- `tests/test_iib_taches_v2.py` : `9b77331dc38d7400f11f42f3b70cba9214f491f95243c5d25f1625efd338a0f5`.
- `scripts/tests-cibles-iib-v2.txt` : `2f531cf6be94babc70f44ac17449c4112841e3186d4e3f082b1ae53c799c19c8`.
- Fichiers réels des tâches (au commit, sceaux conformes) : `taches-entrainement.json` `8d20a698d76baa8a42cd1494227fc411ef043d24a67a413e5cf812541166a4fd`, `taches-evaluation.json` `76cdeace861d2fff45ca732c55c2d97611dcd47edc7c27d62bdad4c37755e67e` ; seule leur structure (clés `run_id`, `manifeste_sha256`, `resultat` ; `resultat.taches` présent) a été regardée.

## Dernières lignes des suites jouées

- 13 essais neufs, lanceur d'avant : `11 failed, 2 passed in 13.92s`.
- 13 essais neufs, lanceur corrigé : `13 passed in 13.29s`.
- Suite ciblée v2 : `469 passed in 146.40s (0:02:26)`.
- Suite ciblée v1 : `456 passed in 135.71s (0:02:15)`.

## Refus d'outils, nettoyage, interdits

Aucun refus d'outil. Dossiers temporaires d'essais (copie du lanceur d'avant, greffon, fichiers fabriqués, dossiers de base des essais) supprimés. Aucun fichier interdit ouvert, aucun résultat d'expérience lu, aucune dépense, aucune instance, aucun modèle chargé ; rien modifié, committé ni poussé dans l'arbre revu ; ce rapport est le seul fichier écrit dans le dépôt, scellé et non committé.
