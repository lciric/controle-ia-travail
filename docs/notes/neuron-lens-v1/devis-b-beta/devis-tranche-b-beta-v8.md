# Devis de la tranche de l'ajustement de nos lentilles (B-β) de la lecture par lentille neuronale (« Neuron Lens » ; Llama 3.1 8B Instruct, nos lentilles R et S) — v8

Écrit par la fille « Neuron Lens » le 2026-11-17 : v1 vers 00:25 UTC, v2 vers 00:45, v3 vers 01:05, v4 vers 01:25, v5 vers 01:35,
v6 vers 02:00 (session `session_016QhUrtahFZo57fZUcRReVA`) ; **v7 le 2026-11-18 entre 01:42 et 01:44 UTC** (`date -u`) par la session
neuve de la fille (`session_01XJ6MgnoxfSYHdF6rpEqZ7w`), avec l'accord de la mère (`session_01XJ6Mgr8BN6UanALsQatc5E`, reprise de la
fille inscrite par elle sous R-3105), pour finir la demande (c) de GO-2026-11-17-03 ; **v8 le 2026-11-18 vers 02:06 UTC** (`date -u`),
même session, même accord.

**v8** = v7 (`devis-tranche-b-beta-v7.md`, `d757a4ed…`, archivée), corrigée selon la contre-lecture de la v7 par un contre-lecteur
neuf (`contre-lecture-devis-tranche-b-beta-v7.md`, `caf59025…` : « à corriger », 0 bloquante, 4 majeures, 15 mineures ; table de
reprise au § 12), selon la consigne de la mère du 2026-11-18 (nœud écrit en toutes lettres et options présentées à Lazar ; relevé daté,
avec sa durée de validité ; provenance des valeurs tirées du code voisin), et sur un **relevé neuf du 2026-11-18T01:57:42Z**
(`releve-prix-vast-h100-20261118T015742Z-v2.tsv`, `b33f853d…`, script v2 `releve_prix_h100_v2.py`, `fb3d8bc6…`) : dix-huit minutes
après celui de la v7, **une offre passe les exigences** (Lettonie, ≈ 2,32 USD/h stockage compris) et une seconde (Japon, ≈ 2,04) n'est
écartée que par la borne de la minuterie. La disponibilité au prix exigé est donc **intermittente** (§ 3) ; le § 7 en fait un nœud à
options. Changements de fond : trois décisions séparées (ligne et plafond, lieu des lentilles, clé d'accès au modèle) et quatre options
chiffrées pour la première (§ 7) ; règle d'arrêt après le banc du montage (§ 5) ; second secret ou accès exigé par les lieux L2 et L3
(§ 2, point 6), d'où la recommandation du lieu L1 ; crédit exigé sans alternative (§ 2, point 8 ; § 5) ; minuterie armée à sa borne haute
sous le prix minimal, au lieu d'un refus (§ 5) ; colonne « existe ou à écrire » des gardes (§ 5) ; provenance des valeurs du code voisin
(§ 1). Les chiffres neufs des §§ 3, 4, 5 et 7 ne sont contre-lus que par la contre-lecture de la v8 (§ 13).

**v7** = v6 (`devis-tranche-b-beta-v6.md`, `debfdf42…`, archivée sur `prep/neuron-lens-v1` au commit `45a81e08`), mise à jour **sans
dépense ni location**. Les retouches de la v5 et de la v6 n'avaient pas été contre-lues : la v7 est contre-lue **en entier** par un
sous-agent neuf (R2, § 12). Changements :
1. **relevé de prix neuf** du 2026-11-18T01:39:39Z (`releve-prix-vast-h100-20261118T013939Z-v1.tsv`, `15a79b58…`, écrit par
   `releve_prix_h100_v1.py`, `d789176e…`, lecture seule) : **aucune H100 SXM ne passe les exigences** ; les deux offres du filtre
   complet, en Tchéquie, sont à ≈ 4,23 USD/h stockage compris (§ 3) ;
2. **faits de la recourse** de la lecture contre ablation couche par couche sur A100 (R-3083) et de **l'essai d'invariance au lot**
   (R-3093) : `measure` au lot 64 tient sur 40 Go ; lots 16 et 64 identiques au bit près sur une A100 de 40 Go ; durées mesurées sur A100
   (§ 1, § 2, § 4, § 6) ;
3. **crédit du loueur** nul et mot de Lazar relayé par la mère, « plus de credits vast avant 9h du matin » (§ 2, point 8 ; § 5) ;
4. **clé d'accès au modèle** (`HF_TOKEN`) : passage à une machine neuve suspendu au mot de Lazar (§ 2, point 7) ;
5. **lieu de rangement des lentilles** écrit comme un choix de Lazar qui conditionne la commande (§ 2, point 6 ; § 7) ;
6. intouchables du relevé du 2026-11-18T01:23Z (§ 5) ; noms en clair au titre, aux en-têtes et aux premières mentions (R-3044,
   étendue R-3085), les sigles restant en appui.

**v6** = v5 (`devis-tranche-b-beta-v5.md`, `ae1975fb…`, archivée), sur un mot de Lazar dans la session de la fille, le 2026-11-17 vers
01:56 UTC : « prix exigé de 2,25 USD/h. ! monte me pkafond » (lu : « monte le plafond »). Aucune H100 SXM ne passait le filtre complet à 2,25 aux relevés de 01:23Z et
01:27Z. Le **prix exigé remonte à 3,00 USD/h**, le prix plafond du plan v1, et le **plafond monte à 88 USD**, le plus petit montant entier
dont l'arrêt dur à 90 % couvre le pire cas à ce prix. L'offre du Montana relevée à 01:27Z (≈ 2,62 USD/h stockage compris, débit montant
1 571 Mbit/s, trafic 0,039 et 0,020 USD/Go, fiabilité 0,995) passerait le filtre complet. Seuls les chiffres qui en dépendent changent ;
les retouches de la v6 ne sont pas contre-lues.

**v5** = v4 (`devis-tranche-b-beta-v4.md`, `1b015d16…`, archivée), corrigée selon la quatrième contre-lecture
(`contre-lecture-devis-tranche-b-beta-v4.md` : « à corriger, légèrement », aucune bloquante, 1 majeure, 10 mineures ; table de reprise
au § 11). Les lieux des lentilles s'appellent désormais **L1, L2, L3** (m-9). Relevé neuf, avec requête témoin :
`releve-prix-vast-h100-20261117T012712Z-v1.tsv`.

**v4** = v3 (`devis-tranche-b-beta-v3.md`, `77719c0c…`, archivée), corrigée selon la troisième contre-lecture
(`contre-lecture-devis-tranche-b-beta-v3.md` : « à corriger », aucune bloquante, 3 majeures, 9 mineures). La table de reprise est au § 10,
et un relevé neuf `releve-prix-vast-h100-20261117T012309Z-v1.tsv` est joint.

**v3** = v2 (`devis-tranche-b-beta-v2.md`, `abc7b727…`, archivée) corrigée selon sa contre-lecture par un second lecteur neuf
(`contre-lecture-devis-tranche-b-beta-v2.md` : « à corriger », aucune bloquante, 3 majeures, 9 mineures ; table de reprise au § 9) ;
chiffres de taille relus dans le code voisin (`02_fit.py` l. 1-10 ; `neuron_lens/transport.py` l. 45-58).

**v2** = v1 (`devis-tranche-b-beta-v1.md`, `b98e53f1…`, archivée) corrigée selon la contre-lecture d'un lecteur neuf
(`contre-lecture-devis-tranche-b-beta-v1.md`, verdict « à corriger » : 1 bloquante, 6 majeures, 9 mineures ; table de reprise au § 8).
Demande (c) de GO-2026-11-17-03 (R-3046, mot de Lazar « b puis c ») : devis contre-lu, **sans aucune dépense**, soumis à Lazar par la mère ;
aucune dépense de B-β sans ligne de calcul neuve. Sources : plan et
devis v1 (§ 4, § 5.3, § 5.4, § 7) et v2 (§ 0, § 3.2 à 3.4) ; texte gelé v6 (`34b88243…`, § B.4) ; devis de la tranche des lentilles publiques (B-α) v2 (`61c394f5…`, § 3) ; les
trois courses de B-α (journaux `journal-course-b-alpha-v1.md` à `-v3.md`) ; banc publié `fit_bench_h100_2026-10-28.log` ; relevé du jour
`releve-prix-vast-20261117T002223Z-v1.tsv` (`1a7cc32c…`) ; relevés H100 de 01:23Z (`8814fec4…`) et de 01:27Z (sur `prep/neuron-lens-v1`) ;
v7 : relevé H100 du 2026-11-18T01:39:39Z (`15a79b58…`, ci-joint) ; résultats de la recourse sur A100
(`diag/20261117-015632-neuron-lens-b-alpha/`, journal `journal-course-b-alpha-v5.md`, `3047ff1c…`) ; verdicts de la recourse
(`lecture-recourse-b7/verdict-recourse-b7-v1.md`, `996744b2…`) et de l'essai d'invariance au lot
(`audit-invariance-lot/verdict-audit-invariance-v1.md`, `4c175cc8…`), tous sur `prep/neuron-lens-v1` au commit `45a81e08`.
v8 : relevé de 01:27Z le 17 : `c1731c11…` ; relevé du 2026-11-18T01:57:42Z (`b33f853d…`, ci-joint) ; contre-lecture de la v7
(`caf59025…`, ci-jointe) ; code voisin relu le 2026-11-18 dans une copie de lecture au commit
`849bfe1678e28becceb1e3864afe5fc8297d02e4` (§ 1).

**Conventions (v8, m-12 et m-13).** Renvois entre parenthèses aux points des contre-lectures : B1, M1 à M6 et m1 à m9, sans tiret, pour
celle de la v1 (§ 8) ; « majeure 1 à 3 » et m-1 à m-9 pour celle de la v2 (§ 9) ; m-A à m-I pour celle de la v3 (§ 10) ; m-1 à m-10 pour
celle de la v4 (§ 11) ; M-1 à M-4 et m-1 à m-15 pour celle de la v7 (§ 12) ; « v4, m-A » se lit « correction portée en v4 pour le point
m-A ». Unités : Gio = 2^30 octets ; Mio = 2^20 octets ; Go = 10^9 octets. Étapes de la course : B0 montage, B1 ajustement des lentilles,
B2 corpus et passe complète, B3 pilotes et lectures, B4 mesure et notation, B5 lectures aux activations, B6 scellement, copie et
destruction. Mesures : stabilité de nos lentilles (B-1), lecture contre pilotage (B-2), avance sur la lentille des logits (B-3), écart
aux lentilles J et J++ (B-4), lecture côté entrée par la lentille S (B-5), notre lentille R contre celle de Neuronpedia (B-6), lecture
contre ablation couche par couche (B-7).

## 1. Ce que fait la tranche de l'ajustement de nos lentilles (B-β) (texte gelé v6, § B.4 ; plan v1, § 4.1 et 4.2 ; plan v2, § 3.2)
La stabilité de nos lentilles R et S entre les moitiés paires et impaires du corpus (B-1), la lecture côté entrée par la lentille S
(`read_S`, B-5), notre lentille R contre celle de Neuronpedia (B-6), et, **avec notre lentille R**, la lecture contre pilotage (B-2),
son avance sur la lentille des logits dans la première moitié du réseau (B-3), l'écart aux lentilles J et J++ (B-4, rapporté) et la
lecture contre ablation couche par couche (B-7). Étapes : B0 (montage, essais des correctifs et de l'estimateur, **essai d'un Llama
miniature contre la force brute** — garde renvoyée de B-α à B-β —, banc d'un document par lentille) ; B1 (ajuster R et S sur 1 000
documents de DCLM, 128 jetons ; **les deux moitiés en un seul passage** : `02_fit.py` envoie le document i à la moitié i mod 2 et tient
deux accumulateurs : `02_fit.py` l. 4-5 et la boucle unique l. 168-177, `neuron_lens/transport.py` l. 49-57 ; reprise sur point de sauvegarde) ; B2 (corpus d'activations, comptes, passe
complète) ; B3 (pilotes `07`, lectures `08`) ; B4 (`measure`, `score` avec notre R) ; B5 (`reads_at_firings.py`) ; B6 (manifeste,
scellement, destruction).

**Ce qui est refait, et pourquoi (M5).** Le plan v2 (§ 3.2) prévoyait de recopier les tables de B-α (« sans nouvelle passe du modèle »).
Elles n'existent plus : les tables de la passe, les activations et le fichier `-causal.pt` de `measure` dépassent la limite de fichier de
l'hébergeur de code, sont restés sur les machines et ont été détruits avec elles (commande B-α v5, M6). B-β refait donc le corpus, la
passe complète et `measure` (≈ 1,5 à 2,3 h). `measure` n'emploie aucune lentille : la refaire ne change pas l'objet, seulement le lot.
Elle se fait au **lot publié 64** : pic estimé **au moins** ≈ 23,5 Gio (`devis-b-alpha/memoire-ablation-lot64-rtx4090-v1.md`, § 2), contre 80 Go de
carte. v7 : la recourse de l'ablation sur une A100 de 40 Go l'a fait passer **en mémoire** au lot 64
(`diag/20261117-015632-neuron-lens-b-alpha/b-alpha-measure-lot64.json`, `a61dbbd1…`, 1 073,7 s) : le pic y est donc sous la mémoire de
cette carte (≈ 39 Gio), pic exact non relevé. L'essai d'invariance au lot (R-3093) a montré que, sur une A100 et ces versions, l'ablation
rend le même résultat au bit près aux lots 16 et 64, mais pas aux lots 1 et 7 ; sur H100, l'effet du lot n'est pas mesuré ; le lot publié
64 reste le choix. Si le lieu des lentilles (§ 2, point 6) peut aussi recevoir
`-causal.pt` (≈ 2 Gio pour Llama, `devis-b-alpha/memoire-measure-b-alpha-v1.md` § 3), `measure` ne serait plus à refaire dans une tranche suivante.
**Provenance des valeurs du code voisin (v8, consigne de la mère)** : les lignes et valeurs de `02_fit.py` et de
`neuron_lens/transport.py` citées ici et aux §§ 2, 4, 6 et 7 ont été relues le 2026-11-18 par la fille dans une copie de lecture du
dépôt voisin au commit `849bfe1678e28becceb1e3864afe5fc8297d02e4`, jamais exécutée : `02_fit.py` l. 4-5 (document i à la moitié
i mod 2 ; sauvegarde toutes les `--save-minutes`), l. 9-10 (9,5 et 9,7 Go pour Qwen3-8B, deux cibles par lentille), l. 161-166 (`save()`
n'écrit qu'un fichier local), l. 168-177 (boucle unique, `lens_doc(…, i % 2, …)`), l. 193 (`--lens`, une lentille par course), l. 213
(`--save-minutes`, défaut 10) ; `transport.py` l. 46 (`DIM_BATCH = 256`), l. 49-57 (`Accumulator`, sommes `[couches, d, d]` par cible et
par moitié), l. 256-258 (`target_layers` : la cible `out` de R s'arrête une couche avant la dernière) ; journal du banc
`data/summary/fit_bench_h100_2026-10-28.log` (`56ffe58d…`, l. 1, 31, 37-42, 68-69, 76-78). Pour Llama (32 couches, d = 4 096), la même
formule donne 63 emplacements pour R et 64 pour S, soit ≈ 7,9 et 8,0 Gio : les « ≈ 8 Gio par lentille » du § 2, point 6.

## 2. Préalables, tous sans dépense (rien ne part sans eux)
1. **Condition de passage de B-α à B-β (M3)** : plan v2, § 3.2 ; texte gelé v6, « Seuil » B et « Critères », reproduction. B-α est faite
   (trois courses, R-2915 : verdict « partiel », **aucune chaîne en défaut**, lu par un lecteur neuf) : la condition est **remplie**. Le
   compte rendu à la mère est fait. La recourse de la lecture contre ablation couche par couche (B-7, GO-2026-11-17-04) ne conditionnait
   la tranche que si elle trouvait une chaîne en défaut : elle n'en a trouvé **aucune** (R-3083 ; `lecture-recourse-b7/verdict-recourse-b7-v1.md`,
   `996744b2…`) ; la condition reste **remplie** (v7).
2. **Texte gelé de la tranche** (préenregistrement, R1), écrit, contre-lu par un sous-agent neuf, scellé : critères B-1 à B-7 avec notre R, B-5 **réécrit** (le
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
   formule redonne les 9,5 et 9,7 Go écrits (`02_fit.py` l. 9-10). C'est au-delà de la limite de l'hébergeur de code : **100 Mo par fichier** selon sa documentation, non revérifiée
   ici ; nos amorces s'arrêtent à 95 Mo, par marge. **Aucun lieu n'est arrêté** ; options pour Lazar :
   **L1** aucun lieu : on ne verse que les empreintes et les mesures dérivées ; les lentilles **et le point de sauvegarde** sont perdus à la
   destruction (coût nul ; aucun secret de plus sur la machine ; la tranche n'est pas rejouable sans refaire l'ajustement, ≈ 16 à 26 USD
   au prix exigé, montage en sus : v8, m-14) ;
   **L2** un stockage d'objets privé du programme, s'il en existe un (compte ou dépôt nouveau sinon : nœud de Lazar ; de l'ordre de 0,2 à
   0,5 USD par mois pour 8 à 17 Go aux prix courants, non relevés ici) ; il permet aussi d'y copier le point de sauvegarde pendant
   l'ajustement (§ 4, perte de machine). **Il exige une clé d'écriture de ce stockage sur la machine louée pendant tout l'ajustement (6 à
   14 h), et non pour un seul geste** : droits restreints (écriture seule, un seul préfixe, révocable), passage au mot de Lazar au même
   titre que la clé d'accès au modèle (point 7). Et du **code à écrire** : `02_fit.py` n'écrit qu'un fichier local (l. 161-166, `save()`),
   si bien que la copie d'une sauvegarde sur trois, la vérification de son empreinte à l'arrivée et la règle des 15 minutes (§ 5) sont à
   écrire et à essayer (R5) (v8, M-3) ;
   **L3** une machine de Lazar (≈ 17 Go : ≈ 45 min à 50 Mbit/s ; délai et débit à voir avec lui). **Deux façons, chacune avec son
   préalable** : la machine louée pousse vers la machine de Lazar (un accès ou un secret de la machine de Lazar sur la machine louée, au
   mot de Lazar) ; ou Lazar tire depuis la machine louée (un accès entrant à la machine louée, sans secret sur elle ; la machine se
   facture pendant la copie et Lazar doit être là) (v8, M-3).
   **Le lieu de rangement des lentilles (L1 aucun, L2 stockage d'objets privé, L3 machine de Lazar) est un choix de Lazar ; il conditionne
   la commande** : la commande de la tranche ne s'écrit pas, et rien ne s'engage, sans ce choix (v7 ; consigne de la mère du 2026-11-18).
7. **Clé d'accès au modèle (`HF_TOKEN`)** (v7) : le téléchargement de Llama 3.1 8B Instruct (accès contrôlé) exige une clé de la
   plateforme de modèles, passée à la machine louée pour ce seul geste puis retirée (forme de GO-2026-11-15-04, dont la levée était bornée à
   l'autonomie du 2026-11-15, jusqu'à 22:39Z : elle est échue, aucune autorisation n'est en cours ; v8, m-9). La clé actuelle a été passée à
   **six** machines louées (R-3068 ; sixième passage à l'essai d'invariance au lot, R-3086 et R-3093 ; le journal de la recourse dit
   « cinquième », juste à sa date) ; sa révocation est recommandée à Lazar (acte du titulaire, ni de la fille ni de la
   mère). Consigne de la mère du 2026-11-18 : ne la passer à **aucune machine neuve** tant que Lazar n'a pas répondu. Le passage d'une
   clé, ancienne ou neuve, à la machine de la tranche est donc un **préalable, au mot de Lazar**.
8. **Crédit du loueur** (v7) : nul au relevé de la mère du 2026-11-18 vers 01:19Z (solde −2,19 USD) ; mot de Lazar relayé par la mère,
   non vérifié ici sur sa source : « plus de credits vast avant 9h du matin ». Rien ne part avant une recharge qui porte le crédit **au moins au
   plafond de la tranche, en plus** des autres lignes ouvertes sur le même compte du loueur, constaté avant la création. Le rechargement
   automatique n'est plus une alternative : il était actif le 17 novembre (journal de la recourse) et n'a pas empêché le solde négatif du
   18 (cause non établie ici) (§ 5, crédit ; v8, m-8).

## 3. La machine
**Carte exigée : H100 SXM 80 Go** (le journal du banc publié dit « one H100 80GB HBM3 (vast.ai) », l. 1 : tenue pour la SXM, inférence
dite ; v8, m-13), **machine vérifiée** (défaut de l'outil, comme pour la tranche des lentilles publiques), **prix lu sur l'instance au plus
le prix exigé, stockage compris**, **débit montant ≥ 200 Mbit/s** (`inet_up>=200`, pour la copie des lentilles), **trafic sortant et
entrant ≤ 0,04 USD/Go chacun** (`inet_up_cost<=0.04 inet_down_cost<=0.04`) ; **aucun repli sur une autre carte** : sans offre au moment
de la commande, rien ne part, message à la mère (nœud : autre carte, mot de Lazar). Motif (contre-lecture de la v1, B1) : le pire cas
est bâti sur le banc d'une H100 ; une A100 serait, selon ce contre-lecteur, deux à trois fois plus lente (estimation non mesurée) et son
pire cas dépasserait l'arrêt dur. Aucune H200 (exclue sans mot de Lazar). Le prix exigé dépend de l'option retenue au § 7 (3,00 USD/h
dans la v6 et l'option (c) ; 4,25 dans les options (a) et (b)).

**Relevés et disponibilité** (lecture seule ; prix avec 200 Go de stockage = `dph_total` + `storage_cost` × 200 / 720 ; filtre
complet : `gpu_name=H100_SXM num_gpus=1 cpu_ram>=64 cpu_cores_effective>=16 disk_space>=200 inet_down>=300 reliability>0.98
cuda_max_good>=13.0 rentable=true`) :

| relevé | offres au filtre complet (prix avec stockage, en USD/h ; débit montant ; trafic sortant et entrant, en USD/Go) | recevables au prix exigé de 3,00 | source |
|---|---|---|---|
| 2026-11-17T00:22:23Z | Japon ≈ 2,145 ; Tchéquie ≈ 4,83 et ≈ 5,03 (débit montant non relevé) | une possible, non vérifiée au débit montant | `releve-prix-vast-20261117T002223Z-v1.tsv`, `1a7cc32c…` |
| 2026-11-17T01:23:09Z | aucune | aucune | `releve-prix-vast-h100-20261117T012309Z-v1.tsv`, `8814fec4…` |
| 2026-11-17T01:27:12Z | Montana ≈ 2,62 (1 571 Mbit/s ; 0,039 et 0,020) | **une** : elle passe les quatre exigences à 3,00 (elle était au-dessus du prix exigé de 2,25 de la v5) | `releve-prix-vast-h100-20261117T012712Z-v1.tsv`, `c1731c11…` |
| 2026-11-18T01:39:39Z | Tchéquie ≈ 4,23 et ≈ 4,23 (7 127 et 8 358 Mbit/s ; ≤ 0,0391) | aucune | `releve-prix-vast-h100-20261118T013939Z-v1.tsv`, `15a79b58…` |
| 2026-11-18T01:57:42Z | Lettonie ≈ 2,32 (420 Mbit/s ; 0,0039 et 0,0026) ; Japon ≈ 2,04 (1 038 Mbit/s ; 0 et 0) ; Tchéquie ≈ 4,10 et ≈ 4,11 | **une** au relevé (Lettonie) ; **deux** avec la règle de la borne haute de la minuterie (§ 5) : le Japon n'est écarté que par le prix minimal de 2,11 | `releve-prix-vast-h100-20261118T015742Z-v2.tsv`, `b33f853d…` |

**Bilan (v8, M-1)** : sur les quatre relevés du filtre complet qui portent le débit montant (01:23Z et 01:27Z le 17 ; 01:39Z et 01:57Z le
18), une offre recevable à 3,00 à deux d'entre eux (deux au dernier avec la règle de la borne haute), aucune aux deux autres. La
disponibilité au prix exigé est **intermittente** : elle a changé en quatre minutes le 17 et en dix-huit minutes le 18. Ce n'est pas un
dépassement durable du plafond, c'est un **risque de disponibilité au moment de la commande**. Aux offres de Tchéquie (≈ 4,10 à 4,23),
le pire cas serait ≈ 106 à 110 USD, au-delà du plafond de 88 USD : à ces prix, rien ne part sans l'option (a) ou (b) du § 7.
**Validité d'un relevé (v8)** : un relevé vaut à son heure ; il ne fonde aucune décision de prix au-delà de l'heure qui suit. Celui de
01:57:42Z aura vieilli à la décision de Lazar : il est à refaire avant elle (lecture seule, `releve_prix_h100_v2.py`), puis la commande
relève dans les minutes qui précèdent la création.
**Hors du filtre par défaut « machine vérifiée »** (`verified=any`, pour information) : une offre non vérifiée au Japon (≈ 1,97 à
01:39Z, débit montant 97 Mbit/s ; ≈ 1,84 à 01:57Z, 88 Mbit/s) : **non retenue** (machines vérifiées seulement ; débit sous les 200
exigés).
**Notes de méthode (v8, m-10)** : l'outil compte déjà 5 Gio de stockage dans `dph_total`, que la formule recompte (moins de 0,005 USD/h).
La recherche ne rend pas toujours les mêmes offres d'une requête à l'autre, même plus large : les machines 140932, 148671 et 149805 de
l'hôte 214845 apparaissent tour à tour, et le relevé de 01:57:42Z rend deux offres de ce même hôte dans une même requête. L'explication
de la v7 (« une offre par hôte ») est donc **fausse** ; la cause n'est pas établie ; le témoin n'est pas un sur-ensemble du filtre. Le
script v2 (`releve_prix_h100_v2.py`, `fb3d8bc6…`) teste la vérification de la machine et le prix minimal de la minuterie, écrit l'hôte, et
donne une colonne d'épreuve par option du § 7 (ses dix essais : un cas sain, six artefacts, des bornes ; tous passés).
**Autres cartes (relevé du 2026-11-17T00:22:23Z, pour mémoire)** : H100 PCIe 80 Go (≈ 2,415, Afrique du Sud, trafic 0,040) : retirée,
moins de calcul que la SXM (de l'ordre d'un quart), vitesse non mesurée ; H100 NVL 94 Go (3,415 à 3,665 ; trafic 0 à 0,0365) :
au-delà du prix exigé de 3,00 ; A100 de 80 Go (six SXM4 de 1,104 à 1,973, une PCIe à 1,461) et de 40 Go (sept, de 0,375 à 0,684) :
retirées (contre-lecture de la v1, B1) ; au plafond de 88 USD, la borne haute de la minuterie v4 aurait refusé **les sept** A100 de 80 Go
et toutes celles de 40 Go (prix minimal 2,11 ; v8, m-1) ; RTX 6000 Ada 48 Go (0,561 à 0,869 ; trafic 0,0026 à 0,0143) : non retenue,
vitesse non mesurée.

## 4. Durées et coût
Durées : **mesurées** sur B-α (RTX 4090) quand elles existent ; **publiées** (Qwen3-8B, H100) sinon ; Llama : 0,9 à 1,2 fois Qwen3-8B,
**hypothèse non mesurée** (32 couches contre 36, couches à portes plus larges), levée par le banc de B0.

**B1 (M1, recalculé)** : banc publié 11,2 à 11,8 s par document (H100 80GB HBM3 du journal du banc, tenue pour la SXM ; Qwen3-8B ; documents
d'exactement 128 jetons ; `torch.compile(dynamic=False)` ; lot de dimensions `--dim-batch` de 128 à 512, l. 37-42 du journal ; la course
garde le défaut du code, 256, `transport.py` l. 46 ; v8, m-13) ; deux lentilles × 1 000 documents = 2 000 passages (les moitiés ne coûtent pas de second passage, § 1)
→ **6,2 à 6,6 h** au banc ; × 0,9 à 1,2 → **5,6 à 7,9 h attendues**. Pire cas : deux fois la borne haute du banc (23,6 s par document)
× 2 000 = **13,1 h**. **Sauvegardes** (absentes du banc) : `--save-minutes 60` (au lieu de 10). Au pire, 13,1 h d'ajustement font ≈ 14
sauvegardes de ≈ 8 Gio, à 1 à 2 min chacune sur le disque local (**non mesuré** ; à mesurer à la première sauvegarde) : + 0,5 h au pire
(v4, m-A ; la v3 comptait 0,3 h) ; + 0,1 à 0,3 h attendus. Avec le lieu L2, une sauvegarde sur trois est copiée vers lui (≈ 5 copies de
≈ 8,6 Go au pire, ≈ 6 min chacune à 200 Mbit/s : + 0,2 h attendues, + 0,5 h au pire). Documents plus courts que 128 jetons : recompilations
de 15 à 37 s (contre-lecture de la v2, m-7) ; elles sont évitées par le **tirage** de documents d'au moins 128 jetons, coupés à 128 (v4, m-H : le banc d'un seul
document ne les mesure pas).

| étape | attendu | pire cas | plan v2 (§ 3.4) | source |
|---|---|---|---|---|
| B0 montage, environnement, téléchargements, essais des correctifs sur la machine, banc | 0,5 à 1 h | **3 h** (M4) | banc 0,5 h ; montage 2 h au pire | mesuré B-α : environnement 64 à 181 s, poids 72 s à 3 min 30, B0 19 à 41 s ; essais de l'ajustement et banc non mesurés ; A100 (recourse, v7) : poids 348 s, tokeniseur et lentilles publiques 335 s, B0 45 s, fumée 71 s |
| B1 deux lentilles, 1 000 documents chacune, sauvegardes et copies vers L2 comprises | 5,9 à 8,5 h | 14,1 h | 6,2 à 8,9 h ; 13,2 h | ci-dessus |
| B2 corpus, comptes, passe complète | 1,0 à 1,5 h | 2,5 h | recopiées (1,5 h au pire) | mesuré B-α : corpus 2 min 31 à 15 min, passe 61 à 66 min (RTX 4090) ; refaite (§ 1, M5) ; A100 (recourse, v7) : corpus 343 s, passe 3 241 s |
| B3 pilotes et lectures (`07`, `08`) | 0,3 à 0,5 h | 1 h | 1,3 h avec B5 | publié (12 min et 5 à 7 min, H100) |
| B4 `measure` (lot 64) et `score` | 0,5 à 0,8 h | 1,5 h | 0,8 h avec le transfert | mesuré B-α : pilotage 514 s, ablation ≈ 15,5 min au lot 16, `score` ≈ 3 min ; A100 (recourse, v7) : `measure` 1 069 s au lot 16 et 1 074 s au lot 64, pilotage et ablation compris, `score` 76 et 86 s |
| B5, B6 lectures aux activations, scellement, poussées | 0,5 à 0,8 h | 1,5 h | — | publié, et mesuré B-α (poussées) |
| B6 copie des lentilles vers leur lieu (≈ 8 à 17 Go ; lieux L2 et L3 seulement ; rien pour L1) | 0,2 à 0,3 h | 0,5 h | — | ≈ 12 min pour 17 Go à 200 Mbit/s, débit exigé ; pire cas à moitié de ce débit (v4, m-E) |
| audit R4 (seconde graine), s'il est déclenché | — | 1 h | — | B-α |
| **heures** | **8,9 à 13,4 h** | **≈ 25,1 h** | 8,8 à 11,5 h ; 21,2 h | |

Durées de l'A100 (v7 ; liste complétée en v8, m-5 ; résultats de la recourse sous `diag/20261117-015632-neuron-lens-b-alpha/`) :
`b-alpha-telecharger-poids.json` `295fb8a6…` (347,5 s), `b-alpha-telecharger-tokeniseur.json` `ebc9ce90…` (335,0 s, lentilles
publiques comprises), `b-alpha-b0.json` `e79aa88e…` (45,2 s), `b-alpha-fumee.json` `203e68ac…` (70,5 s), `b-alpha-corpus.json`
`699e271f…` (342,6 s), `b-alpha-passe.json` `16654673…` (3 241,3 s), `b-alpha-measure.json` `47327c23…` (1 068,7 s, lot 16),
`b-alpha-measure-lot64.json` `a61dbbd1…` (1 073,7 s, lot 64), `b-alpha-score.json` `56d49070…` (76,0 s), `b-alpha-score-lot64.json`
`93928509…` (85,6 s) : pour mémoire ; elles ne changent aucune borne, la H100 n'étant pas mesurée.

**Perte de la machine**. **Détection** : l'instance n'est plus « running » au suivi, ou l'état poussé, poussé toutes les 10 minutes pendant
toute la course (B1 compris), n'avance plus depuis 30 minutes avec le journal muet, ou la course est figée (§ 5). **Après une perte**,
l'instance est détruite par son identifiant (elle se facture tant qu'elle existe), son absence prouvée, et la garde et la minuterie
restent armées jusqu'à l'absence ; le décompte de la dépense continue jusque-là (contre-lecture de la v4, m-4). **Règle : arrêt.** Rien n'est relancé ; compte rendu à la mère ; nœud de
Lazar. Toute reprise sur une nouvelle machine est un **devis neuf** : elle n'est pas comptée ici et peut dépasser le plafond.
**Perte possible, sans plafond propre** : tout ce qui a été dépensé jusqu'à la perte, borné par l'arrêt dur (79,2 USD, v6).
- Au prix exigé de 3,00 USD/h, une perte à la fin de l'ajustement coûte ≈ 51 USD, montage compris (17,1 h ; ≈ 45 USD à 2,62).
- Avec les lieux L1 et L3, les lentilles finies n'existent que sur la machine jusqu'à la copie de B6 : une perte après l'ajustement coûte
  jusqu'à ≈ 74 USD de carte sans aucune lentille (24,6 h), ≈ 75 à 77 USD trafic compris (sous l'arrêt dur ; ≈ 64, et ≈ 66 à 68 trafic
  compris, à 2,62 ; v8, m-2).
- **Seul le lieu L2 protège en cours de route** : il reçoit une sauvegarde sur trois pendant B1, puis les lentilles finies dès la fin de
  B1, avant B2. Une perte ne coûte alors que le travail fait depuis la dernière copie, mais les lentilles déjà copiées ne permettent pas
  de finir B-β sans un devis neuf.
- Le lieu L3 ne protège qu'à la fin de la course.

| poste | attendu | pire cas | plan v2 |
|---|---|---|---|
| carte, stockage compris : au prix exigé de 3,00 ; à l'offre de Lettonie du 2026-11-18T01:57:42Z (≈ 2,32) ; à l'offre du Montana du 2026-11-17 (≈ 2,62, disparue) (v8, m-3) | **≈ 26,7 à 40,2 USD** ; ≈ 20,6 à 31,1 ; ≈ 23,3 à 35,1 | 25,1 h × 3,00 (prix exigé) = **75,3 USD** | 21 à 27 ; 63,6 |
| trafic : entrant ≈ 25 Go (poids ≈ 16 Go ; lentilles de Neuronpedia ≈ 3,1 Go, soit 1,04 Go par fichier au plan v2 ; environnement et corpus, compte large, en partie double avec le reste : m-C) ; sortant ≈ 17 Go de lentilles, plus ≈ 43 Go de copies de sauvegarde avec le lieu L2 | 0 à 3,4 USD | **3,4 USD** (≈ 85 Go à 0,04 au plus : les deux prix de trafic sont bornés par la carte exigée) | — |
| disque 200 Go (+ ≈ 8 Gio transitoires pendant une sauvegarde) | compris au prix lu | — | 4 avec le réseau |
| appels de modèles | 0 | 0 | 0 |
| **total** | **≈ 27 à 44 USD** au prix exigé ; ≈ 21 à 31 en Lettonie (trafic ≈ 0,3 USD) ; ≈ 23 à 39 au Montana | **≈ 78,7 USD** | 21 à 27 ; 68 |

**Écart au plan v2 (M6)** : attendu presque égal ; le pire cas prend 3,9 h de plus. Ces heures viennent de B0 à 3 h faute d'essai local
(M4), de la passe refaite (M5), des copies et des sauvegardes. La machine perdue sort du pire cas et devient un arrêt. Le prix exigé reste celui du plan v1 (3,00), d'où un pire cas et un plafond plus hauts que la v2 (v6).
**Plafond de la v6 : 88 USD**, soit **20 USD de plus que les ≈ 68 annoncés** à Lazar (plan v2, § 3.4 ; GO-2026-11-17-03). Le prix exigé
de 3,00 et ce plafond sont la **lecture par la fille précédente** du mot de Lazar du 2026-11-17 vers 01:56 UTC (« prix exigé de 2,25 USD/h.
! monte me pkafond », où « plafond » peut désigner le plafond de dépense ou le prix plafond par heure) : **à confirmer par lui** (v8, M-2).
Arrêt dur à 90 % = 79,2 USD. Le pire cas, ≈ 78,7 USD trafic compris, **tient dessous**, au prix exigé de **3,00 USD/h** et au trafic exigé
de ≤ 0,04 USD/Go dans chaque sens (25,1 × 3,00 + 3,4 = 78,7) ; 88 est le plus petit entier qui le couvre (78,7 / 0,9 = 87,4). La marge
n'est que de 0,5 USD : le flou des sauvegardes non mesurées peut la consommer, et la garde tronque alors la fin de la course. **Le pire
cas suppose zéro relance du processus** pendant l'ajustement : une relance sur la même machine perd jusqu'à une heure de calcul
(sauvegarde horaire), soit 3 USD au prix exigé, six fois la marge ; une relance comptée porterait le plafond à **91 USD** (26,1 × 3,00 +
3,4 = 81,7 ; 81,7 / 0,9 = 90,8 ; v8, m-15). Aux offres vues, la marge est large : pire cas ≈ 61,6 USD en Lettonie (25,1 × 2,32 + 3,4 ;
marge ≈ 17,6), ≈ 69,2 USD au Montana (25,1 × 2,62 + 3,4 ; marge ≈ 10). Bornes voisines, pour information (v8, M-2) : prix exigé 2,25 et
plafond 68 (pire cas 25,1 × 2,25 + 3,4 = 59,9 ; prix minimal de la minuterie 1,61) ; prix exigé 2,62 et plafond 77 (pire cas 69,2 ; prix
minimal 1,83).

## 5. Gardes (reprises du devis de la tranche des lentilles publiques v2, § 3, et adaptées ; contre-lecture de la v1, M2)
Colonne « état » (v8, m-7) : **existe** = pièce versée qui sert telle quelle (chemin, lignes) ; **à dériver** = repris d'une pièce de la
tranche des lentilles publiques, à adapter ; **à écrire** = rien n'existe. Tout ce qui est « à dériver » ou « à écrire » s'essaie sur un
cas sain et sur un artefact avant la course (R5). Les valeurs sont celles du plafond de 88 USD et du prix exigé de 3,00 ; une autre
option du § 7 les change par les mêmes formules.

| garde | valeur | état |
|---|---|---|
| ligne de GO | ligne de calcul neuve, nommée par la mère sur un mot de Lazar ; échéance proposée **2026-11-30** (volet B, plan v2) ; feu écrit avant toute création ; **à l'échéance, sans course, la ligne tombe sans dépense** (v8, m-4) | procédure |
| prix et trafic de l'instance | prix lu sur l'instance au plus le prix exigé, stockage compris ; trafic sortant et entrant ≤ 0,04 USD/Go ; machine vérifiée ; sinon destruction immédiate par identifiant et message à la mère | prix lu : à dériver (contrôle du prix lu de la tranche des lentilles publiques) ; trafic et vérification : à écrire |
| banc du montage (v8, M-4) | au banc de B0 (un document par lentille, sur la machine) : si le temps par document, projeté sur les 2 000 passages, dépasse **13,1 h (23,6 s par document)**, l'ajustement ne part pas : arrêt, destruction par identifiant, compte rendu à la mère ; **compte rendu sans arrêt** au-delà de 1,2 fois la borne haute du banc publié (**14,2 s** par document) | à écrire |
| compte rendu à la mère | **52,8 USD** (60 % de 88), par la garde de dépense ; elle décide de la suite | existe : `garde_depense_v4.py` (seuil 0,60, l. 30-31) |
| arrêt dur | **79,2 USD** (90 % de 88) : destruction par identifiant, réessayée et vérifiée par l'absence | existe : `garde_depense_v4.py` (seuil 0,90, l. 30-31) |
| minuterie v4 et garde v4 | le trafic au pire est **réservé** par `--frais-fixes 3.4` (garde : dépense = carte + 3,4 ; minuterie : durée = (79,2 − 3,4) / prix lu, tronquée à la seconde) : à 3,00, 90 960 s (25,3 h) ; à 2,62, 104 152 s (28,9 h ; v8, m-2) ; à 2,32, 117 620 s (32,7 h). **Sous le prix minimal** (2,11 USD/h au plafond de 88 : la durée dépasserait la borne haute de 129 600 s), **la minuterie est armée à sa borne haute** (36 h, au-delà du pire cas de 25,1 h) au lieu d'un refus : la garde de dépense tient l'arrêt en dollars, et la minuterie, filet de secours, borne la dépense sous l'arrêt dur (36 h × prix lu + 3,4 < 79,2 USD dès que le prix lu est sous le prix minimal) (v8, m-15) | existe : `garde_depense_v4.py` (`--frais-fixes`, l. 138 ; durée, l. 48-51) et `minuterie_destruction_neuron_lens_v4.sh` (bornes 600 à 129 600 s, l. 22) ; armement à la borne haute : à écrire dans la commande |
| bornes en durée | compte rendu à **13,4 h** (haut de l'attendu) ; rappel à **25,1 h** (pire cas, avant la minuterie de 25,3 h au prix exigé ; v6) ; rappel indépendant à 80 % de la minuterie ; échéance de chaque étape écrite dans l'état poussé, dépassement = compte rendu | à dériver (rappels de la commande de la tranche des lentilles publiques, non relus ici) |
| état poussé | toutes les 10 minutes pendant toute la course, ajustement compris (§ 4, perte de machine) | à dériver (poussées de l'amorce de la tranche des lentilles publiques) |
| crédit (v8, m-8) | `can_pay` vrai, `has_billing` vrai, `billing_failed` faux avant la création (champ absent = arrêt) ; **crédit au moins égal au plafond de la tranche, en plus des autres lignes ouvertes sur le même compte**, constaté avant la création, sans alternative ; crédit < 1 USD en cours de course → arrêt (R-2788, R-2795) ; au 2026-11-18 vers 01:19Z, crédit nul (solde −2,19 USD, relevé de la mère) et aucun crédit avant 9 h (mot de Lazar relayé par la mère) | à dériver (contrôles du devis de la tranche des lentilles publiques v2, § 3 ; code non relu ici) |
| course figée | `gpu_util` ≈ 0 **et** `cpu_util` < 10 % à deux contrôles de suite sans nouvelle poussée → arrêt (R-2800) | à dériver (code non relu ici) |
| copie des lentilles | L2 dès la fin de l'ajustement (et une sauvegarde sur trois pendant), L3 après B5, avant la poussée finale ; empreintes vérifiées au lieu d'arrivée **avant** toute destruction prévue ; s'il reste moins d'une heure avant la minuterie ou l'arrêt dur, la mère décide ; **sans réponse en 15 minutes, la copie continue** jusqu'à la minuterie ou l'arrêt dur, qui restent les filets (v4, m-F) ; rien pour L1 | à écrire (§ 2, point 6) |
| perte de machine | détection et arrêt au § 4 ; aucune reprise sans devis neuf et mot de Lazar | suivi : existe (`suivi_vast_v6.py`) ; détection sur l'état poussé : à écrire |
| une seule instance | branche de résultats neuve exigée absente avant la création ; journaux de la minuterie et de la garde commités ; arrêts par PID vérifiés par leurs arguments ; veille et réarmement sur l'échéance absolue après tout redémarrage du conteneur de la session | à dériver (amorce et veille de la tranche des lentilles publiques) |
| destruction | `vastai destroy instance <ID> -y < /dev/null` ; absence prouvée par `suivi_vast_v6 absente <ID> --non-vide`, jamais sur le code de sortie ; préavis d'une ligne à la mère avant la création et la destruction (R-2883) | existe (`suivi_vast_v6.py`) |
| intouchables | 58936096, 58936099, 58936100 (N-009) ; 60988826 (jeu de l'idée du poids du nul, arrêtée, à ne pas détruire) ; 61049303 et le serveur `sauvegarde-temoin-bailey-v2` (session du témoin de Bailey) ; `poste-temoin-bailey-*` ; 60480302, 60599797, 60670453 (absentes au relevé du 2026-11-18T01:23Z) ; toute instance d'une autre session (v7) | procédure |
| refus | tout refus d'une permission, du crochet ou du classifieur : ni rejoué, ni reformulé, ni contourné ; arrêt et nœud à la mère (R-2864) | procédure |

## 6. Leçons de la tranche des lentilles publiques portées
Entrée idempotente et reprise ; `pip` minuté ; clé `HF_TOKEN` aux seuls téléchargements de Llama, retirée ensuite (révocation
recommandée : la clé a été passée à six machines louées, R-3068, R-3093 ; aucun passage à une machine neuve sans mot de Lazar, § 2, point 7) ; balayage des secrets avant chaque poussée ; essai à blanc de
l'environnement exact des essais (variables, chemins, empreintes) et des appels de `measure` ; estimation de la mémoire de pointe de
chaque partie avant la course (pour l'ajustement, au lot de dimensions par défaut du code, 256, `transport.py` l. 46 : pics publiés
sur Qwen3-8B de 25,8 Gio pour R et 39,2 Gio pour S, l. 38 et 41 du journal du banc ; 22,3 et 31,1 Gio au banc final, l. 68-69 ; 47,9 Gio
en compilation par défaut, l. 31 ; Llama a des couches à portes plus larges, non mesuré ; 80 Go laissent une marge large ; pour `measure`
au lot 64 : **au moins** ≈ 23,5 Gio, v4, m-G, et sous ≈ 39 Gio, passée sur une A100 de 40 Go à la recourse, v7 ; v8, m-13) ; carte contrôlée par l'amorce (`CARTE_ATTENDUE`) ; aucun résultat lu par la fille
(lecteur neuf, plan scellé).

## 7. Décisions demandées (à Lazar, par la mère)
Trois décisions séparées (v8, m-11). Aucune n'a de défaut sous 48 heures : ce sont une dépense et des secrets. Rien ne s'engage avant la
réponse de Lazar, même après 9 h (consigne de la mère du 2026-11-18). Quelle que soit l'option, aucune course ne part avant les préalables
du § 2 (texte gelé contre-lu et scellé, addendum des empreintes, correctifs, lanceur, amorce, commande contre-lue, essai à blanc) : un
travail sans dépense, de l'ordre d'une journée de la fille d'après la préparation de la tranche des lentilles publiques (estimation).

### Décision 1 — ouvrir ou non une ligne de calcul pour la tranche de l'ajustement de nos lentilles, et à quel plafond
**Enjeu** : refaire leur chaîne complète sur Llama avec nos lentilles R et S, seule façon de trancher la stabilité de nos lentilles
(B-1), la lecture côté entrée par la lentille S (B-5), notre lentille R contre celle de Neuronpedia (B-6), et, avec notre lentille R, la
lecture contre pilotage, l'avance sur la lentille des logits et la lecture contre ablation couche par couche (B-2, B-3, B-7). Expérience
hors programme : aucun résultat n'entre dans une porte sans nœud (GO-2026-11-17-03).
**Faits** : au prix exigé de 3,00 USD/h, l'offre recevable va et vient (§ 3 : aucune à 01:39:39Z, une à 01:57:42Z le 18) ; aux offres de
Tchéquie (≈ 4,10 à 4,23), le pire cas (≈ 106 à 110 USD) dépasse le plafond de 88 USD. Le plafond de 88 et le prix exigé de 3,00 sont une
lecture d'un mot de Lazar, 20 USD au-dessus des ≈ 68 annoncés (§ 4) : **à confirmer**. Pire cas : sans relance du processus pendant
l'ajustement ; « avec une » compte une heure de plus (§ 4).

| option | périmètre | prix exigé ; plafond | pire cas, sans relance ; avec une | attendu | avantage | inconvénient |
|---|---|---|---|---|---|---|
| **(a)** relever le plafond | entier (R et S) | 4,25 USD/h ; **123 USD** (le plus petit entier dont l'arrêt dur couvre le pire cas) | 25,1 × 4,25 + 3,4 ≈ 110,1 ; 114,3 (plafond 128) | ≈ 36 à 60 USD aux offres de Tchéquie ; moins si une offre moins chère est là | part dès qu'une H100 vérifiée est offerte (deux à quatre offres à chaque relevé du 18) | 35 USD au-dessus des 88 de la v6, 55 au-dessus des 68 annoncés : on paie la certitude de partir |
| **(b)** garder 88 USD, réduire le périmètre | **notre lentille R seulement** (`02_fit.py --lens R`, l. 193) : on **renonce** à trancher la lentille S, sa stabilité (moitié de B-1) et la lecture côté entrée (B-5, `read_S`) | 4,25 USD/h ; 88 USD | ≈ 17,8 × 4,25 + 2,2 ≈ 77,9 ; ≈ 82,1 (plafond 92) | ≈ 24 à 40 USD aux offres de Tchéquie | garde le plafond et les mesures qui servent un moniteur (lecture contre pilotage et contre ablation avec notre R ; notre R contre la publique) | ce n'est plus « refaire leur chaîne » ; la lentille S n'existe nulle part ailleurs ; marge ≈ 1,3 USD sans relance comptée ; chiffres dérivés par la fille de la table du § 4 (une lentille : 1 000 passages, 6,6 h d'ajustement au pire ; trafic 2,2 USD au pire avec le lieu L2), non contre-lus avant cette version |
| **(c)** attendre un prix plus bas | entier | **3,00 USD/h ; 88 USD** (v6, à confirmer ; 91 avec une relance comptée) | 78,7 ; 81,7 | ≈ 27 à 44 USD au prix exigé ; ≈ 21 à 31 à l'offre de Lettonie du 18 | aucun relèvement ; une offre recevable a paru à deux relevés sur quatre ; dépense nulle tant qu'elle ne paraît pas | la fenêtre peut se refermer avant l'échéance du 30 novembre ; une offre disparaît en minutes : la commande doit être prête à partir sur-le-champ ; relevés d'attente en lecture seule, une fois par jour au plus, par la fille ou la mère |
| **(d)** renoncer | — | — | 0 | 0 | aucune dépense ; la tranche des lentilles publiques (« partielle », R-2915) et sa recourse (R-3083) restent le résultat pour la question « utile à un moniteur » | la stabilité de nos lentilles, la lecture côté entrée et notre R contre la publique ne sont jamais mesurées |

Bornes voisines de (c), pour information (§ 4) : prix exigé 2,25 et plafond 68 (pire cas 59,9) ; prix exigé 2,62 et plafond 77 (pire cas
69,2). Au relevé de 01:57:42Z, une offre aurait passé à (2,25 ; 68), le Japon, et deux à (2,62 ; 77).
**Recommandation : (c)**, avec une date butoir au **2026-11-25** pour la course (la lecture par un lecteur neuf doit tenir avant le 30) ;
sans offre recevable d'ici là, **(d)**. Je ne recommande ni (a) ni (b) : (a) paie 35 USD de plafond pour une certitude dont une expérience
hors programme n'a pas besoin, et (b) renonce à des questions et n'a presque pas de marge. **Confiance 0,6** que (c), puis (d), vaut mieux
pour le programme que (a) ou (b). Le choix entre (c) et (d) dépend des priorités de dépense du matin, qui sont à Lazar : le crédit est nul,
et d'autres travaux attendent aussi du crédit.

### Décision 2 — le lieu de rangement des lentilles, si une ligne s'ouvre
**Choix de Lazar ; il conditionne la commande** (§ 2, point 6). **L1** aucun lieu : aucun secret de plus, aucun code de copie ; perte
entière en cas de machine perdue ; tranche non rejouable sans refaire l'ajustement (≈ 16 à 26 USD, montage en sus). **L2** stockage
d'objets privé : protège en cours de route ; exige une clé d'écriture sur la machine louée pendant 6 à 14 h et du code de copie à écrire ;
un compte nouveau est un nœud. **L3** machine de Lazar : protège à la fin seulement ; un accès ou un secret sur la machine louée, ou la
présence de Lazar pendant que la machine se facture. **Recommandation : L1**, confiance 0,55 : la v7 recommandait L2, mais L2 met un second
secret sur une machine louée pendant des heures, alors que la clé d'accès au modèle a déjà été trop exposée ; les empreintes et les
mesures dérivées suffisent à une expérience hors programme.

### Décision 3 — la clé d'accès au modèle
Révocation de la clé actuelle (passée à six machines louées) ; et, si une ligne s'ouvre, passage d'une clé, neuve de préférence, à la
seule machine de la tranche, pour le seul téléchargement de Llama, retirée ensuite (§ 2, point 7). La mère porte cette décision à Lazar
avec les deux autres.

## 8. Reprise de la contre-lecture de la v1
§§ 8 à 12 : tables d'historique ; valeurs et lettres de l'époque de chaque version, remplacées par les §§ 1 à 7 (v8, m-6).

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
| majeure 2 point de sauvegarde et perte de machine | acceptée : perte de machine = arrêt et nœud, sortie du pire cas ; sauvegardes comptées ; copie au lieu L2 (§ 4, § 5) |
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

## 11. Reprise de la quatrième contre-lecture (de la v4)
| point | reprise |
|---|---|
| majeure trafic entrant non borné | acceptée : `inet_down_cost<=0.04` exigé ; trafic réservé à la garde et à la minuterie (§ 3, § 4, § 5) |
| m-1 requête témoin, tableau, sens de la colonne | acceptée : relevé de 01:27Z avec témoin ; tableau et colonne dits (§ 3) |
| m-2 bas de B1 sans copies | acceptée : 5,9 h, total 8,9 h (§ 4) |
| m-3 cadence de poussée | acceptée : toutes les 10 minutes, B1 compris (§ 4) |
| m-4 après la perte | acceptée : destruction, absence, décompte continu (§ 4) |
| m-5 mise en forme de l'en-tête | acceptée (en-tête) |
| m-6 « au moins » au § 1 | acceptée |
| m-7 ponctuation, renvoi d'historique | acceptée (§ 2, point 6) |
| m-8 minuterie à la carte seule | acceptée : `--frais-fixes 3.4` (§ 5) |
| m-9 mêmes lettres | acceptée : lieux L1, L2, L3 |
| m-10 perte trafic compris | acceptée (§ 4) |

## 12. Reprise de la contre-lecture de la v7
Contre-lecture par un contre-lecteur neuf : `contre-lecture-devis-tranche-b-beta-v7.md` (`caf59025…`), « à corriger », 0 bloquante,
4 majeures, 15 mineures ; aucun nom de modèle.

| point | reprise |
|---|---|
| M-1 disponibilité : reste de la v5 contredit par l'en-tête et le § 7 | acceptée : § 3 réécrit (table des relevés, bilan, offre du Montana recevable à 3,00) |
| M-2 plafond monté de 68 à 88 non porté à la décision ; source non vérifiable | acceptée : § 4 et § 7 (20 USD de plus, lecture du mot à confirmer, bornes voisines (2,25 ; 68) et (2,62 ; 77)) |
| M-3 second secret et code de copie des lieux L2 et L3 | acceptée : § 2, point 6 ; § 5 (« à écrire ») ; § 7, décision 2 (recommandation changée en L1) |
| M-4 aucune règle d'arrêt après le banc du montage | acceptée : § 5, garde « banc du montage » (23,6 s et 14,2 s par document), à écrire et à essayer (R5) |
| m-1 seuils 1,70 et 2,11 ; sept A100 de 80 Go sur sept | acceptée : § 3 (seul le seuil en vigueur ; sept sur sept) |
| m-2 pertes arrondies vers le bas ; 104 152 s | acceptée : § 4 (≈ 74, ≈ 75 à 77 ; ≈ 64, ≈ 66 à 68) ; § 5 (104 152 s) |
| m-3 attendu au prix d'une offre disparue | acceptée : § 4 et § 7 (au prix exigé ; en Lettonie ; au Montana) |
| m-4 plafond au prix du marché ; sort de la ligne ; relevés d'attente | acceptée : § 7, option (a) (123 USD) et option (c) (relevés d'attente) ; § 5 (la ligne tombe à l'échéance) |
| m-5 empreintes manquantes | acceptée : en-tête (relevé de 01:27Z) ; § 4 (dix fichiers de durée) |
| m-6 tables d'historique ; v3 et v2 enchaînées | acceptée : ligne en tête du § 8 ; v3 et v2 séparées dans l'en-tête |
| m-7 ce qui existe et ce qui est à écrire | acceptée : colonne « état » du § 5 |
| m-8 rechargement automatique contredit par le solde négatif | acceptée : alternative retirée (§ 2, point 8 ; § 5) |
| m-9 levée de GO-2026-11-15-04 échue ; sixième passage de la clé | acceptée : § 2, point 7 (échue ; R-3086 cité) |
| m-10 épreuve du relevé, hôte | acceptée : script v2 et relevé neuf ; « une offre par hôte » réfutée (§ 3) |
| m-11 forme de la décision | acceptée : trois décisions ; quatre options chiffrées, avec avantage et inconvénient ; objet de la confiance dit |
| m-12 nommage | acceptée : titre du § 3 ; première mention de la tranche des lentilles publiques en clair ; noms au § 7 ; légende des renvois (en-tête) |
| m-13 « HBM3 », lot de l'ajustement, unités | acceptée : § 3, § 4, § 6 ; légende des unités ; « Gio » écrit « Gio » partout |
| m-14 « ≈ 15 USD » pour refaire l'ajustement | acceptée : ≈ 16 à 26 USD, montage en sus (§ 2, point 6 ; § 7) |
| m-15 relance du processus ; minuterie sous le prix minimal | acceptée : § 4 (zéro relance supposée ; 91 USD avec une relance) ; § 5 (minuterie armée à sa borne haute) |

## 13. Contre-lecture de la v8
Contre-lecture ciblée par un sous-agent neuf, autre que celui de la v7 : reprise de chaque point du § 12, chiffres neufs des §§ 3, 4, 5 et
7, cohérence d'ensemble. Sa reprise ira dans une version suivante, sous un nom neuf (R12).
