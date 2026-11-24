# Contre-lecture du brouillon de Fable sur le budget d'audit borné pendant l'entraînement après pré-entraînement (papier D, chantier 3)

- Contre-lecteur neuf (Opus 5.5), 24 novembre 2026, branche `papier-d/evasion-post-entrainement-v1`. Rien n'est modifié dans le dépôt. Les scripts ont tourné sur des copies, dans le bloc-notes, avec `-I`.
- Pièces lues : `papiers/D/theorie/brouillon-fable-budget-audit-v1/` (section `.tex`, note à l'orchestrateur, script `check_audit_v1.py`), avec des empreintes conformes à leurs `.sha256` ; l'audit `papiers/D/audits/audit-reserves-chantier3-v1/` (pas refait) ; le modèle statique `main-v4-correctif-1.tex` ; la récurrence de la section sur la dynamique (`dynamics-section-v1-correctif-1.tex`, règle (a)).
- Mes scripts : `verif-bud/` dans le bloc-notes (`v1_dissuasion.py`, `v1b_ecart_final.py`, `v2_detection.py`, `v3_aleatoire.py`, `v4_indiscernabilite.py`, sorties `sortie-v*.txt`, compilation dans `verif-bud/latex/`).

## Verdict

**Le brouillon tient, avec des réserves.** J'ai refait sans le texte les preuves de tous les énoncés numérotés : elles sont justes, et je n'y ai trouvé ni erreur de signe ni erreur de constante. Il n'y a aucun défaut bloquant. On compte quatre défauts majeurs : deux énoncés vont plus loin que ce qui est prouvé, une remarque réintroduit l'affirmation que la note elle-même réfute, et l'antériorité n'est pas couverte (règle d'anti-faux-gap, R8). S'y ajoutent treize défauts mineurs, dont une inégalité fausse dans un cas de bord. Le contre-exemple de la note sur la borne inférieure $(T-k+1)/k\cdot\log(1/\delta)$ est confirmé.

## Défauts

### Majeurs

**M1. La remarque sur la détection et la dissuasion réintroduit l'ordre de grandeur réfuté.** Endroit : `audit-budget-section-v1.tex`, lignes 329 et 330 (« catching … takes $B\approx(T/k)\log(1/\delta)$ audits »). Cette approximation n'est juste que si $k\gg\log(1/\delta)$. Pour $k$ petit, elle dépasse même $T$. Exemples avec $T=257$ : pour $k=1$ et $\delta=0{,}05$, le vrai budget minimal $B^\star_{\det}$ vaut 245, contre 769,9 pour l'approximation ; pour $k=3$ et $\delta=0{,}001$, il vaut 231, contre 591,8 (`sortie-v2.txt`). C'est exactement l'erreur que la note corrige à son point 1. **Correction :** écrire $B^\star_{\det}\in[(T-k+1)(1-\delta^{1/k}),\ \lceil T(1-\delta^{1/k})\rceil]$, puis préciser « $\approx (T/k)\log(1/\delta)$ seulement quand $k\gg\log(1/\delta)$ ; près de $T$ quand $k\lesssim\log(1/\delta)$ ».

**M2. La proposition sur l'indiscernabilité dit trop : « the resulting schedules deter every stratum satisfying the trap bound ».** Endroit : lignes 455 et 456. Le plan est calculé pour une fréquence de triche $\tau$ (et une marge $c$, donc une cote a priori $L$) donnée. Il dissuade toute strate de même $\tau$ qui respecte la borne des pièges (le pire cas porte sur $\tau_A$), mais pas les strates d'une autre fréquence. Contre-exemples exacts (`sortie-v4.txt`), tous avec $\Delta R=1$, $C=9$ et $\delta_{\mathrm{ind}}=0{,}1$ :
- $\eta=\infty$, $c=1$ : le plan calculé pour $\tau_0=1$ laisse monter la log-cote de la strate $\tau=0{,}1$ à $x=1{,}79>c$, et celle de la strate $\tau=0{,}3$ à $x=1{,}62>c$ ;
- $\eta=5$, $c=2$ : le plan calculé pour $\tau_0=0{,}5$ laisse monter celle de la strate $\tau=1$ à $x=4{,}0>c$.

Le taux de maintien $\rho^\delta_{\mathrm{hold}}(\tau)$ n'est pas monotone en $\tau$. À $\eta=\infty$, son maximum est atteint pour $\tau\le\delta_{\mathrm{ind}}$, où il vaut 1. **Correction :** écrire « deter every stratum with the same $(\tau,L)$ satisfying the trap bound ». Énoncer ensuite la quantité de planification, $\sup_{\tau\in[\tau_{\min},1]}$, appliquée au plan juste à temps et pas seulement au taux de maintien. Dire où se trouve ce supremum : la strate la plus dure à dissuader triche au taux $\delta_{\mathrm{ind}}$, pas au taux 1. La note le pressent à son point 3.5 ; c'est l'énoncé qui doit le dire.

**M3. La remarque sur la détection et la dissuasion affirme que le taux de dissuasion « does not depend on how often the current policy cheats ».** Endroit : lignes 333 et 334. Ce n'est vrai que dans le champ moyen, où le gradient naturel est calculé sur l'espérance exacte des actions. Avec des actions échantillonnées, le signal de pénalité ne passe que par les épisodes furtifs qui sont audités, environ $n\rho\,\pi_k(f)$ par pas. Quand la triche est rare, c'est beaucoup moins d'un épisode, et la variance du signal explose. C'est précisément le régime où la remarque juge la détection « hopeless ». Le texte reconnaît l'hypothèse (« Sampling noise from the policy's actions is not modelled », ligne 351), mais la remarque en tire un contraste qu'elle ne permet pas. **Correction :** ajouter « in the mean-field model », et signaler que la comparaison avec la détection dans le régime rare est l'objet du point 2 de la section 3 de la note, une expérience ouverte.

**M4. L'antériorité est incomplète, et la nouveauté revendiquée n'est pas vérifiée (R7 et R8).** Endroit : remarque `rem:audit-related`, lignes 488 à 520, et note, section 5.
- Le contrôle de l'intelligence artificielle y est résumé en un seul régime, « a single caught attempt ends the game » (lignes 509 à 511). Ce résumé oublie le voisin le plus proche du programme : le contrôle à faibles enjeux et les menaces diffuses, à vérifier (Wen et al. 2024, *Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats*, arXiv:2411.17693 ; Christiano 2021, « Low-stakes alignment »).
- La « coupling of the audit schedule with … KL-regularised natural policy gradient » doit être confrontée à quatre voisinages. D'abord l'enseignement de politique et l'empoisonnement de récompense sous budget, qui modifient la récompense d'un apprenant sous contrainte de budget, soit le problème miroir de celui-ci. Ensuite le pilotage d'apprenants sans regret par un meneur qui s'engage. Puis les jeux d'inspection où l'inspecté suit une dynamique d'apprentissage ou d'évolution, ce qui contredit en partie la ligne 495. Enfin la récompense rare auditée et repondérée par l'inverse de la probabilité d'audit, qui donne exactement l'échange pénalité contre budget du corollaire (c).
- La dernière contribution revendiquée, « penalties cannot deter cheating rates below $\delta_{\mathrm{ind}}$ » (lignes 517 et 518), figure déjà qualitativement dans le modèle statique (remarque « Rare-Attack Floor of Regime R3 » de `main-v4-correctif-1.tex`). Seul est nouveau le taux $1-c/(\eta\tau\Delta R)$, indépendant de $C$.

**Correction :** mettre « to our knowledge » sous réserve jusqu'à la lecture sur PDF de la liste ci-dessous. Retirer de la liste des apports la phrase sur $\delta_{\mathrm{ind}}$, ou la reformuler comme quantification du plancher déjà noté en R3. Citer les travaux voisins.

### Mineurs

- **m1. Inégalité sur $\rho^\delta_{\mathrm{hold}}$, lignes 459 à 461.** Elle est fausse quand le numérateur est négatif, c'est-à-dire quand $\eta\tau\Delta R<c$. Exemple : $\Delta R=\eta=C=1$, $\tau=0{,}5$, $c=1$, $\delta_{\mathrm{ind}}=0{,}25$ donne $-0{,}667\not\le-1{,}000$ (`sortie-v4.txt`). Ajouter l'hypothèse « when $\eta\tau\Delta R>c$ ».
- **m2. Hypothèses cachées du cadre, lignes 43 à 53.** Trois hypothèses ne sont pas écrites :
  - aucun moniteur dans la boucle, ou un moniteur aveugle sur $f$ ($\beta_f=\beta_h=1$, niche parfaitement furtive) ;
  - un épisode honnête audité n'est jamais pénalisé (pas de faux positif, $\beta_h=1$) ;
  - l'audit est infaillible ($\varepsilon_{\mathrm{trap}}=0$ dans R3).

  Il faut les dire, et noter que le cas général s'obtient par substitution. Avec une capture de probabilité $1-\varepsilon_a$, $W$ devient $(1-\varepsilon_a)W$. Avec un moniteur de boucle sous l'opérateur B, $\Delta R$ devient l'avantage effectif.
- **m3. Constantes de Bernstein, lignes 396 à 399.** Le choix $t=\sqrt{2v\Lambda}+2b\Lambda/3$ est valide : l'exposant vaut au moins $\Lambda$, vérifié sur $10^5$ tirages. Il est prudent d'un facteur 2 sur le terme linéaire par rapport à la forme sous-gamma (Boucheron, Lugosi et Massart, théorème 2.10 à vérifier : $\sqrt{2v\Lambda}+b\Lambda/3$). Il faut citer le numéro du théorème. La même remarque vaut pour (b).
- **m4. Phrase sur l'inégalité de Freedman, lignes 431 à 434.** « replaced by $2bt$ » est valide mais trop prudent : Freedman donne aussi la forme en $bt/3$ par la borne de type Bennett. Surtout, en boucle fermée la log-cote de référence $\ell_k$ devient aléatoire, et « the same statement » n'a plus de sens précis. Le dire ou retirer la phrase.
- **m5. Remarque sur les deux critères, lignes 235 et 236.** « $B^\star_{\mathrm{fin}}=O(1)$ as $T\to\infty$ » n'est vrai qu'à $n$ fixé. Le bon énoncé est $O(n\,\tfrac{\eta}{\gamma}\log\tfrac{\eta W}{\eta C+c})$ quand $K\to\infty$.
- **m6. Notation $\ell^u_k$, lignes 105 et 154.** Elle est employée sans être définie. Poser $\ell^u_k:=-L+x^u_k$.
- **m7. Fin de la ligne 330 jusqu'à la ligne 332.** « a policy that cheats on $k\le\ldots$ episodes escapes any auditor » ne vaut que si la politique tire son ensemble de triche uniformément au hasard, indépendamment de l'auditeur, comme en (b). Le dire.
- **m8. Proposition sur l'indiscernabilité.**
  - Si les audits sont des inspections au hasard d'épisodes ordinaires, $\delta_{\mathrm{ind}}=0$ par construction. Un $\delta_{\mathrm{ind}}>0$ suppose des audits plantés ou reconnaissables, comme les pièges de R3. Dans ce cas $\rho$ est la fraction de pièges et le budget compte des pièges construits. Le dire.
  - En (a), le dénominateur s'annule pour $\rho=1$ et $\tau_A=0$.
- **m9. Preuve de (b) de la proposition, lignes 476 et 477.** Elle ne donne que la monotonie en champ moyen. Pour transporter le théorème de mise en œuvre aléatoire, il faut la domination trajectoire par trajectoire : à tirages d'audit égaux, un $\tau_A$ plus grand donne une log-cote réalisée plus basse à chaque pas. Elle est vraie (vérifiée, `sortie-v3.txt`, point 5) ; il manque une phrase.
- **m10. Remarque sur les deux critères, point (3), lignes 238 à 240.** La direction sûre vaut aussi pour une borne inférieure sur $C$. Elle ne vaut pas pour $\eta$ ni pour $\gamma$, qui ne sont pas monotones. Le préciser.
- **m11. Références, lignes 552 à 557.** Les clés diffèrent de celles du manuscrit statique (`greenblatt2023`, `griffin2024`, contre `greenblatt2023control`, `griffin2024games`). Le titre de Griffin et al. diffère aussi : « … of AI Deployment Protocols » dans le statique, « … of AI Control Protocols » ici. L'un des deux est faux ; à trancher sur le PDF.
- **m12. Script `check_audit_v1.py` (classe B).**
  - Il n'éprouve ni la valeur minimax de détection (a), ni le test de taux (c), ni le corollaire (c), ni l'unicité, ni la remarque sur les deux critères point (3), ni la proposition sur l'indiscernabilité.
  - Le repli des lignes 55 et 56 masque un programme linéaire jugé infaisable par le solveur dans le cas $C=c=0$, où la solution exacte est à la frontière.
  - Le commentaire de la ligne 95 est resté orphelin.
  - Le script n'a pas de manifeste (R9).

  Mes scripts couvrent ces trous.
- **m13. Lecture de la simulation.** La phrase de la note « The bound is conservative » ne vaut que pour le dépassement de budget. L'audit déjà fait le montre (`audit-reserves-chantier3-v1.md`) et je ne le refais pas. À reporter dans le texte si la simulation y est citée.

## Ce qui a été vérifié et tient

**Lemme de log-cote.** La récurrence $x_{k+1}=ax_k+\gamma d_k$ et son déroulé sont justes. Elle coïncide avec la règle (a) de la section sur la dynamique, une fois retiré le terme modulo $\mathbf 1$, qui se simplifie dans la différence. Retirer la strate visible $v$ est exact, parce que la log-cote entre $f$ et $h$ n'en dépend pas.

**Théorème de dissuasion (i).**
- L'identité de sommation (`eq:audit-identity`) est juste, et la borne inférieure par l'enveloppe $\min(c,\Delta R\,G_k)$ aussi. Ce sont des multiplicateurs de dualité explicites.
- La faisabilité du plan juste à temps est vérifiée, tout comme $0<\rho_\kappa\le\rho_{\mathrm{hold}}\le\Delta R/W$, l'unicité pour $\eta<\infty$ et le cas où $\Delta R\,G_K\le c$ donne un budget nul.
- Sur 4 000 instances ($K\le60$, avec les cas $\gamma=\eta$, $\eta=\infty$, $C=0$ et $c=0$), contre un programme linéaire indépendant (HiGHS) : écart maximal $4{,}3\cdot10^{-9}$. L'écart entre la solution du programme linéaire et le plan juste à temps vaut $2{,}8\cdot10^{-10}$, ce qui confirme l'unicité.

**Théorème de dissuasion (ii).**
- La preuve par multiplicateur $\lambda=a^{-m}$ est juste, ainsi que le plan chargé en fin d'horizon.
- La formule $m=\lfloor\log(1-D/(\eta W))/\log a\rfloor$ est juste et reste toujours au plus égale à $K$, puisque $D\le\eta W(1-a^K)$.
- La borne indépendante de l'horizon est juste, par $\log(1/a)\ge\gamma/\eta$ et $\eta W-D\ge\eta C+c$.
- L'écart à un programme linéaire vaut $8{,}5\cdot10^{-14}$, aucune violation n'apparaît, et le cas dégénéré $C=c=0$ se traite à part.

**Corollaire du compromis.** Les points (a), (b) et (c) sont justes. Le point (c) est éprouvé par bissection sur le seuil exact de pénalité, sur 326 cas, sans violation.

**Cohérence avec le modèle statique.**
- À taux constant $\rho$, la log-cote limite vaut $-L+\eta[(1-\rho)\Delta R-\rho C]$. C'est la log-cote statique de l'opérateur B avec $\beta_f=1-\rho$ et $\beta_h=1$ (égalité à $10^{-15}$). Le taux de maintien est donc le seuil de dominance statique.
- À $\eta=\infty$ et $c=0$, $\rho>\rho^\delta_{\mathrm{hold}}$ équivaut à $C>C^\star_{\mathrm{R3}}$ avec $\varepsilon_{\mathrm{trap}}=0$. La borne des pièges $\tau_A\ge(\tau-\delta_{\mathrm{ind}})_+$ est celle de R3, déduite de la variation totale.

**Théorème de détection.**
- Le point (a) est juste : la réduction à l'ensemble $Q(u)$ et la symétrie hypergéométrique tiennent. La valeur du jeu, calculée par programme linéaire sur toutes les stratégies mixtes pour six triplets $(T,k,B)$, égale $1-q$ à $10^{-10}$ près.
- Le point (b) est juste : la chaîne de bornes sur $B^\star_{\det}$ ne présente aucune violation sur 41 671 cas exacts en rationnels ($T\le257$, sept valeurs de $\delta$).
- Le point (c) est juste : $\alpha+\beta\ge\mu$, la valeur minimax $\mu/(1+\mu)$ et les seuils de budget tiennent. Le programme linéaire sur les tests randomisés redonne $\mu/(1+\mu)$ à $10^{-9}$ près.

**Contre-exemple de la note.** Avec $T=100$, $k=1$ et $\delta=0{,}01$, le budget minimal vaut $B^\star=99$, contre 460,5 pour la borne annoncée. La borne $(T-k+1)/k\cdot\log(1/\delta)$ est fausse dans 430 cas sur 2 842 de ma grille, et quand $k$ et $T$ sont grands elle est fausse ou vraie de peu.

**Théorème de mise en œuvre aléatoire.**
- Pour (a) : la décomposition, la borne $b=\gamma W/n$, la variance au plus $(\gamma W)^2\bar\rho\Gamma_K/n$, l'inversion de Bernstein et l'union sur $2K$ événements sont justes. Le point (c) en emploie la version unilatérale sur $K$ événements, ce qui donne $\delta/2$.
- Pour (b) : la borne est juste. Les probabilités de queue exactes, de $2{,}5\cdot10^{-3}$ à $4{,}7\cdot10^{-3}$, restent sous $e^{-\Lambda'}$.
- Pour (c) : la division de $\delta$ en deux moitiés et l'argument du plafond, où le processus plafonné égale le processus sans plafond, sont justes.
- L'inflation (`eq:audit-inflation`) et ses deux formes explicites tiennent, sans violation sur 2 422 cas ; la majoration $\Gamma_K\le\min(K,\eta/\gamma)$ aussi.
- Pour $\gamma=\eta$, j'ai calculé les écarts exacts par loi binomiale, sans simulation de la garantie de seuil. Ils restent sous $e^{-\Lambda}$.

**Proposition sur l'indiscernabilité.** Les points (a) et (b) sont justes : aucune violation sur $2\cdot10^5$ tirages. Le taux de maintien pour $\tau\le\delta_{\mathrm{ind}}$ est juste.

**Script du brouillon.** Relancé sur une copie, il redonne exactement les chiffres de la note : écart $2{,}4\cdot10^{-8}$, aucune violation, $B^\star=99$, échecs de 0,275 % et 0,4 %.

**Compilation.** Avec un emballage minimal (`amsthm`, macros `\E`, `\Prob`, `\DKL`), le fragment compile en 7 pages, sans erreur ni boîte trop pleine. Seules les citations restent indéfinies, ce qui est attendu puisque les références sont en commentaire.

**Règle de symétrie (R4).** L'absence de violation est attendue pour des énoncés prouvés. Mes vérifications ont du pouvoir de discrimination : elles trouvent les contre-exemples de M2 et de m1, et elles visent les cas de bord ($C=c=0$, $\gamma=\eta$, $\eta=\infty$, frontière $\Delta R\,G_K=c$). La garantie de seuil n'est pas éprouvée ici ; elle est renvoyée à l'expérience préenregistrée ailleurs.

## Références à vérifier sur PDF (R7)

Citées par le brouillon :
- Avenhaus, von Stengel et Zamir 2002 : pages 1947 à 1987.
- Dresher 1962 : numéro RM-2972-ARPA.
- Tambe 2011.
- Blocki et al., IJCAI 2013 : ordre des auteurs.
- Becker 1968.
- Yao 1977.
- Le Cam 1973 : attribution de la méthode à deux points.
- Yu 1997.
- Boucheron, Lugosi et Massart 2013 : numéro du théorème de Bernstein.
- Freedman 1975.
- Hoeffding 1963.
- Serfling 1974.
- Greenblatt et al., arXiv:2312.06942 : régime d'une capture qui met fin à la partie.
- Griffin et al., arXiv:2409.07985 : titre exact, voir m11, et liste des auteurs.
- Cen et al. 2022 (`cen2022fast`), absente ici mais citée par la section sur la dynamique pour la même récurrence ; à citer.

Antériorité à confronter, que je suggère sans l'avoir vérifiée :
- **Contrôle à faibles enjeux et menaces diffuses :** Wen et al. 2024, arXiv:2411.17693 ; Christiano 2021, « Low-stakes alignment » ; Korbak et al. 2025, sur l'évaluation des mesures de contrôle.
- **Récompense rare auditée et repondérée :** Amodei et al. 2016, *Concrete Problems in AI Safety*, section sur la supervision à l'échelle ; Christiano 2016, « Semi-supervised reinforcement learning » ; Krueger et al. 2016, *Active reinforcement learning: observing rewards at a cost*.
- **Enseignement de politique et empoisonnement de récompense sous budget :** Zhang et Parkes 2008 ; Zhang, Parkes et Chen 2009 ; Rakhsha et al. 2020, ICML ; Zhang et al. 2020, *Adaptive reward-poisoning attacks against reinforcement learning*.
- **Meneur face à des apprenants :** Deng, Schneider et Sivan 2019, *Strategizing against no-regret learners* ; Blum, Haghtalab et Procaccia 2014.
- **Jeux d'inspection et dissuasion :** Andreozzi 2004, *Rewarding policemen increases crime*, Public Choice ; Tsebelis 1989 ; Maschler 1966 ; Kuhn 1963 ; Avenhaus et Canty 1996, *Compliance Quantified* ; Polinsky et Shavell 1979, échange entre probabilité et montant de l'amende, AER.
- **Recouvrement hypergéométrique et taille d'audit :** Saltman 1975 ; Rivest 2006, *On estimating the size of a statistical audit* ; Aslam, Popa et Rivest 2007 ; Ateniese et al. 2007, *Provable data possession*, CCS ; plans d'échantillonnage à zéro acceptation ; Alpern et Gal 2003, jeux de recherche.
- **Taux sans événement :** règle des trois, Hanley et Lippman-Hand 1983.

## Commandes lancées

```
P=/tmp/claude-0/-home-user-controle-ia-travail/c88f1f22-9d69-5421-86a6-86f206ad7a55/scratchpad
cd papiers/D/theorie/brouillon-fable-budget-audit-v1 && cat *.sha256 && sha256sum audit-budget-section-v1.tex check_audit_v1.py note-to-orchestrator-v1.md
cp audit-budget-section-v1.tex check_audit_v1.py $P/verif-bud/copie/
cd $P/verif-bud/copie && $P/venv/bin/python -I check_audit_v1.py          # sortie-check-audit-v1.txt
cd $P/verif-bud && $P/venv/bin/python -I v1_dissuasion.py                  # sortie-v1.txt
$P/venv/bin/python -I v1b_ecart_final.py v1_dissuasion.py                  # diagnostic du cas C = c = 0
$P/venv/bin/python -I v2_detection.py                                      # sortie-v2.txt
$P/venv/bin/python -I v3_aleatoire.py                                      # sortie-v3.txt
$P/venv/bin/python -I v4_indiscernabilite.py                               # sortie-v4.txt
cd $P/verif-bud/latex && pdflatex -interaction=nonstopmode -halt-on-error emballage.tex   # deux passes, 7 pages
grep (clés de citation du manuscrit statique et de la section sur la dynamique)
```

Graines : `numpy.random.SeedSequence(20261124_01)`, `(…_03)`, `(…_04)`. Environnement : Python du bloc-notes, avec numpy et scipy. Aucun accès au réseau, aucune dépense, aucun fichier du dépôt modifié.
