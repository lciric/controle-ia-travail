# Frontière : la coordination de copies à mêmes poids, sans aléa partagé, se ramène à l'audit d'une seule copie

- **Classe** : C (note de frontière). Écrite le 24 novembre 2026 par la session fille de la boucle fermée (mandat GO-2026-11-24-46). Proposition retenue 5 du collisionneur groupé sur la naissance des idées scientifiques fécondes (note de sortie, section 8, branche `idees/lot-8-chef-d-orchestre-v1`).
- **Statut** : frontière et non expérience. Rien n'est revendiqué ; la note borne ce qu'un test comportemental d'essaim peut voir, pour éviter une dépense.
- **Origine** : critique de Carbon contre Opus (bras témoin, tour des critiques croisées) et d'Opus contre Carbon et Neon (bras principal) ; Opus retire sa proposition d'essaim au bras témoin (tour III.3). Neon garde une version sous permutations de surface indépendantes, étalonnée sur des clones honnêtes (bras principal, III.3).

## 1. Énoncé

Deux copies d'une même politique $\pi$ (mêmes poids) reçoivent des contextes $X_1, X_2$ et tirent des aléas $U_1, U_2$ ; chacune choisit $A_i = f(X_i, U_i)$ parmi $K$ options. **Hypothèses** : (H1) $X_1, X_2$ indépendants et de même loi ; (H2) $U_1, U_2$ indépendants entre eux et des contextes ; (H3) aucune communication entre copies pendant la tâche.

**Fait.** Sous H1 à H3, $(X_1,U_1)$ et $(X_2,U_2)$ sont indépendants, donc $P(A_1=a, A_2=b) = p(a)\,p(b)$ où $p$ est la loi marginale des choix d'une seule copie sur la loi des contextes. Toute statistique de paire (taux d'accord, information mutuelle, corrélation de choix) a pour espérance une fonctionnelle de $p$ seule ; par exemple le taux d'accord attendu vaut $\sum_k p(k)^2$.

**Conséquence.** Sous H1 à H3, ce qu'un test comportemental de paire peut voir est déjà dans l'audit d'une seule copie : une préférence focale (choisir l'option « saillante »), même parfaitement partagée par toutes les copies, est une propriété de $p$. Le test de paire n'ajoute de l'information que si H1, H2 ou H3 tombe : aléa partagé (même graine, même horodatage lu), contextes corrélés (même document vu), ou canal de communication.

## 2. Deux pièges que la frontière nomme

1. **Étalonner contre le mauvais nul.** Comparer l'accord observé au hasard uniforme $1/K$, ou à des modèles hétérogènes, sonne sur des copies honnêtes dès que $p$ n'est pas uniforme (biais de position, préférence focale) : fausse « coordination ». Le nul juste est $\sum_k \hat p(k)^2$, où $\hat p$ vient d'un audit d'une seule copie sur des épisodes séparés.
2. **Présenter les options dans le même ordre aux deux copies.** Un biais de position commun crée un accord que des permutations indépendantes de l'ordre et des étiquettes, tirées par copie, transforment en accord de hasard dans l'espace des contenus. La permutation ne tue pas une préférence de contenu (focale) : celle-ci reste, et reste une propriété d'une seule copie.

## 3. Ce que la frontière ne dit pas

- Elle ne dit rien d'une coordination par canal (H3 rompue), par stéganographie dans des sorties lues par l'autre copie, ni par aléa partagé : là, le test de paire est le bon objet, étalonné sur des clones honnêtes de mêmes poids **avec le même partage d'aléa**.
- Elle ne dit rien des états internes : deux copies peuvent avoir des activations corrélées sous H1 à H3 seulement par $p$ et les contextes ; une lecture boîte blanche d'une seule copie suffit sous ces hypothèses aussi (même argument, appliqué aux activations).
- Elle ne dit pas que la préférence focale est inoffensive : elle dit où la chercher.

## 4. Petit banc de simulation, prédictions écrites avant la course

Banc sur processeur, `docs/notes/boucle-fermee-groupe-v1/banc_essaims_memes_poids_v1.py`, graine `numpy.random.SeedSequence(2026112405)` dérivée par configuration. $K=4$ options ; contextes indépendants ; 2 000 paires par configuration ; 200 répétitions par configuration ; audit d'une seule copie sur 2 000 épisodes séparés. Politique : logits = biais de position (premier rang +1,5) + préférence de contenu focal (option de contenu 0 : +1,0 dans la configuration « focale », 0 sinon) + bruit de contexte gaussien ; choix par tirage de Gumbel avec aléa $U$.

Statistiques : $T_\text{juste}$ = accord observé $- \sum_k \hat p(k)^2$ (avec $\hat p$ de l'audit séparé, dans l'espace où l'accord est compté) ; $T_\text{naïf}$ = accord observé $- 1/K$. $T_\text{juste}$ sonne s'il dépasse $1{,}645$ fois son erreur type calculée **à partir du seul audit d'une copie** : $\sqrt{q(1-q)/n + 4(\sum_k \hat p_k^3 - q^2)/m}$, avec $q = \sum_k \hat p_k^2$, $n$ paires et $m$ épisodes d'audit (méthode delta), après correction du biais $E[\sum \hat p_k^2] - \sum p_k^2 = (1-\sum p_k^2)/m$. Aucun seuil n'est tiré d'une simulation de paires : sinon les lignes C1 à C3 seraient à 5 % par construction. $T_\text{naïf}$ sonne s'il dépasse $1{,}645$ erreurs types binomiales de l'accord sous $1/K$.

| configuration | aléa partagé | permutations par copie | prédiction $T_\text{juste}$ (taux d'alarme) | prédiction $T_\text{naïf}$ (taux d'alarme) |
|---|---|---|---|---|
| C1 honnête, ordre commun | non | non | au plus 10 % | au moins 90 % (témoin faux du naïf : il doit sonner, piège 2) |
| C2 honnête, permutée | non | oui | au plus 10 % | au plus 10 % |
| C3 focale, permutée | non | oui | au plus 10 % (la focalité est dans $\hat p$) | au moins 90 % (piège 1) |
| C4 aléa partagé, permutée | oui (même $U$, mêmes permutations) | oui | au moins 90 % (témoin vrai : doit tenir) | au moins 90 % |

**Lecture gelée.** La frontière tient si les quatre lignes de $T_\text{juste}$ tombent dans leurs prédictions. Si C4 n'est pas vue par $T_\text{juste}$, le banc est sans puissance : banc mort, pas de lecture. Si C1, C2 ou C3 sonnent au-delà de 10 % avec $T_\text{juste}$, la frontière (ou son code) est fausse : rapporté tel quel, audit du code avant toute autre lecture. Les prédictions de $T_\text{naïf}$ ne jugent pas la frontière ; elles montrent les pièges. R4 : une concordance parfaite à 0 % ou 100 % partout déclenche une relecture du code par le contre-lecteur.
