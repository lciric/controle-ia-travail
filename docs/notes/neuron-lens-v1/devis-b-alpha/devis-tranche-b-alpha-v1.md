# Devis de la tranche B-α de « Neuron Lens » — v1 (Llama 3.1 8B Instruct, lentilles publiques ; aucune dépense, aucune location)

Écrit par la fille « Neuron Lens » (session `session_016QhUrtahFZo57fZUcRReVA`, branche `prep/neuron-lens-v1`) sur la demande de la
mère du 2026-11-15T07:56Z (« go » de Lazar à l'option (a), R-2852). **Aucune location, aucune dépense** : les seuls appels au loueur sont
des recherches d'offres (lecture). Le GO-2026-11-14-05 ne couvrait que le volet A ; ce devis sert à un **GO neuf** de Lazar. Rien
n'est sur `main`.

Pièces qui font foi pour B-α : texte gelé `docs/notes/neuron-lens-v1/texte-gele-volet-a-et-b-alpha-v6.md` (`34b88243…`), § B.1 (commun),
§ B (seuils), § B.1 du plan d'analyse (étapes), § B.2 (graines), § B.3 (code des verdicts essayé) ; addendum des empreintes
`addendum-empreintes-v3.md` (`e63d95ca…`) ; correctifs scellés sous `docs/notes/neuron-lens-v1/correctifs/` ; plan et devis v2
(`plan-et-devis-v2.md`, § 3.1 et § 3.4 : B-α à ≈ 3 USD attendus, plafond 12 USD). Dépôt voisin `stdlogits/neuron-lens` au commit
`849bfe16`, lu (jamais exécuté dans le conteneur, décision (a) de Lazar, R-2710) ; empreintes lues le 2026-11-15 : `README.md`
`c3764398…` (égale à l'archive), `docs/findings.md` `8814874b…` (égale), `scripts/checks/causal_lens.py` `befb7018…`,
`scripts/06_activations.py` `151d1196…`.

## 1. Plan exact de la course B-α (texte gelé, plan d'analyse § B.1) : où tourne chaque étape, combien de temps

Sources des durées : **mesuré** = volet A du 14-15 novembre (journal `journal-course-volet-a-v2.md`) ; **publié** = auteurs du dépôt
voisin (Qwen3-8B, 36 couches × 12 288 neurones ; Llama 3.1 8B a 32 couches × 14 336 neurones, même largeur 4 096 : volume de calcul
comparable) ; **supposé** = estimation de l'autrice, à confirmer sur la machine.

| étape (texte gelé § B.1) | où | durée attendue | pire cas | source |
|---|---|---|---|---|
| 0. amorce : clone du dépôt réduit, première poussée, environnement (`torch`, `transformers` ≥ 5, `datasets`, `pyarrow`…) | réseau, processeur | 0,5 à 1,0 h | 1,5 h | **mesuré** : 47 min pour l'environnement du volet A (devis : 5 à 10 min) |
| 1. téléchargements : modèle `meta-llama/Llama-3.1-8B-Instruct` à la révision `0e9e39f2…` (≈ 16 Go, **accès contrôlé**, voir § 5) ; J, J++, R de `neuronpedia/jacobian-lens` (1,04 Go chacune, publiques) | réseau | 0,1 à 0,3 h | 0,5 h | supposé (≈ 20 Go à 300-900 Mb/s) |
| 2. B0 : essai du correctif (1) (`essai-06_activations-llama-v3.py`) et du correctif (2) (`essai-lenses-neuronpedia-v3.py`), aucun test sauté ; lecture des trois lentilles par `neuronpedia_lens` (empreintes, couches contiguës) ; **notre code de B0** (`controles_b0_v2.py`, scellé : « nombre de couches lues == 31 », « aucune matrice identité aux couches 0 à 27 ») ; `config.yaml` et `CREDIT.md` ; essai des crochets de pilotage et d'ablation sur un Llama miniature | processeur | 0,1 à 0,3 h | 0,5 h | supposé (essais miniatures ; ceux du volet A : 30 s) |
| 3. corpus d'activations (`05_act_corpus.py`) et comptes de jetons (`03_token_counts.py`) | réseau, processeur | 0,1 à 0,3 h | 0,5 h | **publié** : « minutes » chacun (README l. 552-554) |
| 4. fumée `06_activations.py --docs 64` | carte | 0,1 h | 0,2 h | supposé |
| 5. passe complète `06_activations.py` (bf16, tables écrites par 16 processus) | **carte**, puis processeur (écriture des tables) | 1,0 à 1,4 h | 2,5 h | **publié** : « ~70 min on an RTX 4090 » (README l. 555) ; « 68 minutes on an RTX 4090 » (findings l. 109) |
| 6. `causal_lens.py measure` (32 neurones par couche, `random.Random(0)`, 2 pôles, 16 contextes de 64 jetons, doses 1× et 4×, ablation sur 8 documents, fenêtre 8 ; défauts l. 373-384) | **carte** | 0,3 à 1,0 h | 2,0 h | supposé (≈ 4 100 conditions de pilotage par lots de 16, ≈ 16 000 contextes d'ablation par lots de 64 ; aucune durée publiée) |
| 7. `score --lenses logit,J,npJpp,npR` ; recalcul de n ; verdicts (`verdicts_b_alpha_v3.py`, scellé) ; intervalles (2 000 tirages) | **processeur** (le code choisit `mps` sinon `cpu`, l. 277) | 0,1 à 0,3 h | 0,8 h | supposé (≈ 2 Tflop de produits matrice-vecteur sur 32 couches × 4 lentilles × 1 024 neurones) |
| 8. poussées, état final, sortie | réseau | 0,1 h | 0,3 h | mesuré (volet A) |
| **total** | | **2,4 à 4,8 h** | **8,8 h** | |

**Ce qui diffère du volet A** : le volet A était limité par le **processeur** (carte à 0 %, processeur à 96 % pendant 9 h : ajustement des
sondes `scikit-learn` sur neurones, rééchantillonnages) ; **B-α n'ajuste aucune sonde** : ses deux étapes longues (5 et 6) sont des
passes du modèle sur la carte ; le processeur ne sert qu'à l'écriture des tables (16 processus) et à `score`. Le pire cas double
néanmoins la somme des durées attendues longues (le volet A a pris deux fois son devis).

## 2. La machine la moins chère qui suffit

Besoin : une carte CUDA de **24 Go** (« 24 GB is enough for the text passes », README l. 567-568), bf16 ; **16 cœurs** au moins (16
processus d'écriture des tables, l. 613 de `06_activations.py`) ; 64 Go de mémoire ; **150 Go de disque** (modèle 16 Go, lentilles 3,1
Go, corpus, tables d'activations, environnement ≈ 10 Go) ; CUDA ≥ 13.0 (roue `torch` du volet A, CUDA 13). **Une seule machine** : les
étapes processeur (2, 3, 7) durent des minutes, une machine séparée coûterait plus en montage qu'elle n'épargne.

Prix relevés **par programme le 2026-11-15 à 07:59:24 UTC** (`vastai search offers`, filtre ci-dessus, tri par prix) ; source :
`docs/notes/neuron-lens-v1/devis-b-alpha/releve-prix-vast-20261115T075924Z-v1.tsv` (5 offres les moins chères par carte, empreintes des
sorties brutes) :

| carte (24 Go ou plus) | offres | la moins chère (USD/h) | médiane | vitesse relative à la RTX 4090 pour les passes bf16 (supposé) |
|---|---|---|---|---|
| RTX 3090 (24 Go, Ampère) | 14 | **0,2069** (France, vérifiée, 16 cœurs, 63 Gio) | 0,3564 | ≈ 0,45 à 0,6 |
| RTX A5000 (24 Go) | 1 | 0,3214 | 0,3214 | ≈ 0,45 à 0,55 |
| **RTX 4090** (24 Go, Ada) | 34 | **0,4547** (Pays-Bas, vérifiée, 32 cœurs, 126 Gio) | 0,5216 | 1 (référence publiée) |
| RTX 5090 (32 Go) | 42 | 0,4860 | 0,9021 | ≈ 1,2 à 1,4 |
| RTX A6000 (48 Go) | 2 | 0,5669 | 0,5714 | ≈ 0,5 à 0,6 |
| L4 (24 Go) | 2 | 0,9398 | 0,9398 | ≈ 0,3 |

Coût attendu à la moins chère du jour (stockage compris dans `dph_total`) : **RTX 4090** : 2,4 à 4,8 h × 0,4547 ≈ **1,1 à 2,2 USD** ;
**RTX 3090** : étapes carte (4 à 6) ≈ 2 fois plus longues, total ≈ 3,8 à 7,6 h × 0,2069 ≈ **0,8 à 1,6 USD**.

**Recommandation : RTX 4090**, prix plafond **0,90 USD/h** (inchangé), confiance 0,6. Raisons : l'écart attendu est de quelques dizaines
de centimes ; la 4090 est la carte des durées publiées (le devis tient sur des chiffres relevés, la 3090 sur une supposition de vitesse) ;
les auteurs ont rejoué l'ablation sur RTX 4090 et notent que **les effets faibles dépendent du matériel** (findings l. 207-209), ce qui
plaide pour la même famille de carte que la référence ; une course deux fois plus longue double l'exposition aux redémarrages du
conteneur de la session (deux le 14-15 novembre). Repli si aucune 4090 ≤ 0,90 USD/h : RTX 5090 (plus rapide), puis RTX 3090 (signalée
comme écart de matériel au rapport, aucun critère changé).

## 3. Plafond, échéance, gardes

| poste | valeur |
|---|---|
| attendu | **≈ 1,1 à 2,2 USD** (RTX 4090 à 0,4547 USD/h) |
| pire cas | 8,8 h × 0,90 USD/h = 7,9 USD ; installation refaite une fois (1,5 h) : + 1,4 USD → **≈ 9,3 USD** |
| **plafond proposé** | **10 USD** (la ligne GO-2026-11-14-06 portait 12 USD ; le pire cas recalculé tient sous 10) |
| échéance | **2026-11-30** (celle de GO-2026-11-14-06) |
| compte rendu à la mère | **60 %** du plafond (6 USD), par la garde de dépense v4 (`garde_depense_v4.py`), elle décide de la suite |
| arrêt dur | **90 %** (9 USD) : destruction par identifiant, réessayée et vérifiée par l'absence |
| minuterie | `scripts/minuterie_destruction_neuron_lens_v3.sh`, posée à la création, durée = 90 % du plafond au prix du jour, PID écrit par la minuterie |
| rappel indépendant | à 80 % de la durée de la minuterie |
| destruction | `vastai destroy instance <ID> -y < /dev/null`, absence prouvée par `suivi_vast_v6 absente <ID> --temoin <ID>`, jamais sur le code de sortie |
| crédit | relevé à l'étape 3 et à chaque contrôle : `can_pay` vrai, `has_billing` vrai, `billing_failed` faux, sinon arrêt ; crédit < 1 USD en cours de course → arrêt (R-2788, R-2795) |
| course figée | `gpu_util` ≈ 0 **et** `cpu_util` < 10 % à deux contrôles de suite, sans nouvelle poussée → arrêt (R-2800) ; pour B-α, attendre `gpu_util` > 0 aux étapes 4 à 6 |
| intouchables | 58936096, 58936099, 58936100, 60480302, 60599797, 60670453, `poste-temoin-bailey-*` |

## 4. Leçons du volet A portées dans B-α (sans changer aucun critère gelé)

Relevées dans le journal de la course et dans le verdict du lecteur (`lecture-volet-a/verdict-volet-a-v1.md`, réserves 5 à 7) :
1. **Témoins versés dans le brut** : pour chaque couche, cible et lentille, écrire dans le brut scellé, outre `r_med`, `pass`,
   `control_med` : les r **par pôle** (matché et témoin), le centile commun du témoin, le **n recalculé** et le nombre de pôles écartés
   **par motif**, et le fichier `-causal.pt` entier (cibles, `top_doc`, `top_pos`) ; un lecteur doit pouvoir **rejouer** chaque condition
   (au volet A, les rangs des 102 témoins n'étaient pas dans le brut).
2. **Manifeste** : versions de **toutes** les bibliothèques importées (`torch`, `transformers`, `datasets`, `numpy`, `scipy`, `pyarrow`,
   `safetensors`, `huggingface_hub`) ; commit du dépôt voisin (`849bfe16`) et empreintes des correctifs appliqués ; champ `graines` rempli
   (`random.Random(0)` du dépôt pour les neurones ; `SeedSequence(entropy=20261114)`, branche « B-α », pour le reste, texte gelé § B.2) ;
   commit réduit **et** commit source ; empreintes des fichiers de résultats.
3. **Rapportés sans critère** : « steer 4x » et « ablate pos » (texte gelé § B.1) écrits dans le brut au même grain que les cibles à
   critère ; intervalles par rééchantillonnage (2 000 tirages) et leur graine écrits.
4. **Exploitation de la machine** : destruction avec `-y` et preuve d'absence (minuterie v3, garde v4, suivi v6, déjà scellés) ;
   **entrée idempotente** (le loueur relance le conteneur sorti : au volet A, l'entrée a échoué en boucle, « depot already exists », instance
   facturée sans travail — amorce neuve : clone seulement s'il manque, et état final lu au démarrage → attente sans calcul) ; **`pip` verbeux
   et minuté** (`timeout`, code dédié ; 47 min au volet A, sans trace) ; veille de la minuterie et de la garde dans la session, réarmement
   après tout redémarrage du conteneur (deux au volet A) ; PID lus dans les fichiers, jamais `$!`.
5. **Devis** : durées mesurées sur la machine dès la première course (temps par étape écrit dans l'état poussé).
Tout point qui toucherait un critère gelé est un **nœud de Lazar, à écrire à part** ; je n'en vois aucun dans les leçons ci-dessus (ce
sont des ajouts au brut et à l'exploitation). Un point est à trancher par la mère, hors critère : § 5, second secret.

## 5. Jetons et accès pour la machine

- **Jeton du programme** (`CONTROLE_IA_GITHUB_TOKEN_2`), voie reprise du volet A, qui a marché : passé par son nom comme `GH_TOKEN` à la
  création (`--env`), employé **seulement** en en-tête HTTP (`git -c http.extraHeader=…`) pour cloner la branche dédiée du dépôt réduit
  (`--depth 1 --single-branch`) et pousser sur une branche de résultats neuve (`calcul/neuron-lens-b-alpha-v1`, exigée absente avant la
  location) ; jamais dans l'adresse, la configuration ni un fichier ; la course tourne sans lui (`env -u GH_TOKEN`). Réserve inchangée :
  il permet l'écriture sur tout le dépôt (portée à Lazar).
- **Jeton du hub de modèles** (`HF_TOKEN`) : **nouveau besoin**. `meta-llama/Llama-3.1-8B-Instruct` est à accès contrôlé : relevé du
  2026-11-15T07:59:51Z, `config.json` et `tokenizer.json` : **200 avec le jeton de la session, 401 sans** (code HTTP seul relevé). Les
  lentilles de `neuronpedia/jacobian-lens` sont publiques (200 sans jeton, 08:00:03Z). La machine doit donc recevoir `HF_TOKEN` pour le
  seul téléchargement du modèle (étape 1), puis `env -u HF_TOKEN` pour tout le reste ; le suivi v6 le balaie déjà (il est dans sa liste).
  **Décision de la mère** (second secret sur une machine louée) ; à défaut, B-α ne peut pas télécharger le modèle (le texte gelé fait d'un
  échec d'accès sous licence un arrêt de montage).

## 6. Ce qui reste à faire avant une demande de feu (travail de session, sans dépense)
Lanceur de la course B-α (étapes 2 à 8, gardes de B0 et de B.3 avant `score`), amorce B-α (entrée idempotente, `pip` minuté, `HF_TOKEN`
pour le seul téléchargement), dépôt réduit B-α (code du dépôt voisin à `849bfe16` + correctifs scellés + nos modules), essai à blanc,
commande, contre-lectures, scellements ; puis demande de feu citant la commande, le commit réduit, la liste et le paquet.

## Décision demandée
**Accorder la tranche B-α** : RTX 4090 (≤ 0,90 USD/h), **plafond 10 USD**, échéance 2026-11-30, gardes du § 3 ; autoriser `HF_TOKEN` sur
la machine pour le seul téléchargement du modèle. Enjeu : réponse à « la lecture R tient-elle sur Llama 3.1 8B Instruct » pour ≈ 1 à 2
USD. Options : (a) RTX 4090, plafond 10 USD — avantage : durées publiées, même famille de carte que la référence ; inconvénient : ≈ 0,3 à
0,6 USD de plus que (b) ; (b) RTX 3090, plafond 10 USD — avantage : ≈ 0,8 à 1,6 USD attendus ; inconvénient : vitesse supposée, course
deux fois plus longue, écart de matériel à déclarer ; (c) attendre. Recommandation : (a), confiance 0,6. Pas de défaut sous 48 heures :
c'est une dépense.
