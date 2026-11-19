# Journal de l'exécutante du saboteur à budget — v2

Session `session_013QMaymHf2YhybDs3MJ62xr`, branche `claude/iib-executante-v1`. Suite du journal v1 (`registres/iib-executante/journal-v1.md`, `20bcd761…`), qui reste tel quel. Exploratoire, non opposable (R-522). Phase 1 : aucune instance, aucune recherche d'offre, aucune dépense ; aucune machine inventoriée ni touchée (la mère s'en charge).

## Phase 1, point 2 — dernière ligne de la suite ciblée à `ec3b0329`
- Suite ciblée des essais du saboteur à budget (liste `847676ef…e3b6`), au processeur, dans l'arbre détaché à `ec3b0329` : **456 passed in 167.69s**. Dernière ligne retenue pour la configuration : « 456 passed » (fixée par la mère, R-3556).

## Phase 1, point 4 — configuration (scellée hors dépôt, non commise)
- Brouillon 3 de la configuration réelle, `config-iib-reel-v1-brouillon3.json`, `53a6f45e305634296958a6801e847f24ccb497367b18369ffcb20e5fccfc74c1`, scellé dans le bloc-notes de la session, **non commis** (consigne de la mère : rien avant le mot de Lazar).
- Seul champ manquant : le mot de Lazar pour la création. La garde du code revu rend 1 sans ce mot, 0 avec une référence factice (essai à blanc, rien gardé de la référence factice).
- Chemin proposé pour la configuration commise : `docs/notes/barreau8-iib-v1/config-iib-reel-v1.json`, sur `prep/iib-code-v3`, enfant direct de `ec3b0329`, configuration et sceau seuls.
- La mère a déclaré la phase 1 finie (R-3572). Le commit de lancement attend la ligne du mot de Lazar transmise par la mère.

## Tâches ajoutées par la mère — côté moniteurs (depuis le journal v1)
- Note d'interface de la passe pour le côté moniteurs : v2 (couples V-01 à V-14), v3 (W-01 à W-03, `477815d1…`), v4 (`1983692a…`), v5 (N-01 à N-04, `407099bc…`, portée sur `main` et transmise), v6 (`20c9ed6e480646b6bf3a5f6007be5f88b439c916763a618f3880634e92ad8ce1`, clés de premier niveau de l'extrait des états). Chaque version fabriquée par programme depuis les couples du rapport de vérification, chaque « avant » présent une seule fois ; programmes et différences dans `docs/notes/barreau8-iib-v1/`. Écarts de forme déclarés sans nouvelle version : titres « v2 » puis « v4 » restés dans les v3 et v5 ; point d'en-tête de la v6 qui dit encore « Version 4 ».
- Programme de l'extrait de la passe pour le côté moniteurs : v1 (`e6172629…`), v2 (`645248bb…`), essais v2 17 passed. Dans `fichiers_de_la_passe`, la clé est le chemin relatif au dépôt (`donnees/<run>/<nom>`), pas le nom de base : dit à la mère ; une v3 seulement sur son mot.
- Programme de l'extrait des états des lectures : v1 (`55e3edbc…`, essais 19 passed), v2 (`7236a47a…`, essais 37 passed) : garde d'ordre du temps sur la ligne de scellement du texte du côté moniteurs, chaîne des deux lectures, forme du nom du run. Nom de livraison confirmé : `etats-lectures-iib-v1.json`. Tous les essais d'extrait ensemble : 82 passed.
- Décision d'ordre de la mère (R-3571) : les lectures du dommage et de la diffusion ne sont jouées qu'après la ligne de scellement du texte des sondes du côté moniteurs ; leurs lignes au registre des décisions ne portent que le chemin et l'empreinte de la sortie, jamais la phrase.

## Suite complète des essais du dépôt, au processeur (pour information, non exigée par l'ordre)
- Arbre de travail sur `b73745b7` (branche de journal), clone superficiel. Premier passage arrêté par la limite de temps des tâches de fond vers 73 % (6 540 essais sur 8 854 collectés) ; le reste rejoué fichier par fichier (111 fichiers, le fichier frontière rejoué en entier).
- Premier passage : 13 échecs, aucun dans un fichier de l'exécutante ; causes lues un par un : module `pypandoc` absent (3, connus, corpus arXiv) ; sortie de course de T0.7 absente du clone (1) ; inventaires de la garde de la référence cachée qui trouvent des fonctions non examinées dans des modules d'autres chantiers (5) ; liste des noms de la copie expurgée qui trouve 36 fichiers de courses d'idéation non classés (3) ; un essai de la course d'idéation sur bassins étroits qui échoue dans la suite et saute seul (1, dépendance d'ordre).
- Reste : 372 failed, 2014 passed, 3 skipped, 4 xfailed. 371 échecs dans les essais des scripts d'amorce et de lancement de T0.6 (versions 2 à 13) : leurs amorces démarrent « après l'échéance » du GO qu'elles citent, désormais passée (dépendance au calendrier, pas au code) ; 1 échec dans la lecture de T0.7 (`8cb539f9` absent du clone superficiel).
- Aucun échec dans les essais du saboteur à budget ni dans les essais d'extrait.

## Reste
- Mot de Lazar transmis par la mère : remplir le champ, sceller la configuration finale, commit de lancement sur `prep/iib-code-v3`, contrôles à blanc rejoués au commit de lancement.
- Réponse de la mère sur la forme des clés de l'extrait de la passe.
- Phase 2 seulement après la remise complète de la mère.
