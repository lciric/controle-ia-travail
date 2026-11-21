# Plan du branchement — l'expérimentateur et l'étage des tests de mort sur la course principale d'auto-conception — v1

**EN ATTENTE DE LA NOTE.** La note de conception générale des expérimentateurs et des tests de mort (registre, R-4372) ne m'a pas été transmise avant la fin de ce travail. Ce plan ne la cite pas, ne l'invente pas et ne lui a pas été confronté. Les points qu'elle doit trancher sont marqués « attend la note ». Une v2 la citera et dira ce qu'elle change.

Pièce de travail (classe C), non contre-lue, non scellée. Elle planifie ; elle ne tranche rien. Processeur seul : aucun appel, aucune dépense, aucun code lancé, aucune écriture dans un dépôt.

- Auteur : planificateur du branchement de l'expérimentateur, modèle F. Je n'ai écrit aucun orchestrateur, aucune conception de véhicule, aucune pièce du palier 1.
- Date (UTC) : 2026-11-21 ; relevé de `date -u` : 07:07:01Z, après la lecture des pièces, avant l'écriture.
- Mandat : `docs/notes/organisme-auto-conception-v1/mandat-planificateur-experimentateur-tests-de-mort-course-principale-v1.md` (`e4ca4586cd603fbf79486752604158fca8c5595d51e6af26e0309ce0f35d80d0`, égale à son compagnon), lu en entier.
- Lecture : `origin/main` du dépôt de l'organisme au commit `332080c5f64d436627351cfbfc17a9603248454c` pour les deux registres ; le disque de `/home/user/controle-ia-travail-organisme` pour les pièces ; le dépôt de l'orchestrateur à `/home/user/lciric/ideation-organism` pour deux fichiers de code. Pièces et empreintes : rapport joint et table jointe.
- Ce texte ne porte aucun identifiant de modèle, aucun nom de clé, aucune méthode d'attaque.

Sigles de renvoi : A69, l'additif des interrupteurs de la v69, v4 (`cb352811…`) ; C70, le cadre de la v70, v3 (`b1822613…`) ; R68, le rapport du développeur de la v68 (`ad42b722…`) ; F68, la fiche des quatre décisions, v7 (`5ddfae18…`) ; L10, le lanceur de course v10 (`f4196ec5…`) ; NA, la conception du véhicule NA-1 (`675f8d39…`) ; DH, le devis de l'héritage v5 (`30c87fa6…`).

## 0. En bref

1. **Rien ne joue aujourd'hui l'expérimentateur ni un test de mort réel sur la course principale.** Le lanceur v10 porte l'interrupteur `tests_de_mort_reels`, éteint, et refuse le moteur réel par construction pour cinq raisons écrites (L10, l. 606 à 619). La v68 corrige trois de ces raisons du côté de l'orchestrateur, en moteur simulé seulement.
2. **Le manque de fond n'est pas du code.** Une carte d'auto-conception propose un mécanisme pour l'organisme, pas une loi sur des données ; un test de mort calcule une statistique sur une colonne d'un fichier, contre un seuil. Aucune pièce lue ne dit sur quelles données le test d'une carte porterait (F68, décision 3). Lazar a tranché (3a) « champs de fiche inchangés » le 20 novembre : son mot du 21 rouvre ce point. **C'est la décision qui commande tout le reste (§ 6, D2), et c'est ce que j'attends de la note.**
3. **Dix lots**, numérotés E0 à E9 : un relevé du code sans écriture, puis neuf lots de code. Deux sont communs avec le palier 1 (ils s'écrivent une fois, dans la v69) ; trois reprennent des lots du véhicule NA-1 au lieu de les récrire. Reste propre à cette course : le pont entre la carte et l'épreuve, les mondes, la boucle à plusieurs générations avec étage, le lanceur.
4. **Calendrier, dit sans forcer** : environ 38 heures de sessions de développeur et de vérificateur, environ 23 heures de textes autour. Trois à cinq jours d'horloge après le mot de Lazar sur D2, si la place du modèle F n'est pas prise par le véhicule NA-1 et si le palier 0b est lu.
5. **Le bac coûte peu ; l'étage coûte.** Location de la machine jetable : de l'ordre de 0,5 dollar au cas bas, 3,3 au cas haut, 10,6 au cas pire, à un tarif relevé le 11 novembre et non relevé aujourd'hui. Les appels de l'expérimentateur et du lecteur n'ont aucun coût mesuré par tentative : de 0,06 à 0,90 dollar selon des bornes écrites dans le code.
6. **Sept décisions reviennent à Lazar** (§ 6). Aucune dépense n'a de défaut.

## 1. Ce qui existe

« Disque » : le disque de `/home/user/controle-ia-travail-organisme`. Chaque empreinte est recalculée par moi (table jointe). Le dossier `docs/notes/organisme-auto-conception-v1/epreuves-v9/` est abrégé `…/epreuves-v9/`.

### 1.1 Les mots de Lazar et le registre

| pièce | ce qu'elle dit | ligne |
|---|---|---|
| GO-2026-11-19-75 | l'expérimentateur modèle est gardé ; le lecteur n'est pas visé | `registres/go.md`, l. 508 |
| GO-2026-11-20-05 | (1a) tests de mort sans rien servir, **pour la seule épreuve du palier 1** ; version suivante, lanceur 11 et additif écrits en routine pour ce seul régime ; allumage sur devis et ligne. (2b) la génération suivante lit le registre des tentatives et leur classe. **(3a) les champs de fiche de la course d'auto-conception restent inchangés.** (4b) machine jetable sous le devis du premier étage payant, essai du bac en première étape | l. 536 |
| GO-2026-11-20-10, point (O3) | orchestrateur v69 : D1 (a′), D2 (a), D3 (a) | l. 541 |
| GO-2026-11-21-16 | le régime « tests de mort réels » s'étend à la course « seuil et moniteurs » ; **priorité dite** : expérimentateurs et tests de mort d'abord sur la course principale et sur les mathématiques nouvelles | l. 615 |
| R-3882 | palier 0a : l'étage exécute une loi plantée sans réécriture, à l'identique en exécuteur factice et dans un vrai bac local ; deux manques : l'étiquette « loi plantée retrouvée » dépend du juge statistique ; aucun générateur de mondes à plusieurs lois | `registres/decisions.md`, l. 4020 |
| R-4131 | A69 v4 et C70 v3 scellés par la mère ; aucun allumage | l. 4269 |
| R-4369, R-4372, R-4386 | la question de Lazar ; la note de conception commandée ; la priorité transmise | l. 4507, 4510, 4524 |

**Lecture.** La ligne 16 étend le régime à une autre course, et dit une priorité pour la course principale. Elle n'accorde pas l'allumage sur la course principale, et ne lève pas (3a). Je le porte à Lazar (§ 6, D1 et D2) plutôt que de le lire à sa place.

### 1.2 Le code et les textes

| pièce | chemin | empreinte | état |
|---|---|---|---|
| orchestrateur, commit de base | `/home/user/lciric/ideation-organism`, commit `a41b7b50…` | — | a porté la course v9 en réel, une génération, sans étage |
| étage entre générations v57 | `orchestrator/pole/etage_entre_generations_v57.py` | `e4bf3681…` | machine jetable exigée, puis étage v5, puis sélection des seules « survit » ; lu en entier ; joué en réel par le chemin du tour fermé (course v67), jamais par la course à plusieurs générations |
| étage des tests de mort v5 | `orchestrator/pole/tests_de_mort_v5.py` | `da524871…` | non ouvert par moi ; verdict calculé par le noyau depuis le fichier brut (docstring de la v57) |
| lanceur du tour fermé à plusieurs générations | `orchestrator/demonstrations/ideation_v59.py` | `5419137c…` | lu en entier ; la génération 2 s'arrête (`JSONDecodeError`), constaté à blanc (R68, § 7) |
| tour fermé v64 | `orchestrator/pole/tour_ferme_v64.py` | `35a8294e…` | non ouvert par moi ; forme imposée, contre-calcul hors du bac ; a tourné en réel (course v67) |
| paquet v68, huit fichiers neufs | `…/epreuves-v9/orchestrateur-v68/paquet/` ; manifeste `manifeste-paquet-orchestrateur-v68-v1.json` | `4ed9fd8e…` | contre-lu « Conforme » ; **moteur simulé seulement** ; refuse le moteur réel par construction ; essai à blanc 18 vérifications sur 18 (`11f56996…`) ; versé sur `main` (R-4383, R-4385) |
| rapport et contre-lecture de la v68 | même dossier | `ad42b722…`, `d2cfeac1…` | lus (rapport en entier, contre-lecture : en-tête et constats 1 et 2) |
| fiche des quatre décisions v7 | même dossier | `5ddfae18…` | contrôlée « conforme » ; décisions 3 et 4 lues en entier |
| additif des interrupteurs v69, v4 | `…/epreuves-v9/orchestrateur-v69/additif-interrupteurs-orchestrateur-v69-v4.md` | `cb352811…` | **scellé** ; lu en entier ; un seul régime, une seule épreuve : le palier 1, une génération ; **aucun code de la v69** |
| cadre de la v70, v3 | même dossier, `cadre-lecture-registre-orchestrateur-v70-v3.md` | `b1822613…` | scellé comme cadre, non comme règle d'un lancement ; lu en entier ; aucun code |
| lanceur de course v9 | `scripts/lancer_course_auto_conception_v9.py` | `1b47c1cf…` | a lancé la course v9 ; une génération, aucun étage |
| lanceur de course v10 | `scripts/lancer_course_auto_conception_v10.py` | `f4196ec5…` | éteint, égal au v9 ; allumé, **refusé en réel** ; lu : l. 1 à 140 et 526 à 625 |
| épreuve des témoins v9 | `scripts/epreuve_temoins_auto_conception_v9.py` | `5be161fa…` | a joué l'épreuve réelle de la course v9 ; non ouvert par moi |
| lanceur de course 11 | aucun fichier | — | décrit par A69, § 7 ; non écrit |
| configuration des interrupteurs | `…/epreuves-v9/rang-0-branchement/configuration-interrupteurs-course-auto-conception-v1.json` | `bb4ecbfb…` | tranche et liste blanche « à remplir » (L10, l. 617) ; non ouverte par moi |
| configuration v5 de la course | `docs/notes/organisme-auto-conception-v1/course-v4/configuration-course-auto-conception-v5.json` | `3f662ee8…` | dix champs de fiche, aucun des quatre champs de test (F68, décision 3) ; non ouverte par moi |
| préenregistrement de la course, v2 | `docs/notes/organisme-auto-conception-v1/course-v2/preenregistrement-course-auto-conception-v2.md` | `0d51e0b3…` | **scellé ; écrit « pas de tests de mort » et « une seule génération »** (F68, décision 3, qui cite sa ligne 57) ; non ouvert par moi |
| palier 0a | `…/epreuves-v9/heritage/palier-0a/rapport-palier-0a-v1.md` | `93d8a104…` | joué, 0 USD ; non ouvert par moi |
| palier 0b | préenregistrement v19 scellé (`883b1b2a…`, GO-2026-11-21-09) | — | lancement accordé le 21 novembre ; **non lu** à l'heure où j'écris (R-4363) ; ses livrables (monde planté, comparateur sans juge, enveloppe de l'étage) sont attendus par A69, § 9, point 4 |
| conception du véhicule NA-1 | `docs/notes/ideation-nouvelles-attaques-v1/conception-vehicule-v1/conception-vehicule-course-nouvelles-attaques-v1.md` | `675f8d39…` | rendue, contre-lecture accordée (R-4381) ; lue en entier ; **son régime retire l'étage et la machine jetable** (NA, § 1.2) |
| course réelle v67 | `docs/notes/organisme-boucle-reelle-v1/course-v67/verdict-course-v67-v1.md` | `d7902432…` | le seul relevé réel de tests de mort : 14 tests, vrai bac, machine louée ; quatre lignes lues |

### 1.3 Les cinq blocages écrits dans le lanceur v10, et où ils en sont

| blocage (L10, l. 606 à 619) | levé par | reste |
|---|---|---|
| bornes des relais, parts au pire, crédits, porte à blanc et bilan de coût comptés pour une génération | personne | à refaire pour N générations et pour les appels de l'étage (lot E8) |
| la génération suivante ne sait pas lire la sélection | la v68, en simulé (R68, § 3, point 1) | (2b) demande le registre entier, non la sélection : C70, aucun code |
| **fiches sans champ de test : chaque fiche serait refusée à l'étage** | personne ; (3a) le maintient | **décision D2** |
| machine jetable sans secret, relais hors d'elle | (4b) dit sous quel devis ; A69, § 5.3 et § 5.4, dit comment | rien de loué ; rien d'écrit pour la durée de location |
| tranche et liste blanche à remplir ; vrai bac jamais rejoué avec l'étage v5 | F68 corrige la seconde moitié : le vrai bac a tourné deux fois avec l'étage (course v67 ; palier 0a en local) | **aucune tranche de données pour cette course** : décision D2 |

## 2. Ce qui manque

Pour faire jouer l'expérimentateur modèle et l'étage des tests de mort réels entre les générations de la course principale, avec l'héritage récompensé (N-044, N-045).

### 2.1 Ce qu'un test de mort éprouve, pour une carte — attend la note

1. **L'objet de l'épreuve.** Trois lectures possibles, que je ne tranche pas : (i) la carte porte un engagement à forme imposée sur un monde planté scellé d'avance, comme le tour fermé ; (ii) la carte reste telle quelle et un pont écrit par l'orchestrateur en tire l'engagement ; (iii) l'épreuve d'une carte est une course de l'organisme sur monde planté (F68 : « l'épreuve d'un mécanisme, c'est une course de l'organisme sur monde planté, pas un script »), que l'étage actuel ne sait pas jouer.
2. **Les données.** Une tranche d'épreuve, une tranche de contrôle (A69, § 4.4), une part servie, disjointes, tirées par graine (règle R9), scellées avant la génération. Aucune n'existe pour cette course.
3. **L'oracle.** La composition se juge sur l'oracle du monde planté et sur le coût, jamais sur le verdict du juge (N-058). L'étiquette « loi plantée retrouvée » dépend aujourd'hui du juge statistique (R-3882) : il faut le comparateur sans juge du palier 0b.
4. **Les mondes.** Aucun générateur de mondes à plusieurs lois vraies composées (R-3882). Des tâches fraîches par génération (N-049) demandent un vivier.

### 2.2 L'orchestrateur

1. **Un sommet d'étage neuf** qui passe les plafonds à l'étage : celui de la v69 (A69, § 1.2, option (a′)). Il n'existe pas. Il est écrit pour une génération ; la course principale en veut plusieurs.
2. **L'enveloppe de l'étage** : lots de douze tentatives au plus, ordre du scellement sans juge, statut « non éprouvée (budget) », seuil scellé vérifié. Livrable du palier 0b.
3. **Le pont entre la carte et la fiche de l'étage**, selon D2 : garde de forme imposée, garde de l'entrée de l'expérimentateur (A69, gardes 9 et 10).
4. **Les classes d'issue** : « tient », « ne tient pas », « non exécutable ou indéterminée », statut « non éprouvée (budget) », et un verdict précis par « tient » (A69, § 4). Le mot « survit » ne sort d'aucun fichier neuf.
5. **Une course à plusieurs générations avec étage**, en réel : la v68 la joue en simulé ; son régime « tests de mort sans rien servir » accepte N générations (R68, § 5), A69 le restreint à une.
6. **La lecture par la génération suivante** : le registre des tentatives et son lecteur (C70, § 3, points 4 à 8). C'est par là que passe l'héritage. Rien n'est écrit.
7. **La récompense de l'héritage et le coût rendu à l'organisme** (N-044, N-045) : aucune pièce lue ne dit comment une génération est récompensée de ce qu'elle lègue, ni quel coût est rendu au signal. Attend la note, ou une conception à part.
8. **L'ordre des rôles** : la course v9 joue un aiguilleur et deux juges ; A69 n'en joue aucun à l'étage. Sur la course principale, les juges restent-ils, pour information seulement ? Non fixé.

### 2.3 Le lanceur, l'additif, la configuration

1. **Un lanceur de course neuf**, à la suite du 11 : il épingle le paquet v68, les fichiers neufs, la chaîne du tour fermé, l'additif, le préenregistrement, la configuration, les tranches ; il compte les bornes des relais et les parts pour N générations plus les appels de l'étage ; il porte la durée maximale de location et l'identifiant de la machine (A69, § 7, transposé).
2. **Un additif des interrupteurs pour cette course** : A69 ne vaut que pour le palier 1 et dit qu'il « ne touche pas la course d'auto-conception » (§ 8). Régime nommé, ce que reçoit chaque rôle, classes, liste d'arrêt.
3. **Un préenregistrement neuf de la course** : le v2 scellé écrit « pas de tests de mort » et « une seule génération ». Hypothèse, prédiction chiffrée, métrique, seuil, critères de lecture, liste d'arrêt (règle R1) ; contre-lu (règle R2).
4. **Une configuration** : étage, tranche, liste blanche, budgets par test et par lecteur, exécutions par fiche, délai, mémoire, plafond de l'étage (les quatorze clés d'étage de L10, l. 597 à 599), portée « par génération ».
5. **Une ligne d'accord de calcul** qui nomme l'interrupteur, l'épreuve, les empreintes, au montant au pire.

### 2.4 Le bac

1. Une machine louée, sans aucune clé, identité dédiée sans compte, bac et ses outils installés ; les relais restent hors d'elle.
2. L'essai du bac en première étape, sans appel de modèle : sonde complète, borne de mémoire, un étage complet à expérimentateur et lecteur écrits par programme, retrait vérifié (A69, § 5.4) ; attestation scellée.
3. Une durée de location bornée, tenue par du code : à la course v67, le plafond de la machine n'était tenu par aucun code.
4. La destruction par l'identifiant du serveur, consignée dans `registres/arrets.md` (règle R10).
5. Où tourne quoi : le verdict de la v67 dit que la course tournait détachée sur la machine louée, avec des appels relayés. Comment les relais restaient hors d'elle n'est pas dans les lignes que j'ai lues : question du lot E0.

### 2.5 Les mesures et les gardes

1. **Mesures** : le coût réel d'un test par tentative (jamais mesuré, DH, § 5) ; les classes par espèce et par génération ; la part « non éprouvée (budget) » ; les refus avant l'épreuve ; l'oracle du monde planté ; ce qui est lu de la génération précédente et ce qu'il coûte.
2. **Gardes** : les vingt d'A69, § 6, chacune avec son cas sain et son artefact (règle R5), transposées à N générations ; plus, si la lecture est allumée, celles de C70, § 3, point 8. Trois mutations au moins par lot.
3. **Aucun score de moniteur dans l'entraînement de l'agent** (N-053) : sans objet ici si aucune carte ne lit un moniteur ; à écrire à l'additif.

## 3. Les lots O et S

Un lot est écrit par un développeur O et vérifié par un vérificateur S, sur un mandat tiré de la conception. Fichiers neufs seulement (règle R12) ; paquet, manifeste et programme d'application à la manière de la v68.

| lot | contenu | dépend de | partagé avec |
|---|---|---|---|
| E0 | **relevé du code, sans écriture** : questions fermées ci-dessous | — | **NA-1, lot 0** : ses questions 2, 5, 7, 8, 9, 10 et 11 valent ici ; elles se lisent dans sa réponse, elles ne se reposent pas |
| E1 | sommet d'étage neuf et enveloppe (plafonds passés à l'étage, lots de douze, ordre du scellement, tranche à son propre chemin, contre-calcul) | E0 ; livrables du palier 0b | **palier 1 : c'est la v69.** Écrit une fois. Ce plan ne le récrit pas : il demande qu'il accepte N générations dès l'écriture (D5) |
| E2 | pont entre la carte et la fiche de l'étage ; garde de forme imposée ; garde de l'entrée de l'expérimentateur et du lecteur | E0 ; **D2 ; la note** | propre à cette course ; les gardes 9 et 10 d'A69 en sont le modèle |
| E3 | mondes et tranches : générateur ou vivier, tirage par graine, disjonction, scellement d'avance, liste blanche | D2 ; la note ; comparateur du palier 0b | la course « seuil et moniteurs » attend un mandat des mondes plantés (R-4377) : un seul programme de tirage et de disjonction pour les deux |
| E4 | classes d'issue, verdict précis, registre des tentatives en ajout seul, chaîne d'empreintes, prédiction scellée avant l'épreuve | E1 | **palier 1** pour les classes (A69, C6) ; **NA-1, lot 5** pour la forme du registre et de sa vérification |
| E5 | génération et course du régime : N générations, étage après chacune, garde de budget de la course, moteur simulé au contrat | E1, E2, E4 | base v68, comme NA-1, lot 6 ; la boucle est propre |
| E6 | lecture du registre par la génération suivante : interrupteur neuf, lecteur, garde des étiquettes, registre vide ou trop long, coût de lecture | E4, E5 ; **D4** | **NA-1, lot 5** (`registre`, `verifier_registre_servi`) : C70, § 5, laisse ouverte la question « un module ou deux » ; je propose un seul module de vérification, deux tables de champs |
| E7 | mesures et export | E4, E5 | forme de NA-1, lot 7 ; contenu propre |
| E8 | lanceur de course : épinglages, bornes des relais pour N générations et pour l'étage, parts, machine déclarée, durée de location, attestation du bac, ligne d'accord | E5 | NA-1, lot 8, pour les relais par clé et le compte sur N générations ; A69, § 7, pour le reste |
| E9 | mise en route et essai du bac ; essai à blanc de bout en bout (simulé, puis relais contre un faux fournisseur) ; chaque arrêt provoqué une fois | E7, E8 | **palier 1** pour l'essai du bac (A69, § 5.4) ; **NA-1, lot 9** pour le faux fournisseur |

Ordre : E0 ; puis E1 ; puis E2, E3 et E4 ensemble ; puis E5 ; puis E6 et E7 ensemble ; puis E8 ; puis E9. Chemin critique : E0, E1, E2, E5, E8, E9. E2 et E3 ne partent pas avant D2.

**Ce qui ne s'écrit pas deux fois.** Avec le palier 1 : le sommet d'étage, l'enveloppe, les classes, l'essai du bac, la garde de durée de location. Avec NA-1 : le relevé du code, la vérification d'un registre servi, les relais comptés sur plusieurs générations, le faux fournisseur. Ce qui n'est pas partageable avec NA-1 : son adaptateur gardé, sa garde de motifs, son portier, ses cases, sa quarantaine.

**Questions propres du lot E0**, chacune avec le fichier et la ligne en réponse :

1. Les fonctions du tour fermé qu'A69 reprend (`carte_servie`, `test_de_mort_impose`, `contre_calculer`, l'adaptateur de l'étage, le contrôle des parts) s'appellent-elles depuis un fichier neuf sans rien prendre au corps de `jouer_etage` (A69, § 1.2, points 2 et 3) ?
2. Où sont construits les adaptateurs réels des relais du tour fermé (A69, § 1.2, point 1 : lanceur absent de la copie lue) ?
3. Quelle version de l'étage la course v67 a-t-elle jouée, et est-ce celle que la course à plusieurs générations appelle (F68, décision 4) ?
4. Le sommet d'étage tient-il plusieurs étages dans une même course, chacun dans son dossier (A69, garde 17) ?
5. Quelles colonnes la statistique hors du bac lit-elle, et une tranche tirée pour cette course peut-elle garder ce format ?
6. Que peut porter `champs_fiche`, et que change un champ de plus à la consigne servie aux proposeurs ?
7. Sur la machine louée de la v67, où tournaient l'orchestrateur, les relais et les scripts ?
8. Ce que la mémoire qui évite les redites fait d'une carte déjà éprouvée.

Une réponse qui contredit ce plan revient au concepteur avant le lot concerné.

## 4. Le calendrier

Estimation en heures de session, sans appel payant. Repères lus : la v68, huit fichiers et 2 096 lignes, écrite en trente minutes et contre-lue en douze ; les heures de NA, § 8, lot par lot. Je compte comme NA, parce que les lots sont de même nature.

| lot | développeur O | vérificateur S | corrections et nouvelle vérification | somme | compté ici ? |
|---|---|---|---|---|---|
| E0 | 0,75 | 0,5 | — | 1,25 | oui ; 0,75 si la réponse du lot 0 de NA-1 est rendue |
| E1 | 2,5 | 1,25 | 1 | 4,75 | **non si la v69 est écrite pour le palier 1** |
| E2 | 2 | 1 | 0,75 | 3,75 | oui |
| E3 | 2 | 1 | 0,75 | 3,75 | oui |
| E4 | 1,5 | 0,75 | 0,5 | 2,75 | à moitié (classes partagées) |
| E5 | 2,5 | 1,25 | 1 | 4,75 | oui |
| E6 | 2 | 1 | 0,75 | 3,75 | oui, si D4 l'allume |
| E7 | 1,5 | 0,75 | 0,5 | 2,75 | oui |
| E8 | 3 | 1,5 | 1 | 5,5 | oui |
| E9 | 2,5 | 1,25 | 1 | 4,75 | oui |
| **somme** | **20,25** | **10,25** | **7,25** | **37,75** | environ 31,5 sans E1 et la moitié de E4 |

Autour du code :

| travail | heures |
|---|---|
| conception du véhicule de cette course, après la note et D2, et sa contre-lecture | 4 |
| dix mandats de code | 3 |
| mondes et tranches : rédaction, scellement d'avance par un agent neuf de la mère | 3 |
| additif des interrupteurs de la course, contre-lecture, corrections | 3 |
| préenregistrement neuf de la course, contre-lecture (règles R1 et R2) | 4 |
| devis de l'étage et du bac, contre-lu | 2 |
| contre-lecture du véhicule entier (règle R2) | 2,5 |
| essai à blanc joué, constats | 1,5 |
| **somme** | **23** |

**Lecture.** De l'ordre de 61 heures de sessions, 55 si la v69 du palier 1 est écrite d'abord. Sur le chemin critique : environ 25 heures de lots, puis la contre-lecture du véhicule et les scellements. **Trois à cinq jours d'horloge** après le mot sur D2, à deux files sans arrêt. C'est la même fourchette que la conception « seuil et moniteurs » donne pour son véhicule (R-4377).

**Ce que je ne peux pas dater.** Le mot de Lazar sur D2 ; l'arrivée de la note ; la lecture du palier 0b, dont dépendent E1 et E3 ; la place du modèle F, que le véhicule NA-1 occupe pour 30 à 36 heures d'horloge (NA, § 8). Parti le 21 novembre, un premier allumage avant le **26 novembre** ne me paraît pas tenable ; entre le 26 et le 28 si NA-1 et cette course se partagent la place.

## 5. Le devis du bac

Machine jetable sous le devis du premier étage payant à tests de mort (GO-2026-11-20-05, 4b). **Aucun prix n'a été relevé aujourd'hui** : aucun appel n'est permis à ce mandat. Les chiffres ci-dessous sont des calculs à la main sur des valeurs lues dans F68 ; le devis réel se refait sur un prix relevé du jour.

### 5.1 Ce qui est lu

| valeur | source | nature |
|---|---|---|
| 0,0577 euro de l'heure, plus 0,00096 pour l'adresse | F68, décision 4, qui cite `registres/depenses.md` sur `main`, ligne 415 | relevé du 11 ou du 12 novembre, non revérifié par moi |
| 1,15 à 1,25 dollar l'euro | F68, même passage | deux lignes du registre des dépenses |
| soit 0,0675 à 0,0733 dollar de l'heure | calcul à la main | — |
| machines déjà louées : 0,07 à 0,27 dollar chacune, pour 4 minutes à 3 heures 18 | F68, même passage | mesuré |
| course v67 : 14 tests de mort, journal de 14:21:52 à 15:07:22, machine ≈ 0,27 dollar | verdict de la v67, l. 164, 167, 199 | mesuré ; soit environ 3,3 minutes par test, tout compris |
| trois exécutions de 120 secondes au plus par tentative | DH, § 5 | valeur de la configuration d'essai, non un réglage |
| 94 cartes à la course v9, une génération | F68, décision 3 | mesuré |

### 5.2 Trois cas, location seule

| cas | hypothèses | heures de machine | location |
|---|---|---|---|
| bas | une génération, 94 tentatives, au rythme mesuré de la v67 ; une heure de mise en route et d'essai du bac | 7 (6,1 arrondies à l'heure entamée) | **0,51 USD** |
| haut | trois générations, 282 tentatives, 9 minutes chacune (6 d'exécution à la borne, 3 de sessions) ; deux heures de mise en route | 45 | **3,30 USD** |
| pire | trois générations, deux fois plus de tentatives (564), 15 minutes chacune ; trois heures de mise en route ; une seule machine | 144 | **10,56 USD** |

Au taux de change haut (1,25). **Plafond proposé pour le poste : 15 USD, et une durée maximale de location gelée au devis** (A69, garde 20). Le nombre de générations de la course principale n'est écrit nulle part : trois est mon hypothèse, reprise de NA-1.

### 5.3 Ce qui n'est mesuré nulle part

1. **Le coût d'un test de mort par tentative, en appels.** Bornes écrites dans le code : 0,06 dollar (un tour au prix prudent), 0,60 (plafonds par défaut de l'expérimentateur et du lecteur), 0,90 (borne du tour fermé, lecteur compris) (DH, § 5). Soit, pour 94 tentatives : 5,64 / 56,40 / 84,60 dollars ; pour 282 : 16,92 / 169,20 / 253,80 ; pour 564 à la borne : 507,60. Le seul relevé réel est celui de la v67 : 1,99 dollar pour 14 tests **et** 4 appels de proposeur, sur la forme imposée, avec d'autres modèles que ceux de cette course ; il ne se transpose pas.
2. **La durée d'une session de l'expérimentateur** sur une carte d'auto-conception.
3. **Le nombre de tentatives par génération** quand la course lit un héritage.
4. **Le bac sur le chemin de la course à plusieurs générations**, et avec des lots nombreux (A69, § 9, point 5).
5. **Le prix du jour** de la machine.

**Lecture.** La location est de l'ordre du pour cent de la dépense de l'étage. Ce qui pèse est l'expérimentateur. Le palier 1 de l'héritage existe pour mesurer ce coût (DH, § 5) : c'est un argument d'ordre (§ 6, D5). À ajouter au devis : les propositions de la course elle-même, 150 dollars de plafond par génération à la course v9.

## 6. Ce qui rouvre une décision de Lazar

Aucun défaut pour une dépense. Aucune de ces décisions n'est prise ici.

**D1 — Étendre le régime « tests de mort réels » à la course principale.**
- Décision : le régime, accordé pour la seule épreuve du palier 1 (GO-2026-11-20-05, 1a) puis étendu à la course « seuil et moniteurs » (GO-2026-11-21-16), s'étend-il à la course principale d'auto-conception ?
- Enjeu : A69 lie l'allumage à une épreuve nommée ; sans mot neuf, tout le véhicule de cette course s'écrit sans pouvoir s'allumer.
- Options : (a) oui, l'écriture en routine, l'allumage sur devis et ligne. Avantage : suit la priorité dite. Inconvénient : un troisième chantier d'étage à tests de mort avant qu'aucun n'ait tourné. (b) oui, après la lecture du palier 1. Avantage : le coût d'un test est mesuré avant. Inconvénient : retarde ce que Lazar veut d'abord. (c) non.
- Recommandation : (a), confiance 0,7. Aucun défaut.

**D2 — Ce qu'un test de mort éprouve sur une carte d'auto-conception (rouvre 3a).**
- Décision : les cartes de la course principale portent-elles un engagement exécutable, et sur quelles données ?
- Enjeu : c'est le blocage de fond. Changer les champs de fiche change la consigne servie et le préenregistrement scellé ; ne pas les changer laisse l'étage refuser chaque fiche.
- Options : (a) champs ajoutés, engagement à forme imposée sur un monde planté scellé d'avance. Avantage : l'étage et le contre-calcul existants servent. Inconvénient : un proposeur écrit le test que sa carte passe ; la course n'est plus comparable à la v9. (b) champs inchangés, un pont écrit par l'orchestrateur tire l'engagement de la carte. Avantage : (3a) tient à la lettre. Inconvénient : le pont décide de ce qui est éprouvé, sans texte qui le fonde. (c) l'épreuve d'une carte est une course de l'organisme sur monde planté, non un script. Avantage : éprouve le mécanisme lui-même. Inconvénient : l'étage actuel ne le joue pas ; coût sans commune mesure.
- Recommandation : **aucune avant la note** ; je ne la devance pas. Aucun défaut : écart à un texte scellé.

**D3 — Le nom de version.**
- Décision : sous quel nom s'écrit le véhicule de cette course ?
- Enjeu : 69 est réservé au palier 1 ; 69, 70 et 71 sont déjà portés par une autre lignée du même orchestrateur (registre, l. 2507, 2558, 2579) ; NA-1 a proposé une série propre.
- Options : (a) une série propre, la version dans le nom, « véhicule AC-1 », suffixe `_ac_v1`. Avantage : aucune collision. Inconvénient : une troisième série. (b) un numéro neuf vérifié libre. Avantage : une seule lignée lisible. Inconvénient : risque d'une collision de plus.
- Recommandation : (a), confiance 0,65, comme NA-1. Défaut sous 48 heures : (a) ; rien ne s'allume par un nom.

**D4 — Ce que la génération suivante lit.**
- Décision : à la course principale, la génération suivante lit-elle le registre des tentatives et leur classe (2b), ou rien d'abord ?
- Enjeu : c'est le canal de l'héritage (N-044, N-045) ; c'est aussi ce qui est servi à un agent, donc un nœud. GO-2026-11-19-76, point 2, réserve deux champs à la lecture du point 7 du palier 0b.
- Options : (a) rien de servi à la première course, lecture à la suivante. Avantage : un seul inconnu à la fois ; le lot E6 sort du chemin critique. Inconvénient : aucun héritage mesuré. (b) lecture du registre dès la première course. Avantage : mesure l'héritage. Inconvénient : dépend du palier 0b ; deux inconnus confondus.
- Recommandation : (a), confiance 0,6. Aucun défaut : ce qui est servi à un agent.

**D5 — L'ordre entre cette course, NA-1 et le palier 1.**
- Décision : dans quel ordre s'écrivent et s'allument les trois ?
- Enjeu : la place du modèle F est unique ; le palier 1 mesure le coût d'un test, que cette course suppose ; NA-1 a une échéance d'accord au 22 novembre, demandée au 26.
- Options : (a) palier 1 d'abord (sommet d'étage, bac, coût mesuré), cette course ensuite sur ce socle, NA-1 en parallèle sur l'autre file. Avantage : rien écrit deux fois ; le devis de cette course s'appuie sur une mesure. Inconvénient : la course principale part après le palier 1. (b) cette course d'abord, le sommet d'étage écrit pour elle. Avantage : suit la priorité à la lettre. Inconvénient : devis sur des bornes ; A69 à reprendre. (c) NA-1 suspendu. Avantage : libère la place. Inconvénient : son accord échoit.
- Recommandation : (a), confiance 0,6, avec le sommet d'étage écrit dès le départ pour N générations. Défaut sous 48 heures : (a) pour l'écriture seule.

**D6 — La dépense.**
- Décision : le devis de l'étage et du bac de cette course, quand il existera.
- Enjeu : aucun coût par tentative n'est mesuré ; aux bornes, l'étage pèse autant que les propositions.
- Options : (a) attendre la mesure du palier 1. (b) un devis sur les bornes, avec un plafond d'arrêt. (c) un essai du bac seul, quelques dollars, sous une ligne à part.
- Recommandation : (a), confiance 0,6. **Aucun défaut.** Rien ne se loue ni ne s'appelle sans devis contre-lu et ligne de calcul.

**D7 — Le préenregistrement de la course.**
- Décision : un préenregistrement neuf remplace-t-il, pour cette course, le v2 scellé qui écrit « pas de tests de mort » et « une seule génération » ?
- Enjeu : écart à un préenregistrement scellé ; hypothèse et critères de lecture à écrire avant tout résultat (règle R1).
- Options : (a) préenregistrement neuf, le v2 gardé tel quel pour les courses closes. (b) additif au v2.
- Recommandation : (a), confiance 0,75 : deux phrases du v2 sont contredites, un additif ne suffit pas. Aucun défaut.

**Hors de ce plan, à dire.** Le mot de Lazar nomme aussi « l'élaboration de nouvelles mathématiques pour l'attaque et la défense ». La précision de la mère borne ce plan à la course principale : le chantier des mathématiques nouvelles n'est pas planifié ici.

## 7. Réserves du planificateur

1. **La note n'est pas intégrée.** Le § 2.1, D2 et les lots E2 et E3 en dépendent.
2. **J'ai lu peu de code** : `etage_entre_generations_v57.py` et `ideation_v59.py` en entier ; L10 par parties. Je n'ai ouvert ni `tests_de_mort_v5.py`, ni `tour_ferme_v64.py`, ni le paquet v68, ni le lanceur v9, ni l'épreuve des témoins. Ce que j'en dis vient des rapports cités.
3. **La conception « seuil et moniteurs » n'a pas été ouverte** : le mandat ne donne que son dossier, et aucune commande de liste n'est permise. J'en tiens ce que dit le registre (R-4377).
4. **Les heures du § 4 et les cas du § 5 sont des estimations**, calculées à la main. Aucun prix n'est du jour.
5. **Le palier 0b n'est pas lu** : ses livrables sont supposés par E1 et E3.
6. Les pièces de `course-v4/` sont citées par leur empreinte, non ouvertes, hors ce qu'en dit F68.

— planificateur du branchement de l'expérimentateur, modèle F
