# Différences entre le brouillon 2 et le brouillon 3 de la spécification des lectures du dommage et de la diffusion sur la course v5 — v1

> EXPLORATOIRE, NON OPPOSABLE (R-522). Pièce de travail du côté exposé ; jamais transmise au côté des moniteurs. Une ligne par différence ; sa cause est entre parenthèses : r1, r2 ou r3 (vérification du brouillon 2), « mot sur les nœuds » (mot de la session mère du 2026-11-24T17:12Z), « jetoniseur » (dossier fourni par la session mère).

- Brouillon 2 : `specification-lectures-dommage-diffusion-course-v5-v1-brouillon2.md`, `5968aa37bfb1931c8a828a5fa2ba6a4d9dc9dec2dfcdd008f16f82b7b8f30c3b`, intact (R12).
- Brouillon 3 : `specification-lectures-dommage-diffusion-course-v5-v1-brouillon3.md` ; son empreinte est donnée par le rédacteur dans son compte rendu.
- Vérification du brouillon 2 : `verification-specification-lectures-v5-cl1-brouillon2.md`, `a477220249a3060637aadd981d23cfe24d210c3f5ed7f9b10656d57ca9313030`.
- Écrit le 2026-11-24 (UTC) par Claude Fable 5.2, rédacteur de la spécification. Tout ce qui n'est pas listé ici est identique à l'octet (contrôle : `diff` des deux fichiers, 29 blocs).

## En-tête

1. Titre : « brouillon 2 » devient « brouillon 3 ».
2. Ligne « Statut » : « brouillon 3, à sceller par la mère après constat du contre-lecteur » ; renvois au brouillon 2, à sa vérification, au brouillon 1 et à la contre-lecture 1 par leurs empreintes.
3. Ligne neuve « Mot rendu sur les trois nœuds » : session mère, accord d'autonomie `GO-2026-11-24-35`, message de 2026-11-24T17:12Z, cité tel que transmis (mot sur les nœuds).
4. Ligne « Date » : heure du brouillon 3, celles des brouillons 1 et 2 gardées.
5. Table de traitement de la contre-lecture 1 : une phrase de plus dit qu'elle est celle du brouillon 2, gardée telle quelle, et que les options de nœud qu'elle nomme ne sont plus dans cette version (mot sur les nœuds).
6. Section neuve « Traitement de la vérification du brouillon 2 » : table des trois mineurs r1 à r3, tous corrigés.

## Sections 0 à 2

7. Section 0, point 5 : « trois nœuds, à trancher » devient « trois nœuds, tranchés », tous trois par leur option (a), chacune dite en une proposition (mot sur les nœuds).
8. Section 1, phrase finale : « sous leurs options recommandées… l'option (b) du nœud N-2 y toucherait » devient « tels que tranchés, les nœuds n'y touchent pas » (mot sur les nœuds).
9. Section 2 : la racine des registres est nommée et définie (r2).

## Section 3

10. Contrôle T0 : le fichier passé par `--registre-sondes` doit être exactement `<racine des registres>/registres/sondes-iib-v1.md` ; la racine des registres est le dossier parent du dossier `registres/` qui le porte ; tout autre nom ou dossier arrête (r2).
11. Contrôle T0 : « pris sous la racine de l'arbre qui porte le registre » devient « pris sous la racine des registres » (r2).

## Section 5

12. Section 5.2 : `ouvrir(racine, chemin_relatif)` devient `ouvrir(sorte_de_racine, chemin_relatif)`, sous l'une de trois racines nommées, seul point de lecture du code neuf (r2).

## Sections 6 et 7

13. Section 6.3, « Consignation, avec une issue » : après tout défaut, seule une ligne postérieure `ISSUE=DEFAUT-AUTORISE`, dont l'identifiant d'accord ouvre une ligne du registre des accords, laisse partir la lecture (2) ; une ligne `ISSUE=SANS-DEFAUT` écrite après un défaut ne débloque rien (r3).
14. Section 7.1, mode réel : source du dossier du jetoniseur citée (branche orpheline `jetoniseur/llama31-8b-instruct-0e9e39f2-v1`, commit `e5677bbf2696e9364da7f4bf191abcc5de16eabc`, dossier `jetoniseur/`), empreintes des quatre fichiers recalculées et égales aux références ; `--jetoniseur` désigne ce dossier, non la racine de la branche (jetoniseur).
15. Section 7.4, point 2, garde de l'audit, réécrite : quatre refus examinés dans l'ordre ; « la dernière ligne décide » disparaît ; s'il existe une ligne `DEFAUT`, il faut une ligne `DEFAUT-AUTORISE` après la dernière ; l'identifiant d'accord doit ouvrir une ligne de `registres/go.md` (contrôle facultatif proposé par le vérificateur, pris) ; la sortie consigne les issues lues, dans leur ordre (r3).
16. Section 7.5, clé `audit_de_la_lecture_1` : « l'issue lue » devient « les issues lues, dans leur ordre » (r3).

## Section 12

17. Liste fermée, réécrite sous trois racines : racine de lecture, racine des registres, dossier du jetoniseur, chacune avec sa liste ; un chemin permis présenté sous une autre racine arrête ; `registres/decisions.md` doit être le fichier passé par `--registre-decisions`, dans le même dossier `registres/` ; `registres/go.md` s'ajoute, pour les seules lignes de l'identifiant cherché ; le script d'audit n'ouvre rien sous la racine des registres (r2, r3).

## Section 13

18. « Les nœuds sont tranchés avant le scellement » devient « ont été tranchés » (mot sur les nœuds).

## Section 14

19. Ligne « T0 » : artefact de plus, registre passé sous un autre nom ou hors d'un dossier nommé `registres` (r2).
20. Ligne « liste fermée » : artefacts de plus, chemin permis sous une autre racine, registre des décisions hors du dossier `registres/` de la racine des registres, ligne du registre des accords autre que celle de l'identifiant cherché (r2, r3).
21. Ligne « garde de l'audit », réécrite : `DEFAUT` puis `SANS-DEFAUT` est un refus (c'était un cas sain) ; `SANS-DEFAUT` puis `DEFAUT`, refus ; `DEFAUT-AUTORISE` avant le dernier `DEFAUT`, refus ; identifiant absent du registre des accords, refus ; cas sain neuf : `DEFAUT` puis `DEFAUT-AUTORISE` à identifiant présent (r3).
22. Ligne « décodage » : « clé seule écrite » devient « la clé seule est imprimée sur la sortie d'erreur ; rien sur disque », et l'essai vérifie qu'aucun fichier n'est créé (r1).
23. Ligne « fidélité » : même correction pour la clé de l'action et le nom du champ (r1).

## Section 16

24. Règle commune : devient « règle commune, appliquée » ; cite le mot rendu ; dit que la version ne porte qu'une option par nœud et que les options non retenues et leurs textes de rechange **sortent de la pièce**, lisibles au brouillon 2 (mot sur les nœuds).
25. Nœuds N-1, N-2 et N-3 : les trois sous-sections à options, recommandations, confiances et textes de rechange sont remplacées par une table à trois lignes (nœud, option tranchée, ce que dit la spécification, où) (mot sur les nœuds).
26. Alinéa neuf « Limites des options retenues, gardées en vue » : les inconvénients que le brouillon 2 écrivait pour chaque option (a), en une phrase chacun (mot sur les nœuds).
27. Sous-section des sept choix : titre « pour information de Lazar » ; phrase d'ouverture : ils ne bloquent pas le scellement, un mot contraire après le scellement est un écart ; point 4 : « sans décision nommée postérieure » (mot sur les nœuds, r3).

## Sections 17 à 19

28. Section 17, « provenance des fichiers du jetoniseur » : la session mère les a versés sur la branche citée ; le reste inchangé (jetoniseur).
29. Section 18, premier alinéa : « vérification des corrections » devient « constat des corrections du brouillon 3 », avec les cinq points à constater.
30. Section 19 : alinéa neuf « Lus en plus pour le brouillon 3 » (vérification du brouillon 2 ; noms et empreintes du commit du jetoniseur, `LISEZMOI.md` et fichier d'empreintes non ouverts).
