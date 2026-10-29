BASSIN_MATH: Arbre Ultramétrique de Crooks (AUC-q)

LOI_PROPOSEE: On scinde le nœud k en deux sous-essaims lorsque le cumulant de Binder vérifie g_k = ½(3 − ⟨q⁴⟩/⟨q²⟩²) < g_c, ce qui signale une transition RSB. On élague l'arête de délégation e lorsque Δ_e = −ln⟨e^{−βW_e}⟩ − ΔF̂_e > ε. Le budget suit la loi b_k ∝ x(q_{k+1}) − x(q_k).

**1. Auto-organisation hors-poids**

Chaque agent a est un spin s_a ∈ {±1}^N : ses verdicts sur N sondes scellées, notées par `jev-1.14.0`. Les couplages J_ab sont égaux à la covariance des erreurs. Les recouvrements q_ab = N⁻¹ s_a·s_b définissent la distribution P(q).

- **Topologie.** Elle est l'arbre de Parisi lui-même : les agents dont le recouvrement dépasse q_k communiquent au niveau k, et seuls les représentants de chaque cluster montent d'un niveau. Un P(q) unimodal signifie une phase symétrique : on fusionne les branches, car elles sont redondantes. L'apparition d'un second pic signifie une brisure de symétrie : on scinde.
- **Spawn.** Un explorateur est engendré à haute température (β faible, phase paramagnétique) quand q_EA → 1, signe de figement. Un démolisseur Red-Team est engendré quand la frustration est faible, c'est-à-dire quand Σ sgn(J_ab J_bc J_ca) > 0. Il est alors couplé antiferromagnétiquement (J < 0) au consensus.
- **Monoculture ou chimère.** Si le q_EA intra-famille dépasse le q_EA inter-famille plus δ, la corrélation H4' est avérée et l'on impose une chimère `fable`/`opus`/`argon` dans ce cluster. Sinon, on conserve la monoculture, moins coûteuse.
- **Dérive (H9).** Chaque délégation est traitée comme un protocole hors-équilibre. Le travail W_e est la divergence `jev` entre la consigne parente et la sortie de l'enfant. La violation de l'égalité de Jarzynski mesure l'irréversibilité, donc la dérive, et l'arête est rejouée ou coupée.
- **Apprentissage.** Seuls les prompts, l'arbre et β sont mutés ; aucun poids n'est modifié.

**2. Objectif anti-Goodhart**

Les magnétisations sont calculées par les équations TAP :

m_a = tanh(β Σ_b J_ab m_b − β² m_a Σ_b J_ab²(1 − m_b²))

Le terme d'Onsager retire l'écho d'un agent sur lui-même, ce qui neutralise la récitation paramétrique recyclée par les pairs.

La récompense s'écrit :

R = Acc_holdout(m^TAP) − λ(q_EA − q*)² − μ Σ_e Δ_e − ν·Cov(jev, vérité_ancrée)

- Les sondes `jev` tournent et sont scellées.
- Le terme ν pénalise tout gain du juge qui n'est pas confirmé sur un sous-ensemble ancré par une vérité exogène : graphes arXiv, Semantic Scholar et Crossref, ainsi que des tâches postérieures à la date de coupure.

**3. Duel M3 (H_A ⊥ H_B)**

Le budget est fixé dans tous les bras à 100 USD Claude et 20 USD Gemini. On compare quatre bras :

| Bras | Description |
|---|---|
| (i) | AUC-q |
| (ii) | Topologie fixe |
| (iii) | Agents i.i.d. avec vote majoritaire |
| (iv) | Contrôle négatif : scissions déclenchées par un P(q) permuté, à fréquence identique |

- **H_A :** (i) obtient une précision vérifiée supérieure à (ii) et à (iii).
- **H_B :** le gain disparaît dans (iv). Cela prouve que c'est la détection de la transition RSB qui est causale, et non la simple mutation de topologie.

Le protocole est préenregistré, avec 20 graines et un test de permutation au seuil α = 0,01. Le critère de réfutation est l'absence de différence entre (i) et (iv).
