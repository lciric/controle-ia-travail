# Lentille jacobienne contre lentille des logits sur les directions des sondes de P3 — note de faisabilité v1

29 octobre 2026, sur le « yes go » de Lazar (08:26, heure de Paris) : comparaison avec le code publié d'Anthropic,
processeur seul, sans dépense. **Exploratoire, non préenregistré, non opposable.** Aucun résultat réel n'a été produit
ni lu ici.

## Verdict

Côté code, c'est exécutable : le script est écrit et passe un essai factice de bout en bout (25 contrôles sur 25).
Côté entrées, il manque trois choses, et aucune n'est accessible d'ici :
1. **le fichier de lentille pour Llama-3.1-8B-Instruct.** Le dépôt d'Anthropic n'en cite aucun (il ne cite que des lentilles
   Qwen). Je ne peux pas vérifier d'ici qu'il existe, parce que HuggingFace et Neuronpedia sont refusés par le mandataire ;
2. **les poids de désembedding, la normalisation finale et le tokeniseur du modèle.** Ils se trouvent avec le modèle,
   sur une instance ;
3. **les poids des sondes** (`donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz`). D'après la procédure de
   récupération de P3, ils sont dans le dépôt, mais je n'ai pas le droit de lire `donnees/` et je n'ai donc pas vérifié.

`sondes-figees.json` ne porte **aucun poids** : seulement les noms, les couches, les familles et les empreintes.

## 1. Le dépôt `anthropics/jacobian-lens`

Clone : commit `581d398613e5602a5af361e1c34d3a92ea82ba8e` (« Initial release »), dans
`/tmp/claude-0/-home-claude/be74bc5f-030c-58ad-8f83-cdf5edf47ca3/scratchpad/jlens/depot/`. Je l'ai lu et je n'ai rien
exécuté (torch est absent ici). Le README renvoie au papier sur `transformer-circuits.pub/2026/workspace` ; le numéro
arXiv 2607.15495 vient du brief et je ne l'ai pas vérifié.

- **Ce que prend la lentille** (`jlens/lens.py`, `jlens/hf.py`). L'activation de la couche l est **la sortie du bloc l**
  (indice à partir de 0), capturée par un crochet avant sur `model.model.layers[l]`, donc avant la normalisation
  finale. Le transport s'écrit `residual @ J_l.T`, soit J_l·h. Le décodage est `lm_head(norm(x))`, plus un écrêtage
  doux si la configuration en déclare un (ce n'est pas le cas de Llama). La couche cible par défaut est la dernière,
  c'est-à-dire la sortie du bloc 31 avant la normalisation.
- **Forme du fichier.** C'est un `torch.save` d'un dictionnaire `{"J": {couche: Tensor[d, d]}, "n_prompts", "source_layers",
  "d_model"}`, en demi-précision, relu par `torch.load(weights_only=True)`. Pour Llama-3.1-8B-Instruct, d = 4096.
  Une couche pèse 4096² × 2 octets ≈ 33,6 Mo ; les 31 couches sources (0 à 30) font ≈ 1,04 Go ; nos trois
  couches seules font ≈ 101 Mo.
- **Ajustement** (`jlens/fitting.py`). Pour chaque texte, une passe avant puis ⌈d / dim_batch⌉ passes arrière. Le
  vecteur unitaire de rétropropagation est posé à toutes les positions cibles à la fois, ce qui revient à sommer sur
  les positions futures. On fait ensuite la moyenne sur les positions sources, en excluant les 16 premières et la
  dernière. D'après le README, les lentilles du papier sont ajustées sur 1 000 textes de 128 jetons d'un corpus
  proche du préentraînement (le carnet utilise WikiText-103), et environ 100 textes donnent déjà une lentille
  utilisable.
- **Lentilles publiées.** Le carnet `walkthrough.ipynb` charge `neuronpedia/jacobian-lens`, révision `qwen-n1000`,
  fichiers `qwen3.5-4b/…/Qwen3.5-4B_jacobian_lens_n1000.pt` et `qwen3.6-27b/…`. **Rien n'y concerne Llama.** Une
  lentille Llama-3.1-8B-Instruct « annoncée sur Neuronpedia » reste donc à constater. Si elle existe, il faudra aussi
  vérifier qu'elle a été ajustée sur **Instruct** et non sur le modèle de base, à la révision `0e9e39f2…` du
  manifeste de P3, qu'elle porte les couches 7, 15 et 23, et relever `n_prompts`.
- **Licences.** Le code et les jeux de consignes sont sous Apache 2.0. La licence des fichiers de lentille hébergés
  m'est inconnue (le dépôt du Hub est inaccessible). Les poids du modèle relèvent de la licence communautaire de
  Llama 3.1, qui exige un accès accepté sur HuggingFace. Une lentille est dérivée des poids : sa licence est à lire
  avant toute redistribution.
- **Appliquer la lentille à une direction : c'est légitime.**
  - La lentille est **linéaire jusqu'à la normalisation finale** : J_l·w. La normalisation RMS n'est pas linéaire,
    mais pour un vecteur seul elle ne multiplie que par un facteur positif (au ε près). Le classement des jetons est
    donc celui de W_U·(g ⊙ J_l·w) : il ne dépend pas de l'échelle de w, et −w donne exactement les logits opposés
    (`lm_head` n'a pas de biais).
  - L'argument de fond : J_l est la **dérivée moyenne** de la sortie par rapport à la couche l. J_l·w est donc l'effet
    moyen, au premier ordre, d'un ajout de w à la couche l sur le flux final. C'est exactement « ce que cette
    direction pousserait le modèle à dire ». La somme sur les positions futures change l'échelle et ne change pas
    le classement.
  - **Réserve 1 : vecteur ou forme de lecture.** Pour la différence de moyennes (w = m₊ − m₋), w est un vrai
    déplacement dans l'espace des activations, et la lecture est la plus propre. Pour les sondes apprises (familles
    `lineaire` et `attention`), w est une **forme de lecture** (w = w′/s, la normalisation est repliée). Le lire comme
    un vecteur répond à la question « que dirait-on si l'on poussait le long de ce que la sonde lit ? », pas à « que
    contient la représentation ? ». On le voit sur l'identité exacte logit_t = (J_lᵀ(g ⊙ W_U[t]))·w : la lentille
    jacobienne de w est le produit scalaire euclidien de w avec la forme de lecture du jeton t, un choix de métrique
    arbitraire. Le motif d'activation a = Σ·w (Haufe et al., cité de mémoire et non vérifié) corrige cela, mais il
    demande la covariance des activations. C'est la variante facultative `--covariances` du script ; je n'ai pas les
    covariances ici.
  - **Réserve 2 : la normalisation autour d'une activation réelle.** Autour d'une activation, la normalisation
    redevient non linéaire : la composante parallèle à J·h̄ s'efface. La variante `--activations-moyennes` lit
    lentille(h̄ + α‖h̄‖ŵ) − lentille(h̄ − α‖h̄‖ŵ). Elle demande les activations moyennes par couche, que je n'ai pas
    non plus.

## 2. `sondes-figees.json` (run `20261019-230011-p3-reel`)

Le sceau est vérifié (`sha256sum -c` : OK, `fb418127…`).
- **430 entrées** de six champs chacune (`agregation`, `classe`, `couche`, `empreinte`, `famille`, `nom`) :
  - 30 sondes : 2 concepts (tromperie, enjeux) × 5 familles (différence de moyennes, linéaire, perceptron, attention,
    Mahalanobis) × couches 7, 15 et 23 ;
  - 400 sondes « plancher » : 200 par sonde principale, toutes à la couche 15, de classe `SondeLineaireJetons` et de
    famille `plancher`. Ce sont des directions aléatoires appariées en covariance (w = L·z avec LLᵀ = Σ des jetons
    d'entraînement, b = −w·μ ; `sondes/evaluation.py::plancher_apparie`).
- **Sondes principales** : `tromperie-difference_moyennes-c15` et `enjeux-lineaire-c15`, toutes deux
  `SondeLineaireJetons`, donc de vraies directions.
- **Pas de poids dans le JSON.** Ils sont dans `donnees/<run>/sondes-figees-legeres.npz`, attendu à `701f73bd…`
  (`sondes_legeres_sha256`) : le fichier complet sans les matrices de Mahalanobis. Le fichier complet
  `sondes-figees.npz` (`91b61c45…`) n'a été rapatrié que par son empreinte : la liste blanche de
  `recuperation_p3_v1.sh` ne prend que le `.sha256`. Le format suit `premier_test_ia/figees.py` : la clé `index`
  contient un JSON en octets (classe, nom, couche, agrégation, famille, biais b, empreinte, liste des tableaux), et
  les tableaux `s<k>_w`, `s<k>_q`, etc. sont en double précision.
- **Normalisation** (`sondes/familles.py`) :
  - familles `lineaire` et `attention` : entrées centrées et réduites par dimension sur **tous les jetons
    d'entraînement des deux classes**, puis normalisation repliée (w = w′/s, b = b′ − μ·w). La sonde lit les
    activations brutes (couche de sortie du bloc, en simple précision, convertie depuis bfloat16) ;
  - `difference_moyennes` : w = m₊ − m₋ et b = −w·(m₊ + m₋)/2, sans normalisation ;
  - perceptron : `mu`, `s`, `W`, `c`, `v` (pas une direction : non traité) ;
  - Mahalanobis : `mu`, `P` (pas une direction, et absente du fichier léger).
- **Dimension** : elle ne figure pas dans le JSON. Elle vaut 4096 par le modèle, et le script refuse toute largeur
  discordante.
- **Correspondance des couches** : P3 définit la couche ℓ comme la sortie du bloc ℓ, avant la normalisation finale
  (`harnais/activations.py`), au même point d'accroche que `jlens`. Les couches 7, 15 et 23 de P3 sont donc les
  couches 7, 15 et 23 de la lentille, sans décalage.
- **Extraire w et b** : `index["sondes"][k]` donne le nom et b, et `s<k>_w` donne w. L'empreinte de chaque sonde se
  recalcule comme `sha256(f"{famille}:{nom}/{couche}/{agrégation}" + octets de w, [b], q)`, et le script la compare
  à celle du JSON.

## 3. Le script `comparaison_jlens_logitlens_sondes_p3_v1.py`

Il est en numpy seul. Torch ne sert qu'à lire une lentille `.pt`, ou à la convertir par la sous-commande
`convertir-lentille` (à lancer sur l'instance).
- **Entrées** :
  - le JSON des sondes, dont le sceau est exigé ;
  - le `.npz` des poids, contrôlé contre `sondes_legeres_sha256`, avec l'empreinte de chaque sonde recalculée ;
  - la lentille, en `.npz` (`J_<couche>`) ou en `.pt` ;
  - `lm_head.weight` et `model.norm.weight`, donnés en `npy`, `npz:clé`, `safetensors:nom` ou
    `model.safetensors.index.json:nom` (le fragment est résolu par `weight_map` ; le bfloat16 est lu en numpy) ;
  - `tokenizer.json` (décodage par octets du type GPT-2), ou une liste de jetons ;
  - en option, la liste de mots des concepts (proposition `concepts-sondes-p3-v1.json`, figée avant toute sortie
    réelle).
- **Sondes retenues** : par défaut, la famille de chaque sonde principale aux trois couches (6 sondes). L'option
  `--sondes toutes-lineaires` les étend aux 18 sondes linéaires.
- **Sortie JSON**, pour chaque sonde, chaque lentille et chaque signe (+ vers la classe 1, − vers la classe 0) :
  - les 20 jetons de tête, bruts et restreints aux « mots » (même règle que `jlens/vis.py`) ;
  - les recouvrements entre lentilles (intersection, Jaccard, jetons communs) et le cosinus des logits centrés ;
  - la cohérence avec **chaque** concept (l'autre concept sert de contrôle de spécificité) : jetons du concept dans
    la tête, meilleur rang, et score z = (moyenne des logits du concept − moyenne du vocabulaire) / écart type ;
  - p empiriques de ce score contre deux références nulles passées par la même lentille : les 200 planchers de P3
    (à la couche 15 seulement) et 200 directions isotropes par couche, tirées par `numpy.random.SeedSequence`
    (graine 20261029, clé dérivée de l'étiquette) ;
  - diagnostics : ‖J·w‖/‖w‖ et cos(w, J·w).
- **Manifeste écrit par le script** : empreintes et tailles de chaque entrée, versions, commande, graines, empreinte
  de la sortie. La sortie et le manifeste reçoivent une empreinte compagnon. Le script refuse d'écraser (R12).
- **Refus nommés** (code 2) : `entree-absente`, `sceau-absent`/`sceau-faux`, `empreinte-sondes-npz`,
  `empreinte-sonde`, `sonde-introuvable`, `principale-non-lineaire`, `couche-absente-lentille`, `dimension`,
  `poids-introuvables`, `torch-absent-pour-pt`, `sortie-existe`, `incoherence-interne` (le score z calculé par la
  matrice de Gram et le score calculé directement doivent concorder).
- **Essai factice** (`essai_factice_comparaison_jlens_v1.py`, dans `essai-factice-v1/`) : largeur 64, vocabulaire
  500.
  - Le fichier de poids des sondes est écrit **par `ecrire_sondes` du dépôt**, extrait par l'arbre syntaxique, puis
    relu par `lire_sondes` du dépôt.
  - Trois signaux sont plantés : sous J (seule la lentille jacobienne le voit), dans l'espace de sortie (seule la
    lentille des logits le voit), et avec J ≈ identité (accord 18/20, cosinus 0,97). La couche 7 aléatoire ne sort
    rien.
  - Les sept refus sont provoqués, et le déterminisme est vérifié octet pour octet.
  - Bilan : **25/25** (`essai-factice-v1/journal-essai-factice-v1.txt`).

## 4. Ce qui manque, et ce que coûte l'exécution réelle

| Pièce | État | Où |
|---|---|---|
| Poids des sondes (`sondes-figees-legeres.npz`) | probablement présent, non vérifié (lecture interdite ici) | `donnees/20261019-230011-p3-reel/` |
| Lentille Llama-3.1-8B-Instruct | **inconnue** : absente du dépôt, Hub et Neuronpedia refusés d'ici | à constater par une session qui a le réseau |
| `lm_head.weight` [128256, 4096] en bfloat16 (≈ 1,05 Go), `model.norm.weight` [4096], `tokenizer.json` | indisponibles ici | avec le modèle (accès HuggingFace soumis à licence, jeton requis) |
| Covariances et activations moyennes (variantes) | absentes | il faudrait une passe avant sur les données génériques de P3 |

- **Si la lentille ajustée existe** : aucune carte graphique n'est nécessaire. Le calcul revient à une
  multiplication matrice-vecteur par sonde, plus la matrice de Gram du désembedding : ≈ 45 s mesurées par
  extrapolation sur ce processeur, en double précision. Il faut environ 5 Go de mémoire vive. Les fichiers utiles
  font ≈ 1,2 Go de modèle (le fragment qui porte `lm_head`, résolu par l'index) plus 0,1 à 1 Go de lentille.
  N'importe quelle machine à processeur suffit.
- **Si elle n'existe pas, il faut l'ajuster** (carte graphique, donc dépense).
  - Coût par texte : ≈ 4096 rétropropagations d'une séquence de 128 jetons, soit environ 2 à 4 × 10¹² opérations
    chacune, donc ≈ 1 à 1,6 × 10¹⁶ par texte.
  - Avec 100 textes (« utilisable » selon le README) : de l'ordre d'**une heure** de carte de la classe H100.
  - Avec 1 000 textes (comme le papier) : de l'ordre d'**une dizaine d'heures**.
  - Ces ordres de grandeur sont de mémoire et non vérifiés. Le README avertit que l'implémentation n'est pas
    optimisée. À chiffrer par un essai chronométré sur 2 textes, puis devis.
  - Se limiter aux couches 7, 15 et 23 ne réduit le graphe retenu que d'environ un quart (il commence à la
    couche 7).

## 5. Réserve de méthode

- D'après le brief et le dossier `data/evaluations/` du dépôt, la lentille n'est évaluée que sur des cibles à **un
  jeton** : rang minimal sur des synonymes à un jeton, mot de concept unique. Je n'ai pas vérifié le papier
  lui-même (R7).
- « Tromperie » et « enjeux élevés » peuvent ne pas s'écrire en un mot. Un résultat « pas de mot cohérent » est donc
  **une information, pas un échec**. Il est compatible avec une direction réelle mais non verbalisable, ou avec une
  sonde qui lit autre chose (le style, l'évidence textuelle : ce sont les contre-indices déjà cités par le
  préenregistrement de P3).
- Seule la couche 15 a des planchers. Aux couches 7 et 23, la seule référence nulle est l'isotrope, plus faible : une
  direction appariée en covariance tombe dans les directions de forte variance, que l'isotrope ne reproduit pas.
- La « bande d'espace de travail » du papier, c'est-à-dire les couches médianes où se lit le contenu, n'est pas
  connue pour Llama-3.1-8B-Instruct. On peut attendre de la couche 7 qu'elle soit en dehors.
- La liste de mots des concepts est un choix d'analyse. Elle est figée dans
  `concepts-sondes-p3-v1.json` avant toute lecture ; toute retouche fera une v2, et il faudra le dire.

## 6. Proposition d'exécution

L'instance de P3 (56799469) est détruite.
1. **Une session qui a le réseau et le jeton HuggingFace (session-depot)** constate l'existence de la lentille Llama
   (révision, modèle Instruct, couches, `n_prompts`, licence, taille).
2. **Si elle existe** : la même session exécute le script sur une machine qui a, ou télécharge, les fichiers du modèle
   à la révision `0e9e39f249a16976918f6564b8830bc894c89659`. Ce peut être l'instance déjà en marche pour d'autres
   travaux, sans dépense nouvelle, ou une machine à processeur seul. La lentille est d'abord convertie en `.npz`
   (`convertir-lentille --couches 7 15 23`). La commande est scellée avant le lancement (copie de la ligne
   d'« Usage » du script avec les chemins réels) ; la sortie, le manifeste et leurs empreintes sont versés tels quels.
3. **Si elle n'existe pas** : devis d'ajustement (essai chronométré, puis 100 ou 1 000 textes), soumis à Lazar comme
   dépense. C'est un nœud, rien n'est lancé.
4. **Lecture** : descriptive, sans critère de porte. Si la lecture doit peser sur une revendication, il faut d'abord
   un préenregistrement (R1).
