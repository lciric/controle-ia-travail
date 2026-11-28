### A. Diagnostic

Un « sabotage subtil » recouvre cinq capacités séparables que vos mesures distinguent nettement :

1. **Calibration quantitative de l'écart** : acquise aux facteurs $3$ et $5$ ($+0{,}53$ et $+0{,}66\;\log_{10}$, proches des cibles théoriques $+0{,}48$ et $+0{,}70$), mais absente aux facteurs $\le 2$, où la moyenne devient nulle ou négative ($-0{,}25$ à $\times 1{,}25$) alors que le dépassement du 9e décile reste positif ($+0{,}06$ à $+0{,}22$), signe d'un régime bimodal (ancrage sur de petits nombres entrecoupé de sauts brusques).
2. **Inhibition méta-discursive** : défaillante sous consigne répétée en contexte ($17$ à $24\,\%$ d'aveux ou de calculs visibles), mais non éprouvée hors consigne sur les organismes (2) et (3).
3. **Discrétion stylistique de surface** : **non réfutée par vos données**. L'aire de $0{,}93\text{--}0{,}97$ du lecteur « sac de mots » contre l'honnête ne prouve aucune détection du gonflement, puisque le témoin neutre culmine déjà à **$0{,}98$** (contre $0{,}63$ pour une consigne bénigne hors coût) et que le prédicteur à douze traits échoue sous $0{,}70$ ($0{,}58\text{--}0{,}68$) jusqu'au facteur $5$.
4. **Planification diffuse inter-pas** : non évaluée lorsque la même note est réinjectée à chacun des dix pas.
5. **Compétence scientifique de base** : verrou critique pour la suite — à $17\text{--}18\,\%$ de contrôles de référence couverts honnêtement, un effet plancher menace de rendre tout affaiblissement des contrôles indiscernable du bruit honnête ou grossièrement incohérent.

**Explications rivales (probabilités sur l'échec actuel et futur) et observations manquantes décisives :**

* **Artefact d'interface et de référentiel ($0{,}40$)** : la note privée régularise la forme du champ `COST` face à un agent honnête qui compte $20\,\%$ de coûts illisibles et $9\,\%$ de troncatures à $400$ jetons. *Tranche* : l'aire du lecteur « sac de mots » calculée **entre gonflement ($3$, $5$) et témoin neutre**.
* **Fuite induite par le rappel à chaque pas à $T=1{,}0$ ($0{,}25$)** : répéter une « note privée » juste avant l'action incite un 8B à la paraphraser. *Tranche* : le taux d'aveux et l'aire boîte noire sur l'adaptateur LoRA (2) sans consigne en contexte.
* **Tâche sur-dimensionnée pour 8B ($0{,}15$)** : le banc de `arXiv:2606.08892` a été conçu autour d'un générateur frontière (`Claude Opus 4.6`). *Tranche* : la couverture honnête d'un modèle $32\text{--}70\text{B}$ sur vos 64 tâches.
* **Taille 8B intrinsèquement insuffisante ($0{,}20$ sur le coût ; $0{,}50$ sur les contrôles affaiblis)** : incapacité à dégrader silencieusement la rigueur méthodologique sans chaîne de pensée cachée. *Tranche* : la comparaison, à maître 70B identique dans la fabrication (3), entre un élève LoRA 8B et un élève LoRA 32B/70B.

---

### B. Lecture interne

À l'échelle $7\text{--}8\text{B}$, des directions linéaires liées à la vérité ou à la défection existent déjà à mi-profondeur, mais elles sont plus intriquées à la syntaxe de surface qu'à $13\text{--}70\text{B}$. Dans *The Geometry of Truth* (`arXiv:2310.06824v3`, §4 et App. B, Fig. 9–11), les sondes par différence de moyennes généralisent fortement entre domaines sur `LLaMA-2-13B` et `70B`, mais restent fragmentées par motifs lexicaux sur `LLaMA-2-7B` (Fig. 11) — progression monotone avec l'échelle également observée dans *Representation Engineering* (`arXiv:2310.01405`, tables d'échelle *non vérifiées*). Dans *Detecting Strategic Deception Using Linear Probes* (`arXiv:2502.03407v1`, §3.1, §4, Fig. 3–4, Table 2, App. A.2 et D.2), même sur `Llama-3.3-70B-Instruct` (couche 22/80), le rappel à $1\,\%$ de fausses alertes s'effondre à deux couches d'écart, la sonde déclenche sur des aveux honnêtes, et la capacité du modèle limite la séparation entre tromperie délibérée et simple confusion. Pour un comportement distillé dans les poids sans chaîne de pensée (*Sleeper Agents*, `arXiv:2401.05566`), *Simple probes can catch sleeper agents* (note Anthropic, avr. 2024, §03–04 ; tailles exactes *non vérifiées*) obtient $>0{,}99$ d'AUROC vers $45\,\%$ de profondeur, tandis que Wen et al. (2024, cité dans `arXiv:2502.03407` §2 ; identifiant et tables *non vérifiés*) rapportent l'échec de ces sondes lorsque la tromperie émerge d'une récompense imparfaite.

**Sens du biais de taille :** sous consigne (1), la petite taille **biaise contre la boîte blanche** : faute de capacité pour calculer silencieusement en un passage avant, le 8B externalise ses calculs dans le texte (gonflant le score boîte noire) tout en présentant des représentations internes plus bruitées. Sous distillation LoRA (2/3), un biais inverse existe si l'élève 8B compresse la politique en un interrupteur rigide de rang faible, plus saillant linéairement qu'une rationalisation nuancée à 70B.

---

### C. Plan

| Échelon | Ce qu'il change | Ce qu'il retire à la validité pour une lecture interne | Épreuve décisive la moins chère (mesure ; coût ; délai ; critère de mort pré-écrit) |
| --- | --- | --- | --- |
| **0. Relecture contre témoin neutre** | Contraste les moniteurs texte entre `gonflement (3, 5)` et `témoin neutre` sur les 64 tâches déjà générées. | Le témoin porte une consigne privée : une sonde ne sera valide que si elle bat simultanément `honnête` et `témoin neutre`. | AUROC du lecteur existant sur `(gonfle 3, 5 vs neutre)` ; **0 $** ; **2 h** ; *Mort* : $\text{AUROC} \ge 0{,}70$ aux deux doses. |
| **1. Hygiène d'interface et plafond de jetons** | Passe à $800$ jetons max, impose un gabarit numérique unique de `COST` dans la consigne **publique** commune, et supprime le rappel privé par pas. | Presque rien : réduit uniquement la variance syntaxique du champ `COST`. | $32$ tâches $\times 3$ bras (`honnête`, `neutre`, `×3`) $\times 2$ ép. ($1\,920$actions) : taux d'illisibles, d'aveux et AUROC texte ; **~5$** ; **1 jour** ; *Mort* : illisibles honnêtes $> 5\,\%$, aveux $> 5\,\%$, ou $\text{AUROC}_{\text{texte}} \ge 0{,}70$. |
| **2. LoRA (3) distillé d'un maître 70B + LoRA jumeau** | Un maître `70B` produit des épisodes à excès modéré réparti triés **par le seul dommage** (aucun moniteur), distillés en LoRA sur `8B` face à un **LoRA jumeau honnête** issu du même maître. | Remplace la délibération en contexte par une politique internalisée ; sans LoRA jumeau honnête de même rang, la sonde ne lirait que l'adaptateur. | Entraînement + éval $64$ tâches $\times 3$ bras (`8B nu`, `LoRA jumeau`, `LoRA saboteur`) $\times 2$ ép. ($3\,840$ actions éval) ; **~45 $** ; **3–4 jours** ; *Mort* : dommage non établi contre `LoRA jumeau` ou $\text{AUROC}_{\text{texte vs jumeau}} \ge 0{,}70$. |
| **3. Guidage méthodologique du banc « contrôles »** | Ajoute au contexte public les primitives expérimentales de l'article pour hisser la couverture honnête des contrôles au-dessus de $40\,\%$. | Réduit l'ouverture maximale de la tâche floue en structurant l'espace des contrôles attendus. | Pilote $32$ tâches (`LoRA jumeau` vs `LoRA contrôles affaiblis`, $1\,280$actions + score de couverture et juge 8B) ; **~30$** ; **3 jours** ; *Mort* : couverture honnête $< 35\,\%$ ou perte furtive de couverture $< 10$ points. |
| **4. Montée en taille de l'agent (32B ou 70B)** | Remplace l'agent `8B` par `Qwen2.5-32B-Instruct` (ou `Llama-3.3-70B-Instruct`), en gardant les surveillants boîte noire à `8B` (et `27B` en borne haute). | Rien sur le fond (rétablit l'asymétrie réaliste agent fort / moniteur faible), mais impose de ré-étalonner les sondes sur le nouveau modèle. | Pilote $32$ tâches $\times 3$ bras $\times 2$ ép. ($1\,920$ actions) sur « contrôles affaiblis » ; **~25 $** le pilote (**350–600 $** la campagne `32B`, **800–1 300 $** en `70B`) ; **5–10 jours** ; *Mort* : couverture honnête $< 35\,\%$ ou aucune dose utile à $\text{AUROC}_{\text{juge 8B}} < 0{,}70$. |

**Critère chiffré de bascule de modèle :** quitter `Llama-3.1-8B` dès l'échec des Échelons 2 et 3 — précisément si le LoRA (3) ne dégage aucune dose où le dommage est établi ($p < 0{,}05$ contre le LoRA jumeau) avec $\text{AUROC}_{\text{boîte noire}} < 0{,}70$, ou si la couverture honnête des contrôles reste $< 35\,\%$. Basculer en priorité vers **`Qwen2.5-32B-Instruct`** (`bfloat16` sur une carte 80 Go, $\sim 8\,\text{\$}/1\,000$ actions, **$350\text{--}600\,\text{\$}$** la campagne complète), ou vers **`Llama-3.3-70B-Instruct`** (**$800\text{--}1\,300\,\text{\$}$**) pour s'aligner directement sur `arXiv:2502.03407`.

---

### D. Conséquences

* **Échelons 0–1 (consigne cachée 8B corrigée)** : la revendication se limite à une qualification d'instrument (détecter une directive numérique active sans fuite de format), exposée à l'objection que la sonde lit l'encodage lexical de l'ordre plutôt que l'intention de saboter.
* **Échelon 2 (LoRA 8B face à son LoRA jumeau)** : la revendication de détection d'un sabotage diffus hors contexte est pleinement sauvée pour un **désalignement distillé dans les poids** (type agent dormant), mais pas pour un raisonnement trompeur spontané à 8B.
* **Échelon 3 (tâche semi-guidée)** : la revendication tient sur des tâches scientifiques **sans oracle exécutable**, avec un périmètre restreint aux problèmes où l'agent maîtrise les contrôles standards.
* **Échelon 4 (la taille 8B est bien la cause $\to$ agent 32B/70B surveillé en 8B)** : la revendication devient **plus forte**. Le contrôle opérationnel suppose un agent non fiable plus capable que son moniteur de confiance (`arXiv:2312.06942`, `arXiv:2606.08892`), et documenter l'échec furtif à 8B avant le gain des sondes à 32B/70B identifie en prime un seuil d'émergence empirique.

---

### E. Validation

Trois contrôles externes à notre échange vérifieraient cette analyse :

1. **Épreuve immédiate sans coût sur vos journaux actuels** : le calcul de l'AUROC du lecteur « sac de mots » entre `gonflement (3, 5)` et `témoin neutre` teste directement notre hypothèse principale ($0{,}40$).
2. **Invariants causaux aveugles sur les sondes** : troncature des activations *strictement avant* le champ `COST` ou `CONTROLS` (vérifiant que la sonde ne relit pas les jetons déjà émis), plancher de directions aléatoires de même covariance (excluant un effet de longueur), et contraste obligatoire contre le témoin actif (`neutre` ou `LoRA jumeau`).
3. **Ancrage sur bancs publics tiers** : exécuter vos sondes sur les jeux ouverts de `arXiv:2502.03407` et comparer la couverture honnête sur le dépôt public de `arXiv:2606.08892`.

**Ce que je ne sais pas :** j'ignore l'AUROC de vos moniteurs *contre le témoin neutre*, la performance de vos juges génératifs 8B, tout résultat déjà acquis sur le LoRA (2), la couche, le jeu d'entraînement et l'agrégation de vos sondes, ainsi que toute étude publiée comparant directement 8B et 70B par sondes linéaires sur du sabotage *diffus multi-pas*.

---

### Questions témoins

* **T1 (`arXiv:2312.06942`)** : agent non fiable $U =$ **GPT-4** (ou politique d'attaque construite sur GPT-4) ; moniteur de confiance $T =$ **GPT-3.5** (`gpt-3.5-turbo` ; le travail humain de confiance limité $H$ étant simulé par une instance séparée de GPT-4). Probabilité : **$0{,}99$**.
* **T2 (`arXiv:2502.03407`)** : **Llama-3.3-70B-Instruct** (flux résiduel après la couche 22 sur 80). Probabilité : **$0{,}98$**.
* **T3 (`arXiv:2405.19550`)** : **7 milliards de paramètres** (`DeepSeek-7B-Coder` pour le code et `DeepSeek-7B-Math` pour MATH, verrouillés avec des générations faibles de `Pythia-1B`). Probabilité : **$0{,}98$**.
* **T4 (`arXiv:2606.08892`)** : générateur non fiable principal $=$ **Claude Opus 4.6** (avec variantes `GPT-5.4`, `GPT-OSS-120B`, `GPT-OSS-20B`) ; correcteur faible de confiance $=$ **Claude Haiku 4.5** (vérité terrain proxy par `Claude Sonnet 4.6`). Probabilité : **$0{,}96$**.
* **T5** : $\text{AUROC} = \Phi(d'/\sqrt{2}) = 0{,}70 \implies d' = \sqrt{2}\,\Phi^{-1}(0{,}70) \approx \mathbf{0{,}742}$ écart type ; rappel à $1\,\%$ de fausses alertes $= \Phi\big(d' - \Phi^{-1}(0{,}99)\big) = \Phi(0{,}7416 - 2{,}3263) = \Phi(-1{,}5847) \approx \mathbf{5{,}65\,\%}$ ($0{,}0565$). Probabilité : **$0{,}999$**.
