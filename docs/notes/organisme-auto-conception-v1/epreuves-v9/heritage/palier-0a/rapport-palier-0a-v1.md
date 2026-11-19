# Héritage — palier 0a : lecture du code de l'étage des tests de mort et essai hors ligne sur des lois plantées — v1

- **Écrit par** le développeur du palier 0a (modèle L′), le 2026-11-19, de 14:20Z à 14:40Z environ (`date -u`). Sur processeur seul, hors ligne : aucun appel à un fournisseur, aucun relais, aucun appel de modèle, aucune dépense.
- **Mandat** : ligne `GO-2026-11-19-71` (paliers 0a et 0b, 0 USD ; R-3874), lue par la mère. Objet : plan `plan-heritage-trois-bras-corrige-v4.md` (`6b0fd0650907c383e19f4548933604f0fa1b39889d8f6e721368f2b52de752f5`), § 8.4, ligne 0a, et réserve 1 du § 13 ; devis `devis-heritage-trois-bras-v4.md` (`94698b6192322de220eb151a6ea0312d6e86712a57fdf057232db0c31b0542ea`), § 3 à § 5. La version 5 du plan, en cours chez un autre agent, n'est ni lue ni touchée.
- **Statut** : vérification d'instrument, **pas une expérience décisive**. Aucune lecture sur l'héritage, aucun bras, aucun proposeur. Les tentatives et les scripts sont écrits par programme (doublures scriptées de l'orchestrateur), jamais par un modèle.
- **Bases** : orchestrateur `/home/user/ideation-organism` au commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`, **lu seulement** (arbre resté propre : `git status --porcelain` vide après l'essai) ; travail sur une copie neuve sous le bloc-notes, où seul un dossier neuf `palier-0a/` a été ajouté (aucun fichier existant modifié ; les seize fichiers employés ont la même empreinte que l'original, manifeste). Dépôt de travail : branche `lot/compte-organisme-v1`, commit `5b32b99e06e353a3d8feb6cabc68724eb0121400` au moment de l'écriture.

## 0. Verdict

**(a) Oui.** L'étage des tests de mort, **version 5** (`pole/tests_de_mort_v5.py`, `da524871b9b498693d67cc099240acb98c4c84c800ee4c69f0a1cb5fe60b64f1`, verdict calculé par le noyau), **sans un octet changé**, a exécuté des engagements portant sur les lois plantées du monde planté de l'organisme (loi vraie S-V1 ; lois fausses S-F1, S-F2, S-F4 ; anti-loi), par le chemin déjà écrit du tour fermé (`tour_ferme_v64.jouer_etage` → `preparer_generation` v53 → `jouer_etage_v57` → étage v5), **dans l'exécuteur factice puis dans le vrai bac à sable `bwrap` local** (bubblewrap 0.9.0, utilisateur dédié sans compte, groupe de contrôle de mémoire, filtre d'appels système, réseau isolé ; sonde complète réussie). Les deux exécuteurs rendent des verdicts, des valeurs et des copies du fichier brut identiques à l'octet (`factice_contre_bwrap.identiques` : vrai).

**(b) Oui, pour le verdict ; oui pour l'appariement, dans la forme existante et avec deux manques.** (b1) Le verdict est calculé par le noyau sur la copie scellée du fichier brut (`gains.csv`, colonne `gain`, moyenne, seuil scellé) ; aucun modèle n'y entre : ma reprise indépendante de la moyenne sur la même copie donne un écart de 0,0 et le même verdict pour les six tentatives testées ; le lecteur témoin et le chiffre imprimé sont consignés, non décisifs. (b2) Le comparateur de l'oracle (`oracle_tour_ferme_v60`) apparie, **par calcul seul**, la loi relue dans le préenregistrement court **scellé** de chaque tentative à la loi plantée dont elle est issue (divergence moyenne 0 nat à la sienne, au moins 0,63 nat à toutes les autres, seuil de l'oracle 0,05 nat). **Deux manques** pour l'usage que le plan en fait (§ 3 ci-dessous) : l'étiquette existante `loi_plantee_retrouvee` dépend de la **promotion par le juge statistique** (inutilisable telle quelle sous N-058 et le § 3.1 du plan) ; et l'organisme n'a ni générateur de mondes à **plusieurs** lois vraies composées (dose ρ, source et cible), ni comparateur qui apparie une tentative à **une** loi parmi plusieurs qui composent un monde.

**Règle de passage du § 8.4 : « oui aux deux »** ⇒ le palier 0b peut se préparer **sur la voie (b)** (les tests de mort) ; la voie (c) (épreuve neuve) n'a pas à être portée à Lazar pour une raison d'instrument. Les manques du § 3 sont du **code sans dépense hors de l'étage** (générateur, comparateur sans juge, tranche d'épreuve, découpage en lots, garde de l'entrée de l'expérimentateur), à écrire et éprouver au palier 0b. Le nœud 1 reste à Lazar : le palier 0a lève la **réserve d'instrument** (« sous réserve du palier 0a ») et lui apporte un fait neuf, dit au § 4 : sur la forme d'engagement du tour fermé, l'étage tourne de bout en bout avec un **expérimentateur écrit par programme**, sans appel de modèle.

## 1. Preuves (sortie `essai-palier-0a-sortie-v1.json`, `0b73f25cccd5e26beeac479b1aeff0864341b43e76c58b6b0145823f805476d0`)

Monde : `exemples/temoins-pari-demo-v1.json` (`fdf4d5c1ca0d2971b416ee5f694deff7a4696fe5defb3a6a1843dffef1231877`), chargé par `a_blanc_v59.charger_monde` : loi vraie S-V1 (3 issues, 2 traits, 2 sous-populations), lois fausses S-F1, S-F2, S-F4. Tranche : 400 épisodes tirés de S-V1 par l'orchestrateur (`tour_ferme_v64.creer_tranche`), index `2e4bb09671997ca80dd256e1c0f680835ee2114880b28fbe9ff78735c2a9464c`, la même dans E1 et E5. Engagement de chaque tentative : la forme imposée du tour fermé (`test_de_mort_impose`) : fichier `gains.csv`, colonne `gain`, statistique `moyenne`, seuil « au moins 0,02 » (lu par le noyau : `≥ 0.02`), données `episodes.csv` et `evaluateur_lois_v62.py`, la loi gelée en JSON canonique dans le texte du test.

| essai | ce qui est joué | issue (sortie, champ `essais.Ek`) |
|---|---|---|
| E1, exécuteur factice | 7 tentatives : P-V1 (S-V1), P-F1, P-F2, P-F4, P-ANTI, P-V1 au seuil « au moins 2,0 », P-V1 sans bloc statistique | P-V1 **survit** (valeur du noyau 0,515368…) ; P-F1, P-F2, P-F4, P-ANTI **éliminées** (−2,51 ; −0,117 ; −1,10 ; −3,89) ; seuil intenable **éliminée** (même valeur 0,515, `≥ 2` faux) ; sans bloc **refusée à l'étage** (motif du noyau, aucune session). Sélection v57 : P-V1 seule (`b39ce07a…`). Contre-calcul du tour fermé (garde 10, `selection_pari.proba`) : six accords. Recalcul indépendant (moi, sur la copie scellée) : écart 0,0, mêmes verdicts. Lecteur témoin : mêmes mots, aucun désaccord consigné |
| E2, artefact « script qui fabrique ses lignes » | anti-loi, script qui écrit `gain = 0,5` partout | le noyau rend **survit** (0,5 ≥ 0,02) : limite dite dans l'en-tête de l'étage, **non détectée par le noyau** ; le contre-calcul du tour fermé l'**arrête** (`ArretTour` : « contre-calcul en désaccord avec le noyau … (garde 10) : arrêt, aucune issue lue ») |
| E3, artefact « aucune exécution » | S-V1, session marquée « rien envoyé » | **non concluant** (« aucune exécution réussie »), contre-calcul « sans objet » |
| E4, treize tentatives dans un étage | 13 copies de S-V1 | **refus avant tout appel** : `EtageRefuse : tests_de_mort : entier de 0 à 12 (reçu 13)` |
| E5, vrai bac `bwrap` | E1 à l'identique | sonde : « bwrap présent ; sonde OK ; connexion réseau refusée ; écriture hors du dossier de travail refusée ; aucune capacité, pas de superutilisateur (ni sur l'hôte) ; … filtre d'appels système actif, mémoire du bac entier bornée (groupe de contrôle), borne de processus tenue » ; **mêmes verdicts, valeurs et copies du fichier brut qu'en E1** ; aucun groupe de contrôle restant ; dossier racine retiré |

Comparateur (`comparateur` de la sortie) : pour chaque tentative testée de E1, la loi relue dans `prereg-court.json` scellé (sceau vérifié) est **égale** à la loi proposée ; divergences moyennes à chaque loi plantée (oracle v60, 4 000 instances, graine de la tâche « oracle|instances ») :

| tentative | S-V1 | S-F1 | S-F2 | S-F4 | appariée à (≤ 0,05 nat) | `classer(...)["loi_plantee_retrouvee"]` si promue / non promue |
|---|---|---|---|---|---|---|
| P-V1 | 0 | 3,008 | 0,634 | 2,072 | S-V1 | vrai / **faux** |
| P-F1 | 2,933 | 0 | 1,933 | 1,406 | S-F1 | faux / faux |
| P-F2 | 0,680 | 2,716 | 0 | 3,301 | S-F2 | faux / faux |
| P-F4 | 1,423 | 0,755 | 1,907 | 0 | S-F4 | faux / faux |
| P-ANTI | 4,318 | 1,275 | 4,028 | 1,782 | aucune | faux / faux |
| P-V1, seuil intenable | 0 | 3,008 | 0,634 | 2,072 | S-V1 | faux / faux (verdict « éliminée ») |

La dernière colonne montre la dépendance au juge : même loi, même divergence nulle, l'étiquette de l'oracle passe de vrai à faux selon la seule promotion par le juge.

Manifeste : `manifeste-essai-palier-0a-v1.json` (graines, versions, empreintes ; § 7).

## 2. Ce que j'ai lu (copie au commit `a41b7b50`, fichiers égaux à l'original)

| fichier | empreinte (préfixe) | lignes lues |
|---|---|---|
| `orchestrator/pole/tests_de_mort_v5.py` | `da524871` | 1-692 (en entier) |
| `orchestrator/pole/tests_de_mort_v4.py` | `35912a3a` | 1-400 (en entier) |
| `orchestrator/pole/tests_de_mort_v3.py` | `ea05eb55` | 1-42 (en entier) |
| `orchestrator/pole/tests_de_mort_v2.py` | `363a3725` | 1-80 (en-tête), 120-160 et 182 (constantes), 257-383 (seuil, comparaison, validation du champ, préenregistrement court), 386-495 (lectures, statistique de colonne), 578-602 (garde du script), 923-927 (`nom_copie`), 1077-1090 (borne mémoire), 1227-1335 (identité dédiée, constructeur du bac), 1397-1478 (identité, racine de travail), 1571-1610 (exécution, environnement minimal), 2073-2135 (exécuteur factice), 2256-2322 (réglages, plafond de l'étage, tranche) |
| `orchestrator/pole/etage_entre_generations_v53.py`, `_v56.py`, `_v57.py` | `d568d25b`, `f0c80e2d`, `e4bf3681` | en entier (105, 60, 84 lignes) |
| `orchestrator/pole/tour_ferme_v64.py` | `35a8294e` | 1-160 (en-tête, constantes), 258-301 (compteur), 440-530 (texte du test, engagement imposé, carte servie, témoins), 692-786 (rôles, adaptateur de l'étage), 787-906 (statistique hors bac, contre-calcul, tranche, `jouer_etage`), 1034-1068 (divergence, découvertes distinctes), 1290-1395 (doublures scriptées) |
| `orchestrator/pole/a_blanc_v59.py` | `606aa8b4` | 1-165 (en-tête, monde, oracle d'audit, cartes scriptées, gardien), 196-358 (script, vérificateur témoin, adaptateur scripté, tranche, choix de l'exécuteur, étage) |
| `orchestrator/pole/oracle_tour_ferme_v60.py` | `514864b7` | 1-169 (en entier) |
| `orchestrator/pole/evaluateur_lois_v62.py` | `26613fe7` | 1-45, 94-101 |
| `orchestrator/pole/proposeurs_references_v59.py` | `7d00371a` | 29-69 |
| `orchestrator/pole/boucle_fermee_v59.py` | `a2de4865` | 60-77 (graines) |
| `orchestrator/pole/fiches_v53.py` | `7cfcf832` | 43-55 |
| `orchestrator/pole/noyau_v56.py` | `eb5a003e` | 100-110 (budget par génération) |
| `orchestrator/pole/course2_v56.py`, `course2_v59.py` | `14f65569`, `b5a19a47` | lignes qui nomment l'étage (402, 426 ; 67, 91) |
| `orchestrator/essais/test_v52b_borne_memoire.py` | `5e5132b9` | 1-130 ; `essais/test_tour_ferme_v64.py` (`52279163`) 700-725 ; `essais/test_v7_ideation_v2.py` 7945-7976 |

Dans le dépôt de travail : le plan v4 (en-tête, § 3.0, § 5, § 6, § 8, § 13) et le devis v4 (§ 3 à § 5) ; au rang 0 : `rapport-developpeur-rang-0-v1.md` (`966a3870…`), `etat-du-code-rang-0-v1.md` (`f50863be…`), `contre-lecture-rang-0-v1.md` (`f219e7cc…`, lignes qui nomment les manques). **Non lus** : le dossier de la v68, la version 5 du plan, toute carte, tout classement, tout dossier interdit par le mandat, les résultats rangés dans l'orchestrateur.

## 3. Ce que l'étage exige d'un engagement, ce que reçoit l'expérimentateur, ce qui manque

### 3.1 Ce que l'étage v5 exige (refus motivé sinon, jamais de repli)

1. **Une fiche** (`fiches-validees.json`, scellée) avec `identifiant_auteur`, `nom`, `empreinte` égale à celle du classement, `enonce` non vide, `loi_predictive.prediction` **contenant un nombre**, `loi_predictive.signe` ∈ {+, −, 0}, `loi_predictive.metrique` non vide (v2 l. 337-357) ;
2. **le champ `test_de_mort`** : `seuil` (texte, ≤ 200 caractères, un nombre ; le comparateur est **lu dans le texte français**, « au moins », « ≤ »…, ou tiré du signe : v2 l. 257-282), `test` (texte non vide, ≤ 3 000 caractères), `donnees` (1 à 12 chemins **exacts** de l'index de la tranche, empreintes reprises), et le bloc `statistique` **exactement** {`fichier` produit par le script, ni sous `tranche/` ni `script.py` ; `colonne` ; `statistique` parmi moyenne, médiane, somme, minimum, maximum, nombre, part positive, écart-type} (v4 l. 124-143, 168-197) ;
3. **un contexte de course** : `manifeste-depart.json` avec `reglages.tests_de_mort` {nombre, empreinte de l'index de la tranche}, `classement.json` (`lisible_L2_L4` vrai ; lignes `eligible`, `rang`, `empreinte`), tous scellés ; les candidates sont les `nombre` premières lignes éligibles, **au plus 12** (v2 l. 132 ; v5 l. 285-303) ; un étage n'est **jamais rejoué** dans un même dossier (v5 l. 267-271) ;
4. **une tranche** déclarée (index scellé, liste blanche, empreintes ; `charger_tranche`, v2 l. 2302-2313) ;
5. **deux rôles** : un expérimentateur et un lecteur témoin d'étiquettes différentes, plafonds réels > 0, 1 à 20 exécutions, délai ≤ 3 600 s, mémoire ≥ 64 Mo, et ≥ 768 Mo dans le vrai bac (v2 l. 2260-2295 ; v3) ; la déclaration de machine jetable par liste blanche de noms (v56), que l'appelant peut passer comme un dictionnaire explicite (fait ici : `ENV_A_BLANC`, aucune valeur de l'environnement lue) ;
6. **dans le vrai bac sous superutilisateur** : un utilisateur dédié sans compte à interpréteur et sans processus vivant, un dossier racine à lui, 0700, traversable (v2 l. 1397-1478).

Le préenregistrement court est **scellé avant la première session** (v5 l. 450) ; le verdict est `verdict_du_noyau_v5` : dernière exécution réussie, copie scellée du fichier nommé, statistique et comparaison par le noyau, tout incident → « non concluant » (v5 l. 202-220 ; v4 l. 315-362), scellé avant la session du lecteur (v5 l. 616-622). La sélection v57 ne retient que « survit » (v57 l. 207-231). Les trois classes et `gardee` du § 3.0 du plan correspondent donc à la lettre.

### 3.2 Ce que l'expérimentateur reçoit — fixé par le code, non par le plan

La consigne (v5 l. 93-152) sert le **préenregistrement court entier** : hypothèse (`enonce`), **prédiction** {texte, valeur, signe}, métrique, seuil, texte du test, données, bloc statistique, quotas, liste d'arrêt, règles, et les **extraits de la fiche** (`nom`, `enonce`, `loi_predictive` projetée, `test_de_mort`), plus l'index de la tranche et l'historique de ses tours (consigne du premier tour : 10 598 caractères, sept titres, sortie E1). Il peut lire la tranche (jusqu'à 200 000 caractères par fiche). Conséquences pour le § 3.0 du plan :
- la « prédiction » du registre **ne doit pas** être projetée sur `loi_predictive.prediction`, que l'étage exige chiffrée **et sert** ; le tour fermé y met un texte neutre écrit par l'orchestrateur (`carte_servie`), et un titre et une hypothèse neutres (« étage servi à l'aveugle ») ; c'est la voie à reprendre ;
- l'étage **n'a pas** la garde « tout champ du registre hors de la liste gelée arrête l'étage » ; la projection v53 (`CORRESPONDANCE` : six champs) est une liste blanche de fait ; la garde R5 du plan se pose **sur la projection**, hors de l'étage.

### 3.3 Ce qui manque (rien n'exige de réécrire l'étage)

1. **Générateur de mondes de l'héritage** (plan § 5) : l'organisme n'a qu'un monde à **une** loi génératrice (S-V1) et des lois fausses qui ne génèrent rien ; pas de paires source et cible, pas de dose ρ, pas de mondes à plusieurs lois vraies composées. Si le générateur sort de la classe actuelle (3 issues, 2 traits, 2 sous-populations, six types de lois), l'évaluateur servi (`evaluateur_lois_v62.py`, `NOMBRE_ISSUES = 3`), la grammaire du gardien et la statistique hors bac sont à étendre — **couche du tour fermé, pas l'étage**.
2. **Comparateur sans juge** (plan § 6) : `classer` exige `promue` (le juge) ; il faut une règle écrite d'avance, par exemple « appariée à la loi plantée j si la divergence moyenne de L_j à la loi de la tentative est ≤ 0,05 nat », calculée sur la loi **relue dans l'engagement scellé** — quelques lignes au-dessus de `Oracle.divergence`, à éprouver (R5). Pour un monde à plusieurs lois vraies composées, la définition même de « retrouver la loi j » (sur quel domaine, contre quelle loi de référence) est à fixer : l'oracle actuel compare à **la** loi génératrice entière.
3. **Tranche d'épreuve** (plan § 3.0) : la tranche du tour fermé est tirée de la loi du monde par la graine de la tâche ; le partage « part servie / tranche d'épreuve » du jeu d'évolution, sa graine par monde et la garde « une ligne de la tranche d'épreuve dans ce qui est servi arrête la génération » sont à écrire. L'étage accepte toute tranche déclarée.
4. **Plus de douze tentatives** : une génération d'environ 94 tentatives (devis § 5) demande au moins huit étages, chacun dans son dossier, avec son classement et sa copie de tranche ; une enveloppe à écrire. Le statut « non éprouvée (budget) » du plan n'existe pas dans l'étage : à porter par l'enveloppe.
5. **Fabrication des lignes** : le noyau ne la voit pas (E2). La seule garde existante est le contre-calcul du tour fermé, qui ne vaut que pour la forme imposée (loi dans la grammaire, statistique de l'évaluateur). Un engagement **libre** (fichier, colonne, statistique choisis par le proposeur) n'a aucune garde contre un script qui fabrique ses lignes : le préenregistrement de l'étage sur processeur doit soit imposer la forme du tour fermé, soit dire cette limite.
6. **Lecteur témoin** : l'étage l'exige (v2 l. 2276-2277) et ouvre une session par fiche testée (v5 l. 625) ; le retirer (plan, § 12, question 8) demande une version neuve de l'étage, ou une doublure scriptée (à 0 USD) comme ici.
7. **Seuil en texte** : le comparateur est lu dans une phrase française ; l'enveloppe doit vérifier que le seuil scellé (`valeur`, `comparateur`) est bien celui qu'elle voulait (cas sain et artefact).
8. **scipy** : le module de l'oracle l'importe en tête ; il n'est pas installé sur cette machine (bouchon dans `sys.modules` pour l'essai, § 6). L'usage réel du comparateur demande scipy, ou un module neuf qui n'importe que ce qu'il emploie.

## 4. Conséquences

- **Nœud 1** (« épreuve programmée = tests de mort, sous réserve du palier 0a ») : la réserve d'instrument est levée — l'étage exécute sans réécriture un engagement sur une loi plantée, et le verdict est calculé par le noyau sur le fichier brut. **Fait neuf, à porter avec le nœud, sans le trancher** : sur la forme imposée du tour fermé, l'expérimentateur n'a rien à décider (le script est fixe : relire la loi, appeler l'évaluateur) ; l'étage a tourné de bout en bout avec un expérimentateur et un lecteur **écrits par programme**, à 0 USD d'appels. Le plan v4 (§ 3.0) prévoit un expérimentateur modèle, « ni juge, ni proposeur », dont `resultat` dépend ; un expérimentateur programmé rendrait `resultat` entièrement programmé pour les engagements dans la grammaire. Choisir l'un ou l'autre change le § 3.0, le § 3.1 et le devis : c'est à Lazar. Je n'ai pas vérifié qu'un lanceur réel accepte les doublures hors du mode à blanc.
- **Palier 0b** : l'« exécuteur simulé » de l'étage sur processeur (plan § 7) peut être **l'étage v5 lui-même**, exécuteur factice (sept tentatives en un peu plus d'une seconde de durée murale locale ici, ce n'est pas un coût), avec des répondeurs scriptés ; avant lui, les manques 1 à 5 et 7 du § 3.3 sont à écrire, chacun avec sa garde éprouvée sur un cas sain et un artefact.
- **Palier 1** : ce qui reste à mesurer n'est plus l'instrument mais la conduite et le coût d'un expérimentateur modèle, **si** le nœud 1 le garde ; avec un expérimentateur programmé, le palier 1 ne mesure plus le coût du test (nul en appels) mais seulement la part de tentatives refusées au gardien ou à l'étage, et la location de la machine.

### Les quatre manques du rang 0, et la v68

1. *Héritage de la sélection illisible* (`json.loads` sur du Markdown, chemin `course2_v59`) : il ne touche pas l'étage ; il interdit de prendre `course2_v59` comme véhicule du registre. Le chemin du tour fermé (`boucle_fermee_v59`, `tour_ferme_v64`) sert sa propre vue aux proposeurs ; non éprouvé ici.
2. *Aucun étage après la dernière génération* (`course2_v56` l. 426, `course2_v59` l. 91) : propre au véhicule de la course 2 ; le tour fermé appelle l'étage dans chaque génération, et l'essai l'appelle directement, sans rien servir : le test de mort du monde final « pour la mesure seulement » (plan § 6) est jouable ainsi, sans écrire dans un registre.
3. *Budget remis à zéro par génération* (`noyau_v56` l. 106) : propre à la course 2 ; l'étage borne chaque fiche, pas la course (`plafond_total_usd` non passé par le tour fermé, qui tient son propre compteur). Le budget égal par bras du plan, test compris, est à tenir par l'enveloppe.
4. *Bac réel jamais joué avec l'étage v5* : **joué ici localement** (E5 : sonde complète, sept tentatives, valeurs égales au factice, aucun groupe de contrôle restant). Reste à rejouer sur la machine louée jetable (autre noyau, peut-être cgroup v2 : « SUPPOSÉ » de `tests_de_mort_v3.py`) et avec des scripts qui ne sont pas fixes.

**v68** (non lue ; plan du rapport du rang 0, § 5) : elle vise le véhicule de la course 2 (lecture de la sélection, étage après la dernière génération, refus de la portée « course »). L'étage lui-même n'en a pas besoin pour une épreuve sur monde planté par le chemin du tour fermé ; elle n'est requise que si l'épreuve de l'héritage se joue dans la course 2, dont les fiches n'ont pas de champ de test (nœud des champs de fiche du rang 0).

## 5. Coût par tentative : ce que le code borne (aucun chiffre réel)

- Expérimentateur : au plus `budget_test_usd` par fiche (défaut 0,50, « SUPPOSÉ », v2 l. 136 ; 0,80 au tour fermé, `BUDGET_EXPERIMENTATEUR_PAR_CARTE_USD`), au plus 12 tours (`TOURS_MAX_PAR_FICHE`), 2 tours par session (`MAX_TOURS_SESSION`), 1 à 20 exécutions (défaut 3), délai par exécution ≤ 3 600 s (défaut 120 s, celui que le tour fermé laisse, quotas de la sortie), mémoire 768 Mo au moins dans le vrai bac ; vérification préalable « consigne × prix d'un caractère > reste » si un prix est passé (v5 l. 468).
- Lecteur témoin : au plus `budget_lecteur_usd` (0,10, « SUPPOSÉ »), une session par fiche testée.
- Étage : au plus 12 fiches ; somme des plafonds = nombre × (plafond de l'expérimentateur + plafond du lecteur) (`plafond_etage`, v2 l. 2297).
- Fiche refusée à l'étage : aucune session. Fiche « rien envoyé » : coût 0 et « non concluant » (E3).
- Avec les doublures programmées de cet essai : 0 USD d'appels par construction ; la location de la machine jetable reste hors chiffre (devis § 5).

## 6. Écarts et réserves

1. **scipy absent** : bouchon posé dans `sys.modules` pour importer `oracle_tour_ferme_v60` (dont seule `temperee_inclinee` emploie `minimize`) ; le bouchon lève s'il est appelé, il ne l'a pas été (sinon l'essai se serait arrêté). Aucun paquet installé, aucun réseau.
2. **Dossier racine du vrai bac sous `/tmp`** (`palier0a-bac-v1-…`, parent 0711, `bac` 0700 à l'identité 64097) : le bloc-notes n'est pas traversable par l'identité dédiée. Créé et retiré par le programme (`racine_retiree` : vrai). L'exécution a créé puis retiré des groupes de contrôle de mémoire de l'hôte (code de l'orchestrateur ; aucun restant).
3. **Processus de l'identité dédiée** : le relevé fait **juste après** le retrait trouve sept identifiants encore présents (sortie, `E5.processus_restants_de_l_identite_dediee`) ; relevé refait à 14:28:04Z : **aucun** processus de l'identité 64097, et aucun des sept identifiants n'existe plus. L'essai réel de l'orchestrateur attend jusqu'à `DELAI_RETRAIT_GROUPE_S` + 5 s avant ce relevé ; mon programme ne l'attend pas : défaut de forme du programme v1, sans effet sur les verdicts.
4. Les dossiers d'étage (préenregistrements, verdicts, copies scellées) restent dans le bloc-notes ; leurs empreintes sont dans la sortie versée. Rejouer : § 7.
5. Le monde employé est l'exemple de l'organisme, pas un monde de l'héritage (manque 1) : l'essai établit l'instrument, rien sur la difficulté des mondes de l'héritage.
6. Lecture du code ciblée (§ 2), non intégrale pour `tests_de_mort_v2.py` (2 769 lignes) et `tour_ferme_v64.py` (1 395 lignes).

## 7. Pièces versées (ce dossier)

| pièce | rôle |
|---|---|
| `essai_palier_0a_tests_de_mort_v1.py` | le programme d'essai (bibliothèque standard, numpy ; importe la copie de l'orchestrateur) |
| `essai-palier-0a-sortie-v1.json` | sa sortie |
| `manifeste-essai-palier-0a-v1.json` | graines (`SeedSequence(202611190)` → racine `8204760644583704453`, tâche `palier-0a|essai-tests-de-mort-v1`), versions (Python 3.13.18, numpy 2.5.3, bubblewrap 0.9.0, noyau Linux 6.18.44), empreintes des seize fichiers de l'orchestrateur employés (égales à l'original), commit de base, état de la copie |
| `rapport-palier-0a-v1.md` | ce rapport |

Empreintes : compagnons `.sha256`. Rejouer : copie neuve de l'orchestrateur au commit `a41b7b50` (`cp -a`), le programme placé dans `<copie>/palier-0a/`, puis `PYTHONDONTWRITEBYTECODE=1 python3 -B essai_palier_0a_tests_de_mort_v1.py --sortie <dossier neuf> --bac les-deux` (bac réel : superutilisateur, `bwrap`, `setpriv`, identité 64097 sans compte).
