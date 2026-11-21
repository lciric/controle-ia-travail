# Rapport de l'auteur — script de démarrage de l'essai 3 (palier 0b) — v2

Pièce de travail (classe C), écrite le 2026-11-21 vers 21:25Z par l'auteur de la v1 (modèle O), à la demande de la mère. La v2 porte les six points de la contre-lecture S récupérée :
- relevé `…/contre-lecture-script-demarrage-v1-recuperee/releve-contre-lecture-script-demarrage-interrompue-v1.md`, `f3e55b18…cfc3b` ;
- verdict provisoire « À corriger ».

Elle porte aussi les décisions de la mère sur les points ouverts. La v1 reste intacte dans le dossier parent.

Ce que je n'ai pas fait :
- aucune machine créée, aucun appel à Hetzner ni à GitHub ;
- aucun jeton réel lu ; aucun environnement du conteneur affiché ni listé ;
- aucune dépense, aucun commit, aucune poussée ;
- aucun arrêt de processus hors de mes serveurs factices, chacun par son identifiant (`pgrep` vide à la fin) ;
- aucune coupure ni aucun refus.

## Fichiers et empreintes (dossier `v2/`, compagnon `.sha256` à côté de chacun)

| Pièce | sha256 |
|---|---|
| `demarrage-machine-essai-3-v2.sh` (ASCII seul, 10 567 octets) | `63ea8498b2b0e93ba6cf86e72e3c3ccf855e88a58edce94f6fc179cab0ac395d` |
| `fabriquer-donnees-demarrage-v2.sh` | `8096d3cfe436ff66458cad3a2907d4b4c64fc3e5897af23a5c9d214602d294dc` |
| banc `v2/essais/outils/*` | compagnons à côté de chaque fichier |
| résultats `v2/essais/travail/cas/*/resume.txt`, `…/fabricant-essais/table.txt`, `…/s1-sain/journaux/{garde-branche*,controle-argv,assistant}.txt`, `…/q5-assistant-hote-de-production/journaux/assistant.txt` | compagnons à côté de chaque fichier |

Les quatre pièces de la tenue ne changent pas et restent dans les données de démarrage, comme la mère l'a décidé. La charge ne change pas non plus : `ea613795…b753`.

## Marge de taille

Données saines, script v2 et jeton factice de 44 signes : 31 902 octets bruts.

Lecture retenue : **longueur de la chaîne JSON du champ `user_data`, échappée en ASCII, guillemets compris, avec le jeton le plus long admis (100 signes)**. Elle donne **32 479 octets, soit une marge de 289 octets** sous 32 768.

Le calcul du fabricant (bash) et un calcul indépendant (`tailles-json.py`, `json.dumps`) donnent le même nombre.

Pour l'obtenir :
- j'ai retiré les 68 signes non ASCII, et le fabricant refuse désormais tout signe non ASCII ou de contrôle ;
- j'ai réduit les commentaires et les messages ;
- j'ai abaissé le jeton admis à 100 signes au plus (jeton GitHub à grain fin : 93 signes ; écart 1 ci-dessous).

Autres lectures, pour information (`tailles-json.py`, jeton de 100 signes) :

| Lecture | Taille | Marge |
|---|---|---|
| octets bruts | 32 140 | 628 |
| chaîne JSON en UTF-8 | 32 479 | 289 |
| chaîne JSON avec l'échappement HTML de Go (`< > &` en `<`…, celui de `encoding/json` par défaut) | 33 074 | **−306** |
| la même, avec `/` échappé | 33 552 | −784 |

Le fabricant écrit la ligne « Go » dans ses empreintes. Bâtir le corps de la requête avec un encodeur JSON de Go qui échappe le HTML (outil en ligne de commande `hcloud`, par exemple) dépasserait donc la lecture stricte. Il faut un encodeur qui n'échappe pas le HTML, par exemple `json.dumps` de Python envoyé par `curl`. C'est à trancher (ci-dessous).

## Les six points

1. **`.git` refait juste avant le pas (f)**, code 55, en plus du pas (c) (code 51). Cas `cl-q3-git-apres-c` (faux pip, `git init` dans la racine et un intrus non suivi après le pas (c)) : 55, aucun départ. En v1 : 0.
2. **Portes d'essai refusées en production.** Une variable `ESSAI_DEMARRAGE_*` présente sans `ESSAI_DEMARRAGE_BANC=oui` donne un refus en code 19, avant toute action (rien n'est créé). Le fabricant refuse un script qui affecte une porte d'essai (`ESSAI_DEMARRAGE_…=`), code 5. Ses propres réglages d'essai (`FABRICANT_SCRIPT`, `FABRICANT_DEPOT_DISTANT`) ne valent qu'avec `FABRICANT_BANC=oui` (sinon code 2), et les empreintes disent alors « DONNÉES D'ESSAI ».
3. **Âge de `H0_PREVU`.** Refus en code 21 si `H0_PREVU` est plus vieux que 7 200 s, ou plus de 600 s dans l'avenir, au démarrage. Justification :
   - le fabricant est joué « juste avant la création », et la création, le premier démarrage et l'arrivée de cloud-init au script prennent quelques minutes ;
   - 2 h couvrent un retard de création, ou une file d'attente chez Hetzner, avec une large marge ;
   - au-delà, les données sont vieilles, ou reprises par erreur, et l'arrêt de durée (`H0_PREVU` + 94 h) couperait plus de 2 h du budget de 94 h ;
   - le cas du contre-lecteur (`H0_PREVU` périmé, programme arrêté moins d'une seconde après son départ) est ainsi refusé avant tout ;
   - les 600 s d'avance tolèrent un petit écart d'horloge.

   Mesuré : 3 h → 21 ; 1 h → passe le pas 0 ; +1 h → 21 ; et 218 à 1 558 s dans les cas sains joués.
4. **Crochet avant poussée.** En plus de la v1 (seule la branche permise, jamais d'effacement), il refuse toute mise à jour non descendante : `git merge-base --is-ancestor <distant> <local>`, faux ou impossible → refus. Le script n'emploie jamais `--no-verify` (0 occurrence), et le fabricant refuse un script qui le porte (code 5).

   Limite inchangée : un processus en superutilisateur qui lit le jeton peut pousser autrement (écart déclaré) ; la protection de branche côté GitHub n'est pas vérifiée.
5. **Assistant restreint à l'hôte du dépôt.** Le protocole et l'hôte sont tirés de `DEPOT_URL` : `https` et `github.com` en production. Seule la demande `get` reçoit le jeton : rien pour `store` et `erase`, ni pour un autre hôte, un hôte voisin (`github.com.evil.example`), un autre protocole ou un hôte absent.
6. **Seuil du fabricant calé sur la lecture stricte** (ci-dessus). Code 6 au-delà de 32 768, ou à tout signe non ASCII ou de contrôle.

## Décisions de la mère, portées

- **Pièces dans les données de démarrage** : gardées.
- **Code 5 du départ.** Le départ écrit son code dans `code-depart-essai-3.txt`, qui est versé dans l'état. Après tout départ (0 ou 5), le script attend au plus 300 s que le lanceur écrive son code ou la ligne « départ du programme ». Si le code est non nul, il s'arrête net en code 85 et verse l'échec. Code 5 avec programme vivant : la suite continue, avec une ligne « ATTENTION » au journal et « code du depart : 5 » dans l'état.

  La même règle couvre `cl-q5` : lanceur qui refuse au vrai départ (code 10) alors que le départ rend 0 → 85, où la v1 rendait 0.
- **Versement en plus** :
  - `journal-essai-3.txt` et `sortie-gardien-essai-3.txt`, **plafonnés à 1 048 576 octets chacun (1 Mio, la fin du fichier, par `tail -c`)** ;
  - `arret-gardien.txt`, en entier.

  Mesuré : journal de 2 501 559 octets → 1 048 576 versés ; `arret-gardien.txt` de 747 octets versé à l'identique.
- **Branche neuve et réservée à la machine.** Le fabricant refuse si la branche existe déjà sur le dépôt distant (code 8), et aussi si la vérification est impossible (code 8). La vérification se fait par la session, en lecture, sans jeton déposé.

  La commande, écrite dans les empreintes, est `GIT_TERMINAL_PROMPT=0 git ls-remote --exit-code --heads https://github.com/lciric/controle-ia-travail.git refs/heads/recuperation/palier-0b-programme-1-essai-3-v1`. Le code 2 signifie que la branche est absente.

  **Elle n'a été jouée que sur mes dépôts factices** (`FABRICANT_BANC=oui`, `FABRICANT_DEPOT_DISTANT`).

## Table des essais (banc rejoué en entier, factices locaux)

| Cas | Point | Attendu | Rendu | Jeton : fichiers / histoire / `ps` | Tenu |
|---|---|---|---|---|---|
| s1-sain | tous | 0 ; argv égal ; 4 commits avec `journal-essai-3.txt` et `sortie-gardien-essai-3.txt` | 0 ; `controle-argv.txt` ÉGAL ; 4 commits, 10 fichiers ; état « code du depart : 0 » | 0 / 0 / 0 (2 978 relevés) | oui |
| s1, garde de branche, 3e passe | 4 | 7 refus (main, autre, voisin, effacement, étiquette, forcée réécrite, forcée orpheline), distant inchangé ; descendante admise | idem ; message de la garde à chaque refus | — | oui |
| s1, assistant (http://127.0.0.1:PORT) | 5 | jeton à l'hôte permis seul | 1 réponse ; 0 pour les 6 autres demandes | assistant : 0 ligne en clair | oui |
| q5, assistant de production (https://github.com), cas arrêté au pas (a), sans réseau | 5 | jeton à `github.com` seul | 1 réponse ; 0 pour les 6 autres | — | oui |
| q2, portes sans banc | 2 | 19, rien créé | 19, base absente | 0 / — / 0 | oui |
| q3, `H0_PREVU` vieux de 3 h | 3 | 21 | 21 (« vieux de 11060 s ») | 0 | oui |
| q3, `H0_PREVU` vieux de 1 h (sain) | 3 | passe le pas 0 | passe, puis 30 au faux apt voulu | 0 | oui |
| q3, `H0_PREVU` dans 1 h | 3 | 21 | 21 (−3 339 s) | 0 | oui |
| cl-q3-git-apres-c | 1 | 55, aucun départ | 55, faux programme jamais lancé | 0 / 0 / 0 | oui |
| cl-q5, lanceur qui refuse au vrai départ | code 5 / départ | 85, journal de l'essai versé | 85 (« code 10 ») ; `journal-essai-3.txt` versé | 0 / 0 / 0 | oui |
| m5, code 5 et programme vivant (faux `setsid`) | code 5 | 0, ATTENTION, état « code du depart : 5 » | idem ; 5 commits | 0 / 0 / 0 | oui |
| m5, code 5 et programme mort (code 9) | code 5 | 85 | 85 (« code 9 ») | 0 / 0 / 0 | oui |
| v1, arrêt de place forcé et 2,5 Mo de sortie | versement | `arret-gardien.txt` versé ; journal plafonné | 747 octets versés ; 1 048 576 sur 2 501 559 ; code de sortie 143 | 0 / 0 / 0 | oui |
| b1, jeton refusé par le serveur | — | 41 | 41 ; versement d'échec refusé (même jeton) | 0 | oui |
| b2, commit absent | — | 41, journal poussé | 41, poussé | 0 | oui |
| z1, jeton vide / z2, `@JETON@` | — | 22 | 22 / 22 | 0 | oui |
| z3, `H0_PREVU` mal formé | — | 21 | 21 | 0 | oui |
| z4, second démarrage | — | 20 | 20 | 0 | oui |
| c1, commit avec `.git` | — | refus | 50 (`git archive` refuse) | 0 | refus sûr |
| c2, `.git` laissé par l'extraction | — | 51 | 51 | 0 | oui |
| c3, commit autre | — | 53 | 53 | 0 | oui |
| d1, pip en échec | — | 61 | 61 | 0 | oui |
| e1, pièce altérée / e2, pièce en trop | — | 72 / 71 | 72 / 71 | 0 | oui |
| f1, racine altérée après (c) | — | 81 | 81 | 0 | oui |
| f2, paramètres du gardien refusés | — | 82 | 82 | 0 | oui |
| t1, témoin de fuite (objet vrai) | banc | 3 canaux trouvés | journal, URL, `ps` 44/45 | 2 / — / 44 | oui |

**Fabricant v2** (`table.txt`) : **21 cas, 21 tenus**.

| Cas | Code |
|---|---|
| F01 variable vide ; F02 variable absente | 3 |
| F03 jeton à espaces ; F04 jeton court ; F04b jeton de 101 signes | 3 |
| F05 sortie existante ; F06 sortie relative ; F07 sortie dans un dépôt | 4 |
| F08 empreinte du script fausse ; F09 ligne 2 autre | 5 |
| F10 trop grand en lecture stricte (32 863 octets) | 6 |
| F13 porte d'essai dans le script ; F14 `--no-verify` dans le script | 5 |
| F15 signe non ASCII | 6 |
| F16 branche déjà présente sur le dépôt factice | 8 |
| F17 dépôt injoignable | 8 |
| F18 réglage d'essai sans banc | 2 |
| F11, F12 sains ; F20 sain avec un jeton de 100 signes | 0 |

Pour les sorties saines :
- droits 600 ;
- le jeton est sur la seule ligne 3 ;
- le texte sans jeton est égal aux données, jeton masqué ;
- aucun autre fichier ne porte le jeton, et aucune sortie n'est laissée après un refus ;
- `ps` : 0 ligne.

**Dénominateur et passes ratées.** La garde de branche a été jouée trois fois sur s1. Les deux premières passes sont gardées sous leurs noms.
- **Passe 1** : je relançais le serveur sur un port neuf. Toutes les poussées sont tombées en code 128 faute de jeton, parce que l'assistant restreint à l'hôte d'origine (le point 5 en acte) n'a rien rendu. La garde n'était jamais atteinte.
- **Passe 2** : le dépôt local était en avance d'un commit. L'« histoire réécrite » descendait donc encore de la tête distante, et elle a été admise à bon droit. L'essai était mal construit, et cette passe a aussi modifié le distant factice du cas.
- **Passe 3**, sur le même dépôt : le dépôt local est d'abord remis sur la tête distante, et le commit orphelin est fabriqué par `commit-tree`. Les 7 refus et l'admission tiennent.

Non joués :
- les codes 60, 83 et 84 ;
- une charge à pièce manquante ;
- l'intervalle de 1 800 s ;
- le chemin de production par défaut (`/srv`, le vrai apt, GitHub) : il ferait des actions réseau interdites ;
- cloud-init.

## Écarts

1. **Jeton admis : 20 à 100 signes** (400 en v1), pour tenir dans la lecture stricte. Un jeton GitHub à grain fin fait 93 signes, un jeton classique 40.
2. **Messages et commentaires du script sans accents** (ASCII seul). Le journal de démarrage est donc en français sans accents.
3. **`exec >> journal`** : toute la sortie du script et de la boucle va au journal de démarrage, et plus rien au journal de cloud-init, sauf le refus 19.
4. **Attente d'au plus 300 s après le départ** (code du lanceur ou ligne « départ du programme »). Le gardien part donc un peu plus tard qu'en v1. Si la ligne et le code manquent après 300 s, la suite continue.
5. **Retirés pour la place** :
   - le relevé `pip freeze` et les versions de git et de Python au journal ;
   - la taille de `journal-essai-3.txt` dans l'état ;
   - le nettoyage de l'environnement du programme, que j'avais d'abord écrit sur la trouvaille de côté du contre-lecteur.

   Le programme hérite donc toujours de `DEBIAN_FRONTEND`, `GIT_CONFIG_GLOBAL`, `GIT_CONFIG_NOSYSTEM` et `GIT_TERMINAL_PROMPT` (réserve).
6. **Le fabricant lit `BRANCHE` et `DEPOT_URL` dans le script**, pour que la vérification de la branche porte sur ce que la machine poussera.
7. **Banc.**
   - Nouveaux outils : faux `setsid` (modes enfant, mort, sorties), faux pip qui pose un `.git`, sortie volumineuse du faux programme, essais de l'assistant, mesure JSON indépendante.
   - Le joueur de cas retire désormais la racine et le clone de chaque cas après les recherches.
   - Le dépôt factice partagé de la v1 sert encore.

## Ce qui reste à trancher avant la création

1. **Encodeur de la requête de création.** La marge est de +289 en JSON ASCII et de −306 avec l'échappement HTML de Go. Je recommande un corps fabriqué par `json.dumps` (Python), sans échappement HTML, puis envoyé par `curl`. Il ne faut pas passer par `hcloud`, ou alors seulement après une vérification de la façon dont Hetzner compte les 32 Kio, ce qui reste le premier pas non justifié.
2. **Quel jeton** (inchangé) : un jeton à grain fin, sur le seul dépôt, « contenu » en lecture et écriture, à durée courte, révoqué après la destruction ; au plus 100 signes.
3. **La vérification de la branche** se joue dans la session, au moment de la fabrication, sur le vrai dépôt (`FABRICANT_BANC` non posé).
4. **Contre-lecture S de la v2**, puis le fabricant joué avec l'empreinte contre-lue du script (`63ea8498…`) en troisième paramètre.
5. **La voie qui fait foi** pour la création, la lecture de H0 et la destruction (inchangé depuis la v1).
6. **Environnement hérité par le programme** (écart 5) : l'accepter, ou rendre de la place pour le nettoyer.

## Relevé de méthode

**Chaîne de raisonnement.**
1. Six points et quatre décisions : relevé `f3e55b18…` et message de la mère.
2. La taille de la v2 complète, avant allègement, était de −1 369 octets en JSON ASCII (mesure `tailles-json.py` sur `mesure-b`). Après allègement : +289 (mesures `mesure-d`, `ud-sain.empreintes.txt`). Le fabricant (bash) et Python sont égaux à l'octet (32 479 et 33 074).
3. Chaque point a un artefact et un cas sain (table) ; le cas `cl-q3` du contre-lecteur rend 55.
4. Le jeton reste hors des fichiers, de l'histoire et de `ps` dans tous les cas, et le témoin t1 rend les trois canaux.
5. Hetzner compte les 32 Kio au plus comme une chaîne JSON échappée en ASCII : **supposé**. C'est la lecture que la mère demande.
6. Sur la machine réelle, cloud-init, apt, pip et GitHub se conduisent comme les factices : **supposé**.

**Objets de contrôle.**
- **Assistant.** Faux : 6 demandes (hôte étranger, hôte voisin, autre protocole, hôte absent, `store`, `erase`), prédit rien, rendu rien. Vrai : l'hôte permis, prédit et rendu le jeton.
- **Garde.** Faux : 7 poussées interdites, refusées. Vrai : une poussée descendante, admise. Deux passes mal construites sont rapportées, et non effacées.
- **Âge de `H0_PREVU`.** Faux : 3 h et +1 h, refus. Vrai : 1 h et 4 à 26 min, admis.
- **Taille.** Faux : script gonflé (F10) et signe non ASCII (F15), refus. Vrai : F11, F12, F20.
- **Branche.** Faux : branche présente sur un dépôt factice (F16), refus. Vrai : branche absente, 0.
- **Recherche du jeton.** Témoin t1 (vrai par construction) : trouvé.

**Premier pas non justifié.** Pas 5 : la façon dont Hetzner compte la limite. La documentation d'API ou une création d'essai, qui coûterait, le justifierait.

**Mode d'échec affecté.** Sans objet : je suis auteur.

**Dérivation de l'énoncé seul.** Sans objet : je ne suis pas agent de re-dérivation.

**Trouvaille de côté.** L'assistant restreint à l'hôte a cassé mon propre essai de garde en passe 1. Il faut donc que l'URL du dépôt, et elle seule, porte l'hôte exact, port compris : sur la machine c'est `github.com` sans port, ce qui est conforme.

**Évaluateur et conseil.**
- **Qui juge.** Mon banc juge le produit, puis le lecteur S. Le banc a été admis sur le témoin t1 et sur les objets faux ci-dessus.
- **Bon jugement sans le mériter.** C'est possible :
  - factices et non vraie machine ;
  - HTTP et non HTTPS ;
  - pas de cloud-init ;
  - artefacts choisis par moi ;
  - attente de 300 s jouée seulement en quelques secondes.
- **Conseil au lecteur.** Viser :
  - l'attente après le départ, et ses fenêtres ;
  - la marge de 289 octets, et l'encodeur de la requête ;
  - le crochet face à un distant que la machine n'a pas vu.
