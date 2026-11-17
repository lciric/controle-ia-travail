# Devis de la tranche B-β de « Neuron Lens » (Llama 3.1 8B Instruct, nos lentilles R et S) — v4

v4 = v3 (`devis-tranche-b-beta-v3.md`, `77719c0c…`, archivée), corrigée selon la troisième contre-lecture
(`contre-lecture-devis-tranche-b-beta-v3.md` : « à corriger », aucune bloquante, 3 majeures, 9 mineures). La table de reprise est au § 10,
et un relevé neuf `releve-prix-vast-h100-20261117T012309Z-v1.tsv` est joint. Écrite le 2026-11-17 vers 01:30 UTC.

v3 = v2 (`devis-tranche-b-beta-v2.md`, `abc7b727…`, archivée) corrigée selon sa contre-lecture par un second lecteur neuf
(`contre-lecture-devis-tranche-b-beta-v2.md` : « à corriger », aucune bloquante, 3 majeures, 9 mineures ; table de reprise au § 9) ;
chiffres de taille relus dans le code voisin (`02_fit.py` l. 1-10 ; `neuron_lens/transport.py` l. 45-58). v2 = v1 (`devis-tranche-b-beta-v1.md`, `b98e53f1…`, archivée) corrigée selon la contre-lecture d'un lecteur neuf
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
deux accumulateurs : `02_fit.py` l. 4-5 et la boucle unique l. 168-177, `neuron_lens/transport.py` l. 49-57 ; reprise sur point de sauvegarde) ; B2 (corpus d'activations, comptes, passe
complète) ; B3 (pilotes `07`, lectures `08`) ; B4 (`measure`, `score` avec notre R) ; B5 (`reads_at_firings.py`) ; B6 (manifeste,
scellement, destruction).

**Ce qui est refait, et pourquoi (M5).** Le plan v2 (§ 3.2) prévoyait de recopier les tables de B-α (« sans nouvelle passe du modèle »).
Elles n'existent plus : les tables de la passe, les activations et le fichier `-causal.pt` de `measure` dépassent la limite de fichier de
l'hébergeur de code, sont restés sur les machines et ont été détruits avec elles (commande B-α v5, M6). B-β refait donc le corpus, la
passe complète et `measure` (≈ 1,5 à 2,3 h). `measure` n'emploie aucune lentille : la refaire ne change pas l'objet, seulement le lot.
Elle se fait au **lot publié 64** : pic estimé ≈ 23,5 GiB (`devis-b-alpha/memoire-ablation-lot64-rtx4090-v1.md`, § 2), contre 80 Go de
carte ; la recourse de l'ablation sur l'A100, si elle part, le mesure en plus. Si le lieu des lentilles (§ 2, point 6) peut aussi recevoir
`-causal.pt` (≈ 2,6 Go pour Llama, d'après les 2,9 Go publiés pour Qwen3-8B), `measure` ne serait plus à refaire dans une tranche suivante.

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
6. **Lieu des lentilles ajustées** (taille **calculée**, majeure 1 de la v2) : le point de sauvegarde de `02_fit.py` garde, par lentille,
   deux cibles × deux moitiés × une matrice de 4 096 × 4 096 en float32 (64 Mio) par couche (`transport.py` l. 49-57 : `sums[(cible,
   moitié)]` de forme `[couches, d, d]`) : ≈ 32 × 4 × 64 Mio ≈ **8 Gio par lentille, ≈ 16 Gio (≈ 17 Go) pour R et S** ; les moyennes seules (lentilles exportées) en font la
   moitié, ≈ 8 Gio **pour les deux**. Contrôle : avec le nombre de couches lues par cible de Qwen3-8B (71 et 72 emplacements), la même
   formule redonne les 9,5 et 9,7 Go écrits (`02_fit.py` l. 9-10 ; v4, m-D) C'est au-delà de la limite de l'hébergeur de code : **100 Mo par fichier** selon sa documentation, non revérifiée
   ici ; nos amorces s'arrêtent à 95 Mo, par marge. **Aucun lieu n'est arrêté** ; options pour Lazar :
   (a) aucun lieu : on ne verse que les empreintes et les mesures dérivées ; les lentilles **et le point de sauvegarde** sont perdus à la
   destruction (coût nul ; B-β n'est pas rejouable sans refaire B1, ≈ 15 USD) ;
   (b) un stockage d'objets privé du programme, s'il en existe un (compte ou dépôt nouveau sinon : nœud de Lazar ; de l'ordre de 0,2 à
   0,5 USD par mois pour 8 à 17 Go aux prix courants, non relevés ici) ; il permet aussi d'y copier le point de sauvegarde pendant B1
   (§ 4, perte de machine) ;
   (c) une machine de Lazar, par copie directe (≈ 17 Go : ≈ 45 min à 50 Mbit/s ; délai et débit à voir avec lui).
   **Condition de la commande** : la commande de B-β ne s'écrit pas sans ce choix.

## 3. La machine (B1 : bloquante corrigée)
Relevé du 2026-11-17T00:22:23Z (filtre exact, m3 : `num_gpus=1 cpu_ram>=64 cpu_cores_effective>=16 disk_space>=200 inet_down>=300
reliability>0.98 cuda_max_good>=13.0 rentable=true`) ; prix à la recherche, **stockage en sus** ; stockage de 200 Go ajouté (m4) :

| carte | offres | prix (USD/h) → avec 200 Go de stockage | trafic (USD/Go) | remarque |
|---|---|---|---|---|
| **H100 SXM 80 Go** | 3 | **2,108 → ≈ 2,145** (Japon) ; 4,642 → ≈ 4,83 ; 4,843 → ≈ 5,03 | 0 ; 0,039 ; 0,038 | carte du banc publié ; **une seule offre au prix exigé** |
| H100 PCIe 80 Go | 1 | 2,348 → ≈ 2,415 (Afrique du Sud) | 0,040 | **retirée** : moins de calcul que la SXM (de l'ordre d'un quart), vitesse non mesurée |
| H100 NVL 94 Go | 3 | 3,415 à 3,665 | 0 à 0,0365 (m2) | au-delà du prix exigé |
| A100 SXM4 80 Go | 6 | 1,104 à 1,973 | 0,004 à 0,039 | **retirée** (B1) |
| A100 PCIe 80 Go | 1 | 1,461 | 0,004 | **retirée** (m1) |
| A100 40 Go | 7 (3 SXM4 + 4 PCIe ; m1) | 0,375 à 0,684 | 0,003 à 0,004 | **retirée** (B1) |
| RTX 6000 Ada 48 Go | 4 | 0,561 à 0,869 | 0,0026 à 0,0143 (m2) | non retenue ; vitesse non mesurée |

**Carte exigée : H100 SXM 80 Go, prix lu sur l'instance ≤ 2,25 USD/h stockage compris** (§ 4), **débit montant ≥ 200 Mbit/s**
(`inet_up>=200`, pour la copie des lentilles), **trafic sortant ≤ 0,04 USD/Go** (`inet_up_cost<=0.04`, v4) ; **aucun repli** (comme en B-α) : sans offre au
jour de la course, rien ne part, message à la mère (nœud : autre carte, mot de Lazar). Motif (B1) : le pire cas est bâti sur le banc
d'une H100 SXM ; une A100 serait, selon le contre-lecteur, deux à trois fois plus lente (estimation non mesurée), son pire cas
dépasserait l'arrêt dur, et la minuterie v4 (borne haute 129 600 s) refuse tout prix lu sous 61,2 / 36 = 1,70 USD/h : six A100 de 80 Go
sur sept (cinq SXM4 sur six, et la PCIe) et toutes celles de 40 Go seraient refusées. Un repli exigerait un pire cas chiffré, un prix exigé et une minuterie v5 : nœud,
non proposé. Aucune H200 (exclue sans mot de Lazar).
**Disponibilité, non établie (v4, majeure 1)** : le relevé de 00:22Z n'a pas de colonne de débit montant ; l'offre du Japon (≈ 2,145) n'est
donc pas vérifiée au filtre complet. Le relevé neuf `releve-prix-vast-h100-20261117T012309Z-v1.tsv` (H100 SXM, même filtre, sans borne de débit ni de prix)
ne compte **aucune offre** à 01:23Z. Les offres de H100 SXM vont et viennent : la commande relèvera le jour de la course ; sans offre au
filtre complet, rien ne part.

## 4. Durées et coût
Durées : **mesurées** sur B-α (RTX 4090) quand elles existent ; **publiées** (Qwen3-8B, H100) sinon ; Llama : 0,9 à 1,2 fois Qwen3-8B,
**hypothèse non mesurée** (32 couches contre 36, couches à portes plus larges), levée par le banc de B0.

**B1 (M1, recalculé)** : banc publié 11,2 à 11,8 s par document (H100 SXM, Qwen3-8B, documents d'exactement 128 jetons,
`torch.compile(dynamic=False)`) ; deux lentilles × 1 000 documents = 2 000 passages (les moitiés ne coûtent pas de second passage, § 1)
→ **6,2 à 6,6 h** au banc ; × 0,9 à 1,2 → **5,6 à 7,9 h attendues**. Pire cas : deux fois la borne haute du banc (23,6 s par document)
× 2 000 = **13,1 h**. **Sauvegardes** (absentes du banc) : `--save-minutes 60` (au lieu de 10). Au pire, 13,1 h d'ajustement font ≈ 14
sauvegardes de ≈ 8 Gio, à 1 à 2 min chacune sur le disque local (**non mesuré** ; à mesurer à la première sauvegarde) : + 0,5 h au pire
(v4, m-A ; la v3 comptait 0,3 h) ; + 0,1 à 0,3 h attendus. Avec le lieu (b), une sauvegarde sur trois est copiée vers lui (≈ 5 copies de
≈ 8,6 Go au pire, ≈ 6 min chacune à 200 Mbit/s : + 0,5 h au pire ; v4, majeure 2). Documents plus courts que 128 jetons : recompilations
de 15 à 37 s (m-7) ; elles sont évitées par le **tirage** de documents d'au moins 128 jetons, coupés à 128 (v4, m-H : le banc d'un seul
document ne les mesure pas).

| étape | attendu | pire cas | plan v2 (§ 3.4) | source |
|---|---|---|---|---|
| B0 montage, environnement, téléchargements, essais des correctifs sur la machine, banc | 0,5 à 1 h | **3 h** (M4) | banc 0,5 h ; montage 2 h au pire | mesuré B-α : environnement 64 à 181 s, poids 72 s à 3 min 30, B0 19 à 41 s ; essais de l'ajustement et banc non mesurés |
| B1 deux lentilles, 1 000 documents chacune, sauvegardes et copies (b) comprises | 5,7 à 8,5 h | 14,1 h | 6,2 à 8,9 h ; 13,2 h | ci-dessus |
| B2 corpus, comptes, passe complète | 1,0 à 1,5 h | 2,5 h | recopiées (1,5 h au pire) | mesuré B-α : corpus 2 min 31 à 15 min, passe 61 à 66 min (RTX 4090) ; refaite (§ 1, M5) |
| B3 pilotes et lectures (`07`, `08`) | 0,3 à 0,5 h | 1 h | 1,3 h avec B5 | publié (12 min et 5 à 7 min, H100) |
| B4 `measure` (lot 64) et `score` | 0,5 à 0,8 h | 1,5 h | 0,8 h avec le transfert | mesuré B-α : pilotage 514 s, ablation ≈ 15,5 min au lot 16, `score` ≈ 3 min |
| B5, B6 lectures aux activations, scellement, poussées | 0,5 à 0,8 h | 1,5 h | — | publié, et mesuré B-α (poussées) |
| B6 copie des lentilles vers leur lieu (≈ 8 à 17 Go ; options (b), (c) seulement ; rien pour (a)) | 0,2 à 0,3 h | 0,5 h | — | ≈ 12 min pour 17 Go à 200 Mbit/s, débit exigé ; pire cas à moitié de ce débit (v4, m-E) |
| audit R4 (seconde graine), s'il est déclenché | — | 1 h | — | B-α |
| **heures** | **8,7 à 13,4 h** | **≈ 25,1 h** | 8,8 à 11,5 h ; 21,2 h | |

**Perte de la machine** (v4, majeure 3). **Détection** : l'instance n'est plus « running » au suivi, ou l'état poussé n'avance plus depuis
30 minutes avec le journal muet, ou la course est figée (§ 5). **Règle : arrêt.** Rien n'est relancé ; compte rendu à la mère ; nœud de
Lazar. Toute reprise sur une nouvelle machine est un **devis neuf** : elle n'est pas comptée ici et peut dépasser le plafond.
**Perte possible, sans plafond propre** : tout ce qui a été dépensé jusqu'à la perte, borné par l'arrêt dur (61,2 USD).
- Au prix exigé, une perte à la fin de B1 coûte ≈ 39 USD, B0 compris.
- Avec les lieux (a) et (c), les lentilles finies n'existent que sur la machine jusqu'à la copie de B6 : une perte après B1 coûte jusqu'à
  ≈ 55 USD sans aucune lentille.
- **Seul le lieu (b) protège en cours de route** : il reçoit une sauvegarde sur trois pendant B1, puis les lentilles finies dès la fin de
  B1, avant B2. Une perte ne coûte alors que le travail fait depuis la dernière copie, mais les lentilles déjà copiées ne permettent pas
  de finir B-β sans un devis neuf.
- Le lieu (c) ne protège qu'à la fin de la course.

| poste | attendu | pire cas | plan v2 |
|---|---|---|---|
| carte (H100 SXM ≈ 2,15 USD/h, stockage compris ; offre du 00:22Z, non revue au filtre complet) | **≈ 19 à 29 USD** | 25,1 h × 2,25 (prix exigé) = **56,5 USD** | 21 à 27 ; 63,6 |
| trafic : entrant ≈ 25 Go (poids ≈ 16 Go ; lentilles de Neuronpedia ≈ 3,1 Go, soit 1,04 Go par fichier au plan v2 ; environnement et corpus, compte large, en partie double avec le reste : m-C) ; sortant ≈ 17 Go de lentilles, plus ≈ 43 Go de copies de sauvegarde avec le lieu (b) | 0 à 3,4 USD | **3,4 USD** (≈ 85 Go à 0,04 au plus, plafond de trafic exigé) | — |
| disque 200 Go (+ ≈ 8 Gio transitoires pendant une sauvegarde) | compris au prix lu | — | 4 avec le réseau |
| appels de modèles | 0 | 0 | 0 |
| **total** | **≈ 19 à 32 USD** | **≈ 59,9 USD** | 21 à 27 ; 68 |

**Écart au plan v2 (M6)** : attendu presque égal ; le pire cas prend 3,9 h de plus. Ces heures viennent de B0 à 3 h faute d'essai local
(M4), de la passe refaite (M5), des copies et des sauvegardes. La machine perdue sort du pire cas et devient un arrêt. Le prix exigé, 2,25
au lieu de 3,00, compense en dollars.
**Plafond demandé : 68 USD** (plan v2, § 3.4). Arrêt dur à 90 % = 61,2 USD. Le pire cas, ≈ 59,9 USD trafic compris, **tient dessous**
sans troncature, au prix exigé de **2,25 USD/h** et au trafic sortant exigé de ≤ 0,04 USD/Go (25,1 × 2,25 + 3,4 = 59,9). La marge de
1,3 USD couvre le flou des sauvegardes non mesurées (v4, majeure 2 et m-A ; la v3 tenait à 0,14 USD près, à trafic presque nul). L'offre
de 00:22Z (≈ 2,145) tiendrait sous ce prix, mais son débit montant n'est pas connu (§ 3).

## 5. Gardes (M2 : reprises du devis B-α v2, § 3, et adaptées)
| garde | valeur |
|---|---|
| ligne de GO | ligne de calcul neuve, nommée par la mère sur un mot de Lazar ; échéance proposée **2026-11-30** (volet B, plan v2) ; feu écrit avant toute création |
| compte rendu à la mère | **40,8 USD** (60 %), par la garde de dépense v4 ; elle décide de la suite |
| arrêt dur | **61,2 USD** (90 %) : destruction par identifiant, réessayée et vérifiée par l'absence |
| minuterie v4 | durée = 90 % du plafond au prix lu : à 2,25, 97 920 s (27,2 h) ; à 2,15, 102 474 s ; bornes 600 à 129 600 s : un prix lu sous 1,70 USD/h serait **refusé** par la minuterie (m-5) ; rien ne part alors, message à la mère |
| bornes en durée | compte rendu à **13,4 h** (haut de l'attendu) ; rappel à **25,1 h** (pire cas, avant la minuterie de 27,2 h au prix exigé) ; rappel indépendant à 80 % de la minuterie ; échéance de chaque étape écrite dans l'état poussé, dépassement = compte rendu |
| crédit | `can_pay` vrai, `has_billing` vrai, `billing_failed` faux avant la création (champ absent = arrêt) ; crédit < 1 USD en cours de course → arrêt (R-2788, R-2795) ; **le crédit doit couvrir le plafond ou le rechargement automatique être actif** (le crédit relevé en B-α était de l'ordre de 5 à 6 USD) |
| course figée | `gpu_util` ≈ 0 **et** `cpu_util` < 10 % à deux contrôles de suite sans nouvelle poussée → arrêt (R-2800) |
| copie des lentilles | (b) dès la fin de B1, (c) après B5, avant la poussée finale ; empreintes vérifiées au lieu d'arrivée **avant** toute destruction prévue ; s'il reste moins d'une heure avant la minuterie ou l'arrêt dur, la mère décide ; **sans réponse en 15 minutes, la copie continue** jusqu'à la minuterie ou l'arrêt dur, qui restent les filets (v4, m-F) |
| perte de machine | détection et arrêt au § 4 ; aucune reprise sans devis neuf et mot de Lazar |
| une seule instance | branche de résultats neuve exigée absente avant la création ; journaux de la minuterie et de la garde commités ; arrêts par PID vérifiés par leurs arguments ; veille et réarmement sur l'échéance absolue après tout redémarrage du conteneur de la session |
| destruction | `vastai destroy instance <ID> -y < /dev/null` ; absence prouvée par `suivi_vast_v6 absente <ID> --non-vide`, jamais sur le code de sortie ; préavis d'une ligne à la mère avant la création et la destruction (R-2883) |
| intouchables | 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, la machine 60988826, `poste-temoin-bailey-*`, toute instance d'une autre session |
| refus | tout refus d'une permission, du crochet ou du classifieur : ni rejoué, ni reformulé, ni contourné ; arrêt et nœud à la mère (R-2864) |

## 6. Leçons de B-α portées
Entrée idempotente et reprise ; `pip` minuté ; clé `HF_TOKEN` aux seuls téléchargements de Llama, retirée ensuite (révocation
recommandée : la clé aura été passée à quatre ou cinq machines) ; balayage des secrets avant chaque poussée ; essai à blanc de
l'environnement exact des essais (variables, chemins, empreintes) et des appels de `measure` ; estimation de la mémoire de pointe de
chaque partie avant la course (pour B1 : pic publié de 20 à 29 Go à lot de 128 sur Qwen3-8B ; Llama a des couches à portes plus larges,
non mesuré ; 80 Go laissent une marge large ; pour `measure` au lot 64 : **au moins** ≈ 23,5 GiB, v4, m-G) ; carte contrôlée par l'amorce (`CARTE_ATTENDUE`) ; aucun résultat lu par la fille
(lecteur neuf, plan scellé).

## 7. Décision demandée (à Lazar, par la mère)
**Décision** : ouvrir ou non une ligne de calcul pour B-β, et choisir le lieu des lentilles. **Enjeu** : refaire leur chaîne complète sur
Llama (nos lentilles R et S), seule façon de trancher B-1, B-5, B-6 et B-2/B-3/B-7 avec la lentille R ajustée par leur code. Options :
(a) **plafond 68 USD, H100 SXM seule, prix lu ≤ 2,25 USD/h, débit montant ≥ 200 Mbit/s, trafic sortant ≤ 0,04 USD/Go**, aucun
repli :
- avantages : attendu ≈ 19 à 32 USD ; pire cas entier sous l'arrêt dur ;
- inconvénients : aucune offre au filtre complet n'est établie (aucune H100 SXM à 01:23Z) et la course peut attendre une offre ; une perte
  de machine coûte tout ce qui a été dépensé jusque-là (≈ 39 USD à la fin de B1, ≈ 55 USD après) sauf avec le lieu (b) ;
(b) variante économe (S seulement, plan v2 § 0 point 3) — à recalculer avant toute décision (la v1 citait le pire cas de la v2, ≈ 48 USD,
comme un plafond : m5) ; inconvénient : ce n'est plus la reproduction ;
(c) ne pas faire B-β (B-α « partiel » suffit pour la question « utile à un moniteur »).
Lieu des lentilles : (a) aucun, (b) stockage d'objets privé, (c) machine de Lazar (§ 2, point 6).
**Recommandation : (a), avec le lieu (b)** (seul à protéger en cours de route) ; s'il faut un compte nouveau pour (b), c'est le nœud de
Lazar. À défaut, (c), en acceptant la perte entière en cas de machine perdue. Confiance 0,45. Le lieu est une condition de la commande.
Pas de défaut sous 48 heures : c'est une dépense.

## 8. Reprise de la contre-lecture de la v1
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

## 9. Reprise de la contre-lecture de la v2
| point | reprise |
|---|---|
| majeure 1 taille des lentilles | acceptée : ≈ 8 Gio par lentille, ≈ 16 Gio les deux, formule et contrôle sur Qwen3-8B (§ 2, point 6) |
| majeure 2 point de sauvegarde et perte de machine | acceptée : perte de machine = arrêt et nœud, sortie du pire cas ; sauvegardes comptées ; copie au lieu (b) (§ 4, § 5) |
| majeure 3 sortie des lentilles | acceptée : `inet_up>=200`, copie comptée à B6, règle si la minuterie approche (§ 3, § 4, § 5) |
| m-1 A100 de 80 Go | acceptée (§ 3) |
| m-2 lignes citées | acceptée (§ 1) |
| m-3 1,5 à 2,3 h | acceptée (§ 1) |
| m-4 lot 64 sur 80 Go | acceptée : condition retirée, pic sourcé (§ 1) |
| m-5 « refusée » | acceptée (§ 5) |
| m-6 rappel après la minuterie | acceptée : rappel à 24,9 h, minuterie à 25,7 h au prix exigé (§ 5) |
| m-7 recompilations | acceptée : documents d'au moins 128 jetons, mesuré au banc de B0 (§ 4) |
| m-8 options équivalentes | acceptée : une seule option, prix exigé 2,38 (§ 4, § 7) |
| m-9 coefficient de Llama | sans objet |
| trafic, `-causal.pt` non sourcés | acceptée : 3,1 Go (plan v2), ≈ 5 Go au journal B-α v1, ≈ 2,6 Go (§ 1, § 4) |

## 10. Reprise de la troisième contre-lecture (de la v3)
| point | reprise |
|---|---|
| majeure 1 filtre non rejoué | acceptée : relevé neuf `releve-prix-vast-h100-20261117T012309Z-v1.tsv` (aucune H100 SXM) ; disponibilité dite non établie (§ 3, § 7) |
| majeure 2 trafic des copies | acceptée : trafic sortant exigé ≤ 0,04 USD/Go, copies d'une sauvegarde sur trois comptées, prix exigé 2,25 (§ 3, § 4) |
| majeure 3 perte de machine | acceptée : détection, perte jusqu'à la dépense entière, (b) seul protecteur, reprise = devis neuf (§ 4, § 5, § 7) |
| m-A sauvegardes | acceptée : 14 au pire, + 0,5 h, à mesurer (§ 4) |
| m-B prix exigé | acceptée : 2,25 avec m-A et la majeure 2 |
| m-C trafic | acceptée : compte large, double compte dit |
| m-D contrôle sur Qwen3-8B, Gio et Go | acceptée (§ 2, point 6) |
| m-E débit du pire cas, copie pour (a) | acceptée (§ 4) |
| m-F règle de la dernière heure | acceptée : défaut à 15 minutes, empreintes avant destruction (§ 5) |
| m-G pic « au moins » | acceptée (§ 6) |
| m-H recompilations | acceptée : évitées par le tirage, pas par le banc (§ 4) |
| m-I mise en forme | acceptée |
