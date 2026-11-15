# Devis de la tranche B-α de « Neuron Lens » — v2 (Llama 3.1 8B Instruct, lentilles publiques ; aucune dépense, aucune location)

**v2 = v1** (`devis-tranche-b-alpha-v1.md`, `3e06dbcd…`, archivée) **corrigée après sa contre-lecture**
(`docs/notes/neuron-lens-v1/devis-b-alpha/contre-lecture-devis-tranche-b-alpha-v1.md`, `b9b3beb1…`, verdict « feu possible après
corrections ») **et les décisions de la mère R-2861** (M1 à M6), avec les mots de Lazar R-2852 (préparer le devis) et R-2860
(`HF_TOKEN`). Écrit par la fille « Neuron Lens » (session `session_016QhUrtahFZo57fZUcRReVA`, branche `prep/neuron-lens-v1`). **Aucune
location, aucune dépense** ; rien sur `main`.

## Différentiel déclaré (v1 → v2)
| point | v1 | v2 |
|---|---|---|
| M1 | addendum partie 2 absent du plan | étape **3 bis** : partie 2 de l'addendum et sorties des contrôles de B0, scellées et poussées après le corpus et avant la fumée ; garde du lanceur |
| M2 | plafond 10 USD ; audits R4 non chiffrés | plafond **12 USD** (ligne GO-2026-11-14-06), compte rendu **7,20**, arrêt dur **10,80** ; audits R4 chiffrés sur la même machine ; **correctif (3)** à écrire, contre-lire, sceller avant le feu ; prix lu exigé **≤ 0,80 USD/h** pour que le pire cas complet tienne sous l'arrêt dur |
| M3 | bornes en argent seulement | bornes **en durée** : compte rendu à 4,9 h, rappel à 9,1 h, échéance par étape dans l'état poussé |
| M4 | repli RTX 5090, puis 3090 | **aucun repli** : pas de RTX 4090 ≤ 0,80 USD/h (prix lu) → rien ne part, message à la mère ; l'option RTX 3090 est un changement de ligne |
| M5 | exposition de `HF_TOKEN` sous-estimée | exposition résiduelle écrite ; `HF_HUB_OFFLINE=1`, aucun nom secondaire, aucune session du hub ; essai des sept formes rejoué pour cette clé ; couvert par GO-2026-11-15-04 |
| M6 | `-causal.pt` entier versé au brut | **empreinte** du fichier et grandeurs **par pôle calculées par notre code** ; voie de sortie essayée à blanc ; toute retouche du code voisin = nœud |
| mineurs 1 à 14 | | portés aux endroits marqués « (m1) » à « (m14) » |
| ordre | téléchargements, puis B0 | tokeniseur et lentilles d'abord, **poids du modèle après B0** (contre-lecture, point 6) |
| attendu | 1,1 à 2,2 USD | **1,2 à 2,5 USD** (prix lu estimé à l'offre + 10 % de stockage pour 150 Go ; trafic relevé avant création) |

Pièces qui font foi pour B-α : texte gelé `texte-gele-volet-a-et-b-alpha-v6.md` (`34b88243…`), § B.1 (commun), § B (seuils), plan
d'analyse § B.1 à B.4, critères de lecture B, audit R4, liste d'arrêt ; addendum `addendum-empreintes-v3.md` (`e63d95ca…`, partie 1 ;
§ 3, § 4 et § 6 pour la partie 2) ; correctifs scellés sous `docs/notes/neuron-lens-v1/correctifs/` ; plan et devis v2 (§ 3.1, § 3.4).
Dépôt voisin `stdlogits/neuron-lens` au commit `849bfe16`, lu, jamais exécuté dans le conteneur (R-2710) ; empreintes lues le
2026-11-15 : `README.md` `c3764398…`, `docs/findings.md` `8814874b…`, `scripts/checks/causal_lens.py` `befb7018…`,
`scripts/06_activations.py` `151d1196…` (égales aux copies archivées).

**Statut (m1)** : ce devis sert à la **demande de feu sous GO-2026-11-14-06** (12 USD, échéance 2026-11-30, R-2725), avec le second
secret couvert par **GO-2026-11-15-04** (R-2860) ; toute carte autre que la RTX 4090 demande un mot à part de Lazar.

## 1. Plan exact (texte gelé, plan d'analyse § B.1), lieu et durée de chaque étape

Sources : **mesuré, transposé** = mesuré au volet A (14-15 novembre, journal `journal-course-volet-a-v2.md`) sur un autre montage ;
**publié, transposé** = auteurs, sur Qwen3-8B (36 couches × 12 288 neurones), transposé à Llama 3.1 8B (32 × 14 336, même largeur 4 096,
volume voisin) ; **supposé** = estimation de l'autrice.

| étape | où | attendu | pire cas (borne d'étape) | source |
|---|---|---|---|---|
| 0. amorce : clone (entrée idempotente), première poussée, environnement (`pip` verbeux, `timeout` **3 600 s**, code dédié) (m10) | réseau, processeur | 0,5 à 1,0 h | 1,5 h | mesuré au volet A (47 min, cause inconnue), transposé ; borne = `timeout` + marge |
| 1. téléchargement du **tokeniseur** (révision `0e9e39f2…`, accès contrôlé) et des trois lentilles J, J++, R (1,04 Go chacune, publiques) | réseau | 0,05 à 0,1 h | 0,2 h | supposé |
| 2. **B0** : essai du correctif (1) (`essai-06_activations-llama-v3.py`) et du correctif (2) (`essai-lenses-neuronpedia-v3.py`), aucun test sauté ; lecture des trois lentilles par `neuronpedia_lens` (empreintes, couches contiguës, **autres clés consignées**) ; contrôles « nombre de couches lues == 31 » et « aucune matrice identité aux couches 0 à 27 » de `verdicts_b_alpha_v3.py` (`controle_lentille`, l. 215) ; provenances, `catalog.kept` et **comptes des doubles jetons de début** de `controles_b0_v2.py` ; `config.yaml` et `CREDIT.md` (**convention « clé l = sortie de la couche l »**) ; essai des crochets de pilotage et d'ablation sur un Llama miniature (**à écrire**, m4) ; code des verdicts (B.3) rejoué sur la machine (m5) | processeur | 0,1 à 0,3 h | 0,5 h | supposé (essais du volet A : 30 s) |
| 2 bis. téléchargement des **poids** de `meta-llama/Llama-3.1-8B-Instruct` (révision `0e9e39f2…`, ≈ 16 Go), seulement si B0 est passé ; puis `HF_TOKEN` retiré (§ 5) | réseau | 0,05 à 0,2 h | 0,4 h | supposé (16 Go ≈ 7 min à 300 Mb/s) |
| 3. corpus d'activations : `05_act_corpus.py --docs dclm=40000,zh=8000,code=8000,chat=8000` (addendum § 4), après dépôt du fichier de provenance « chat » au nom de Llama (`correctif-provenance-chat-llama-v2.md`) ; comptes de jetons `03_token_counts.py` (m3) | réseau, processeur | 0,1 à 0,3 h | 0,5 h | publié (« minutes », README l. 552-554), transposé |
| **3 bis. addendum des empreintes, partie 2** (fichier neuf, R12) : empreintes des poids, du tokeniseur et des trois lentilles téléchargés (égalité exigée), des **quatre tranches** du corpus (égalité des listes d'identifiants de lignes), versions des bibliothèques, tailles, comptes des doubles jetons de début ; **sorties** des contrôles de B0 ; scellé **sur la machine** par notre code (aucune pause humaine) et poussé ; tout écart = arrêt (M1) | processeur, réseau | 0,05 à 0,1 h | 0,3 h | supposé |
| 4. fumée `06_activations.py --docs 64` (« writes no tables », l. 608) ; **ne part pas** sans le compagnon de la partie 2 (garde du lanceur) | carte | 0,1 h | 0,2 h | supposé |
| 5. passe complète `06_activations.py` (bf16 ; tables écrites par 16 processus, éprouvées seulement en fin de passe, m11) ; reprise des états gardés toutes les 10 min (`--save-minutes`) après une relance (m12) | **carte**, puis processeur | 1,0 à 1,4 h | 2,5 h | publié (« ~70 min on an RTX 4090 », README l. 555 ; « 68 minutes », findings l. 109), transposé |
| 6. `causal_lens.py measure` aux défauts publiés (lignes 374 à 377 de la copie : 32 neurones par couche, `random.Random(0)`, deux pôles, 16 contextes de 64 jetons, positions `[16, T)`, doses 1× et 4× `act_top`, ablation sur les 8 premiers documents du pôle, fenêtre de 8) (m6) ; reprise des états | **carte** | 0,3 à 1,0 h | 2,0 h | supposé (4 096 conditions de pilotage, 16 384 contextes d'ablation) |
| 7. `score --lenses logit,J,npJpp,npR` ; recalcul de n par notre code ; grandeurs par pôle (§ 4) ; verdicts par `verdicts_b_alpha_v3.py` (scellé) ; intervalles (2 000 tirages) ; déclencheurs « trop beau » et « tout négatif » évalués **avant la destruction** (m8) | **processeur** (`mps` sinon `cpu`, l. 277) | 0,1 à 0,3 h | 0,8 h | supposé |
| 8. poussées, état final, sortie (entrée idempotente : une relance par le loueur lit l'état final et attend sans calcul) | réseau | 0,1 h | 0,3 h | mesuré au volet A |
| **total de la course** | | **2,5 à 4,9 h** | **9,1 h** | |
| audit R4 « trop beau » : `measure` relancé avec la graine 1 par le **correctif (3)**, puis `score` ; **même machine, avant destruction** | carte, processeur | — | + 2,8 h | pire cas des étapes 6 et 7 |
| audit R4 « tout négatif » : `score` rejoué sur la sortie publiée de `measure` (2,9 Go, addendum § 3), **même machine** | réseau, processeur | — | + 0,8 h | supposé |

**La machine pousse le brut ; la lecture reste à un lecteur neuf** (m8), comme au volet A. **Ce qui diffère du volet A** : B-α n'ajuste
aucune sonde ; ses étapes longues (5, 6) sont des passes du modèle sur la carte ; le processeur ne sert qu'à l'écriture des tables et à
`score`. Pire cas complet : course 9,1 h + réinstallation 1,5 h + audit le plus long 2,8 h = **13,4 h**.

## 2. La machine

**Une RTX 4090, une seule instance, prix lu sur l'instance (`dph_total`, stockage compris) ≤ 0,80 USD/h** ; aucun repli (M4) : s'il n'y
en a pas, **rien ne part**, message à la mère (nœud : autre carte). Exigences : 24 Go (README l. 567-568), bf16 ; 16 cœurs au moins
(l. 613 de `06_activations.py`) ; 64 Go de mémoire ; 150 Go de disque ; CUDA ≥ 13.0 ; prix du trafic de l'offre relevé avant création ;
`dph_total` relu sur l'instance après création, exigé ≤ 0,80, sinon destruction (m9).

Prix relevés par programme le 2026-11-15 à 07:59:24 UTC (`vastai search offers`, filtre ci-dessus ; source :
`docs/notes/neuron-lens-v1/devis-b-alpha/releve-prix-vast-20261115T075924Z-v1.tsv`, `7a3d56e0…`) : **RTX 4090, 34 offres, la moins chère
0,4547 USD/h, médiane 0,5216**. Pour mémoire (hors ligne) : RTX 3090 0,2069, RTX A5000 0,3214, RTX 5090 0,4860, RTX A6000 0,5669, L4
0,9398 ; vitesses relatives non mesurées (m14).

Pourquoi la RTX 4090 (inchangé) : carte des durées publiées ; les auteurs notent que les **effets faibles dépendent du matériel**
(findings l. 207-209), et B-7 (« ablate win », couches 0 à 15) est la mesure la plus exposée ; l'écart de prix est de quelques dizaines
de centimes.

## 3. Plafond, durées, échéance, gardes

| poste | valeur |
|---|---|
| attendu | **≈ 1,2 à 2,5 USD** (2,5 à 4,9 h à ≈ 0,50 USD/h lu : offre 0,4547 + ≈ 10 % de stockage pour 150 Go ; au volet A, + 5,6 % pour 80 Go) |
| pire cas complet | 13,4 h × 0,80 USD/h = **10,72 USD**, sous l'arrêt dur ; au prix du jour (≈ 0,50) : ≈ 6,7 USD |
| **plafond** | **12 USD** (ligne GO-2026-11-14-06, M2) |
| compte rendu à la mère | **7,20 USD** (60 %), par la garde de dépense v4 ; elle décide de la suite |
| arrêt dur | **10,80 USD** (90 %) : destruction par identifiant, réessayée et vérifiée par l'absence |
| **bornes en durée** (M3) | compte rendu à la mère à **4,9 h** de location (haut de l'attendu) ; **rappel programmé à 9,1 h** (pire cas de la course), la mère décide ; échéance de chaque étape (attendu et pire cas du § 1) écrite dans l'état poussé ; dépassement du pire cas d'une étape = compte rendu |
| minuterie | durée = 90 % du plafond au prix lu (à 0,80 : 48 600 s ; à 0,4547 : 85 506 s) ; la minuterie v3 refuse au-delà de 108 000 s, soit un prix sous 0,40 USD/h : **minuterie v4** à écrire (borne haute 129 600 s, 12 USD à 0,30), contre-lue et essayée (m13) |
| rappel indépendant | à 80 % de la durée de la minuterie, en plus du rappel en durée |
| échéance | **2026-11-30** |
| destruction | `vastai destroy instance <ID> -y < /dev/null` ; absence prouvée par `suivi_vast_v6 absente <ID> --temoin 60480302` (ou 60670453), jamais sur le code de sortie |
| crédit | relevé à l'étape 3 de la commande et à chaque contrôle : `can_pay` vrai, `has_billing` vrai, `billing_failed` faux (champ absent = arrêt) ; crédit < 1 USD en cours de course → arrêt (R-2788, R-2795) |
| course figée | `gpu_util` ≈ 0 **et** `cpu_util` < 10 % à deux contrôles de suite, sans nouvelle poussée → arrêt (R-2800) |
| repris de la commande v14 | une seule instance ; branche de résultats `calcul/neuron-lens-b-alpha-v1` exigée absente ; journaux de la minuterie et de la garde commités ; arrêts par PID vérifiés par leurs arguments ; veille et réarmement après tout redémarrage du conteneur de la session |
| intouchables | 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, `poste-temoin-bailey-*` |

## 4. Leçons du volet A portées dans B-α (sans changer aucun critère gelé)
1. **Témoins rejouables, sans le fichier entier (M6)** : `-causal.pt` (≈ 2,9 Go pour Qwen3-8B, addendum § 3 ; même ordre attendu ; au-delà
   de la limite de 100 Mo de l'hébergeur, connue, non revérifiée) **n'est pas versé** ; sont versés : son **empreinte**, et, **calculées par
   notre code lisant ce fichier** (jamais par une retouche de `score`), les grandeurs **par pôle** : r par lentille et par cible (matché
   et témoin), motif d'écart, n recalculé et pôles écartés par motif, `top_doc`, `top_pos`, doses ; plus le centile commun du témoin. Taille
   bornée (≈ 1 024 neurones × 2 pôles × 4 lentilles × 4 cibles : quelques Mo). Voie de sortie (poussée git vers le dépôt privé) **essayée à
   blanc** avant le feu. **Toute retouche du code voisin, `score` compris, est un nœud de Lazar** (m7 ; écart 14 du texte gelé).
2. **Manifeste** : versions de toutes les bibliothèques importées ; commit voisin `849bfe16` et empreintes des correctifs ; champ `graines`
   rempli (`random.Random(0)` ; `SeedSequence(entropy=20261114)`, branche « B-α ») ; commit réduit **et** commit source ; empreintes des
   fichiers de résultats.
3. **Rapportés sans critère** : « steer 4x » et « ablate pos » au même grain ; intervalles et leur graine.
4. **Exploitation** : destruction `-y` et preuve d'absence ; **entrée idempotente** (clone seulement s'il manque ; état final lu au
   démarrage → attente sans calcul ; sinon **reprise** des états gardés au lieu de recommencer, m12) ; **`pip` verbeux, `timeout` 3 600 s**,
   code dédié ; veille et réarmement ; PID lus dans les fichiers ; durées par étape écrites dans l'état poussé.
Aucun point de ces leçons ne touche un critère gelé (contre-lecture, réponse 1, sous la condition du point 1 ci-dessus).

## 5. Jetons et accès pour la machine

- **Jeton du programme** (`CONTROLE_IA_GITHUB_TOKEN_2`) : voie du volet A (passé par son nom comme `GH_TOKEN` par `--env` ; en-tête HTTP
  seulement ; branche dédiée du dépôt réduit en clone `--depth 1 --single-branch` ; poussée vers `calcul/neuron-lens-b-alpha-v1` ;
  course sous `env -u GH_TOKEN`). Réserve inchangée : il écrit sur tout le dépôt. Nouveau pour B-α : le code voisin tourne plus longtemps
  et plus largement sur la machine (étapes 2 à 7).
- **`HF_TOKEN`**, couvert par **GO-2026-11-15-04** (R-2860) : passé **par son nom seulement**, dans le seul shell de lancement, pour le
  seul téléchargement du tokeniseur (étape 1) et des poids (étape 2 bis) de `meta-llama/Llama-3.1-8B-Instruct` ; **jamais écrit** dans un
  fichier, un journal, une sortie ni une branche ; aucune session du hub ouverte (`huggingface-cli login` interdit : il écrirait la clé
  dans un fichier) ; après le téléchargement : `env -u HF_TOKEN -u HUGGING_FACE_HUB_TOKEN` et `HF_HUB_OFFLINE=1` pour tout le reste,
  vérifiés par leur nom (absence dans l'environnement de chaque étape suivante, sans lire la valeur). Relevé d'accès du
  2026-11-15T07:59:51Z : `config.json`, `tokenizer.json` : 200 avec la clé, 401 sans (codes seuls) ; lentilles : 200 sans clé.
  **Exposition résiduelle (M5), déclarée** : passée par `--env`, la clé reste (a) dans la **configuration de l'instance chez le loueur
  jusqu'à la destruction** (visible dans l'interface du compte du loueur), (b) dans l'**environnement du processus d'entrée** pendant
  toute la location, et (c) elle **revient à chaque relance du conteneur** par le loueur. `env -u` la retire aux processus enfants
  seulement : il suffit contre une fuite par héritage (journaux, manifeste, vidage de l'environnement), pas contre un code qui la
  chercherait (le code voisin tourne sous le même utilisateur) ni contre l'exploitant de la machine. Le suivi v6 balaie déjà
  `HF_TOKEN` ; **l'essai des sept formes est à rejouer à blanc pour cette clé** (arbre, objets git, journaux, manifeste, état poussé).
  Recommandation de la mère, à Lazar (acte de compte, hors de mon périmètre) : une **clé neuve à lecture seule, limitée à ce modèle,
  révoquée après la course**. Si une permission ou le classifieur refuse ce passage : ni contournement ni reformulation, message à la
  mère.

## 6. Ce qui reste à faire avant la demande de feu (travail de session, sans dépense)
1. **Correctif (3)** de l'audit « trop beau » (seconde graine de neurones, 1, pour `measure`), écrit, contre-lu, scellé (M2).
2. **Essai des crochets** de pilotage et d'ablation sur un Llama miniature, écrit et contre-lu (m4).
3. **Notre code** des grandeurs par pôle lisant `-causal.pt` (M6 ; le recalcul de n existe déjà, scellé : `n_par_couche` et
   `n_depuis_causal`, `verdicts_b_alpha_v3.py` l. 245-289), et celui de la **partie 2 de l'addendum** (M1), avec essais (cas sain et
   artefacts).
4. **Lanceur** de la course B-α (étapes 1 à 8, gardes : B0 avant toute passe ; partie 2 scellée avant la fumée ; B.3 consigné avant la
   location et rejoué sur la machine avant `measure`, m5 ; audits R4 sur la même machine avant destruction).
5. **Amorce B-α** (entrée idempotente avec reprise, `pip` verbeux et minuté, `HF_TOKEN` pour le seul téléchargement) ; **minuterie v4**
   (m13) ; **dépôt réduit B-α** (code voisin à `849bfe16` + correctifs scellés + nos modules).
6. **Essai à blanc** : voie de sortie du brut (M6), entrée idempotente et reprise, sept formes pour `GH_TOKEN` et `HF_TOKEN` (M5).
7. **Commande** de location et de lancement (bornes du § 3), **contre-lectures**, scellements ; puis demande de feu citant la commande, le
   commit réduit, la liste et le paquet.

## Décision demandée
**Feu sous GO-2026-11-14-06** après les pièces du § 6 : RTX 4090, prix lu ≤ 0,80 USD/h, **plafond 12 USD**, compte rendu 7,20, arrêt
dur 10,80, bornes en durée 4,9 h et 9,1 h, échéance 2026-11-30 ; `HF_TOKEN` selon GO-2026-11-15-04. Enjeu : « la lecture R tient-elle
sur Llama 3.1 8B Instruct » pour ≈ 1,2 à 2,5 USD. Options : (a) ce plan — avantage : conforme à la ligne et au texte gelé, pire cas
complet sous l'arrêt dur ; inconvénient : 7 pièces à écrire et contre-lire avant le feu ; (b) **changement de ligne** vers une RTX 3090
(≈ 0,8 à 1,6 USD) — avantage : moins cher ; inconvénient : vitesse non mesurée, écart à la référence sur les effets faibles, mot de Lazar
exigé ; (c) attendre. Recommandation : (a), confiance 0,65. Pas de défaut sous 48 heures : c'est une dépense.
