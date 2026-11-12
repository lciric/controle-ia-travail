# Essai Lean, D-1a — procédure du poste local — v7

- **Pour** : la session mère, qui en tire la seconde consigne du poste local (Claude Code sur l'ordinateur de Lazar).
- **Écrit par** : l'auteur du harnais (Opus 5.5).
- **Remplace** : `procedure-poste-local-d1a-v6.md` (`9e7f5172…`), qui reste versée telle quelle (R12).
- **Sources** : décisions R-2323, R-2333 et R-2415 ; contre-lecture `contre-lecture-courte-machine-harnais-d1a-v5.md`
  (`897b7438…`), section finale ; rapport `rapport-poste-local-d1a-v1.md` (branche `donnees/lean-outillage-d1a-poste-local-v1`).
- **Code** : branche `prep/lean-outillage-d1a-v7`, commit `65167979a9f2910a6d8e0d9767ceccdef2c2d018`, parti de `149babdc` (v6), non fusionné.
  - Module : `controle_ia.lean_essai.minuterie_v6` (inchangé).
  - Pilote : `scripts/lean_essai_d1a_v7/piloter_poste_v7.sh`.
  - Installateur lancé par le pilote : `scripts/lean_essai_d1a_v2/installer_chaine_v2.sh`.

## Changements depuis v6

- **Seule cause de l'arrêt du premier essai corrigée** (`noyau` non conforme, 0/18) : les fichiers compilés de Mathlib tirés du
  cache étaient en `-rw-------` ; après `chown -R chaine` et `chmod -R go-w`, `bac` ne lisait pas `Mathlib.olean`.
  - `installer_chaine_v2.sh` = `installer_chaine_v1.sh` (inchangé, R12) plus `chmod -R a+rX` sur `/opt/elan`, `/opt/mathlib`,
    `/opt/pybac`, après `go-w` et avant le montage en lecture seule ;
  - plus une **garde de lisibilité** qui arrête l'installation (code 5, ligne « ARRÊT » au journal d'installation) si un
    fichier ou un dossier de ces trois arbres n'est pas lisible par les autres, si un dossier n'est pas traversable, si un
    exécutable ne l'est pas pour les autres, ou si `bac` (par `runuser`) ne lit pas l'échantillon : `/opt`, `/opt/harnais`,
    les trois racines, `Mathlib.olean`, le Python du bras S, les dossiers existants de `LEAN_PATH` ; ou n'exécute pas `lean`
    et ce Python. En cas d'arrêt, la phase « avant » du pilote échoue (`set -e`) : rien d'autre n'est lancé, la session locale
    passe à la section 5 (destruction par l'identifiant), compte rendu ; aucune réinstallation hors consigne.
- `piloter_poste_v7.sh` = `piloter_poste_v6.sh` avec trois changements :
  - la phase « avant » copie et lance `installer_chaine_v2.sh` ;
  - **clé d'hôte** (rapport, incident 5) : `scp` reçoit aussi `-o StrictHostKeyChecking=accept-new`, comme `ssh`. La première
    copie, qui précède tout `ssh`, enregistre la clé d'hôte d'un serveur jamais vu au lieu d'échouer ; une clé **différente**
    d'une clé déjà enregistrée reste refusée. Plus besoin du `ssh … true` préalable du premier essai.
  - **cache du résolveur** (rapport, incident 6) : dans la phase « apres », `resolvectl flush-caches` sur le serveur, après
    la coupure et avant la sonde. La sonde « après » ne lit plus la réponse que la sonde « avant » a mise en cache (faux
    « résolveur système : ouverte »). Cela ne fait que durcir la sonde : réseau coupé, le cache ne peut plus se remplir, et
    la sonde interne de l'exécuteur (`sonde_reseau_v1`, inchangée) en profite aussi. Commande absente ou en échec : arrêt du
    pilote (`set -e`), rien n'est lancé.
  - Noms des sorties (`*-v6.*`) et fichiers écrits sur la machine (`journal-installation-v1.txt`, `chaine-v1.json`) gardés.
- Essais : `tests/test_lean_essai_installer_v2.py` (garde sur des fichiers réels 0644 et 0600, ordre de l'installateur,
  clé d'hôte de `scp`, place du vidage du cache, aucun autre changement que ceux-ci) ; mutations
  `scripts/lean_essai_d1a_v7/mutations_harnais_v7.py` (l01 à l07 en plus, toutes tuées).
- **Le reste de la procédure est celui de la v6, mot pour mot**, hors des noms du pilote.
- **Point ouvert pour Lazar — source SSH du pare-feu** (rapport, incident 4 et écart 6) : le poste sort par au moins deux
  adresses IPv4 du même /24 ; avec une règle à une seule adresse, le port 22 n'était joignable qu'environ une fois sur huit.
  Au premier essai, sur ton accord, les règles ont été reposées hors procédure avec la source SSH élargie au /24. **Le
  harnais n'est pas changé** (`acces-creer` et `acces-couper` posent toujours la seule `IP_POSTE`) : c'est une règle de
  sécurité, à trancher par toi. Options : (1) garder une seule adresse et mesurer d'abord les adresses de sortie du poste ;
  (2) admettre une source en réseau (/24) dans le harnais (version neuve, essais et mutations) ; (3) refaire à la main,
  déclaré comme écart, ce qui a été fait au premier essai. Le trafic sortant du serveur reste coupé dans les trois cas.
- **Non repris** : la sonde (`sonde_reseau_v1.py`) n'est pas changée ; un nom neuf à chaque appel aurait demandé une
  version neuve de la sonde, de l'exécuteur et de l'épreuve qui l'importent. Le vidage du cache suffit à l'incident.
- **Réserve pour la consigne** : la minuterie refuse une seconde préparation et une seconde machine sous le même GO
  (`rattrapage-machine-d1a-*` déjà versé, journal des créations, ligne de `registres/depenses.md`). Le second essai demande
  donc **un GO neuf**, une branche du poste neuve partie du commit ci-dessus (sans les pièces du premier essai dans `V`), et
  le GO de la consigne à la place de `GO-2026-11-10-13` dans les commandes ci-dessous.

## Rappel : ce qui changeait de la v5 à la v6
- **Statut** : rien de ceci n'a tourné contre l'interface réelle de Hetzner ; les essais tournent sur un faux transport et sur
  de vrais processus locaux. Cette procédure ne vaut qu'après la contre-lecture courte du tour 6, et sous une consigne neuve
  de la mère.


- **CLC5-02** : trois tâches de la mère au lieu de deux.
  - Une dans sa session, à `H`.
  - **Deux qui ouvrent une session neuve**, à `H + 30 min` et à `H + 24 h`.
  - Les identifiants des trois sont inscrits dans `registres/etat.md` et dans chaque passation.
  - Lazar pose son propre rappel à `H + 1 h`.
- **CLC5-04** : une ligne « en tâche jusqu'à … » dans `registres/etat.md`, écrite par la mère à l'armement, pour que la
  routine de reprise ne détruise pas le serveur au travail.
- **CLC5-05** : les commandes du harnais tournent **hors du bac à sable de Claude Code** sur le poste, après un essai à blanc.
- **CLC5-07** : **aucune donnée du poste de Lazar dans un fichier versé ou poussé**.
  - Son adresse IPv4 ne vit qu'en mémoire, comme argument de commande. Le fichier d'accès ne la porte plus.
  - La clé part sans son commentaire, souvent `utilisateur@machine`. Les sorties ne portent que des chemins relatifs au
    clone.
  - **`garde-poste` précède chaque commit.**
- **Mot « armée »** : il porte l'empreinte (sha256) du fichier de rattrapage lu par la mère. `creer-et-armer` exige cette
  empreinte (`--empreinte-mere`) et la compare avant tout appel.
- **Création** :
  - la clé SSH et le pare-feu sont pris dans le fichier d'accès poussé : plus de `--cle-ssh` ni de `--pare-feu` ;
  - une seconde préparation est refusée, même dans un clone sans journal des créations (CLC5-03) ;
  - le contrôle de survie n'est plus trompé par la course de l'`exec` (CLC5-01).
- **Bornes** :
  - `detruire` et `inventaire` rendent le code 5 au-delà de 8 minutes de panne passagère ;
  - le pilote borne chaque commande SSH.

## Rôles et règle d'or

- **Session locale** : clone du dépôt, jeton `HCLOUD_TOKEN` dans son environnement (lu par son nom, jamais affiché ni écrit),
  SSH vers la machine. Elle seule crée.
- **Session mère** : dans le nuage, sans SSH, avec son propre `HCLOUD_TOKEN`. Elle lit et détruit par identifiant, par des
  requêtes de l'interface, sans aucun code de la branche.
- **Lazar** : relaie entre les deux sessions, qui ne se parlent pas. Il donne à la session locale l'adresse IPv4 publique du
  poste, **dans la conversation seulement**.
- **Règle d'or** :
  - aucune création avant le mot « armée » de la mère, avec son empreinte ;
  - une seule préparation, une seule création ; jamais de recréation ; jamais de relance d'une minuterie.

## 0. Prérequis du poste (session locale)

1. **Dépôt** :
   - **un seul clone** de `https://github.com/lciric/controle-ia-travail` ; `git remote -v` le montre, jamais
     `lciric/controle-ia` ;
   - branche de travail à soi, au nom fixé par la consigne, partie du commit ci-dessus, poussée avec `git push -u` ;
   - **toutes les commandes se lancent depuis la racine du clone**.
2. **Outils** :
   - Python 3.11 ou plus récent (essais passés sous 3.11 et 3.13 ; bibliothèque standard seule pour la minuterie) ;
   - `git`, `ssh`, `ssh-keygen`.
3. **Jeton** : `HCLOUD_TOKEN` est posé par Lazar dans l'environnement de la session. C'est un jeton en lecture et écriture du
   projet de l'essai. Jamais `env`, `printenv` ni affichage.
4. **Hors du bac à sable de Claude Code (CLC5-05)** : les commandes du harnais (`minuterie_v6`, pilote) tournent sans le bac
   à sable, selon le réglage que Lazar choisit. Elles sont pré-autorisées, pour qu'aucune destruction n'attende une demande
   de permission. **Essai à blanc** avant L1 :
   - `python3 -c "import subprocess; p = subprocess.Popen(['sleep', '900'], start_new_session=True); print(p.pid)"`,
     puis, dans une **autre** commande, `kill -0 <PID>`, qui doit réussir ;
   - après une fin puis une reprise de la session, `kill -0 <PID>` doit réussir encore ; ensuite `kill <PID>` (R10) ;
   - `python3 -c "import urllib.request; print(sorted(urllib.request.getproxies()))"` n'imprime que des noms, jamais une
     valeur. Il doit rendre `[]`, ou un mandataire du système, jamais un mandataire propre à la session ;
   - si l'un des trois échoue : arrêt, compte rendu à Lazar, aucune préparation.
5. **Ordinateur** :
   - sur secteur, veille coupée, **capot ouvert**, pas de déconnexion de la session, jusqu'à la destruction ;
   - sous macOS, `caffeinate -i -w <PID de la minuterie>`, lancé détaché après L6 (il n'empêche pas la veille capot fermé).
6. **Notation** :
   - `MV6` désigne `PYTHONPATH=src python3 -B -m controle_ia.lean_essai.minuterie_v6` ;
   - `V` désigne `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1` ;
   - `IP_POSTE` est l'adresse donnée par Lazar ; elle n'est jamais écrite dans un fichier du clone ;
   - tout fichier passé à `--journal` ou à `--sortie` porte un nom neuf (R12).
7. **Avant chaque commit** : `MV6 garde-poste --ip-poste IP_POSTE && git commit …`.
   - La commande lit l'index git et refuse (code 1) s'il porte l'adresse du poste, son dossier personnel ou le chemin du
     clone.
   - Elle n'en écrit jamais la valeur, seulement la nature.

## 1. Avant la création

### L1 (locale) — préparer, une seule fois

```
MV6 preparer --go GO-2026-11-10-13 --heure-limite-creation <T_LIM> --heure-tache-mere <H>
```

- `T_LIM` et `H` sont fixés par la consigne, en ISO 8601 UTC.
- **Refus** :
  - `T_LIM` déjà passée ;
  - `H` moins de 2 heures après `T_LIM`, ou plus de 47 heures après maintenant ;
  - GO invalide ;
  - machine déjà inscrite sous ce GO ;
  - **un autre fichier `rattrapage-machine-d1a-*` déjà dans `V` (CLC5-03)**.
- **Fichier écrit** : `V/rattrapage-machine-d1a-<jeton12>-v1.json`. Il contient :
  - le jeton, les étiquettes fixes et le nom ;
  - l'heure de préparation et l'heure limite de création ;
  - l'échéance au plus tard `H − 1 h` ;
  - **les trois tâches de la mère** (heure, mode, message autosuffisant avec les formes `curl`) ;
  - **la ligne d'état de la mère** et l'heure du rappel de Lazar (`H + 1 h`) ;
  - les commandes de destruction du poste.

### L2 (locale) — clé SSH et pare-feu étiquetés

```
ssh-keygen -t ed25519 -N "" -C lean-outillage-d1a -f <dossier hors du dépôt>/cle-lean-d1a
MV6 acces-creer --rattrapage V/rattrapage-machine-d1a-<jeton12>-v1.json \
    --cle-publique <dossier hors du dépôt>/cle-lean-d1a.pub --ip-poste IP_POSTE
```

- **Objets créés** (gratuits) : une clé SSH et un pare-feu, nommés `lean-outillage-d1a-<jeton12>` et étiquetés `essai`,
  `pas`, `go`, `creation=<jeton>`. Le pare-feu porte les règles d'installation (SSH depuis le seul poste).
- La clé est envoyée **sans son commentaire**.
- **Fichier écrit** : `V/acces-machine-d1a-<jeton12>-v1.json`, avec les identifiants et l'empreinte de la clé, **sans
  l'adresse du poste ni les règles**.

### L3 (locale) — pousser avant toute création

- `MV6 garde-poste --ip-poste IP_POSTE`, puis committer et pousser les deux fichiers.
- Donner à Lazar, pour la mère :
  - la branche et le commit ;
  - le jeton ;
  - les identifiants de la clé et du pare-feu, et l'empreinte de la clé.

### M1 à M6 (mère) — s'armer avant la création

- **M1 — lire** : `git fetch` de la branche du poste, relecture des deux fichiers, et calcul de **l'empreinte sha256 du
  fichier de rattrapage tel que poussé**.
- **M2 — même projet** : par son propre jeton,
  - `GET /v1/ssh_keys?label_selector=creation%3D<jeton>` doit rendre une seule clé, de même identifiant et de même
    empreinte ;
  - `GET /v1/firewalls?label_selector=creation%3D<jeton>` doit rendre un seul pare-feu, de même identifiant ;
  - des réponses, n'afficher que les identifiants et les noms : les règles portent l'adresse du poste.
  - Sinon : **arrêt, aucune création**.
- **M3 — droit d'écrire** : `POST /v1/firewalls` avec `{"name": "preuve-ecriture-mere-<jeton12>", "labels": {"essai":
  "lean", "preuve": "mere"}}`, puis `DELETE` du même identifiant, puis `GET`, qui doit rendre 404. C'est gratuit. Un 401 ou un
  403 : arrêt.
- **M4 — destruction à blanc** : les deux listes (par étiquettes et par nom) ne rendent aucun serveur.
- **M5 — trois tâches** (CLC5-02), aux heures absolues du fichier, chacune avec son message recopié tel quel :
  - **T1**, à `H` : rappel dans la session mère (`send_later`).
  - **T2**, à `H + 30 min` : **tâche programmée qui ouvre une session neuve** à son déclenchement.
  - **T3**, à `H + 24 h` : de même.
  - Relire les trois après création : actives, prochaine heure exacte.
  - La session qui porte T1 n'est pas archivée avant « aucun serveur de l'essai ».
- **M5 bis — ligne d'état** (CLC5-04) : recopier `ligne_etat_mere` du fichier dans `registres/etat.md`, avec les identifiants
  des trois tâches, puis committer. La reprendre dans chaque passation jusqu'à la destruction confirmée.
  - La routine de reprise (R-2322) ne détruit pas un serveur en tâche avant l'heure de cette ligne.
  - Au-delà de cette heure, ou si la ligne manque, elle le détruit.
- **M6 — signaler** : dire à Lazar « armée », avec **l'empreinte sha256 du fichier de rattrapage**, les identifiants des
  tâches, `H`, `H + 30 min` et `H + 24 h`.
  - Lazar le transmet à la session locale, et pose son rappel personnel à `H + 1 h` : console de Hetzner, zéro serveur
    attendu.
  - **Sans ce mot, aucune création.**

## 2. Création (session locale)

### L4 — juste avant

- `MV6 inventaire` doit rendre « aucun serveur de l'essai ».
- L'heure doit être avant `T_LIM`.
- Le mot « armée » doit être reçu, avec son empreinte.

### L5 — création détachée, une seule fois

```
MV6 creer-et-armer --go GO-2026-11-10-13 --rattrapage V/rattrapage-machine-d1a-<jeton12>-v1.json \
    --empreinte-mere <empreinte du mot « armée »> --type ccx33 --lieu <lieu du devis> --deja-depense-usd 0 \
    --journal V/journal-creation-d1a-<jeton12>-v1.jsonl --detache --sortie V/sortie-creation-d1a-<jeton12>-v1.log
```

- **Ce que rend la commande** : tout de suite, le PID du processus détaché et le chemin relatif de la sortie.
- **Ce que fait le processus**, dans l'ordre :
  1. contrôles, avant tout appel :
     - empreinte égale à celle du mot « armée » ;
     - aucun autre fichier de rattrapage ;
     - heure limite ;
     - fichiers de rattrapage **et** d'accès poussés (lus par `git ls-remote`) ;
     - GO, seconde machine refusée, type dans la liste du devis, taux d'au moins 1,25, devis ;
  2. intention écrite avant l'appel ;
  3. création avec la clé et le pare-feu du fichier d'accès ; si la réponse se perd, rattrapage par l'étiquette pendant
     10 minutes ;
  4. minuterie détachée, d'échéance `min(création + 48 h, H − 1 h)` ;
  5. **contrôle de survie par `poll()`** : processus vivant et première ligne « garder » en 120 secondes ; sinon,
     destruction immédiate par l'identifiant.
- **Attendre** la fin du processus (`kill -0 <PID>` toutes les 15 secondes, 15 minutes au plus), puis lire la sortie.
- **Fin normale** : la dernière ligne est un objet JSON avec `identifiant`, `echeance`, `minuterie.pid`,
  `minuterie.fichier_pid` et `minuterie.journal` (chemins relatifs au clone).
- **Toute autre fin** : section 4. **Aucun second essai** ; le code le refuse de toute façon.

### L6 — dans la minute

```
MV6 verifier-minuterie --fichier-pid <minuterie.fichier_pid> --journal-minuterie <minuterie.journal>
```

- Il doit rendre `"conforme": true`.
- Sinon, refaire deux minutes plus tard. Encore non conforme : `MV6 detruire --identifiant <N> --journal <neuf>`, puis
  `MV6 inventaire`, arrêt, compte rendu. **Jamais de relance de la minuterie.**

### L7 — pousser et signaler, tout de suite

- `MV6 garde-poste --ip-poste IP_POSTE`, puis pousser : le journal des créations, le fichier PID, le journal et la sortie de
  la minuterie, la sortie et le journal de la création.
- Donner à Lazar, pour la mère : l'identifiant, l'échéance et le PID.

## 3. Pendant le travail (session locale)

- **Adresse du serveur** : `MV6 adresse-serveur --identifiant N`. Cette adresse est utilisée seulement en argument, jamais
  versée.
- **Ordre** :
  1. `scripts/lean_essai_d1a_v7/piloter_poste_v7.sh avant <adresse du serveur> <clé privée> <commit de Mathlib>` ;
  2. `MV6 acces-couper --rattrapage … --ip-poste IP_POSTE`, puis
     `MV6 verifier-coupure --serveur N --pare-feu F --journal <neuf>` (adresses masquées) ;
  3. `piloter_poste_v7.sh apres <adresse du serveur> <clé privée> <dossier de sorties hors du clone>`.
- **Le pilote se lance en arrière-plan**, sorties dans des fichiers : l'installation dépasse la limite d'une commande de
  premier plan. Chaque commande SSH est bornée par `timeout` côté serveur ; une connexion qui pend l'est par
  `ConnectTimeout` et `ServerAlive*`.
- **Pièces du pilote** : elles ne vont dans `V` qu'après `MV6 garde-poste --ip-poste IP_POSTE --fichier <pièce>` (code 0).
- **À chaque reprise de session, et au moins toutes les heures** : lire la sortie de la création et le fichier PID, puis
  `MV6 verifier-minuterie … --journal-minuterie …`.
  - Non conforme deux fois, à 2 minutes d'écart : `MV6 detruire --identifiant N`.
  - Jamais de relance.
- **Ne jamais** renommer le serveur ni toucher à ses étiquettes.
- **Machine injoignable** : `MV6 inventaire`. Si le serveur est absent (la mère, la minuterie ou la routine de reprise l'a
  détruit) : **ne pas recréer**, compte rendu.
- **Commande bornée** : `detruire` ou `inventaire` qui rend le code 5 (panne passagère de plus de 8 minutes), ou qu'un outil
  coupe sans code : refaire 15 minutes plus tard, puis prévenir Lazar et la mère.

## 4. Fin anormale de la création (session locale)

1. `MV6 detruire --pas d1a --journal <neuf>` tout de suite.
   - Code 0 : lire `detruits`.
   - **Code 3** : Lazar détruit à la main, par l'identifiant, dans la console.
   - Codes 4 et 5 : refaire.
2. `MV6 inventaire` doit rendre « aucun serveur de l'essai ».
3. **Quinze minutes plus tard**, refaire 1 et 2.
4. Compte rendu à Lazar ; aucun second essai.

## 5. Fin normale

1. **Locale** : `MV6 detruire --identifiant N --journal <neuf>`. Code 3 : destruction à la main.
2. **Locale** : `MV6 inventaire` doit rendre « aucun serveur de l'essai », avec `ips_primaires_non_attribuees` vide. Sinon,
   le signaler sans rien supprimer.
3. **Locale** : `MV6 acces-supprimer --rattrapage …`.
4. **Locale** : `MV6 verifier-minuterie …`. Si la minuterie vit encore, l'arrêter par son PID (`kill <PID>`, R10).
5. **Locale** : `MV6 garde-poste --ip-poste IP_POSTE`, puis pousser toutes les pièces. Lazar prévient la mère.
6. **Mère** :
   - relire par son propre jeton (M4) ;
   - inscrire l'arrêt dans `registres/arrets.md` et clore la ligne « en tâche jusqu'à » ;
   - alors seulement, désarmer T1 à T3, ou les laisser tourner : elles ne trouveront rien.
   - Aucune copie publique avant une relecture des pièces versées (CLC5-07).

## 6. Codes de sortie de `minuterie_v6`

| Code | Sens |
|---|---|
| 0 | Fait. |
| 1 | Arrêt : refus, ou serveur créé puis détruit ; erreur inattendue, avec une trace aux chemins masqués. Lire le message. |
| 2 | Usage. |
| **3** | **Destruction refusée durablement (401 ou 403)** : le détruire à la main par son identifiant. |
| **4** | **Rattrapage à refaire** : `detruire --pas d1a` maintenant, puis quinze minutes plus tard. |
| **5** | **Panne passagère plus longue que la borne** : refaire dans 15 minutes, puis prévenir Lazar et la mère. |

## 7. Réserves

- **Aucun appel réel n'a été fait.** Les premières lectures réelles sont M2 et M4, faites par la mère.
- **La minuterie locale meurt avec l'ordinateur** (extinction, déconnexion). Les garde-fous de fond sont T1 à T3, la ligne
  d'état lue par la routine de reprise, et le rappel de Lazar.
- **Coût au pire**, garde-fous locaux morts :
  - jusqu'à `H` (47 heures après la préparation au plus) si T1 agit ; `H + 30 min` si seule T2 agit ; `H + 24 h` si seule T3
    agit, soit 71 heures, environ 30 USD pour `ccx33` (extrapolation de la contre-lecture, non vérifiée ici) ;
  - au-delà, seuls le rappel de Lazar et la routine de reprise restent.
- **Le bac à sable et le mandataire du poste ne sont pas éprouvés ici.** L'essai à blanc du point 4 de la section 0 en décide.
- **`garde-poste`** :
  - il ne lit que ce qu'on lui donne (l'index git, ou des fichiers nommés) ;
  - il ne connaît ni le nom de la machine ni celui de l'utilisateur, seulement l'adresse, le dossier personnel et le chemin
    du clone. Le reste tient à la discipline de la consigne.
