# Proposition A — Tour III.3 : réponse aux critiques

**État des pièces.**
- FAITS §3 annonce six familles de mécanismes mais n'en liste que quatre. La pièce est coupée et je n'invente pas les deux familles manquantes.
- Ma conception III.1 et les sections « Sur la proposition A » de B et de C sont présentes et complètes. Je ne traite que ces sections.

**Statuts.**
- Les dérivations de B et de C gardent leur statut : HYPOTHÈSE. Quand je les accepte, elles restent des HYPOTHÈSES. J'ajoute « re-dérivé par moi » quand j'ai refait le calcul.
- Les faits du dossier gardent leur statut : VÉRIFIÉ (§2) ou RAPPORTÉ (§1, §3, §4).
- Je ne cite que les identifiants arXiv donnés par le dossier.

---

## (a) Verdict, critique par critique

| # | Critique (source) | Verdict | Raison ou test |
|---|---|---|---|
| 1 | A3 : α − k_max/(n+1) borne une p-valeur isolée, pas un e-processus. À référence gelée, les facteurs sont, conditionnellement à la référence, i.i.d. d'espérance ≠ 1, d'où une divergence même à k = 0. On a α′ ≤ 0 dès que k_max/(n+1) ≥ α (B a1, b1 ; C a1, b) | **Acceptée** (re-dérivé par moi) | J'abandonne ma construction. Le banc doit reproduire cet échec (contrôle de banc, A3′). |
| 2 | A3 : une référence mise à jour en ligne est empoisonnée par le sabotage (B, C) | **Acceptée** | La référence est gelée dans A3′. |
| 3 | A3 : contamination ciblée, dérive bénigne, dépendance temporelle (C c1) | **Transformée en test** | Ce sont des cellules de la grille de A3′. |
| 4 | A1 : un nul limité à deux sauts est myope ; PPMI-SVD capte les blocs et les chemins longs (B a4, C a2) | **Acceptée** | J'ajoute Katz, le PageRank personnalisé et la SVD de la co-mention documentaire. |
| 5 | A1 : le contrôle « recâblage + dates permutées » donne 0 par construction (B a4) | **Partiellement rejetée** | Il ne discrimine pas H_A de H_B, c'est vrai. Mais il détecte les fuites : un gain non nul y signale de l'information future dans le pipeline. Je le garde à ce titre et j'ajoute un nul discriminant. |
| 6 | A1 : confusions de granularité, de capacité, d'ajustement, de prévalence et de dépendance dyadique (C a2, b) | **Acceptée** | Protocole 2×2 (ordre topologique × granularité de contexte), vecteurs aléatoires de même dimension, trois tranches temporelles, log-vraisemblance, bootstrap par nœuds. |
| 7 | A1 : nul dynamique à blocs et auto-excitation (B c2) | **Transformée** | Je l'adopte pour fixer le seuil. J'ajoute un *contrôle du contrôle* : un nul assez riche peut absorber le signal lexical et rendre H_B vraie par construction. |
| 8 | A2 : le détecteur inverse la règle du générateur, donc tautologie (B a3, C a3) | **Acceptée** | — |
| 9 | A2 : à partir des seules paires (contexte, prédicat), la fausse identité a la même loi qu'un concept unique controversé (B b3) | **Acceptée** (re-dérivé par moi : lois égales ⇒ aucun estimateur ne les distingue) | Je retire la version « texte seul » sans l'expérimenter, puisque son issue est fixée analytiquement. |
| 10 | A2 : l'induction de sens sépare déjà (i) et (ii), en sens inverse ; le vrai défi est (i) contre les concepts uniques (C a3) | **Acceptée** | La ligne de base est testée dans les deux orientations. |
| 11 | A2 : « AUROC à FPR fixé » est mal défini (C) | **Acceptée** | Remplacée par le TPR à FPR = α. |
| 12 | A2 : la controverse empirique serait le confondant « majeur » (B a3) | **Contrôle accepté, « majeur » rejeté** | Ce classement n'est établi nulle part. |
| 13 | A5 : conditionner sur les preuves refactorisées plus tard fait fuir le futur (B a2, C a4) | **Acceptée** | Mon H_A était invalide. |
| 14 | A5 : extraire une définition revient à factoriser un sous-terme répété ; mathlib formalise des mathématiques préexistantes (B a2) | **Acceptée** | La portée baisse. A5′ ne garde que les définitions non préfigurées par anti-unification. |
| 15 | A5 : confondants (lots d'auteurs, cadence, plans de manuels, ce dernier OBSERVÉ-NON-AUDITÉ chez C) | **Transformée** | Modèle d'activité en ligne de base, exclusion des cas « même auteur ». |
| 16 | A5 : variance de l'AUROC avec peu de positifs (C) | **Acceptée** | Les positifs sont comptés avant toute lecture des prédicteurs. |
| 17 | A6 : une rotation orthogonale élude la sonde et laisse les voisinages invariants ; l'attaque n'est pas adaptative (B a5, C a5) | **Acceptée** | A6 ne testait pas une marge asymétrique. |
| 18 | A6 : « l'évasion se transfère à *tous* les détecteurs » est invérifiable, ce qui viole B4 (B, C) | **Acceptée** | — |
| 19 | A6 : la recalibration du détecteur après attaque n'était pas tranchée (C) | **Acceptée** | Deux régimes préenregistrés : figé et ré-ajusté. |
| 20 | A6 : ligne de base de surface triviale si H(Z\|X) = 0 ; C propose une tâche avec H(Z\|X) > 0 (C c5-iv) | **Critique acceptée, remède rejeté** | Pour un réseau déterministe qui lit X, toute variable décodable de ses activations est une fonction de X, donc H(Z\|X) = 0 toujours. La vraie question est l'accessibilité calculatoire. Je la teste avec une variable Z fonction de X mais calculatoirement profonde, et une classe de surface de capacité appariée. |
| 21 | A7 : réindexation MeSH rétroactive (OBSERVÉ-NON-AUDITÉ chez C), patrons de types choisis en connaissant leur rendement, permutation conditionnée sur la seule fréquence (B a4, C a6) | **Acceptée** | Instantané MeSH de l'année t (disponibilité : à vérifier), permutation conditionnée sur fréquence, degré et communauté, patrons choisis sur une période antérieure disjointe. |
| 22 | A8 : jumeaux trop propres ; une nuisance de procédure suffit à pousser l'AUROC vers 1 (B a5, C) | **Acceptée** | Les témoins suivent une procédure appariée (graines, ajustements bénins de même méthode, rang et nombre de pas). Les jumeaux servent seulement de plafond. |
| 23 | A9 : sous « mêmes poids, contextes indépendants », la loi jointe factorise, donc la corrélation est nulle sous les deux hypothèses (B b6, C) | **Acceptée** (re-dérivé par moi) | J'abandonne le nul (voir (b), A9). |
| 24 | La passerelle processeur → carte graphique présuppose l'invariance d'échelle que j'avais moi-même contestée (C a7) | **Partiellement rejetée** | C'est une règle d'allocation de budget, pas une inférence. Le défaut est pourtant réel : elle ferme les pistes qui n'émergent qu'à grande échelle. Je le transforme en test : A10. |
| 25 | Auto-critique, à partir de la critique de B contre C : mes duels III.1 avaient aussi des zones grises (en A1, un gain ni nul ni stable sur 7 déciles ne réfutait rien) | **Acceptée** | Règle R-B4 ci-dessous. |

---

## (b) Expériences corrigées

### Règle commune R-B4

- **Hypothèses.** Chaque duel fixe une statistique θ et un seuil c préenregistré. H_A : θ > c ; H_B : θ ≤ c. Les deux hypothèses sont exclusives et exhaustives.
- **Effectif.** Il est fixé avant lecture pour une puissance de 0,9 à |θ − c| ≥ η.
- **Issues.** Il n'y a pas de zone d'abstention : chaque issue réfute une hypothèse. Je publie le risque d'erreur dans la bande |θ − c| < η.
- **Non-exécutabilité.** Si l'effectif est inatteignable, l'action est déclarée *non exécutable*, pas « non concluante ». Les positifs sont comptés avant toute lecture des prédicteurs.
- **Multiplicité.** La correction porte sur l'ensemble du programme.
- **Chiffres.** Tous les seuils, effectifs et coûts sont **illustratifs**.

### Re-classement

Les notes sont mes jugements (HYPOTHÈSE).

| Action | Gain | Facilité | Portée | Découverte | Coût | Score |
|---|---|---|---|---|---|---|
| A1′ Géométrie lexicale contre topologie multi-sauts | 5 | 4 | 4 | 3 | 1 | **240** |
| A3′ E-processus à boule de Kolmogorov | 5 | 4 | 5 | 2 | 1 | **200** |
| A2′ Scission avec covariable de régime | 4 | 3 | 3 | 4 | 1 | **144** |
| A4 Transition de champ contre vieillissement et blocs | 4 | 5 | 3 | 2 | 1 | **120** |
| A5′ Définitions non préfigurées (mathlib) | 4 | 3 | 2 | 4 | 1 | **96** |
| A10 Transfert d'échelle (Pythia) | 4 | 4 | 4 | 2 | 2 | **64** |
| A6′ Marge asymétrique, attaque adaptative | 4 | 2 | 5 | 3 | 2 | 60 |
| A7′ Chaînage typé, MeSH millésimé | 3 | 3 | 3 | 2 | 1 | 54 |
| A8′ Audit des poids, témoins appariés | 4 | 2 | 5 | 4 | 3 | 53 |

### A1′. La fenêtre lexicale bat-elle la topologie multi-sauts ?

- **Données.**
  - Résumés PubMed d'un domaine délimité par une liste de revues, et non par MeSH (voir ligne 21).
  - Trois tranches t0 < t1 < t2 : traits calculés jusqu'à t0, combinaison apprise sur les liens apparus dans (t0, t1], test sur (t1, t2].
- **Modèles.**
  - **G** : graphe de co-mention documentaire (voisins communs, Adamic-Adar, attachement préférentiel, Katz, PageRank personnalisé, SVD de rang d).
  - **G+R** : G plus d coordonnées gaussiennes, pour contrôler la capacité.
  - **G+L** : G plus PPMI-SVD de rang d calculée sur des fenêtres de phrase.
- **θ** : gain moyen de log-vraisemblance prédictive de G+L sur G+R, pondéré par décile de fréquence. L'intervalle vient d'un bootstrap par nœuds.
- **c** : quantile 95 % de θ sur des corpus engendrés par un nul dynamique à blocs et auto-excitation ajusté jusqu'à t0. Ce nul est proposé par B ; je m'en sers en le disant.
- **Hypothèses.**
  - H_A : θ > c. La fenêtre de phrase porte, sur les liens futurs, une information que la topologie multi-sauts et le vieillissement ne portent pas.
  - H_B : θ ≤ c.
- **Contrôle de fuite** : corpus recâblé à degrés préservés, avec dates permutées. θ doit y valoir 0 à l'erreur près, sinon la passe est annulée.
- **Contrôle du contrôle** : un monde synthétique où l'évaluateur plante une information présente *seulement* dans les fenêtres de phrase. Si θ ≤ c sur ce monde, le nul absorbe le signal, c est invalide, et je rejoue avec un nul préenregistré plus pauvre.
- **Ce qui falsifie.**
  - θ > c réfute H_B.
  - θ ≤ c réfute H_A. Dans ce domaine, les succès rétrospectifs du §2.5 (VÉRIFIÉ) cessent alors d'être revendicables comme supérieurs à la topologie, sans être pour autant « expliqués » par elle.
- **Premier pas sur processeur** : une seule tranche annuelle. **Coût** : une journée de processeur.

### A3′. Garantie séquentielle sous référence finie contaminée

- **Contrôle de banc** (ce n'est pas un duel) : ma construction III.1 sur des flux i.i.d., référence gelée, k = 0, T = 100 n (repris de B). Le taux de fausses alertes doit y dépasser α. Sinon, le banc est défectueux.
- **Construction testée** (HYPOTHÈSE, la mienne).
  - Je reprends l'idée d'une boule de contamination présente chez B et C. Je la pose sur la fonction de répartition, ce qui évite le problème de sens de troncature que C relève contre B.
  - Score borné ; fonction de pari g croissante, à valeurs dans [0, 1].
  - Facteur : e_t = 1 + λ (g(s_t) − m⁺), avec m⁺ = moyenne de g sur la référence + r.
  - Rayon : r = k_max/n + γ, avec γ = √(ln(2/δ) / (2(n − k_max))). La constante vient de l'inégalité DKW (Massart, 1990, *The Tight Constant in the Dvoretzky-Kiefer-Wolfowitz Inequality*).
  - Budget d'erreur : δ + α_seq = α.
- **Argument de validité** (HYPOTHÈSE, à vérifier).
  - k points quelconques, même choisis par un adversaire, déplacent la fonction de répartition empirique d'au plus k/n en norme sup.
  - Pour g monotone à valeurs dans [0, 1], |E_F g − E_G g| ≤ ‖F − G‖∞.
  - Donc, sur l'événement DKW, E[e_t] ≤ 1 pour toute loi honnête, que la contamination soit basse, haute ou ciblée.
  - L'unité échangeable est l'épisode (HYPOTHÈSE).
- **θ** : maximum, sur une grille préenregistrée de cellules, de FPR_sup(T) − α, corrigé par Bonferroni sur les cellules. Les cellules couvrent :
  - contamination basse, haute et ciblée ;
  - dépendance inter-épisodes de portée τ ;
  - dérive bénigne de norme sup inférieure à r.

  On fixe c = 0.
- **Hypothèses.** H_A : θ ≤ 0. H_B : θ > 0.
- **Prédiction annexe, falsifiable** : sous une dérive bénigne de norme sup *supérieure* à r, la validité doit tomber. Si elle tient, mon analyse du mécanisme est fausse.
- **Produit attendu.**
  - Une condition nécessaire de détection : ρ · (E_H g − E_F0 g) > r (HYPOTHÈSE, cohérente avec la borne b1 de B).
  - La courbe (n, ε_max) ↦ dilution minimale détectable.
  - Une comparaison avec un CUSUM écrêté au même rayon, sur le même score. Cette ligne de base est reprise de la critique de C contre B.
- **Ce qui falsifie.**
  - Un dépassement significatif de α dans une cellule réfute H_A.
  - Une validité tenue sur toute la grille réfute H_B.
- **Premier pas sur processeur** : flux par épisodes générés par l'évaluateur, avec des dommages abstraits. **Coût** : quelques heures.

### A2′. Fausse identité contre concepts uniques, avec covariable de régime

- **Données** : assertions typées (terme, prédicat, valeur, régime Z, document, laboratoire).
- **Générateur** : conçu par un évaluateur externe à qui le score n'est pas communiqué. Il produit les classes suivantes.
  - (i) Fusion : une partition latente *discrète*, non réductible à une fonction de Z, gouverne conjointement au moins deux prédicats.
  - (iii-a) Concept unique dont un prédicat dépend de Z.
  - (iii-b) Controverse liée au laboratoire.
  - (iii-c) Métonymie intra-domaine.
  - (iii-d) Piège : concept unique dont deux prédicats dépendent tous deux de Z.
  - (iv) Concepts propres.
- **Score** (HYPOTHÈSE) : gain de longueur de description d'un modèle à deux concepts partageant une partition, contre le meilleur modèle à un concept. Ce dernier peut inclure une interaction avec Z, un effet laboratoire et un effet de cadre syntaxique.
- **θ** : TPR sur (i) à FPR = α, ce FPR étant mesuré sur (iii-a…d) et (iv). On en retranche le même TPR obtenu par la meilleure ligne de base : induction de sens dans les deux orientations, ou conflit sur un seul prédicat. On fixe c = 0.
- **Hypothèses.** H_A : θ > 0. H_B : θ ≤ 0.
- **Taille minimale** n_T par jeton : fixée avant génération à partir de la condition de puissance de longueur de description donnée par B (b3).
- **Ce qui falsifie.**
  - θ ≤ 0 réfute H_A : même avec une covariable, la scission n'est pas séparable des concepts uniques.
  - θ > 0 réfute H_B, *dans les familles de générateurs testées seulement*.
- **Coût** : quelques heures.

### A4. Une « transition de champ » excède-t-elle vieillissement et blocs ?

J'utilise, en le disant, deux critiques adressées à d'autres : le nul à vieillissement auto-excité et à blocs (B contre C), et le regroupement hiérarchique le long d'un arbre figé avant la coupure (C contre B).

- **Données** : métadonnées arXiv datées, avec les catégories déclarées à la soumission. Il reste à vérifier qu'elles ne sont pas réattribuées après coup. Aucun concept OpenAlex n'est utilisé.
- **θ** : on mesure, à chacun des trois niveaux de l'arbre, l'écart standardisé entre l'exposant (ou la date) de transition estimé et sa distribution sous le nul ajusté avant t. θ est le plus petit de ces trois écarts.
- **c** : quantile 95 % de ce minimum sous le nul.
- **Hypothèses.** H_A : θ > c. H_B : θ ≤ c.
- **Contrôle du contrôle** : un monde à percolation plantée, sur lequel on doit obtenir θ > c.
- **A priori** (HYPOTHÈSE) : H_B, conformément à l'objection du §3.3 (RAPPORTÉ).
- **Ce qui falsifie.**
  - θ ≤ c réfute H_A : le signal de transition n'excède pas le vieillissement et les blocs à toutes les granularités.
  - θ > c réfute H_B : un signal persiste à toutes les granularités au-delà du nul.
- **Premier pas sur processeur** : une seule catégorie racine. **Coût** : une journée.

### A5′. Un signal précède-t-il une définition non préfigurée ?

- **Portée acceptée** (ligne 14) : A5′ teste l'apparition d'une définition *dans un dépôt*, pas l'invention mathématique.
- **Unité** : chaque module au temps t. Tous sont scorés, sans aucun filtrage par le futur.
- **Issue Y** : une définition est introduite dans (t, t+Δ], utilisée dans le module, et son corps n'est *pas* une instance d'anti-unification typée avec variables liées de termes présents à t. Ce compresseur λ-abstrait est celui que B oppose à C ; je l'emploie ici comme filtre.
- **Prédicteurs** : une liste préenregistrée d'indicateurs de tension à t.
- **Ligne de base d'activité** : intensité d'édition, nombre d'auteurs, profondeur d'import, âge, taille.
- **Exclusions** : cas « même auteur » dans la fenêtre ; migration Lean 3 → Lean 4.
- **θ** : ΔAUROC entre (tension + activité) et (activité seule), avec un bootstrap par grappes de modules. On fixe c = 0.
- **Hypothèses.** H_A : θ > 0. H_B : θ ≤ 0.
- **Pré-condition** : compter N_pos avant tout calcul de prédicteur. S'il est insuffisant pour la puissance fixée, l'action est non exécutable.
- **Ce qui falsifie.**
  - θ > 0 réfute H_B, sur le seul cas de mathlib.
  - θ ≤ 0 réfute H_A : la piste « tension formelle » du §3.4 perd son seul banc horodaté.
- **Coût** : une à deux journées, plus le temps d'ingénierie.

### A10. Le petit modèle prédit-il le suivant ? (critique C a7)

- **Modèles** : la suite Pythia (Biderman et al., 2023, *Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling*), dont les données d'entraînement sont publiques. On prend les trois plus petites tailles, en inférence sur processeur.
- **Étanchéité** : t0 est postérieur à la fin du corpus d'entraînement (date à vérifier). Sinon, des liens de (t0, t1] fuient dans les états cachés.
- **θ_s** : gain obtenu par A1′ quand on remplace L par les états cachés du modèle de taille s.
- **e** : |θ₃ − extrapolation log-linéaire à partir de θ₁ et θ₂|. On fixe c = η.
- **Hypothèses.** H_A : e ≤ η. H_B : e > η.
- **Ce qui falsifie.**
  - e > η réfute H_A : la passerelle ne peut pas s'appuyer sur les petits modèles. Il faut alors un test direct ou l'abandon.
  - e ≤ η réfute H_B, mais *dans cette famille seulement*. Le passage à ~8 milliards de paramètres reste non testé (§2.4).
- **Coût** : quelques jours de processeur.

### Corrections hors des six premières

- **A6′ (7ᵉ).**
  - Le bras d'attaque, déclaré et tenu par l'équipe rouge, est adaptatif contre *chaque* détecteur : sonde linéaire, sonde ré-entraînée après l'attaque, invariant local, intervention causale. Deux régimes : détecteur figé ou ré-ajusté.
  - θ : pour chaque détecteur, le surcoût de risque de tâche nécessaire pour le faire passer sous son seuil, rapporté à celui de la sonde ré-entraînée. On prend le maximum sur les détecteurs.
  - H_A : θ > 1 + c. H_B : θ ≤ 1 + c.
  - La variable Z est calculatoirement profonde (ligne 20). Aucun détail d'attaque n'est donné ici.
- **A7′ (8ᵉ)** : voir la ligne 21.
- **A8′ (9ᵉ)** : voir la ligne 22.
- **A9 (retiré).**
  - Pour des copies aux mêmes poids sans aléa partagé, la loi jointe se déduit de la politique individuelle (HYPOTHÈSE, re-dérivé). Toute coordination est donc une *propriété d'une seule copie*. Le problème se ramène à l'audit d'un seul modèle.
  - Je ne sais pas en faire un test décisif.

---

## (c) Réponse à l'arbitre

### Ce qui est établi

**D'après le dossier (VÉRIFIÉ, §2).**
- Des statistiques de cooccurrence reconstruisent des structures relationnelles (géographie, couleur, espace-temps) sans ancrage sensoriel.
- Les métriques globales de convergence sont confondues par la largeur et la profondeur. Après étalonnage par permutation, l'accord est surtout local (Gröger, Wen et Brbić, 2026, arXiv 2602.14486).
- Une géométrie circulaire peut se comporter localement comme des états discrets (Gupta, Fruengel et Heimersheim, 2026, arXiv 2610.37796).
- Une bonne prédiction n'implique pas une loi transférable (Vafa et al., 2024, arXiv 2406.03689).
- Une sonde peut mémoriser sans sélectivité (Hewitt et Liang, 2019, arXiv 1909.03368).
- Une coupure temporelle simulée par consigne laisse un écart de 52 % (Li et al., 2026, arXiv 2601.13717). Seuls le masquage strict ou des modèles antérieurs à la coupure sont admissibles.

**Acquis de ce tour.** Ce sont des HYPOTHÈSES analytiques de B et C, re-dérivées par moi et non vérifiées par un tiers.
- Une correction statique du seuil ne protège pas un e-processus contre une référence gelée ou contaminée.
- À partir des seules paires (contexte, prédicat), une fausse identité et un concept unique controversé sont indiscernables.
- Pour des copies aux mêmes poids, aucune statistique de paire n'informe au-delà de la politique individuelle.
- Éluder une seule sonde linéaire ne dit rien d'une marge asymétrique.
- Une limite que je propose (HYPOTHÈSE) : si le déplacement dû au sabotage reste dans le rayon « contamination + erreur d'échantillonnage », aucune méthode fondée sur la seule référence ne le détecte, quel que soit l'outil.

### Solide ou fragile

- **Solide** : la reconstruction relationnelle locale.
- **Fragile** :
  - les rapprochements à distance non typés (polysémie, survivant) ;
  - la convergence globale ;
  - la criticité sur graphes finis (§3.3, RAPPORTÉ) ;
  - la scission détectée par le texte seul ;
  - toute garantie séquentielle qui suppose une référence propre.

### Ce qui n'est pas établi

- Que la géométrie distributionnelle batte la topologie multi-sauts (A1′).
- Qu'un détecteur interne garde une marge face à un adversaire adaptatif (A6′).
- Qu'un signal précède une définition non préfigurée (A5′).
- Que les « transitions » excèdent le vieillissement et les blocs (A4).
- Le transfert vers ~8 milliards de paramètres (A10).
- Le contenu des deux familles manquantes du §3.
- Un détecteur de coordination : je ne sais pas.

### L'expérience à faire en premier : A1′

1. C'est le score le plus élevé, pour une journée de processeur.
2. Ses deux issues réorientent le budget :
   - si θ ≤ c, la couche « connaissance latente » n'a pas d'objet mesurable dans ce domaine, et la rétrodiction par modèles de langue cesse d'être prioritaire ;
   - si θ > c, A10 décide si le signal se prolonge avec la taille.

Je lance A3′ en parallèle. Elle est indépendante, coûte quelques heures, et c'est l'instrument de contrôle le plus directement livrable.

### Limites qui subsistent

- Un générateur, même aveugle au score, ne valide que ce qu'il sait planter.
- La formule multiplicative relègue A6′ au 7ᵉ rang, alors que le dossier donne la priorité au contrôle boîte blanche. Je le signale plutôt que de retoucher mes notes.
- La validité de A3′ repose sur l'échangeabilité des épisodes.
- A5′ ne teste pas l'invention mathématique.

FIN-DE-CELLULE