# Rapport du développeur — véhicule NA-1, lot 6 v3 (type exact du journal de la colonne, couverture, sorties en v3) — v1

- Développeur du lot 6 v2 du véhicule NA-1 (modèle O), qui reprend son paquet en v3 sur la vérification S du lot 6 v2 (« À corriger ») et sur les décisions de la mère relayées par la coordination (18:59Z, GO-2026-11-21-69). Je n'ai écrit ni le lot 6 v1, ni les lots 1 à 5 et 10 a, ni la conception, ni la vérification.
- Date (UTC) : 2026-11-21, après 19:28Z.
- Processeur seul : aucun appel à un fournisseur, aucune clé, aucune dépense, aucun commit, aucune écriture dans un dépôt, aucune attache de dépôt. Rien ouvert sous `additif-matiere-premiere-v1/`, `archives-reponses-modeles/`, `/root/.claude/` ; aucune branche de quarantaine ni de matière première. Le dossier parent `docs/notes/ideation-nouvelles-attaques-v1/` n'a pas été listé ; chaque dossier de lot ouvert par son chemin complet. Données factices seules.
- Mot de Lazar (GO-2026-11-21-74), « tous de faux positifs je confirme » : lu. **Aucune coupure de classifieur, aucun refus de permission ni de garde.**

## 1. Verdict

- **Les quatre points de la mère sont portés.** (1) Type exact : en états 1 et 2, sous-classe, classe falsifiée par `__class__`, imitation sans héritage et envoi surchargé sont refusés par l'arrêt nommé ; la ligne plantée ne part pas ; état 0 inchangé ; rétablir `isinstance` (N18) est tué. (2) V8 et V10 ont leur essai, leurs mutations sont tuées (N21, N22) ; W1 dit au § 3, non retiré. (3) Sorties en v3 (`journal-arrets-et-generations-na-v3.jsonl`, `bilan-course-na-v3.json`), formats du § 6 mis à jour. (4) E-1, R3, R4, R5 : pris acte (§ 7), non codés.
- **Essais du lot 6 v3 seuls : 127 passés, 14 sous-essais passés, 0 échec** (`journal-essais-na-lot-6-v3.txt`) : course 54, arrêts 44, câblage 29 (les 116 du v2, plus 11 neufs).
- **Chaîne entière sur copie neuve** (v68, lots 2 v5, 3 v3, 4 v1, 5 v1, 10 a, puis le paquet v3 par mon programme, `--lancer-essais`) : **770 passés, 92 sous-essais passés, 0 échec** (= 759 du v2 + 11 ; 78 + 14 sous-essais).
- **Mutations : 57 tuées sur 57** sur la copie d'application (`journal-mutations-na-lot-6-v3.json`) : M01 à M34 (v1), N01 à N17 (v2), N18 à N23 (v3) ; T0 passe, T1 survit, aucune invalide.
- Programme d'application : cas sain ; cinq refus éprouvés (§ 5).

## 2. Pièces lues

| pièce | empreinte |
|---|---|
| vérification du lot 6 v2 (`lot-6-vehicule-na-v2/verification-v1/verification-lot-6-na-v2-v1.md`) | voir § 9 |
| sondes du vérificateur : `sondes/sonde_cablage.py`, `sondes/mes_mutations.py` | voir § 9 |
| mon lot 6 v2 (rapport `27356cd0…`, table `0e318355…`, paquet) | dossier `dev-vehicule-na-lot-6-v2/` |
| mot de la coordination (décisions de la mère, 18:59Z) | message à la session, non versé en pièce ; repris ici point par point (§ 3) |
| base v68 : pièces tirées d'`origin/main` au lot 6 v2 (manifeste `4ed9fd8e…`, programme `9b6e6843…`), reprises par copie | égales à leurs compagnons |

## 3. Ce que la v3 porte (décisions de la mère, point par point)

Module `paquet/orchestrator/pole/course_na_v3.py` (noté C3) ; lanceur `demonstrations/lancer_orchestrateur_na_v3.py` (L3).

| point | décision | code | épreuves |
|---|---|---|---|
| 1 | type exact à la place d'`isinstance` : une sous-classe du journal de la colonne ne compte pas ; une classe falsifiée (`__class__`) et une surcharge de `journaliser_envoi` sont refusées | C3:188 (`type(journal) is not mp.JournalRequetesColonneNA` : `type()` lit la classe réelle, non l'attribut `__class__`) ; C3:193 et C3:194 (envoi remplacé sur la classe depuis l'import, ou posé sur l'instance) ; référence relevée à l'import C3:96 | `TestCablageJournauxHostiles` (sondes S0 à S6 du vérificateur reprises, plus une sous-classe muette et un envoi posé sur l'instance) ; mutations N18, N19, N20 |
| 2 | essai de la valeur « au coffre par refus du portier » de la ligne (V8) | ligne C3:651 (inchangée) | `TestRefusEcrits::test_au_coffre_par_refus_du_portier_porte_a_la_ligne_de_generation` ; mutation N21 (= V8) |
| 2 | essai du refus de sceau du journal de la génération 1 (V10) | C3:787 à C3:796 (inchangé) | `TestRefusDeSceauDuJournalG1` ; mutation N22 (= V10) |
| 2 | garde redondante de `configuration_course_na_v1.py` l. 300-301 (W1) | non retirée (fichier inchangé depuis le v1) | voir ci-dessous |
| 3 | R12 vaut pour les sorties | C3:100, C3:101 ; version du journal C3:279 ; version de la course C3:92 | `TestTroisGenerations::test_noms_de_sortie_en_v3` ; mutation N23 |
| 4 | E-1 accepté ; R3 et R5 au lot 8, R4 à l'additif | non codés | § 7 |

**W1, dit sans retrait.** `configuration_course_na_v1.py` l. 300-301 (`if t.marque != rt.MARQUE_COURSE: raise rt.TableRefusee(…)`) **ne décide rien** : la ligne 299 appelle `rt.lire_table(octets, p.sha256, rt.MARQUE_COURSE, p.nom)`, qui refuse déjà toute table d'une autre marque (`routage_na_v1.py` l. 229-230, du lot 4, figé). La condition de la l. 300 ne peut donc jamais être vraie ; la mutation W1 du vérificateur (qui la retire) survit pour cette raison. Le fichier est gardé à l'octet du v1 (`02644792…`), la garde E7 effective est celle du lot 4. Ma citation « F:294 » du rapport v2 visait cette garde redondante ; la garde qui décide est `routage_na_v1.py` l. 229-230.

**Ce que le refus regarde, en état 1 ou 2, dans l'ordre** (C3:173 `refuser_cablage`) : l'état est un entier 0, 1 ou 2 ; l'objet est un journal du lot 3 (`isinstance(…, jn.JournalRequetes)`, comme le contexte du lot 4, inchangé du v2 et seul contrôle en état 0) ; **type exact** du journal de la colonne ; envoi non surchargé (classe, instance) ; contrôle de départ du même état, colonne chargée (renforcement E-1, accepté). En état 0, rien de plus que le v2 (« état 0 inchangé »).

Ce qui ne change pas : refus au départ (C3:722, C3:723) et à la construction (C3:355) ; l'arrêt nommé `ArretCablageColonneNA` (C3:157), numéro à l'additif, aux arrêts connus (C3:244) ; la fabrique pour le lanceur (C3:204) ; le lanceur (L3:126, L3:156, L3:157).

## 4. Exigences du lot 6 (v1 et v2) et lieux

Le reste du code est celui du v2, aux mêmes fonctions (décalage de lignes seulement) : classe C3:339 ; `fournisseurs_requis` ; proposition, aiguillage (E4), surcharge de `juger` (A17, identifiants réencodés, A2) ; refus écrits et garde de remplacement ; étapes neutralisées ; course C3:669 ; ligne de la génération C3:630 (E6) ; journal des arrêts C3:273 (E5) ; F (inchangé) : régime, gardes héritées, copie par génération, n° 14 ; S (inchangé) : E8. Le tableau complet est celui du rapport v2, § 4 (`27356cd0…`), lu avec ce décalage.

## 5. Essais et mutations

**Commandes** (`TMPDIR` posé dans mon dossier avant le premier essai ; une commande simple par appel) :
1. `python3 -B pieces-origin-main/v68/appliquer_paquet_orchestrateur_v68_v1.py --source /home/user/lciric/ideation-organism --destination application` : conforme (commit `a41b7b50…`).
2. Programmes des lots 2 v5, 3 v3, 4 v1, 5 v1, 10 a sur `application` : 17, 6, 9, 12, 4 fichiers, aucun refus.
3. Développement sur `travail/` (copie de `application`) : 127 passés ; mutations de brouillon : 59 jouées, 55 tuées, **N01 et N13 invalides** (leur texte cherché était la ligne `isinstance` remplacée) ; recibles sur le texte v3, rejouées seules : tuées. Puis le manifeste (`20c4065c…`, 11 fichiers, 56 dépendances).
4. `env TMPDIR=… NA_LISTE_REELLE_DEPOT=/home/user/controle-ia-travail …/python -B appliquer_paquet_vehicule_na_lot_6_v3.py --destination application --lancer-essais` : 11 fichiers, **770 passés, 92 sous-essais**.
5. `pytest -v` des trois fichiers du lot 6 v3 dans la copie : **127 passés, 14 sous-essais**.
6. `mutations_na_lot6_v3.py --racine application/orchestrator --journal journal-mutations-na-lot-6-v3.json` : **59 jouées, 57 tuées**, T0 passe, T1 survit.
7. Refus du programme d'application (code 2, rien copié) : seconde application (R12) ; `/home/user/orchestrateur-a41b7b50` ; le paquet ; une copie sans le lot 10 a (`dev-vehicule-na-lot-6-v2/copie-nue`, « `matiere_premiere_na_v1.py` ») ; paquet altéré d'une ligne (copie sous `tmp/`).

**Essais neufs en v3 (11)** :

| essai | cas sain | artefact |
|---|---|---|
| `TestCablageJournauxHostiles::test_hostiles_refuses_aux_etats_1_et_2` (12 sous-essais) | — | états 1 et 2 × S1 (sous-classe qui surcharge l'envoi), sous-classe muette, S2 (imitateur plat), S3 (`__class__` falsifiée), S4 (sous-classe du lot 3, départ juste), envoi posé sur l'instance : `ArretCablageColonneNA` au départ, ligne d'arrêt nommée, aucun appel, aucune génération |
| `…::test_imitateur_de_classe_cause_type_exact` | — | cause « type exact » ; `type_journal` = classe réelle (`ImitateurClasse`) |
| `…::test_envoi_remplace_sur_l_instance_cause_surcharge` | — | cause « surchargé » |
| `…::test_envoi_remplace_sur_la_classe_refuse` | classe restaurée : reçu | envoi de la classe remplacé : refus « surchargé » |
| `…::test_temoin_s0_journal_exact_la_garde_arrete_la_ligne` | S0 : journal exact, la garde de la colonne arrête la ligne plantée | — |
| `…::test_etat_2_journal_exact_depart` | état 2, journal exact : trois générations | — |
| `…::test_etat_0_inchange_s5_s6` (2 sous-essais) | état 0 : S5 journal ordinaire, S6 sous-classe qui surcharge l'envoi : trois générations | — |
| `TestRefusDeSceauDuJournalG1::test_sceau_refuse_dit_a_la_ligne_d_arret` (V10) | — | journal g1 altéré avant le refus : `journal_requetes_g1 = "scellement refusé (JournalReecrit)"` à la ligne d'arrêt et au bilan |
| `…::test_sans_alteration_la_cle_est_absente` | clé absente | — |
| `TestRefusEcrits::test_au_coffre_par_refus_du_portier_porte_a_la_ligne_de_generation` (V8) | un refus écrit du portier sur quatre fiches : la ligne porte 1 (égal au portier), puis 0, 0 ; la course continue | — |
| `TestTroisGenerations::test_noms_de_sortie_en_v3` | fichiers en `-na-v3`, versions `course-na-v3` | aucun nom de sortie en `-na-v1.` ou `-na-v2.` |

**Mutations neuves en v3** : N18 (`isinstance` rétabli) tuée par les hostiles ; N19 (envoi posé sur l'instance admis) ; N20 (envoi de la classe remplacé admis) ; N21 (= V8, valeur à 0) ; N22 (= V10, refus de sceau tu) ; N23 (nom du journal des arrêts revenu au v1) : toutes tuées. N01 et N13 reciblées sur le texte v3 (voir commande 3).

Les sondes et mutations du vérificateur importent `course_na_v2` et `aides_na_lot6_v2` : non rejouées telles quelles ; leurs cas S0 à S6, V8, V10, V13 (= N18) sont repris.

## 6. Formats pour les lots 7, 8 et 10 a (mis à jour en v3)

**Ce qui change par rapport au v2 :** les noms des deux fichiers de la course et deux champs `version`. Rien d'autre.

| objet | v2 | v3 |
|---|---|---|
| journal des arrêts et des générations | `journal-arrets-et-generations-na-v1.jsonl` | **`journal-arrets-et-generations-na-v3.jsonl`** (+ `.sha256`) ; champ `version` des lignes de la classe d'ajout seul : `journal-arrets-et-generations-na-v3` |
| bilan | `bilan-course-na-v1.json` | **`bilan-course-na-v3.json`** ; `version` : `course-na-v3` |
| ligne `départ` | `depart.version` = `course-na-v2` | `depart.version` = `course-na-v3` |
| journaux des requêtes | `journaux/journal-requetes-g<g>.jsonl` | inchangé (fichiers du lot 3 v3, nommés par la course ; format du lot 3) |
| dossiers de génération | `generation-<g>/…` | inchangé (noms de la v68 et des lots 5) |

Le lot 7 lit les deux fichiers par `course_na_v3.NOM_JOURNAL_ARRETS` et `course_na_v3.NOM_BILAN`, et le journal par `course_na_v3.lire_journal_arrets_generations(chemin, exiger_sceau=True)`.

**Journal des arrêts et des générations** : champs permis `evenement`, `generation`, `depart`, `copies`, `arret`, `ligne`, `cles`, `cloture` ; événements, liste fermée, dans cet ordre : `départ` (`version`, `regime`, `gardes_heritees`, `plafond_course_usd`, `empreintes`, `statut_des_valeurs`, `go`, `etat_colonne`) ; `copies de configuration` ({"1","2","3"} → sha256) ; par génération complète `génération` (`ligne`) puis `cumul par clé` (`cumul`, `cause_non_etablie_par_cle`, `etat_relais_illisible_par_cle`) ; au plus un `arrêt` (`type`, `numero`, `nom`, et sans contenu : `role`, `cle`, `piece`, `generation`, `etape`, `clause`, `famille`, `rang`, `cause`, `n`, `moment`, `etat_colonne`, `type_journal`, puis `poste`, `motif`, `journal_requetes_g1`) ; `clôture` (`generations_completes`, `arret`) ; sceau. `type_journal` est le nom de la classe **réelle** du journal (`type(…).__name__`), jamais ce que dit `__class__`.

**Ligne de la génération** (C3:630, inchangée du v2) : `generation`, `cases_servies`, `copie_configuration_sha256`, `registre_servi`, `comptes_melange_lot_4`, `comptes_portier_lot_5`, `comptes_journal_lot_3`, `comptes_envois_lot_4`, `comptes_lot_6`, `au_coffre_par_refus_du_portier` (à part, égal à `comptes_portier_lot_5["au_coffre_par_refus_du_portier"]`, désormais éprouvé), `arrets_consignes`, `coffre`, `etapes`, `cout_generation_usd`, `cout_par_role_usd`, `cout_par_adaptateur_usd`, `memoire`, `journal_requetes_sha256`, `noeud`.

**Bilan** : `version`, `regime`, `go`, `generations`, `arret`, `signaux`, `budget_course`, `statut_des_valeurs`.

**Lot 8** : `depart = mp.preparer_depart(…)`, puis `lancer_orchestrateur_na_v3.principal(argv, depart_colonne=depart)` ; la course reçoit `etat_colonne=depart.etat` et `fabrique_journal=course_na_v3.fabrique_journal_colonne(depart)`. Toute autre fabrique doit rendre, en état 1 ou 2, un `JournalRequetesColonneNA` de type exact, non modifié. **À la charge du lot 8 (décision de la mère)** : R3 (porter `comptes_colonne` où il faut) et R5 (brancher `mp.garder_registre_servi` et le contrôle des pièces fixes à la génération 2, par `gardes_depart_en_plus`).

**Lot 10 a** : interfaces lues inchangées (`DepartColonne`, `Colonne`, `JournalRequetesColonneNA` et sa méthode `journaliser_envoi` telle qu'elle est définie dans la classe, `ArretColonneNA`, `GenerationRefuseeColonneNA`, `RefusColonneNA`, `ARRET_COLONNE`, états). Le lot 6 v3 exige désormais que la classe ne soit pas dérivée : si le lot 10 a voulait un jour une sous-classe, ce refus la refuserait.

## 7. Écarts et remarques

**Décisions de la mère, prises acte :**
- E-1 (renforcement : journal de la colonne d'un autre état refusé) : **accepté** ; gardé tel quel.
- E-6 (noms de sortie v1) : **levé** ; sorties en v3 (point 3).
- R3 (`comptes_colonne` non porté à la ligne) et R5 (tenue (iii) et pièces fixes non branchées) : **au lot 8** ; non codés ici.
- R4 (la garde de la colonne arrête toute la course à la première ligne égale) : **à l'additif** ; non codé.

**Mes écarts v3 :**
- F-1. Le refus d'une surcharge de l'envoi va un peu au-delà du « type exact » : avec le type exact, une surcharge par sous-classe est déjà refusée ; je refuse en plus un envoi posé sur l'instance (`vars(journal)`) et un envoi de la classe remplacé depuis l'import du module (C3:96, C3:193). Limite : une classe modifiée **avant** l'import de `course_na_v3` ne se voit pas (la référence est relevée à l'import) ; un remplacement de `jn.JournalRequetes.journaliser_envoi` (classe mère, appelée par `super()`) ne se voit pas non plus. Non éprouvés comme « refusés » : ils ne le sont pas ; dit ici.
- F-2. Le journal reste un objet mutable : le contrôle a lieu au départ et à la construction, non à chaque envoi (constat du vérificateur, § 6 de sa pièce). Non changé : hors de la décision.
- F-3. Les pièces v68 sont reprises par copie de mon dossier v2 (où elles avaient été tirées d'`origin/main` par `git show … >`), empreintes égales aux compagnons d'`origin/main`.
- F-4. Deux sorties trop longues ont été rangées d'office par l'outil sous `/root/.claude/…/tool-results/` : un `diff -rq` au lot 6 v2 (E-10 du v2), et, en v3, une recherche de « v2 » lancée par erreur sur tout mon dossier (copie d'application comprise). Ni l'une ni l'autre ouverte ; la recherche refaite sur le paquet seul.
- F-5. Le fichier d'essais du câblage porte en v3 les sondes du vérificateur réécrites en essais (mêmes classes hostiles, mêmes cas), non son fichier lui-même.
- Repris du v2, sans changement : E-2 à E-5, E-7, E-9, E-11, V1-1 à V1-7 (rapport v2, § 7).

**Remarques restantes :** R1 (numéro de l'arrêt à l'additif) ; R2 (état 0 : tout journal du lot 3 reçu) ; R6 (`ContexteGenerationNA.etat_colonne` sans défaut).

## 8. Relevé de méthode

**Chaîne de raisonnement.**
1. La vérification du lot 6 v2 (`e8992a54…`, § 2, question 1) montre que `isinstance` (C2:179) laisse passer, aux états 1 et 2, une sous-classe qui surcharge l'envoi (S1, S1b) et un objet qui falsifie `__class__` (S3, S3b) : la ligne plantée part. Sa mutation V13 (type exact) laisse tous mes essais v2 au vert : aucun essai ne séparait sous-classe et journal exact.
2. La mère tranche (18:59Z, relayé) : une sous-classe ne compte pas ; refuser aussi `__class__` falsifiée et une surcharge de l'envoi.
3. `type(x)` rend la classe réelle de l'objet et ignore l'attribut `__class__` ; `isinstance` consulte aussi `__class__` (comportement du langage, supposé connu ; éprouvé par l'essai `test_imitateur_de_classe_cause_type_exact`, qui rend `type_journal = "ImitateurClasse"`).
4. Donc C3:188 refuse toute sous-classe et tout imitateur. Une surcharge de l'envoi par sous-classe est déjà refusée par C3:188 ; restent l'envoi posé sur l'instance et la classe modifiée après import : C3:193 et C3:194 (écart F-1, au-delà de la lettre, dans son sens).
5. En état 0, la v3 ne change rien (C3:183, C3:185) : les essais d'état 0 du v2 et S5, S6 passent.
6. V8 et V10 survivaient faute d'essai ; les essais neufs les tuent (mutations N21, N22). W1 ne décide rien (pas lu dans `routage_na_v1.py` l. 229-230) : dit, non retiré.
7. Sorties en v3 (C3:100, C3:101) : essai à noms littéraux et mutation N23.
8. Chaîne entière, essais et mutations rejoués sur copie neuve (§ 5).

**Objets de contrôle.**
- Type exact. Faux par construction (« le journal est celui de la colonne » est faux) : sous-classe qui surcharge l'envoi, sous-classe muette, imitateur plat, imitateur à `__class__` falsifiée, sous-classe du lot 3 au départ juste, envoi posé sur l'instance, aux états 1 et 2 ; attendu : `ArretCablageColonneNA` au départ, aucune génération, aucun appel ; rendu : idem (12 sous-essais). Vrai par construction : journal exact aux états 1 et 2 ; attendu : départ (état 1 : la garde de la colonne arrête la ligne plantée ; état 2 : trois générations) ; rendu : idem.
- Classe modifiée. Faux : envoi de la classe remplacé, journal exact ; attendu : refus « surchargé » ; rendu : refus. Vrai : la même classe restaurée ; attendu et rendu : reçu.
- État 0 inchangé. Vrai : journal ordinaire, sous-classe qui surcharge l'envoi ; attendu : trois générations ; rendu : idem.
- V8. Vrai par construction : un refus écrit du portier sur quatre fiches ; attendu : la ligne porte 1, puis 0 ; rendu : 1, 0, 0. La mutation qui met 0 : tuée.
- V10. Faux : fichier du journal de la génération 1 altéré avant le refus ; attendu : `journal_requetes_g1 = "scellement refusé (JournalReecrit)"` à la ligne d'arrêt et au bilan ; rendu : idem. Vrai : sans altération ; attendu et rendu : clé absente.
- Noms de sortie. Vrai : les fichiers v3 existent ; faux : aucun nom de sortie en `-na-v1.` ni `-na-v2.` ; rendu : conforme ; mutation N23 tuée.
- Juge des mutations : témoins non muté et inerte (§ 5).

**Premier pas non justifié.** Le pas 4, pour sa partie F-1 : que refuser aussi l'envoi posé sur l'instance et la classe modifiée depuis l'import soit voulu ; la mère a dit « une surcharge de `journaliser_envoi` », sans dire où. Le justifierait son mot sur ce point. Une classe modifiée avant l'import et la classe mère modifiée ne sont pas couvertes (dit en F-1).

**Mode d'échec affecté.** Sans objet : je suis développeur, non relecteur.

**Dérivation de l'énoncé seul.** Sans objet : je suis développeur, non agent de re-dérivation.

**Trouvaille de côté.**
- Le contrôle reste ponctuel (départ et construction) ; un journal mutable modifié après (par exemple `depart` remplacé) n'est pas revu à l'envoi (F-2) : point pour la mère, non poursuivi.
- Les sondes et les mutations du vérificateur importent `course_na_v2` et `aides_na_lot6_v2` : elles ne se rejouent pas telles quelles sur le v3 ; leurs cas sont repris en essais.

**Évaluateur et conseil.** Ce qui juge mon produit : les essais du lot 6 v3 et les mutations (dont les cinq neuves sur les trous relevés par le vérificateur), rejouables sur copie neuve par mon programme ; témoins non muté et inerte. Les cas hostiles viennent du vérificateur S (autre auteur), mais leur réécriture en essais est de moi. Par où le produit pourrait être bien jugé sans le mériter : les limites dites en F-1 et F-2 ne sont pas éprouvées comme refusées, parce qu'elles ne le sont pas.

## 9. Table d'empreintes et pièces

Pièces lues : vérification du lot 6 v2 `e8992a546aebf04a16a442ff017232862daa93a2d58102f5968b147a19efc871` ; `sondes/sonde_cablage.py` `90df6495c0e7b06babc14573988df0d49e946854944dcbf86433769aef4633ff` ; `sondes/mes_mutations.py` `9ccec7de3eb336ec56f82e3a20ded6d7387c9e90970017326dd60b0b6f8ff3e3` (égales à leurs compagnons).

| fichier | sha256 |
|---|---|
| `paquet/orchestrator/pole/course_na_v3.py` | `7c154a8987a34d75cee13ecf27d1d580e65afbeba051a3b34ef6798a56e87614` |
| `paquet/orchestrator/demonstrations/lancer_orchestrateur_na_v3.py` | `3a104c93a654b9b88840da9922b9dd180dbfc807427d6ce2120220d41a88de96` |
| `paquet/orchestrator/essais/aides_na_lot6_v3.py` | `26230d94a6597f90bd72e5ac8179c1a567f046fa4d638401166a79497a2825b9` |
| `paquet/orchestrator/essais/test_na_lot6_v3_course.py` | `cb34d9f5688a364e9e1c80240ef7944430d8e436acca4f42ee63eedd63283542` |
| `paquet/orchestrator/essais/test_na_lot6_v3_arrets.py` | `306b78cc7dc9531e8a7a672b14ad113c4429dc441003121e7e972e2166ebcde4` |
| `paquet/orchestrator/essais/test_na_lot6_v3_cablage.py` | `341c6656cd5c9b2f584ca2c76b8ebf4dc4bcbcc83a5c19cdd976866320915696` |
| `paquet/orchestrator/essais/mutations_na_lot6_v3.py` | `d8b50a5dda1a331c8e4b9da84500204ba5d385170180bc22c61548fa319f14d4` |
| inchangés du v1 : `configuration_course_na_v1.py`, `simulation_na_v1.py`, `ecrire_configuration_course_essai_na_v1.py`, `configuration_essai_na_lot6_v1.py` | `02644792…`, `3ab45961…`, `ea23b740…`, `53721905…` |
| `manifeste-paquet-vehicule-na-lot-6-v3.json` | `20c4065c585ef3631d076eef536aeb0425bc7a4f34023baa71f640c7d7ba12fc` |
| `appliquer_paquet_vehicule_na_lot_6_v3.py` | `2796c42a45d5a410581aaaba7e135ee4a1d47d1d0eacf521f27e39a69b66fc32` |
| `ecrire_manifeste_et_compagnons_na_lot6_v3.py` | `f68d1f5dc02e85d305599b3bd7bb8a0e5af3ffb57e287bc4f6c052c87f74ba82` |
| `journal-essais-na-lot-6-v3.txt` | `6257b8e8ac31a1e650bf255b3ee0680894d7b44805921c7ad9b5bf487261a71e` |
| `journal-essais-chaine-copie-neuve-na-lot-6-v3.txt` | `9260675ffa0532772b8e038bda5624f565a83ced4b8ccfd4e7dbcacc37666d2b` |
| `journal-mutations-na-lot-6-v3.json` | `f586771564b53e36a6e27509bdef8f2c40637ed91d5eb9c87d867142a99bb5ea` |

Table complète, ce rapport compris : `table-empreintes-dossier-na-lot-6-v3.txt`, écrite après lui, avec son compagnon ; un compagnon par fichier. Hors table : `application/`, `travail/`, `tmp/`, `pieces-origin-main/`.

— développeur du lot 6 du véhicule NA-1 (v2, v3), modèle O
