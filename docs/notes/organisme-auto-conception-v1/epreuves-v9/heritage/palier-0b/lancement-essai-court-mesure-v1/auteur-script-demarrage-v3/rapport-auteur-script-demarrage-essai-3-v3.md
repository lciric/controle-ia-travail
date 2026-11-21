# Rapport de l'auteur — script de démarrage de l'essai 3 (palier 0b) — v3

Pièce de travail (classe C), écrite le 2026-11-21 vers 22:40Z par l'auteur des v1 et v2 (modèle O). Elle porte les six corrections décidées par la mère à 21:43Z, sur la contre-lecture S de la v2. Cette contre-lecture a été récupérée : `…/contre-lecture-script-demarrage-v2-recuperee/releve-contre-lecture-script-demarrage-v2-interrompue-v1.md`, `f17ff011…2cee`, verdict provisoire « À corriger ». Les v1 et v2 restent intactes.

Règles tenues pendant la session :
- aucune machine créée, aucun appel à Hetzner ni à GitHub, aucun jeton réel lu ;
- aucun environnement du conteneur affiché ni listé : l'espion git du point 1 ne lit que deux variables nommées ;
- aucun `sleep` isolé : toutes les attentes sont des boucles de sondage sur un fichier ;
- aucune dépense, aucun commit, aucune poussée ;
- seuls mes serveurs factices ont été arrêtés, chacun par son identifiant ; aucun processus factice ne restait vivant à la fin ;
- aucune coupure ni aucun refus n'est survenu.

## Écart principal, à trancher : le script de démarrage voyage désormais dans la charge, derrière une amorce

Avec les corrections 2 à 5, le script en clair ne tenait plus sous 32 Kio. Mesuré par `tailles-json.py` sur `v3/essais/travail/fabricant/mesure-a.sans-jeton`, en JSON échappé en ASCII avec un jeton de 100 signes :
- **33 688 octets, soit −920** ;
- −363 même en octets bruts.

J'ai donc mis le script de démarrage v3 dans la charge, avec les quatre pièces, qui restent dans les données de démarrage comme la mère l'a décidé. Une **amorce** de 821 octets, en clair, fait le reste (`amorce-demarrage-essai-3-v3.sh`) :
- elle extrait la charge (`tar.gz` en base64) ;
- elle contrôle l'empreinte du script contre `E_SCRIPT`, que le fabricant écrit dans les données ;
- elle refuse en code 18 si la charge est illisible ou si le script a une autre empreinte, et en code 20 si la charge est déjà présente ;
- puis elle lit le script, qui garde `H0_PREVU` et le jeton sans les exporter.

La charge passe de `xz` à `gzip -9 -n` : l'amorce extrait la charge avant l'installation des paquets, et gzip fait partie des paquets essentiels de debian, ce que `xz` n'est pas forcément (supposé, voir réserves).

Le texte en clair contrôlé par la machine est donc :
- l'amorce ;
- l'empreinte du script, inscrite dans les données ;
- le script, qui ne se lit plus dans les données de démarrage mais dans la charge, et dont le fabricant donne l'empreinte.

Si la mère refuse ce changement, l'autre voie est de retirer des fonctions : par exemple les versements plafonnés, ou l'attente de 300 s.

## Fichiers et empreintes (dossier `v3/`, compagnon `.sha256` à côté de chacun)

| Pièce | Taille | sha256 |
|---|---|---|
| `demarrage-machine-essai-3-v3.sh` | 12 163 octets | `9beb07052a5add7e7381b47f89aa5216a80130b5d8132b3c4fa96bf2a43b7588` |
| `amorce-demarrage-essai-3-v3.sh` | 821 octets | `1ddd658975e50877fd68e52299a58a44f2ffaba33bb159a57a93736c5344e4b7` |
| `fabriquer-donnees-demarrage-v3.sh` | — | `4f47514a82eb9fedfa87f81980f7a5199e25fe2bc6c6f5e0abe6e2c441d660d2` |

- **Banc `v3/essais/outils/`**. Il contient notamment :
  - le **faux `setsid`** `chemin-setsid/setsid`, désormais livré (point 6), avec les modes enfant, tardif, mort, sorties, tue, tue-tard et gardien-bloque ;
  - l'espion git `espion/git` et le cas `q1-j-exporte.sh` ;
  - le lot `lot-v3.sh`.
- **Résultats bruts** : `v3/essais/travail/lot-v3.txt`, les `cas/*/resume.txt`, `q1-j/resume.txt`, `fabricant-essais/table.txt`, et `cas/s1-sain/journaux/{garde-branche,assistant,controle-argv}.txt`.

## Marge de taille

Données saines v3, avec un jeton factice de 44 signes : 30 354 octets.

| Lecture (jeton de 100 signes) | Taille | Marge |
|---|---|---|
| **Chaîne JSON échappée en ASCII, guillemets compris (seuil du fabricant)** | **30 443** | **2 325** |
| Octets bruts | 30 410 | 2 358 |
| Échappement HTML de Go | 30 468 | 2 300 |
| Avec `/` échappé | 30 943 | 1 825 |

Le calcul du fabricant (en bash) et celui de `tailles-json.py` donnent les mêmes nombres. La lecture « Go » repasse donc au-dessus de zéro.

**Correction du chiffre de la v2 (point 6).** Les octets bruts de la v2, avec un jeton de 100 signes, font **31 958, pour une marge de 810**, et non 32 140 et 628. J'avais repris la mesure d'une version intermédiaire (`mesure-c`). Le chiffre juste se lit sur `v2/essais/travail/fabricant/mesure-d.sans-jeton`.

## Les six corrections

1. **`declare +x J`** en tête du fabricant : même si la session exporte `J`, aucun enfant n'en hérite. Cas `q1-j` refait, avec un espion git qui ne lit que `J` et la variable nommée, jamais l'environnement :

   | Cas | Appels de git dont `J` porte le jeton |
   |---|---|
   | Témoin, v3 sans `J` | 0 sur 2 |
   | **Objet vrai, fabricant v2 avec `J` exporté** | **2 sur 2** (la fuite est vue) |
   | **v3 avec `J` exporté** | **0 sur 2** |

   Aucun jeton dans les sorties.
2. **Contrôle du `.git` refait juste avant `demarrer`** (code 56), en plus des pas (c) (code 51) et (f) (code 55).
   - Artefact `p2` : un `.git` est posé pendant le contrôle seul des paramètres du gardien, qui est le dernier pas avant `demarrer` ; le script rend 56 et rien ne part.
   - Cas sain : s1.
3. **Code 5 du départ.** Le script lit l'identité sur le programme lui-même : il doit être vivant et chef de son groupe ; le groupe et l'heure de départ sont lus dans `/proc/PID/stat`. Il les écrit alors dans `pgid-essai-3.txt` et `depart-processus-essai-3.txt`, et garde ce qu'avait écrit le départ sous `*-ecrit-par-le-depart.txt`. Le gardien s'attache ainsi à cette identité. Sinon, il arrête le programme par identifiant et sort en code 86, échec écrit et poussé.
   - **Cas sain `p3`** (faux `setsid` « tardif ») : départ 5, identité confirmée (« groupe 19053, départ 2397177 »). Le gardien écrit « identité confirmée », et à l'heure d'arrêt de durée, ramenée pour le banc à +170 s, il **envoie le signal de fin au groupe**. Tous les membres sont absents 0,2 s après, et le code de sortie est 143. L'arrêt de 94 h arrête donc bien le programme dans ce cas.
   - **Artefact `q6-enfant`** (cas du contre-lecteur) : départ 5, le programme n'est pas chef de son groupe → code 86. Le programme est arrêté par identifiant (4 processus, aucun forcé), l'échec est poussé, et aucun processus ne reste.
   - **`q6-mort`** : code 85.
4. **Lanceur tué sans écrire son code** : c'est un échec, jamais un code 0.
   - Tué pendant l'attente (`p4`, mode « tue ») : code 87, échec écrit et poussé.
   - Tué après l'attente (`p4`, mode « tue-tard ») : le script a fini en 0, mais la boucle, en constatant la fin, écrit « code 87 : lanceur arrete sans ecrire son code ». Cet échec figure dans l'état versé.
5. **Échec 84** (gardien refusé, artefact `p5` : départ du gardien bloqué, code 4). Le programme lancé est arrêté par identifiant (3 processus) **avant** le versement de l'échec ; code de sortie 143, aucun processus restant.
6. **Faux `setsid` livré** et chiffre corrigé (ci-dessus).

Ce qui est fait en plus : l'environnement des deux départs est nettoyé (`env -u` des quatre réglages de git et d'apt). Le faux programme, qui ne lit que ces quatre variables nommées, n'en hérite d'aucune. C'était la réserve de la v2, et la place gagnée la permet.

## Table des essais (banc rejoué en entier ; racines et clones retirés après chaque cas)

**Lot `lot-v3.txt` : 40 cas, 40 tenus ; s1-sain est joué à part.** Dans tous les cas, le jeton factice est absent des fichiers, de l'histoire versée et de `ps`, sauf dans le témoin, qui doit le montrer.

| Cas | Attendu | Rendu |
|---|---|---|
| s1-sain | 0 | 0 ; arguments égaux au complément ; branche de 3 commits |
| q2, portes d'essai sans banc | 19 | 19 |
| q3, `H0_PREVU` vieux de 3 h ; q3, `H0_PREVU` dans 1 h | 21 ; 21 | 21 ; 21 |
| z1, jeton vide ; z2, `@JETON@` ; z3, `H0_PREVU` mal formé ; z4, second démarrage | 22 ; 22 ; 21 ; 20 | idem |
| a1, apt en échec ; q5, assistant de production, sans réseau | 30 ; 30 | idem |
| b1, jeton refusé ; b2, commit absent | 41 ; 41 | idem |
| **e3, script altéré dans la charge** | **18 (amorce)** | **18** |
| t1, témoin de fuite | 99, jeton trouvé | 99 ; 2 fichiers, `ps` 42 lignes |
| **Table de racines altérées du contre-lecteur** (`cl-q3`, faux pip) : fichier, lien, modification, suppression | 81 | 81 |
| idem : `.git` en fichier, sous-`.git`, `.git` vide, `.git` valide (tête au commit) | 55 | 55 |
| idem : dossier vide, `chmod` | 0 (non vus, limite connue) | 0 |
| **p2, `.git` avant `demarrer`** | **56** | **56** |
| **q6-enfant** | **86**, programme arrêté | **86**, 0 restant |
| **q6-mort** | **85** | **85** |
| **p3, code 5, identité confirmée** | **0**, arrêt de durée avec signal | **0** ; signal au groupe ; 143 |
| **p4, tué pendant l'attente** | **87** | **87** |
| **p4, tué après l'attente** | 0, échec 87 versé | 0, échec 87 versé |
| **p5, gardien refusé** | **84**, programme arrêté | **84** ; 143 ; 0 restant |
| cl-q5, le lanceur refuse au vrai départ | 85 | 85 |
| c1 ; c2 ; c3 ; d1 ; e1 ; e2 ; f1 ; f2 | 50 ; 51 ; 53 ; 61 ; 72 ; 71 ; 81 ; 82 | idem |
| v1, arrêt de place et plafond | 0 | 0 ; 1 048 576 octets versés ; `arret-gardien.txt` versé ; aucun réglage hérité |

Autres essais sur s1 :
- garde de branche : 7 refus avec le message de la garde, distant inchangé, la poussée descendante admise ;
- assistant (factice) : jeton à l'hôte permis seul, rien aux 6 autres demandes ; même résultat pour l'assistant de production `https://github.com` ;
- `--no-verify` : 0 occurrence dans le script et dans l'amorce.

**Fabricant v3** (`table.txt`) : 21 cas, 21 tenus.
- Refus : codes 3 (×5), 4 (×3), 5 (×4), 6, 8 (×2), 2.
- Sains : F11, F12, F20 (jeton de 100 signes) et F15. F15 porte un signe non ASCII dans le script : désormais comprimé, il ne gêne plus.
- Trop grand : 36 751 octets en lecture stricte, script gonflé de remplissage aléatoire.
- Branche présente sur un dépôt factice : 8.

**Dénominateur.**
- Le compteur « restants » rend 1 dans p2 et f1. Ce n'est pas un processus du cas : c'est le joueur de cas lui-même, dont un argument contient le chemin du cas ; je l'ai vu dans `processus-restants.txt`. Les autres cas rendent 0.
- La garde de branche a été jouée une fois en v3, avec un outil où il restait un nom de fichier v2. Seule la ligne de comptage de `--no-verify` était touchée ; elle a été refaite à la main (0) et l'outil corrigé.

Non joués :
- codes 60, 62, 83 et 70 ;
- intervalle de 1 800 s ;
- chemin de production par défaut ;
- cloud-init.

## Écarts

1. **Amorce et script dans la charge** (section en tête), avec **gzip au lieu de xz**.
2. Nouveaux codes :
   - 18 : amorce, charge ou empreinte du script ;
   - 56 : `.git` juste avant `demarrer` ;
   - 86 : code 5 et identité non confirmée ;
   - 87 : lanceur tué sans code.
3. **Au code 5, le script réécrit `pgid-essai-3.txt` et `depart-processus-essai-3.txt`** avec l'identité lue sur le programme, et garde les fichiers d'origine. C'est le seul cas où le script écrase un fichier du départ v4.
4. **L'arrêt par identifiant** (84, 85, 86, 87) vise le processus écrit dans `pid-essai-3.txt` et ses descendants, trouvés par la chaîne des parents dans `/proc`. Il envoie le signal de fin, attend au plus 30 s, puis force l'arrêt. L'heure de départ des descendants n'est pas comparée : l'instantané et le signal se suivent immédiatement (réserve).
5. **Le dépôt factice partagé de 2,1 Go a été retiré à la fin** pour la place. Les dépôts distants des cas, qui en partageaient les objets, ne sont plus lisibles ; leurs résumés restent.

## Réserves et ce qui reste à trancher

1. **Accepter l'amorce** (écart 1). Elle redonne 2 325 octets de marge, et une marge positive aussi en lecture Go.
2. **gzip présent sur l'image debian-13 de Hetzner avant toute installation** : supposé, parce qu'il est essentiel dans debian. Il est à vérifier sur l'image, ce qui demande une machine (dépense).
3. **La façon dont Hetzner compte les 32 Kio** : toujours le premier pas non justifié, moins pressant avec 2 325 octets de marge.
4. Le jeton (inchangé) : 100 signes au plus, jeton à grain fin, révoqué après la destruction.
5. La vérification de la branche se joue dans la session, sur le vrai dépôt, à la fabrication.
6. La contre-lecture S de la v3 doit porter sur trois choses :
   - l'amorce ;
   - le réécrit des fichiers d'identité au code 5 ;
   - l'arrêt par identifiant.

   Le fabricant se joue ensuite avec `9beb0705…` en troisième paramètre.
7. La voie qui fait foi pour la création, la lecture de H0 et la destruction (inchangé).

## Relevé de méthode

**Chaîne de raisonnement.**
1. Six corrections, prises dans la décision de la mère et dans le relevé `f17ff011…`.
2. Avec ces corrections, le script en clair fait −920 octets en JSON ASCII (`mesure-a`). D'où l'amorce. La v3 fait +2 325 (`ud-sain.empreintes.txt` et `tailles-json.py`, égaux).
3. Chaque correction a un cas sain et un artefact dans le lot, et la fuite de `J` a été vue sur l'objet vrai (fabricant v2).
4. L'arrêt de 94 h arrête le programme au code 5 confirmé : vu dans p3, sur une heure ramenée.
5. gzip est présent sur l'image debian avant apt : **supposé**.
6. Hetzner compte au plus la chaîne JSON échappée en ASCII : **supposé**.
7. Cloud-init, apt, pip et GitHub se conduisent comme les factices : **supposé**.

**Objets de contrôle.**

| Mécanisme | Faux par construction | Vrai par construction |
|---|---|---|
| Espion `J` | fabricant v2 avec `J` exporté : prédit fuite, rendu 2 sur 2 | v3 avec `J` exporté, et témoin sans `J` : 0 |
| Contrôle `.git` | `.git` posé juste avant `demarrer` (56), et quatre formes de `.git` (55) | s1 |
| Identité au code 5 | enfant, non chef de son groupe : 86 | tardif : confirmé, signal envoyé |
| Lanceur sans code | tué pendant l'attente, et après : 87 | s1 : code écrit, 0 |
| Échec 84 | départ du gardien bloqué : programme arrêté | s1 |
| Taille | script gonflé (F10) | F11, F12, F20 |
| Recherches du jeton | — | témoin t1 : trouvé |

**Premier pas non justifié.** Pas 5 : gzip sur l'image avant apt. Une machine d'essai sur devis, ou la liste des paquets de l'image publiée par Hetzner, le justifierait.

**Mode d'échec affecté.** Sans objet : je suis auteur.

**Dérivation de l'énoncé seul.** Sans objet : je ne suis pas agent de re-dérivation.

**Trouvaille de côté.** Le compteur de processus restants du banc se compte lui-même quand un argument porte le chemin du cas. C'est un défaut de l'instrument, non du script ; il faudrait exclure le joueur par son identifiant.

**Évaluateur et conseil.**
- **Qui juge.** Mon banc juge le produit, puis le lecteur S. Le banc a été admis sur le témoin t1, sur l'objet vrai du point 1 et sur les artefacts.
- **Bon jugement sans le mériter.** C'est possible :
  - factices, HTTP local ;
  - pas de cloud-init, pas de vrai apt ;
  - heure d'arrêt ramenée à +170 s dans p3 ;
  - artefacts choisis par moi.
- **Conseil au lecteur.** Viser :
  - l'amorce : `BASH_SOURCE`, lecture en `.`, code 18 ;
  - la fenêtre entre la lecture de l'identité et la prise de garde ;
  - l'arrêt par identifiant face à la réutilisation des identifiants.
