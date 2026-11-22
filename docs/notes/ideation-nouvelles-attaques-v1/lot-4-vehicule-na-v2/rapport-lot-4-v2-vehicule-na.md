# Rapport du développeur — véhicule NA-1, lot 4 v2 (appel gardé v2, adaptateur Claude direct, règle de repli)

- Développeur du lot 4 v2, modèle O. Je n'ai écrit ni les nœuds, ni le projet d'additif, ni les lots 1 à 3, 5 et 6. J'ai écrit seul ce qui suit.
- Date (UTC) : 2026-11-22.
- Processeur seul. **Aucun appel de modèle, aucune requête vers un fournisseur, aucune clé, aucune dépense**, aucun relais lancé, aucune écriture dans un dépôt, aucun commit. Les seules requêtes réseau vont à un faux serveur sur `127.0.0.1`, ouvert par les essais.
- **Aucun refus d'outil ni de classifieur.**
- **Un incident à dire** : au début, une commande d'affichage du code de la v1 (`appel_garde_na_v1.py`, en entier) a produit une sortie trop longue. L'outil d'agent l'a rangée d'office sous `/root/.claude/projects/…/tool-results/`. Je ne l'ai pas écrite moi-même et je ne l'ai pas lue. Elle ne contient que le code source de la v1. Ensuite, j'ai tout lu par tranches de moins de 150 lignes.
- Ce rapport ne porte ni chemin complet du bloc-notes ni identifiant de modèle. Les deux modèles de repli n'y sont nommés que par leur rôle, « premier » et « second ». Dans le code et les essais, ils ne sont jamais écrits : ils viennent de la configuration, et les essais emploient des noms neutres.

## 1. Verdict

- **Livré** :
  - `appel_garde_na_v2.py` (copie modifiée de la v1 `d16d07bf…`) ;
  - `adaptateur_claude_direct_na_v1.py` (type neuf ; il remplace `adaptateur_claude_na_v1.py`, `38baa206…`, pour les clés Claude) ;
  - leurs essais, leurs mutations, le programme d'application et le différentiel.
- **Essais** : 89 neufs, tous passés (59 pour la surcharge et le repli, 30 pour l'adaptateur). Avec les lots 3 v3 et 4 v1, sur une copie neuve du commit `a41b7b50`, où les lots 2 v5, 3 v3, 4 v1 puis 4 v2 sont posés par leurs programmes : **248 passés, 0 échec** (`journal-essais-na-lot-4-v2.txt`). Les essais du lot 2 v5 ne sont pas joués, parce qu'ils lisent la liste réelle des motifs.
- **Mutations : 61 sur 61 tuées.** Le témoin non muté passe, le témoin inerte survit (`journal-mutations-na-lot-4-v2.json`).
- **Le lot 4 v2 n'est pas branchable tel quel sur le lot 6 v3.** L'interface change : contexte, issues, juges servis par repli, adaptateur. Il faut un lot 6 v4 (§ 5).

## 2. Pièces lues

| pièce | empreinte |
|---|---|
| nœuds du véhicule v2 (NO) ; sa vérification | `79b9d423…` ; `e7eb1682…` |
| projet d'additif v2 (PA) ; sa vérification | `6e9bb88e…` ; `e4984e1a…` |
| conception du véhicule v5 (CO), par la seule voie des renvois | `1b7f6822…` |
| lot 4 v1 : rapport, vérification, `appel_garde_na_v1.py`, `adaptateur_claude_na_v1.py`, aides, essais, mutations | `1b16fabb…`, `3c8d1aa2…`, `d16d07bf…`, `38baa206…` |
| mandat du lot 4 v1 et errata 1 à 3 (empreintes recalculées, non relus en entier) | `df5a1cea…`, `47721c81…`, `1d6de645…`, `72fa461a…` |
| orchestrateur `a41b7b50` : `adaptateurs.py`, `relais.py`, `relais_reel_v2.py` (l. 60-143, 262-345), `noyau_v56.py` (`appel`, `juger`), `suivi_roles_v54.py`, `caviardage.py`, `journal_na_v3.py`, `routage_na_v1.py` | — |
| lot 6 v3, par recherche seulement : lieux d'usage du lot 4 dans `course_na_v3.py` et `configuration_course_na_v1.py` | — |
| kit de l'interface des messages installé dans l'environnement virtuel du dépôt | version 2.12.0 |

## 3. Exigences et code

Abréviations : **AG** = `pole/appel_garde_na_v2.py`, **AD** = `pole/adaptateur_claude_direct_na_v1.py`.

### Adaptateur direct (D-N1, D-N2)

| exigence | code | épreuve (cas sain ; artefact) |
|---|---|---|
| A-1, D2 : la requête assemblée part seule, dans un message « user », sans champ système ; liste fermée des clés du corps | AD:194 `construire_corps_na`, AD:203 `verifier_corps_na` | consigne seule, à l'octet, au faux client et **au corps reçu par le faux serveur** ; `system`, `fallbacks`, `betas`, `tools`, `metadata`, `temperature`, `stream`, un message changé ou ajouté : refusés |
| A1 : `max_retries=0` écrit, relu à la construction et avant chaque envoi | AD:287 `fabrique_client_reel`, AD:297 | client réel : 0 ; une 529 au faux serveur : **une** requête ; témoin, un client réel à `max_retries=2` : trois requêtes ; faux client à 2 : refusé ; client changé après la construction : refusé avant l'envoi |
| A2 : ni paramètre de repli ni en-tête bêta ; trace de repli dans la réponse → refus `messages.repli_fournisseur` | AD:236, AD:247 ; AG:82 | aucun en-tête `anthropic-beta` reçu par le faux serveur ; un bloc `fallback`, une itération `fallback_message` : n° 31 |
| A3 : coût par l'usage, au barème versé ; usage absent ou sans sa forme : coût inconnu, au plafond de la tentative ; au cumul de la clé, le pire de la tentative s'il est plus haut | AD:174 ; AG:510-524 | usage lu au barème ; usage absent, vide, négatif ou sans jetons d'entrée : inconnu, jamais zéro ; cumul relevé au pire quand le noyau compte moins |
| A4 : réponse brute conservée par tentative (refus, erreurs et exceptions compris) ; impossible : rien n'est rendu | AD:331, AD:371 | trois tentatives, trois fichiers et leurs compagnons ; **texte caviardable conservé brut** (réponse au point Z4-48 de la vérification v1) ; dossier retiré : `ConservationImpossible` |
| A5 : catégorie lue à `stop_details.category`, sinon « catégorie non lue » | AD:247 | catégorie présente, absente, vide, sans détail |
| A6 : liste fermée des raisons ; repli seulement sur `refusal` | AD:247 ; AG:79-80, AG:575-596 | `pause_turn`, `tool_use`, `stop_sequence`, absente, inconnue, `max_tokens` : aucune requête de plus |
| A7 : un jeu (plafond de sortie, effort, réflexion, flux) par rôle du kit et par modèle admis, contrôlé contre la table versée ; n° 32 (proposé) | AD:126 `lire_reglages_na` | effort non admis sur le second modèle de repli : refus qui dit « effort » ; plafond, réflexion, flux, champ en trop, jeu manquant : refusés |
| N2 : 402 `billing_error` → « crédit d'amont » ; 402 du relais à son plafond → « plafond du relais » ; 403 « modèle non permis » du relais → n° 31 ; toute autre erreur garde son statut | AD:267 ; AG:597-615 | n° 13 levé sur le crédit d'amont et sur le plafond du relais ; non levé sur une 403 d'accès ni sur un 402 d'un autre type ; mêmes classes vues par le client réel au faux serveur |
| modèles admis : liste fermée de la configuration (`verifier_modele_reel` du kit retiré du chemin) | AD:302 | modèle hors liste : refusé avant toute requête |

### Surcharge v2 et règle de repli (D-35, D-i à D-iii)

| ligne | code | épreuve (cas sain ; artefact) |
|---|---|---|
| P1 : la même requête assemblée est rejouée sur le premier, puis le second modèle de repli ; le n° 1 se lève au troisième refus (portée « appel », ou « course ») ; reformulation refusée | AG:420-469, AG:617 | premier et second repli servis ; trois refus → n° 1, avec les trois catégories ; portée « course » levée après trois requêtes, pas avant ; reformulation : « requête journalisée » |
| P2, P3 : refus en prose, crédit, accès, coupure, raison inconnue : jamais rejoués | AG:540-615 | une seule requête dans chaque cas |
| P4, P15 : n° 12 avec le pire de chaque tentative, pris par (rôle, modèle) | AG:236-280, AG:476-484 | part juste pour la première tentative, dépassée par la seconde : n° 12, une requête ; pire du premier repli plus haut que celui du rôle : n° 12 au repli |
| P5 : chaque tentative est une réservation neuve du noyau ; une coupure arrête la chaîne | AG:510-538 | reste épuisé par la première : « non lancé », une requête |
| P6 : une ligne « envoi » neuve par tentative (même empreinte, rang neuf), garde et égalité repassées | AG:485-509 | deux lignes, une empreinte ; écart d'égalité au second rang : renvoi au rang 2 ; journal en panne au second : arrêt |
| P7, P9 : fiche servie par repli attribuée au modèle servi (« servie par repli : modèle »), issue « refus par classifieur, servi par repli » | AG:565-572 | attribution et issue rendues ; la clé n'est jamais dans les lignes de tentative |
| P11, D-ii : le repli vaut aux lignes à part, au plafond de la ligne | AG (même chemin) | sonde de refus : servie par repli, marquée ; plafond de la ligne repassé par tentative |
| P12 : classe de la tentative servie rendue (`classe_tentative_servie`) ; une erreur en repli → « réponse illisible », sous-compte « en repli » | AG:565-572, AG:600-614 | réponse coupée en repli : « servie », classe « réponse illisible » ; 529 en repli : la chaîne s'arrête |
| P16, n° 31 : modèle servi absent ou différent du modèle demandé **de la tentative** ; le rôle garde son modèle ; modèle demandé autre que celui du rôle refusé avant l'envoi | AG:553-564, AG:443-446 | servi par le second au lieu du premier : n° 31 ; servi absent : n° 31 ; date stricte admise (R-764) ; changement au même modèle demandé : n° 31 |
| P17 : verdict du portier ou d'un juge servi par repli = verdict du rôle, modèle servi rendu (`r.modele_servi`, `par_repli`) | AG:565-572 | verdict lu et rendu |
| n° 34 (proposé) : un (rôle d'une clé Claude, modèle de repli) sans pire refuse la construction | AG:236-267 | pire manquant, rôle sans pires, pire nul : refus |
| D-N1 : chaque adaptateur d'une clé Claude est l'adaptateur direct, et admet les modèles de ses rôles et les deux de repli | AG:308-325 | adaptateur d'origine sur une clé Claude : refus ; liste sans le second modèle : refus |
| « replis », mesure descriptive (P10, point 3) | AG:398-418 (`na_replis`), AG:660 `comptes_replis_na` | comptes par (rôle, modèle demandé, modèle servi, catégorie, issue) |

L'arrêt n° 27 n'est ni lu ni levé ici. Les arrêts n° 11 et n° 12 gardent leur lettre : le pire est pris par tentative, sur la même clé, sans bascule.

## 4. Écarts et choix de code (à confirmer)

1. **Issues neuves** : « refus par classifieur, servi par repli » et « arrêt n° 1, consigné après trois refus ». L'issue de la v1 « arrêt n° 1, consigné, non relancé » reste pour les commandes externes et le protocole. Tout autre événement de refus devient « réponse illisible, cause non établie », au sous-compte « refus hors liste ». C'est A6, qui remplace la l. 74 de la v1.
2. **A2 de la v1 devient l'arrêt n° 31**, et la classe garde son nom (`ArretA2NA`). Les n° 31, 32 et 34 sont proposés (PA § 10) : la mère les confirme.
3. **`lire_etat_relais` est retiré du contexte**, avec la lecture de `/relais/etat`. L'erreur du relais (402 à son plafond, 403 pour un modèle) arrive maintenant telle quelle. Le message synthétique de l'outil n'existe plus.
4. **Coût d'une erreur** : une erreur rendue par un statut, avant tout octet de réponse, coûte zéro. Une erreur sans statut (connexion, délai), ou survenue après le début d'un flux, est au coût inconnu. Le code tranche ainsi, la lettre ne le fixe pas.
5. **Le flux est exigé au-delà de 16 000 jetons de sortie.** C'est un choix de code prudent. NO dit seulement que le flux est « obligatoire pour 128 000 ».
6. **Corps brut en flux** : les événements du kit, rendus en dictionnaires, plus le message final. Ce ne sont pas les octets du flux d'événements. Hors flux, c'est le texte de la réponse HTTP.
7. **Crédit d'amont = 402 et type `billing_error`, les deux à la fois.** Un épuisement de crédit signalé autrement (400 ou 429 de plafond de dépense, par exemple) est lu « cause non établie », et la course continue. La forme réelle n'est pas vérifiée sur une page versée.
8. **Le modèle servi admet le suffixe de date strict** (`modele_conforme`, R-764). P16 dit « le seul modèle demandé » : la mère dit si ce suffixe vaut le même modèle.
9. **L'en-tête du jeton factice.** Le kit 2.12 ne pose qu'`Authorization` (relevé au faux serveur), alors que le relais v2 ne lit que `x-api-key` (l. 268) : sans correction, tout appel recevrait un 401. L'adaptateur pose donc `x-api-key` à la valeur du jeton factice. Le relais retire `Authorization` (l. 77).
10. **Le kit envoie l'en-tête de version d'interface `2026-10-21`.** Les réglages admis de A7 sont à lire pour cette version.
11. **Pas 0 en chaîne** : un rôle arrêté entre deux tentatives rend un « refus écrit ». Ce cas est inaccessible avec la configuration du lot 6 (A3 et A14 désactivés, A11 vide), mais il est défini et éprouvé.

## 5. Ce qui touche les autres lots

**Lot 5 (v2)** :
- un verdict du portier servi par repli porte `par_repli` et `r.modele_servi` ;
- le passeport A17 doit être marqué « par repli » (P17) ;
- les comptes « servies par repli » restent à part.

**Lot 6 (v4)** :
- contexte : les champs `modeles_par_role`, `modeles_repli` et `pires_repli` sont neufs, `lire_etat_relais` est retiré ;
- adaptateur direct : il prend la configuration `modeles_admis`, `reglages` (A7), `admis` (table versée) et `bareme` (versé) ;
- `_classer_retour_proposeur` doit lire les deux issues neuves. Aujourd'hui, une issue inconnue lève `DefautLot6` ;
- la surcharge de `juger` lève A2 quand le modèle servi d'un juge change. Il faut sauter ce contrôle quand `a["par_repli"]` est vrai, et garder la clé (rôle, modèle demandé) ;
- table des arrêts : ajouter n° 31 et n° 34 ;
- champ « modèles de repli » à côté de `a11_modeles: []` ;
- chaque tentative est un appel pour le suivi des rôles et une consommation au coffre (`modele_demande` de la tentative) : M4 et A14 comptent des tentatives, non des chaînes ;
- sonde (P11) : `par_repli` vrai signifie « l'espèce n'est pas dite acceptante ».

**Lot 7** : la mesure « replis » se lit sur `na_replis` (`comptes_replis_na`). Il faut aussi la double lecture de M1 à M7 et M4 sans les tentatives de repli (P9, P10).

**Lot 8** :
- le relais v2 doit permettre les deux modèles de repli, sinon il rend un 403, lu en n° 31 ;
- son barème ne les porte pas : ils sont comptés à la borne haute `BAREME_INCONNU` ;
- épingler le paquet `anthropic` (2.12.0 relevé) dans l'environnement du lanceur ;
- ajouter les deux modules neufs à la table du code chargé (C-1).

**Lot 9** : les épreuves de la règle de repli en moteur simulé, à l'échelle d'une course (PA § 5, épreuves) :
- M3 et n° 5 avec les fiches de repli ;
- lecture « espèces seules » ;
- sonde ;
- juge servi par repli sans n° 31.

## 6. Ce qui reste ouvert

1. **Journal v4 (P6)** : le journal v3 est fermé, et sa ligne « envoi » ne porte pas le modèle demandé. Celui-ci vit dans `na_replis`, au coffre et dans la réponse brute.
2. **Garde Google (N4, G-1)** : elle n'est pas faite ici. Le mandat porte sur l'adaptateur Claude et le repli. NO § 4 la plaçait dans le même lot 4 v2, à `_apres_retour_na`.
3. **Valeurs de la configuration** : les valeurs admises de A7, le barème des deux modèles de repli et les six pires de l'aiguilleur et du juge par modèle (PA § 11) ne sont écrits nulle part ici ; les essais n'emploient que des valeurs d'essai. Je signale une indication tirée de la documentation embarquée de l'outil d'agent, **non opposable (R7)**, à vérifier sur la page versée : sur les deux modèles de repli, l'effort maximal intermédiaire (`xhigh`) ne serait pas admis, la réflexion se réglerait en « adaptive », et l'échantillonnage (`temperature`) serait refusé à la version `2026-10-21`.
4. **Relevé de l'adaptateur direct derrière le vrai relais** (PA § 11) : c'est le jeu de la mère. Il n'est pas fait.
5. **La voie du flux n'est éprouvée qu'au faux client**, pas au client réel avec un faux serveur d'événements.
6. **Les essais du client réel exigent le paquet `anthropic`.** Sans lui, ils sont sautés, et les mutations D-06 et D-07 ne seraient plus tuées.

## 7. Livré (dossier `vehicule-na-lot-4-v2/` du bloc-notes ; le chemin complet est dans le message de remise)

- `paquet/orchestrator/pole/` : `appel_garde_na_v2.py`, `adaptateur_claude_direct_na_v1.py` ;
- `paquet/orchestrator/essais/` : `aides_na_lot4_v2.py`, `test_na_v2_appel_garde.py`, `test_na_v1_adaptateur_claude_direct.py`, `mutations_na_lot4_v2.py` ;
- `appliquer_paquet_vehicule_na_lot_4_v2.py`, `ecrire_manifeste_paquet_na_lot4_v2.py`, `manifeste-paquet-vehicule-na-lot-4-v2.json` ;
- `journal-essais-na-lot-4-v2.txt`, `journal-mutations-na-lot-4-v2.json`, `differentiel-lot-4-v1-v2.diff` ;
- `table-empreintes-dossier-na-lot-4-v2.txt`, avec un compagnon `.sha256` par fichier de la table.

`copie-neuve/` (la copie de l'orchestrateur où les paquets sont posés) reste hors de la table : ce n'est pas un dépôt.

— développeur du lot 4 v2 du véhicule NA-1, modèle O
