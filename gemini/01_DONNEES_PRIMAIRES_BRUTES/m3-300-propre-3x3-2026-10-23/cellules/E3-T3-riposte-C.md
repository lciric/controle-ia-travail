# Proposition C · Tour III.3 : Riposte

**Avertissement d'intégrité (Règle 2)** : Les données de l'espèce `claude-opus-5-5` (100 explorateurs et 10 Champions DPP) restent absentes des Annexes 1, 2 et 3 [statut : VÉRIFIÉ sur la pièce], et 19 des 20 champions présents (tous sauf Fable #01) s'arrêtent au milieu d'un mot ou d'une formule avant la balise `FIN-DE-CHAMPION-M3` [statut : OBSERVÉ-NON-AUDITÉ].

---

## (a) Traitement point par point des attaques contre C

### 1. Attaques de l'équipe rouge A (section « Contre la proposition C »)

- **F-C1 & F-C2 (Dégénérescence de $q_{ff}$ dans le premier orthant, saturation de la NCD sur textes courts, et mesure du style de défaut plutôt que du contenu de l'erreur `H4'`)** : **ACCEPTÉE**.
  - *Correction* : Un cosinus sur $\mathbb{R}_+^3$ est borné inférieurement par $0$ et confond le profil stylistique avec l'erreur factuelle ou causale partagée (`H4'`). Nous supprimons $q_{ff} = \text{CosSim}(\mathbf{e}_i,\mathbf{e}_j)(1-\text{NCD})$ et le remplaçons dans le Duel 1 corrigé par la **concordance des erreurs sur items à vérité-terrain** (coefficient $\kappa$ de Cohen / taux de co-validation d'erreurs plantées connues, stratifié à taux de faux rejet $\text{FRR}$ fixé).
- **F-C3 & Évasion contre (1) (Destruction de la sous-tâche $c_k$ par $\Pi_{\perp c_0}$ et canal de fuite `H7`/`H9` via les « variables d'état »)** : **ACCEPTÉE**.
  - *Correction* : L'opérateur $\Pi_{\perp c_0}$ sur texte libre détruit la consigne spécifique ou laisse fuir un verdict dans un champ libre. Nous le remplaçons par une **enveloppe d'état typée à schéma strict** (JSON validé hors-LLM : `{"paper_ids": [str], "metric_name": str, "threshold": float}` sans aucun champ de texte libre) concaténée au bloc immuable $c_0$ injecté par l'orchestrateur Python.
- **F-C4 (Coefficients de $r_i$ non marqués `illustratif` et polarité supposée des 6 têtes `jev-1.14.0`)** : **ACCEPTÉE**.
  - *Correction* : Les coefficients $(1, 2, 2, -3, -2)$ sont marqués `illustratif`. La polarité et le pouvoir discriminant de chaque tête `jev-1.14.0` font l'objet d'un test préalable obligatoire (Expérience 0 ci-dessous) avant tout branchement du filtre d'arrêt.
- **F-C5 & F-C6 (Fuite instrument/évaluation entre `jev` et les duels ; vulnérabilité de VER au « gabarit vide »)** : **TRANSFORMÉE EN TEST**.
  - *Transformation* : Intégrée directement au Duel 3 corrigé : `jev-1.14.0` est banni de la métrique d'évaluation finale au profit d'un **test d'exclusivité causale croisée** (suggestion de A que nous adoptons en le disant) et de l'exécution d'un script d'intervention sur `Llama-3.1-8B-Instruct`, opposés à un contrôle négatif de « gabarit vide ».
- **F-C7 (Absence de taux de faux rejet $\text{FRR}$ fixé à côté du $\text{CFR}$ dans le Duel 1)** : **ACCEPTÉE**.
  - *Correction* : Le Duel 1 corrigé évalue le $\text{CFR}$ à $\text{FRR}$ fixé ($\le 0,10$ [illustratif]) sur des items honnêtes appariés.
- **F-C8 (Deux traitements confondus dans le Duel 2 — anti-troncature et réinjection — et glissement de statut sur l'Annexe 1)** : **ACCEPTÉE**.
  - *Correction* : L'anti-troncature est appliquée uniformément aux deux bras du Duel 2 pour isoler l'effet pur de la réinjection contre `H9`. L'interprétation de la baisse de survie de Fable en Annexe 1 comme une dérive `H9` est rectifiée en **HYPOTHÈSE**.
- **F-C9 & F-C10 (Statuts inflatés sur les log-probabilités de `jev`, l'absence de logs, les modèles hors socle d'Argon #03, et le budget supposé intact)** : **ACCEPTÉE**.
  - *Correction* : Les log-probabilités de `jev-1.14.0`, la cause de l'absence d'Opus et le reliquat exact des plafonds de $100\text{ USD}$ et $20\text{ USD}$ [statut : VÉRIFIÉ comme plafonds initiaux] passent au statut **HYPOTHÈSE**. Les noms de modèles hors socle d'Argon #03 (`Gemini-Flash`, `Claude-3.5-Sonnet`) sont rejetés et remplacés par les seules ressources vérifiées (`gemini-4-argon`, `claude-fable-5-1`, `claude-opus-5-5`, `Llama-3.1-8B/70B`).
- **F-C11 & Évasion contre (4) (Juge Red-Team mouvant et triche sur la nouveauté `zstd` par bruit de surface)** : **ACCEPTÉE**.
  - *Correction* : Le terme de nouveauté `zstd` sur texte brut est supprimé ; la survie $y_m$ est évaluée face à une **archive gelée de tests adverses** et un vérificateur d'exclusivité causale.

### 2. Attaques de l'équipe rouge B (section « Contre la proposition C » et Duel transversal)

- **Protocole B1 (Interdiction de fusionner les propositions)** : **REJETÉE AVEC SA RAISON**.
  - *Raison* : La règle B1 stipule : *« tu ne résumes pas, ne fusionnes pas et n'harmonises pas les autres propositions. Tu les attaques, ou tu t'en sers en le disant »* — où « les autres propositions » désigne explicitement les propositions A et B du Collisionneur 3×3 (« Tu es la proposition C. Les autres propositions portent les lettres A, B »). Or, au tour III.1, nous n'avions ni reçu ni fusionné A ou B ; nous avons sélectionné et combiné des équations issues des *données d'entrée* (les Champions de l'Annexe 3) en les citant nommément, tout en rejetant 15 des 20 champions.
- **Règle 1 (Glissements de statut : vecteur `jev`, mécanisme de troncature amont, et contre-exemple Fable #01 entier avec `Duels = 0.05`)** : **ACCEPTÉE**.
  - *Correction* : Le fait que Fable #01 (CDW) soit entier tout en ayant `Duels = 0.05` [statut : OBSERVÉ-NON-AUDITÉ] réfute notre affirmation selon laquelle la troncature expliquait à elle seule le bas score `Duels` de Fable. La troncature amont et l'effet de la coupure sur `Duels` sont requalifiés en **HYPOTHÈSE**.
- **C-1 & C-2 (Boucle d'auto-évaluation de `jev` et dégénérescence + erreur de typage paire/espèce de $q_{f_i f_j}$)** : **ACCEPTÉE** (voir F-C1, F-C2 et F-C5 ci-dessus : séparation stricte entre `jev` et l'oracle des duels, et remplacement de $q_{ff}$).
- **C-3 (Inertie algébrique du filtre de Wald si $r_{\min} = \min_s r_i^{(s)} \implies \Lambda_i^{(k)} \ge 0 > B_{\text{Wald}}$)** : **ACCEPTÉE**.
  - *Correction* : L'écriture $r_{\min}$ était ambiguë. Nous la remplaçons par une cible de qualité exigée $\tau_{\text{cible}} > 0$ [illustratif] fixée sur le quantile $70\text{ \%}$ [illustratif] d'une cohorte de calibration : chaque étape où $r_i^{(s)} < \tau_{\text{cible}}$ ajoute un incrément strictement négatif, permettant à $\Lambda_i^{(k)}$ de franchir $B_{\text{Wald}} < 0$. Un contrôle négatif vérifie que le taux de mise à mort est $> 0$.
- **C-4 & Scénario d'évasion Brier (Le réplicateur de Brier récompense la prédiction lucide de son propre échec $\mu_m \approx 0, y_m = 0$ et le charabia incompressible)** : **ACCEPTÉE**.
  - *Correction* : Faille mathématique majeure de notre équation (4). Un score de Brier pur $(\mu_m - y_m)^2$ récompense une cellule qui annonce $\mu_m = 0$ et échoue volontairement ($y_m = 0$). Nous remplaçons la mise à jour par un **gain espéré unilatéral** : le terme de récompense est multiplié par l'indicateur de succès $y_m \in \{0,1\}$, soit $R_m = y_m \left(1 - (\mu_m - 1)^2\right) - (1 - y_m)\,\mu_m^2 - \gamma_{\text{coût}} c_m$. Si $y_m = 0$, le gain est $\le 0$ quel que soit $\mu_m$, et nul texte vide ou bruyant ne peut accroître son budget.
- **C-5 (Score de pont $S_0 = C(u)+C(v)-C(u\oplus v)$ non normalisé et biaisé par la longueur)** : **ACCEPTÉE**.
  - *Correction* : Remplacé par la distance d'information normalisée $\text{NCD}(u,v) \in [0,1]$ évaluée à longueur de résumé tronquée à $1\,000$ caractères [illustratif], en cherchant les paires à distance de citation $d_{\text{cit}}(u,v) \ge 4$ [illustratif] mais à compression croisée intermédiaire ($\text{NCD} \in [0,60 ; 0,85]$ [illustratif], évitant à la fois les doublons et le bruit sans rapport).
- **C-6, C-7 & C-8 (Traitements confondus au Duel 2, zones mortes violant B4 dans les 3 duels, reliquat budgétaire inconnu, absence d'Opus, et confusion existence/attribution dans Crossref)** : **ACCEPTÉE**.
  - *Correction* : Dans la section (b) ci-dessous, chaque duel est reformulé avec une **partition binaire exhaustive sans zone morte** ($\theta$ unique : $\ge \theta$ falsifie $H_B$, $< \theta$ falsifie $H_A$), le plan s'adapte au budget *résiduel* mesuré par un appel d'inventaire initial, Opus est isolé derrière un test de disponibilité (`ping`), et Crossref est complété par une vérification d'entailment sur le résumé réel de l'article extrait.
- **Duel transversal de B (Résistance au gabarit vide de 600 tokens sur lorem-ipsum)** : **TRANSFORMÉE EN TEST**.
  - *Transformation* : Intégré comme contrôle négatif éliminatoire du Duel 3 corrigé.

---

## (b) Loi Mère corrigée ($\mathcal{L}^*_{\text{v2}}$) et Expériences Corrigées (Inférence Forte B4 sans zone morte)

### Synthèse des corrections sur $\mathcal{L}^*_{\text{v2}}$ [statut : HYPOTHÈSE]
1. **Anti-`H9` et Anti-`H7` par Enveloppe Typée (remplace Éq. 1)** : La consigne racine $c_0$ est réinjectée par l'orchestrateur Python à chaque profondeur $k$, et l'agent délégant $i$ ne peut transmettre à l'agent $j$ qu'un objet JSON à schéma rigide sans texte libre (`paper_ids` vérifiés dans S2/Crossref, `target_layer` $\in [0, 80]$, `metric_id`). Tout champ hors schéma ou toute génération tronquée (absence de phrase complète avant la balise de fin) est rejetée à $0\text{ USD}$.
2. **Routage Anti-`H4'` par Désaccord Empirique (remplace Éq. 2)** : Au lieu du cosinus sur $\mathbb{R}_+^3$, deux agents $(i,j)$ traitant un pont extraient chacun un graphe dirigé minimal d'hypothèse causale $G_i, G_j$ (variables d'intervention sur `Llama-3.1` $\to$ direction de l'effet sur la métrique). La corrélation intra-espèce est mesurée sur une batterie de 20 items de contrôle contenant des pièges plantés (références hors-sujet, corrélations fallacieuses). Si le taux d'erreur conjointe intra-espèce dépasse l'indépendance à marginales fixées (contrôle emprunté à A, F-B1, en le disant), le vérificateur est forcé d'appartenir à une espèce différente ($f_j \neq f_i$) ou à une échelle de poids différente (`Llama-3.1-8B` vs `70B`).
3. **Arrêt de Wald Calibré (remplace Éq. 3)** : Utilisé uniquement pour les têtes `jev-1.14.0` ayant survécu à l'Expérience 0, avec dérive $\Lambda_i^{(k)} = \sum_{s=1}^k (r_i^{(s)} - \tau_{\text{cible}})$ où $\tau_{\text{cible}}$ est la médiane des textes valides.
4. **Allocation Unilatérale Anti-Échec (remplace Éq. 4)** : La mise à jour budgétaire d'une cellule $m$ vaut $B_m^{(t+1)} \propto B_m^{(t)} \exp\left(\eta \left[ y_m (1 - (\mu_m - 1)^2) - (1 - y_m)\mu_m^2 - \gamma_{\text{coût}} c_m \right]\right)$, où $y_m \in \{0,1\}$ vaut $1$ ssi le protocole survit à l'archive gelée de tests adverses et au vérificateur d'exclusivité causale.

---

### Expérience 0 (Prérequis à 0 USD API) : Calibration de polarité et résistance au gabarit de `jev-1.14.0`
- **Hypothèse $H_A$ (Validité sémantique d'au moins un sous-score de `jev-1.14.0`)** : Sur un corpus équilibré de $30$ textes [illustratif] (les 20 champions + 10 textes synthétiques générés localement par `Llama-3.1-8B-Instruct` incluant 5 « gabarits vides sur lorem-ipsum » et 5 protocoles valides inspirés de Xu et al., `arXiv:2602.00986v2` dont on inverse les signes d'équations ou retire les contrôles sans toucher aux mots-clés), au moins une tête de `jev-1.14.0` affiche une corrélation de rang $|\rho_{\text{Spearman}}| \ge 0,50$ [illustratif] avec la vérité-terrain construite et attribue aux 5 « gabarits vides » un score inférieur à la médiane des protocoles valides.
- **Hypothèse $H_B$ (Capteur purement lexical / vulnérable au gabarit vide)** : Toutes les têtes de `jev-1.14.0` ont $|\rho_{\text{Spearman}}| < 0,50$ [illustratif] avec la vérité-terrain hors-regex, OU au moins une tête attribue aux « gabarits vides sur lorem-ipsum » un score supérieur ou égal à la médiane des protocoles valides.
- **Contrôles négatifs** : (1) 5 textes « gabarits vides » (Duel transversal de B) ; (2) Fable #01 (CDW) tronqué artificiellement aux 19 longueurs des autres champions (contrôle de troncature appariée emprunté à B, en le disant) pour mesurer l'effet mécanique pur de la coupure sur `Duels` et `Contrôles`.
- **Règle de décision sans zone morte** : Si $|\rho| \ge 0,50$ et $\text{Score}(\text{Gabarit vide}) < \text{Médiane}(\text{Valides})$, **$H_B$ est réfutée** (la tête est retenue avec son signe observé dans $\mathcal{L}^*_{\text{v2}}$). Sinon, **$H_A$ est réfutée** et `jev-1.14.0` est banni de la fonction objectif (utilisé uniquement comme log descriptif).

---

### Duel 1 Corrigé : Routage Chimérique contre `H4'` à marginales et $\text{FRR}$ contrôlés
- **Hypothèse $H_A$ (Supériorité du croisement d'espèces contre les erreurs partagées `H4'`)** : Sur une batterie de $40$ propositions expérimentales [illustratif] contenant 20 propositions valides et 20 propositions avec une erreur méthodologique ou d'attribution plantée (DOI réel mais affirmation absente du résumé de l'article, ou confusion corrélation/causalité), un comité chimérique (générateur `gemini-4-argon` vérifié par `claude-fable-5-1`, et réciproquement), calibré pour un taux de faux rejet $\text{FRR} \le 0,15$ [illustratif] sur les 20 propositions valides, présente un excès d'erreurs co-validées $\Delta_{\text{CFR}} = \text{CFR}_{\text{obs}} - \text{CFR}_{\text{indép-marginales}}$ inférieur d'au moins $15\text{ points de pourcentage}$ [illustratif] à celui des monocultures (`Fable-Fable` et `Argon-Argon`) évaluées sur une moitié disjointe du corpus (séparation sélection/évaluation empruntée à A, F-B3).
- **Hypothèse $H_B$ (Équivalence aux marginales près ou corrélation inter-espèces par données partagées)** : À $\text{FRR} \le 0,15$ [illustratif] fixé, l'écart $\Delta_{\text{CFR}}(\text{Mono}) - \Delta_{\text{CFR}}(\text{Chimère}) < 15\text{ points de pourcentage}$ [illustratif].
- **Contrôles négatifs** :
  1. Simulation de Monte-Carlo de $\text{CFR}_{\text{indép-marginales}} = p_{\text{err}}(i) \cdot p_{\text{accept}}(j)$ avec les taux de base réels de chaque agent (contrôle de A, F-B1).
  2. Contraste local à $0\text{ USD}$ entre `Llama-3.1-8B-Instruct` et `Llama-3.1-70B` (mêmes données de pré-entraînement, poids distincts — contrôle de A, F-B2).
- **Falsification binaire exhaustive** : Écart $\ge 15\text{ points}$ $\implies$ **$H_B$ réfutée** ; Écart $< 15\text{ points}$ $\implies$ **$H_A$ réfutée** (l'essaim abandonne le surcoût de traduction chimérique et utilise le modèle unique le plus économique par tâche).

---

### Duel 2 Corrigé : Enveloppe Typée + Réinjection de $c_0$ contre l'érosion `H9` (Anti-troncature isolée)
- **Hypothèse $H_A$ (Préservation de la conformité et de la pertinence par enveloppe typée)** : Sur 20 chaînes de délégation de profondeur $k=5$ [illustratif], lorsque **les deux bras** bénéficient du même garde-fou anti-troncature (relance si la sortie ne se termine pas par une phrase complète avant la balise), le bras $\mathcal{L}^*_{\text{v2}}$ (réinjection de $c_0$ + passage de contexte par schéma JSON strict sans texte libre) obtient à $k=5$ un score de conformité-pertinence conjointe $CP_5 = \text{Conformité\_par\_affirmation}_5 \times \text{Pertinence\_tâche}_5$ supérieur d'au moins $20\text{ points de pourcentage}$ [illustratif] au bras de délégation en texte libre sans réinjection.
- **Hypothèse $H_B$ (Absence d'effet propre ou perte de pertinence par rigidité du schéma)** : À anti-troncature identique, $CP_5(\mathcal{L}^*_{\text{v2}}) - CP_5(\text{Libre}) < 20\text{ points de pourcentage}$ [illustratif].
- **Métrique exacte (normalisée par affirmation et anti-vacuité, suivant A F-B8 et B C-5/C-6)** :
  - $\text{Conformité\_par\_affirmation}$ : proportion d'affirmations factuelles/numériques/bibliographiques correctement balisées, en comptant comme **violation** le sur-marquage (marquer `illustratif` un chiffre vérifié du socle ou `(référence à vérifier)` un article fourni par l'API) et l'absence totale de référence ($0\text{ réf} \implies \text{Conformité} = 0$).
  - $\text{Pertinence\_tâche}$ : proportion des contraintes spécifiques de la sous-tâche $k$ effectivement résolues dans le protocole final (0 si l'agent se contente de recopier $c_0$).
- **Contrôles négatifs** : (1) Sortie égale à l'écho textuel de $c_0$ (doit donner $CP_5 = 0$) ; (2) *Sham injection* en langage naturel (injection d'un texte réglementaire hors-sujet de même longueur en tokens que $c_0$).
- **Falsification binaire exhaustive** : Gain $\ge 20\text{ points}$ et supérieur à la *sham injection* $\implies$ **$H_B$ réfutée** ; Gain $< 20\text{ points}$ ou égal à la *sham injection* $\implies$ **$H_A$ réfutée**.

---

### Duel 3 Corrigé : Allocation Unilatérale + Test d'Exclusivité Causale vs Sélection `jev` Brute (et Test du Gabarit Vide)
- **Hypothèse $H_A$ (Validité causale et exécutabilité sous $\mathcal{L}^*_{\text{v2}}$)** : À budget API égal ($6\text{ USD}$ par bras [illustratif]), les 10 protocoles $\mathcal{M}_1$ sélectionnés par $\mathcal{L}^*_{\text{v2}}$ (gain unilatéral anti-échec + test d'exclusivité croisée) atteignent un taux d'Exécutabilité et d'Exclusivité Causale ($\text{EEC}$) supérieur d'au moins $30\text{ points de pourcentage}$ [illustratif] aux 10 protocoles sélectionnés par le Score Composite `jev-1.14.0` brut + DPP, tout en rejetant $100\text{ \%}$ des « gabarits vides sur lorem-ipsum ».
- **Hypothèse $H_B$ (Suffisance de `jev` brut ou vulnérabilité de $\mathcal{L}^*_{\text{v2}}$ au gabarit)** : $\text{EEC}(\mathcal{L}^*_{\text{v2}}) - \text{EEC}(\text{Jev-Brut}) < 30\text{ points de pourcentage}$ [illustratif] OU au moins un « gabarit vide » reçoit un budget croissant sous $\mathcal{L}^*_{\text{v2}}$.
- **Métrique $\text{EEC}$ (indépendante de `jev` et de la regex)** : Une proposition vaut $\text{EEC} = 1$ ssi :
  1. **Exclusivité causale en aveugle** : Un modèle tiers (`Llama-3.1-70B` local à $0\text{ USD}$) à qui l'on fournit uniquement le protocole expérimental et $H_A$ prédit une direction d'effet sur la métrique (ex. hausse des infractions de $0,49 \to 0,65$) **strictement opposée** à celle qu'il prédit lorsqu'on lui fournit uniquement le protocole et $H_B$.
  2. **Ancrage d'attribution** : Le résumé réel de chaque papier cité (récupéré via l'API S2/arXiv) implique logiquement l'affirmation qui lui est attribuée (vérifié sur `Llama-3.1-70B`).
  3. **Exécution sèche (*dry-run*)** : Les paramètres d'intervention sur `Llama-3.1-8B-Instruct` (couches, neurones, taille d'échantillon) s'exécutent sans erreur de typage sur 2 exemples en GPU local.
- **Contrôles négatifs (issus de A et B)** : (1) 10 « gabarits vides de 600 tokens sur lorem-ipsum » où $H_A$ et $H_B$ prédisent la même issue ; (2) Cellule MAP-Elites « échec lucide » ($\mu_m = 0,05$, sortie vide) ; (3) Contrôle positif : le protocole d'ablation des $< 1\text{ \%}$ de *Value/Dopamine Neurons* de Xu et al. (`arXiv:2602.00986v2`, $-54,9\text{ pts}$ [statut : VÉRIFIÉ]) doit obtenir $\text{EEC} = 1$.
- **Falsification binaire exhaustive** : Écart $\ge 30\text{ points}$ avec $0\text{ \%}$ de gabarit vide accepté et contrôle positif à $1$ $\implies$ **$H_B$ réfutée** ; sinon $\implies$ **$H_A$ réfutée**.

---

## (c) Réponse à la question de l'arbitre en une page : Ce qui est établi, ce qui ne l'est pas, et l'expérience à faire en premier

### 1. Ce qui est établi
- **Sur le socle du projet (`controle-ia`) [statut : VÉRIFIÉ]** : Nous disposons des modèles ouverts `Llama-3.1-8B-Instruct` et `70B` sur GPU A100 80 Go / H200 NVL, d'un accès illimité et gratuit à `jev-1.14.0` et aux API bibliographiques (arXiv, Semantic Scholar, Crossref, Alignment Forum/LessWrong, GitHub), et de quatre ancrages empiriques : le verdict nul des sondes linéaires génériques `P3` sur `(i-a)`, les incidents de délégation *Sol* et *Astra* (OpenAI, oct. 2026), la hausse des infractions sous rejets répétés ($0,49 \to 0,65$, Jhaveri et al., 2026 ; Tagliabue et al., 2026) sans levier par pilotage linéaire dense, et l'existence d'un sous-système parcimonieux ($< 1\text{ \%}$ de *Value/Dopamine Neurons*, Xu et al., `arXiv:2602.00986v2`, $-54,9\text{ pts}$ par ablation). Aucune tête de sabotage ni sonde temps réel n'existe en production.
- **Sur l'exécution $\mathcal{M}_3$ transmise [statut : VÉRIFIÉ sur la pièce / OBSERVÉ-NON-AUDITÉ pour les scores]** :
  1. La cohorte `claude-opus-5-5` est intégralement absente des Annexes 1, 2 et 3 ($0/100$ explorateurs, $0/10$ champions).
  2. Sur les 200 explorateurs restants, seuls $83$ sont marqués « valides » en Annexe 1 ($14/100$ pour `claude-fable-5-1` avec quatre vagues absentes V05, V06, V09, V10 ; $69/100$ pour `gemini-4-argon` avec un score moyen stationnaire entre `0.52` et `0.80`).
  3. Sur les 20 Champions DPP transmis en Annexe 3, **19 sur 20 sont coupés au milieu d'un mot ou d'une équation** juste avant la balise `FIN-DE-CHAMPION-M3`. Seul Fable #01 (CDW) est syntaxiquement complet, et son score `Duels` vaut pourtant `0.05` — ce qui prouve sur pièce que la coupure du texte ne suffit pas à expliquer la faiblesse du score `Duels` chez Fable.
  4. Le Score Composite `jev-1.14.0` observé en Annexe 2 est fortement tiré par la colonne `Rigueur Jev` (jusqu'à `2.07` sur Argon V05 k=042) alors que les colonnes `Contrôles` (`0.04` à `0.11`) et `Duels` (sauf Argon V01 k=003 à `0.68`) restent très basses et qu'aucun des 20 champions n'applique les règles de marquage `(référence à vérifier)` ou `illustratif`.

### 2. Ce qui n'est pas établi [statut : HYPOTHÈSE]
- **Sur les instruments et ressources** : (1) Le reliquat réel des plafonds de $100\text{ USD}$ (Anthropic) et $20\text{ USD}$ (Gemini) après le tour $\mathcal{M}_3$ ; (2) La raison technique de l'absence de `claude-opus-5-5` et du rejet des $217$ explorateurs manquants ; (3) La formule exacte, la polarité (haut = bon ou mauvais) et la résistance au *Goodhart* lexical ou au « gabarit vide » des 6 sous-scores de `jev-1.14.0`.
- **Sur la dynamique des essaims (`H4'`, `H5`, `H7`, `H9`)** : (1) Il n'est pas établi que les 10 vagues de déflation améliorent la qualité ou la diversité par rapport à une seule vague stratifiée par cône ; (2) Il n'est pas établi que les erreurs de `claude-fable-5-1` et `gemini-4-argon` soient moins corrélées entre espèces qu'au sein d'une même espèce une fois contrôlés les taux d'erreur de base (marginales) et le corpus de pré-entraînement partagé ; (3) Il n'est pas établi qu'une loi d'auto-organisation complexe ($\mathcal{L}^*$) batte un pipeline séquentiel simple couplé à des vérifications programmatiques déterministes (API S2/Crossref + test d'exclusivité causale sur `Llama-3.1-70B`).

### 3. L'expérience à faire en premier (Coût API : 0 USD ; Durée : < 1 heure sur CPU + 1× GPU local `Llama-3.1-8B/70B`)

Avant d'engager le moindre dollar du budget API résiduel dans $\mathcal{M}_2$ ou $\mathcal{M}_1$, il faut exécuter **l'Expérience 0 (Calibration en aveugle de `jev-1.14.0`, de la troncature et du vérificateur d'exclusivité causale)** :
1. **Protocole** : Prendre Fable #01 (seul texte entier) et générer localement sur `Llama-3.1-8B-Instruct` 5 protocoles expérimentaux complets et valides (calqués sur l'ablation des neurones de valeur de Xu et al. et la dérive $0,49 \to 0,65$ sous rejets répétés). Appliquer quatre transformations contrôlées :
   - *(T1 — Troncature appariée)* : Couper ces 6 textes complets aux longueurs exactes des 19 champions tronqués de l'Annexe 3.
   - *(T2 — Sabotage causal)* : Rendre $H_A$ et $H_B$ identiques dans leurs prédictions ou inverser le signe du seuil de décision, en conservant 100 % du vocabulaire mathématique et des balises.
   - *(T3 — Dégonflage d'éponymes)* : Remplacer les noms propres mathématiques (*Wyner, Parisi, Cugliandolo-Kurchan, Bockstein*) par des termes génériques (*méthode A, couplage B*) en gardant les équations et les duels intacts.
   - *(T4 — Gabarit vide de 600 tokens)* : Coller les en-têtes `H_A`, `H_B`, `Contrôle négatif`, `(référence à vérifier)` et `illustratif` sur 10 textes *lorem-ipsum* hors-sujet.
2. **Mesure simultanée à 0 USD** : Passer les textes $(T0, T1, T2, T3, T4)$ dans `jev-1.14.0` ET dans notre vérificateur d'exclusivité causale en aveugle sur `Llama-3.1-70B`.
3. **Décision immédiate (Inférence forte B4)** :
   - T1 mesure exactement la part de la chute de `Duels` due à la troncature amont.
   - Toute tête de `jev-1.14.0` qui chute plus sous T3 (retrait d'éponymes) que sous T2 (sabotage causal) ou qui accepte T4 (gabarit vide) est **disqualifiée comme fonction objectif**. L'essaim attaque alors $\mathcal{M}_2 \to \mathcal{M}_1$ gouverné uniquement par les filtres survivants, l'enveloppe JSON typée anti-`H9` et le test d'exclusivité causale sur `Llama-3.1-70B`.

FIN-DE-CELLULE