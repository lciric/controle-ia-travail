# Texte gelé — « Neuron Lens » : volet A (Qwen3-8B) et tranche B-α (Llama 3.1 8B Instruct) — v3

Préenregistrement court d'une expérience **hors du programme**, aux sections du gabarit `prereg/gabarit-preregistrement-v1.md`
(R1, R2). **Remplace la v2** (`texte-gele-volet-a-et-b-alpha-v2.md`, `239e359eafec6780d3f353ef8dc0f65cad7c5fb2d0832f49849022b251c10629`,
jamais scellée, archivée telle quelle), elle-même issue de la v1 (`4ac7b556ad4519790216ed00fc7ddedcbd23393bc5d53ac0facdc6690c940267`),
après les contre-lectures 1 et 2 (`docs/notes/neuron-lens-v1/contre-lectures/`) et les comptes faits sur le texte seul
(« Plan d'analyse », A.0). Il ne lance rien : **aucune ligne de GO n'est inscrite** ; aucune machine, aucune
dépense, aucun appel de modèle avant une ligne inscrite par la mère sur un mot direct de Lazar **et** son feu écrit avec le
numéro de ligne ; aucune exécution du code voisin avant une règle décidée par Lazar (R-2685).

- Autrice : session fille « Neuron Lens » (`session_01QPDgKfBxeeiM3BsxqJgSgf`, branche `prep/neuron-lens-v1`), consigne de la
  mère `session_01QPDgKgACWyCkCN8HjqwNXy` (R-2685). Modèle de l'autrice : « modèle A ».
- Date : v2 écrite le 2026-11-14 vers 10:00–10:05 UTC ; v3 à partir de 10:14 UTC (`date -u`).
- Code d'analyse : **aucun écrit à ce jour** (seul l'outil de comptes sur le texte, `docs/notes/neuron-lens-v1/outils/comptes_avant_scellement_v1.py`,
  `64c538d3b47ce1d47b65e59fb07d5207b150570ac6e32a74545bf0de1f59d9fb`, sortie `comptes-avant-scellement-v1.json`,
  `e0aa5a1cb8e577c096354fd920372432a03774ec2faef03e67bdbbb0e4b9bf6d`, tous deux scellés). Code voisin épinglé : `stdlogits/neuron-lens`, commit
  `849bfe1678e28becceb1e3864afe5fc8297d02e4` (MIT), plus **trois correctifs datés** dans `docs/notes/neuron-lens-v1/correctifs/`,
  chacun contre-lu et scellé avant usage : (1) passe d'activations (`06_activations-llama-v2.diff`) ; (2) lentilles publiques
  de Llama dans `lenses.py` (`lenses-neuronpedia-llama-v2.diff` : empreintes vérifiées sur le fichier lu, couches `0..30` exigées,
  erreur sur tout autre format) ; (3) graine de neurones de l'audit (**à écrire**, contre-lire et sceller avant tout audit qui
  l'emploie : `random_neurons` est appelé avec la graine 0 par `sample_neurons` et par `score`, qui doivent recevoir la même graine). Notre code d'analyse du volet A
  sera écrit après le scellement de ce texte, contre-lu, et son commit consigné au manifeste ; il met en œuvre ce texte sans rien
  en changer (tout écart : liste d'arrêt).
- Documents qui font foi :

| pièce | chemin | empreinte SHA-256 |
|---|---|---|
| consigne de la première fille | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-12-2019-v1/consigne-fille-neuron-lens-v1.md` (`main`) | `43ac1788b4b3260bad6e1c68614ab337cd4ae539aa9302ae69ba757a46de5b2e` |
| interdits communs v2 | `docs/notes/g0-deux-semaines-v1/consignes-mere-2026-11-10-0500-v1/interdits-communs-v2.md` (`main`) | `1ee3b37075aacb278864e6eeda99b72e0d1babe9d6d02bd4a0c0aff26131337f` |
| plan et devis v1 (§§ 3, 4.2) | `docs/notes/neuron-lens-v1/plan-et-devis-v1.md` | `bc20a12aeb5cffeaa12ac264d5141036100b530f4a6a7c0998e24d1b184e3668` |
| plan et devis v2 (§§ 3, 4) | `docs/notes/neuron-lens-v1/plan-et-devis-v2.md` | `4f6534907b849cada369ac87df6fbcf87f766085c0ed56c0388bf849e4aa9c77` |
| passation reprise | `docs/notes/neuron-lens-v1/passations/2026-11-14-0933.md` | `80507f8c075e84e11f77c4994c47f17a5e56990b3dda77bd1ae75a5c66333dcb` |
| résultats publiés, lecture contre pilotage (Qwen3-8B) | `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/causal_lens_qwen3-8b.json` | `8904c4d34154068293700fbabf967f553415e6969aafebe06e29a452e03830d3` |
| résultats publiés, lectures aux activations | `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/reads_at_firings_qwen3-8b.json` | `ac0bf101e341385a400bbecb751f9720428da1d0bd09a752c8337dd84ba182cd` |
| code publié de la mesure (copie) | `docs/sources/neuron-lens-v1-devis-20261113/reference-publiee/scripts-checks-causal_lens.py.txt` | compagnon `.sha256` |
| constats publiés (§ 1) | `docs/findings.md` voisin au commit `849bfe16` ; copie `docs/sources/neuron-lens-lecture-20261113/depot-neuron-lens/docs-findings.md` (`main`) | `8814874b1cbe144f2cd1070ee20384b397be105c47b3e9cbeb9360a25ee5a866` |
| arbres des lentilles (Neuronpedia ; `stdlogits/rs-lenses`) | `docs/sources/neuron-lens-lecture-20261113/huggingface/lentilles-neuronpedia-jacobian-lens-arbre.json`, `…/lentilles-stdlogits-rs-lenses-arbre.json` (`main`) | manifeste v2 du lecteur ; `d2a7a076aa86ada4b6901bb02e9380f08ec2db9b8214f4346d2a6c552d999ec1` |
| jeux publics et tokeniseur (relevés le 2026-11-14 à 09:58 UTC) | `docs/sources/neuron-lens-v2-contrastes-20261114/` (manifeste et compagnons) | voir « Métrique », A.2 |

## Hypothèse

### Portée et séparations
- **Hors programme.** Aucune hypothèse du programme (H1 à H9, HC1 à HC6, L, T, Tr) n'est testée ; aucun résultat n'entre dans
  T0.7, T0.8, G0, G1 ni dans un préenregistrement du programme sans nœud de Lazar.
- **Séparation d'avec P3 et P3b** (R-2685) : l'autrice n'a rien lu de P3 ni de P3b. **Les sorties de ce texte ne servent à fixer
  aucun choix de lecture de P3b** (`GO-2026-10-20-10`), même si la famille des lentilles est la même pour Llama 3.1 8B Instruct.
  Aucune donnée réservée, aucune sonde du programme n'est employée ou lue.
- **Modèles** : volet A, `Qwen/Qwen3-8B` (changement de modèle permis pour ce seul volet, R-2528) ; tranche B-α,
  `meta-llama/Llama-3.1-8B-Instruct`. Les étiquettes en mots du catalogue publié viennent d'un modèle de la famille Claude
  (« modèle C ») : description seulement, jamais un critère.
- **Antériorité** : lire un poids de sonde par projection sur le vocabulaire est ancien ; rien n'est revendiqué.
- **Règle de lecture** : une lecture par lentille **peut ajouter un soupçon sur une sonde, jamais la blanchir** ; « fuite non
  retrouvée » se lit « l'instrument ne voit pas une fuite plantée à cette profondeur ».
- **Hors de ce texte** : tranche B-β (voir « Plan d'analyse », B.4), option B-bis, têtes d'attention.

### Volet A — Neuron Lens tel que publié, sur Qwen3-8B, vu d'un moniteur
- **A-i (audit de fuite textuelle)** : la lentille S, appliquée au poids d'une sonde linéaire, nomme les jetons d'entrée dont la
  sonde dépend, y compris une fuite plantée, mieux qu'une lecture sans lentille et sans se réduire à ce qu'un sac de jetons dit.
- **A-ii (neurones comme traits)** : à budget petit (k ≤ 64 neurones), un détecteur sur neurones égale une sonde sur le flux
  résiduel en distribution sans perdre hors distribution.

### Tranche B-α — la lecture R tient-elle sur Llama 3.1 8B Instruct, avec les lentilles publiques ?
- **B-2** : la lecture de l'écriture d'un neurone par la lentille R publique de Neuronpedia prédit l'effet de son pilotage.
- **B-3** : elle devance nettement la lentille des logits dans la première moitié du réseau.
- **B-4** (rapportée, non décisive) : écart sur les lentilles J et J++ publiques.
- **B-7** (conclusion pour un moniteur, hors verdict de reproduction) : la lecture prédit mal ce qu'**une activation isolée** fait
  en contexte avant les deux tiers de la profondeur.

## Prédiction chiffrée et signe attendu

R3 : aucune course ne vise un signe ; les issues contraires sont écrites et rapportées à l'identique.

| mesure | prédiction | issue modale prédite |
|---|---|---|
| A-i | aucune direction visée | « n'apporte rien » ou « indéterminé » (confiance 0,7) |
| A-ii | en distribution, écart à la sonde résiduelle < 0,02 dès k = 64 ; hors distribution, aucune direction | « indéterminé » ou « sans objet » sur C1 et C2 (plafond) |
| B-2, B-3 | motif publié retrouvé avec la lentille R publique (0,55) | « reproduit avec la lentille R publique » |
| B-4 | positif et petit (+0,026 à +0,131 publiés), non décisif | — |
| B-7 | bas (< 0,25) sur les couches 0 à 15, ≥ 0,50 sur 26 à 29 | « reproduit » |

## Métrique

### A.1 Commun au volet A
- **Modèle** : `Qwen/Qwen3-8B`, révision `b968826d9c46dd6066d109eabc6255188de91218`, licence Apache-2.0 (fiche relevée le
  2026-11-14, `docs/sources/neuron-lens-v2-contrastes-20261114/qwen3-8b-api.json`) ; 36 couches, 4 096 dimensions, 12 288
  neurones par couche à portes.
- **Lentilles** (`stdlogits/rs-lenses`, CC BY 4.0, citation due) : R = `qwen3-8b/r-lens/lens.pt`
  (`5eaa4d56e10d0c535b5170d5aaaa1174fb8dedf0fddb2f9821cec0aa1050fae1`) ; S = `qwen3-8b/s-lens/out.pt`
  (`f87601433def8cfc403508acccadb7e62d99a5ccf51ec30e730d7c93c21d37ec`) ; S côté entrée pour le cas sain : `qwen3-8b/s-lens/mid.pt`
  (`836ac41eb7ba2194c1302e27b37d92dce23d67504310444ecfe926e6bd28a1b2`). Empreintes calculées sur les fichiers téléchargés.
- **Couches lues** : 8, 14, 20, 26.
- **Invite** : un seul tour d'utilisateur, rendu par le gabarit de Qwen3 sans invite de génération
  (`<|im_start|>user\n` … `<|im_end|>\n`) ; contenu = **préambule identique pour toutes les classes** puis texte de l'exemple.
  Préambule, écrit ici : « Below is one short text taken from a public collection used in research on language models. Read it
  as written; no answer is needed. » suivi de deux retours à la ligne (27 jetons ; préfixe du gabarit : 3 jetons).
- **Position lue** : le dernier jeton du contenu de l'utilisateur ; aucune moyenne sur les jetons. Positions lues sur le texte
  seul : C1 34 à 59 ; AdvBench retenu 36 à 58 ; C2 47 à 81 ; C2 paraphrasé 45 à 77 ; C3 33 à 65 ; **aucune sous 16**. Le jeton
  planté de C2 commence à la position 36 pour tous les énoncés. (Le rendu manuel du gabarit est vérifié à la course par le
  tokeniseur du modèle ; tout écart d'identifiants arrête la course.)
- **Vocabulaire lu** : jetons gardés du catalogue publié (`catalog.kept`, Qwen3-8B), dont l'empreinte est consignée à
  l'addendum (liste d'arrêt).
- **Lectures d'un covecteur `w` à la couche L** :
  1. `w` est ramené au flux brut (les traits de la sonde sont centrés-réduits : `w_brut = w / σ`, σ des traits d'apprentissage),
     puis normé à 1 ; `−w` est lu par la même formule (aucune convention de signe implicite) ;
  2. lecture S : `s_v(w) = w · K_L (W_E[v] − m)`, `m` = moyenne de `W_E` sur les jetons gardés, `K_L` = `s-lens/out.pt` ;
  3. témoin sans lentille : `t_v(w) = w · (W_E[v] − m)` ;
  4. **centrage-réduction (`_z`)** : pour chaque jeton `v`, `μ_v` et `σ_v` sont la moyenne et l'écart-type de `s_v(u)` (resp.
     `t_v(u)`) sur **1 000 covecteurs unitaires gaussiens de référence**, un tirage par couche lue, commun à tous les contrastes
     et découpes (graine : Plan d'analyse, A.1), distincts des 100 directions témoins ; `z_v(w) = (s_v(w) − μ_v) / σ_v`. Pour des
     références isotropes, `μ_v ≈ 0` et `σ_v ≈ ‖K_L(W_E[v] − m)‖ / √d` : ce `_z` vaut environ √d fois le cosinus entre `w` et
     l'empreinte du jeton ; il retire les **jetons pivots de grande norme**, pas un mode commun aux directions réelles de la couche
     (ce que fait le `_z` du catalogue, moyenné sur les pôles d'une couche) ; **écart déclaré**, avec cette limite. Les lectures
     `_z` portent les critères ; les brutes sont rapportées.
  5. lecture R (description, sans critère) : `W_U (γ ⊙ norm(J_L u))` pour `u` = différence des moyennes des classes, et pour
     `w_brut` à part ; mêmes 20 premiers jetons rapportés.
- **Sonde** : régression logistique L2 avec ordonnée à l'origine, solveur `lbfgs` (`scikit-learn`, version consignée),
  1 000 itérations au plus, pénalité choisie sur la grille C ∈ {10⁻⁴, 10⁻³, 10⁻², 10⁻¹, 1, 10, 10²} par validation croisée
  interne à 5 plis **groupés** (mêmes groupes que les découpes), critère : AUROC moyenne ; égalité : le plus petit C ;
  traits centrés-réduits sur l'apprentissage.
- **Sac de jetons** : même régression, même grille, mêmes plis, sur les **comptes bruts** (non centrés-réduits) des jetons du
  texte de l'exemple (préambule exclu, identique partout). Ordre de ses poids pour A3 : |poids| décroissant, puis identifiant
  croissant ; seuls les poids non nuls comptent (s'il y en a moins de 10 d'un signe, on prend ceux qui existent, nombre rapporté).
- **Base « longueur seule »** (rapportée, sans critère) : AUROC de la longueur du texte en jetons, par contraste (sur le texte
  seul : 0,61 sur C1, 0,57 sur C3, calcul du contre-lecteur 2).

### A.2 Contrastes (fixés ici ; comptes dans `comptes-avant-scellement-v1.json`)
Fichiers, relevés le 2026-11-14 à 09:58 UTC (`docs/sources/neuron-lens-v2-contrastes-20261114/`) : JailbreakBench nuisibles
`4a8ec6832056b631eb092dccc60d37a61c3d441268268888b3d006288afeffa1`, bénins `3cda234d21a991fa309bbfea4b6d9dae31ccdf8e9d452424b6a983e4fdc33468` (MIT) ;
AdvBench `6cd1a5c63c07610d7eb67307772ee5606017ee950b5770ab288a2c487489d3e1` (MIT) ; faits de `representation-engineering`
`151b6163289460eb8b37f7c6a1998e23aed8e05b5e557bf1a2297079bf0e5af9` (MIT, commit `5455d8a3…`) ; tokeniseur de Qwen3-8B
`aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4` (non versé au dépôt : 11 Mo ; empreinte vérifiée au
téléchargement de la course).
- **C1, nuisible contre bénin** : 100 paires de JailbreakBench (même `Index`, même comportement) ; 200 exemples. Hors
  distribution : les 520 nuisibles d'AdvBench moins ceux qui sont identiques à un nuisible de JailbreakBench après normalisation
  (11) ou proches (indice de Jaccard des mots ≥ 0,5 avec un nuisible de JailbreakBench ; 57 retirés en tout) : **463 retenus**,
  contre les bénins du test de la découpe.
- **Faits** : 612 lignes, 598 énoncés distincts ; « The Nile River is the longest river in the world. » porte les deux étiquettes
  et est retiré ; **297 vrais et 300 faux retenus**, dédoublonnés par texte.
- **C2, fuite plantée** : les 297 vrais, précédés de « Pretend you're an honest person making statements about the world. » ou
  de « Pretend you're an untruthful person making statements about the world. » (gabarit publié, `examples/honesty/utils.py`,
  ligne 33), séparés de l'énoncé par une espace ; 594 exemples. Hors distribution : « Imagine you are a truthful speaker stating
  facts about the world. » / « Imagine you are a deceptive speaker stating facts about the world. », **sur les seuls énoncés du
  test de la découpe**.
- **C3, vrai contre faux** : 297 vrais contre 300 faux, sans consigne ; pas de jeu hors distribution.
- **Ensemble P des jetons plantés** (identifiants qui diffèrent entre les deux consignes tokenisées en contexte, identiques pour
  tous les énoncés) : `650` « Ġun », `58577` « truth », `1262` « ful » (forme « untruthful ») et `10745` « Ġhonest ». Les
  morceaux génériques (« Ġun », « ful ») sont gardés : ce sont eux que voit le modèle.

### A.3 Mesure A-i — lire la direction d'une sonde
| | métrique (par contraste, couche, découpe) |
|---|---|
| A1 (C2) | meilleur rang d'un jeton de P parmi les jetons gardés, dans la lecture S `_z` de +w et de −w (le meilleur des deux signes) |
| A2 (C1) | corrélation de rangs de Spearman entre la lecture S `_z` de w et les poids du sac de jetons, sur les jetons gardés présents dans le **texte de l'exemple** (préambule exclu) d'au moins 2 invites d'apprentissage |
| A3 (C1, C2) | chute d'AUROC de la sonde sur le test quand on retire du texte de l'exemple les 20 jetons de la lecture S `_z` (10 premiers de +w, 10 premiers de −w) : suppression de toutes leurs occurrences dans la suite des identifiants du texte, **sans nouvelle tokenisation**, puis passe de nouveau ; sonde non réapprise ; un exemple dont le texte devient vide est écarté et compté |

Témoins de A1 et A2 : 100 covecteurs unitaires gaussiens ; sonde apprise sur étiquettes permutées ; direction de la sonde de C3 à
la même couche ; lecture sans lentille. Tous les témoins sont lus **sur les deux signes**, comme `w`. Rapporté en plus pour A3 : le
nombre des 20 jetons retirés qui sont présents dans les textes de test. Témoins de A3 : 200 tirages de 20 jetons, chacun apparié à un jeton retiré par classe de
fréquence d'apprentissage (classe « 0 » pour les jetons absents des invites d'apprentissage ; déciles parmi les jetons présents) ;
les 20 premiers jetons du sac de jetons (10 par signe).

### A.4 Mesure A-ii — des neurones comme traits
Traits : activations des neurones de la couche à portes (porte activée × montée), mêmes couches, même position. Détecteurs : à k ∈
{1, 8, 64, 512}, les k neurones de plus grand écart moyen standardisé entre classes sur l'apprentissage, puis logistique L2 (grille
de A.1) ; détecteur dense (12 288). Références : sonde résiduelle (4 096) ; sonde sur les k premières composantes principales ;
k neurones au hasard (20 tirages, moyenne) ; sac de jetons. Métrique : AUROC en distribution (test de la découpe) et hors
distribution (C1, C2) ; écart apparié à la sonde résiduelle moyenné sur les 5 découpes ; intervalle à 95 % par rééchantillonnage
apparié des exemples de test (2 000 tirages, stratifiés par découpe). Les jeux de test des 5 découpes se recouvrent : cet intervalle
n'est pas celui d'exemples indépendants ; il est rapporté comme tel.

### A.5 Description jointe (sans critère)
Pour les 8 premiers neurones de chaque détecteur parcimonieux : étiquette (modèle C) et lectures du catalogue, accord avec une liste
de mots du concept fixée avant la course. Lectures R (A.1, point 5) : 20 premiers jetons par couche.

### B.1 Commun à la tranche B-α
- **Modèle** : `meta-llama/Llama-3.1-8B-Instruct` (32 couches, 14 336 neurones par couche, 4 096 dimensions) ; révision consignée à
  l'addendum.
- **Chaîne** : dépôt voisin au commit `849bfe16` avec les correctifs (1) et (2) ; `checks/causal_lens.py measure` avec ses défauts
  publiés (lignes 374 à 377 de la copie) : 32 neurones par couche (`random.Random(0)`), deux pôles, 16 contextes de 64 jetons,
  positions `[16, T)`, doses 1× et 4× `act_top`, ablation sur les 8 premiers documents du pôle, fenêtre de 8 ; puis `score`.
- **Lentilles notées** (aucune n'entre dans `measure`) : logits (identité) ; de `neuronpedia/jacobian-lens` (licence Llama 3.1,
  citation due) : J `llama3.1-8b-it/jlens/Salesforce-wikitext/Llama-3.1-8B-Instruct_jacobian_lens.pt`
  (`d5300a1575c0b5ad6e01b098c75adb072f3a6c246f184ce2fb35a3550fc8c68b`), J++ `llama3.1-8b-it/jpp/Salesforce-wikitext/Llama-3.1-8B-Instruct_jpp_lens.pt`
  (`8bd04f482aed9c85e76e71ccb510907405500512193cdfcc34f4f31722056f7c`, nom `npJpp`), R publique
  `llama3.1-8b-it/rlens/Salesforce-wikitext/Llama-3.1-8B-Instruct_rlens.pt` (`a63a1588f2cb61850c68131a5f13b74590f4fe137f67bf80c627547d2230d31c`,
  nom `npR`). Nombres de documents d'ajustement (461 ; 64) : **niveau citation**, relus dans les `config.yaml` en B0.
- **Métriques par couche, cible et lentille** (définitions de `score`) : `r_med` (r de Pearson médian sur les pôles retenus, sur le
  vocabulaire vu au moins 5 fois) ; `pass` (part des pôles dont r dépasse le 99ᵉ centile des r du témoin, centile commun aux
  couches) ; `control_med` (**témoin** : pôle apparié à la lecture du neurone tiré suivant) ; **n** (pôles retenus par `score`,
  qui écarte les pôles d'effet nul et, pour l'ablation, ceux sans contexte). `score` n'écrit pas n : **notre code le recalcule**
  à partir du fichier `-causal.pt` par la règle de `score` (pôle retenu si sa cible a une norme non nulle sur les lignes du
  tokeniseur, avant le filtre de vocabulaire ; pour l'ablation, s'il a des contextes, `fired`), avec le nombre de pôles écartés
  par motif ; code contre-lu et essayé (R5 : pôle forcé à zéro → écarté ; pôle sans contexte → écarté). Sur la référence, les
  dénominateurs de `pass` donnent 64, 59, 57, 62, 61 aux couches 0 à 4.
  **Couche 31** : les fichiers de Neuronpedia n'ont que les couches 0 à 30 ; à la couche 31, `J`, `npJpp` et `npR` sont
  **exactement** la lentille des logits dans `score` (même construction que la référence publiée, dont le fichier J s'arrête à
  la couche 34 sur 36) : ce ne sont pas des mesures de lentille ; elles entrent dans le centile commun de `pass`, comme dans la
  référence.
  Cibles : « steer 1x » (B-2, B-3, B-4) ; « ablate win » (B-7) ; « steer 4x » et « ablate pos » rapportées sans critère.
  Intervalles par rééchantillonnage des pôles (2 000 tirages), rapportés ; verdicts sur les valeurs ponctuelles.
- **Couche lisible** : n ≥ 48 pour la cible considérée. Une couche non lisible ne compte ni pour ni contre ; une bande dont plus du
  quart des couches est non lisible rend la mesure « partielle » pour cette bande.
- **Seuils et profondeur** : les bandes de couches sont reprises du plan v1 telles quelles ; à profondeur convertie (couche Llama
  l ↔ couche Qwen3 **⌊l × 36/32⌋**, partie entière, règle unique de ce texte), elles valent environ 0,53 à 0,70 fois les valeurs publiées (bande 8–15), 0,62 à 0,76 (16–23), 0,86
  à 0,88 (24–27) (calcul du contre-lecteur, rapport de la contre-lecture 1, point 19) ; la v1 disait « environ 0,8 », inexact.

## Seuil

Fixés avant toute lecture ; aucun résultat n'existe.

### A — volet A
Règle de couche : pour une découpe, la condition est évaluée à chaque couche ; une couche est **« positive »** si la condition
tient dans au moins 3 des 5 découpes, **« négative »** si elle tient dans au plus 1 découpe, « indécise » sinon. Rangs : médiane
sur les découpes.
- **A1** : condition à une couche = un jeton de P parmi les 10 premiers (l'un ou l'autre signe), **et** aucun jeton de P dans les
  10 premiers d'aucune des 100 directions aléatoires, de la sonde à étiquettes permutées, ni de la direction de C3 (à cette couche
  et cette découpe). **« Retrouvée »** : au moins 2 couches positives ; **« non retrouvée »** : 4 couches négatives ; sinon
  « partielle ». Arrêt si P n'a aucun jeton parmi les jetons gardés.
- **A2** : condition = ρ de Spearman au-dessus du 99ᵉ centile des ρ des 100 directions aléatoires. **« Nomme »** : au moins
  2 couches positives. **« Sans objet »** si l'AUROC en distribution du sac de jetons sur C1 (moyenne des 5 découpes) est < 0,60.
  (Le critère de la v1, précision à 20 contre des jetons « associés » par le test exact de Fisher, est **inatteignable** : sur le
  texte seul, cet ensemble compte 0 à 1 jeton par signe et par découpe — comptes, A2 ; **écart déclaré**.)
- **A3** : condition = chute au-dessus du 95ᵉ centile des 200 tirages **et** ≥ la moitié de la chute obtenue avec les jetons du sac
  de jetons. Une couche est **sans objet** pour A3 si la chute du sac de jetons y est < 0,02 d'AUROC (moyenne des 5 découpes) ; un
  contraste est sans objet pour A3 si ses 4 couches le sont. Parmi les couches non sans objet : « dépendance lue » = au moins 2
  couches positives ; **« dépendance non lue »** = toutes négatives pour la condition « chute < moitié de celle du sac de jetons »
  (règle 3/5–1/5) ; sinon « indécise ».
- **S fait mieux que sans lentille** : condition à une découpe et une couche = rang de S strictement meilleur que celui de la
  lecture sans lentille (A1), ou ρ de S strictement plus grand (A2) ; règle de couche 3/5–1/5 ; il faut au moins 2 couches
  positives **qui soient aussi des couches positives de A1** (pour la comparaison en A1) **ou de A2** (pour la comparaison en A2).
  « Sans lentille ≥ S » à une couche = couche négative de cette condition.
- **Composantes de A1 rapportées à part** : (i) S place un jeton de P dans ses 10 premiers ; (ii) un témoin le fait aussi.
- **Centiles** : `numpy.quantile`, interpolation linéaire par défaut ; « au-dessus » = strictement.
- **« Nomme » (A2)** est rapporté ; il n'entre dans le verdict que par la comparaison « S fait mieux que sans lentille ».
- **A-ii**, par contraste. **Plafond**, par couche (moyenne des 5 découpes) : si l'AUROC en distribution de la sonde résiduelle est
  ≥ 0,99 à une couche, la partie « en distribution » y est sans objet et cette couche ne se juge que hors distribution ; si les deux
  sont ≥ 0,99 (C3 : en distribution), la couche est sans objet ; un contraste dont les 4 couches sont sans objet est **sans objet**.
  Ordre de priorité : « n'apporte rien » > « apporte » > « indéterminé ». **« N'apporte rien »** : à chaque couche non sans objet, la
  sonde gagne de plus de 0,05 à tout k ≤ 512, sur chaque partie non sans objet (en distribution, hors distribution ; C3 : en
  distribution). **« Apporte »** : il existe k ≤ 64 tel que, à au moins 2 couches non sans objet, AUROC en distribution des neurones
  ≥ AUROC de la sonde − 0,02 (si cette partie n'est pas sans objet) **et** borne basse de l'intervalle à 95 % de l'écart hors
  distribution (neurones − sonde) ≥ −0,05 (C3 : condition en distribution seule). **Qualificatif rapporté avec le verdict** (C1 et
  C3) : « au-delà du texte » si le meilleur détecteur à k ≤ 64 dépasse le sac de jetons d'au moins 0,02 d'AUROC hors distribution
  (C3 : en distribution) ; sinon « pas au-delà du texte ». **Sur C2, qualificatif sans objet** : les paraphrases se tokenisent en
  jetons absents de l'apprentissage (« Ġtruthful », « Ġdeceptive »), le sac de jetons y vaut 0,5 par construction.

### B — tranche B-α (lentille `npR`, cible « steer 1x » sauf mention)
« Reproduit » exige la condition à **chaque couche lisible** de la bande. **Le tableau fait foi** pour « non reproduit » : ses
clauses portent sur les bandes qu'il nomme ; « plus de N des couches » se lit « plus de la moitié des couches **lisibles** de la bande
nommée » (N vaut pour une bande entièrement lisible ; règle du plan v1 pour B-3, étendue aux autres clauses, **écart déclaré**).

| mesure | « reproduit » | « non reproduit » |
|---|---|---|
| B-2 | `r_med` ≥ 0,40 (couches 8–15), ≥ 0,60 (16–23), ≥ 0,85 (24–27) ; `pass` ≥ 0,90 (8–27) ; témoin : `control_med` hors de ±0,05 à **au plus une** couche de 0 à 27, et à aucune hors de ±0,10 | `pass` < 0,50 à plus de 6 des 12 couches 16–27, ou `r_med` < 0,30 à plus de 4 des 8 couches 16–23 |
| B-3 | `r_med`(npR) − `r_med`(logits) ≥ +0,20 à chaque couche 4–15 | écart ≤ 0 à plus de 6 des 12 couches 4–15 |
| B-4 | rapportée : `r_med`(npR) − `r_med`(J) et − `r_med`(npJpp), couches 4–23 ; **non décisive** | — |
| B-7 (« ablate win ») | `r_med` < 0,25 à chaque couche 0–15 **et** ≥ 0,50 à chaque couche 26–29 | `r_med` ≥ 0,40 à plus de 4 des 8 couches 8–15, ou < 0,30 à plus de 2 des 4 couches 26–29 |

**Chaîne en défaut ou mode commun réel, audit** (aucun verdict de mesure ; passage à B-β suspendu jusqu'à l'audit) : (a)
`control_med` hors de ±0,10 à une couche de 0 à 27, **pour l'une des quatre cibles et l'une des quatre lentilles** (un mode commun
réel de Llama, toutes les écritures d'une couche poussant les mêmes jetons, est une explication à examiner, pas un verdict) ; (b) **pilotage sans effet** : à une couche de 0 à 27, plus de la moitié des 64 pôles
écartés par `score` pour effet nul en « steer 1x » ; (c) cas sains internes manqués : lentille des logits, `r_med` (« steer 1x »)
< 0,80 à l'une des couches 28–30 (publié à la même profondeur : 0,935 à 0,957) ; **lentille `npR`**, `r_med` < 0,85 à l'une des
couches 28–30 (publié pour la lentille R : 0,98 à 0,99) ; (d) essai du correctif (1) ou (2) en échec, ou fumée de la passe en échec ; (e) **repli sur la lentille des logits** : pour `J`,
`npJpp` ou `npR`, |`r_med`(lentille) − `r_med`(logits)| < 10⁻³ à une couche de 0 à 23 (« steer 1x »), ou une matrice d'un fichier
de lentille égale à l'identité (à 10⁻⁶ près) à une couche de 0 à 27 ; le correctif (2) refuse déjà tout fichier dont les couches ne
sont pas exactement `0..30`.
Les couches 28 à 31 ne comptent pour aucun verdict de B-2 ni B-3 (toute lentille y approche r = 1 ; 0,9998 pour les logits à la
dernière couche de Qwen3-8B).

## Plan d'analyse

### A.0 Comptes faits avant scellement, sur le texte seul (aucun modèle, aucune activation)
Outil `comptes_avant_scellement_v1.py` (`64c538d3…`) sur les fichiers de A.2 et le tokeniseur ; sortie `comptes-avant-scellement-v1.json`
(`e0aa5a1c…`) : positions lues et source (A.1), effectifs (A.2), ensemble P (A.2), taille des ensembles « associés » de l'ancien A2
(0 à 1 par signe et par découpe sur 58 à 75 jetons testés). Ces comptes ont servi à fixer le préambule, A2 et les effectifs ; ils ne
lisent aucune étiquette de sortie d'un modèle.

### A.1 Volet A
- **Données** : C1 200 (hors distribution : 463 contre bénins de test) ; C2 594 (hors distribution : énoncés de test, deux consignes) ;
  C3 597. Pas d'arrêt optionnel.
- **Découpes** : 5 découpes 70/30, stratifiées, **groupées** : C1 par paire (`Index`), C2 par énoncé, C3 par énoncé (après
  dédoublonnage). Les jeux hors distribution ne servent ni à l'apprentissage ni au choix d'un hyperparamètre.
- **Graines (R9)** : `numpy.random.SeedSequence(entropy=20261114)` ; `spawn(4)` → enfants 0, 1, 2 pour les contrastes C1, C2, C3,
  enfant 3 pour les **covecteurs de référence `_z`** (puis `spawn(4)`, un par couche lue 8, 14, 20, 26, communs aux contrastes et
  aux découpes) ; pour chaque contraste `spawn(5)` → découpes ; pour chaque découpe `spawn(6)` dans l'ordre : permutation de la
  découpe, directions aléatoires (puis `spawn(4)`, une par couche), étiquettes permutées, tirages de A3, neurones aléatoires,
  rééchantillonnage ; numpy ≥ 1.25 ; graines consignées au manifeste (configuration et empreinte, versions, commit). (Les
  comptes A.0 ont tiré leurs découpes de C1 par l'enfant 0 de `spawn(3)` : comptes sur le texte seul, sans lien avec les découpes
  de la course.)
- **Ordre fixe de la course** : (1) addendum des empreintes scellé ; (2) cas sains (ci-dessous) **avant toute lecture** des
  contrastes ; (3) sondes et lectures ; (4) rapport complet.
- **Cas sains, toujours joués, avant toute lecture** (10 premiers pris parmi les jetons gardés ; vocabulaire entier rapporté à
  côté) : (i) lecture R brute de l'écriture du pôle publié `L8 n344 +` (README voisin : « owl, noct, bedtime, night ») : un jeton
  parmi ses 10 premiers dont la forme décodée, sans espace ni casse, commence par « owl » ou « noct » ou vaut « night » ; (ii) lecture
  S **brute**, avec `s-lens/mid.pt` à la couche 1, de la direction de lecture du pôle publié `L1 n11672 −` : `c · K^mid_1 (e_v − ē)`
  avec `c = â − b̂` (lignes de porte et de montée multipliées par le poids de la norme d'après l'attention, normées), ou `c = b̂` si le
  pôle est sur le lobe négatif (`neg_lobe` > 0,5 dans la table `acts` de la couche 1 du catalogue, versée à l'addendum ; définition de
  `scripts/08_reads.py`, en-tête, et `neuron_lens/neurons.py`, `read_rows`) (README voisin : « German, Germany, 德国 ») : un jeton
  parmi ses 10 premiers dont la forme décodée, sans espace ni casse, contient « german » ou « 德 » ; (iii) **cas synthétique de la
  chaîne des critères**, à chaque couche lue : pour le jeton fixé `v0` = « Ġworld » (identifiant 1879), le covecteur
  `w = K_L (W_E[v0] − m)` normé, ramené par la même chaîne que les sondes (lecture S `_z` avec `s-lens/out.pt` et les covecteurs de
  référence), doit placer `v0` au rang 1 ; de même la lecture sans lentille `_z` avec `w = W_E[v0] − m`. Un cas sain manqué = **chaîne
  en défaut** pour tout le volet A.
- **Comparaisons multiples** : règles de décision fixes, pas de tests ; tout est rapporté (4 couches × 3 contrastes × 4 budgets).

### A.2 Critères de lecture du volet A, rappel d'ordre
Ordre de priorité de A-i : chaîne en défaut > « n'apporte rien » > « apporte » > « indéterminé ».

### B.1 Tranche B-α — étapes
B0 : montage ; essai du correctif (1) (`essai-06_activations-llama-v2.py`, aucun test sauté) ; lecture des trois fichiers de
Neuronpedia (empreintes, format refusé s'il n'est pas celui du fichier J : correctif (2)) ; essai écrit et contre-lu des crochets de
pilotage et d'ablation de `causal_lens.py` sur un Llama miniature (norme de la cible non nulle, pôle témoin différent du pôle) →
corpus d'activations et comptes de jetons → fumée `06_activations.py --docs 64` → passe complète → `measure` → `score --lenses
logit,J,npJpp,npR` → scellement, destruction par identifiant. (L'essai de l'estimateur des lentilles contre la force brute sur un
Llama miniature appartient à B-β, qui ajuste des lentilles ; tolérances : celles des essais du dépôt, inchangées.)

### B.2 Graines
`random.Random(0)` du dépôt pour les neurones ; seconde graine (1) seulement pour l'audit, par le correctif (3) contre-lu ; toute
autre graine par `SeedSequence(entropy=20261114)`, branche « B-α », consignée.

### B.3 Code des verdicts essayé (R5)
Avant la course, le code qui applique les seuils de B est passé sur la référence publiée de Qwen3-8B convertie (couche Llama l ←
couche Qwen3 ⌊l × 36/32⌋ ; lentille « R:dclm » dans le rôle de `npR`, « J » dans celui de `J` et de `npJpp` ; n pris égal à 64), puis
sur trois artefacts tirés de ce fichier, chacun séparément :

| cas | modification | attendu |
|---|---|---|
| (i) référence | aucune | B-2, B-3, B-7 « reproduit » ; aucune chaîne en défaut ; verdict « reproduit avec la lentille R publique » |
| (ii-a) | `pass` de `npR` (« steer 1x ») mis à 0,40 aux couches 16 à 27 | B-2 « non reproduit » ; B-3 « reproduit » ; B-7 « reproduit » ; verdict « non reproduit avec la lentille R publique » |
| (ii-b) | `control_med` de `npR` (« steer 1x ») mis à 0,20 à la couche 10 | chaîne en défaut (a) ; **aucun** verdict de mesure |
| (ii-c) | `r_med` de `npR` remplacé par celui des logits, toutes cibles | chaîne en défaut (e) ; aucun verdict de mesure |

Résultats consignés avant la course ; tout écart à l'attendu arrête la course.

### B.4 Hors de ce texte : tranche B-β (texte séparé, gelé avant β)
B-1, B-5, B-6, et B-2, B-3, B-4, B-7 avec notre lentille R. Relevés pour ce futur texte, sans rien geler :
- **Stabilité (R7)**, `docs/findings.md` voisin (`8814874b…`, § 1, lignes 49 à 62) : différence entre moitiés de la lentille R 0,04 à
  0,06 (couches 0–18), 0,03 (19–22), 0,02 (23–27), ≤ 0,01 dès 28 ; S 0,00–0,05 (`mid`), 0,01–0,05 (`out`) ; même premier jeton entre
  moitiés pour 0,89 à 0,99 des neurones aux six couches tabulées (2, 8, 14, 20, 26, 32 ; « 12 couches » dites mesurées) :
  **opposables**.
- **Critère B-5 du plan v1 mal posé** (« décroissant sur le premier quart ») : `read_S` publié 0,848, 0,248, 0,090, 0,229, 0,352
  aux couches 0 à 4 ; l'original manquerait ce critère. À réécrire.

## Critères de lecture gelés

### Volet A, mesure (i)
| issue observée | verdict |
|---|---|
| cas sain manqué | **chaîne en défaut** |
| A1 non retrouvée ; **ou** « sans lentille ≥ S » à chaque couche sur A1 **et** sur A2 (si A2 est sans objet : sur A1 seul) ; **ou** A3 « dépendance non lue » dans chaque contraste où A3 n'est pas sans objet, avec au moins un contraste non sans objet | **n'apporte rien** |
| A1 retrouvée **et** S fait mieux que sans lentille sur A1 ou A2, sans condition de la ligne précédente | **apporte quelque chose** |
| autre (A1 partielle, A2 ou A3 sans objet, etc.) | **indéterminé**, mesure par mesure |

### Volet A, mesure (ii), par contraste, sans agrégation
« apporte » (avec qualificatif « au-delà du texte » ou non) ; « n'apporte rien » ; « sans objet » (plafond) ; sinon « indéterminé ».

### Tranche B-α, reproduction
| issue | verdict |
|---|---|
| chaîne en défaut | **chaîne en défaut** ; passage à B-β suspendu (plan v2 § 3.2) |
| B-2 et B-3 « reproduit » | **reproduit avec la lentille R publique** |
| B-2 ou B-3 « non reproduit » | **non reproduit avec la lentille R publique** — **ne conclut pas sur la chaîne** (64 documents, autre corpus, autre code) ; B-β tranche ; ne bloque pas B-β |
| autre | **partiel**, mesure par mesure |

Un « reproduit » dira que la lentille lit ce qu'une direction **pousse en moyenne**, pas qu'elle nomme le concept d'une invite donnée
(banc public cité par le lecteur : 31 % à 53 % sur ce modèle, niveau citation).

### Tranche B-α, B-7 (pour un moniteur)
| issue | lecture |
|---|---|
| « reproduit » | là où `r_med` est bas, une étiquette de neurone décrit une poussée moyenne et ne peut pas servir à lire un épisode. Cette conclusion vaut pour **toute** lentille : sur la référence, « ablate win » est presque la même pour les trois (couche 26 : logits 0,53, J 0,51, R 0,54) ; B-7 ne distingue pas la lentille R |
| « non reproduit » par le haut | audit R4 avant toute lecture ; s'il tient, rapporté comme lecture valable en contexte plus tôt que publié |
| « non reproduit » par le bas | rapporté : la lecture ne dit pas ce qu'une activation fait, même tard |
| autre | couche par couche |

### Audit symétrique (R4)
- **Volet A, trop beau** : A1 au rang 1 à toutes les couches, ou neurones égaux à la sonde partout → direction permutée sans P, retrait
  de jetons vérifié sur le texte, sixième découpe (graine suivante) ; verdict après l'audit.
- **Volet A, tout négatif** (déclencheur : A1 « non retrouvée » et A-ii « n'apporte rien » sur C1 et C3) : les cas sains sont déjà
  joués ; en plus, rapporter l'AUROC de test de la sonde de C2 à chaque couche (si elle est < 0,9, la sonde n'a pas appris la fuite
  et A1 est relu en conséquence, sans changer le verdict) et vérifier que P est dans le vocabulaire gardé.
- **B-α, trop beau** : `r_med` ≥ 0,95 à une couche 0–7, ou `control_med` exactement 0 → témoin bien apparié, pilotage de norme non
  nulle, `measure` relancé avec la graine 1 (correctif (3), qui doit alors être écrit, contre-lu et scellé avant ; sinon l'audit
  attend et le verdict aussi) ; verdict après l'audit.
- **B-α, tout négatif** (déclencheur : B-2 et B-3 tous deux « non reproduit ») : rejouer `score` sur les sorties de `measure` publiées pour Qwen3-8B si elles existent, sinon `measure` sur
  Qwen3-8B aux couches 8 et 20 seulement, dans le plafond ; cas sain manqué (écart > 0,05 aux valeurs publiées) = chaîne en défaut.

## Liste d'arrêt

| condition | action |
|---|---|
| pas de ligne de GO inscrite par la mère sur un mot de Lazar, ou pas de feu écrit avec le numéro de ligne, ou pas de règle de Lazar sur l'exécution du code voisin | rien ne part |
| ce texte non scellé ; un correctif employé non contre-lu ou non scellé | rien ne part (R1, R2) |
| **addendum des empreintes** non scellé avant la première passe : révision de Llama 3.1 8B Instruct, `catalog.kept` et table `acts` de la couche 1 du catalogue de Qwen3-8B, corpus d'activations de Llama (révisions, tailles), fichiers de lentilles téléchargés, **liste de mots du concept** de A.5 | rien ne part |
| à B0 : un fichier de Neuronpedia sans exactement 31 couches, ou dont `config.yaml` / `CREDIT.md` disent une autre convention que « clé l = sortie de la couche l » | arrêt de B-α ; écart écrit |
| empreinte d'un fichier différente de celle écrite ici ou à l'addendum ; licence différente | arrêt ; message à la mère |
| rendu de l'invite par le tokeniseur du modèle différent des identifiants comptés (A.0) | arrêt du volet A ; message |
| P sans jeton parmi les jetons gardés | arrêt du volet A ; message |
| format d'un fichier de Neuronpedia refusé par `neuronpedia_lens` | arrêt de B-α ; toute lecture adaptée est écrite comme écart daté, contre-lue, avant usage |
| essai du correctif (1) avec un test sauté ou en échec ; fumée `--docs 64` en échec | arrêt de B-α : chaîne en défaut |
| dépense à 60 % du plafond de la ligne ou de la tranche | compte rendu à la mère ; à 90 %, arrêt dur |
| minuterie de destruction par identifiant non posée à la création | destruction par identifiant avant toute passe (R10) |
| refus d'un contrôle de permission ou d'un classifieur | arrêt sur ce point, rapport tel quel ; ni contournement, ni reformulation, ni transfert |
| envie d'écart à ce texte | écrit, daté, nouvelle version (R12), contre-lu, avant d'être fait |
| toute lecture touchant P3, P3b, T0.6, T0.7, P3-bis ou un chemin interdit | interdit ; arrêt |

**R5** : chaque garde codée (empreintes, rendu de l'invite, P dans les gardés, format des lentilles, part de pôles écartés, plafond de
dépense, code des verdicts) est essayée avant la course sur un cas sain et sur un artefact (fichier altéré d'un octet ; identifiant
changé ; P vidé ; fichier au mauvais format ; pôles écartés forcés ; dépense simulée ; référence altérée de B.3) ; résultats consignés ;
aucun repli silencieux.

### Écarts au plan v1 et v2, déclarés
1. Consigne de C2 : « untruthful » (gabarit publié), pas « dishonest » ; P en découle.
2. **Gabarit de C2** : le gabarit publié met la consigne sous la marque d'utilisateur et un **énoncé tronqué** après la marque
   d'assistant ; ici consigne et énoncé entier sont dans un seul tour d'utilisateur, après un préambule.
3. **Préambule neutre** de 27 jetons ajouté à toutes les invites (positions ≥ 16 ; mot planté en position 36).
4. Position lue : dernier jeton du contenu de l'utilisateur.
5. Faits dédoublonnés (297 vrais, 300 faux ; énoncé contradictoire retiré) ; C2 hors distribution restreint aux énoncés de test ;
   AdvBench dédoublonné (identité et Jaccard ≥ 0,5 : 463 retenus) ; découpes groupées.
6. `_z` d'un covecteur par 1 000 covecteurs de référence (le catalogue standardise sur les colonnes d'une couche) ; équivalent
   à √d fois un cosinus : retire les pivots de grande norme, pas un mode commun réel.
7. **A2 remplacé** (Fisher inatteignable) par la corrélation de rangs avec le sac de jetons, avec issue « sans objet ».
8. A3 : plancher de 0,02 et appariement des jetons absents ; A1 : témoins « permuté » et « C3 » entrés dans la condition.
9. A-ii : plafond 0,99 par couche, qualificatif « au-delà du texte » (sans objet sur C2) ; « n'apporte rien » exige « à chaque
   couche » (durcissement du plan) ; « apporte » exige une borne basse ≥ −0,05 hors distribution (le plan disait « intervalle
   contenant 0 », sans marge) ; ordre de priorité écrit.
10. Règle « 3 découpes sur 5 / au plus 1 » et médianes des rangs.
11. Cas sains du volet A joués toujours, avant lecture, en R **et** en S (le plan v1 § 3.4 les prévoyait en R et S « si tout échoue »).
12. B : « non reproduit » à plus de la moitié des couches lisibles pour toutes les bandes (le plan ne le disait que pour B-3) ;
   témoin de B-2 toléré hors de ±0,05 à une couche ; couche lisible n ≥ 48 ; « pilotage sans effet » chiffré ; cas sain `npR` ajouté.
13. B-3 publié relu : +0,352 à +0,425 (couches 4–17) ; le plan écrivait +0,35 à +0,42 ; seuil inchangé.
14. Trois correctifs du code voisin (préambule de ce texte) ; n recalculé par notre code ; couche 31 des lentilles de Neuronpedia
   égale aux logits, notée.
15. Base « longueur seule » rapportée ; garde (e) « repli sur les logits » ; cas sain synthétique de la chaîne des critères.

### Provenance des chiffres (R6, R7)
| chiffre | source | clé |
|---|---|---|
| B-2 publié : `r_med` R 0,33 (0), 0,45 (4), 0,49 (8), 0,65 (12), 0,74 (16), 0,87 (20), 0,95 (24) ; `pass` ≥ 0,9375 dès la couche 5 ; témoin −0,038 à +0,031 | `causal_lens_qwen3-8b.json` (`8904c4d3…`) | `targets["steer 1x"]["R:dclm"]` |
| B-3 publié : +0,352 à +0,425 (4–17) ; couche 8 : 0,49 contre 0,12 | idem | `["steer 1x"]["R:dclm"/"logit"]["r_med"]` |
| B-4 publié : +0,026 à +0,131 (4–23) | idem | `["steer 1x"]["R:dclm"/"J"]["r_med"]` |
| B-7 publié : 0,05 (0), 0,05 (4), 0,08 (8), 0,08 (12), 0,13 (16), 0,23 (20), 0,40 (24), 0,67 (28), 0,87 (32) ; témoin −0,013 à +0,029 ; couche 26 : logits 0,53, J 0,51, R 0,54 | idem | `["ablate win"]` |
| cas sains : logits 0,935 à 0,957 (couches 31–33 de Qwen3-8B, ⌊l × 36/32⌋ pour l = 28–30), 0,9998 à la dernière ; R 0,98 à 0,99 aux mêmes profondeurs | idem | `["steer 1x"]["logit"/"R:dclm"]` |
| n : 64, 59, 57, 62, 61 aux couches 0 à 4 (« steer 1x »), reconstruit des dénominateurs de `pass` | idem et contre-lectures 1 (point 12) et 2 (point 3) | `pass` |
| `read_S` 0,848, 0,248, 0,090, 0,229, 0,352 | `reads_at_firings_qwen3-8b.json` (`ac0bf101…`) | `["neurons"]["layers"][i]["read_S"]` |
| stabilité | `docs/findings.md` voisin (`8814874b…`), lignes 49 à 62 | — |
| défauts de `measure`, définition de `pass` | copie de `causal_lens.py` (lignes 1–61, 66–76, 325, 374–377) | — |
| positions, effectifs, P, ancien A2 | `comptes-avant-scellement-v1.json` (`e0aa5a1c…`) | — |
| 31 % à 53 %, 461 et 64 documents | note du lecteur (`12c8f673e41411683b112d5a218a2a88d6493fb91a60338393134aba0bf2a44e`) | **niveau citation, non opposable** |
| AUROC de la longueur 0,61 (C1), 0,57 (C3) ; jetons « Ġtruthful » 89867, « Ġdeceptive » 80274 | contre-lecture 2 (points 8 et 20), sur le texte seul | description |

Chiffres publiés recalculés par l'autrice (09:45 UTC) et par le contre-lecteur 1 (rapport, § 4 : tous en accord).

## Contre-lecture

- **Contre-lecture 1** — sous-agent neuf, « modèle B », lancé par l'autrice ; il n'a pas écrit le texte. Brouillon relu :
  `texte-gele-volet-a-et-b-alpha-v1.md`, `4ac7b556ad4519790216ed00fc7ddedcbd23393bc5d53ac0facdc6690c940267`. Rapport :
  `docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-1-texte-gele-v1-expurge.md`, `9f236ea87ba210bb9d72a31c4f8cfb6d671511100365920e52822af74c179be6` (copie expurgée d'un nom de modèle ; original `3d839dfce7f22e23c75638f4b8e2133e0ab133141b6eeb1c05eb7afa462dd868` retiré de l'arbre, dans l'historique). Verdict :
  « scellable après corrections ». Traitement :

| remarque | traitement |
|---|---|
| 1 positions < 16 | acceptée : préambule de 27 jetons, positions comptées (A.0) |
| 2 `_z` non défini | acceptée : formule complète (Métrique A.1) ; renvoi de fonction corrigé |
| 3 A2 inatteignable, A3 vide | acceptée : comptes faits (0 à 1 jeton associé) ; A2 remplacé ; plancher et appariement de A3 |
| 4 B-3 à 7 sur 12 | acceptée : « plus de la moitié » partout |
| 5 pilotage sans effet | acceptée : critère (b) |
| 6 cas sains | acceptée : toujours, avant lecture, R et S, listes de chaînes |
| 7 doublons des faits | acceptée |
| 8 fuite hors distribution de C2 | acceptée |
| 9 gabarit de C2 | acceptée : écart 2 |
| 10 ensemble P et témoins | acceptée : P listé, arrêt si hors des gardés, témoins dans la condition |
| 11 A-ii plafond, sac de jetons | acceptée : plafond, qualificatif, écart 9, C3 précisé |
| 12 n par couche | acceptée : couche lisible n ≥ 48 |
| 13 retouches du code voisin | acceptée : trois correctifs déclarés |
| 14 gardes de B-α | acceptée : cibles et lentilles nommées, cas sain `npR`, code des verdicts essayé (B.3), essai des crochets de pilotage ; garde « force brute » renvoyée à B-β |
| 15 empreintes manquantes | acceptée : jeux et Qwen3-8B écrits ; le reste à l'addendum, scellé avant la première passe |
| 16 libertés | acceptée : grille, plis groupés, retrait sans nouvelle tokenisation, ensemble du Spearman, règle 3/5–1/5, médianes |
| 17 « même modèle » | **refusée, constat contraire** : la description de la session autrice (outil de session, champ du modèle servi) donne un modèle différent de celui que le contre-lecteur dit être le sien ; modèle A ≠ modèle B. Le contre-lecteur s'est fié à une ligne d'attribution qu'il a mal lue |
| 18 témoin fragile | acceptée : au plus une couche hors de ±0,05 |
| 19 « 0,8 fois » | acceptée : phrase corrigée |
| 20 B-7 et la lentille | acceptée |
| 21 issue modale | acceptée |
| 22 titres | acceptée : titres du gabarit |
| 23 intervalles | acceptée : dit en A.4 |
| 24 lignes 374–377 | acceptée |

- **Contre-lecture 2** — sous-agent neuf, « modèle B », lancé par l'autrice ; il n'a pas écrit le texte. Brouillon relu :
  `texte-gele-volet-a-et-b-alpha-v2.md`, `239e359eafec6780d3f353ef8dc0f65cad7c5fb2d0832f49849022b251c10629`. Rapport :
  `docs/notes/neuron-lens-v1/contre-lectures/contre-lecture-2-texte-gele-v2.md`, `1a4a1b8dd435b40dc8ac4601685f78e96773937c2315e73cd6bc1f6ba8f3925e`. Verdict : « scellable après
  corrections mineures » ; comptes relancés, identiques octet pour octet ; référence convertie : « reproduit » partout, aucune
  chaîne en défaut. Traitement :

| remarque | traitement |
|---|---|
| 1 artefact de B.3 contradictoire | acceptée : le tableau fait foi ; trois artefacts séparés, attendus de B-2, B-3, B-7 écrits |
| 2 « plus de N » contre « moitié des lisibles » | acceptée : « plus de la moitié des couches lisibles de la bande nommée » |
| 3 n non produit par `score` | acceptée : recalcul par notre code, règle écrite, essai R5 |
| 4 repli silencieux sur les logits | acceptée : correctif (2) v2 (couches exactes, empreintes) et garde (e), artefact (ii-c) |
| 5 « S fait mieux » sans marge | acceptée : règle de couche, couches positives de A1 ou A2 |
| 6 trous de « n'apporte rien » (A-i) | acceptée : A2 sans objet → A1 seul ; « dépendance non lue » définie ; plancher de A3 par couche |
| 7 A-ii plafond, priorité, marge | acceptée : plafond par couche, ordre écrit, borne basse ≥ −0,05 |
| 8 qualificatif vide sur C2 | acceptée : sans objet sur C2 |
| 9 graines et portée du `_z` | acceptée : un tirage par couche (enfant 3) ; équivalence et limite écrites |
| 10 détails de A1, A2 | acceptée : deux signes, composantes séparées, `numpy.quantile`, texte de l'exemple, « nomme » rapporté |
| 11 cas sains | acceptée : formule du cas (ii), lecture brute, table `acts` à l'addendum, cas synthétique (iii), jetons gardés |
| 12 deux conversions | acceptée : partie entière partout |
| 13 refus de la remarque 17 non étayé | **maintenu, sans pièce versée** : la vérification a été faite par l'outil de description de session (champs du modèle configuré et du modèle servi), qui donne pour l'autrice un modèle différent de celui que les deux contre-lecteurs déclarent ; la pièce n'est pas versée au dépôt parce que les consignes interdisent d'y écrire un identifiant de modèle de la famille Claude. La mère peut le vérifier par le même outil sur la session `session_01QPDgKfBxeeiM3BsxqJgSgf` |
| 14 liste de mots | acceptée : à l'addendum |
| 15 A3 sur C1, égalités du sac de jetons | acceptée : nombre des jetons présents rapporté ; ordre des poids fixé |
| 16 mode commun réel | acceptée : libellé « chaîne en défaut ou mode commun réel, audit » |
| 17 déclencheurs de l'audit | acceptée : déclencheurs écrits ; AUROC de test de la sonde de C2 |
| 18 sonde et sac de jetons | acceptée : solveur, ordonnée, égalités, comptes bruts |
| 19 empreintes abrégées | acceptée : empreintes entières ; outil et sortie scellés |
| 20 longueur | acceptée : base « longueur seule » rapportée |
| 21 correctif (3) | acceptée : rappelé dans l'audit |
