# Devis de la tranche B-β de « Neuron Lens » (Llama 3.1 8B Instruct, nos lentilles R et S) — v1

Demande (c) de GO-2026-11-17-03 (R-3046, mot de Lazar « b puis c ») : devis contre-lu, **sans aucune dépense**, soumis à Lazar par la
mère ; aucune dépense de B-β sans ligne de calcul neuve. Écrit par la fille « Neuron Lens » le 2026-11-17 (≈ 00:25 UTC). Sources :
plan et devis v1 (§ 4 et § 5.3) et v2 (§ 3.4 : B-β ≈ 22 USD attendus, plafond **68 USD**) ; texte gelé v6 (`34b88243…`, § B.4 : « Hors
de ce texte : tranche B-β (texte séparé, gelé avant β) ») ; les trois courses de B-α (journaux `journal-course-b-alpha-v1.md` à `-v3.md`)
pour les durées **mesurées** ; relevé des prix du jour `releve-prix-vast-20261117T002223Z-v1.tsv` (ci-joint, scellé).

## 1. Ce que fait B-β (texte gelé v6, § B.4 ; plan v1, § 4.1 et 4.2)
B-1 (stabilité des lentilles R et S, moitiés paires et impaires), B-5 (côté entrée, `read_S`), B-6 (notre R contre celle de Neuronpedia),
et B-2, B-3, B-4, B-7 **avec notre lentille R**. Étapes : B0 (montage, essais de l'estimateur du dépôt, **essai d'un Llama miniature
contre la force brute** — garde renvoyée de B-α à B-β —, banc d'un document par lentille) ; B1 (ajuster R et S sur 1 000 documents de
DCLM, 128 jetons, moitiés séparées, reprise sur point de sauvegarde) ; B2 (corpus d'activations, comptes, passe complète) ; B3 (pilotes
`07`, lectures `08`) ; B4 (`measure`, `score` avec notre R) ; B5 (`reads_at_firings.py`) ; B6 (manifeste, scellement, destruction).

## 2. Préalables, tous sans dépense (rien ne part sans eux)
1. **Texte gelé de B-β** (R1), écrit, contre-lu par un sous-agent neuf, scellé : critères B-1 à B-7 avec notre R, B-5 **réécrit** (le
   critère « décroissant sur le premier quart » du plan v1 est mal posé, texte gelé v6 § B.4), seuils, plan d'analyse, liste d'arrêt.
2. **Addendum des empreintes** pour B-β (corpus de la lentille `dclm.provenance.json` `16957c52…`, révision de DCLM `2fa015e4…`).
3. **Correctifs** du code voisin pour ajuster sur Llama (`02_fit.py`, côtés R et S, point d'entrée de la couche à portes), contre-lus,
   avec leurs essais (miniature contre force brute) ; réemploi des correctifs (1) à (3) de B-α.
4. **Lanceur, amorce, dépôt réduit, essai à blanc, commande** : à dériver des pièces de B-α (lanceur v3 et ses leçons : copie
   d'origine, lot de `measure`, entrée idempotente, balayage, clé aux seuls téléchargements). Constat à porter (`essais_ok` lu des
   résultats, `constats-a-porter-b-alpha-v1.md`).
5. **Où mettre les lentilles ajustées** (≈ 10 Go au plan v1 ; au-delà de la limite de l'hébergeur de code à 95 Mo par fichier) : le
   plan v1 dit « copiées hors de la machine, gardées hors du dépôt git ». **Aucun lieu n'est arrêté** : un stockage neuf serait un compte
   ou un dépôt nouveau (nœud de Lazar). Sans lieu, on ne verse que les empreintes et les mesures dérivées, et les lentilles sont perdues
   à la destruction (comme `-causal.pt` en B-α). **Décision à prendre avant la commande.**

## 3. La machine
Les lentilles s'ajustent sur une carte de grande mémoire (banc publié : pic de 20 à 29 Go à lot de 128 ; 48 Go compilé à lot de 256 ;
11,2 à 11,8 s par document sur une H100, `fit_bench_h100_2026-10-28.log`). Relevé du 2026-11-17T00:22:23Z (filtre : une carte, ≥ 64 Go de
mémoire vive, ≥ 16 cœurs, ≥ 200 Go de disque, fiabilité > 0,98, CUDA ≥ 13.0) :

| carte | offres | prix (USD/h, à la recherche, stockage en sus) | trafic (USD/Go) | remarque |
|---|---|---|---|---|
| **H100 SXM 80 Go** | 3 | **2,108** (Japon), puis 4,642 et 4,843 | 0 à 0,039 | carte des durées publiées ; **une seule offre au prix du devis** |
| H100 PCIe 80 Go | 1 | 2,348 (Afrique du Sud) | 0,040 | |
| H100 NVL 94 Go | 3 | 3,415 à 3,665 | 0 | au-delà du prix plafond de 3,00 |
| A100 SXM4 80 Go | 6 | 1,104 à 1,973 | 0,004 à 0,039 | repli, vitesse non mesurée |
| A100 40 Go | 8 | 0,375 à 0,684 | 0,003 à 0,004 | lot de 128 seulement (pic 20 à 29 Go) |
| RTX 6000 Ada 48 Go | 4 | 0,561 à 0,869 | 0,003 | lot de 128 ; vitesse non mesurée |

**Recommandation** : H100 (SXM ou PCIe), prix lu ≤ 3,00 USD/h (prix plafond du plan v1, inchangé) ; **repli** : A100 de 80 Go, puis de
40 Go à lot de 128, décidé par le banc de B0 avant d'engager les heures. Aucune H200 (exclue sans mot de Lazar).

## 4. Durées et coût

Durées : **mesurées** sur B-α (RTX 4090) quand elles existent ; **publiées** (Qwen3-8B, H100) sinon ; Llama : 0,9 à 1,2 fois Qwen3-8B,
**hypothèse non mesurée**, levée par le banc.

| étape | attendu | pire cas | source |
|---|---|---|---|
| B0 montage, environnement, téléchargements, essais, banc | 0,5 à 1 h | 2 h | mesuré B-α : environnement 1 à 3 min, poids 1 à 4 min, B0 19 à 41 s ; banc et correctifs de l'ajustement non mesurés |
| B1 deux lentilles (R, S), 1 000 documents chacune | 6,2 à 8,9 h | 13,2 h | publié (≈ 3 h par lentille sur une H100), × 0,9 à 1,2 ; pire cas 1,5 fois la borne haute |
| B2 corpus, comptes, passe complète | 1,0 à 1,5 h | 2,5 h | mesuré B-α : corpus 2,5 à 15 min, passe 61 à 66 min sur une RTX 4090 |
| B3 pilotes et lectures (`07`, `08`) | 0,3 à 0,5 h | 1 h | publié (12 min et 5 à 7 min, H100) |
| B4 `measure` (lot de 64 : la mémoire d'une carte de 80 Go le permet) et `score` | 0,5 à 0,8 h | 1,5 h | mesuré B-α : pilotage 514 s, ablation ≈ 15 min à lot 16, `score` ≈ 3 min |
| B5, B6 lectures aux activations, scellement, poussées | 0,5 à 0,8 h | 1,5 h | publié, et mesuré B-α (poussées) |
| audit R4 (seconde graine), s'il est déclenché | — | 1 h | B-α |
| une machine perdue et remontée (les ajustements reprennent sur point de sauvegarde) | — | 1 h | plan v1 |
| **heures** | **9 à 13,5 h** | **≈ 23,7 h** | |

| poste | attendu | pire cas |
|---|---|---|
| carte (H100 à ≈ 2,2 USD/h lus, stockage compris) | **≈ 20 à 30 USD** | 23,7 h × 3,00 (prix plafond) = **71 USD** |
| disque 200 Go et trafic (≈ 30 Go entrants) | ≈ 0,5 USD | 3 USD |
| appels de modèles | 0 | 0 |
| **total** | **≈ 21 à 31 USD** | **≈ 74 USD** |

**Plafond demandé : 68 USD** (celui du plan v2, § 3.4), ce qui suppose de tenir le pire cas sous l'arrêt dur à 90 % (61,2 USD) : à
3,00 USD/h, 61,2 USD = 20,4 h ; au prix du jour (≈ 2,2), 27,8 h. **Le pire cas ci-dessus (23,7 h) tient sous l'arrêt dur au prix du jour,
pas au prix plafond** : comme en B-α (R-2887), le **prix lu exigé** est fixé pour que le pire cas tienne : **≤ 2,55 USD/h** (23,7 h ×
2,55 = 60,4 USD < 61,2). Si Lazar préfère garder 3,00 USD/h, le plafond doit monter à ≈ 80 USD (pire cas 74 + marge). Option économe
(plan v2, § 0, point 3 : réemployer la lentille R publique, n'ajuster que S) : ≈ 13 à 17 USD attendus, pire cas ≈ 48 USD ; on y perd B-1
pour R, B-6 et `read_R` ; non recommandée (ce n'est plus « refaire leur chaîne »).

Gardes : compte rendu à la mère à 60 % du plafond (40,8 USD), arrêt dur et destruction vérifiée à 90 % (61,2 USD) par la garde de
dépense v4 ; minuterie v4 (durée = 90 % du plafond au prix lu : à 2,55, 86 400 s ; bornes de la v4 : 600 à 129 600 s) ; rappels en
durée à la borne haute de l'attendu (13,5 h) et au pire cas (23,7 h) ; une seule instance ; destruction par identifiant (R10), absence
prouvée par `suivi_vast_v6 absente --non-vide`.

## 5. Leçons de B-α portées
Entrée idempotente et reprise ; `pip` minuté ; clé `HF_TOKEN` aux seuls téléchargements de Llama, retirée ensuite ; balayage des
secrets avant chaque poussée ; essai à blanc de l'environnement exact des essais (variables, chemins, empreintes) et des appels de
`measure` ; estimation de la mémoire de pointe de chaque partie avant la course ; préavis d'une ligne à la mère avant la création et la
destruction (R-2883) ; aucun résultat lu par la fille (lecteur neuf, plan scellé).

## 6. Décision demandée (à Lazar, par la mère)
Ligne de calcul neuve pour B-β. Enjeu : refaire leur chaîne complète sur Llama (nos lentilles R et S), seule façon de trancher B-1, B-5,
B-6 et B-2/B-3/B-7 avec la lentille R ajustée par leur code. Options :
(a) **plafond 68 USD, prix lu ≤ 2,55 USD/h**, H100 (repli A100 80 Go) — avantage : pire cas sous l'arrêt dur ; inconvénient : une seule
H100 au bon prix au relevé, le repli A100 n'a pas de vitesse mesurée ;
(b) plafond ≈ 80 USD, prix lu ≤ 3,00 USD/h — avantage : plus d'offres ; inconvénient : plus cher au pire ;
(c) option économe (S seulement), plafond ≈ 48 USD — avantage : moins cher ; inconvénient : ce n'est plus la reproduction ;
(d) ne pas faire B-β (B-α « partiel » suffit pour la question « utile à un moniteur »).
**Recommandation : (a)**, confiance 0,5 ; et le lieu des lentilles ajustées (§ 2, point 5) à trancher avant la commande. Pas de défaut sous
48 heures : c'est une dépense.
