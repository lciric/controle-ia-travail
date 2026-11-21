# Note de revérification — ordre de l'étalonnage, version 2, brouillon 2 — cl1

Date : 2026-11-21. Même vérificateur (Claude Opus 5.5), même mandat ; je ne suis pas l'auteur de la pièce. Pièce : `ordre-etalonnage-ii-b-v5-v2-brouillon2.md` (`9bf05c30…`, compagnon vérifié).

**Verdict : conforme ; scellable une fois les huit champs remplis.** Un mineur (n1) est à préciser par la mère à l'application.

- **Rejeu** : les deux programmes, joués en chaîne sur une copie du brouillon 8 (`ordre-rejeu-v2-b12/`), rendent `284d9ec1…` puis `9bf05c30…`. Les brouillons 1 et 2 de la version 2 sont **identiques à l'octet**.
- **Ce qui change** du brouillon 8 au brouillon 2 de la version 2 :
  - l'en-tête de la version 2, avec sa cause et GO-2026-11-21-87 ;
  - le code : quinze correctifs, arbre `bbcd9a84…` ;
  - la liste figée v5 (`f9ff477d…`, 24 fichiers) et 275 essais ;
  - l'amorce `a4686068…` ;
  - la vérification du correctif 0012, remplie ;
  - § 11 : deux rangs de plus et la phrase d'application.
  
  Rien d'autre ne change.
- **Arbre retrouvé** : `0011` puis `0012` appliqués sur mon `arbre-final` (arbre `ed9b0e48…`, rangs 1 à 13) rendent **`bbcd9a84a77ac667ef6f9106b19afe29ffab041f`**. Dans cet arbre :
  - la liste `scripts/tests-cibles-iib-v5-v5.txt` a pour empreinte `f9ff477d…` et compte 24 fichiers, et l'amorce porte cette empreinte en dur ;
  - l'amorce a pour empreinte `a4686068…` ;
  - le lanceur de session `42d295c8…` est inchangé, comme le dit l'ordre.
- **Empreintes des correctifs neufs** : `0011` `947e5a49…` et `0012` `4cd18c1f…`, compagnons OK. Chaque empreinte des lignes changées correspond à son fichier : la relecture par l'API `ea3ffcc0…`, la vérification du 0012 `5bd13368…`, mes notes `6a9e2e79…`, `350b4c61…` et `ffe2e024…`, et le brouillon 8. La tête locale du développeur, `887561b7…`, est dans le dépôt local, et son arbre est bien `bbcd9a84…`.
- **GO-2026-11-21-87** est sur `main` : relance accordée d'avance, option (a), sous GO-2026-11-21-70.
- **Aucun « 271 » ni arbre d'avant là où il ferait foi** : les lignes Code, Amorce et Essais, le § 4 étape 6, les variables du § 5 (`IIB_TESTS_ATTENDUS=275`) et le § 11 portent 275 et `bbcd9a84…`. Les « 271 » et `ed9b0e48…` qui restent sont dans l'historique de l'en-tête et du statut, et au § 4 étape 2 (la répétition décrite est celle de la version 1). Le seul `ed9b0e48…` du § 11 désigne la base des treize premiers rangs.
- **Les huit champs restants** sont les champs attendus, et aucun n'est faux : branche du code, commit revu, commit de lancement, configuration, fichier d'entrées, intouchables, étiquette, sort de la machine.
- **n1** : `origin/prep/iib-code-v5` pointe aujourd'hui sur `b2d568c4…`, le commit de lancement de la version 1 (arbre `a893c778…`, avec la configuration et les pièces), et non plus sur `62356e2f…`. Le § 11 écrit « les rangs 14 et 15 appliqués sur `origin/prep/iib-code-v5` (`62356e2f…`) » : c'est sur ce commit nommé qu'il faut les appliquer, pas sur la tête de la branche. Le contrôle de l'arbre `bbcd9a84…` rattraperait l'erreur ; la mère le précise à l'application.
