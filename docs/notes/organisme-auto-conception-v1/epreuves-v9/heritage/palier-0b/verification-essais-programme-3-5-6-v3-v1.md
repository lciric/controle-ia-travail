# Vérification différentielle des essais v3 du programme des étapes 3 à 6 — v1

Vérificateur neuf, modèle S (a vérifié les v1 et v2). 2026-11-20. Rien n'est lancé en vrai, aucune graine décisive, aucune écriture dans le dépôt.

## Verdict : **À corriger** (un point, dans les essais ; le programme v2 n'est pas touché)

1. **Variable `PROGRAMME_3_5_6_MUTANT` : porte dérobée des essais.** Posée par erreur (ou avec un autre programme), elle fait charger n'importe quel fichier sans contrôle d'empreinte, et les essais passent sans rien signaler. Preuve : je l'ai posée sur une copie du programme v2 augmentée d'une ligne de commentaire (empreinte différente de `1f04cb46…`) ; les 30 essais joués (31 moins la chaîne entière, longue) passent, sans message. Un programme autre que le v2 peut donc être déclaré éprouvé. Correction : ajouter un essai `test_le_programme_charge_est_le_v2` qui exige `PR.empreinte_du_programme() == EMPREINTE_DU_PROGRAMME_V2` (il échoue chaque fois que la variable est posée, la preuve du mutant en compte alors trois échecs, dont celui-là, dits d'avance au rapport) ; à défaut, exiger de la variable une seconde variable portant l'empreinte attendue du mutant, contrôlée à l'import.

Les points 1, 2, 3, 5 et 6 sont conformes.

## 0. Empreintes
Table du sous-dossier v3 : 5 lignes, 5 OK (essais `cf1608c3…`, rapport, différentiel, deux journaux). Programme du bloc-notes du développeur : `1f04cb463c2fca7d2d67bfa3a8045bd4c9592e4e93bb564000ec102421cfdb14`, égal à celui versé sous `programme-3-5-6-v2/` (que les essais chargent dans l'arbre versé, `../../programme-3-5-6-v2/`).

## 1. Point 3 de ma v2 levé : conforme
`_verifier_le_retour` (appelée dans `…cas_sain_plante_la_chaine_finit_tenue`) exige : `frequences` et `reglages` couples de longueur 2 ; chemin égal à `<dossier>/etape-5/<fichier des fréquences>` et `<dossier>/etape-6/<fichier des réglages>`, existant ; empreinte égale au SHA-256 du fichier et à son compagnon ; `manifestes` de clés exactement 3 à 6, chacune égale au SHA-256 du `manifeste.json` de son étape. L'essai neuf `test_v3_main_imprime_le_retour_de_lancer` relit la sortie imprimée de `main` et lui applique les mêmes contrôles. Un second essai neuf (`…arret_au_point_5_aucun_retour_ni_gele_imprime`) contrôle que, sur l'arrêt au point 5, rien n'est rendu ni imprimé. Preuve par défaut planté (§ 4) : la permutation (chemin, empreinte) du retour est maintenant vue.

## 2. Point 2 : sortie de `main` non JSON — suffisant
Les lignes sont relues à une forme fixe (« étape N : manifeste EMPREINTE », « fréquences gelées : CHEMIN EMPREINTE », « réglages gelés : CHEMIN EMPREINTE »), toute autre ligne fait échouer, les clés manquantes aussi (`sorted(lu) == […]`, clés 3 à 6), et l'ordre chemin puis empreinte est contrôlé par l'égalité avec le chemin du fichier. C'est ce que reçoivent les programmes 6 bis–7 et 8–9. Un JSON ne couvrirait rien de plus ; imposer un programme v3 pour cela serait disproportionné. Limite sans conséquence : la relecture sépare sur l'espace, donc un chemin à espaces ferait échouer l'essai (jamais le cas sous le dossier d'essai ; à garder en tête pour la pièce de contrôle de la mère, qui fixe le dossier).

## 3. Point 3 : `lancer` remplacé par lui-même sous « essai-de-forme » — ne masque rien d'essentiel
Le remplacement (`lambda texte, racine, copie, dossier: origine(…, **REDUIT)`) garde la signature positionnelle de l'appel de `main` : une permutation des quatre arguments dans `main` serait vue. Ce qu'il écarte : l'appel de `lancer` de `main` sans couche ni taille, c'est-à-dire les couches des étapes ; il est éprouvé ailleurs (essai de la ligne de commande par sous-processus : refus du verrou avant tout geste, avec les valeurs par défaut ; essais « couche interdite » et « tailles réduites refusées »). Rien d'autre de `main` n'est contourné (contrôle du nombre d'arguments éprouvé par la ligne de commande, impressions éprouvées).

## 4. Point 5 : essais rejoués, comparés aux relevés — identiques
- 32 essais (31 du fichier plus l'essai final « aucune graine décisive » du code v6), sur copie, code v6 copié, couche « essai-de-forme » seule : **32 passés, 0 échoué (767 s)** ; relevé du développeur : 32 passés (835 s).
- Mutant (copie jetable du programme, une ligne permutée `(sha_f, chemin_f)` et `(sha_r, chemin_r)`) : **2 échoués, 29 passés** (763 s) ; les deux échecs : `test_v2_point_5_cas_sain_plante_la_chaine_finit_tenue` et `test_v3_main_imprime_le_retour_de_lancer`, sur l'assertion du chemin ; relevé : 2 échoués, 29 passés, mêmes essais. L'essai de la chaîne entière réelle, lui, passe sous le mutant (il n'utilise pas le retour, voir ma v2) : la couverture repose sur l'essai planté et sur `main`, ce qui suffit.

## 5. Point 6 : différentiel v2 → v3 — conforme au rapport
J'ai refait `diff -u` entre les essais v2 et v3 du dépôt : identique, hors les deux lignes d'en-tête, au fichier `differentiel-essais-v2-v3.diff` versé. Il ne change que : docstring, chargement (chemin vers le v2 et contrôle d'empreinte, variable du mutant), l'appel `_verifier_le_retour(r)` et sa définition, les aides de `main`, deux essais neufs. Le programme v2 est inchangé (même empreinte).

## 6. Écarts à mon mandat
Aucun refus de permission, de classifieur ni de garde ; aucune liste de processus ni commande d'arrêt ; aucune écriture dans le dépôt. Un `diff` avec substitution de processus (hors règle « commande simple ») pour comparer deux différentiels : sans effet.

Signé : vérificateur, modèle S.
