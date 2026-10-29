BASSIN_MATH: Roi de Phase à Chaînes Dolev-Strong et Audit Freivalds (RP-DSF)

LOI_PROPOSEE: À chaque phase k = 1…f_eff+1, le roi est K_k = argmax_{i ∈ fam ≠ fam(K_{k−1})} ρ_i, où ρ_i est le taux d'audit Freivalds réussi. On a f_eff = |clusters de collusion|, et la règle impose n_eff ≥ 4·f_eff + 1 ainsi que κ(G) ≥ 2·f_eff + 1. Sinon, l'essaim doit muter.

**1. Mécanisme d'auto-organisation hors-poids**

- **Clusters de collusion.** On mesure l'excès d'accord pour chaque paire d'agents : χ_ij = P(accord ∧ erreur) − p_i·p_j. Le graphe de seuil χ_ij > τ est partitionné en clusters. Chaque cluster compte comme un seul votant byzantin potentiel, ce qui traite H4'.
- **Monoculture ou chimère.** Si une famille de poids fait chuter n_eff sous 4·f_eff + 1, on spawne un agent d'une autre famille. Le choix suit le coût marginal : Gemini (20 USD) pour la diversité bon marché, Opus pour la profondeur.
- **Topologie (qui parle à qui).** Elle est mutée pour maintenir une connectivité de Dolev κ(G) ≥ 2·f_eff + 1. On ajoute l'arête qui maximise la connectivité par chemins disjoints et on retire les arêtes intra-cluster redondantes.
- **Rôle du roi.** Il partitionne les tâches. Le Phase King tolère les agents non coopératifs sans supposer la majorité honnête d'une famille.
- **Anti-dérive (H9).** Chaque délégation porte une chaîne Dolev-Strong de hachages signés de la consigne racine. jev-1.14.0 calcule la distance sémantique d(consigne_racine, sous-consigne). Toute chaîne dont un maillon dépasse ε est rejetée.
- **Explorateur ou démolisseur.**
  - On spawne un explorateur Red-Team si l'accord est élevé mais l'audit est faible : c'est un faux consensus.
  - On spawne un explorateur ordinaire si l'audit est élevé mais la couverture bibliographique faible.

**2. Fonction objectif et anti-Goodhart**

R = Σ_c 𝟙[c ∈ S_aléa] · V(c) − λ·Σ χ_ij⁺ − μ·coût_USD

- V(c) = 1 seulement si le DOI ou l'identifiant arXiv existe (Crossref ou Semantic Scholar) et si jev confirme l'implication source→affirmation. Cela neutralise la récitation de mémoire paramétrique.
- S_aléa est un échantillon de requêtes de type PCP, tiré par une graine engagée après production. L'essaim ne peut donc pas anticiper ce qui sera vérifié.
- Le juge n'est jamais optimisé directement. 20 % des audits restent cachés et ne servent qu'à l'évaluation finale.

**3. Duel décisif M3 (H_A ⊥ H_B)**

Chaque bras dispose du même budget : 60 USD Claude et 12 USD Gemini. Le protocole porte sur 40 questions de contrôle-IA, avec un jeu d'or caché.

| Bras | Configuration |
|---|---|
| A | RP-DSF |
| B | Topologie fixe, en étoile |
| C | Ensemble i.i.d. avec vote majoritaire |
| D (contrôle négatif) | RP-DSF avec scores d'audit permutés aléatoirement |

Les deux hypothèses font des prédictions mutuellement exclusives :

- **H_A :** A > B, C et D en précision vérifiée sur l'or caché, avec un χ moyen et une dérive inférieurs.
- **H_B :** A ≈ D. Dans ce cas, le gain vient du budget ou de la diversité brute, et non de la loi.

H_A est rejetée si l'intervalle de confiance bootstrap à 95 % de (A − D) contient 0.
