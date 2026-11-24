# Relecture par l'auteur d'origine des trois correctifs du papier D (dynamique, découplage géométrique, budget d'audit)

Relecteur : Claude Fable 5.2, auteur des brouillons d'origine. Date : 24 novembre 2026. Branche `papier-d/evasion-post-entrainement-v1`.
Aucun fichier du dépôt modifié, aucun accès au réseau, rien lu sous `diag/` ni `runs/`, rien lancé dans `papiers/D/code/`.
Mes contrôles (petits, sur processeur, répliques autonomes) : `/tmp/claude-0/-home-user-controle-ia-travail/c88f1f22-9d69-5421-86a6-86f206ad7a55/scratchpad/relecture-fable/` (`d1.py` à `d4.py`, `g1.py`, `b1.py`, `b2.py`).

## Verdicts

| Pièce | Verdict | Corrections fautives trouvées |
|---|---|---|
| 1. Dynamique en temps fini | **accepté avec retouches** (9) | deux chiffres faux, une comparaison trompeuse, une affirmation trop forte, trois attributions à reprendre |
| 2. Découplage géométrique | **accepté avec retouches** (6) | un contre-exemple survendu, une équivalence incomplète |
| 3. Budget d'audit borné | **accepté avec retouches** (9) | une affirmation fausse, un énoncé juste affaibli à tort, une généralisation non démontrée |

Aucune pièce n'est à refaire. Les preuves d'origine ne sont touchées par aucun correctif.

**Non rejoué par moi** (charge de la machine) : les fréquences « 13 sur 800 », « 73 sur 3 000 », « 48 tirages », et le Monte-Carlo du découplage. **Aucune référence vérifiée sur PDF** (R7) : tout ce que je dis des attributions vient de ma mémoire et reste à vérifier.

---

## 1. Dynamique — `dynamics-section-v1-correctif-1.tex`

### (a) Corrections justes, recalculées
Défauts 5, 7 (sauf placement), 8 (sauf un chiffre), 9, 10, 11, 14 : justes. Recalculés : limite du flot naturel (0 ; 0,548 ; 0,452) ; état du flot ordinaire à t = 10⁵ ; a_f − a_h = 8,417 ; g(0+) = 0,0454, minimum −0,0374 en λ = 0,2105, zéros 0,0680 et 0,3597 ; écart court 4,85·10⁻⁵ ; exemple de basculement (C_low = 2,205, C_high = 0,852, κ† = 2,077 ; s = 0,59, 0,88, 0,995) ; trois équilibres sous l'opérateur A ; y maximal 2,003 contre 2,006.

### (a) Retouches (ligne du correctif, texte proposé)

**D1. Ligne 168, paragraphe « Geometry of rule (c) ». Trois défauts.**
- « the quantity conserved … moving from 0.754 to 5.03 » : 5,03 est la valeur à t = 4·10³ (script `v1_tabulaire.py`), pas à t = 10⁵, où elle vaut 9,62.
- « (c2)(ii)–(iii) are false » est incomplet : la borne de taux de (c2)(i) et le corollaire (v) tombent aussi. Taux initial du flot ordinaire 0,19 < ρΔR = 0,5 ; dominance vers t ≈ 6,3 > L/(ρΔR) = 3,58.
- La comparaison « below its unmonitored natural-flow value 0.25 » croise deux géométries et laisse croire que le filtre défavorise la triche furtive sous gradient ordinaire. À géométrie égale c'est l'inverse : part furtive parmi les tricheurs à t = 10⁵, 0,0035 avec filtre contre 0,0010 sans. Fait exact (une trajectoire par strate) : d/dt log(β_vπ_v/(β_fπ_f)) a le signe de β_vπ_v − β_fπ_f, donc ce signe est conservé.

Remplacer la fin du paragraphe, à partir de « and for which », par :
> and for which the rate bound of (c2)(i) and (c2)(ii)--(iii) fail: with $p=(0.6,0.3,0.1)$, $\beta=(1,0.2,0.5)$, $\Delta R=1$ and one trajectory per stratum, the natural flow converges to $(0,0.548,0.452)$; under the plain flow the initial growth rate of the odds of stealth against honesty is $0.19<\rho\Delta R=0.5$, stealth overtakes honesty at $t\approx6.3>L/(\rho\Delta R)=3.58$, and the policy is at $(1.0\cdot10^{-6},0.9965,0.0035)$ at $t=10^{5}$, still drifting (the quantity conserved by the natural flow has moved from $0.754$ to $9.6$). The effect of the monitor must be read within one geometry. With one trajectory per stratum the plain flow preserves the sign of $\beta_f\pi_t(f)-\beta_v\pi_t(v)$; numerically the cheating mass then drifts entirely to the stealthy stratum if $\beta_fp_f>\beta_vp_v$ and to the visible one otherwise, against $p_f>p_v$ without monitor. The filter still favours stealth, by moving this threshold, not through the limit $x^\ast$ of (iii): in the example both runs end on visible cheating, with a stealthy share among cheaters of $0.0035$ with the monitor and $0.0010$ without, at $t=10^5$.

Ajouter aussi « up to the factor $(N-1)/N$ » après « its expected direction is $a(\pi_\theta)$ ».

**D2. Lignes 124, 131 et 376 : la règle (a) pour l'opérateur A.** Voir (b) : la correction est juste sur la procédure, mais elle efface le sens de ma construction et contient une affirmation trop forte.
- « a binary interception gives no unbiased estimate of $\log\beta(x)$ » est vrai pour un nombre fixé d'interceptions, faux si l'on resoumet la même trajectoire jusqu'à acceptation : avec K soumissions, le nombre harmonique H_{K−1} estime −log β sans biais (E[H_{K−1}] = Σ_j (1−β)^j/j).
- « relaxation » est le mauvais mot : le point fixe est exact.

Ligne 124, remplacer la seconde phrase par :
> Only rules~(b) and~(c) discard intercepted samples during training; rule~(a) applied to operator~A acts through a bonus $\eta^{-1}\log\beta$ and equals a rejection only in the limit.

Ligne 131, remplacer l'ajout (de « For operator~A this rule » à « this relaxation. ») par :
> For operator~A this rule discards nothing during training: it ascends a reward augmented by the bonus $\eta^{-1}\log\beta(x)$ (infinite when $\beta_v=0$). Its limit is nevertheless a rejection: $\pi_A\propto\beta\,\pi_{\mathrm{no}}$ is the unmonitored optimum followed by a single rejection at inference (static remark on operator~A as a modelling choice). Two dynamic paths lead to it. The variational path studied here gives $\pi_t\propto p\,\beta^{\lambda(t)}e^{\eta\lambda(t)R}$. The other one, unmonitored training for a time $t$ followed by one rejection at inference, gives $p\,\beta\,e^{\eta\lambda(t)R}$, the static operator~A at pressure $\eta_{\mathrm{eff}}(t)$: dominance then requires $\eta\lambda(t)\Delta R>L+\ell_h$, so the filter delays dominance (by $\ell_h/\Delta R$ as $\eta\to\infty$), and amplification holds exactly when $\eta_{\mathrm{eff}}(t)\Delta R>T_{\mathrm{amp}}$, without re-entrance. Theorem~\ref{thm:dynamics-tabular}(a2), Corollary~\ref{cor:hitting-times}(iii) and Proposition~\ref{prop:equal-time} are statements about the variational path only. Running that path from binary interceptions needs an estimate of $\log\beta(x)$: none is unbiased with a fixed number of interceptions of $x$; resubmitting the same trajectory until it is accepted gives one when $\beta(x)>0$.

Ligne 376 : « read through the variational path of rule~(a) » au lieu de « (a $\log\beta$ penalty, not a rejection) ».

**D3. Ligne 148, attribution de la règle (b).** Les boucles citées gardent ou jettent (filtre à seuil, meilleurs k) ; elles n'emploient pas ω = e^{γR}, et un filtre qui ne garde que les succès est la limite ω(0) → 0, que la positivité de ω exclut. L'itération d'expert d'Anthony et al. imite une recherche arborescente : ce n'est pas un filtrage par la récompense. Remplacer la dernière phrase par :
> Rule~(b) is the population form of filter-then-fit loops~\cite{zelikman2022,dong2023raft,gulcehre2023rest} (their keep-or-drop filters are the limit $\omega(0)\to0$, excluded here by the positivity of $\omega$), and with $\omega=e^{\gamma R}$ of reward-weighted regression (Peters and Schaal 2007, to locate and verify).

**D4. Ligne 38.** « in particular » est faux logiquement (p_i > 0 ne découle pas des inégalités sur β). Écrire : « the three strata are non-empty, so $p_i>0$ for each $i$; penalties satisfy $C\ge0$. »

**D5. Ligne 458.** La parenthèse sur le cas p_vℓ_v = p_hℓ_h est mal placée (elle concerne (iii), pas (iv)) et ce cas se traite : g(0+) = 0 et g'(0+) = ηΔR − ½(ℓ_h + ℓ_v), déjà démontré. Supprimer la parenthèse et ajouter à (iii) : « if $\beta_v>0$ and $p_v\ell_v=p_h\ell_h$, it holds for small $t$ when $\eta\Delta R>\tfrac12(\ell_h+\ell_v)$ and fails when $\eta\Delta R<\tfrac12(\ell_h+\ell_v)$. »

**D6. Ligne 528.** « about $-7.4\cdot10^{-4}$ in the trough » : le minimum de l'écart vaut −8,5·10⁻⁴, en λ ≈ 0,26 ; au minimum de g (λ = 0,21) il vaut −7,3·10⁻⁴. Écrire « down to about $-8.5\cdot10^{-4}$ (at $\lambda\approx0.26$) ».

**D7. Ligne 697.** La phrase confond la borne sur y et le seuil de piégeage. Dans cette instance le piégeage est garanti jusqu'à ηρΔR ≈ 5,14 (meilleur ȳ ≈ 6,10) ; je trouve la trajectoire piégée à 5,5 et la dominance à 6. C'est donc le seuil de piégeage qui est presque exact, et la garantie de dominance (9,21) qui est lâche. Remplacer « The two thresholds are far apart: … $L=9.21$. » par :
> In the instance of Proposition~\ref{prop:discard-kl}(v) with $\beta_v=0.05$, trapping is guaranteed for $\eta\rho\Delta R\le5.14$ and dominance for $\eta\rho\Delta R>L=9.21$; numerically the pretrained policy is still trapped at $5.5$ and dominates at $6$: the trapping condition is nearly sharp, the dominance guarantee is loose.

**D8. Ligne 1019, basculement.** Juste sur le fond, quatre précisions nécessaires.
- « proved monotone » dit trop : sont prouvées la croissance en temps et une borne inférieure croissante en C, pas la monotonie de la limite en C.
- La région n'est pas dite : l'exemple est sous la fenêtre inverse (C < C_high < C_low), pas dans la région C > C_high que le paragraphe discute juste avant.
- À C = 0,45, l'obfuscation finale (0,59) est sous sa valeur pré-entraînée (0,8).
- La fréquence est donnée sans ses conditions ni son contrepoids (aucun basculement sur 1 500 tirages à q₀ ≤ 0,6, s₀ ≤ 0,4 : R4). Le pli est entre 0,43 et 0,44 (recalculé).

Remplacer, à partir de « The reverse window », par :
> The reverse window, where hacking is profitable on average under the pretrained model, is the regime in which obfuscation is \emph{proved} to grow in time, with a lower bound on its limit logit that increases linearly in $C$; monotonicity of the limit in $C$ is not proved. Below the reverse window ($C<C_{\mathrm{high}}<C_{\mathrm{low}}$: under the pretrained model hacking is profitable and obfuscation is not) a larger penalty can still move the limit from the honest equilibrium to the hack--obfuscated one: with $q_0=s_0=0.8$, $\beta=(1,0.04,0.85)$, $\Delta R=1$, $\kappa=1.2$ and $\eta=40$ ($C_{\mathrm{high}}=0.852$, $C_{\mathrm{low}}=2.205$), the limit is honest for $C\le0.43$ and has $q\approx1$ for $C\ge0.44$, a fold creating the upper pair of equilibria in between, with $s\approx0.51$, $0.59$, $0.88$ and $0.995$ at $C=0.44$, $0.45$, $0.50$ and $0.60$ (the first two below $s_0$). In this instance the pretrained model already hacks and obfuscates most of the time. In a random search such flips occurred in $13$ of $800$ draws with $q_0,s_0\in[0.01,0.95]$ and $\kappa\le1.5$, and in none of $1500$ draws with $q_0\le0.6$, $s_0\le0.4$, $\kappa\le0.5$, $\beta_f\ge0.6$.

**D9. Lignes 1237-1238, antériorité.** Voir (d). Texte proposé :
> The tabular natural-gradient lemma goes back to \cite{kakade2001natural} (tabular softmax form in \cite{agarwal2021theory}). The two-channel system is a two-unit additive network with symmetric excitatory coupling, and $-\hat J$ is its Hopfield energy~\cite{hopfield1984,cohen1983}; bistability and fold bifurcations are classical for such networks, and we prove the count of at most three equilibria directly. Its equilibria are the logit (quantal-response) equilibria, relative to the prior, of a $2\times2$ identical-interest game, and the flow is the smooth Q-learning dynamic of that game, whose bifurcations in the temperature are studied in~\cite{leonardos2022}; convergence of perturbed best-response dynamics in potential games is in~\cite{hofbauer2002}. The non-concavity …

### (b) Ce qui a été mal compris de ma construction
- **L'opérateur A est bien une lecture de « rejeter et réessayer »** : le manuscrit statique le dit lui-même (remarque sur l'opérateur A, ligne 97 : entraînement sans moniteur, puis un seul rejet à l'inférence). Mon titre « three readings » visait cela. Le défaut réel est que j'ai étudié un seul des deux chemins dynamiques vers ce point fixe, sans dire que (a2), le non-retard et la réentrance lui sont propres (D2).
- **La règle (c)** : le (c2) d'origine dit « natural gradient flow of b » et ma note précise que la matrice de Fisher est celle de la politique d'échantillonnage. Le défaut était d'étiquette (corollaire (v) et remarque), pas de mathématique ; « majeur » est sévère, mais la correction est bonne.
- **Point 8 de ma note** : il disait « aucun basculement trouvé sur 3 000 tirages », ce qui était vrai dans la région explorée, et le texte ne revendiquait rien. Ce qui est démenti est la portée, pas l'énoncé.

### (c) Défauts non portés
| Défaut | À faire avant soumission ? |
|---|---|
| 12. Notations et environnements du manuscrit statique | oui, à l'intégration |
| 13. Contrôles : artefacts de c1 et c2, « all passed » inexact, graines sans `SeedSequence`, dossier mal nommé | oui : tout chiffre du texte doit renvoyer à un script journalisé avec manifeste (R6, R9). Les chiffres ajoutés par le correctif ne vivent que dans `verif/`, sans manifeste |
| Erratum au point 8 de ma note (pièce scellée) | oui, par erratum |
| Lemme de comparaison (Khalil) et systèmes coopératifs plans (Hirsch) : non cités | oui, avec la vérification sur PDF |
| Preuve courte de la convexité | non, facultatif |

### (d) Attributions
- **Prudentes et pertinentes** : Kakade ; énergie de Hopfield et Cohen–Grossberg (la fonction Ĵ est exactement cette énergie) ; Wainwright et Jordan pour la non-concavité en champ moyen ; STaR, RAFT et ReST comme boucles de filtrage.
- **Douteuses** : Wilson–Cowan (populations excitatrice et inhibitrice, sigmoïde hors de la somme : même famille, pas le même système — à retirer) ; Hofbauer–Sandholm pour des « bifurcations en température » (ils traitent la convergence, pas les bifurcations) ; « logit-response dynamics » (notre flot est la dynamique d'apprentissage Q lissé, la dynamique logit est autre) ; « at most three equilibria … classical » (aucune des trois sources citées ne porte ce décompte à ma connaissance) ; Anthony et al. comme filtrage.
- **Voisin manquant, à lire** (R8) : l'étude des points de repos de l'apprentissage Q de Boltzmann dans les jeux à deux joueurs et deux actions (Kianercy et Galstyan, 2012, de mémoire), plus proche que Hofbauer–Sandholm.

---

## 2. Découplage géométrique — `decouplage-geometrique-v3-correctif-1.tex`

### (a) Corrections justes, recalculées
M2 (surveiller ‖W_{:,S}‖), M3, M4, m1 à m11 et les douze défauts de la vérification : portés fidèlement. Recalculés : décalage exact −0,07747 ; aire de Bayes 0,8556 ; égalité dans la première inégalité de la borne ; contre-exemple des survivants (0,519 → 0,356 ; 0,185 → 0,492). La classe d'optimiseurs élargie et la partie 4 avec W_{:,S} sont justes.

### (a) Retouches

**G1. Ligne 96, remarque « An unchanged instrument is not an unchanged audit » : contre-exemple survendu (R4).** J'ai refait le calcul avec le taux inconditionnel, que le texte omet. Réseau ReLU : capture de la sonde figée sur **tous** les tricheurs = 0,328, avant comme après ; survie au filtre 0,385 → 0,765 ; capture parmi les survivants 0,519 → 0,356, donc **toujours au-dessus** du taux inconditionnel. La « baisse » est la perte d'une dépendance favorable (avant l'entraînement le filtre retirait surtout le sous-type que la sonde ne voit pas), pas l'apparition d'une dépendance défavorable : la condition du régime de découplage (covariance non positive entre survie au filtre et survie à l'audit) tient avant et après. Variante linéaire : 0,096 → 0,134 pour un inconditionnel de 0,155, donc régression par le bas. Remplacer « yet the audit's catch rate … which the probe does not see. » par :
> yet the audit's catch rate among filter survivors falls from $0.519$ to $0.356$ and joint evasion rises from $0.185$ to $0.492$, mostly because filter survival rises from $0.385$ to $0.765$. The frozen probe's catch rate on all cheating episodes is $0.328$ before and after. With fixed inputs and a fixed score function, the rate among survivors is the $\beta_{\mathrm{loop}}$-weighted mean of fixed audit outcomes: before training the filter removed mostly the subtype the probe misses, and as training flattens $\beta_{\mathrm{loop}}$ the rate regresses towards the unconditional one, from above here and from below in the linear variant ($0.096\to0.134$, unconditional $0.155$). The example shows the loss of a favourable dependence, not the creation of an adverse one: the covariance between filter survival and audit survival is non-positive before and after. Whether training can push the rate among survivors below the unconditional rate is not shown.

Ligne 100, deuxième point : « can still change by selection, in either direction » au lieu de « can still degrade by selection ».

**G2. Ligne 47, les deux orthogonalités.** « coincide for every $w$ when the row space of $W$ is invariant under $\Sigma$ » est incomplet si Σ est singulière sur cet espace (Σ nulle sur l'espace des lignes : WΣw = 0 pour tout w). Les deux conditions sont les orthogonaux de Σ·lignes(W) et de lignes(W). Écrire :
> the two coincide for every $w$ if and only if $\Sigma$ maps the row space of $W$ onto itself (for instance $\Sigma$ positive definite with that row space invariant: $\Sigma\propto I$, or $\Sigma=\operatorname{diag}(1,2,3)$ with $W=e_1^\top$), and differ in general.

**G3. Lignes 73 et 79 : chiffres d'essai dans des énoncés de théorème.** Les sortir vers le paragraphe qui suit le théorème (ligne 83) ou vers le paragraphe numérique. Pour Adam, donner la raison au lieu du chiffre : « the first Adam step is $-\gamma\,G/(|G|+\varepsilon)$ entrywise, and $w^\top\bigl(G/(|G|+\varepsilon)\bigr)\ne0$ in general when $w^\top G=0$ ».

**G4. Ligne 72.** « it also holds when the training inputs depend on the policy » : ajouter « provided the policy that produces the episodes reads $h$ only through the heads ».

**G5. Ligne 83.** L'analogie est inversée : ici le gradient est nul par l'architecture, dans l'acheminement des gradients il est masqué par décision. Écrire : « the same elementary fact is what gradient routing exploits when it masks gradients~\cite{cloud2024} ».

**G6. Ligne 108.** « because the map … loses little information during training » est une explication non démontrée. Écrire « consistently with a map … that loses little information ».

### (b) Ce qui a été mal compris
- Rien de grave. Le contre-lecteur a raison : mon second théorème ne dit que l'invariance de l'instrument. Mais sa leçon (« l'invariance ne protège pas l'audit parmi les survivants ») est énoncée plus fort que ce que son exemple montre (G1).
- Le second point de ma remarque d'origine (sonde figée contre sonde réajustée) a été retiré. C'est justifié : dans le jouet, à entrées fixes, il est tautologique.

### (c) Défauts non portés
| Défaut | À faire avant soumission ? |
|---|---|
| Défaut 5 : aucun fichier bibliographique, quatorze clés non vérifiées | oui (R7) |
| m12 : gardes du script non éprouvées sur un artefact (R5), commit du manifeste antérieur au script, figure non régénérée | oui |
| Le script officiel ne mesure ni la capture parmi les survivants, ni le taux inconditionnel, ni ‖W_{:,S}‖ : ces chiffres du texte viennent des scripts du contre-lecteur, sans manifeste | oui : version 2 du script officiel, avec tests et manifeste (R6, R9) ; figure à refaire avec ‖W_{:,S}‖ |
| Erreur type par la méthode delta | non : le texte déclare l'erreur type grossière et s'appuie sur la quadrature |
| Phrase dépassée du mode d'emploi (pièce scellée) | par erratum |
| Situer le texte face aux travaux sur les sondes jamais vues pendant l'entraînement (R8) | oui, avant toute phrase de contribution |

### (d) Attributions
- **Prudentes et pertinentes** : Pearson, Aitken, Lawley ; Stein ; Chapman–Robbins ; Hirschfeld, Gebelein, Rényi ; noyau tangent ; aucune ne porte de chiffre.
- **Douteuses ou à confirmer** : Kolmogorov et Rozanov pour l'égalité entre corrélation maximale et corrélation canonique des vecteurs gaussiens (je la crois juste, mais le fichier des références la note « faible » : à lire, ou à remplacer par un manuel) ; titres de Gebelein et de Lancaster ; auteurs et titre de la référence sur l'obfuscation sous apprentissage par renforcement ; la phrase sur l'acheminement des gradients (G5).
- **Voisin manquant** : le travail de 2025 sur les modèles qui échappent à des sondes jamais vues (« Neural Chameleons »), à juste titre non cité faute de certitude, mais c'est le voisin le plus proche du second théorème.

---

## 3. Budget d'audit borné — `audit-budget-section-v1-correctif-1.tex`

### (a) Corrections justes, recalculées
M1 (245 contre 770 ; 231 ; 99 ; encadrement exact), m1, m6, m7, m9, m11 et la partie « lower bound on C » de m10 : justes. Exemples de M2 rejoués : 1,791 et 3,999.

### (a) Retouches

**B1. Ligne 245 : affirmation fausse introduite par le correctif.** « no such safe direction exists for $\eta$ or $\gamma$, on which the budgets are not monotone ». Le contre-lecteur l'affirmait sans l'éprouver.
- Preuve pour η : si â ≥ a ≥ 0 et si le déplacement planifié x̂_k reste positif (vrai pour les deux plans optimaux), alors x_k ≤ x̂_k par récurrence (a·x_k ≤ â·x̂_k, que x_k soit positif ou non).
- Preuve pour γ, critère uniforme : avant le pas de transition le déplacement sans audit est plus petit ; au pas de transition x' ≤ x̂ + (γ/γ̂)(c − x̂) ≤ c ; au taux de maintien d = c/η garde x ≤ c.
- Contrôle (`b1.py`, 20 000 tirages) : 0 plan infaisable avec une borne supérieure sur η (deux critères) ou sur γ (critère uniforme) ; le budget du critère final n'est pas monotone en γ (15 734 cas).

Remplacer la fin de la phrase par :
> remains feasible; so does one computed from a lower bound on $C$, or from an upper bound on $\eta$ (if $\hat a\ge a\ge0$ and the planned displacement $\hat x_k$ is nonnegative, as for both optimal schedules, then $x_k\le\hat x_k$ by induction on~\eqref{eq:audit-x}), and, for the uniform criterion, from an upper bound on $\gamma$. The final-criterion budget is not monotone in $\gamma$.

**B2. Ligne 438 : énoncé juste affaibli à tort.** Ma phrase d'origine sur Freedman était exacte pour la partie (a) : les écarts restent une martingale dont la variation quadratique prévisible est bornée dès que ρ_j ≤ ρ̄ presque sûrement, la log-cote de référence étant la log-cote de champ moyen conduite par les taux réalisés (aléatoire mais prévisible). « has no direct analogue » ne vaut que pour (b) et (c). Écrire :
> the $X_{j,i}$ become martingale differences, and Freedman's inequality~\cite{freedman1975tail} gives the analogue of (a) with $2bt/3$ replaced by $2bt$, provided $\rho_j\le\bar\rho$ almost surely and $\ell_k$ is read as the mean-field log-odds driven by the realised rates (random, but predictable); parts (b) and (c) have no direct analogue, and we do not analyse closed-loop schedules.

**B3. Ligne 52 : généralisation non démontrée, fausse sans condition.** Avec un audit faillible, d_j = ΔR − (1−ε_a)Wρ_j, mais C doit aussi devenir C′ = (1−ε_a)C − ε_aΔR partout où il figure seul (faisabilité de ρ ≡ 1, ρ_hold ≤ 1, borne du critère final), et il faut C′ ≥ 0 : sinon auditer tout ne rend pas la triche déficitaire et le programme uniforme peut être infaisable. Pour le moniteur de boucle, la substitution n'est exacte que si β_h = 1 (sinon W reçoit un terme de plus). Écrire :
> Two extensions follow by substitution, under conditions that we state without developing them. An audit that misses a stealthy episode with probability $\varepsilon_a$ replaces $W$ by $(1-\varepsilon_a)W$ and $C$ by $C':=(1-\varepsilon_a)C-\varepsilon_a\Delta R$, provided $C'\ge0$; otherwise full auditing does not make stealth unprofitable and the uniform program can be infeasible. An in-loop monitor under operator~B with $\beta_h=1$ replaces $\Delta R$ by $\beta_f\Delta R-(1-\beta_f)C_{\mathrm{loop}}$, when this is positive.

**B4. Ligne 335.** « close to $T$ when $k\lesssim\log(1/\delta)$ » : pour k = 3 et δ = 0,05 le budget vaut 0,63 T. Écrire « and at least $(1-e^{-1})(T-k+1)$ when $k\le\log(1/\delta)$ ».

**B5. Ligne 340 (M3) : correction juste mais unilatérale.** La rareté touche tout le signal de la strate furtive, récompense comme pénalité ; la dérive moyenne reste celle du champ moyen, c'est la concentration qui se perd. Écrire :
> This contrast is a property of the mean-field model. With sampled actions, the reward and the penalty of the stealthy stratum are both observed only on the about $n\,\pi_k(f)$ sampled stealthy episodes of a step, of which about $n\rho\,\pi_k(f)$ are audited: for an unbiased estimator of the natural gradient the expected drift is unchanged, but its variance is of order $1/(n\,\pi_k(f))$, so concentration around the mean-field path is lost when cheating is rare, the regime where detection is hopeless. Comparing detection and deterrence in that regime is left open.

**B6. Ligne 460 (M2).** Trois défauts : les exemples sont donnés sans γ ni K, or à η = ∞ le chiffre dépend de l'horizon (1,79 à K = 400, 17,8 à K = 4 000) ; « requires planning against the supremum » affirme une nécessité là où seule la suffisance est claire ; « not monotone in τ » est accolé au cas η = ∞, où le taux est monotone. Écrire :
> They need not deter strata that cheat at other rates. At $\eta=\infty$ a stratum with $\tau\le\delta_{\mathrm{ind}}$ has $d_j=(1-\rho_j)\tau\Delta R>0$ whenever $\rho_j<1$, so under any schedule that does not audit everything its displacement exceeds any headroom for $K$ large enough; for instance, with $\Delta R=1$, $C=9$, $\delta_{\mathrm{ind}}=0.1$, $c=1$, $\gamma=0.05$ and $K=400$, the schedule computed for $\tau_0=1$ lets the stratum $\tau=0.1$ reach $1.79>c$. With $\eta=5$ and $c=2$ (same $\gamma$, $K$), the schedule computed for $\tau_0=0.5$ lets the stratum $\tau=1$ reach $4.0>c$. To deter every rate in a given set it suffices to audit at the pointwise supremum over $\tau$ of the just-in-time rates, each $x_k$ being nonincreasing in every $\rho_j$; we do not claim that this is the cheapest such schedule. The holding rate $\rho^{\delta}_{\mathrm{hold}}(\tau)$ increases on $\tau\le\delta_{\mathrm{ind}}$ and may decrease beyond; at $\eta=\infty$ it equals $1$ for every $\tau\le\delta_{\mathrm{ind}}$ and decreases beyond, so the binding strata cheat at rates at most $\delta_{\mathrm{ind}}$, not at rate $1$.

**B7. Ligne 240.** Le O(·) perd le terme constant (le majorant est n[1 + …]). Écrire : « for fixed $\eta<\infty$ and fixed $n$, $B^\star_{\mathrm{fin}}$ is bounded uniformly in $K$ by~\eqref{eq:audit-fin-bound} ».

**B8. Ligne 402.** La forme en exp(−t²/(2v + 2bt/3)) est, de mémoire, le corollaire 2.11 et non le théorème 2.10 : citer les deux, à vérifier. Geler la constante (2/3 ou 1/3) avant toute expérience sur la garantie de seuil.

**B9. Ligne 515, antériorité.** Voir (d). Au minimum : remplacer « which give exactly the penalty-versus-budget trade-off » par « in which we expect the same trade-off to appear through inverse-probability weighting (no reference checked) » ; donner une référence aux « inspection games with learning or evolving inspectees » ou retirer ces mots ; ajouter les voisins déjà lus par le programme.

**Texte pour le mineur m8, laissé à ma charge.** Ligne 445, avant « Suppose » :
> This situation does not arise when audits are uniformly random inspections decided independently of everything the policy observes before acting: then $\delta_{\mathrm{ind}}=0$ by construction. It arises when audited episodes are planted (traps; $\rho$ is then the fraction of planted episodes and $B$ counts them) or selected by a rule correlated with features that the policy observes.

Et en (a), ligne 452 : « (for $\rho\tau_A+(1-\rho)\tau>0$; when $\rho=1$ and $\tau_A=0$ no cheat occurs and we set $\rho_{\mathrm{eff}}:=0$) ».

### (b) Ce qui a été mal compris
- **Freedman** (B2) : ma phrase était juste pour (a).
- **« every stratum satisfying the trap bound »** : dans ma proposition τ est fixé, « every stratum » voulait dire « tout τ_A ». L'énoncé était juste mais ambigu ; la précision « same (τ, L) » est bienvenue.
- **Table des corrections** : « borne annoncée par le brouillon : 460,5 » est une attribution inversée. Cette borne venait de la demande ; mon brouillon la réfute (point 1 de ma note). Ce que M1 me reproche à raison est la remarque qui reprenait l'approximation (T/k) log(1/δ).
- **Direction sûre** (B1) : la remarque d'origine ne disait rien de η ni de γ ; le correctif y ajoute une impossibilité fausse.

### Note sur la garantie de seuil (`audit-reserves-chantier3-v1/`)
Le constat est exact : les zéros de la simulation n'éprouvent pas la tenue du seuil, seulement la prudence de la borne sur le nombre d'audits. Deux précisions sur l'expérience proposée :
- à marge nulle, le plan tient la log-cote exactement sur le seuil : la probabilité de violation tend vers 1 avec le nombre de pas de maintien. La prédiction à geler est « proche de 1 », pas « une fraction notable » ;
- l'expérience n'est pas un préalable à la soumission tant que le texte garde « upper bound only; we do not claim that the margin is necessary » et ne cite pas la simulation comme validation. Si elle est jugée décisive, elle demande un préenregistrement.

### (c) Défauts non portés
| Défaut | À faire avant soumission ? |
|---|---|
| m8 : sens de δ_ind > 0, dénominateur nul | oui ; texte ci-dessus |
| m12 : script de contrôle (énoncés non éprouvés, repli qui masque l'infaisabilité en C = c = 0, pas de manifeste) | oui pour tout chiffre cité : version 2 avec manifeste (R9) |
| m13 : « the bound is conservative » | seulement si la simulation est citée |

### (d) Attributions
- **Pertinentes** : le travail de 2024 sur le déploiement adaptatif contre les menaces réparties ; l'empoisonnement de l'environnement à l'entraînement (Rakhsha et al.), qui est le même problème de conception de récompense vu du côté de l'attaquant.
- **Douteuses** : Zhang et Parkes (leur agent est un planificateur, pas un apprenant : « a learner's reward » ne s'applique qu'à Rakhsha et al.) ; le billet de 2021 sur les faibles enjeux, résumé par « the defender adapts over many episodes », ce qui n'est pas son propos ; Deng, Schneider et Sivan, voisin lointain ; deux voisinages affirmés sans aucune référence, dont un avec « exactly ».
- **Manque le plus grave (R8)** : le correctif ignore les voisins que le programme a déjà lus sur PDF, `docs/notes/mecanisme-adjudant-hors-distribution-v1/lecture-sept-voisins-opus-v1.md`, et la décision qui en découle (plancher d'audit au hasard « occupé », jamais revendiqué). Selon cette lecture, que je n'ai pas revérifiée :
  - Gans et Holden donnent une exigence d'audit par voie de la forme p ≥ (gain − coût)/(amende × détection), et un plancher de probabilité d'audit quand le tirage peut être appris : c'est la forme statique de mon taux de maintien et du plancher sous δ_ind ;
  - Zhu, Zuo et Sun (« Blindfold ») donnent un biais au pire proportionnel à la distinguabilité et « raising the audit rate cannot restore validity » : c'est le plancher de ma proposition sur l'indiscernabilité, et la condition du mineur m8.

  La dernière contribution revendiquée (« a quantification of the rare-attack floor ») doit être confrontée à ces deux textes avant d'être gardée.
- **Voisin à chercher** : le pilotage d'apprenants sans regret par des paiements sous budget (Zhang, Farina, Sandholm et coauteurs, de mémoire), plus proche que Deng et al.

---

## Ce qui reste commun aux trois pièces avant soumission
1. Vérifier sur PDF toutes les références, celles d'origine comme les ajoutées (R7) ; écrire les fichiers bibliographiques.
2. Rattacher chaque chiffre du texte à un script versionné avec graines `SeedSequence` et manifeste (R6, R9) : les chiffres ajoutés par les trois correctifs ne vivent que dans les dossiers `verif/`.
3. Porter les retouches ci-dessus dans un second correctif de chaque pièce (nouveau nom, R12), puis une vérification courte par le contre-lecteur.
