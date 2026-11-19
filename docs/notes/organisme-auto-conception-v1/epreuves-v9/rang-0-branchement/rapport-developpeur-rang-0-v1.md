# Rapport du développeur — rang 0 des épreuves v9 (branchement, éteint par défaut) — v1

- Développeur unique du rang 0 (modèle L′), 2026-11-19, 13:33Z → 13:58Z (`date -u`). Processeur seul, hors ligne, aucun appel à un fournisseur, aucun relais réel, jamais `--reel`, aucune dépense ; tout lancement fait sous `--a-blanc` (moteur simulé de l'orchestrateur). Orchestrateur `/home/user/ideation-organism` (commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`) **lu seulement**, arbre propre avant et après.
- État du code (ce qui existe et ce qui manque, fichiers et lignes) : `etat-du-code-rang-0-v1.md`, même dossier.
- **Écrire ce branchement est de la routine ; l'activer est un nœud de Lazar. Rien ici ne l'active** : l'additif de préenregistrement des interrupteurs n'est pas épinglé (à venir), donc tout allumage est refusé hors de l'essai à blanc, et le moteur réel allumé est refusé par construction dans cette version.

## 1. Verdict

Le lanceur v10 porte deux interrupteurs nommés, éteints par défaut. **Éteint, il rejoue la v9 à l'identique**, prouvé par comparaison manifeste contre manifeste d'un essai à blanc v9 et d'un essai à blanc v10 (§ 3). **Allumé**, il exige une ligne de GO dont le périmètre nomme chaque interrupteur et un additif épinglé, sans quoi il refuse avant toute écriture. **Allumé sous `--a-blanc`**, il joue la chaîne de l'orchestrateur jusqu'au bout de ce qu'elle sait faire : génération 1, étage de tests de mort (exécuteur factice), sélection scellée, servie à la génération 2. **La génération 2 s'arrête alors sur un défaut de l'orchestrateur épinglé** (l'héritage servi en texte est lu par `json.loads`). La lecture de la sélection et les tests de mort réels exigent donc une version d'orchestrateur (plan au § 5), puis un lanceur v11, un additif, un devis et une machine jetable (§ 6). Le rang 0 ne débloque aujourd'hui **aucun étage réel** de l'ordre v3 ; il en pose le code de garde et la preuve d'innocuité.

## 2. Livré

| pièce | chemin | sha256 |
|---|---|---|
| lanceur v10 | `scripts/lancer_course_auto_conception_v10.py` (3 334 lignes ; la v9 reste en place) | `f4196ec5662266a0d22c2832c3fdd19a9af159ef1514b70a95e4b348f546a07a` |
| configuration des interrupteurs (nom neuf, jamais ouverte éteint) | `rang-0-branchement/configuration-interrupteurs-course-auto-conception-v1.json` | `bb4ecbfb24f43d356474d301052ff8df80f829bc7a8b6c0365b64004f8608c3c` |
| essais | `tests/test_lancer_course_auto_conception_v10.py` | `d0d2de5541022bf4bf5184002989cdfde55c2f3dff3248e67afcbe7f4bf046a3` |
| essais à blanc versés (82 fichiers, compagnons compris) | `rang-0-branchement/essai-a-blanc-v1/` | comparaison : `08ddb283130bea16de29becadf8aa917ee2eb8a15d45ee2c24f0ea52504e5cb4` |
| état du code | `rang-0-branchement/etat-du-code-rang-0-v1.md` | au compagnon |
| ce rapport | `rang-0-branchement/rapport-developpeur-rang-0-v1.md` | au compagnon |

Décomptes : **45 essais v10, 45 passés** ; **essais v9 rejoués : 307 passés** (inchangés). Suite entière du dépôt non rejouée (durée) : seuls ces deux fichiers l'ont été.

## 3. Ce qui est branché (lanceur v10)

1. **Interrupteurs** (`INTERRUPTEURS`, l. 567) : `lecture_selection_generation_suivante` (`--allumer-lecture-selection`) et `tests_de_mort_reels` (`--allumer-tests-de-mort-reels`), placés avant `--a-blanc` ; éteints sans option. `principal` (l. 3304) refuse toute autre option, une option après `--a-blanc`, et un interrupteur avec `--decouper`.
2. **Éteints** : `executer` (l. 2889) suit la v9 ligne pour ligne ; trois lignes de la v9 seulement sont remplacées, toutes paramétrées par l'interrupteur (commande `--generations 1`, montant 150 vérifié, nom du dossier d'alerte de crédit), et chaque ligne ajoutée contient un jeton d'une liste fermée propre à la v10 (« allume », « interrupteurs », « montant_attendu »…), contrôle textuel plus faible que la preuve par essai ci-dessous (essai `test_executer_v10_ne_retire_de_la_v9_que_trois_lignes`). Toutes les autres fonctions et classes de la v9 sont identiques au caractère près (`test_le_reste_de_la_v9_inchange`), sauf cinq : `reglages_a_blanc`, `principal` et la classe `Reglages` (ajouts pour les interrupteurs, sans effet éteints), `ecrire_registre_derive` et `verifier_course_jamais_lancee_ou_closes_admises` (nom de version dans un texte seulement). Le manifeste de départ porte en plus `interrupteurs_v10` = « éteints ».
3. **Garde des interrupteurs** (`garder_interrupteurs`, l. 2778), appelée juste après la pièce de départ, avant la garde « une seule course », avant tout appel et toute écriture, dans cet ordre :
   - noms connus, chacun une fois ; **combinaison** (`verifier_combinaison`, l. 2695) : la lecture exige les tests de mort ; les tests de mort seuls sont refusés (aucun étage après la dernière génération dans l'orchestrateur) ;
   - **configuration des interrupteurs** (`lire_configuration_interrupteurs`, l. 2708) : empreinte épinglée, scellée, N ≥ 2, portée « par_generation », lanceur `ideation_v59.py` au commit épinglé, étage complet, correspondance à six champs, plafond d'étage > 0, `environnement_permis` sans nom de clé ; montant requis N × 150 + (N − 1) × plafond de l'étage ;
   - **ligne de GO** (`go_interrupteurs` de la pièce de départ ; ni consommée, ni celle de l'épreuve des témoins) vérifiée par la `verifier_go` de la v9 : type « calcul », Lazar, période, non révoquée, plafond exactement égal au montant requis, **périmètre qui nomme chaque interrupteur allumé** et « auto-conception » ; registre de `main` en réel, registre d'essai scellé sous `--a-blanc` (jamais `registres/`) ;
   - **additif des interrupteurs** (`verifier_additif_interrupteurs`, l. 2756) : empreinte posée dans le lanceur (`ADDITIF_INTERRUPTEURS = (None, None)`, l. 575 : **à venir**), présent, scellé, qui cite l'empreinte du préenregistrement v2, celle de la configuration des interrupteurs, et nomme chaque interrupteur ;
   - **moteur réel : refus** avec les cinq blocages de `BLOCAGES_REELS_V10` (l. 606).
4. **Allumé, à blanc** : empreintes de quinze fichiers de l'orchestrateur propres au chemin v59 vérifiées en plus (`verifier_empreintes_allume`) ; configuration v5 assemblée comme en v9 puis portée « par_generation » et étage ajoutés (`appliquer_interrupteurs`, l. 2823 ; « À REMPLIR » refusé, tranche d'essai substituée) ; commande `demonstrations/ideation_v59.py … --generations 2` ; montant vérifié 305 USD ; `POLE_MACHINE_JETABLE_V56=1` posée comme **déclaration d'essai** (jamais en réel ; code qui refuse si le moteur est réel) ; au manifeste de fin, coûts de chaque génération et bilan de la course de l'orchestrateur relu **par comptes seulement** (aucun verdict, aucun contenu de fiche : `bilan_allume`, l. 2854).

### Preuve « éteint = v9 » (`essai-a-blanc-v1/comparaison-eteint-v9-v10.json`)

Essai à blanc v9, dossier renommé, puis essai à blanc v10 éteint **au même chemin**. Le manifeste de départ v9, après neuf substitutions nommées, est **égal au caractère près** au manifeste v10 sans `interrupteurs_v10`. Les substitutions : identifiant de run, horodatage, chemin, version et empreinte du lanceur ; puis les empreintes qui en dérivent, chacune admise **seulement** si son fichier est égal aux substitutions précédentes près : contre-lecture d'essai (elle cite le lanceur), acte de gel, configuration servie, empreinte de configuration de l'orchestrateur. Sorties de l'orchestrateur égales à l'octet (classement, fiches, mémoire, accords, fusions inachevées) ; consommations égales hors durées (horloge) ; manifeste de fin égal sur ses clés comparées (code 0, ce qui a été fait, coûts, écart au devis, plafond, crédits, inventaire : comptes et zéro erreur) ; mêmes clés des deux côtés. Mutation : un manifeste dont la commande dit deux générations est vu comme un écart.

### Essai à blanc allumé (`essai-a-blanc-v1/v10-allume/`)

Code du lanceur 2. Manifestes : départ `95f1f74f9fa8a3a36f07de6f66ac00204c541aa2695a1073f48e0eb7cc9b42fc`, fin `5724fa3844b8f677dcd8fa9b973491954887a6ba9967c6522ee6e242fc070409`. Génération 1 jouée (110 fiches classées, 3,85 USD fictifs) ; étage joué (2 candidates, **2 refusées à l'étage** : « fiche sans champ test_de_mort », 0 testée) ; sélection scellée vide (`ca6df204a0ff3de2bff84d40f479b8ea91026a6452d2613adf2d0037af022ed0`) servie à la génération 2 ; génération 2 commencée puis arrêtée : `JSONDecodeError` (bilan de l'orchestrateur `094e8bfc…`, scellé). Contrôles : `essai-a-blanc-v1/v9-temoin/` (code 0) et `v10-eteint/` (code 0).

## 4. Ce qui n'est pas branché, et pourquoi

| manque | où il se règle |
|---|---|
| génération 2 qui lit la sélection : `json.loads` sur du Markdown | orchestrateur (§ 5, point 1) |
| tests de mort sans rien servir (étage après la dernière génération) | orchestrateur (§ 5, point 2) ; la v10 refuse `tests_de_mort_reels` seul |
| budget repris à zéro par génération | lanceur : portée « par_generation » exigée (fait) ; orchestrateur : § 5, point 3 |
| bornes des relais, parts au pire, crédits, porte à blanc, plafond du relais Claude à 150 : calculés pour une génération | lanceur v11 (§ 6) |
| fiches de la course d'auto-conception sans champ de test (projection impossible ; aucun champ inventé) | **nœud** : changer `champs_fiche` change la consigne servie et le préenregistrement |
| machine jetable (R-640) alors que les relais portent les clés sur la même machine | **nœud et dépense** : machine louée, relais hors d'elle ou série sans clé |
| tranche exploratoire réelle et liste blanche | à écrire avec l'additif (aucune pour cette course) |
| bac à sable réel jamais joué avec l'étage v5 | essai réel du bac sur la machine louée (orchestrateur, § 5, point 4) |
| ce qui est servi, et à qui (survivantes, verdict servi ?) | nœuds 2 et 14 de l'ordre v3 ; la v59 sert nom et énoncé des seules « survit » |

## 5. Plan pour une version d'orchestrateur à part (proposée « v68 » ; fichiers neufs, R12, rien de la v56 à la v67 touché)

1. **`pole/course2_v68.py`** : classe `GenerationV68(GenerationV56)` qui redéfinit `_heritage_garde` : si l'héritage est le texte de `heritage_depuis_selection` (marqueur de tête exact et empreinte de sélection citée), le passer ligne par ligne à la garde A4 (`fv.trouver` sur chaque ligne ; ligne exclue ou arrêt selon `a4_action`, comme la v54), sinon la lecture JSON de la v54 inchangée ; redéfinir `_proposer` (copie de la v54, l. 135-166) pour prendre le titre de la section servie dans un attribut (`TITRE_HERITAGE_SELECTION` = « Fiches retenues par l'étage de tests de mort de la génération précédente (nom et énoncé) ») au lieu de « titres, résumés, verdict agrégé ». Fonction `executer_course_v68(conf, sortie, adaptateurs, *, nombre_generations, go, etage, lecture_selection: bool, etage_apres_derniere: bool, …)` :
   - `lecture_selection=True` : la v59 avec `GenerationV68` ;
   - `lecture_selection=False` : **aucun héritage servi** (`heritage_texte=None` pour toute génération ; la mémoire anti-redite seule passe, elle n'est pas servie), et l'étage joué après chaque génération **y compris la dernière** si `etage_apres_derniere=True` (`g <= nombre_generations`) ; c'est le chemin « tests de mort réels sans rien servir » que demandent la plupart des lignes ;
   - refus, avant toute génération : `nombre_generations > 1` en portée « course » (point 3) ; lecture sans étage ; étage sans machine jetable (v56, inchangé).
2. **Étage après la dernière génération** : dans `executer_course_v68`, `preparer_generation(sortie/"etage-apres-generation-g", …)` puis `jouer_etage_v57` pour la dernière génération aussi ; la sélection est écrite et scellée, jamais servie (bilan : `heritage_servi_a_la_suivante: null`).
3. **Budget** : soit le refus ci-dessus, soit un `BudgetV68` qui reçoit le cumul des générations précédentes (et le coût de l'étage) et l'ajoute avant la règle d'A1 ; je recommande le refus (plus simple, la portée « par_generation » couvre le besoin).
4. **`demonstrations/ideation_v68.py`** : le lanceur v8 chargé à part (comme `ideation_v59.py`), avec `c2.executer_course_v56 = course2_v68.executer_course_v68` et deux options lues par `construire_analyseur` étendu : `--lecture-selection {oui,non}` (aucun défaut si `--generations` > 1) et `--etage-apres-derniere`. Le montant de `--verifier-seulement` compte alors N étages si l'étage suit la dernière génération (`montant_requis` à étendre : N × S17 + N × plafond de l'étage).
5. **Essais** (`essais/test_v68_course2.py`) : course de deux générations en moteur simulé, sélection non vide (fiches simulées **avec** champ `test_de_mort` à bloc `statistique`, exécuteur factice), la génération 2 reçoit le texte de sélection, titre neuf, A4 sur l'héritage (cas sain, ligne interdite exclue, arrêt) ; `lecture_selection=False` : aucune consigne de la génération 2 ne contient de section d'héritage, étage joué après la dernière génération ; refus de la portée « course » à N > 1 ; R12 sur les fichiers v56, v57, v59 (empreintes) ; **un essai de bout en bout par le lanceur `ideation_v68.py`** (celui qui a manqué à la v59).
6. **Bac à sable réel** : rejouer `essais/test_v52b_borne_memoire.py` et un étage v5 réel sur la machine louée, avant tout GO de l'étage (supposé de `tests_de_mort_v3.py`).

## 6. Plan pour le lanceur v11 (après la v68, l'additif et le mot de Lazar)

Épingler l'orchestrateur v68 ; `LANCEUR_ORCHESTRATEUR_ALLUME = demonstrations/ideation_v68.py` et ses options ; autoriser `tests_de_mort_reels` seul (`--lecture-selection non --etage-apres-derniere`) ; bornes des relais Gemini et d'Astra, parts au pire et relevé des crédits multipliés par N, plus les appels de l'expérimentateur et du lecteur de l'étage (`executions_par_fiche` × `nombre` × N) ; plafond du relais Claude porté au montant requis ; porte à blanc inchangée ; bilan de coût sur toutes les générations et les étages (fait en v10 pour les générations) ; `POLE_MACHINE_JETABLE_V56` transmise **seulement** si l'opérateur l'a posée dans l'environnement du lanceur, avec la référence du devis de location ; tranche et liste blanche épinglées par l'additif ; garde « fiches projetables » exigée vraie ; une seule ligne de GO pour la course allumée (périmètre : les interrupteurs ; plafond : le montant requis) ; épinglage de l'additif (`ADDITIF_INTERRUPTEURS`) ; essais repris de la v10.

## 7. Lignes de l'ordre v3 que cela débloque

- **Par la v10 seule : aucun étage réel.** Elle livre la forme de l'activation (interrupteurs, ligne de GO nominative, additif, refus réel), la preuve qu'éteinte elle ne change rien, et le constat du défaut de la v59 — qui, sans ce rang, serait apparu à la première dépense d'un étage payant sur plusieurs générations (rangs 6, 8, 9, 12 : des centaines à des milliers d'USD selon le § 2 de l'ordre v3).
- **Après la v68 (§ 5) et le lanceur v11 (§ 6), sous additif, devis et GO** :
  - tests de mort réels sans rien servir : rangs **1, 2, 4, 10, 11, 14, 18, 21**, et 6 si son oracle lit des lois promues ;
  - lecture de la sélection par la génération suivante (avec tests de mort) : rangs **6, 7, 8, 9** (second temps), **12, 20** (second temps) ; 17 et 19 à vérifier ;
  - avec, pour chacune, les nœuds de l'ordre v3 qui la gardent (points 1, 2, 3, 14 : ce qui est servi) et, pour la course d'auto-conception, le nœud des champs de fiche.
- Réserve (état du code, § 5) : plusieurs de ces lignes jouent leur étage payant sur un monde planté dont les fiches portent loi et test ; leur véhicule est le lanceur de leur banc, qui reprendra les gardes des interrupteurs de la v10.

## 8. Écarts

1. Une commande du shell a contenu un heredoc **vide** (`python3 - "$f" <<'EOF'` suivi de `EOF`), contraire à la consigne « jamais de heredoc » : rien n'a été exécuté ni écrit (sortie : « skip »). Signalé ; aucun autre.
2. Les trois configurations servies à l'orchestrateur (≈ 900 Ko chacune : la matière découpée) sont versées dans `essai-a-blanc-v1/` pour que le contre-lecteur rejoue la chaîne de substitutions sur les fichiers ; poids du dépôt ≈ 3,6 Mo.
3. Les empreintes de quinze fichiers de l'orchestrateur ajoutées à l'épinglage ont été lues au commit a41b7b50 (`git show`) et sur disque (égales).
4. Les valeurs de l'étage dans la configuration des interrupteurs (2 candidates, 3 exécutions, 120 s, 1 024 Mo, 5 USD, modèles de l'expérimentateur et du lecteur) sont celles de l'essai à blanc, pas un réglage : l'additif les fixera.
5. L'essai « éteint = v9 » compare deux essais faits à quelques secondes d'écart ; le commit du dépôt de travail peut changer entre eux (d'autres agents committent) : substitution nommée prévue, non requise lors des essais versés.
6. Suite entière des essais du dépôt non rejouée ; seuls les essais v9 et v10.
