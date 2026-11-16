# Vérification courte de la procédure pas à pas du pilote MR-2 sur la machine jetable — v7 (passage v6 → v7) — v1

- **Lecteur** : instance neuve, qui n'a écrit aucune version de la procédure, aucune de ses contre-lectures, ni la vérification de la
  v6. Ce rapport n'écrit aucun nom de modèle.
- **Pièce vérifiée** : `procedure-pilote-mr2-v74-machine-v7.md`, empreinte
  `be688ec1eab8a91de7b12088f3e1f887f52ea9dac0fc7225c53371832e540c5d`, égale à son compagnon et à l'empreinte attendue. Comparée à la v6
  (`6eb3a1cf273e6c132b903132921f04d4c72a09650496ba7e9cf1c1ae1d5343ff`, égale à son compagnon). Liste des corrections attendues : la
  vérification de la v6 (`e5dd91242eaded4af2918c5b2ed2c7ba448ffb33db7cb98a6cb6392786ea65b2`, égale à son compagnon, lue dans le dépôt
  de travail).
- **Copie** : `/home/user/verif-pilote-v7`, tête détachée `549ce697`, arbre propre avant écriture.
- **Fin** : 2026-11-15T07:49:39Z (sortie de `date -u` de la dernière commande avant l'écriture de ce fichier).
- **Aucune commande de la procédure n'a été jouée contre un service** : aucun appel au loueur, aucune machine, aucun modèle, aucune
  clé lue, ni `env` ni `printenv`.

## Verdict : jouable après corrections

0 bloquant, **2 majeurs**, 9 mineurs.

Le différentiel est presque entièrement déclaré, les sections dites inchangées le sont, et les deux majeurs de la v6 sont **fermés
sur le fond**. Mais deux défauts neufs sont entrés avec la v7, tous deux dans la section 9 :

- **MA** : la ligne de lancement détaché a reçu une garde `test ! -e … &&` devant `setsid nohup … &`. Sous cette forme, la commande
  `ssh` ne rend pas la main avant la fin du processus détaché (jusqu'à 12 h pour `jouer`), et « lancé » s'affiche même quand rien
  n'est lancé. Éprouvé ici sur une commande factice. Changement **non déclaré**, à la commande la plus sensible de la procédure.
- **MB** : la relance « toujours sous `reel-2` » fait « rejouer TOUS les contrôles juste avant », dont `test ! -e /root/pilote/reel`,
  qui échoue justement dans le cas où `reel/` a été créé au premier essai ; la consigne voisine dit alors « arrêt (A) si un dossier
  existe ». La relance promise devient impossible à la lettre dans ce cas.

Chacun se corrige par une ligne. Aucun des deux ne fait dépenser plus que prévu par lui-même ; MA peut mener, par une seconde
frappe de l'exécutant, à l'accident que le majeur N1 de la v5 voulait écarter (voir MA).

## Limites

- Texte scellé non lu (autre branche, interdite à ce lecteur).
- Outil du loueur : lu **dans son code installé**, sans l'exécuter (`/home/user/vastai-env/lib/python3.13/site-packages/vastai/`,
  version 1.8.3 d'après ses métadonnées).
- Code du lanceur : lu dans le paquet de la copie (`e3d83e47a06b2941c54240b96612cb17880fe4162e7822a2eb02ebac64c785b1`), dépaqueté
  hors de tout dépôt, tête `605e0f60f3eed0948948e6a4eb15cb73de1d03de`.
- Essais de forme, sur données factices seulement, dans le dossier temporaire de la session : le lancement détaché avec `sleep` à la
  place du pilote ; le rendu du script modèle avec des empreintes factices ; les programmes de preuve de la section 11 sur des
  listes factices. Seule exécution sur une pièce vraie : le lecteur gelé des lignes de la section 1, en lecture seule, sous
  `env -i`, sur une copie de `registres/go.md` de `main` (aucun appel, aucune clé).
- Non vérifiables ici : l'image `python:3.13-bookworm` chez le loueur (présence de git, de `setsid`, de `shred`, service de copie de
  fichiers par ssh), l'existence de numpy 2.5.3, la clé ssh du compte.
- Aucun refus d'outil, de crochet ni de classifieur rencontré.

## 1. Différentiel exact v6 → v7

`diff` des deux fichiers : 33 blocs. Bornes des sections de la v6 comparées aux blocs : **aucun bloc ne tombe dans les sections 4, 5,
7, 8, 12, 13, 12 bis, 12 ter** (lignes 121-158, 174-195, 328-397 de la v6) : elles sont inchangées, comme déclaré.

| lignes de la v7 | changement | point déclaré |
|---|---|---|
| 1 | titre « v7 » | version (R12) |
| 5-17 | versions, « remplace la v6 pour l'usage », outil 1.8.3 | m5, écart de version |
| 32-48 | préambule de chaque commande, `variables.sh`, « 14 h », `ID` défini une seule fois, notation ssh | m11, m5, m13 |
| 62-64 | codes 1 et 2 de l'interprète | M2 |
| 66-76 | (A) exclu entre `jouer` réussi et mesure faite ; effacement des clés avant le nœud du point (6) | M2, m9 |
| 78-81 | heure limite | m8 |
| 86 | `W` et `ENV` posés en tête de la section 1 | m11 |
| 99-120 | attendus resserrés ; contrôles des noms de clés et des lignes avant la location | m6 |
| 124-163 | `GO_ID=` sur la création et l'aide ; solde par programme ; étiquette ; image nommée ; `heure-limite.txt` ; repli écrit | m2, m12, m11, m7, m8, m3 |
| 167-193 | `ssh_config` ; contrôle dans le chemin réduit ; `scp -F` | m13, m7 |
| 233-259 | script détaché de `generer` ; `H` et `S1` à `S4` tirés par programme | m10, m11 |
| 288-290 | garde des variables ; `reel-2` absent ; numpy sous le chemin réduit | m11, M1, m7 |
| 306-318 | texte des contrôles et des clés resserré ; « risque résiduel **accepté** par la mère » | m6 pour le renvoi ; **le mot « accepté » n'est pas déclaré** (a4) |
| 320-333 | script modèle à marques ; **garde `test ! -e … &&` devant le lancement** | m1 ; **la garde n'est pas déclarée** (MA) |
| 335-365 | suivi ; issues de `jouer` ; relance toujours sous `reel-2`, en commandes ; tout autre code | M1, M2, m1 |
| 367-402 | script détaché de `mesurer` ; codes de `mesurer` ; `lire` non nul → nœud | m10, M2 |
| 407-421 | `ssh -F`, `scp -F`, `$REEL`, contrôle par le compagnon, `REEL/prive/` | m13, m14, m5 |
| 423-441 | destruction enchaînée, programmes « avant » et « après », témoin | m3, m4 |
| 514-543 | section 12 quater | déclaré |

**Changements non déclarés** (aucun ne touche les sections dites inchangées) :

1. la garde `test ! -e /root/pilote/code-… &&` ajoutée devant les trois lancements détachés (l. 244, 332, 355, 379) : **MA** ;
2. le nœud « à 2,70 USD dépensés sur la machine » (v6 l. 93-94) a disparu (a4) ;
3. « aucun arrêt du processus sans elle, et alors par son PID (R10) » (v6 l. 258-259) a disparu (a4) ;
4. « risque résiduel à trancher par la mère » est devenu « accepté par la mère » (l. 318), sans référence (a4) ;
5. le témoin de l'inventaire d'avant (« la liste doit montrer les instances intouchables qui existent », v6 l. 87-88) a disparu ;
   l'étape reste titrée « avec témoin » (a4).

## 2. Les deux majeurs de la v6

### M1 de la v6 (relance toujours sous `reel-2`) : fermé sur les noms ; un défaut neuf dans les contrôles (MB)

- **Refus avant la création de `reel/`** (gardes du mode réel, préparation des mondes, erreur d'usage de l'interprète) : le premier
  script a écrit `journal-09-reel.txt` et `code-09-reel.txt` (2) et effacé les clés ; `lancements.jsonl` absent. La relance (l. 351-356)
  renomme les deux pièces, exige `reel-2` et le registre absents, rejoue les contrôles (ils passent : ni `reel` ni `reel-2`), renvoie
  les clés, rend `lancer-reel-2.sh` depuis le modèle (éprouvé ici : 0 marque, `bash -n` juste, `--sortie /root/pilote/reel-2`,
  `journal-09-reel-2.txt`, `code-09-reel-2.txt`), lance, suit `code-09-reel-2.txt` avec « clés effacées ». La consigne contraire de
  la v6 (« garde `reel` ») n'existe plus (l. 346-348). **Chemin cohérent.**
- **Refus après la création de `reel/`**, registre des lancements absent : mêmes commandes, mêmes noms en `-2`. Mais le commentaire
  de la l. 353 fait rejouer **tous** les contrôles « juste avant », dont la l. 289, qui exige `reel` absent : elle n'imprime pas
  « absents », et la l. 306 dit « arrêt (A) si un dossier existe ». **MB.**
- Après la relance, `REEL=reel-2` est écrit dans `variables.sh` (l. 359) et repris par les sections 10 et 11 ; un second code 2 mène
  à (A) (l. 360).

### M2 de la v6 (conduite entre un `jouer` réussi et la mesure faite) : fermé

- (A) est exclu de cet intervalle dans sa définition même (l. 66-67).
- `mesurer`, code 2 (les cinq refus du lanceur, tous levés avant le programme de mesure, l. 558-569 du lanceur), code 1 (erreur non
  rattrapée, par exemple manifeste absent) : cause écrite, absence de `sortie-mesure*` et de `mesure-pilote-v70*` constatée, nœud à
  la mère, machine gardée, ni relance ni (A) sans son mot (l. 386-389). Code 3 : (A) (l. 385). Conforme à la correction 1.
- `mesurer`, code 97 : **inatteignable** tel que le script est écrit (a1) ; sans dommage, mais le suivi reste « en cours ».
- `jouer` hors 0, 2, 3, ou muet : aucune relance ; registre des lancements présent ou illisible → (A) ; absent → nœud à la mère,
  machine gardée (l. 363-365). Conforme à la correction 2. La commande qui constate la présence du registre n'est pas écrite (a7).
- `lire` non nul : nœud à la mère, machine gardée (l. 398-399), au lieu de l'arrêt (A) de la v6 : déclaré.
- Borne : « au plus jusqu'à l'heure limite » ; à l'heure limite sans mot de la mère et sans processus, (A) (l. 78-80). La mère doit
  donc répondre avant ; le nœud d'une heure avant l'y invite.

## 3. Les quatorze mineurs de la v6

| mineur | porté | où (v7) | reste |
|---|---|---|---|
| m1 relance en commandes | oui | 351-360 | MB ; MA |
| m2 `GO_ID=` sur la création et l'aide | oui | 124-126, 142 | — |
| m3 preuves par programme | oui | 153-154, 428-433 | point 6 de la section 2 (a3) |
| m4 garde de l'identifiant | oui | 426-430 | — |
| m5 restes de la v5 | oui | 7, 43-46, 418-419 | — |
| m6 clés et lignes avant la location | oui | 105-119 | lecteur gelé rejoué ici : « lues au montant exact », code 0 |
| m7 chemin réduit, image nommée | oui | 136, 187, 290 | image non vérifiable ici |
| m8 heure limite | oui | 78-81, 143 | nœud à 2,70 USD retiré sans le dire (a4) |
| m9 clés pendant le point (6) | oui | 71-73 | même souci hors du point (6) (a7) |
| m10 scripts détachés | oui | 238-245, 372-380 | a1 ; MA |
| m11 variables de la session | oui | 36, 41-42, 135, 254-255, 288 | `REEL` et `ETIQ` non gardés (a2) |
| m12 solde | oui | 127-131 | champ tranché ci-dessous : `credit` |
| m13 ssh | en partie | 47-48, 167-182 | le programme qui tire l'adresse et le port n'est pas écrit (a5) |
| m14 contrôle par le compagnon | oui | 414 | — |

Aucun mineur n'est dit « non porté ».

## 4. Régressions : argent, arrêt, clés

- **Lignes et montants** : inchangés (20 et 21,72 USD ; parts 12, 8, 9,36, 9,36 ; machine 3 USD ; prix total au plus 0,20 USD par
  heure ; pire cas 14 h, soit 2,80 USD). Lus par le lecteur gelé sur la copie de `main` : conformes.
- **Plafonds des fournisseurs** : mécaniques, inchangés (l. 338-339).
- **Heure limite** : désormais écrite dans un fichier (l. 143) et dotée d'une conduite (l. 78-81) : mieux qu'en v6. Le nœud à
  2,70 USD a disparu (a4) ; à 0,20 USD par heure il tombait après le nœud « une heure avant », donc sans perte de garde.
- **`GO_ID=`** : la seule ligne de création (l. 142) commence par `GO_ID=GO-2026-11-14-14` ; l'aide, si elle est lue, « sous le même
  préfixe » (l. 125-126). Le crochet (empreinte `73be0638…`, égale dans la copie et dans le dépôt de travail) cherche l'identifiant
  n'importe où dans la commande : le préambule placé devant ne gêne pas.
- **Arrêt et destruction** : par identifiant relu de `identifiant.txt`, exigé entier, étiquette comparée par programme juste devant
  `destroy`, `-y` ; preuve d'absence par la liste relue et témoin (« toute autre instance listée avant l'est encore après »), témoin
  vide dit ; jamais par le code de sortie (dans le code 1.8.3, `destroy instance` rend 0 même en échec : la règle est juste). Éprouvé
  ici sur listes factices : absent avec un témoin ; témoin vide rend « 0 » ; identifiant encore listé rend une erreur. Aucune
  seconde création avant la preuve (l. 161, 441). Les sept identifiants intouchables n'apparaissent qu'à l'en-tête.
- **Clés** : aucune valeur en argument ni à l'écran (`printf` interne vers l'entrée de ssh ; `${NOM:?}` n'affiche que le nom) ;
  `variables.sh` ne reçoit aucune clé ; le programme du solde n'affiche que le solde, et une erreur n'y affiche que le nom du champ.
  Reste a7.
- **R10** : la phrase « arrêt d'un processus par son PID » a disparu du suivi (a4) ; l'interdit général de l'en-tête (l. 27) tient.

## 5. Les deux points de l'outil 1.8.3, tranchés dans son code

**Solde du compte.** `show user --raw` rend l'objet du compte tel que le service le donne, moins `api_key`
(`api/billing.py` l. 236-240 ; `cli/commands/billing.py` l. 538-546 ; impression par `json.dumps` dans `cli/main.py` l. 206-208).
Les champs lus par l'affichage en tableau (`cli/display.py` l. 341-371) comprennent **`credit`**, seul champ formaté en montant
(`{:0.2f}`), et `balance`, sans format ; la notice jointe à l'outil dit de cette commande « credit balance ». **Le nom `credit` de la
l. 129 est juste** : la réserve « nom du champ à confirmer » peut être levée. Le code ne dit pas le sens exact de `balance` ; par
prudence, afficher les deux (aucun n'est personnel) et exiger le seuil par programme :
ancien : `… print("solde", json.load(sys.stdin)["credit"])'` ;
nouveau : `… u=json.load(sys.stdin);print("solde", u["credit"], "balance", u.get("balance"));assert float(u["credit"])>=5'`.
En mode brut, l'avis de mise à jour de l'outil est supprimé et les erreurs vont sur la sortie d'erreur : la sortie standard reste du
JSON pur.

**Adresse et port ssh.** Les deux voies de la l. 182 existent.
- `ssh-url ID` (`cli/commands/misc.py` l. 153-218) imprime une ligne `ssh://root@ADRESSE:PORT`. Il lit d'abord un fichier de cache
  de l'outil (`ssh_ID.json` dans le dossier de cache de l'utilisateur), sinon la liste des instances : si la ligne porte
  `ports["22/tcp"]`, adresse = `public_ipaddr` et port = `ports["22/tcp"][0]["HostPort"]` ; sinon adresse = `ssh_host` et port =
  `ssh_port` (plus 1 seulement si le type de lancement contient « jupyter » ; le type par défaut de la création est ssh). **Piège** :
  sur un port introuvable il imprime `error: ssh port not found` et sort en code 0 ; sur un identifiant inconnu il imprime une
  erreur sur la sortie standard. Son code de sortie ne prouve rien.
- `show instances --raw` rend la liste plate des lignes entières ; champs : `ssh_host` et `ssh_port` (relais du loueur),
  `public_ipaddr` et `ports` (accès direct), `image_runtype`.

Recommandé, la seconde voie, sans cache et vérifiable (éprouvé ici sur une ligne factice) :
`vastai show instances --raw > "$ENV/instances-ssh.json" && python3 -c 'import json,re,sys;m=[i for i in json.load(open(sys.argv[1])) if str(i["id"])==sys.argv[2]];assert len(m)==1,m;h=str(m[0]["ssh_host"]);p=int(m[0]["ssh_port"]);assert re.fullmatch(r"[A-Za-z0-9.-]+",h) and 0<p<65536;print(h,p)' "$ENV/instances-ssh.json" "$(cat "$ENV/identifiant.txt")"`
Tant que la machine se monte, ces champs peuvent être nuls : le programme échoue, on relit plus tard (attente à borner, a5).

## 6. Commandes et scripts cités

- **Lanceur** (analyseur l. 643-699) : `secret CHEMIN` ; `generer --secret --phrase-fichier --texte --texte-sha256 --sortie` ;
  `preparer --mondes --mondes-sha256` ; `jouer --mode --mondes --mondes-sha256 --sortie` et les huit options du mode réel ;
  `mesurer --sortie --mondes --mondes-sha256` ; `lire --sortie --ecrire` ; `rapatrier --source --destination --mondes
  --mondes-sha256` ; `bloc --releve-sonde`. Toutes existent, noms exacts. Codes 0, 2 (refus), 3 (arrêt) : l. 737-743.
- **Bloc neuf de la section 1** : `pole/proposeurs_pilote_v72.py` (`lire_configuration(chemin)`, rend un couple), `pole/proposeurs_pilote_v70.py`
  (`lire_go_du_pilote(conf, registre, go_pi1, go_pi2)`), `demonstrations/pilote_mr2_v74.py` (`CONFIGURATION`) : présents, signatures
  égales à l'appel écrit ; l'appel rend « lignes du pilote lues au montant exact », code 0, sous `env -i` et `-I`.
- **Outil du loueur 1.8.3** : `create instance ID --image --disk --label`, `--raw` général, sortie `{"success": …, "new_contract": N}` ;
  `show instances --raw` ; `show user --raw` ; `ssh-url ID` ; `destroy instance ID -y` : existent sous la forme écrite.
- **Scripts** : modèle de la section 9 rendu pour `reel` et `reel-2` (0 marque, `bash -n` juste). Lancement détaché : voir MA.

## 7. Constats classés

### Bloquant

Aucun.

### Majeurs

**MA — Le lancement détaché, tel qu'il est écrit en v7, retient la commande `ssh` jusqu'à la fin du processus, et affiche « lancé »
même quand rien n'est lancé** (l. 332 et 355 pour `jouer` ; l. 244 pour `generer` ; l. 379 pour `mesurer`). Changement non déclaré.
Dans `test ! -e F && setsid nohup bash S > /dev/null 2>&1 < /dev/null & echo lancé`, le `&` met en arrière-plan toute la liste
`test … && setsid …` : un sous-interpréteur attend la fin du script en gardant ouvertes la sortie et l'erreur de la session ssh, et
`echo lancé` s'exécute dans tous les cas. Éprouvé ici, avec `sleep 4` à la place du script et un tube à la place de ssh : forme de
la v6, retour en 0,005 s ; forme de la v7, retour en 4,0 s ; forme de la v7 avec le fichier de code déjà présent : « lancé » affiché
alors que rien n'est parti.
Conséquence : la commande de lancement du pilote réel ne rend pas la main (12 min pour `generer`, jusqu'à 12 h pour `jouer`) ;
l'outil de la session la coupe à son délai. Le pilote survit (il est détaché), mais l'exécutant voit un délai dépassé à l'étape la
plus chère. S'il rejoue la ligne, la garde ne protège pas : `code-09-reel.txt` n'existe qu'**après** la fin du pilote. Le second
script tronque alors `journal-09-reel.txt`, reçoit un refus (dossier de sortie existant), écrit « 2 » dans `code-09-reel.txt` et
efface le fichier des clés : le suivi lit « 2 » avec « clés effacées », le registre des lancements existe, la règle dit arrêt (A),
et la machine est détruite pendant les appels payés. C'est l'accident du majeur N1 de la v5, par un autre chemin.
Correction — ancien (l. 332) : « `ssh M 'test ! -e /root/pilote/code-09-reel.txt && setsid nohup bash /root/pilote/lancer-reel.sh > /dev/null 2>&1 < /dev/null & echo lancé'` » ;
nouveau : « `ssh M 'test ! -e /root/pilote/code-09-reel.txt && test ! -e /root/pilote/journal-09-reel.txt && { setsid nohup bash /root/pilote/lancer-reel.sh > /dev/null 2>&1 < /dev/null & echo lancé; } || echo "NON LANCÉ"'` »
(forme éprouvée ici : retour immédiat ; « NON LANCÉ » si le fichier existe). La garde sur le **journal**, écrit dès le début du
script, est celle qui interdit un second lancement pendant le premier. Même forme aux l. 244 (`code-06-generer.txt`,
`journal-06-generer.txt`), 355 (`code-09-reel-2.txt`, `journal-09-reel-2.txt`) et 379 (`code-10-mesurer.txt`,
`journal-10-mesurer.txt`). Ajouter après chaque lancement : « si la commande de lancement ne rend pas la main ou dépasse son délai :
**ne jamais la rejouer** ; passer au suivi ».

**MB — Relance après un refus tombé une fois `reel/` créé : le contrôle rejoué exige `reel` absent** (l. 353 contre l. 289 et 306).
La l. 353 dit « rejouer TOUS les contrôles « juste avant » ci-dessus » ; le premier de ces contrôles est
`test ! -e /root/pilote/reel && test ! -e /root/pilote/reel-2 && test ! -e /root/pilote/lancements.jsonl && echo absents`, et la
l. 306 dit « arrêt (A) si un dossier existe ». Quand le premier essai a créé `reel/` (refus au lancement des relais ou à leur
attente : registre absent, donc relance permise par la l. 346), ce contrôle échoue : à la lettre, l'exécutant détruit la machine,
et la relance que la l. 346-348 accorde « que `reel/` ait été créé ou non » n'a jamais lieu ; sinon il choisit seul, machine louée.
L'issue à la lettre est du côté prudent (rien n'est appelé), mais elle coûte les mondes, donc un texte neuf et le mot de Lazar.
Correction — ancien (l. 353) : « `# rejouer TOUS les contrôles « juste avant » ci-dessus, puis renvoyer les clés (bloc « Clés »)` » ;
nouveau : « `# rejouer tous les contrôles « juste avant » ci-dessus SAUF la ligne des dossiers, remplacée par :` puis
`ssh M 'test ! -e /root/pilote/reel-2 && test ! -e /root/pilote/lancements.jsonl && echo absents'` `# (reel/ du premier essai peut exister : il reste en place, jamais rapatrié) ; puis renvoyer les clés (bloc « Clés »)` ».

### Mineurs

- **a1 — `cd … || exit 97` n'écrit pas le fichier de code** (l. 240, 374). Le suivi dit « en cours » sans fin ; le « 97 » de la
  l. 386 ne peut pas être lu. Ancien : « `cd /root/pilote/arbre/orchestrator || exit 97` » ; nouveau (l. 374) :
  « `cd /root/pilote/arbre/orchestrator || { echo 97 > /root/pilote/code-10-mesurer.txt; exit 97; }` », et de même à la l. 240 avec
  `code-06-generer.txt` (la forme de la l. 326 le fait déjà). Dire aussi : « `mesurer` muet (aucun code, processus disparu) : même
  conduite que tout autre code non nul ».
- **a2 — `REEL` et `ETIQ` ne sont pas gardés.** `REEL` n'est écrit dans `variables.sh` qu'après une relance (l. 359 : « sinon
  `REEL=reel` », sans commande) ; avec `REEL` vide, le `sed` de la l. 378 rend `--sortie /root/pilote/` avec 0 marque restante
  (éprouvé), et la l. 407 prend `/root/pilote/` pour source. Nouveau : après un code 0 du premier essai,
  `echo REEL=reel >> "$ENV/variables.sh"` ; en tête des commandes des sections 10 et 11, `: "${REEL:?}" "${H:?}"`. De même
  `: "${ETIQ:?}"` en tête de la commande de création (l. 142) : une étiquette vide ferait refuser la destruction par le programme
  « avant ».
- **a3 — Point 6 de la section 2 : « programme du repli, rendu égal à `identifiant.txt` »** (l. 159-160). Rejoué tel qu'écrit, le
  programme du repli **récrit** `identifiant.txt` (et le vide s'il échoue). Nouveau : le même programme sans la redirection, suivi de
  `| diff - "$ENV/identifiant.txt" && echo "seul ajouté, égal à l'identifiant"`.
- **a4 — Quatre retraits ou changements non déclarés.** (i) Le nœud « à 2,70 USD dépensés sur la machine » (v6 l. 93-94) : le dire
  retiré (couvert par le nœud d'une heure avant) ou le remettre. (ii) « aucun arrêt du processus sans elle, et alors par son PID
  (R10) » (v6 l. 258-259) : à remettre dans le paragraphe de l'heure limite (l. 78-81). (iii) « risque résiduel **accepté** par la
  mère » (l. 318 ; v6 : « à trancher par la mère ») : aucune décision retrouvée dans les registres lus ; citer la référence ou
  revenir à « à trancher ». (iv) Le témoin de l'inventaire d'avant (l. 132-133) : dire ce qu'il est (au moins une instance listée),
  ou retirer « avec témoin ».
- **a5 — ssh : le programme qui remplit `ADRESSE` et `PORT` n'est pas écrit** (l. 171-182), ni l'attente du montage de la machine,
  ni la clé privée employée. Nouveau : le programme de la section 5 ci-dessus, sa sortie versée dans `ssh_config` par programme ;
  une attente bornée (par exemple dix minutes de relectures de la liste) avant l'arrêt (A) ; une ligne `IdentityFile` si la clé
  n'est pas celle par défaut ; avant la création, constater que le compte du loueur porte une clé ssh.
- **a6 — Solde** (l. 129-130) : lever la réserve, le champ est `credit` ; seuil exigé par programme (section 5 ci-dessus).
- **a7 — « Tout autre code » de `jouer`, machine gardée** (l. 363-365). La commande qui constate le registre n'est pas écrite :
  `ssh M 'test -e /root/pilote/lancements.jsonl && echo présent || echo absent'` (un échec de ssh vaut « illisible »). Et si le
  script a été tué avant sa dernière ligne, le fichier des clés reste sur la machine pendant l'attente : ajouter « si aucun `jouer`
  ne tourne, effacer les clés (étape (2) de (A)) avant le nœud ».
- **a8 — Recherche de l'offre non écrite** (l. 136-148 ; déjà vrai en v6). « Recopié par programme de la recherche d'offres » sans
  commande ni champ du prix total. À écrire, ou à dire fait à la main par la mère avec le prix consigné.
- **a9 — Section 12 quater, « éprouvé »** (l. 536-540) : la liste ne comprend pas la ligne de lancement détaché, seule partie du
  script changée dans sa mécanique. À éprouver après correction de MA, avec une commande factice, à travers un tube ou un ssh local.

## Pièces

- Arbre dépaqueté et essais de forme : dossier temporaire de la session du lecteur, hors de tout dépôt (`arbre-v7/`, `essais/`).
- Rien d'autre n'a été écrit dans la copie que ce rapport et son compagnon ; aucun commit, aucune poussée.
