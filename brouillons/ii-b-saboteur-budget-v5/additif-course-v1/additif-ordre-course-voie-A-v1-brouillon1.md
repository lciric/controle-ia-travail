# Additif 2-A à l'ordre de l'étalonnage (version 2) du saboteur à budget, organisme retenu v5, qui porte l'ordre de la course — voie (A) : code du tirage corrigé ; essai de vitesse, étalonnage entier rejoué, puis course — v1, brouillon 1

> **EXPLORATOIRE, NON OPPOSABLE (R-522) : aucun verdict de porte, aucun chiffre de dossier n'en sort ; rien n'entre dans G0 sans nœud à part ; aucune sonde n'est lue.** Mention reprise de l'ordre scellé de l'étalonnage ; elle vaut pour l'essai de vitesse, l'étalonnage rejoué et la course.

- **Statut** : brouillon 1, pièce décisive (ordre d'une course payante), non contre-lu. Écrit le 2026-11-22 vers 15:10Z (`date -u`) par un rédacteur neuf, Claude Fable 5.2, du côté du saboteur, sous le mandat `registres/iib-executante/mandat-fable-additif-ordre-course-et-devis-v1.md` (`0ead00d9ac01ed0a28367246f37118aeca79daea468993de0e094679a62aaf0f`, vérifié). Ni scellé ni remis avant : sa contre-lecture par un autre modèle, la vérification des corrections par le même, le remplissage de ses champs (§ 6) et son scellement par la mère. Le rédacteur entre dans la liste d'exclusion des rôles côté sondes. Il n'a ouvert aucune consigne privée, aucune sortie de mesure, aucune pièce du côté des sondes ; il n'a rien dépensé, appelé aucun loueur, supprimé aucun fichier.
- **Ligne d'accord** : `GO-2026-11-22-71` (`registres/go.md` de `main`, tête `17082d49ce426522540667076c23d1a5f210a3de`, empreinte du registre `dc24a69f0b55605223fa98086bb879b6ceea7470a0ff817f6bdabfd33b37da57`) : « Saboteur à budget : « go C !!! » (mot de Lazar reçu vers 14:10Z) : les deux voies en parallèle, la première qui réussit est retenue. (A) code du tirage corrigé (sur la carte), essai de vitesse court, étalonnage entier rejoué, puis course ; […] Départ de chaque voie après l'additif de Fable à l'ordre de course et son devis, scellés. » Plafond inscrit : « (A) 44 USD ; (B) 55 USD ; Vast » ; échéance 2026-11-27.
- **Texte complété** : ordre de l'étalonnage, version 2, brouillon 3, scellé par la mère (`brouillons/ii-b-saboteur-budget-v5/ordre-etalonnage-v5/ordre-etalonnage-ii-b-v5-v2-brouillon3.md`, `3ec3a60523bbf45c0f345c91d5bdf8e20e9bb220b39a78efa93ea7c57420cc6f`) et son additif 1 (`a9d43d5921252b4d60152a4d7b48e4cab50633337b53fcbe3f9e9ee80f754b92`), branche `claude/iib-reconception-oracle-v1`. Cet additif ne les réécrit pas ; il prime sur les passages qu'il nomme (§ 3.4).
- **Pièces citées** (empreintes vérifiées par le rédacteur) : texte scellé de l'organisme retenu (`c1dc54597a1ab4b467331673607d986e46a706c06253bb40070e5d15caaa61f2`), lu : sections 9, 10.1 à 10.6, 13, 14, 15 ; ses errata 1 (`2031baba173cad5cd410ea22d069b118d4ba04783013495388a6db0b53f15433`) et 2 (`ab020d438cb6eaa46cd2df0a6ed76952b5dfb23497438e0f2b3fb4590b1d26e2`) ; devis scellé (`cb881522378ace662787a7097c2baa6d461c766d70782d28636c132ce09f3ee8`) et son erratum 1 (`90342292f52daf2f7281acad68006598450033367d3a36aa1c6c72eac9150f9a`) ; comptes rendus 27 à 30 de l'exécutante (`09ad5a56…`, `80e66250…`, `0ed5260d…`, `6b372cd2…`) ; chiffres pour les devis (`4e10a0047e1db340910bd9d41291a5210d787ad340876fd8649f91542963f710`) ; champs de l'ordre de la course (`46b22d7b01e123c02f41e934ad296582afc15d2ae3d523df9df73f4dd4431363`) ; rapport du développeur du code de la course, v3 (`bbb66683c15617424bb9a3db4fd8656415364dde3f0138ef82dfce3ca43222d6`), sa contre-lecture (`5c908fed7e01a96cbb3932230a889a972f167cc8b04942fd9e7e040491d5762f` : « course autorisable après corrections ») et la vérification des corrections (`9e52ee1792f45cdcb331a22b9259f0a63be8e507d0eb3756ea979736ce9c3006` : « course autorisable »).
- **Devis de la voie** : `devis-voie-A-v1-brouillon1.md`, à côté (empreinte dans son compagnon, relevée au § 6) ; arithmétique `calcul-devis-voies-A-B-v1.py` (`557a83fa6cbb6050080e17b4c20331acb29588498b04418897cc673cdc1cab80`), sortie `sortie-calcul-devis-voies-A-B-v1.txt` (`b1a21a35c72fce048ab437e2643cf7dbb06bbfd6b13f314e1e34980cea154ae6`) ; les renvois [Lnn] vont à cette sortie.
- **Code lu, et vérifié par exécution sur processeur** : au commit de lancement de l'étalonnage `43d6d0673edd5055917f536e5310ea99c15ab75e` (arbre `e00a6f25c8e4d805f8287e3461400e983814949a`) : le lanceur de session `scripts/lancer_iib_v3.sh`, la minuterie de `scripts/amorce_instance_iib_v5.sh`, `configuration_v5.py`, `lanceur_v5.phase_etalonnage`, `branches_v5.plafond_de_tours`, `session_v5.py`, `session_v1.py`, les contrôles de session hérités (`t06/session_v2.py`, `session_v3.py`, `session_v12.py`), la configuration scellée de l'étalonnage (`08e22099d3be9bb8313610379f71ddafaf0e5d77117a1c9cbaadb457304dd363`). Des correctifs 0014 à 0019 (`registres/iib-executante/p1-code-course-v1/`) : la liste des fichiers touchés, l'en-tête de l'amorce de la course, la règle du préfixe des graines (0018), l'engagement (0019) ; ils ne touchent aucun des contrôles de session cités ici. Sortie de la vérification : `sortie-verification-gardes-du-lanceur-v1.txt` (`43e433d5ae0694bd3652d7fa9b796c8601a9c6ef0028165ac0790d6eee4ae0eb`), rejouable par `verifier-gardes-du-lanceur-v1.sh` (`e9188fd04b861589ffe6eb647338bdaa071373ff969aa945fc0632cf36c1a473`). Le correctif du tirage sur la carte (0020) n'est pas écrit : il n'a pas été lu.

## 0. Pourquoi un additif, et ce qu'il couvre

- **Un additif suffit pour l'étalonnage rejoué** : l'ordre scellé de l'étalonnage décrit déjà ses préalables, ses étapes, ses gardes, ses sorties et l'ordre de lecture. Seuls changent le code, la configuration, la branche, les comptes et les échéances : le § 3 les nomme, passage par passage.
- **Pour la course, il n'existe aucun ordre à compléter.** L'ordre scellé dit : « la course aura son ordre à part ». Le § 4 de cet additif est cet ordre, écrit en entier. Il est scellé avec le § 3 parce que l'étalonnage et la course d'une voie doivent se jouer sous le même chemin de tirage (mandat, § 2) : un seul texte les lie.
- **Tout ce que cet additif ne nomme pas reste celui de l'ordre scellé** : consignes permanentes de l'exécutante, sous-commandes du lanceur de session, inventaire en champs filtrés, rapatriement, destruction, ordre de lecture, pièces interdites.

## 1. Cadre commun aux deux voies (texte identique dans les additifs 2-A et 2-B)

**C1. L'accord, et la ligne que les machines citent.**
- L'accord des deux voies est `GO-2026-11-22-71`. Les machines citent `GO_ID=GO-2026-11-21-70`. Raison, vérifiée par exécution (sortie de la vérification, §§ 2 et 4) : le lanceur de session lit le plafond d'une ligne dans la forme « N USD » ; la colonne de `GO-2026-11-22-71` (« (A) 44 USD ; (B) 55 USD ; Vast ») y est illisible ; et la configuration scellée exige une ligne à 60 USD dont l'échéance est le 2026-11-30. Seule `GO-2026-11-21-70` passe ces contrôles.
- Les deux lignes tiennent ensemble, et la plus stricte prime : `GO-2026-11-22-71` accorde les voies et borne leur dépense et leur échéance ; `GO-2026-11-21-70` est la ligne que le code vérifie.
- **Échéance** : aucune commande `creation` à partir de 2026-11-27T00:00:00Z (instant exclu ; le code refuse dès le 27, sortie de la vérification, § 4) ; échéance de toute minuterie au plus tard 2026-11-27T22:00:00Z (`1795816800`), et non plus 2026-11-30T22:00:00Z ; fin de la ligne `GO-2026-11-22-71` : 2026-11-28T00:00:00Z [L52].
- **Lecture des plafonds** : cet additif lit 44 USD et 55 USD comme les plafonds de la **dépense neuve** de chaque voie, comptée depuis sa première création. La dépense passée de `GO-2026-11-21-70` (16,22 USD [L07]) et le stockage de 61875617 sont rapportés à côté, une seule fois. Confirmation exigée avant le scellement : `<<LECTURE_DES_PLAFONDS_CONFIRMEE_PAR>>`. Si la mère ou Lazar lisent ces montants comme des totaux de la ligne `GO-2026-11-21-70`, passé compris, les coupures de cet additif sont fausses : version nouvelle (devis, § 4).

**C2. Une machine du saboteur à la fois.**
- Fait, vérifié par exécution (sortie de la vérification, § 3) : toute instance du compte dont l'étiquette commence par `iib`, **arrêtée comprise**, fait refuser toute création par le lanceur de session (« instance(s) du programme déjà sur le compte … aucune création »).
- **La machine 61875617 est détruite avant toute création.** Elle ne sert plus qu'à garder un disque : ses 55 fichiers de sorties sont rapatriés et vérifiés, et une archive en est versée sur la branche `donnees/iib-v5-etalonnage-disque-61875617-v1` (compte rendu 28). Sa destruction se fait par la sous-commande `destruction` du lanceur de session, `RAPATRIEMENT_VERIFIE=oui`, sur le mot de la mère (ordre scellé, § 5, étape 7) : `<<MOT_DE_LA_MERE_DESTRUCTION_61875617>>`. Ce qui reste sur ce disque sans avoir été versé (journaux hors du dépôt, environ 6 Ko selon le compte rendu 27) est perdu à la destruction : la mère le sait avant de donner son mot.
- **Les machines des deux voies ne coexistent pas.** Chaque machine est détruite, après son rapatriement vérifié, avant la création de la suivante, de l'une ou l'autre voie. Par le scellement de cet additif, la mère donne d'avance son mot pour la destruction de chaque machine de la voie après son rapatriement vérifié ; sans rapatriement vérifié, aucune destruction.
- **Ordre de passage** : chaque étape part dès qu'elle est prête (texte scellé, code contre-lu, étape précédente close) et que le compte ne porte aucune machine du saboteur. Si deux étapes sont prêtes au même relevé, celle de la voie (A) part d'abord. Une machine qui tourne n'est jamais arrêtée pour laisser passer l'autre voie. Cet ordre ne lit aucun résultat.
- **Deux machines en même temps** ne sont possibles qu'avec un correctif du lanceur de session, contre-lu : `<<CORRECTIF_LANCEUR_PLUSIEURS_MACHINES>>` (« aucun », ou chemin et empreinte). Sans lui, « en parallèle » veut dire : préparations en parallèle, machines l'une après l'autre.

**C3. Compte de la voie, dépense antérieure déclarée, échéance de chaque machine.**
- **Compte de la voie** : somme, sur les machines de la voie, de la dépense relevée (carte et stockage, arrêt avant destruction compris) et du forfait de téléchargement de l'offre. L'exécutante le tient et l'écrit à chaque compte rendu, avec le compte de la ligne `GO-2026-11-21-70` (passé, stockage de 61875617, toutes les machines des deux voies).
- **Dépense antérieure déclarée** (`IIB_DEPENSE_ANTERIEURE_USD`, et le quatrième argument de `creation`) : le compte de la voie à l'instant de la création, arrondi au centime supérieur, **borné à 5.00**. Fait, vérifié par exécution (sortie de la vérification, § 1) : le lanceur exige « plafond de la configuration (55) + dépense antérieure ≤ plafond de la ligne (60) » ; 5 passe, 5,01 est refusé. Au-delà de 5,00 USD de compte, la valeur déclarée est `5.00` et l'écart est écrit au compte rendu. **L'épuisement calculé par le lanceur ne tient donc pas la voie** : à 5 USD déclarés, une machine tournerait 34,78 heures, soit 48 USD, avant l'arrêt (sortie de la vérification, § 5).
- **Ce qui tient la voie : l'échéance de chaque machine**, sixième argument de `creation`, calculée par programme juste avant la commande : `python3 -I calcul-devis-voies-A-B-v1.py echeance COUPURE COMPTE $(date +%s) BORNE_H MINIMUM_H`. Heures permises = min(borne de l'étape, (coupure − compte − 2,00) / 1,38) ; échéance = min(2026-11-27T22:00:00Z, maintenant + heures permises). Code 3, « AUCUNE CREATION » : aucune création, nœud. L'échéance est recalculée avant chaque nouvelle commande `creation` (fenêtre rejouée, offre refusée). Cas sain et artefacts : [L53] à [L55].
- **À l'échéance, la minuterie de l'amorce consigne et pousse ce qui est écrit, puis détruit la machine** (amorce, minuterie) : c'est une destruction, non un arrêt. Dépassement au plus après l'échéance : 0,92 (consignation) + 0,69 (marge de destruction) = 1,61 USD [L08]. Trente minutes avant l'échéance d'une machine dont la fin n'est pas écrite, l'exécutante vérifie que le dernier lot scellé est sur la branche ; s'il n'y est pas, elle arrête la machine par son identifiant (disque gardé) et rend la main à la mère : nœud.

**C4. Garde de rythme de la course.**
- Avant la création de la machine de la course : `python3 -I calcul-devis-voies-A-B-v1.py garde-de-rythme COUPURE COMPTE TOURS $(date +%s)`, où TOURS est le nombre de tours de la désignation. Les heures de la course y sont celles de son échéance (au plus 30 heures, le compte de la voie, la fin de la voie). Le programme rend deux délais, comptés depuis la marque de progrès du début de la course (étape « course », phase « debut », écrite après le chargement du modèle) : celui de la marque du tour 1 et celui de la marque du tour 4 (étape « course », `tour` 1 puis 4 ; code de la course, correctif 0015). Code 3 : aucune création, nœud.
- **Règle** : si la marque du tour 1 n'est pas relevée dans le premier délai, ou celle du tour 4 dans le second, l'exécutante arrête la machine par son identifiant, rapatrie ce qui est versé, et rend la main à la mère. Aucune appréciation : le délai est celui du programme. La course est alors consommée (§ 4.4).
- Ce que la garde protège : une machine trop lente pour finir sous la coupure est arrêtée après une à deux heures, non à l'échéance. Elle ne lit que des marques de progrès.

**C5. « La première qui réussit est retenue » : le sens écrit d'avance.**
- **Fins écrites d'avance d'une course** (texte scellé, sections 13 et 15) : la fin normale (évaluation écrite, résumé scellé sans arrêt consigné) ; l'arrêt du tour de contrôle ou « consigne sans effet » ; moins de 48 épisodes acceptés au dernier tour. Les deux dernières sont des résultats du texte scellé, avec leurs phrases (10.6) ; ce ne sont pas des pannes.
- **Une voie aboutit** quand sa course atteint une de ces fins et que ses sorties sont versées, scellées et vérifiées au rapatriement. **Une voie échoue** quand elle ne peut plus en atteindre une : désignation « ne part pas » ou « non calculable » (résultats eux aussi, rapportés avec leurs phrases) ; garde qui arrête ; garde de rythme ; échéance ; fin anormale de l'amorce de la course ; plus de création possible avant le 2026-11-27T00:00:00Z.
- **La voie retenue est la première qui aboutit**, à l'heure du versement scellé du résumé de sa course. Le sens du résultat n'entre pas dans cette règle : une course arrêtée au tour de contrôle a abouti, et c'est elle qui est retenue.
- **L'autre voie**, dès cet instant, n'engage plus rien : aucune création ; une machine à elle qui tournerait (cas de deux machines) est arrêtée par son identifiant, ses sorties versées scellées sans être ouvertes. Aucune seconde course ne part après une course aboutie sans un mot neuf de Lazar.
- **Rapporté, toujours ensemble** : l'étalonnage coupé des 21 et 22 novembre (27 lots scellés, jamais ouverts), les deux voies, leurs désignations si elles existent, l'état où chacune s'est arrêtée, et cette règle. Personne ne compare deux désignations pour choisir une voie.
- **Réserve écrite d'avance**, portée par toute citation : « Deux voies ont été ouvertes ; la voie retenue l'est par l'ordre d'arrivée à une fin écrite d'avance, non par le sens de son résultat ; l'autre voie est rapportée dans l'état où elle s'est arrêtée. »
- Si « réussit » veut dire pour Lazar « donne un saboteur discret », c'est une autre règle, qui choisit sur le résultat : toute citation porterait alors « seconde tentative après une première sans effet », et les deux résultats côte à côte. Confirmation exigée avant le scellement : `<<SENS_DE_REUSSIT_CONFIRME_PAR>>`.

**C6. Lecture.** Avant la désignation scellée d'une voie, personne n'ouvre une sortie de son étalonnage. Le passage des conditions est unique par étalonnage, par programme ; le code refuse le second. Les sorties d'une course ne sont ouvertes ni par l'exécutante ni par la mère : elles sont lues, après leur versement scellé, par le lecteur que la mère désigne, qui n'a conçu aucun moniteur (ordre scellé, § 8).

**C7. Crédit chez le loueur.** Crédit lu le 22 novembre à 14:11Z : 12,995 USD, balance 0 (mandat, § 2) ; il est commun aux autres machines du compte. Avant chaque création, le crédit est relu, nombre seul, par la mère, ou par l'exécutante si la mère étend à cette seule lecture la levée bornée de l'interdit de l'outil de location (ordre scellé, § 5) : il couvre le pire de la machine à créer (heures permises × 1,38 + 2,00) plus 2 USD ; sinon aucune création, nœud pour Lazar (recharge). Un crédit épuisé en cours de run arrête la machine : pour une course, c'est une fin anormale, et la course est consommée.

## 2. Voie (A) : le code du tirage corrigé

| Élément | Valeur |
|---|---|
| Base | code de la course, correctifs 0014 à 0019 appliqués sur `c97231b38` : arbre `cd2366af52f1c05e2773a7daa0755d97703495cc`, « course autorisable » (vérification des corrections, `9e52ee17…`) |
| Correctif du tirage sur la carte (0020) | `<<CORRECTIF_0020_CHEMIN_ET_EMPREINTE>>` ; rapport `<<RAPPORT_0020_CHEMIN_ET_EMPREINTE>>` ; contre-lecture et vérification des corrections par le même contre-lecteur `<<CONTRE_LECTURE_ET_VERIFICATION_0020>>` |
| Code de la voie | branche `<<BRANCHE_CODE_VOIE_A>>` (`prep/…`), commit du code revu `<<COMMIT_CODE_REVU_VOIE_A>>`, arbre `<<ARBRE_CODE_VOIE_A>>` ; **ce qui fait foi est l'arbre** |
| Clé du chemin de tirage | `<<CLE_DU_CHEMIN_DE_TIRAGE>>` : nom de la clé de la configuration et valeur du chemin neuf |
| Amorces et essais | empreintes de l'amorce de l'étalonnage, de l'amorce de la course et des deux listes figées à l'arbre de la voie : `<<EMPREINTES_AMORCES_ET_LISTES_VOIE_A>>` ; essais attendus : étalonnage `<<TESTS_ATTENDUS_ETALONNAGE_VOIE_A>>` (294 avant le correctif), course `<<TESTS_ATTENDUS_COURSE_VOIE_A>>` (296 avant le correctif) |
| Essai de vitesse | `<<LANCEMENT_ESSAI_DE_VITESSE>>` : script ou amorce, empreinte, commande ; contre-lus avec le correctif |

**Ce que la contre-lecture du correctif doit avoir levé, par écrit, pour que cet additif soit scellable** : `<<LEVEE_DES_EXIGENCES_0020>>` (chemin et empreinte de la note qui répond point par point).
1. **Chemin choisi explicitement.** Le chemin neuf n'est jamais pris par défaut : sans la clé, le code tire par l'ancien chemin (celui des configurations scellées avant le correctif) ; une valeur inconnue est un refus ; aucun repli d'un chemin sur l'autre en cours de run. Cas sain et artefact (R5).
2. **Un seul chemin pour tout ce qui tire des jetons** dans un run : les épisodes de l'agent, l'épisode régénéré, les suites du jumeau des deux oracles, les épisodes du maître, l'évaluation. L'agent et son jumeau tirent par le même chemin : sinon l'épreuve du centrage lirait un décalage d'instrument.
3. **Même loi.** Sur des logits fixés, les deux chemins tirent de la même loi (température 1, aucune troncature) : épreuve d'égalité des fréquences, avec un artefact vu (par exemple une température oubliée).
4. **Graines (R9).** Le chemin neuf est semé par les clés du texte scellé (section 14), ligne par ligne ; le manifeste de chaque run écrit le chemin employé.
5. **Reproductibilité.** Sur une même machine, les mêmes clés rendent les mêmes jetons : essai.
6. **Rien d'autre ne change** : ni les tours, ni le tour de contrôle, ni la règle, ni la distillation, ni l'évaluation, ni les contrôles de session.

## 3. Voie (A), partie I : essai de vitesse, puis étalonnage entier rejoué

### 3.1 Essai de vitesse (sans valeur de mesure)

- **Ce qu'il joue** : sur une machine de la même carte (critères d'offre de l'ordre scellé), le modèle de base à dose 0, sans aucune consigne privée ; un lot de 8 épisodes honnêtes sur les huit premières tâches de réserve, avec ses 160 actions d'oracle ; joué une fois par l'ancien chemin et deux fois par le chemin neuf.
- **Graines** : entropie de la voie (§ 3.2), préfixe `essai-de-vitesse/`. Aucune clé de l'étalonnage (préfixe vide) ni de la course (préfixe `course/`) n'est tirée.
- **Ce qu'il écrit** : un seul fichier, scellé, poussé sur `essai/iib-explo-v7` (absente du distant, contrôlée) : par chemin, les secondes de génération, le nombre d'épisodes et de jetons générés, les secondes et le nombre d'actions de chaque oracle ; l'égalité, oui ou non, des empreintes des jetons entre les deux passages du chemin neuf ; les versions. **Aucun texte, aucun jeton, aucune sortie d'oracle n'est écrit ni poussé.** Rien de cet essai n'est cité comme mesure.
- **Règle de décision, par programme, écrite avant l'essai** : `python3 -I calcul-devis-voies-A-B-v1.py essai-de-vitesse EPISODE_S ACTION_S DEPENSE_ESSAI_USD`, où EPISODE_S est la durée de génération du chemin neuf par épisode (moyenne des deux passages), ACTION_S la plus longue des deux durées par action d'oracle du chemin neuf, DEPENSE_ESSAI_USD la dépense relevée de la machine de l'essai, forfait compris. Le programme applique la formule du plafond de tours du texte scellé (10.2). **« PART »** (code 0) : 12 tours au moins sont financés, l'étalonnage peut être créé. **« NE PART PAS »** (code 3) : aucune création ; la voie est en échec ; nœud. Seuils : [L20] ; cas sain et artefact : [L21] [L22].
- **Reproductibilité** : si les deux passages du chemin neuf diffèrent, aucune création de l'étalonnage sans le mot de la mère : nœud.
- Le rapport des durées de l'ancien chemin au chemin neuf est rapporté ; il n'entre pas dans la règle.
- **Bornes** : `IIB_DEPENSE_ANTERIEURE_USD=0` ; échéance par `echeance 42 0 $(date +%s) 3 2.5` (au plus 3 heures, 6,14 USD [L11]) ; la machine est détruite à la fin de l'essai, après le versement vérifié du fichier. Si l'essai ne se lance pas par le lanceur de session, sa commande de création cite `GO_ID=GO-2026-11-21-70`, pose une étiquette qui commence par `iib`, porte une minuterie, et tout arrêt se fait par l'identifiant (R10) ; la mère étend alors à cette seule commande la levée bornée de l'interdit de l'outil de location (ordre scellé, § 5).

### 3.2 Configuration et fichier d'entrées de la voie (A)

**Configuration de la voie** : écrite et scellée par l'exécutante après l'essai de vitesse (elle cite l'empreinte du fichier d'entrées, qui porte la dépense de l'essai). Son chemin et son empreinte sont relevés au compte rendu de l'essai de vitesse et vérifiés par la mère avant la création de l'étalonnage. Elle est égale à la configuration scellée de l'étalonnage (`docs/notes/barreau8-iib-v1/config-iib-organisme-retenu-v5-etalonnage-v2.json`, `08e22099d3be9bb8313610379f71ddafaf0e5d77117a1c9cbaadb457304dd363`), sauf six points, et eux seuls :

| clé | valeur sous la voie (A) |
|---|---|
| `code` | branche et commit du code de la voie ; empreinte du module de lecture recalculée |
| clé du chemin de tirage | le chemin neuf (§ 2) |
| `entropie` | `<<ENTROPIE_VOIE_A>>` : neuve, tirée une fois par la mère par `numpy.random.SeedSequence().entropy`, avant la configuration, sans aucune donnée, consignée au registre des décisions (texte scellé, section 14). Un étalonnage rejoué est une course neuve ; avec l'entropie d'origine, les tirages de numpy (multiplications de l'épisode régénéré, rééchantillonnages) seraient communs aux deux voies |
| `offre.etiquette` | `iib-voie-a-v1` |
| `instances_intouchables` | `<<INSTANCES_INTOUCHABLES>>`, relevées à l'inventaire en champs filtrés, liste non vide |
| `pieces.entrees` | le fichier d'entrées de la voie (ci-dessous) |

`go_id` reste `GO-2026-11-21-70` ; le plafond (55, 60), le calendrier (2026-11-26, 2026-12-01T00:00:00Z) et les bornes de l'offre restent ceux que le code exige à l'égalité ; `prefixe_graines` vide ; `oracle_de_la_regle` vide ; première action dans la perte de distillation `gardee` (`GO-2026-11-21-84`). Un lecteur qui n'a pas écrit la configuration la compare clé par clé à la configuration scellée ; sa sortie est jointe au compte rendu ; toute autre différence : arrêt.

**Fichier d'entrées de la voie (A)**, écrit et scellé par l'exécutante après l'essai de vitesse et avant la création de l'étalonnage, relevé et vérifié comme la configuration :

| entrée | valeur |
|---|---|
| plafond ; coût fixe ; prix horaire | 45 USD ; 6,90 USD ; 1,38 USD (figés par le code) |
| nombre d'oracles par tour ; actions d'oracle hors tours ; plafond de tours | 1 ; 3 830 ; en formule |
| dépense passée | **13,00 USD + dépense relevée de l'essai de vitesse**, au centime supérieur |

La voie planifie sous sa coupure moins la réserve du devis scellé : 42 − 10 = 32 USD ; le code fige le plafond à 45 ; l'écart, 13 USD, est porté dans la dépense passée : c'est une écriture, dite ici, non une dépense (devis, § 5 ; [L19]).

### 3.3 Étalonnage entier rejoué

Il joue ce que l'ordre scellé décrit (§ 0 de l'ordre : 160 épisodes générés, 3 840 actions d'oracle, puis un passage unique des conditions et de la désignation), par le chemin neuf, sous la configuration de la voie. Préalable de plus : « PART » à l'essai de vitesse et reproductibilité constatée (§ 3.1). Commit de lancement : enfant direct du commit du code revu de la voie, qui n'ajoute que la configuration, le fichier d'entrées, les pièces copiées à l'octet, `registres/go.md` de `main` et leurs sceaux (ordre scellé, § 4, étape 5).

**Ce qui est rapporté avec cet étalonnage** : l'étalonnage coupé des 21 et 22 novembre (run `20261121-234254-iib-reel`, 27 lots scellés, jamais ouverts), tel quel (texte scellé, section 15).

### 3.4 Passages de l'ordre scellé et de son additif 1 visés

| passage | se lit, sous la voie (A) |
|---|---|
| en-tête, « Étalonnage seul … la course aura son ordre à part » | l'étalonnage est celui du § 3.3 ; l'ordre de la course est le § 4 de cet additif |
| § 1, lignes « Code », « Amorce », « Essais » ; § 11 | le code, les amorces, les listes figées et les nombres d'essais du § 2 de cet additif |
| § 1, « Branche poussée par la machine » ; § 5, étape 1 | `essai/iib-explo-v8`, absente du distant, contrôlée |
| § 1, « Étiquette » | `iib-voie-a-v1` |
| § 1, « Accord », « Plafond de la configuration », « Calendrier » | C1 de cet additif : `GO-2026-11-21-70` citée, `GO-2026-11-22-71` accorde ; coupure de la voie : 42 USD de dépense neuve ; minuterie au plus tard 2026-11-27T22:00:00Z |
| § 1, « Coupure propre de l'étalonnage » ; additif 1, § 1 | la règle de la surveillance reste et joue, au seuil que porte le code de la voie (16 USD avec le correctif 0013 ; l'exécutante le confirme à l'arbre de la voie) ; l'échéance de la machine (6,5 heures au plus, soit 8,97 USD de carte au prix borne) la précède dans tous les cas |
| § 1, « Configuration », « Fichier d'entrées », « Entropie » ; § 2 | § 3.2 de cet additif |
| § 2 et § 5, étape 1, `IIB_DEPENSE_ANTERIEURE_USD=0` | la dépense antérieure déclarée de C3 |
| § 5, étape 1, `--verifier-go-seulement 55` | `--verifier-go-seulement 55 <dépense antérieure déclarée>` |
| § 5, étape 2, `creation auto course 0 <dossier> 1796076000` | `creation auto course <dépense antérieure déclarée> <dossier> <échéance>` ; échéance par `echeance 42 <compte> $(date +%s) 6.5 5.5` |
| § 5, étape 4, durées | 3,58 heures attendues, 5,19 au haut [L12] ; chaque lot scellé est poussé (correctif 0014) |
| § 5, étape 7, sort de la machine | destruction après le rapatriement vérifié et la désignation scellée (C2) |
| § 9, devis | le devis de la voie (A) |
| additif 1, § 2 (rien n'est poussé avant la fin) et § 3 (relance de la surveillance) | sans objet sous le code de la voie |

## 4. Voie (A), partie II : ordre de la course

### 4.1 Ce que la course est, et n'est pas

- **Elle est** la course du maître de l'organisme retenu, telle que le texte scellé la décrit (sections 13 et 15 ; devis scellé, § 4 ; errata) : par tour, 32 épisodes du maître sous la consigne privée de la variante désignée et 320 actions de l'oracle désigné ; tour de contrôle au tour 4 ; fin dès 96 épisodes acceptés, ou au dernier tour ; puis la distillation de l'élève et du témoin-jumeau (48 à 127 épisodes), les actions de l'autre oracle hors tours (au plus 3 830), et l'évaluation (256 épisodes, quatre conditions). Nombre de tours : celui de la désignation.
- **Elle n'est pas** un préenregistrement, une lecture de sonde, une pièce de G0. Aucune activité interne n'est enregistrée ; aucun score de moniteur n'entre nulle part.
- **Elle ne part que si** la désignation scellée de la voie rend l'oracle à contexte réécrit ou l'oracle au contexte de l'agent. Sinon la voie est en échec (C5), et les phrases écrites d'avance (10.6) sont rendues.

### 4.2 Cadre

| Élément | Valeur |
|---|---|
| Code | celui de la voie (§ 2) : le même arbre que l'étalonnage rejoué |
| Amorce | `scripts/amorce_instance_iib_course_v5.sh`, choisie par `IIB_AMORCE` ; liste figée `scripts/tests-cibles-iib-course-v5-v1.txt` ; essais attendus du § 2 |
| Configuration | écrite par programme (`designation_v5.configuration_de_course`) depuis la configuration de la voie : seuls changent `oracle_de_la_regle` (valeur, chemin et empreinte de la désignation) et `prefixe_graines` (`course/`, correctif 0018, même entropie) ; scellée. Le code refuse une configuration qui diffère autrement de celle du manifeste de l'étalonnage : **le chemin de tirage de la course est donc celui de l'étalonnage** |
| Commit de la course | enfant direct du commit de lancement de l'étalonnage de la voie, sur la branche du code de la voie ; il n'ajoute que les sorties scellées rapatriées de l'étalonnage de la voie (`diag/<run>/`, `donnees/<run>/lots/`, `runs/<run>/`), le résultat du passage des conditions, la configuration de la course et leurs sceaux. **Il porte une et une seule désignation scellée**, celle de la voie (l'amorce refuse sinon) ; rien de la voie (B) |
| Branche poussée par la machine | `essai/iib-explo-v9`, absente du distant, contrôlée |
| Carte | celle de l'ordre scellé (§ 1, ligne « Carte ») ; fenêtre vide : nœud |
| Accord, échéances | C1 ; coupure de la voie 42 USD de dépense neuve ; échéance de la machine par `echeance 42 <compte> $(date +%s) 30 11` |
| Mode | `reel`, `PREREG_ABSENT=1`, `GO_ID=GO-2026-11-21-70` |
| Exécutante | `session_01XJ6MgqUTEVCed6a2f6rWmC` (branche `claude/iib-executante-v5`) |

### 4.3 Préalables, dans l'ordre

1. Désignation scellée de la voie, d'issue « N » ou « P » ; configuration de la course écrite par programme et scellée ; commit de la course poussé.
2. **Contrôles à blanc à ce commit, sans dépense** : garde de la configuration en code 0 ; liste figée de la course rejouée, dernière ligne égale au nombre attendu ; `--verifier-go-seulement 55 <dépense antérieure déclarée>` en code 0 ; `controles-explo` avec `IIB_AMORCE` en code 0 ; `git ls-remote --exit-code origin refs/heads/essai/iib-course-engagee-<run de l'étalonnage>` rend 2 (référence absente) ; les trois sous-commandes du programme de calcul rejouées sur leurs cas de contrôle ([L21], [L22], [L53] à [L57]) ; tout écart : arrêt.
3. Aucune machine du saboteur sur le compte (C2) ; compte de la voie relevé ; crédit relu (C7) ; échéance et garde de rythme calculées (C3, C4), portées au compte rendu avant la création.

### 4.4 Étapes de l'exécutante

1. **Variables** : `GO_ID=GO-2026-11-21-70`, `IIB_AMORCE=scripts/amorce_instance_iib_course_v5.sh`, `IIB_BRANCHE_CODE` (branche du code de la voie), `IIB_BRANCHE=essai/iib-explo-v9`, `IIB_DEPENSE_ANTERIEURE_USD` (C3), `IIB_TESTS_ATTENDUS` (§ 2), `IIB_INSTANCES_INTOUCHABLES`, `IIB_REGISTRE_GO`, `IIB_REGISTRE_DECISIONS`, `PREREG_ABSENT=1`, les jetons par leur nom ; jamais `IIB_AUCUNE_INTOUCHABLE`.
2. **Création** : `creation auto course <dépense antérieure déclarée> <dossier> <échéance>` ; la commande imprimée est exécutée une seule fois ; fenêtre et codes comme à l'ordre scellé (§ 5, étape 2).
3. **Engagement — à lire avant d'exécuter la commande.** Dès son premier démarrage, l'amorce pousse la référence `essai/iib-course-engagee-<run de l'étalonnage>`, avant l'installation. **Toute fin anormale de l'amorce, échec de la suite d'essais sur la carte compris, consomme la seule course permise sur cet étalonnage.** Aucune relance sans le mot de Lazar, un devis neuf et la suppression de la référence par la mère.
4. **Sur la machine** : engagement ; installation ; liste figée de la course, moteur à torch du distillateur compris ; chargement du modèle ; tours du maître ; tour de contrôle ; distillation ; évaluation ; chaque lot scellé est poussé ; à la fin, sorties scellées et poussées, machine mise à l'arrêt, disque gardé.
5. **Surveillance** : comme à l'ordre scellé (§ 5, étape 3), sans la règle de la coupure propre, qui ne joue pas pendant la course. S'y ajoutent la garde de rythme (C4) et la vérification avant l'échéance (C3).
6. **Rapatriement, machine arrêtée, avant toute destruction** : comme à l'ordre scellé (§ 5, étape 5) : chaque fichier listé est vérifié un par un ; le nombre vérifié est égal au nombre listé. Aucune sortie n'est ouverte.
7. **Destruction** après le rapatriement vérifié (C2).
8. **Compte rendu** (nombres et états seuls) : ceux de l'ordre scellé (§ 5, étape 8), plus : la dépense antérieure déclarée et le compte réel ; l'échéance et les délais de la garde de rythme ; les heures des marques du tour 1 et du tour 4 ; la fin de la course parmi les fins écrites d'avance, telle que la disent la dernière marque et le nom des fichiers versés ; le compte de la voie et celui de la ligne.

### 4.5 Sorties et lecture

Noms et versement : ceux du code de la course (témoin d'engagement `diag/<étalonnage>/course-engagee-iib-v5.json`, sorties des tours et de l'évaluation sous `diag/<étalonnage>/`, manifeste et résumé du run de la course) ; chaque fichier scellé et rattaché au manifeste. Toute citation porte : la phrase de 10.6 qui convient, la clause du premier coût, la mention « exploratoire, non opposable », la réserve de C5, et le chemin de tirage employé.

## 5. Arrêts de la voie (tous par identifiant de machine, R10)

- **Avant toute création, aucune création** : un champ du § 6 encore entre chevrons ; une machine du saboteur sur le compte, 61875617 comprise ; crédit insuffisant ; code 3 du programme (`echeance`, `garde-de-rythme`) ; un contrôle en code non nul ; branche d'essai déjà présente ; ligne d'accord absente ou échue ; heure à partir de 2026-11-27T00:00:00Z ; fenêtre d'offres vide ; l'autre voie a abouti (C5).
- **Essai de vitesse** : « NE PART PAS » ; chemin neuf non reproductible ; échéance : la voie s'arrête, nœud.
- **Étalonnage rejoué** : les arrêts de l'ordre scellé (§ 6), la coupure propre de l'étalonnage, l'échéance de la machine ; issues « ne part pas » et « non calculable » : la course ne part pas, les résultats sont versés et scellés.
- **Course** : référence d'engagement déjà présente ; suite d'essais en échec ; toute garde du texte scellé ; garde de rythme ; échéance ; crédit épuisé. Les fins écrites d'avance (tour de contrôle, consigne sans effet, moins de 48 épisodes acceptés) ne sont pas des pannes : la course a abouti.
- **Aucun arrêt n'est suivi d'une relance sans nœud de Lazar et devis neuf ; aucun réglage en cours ; aucun repli silencieux ; aucun second passage des conditions ; aucune sortie supprimée avant son versement scellé.**

## 6. Champs à remplir avant le scellement

Un champ est écrit entre chevrons doubles. **Tant qu'un seul reste dans le texte, l'additif n'est pas scellé, et rien n'est créé.** Ils sont remplis par programme, dans une version nouvelle du texte.

| champ | ce qu'il attend | qui le remplit |
|---|---|---|
| `<<LECTURE_DES_PLAFONDS_CONFIRMEE_PAR>>` | la ligne du registre ou le mot qui confirme que 44 USD est le plafond de la dépense neuve de la voie | mère (mot de Lazar) |
| `<<SENS_DE_REUSSIT_CONFIRME_PAR>>` | la ligne du registre qui confirme la règle de C5 | mère (mot de Lazar) |
| `<<MOT_DE_LA_MERE_DESTRUCTION_61875617>>` | le mot de la mère, daté | mère |
| `<<CORRECTIF_LANCEUR_PLUSIEURS_MACHINES>>` | « aucun », ou chemin, empreinte et vérification du correctif | mère ou exécutante |
| `<<CORRECTIF_0020_CHEMIN_ET_EMPREINTE>>`, `<<RAPPORT_0020_CHEMIN_ET_EMPREINTE>>`, `<<CONTRE_LECTURE_ET_VERIFICATION_0020>>`, `<<LEVEE_DES_EXIGENCES_0020>>` | les pièces du correctif du tirage sur la carte | exécutante |
| `<<BRANCHE_CODE_VOIE_A>>`, `<<COMMIT_CODE_REVU_VOIE_A>>`, `<<ARBRE_CODE_VOIE_A>>`, `<<CLE_DU_CHEMIN_DE_TIRAGE>>`, `<<EMPREINTES_AMORCES_ET_LISTES_VOIE_A>>`, `<<TESTS_ATTENDUS_ETALONNAGE_VOIE_A>>`, `<<TESTS_ATTENDUS_COURSE_VOIE_A>>`, `<<LANCEMENT_ESSAI_DE_VITESSE>>` | le code de la voie | exécutante, vérifié par la mère |
| `<<ENTROPIE_VOIE_A>>` | l'entropie neuve et la ligne du registre des décisions qui la consigne | mère |
| `<<INSTANCES_INTOUCHABLES>>` | les machines des autres chantiers, relevées à l'inventaire en champs filtrés ; liste non vide | exécutante |

**Relevés en cours de voie, et non champs** (ils n'existent qu'après une étape ; chacun est porté au compte rendu de cette étape et vérifié par la mère avant l'étape suivante) : le chemin et l'empreinte du fichier d'entrées et de la configuration de la voie (après l'essai de vitesse) ; le commit de lancement de l'étalonnage ; le run de l'étalonnage ; le commit de la course et sa configuration (après la désignation).

Empreinte du devis de la voie, à relever dans son compagnon au scellement : `devis-voie-A-v1-brouillon1.md.sha256`.

## 7. Points rendus à la mère par le rédacteur

1. **Lecture des plafonds** (C1) et **sens de « réussit »** (C5) : deux nœuds pour Lazar ; l'additif écrit la lecture prudente pour la validité (fin écrite d'avance, sans regard au résultat) et la lecture littérale du registre (dépense neuve).
2. **Une machine à la fois** (C2) : le « en parallèle » de l'accord n'est pas exécutable par le lanceur actuel ; correctif du lanceur, ou machines l'une après l'autre.
3. **Dépense antérieure bornée à 5 USD** (C3) : la valeur déclarée peut être inférieure au compte réel ; c'est dit, et la voie est tenue par les échéances. Corriger la garde du lanceur est un travail de code, non fait ici.
4. **L'échéance détruit** (C3) : ce qui n'est pas poussé à cet instant est perdu ; la poussée par lot et la consignation la précèdent.
5. **Fichier d'entrées** (§ 3.2) : la dépense passée porte une écriture de 13 USD ; le code ne permet pas d'écrire un autre plafond que 45.
6. **Entropie neuve** (§ 3.2) : à tirer par la mère avant la configuration.
7. **Essai de vitesse** (§ 3.1) : sa manière de se lancer n'existe pas encore ; ses exigences sont écrites ; le fichier d'entrées et la configuration de la voie ne peuvent être scellés qu'après lui.
8. **Jamais éprouvés avant la machine** : le chemin neuf sur une carte, le mode réel de la course, le moteur à torch sur carte, la minuterie de l'amorce de la course.
