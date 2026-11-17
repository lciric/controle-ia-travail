# Devis de la recourse de la lecture contre ablation (B-7) de B-α sur une A100 SXM4 40 Go, aux lots 16 et 64 — v1

Écrit par la fille « Neuron Lens » le 2026-11-17 (≈ 00:45 UTC), troisième pièce demandée par GO-2026-11-17-04. Ligne **GO-2026-11-14-06**
(12 USD, échéance 2026-11-30). Commande : `commande-b-alpha-v6.md`. Relevé du jour : `releve-prix-vast-a100-20261117T003231Z-v1.tsv`
(ci-joint, scellé). Aucune dépense avant le feu de la mère.

## 1. Offres du jour (2026-11-17T00:32:31Z ; filtre de la commande v6, étape 4, sans borne de prix)
| offre | mémoire (Mio) | prix à la recherche (USD/h, stockage en sus) | stockage (USD/Go/mois) | + stockage 150 Go (USD/h) | trafic entrant (USD/Go) | fiabilité | lieu |
|---|---|---|---|---|---|---|---|
| 58155312 | 39 936 | 0,5361 | 0,40 | ≈ 0,083 → ≈ 0,62 | 0,0026 | 0,9959 | Alberta (CA) |
| 56423175 | 39 936 | 0,5494 | 0,40 | ≈ 0,083 → ≈ 0,63 | 0,0026 | 0,9949 | Alberta (CA) |
| 59897131 | 40 960 | 0,6361 | 0,20 | ≈ 0,042 → ≈ 0,68 | 0,0026 | 0,98 | Royaume-Uni |
| 48716614 | 40 960 | 0,6681 | 0,20 | ≈ 0,042 → ≈ 0,71 | 0,0026 | 0,9983 | Massachusetts (US) |

Quatre offres tiennent sous le prix lu exigé de 0,73 USD/h stockage compris (borne R-2887 gardée) ; la marge est mince pour les deux
dernières (le prix lu sur l'instance fait foi, étape 8 : au-delà de 0,73, destruction).

## 2. Durées
| partie | attendu | pire cas codé (échéances du lanceur v4) | source |
|---|---|---|---|
| montage, environnement, essais | 0,1 à 0,3 h | 2,2 h (pip sous `timeout` 2 × 3 600 s) | mesuré, troisième course : quelques minutes |
| chaîne du lot 16 jusqu'aux verdicts (comme la troisième course) | ≈ 2,1 h | 7,8 h | **mesuré** sur une RTX 4090 : 2 h 6 min 43 s de location au total ; l'A100 n'est pas plus lente pour ces passes en bf16 (non mesuré) |
| seconde série : bascule, `measure` au lot 64, `score`, grandeurs, verdicts | ≈ 0,5 h | 1,95 h | mesuré en troisième course : pilotage 514 s, ablation ≈ 15 min au lot 16 (le lot 64 fait les mêmes jetons en moins de passes), `score` ≈ 3 min |
| audits R4, s'ils sont requis | — | 2,8 h (lot 16) + 1,5 h (lot 64) + 0,8 h (« tout négatif ») | échéances codées |
| **total** | **≈ 2,7 à 3,0 h** | **≈ 17 h** sans troncature | |

## 3. Coût
| poste | attendu | pire cas |
|---|---|---|
| carte, stockage compris (≈ 0,62 à 0,73 USD/h) | ≈ 1,7 à 2,2 USD | tronqué par l'arrêt dur de la garde : **7,65 USD** |
| trafic (≈ 25 Go entrants à 0,0026 ; sortants faibles) | ≈ 0,1 USD | 0,3 USD |
| **total de la course** | **≈ 1,8 à 2,3 USD** | **≈ 7,95 USD** |
| **ligne GO-2026-11-14-06 après la course** (≈ 2,1 USD déjà faits) | **≈ 3,9 à 4,4 USD** sur 12 | **≈ 10,05 USD** sur 12, sous l'arrêt dur de la ligne (10,80) |

Le pire cas codé (≈ 17 h × 0,73 ≈ 12,4 USD) **ne tient pas** sous le plafond : comme en B-α, la garde v4 (plafond 8,5 USD pour cette
course, 60 % : 5,10 ; 90 % : 7,65) et la minuterie (D = 90 % de 8,5 au prix lu : 10,5 h à 0,73, 12,3 h à 0,62) **tronquent** la
course. Une troncature ne perd que les étapes non faites : les poussées ont lieu toutes les 10 minutes, et la chaîne du lot 16 (pire
cas codé 10 h avec le montage) finit avant la seconde série. Déclaré : au pire cas codé de chaque étape, la seconde série peut ne pas
être atteinte avant l'arrêt dur ; la mère est prévenue à 4,8 h et décide à 8,0 h (rappels de la commande, étape 11).

## 4. Gardes et réserves
- Une seule instance ; destruction par identifiant (R10) ; absence prouvée par `suivi_vast_v6 absente <ID> --non-vide`.
- La mémoire de l'A100 au lot 64 est estimée (marge ≈ 15,5 GiB), non mesurée ; échec par mémoire : les résultats du lot 16 sont déjà
  poussés, destruction, rapport.
- `HF_TOKEN` passe une quatrième fois à une machine louée (GO-2026-11-15-04 : téléchargement de Llama seulement, retiré ensuite) ;
  révocation recommandée à Lazar après la course.
