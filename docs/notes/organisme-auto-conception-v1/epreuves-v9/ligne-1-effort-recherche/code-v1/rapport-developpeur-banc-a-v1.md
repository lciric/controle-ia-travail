# Banc A de la ligne 1 (« l'effort de recherche compté dans le seuil de promotion ») — rapport du développeur, code v1

Auteur : développeur unique du code du banc, « modèle L′ ». Date (`date -u`) : 2026-11-19, écrit entre 15:09 et 15:25. Étage sur processeur seul : aucune dépense, aucun appel de modèle, aucune connexion.

## 0. Verdict

Le code du banc, ses essais et la commande de lancement sont écrits ; **42 essais sur 42 passent** (gardes A1 à A17 chacune sur un cas sain et sur un artefact, essais 1 à 11 de l'annexe A, dépôt) ; l'essai de fumée de toute la chaîne (étalonnage → course décisive → rejeu → analyse → empaquetage), sur des racines disjointes, passe en 45 secondes, rejeu identique au bit près. **Rien n'est lancé** : ni étalonnage, ni audit, ni course décisive. Aucun écart voulu au préenregistrement ; **dix-huit choix que le préenregistrement ne fixe pas à la lettre** sont dits au § 4, dont **cinq touchent le fond et demandent la décision de la mère avant tout lancement** (4.1 à 4.5).

## 1. Ce qui fait foi, ce qui est vérifié

- Préenregistrement : `prereg/organisme-auto-conception-v9/preenregistrement-ligne-1-effort-recherche-v5.md`, sha256 `523adfd75333d7f2e99a6fe4f868c7dc6982a67e51953734f40258d7a40fc0b9`, commit de scellement `7dcd6a44c777f3aea55b5c68ef8547f9f83438fa` (2026-11-19T14:27:16Z), clé PREREG-ORGANISME-V9-LIGNE-1 (R-3879). Lu par `git show refs/remotes/origin/main:…` après `git fetch -q --depth=1`, empreinte vérifiée. Le code cite ce chemin et cette empreinte dans chaque module ; `banc_ligne1_v1.verifier_preenregistrement` lit le fichier (arbre de travail, sinon le commit de scellement, sinon la copie à l'octet du compte) et **refuse de tourner** si l'empreinte diffère (essai `test_preenregistrement_cite_et_verifie`, cas sain et artefact).
- Organisme : dépôt `ideation-organism`, commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, les neuf fichiers de `orchestrator/pole/` de la liste du préenregistrement, empreintes toutes conformes (relues par programme à chaque lancement : garde A1). Importé **en lecture seule** par chemin (`--organisme`), `python3 -B`, `PYTHONDONTWRITEBYTECODE=1` ; vérifié après coup : aucun `__pycache__` ni fichier modifié dans ce dépôt (`git status` vide).
- **Lieu du code.** Le préenregistrement fixe à la lettre (annexe A) le dossier `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/code/` et les noms de fichiers ; le mandat proposait `src/controle_ia/epreuves_v9/banc_a_ligne_1/` et `tests/`. **J'ai suivi le préenregistrement** (il prime, à la lettre) : mêmes noms que l'annexe A, essais sous `code/essais/`. Conséquence : la commande générale `python -m pytest -q` du dépôt ne les ramasse pas (son `testpaths` est `tests/`) ; on les lance par leur chemin (commande au § 5).

## 2. Correspondance préenregistrement → code, section par section

| section du préenregistrement | où dans le code |
|---|---|
| Monde planté : 3 issues, 2 traits, 2 sous-populations, 8 lignées, rôles permutés par course (même permutation dans les deux classes) | `banc.objets_communs` (rôles : clé tirée par lignée, tâche « course \| lignée \| role », lignées triées) ; `configuration_ligne1_v1.json`, `monde.roles` |
| Mondes à effet (`loi_softmax_aleatoire`, force étalonnée) ; sans effet (issues indépendantes, marginale de Dirichlet (4, 4, 4)) | `banc.objets_communs`, `banc.monde_sans_effet` |
| Hypothèse vraie (poids bruités, écart-type 0,25 × force) ; diffuse (softmax tirée, force 1,0) | `banc.objets_communs` |
| Variantes `transformee` (puissance U[0,4 ; 1,6], inclinaison N(0 ; 0,3) issues 2 et 3) ; tranchantes `si_sinon` (trait, seuil s ± U[−0,15 ; 0,15], confiance c, marginale de la tranche hors région) | `banc.variantes` |
| Tranche exploratoire de 400 épisodes, commune aux classes, lue par le seul proposeur | `banc.tirer_tranche` (comme `a_blanc_v59.creer_tranche`) |
| Proposeurs : 6 générations, 2 ou 12 engagements par appel, tri par la statistique du test de mort sur la tranche, tout transmis dans cet ordre | `banc.jouer_course_pleine` (`statistique_test_de_mort`, tri stable décroissant) |
| Texte d'une carte, mot par mot, zéro « +0.00 » | `banc.texte_carte`, `banc.ecrire_valeur` |
| Étage 1, mémoire anti-redite : **une seule voie** `jaccard(bardeaux(texte brut, 3), …)`, liste par lignée, refusés compris, `s + 1e-12 >= 0,6` | `banc.similarite` (seule définition), `banc.decider_memoire` |
| Étage 2, règle « affinage » (rayon 0,02, au plus une dérivée par appel) | `banc.derive`, `banc.decider_affinage` |
| Étage 3, quota d'aiguillage (2) | `banc.decider_quota` |
| Course pleine calculée une fois, rejouée par chaque bras | `banc.jouer_course_pleine`, `banc.jouer_bras` |
| Jugement : appel pour appel `a_blanc_v59.juger_carte`, tirages et niveau en paramètres ; cache par (tâche, empreinte de l'engagement) | `banc.juger`, `banc.juger_banc` ; un jugement par carte de la course pleine, partagé par tous les bras ; confirmations du bras c gardées par tâche |
| Bras a, b, c, d, a′, T0, d-E1, d-E2, d-E3 ; copie profonde des issues | `banc.regle_e_bh` (appelle `cycle.appliquer_multiplicite` de l'organisme), `banc.regle_bonferroni`, `banc.regle_seule`, `banc.choisir_c`, `banc.jouer_bras` |
| Garantie de d, a′, b | éprouvée par le jouet analytique (essai 8) |
| Registre des essais, définition E0 (réception) ; E1, E2, E3 ; m porté à m_s, compté | `banc.numeroter`, `banc.m_par_definition`, `jouer_bras` (`m_portes_a_m_s`) |
| Deux vérités ; oracle sur 4 000 instances fixées par monde ; vraie ≥ 0,005, fausse ≤ 0, indéterminée entre | `banc.gain_oracle`, `banc.etiquette_oracle` |
| Métriques M1-nul, Δa, M1-oracle, M2 (par lignée, par essai, par famille), M3 sous deux conventions et par force, M4-nul, M5, D1 | `analyse.mesures_course`, `analyse.mesures_classe_course`, `analyse.analyser_sorties`, `analyse.m5_par_generation` |
| Bornes unilatérales à 97,5 % par 10 000 rééchantillons des courses, appariés | `analyse.Reechantillonnage` (une matrice de comptes, tirée une fois, partagée par toutes les métriques) |
| Seuil (« dépasse », « tient », « indécis » ; Δa positif ; δ = 0,05 sous deux conventions) | `analyse.mot_niveau`, `analyse.mot_d_contre_c` |
| Critères de lecture gelés, lignes 0 à 7 | `analyse.appliquer_table` |
| Mentions obligatoires ; prédictions P1 à P11 | `analyse.analyser_sorties` (tout est écrit dans la lecture scellée), `analyse.predictions` |
| Audit de symétrie (points lus en premier ; courses 0, 300, 599 rejouées par un programme à part) | `analyse.points_audit` ; `rejouer_journal_ligne1_v1` (programme à part), étape `rejouer` du lanceur |
| Lecture de sensibilité d-E1, d-E2, d-E3, sans verdict | bras `d_E1`, `d_E2`, `d_E3` ; `analyse` (« sensibilite »), hors table |
| Journal scellé des décisions (entrées exactes, table des objets, chaîne d'empreintes, un fichier par course et par classe, tronc puis bras) | `journal_ligne1_v1.Journal` ; appels dans `jouer_course_pleine` et `jouer_bras` |
| Rejeu au bit près (A16) | `rejouer_journal_ligne1_v1.rejouer_fichier`, `rejouer_dossier` |
| Tailles (600 courses par classe, 400 d'étalonnage), graines (racines 2026111900 à 2026111903, `boucle_fermee_v59.graine_de_tache`) | `configuration_ligne1_v1.json` ; `banc.Graines` (consigne la première dérivation par racine) |
| Manifeste de course | `lancer.decisive` (`manifeste-course-decisive-ligne1-v1.json`) |
| Ordre des gestes 3 à 8 | `lancer.tout` (étalonnage → décisive → rejeu → analyse ; chaque étape scelle avant la suivante) |
| Étalonnage : dichotomie des forces, grille (s, c), 400 courses par classe rejouées par T0 seul, portes, part des indéterminées | `etalonnage_ligne1_v1` (`dichotomie`, `etalonner_forces`, `etalonner_grille`, `jouer_courses`, `lire_courses`, `porte_prise`, `porte_cartes_par_appel`, `exiger_portes`) |
| Audit du générateur (trois traits, deux étiquettes, régression paire → impaire, intervalles à 95 % sur 1 000 rééchantillons, aires nommées hors plage) | `etalonnage.audit_generateur`, `auc_ponderee`, `ajuster_logistique` |
| Sortie de l'étalonnage dans un fichier à part, nom neuf, cité par le manifeste | `sortie-etalonnage-ligne1-v1.json` ; le manifeste en porte le chemin et l'empreinte |

## 3. Gardes et portes : où, et leurs essais (règle R5)

| garde | où | cas sain | artefact (celui du préenregistrement) |
|---|---|---|---|
| A1 | `banc.verifier_empreintes_organisme`, `charger_organisme` (et contrôle des fichiers effectivement chargés) | les neuf fichiers | un octet changé dans une copie de `cycle.py` |
| A2 | `banc.installer_garde_a2` (toute connexion refusée ; import d'un client de modèle ou d'un adaptateur de l'organisme refusé) | un jugement passe | `socket.create_connection`, `socket.connect`, import de `anthropic` et de `pole.adaptateurs_v56` |
| A3 | `banc.verifier_appariement` | course d'essai | une lignée ôtée d'une classe ; une tranche tirée avec la classe dans sa tâche |
| A4 | `banc.numeroter` | génération 1 | un essai refusé retiré du registre |
| A5 | `banc.regle_e_bh` | bras d | m abaissé d'une unité |
| A6 | `banc.verifier_jugement_identique` (dix lois ; appelé avant toute étape par le lanceur) | dix lois identiques au bit près | un instant de lecture ajouté |
| A7 | `analyse.analyser_sorties` (lecture refusée, ligne 0) | indéterminées nulles | seuil de vérité déplacé |
| A8 | `etalonnage.audit_generateur`, `exiger_portes` | traits sans fuite | le rôle écrit dans l'identifiant |
| A9 | `etalonnage.dichotomie`, `porte_prise`, `exiger_portes` | cible atteinte ; prise | cible inatteignable ; T0 sans prise (couple sans effet) |
| A10 | `banc.exiger_fini` (trajectoires, richesses, oracle, métriques) | valeurs finies | NaN ; infini dans une métrique |
| A11 | `analyse.analyser_sorties` | bras a sans fausse promotion | règle remplacée par le seuil seul |
| A12 | `analyse.verifier_scellement_avant_analyse` | mini-chaîne de deux courses, analyse complète | empreinte du programme changée au manifeste ; sortie brute non scellée |
| A13 | `lancer.surveiller` | enfant rapide | plafond à une seconde : arrêt du groupe par identifiant, arrêt écrit, processus disparu |
| A14 | `lancer.verifier_derivations` | dérivation après le scellement | manifeste planté avec une dérivation antérieure |
| A15 | `etalonnage.porte_cartes_par_appel`, `exiger_portes` | écart 0,05 | mémoire réglée à 0,1 dans la seule classe « peu » (course réelle) |
| A16 | `rejouer_journal_ligne1_v1` | journaux d'essai, toutes décisions identiques | une trajectoire modifiée ; une ligne ôtée |
| A17 | `banc.jouer_bras` (contexte d'étalonnage), `etalonnage.verifier_sortie_sans_bras_interdit` | T0 joué | bras a calculé pendant l'étalonnage ; sortie contenant un bras a |

Portes de l'étalonnage : prise (A9), cartes jugées par appel (A15), audit (A8) ; chacune écrit sa sortie scellée puis lève sa garde nommée ; la part des indéterminées est mesurée sans porte, mise en tête au-delà de 20 % (la course décisive refuse alors de partir : `DecisionMereRequise`). Aucun repli silencieux : chaque garde lève une exception nommée.

## 4. Choix que le préenregistrement ne fixe pas à la lettre

Aucun n'est un écart voulu à une règle écrite ; chacun comble un silence. **4.1 à 4.5 touchent ce qui est jugé ou lu : je demande que la mère les tranche avant tout lancement** (la consigne dit « arrête et rapporte » : je n'ai rien lancé ; le code est versé pour la contre-lecture). 4.6 à 4.18 sont des choix de code sans effet attendu sur une règle.

1. **Largeur fixe du texte.** Le préenregistrement exige à la fois « +0.00 » pour toute valeur nulle et une « largeur fixe » : seule la forme « %+.2f » les concilie, ce qui suppose des valeurs de moins de 10 en valeur absolue. Une valeur de 10 ou plus (poids × puissance, possible si une force étalonnée dépasse environ 1,5) allongerait le texte d'un caractère. Le code **n'arrête pas** (ce n'est pas une garde du préenregistrement) : la constance des longueurs est une vérification de construction rapportée (`longueurs_de_texte` dans la sortie de l'étalonnage et dans la lecture). Sur les courses d'essai : longueur constante (93 et 51 caractères).
2. **Confiance des lois tranchantes** : « la confiance c sur une issue tirée au hasard » ; le reste, (1 − c)/2 sur chacune des deux autres issues (comme le programme de chronométrage de l'annexe B : [0,75 ; 0,125 ; 0,125]).
3. **Marginale de la tranche** : hors de la région, fréquences brutes (comptes / 400) ; la statistique du test de mort (D1 et tri du proposeur) garde le lissage à 0,5 du script de l'expérimentateur, comme `TEST_DE_MORT` le fait.
4. **Engagement de confirmation du bras c** : niveau déclaré dans l'engagement neuf = 0,05/6 (son seuil 1/α vaut alors log(6/0,05), celui de la promotion) ; tâche « …|carte=<id>|confirmation » ; 100 instances d'entraînement, comme `juger_carte`. Le niveau entre dans l'empreinte de l'engagement, donc dans la graine des tirages frais : un autre choix donnerait d'autres tirages, sans changer la validité.
5. **Audit, étiquette d'effet** : les cartes « indéterminées » sont **hors** des aires de l'étiquette d'effet (vraie contre fausse), comptées dans la table croisée. Autre voie possible : les compter comme non vraies.
6. Ordre d'arrivée des lignées : leur indice dans la course ; numérotation du registre propre à chaque génération (1 à m_r), comme m.
7. Ex æquo du tri du proposeur : ordre de génération des variantes (tri stable).
8. Hypothèses et paramètres des variantes arrondis à 6 décimales, comme les lois aléatoires de l'organisme ; gain d'oracle non arrondi (`a_blanc_v59.oracle` arrondit à 6 décimales pour l'affichage).
9. Cartes des mondes sans effet : étiquetées « fausses » sans calcul de gain (par l'inégalité de Gibbs, leur gain est négatif ou nul).
10. Générateurs : `random.Random` graine par `graine_de_tache` (comme l'organisme) ; loi de Dirichlet par `gammavariate` ; rééchantillonnages par `numpy.random.default_rng(graine_de_tache(2026111903, tâche))`, percentiles linéaires de numpy ; une seule matrice de rééchantillonnage pour toute la lecture (tâche « reechantillonnage\|courses\|lecture »), d'où l'appariement de tous les écarts.
11. Étalonnage des forces : un monde neuf par jugement **et par pas** (tâche avec la cible et le numéro du pas) ; force non arrondie.
12. Régression de l'audit : traits centrés réduits sur les courses paires, maximum de vraisemblance sans pénalité, pas de Newton par moindres carrés (le numéro du premier essai de l'appel vaut 1 + n × rang de la lignée en course pleine : il est colinéaire au rang). Aires par les rangs, ex æquo pour moitié.
13. Opérations des prédictions : « ordre inverse au-delà des intervalles » (P6, P11) = borne haute de l'écart apparié sous 0 pour une paire voisine ; P8 démentie si la borne basse (tranchantes, tranche relue) est à 0 ou dessous ; P4, P5, P7, P9 sur les bornes que leur colonne nomme.
14. « c tient le niveau » (condition de « c domine ») : lu dans la classe « beaucoup », comme les autres quantités du bras c.
15. M2 « par essai » : rapport des sommes sur toutes les courses.
16. Garde A14 : chaque étape dérive d'abord, dans le processus parent, une graine « ouverture\|… » de sa racine, pour que l'horodatage consigné soit le plus précoce ; A3 compare aussi la tranche fraîche de D1.
17. Renforcements : le rejeu porte aussi sur les journaux des 800 courses d'étalonnage ; le lanceur refuse un code non commis (hors fumée) et une course décisive dont le code diffère de celui de l'étalonnage.
18. Compression xz (préréglage 6, déterministe), choisie parce que gzip donnait environ 1 Mo par course (plus de 500 Mo au total) ; le journal reste une ligne JSON par entrée.

## 5. Essais : décomptes

Commande : `PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B -m pytest -v -p no:cacheprovider essais/test_banc_ligne1_v1.py` depuis `code/`. **42 essais, 42 passent, 0 échec**, 66 secondes (sortie : `sortie-essais-banc-a-ligne1-v1.txt`). Répartition (9 + 17 + 13 + 3 = 42) : essais 1 à 3, 5 à 8, 10 et 11 de l'annexe A, un essai chacun (9) ; essai 4 : 17 essais de gardes, A1 à A17, chacun cas sain et artefact, portes comprises (le cas sain de A6 est l'essai 1, son artefact a son propre essai) ; essai 9 : 13 jeux (8 lignes de la table, 5 jeux de plus) ; préenregistrement cité et vérifié (1) ; dépôt en morceaux (1) ; aucune racine d'étalonnage, décisive ni de rééchantillonnage dérivée pendant les essais (1, dernier). Racine des graines : 2026111900 seule.

R4 (trop beau) : tous ont passé dès le premier passage. J'ai vérifié que chaque artefact fait bien tirer sa garde (`pytest.raises` sur l'exception nommée) et relu des comptes de deux courses d'essai : refus par étage et par rôle, cartes jugées par appel (1,94 contre 2,0 : écart 0,06, sous la porte de 0,1 mais proche d'elle), longueurs de texte constantes.

## 6. Durées : mesurées sur la fumée, extrapolées

Fumée (`sortie-fumee-banc-a-ligne1-v1.txt`) : 4 processus sur 4 cœurs ; 45 secondes de bout en bout ; une course décisive (deux classes, neuf bras, journaux et sorties compressés) prend **9,1 à 11,6 secondes** de calcul quand quatre tournent ensemble (8,1 secondes seule, en gzip) ; rejeu de 26 journaux en 11,7 secondes.

Extrapolation à la taille du préenregistrement, 4 processus :

| poste | compte | durée prévue |
|---|---|---|
| forces et grille | 64 000 + 48 000 jugements au plus (5 à 6 ms chacun, annexe B) | 3 à 4 minutes |
| 400 courses d'étalonnage par classe (T0 seul) | 400 courses × 9 à 10 s / 4 | 15 à 17 minutes |
| audit du générateur (1 000 rééchantillons, ~16 aires) et lecture des sorties | — | 2 à 5 minutes (non mesuré à cette taille) |
| 600 courses décisives par classe | 600 × 9 à 11,6 s / 4 | 23 à 29 minutes |
| rejeu (1 200 journaux décisifs + 800 d'étalonnage + 6) | — | 8 à 15 minutes |
| analyse (10 000 rééchantillons) | — | 2 à 5 minutes (non mesuré à cette taille) |

**Total prévu : environ 1 heure (45 minutes à 1 heure 30) sur quatre processus ; environ 3 heures 30 à 4 heures sur un cœur.** Dans la fourchette de l'annexe B pour quatre cœurs (35 à 70 minutes) ; légèrement au-dessus de sa borne haute sur un cœur (3 heures 30), à cause de la compression et du rejeu des journaux d'étalonnage. Plafond A13 : 12 heures, loin.

## 7. Taille des journaux et dépôt (R-3851)

Mesuré sur la fumée : 407 Ko compressés par course décisive (journal « beaucoup » 249 Ko, « peu » 74 Ko, sorties 64 et 19 Ko), 387 Ko par course d'étalonnage ; avant compression, 4,8 Mo et 4,1 Mo (le chiffre du préenregistrement, « quelques centaines de mégaoctets avant compression », était trop bas).

**Prévu : environ 245 Mo (décisive) + 155 Mo (étalonnage) + moins de 5 Mo de fichiers JSON ≈ 400 Mo compressés**, environ 4,5 Go avant compression. C'est **sous le plafond de 500 Mo, avec une marge de 20 % seulement**. Dépôt : `lancer_ligne1_v1.py empaqueter` met les fichiers déjà compressés en morceaux tar de 90 Mo au plus (cinq morceaux attendus), compagnons `.sha256`, manifeste scellé `manifeste-depot-ligne1-v1.json` ; il refuse au-delà de 500 Mo (`DepotTropGros` : arrêt et rapport avant de pousser). Éprouvé sur la fumée (un morceau de 4,2 Mo) et par l'essai du dépôt. Le lieu (branche du compte, ou archive hors dépôt dont l'empreinte est dans le dépôt) reste à fixer par la mère avant la course décisive (préenregistrement) ; si la marge paraît courte, les journaux d'étalonnage (155 Mo) peuvent aller hors dépôt.

## 8. Commande de lancement

Dans `commande-lancement-banc-a-ligne1-v1.md` (avec reprise, suivi, arrêt par identifiant, empaquetage). La commande unique, détachable et reprenable :

```
D=/home/user/runs-banc-a-ligne1-v1 ; mkdir -p "$D" && cd /home/user/controle-ia-travail && setsid nohup env PYTHONDONTWRITEBYTECODE=1 /usr/local/bin/python3 -B docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/code/lancer_ligne1_v1.py tout --sortie "$D" --organisme /home/user/ideation-organism/orchestrator --processus 4 > "$D/lanceur.log" 2>&1 < /dev/null &
```

## 9. Réserves

1. Le code n'a été contre-lu par personne ; la contre-lecture par l'autre modèle vient ensuite (règle R2). Les cinq choix 4.1 à 4.5 sont à trancher avant le lancement.
2. Le jugement est une réécriture de `juger_carte` : identité au bit près vérifiée sur dix lois (A6), pas sur toutes les lois du banc ; le rejeu (A16) vérifie ensuite chaque jugement du banc contre lui-même, non contre `juger_carte`.
3. L'écart de cartes jugées par appel entre classes est proche de la porte A15 sur deux courses d'essai (0,06 pour 0,1) : la porte peut tirer à l'étalonnage ; ce serait alors un arrêt, retour à la mère, sans changement du code.
4. Les durées d'audit et d'analyse à pleine taille ne sont pas mesurées.
5. La fumée a lu ses propres portes et métriques par programme pour éprouver la chaîne ; je n'ai lu que des durées, des tailles, des comptes et des sceaux.

## 10. Fichiers (nouveaux ; empreintes)

Code, sous `docs/notes/organisme-auto-conception-v1/epreuves-v9/ligne-1-effort-recherche/code/` :

| fichier | sha256 |
|---|---|
| `configuration_ligne1_v1.json` | `f4972d1833a955d91576a5d76252bb7e83dae3e25d7e05808e9a2e68cd89d809` |
| `banc_ligne1_v1.py` | `ccc97ea2d0cee6d0e9ef08cb0e28699aab11fb424fef3f4f22676a30bbd549ba` |
| `journal_ligne1_v1.py` | `d1506aec4ce601da1054b52231aeeca2142c8a8759a318c312a587316bb477fa` |
| `rejouer_journal_ligne1_v1.py` | `369c7b3d1dccec134a8c35afa44f4d8bc9a15eac1a14dd932f2767b15121bc82` |
| `etalonnage_ligne1_v1.py` | `d7c1592dce5ed6c9af9b056e8e71696401313458adb51aaddac8ce6d20fec5dd` |
| `lancer_ligne1_v1.py` | `4b0d4759aba45a1f32768b22424079d85f0c6710ba35c1704d402831b3391fad` |
| `analyse_ligne1_v1.py` | `6c03cfa27cb87580e7895b45531db44e6c04148d1debbf9a633a11b318bd98a3` |
| `essais/test_banc_ligne1_v1.py` | `deb31990ab1c375c93c5ab13a315a48bb9f3917f3111e2cde560043b2797e305` |

Livrables, sous `…/ligne-1-effort-recherche/code-v1/` : ce rapport ; `commande-lancement-banc-a-ligne1-v1.md` (`9840580209bd84abd15aa3795225c65cacbb6044a1a2df7f7f15392cdf7b2ef3`) ; `sortie-fumee-banc-a-ligne1-v1.txt` (`144d41165886e4c45920efc3be750855cec0875503478b3a93cfb729e7ec631e`) ; `sortie-essais-banc-a-ligne1-v1.txt` (`e81fd3a303c9987653ade1e9c6596c1ab8e814df9b174b9ef41b8e8788de9bfe`). Chaque fichier porte son compagnon `.sha256`. La fumée a tourné sur exactement ces empreintes de code (manifeste de la fumée, champ `code`).
