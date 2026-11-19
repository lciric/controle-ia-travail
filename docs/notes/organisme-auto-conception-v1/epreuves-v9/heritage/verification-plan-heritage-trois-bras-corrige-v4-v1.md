# Vérification de la version 4 du plan à trois bras corrigé de l'héritage et de son devis — v1

## En-tête

- **Vérificateur** : modèle O, auteur des vérifications des versions 2 et 3 (`verification-plan-heritage-trois-bras-corrige-v3-v1.md`, `b030e2749e79b6de1fc83feb8ca06dc12cdb18eba8d9a3483659d101d60986b5`, relue en entier). Il n'a écrit ni le plan, ni le devis, ni leurs programmes de calcul. Rédacteur des pièces vérifiées : modèle F.
- **Objet** : les quatre constats de la vérification de la version 3 ; les demandes de la mère pour la version 4 (paliers, règle de passage écrite d'avance, variantes à deux, trois et cinq espèces, test de mort par tentative, recommandations par nœud) ; le calcul neuf, rejoué ; et le différentiel v3 → v4, pour dire si un autre changement demande une contre-lecture complète.
- **Heures** (`date -u`) : début de lecture 2026-11-19T14:13:05Z (premier rejeu du calcul) ; début d'écriture 2026-11-19T14:16:09Z.
- **Commits lus** : branche `lot/compte-organisme-v1` à `e77b696568ea7c57339b3700f1b9e4c068abffb2` (tête locale égale à la tête distante ; la version 4 y est versée par `1dc161e1b4255fcbef8b2afbaa648a0a7ba92ac9`, 14:11:51Z) ; `main` lu à `8379ba96c02da34f9af138b00add09967d749a8b` (le rédacteur l'avait lu à `416a3342…` ; `main` a avancé depuis).
- **Empreintes vérifiées** (contenu lu, et compagnon `.sha256` ; toutes conformes) :
  - `plan-heritage-trois-bras-corrige-v4.md` : `6b0fd0650907c383e19f4548933604f0fa1b39889d8f6e721368f2b52de752f5` ;
  - `devis-heritage-trois-bras-v4.md` : `94698b6192322de220eb151a6ea0312d6e86712a57fdf057232db0c31b0542ea` ;
  - `calcul_devis_heritage_v4.py` : `2b5bbf4e05fe7a1e476a3bcfdadcd7ae4a61a4c3b301ed986388c68f30a392a9` ;
  - `calcul-devis-heritage-v4.json` : `f503c224de06bfa9760e63788ce101e915e6ef1ec566d012fa8ed91ef2240d5c` ;
  - inchangés, contre leur compagnon : plan v3 (`ad1226f6…`), devis v3 (`d5858427…`), vérification v3 (`b030e274…`), `calcul_devis_heritage_v2.py` (`5d21b393…`), `calcul-devis-heritage-v2.json` (`132a0764…`).
- **Autres lectures** : `registres/go.md` sur `main` (`72e52540c4b25997d0aa6057ea880bdc765e0cd09c5650b65a0b084da174f558`), lignes `GO-2026-11-19-60` à `GO-2026-11-19-74` ; `docs/decisions/decision-N-045-v2.md` sur `main` (`c7b05e39…`, conforme au plan), titre et point 4 ; pour les bornes du test de mort, dans le code de l'organisme (commit `a41b7b50f7c64ce488c120bb89ad3d25fb1dd1cb`), les seules lignes des cinq constantes citées et leurs deux fichiers par empreinte (`tests_de_mort.py` `fc5d3507…`, `tour_ferme_v64.py` `35a8294e…`, conformes ; valeurs 0,5, 0,1, 12, 0,80 et « 12 × 0,06 = 0,72 » trouvées telles que le devis les cite) ; le rapport du rang 0 et sa configuration d'essai, par empreinte seulement (`966a3870…`, `bb4ecbfb…`, conformes).
- **Différentiels** : `git diff --no-index` du plan v3 contre v4, mot à mot, lu en entier ; le devis v4 lu en entier, la structure ayant changé (son § 11 la décrit).
- **Calcul rejoué** : `calcul_devis_heritage_v4.py`, copié hors du dépôt et lancé deux fois (`python3 -I -B`) : deux sorties identiques à l'octet, d'empreinte `f503c224…`, égale à celle de la sortie versée.
- **Recherche « Ne pas écrire »** refaite avec mon programme des vérifications précédentes, hors du dépôt, sur les quatre fichiers de la v4 ; recherche à part des identifiants et noms de famille de modèles.
- **Cartes** : aucune ouverte. **Non lus** : le corps du code de l'organisme ; tout dossier interdit par le mandat.
- Aucun appel à un fournisseur de modèles, aucune dépense, aucun refus d'outil.

## Table des points demandés

| point | appliqué | où, et remarque |
|---|---|---|
| constat 1 de la v3 : ce que l'expérimentateur reçoit du champ `tentative` | **oui** | § 3.0 : liste exacte gelée au préenregistrement de l'étage sur processeur ; valeur proposée, l'engagement et la description bornée, chacun entre balises de donnée ; raison et prix dits ; la garde s'éprouve sur la liste gelée. Alignés : § 1 (ligne de c.8), § 3.1 (invariant et essai), § 7 (point 5), § 13 (réserve 13, la valeur n'est pas tirée du code ; le palier 0a l'établit) |
| constat 2 : ligne « coût » du § 3.0 | **oui** | « hors le test de mort de la génération finale, payé à part (§ 2, règle 4 ; § 6) » |
| constat 3 : deux renvois | **oui** | § 17, constat 4 : le renvoi au § 0 du devis est retiré. En-têtes du plan et du devis : la ligne 67 est dite lue sur `main`, le fichier qu'elle cite sur la branche, commit `7e140479` ; je le confirme sur `main` (la ligne 67 écrit elle-même « branche lot/compte-organisme-v1, 7e140479 ») |
| constat 4 : activation du branchement, nœud | **oui** | § 8.1, condition 2 (tenue par le mot de Lazar, non par la livraison du code) ; § 12, question 1 (répondre oui ne l'active pas ; le palier 1 ne part pas sans ce mot) ; en-tête ; devis § 4 (passage 0b → 1) et § 9 (nœud 1, activation palier par palier). Une ligne du § 8.4 ne le reprend pas : constat neuf 4 |
| paliers | **oui** | plan § 8.4 (neuf) et devis § 3 : 0a, 0b, 1, 2a, 2b, 3, 4, puis 5 (témoins jugés, sur demande) et 6 (diagnostic) ; pour chacun, ce qu'il permet de conclure et ce qu'il ne permet pas. Le § 8.4 ne change ni le dessin, ni un critère, ni un seuil : vérifié contre les § 7, 8.0 et 8.3 |
| règle de passage écrite d'avance | **oui**, avec trois précisions | plan § 8.4 et devis § 4 : une règle par passage, chiffrée, qui fait proposer le suivant sans rien dépenser ; aucune n'arrête pour le coût ; aucune ne lit un verdict de juge ; la règle 3 → 4 ne vise aucun signe (règle R3). Précisions : constats neufs 2, 3 et 4 |
| variantes à deux, trois et cinq espèces | **oui** | devis § 6 : chiffrage par palier, cumuls, haut et pire, paliers 5 et 6 ; ce que chaque variante fait perdre ; la voie « en escalier » et son seuil (0,25 USD par tentative), qui ordonne et ne retire rien. N-058 tenu : la composition se juge sur l'oracle et le coût, accord de Lazar requis |
| test de mort par tentative | **oui** | devis § 5 : aucune mesure réelle, dit et argumenté ; chiffré sur les cinq bornes écrites, vérifiées dans le code (ci-dessus) ; « des plafonds et un prix prudent, pas des mesures » ; le palier 1 le mesure, plafond d'arrêt proposé 290 USD ; machine d'exécution hors chiffre, bornée à 3 290 heures (32 900 × 3 × 120 s, exact) |
| recommandations par nœud | **oui** | devis § 9 : pour chacun des cinq nœuds, recommandation, confiance (0,7 ; 0,55 ; 0,75 ; 0,6 ; 0,65) et ce qui la ferait changer ; aucun n'est tranché, aucun n'a de défaut. Le changement de recommandation sur les juges à modèle (non joués à l'étage, palier 5 sur demande) est dit au plan (§ 12, question 3) et au devis (§ 9, § 10, § 11) ; il va dans le sens du mot de Lazar et de N-058 |
| calcul | **rejoué, exact** | voir ci-dessous |

### Le calcul

- Rejeu : deux sorties identiques à l'octet, `f503c224…`, égale à la sortie versée.
- **Continuité avec la v2** : les cumuls de propositions de la v4 sont ceux de la sortie v2 plus le palier 1, au centime : estimation 20 466,97 + 58,64 = 20 525,61 ; haut 35 186,76 + 73,31 = 35 260,07 ; pire 56 298,82 + 117,29 = 56 416,11 ; le palier 5 (3 713,91) est l'écart v2 entre l'étage avec et sans aiguilleur et juges (19 430,67 − 15 716,75). Les constantes de coût sont donc les mêmes.
- **Chaque chiffre du devis v4 a été confronté à la sortie** : § 0 (points 2 à 4), § 2, § 3 (deux tables), § 5 (table à cinq valeurs pour A, à trois pour B et C, totaux 32 900 tentatives ; rapports « un dixième » et « une fois et demie », « deux à quatre fois »), § 6 (variantes, 43 et 78 sources à dépense égale, 40 % des appels et 72 % du coût, voie en escalier à 3 110 USD et de 3 900 à 11 000 USD, seuil de 0,25 USD donnant 8 225 USD et plus de 28 000 USD), § 7 (350 et 481 générations de bras ; une source de plus ; six, dix, douze et seize sources), § 8 (leviers : 5 280, 1 760, 1 580, 3 710 USD ; divisions par 3,6 et 6,6), § 9 et § 10. **Tous exacts aux arrondis dits.** Le levier « course source d'une génération, 40 générations de bras de moins » est repris de la v3 sans changement.
- Aucun nom de rôle ni d'espèce, aucun identifiant de modèle dans le programme ni dans sa sortie ; les espèces y sont numérotées comme au devis.

## Le reste du différentiel

- **Plan** : hors des quatre constats et du § 8.4, les morceaux changés sont l'en-tête (version, pièces lues, puce neuve sur la ligne `GO-2026-11-19-69`), le § 0 (renvois), le § 12 (questions 3, 4, 6, 7 et 9 : renvois au devis v4 et au § 8.4, recommandation sur les juges retirée), le § 13 (réserves 10, 12 et 13), le § 14 (alinéa v4), les § 19 et § 20. Aucune hypothèse, aucune revendication, aucun seuil, aucun chiffre du § 3.3 ne change ; les § 3.3, 4, 5, 9 et 10 sont inchangés. Un renvoi de la règle 6 du § 2 (au § 2 bis du devis v3) change aussi, que le § 20 ne nomme pas : constat neuf 5.
- **Devis** : réorganisé par paliers ; aucun chiffre de la v3 n'est changé (vérifié par la continuité du calcul ci-dessus) ; la recommandation passe de « (a), aiguilleur et juges joués, confiance 0,6 » à « paliers dans l'ordre, sans aiguilleur ni juges, confiance 0,55 » : dit au § 11.
- **Listes « Ne pas écrire »** : mon programme rend sur la v4 douze occurrences, toutes relues et bénignes : onze des douze de la v3 (sujets désignés au § 14 du plan, « aucune priorité » du § 10, « bras de diagnostic seulement », montant 72,50, qui ne paraît plus que deux fois) et une neuve (« le palier précédent », devis § 4). Aucune formule interdite ; aucun identifiant ni nom de famille de modèles dans les quatre fichiers.
- **Mot de Lazar et N-058** : tenus. Les règles de passage ne lisent que des épreuves exécutées, l'oracle du monde planté et des coûts mesurés ; aucun critère, aucune règle, aucune variante ne dépend du verdict d'un juge ; le volet des témoins jugés est un palier d'information, sur demande.
- **Rien d'autre ne demande une contre-lecture complète.**

## Constats neufs

Gravité : **M** = moyen ; **m** = mineur. Aucun ne demande une version 5 : le premier se règle à la présentation à Lazar, les autres aux préenregistrements nommés.

### 1. (M, pour la mère) La ligne `GO-2026-11-19-71` est postérieure à la v4 et recouvre en partie la fiche du devis

Sur `main`, la ligne `GO-2026-11-19-71` (Lazar, « Ma recommandation : (b) go », vers 14:12Z) retient pour l'héritage « **option (b), l'étage sur processeur seul pour l'instant**, à 0 USD d'appels », la suite se décidant à sa lecture, avec le préalable « la question 1 du plan doit être tranchée avant le préenregistrement de cet étage ». Cette option (b) est celle du **devis v3** (§ 9). La v4, versée à 14:11:51Z sur `main` lu à `416a3342…`, ne la connaît pas ; ce n'est pas une faute du rédacteur. Mais :

- la lettre (b) **désigne une autre option dans le devis v4** : « les paliers 0a, 0b et 1 », qui comprend le palier 1, de l'ordre de 115 USD, plafond 290. Le palier 1 **n'est pas couvert** par la ligne 71 ;
- la fiche du § 9 du devis v4 (options et recommandation (a)) est donc dépassée pour son premier temps : ce qui reste à décider après la ligne 71, c'est l'ordre des paliers au-delà de 0b et le palier 1.

**Correction** (à la présentation, sans version neuve) : présenter le devis v4 en disant que la ligne 71 couvre les paliers 0a et 0b (0 USD) ; que le palier 1 demande son préenregistrement court, son devis, sa ligne d'accord et le mot d'activation du branchement ; citer toute option avec sa version (« option (b) du devis v3 ») ; et faire suivre le palier 0a du mot de Lazar sur le nœud 1 avant le préenregistrement du palier 0b (préalable de la ligne 71, compatible avec la recommandation du devis, « oui, sous réserve du palier 0a »). Le fait est à inscrire au § 13 d'une version suivante s'il en vient une.

### 2. (m) Le pilote en deux temps : niveau de la borne, et « nombre lu »

- La règle 2a → 2b s'arrête à six paires si le nombre de sources y vaut déjà le plancher de dix. La procédure rend alors la borne à six paires, sinon celle à neuf : sa couverture n'est plus exactement celle d'une borne à 95 % fixée d'avance (au pire, par réunion, le risque se double). Le § 8.4 dit « la borne haute reste calculée sur toutes les paires jouées », ce qui ne règle pas ce point. **Correction** au préenregistrement du pilote : dire la couverture de la procédure en deux temps, ou partager le risque entre les deux regards, ou retirer l'exception (i).
- « Le nombre de sources lu à la borne haute à six paires » : dire s'il s'agit du nombre lu dans la table ou du nombre retenu après la majoration du § 8.0 (part de différences nulles) ; seul le second décide.
- Devis § 8, levier « pilote arrêté à six paires » : « la règle du § 4 ne l'arrête que si cela ne change rien » est inexact ; une troisième source ne peut pas abaisser le nombre sous dix, mais elle peut le relever si l'estimation monte. Écrire « que si une troisième source ne peut plus l'abaisser ».

### 3. (m) Paliers 3 et 4 : les conditions de lecture se recalculent au palier 4

Au palier 3, seules les sources à dose nulle et les bras 2 et 3 sont joués. Trois des quatre conditions de l'étape 1 du § 8.3 (troncature entre bras, chaîne d'empreintes, générateur) portent aussi sur les sources à dose non nulle et sur le bras 1, qui n'existent qu'au palier 4. Le § 8.4 ne dit pas qu'elles sont recalculées au palier 4 sur toutes les sources et les trois bras, ni qu'une lecture peut encore y devenir « invalide ». **Correction** au préenregistrement de l'étage : le palier 3 clôt la seule règle de validité ; les trois autres conditions se lisent à nouveau au palier 4, sur l'ensemble, avant la table de l'étape 2.

### 4. (m) Palier 1 : ce qui n'est pas réemployé, et une ligne à aligner

- Le préenregistrement court du palier 1 doit dire que son monde planté, ses tentatives et le registre qu'il produit ne sont réemployés par aucun palier suivant (ni source, ni pilote, ni monde final ; graines distinctes, règle R9), comme le pilote le dit pour ses sources.
- Plan § 8.4, ligne 0b, règle de passage : « issue lisible : palier 1 » ne reprend pas le mot d'activation du branchement, que portent le § 12 (question 1) et le devis § 4. Ajouter « et le branchement activé par le mot de Lazar ».

### 5. (m, forme) § 20 du plan

Le § 20 nomme deux renvois au devis suivant la numérotation v4 (§ 3.0 et § 6) ; il y en a un troisième, à la règle 6 du § 2 (« au § 2 bis du devis v3, que le devis v4 cite sans le recopier »). Sans effet sur le fond.

## Verdict

Scellable.

Les quatre constats de la vérification de la version 3 sont appliqués fidèlement, sans dégât. Les demandes de la mère sont toutes portées : paliers du moins cher au plus cher, chacun avec ce qu'il permet et ne permet pas de conclure ; une règle de passage chiffrée et écrite d'avance par passage, qui ne lit ni un juge ni un coût pour arrêter ; variantes à deux, trois et cinq espèces avec ce que chacune fait perdre ; test de mort par tentative chiffré sur des bornes écrites que j'ai retrouvées dans le code, et mesuré au palier 1 ; recommandation et confiance par nœud, aucun tranché. Le calcul neuf, rejoué deux fois, rend la sortie versée à l'octet ; tous les chiffres du devis lui sont fidèles, et il prolonge la v2 au centime. Les listes « Ne pas écrire », le mot de Lazar et N-058 sont tenus. Rien d'autre n'a changé qui demande une contre-lecture complète. **Pour la mère** : la ligne `GO-2026-11-19-71`, postérieure à la v4, retient l'option (b) du devis v3 (étage sur processeur seul) ; la lettre (b) désigne autre chose dans le devis v4, et le palier 1 n'est pas couvert (constat 1) : à dire en présentant le devis. Les constats 2 à 5 sont mineurs, à reprendre aux préenregistrements du pilote, de l'étage et du palier 1. Les cinq nœuds restent à Lazar.
