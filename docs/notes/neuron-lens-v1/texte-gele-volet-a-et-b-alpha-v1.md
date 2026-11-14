# Texte gelé — « Neuron Lens » : volet A (Qwen3-8B) et tranche B-α (Llama 3.1 8B Instruct) — v1

Préenregistrement court d'une expérience **hors du programme**, au gabarit `prereg/gabarit-preregistrement-v1.md` (R1, R2).
Il ne lance rien : **aucune ligne de GO n'est inscrite** pour ce travail ; aucune machine, aucune dépense, aucun appel de
modèle avant une ligne inscrite par la session mère sur un mot direct de Lazar **et** son feu écrit avec le numéro de ligne.

- Autrice : session fille « Neuron Lens » (deuxième fille, `session_01QPDgKfBxeeiM3BsxqJgSgf`, branche
  `prep/neuron-lens-v1`), sous la consigne de la mère `session_01QPDgKgACWyCkCN8HjqwNXy` (registre R-2685). Modèle de
  l'autrice : « modèle A ».
- Date : brouillon commencé le 2026-11-14 à 09:47 UTC (`date -u`).
- Commit de départ de la branche : `862e151932f33504d7760c47ad1e178e8a787f8f`.
- Code d'analyse : **aucun écrit à ce jour.** Code voisin épinglé : `stdlogits/neuron-lens`, commit
  `849bfe1678e28becceb1e3864afe5fc8297d02e4` (licence MIT), plus le correctif daté de `scripts/06_activations.py` écrit dans
  notre dépôt (`docs/notes/neuron-lens-v1/correctifs/`), contre-lu avant tout usage. Notre code d'analyse du volet A sera écrit
  **après** le scellement de ce texte, contre-lu, et son commit consigné au manifeste de chaque course ; il met en œuvre ce
  texte et n'en change rien (tout écart : § 9).
- Documents qui font foi :

| pièce | chemin | empreinte SHA-256 |
|---|---|---|
| consigne de la première fille | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-fille-neuron-lens-v1.md` (`main`) | `43ac1788b4b3260bad6e1c68614ab337cd4ae539aa9302ae69ba757a46de5b2e` |
| interdits communs v2 | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`main`) | `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` |
| plan et devis v1 (§§ 3, 4.2) | `docs/notes/neuron-lens-v1/plan-et-devis-v1.md` | `bc20a12aeb5cffeaa12ac264d5141036100b530f4a6a7c0998e24d1b184e3668` |
| plan et devis v2 (§§ 3, 4) | `docs/notes/neuron-lens-v1/plan-et-devis-v2.md` | `4f6534907b849cada369ac87df6fbcf87f766085c0ed56c0388bf849e4aa9c77` |
| passation reprise | `docs/notes/neuron-lens-v1/passations/2026-11-14-0933.md` | `80507f8c075e84e11f77c4994c47f17a5e56990b3dda77bd1ae75a5c66333dcb` |
| résultats publiés, lecture contre pilotage (Qwen3-8B) | `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/causal_lens_qwen3-8b.json` | `8904c4d34154068293700fbabf967f553415e6969aafebe06e29a452e03830d3` |
| résultats publiés, lectures aux activations (Qwen3-8B) | `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/reads_at_firings_qwen3-8b.json` | `ac0bf101e341385a400bbecb751f9720428da1d0bd09a752c8337dd84ba182cd` |
| code publié de la mesure (copie) | `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/scripts-checks-causal_lens.py.txt` | compagnon `.sha256` |
| constats publiés (stabilité, § 1) | `docs/findings.md` du dépôt voisin au commit `849bfe16` ; copie archivée `docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/docs-findings.md` (`main`) | `8814874b1cbe144f2cd1070ee20384b397be105c47b3e9cbeb9360a25ee5a866` |
| arbre des lentilles de Neuronpedia | `docs/sources/neuron-lens-lecture-20261113/huggingface/lentilles-neuronpedia-jacobian-lens-arbre.json` (`main`) | manifeste v2 du lecteur |
| arbre des lentilles publiées de neuron-lens | `docs/sources/neuron-lens-lecture-20261113/huggingface/lentilles-stdlogits-rs-lenses-arbre.json` (`main`) | `d2a7a076aa86ada4b6901bb02e9380f08ec2db9b8214f4346d2a6c552d999ec1` |

## 0. Portée et séparations

- **Hors programme.** Aucune hypothèse du programme (H1 à H9, HC1 à HC6, L, T, Tr) n'est testée ici ; aucun résultat de ce
  texte n'entre dans T0.7, T0.8, G0, G1 ni dans un préenregistrement du programme sans nœud de Lazar.
- **Séparation d'avec P3 et P3b** (décision de la mère, R-2685) : l'autrice n'a rien lu de P3 ni de P3b (préenregistrements,
  données, résultats, lignes de registre au-delà de leur première ligne). **Les sorties de ce texte ne servent à fixer aucun
  choix de lecture de P3b** (`GO-2026-10-20-10`), même si la famille des lentilles est la même pour Llama 3.1 8B Instruct.
  Aucune donnée réservée du programme, aucune sonde du programme n'est employée ou lue.
- **Modèles nommés** : volet A, `Qwen/Qwen3-8B` (changement de modèle permis pour ce seul volet, R-2528) ; tranche B-α,
  `meta-llama/Llama-3.1-8B-Instruct` (modèle des sondes du programme). Les étiquettes en mots du catalogue publié ont été écrites
  par un modèle de la famille Claude, noté ici « modèle C » ; elles ne servent qu'à la description (§ 3.5), jamais à un critère.
- **Antériorité** : lire un poids de sonde par projection sur le vocabulaire est une technique ancienne ; ce texte ne revendique
  rien, il mesure si l'instrument sert (plan v2 § 4, point 4).
- **Règle de lecture, écrite d'avance** : une lecture par lentille **peut ajouter un soupçon sur une sonde, jamais la blanchir**.
  « Fuite non retrouvée » se lit « l'instrument ne voit pas une fuite plantée à cette profondeur », jamais « pas de fuite ».
- **Hors de ce texte** : la tranche B-β (§ 8), l'option B-bis (étiquettes), les têtes d'attention.

## 1. Hypothèses

### Volet A — Neuron Lens tel que publié, sur Qwen3-8B, du point de vue d'un moniteur
- **A-i (audit de fuite textuelle)** : la lentille S, appliquée à la direction d'une sonde linéaire, nomme les jetons d'entrée
  dont la sonde dépend, y compris une fuite textuelle plantée, mieux qu'une lecture sans lentille et sans se réduire à ce qu'un
  sac de jetons dit déjà.
- **A-ii (neurones comme traits)** : à budget petit (k ≤ 64 neurones de la couche à portes), un détecteur sur neurones égale une
  sonde sur le flux résiduel en distribution sans perdre hors distribution.

### Tranche B-α — la lecture par la lentille R tient-elle sur Llama 3.1 8B Instruct, avec les lentilles publiques ?
- **B-2** : la lecture R (lentille R publique de Neuronpedia) de l'écriture d'un neurone prédit l'effet de son pilotage sur les
  log-probabilités, couche par couche, comme sur Qwen3-8B.
- **B-3** : cette lecture devance nettement la lentille des logits dans la première moitié du réseau.
- **B-4** (rapportée, non décisive) : écart de la lentille R publique sur les lentilles J et J++ publiques.
- **B-7** (porte la conclusion pour un moniteur, n'entre pas dans le verdict de reproduction) : la lecture R prédit mal ce
  qu'**une activation isolée** fait en contexte (ablation) avant les deux tiers de la profondeur, comme sur Qwen3-8B.

## 2. Prédictions chiffrées et signe attendu (R3 : aucune course ne vise un signe)

| mesure | prédiction écrite | réfutation |
|---|---|---|
| A-i | aucune direction prédite pour A1 et A2 ; confiance 0,3 dans « apporte quelque chose » (plan v2 § 0) | issues du § 6.1 |
| A-ii | en distribution, écart à la sonde résiduelle inférieur à 0,02 dès k = 64 ; hors distribution, aucune direction prédite | issues du § 6.2 |
| B-2, B-3 | motif publié reproduit à profondeur relative (confiance 0,55, plan v2 § 0), avec la réserve que la lentille R publique repose sur peu de documents | issues du § 6.3 |
| B-4 | signe positif attendu, petit (+0,03 à +0,13 publiés sur Qwen3-8B), non décisif | — |
| B-7 | r médian bas (< 0,25) dans la première moitié, élevé (≥ 0,50) sur les couches 26 à 29 | issues du § 6.4 |

## 3. Métriques

### 3.1 Commun au volet A
- **Modèle** : `Qwen/Qwen3-8B` (36 couches, flux de 4 096 dimensions, 12 288 neurones par couche à portes) ; révision du
  dépôt du modèle relevée et consignée au manifeste avant la course ; licence relue sur la fiche du modèle avant le
  téléchargement (Apache 2.0 attendue ; sinon arrêt, § 7).
- **Lentilles** (publiées, `stdlogits/rs-lenses`, CC BY 4.0, citation due) : R = `qwen3-8b/r-lens/lens.pt`
  (empreinte de stockage `5eaa4d56e10d0c535b5170d5aaaa1174fb8dedf0fddb2f9821cec0aa1050fae1`, sortie de la couche L → sortie de la
  dernière couche) ; S = `qwen3-8b/s-lens/out.pt` (`f87601433def8cfc403508acccadb7e62d99a5ccf51ec30e730d7c93c21d37ec`, plongements
  des jetons → sortie de la couche L). Empreintes vérifiées au téléchargement ; écart = arrêt (§ 7).
- **Couches lues** : 8, 14, 20, 26 (fixées avant toute mesure).
- **Position** : chaque invite est rendue par le gabarit de conversation du modèle (un seul tour d'utilisateur, sans invite de
  génération) ; la position lue est le **dernier jeton du contenu de l'utilisateur** (avant les marques de fin de tour). Aucune
  moyenne sur les jetons. Les lentilles ne sont ajustées qu'à partir de la position 16 (`SKIP_FIRST = 16`,
  `neuron_lens/transport.py`) : un exemple dont la position lue est < 16 est écarté et compté.
- **Vocabulaire lu** : les jetons gardés du catalogue publié (`catalog.kept`, Qwen3-8B).
- **Lectures d'une direction** :
  - lecture S d'un covecteur `w` à la couche L : score de chaque jeton `v` = `w · K_L (W_E[v] − moyenne_v W_E)` ;
  - lecture R d'un vecteur `u` du flux à la couche L : logits `W_U (γ ⊙ norm(J_L u))` ;
  - lecture **sans lentille** (témoin) : `w · (W_E[v] − moyenne_v W_E)` ;
  - **vecteur et covecteur** (plan v2 § 4, point 1) : le poids `w` d'une sonde est un covecteur ; il est lu par S. La lecture R
    porte sur la **différence des moyennes des classes** (vecteur du flux), rapportée sans critère ; la lecture R de `w` est
    rapportée à part, sans critère.
  - **Lectures centrées-réduites (`_z`)** : chaque score de jeton est centré-réduit par la moyenne et l'écart-type de ce jeton
    sur les colonnes de la couche (les neurones de la couche, comme dans `neuron_lens/readout.py`, `layer_logit_stats`, et
    `scripts/08_reads.py`, variantes `_z`). **Les lectures `_z` sont celles des critères** ; les lectures brutes sont rapportées
    à côté (les auteurs décrivent la lecture S brute comme noyée par des jetons pivots après la couche 8).
- **Sonde** : régression logistique, pénalité L2 choisie par validation croisée interne à l'apprentissage (5 plis), sur le flux
  résiduel à la sortie de la couche, traits centrés-réduits sur l'apprentissage.
- **Sac de jetons** (prédicteur sur le texte seul, dans l'esprit de N-029) : régression logistique L2 (même choix de pénalité)
  sur les comptes des jetons du contenu de l'utilisateur ; ses poids servent de référence en A2 et A3.

### 3.2 Contrastes publics (trois, fixés ici)
- **C1, nuisible contre bénin** : les 100 comportements nuisibles et les 100 bénins de JailbreakBench (MIT), appariés par
  catégorie. Hors distribution : les comportements nuisibles d'AdvBench (`llm-attacks`, MIT) **dont ceux que JailbreakBench
  indique comme tirés d'AdvBench, ou identiques après normalisation (minuscules, ponctuation retirée), sont retirés**, contre les
  bénins de JailbreakBench du jeu de test de la découpe ; nombre retenu consigné.
- **C2, fuite plantée** : les 306 énoncés vrais de `representation-engineering` (`data/facts/facts_true_false.csv`, MIT,
  empreinte du fichier `151b6163289460eb8b37f7c6a1998e23aed8e05b5e557bf1a2297079bf0e5af9` relevée le 2026-11-14 au commit
  `5455d8a375d5fb1cb191f9ebcd089b7c21e9a31e`), précédés de la consigne du gabarit publié
  (`examples/honesty/utils.py`) : « Pretend you're an honest person making statements about the world. » contre « Pretend
  you're an untruthful person making statements about the world. ». La seule différence entre classes est le mot de la consigne :
  la fuite textuelle est connue par construction. Hors distribution : même contraste avec la paraphrase écrite ici, avant toute
  course : « Imagine you are a truthful speaker stating facts about the world. » contre « Imagine you are a deceptive speaker
  stating facts about the world. ».
- **C3, vrai contre faux** : les 306 énoncés vrais contre les 306 faux du même fichier, sans consigne. Témoin où la fuite lexicale
  attendue est faible. Pas de jeu hors distribution.
- **Jetons plantés** (A1) : l'ensemble P des identifiants de jetons qui apparaissent dans la tokenisation par Qwen3-8B des six
  formes « honest », « untruthful », chacune nue, précédée d'une espace, et précédée d'une espace avec majuscule initiale, hors
  jetons de moins de trois caractères ; P est calculé et consigné avant la première passe du modèle.

### 3.3 Mesure A-i — lire la direction d'une sonde
| | métrique (par contraste, couche et découpe) |
|---|---|
| A1 (C2) | meilleur rang d'un jeton de P dans la lecture S `_z` de +w et de −w (les deux signes, rang parmi les jetons gardés) |
| A2 (C1) | précision à 20 : moyenne, sur les deux signes, de la part des 20 premiers jetons de la lecture S `_z` de ±w qui sont associés à la classe de ce signe ; un jeton est « associé » s'il apparaît dans au moins 5 invites d'apprentissage et que le test exact de Fisher de sa présence entre classes passe le taux de fausses découvertes de 5 % (Benjamini-Hochberg) ; et corrélation de rangs de Spearman entre la lecture S et les poids du sac de jetons (rapportée) |
| A3 (C1, C2) | chute d'AUROC de la sonde, sur le jeu de test, quand on retire des invites les 20 jetons de la lecture S `_z` (les 10 premiers de chaque signe) : toutes leurs occurrences sont supprimées de la suite des jetons du contenu de l'utilisateur, puis l'invite est rendue et passée de nouveau ; la sonde n'est pas réapprise |

Témoins de A1 et A2 : 100 directions aléatoires (gaussiennes, même norme que w) ; une sonde apprise sur étiquettes permutées ;
la direction de la sonde de C3 à la même couche ; la lecture sans lentille. Témoins de A3 : 20 jetons tirés au hasard parmi les
jetons gardés du même décile de fréquence d'apprentissage que chacun des 20 retirés (200 tirages) ; les 20 premiers jetons du sac
de jetons (10 par signe).

### 3.4 Mesure A-ii — des neurones comme traits
Traits : activations des neurones de la couche à portes (porte activée × montée, 12 288 par couche), mêmes couches, même
position. Détecteurs : à budget k ∈ {1, 8, 64, 512}, les k neurones de plus grand écart moyen standardisé entre classes sur
l'apprentissage, puis régression logistique L2 ; détecteur dense sur les 12 288 neurones. Comparés sur les mêmes découpes à : la
sonde résiduelle (4 096 dimensions) ; la sonde restreinte aux k premières composantes principales de l'apprentissage (budget
égal) ; k neurones tirés au hasard (20 tirages, moyenne) ; le sac de jetons. Métrique : AUROC en distribution (test de la
découpe) et hors distribution (C1, C2) ; écart apparié au détecteur de référence (sonde résiduelle) moyenné sur les 5 découpes ;
intervalle à 95 % par rééchantillonnage apparié des exemples de test (2 000 tirages, stratifiés par découpe).

### 3.5 Description jointe (sans critère)
Pour les 8 premiers neurones de chaque détecteur parcimonieux : étiquette du catalogue (modèle C) et lectures du catalogue, et
leur accord avec une liste de mots du concept fixée avant la course (aucun juge par modèle). Lecture R de ±w et de la différence
des moyennes : 20 premiers jetons par couche.

### 3.6 Commun à la tranche B-α
- **Modèle** : `meta-llama/Llama-3.1-8B-Instruct` (32 couches, 14 336 neurones par couche à portes, 4 096 dimensions) ;
  révision consignée au manifeste.
- **Chaîne** : celle du dépôt voisin au commit `849bfe16`, `06_activations.py` avec le correctif contre-lu ; `checks/causal_lens.py
  measure` avec ses défauts publiés : 32 neurones tirés par couche (`random.Random(0)`, fonction `random_neurons`), les deux pôles
  (64 pôles par couche), 16 contextes de 64 jetons, positions `[16, T)`, doses 1× et 4× l'activation typique haute du pôle
  (`act_top`), ablation en contexte sur les 8 premiers documents du pôle, fenêtre de 8 positions ; puis `score`.
- **Lentilles notées** (aucune n'entre dans `measure`) : lentille des logits (identité) ; et, de `neuronpedia/jacobian-lens`
  (licence Llama 3.1, citation due), par empreinte de stockage :
  J = `llama3.1-8b-it/jlens/Salesforce-wikitext/Llama-3.1-8B-Instruct_jacobian_lens.pt`
  (`d5300a1575c0b5ad6e01b098c75adb072f3a6c246f184ce2fb35a3550fc8c68b`) ;
  J++ = `llama3.1-8b-it/jpp/Salesforce-wikitext/Llama-3.1-8B-Instruct_jpp_lens.pt`
  (`8bd04f482aed9c85e76e71ccb510907405500512193cdfcc34f4f31722056f7c`) ;
  R publique = `llama3.1-8b-it/rlens/Salesforce-wikitext/Llama-3.1-8B-Instruct_rlens.pt`
  (`a63a1588f2cb61850c68131a5f13b74590f4fe137f67bf80c627547d2230d31c`).
  Nombre de documents d'ajustement (J : 461 ; J++ et R : 64) : **niveau citation** (note du lecteur), relu dans les
  `config.yaml` à B0 et consigné.
- **Métriques par couche et par lentille** (définitions de `score`, copie empreintée) :
  - `r_med` : r de Pearson médian, sur les 64 pôles tirés, entre la lecture de l'écriture `s·W_down[:, n]` et la cible, sur le
    vocabulaire (jetons vus au moins 5 fois dans les corpus d'activations) ;
  - `pass` (« part prédite ») : part des pôles dont le r dépasse le 99ᵉ centile des r du témoin, centile mis en commun sur les
    couches ;
  - `control_med` (**témoin**) : r médian de chaque pôle apparié à la lecture du neurone tiré suivant de la même couche.
  - Cibles : « steer 1x » pour B-2, B-3, B-4 ; « ablate win » (contribution de l'activation, à sa position et sur les 8
    suivantes) pour B-7 ; « steer 4x » et « ablate pos » rapportées sans critère.
  - Intervalles : rééchantillonnage des 64 pôles par couche (2 000 tirages), rapportés ; **les verdicts portent sur les valeurs
    ponctuelles**, comme les valeurs publiées.
- **Profondeur relative** : les seuils ci-dessous sont déjà exprimés en couches de Llama (32) à partir des valeurs publiées de
  Qwen3-8B (36) à la même profondeur relative, à environ 0,8 fois la valeur publiée (plan v1 § 4.2).

## 4. Seuils (fixés avant toute lecture ; aucun résultat n'existe)

### 4.1 Volet A
- **A1 « retrouvée »** : un jeton de P parmi les 10 premiers (l'un ou l'autre signe) à au moins 2 des 4 couches, et dans 0 des 100
  directions aléatoires à ces couches (moins de 1 %) ; **« non retrouvée »** : à aucune couche ; sinon « partielle ». Une couche
  compte si la condition tient dans au moins 3 des 5 découpes.
- **A2 « nomme »** : précision à 20 ≥ 0,25 et au-dessus du 99ᵉ centile des directions aléatoires, à au moins 2 couches (même
  règle des 3 découpes sur 5).
- **A3 « dépendance lue »** : chute au-dessus du 95ᵉ centile des 200 tirages aléatoires **et** ≥ la moitié de la chute obtenue
  avec les jetons du sac de jetons, à au moins 2 couches (moyenne des 5 découpes), par contraste.
- **« S fait mieux que sans lentille »** : à au moins 2 couches, meilleur rang strictement plus petit en A1, ou précision à 20
  strictement plus grande en A2 (moyennes des 5 découpes).
- **A-ii « apporte »**, par contraste : il existe k ≤ 64 tel que, à au moins 2 des 4 couches, l'AUROC en distribution du
  détecteur sur neurones est ≥ AUROC de la sonde résiduelle − 0,02 **et** l'intervalle à 95 % de l'écart hors distribution
  (neurones − sonde) contient 0 ou lui est entièrement favorable (C3 : condition en distribution seule). **« N'apporte rien »** :
  la sonde résiduelle gagne de plus de 0,05 à tout k ≤ 512, à chaque couche, en distribution et hors distribution.
- Exemples écartés (position < 16) : plus de 5 % d'un contraste = arrêt (§ 7).

### 4.2 Tranche B-α (lentille R publique, sauf mention)
Précision ajoutée par ce texte (le plan disait « sur les couches a à b » sans dire « à chaque couche » ou « en majorité ») :
**« reproduit » exige la condition à chaque couche de la bande ; « non reproduit » est atteint si la condition contraire tient à
au moins la moitié des couches de la bande.**

| mesure | « reproduit » | « non reproduit » |
|---|---|---|
| B-2 (steer 1x) | `r_med` ≥ 0,40 à chaque couche 8 à 15, ≥ 0,60 à chaque couche 16 à 23, ≥ 0,85 à chaque couche 24 à 27 ; `pass` ≥ 0,90 à chaque couche 8 à 27 ; témoin : `control_med` entre −0,05 et +0,05 à chaque couche 0 à 27 | `pass` < 0,50 à au moins 6 des 12 couches 16 à 27, ou `r_med` < 0,30 à au moins 4 des 8 couches 16 à 23 |
| B-3 (steer 1x) | `r_med`(R) − `r_med`(logits) ≥ +0,20 à chaque couche 4 à 15 | écart ≤ 0 à au moins 6 des 12 couches 4 à 15 |
| B-4 | rapportée : `r_med`(R) − `r_med`(J) et − `r_med`(J++), couches 4 à 23, signe et taille ; **non décisive** | — |
| B-7 (ablate win) | `r_med` < 0,25 à chaque couche 0 à 15 **et** ≥ 0,50 à chaque couche 26 à 29 | `r_med` ≥ 0,40 à au moins 4 des 8 couches 8 à 15 (audit R4 avant de s'en réjouir), ou < 0,30 à au moins 2 des 4 couches 26 à 29 |

**Chaîne en défaut** (aucun verdict de mesure, § 7) : `control_med` hors de ±0,10 à une couche quelconque de 0 à 27, pour
n'importe quelle lentille ; ou cas sain interne manqué : lentille des logits, `r_med` (steer 1x) < 0,80 à l'une des couches 28 à
30 (valeurs publiées sur Qwen3-8B à la même profondeur : 0,94 à 0,96) ; ou essai miniature de B0 en échec (§ 7).
Les couches 28 à 31 ne comptent pour aucun verdict de B-2 ni B-3 : toute lentille y approche r = 1 (0,9998 pour la lentille des
logits à la dernière couche de Qwen3-8B).

## 5. Plan d'analyse

### 5.1 Volet A
- **Données** : C1 (200 en distribution ; hors distribution : AdvBench dédoublonné contre bénins de test), C2 (612 en
  distribution, 612 hors distribution), C3 (612). Taille fixée par les jeux publics, sans arrêt optionnel.
- **Découpes** : 5 découpes apprentissage/test 70/30, stratifiées par classe et **groupées** : C1 par paire de JailbreakBench
  (comportement nuisible et bénin de même catégorie et rang), C2 par énoncé (les deux consignes d'un même énoncé du même côté),
  C3 par ligne. Les jeux hors distribution ne servent jamais à l'apprentissage ni au choix d'un hyperparamètre.
- **Graines (R9)** : `numpy.random.SeedSequence(entropy=20261114)`, puis `spawn` dans cet ordre fixe : contraste (C1, C2, C3) →
  découpe (5) → tâche (directions aléatoires, permutation, tirages de A3, neurones aléatoires, rééchantillonnage) ; numpy ≥ 1.25 ;
  graines dérivées consignées au manifeste de la course avec configuration et empreinte, versions, commit.
- **Comparaisons multiples** : les critères sont des règles de décision fixes, pas des tests ; aucune correction au-delà du taux de
  fausses découvertes de A2. Les 4 couches × 3 contrastes × 4 budgets sont tous rapportés, sans sélection.
- **Rapport** : chaque valeur renvoie à un fichier brut scellé ; toutes les cases des tableaux, y compris les contrastes et couches
  qui ne passent pas.

### 5.2 Tranche B-α
- **Étapes** : B0 (montage ; essais de l'estimateur du dépôt ; essai Llama miniature aléatoire contre la force brute ; lecture
  d'un fichier de Neuronpedia et vérification de son format et de son empreinte) → corpus d'activations et comptes de jetons →
  passe d'activations avec le correctif contre-lu → `causal_lens.py measure` (défauts publiés, § 3.6) → `score` pour les quatre
  lentilles → scellement des sorties brutes, destruction de la machine par son identifiant.
- **Graines** : celles du dépôt voisin (`random.Random(0)` pour les neurones) ; toute autre graine dérivée par `SeedSequence`
  (`entropy=20261114`, branche « B-α ») et consignée. Seconde graine de neurones (1) seulement pour l'audit R4.
- **Rapport** : les quatre cibles × quatre lentilles × 32 couches, valeurs et intervalles ; B-2 et B-3 avec la lentille R
  publique ; les mêmes métriques pour J et J++ rapportées.

## 6. Critères de lecture gelés

### 6.1 Volet A, mesure (i)
Ordre de priorité : chaîne en défaut > « n'apporte rien » > « apporte » > « indéterminé ».

| issue observée | verdict |
|---|---|
| cas sain manqué (§ 6.5) | **chaîne en défaut** : aucun verdict |
| A1 non retrouvée ; **ou** sans lentille ≥ S à chaque couche sur A1 et A2 ; **ou** A3 : chute < moitié de celle du sac de jetons à chaque couche, en C1 et en C2 | **n'apporte rien** à un moniteur |
| A1 retrouvée **et** S fait mieux que sans lentille sur A1 ou A2 (et aucune condition de la ligne précédente) | **apporte quelque chose** |
| tout autre cas (A1 partielle, etc.) | **indéterminé**, mesure par mesure |

### 6.2 Volet A, mesure (ii) — par contraste, sans agrégation
| issue | verdict |
|---|---|
| condition « apporte » du § 4.1 | **apporte** (pour ce contraste) |
| condition « n'apporte rien » du § 4.1 | **n'apporte rien** (pour ce contraste) |
| ni l'une ni l'autre | **indéterminé** |

### 6.3 Tranche B-α, reproduction
| issue | verdict |
|---|---|
| chaîne en défaut (§ 4.2) | **chaîne en défaut** : aucun verdict ; passage à B-β suspendu (plan v2 § 3.2) |
| B-2 et B-3 « reproduit » | **reproduit avec la lentille R publique** |
| B-2 ou B-3 « non reproduit » | **non reproduit avec la lentille R publique** — **ne conclut pas sur la chaîne** (lentille de peu de documents, autre corpus, autre code) ; c'est B-β qui tranche ; ne bloque pas B-β |
| autre | **partiel**, mesure par mesure |

Ce qu'un « reproduit » permettra de dire, et pas plus : la lentille lit ce qu'une direction **pousse en moyenne** ; pas qu'elle
nomme le concept d'une invite donnée (banc public cité par le lecteur : 31 % à 53 % sur ce modèle, niveau citation).

### 6.4 Tranche B-α, B-7 (conclusion pour un moniteur)
| issue | lecture |
|---|---|
| « reproduit » | là où `r_med` est bas, une étiquette de neurone décrit une poussée moyenne et **ne peut pas servir à lire un épisode** ; un moniteur ne s'y fie pas avant les couches où B-7 dépasse 0,50 |
| « non reproduit » par le haut (≥ 0,40 tôt) | audit R4 (§ 6.5) avant toute lecture ; si l'audit tient : la lecture vaudrait en contexte plus tôt que publié, rapporté comme tel |
| « non reproduit » par le bas (< 0,30 tard) | la lecture ne dit pas ce qu'une activation fait, même tard : rapporté |
| autre | rapporté couche par couche |

### 6.5 Audit symétrique (R4), déclenché des deux côtés
- **Volet A, trop beau** : A1 réussie à toutes les couches avec un rang 1, ou neurones égaux à la sonde partout → vérifier que la
  lecture ne voit pas les étiquettes (direction permutée), que le retrait de jetons change bien le texte, relancer sur une sixième
  découpe (graine suivante de la `SeedSequence`) ; le verdict attend l'audit.
- **Volet A, tout échoue** : vérifier la chaîne sur le pôle publié `L8 n344 +` du README voisin (lecture R de son écriture
  publiée : « owl, noct, bedtime, night ») : notre lecture R doit placer un jeton de la famille « owl » parmi ses 10 premiers ;
  sinon **chaîne en défaut**, pas « n'apporte rien ».
- **B-α, trop beau** : `r_med` ≥ 0,95 à une couche 0 à 7, ou `control_med` exactement 0 → vérifier que le témoin apparie bien un
  autre neurone, que le pilotage change les log-probabilités (norme non nulle), relancer `measure` avec la graine de neurones 1 ;
  le verdict attend l'audit.
- **B-α, tout échoue** : rejouer `score` sur les sorties de `measure` publiées pour Qwen3-8B si elles sont disponibles (cas sain) ;
  sinon `measure` sur Qwen3-8B, couches 8 et 20 seulement, dans le plafond ; si le cas sain ne retrouve pas les valeurs publiées
  à ±0,05, **chaîne en défaut**.

## 7. Liste d'arrêt

| condition | action |
|---|---|
| pas de ligne de GO inscrite par la mère sur un mot de Lazar, ou pas de feu écrit avec le numéro de ligne | rien ne part |
| correctif de `06_activations.py` non contre-lu, ou ce texte non scellé | rien ne part (R1, R2) |
| empreinte d'un fichier de lentille ou de données différente de celle écrite ici | arrêt ; message à la mère |
| licence d'un modèle ou d'un jeu différente de celle relevée | arrêt ; message à la mère |
| B0 : écart de l'estimateur à la force brute sur le Llama miniature supérieur à celui obtenu sur le Qwen3 miniature par les essais du dépôt | arrêt de B-α : **chaîne en défaut** ; message à la mère |
| format d'un fichier de Neuronpedia illisible par `load_lens` | lecture directe du fichier (une application 4 096 × 4 096 par couche) écrite comme écart daté (§ 9) avant usage ; sinon arrêt |
| plus de 5 % d'exemples écartés (position < 16) dans un contraste | arrêt du volet A ; message |
| dépense à 60 % du plafond de la ligne ou de la tranche | compte rendu à la mère ; à 90 % arrêt dur |
| minuterie de destruction par identifiant non posée à la création de la machine | la machine est détruite par son identifiant avant toute passe (R10) |
| refus d'un contrôle de permission ou d'un classifieur | arrêt sur ce point, rapport tel quel ; ni contournement, ni reformulation, ni transfert |
| toute envie d'écart à ce texte | écrit et daté avant d'être fait, nouvelle version (R12), contre-lu ; sinon interdit |
| toute lecture qui toucherait P3, P3b, T0.6, T0.7, P3-bis ou un chemin interdit | interdit ; arrêt |

**R5** : chaque garde ci-dessus qui est du code (empreintes, écart à la force brute, part d'exemples écartés, plafond) est essayée
sur un cas sain et sur un artefact (fichier altéré d'un octet ; écart forcé ; jeu tronqué ; dépense simulée) avant la course, et le
résultat de l'essai est consigné ; aucun repli silencieux.

## 8. Hors de ce texte : tranche B-β (à geler dans un texte séparé avant β)

B-1 (stabilité), B-5 (côté entrée), B-6 (deux codes), et B-2, B-3, B-4, B-7 relues avec **notre** lentille R. Deux faits relevés
pour ce futur texte, sans rien geler :
- **Chiffres de stabilité relus (R7)** dans `docs/findings.md` du dépôt voisin (`8814874b…`, § 1, lignes 49 à 62) : différence
  entre moitiés de la lentille R 0,04 à 0,06 (couches 0 à 18), 0,03 (19 à 22), 0,02 (23 à 27), 0,01 ou moins dès 28 ; lentille S
  0,00 à 0,05 (`mid`) et 0,01 à 0,05 (`out`) ; même premier jeton entre moitiés pour 0,89 à 0,99 des neurones aux six couches
  tabulées (2, 8, 14, 20, 26, 32 ; mesure de `checks/lens_compare.py`, dite sur 12 couches). Les fourchettes du plan v1 (« ≤ 6 % »,
  « 89 à 99 % ») sont donc **opposables** à ce niveau.
- **Critère B-5 du plan v1 mal posé** : « `read_S` ≥ 0,60 à la couche 0 **et décroissant sur le premier quart** ». La référence
  publiée elle-même n'est pas décroissante (`read_S` = 0,848, 0,248, 0,090, 0,229, 0,352 aux couches 0 à 4,
  `reads_at_firings_qwen3-8b.json`) : le critère serait manqué par l'original. À réécrire dans le texte de B-β.

## 9. Écarts au plan v1 et v2, écrits ici avant toute course

1. **Consigne de C2** : le gabarit publié dit « an honest » contre « **an untruthful** », pas « dishonest » (plan v1 § 3.2) ; P est
   donc formé de « honest » et « untruthful ». La paraphrase hors distribution (« truthful » / « deceptive ») est écrite au § 3.2.
2. **Position** : « dernier jeton de l'invite » (plan v1) précisé en « dernier jeton du contenu de l'utilisateur » (le dernier
   jeton du gabarit est une marque de fin de tour, sans contenu).
3. **Bandes de couches** : « reproduit » à chaque couche, « non reproduit » à la moitié au moins (§ 4.2) ; le plan ne le disait pas.
4. **A1, A2, A3** : règle « 3 découpes sur 5 » et « au moins 2 couches » pour A3 ; témoins de A3 appariés par décile de fréquence ;
   ordre de priorité des issues de (i) ; détecteurs parcimonieux de A-ii par écart moyen standardisé ; agrégation de A-ii par
   contraste seulement.
5. **Découpes groupées** (C1 par paire, C2 par énoncé) et **dédoublonnage** d'AdvBench contre JailbreakBench.
6. **Cas sain interne de B-α** (lentille des logits, couches 28 à 30) ajouté à « chaîne en défaut ».
7. **B-3** : écart publié relu à +0,352 à +0,425 (couches 4 à 17, `causal_lens_qwen3-8b.json`) ; le plan v1 écrivait +0,35 à
  +0,42 ; seuil inchangé.
8. Tout écart ultérieur suit la liste d'arrêt (§ 7).

## 10. Provenance des chiffres de ce texte (R6, R7)

| chiffre | source | clé |
|---|---|---|
| B-2 publié : `r_med` R 0,33 (couche 0), 0,45 (4), 0,49 (8), 0,65 (12), 0,74 (16), 0,87 (20), 0,95 (24) ; `pass` ≥ 0,9375 dès la couche 5 ; témoin −0,038 à +0,031 | `causal_lens_qwen3-8b.json` (`8904c4d3…`) | `targets["steer 1x"]["R:dclm"]` |
| B-3 publié : écart R − logits +0,352 à +0,425 (couches 4 à 17) ; couche 8 : 0,49 contre 0,12 | idem | `["steer 1x"]["R:dclm"|"logit"]["r_med"]` |
| B-4 publié : écart R − J +0,026 à +0,131 (couches 4 à 23) | idem | `["steer 1x"]["R:dclm"|"J"]["r_med"]` |
| B-7 publié : `r_med` 0,05 (0), 0,05 (4), 0,08 (8), 0,08 (12), 0,13 (16), 0,23 (20), 0,40 (24), 0,67 (28), 0,87 (32) ; témoin −0,013 à +0,029 | idem | `["ablate win"]["R:dclm"]` |
| cas sain interne : lentille des logits 0,94 à 0,96 (couches 31 à 33 de Qwen3-8B) ; 0,9998 à la dernière couche | idem | `["steer 1x"]["logit"]["r_med"]` |
| `read_S` 0,848 (couche 0), puis 0,248, 0,090, 0,229, 0,352 | `reads_at_firings_qwen3-8b.json` (`ac0bf101…`) | `["neurons"]["layers"][i]["read_S"]` |
| stabilité (§ 8) | `docs/findings.md` voisin (`8814874b…`), lignes 49 à 62 | — |
| défauts de `measure` et définition de `pass` | `scripts-checks-causal_lens.py.txt` (lignes 1 à 61, 66 à 76, 325, 373 à 377) | — |
| consigne de C2 | `representation-engineering`, `examples/honesty/utils.py`, ligne 33 et 45-46, commit `5455d8a3…` | — |
| 31 % à 53 % (banc de concepts), 461 et 64 documents | note du lecteur `docs/notes/lecture-voisin-neuron-lens-v1.md` (`12c8f673…`) | **niveau citation, non opposable** |

Valeurs recalculées par l'autrice le 2026-11-14 vers 09:45 UTC sur les fichiers ci-dessus (empreintes vérifiées par
`sha256sum -c` sur les compagnons).

## 11. Contre-lecture (R2)

À remplir après la contre-lecture : sous-agent neuf d'un autre modèle que l'autrice (« modèle B »), qui ne l'a pas écrit ;
empreinte du brouillon relu ; chemin et empreinte de son rapport ; traitement de chaque remarque.
