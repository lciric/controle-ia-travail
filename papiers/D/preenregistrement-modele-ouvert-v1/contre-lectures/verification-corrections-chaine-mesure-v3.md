# Vérification de la chaîne v3 (diff contre v2 ; 12 tests réussis en 63 s)

- Point 1 (mineur : `descriptive` et `price_decomposition` mélangent tâches à avantage et tâches témoins) : non corrigé. Aucun changement dans le diff. À rapporter comme limite connue ou filtrer sur `advantage_task`.
- Point 6 (filtre au hasard) : sans objet pour le code ; reste une exigence du préenregistrement (borne de non-effet sur modèle réel). Le champ `scope` reste là.
- Point 9 : corrigé. `check_dry_run` est extraite ; le test injecte cinq pannes (contrôle positif, sélection du moniteur, sélection du hasard, transmission plantée non vue, intervalle nul excluant 0) et vérifie qu'elles lèvent GuardError, avec le cas sain. `conf` est validé et testé (0, 1, 1,5).
- Point 10 : corrigé avec une réserve. `sign_test_two_sided(..., design_pairs=)` appelle `check_design_pairs` et est testé. Mais `design_pairs=None` est le défaut : le garde est facultatif, donc contournable en silence. Mineur ; rendre l'argument obligatoire ou consigner dans le préenregistrement que l'appelant passe toujours le nombre de paires du plan.
- Point 11 : corrigé (conf validé ; docstring d'unités indépendantes ; le code ne peut pas vérifier l'indépendance, reste à la charge de l'appelant).
- N1 : partiellement. `validate_detector` (rappel au moins 0,9, faux positifs au plus 0,05, cas plantés positifs et négatifs obligatoires) est testée sur sain et deux artefacts. Rien ne force son appel avant `hack_truth` : c'est une fonction disponible, non une condition de lecture. À inscrire dans le préenregistrement comme étape préalable scellée, avec les seuils 0,9 et 0,05 justifiés.
- N2 : corrigé. Les poids sont calculés une fois (`wcache`), test par compte d'appels exact. Réserve mineure : la clé est `id(e)` ; correct tant que les épisodes restent vivants, ce qui est le cas.
- N3 : corrigé pour le signalement (`interval_status`, `residual_interval_95: None`, `caveat`, comptes des tâches écartées dans chaque sens, testés). Le biais de conditionnement n'est pas corrigé, seulement déclaré ; acceptable si le préenregistrement le dit.
- N4 : corrigé (`git -C` dans le dossier du script, repli « unavailable », liste de graines complète, docstring et usage en v3). L'arbre modifié n'est toujours pas signalé : mineur ; ajouter `git status --porcelain` au manifeste.
- N5 : corrigé par note dans la docstring.

Défaut nouveau : aucun bloquant. Seuls les deux points mineurs ci-dessus (garde facultatif du test des signes, détecteurs non câblés).

Verdict : prêt à être scellé, sous réserve que le préenregistrement impose `design_pairs`, la validation préalable des détecteurs et la déclaration des limites des points 1 et 6 et du conditionnement des tâches.
