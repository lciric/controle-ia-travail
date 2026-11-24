# Erratum transversal du dossier des questions du directeur : une seule notation pour κ, et la comparaison des hypergraphes renvoyée à la question 7 (v1)

- **Nature** : pièce de travail (classe C), erratum transversal ; aucune pièce existante n'est modifiée.
- **Heure** : `2026-11-24T16:41:28Z` (`date -u`).
- **Auteur** : Claude Opus 5.5, effort élevé, sous-agent de la session fille `session_016QhUrtAyz3dFV4u1BbUBoS`.
- **Pièces visées** (dossier `docs/notes/questions-directeur-2026-11-24-v1/`) : réponses q1 (`2cc29632…`), q3 (`af126ebf…`), q4 (`249c611c…`), q5 (`0bdc9810…`), q7 (`937e3e69…`), q9 (`e981c88c…`) ; toute pièce future du dossier.
- **Sources** : `contre-lecture-reponses-q1-q5-q7-q9-v1.md` (`9cefaa1fab6da2328bf99990f06ed03b4ec790c5e954e75c8209af07c68a786f`), « Contradictions entre pièces », points 1 et 2 ; `docs/notes/idee-interessante-v1/reponse-fable-max-v1.md` (`8ec4f9e0b2f835472ff5040b852aba9e365942573973aad642b9505957ca5db0`), l. 39 ; `docs/notes/idee-interessante-v1/reponses-google-v1/reponse-carbon-v1.md` (`a9532fbb60c34d46647b81de1a4c52cdb6cec3521cf1728e7b16fc6e80db5ca6`), l. 36-40 ; `complement-questions-8-9-et-corrections-note-v1.md`, correction (1).

## 1. Notation, fixée pour tout le dossier

**Règle.** κ n'a qu'un sens : la **part des conflits** d'une correspondance φ au sens de Fable (l. 39) : « la part dont l'image porte un type incompatible ». Tout autre emploi de κ dans le dossier se lit avec le symbole neuf ci-dessous.

| Symbole | Sens | Origine | Remplace |
|---|---|---|---|
| `c(φ)` | couverture : part des relations de `R_a` dont l'image existe dans `R_b` avec le même type | Fable, l. 39 | — |
| `κ(φ)` | part des conflits : part des relations dont l'image existe avec un type incompatible | Fable, l. 39 ; questions 7 et 9 ; corrections du 24 novembre | — |
| `K_r = max_φ [c − κ]`, `Z_r = (K_r − moyenne)/écart-type` sous recâblage | score serrure-clé et son écart réduit | Fable, l. 39 | — |
| `c_C(φ)` | couverture pondérée par ω chez Carbon | Carbon, l. 36-38 | le κ de Carbon (question 5, section 3) |
| `χ_C(φ)` | taux de conflits chez Carbon | Carbon, l. 36 et 38 | le χ de Carbon (question 5, section 3 ; question 7, tableau de la section 2, « inhibition (I, χ) ») |
| `γ_C` | pénalité des conflits chez Carbon | Carbon, l. 39-40 | le γ de Carbon, homonyme du γ du champ chez Fable |
| `K_C = max_φ c_C(φ)·exp(−γ_C χ_C(φ))` | score serrure-clé de Carbon | Carbon, l. 39-40 | `K = max κ·e^(−γχ)` (question 5) |
| `ψ` | coefficient de la voie catalytique dans la cinétique | question 3, section 2, prédiction 2 | κ (question 3) |
| `k₀` | constante de rencontre | question 3, section 3 | κ₀ (question 3) |
| `w_m` | poids de la méthode m dans la voie catalytique | question 3, sections 2 et 3 | `c_m` (homonyme de la couverture c) |
| `β_E`, `δ_E` | coefficients de la barrière, `E_ab = E₀ − β_E Z_ab − δ_E P_ab` | question 3, section 3 | `β′`, `δ′` (β′ est chez Fable le coefficient de Z dans la crédibilité q) |
| `G(t)`, `ΔG(t)` | part des auteurs dans la plus grande composante, et son excès sur le nul | question 4, section 3 | `P(t)`, `ΔP(t)` (P est ailleurs le terme des problèmes δP) |
| `χ(t)` | susceptibilité du graphe des coauteurs | question 4, section 3 | inchangé : sans indice, distinct de `χ_C` |
| « kappa de Cohen », « kappa pondéré » | accord entre lecteurs | question 1 | toujours écrit en toutes lettres, jamais κ |

Lecture des formules touchées : question 3, `λ = p⁰·[e^{βZ+δP} + ψ·Σ_m w_m h_a(m) h_b(m)·e^{β_c Z + δP}]` (avec le facteur `e^{δP}` de l'erratum 1 de la question 3, mineur 2) et `k_D = k₀·n_a^{m_a}·n_b^{m_b}·C_ab` ; question 5, `K_C = max c_C·e^(−γ_C χ_C)`.

**Homonymies relevées, laissées en place** (le contexte les sépare ; à ne pas reprendre dans une pièce neuve) : ρ désigne chez Fable à la fois le type d'une relation `(x, ρ, y)` et le coefficient de S dans q, puis ailleurs la corrélation intra-course (question 4) et le ρ de Spearman (questions 2 et 5) ; m est l'exposant du préfacteur en T et l'indice de méthode (question 3). Pour toute pièce neuve : écrire `r` pour le type de relation, comme Carbon.

## 2. La comparaison des hypergraphes : la question 7 fait foi

**Contradiction.** La question 5 (section 3, ligne « Objets ») classe l'écart entre les objets de Carbon et de Fable en « vocabulaire surtout ». La question 7 porte la comparaison (critères fixés d'avance, section 3 ; tableau, section 4). Carbon y l'emporte sur l'expression (critère 1 : flèche envoyée sur un chemin, absence, alphabet qui croît, problèmes) et en partie sur les problèmes (critère 5). Fable l'emporte sur la mesurabilité, le coût, la parcimonie et l'oracle planté (critères 2, 3, 6 et 7), et le critère 4 est à égalité. D'où son verdict de section 4 : « aucun ne domine, d'où la fusion ».

**Tranché.** L'écart est **de fond en partie**, non de vocabulaire. La question 7, sections 3 à 5, fait foi. Dans la question 5, la ligne « Objets » se lit « fond en partie ; voir la question 7 » (erratum 1 de la question 5, mineur 4). La phrase de tête de la question 7 (« celui de Fable est meilleur ») cède à sa propre section 4 (`errata-mineurs-q1-q2-q7-v1.md`). L'objet commun du dossier s'appelle **l'hypergraphe fusionné** : l'hypergraphe orienté de la question 7, section 5, le cœur de Fable, la résolvante et la couche typée de Carbon, plus les poids, les anomalies empiriques, l'ancrage et le couplage δP. La question 9 le reprend sous ce sens, et rien n'y change.

**Rappel.** Carbon n'écrit nulle part « hypergraphe » (question 7, section 2). Le mot reste attribué à Fable et à Neon.
