# Erratum 4 au mandat de la session de lecture du barreau 5 — v2

Écrit le 22 novembre 2026 vers 23:30Z (`date -u`) par le concepteur de l'erratum de chaîne (Claude Opus 5.5), à la demande du conducteur (`session_013QMayjM1PQPWkLifMw9HDR`). Pièce de classe C.

- **Pièces visées** : `mandat-session-lecture-b5f-v2.md` (`b1eb2afc57d59df9d3a9eab96c22087ebbde6b4cb54824c4b62231ccc9fa991f`) et ses errata 1 à 3 (`cde0279c…`, `4d1678b5…`, `1c9d9ce1…`). Elles restent telles quelles (R12).
- **Source** : `erratum-chaine-relecture-decisive-b5f-v2.md` (`01298f0f73a731e6ee31e0e91b45367da75ba1bd2276ba5d041000b9f87da87b`), § 8.2 et § 8.5, vérifié conforme (`verification-corrections-erratum-chaine-b5f-v1.md`, `08fd34535a36b4c702510e9daf250fd85a962847d9b276ec9a41c2f89cb922c8`).
- **Accord** : GO-2026-11-22-147.
- **Portée** : cet erratum prime sur ces pièces pour les seuls points ci-dessous.

1. **Relance accordée, voie B.**
   - La relecture décisive tombée (instance 62047649, « commit des entrées … introuvable ») est relancée sous GO-2026-11-22-147. Cet accord s'ajoute à GO-2026-11-19-86 et à GO-2026-11-22-117 (erratum 1, point 2). Le § 9, point 5, est levé.
   - **La branche de sortie garde son nom** : `donnees/barreau5-familles-jumelles-v1-lecture`. Sa tête de la tentative tombée (`81061453`) est copiée sous `traces/barreau5-lecture-tentative-1`, et Lazar supprime l'ancienne branche. Tu n'y touches pas.
   - **Avant toute commande**, tu vérifies qu'elle est absente : `git ls-remote --exit-code origin refs/heads/donnees/barreau5-familles-jumelles-v1-lecture` doit rendre le code 2. Sinon arrêt, et tu le dis au conducteur.

2. **Coupure** (remplace le point 7 de l'erratum 2).
   - La relecture décisive a une coupure de **14 USD** (mot de la mère, R-5029 ; GO-2026-11-22-147). Elle reste sous les 21 USD de GO-2026-11-21-64 et sous les 33 USD de GO-2026-11-22-117.
   - **Ta veille la tient** (§ 5.4, pas 7) : arrêt par l'identifiant dès que le cumul de l'instance, plus un quart d'heure, atteint 14 USD.
   - L'instance garde son échéance, calculée par le code sur 21 USD ; tu ne retouches pas la commande.
   - La ligne d'engagement (pas 1) écrit 14 USD et les trois accords. La dépense antérieure y est le cumul commun relevé, marche tombée comprise.

3. **Commande de lecture, version 3.** Elle remplace la version 2 au § 3, point 6, au § 4, point 3, au § 5, au § 5.1, au § 5.4, pas 5, et au § 9, point 9.
   - **Arbre de commande** : au commit de code v3 que cite la ligne d'épinglage (point 5), et non plus à `5402367e`, dont il descend. Tu le récupères par le nom entier de sa branche, que te donne le conducteur.
   - **Lecture** :
     - tu lis `src/controle_ia/barreau5_familles/commande_lecture_v3.py` et `scripts/lancer_b5f_lecture_v3.sh` ;
     - tu rejoues sans les lire `tests/test_commande_lecture_v3.py`, `tests/test_amorce_b5f_lecture_identification_v1.py` et `tests/test_ouverture_suffixes_v1.py` ;
     - du rapport de vérification de ce code, tu ne vérifies que l'empreinte.
   - **Empreintes** : celles du module, du lanceur et des essais v3, que te donne le conducteur, recalculées par `git show` au commit v3. Plus `0adb6efba0a430f11c30e01da52787ef0482e20f6d74f699dbe8d76d2d300001`, l'empreinte de l'amorce embarquée.
   - **Commande** (pas 5) : `ARBRE_COMMANDE/scripts/lancer_b5f_lecture_v3.sh commande decisif ARBRE_COMMANDE OFFRE.json COMMIT_MARCHE BRANCHE_MARCHE AAAAMMJJ-HHMMSS-b5f-lecture ENTREES_COMMIT DIVERGENCE GARDE EXISTANTS.json`, avec les arguments de la v2.
     - L'identifiant de marche est neuf ; le commit des entrées est le même.
     - Le lanceur v2 ne sert plus.
     - `registres/go.md` de l'arbre de commande est tenu à jour.

4. **Amorce embarquée.** La v3 emporte l'amorce figée plus une seule ligne : l'aide d'identification inscrite dans le clone des entrées. Son empreinte, `0adb6efb…`, est imprimée par le lanceur avant la commande.
   - **Avant de jouer une commande** (pas 6) : tu décodes son segment base64 dans ton bloc-notes et tu en calcules l'empreinte. **Aucune commande n'est jouée si l'amorce décodée n'a pas l'empreinte `0adb6efb…`, quel que soit le lanceur qui l'a imprimée.** Une commande v1 ou v2 retomberait à l'identique. Dans ce cas : arrêt, au conducteur.
   - **Après la création** (pas 7) : la ligne de journal « amorce de lecture v1 : empreinte … » doit porter `0adb6efb…`. Sinon, arrêt de l'instance par son identifiant (R10) et appel du conducteur.
   - Le nom `/root/amorce_b5f_lecture_v1.sh` et ce libellé restent ceux de la v1 (écart déclaré à R12) : c'est l'empreinte du journal qui distingue les deux amorces.

5. **Ligne d'épinglage.** Le commit de la marche neuf (`COMMIT_MARCHE`, donné par le conducteur) est un enfant de `2beeec31` qui n'en diffère que sous `registres/`. Il porte au registre propre, sous la table, une ligne libre au format exact de l'erratum de chaîne v2 (§ 4.3 (d)) :

   `Erratum de chaîne de la relecture décisive (barreau 5) : erratum sha256 01298f0f73a731e6ee31e0e91b45367da75ba1bd2276ba5d041000b9f87da87b ; code de commande v3 et d'ouverture à noms suffixés v1, commit <40 signes>, vérifié sha256 <64 signes> ; accord GO-2026-11-22-147 ; branche de sortie donnees/barreau5-familles-jumelles-v1-lecture`

   - Ce n'est pas une ligne à clé. Tu ne l'écris pas ; le module v3 la lit et la vérifie.
   - Ton filtre des lignes à clé (erratum 2, point 2) ne change pas. Tu vérifies seulement, par programme, que cette ligne figure une fois et une seule au registre du commit de la marche, et tu y lis le commit v3.
   - `GO-LECTURE-B5F` reste telle quelle : elle cite la v2.

6. **Référence distante, récupérée en forçant** (§ 5.4, pas 8 et 9).
   - Si l'un de tes dépôts a récupéré l'ancienne `donnees/barreau5-familles-jumelles-v1-lecture`, tu la récupères en forçant, par son nom entier, avant « scores » et avant « detruire » : `git fetch origin +refs/heads/donnees/barreau5-familles-jumelles-v1-lecture:refs/remotes/origin/donnees/barreau5-familles-jumelles-v1-lecture`.
   - Sans cela, `ligne_scores` refuserait à tort.
   - « scores », « detruire » et « verifier-destruction » restent ceux de la version 1, joués depuis l'arbre figé.

7. **Essais rejoués** (remplace le point 3 de l'erratum 2 ; options de l'erratum 3). Un essai rouge : arrêt, son nom seul au conducteur.
   - **Arbre figé** :
     - `tests/test_barreau5_familles_relecture_v1.py` (24) ;
     - `tests/test_lancer_b5f_lecture_v1.py` (43) ;
     - `tests/test_barreau5_familles_engagement_v1.py` (23) ;
     - `tests/test_amorce_b5f_lecture_v1.py` (51) ;
     - `tests/test_amorce_b5f_lecture_entiere_v1.py` (4).
   - **Arbre de commande** :
     - `tests/test_commande_lecture_v2.py` (113 passés, 1 sauté) ;
     - `tests/test_commande_lecture_v3.py` ;
     - `tests/test_amorce_b5f_lecture_identification_v1.py` ;
     - `tests/test_ouverture_suffixes_v1.py` ;
     - `tests/test_barreau5_familles_lecture_v1.py` (102) ;
     - `tests/test_barreau5_familles_epreuve_verite_plantee_v1.py` (155).

8. **Ce qui ne change pas** : le reste du mandat et de ses errata. Notamment :
   - « config » et « verifier » de la version 1, sur le commit de la marche neuf ;
   - la règle de l'offre ;
   - la garde `une_sur_dix` ;
   - les points d'ancrage ;
   - la destruction seulement après « versement final prouvé » ;
   - ce que tu rends, et ce que tu ne rends jamais.
