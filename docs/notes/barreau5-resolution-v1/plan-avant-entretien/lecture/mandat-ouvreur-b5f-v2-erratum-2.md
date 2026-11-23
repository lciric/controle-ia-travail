# Erratum 2 au mandat de l'ouvreur du barreau 5 — v2

Écrit le 22 novembre 2026 vers 23:30Z (`date -u`) par le concepteur de l'erratum de chaîne (Claude Opus 5.5), à la demande du conducteur (`session_013QMayjM1PQPWkLifMw9HDR`). Pièce de classe C.

- **Pièces visées** : `mandat-ouvreur-b5f-v2.md` (`3c3f1092c1935b3bc6adc165da6829d4571024c541e62b008fb7263c115bc3d6`) et son erratum 1 (`c9adf95d…`). Elles restent telles quelles (R12).
- **Source** : `erratum-chaine-relecture-decisive-b5f-v2.md` (`01298f0f73a731e6ee31e0e91b45367da75ba1bd2276ba5d041000b9f87da87b`), § 5, vérifié conforme (`verification-corrections-erratum-chaine-b5f-v1.md`, `08fd3453…`).
- **Accord** : GO-2026-11-22-147, qui donne la voie B et la variante à noms suffixés accordée d'avance.
- **Portée** : cet erratum prime sur ces pièces pour les seuls points ci-dessous.

1. **Branche des scores (voie B).**
   - `BRANCHE_SCORES` reste `donnees/barreau5-familles-jumelles-v1-lecture`, toujours lue dans `SCORES-B5F`. Le pas 6 joue donc « scores » de la version 1, et le nœud 9 est levé.
   - Tu récupères cette branche par son nom entier. Si une référence locale plus ancienne existait, tu la récupères en forçant (`+refs/heads/<nom>:refs/remotes/origin/<nom>`).

2. **Deuxième arbre : le code v3.**
   - **Mise en place.** Après le pas 6, tu récupères dans la racine, par son nom entier, la branche du code v3 (nom et commit `COMMIT_V3` donnés par le conducteur). Puis : `git -C <BN>/racine worktree add --detach <BN>/code-v3 <COMMIT_V3>`.
   - **La racine reste au code figé** : les pas 2 et 14 sont inchangés.
   - **Pas 3** : tu vérifies aussi, au commit v3, les empreintes que te donne le conducteur pour `src/controle_ia/barreau5_familles/ouverture_suffixes_v1.py`, `scripts/lancer_b5f_ouverture_suffixes_v1.sh` et `tests/test_ouverture_suffixes_v1.py`.
   - **Pas 4** : tu rejoues de plus, dans `<BN>/code-v3`, `tests/test_ouverture_suffixes_v1.py`, avec les mêmes options.
   - **Lanceur neuf** : `PYTHON_B5F=<BN>/racine/.venv/bin/python bash <BN>/code-v3/scripts/lancer_b5f_ouverture_suffixes_v1.sh …`, avec `<BN>/code-v3` comme RACINE.

3. **Pas 11, cas « (b) seule égale ».** Ce cas remplace « arrêt … jusqu'à l'erratum de chaîne ».
   - Le programme écrit la table de (b) par `ecrire_table`, au même chemin `/dev/shm/b5f-ouverture-v1/table/table-etiquettes-b5f-v1.json`, et imprime le nombre de lignes.
   - Tu continues au pas 11 bis.
   - Les cas « (a) égale » et « aucune égale » sont inchangés. Aucune troisième liste n'est jamais essayée.

4. **Pas 11 bis : `variante`, dans tous les cas.** Avant le pas 12, que le pas 11 ait donné (a) ou (b) :

   `… lancer_b5f_ouverture_suffixes_v1.sh variante <BN>/code-v3 <COMMIT_REGISTRE_1> <BN>/formation /dev/shm/b5f-ouverture-v1/table/table-etiquettes-b5f-v1.json`

   - **Commit prouvé.** Elle lit la ligne `SCORES-B5F` au registre de `COMMIT_REGISTRE_1` pour trouver le commit prouvé. Elle vérifie que la ligne d'épinglage de l'erratum figure au registre de ce commit : le code de la variante était donc figé avant la création de l'instance.
   - **Décision.** Elle vérifie la cohérence de la table et son égalité à l'engagement. Puis elle **décide sur les graphies de la table engagée elle-même** :
     - (a) si toutes ses familles sont des bases ;
     - (b) si chacune égale le nom de sa copie lue, que donne la branche de la formation ;
     - sinon, refus et nœud.
   - **Sortie.** Elle n'imprime que la lettre et les trois empreintes (E_a, E_b, engagement).
   - **Contrôle.** Sa lettre doit égaler celle du pas 11 ; sinon arrêt, nœud.

5. **Ordre des gestes** : `variante` et `preparer` (pas 11 bis et 12), puis `OUVERTURE-B5F` (pas 13), puis `ouvrir` (pas 15).
   - **En (a)** : `preparer` et `ouvrir` du lanceur v1, depuis la racine, comme écrit au mandat.
   - **En (b)** : `preparer` et `ouvrir` du lanceur neuf, avec les arguments de la version 1 et `<BN>/code-v3` comme RACINE ; les chemins de sortie restent ceux du mandat.
   - `preparer` n'exige pas `OUVERTURE-B5F` ; `ouvrir` la vérifie, avec les dates.

6. **Ligne d'ouverture en (b)** (pas 13).
   - Le contenu ne change pas.
   - Dans la référence, « de 30 couples nus (couples-b5f-nus-v1.json, sha256 <…>) » devient « des 30 couples de la pièce des sorties de la formation (couples-b5f-formation-v1.json, sha256 <…>) ; variante (b) de l'erratum de chaîne v2 (01298f0f…) ».

7. **Résultat en (b).**
   - **Fichier de plus.** Le dossier `…/resultat/` porte aussi `traduction-table-b5f.json` et son compagnon : la table de traduction par famille, sans nom opaque ; E_a, E_b, l'engagement ; l'empreinte de l'erratum. Tu ne l'ouvres pas. Au pas 17, tu le verses avec le résultat.
   - **Champ changé.** Dans le résultat, `a_garde_d_ouverture.code` porte le commit de `CODE-LECTURE-B5F`, la mention « égal hors des listes fermées de la v2 et de l'erratum », le commit v3 et l'empreinte de l'erratum, au lieu de « égal ».

8. **Arrêts, écarts, nœuds.**
   - Tout refus de `variante` ou du lanceur neuf est un arrêt, motif à la lettre, selon le § 7 (masque des noms opaques).
   - Les écarts déclarés du § 2 gagnent un point (3) : en (b), la table de (b) est écrite, et l'ouverture passe par l'entrée recomposée de l'erratum de chaîne v2. Cette entrée appelle le programme de lecture figé, inchangé à son empreinte. C'est l'écart 5 de cet erratum : point 7, troisième tiret, et liste d'arrêt, point 10.
   - Nœud 3 : l'accord est GO-2026-11-22-147.

9. **Lecteur du verdict : aucun erratum.** Son mandat (`mandat-juge-verdict-b5f-v2.md`, `17aafef2…`) ne lit que `resultat-lecture-b5f.json`, ce que dit sa l. 45 (« `diag/` hors du seul fichier du résultat »). Il n'en contrôle pas `a_garde_d_ouverture.code`.
