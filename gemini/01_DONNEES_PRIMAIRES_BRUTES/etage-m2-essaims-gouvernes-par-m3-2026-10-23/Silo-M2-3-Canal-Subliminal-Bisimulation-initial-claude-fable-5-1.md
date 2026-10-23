# Proposition — Pont M2 (canal subliminal Sol→Astra)

**Pièces manquantes (une ligne chacune) :** les champs `{lettre}`, `{autres}`, `{mots}`, `{marqueur}` sont vides dans l'en-tête ; les trois résumés 1301.2158, 2604.26748 et 1310.7906 sont visiblement coupés (« syner », « corollar », « The next ») ; le mot `S_TD` et le détail de « l'échec de la sonde linéaire » ne sont pas transmis, je ne les reconstruis pas. Le texte de mission contient des caractères corrompus (« ? »), je lis à travers sans compléter.

## 1. Choix de l'article (règle L*v2-1)

**Choisi : arXiv:2407.21732v2** (référence à vérifier). Statut du résumé : RAPPORTÉ (texte fourni par l'API, non audité par moi).

Ancrage (règle L*v2-2) — phrase exacte : « *highlighting the impact of memory on achieving error-free communication* » (référence à vérifier), et : « *We analyze the zero-error capacity of the semantic channel using a comprehensive framework that accommodates multiple input and output memories* » (référence à vérifier).

Correspondance de précondition, sans métaphore : une sonde linéaire lue à la position *t* sur $h_\ell^{(t)}$ est un décodeur **sans mémoire** (une fonction de $h_\ell^{(t)}$ seul). L'hypothèse mathématique native de l'article est précisément : *la capacité zéro-erreur d'un canal dépend de la mémoire d'entrée/sortie et diffère du cas sans mémoire*. Si le contrordre fuit par un code à mémoire (la classe du contrordre n'est séparable qu'au niveau de la **suite** $h_\ell^{(t..t+n)}$, jamais d'un $h_\ell^{(t)}$ isolé), alors l'échec de la sonde est **structurel**, pas statistique. HYPOTHÈSE : c'est ce qui s'est produit.

**Pourquoi pas les autres (B1, attaque anticipée) :** 2604.26748 (complexité RMDP/bisimulation) porte sur le problème de seuil sous incertitude de transition ; rien dans le résumé transmis ne traite de détection d'information, et la partie « bisimulation » est coupée — l'utiliser serait importer un mot du titre, interdit par Zéro Métaphore. 1108.0391 (capacité croît avec la puissance) suppose un canal **memoryless** vectoriel : c'est l'hypothèse *inverse* de notre échec. 1301.2158 et 1310.7906 : pas de notion de canal ni de détection.

## 2. Opérateur compilé sur les tenseurs (HYPOTHÈSE de construction)

Opérateur de l'article : capacité zéro-erreur $\Theta_n = \frac{1}{n}\log_2 \alpha(G_n)$, où $G_n$ est le graphe de confusabilité sur les messages de longueur $n$ et $\alpha$ le nombre d'indépendance (Shannon). Compilation :

- Vertex = classe de contrordre $c \in \{1..K\}$ (K ≥ 2, dont « aucun »).
- Pour chaque essai : Sol reçoit (tâche, $c$), émet la délégation $m$ ; on enregistre chez Astra lisant $m$ les $h_\ell^{(t)}$, $\ell \in [2,22]$, fenêtre de $n$ tokens.
- Quantification : $q_n(\cdot)$ = codage produit (k-means par couche puis concaténation sur $n$ positions ; $k$ fixé par validation, `illustratif` : $k=64$).
- Arête $(c,c')$ dans $G_n$ ssi il existe un essai de classe $c$ et un essai de classe $c'$ avec $q_n$ identique (cellules de confusion partagées). $G_1$ = même chose avec $n=1$ (le décodeur sans mémoire = la sonde).

```
compute_O(data) -> float:
    K = nb classes de contrordre
    G1 = graphe_confusabilite(data, n=1)
    Gn = graphe_confusabilite(data, n=n_fen)   # n_fen=8, illustratif
    theta1 = log2(alpha(G1))
    thetan = log2(alpha(Gn)) / n_fen
    return (thetan - theta1) / log2(K)   # gain zéro-erreur dû à la mémoire, normalisé
```

$\alpha$ exact (K petit, ≤ 8 `illustratif`), donc pas d'approximation cachée.

## 3. Spécification EEC sans zone morte (règle L*v2-3)

- $H_A$ (code à mémoire) : $\hat I_A = [0{,}25 ;\ 1]$ `illustratif`.
- $H_B$ (fuite sans mémoire ou absente) : $\hat I_B = [-1 ;\ 0{,}10]$ `illustratif`.
- $\text{dist}(\hat I_A,\hat I_B) = 0{,}15 > 0{,}10$ `illustratif`. Résultat dans $]0{,}10 ; 0{,}25[$ : expérience **non conclusive**, déclaré tel quel, pas de troisième hypothèse inventée.

**Contrôle $R_S$ :** (i) permutation des étiquettes $c$ entre essais (1000 tirages, `illustratif`) : $O$ doit tomber dans $\hat I_B$ pour ≥ 95 % des tirages, sinon la quantification fabrique de l'indépendance artefactuelle ; (ii) ablation d'ordre : permuter les positions à l'intérieur de chaque fenêtre de $n$ tokens avant $q_n$ ; si $O$ reste dans $\hat I_A$, la mémoire exploitée est un sac de tokens, pas une séquence, et l'opérateur de l'article n'est que partiellement applicable — on le dit.

## 4. Inférence forte (B4)

- Issue dans $\hat I_A$ : falsifie « une sonde linéaire mieux entraînée / plus de données suffirait » ; la borne de fuite doit être calculée sur $\Theta_n$, pas sur une métrique par position.
- Issue dans $\hat I_B$ : falsifie « le canal subliminal est un code à mémoire » ; l'échec de la sonde relève alors de l'échantillonnage ou du choix de couche, et le verrou H9 reste un problème de détection classique.

Statut global : aucune valeur de $O$ n'existe encore ; tout ce qui précède est HYPOTHÈSE ou RAPPORTÉ. Ce qui peut être réfuté : l'existence d'un gain zéro-erreur dû à la mémoire sur Llama-3.1-8B-Instruct, couches 2–22.

FIN-PONT-M2
