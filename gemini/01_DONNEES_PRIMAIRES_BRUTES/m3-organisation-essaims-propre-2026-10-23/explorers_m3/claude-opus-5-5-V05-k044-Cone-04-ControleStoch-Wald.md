BASSIN_MATH: Conception Séquentielle de Chernoff à Information Décorrélée par Dollar (CSC-IDD)

LOI_PROPOSEE: $a_t=\arg\max_{a\in\mathcal A}\dfrac{(1-\hat\rho_a)\,\min_{j\neq\hat\jmath_t}\mathrm{KL}\!\left(P_{\hat\jmath_t,a}\,\|\,P_{j,a}\right)}{\lambda_C c^C_a+\lambda_G c^G_a}$. On arrête dès que $\Lambda_t=\log\dfrac{p_{\hat\jmath}}{\max_{j\ne\hat\jmath}p_j}\ge\log\dfrac{1-\beta}{\alpha}$.

**1. Mécanisme d'auto-organisation hors-poids**

- **Actions et hypothèses.** Une action $a=(\text{famille},\text{rôle},\text{arête})$ précise la famille parmi fable, opus, argon ou une chimère, le rôle (explorateur ou démolisseur Red-Team) et l'arête de communication. Les hypothèses $\{H_j\}$ portent sur la véracité de chaque affirmation et incluent explicitement « récitation paramétrique ».
- **Choix de l'action.** À chaque pas, l'essaim applique la règle de Chernoff, active et séquentielle. Il ne spawne que l'agent qui maximise l'information discriminante contre l'alternative la plus proche, par dollar dépensé.
- **Rôles.**
  - Un explorateur est spawné quand la divergence de Kullback-Leibler (KL) est maximale vers des hypothèses non couvertes.
  - Un démolisseur est spawné quand l'alternative la plus proche est l'hypothèse « faux plausible ».
- **Corrélation des erreurs (H4').** Un filtre particulaire estime la corrélation latente d'erreurs $\hat\rho_a$ entre familles à partir des désaccords notés par `jev-1.14.0`. La chimère l'emporte sur la monoculture exactement quand le facteur $(1-\hat\rho_a)$ compense son surcoût.
- **Dérive de consigne (H9).** Un CUSUM $S_t=\max(0,S_{t-1}+d_t-\kappa)$ suit $d_t$, la distance `jev` entre la consigne déléguée et la consigne racine. Si $S_t>h$, la branche est élaguée et re-spawnée depuis la racine.
- **Non-stationnarité.** Les vraisemblances $P_{j,a}$ sont apprises par Thompson escompté (facteur $\gamma$). Elles sont réinitialisées dès qu'un CUSUM détecte un changement de régime.
- **Budget.** Les multiplicateurs $\lambda_C$ (budget Claude, 100 USD) et $\lambda_G$ (budget Gemini, 20 USD) suivent une montée sous-gradient : $\lambda\leftarrow[\lambda+\eta(\text{dépense}-\text{rythme cible})]_+$.

**2. Fonction objectif et dispositif anti-Goodhart**

$$J=\mathbb E\!\left[\mathbf 1\{\hat\jmath_\tau=j^*\}\right]-\lambda_C C^C_\tau-\lambda_G C^G_\tau-\omega\,\#\{\text{refs non vérifiées}\}$$

- **Vérité terrain.** $j^*$ provient uniquement de vérifications externes : existence et contenu des références via arXiv, Semantic Scholar et Crossref, à coût nul.
- **Juge non optimisable.** Le juge `jev` ne fournit que des vraisemblances, jamais la récompense. Ses gabarits sont tournés aléatoirement et 10 % de canaris plantés, à réponse connue, détectent toute optimisation contre lui.

**3. Duel décisif ($H_A\perp H_B$)**

- **Corpus.** 400 affirmations, dont 30 % de fausses références ou de récitations plantées.
- **Bras, tous à budget identique (100 USD Claude et 20 USD Gemini) :**
  - (i) CSC-IDD ;
  - (ii) essaim à topologie fixe ;
  - (iii) allocation i.i.d. uniforme ;
  - (iv) **contrôle négatif** : CSC-IDD avec étiquettes `jev` permutées, qui doit égaler (iii).
- **$H_A$ (gain d'efficacité).** CSC-IDD réduit le coût par décision correcte d'au moins 30 % à $\alpha=\beta=0{,}05$.
- **$H_B$ (origine du gain, orthogonale).** Le gain disparaît si l'on force $\hat\rho_a=0$ ou une monoculture, ce qui prouve que la décorrélation est causale.
- **Analyse du duel.** Le duel est lui-même jugé par un test séquentiel du rapport de vraisemblance (SPRT) préenregistré sur les décisions appariées.
- **Réfutation.** La loi est réfutée si (iv) atteint la performance de (i), ou si (i) ne bat pas (ii).
