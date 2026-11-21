# Vérification du lot 6 v2 du véhicule NA-1 — v1

**Verdict : À corriger.** La lettre du refus de câblage est tenue (trois épreuves, chaîne entière, mutations du développeur rejouées). Mais le refus repose sur `isinstance` : une sous-classe du journal de la colonne qui surcharge l'envoi, et un objet qui falsifie `__class__`, passent aux états 1 et 2, et la ligne plantée part. Aucun essai ni aucune mutation du lot ne l'éprouve. Correction d'une ligne, éprouvée par moi sur une copie (§ 3).

Vérificateur neuf, hostile. Je n'ai écrit ni le lot 6 v2, ni les lots 1 à 5 et 10 a, ni la conception ; je n'ai lu aucune vérification antérieure du lot 6 v2. Processeur seul : aucun fournisseur, aucune clé, aucune dépense, aucun commit, aucune attache de dépôt. Mot de Lazar (GO-2026-11-21-74) lu ; aucune coupure ni refus rencontré. Je n'ai pas listé le dossier parent ; seuls les dossiers permis ont été listés (lot 6 v2, lots 2 v5, 3 v3, 4 v1, 5 v1, 10 a).

## 1. Rejeu de la chaîne (copie neuve dans mon dossier)

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/verificateur-lot-6-v2-b/`, `TMPDIR` posé dans `tmp/` avant tout essai.

- Base v68 tirée par `git show origin/main:… >` : programme `9b6e6843…`, manifeste `4ed9fd8e…` (égaux au rapport). Posée par son programme sur `/home/user/lciric/ideation-organism` (commit `a41b7b50…`, conforme). Puis lots 2 v5, 3 v3, 4 v1, 5 v1, 10 a par leurs programmes, sans refus.
- Programme du lot 6 v2 avec `--lancer-essais` : 11 fichiers copiés, **759 passés, 78 sous-essais passés, 0 échec** (188 s). Égal au journal `journal-essais-chaine-copie-neuve-na-lot-6-v2.txt`.
- Décompte des essais du lot 6 v2 par `--collect-only` : course 53, arrêts 43, câblage 20 = **116** (égal au rapport).
- Mutations du développeur rejouées par son programme : **53 jouées, 51 tuées, 0 survivante, 0 invalide**, T0 passe, T1 survit (journal `journal-mutations-rejouees.json`).
- Table d'empreintes du lot : `sha256sum -c` code 0.

## 2. Mode d'échec affecté : lignes tenu / cassé

**Question (1) — le refus de câblage laisse-t-il partir un appel dont le journal n'est pas celui de la colonne ? CASSÉ (sur la sous-classe et l'imitation par `__class__`) ; tenu sur l'imitation plate et l'état 0.**
Pas visé : `pole/course_na_v2.py:176-185` (`refuser_cablage`), notamment la ligne 179 `isinstance(journal, mp.JournalRequetesColonneNA)`. Sonde : `sondes/sonde_cablage.py` (une ligne plantée, égale à une entrée de la colonne, dans la requête d'un proposeur de la génération 1 ; on regarde si elle figure en « envoi » au journal des requêtes).

| cas | état | rendu | ligne partie ? |
|---|---|---|---|
| S0 témoin : journal de la colonne sain | 1 | `ArretColonneNA` | non (attendu) |
| S3c journal ordinaire | 2 | `ArretCablageColonneNA` | non (attendu) |
| **S1 sous-classe du journal de la colonne qui surcharge `journaliser_envoi`** | 1 | course finie, 3 générations | **oui** |
| **S1b idem** | 2 | course finie, 3 générations | **oui** |
| S2 objet qui imite l'interface sans hériter | 1 | `ArretCablageColonneNA` | non |
| **S3 objet qui imite l'interface et falsifie `__class__`** | 1 | course finie, 3 générations | **oui** |
| **S3b idem** | 2 | course finie, 3 générations | **oui** |
| S4 hérite seulement du journal du lot 3, `depart` d'allure juste | 1 | `ArretCablageColonneNA` | non |

Cause : `isinstance` accepte toute sous-classe et se laisse tromper par `__class__` ; la garde réelle vit dans la méthode `journaliser_envoi`, que le refus ne regarde pas. Le développeur l'a dit (rapport § 8, « Évaluateur et conseil ») ; ce n'est pas éprouvé. Le refus n'est pas rejoué à l'envoi : le journal, objet mutable, n'est contrôlé qu'au départ et à la construction.
Mutation V13 (§ 4) : remplacer `isinstance` par `type(...) is` laisse **tous** les essais du lot au vert, donc aucun essai ne sépare une sous-classe du journal exact.

**Refuse-t-il à tort à l'état 0 ? TENU.** S5 (journal ordinaire) et S6 (sous-classe qui surcharge l'envoi) partent, trois générations ; `test_etat_0_*` passent. Refusés en état 0 : un objet qui n'est pas un `JournalRequetes` du lot 3 (S7), ce qui est cohérent avec le contexte du lot 4 (`appel_garde_na_v1.py:217`). S8 (état 0, journal de la colonne d'état 2) : l'arrêt vient de la garde de la colonne elle-même, non du refus de câblage ; c'est la remarque R2 du rapport.

**Question (2) — classe de génération et course : exigences du mandat v1 et de l'erratum 1 v2. TENU**, avec deux réserves de tests.
- Classe : `GenerationNA(ag.AppelGardeNA, GenerationV68)`, `course_na_v2.py:323` ; `fournisseurs_requis` `:327` ; étapes neutralisées `:363,:367` ; aiguillage `:458` ; `juger` `:493`.
- **E4** tenu : `_appeler_portier` rend `a["refus_ecrit"]` avant `a["r"]`/`a["lu"]` (`:445-446`) ; mutation M01 tuée ; essai artefact `test_portier_arrete_fiches_au_coffre_classe_ecrite_puis_arret_5`.
- **E5** tenu : fichier à part, ajout seul, liste fermée de six événements (`:257-269`), scellé `:794` ; le journal du lot 3 reste à quatre événements (essai `test_journal_du_lot_3_ferme_a_ses_quatre_evenements`) ; M32, M33 tuées.
- **E6** tenu dans le code (`:614-646`, chaque source sous sa clé, rien d'additionné) ; mutation M29 tuée. **Réserve** : ma mutation V8 (clé `au_coffre_par_refus_du_portier` de la ligne mise à 0) **survit** : la valeur « à part » de la ligne n'est pas éprouvée.
- **E7** tenu à l'essai (`test_table_artefact_refusee_au_depart` et `…_dans_le_contexte…`, M24 tuée). **Réserve** : le test du refus à `configuration_course_na_v1.py:300-301` n'est pas la garde effective (ma mutation W1, qui le retire, survit : `rt.lire_table` refuse déjà). La citation « F:294 » du rapport vise donc une garde redondante.
- **E8** tenu : `requetes_na()` garde taille et empreinte du corps et de chaque message (`simulation_na_v1.py:223,244-255`) ; mes mutations W2 (empreinte du corps) et W3 (taille) tuées par `test_egalite_journal_et_chaine_recue`, M25 (messages) tuée.

**Question (3) — essais et mutations mérités ? TENU pour le fond, CASSÉ sur un point.**
- Mérités : les 17 mutations neuves sont toutes tuées, et pour de bonnes raisons (assertions nommées, § 4). Mon propre lot de 16 mutations (V1 à V13, W1 à W3) : 11 tuées, 5 survivantes (V7 équivalente, V10, V13 sain, W1 redondante, V8) ; toutes les prédictions sont tenues sauf V8 (prédite tuée, survit).
- Non mérité : le refus par `isinstance` n'a pas d'essai de sous-classe ni d'imitation (V13 survit). Le montage d'essai ne fabrique que le journal exact ou le journal ordinaire.
- Le juge du programme de mutations déclare « tuée » tout code de retour non nul, y compris un plantage ; les causes que j'ai relues sont des assertions (N-série et mes V1 à V6 ci-dessous).

## 3. Correction proposée (non appliquée au lot)

Sur une copie à moi (`copie-resserree/`), remplacer la ligne 179 par :
`if type(journal) is not mp.JournalRequetesColonneNA or type(journal).journaliser_envoi is not mp.JournalRequetesColonneNA.journaliser_envoi:`
Résultat de la même sonde : S1, S1b, S3, S3b passent à « `ArretCablageColonneNA`, rien ne part » ; S0 (journal sain), S5 et S6 (état 0) inchangés. Il manque alors des essais pour S1 et S3 (mutation V13 les rendrait tuables). Lot inchangé tant que la mère n'a pas tranché.

## 4. Mutations à moi (fautes par construction, prédites avant le premier lancement)

Programme : `sondes/mes_mutations.py` ; journal : `journal-mes-mutations.txt` (V1 à V13) ; W1 à W3 jouées ensuite par le même programme (sortie en terminal : W1 survit, W2 et W3 tuées). Essais joués : les trois fichiers du lot 6 v2, `-x`.

| id | faute | prédit | rendu | cause |
|---|---|---|---|---|
| V1 | construction : l'état passé au refus toujours 0 | tuée | tuée | `ArretCablageColonneNA not raised` (câblage, génération 2) |
| V2 | départ : état toujours 0 | tuée | tuée | moment « construction de la génération 1 » ≠ « départ de la course » |
| V3 | journal de la génération refusée non scellé | tuée | tuée | `JournalReecrit : journal non scellé` |
| V4 | ligne d'arrêt sans `etat_colonne` | tuée | tuée | `KeyError: 'etat_colonne'` |
| V5 | ligne « départ » sans `etat_colonne` | tuée | tuée | `KeyError` |
| V6 | état 0 : objet non journal admis | tuée | tuée | `ContexteRefuse` du lot 4 au lieu de l'arrêt nommé |
| V7 | clause « colonne chargée » retirée | survit (équivalent : le constructeur du lot 10 a l'exige) | survit | — (clause inatteignable) |
| V8 | « au coffre par refus du portier » à 0 dans la ligne | tuée | **survit** | non éprouvé |
| V9 | la fabrique de la colonne rend toujours le même journal | tuée | tuée | `ArretRequeteJournaliseeNA` |
| V10 | refus de sceau du journal de la génération 1 tu | survit (aucun essai prévu) | survit | non éprouvé |
| V11 | renforcement : état du journal supérieur admis | tuée | tuée | essai de renforcement état 1 / journal d'état 2 |
| V12 | refus à la construction placé après le constructeur hérité | tuée | tuée | `generation-2` existe (« avant tout constructeur hérité » éprouvé) |
| V13 | `type(...) is` au lieu de `isinstance` | survit (resserrement sain) | survit | montre que le trou n'est pas éprouvé |
| W1 | E7 : refus de la table retiré dans la configuration | tuée ou équivalente | survit | garde redondante |
| W2, W3 | E8 : empreinte / taille du corps non gardées | tuée | tuée | `test_egalite_journal_et_chaine_recue` |

## 5. Écarts E-1 à E-10 et points R3 à R5 : ce qui reste pour la mère

- **Pour la mère** : E-1 (renforcement : journal de la colonne d'un autre état refusé ; V11 le montre éprouvé ; à confirmer par la mère). E-2 (état inconnu ou fabrique absente : arrêt nommé levé avant toute écriture, donc sans ligne au journal des arrêts ; seul le message le porte). E-4 (aucun chemin en ligne de commande : le lanceur exige un `DepartColonne` Python ; lancé seul, il refuse toujours). E-6 (noms de sortie `…-v1` gardés, R12 à trancher). E-8 (le développeur a listé le dossier parent : écart à son mandat, déclaré ; conduite, non code). R1 (numéro de l'arrêt à l'additif). R3 (`comptes_colonne` non porté à la ligne). R4 (la garde de la colonne arrête toute la course à la première ligne égale ; refus de case voulu ou non ?). **R5 (important)** : `mp.garder_registre_servi` et le contrôle des pièces fixes à la génération 2 ne sont branchés ni par la course ni par le lanceur (`gardes_depart_en_plus=()` par défaut ; le lanceur ne les passe pas, `lancer_orchestrateur_na_v2.py:154-158`) : en états 1 et 2, la tenue (iii) n'agit que si le lot 8 les branche.
- Sans suite : E-3, E-5, E-7, E-9, E-10 et E-11 (déclarés, sans effet sur la sûreté ; je n'ai rien ouvert sous `/root/.claude/`) ; R2, R6 (cohérents avec le code lu).

## 6. Relevé de méthode

**Chaîne de raisonnement.**
1. Mandat de reprise (`89b2a38d…`), mandat v1 (`b5976626…`), erratum 1 v2 (`24d37f85…`), consigne commune : lus en entier.
2. Rejeu : v68 puis lots 2 à 5 et 10 a par leurs programmes, puis `appliquer_paquet_vehicule_na_lot_6_v2.py --lancer-essais` : 759 passés, 78 sous-essais, 0 échec (§ 1) ; mutations du développeur rejouées : 51 tuées sur 51.
3. Lecture de `course_na_v2.py` en entier, de `matiere_premiere_na_v1.py:491-520` (la garde vit dans `journaliser_envoi`, lit `self.depart.colonne`) et de `appel_garde_na_v1.py:217` (contexte du lot 4 : `isinstance` du journal du lot 3).
4. Pas 3 implique : `isinstance` ne protège pas la méthode. Sonde `sondes/sonde_cablage.py` : S1, S1b, S3, S3b laissent partir la ligne plantée (rejouable : `PYTHONPATH` non requis, argument = racine de `orchestrator`).
5. Correction par `type(…) is` sur copie : sonde repasse au rouge là où il faut, au vert pour S0, S5, S6 (§ 3).
6. Mutations V1 à V13, W1 à W3 : prédictions écrites dans le fichier avant lancement, causes lues (§ 4).
7. Écarts et remarques du rapport relus contre le code (§ 5).

**Objets de contrôle.** Faux par construction : états 1 et 2 avec journal ordinaire (S3c), état 1 avec journal de la colonne d'un autre état, mutations V1 à V6, V9, V11, V12. Attendu : refus nommé et rien ne part ; rendu : conforme. Vrai par construction : S0 (journal sain) et S5 (état 0, journal ordinaire) : le premier arrête sur la garde de la colonne, le second part ; conforme. Le contrôle du trou : S1 et S3 sont faux (la conclusion « le journal est celui de la colonne » est fausse), le refus y « réussit » à tort : c'est le défaut relevé.

**Premier pas non justifié.** Pas 4 pour la gravité : que des appelants hostiles (sous-classe, `__class__`) soient dans le modèle de menace du lot. Le mot de la mère (GO-2026-11-21-69) dit « n'est pas `JournalRequetesColonneNA` » ; ce qui le justifierait est que la mère dise si une sous-classe compte comme « celui de la colonne ».

**Mode d'échec affecté.** Épreuve qui ne peut pas échouer ou pas réussir, appliquée au refus de câblage : tenu pour l'état 0, l'imitation plate et le journal ordinaire ; cassé pour la sous-classe et `__class__` (§ 2).

**Dérivation de l'énoncé seul.** Sans objet : je suis vérificateur, non agent de re-dérivation.

**Trouvaille de côté.** (a) Ma mutation V8 survit : la valeur « au coffre par refus du portier » de la ligne de la génération n'est pas éprouvée. (b) V10 survit : le refus de sceau du journal de la génération 1 dit à la ligne d'arrêt n'est pas éprouvé. (c) La garde E7 de `configuration_course_na_v1.py:300` est redondante avec `lire_table`.

**Évaluateur et conseil.** Ce qui juge mon verdict : la sonde `sonde_cablage.py` (témoins S0, S3c, S5 admis avant les cas hostiles : le sain arrête sur la garde de la colonne, l'artefact ordinaire est refusé, l'état 0 part) et les mutations V1 à V13, W1 à W3 avec prédictions écrites. Je pourrais être jugé trop sévère par un lecteur qui ne retient que la lettre (`isinstance` satisfait le mot de la mère) ; trop clément si l'on oublie que le journal est mutable après le contrôle (non sondé : un crochet d'essai peut remplacer `depart` après la construction).
