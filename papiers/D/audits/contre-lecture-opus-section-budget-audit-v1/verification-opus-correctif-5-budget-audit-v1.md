# Vérification des corrections de la section sur le budget d'audit (papier D) : correctif 5 — v1

- Vérificateur : Opus 5.5, effort élevé, auteur de la contre-lecture du correctif 4. Je n'ai modifié aucun fichier du dépôt.
- Pièces vérifiées (commit `ab73dbb8`), toutes conformes à leur compagnon `.sha256` :
  - `audit-budget-section-v1-correctif-5.tex` (`8632aa52…e316`) ;
  - `table-corrections-contre-lecture-opus-budget-audit-v1.md` ;
  - `bib-a-ajouter-budget-audit-v1.tex` (`18f44b62…1020`) ;
  - le dossier `essai-insertion-c5/` (les copies de la section et des entrées y sont identiques aux originaux).
- Le manuscrit de l'essai est identique à `main-v4-correctif-4.tex` du dossier du manuscrit.
- Mes scripts sont dans `/tmp/claude-0/-home-user-controle-ia-travail/c88f1f22-9d69-5421-86a6-86f206ad7a55/scratchpad/verif-budget-audit/` :
  - `checks_c5.py` et `npg_exact.py`, pour les calculs ;
  - `diff_c4_c5_reverse.txt`, différence mot à mot entre les correctifs 4 et 5, renommages inversés ;
  - `compil-c5/`, ma compilation.

## Verdict

**Corrections acceptées. Aucun défaut bloquant ne reste.**

- **Traitement des défauts** : neuf défauts sont traités (D1 à D6, D9, D10 et D12) ; trois le sont en partie (D7, D8, D11), pour des raisons qui sortent de la pièce. Les deux rejets sont acceptables.
- **Ajouts non contre-lus** : ils sont tous justes. J'ai vérifié par calcul la dynamique, le lemme, le point fixe, la limite statique et les deux contre-exemples.
- **Défauts nouveaux** : trois, tous mineurs (N1 à N3).
- **Compilation** : je confirme le résultat de Fable. Trois passes, aucune erreur, aucune référence ni citation indéfinie, 22 pages.
- **À remonter à Lazar** : le resserrement du plancher ne restreint aucune revendication du manuscrit de base. Mais l'insertion touche deux revendications du manuscrit : son cadre déclaré « statique », et la nouveauté du régime des pièges indistinguables (R3), sur laquelle la section cite maintenant deux voisins proches. Voir le point 4.

## 1. Compilation, refaite par moi

- **Méthode** : copie de `essai-insertion-c5.tex` et de ses deux fichiers `\input` dans mon bloc-notes, puis trois passes de `pdflatex`.
- **Résultat** : code de retour 0 aux trois passes ; aucune ligne d'erreur ; aucune référence ni citation indéfinie ; aucun label en double ; 22 pages, 488 452 octets, comme l'essai versé.
  - **Boîtes trop larges** : les deux du journal (9,9 pt et 3,8 pt) sont dans le manuscrit de base, pas dans la section.
  - **Boîtes trop lâches** : trois, toutes dans la bibliographie (Bailey et al., Halberstadt, Deng et al.). C'est cosmétique.
- **Contenu de l'essai** : il ne diffère du manuscrit `main-v4-correctif-4.tex` que par trois lignes de préambule, plus `\theoremstyle{plain}`, et par deux `\input`.
- **Pages de la section** (11 à 19) : je les ai lues en texte. Aucun « ?? », aucun « chantier », aucun chemin du dépôt.

## 2. Statut par défaut

| Défaut | Statut | Justification |
|---|---|---|
| D1 | **traité** | La récurrence est définie dans la section (`eq:audit-dyn`), et je l'ai vérifiée (§ 3). L'abandon de la strate visible est démontré dans la preuve du lemme. `L` est défini comme la barrière de R1, et sa définition coïncide avec celle du manuscrit. Le chapeau renvoie à `thm:escape`, R3. Aucun renvoi ne sort du manuscrit : la compilation n'en laisse aucun indéfini. |
| D2 | **traité**, hors de la section | Les trois lignes de préambule sont dans la table, § 3, et en tête de la section. Elles sont éprouvées par la compilation. |
| D3 | **traité** | Ma différence mot à mot, renommages inversés, ne montre aucun reste de l'ancienne notation. $C$ désigne bien la pénalité de l'opérateur B. Mineur : $C_{\max}$ est laissé tel quel ; c'est sans conflit. |
| D4 | **traité** | « 144 configurations », dont 6 avec $\varepsilon>c$ et la garantie vide. Recalculé par `verif_c5.py`, rejoué par moi : 144 points, 6 points, tous à n = 100, γ = 0,2, η = 1, $C_{\mathrm{aud}}$ = 19. |
| D5 | **traité** | Le texte dit « sits on the threshold (Theorem…(i)) … some positive margin is needed; the order of ε is not claimed ». `rem:audit-random` est mise en accord. |
| D6 | **traité** ; ajout facultatif rejeté | Le texte dit maintenant : marge oracle ; niveau δ/2 du processus sans plafond ; « at most » ; économie mesurée sur $B_\varepsilon$ et non sur $B_{\mathrm{rand}}$ ; « nothing here shows that it could be used in practice ». Le rejet de l'ajout facultatif est conforme à R6, puisque ce calcul n'est pas scellé. Voir N2 pour une formulation restée inexacte. |
| D7 | **partiellement traité** | Les clés sont alignées sur le manuscrit ; vingt `\bibitem` sont fournis ; la compilation ne laisse aucune citation indéfinie. Reste, hors de la pièce : inscrire Gans et Holden, et Zhu, Zuo et Sun, au registre des références. |
| D8 | **partiellement traité** | Zhang et Parkes 2008 est retirée du texte. L'antériorité de l'audit d'élection est ajoutée, sans formule. « low-stakes alignment » et « recent preprints » sont corrigés. Le numéro de théorème de Boucheron et la constante de Freedman sont retirés : je l'ai vérifié, le texte dit « another constant in the linear term ». Reste : `aslam2007` est cité alors qu'il est encore NON_CONFIRMEE au registre, avec des initiales écrites de mémoire ; aucune affirmation n'a été lue sur PDF. |
| D9 | **traité** | Aucune note de travail ne s'imprime plus. Il reste une phrase de limite, acceptable : « We have not searched systematically… ». |
| D10 | **traité** | L'en-tête est sans chemin, sans état périmé, sans identifiant interne. Le bloc bibliographique en commentaire est retiré. |
| D11 | **partiellement traité** | Le commentaire porte maintenant les empreintes complètes ; je les ai vérifiées, elles sont exactes. Reste : verser le verdict sur la branche du papier, et nommer le script parmi les scripts compagnons. Le commentaire porte encore des noms internes de fichiers (« chantier3 ») ; il faut les retirer avant le dépôt des sources. |
| D12 | **traité** (points 1, 2, 3, 5) ; point 4 sans objet ; point 6 rejeté | Point 1 : les deux contre-exemples sont vérifiés au § 3. Points 2, 3 et 5 : conformes. Point 4 : il ne demandait rien. Le rejet du point 6 est acceptable : c'était un ajout facultatif, et le chiffre reste au verdict scellé. |

## 3. Ajouts vérifiés par calcul

1. **Dynamique** `eq:audit-dyn`, gradient naturel et point fixe (`checks_c5.py`, `npg_exact.py`).
   - **Gradient naturel.** J'ai simulé une montée de gradient naturel en softmax tabulaire avec ancre de Kullback-Leibler, en prenant pour $F^\dagger F$ le projecteur exact orthogonal aux constantes. Elle coïncide avec l'inclinaison $\pi_k\propto e^{\phi_k}\pi_0$ à $1{,}4\times10^{-15}$ près, sur 300 tirages aléatoires.
   - **Projecteur.** Dans les cas bien conditionnés, `pinv(F)F` vaut ce projecteur à $10^{-14}$ près. L'écart de $10^{-3}$ que donne `pinv` quand $\pi$ est minuscule est numérique.
   - **Forme équivalente.** $d\pi_{k+1}/d\pi_0\propto(d\pi_k/d\pi_0)^a e^{\gamma r_k}$ : exact.
   - **Maximiseur.** Celui de $\gamma\E_\pi[r_k]-(1-a)\DKL(\pi\|\pi_0)-a\DKL(\pi\|\pi_k)$ est bien $\pi_{k+1}$. Je l'ai retrouvé par optimisation numérique, à $10^{-5}$ près. Voir N1 pour l'expression « step of size γ ».
   - **Point fixe.** $\phi_k=\eta(1-a^k)r$ (exact) et convergence vers $e^{\eta r}\pi_0$, atteinte en un pas si $\gamma=\eta$. Pour $r=\bar R_C$, c'est l'opérateur B ; si $\beta\equiv1$, c'est la référence sans moniteur. Exact.
2. **Lemme `lem:audit-logodds`, rendu autonome.** La preuve est juste : $\phi_k$ est constant sur chaque strate, $Z_k$ se simplifie, et la strate visible n'entre pas. Numériquement, avec une récompense **non constante** sur la strate visible, l'écart à `eq:audit-logodds` est au plus $4{,}4\times10^{-15}$.
3. **Limite statique et lien avec R1 et R3.** À taux d'audit constant, $x_k\to\eta(\Delta R_{\mathrm f}-W\rho)$ : c'est le rapport des logits de l'opérateur B de R1 avec $\beta_{\mathrm h}=1$, $\beta_{\mathrm f}=1-\rho$ et $C=C_{\mathrm{aud}}$ (vérifié : −4,5 dans les deux calculs). Le seuil $(1-\rho)\Delta R_{\mathrm f}/\rho$ est bien $C^*_{\mathrm{R3}}$ à $\varepsilon_{\mathrm{trap}}=\delta_{\mathrm{ind}}=0$ (vérifié sur la formule du manuscrit). La barrière $L$ coïncide avec $\Delta\DKL(\Pi_{\mathrm f}\|\Pi_{\mathrm h};\pi_0):=\log(p_{\mathrm h}/p_{\mathrm f})$ du manuscrit.
4. **Les deux contre-exemples sur la direction de $\gamma$ au critère final.**
   - **Majorant de $\gamma$.** Avec $\hat\gamma=\eta>\gamma$, le plan prévu audite le seul dernier tour, au taux $(\eta\Delta R_{\mathrm f}-c)/(\eta W)$. Il laisse $x_K-c=a(\Delta R_{\mathrm f}G_{K-1}-c)$. Je l'ai démontré à la main, puis vérifié sans écart sur 16 899 cas aléatoires. Cette quantité est positive dès que la niche apparaît au tour $K-1$ et que $a>0$, ce que garantit $\gamma<\eta$.
   - **Minorant de $\gamma$, à $\eta=\infty$.** Seule la somme des taux compte, et elle vaut $(K\Delta R_{\mathrm f}-c/\hat\gamma)/W$. Donc $x_K=\gamma c/\hat\gamma>c$ dès que $c>0$. Si le plan prévu ne prévoit aucun audit alors qu'il en faut, l'infaisabilité est immédiate. Vérifié sur 19 524 cas, sans échec.
   - **Portée.** Il suffit d'un contre-exemple par direction pour dire « no safe direction » : la phrase est juste. `verif_c5.py`, rejoué, donne les mêmes valeurs (2,099152 contre 0,98 × 2,141991).
5. **Autres phrases neuves.** Elles sont justes :
   - à $\eta=\infty$, l'écart $\hat\ell_k-\ell_k$ est une martingale en $k$ ;
   - la strate la pire sous $\delta_{\mathrm{ind}}$ a $\tau_{\mathrm{aud}}=0$ ;
   - le lien $\varepsilon_{\mathrm{aud}}\leftrightarrow\varepsilon_{\mathrm{trap}}$ et $\tau,\tau_{\mathrm{aud}}\leftrightarrow\tau_{\mathrm{ord}},\tau_{\mathrm{trap}}$ est fidèle à R3.
6. **Intégrité.** Les renommages inversés, le correctif 5 ne diffère du correctif 4 qu'aux passages que la table déclare. Aucun énoncé, aucune preuve et aucun exemple chiffré n'a changé de contenu.
7. **Entrées bibliographiques.**
   - Les auteurs de « Blindfold » (Wei Zhu, Meiyun Zuo, Huiping Sun) et de Gans et Holden (Joshua S. Gans, Richard Holden) sont conformes à la première page des PDF du dépôt. J'ai relu ces pages ; les empreintes `5250fa11…` et `e28a4e8d…` sont conformes à la note de lecture.
   - Les autres entrées concordent avec le registre v2 et avec ma connaissance.
   - Seule `aslam2007` reste à confirmer (D8).

## 4. Le resserrement du plancher, et la portée des revendications du manuscrit de base (à remonter à Lazar)

- **Le resserrement lui-même ne restreint aucune revendication du manuscrit de base.**
  - Le manuscrit ne revendique pas le plancher pour les attaques rares. Il le présente comme une **limite** du régime R3 :
    - R3 « excludes frequent cheaters only » ;
    - la remarque qui suit R3 : « does not block a policy that cheats at a very rare rate $\tau_{\mathrm{ord}}\le\delta_{\mathrm{ind}}$ » ;
    - la section des limites : « Regime R3 leaves an irreducible floor for rare attacks ».
  - Le passage de « a quantification of the rare-attack floor » à « the expression in this dynamics … ; we do not claim the floor itself » ne resserre donc que la revendication **de la section**. Cela reste une décision de revendication.
- **Mais l'insertion touche deux revendications du manuscrit**, que Fable signale en partie (table, § 3) :
  1. **Le cadre déclaré.** Le résumé et l'introduction disent étudier « a restricted, static version » ; les limites classent « finite-time stochastic gradient dynamics » et « dynamic … allocation and rare-attack floor » parmi les problèmes ouverts. La section dit « The analysis is no longer static ». L'insertion **élargit** donc ce que le papier revendique, et le résumé, la liste des contributions et les limites devront changer. C'est une modification de revendication, donc un nœud de Lazar.
  2. **La nouveauté de R3.** La section cite deux prépublications récentes, Gans et Holden (septembre 2026) et « Blindfold » (octobre 2026) :
     - la première comme « the static form … of the floor below $\delta_{\mathrm{ind}}$ » ;
     - la seconde comme « the closest analogue … of the condition $\delta_{\mathrm{ind}}>0$ ».

     Or le manuscrit présente R3 comme une contribution : liste des contributions, item 3, et « Theorem~\ref{thm:escape}(3) turns the exact same total variation inequality in favor of the defender ». Il ne cite aucun de ces deux textes. Une fois la section insérée, le papier se contredirait sur ce point. Il faut confronter la revendication de R3 à ces deux voisins, ce qui relève aussi de Lazar.

## 5. Défauts nouveaux

| N° | Gravité | Emplacement | Constat | Correction |
|---|---|---|---|---|
| N1 | mineur | Paragraphe « Dynamics », phrase « this is one step of size γ, proximal relative to the current policy, on the KL-regularized objective » | Le maximiseur affiché est juste. Mais, ramené à l'objectif $\E_\pi[r_k]-\eta^{-1}\DKL(\pi\|\pi_0)$, le terme proximal a pour coefficient $a/\gamma$ : c'est un pas proximal **exact** de taille $\gamma/a=\gamma\eta/(\eta-\gamma)$. Je l'ai vérifié : la même loi est obtenue avec cette taille. C'est un pas de taille $\gamma$ seulement au sens de la montée miroir, sur l'objectif linéarisé en $\pi_k$. | « one mirror-ascent step of size γ on this objective (equivalently, an exact proximal step of size γ/a) ». |
| N2 | mineur | `rem:audit-random-sim`, « in the 137 configurations where the crossing is seen without margin » | Au point n° 31, le franchissement sans marge est bien vu (91 744 sur 100 000). C'est sa lecture qui est non concluante, par sensibilité à la tolérance. La phrase contredit aussi celle qui précède dans la même remarque. | « in the 137 configurations where the reading without margin is conclusive ». |
| N3 | mineur | Table, § 3, préambule | L'essai ajoute `\theoremstyle{plain}` après la définition ; la table l'omet. C'est sans effet aujourd'hui, mais tout `\newtheorem` ajouté plus tard prendrait le style « definition ». | Ajouter `\theoremstyle{plain}` aux trois lignes de la table. |

Hors défaut :
- **Policy teaching.** Le voisin « policy teaching » a disparu avec Zhang et Parkes 2008. L'article de Zhang, Parkes et Chen (2009), que la recherche du registre a trouvé, pourrait le remplacer après vérification. C'est facultatif.
- **Commentaires.** Ceux de la remarque `prop:audit-indist` ne sont pas touchés ; la table les note en dehors du mandat.
