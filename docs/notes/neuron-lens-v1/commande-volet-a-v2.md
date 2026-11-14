# Commande de location et de lancement du volet A de « Neuron Lens » — v2 (proposée, **non exécutée**)

Remplace la v1 (`commande-volet-a-v1.md`, `722818ba…`, archivée) après la contre-lecture 3
(`docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-3-course-v3-et-lancement.md`, remarques 1, 3, 4, 7, 11, 12) et la décision
de la mère R-2737 (dépôt réduit, aucun historique ; outil du loueur installé au feu, clé lue par son nom `VAST_API_KEY`, jamais
affichée).

Pour la ligne **GO-2026-11-14-05** (volet A, plafond 10 USD, échéance 30 novembre). Rien ne part sans le **feu écrit de la mère, avec
le numéro de ligne**, après : pièces contre-lues (modèle D) et scellées ; fusion ordinaire de `refs/remotes/origin/main` dans la branche
et vérification des lignes GO-2026-11-14-05 et -06 dans `registres/go.md` (R-2729). Toute heure consignée vient de `date -u` dans la
même commande. Aucune clé sur la machine : Qwen3-8B, `rs-lenses` et le catalogue sont publics.

## 0. Avant la location (conteneur de la session)
1. Outil du loueur : `pip install vastai` (version consignée) ; la clé est lue par son nom (`VAST_API_KEY`), jamais affichée.
2. `date -u +%FT%TZ; vastai show user --raw | python3 -c 'import json,sys; print(json.load(sys.stdin)["credit"])'` → **crédit
   relevé**, consigné au journal. Crédit < 12 USD → arrêt, message à la mère.
3. Prix du jour :
   `date -u +%FT%TZ; vastai search offers 'gpu_name=RTX_4090 num_gpus=1 cpu_ram>=64 cpu_cores_effective>=8 disk_space>=80 inet_down>=300 reliability>0.98 cuda_max_good>=12.8 dph_total<=0.90 rentable=true' -o 'dph_total' --raw`
   → offre la moins chère retenue ; identifiant d'offre, `dph_total`, cœurs, mémoire, disque, CUDA consignés. Aucune offre → arrêt.
4. **Dépôt réduit** au commit scellé de la course :
   `python scripts/depot_reduit_neuron_lens_volet_a_v3.py <COMMIT> <dossier neuf>` → `liste-fichiers.sha256` (liste exacte et
   empreintes), `rapport.json` (commit source, commit réduit, empreinte de la liste, empreinte du paquet), paquet
   `neuron-lens-volet-a-reduit.bundle` (branche `course`, un seul commit). Liste et empreintes jointes à la demande de feu.

## 1. Location (une seule instance), minuterie, garde, rappel
5. `GO_ID=GO-2026-11-14-05 vastai create instance <OFFRE> --image pytorch/pytorch:2.7.1-cuda12.8-cudnn9-runtime --disk 80 --ssh --direct --label neuron-lens-volet-a --raw`
   → **identifiant d'instance** et heure de création consignés.
6. **Minuterie de destruction par identifiant**, posée aussitôt, avant toute passe (R10) ; durée restante comptée depuis la création :
   `D=$(PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v2 --minuterie-seulement --prix-h <PRIX> --plafond 10 --debut <ISO_CREATION>)`
   puis, en arrière-plan : `sleep $D; vastai destroy instance <ID>` (PID consigné).
7. **Garde de dépense** en arrière-plan (PID consigné) :
   `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v2 --instance <ID> --prix-h <PRIX> --plafond 10 --debut <ISO_CREATION> --frais-fixes 0 --journal docs/notes/neuron-lens-v1/journal-depense-volet-a-v1.jsonl`
   → compte rendu à la mère à 60 % (6 USD) ; à 90 % (9 USD), destruction par identifiant réessayée et vérifiée (code 4 et message
   immédiat à la mère si elle échoue). Pas de frais fixes chez ce loueur (stockage compris dans `dph_total`).
8. **Rappel indépendant** (si le conteneur de la session tombe, minuterie et garde tombent avec lui) : `send_later` à 80 % de la
   durée de la minuterie, message « vérifier et détruire l'instance <ID> ».

## 2. Sur la machine (par `ssh`, aucune clé copiée)
9. `apt-get update && apt-get install -y git` (absent de l'image) ; `scp` du paquet ; vérification de son empreinte ;
   `git clone --branch course neuron-lens-volet-a-reduit.bundle depot && cd depot && git rev-parse HEAD` = commit réduit.
10. `python -m venv .venv && . .venv/bin/activate && pip install -r requirements-neuron-lens-volet-a-v1.txt` ;
    `python -c 'import torch; assert torch.cuda.is_available(); print(torch.cuda.get_device_name(0))'` → sinon arrêt, destruction.
11. Essais rapides (≈ 1 min ; la fumée longue de l'assemblage a passé dans le conteneur et n'est pas rejouée sur la machine payée) :
    `PYTHONPATH=src python -m pytest -q tests/test_neuron_lens_volet_a_extraction_v2.py tests/test_neuron_lens_volet_a_chargement_v1.py tests/test_neuron_lens_volet_a_lancer_v2.py tests/test_neuron_lens_volet_a_donnees_v1.py tests/test_neuron_lens_volet_a_donnees_v2.py tests/test_neuron_lens_volet_a_sondes_v2.py tests/test_neuron_lens_volet_a_lectures_v2.py tests/test_neuron_lens_garde_depense_v2.py`
    → un essai sauté ou en échec : arrêt, destruction par identifiant. `git status --porcelain` vide exigé.
12. Course (dans `tmux`, pour survivre à la coupure de `ssh`) :
    `GO_ID=GO-2026-11-14-05 PYTHONPATH=src python -m controle_ia.neuron_lens.volet_a_lancer_v2 --run-id <AAAAMMJJ-HHMMSS>-neuron-lens-volet-a --cache /workspace/hf --appareil cuda`
13. **Rapatriement périodique** (conteneur de la session, arrière-plan, PID consigné) : toutes les 30 min, `scp -r` de
    `depot/runs/<run_id>/` et `depot/diag/<run_id>/` vers un dossier neuf du conteneur (une destruction à 90 % ne perd pas les mesures
    brutes déjà scellées par contraste).

## 3. Retour et destruction
14. Rapatriement final ; `verifier_resultat` sur chaque fichier de `diag/<run_id>/` ; copie dans la branche ; commit ; poussée de la
    branche seule.
15. `vastai destroy instance <ID>` ; `vastai show instances --raw` → instance absente ; minuterie, garde et rapatriement arrêtés
    **par PID** ; rappel annulé ; crédit relevé de nouveau ; dépense consignée ; rapport à la mère.

## Devis (refait après la contre-lecture 3)
- Processeur (sondes, détecteurs sur 12 288 neurones, intervalle apparié) : 1 à 2 h (mesures synthétiques sur 4 cœurs ; 8 cœurs
  exigés).
- Passes de A3 : ≈ 960 000 séquences au plus sans cache (estimation du contre-lecteur) ; l'extraction v2 arrête la passe à la couche
  lue (en moyenne la moitié de la profondeur) et les invites que le retrait ne modifie pas ne repassent pas : ≈ 0,7 à 2 h à 50–70
  séquences complètes par seconde.
- Téléchargement (≈ 17 Go) et chargement : ≈ 0,3 h ; essais rapides : quelques minutes.
- **Total 2,5 à 5 h, soit 2,3 à 4,5 USD à 0,90 USD/h ; jusqu'à 6,3 USD si l'audit R4 « trop beau » se déclenche (+ 40 %).**
  Le débit réel n'est pas mesuré avant la course : la garde le surveille ; à 60 % (6 USD) la mère reçoit le compte rendu et décide ;
  à 90 % l'arrêt est dur (les mesures brutes des contrastes finis sont déjà scellées et rapatriées).
