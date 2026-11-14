# Passation du compte 4 — 2026-11-14T05:59:58Z

Écrite à 2026-11-14T05:59:58Z (heure relevée par `date -u`) par la session du compte 4 (`session_01Qi7Gr2uGzyVcw9VmDXgvEV`, modèle A), pendant l'autonomie accordée par Lazar jusqu'à 2026-11-14T10:49:43Z (C4-0023). Brief `docs/notes/plan-paquet-multi-comptes-v1/brief-compte-4-v1.md` (`d56b336f…`) ; plan `3b1bda25…`, lot « compte 4 ». Journaux provisoires : `registres-provisoires/compte-4-2026-11-13*.md` et `compte-4-2026-11-14*.md`, dernier `compte-4-2026-11-14-v14.md` (`e79c11094675f7c21351777af53882ed33876926368c3f7eb921ac77144b2559`, C4-0052). Modèles notés « A » (cette session et ses développeurs) et « B » (les lecteurs), R-2598. **Aucune dépense, aucune instance, aucune clé employée par ce compte.**

## Fait

- **Tâche 1, texte « validité de l'adaptateur »** : brouillon 5 `brouillons/validite-adaptateur-v1/validite-adaptateur-preenregistrement-v1-brouillon5.md` (`56fb63e9b2f4ae8cb8361e94568a99c4ddbdb219220670a7e05f004afdaead26`) ; couples du brouillon 6 prêts, **non appliqués** : `brouillons/validite-adaptateur-v1/candidat1-pieces/faire-couples-brouillon6-v1.py` (`f92c31c3…`, 14 couples A6-01 à A6-14, refuse tout commit autre que `c2fab6cc7267b76228a75dc3e2e08bc7aa038961`) ; pièce de confirmation des champs `confirmation-champs-t07-fusion-c2fab6cc-v2.md` (`321b169a…` ; la v1 fautive gardée).
- **Tâche 2, audit des fuites** : préparation rendue (C4-0015), auditeur non lancé.
- **Tâche 3, T0.8** : code **citable tel quel** au commit `453a71e1c6729d7ec5d43e3a4a0e3522dfd38579` (branche `prep/t08-code-compte4-v1`, poussée ; empreintes `brouillons/t08-code-compte4-v1/empreintes-code-t08-453a71e1-v1.md`, `797ac967…`) ; texte candidat **brouillon 7** `brouillons/T0.8-bases-boite-noire-v0-v1-brouillon7.md` (`1877e384…`), sept marqueurs restants dont `MOT_LAZAR_T5_19`.
- **Tâche 4, (ii-b)** : code au commit `3baecee7044f2f1701743dc307da9bdcb8fcf217` (branche `prep/iib-code-compte4-v1`, poussée ; rapport `95659307…`) ; contre-lecture 1 `brouillons/iib-code-compte4-v1/contre-lecture-1-code-iib-v1.md` (`a375c699…`) : « autorisable après les corrections listées », 1 bloquant, 6 majeurs, 11 mineurs ; corrections **arrêtées** sur un refus du classifieur (C4-0052), aucune faite.

## Reste

- **Tâche 1** : à l'annonce par la mère du remplacement de la ligne CODE-T07 (fusion `c2fab6cc`), appliquer `faire-couples-brouillon6-v1.py` (`python3 -I faire-couples-brouillon6-v1.py DATE HEURE COMMIT ANNONCE SORTIE`, puis `appliquer-couples-vadapt-v2.py` sur le brouillon 5), vérification courte par un lecteur neuf du modèle B qui n'est pas lecteur de P3-bis, puis rendre le candidat (cible `prereg/validite-adaptateur-v1.md`) à la mère. `<<COMMIT_C7_T07>>` reste jusque-là.
- **Tâche 3** : mot de Lazar sur T5-19 (options (a) garder, (b) retirer, code inchangé, (c) retirer et changer le code ; recommandation (a), confiance 0,7 ; pas de défaut) ; puis texte qui remplit `MOT_LAZAR_T5_19`, et une vérification courte du différentiel du brouillon 6 à ce texte. Points du code pour la mère : VCT8B-02 (une ligne CODE-T08 à deux commits passe), VCT8B-03 (passe à blanc sur le registre), forme des lignes CODE-T08 et SCELLEMENT-T08, passe à blanc sur le registre réel, l'instance doit cloner la branche du code ; questions Q-1, Q-2, Q-4, Q-C2, Q-C3, Q-C5, Q-C6.
- **Tâche 4** : décisions de la mère (C4-0050, C4-0052) : historique de la branche (options (a), (b), (c) de CLIIBC-01) ; chemin permis pour récrire les fichiers qui portent des fragments (`iib/jouet_v1.py`, `tests/test_iib_exclusion_v1.py`, `tests/test_iib_consigne_v1.py`) ; reprise ou non des corrections CLIIBC-02 à 18 ; puis vérification courte et note sur le devis ; à l'intégration : version neuve de `tests/test_cibles_invisibles_v3.py` (deux échecs neufs qui ne nomment que `iib/`). M7 non tranchée.

## Réserves

- **Fragments de la consigne privée du maître (ii-b)** poussés sur `prep/iib-code-compte4-v1` (commits `e70ab23e` à `3baecee7`) ; à la tête aussi, tant qu'aucune correction n'est faite. Ne pas intégrer cette branche avant la décision de la mère.
- **Refus du classifieur** (C4-0052) : non contourné ; aucune relance par ce compte.
- **Écarts de ce compte, déclarés** : identifiants de modèles écrits une fois au journal v11 (`d1784495…`, preuve de N-052) ; v1 de la vérification courte du brouillon 5 de T0.8 versée avant le rendu, avec des identifiants (gardée, la v3 `f788bb73…` fait foi) ; consigne du développeur de (ii-b) (`6912fa48…`) sans le motif de la garde des secrets du brief ; consigne des corrections de (ii-b) (`33c33ac1…`) qui omettait `tests/test_iib_consigne_v1.py`.
- **Écarts des agents, déclarés par eux** : le développeur de (ii-b), un `grep -rln` dans `src/controle_ia/` (noms de `t07/` affichés, non ouverts) ; le contre-lecteur 1 de (ii-b), un `grep -l -r` dans le seul dossier factice `essai/iib-jouet-compte4-v1/`.
- **Qui a lu quoi** (à porter par la mère) : consigne privée du maître de (ii-b) lue en entier par le développeur du code de (ii-b) (modèle A) et par le contre-lecteur 1 de ce code (modèle B) : jamais lecteurs des sondes de (ii-b) ; le développeur des corrections ne l'a pas ouverte. Lecteurs du code et des textes de T0.8 (contre-lecteur 1 du code, vérificateurs des corrections, vérificateurs des brouillons 5 et 6), tous modèle B : aucun fichier de T0.7 ni de P3-bis ouvert, selon leurs consignes et leurs rapports. Lecteurs de T0.7 scellé : C4-0003 et C4-0012.
- Mots de Lazar tapés dans ce compte : recopiés aux journaux (C4-0005, C4-0019, C4-0023), sans effet de nœud avant inscription par la mère.

## Prochaine action

Attendre la mère et Lazar : annonce CODE-T07 (tâche 1), mot sur T5-19 (tâche 3), décisions sur (ii-b) (tâche 4). Rien d'autre n'est en cours.

## Agents et instances actifs

- Agents : **aucun** (le dernier, développeur des corrections de (ii-b), s'est arrêté à 2026-11-14T05:5x sur le refus).
- Instances de calcul : **aucune** créée ni touchée par ce compte.
- Arbres de travail : `/home/user/t08-code-compte4-v1` (tête `453a71e1`, propre) ; `/home/user/iib-code-compte4-v1` (tête `3baecee7`, propre). Branche du lot : `lot/compte-4-v1`.
