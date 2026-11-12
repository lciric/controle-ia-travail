# Essai Lean D-1a — rapport de la session du poste local — v1

- **Consigne** : `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-1136-v1/consigne-poste-local-lean-d1a-v1.md`
  (`12793f76238db42300f0ec57d8cd03d32ab7b564f74367cd82df524a4891b456`, vérifiée aussi par `sha256sum -c` de son compagnon sur
  `origin/main`).
- **Procédure** : `procedure-poste-local-d1a-v6.md` (`9e7f51727dc3fd9a0385485ffb05e5eea3aa264d1280a2a090588665b2b4088b`).
- **Harnais** : branche `prep/lean-outillage-d1a-v6`, commit `149babdc56f51925e9bc4e93a61041cc755bd2a3` ; branche du poste
  `donnees/lean-outillage-d1a-poste-local-v1`, partie de ce commit.
- **Dépense** : GO-2026-11-10-13 seul. Aucun appel de modèle ; aucune clé de modèle ni dépôt du programme sur la machine.
- Toutes les heures sont relevées par `date -u`. Chemins relatifs au clone. Aucune adresse du poste ni du serveur dans ce
  rapport ni dans les pièces (adresse du serveur masquée en `<adresse du serveur>` dans une pièce ; `garde-poste --fichier`
  conforme sur chacune).

## Verdict

**Arrêt au premier pas de l'épreuve : `noyau` non conforme (0 cas réussi sur 18).** Cause unique, établie : les fichiers
compilés de Mathlib tirés du cache sont en mode `-rw-------` (propriétaire `chaine`) ; l'utilisateur `bac` traverse les
dossiers mais ne lit pas `Mathlib.olean` (G-L1 : « Permission denied »). Défaut de `scripts/lean_essai_d1a_v1/installer_chaine_v1.sh`
(changement de propriétaire sans droit de lecture pour les autres), **pas de l'isolement**. Conformément à la consigne, rien
d'autre n'a été lancé (ni épreuve, ni mesures) ; fin normale (section 5). Serveur détruit, inventaire vide, clé et pare-feu
supprimés. Coût : une heure facturée, 0,28 USD.

## Vie du serveur

| Élément | Valeur |
|---|---|
| Identifiant | 175751342 |
| Type, lieu | `ccx33`, `hel1` |
| Prix relevé à la création | 0,22596 EUR/h (serveur) + 0,00096 EUR/h (IPv4) = 0,22692 EUR/h ; 0,28365 USD/h au taux de 1,25 |
| Création | 2026-11-11T23:58:44Z |
| Échéance de la minuterie | 2026-11-13T20:35:28Z (`min(création + 48 h, H − 1 h)`), PID 1117 |
| Destruction demandée | 2026-11-12T00:24:07Z (`detruire --identifiant`, code 0, `detruit: true`) |
| Durée de vie | ≈ 25 min 23 s |
| Coût | 1 heure facturée : 0,22692 EUR ≈ **0,28 USD** (cumul de la minuterie : 0,28 USD) |
| Inventaire final | 00:24:09Z et 00:26:47Z : « aucun serveur de l'essai », `ips_primaires_non_attribuees` vide |
| Clé et pare-feu | `acces-supprimer` : 00:24:10Z code 1 (422 `resource_in_use`, pare-feu encore attaché pendant la suppression asynchrone du serveur) ; 00:26:45Z code 0 (pare-feu et clé supprimés) |
| Minuterie | `verifier-minuterie` conforme à L6 et à la fin ; arrêtée par son PID 1117 à 00:24:11Z (R10) |

## Déroulé

1. **Dépôt et routine** : clone neuf sous WSL (Ubuntu), identité `poste-local <poste-local@invalid>` pour ce clone seul ;
   `prep/lean-outillage-d1a-v6` récupérée par refspec ; branche du poste créée à `149babdc`. Routine de `CLAUDE.md` :
   `sha256sum -c sha256sums-lancement-v2.txt` conforme ; `verifier-arbre` **non lancé** (`docs/notes/bras-attaque/` extrait dans
   le clone : interdits communs v2, règle 9) ; `registres/etat.md` et la passation `2026-11-10-2206.md` lus, sans reprise de tâche.
2. **Section 0** : Python 3.14.4, OpenSSH 10.2p1. Essai à blanc : `sleep 900` détaché (PID 4368), `kill -0` réussi depuis une
   autre commande, puis **après fin et reprise réelles de la session** (hôte de la session relancé), puis `kill` par PID ;
   `getproxies()` rend `[]`, `getproxies_environment()` vide.
3. **L1** (2026-11-11T23:35:28Z) : `T_LIM` = 2026-11-12T05:35:28Z ; `H` = 2026-11-13T21:35:28Z.
   `preparer` code 0 : `rattrapage-machine-d1a-7b833a333f09-v1.json`, étiquette `7b833a333f09436c9b2164930cebcc14`.
4. **L2** (23:35:45Z) : clé ed25519 hors du dépôt ; `acces-creer` code 0 : clé 132500120
   (`5d:dc:6f:43:c1:d1:eb:8a:9c:5b:d5:87:29:e6:a0:b7`), pare-feu 12031843.
5. **L3** (23:36:14Z) : `garde-poste` conforme ; commit `2c08ce037d0b42fc471c391b046544ec0d648df0` poussé.
   Rattrapage `9a2f4d3c68d5b47a72278bbe56602f7ac757859ba96ecf61d0be10708fa27666`, accès
   `fb36d954d961647fa4e21155703bb804eb972e93c1174ef86a8b6230c38effbe`.
6. **Mot « armée »** reçu avec l'empreinte `9a2f4d3c…7666` (égale) ; tâches de la mère : T1 `trig_013NADgikL46HVvA5XCJUYmy`
   (H), T2 `trig_01BiwNZWFLwsbprdpdbvQxbb` (H + 30 min), T3 `trig_011VxYMdD2YSFpYqmWVUZY2G` (H + 24 h).
7. **L4** (23:40:37Z) : inventaire vide.
8. **L5, première** (23:41:23Z) : `GardeArret` **avant tout appel** : « rattrapage … non poussé (branche sans amont) ». Le clone
   court (`--single-branch`) n'avait aucune référence de suivi pour la branche du poste : `@{upstream}` ne se résolvait pas.
   Journal des créations v1 : une seule ligne d'arrêt, aucune intention. **Section 4** : `detruire --pas d1a` et `inventaire`
   à 23:42Z et 23:57Z : aucun serveur.
9. **L5, seconde et dernière** (23:58:41Z), **sur accord direct de Lazar** (« Mon accord », non de la mère), après réparation :
   `git fetch` par refspec puis `git remote set-branches --add origin <branche>` (configuration locale du clone) ;
   `fichier_pousse` vrai pour les deux fichiers ; L4 refaite (vide). Création 23:58:44Z, survie conforme.
10. **L6** (23:59:09Z) : `conforme: true`. **L7** (23:59:26Z) : commits `d156c260ea21b47d1824b5017efc432a0b147571` et
    `c39c586ed7a894918116b5f45da231bc71419062` poussés (journaux et sorties de création, PID, journal et sortie de la minuterie,
    journal des créations).
11. **Section 3, pilote « avant »** : quatre échecs à la première copie, sans effet sur le serveur (voir Incidents), puis
    essai 5 (00:14:40Z → 00:17:19Z) conforme : chaîne installée, réseau ouvert attendu, aucun écart.
12. **Coupure** (00:17:36Z) : règles de coupure du harnais (source SSH élargie au /24, voir Écarts) ; `verifier-coupure` code 0,
    pare-feu `applied`, seule règle sortante ICMP vers `192.0.2.1/32`.
13. **Pilote « après »** : essai 1 (00:18:08Z) arrêté à la sonde après coupure (faux positif de cache DNS, voir Incidents) ;
    essai 2 (00:20:49Z) : sonde conforme (aucun écart), vérificateur épinglé, **`noyau` non conforme** → arrêt.
14. **Section 5** : voir « Vie du serveur ».

## Valeurs des pièces (partie machine)

- **VERSION-LEAN** : `Lean (version 4.35.0, x86_64-unknown-linux-gnu, commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc, Release)` ;
  `lean-toolchain` `leanprover/lean4:v4.35.0` ; elan 4.2.4 (`227caca13`, 2026-08-25), `elan-init.sh` sha256
  `a620ff1641616222c8d37c54845492004bb84d6877cdbc944dd65c1aa685bf53`.
- **COMMIT-MATHLIB** : `56a005855ea17e0b0958f73ec801ae140b0a1679`, étiquette stable `v4.35.0`, choisie par
  `choisir_commit_mathlib_v1.sh` à 2026-11-11T23:41:48Z.
- **MACHINE** : Hetzner Cloud, `ccx33`, `hel1`, identifiant 175751342, 0,22692 EUR/h (0,28365 USD/h au taux de 1,25) ;
  Ubuntu avec systemd 255 ; bubblewrap 0.9.0, nftables 1.0.9 ; disque libre après installation 217 876 201 472 octets.
- **Mesures obtenues** (installation seulement) : cache de Mathlib (9 031 fichiers) téléchargé et décompressé en 72 s ;
  `lake build` de contrôle 6 s (9 046 tâches, rien reconstruit) ; tailles : Mathlib 7 737 489 290 octets (dont `.lake`
  7 102 771 403), elan 3 151 390 917, Python du bras S 296 111 793 (3.12.3) ; vérificateur du noyau épinglé
  `1f744a4d8addde8579b55c2970c456b829a244216f98e58a5144e627021efe28`.
- **Non mesurés** (arrêt au pas `noyau`) : temps d'un item jouet, mémoire à trois processus.
- **ESSAIS-R5 (partie machine)** : non joués au-delà de `noyau` : 18 cas (9 avec G-L3+, 9 sans), **0 réussi**, cause unique
  ci-dessus ; épreuve d'isolement non lancée.
- **Isolement** : sonde après coupure (essai 2) : TCP sortant jeté (1.1.1.1, 9.9.9.9, 8.8.8.8 : 443), DNS UDP refusé localement
  (EPERM), résolveur système fermé ; boucle locale ouverte (cas sain).

## Incidents

1. **WSL et poste** : chemins du dépôt interdits sous Windows ; tout sous WSL (Ubuntu), clone dans le système de fichiers
   Linux. Premier lancement d'Ubuntu (OOBE) fait par Lazar.
2. **Jeton de Hetzner** : absent de l'environnement de la session jusqu'à la relance de son hôte ; passé au seul processus WSL
   pendant l'essai à blanc, puis présent nativement. Jamais affiché ni écrit.
3. **Première L5** arrêtée par le harnais (branche sans référence de suivi, clone court) : section 4, aucune dépense.
4. **Adresse du poste** : le réseau du poste sort par au moins deux adresses IPv4 du même /24 (dont l'IP_POSTE donnée) ;
   le port 22 n'était joignable qu'≈ 1 fois sur 8 avec une règle à une seule adresse (pilote « avant » essais 1 et 4).
5. **Pilote, défaut** : `scp` (`C`) n'a pas `StrictHostKeyChecking=accept-new` et passe avant tout `ssh` ; sur un poste qui n'a
   jamais vu le serveur (et sans `~/.ssh`), « Host key verification failed » (essais 2 et 3). Contourné sans toucher au pilote :
   `~/.ssh` créé, clé d'hôte enregistrée par un `ssh … true` avec `accept-new` (ED25519
   `SHA256:nkbJqH5/NKzYgXLkaCG6n5GFSzJv/BqX1mBf2PeHATI`).
6. **Sonde après coupure, faux positif** (pilote « après » essai 1) : « résolveur système (example.com) : ouverte ». Diagnostic
   en lecture seule (00:19:47Z) : `example.com` et deux noms neufs non résolus, cache de `systemd-resolved` vide (43 succès de
   cache comptés) ; la réponse venait du cache rempli par la sonde « avant ». Pilote relancé (coupure idempotente,
   `flush ruleset`), sorties dans un dossier neuf.
7. **`noyau` non conforme** : voir Verdict ; diagnostic en lecture seule à 00:23:50Z
   (`apres-essai2-diagnostic-permissions-v1.txt`).
8. **`acces-supprimer`** : 422 `resource_in_use` juste après la destruction ; réussi 2 min 35 s plus tard.

## Écarts déclarés

1. Dépôt privé : le jeton de `gh` (compte `lciric`) passé au seul `git` (clone, fetch, push) et au processus de création
   (lecture `git ls-remote`, par `GIT_CONFIG_*`) ; jamais écrit ni affiché.
2. Commandes réseau hors du bac à sable de Claude Code (le bac à sable coupe GitHub).
3. `verifier-arbre` non lancé (règle 9).
4. **Seconde L5 sur accord direct de Lazar**, non de la mère (la procédure dit « aucun second essai »).
5. Configuration locale du clone : `git remote set-branches --add origin donnees/lean-outillage-d1a-poste-local-v1`.
6. **Règles du pare-feu reposées hors procédure** (accord de Lazar) : `regles_installation` du harnais d'abord avec l'adresse de
   sortie mesurée, puis avec la source SSH élargie au **/24** de l'IP_POSTE ; `regles_coupure` du harnais avec la même source
   /24, règle sortante inchangée. Nom du pare-feu relu avant chaque pose. Le trafic sortant reste coupé : l'épreuve n'en est
   pas affaiblie.
7. Clé d'hôte enregistrée par un `ssh … true` hors pilote ; `~/.ssh` créé dans WSL.
8. Deux lectures de diagnostic sur le serveur (DNS, permissions), sans aucune écriture.
9. Pilote « après » relancé une fois après le faux positif de cache.

## Propositions pour une version suivante (non appliquées)

- `installer_chaine_v1.sh` : rendre la chaîne et Mathlib lisibles par `bac` avant le montage en lecture seule (par exemple
  `chmod -R a+rX` sur `/opt/mathlib`, elan et le Python du bras S), et ajouter un essai R5 « `bac` lit `Mathlib.olean` ».
- `piloter_poste_v6.sh` : `StrictHostKeyChecking=accept-new` aussi dans `C` (scp), ou un premier `ssh … true`.
- `sonde_reseau_v1.py` : interroger le résolveur système sur un nom aléatoire jamais demandé (cache).
- Pare-feu : accepter une source en réseau (/24) quand le poste sort par une adresse partagée, avec une mesure préalable du
  nombre d'adresses de sortie.

## Lignes proposées (la mère les inscrit)

- `registres/depenses.md` : `2026-11-12 | GO-2026-11-10-13 | Hetzner ccx33 hel1, serveur 175751342, essai Lean D-1a (outillage) |
  2026-11-11T23:58:44Z → 2026-11-12T00:24:07Z, 1 h facturée | 0,22692 EUR ≈ 0,28 USD (taux 1,25) | poste local, branche
  donnees/lean-outillage-d1a-poste-local-v1`
- `registres/arrets.md` : `2026-11-12T00:24:07Z | Hetzner 175751342 (ccx33, hel1) | detruire --identifiant, code 0 ; inventaire
  vide 00:24:09Z et 00:26:47Z ; clé 132500120 et pare-feu 12031843 supprimés 00:26:45Z ; minuterie PID 1117 arrêtée |
  fin normale après « noyau » non conforme (lecture des .olean refusée à bac)`
- Ligne « en tâche jusqu'à » de `registres/etat.md` : à clore. T1 à T3 ne trouveront rien.

## Pièces versées

Sous `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/` :
- `rattrapage-machine-d1a-7b833a333f09-v1.json`, `acces-machine-d1a-7b833a333f09-v1.json` ;
- `journal-creations-machines-v1.jsonl`, `journal-creation-d1a-7b833a333f09-v1.jsonl` et `-v2.jsonl`,
  `sortie-creation-d1a-7b833a333f09-v1.log` et `-v2.log` ;
- `journal-destruction-d1a-7b833a333f09-v1.jsonl`, `-v2.jsonl`, `-v3.jsonl` ; `verification-coupure-d1a-7b833a333f09-v1.jsonl` ;
- `minuterie-d1a-7b833a333f09-pid-v1.txt`, `-journal-v1.jsonl`, `-sortie-v1.log` ;
- `pieces-poste-local-d1a-7b833a333f09-v1/` : journaux des pilotes (avant 1 à 5, après 1 et 2), coupure et sonde de chaque
  « après », vérificateur épinglé, premier pas `noyau`, diagnostic des permissions, journal du poste.
