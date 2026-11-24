# Vérification des corrections du banc des essaims à mêmes poids (v1 vers v2)

Même contre-lecteur (Claude Sonnet 5.5, classe B). Lus : `erratum-1-note-frontiere-essaims-memes-poids-v1.md`, `banc_essaims_memes_poids_v2.py` et son `diff` avec la v1. `main` non lancé. La note scellée (empreinte `058ede5b`) et la v1 du banc sont inchangées (`git diff` vide).

## Verdict : tient

Toutes les remarques sont tenues, aucune prédiction ni aucun seuil ne bouge, aucune régression de calcul. Deux remarques mineures nouvelles, sans effet sur la course.

## Remarque par remarque

- **1 (C3, T_naïf à la limite) : tenue.** Erratum point 3, chiffres identiques (0,91 à 0,93 ; 0,74 à 0,95), précision que l'échec ne juge pas la frontière. Le code ajoute `pieges_non_montres` (v2:119-121), sans effet sur `lecture`.
- **2 (C4, aléa partagé) : tenue.** Erratum point 2 : « dans le même repère », permutations partagées vs Gumbel partagé. Voir la remarque nouvelle A sur les chiffres.
- **3 (portée de « tient ») : tenue par l'erratum point 4. Voir la remarque nouvelle B : la chaîne imprimée par le code est inchangée.
- **4 (R4, pièges non montrés) : tenue.** v2:116-121 ; les taux sont des moyennes de booléens, donc 0.0 ou 1.0 exacts, la comparaison est sûre ; en prédictions attendues C2 et C3 en T_juste sont à environ 5 %, donc le drapeau ne se déclenche pas à tort.
- **5 (graines, manifeste R9) : tenue.** Docstring aligné sur le code ; `cles_graines` calculées après le `spawn` par configuration et avant le `spawn` des répétitions : `spawn_key` d'un enfant ne change pas ensuite, entiers sérialisables. `code_sha256` lit `__file__` en binaire : correct. `python` ajouté.
- **6 (hypothèses de la section 1) : tenue.** Erratum point 1.
- **7 (q corrigé / non corrigé) : tenue** (noté, non changé, erratum point 5).

## Prédictions, seuils, noyau

`diff` : seules modifications = docstring, imports (`hashlib`, `os`, `platform`, `subprocess`), en-tête du dictionnaire `res`, deux blocs après `lecture`. Inchangés : `K`, `N_PAIRES`, `N_AUDIT`, `N_REP`, `BIAIS_POSITION`, `FOCAL`, `SD_CONTEXTE`, `GRAINE`, `CONFIGS`, `PREDICTIONS`, `choix` à `statistiques`, seuil 1,645, seuil naïf, tirage des graines (`racine.spawn(len(CONFIGS))` avant tout nouvel appel : aucune consommation de graine nouvelle ; la création de `code`/`commit` n'utilise pas le générateur). Le fichier compile. Le calcul du commit : `git rev-parse HEAD` dans le dossier du script ; `FileNotFoundError` (sous-classe d'`OSError`) est attrapée ; pas de régression.

## Remarques nouvelles

- **A. Mineure** — erratum point 2. « excès d'accord 0,250 / 0,349 / 0,608 » : ce sont des **accords**, non des excès (l'excès sur 0,25 vaut 0, 0,099, 0,358), et les mesures étaient à grand effectif (400 000), non « petits effectifs ». Correction par un erratum 2 ou à la lecture ; sans effet sur le banc.
- **B. Mineure** — v2:112-116 (champ `lecture`) : la chaîne « la frontière tient sur le banc » reste imprimée telle quelle, malgré l'erratum point 4 ; la course doit donc être rapportée avec l'erratum, ce qu'il impose déjà (« il prime »). Optionnel : renommer sans changer la logique.
- **C. Mineure** — v2:90-94. Si `git` s'exécute mais échoue (hors dépôt, ou erreur), `commit` vaut la chaîne vide sans alerte, et un arbre modifié n'est pas signalé ; `code_sha256` couvre le contenu du code, donc rien n'est perdu. Optionnel : `"inconnu"` si la chaîne est vide, `git status --porcelain` pour l'état.

## Décompte

Bloquantes : 0. À corriger : 0. Mineures : 3 (A, B, C). La course de `banc_essaims_memes_poids_v2.py` peut partir selon l'accord de Lazar.
