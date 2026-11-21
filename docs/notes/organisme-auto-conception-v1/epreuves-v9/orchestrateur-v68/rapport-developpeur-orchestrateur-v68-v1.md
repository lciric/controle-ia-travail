# Rapport du développeur — orchestrateur v68 de l'organisme d'idéation (fichiers neufs, sans dépense) — v1

- Développeur unique de la v68 (modèle L′), 2026-11-19, 14:18Z → 14:48Z (`date -u`). Routine (R-3861) : processeur seul, hors ligne, aucun appel à un fournisseur, aucun relais réel, jamais `--reel`, aucune dépense, aucune valeur de clé lue. Tout lancement en moteur simulé ; l'étage de tests de mort joué avec l'**exécuteur factice demandé explicitement** (aucune barrière, le vrai bac à sable n'est pas joué).
- Orchestrateur `/home/user/ideation-organism`, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb` : **lu seulement** ; arbre propre avant et après (`git status --porcelain --ignored` vide). Travail sur une copie (`cp -a`) dans le bloc-notes ; à la fin, `git status` de la copie ne montre que les huit fichiers neufs, non suivis.
- Mandat : plan v68 du rapport du rang 0 (`rang-0-branchement/rapport-developpeur-rang-0-v1.md`, `966a3870…`, § 5), les quatre précisions de la contre-lecture (`contre-lecture-rang-0-v1.md`, `f219e7cc…`, constat 9), les exigences de la mère (R-3861) et la garde du complément 3 de N-073 (la mémoire ne sert jamais un verdict).
- **Écrire cette version est de la routine ; l'allumer est un nœud de Lazar. Rien ici ne l'allume** : le lanceur v68 refuse le moteur réel par construction.

## 1. Verdict

Les trois défauts de l'orchestrateur épinglés au rang 0 sont corrigés dans des fichiers neufs, et un quatrième (budget remis à zéro par génération, **bloquant** pour la mère) a sa garde : (1) la génération suivante lit la sélection scellée **en objet**, gardée ligne par ligne par A4, sous un titre neuf — plus de `JSONDecodeError` ; (2) un étage peut suivre la dernière génération, ce qui ouvre le régime « tests de mort sans rien servir », séparé du régime « lecture de la sélection » ; (3) une garde de budget **de la course** cumule générations et étages et s'arrête au plafond de la course ; (4) `heritage_lu` est écrit sur la ligne de la génération g + 1. Courses de bout en bout sur deux générations, moteur simulé, interrupteurs allumés puis éteints : toutes conformes ; le témoin v59 casse comme au rang 0 sur la même configuration. **La v68 ne débloque aucun étage réel** : il faut encore le lanceur v11, l'additif, les nœuds de Lazar, un devis, une ligne de GO et la machine jetable (§ 7).

## 2. Livré (paquet, à appliquer sur une copie neuve de l'orchestrateur)

Dossier : `docs/notes/organisme-auto-conception-v1/epreuves-v9/orchestrateur-v68/`.

| fichier neuf (chemin dans l'orchestrateur) | lignes | sha256 | rôle |
|---|---|---|---|
| `orchestrator/pole/configuration_v68.py` | 65 | `1241b18b6d89d02d88e6187fc38030d3fcbc7c355e307f3c6b0ad68fab87503b` | `montant_requis_v68` (N générations, E étages), `nombre_etages_v68` |
| `orchestrator/pole/budget_course_v68.py` | 133 | `730ab7eca553494b5b4e97f469de62431ae00ce56d6642ae8c195a378df43558` | `GardeBudgetCourseV68`, second calcul `rejouer_journal_course_v68` |
| `orchestrator/pole/course2_v68.py` | 386 | `c1aeab4cc58118a373dd1503d34fd4e02694aeed6e550675aacd74db050b1024` | `GenerationV68`, `lignes_depuis_selection_v68`, `rendre_heritage_v68`, `verifier_regime_v68`, `executer_course_v68` |
| `orchestrator/pole/simulation_v68.py` | 110 | `c1efecd432c6001fec109049e9c97eaa5b0cabe26a5d896e2f3c9933ca8b217c` | moteur simulé : fiches avec `test_de_mort` à bloc `statistique`, rôles de l'étage ; inerte sans ce champ |
| `orchestrator/demonstrations/ideation_v68.py` | 176 | `6fce17357b8eafe47764d8b860d0a59051820763db41a2ec0bf27639a2484d09` | lanceur (le v8 chargé à part) |
| `orchestrator/demonstrations/essai_a_blanc_v68.py` | 214 | `4629cce12e56a602b9806138d97b509ea86d66226ce2de357baa77997f7f85f3` | essai à blanc de bout en bout |
| `orchestrator/essais/aides_v68.py` | 122 | `45b705bd6bccfc0cf75a7103d6ce12392ec4c04596878ae66b34f5ea58b7d004` | aides des essais |
| `orchestrator/essais/test_v68_course2.py` | 890 | `6c45b32fea6b011b31f834fd75a952a62800d3faa6dc83a467158318dd94c676` | essais de la v68 |

Pièces du dossier : `paquet/orchestrator/…` (les huit fichiers), `manifeste-paquet-orchestrateur-v68-v1.json` (chemin, sha256, octets et lignes de chaque fichier ; commit de base ; 38 fichiers existants lus, avec leur empreinte au commit et dans la copie, égales ; aucun fichier existant modifié), `appliquer_paquet_orchestrateur_v68_v1.py` (`9b6e6843…` : vérifie les empreintes du paquet, refuse une destination existante ou placée dans la source, clone la source **sans y écrire**, fixe le commit de base, copie, vérifie chaque copie et que `git status` ne montre que les fichiers du paquet, non suivis ; `--lancer-essais`), `journal-essais-orchestrateur-v68-v1.txt`, `essai-a-blanc-v1/` (résumé, journaux, bilans), ce rapport. Empreintes du manifeste et de ce rapport : compagnons `.sha256`.

Écart de chemin : la consigne disait `paquet/tests/…` ; les essais de l'orchestrateur vivent dans `orchestrator/essais/` : le paquet suit le chemin réel (`paquet/orchestrator/essais/…`), comme `paquet/orchestrator/pole/…` et `paquet/orchestrator/demonstrations/…`.

## 3. Ce qui est fait

1. **Héritage illisible (rang 0, manque 1).** `lignes_depuis_selection_v68` lit la sélection de l'étage avec la vérification de la v59 (`boucle_fermee_v59.lire_scelle_verifie` : fichier régulier, sceau, empreinte consignée par l'étage), vérifie la version v57 et le sceau des fiches de l'étage, refuse une retenue absente ou sans nom ou énoncé (aucun champ inventé), et rend un **objet** `{type, selection_sha256, depuis_generation, lignes: [{identifiant_auteur, nom, enonce}]}` (nom et énoncé ramenés à une ligne : un énoncé ne peut pas ouvrir une section `##`). `GenerationV68(GenerationV56)` refuse tout héritage texte (`heritage_texte`, classement des juges de la v56, Markdown de la v59 : `HeritageNonSelection`, avant toute écriture) ; `_heritage_garde` passe **chaque ligne** « - nom : énoncé » à `fiches_v54.trouver` (ligne exclue avec incident, ou arrêt, selon `a4.action`, comme la v54) ; `_proposer` est la copie de la v54 (l. 135-166) au titre près (`TITRE_HERITAGE_SELECTION` = « Fiches retenues par l'étage de tests de mort de la génération précédente (nom et énoncé) », au lieu de « titres, résumés, verdict agrégé ») plus un compteur ; un essai le tient par le code source. J'ai pris la variante « objet » plutôt que la reconnaissance du Markdown de la v59 que proposait le § 5 (ce que la contre-lecture laissait ouvert) : aucune analyse de texte, aucune empreinte servie aux proposeurs.
2. **Étage après la dernière génération (manque 2).** `etage_apres_derniere=True` joue l'étage après chaque génération, la dernière comprise ; la sélection est écrite et scellée, jamais servie (`selection.servie_a_la_suivante: false`, `heritage_servi_a_la_suivante: null`).
3. **Budget de la course (manque 3, bloquant).** `GardeBudgetCourseV68` : avant chaque poste, **réservation au pire** (génération : S17 entier ; étage : son plafond) ; poste refusé si cumul + réservation dépasse le plafond de la course (`PlafondDeCourseAtteint`, arrêt **avant** toute dépense du poste) ; après le poste, coût réel compté en entier (cumul du `BudgetV56` de la génération ; coûts rendus par l'étage), coût inconnu compté à la réservation ; coût au-delà de la réservation ou cumul au-delà du plafond : `CumulCourseAuDela`. Le plafond de la course est un argument **sans défaut**, réel > 0 et jamais au-delà du montant requis (le lanceur passe le montant requis, ou `--plafond-course-usd` plus bas). L'étage doit tenir lui-même ce que la course lui réserve : `reglages.plafond_total_usd` exigé et ≤ `plafond_etage_usd` ; un expérimentateur externe exige `plafond_externe_usd`, la somme sous le plafond de l'étage (sans cela, l'étage v5 ne borne pas le coût externe). La règle d'A1 de chaque génération (S17, ligne 11a) est inchangée. La portée « course » est refusée pour N > 1 ou un étage (`montant_requis_v68`) : la garde cumule, mais une ligne de GO à S17 ne couvrirait pas N générations.
4. **`heritage_lu` (précision ii)** : sur la ligne de la génération g + 1 — empreinte de la sélection lue, génération source, retenues, servies, identifiants exclus par A4, section « servie », « servie vide » ou « omise » (avec la raison), règle de la sélection vide, titre, empreinte du texte servi (« ## titre » et les lignes), nombre de consignes qui l'ont reçue.
5. **Sélection vide (précision iii)** : `selection_vide` ∈ {« omettre », « servir_vide »}, **défaut « omettre »** : c'est ce qui minimise ce qui est servi (aucune section ; la consigne de g + 1 est alors celle d'une génération sans héritage, et « rien n'a survécu » n'est pas dit aux proposeurs). « servir_vide » rend le comportement de la v59 (« - (aucune fiche retenue) »). Toutes les lignes exclues par A4 : même règle. **À fixer par l'additif (nœud 14 de l'ordre v3).**
6. **Montant requis (précision i)** : `configuration_v68.montant_requis_v68` (module neuf ; la v54 intacte) : N × S17 + E × plafond de l'étage, E = N − 1 ou N ; égal à la v54 pour E = N − 1 (essai). Sous `--verifier-seulement`, le lanceur v68 rend ce montant et le nombre d'étages : le lanceur v11 pourra recouper.
7. **Moteur simulé v68** : les fiches portent un `test_de_mort` projetable (bloc `statistique`, donnée de la tranche d'essai) **seulement si** `champs_fiche` le demande ; l'expérimentateur simulé écrit un fichier brut de moyenne 0,42 ou 0,18 selon l'empreinte de l'identifiant de la fiche, le lecteur est un témoin honnête ; le verdict reste celui du noyau de l'étage v5. Sans ce champ (configuration v5 de la course d'auto-conception), ses réponses sont celles de la v56 (essai).
8. **Lanceur `ideation_v68.py`** : le v8 chargé à part ; options `--lecture-selection {oui,non}` (défaut « non »), `--etage-apres-derniere` (absent par défaut), `--selection-vide` (défaut « omettre »), `--plafond-course-usd` ; régime vérifié avant toute écriture ; sessions sous `TMPDIR` de l'environnement donné ; sans `--course-2`, la main au lanceur v8.

## 4. Refus et gardes (chacun avec un cas sain et un artefact, R5)

Avant toute génération et toute écriture : nombre de générations (entier ≥ 1) ; interrupteurs non booléens (aucun défaut) ; lecture avec une seule génération ; lecture sans étage ; étage après la dernière sans étage ; `selection_vide` inconnu ; titre vide, sur deux lignes ou porteur d'une étiquette interdite (A4) ; portée « course » avec N > 1 ou un étage ; plafond de la course absent, nul, négatif, booléen ou au-delà du montant requis ; étage sans `plafond_total_usd` ou au-delà de son plafond, expérimentateur externe sans plafond externe ou au-delà ; clé d'étage manquante ; machine non jetable (variable absente, nom hors liste blanche) ; sortie présente (R12). Chaque refus est éprouvé **pour son motif** (texte de l'exception) et sans création de la sortie ; un témoin montre que les mêmes arguments sans l'artefact passent les gardes.

Pendant la course : héritage texte refusé ; sélection non vérifiée (empreinte autre, sceau absent, version autre, retenue absente, retenue sans nom) refusée ; A4 par ligne (exclue ou arrêt) ; plafond de la course atteint (arrêt avant la génération 2, rien d'écrit pour elle) ; génération au-delà de sa réservation (relais qui n'aurait pas tenu) ; étage au-delà de son plafond ; coût d'étage inconnu compté à la réservation. Trois mutations montrent que les essais ont des dents (réservation retirée : la génération 2 part ; A4 retirée : la ligne interdite passe ; compte retiré : l'étage à 6 USD sous une réservation de 5 passe).

Lanceur : moteur réel — un interrupteur allumé (`tests_de_mort_reels` dès qu'un étage est configuré, `lecture_selection_generation_suivante` avec la lecture) exige `--registre-go` et une ligne de GO au montant requis (`verifier_go_v56` : type, Lazar, période, révocations, montant exact) **dont le périmètre nomme chaque interrupteur allumé** ; puis, **toujours**, `MoteurReelRefuseV68` liste les blocages (additif non épinglé : `ADDITIF_INTERRUPTEURS_V68 = (None, None)` ; lanceur v11 absent ; bac à sable réel jamais joué avec l'étage v5 ; machine jetable ; aucune ligne de GO). Éteint aussi : le moteur réel est refusé (le chemin réel de la course d'auto-conception reste le lanceur v9 → `ideation_v8.py`, inchangé). Aucune variable d'environnement ni aucun champ de configuration n'allume quoi que ce soit.

Programme d'application : destination existante, destination dans la source, fichier du paquet altéré : refusés avant toute copie (journal des essais).

## 5. Régimes possibles

| régime | options du lanceur | ce qui est servi aux proposeurs | étages | montant requis |
|---|---|---|---|---|
| éteint, sans étage (interrupteurs éteints) | configuration sans `etage_tests_de_mort` | rien | aucun | N × S17 |
| éteint, avec étage | configuration avec étage, aucune option | rien ; sélection scellée jamais servie | entre les générations | N × S17 + (N − 1) × E |
| **tests de mort sans rien servir** | `--etage-apres-derniere` (N ≥ 1) | rien | après chaque génération, la dernière comprise | N × S17 + N × E |
| **lecture de la sélection** | `--lecture-selection oui` (N ≥ 2) | g + 1 : nom et énoncé des retenues de l'étage de g, sous A4 | entre les générations (+ après la dernière avec l'option) | N × S17 + (N − 1 ou N) × E |

La mémoire anti-redite passe d'une génération à l'autre comme en v56 ; elle n'est jamais servie et ne porte aucun verdict (complément 3 de N-073). Aucun régime ne sert le classement des juges. Essais : aucune consigne de proposeur (passe 1, deux générations, tous régimes) ne contient « survit », « éliminée », « non concluant », « notable » ni « verdict agrégé » ; la génération 1 est la même (classement, fiches, mémoire à l'octet) en régime « tests de mort » et en régime « lecture » ; éteint, une génération sans étage, les sorties de la génération sont égales à l'octet à celles de la course v56, avec le moteur simulé v56 comme avec le v68.

## 6. Essais (décomptes)

Lancés au premier plan ou en tâche de fond, `python3 -B -m pytest -q -p no:cacheprovider`, `PYTHONDONTWRITEBYTECODE=1`, dans la copie de travail (journal : `journal-essais-orchestrateur-v68-v1.txt`).

- **Essais neufs de la v68** (`essais/test_v68_course2.py`) : **55 passés, 0 échec** (78 sous-essais), dans la copie de travail, puis **rejoués dans une copie neuve après application du paquet par son programme** : 55 passés.
- **Essais existants qui touchent `course2_v54/v56/v59`, `noyau_v56`, `budget_v56`, `etage_entre_generations_v57` et les lanceurs v8/v59** (douze fichiers : `test_attaque_goodhart_v2` à `v5`, `test_juges_idees_v2`, `test_v54_annexe`, `test_v54_corrections`, `test_v54_prepilote`, `test_v55_corrections`, `test_v56_corrections`, `test_v57b_cablage_verdict`, `test_v59_boucle_fermee`) : **avant la v68 : 515 passés, 2 échecs, 3 ignorés** ; avec la v68 (même liste plus `test_v53_course2`) : **531 passés, 3 échecs, 3 ignorés** (591 sous-essais ; 14:40:43Z → 14:47:13Z), soit les mêmes 515 et 2 qu'avant, plus 16 passés et 1 échec de `test_v53_course2`. Les trois échecs sont antérieurs à la v68 et sans lien avec elle : `test_v54_prepilote::TestR12::test_aucun_fichier_de_la_v53_modifie`, `test_v55_corrections::TestR12V55::test_aucun_fichier_de_la_v54_modifie` et `test_v53_course2::TestR12::test_aucun_fichier_de_la_v52b_modifie` cherchent les listes `EMPREINTES-orchestrateur-pole-v7-v52b/v53/v54`, absentes de l'arbre au commit a41b7b50 (seule la liste v56 y est).
- Non lancés : `test_tour_ferme_v62`, `_v63`, `_v64`, `test_v61_tour_ferme` (retenus par la recherche parce qu'ils nomment `ideation_v8` dans un texte) : `scipy` absent de la machine, erreur à la collecte ; rien installé (hors ligne).

## 7. Essai à blanc de bout en bout (versé : `essai-a-blanc-v1/`)

Joué **dans la copie neuve où le programme d'application a posé le paquet**, par `demonstrations/essai_a_blanc_v68.py` : douze lancements du lanceur en processus à part (`python -I -B`, environnement réduit à `PATH`, `POLE_MACHINE_JETABLE_V56=1`, `TMPDIR` dans la sortie, `LANG`, `PYTHONDONTWRITEBYTECODE`), 14:42:25Z → 14:42:37Z. Résumé `resume-essai-a-blanc-v68.json` (`11f56996…`) : **18 vérifications sur 18 vraies**.

| lancement | code | constat (comptes seulement) |
|---|---|---|
| vérifier sans étage / éteint / tests de mort / lecture | 0 | interrupteurs « éteints », 100 USD (E = 0) ; « tests_de_mort_reels », 105 USD (E = 1) ; 110 USD (E = 2) ; les deux interrupteurs, 105 USD |
| éteint sans étage, 2 générations | 0 | 11 + 11 fiches classées ; aucun étage ; aucun héritage ; cumul de la course 1,62 USD fictifs sur 100 |
| éteint avec étage, 2 générations | 0 | étage après la génération 1 : 3 candidates, 2 « survit », 1 « éliminée » ; sélection `a9ed1952…` scellée, **jamais servie** ; génération 2 sans héritage |
| tests de mort sans rien servir | 0 | étage après chaque génération (2 survit / 1 éliminée ; puis 1 survit) ; rien servi ; cumul 1,74 USD sur 110 (quatre postes) |
| lecture de la sélection | 0 | la génération 2 lit `a9ed1952…` : 2 retenues, 2 servies, section servie dans 2 consignes ; empreinte du texte servi `8f4d402f…` **égale à celle recalculée à part** depuis les fichiers scellés de l'étage ; la fiche éliminée absente |
| plafond de la course 50,5 USD | 2 | génération 1 et étage joués ; génération 2 refusée (`PlafondDeCourseAtteint`, cumul 0,90 + 50 > 50,5) ; aucun dossier `generation-2` |
| moteur réel, lecture allumée | 2 | `GoRefuse` : `--registre-go` exigé ; aucune sortie |
| moteur réel, éteint sans étage | 2 | `MoteurReelRefuseV68` : refusé par construction ; aucune sortie |
| témoin : lanceur `ideation_v59.py`, 2 générations | 2 | `JSONDecodeError` à la génération 2 (le défaut du rang 0, sur la même configuration) |

## 8. Ce que la v68 permet et ne permet pas

Permet, **en moteur simulé** : les trois régimes ci-dessus, séparément ; une sélection non vide lue par la génération suivante sans rien d'autre ; des tests de mort sur chaque génération sans rien servir ; un plafond de course tenu ; un montant requis juste pour N étages ; un essai de bout en bout par le lanceur.

Ne permet pas : **aucune exécution réelle** (moteur réel refusé par construction) ; aucun allumage sans additif ; le bac à sable réel n'est pas joué (exécuteur factice) ; les bornes des relais, parts au pire et crédits du lanceur de course restent calculés pour une génération (lanceur v10) ; les fiches de la course d'auto-conception n'ont toujours pas de champ de test (configuration v5) : l'étage les refuserait toutes (le moteur simulé v68 ne change rien à cela, il est inerte sur cette configuration) ; la réservation au pire (S17 entier par génération) peut arrêter une course dont la dépense réelle aurait tenu : c'est voulu (jamais de dépassement), à dire au devis.

## 9. Ce qui reste

1. **Contre-lecture** de la v68 par un autre modèle (R2).
2. **Lanceur de course v11** (plan du rang 0, § 6) : épingler l'orchestrateur v68 (les huit empreintes du manifeste) et `demonstrations/ideation_v68.py` ; autoriser `tests_de_mort_reels` seul (`--etage-apres-derniere`, sans lecture) ; recouper le montant (N − 1 ou N étages) avec `--verifier-seulement` ; bornes des relais, parts au pire et crédits multipliés par N, plus les appels de l'étage ; plafond du relais Claude porté au montant requis ; relire `heritage_lu` et `budget_course` par comptes ; reprendre les gardes des interrupteurs de la v10.
3. **Additif des interrupteurs** (à épingler dans le lanceur v11 et dans `ADDITIF_INTERRUPTEURS_V68` d'une version suivante) : ce qui est servi et à qui, le titre de la section, la règle de la sélection vide (défaut proposé : « omettre »), le régime retenu par ligne, la tranche et la liste blanche, les valeurs de l'étage.
4. **Nœuds de Lazar** : activation de chaque interrupteur (points 2 et 14 de l'ordre v3 : ce qui est servi) ; champs de fiche de la course d'auto-conception (changer `champs_fiche` change la consigne servie et le préenregistrement) ; devis ; ligne de GO nominative ; toute exécution réelle.
5. **Machine jetable** (R-640) : location, relais hors de la machine ou série sans clé — nœud et dépense ; essai réel du bac à sable (`test_v52b_borne_memoire`, un étage v5 réel) avant tout GO d'étage.

## 10. Lignes de l'ordre v3 (d'après le § 7 du rapport du rang 0, contre-lu ; ordre v3 `b19f550b…` non relu en entier ici)

- **Débloquées côté orchestrateur par la v68** (le défaut qui les arrêtait dans l'orchestrateur est corrigé ; **aucune n'est jouable en réel aujourd'hui**) :
  - tests de mort réels sans rien servir (manque 2 levé) : rangs **1, 2, 4, 10, 11, 14, 18, 21**, et 6 si son oracle lit des lois promues ;
  - lecture de la sélection par la génération suivante (manque 1 levé) : rangs **6, 7, 8, 9** (second temps), **12, 20** (second temps) ; 17 et 19 à vérifier.
- **Restent bloquées pour toutes ces lignes** : lanceur v11, additif, nœuds 2 et 14 (ce qui est servi), devis, ligne de GO, machine jetable, bac à sable réel ; pour la course d'auto-conception, en plus, le nœud des champs de fiche. Réserve du rang 0 maintenue : plusieurs de ces lignes jouent leur étage payant sur un monde planté (bancs A, B, F, H…) dont le véhicule est le lanceur de leur banc, qui reprendra les gardes des interrupteurs.
- **Non concernées** : rang 3 et les étages sur processeur des rangs 5, 13, 15, 16, 22 (inchangé).

## 11. Écarts

1. Une commande du shell a contenu un heredoc **vide** (`python3 -B - <<'X'` suivi de `X`), contraire à la consigne « jamais de heredoc » : rien n'a été exécuté ni écrit (sortie vide, `|| true`). Signalé ; aucun autre.
2. Chemin du paquet : `paquet/orchestrator/essais/` au lieu de `paquet/tests/` (§ 2).
3. Quatre fichiers d'essais existants non lancés (`scipy` absent, § 6) ; la base « avant » couvre douze fichiers, la mesure « avec la v68 » treize (`test_v53_course2` ajouté).
4. Les valeurs de l'étage d'essai (3 candidates, 3 exécutions, 120 s, 1 024 Mo, 5 USD, préfixe de graines `v68c` choisi pour que la génération 1 ait des fiches notables et une sélection qui retient et exclut) sont des valeurs d'essai, pas un réglage.
5. Les coûts cités sont **fictifs** (moteur simulé, 0,01 USD par appel) ; aucune dépense.
