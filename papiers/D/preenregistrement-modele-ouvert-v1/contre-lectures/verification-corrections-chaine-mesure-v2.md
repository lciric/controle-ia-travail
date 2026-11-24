# Vérification des corrections, chaîne de mesure v2

Tests : 8 réussis (31 s). JSON v2 cohérent avec le code (manifeste complet, clé « non probant », intervalles de bootstrap).

## Mes 12 points
1. advantage_task : corrigé pour le taux principal (`primary_rate` filtre, `control_task_rate` à part, testés, garde si aucun épisode). Reste mineur : `descriptive` et `price_decomposition` mélangent encore tâches à avantage et tâches témoins.
2. Triche stricte vs large : corrigé dans la forme (`hack_truth` strict, `broad_failure` descriptif, `assertions_altered` ne compte que les assertions altérées ou supprimées). Réserve nouvelle (voir N1) : `hardcoded` et `impossible_task` sont des entrées, aucun détecteur n'est livré ni validé.
3. Cas limites de la vérité : corrigé (quatre cas plus `visible=None`, testés). Règle d'exclusion « non évaluable » toujours non écrite : mineur, partiel.
4. Chaîne de pensée : corrigé, déjà bon.
5. Price : corrigé en grande partie. Appariement par tâche, bootstrap par tâche, résidu renommé « transmission + composition », seuil de 30 tricheurs sur parent et enfant, enfant sans tricheur testé. Réserves : N2 et N3.
6. Filtre au hasard : partiellement. Le champ `scope` du JSON dit que le contrôle est arithmétique. L'enfant reste le parent par construction. La borne de non-effet sur modèle réel reste à fixer dans le préenregistrement, non dans ce code.
7. Générateur circulaire : corrigé pour l'essentiel. Une transmission plantée (+0,05) est retrouvée : résidu 0,055, intervalle [0,048 ; 0,063], et le test s'applique aussi à +0,08. Le cas sans transmission contient 0. Limite assumée : le générateur suit toujours le modèle testé. Pas de test avec `advantage=False` dans le générateur : mineur.
8. Portée de l'essai à blanc : corrigé (champ `scope`, clé `primary_per_thousand_synthetic_non_probant`).
9. Gardes : partiellement. Extraits et testés : règle du contrôle positif (sain et artefact « tout mentionné »), filtre inconnu, enfant sans tricheur, `descriptive([])` en GuardError, `visible=None`. Non corrigé : les gardes de cohérence de `dry_run` (écart de sélection à Var/E, filtre au hasard, intervalle sans transmission, transmission non vue) restent en ligne et jamais déclenchées en test. `conf` hors de (0, 1) non validé.
10. Test des signes : partiellement. `check_design_pairs` existe et est testé, mais `sign_test_two_sided` ne l'appelle pas et n'avertit pas quand n < 6. L'hypothèse d'indépendance entre graines n'est pas écrite.
11. Borne à zéro événement : partiellement. La docstring exige des unités indépendantes, mais rien ne le garantit dans le code ni sur `conf`.
12. Reproductibilité : majoritairement corrigé (empreinte du fichier de tests, configuration et son empreinte, `argv`, commit, paramètre `rng` mort supprimé). Réserves : N4.

## Défauts nouveaux
N1. (mineur-majeur) Détecteurs de `hardcoded`, `impossible_task` et `assertions_altered` hors périmètre : leur rappel détermine le taux principal. Un rappel inférieur à 1 sous-estime la triche. Ajouter une validation par cas plantés (triche codée en dur connue) avant lecture, à inscrire au préenregistrement.
N2. (mineur) Dans `price_decomposition`, `weight` est rappelé à chaque rééchantillon. Avec le filtre au hasard (`r.random()`), les poids sont retirés de nouveau et du bruit entre dans l'intervalle de ce seul contrôle. Précalculer les poids une fois ; exiger un poids déterministe.
N3. (mineur) L'appariement se limite aux tâches ayant des tricheurs dans les deux générations : on conditionne sur le résultat, ce qui peut biaiser le résidu quand l'enfant n'a plus de tricheurs sur beaucoup de tâches. Rapporter le nombre de tâches écartées (`paired_tasks` seul ne suffit pas). Sans `rng` ou avec moins de 10 tâches, l'intervalle est omis sans avertissement : lever une GuardError ou écrire `interval: None`.
N4. (mineur) `git rev-parse` s'exécute dans le répertoire courant : il renvoie une chaîne vide, non « unavailable », hors dépôt, et ne signale pas un arbre sale. La configuration est recopiée à la main, avec les graines `boot-1..3` absentes de la liste « tasks ». Docstring et usage citent encore v1 ; la ligne « hack truth … modified » est périmée.
N5. (mineur) Les gardes du dry_run (intervalle sans transmission contenant 0) échouent par construction une fois sur vingt pour une graine donnée : acceptable car les graines sont fixes, mais à écrire.

## Verdict
Non pas encore : v2 corrige l'essentiel (1 à 5, 7, 8) ; il reste, avant scellement, à tester les gardes de cohérence de `dry_run` sur une panne injectée (point 9), à câbler `check_design_pairs` et à valider `conf` (10, 11), et à ajouter la validation des détecteurs (N1) et le précalcul des poids (N2), sans nouvelle contre-lecture complète.
