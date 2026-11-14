# Commande de location et de lancement du volet A de « Neuron Lens » — v1 (proposée, **non exécutée**)

Pour la ligne **GO-2026-11-14-05** (volet A, plafond 10 USD, échéance 30 novembre). Rien de ce qui suit ne part sans le **feu écrit de
la mère, avec le numéro de ligne**, après : code de la course contre-lu (modèle D) et scellé ; fusion ordinaire de
`refs/remotes/origin/main` dans la branche et vérification des lignes GO-2026-11-14-05 et -06 dans `registres/go.md` (R-2729). Aucune
clé n'est écrite ici ni envoyée sur la machine : la clé du loueur reste dans le conteneur de la session, lue par l'outil `vastai` par
son nom ; Qwen3-8B, `rs-lenses` et le catalogue sont publics (aucun jeton Hugging Face sur la machine).

## 0. Avant la location (conteneur de la session)
1. `vastai show user --raw` → **crédit relevé** (champ `credit`), consigné au journal avec l'heure (`date -u` dans la même commande).
   Crédit < 12 USD → arrêt, message à la mère.
2. Prix du jour, même commande que l'heure :
   `date -u +%FT%TZ; vastai search offers 'gpu_name=RTX_4090 num_gpus=1 cpu_ram>=64 disk_space>=80 inet_down>=300 reliability>0.98 dph_total<=0.90 rentable=true' -o 'dph_total' --raw | head -c 20000`
   → offre la moins chère retenue ; identifiant d'offre, `dph_total`, mémoire, disque consignés. Aucune offre ≤ 0,90 USD/h → arrêt.
3. Paquet du dépôt au commit scellé de la course (aucune clé dedans ; garde des secrets à 0 sur le paquet) :
   `git bundle create /tmp/…/neuron-lens-volet-a.bundle prep/neuron-lens-v1` ; empreinte du paquet consignée.

## 1. Location (une seule instance), minuterie et garde
4. `GO_ID=GO-2026-11-14-05 vastai create instance <OFFRE> --image pytorch/pytorch:2.7.1-cuda12.8-cudnn9-runtime --disk 80 --ssh --direct --label neuron-lens-volet-a --raw`
   → **identifiant d'instance** consigné avec l'heure de création.
5. **Minuterie de destruction par identifiant, posée à la création, avant toute passe** (R10) :
   `python -m controle_ia.neuron_lens.garde_depense_v1` donne la durée (`minuterie_s(prix, 10.0)`, 90 % du plafond au prix lu) ;
   commande en arrière-plan : `sleep <DUREE>; vastai destroy instance <ID>` (identifiant, jamais motif).
6. **Garde de dépense** en arrière-plan, journal dans `docs/notes/neuron-lens-v1/journal-depense-volet-a-v1.jsonl` :
   `PYTHONPATH=src .venv/bin/python -m controle_ia.neuron_lens.garde_depense_v1 --instance <ID> --prix-h <PRIX> --plafond 10 --debut <ISO> --journal …`
   → compte rendu à la mère à 60 % (6 USD), destruction par identifiant à 90 % (9 USD).

## 2. Sur la machine (par `ssh`, aucune clé copiée)
7. `scp` du paquet ; `git clone neuron-lens-volet-a.bundle depot && cd depot && git checkout <COMMIT>` ; vérification
   `git rev-parse HEAD` = commit scellé.
8. `python -m venv .venv && . .venv/bin/activate && pip install -r requirements-neuron-lens-volet-a-v1.txt`.
9. Essais miniatures d'abord (sans réseau vers le loueur) :
   `PYTHONPATH=src python -m pytest -q tests/test_neuron_lens_volet_a_*_v1.py tests/test_neuron_lens_volet_a_*_v2.py tests/test_neuron_lens_volet_a_course_v3.py tests/test_neuron_lens_garde_depense_v1.py`
   → un essai sauté ou en échec : arrêt, destruction par identifiant.
10. Course :
   `GO_ID=GO-2026-11-14-05 PYTHONPATH=src python -m controle_ia.neuron_lens.volet_a_lancer_v1 --run-id <AAAAMMJJ-HHMMSS>-neuron-lens-volet-a --cache /workspace/hf --appareil cuda`
   (la garde du rendu, le manifeste décisif, le relevé des fichiers et les mesures brutes par étape sont dans le lanceur).

## 3. Retour et destruction
11. `scp -r` de `runs/<run_id>/` et `diag/<run_id>/` vers la branche ; `python -m controle_ia.scellement verifier-arbre .` et
    `controle_ia.manifeste.verifier_resultat` sur chaque fichier ; commit, poussée de la branche seule.
12. `vastai destroy instance <ID>` ; `vastai show instances --raw` → instance absente ; minuterie et garde arrêtées **par PID** ;
    crédit relevé de nouveau ; dépense consignée au journal ; rapport à la mère.

## Devis
Mesures sur processeur (conteneur, 4 cœurs) : sonde dense sur 12 288 neurones ≈ 16 s, sondes parcimonieuses ≈ 0,1–0,2 s, sonde sur le
flux (4 096 traits) ≈ 5 s, sur données synthétiques (convergence plus lente possible sur les vraies). Par contraste, découpe et couche :
≈ 1 à 2 min de processeur (A-ii, sondes, intervalle apparié) ; 60 unités → 1 à 2 h ; passes de A3 (≈ 200 tirages par unité de C1 et
C2, invites inchangées en cache) et chargement (≈ 17 Go) : ≈ 0,5 à 1 h. **Durée estimée 2 à 4 h, dépense estimée 1 à 4 USD** à
≤ 0,90 USD/h ; plafond 10 USD ; minuterie à 10 h au plus (9 USD à 0,90 USD/h). Audit R4 « trop beau », s'il se déclenche : + 20 à 40 %.
