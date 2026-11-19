# Contre-lecture de l'inventaire par instantané v5 (classe B : instrument), puis vérification de la v6

Contre-lecteur : sous-agent neuf d'un autre modèle que l'auteur (Fable ; auteur : la session attaquant informé,
Opus 5.5), 19 novembre 2026. Rapports rendus à la session et versés ici par elle (règle « les agents écrivent dans leur
bloc-notes, la session verse »). Transcription fidèle et resserrée ; aucune valeur de clé, aucun fichier du dépôt modifié
par le contre-lecteur, aucun refus de classifieur.

## 1. Contre-lecture de la v5 (rendue vers 15:22Z)
Pièces vérifiées par empreinte :
- `inventaire-instantane-v4.sh` `e97cf531…` et `inventaire-instantane-v5.sh` `f22b10e2…` ;
- `construire-donnees-inventaire-instantane-v4.py` `57fe0cc4…` et `construire-donnees-inventaire-instantane-v5.py` `99cdce18…` ;
- `instantanes-postes-v2.json` `2e4b56de…` et `sauvegarde-v2-creation.json` `7d3e31c3…` ;
- `sauvegarde-sondes-hetzner-v2.sh` `d60feb03…`, égal au champ `script_sans_secrets_sha256`.

**C1, bloquant.** Le script de la sauvegarde finit par `shred -u /root/.ssh/vast /root/.ssh/deploiement` (l. 101), et ses
deux sorties de boucle y mènent ; l'instance 60480302 est détruite depuis le 15 novembre. Les deux clés ne sont donc très
probablement plus sur le disque copié. Conséquence : la v5 sort en refus à l'étape « classement », et `refus()` ne
pousse rien faute de clé lisible ; serveur payant, aucune marque, aucune trace sur la branche. Correction proposée : pour
le genre « sauvegarde », lire les clés dans `/var/lib/cloud/instances/$POSTE/user-data.txt`, chacune devant donner au
moins une valeur (R5) ; pousser avec la clé de déploiement extraite ; ajouter les clés encore sur le disque ; dire la
source dans la marque. À vérifier : l'inscription en écriture de la clé de déploiement `diag-temoin-bailey-depot-20261115`.

**C2, moyen.** Le refus reste invisible quand la clé de déploiement manque (hérité de la v4) ; sur ce disque, c'est le
chemin attendu. Correction : celle de C1, plus un délai d'opérateur écrit, au-delà duquel le serveur d'inventaire est
éteint par identifiant et l'échec consigné.

**C3, mineur.** Libellés « poste » pour une sauvegarde, genre absent de la marque de refus.

**C4, mineur.** La règle « au moins une valeur par source » est plus stricte qu'en v4 : c'est un durcissement, sans cas
concret.

Contrôlés sans écart : cinq blocs remplis chacun une fois ; nom de 38 caractères ; 24 038 octets ; lieu `nbg1` ; heure
d'arrêt conforme à la table ; dossier d'instance attendu ; dépôt `/root/depot` ; secrets de `/root/.ssh/` et
`/var/lib/cloud/` nommés sans empreinte ; un seul journal versable, `/root/sauvegarde-v2.log`. Essais locaux A à I
(constructeur, refus, non-régression des postes, genres, module de contrôle, clés absentes, `refus()` sans clé).
Verdict : **écarts** ; le constructeur v5 est conforme.

## 2. Vérification des corrections, v6 (rendue vers 15:30Z)
Pièces : `inventaire-instantane-v6.sh` `26653fa0…` et `construire-donnees-inventaire-instantane-v6.py` `c87c57f5…`,
chacune égale à son compagnon ; les v5 sont inchangées.

| Constat | État |
|---|---|
| C1 | corrigé. Extraction après les gardes de forme ; `CLE_POUSSEE` dans `refus()` et à la poussée ; `source_cles` dans la marque. Essais : clés factices ed25519 et RSA 3072 ressorties identiques octet pour octet, en 0600, acceptées par `ssh-keygen -y`, chargées dans le contrôle ; `/run` hors du parcours |
| C2 | corrigé avec réserve. Le refus reste muet si l'extraction échoue avant d'écrire la clé de déploiement, si `user-data.txt` manque, ou si la clé n'est plus inscrite sur GitHub. Seul le délai d'opérateur (25 minutes) couvre ces cas ; les inventaires v4 ont fini en 92 à 119 s |
| C3 | corrigé |
| C4 | gardé, comme durcissement |

Constats nouveaux, mineurs :
- **N1** : avant de consigner un échec, éteindre d'abord le serveur par son identifiant, puis relire la branche (la boucle
  de poussée peut réessayer une heure).
- **N2** : hérité de la v4. Une dernière ligne de clé de moins de 40 caractères n'entre pas dans les valeurs exactes ;
  observée quand même relevée comme douteuse, par une règle non établie.
- **N3** : un échec sur la clé `vast` après l'écriture de la clé de déploiement donne un refus visible.
- **N4** : non établi. Présence de `user-data.txt` sur le disque copié ; inscription de la clé de déploiement.

Verdict : **conforme, avec réserves** ; rien de bloquant introduit par la v6.

## 3. Suite donnée par la session
- La v6 est employée.
- Délai d'opérateur : 25 minutes après la création. À l'échéance, application de N1 : arrêt par identifiant, puis
  relecture de la branche, puis consignation et rapport à Lazar.
- N2 et N4 sont acceptés comme réserves.
