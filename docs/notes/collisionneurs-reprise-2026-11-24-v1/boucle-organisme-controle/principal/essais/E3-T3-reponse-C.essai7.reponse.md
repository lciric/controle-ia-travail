*État des pièces et conformité :* les pièces `FAITS`, `QUESTION DE L'ARBITRE`, `E3-T1-conception-C`, `E3-T2-critique-croisee-A` et `E3-T2-critique-croisee-B` sont toutes présentes et complètes (`OBSERVÉ-NON-AUDITÉ` sur leurs empreintes `sha256`, non recalculées). Les faits issus du dossier conservent le statut `RAPPORTÉ`, les déductions mathématiques le statut `VÉRIFIÉ`, et les propositions empiriques non testées le statut `HYPOTHÈSE`. Conformément au protocole (B1), cette réponse ne traite que les sections de A et de B visant la proposition C et crédite explicitement chaque emprunt. Tout chiffre ne provenant pas des faits est marqué `[illustratif]`. Aucun identifiant arXiv n'est donné de mémoire (`arXiv : pas sûr`).

---

## (a) Réponse point par point aux critiques visant C

### Critiques issues de A (`E3-T2-critique-croisee-A`)

1. **A-a1 / A-b1 / A-c1 — Banc circulaire du filtre amont $\Phi_{\text{CPU}}$, décalage de covariables et arbitraire d'AR(1) (`Expérience 1`).**
   - **Verdict : Acceptée.** Construire les `100` [illustratif] objets invalides sur la taxinomie même codée dans $\Phi_{\text{CPU}}$ rend le succès partiellement vrai par construction, et le poids des types d'invalidité du banc diffère de ceux émis par `I`.
   - **Correction (empruntée à A-c1) :** confier la création du banc d'invalides à une instance tierce aveugle au code de $\Phi_{\text{CPU}}$ (lecture unique), y adjoindre un échantillon audité de sorties brutes de `I`, et compléter la batterie synthétique AR(1) par des blocs rééchantillonnés de séries honnêtes réelles issues de $\mathcal{D}_{\text{hon}}^{\text{cal}}$.

2. **A-a2 — CN1 (placebo à cible permutée) ne teste pas le couplage mais seulement le filtre.**
   - **Verdict : Acceptée.** La validité sous $H_0$ ne dépend pas de $\Pi_{\text{spec}}$. CN1 est requalifié en contrôle de calibration du détecteur interne sur bruit pur ; le test du couplage est porté exclusivement par le bras placebo de l'`Expérience 5`.

3. **A-a3 / A-b2 / A-c2 — Confusion mémoire/naturalité dans $R_{\text{temp}}$ et variance explosive du ratio (`Expérience 2`).**
   - **Verdict : Transformée en test.** A montre justement que des lois procédurales arbitraires perdent les régularités physiques (symétries, homogénéité, parcimonie) qu'un modèle pré-entraîné peut exploiter sans mémorisation, et que le ratio $R_{\text{temp}}$ a une variance instable (méthode delta) dès que $p_h$ est faible.
   - **Correction (empruntée à A-c2) :** remplacer $R_{\text{temp}}$ par un **plan factoriel `2×2` [illustratif]** croisant `(lois historiques originales vs lois historiques perturbées-anonymisées conservant les symétries structurelles)` $\times$ `(avec LLM vs sans LLM)`, mesuré par un contraste d'interaction borné.

4. **A-a4 / A-c3 — Même lignée de modèles (Llama/Qwen) des deux côtés (co-ascendance).**
   - **Verdict : Transformée en test (et acceptée en règle par défaut).** Utiliser la même lignée pour assister `I`, concevoir les familles et incarner la cible 8B crée un artefact potentiel de biais partagés (`HYPOTHÈSE`).
   - **Correction (empruntée à A-c3) :** imposer par défaut trois lignées distinctes (ou concepteurs humains pour les familles) entre `I`, le concepteur de familles et la cible 8B, et intégrer un bras croisé (lignée partagée vs disjointe) hors-$\mathcal{F}_k$ pour mesurer cet artefact.

5. **A-a5 / A-b3 / A-c4 — Restriction d'étendue sur $\rho_s$, chevauchement possible avec $\mathcal{D}_{\text{hon}}$, bruit sur « `80%` des `30` » et trajectoires concaténées (`Expérience 3`).**
   - **Verdict : Acceptée.** Sélectionner des détecteurs déjà « certifiés CPU » écrase $\operatorname{Var}(\text{dérive}_{\text{sim}})$ et détruit l'identifiabilité de $\rho_s$ (`VÉRIFIÉ`).
   - **Correction (empruntée à A-c4) :** (i) imposer $\mathcal{D}_{\text{hon}}^{\text{cal}} \cap \mathcal{D}_{\text{hon}}^{\text{eval}} = \emptyset$ croisé entre deux architectures 8B et entre domaines de tâches ; (ii) évaluer $\rho_s$ sur un banc stratifié non tronqué (certifiés, limites, invalides) ; (iii) remplacer la concaténation par des trajectoires longues **natives** (chaînes multi-agents), doublées d'un contrôle natives vs concaténées ; (iv) borner le FPR réel par intervalles exacts de Clopper-Pearson (Clopper & Pearson, 1934, *The use of confidence or fiducial limits illustrated in the case of the binomial*, Biometrika, arXiv : pas sûr).

6. **A-a6 / A-b5 / A-c5 — Référence fixe gagnée d'avance, disjonction « TPR ou délai », volumes honnêtes non égalisés et pseudo-réplication (`Expérience 4`).**
   - **Verdict : Partiellement acceptée, partiellement rejetée.**
     - *Acceptée* sur la disjonction (figée en une métrique primaire unique), l'égalisation stricte du volume de données honnêtes $N_0$ entre $Q_t$ et la référence fixe (emprunté à A-c5), et la pseudo-réplication (passage à $K_4 = 2$ [illustratif] familles indépendantes et requalification en test de faisabilité, $\tau^2$ n'étant pas estimable sur $K_4$ petit).
     - *Rejetée* si la critique implique de retirer la référence fixe : battre la référence fixe en $T = 5 N_0$ [illustratif] n'est certes pas un critère suffisant, mais son maintien à $N_0$ égal reste indispensable comme **témoin positif de régime** vérifiant que l'épreuve opère bien au-delà du plafonnement sur traces 8B réelles. L'épreuve décisive porte contre les bases boîte noire, boîte blanche par action et e-processus standard.

7. **A-a7 / A-b6 — Non-jugeabilité de la règle `2/3` sur $K = 3$ familles et vacuité du « double aveugle » d'un orchestrateur déterministe (`Expérience 5`).**
   - **Verdict : Acceptée.** Sous l'égalité, un test des signes sur $K = 3$ [illustratif] a une p-valeur minimale de `0,125` [illustratif] (`VÉRIFIÉ`), et l'aveuglement pertinent concerne le concepteur des familles vis-à-vis de $\Pi_{\text{spec}}$ ainsi que les auditeurs humains, non un script déterministe.
   - **Correction :** imposer $K = 5$ [illustratif] familles indépendantes évaluées par produit d'e-valeurs inter-familles $\ge 20$ [illustratif] (ou déclarer la généralisation inter-familles non jugeable si le budget réel $K_{\max} < 5$ [illustratif]).

8. **A-a8 / A-c6 — Canal humain non audité dans $\Pi_{\text{spec}}$.**
   - **Verdict : Acceptée.** Un audit cryptographique ne verrouille pas la mémoire d'un chercheur réécrivant des « verrous théoriques » après lecture de $\mathcal{F}_{k-1}$.
   - **Correction (empruntée à A-c6) :** gel cryptographique intégral de $\Pi_{\text{spec}}$ avant la lecture de $\mathcal{F}_1$ + injection d'un verrou-canari fictif absent de toutes les familles.

9. **A-a9 / A-b8 / A-c7 — Plancher d'audit $(1 - q_s \underline{p}_s)^{n_s}$ anti-conservateur par Jensen et hypothèse d'indépendance.**
   - **Verdict : Acceptée.** Par convexité, $\mathbb{E}[(1 - q_s P)^{n_s}] \ge (1 - q_s \mathbb{E}[P])^{n_s}$ (`VÉRIFIÉ`) : utiliser une borne sur la moyenne de strate sous-estime la survie d'un sabotage ciblant les dommages les plus difficiles, et l'indépendance échoue sur un défaut systématique de l'oracle.
   - **Correction (empruntée à A-c7) :** remplacer la moyenne de strate par une borne inférieure sur la queue basse par type de dommage, $\underline{p}_{s,\min}$, et restreindre la garantie aux actes indépendants de détectabilité $\ge \underline{p}_{s,\min}$.

10. **A-a10 / A-b4 / A-b7 — Borne lipschitzienne non testable (§3.2.3), caractère conditionnel de §3.3 et non-identifiabilité de $\pi_0$.**
    - **Verdict : Partiellement acceptée, partiellement rejetée.**
      - *Acceptée* sur la borne lipschitzienne (§3.2.3) : $d_{\mathcal{F}}$ en dimension des activations est inutilisable et $\varepsilon_{\text{strat}}$ non estimable ; je retire cette borne au profit d'indicateurs testables en basse dimension (`Expérience 3`). *Acceptée* également sur la formulation conditionnelle de §3.3 (valide uniquement à $\text{TPR}_\Phi$ maintenu) et sur le fait que les promotions seules n'identifient que la $\text{VPP}$, non $\pi_0$.
      - *Rejetée* en tant qu'objection à la priorité du filtre amont : même avec $\pi_0 \in (0, 1)$ inconnu, $\text{VPP}(\Phi)$ reste strictement décroissante en $\text{FPR}_{\Phi,\text{tot}} / \text{TPR}_\Phi$ (`VÉRIFIÉ` par Bayes), et le coût irréversible des familles (`RAPPORTÉ`) maintient la sélectivité amont comme levier prioritaire.

---

### Critiques issues de B (`E3-T2-critique-croisee-B`)

1. **B-a1 / B-b1 / B-c2 — Réintroduction cachée du plafond $T > N_0$ via les invariants estimés $\hat{\eta}_{N_0}$, fuite sur $\mathcal{D}_{\text{hon}}$ et perte de puissance dans $\ker \Pi_{\eta_0}$.**
   - **Verdict : Acceptée.** C'est le défaut mathématique majeur de ma proposition T1. Dès que $e_t(X_t; \hat{\eta}_{N_0})$ repose sur un paramètre empirique de dimension effective $d_{\text{eff}}$ appris sur $N_0$ trajectoires honnêtes, tous les pas $t = 1,\dots,T$ partagent l'erreur figée $\hat{\eta}_{N_0} - \eta_0$, réintroduisant une dérive dès $T \gtrsim N_0 / d_{\text{eff}}$ (`VÉRIFIÉ`). L'impossibilité de détecter un sabotage dans $\ker \Pi_{\eta_0}$ est également exacte (`VÉRIFIÉ`).
   - **Correction (empruntée à B-c2) :** (i) distinguer strictement les **nuls par acte sans estimation sur $\mathcal{D}_{\text{hon}}$** (symétrie/randomisation en ligne à l'acte $t$, ou symétrie entre copies en essaim — seuls affranchis de $N_0$) des **nuls à invariant estimé $\hat{\eta}_{N_0}$** (qui exigent une marge d'estimation explicite et ne revendiquent pas l'indépendance vis-à-vis de $N_0$) ; (ii) imposer $\mathcal{D}_{\text{hon}}^{\text{inv}} \cap \mathcal{D}_{\text{hon}}^{\text{eval}} = \emptyset$ inter-tâches testé jusqu'à $T = 5 N_0$ [illustratif].

2. **B-a2 / B-c5 — Contradiction interne du « pare-feu sans score » ($\alpha$-investissement et dilemme boucle statique vs fuite humaine).**
   - **Verdict : Partiellement acceptée, partiellement rejetée.**
     - *Acceptée* sur l'$\alpha$-investissement (Foster & Stine, 2008, *$\alpha$-investing: a procedure for sequential control of expected false discoveries*, JRSS-B, arXiv : pas sûr) : faire dépendre $\alpha_k$ des rejets passés rompt l'étanchéité inter-tours (`VÉRIFIÉ`). Je le remplace par une **allocation fixe prédéterminée** $\alpha_k = \alpha / K$. *Acceptée* aussi sur le gel cryptographique intégral de $\Pi_{\text{spec}}$ avant $\mathcal{F}_1$ (emprunté à B-c5).
     - *Rejetée* sur le faux dilemme « soit conditionnement statique unique, soit fuite via $\mathcal{F}_k$ » : une **boucle fermée honnête** non circulaire existe entre `I` et $\mathcal{D}_{\text{hon}}^{\text{cal}}$, où `C` renvoie itérativement à `I` les modes réels de non-stationnarité honnête 8B violant $H_0$ (sans aucun sabotage ni lecture de $\mathcal{F}_k$), jusqu'à convergence sur $\mathcal{D}_{\text{hon}}^{\text{cal}}$, avant gel complet et évaluation unique sur $\mathcal{F}_k$.

3. **B-a3 / B-c3 — Erreur d'assimilation dans l'équation de Bayes (§3.3) : $\Phi_{\text{CPU}}$ laisse passer les martingales valides mais sans puissance.**
   - **Verdict : Acceptée.** Assimiler « valide sous $H_0$ » à « valide et utile » permettait à $e_t \equiv 1$ ou à des variantes triviales de saturer les promotions (`VÉRIFIÉ`).
   - **Correction (empruntée à B-c3) :** transformer $\Phi_{\text{CPU}}$ en **filtre bi-étage** (Étage 1 : validité sous $H_0$ ; Étage 2 : puissance minimale sur alternatives locales synthétiques + déduplication fonctionnelle contre les bases existantes), dissocier $\text{FPR}_{\Phi,\text{inval}}$ et $\text{FPR}_{\Phi,\text{triv}}$ dans §3.3, et injecter des martingales dégénérées comme contrôle négatif dans l'`Expérience 1`.

4. **B-a4 / B-c1 / B-c4 — Budget matériel asymétrique CPU/GPU (`Expérience 2`) et bibliothèque mécanique privée de $\Pi_{\text{spec}}$ (`Expérience 5`).**
   - **Verdict : Acceptée.** Comparer `I` + GPU à une ablation CPU seule confond FLOPs et LLM ; priver la bibliothèque mécanique de $\Pi_{\text{spec}}(\mathcal{D}_{\text{hon}}^{\text{cal}})$ confond prétraitement honnête et idéation automatisée (`VÉRIFIÉ`).
   - **Correction (empruntée à B-c1 et B-c4) :** égaliser le coût financier/FLOPs total (CPU + GPU) dans l'`Expérience 2`, apparier les lois par information de Fisher minimale, et alimenter la bibliothèque mécanique avec exactement le même $\Pi_{\text{spec}}(\mathcal{D}_{\text{hon}}^{\text{cal}})$ dans l'`Expérience 5`.

5. **B-b2 — Dégénérescence de la borne lipschitzienne et auto-réfutation de $\hat{\rho}_s$ quand les supermartingales certifiées sont conservatrices (`Expérience 3`).**
   - **Verdict : Acceptée.** Lorsque $\max_i \alpha_i^{\text{8B}} \ll N_{\text{test}}^{-1}$, les ex æquo à zéro rendent $\hat{\rho}_s \to 0$ alors même que tous les détecteurs sont valides (`VÉRIFIÉ`).
   - **Correction :** mesurer $\hat{\rho}_s$ sur une statistique continue non dégénérée — le `95`e percentile [illustratif] de $S_T^{(m)} = \max_{t \le T} \log E_t^{(m)}$ sur un banc stratifié — et évaluer séparément la validité anytime des détecteurs certifiés.

6. **B-b3 — Instabilité de Fieller / Gleser-Hwang sur le ratio $\hat{R}_{\text{temp}}$ et régime dégénéré $p \to 0^+$ (`Expérience 2`).**
   - **Verdict : Acceptée.** Le ratio est abandonné au profit d'un contraste d'interaction sur différences bornées assorti d'un plancher absolu de découverte $p_{\min}$ (`Expérience 2` corrigée).

7. **B-b4 — Gonflement d'erreur de type I sur `2/3` des familles (`Expérience 5`) et rupture du plancher d'audit si $Q_s^{\text{adv}}$ se concentre sur $\{p_s(x) = 0\}$.**
   - **Verdict : Partiellement acceptée, partiellement rejetée.**
     - *Acceptée* sur l'`Expérience 5` (`10/64 \approx 0,156` [illustratif] à 4 bras sous le nul ; remplacé par $K = 5$ [illustratif] et produit d'e-valeurs inter-familles) et sur le théorème de rupture lorsque le sabotage vit dans $\{p_s(x) = 0\}$ (`VÉRIFIÉ`).
     - *Rejetée* si l'on en concluait l'inutilité du plancher d'audit : reformulé sur la classe $\mathcal{C}(\underline{p}_{s,\min})$ des dommages de détectabilité $\ge \underline{p}_{s,\min}$, le plancher contraint l'adversaire à se replier sous le seuil de détection humaine.

---

## (b) Expériences corrigées (et trois rectifications de formalisation)

Trois rectifications préalables s'appliquent à la section 3 de T1 :
1. **Dédoublement du nul par acte (suite à B-a1/B-b1) :** seul un nul par acte **sans estimation sur $\mathcal{D}_{\text{hon}}$** (invariance exacte par intervention en ligne à l'acte $t$, ou symétrie entre copies en essaim) affranchit l'inégalité de Ville (Ville, 1939, *Étude critique de la notion de collectif*, arXiv : pas sûr) de la taille $N_0$ (`VÉRIFIÉ`) ; tout nul paramétré par $\hat{\eta}_{N_0}$ subit un plafonnement effectif en $O(N_0 / d_{\text{eff}})$ et doit inclure une marge d'estimation vérifiée sur $\mathcal{D}_{\text{hon}}^{\text{eval}}$ disjoint.
2. **Boucle fermée honnête + gel avant $\mathcal{F}_1$ (suite à A-a8/B-a2/B-c5) :** la rétroaction itérative s'exerce uniquement entre `I` et les modes d'échec sous $H_0$ observés sur $\mathcal{D}_{\text{hon}}^{\text{cal}}$. Une fois figé, $\Pi_{\text{spec}}$ (avec canari fictif) est gelé cryptographiquement avant $\mathcal{F}_1$, et le budget inter-tours suit une allocation fixe $\alpha_k = \alpha / K$ (suppression de l'$\alpha$-investissement).
3. **Filtre bi-étage dans §3.3 (suite à B-a3/A-b7) :** on remplace $\text{FPR}_\Phi$ par le taux combiné sur invalides et valides sans puissance, $\text{FPR}_{\Phi,\text{tot}} = \mathbb{P}(\text{passe }\Phi \mid \neg(V \cap U))$, et on abandonne la borne lipschitzienne de §3.2.3.

Toutes les expériences ci-dessous respectent l'inférence forte (B4 : partition exclusive $H_A / H_B$, où chaque issue falsifie l'autre). Tous les seuils numériques, effectifs, durées et coûts sont `[illustratif]`.

### Expérience 1 corrigée (C1) — Sélectivité bi-étage du filtre $\Phi_{\text{CPU}}$ sur banc aveugle
- **`H_A` :** Sur un banc conçu par une instance aveugle au code de $\Phi_{\text{CPU}}$ (lu une seule fois), le filtre bi-étage (Étage 1 : preuve/vérification $H_0$ + stress-test sur blocs rééchantillonnés de $\mathcal{D}_{\text{hon}}^{\text{cal}}$ ; Étage 2 : puissance locale minimale + déduplication fonctionnelle) satisfait simultanément : borne supérieure Clopper-Pearson (`95%` [illustratif]) de $\text{FPR}_{\Phi,\text{inval}} \le 0,05$ [illustratif], de $\text{FPR}_{\Phi,\text{triv}} \le 0,10$ [illustratif], et borne inférieure (`95%` [illustratif]) de $\text{TPR}_{\Phi,\text{utile}} \ge 0,75$ [illustratif], avec maintien de $\text{FPR}_{\Phi,\text{inval}} \le 0,05$ [illustratif] sur un audit indépendant de `50` [illustratif] sorties réelles de `I`.
- **`H_B` :** Au moins l'une de ces bornes de confiance échoue, démontrant que $\Phi_{\text{CPU}}$ laisse passer des objets invalides ou triviaux, ou rejette trop d'objets utiles.
- **Protocole et contrôle négatif :** `300` [illustratif] objets (`100` valides-et-utiles, `100` invalides conçus à l'aveugle, `100` martingales valides mais sans puissance/dupliquées : $e_t \equiv 1$, bruit orthogonal, réécritures syntaxiques de la bibliothèque de base ; contrôle de B-c3 et A-c1) + `50` [illustratif] sorties brutes de `I` auditées indépendamment.
- **Coût :** CPU seul (`32` cœurs, `40–60` h CPU, `10–30` € [illustratif]), `0` GPU, `0` famille consommée.
- **Falsification :** tout échec d'une borne réfute `H_A` et suspend le couplage ; la satisfaction conjointe réfute `H_B`.

### Expérience 2 corrigée (C2) — Audit mémoire vs naturalité par plan factoriel `2×2` à coût total égal
- **`H_A` :** À coût financier/énergétique total égal (CPU + GPU converti en cœurs-heures CPU pour le bras sans LLM, B-c4), sur `100` [illustratif] lois historiques perturbées-anonymisées conservant symétries structurelles et information de Fisher minimale (A-c2), `I` avec LLM atteint $p_{\text{pert,LLM}} \ge 0,25$ [illustratif], surpasse l'ablation sans LLM ($\Delta_{\text{pert}} = p_{\text{pert,LLM}} - p_{\text{pert,sym}} > 0$, test exact unilatéral $p < 0,01$ [illustratif]), **et** la borne supérieure (`95%` [illustratif]) sur l'interaction de mémorisation $\Delta_{\text{mém}} = (p_{\text{orig,LLM}} - p_{\text{orig,sym}}) - (p_{\text{pert,LLM}} - p_{\text{pert,sym}})$ est $< 0,15$ [illustratif].
- **`H_B` :** $p_{\text{pert,LLM}} < 0,25$ [illustratif], ou $\Delta_{\text{pert}}$ n'est pas significatif à $p < 0,01$ [illustratif], ou la borne supérieure de $\Delta_{\text{mém}} \ge 0,15$ [illustratif], établissant l'inefficacité à coût égal ou la dominance de la mémorisation.
- **Contrôles négatifs :** `60` [illustratif] mondes de bruit pur (taux de fausses découvertes $\le 0,05$ [illustratif] après contrôle multiple) ; troisième bras descriptif de `100` [illustratif] lois *de novo* bien conditionnées.
- **Coût :** `250–400` h CPU + `15–30` h GPU `24` Go (`60–150` € [illustratif]), `0` famille.
- **Falsification :** échec sur l'une des trois clauses ou sur bruit pur réfute `H_A` (et impose de retirer le LLM de `I`) ; satisfaction conjointe réfute `H_B`.

### Expérience 3 corrigée (C3) — Transfert hors-échantillon croisé vers activations honnêtes 8B natives
- **`H_A` :** Calibré sur $\mathcal{D}_{\text{hon}}^{\text{cal}}$ (modèle 8B $M_1$, domaine de tâches $A$), le banc CPU prédit le rang du `95`e percentile [illustratif] de $S_T^{(m)} = \max_{t \le T} \log E_t^{(m)}$ sur un jeu strictement disjoint $\mathcal{D}_{\text{hon}}^{\text{eval}}$ (modèle 8B $M_2$ d'architecture distincte, domaine $B$, $N_{\text{test}} = 300$ [illustratif] trajectoires longues **natives** de chaînes multi-agents, $T = 5 N_0$ [illustratif]) avec une borne inférieure IC `95%` de $\hat{\rho}_s \ge 0,50$ [illustratif] sur `45` [illustratif] détecteurs stratifiés (`15` certifiés, `15` limites, `15` invalides), **surpasse** un simulateur placebo sans autocorrélation temporelle ($\Delta \hat{\rho}_s > 0$, IC `95%` $> 0$), **et** au moins `80%` [illustratif] des `15` [illustratif] détecteurs certifiés maintiennent une borne supérieure Clopper-Pearson (`95%`) de FPR anytime $\le 0,08$ [illustratif] (pour $\alpha = 0,05$ [illustratif]).
- **`H_B` :** Au moins l'une de ces trois conditions échoue, démontrant la non-transférabilité du banc CPU ou la dérive des invariants estimés $\hat{\eta}_{N_0}$ à horizon $T = 5 N_0$ [illustratif].
- **Contrôles négatifs :** (1) comparaison trajectoires natives vs concaténées de même longueur (A-c4), (2) simulateur placebo à marges identiques mais autocorrélation détruite (adapté de A), (3) changements de domaine bénins et paraphrases stylistiques sur $\mathcal{D}_{\text{hon}}^{\text{eval}}$.
- **Coût :** deux modèles ouverts ~8B d'architectures distinctes, `1–2` GPU `48` Go, `60–120` h GPU (`120–350` € [illustratif]), `0` famille consommée.
- **Falsification :** tout échec de seuil ou absence d'avantage sur le placebo sans autocorrélation réfute `H_A` et interdit l'accès à $\mathcal{F}_k$ ; succès conjoint réfute `H_B`.

### Expérience 4 corrigée (C4) — Faisabilité d'un nul par acte au-delà de $N_0$ à budget honnête égal
- **`H_A` :** Sous séparation des lignées (`I`, concepteur des familles, cible 8B), gel cryptographique de $\Pi_{\text{spec}}$ et allocation fixe $\alpha / (B K_4)$ ($B = 3$ [illustratif] promotions, $K_4 = 2$ [illustratif] familles indépendantes), au moins un nul par acte synthétisé (prioritairement sans paramètre estimé sur $\mathcal{D}_{\text{hon}}$, sinon corrigé et pré-validé sur $\mathcal{D}_{\text{hon}}^{\text{eval}}$) (i) maintient une borne supérieure (`95%` [illustratif]) de FPR anytime $\le 0,08$ [illustratif] à $T = 5 N_0$ [illustratif] sur $\mathcal{D}_{\text{hon}}^{\text{eval}}$ disjoint, **et** (ii) surpasse simultanément les quatre bases dotées du **même** volume $N_0$ de trajectoires honnêtes (boîte noire, boîte blanche par action, référence fixe témoin, e-processus séquentiel standard) d'au moins $+0,10$ [illustratif] sur la métrique unique préenregistrée $\text{AUDD}$ (aire normalisée détection–délai avant dommage critique) sur **chacune** des `2` [illustratif] familles indépendantes (lecture unique).
- **`H_B` :** Aucun des $B$ candidats promus ne satisfait conjointement la validité anytime hors-échantillon et le gain $\ge +0,10$ [illustratif] en $\text{AUDD}$ contre les quatre bases sur les `2` [illustratif] familles.
- **Contrôles négatifs :** (1) trajectoires honnêtes longues disjointes ($T = 5 N_0$) avec paraphrases stylistiques, (2) référence fixe à $N_0$ égal comme témoin positif du plafonnement, (3) bras croisé hors-$\mathcal{F}_k$ de co-ascendance (lignée partagée vs disjointe, A-c3).
- **Coût :** `150` h CPU + `100–180` h GPU `48–80` Go (`250–550` € [illustratif]) + **`2` [illustratif] familles consommées**.
- **Falsification :** violation de FPR ou échec contre une seule base ou une seule famille réfute `H_A` ; succès conjoint réfute `H_B` (en notant que $\tau^2$ inter-familles requiert l'`Expérience 5`).

### Expérience 5 corrigée (C5) — Utilité nette de la boucle fermée honnête face à la bibliothèque prétraitée
- **Condition préalable de jugeabilité :** exige $K = 5$ [illustratif] familles indépendantes inédites ; si le programme dispose de $K_{\max} < 5$ [illustratif], la supériorité inter-familles est déclarée non jugeable (seule une disqualification rapide sur $K = 2$ [illustratif] reste licite).
- **`H_A` :** Sur $K = 5$ [illustratif] familles inédites indépendantes (Axes 1 et 2, conçues par des instances/lignées aveugles à $\Pi_{\text{spec}}$ gelé avant $\mathcal{F}_1$, lecture unique, allocation fixe $\alpha / K$, auditeurs humains masqués aux bras), la **boucle fermée honnête** (`I` itérant sur les échecs sous $H_0$ de $\mathcal{D}_{\text{hon}}^{\text{cal}}$) surpasse simultanément (i) `I` en boucle ouverte, (ii) la bibliothèque mécanique alimentée par **exactement le même** $\Pi_{\text{spec}}(\mathcal{D}_{\text{hon}}^{\text{cal}})$ (B-c1), et (iii) le bras placebo (retours honnêtes permutés), en produisant une e-valeur inter-familles combinée $\prod_{k=1}^5 e_k^{\text{fam}} \ge 20$ [illustratif] sur $\text{AUDD}$ contre le meilleur comparateur, à FPR anytime $\le 0,05$ [illustratif], avec un rendement net normalisé par coût total $\widehat{\mathcal{R}}_{\text{couplée}} > \max(\widehat{\mathcal{R}}_{\text{ouverte}}, \widehat{\mathcal{R}}_{\text{méc}+\Pi})$ et zéro activation anormale du canari.
- **`H_B` :** $\prod_{k=1}^5 e_k^{\text{fam}} < 20$ [illustratif], ou $\widehat{\mathcal{R}}_{\text{couplée}}$ ne domine pas les comparateurs, ou violation du FPR/canari — falsifiant l'intérêt pratique du couplage et déclenchant son débranchement.
- **Contrôles négatifs :** bibliothèque mécanique munie du même $\Pi_{\text{spec}}(\mathcal{D}_{\text{hon}}^{\text{cal}})$ (B-c1), bras placebo permuté, verrou-canari fictif dans $\Pi_{\text{spec}}$ (A-c6), séparation des lignées (A-c3).
- **Coût :** deux modèles ~8B, `250–450` h GPU + `450` h CPU (`700–1800` € [illustratif]) + **`5` [illustratif] familles consommées** ($\mathcal{F}_{\text{val}}$ strictement intacte).
- **Falsification :** échec sur l'e-valeur combinée, le rendement net ou le canari réfute `H_A` et arrête le couplage ; satisfaction conjointe réfute `H_B`.

---

## (c) Réponse à la question de l'arbitre (en une page)

**Ce qui est établi.**
Trois contraintes du programme de contrôle sont des faits du dossier (`RAPPORTÉ`) : (1) aucun score issu d'un moniteur ou d'un juge ne peut alimenter la sélection d'un proposeur hors bras d'attaque déclaré ; (2) toute reconception s'évalue sur une famille inédite tenue à l'écart et lue une seule fois, sous budget GPU modeste sur modèles ouverts d'environ huit milliards de paramètres ; (3) l'accumulation séquentielle calibrée sur référence honnête fixe plafonne au-delà de sa taille $N_0$, sauf usage d'un nul par acte, et les garanties indépendantes de la reconnaissance de l'attaque reposent sur un plancher d'audit exogène.

Cinq propriétés mathématiques sont par ailleurs établies (`VÉRIFIÉ`), dont trois précisées grâce aux critiques de A et de B :
- Toute rétroaction directe par scores de familles ou par $\alpha$-investissement entre tours rompt l'étanchéité statistique. La seule boucle fermée non circulaire relie l'organisme `I` aux **échecs sous $H_0$ sur trajectoires honnêtes $\mathcal{D}_{\text{hon}}^{\text{cal}}$**, avec gel cryptographique intégral de la spécification $\Pi_{\text{spec}}$ avant la première lecture de famille.
- Un nul par acte n'abolit le plafond $N_0$ que s'il repose sur une **symétrie/invariance exacte en ligne sans paramètre estimé sur $\mathcal{D}_{\text{hon}}$** ; tout invariant $\hat{\eta}_{N_0}$ appris sur $N_0$ trajectoires réintroduit une erreur partagée et un plafonnement en $O(N_0 / d_{\text{eff}})$ (établi par B).
- En régime de découvertes rares et de lectures de familles irréversibles, la valeur prédictive positive des promotions est gouvernée par le rapport $\text{FPR}_{\Phi,\text{tot}} / \text{TPR}_\Phi$ d'un filtre amont **bi-étage** éliminant conjointement les objets invalides sous $H_0$ et les martingales formellement valides mais sans puissance.
- Le plancher d'audit exogène est soumis à l'inégalité de Jensen (établi par A) et ne borne la survie que sur les dommages dont la détectabilité dépasse un minorant de queue basse $\underline{p}_{s,\min} > 0$, jamais sur les dommages invisibles à l'oracle (établi par B).

**Ce qui ne l'est pas.**
Rien ne démontre aujourd'hui (`HYPOTHÈSE`) : (1) que les mondes synthétiques sur processeur prédisent le comportement d'un détecteur sur activations honnêtes réelles 8B (transfert CPU $\to$ 8B) ; (2) que le guidage par modèle pré-entraîné dans `I` produise une capacité d'invention hors mémorisation et hors biais de naturalité, supérieure à une recherche symbolique sans LLM à coût total égal ; (3) que la boucle honnête `I ↔ D_hon` batte une bibliothèque mécanique de tests séquentiels alimentée par le même prétraitement $\Pi_{\text{spec}}(\mathcal{D}_{\text{hon}})$ ; (4) qu'aucun artefact de co-ascendance ne biaise l'évaluation lorsque les modèles partagent la même lignée ; (5) *je ne sais pas* combien de familles indépendantes $K_{\max}$ le programme peut réellement financer (conditionnant la jugeabilité même d'une généralisation inter-familles), ni si un résultat validé à 8B se transfère à des échelles supérieures.

**L'expérience à faire en premier.**
Exécuter **l'Expérience 1 corrigée (filtre amont bi-étage $\Phi_{\text{CPU}}$ sur banc conçu à l'aveugle)** — coût exclusivement CPU (`10–30` € [illustratif], `0` GPU, `0` famille consommée). Elle est le verrou économique et logique prioritaire : sans un filtre bi-étage capable de bloquer à la fois les statistiques invalides sous $H_0$ et les martingales dégénérées sans puissance, tout branchement de `I` (avec ou sans modèle pré-entraîné) gaspille le budget GPU et détruit des familles à lecture unique. Immédiatement après réussite de ce filtre — et *avant* toute modification de l'architecture d'idéation ou consommation d'une famille — exécuter l'`Expérience 2` corrigée (plan `2×2` mémoire/naturalité à coût total égal) pour trancher si le LLM dans `I` doit être conservé, puis l'`Expérience 3` corrigée (transfert croisé sur trajectoires honnêtes 8B natives disjointes) pour vérifier si le simulateur amont est valide. Si l'une de ces trois portes échoue, on ne consomme aucune famille de sabotage.

FIN-DE-CELLULE