# Compte rendu d'E3 (T0.6, lanceur v9, amorce v7) — fille 6, 7 novembre 2026

Ordre `docs/procedures/ordre-fille-6-t06-e3-v9.md` (sceau e558e2a9…, main 4eaf5e31) ; commit d'épreuve a5dd8e05 (code src/scripts inchangé depuis e940d4b2) ; configuration `config-t06-epreuve-e3-v5.json` (b57df6ab) ; GO-2026-11-06-01 ; autorisation de location de Lazar (R-1655). Aucune valeur de clé, aucun résultat de sonde.

## Écarts acceptés
- Jeton `CONTROLE_IA_GITHUB_TOKEN="$CONTROLE_IA_GITHUB_TOKEN_2"` sous `env -i` (R-1667) ; arbre `git worktree` détaché ; environnement `/home/user/venv-depot`.
- verifier-arbre à a5dd8e05 : 130 problèmes, aucun sur une pièce de l'épreuve (R-1669).
- R-1714 (« on la lance », créer même si la règle des 2,5 h échoue) : reçu à 21:18Z, après la création ; **non utilisé** (règle passée à 3,90).

## Tentatives d'E3 sans création (0 USD)
- v5 (21:2xZ, 17:25Z) : toutes les A100 rendues de 40 Go → code 3 (`memoire_carte_min_mo`).
- v6 (20:58Z) : dépense réelle d'E2 0,627 > 0,6 → arrêt.
- v7 (21:01Z) : règle des 3 h : 1,143333 × 3 + 1,0417 = 4,47 > 4,27 → arrêt.
- v8 (21:04Z) : règle des 2,5 h : 1,116667 × 2,5 + 1,5625 = 4,35 > 4,27 (forfait de téléchargement à 0,039 $/Go) → arrêt.

## Instance
| | |
|---|---|
| identifiant | 59623267 |
| offre / machine | 29019375 (rang 2 ; rang 1 sauté : téléchargement 0,039 $/Go > 0,03) / 25723 |
| prix relevés | carte 1,093333 + stockage 0,05 = dph_total 1,143333 USD/h ; téléchargement 0,026 $/Go, forfait 1,0417 |
| règle des 2,5 h | 1,143333 × 2,5 + 1,0417 = 3,90 ≤ 4,27 |
| création | 2026-11-07T21:07:58Z |
| fin de la suite | 22:24:59Z (« tests en échec : arrêt ») |
| arrêt | 22:25:03Z par l'amorce (« ARRÊT OBTENU (stopped, HTTP 200) ») |
| destruction | 22:27:13Z par moi, par l'identifiant, sur accord de la mère |
| code de sortie de l'amorce | 1 |
| branche | essai/t06-e3-v4, dernier commit eee41eb9 (« traces de l'instance (arrêt pendant tests) ») |

## Lecture obligatoire avant création (21:07:24Z)
Filtre égal à l'ordre (`gpu_name=A100_SXM4 gpu_ram>=78 reliability>=0.98 inet_down>=500 cuda_max_good>=13.0 cpu_ram>=128 cpu_cores_effective>=16 disk_space>=150 dph_total<=1.3`), erreurs vides : avec tout 3 offres, cuda min 13,0, gpu_ram min 81920 ; sans cuda 3 (min 13,0) ; sans gpu_ram 4, dont une A100 de 40 960 Mo qui disparaît avec la clause.

## Table E3-1 à E3-11
| n° | obtenu | verdict |
|---|---|---|
| E3-1 | « torch 2.14.1+cu130 cuda 13.0 disponible True » ; nvidia-smi « NVIDIA A100-SXM4-80GB, 615.71.09, 81920 MiB » ; installation sans « installation impossible » | conforme |
| E3-2 | **« 50 failed, 3113 passed, 23 skipped in 4488.87s (1:14:48) »** (`traces/t06-20261107-222500-WXKq/tests.txt`) — échecs : 30 test_hote_durable_a1_v3_v4.py, 16 test_hote_durable_a1_v3_v3.py, 2 test_t06_v7_amorce_minuterie.py, 1 test_t06_v9_nouveaux.py, 1 test_sonde_hote_durable_a1_v3_v10.py | **non conforme** (échecs) |
| E3-3 à E3-9 | run jamais lancé (arrêt après la suite) | **non observés** |
| E3-10 | « MATERIEL MemTotal_ko=527922548 coeurs=128 flock=oui » ≥ 121 600 000 | conforme |
| E3-11 | facture 1,465 USD ≤ 4,27 ; cumul E2 + E3 = 2,092 ≤ 4,9 | conforme |

Autres lignes : « CLONAGE mode=reel secondes=8 octets_git=100585020 octets_arbre=309093906 debit_Mo_s=51.21 motifs=28 » (21:08:25Z) ; « branche essai/t06-e3-v4 poussée avant l'installation (droit d'écriture éprouvé) » (21:08:28Z) ; « citations lues : tests attendus ? ».

## Texte de `show instance 59623267 --raw` après destruction (22:27:24Z, un seul appel)
```
{
 "instances": null
}
```

## Montants (factures Vast, 22:30:15Z)
59623267 : **1,465 USD** (gpu 1,399 = 1,279 h à 1,093 $/h ; disque 0,066 = 1,330 h à 0,050 $/h ; téléchargement 0 relevé). E2 : 0,627 (59555071 0,149 ; 59589344 0,019 ; 59590613 0,099 ; 59598117 0,289 ; 59601024 0,071). **Cumul E2 + E3 = 2,092 USD** (GO 5 USD). Estimation de `surveillance` à la fin ≈ 1,29 h × 1,1433 + 1,0417 ≈ 2,52 (le forfait de téléchargement du modèle n'a pas été consommé : le run n'a pas démarré).

## Durée pour la planification
Suite complète sur l'instance : 1 h 14 min 48 s (3 186 essais) ; de la création à la fin de la suite : 1 h 17 min.

## Attendus manquants et arrêts
- Suite complète en échec (50) → arrêt de l'amorce avant le run (conduite §5 : instance laissée arrêtée, détruite sur accord de la mère).
- Inventaire final (22:27Z) : aucune instance t06-e2 ni t06-e3 ; 4 instances (R8 ×3, 59288960), toutes arrêtées.
- Rejeu d'E2-6 suspendu (mère).
