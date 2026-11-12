# Essai Lean D-1a, second essai — rapport de la session du poste local — v2

- **Consigne** : `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/consigne-poste-local-lean-d1a-v2.md` sur `origin/main`
  (`af1d8ae3f5e8d4a405d3c874fe230acb48988c5000fd34c06b2314510189218d`, vérifiée avant lecture et par `sha256sum -c` de son
  compagnon).
- **Procédure** : `procedure-poste-local-d1a-v9.md` (`7f69fece209909cdc132a32529e6df6c795455cd380dbf9db495b45b1602b59e`), lue
  sur `origin/prep/lean-outillage-d1a-v7` (tête `b0b8667a`).
- **Harnais** : `prep/lean-outillage-d1a-v7`, commit `32a40613eb1ec006cbee4144e1ec94dfe84e8237` ; branche du poste
  `donnees/lean-outillage-d1a-poste-local-v2`, partie de ce commit.
- **Dépense** : GO-2026-11-10-13 seul (seconde machine sous cette ligne, R-2426). Aucun appel de modèle ; aucune clé de modèle
  ni dépôt du programme sur la machine.
- Heures relevées par `date -u`. Chemins relatifs au clone. Aucune adresse du poste, de son /24 ni du serveur dans ce rapport
  ou dans les pièces (adresse du serveur masquée dans une pièce ; `garde-poste --fichier` conforme sur chacune).

## Verdict

**Arrêt au premier pas de l'épreuve : `noyau` non conforme (0 cas réussi sur 18), cause neuve.** Le vérificateur du noyau
`src/controle_ia/lean_essai/verificateur_noyau_v4.lean` **ne compile pas sous Lean 4.35.0** :
`Unknown identifier CollectAxioms.collect` (l. 48, dans `axiomesDe`) et `Invalid field notation` (l. 49). La garde G-L7 échoue
dans tous les cas, et, par voie de conséquence, G-L2, G-L4 et G-L5 du cas sain. Le cas « simproc » échoue aussi à la
compilation de l'item (`Function._hors_noyau` absent de l'environnement, G-L1). **Défaut de compatibilité du harnais avec la
chaîne épinglée, pas de l'isolement.** Rien d'autre lancé (consigne) ; fin normale (section 5).

**Corrections du harnais v7 éprouvées sur machine réelle, toutes conformes** : garde de lisibilité (`bac` lit 16 chemins dont
`Mathlib.olean`, exécute `lean` et Python) ; essai R5 « `bac` lit `Mathlib.olean` » (sain, témoin 0644, artefact 0600
refusé) ; `scp` en `accept-new` et `ssh-keygen -R` préalable ; source SSH `/24` (P mesuré) ; référence de suivi et
`fichier_pousse` ; sonde v2 sur nom aléatoire et vidage du cache : réseau fermé sans écart après la coupure. La cause du premier
essai (lecture des `.olean`) a disparu.

## Vie du serveur

| Élément | Valeur |
|---|---|
| Identifiant | 175838427 |
| Type, lieu | `ccx33`, `hel1` (Ubuntu 24.04.4 LTS, noyau 6.8.0-137, 8 cœurs, 32 857 436 160 octets de mémoire) |
| Prix | 0,22692 EUR/h (serveur 0,22596 + IPv4 0,00096) ; 0,28365 USD/h au taux de 1,25 |
| Création | 2026-11-12T14:31:04Z (`creer-et-armer --deja-depense-usd 0.28`, L5 lancée 14:31:01Z) |
| Échéance de la minuterie | 2026-11-14T11:02:19Z (`H − 1 h`), PID 2441 |
| Destruction demandée | 2026-11-12T14:39:50Z (`detruire --identifiant`, code 0, `detruit: true`) |
| Durée de vie | ≈ 8 min 46 s |
| Coût | 1 heure facturée : 0,22692 EUR ≈ **0,28 USD** ; cumul sous GO-2026-11-10-13 : **0,56 USD** sur 65 |
| Inventaire | 14:39:52Z et 14:42:25Z : « aucun serveur de l'essai », `ips_primaires_non_attribuees` vide |
| Clé et pare-feu | `acces-supprimer` 14:42:23Z, code 0 du premier coup (pare-feu et clé supprimés) |
| Minuterie | conforme à L6 (14:31:33Z) et pendant le travail ; terminée d'elle-même à 14:40:09Z (« serveur absent, confirmée par deux lectures ») ; `verifier-minuterie` à 14:42:24Z : processus absent, attendu |
| Autre serveur du projet | 175834755 (`organisme-v67-course`, autre session) non touché |

## Déroulé

1. **Dépôt** (12:3x Z) : clone neuf sous WSL ; identité `poste-local` pour ce clone ; `prep/lean-outillage-d1a-v7` par refspec ;
   branche du poste à `32a40613`, `git push -u`, référence de suivi (`fetch` par refspec, `remote set-branches --add`),
   `@{upstream}` résolu ; `V` sans pièce du premier essai. Routine : `sha256sum -c sha256sums-lancement-v2.txt` conforme ;
   `verifier-arbre` non lancé (`docs/notes/bras-attaque/` extrait, règle 9) ; `registres/etat.md` et `2026-11-12-0519.md` lus.
2. **Section 0** : Python 3.14.4, OpenSSH 10.2p1 ; `HCLOUD_TOKEN` présent ; `getproxies()` `[]`,
   `getproxies_environment()` vide ; vérificateur en `644`.
   **`adresses-sortie`** (12:43:59Z) : 16 essais, 16 réponses, 0 échec, **2 adresses distinctes**, `ip_poste_vue`, 0 hors du
   /24 → **P = 24**.
   **Essai à blanc** : `sleep` PID 817 lancé 13:56:09Z ; `kill -0` réussi depuis une autre commande ; hôte de la session
   relancé (claude.exe 39200 terminé, nouvel hôte 41508 démarré 14:00:31Z, après le `sleep`) ; `kill -0 817` réussi
   14:01:52Z, puis `kill 817` (R10).
3. **L1** (14:02:19Z) : `T_LIM` 2026-11-12T20:02:19Z ; `H` 2026-11-14T12:02:19Z ; `preparer` code 0,
   `rattrapage-machine-d1a-84f813c9b330-v1.json`, jeton `84f813c9b33042ab95bdbb0fa3d607f2`.
4. **L2** : `acces-creer --prefixe-poste 24` code 0 : clé 132525089 (`88:45:54:74:12:c5:3b:4a:c5:e8:12:94:4b:84:0e:22`),
   pare-feu 12036919.
5. **L3** : `garde-poste` conforme (adresse, /24, dossier personnel, chemin du clone) ; commit
   `9196a99874b13d270cb7ee88b150c1ab46878c3e` poussé ; amont résolu ; `fichier_pousse` vrai pour les deux fichiers.
   Rattrapage `1ac1f180fc0533b2b49626d6b52bdc6196b68ef2f2df2ec3d564d0e5b388e7e4`, accès
   `fd76bee6d315e4652824638bc836848ef838d6b67a58160c100ee761db0424d8`.
6. **Mot « armée »** (R-2434) avec l'empreinte `1ac1f180…88e7e4` (égale) ; T1 `trig_01KLbFn2NCK4Zdc1DxKF3HE5`,
   T2 `trig_01XQbHnFNbCPttrW4W8oLwGF`, T3 `trig_01Eaze6ympX8U7abyyZXnFLj`.
7. **L4** (14:31:00Z) inventaire vide ; **L5** (14:31:01Z) création 14:31:04Z, survie conforme ; **L6** (14:31:33Z)
   conforme ; **L7** (14:31:37Z) commit `315951a62ec86a7621bbc2e8d07b417c9dd8288a` poussé.
8. **Section 3** : adresse du serveur déjà connue de `known_hosts` (3 lignes, adresse réattribuée) → `ssh-keygen -R`.
   **Pilote « avant »** v8 (14:31:59Z → 14:34:35Z) : installation conforme, garde de lisibilité conforme, sonde v2 « ouverte »
   sans écart, essai R5 « `bac` lit `Mathlib.olean` » conforme. **Coupure** (14:34:51Z, `--prefixe-poste 24`) ;
   `verifier-coupure` code 0, pare-feu `applied`, seule règle sortante ICMP vers `192.0.2.1/32`. **Pilote « après »**
   (14:35:19Z → 14:39:19Z, code 1) : sonde après coupure conforme (aucun écart), vérificateur épinglé, **`noyau` non
   conforme** → arrêt.
9. **Section 5** : voir « Vie du serveur ».

## Valeurs des pièces (partie machine)

- **VERSION-LEAN** : `Lean (version 4.35.0, x86_64-unknown-linux-gnu, commit eb6cafb7290e8bd5f2937522d8d804f58f02bafc, Release)` ;
  `lean-toolchain` `leanprover/lean4:v4.35.0` ; elan 4.2.4 (`227caca13`), `elan-init.sh` sha256
  `a620ff1641616222c8d37c54845492004bb84d6877cdbc944dd65c1aa685bf53` (identique au premier essai).
- **COMMIT-MATHLIB** : `56a005855ea17e0b0958f73ec801ae140b0a1679` (`v4.35.0`), gardé épinglé depuis le premier essai.
- **MACHINE** : Hetzner Cloud `ccx33`, `hel1`, identifiant 175838427, 0,22692 EUR/h ; Ubuntu 24.04.4 LTS, noyau
  6.8.0-137-generic, 8 cœurs, 32 857 436 160 octets ; bubblewrap 0.9.0, nftables 1.0.9, systemd 255.4-1ubuntu8.16.
- **Mesures obtenues** (installation) : cache de Mathlib (9 031 fichiers) en 65 s ; `lake build` de contrôle 6 s (9 046 tâches,
  rien reconstruit) ; Mathlib 7 737 547 107 octets (dont `.lake` 7 102 772 635), elan 3 151 390 917, Python du bras S
  296 111 793 (3.12.3) ; disque libre 217 876 484 096 ; vérificateur épinglé sha256
  `1f744a4d8addde8579b55c2970c456b829a244216f98e58a5144e627021efe28`.
- **Non mesurés** (arrêt au pas `noyau`) : temps d'un item jouet, mémoire à trois processus.
- **ESSAIS-R5 (partie machine)** : garde de lisibilité conforme ; « `bac` lit `Mathlib.olean` » conforme (3/3) ; `noyau`
  0/18 (9 avec G-L3+, 9 sans), cause ci-dessus ; épreuve d'isolement non lancée.
- **Isolement** : après la coupure (cache vidé), TCP sortant jeté (1.1.1.1, 9.9.9.9, 8.8.8.8 : 443), DNS UDP refusé
  localement (EPERM), résolveur système sans réponse sur un nom aléatoire ; boucle locale ouverte (cas sain).

## Incidents

1. **WSL arrête Ubuntu quand aucune fenêtre WSL n'est ouverte** : le premier `sleep` de l'essai à blanc (PID 466) est mort
   (redémarrage de la distribution visible à l'heure de `systemd`, `uptime -s` inchangé car il date la machine virtuelle).
   Parade : un terminal Ubuntu ouvert par Lazar jusqu'à la destruction. Un `wsl.exe` coupé par une borne, lui, ne tue pas les
   processus détachés (essai fait).
2. **Commandes bloquées par la capture du PID** (`PID=$(python3 … Popen(sleep))`) : le `sleep` hérite de la sortie de la
   substitution, qui attend sa fin. Deux commandes coupées, deux `sleep` égarés arrêtés par PID ; corrigé (PID écrit dans un
   fichier).
3. **Adresse du serveur déjà dans `known_hosts`** (3 lignes) : retirée par `ssh-keygen -R`, comme prescrit.
4. **`noyau` non conforme** : voir Verdict.

## Écarts déclarés

1. Jeton de `gh` passé au seul `git` (clone, fetch, push) et au processus de création (`git ls-remote`, par `GIT_CONFIG_*`),
   jamais écrit ni affiché (prévu par la procédure v9).
2. Commandes réseau hors du bac à sable de Claude Code.
3. `verifier-arbre` non lancé (règle 9).
4. Aucun autre : les règles du pare-feu et la clé d'hôte sont passées par le harnais.

## Propositions pour une version suivante (non appliquées)

- **Vérificateur du noyau** : porter `axiomesDe` vers l'interface actuelle de Lean (collecte des axiomes par
  `Lean.collectAxioms` en `CoreM`/`MetaM`), et vérifier les autres appels du fichier contre Lean 4.35.0 ; revoir l'item
  « simproc » (`Function._hors_noyau`).
- **Essai R5 neuf, avant la coupure** : compiler `verificateur_noyau_v4.lean` sur la machine (et un item sain jusqu'au
  vérificateur), réseau ouvert, comme « `bac` lit `Mathlib.olean` » ; non conforme : arrêt avant la coupure.
- **Essais hors machine** : compiler le vérificateur contre la chaîne épinglée (Lean et Mathlib au commit) dans les essais du
  harnais, pas seulement sur un faux transport.
- **Procédure, section 0** : exiger un terminal WSL ouvert (ou un réglage d'inactivité de WSL) jusqu'à la destruction ;
  vérifier l'heure de démarrage de `systemd` (PID 1) avant et après l'essai à blanc.

## Lignes proposées (la mère les inscrit)

- `registres/depenses.md` : `2026-11-12 | GO-2026-11-10-13 | Hetzner ccx33 hel1, serveur 175838427, essai Lean D-1a, second essai
  (outillage) | 2026-11-12T14:31:04Z → 14:39:50Z, 1 h facturée | 0,22692 EUR ≈ 0,28 USD (taux 1,25) ; cumul de la ligne
  0,56 USD | poste local, branche donnees/lean-outillage-d1a-poste-local-v2`
- `registres/arrets.md` : `2026-11-12T14:39:50Z | Hetzner 175838427 (ccx33, hel1) | detruire --identifiant, code 0 ; inventaire
  vide 14:39:52Z et 14:42:25Z ; clé 132525089 et pare-feu 12036919 supprimés 14:42:23Z ; minuterie PID 2441 terminée
  d'elle-même 14:40:09Z | fin normale après « noyau » non conforme (vérificateur incompatible avec Lean 4.35.0)`
- Ligne « en tâche jusqu'à 2026-11-14 11:02 UTC » de `registres/etat.md` : à clore. T1 à T3 ne trouveront rien.

## Pièces versées

Sous `docs/notes/g0-deux-semaines-v1/lean-outillage-d1a-v1/` :
- `rattrapage-machine-d1a-84f813c9b330-v1.json`, `acces-machine-d1a-84f813c9b330-v1.json` ;
- `journal-creations-machines-v1.jsonl`, `journal-creation-d1a-84f813c9b330-v1.jsonl`,
  `sortie-creation-d1a-84f813c9b330-v1.log` ;
- `minuterie-d1a-84f813c9b330-pid-v1.txt`, `-journal-v1.jsonl`, `-sortie-v1.log` ;
- `verification-coupure-d1a-84f813c9b330-v1.jsonl`, `journal-destruction-d1a-84f813c9b330-v1.jsonl` ;
- `pieces-poste-local-d1a-84f813c9b330-v1/` : journaux des pilotes « avant » et « après », coupure, sonde après coupure,
  vérificateur épinglé, premier pas `noyau`, journal du poste.
