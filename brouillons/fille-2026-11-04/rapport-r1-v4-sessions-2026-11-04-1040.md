# Rapport — R1 v4 (GO-2026-11-03-03) : session 1 (témoin) faite, session 2 refusée par Vast — 2026-11-04-1040 UTC (date -u)
Ordre : `docs/procedures/ordre-fille-r1-v4-lancement-v2.md` (a50a0cf5…), `main` 7fcb6cad. Texte scellé `prereg/R1-addendum-relance-v4.md` (0f10881b…), commit de scellement 937f1317. Fille `session_01Qi7Gr3s7JVgpRP17VcSyAf`.

## Session 1 — témoin
- **Étape A** (08:29Z) :
  - GO valide (60 USD, échéance 2026-11-17), dépense déjà imputée 0 ;
  - cinq sceaux OK ;
  - épreuves des gardes de dépense : corps identique à l'octet à la sortie de référence f2eb1d8f… ;
  - vastai 1.8.3 dans un environnement à part (`/home/user/venv-vastai`, l'outil `/opt/vastai-venv-v1` étant absent) ;
  - `show instances` : les trois R8 de Lazar actives, non touchées.
- **Offre** 44032502 : A100 SXM4 80 Go, Tchéquie, 1,1067 USD/h, stockage 0,24 USD par Go et par mois.
- **Création** : instance **59079406**, T0 **2026-11-04T08:30:40Z**. Disque estimé 1,32 USD ; H = 3 003,7 min ; heure de destruction 2026-11-06T10:34:22Z.
- **Tâches planifiées** :
  - (i) `trig_014NcHLP4khcwA2nLZHMfgKV` (minute 31 de chaque heure) ;
  - (ii) `trig_01RrnE8DvZ1FoaheUnQ96e6v` (run_once 2026-11-06T10:34:22Z) ;
  - `lire_prompt` et `exiger_armement` conformes.
- **Prompts réécrits deux fois** sur ordre de la mère. La première version (ligne de localisation seule) échouait : les sessions ouvertes par les tâches n'ont ni dépôt ni vastai. Le bloc « Moyens » (a) à (e) a été ajouté à 08:38Z, puis (f) à 08:45Z (aucune sortie brute de vastai, aucune clé écrite sur disque).
- **Tirs d'essai** :
  - (i) à 08:33Z : échec (pas de dépôt ni de vastai) ;
  - (i) réécrite à 08:39Z : « rien », engagé 1,55 USD, projeté 2,84 USD ;
  - tâche d'essai sans identifiant `trig_0131TNQw…` : vastai installé, listing rendu, rien détruit ; tâche supprimée.
- **Surveillance** filtrée toutes les 10 min (`--tests 381`) : en cours, puis « conforme » dès 09:13Z (session temoin, plafond 180, délai 120, tests 381). Fin lue à 09:23Z : « AMORCE 2026-11-04T09:20:50Z : fin, code 0 », `etape=fin`. Branche `calcul/r1-v4-temoin-reel-v1` à 28036be2.
- **Coupure** : ma session a été coupée par la limite d'usage d'environ 09:23Z à 10:23Z, conteneur repris. Le tir de (i) à 09:31Z a ÉCHOUÉ, `USAGE_LIMIT_REACHED`.
- **Destruction** : à 10:23Z, l'instance était « exited/stopped » (arrêtée par l'amorce en fin de plafond). Détruite par son identifiant vers 10:25Z. Le premier essai sans `-y` a été annulé par l'invite de confirmation de vastai ; le second, avec `-y`, a réussi. `show instances` ensuite : seulement les R8.
- **Tâches (i) et (ii)** supprimées.
- **Dépense estimée** : ≈ 0,96 USD (0,84 h en marche × 1,1067, plus ≈ 1 h de stockage arrêté). Borne haute 2,1 USD. Relevé exact à faire sur la facture Vast.
- **Versement B5** : commit **`5bd62a004279776c2718b3201c11001e16fa6527`** sur `prep/r1-relance-v4`, fils de 937f1317. Il ajoute seulement `runs/20261104-091009-r1-v4-temoin-reel/manifeste.json` (43e2dd5c…) et `diag/20261104-091009-r1-v4-temoin-reel/resolution-graine-lot-v3-temoin.json` (25d68f33…), avec leurs sceaux. Copiés à l'octet de 28036be2, sceaux OK, aucun `arret.json`, contenu non lu.

## Session 2 — réparation : tentative refusée
- **Étape A** au commit 5bd62a00 : arbre propre, cinq sceaux OK, épreuves identiques, table v4 absente.
- **Garde de destruction** : `destroy instance 1 -y` → « 404 Instance 1 not found », rien détruit.
- **Borne de création** (condition de la mère) : 2,1 + 36,75 × 1,1067 + 1,5 = **44,27 USD** ≤ 57.
- **Tâche d'essai de vérification** (session reparation, bloc « Moyens » (a) à (g), sans identifiant) `trig_018jarxh…`, tirée une fois (`cse_01Qi7Gr4vjNqgn84fVpD4zYD`, 10:31 → 10:37Z) : vastai installé, dépôt à 5bd62a00, `decision_horaire` → « echec_visible », listing filtré, rien détruit ; tâche supprimée.
- **Création** à 10:38:38Z, même commande que la session 1 (label r1-v4-reparation, TEMOIN_RUN=20261104-091009-r1-v4-temoin-reel, PLAFOND 2200, DÉLAI 2100) : **refusée**, HTTP 400 « Your account lacks credit; see the billing page. » Aucune instance, aucune tâche posée.

## Écarts et défauts constatés
1. `commande_destruction` du module scellé rend `vastai destroy instance <id>` sans `-y`. vastai 1.8.3 demande alors une confirmation et sort sur « Aborted » sans rien détruire. Contourné par le point (g) des « Moyens » et par `surveiller_r1v4_v2.sh` (50e8b991…).
2. Les tâches planifiées tombent sur la limite d'usage du compte (tir de 09:31Z) : elles ne sont pas indépendantes de la session de pilotage. Borne retenue par la mère : le plafond de l'amorce, puis l'instance « exited ».
3. Les sessions ouvertes par les tâches n'ont ni dépôt ni connecteur. Corrigé par les « Moyens » (a) et (b).
4. Risque de secret : la session d'essai de 08:39Z a affiché `vastai show instances --raw` brut. La sortie contenait la variable d'environnement d'une clé de déploiement des R8 ; `HF_TOKEN` et `GH_TOKEN` de l'instance 59079406 y figuraient peut-être aussi. Corrigé par (f). La rotation est soumise à Lazar par la mère.
5. Crédit Vast épuisé : création de la session 2 impossible. Recharge à décider par Lazar.

## Outils de la fille (hors dépôt)
- `surveiller_r1v4_v1.sh` 1d158a5b…, puis `surveiller_r1v4_v2.sh` 50e8b991… (avec `-y`) ;
- `garde_secrets_v1.py` 606902b9….
