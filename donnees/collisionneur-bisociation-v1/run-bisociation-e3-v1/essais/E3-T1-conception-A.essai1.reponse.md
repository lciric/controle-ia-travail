# Cellule A — Tour III.1 — recombinaison bisociative à deux espaces

## 0. Pièces reçues

Les quatre pièces sont présentes et non coupées. Pièce D est bien limitée aux lignes 29-33 : les notions « mémoire qui refuse les redites » et « héritage récompensé » que la question lui attribue **n'y figurent pas** (session-depot le dit déjà ; je n'ajoute rien). Pièce C est le préambule d'une course *défensive* (sondes, HELIOS) : son gabarit n'a pas de champ « méthode » ni « test de mort » mais « livrables », « critère de mort », « vis-à-vis » ; la question cite le gabarit de mémoire, pas mot pour mot.

---

## (a) Ce que la question suppose sans que ce soit établi

| # | Présupposé | Statut | Remarque |
|---|---|---|---|
| A1 | « La forme corrigée a été réfutée. » | **OBSERVÉ-NON-AUDITÉ** | Pièce B se déclare « régime exploratoire, rien d'opposable », sans contre-lecture (§ 9, R2). La décision R-527 (pièce A, en-tête) s'en est servie comme défaut, ce qui est une décision d'ingénierie, pas une réfutation auditée. |
| A2 | « Elle ne cible pas l'éloignement des paires. » | **RAPPORTÉ** (B § 3) | C'est le point le plus solide de B : audit descriptif mais mécaniquement expliqué (pour une paire, det = q_i²q_j²((1+γ)² − cos⁴) ; pénalité 0,6 % à cos = 0,28 ; corrélation de rang 0,977 entre l'ordre glouton et q). |
| A3 | « La proximité conceptuelle est l'ingrédient manquant. » | **HYPOTHÈSE** | Dans les mondes de B, le partage d'opérateur est déjà une **condition d'entrée** (étage commun : étiquette partagée, « la plus rare », B § 5). Ce qui a gagné dans ces mondes, c'est (i) l'éloignement de domaine grossier (b_eloigne +11,9 / +6,6) et (ii) l'évitement des moyeux (d1, +17,0 quand les moyeux dominent). Rien dans B ne montre qu'une proximité conceptuelle *continue* ajoute à l'étiquette partagée *binaire*. Le candidat le plus proche est d1_inv (+5,3 / +4,8), qui pondère par la rareté, pas par une similarité vectorielle. |
| A4 | Les deux espaces sont séparables sur des fiches réelles. | **HYPOTHÈSE** | B § 2.3 : dans ses mondes, « les mots de domaine […] ne franchissent jamais un domaine ». Dans une littérature réelle, les mots de méthode traversent les domaines et les mots de domaine aussi (un « processus de richesse » est à la fois concept et marqueur de finance). Aucune pièce ne mesure cette séparabilité. |
| A5 | Le mot de Lazar : « maximiser le volume […] en même temps qu'on **minimise** leur proximité conceptuelle ». | **RAPPORTÉ** | Lu à la lettre, il demande des parents *loin* en concepts ; l'hypothèse de travail de la question demande des parents *proches* en concepts. L'une des deux formulations est inversée (transcription ou intention). À trancher par Lazar **avant** le préenregistrement, sinon le test n'a pas de signe. Je conçois ci-dessous pour « proches en concepts », en gardant le signe comme paramètre (α < 0 rend l'autre lecture). |
| A6 | « Mettre la proximité dans l'objectif » diffère de « filtre après coup ». | **HYPOTHÈSE** | Vrai seulement si la proximité conceptuelle est graduée (plusieurs opérateurs partagés, rareté, poids). Si elle reste binaire, objectif et filtre tirent le même sous-ensemble. |
| A7 | Le seuil d'adoption +12 points (B, préenregistrement) est la bonne règle. | **HYPOTHÈSE** | B § 7.3 le critique lui-même : à 10-20 % de précision, +12 = ×1,6 à ×2,2 ; même l'a priori idéalisé ne l'atteint pas dans les deux mondes. |
| A8 | Trois témoins suffisent (stratifié, v6.3, Swanson). | **HYPOTHÈSE** | Il manque le témoin le moins cher qui gagne le plus : **b_eloigne** (strates dissemblables d'abord, +11,9 / +6,6, B § 1). Toute machinerie à deux espaces doit battre ce diagnostic à une ligne, sinon elle ne vaut pas son coût. |
| A9 | Le tirage de B mesure la recombinaison. | **RAPPORTÉ** (B § 6) | Il mesure les paires envoyées à la fusion, pas la qualité des filles. |

---

## (b) Expériences décisives

### Préalable : objet proposé (point 1 de la question)

**Diagnostic**, à partir de B § 3 (RAPPORTÉ) : dans un tirage déterminantal glouton, la diagonale gouverne et les termes croisés n'agissent qu'à cos proche de 1. « Minimiser le produit scalaire des domaines » **est contenu** dans « maximiser le volume » d'un ensemble d'articles, mais à un ordre de grandeur inopérant (pénalité 0,6 % à cos = 0,28). Et la sélection porte sur des **articles** alors que la fusion consomme des **paires** : un ensemble d'articles divers contient toutes ses paires, proches comprises. Deux remèdes exclusifs : rendre le noyau tranchant (exp(−cos/τ), non testé selon B § 6) ou déplacer l'ensemble de base vers les paires et mettre ce qu'on veut dans la diagonale.

**Forme recommandée (O-paires)** — ensemble de base = paires valides (pont non vide, compatibles, jamais fusionnées : l'étage commun de B conservé). Pour une paire p = (i, j) :

- qualité : w_p = q_i q_j · c_ij^α · (1 − s_ij)^β, avec s_ij = ⟨d_i, d_j⟩ (cosinus de domaine), c_ij = ⟨k_i, k_j⟩ où k est le vecteur de concepts normalisé et pondéré par la rareté inverse (un moyeu pèse peu) ; α = β = 1 par défaut ;
- traits de diversité : φ_p = [indicatrice de la strate (paire de domaines estimés) ; λ·(e_i + e_j)] ;
- noyau : L_pq = w_p ⟨φ_p, φ_q⟩ w_q + γ δ_pq.

Propriétés : L est une matrice de Gram pondérée plus γI, donc définie positive pour γ > 0 ; Cholesky de pièce A s'applique telle quelle ; déterminant bien défini. Coût : |P| ≤ n(n−1)/2 = 780 pour n = 40 (B § 5) ; glouton de taille k sur 780 éléments avec Cholesky incrémentale, négligeable sur processeur. Ce qu'il maximise exactement : Σ_{p∈Y} 2 log w_p + log det(Φ_Y Φ_Yᵀ + …), c'est-à-dire *qualité à deux espaces des paires* **plus** *volume des strates occupées* (une paire par strate à λ = 0 et γ → 0, et répulsion entre paires partageant une fiche à λ > 0).

Ce qui le distingue du tirage déterminantal classique : (1) l'ensemble de base est l'espace des paires ; (2) le rapport concept/domaine est dans la **diagonale** (là où le glouton regarde) ; (3) la répulsion porte sur les strates, non sur les cosinus de domaine. Le terme « à part » demandé par la question est donc (1 − s_ij)^β dans w_p : oui, il faut un terme à part, parce que le volume ne le fournit pas à ces cosinus.

Propriété utile pour le test : la famille **contient les témoins** comme cas limites — α = β = 0 ≈ stratifié avec préférence de qualité ; α = 0, β grand ≈ b_eloigne ; c_ij = rareté de l'étiquette commune, β = 0 ≈ d1_inv (B § 1). Le test devient une ablation à deux boutons, ce qui est ce que demande « est-ce l'ingrédient manquant ».

Options écartées : (O-Schur) L = diag(q)(S_concept ⊙ (1 − S_dom))diag(q) — c'est le « noyau fautif » de pièce A, non semi-défini positif ; réparé par γ minimal, il repousse ce qu'il visait (B § 4, bras (e), −5,7). (O-somme) S_concept ⊕ S_dom reste semi-défini positif mais récompense *les deux* proximités, à l'opposé du but. (O-Swanson guidé) marche biparti fiches × concepts, pas ∝ rareté(c)·(1 − s_ij) : c'est un tirage **indépendant** ∝ w_p sans répulsion ; je le garde comme comparateur E2, pas comme forme.

Confiance : haute sur le diagnostic (c'est l'audit de B), moyenne sur le remède, faible sur l'hypothèse A3 qu'il adresse.

### E1 — La proximité conceptuelle graduée est-elle l'ingrédient manquant ?

- **H_A** : à étage commun identique, O-paires avec α = 1 bat O-paires avec α = 0 d'au moins +4 points de précision (illustratif) dans les mondes à ponts conceptuels gradués, intervalle à 95 % au-dessus de +1.
- **H_B** : le gain est ≤ +1,5 point (intervalle contenant 0) : ce que « concept » apporte est déjà dans « étiquette partagée + rareté » (d1_inv).
- **Métrique** : précision des vrais ponts parmi les 12 paires tirées (k = 4 × 3 générations), 400 mondes par condition, écart apparié, 2 000 rééchantillonnages — la mesure de B § 1, inchangée.
- **Mondes étendus** (point 3) : mêmes 8 domaines × 5 articles ; chaque article porte **plusieurs** opérateurs latents (3 à 5, illustratif) avec rareté variable ; vérité à trois classes : *pont conceptuel vrai* (champs différents, ≥ 2 opérateurs latents non-moyeux partagés ou 1 opérateur rare, contraintes compatibles), *faux pont* (étiquette commune homonyme, opérateurs latents disjoints), *pont de surface* (même champ ou mots de domaine partagés, opérateur partagé — valide pour le filtre, mais non compté comme pont bisociatif). Niveaux d'observation du lexique conservés (0,90 / 0,70 / 0,45).
- **Contrôle négatif 1 (concept nul)** : vecteurs de concepts permutés entre fiches, vérité inchangée ; α = 1 doit valoir α = 0 à ±1,5 (placebo de B § 2.1). Un gain ici = fuite ou artefact → H_A falsifiée par artefact.
- **Contrôle négatif 2 (concept inversé)** : ponts plantés entre paires conceptuellement *éloignées* qui partagent une étiquette de surface ; exigence stricte de B § 7.2 : Δ_inversé − Δ_normal < 0 avec intervalle sous 0. Si Δ ne baisse pas, la méthode ne cible pas la proximité conceptuelle (même défaut que (a) pour l'éloignement, B § 2.2).
- **Ce qui falsifie** : H_A tombe si l'écart α=1 − α=0 est sous +1,5 **ou** si le contrôle 2 ne baisse pas. H_B tombe si l'écart dépasse +4 avec contrôles passés. Issue intermédiaire (+1,5 à +4) : « non concluant, puissance insuffisante », pas d'adoption.
- **Puissance** (dérivée, illustrative) : les demi-largeurs de B (≈ 1,5 point à 400 mondes) donnent un écart-type apparié ≈ 15 points par monde ; détecter +4 à 80 % de puissance demande ≈ 110 mondes ; 400 mondes couvrent +2,5. Pour un effet de +1,5, il faudrait ≈ 800 mondes.
- **Seuil d'adoption dans le pôle** (distinct du seuil de détection) : relatif, ×1,3 sur le stratifié **et** ≥ b_eloigne − 2 points dans les deux mondes de décision (illustratif ; répond à B § 7.3 et à A8).

### E2 — La répulsion déterminantale ajoute-t-elle quelque chose au tirage pondéré ?

- **H_A** : le glouton déterminantal sur paires bat le tirage indépendant ∝ w_p (marche de Swanson guidée) d'au moins +3 points de précision, et par ≥ 0,15 sur « strates distinctes par paire » (B donne 0,998 pour (b), 0,707 pour (a)).
- **H_B** : égalité à ±1,5 : la machinerie de volume n'apporte rien au-delà de la pondération ; on garde le tirage ∝ w_p, plus simple.
- **Contrôle** : monde sans pont (placebo) — les deux doivent être égaux au placebo.
- **Ce qui falsifie** : H_A tombe si l'écart est sous +1,5 ; H_B tombe sinon. Dans les deux cas, on apprend où loger le coût.

### E3 — Items contre paires (pourquoi (a) a perdu)

- **H_A** : la perte de la forme corrigée vient de l'ensemble de base (articles) ; un noyau *tranchant* sur articles, exp(−s_ij/τ) à τ = 0,1 (illustratif), reste au niveau de l'uniforme (écart à (c) dans [−1,5 ; +1,5]).
- **H_B** : la perte vient de la platitude de cos² ; le noyau tranchant sur articles rejoint b_eloigne (≥ +8 sur le stratifié).
- **Ce qui falsifie** : si le noyau tranchant gagne, H_A tombe et O-paires n'est pas nécessaire (il suffit de régler τ) ; s'il stagne, H_B tombe et le déplacement vers les paires est justifié.

### E4 — Représentation des concepts : capte-t-elle le concept et non le domaine ? (point 2)

- **Options** : (R1) liste fermée d'opérateurs et de structures déclarée par le proposeur dans un champ nouveau du gabarit, chaque entrée **ancrée** à un passage de la fiche (symbole, formule, nom de théorème, citation) vérifié par programme ; (R2) étiquetage par un modèle tiers, **hors boucle**, aveugle au champ domaine, scellé avant tirage (conforme au critère « étiquetage hors boucle » de l'arbitre) ; (R3) extraction par programme (motifs, symboles, références). Recommandation : R1 comme source du vecteur, R3 comme vérification mécanique obligatoire (une entrée non ancrée fait refuser la fiche, comme `valider_fille` refuse une prédiction identique à un parent, pièce A), R2 comme instrument de mesure de R1 seulement, jamais comme entrée du tirage. Confiance moyenne.
- **Contre la manipulation** : vecteur normalisé (comme `vecteurs_domaine`, pièce A : 1/√|étiquettes|) et pondéré par rareté inverse — déclarer vingt concepts dilue ; déclarer un concept rare non ancré est refusé mécaniquement ; une étiquette présente dans plus de 25 % du vivier (le taux de moyeu de B § 5) sort du vecteur.
- **H_A** : un classifieur linéaire « domaine à partir du vecteur de concepts » reste ≤ hasard + 0,10 (hasard = 1/8 sur 8 domaines, mondes de B), **et** la détection des paires à opérateur latent partagé (c_ij au-dessus d'un seuil fixé sur un jeu de calibrage) atteint ≥ 0,70 à fausses alertes ≤ 0,10 (illustratif, aligné sur le niveau « moyen » du lexique de B).
- **H_B** : le vecteur est un proxy du domaine (classifieur ≥ 0,50) **ou** la détection reste sous 0,50 : alors O-paires ne fait que doubler le terme de domaine, et E1 est non interprétable.
- **Contrôle négatif** : vecteurs de concepts permutés → classifieur au hasard ; sinon, fuite par la forme du champ.
- **Sous-test manipulation** : fiches « gonflées » plantées (20 concepts, ou un concept rare non ancré) ; H_A' : leur taux de tirage ≤ honnêtes + 2 points ; H_B' : > +5 points, la représentation est manipulable et le champ doit passer par R2 ou R3 seuls.

### E5 — Passage aux vraies fiches de la course 2 (lecture sans sélection, N-053)

- **Protocole** : toutes les survivantes de la course 2 ; les quatre bras (stratifié, v6.3, d1, O-paires) tirent leurs paires **avant toute fusion**, liste scellée ; chaque paire est fusionnée par le même modèle avec la même consigne (`consigne_fusion`, pièce A) ; l'identité du bras est retirée des dossiers `paire-NN` avant jugement ; **toutes** les filles, refusées comprises, sont comptées (archive complète, pièce D § 6) ; la lecture se fait sur le fichier scellé, par bras, avant qu'un verdict de promotion soit connu.
- **H_A** : la part de filles recevables (`valider_fille` sans motif) puis promues est plus élevée pour O-paires que pour le stratifié d'au moins +10 points (illustratif).
- **H_B** : égalité à ±5 : le tirage ne change pas la fusion ; l'ingrédient limitant est le fuseur, pas la paire.
- **Contrôle** : paires du stratifié rejouées deux fois avec graines différentes — l'écart entre ces deux répétitions borne le bruit de fusion ; un écart inter-bras sous ce bruit ne compte pas.
- **Ce qui falsifie** : H_A tombe si l'écart est sous le bruit de fusion ; H_B tombe sinon. Dans les deux cas la ligne « le test de B ne dit rien des filles » (A9) est levée.

---

## (c) Instruments nommés dans la question : mesure minimale

| Instrument | Détection / fausses alertes à mesurer | Cas honnêtes appariés | Vérification mécanique à battre |
|---|---|---|---|
| Objectif à deux espaces (O-paires) | Précision des vrais ponts ; pièges tirés : moyeux, homonymes, contraintes incompatibles (B § 1 : (b) 0,385 / 0,038 / 0,262 ; (d1) 0,122 / 0,040 / 0,251, RAPPORTÉ) | Mêmes 400 mondes, mêmes 40 candidats, même étage commun | **b_eloigne** (+11,9 / +6,6) et d1_inv (+5,3 / +4,8) : deux lignes de code chacune |
| Noyau corrigé v6.3 (témoin) | Déjà mesuré : −4,8 / −2,2 (RAPPORTÉ) | — | Sert de plancher ; ne pas réoptimiser |
| Stratifié (témoin) | Déjà mesuré : 0,203 / 0,127 | — | Témoin de référence |
| Marche de Swanson d1 (témoin) | 0,239 / 0,165 ; sensible au taux de moyeux (−0,2 à 0,10, +10,1 à 0,50, B § 4) | Balayage du taux de moyeux 0,10 / 0,25 / 0,50 | À battre **à 0,10**, là où son avantage disparaît |
| Champ « concepts » déclaré (R1) | Rappel des opérateurs latents plantés ; parasites ; part de fiches gonflées tirées | Fiches honnêtes vs fiches gonflées, même domaine et même q | Extraction par motifs (R3) au niveau « bien » du lexique (0,90 de couverture) : si R1 ne bat pas R3, le champ est inutile |
| Étiqueteur tiers hors boucle (R2) | Accord avec les opérateurs latents (mondes) ou avec deux annotateurs humains (fiches réelles) ; taux d'étiquettes qui sont des mots de domaine | Fiches dont le domaine a été caviardé vs non caviardé | R3 ; et le classifieur de séparabilité (≤ hasard + 0,10) |
| Test de séparabilité | Exactitude « domaine depuis concepts » ; détection des paires à opérateur partagé à fausses alertes ≤ 0,10 | Vecteurs réels vs vecteurs permutés | Hasard + 0,10 ; vecteur de domaine lui-même (qui doit, lui, classer le domaine) |
| Mondes à ponts plantés étendus | Cosinus de domaine validés avant méthode (B : 0,54 / 0,28 / 0,03) ; cosinus de concepts validés de même (intra-pont vs hors-pont) ; plafond oracle (B : 0,750 / 0,487) | Graines de validation distinctes des graines de décision | Le générateur doit laisser gagner b_eloigne et d1 comme dans B, sinon il est cassé |
| Filtre de compatibilité (pièce A) | Rappel 0,57-0,60, rejets à tort 4-5 % (B § 5, RAPPORTÉ) ; il laisse passer 0,25-0,27 de paires vraiment incompatibles | Inchangé entre bras | Non réoptimisé ici (sinon confusion des causes) |

---

## (d) Ancrage matériel

- **Tirage et mondes** : processeur seul, bibliothèque standard, comme B (run complet 93 s pour 4 000 mondes, RAPPORTÉ B § 5). O-paires multiplie l'ensemble de base par ≈ 20 (780 paires contre 40 articles) avec Cholesky incrémentale de taille ≤ k : ≤ 10 minutes pour 4 000 mondes (illustratif). E1 à E3 ensemble, avec contrôles : < 1 h de processeur (illustratif). Aucun appel de modèle.
- **Étiquetage hors boucle (R2) et séparabilité** : modèles ouverts connus de moi, hors pièces, disponibilité à vérifier : Qwen2.5-72B-Instruct, Llama-3.1-70B-Instruct. Pour 40 fiches × 3 étiquetages × ≈ 2 000 jetons ≈ 0,25 M jetons : < 1 $ par API ou < 1 h sur une carte de 80 Go en local (illustratif). Classifieur linéaire : négligeable.
- **E5 (course 2)** : le plafond par fusion existe dans la configuration (`plafond_recombinaison_usd`, pièce A) mais sa valeur n'est dans aucune pièce. Illustratif : 4 bras × 12 paires + 12 répétitions de contrôle = 60 fusions × ≈ 10 k jetons ≈ 0,6 M jetons ; 5 à 50 $ selon le modèle de fusion ; jugement aveugle en sus. Accès réseau et dépense : sur devis et GO, chez session-depot, comme la question l'exige.
- **Données réelles (étape 8 de B)** : non nécessaire pour E1-E4 ; nécessaire seulement si on veut situer le niveau d'observation réel du lexique. Hors de ce tour.

---

## Antériorité (point 4) — à vérifier sur PDF (R7)

- Décomposition qualité × diversité d'un noyau déterminantal, L_ij = q_i ⟨φ_i, φ_j⟩ q_j, et k-DPP : Kulesza & Taskar, 2012, *Determinantal Point Processes for Machine Learning* (Foundations and Trends in Machine Learning) ; Kulesza & Taskar, 2011, « k-DPPs: Fixed-Size Determinantal Point Processes » (ICML). C'est la forme que j'emploie ; ce qu'ils ne font pas : un ensemble de base de **paires** avec une qualité à deux espaces. Je ne connais pas de référence exacte pour cela : **zone vierge, donc question** (R8), pas trou.
- Découverte fondée sur la littérature : Swanson, 1986, « Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge » (Perspectives in Biology and Medicine) ; Swanson & Smalheiser, 1997, « An interactive system for finding complementary literatures » (Artificial Intelligence) — référence à vérifier pour le titre exact. Le schéma A-B-C est un filtre par terme intermédiaire, sans objectif de volume.
- Bisociation : Koestler, 1964, *The Act of Creation*. Deux « matrices » habituellement incompatibles reliées par un élément commun — c'est l'énoncé verbal des deux espaces, sans forme mathématique.
- Analogie comme structure relationnelle partagée entre domaines différents : Gentner, 1983, « Structure-Mapping: A Theoretical Framework for Analogy » (Cognitive Science). La plus proche antériorité conceptuelle de « loin en domaine, proche en structure ».
- Combinaisons atypiques : Uzzi, Mukherjee, Stringer & Jones, 2013, « Atypical Combinations and Scientific Impact » (Science) — mesure *a posteriori* sur les références, pas un opérateur de tirage.
- Évolution ouverte, nouveauté, qualité-diversité : Lehman & Stanley, 2011, « Abandoning Objectives: Evolution Through the Search for Novelty Alone » (Evolutionary Computation) ; Pugh, Soros & Stanley, 2016, « Quality Diversity: A New Frontier for Evolutionary Computation » (Frontiers in Robotics and AI) ; MAP-Elites, Mouret & Clune, 2015 — référence à vérifier. La grille par niches est l'analogue du stratifié ; aucune n'a de second espace de « concepts ».
- Programmation génétique : Koza, 1992, *Genetic Programming* (MIT Press) ; le croisement y opère sur des sous-arbres **structurellement compatibles**, ce qui est un filtre de concept, pas un objectif.

---

## Recommandation et confiance

1. Lever A5 (signe de la proximité conceptuelle) avant toute écriture de préenregistrement.
2. Ajouter b_eloigne et d1_inv aux témoins ; seuil relatif (×1,3) plutôt que +12 absolu.
3. Forme : O-paires (ensemble de base = paires, deux espaces dans la diagonale, répulsion par strates). Confiance moyenne qu'elle batte le stratifié ; confiance faible qu'elle batte b_eloigne de plus de 2 points, car dans les mondes de B l'éloignement grossier porte déjà presque tout le gain atteignable (plafond 0,750 contre 0,322 pour b_eloigne, mais la différence vient du bruit d'observation, pas du tirage).
4. Représentation : R1 ancrée + vérification R3 ; R2 hors boucle comme instrument de mesure seulement.
5. Ordre : E4 (séparabilité) **avant** E1, sinon E1 n'est pas interprétable ; E3 en parallèle (bon marché) ; E2 avant d'investir dans la machinerie ; E5 seulement si E1 passe.

FIN-DE-CELLULE