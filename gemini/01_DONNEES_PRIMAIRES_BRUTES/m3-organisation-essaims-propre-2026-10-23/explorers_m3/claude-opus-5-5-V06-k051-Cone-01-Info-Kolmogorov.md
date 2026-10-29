BASSIN_MATH: Factorisation Markovienne Algorithmique à Ancrage de Consigne (FMA-AC)

LOI_PROPOSEE: on approxime K par un compresseur réel C (LZMA ou zstd-dict). Pour des sorties x_j et une consigne c, l'arête u→v survit ssi Î(x_u:x_v|c) = C(x_v|c) − C(x_v|x_u,c) > τ ; de plus, l'agent v est re-ancré ssi Î(c:x_v) < ρ·Î(c:x_parent). Topologie* = argmin_G Σ_j C(x_j | pa_G(j), c), sous coût ≤ B.

**1. Mécanisme d'auto-organisation hors-poids**
La condition de Markov algorithmique (Janzing–Schölkopf) s'énonce K(x₁…x_n) ≐ Σ_j K(x_j|pa_j*). L'essaim l'exploite en trois règles, appliquées à chaque tour sur ses propres transcrits.

- **Orientation.** Le graphe de communication est réappris en minimisant la longueur de description factorisée. On conserve u→v si x_u comprime réellement x_v. Sinon, v ne reçoit plus u.
- **Corrélation (H4').** Si la redondance résiduelle Î(x_u:x_v|c) entre agents de même famille dépasse τ, la paire devient suspecte d'erreur commune par poids partagés. Le nœud v est alors remplacé par une chimère d'une autre famille (Opus↔Fable↔Argon). La monoculture n'est conservée que si cette redondance reste sous τ.
- **Dérive (H9).** La conservation de Levin interdit à l'information sur c de croître le long d'une délégation. Une perte supérieure au facteur ρ déclenche un re-ancrage, c'est-à-dire une réinjection de c brute.
- **Spawn d'un explorateur.** Il est lancé quand la nouveauté conditionnelle C(x_new|pool)/|x_new| est élevée et que jev-1.14.0 valide le contenu.
- **Spawn d'un démolisseur Red-Team.** Il est lancé quand la déficience de hasard δ = |x| − C(x|corpus) est forte, où le corpus provient d'arXiv, Semantic Scholar et Crossref. Une telle compressibilité signale une récitation paramétrique probable.
- **Budget.** Les requêtes Claude (100 USD) et Gemini (20 USD) sont allouées au prorata du gain marginal ΔΣC par dollar.

**2. Fonction objectif et anti-Goodhart**

R = [L(D_h) − L(D_h | H_essaim)] / $ − λ·Î(x_essaim : r_jev | c) − μ·Σ δ_corpus

- D_h est un lot d'étiquettes jev tenu caché et tournant.
- L est la longueur MDL en bits.
- r_jev représente les traits de surface de la grille du juge.

Le deuxième terme pénalise toute information que les sorties portent sur le juge au-delà de c, ce qui empêche l'optimisation directe de jev (Goodhart). Le troisième terme pénalise la récitation de la mémoire paramétrique.

**3. Duel décisif M3 (H_A ⊥ H_B)**

- **H_A :** le gain provient de la factorisation algorithmique.
- **H_B :** le gain provient seulement de la diversité chimérique.

Le protocole compare quatre bras à budget identique (120 USD), avec un mélange de familles strictement apparié :

| Bras | Configuration |
|---|---|
| (i) | FMA-AC |
| (ii) | Topologie fixe |
| (iii) | Échantillons i.i.d. |
| (iv) | Contrôle négatif : FMA-AC avec compresseur permuté (Î calculée sur des transcrits mélangés) |

Le dispositif comprend 40 tâches et 5 graines, avec une métrique primaire R mesurée sur le lot D_h, ainsi que deux métriques secondaires : la corrélation des erreurs inter-agents et la pente de perte de Î(c:x) par niveau de délégation.

H_A est validée si (i) > (ii) et (iii), avec (iv) ≈ (iii), par un test de permutation à p < 0,01. Si (iv) ≈ (i), H_B l'emporte.
