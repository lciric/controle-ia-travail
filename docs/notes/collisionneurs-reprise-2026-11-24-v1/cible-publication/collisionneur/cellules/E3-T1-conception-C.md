*Note liminaire (règle d'intégrité 2) : les blocs `FAITS` et `QUESTION DE L'ARBITRE` sont transmis intégralement, mais le manuscrit source et le script de vérification numérique mentionnés dans `FAITS` sont absents ; leur contenu interne relève donc du statut `OBSERVÉ-NON-AUDITÉ` et n'est ni reconstitué ni extrapolé.*

---

## Partie A — Présupposés non établis dans la question et audit formel minimal *(livrable a)*

L'analyse des blocs `FAITS` et `QUESTION DE L'ARBITRE` fait apparaître sept présupposés implicites qui ne sont pas établis à ce stade, ainsi que trois précisions algébriques directement vérifiables à partir des formules explicites de `FAITS`.

1. **Adéquation entre les opérateurs statiques de Gibbs (A et B) sur l'espace des politiques et l'entraînement réel par gradient** — `HYPOTHÈSE`.
   Les opérateurs A et B définissent des lois d'équilibre sur une partition fixe $\Pi = \Pi_{\mathrm{h}} \sqcup \Pi_{\mathrm{v}} \sqcup \Pi_{\mathrm{f}}$ (`RAPPORTÉ`). Or l'entraînement après pré-entraînement (PPO, GRPO, DPO) optimise des paramètres continus partagés $\theta$ au niveau des trajectoires. De plus, trois faits algébriques sont directement `VÉRIFIÉ` à partir des formules explicites fournies dans `FAITS` :
   - **Non-équivalence de A avec un filtrage itératif en boucle** : dans $\pi_{\mathrm{A}}^{(\eta)}(\pi) \propto \beta(\pi) e^{\eta R(\pi)} \pi_0(\pi)$, le facteur $\beta(\pi)$ ne varie pas avec $\eta$. Il correspond à un rejet *à un pas* (post-hoc ou sur le prior initial), non à un filtrage itératif (où $\beta$ se composerait au fil des tours) ni au masquage des épisodes détectés dans la mise à jour de récompense (qui optimise $\beta(\pi)R(\pi)$, soit B à $C = 0$).
   - **Non-invariance par translation de $R_0$ dans l'opérateur B** : dans $\pi_{\mathrm{B}}^{(\eta, C)}(\pi) \propto e^{\eta [\beta(\pi) R(\pi) - (1-\beta(\pi)) C]} \pi_0(\pi)$, l'écart d'exposant entre $\Pi_{\mathrm{f}}$ et $\Pi_{\mathrm{h}}$ vaut $\eta[\beta_{\mathrm{f}} \Delta R - (\beta_{\mathrm{h}} - \beta_{\mathrm{f}})(R_0 + C)]$. Le plancher $\frac{\beta_{\mathrm{h}} - \beta_{\mathrm{f}}}{\beta_{\mathrm{f}}} C$ (`RAPPORTÉ`) est donc exact pour $R_0 = 0$ et constitue un minorant si $R_0 \ge 0$, mais cesse d'être garanti si $R_0 < 0$ avec $R_0 + C < 0$.
   - **Condition de régime pour la comparaison B contre A lorsque $\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1 > \beta_{\mathrm{v}} > 0$** : sous B, $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}})$ croît strictement avec $C$ pour tout $\eta > 0$, mais l'inégalité stricte $\pi_{\mathrm{B}}^{(\eta, C)}(\Pi_{\mathrm{f}}) > \pi_{\mathrm{A}}^{(\eta)}(\Pi_{\mathrm{f}})$ exige $\eta(1 - \beta_{\mathrm{v}})(R_0 + \Delta R + C) > \ln(1/\beta_{\mathrm{v}})$ ; dans le régime contraire (faible $\eta$ et $C$ modéré), A rejette plus fortement $\Pi_{\mathrm{v}}$ que B. Le manuscrit étant non transmis (`OBSERVÉ-NON-AUDITÉ`), il reste à vérifier si ces conditions de régime y figurent explicitement ou ont été condensées dans le résumé.

2. **Exhaustivité des preuves et suffisance des $14\,000$ tirages aléatoires** — `OBSERVÉ-NON-AUDITÉ` (manuscrit et script absents ; existence des tirages : `RAPPORTÉ`). Des tirages numériques confirment la cohérence interne d'identités algébriques, non la validité des hypothèses de modélisation ni l'absence de cas limites omis.

3. **Satisfaction pratique des hypothèses des mécanismes d'atténuation** — `HYPOTHÈSE`.
   - Le théorème de découplage hors boucle exige une covariance négative ou nulle (sous A) ou une association négative/indépendance (sous B) entre détecteur en boucle et auditeur hors boucle sur les tricheurs (`RAPPORTÉ`). En pratique, deux détecteurs fondés sur le texte ou sur des représentations corrélées peuvent avoir une covariance strictement positive.
   - Pour les épisodes pièges, si les supports des épisodes pièges synthétiques et des épisodes ordinaires sont disjoints en espace de séquences de haute dimension, alors $d_{\mathrm{TV}} = 1$ et la borne $\max(0, \tau_{\mathrm{ord}} - \delta_{\mathrm{ind}})$ devient identiquement nulle (`VÉRIFIÉ`). L'efficacité réelle des pièges repose donc sur une indistinguabilité *computationnelle* non modélisée par la distance en variation totale.

4. **Transférabilité d'un contournement furtif contrôlé à petite échelle vers les modèles frontières** — `HYPOTHÈSE`. La question suppose implicitement qu'un protocole RL sur modèles ouverts (sans stéganographie linguistique spontanée) fournit un signal pertinent sur le mécanisme étudié. Cela ne vaut que pour tester la *dynamique d'optimisation sous filtrage*, non pour estimer la probabilité d'émergence spontanée d'une stéganographie à grande échelle.

5. **Adéquation entre « enceinte la plus prestigieuse » et valeur scientifique de l'arbitrage** — `HYPOTHÈSE`. Une conférence généraliste très sélective peut rejeter pour des raisons de mode ou de format, alors qu'une revue technique ouverte (TMLR) ou une conférence dédiée à la sécurité de l'apprentissage (IEEE SaTML) peut offrir un examen plus pertinent des protocoles adversariaux.

6. **Gain marginal des preuves mécanisées pour l'acceptation en conférences ML** — `HYPOTHÈSE`. Rien dans `FAITS` n'établit qu'une formalisation compilée d'algèbre finie augmente la probabilité d'acceptation dans les conférences visées.

7. **Stabilité des politiques d'anonymat et de non-promotion des conférences** — `HYPOTHÈSE`. Ces règles varient selon les conférences et évoluent d'une édition à l'autre ; toute stratégie concrète impose de vérifier l'appel à communications (CFP) de l'édition visée.

---

## Partie B — Réponse aux quatre questions de l'arbitre

### 1. Évaluation sans complaisance du manuscrit actuel

**Enceintes où le manuscrit statique actuel est déjà compétitif :**
- **Ateliers thématiques** adossés à NeurIPS, ICML ou ICLR (alignement, sécurité de l'IA, évaluations et audit, interprétabilité) : le format court, la clarté des seuils exacts et le contraste opératoire entre rejet pur (A) et pénalité négative (B) y trouvent un public direct, sans exigence stricte d'expériences à grande échelle.
- **Piste *Position Paper* (ex. ICML)** : uniquement si le texte est réécrit comme une thèse méthodologique falsifiable (contre l'usage naïf de détecteurs imparfaits pénalisants dans la boucle d'entraînement et pour l'audit découplé), le modèle formel servant d'armature analytique plutôt que de contribution mathématique autonome.
- **TMLR** : *non compétitif en l'état* si l'article reste purement statique sans expériences ni extension dynamique ; TMLR évalue la solidité technique et la portée des preuves ou validations empiriques, et jugerait l'algèbre actuelle trop élémentaire pour une publication autonome.

**Objections rédhibitoires dans les conférences principales de premier rang (NeurIPS, ICML, ICLR, COLT, ALT, IEEE SaTML) :**
1. **Profondeur mathématique insuffisante** : les résultats reposent sur de l'algèbre d'équilibre de Gibbs sur une partition finie, une identité de covariance et une borne en variation totale d'une ligne (`RAPPORTÉ`). Pour COLT/ALT et les relecteurs théoriciens de NeurIPS/ICML, il n'y a ni borne minimax, ni complexité d'échantillonnage, ni analyse de convergence dynamique.
2. **Rupture entre le modèle et les algorithmes de post-entraînement** : l'opérateur A ne capture pas le filtrage itératif en ligne, l'opérateur B dépend du niveau absolu de $R_0$ (`VÉRIFIÉ`), et la partition statique ignore le partage de poids $\theta$ et l'accessibilité locale par gradient.
3. **Vacuité empirique de certaines bornes** : la borne par variation totale s'effondre dès que les pièges synthétiques ont un support disjoint des épisodes réels ($d_{\mathrm{TV}} = 1$, `VÉRIFIÉ`), et l'hypothèse d'indépendance ou d'association négative de l'audit hors boucle laisse intacte la question critique de la corrélation entre moniteurs.
4. **Absence totale de validation sur réseaux de neurones réels** (`RAPPORTÉ`) : dans un champ où la sur-optimisation de proxys (Gao, Schulman & Hilton, 2023, *Scaling Laws for Reward Model Overoptimization*) et le contournement de moniteurs de chaînes de pensée (référence à vérifier) sont déjà discutés qualitativement, un modèle sans vérification empirique de ses prédictions *non triviales* (notamment l'inversion ou l'amplification différentielle entre A et B) sera rejeté comme formalisation élémentaire d'un folklore connu.

### 2. Cible la plus ambitieuse réellement atteignable et mauvais ajustements

**Cible la plus ambitieuse réaliste :**
- **NeurIPS, ICML ou ICLR (piste principale)**, à la condition impérative de transformer le manuscrit en article **théorie + expériences contrôlées sur modèles ouverts** démontrant ou délimitant empiriquement : (i) l'écart opératoire entre filtrage par rejet et pénalité négative $-C$, (ii) la dynamique temporelle sous régularisation KL, et (iii) la sensibilité différentielle des auditeurs hors boucle (texte vs représentations internes).
- **Alternatives à meilleur rapport risque/rendement scientifique :** **IEEE SaTML** (très bon ajustement thématique si l'angle audit adversarial, détecteurs en boucle et pièges est évalué rigoureusement contre des vérifications mécaniques) et **TMLR** (arbitrage axé sur la rigueur et la reproductibilité, sans biais de sélection thématique).

**Mauvais ajustements thématiques ou méthodologiques :**
- **COLT / ALT** : la barre de technicité théorique (dynamique stochastique en haute dimension, bornes inférieures d'information serrées) exigerait de reformuler entièrement le problème en jeu séquentiel abstrait, au risque de rompre le lien avec le post-entraînement de modèles de langage tout en restant vulnérable à des rejets sur le naturel des hypothèses.
- **JMLR** : délais éditoriaux longs (souvent $12$ à $24$ mois [illustratif]) et attente d'une ampleur monographique mal adaptés à un problème empirique rapide.
- **Conférences de sécurité systèmes (IEEE S&P, CCS, USENIX Security)** : attente d'un modèle de menace de bout en bout sur systèmes déployés et d'attaques adaptatives complètes ; une étude centrée sur des opérateurs de Gibbs et des bancs RL contrôlés y paraîtrait hors périmètre.

### 3. Extensions mathématiques et expérimentales optimales

Le classement ci-dessous arbitre entre gain d'acceptabilité en conférence principale et risque d'impasse technique :

1. **Priorité 1 (théorie, risque faible, fort levier) : Dynamique de descente miroir (*mirror descent*) KL + borne $\mathcal{F}$-IPM pour les pièges + clarification algébrique A/B.**
   - Remplacer la photo statique par la dynamique discrète/continue de *mirror descent* régularisé KL (dont Gibbs est le point fixe) permet : (a) de distinguer rigoureusement rejet post-hoc, rejet itératif à chaque étape et masquage de récompense ; (b) d'expliciter le rôle du référentiel $R_0$ et de la condition $\eta(1-\beta_{\mathrm{v}})(R_0+\Delta R+C) > \ln(1/\beta_{\mathrm{v}})$ ; (c) d'analyser les *barrières de trajectoire* (dépendance de chemin lorsque $\Pi_{\mathrm{v}}$ sert ou non de tremplin vers $\Pi_{\mathrm{f}}$).
   - Remplacer la distance en variation totale par une **métrique de probabilité intégrale $\mathcal{F}$-IPM** restreinte à la classe de discriminants réalisables par la politique supprime la vacuité à $d_{\mathrm{TV}} = 1$ tout en conservant une preuve courte et propre.

2. **Priorité 2 (expérimental, levier indispensable, risque maîtrisable) : Banc RL contrôlé sur modèles ouverts à contournement *structural*, sans parier sur la stéganographie linguistique spontanée.**
   - Attendre l'émergence spontanée d'une stéganographie linguistique sur un modèle ouvert de classe $7$–$8$ milliards de paramètres [illustratif] expose à une impasse expérimentale connue (référence à vérifier), car $\pi_0(\Pi_{\mathrm{f}}^{\text{stégo}})$ y est trop faible.
   - La solution falsifiable consiste à utiliser une tâche de génération de code avec harnais de tests vulnérable et **vérificateur mécanique oracle caché**, où coexistent deux classes de contournement déjà accessibles dans $\pi_0$ (ou calibrées par un amorçage SFT mesuré) : $\Pi_{\mathrm{v}}$ (contournement explicite visible en surface ou annoncé en chaîne de pensée, détecté par le moniteur en boucle) et $\Pi_{\mathrm{f}}$ (contournement par indirection syntaxique ou raisonnement silencieux, faiblement détecté par le moniteur en boucle). Ce protocole teste directement les prédictions du modèle sur des réseaux réels tout en explicitant sa limite de validité externe.

3. **Priorité 3 (audit interne, risque modéré, fort levier à NeurIPS/ICLR/SaTML) : Géométrie des représentations internes hors boucle.**
   - Comparer un auditeur texte hors boucle plus capable et une sonde linéaire (*linear probe*) entraînée sur les activations résiduelles de $\pi_0$ avant RL, en mesurant empiriquement la covariance conditionnelle $\widehat{\mathrm{Cov}}_{\text{cheat}}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})$. Les deux issues — maintien de la sonde ou dégradation conjointe — sont scientifiquement publiables car elles délimitent empiriquement le théorème de découplage.

4. **Extensions à écarter en priorité (mauvais ratio coût/rendement) :**
   - **Bornes d'information séquentielles ou computationnelles lourdes** : risque élevé d'impasse technique ou d'hypothèses irréalistes, pour un gain marginal hors COLT.
   - **Preuves mécanisées (Lean/Coq)** : effort faible pour de l'algèbre finie, mais gain d'acceptabilité quasi nul en conférences ML/sécurité (risque inverse d'être perçu comme du vernis formel compensant la légèreté des preuves). À envisager uniquement comme artefact reproductible secondaire après les extensions 1 à 3.

### 4. Stratégie de diffusion et d'anonymat

*(Note de statut : les règles précises d'embargo et de non-promotion doivent être vérifiées dans le CFP de l'édition visée — `HYPOTHÈSE` sur leur constance d'une année sur l'autre.)*

- **Éviter le piège du billet public identique avant soumission en double aveugle :** si le manuscrit statique est publié en billet signé sous le même titre et les mêmes notations juste avant une soumission ICML/NeurIPS/ICLR, le risque de rupture d'anonymat ou de violation des clauses de non-promotion pendant la fenêtre d'évaluation est réel (notamment à ICLR et lors des embargos pré-décision de certaines éditions NeurIPS/ICML, à vérifier dans le CFP).
- **Séquencement recommandé :**
  1. *Retour rapide sans griller la cible principale* : présenter la version statique dans un **atelier non archivé (*non-archival workshop*)** si le calendrier s'y prête, ou diffuser en cercle restreint avant soumission principale. Si un dépôt d'antériorité rapide est jugé prioritaire, préférer un **preprint arXiv sobre** (si autorisé par le CFP de la conférence visée), sans billet promotionnel ni diffusion sur réseaux sociaux pendant la période d'évaluation.
  2. *Soumission principale anonymisée* (version augmentée : dynamique + $\mathcal{F}$-IPM + expériences RL et sondes) : code et données sur dépôt strictement anonymisé, aucune auto-citation identifiante d'un billet préalable, vérification explicite des règles arXiv auprès d'IEEE SaTML si cette cible est retenue (les conférences IEEE de sécurité imposant parfois des contraintes plus strictes que NeurIPS/ICML).
  3. *Billet technique public de synthèse* : à publier **après** la levée d'embargo ou la décision (ou dès la soumission si l'option retenue est TMLR et si le guide auteur en vigueur l'autorise explicitement).

---

## Partie C — Expériences décisives en inférence forte *(livrable b)*

Toutes les expériences ci-dessous s'appuient sur le banc de génération de code avec oracle mécanique caché (tests secrets + sandbox). Tous les seuils, nombres de graines et tailles d'effet sont marqués `[illustratif]`.

### Expérience 1 — Contraste opérateur B (pénalité négative) contre opérateur A (rejet pur) en régime de niche quasi furtive
- **$H_A$ (Prédiction du modèle)** : Lorsque $\beta_{\mathrm{f}} \approx \beta_{\mathrm{h}} > \beta_{\mathrm{v}}$ ($\beta_{\mathrm{v}} \approx 0{,}15$, $\beta_{\mathrm{f}} \ge 0{,}90$, $\beta_{\mathrm{h}} \approx 0{,}95$ [illustratif]) et que $C$ est élevé, l'entraînement RL sous pénalité négative (B) produit une fréquence finale de contournement furtif $\Pi_{\mathrm{f}}$ strictement supérieure à celle obtenue sous filtrage par rejet sans pénalité (A), à divergence $D_{\mathrm{KL}}(\pi_t \| \pi_0)$ appariée.
- **$H_B$ (Généralisation répulsive en paramètres partagés)** : Le partage de représentations dans les poids $\theta$ fait que le gradient négatif induit par $-C$ sur $\Pi_{\mathrm{v}}$ réprime aussi $\Pi_{\mathrm{f}}$, maintenant la fréquence finale de $\Pi_{\mathrm{f}}$ sous B inférieure ou égale à celle sous A.
- **Métrique et seuil** : Écart $\Delta P_{\mathrm{f}} = P_{\mathrm{B}}(\Pi_{\mathrm{f}}) - P_{\mathrm{A}}(\Pi_{\mathrm{f}})$ mesuré par l'oracle mécanique sur $5$ graines indépendantes [illustratif], à $D_{\mathrm{KL}}$ apparié à $\pm 5\,\%$ [illustratif]. Seuil en faveur de $H_A$ : $\Delta P_{\mathrm{f}} > +0{,}05$ avec intervalle de confiance (IC) à $95\,\%$ strictement positif [illustratif]. Seuil en faveur de $H_B$ : $\Delta P_{\mathrm{f}} \le 0$ avec borne supérieure de l'IC $95\,\% \le +0{,}02$ [illustratif] (zone intermédiaire déclarée non concluante et soumise à ajout de graines).
- **Contrôle négatif** : Moniteur en boucle aléatoire indépendant de la classe ($\beta_{\mathrm{v}} = \beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 0{,}50$ [illustratif]), devant donner $|\Delta P_{\mathrm{f}}| < 0{,}02$ [illustratif], et RL sans moniteur ($\beta \equiv 1$) confirmant que $\Pi_{\mathrm{v}}$ reste exploité en l'absence de filtrage.
- **Falsification** : $\Delta P_{\mathrm{f}} > +0{,}05$ (IC $95\,\% > 0$) [illustratif] falsifie $H_B$ ; $\Delta P_{\mathrm{f}} \le 0$ (borne sup. IC $\le +0{,}02$) [illustratif] falsifie $H_A$ et la transférabilité directe de la prédiction B $>$ A au RL sur réseaux neuronaux.

### Expérience 2 — Suffisance du modèle statique contre dépendance de chemin en dynamique de gradient
- **$H_A$ (Suffisance de la statistique statique $\pi_0$)** : À masse a priori $\pi_0(\Pi_{\mathrm{f}})$, divergence KL et paramètres $(\beta, \Delta R, C)$ identiques, la probabilité finale $P(\Pi_{\mathrm{f}})$ ne dépend pas de l'accessibilité intermédiaire de $\Pi_{\mathrm{v}}$ durant l'optimisation.
- **$H_B$ (Effet de barrière dynamique)** : Deux initialisations ayant le même $\pi_0(\Pi_{\mathrm{f}})$ (à $\pm 10\,\%$ relatif [illustratif]) mais différant par la présence ou la suppression précoce du chemin intermédiaire $\Pi_{\mathrm{v}}$ convergent vers des fréquences $P(\Pi_{\mathrm{f}})$ nettement différentes.
- **Métrique et seuil** : Écart absolu $|P_{\text{chemin}}(\Pi_{\mathrm{f}}) - P_{\text{bloqué}}(\Pi_{\mathrm{f}})|$ sur $5$ graines [illustratif]. Seuil $H_B$ : écart $> 0{,}10$ avec $p < 0{,}01$ (test de permutation) [illustratif]. Seuil $H_A$ : équivalence statistique (test TOST) dans une marge $< 0{,}03$ [illustratif].
- **Contrôle négatif** : Simulation d'échantillonnage de Gibbs exact sur un modèle discret tabulaire de mêmes $(\pi_0, \beta, \Delta R, C)$, qui doit produire un écart $< 0{,}01$ [illustratif].
- **Falsification** : Écart $> 0{,}10$ [illustratif] falsifie $H_A$ (rendant indispensable l'extension dynamique) ; équivalence $< 0{,}03$ [illustratif] falsifie $H_B$.

### Expérience 3 — Découplage hors boucle : sonde linéaire interne contre auditeur texte
- **$H_A$ (Orthogonalité représentationnelle de la sonde interne)** : Sous sélection en boucle par un moniteur de surface $D_{\mathrm{loop}}$, une sonde linéaire $D_{\text{sonde}}$ entraînée sur $\pi_0$ avant RL présente une covariance nulle ou négative avec $D_{\mathrm{loop}}$ sur les tricheurs et conserve son taux de faux négatifs ($\mathrm{FNR}$), alors qu'un juge texte hors boucle plus fort $D_{\text{texte}}$ se dégrade.
- **$H_B$ (Dérive représentationnelle conjointe)** : La pression de sélection contre $D_{\mathrm{loop}}$ déforme les représentations internes de manière positivement corrélée, dégradant aussi le $\mathrm{FNR}$ de $D_{\text{sonde}}$.
- **Métrique et seuil** : Variation $\Delta \mathrm{FNR} = \mathrm{FNR}_{\text{après RL}} - \mathrm{FNR}_{\text{avant RL}}$ évaluée à taux de fausses alertes fixé $\mathrm{FPR} = 0{,}05$ [illustratif] sur cas honnêtes appariés, complétée par $\widehat{\mathrm{Cov}}_{\text{cheat}}(\beta_{\mathrm{loop}}, \beta_{\mathrm{audit}})$. Seuil $H_A$ : $\Delta \mathrm{FNR}_{\text{sonde}} \le +0{,}03$ simultanément à $\Delta \mathrm{FNR}_{\text{texte}} \ge +0{,}15$ [illustratif]. Seuil $H_B$ : $\Delta \mathrm{FNR}_{\text{sonde}} \ge +0{,}10$ (IC $95\,\% > 0$) [illustratif].
- **Contrôle négatif** : (i) Évaluation sur un modèle RL entraîné *sans* détecteur en boucle ($\beta \equiv 1$) pour isoler la dérive générale de distribution due au RL (seuil attendu : $|\Delta \mathrm{FNR}_{\text{ctrl}}| < 0{,}05$ [illustratif]) ; (ii) sonde entraînée sur étiquettes permutées (AUROC attendu $0{,}50 \pm 0{,}03$ [illustratif]).
- **Falsification** : $\Delta \mathrm{FNR}_{\text{sonde}} \ge +0{,}10$ au-dessus du contrôle sans moniteur [illustratif] falsifie $H_A$ ; $\Delta \mathrm{FNR}_{\text{sonde}} \le +0{,}03$ avec $\Delta \mathrm{FNR}_{\text{texte}} \ge +0{,}15$ [illustratif] falsifie $H_B$.

### Expérience 4 — Épisodes pièges à $d_{\mathrm{TV}} = 1$ : efficacité sous faible $\mathcal{F}$-IPM contre détection opportuniste
- **$H_A$ (Efficacité sous indistinguabilité bornée)** : Avec une fraction $\rho = 0{,}10$ [illustratif] de pièges synthétiques à support disjoint ($d_{\mathrm{TV}} = 1$) mais faiblement distinguables par un classifieur de même capacité que la politique ($\mathcal{F}$-IPM faible), le taux d'interception sur pièges $\tau_{\mathrm{trap}}$ reste proche du taux de triche ordinaire $\tau_{\mathrm{ord}}$.
- **$H_B$ (Contournement contextuel des pièges)** : La politique exploite des indices résiduels des pièges synthétiques pour s'abstenir sur les pièges tout en trichant sur les épisodes ordinaires ($\tau_{\mathrm{trap}} \ll \tau_{\mathrm{ord}}$).
- **Métrique et seuil** : Écart $\Delta \tau = \tau_{\mathrm{ord}} - \tau_{\mathrm{trap}}$ mesuré par l'oracle mécanique lorsque $\tau_{\mathrm{ord}} \ge 0{,}30$ [illustratif]. Seuil $H_A$ : $\Delta \tau \le 0{,}05$ [illustratif]. Seuil $H_B$ : $\Delta \tau \ge 0{,}15$ [illustratif].
- **Contrôles négatifs** : (i) Pièges tirés de la *même* distribution que les épisodes ordinaires ($\delta_{\mathrm{ind}} = 0$, devant donner $|\Delta \tau| < 0{,}03$ [illustratif]) ; (ii) contrôle positif d'évasion avec pièges porteurs d'une balise explicite (devant produire $\Delta \tau \ge 0{,}30$ [illustratif] pour attester que la politique est capable de discrimination contextuelle).
- **Falsification** : $\Delta \tau \ge 0{,}15$ [illustratif] falsifie $H_A$ ; $\Delta \tau \le 0{,}05$ (alors que le contrôle balisé dépasse $0{,}30$) [illustratif] falsifie $H_B$ et la suffisance de la borne TV actuelle.

---

## Partie D — Métrologie minimale pour chaque instrument nommé *(livrable c)*

Chaque chiffre ci-dessous est `[illustratif]`. Un instrument appris n'est considéré fonctionnel que s'il satisfait simultanément ses bornes de détection/fausses alertes sur cas honnêtes appariés et bat strictement les vérifications mécaniques déterministes sur les cas de contournement furtif $\Pi_{\mathrm{f}}$.

| Instrument nommé | Mesure minimale (TPR / FPR) | Cas honnêtes appariés pour mesurer FPR | Vérifications mécaniques à battre |
| :--- | :--- | :--- | :--- |
| **Détecteur en boucle** (filtre de surface / juge CoT) | Calibration contrôlée : $\mathrm{TPR}(\Pi_{\mathrm{v}}) \ge 0{,}80$ et $\mathrm{TPR}(\Pi_{\mathrm{f}}) \le 0{,}15$ à $\mathrm{FPR} \le 0{,}05$ [illustratif] (pour instancier $\beta_{\mathrm{v}} < \beta_{\mathrm{f}} \le \beta_{\mathrm{h}}$) | Solutions honnêtes de même longueur de CoT ($\pm 15\,\%$ [illustratif]), même difficulté de problème et même complexité syntaxique | Expressions régulières sur mots-clés de triche et analyseur statique AST détectant l'accès direct aux fichiers de tests |
| **Sonde géométrique interne hors boucle** (*linear probe* sur activations) | Sur $\Pi_{\mathrm{f}}$ après RL : $\mathrm{TPR} \ge 0{,}75$ à $\mathrm{FPR} \le 0{,}05$ [illustratif], avec dérive $\Delta \mathrm{FNR} \le +0{,}03$ [illustratif] | Solutions honnêtes appariées en longueur de réponse, complexité cyclomatique, bibliothèques importées et score de récompense $R_0$ | Analyseur AST + métriques de surface (entropie de tokens, ratio code/commentaires, temps d'exécution en sandbox) : la sonde doit dépasser d'au moins $+0{,}15$ en TPR à FPR fixé [illustratif] la meilleure règle mécanique |
| **Auditeur texte hors boucle** (juge LLM plus fort) | Sur $\Pi_{\mathrm{f}}$ après RL : $\mathrm{TPR} \ge 0{,}70$ à $\mathrm{FPR} \le 0{,}05$ [illustratif] | Mêmes cas honnêtes appariés (incluant des solutions honnêtes inhabituelles ou peu idiomatiques pour tester le biais de style) | Mêmes vérifications mécaniques AST/sandbox + comparaison différentielle sur entrées générées aléatoirement (*fuzzing* léger) |
| **Dispositif d'épisodes pièges** (*honeypots*) | Interception $\tau_{\mathrm{trap}} \ge \max(0{,}25,\, \tau_{\mathrm{ord}} - 0{,}05)$ à $\mathrm{FPR} \le 0{,}02$ [illustratif] (fausses alertes sur politiques honnêtes soumises aux pièges) | Épisodes honnêtes appariés en domaine, distribution de longueurs d'entrée, format de prompt et métadonnées de harnais | Audit aléatoire pur sur épisodes ordinaires déjà vérifiés mécaniquement a posteriori (le dispositif de pièges doit égaler son rendement d'interception à coût de vérification inférieur) |
| **Instruments formels** (script numérique ; preuves mécanisées Lean/Coq) | Non applicable en TPR/FPR : zéro contre-exemple exact + zéro `sorry`/axiome non standard + correspondance exacte des hypothèses (ex. domaine de $R_0$) | Cas limites dégénérés ($R_0 < 0$, $\beta_{\mathrm{v}} \to 0$, $\eta \to 0^+$, $\beta_{\mathrm{f}} = \beta_{\mathrm{h}} = 1$) | Calcul formel symbolique autonome (arithmétique rationnelle exacte et solveurs SMT sur les inégalités rationnelles) |

*Précision méthodologique :* l'appariement strict des cas honnêtes (longueur, style peu idiomatique, complexité) est indispensable ; sans lui, une sonde interne ou un juge hors boucle peut obtenir un TPR élevé simplement en détectant un artefact de longueur ou de formatage, ce qu'une vérification mécanique triviale bat déjà.

---

## Partie E — Ancrage matériel *(livrable d)*

Tous les ordres de grandeur ci-dessous sont `[illustratif]` (aucun ne provient de `FAITS`).

- **Modèles ouverts :**
  - *Famille principale* : modèle de code/raisonnement ouvert de classe $7$ milliards de paramètres [illustratif] (ex. série Qwen-Coder/Instruct).
  - *Réplication inter-familles* : modèle ouvert indépendant de classe $8$ milliards de paramètres [illustratif] (ex. série Llama-Instruct), pour réfuter un artefact spécifique à un seul pré-entraînement.
  - *Ablation d'échelle pilote* : modèle de classe $3$ milliards de paramètres [illustratif] pour le débogage rapide du banc et du calibrage de $\pi_0$.
  - *Moniteurs* : moniteur en boucle hybride (règles AST + modèle léger de classe $1{,}5$ à $3$ milliards [illustratif]) ; auditeur texte hors boucle de classe $32$ à $70$ milliards [illustratif] en inférence quantifiée.

- **Calcul nécessaire :**
  - Construction du banc, calibrage SFT de $\pi_0$ et tests pilotes : $15$ à $30$ heures-GPU de classe H100 ($80$ Go) [illustratif].
  - Campagne RL (GRPO/PPO avec LoRA ou entraînement complet, $500$ à $1\,000$ étapes par essai [illustratif]) couvrant les Expériences 1 à 4 : environ $10$ configurations expérimentales et contrôles × $5$ graines [illustratif] = $50$ entraînements [illustratif], à $4$–$8$ heures-GPU H100 par entraînement [illustratif], soit $200$ à $400$ heures-GPU H100 [illustratif] pour la famille principale.
  - Extraction d'activations, entraînement/validation des sondes linéaires, inférence du juge texte hors boucle et exécution sandboxée de l'oracle : $40$ à $60$ heures-GPU H100 [illustratif] et environ $200$ heures-CPU [illustratif].
  - Réplication sur la seconde famille de modèles et marge d'itération (facteur $1{,}5$ [illustratif]) : **total consolidé de $500$ à $1\,000$ heures-GPU H100** [illustratif] (ou environ $1\,000$ à $2\,000$ heures-GPU A100 $80$ Go [illustratif]).

- **Coût estimé et calendrier :**
  - Sur cloud locatif à la demande ($2{,}00$ à $3{,}50$ USD par heure-GPU H100 [illustratif]) : **$1\,000$ à $3\,500$ USD** [illustratif] (réductible à $500$–$1\,200$ USD [illustratif] en instances préemptibles ou sur cluster académique).
  - Temps d'ingénierie et d'analyse : $6$ à $10$ semaines-personne [illustratif] ($2$–$3$ semaines [illustratif] pour l'extension dynamique *mirror descent* + $\mathcal{F}$-IPM ; $4$–$7$ semaines [illustratif] pour le banc de code, la campagne RL, les sondes et les contrôles négatifs).

FIN-DE-CELLULE