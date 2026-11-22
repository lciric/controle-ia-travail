# Rapport de l'auteur : outil de contrôle de sortie et d'envoi de la création, essai 3, v2

Pièce de travail (classe C), écrite le 2026-11-22 vers 02:28Z par l'auteur des versions précédentes (modèle O), sur l'ordre de 02:21Z. Elle apporte trois corrections, R1 à R3, et rien d'autre. La v1 reste intacte. Les chemins sont relatifs à `controle-sortie-v2/`.

## Verdict

- **Les 13 cas de la v1, rejoués sur la v2 : tous tenus.** S'y ajoutent les cas des trois corrections, le témoin du recompactage et le témoin v1 de la redirection, eux aussi tous tenus (`travail/table.txt`).
- **Remesure** : sur les mêmes données saines, le corps de la v2 et celui de la v1 sont **égaux** (`17a9c373…`, 32 809 octets).
- **Jetons factices** : présents dans aucun fichier de sortie, aucune sortie des outils, ni dans `ps` (101 relevés, 0 ligne).

Ce qui n'a pas eu lieu :
- aucune machine, aucun appel réel ;
- `HCLOUD_TOKEN` n'a jamais été lu : il est retiré par `env -u`, et l'outil le refuse au banc ;
- je n'ai affiché ni l'environnement ni la valeur d'aucune variable ;
- aucun `sleep` isolé, aucun heredoc ;
- aucun processus arrêté ;
- aucun commit ni poussée ;
- aucun refus.

**Écart à la règle.** Un de mes appels a passé du code en ligne à l'interpréteur : `python -I -c 0`, une instruction vide, sans effet. Il est déclaré ici.

## Pièces (compagnon `.sha256` à côté de chacune)

| Pièce | sha256 |
|---|---|
| `controler-et-creer-essai-3-v2.py` | `73046b317d4f1a0c751891abaeb7d849e5fa906f79fd671dbaaff9ee6ea460d5` |
| `banc/banc-controle-sortie.sh` | `e4b3e6ff3b034f8f886a2a52fc275dee857954f59528fc3b98f110f57c57b34b` |
| `banc/serveur-hetzner-factice.py` (ajoute la route `POST /v1/servers-redirige`, qui répond 302 vers `/autre-route`, et journalise toutes les requêtes) | `f5dd44de1a765d0dec80faeffa906adaac9f3ff6dbc449a005bce2043f2ae4d3` |
| `banc/corps-attendu.py`, `fabricant-avec-jeton.sh`, `guetteur-ps.sh`, `ecrire-compagnons.sh` | repris de la v1, inchangés |

## Corrections

**R1, redirections.** L'ouvreur est monté à la main (`OpenerDirector`), sans aucun gestionnaire de redirection. Il contient seulement :
- le mandataire (`ProxyHandler`), réglé sur aucun mandataire pour une adresse de banc ;
- les gestionnaires `HTTPHandler` et `HTTPSHandler` ;
- les gestionnaires d'erreur `HTTPDefaultErrorHandler` et `HTTPErrorProcessor`.

Une réponse 3xx est un échec : **nouveau code 22**, écrit au relevé. Elle n'est jamais suivie, et rien n'est renvoyé ailleurs.

**R2, charge.**
- Le flux gzip est décompressé par `zlib`. L'outil exige que le flux soit fini (`eof`), avec `unused_data` vide : une seule trame, et aucun octet après elle.
- Le tar est relu sans compression. Après le dernier membre, l'outil exige des zéros seulement, sur une longueur exacte : le plus petit multiple de 10 240 qui contient le dernier membre plus deux blocs nuls. C'est le remplissage du tar GNU du fabricant : 81 920 octets ici.
- Sinon : refus 14.

**R3, `--nom-jeton`.** L'option n'est admise qu'avec `--adresse`, et seulement au banc ; sinon, code 2.

## Table des cas (`travail/table.txt`)

| Cas | Attendu | Rendu |
|---|---|---|
| C1, sain, à blanc | 0 | 0 ; corps égal à la voie indépendante |
| C2, amorce altérée d'un octet | 12 | 12 |
| C2, charge altérée | 14 | 14 |
| C2, deux lignes `E_SCRIPT=` | 11 | 11 |
| C2, `E_SCRIPT+=` | 11 | 11 |
| C2, trop grand | 13 | 13 (33 797 octets) |
| C2, non ASCII | 10 | 10 |
| **C2, octets aléatoires après le gzip (R2)** | 14 | 14 (64 octets après la fin) |
| **C2, seconde trame gzip (R2)** | 14 | 14 (37 octets après la fin) |
| **C2, octets aléatoires après le tar (R2)** | 14 | 14 (81 984 octets, 81 920 attendus) |
| **C2, octet non nul dans le remplissage du tar (R2)** | 14 | 14 |
| C2, témoin : charge saine recompressée | 0 | 0 |
| Remesure : v1 et v2 à blanc sur les mêmes données | même corps | ÉGAUX (`17a9c373…`) |
| C3, adresse hors banc | 2 | 2 |
| C4, `--nom-jeton` hors banc | 2 | 2 |
| C5, au banc, adresse autre que 127.0.0.1 | 2 | 2 |
| C6, au banc, nom `HCLOUD_TOKEN` | 2 | 2 |
| **C9, au banc, `--nom-jeton` sans `--adresse` (R3)** | 2 | 2 |
| C7, envoi sain au banc | 0, corps reçu = corps calculé | 0 ; ÉGAUX ; jeton de l'interface juste ; ni `"root_password"` ni `user_data` au relevé |
| C8, fichier remplacé après la lecture | octets lus envoyés | 0 ; voir ci-dessous |
| **C10, réponse 302 vers une autre route (R1)** | 22 | 22 ; voir ci-dessous |
| T1, témoin : la v1 sur la même redirection | suit la redirection | voir ci-dessous |

Précisions :
- **C3 à C6 et C9** : le serveur factice n'a reçu aucune requête.
- **C2, charge saine recompressée** : la charge recompressée est identique à la charge saine.
- **C8** : le serveur a reçu le corps des octets lus, et non celui des nouveaux octets.
- **C10** : le serveur a reçu 1 requête. Aucune requête n'a atteint `/autre-route`, et le jeton factice n'a paru sur aucune autre route. Le relevé porte « ÉCHEC (22) : réponse de redirection, code HTTP 302, non suivie ».
- **T1** : la v1 a fait 2 requêtes, dont 1 vers `/autre-route`, avec le jeton factice. C'est le défaut R1, et il est vivant sur la v1 : C10 a donc de la puissance.

Pour les quatre cas R2 et le témoin, seule la dernière ligne (la charge) diffère des données saines.

## Chemins lus hors de ce dossier

Dans `/tmp/claude-0/-home-user-controle-ia-travail/d90e22c7-b755-5554-90ae-faa848d18eef/scratchpad/auteur-script-demarrage-essai-3/` :
- `v8/fabriquer-donnees-demarrage-v8.sh`, avec l'amorce, le script et le réducteur de ce même dossier ;
- `controle-sortie-v1/controler-et-creer-essai-3-v1.py`, pour la remesure et le témoin T1 ;
- `controle-sortie-v1/banc/` : les outils du banc, copiés ;
- `essais/travail/jeton-factice.txt` et `essais/travail/jeton-factice-autre.txt`.

Les quatre pièces, lues par le fabricant :
- `/home/user/controle-ia-travail/docs/notes/organisme-auto-conception-v1/epreuves-v9/heritage/palier-0b/lancement-essai-court-mesure-v1/auteur-lanceur-v4/lancer-essai-3-v4.sh` et `demarrer-essai-3-v4.sh` ;
- `…/lancement-essai-court-mesure-v1/auteur-lanceur-v3-gardien-v4/gardien-essai-3-v4.py` et `demarrer-gardien-essai-3-v4.sh`.

Autres :
- `…/lancement-essai-court-mesure-v1/verification-controle-sortie-v1/verification-controle-sortie-v1-v1.md` (réserves) et la liste de son dossier ;
- `/home/user/controle-ia-travail/.venv/bin/python` ;
- `/dev/urandom` et `/dev/zero`.

## Outils du système employés

- **Shell et environnement** : `bash` (commandes internes `read`, `printf`, `echo`, `wait`, `umask`, `set`, `export`, `cd`, `:`, substitution de processus `<( )`), `env -u`.
- **Fichiers** : `mkdir`, `rm`, `mv`, `cp`, `chmod`, `ls`, `find`.
- **Texte** : `cat`, `sed`, `grep`, `cut`, `tr`, `wc`, `head`, `tail`, `seq`.
- **Empreintes et comparaison** : `sha256sum`, `cmp`, `diff`.
- **Codage et archives** : `base64`, `gzip`, `tar` (dans le fabricant).
- **Autres outils** : `date`, `dirname`, `basename`.
- **Git** : `/usr/bin/git`, pour `init --bare` et `ls-remote` sur le dépôt factice vide, retiré à la fin.
- **Processus** : `ps` et `sleep`, dans `guetteur-ps.sh` et dans les boucles de guet.
- **Python** (`-I`), bibliothèque standard seulement : `base64`, `datetime`, `hashlib`, `io`, `json`, `os`, `re`, `sys`, `tarfile`, `time`, `urllib`, `zlib`, `http.server`, `py_compile`.
