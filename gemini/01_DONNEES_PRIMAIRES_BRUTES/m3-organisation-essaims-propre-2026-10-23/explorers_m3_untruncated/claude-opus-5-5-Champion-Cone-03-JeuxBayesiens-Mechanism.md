BASSIN_MATH: Contrat d'Équipe Holmström–Dasgupta-Ghosh à Audit Concavifié (CEHDG-AC)

LOI_PROPOSEE: $R_i=\underbrace{\big[\mathbb{1}(r_i^t=r_j^t)-\mathbb{1}(r_i^{t'}=r_j^{t''})\big]_{f(i)\neq f(j)}}_{\text{DG détendancé inter-familles}}+\pi^*(\mu)\,B(r_i,\text{jev})+\mathbb{1}(Q\ge\bar Q)\,s_i-c_i$, avec $\pi^*=\arg\max_\pi \operatorname{cav}V(\mu)$ et des parts de budget $b_i\propto\exp(\eta\,\bar R_i/\$_i)$.

**1. Mécanisme d'auto-organisation hors-poids**

- **Tâches et pairs.** Chaque agent rapporte des verdicts $r_i$ sur des tâches partagées. Son pair $j$ est tiré obligatoirement dans une autre famille de poids, Claude ou Gemini.
- **Correction de corrélation (H4').** Le terme de Dasgupta-Ghosh soustrait l'accord observé sur des tâches distinctes $t',t''$. Un accord dû à un biais commun rapporte donc zéro.
- **Arbitrage monoculture/chimère.** La monoculture n'est conservée que si sa covariance détendancée est inférieure à celle de la chimère.
- **Topologie.** Les poids de communication suivent $w_{ij}\leftarrow w_{ij}\,e^{\eta R_{ij}}$.
- **Spawn d'un agent.** Un explorateur est créé si la valeur d'information $\mathrm{VoI}=\mathbb{E}[\Delta H(\mu)]$ dépasse son coût. Un démolisseur Red-Team est créé si le postérieur $\mu(\text{claim})>0{,}8$ et si la diversité des familles est inférieure à 2.
- **Dérive de consigne (H9).** `jev` compare chaque sous-consigne à la consigne racine. Toute divergence au-delà d'un seuil $\tau$ annule $R_i$.
- **Récitation de la mémoire paramétrique.** Toute affirmation doit porter un identifiant Semantic Scholar, arXiv ou Crossref, vérifié par l'API. Une affirmation sans identifiant valide reçoit un verdict nul.
- **Budget.** Les parts sont réallouées par tour selon le score par dollar, sous les plafonds de 100 USD pour Claude et 20 USD pour Gemini.

**2. Fonction objectif et dispositif anti-Goodhart**

L'essaim maximise $\sum_i R_i$ sous $\sum_i c_i\le$ budget, avec trois protections :

- **Persuasion de Kamenica-Gentzkow.** L'orchestrateur s'engage sur une politique d'audit $\pi^*$ obtenue par concavification. Les agents ignorent quelles tâches seront jugées par `jev`. Comme le score de Brier $B$ est propre, rapporter sa vraie croyance est une stratégie optimale, et optimiser contre le juge n'est pas rentable.
- **Contrat de Holmström.** La part d'équipe $s_i$ n'est versée que si la qualité collective $Q$, mesurée sur des audits cachés, atteint le seuil $\bar Q$. Sinon, la part est confisquée, ce qui rompt l'équilibre budgétaire et empêche le passager clandestin.
- **Équilibre véridique.** Le terme de Dasgupta-Ghosh rend l'équilibre véridique strictement préférable à toute collusion non informative.

**3. Duel décisif ($H_A\perp H_B$), à budget constant de 120 USD**

Quatre bras, chacun sur 30 graines :
- **(A) CEHDG-AC** adaptatif ;
- **(B) Topologie fixe** chimérique ;
- **(C) Essaim i.i.d.** monoculturel ;
- **(D) Contrôle négatif** : CEHDG-AC dont les scores $R_i$ sont permutés aléatoirement entre agents.

Protocole et métrique :
- La métrique est l'exactitude sur 500 affirmations bibliographiques vérifiables, tenues à l'écart et jamais auditées pendant l'évolution.
- La covariance d'erreur inter-agents est mesurée en parallèle.

Hypothèses :
- **$H_A$** : A dépasse B et C d'au moins 5 points, avec une covariance d'erreur plus faible.
- **$H_B$** : D ne fait pas mieux que B. Cela prouve que le gain vient du signal incitatif et non de la seule adaptativité.

Test et critère de réfutation :
- Le test est un test de permutation pré-enregistré au seuil $\alpha=0{,}01$, avec correction de Holm.
- La loi est réfutée si A ne dépasse pas B, ou si D égale A.
