# Proposition B — Diversifier les idées des proposeurs sans affaiblir la garde

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé implicite | Statut réel | Commentaire |
|---|---|---|---|
| P1 | La corrélation des 11 lois en G1 provient d'un défaut de diversité *des proposeurs* (consignes, contextes). | **HYPOTHÈSE** | Le verdict (RAPPORTÉ) dit « K1 ignore z1 ; toute loi qui ajoute z1 bat nettement K1 ». Dans un monde à 2 traits réels et un seul constat fort au-delà de K1, même des proposeurs parfaitement diversifiés convergeraient vers z1. Le manque de diversité pourrait être *du monde*, pas *du mécanisme*. |
| P2 | Des mécanismes de diversification (consignes, rôles, regroupement) *augmenteront* le nombre d'idées *distinctes et correctes* promues. | **HYPOTHÈSE** | La diversification peut aussi pousser vers des idées fausses ou vers la classe non couverte du nul (voir §1 des faits : « brèche hors classe établie, 24/24 »). Le gain net n'est pas établi. |
| P3 | La mesure de diversité peut être définie sur le contenu des lois (formes, traits, distance entre prédictions) indépendamment de la vérité. | **HYPOTHÈSE** | La diversité syntaxique (formes, traits) ne garantit pas la diversité sémantique (prédictions distinctes sur les issues). Des lois syntaxiquement différentes peuvent être fonctionnellement identiques. Inversement, des lois de même forme sur des traits différents peuvent être sémantiquement distinctes. |
| P4 | Le regroupement des doublons au sein d'une génération est réalisable par un critère mécanique, sans modèle. | **HYPOTHÈSE** | Le verdict ne décrit aucune distance mécanique entre fiches. La grammaire fermée (6 formes, coefficients bornés ±4) *permet* de définir une distance prédictive, mais le seuil de doublon n'a pas été testé. |
| P5 | Le blocage en G2 (0/12 promues) résulte de la saturation de la niche « ajouter z1 » et non d'un plafond du monde S-V1. | **RAPPORTÉ comme lecture du verdict** : « 12 refus sur 12 en génération 2 ne disent rien d'une capacité à progresser au-delà ». Le monde S-V1 n'a que 2 traits réels et 2 sous-populations ; il est possible qu'il ne contienne *aucun* constat supplémentaire détectable à 200 tirages et seuil ≈ 6,09. |
| P6 | Un monde « plus riche » (plusieurs traits cachés, interactions, effets de tailles variées) rend la diversité *observable* et récompensable. | **HYPOTHÈSE** | C'est plausible mais la richesse du monde n'entraîne pas mécaniquement que des proposeurs à un appel chacun exploreront plus d'une direction. |
| P7 | Les 50 mondes neufs (RAPPORTÉ, GO-2026-11-12-05) seront disponibles avant la prochaine course. | **RAPPORTÉ** comme décision prise ; leur statut réel (générés ? validés ?) n'est pas dans les faits. |

---

## (b) Expériences décisives, chacune en duel H_A / H_B

### Exp. 1 — La diversité-source : monde pauvre vs. monde riche

**Question tranchée** : le facteur limitant de la diversité est-il le monde ou le proposeur ?

| | H_A : facteur = monde | H_B : facteur = proposeur |
|---|---|---|
| Prédiction | Sur un monde riche (≥ 5 traits réels, ≥ 2 interactions), les *mêmes* proposeurs (mêmes consignes, même vue, un appel) produisent des lois couvrant ≥ 3 constats distincts (clusters prédictifs, voir métrique ci-dessous). Sur S-V1, ≤ 1. | Sur le monde riche, les mêmes proposeurs convergent encore sur ≤ 1 constat ; il faut modifier le mécanisme. |
| Métrique | Nombre de clusters prédictifs parmi les lois *promues*, mesuré par distance L1 entre vecteurs de prédiction sur un jeu commun de 1 000 épisodes synthétiques (traits tirés de la distribution du monde), clustering hiérarchique, seuil de coupure préenregistré à d_L1 = 0,05. |
| Contrôle négatif | Même monde riche, archive K1 remplacée par K1-riche qui couvre déjà *tous* les traits réels : aucune loi ne devrait être promue (le nul les contient). Si des lois passent, le juge fuit. |
| Seuil | ≥ 3 clusters prédictifs distincts parmi les promues (monde riche) vs. ≤ 1 (S-V1), sur ≥ 3 graines. |
| Falsifie H_A | Si ≤ 1 cluster sur le monde riche aussi. |
| Falsifie H_B | Si ≥ 3 clusters sans changer les proposeurs. |
| Coût | 2 mondes × 3 graines × 2 proposeurs × 1 appel = 12 appels proposeurs. Au coût v67 (~0,05 USD/appel proposeur, RAPPORTÉ : 1,99 USD / 46 appels totaux, 4 de proposeurs ≈ 0,17 USD pour 4 appels, soit ~0,04 USD/appel), **≈ 0,50 USD modèles** (illustratif). Machine ≈ 0,15 USD (illustratif). |

---

### Exp. 2 — Regroupement des doublons : réduction du gaspillage vs. perte de puissance

**Question tranchée** : le regroupement intra-génération réduit-il le nombre de promotions redondantes sans supprimer de découverte vraie ?

| | H_A : le regroupement aide | H_B : le regroupement supprime des vrais positifs |
|---|---|---|
| Prédiction | Après regroupement (une seule fiche par cluster prédictif, la plus grande e-valeur), le nombre de constats distincts promus est identique, le nombre de fiches promues baisse. | Le regroupement rejette une fiche qui porte un constat *absent* des autres fiches du cluster (faux regroupement). |
| Métrique | (i) Constats distincts promus (clusters prédictifs, même distance que Exp. 1) ; (ii) fiches promues ; (iii) taux de faux regroupement = nombre de fiches rejetées par le regroupement dont le constat n'apparaît dans aucune autre fiche promue, vérifié par l'oracle a posteriori. |
| Contrôle négatif | Exécution sans regroupement sur le même monde et la même graine : baseline. |
| Design | Monde riche, ≥ 3 graines. Chaque graine exécutée *deux fois* : avec et sans regroupement. Même tirage des proposeurs (même prompt, même seed API si disponible, sinon ≥ 5 graines pour moyenner). |
| Seuil de coupure du regroupement | d_L1 = 0,05 (même que Exp. 1), préenregistré. |
| Falsifie H_A | Taux de faux regroupement > 0 sur ≥ 1 graine. |
| Falsifie H_B | Taux de faux regroupement = 0 sur toutes les graines, et fiches promues < baseline sur toutes. |
| Coût | 2 conditions × ≥ 5 graines × 2 proposeurs = 20 appels. **≈ 0,80 USD** (illustratif). |

---

### Exp. 3 — Consigne de diversité : gain réel ou Goodhart ?

**Question tranchée** : une consigne explicite de diversité (« proposez des lois qui diffèrent des lois de l'archive par les traits et les formes utilisés ») augmente-t-elle les constats distincts *vrais* ou augmente-t-elle les promotions dans la classe non couverte du nul ?

| | H_A : gain réel (constats vrais ↑) | H_B : Goodhart (promotions non couvertes ↑) |
|---|---|---|
| Prédiction | Plus de clusters prédictifs parmi les lois promues *et* confirmées par l'oracle. | Plus de lois promues mais taux de faux positifs oracle ↑ (lois promues mais fausses selon l'oracle), ou lois promues par brèche hors classe. |
| Métrique | (i) Clusters prédictifs vrais (promus ET confirmés oracle) ; (ii) taux de faux positifs oracle ; (iii) nombre de promotions dont la e-valeur dépasse le seuil mais dont la forme est une recombinaison par morceaux, produit ou composition (classe non couverte, détection a posteriori par l'oracle). |
| Contrôle | Même monde, même graine, consigne neutre (la consigne actuelle sans mention de diversité). |
| Falsifie H_A | Clusters prédictifs vrais ≤ baseline, ou taux de faux positifs oracle > baseline + 0,05. |
| Falsifie H_B | Clusters prédictifs vrais > baseline ET taux de faux positifs oracle ≤ baseline. |
| Coût | 2 consignes × ≥ 5 graines × 2 proposeurs = 20 appels. **≈ 0,80 USD** (illustratif). |

**Risque identifié** : la consigne de diversité peut implicitement informer le proposeur qu'il existe d'autres constats (fuite partielle de structure). Mitigation : la consigne ne mentionne ni le nombre de traits, ni les interactions ; elle porte uniquement sur les formes et les traits *de la grammaire publique*.

---

### Exp. 4 — Nombre d'appels : un appel vs. plusieurs appels indépendants par proposeur

**Question tranchée** : à budget apparié, plusieurs appels indépendants (avec température > 0, ou prompts légèrement variés) produisent-ils plus de constats distincts qu'un seul appel avec plafond de 6 lois ?

| | H_A : plusieurs appels diversifient | H_B : les appels supplémentaires sont redondants |
|---|---|---|
| Prédiction | 3 appels × 2 lois > 1 appel × 6 lois en clusters prédictifs promus. | ≤ même nombre de clusters. |
| Métrique | Clusters prédictifs promus (même métrique). |
| Contrôle | 1 appel × 6 lois, même proposeur, même monde, même graine (ou ≥ 5 graines moyennées). |
| Coût | Budget apparié : 3 appels × 2 lois = même nombre de tokens environ. **≈ 0,40 USD** par condition × 2 conditions (illustratif). |
| Falsifie H_A | Clusters ≤ baseline sur ≥ 4 graines sur 5. |
| Falsifie H_B | Clusters > baseline sur ≥ 4 graines sur 5. |

---

### Exp. 5 — Mesure de diversité : la distance prédictive L1 capture-t-elle les constats distincts ?

Ceci est une **calibration d'instrument**, pas une expérience sur l'organisme.

| | H_A : d_L1 sépare les constats | H_B : d_L1 échoue |
|---|---|---|
| Prédiction | Sur un monde dont l'oracle connaît K constats distincts, les K lois oracle correspondantes forment K clusters à seuil 0,05. | Elles forment < K ou > K clusters. |
| Métrique | Nombre de clusters retrouvés vs. K. |
| Construction | L'oracle génère K lois (une par constat), plus K lois synonymes (même constat, forme différente) et K lois adversariales (constat différent, prédictions proches). Jeu de 1 000 épisodes synthétiques. |
| Falsifie H_A | Nombre de clusters ≠ K. |
| Falsifie H_B | Nombre de clusters = K sur ≥ 3 mondes. |
| Coût | Aucun appel modèle : calcul pur. **≈ 0,01 USD** (illustratif). |

---

## (c) Instruments nommés dans la question — mesure minimale de fonctionnement

### C1. Regroupement des doublons (clustering prédictif intra-génération)

- **Taux de détection** : proportion de paires de fiches portant le même constat (vérifié oracle) et placées dans le même cluster. Cible : ≥ 0,90.
- **Taux de fausses alertes** : proportion de paires portant des constats distincts (vérifié oracle) mais placées dans le même cluster. Cible : ≤ 0,05.
- **Cas honnêtes appariés** : paires générées par l'oracle sur un monde connu : K paires synonymes (même constat, formes variées), K paires distinctes.
- **Vérification mécanique à battre** : clustering naïf sur la forme syntaxique seule (même forme = même cluster). Le clustering prédictif doit avoir un F1 strictement supérieur.

### C2. Mesure de diversité préenregistrable (distance prédictive L1)

- **Taux de détection** : proportion de constats distincts correctement séparés. Cible : ≥ 0,85 sur les mondes oracle.
- **Taux de fausses alertes** : proportion de paires synonymes classées comme distinctes. Cible : ≤ 0,10.
- **Cas honnêtes appariés** : voir Exp. 5 ci-dessus.
- **Vérification mécanique à battre** : diversité syntaxique naïve (nombre de formes distinctes parmi les promues). La diversité prédictive doit mieux corréler (rang de Spearman) avec le nombre de constats oracle.

### C3. Consigne de diversité

- **Taux de détection** : proportion de constats du monde que le proposeur inclut dans ses 6 lois, sur un monde où l'oracle en connaît K ≥ 3. Cible : ≥ 2/K (illustratif, au moins deux constats couverts).
- **Taux de fausses alertes** : proportion de lois proposées qui sont fausses (rejetées par l'oracle). Cible : ≤ baseline + 0,05.
- **Cas honnêtes appariés** : même proposeur, même monde, consigne neutre vs. consigne diversité.
- **Vérification mécanique à battre** : tirage aléatoire de 6 lois dans la grammaire (uniformément sur les formes et les coefficients). La consigne doit produire un taux de détection strictement supérieur.

---

## (d) Ancrage matériel

| Poste | Détail | Coût estimé |
|---|---|---|
| **Modèles (proposeurs)** | Kimi k3.1-pro et Gemini-4-Argon, par relais local. Exp. 1–4 : ~72 appels proposeurs au total. Au coût v67 (~0,04 USD/appel, illustratif), **≈ 2,90 USD**. | illustratif |
| **Modèles (oracle/vérification)** | Aucun modèle requis pour la mesure de diversité ni le regroupement (mécaniques). L'oracle est l'expérimentateur humain ou le script qui connaît la loi plantée. | 0 USD |
| **Calcul machine** | Clustering L1 sur 1 000 épisodes × ≤ 50 lois : négligeable. Orchestrateur, gardien, juge : identiques à v67. ≈ 0,27 USD par course (RAPPORTÉ). 5 courses (Exp. 1–4 + calibration) × 3 graines ≈ **4 USD**. | illustratif |
| **Mondes** | 50 mondes neufs (RAPPORTÉ, GO-2026-11-12-05). Coût de génération déjà approuvé et non inclus ici. Exp. 1–4 requièrent ≥ 3 mondes riches et S-V1. |  |
| **Total modèles + machine** | **≈ 7 USD** | illustratif |
| **Modèles ouverts** | Si N-045 (bon marché d'abord) exige un test avec des modèles ouverts : Mistral Large ou Qwen-2.5-72B via API (coût comparable ou inférieur). Aucun modèle ouvert n'est requis par le protocole actuel, mais un pilote A/A (N-045) sur un modèle ouvert comme baseline de coût serait pertinent. | |
| **Temps humain** | Préenregistrement : ~2 h. Vérification oracle a posteriori pour Exp. 3 : ~1 h par monde (K constats à vérifier manuellement). | non chiffré |

---

## Synthèse des recommandations ordonnées par priorité

1. **Calibrer l'instrument d'abord** (Exp. 5) : la distance prédictive L1 est la brique commune au regroupement et à la mesure de diversité. Si elle échoue à seuil 0,05, tout le reste est construit sur du sable. Coût : quasi nul.

2. **Séparer monde et proposeur** (Exp. 1) : avant d'ajouter de la machinerie aux proposeurs, vérifier que le facteur limitant n'est pas S-V1. Si H_A (facteur = monde) est confirmée, le passage aux mondes riches suffit à court terme.

3. **Regroupement** (Exp. 2) : mécanisme le plus sûr car purement mécanique, pas de risque de fuite, pas de Goodhart. À tester dès que l'instrument est calibré.

4. **Appels multiples** (Exp. 4) : peu coûteux, aucun changement de consigne, pas de risque de fuite. Si H_A confirmée, c'est le levier le moins intrusif.

5. **Consigne de diversité** (Exp. 3) : le mécanisme le plus risqué (Goodhart, fuite implicite de structure). À ne tester qu'après les quatre précédents, et uniquement si le déficit de diversité persiste sur monde riche.

**Ce que je ne recommande pas** : toute forme de « récompense de la nouveauté » qui entrerait dans la vue des proposeurs sous forme de score ou de classement, car cela violerait N-053 (aucun score de juge dans un signal de sélection d'un agent) ou créerait un gradient vers la classe non couverte du nul.

FIN-DE-CELLULE