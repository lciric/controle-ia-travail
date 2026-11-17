# La lecture contre ablation (B-7) à lot 64 tient-elle dans une RTX 4090 ? — note v1

Écrite par la fille « Neuron Lens » le 2026-11-17 (≈ 00:20 UTC), premier point de la demande (b) de GO-2026-11-17-03 (R-3046) :
recourir la seule lecture contre ablation de la tranche B-α avec le lot publié de 64, pour lever l'écart de lot de la troisième course
(lot 16 à l'ablation, R-2914, R-2915). Aucune location, aucune dépense.

## Réponse : non (avec un écart à la ligne pour une autre carte)
1. **Mesuré** (relance du 2026-11-15, instance 60773264, `diag/20261115-102017-neuron-lens-b-alpha/journaux/measure.log`) : à lot 64,
   l'ablation échoue dès la couche 0 par mémoire épuisée : « Tried to allocate 896.00 MiB. GPU 0 has a total capacity of 23.57 GiB of
   which 100.75 MiB is free. […] 21.07 GiB is allocated by PyTorch, and 1.93 GiB is reserved by PyTorch but unallocated » ; hors PyTorch
   ≈ 0,46 GiB.
2. **Au mieux, sans aucune fragmentation** (réglage de l'allocateur `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`, qui ne change pas
   le code ni les résultats) : au point d'échec, la couche à portes a deux tenseurs de 0,875 GiB vivants (sortie de `gate_proj` et son
   activation) et doit encore en allouer deux (sortie de `up_proj`, produit), puis la sortie de `down_proj` (≈ 0,25 GiB). Pic alloué
   ≈ 21,07 + 0,875 + 0,875 + 0,25 ≈ **23,07 GiB**, plus 0,46 hors PyTorch ≈ **23,53 GiB** contre **23,57 GiB** : **marge ≈ 0,04 GiB**
   (0,29 GiB si la sortie est allouée après la libération des intermédiaires). Une marge de cet ordre n'est pas tenable : tout tenseur
   de plus, tout cache de l'allocateur ou un autre ordre d'allocation la dépasse. **Lot 64 sur une RTX 4090 : non établi, très
   probablement impossible.**
3. **Il faut donc une autre carte** : écart à la ligne GO-2026-11-14-06 (« une RTX 4090 »), nœud de Lazar (GO-2026-11-17-03 le prévoit).

## Cartes possibles (relevé des offres du 2026-11-17T00:20:51Z, mêmes filtres que la commande v5, sans plafond de prix)
| carte | mémoire (`gpu_ram`) | offres | moins chère (USD/h, à la recherche, stockage en sus) | trafic (USD/Go) | marge estimée à lot 64 (mémoire − ≈ 23,5 GiB de pic, hors fragmentation) |
|---|---|---|---|---|---|
| RTX 5090 | 32 607 Mio | 36 | 0,4860 | 0,0156 | ≈ 8,3 GiB |
| A100 SXM4 | 39 936 Mio | 9 | 0,5494 | 0,0026 | ≈ 15,5 GiB |
| A100 PCIe | 40 960 Mio | 5 | 0,5810 | 0,0040 | ≈ 16,5 GiB |
| RTX 6000 Ada | 49 140 Mio | 4 | 0,5614 | 0,0039 | ≈ 24,5 GiB |
| L40S | 46 068 Mio | 3 | 0,8009 | 0,0091 | ≈ 21,5 GiB |
| RTX A6000 | 48 Go | 0 | — | — | — |

## Ce qu'un changement de carte change (à peser par Lazar)
- Les auteurs notent que **les effets faibles dépendent du matériel** (findings l. 207-209, cité au devis v2, § 2), et B-7 (« ablate win »,
  couches 0 à 15) est **la mesure la plus exposée** : recourir B-7 sur une autre carte lève l'écart de lot mais en ouvre un de matériel,
  par rapport à la troisième course (RTX 4090, lot 16) et à la référence publiée.
- La course ne peut pas rejouer la seule ablation : `measure` fait le pilotage puis l'ablation, et il lui faut les tables de la passe
  complète (`06_activations.py`), perdues avec l'instance. Une commande B-7 refait donc la chaîne jusqu'à `measure` (≈ 1,5 à 2 h), puis
  `score` et les verdicts ; le devis en tient compte (≈ 1 à 1,5 USD sur une RTX 5090, hors trafic).
- Une RTX 5090 (architecture plus récente) demande `torch` avec sa prise en charge ; non vérifié ici.

## Statut
Arrêt de la demande (b) à ce point, comme le prescrit GO-2026-11-17-03 : message à la mère, qui le porte à Lazar. Aucune commande n'est
écrite avant son mot (choix de la carte).
