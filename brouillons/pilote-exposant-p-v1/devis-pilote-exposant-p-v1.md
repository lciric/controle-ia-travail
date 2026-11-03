# Devis — pilote de l'exposant p (v1)

Rédigé le 3 novembre 2026 vers 09:00 UTC (`date -u`) par le concepteur-rédacteur neuf du pilote. **Nœud de décision** : aucune dépense ni aucune instance sans GO de Lazar sur ce devis, consigné dans `registres/go.md` (`GO_ID=GO-AAAA-MM-JJ-NN`). Rien n'a été lancé ; aucune commande Vast.ai n'a été passée pour ce devis (prix tirés des registres, à relire au moment du GO).

## 1. Volume de calcul (calcul)

| Poste | Quantité |
|---|---|
| Plans balayés | 230 : 25 sur le modèle de base (1 témoin décisif, 17 isotropes, 7 Wealth × Gender descriptifs) ; 205 sur le modèle lu (17 isotropes, 32 (E, R), 60 différences aléatoires, 20 (E, rd) et (R, rd), 10 contrastives, 32 Wealth × Gender, 10 mixtes, 16 moitiés, 8 (E, Formal)) |
| Passes avant par plan | 30 ancres × (961 points + 1 référence) = 28 860 séquences de 5 jetons |
| Passes avant de balayage | 230 × 28 860 = **6 637 800** séquences, 33,2 millions de jetons |
| Passes d'extraction | ≈ 1 700 invites de 10 à 25 jetons (directions des deux modèles), 10 000 entrées de 5 jetons (réserve) et 240 ancres sur le modèle de base, arrêtées au bloc 2 : négligeable |
| Arithmétique | 2 × 6,76 milliards de paramètres traversés (blocs 0 à 30) par jeton ≈ 1,35 × 10¹⁰ opérations ; total ≈ 4,5 × 10¹⁷ opérations |

## 2. Durée sur A100 80 Go

- **Ma propre estimation (calcul).** Lots de 961 points × 5 jetons (4 805 jetons par passe avant). Hypothèse : 40 % de la crête de 312 téraopérations par seconde en `bfloat16`, soit ≈ 125 × 10¹² opérations par seconde (supposé). Cela donne ≈ 3 600 s de balayage, ≈ **15 s par plan**.
- **Débit publié du papier**, en contrepoint pessimiste : « ~40 s/pair on H100 », avec des lots de 64 points (`README.md` du code, section « Re-sweep from model weights »). Les petits lots sous-emploient la carte. Repris tel quel sur A100 et majoré de moitié pour l'écart de carte (supposé) : ≈ **60 s par plan**, soit ≈ 13 800 s.
- **Ordre de grandeur du programme** : P3 a mesuré 40,2 s par épisode en lots de 8. Il s'agissait de génération autorégressive, non comparable aux passes avant courtes du pilote : repère seulement.
- **Mise en place** (supposé, d'après les runs du programme) :
  - environnement GPU et `datasets`, 5 à 8 min ;
  - deux modèles de 16 Go, 3 à 11 min ;
  - 62 essais, 3 à 5 min ;
  - flux FineWeb-edu (≈ 20 000 documents lus pour remplir le tampon de 10 000), 1 à 3 min ;
  - chargements, analyse et poussées, ≈ 5 min ;
  - total ≈ 20 à 35 min.
- **Plafonds** :
  - interne de 14 400 s ; un bloc décisif qui n'y tient plus arrête le run, un bloc descriptif est sauté ;
  - les 110 plans décisifs passent en tête : ≈ 0,5 h au débit estimé, ≈ 1,8 h au débit pessimiste ;
  - délai externe de 270 min sur le run.

| Scénario | Balayage | Total de carte |
|---|---|---|
| attendu (15 s par plan) | ≈ 1,0 h | ≈ **1,5 h** |
| pessimiste (60 s par plan) | ≈ 3,8 h (plafond interne de 4 h ; descriptifs coupés au besoin) | ≈ **4,5 h** |
| pire cas | 270 min (délai externe) | ≈ **5,7 h** (mise en place 40 min, délai de surveillance avant l'arrêt 30 min) |

## 3. Dépense

Prix relevés dans `registres/depenses.md` pour ce filtre (octobre 2026) : 1,08 à 1,2133 USD l'heure ; téléchargement 0,026 USD par Go ; disque ≈ 0,0267 USD l'heure pour 80 Go. Calcul au prix haut de 1,2133 USD l'heure :

| Scénario | Carte | Téléchargement (≈ 35 Go : deux modèles, roues de torch, flux) | Disque | Total |
|---|---|---|---|---|
| attendu | 1,5 h → 1,82 USD | 0,91 USD | ≈ 0,05 USD | **≈ 2,8 USD** |
| pessimiste | 4,5 h → 5,46 USD | 0,91 USD | ≈ 0,15 USD | **≈ 6,5 USD** |
| pire cas | 5,7 h → 6,92 USD | 0,91 USD | ≈ 0,3 USD (instance arrêtée jusqu'à sa destruction) | **≈ 8,1 USD** |

**Plafond proposé pour le GO : 10 USD.** Il couvre le pire cas et une hausse de prix jusqu'à ≈ 1,5 USD l'heure ; au-delà, nouvel avis.

## 4. Offre (filtre usuel du programme, à relire au GO)

```
vastai search offers "gpu_name in [A100_SXM4,A100_PCIE] gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true" -o dph_total --storage 80 --raw
```

- Disque de 80 Go : deux modèles (≈ 32 Go), environnement (≈ 10 Go), cache du flux, sorties (≈ 20 Mo de grilles compressées).
- `cuda_vers>=13.0` : la roue de torch 2.14.1 vise CUDA 13.0 (`requirements-gpu.txt`).
- Jetons transmis par `--env`, jamais écrits : `GH_TOKEN` (grain fin, dépôt de travail privé seulement, jamais `lciric/controle-ia`) et `HF_TOKEN` (lecture ; la licence Llama 3.1 doit être acceptée pour **les deux** dépôts, `meta-llama/Llama-3.1-8B` et `meta-llama/Llama-3.1-8B-Instruct`. Le script le vérifie avant tout téléchargement lourd).
- Lancement : `COMMIT=<commit de scellement> bash scripts/pilote_exposant_p_instance_v1.sh`, sous une amorce bornée sur le modèle de `scripts/amorce_instance_p3.sh` (plafond d'ensemble proposé : 300 min ; amorce non écrite dans ce brouillon). Arrêt de l'instance par son identifiant (R10), consigné dans `registres/arrets.md`.
- Avant la dépense, une répétition jouet sur processeur est possible, gratuite : `MODE=jouet PREREG_ABSENT=1 CONFIG=… STIMULI=… TESTS_ATTENDUS=62` ; la répétition de bout en bout fait aussi partie des 62 essais.
