NB_FAILLES_M2: 8

**Pièces manquantes ou corrompues :**
- `{lettre}`, `{autres}`, `{mots}` et `{marqueur}` sont vides dans mon en-tête. Je ne peux donc ni me désigner, ni respecter une limite de mots, ni émettre le marqueur final exact.
- La « matrice de prédation apprise en M3 », les règles L\*v2-1 à 3, `S_TD` et le détail de l'échec de la sonde ne sont pas transmis. Je ne vérifie pas la conformité à ces règles.
- Trois résumés sont coupés (1301.2158, 2604.26748, 1310.7906). Les accents sont corrompus (« ? »).

---

## F1 — La branche H_A est inatteignable par construction (B4 violé)

Dans `compute_O`, les sommets de $G_n$ sont les **K classes**, d'où $\alpha(G_n)\le K$. Avec $\theta_1\ge 0$, on obtient :

$$O \le \frac{\log_2 K / n_{fen}}{\log_2 K} = \frac{1}{n_{fen}} = 0{,}125 \quad (\text{avec } n_{fen}=8, \text{ illustratif})$$

Toute issue tombe donc dans $\hat I_B$ ou dans la zone non conclusive $]0{,}10 ; 0{,}25[$. Une seule hypothèse est falsifiable.

**Correctif exigé :** chaque essai émet *un* message sur $n$ positions, donc il faut retirer la division par $n$ et définir
$O=\big(\log_2\alpha(G_n)-\log_2\alpha(G_1)\big)/\log_2 K \in [-1;1]$.
Il faut ensuite montrer que les deux intervalles sont atteignables, par exemple sur des données synthétiques.

## F2 — Le résumé ne soutient que partiellement l'opérateur (Abstract Entailment)

Ce que soutient le résumé cité (RAPPORTÉ) : « la mémoire d'entrée/sortie affecte la communication zéro-erreur ». Rien de plus.

En revanche :
- La formule $\frac1n\log\alpha(G^{\boxtimes n})$ n'y figure pas. Elle provient de Shannon (1956, *The zero error capacity of a noisy channel*), où elle est définie pour un canal **sans mémoire**.
- La comparaison annoncée dans le résumé porte sur « *classical memory channels* », non sur le cas sans mémoire. L'affirmation « diffère du cas sans mémoire » n'y est pas.
- Chez l'auteur, la mémoire est une propriété du **canal**. Le pont la transporte vers le **décodeur** (la sonde), ce qui constitue un changement d'objet.

**Correctif exigé :** reclasser la correspondance en HYPOTHÈSE de transfert, citer Shannon 1956 pour la formule, et ne garder de 2407.21732 que l'ancrage générique.

## F3 — $\Theta_n>\Theta_1$ n'implique pas un code à mémoire

Même pour un canal sans mémoire, le codage par blocs augmente la capacité zéro-erreur. Exemple du pentagone : $\alpha(C_5)=2$ alors que $\Theta(C_5)=\sqrt5$ (Lovász, 1979, *On the Shannon capacity of a graph*). H_A et H_B ne sont donc pas exclusives sur cette observable.

**Correctif exigé :** ajouter un nul « canal sans mémoire conditionnel ». On remplace chaque position $t$ par $h_\ell^{(t)}$ tiré d'un *autre* essai de la même classe, ce qui conserve les marginales par position et détruit la dépendance séquentielle. H_A exige que $O_{réel}$ excède ce nul. L'ablation (ii) proposée, une permutation intra-fenêtre, ne teste pas cela.

## F4 — Artefact de rareté de la quantification

Une arête est créée dès qu'**une seule** collision existe. Le comportement des deux graphes dépend alors de la taille de l'espace de quantification :
- $G_1$ (64 cellules, illustratif) tend vers le graphe complet quand le nombre d'essais N croît, d'où $\theta_1\to0$.
- $G_n$ ($64^8$ cellules, illustratif) tend vers le graphe vide, d'où $\alpha=K$.

$O$ mesure alors la taille de l'espace de codage, pas la mémoire. Le contrôle (i) échoue lui aussi : sous permutation, $G_n$ reste vide, donc $O$ reste figé et le contrôle ne diagnostique rien.

**Correctif exigé :** égaliser le nombre de cellules entre $q_1$ et $q_n$, publier la courbe de $O$ en fonction de N, et utiliser des partitions apprises sur un jeu disjoint.

## F5 — $h_\ell^{(t)}$ n'est pas « sans mémoire »

Avec l'attention causale, $h_\ell^{(t)}$ pour $\ell\ge2$ intègre déjà les tokens d'indice $\le t$. L'opposition « position isolée contre suite » est donc mal posée.

**Correctif exigé :** comparer la fenêtre $h^{(t..t+n)}$ à une sonde lue sur la **dernière** position de la même fenêtre. Sans cela, H_A confond mémoire et position.

## F6 — Confondant de non-linéarité

L'échec d'une sonde *linéaire* peut venir de la non-linéarité et non de la mémoire.

**Correctif exigé :** ajouter un troisième bras, un décodeur non linéaire sans mémoire (MLP sur $h^{(t)}$). Si ce bras réussit, H_A est falsifiée même si $O$ est élevé.

## F7 — Tenseurs sur Llama-3.1-8B-Instruct non spécifiés

Les valeurs suivantes viennent de ma mémoire, ne figurent pas dans les pièces et sont à vérifier sur `config.json` : 32 blocs, $d_{model}=4096$, `hidden_states` de longueur 33 (indice 0 = embeddings).

Le pont ne précise pas :
- la dimension de $h$ ;
- la convention d'indexation des couches 2–22 ;
- le point de départ de la fenêtre et le traitement des messages plus courts que $n$ ;
- quelle couche entre dans `compute_O`, qui n'a aucun argument $\ell$.

Si l'on teste 21 couches, il faut une correction pour comparaisons multiples, ou bien une couche préenregistrée.

**Correctif exigé :** une signature `compute_O(data, ℓ, t0, n)`, avec une règle de troncature et de remplissage explicite.

## F8 — Critères incommensurables

L'échec de la sonde est statistique (précision). Le critère du pont est zéro-erreur : une seule collision bruitée suffit à tuer une paire de classes. Une issue dans $\hat I_B$ peut donc venir d'un manque de puissance de l'estimateur, ce qui crée une asymétrie de falsification.

**Correctif exigé :** rapporter en parallèle une version à erreur ε, c'est-à-dire la précision du décodeur à fenêtre $n$ contre celle du décodeur sans mémoire, avec les mêmes partitions.

---

**Ce que cet audit rend réfutable :**
- F1 est une borne algébrique, vérifiable sur le pseudo-code.
- F3 se tranche par le nul conditionnel.
- F5 et F6 se tranchent par les bras supplémentaires.

Toute valeur de $O$ reste inexistante. L'ensemble du pont reste au statut HYPOTHÈSE ou RAPPORTÉ.

*(Marqueur final non émis : le champ `{marqueur}` est vide dans les consignes.)*
