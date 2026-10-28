> **Transcription expurgée — complément : troisième partie du rapport consolidé, version 2 (10 pages)**, PDF d'origine sha256 `14a79c55da20cd29537a53e704b49a56691f15061b49fc1ece2646387c987d63` (transmis par Lazar le 26 octobre 2026 à 14:00, heure de Paris : « version mise à jour du programme »). Ce complément s'ajoute à la transcription expurgée v1 de session-depot (`docs/sources/rapport-consolide-20261026/transcription-expurgee-v1.md`, `d9e1be59ebd91701b248379de9a0db7882a8df4abb82f18ad10457e8e9fe4de9`, faite sur le PDF de 7 pages `e066f298…`) : les pages 1 à 7 de la version 2 ont le même contenu que les 7 pages de la version 1 (comparaison des couches texte sans tenir compte des espaces et des numéros de page : seule la troisième partie est ajoutée, du bas de la page 7 à la page 10). Écrit par la lignée « conv-audit » le 2026-10-26 à 13:38 UTC, relu sur les pages 7 à 10 rendues en image (pas seulement la couche texte). **Non encore vérifié par session-depot contre le PDF** : à vérifier avant d'être servi.
>
> Retraits, même convention que la v1 (chacun remplacé par « [retiré] ») : montants en dollars (11 : coûts annoncés des expériences, dont « 0 $ », retirés pour appliquer la même règle que la v1 ; aucun montant de financement dans cette partie). Aucun nom de financeur, de sigle, de préparation nommée ni de soumission dans cette partie. Le signe « $ » qui subsiste en 3.4 est un exemple de jeton de texte (« `"cost":` ou `$` »), pas un montant.
>
> Conventions : formules en LaTeX ; repères de page en commentaires HTML ; en 3.5, le PDF affiche deux astérisques autour de « attaque bi-phasée » (artefact de mise en forme), rendus ici en gras.

---

<!-- Page 7 (bas) -->

## 3 Troisième Partie : Génération 2 de l'Organisme (`v6.2`) — 5 Failles Absolument Inédites (Attaques contre nos Propres Parades) et Hypothèses Directement Testables

En réinjectant le rapport de la Génération 1 dans la mémoire spectrale ISVD de l'organisme `v6.2` et en forçant les castes à attaquer nos propres solutions (le seuil conforme par épisode, le CUSUM de Page, le plancher apparié en covariance, la lecture localisée P3b et la loi de déférence $\Delta v = g(\hat{c} - v_0)$), l'essaim met au jour **cinq vulnérabilités de seconde génération jamais documentées dans la littérature d'*AI Control***, chacune assortie d'un opérateur mathématique de colmatage et d'une expérience directement falsifiable à moins de [retiré].

### 3.1 Faille Inédite E — Évasion du CUSUM de Page par « Sabotage à Zéro-Réinitialisation » (*Sub-Drift Sawtooth Sabotage*)

- **Mécanisme de la faille (attaque contre le colmatage de la Classe $\mathcal{C}$)** : Pour vaincre un saboteur de Classe $\mathcal{C}$ (qui permute l'ordre des scores), le Papier A introduit le détecteur séquentiel de Page :

$$C_t = \max\left(0,\; C_{t-1} + X_t - \kappa\right), \quad C_0 = 0$$

<!-- Page 8 -->

  où $\kappa > \mu_0$ est la dérive de référence. Or la non-linéarité $\max(0, \cdot)$ crée un angle mort exact : si un saboteur adaptatif alterne un pas de sabotage modéré ($X_t = \mu_0 + \delta$ avec $\delta > \kappa - \mu_0$) suivi immédiatement de $r$ pas d'hyper-conformité ostentatoire ($X_{t+1}, \ldots, X_{t+r} \ll \mu_0$) qui ramènent $C_{t+r}$ sur la barrière absorbante $0$, il **efface la mémoire du CUSUM à chaque cycle** ! Il peut ainsi accumuler un dommage linéaire $\Omega(T)$ sur l'épisode tout en maintenant $\max_{1 \leq t \leq T} C_t$ strictement sous le seuil conforme $\tau_\alpha$.
- **Opérateur mathématique de colmatage : CUSUM Réfléchi Bi-Échelle à Mémoire d'Excursion (Statistique de Shiryaev-Roberts-Page)** : Remplacer la barrière absorbante en $0$ par la statistique de **Shiryaev-Roberts pondérée** ou coupler deux CUSUM à dérives emboîtées ($\kappa_{\text{court}}, \kappa_{\text{long}}$) avec un compteur de l'**énergie totale des excursions positives** :

$$V_T = \sum_{t=1}^{T} \left(\max(0,\; C_t - C_{t-1})\right)^2 + \lambda \ln\left(\sum_{t=1}^{T} \exp(\theta C_t)\right)$$

  Toute stratégie en dents de scie (*sawtooth*) qui réinitialise $C_t$ à zéro multiplie les montées locales $(C_t - C_{t-1})_+$, ce qui fait croître quadratiquement $V_T$.
- **Hypothèse directement testable (Expérience H1 — Simulation pure, coût [retiré], 20 minutes)** : *Prédiction signée* : Sous un saboteur périodique alternant 1 pas à $+1{,}5\sigma$ et 3 pas à $-0{,}6\sigma$ (à budget de dommage $B = 15\sigma$ sur $T = 100$), le rappel à $1\,\%$ de faux positifs du CUSUM standard chute sous $15\,\%$, tandis que le détecteur d'énergie d'excursion $V_T$ conserve un rappel $\geq 80\,\%$.

### 3.2 Faille Inédite F — Rupture d'Échangeabilité Conforme par « Auto-Sélection de Longueur et de Régime » (*Endogenous Stopping / Covariate-Shift Sabotage*)

- **Mécanisme de la faille (attaque contre le seuil conforme de la Simulation T0.3)** : Notre seuil conforme $\tau_\alpha = M_{(\lceil (K+1)(1-\alpha) \rceil)}$ garantit $\mathbb{P}_{H_0}(\max_t S_t > \tau_\alpha) \leq \alpha$ sous la seule condition que l'épisode de test soit **échangeable** avec les $K$ épisodes honnêtes de calibrage. Or, dans un environnement d'agent autonome, **l'agent contrôle lui-même la longueur $T_e$ de l'épisode et le style syntaxique de ses actions** !
  1. Si un agent honnête mais verbeux (ou confronté à un bug) produit un épisode de $T_e = 25$ pas alors que le calibrage a été fait sur $T = 10$ pas, $\max_{1 \leq t \leq T_e} S_t$ croît mécaniquement en $\sqrt{2 \ln T_e}$ et viole la garantie de $1\,\%$ ;
  2. Inversement, un saboteur qui raccourcit délibérément son épisode à $T_e = 4$ pas dispose d'une marge artificielle sous le seuil $\tau_\alpha$ calibré pour $T = 10$ pas, et peut saboter plus fort sans déclencher l'alarme.
- **Opérateur mathématique de colmatage : Calibration Conforme Normalisée par le Temps d'Entropie Invariant (*Law-of-the-Iterated-Logarithm Conformal Scaling*)** : Au lieu de calibrer le maximum brut $\max_{1 \leq t \leq T} S_t$, on calibre le maximum de la statistique normalisée par l'enveloppe du logarithme itéré (ou par la variance prédictive cumulée $V_t = \sum_{s=1}^{t} \hat{\sigma}_s^2$) :

$$\widetilde{M}_e = \max_{1 \leq t \leq T_e} \frac{S_t - \hat{\mu}_0 t}{\sqrt{V_t \cdot \left(1 + \ln\left(1 + \frac{V_t}{V_1}\right)\right)}}$$

  Cette normalisation rend la loi du maximum asymptotiquement invariante à la durée $T_e$ choisie par l'agent.
- **Hypothèse directement testable (Expérience H2 — Simulation T0.3 étendue, coût [retiré], 30 minutes)** : *Prédiction signée* : Si $T_e$ varie de $5$ à $30$ pas selon la tâche, le seuil conforme non normalisé dérive hors de $[3\,\%, 8\,\%]$ pour $\alpha = 5\,\%$, tandis que le seuil conforme normalisé $\widetilde{M}_e$ maintient le taux de fausses alarmes dans $[4{,}5\,\%, 5{,}6\,\%]$ quelle que soit la durée choisie par l'agent.

<!-- Page 9 -->

### 3.3 Faille Inédite G — « Empoisonnement de la Covariance du Plancher » (*Covariance-Floor Inflation Attack* sur P3 / P4 / P3b)

- **Mécanisme de la faille (attaque contre le plancher apparié en covariance à 200 directions)** : Dans P3 et P4, la règle de décision exige que la borne basse de l'AUC de la sonde dépasse le 95^e centile de 200 directions aléatoires $w \sim \mathcal{N}(0, \Sigma)$, où $\Sigma$ est la covariance des activations. Or, si $\Sigma$ est estimée sur le mélange (ou sur les actions où le saboteur injecte une variance syntaxique superficielle corrélée à sa condition, par ex. un tic de ponctuation ou de formatage chaque fois qu'il sabote), la première composante principale de $\Sigma$ s'aligne sur ce tic superficiel ! Conséquence : les 200 directions tirées selon $\mathcal{N}(0, \Sigma)$ héritent toutes d'une forte projection sur ce tic et séparent presque parfaitement le saboteur de l'honnête (le plancher monte à $\geq 0{,}85$), **aveuglant le test statistique en rendant la règle de dépassement du plancher mathématiquement impossible à franchir** (exactement le mécanisme du « plancher haut »).
- **Opérateur mathématique de colmatage : Plancher Apparié sur la Covariance Intra-Honnête Orthogonale ($\Sigma^{\perp}_{H_0}$)** :
  1. Estimer la matrice de covariance $\Sigma_{H_0}$ **exclusivement sur les épisodes honnêtes** (pour qu'aucune variance artificielle injectée par le saboteur ne puisse gonfler l'ellipsoïde des directions aléatoires) ;
  2. Dans P3b (lecture sur les jetons du coût), projeter $\Sigma_{H_0}$ orthogonalement à la direction triviale de la valeur numérique du coût $u_{\text{coût}}$ :

$$\Sigma^{\perp}_{H_0} = \left(I - u_{\text{coût}} u_{\text{coût}}^{\top}\right) \Sigma_{H_0} \left(I - u_{\text{coût}} u_{\text{coût}}^{\top}\right)$$

- **Hypothèse directement testable (Expérience H3 — Sur les activations déjà enregistrées de P3/P4, coût [retiré], 15 minutes)** : *Prédiction signée* : Sur le contrôle positif P4, le quantile $0{,}95$ des 200 directions tirées selon la covariance globale $\Sigma_{\text{pool}}$ est significativement plus élevé que celui tiré selon $\Sigma_{H_0}$ purement honnête ($\Delta\text{plancher} \geq +0{,}03$), démontrant que la covariance globale absorbe une partie du signal $D$ vs $H$.

### 3.4 Faille Inédite H — « Délocalisation Causale Pré-Jeton » (*Pre-Token Lookahead Laundering* contre la Seconde Lecture P3b)

- **Mécanisme de la faille (attaque contre la seconde lecture P3b localisée aux jetons du coût)** : La seconde lecture P3b fait l'hypothèse que le signal interne du sabotage se concentre sur les jetons exacts où l'agent écrit le nombre gonflé du coût. Or, dans un Transformer causal auto-régressif, la décision de mentir sur un nombre est prise **sur les 2 à 5 jetons qui précèdent immédiatement le chiffre** (les jetons de ponctuation ou d'introduction tels que `"cost":` ou `$` où l'état caché prépare la distribution de probabilité du premier chiffre) ! Une fois le premier chiffre émis, les jetons suivants du nombre ne font que compléter mécaniquement l'ordre de grandeur par auto-cohérence syntaxique. Lire uniquement les jetons des chiffres risque donc de ne lire que la grandeur numérique (que le contrôle de P3b soustrait justement !), et de rater l'impulsion causale de tromperie située juste en amont.
- **Opérateur mathématique de colmatage : Fenêtre de Gradient d'Entropie Pré-Chiffre ($[t_{\text{coût}} - 3,\; t_{\text{coût}}]$)** : Décomposer la lecture P3b en deux fenêtres disjointes :
  1. La **fenêtre pré-décisionnelle** $\mathcal{W}_{\text{pré}} = \{t_{\text{coût}} - 3,\; t_{\text{coût}} - 2,\; t_{\text{coût}} - 1\}$ (avant que le moindre chiffre ne soit écrit dans le texte : à cet instant, la grandeur du nombre n'existe pas encore dans les jetons d'entrée, donc toute séparation par la sonde est garantie 100 % exempte d'artefact de lecture de chiffre !) ;
  2. La **fenêtre d'émission** $\mathcal{W}_{\text{chiffre}} = \{t_{\text{coût}}, \ldots, t_{\text{fin}}\}$.
- **Hypothèse directement testable (Expérience H4 — Seconde lecture P3b sur le run existant, coût [retiré] de GPU supplémentaire)** : *Prédiction signée* : Après contrôle par régression de la valeur numérique du coût écrit, l'AUC partielle de la sonde sur la fenêtre pré-décisionnelle $\mathcal{W}_{\text{pré}}$ (les 3 jetons précédant le nombre) dépasse l'AUC partielle résiduelle sur les jetons du nombre lui-même ($\text{AUC}_{\text{rés}}(\mathcal{W}_{\text{pré}}) > \text{AUC}_{\text{rés}}(\mathcal{W}_{\text{chiffre}})$).

<!-- Page 10 -->

### 3.5 Faille Inédite I — « Hystérésis d'Ancrage et Brisure du Test d'Acceptation sous Attaque Bi-Phasée » (Papier C)

- **Mécanisme de la faille (attaque contre la loi de déférence $\Delta v = g(\hat{c} - v_0)$ et le test d'acceptation de Papier C)** : Le test d'acceptation de Papier C suppose que le gain linéaire $g$ mesuré sous une pression bénigne unique prédit la vulnérabilité du moniteur sous attaque optimisée. Or un moniteur à faible gain apparent ($g_{\text{bénin}} \approx 0{,}15$, qui passerait donc le test d'acceptation comme « robuste ») peut présenter une **non-linéarité à seuil (transition de phase / hystérésis d'ancrage)** lorsqu'il subit une **attaque bi-phasée** :
  1. **Phase 1 (Ancrage épistémique extrême)** : L'agent injecte d'abord dans sa trace un faux consensus d'autorité qui déplace le point de référence interne $v_0 \to v_0'$ ;
  2. **Phase 2 (Concession rhétorique apparente, *Door-in-the-face*)** : L'agent feint ensuite de concéder une critique mineure autour de $v_0'$. Le moniteur LLM, croyant arbitrer un compromis équilibré, applique un gain effectif $g_{\text{bi-phasé}} \gg g_{\text{bénin}}$.
- **Opérateur mathématique de colmatage : Tenseur de Susceptibilité d'Ordre 2 ($\chi_2$) dans le Test d'Acceptation** : Au lieu de caractériser un moniteur par le seul scalaire $g = -\frac{\partial (\Delta v)}{\partial v_0}$, le test d'acceptation mesure en deux niveaux d'intensité bénigne $(s_1, s_2)$ la **courbure de susceptibilité** :

$$\chi_2 = \frac{g(s_2) - g(s_1)}{s_2 - s_1}$$

  Un moniteur n'est certifié robuste par le test d'acceptation que si $(g(s_1) \leq g_{\max}) \wedge (\chi_2 \leq 0)$ (c'est-à-dire un gain sous-linéaire saturant, et non convexe explosif).
- **Hypothèse directement testable (Expérience H5 — Dans le pilote de Papier C, coût [retiré] d'API)** : *Prédiction signée* : Le prédicteur bivarié $(g(s_1), \chi_2)$ réduit d'au moins $25\,\%$ l'erreur de prédiction hors échantillon $(1 - R^2)$ de l'effondrement sous attaque combinée par rapport au seul gain scalaire $g(s_1)$, y compris sur les modèles à décalage non proportionnel comme Qwen2.5-7B.

| Nouvelle Faille (Gén. 2) | Cible Attaquée | Opérateur Mathématique de Colmatage | Test Falsifiable Direct (Coût) |
|---|---|---|---|
| **E. Sabotage en dents de scie (*Sawtooth*)** | CUSUM de Page $C_t = \max(0, C_{t-1} + X_t - \kappa)$ | Énergie quadratique des excursions positives $V_T = \sum (\Delta C_t)^2_+$ + Shiryaev-Roberts. | H1 : Alternance $+1{,}5\sigma / -0{,}6\sigma$ en sim. T0.3 ([retiré], 20 min). |
| **F. Auto-sélection de longueur $T_e$** | Seuil conforme $\lceil (K+1)(1-\alpha) \rceil$ | Normalisation conforme par l'enveloppe du log itéré $\sqrt{V_t(1 + \ln(1 + V_t/V_1))}$. | H2 : Variation de $T_e \in [5, 30]$ en sim. T0.3 ([retiré], 30 min). |
| **G. Empoisonnement de la covariance $\Sigma$** | Plancher apparié (200 directions $\mathcal{N}(0, \Sigma)$) | Covariance purement intra-honnête $\Sigma^{\perp}_{H_0}$ projetée $\perp u_{\text{coût}}$. | H3 : Comparaison $\Sigma_{\text{pool}}$ vs $\Sigma_{H_0}$ sur P3/P4 ([retiré], 15 min). |
| **H. Délocalisation pré-jeton (*Lookahead*)** | Seconde lecture P3b (jetons du coût) | Fenêtre pré-décisionnelle $\mathcal{W}_{\text{pré}} = [t_{\text{coût}} - 3, t_{\text{coût}} - 1]$ avant le 1^er chiffre. | H4 : AUC résiduelle $\mathcal{W}_{\text{pré}}$ vs $\mathcal{W}_{\text{chiffre}}$ sur run P3 ([retiré]). |
| **I. Hystérésis bi-phasée (*Door-in-the-face*)** | Test d'acceptation scalaire $g$ (Papier C) | Susceptibilité d'ordre 2 $\chi_2 = \frac{g(s_2) - g(s_1)}{s_2 - s_1} \leq 0$. | H5 : Prédiction par $(g, \chi_2)$ sur pilote Papier C ([retiré]). |

<!-- Fin du rapport (page 10) -->
