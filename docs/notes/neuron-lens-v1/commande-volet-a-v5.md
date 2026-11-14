# Commande de location et de lancement du volet A de « Neuron Lens » — v5, sans ssh (proposée, **non exécutée**)

Remplace la v4 (`commande-volet-a-v4.md`, `417ca3b4…`, archivée) après sa contre-lecture
(`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-6-commande-v4-sans-ssh.md`) : suivi sans secret (`suivi_vast_v1`, aucune sortie
brute de `vastai show`) ; entrée de l'instance vérifiée dans la source de l'outil 1.11.0 (`--args` est une liste transmise telle
quelle : `["-c", "<texte>"]`) ; filtre `cuda_max_good>=13.0` (la roue par défaut de `torch` 2.14.1 dépend des bibliothèques CUDA 13,
`nvidia-nccl-cu13`, métadonnées publiques de PyPI) ; branche des résultats exigée absente avant la location ; amorce v2 (première
poussée fatale, code 14 ; poussée finale persistante) ; dépôt réduit v6. La v4 remplaçait la v3 (`commande-volet-a-v3.md`, `992e11ac…`, archivée), dont le feu (R-2749) est tombé : le conteneur de la session ne peut
pas joindre la machine par ssh (mandataire réseau limité au HTTPS ; arrêt du 14 novembre, rapport à la mère). Décision de la mère
R-2752 : commande sans ssh, sur le patron des courses précédentes du compte — branche dédiée du dépôt réduit, script de démarrage de
l'instance, résultats poussés sur une branche du dépôt de travail privé, suivi par `vastai logs` et `vastai show instance`.

Pour la ligne **GO-2026-11-14-05** (volet A, plafond 10 USD, échéance 30 novembre). Rien ne part sans un **nouveau feu écrit de la
mère, avec le numéro de ligne**, citant cette v4 et ses empreintes. Toute heure consignée vient de `date -u` dans la même commande.
Jamais vers `main`, jamais vers `lciric/controle-ia`, rien dans `registres/`. Ne jamais toucher les instances 58936096, 58936099,
58936100, 60480302, 60599797, ni aucune instance ou serveur d'une autre session.

**Secrets** : `VAST_API_KEY` reste dans le conteneur, lue par son nom. Le seul secret passé à la machine est le jeton du programme :
`GH_TOKEN` reçoit la valeur de `CONTROLE_IA_GITHUB_TOKEN_2`, développée par le shell du lancement, jamais affichée ni écrite (elle est
conservée dans la configuration de l'instance chez le loueur jusqu'à sa destruction). Sur la machine, le jeton ne sert qu'en en-tête
HTTP de chaque commande `git` (`-c http.extraHeader`) : ni l'adresse du dépôt, ni la configuration git, ni le disque, ni le journal ne le
contiennent ; la course tourne **sans** lui (`env -u GH_TOKEN`). Le modèle et les lentilles sont publics.

## 0. Avant la location (conteneur de la session)
1. Outil du loueur : `vastai` 1.11.0, installé dans un environnement à part de l'espace de travail ; clé lue par son nom.
2. `date -u +%FT%TZ; vastai show user --raw | python3 -c 'import json,sys; print(json.load(sys.stdin)["credit"])'` → **crédit relevé**,
   consigné au journal. Crédit < 12 USD → arrêt, message à la mère.
3. Prix du jour :
   `date -u +%FT%TZ; vastai search offers 'gpu_name=RTX_4090 num_gpus=1 cpu_ram>=64 cpu_cores_effective>=8 disk_space>=80 inet_down>=300 reliability>0.98 cuda_max_good>=13.0 dph_total<=0.90 rentable=true' -o 'dph_total' --raw`
   → offre la moins chère ; identifiant, `dph_total`, cœurs, mémoire, disque, CUDA consignés. Aucune offre → arrêt.
4. **Dépôt réduit** au commit scellé de la course :
   `python scripts/depot_reduit_neuron_lens_volet_a_v6.py <COMMIT> <dossier neuf>` → `liste-fichiers.sha256`, `rapport.json` (commit
   réduit, empreinte de la liste, empreinte du paquet), paquet `neuron-lens-volet-a-reduit.bundle`. Le commit réduit est poussé sur la
   **branche dédiée** `course/neuron-lens-volet-a-reduit-v6` du dépôt de travail :
   `git fetch <paquet> course:refs/heads/course/neuron-lens-volet-a-reduit-v6 && git push origin course/neuron-lens-volet-a-reduit-v6` ;
   puis `git ls-remote origin refs/heads/course/neuron-lens-volet-a-reduit-v6` = commit réduit, et
   `git ls-remote origin refs/heads/calcul/neuron-lens-volet-a-v1` **vide** (branche des résultats absente ; sinon arrêt).

## 1. Location (une seule instance), minuterie, garde, rappel
5. Création (image `python:3.12-bookworm` : git, venv et coreutils compris ; `torch` installé par `pip` avec ses bibliothèques CUDA) :
   ```
   GO_ID=GO-2026-11-14-05 vastai create instance <OFFRE> --raw --image python:3.12-bookworm --disk 80 --label neuron-lens-volet-a \
     --env "-e GH_TOKEN=$CONTROLE_IA_GITHUB_TOKEN_2 -e COMMIT_REDUIT=<COMMIT_REDUIT> -e GO_ID=GO-2026-11-14-05 -e RUN_ID=<AAAAMMJJ-HHMMSS>-neuron-lens-volet-a -e CACHE_HF=/workspace/hf -e BRANCHE_RESULTATS=calcul/neuron-lens-volet-a-v1 -e PERIODE_POUSSE_S=1800" \
     --entrypoint bash --args -c 'set -e; mkdir -p /workspace; cd /workspace; git -c http.extraHeader="Authorization: Basic $(printf "x-access-token:%s" "$GH_TOKEN" | base64 -w0)" clone -q --depth 1 --single-branch --branch course/neuron-lens-volet-a-reduit-v6 https://github.com/lciric/controle-ia-travail.git depot; exec bash depot/scripts/amorce_neuron_lens_volet_a_v2.sh'
   ```
   → **identifiant d'instance** et heure de création consignés. (Les `$` des arguments sont entre apostrophes : développés sur la
   machine, pas dans le conteneur ; seul `$CONTROLE_IA_GITHUB_TOKEN_2` de `--env` est développé par le shell du lancement.)
6. **Minuterie de destruction par identifiant**, posée aussitôt (R10), durée comptée depuis la création :
   `D=$(PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v3 --minuterie-seulement --prix-h <PRIX> --plafond 10 --debut <ISO_CREATION>)`
   puis en arrière-plan `sleep $D; vastai destroy instance <ID>` (PID consigné).
7. **Garde de dépense** en arrière-plan (PID consigné) :
   `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v3 --instance <ID> --prix-h <PRIX> --plafond 10 --debut <ISO_CREATION> --frais-fixes 0 --journal docs/notes/neuron-lens-v1/journal-depense-volet-a-v1.jsonl`
   → compte rendu à la mère à 60 % (6 USD, elle décide de la suite) ; destruction réessayée et vérifiée à 90 % (9 USD ; code 4 et
   message immédiat à la mère si elle échoue).
8. **Rappel indépendant** : `send_later` à 80 % de la durée de la minuterie, « vérifier et détruire l'instance <ID> ».

## 2. Sur la machine (script `scripts/amorce_neuron_lens_volet_a_v2.sh`, sans intervention)
9. Commit égal à `COMMIT_REDUIT` et arbre propre, sinon arrêt (code 10, visible dans les journaux) ; première poussée (« environnement
   pret ») impossible → arrêt (code 14), avant toute dépense de carte graphique ; environnement aux versions
   épinglées ; carte graphique exigée (code 11) ; essais rapides (liste de la v3), un échec ou un essai sauté = arrêt (code 12) ; course
   `volet_a_lancer_v3` sans le jeton ; poussée sur `calcul/neuron-lens-volet-a-v1` des `runs/<run_id>/`, `diag/<run_id>/` et d'un
   fichier d'état `etat-neuron-lens-volet-a.txt` à chaque étape, toutes les 30 min pendant la course, à la fin et à tout arrêt (sauf le
   code 10, avant l'arbre de travail des résultats : visible dans les journaux seulement). Le conteneur s'arrête à la fin du script.
10. Tout arrêt de la machine (codes 10 à 14, échec de la course) : destruction par identifiant aussitôt lu, rapport à la mère.

## 3. Suivi, retour et destruction (conteneur de la session)
11. Suivi, **jamais par une sortie brute de `vastai show`** (elle restitue la configuration de l'instance, jeton compris) :
    `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.suivi_vast_v1 logs <ID> 40` (lignes `AMORCE …`) et
    `… suivi_vast_v1 instance <ID>` (champs `id`, `actual_status`, `dph_total`… ; toute sortie contenant un secret est refusée) ; un état
    « exited » se détruit aussitôt (stockage facturé) ; état de la course :
    `git fetch origin +refs/heads/calcul/neuron-lens-volet-a-v1:refs/remotes/origin/calcul/neuron-lens-volet-a-v1` puis
    `git show refs/remotes/origin/calcul/neuron-lens-volet-a-v1:etat-neuron-lens-volet-a.txt`.
12. Fin (« course terminee » ou arrêt) : récupération par cette branche ; `verifier_resultat` sur chaque fichier de `diag/<run_id>/` ;
    copie dans `prep/neuron-lens-v1` ; commit ; poussée de la branche seule.
13. `vastai destroy instance <ID>` ; `… suivi_vast_v1 instances` → instance absente ; minuterie et garde arrêtées **par PID** ; rappel
    annulé ; crédit relevé de nouveau ; lignes proposées à la mère pour `registres/arrets.md` et `registres/depenses.md`.

## Essai à blanc (sans location), fait avant la demande de feu
Script `scripts/essai_a_blanc_amorce_neuron_lens_v2.sh` ; journal complet versé (`docs/notes/neuron-lens-v1/essai-a-blanc-amorce-v2.txt`,
empreinte au compagnon) : cas nominal avec la **liste réelle** des essais rapides (61 passés), course jouet sans jeton, poussées
périodiques, état final « course terminee », fichiers présents sur la branche des résultats ; artefacts (R5) : mauvais commit → code 10
(journaux seulement) ; essai en échec → 12 ; essai sauté → 12 ; première poussée impossible → 14 ; balayage du jeton factice sur les
disques des machines d'essai, le dépôt distant et les journaux.

## Jeton
Le jeton du programme permet l'écriture sur tout le dépôt de travail, `main` compris ; « jamais vers `main` » n'est garanti que par
l'amorce (poussée vers `refs/heads/calcul/neuron-lens-volet-a-v1` seulement). Si un jeton restreint à une branche existe, il est préférable
(point signalé à la mère).

## Devis (inchangé depuis la v3, borne haute)
3,5 à 5,5 h, soit 3,2 à 5 USD à 0,90 USD/h, jusqu'à 7 USD si l'audit R4 « trop beau » se déclenche ; installation de `torch` et de ses
bibliothèques CUDA par `pip` en plus (≈ 5 à 10 min). Le débit réel n'est pas mesuré avant la course : la garde le surveille (6 USD
compte rendu, 9 USD arrêt dur). Si la version de CUDA de l'hôte ne convient pas à `torch` 2.14.1, l'amorce s'arrête au code 11 (quelques
minutes de location perdues).
