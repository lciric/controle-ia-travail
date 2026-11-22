Rédigé par Claude Opus 5.5 en remplacement de Fable 5.2 (limite atteinte) : À REVOIR PAR FABLE avant scellement.

# Différences — voie (A), brouillons 2 vers brouillons 3 de l'additif et du devis — v1 (pièce de travail)

Écrit le 2026-11-22 vers 16:55Z par le rédacteur de remplacement (Claude Opus 5.5), sous `mandat-fable-brouillon3-voie-A-v1.md` (`f1bfb4bd…`). Brouillons 2 intacts : additif `709e15357d6d9d53461414ca77a39746a95af3131eb8804185fc3d205731d15d`, devis `9b48987ba823426ed4c7a4c564bdeeec2290ad9a24cb54a4d06da2d0c9ff119e`. Source des corrections : `note-verification-brouillon2-voie-A-cl1.md` (`6be4c5c7…`), sections B, C et D. Une correction par ligne.

## Section B de la vérification
1. **B1, tirage à l'étalonnage** : contrôle « la commande de création imprimée porte `-e IIB_TIRAGE=carte` » ajouté au § 3.2 (et au § 3.4, ligne de l'étape 2) ; sinon, pas d'exécution, nœud.
2. **B1, arrêt de l'étalonnage** : « journal de l'amorce (`TIRAGE=`) ou marque de chargement (`tirage`) autre que `carte` : arrêt par l'identifiant » ajouté au § 5 et à la ligne « surveillance » du § 3.4.
3. **B1, course** : même contrôle de la commande imprimée au § 4.3 (point 5) ; même arrêt au § 5, partie « Course ».
4. **B2** : A2 écrit « sans rapatriement vérifié, aucune destruction, sauf par la minuterie de l'amorce, à l'échéance (ordre scellé ; A3) ».
5. **B3** : machine 61875617 détruite par la mère, par l'identifiant seul, le 2026-11-22 à 15:26:31Z, sur l'ordre de Lazar (« go toi-même », `GO-2026-11-22-77`) ; `registres/arrets.md` de `main`, ligne 153 (la note dit 15:27Z ; l'heure retenue est celle du registre).

## Section C de la vérification (correctif 0023)
6. **A3, dépense antérieure déclarée** : « borné à 5.00 », « 5,52 USD refusés » et la valeur `5.00` retirés ; c'est le compte vrai, arrondi au centime supérieur, sans borne ; la règle du correctif 0023 est écrite telle que le mandat la donne, avec ses cas vérifiés.
7. **A3, machine de la course** : « à 5 USD déclarés … 34,78 heures » retiré ; l'épuisement du lanceur tient le total sous 60 ; l'échéance, calculée sur 55, le précède toujours ; le pire reste 59,76 [M27], [M14].
8. **A3, ce qui tient la coupure** : le programme rend comme dépense antérieure le compte lui-même.
9. **§ 4.3, point 3** : forme exacte `bash scripts/lancer_iib_v3.sh --verifier-go-seulement 55 <compte de la voie>` avec `GO_ID`, sa ligne imprimée « coupure effective de la machine … ; correctif 0023 », code 0 attendu, refus en code 2.
10. **§ 6** : champs `<<VERIFICATION_DU_CORRECTIF_0022>>` et `<<CORRECTIF_0023_CHEMIN_EMPREINTE_ET_VERIFICATION>>` ajoutés ; `<<LISTE_ETALONNAGE_AVEC_ESSAI_DU_TIRAGE>>` rattaché au correctif 0022 (liste v7) et à sa vérification.
11. **§ 7, point 3** (borne de 5 USD, « non fait ») : retiré ; points suivants renumérotés.
12. **Arbre du code** : `6696aca1f` / `725f3d58` ne sont plus l'arbre de la voie ; `<<COMMIT_CODE_REVU_VOIE_A>>` et `<<ARBRE_CODE_VOIE_A>>` désignent l'arbre qui porte 0021, 0022 et 0023, vérifiés.
13. **Devis, § 4** (« Ce qui tient la coupure pendant la course ») : réécrit comme A3.
14. **Devis, liste d'arrêt** : ligne « garde de dépense du correctif 0023 en refus » ajoutée ; lignes du tirage (B1) ajoutées.
15. **Programme de calcul v3** : `DECLAREE_MAX` retiré ; valeur déclarée = compte ; [M24] (déclaré 5,52), [M25] (cas sain au compte haut 9,65, au lieu de 4,20), [M27] (coupure de la machine, épuisement et échéance aux comptes 0 ; 5,52 ; 9,65 ; 16,22) refaites ; aucune autre ligne ne change (comparé à la sortie v2).
16. **Vérification des gardes v3** : jouée au commit `9b03d0ea…` (arbre `ce3e51ca…`) sur `registres/go.md` de `main` (`e765c0ce…`) ; 0 ; 4,20 ; 5 ; 5,01 ; 5,52 ; 9,65 ; 16,22 ; 59,99 acceptés ; 60 ; 60,01 ; négatif ; non fini ; illisible ; configuration 61 ; ligne absente refusés ; épuisement lu sous le plafond total.

## Section D de la vérification (champs)
17. `<<VERIFICATION_DU_CORRECTIF_0021>>` rempli : `note-verification-0021-cl1.md`, `213537e7…`, « autorisable ».
18. `<<BRANCHE_CODE_VOIE_A>>` remplacé par `prep/iib-tirage-carte-v1` (poussée, à `6696aca1f` au distant, à avancer jusqu'à 0023).
19. `<<TESTS_ATTENDUS_ETALONNAGE_VOIE_A>>` et `<<TESTS_ATTENDUS_COURSE_VOIE_A>>` restent des champs ; valeurs annoncées 311 (liste v7) et 313 (liste de la course v2), rapport du développeur v6.
20. Restent des champs, inchangés : `<<COMMIT_CODE_REVU_VOIE_A>>`, `<<ARBRE_CODE_VOIE_A>>`, `<<EMPREINTES_AMORCES_ET_LISTES_VOIE_A>>` (l'amorce de l'étalonnage change avec la liste v7), `<<ENTROPIE_VOIE_A>>`, `<<INSTANCES_INTOUCHABLES>>`, `<<CONFIG_VOIE_A_CHEMIN_ET_EMPREINTE>>`, `<<COMMIT_LANCEMENT_ETALONNAGE_VOIE_A>>`.

## Faits neufs écrits
21. **Correctif 0022** (§ 2) : tête `4f538eef…`, arbre `a814f070…` ; fichier `diag/<run>/vitesse-premier-lot-iib-v5.json` et marque `etape=vitesse lot=1 …` décrits ; ils ne changent pas la règle de l'essai de vitesse (A4).
22. **`GO-2026-11-22-77`** cité en tête des deux pièces ; registre relu à la tête `3b7d0398…`.

## Ce qui ne change pas
Toutes les décisions du brouillon 2 : plafond 60, coupure 55, pire 59,76 ; essai de vitesse et son délai (35,5 min) ; garde de la course et ses délais ; échéances ; fichier d'entrées ; configuration ; voie (B) gardée ; chiffres attendu et haut du devis.
