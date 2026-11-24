# Chantier 3 du papier D : la simulation n'éprouve pas la garantie de seuil — constat et expérience proposée (non lancée)

- **Session** : fille 2 du papier D (Opus 5.5), 24 novembre 2026, sur mandat de la mère. Classe C (note de travail). Aucune course lancée.
- **Pièce visée** : brouillon de Fable non contre-lu `papiers/D/theorie/brouillon-fable-budget-audit-v1/`, théorème de mise en œuvre aléatoire (`thm:audit-random`, l. 359 à 420 de `audit-budget-section-v1.tex`) et simulation de couverture de `check_audit_v1.py`.

## Constat, noir sur blanc

**La simulation de couverture du chantier 3 n'éprouve pas la garantie de seuil.**

Le théorème garantit deux choses, chacune avec une probabilité d'au moins $1 - \delta/2$ :
- (a) la charge estimée reste sous le seuil critique à tous les tours : $\max_{k \le K}\hat\ell_k \le \ell_{\text{crit}}$ ;
- (b) le nombre d'audits ne dépasse pas $B_{\text{rand}}$.

Sur 800 000 répétitions (quatre configurations, cinq graines, 40 000 tirages chacune ; `audit-reserves-chantier3-v1.md`), on observe **zéro** violation du seuil. Tous les échecs sont des dépassements de budget, et leur probabilité exacte est d'environ 0,27 % pour un niveau nominal de 5 %. Ce zéro ne valide pas (a) : la marge de Bernstein $\varepsilon$ tient la trajectoire loin du seuil, si bien que la simulation n'approche jamais la région où (a) pourrait échouer. Elle mesure seulement que (b) est très prudente.

Ce que ce zéro ne permet donc pas de dire :
- que la garantie (a) est serrée ;
- que la marge $\varepsilon$ est nécessaire ;
- que (a) tient hors des hypothèses du théorème, par exemple avec un plan recalculé en boucle fermée ou un gradient de politique stochastique.

La phrase du brouillon « the bound is conservative » est exacte pour (b). Elle ne doit pas être lue comme une validation de (a).

## Expérience proposée, sur processeur, sans dépense

**But.** Éprouver la garantie (a) près de sa limite, en faisant varier la marge, et mesurer de combien elle est prudente.

**Plan.**
1. **Marge réduite.** Pour un facteur $\lambda \in \{0 ; 0{,}1 ; 0{,}25 ; 0{,}5 ; 0{,}75 ; 1\}$, construire le plan glouton en boucle ouverte pour le seuil $\ell_{\text{crit}} - \lambda\varepsilon$, puis mesurer $P(\max_k \hat\ell_k > \ell_{\text{crit}})$ (violation du seuil seulement, séparée du dépassement de budget).
2. **Marge empirique minimale.** Chercher par bissection la plus petite marge $\varepsilon_{\text{emp}}$ qui donne une violation au plus $\delta/2$, et rapporter $\varepsilon_{\text{emp}}/\varepsilon$, ainsi que le budget épargné $(B(\varepsilon) - B(\varepsilon_{\text{emp}}))/B^*$. C'est le point 1 que la note de Fable recommande déjà.
3. **Distance au seuil.** Rapporter le quantile $1 - \delta/2$ de $\max_k(\hat\ell_k - \ell_{\text{crit}})$ à marge nominale : à quelle distance du seuil reste-t-on ?
4. **Hors des hypothèses (descriptif, sans revendication).** (i) Plan recalculé à chaque tour à partir des audits réalisés, en boucle fermée. (ii) Grandes valeurs de $K$ devant $n$, où $\varepsilon$ est grand.
5. **Grille.** $K \in \{50, 200, 500\}$, $n \in \{100, 1000\}$, $\gamma \in \{0{,}05 ; 0{,}2\}$, $\eta \in \{1 ; 10 ; \infty\}$, $\Delta R = 1$, $C \in \{4, 19\}$, $\delta \in \{0{,}05 ; 0{,}1\}$, avec $c$ pris **hors de la frontière** $\eta\Delta R = c$ (par exemple $c = 0{,}5\,\eta\Delta R$, et $c = 1$ pour $\eta = \infty$).
6. **Répétitions.** $10^5$ par point. Pour estimer une probabilité de l'ordre de $\delta/2$ à 10 % près en relatif, il faut environ $4/(0{,}01 \cdot \delta/2)$ tirages, soit 16 000 à $\delta = 0{,}05$ : $10^5$ laisse une marge large. Intervalles de Clopper-Pearson à 95 %.
7. **Graines** : `numpy.random.SeedSequence`, une sous-graine par point de grille (R9). Manifeste du run. Script neuf et versionné, qui ne touche pas au brouillon.

**Prédictions, à figer avant la course** (le script fait foi ; ce ne sont pas des résultats) :
- à $\lambda = 1$, violation $\le \delta/2$ en tout point (sinon le théorème, ou sa mise en œuvre, est faux) ;
- à $\lambda = 0$, violation nettement positive, de l'ordre d'une fraction notable ; sinon la marge n'est pas nécessaire et le budget est surdimensionné ;
- $\varepsilon_{\text{emp}}/\varepsilon$ nettement sous 1, attendu entre 0,2 et 0,6 vu la prudence mesurée sur (b) ; ce chiffre est une estimation, pas un fait.

**Garde de symétrie (R4).** Une violation nulle même à $\lambda = 0$ serait « trop propre » et déclencherait le même audit qu'ici : vérifier que le plan sans marge atteint vraiment le seuil en espérance, et que l'événement est bien compté.

**Coût et durée.** Environ $3 \times 2 \times 2 \times 3 \times 2 \times 2 = 144$ points de grille, multipliés par six valeurs de $\lambda$, à $10^5$ tirages chacun, vectorisés avec numpy. Ordre de grandeur : quelques dizaines de minutes sur un processeur ordinaire. Aucune dépense.

**Statut.** Proposée, **non lancée**. Selon la règle du programme, le préenregistrement et ses critères relèvent de Fable, avec contre-lecture par Opus, si la mère juge l'expérience décisive pour le papier ; sinon elle reste un contrôle d'instrument, de classe B.
