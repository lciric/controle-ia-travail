# Devis — pilote de l'exposant p (v2, pour le brouillon 2 du préenregistrement)

Rédigé le 4 novembre 2026 vers 02:20 UTC (`date -u`) par le rédacteur neuf du brouillon 2 (sous-agent). Remplace, pour le brouillon 2, `devis-pilote-exposant-p-v1.md` (gardé tel quel, R12). **GO déjà accordé** : GO-2026-11-04-03, calcul, **30 USD**, du 4 au 18 novembre 2026 (`registres/go.md` de `main`, ligne 241 ; mots de Lazar du 3 novembre, R-1343 et R-1344). Le pire cas de ce devis doit tenir sous 30 USD : **il tient (≈ 17 USD, section 3)**. Rien n'a été lancé ; aucune commande Vast.ai n'a été passée (prix tirés de `registres/depenses.md`, à relire au lancement).

## 1. Volume (calcul)

| Bloc (ordre gelé) | Statut | Plans |
|---|---|---|
| Base : Wealth × Gender, sous-ensemble 0 | décisif (témoin positif) | 1 |
| Base : 17 isotropes ; Wealth × Gender sur les sous-ensembles 1 à 7 | descriptif, sous réserve de temps | 24 |
| Lu : 17 isotropes | décisif (instrument) | 17 |
| Lu : (E, R), 32 sous-ensembles | décisif | 32 |
| Lu : 60 différences aléatoires, plan k sur k mod 32 | décisif (référence répartie, B3) | 60 |
| Lu : Wealth × Gender, 32 sous-ensembles | décisif (sensibilité, B4) | 32 |
| Lu : jumeau (N, R), 32 sous-ensembles | qualificatif (emprunt R9-bis) | 32 |
| Lu : famille, K = 8 plans × 31 autres sous-ensembles | qualificatif (voie B de B2) | 248 |
| Lu : (E, rd), (R, rd), contrastives, mixtes, moitiés, (E, Formal) | descriptif | 64 |
| **Total** | 142 décisifs, 280 qualificatifs, 88 descriptifs | **510** |

- Passes avant par plan : 30 ancres × (961 points + 1 référence) = 28 860 séquences de 5 jetons ; total 510 × 28 860 ≈ **14,7 millions** de séquences (calcul ; 230 plans et 6,6 millions au brouillon 1).
- Extraction des directions, réserve de 10 000 entrées et choix du jumeau sur le tokeniseur : négligeables.
- Si l'issue est « exclu » ou « non concluant (identification) », le plan (E, R) n'est mesuré que sur le sous-ensemble 0, et la sensibilité, le jumeau et la famille ne sont pas mesurés (ils ne seraient pas lus) : ≈ 199 plans de moins.

## 2. Durée sur A100 80 Go

- Débit attendu (calcul du brouillon 1, repris) : ≈ **15 s par plan** (lots de 961 points × 5 jetons, 40 % de la crête en `bfloat16`, supposé).
- Débit pessimiste (code publié, « ~40 s/pair on H100 », lots de 64, majoré de moitié pour l'A100, supposé) : ≈ **60 s par plan**. C'est aussi la durée par plan prévue que le lanceur emploie avant d'en avoir mesuré une (`plafonds.duree_plan_prevue_s`).
- Mise en place (supposé, d'après les runs du programme) : 25 à 45 minutes (environnement, deux modèles, essais des pilotes v1 et v2 et du script, flux FineWeb-edu).

| Scénario | Balayage | Total de carte |
|---|---|---|
| attendu (15 s par plan) | 510 plans ≈ 2,1 h (décisifs seuls ≈ 0,6 h) | ≈ **2,7 h** |
| pessimiste (60 s par plan) | ≈ 8,5 h (décisifs seuls ≈ 2,4 h) | ≈ **9,3 h** |
| pire cas | plafond de l'amorce, 630 min, puis 30 min de surveillance avant l'arrêt par identifiant | ≈ **11 h** |

**Plafonds** (configuration v2, figés au scellement) :
- interne du lanceur : 34 200 s (9,5 h). Un bloc décisif qui n'y tient plus arrête le run. Un bloc qualificatif ou descriptif n'est lancé que si le temps restant couvre aussi les blocs décisifs à venir (contre-lecture R2, I5 ; corrige l'erreur du devis v1 relevée par le couple D01) ; sinon il est sauté et consigné ;
- délai externe du run : 600 min (script d'instance v2) ;
- plafond d'ensemble de l'amorce : 630 min.

## 3. Dépense

Prix relevés dans `registres/depenses.md` pour ce filtre (octobre et novembre 2026) : **1,08 à 1,366 USD l'heure** (instances 58162997 à 1,08 ; 58926345 à 1,2133 ; 57978233 à 1,366) ; téléchargement 0,026 USD par Go ; disque ≈ 0,0267 USD l'heure pour 80 Go. Calcul au prix haut arrondi de **1,40 USD l'heure** :

| Scénario | Carte | Téléchargement (≈ 35 Go) | Disque | Total |
|---|---|---|---|---|
| attendu | 2,7 h → 3,78 USD | 0,91 USD | ≈ 0,08 USD | **≈ 4,8 USD** |
| pessimiste | 9,3 h → 13,02 USD | 0,91 USD | ≈ 0,25 USD | **≈ 14,2 USD** |
| pire cas | 11 h → 15,40 USD | 0,91 USD | ≈ 0,3 USD | **≈ 16,6 USD** |

- **Pire cas ≈ 16,6 USD < 30 USD (GO-2026-11-04-03).** L'amorce exige un plafond de GO d'au moins 17 USD (`MONTANT_PIRE_CAS_USD`, arrondi). Le pire cas reste sous 30 USD tant que le prix ne dépasse pas ≈ 2,6 USD l'heure (calcul : (30 − 1,2) / 11).
- Coût des ajouts du brouillon 2 (calcul) : famille K = 8 (voie B de B2) +248 plans, soit +1,0 h et ≈ +1,4 USD attendus, +4,1 h et ≈ +5,8 USD au pessimiste ; jumeau +32 plans, ≈ +0,2 USD attendus, +0,8 USD au pessimiste ; sensibilité sur le modèle lu : déjà au devis v1 (descriptive alors, décisive maintenant).

## 4. Offre et lancement (à relire au moment du lancement)

```
vastai search offers "gpu_name in [A100_SXM4,A100_PCIE] gpu_ram>=79 num_gpus=1 cuda_vers>=13.0 verified=true datacenter=true reliability>=0.99 cpu_ram>=128 disk_space>=80 rentable=true" -o dph_total --storage 80 --raw
```

1. **Avant toute création** (machine de la session) : `AMORCE_ETAPE=verifier GO_ID=GO-2026-11-04-03 REGISTRE_GO=/home/user/controle-ia-travail/registres/go.md bash scripts/amorce_instance_pilote_exposant_p_v2.sh` → code 0 exigé (essayé ici le 4 novembre : GO valide, plafond 30 USD ≥ 17 ; avertissement rapporté : seize identifiants en double ailleurs dans le registre de `main`).
2. Création de l'instance par une commande qui cite `GO_ID=GO-2026-11-04-03` (garde de calcul). **Réserve** : la garde `.claude/hooks/garde_calcul.py` lit le registre de l'arbre où elle tourne ; sur la branche `canal/conv-audit-n04` le GO est absent, sur `main` elle bloque à cause des seize doublons (R-1122). La session de lancement doit trancher ce point avant de créer l'instance (nœud de session-depot, hors de ce brouillon).
3. Commande de démarrage : l'amorce en étape `instance`, avec `COMMIT`, `GO_ID`, `GH_TOKEN` (grain fin, dépôt de travail privé seulement, jamais `lciric/controle-ia`) et `HF_TOKEN` (licence Llama 3.1 acceptée pour **les deux** modèles) passés par `--env`, jamais écrits. L'amorce revérifie le GO sur `origin/main:registres/go.md` avant toute installation.
4. Arrêt de l'instance par son identifiant (R10), consigné dans `registres/arrets.md`.

Répétition gratuite possible avant la dépense, sur processeur : `MODE=jouet PREREG_ABSENT=1 CONFIG=… STIMULI=… TESTS_ATTENDUS=…` (la répétition de bout en bout fait aussi partie des essais).
