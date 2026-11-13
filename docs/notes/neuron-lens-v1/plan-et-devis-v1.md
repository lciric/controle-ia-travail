# « Neuron Lens » : essai sur un modèle publié (volet A) et reproduction sur Llama 3.1 8B (volet B) — plan et devis, v1

Écrit par la session fille « Neuron Lens » le 13 novembre 2026 (heures relevées par `date -u` : début 13:01 UTC, prix 13:04 UTC,
licences 13:06 UTC), sous la consigne `consigne-fille-neuron-lens-v1.md` (`43ac1788…`) et les interdits communs v2 (`1ee3b370…`).
**Aucune dépense, aucune location, aucun appel de modèle n'a eu lieu.** Ce texte est un plan et un devis ; il ne lance rien.
Abréviations gardées : USD, Go (gigaoctet), « H100 », « A100 », « RTX 4090 » (noms de cartes), « AUROC » (aire sous la courbe
de détection ; 0,5 = hasard).

## 0. Verdict en cinq lignes

1. **Faisable, et pas cher.** Le code est public, sous licence MIT, et tient en une chaîne numérotée ; les lentilles et le
   catalogue sont sous CC BY 4.0. Volet A : ≈ 1 USD attendu, plafond proposé **10 USD**. Volet B : ≈ 30 USD attendus, plafond
   proposé **80 USD**. Aucun appel de modèle payant dans les deux lignes.
2. **Llama 3.1 8B se prête à la chaîne, à une retouche près.** Par lecture du code : l'ajustement des lentilles ne dépend que
   de pièces que Llama possède (normes RMS, couche à portes SiLU, attention sans biais) ; la passe d'activations plante en
   revanche sur les têtes d'attention (elle exige des normes de requête et de clé que Llama n'a pas) : une retouche bornée
   d'un seul script. **Non vérifié par exécution** : l'essai gratuit sur un Llama miniature a été refusé par le classifieur
   de permissions (§ 7) ; je ne l'ai pas contourné.
3. **Ce n'est pas un moniteur, et le volet A le teste comme tel** : la lentille lit-elle ce sur quoi une sonde s'appuie
   (audit de fuite textuelle, avec une fuite plantée connue et un témoin sans lentille), et des neurones font-ils d'aussi
   bons traits qu'une sonde sur le flux résiduel, à budget égal et hors distribution ? Les deux issues sont écrites d'avance.
4. **Réserves (R4).** Les chiffres publiés sont sans réplication ; la mesure phare (lecture contre pilotage) tend vers 1 en
   fin de réseau pour toute lentille, y compris la plus naïve : seule la moitié basse du réseau et l'avance sur les témoins
   sont informatives. Le pilotage pousse au-delà du régime naturel (jusqu'à 4 fois l'activation typique, à chaque position).
5. **Recommandation** : accorder les deux lignes, B d'abord sur la même machine que A (un seul montage) ; confiance 0,6 que B
   reproduit le motif, 0,4 que A montre un apport net pour un moniteur au-delà d'un sac de mots. Sans les lignes, rien ne part.

## 1. Sources, empreintes, licences

| pièce | où | empreinte ou révision |
|---|---|---|
| dépôt de recherche `stdlogits/neuron-lens` (cloné en lecture, jamais écrit) | `https://github.com/stdlogits/neuron-lens` | commit `849bfe1678e28becceb1e3864afe5fc8297d02e4` (11 novembre 2026) ; `README.md` `c3764398…`, `docs/findings.md` `8814874b…`, `docs/design.md` `88478b63…` : identiques à l'archive du lecteur (`docs/sources/neuron-lens-lecture-20261113/manifeste-sources-v1.tsv`) |
| chiffres publiés de référence (copies) | `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/` | `causal_lens_qwen3-8b.json` `8904c4d3…`, `reads_at_firings_qwen3-8b.json` `ac0bf101…`, `fit_bench_h100_2026-10-28.log`, `scripts-checks-causal_lens.py.txt` (compagnons `.sha256`) |
| prix relevés | `docs/sources/neuron-lens-v1-devis-20261113/prix-vast/` | cinq fichiers, relevés à 13:04 UTC (§ 5.1) |
| licences des contrastes publics | `docs/sources/neuron-lens-v1-devis-20261113/licences/` | relevées à 13:06 UTC |

Licences : code de `neuron-lens` **MIT** (`LICENSE`, « Copyright (c) 2026 a9lim and treetowntree ») ; lentilles
`stdlogits/rs-lenses` et catalogue `stdlogits/neuron-lens` **CC BY 4.0** (citation obligatoire) ; Qwen3-8B **Apache 2.0** (dit
par le dépôt ; à relire sur la fiche du modèle avant le téléchargement) ; Llama 3.1 8B Instruct : licence communautaire
Llama 3.1, déjà acceptée par le programme ; lentilles J et R de Llama 3.1 8B Instruct déjà publiées par Neuronpedia
(`neuronpedia/jacobian-lens`, dossier `llama3.1-8b-it`, 1,04 Go chacune, 64 documents de WikiText, licence Llama 3.1) ;
contrastes du volet A : `llm-attacks` (AdvBench) MIT, `JailbreakBench` MIT, `representation-engineering` (faits vrais et
faux, gabarit honnête/malhonnête) MIT. **Écarté** : `geometry-of-truth` (aucun fichier de licence trouvé : 404).

## 2. Ce que le code permet sans réécriture

La chaîne (README, « Reproducing ») : `01` corpus des lentilles → `02_fit.py` (lentilles R et S) → `05` corpus d'activations
→ `03` comptes de jetons → `06_activations.py` → `07_drivers.py` → `08_reads.py` → `checks/reads_at_firings.py` →
`checks/causal_lens.py measure` puis `score`. Le modèle se choisit par `NEURON_LENS_MODEL` et `--model`.

| étape | Qwen3-8B (volet A) | Llama 3.1 8B Instruct (volet B), par lecture du code |
|---|---|---|
| lentilles | publiées (4 fichiers de 2,42 Go) : rien à ajuster | `02_fit.py` : attendu sans retouche. `layers.py` compose chaque couche à partir de ce qu'elle contient ; `check` refuse seulement les biais de projection, l'attention bidirectionnelle et les pièces de Qwen3.5 ; les normes de requête et de clé sont lues par `getattr(..., None)`. Noms de poids de Llama = branche « non Gemma » de `arch.names` et `neurons.mlp_names` |
| passe d'activations | publiée dans le catalogue ; à refaire seulement pour nos invites | **`06_activations.py` plante** : `hooks` lit `at.q_norm` et `at.k_norm` sans garde (lignes 287-289). Retouche : sauter ces deux crochets quand la norme manque et laisser à zéro les sommes des têtes. Une dizaine de lignes, un seul fichier |
| lectures par les poids | publiées | `08_reads.py --parts neurons` (l'option existe) : sans retouche ; la partie « têtes » (`arch.qk`) exige les normes absentes : **hors périmètre** |
| lecture contre pilotage | chiffres publiés (`causal_lens_qwen3-8b.json`) | `causal_lens.py` : sans retouche pour le pilotage et l'ablation ; la notation prend `--lenses logit,R:<notre ajustement>` ; témoin J : une ligne à ajouter au dictionnaire `NEURONPEDIA_FILES` de `lenses.py` (le fichier J de Llama existe chez Neuronpedia) |
| étiquettes | publiées (Claude Haiku) | non refaites (§ 4.4) |

Limite de cette colonne : **lecture seule**. Les essais de l'estimateur du dépôt comparent les lentilles à des jacobiennes
calculées par force brute sur un Qwen3 miniature aléatoire ; le même essai sur un Llama miniature aléatoire (aucun poids
téléchargé, processeur seul) aurait tranché ; il a été refusé (§ 7). Il devient l'étape B0, première chose faite sur la
machine louée, avec arrêt si l'écart à la force brute dépasse celui du Qwen3 miniature.

## 3. Volet A — Neuron Lens tel que publié, sur Qwen3-8B : apporte-t-il quelque chose à un moniteur ?

Modèle : Qwen3-8B (changement de modèle permis pour ce seul volet, mot de Lazar R-2528). Aucune donnée réservée du programme,
aucune sonde du programme. Couches lues : 8, 14, 20, 26 (un quart, deux cinquièmes, plus de la moitié, trois quarts de la
profondeur ; choisies avant toute mesure). Position : dernier jeton de l'invite (aucune moyenne sur les jetons).

### 3.1 Contrastes publics (trois, fixés d'avance)
- **C1, nuisible contre bénin** : 100 comportements nuisibles et 100 bénins appariés par thème de JailbreakBench ; hors
  distribution : les 520 comportements nuisibles d'AdvBench contre les bénins tenus à l'écart.
- **C2, fuite plantée** : les mêmes faits vrais (jeu de `representation-engineering`), précédés de la consigne « honnête » ou
  « malhonnête » du gabarit publié. La seule différence entre classes est le mot de la consigne : la fuite textuelle est
  **connue par construction**. Hors distribution : même contraste avec une paraphrase de la consigne (« truthful » /
  « deceptive »), écrite avant la course.
- **C3, vrai contre faux** : faits vrais contre faux du même jeu, sans consigne. Témoin où la fuite lexicale attendue est faible.

Découpes : 5 découpes apprentissage/test (70/30) par `numpy.random.SeedSequence`, graines au manifeste (R9) ; intervalles par
rééchantillonnage sur les exemples de test.

### 3.2 Mesure (i) — lire la direction d'une sonde : audit de fuite textuelle
Sonde : régression logistique (pénalité L2 choisie par validation interne) sur le flux résiduel à la sortie de la couche.
Sa direction est lue par la lentille S (quels jetons d'entrée la portent : `w · K_L (W_E[v] − moyenne)`) et par la lentille R
(ce qu'elle fait dire), sur les jetons gardés du catalogue.

| | hypothèse | métrique | témoins | seuil de lecture, écrit d'avance |
|---|---|---|---|---|
| A1 (C2) | la lentille S retrouve une fuite plantée | rang des jetons plantés (liste fixée : formes de « honest » et « dishonest ») dans la lecture S de ±w | 100 directions aléatoires de même norme ; sonde apprise sur étiquettes permutées ; direction de la sonde de C3 ; **lecture sans lentille** `w · (W_E[v] − moyenne)` | « retrouvée » : un jeton planté dans les 10 premiers à au moins 2 des 4 couches, et dans moins de 1 % des directions aléatoires. « non retrouvée » : aucune couche. Entre les deux : « partiel » |
| A2 (C1) | la lecture S nomme les jetons qui séparent les classes | précision à 20 : part des 20 premiers jetons de la lecture S parmi les jetons associés à la classe (sac de jetons, taux de fausses découvertes 5 %) ; corrélation de rangs avec les poids du sac de jetons | les mêmes quatre | « nomme » : précision à 20 ≥ 0,25, au-dessus du 99ᵉ centile des directions aléatoires, à au moins 2 couches |
| A3 (C1, C2) | les jetons nommés sont ceux dont la sonde dépend | chute d'AUROC de la sonde quand on retire des invites de test les 20 jetons de la lecture S | 20 jetons aléatoires de même fréquence (200 tirages) ; les 20 premiers jetons du sac de jetons | « dépendance lue » : chute au-dessus du 95ᵉ centile des tirages aléatoires et ≥ la moitié de la chute obtenue avec le sac de jetons |

**Ce qui dirait « apporte quelque chose à un moniteur » pour (i)** : A1 retrouvée **et** la lentille S fait mieux que la
lecture sans lentille à au moins 2 couches sur A1 ou A2. **Ce qui dirait « n'apporte rien »** : A1 non retrouvée, ou la
lecture sans lentille fait aussi bien partout (la lentille est alors un détour), ou le sac de jetons dit déjà tout (A3 :
chute inférieure à la moitié de la sienne partout). La lecture R de ±w est rapportée telle quelle (20 premiers jetons par
couche), sans critère : description.

### 3.3 Mesure (ii) — des neurones comme traits d'un détecteur
Traits : activations des neurones de la couche à portes (porte activée × montée, 12 288 par couche), mêmes couches, même
position. Détecteurs : régression logistique parcimonieuse à budget k ∈ {1, 8, 64, 512} neurones choisis sur
l'apprentissage ; régression dense sur tous les neurones. Comparés, sur les mêmes découpes, à : la sonde sur le flux
résiduel (4 096 dimensions) ; la même sonde restreinte à k directions principales (budget égal) ; k neurones tirés au
hasard ; un sac de jetons (prédicteur sur le texte seul, dans l'esprit de N-029).

Métrique : AUROC en distribution et hors distribution (§ 3.1), écart apparié à la sonde résiduelle, intervalle à 95 %.
Prédiction écrite (sans signe visé, R3) : en distribution, écart inférieur à 0,02 dès k = 64 ; hors distribution, aucune
direction prédite. **« Apporte quelque chose »** : à k ≤ 64, AUROC ≥ sonde résiduelle − 0,02 en distribution **et**
intervalle de l'écart hors distribution qui contient 0 ou lui est favorable. **« N'apporte rien »** : la sonde résiduelle
gagne de plus de 0,05 à tout k ≤ 512, en distribution et hors distribution. Description jointe, sans critère : pour les 8
premiers neurones de chaque détecteur, l'étiquette et les lectures du catalogue publié, et leur accord avec une liste de
mots du concept fixée avant la course (aucun juge par modèle).

### 3.4 Audit symétrique (R4), déclenché des deux côtés
Si A1 réussit à toutes les couches avec un rang 1, ou si les neurones égalent la sonde partout : vérifier que la lecture ne
voit pas les étiquettes (direction permutée), que le retrait de jetons change bien le texte, relancer sur une sixième
découpe. Si tout échoue : vérifier la chaîne sur le neurone publié `L8 n344 +` (« owl »), dont la lecture R et S est
donnée dans le README ; si ce témoin sain n'est pas retrouvé, le résultat est « chaîne en défaut », pas « n'apporte rien ».

### 3.5 Étapes, machine, durée
Une carte de 24 Go suffit (README : « 24 GB is enough for the text passes ») : RTX 4090. Montage et téléchargements (modèle
16 Go, lentilles 9,7 Go, tables du catalogue pour les couches lues ≈ 1 Go) : 0,75 h. Passes avant sur ≈ 3 000 invites
courtes, quatre couches : minutes. Sondes, lectures, retraits de jetons : 0,5 h. Scellement et transfert : 0,25 h.
**Attendu : 1,5 à 2 h.** Disque : 60 Go.

## 4. Volet B — refaire la chaîne sur Llama 3.1 8B Instruct

Modèle : `meta-llama/Llama-3.1-8B-Instruct` (celui des agents et des sondes, programme v2 § « Modèles ») : 32 couches,
14 336 neurones par couche, 4 096 dimensions. Aucun usage dans une expérience préenregistrée du programme : c'est une
reproduction à part ; tout branchement sur T0.7, T0.8 ou G1 serait un nœud.

### 4.1 Étapes
- **B0** montage ; essais de l'estimateur du dépôt ; **essai Llama miniature contre la force brute** (garde : arrêt si
  l'écart dépasse celui du Qwen3 miniature) ; banc d'un document par lentille (durée et mémoire réelles, avant d'engager
  les heures).
- **B1** lentilles R et S : 1 000 documents de DCLM (révision épinglée par le dépôt), 128 jetons, moitiés paires et
  impaires séparées ; reprise sur point de sauvegarde.
- **B2** corpus d'activations (web, chinois, code, conversation rendue par le gabarit de Llama), comptes de jetons, passe
  d'activations **avec la retouche du § 2**, contre-lue avant usage (R2) et gardée dans notre dépôt comme un correctif daté.
- **B3** pilotes exacts par substitution de jetons (`07`) ; lectures par les poids, neurones seulement (`08`).
- **B4** lecture contre pilotage : 32 neurones tirés au hasard par couche (graine 0, comme les auteurs), deux pôles, doses
  1× et 4×, 16 contextes de 64 jetons ; ablation en contexte ; notation contre trois lentilles : logits, J (Neuronpedia),
  R (la nôtre), plus R de Neuronpedia comme comparaison entre deux codes.
- **B5** lectures aux activations (`reads_at_firings.py`, neurones).
- **B6** manifeste par course (R9), résultats bruts scellés, lentilles ajustées copiées hors de la machine (≈ 10 Go ;
  gardées hors du dépôt git, empreintes au manifeste), machine détruite par son identifiant (R10), dépense relevée.

### 4.2 Mesures de validité, plan d'analyse écrit d'avance

Référence : Qwen3-8B, fichiers empreintés du § 1. La comparaison se fait à **profondeur relative** (Llama a 32 couches,
Qwen3-8B 36). Seuils fixés à environ 0,8 fois la valeur publiée à la même profondeur relative. La mesure n'emploie
aucune lentille (`measure`) ; la lentille n'entre qu'à la notation : pas de circularité par construction, à vérifier dans
la sortie.

| | ce que les auteurs rapportent (Qwen3-8B) | métrique sur Llama | témoin | « reproduit » | « non reproduit » |
|---|---|---|---|---|---|
| B-1 stabilité | moitiés du corpus : écart ≤ 6 % à chaque couche ; même premier jeton pour 89 à 99 % des neurones (README, résultat 1 : niveau transcription) | écart relatif entre moitiés par couche (imprimé par `02_fit.py`) ; accord du premier jeton des lectures d'écriture | — | écart ≤ 10 % partout et accord ≥ 80 % partout | une couche à plus de 20 % ou un accord sous 60 % |
| B-2 lecture R contre pilotage, dose 1× | r médian 0,33 (couche 0), 0,45 (4), 0,49 (8), 0,65 (12), 0,74 (16), 0,87 (20), 0,95 (24) ; part des pôles « prédits » ≥ 0,94 à chaque couche dès la couche 5 (`causal_lens_qwen3-8b.json`, `8904c4d3…`) | r de Pearson médian sur le vocabulaire gardé, par couche ; part des pôles au-delà du 99ᵉ centile du témoin | lecture du neurone voisin tiré au hasard (médiane publiée entre −0,04 et +0,03 selon la couche) | r médian ≥ 0,40 sur les couches 8 à 15, ≥ 0,60 sur 16 à 23, ≥ 0,85 sur 24 à 27 ; part prédite ≥ 0,90 sur les couches 8 à 27 ; témoin : médiane entre −0,05 et +0,05 | part prédite < 0,50 sur les couches 16 à 27, ou r médian < 0,30 sur 16 à 23, ou témoin hors de ±0,10 (chaîne en défaut) |
| B-3 avance sur la lentille des logits | couche 8 : 0,49 contre 0,12 ; écart de +0,35 à +0,42 des couches 4 à 17 (même fichier) ; la lentille des logits rejoint vers la couche 20 | écart des r médians, R moins logits, par couche | — | écart ≥ +0,20 à chaque couche de 4 à 15 | écart ≤ 0 sur plus de la moitié de ces couches |
| B-4 avance sur la lentille J | +0,03 à +0,13 des couches 4 à 23 (même fichier, vérifié couche par couche) | écart des r médians, R moins J | **réserve** : la lentille J de Llama vient d'un autre corpus (WikiText, 64 documents) | rapporté, **non décisif** : signe et taille, couche par couche | — |
| B-5 côté entrée, lentille S | à la couche 0, la lecture S nomme le jeton sous l'activation pour 85 % des pôles (`read_S` = 0,848, `reads_at_firings_qwen3-8b.json`, `ac0bf101…`) | `read_S` par couche (part des pôles au taux de fausses découvertes 5 %) | lecture d'un autre pôle de la couche | `read_S` ≥ 0,60 à la couche 0 et décroissant sur le premier quart | `read_S` < 0,30 à la couche 0 |
| B-6 deux codes | — | notre lentille R contre celle de Neuronpedia : écart des r médians de B-2 | — | rapporté : écart absolu ≤ 0,05 attendu | un écart > 0,15 ouvre un audit des deux |

Verdict d'ensemble du volet B : **« reproduit »** si B-1, B-2, B-3 et B-5 le sont ; **« non reproduit »** si B-2 ou B-3 ne
l'est pas ; sinon **« partiel »**, mesure par mesure. Les couches 28 à 31 ne comptent pas pour B-2 ni B-3 : toute lentille y
atteint r ≈ 1 (0,9998 pour la lentille des logits à la dernière couche de Qwen3-8B), ce qui ne dit rien.

**R3, R4.** Aucune course ne vise un signe : « non reproduit » est un résultat, rapporté à l'identique. Audit symétrique :
si tout passe très au-dessus des seuils (r ≥ 0,95 dès le premier quart) ou si le témoin vaut exactement 0, vérifier que le
témoin apparie bien un autre neurone, que le pilotage change les prédictions (norme non nulle), relancer B4 avec une
seconde graine de neurones (graine 1, ≈ 0,5 h, comprise au devis). Si tout échoue : rejouer `causal_lens.py score` sur les
lentilles publiées de Qwen3-8B (cas sain) avant de conclure. Tout écart à ce plan est écrit avant d'être fait.

### 4.3 Ce qui n'est pas refait
Têtes d'attention ; images et son ; arêtes et sources ; l'étiquetage complet (105 USD chez les auteurs pour 884 736 pôles).

### 4.4 Échantillon d'étiquettes (option B-bis, chiffrée, non recommandée maintenant)
160 pôles tirés au hasard (la taille du pilote des auteurs), étiquetés par Claude Haiku à partir des lectures et des
contextes, puis notés à l'aveugle par détection (AUROC, publié : 0,80 à 0,89). Coût : moins de 3 USD de modèle au pire
(l'étiquetage complet des auteurs revient à 0,012 centime par pôle ; la notation coûte plus que l'étiquette), 1 h de carte.
Plafond à part proposé : **6 USD**. Je recommande de l'attendre : étiqueteur et juge de la famille Claude (réserve de
N-053), et l'étiquette en mots n'entre pas dans la question « utile à un moniteur ».

## 5. Devis

### 5.1 Prix relevés le 13 novembre 2026 à 13:04 UTC
Source : interface publique de recherche d'offres de Vast.ai (`console.vast.ai/api/v0/bundles`), sans clé, client générique,
offres vérifiées, à la demande, une carte. Fichiers et empreintes dans `prix-vast/`.

| carte | offres | minimum | médiane | maximum (USD par heure) | note |
|---|---|---|---|---|---|
| RTX 4090, 24 Go | 40 (les 40 moins chères) | 0,374 | 0,507 | 0,870 | volet A |
| A100 SXM4, 40 Go | 7 | 0,601 | 0,845 | 1,451 | repli du volet B ; aucune A100 de 80 Go offerte ce jour |
| A100 PCIE, 40 Go | 5 | 0,403 | 0,590 | 0,808 | repli |
| H100 SXM, 80 Go | **1** | 2,344 | 2,344 | 2,344 | carte des relevés de durée des auteurs |
| H200 | 2 | 5,264 | 5,672 | 6,080 | **exclue** sans un mot de Lazar (usage du programme) |

Stockage relevé : 0,13 à 1,00 USD par Go et par mois selon l'offre.

### 5.2 Volet A

| poste | attendu | pire cas |
|---|---|---|
| carte RTX 4090 | 2 h × 0,51 = 1,0 USD | 8 h × 0,87 = 7,0 USD (un remontage, un téléchargement lent, une relance) |
| disque 60 Go et réseau | < 0,1 USD | 1,0 USD |
| appels de modèles | 0 | 0 |
| **total** | **≈ 1 USD** | **8 USD** → plafond proposé **10 USD** |

### 5.3 Volet B

Durées publiées (Qwen3-8B) : lentille, 11 à 16 s par document sur une H100, soit ≈ 3 h par lentille pour 1 000 documents
(README ; banc `fit_bench_h100_2026-10-28.log` : 11,2 à 11,8 s, pic de 20 à 29 Go à lot de 128, 48 Go compilé à lot de
256) ; passe d'activations ≈ 70 min sur une RTX 4090 ; pilotes 12 min ; lectures 5 à 7 min. Llama a moins de couches (32
contre 36) et des couches à portes plus larges (14 336 contre 12 288) : je compte 0,9 à 1,2 fois Qwen3-8B, **hypothèse non
mesurée**, levée par le banc de B0.

| poste (une H100 de 80 Go à 2,344 USD/h) | attendu | pire cas |
|---|---|---|
| B0 montage, essais, banc | 1,0 h | 3 h (retouche à déboguer sur la machine, faute d'essai local) |
| B1 deux lentilles, 1 000 documents chacune | 6,2 à 8,9 h | 13,2 h (1,5 fois la borne haute) |
| B2 corpus et passe d'activations | 1,5 h | 3 h |
| B3 pilotes et lectures | 0,5 h | 1 h |
| B4 pilotage, ablation, notation, seconde graine si audit | 1,0 h | 2 h |
| B5, B6 lectures aux activations, scellement, transfert | 0,8 h | 1,5 h |
| une machine perdue et remontée (les ajustements reprennent) | — | 1 h |
| **heures** | **11 à 13,7 h** | **≈ 24,7 h** |
| carte | 26 à 32 USD | 24,7 h × 3,00 USD/h (prix plafond par heure) = 74 USD |
| disque 150 Go, réseau | ≈ 1 USD | 5 USD |
| appels de modèles | 0 | 0 |
| **total** | **≈ 30 USD** | **≈ 79 USD** → plafond proposé **80 USD** |

Repli si aucune H100 n'est offerte à 3,00 USD/h ou moins : A100 de 40 Go à lot de 128 (le pic publié de 20 à 29 Go y
tient), vitesse **non mesurée** (je compte 2 à 3 fois plus lent) : 16 à 30 h à 0,60–0,85 USD/h, soit 10 à 26 USD, sous le
même plafond ; le banc de B0 décide avant d'engager les heures, et si la projection dépasse le plafond je m'arrête et
j'écris. Réduction possible, non recommandée : 500 documents par lentille (≈ 20 USD attendus), au prix de la fidélité à B-1.

Garde de dépense : horloge de la machine relevée à chaque étape ; arrêt et message à la mère à 60 % du plafond ; arrêt dur
à 90 % ; minuterie de destruction par identifiant posée à la création (R10).

### 5.4 Ce qui se fait sans dépense, avant ou sans GO
Déjà fait : lecture du code et des chiffres publiés, relevé des prix et des licences. Faisable sur processeur, sans carte :
le texte gelé de chaque volet (préenregistrement court tiré des §§ 3 et 4.2) et sa contre-lecture par un sous-agent neuf
(R2) ; l'écriture de la retouche de `06_activations.py` ; la préparation des trois contrastes et du sac de jetons ; la
lecture descriptive du catalogue publié. **Non faisable ici** : toute passe sur un modèle de 8 milliards de paramètres
(15 Go de mémoire vive sur cette machine) ; et, tant que le refus du § 7 tient, toute exécution locale du code cloné.

## 6. Lignes de GO proposées (à inscrire par la mère sur un mot direct de Lazar)

| objet | plafond | échéance |
|---|---|---|
| **Volet A** — Neuron Lens tel que publié sur Qwen3-8B (modèle permis pour ce seul volet, R-2528) : audit de fuite textuelle d'une sonde et neurones comme traits, sur trois contrastes publics sous licence MIT, plan `docs/notes/neuron-lens-v1/plan-et-devis-v1.md` §§ 3 et 5.2 ; une carte RTX 4090 (ou la machine du volet B) chez Vast.ai, ≤ 0,90 USD/h si louée seule ; aucun appel de modèle ; texte gelé contre-lu et scellé avant la course ; destruction par identifiant | **10 USD** | 2026-11-30 |
| **Volet B** — reproduction de la chaîne Neuron Lens sur `meta-llama/Llama-3.1-8B-Instruct` : lentilles R et S (1 000 documents), passe d'activations, lecture contre pilotage et témoins, plan §§ 4 et 5.3 ; une carte H100 de 80 Go ≤ 3,00 USD/h, repli A100 de 40 Go ; aucune H200 ; aucun appel de modèle ; texte gelé contre-lu et scellé avant la course ; compte rendu à 60 % du plafond ; destruction par identifiant | **80 USD** | 2026-11-30 |
| *option B-bis, non recommandée maintenant* — échantillon de 160 étiquettes et leur notation à l'aveugle | *6 USD* | — |

Format de décision. **Décision** : accorder A, B, les deux, ou aucun. **Enjeu** : savoir, pour ≈ 30 USD, si cette lecture
des neurones tient sur notre modèle et sert un moniteur, avant d'y investir du temps de programme. **Options** : (a) A et B —
réponse complète ; coût ≈ 31 USD attendus, 90 au pire ; (b) B seul — la reproduction sur notre modèle, sans la question
du moniteur ; (c) A seul — la question du moniteur pour ≈ 1 USD, mais sur un modèle qui n'est pas le nôtre.
**Recommandation** : (a), confiance 0,6. Pas de défaut sous 48 heures : c'est une dépense, sans mot rien ne part.

## 7. Réserves, nœuds, refus

- **Refus rapporté tel quel.** Entre 13:04 et 13:06 UTC (bornes relevées par `date -u`), la commande qui lançait, sur processeur et dans un environnement jetable, les
  essais du dépôt cloné (`tests/test_transport.py`) puis leur copie avec `LlamaConfig` et `LlamaModel` à la place de
  `Qwen3Config` et `Qwen3Model` a été refusée par le classifieur du mode automatique (« Unauthorized Access »). Je n'ai ni
  reformulé ni contourné. Conséquence : la portabilité à Llama est établie par lecture seulement ; l'essai passe en B0, sur
  la machine louée (compris au pire cas). Si Lazar veut le lever : une règle de permission pour exécuter localement ce
  dépôt public (essais sur modèles miniatures aléatoires, aucun poids téléchargé).
- **Prix** : relevés par l'interface publique sans clé, pas par l'outil `vastai` (interdit commun 3) ; une seule H100
  offerte ce jour.
- **Note du lecteur** (`docs/notes/lecture-voisin-neuron-lens-v1.md`) : pas encore sur `main` à 13:10 UTC (commit `b202431c`) ; ce plan s'appuie
  sur ses sources archivées et sur le code. À sa parution je la confronte au code et je signale tout désaccord.
- **Niveau des chiffres (R7)** : les valeurs de B-2, B-3 et B-5 viennent des fichiers de résultats publiés, empreintés ; les
  fourchettes de B-1 viennent du README (niveau transcription, à relire dans `docs/findings.md` avant le texte gelé) ;
  chaque valeur citée de `causal_lens_qwen3-8b.json` a été recalculée sur les 36 couches à 13:10 UTC.
- **Ce plan n'a pas été contre-lu** (R2) : la contre-lecture porte sur le texte gelé de chaque volet, avant toute course.
- **Nœuds** : toute dépense hors ligne inscrite ; tout usage de ces lentilles ou de ces neurones dans T0.7, T0.8, G1 ou
  un préenregistrement du programme ; toute lecture de la direction d'une **sonde du programme** (le volet A n'en lit
  aucune) ; toute affirmation publique ; tout contact avec les auteurs (je rédige, Lazar envoie) ; l'option B-bis.
