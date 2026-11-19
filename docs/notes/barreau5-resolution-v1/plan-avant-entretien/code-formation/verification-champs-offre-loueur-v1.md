# Noms des champs de l'offre du loueur : vérification sur une sortie réelle (v1)

Note de travail de la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`), 19 novembre 2026 vers 20:05Z. Elle répond au choix 21 du rapport v2 du développeur et au point 4 du § 7 de son rapport v3 : les noms des champs n'avaient jamais été vus sur une vraie sortie.

## Ce qui a été fait
- **Requête** : une seule recherche d'offres, en lecture, sans dépense, vers l'interface du loueur de cartes (`console.vast.ai/api/v0/bundles/`).
  - Filtre : carte A100 SXM4, une carte, louable, à la demande.
  - La clé est passée par son nom dans la commande (`VAST_API_KEY`) ; sa valeur n'a été ni écrite ni affichée.
  - Le CLI du loueur refuse le certificat du mandataire réseau ; la requête est donc passée par `curl`, qui le lit.
- **Sortie brute** : `sortie-recherche-offres-loueur-2026-11-19T2002Z-v1.json` (même dossier), scellée (`3b058a95…`). Ce sont des données publiques du marché. Elle ne contient aucune clé : la recherche de « api_key », « token » et « bearer » n'y trouve rien.
- **Garde du code** : `formation_v1.exiger_offre` jouée sur chaque offre, sans réseau.

## Résultats
1. **Champs** : les dix champs que lit le code sont présents dans les 28 offres rendues, avec des types numériques (sauf le nom de la carte). Ce sont `id`, `gpu_name`, `num_gpus`, `gpu_ram`, `cpu_cores_effective`, `cpu_ram`, `disk_space`, `cuda_max_good`, `dph_total` et `storage_cost`.
   - `id` est un entier, et la garde le lit par `str(...).isdigit()`.
   - `gpu_name` vaut « A100 SXM4 ».
   - `gpu_ram` est en Mo : 81 920 pour 80 Go, et 40 960 pour les cartes de 40 Go, que la garde refuse à bon droit.
2. **Garde réelle** : 3 offres sur 28 sont acceptées par `exiger_offre` à 20:02Z.
   - 17 sont refusées pour `gpu_ram` (cartes de 40 Go).
   - Les autres refus : 3 pour le prix, 2 pour le disque, 2 pour les cœurs, 1 pour le stockage.
3. **Carte de 80 Go seule** (11 offres) : nombre d'offres qui passent chaque borne.

   | borne | offres qui passent, sur 11 |
   |---|---|
   | prix ≤ 1,30 USD de l'heure | 7 |
   | cœurs ≥ 16 | 9 |
   | mémoire vive ≥ 128 000 Mo | 11 |
   | disque ≥ 150 Go | 7 |
   | CUDA ≥ 13.0 | 10 |
   | stockage ≤ 0,08 USD de l'heure | 8 |
   | **toutes les bornes** | **3** |

   - Les trois offres acceptées coûtent 1,12, 1,14 et 1,19 USD de l'heure, près du plafond de l'offre.
4. **Unité de `storage_cost`** : non vérifiable sur cette seule sortie. Le code la tient pour un prix au Go et au mois (choix 21). La valeur vue, 0,2, donne 0,041 USD de l'heure pour 150 Go, ce qui est plausible.

## Ce que cela change
- **Pour le code** : rien. Les noms et les types sont bons, et la garde se comporte comme ses essais le disent.
- **Pour le devis et le calendrier** : c'est un instantané du marché, qui change d'heure en heure.
  - Sept instances sont prévues, et trois offres seulement passaient les bornes à 20:02Z. Si le calendrier les lance ensemble, il faudra peut-être les lancer par vagues, ou attendre des offres.
  - Le prix réel est plus près de 1,15 USD de l'heure que du prix médian supposé, si le devis en supposait un plus bas. C'est au rédacteur du devis de le dire au brouillon 4.
