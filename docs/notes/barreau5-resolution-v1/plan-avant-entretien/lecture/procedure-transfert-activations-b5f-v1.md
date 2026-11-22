# Procédure — transfert des activations de la relecture du barreau 5 vers le volume de stockage — v1

- **Statut** : pièce de classe B (instrument) : contre-lecture par un autre modèle, puis vérification des corrections par le même contre-lecteur, avant tout geste payant. Elle ne vaut accord de rien.
- **Rédacteur** : Claude Opus 5.5 (`claude-opus-5-5`), rédacteur neuf, sous-agent du conducteur de la lecture du barreau 5 (`session_013QMayjM1PQPWkLifMw9HDR`). Écrite le 22 novembre 2026, de 19:20 à 19:45Z environ. Aucun appel payant, aucune machine, aucun volume, aucun appel en écriture chez le loueur de cartes ni chez Hetzner ; deux lectures de documentation publique (§ 13).
- **Accord** : GO-2026-11-22-117 (« … plus 17 à 24 USD pour garder les activations … go » ; plafond 33 USD, 9 + 24 ; **échéance 2026-11-30**), part « garder les activations », **24 USD au plus**.
- **Décision servie (mère)** : sous la garde « trois_couches », l'amorce verse les scores fermés puis laisse les activations (≈ 152 Go) sur l'instance de relecture, **arrêtée et non détruite** (mandat de la session de lecture v2, § 5.4, pas 8, et § 9, point 8). Cette procédure les tire de là vers le volume de 200 Go, les prouve fichier par fichier, puis détruit l'instance et le serveur, et garde le volume.
- **Pièces lues, et elles seules** (dossier P = `docs/notes/barreau5-resolution-v1/plan-avant-entretien/`) : P/`devis-garde-activations-volume-v2.md` (`8112974b…`) ; sa vérification P/`verification-devis-garde-activations-volume-v2-v1.md` (`80954295…`) ; son erratum 1 (`e891bca4…`, mal formé, laissé tel quel) ; sa contre-lecture P/`contre-lecture-devis-garde-activations-volume-v1.md` (`1d0e7861…`) ; le mandat P/lecture/`mandat-session-lecture-b5f-v2.md` (`b1eb2afc…`), § 5.4 et § 8, et ses errata 1 à 3 ; le texte scellé, lignes 363 à 368 (« Données gardées ») seulement ; le code figé au commit `c76e79169` : `scripts/amorce_b5f_lecture_v1.sh`, `scripts/lancer_b5f_lecture_v1.sh`, et, de `src/controle_ia/barreau5_familles/relecture_v1.py`, ce qui touche l'écriture et l'inventaire des activations, la règle de garde, la commande de création et la destruction ; `src/controle_ia/manifeste.py` au même commit (fonction `generateur`, pour le repli « une sur dix ») ; `registres/go.md` (ligne de l'accord) ; `registres/arrets.md` (lignes Hetzner, pour la pratique) ; `.claude/hooks/garde_calcul.py` ; le client du loueur installé (`vastai` 1.11.2, `.venv`), fonctions `copy`. Aucun score, aucun résultat, aucune table d'étiquettes, aucun sel.

## 0. Ce que fait l'amorce figée sous « trois_couches » (constat sur le code, commit `c76e79169`)

1. La marche écrit les activations sous `/root/b5f-lecture-v1/depot/donnees/<marche>/activations/<série>/c{7,15,23}/<tâche>__p<pas>.npy`, puis `donnees/<marche>/inventaire-activations.json` (forme `{"fichiers": [{"chemin", "octets", "sha256"}]}`, chemins relatifs à `donnees/<marche>/`) et `garde-activations.json`, chacun avec son compagnon `.sha256` (`relecture_v1.garde_des_activations`).
2. Au versement, l'inventaire des activations sort avec les fichiers fermés (`sorties_fermees`), entre dans l'inventaire final `traces-b5f-lecture/inventaire-final.json`, et est prouvé (poussé, relu à la taille et à l'empreinte) : ligne de journal « versement des sorties prouvé : … au commit C ». **C est le commit prouvé** de cette procédure.
3. Les activations, elles, ne sortent pas : signal « activations gardées par la règle trois_couches, à verser sur le volume accordé (nœud 4) … aucune destruction avant ce versement ». Le témoin final n'est pas écrit ; la ligne « versement final prouvé » **n'apparaît pas** ; la minuterie de l'instance, à son échéance, demande l'état « stopped » par l'identifiant, sans détruire (disque gardé).
4. L'instance est créée avec `--entrypoint bash --args -c "… bash /root/amorce_b5f_lecture_v1.sh"` : pas de service SSH, pas de script de démarrage du loueur. À un redémarrage, le conteneur rejouerait l'amorce, qui sortirait aussitôt en refus (« échéance d'arrêt passée », avant toute écriture) : **un redémarrage ne donne aucun accès** (§ 5, option a).

## 1. La procédure en douze gestes

| | geste | où | garde (programme) |
|---|---|---|---|
| 1 | accord en période ; ligne d'engagement inscrite par la mère | session | `accord` |
| 2 | preuve de l'inventaire au commit prouvé, sans affichage | session | `preuve-inventaire` |
| 3 | état de l'instance arrêtée, liste réduite ; délai de 72 heures | session | `reduire-liste vast`, `echeance-vast` |
| 4 | projection de dépense de la part volume | session | `garde-depense` |
| 5 | clé SSH jetable et pare-feu ; volume (protégé contre la suppression) ; serveur | session et poste | `corps-*`, `protection-volume` |
| 6 | minuterie du serveur, PID consigné | session | `minuterie_serveur_v1.sh` |
| 7 | sonde : copie du seul inventaire, empreinte comparée | serveur | `demande_rsync_vast_v1.py` (SONDE=1) |
| 8 | tirage des ≈ 152 Go | serveur | `demande_rsync_vast_v1.py` |
| 9 | vérification de chaque fichier par son empreinte | serveur | `verifier-copie` |
| 10 | destruction de l'instance par son identifiant, absence prouvée | session | `detruire-vast`, `verifier-absence` |
| 11 | destruction du serveur, de la clé et du pare-feu ; volume détaché, gardé | session | `detruire-serveur`, `supprimer`, `verifier-absence` |
| 12 | lignes des registres rédigées ; la mère les verse | session | — |

Programmes : dossier `transfert-activations-v1/` à côté de cette pièce (§ 12). Chacun refuse avec le code 2 et un motif ; `garde-depense` et `echeance-vast` rendent le code 3 à la coupure.

## 2. Qui fait quoi, et où

- **La session** (le conducteur, ou l'opérateur qu'il désigne) : tout ce qui passe par HTTPS — interface de Hetzner, interface du loueur, minuterie, gardes, registres. Clés lues **par leur nom seul** : `HCLOUD_TOKEN`, `VAST_API_KEY` ; jamais affichées, jamais écrites, jamais dans un message. Les commandes Hetzner imprimées passent le jeton à `curl` par l'entrée standard (`printf … "$HCLOUD_TOKEN" | curl -K -`) : `printf` est une commande interne du shell, le jeton n'apparaît dans aucune liste de processus ni à l'écran.
- **Le poste à SSH** : **cette session en nuage ne peut pas ouvrir de connexion SSH** (essai du 22 novembre à 19:30Z : `ssh` et `rsync` absents ; connexion au port 22 d'un hôte public refusée). Il faut donc une machine qui parle SSH : par défaut, **le poste local de Lazar**, joint par Remote Control, comme pour les essais Lean (`registres/arrets.md`, l. 95 à 151 : « poste local », clé SSH jetable et pare-feu supprimés en fin). Le poste ne reçoit aucune donnée : il pilote le serveur par `ssh -A` ; les octets vont directement de l'hôte du loueur au serveur. **Nœud pour la mère** (§ 11, Q1).
- **Le serveur de transfert** : un `cx23` à Helsinki (`ccx13` si `cx23` manque), nommé `b5f-transfert-v1`, étiquettes `programme=controle-ia`, `barreau=b5f`, `accord=GO-2026-11-22-117`, `piece=b5f-transfert-v1`. Il ne porte aucune clé du projet : ni jeton Hetzner, ni clé du loueur, ni jeton GitHub ; la clé SSH qui ouvre la copie chez le loueur reste sur le poste (agent transféré par `ssh -A`).
- **Le volume** : `b5f-activations-v1`, 200 Go, `hel1`, `ext4`, mêmes étiquettes avec `piece=b5f-activations-v1`, **protégé contre la suppression** dès sa création (`change_protection`, `delete: true`) : sa suppression demande le mot de Lazar (devis v2, § 5, point 3).

## 3. Avant toute création

Variables du geste (aucune clé) : `P=docs/notes/barreau5-resolution-v1/plan-avant-entretien/lecture/transfert-activations-v1`, `PY=".venv/bin/python -I"`, `W=<bloc-notes de l'opérateur>`, `ID=<identifiant de l'instance de relecture>`, `RUN=<AAAAMMJJ-HHMMSS-b5f-lecture>`, `C=<commit prouvé, 40 signes>`, `FIN=<fin de la relecture, AAAA-MM-JJTHH:MM:SSZ : heure de la ligne « fin, code … ; état « stopped » demandé » du journal>`.

1. **Accord** : `$PY $P/transfert_activations_v1.py accord registres/go.md $(date -u +%F)` — ligne unique, type « calcul », accordée par Lazar, jour dans la période. Le registre est lu par programme. (La garde de calcul du dépôt ne reconnaît que les numéros d'accord à deux chiffres : `GO-2026-11-22-117` n'y passerait pas pour un `vastai create|start`, que cette procédure n'emploie jamais ; `vastai destroy` n'est pas filtré par elle.)
2. **Ligne d'engagement** (§ 10) rédigée, inscrite par la mère **avant** la création du volume.
3. **Preuve de l'inventaire** : la branche de lecture récupérée par son nom entier vers une référence distante (`git fetch origin donnees/barreau5-familles-jumelles-v1-lecture:refs/remotes/origin/donnees/barreau5-familles-jumelles-v1-lecture`), jamais extraite. Puis `$PY $P/transfert_activations_v1.py preuve-inventaire . $C $RUN $W/preuve-inventaire.json`. Le programme lit par `git show`, sans rien afficher, trois fichiers du commit : l'inventaire des activations, son compagnon, l'inventaire final ; il exige que C soit sur `origin/donnees/barreau5-familles-jumelles-v1-lecture`, que le compagnon concorde, que l'inventaire final liste l'inventaire des activations à sa taille et à son empreinte, et que chaque chemin ait la forme d'une activation. Il imprime seulement : nombre de fichiers, total d'octets, empreinte de l'inventaire, commit. **Arrêt** si refus.
4. **Instance** : liste brute du loueur écrite dans `$W` sans être affichée, puis `reduire-liste vast` (identifiant, étiquette, états, prix de stockage, prix de sortie de données) ; l'instance `$ID` doit porter `b5f-lecture-v1` et être arrêtée. Délai : `echeance-vast $FIN $(date -u +%FT%TZ)` ; code 3 = délai dépassé → § 9.
5. **Dépense** (§ 8) : `garde-depense $W/etat-depense.json` avec `nouvelle_seance` ; « refusée » ou code 3 : aucune création.

## 4. Création, sous GO-2026-11-22-117

Chaque commande est imprimée par le programme, lue, puis jouée telle quelle ; chaque réponse est écrite dans `$W` et réduite par programme avant tout regard (identifiants, noms, états).

1. **Clé SSH jetable** (sur le poste) : `ssh-keygen -t ed25519 -N '' -C b5f-transfert-v1 -f <poste>/cle-b5f-transfert-v1` ; la partie publique seule part : `corps-cle-ssh <poste>/cle-b5f-transfert-v1.pub` → identifiant `K`. La clé privée ne quitte pas le poste.
2. **Pare-feu** : `corps-pare-feu <IPv4 publique du poste>` (entrée TCP 22 depuis cette seule adresse) → identifiant `F`.
3. **Volume** : `corps-volume` → identifiant `V` ; puis aussitôt `protection-volume $V`. L'interface dit qu'un volume ne s'attache qu'à un serveur du même lieu (référence de l'interface, « Create a Volume » : « a Volume can be attached to a Server only in the same Location as the Volume itself »).
4. **Serveur** : `corps-serveur cx23 $V $K $F` → identifiant `S` (si `cx23` est refusé faute de place à `hel1` : `ccx13`, même commande ; la garde de dépense est rejouée avec ce type). Volume attaché et monté à la création (`automount`).
5. **Minuterie, aussitôt** (§ 4 du devis : tenue hors du serveur, sans le jeton sur le serveur) : `nohup bash $P/minuterie_serveur_v1.sh $S $(( $(date +%s) + 12*3600 )) $W/minuterie-$S.txt > /dev/null 2>&1 &` puis `echo $!` → PID consigné. Échéance par défaut : **12 heures** (séance attendue du devis) ; le programme refuse au-delà de 24 heures. À l'échéance : DELETE par l'identifiant, puis relecture jusqu'au 404. Si la session qui la tient tombe, la session suivante détruit le serveur dès sa reprise (routine, point 4). La minuterie s'arrête par son PID seul (R10), jamais par motif.
6. **Contrôle du montage** (sur le serveur, par `ssh -A -i <poste>/cle-b5f-transfert-v1 root@<IPv4 de S>`) : `findmnt -no TARGET,SOURCE /mnt/HC_Volume_$V` et `df -B1 --output=avail /mnt/HC_Volume_$V` ; l'espace libre doit dépasser le total d'octets de la preuve d'au moins 3 % ; sinon **arrêt**, repli « couche 15 » (§ 9). Le point de montage `/mnt/HC_Volume_<id>` est l'usage de Hetzner, non vérifié sur page (§ 13) : `findmnt` le prouve.
7. Sur le serveur : `apt-get install -y rsync python3` si absents ; copie, depuis le poste, de `transfert_activations_v1.py` et de `preuve-inventaire.json` vers `/mnt/HC_Volume_$V/b5f-activations-v1/controle/` (`scp`), empreintes comparées des deux côtés.

## 5. Joindre les données de l'instance arrêtée

| option | ce qu'elle fait | coût | verdict |
|---|---|---|---|
| (a) redémarrer l'instance et y entrer par SSH | — | carte facturée à l'heure tant qu'elle tourne ; l'hôte peut avoir reloué la carte (« cannot be started ») | **écartée** : aucun service SSH (entrée remplacée par l'amorce), le conteneur rejoue l'amorce et s'arrête ; la garde de calcul bloquerait `vastai start` sous un accord à trois chiffres |
| (b) **copie par l'outil du loueur vers « local » = le serveur** | l'interface du loueur rend une adresse et un port de l'hôte ; rsync par SSH tire le dossier vers le serveur | sortie de données de l'hôte, au prix de l'offre ; entrée chez Hetzner (non vérifiée : supposée gratuite) | **retenue** |
| (c) copie vers un stockage en nuage du loueur (S3, Backblaze…) | — | autre ressource, autre compte | écartée : hors de l'accord, nœud |
| (d) copie d'instance à instance | — | une instance du loueur en marche comme destination | écartée : une carte de plus, hors de l'objet |

**Ce que dit la documentation du loueur** (lue le 22 novembre ; § 13) : les méthodes intégrées « offer ways to copy data to/from a stopped instance, with some constraints » ; pour la copie d'une instance vers « local », un extrait de recherche de leur page dit que « the remote instance must be on a machine with open ports (although the instance itself does not need open ports), and the remote instance can be stopped/inactive » — **phrase vue dans un extrait de moteur, absente de la page relue** ; « Copying data between instances accrues internet bandwidth usage charges » ; « Don't copy to /root or / as a destination » ; la copie « use[s] ssh authentication ».

**Ce que fait le client du loueur** (code lu, `vastai` 1.11.2) : `vastai copy C.<ID>:<chemin> local:<chemin>` envoie une requête à l'interface (`storage.copy`, `src_id="C.<ID>"`, `dst_id="local"`), reçoit `src_addr` et `src_port`, puis joue `rsync -arz … -e "ssh -p <port> -o StrictHostKeyChecking=no" vastai_kaalia@<adresse>::C.<ID>/<chemin> <destination>`. L'authentification est une clé SSH du compte du loueur.

**Comment la procédure l'emploie** : la session fait la requête (elle seule tient `VAST_API_KEY`) par `demande_rsync_vast_v1.py`, qui n'imprime que l'adresse, le port et la commande rsync à jouer **sur le serveur** ; la réponse brute n'est jamais imprimée. Le serveur joue rsync sous `ssh -A` depuis le poste : l'agent du poste porte la clé reconnue par le loueur, jamais copiée. **Non vérifié** : quelle clé le loueur accepte pour cette copie (une clé déjà inscrite au compte, ou une clé à inscrire, ce qui changerait le compte : nœud) ; la durée de validité de l'adresse et du port rendus (§ 11, Q2).

1. **Sonde d'abord** (quelques centaines de kilo-octets) : `SONDE=1 $PY $P/demande_rsync_vast_v1.py $ID $RUN /mnt/HC_Volume_$V` → commande rsync jouée sur le serveur ; puis `sha256sum` du fichier reçu (dans `sonde-$RUN/`, hors du dossier vérifié) comparé à l'empreinte de l'inventaire de la preuve. Égal : le chemin marche, la clé est acceptée. Différent ou refus : **arrêt**, rien de plus n'est tiré, nœud.
2. **Tirage** : même programme sans `SONDE` → commande jouée sur le serveur, de préférence dans `tmux` ou `nohup` (la connexion du poste peut tomber), journal sur le volume. `--partial` : une reprise ne retire que ce qui manque. Durée : le devis dit 0,5 à 1,7 heure à un débit supposé ; le disque du volume ne bride pas (l'hébergeur annonce 200 Mo/s soutenus, soit ≈ 13 minutes pour 152 Go) ; le débit réel de l'hôte n'est pas connu.
3. **Aucune lecture du contenu** : ni `ls` des dossiers d'activations, ni ouverture d'un fichier `.npy`, par un humain ou un agent ; rsync n'imprime que l'avancement et des comptes (`--info=progress2,stats2`) ; seuls des programmes lisent les octets, pour les empreintes.

**Coûts du loueur pendant ce temps** (hors du devis v2, qui ne les comptait pas) : instance arrêtée, ≈ 0,12 USD de l'heure (ordre de grandeur donné par la mère, à relever sur la liste réduite, champ `storage_cost`) ; sortie de données, ≈ 0,039 USD par Go sur l'offre relevée le 21 novembre (devis v2, § 7 ; unité du champ non vérifiée), soit **≈ 5,9 USD pour 152 Go, 6,5 pour 166**, à relever sur l'offre réelle (`inet_up_cost`). Sur quelle part de l'accord ces deux postes se comptent : **nœud** (§ 11, Q3).

**Risque que l'hôte ne soit plus disponible** : si la machine de l'hôte est hors ligne, la copie est impossible tant qu'elle l'est ; la procédure réessaie dans le délai de 72 heures, sans jamais détruire. Si l'hôte ne revient pas avant le délai, **rien n'est récupérable** : nœud pour Lazar (payer l'attente ou détruire), jamais une destruction d'office (§ 9).

## 6. Vérification de chaque fichier

Sur le serveur, après le tirage :

`python3 -I /mnt/HC_Volume_$V/b5f-activations-v1/controle/transfert_activations_v1.py verifier-copie /mnt/HC_Volume_$V/b5f-activations-v1/controle/preuve-inventaire.json /mnt/HC_Volume_$V/b5f-activations-v1/$RUN /mnt/HC_Volume_$V/b5f-activations-v1/controle/constat-1.json`

- Chaque fichier de l'inventaire prouvé doit être un fichier ordinaire (pas un lien), à sa taille et à son empreinte ; tout autre fichier sous le dossier est « en trop ». Le constat (chemin, statut) reste sur le volume et ne s'affiche pas ; l'écran ne porte que les comptes (conformes, manquants, taille, empreinte, liens, en trop), « complet oui/non » et l'empreinte du constat. Code 0 si complet, 3 sinon.
- Non complet : reprise du tirage (même commande, `--partial`), puis constat suivant sous un nom neuf (`constat-2.json` : on n'écrase jamais, R12), dans la limite du délai.
- Le constat complet est rapatrié sur le poste (`scp`), son empreinte comparée à celle imprimée, puis versé au bloc-notes de la session. Il porte les noms opaques des fichiers, aucune grandeur.

## 7. Destructions, dans cet ordre (R10, « récupérer ce qui est récupérable »)

1. **L'instance de relecture**, seulement sur un constat complet de tout l'inventaire prouvé : liste neuve du loueur, réduite (`reduire-liste vast`), puis `detruire-vast LISTE.json $ID $W/preuve-inventaire.json CONSTAT.json`. Le programme exige l'étiquette `b5f-lecture-v1`, un identifiant présent une seule fois, et un constat du même commit et du même inventaire, complet, sur tout l'inventaire. Il imprime `GO_ID=GO-2026-11-22-117 vastai destroy instance $ID -y`, jouée telle quelle. Puis liste neuve, réduite, et `verifier-absence LISTE_NEUVE.json $ID 58936096` : identifiant absent, **témoin présent** (une machine intouchable du mandat, § 8, lue sans y toucher). Une destruction ne se juge jamais par un code de sortie. Intouchables : 58936096, 58936099, 58936100, 60988826.
2. **Fin de séance sur le serveur** : `sync`, puis sortie. Aucun démontage n'est exigé : la destruction du serveur détache le volume (référence de l'interface, « Delete a Server » : « Any resources attached to the server (like Volumes, …) are detached while the server is deleted »).
3. **Le serveur** : liste neuve (`lister servers`, réduite par `reduire-liste hetzner-serveurs`), `detruire-serveur LISTE.json $S` (nom et étiquettes du transfert exigés), commande jouée, puis liste neuve et `verifier-absence LISTE_NEUVE.json $S <témoin>` ; si aucun autre serveur n'existe dans le projet, le témoin est la relecture `GET /v1/servers/$S` en 404, consignée. Puis la minuterie est arrêtée **par son PID** (`kill <PID>`), après lecture de son journal.
4. **Clé SSH et pare-feu** : `supprimer ssh_keys $K`, `supprimer firewalls $F`, chacun relu absent (`lister`).
5. **Le volume reste** : `lister volumes`, réduit : `b5f-activations-v1`, `server` vide, protection « delete » active. Sa suppression ne se fait que sur le mot de Lazar, après inventaire scellé (devis v2, § 5, point 3).

## 8. Garde de dépense et délais

- **Part volume, coupure à 24 USD** (taux de 1,25 USD pour 1 EUR, convention du registre des dépenses). `garde-depense` compte, toutes taxes, le volume au plafond mensuel entier pour chaque période de 30 jours entamée jusqu'à l'échéance de garde, chaque séance (heures écoulées ; pour un serveur vivant, jusqu'à sa minuterie) avec son adresse IPv4, et, si la mère les y range, les postes du loueur (`postes_vast.usd`). Objets de contrôle rejoués aux essais : le pire cas du devis (un mois, trois séances de 24 heures sur `ccx13`) rend **23,56 USD**, sous le plafond ; l'attendu (un mois, une séance de 12 heures sur `cx23`) **17,33 USD** ; une quatrième séance, un serveur oublié un mois, un deuxième mois, ou un mois plus 72 heures d'instance arrêtée (8,64 USD) rendent la coupure.
- **Conséquence chiffrée** : si l'instance arrêtée et la sortie de données se comptent dans la part volume, elles n'y tiennent pas avec un mois de volume (17,2 + 6 à 8,6 > 24). Il faut soit les compter ailleurs (part relecture ou plafond commun), soit raccourcir la garde du volume. **Nœud** (§ 11, Q3).
- **Instance arrêtée : 72 heures au plus** après `FIN`, ≈ 0,12 USD de l'heure (8,64 USD au plus). `echeance-vast` rend le temps écoulé, le temps restant et le coût estimé ; code 3 au-delà.
- **Échéance de l'accord** : GO-2026-11-22-117 court jusqu'au **30 novembre 2026** ; le devis v2 garde le volume jusqu'au 21 décembre. Toute création après le 30 novembre est refusée par `accord`, et la garde du volume au-delà du 30 novembre demande que la mère le porte à Lazar (§ 11, Q4).
- **Après la dernière séance** : relevé de la facture par identifiants (volume, serveur, adresse), versé au registre des dépenses.

## 9. Replis

Ordre du texte scellé (« Données gardées ») : (1) la couche 15 seule (≈ 44 Go) si un lieu de cette taille existe ; (2) une action sur dix, couche 15 (≈ 4,4 Go), « en morceaux sur la branche de lecture ». La mère a demandé, à 72 heures : « verser ce que une_sur_dix aurait versé, puis détruire ».

- **Volume plein, ou tirage entier impossible dans le temps, le volume existant** : `selection couche_15 $W/preuve-inventaire.json $W/selection-couche-15.txt`, tirage restreint à cette liste (`rsync --files-from=<liste>` ajouté à la commande imprimée, liste copiée sur le serveur, chaque chemin privé de son préfixe `activations/`, puisque la source rsync est le dossier `activations/` lui-même), constat sur la sélection (`verifier-copie … selection-couche-15.txt`).
- **Délai de 72 heures atteint sans constat complet** : `selection une_sur_dix $W/preuve-inventaire.json $W/selection-une-sur-dix.txt MANIFESTE.json`, où `MANIFESTE.json` est `runs/$RUN/manifeste.json` lu au commit prouvé par `git show`, sans affichage. Le calcul est celui de la marche figée (graine `b5f/tirages/garde-activations`, contrôle de la graine reconstruite) ; les essais le comparent au code figé exécuté (§ 12). Les fichiers choisis sont tirés et prouvés (constat sur la sélection), puis `detruire-vast … --repli SELECTION.txt $FIN <maintenant>` : le programme exige le délai atteint et un constat complet de cette sélection.
- **Où va la sélection « une sur dix »** : sur le volume s'il existe (c'est le lieu accordé) ; sinon, le texte scellé dit « en morceaux sur la branche de lecture », ce que ni le serveur (sans jeton GitHub) ni cette session (sans SSH) ne peut faire sans un geste de plus : nœud (§ 11, Q5).
- **Hôte hors ligne au délai** : rien n'est récupérable ; aucune destruction d'office ; nœud pour Lazar.

## 10. Lignes de registre à rédiger (la mère les verse ; 600 signes au plus)

- **Dépenses, engagement** (avant le volume) : « engagement : barreau 5, garde des activations (GO-2026-11-22-117, part volume 24 USD, échéance de l'accord 30 novembre) : devis devis-garde-activations-volume-v2.md (8112974b…), erratum 2 ; procédure procedure-transfert-activations-b5f-v1.md ([empreinte]) ; volume b5f-activations-v1, 200 Go, hel1, 0,0572 EUR hors taxe par Go et par mois ; serveur b5f-transfert-v1 [type], minuterie [12] heures, PID [n] ; instance de relecture [ID] arrêtée depuis [FIN], ≈ [storage_cost] USD de l'heure, 72 heures au plus ; sortie de données ≈ [x] USD, comptée sous [part à dire] ; cumul de la part avant : [y] USD ».
- **Dépenses, relevé** (à chaque fin de séance) : « relevé : barreau 5, garde des activations : volume [V] depuis [date], serveur [S] [heures] h, adresse IPv4 ; instance [ID] arrêtée [h] h ; sortie [Go] Go ; cumul de la part [z] USD sur 24 ».
- **Arrêts, instance** : « [date] | loueur [ID] (b5f-lecture-v1) | détruite par son identifiant après transfert prouvé : constat [empreinte], [n] fichiers conformes sur [n], commit prouvé [C court], inventaire [empreinte courte] ; absence relue, témoin 58936096 présent | conducteur de la lecture, GO-2026-11-22-117 ».
- **Arrêts, serveur** : « [date] | Hetzner [S] (b5f-transfert-v1, [type], hel1) | détruit par son identifiant ; clé [K] et pare-feu [F] supprimés ; minuterie PID [n] arrêtée par son PID ; volume [V] détaché, gardé, protégé ; absence relue ([liste ou 404]) | … ».
- **Volume** (état vivant, par la mère) : « volume b5f-activations-v1 [V], hel1, 200 Go, [n] fichiers, constat [empreinte] ; protégé ; question à Lazar le [date] ».

## 11. Questions ouvertes pour la mère

1. **Poste à SSH** : cette session en nuage n'a ni `ssh` ni `rsync`, et le port 22 sortant est refusé. Faut-il le poste local de Lazar (Remote Control), comme pour les essais Lean, ou une autre voie ? Sans machine qui parle SSH, la procédure ne peut pas tirer les données.
2. **Clé reconnue par le loueur** : le poste a-t-il une clé SSH déjà inscrite au compte du loueur ? Sinon, inscrire une clé jetable puis la retirer change le compte : nœud. À relire par la liste des clés du compte, en lecture seule, avant tout.
3. **Sur quelle part comptent l'instance arrêtée (≤ 8,64 USD) et la sortie de données (≈ 6 à 6,5 USD)** : la part relecture (9 USD, déjà serrée), la part volume (24 USD : elle n'y tient pas avec un mois de volume), ou une ligne neuve ? Le devis v2 ne les comptait pas ; son § 4 renvoyait la sortie au plafond commun de GO-2026-11-19-86.
4. **Échéance** : GO-2026-11-22-117 finit le 30 novembre, le devis garde le volume jusqu'au 21 décembre (question à Lazar le 14 décembre). Le volume peut-il rester après le 30 novembre sous cette ligne, ou faut-il un mot de Lazar avant ?
5. **Repli « une sur dix »** : sur le volume (lieu accordé), ou sur la branche de lecture comme le dit le texte scellé ? Et l'ordre du texte (couche 15 d'abord) prime-t-il sur la formule « une_sur_dix à 72 heures » ?
6. **La ligne « versement final prouvé »** n'apparaît jamais sous « trois_couches » (§ 0, point 3) : le mandat (§ 5.4, pas 9) en fait la condition de l'inventaire et de la destruction. Cette procédure prend pour commit prouvé celui de « versement des sorties prouvé » ; un erratum au mandat est à écrire.
7. **Relevé de prix** : `storage_cost` et `inet_up_cost` de l'instance réelle, et leurs unités, ne sont pas vérifiés.

## 12. Programmes et essais

Dossier `transfert-activations-v1/` :
- `transfert_activations_v1.py` — gardes et commandes imprimées (bibliothèque standard ; numpy pour « une sur dix » seulement) ; aucun réseau.
- `demande_rsync_vast_v1.py` — la seule requête au loueur (adresse et port de copie), lue par le client installé ; imprime la commande rsync pour le serveur.
- `minuterie_serveur_v1.sh` — minuterie de destruction du serveur, par identifiant, jugée par le 404 relu.
- `essais_transfert_activations_v1.py` — **76 essais**, tous verts au 22 novembre 2026 vers 19:42Z, sur processeur, sans réseau : `PYTHONPATH=src .venv/bin/python -m pytest -q -p no:cacheprovider <dossier>/essais_transfert_activations_v1.py`. Chaque garde a son cas sain et ses artefacts : accord (hors période, type, accordant, double, absent ; ligne réelle du registre lue) ; preuve (commit hors branche, compagnon discordant, inventaire final discordant, chemin hors forme, double, arguments) ; copie (manquant, octet changé, taille, lien, fichier en trop, sélection hors inventaire) ; sélections égales à `garde_des_activations` du commit figé, exécutée hors de son module, et graine altérée refusée ; corps (type, identifiants, clé privée, adresse privée) ; jeton jamais dans une commande ; liste réduite sans clés ; destructions (étiquette, double, constat incomplet, autre commit, autre inventaire, sélection, repli avant le délai) ; absence (présent, témoin absent) ; dépense (objets du devis) ; délai ; minuterie contre un faux `curl` (destruction jugée par le 404, jamais par le code ; refus sans jeton, au-delà de 24 heures ; jeton jamais au journal ni dans les arguments).
- **Ce que les essais ne touchent pas** : l'interface réelle du loueur (forme de la réponse de copie, acceptation de la clé), l'interface réelle de Hetzner, rsync réel. La sonde du § 5 est l'épreuve réelle du chemin, avant tout tirage.

## 13. Ce que je n'ai pas pu vérifier

- **Loueur** : pages `docs.vast.ai/documentation/instances/data-movement`, `docs.vast.ai/guides/instances/storage/data-movement` et `docs.vast.ai/cli/reference/copy` lues le 22 novembre par un outil de lecture (non versées sous empreinte) ; la contrainte « machine with open ports » vient d'un extrait de moteur de recherche, non retrouvée sur la page ; aucune page ne dit le prix du stockage d'une instance arrêtée, ni la validité de l'adresse rendue, ni quelle clé SSH est acceptée. Le mécanisme de copie est lu dans le code du client 1.11.2, non éprouvé.
- **Hetzner** : la référence de l'interface (`https://docs.hetzner.cloud/cloud.spec.json`, relevée le 22 novembre à 19:29Z, sha256 `3f90e2a03d37da90cde0b14744419bde101bb20829d0d870c0c3b95c5b3d1225`, non versée : 3,5 Mo) donne les corps de création, le lieu commun du volume et du serveur, le détachement à la destruction du serveur, la protection contre la suppression, la taille de 10 Go à 10 To ; la page « Volumes » de la documentation donne 200 Mo/s soutenus. **Non vérifiés** : la facturation d'un volume détaché (le devis le suppose, § 10, pas 5), la gratuité du trafic entrant, le point de montage `/mnt/HC_Volume_<id>`, la disponibilité de `cx23` à `hel1` ce jour.
- **Coûts du loueur** : 0,12 USD de l'heure à l'arrêt et 0,039 USD par Go de sortie sont des ordres de grandeur (mère ; devis v2, § 7), à relever.
- **Durée du tirage** : débit de l'hôte inconnu.
