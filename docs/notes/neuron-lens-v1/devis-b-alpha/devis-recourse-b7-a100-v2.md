# Devis de la recourse de la lecture contre ablation (B-7) de B-α sur une A100 SXM4 40 Go, aux lots 16 et 64 — v2

v2 = v1 (`devis-recourse-b7-a100-v1.md`, `1275ae84…`, archivée) avec la majeure M4 et les mineures 6 et 7 de la contre-lecture de la
commande v6 : scénario des audits chiffré, rappels recalés, ordre des séries pesé, origine du plafond et de la dépense déjà faite.

Écrit par la fille « Neuron Lens » le 2026-11-17 (≈ 00:45 UTC), troisième pièce demandée par GO-2026-11-17-04. Ligne **GO-2026-11-14-06**
(12 USD, échéance 2026-11-30). Commande : `commande-b-alpha-v7.md`. Relevé du jour : `releve-prix-vast-a100-20261117T003231Z-v1.tsv`
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
| **total sans audit** | **≈ 2,7 à 3,0 h** (4,8 h aux échéances codées) | **≈ 17 h** sans troncature | |
| **total avec les deux audits « trop beau »** (v2) | ≈ 3,7 à 4,0 h mesurés à la troisième course (un audit ≈ `measure` + `score` + grandeurs ≈ 0,5 h) ; **6,9 h** aux échéances codées (+ 1,3 et + 0,8 h) | inchangé | le déclencheur lit le pilotage, même calcul aux deux séries : requis à l'un, il l'est en principe à l'autre |

## 3. Coût
| poste | attendu | pire cas |
|---|---|---|
| carte, stockage compris (≈ 0,62 à 0,73 USD/h) | ≈ 1,7 à 2,2 USD | tronqué par l'arrêt dur de la garde : **7,65 USD** |
| trafic (≈ 25 Go entrants à 0,0026 ; sortants faibles) | ≈ 0,1 USD | 0,3 USD |
| **total de la course** | **≈ 1,8 à 2,3 USD** ; avec les deux audits ≈ 2,5 à 3,0 USD (+ ≈ 0,7 USD mesurés ; + 1,5 USD aux échéances codées) | **≈ 7,95 USD** |
| **ligne GO-2026-11-14-06 après la course** (≈ 2,1 USD déjà faits : compte large de 0,06 + 0,71 + 0,1 + 1,05 + 0,1 = 2,02 USD, journaux des trois courses ; la mère tient le compte exact au registre) | **≈ 3,9 à 4,4 USD** sur 12 | **≈ 10,05 USD** sur 12, sous l'arrêt dur de la ligne (10,80) |

**Plafond de la garde : 8,5 USD**, choisi pour que son seuil de 60 % tombe sur celui de la ligne : 2,1 + 0,6 × 8,5 = 7,2 USD (60 % de 12),
et son arrêt dur sous celui de la ligne : 2,1 + 0,9 × 8,5 = 9,75 < 10,80.
Le pire cas codé (≈ 17 h × 0,73 ≈ 12,4 USD) **ne tient pas** sous le plafond : comme en B-α, la garde v4 (plafond 8,5 USD pour cette
course, 60 % : 5,10 ; 90 % : 7,65) et la minuterie (D = 90 % de 8,5 au prix lu : 10,5 h à 0,73, 12,3 h à 0,62) **tronquent** la
course. Une troncature ne perd que les étapes non faites : les poussées ont lieu toutes les 10 minutes, et la chaîne du lot 16 (pire
cas codé 10 h avec le montage) finit avant la seconde série. Déclaré : au pire cas codé de chaque étape, la seconde série peut ne pas
être atteinte avant l'arrêt dur. **Rappels** (v2) : compte rendu à **4,8 h** (attendu codé sans audit), à **6,9 h** (attendu codé avec les
deux audits) ; à **9,0 h**, la mère décide (avant la minuterie : 10,5 h à 0,73, 12,3 h à 0,62) ; et à 80 % de la minuterie.
**Ordre des séries, pesé** (v2) : la seconde série (lot 64), celle que la recourse vient chercher, passe après la série du lot 16 et son
audit éventuel. Motif : la série du lot 16 est la comparaison au matériel (A100 contre RTX 4090) et le cas sain de déterminisme ; sans
elle, un écart de B-7 au lot 64 ne pourrait être attribué ni au lot ni à la carte. Coût : au pire cas codé, la seconde série peut être
coupée par l'arrêt dur ; aux durées mesurées, elle finit vers 4 h, loin des 10,5 h de la minuterie. L'ordre inverse (lot 64 d'abord)
est possible par un lanceur v6 si la mère le préfère.

## 4. Gardes et réserves
- Une seule instance ; destruction par identifiant (R10) ; absence prouvée par `suivi_vast_v6 absente <ID> --non-vide`.
- La mémoire de l'A100 au lot 64 est estimée (marge ≈ 15,5 GiB), non mesurée ; échec par mémoire : les résultats du lot 16 sont déjà
  poussés, destruction, rapport.
- `HF_TOKEN` passe une quatrième fois à une machine louée (GO-2026-11-15-04 : téléchargement de Llama seulement, retiré ensuite) ;
  révocation recommandée à Lazar après la course.
