# « Neuron Lens » — plan et devis, v2 : ce que changent la note du lecteur et les lentilles publiques de Llama

Écrit par la session fille « Neuron Lens » le 13 novembre 2026 à 13:17 UTC (`date -u`), à la demande de la mère (message de
13:16 UTC). **Remplace le § 4 (volet B), le § 5.3 et la ligne « volet B » du § 6 de la v1** (`plan-et-devis-v1.md`,
`bc20a12a…`, archivée telle quelle) et **amende le § 3 (volet A)** sur quatre points ; le reste de la v1 tient.
Lue et confrontée au code : `docs/notes/lecture-voisin-neuron-lens-v1.md` (`12c8f673…`, commit `9999c6a2` de `main`).
**Aucune dépense, aucune machine, aucun appel de modèle.** Aucune machine de ma part avant le feu de la mère (pas avant la
fin de la course P3-bis), même si une ligne est inscrite.

## 0. En cinq lignes

1. **Les lentilles publiques de Llama ne suppriment pas l'ajustement, elles permettent de le faire en second.** Elles couvrent
   le côté sortie seulement (J, J++, R ; sortie des blocs 0 à 30 vers le bloc 31) : la mesure phare (lecture contre pilotage,
   contre ses témoins) se fait **sans rien ajuster**. Manquent : la lentille S (côté entrée), le point de lecture à l'entrée
   de la couche à portes, et des moitiés de corpus pour la stabilité.
2. **Le volet B se coupe donc en deux tranches.** B-α, sans ajustement, sur une carte de 24 Go : ≈ 3 USD attendus, plafond
   **12 USD**. B-β, lentilles S et R ajustées par leur code : ≈ 22 USD attendus, plafond **68 USD**. Total inchangé : **80 USD**.
3. **Variante économe** (réemployer la lentille R publique, n'ajuster que S) : plafond total **60 USD**, ≈ 16 à 20 USD attendus ; on y
   perd la stabilité de R, la comparaison entre deux codes et la lecture R des directions d'entrée. Non recommandée : ce
   n'est plus « refaire leur chaîne ».
4. **Deux points du lecteur changent ce que je mesure**, pas ce que cela coûte : j'ajoute la lecture contre l'**ablation en
   contexte** (ce qu'une activation fait dans un épisode : c'est ce qu'un moniteur lit), et je baisse ma confiance.
5. **Recommandation** : ligne B à 80 USD en deux tranches, compte rendu entre les deux ; confiance 0,55 que B-α reproduit le
   motif moyen, 0,3 que le volet A montre un apport net pour un moniteur (0,4 en v1).

## 1. Confrontation de la note du lecteur au code (commit `849bfe16…`)

| point du lecteur | ce que dit le code | suite |
|---|---|---|
| ajustement des lentilles sur Llama « probablement oui », à essayer sur un Llama minuscule | d'accord (v1 § 2) ; l'essai m'a été refusé en local (v1 § 7) | reste l'étape B0, sur machine |
| catalogue complet « non sans adaptation » (normes de requête et de clé) | d'accord ; précisé : `06_activations.py` lignes 287-289 ; `08_reads.py` et `reads_at_firings.py` ont une option `--parts neurons` | retouche d'un script, inchangée |
| branche `neuron-lens-2` citée par le script de machine, non lue | elle existe (`f699d0c9…`), distincte de `main` ; `README` et résultats de référence sont ceux de `main` | je reste sur `main` au commit épinglé ; écart à la branche noté, non lu |
| Drowse sous AGPL-3.0 | la v1 notait la lentille par `R:<ajustement>`, forme qui passe par Drowse. **Erreur de la v1, corrigée** : la forme `fit:<fichier>` lit l'ajustement sans Drowse (`lenses.py`, `load_lens`) | aucun code AGPL installé ni intégré |
| lecteur de lentilles de Neuronpedia | `load_lens("J")` lit déjà ce format pour Qwen3-8B ; trois entrées à ajouter au dictionnaire `NEURONPEDIA_FILES` pour J, J++ et R de Llama. **Compatibilité du format non vérifiée par exécution** | vérifiée en B0 ; sinon lecture directe du fichier (une application 4 096 × 4 096 par couche) |
| durées et tailles | concordent avec la v1 | — |

Aucun désaccord de fond entre la note et le code. Deux ajouts de ma part que la note n'avait pas : les fichiers de
résultats publiés (`data/summary/`), dont viennent mes seuils, et le fait que la mesure phare n'exige que le point de
lecture « sortie de couche », celui que les lentilles publiques couvrent.

## 2. Ce qui se réemploie, ce qui reste à ajuster

| pièce | existe pour Llama 3.1 8B Instruct ? | licence | usage dans le volet B |
|---|---|---|---|
| lentille J (461 documents de WikiText), J++ et R (64 documents), sortie des blocs 0 à 30, demi-précision, 1,04 Go chacune (`neuronpedia/jacobian-lens`) | oui | licence communautaire Llama 3.1 et politique d'usage (dérivées du modèle) ; code d'ajustement Apache-2.0 ; **citation due** (Neuronpedia, « bubskee », Blank, Bhatia et Nanda, Ayonrinde et Lindsey) | **réemployées** : témoins J et J++, et lentille R de la tranche B-α |
| lentille R ajustée par le code de neuron-lens (1 000 documents de DCLM, deux moitiés, deux points de lecture) | non | la nôtre ; code MIT | **à ajuster** (B-β) : stabilité, comparaison entre deux codes, lecture R des directions d'entrée |
| lentille S (côté entrée) | non | la nôtre | **à ajuster** (B-β) : c'est la pièce propre à neuron-lens |
| activations, activation typique et meilleures activations par pôle | non | — | **à refaire** (B-α) : le pilotage en a besoin |
| descriptions des neurones par Transluce (2024) | oui | code MIT ; **licence de la base non vérifiée** | non employées ; pourraient remplacer l'option B-bis à coût nul, après vérification de la licence (nœud N-061) |

Réserves sur le réemploi : la lentille R publique repose sur 64 documents (erreur d'échantillonnage d'environ 8 %, contre
1,5 à 2 % à 1 000 ; calcul du lecteur à partir des 65 % entre deux documents), un autre corpus, un autre code. Une
reproduction manquée avec elle ne conclut pas ; une reproduction réussie vaut d'autant plus.

## 3. Volet B révisé

### 3.1 Tranche B-α — lecture contre pilotage avec les lentilles publiques (aucun ajustement)
B0 (montage, essais du dépôt, **essai Llama miniature contre la force brute**, lecture d'un fichier de Neuronpedia) → corpus
d'activations et comptes de jetons → passe d'activations avec la retouche contre-lue → `causal_lens.py measure` (32
neurones par couche, graine 0, doses 1× et 4×, ablation en contexte) → `score` contre : lentille des logits, J, J++, R
publique → scellement, destruction. Carte : RTX 4090 (24 Go : « enough for the text passes »).

### 3.2 Tranche B-β — refaire leur chaîne (lentilles S et R ajustées)
Banc d'un document par lentille → ajustement de S puis de R (1 000 documents de DCLM chacune) → pilotes exacts (`07`) →
lectures, neurones seulement (`08`) → `reads_at_firings.py` → nouvelle notation de la mesure de B-α avec notre lentille R
(`fit:…`, sans nouvelle passe du modèle) → scellement, destruction. Carte : H100 de 80 Go, repli A100 de 40 Go. Les tables
d'activations de B-α sont recopiées (ou refaites : 1,5 h comptée au pire cas).

**Passage de α à β** : compte rendu à la mère après B-α. β part sauf « chaîne en défaut » (témoin hors de ±0,10, pilotage
sans effet, essai miniature en échec). Un B-α « non reproduit » **ne bloque pas** β : avec 64 documents, la lentille publique
peut être la cause, et c'est β qui le dit.

### 3.3 Mesures et seuils
Les mesures B-1 à B-6 de la v1 (§ 4.2) et leurs seuils sont **inchangés**, avec ce partage :

| mesure | tranche | lentille |
|---|---|---|
| B-2 lecture R contre pilotage ; B-3 avance sur la lentille des logits | α (lentille R publique), puis β (la nôtre) : **deux lectures, toutes deux rapportées** ; le verdict du volet se prononce sur β, celle qui refait leur chaîne | — |
| B-4 avance sur J | α et β ; ajout : J++ rapportée de même, non décisive | — |
| B-1 stabilité, B-5 côté entrée, B-6 deux codes | β | — |
| **B-7, neuve** — lecture contre l'ablation en contexte | α et β | voir ci-dessous |

**B-7 (point du lecteur : une activation isolée ne fait pas ce que dit la moyenne).** Référence publiée
(`causal_lens_qwen3-8b.json`, cible « ablate win », lentille R) : r médian 0,05 (couche 0), 0,05 (4), 0,08 (8), 0,08 (12),
0,13 (16), 0,23 (20), 0,40 (24), 0,67 (28), 0,87 (32) ; témoin entre −0,01 et +0,03. Autrement dit, sur Qwen3-8B la
lecture ne dit presque rien de ce qu'une activation fait en contexte avant les deux tiers de la profondeur. Métrique sur
Llama : la même. **« Reproduit »** : r médian < 0,25 sur les couches 0 à 15 **et** ≥ 0,50 sur 26 à 29. **« Non reproduit »** :
r médian ≥ 0,40 sur les couches 8 à 15 (la lecture vaudrait en contexte plus tôt que publié : audit R4 avant de s'en
réjouir), ou < 0,30 sur 26 à 29. B-7 n'entre pas dans le verdict de reproduction ; elle porte la conclusion **pour un
moniteur** : là où B-7 est basse, une étiquette de neurone décrit une poussée moyenne et ne peut pas servir à lire un épisode.

**Lecture faible à notre échelle (autre point du lecteur).** Le banc public cité (concept attendu dans les dix premiers
jetons : 31 % lentille des logits, 42 % J, 45 % R, 53 % J++ sur Llama 3.1 8B Instruct) mesure autre chose que B-2 (un rappel
de concept sur des invites, pas un accord moyen avec le pilotage) : les deux peuvent être vrais ensemble. Il ne change
aucun seuil ; il change ce qu'on aura le droit de conclure : un B-2 « reproduit » dira que la lentille lit ce qu'une
direction **pousse en moyenne**, pas qu'elle nomme le concept d'une invite donnée plus d'une fois sur deux.

### 3.4 Devis révisé (prix de la v1 § 5.1, relevés à 13:04 UTC)

| tranche | poste | attendu | pire cas |
|---|---|---|---|
| **B-α** (RTX 4090, médiane 0,507, maximum relevé 0,870 USD/h) | B0, corpus, passe d'activations, pilotage et ablation, notation, transfert | 4,5 à 5,5 h → **≈ 3 USD** | 12 h × 0,87 = 10,4 USD ; disque 100 Go et réseau 1 USD → **≈ 11,5 USD** |
| | **plafond de tranche** | | **12 USD** |
| **B-β** (H100 à 2,344 USD/h ; prix plafond 3,00) | banc 0,5 h ; deux lentilles 6,2 à 8,9 h ; pilotes, lectures, lectures aux activations 1,3 h ; notation et transfert 0,8 h | 8,8 à 11,5 h → **21 à 27 USD** | banc et montage 2 h ; lentilles 13,2 h ; activations refaites 1,5 h ; reste 3,5 h ; une machine perdue 1 h = 21,2 h × 3,00 = 63,6 USD ; disque et réseau 4 USD → **≈ 68 USD** |
| | **plafond de tranche** | | **68 USD** |
| **volet B entier** | | **≈ 24 à 30 USD** | **plafond 80 USD** (inchangé) |

Variante économe (β sans notre lentille R : une seule lentille, 3,1 à 4,4 h) : attendu ≈ 13 à 17 USD pour β (16 à 20 avec B-α), pire cas ≈ 48 USD
pour β, **plafond total 60 USD**. Perdu : B-1 pour R, B-6, et la lecture R des directions d'entrée (`read_R` de B-5).

Pourquoi le plafond de la reproduction complète ne baisse pas : la lentille S n'existe nulle part ; la lentille R publique
n'a ni moitiés, ni point d'entrée de la couche à portes, ni le même corpus. Ce que les lentilles publiques apportent, c'est
l'ordre : la réponse à la question principale pour ≈ 3 USD, avant d'engager les heures de H100.

Gardes inchangées (v1 § 5.3) : compte rendu à 60 % du plafond de la tranche, arrêt dur à 90 %, minuterie de destruction
par identifiant, aucune H200.

## 4. Volet A : quatre amendements tirés de la note du lecteur (devis et plafond inchangés : 10 USD)

1. **Vecteur et covecteur.** La lentille R transporte un vecteur du flux ; le poids d'une sonde est un covecteur. La lecture
   R (ce que la direction fait dire) se fait donc sur la **différence des moyennes des classes** ; le poids de la sonde est
   lu par la lentille S seulement (`c · K_L …` prend bien un covecteur) ; la lecture R du poids est rapportée à part, sans
   critère. Les mesures A1 à A3 (lecture S du poids) ne changent pas.
2. **Positions.** Les lentilles ne sont ajustées qu'à partir de la position 16 : chaque invite est rendue par le gabarit de
   conversation du modèle et la position lue (dernier jeton) doit être ≥ 16, sinon l'exemple est écarté et compté.
3. **Règle de lecture, écrite d'avance** : une lecture par lentille **peut ajouter un soupçon, jamais blanchir une sonde**.
   « A1 non retrouvée » se lit « l'instrument ne voit pas une fuite plantée à cette profondeur », pas « pas de fuite ».
   Couches lues (8, 14, 20, 26 sur 36) : d'après les auteurs, la lecture S brute est noyée par les jetons pivots après la
   couche 8 ; les lectures centrées-réduites du catalogue (`_z`) sont donc celles du critère, les brutes rapportées à côté.
4. **Antériorité** : lire un poids de sonde par projection sur le vocabulaire est une technique ancienne (article de la
   lentille J, cité par le lecteur) : le volet A ne revendique rien ; il mesure si l'instrument sert.

## 5. Lignes de GO proposées (remplacent celles de la v1 pour le volet B)

| objet | plafond | échéance |
|---|---|---|
| **Volet A** — inchangé (v1 § 6), avec les amendements du § 4 | **10 USD** | 2026-11-30 |
| **Volet B** — reproduction sur `meta-llama/Llama-3.1-8B-Instruct`, en deux tranches sous un seul plafond : **B-α** (lecture contre pilotage et ablation, lentilles publiques de Neuronpedia sous licence Llama 3.1, une RTX 4090 ≤ 0,90 USD/h, au plus 12 USD) puis, après compte rendu à la mère, **B-β** (lentilles S et R ajustées sur 1 000 documents, lectures aux activations, une H100 de 80 Go ≤ 3,00 USD/h, repli A100 de 40 Go, au plus 68 USD) ; aucune H200 ; aucun appel de modèle ; texte gelé contre-lu et scellé avant chaque tranche ; destruction par identifiant ; aucune machine avant le feu de la mère | **80 USD** | 2026-11-30 |
| *variantes* : B-α seule, **12 USD** ; économe (sans notre lentille R), **60 USD** | | |

Décision : accorder B en deux tranches (80), la variante économe (60), ou B-α seule (12). Recommandation : deux tranches,
confiance 0,6 ; à défaut B-α seule, qui répond déjà à « la lecture tient-elle sur notre modèle ». Pas de défaut sous
48 heures : c'est une dépense.

## 6. Réserves

- Compatibilité du format des fichiers de Neuronpedia avec `load_lens`, et portabilité à Llama : **par lecture seulement** ;
  le refus du classifieur sur l'exécution locale (v1 § 7) tient toujours, non contourné.
- Les pourcentages du banc de concepts et l'erreur d'échantillonnage à 64 documents sont repris de la note du lecteur
  (niveau citation, R7) ; je ne les ai pas rouverts dans leurs sources.
- Les valeurs de B-7 viennent du fichier publié `causal_lens_qwen3-8b.json` (`8904c4d3…`), relues à 13:16 UTC.
- Ce texte n'est pas contre-lu (R2) : la contre-lecture porte sur le texte gelé de chaque tranche.
- Nœuds inchangés (v1 § 7), plus : tout emploi de la base de descriptions de Transluce (licence non vérifiée).
