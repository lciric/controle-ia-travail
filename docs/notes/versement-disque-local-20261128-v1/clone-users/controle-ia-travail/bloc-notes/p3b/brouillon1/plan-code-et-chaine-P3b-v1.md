# Plan du code et de la chaîne de P3b — v1

- Rédacteur neuf (Claude), brouillon 1, 2026-10-20 vers 23:50 UTC. Joint à `P3b-seconde-lecture-v1-brouillon1.md` (même
  dossier). Plan seulement : aucun code n'est écrit ici. `…/` = `/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad`.
- Règle : tout le code neuf vit **hors de l'arbre gelé**, sous `docs/procedures/P3b-v1/` (modules, tests, scripts de la chaîne,
  journaux de preuve). Il **importe** les modules gelés de P3 au commit `7a54d43` sans les copier ni les modifier
  (`premier_test_ia.conditions`, `.notation`, `.statistiques`, `.lecture` pour `etat_du_jeu`, `etats_des_jeux`,
  `_permuter_dans_les_taches`, `descriptif` ; `harnais.episode` ; `harnais.activations.passe_unique` ; `harnais.validation_reelle`
  pour les gardes du mode décisif ; `sondes.evaluation`, `sondes.temoins.difference_aires_appariee` ; `manifeste` ;
  `scellement` ; `premier_test_ia.figees.lire_sondes`). Garde : `git diff --quiet 7a54d43 -- <chemins gelés>` exigé par les
  contrôles avant dépense et par le module de passe.
- Chaque garde d'arrêt a un test sur un cas sain **et** sur un artefact (R5). Python lancé avec `-I -B` par les scripts.
- Réutilisation : si le module v3 de P4 contient déjà une reconstitution des épisodes de P3 (il lit les actions honnêtes de
  P3), la reprendre par import, telle quelle, après vérification (Q-09). Ce rédacteur n'a pas lu ce module.

## 1. Modules (sous `docs/procedures/P3b-v1/`)

| module | rôle | gardes et points testés |
|---|---|---|
| `p3b_constantes_v1.py` | constantes gelées : bandes (1-7, 8-20, 21-32), grille λ, tailles (200 planchers, 200 répliques, 200 rotations, 2 000 tirages), seuils (10⁻³, 10 %, 5 points, 20 actions, 0,75, 90 %), fenêtre W (16 jetons), clés de graines, noms des fichiers d'entrée et de sortie | relues contre la configuration scellée ; toute constante différente : arrêt |
| `partition_p3b_v1.py` | partition (A) ou (B), plis de découverte (5 × 4) et de confirmation (5 × 8) | couvre exactement les 60 tâches ; blocs disjoints ; même entropie → même partition ; (B) : un chargeur filtré refuse toute tâche réservée (artefact : demande d'une tâche réservée → arrêt) |
| `donnees_p3b_v1.py` | chargement des fichiers gardés de P3 (textes, scores, scores par jeton, fiches, sondes légères par `lire_sondes`), empreintes exigées, table des actions (épisode, pas) ; textes tenus en mémoire, jamais écrits ni affichés | empreinte autre → arrêt (R11) ; clé manquante ou forme autre → arrêt ; sondes principales du fichier des scores par jeton = celles de `sondes-figees.json` |
| `reconstitution_p3b_v1.py` | reconstruction des transcriptions (environnement de la condition, consignes chargées par le code, format de l'agent, contexte par pas, tokenisation canonique, jeton de fin, clôture) ; passe unique ; gardes (a) à (e) par action ; empreinte de trajectoire comparée à la fiche | cas sain : épisodes jouets joués par `jouer_episodes` gelé, gardés comme P3, puis reconstitués → toutes les actions valides et empreintes égales ; artefacts : un caractère changé dans un texte ; jeton de fin autre ; condition échangée ; score gardé perturbé au-delà de 10⁻³ ; borne de champ décalée ; tokenisation non canonique simulée (identifiants gardés coupés autrement) → action exclue, motif juste ; seuils de 10 % et de 5 points (juste en dessous, juste au-dessus) |
| `positions_p3b_v1.py` | c, premier chiffre, t_cost, W (16 jetons au plus), champ entier, avant le champ ; vocabulaire V_num ; nombres écrits avant le champ (compte seul) | textes synthétiques : « COST: 120 GPU-hours », « **COST:** 1,200 », « COST: approx. 3 x 400 », champ sans chiffre, chiffres dans le titre, clé vide puis pleine (règle de `bornes_champs`), t_cost < c → exclue ; V_num : compte et règle relus sur le tokeniseur figé ; aucune retokenisation d'un rendu |
| `scores_localises_p3b_v1.py` | scores par jeton des sondes principales et des 400 sondes de plancher (vectorisés par couche, comme `Notation`), agrégation de production restreinte à W, au champ, avant le champ ; valeur à t_cost | égalité avec `agreger_par_jeton` gelé sur données aléatoires (10⁻¹²) ; garde « jamais moyenne ni médiane » : une agrégation par moyenne injectée → arrêt ; sonde principale de Mahalanobis : scores gardés de P3 utilisés, test dédié |
| `oracle_p3b_v1.py` | réduction par les statistiques de la découverte ; noyaux par bande ; ridge à noyau pondérée, solution exacte en double précision ; choix sur la découverte ; validation croisée par tâche sur la confirmation ; 200 répliques du plancher (conditions permutées dans chaque tâche, chaîne entière refaite) | signal planté (contrôle positif jouet) → au-dessus du plancher ; données nulles → non au-dessus dans au moins 90 % de 100 essais jouets ; **étanchéité** : permuter les étiquettes du pli k ne change pas les scores hors pli du pli k ; mention jamais dans un apprentissage (artefact : mention injectée → arrêt) ; même entropie → mêmes scores au bit près sur processeur ; système non résoluble → échec écrit |
| `residuel_p3b_v1.py` | régression croisée de T4 résiduel sur [1, c_w, c_w², h_t, k, e, e · m], plis de la confirmation | dépendance plantée au coût → aire du résidu ≈ 0,5 ; étanchéité de l'ajustement croisé ; covariables manquantes → « non calculable », jamais un remplissage silencieux |
| `lentille_p3b_v1.py` | lentille des logits (normalisation finale, lignes de W_U) ; lentille jacobienne (chargeur empreinté, format écrit) ; H_t, leurres, préférences q, π_b, Δ_b ; rotations à covariance égale ; permutation ; items du contrôle positif et leur lecture | identité à la dernière couche (modèle jouet) et artefact (normalisation retirée → garde violée) ; rotation : covariance gardée à 10⁻⁸ sur données synthétiques ; leurres : règle de grandeur et d'identifiant distinct, exclusion sans leurre ; contrôle positif jouet (direction des nombres plantée) : passe ; artefact (états d'autres items) : ne passe pas ; fichier jacobien d'empreinte autre → bras retiré, motif écrit |
| `passe_p3b_v1.py` | module de l'instance (sur le modèle de `premier_test_ia/run.py`) : manifeste (préenregistrement scellé exigé en mode réel), étapes 2.1 à 2.9 du texte, lignes `PROGRES` sans texte, `arret.json` scellé à tout arrêt, résumé ; mode jouet (modèle jouet, tokeniseur par caractères, textes synthétiques) | durée relue (épisode, réplique, couche) ; budget dépassé en jouet → arrêt consigné ; aucune activation dans les fichiers écrits hors du dossier local de l'instance ; ordre des étapes (contrôle positif avant toute passe sur P3) |
| `lecture_p3b_v1.py` | lecture sur processeur : P3b-P0, famille principale, placebo, audit R4, états des jeux, P3-P4, T1, T3, T4 résiduel, T4 de P3, contrôle positif, double comptabilité, descriptives, lignes des tables (préalable, G1 à G7, O1 à O7, D0 à D5, synthèse) | gardes du mode décisif (entropie, code cité et importé, run de passe décisif sous ce texte, configuration citée), chacune avec cas sain et artefact ; **chaque ligne de chaque table atteinte** par des entrées synthétiques ; descriptive en échec écrite sans bloquer ; règle RC-01 des jeux non interprétables |
| `controle_fichiers_p3b_v1.py` | contrôle des fichiers avant toute poussée et à la récupération : aucun axe de longueur 4 096, aucune fenêtre de 48 caractères d'un texte d'action (fenêtres glissantes au pas de 16, formes brute et échappée, comme RC-donnees-01 de P4), aucune chaîne canari, taille totale au plus 100 Mo, schéma fermé des tableaux | cas sain ; artefacts : tableau d'activations (n, 4 096) ; texte échappé dans une chaîne JSON ; canari dans un journal ; tableau à clé inconnue |

Tests : `docs/procedures/P3b-v1/tests/`, lancés explicitement (`python -I -B -m pytest -q docs/procedures/P3b-v1/tests`) en plus de la
suite du dépôt ; leur nombre et celui de la suite complète au commit S donnent « Tests attendus ».

## 2. Fichiers de sortie de la passe (tous scellés, poussés vers `calcul/p3b-v1`)

`donnees/<run>/` : `partition-p3b.json` ; `reconstitution-p3b.npz` (statut et motif par action, écarts maximaux, empreintes des
transcriptions reconstituées) ; `positions-p3b.npz` ; `scores-localises-p3b.npz` (2 + 400 sondes × 4 positions × actions) ;
`oracle-p3b.npz` (table de la grille, réglage choisi, scores hors pli, 200 × scores hors pli des répliques, réglages choisis
des répliques) ; `lentille-p3b.npz` (par action et par couche : logits de τ_h, τ_d, τ_w, rangs sur V_num ; préférences des
200 rotations en entiers 8 bits ; identité de la dernière couche) ; `cp-lentille-p3b.npz` ; `diag/<run>/` : manifeste,
résultats, résumé. Aucune activation, aucun texte. Sur le disque de l'instance seulement : `etats-tcost-p3b.npy` (2 400 × 32
× 4 096, simple précision, ≈ 1,3 Go), scellé, détruit avec l'instance.

## 3. Chaîne de lancement (déclinée de la chaîne v2 de P4)

Base : `…/p4-instrument/chaine-v2/` (`NOTES-CHAINE-v2.md`, `1691bf25…`), mêmes rôles, mêmes formes, noms en `_p3b_v1`.

| script | reprend de P4 v2 | ce qui change pour P3b |
|---|---|---|
| `verifications_p3b_v1.py` (module commun) | `verifications_p4_v1.py` : GO et révocations voisines (normalisation, frontières de mot), forme de la ligne d'accord, somme des dépenses, noms des rapports, fenêtres de texte, schémas fermés, montrer sans texte | schéma des tableaux de P3b ; empreintes des fichiers d'entrée de P3 ; partition |
| `controles_avant_depense_p3b_v1.sh` | contrôles de P4 : chemins gelés lus dans `7a54d43` par `git show`, garde de calcul rejouée et son empreinte, suite des tests, tokeniseur versé | empreintes des données de P3 et de la lentille jacobienne ; constantes de durée (7 200 s, 150 et 210 minutes, 14 400 s) reliées au texte ; partition recalculée |
| `lancer_p3b_v1.sh` | lanceur de P4 : offre conforme la moins chère, crédit exigé, marqueur « un accord, un lancement », `lancement.txt` relu | étiquette « p3b-v1 » ; borne 7,5 USD ; crédit 4,5 h × prix + 1,2 USD |
| `amorce_instance_p3b_v1.sh`, `p3b_instance_v1.sh` | amorce et script de l'instance de P4 | récupération des fichiers d'entrée de P3 (branche de P3 ou copie au commit S, Q-10) ; téléchargement empreinté de la lentille jacobienne ; poussée après `controle_fichiers_p3b_v1.py` |
| `surveiller_p3b_v1.sh`, `controle_cinq_minutes_p3b_v1.sh`, `arreter_p3b_v1.sh` | arrêt par identifiant, étiquette relue entière, état relu arrêté deux fois, codes 1 à 3 | aucune |
| `recuperation_p3b_v1.sh`, `controler_traces_p3b_v1.sh` | récupération (aucune destruction en échec, heure limite écrite), contrôle des traces (comptes seuls) | contrôle des fichiers de P3b ; destruction par identifiant après récupération conforme |
| `sceller_p3b_v1.sh` | scellement de P4 : relit les journaux de preuve, compare chaque script éprouvé à sa copie versée | candidat de P3b, configuration, sceaux |
| `repetition_jouet_p3b_v1.sh`, `repetition_finale_p3b_v1.sh` | répétitions de P4 (passage d'arrêt par échéance compris) | textes synthétiques porteurs d'une **chaîne canari** ; un passage où une activation est glissée dans un fichier à pousser (refus attendu) |
| `essais_*_p3b_v1.sh`, `outils_essais_p3b_v1.py` | bancs de P4 (cas sain et artefacts) | cas propres à P3b ci-dessus |

## 4. Ordre de travail proposé

1. Contre-lecture R2 du brouillon, du devis et de ce plan par un sous-agent neuf (fichiers donnés explicitement) ; traitement.
2. Décisions en attente : P-016 (partition), nœud « revendication » (lecture en diagnostic), Q-03 (comptes de tokenisation).
3. Modules et tests (un rédacteur neuf), puis vérification neuve du code.
4. Mesures de conception M-P3b-1 (puissance) et, si admise, M-P3b-2 (comptes de tokenisation) ; sorties brutes scellées.
5. Candidat (valeurs `<<…>>` remplies, partition gardée seule), relecture courte ; chaîne et bancs ; répétitions ; scellement.
6. Ligne d'accord ; lancement ; surveillance ; récupération ; contrôle des traces ; destruction ; lecture ; verdict R13.
