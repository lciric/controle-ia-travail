# Devis de la tranche B-β de « Neuron Lens » (Llama 3.1 8B Instruct, nos lentilles R et S) — v2

v2 = v1 (`devis-tranche-b-beta-v1.md`, `b98e53f1…`, archivée) corrigée selon la contre-lecture d'un lecteur neuf
(`contre-lecture-devis-tranche-b-beta-v1.md`, verdict « à corriger » : 1 bloquante, 6 majeures, 9 mineures ; table de reprise au § 8).
Demande (c) de GO-2026-11-17-03 (R-3046, mot de Lazar « b puis c ») : devis contre-lu, **sans aucune dépense**, soumis à Lazar par la mère ;
aucune dépense de B-β sans ligne de calcul neuve. Écrit par la fille « Neuron Lens » le 2026-11-17 (≈ 00:45 UTC). Sources : plan et
devis v1 (§ 4, § 5.3, § 5.4, § 7) et v2 (§ 0, § 3.2 à 3.4) ; texte gelé v6 (`34b88243…`, § B.4) ; devis B-α v2 (`61c394f5…`, § 3) ; les
trois courses de B-α (journaux `journal-course-b-alpha-v1.md` à `-v3.md`) ; banc publié `fit_bench_h100_2026-10-28.log` ; relevé du jour
`releve-prix-vast-20261117T002223Z-v1.tsv` (`1a7cc32c…`, ci-joint).

## 1. Ce que fait B-β (texte gelé v6, § B.4 ; plan v1, § 4.1 et 4.2 ; plan v2, § 3.2)
B-1 (stabilité des lentilles R et S, moitiés paires et impaires), B-5 (côté entrée, `read_S`), B-6 (notre R contre celle de Neuronpedia),
et B-2, B-3, B-4, B-7 **avec notre lentille R**. Étapes : B0 (montage, essais des correctifs et de l'estimateur, **essai d'un Llama
miniature contre la force brute** — garde renvoyée de B-α à B-β —, banc d'un document par lentille) ; B1 (ajuster R et S sur 1 000
documents de DCLM, 128 jetons ; **les deux moitiés en un seul passage** : `02_fit.py` envoie le document i à la moitié i mod 2 et tient
deux accumulateurs, l. 4-8 et 98-120 de la copie ; reprise sur point de sauvegarde) ; B2 (corpus d'activations, comptes, passe
complète) ; B3 (pilotes `07`, lectures `08`) ; B4 (`measure`, `score` avec notre R) ; B5 (`reads_at_firings.py`) ; B6 (manifeste,
scellement, destruction).

**Ce qui est refait, et pourquoi (M5).** Le plan v2 (§ 3.2) prévoyait de recopier les tables de B-α (« sans nouvelle passe du modèle »).
Elles n'existent plus : les tables de la passe, les activations et le fichier `-causal.pt` de `measure` dépassent la limite de fichier de
l'hébergeur de code, sont restés sur les machines et ont été détruits avec elles (commande B-α v5, M6). B-β refait donc le corpus, la
passe complète et `measure` (≈ 1,5 à 2 h). `measure` n'emploie aucune lentille : la refaire ne change pas l'objet, seulement le lot.
Elle se fait au **lot publié 64** si la recourse de l'ablation sur l'A100 de 40 Go le confirme en mémoire (pic estimé ≈ 23,5 GiB ; une
carte de 80 Go en a le triple) ; à défaut, au lot 16, écart déclaré comme en B-α. Si le lieu des lentilles (§ 2, point 6) peut aussi
recevoir `-causal.pt` (≈ 2 Go), `measure` ne serait plus à refaire dans une tranche suivante.

## 2. Préalables, tous sans dépense (rien ne part sans eux)
1. **Condition de passage de B-α à B-β (M3)** : plan v2, § 3.2 ; texte gelé v6, « Seuil » B et « Critères », reproduction. B-α est faite
   (trois courses, R-2915 : verdict « partiel », **aucune chaîne en défaut**, lu par un lecteur neuf) : la condition est **remplie**. Le
   compte rendu à la mère est fait. La recourse de B-7 (GO-2026-11-17-04) ne conditionne pas β, sauf si elle trouve une chaîne en défaut.
2. **Texte gelé de B-β** (R1), écrit, contre-lu par un sous-agent neuf, scellé : critères B-1 à B-7 avec notre R, B-5 **réécrit** (le
   critère « décroissant sur le premier quart » du plan v1 est mal posé, texte gelé v6 § B.4), seuils, plan d'analyse, liste d'arrêt.
3. **Addendum des empreintes** pour B-β (m7) : les empreintes du corpus de la lentille (`dclm.provenance.json` `16957c52…`, révision de
   DCLM `2fa015e4…`) sont **déjà** aux addenda v1 à v3 (« B-β seulement ») ; **manquent** : la liste des 1 000 documents tirés pour Llama
   (tokeniseur de Llama, 128 jetons) et les empreintes des lentilles ajustées, à consigner sur la machine (partie 2 de l'addendum, comme
   en B-α).
4. **Correctifs** du code voisin pour ajuster sur Llama (`02_fit.py`, côtés R et S, point d'entrée de la couche à portes), écrits et
   contre-lus **ici, par lecture seulement** ; **leurs essais tournent sur la machine, à B0** (M4) : l'exécution locale du code voisin
   est refusée (plan v1, § 7 ; règle de Lazar R-2710). Le pire cas de B0 en tient compte (3 h, comme au plan v1). Réemploi des
   correctifs (1) à (3) de B-α.
5. **Lanceur, amorce, dépôt réduit, essai à blanc, commande** : dérivés des pièces de B-α (lanceur v4 : `essais_ok` lu des résultats ;
   copie d'origine, lot de `measure`, entrée idempotente, balayage, clé aux seuls téléchargements) ; `pytest` à épingler (constat porté).
6. **Lieu des lentilles ajustées** (m8 : taille **estimée** de 2 à 10 Go : une matrice de 4 096 × 4 096 en float32 fait 64 Mio, une
   lentille par côté en compte une par couche lue, soit ≈ 2 Gio, davantage avec les accumulateurs des moitiés ; le plan v1 disait
   « ≈ 10 Go » sans calcul ; au-delà, en tout cas, de la limite de l'hébergeur de code : **100 Mo par fichier** selon sa documentation, non
   revérifiée ici ; nos amorces s'arrêtent à 95 Mo, par marge, m6). **Aucun lieu n'est arrêté** ; options pour Lazar :
   (a) aucun lieu : on ne verse que les empreintes et les mesures dérivées, les lentilles sont perdues à la destruction (coût nul ;
   B-β n'est pas rejouable sans refaire B1, ≈ 15 USD) ; (b) un stockage d'objets privé du programme, s'il en existe un (compte ou dépôt
   nouveau sinon : nœud de Lazar ; ≈ 0,1 à 0,3 USD par mois pour 10 Go aux prix courants des stockages d'objets, non relevés ici) ;
   (c) une machine de Lazar, par copie directe (délai et débit à voir avec lui). **Condition de la commande** : la commande de B-β ne
   s'écrit pas sans ce choix.

## 3. La machine (B1 : bloquante corrigée)
Relevé du 2026-11-17T00:22:23Z (filtre exact, m3 : `num_gpus=1 cpu_ram>=64 cpu_cores_effective>=16 disk_space>=200 inet_down>=300
reliability>0.98 cuda_max_good>=13.0 rentable=true`) ; prix à la recherche, **stockage en sus** ; stockage de 200 Go ajouté (m4) :

| carte | offres | prix (USD/h) → avec 200 Go de stockage | trafic (USD/Go) | remarque |
|---|---|---|---|---|
| **H100 SXM 80 Go** | 3 | **2,108 → ≈ 2,145** (Japon) ; 4,642 → ≈ 4,83 ; 4,843 → ≈ 5,03 | 0 ; 0,039 ; 0,038 | carte du banc publié ; **une seule offre au prix exigé** |
| H100 PCIe 80 Go | 1 | 2,348 → ≈ 2,415 (Afrique du Sud) | 0,040 | **retirée** : moins de calcul que la SXM (de l'ordre d'un quart), vitesse non mesurée |
| H100 NVL 94 Go | 3 | 3,415 à 3,665 | 0 à 0,0365 (m2) | au-delà du prix exigé |
| A100 SXM4 80 Go | 7 | 1,104 à 1,973 | 0,004 à 0,039 | **retirée** (B1) |
| A100 PCIe 80 Go | 1 | 1,461 | 0,004 | **retirée** (m1) |
| A100 40 Go | 7 (3 SXM4 + 4 PCIe ; m1) | 0,375 à 0,684 | 0,003 à 0,004 | **retirée** (B1) |
| RTX 6000 Ada 48 Go | 4 | 0,561 à 0,869 | 0,0026 à 0,0143 (m2) | non retenue ; vitesse non mesurée |

**Carte exigée : H100 SXM 80 Go, prix lu sur l'instance ≤ 2,55 USD/h stockage compris. Aucun repli** (comme en B-α) : sans offre au
jour de la course, rien ne part, message à la mère (nœud : autre carte, mot de Lazar). Motif (B1) : le pire cas est bâti sur le banc
d'une H100 SXM ; une A100 serait, selon le contre-lecteur, deux à trois fois plus lente (estimation non mesurée), son pire cas
dépasserait l'arrêt dur, et la minuterie v4 (borne haute 129 600 s) refuse tout prix lu sous 61,2 / 36 = 1,70 USD/h : cinq A100 de 80 Go
sur sept et toutes celles de 40 Go seraient refusées. Un repli exigerait un pire cas chiffré, un prix exigé et une minuterie v5 : nœud,
non proposé. Aucune H200 (exclue sans mot de Lazar).

## 4. Durées et coût
Durées : **mesurées** sur B-α (RTX 4090) quand elles existent ; **publiées** (Qwen3-8B, H100) sinon ; Llama : 0,9 à 1,2 fois Qwen3-8B,
**hypothèse non mesurée** (32 couches contre 36, couches à portes plus larges), levée par le banc de B0.

**B1 (M1, recalculé)** : banc publié 11,2 à 11,8 s par document (H100 SXM, Qwen3-8B) ; deux lentilles × 1 000 documents = 2 000 passages
(les moitiés ne coûtent pas de second passage, § 1) → **6,2 à 6,6 h** au banc ; × 0,9 à 1,2 → **5,6 à 7,9 h attendues**. Pire cas :
deux fois la borne haute du banc (23,6 s par document) × 2 000 = **13,1 h** (la v1 et le plan v1 écrivaient 6,2 à 8,9 h et 13,2 h,
tirés de la plage de 11 à 16 s du README sans coefficient : dérivation fausse, M1).

| étape | attendu | pire cas | plan v2 (§ 3.4) | source |
|---|---|---|---|---|
| B0 montage, environnement, téléchargements, essais des correctifs sur la machine, banc | 0,5 à 1 h | **3 h** (M4) | banc 0,5 h ; montage 2 h au pire | mesuré B-α : environnement 64 à 181 s, poids 72 s à 3 min 30, B0 19 à 41 s ; essais de l'ajustement et banc non mesurés |
| B1 deux lentilles, 1 000 documents chacune | 5,6 à 7,9 h | 13,1 h | 6,2 à 8,9 h ; 13,2 h | ci-dessus |
| B2 corpus, comptes, passe complète | 1,0 à 1,5 h | 2,5 h | recopiées (1,5 h au pire) | mesuré B-α : corpus 2 min 31 à 15 min, passe 61 à 66 min (RTX 4090) ; refaite (§ 1, M5) |
| B3 pilotes et lectures (`07`, `08`) | 0,3 à 0,5 h | 1 h | 1,3 h avec B5 | publié (12 min et 5 à 7 min, H100) |
| B4 `measure` et `score` | 0,5 à 0,8 h | 1,5 h | 0,8 h avec le transfert | mesuré B-α : pilotage 514 s, ablation ≈ 15,5 min au lot 16, `score` ≈ 3 min |
| B5, B6 lectures aux activations, scellement, poussées | 0,5 à 0,8 h | 1,5 h | — | publié, et mesuré B-α (poussées) |
| audit R4 (seconde graine), s'il est déclenché | — | 1 h | — | B-α |
| une machine perdue et remontée (reprise sur point de sauvegarde) | — | 1 h | 1 h | plan v1 |
| **heures** | **8,4 à 12,5 h** | **≈ 24,6 h** | 8,8 à 11,5 h ; 21,2 h | |

| poste | attendu | pire cas | plan v2 |
|---|---|---|---|
| carte (H100 SXM ≈ 2,15 USD/h lus, stockage compris) | **≈ 18 à 27 USD** | 24,6 h × 2,55 (prix exigé) = **62,7 USD** | 21 à 27 ; 63,6 |
| trafic (≈ 30 Go entrants : poids ≈ 16 Go, lentilles de Neuronpedia ≈ 6 Go, environnement ≈ 5 Go, corpus ; m8) | 0 à 1,2 USD | 1,2 USD | — |
| disque 200 Go | compris au prix lu | — | 4 avec le réseau |
| appels de modèles | 0 | 0 | 0 |
| **total** | **≈ 18 à 28 USD** | **≈ 64 USD** | 21 à 27 ; 68 |

**Écart au plan v2 (M6)** : attendu presque égal ; pire cas + 3,4 h (B0 à 3 h faute d'essai local, M4 ; passe refaite, M5), compensé en
dollars par le prix exigé (2,55 contre 3,00).
**Plafond demandé : 68 USD** (plan v2, § 3.4). Arrêt dur à 90 % = 61,2 USD ; le pire cas (≈ 64 USD, trafic compris) le **dépasse de
≈ 2,8 USD** : la garde tronque alors la course à ≈ 23,5 h (61,2 / 2,55 − marge de trafic) ; la troncature ne perd que la fin (B5, B6
ou un audit), les poussées étant faites toutes les 10 minutes ; déclaré. Pour tenir le pire cas entier sous l'arrêt dur, il faudrait
un prix exigé ≤ 2,44 USD/h (l'offre du jour à ≈ 2,15 y tient) ou un plafond de ≈ 72 USD.

## 5. Gardes (M2 : reprises du devis B-α v2, § 3, et adaptées)
| garde | valeur |
|---|---|
| ligne de GO | ligne de calcul neuve, nommée par la mère sur un mot de Lazar ; échéance proposée **2026-11-30** (volet B, plan v2) ; feu écrit avant toute création |
| compte rendu à la mère | **40,8 USD** (60 %), par la garde de dépense v4 ; elle décide de la suite |
| arrêt dur | **61,2 USD** (90 %) : destruction par identifiant, réessayée et vérifiée par l'absence |
| minuterie v4 | durée = 90 % du plafond au prix lu : à 2,55, 86 400 s ; à 2,15, 102 474 s ; bornes 600 à 129 600 s (prix lu ≥ 1,70 exigé par la borne : tenu par la carte exigée) |
| bornes en durée | compte rendu à **12,5 h** (haut de l'attendu) ; rappel à **24,6 h** (pire cas) ; rappel indépendant à 80 % de la minuterie ; échéance de chaque étape écrite dans l'état poussé, dépassement = compte rendu |
| crédit | `can_pay` vrai, `has_billing` vrai, `billing_failed` faux avant la création (champ absent = arrêt) ; crédit < 1 USD en cours de course → arrêt (R-2788, R-2795) ; **le crédit doit couvrir le plafond ou le rechargement automatique être actif** (le crédit relevé en B-α était de l'ordre de 5 à 6 USD) |
| course figée | `gpu_util` ≈ 0 **et** `cpu_util` < 10 % à deux contrôles de suite sans nouvelle poussée → arrêt (R-2800) |
| une seule instance | branche de résultats neuve exigée absente avant la création ; journaux de la minuterie et de la garde commités ; arrêts par PID vérifiés par leurs arguments ; veille et réarmement sur l'échéance absolue après tout redémarrage du conteneur de la session |
| destruction | `vastai destroy instance <ID> -y < /dev/null` ; absence prouvée par `suivi_vast_v6 absente <ID> --non-vide`, jamais sur le code de sortie ; préavis d'une ligne à la mère avant la création et la destruction (R-2883) |
| intouchables | 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, la machine 60988826, `poste-temoin-bailey-*`, toute instance d'une autre session |
| refus | tout refus d'une permission, du crochet ou du classifieur : ni rejoué, ni reformulé, ni contourné ; arrêt et nœud à la mère (R-2864) |

## 6. Leçons de B-α portées
Entrée idempotente et reprise ; `pip` minuté ; clé `HF_TOKEN` aux seuls téléchargements de Llama, retirée ensuite (révocation
recommandée : la clé aura été passée à quatre ou cinq machines) ; balayage des secrets avant chaque poussée ; essai à blanc de
l'environnement exact des essais (variables, chemins, empreintes) et des appels de `measure` ; estimation de la mémoire de pointe de
chaque partie avant la course (pour B1 : pic publié de 20 à 29 Go à lot de 128 sur Qwen3-8B ; Llama a des couches à portes plus larges,
non mesuré ; 80 Go laissent une marge large) ; carte contrôlée par l'amorce (`CARTE_ATTENDUE`) ; aucun résultat lu par la fille
(lecteur neuf, plan scellé).

## 7. Décision demandée (à Lazar, par la mère)
**Décision** : ouvrir ou non une ligne de calcul pour B-β. **Enjeu** : refaire leur chaîne complète sur Llama (nos lentilles R et S),
seule façon de trancher B-1, B-5, B-6 et B-2/B-3/B-7 avec la lentille R ajustée par leur code. Options :
(a) **plafond 68 USD, H100 SXM seule, prix lu ≤ 2,55 USD/h**, aucun repli — avantage : attendu ≈ 18 à 28 USD, le pire cas à 2,8 USD
près sous l'arrêt dur, la carte du banc publié ; inconvénient : une seule offre au bon prix au relevé, la course peut attendre une offre ;
(b) idem avec un prix exigé ≤ 2,44 USD/h — avantage : pire cas entier sous l'arrêt dur ; inconvénient : encore moins d'offres ;
(c) variante économe (S seulement, plan v2 § 0 point 3) — à recalculer avant toute décision (la v1 citait le pire cas de la v2, ≈ 48 USD,
comme un plafond : m5 ; un arrêt dur à ce niveau exigerait ≈ 53 USD de plafond) ; inconvénient : ce n'est plus la reproduction ;
(d) ne pas faire B-β (B-α « partiel » suffit pour la question « utile à un moniteur »).
**Recommandation : (a)**, confiance 0,5 ; **le lieu des lentilles (§ 2, point 6) est une condition de la commande**, à trancher en même
temps que la ligne. Pas de défaut sous 48 heures : c'est une dépense.

## 8. Reprise de la contre-lecture
| point | reprise |
|---|---|
| B1 pire cas hors H100 SXM ; repli incompatible avec la minuterie | acceptée : PCIe et A100 retirées, aucun repli (§ 3) |
| M1 dérivation de B1 | acceptée : base du banc, coefficient appliqué, recalcul (§ 4) |
| M2 gardes de B-α | acceptée : § 5, repris du devis B-α v2 § 3 |
| M3 condition de passage | acceptée : § 2, point 1 |
| M4 essais impossibles ici | acceptée : essais sur la machine à B0, pire cas de B0 à 3 h (§ 2, point 4 ; § 4) |
| M5 refaire passe et `measure` | acceptée : motif dit (tables détruites), lot 64 lié à la recourse (§ 1) |
| M6 écart au plan v2 | acceptée : colonne « plan v2 » et phrase d'écart (§ 4) |
| m1 offres A100 | acceptée (§ 3) |
| m2 trafic NVL et RTX 6000 Ada | acceptée (§ 3) |
| m3 filtre | acceptée (§ 3) |
| m4 prix de l'offre, stockage, trafic | acceptée : prix avec stockage ; l'offre PCIe à trafic 0,040 est retirée (§ 3, § 4) |
| m5 option (c) | acceptée : à recalculer, plafond distingué du pire cas (§ 7) |
| m6 limite de l'hébergeur | acceptée : 100 Mo documentés, non revérifiés ; 95 Mo par marge (§ 2, point 6) |
| m7 préalable 2 | acceptée : ce qui existe et ce qui manque (§ 2, point 3) |
| m8 10 Go et 30 Go | acceptée : estimation et sa base (§ 2, point 6 ; § 4) |
| m9 moitiés | acceptée : un seul passage, deux accumulateurs, lu dans `02_fit.py` (§ 1) |
| question 4 : lieu des lentilles | acceptée : options chiffrées et condition de la commande (§ 2, point 6 ; § 7) |
| question 5 : GO-2026-11-17-03 introuvable dans `registres/go.md` de la branche | la ligne est inscrite par la mère sur `main` ; la branche de la fille ne porte pas `registres/` |
