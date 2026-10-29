BASSIN_MATH: Lande-Arnold à Matrice-G Décorrélée et Parasites Gène-pour-Gène de Flor (LAG-GFG)

LOI_PROPOSEE: $\Delta\bar z = G\,\beta + \mu\,\varepsilon$, avec $\beta = P^{-1}\operatorname{Cov}(w,z)$ et $G \leftarrow G - \kappa\,\mathrm{offdiag}(R_{\text{err}})$. Le budget $b_i$ suit $\dot b_i = b_i(\hat w_i - \bar w) + \nu\,(\bar b - b_i)$, sous les plafonds 100 USD Claude et 20 USD Gemini.

1. **Mécanisme d'auto-organisation et d'entraînement hors-poids**
   - **Génome.** Chaque lignée porte un vecteur de traits $z$, sans aucune modification de poids. Ce vecteur contient la matrice d'adjacence (qui parle à qui), le ratio explorateur/démolisseur, la part de chaque famille (Fable, Opus, Argon), la profondeur maximale de délégation et le gabarit de consigne.
   - **Gradient de sélection.** Toutes les $k$ générations, on régresse la fitness $w$ sur $z$ pour obtenir $\beta$.
   - **Matrice G.** $G$ est la covariance des traits entre lignées. Ses termes hors-diagonale sont amputés de $R_{\text{err}}$, la corrélation d'erreurs entre familles mesurée gratuitement par `jev-1.14.0`. Ce couplage combat $H4'$.
   - **Arbitrage monoculture ou chimère.** Un sous-agent est spawné dans le sens de $G\beta$. La chimère est choisie si $\rho_{\text{intra}} > \rho_{\text{inter}} + \delta$, sinon la monoculture est conservée.
   - **Red-Team gène-pour-gène.** Les démolisseurs portent des « gènes d'avirulence » $a \in \{0,1\}^m$, qui sont des classes d'attaque (récitation, dérive, citation fantôme). Un hôte résiste si $\forall j,\ a_j \le r_j$. On spawne un démolisseur lorsque la fréquence des parasites non couverts dépasse $\theta$.
   - **Archive MAP-Elites.** Elle est indexée par (sous-question, famille, profondeur) et conserve la diversité.

2. **Fonction objectif et anti-Goodhart**

$$w = \frac{N_{\text{vérif}}}{\$} - \lambda\,\bar\rho_{\text{err}} - \mu\,D_{\text{jev}}(\text{consigne}_0,\text{consigne}_d) - \eta\,\mathrm{Rec} - \gamma\,S_{\text{parasites}}$$

   - $N_{\text{vérif}}$ compte les nouvelles cellules d'archive validées par les graphes Crossref et Semantic Scholar (DOI existant et postérieur au gel).
   - $\mathrm{Rec}$ est le taux de récitation, c'est-à-dire les affirmations sans source.
   - $S_{\text{parasites}}$ est le succès des parasites archivés, en mode décalé dans le temps.
   - Mesures anti-Goodhart : 30 % des items sont jugés par un juge caché, sur des seuils jev non exposés, et $\beta$ n'est estimé que sur la partie publique.

3. **Duel décisif $H_A \perp H_B$**
   - **Hypothèses.** $H_A$ : la dynamique $G\beta$ décorrélée cause le gain. $H_B$ : le seul mélange chimérique suffit.
   - **Bras expérimentaux**, tous à budget identique de 100 USD et 20 USD :
     - (i) LAG-GFG ;
     - (ii) chimère fixe aux proportions finales de (i) ;
     - (iii) agents i.i.d. ;
     - (iv) contrôle négatif : LAG-GFG avec $w$ permuté, qui doit égaler (iii).
   - **Protocole.** 10 graines par bras, analyse préenregistrée.
   - **Critères.** Le critère principal est le nombre de cellules vérifiées par dollar. Les critères secondaires sont $\bar\rho_{\text{err}}$, la dérive $D_{\text{jev}}$ et $\mathrm{Rec}$.
   - **Test statistique.** Wilcoxon apparié avec correction de Holm.
   - **Décision.**
     - $H_A$ est acceptée si (i) > (ii) > (iii) et si (iv) ≈ (iii).
     - $H_B$ est acceptée si (ii) ≈ (i).
