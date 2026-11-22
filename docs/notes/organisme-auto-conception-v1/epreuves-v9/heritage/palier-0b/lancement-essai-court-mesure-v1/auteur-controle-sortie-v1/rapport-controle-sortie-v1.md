# Rapport de l'auteur : outil de contrôle de sortie et d'envoi de la création, essai 3, v1

Pièce de travail (classe C), écrite le 2026-11-22 vers 02:10Z par l'auteur des versions précédentes (modèle O), sur l'ordre de 02:02Z. Le fabricant v8 et toute la pile restent inchangés. Les chemins sont relatifs à `controle-sortie-v1/`.

## Verdict

**13 cas sur 13 tenus, entièrement sur factices** (`travail/table.txt`). Aucun appel n'a été fait à Hetzner ni à GitHub.

Pendant la session :
- aucune machine n'a été créée ;
- `HCLOUD_TOKEN` n'a jamais été lu : chaque appel de banc le retire par `env -u`, et l'outil refuse ce nom au banc ;
- je n'ai affiché ni l'environnement ni la valeur d'aucune variable ;
- aucun `sleep` isolé, aucun heredoc, aucun processus arrêté ;
- aucun commit ni poussée ;
- aucun refus de permission, de classifieur ou de garde.

## Pièces (compagnon `.sha256` à côté de chacune)

| Pièce | sha256 |
|---|---|
| `controler-et-creer-essai-3-v1.py` | `8d88b2637d36b5b81638010e3283de3992f2571463e1ada1c231250f91cecb30` |
| `banc/banc-controle-sortie.sh` | `151918397a9273f35fe712a8ae1435e9ccb256e5d6e8b17d610a4bbc608b3840` |
| `banc/serveur-hetzner-factice.py` | `b2163bcf29bd8dede884755bb2f9e9db1b60b5067496c5d74fa2312e82764763` |
| `banc/corps-attendu.py` (voie indépendante) | `54d0204950e7b9b8020430e12a856967eaf6f8e1475a7fafc43ecfbc102a0cc0` |

Le banc copie aussi trois outils de la v8 : `fabricant-avec-jeton.sh`, `guetteur-ps.sh` et `ecrire-compagnons.sh`.

## Ce que fait l'outil

L'outil lit le fichier **une seule fois**, en octets (`f.read()`). Il ne le relit jamais ensuite.

Sur ces octets, il fait les contrôles dans cet ordre et s'arrête au premier échec, avec un code non nul, sans rien envoyer :

| Code | Contrôle |
|---|---|
| 10 | ASCII : `0x20` à `0x7e`, plus saut de ligne et tabulation (règle du fabricant) |
| 11 | une seule ligne commençant par `E_SCRIPT` (blancs de tête admis) : la ligne 4, égale à `E_SCRIPT=061f7993…` |
| 12 | forme et amorce : lignes 2 et 3, repère de charge unique, avant-dernière ligne ; amorce `524cfc4a…` |
| 13 | `user_data` d'au plus 32 768 octets en JSON échappé en ASCII |
| 14 | charge : base64 puis tar.gz en mémoire ; exactement cinq fichiers réguliers, le script `061f7993…` et les quatre pièces à leurs empreintes |

L'amorce est reconstruite comme l'inverse exact de l'assemblage du fabricant : ligne 1, puis le repère `# @DONNEES-DE-DEMARRAGE@`, puis les lignes 5 jusqu'au repère de charge. Le jeton n'y entre donc pas.

Le corps de création est construit sur ces mêmes octets, d'après la fiche du devis v5 :
- `essai-3-palier-0b`, `cpx42`, `hel1`, `debian-13` ;
- IPv4 et IPv6 ;
- `start_after_create` ;
- `ssh_keys: []`.

Les deux modes :
- **`--a-blanc`** (par défaut) écrit, dans un relevé neuf et sur la sortie, l'empreinte et la taille du corps et l'empreinte des données. Il ne lit aucun jeton et n'écrit jamais le corps.
- **`--envoyer`** poste le corps par `urllib`, dans le même processus, à `https://api.hetzner.cloud/v1/servers`. Le jeton est lu par le seul nom `HCLOUD_TOKEN`. Le relevé reçoit le code HTTP, l'identifiant, le statut, l'heure et le corps de la réponse expurgé : clés `root_password` et `user_data` retirées partout. Codes : 20 si le jeton est absent ou mal formé, 21 si l'envoi échoue ou si la réponse n'est pas un 201.

Hors banc, les options `--adresse`, `--nom-jeton` et `--pause-apres-lecture` sont refusées (code 2). Au banc, seule une adresse `http://127.0.0.1:PORT/…` est admise, sans mandataire.

## Table des cas (`travail/table.txt`)

| Cas | Attendu | Rendu |
|---|---|---|
| C1, fichier sain, à blanc | 0 | 0 ; corps de 32 809 octets, empreinte égale à la voie indépendante |
| C2, amorce altérée d'un octet | refus | 12, amorce `d78a080f…` |
| C2, charge altérée d'un octet | refus | 14 (`ReadError`) |
| C2, deux lignes `E_SCRIPT=` | refus | 11 (lignes 4 et 5) |
| C2, une ligne `E_SCRIPT+=` | refus | 11 (lignes 4 et 5) |
| C2, `user_data` trop grand | refus | 13 (33 797 octets) |
| C2, signe non ASCII | refus | 10 |
| C3, adresse locale hors banc | refus | 2 |
| C4, `--nom-jeton` hors banc | refus | 2 |
| C5, au banc, adresse autre que 127.0.0.1 | refus | 2 |
| C6, au banc, nom `HCLOUD_TOKEN` | refus | 2, jeton non lu |
| C7, envoi sain au banc | 0, corps reçu = corps calculé | 0 ; détail ci-dessous |
| C8, fichier remplacé sur disque après la lecture | les octets lus sont envoyés | 0 ; détail ci-dessous |

Après C3 à C6, le serveur factice a reçu 0 requête.

**C7.** Le serveur factice reçoit un corps `c4696225…`. C'est l'empreinte que l'outil a calculée à blanc et celle de la voie indépendante : **ÉGAUX**. Le jeton reçu est bien le jeton factice de l'interface. Le relevé ne porte ni `"root_password"`, ni le mot de passe factice, ni `user_data`.

**C8.** Pendant la pause du banc, juste après la lecture, le fichier est remplacé (`mv`) par d'autres données valides. Le serveur reçoit `c4696225…`, le corps des **octets lus**. Le corps des nouveaux octets serait `cdde2056…`. Le relevé porte l'empreinte des données lues. Le serveur a reçu 2 requêtes au total.

**Jetons.** Le jeton factice du dépôt (les deux) et celui de l'interface ne sont dans aucun fichier : la seule exception, ce sont les données d'entrée du banc et les fichiers de jetons eux-mêmes. Ils ne sont non plus dans aucune sortie de l'outil (0 ligne) ni dans `ps` (59 relevés, 0 ligne).

Les artefacts sont décrits en tête de `travail/table.txt`. Pour les insertions, la colonne « octets différents » de `cmp -l` compte les décalages, et non les octets ajoutés.

**Dénominateur.** Il y a eu une passe 1, gardée dans `travail-passe-1-controle-root-password-mal-ecrit/` (ses données d'entrée sont retirées). Son contrôle « root_password présent » était faux par construction : il comptait le mot dans le libellé « root_password et user_data retirés ». J'ai corrigé le banc pour chercher la clé `"root_password"` et le mot de passe factice. L'outil n'a pas changé.

## Écarts et points non joués

1. **Le vrai envoi n'est pas joué.** En vrai, `urllib` passe par le mandataire de sortie de la session s'il existe. Le certificat de ce mandataire (`SSL_CERT_FILE` ou un équivalent) n'a pas été éprouvé.
2. **Le contrôle de la charge va au-delà de l'ordre.** Il exige aussi les quatre pièces à leurs empreintes et aucun autre membre.
3. **`ssh_keys` est écrit comme une liste vide**, et non omis.
4. **Taille au sens de Go, pour information** : 32 708 octets (marge 60). Elle est mesurée par la v8 ; l'outil ne refuse que sur la lecture ASCII, comme l'ordre le demande.
5. **L'ordre des contrôles est choisi** pour que chaque artefact soit arrêté par son propre contrôle.

## Chemins lus hors de ce dossier

- Fabricant v8 et ses pièces :
  - `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/auteur-script-demarrage-essai-3/v8/fabriquer-donnees-demarrage-v8.sh`, avec l'amorce, le script et le réducteur de ce dossier ;
  - les outils copiés depuis `…/auteur-script-demarrage-essai-3/v8/essais/outils/`.
- Jetons factices du dépôt : `…/auteur-script-demarrage-essai-3/essais/travail/jeton-factice.txt` et `jeton-factice-autre.txt`.
- Les quatre pièces, lues par le fabricant :
  - `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-lanceur-v4/lancer-essai-3-v4.sh` et `demarrer-essai-3-v4.sh` ;
  - `…/lancement-essai-court-mesure-v1/auteur-lanceur-v3-gardien-v4/gardien-essai-3-v4.py` et `demarrer-gardien-essai-3-v4.sh`.
- Lus pour l'ordre :
  - `…/lancement-essai-court-mesure-v1/devis-serveur-loue-palier-0b-essai-3-v5.md` (lignes 1 à 40) ;
  - `…/lancement-essai-court-mesure-v1/verification-fabricant-v8-v1/verification-fabricant-v8-v1.md` (verdict et réserve).
- `/home/user/controle-ia-travail/.venv/bin/python`.
- `/dev/urandom` (jeton factice de l'interface) et `/dev/zero` (remplissage).

## Outils du système employés

- **Shell** : `bash` (commandes internes `read`, `printf`, `echo`, `wait`, `umask`, `set`, `export`, `cd`, `:`) et `env` (`-u HCLOUD_TOKEN`).
- **Fichiers** : `mkdir`, `rm`, `mv`, `cp`, `chmod`, `ls`, `find`, `stat`.
- **Texte** : `cat`, `sed`, `grep`, `cut`, `tr`, `wc`, `head`, `tail`, `seq`.
- **Comparaison et empreintes** : `sha256sum`, `cmp`, `diff`.
- **Encodage, archive, dates** : `base64`, `tar`, `gzip`, `date`, `dirname`, `basename`.
- **Git** : `/usr/bin/git`, pour `init --bare` et `ls-remote`, sur le dépôt factice vide du banc, retiré à la fin.
- **Processus** : `ps` et `sleep`, dans la boucle de guet `guetteur-ps.sh` et dans les boucles d'attente de fichiers.
- **Python**, en `-I`, modules de la bibliothèque standard seulement : `base64`, `datetime`, `hashlib`, `io`, `json`, `os`, `re`, `sys`, `tarfile`, `time`, `urllib`, `http.server`.
