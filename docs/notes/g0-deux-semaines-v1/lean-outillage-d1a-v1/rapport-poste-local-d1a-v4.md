# Rapport du poste local — essai Lean D-1a, quatrième essai (rapport v4)

- **Écrit par** : la session du poste local `local_3132aef1-f8e1-4066-941b-688bdaf275e7` (Claude Opus 5.5, `claude-opus-5-5`), le 2026-11-21 vers 19:25 UTC (`date -u`). Pièce de travail (classe C).
- **Sous** : la consigne v8 (`consigne-poste-local-lean-d1a-v8.md`, `3279bf4256b8c1eab212b2ff76c6ce7155d76863253d18b5f812d0f486cf1ed5`) et son erratum 1 (`84bdfff6539bfbb785ced642384315a9f6485beba8c5411ae8c280def4e46d8e`), lus sur `origin/main` au commit `74a15437`.
- **Procédure** : v12 (`procedure-poste-local-d1a-v12.md`, `10872ae6bb6b4bdc45e48742ac879a50d024408c283138da51a5b7aaaff43cac`), au commit `47c7faaf`.
- **Dépense** : GO-2026-11-10-13.
- **Session mère** : `session_01Qi7Gr3eYmAhDEJzqLgWcv1`.
- **Branche** : `donnees/lean-outillage-d1a-poste-local-v6`, partie de `47c7faaf50da2c2abd2cce32dc203c8a7f49e03b`. La tête de `prep/lean-outillage-d1a-v11` n'a pas bougé.
- **Statut de cette pièce** : une lecture du poste, jamais un verdict de porte. L'outillage D-1a n'est déclaré conforme par personne d'autre que la mère, sur ces lectures.

## 0. En bref

| Lecture | Résultat |
|---|---|
| Pilote « avant » | code 0 ; trois essais R5 conformes |
| Pas `noyau` | **conforme, 18 cas sur 18** |
| Épreuve d'isolement v8 | **code 1, « non conforme »** : 35 cas sur 36 ; un seul cas en échec, « sortie de lui-même en code 137, sans consommer la limite (5 s) », écart « stdout sans « SORTIE 137 » » ; cause non établie |
| Genres | gardes Lean, isolement Lean, Python, limites Lean : conformes ; limites : non conforme ; aucun genre « épreuve morte » |
| « Temps de processus (5 s) » | « délai » à 5,012 s : conforme (§ 8.3, première lecture) |
| Limite Lean (512M) | conforme, lue sur la seule compilation |
| Mémoire, chemin du cgroupe | juste ; pics rapportés |
| Mesures, trois passages en parallèle | **`parallele_3_compte` vrai, aucun motif** : le passage en parallèle est compté |
| Sondes réseau | « fermée » après la coupure et à la fin, aucun écart |
| Serveur | 177109613, de 18:53:18Z à 19:11:58Z, détruit par son identifiant ; environ 0,28 USD |

## 1. Vie du serveur

- **Serveur** : Hetzner `ccx33`, `hel1`, identifiant **177109613**, nom `lean-outillage-d1a-fae70647f54e`, étiquette `creation=fae70647f54e4c5a8207fae7ed07a795`.
- **Création** : L5 lancé à 18:53:16Z ; serveur vivant depuis 2026-11-21T18:53:18Z.
- **Destruction** : par son identifiant à **19:11:58Z** (`MV7 detruire`, code 0, une tentative). Vie : environ 18 min 40 s.
- **Machine** (relevé de l'installation) : Ubuntu 24.04.4 LTS ; noyau 6.8.0-137-generic ; 8 cœurs ; 32 857 440 256 octets de mémoire ; systemd 255 (255.4-1ubuntu8.16) ; bubblewrap 0.9.0 ; nftables 1.0.9.
- **Coût** : une heure facturée de `ccx33`, soit environ 0,28 USD (0,22692 EUR au taux de 1,25, d'après `registres/depenses.md`).
- **Cumul sous GO-2026-11-10-13** : environ **1,12 USD sur 65**. Quatre serveurs : 175751342, 175838427, 177067030, 177109613.
- **Minuterie** : PID 9268, échéance 2026-11-23T15:47:18Z (`H` − 1 h). Conforme en L6 (18:53:43Z) et à 19:12:10Z ; arrêtée par son PID à 19:12:21Z.
- **Inventaires** : « aucun serveur de l'essai » en L4 (18:52:57Z), après la destruction (19:12:00Z) et à l'inventaire final (19:12:24Z), avec `ips_primaires_non_attribuees` vide.
- **Accès** : clé SSH 132916986 et pare-feu 12126345 supprimés chez le loueur à 19:12:09Z (`acces-supprimer`, code 0, sans 422). Aucun fichier du poste n'a été supprimé.
- **Relecture de la mère** (M4, par son propre jeton, 19:15:31Z) : le serveur 177109613 rend 404 ; aucun serveur par étiquettes ni par nom ; aucune clé ni pare-feu sous l'étiquette. La ligne « en tâche jusqu'à » est close et l'arrêt inscrit par la mère (R-4681). Les tâches T1 à T3 restent actives comme filets.

## 2. Préfixe du poste et adresses de sortie

- **Adresse du poste** : lue depuis Ubuntu par une requête au service de `adresses-sortie`, à 18:24:31Z, car Lazar ne l'a pas donnée (écart 2 du rapport v3, repris ; voir § 9).
- **`MV7 adresses-sortie`**, à 18:24:38Z, code 0. Comptes seulement :
  - 16 essais, 16 réponses, 0 échec, 0 illisible ;
  - 1 adresse distincte, l'adresse du poste vue ;
  - 0 hors du /24 ;
  - `prefixe_conseille` 32.
- **`P` retenu : 32.**
- **Signal de la consigne** : la mesure rend 32, alors que les deux premiers essais avaient vu plusieurs sorties dans le même /24. Lazar l'a reçu dans la session, la mère dans le message de 18:26Z. Aucune connexion SSH n'a échoué de tout l'essai.

## 3. Essai à blanc et mandataire

- **Question à Lazar** (« le poste a-t-il changé ? ») : réponse mot pour mot, « Rien n'a changé ».
- **Doute** : le compte Claude a changé (erratum 1, point 2). Relevé en lecture seule :
  - aucun réglage de bac à sable dans les fichiers de réglage de l'utilisateur ;
  - aucune commande du harnais pré-autorisée ;
  - session en mode de permission « auto ».

  Un doute compte comme un changement : **essai à blanc refait** entier (procédure, section 0, point 4).
- **Relevés** :
  - 17:46:25Z : `sleep 3600` détaché (`start_new_session`), PID 8075 ; `kill -0` code 0, dans une autre commande.
  - Relance réelle de l'application Claude par Lazar, par le Gestionnaire des tâches.
  - 18:17:29Z : `kill -0 8075` code 0.
  - Preuve de relance par l'écart D1. Hôte de la session : `claude.exe` créé à 18:16:44Z, sous le processus de l'application créé à 18:16:04Z (parent : l'explorateur), tous deux plus récents que le départ du `sleep`. L'ancien hôte, créé à 17:10:16Z, a disparu.
  - Deux `claude.exe` anciens, créés à 09:39:45Z et à 09:58:13Z, sont restés vivants. Ils ne portent pas cette session.
  - 18:18:44Z : `kill 8075` code 0 (R10) ; `kill -0` ensuite code 1.
- **Mandataire** : `[]` à 17:38:38Z et à 18:18:44Z.
- **Version d'Ubuntu du poste** : Ubuntu 26.04.1 LTS. Python 3.14.4.
- **Terminal WSL** : processus 1 d'Ubuntu démarré à 07:41:26Z, même valeur aux deux relevés (17:38:38Z, au début du mandat 2, et 18:47:05Z, juste avant L1), et encore à 18:17:29Z. Les deux `bash` du terminal vivent depuis 07:41:34Z. Ubuntu n'a pas redémarré pendant l'essai.

## 4. Canal des messages

- **Premier message direct** envoyé à 17:27:31Z ; accusé de réception de la mère à 17:28:10Z.
- **Envois directs suivants : échecs.** Cinq envois du poste vers la mère ont échoué, vers 17:47Z, 17:48Z, 17:52Z, 17:55Z et à 18:18Z, après la relance de l'application, sur l'erreur « this computer is not a trusted device for your account yet ». Le sens mère → poste a toujours fonctionné.
- **Repli écrit déclenché** (deux échecs à une minute d'écart). Lazar a dit ensuite, mot pour mot :
  - « met en place yun canal direct de comm entre la mere et toi, je ne vais pas faire le relais » ;
  - « Ce que je propose, sans relais de ta part : go » ;
  - « Canal par la branche ».
- **Écart demandé par écrit** (message de 18:26Z, commit `934dc30e`) et **accepté par écrit par la mère** :
  - du poste vers la mère : des fichiers neufs dans `V/messages-poste-vers-mere-d1a-v6/`, chacun avec son compagnon `.sha256`, `garde-poste` passé avant chaque commit ;
  - de la mère vers le poste : son outil d'envoi.
- **Geste de Lazar** : il a dit une seule fois à la mère de lire la branche. Ce n'est pas un relais.
- **Messages versés** :
  - 18:26Z, mandat 2 et demande d'écart (`157233e1…`) ;
  - 18:49Z, L3 (`602ccc54…`) ;
  - 18:54Z, L7 ;
  - 19:14Z, fin.
- **Mot « armée »** : reçu de la mère par son outil d'envoi, gestes M1 à M6 faits à 18:51Z, avec l'empreinte du fichier de rattrapage `00e7972d…`, égale à la mienne. Son « poste armé » de 17:28Z n'a pas été lu comme ce mot, faute d'empreinte.

## 5. Sorties des étapes

- **Mandat 1** :
  - clone neuf à une seule branche (`main`), sous un nom neuf du système de fichiers d'Ubuntu ;
  - `ls-remote` de `-v6` avant la création : code 0, aucune ligne ;
  - après la création : `rev-parse HEAD` = `47c7faaf`, `status` vide ;
  - `git push -u` fait, référence de suivi posée (`@{upstream}` = `origin/donnees/lean-outillage-d1a-poste-local-v6`) ;
  - `V` sans rattrapage ni journal des créations ;
  - six compagnons du code égaux à la liste de la consigne (`2df3595d`, `3b1dabd7`, `c7e5be09`, `bd05d9b9`, `182033f8`, `3ef23bfa`) ;
  - documents de lancement conformes ;
  - rapport v3 lu sur `-v4` (`be44a0d6…`).
- **L1** (18:47:18Z) :
  - `preparer`, code 0, jeton `fae70647f54e4c5a8207fae7ed07a795` ;
  - `T_LIM` 2026-11-22T00:47:18Z ; `H` 2026-11-23T16:47:18Z ;
  - tâches de la mère T1 `trig_01MU2WJrqVdoSec5i2DVx4SJ`, T2 `trig_0194ZmtSi1duE4ecntDoHMaM`, T3 `trig_01UKkJNDY21f29mZTCF2cWKu`.
- **L2** (18:47:43Z) :
  - clé ed25519 neuve, dans un dossier neuf hors du dépôt ;
  - `acces-creer --prefixe-poste 32`, code 0 : clé 132916986 (empreinte `47:c5:3f:c7:a6:1d:af:3c:82:9d:7d:de:f9:fc:28:6a`), pare-feu 12126345.
- **L3** :
  - commit `b1f8dff2` ;
  - rattrapage `00e7972d004729905cd2c98d603be6da7ee4174370dd73136bf90a93785a8347`, accès `55c6e76d…`.
- **L4 à L7** :
  - inventaire vide à 18:52:57Z ;
  - `creer-et-armer … --type ccx33 --lieu hel1 --deja-depense-usd 0.84` : processus détaché 9204, fin normale ;
  - contrôle de survie : vivante, « garder » ;
  - L6 conforme ;
  - L7 poussé au commit `c3f1e408`.
- **Section 3** :
  - L'adresse du serveur était déjà connue du poste (adresse réattribuée) : `ssh-keygen -R`, l'ancien fichier gardé par `ssh-keygen` en `.old`.
  - Pilote « avant » de 18:55:19Z à 18:58:02Z, code 0 ; installation par `installer_chaine_v2.sh` (cache de Mathlib en 69 s, `lake build` sans reconstruction).
  - Coupure à 18:58:29Z, deux règles. Première `verifier-coupure` « pending » (code 1) ; seconde lecture seule à 18:59:42Z, journal neuf, « applied » (code 0) ; nftables chargé sur la machine à 19:00:01Z.
  - Pilote « apres » de 18:59:59Z à 19:11:39Z, code 0. Vérificateur épinglé `3ef23bfa…`, égal au compagnon et au troisième essai.
- **Section 5** : voir le § 1.
- **Pièces** : sous `V/pieces-poste-local-d1a-fae70647f54e-v1/`, 13 fichiers, manifeste `V/empreintes-pieces-poste-local-d1a-fae70647f54e-v2.sha256` (`da2044df…`).

## 6. Lecture de la section 8 (procédure v12, sans rien y changer)

### 8.1.1 Pilote « avant »

- **Code 0.**
- **Garde de lisibilité** conforme : aucun chemin fermé aux autres dans les trois arbres ; `bac` lit 16 chemins et exécute `lean` et `python`.
- **« `bac` lit `Mathlib.olean` »** conforme : cas sain lu, témoin 0644 lu, artefact 0600 refusé.
- **« Le vérificateur compile sur la machine »** conforme : cas sain en code 0, sans message ; copie cassée refusée (code 1, `error`). Lean 4.35.0, commit `eb6cafb7…`.
- **Sonde « avant »** : « ouverte ».

### 8.1.2 Pas `noyau`

**`premier-pas-noyau-v6.json` : `conforme` vrai, 18 cas sur 18** (9 cas, avec et sans G-L3+). La lecture continue.

### 8.1.3 Code de l'épreuve

`epreuve-code-v6.txt` : **1, non conforme**.

### 8.1.4 Épreuve d'isolement (`epreuve-isolement-v6.json`)

1. **`statut`** : « non conforme ». Manifestes d'avant et d'après égaux.
2. **`genres`** : gardes Lean conforme ; isolement Lean conforme ; Python conforme ; **limites non conforme** ; limites Lean conforme. **`genres_morts`** : vide. Cas sains : isolement Lean vrai, Python vrai.
3. **Les cas, genre par genre** :
   - **Gardes Lean (21)** : 21 cas `ok`, aucun écart.
   - **Isolement Lean (5)** (§ 8.2) : chacun porte `sonde_muette` faux et `code_compilation` 0, et chaque tentative a l'issue attendue.
     - Lectures hors du dossier : toutes « ECHEC » (fichier introuvable : leurre, leurre par `/proc/1/root`, `/etc/shadow`, clé SSH de root, `/srv`, harnais, tampon du réseau).
     - Écritures : toutes « ECHEC » (contrôle, contrôle sous `/srv` et harnais introuvables ; Mathlib, `.olean` de Mathlib, elan et `/usr` en système de fichiers en lecture seule). L'extrait est tronqué au-delà.
     - Cas sain de persistance : **`ecriture-tmp` et `ecriture-item` « REUSSI »**.
     - Rien pour l'item suivant : trois « ECHEC » (fichier introuvable).
     - **Détail des trois tentatives réseau** :
       - `reseau-curl-ip` : ECHEC, code 7, « Failed to connect to 1.1.1.1 port 80 after 0 ms: Couldn't connect to server ». C'est un refus du réseau.
       - `reseau-dns` : ECHEC, code 1, `socket.gaierror: [Errno -3] Temporary failure in name resolution`. C'est une résolution impossible.
       - `reseau-python-tcp` : ECHEC, code 1. La trace commence par `socket.py`, ligne 852, dans `create_connection`, puis « raise excep… ». **La raison n'est pas dans les 160 caractères gardés.** Le programme a bien été lancé (la trace vient de `create_connection`), mais le refus du réseau n'est pas lisible dans l'extrait. Je le dis, sans conclure plus loin.
     - Aucune tentative ne dit que le programme n'a pas été lancé : ni « could not execute external process », ni code 127.
   - **Python (4)** : 4 cas `ok`, aucun écart.
   - **Limites (5)** :
     - « mémoire (512M) » : incident « mémoire » (systemd `oom-kill`) ; attendu, `ok`.
     - « tâches (32) » : aucun incident, `ok`. L'épreuve l'accepte. Le relevé du « REFUS » sans « LANCES » n'est pas porté par la sortie lue.
     - « temps de processus (5 s) » : incident « délai » (§ 8.3 ci-dessous), `ok`.
     - « durée murale (10 s) » : incident « délai » (systemd `timeout`, 10,009 s), `ok`.
     - **« sortie de lui-même en code 137, sans consommer la limite (5 s) » : `ok` faux**, écart « stdout sans « SORTIE 137 » ». Faits relevés :
       - code 137 ;
       - aucun incident ;
       - temps de processeur de l'unité 0,033 s ;
       - durée murale 0,101 s ;
       - systemd : `exit-code`, `status=137` ;
       - aucun relevé de mémoire (unité de 33 ms, sous la seconde du § 8.4).

       Les trois conditions de la lecture écrite du § 8.2 (code 137, aucun incident, temps de quelques dizaines de millisecondes) sont tenues. L'épreuve exige en plus que la sortie standard porte « SORTIE 137 », et elle ne la porte pas. **Cette sortie n'entre dans aucune lecture écrite : je la rapporte telle quelle, cause non établie** (préambule du § 8). La sortie standard elle-même n'est pas dans la pièce.
   - **Limites Lean (1), « mémoire d'un processus Lean (512M) »**, lu sur la seule compilation :
     - `temps.resultat` = `oom-kill` ;
     - `incident_compilation` = « mémoire » ;
     - `code_compilation` = 1, non nul ;
     - extrait de sortie vide, sans « ALLOUE ».

     **Conforme.** Relevés sans compter : `incident_noyau` nul ; vérificateur en `exit-code` 1 (1,624 s) ; `incident_bac` « mémoire ».
4. **`controles_hote`** : vide.
5. **Bloc `memoire`** : point 6 ci-dessous.

### 8.3 Cas « temps de processus (5 s) »

- Incident « délai » ; temps de processeur de l'unité 5,012 s, au moins 4,95 s.
- systemd : `exit-code` 137, durée de service 5,013 s.
- **Première lecture écrite : conforme.**

### 8.4 Mémoire (épreuve)

- **`chemin_cgroupe_faux`** : faux ; `lancements_sans_releve` vide.
- **Pics rapportés** (au moins trois relevés) pour 31 unités sur 36. Les 5 sans pic sont des unités Python ou de limites de moins d'une seconde.
- **Ordres de grandeur** :
  - compilations des gardes Lean : 659 à 675 millions d'octets (environ 630 à 645 Mio) ;
  - items d'isolement Lean : 60 à 76 millions d'octets ;
  - Python sain : 53 millions d'octets ;
  - limite mémoire Python : 466 millions d'octets ;
  - limite Lean : 54 millions d'octets.

  Aucune valeur n'est de l'ordre de quelques centaines de Kio pour un processus Lean avec Mathlib : rien ne dit que la mesure est encore fausse. Pour comparaison, le « Memory peak » de systemd vaut 336 Kio à 1,5 Mio sur les mêmes unités, ce que la correction B2 écarte justement.
- Aucun « conforme » ne dépend du pic.

### 8.5 Mesures (`mesures-v6.json`)

- **`suite`** (3 passages, `system.slice`) : les trois acceptent l'item sain, sans incident. Compilation environ 4,3 s de processeur, pic environ 669 millions d'octets ; vérificateur environ 7,0 à 7,1 s, pic environ 2,40 milliards d'octets (environ 2,24 Gio).
- **`parallele_3`** (3 passages, tranche réservée `bacmesure5931df57.slice`) : les trois acceptent l'item sain, sans incident. Pics de même ordre.
- **`memoire`** : chemin de cgroupe juste ; aucun lancement sans relevé.
- **`releve_machine`** :
  - période 0,1 s ;
  - `MemTotal` 32 857 440 256 octets ;
  - `MemAvailable` : 31 999 680 512 avant, 24 783 241 216 au plus bas, 31 518 314 496 après, sur 119 relevés ;
  - pic de la tranche 7 207 055 360 octets, sur 118 relevés.
- **`parallele_3_compte` : vrai. `parallele_3_motifs` : vide** (recopié tel quel : `[]`).
- **`parallele_3_calcul`** :
  - `baisse_dispo_octets` 7 216 439 296 ;
  - `dispo_min_prudente_octets` 24 783 241 216 ;
  - `seuil_pic_octets` 16 428 720 128 ;
  - `seuil_dispo_octets` 8 214 360 064.
- **Les sept critères tiennent** :
  1. trois acceptations sans incident ;
  2. chemin de cgroupe juste ;
  3. 118 relevés de la tranche ;
  4. 119 relevés de `MemAvailable`, avec `MemTotal` et `MemAvailable` lus avant ;
  5. pic de la tranche (7,21 G) sous la moitié de `MemTotal` (16,43 G) ;
  6. baisse (7,216 G) au plus pic + 1 Gio (8,28 G) ;
  7. disponible au plus bas, estimé prudemment (24,78 G), au moins le quart (8,21 G).
- **Lecture : la mémoire de la machine entière pour trois passages en parallèle est mesurée, et le passage en parallèle est compté.**

### 8.6 Sondes réseau

- `sonde-apres-coupure-v6.json` et `sonde-fin-v6.json` : attendu « fermée », **aucun écart**.
- La boucle locale (cas sain) est « ouverte » ; toutes les cibles extérieures sont « fermée » (TCP sans réponse, DNS en refus local `EPERM`, résolveur sans réponse).
- Les deux fichiers sont identiques octet pour octet (`d1d37254…`).

## 7. Verdict du poste (§ 8.6, une lecture, jamais un verdict de porte)

- **« noyau »** : conforme, 18 sur 18.
- **« épreuve »** : non conforme (code 1). Statut « non conforme ». Genres : gardes Lean, isolement Lean, Python et limites Lean conformes ; limites non conforme par **un seul cas**, « sortie de lui-même en code 137, sans consommer la limite (5 s) », sur l'écart « stdout sans « SORTIE 137 » ». Cause non établie ; aucune lecture inventée ; aucun reclassement.
- **« mesures »** : passage en parallèle compté ; les sept critères tiennent.
- **Ce qui reste non éprouvé ou non lisible** :
  - la cause de l'absence de « SORTIE 137 » sur la sortie standard du cas 137, dont la sortie standard n'est pas versée par l'épreuve ;
  - le motif du refus de `reseau-python-tcp`, coupé par la borne de 160 caractères ;
  - le « REFUS » sans « LANCES » du cas « tâches (32) », non porté par la sortie lue.
- **Ce qui est éprouvé au quatrième essai et ne l'était pas au troisième** :
  - les cinq sondes v3 rendent leurs tentatives sous `bwrap` et l'utilisateur `bac` ;
  - le classement « délai » par le temps de l'unité ;
  - le classement « mémoire » d'un processus Lean par `oom-kill` ;
  - le chemin du cgroupe des unités et de la tranche réservée sous Ubuntu 24.04 et systemd 255 ;
  - le pic échantillonné ;
  - la mémoire de la machine entière.

## 8. Valeurs des pièces

- **`VERSION-LEAN`** : Lean 4.35.0, `x86_64-unknown-linux-gnu`, commit `eb6cafb7290e8bd5f2937522d8d804f58f02bafc`, Release ; toolchain `leanprover/lean4:v4.35.0` ; elan 4.4.0.
- **`COMMIT-MATHLIB`** : `56a005855ea17e0b0958f73ec801ae140b0a1679`.
- **`MACHINE`** : Hetzner `ccx33`, `hel1`, serveur 177109613 ; Ubuntu 24.04.4 LTS, noyau 6.8.0-137-generic, 8 cœurs, 32 857 440 256 octets, systemd 255.4-1ubuntu8.16 ; Python du bras S 3.12.3.
- **`ESSAIS-R5`**, partie machine :
  - lecture par `bac` conforme ;
  - compilation du vérificateur conforme ;
  - pas `noyau` 18 sur 18 ;
  - épreuve non conforme, 35 cas sur 36 ;
  - mesures : parallèle compté.

**Empreintes des pièces versées** (manifeste `da2044df…`) :

| Pièce | sha256 |
|---|---|
| `coupure-v6.txt` | `8bfe729f…` |
| `epreuve-code-v6.txt` | `22c04673…` |
| `epreuve-isolement-v6.json` | `7abdc0c3…` |
| `installation-v6.txt` | `9fe3b8ed…` |
| `mesures-v6.json` | `59a0d783…` |
| `premier-pas-noyau-v6.json` | `845c6bdc…` |
| `sonde-apres-coupure-v6.json` et `sonde-fin-v6.json` | `d1d37254…` |
| `verificateur-epingle-v6.json` | `25bf1cdb…` |
| `pilote-apres-v1.log` | `c651a7b1…` |
| `pilote-avant-v1-adresse-serveur-masquee.log` | `d150b53b…` |

## 9. Incidents et écarts

1. **Lecture des deux pièces de lancement par l'interface GitHub** (`gh api`, lecture seule), avant le clone. Le `git fetch` d'un ancien clone Windows pendait : il a été arrêté par son identifiant de tâche, n'a rien modifié, et ce clone n'a pas été repris. Accepté par la mère.
2. **`git ls-remote` en lecture sur `-v5`**, hors de la liste de la règle 4 : il rend `47c7faaf`. Accepté par la mère.
3. **Deux dossiers neufs hors du clone** pour les `sha256sum -c` de la consigne et des documents de lancement de `main`. Accepté par la mère.
4. **Canal des messages** : échecs de l'envoi direct, repli déclenché, puis canal par la branche accepté par écrit par la mère (§ 4).
5. **Adresse du poste lue par la session** (écart 2 du rapport v3, accepté d'avance par la consigne v8).
6. **Copie versée masquée** (écart 6 du rapport v3) : `pilote-avant-v1.log` portait l'adresse du serveur une fois ; sa copie versée la masque. Empreinte de l'original, gardé sur le poste : `8ef0247b315fa02d0fccfd9c5157b1c5cb840341707782f976e6869786a7d20e` ; de la copie : `d150b53bf09f9cef46298ec508d7ede06d93a78bc4acf140114ea03c18120a85`. Aucune autre pièce ne porte l'adresse du serveur.
7. **Premier manifeste des pièces fautif** (`…-v1.sha256`, chemins faux, ne passe pas `sha256sum -c`) : ni versé ni supprimé ; remplacé par le `-v2`.
8. **Commandes lancées depuis l'hôte Windows** par `wsl.exe -e`, depuis la racine du clone, les processus détachés vivant dans Ubuntu (écart 8 du rapport v3). Clés de modèle `KIMI_API_KEY` et `GEMINI_API_KEY_2` (noms lus dans `WSLENV`) retirées par `env -u NOM <commande>`. Jeton de `gh` passé au seul processus `git` par l'environnement, jamais écrit ni affiché.
9. **Clé d'hôte déjà connue** (adresse du serveur réattribuée) : `ssh-keygen -R`, comme le prévoit la procédure.
10. **Coupure en « pending » à la première lecture** : seconde lecture seule à une minute, conforme (écart accepté de la v12).
11. **Dernière ligne du pilote « apres »**, qui nomme `minuterie_v6 detruire` : texte hérité. La destruction s'est faite par la minuterie v7.
12. **Aucun refus** d'un contrôle de permissions ni d'un classifieur ; aucune relance du pilote ni d'aucune étape ; aucune commande à la main sur la machine.

## 10. Lignes proposées pour les registres

**`registres/depenses.md`** :

| 2026-11-21 | GO-2026-11-10-13 | Hetzner ccx33 hel1, serveur 177109613, essai Lean D-1a, quatrième essai (outillage) | 2026-11-21T18:53:18Z → 19:11:58Z, 1 h facturée | ≈ 0,28 USD ; cumul de la ligne ≈ 1,12 USD | poste local, branche donnees/lean-outillage-d1a-poste-local-v6, rapport v4 |

**`registres/arrets.md`** :

| 2026-11-21 | serveur Hetzner 177109613 « lean-outillage-d1a-fae70647f54e » (essai Lean D-1a, quatrième essai) | détruit par son identifiant à 19:11:58Z par le poste local (fin normale, section 5) ; clé 132916986 et pare-feu 12126345 supprimés ; minuterie 9268 arrêtée par son PID ; inventaire final vide à 19:12:24Z ; absence relue par le jeton de la mère à 19:15:31Z (404, aucun serveur, aucune clé ni pare-feu sous l'étiquette) ; tâches T1 à T3 laissées actives comme filets | poste local, relu par la mère |
