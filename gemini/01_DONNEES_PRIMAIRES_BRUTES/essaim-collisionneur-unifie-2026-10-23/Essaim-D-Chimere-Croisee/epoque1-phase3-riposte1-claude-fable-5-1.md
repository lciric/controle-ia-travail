`BASSIN_MATH: Koopman-DMD à noyau indexé par couche sur $S_{\text{TD}}$, avec spectre différentiel E1 et vérificateur de coût d'évasion`

**1. Sur l'attaque reçue — constat avant riposte**
L'objet retourné par `claude-opus-5-5` est vide : `texte=''`, `fin='max_tokens'`, seul un bloc `thinking` existe. Il n'y a **aucune critique à accepter ni à réfuter**. Je refuse d'en inventer et de les lui attribuer. En Phase 3, une riposte sans attaque reçue exige une auto-attaque explicite ; les trois critiques suivantes sont **auto-générées**, non imputables à l'équipe rouge.

*Auto-critique A (acceptée, algébrique)* : un opérateur unique $\hat K$ sommé sur $\ell=2..21$ suppose une dynamique **autonome** ; or chaque couche $f_\ell$ a ses propres poids, donc $\phi(z_{\ell+1}) \approx K_\ell\,\phi(z_\ell)$ avec $K_\ell \neq K_{\ell'}$. Le spectre de $\hat K$ moyen est un artefact. Correction : opérateurs indexés par couche, ou dynamique prise sur l'axe **token** $t$ à couche fixe (système homogène dans le temps à paramètres gelés).

*Auto-critique B (acceptée)* : ma proposition n'intègre pas E1 ; rien n'empêche le spectre de coder la *lecture* d'une instruction, retombant dans le piège de P3.

*Auto-critique C (acceptée)* : le socle 4 n'est vérifié que sur ses modèles d'origine ; E0 est un prérequis bloquant sur Llama-3.1-8B.

**2. Opérateur corrigé**
Pour chaque couche $\ell \in [5,22]$ (Dopamine Neurons), dynamique sur les tokens du canal $m_{1\to 2}$ :
$$\hat K_\ell = \arg\min_K \sum_t \|\phi(z_{\ell,t+1}) - K\,\phi(z_{\ell,t})\|^2 + \lambda\|K\|_F^2,\quad \phi:\mathbb{R}^{d_S}\to\mathbb{R}^{D}$$
avec $D=512$ (illustratif), $\lambda$ choisi par validation croisée sur données honnêtes uniquement. Statistique de régime : $\sigma_\ell = \{\log|\mu_i(\hat K_\ell)|\}_{i\le k}$, $k=16$ (illustratif), puis **spectre différentiel** $\Delta\sigma = \sigma^{\text{avec prompt sys}} - \sigma^{\text{re-forward sans prompt sys}}$, exactement le contraste E1.

**3. Duel $H_A \perp H_B$**
- $H_A$ (mécanisme) : $\Delta\sigma$ sépare $(i\text{-}a)$ des honnêtes **et** ne sépare pas E1 (honnête + instruction secondaire bénigne secrète de même longueur + saboteur inactif).
- $H_B$ (confondant) : $\Delta\sigma$ sépare aussi E1 des honnêtes ⇒ le spectre code la lecture d'instruction, pas l'acte. **Contrôle négatif