# Rapport de l'auteur — script de démarrage de la machine de l'essai 3 (palier 0b) — v1

Pièce de travail (classe C), écrite par un auteur neuf (modèle O) le 2026-11-21, vers 20:05Z ; à contre-lire par un modèle S.
Mandat : `…/lancement-essai-court-mesure-v1/mandat-auteur-script-demarrage-serveur-essai-3-v1.md` (`dcd05a42…fce3d`, vérifié à l'ouverture).

**En bref.**
- Le script de démarrage et le fabricant sont écrits.
- Ils sont éprouvés de bout en bout sur des factices locaux, avec les vraies pièces de la tenue (lanceur v4, gardien v4 et leurs scripts de départ) et le vrai arbre du commit `d7f949ac`. Les valeurs d'emploi du lanceur n'ont reçu aucun remplacement.
- Cas sain : les pas (a) à (g) passent. Le faux programme reçoit la commande du complément, égale à l'octet aux trois chemins près. Le gardien tient son journal et écrit les deux inventaires. La boucle pousse 4 commits sur la seule branche de récupération, dont le fichier « fin ».
- Chaque artefact essayé est refusé avec son code et une ligne qui le nomme. Le journal est poussé quand le versement est prêt.
- Le jeton factice n'apparaît dans aucun fichier produit, dans aucune histoire versée, ni dans `ps`. Les recherches ont été vues rouges sur un témoin qui fuit exprès.
- **Écart principal : les quatre pièces voyagent dans les données de démarrage.** Elles n'existent ni dans le commit ni sur `origin/main`. Elles sont comprimées, et les données de démarrage font 32 112 octets, contre une limite de 32 Kio supposée.

Dossier : `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/auteur-script-demarrage-essai-3/`.
- Aucune machine n'a été créée.
- Aucun appel n'a été fait à Hetzner ni à GitHub.
- Aucune variable de jeton réel n'a été lue : seuls des jetons factices, fabriqués ici, ont servi.
- Rien n'a été dépensé, rien n'a été commité ni poussé.
- Le dépôt de travail a été lu seulement (`git show`, `log`, `branch --contains`, `cat-file`, `ls-tree`, `count-objects`, et un `fetch` qui lisait le dépôt pour remplir le dépôt factice).
- Rien n'a été écrit sous les chemins interdits.
- Processus arrêtés : mes deux serveurs factices seulement, chacun par son identifiant. Aucun processus factice ne reste vivant (`pgrep` vide).
- Aucune coupure ni aucun refus n'est survenu.

## Fichiers et empreintes (compagnon `.sha256` à côté de chacun)

| Pièce | sha256 |
|---|---|
| `demarrage-machine-essai-3-v1.sh` (script de démarrage, 10 777 octets) | `580d81c50bc83616375a83a49b69860dd10d71ae79c8fe5bf19f18f718aa1459` |
| `fabriquer-donnees-demarrage-v1.sh` (fabricant) | `a7d54bf0e95645a4592c8b237da6980690362a5afcfc19ebd782111ef9a3a098` |
| `essais/outils/*` (banc : serveur git factice, faux apt, faux python3, faux pip, faux programme, guetteur de `ps`, joueur de cas, garde de branche, contrôleur des arguments, artefacts, témoin de fuite, essais du fabricant) | compagnons à côté de chaque fichier |
| `essais/travail/cas/*/resume.txt`, `essais/travail/fabricant-essais/table.txt`, `essais/travail/cas/s2-sain/journaux/garde-branche.txt` et `controle-argv.txt` | résultats bruts, avec leurs compagnons |

Pièces lues (sha256 relevés, égaux à leurs compagnons) :
- lanceur v4 `b989db6e…5865` et départ v4 `64b2c0ce…5937` ;
- gardien v4 `ba39fe9b…46ed` et départ du gardien v4 `b333b2eb…6232` ;
- devis v5 `452e7bcf…47fb` ;
- complément 1 v3, par `git show` redirigé vers `lu-complement-1-v3.md` : `56ed20f8…b867` ;
- consigne commune, par `git show` redirigé vers `lu-consigne-commune.md` : `d327b3fc…23d8` ;
- ces deux extractions ont été retirées de mon dossier après usage, parce qu'elles portent un nom de modèle. Elles se refont à l'identique par le même `git show` redirigé (empreintes ci-dessus). Pour rejouer `controler-argv.py`, il faut d'abord refaire l'extraction du complément ;
- pour la même raison, j'ai retiré des cas les listes d'empreintes de la copie (`liste-de-la-copie.txt`, `empreintes-recalculees-de-la-copie.txt`) : ce sont les noms de fichiers du commit, égaux à la référence `ab90e73b…`, sauf dans c3 et f1 ;
- vérifications du lanceur v4 (`verification-lanceur-v4-v1.md`) et du gardien v4, rapports des auteurs.

## Ce que fait le script de démarrage (sur la machine, en superutilisateur, au premier démarrage)

**Assemblage.** Les données de démarrage contiennent, dans l'ordre :
- la ligne 1 du script ;
- `H0_PREVU=…` et `JETON_DEMARRAGE='…'`, deux lignes posées par le fabricant à la place de la ligne 2, `# @DONNEES-DE-DEMARRAGE@` ;
- le reste du script ;
- la ligne `__CHARGE_DES_PIECES__` ;
- la charge : un tar déterministe des quatre pièces, comprimé par `xz -9e`, en base64 sur une ligne.

Le script s'arrête par `exit` avant la charge.

**Lieux sur la machine.**
- `/srv/essai-3/` : journal `journal-demarrage-essai-3.txt`, dépôt lu `depot.git`, `racine/`, `venv/`, `tenue/`, `tenue-verification/`, `sorties/etapes-3-a-6-essai-3`, `versement/`.
- `/root/essai-3-secret/jeton` : droits 600, dossier en 700.

**Le jeton.**
- Il est lu dans une variable du shell, jamais exportée.
- Il est écrit par `printf` (commande interne du shell) dans le fichier 600, puis la variable est effacée par `unset`.
- Un assistant d'authentification de git (`assistant-jeton.sh`, droits 700) le lit dans ce fichier par `read` et le rend à git sur sa sortie standard. Il ne passe donc jamais dans une URL, dans une ligne de commande ou dans un journal.
- `GIT_CONFIG_GLOBAL=/dev/null` et `GIT_CONFIG_NOSYSTEM=1` : aucune configuration git extérieure n'est lue.

**Pas et codes.** Chaque pas écrit « début » et « fait » avec l'heure UTC. Tout échec écrit « ÉCHEC du pas (x), code N : … », et la même ligne dans `echec-demarrage-essai-3.txt`. Le script s'arrête avec ce code. Si le dépôt de versement est déjà préparé, il pousse d'abord une fois le journal et l'état.

| Pas | Action | Codes |
|---|---|---|
| (0) | `/srv/essai-3` déjà présent (second démarrage) | 20 |
| (0) | `H0_PREVU` absent ou mal formé | 21 |
| (0) | jeton absent, `@JETON@` ou hors `[A-Za-z0-9_-]{20,400}` | 22 |
| (0) | fichier du jeton, droits autres que 600 | 23 |
| (0) | assistant d'authentification | 24 |
| (a) | `apt-get update` puis `install git python3 python3-venv ca-certificates xz-utils` ; attente du verrou jusqu'à 600 s ; trois tentatives | 30, 31, 32 |
| après (a) | dépôt de versement préparé en local, sans réseau, avec un crochet avant poussée qui refuse toute référence autre que `refs/heads/recuperation/palier-0b-programme-1-essai-3-v1` et tout effacement | 25 |
| (b) | `git init --bare`, puis `fetch --depth 1 origin d7f949ac…` en HTTPS (trois tentatives), puis contrôle du commit ; l'adresse de poussée de ce dépôt est volontairement invalide | 40, 41, 42 |
| (c) | `git archive` du commit, extrait par `tar -x`. Refus si un `.git` se trouve à n'importe quelle profondeur. Puis la liste des empreintes par la recette du lanceur v4 (`LC_ALL=C find … \| sort -z \| xargs -0 sha256sum`), dont l'empreinte doit être `ab90e73b…91b4`. Enfin `EMPREINTES-DE-LA-COPIE.txt` (copie de la liste à l'octet) et `COMMIT-DE-LA-COPIE.txt` | 50, 51, 52, 53, 54 |
| (d) | `python3 -m venv /srv/essai-3/venv`, puis `pip install -r racine/requirements-cpu.txt` (trois tentatives), puis `pip freeze` au journal. L'environnement est hors de la racine : la racine doit rester égale à la référence | 60, 61, 62 |
| (e) | charge extraite dans `charge/` : exactement quatre entrées, fichiers réguliers ; chacune copiée dans `tenue/`, puis contrôlée à son empreinte écrite en dur | 70, 71, 72 |
| (f) | voir le détail ci-dessous | 80 à 84 |
| (g) | `setsid nohup` du même script en mode `--boucle-de-versement`, détaché | — |

Détail du pas (f), dans cet ordre :
1. Heure d'arrêt = `H0_PREVU` + 94 h (code 80 si elle ne se calcule pas).
2. Lanceur v4 en `--verifier-seulement` dans `tenue-verification/` : code 0 exigé, et 0 écrit dans le fichier (sinon 81).
3. Paramètres du gardien contrôlés par le gardien lui-même en `--verifier-seulement`, **avant tout départ** (sinon 82).
4. Départ de l'essai par `demarrer-essai-3-v4.sh` (sinon 83). Le code 5 est consigné en « ATTENTION », et la suite continue.
5. Départ du gardien v4 : interpréteur `/usr/bin/python3`, `--heure-arret-duree` à l'heure calculée, `--arret-mesure desarme`, `--seuil-libre-octets 8000000000` (sinon 84).
6. Heure de départ du gardien (22e champ de `/proc/PID/stat`) relevée pour la boucle.

**Boucle de versement (g).**
- Toutes les 30 min, elle copie dans `versement/essai-3/` : le journal de démarrage, `tenue/journal-de-tenue-essai-3.txt`, chaque inventaire dont le compagnon existe (avec ce compagnon), et `etat-essai-3.txt`.
- Le fichier d'état porte : l'heure, le numéro du versement, n (compté comme le gardien), les octets libres, le programme et le gardien (identifiant, vivant ou absent), le processus de la boucle, le code de sortie, la présence de `arret-gardien.txt` et l'échec éventuel.
- Elle commite, puis pousse `HEAD:refs/heads/recuperation/palier-0b-programme-1-essai-3-v1`, trois tentatives, jamais en force.
- Toutes les 60 s, elle regarde si le gardien vit encore (identifiant et heure de départ).
- Quand le gardien a disparu : un dernier versement, puis `fin-essai-3.txt`, poussé.
- Un échec de poussée est écrit au journal, et la boucle continue.

## Le fabricant

`fabriquer-donnees-demarrage-v1.sh NOM_DE_VARIABLE SORTIE [EMPREINTE_ATTENDUE_DU_SCRIPT]`

**Ce qu'il contrôle.**
- Il lit le jeton par `${!NOM}`, puis retire la variable de son environnement : les commandes qu'il lance n'en héritent pas.
- Code 3 : variable absente ou vide, ou jeton mal formé.
- Code 2 : nom réservé.
- Code 4 : `SORTIE` relative, déjà présente, ou dans un dépôt git.
- Code 5 : script autre que l'empreinte donnée, ligne 2 autre que le repère, pièce autre que son empreinte en dur, ou pièce que le script n'attend pas.
- Code 6 : données de plus de 32 768 octets.
- Code 7 : écriture ou contrôle qui échoue.
- À tout refus 6 ou 7, il retire les fichiers déjà écrits par cet appel.

**Ce qu'il écrit.**
- `SORTIE`, en droits 600 : les données complètes, avec `H0_PREVU` à l'heure de la fabrication (`date -u`).
- `SORTIE.sans-jeton` : le même texte, la ligne 3 étant `JETON_DEMARRAGE='@JETON@'`.
- `SORTIE.charge.b64` : la charge seule.
- `SORTIE.empreintes.txt` : les empreintes du script, des pièces, de la charge et du texte sans jeton, `H0_PREVU`, l'heure d'arrêt et la taille.

**Son contrôle final.** `SORTIE`, ligne 3 remplacée par celle du texte sans jeton, doit avoir la même empreinte que `SORTIE.sans-jeton`, et la taille attendue.

## Table des essais

Tous sur factices locaux :
- un dépôt nu factice, rempli du seul commit `d7f949ac`, plus deux commits artefacts ;
- un dépôt par cas, aux objets partagés, servi en HTTP sur 127.0.0.1 par `git http-backend`, derrière une authentification de base qui exige le jeton factice (lu dans un fichier par le serveur) ;
- un faux apt et un faux pip ;
- un faux `python3` : `-m venv` fabrique un environnement factice, et tout autre appel passe au vrai interpréteur, qui fait tourner le vrai gardien ;
- un faux programme du palier 0b : il écrit ses arguments, imite les étapes 3 et 4, puis rend 0 ;
- un guetteur de `ps`, qui relève toutes les 20 ms.

Réglages d'essai : intervalle de versement 5 s, gardien `--intervalle-s 1 --delai-force-s 5`, attente entre deux tentatives 1 s.

Les quatre colonnes de recherche du jeton, pour chaque cas :
- **fich.** : nombre de fichiers du cas qui le portent, hors les trois qui doivent le porter (`part-001`, `secret/jeton`, et le jeton du serveur) ;
- **hist.** : lignes qui le portent dans l'histoire versée (`git log -p` de la branche distante et du dépôt de versement) ;
- **ps** : lignes de `ps` qui le portent ;
- **600** : droits du fichier du jeton.

« — » : l'objet n'existe pas dans ce cas.

| Cas | Pas visé | Attendu | Rendu | fich. | hist. | ps | 600 | Tenu |
|---|---|---|---|---|---|---|---|---|
| s2-sain | tous | 0 ; argv égal au complément ; inventaires des étapes 3 et 4 ; 4 commits poussés dont « fin » | 0 en 86 s ; `controle-argv.txt` : ÉGAL (8 lignes) ; 4 commits, 8 fichiers sur la branche ; code de sortie 0 | 0 | 0 / 0 | 0 sur 2 771 relevés | oui | oui |
| s2, garde de branche | (g) | poussées vers `main`, vers une autre branche, vers `…-v1-bis`, et effacement de la branche : refusées ; poussée vers la branche permise : admise | 4 refus, message de la garde chaque fois, distant inchangé ; poussée permise admise | — | — | — | — | oui |
| s1 (fortuit) | (a) | — | 30 : factices non exécutables, « Permission denied », trois tentatives | 0 | — | 0 | oui | refus sûr |
| a1-apt-echec | (a) | 30 | 30 ; aucun versement (dépôt de versement pas encore prêt) | 0 | — | 0 | oui | oui |
| b1-jeton-refuse | (b) | 41 ; versement d'échec refusé (même jeton) | 41 ; 12 réponses 401 ; « ÉCHEC du versement » écrit | 0 | 0 | 0 | oui | oui |
| b2-commit-absent | (b) | 41 ; journal poussé | 41 ; 1 commit poussé (journal et état) | 0 | 0 / 0 | 0 | oui | oui |
| z1-jeton-vide | (0) | 22 | 22 ; aucun fichier de jeton | 0 | — | 0 | — | oui |
| z2-sans-jeton (`@JETON@`) | (0) | 22 | 22 | 0 | — | 0 | — | oui |
| z3-h0-faux | (0) | 21 | 21 | 0 | — | 0 | — | oui |
| z4-second-demarrage | (0) | 20, rien refait | 20 ; une ligne ajoutée au journal existant | 0 | — | 0 | — | oui |
| c1, commit avec `.git` dans l'arbre | (c) | 51 | **50** : `git archive` refuse lui-même (« invalid path '.git/HEAD' ») ; refus sûr, avant mon contrôle | 0 | 0 / 0 | 0 | oui | refus sûr, voir c2 |
| c2, `.git` laissé par l'extraction (faux `tar`) | (c) | 51 | 51 « la racine contient un .git : docs/.git » | 0 | 0 / 0 | 0 | oui | oui |
| c3, commit autre (un fichier en trop) | (c) | 53 | 53 (liste `82828a62…` contre `ab90e73b…`) | 0 | 0 / 0 | 0 | oui | oui |
| d1-pip-echec | (d) | 61 | 61 | 0 | 0 / 0 | 0 | oui | oui |
| e1, gardien altéré d'un octet | (e) | 72 | 72 (`5648d554…` contre `ba39fe9b…`) | 0 | 0 / 0 | 0 | oui | oui |
| e2, cinquième fichier dans la charge | (e) | 71 | 71 | 0 | 0 / 0 | 0 | oui | oui |
| f1, racine altérée après (c) (par le faux pip) | (f) | 81 ; aucun départ | 81 (lanceur : 12) ; aucun fichier de départ, faux programme jamais lancé | 0 | 0 / 0 | 0 | oui | oui |
| f2, paramètres du gardien refusés | (f) | 82 ; aucun départ | 82 (« … plus que 3600 s : refusée ») ; aucun départ | 0 | 0 / 0 | 0 | oui | oui |
| t1, témoin de fuite v1 | banc | les trois canaux trouvés | journal et URL trouvés ; **ps : 0** (le témoin ne fuyait pas, voir plus bas) | 2 | — | 0 | — | témoin à refaire |
| t2, témoin de fuite v2 | banc | les trois canaux trouvés | journal et URL trouvés ; ps : 44 lignes sur 45 relevés | 2 | — | 44 | — | oui |
| contrôleur des arguments, objet faux | banc | ÉCHEC | ÉCHEC, ligne 7 | — | — | — | — | oui |

**Fabricant** (`essais/travail/fabricant-essais/table.txt`, seconde passe, fabricant `a7d54bf0…`). 12 cas, 12 tenus :
- F01 variable vide : 3 ;
- F02 variable absente : 3 ;
- F03 jeton à espaces : 3 ;
- F04 jeton court : 3 ;
- F05 sortie existante : 4 ;
- F06 sortie relative : 4 ;
- F07 sortie dans un dépôt git factice : 4 ;
- F08 empreinte du script fausse : 5 ;
- F09 ligne 2 autre : 5 ;
- F10 trop grand (33 612 octets) : 6 ;
- F11 sain avec l'empreinte juste : 0 ;
- F12 sain sans empreinte : 0.

Contrôles des sorties saines :
- droits 600 ;
- jeton sur une seule ligne, la ligne 3 ;
- texte sans jeton égal aux données, jeton masqué ;
- lignes 3 et suivantes du script égales aux lignes 4 et suivantes du texte sans jeton, jusqu'au repère ;
- aucun autre fichier ne porte le jeton ;
- aucune sortie partielle n'est laissée ;
- `ps` : 0 ligne.

Première passe : 12 tenus aussi. Elle a montré un défaut : après le refus 6, `.charge.b64` et `.sans-jeton` restaient, sans jeton, et un nouvel appel aurait été refusé en 4. Corrigé (retrait à tout refus 6 ou 7), puis la passe a été rejouée. Le dossier de la première passe a été retiré. Le premier refus 6 avait été rencontré en vrai, sur une première version du script trop longue (34 044 octets).

Non joués :
- charge à pièce manquante : même contrôle que e2 ;
- échec de `venv` (code 60) ;
- codes 83 et 84 ;
- code 5 du départ ;
- boucle à l'intervalle d'emploi de 1 800 s, qui découpe l'attente en pas de 60 s : seul le pas de 5 s a été joué ;
- vrais apt, pip, GitHub et cloud-init.

## Écarts

1. **Les pièces voyagent dans les données de démarrage** : charge tar, `xz` et base64, ajoutée par le fabricant. Le point 2 du mandat ne la nomme pas. Le lanceur v4, le gardien v4 et leurs départs ne sont ni dans `d7f949ac` (`git cat-file -e` : absent) ni sur `origin/main` (`ls-tree` vide), et le pas (h) n'admet pas d'autre action réseau. Chaque pièce est contrôlée deux fois à son empreinte en dur : par le fabricant, et sur la machine.
2. **Clonage = `git init --bare`, puis `fetch --depth 1` du commit**, et non `git clone`. Le résultat est équivalent à un clone superficiel au commit. Le commit est sur `origin/main` (`git branch -a --contains`).
3. **Versement préparé en local dès la fin de (a)**, et **un versement unique en cas d'échec**, sur la seule branche permise. Le versement est hors de la lettre de (g), mais dans son objet.
4. **Code 5 du départ** (groupe ou heure de départ inconnus) : la suite continue, avec un gardien qui n'enverra aucun signal. Arrêter laisserait le programme lancé sans gardien ni versement. À trancher.
5. **Gardien interprété par `/usr/bin/python3`**, et non par l'environnement du dépôt. Il n'emploie que la bibliothèque standard.
6. **Paramètres du gardien contrôlés avant le départ de l'essai** (code 82). C'est un contrôle de plus que dans le départ du gardien, qui ne contrôle qu'après.
7. **Fichier d'état** : n y est pris au sens du gardien (dossiers de source sur 648). S'y ajoutent le numéro du versement, le code de sortie, la présence de `arret-gardien.txt` et l'échec éventuel. `fin-essai-3.txt` est versé aussi.
8. **Rien d'autre n'est versé.** Ni `journal-essai-3.txt` (sortie du programme), ni `arret-gardien.txt`, ni `mesure-essai-3.txt`. À trancher.
9. **Fabricant** :
   - jeton limité à `[A-Za-z0-9_-]`, de 20 à 400 signes ;
   - troisième paramètre facultatif : l'empreinte attendue du script ;
   - trois fichiers sans jeton à côté de la sortie ;
   - réglage d'essai `FABRICANT_SCRIPT`.
10. **Portes d'essai `ESSAI_DEMARRAGE_*`** (base, secret, adresse du dépôt, apt, python3, intervalle, attente, options du gardien, commit, référence). Elles sont écrites à la première ligne du journal. Sur la machine, la ligne attendue est « réglages d'essai : aucun ».
11. **Dépôt factice servi en HTTP local avec authentification**, et non par un simple chemin. Plus fort : l'assistant d'authentification et les refus 401 sont éprouvés.
12. `HOME=/root` si `HOME` est absent ; aucune configuration git globale ni système n'est lue.
13. `H0_PREVU` est l'heure de la fabrication, avant H0. L'arrêt vient donc plus tôt de H0 − `H0_PREVU`, du côté sûr. L'essai joué donne 19:36:16Z + 94 h = 2026-11-25T17:36:16Z.

## Réserves et supposés

- **Limite des données de démarrage de Hetzner : 32 Kio, supposée et non vérifiée sur la documentation.** Taille : 32 112 octets pour un jeton de 45 signes, soit une marge de 656 octets. Un jeton `github_pat_` de 93 signes laisse environ 608 octets. Toute ligne ajoutée au script la consomme.
- **Où le jeton reste lisible sur la machine** :
  - dans les copies que cloud-init garde des données (`/var/lib/cloud/instance/…`, en superutilisateur) ;
  - par le service de métadonnées de Hetzner, ouvert à tout processus local ;
  - dans le fichier 600.

  Le programme tourne en superutilisateur et pourrait le lire. C'est l'écart déjà déclaré (devis v5, § 6 (a), GO-2026-11-21-75). La garde de branche est locale : le jeton lui-même permet de pousser ailleurs.
- **Branche neuve.** La branche de récupération doit être neuve, et seule la machine doit y pousser : sans force, une autre histoire ferait refuser chaque poussée. Le devis v5, § 6 (a), prévoyait que le poste y verse le relevé de 6 h.
- **Cloud-init, supposé** :
  - il joue `part-001` par son chemin (`BASH_SOURCE`) ;
  - les processus détachés survivent à la fin de `cloud-final` (supposé `KillMode=process`) ;
  - le réseau est prêt.
- **Debian 13, supposé** :
  - git ≥ 2.32, pour `GIT_CONFIG_GLOBAL` ;
  - Python 3.13, avec les roues de `requirements-cpu.txt` (dont torch 2.14.1).
- **GitHub, supposé** :
  - il sert un commit atteignable demandé par son identifiant ;
  - il accepte l'utilisateur `x-access-token` avec le jeton choisi.
- **Le guetteur de `ps` ne voit pas un processus de moins de 20 ms.** Par construction, aucune ligne de commande ne porte le jeton (assistant appelé `assistant-jeton.sh get`).
- **La recherche dans l'histoire git n'a pas été vue rouge sur un témoin** : le témoin s'arrête avant tout versement. Les recherches dans les fichiers et dans `ps` l'ont été (t2).
- La machine gardera aussi environ 2 Go de clone et la charge ; la place n'est pas en cause (320 Go).
- **Place prise par le banc dans mon dossier.** Le dépôt factice partagé `essais/travail/distant/` fait 2,1 Go : à garder pour rejouer, à retirer sinon. Les racines et les clones des cas lourds ont été retirés après chaque cas. Les données de démarrage d'essai (`essais/travail/fabricant/`) et les deux jetons factices restent : ils ne portent que des jetons factices.

## Ce qui reste à trancher avant la création

1. **Quel jeton.** Je recommande un jeton à grain fin, restreint au seul dépôt de travail, droit « contenu » en lecture et écriture, à durée courte, révoqué après la destruction.
2. **Accepter le transport des pièces dans les données de démarrage** (écart 1). L'autre voie est de les pousser sur une branche et d'ajouter une seconde lecture réseau sur la machine.
3. **Vérifier la limite de 32 Kio** sur la documentation de Hetzner, et la taille réelle avec le jeton choisi : le fabricant la contrôle.
4. **Branche de récupération neuve et réservée à la machine.** Le relevé de 6 h se lit alors dans la pièce versée par la machine (`etat-essai-3.txt`, journal de tenue, inventaire de l'étape 3), et non par un versement du poste.
5. **Code 5** : continuer (choix actuel) ou arrêter (écart 4).
6. **Liste du versement** : ajouter ou non `journal-essai-3.txt`, `arret-gardien.txt`, `mesure-essai-3.txt` (écart 8).
7. **Contre-lecture S** du script et du fabricant. Le fabricant se joue ensuite avec son troisième paramètre égal à l'empreinte contre-lue du script (`580d81c5…` aujourd'hui).
8. **Enchaînement des deux voies.** Le devis v5, § 6, recommande la voie (a), depuis le poste local, mais ce mandat prévoit la création depuis la session, avec un fabricant joué dans la session. La mère doit dire quelle voie fait foi pour la création, la lecture de H0 et la destruction à H0 + 98 h.

## Relevé de méthode

**Chaîne de raisonnement.**
1. Les pièces, le commit, la référence et la branche font foi : mandat `dcd05a42…`, devis v5 `452e7bcf…` (§ 3 à 5), complément 1 v3 `56ed20f8…`, lanceur v4 `b989db6e…` (recette en tête, `REFERENCE_ATTENDUE` l. 67), gardien v4 `ba39fe9b…` (l. 670-705).
2. Les pièces sont absentes du commit et de `origin/main` : `git cat-file -e d7f949ac:…/lancer-essai-3-v4.sh` échoue, et `git ls-tree -r origin/main …` est vide. Elles doivent donc voyager avec les données de démarrage (pas 1, et le pas (h) du mandat).
3. Taille : la charge en base64 fait 21 245 octets (`wc -c`), le script 10 777, et les données 32 112 (sortie du fabricant, F11). La limite de 32 Kio est **supposée**.
4. Le jeton ne passe que par des commandes internes du shell (`printf`, `read`), par un fichier 600 et par l'assistant de git. Recherches : z, b, c, d, e, f et s2, colonne fich. = 0, hist. = 0, ps = 0. Le témoin t2 rend les trois canaux.
5. La racine est égale à la référence sans aucun remplacement : s2, lanceur en emploi (« 35732 fichiers refaits, égaux ») ; c3 rend 53 ; f1 rend 81.
6. La commande lancée est celle du complément aux trois chemins près : `controle-argv.txt`, ÉGAL ; l'objet faux rend ÉCHEC.
7. Les heures sont lues sur `H0_PREVU` + 94 h : journal de s2 (2026-11-25T17:36:16Z) et paramètres reçus par le gardien.
8. Le versement ne vise que la branche permise : `garde-branche.txt`, 4 refus et 1 admission.
9. Sur la machine réelle, apt, pip, GitHub et cloud-init se conduisent comme les factices : **supposé**.

**Objets de contrôle.**
- **Recherche du jeton.** Objet vrai par construction : le témoin t2, où le jeton fuit par trois canaux. Je prédisais trois canaux trouvés, et le rendu est journal, URL et `ps` : 44 lignes.

  Objet faux par construction : les cas sains et les artefacts, où le jeton ne devait sortir nulle part. Prédit 0, rendu 0 partout.

  Le premier témoin, t1, ne fuyait pas par `ps` : `bash -c` qui ne lance qu'une commande se remplace par cette commande et perd ses arguments. Le guetteur rendait donc 0 à bon droit. Le témoin a été refait (t2) avant de croire le guetteur.
- **Refus des pas.** Pour chaque pas (0), (a) à (f), au moins un artefact rend son code (table), et le cas sain s2 rend 0.

  Cas où le mécanisme visé ne pouvait pas échouer : c1. `git archive` refuse lui-même un `.git` dans l'arbre, et mon contrôle 51 n'y était pas atteint. Il a été éprouvé par une autre voie (c2, faux `tar`).
- **Garde de branche.** Faux : quatre poussées interdites, refusées. Vrai : la poussée permise, admise.
- **Contrôleur des arguments.** Vrai : le relevé de s2, ÉGAL. Faux : le chemin des sorties changé, ÉCHEC.

**Premier pas non justifié.** Pas 3 : la limite de 32 Kio des données de démarrage n'est pas lue sur la documentation de Hetzner. La lire sur la documentation, ou faire une création d'essai, qui coûterait, la justifierait. Le pas 9 vient ensuite : un démarrage réel, ou une machine d'essai debian-13 sur devis, le justifierait.

**Mode d'échec affecté.** Sans objet : je suis auteur, non relecteur.

**Dérivation de l'énoncé seul.** Sans objet : je ne suis pas agent de re-dérivation.

**Trouvaille de côté.**
- (a) `git archive` refuse un chemin `.git` dans l'arbre (« invalid path ») : la réserve de la vérification du lanceur v4 est donc aussi tenue par git, pour une copie faite par `git archive`.
- (b) `bash -c 'une seule commande'` remplace son image par la commande : utile à savoir pour tout témoin qui passe par `ps`.
- (c) Le relevé de 6 h du devis (§ 6 (a)) et la poussée de la machine visent la même branche : ce point est à trancher (point 4 ci-dessus).

**Évaluateur et conseil.**
- **Qui juge.** Mon banc juge le produit : faux serveur, factices, guetteur, recherches. Il a été admis sur le témoin t2 et sur les objets faux ci-dessus. Le lecteur S jugera ensuite.
- **Bon jugement sans le mériter.** C'est possible par plusieurs voies :
  - les factices d'apt, de pip, de `venv` et du programme ne reproduisent ni le réseau ni les durées ;
  - le serveur factice parle HTTP, et non HTTPS, et n'est pas GitHub ;
  - cloud-init n'est pas joué ;
  - l'intervalle de 1 800 s n'est pas joué ;
  - mes artefacts sont ceux auxquels j'ai pensé ;
  - les codes 5, 60, 83 et 84 ne sont pas joués.
- **Conseil au lecteur.** Viser d'abord les points suivants :
  - la survie des processus détachés après cloud-init ;
  - la taille ;
  - les endroits où le jeton reste lisible sur la machine ;
  - la branche partagée avec le relevé de 6 h.
