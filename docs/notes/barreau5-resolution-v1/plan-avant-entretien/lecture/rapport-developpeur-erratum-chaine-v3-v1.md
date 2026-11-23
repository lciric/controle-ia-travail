# Rapport du développeur : code de l'erratum de chaîne de la relecture décisive du barreau 5 (commande v3, ouverture à noms suffixés v1) — v1

Écrit le 23 novembre 2026 vers 00:30Z par un développeur neuf (Claude Opus 5.5), sous-agent du conducteur `session_013QMayjM1PQPWkLifMw9HDR`. Consigne de nuit : effort minimal suffisant ; rien de payant ; rien poussé. Classe B (code).

Arbre de travail : `/home/user/controle-ia-travail/.claude/worktrees/agent-a89be1d2701a117b9`, branche locale `course/barreau5-commande-lecture-v3` (non poussée).

## Pièces lues

- Erratum v2 `erratum-chaine-relecture-decisive-b5f-v2.md`, branche `conducteur-b5f/lecture-v1` (tête `c11af597be3ac3aaefaac8fd9b011f6de5ed0c51`), en entier : sha256 `01298f0f73a731e6ee31e0e91b45367da75ba1bd2276ba5d041000b9f87da87b`, égale à son compagnon.
- Sa vérification `verification-corrections-erratum-chaine-b5f-v1.md`, en entier.
- Pour les renvois de la v2 (« essais du § 6.2 de la v1 », liste du § 5.4 de la v1) : les § 4.3, 5.4, 5.6, 6.1 à 6.3 de l'erratum v1.
- Le code des commits figé (`c76e79169`) et v2 (`5402367e`) : modules, lanceurs, amorce, essais. Aucune table, aucun sel, aucun score ; ni `donnees/*`, ni `formation-b5f/*`, ni `traces/*`, ni `diag/`, ni les verdicts, ni l'état, ni les décisions, ni les passations. Un essai d'extraire `donnees/…/taches-evaluation.json` du commit figé pour les essais a été refusé par le classifieur ; je ne l'ai pas contourné, et les essais de la relecture passent sans ce fichier.

## Le commit

- Commit v3 : `9e682f0e0359ddde31fdf1bf1eae4a9e1e2acb5b` ; parent : `5402367e5b62c8ac294c55d5cc0230ebdfbaa457` (commit v2).
- Il ajoute les sept fichiers de la liste fermée, tous en mode 100644, et ne modifie aucun fichier existant (`git diff --raw` : sept lignes « A »).

| Fichier | sha256 |
|---|---|
| `scripts/lancer_b5f_lecture_v3.sh` | `828c66842a7ac9f52583469d71d2a8e583e0c69ada50c050b74f53c21db6c497` |
| `scripts/lancer_b5f_ouverture_suffixes_v1.sh` | `041826419ef2c52ee2ed1ea9926a9778736fbffe57b579d66d63359883353561` |
| `src/controle_ia/barreau5_familles/commande_lecture_v3.py` | `95aeffeb98e3ecdb9e2a22eb383e5afb34999cd967365f6fe714b81175c1a7c1` |
| `src/controle_ia/barreau5_familles/ouverture_suffixes_v1.py` | `bcb49d05e92211f4df69a99ec732085c628d376ff13533ee062b8129964e3bb7` |
| `tests/test_amorce_b5f_lecture_identification_v1.py` | `5ac5a573c5b6f8f29e0d639ef8fa00cb6a2ffe86fc9eaf2da3b20d571b2b9e00` |
| `tests/test_commande_lecture_v3.py` | `2c1144ff7dd50571173b22df6c8552a4d2b1df7deeb5286fa93337cc747f8fc1` |
| `tests/test_ouverture_suffixes_v1.py` | `8d0b44005fdca6402e94c9d77a61395f39712270803e2231bfcd793c553f5a4f` |

Amorce embarquée recomposée : `amorce_corrigee(amorce figée 54a676f3…)` donne sha256 `0adb6efba0a430f11c30e01da52787ef0482e20f6d74f699dbe8d76d2d300001`, 33 536 octets, 405 lignes. C'est la valeur attendue. La seule différence est la ligne ajoutée après la l. 362.

## Ce que fait le code

- **Commande v3** : le corps de la commande v2, à deux remplacements près (essai de différence fermée). Le premier remplace (d), (b) et (c) par `commit_de_code_verifie`, qui enchaîne (d), (d'), (c'1), (c'2) et (b'). Le second embarque `amorce_corrigee(...)`. Seule entrée : « commande decisif ». Le lanceur imprime d'abord « B5F AMORCE EMBARQUÉE : sha256 … ». Il refuse aussi toute sortie qui n'a pas exactement un segment base64, ou dont le segment décodé n'est pas `0adb6efb…` (C12, vérifié aussi dans le module).
- **Ligne d'épinglage** (`commit_v3_epingle`) :
  - le format est celui du § 4.3 (d), à la lettre (ASCII, plus les lettres composées du texte) ;
  - une ligne est « candidate » si, une fois mise en forme composée, ses espaces ramenées à U+0020 et ses espaces de tête ôtées, elle commence par le préfixe ;
  - il faut une candidate et une seule, et elle doit égaler le format en colonne 1 ;
  - l'erratum, l'accord et la branche doivent égaler les constantes.
- **Ouverture à noms suffixés** : `variante`, `preparer`, `garde_d_ouverture` et `ouvrir` sont recomposés. Les essais d'égalité ligne à ligne vérifient les différences : une ligne insérée dans `preparer`, quatre blocs dans la garde, deux dans `ouvrir`. Les objets privés récrits à l'identique ont chacun un essai d'égalité.
- **Les trois précisions de la vérification, appliquées** :
  1. `code_au_commit_v3` lit `SCORES-B5F`, prend le registre du commit prouvé, puis rejoue (d), (d'), (c'1) (avec le commit de `CODE-LECTURE-B5F` du registre donné), (c'2) et (b') ;
  2. en (b), `a_garde_d_ouverture.code` vaut `{"commit", "arbre_gele": "égal hors des listes fermées de la v2 et de l'erratum", "commit_de_code", "erratum_sha256"}` ;
  3. la copie lue c(base) se calcule base par base : par `_familles_formees` (récrite à l'identique) dans `variante` et `preparer`, au champ « copie » du résumé contrôlé par `exiger_copie_lue` dans `ouvrir`, jamais à partir des graphies de la table.
- **Fichier de traduction** : `traduction-table-b5f.json`, scellé à côté du résultat. Il porte la traduction, E_a, E_b, l'engagement, les copies, `erratum_sha256` et la variante.

## Essais

**Écrits avant le code**, puis joués (`--tb=no -rN -q -p no:cacheprovider --basetemp=<bloc-notes>`).

**Sur le commit v3** : 552 passés et 1 sauté, en un seul passage. Le détail :

| Essais | Compte |
|---|---|
| commande v2 | 113 passés, 1 sauté |
| commande v3 | 77 |
| identification | 5 |
| ouverture | 100 |
| lecture | 102 |
| épreuve à vérité plantée | 155 |

**Arbre figé** (commit `c76e79169`, extrait par `git archive` dans le bloc-notes, sans `registres/` ni `donnees/`) :

| Essais | Compte |
|---|---|
| relecture | 24 passés, après ajout de `docs/sources/invites-2606.08892-v1`, dont l'absence faisait tomber 15 essais |
| lanceur v1 | 43 |
| engagement | 23 |
| amorce | 51 |
| amorce entière | 4 |

Facultatif non joué sur l'arbre figé : sondes 20. Lecture 102 est jouée sur le commit v3, où `lecture_v1.py` est identique.

**Amorce embarquée (C10)** : les 51 essais figés de l'amorce, joués sur une copie jetable où l'amorce est remplacée par l'amorce corrigée, donnent 51 passés. Le bloc « branche » rend `BRANCHE_SORTIE`.

**Identification (§ 6.1)** : `git http-backend` est servi par un serveur HTTP local à identification Basic. Les variables `GIT_*` et de mandataire sont retirées.
- L'amorce figée tombe : code 2, « commit des entrées … introuvable », « could not read Username » et « promisor remote », branche de sortie aux seules traces.
- R12 : l'amorce corrigée refuse avant tout clone des entrées.
- Garde neuve : un faux `git` refuse l'inscription ; arrêt au journal, aucune extraction.
- Cas sain : copie sous `traces/…`, suppression à tête vérifiée, puis l'amorce corrigée : entrées extraites, versement, preuve, témoin. `ligne_scores` figée accepte le commit prouvé, et le jeton n'est écrit nulle part.
- Témoins : 401 sans identification ; `remote.origin.promisor` présent même dans l'échec.

**Mutations attrapées : 15 sur 15**, chacune rendant au moins un essai rouge (script `mutations.py` du bloc-notes ; chaque fichier est rendu à l'octet) :
1. traduire avant l'engagement ;
2. tirer c(base) de la table, côté `_familles_formees` ;
3. tirer c(base) de la table, côté résumé de `ouvrir`. Elle n'était d'abord pas attrapée ; un essai de table mélangée dans `ouvrir` a été ajouté avant le commit ;
4. admettre deux graphies ;
5. oublier `-r1` ;
6. jouer la cohérence sur T_nu ;
7. épinglage : espace initiale admise ;
8. épinglage : deux lignes admises ;
9. (c'2) : mode non vérifié ;
10. (c'1) omise ;
11. (b') omise ;
12. amorce figée embarquée ;
13. condition C12 du lanceur retirée ;
14. ligne ajoutée retirée de l'amorce ;
15. ligne placée après l'extraction.

## Écarts et réserves

1. **Parité (§ 5.6)** : par défaut, sur un échantillon fixé de 39 mondes (les deux premiers de chaque groupe et les neuf de V7) ; sur les 7 269 mondes si `B5F_PARITE_TOUS=1` (environ trois heures, non joué). Les 39 passent : égalité exacte, ou à 10⁻¹² relatif pour les réels ; refus des deux côtés pour les artefacts de table.
2. **Jumeau suffixé** : `T03-x1`, `T04-x1-r1` et `T05-r1`. Il y a donc deux familles retirées, pas une, pour couvrir les trois graphies. La table engagée du jumeau est recalculée depuis `planter` de la fabrique figée.
3. **Réemplois déclarés** :
   - les faux outils de l'essai à blanc, importés ; la fausse marche à une ligne près (inventaire rempli) ;
   - le montage figé de `preparer` (`_branche_de_formation`, `registre`) ;
   - les aides du monde git de la commande v2.
4. **Doublon après traduction** : il n'est pas atteignable par une table cohérente, parce que deux graphies sont refusées avant. Il est éprouvé sur la garde de ligne elle-même (`exiger_lignes_du_plan`).
5. **Branche** : le commit est local, sur `course/barreau5-commande-lecture-v3`. L'erratum proposait `commande-b5f/lecture-v3` pour la poussée, que je ne fais pas.
6. **Le présent rapport** n'est pas dans le commit v3, pour que la liste fermée reste à sept fichiers ; il est scellé dans l'arbre de travail, non suivi.
7. **Exclusions** : je suis dans les exclusions du point 7 (a). Je ne tiens ni l'ouvreur ni le juge.
