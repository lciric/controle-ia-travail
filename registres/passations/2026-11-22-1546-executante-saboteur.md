# Passation — exécutante v5 du saboteur à budget (session_01XJ6MgqUTEVCed6a2f6rWmC), 2026-11-22T15:46:15Z

Arrêt sur l'ordre de Lazar (15:43Z, par la mère) : « arrête tout … on n'a plus de crédits ici ». Rien n'est lancé ; aucun sous-agent ne tourne.

## Fait
- Étalonnage v5 : coupure propre à 16 USD (12:54:30Z), arrêt de 61875617 par l'identifiant (latence 14 s) ; relance courte (GO-2026-11-22-44/-66) : 27 lots + 27 identifiants + manifeste poussés sur essai/iib-explo-v6 (f4bf68bb), 55/55 vérifiés, archive cloisonnée donnees/iib-v5-etalonnage-disque-61875617-v1 (bcf25130). 61875617 détruite par la mère à 15:27Z (GO-2026-11-22-77), absente de l'inventaire. Passage des conditions **non joué** (gardé).
- Code de la course : correctifs 0014–0021 développés (Opus) et contre-lus puis vérifiés (autre Opus) : « course autorisable » ; poussés sur prep/iib-tirage-carte-v1 = 6696aca1f (arbre 725f3d58). Correctif 0022 (vitesse au premier lot, liste d'étalonnage v7 ; 297 essais v6, 311 v7 sur carte) écrit, **non contre-lu**, tête locale 4f538eefa (arbre a814f070), versé en patch. Correctif 0023 (garde de dépense : coupure effective = ligne − dépense antérieure réelle, GO-2026-11-22-77) **non écrit**.
- Reprise R001 (voie B, gardée pour plus tard) : écrite, 311 essais, essai central réussi, **non contre-lue**.
- Voie (A) : mandats Fable v1 et brouillon 2 ; additif et devis de (A) en brouillon 2 (Fable, commit 30ea7862 sur claude/iib-executante-v5-fable-additif-c) ; vérification : « pas encore scellable » (brouillon 3 demandé à Fable, non rendu).
- Comptes rendus 24 à 30 ; pièces sous registres/iib-executante/ (p1-code-course-v1, reprise-etalonnage-R001-v1, relance-courte-61875617-v1, contre-lecture-voie-A-v1, mandats, chiffres-devis-code-corrige-v1).

## Reste — chemin critique de la voie (A) (course au plus tard le 25 au matin)
1. Contre-lire et vérifier le 0022 ; écrire, contre-lire et vérifier le 0023 ; pousser le code final sous prep/ (mot de la mère).
2. Brouillon 3 de Fable (gardes du tirage à l'étalonnage, dépense déclarée vraie, mineurs, champs du § 6), puis vérification par le même contre-lecteur.
3. Configuration neuve de la voie (go_id GO-2026-11-22-75, étiquette iib-voie-a-v1, entropie tirée par la mère), fichier d'entrées, commit de lancement ; scellement par la mère.
4. Étalonnage rejoué sous IIB_TIRAGE=carte (essai/iib-explo-v7 ; vitesse lue au lot 2, 35,5 min) ; passage unique des conditions ; course (essai/iib-explo-v8, TESTS_ATTENDUS=312).

## Réserves
- Le gain de vitesse du tirage sur la carte n'est pas mesuré ; sur processeur, le neuf est plus lent ; la cause du ×5 n'est pas prouvée.
- Classifieur de cette session : refus d'un essai à blanc des gardes de destruction (non contourné).
- Outil du loueur : `execute` plante en 1.8.3 et 1.11.2 (lu par l'API directe).
- Copies de travail et sous-agents dans le bloc-notes : perdus à la fin de la session ; tout ce qui compte est versé ou poussé.

## Instances (inventaire 15:46Z)
58936096, 58936099, 58936100, 60988826 : exited (intouchables) ; 61932710 : running, autre chantier, non touchée. Aucune machine du saboteur. Crédit Vast 39,04 USD, recharge automatique active.
