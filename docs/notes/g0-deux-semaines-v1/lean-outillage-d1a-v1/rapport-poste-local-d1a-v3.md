# Essai Lean D-1a — rapport du poste local — troisième essai (v3)

- **Par** : la session fille du poste local de Lazar (Claude Code, Opus 5.5, `claude-opus-5-5`), sous la consigne
  `consigne-poste-local-lean-d1a-v5.md` (`427584c7f2c32a2521ce2fa9f3685295473f4791160ac1bc4ef2e34a863245bd`, sur `origin/main`
  `7fd65ddc`), session mère `session_01QPDgKgejkqwnuaJHJ31Ydo`.
- **Procédure** : `procedure-poste-local-d1a-v11.md` (`932b3bbc8f7741c8b18a99ba2384b56d70225bcb10af79cfcaa24d250e124e20`),
  branche `prep/lean-outillage-d1a-v10`, commit `ae894d8df2a19f51e532ff667160ae7bba2bf6ac` (correction E1 : point de départ de
  la branche du poste).
- **Branche du poste** : `donnees/lean-outillage-d1a-poste-local-v4`, partie de `ae894d8d`.
- **Dépense** : `GO-2026-11-10-13` (65 USD au plus, échéance 2026-11-30), troisième machine sous cette ligne, déclarée.
- Heures en UTC (`date -u` sous Ubuntu, ou heure de création Windows convertie). Aucune adresse ni aucun chemin du poste ici ;
  l'adresse du serveur loué est masquée (`<adresse-serveur>`).

## 1. Verdict du poste (lecture du poste, sans verdict de porte)

- **Pas `noyau` : conforme, 18 cas sur 18.** La réparation visée par le troisième essai tient sur la machine : le
  vérificateur v6 compile sous Lean 4.35.0 (essai R5, avant la coupure) puis rejoue et juge les 18 cas dans le bac
  (`bwrap`, `systemd`, `MemoryMax=6G`, `MemorySwapMax=0`), sans incident du bac, environ 4,3 à 4,7 s par passage.
- **Épreuve d'isolement : non conforme, 28 cas sur 34 (code 1).** Les 21 cas des gardes Lean, les 4 cas Python du bras S et
  3 limites sur 4 sont conformes. Écarts : **5 cas « isolement Lean » sans aucune tentative relevée** (l'item sonde sort en
  code 1 à la compilation en environ 0,4 s, avant toute tentative) et **le cas « temps de processus (5 s) »** (processus tué à
  5,01 s de temps processeur, fin `code=exited/status=137`, non classé « délai »).
- **Lecture proposée par le poste, soumise à la mère et à Fable (nœud, section 8)** : noyau et gardes Lean conformes sur la
  machine ; isolement Lean **non éprouvé** (ni prouvé, ni démenti ; aucun signe de brèche) ; isolement Python conforme ; limite de
  temps processeur effective, seul son classement manque.
- **Serveur détruit par son identifiant**, deux inventaires vides, clé et pare-feu supprimés, minuterie arrêtée par son PID.
  Coût : une heure facturée, environ 0,28 USD ; cumul sous `GO-2026-11-10-13` : 0,84 USD.

## 2. Vie du serveur et coût

| Pas | Heure | Fait |
|---|---|---|
| L1 `preparer` | 10:01:45Z | jeton `3f443896b5dc`, étiquette `3f443896b5dc4606a75889d3f1dac4af` ; `T_LIM` 2026-11-21T16:01:45Z ; `H` 2026-11-23T08:01:45Z |
| L2 `acces-creer` | 10:02:00Z | clé SSH 132903034 (`ff:e9:52:02:c5:99:e6:40:f9:25:ea:85:e7:d2:b9:c9`), pare-feu 12123398, `--prefixe-poste 32` |
| L3 poussée | 10:02:23Z | commit `e775ea53` ; empreinte du rattrapage poussé `6af8c205d5c6adb2611ca598037e394f2c5ca0ea03b7b4f25dfcda2980f384d2` |
| Mot « armée » | ~10:06Z | mère : empreinte égale ; M2 à M5 bis faits ; T1 `trig_01DAfWnJTRmTfTiQKhPnE5fN`, T2 `trig_01YRcbjtHAX3QtgR2NPCUAst`, T3 `trig_01PNFugpL4jEFnBEmXzyqzZN` ; ligne « en tâche jusqu'à 2026-11-23 07:01 UTC » (R-4506) |
| L4 `inventaire` | 10:08:02Z | aucun serveur de l'essai |
| L5 `creer-et-armer` | 10:08:21Z → 10:08:31Z | serveur **177067030** (`ccx33`, `hel1`) depuis **10:08:25Z** ; échéance 2026-11-23T07:01:45Z (44,9 h) ; minuterie PID 2109 ; survie : vivante, « garder » |
| L6 `verifier-minuterie` | 10:08:41Z | conforme |
| L7 poussée | 10:09:05Z | commit `68f8c5f0` (six pièces) |
| Pilote « avant » | 10:10:46Z → 10:13:34Z | code 0 |
| Coupure | 10:14:21Z | `acces-couper` code 0 ; `verifier-coupure` : v1 code 1 (« pending »), v2 10:15:35Z code 0 (« applied ») |
| Pilote « apres » | 10:15:56Z → 10:27:40Z | code 0 (épreuve en code 1, voir section 4) |
| Section 5 `detruire --identifiant 177067030` | **10:27:57Z** | code 0, « suppression demandée », 1 essai |
| `inventaire` 1 et 2 | 10:27:59Z, 10:29:09Z | aucun serveur de l'essai ; `ips_primaires_non_attribuees` vide (deux lectures, demande de la mère) |
| `acces-supprimer` | 10:28:09Z | clé et pare-feu supprimés (aucun 422) |
| `verifier-minuterie`, arrêt | 10:28:10Z, 10:28:17Z | conforme, dernière garde 10:27:31Z (cumul 0,28 USD) ; `kill 2109` après contrôle de sa ligne de commande (R10) ; arrêtée |

- **Vie** : 10:08:25Z → 10:27:57Z, environ 19,5 minutes ; **une heure facturée** d'une `ccx33`, 0,22692 EUR au taux de 1,25,
  **environ 0,28 USD** (minuterie : « cumul 0.28 USD »).
- **Cumul sous `GO-2026-11-10-13`** : 0,56 + 0,28 = **0,84 USD** sur 65 ; reste 64,16 USD.

## 3. Section 0

- **Dépôt** : clone neuf `--single-branch` dans le système de fichiers d'Ubuntu (WSL) ; `git remote -v` montre
  `lciric/controle-ia-travail` seul ; `fetch` par refspec de `prep/lean-outillage-d1a-v10` (= `ae894d8d`) ; `git ls-remote` de
  la branche v4 : code 0, aucune ligne (07:28Z, puis 09:27:15Z juste avant la création) ; branche poussée à 09:27Z à
  `ae894d8d`, référence de suivi posée. `V` sans `rattrapage-machine-d1a-*-v1.json` ni `journal-creations-machines-v1.jsonl`. La
  branche `donnees/lean-outillage-d1a-poste-local-v3` n'a été ni récupérée ni lue.
- **Empreintes** : procédure v11 conforme ; consigne v5 : `sha256sum -c` OK ; documents de lancement (routine, point 1
  limité) : OK. Routine, point 2 : `registres/etat.md` et la dernière passation lus sur `origin/main`.
- **Outils** : Ubuntu 26.04.1 ; Python 3.14.4 (seule version au moins égale à 3.11 sur le poste ; essais du harnais passés sous
  3.11 et 3.13 seulement) ; git 2.53 ; OpenSSH 10.2 ; `ssh-keygen`. `HCLOUD_TOKEN` présent, lu par son nom. Jeton de `gh` passé
  à `git` par l'environnement du seul processus.
- **Terminal WSL** : aucun ouvert au départ (Ubuntu s'arrêtait et redémarrait entre deux commandes, numéros de processus remis
  à zéro : le mécanisme de R-2434) ; terminal de Lazar ouvert à 07:41:34Z, Ubuntu démarrée à 07:41:26Z et jamais redémarrée
  ensuite (vérifié avant l'essai à blanc, avant L1 et jusqu'à l'inventaire final).
- **Essai à blanc** (point 4, preuve de relance selon D1) :
  - premier `sleep 900` (PID 1352, 09:29:24Z) : vivant à la seconde commande ; la relance réelle de l'application n'a eu lieu
    qu'après sa fin naturelle (09:44:24Z) ; **non compté** ;
  - second `sleep 900` (PID 1586, 09:46:06Z) : vivant à la seconde commande (09:46:18Z) ; application arrêtée par le
    Gestionnaire des tâches (arborescence du processus racine) puis rouverte ; **vivant à 10:00:03Z** ; hôte `claude.exe` créé
    à **09:59:00Z** (application 09:58:19Z), plus récent que le `sleep` : **conforme** ; `kill 1586` (R10) ;
  - `getproxies()` : `[]`.
- **Adresses de sortie** (10:00:34Z), code 0 : `essais 16, reponses 16, echecs 0, illisibles 0, adresses_distinctes 1,
  ip_poste_vue true, hors_du_24_du_poste 0, prefixe_conseille 32`. Rend 32 alors que les essais 1 et 2 avaient plusieurs sorties
  dans le même /24 : **signalé à Lazar avant L2** ; Lazar a retenu **`P` = 32** (la mesure). La connexion SSH du pilote n'a
  connu aucun échec avec ce préfixe.
- **Vérificateur** : `stat -c %a src/controle_ia/lean_essai/verificateur_noyau_v6.lean` = `644`.
- **Ordinateur** : sur secteur (vérifié 08:38Z), veille « jamais », capot « ne rien faire ».

## 4. Sorties des étapes de la machine

### Pilote « avant » (code 0)

- **Machine** : `ccx33`, `hel1` ; Ubuntu 24.04.4 LTS, noyau 6.8.0-138-generic ; 8 cœurs ; 32 857 436 160 octets de mémoire ;
  disque libre 217 862 053 888 octets.
- **Installation** (`installer_chaine_v2.sh`) : bubblewrap 0.9.0, nftables 1.0.9, systemd 255 ; `elan-init.sh` sha256
  `a620ff16…` ; elan 4.4.0 ; Mathlib `56a005855ea17e0b0958f73ec801ae140b0a1679`, `leanprover/lean4:v4.35.0` ; cache de Mathlib
  en 63 s ; `lake build` de contrôle (rien à reconstruire) 5 s ; Python du bras S 3.12.3.
- **Garde de lisibilité : conforme** — « aucun chemin fermé aux autres dans les trois arbres ; bac lit 16 chemins (dont
  Mathlib.olean) et exécute lean et python ».
- **Sonde v2 « ouverte »** : conforme, aucun écart (résolveur système sur nom aléatoire : « nom inexistant » revenu).
- **Essai R5 « bac lit Mathlib.olean »** : sain lu, témoin 0644 lu, artefact 0600 refusé ; bilan conforme.
- **Essai R5 « le vérificateur compile sur la machine »** : sain (`/root/verificateur_noyau_v6.lean`, sha256 `3ef23bfa…`) code 0
  **sans message** ; copie cassée refusée, code 1 (`error(lean.unknownIdentifier)`) ; bilan conforme.

### Coupure

- `acces-couper` : 2 règles posées (entrée SSH depuis `IP_POSTE/32` ; seule règle sortante ICMP vers 192.0.2.1/32, refus
  implicite du reste).
- `verifier-coupure` v1 (10:14:24Z) : code 1, pare-feu à l'état `pending` 3 s après ; v2 (10:15:35Z, lecture seule, journal
  neuf) : code 0, `applied`. Les deux journaux sont versés.
- Sur la machine (`coupure-v6.txt`) : table `inet coupure_d1a`, politiques `drop` en sortie, entrée et transit ; sortie
  permise vers `lo`, connexions établies, DHCP et métadonnées ; entrée permise sur `lo`, établies, port 22, DHCP.

### Pilote « apres » (code 0)

- **Sonde après coupure et sonde de fin** : « fermée », aucun écart (boucle locale ouverte ; TCP 443 vers 1.1.1.1, 9.9.9.9,
  8.8.8.8 sans réponse ; DNS refusé localement ; résolveur système sans réponse).
- **Vérificateur épinglé** : sha256 `3ef23bfa6600bf3a79fca2c31427dccf6c2ec7d67832bddb5c4df971a269d2ee`, identique à celui
  compilé avant la coupure (`cmp` passé).
- **Premier pas `noyau` : conforme, 18 sur 18**, avec et sans G-L3+ : sain (rejeu et aller-retour réussis) ; simproc hors noyau
  v5 (pré-procédure) pris et nommé par le rejeu ; `run_cmd` pris et nommé ; instance qui change le sens prise par
  l'aller-retour ; module `prelude` sans import refusé (CLC3-03) ; commentaire `/--/` (CLC3-01) ; nom à omicron (CLC3-06) ; deux
  relevés (code d'un simproc, tactique nommée d'Aesop, à la compilation). `incident_bac` nul partout ; aucun échec de mémoire
  ni de délai : **les relevés de la correction E2 sont sans objet**. Deux observations non jugées, dont « sous-terme de preuve
  dans l'énoncé (`pp.proofs` vrai) » : refusé par G-L5 (aller-retour en échec).
- **Épreuve d'isolement : non conforme, 28 sur 34.** Manifeste avant = après (`446c1316…`).

| Genre | Cas | Résultat |
|---|---|---|
| gardes Lean | 21 (G-L1 à G-L7, CLL-01 à CLL-04, CLC2-01, CLC3-06, initialiseurs) | 21 ok |
| isolement Lean | lectures hors du dossier ; écritures ; persistance (cas sain) ; persistance (rien pour l'item suivant) ; réseau pendant la compilation | **5 KO : toutes les tentatives « absente »** ; compilation code 1 en 0,36 à 0,42 s, noyau code 1 en 1,5 à 1,6 s ; `observe` vide |
| Python (bras S) | sain ; isolement ; persistance x2 | 4 ok |
| limites | mémoire 512M ; tâches 32 ; durée murale 10 s | 3 ok |
| limites | temps de processus 5 s | **KO** : tué à 5,011 s de processeur, fin `code=exited/status=137`, `incident_bac` nul au lieu de « délai » |

  Les tentatives sont lues dans la sortie de compilation de l'item sonde (`epreuve_isolement_v6.py`, l. 69, 127-130, 211) ; le
  texte de cette sortie n'est pas dans le JSON versé, la cause de l'échec précoce n'est donc pas établie ici. L'exécuteur ne
  classe en « délai » que si la fin contient « XCPU » (`executeur_bac_v6.py`, l. 160).
- **Mesures** (`sain_v1.lean`) : trois passages en suite, tous acceptés (compilation 4,40 à 4,67 s ; noyau 7,22 à 7,27 s) ;
  trois en parallèle : 11,73 s muraux (noyau 7,13 à 7,17 s chacun). **Réserve** : les pics de mémoire relevés par `systemd`
  (0,3 à 1,5 Mio, une fois 633 Mio) sont invraisemblables pour un passage Lean qui importe Mathlib (2,1 Gio de mémoire anonyme
  mesurés hors machine) ; la mesure ne voit probablement pas le processus Lean ; la mémoire à trois processus n'est pas
  établie.

## 5. Valeurs des pièces

- **VERSION-LEAN** : `Lean (version 4.35.0, x86_64-unknown-linux-gnu, commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc,
  Release)`.
- **COMMIT-MATHLIB** : `56a005855ea17e0b0958f73ec801ae140b0a1679` (taille 7 748 372 313 octets, dont `.lake` 7 102 801 866 ;
  elan 3 152 408 453 ; Python du bras S 296 111 793).
- **MACHINE** : Hetzner `ccx33`, `hel1`, serveur 177067030 ; Ubuntu 24.04.4 LTS ; noyau 6.8.0-138-generic ; 8 cœurs ;
  32 857 436 160 octets.
- **ESSAIS-R5 (partie machine)** : lecture par `bac` : conforme ; compilation du vérificateur : conforme ; pas `noyau` :
  conforme (18/18) ; épreuve : non conforme (28/34 ; 5 isolement Lean sans tentative, 1 classement du temps processeur).

## 6. Pièces versées

Sous `pieces-poste-local-d1a-3f443896b5dc-v1/`, chacune contrôlée par `garde-poste --fichier` (code 0). Les originaux restent
sur le poste, hors du clone ; la copie versée du journal « avant » masque une occurrence de l'adresse du serveur, les autres
sont identiques aux originaux.

| Fichier | sha256 de l'original | sha256 versé |
|---|---|---|
| `pilote-avant-v1.log` | `d7295b585876f194a2245daed8e651e120dd133c20a3dd9a6a93162a5ae1d9b7` | `02e90ce88cd75c84d0b158bb8f9df1613fb68e2d174be7059e8ff2dbe28b7da9` |
| `pilote-apres-v1.log` | `4389be264635effc0499b125182ae364fc02847b71a19611a23b2c8e9b668649` | identique |
| `coupure-v6.txt` | `ce8b426dce63634cebda1f41a38a9e6c650c6d313924eed139b934269e0077d5` | identique |
| `epreuve-code-v6.txt` | `3af27f893057c0bf80cbc215a9a33520bf7e3e7b02f2f5d8e4036461fc6fae9e` | identique |
| `epreuve-isolement-v6.json` | `c522409f8f416070f4ee10f18f4c75186b1c42deef42fbe1764e6da5b3059741` | identique |
| `installation-v6.txt` | `b55cdf64d3bd28106118004deb4c7b820132946da7aadfdc5a1611b6c96d51e6` | identique |
| `mesures-v6.json` | `59ecf52ae4af0f3ef04a20a80a398f97db2c83012691b9aebbaa00f78223a675` | identique |
| `premier-pas-noyau-v6.json` | `f0141a49b58dc9c556f9d5bb34072d57b5c24ad615e2cc141d9474cceb338ff1` | identique |
| `sonde-apres-coupure-v6.json` | `d1d37254b0568ede042a2cbcfdf7926c03b5c6b4018b0011412a1a333f541f65` | identique |
| `sonde-fin-v6.json` | `d1d37254b0568ede042a2cbcfdf7926c03b5c6b4018b0011412a1a333f541f65` | identique |
| `verificateur-epingle-v6.json` | `25bf1cdb27f10b74b31c5487d1332f359ec0d013aecd00387b8828e3a9f2f45e` | identique |

Dans `V` aussi : `verification-coupure-d1a-3f443896b5dc-v1.json` et `-v2.json`, `destruction-d1a-3f443896b5dc-v1.jsonl`, le
journal de la minuterie et le journal des créations à jour.

## 7. Incidents et écarts

Incidents :
1. Avant l'ouverture du terminal, Ubuntu s'arrêtait entre deux commandes (R-2434 observé ; sans conséquence, rien n'était
   lancé).
2. L'hôte de la session a été recréé sans geste de Lazar vers 08:49Z (application) ; Ubuntu a tenu.
3. Premier essai à blanc perdu par le délai fixe du `sleep 900` (fin naturelle avant le contrôle d'après relance).
4. Pare-feu à l'état `pending` 3 s après la coupure.
5. Épreuve non conforme (section 4) ; mesure de mémoire non fiable (réserve, section 4).

Écarts déclarés :
1. **D1** — preuve de relance par l'heure de création Windows du processus hôte `claude.exe`, comparée en UTC au départ du
   `sleep` dans Ubuntu (au lieu de `ps -o lstart`, qui ne voit pas l'hôte sous Windows) ; acceptée par Lazar, puis par la mère
   (R-4453, R-4456, R-4485).
2. **Adresse du poste lue par la session** (une requête au service de `adresses-sortie`, `https://api.ipify.org`) sur mot de
   Lazar (« Lis-la toi-même »), au lieu d'être donnée par lui ; jamais écrite dans un fichier.
3. **D2** — poussée de la branche v4 juste avant l'essai à blanc (et non au mandat 1), pour ne pas laisser une branche vide si
   la section 0 bloquait ; sans objet au final.
4. **Seconde lecture de `verifier-coupure`** (lecture seule, journal neuf) après « pending ».
5. **Deux inventaires** après la destruction (demande de la mère ; la procédure en demande un).
6. **Pièces du pilote versées en copies** où l'adresse du serveur est masquée (une occurrence), originaux sur le poste.
7. Clés de modèle transmises à Ubuntu par la variable `WSLENV` du poste : retirées de l'environnement de chaque commande du
   harnais (seuls `HCLOUD_TOKEN` et, pour `git`, le jeton de `gh`). Rien sur la machine.
8. Commandes lancées depuis l'hôte Windows par `wsl.exe -e`, depuis la racine du clone ; les processus détachés (création,
   minuterie, pilotes) vivent dans Ubuntu (`setsid` pour les pilotes).
9. Point 9 de « Avant de lancer » (ce qu'a fait la session du poste sur la branche v3) : question restée entre Lazar et la mère ;
   ce poste n'en sait rien.

Aucun refus de contrôle de permissions ni de classifieur. Aucune relance de minuterie, aucune seconde préparation, aucune
seconde création.

## 8. Nœud soumis à la mère (et à Fable)

Lecture de l'épreuve et suite à donner. Recommandation du poste : ne pas déclarer l'outillage D-1a « conforme » ; déclarer
« noyau et gardes Lean conformes sur la machine, isolement Lean non éprouvé, classement du temps processeur à corriger, mesure
de mémoire à refaire » ; avant tout quatrième essai, rejouer hors machine contre la chaîne épinglée les cinq items sondes de
l'isolement Lean (en lisant leur sortie de compilation) et le cas du temps processeur (fin 137 sous `LimitCPU`, ou
`SIGXCPU`), sous consigne neuve. Confiance : moyenne sur l'isolement Lean, haute sur le noyau, les gardes et la limite de
temps.

## 9. Lignes proposées pour les registres

- `registres/depenses.md` : 2026-11-21 — `GO-2026-11-10-13` — Hetzner `ccx33` `hel1`, serveur 177067030 (essai Lean D-1a,
  troisième essai, poste local), 10:08:25Z → 10:27:57Z, une heure facturée, environ 0,28 USD (0,22692 EUR au taux de 1,25) ;
  cumul sous ce GO 0,84 USD sur 65 ; branche `donnees/lean-outillage-d1a-poste-local-v4`.
- `registres/arrets.md` : 2026-11-21 10:27:57Z — serveur Hetzner 177067030 (`lean-outillage-d1a`, `ccx33`, `hel1`,
  `GO-2026-11-10-13`) détruit par son identifiant (fin normale, section 5) ; inventaires vides 10:27:59Z et 10:29:09Z ; clé
  132903034 et pare-feu 12123398 supprimés ; minuterie 2109 arrêtée par son PID à 10:28:17Z ; branche
  `donnees/lean-outillage-d1a-poste-local-v4`.

## 10. Rappel daté

`registres/rappels.md` : aujourd'hui, samedi 21 novembre, vers 18 h (Paris), rappel à Lazar de la lecture des trois sources du
jugement contre la surveillance (Hebbar 2025 ; Gasteiger et al. 2025 ; Gan et al., arXiv 2604.16286). Fait par le poste dans sa
conversation ; l'inscription au registre revient à la mère.
